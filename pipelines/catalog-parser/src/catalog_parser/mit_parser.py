from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

from .disciplines import enrich_catalog_entries
from .entity_contexts import build_entity_contexts
from .markdown_sources import canonicalize_url, deduplicate_extracted, extract_urls_from_markdown, source_id_for


@dataclass
class ParseResult:
    source_registry: list[dict]
    catalog_entries: list[dict]
    url_manifest: list[dict]
    quick_facts: list[dict]
    entity_contexts: list[dict]
    summary: dict

    def write_jsonl(self, out_dir: Path) -> None:
        for name, rows in [
            ("source_registry.jsonl", self.source_registry),
            ("catalog_entries.jsonl", self.catalog_entries),
            ("url_manifest.jsonl", self.url_manifest),
            ("quick_facts.jsonl", self.quick_facts),
            ("entity_contexts.jsonl", self.entity_contexts),
        ]:
            with (out_dir / name).open("w", encoding="utf-8") as f:
                for row in rows:
                    f.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


# slug / stable_id live in markdown_sources (Task 3 shared core). Re-exported here
# so existing `from mit_parser import stable_id` imports keep working.
from .markdown_sources import slug, stable_id  # noqa: E402,F401


def extract_capture_date(text: str) -> str:
    head = "\n".join(text.splitlines()[:80])
    match = re.search(
        r"(?:Data capture date|Capture date|生成日期|采集日期|数据捕获日期)[^\n\d]*(20\d{2}-\d{2}-\d{2})",
        head,
        re.IGNORECASE,
    )
    if not match:
        match = re.search(r"\b(20\d{2}-\d{2}-\d{2})\b", head)
    return match.group(1) if match else "unknown"


def table_rows(lines: list[str], start_index: int) -> list[list[str]]:
    rows: list[list[str]] = []
    for line in lines[start_index:]:
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells and all(re.fullmatch(r"[-: ]+", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def parse_mit_markdown(path: Path) -> ParseResult:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    capture_date = extract_capture_date(text)
    dataset_version = "mit_20260704_v2"

    source_registry_by_id: dict[str, dict] = {}
    url_manifest_by_id: dict[str, dict] = {}
    catalog_entries: list[dict] = []
    quick_facts: list[dict] = []

    current_school = ""
    current_department = ""
    current_degree = ""
    current_section = ""

    for i, line in enumerate(lines):
        if line.startswith("## "):
            current_section = line[3:].strip()
        elif line.startswith("#### ") and ("SECTION 1" in current_section or "SECTION 2" in current_section):
            current_school = line[5:].strip()
        elif line.startswith("##### "):
            current_department = line[6:].strip()
        elif line.startswith("###### "):
            current_degree = line[7:].strip()

        if line.startswith("| # | 课程号 | 专业 | URL |"):
            for cells in table_rows(lines, i)[1:]:
                if len(cells) < 4:
                    continue
                _, course_code, program_name, url = cells[:4]
                add_catalog_entry(
                    catalog_entries,
                    source_registry_by_id,
                    url_manifest_by_id,
                    "mit",
                    current_school,
                    current_department,
                    "undergraduate",
                    "SB",
                    program_name,
                    url,
                    capture_date,
                    dataset_version,
                    course_code=course_code,
                    raw_section_path=f"{current_section} > {current_school} > {current_department} > {current_degree}",
                )

        if line.startswith("| # | Minor | 所属学院 | URL |"):
            for cells in table_rows(lines, i)[1:]:
                if len(cells) < 4:
                    continue
                _, program_name, school, url = cells[:4]
                add_catalog_entry(
                    catalog_entries,
                    source_registry_by_id,
                    url_manifest_by_id,
                    "mit",
                    school,
                    "Minor",
                    "undergraduate",
                    "Minor",
                    program_name,
                    url,
                    capture_date,
                    dataset_version,
                    course_code=None,
                    raw_section_path="SECTION 1 > Minors",
                )

        if line.startswith("| # | 项目 | 学位全称 | URL |"):
            for cells in table_rows(lines, i)[1:]:
                if len(cells) < 4:
                    continue
                _, program_name, degree_full_name, url = cells[:4]
                add_catalog_entry(
                    catalog_entries,
                    source_registry_by_id,
                    url_manifest_by_id,
                    "mit",
                    current_school,
                    current_department,
                    "graduate",
                    normalize_degree(current_degree),
                    program_name,
                    url,
                    capture_date,
                    dataset_version,
                    degree_full_name=degree_full_name,
                    raw_section_path=f"{current_section} > {current_school} > {current_department} > {current_degree}",
                )

        if line.startswith("| # | 项目 (Program) | 申请截止"):
            for cells in table_rows(lines, i)[1:]:
                if len(cells) < 8:
                    continue
                _, program_name, deadline, fee, test_policy, english, funding, source = cells[:8]
                url_match = re.search(r"\((https?://[^)]+)\)", source)
                if not url_match:
                    continue
                url = url_match.group(1)
                source_id = add_source(
                    source_registry_by_id,
                    url_manifest_by_id,
                    "mit",
                    url,
                    ["admission_requirements", "deadline", "tests", "funding", "application_fee"],
                    "program_admission",
                    capture_date,
                    dataset_version,
                )
                for fact_type, fact_key, raw_value in [
                    ("deadline", "application_deadline", deadline),
                    ("application_fee", "application_fee", fee),
                    ("gre_gmat_policy", "standardized_test_policy", test_policy),
                    ("english_requirement", "english_minimums", english),
                    ("funding_model", "funding_model", funding),
                ]:
                    if raw_value and raw_value != "—":
                        quick_facts.append({
                            "fact_id": stable_id("fact", "mit", program_name, fact_key, dataset_version),
                            "university_id": "mit",
                            "program_id": None,
                            "entry_id": None,
                            "fact_type": fact_type,
                            "fact_key": fact_key,
                            "raw_value": raw_value,
                            "normalized_value": normalize_fact_value(fact_type, raw_value),
                            "unit": None,
                            "currency": "USD" if "$" in raw_value else None,
                            "admission_cycle": "2026" if "2026" in raw_value else None,
                            "term": "Fall",
                            "source_id": source_id,
                            "source_url": canonicalize_url(url),
                            "evidence_ids": ["E-G-008"],
                            "weknora_chunk_ids": [],
                            "capture_date": capture_date,
                            "dataset_version": dataset_version,
                            "source_version": None,
                            "confidence": 0.9,
                            "review_status": "review_required",
                            "conflict_status": "none",
                            "status": "active",
                        })

    add_mit_institution_facts(
        quick_facts,
        source_registry_by_id,
        url_manifest_by_id,
        capture_date,
        dataset_version,
    )

    unclassified_urls = add_markdown_prose_sources(
        text,
        source_registry_by_id,
        url_manifest_by_id,
        "mit",
        capture_date,
        dataset_version,
    )
    enrich_catalog_entries(catalog_entries)

    summary = {
        "university_id": "mit",
        "university_name": "Massachusetts Institute of Technology",
        "country_code": "US",
        "region": "Massachusetts",
        "aliases": ["MIT"],
        "catalog_entries": len(catalog_entries),
        "catalog_entries_with_disciplines": len(catalog_entries),
        "source_registry": len(source_registry_by_id),
        "url_manifest": len(url_manifest_by_id),
        "quick_facts": len(quick_facts),
        "mit_reconciliation_expected": 157,
        "mit_reconciliation_pass": len(catalog_entries) == 157,
        "unclassified_urls": unclassified_urls,
    }
    entity_contexts = build_entity_contexts(
        university_id="mit",
        university_name=summary["university_name"],
        country_code=summary["country_code"],
        region=summary["region"],
        catalog_entries=catalog_entries,
        quick_facts=quick_facts,
        source_registry=list(source_registry_by_id.values()),
        dataset_version=dataset_version,
    )
    summary["entity_contexts"] = len(entity_contexts)
    return ParseResult(
        source_registry=list(source_registry_by_id.values()),
        catalog_entries=catalog_entries,
        url_manifest=list(url_manifest_by_id.values()),
        quick_facts=quick_facts,
        entity_contexts=entity_contexts,
        summary=summary,
    )


def add_mit_institution_facts(quick_facts: list[dict], source_registry_by_id: dict, url_manifest_by_id: dict, capture_date: str, dataset_version: str) -> None:
    facts = [
        {
            "source_url": "https://mitadmissions.org/apply/firstyear/deadlines-requirements/",
            "topics": ["undergraduate_admission", "deadline"],
            "url_type": "deadline",
            "fact_type": "deadline",
            "fact_key": "undergraduate_early_action_deadline",
            "raw_value": "November 1",
            "normalized_value": {"month": 11, "day": 1, "label": "Early Action"},
            "evidence_ids": ["E-U-003"],
        },
        {
            "source_url": "https://mitadmissions.org/apply/firstyear/deadlines-requirements/",
            "topics": ["undergraduate_admission", "deadline"],
            "url_type": "deadline",
            "fact_type": "deadline",
            "fact_key": "undergraduate_regular_action_deadline",
            "raw_value": "January 5",
            "normalized_value": {"month": 1, "day": 5, "label": "Regular Action"},
            "evidence_ids": ["E-U-003"],
        },
        {
            "source_url": "https://mitadmissions.org/apply/firstyear/tests-scores/",
            "topics": ["undergraduate_admission", "tests", "english_requirement"],
            "url_type": "tests",
            "fact_type": "english_requirement",
            "fact_key": "undergraduate_english_minimums",
            "raw_value": "TOEFL Minimum: 90 Recommended: 100; IELTS Minimum: 7 Recommended: 7.5; DET Minimum: 120 Recommended: 125",
            "normalized_value": {"toefl_min": 90, "toefl_recommended": 100, "ielts_min": 7, "ielts_recommended": 7.5, "det_min": 120, "det_recommended": 125},
            "evidence_ids": ["E-U-004"],
        },
        {
            "source_url": "https://sfs.mit.edu/undergraduate-students/the-cost-of-attendance/coa/",
            "topics": ["undergraduate_cost", "tuition", "cost_of_attendance"],
            "url_type": "tuition_fee",
            "fact_type": "tuition",
            "fact_key": "undergraduate_tuition_2026_2027",
            "raw_value": "$66,720",
            "normalized_value": {"amount": 66720, "currency": "USD", "academic_year": "2026-2027"},
            "evidence_ids": ["E-U-005"],
        },
        {
            "source_url": "https://sfs.mit.edu/undergraduate-students/the-cost-of-attendance/coa/",
            "topics": ["undergraduate_cost", "cost_of_attendance"],
            "url_type": "tuition_fee",
            "fact_type": "cost_of_attendance",
            "fact_key": "undergraduate_total_coa_2026_2027",
            "raw_value": "$92,760",
            "normalized_value": {"amount": 92760, "currency": "USD", "academic_year": "2026-2027"},
            "evidence_ids": ["E-U-005"],
        },
        {
            "source_url": "https://sfs.mit.edu/undergraduate-students/cost-and-affordability/making-mit-affordable/",
            "topics": ["undergraduate_aid", "financial_aid_policy"],
            "url_type": "funding",
            "fact_type": "financial_aid_policy",
            "fact_key": "undergraduate_need_blind_full_need_international",
            "raw_value": "Need-blind and full-need for all undergraduate students, domestic and international.",
            "normalized_value": {"need_blind": True, "full_need": True, "international_included": True},
            "evidence_ids": ["E-U-006"],
        },
        {
            "source_url": "https://sfs.mit.edu/undergraduate-students/cost-and-affordability/making-mit-affordable/",
            "topics": ["undergraduate_aid", "financial_aid_policy"],
            "url_type": "funding",
            "fact_type": "financial_aid_policy",
            "fact_key": "undergraduate_tuition_free_income_threshold",
            "raw_value": "Families with annual income under $200,000 typically attend MIT tuition-free.",
            "normalized_value": {"income_threshold": 200000, "currency": "USD", "benefit": "tuition_free"},
            "evidence_ids": ["E-U-006"],
        },
    ]
    for fact in facts:
        source_id = add_source(
            source_registry_by_id,
            url_manifest_by_id,
            "mit",
            fact["source_url"],
            fact["topics"],
            fact["url_type"],
            capture_date,
            dataset_version,
        )
        quick_facts.append({
            "fact_id": stable_id("fact", "mit", fact["fact_key"], dataset_version),
            "university_id": "mit",
            "program_id": None,
            "entry_id": None,
            "fact_type": fact["fact_type"],
            "fact_key": fact["fact_key"],
            "raw_value": fact["raw_value"],
            "normalized_value": fact["normalized_value"],
            "unit": None,
            "currency": "USD" if "$" in fact["raw_value"] else None,
            "admission_cycle": "2026" if "2026" in fact["raw_value"] else None,
            "term": None,
            "source_id": source_id,
            "source_url": canonicalize_url(fact["source_url"]),
            "evidence_ids": fact["evidence_ids"],
            "weknora_chunk_ids": [],
            "capture_date": capture_date,
            "dataset_version": dataset_version,
            "source_version": None,
            "confidence": 0.95,
            "review_status": "review_required",
            "conflict_status": "none",
            "status": "active",
        })


def normalize_degree(value: str) -> str:
    allowed = {"SM", "MEng", "MArch", "MCP", "MASc", "MBA", "MBAn", "MFin", "MSMS", "PhD", "ScD"}
    return value if value in allowed else "Other"


def add_source(source_registry_by_id: dict, url_manifest_by_id: dict, university_id: str, url: str, topics: list[str], url_type: str, capture_date: str, dataset_version: str) -> str:
    # Plan §4.3 canonicalization (was a bare url.strip() before Task 3).
    canonical = canonicalize_url(url)
    parsed = urlparse(canonical)
    source_id = source_id_for(university_id, canonical)
    if source_id not in source_registry_by_id:
        source_registry_by_id[source_id] = {
            "source_id": source_id,
            "university_id": university_id,
            "program_id": None,
            "entry_ids": [],
            "source_url": canonical,
            "canonical_url": canonical,
            "url_type": url_type,
            "topics": sorted(set(topics)),
            "official_source": True,
            "priority": 1,
            "content_hash": None,
            "weknora_content_hash": None,
            "crawl_status": "not_applicable",
            "parser_status": "parsed",
            "weknora_import_status": "pending",
            "status": "active",
            "capture_date": capture_date,
            "last_verified": capture_date,
            "dataset_version": dataset_version,
            "source_version": None,
            "error_message": None,
        }
    else:
        source_registry_by_id[source_id]["topics"] = sorted(set(source_registry_by_id[source_id].get("topics", [])) | set(topics))
        if source_registry_by_id[source_id].get("url_type") == "overview" and url_type != "overview":
            source_registry_by_id[source_id]["url_type"] = url_type
    url_id = stable_id("url", source_id)
    if url_id not in url_manifest_by_id:
        url_manifest_by_id[url_id] = {
            "url_id": url_id,
            "source_id": source_id,
            "university_id": university_id,
            "program_id": None,
            "entry_ids": [],
            "source_url": canonical,
            "canonical_url": canonical,
            "url_type": url_type,
            "topics": sorted(set(topics)),
            "official_source": True,
            "priority": 1,
            "weknora_collection_id": None,
            "weknora_knowledge_id": None,
            "weknora_document_id": None,
            "weknora_chunk_ids": [],
            "import_status": "pending",
            "import_error": None,
            "content_hash": None,
            "capture_date": capture_date,
            "dataset_version": dataset_version,
            "source_version": None,
            "status": "active",
        }
    else:
        url_manifest_by_id[url_id]["topics"] = sorted(set(url_manifest_by_id[url_id].get("topics", [])) | set(topics))
        if url_manifest_by_id[url_id].get("url_type") == "overview" and url_type != "overview":
            url_manifest_by_id[url_id]["url_type"] = url_type
    return source_id


def add_markdown_prose_sources(
    text: str,
    source_registry_by_id: dict,
    url_manifest_by_id: dict,
    university_id: str,
    capture_date: str,
    dataset_version: str,
) -> int:
    unclassified = 0
    for extracted in deduplicate_extracted(extract_urls_from_markdown(text)).values():
        heading_topics = [slug(value) for value in extracted.heading_path[-3:] if slug(value)]
        if not heading_topics:
            unclassified += 1
        add_source(
            source_registry_by_id,
            url_manifest_by_id,
            university_id,
            extracted.canonical,
            sorted(set(["prose", *heading_topics])),
            "overview",
            capture_date,
            dataset_version,
        )
    return unclassified


def add_catalog_entry(catalog_entries: list[dict], source_registry_by_id: dict, url_manifest_by_id: dict, university_id: str, school: str, department: str, level: str, degree_level: str, program_name: str, url: str, capture_date: str, dataset_version: str, course_code: str | None = None, degree_full_name: str | None = None, raw_section_path: str | None = None) -> None:
    topics = ["catalog", "programs"]
    if "degree-charts" in url:
        topics.append("degree_chart")
    source_id = add_source(source_registry_by_id, url_manifest_by_id, university_id, url, topics, "degree_chart" if level == "undergraduate" else "program_admission", capture_date, dataset_version)
    entry_id = stable_id(
        "ent",
        university_id,
        level,
        degree_level,
        course_code or "",
        program_name,
        degree_full_name or "",
    )
    catalog_entries.append({
        "entry_id": entry_id,
        "university_id": university_id,
        "program_id": None,
        "school": cleanup_markdown(school),
        "department": cleanup_markdown(department),
        "level": level,
        "degree_level": degree_level,
        "degree_full_name": cleanup_markdown(degree_full_name) if degree_full_name else None,
        "course_code": cleanup_markdown(course_code) if course_code else None,
        "program_name": cleanup_markdown(program_name),
        "canonical_program_name": cleanup_markdown(program_name),
        "aliases": [],
        "source_id": source_id,
        "source_url": canonicalize_url(url),
        "topics": topics,
        "search_text": " ".join(filter(None, [university_id.upper(), school, department, degree_level, course_code or "", program_name])),
        "cross_school": "跨学院" in program_name,
        "cross_school_names": [],
        "raw_section_path": raw_section_path,
        "capture_date": capture_date,
        "dataset_version": dataset_version,
        "source_version": None,
        "status": "active",
    })
    source_registry_by_id[source_id]["entry_ids"].append(entry_id)
    url_manifest_by_id[stable_id("url", source_id)]["entry_ids"].append(entry_id)


def cleanup_markdown(value: str | None) -> str:
    if not value:
        return ""
    value = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"\*\*|`", "", value)
    return value.strip()


def normalize_fact_value(fact_type: str, raw_value: str):
    if fact_type == "application_fee":
        match = re.search(r"\$(\d+(?:\.\d+)?)", raw_value)
        return {"amount": float(match.group(1)), "currency": "USD"} if match else {"raw": raw_value}
    if fact_type == "english_requirement":
        result = {}
        for key in ["IELTS", "TOEFL", "DET"]:
            match = re.search(key + r"\s+(\d+(?:\.\d+)?)", raw_value)
            if match:
                result[key.lower()] = float(match.group(1))
        return result or {"raw": raw_value}
    return {"raw": raw_value}
