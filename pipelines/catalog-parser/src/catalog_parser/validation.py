from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from .postgres_loader import ENTITY_SPECS, EntitySpec, load_dataset
from .quality_rules import QUALITY_RULESET_VERSION, program_name_issue


ROOT = Path(__file__).resolve().parents[4]
SCHEMA_DIR = ROOT / "docs/schemas"
SCHEMA_FILES = {
    "source_registry": "source_registry.schema.json",
    "catalog_entries": "catalog_entries.schema.json",
    "url_manifest": "url_manifest.schema.json",
    "quick_facts": "quick_facts.schema.json",
    "entity_contexts": "entity_contexts.schema.json",
}
CATALOG_AUDIT_VERSION = QUALITY_RULESET_VERSION
GRADUATE_DEGREES = {"SM", "MEng", "MArch", "MCP", "MASc", "MBA", "MBAn", "MFin", "MSMS", "PhD", "ScD"}
DOMAIN_IN_PATH = re.compile(
    r"^/([a-z0-9-]+(?:\.[a-z0-9-]+)*\.(?:edu|org|com|net|gov|ca|ac\.uk|edu\.au|edu\.sg))(?:/|$)",
    re.IGNORECASE,
)
DECLARED_TOTAL_LABELS = re.compile(
    r"(?:total\s+degree\s+programs?(?:\s*\(including\s+minors?\))?|degree\s+programs?\s+total|"
    r"catalog\s+entries\s+total|学位项目总计[^|]*(?:含\s*minors?|含辅修))",
    re.IGNORECASE,
)


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


def _url_integrity_issue(value: Any) -> str | None:
    if not is_valid_http_url(value):
        return "invalid_http_url"
    parsed = urlparse(str(value))
    host = (parsed.hostname or "").lower()
    for match in DOMAIN_IN_PATH.finditer(parsed.path):
        embedded = match.group(1).lower()
        if embedded != host and not host.endswith(f".{embedded}"):
            return "embedded_domain_in_path"
    return None


def _descriptor_mentions_degree(row: dict[str, Any], degree: str) -> bool:
    descriptor = " ".join(
        str(row.get(field) or "")
        for field in ("program_name", "degree_full_name")
    ).lower()
    patterns = {
        "SM": r"\b(?:m\.?s|s\.?m|m\.?a|master)\b",
        "MEng": r"\bm\.?eng\b|master of engineering",
        "MArch": r"\bm\.?arch\b|master of architecture",
        "MBA": r"\bmba\b|master of business administration",
        "PhD": r"\bph\.?d\b|doctor of philosophy",
        "Minor": r"\bminor\b|辅修",
    }
    pattern = patterns.get(degree)
    return bool(pattern and re.search(pattern, descriptor))


def declared_catalog_expectation(markdown_text: str | None) -> dict[str, Any] | None:
    if not markdown_text:
        return None
    expectations: list[dict[str, Any]] = []
    for line_number, line in enumerate(markdown_text.splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [re.sub(r"[*_`]", "", cell).strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not DECLARED_TOTAL_LABELS.search(cells[0]):
            continue
        number = re.search(r"\b(\d{1,5})\b", cells[1].replace(",", ""))
        if number:
            expectations.append({"label": cells[0], "expected_count": int(number.group(1)), "line": line_number})
    return max(expectations, key=lambda item: item["expected_count"]) if expectations else None


def parser_failure_audit(error: str) -> dict[str, Any] | None:
    if error not in {
        "Deep v2 Markdown produced zero catalog entries",
        "Deep v2 Markdown must include a data capture date",
    }:
        return None
    return {
        "audit_status": "failed",
        "audit_version": CATALOG_AUDIT_VERSION,
        "matched_rule_ids": ["CAT-COVERAGE-001"],
        "failures": ["catalog_completeness"],
        "warnings": [],
        "checks": {
            "catalog_completeness": {
                "status": "failed",
                "reason": error,
                "actual_count": 0,
            }
        },
        "before_counts": {},
        "after_counts": {},
    }


def catalog_quality_audit(
    dataset: dict[str, list[dict[str, Any]]],
    *,
    markdown_text: str | None = None,
    parser_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    entity_issues: list[dict[str, Any]] = []
    for row in dataset["catalog_entries"]:
        reason = program_name_issue(row.get("program_name"))
        if reason:
            entity_issues.append({"rule_id": "CAT-ENTITY-001", "record_id": row.get("entry_id"), "value": row.get("program_name"), "reason": reason})

    url_issues: list[dict[str, Any]] = []
    placeholder_urls: list[dict[str, Any]] = []
    for entity_name in ("source_registry", "catalog_entries"):
        id_field = "source_id" if entity_name == "source_registry" else "entry_id"
        for row in dataset[entity_name]:
            for field in ("canonical_url", "source_url"):
                if field not in row:
                    continue
                reason = _url_integrity_issue(row.get(field))
                if reason:
                    url_issues.append({"rule_id": "CAT-URL-001", "entity": entity_name, "record_id": row.get(id_field), "field": field, "url": row.get(field), "reason": reason})
                host = (urlparse(str(row.get(field) or "")).hostname or "").lower()
                if host in {"example.com", "example.edu"} or host.endswith(".example"):
                    placeholder_urls.append({"entity": entity_name, "record_id": row.get(id_field), "field": field, "url": row.get(field)})

    degree_issues: list[dict[str, Any]] = []
    for row in dataset["catalog_entries"]:
        degree = row.get("degree_level")
        level = row.get("level")
        url = str(row.get("source_url") or "").lower()
        reason = None
        if level == "undergraduate" and degree in GRADUATE_DEGREES:
            reason = "graduate_degree_marked_undergraduate"
        elif level == "graduate" and degree in {"SB", "Minor"}:
            reason = "undergraduate_degree_marked_graduate"
        url_slug = urlparse(url).path.rstrip("/").rsplit("/", 1)[-1]
        if not reason and re.search(r"(?:^|[-_])minor(?:[-_]|$)", url_slug) and degree != "Minor":
            reason = "minor_url_degree_mismatch"
        elif (
            not reason
            and re.search(r"(?:^|[-_])phd(?:[-_]|$)", url_slug)
            and degree != "PhD"
            and not (_descriptor_mentions_degree(row, degree) and re.search(r"\bph\.?d\b", str(row.get("program_name") or "").lower()))
        ):
            reason = "phd_url_degree_mismatch"
        if reason:
            degree_issues.append({"rule_id": "CAT-DEGREE-001", "record_id": row.get("entry_id"), "degree_level": degree, "level": level, "source_url": row.get("source_url"), "reason": reason})

    source_counts: dict[str, int] = {}
    for row in dataset["catalog_entries"]:
        source_url = str(row.get("source_url") or "")
        source_counts[source_url] = source_counts.get(source_url, 0) + 1
    dominant_source_count = max(source_counts.values(), default=0)
    source_specificity_ratio = dominant_source_count / len(dataset["catalog_entries"]) if dataset["catalog_entries"] else 0.0
    generic_source_warning = len(dataset["catalog_entries"]) >= 5 and source_specificity_ratio >= 0.8

    expectation = declared_catalog_expectation(markdown_text)
    actual_count = len(dataset["catalog_entries"])
    completeness_status = "skipped"
    completeness_details: dict[str, Any] = {"actual_count": actual_count, "expectation": expectation}
    if expectation:
        ratio = actual_count / expectation["expected_count"] if expectation["expected_count"] else 1.0
        completeness_status = "failed" if ratio < 0.5 else "needs_review" if ratio < 0.9 else "passed"
        completeness_details["coverage_ratio"] = ratio
    elif actual_count == 0:
        completeness_status = "failed"
    elif actual_count < 5:
        completeness_status = "needs_review"
    if parser_summary:
        completeness_details["parser_summary"] = {
            key: parser_summary.get(key)
            for key in ("candidate_tables", "catalog_tables", "rejected_tables", "rejected_catalog_rows")
            if key in parser_summary
        }

    checks = {
        "entity_validity": {"status": "failed" if entity_issues else "passed", "issue_count": len(entity_issues), "issues": entity_issues[:100]},
        "url_integrity": {"status": "failed" if url_issues else "passed", "issue_count": len(url_issues), "issues": url_issues[:100], "placeholder_warnings": placeholder_urls[:100]},
        "degree_consistency": {"status": "failed" if degree_issues else "passed", "issue_count": len(degree_issues), "issues": degree_issues[:100]},
        "source_specificity": {
            "status": "needs_review" if generic_source_warning else "passed",
            "dominant_source_ratio": source_specificity_ratio,
            "distinct_source_count": len(source_counts),
            "dominant_source_url": max(source_counts, key=source_counts.get) if source_counts else None,
        },
        "catalog_completeness": {"status": completeness_status, **completeness_details},
    }
    failures = [name for name, check in checks.items() if check["status"] == "failed"]
    warnings = [name for name, check in checks.items() if check["status"] == "needs_review"]
    if placeholder_urls:
        warnings.append("placeholder_urls")
    matched_rule_ids: list[str] = []
    if entity_issues:
        matched_rule_ids.append("CAT-ENTITY-001")
    if url_issues:
        matched_rule_ids.append("CAT-URL-001")
    if degree_issues:
        matched_rule_ids.append("CAT-DEGREE-001")
    if completeness_status in {"failed", "needs_review"}:
        matched_rule_ids.append("CAT-COVERAGE-001")
    if generic_source_warning:
        matched_rule_ids.append("CAT-SOURCE-001")
    return {
        "audit_status": "failed" if failures else "needs_review" if warnings else "passed",
        "audit_version": CATALOG_AUDIT_VERSION,
        "matched_rule_ids": matched_rule_ids,
        "failures": failures,
        "warnings": sorted(set(warnings)),
        "checks": checks,
        "before_counts": {},
        "after_counts": {name: len(rows) for name, rows in dataset.items()},
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


def validate_school(
    data_dir: Path,
    university_id: str,
    *,
    markdown_text: str | None = None,
    parser_summary: dict[str, Any] | None = None,
) -> dict[str, Any]:
    dataset = load_dataset(data_dir, university_id)
    checks = {
        "schema": validate_json_schemas(dataset),
        "required_fields": required_field_completeness(dataset),
        "url_legal_rate": url_legal_rate(dataset),
        "cross_references": cross_reference_checks(dataset),
        "catalog_quality": catalog_quality_audit(
            dataset,
            markdown_text=markdown_text,
            parser_summary=parser_summary,
        ),
        "mit_reconciliation": mit_reconciliation(dataset, university_id),
    }
    failures = [
        name
        for name, check in checks.items()
        if (check.get("status") or check.get("audit_status")) not in {"passed", "needs_review", "skipped"}
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
