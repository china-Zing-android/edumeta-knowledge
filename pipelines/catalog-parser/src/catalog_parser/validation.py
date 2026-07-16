from __future__ import annotations

import json
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .postgres_loader import ENTITY_SPECS, EntitySpec, load_dataset


ROOT = Path(__file__).resolve().parents[4]
SCHEMA_DIR = ROOT / "docs/schemas"
SCHEMA_FILES = {
    "source_registry": "source_registry.schema.json",
    "catalog_entries": "catalog_entries.schema.json",
    "url_manifest": "url_manifest.schema.json",
    "quick_facts": "quick_facts.schema.json",
    "entity_contexts": "entity_contexts.schema.json",
}


def load_schema(entity_name: str) -> dict[str, Any]:
    return json.loads((SCHEMA_DIR / SCHEMA_FILES[entity_name]).read_text(encoding="utf-8"))


def validate_json_schemas(dataset: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    try:
        from jsonschema import Draft202012Validator, FormatChecker
    except ImportError as exc:
        raise RuntimeError("jsonschema is required for validate-school. Install project dependencies first.") from exc

    errors: list[dict[str, Any]] = []
    for spec in ENTITY_SPECS:
        schema = load_schema(spec.name)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        for index, record in enumerate(dataset[spec.name], start=1):
            for error in sorted(validator.iter_errors(record), key=lambda item: item.path):
                errors.append(
                    {
                        "entity": spec.name,
                        "file": spec.file_name,
                        "line": index,
                        "record_id": record.get(spec.primary_key),
                        "path": ".".join(str(part) for part in error.path),
                        "message": error.message,
                    }
                )
    return {
        "status": "passed" if not errors else "failed",
        "error_count": len(errors),
        "errors": errors[:100],
        "truncated": len(errors) > 100,
    }


def required_field_completeness(dataset: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    total = 0
    missing: list[dict[str, Any]] = []
    for spec in ENTITY_SPECS:
        for record in dataset[spec.name]:
            total += len(spec.required_columns)
            for column in spec.required_columns:
                if column not in record or record[column] is None:
                    missing.append(
                        {
                            "entity": spec.name,
                            "record_id": record.get(spec.primary_key),
                            "field": column,
                        }
                    )
    present = total - len(missing)
    rate = present / total if total else 1.0
    return {
        "status": "passed" if not missing else "failed",
        "total_required_values": total,
        "missing_count": len(missing),
        "complete_count": present,
        "complete_rate": rate,
        "missing": missing[:100],
        "truncated": len(missing) > 100,
    }


def is_valid_http_url(value: Any) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def url_legal_rate(dataset: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    checked: list[dict[str, str]] = []
    for spec in ENTITY_SPECS:
        for record in dataset[spec.name]:
            for field in ("source_url", "canonical_url"):
                if field in record:
                    checked.append(
                        {
                            "entity": spec.name,
                            "record_id": str(record.get(spec.primary_key)),
                            "field": field,
                            "url": record.get(field),
                        }
                    )
    invalid = [item for item in checked if not is_valid_http_url(item["url"])]
    legal = len(checked) - len(invalid)
    rate = legal / len(checked) if checked else 1.0
    return {
        "status": "passed" if rate >= 0.99 else "failed",
        "total": len(checked),
        "legal": legal,
        "invalid_count": len(invalid),
        "legal_rate": rate,
        "threshold": 0.99,
        "invalid": invalid[:100],
        "truncated": len(invalid) > 100,
    }


def index_records(spec: EntitySpec, rows: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    return {str(row[spec.primary_key]): row for row in rows}


def cross_reference_checks(dataset: dict[str, list[dict[str, Any]]]) -> dict[str, Any]:
    source_ids = {row["source_id"] for row in dataset["source_registry"]}
    entry_ids = {row["entry_id"] for row in dataset["catalog_entries"]}
    errors: list[dict[str, Any]] = []
    for row in dataset["catalog_entries"]:
        if row["source_id"] not in source_ids:
            errors.append({"entity": "catalog_entries", "record_id": row["entry_id"], "field": "source_id", "missing_id": row["source_id"]})
    for row in dataset["url_manifest"]:
        if row["source_id"] not in source_ids:
            errors.append({"entity": "url_manifest", "record_id": row["url_id"], "field": "source_id", "missing_id": row["source_id"]})
        for entry_id in row.get("entry_ids", []):
            if entry_id not in entry_ids:
                errors.append({"entity": "url_manifest", "record_id": row["url_id"], "field": "entry_ids", "missing_id": entry_id})
    for row in dataset["quick_facts"]:
        if row["source_id"] not in source_ids:
            errors.append({"entity": "quick_facts", "record_id": row["fact_id"], "field": "source_id", "missing_id": row["source_id"]})
        if row.get("entry_id") and row["entry_id"] not in entry_ids:
            errors.append({"entity": "quick_facts", "record_id": row["fact_id"], "field": "entry_id", "missing_id": row["entry_id"]})
    for row in dataset["source_registry"]:
        for entry_id in row.get("entry_ids", []):
            if entry_id not in entry_ids:
                errors.append({"entity": "source_registry", "record_id": row["source_id"], "field": "entry_ids", "missing_id": entry_id})
    for row in dataset["entity_contexts"]:
        context_id = row["context_id"]
        entry_id = row.get("entry_id")
        if row.get("entity_type") == "program" and entry_id not in entry_ids:
            errors.append({"entity": "entity_contexts", "record_id": context_id, "field": "entry_id", "missing_id": entry_id})
        for source_id in row.get("source_ids", []):
            if source_id not in source_ids:
                errors.append({"entity": "entity_contexts", "record_id": context_id, "field": "source_ids", "missing_id": source_id})
        for topic in row.get("available_topics", []):
            for source_id in topic.get("source_ids", []):
                if source_id not in source_ids:
                    errors.append({"entity": "entity_contexts", "record_id": context_id, "field": "available_topics.source_ids", "missing_id": source_id})
        for related in row.get("related_entities", []):
            if related.get("entity_type") == "program":
                related_entry_id = related.get("entry_id") or related.get("entity_id")
                if related_entry_id not in entry_ids:
                    errors.append({"entity": "entity_contexts", "record_id": context_id, "field": "related_entities.entry_id", "missing_id": related_entry_id})
            for source_id in related.get("source_ids", []):
                if source_id not in source_ids:
                    errors.append({"entity": "entity_contexts", "record_id": context_id, "field": "related_entities.source_ids", "missing_id": source_id})
    return {
        "status": "passed" if not errors else "failed",
        "error_count": len(errors),
        "errors": errors[:100],
        "truncated": len(errors) > 100,
    }


def mit_reconciliation(dataset: dict[str, list[dict[str, Any]]], university_id: str) -> dict[str, Any]:
    if university_id != "mit":
        return {"status": "skipped", "reason": "MIT-only reconciliation"}
    catalog = dataset["catalog_entries"]
    sb = sum(1 for row in catalog if row.get("degree_level") == "SB")
    minor = sum(1 for row in catalog if row.get("degree_level") == "Minor")
    graduate = sum(1 for row in catalog if row.get("level") == "graduate")
    total = len(catalog)
    passed = (sb, minor, graduate, total) == (55, 17, 85, 157)
    return {
        "status": "passed" if passed else "failed",
        "expected": {"sb": 55, "minor": 17, "graduate": 85, "total": 157},
        "actual": {"sb": sb, "minor": minor, "graduate": graduate, "total": total},
    }


def validate_school(data_dir: Path, university_id: str) -> dict[str, Any]:
    dataset = load_dataset(data_dir, university_id)
    checks = {
        "schema": validate_json_schemas(dataset),
        "required_fields": required_field_completeness(dataset),
        "url_legal_rate": url_legal_rate(dataset),
        "cross_references": cross_reference_checks(dataset),
        "mit_reconciliation": mit_reconciliation(dataset, university_id),
    }
    failures = [
        name
        for name, check in checks.items()
        if check.get("status") not in {"passed", "skipped"}
    ]
    return {
        "mode": "validate_school",
        "status": "passed" if not failures else "failed",
        "university_id": university_id,
        "data_dir": str(data_dir),
        "counts": {name: len(rows) for name, rows in dataset.items()},
        "failures": failures,
        "checks": checks,
    }


def write_validation_report(path: Path, report: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
