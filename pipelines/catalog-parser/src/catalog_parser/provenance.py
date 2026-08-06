"""Deterministic Markdown-to-JSONL provenance records.

The business JSONL files remain compact and schema-compatible.  This module
creates a sidecar audit stream that answers a narrower question: which exact
Markdown snapshot and line produced a structured record, and which fields were
read directly versus derived by a deterministic rule.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

from .markdown_sources import canonicalize_url


class ProvenanceError(ValueError):
    """Raised when a record cannot be tied to a valid Markdown snapshot."""


ENTITY_KEYS = {
    "catalog_entries": "entry_id",
    "quick_facts": "fact_id",
}

CATALOG_DIRECT_FIELDS = {
    "school",
    "department",
    "level",
    "degree_level",
    "degree_full_name",
    "course_code",
    "program_name",
    "source_url",
}
FACT_DIRECT_FIELDS = {
    "entry_id",
    "fact_type",
    "fact_key",
    "raw_value",
    "unit",
    "currency",
    "admission_cycle",
    "term",
    "source_url",
    "evidence_ids",
}

DERIVED_FIELDS = {
    "entry_id": "stable_record_id",
    "fact_id": "stable_record_id",
    "source_id": "canonical_source_id",
    "canonical_program_name": "catalog_name_normalization",
    "aliases": "catalog_alias_normalization",
    "discipline_ids": "discipline_taxonomy",
    "discipline_labels": "discipline_taxonomy",
    "search_text": "search_text_composition",
    "cross_school": "cross_school_detection",
    "cross_school_names": "cross_school_detection",
    "normalized_value": "fact_value_normalization",
    "topics": "topic_classification",
}

SYSTEM_FIELDS = {
    "dataset_version",
    "capture_date",
    "source_version",
    "confidence",
    "review_status",
    "conflict_status",
    "status",
    "weknora_chunk_ids",
}

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_URL_RE = re.compile(r"https?://[^\s)\]>\"']+", re.IGNORECASE)


def _record_hash(record: dict[str, Any]) -> str:
    payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _clean_markdown(value: Any) -> str:
    if value is None:
        return ""
    text = str(value)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`~]", "", text)
    return " ".join(text.split()).strip()


def _match_text(value: Any) -> str:
    text = _clean_markdown(value).casefold()
    return " ".join(re.findall(r"[a-z0-9\u4e00-\u9fff]+", text))


def _canonical_urls(line: str) -> set[str]:
    urls: set[str] = set()
    for raw in _URL_RE.findall(line):
        try:
            urls.add(canonicalize_url(raw.rstrip(".,;:")))
        except ValueError:
            continue
    return urls


def _contains_value(line: str, value: Any) -> bool:
    expected = _match_text(value)
    if not expected:
        return False
    actual = _match_text(line)
    return expected in actual


def _token_overlap(line: str, value: Any) -> float:
    expected = set(_match_text(value).split())
    actual = set(_match_text(line).split())
    if not expected:
        return 0.0
    return len(expected & actual) / len(expected)


def _line_score(line: str, record: dict[str, Any], entity: str) -> int:
    score = 0
    if line.lstrip().startswith("|"):
        score += 2
    if entity == "catalog_entries":
        if _contains_value(line, record.get("program_name")):
            score += 10
        if record.get("course_code") and _contains_value(line, record["course_code"]):
            score += 3
    else:
        if _contains_value(line, record.get("raw_value")):
            score += 12
        else:
            overlap = _token_overlap(line, record.get("raw_value"))
            if overlap >= 0.65:
                score += 10
            elif overlap >= 0.4:
                score += 6
        if record.get("fact_key") and _contains_value(line, record["fact_key"].replace("_", " ")):
            score += 2
    source_url = str(record.get("source_url") or "")
    if source_url:
        try:
            canonical_source = canonicalize_url(source_url)
        except ValueError:
            canonical_source = source_url
        if canonical_source in _canonical_urls(line):
            score += 8
    return score


def _heading_path(lines: list[str], line_number: int) -> list[str]:
    levels: dict[int, str] = {}
    for line in lines[:line_number]:
        match = _HEADING_RE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        levels = {key: value for key, value in levels.items() if key < level}
        levels[level] = _clean_markdown(match.group(2))
    return [levels[level] for level in sorted(levels)]


def _find_line(lines: list[str], record: dict[str, Any], entity: str) -> tuple[int, int, int]:
    candidates = [
        (score, index)
        for index, line in enumerate(lines)
        if (score := _line_score(line, record, entity)) > 0
    ]
    if not candidates:
        record_id = record.get(ENTITY_KEYS[entity], "unknown")
        raise ProvenanceError(f"{entity}:{record_id} has no matching Markdown line")
    score, index = max(candidates, key=lambda item: (item[0], -item[1]))
    minimum_score = 12 if entity == "catalog_entries" else 10
    if score < minimum_score:
        record_id = record.get(ENTITY_KEYS[entity], "unknown")
        raise ProvenanceError(f"{entity}:{record_id} has an ambiguous Markdown match (score={score})")
    return index + 1, index + 1, score


def _field_kind(entity: str, field: str) -> tuple[str, str | None]:
    direct = CATALOG_DIRECT_FIELDS if entity == "catalog_entries" else FACT_DIRECT_FIELDS
    if field in direct:
        return "direct", None
    if field in DERIVED_FIELDS:
        return "derived", DERIVED_FIELDS[field]
    if field in SYSTEM_FIELDS:
        return "system", "ingestion_runtime"
    return "derived", "parser_contract"


def _field_mappings(entity: str, record: dict[str, Any], line_start: int, line_end: int) -> dict[str, dict[str, Any]]:
    fields: dict[str, dict[str, Any]] = {}
    for field, value in record.items():
        kind, rule = _field_kind(entity, field)
        item: dict[str, Any] = {
            "kind": kind,
            "line_start": line_start,
            "line_end": line_end,
        }
        if kind == "direct":
            item["column"] = field
            item["raw_value"] = value
        elif rule:
            item["rule"] = rule
        fields[field] = item
    return fields


def build_provenance(
    markdown_text: str,
    dataset: dict[str, list[dict[str, Any]]],
    *,
    university_id: str,
    dataset_version: str,
    source_path: str | None = None,
) -> list[dict[str, Any]]:
    """Build one traceability record for each catalog/fact JSONL row."""

    lines = markdown_text.splitlines()
    md_hash = hashlib.sha256(markdown_text.encode("utf-8")).hexdigest()
    mappings: list[dict[str, Any]] = []
    for entity, primary_key in ENTITY_KEYS.items():
        for record in dataset.get(entity, []):
            record_id = str(record.get(primary_key) or "")
            if not record_id:
                raise ProvenanceError(f"{entity} record is missing {primary_key}")
            if record.get("university_id") != university_id:
                raise ProvenanceError(f"{entity}:{record_id} belongs to another university")
            if str(record.get("dataset_version") or "") != dataset_version:
                raise ProvenanceError(f"{entity}:{record_id} has a different dataset_version")
            line_start, line_end, match_score = _find_line(lines, record, entity)
            section_path = " > ".join(_heading_path(lines, line_start - 1))
            mapping_seed = f"{university_id}|{dataset_version}|{entity}|{record_id}"
            mapping_id = f"prov_{hashlib.sha256(mapping_seed.encode('utf-8')).hexdigest()[:24]}"
            mappings.append(
                {
                    "mapping_id": mapping_id,
                    "university_id": university_id,
                    "dataset_version": dataset_version,
                    "jsonl": {
                        "entity": entity,
                        "record_id": record_id,
                        "record_hash": _record_hash(record),
                    },
                    "md": {
                        "file": source_path,
                        "sha256": md_hash,
                        "line_start": line_start,
                        "line_end": line_end,
                        "section_path": section_path,
                        "snippet": lines[line_start - 1][:2000],
                    },
                    "fields": _field_mappings(entity, record, line_start, line_end),
                    "verification": {
                        "status": "verified" if match_score >= 12 else "review_required",
                        "version_match": True,
                        "line_match": True,
                        "all_fields_mapped": True,
                        "match_score": match_score,
                    },
                }
            )
    validate_provenance(mappings, markdown_text)
    return mappings


def validate_provenance(mappings: Iterable[dict[str, Any]], markdown_text: str) -> None:
    """Validate snapshot identity and line ranges before publication."""

    expected_hash = hashlib.sha256(markdown_text.encode("utf-8")).hexdigest()
    line_count = len(markdown_text.splitlines())
    seen: set[tuple[str, str]] = set()
    for mapping in mappings:
        jsonl = mapping.get("jsonl") or {}
        md = mapping.get("md") or {}
        entity = str(jsonl.get("entity") or "")
        record_id = str(jsonl.get("record_id") or "")
        if entity not in ENTITY_KEYS or not record_id:
            raise ProvenanceError("mapping has an invalid JSONL identity")
        identity = (entity, record_id)
        if identity in seen:
            raise ProvenanceError(f"duplicate provenance mapping: {entity}:{record_id}")
        seen.add(identity)
        if md.get("sha256") != expected_hash:
            raise ProvenanceError(f"{entity}:{record_id} does not match the Markdown snapshot hash")
        start = md.get("line_start")
        end = md.get("line_end")
        if not isinstance(start, int) or not isinstance(end, int) or start < 1 or end < start or end > line_count:
            raise ProvenanceError(f"{entity}:{record_id} has an invalid Markdown line range")
        verification = mapping.get("verification") or {}
        if verification.get("version_match") is not True:
            raise ProvenanceError(f"{entity}:{record_id} has a version mismatch")


def write_provenance_jsonl(path: Path, mappings: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for mapping in mappings:
            handle.write(json.dumps(mapping, ensure_ascii=False, sort_keys=True) + "\n")


def read_provenance_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
