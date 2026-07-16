from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from catalog_parser.disciplines import enrich_catalog_entries
from catalog_parser.entity_contexts import build_entity_contexts


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


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _dataset_version(records: list[dict[str, Any]]) -> str:
    versions = {str(row.get("dataset_version") or "unknown") for row in records}
    if len(versions) != 1:
        raise ValueError(f"records must have exactly one dataset_version, got {sorted(versions)}")
    return next(iter(versions))


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
        write_index = spec.alias.removesuffix("_current") + "_v1"
        plan[spec.entity_name] = {
            "spec": spec,
            "records": records,
            "count": len(records),
            "alias": spec.alias,
            "write_index": write_index,
            "dataset_version": version,
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
    if not client.indices.exists(index=index_name):
        client.indices.create(index=index_name, body=mapping)
    else:
        client.indices.put_mapping(index=index_name, body={"properties": mapping.get("mappings", {}).get("properties", {})})
    try:
        aliases = client.indices.get_alias(name=item["alias"])
    except Exception as exc:  # opensearch-py NotFoundError shape varies by version
        if getattr(exc, "status_code", None) != 404:
            raise
        aliases = {}
    if index_name not in aliases:
        client.indices.put_alias(index=index_name, name=item["alias"])


def publish_school(
    data_dir: Path,
    university_id: str,
    opensearch_url: str,
    *,
    university_metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    plan = load_publish_plan(data_dir, university_id, university_metadata=university_metadata)
    try:
        from opensearchpy import OpenSearch, helpers
    except ImportError as exc:
        raise RuntimeError("opensearch-py is required for OpenSearch publishing") from exc

    client = OpenSearch(opensearch_url)
    published: dict[str, Any] = {}
    for entity, item in plan.items():
        spec: IndexSpec = item["spec"]
        _ensure_index_and_alias(client, item)
        if entity in {"universities", "catalog_entries", "entity_contexts"}:
            client.update_by_query(
                index=item["alias"],
                body={
                    "script": {"source": "ctx._source.is_current = false", "lang": "painless"},
                    "query": {"term": {"university_id": university_id}},
                },
                conflicts="proceed",
                refresh=True,
            )
        client.delete_by_query(
            index=item["write_index"],
            body={"query": {"bool": {"filter": [
                {"term": {"university_id": university_id}},
                {"term": {"dataset_version": item["dataset_version"]}},
            ]}}},
            conflicts="proceed",
            refresh=True,
        )
        ok_count, errors = helpers.bulk(
            client,
            bulk_actions(item["write_index"], spec.id_field, item["records"]),
            raise_on_error=False,
        )
        if errors:
            raise RuntimeError(f"OpenSearch bulk indexing failed for {entity}: {errors[:3]}")
        client.indices.refresh(index=item["write_index"])
        count = client.count(
            index=item["alias"],
            body={"query": {"bool": {"filter": [
                {"term": {"university_id": university_id}},
                {"term": {"dataset_version": item["dataset_version"]}},
            ]}}},
        )["count"]
        if count != item["count"]:
            raise RuntimeError(f"OpenSearch count verification failed for {entity}: expected {item['count']}, got {count}")
        published[entity] = {
            "count": ok_count,
            "alias": item["alias"],
            "write_index": item["write_index"],
            "dataset_version": item["dataset_version"],
        }
    return {"mode": "opensearch", "university_id": university_id, "indexes": published, "status": "published"}
