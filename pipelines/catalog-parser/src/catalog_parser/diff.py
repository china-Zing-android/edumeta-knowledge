from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .postgres_loader import ENTITY_SPECS, EntitySpec, load_dataset, record_hash


HASH_IGNORED_FIELDS = {
    "capture_date",
    "dataset_version",
    "source_version",
    "last_verified",
    "content_hash",
    "weknora_content_hash",
    "weknora_collection_id",
    "weknora_knowledge_id",
    "weknora_document_id",
    "weknora_chunk_ids",
    "weknora_import_job_id",
    "weknora_import_status",
    "crawl_status",
    "parser_status",
    "import_status",
    "import_error",
    "error_message",
}


def normalized_record(record: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in record.items() if key not in HASH_IGNORED_FIELDS}


def normalized_record_hash(record: dict[str, Any]) -> str:
    return record_hash(normalized_record(record))


def records_by_id(spec: EntitySpec, records: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(record[spec.primary_key]): record for record in records}


def diff_entity(spec: EntitySpec, previous_records: list[dict[str, Any]], current_records: list[dict[str, Any]]) -> dict[str, Any]:
    previous_by_id = records_by_id(spec, previous_records)
    current_by_id = records_by_id(spec, current_records)
    previous_ids = set(previous_by_id)
    current_ids = set(current_by_id)
    added = sorted(current_ids - previous_ids)
    removed = sorted(previous_ids - current_ids)
    changed: list[str] = []
    unchanged: list[str] = []
    changed_hashes: dict[str, dict[str, str]] = {}
    for record_id in sorted(previous_ids & current_ids):
        previous_hash = normalized_record_hash(previous_by_id[record_id])
        current_hash = normalized_record_hash(current_by_id[record_id])
        if previous_hash == current_hash:
            unchanged.append(record_id)
        else:
            changed.append(record_id)
            changed_hashes[record_id] = {"previous": previous_hash, "current": current_hash}
    removed_active = [
        record_id
        for record_id in removed
        if previous_by_id[record_id].get("status") not in {"inactive", "deprecated", "superseded"}
    ]
    return {
        "entity": spec.name,
        "primary_key": spec.primary_key,
        "added_ids": added,
        "changed_ids": changed,
        "removed_ids": removed,
        "removed_active_ids": sorted(removed_active),
        "unchanged": len(unchanged),
        "counts": {
            "previous": len(previous_records),
            "current": len(current_records),
            "added": len(added),
            "changed": len(changed),
            "removed": len(removed),
            "removed_active": len(removed_active),
            "unchanged": len(unchanged),
        },
        "changed_hashes": changed_hashes,
    }


def _collect_source_ids(dataset: dict[str, list[dict[str, Any]]], ids_by_entity: dict[str, set[str]]) -> set[str]:
    source_ids: set[str] = set(ids_by_entity.get("source_registry", set()))
    for row in dataset.get("url_manifest", []):
        if row.get("url_id") in ids_by_entity.get("url_manifest", set()) and row.get("source_id"):
            source_ids.add(str(row["source_id"]))
    for row in dataset.get("catalog_entries", []):
        if row.get("entry_id") in ids_by_entity.get("catalog_entries", set()) and row.get("source_id"):
            source_ids.add(str(row["source_id"]))
    for row in dataset.get("quick_facts", []):
        if row.get("fact_id") in ids_by_entity.get("quick_facts", set()) and row.get("source_id"):
            source_ids.add(str(row["source_id"]))
    return source_ids


def _collect_entry_ids(dataset: dict[str, list[dict[str, Any]]], ids_by_entity: dict[str, set[str]]) -> set[str]:
    entry_ids: set[str] = set(ids_by_entity.get("catalog_entries", set()))
    for row in dataset.get("url_manifest", []):
        if row.get("url_id") in ids_by_entity.get("url_manifest", set()):
            entry_ids.update(str(item) for item in row.get("entry_ids", []) if item)
    return entry_ids


def diff_school(
    previous_data_dir: Path,
    current_data_dir: Path,
    university_id: str,
    *,
    allow_active_removal: bool = False,
) -> dict[str, Any]:
    previous = load_dataset(previous_data_dir, university_id)
    current = load_dataset(current_data_dir, university_id)
    entity_reports = {spec.name: diff_entity(spec, previous[spec.name], current[spec.name]) for spec in ENTITY_SPECS}
    changed_or_added_ids = {
        name: set(report["added_ids"]) | set(report["changed_ids"])
        for name, report in entity_reports.items()
    }
    removed_ids = {name: set(report["removed_ids"]) for name, report in entity_reports.items()}
    affected_source_ids = sorted(
        _collect_source_ids(current, changed_or_added_ids)
        | _collect_source_ids(previous, removed_ids)
    )
    affected_source_urls: list[dict[str, str]] = []
    seen_source_urls: set[str] = set()
    for dataset in (previous, current):
        for source in dataset.get("source_registry", []):
            source_id = str(source.get("source_id") or "")
            url = str(source.get("canonical_url") or source.get("source_url") or "")
            if source_id in affected_source_ids and url and url not in seen_source_urls:
                seen_source_urls.add(url)
                affected_source_urls.append({"source_id": source_id, "url": url})
    affected_entry_ids = sorted(
        _collect_entry_ids(current, changed_or_added_ids)
        | _collect_entry_ids(previous, removed_ids)
    )
    affected_fact_ids = sorted(changed_or_added_ids.get("quick_facts", set()) | removed_ids.get("quick_facts", set()))
    affected_url_ids = sorted(changed_or_added_ids.get("url_manifest", set()) | removed_ids.get("url_manifest", set()))
    affected_context_ids = sorted(changed_or_added_ids.get("entity_contexts", set()) | removed_ids.get("entity_contexts", set()))
    reimport_source_ids = sorted(
        set(entity_reports["source_registry"]["added_ids"])
        | set(entity_reports["source_registry"]["changed_ids"])
        | _collect_source_ids(current, {"url_manifest": changed_or_added_ids.get("url_manifest", set())})
    )
    blocking_failures: list[str] = []
    if not allow_active_removal:
        for report in entity_reports.values():
            if report["removed_active_ids"]:
                blocking_failures.append(
                    f"{report['entity']} has physically removed active records: {', '.join(report['removed_active_ids'][:10])}"
                )
    change_count = sum(report["counts"]["added"] + report["counts"]["changed"] + report["counts"]["removed"] for report in entity_reports.values())
    return {
        "status": "failed" if blocking_failures else ("changed" if change_count else "unchanged"),
        "university_id": university_id,
        "previous_data_dir": str(previous_data_dir),
        "current_data_dir": str(current_data_dir),
        "blocking_failures": blocking_failures,
        "change_count": change_count,
        "entities": entity_reports,
        "affected": {
            "source_ids": affected_source_ids,
            "source_urls": sorted(affected_source_urls, key=lambda item: (item["source_id"], item["url"])),
            "entry_ids": affected_entry_ids,
            "fact_ids": affected_fact_ids,
            "url_ids": affected_url_ids,
            "context_ids": affected_context_ids,
        },
        "weknora_reimport_source_ids": reimport_source_ids,
        "single_source_update": len(affected_source_ids) <= 1 and change_count > 0,
        "publishable": not blocking_failures,
    }


def write_diff_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
