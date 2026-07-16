from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from .disciplines import enrich_catalog_entries
from .entity_contexts import build_entity_contexts
from .markdown_sources import canonicalize_url, is_valid_http_url
from .mit_parser import (
    ParseResult,
    add_catalog_entry,
    add_source,
    add_markdown_prose_sources,
    cleanup_markdown,
    extract_capture_date,
    normalize_fact_value,
    stable_id,
    table_rows,
)


class StructuredMarkdownContractError(ValueError):
    pass


CATALOG_REQUIRED = {"school", "department", "level", "degree_level", "program_name", "source_url"}
FACT_REQUIRED = {"fact_type", "fact_key", "raw_value", "source_url"}
FACT_TYPES = {
    "deadline",
    "application_fee",
    "fee_waiver",
    "gre_gmat_policy",
    "english_requirement",
    "tuition",
    "cost_of_attendance",
    "funding_model",
    "application_platform",
    "test_code",
    "financial_aid_policy",
    "admission_policy",
}
DEGREE_LEVELS = {
    "SB",
    "Minor",
    "SM",
    "MEng",
    "MArch",
    "MCP",
    "MASc",
    "MBA",
    "MBAn",
    "MFin",
    "MSMS",
    "PhD",
    "ScD",
    "Certificate",
    "Other",
}


def _metadata_value(text: str, key: str) -> str | None:
    pattern = re.compile(rf"^\s*\*\*{re.escape(key)}\*\*:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
    match = pattern.search(text)
    return cleanup_markdown(match.group(1)) if match else None


def _dataset_version(text: str, university_id: str, capture_date: str) -> str:
    configured = _metadata_value(text, "Dataset version")
    if configured:
        return configured
    compact_date = capture_date.replace("-", "") if capture_date != "unknown" else "unknown"
    return f"{university_id}_{compact_date}_v1"


def _normalize_header(value: str) -> str:
    value = cleanup_markdown(value).lower()
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"[^a-z0-9_]+", "_", value)
    return value.strip("_")


def _row_dicts(lines: list[str], start_index: int) -> list[dict[str, str]]:
    rows = table_rows(lines, start_index)
    if len(rows) < 2:
        return []
    headers = [_normalize_header(cell) for cell in rows[0]]
    result: list[dict[str, str]] = []
    for cells in rows[1:]:
        row = {headers[index]: cleanup_markdown(cells[index]) for index in range(min(len(headers), len(cells)))}
        result.append(row)
    return result


def _split_list(value: str | None, default: list[str]) -> list[str]:
    if not value:
        return default
    items = [cleanup_markdown(item) for item in re.split(r"[,;]", value) if cleanup_markdown(item)]
    return items or default


def _bool_value(value: str | None, default: bool = True) -> bool:
    if value is None or value == "":
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "official"}


def _int_value(value: str | None, default: int = 1) -> int:
    if not value:
        return default
    try:
        parsed = int(value)
    except ValueError:
        return default
    return max(parsed, 1)


def _url_type(row: dict[str, str], level: str) -> str:
    configured = row.get("url_type")
    if configured:
        return configured
    return "degree_chart" if level == "undergraduate" else "program_admission"


def _level(value: str) -> str:
    normalized = value.strip().lower()
    aliases = {
        "undergrad": "undergraduate",
        "ug": "undergraduate",
        "grad": "graduate",
        "nondegree": "non_degree",
        "non-degree": "non_degree",
    }
    return aliases.get(normalized, normalized)


def _degree_level(value: str) -> str:
    cleaned = cleanup_markdown(value)
    return cleaned if cleaned in DEGREE_LEVELS else "Other"


def _validate_table(name: str, row: dict[str, str], required: set[str]) -> None:
    missing = sorted(field for field in required if not row.get(field))
    if missing:
        raise StructuredMarkdownContractError(f"{name} row is missing required fields: {', '.join(missing)}")


def _apply_source_overrides(source_registry_by_id: dict[str, dict[str, Any]], url_manifest_by_id: dict[str, dict[str, Any]], source_id: str, row: dict[str, str]) -> None:
    url_id = stable_id("url", source_id)
    for target in (source_registry_by_id.get(source_id), url_manifest_by_id.get(url_id)):
        if not target:
            continue
        target["official_source"] = _bool_value(row.get("official_source"), True)
        target["priority"] = _int_value(row.get("priority"), 1)


def parse_structured_markdown(university_id: str, path: Path) -> ParseResult:
    text = path.read_text(encoding="utf-8")
    declared_university_id = _metadata_value(text, "University ID")
    if declared_university_id and declared_university_id.lower() != university_id.lower():
        raise StructuredMarkdownContractError(
            f"University ID mismatch: CLI requested {university_id!r}, document declares {declared_university_id!r}."
        )
    capture_date = extract_capture_date(text)
    if capture_date == "unknown":
        raise StructuredMarkdownContractError("Structured Markdown must declare **Data capture date**: YYYY-MM-DD.")
    dataset_version = _dataset_version(text, university_id, capture_date)
    university_name = _metadata_value(text, "University name") or university_id.upper()
    country_code = (_metadata_value(text, "Country code") or "").upper() or None
    region = _metadata_value(text, "Region")
    aliases = _split_list(_metadata_value(text, "Aliases"), [])

    lines = text.splitlines()
    source_registry_by_id: dict[str, dict[str, Any]] = {}
    url_manifest_by_id: dict[str, dict[str, Any]] = {}
    catalog_entries: list[dict[str, Any]] = []
    quick_facts: list[dict[str, Any]] = []
    catalog_entry_by_program_name: dict[str, dict[str, Any]] = {}
    catalog_tables = 0
    fact_tables = 0

    for index, line in enumerate(lines):
        normalized_line = line.strip().lower()
        if normalized_line.startswith("|") and {"school", "department", "program_name", "source_url"}.issubset(
            {_normalize_header(cell) for cell in line.strip().strip("|").split("|")}
        ):
            catalog_tables += 1
            for row in _row_dicts(lines, index):
                _validate_table("catalog", row, CATALOG_REQUIRED)
                level = _level(row["level"])
                degree_level = _degree_level(row["degree_level"])
                topics = _split_list(row.get("topics"), ["catalog", "programs"])
                url_type = _url_type(row, level)
                before_count = len(catalog_entries)
                add_catalog_entry(
                    catalog_entries,
                    source_registry_by_id,
                    url_manifest_by_id,
                    university_id,
                    row["school"],
                    row["department"],
                    level,
                    degree_level,
                    row["program_name"],
                    row["source_url"],
                    capture_date,
                    dataset_version,
                    course_code=row.get("course_code") or None,
                    degree_full_name=row.get("degree_full_name") or None,
                    raw_section_path=row.get("raw_section_path") or "Structured Markdown > Catalog Entries",
                )
                entry = catalog_entries[before_count]
                entry["topics"] = sorted(set(topics))
                entry["search_text"] = " ".join(
                    filter(
                        None,
                        [
                            university_name,
                            university_id.upper(),
                            entry["school"],
                            entry["department"],
                            entry["degree_level"],
                            entry.get("course_code") or "",
                            entry["program_name"],
                        ],
                    )
                )
                source_id = entry["source_id"]
                source_registry_by_id[source_id]["url_type"] = url_type
                source_registry_by_id[source_id]["topics"] = sorted(set(topics))
                url_id = stable_id("url", source_id)
                url_manifest_by_id[url_id]["url_type"] = url_type
                url_manifest_by_id[url_id]["topics"] = sorted(set(topics))
                _apply_source_overrides(source_registry_by_id, url_manifest_by_id, source_id, row)
                catalog_entry_by_program_name[entry["program_name"].lower()] = entry

        if normalized_line.startswith("|") and {"fact_type", "fact_key", "raw_value", "source_url"}.issubset(
            {_normalize_header(cell) for cell in line.strip().strip("|").split("|")}
        ):
            fact_tables += 1
            for row in _row_dicts(lines, index):
                _validate_table("quick_fact", row, FACT_REQUIRED)
                fact_type = row["fact_type"]
                if fact_type not in FACT_TYPES:
                    raise StructuredMarkdownContractError(f"Unsupported fact_type {fact_type!r}.")
                source_url = row["source_url"]
                if not is_valid_http_url(source_url):
                    raise StructuredMarkdownContractError(f"Invalid fact source_url {source_url!r}.")
                topics = _split_list(row.get("topics"), [fact_type])
                source_id = add_source(
                    source_registry_by_id,
                    url_manifest_by_id,
                    university_id,
                    source_url,
                    topics,
                    row.get("url_type") or "overview",
                    capture_date,
                    dataset_version,
                )
                _apply_source_overrides(source_registry_by_id, url_manifest_by_id, source_id, row)
                linked_entry = catalog_entry_by_program_name.get(row.get("program_name", "").lower())
                if linked_entry:
                    entry_id = linked_entry["entry_id"]
                    if entry_id not in source_registry_by_id[source_id]["entry_ids"]:
                        source_registry_by_id[source_id]["entry_ids"].append(entry_id)
                    url_id = stable_id("url", source_id)
                    if entry_id not in url_manifest_by_id[url_id]["entry_ids"]:
                        url_manifest_by_id[url_id]["entry_ids"].append(entry_id)
                else:
                    entry_id = None
                raw_value = row["raw_value"]
                quick_facts.append(
                    {
                        "fact_id": stable_id("fact", university_id, row.get("program_name", ""), row["fact_key"], dataset_version),
                        "university_id": university_id,
                        "program_id": None,
                        "entry_id": entry_id,
                        "fact_type": fact_type,
                        "fact_key": row["fact_key"],
                        "raw_value": raw_value,
                        "normalized_value": normalize_fact_value(fact_type, raw_value),
                        "unit": row.get("unit") or None,
                        "currency": row.get("currency") or ("USD" if "$" in raw_value else None),
                        "admission_cycle": row.get("admission_cycle") or None,
                        "term": row.get("term") or None,
                        "source_id": source_id,
                        "source_url": canonicalize_url(source_url),
                        "evidence_ids": _split_list(row.get("evidence_ids"), []),
                        "weknora_chunk_ids": [],
                        "capture_date": capture_date,
                        "dataset_version": dataset_version,
                        "source_version": row.get("source_version") or None,
                        "confidence": float(row.get("confidence") or 0.8),
                        "review_status": row.get("review_status") or "review_required",
                        "conflict_status": row.get("conflict_status") or "none",
                        "status": row.get("status") or "active",
                    }
                )

    if catalog_tables == 0:
        raise StructuredMarkdownContractError("Structured Markdown must include a catalog table with school/department/program_name/source_url columns.")
    if not catalog_entries:
        raise StructuredMarkdownContractError("Structured Markdown catalog table produced zero catalog entries.")

    unclassified_urls = add_markdown_prose_sources(
        text,
        source_registry_by_id,
        url_manifest_by_id,
        university_id,
        capture_date,
        dataset_version,
    )
    enrich_catalog_entries(catalog_entries)

    source_registry = list(source_registry_by_id.values())
    entity_contexts = build_entity_contexts(
        university_id=university_id,
        university_name=university_name,
        country_code=country_code,
        region=region,
        catalog_entries=catalog_entries,
        quick_facts=quick_facts,
        source_registry=source_registry,
        dataset_version=dataset_version,
    )

    return ParseResult(
        source_registry=source_registry,
        catalog_entries=catalog_entries,
        url_manifest=list(url_manifest_by_id.values()),
        quick_facts=quick_facts,
        entity_contexts=entity_contexts,
        summary={
            "university_id": university_id,
            "university_name": university_name,
            "country_code": country_code,
            "region": region,
            "aliases": aliases,
            "parser_adapter": "generic_structured",
            "catalog_tables": catalog_tables,
            "fact_tables": fact_tables,
            "catalog_entries": len(catalog_entries),
            "catalog_entries_with_disciplines": len(catalog_entries),
            "source_registry": len(source_registry_by_id),
            "url_manifest": len(url_manifest_by_id),
            "quick_facts": len(quick_facts),
            "entity_contexts": len(entity_contexts),
            "unclassified_urls": unclassified_urls,
        },
    )
