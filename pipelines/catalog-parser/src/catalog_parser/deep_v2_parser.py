from __future__ import annotations

import re
from collections import Counter
from pathlib import Path
from typing import Any
from urllib.parse import urljoin, urlparse

from .disciplines import enrich_catalog_entries
from .entity_contexts import build_entity_contexts
from .markdown_sources import canonicalize_url, is_valid_http_url
from .quality_rules import program_name_issue
from .mit_parser import (
    ParseResult,
    add_catalog_entry,
    add_markdown_prose_sources,
    cleanup_markdown,
    extract_capture_date,
    stable_id,
)


PROGRAM_HEADER_NAMES = {
    "专业", "专业名称", "专业 / major", "专业(major)", "专业 / program", "专业/项目",
    "项目", "项目名称", "项目 / program", "学位项目", "课程", "课程名", "课程名称",
    "program", "program name", "programme", "programme name", "major", "major name",
    "minor", "minor name", "course", "course name", "option", "certificate",
}
NON_CATALOG_HEADER_TERMS = {
    "admission category", "录取类别", "typical future program directions", "典型后续专业方向",
    "evidence id", "data key", "why missing", "target url", "priority", "证据", "数据键",
}
NON_CATALOG_VALUE_HEADERS = {
    "value", "值", "snippet", "information", "信息", "说明", "内容", "详情", "费用", "日期", "金额", "deadline",
}
CATALOG_SUPPORT_HEADER_TERMS = {
    "degree", "学位", "url", "source", "school", "faculty", "college", "学院", "department", "系",
    "code", "代码", "type", "award", "partner", "home", "campus", "mode", "duration",
}
FULL_URL_PATTERN = re.compile(r"https?://[^\s`|)>]+", re.IGNORECASE)
BARE_DOMAIN_PATTERN = re.compile(
    r"(?<![@\w.])(?:[a-z0-9-]+\.)+(?:edu|org|com|net|gov|ca|ac\.uk|edu\.au|edu\.sg)(?:/[^\s`|)>]*)?"
)
TABLE_SEPARATOR_CELL = re.compile(r"[-: ]+")


def _clean_url(value: str, base_url: str | None = None) -> str | None:
    match = FULL_URL_PATTERN.search(value)
    if match:
        candidate = match.group(0).rstrip(".,;:]}\"")
    else:
        match = BARE_DOMAIN_PATTERN.search(value)
        if match:
            candidate = f"https://{match.group(0).rstrip('.,;:]}\"')}"
        else:
            relative_match = re.search(r"(?<![\w/])/[a-z0-9][^\s`|)>]*", value, re.IGNORECASE)
            if not relative_match or not base_url:
                return None
            candidate = urljoin(base_url, relative_match.group(0).rstrip(".,;:]}\""))
    try:
        canonical = canonicalize_url(candidate)
    except ValueError:
        return None
    return canonical if is_valid_http_url(canonical) else None


def _document_base_url(text: str) -> str | None:
    candidates: list[str] = []
    for line in text.splitlines():
        for match in FULL_URL_PATTERN.finditer(line):
            candidate = _clean_url(match.group(0))
            if candidate:
                candidates.append(candidate)
    if not candidates:
        return None
    host_counts = Counter(urlparse(candidate).netloc.lower() for candidate in candidates)
    first_host_index: dict[str, int] = {}
    for index, candidate in enumerate(candidates):
        first_host_index.setdefault(urlparse(candidate).netloc.lower(), index)
    excluded_hosts = ("topuniversities.com", "wikipedia.org", "usnews.com", "linkedin.com", "facebook.com")
    ranked_hosts = sorted(
        host_counts,
        key=lambda host: (
            any(host == excluded or host.endswith(f".{excluded}") for excluded in excluded_hosts),
            -host_counts[host],
            first_host_index[host],
        ),
    )
    selected_host = ranked_hosts[0]
    selected = next(candidate for candidate in candidates if urlparse(candidate).netloc.lower() == selected_host)
    parsed = urlparse(selected)
    return f"{parsed.scheme}://{parsed.netloc}"


def _relaxed_table_rows(lines: list[str], start_index: int) -> list[list[str]]:
    rows: list[list[str]] = []
    index = start_index
    while index < len(lines):
        line = lines[index]
        if line.startswith("|"):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if cells and not all(TABLE_SEPARATOR_CELL.fullmatch(cell) for cell in cells):
                rows.append(cells)
            index += 1
            continue
        if not line.strip():
            next_index = index + 1
            while next_index < len(lines) and not lines[next_index].strip():
                next_index += 1
            if next_index < len(lines) and lines[next_index].startswith("|"):
                if next_index + 1 < len(lines) and lines[next_index + 1].startswith("|"):
                    separator = [cell.strip() for cell in lines[next_index + 1].strip().strip("|").split("|")]
                    if separator and all(TABLE_SEPARATOR_CELL.fullmatch(cell) for cell in separator):
                        break
                index = next_index
                continue
        break
    return rows


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


def _table_is_start(lines: list[str], index: int) -> bool:
    if not lines[index].startswith("|") or (index > 0 and lines[index - 1].startswith("|")):
        return False
    if index + 1 >= len(lines) or not lines[index + 1].startswith("|"):
        return False
    cells = [cell.strip() for cell in lines[index + 1].strip().strip("|").split("|")]
    return bool(cells) and all(TABLE_SEPARATOR_CELL.fullmatch(cell) for cell in cells)


def _normalized_header(value: str) -> str:
    return re.sub(r"\s+", " ", cleanup_markdown(value).strip().lower())


def _is_catalog_table(headers: list[str]) -> bool:
    normalized = {_normalized_header(value) for value in headers}
    if normalized & NON_CATALOG_HEADER_TERMS:
        return False
    has_supporting_catalog_column = any(
        any(term in value for term in CATALOG_SUPPORT_HEADER_TERMS)
        for value in normalized
    )
    if normalized & NON_CATALOG_VALUE_HEADERS and not has_supporting_catalog_column:
        return False
    if len(normalized & NON_CATALOG_VALUE_HEADERS) >= 2:
        return False
    first = _normalized_header(headers[0]) if headers else ""
    degree_columns = sum(
        1
        for value in normalized
        if re.fullmatch(r"(?:ba|bs|sb|minor|phd|cert|certificate|ma|ms|mba|meng|mfa|mph|jd|llm|合计)", value)
    )
    if ("级别" in first or "level" in first) and degree_columns >= 2:
        return False
    return _program_column(headers) is not None


def _is_valid_program_name(value: str) -> bool:
    normalized = cleanup_markdown(value).strip()
    if program_name_issue(normalized):
        return False
    if re.fullmatch(r"e-[a-z0-9-]+", normalized.lower()):
        return False
    if _clean_url(normalized):
        return False
    return True


def _specific_degree_hint(row_degree: str, heading_values: list[str], source_url: str) -> str | None:
    candidates = [row_degree, source_url.rsplit("/", 1)[-1]]
    for heading in reversed(heading_values):
        lowered = heading.lower()
        if ("minor" in lowered or "辅修" in lowered) and any(
            term in lowered for term in ("major", "program", "programme", "option", "专业", "项目")
        ):
            continue
        candidates.append(heading)
    patterns = (
        ("Graduate Minor", r"\bgraduate\s+(?:field\s+)?minor\b"),
        ("Minor", r"\bminor\b|辅修"),
        ("PhD", r"\bph\.?d\b|doctor of philosophy|博士"),
        ("MEng", r"\bm\.?eng\b|master of engineering"),
        ("MArch", r"\bm\.?arch\b|master of architecture"),
        ("MBA", r"\bmba\b"),
        ("MS", r"\bm\.?s\b|master of science"),
        ("MA", r"\bm\.?a\b|master of arts"),
        ("BS", r"\bb\.?s\b|bachelor of science|(?:^|[-_])bs(?:[-_]|$)"),
        ("BA", r"\bb\.?a\b|bachelor of arts|(?:^|[-_])ba(?:[-_]|$)"),
    )
    for candidate in candidates:
        value = candidate.lower()
        for label, pattern in patterns:
            if re.search(pattern, value):
                return label
    return None


def _degree_metadata(context: str, row_degree: str, heading_values: list[str], source_url: str) -> tuple[str, str, str | None]:
    hint = _specific_degree_hint(row_degree, heading_values, source_url)
    if hint == "Graduate Minor":
        return "Other", "graduate", hint
    if hint == "Minor":
        return "Minor", "undergraduate", hint
    if hint == "PhD":
        return "PhD", "graduate", hint
    if hint in {"MEng", "MArch", "MBA"}:
        return hint, "graduate", hint
    if hint in {"MS", "MA"}:
        return "SM", "graduate", hint
    if hint in {"BA", "BS"}:
        return "SB", "undergraduate", hint
    degree_level, level = _degree_and_level(context)
    return degree_level, level, cleanup_markdown(row_degree) or None


def _nearest_source_url(lines: list[str], table_index: int, base_url: str | None = None) -> str | None:
    for index in range(table_index - 1, max(-1, table_index - 140), -1):
        line = lines[index]
        if index != table_index - 1 and line.startswith("## "):
            break
        candidate = _clean_url(line, base_url)
        if candidate:
            return candidate
    return base_url


def _program_column(headers: list[str]) -> int | None:
    for index, header in enumerate(headers):
        normalized = _normalized_header(header)
        if normalized in PROGRAM_HEADER_NAMES:
            return index
        if re.fullmatch(r"(?:专业|项目|课程)(?:名称|名)?\s*(?:\([^)]*\))?", normalized):
            return index
        if re.fullmatch(r"(?:minor|major)\s+(?:name|名称)", normalized):
            return index
        if re.fullmatch(
            r"(?:(?:phd|master'?s?|undergraduate|graduate)\s+)?(?:program|programme)(?:\s+name)?(?:\s*\([^)]*\))?",
            normalized,
        ):
            return index
    return None


def parse_deep_v2_markdown(university_id: str, path: Path) -> ParseResult:
    text = path.read_text("utf-8")
    lines = text.splitlines()
    document_base_url = _document_base_url(text)
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
    candidate_tables = 0
    rejected_tables = 0
    rejected_rows = 0

    for index, line in enumerate(lines):
        heading = re.match(r"^(#{2,6})\s+(.+)$", line)
        if heading:
            level = len(heading.group(1))
            heading_path = {key: value for key, value in heading_path.items() if key < level}
            heading_path[level] = cleanup_markdown(heading.group(2))
            continue
        if not _table_is_start(lines, index):
            continue
        candidate_tables += 1
        rows = _relaxed_table_rows(lines, index)
        if len(rows) < 2:
            continue
        headers = [cleanup_markdown(value) for value in rows[0]]
        if not headers:
            continue
        if not _is_catalog_table(headers):
            rejected_tables += 1
            continue
        program_index = _program_column(headers)
        if program_index is None:
            continue
        url_index = next((i for i, header in enumerate(headers) if "url" in header.lower() or "source" in header.lower()), None)
        code_index = next((i for i, header in enumerate(headers) if "代码" in header or "code" in header.lower()), None)
        degree_index = next((i for i, header in enumerate(headers) if "学位" in header or "type" in header.lower()), None)
        school_index = next((i for i, header in enumerate(headers) if header.lower() in {"school", "faculty", "college", "学院"}), None)
        department_index = next((i for i, header in enumerate(headers) if header.lower() in {"department", "dept", "系", "院系"}), None)
        context_parts = [heading_path[key] for key in sorted(heading_path)]
        school = heading_path.get(4) or heading_path.get(3) or university_name
        department_heading = heading_path.get(5) or school
        default_source_url = _nearest_source_url(lines, index, document_base_url)
        table_added = 0

        for cells in rows[1:]:
            if program_index >= len(cells):
                continue
            program_name = cleanup_markdown(cells[program_index])
            if not _is_valid_program_name(program_name):
                rejected_rows += 1
                continue
            source_url = _clean_url(cells[url_index], document_base_url) if url_index is not None and url_index < len(cells) else default_source_url
            if not source_url:
                continue
            course_code = cleanup_markdown(cells[code_index]) if code_index is not None and code_index < len(cells) else None
            row_degree = cleanup_markdown(cells[degree_index]) if degree_index is not None and degree_index < len(cells) else ""
            row_school = cleanup_markdown(cells[school_index]) if school_index is not None and school_index < len(cells) else school
            row_department = cleanup_markdown(cells[department_index]) if department_index is not None and department_index < len(cells) else department_heading
            degree_level, level, degree_hint = _degree_metadata(
                " ".join([*context_parts, " ".join(headers), program_name, row_degree]),
                row_degree,
                context_parts,
                source_url,
            )
            entry_id = stable_id(
                "ent",
                university_id,
                level,
                degree_level,
                course_code or "",
                program_name,
                degree_hint or "",
            )
            if entry_id in seen_entry_ids:
                continue
            seen_entry_ids.add(entry_id)
            add_catalog_entry(
                catalog_entries,
                source_registry_by_id,
                url_manifest_by_id,
                university_id,
                row_school or school,
                row_department or department_heading,
                level,
                degree_level,
                program_name,
                source_url,
                capture_date,
                dataset_version,
                course_code=course_code,
                degree_full_name=degree_hint or row_degree or None,
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
            "candidate_tables": candidate_tables,
            "rejected_tables": rejected_tables,
            "rejected_catalog_rows": rejected_rows,
            "catalog_entries": len(catalog_entries),
            "catalog_entries_with_disciplines": len(catalog_entries),
            "source_registry": len(source_registry_by_id),
            "url_manifest": len(url_manifest_by_id),
            "quick_facts": 0,
            "entity_contexts": len(entity_contexts),
            "unclassified_urls": unclassified_urls,
        },
    )
