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
    add_markdown_prose_sources,
    cleanup_markdown,
    extract_capture_date,
    stable_id,
    table_rows,
)


PROGRAM_HEADER_TOKENS = ("专业", "项目", "program", "option", "minor", "certificate")
URL_PATTERN = re.compile(
    r"https?://[^\s`|)>]+|(?<![@\w])(?:[a-z0-9-]+\.)+(?:edu|org|com|ac\.uk|edu\.au|ca)(?:/[^\s`|)>]*)?",
    re.IGNORECASE,
)


def _clean_url(value: str) -> str | None:
    match = URL_PATTERN.search(value)
    if not match:
        return None
    candidate = match.group(0).rstrip(".,;:]}\"")
    if not candidate.startswith(("http://", "https://")):
        candidate = f"https://{candidate}"
    try:
        canonical = canonicalize_url(candidate)
    except ValueError:
        return None
    return canonical if is_valid_http_url(canonical) else None


def _university_name(text: str, university_id: str) -> str:
    first_heading = next((line[2:].strip() for line in text.splitlines() if line.startswith("# ")), "")
    name = re.split(r"\s+(?:Admissions|Knowledge Base|—|–)", first_heading, maxsplit=1)[0].strip()
    return cleanup_markdown(name) or university_id.upper()


def _degree_and_level(context: str) -> tuple[str, str]:
    value = context.lower()
    if "minor" in value or "辅修" in value:
        return "Minor", "undergraduate"
    if "certificate" in value or "证书" in value:
        return "Certificate", "graduate" if "graduate" in value or "研究生" in value else "undergraduate"
    if re.search(r"\b(ph\.?d|sc\.?d|th\.?d)\b", value):
        return "PhD", "graduate"
    if "mba" in value:
        return "MBA", "graduate"
    if re.search(r"\bm\.?eng\b", value):
        return "MEng", "graduate"
    if re.search(r"\bm\.?arch\b", value):
        return "MArch", "graduate"
    if re.search(r"\b(m\.?s|s\.?m|m\.?a|a\.?m|med|mfa|mph|mpp|mids|mat)\b", value):
        return "SM", "graduate"
    if re.search(r"\b(b\.?a|a\.?b|b\.?s|s\.?b|bse|bfa|bas|bsn|bae|bmus|bsd|bsla|bsw)\b", value):
        return "SB", "undergraduate"
    if "undergraduate" in value or "本科" in value:
        return "SB", "undergraduate"
    if "graduate" in value or "研究生" in value or "master" in value or "doctoral" in value:
        return "Other", "graduate"
    return "Other", "undergraduate"


def _nearest_source_url(lines: list[str], table_index: int) -> str | None:
    for index in range(table_index - 1, max(-1, table_index - 140), -1):
        line = lines[index]
        if index != table_index - 1 and line.startswith("## "):
            break
        candidate = _clean_url(line)
        if candidate:
            return candidate
    return None


def _program_column(headers: list[str]) -> int | None:
    for index, header in enumerate(headers):
        lowered = header.lower()
        if any(token in lowered for token in PROGRAM_HEADER_TOKENS):
            return index
    return None


def parse_deep_v2_markdown(university_id: str, path: Path) -> ParseResult:
    text = path.read_text("utf-8")
    lines = text.splitlines()
    capture_date = extract_capture_date(text)
    if capture_date == "unknown":
        raise ValueError("Deep v2 Markdown must include a data capture date")
    dataset_version = f"{university_id}_{capture_date.replace('-', '')}_v2"
    university_name = _university_name(text, university_id)
    source_registry_by_id: dict[str, dict[str, Any]] = {}
    url_manifest_by_id: dict[str, dict[str, Any]] = {}
    catalog_entries: list[dict[str, Any]] = []
    seen_entry_ids: set[str] = set()
    heading_path: dict[int, str] = {}
    parsed_tables = 0

    for index, line in enumerate(lines):
        heading = re.match(r"^(#{2,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            heading_path = {key: value for key, value in heading_path.items() if key < level}
            heading_path[level] = cleanup_markdown(heading.group(2))
            continue
        if not line.startswith("|"):
            continue
        rows = table_rows(lines, index)
        if len(rows) < 2:
            continue
        headers = [cleanup_markdown(value) for value in rows[0]]
        if not headers or headers[0].strip() != "#":
            continue
        program_index = _program_column(headers)
        if program_index is None:
            continue
        url_index = next((i for i, header in enumerate(headers) if "url" in header.lower() or "source" in header.lower()), None)
        code_index = next((i for i, header in enumerate(headers) if "代码" in header or "code" in header.lower()), None)
        degree_index = next((i for i, header in enumerate(headers) if "学位" in header or "type" in header.lower()), None)
        context_parts = [heading_path[key] for key in sorted(heading_path)]
        school = heading_path.get(4) or heading_path.get(3) or university_name
        department_heading = heading_path.get(5) or school
        default_source_url = _nearest_source_url(lines, index)
        table_added = 0

        for cells in rows[1:]:
            if program_index >= len(cells):
                continue
            program_name = cleanup_markdown(cells[program_index])
            if not program_name or program_name.lower() in {"n/a", "none", "total", "合计"}:
                continue
            source_url = _clean_url(cells[url_index]) if url_index is not None and url_index < len(cells) else default_source_url
            if not source_url:
                continue
            course_code = cleanup_markdown(cells[code_index]) if code_index is not None and code_index < len(cells) else None
            row_degree = cleanup_markdown(cells[degree_index]) if degree_index is not None and degree_index < len(cells) else ""
            degree_level, level = _degree_and_level(" ".join([*context_parts, " ".join(headers), program_name, row_degree]))
            entry_id = stable_id("ent", university_id, level, degree_level, course_code or "", program_name, "")
            if entry_id in seen_entry_ids:
                continue
            seen_entry_ids.add(entry_id)
            add_catalog_entry(
                catalog_entries,
                source_registry_by_id,
                url_manifest_by_id,
                university_id,
                school,
                department_heading,
                level,
                degree_level,
                program_name,
                source_url,
                capture_date,
                dataset_version,
                course_code=course_code,
                degree_full_name=row_degree or None,
                raw_section_path=" > ".join(context_parts),
            )
            catalog_entries[-1]["search_text"] = " ".join(
                filter(None, [university_name, university_id.upper(), school, department_heading, degree_level, course_code or "", program_name])
            )
            table_added += 1
        if table_added:
            parsed_tables += 1

    if not catalog_entries:
        raise ValueError("Deep v2 Markdown produced zero catalog entries")
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
        country_code=None,
        region=None,
        catalog_entries=catalog_entries,
        quick_facts=[],
        source_registry=source_registry,
        dataset_version=dataset_version,
    )
    return ParseResult(
        source_registry=source_registry,
        catalog_entries=catalog_entries,
        url_manifest=list(url_manifest_by_id.values()),
        quick_facts=[],
        entity_contexts=entity_contexts,
        summary={
            "university_id": university_id,
            "university_name": university_name,
            "country_code": None,
            "region": None,
            "aliases": [],
            "parser_adapter": "deep_v2",
            "catalog_tables": parsed_tables,
            "catalog_entries": len(catalog_entries),
            "catalog_entries_with_disciplines": len(catalog_entries),
            "source_registry": len(source_registry_by_id),
            "url_manifest": len(url_manifest_by_id),
            "quick_facts": 0,
            "entity_contexts": len(entity_contexts),
            "unclassified_urls": unclassified_urls,
        },
    )
