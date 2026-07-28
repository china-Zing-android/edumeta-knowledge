from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from catalog_parser.disciplines import enrich_catalog_entries
from catalog_parser.entity_contexts import build_entity_contexts
from catalog_parser.quality_rules import QUALITY_RULESET_VERSION


@dataclass(frozen=True)
class IndexSpec:
    entity_name: str
    file_name: str | None
    id_field: str
    alias: str
    mapping_path: Path


ROOT = Path(__file__).resolve().parents[4]

INDEX_SPECS: tuple[IndexSpec, ...] = (
    IndexSpec("universities", None, "university_id", "l1_universities_current", ROOT / "infra/opensearch/l1_universities_mapping.json"),
    IndexSpec("catalog_entries", "catalog_entries.jsonl", "entry_id", "l1_catalog_entries_current", ROOT / "infra/opensearch/l1_catalog_entries_mapping.json"),
    IndexSpec("quick_facts", "quick_facts.jsonl", "fact_id", "l1_quick_facts_current", ROOT / "infra/opensearch/l1_quick_facts_mapping.json"),
    IndexSpec("sources", "url_manifest.jsonl", "source_id", "l1_sources_current", ROOT / "infra/opensearch/l1_url_manifest_mapping.json"),
    IndexSpec("entity_contexts", "entity_contexts.jsonl", "context_id", "l1_entity_contexts_current", ROOT / "infra/opensearch/l1_entity_contexts_mapping.json"),
)


def _new_client(opensearch_url: str) -> Any:
    try:
        from opensearchpy import OpenSearch
    except ImportError as exc:
        raise RuntimeError("opensearch-py is required for OpenSearch publishing") from exc
    return OpenSearch(
        opensearch_url,
        timeout=float(os.getenv("OPENSEARCH_PUBLISH_TIMEOUT_SECONDS", "120")),
        max_retries=1,
        retry_on_timeout=True,
    )


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _dataset_version(records: list[dict[str, Any]]) -> str:
    versions = {str(row.get("dataset_version") or "unknown") for row in records}
    if len(versions) != 1:
        raise ValueError(f"records must have exactly one dataset_version, got {sorted(versions)}")
    return next(iter(versions))


def _mapping_schema_version(mapping_path: Path) -> str:
    mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
    version = str(mapping.get("mappings", {}).get("_meta", {}).get("edumeta_schema_version") or "").strip()
    if not version or not re.fullmatch(r"[A-Za-z0-9_-]+", version):
        raise ValueError(f"mapping must define a safe edumeta_schema_version: {mapping_path}")
    return version


def _university_record(
    university_id: str,
    catalog: list[dict[str, Any]],
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    metadata = metadata or {}
    dataset_version = _dataset_version(catalog)
    aliases = {university_id, university_id.upper(), *(metadata.get("aliases") or [])}
    university_name = metadata.get("university_name") or (
        "Massachusetts Institute of Technology" if university_id == "mit" else university_id.replace("_", " ").title()
    )
    aliases.add(university_name)
    return {
        "university_id": university_id,
        "university_name": university_name,
        "aliases": sorted(aliases),
        "country_code": metadata.get("country_code"),
        "region": metadata.get("region"),
        "school_tier": metadata.get("school_tier") or "core",
        "dataset_version": dataset_version,
        "is_current": True,
        "status": "active",
    }


def load_publish_plan(
    data_dir: Path,
    university_id: str,
    *,
    university_metadata: dict[str, Any] | None = None,
) -> dict[str, dict[str, Any]]:
    catalog = read_jsonl(data_dir / "catalog_entries.jsonl")
    enrich_catalog_entries(catalog)
    catalog_version = _dataset_version(catalog)
    metadata = university_metadata or {}
    quick_facts = read_jsonl(data_dir / "quick_facts.jsonl")
    sources = read_jsonl(data_dir / "url_manifest.jsonl")
    context_path = data_dir / "entity_contexts.jsonl"
    entity_contexts = (
        read_jsonl(context_path)
        if context_path.exists()
        else build_entity_contexts(
            university_id=university_id,
            university_name=metadata.get("university_name") or (
                "Massachusetts Institute of Technology" if university_id == "mit" else university_id.replace("_", " ").title()
            ),
            country_code=metadata.get("country_code"),
            region=metadata.get("region"),
            catalog_entries=catalog,
            quick_facts=quick_facts,
            source_registry=sources,
            dataset_version=catalog_version,
        )
    )
    for record in entity_contexts:
        record["is_current"] = True
    for record in catalog:
        record.update({
            "university_name": metadata.get("university_name") or (
                "Massachusetts Institute of Technology" if university_id == "mit" else university_id.replace("_", " ").title()
            ),
            "country_code": metadata.get("country_code"),
            "region": metadata.get("region"),
            "school_tier": metadata.get("school_tier") or "core",
            "is_current": True,
        })
    plan: dict[str, dict[str, Any]] = {}
    for spec in INDEX_SPECS:
        if spec.file_name is None:
            records = [_university_record(university_id, catalog, metadata)]
        elif spec.entity_name == "catalog_entries":
            records = catalog
        elif spec.entity_name == "quick_facts":
            records = quick_facts
        elif spec.entity_name == "sources":
            records = sources
        elif spec.entity_name == "entity_contexts":
            records = entity_contexts
        else:
            records = read_jsonl(data_dir / spec.file_name)
        wrong_school = [row.get(spec.id_field) for row in records if row.get("university_id") != university_id]
        if wrong_school:
            raise ValueError(f"{spec.file_name or spec.entity_name} contains records for another university: {wrong_school[:3]}")
        ids = [str(row[spec.id_field]) for row in records]
        if len(ids) != len(set(ids)):
            raise ValueError(f"{spec.file_name or spec.entity_name} contains duplicate {spec.id_field}")
        version = _dataset_version(records) if records else catalog_version
        schema_version = _mapping_schema_version(spec.mapping_path)
        write_index = spec.alias.removesuffix("_current") + f"_v{schema_version}"
        plan[spec.entity_name] = {
            "spec": spec,
            "records": records,
            "count": len(records),
            "alias": spec.alias,
            "write_index": write_index,
            "dataset_version": version,
            "schema_version": schema_version,
            "mapping_path": str(spec.mapping_path),
        }
    return plan


def dry_run_report(data_dir: Path, university_id: str) -> dict[str, Any]:
    plan = load_publish_plan(data_dir, university_id)
    return {
        "mode": "dry_run",
        "university_id": university_id,
        "data_dir": str(data_dir),
        "indexes": {
            entity: {key: item[key] for key in ("count", "alias", "write_index", "dataset_version", "mapping_path")}
            for entity, item in plan.items()
        },
        "status": "validated",
    }


def versioned_document_id(record: dict[str, Any], id_field: str) -> str:
    return f"{record['university_id']}:{record['dataset_version']}:{record[id_field]}"


def bulk_actions(index_name: str, id_field: str, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {
            "_op_type": "index",
            "_index": index_name,
            "_id": versioned_document_id(record, id_field),
            "_source": record,
        }
        for record in records
    ]


def _ensure_index_and_alias(client: Any, item: dict[str, Any]) -> None:
    index_name = item["write_index"]
    mapping = json.loads(Path(item["mapping_path"]).read_text(encoding="utf-8"))
    expected_version = str(mapping["mappings"]["_meta"]["edumeta_schema_version"])
    timeout_seconds = float(os.getenv("OPENSEARCH_PUBLISH_TIMEOUT_SECONDS", "120"))
    created = not client.indices.exists(index=index_name)
    if created:
        client.indices.create(index=index_name, body=mapping)
        health = client.cluster.health(
            index=index_name,
            wait_for_status="yellow",
            wait_for_no_initializing_shards=True,
            timeout=f"{timeout_seconds:g}s",
            request_timeout=timeout_seconds + 5,
        )
        if health.get("timed_out") or health.get("status") not in {"yellow", "green"}:
            raise RuntimeError(f"OpenSearch index did not become ready: {index_name}")
    else:
        current = client.indices.get_mapping(index=index_name)
        current_version = (
            current.get(index_name, {})
            .get("mappings", {})
            .get("_meta", {})
            .get("edumeta_schema_version")
        )
        if str(current_version or "") != expected_version:
            raise RuntimeError(
                f"OpenSearch physical index schema mismatch: {index_name} "
                f"has {current_version!r}, expected {expected_version!r}"
            )
    try:
        aliases = client.indices.get_alias(name=item["alias"])
    except Exception as exc:  # opensearch-py NotFoundError shape varies by version
        if getattr(exc, "status_code", None) != 404:
            raise
        aliases = {}
    legacy_indexes = sorted(name for name in aliases if name != index_name)
    if legacy_indexes:
        source_count = int(client.count(index=",".join(legacy_indexes))["count"])
        target_count = int(client.count(index=index_name)["count"])
        if target_count != source_count:
            task = client.reindex(
                body={
                    "source": {"index": legacy_indexes},
                    "dest": {"index": index_name},
                },
                wait_for_completion=False,
                request_timeout=10,
            )
            task_id = task.get("task")
            if not task_id:
                raise RuntimeError(f"OpenSearch schema migration did not return a task id for {item['alias']}")
            task_result = client.tasks.get(
                task_id=task_id,
                wait_for_completion=True,
                timeout=f"{timeout_seconds:g}s",
                request_timeout=timeout_seconds + 5,
            )
            if not task_result.get("completed"):
                raise RuntimeError(
                    f"OpenSearch schema migration task did not finish for {item['alias']}: {task_id}"
                )
            if task_result.get("error"):
                raise RuntimeError(
                    f"OpenSearch schema migration task failed for {item['alias']}: {task_result['error']}"
                )
            response = task_result.get("response") or {}
            failures = response.get("failures") or []
            if response.get("timed_out") or failures:
                raise RuntimeError(
                    f"OpenSearch schema migration failed for {item['alias']}: {failures[:3]}"
                )
            client.indices.refresh(index=index_name)
            target_count = int(client.count(index=index_name)["count"])
        if target_count != source_count:
            raise RuntimeError(
                f"OpenSearch schema migration count mismatch for {item['alias']}: "
                f"source={source_count}, target={target_count}"
            )
        actions = [
            {"remove": {"index": legacy_index, "alias": item["alias"]}}
            for legacy_index in legacy_indexes
        ]
        if index_name not in aliases:
            actions.append({"add": {"index": index_name, "alias": item["alias"]}})
        client.indices.update_aliases(body={"actions": actions})
    elif index_name not in aliases:
        client.indices.put_alias(index=index_name, name=item["alias"])


def publish_school(
    data_dir: Path,
    university_id: str,
    opensearch_url: str,
    *,
    university_metadata: dict[str, Any] | None = None,
    activate: bool = True,
    client: Any | None = None,
    bulk_writer: Any | None = None,
) -> dict[str, Any]:
    plan = load_publish_plan(data_dir, university_id, university_metadata=university_metadata)
    if client is None or bulk_writer is None:
        try:
            from opensearchpy import helpers
        except ImportError as exc:
            raise RuntimeError("opensearch-py is required for OpenSearch publishing") from exc
        client = client or _new_client(opensearch_url)
        bulk_writer = bulk_writer or (
            lambda target, actions: helpers.bulk(target, actions, raise_on_error=False)
        )
    published: dict[str, Any] = {}
    write_indexes: set[str] = set()
    for entity, item in plan.items():
        spec: IndexSpec = item["spec"]
        _ensure_index_and_alias(client, item)
        if entity in {"universities", "catalog_entries", "entity_contexts"}:
            for record in item["records"]:
                record["is_current"] = False
        client.delete_by_query(
            index=item["write_index"],
            body={"query": {"bool": {"filter": [
                {"term": {"university_id": university_id}},
                {"term": {"dataset_version": item["dataset_version"]}},
            ]}}},
            conflicts="proceed",
            refresh=False,
        )
        ok_count, errors = bulk_writer(
            client,
            bulk_actions(item["write_index"], spec.id_field, item["records"]),
        )
        if errors:
            raise RuntimeError(f"OpenSearch bulk indexing failed for {entity}: {errors[:3]}")
        write_indexes.add(item["write_index"])
        published[entity] = {
            "count": ok_count,
            "alias": item["alias"],
            "write_index": item["write_index"],
            "dataset_version": item["dataset_version"],
        }
    client.indices.refresh(index=",".join(sorted(write_indexes)))
    for entity, item in plan.items():
        count = client.count(
            index=item["alias"],
            body={"query": {"bool": {"filter": [
                {"term": {"university_id": university_id}},
                {"term": {"dataset_version": item["dataset_version"]}},
            ]}}},
        )["count"]
        if count != item["count"]:
            raise RuntimeError(f"OpenSearch count verification failed for {entity}: expected {item['count']}, got {count}")
    if activate:
        activate_school_documents(client, plan, university_id)
    return {
        "mode": "opensearch",
        "university_id": university_id,
        "indexes": published,
        "status": "published" if activate else "staged",
    }


def activate_school_documents(client: Any, plan: dict[str, dict[str, Any]], university_id: str) -> None:
    aliases: set[str] = set()
    for entity in ("universities", "catalog_entries", "entity_contexts"):
        item = plan[entity]
        aliases.add(item["alias"])
        dataset_version = item["dataset_version"]
        client.update_by_query(
            index=item["alias"],
            body={
                "script": {"source": "ctx._source.is_current = true", "lang": "painless"},
                "query": {"bool": {"filter": [
                    {"term": {"university_id": university_id}},
                    {"term": {"dataset_version": dataset_version}},
                ]}},
            },
            conflicts="proceed",
            refresh=False,
        )
        client.update_by_query(
            index=item["alias"],
            body={
                "script": {"source": "ctx._source.is_current = false", "lang": "painless"},
                "query": {"bool": {
                    "filter": [{"term": {"university_id": university_id}}],
                    "must_not": [{"term": {"dataset_version": dataset_version}}],
                }},
            },
            conflicts="proceed",
            refresh=False,
        )
    client.indices.refresh(index=",".join(sorted(aliases)))


def activate_published_school(
    data_dir: Path,
    university_id: str,
    opensearch_url: str,
    *,
    university_metadata: dict[str, Any] | None = None,
    client: Any | None = None,
) -> None:
    plan = load_publish_plan(data_dir, university_id, university_metadata=university_metadata)
    if client is None:
        client = _new_client(opensearch_url)
    activate_school_documents(client, plan, university_id)


def audit_staged_school(
    data_dir: Path,
    university_id: str,
    opensearch_url: str,
    *,
    university_metadata: dict[str, Any] | None = None,
    client: Any | None = None,
    max_probes: int = 5,
) -> dict[str, Any]:
    plan = load_publish_plan(data_dir, university_id, university_metadata=university_metadata)
    if client is None:
        client = _new_client(opensearch_url)

    catalog_item = plan["catalog_entries"]
    selected: list[dict[str, Any]] = []
    seen_degrees: set[str] = set()
    for row in sorted(catalog_item["records"], key=lambda item: (str(item.get("degree_level")), str(item.get("program_name")))):
        degree = str(row.get("degree_level") or "")
        if degree in seen_degrees and len(selected) < max_probes:
            continue
        selected.append(row)
        seen_degrees.add(degree)
        if len(selected) >= max_probes:
            break
    if not selected:
        selected = catalog_item["records"][:max_probes]

    probe_results: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for row in selected:
        filters = [
            {"term": {"university_id": university_id}},
            {"term": {"dataset_version": catalog_item["dataset_version"]}},
            {"term": {"status": "active"}},
            {"term": {"level": row.get("level")}},
            {"term": {"degree_level": row.get("degree_level")}},
        ]
        response = client.search(index=catalog_item["alias"], body={
            "size": 1,
            "track_total_hits": False,
            "query": {"bool": {
                "filter": filters,
                "should": [
                    {"term": {"entry_id": {"value": row["entry_id"], "boost": 50}}},
                    {"match_phrase": {"program_name": {"query": row["program_name"], "boost": 10}}},
                ],
                "minimum_should_match": 1,
            }},
        })
        hits = response.get("hits", {}).get("hits", [])
        actual_id = (hits[0].get("_source") or {}).get("entry_id") if hits else None
        passed = actual_id == row["entry_id"]
        result = {"query": row["program_name"], "expected_entry_id": row["entry_id"], "actual_entry_id": actual_id, "passed": passed}
        probe_results.append(result)
        if not passed:
            failures.append(result)

    negative_response = client.search(index=catalog_item["alias"], body={
        "size": 1,
        "track_total_hits": False,
        "query": {"bool": {
            "filter": [
                {"term": {"university_id": university_id}},
                {"term": {"dataset_version": catalog_item["dataset_version"]}},
            ],
            "must": [{"match_phrase": {"program_name": "__edumeta_nonexistent_program__"}}],
        }},
    })
    negative_hits = negative_response.get("hits", {}).get("hits", [])
    if negative_hits:
        failures.append({"query": "__edumeta_nonexistent_program__", "reason": "negative_probe_returned_match"})

    checks = {
        "retrieval_regression": {
            "status": "failed" if failures else "passed",
            "probe_count": len(probe_results) + 1,
            "probes": probe_results,
            "negative_probe_passed": not negative_hits,
            "failures": failures,
        }
    }
    return {
        "audit_status": "failed" if failures else "passed",
        "audit_version": QUALITY_RULESET_VERSION,
        "matched_rule_ids": ["RET-SCOPE-001"] if failures else [],
        "checks": checks,
        "failures": ["retrieval_regression"] if failures else [],
        "warnings": [],
        "record_ids": [row["entry_id"] for row in selected],
        "before_counts": {},
        "after_counts": {name: item["count"] for name, item in plan.items()},
    }
