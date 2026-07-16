from __future__ import annotations

import re
from collections import defaultdict
from typing import Any

from .markdown_sources import stable_id


FACT_TOPIC_NAMES = {
    "application_fee": "application_fee",
    "cost_of_attendance": "cost_of_attendance",
    "deadline": "deadline",
    "english_requirement": "english_requirement",
    "financial_aid_policy": "financial_aid",
    "funding_model": "funding",
    "gre_gmat_policy": "standardized_tests",
    "tuition": "tuition",
}

SOURCE_TOPIC_NAMES = {
    "admission_requirements": "application_requirements",
    "application": "application_requirements",
    "culture": "student_culture",
    "degree_chart": "curriculum",
    "funding": "funding",
    "student_culture": "student_culture",
    "tests": "standardized_tests",
}


def _plain_program_name(value: str) -> str:
    return re.split(r"\s*⚠\s*跨学院\s*:", value, maxsplit=1)[0].strip()


def _display_label(entry: dict[str, Any]) -> str:
    title = _plain_program_name(str(entry.get("program_name") or ""))
    course_code = str(entry.get("course_code") or "").strip()
    if course_code:
        return f"{course_code} {title}"
    degree_level = str(entry.get("degree_level") or "").strip()
    if entry.get("level") == "graduate" and degree_level:
        return f"{title} ({degree_level})"
    return title


def _topic_rows(
    *,
    facts: list[dict[str, Any]],
    sources: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    topics: dict[str, dict[str, Any]] = {}
    for fact in facts:
        topic = FACT_TOPIC_NAMES.get(str(fact.get("fact_type") or ""))
        if not topic:
            continue
        row = topics.setdefault(topic, {"topic": topic, "availability": "l1", "source_ids": []})
        source_id = fact.get("source_id")
        if source_id and source_id not in row["source_ids"]:
            row["source_ids"].append(source_id)
    for source in sources:
        for source_topic in source.get("topics") or []:
            topic = SOURCE_TOPIC_NAMES.get(str(source_topic))
            if not topic:
                continue
            row = topics.setdefault(topic, {"topic": topic, "availability": "weknora", "source_ids": []})
            if row["availability"] != "l1":
                row["availability"] = "weknora"
            source_id = source.get("source_id")
            if source_id and source_id not in row["source_ids"]:
                row["source_ids"].append(source_id)
    result: list[dict[str, Any]] = []
    for _, row in sorted(topics.items()):
        source_ids = sorted(row["source_ids"])
        result.append({**row, "source_ids": source_ids[:5], "source_count": len(source_ids)})
    return result


def _sample_schools(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_school: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        school = str(entry.get("school") or "").strip()
        if school:
            by_school[school].append(entry)

    result: list[dict[str, Any]] = []
    sampled_schools = sorted(by_school, key=lambda school: (-len(by_school[school]), school))[:5]
    for school in sampled_schools:
        school_entries = by_school[school]
        departments = sorted({str(row.get("department") or "").strip() for row in school_entries if row.get("department")})
        sample_programs = sorted(
            (
                {
                    "entity_id": row["entry_id"],
                    "title": _plain_program_name(str(row.get("program_name") or "")),
                    "display_label": _display_label(row),
                    "source_id": row.get("source_id"),
                }
                for row in school_entries
            ),
            key=lambda row: (row["display_label"].lower(), row["entity_id"]),
        )[:3]
        result.append(
            {
                "entity_type": "school",
                "entity_id": stable_id("school", school),
                "title": school,
                "sample_departments": departments[:3],
                "sample_programs": sample_programs,
            }
        )
    return result


def _relation(entry: dict[str, Any], candidate: dict[str, Any]) -> tuple[int, str, str] | None:
    if entry.get("level") != candidate.get("level"):
        return None
    shared_disciplines = sorted(set(entry.get("discipline_ids") or []) & set(candidate.get("discipline_ids") or []))
    entry_label = _display_label(entry)
    if candidate.get("cross_school") and shared_disciplines:
        return (
            300,
            "interdisciplinary_related",
            f"Same university and study level as {entry_label}; shares {', '.join(shared_disciplines)} and is marked cross-school.",
        )
    if entry.get("department") == candidate.get("department") and entry.get("degree_level") == candidate.get("degree_level"):
        return (
            250,
            "same_department_and_degree",
            f"Same university, department, study level, and degree level as {entry_label}.",
        )
    if entry.get("department") == candidate.get("department"):
        return (200, "same_department", f"Same university, department, and study level as {entry_label}.")
    if shared_disciplines and entry.get("degree_level") == candidate.get("degree_level"):
        return (
            150,
            "same_discipline_and_degree",
            f"Same university, study level, and degree level as {entry_label}; shares {', '.join(shared_disciplines)}.",
        )
    if shared_disciplines:
        return (100, "same_discipline", f"Same university and study level as {entry_label}; shares {', '.join(shared_disciplines)}.")
    return None


def _related_entities(entry: dict[str, Any], entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    ranked: list[tuple[int, str, dict[str, Any]]] = []
    for candidate in entries:
        if candidate.get("entry_id") == entry.get("entry_id"):
            continue
        relation = _relation(entry, candidate)
        if relation is None:
            continue
        score, relation_type, relation_reason = relation
        ranked.append(
            (
                score,
                str(candidate.get("entry_id")),
                {
                    "entity_type": "program",
                    "entity_id": candidate["entry_id"],
                    "entry_id": candidate["entry_id"],
                    "title": _plain_program_name(str(candidate.get("program_name") or "")),
                    "display_label": _display_label(candidate),
                    "attributes": {
                        "course_code": candidate.get("course_code"),
                        "degree_level": candidate.get("degree_level"),
                        "department": candidate.get("department"),
                        "school": candidate.get("school"),
                    },
                    "relation_type": relation_type,
                    "relation_reason": relation_reason,
                    "source_ids": [candidate["source_id"]] if candidate.get("source_id") else [],
                },
            )
        )
    ranked.sort(key=lambda item: (-item[0], item[1]))
    result: list[dict[str, Any]] = []
    seen_labels: set[str] = set()
    for _, _, row in ranked:
        if row["display_label"] in seen_labels:
            continue
        seen_labels.add(row["display_label"])
        result.append(row)
        if len(result) == 2:
            break
    return result


def _program_facts(entry: dict[str, Any], facts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    source_id = entry.get("source_id")
    entry_id = entry.get("entry_id")
    result = [row for row in facts if row.get("entry_id") == entry_id or row.get("source_id") == source_id]
    if entry.get("level") == "undergraduate":
        result.extend(
            row
            for row in facts
            if "undergraduate" in str(row.get("fact_id") or "") and row not in result
        )
    return result


def build_entity_contexts(
    *,
    university_id: str,
    university_name: str,
    country_code: str | None,
    region: str | None,
    catalog_entries: list[dict[str, Any]],
    quick_facts: list[dict[str, Any]],
    source_registry: list[dict[str, Any]],
    dataset_version: str,
) -> list[dict[str, Any]]:
    sources_by_id = {row["source_id"]: row for row in source_registry}
    undergraduate_sb_count = sum(1 for row in catalog_entries if row.get("degree_level") == "SB")
    undergraduate_minor_count = sum(1 for row in catalog_entries if row.get("degree_level") == "Minor")
    graduate_count = sum(1 for row in catalog_entries if row.get("level") == "graduate")
    cross_school_count = sum(1 for row in catalog_entries if row.get("cross_school"))
    sample_children = _sample_schools(catalog_entries)
    sample_source_ids = sorted(
        {
            program["source_id"]
            for child in sample_children
            for program in child.get("sample_programs") or []
            if program.get("source_id")
        }
    )
    contexts: list[dict[str, Any]] = [
        {
            "context_id": stable_id("ctx", university_id, "university", university_id),
            "entity_type": "university",
            "entity_id": university_id,
            "university_id": university_id,
            "entry_id": None,
            "title": university_name,
            "display_label": university_name,
            "attributes": {
                "country_code": country_code,
                "region": region,
            },
            "highlights": [
                {"kind": "catalog_count", "label": "Undergraduate SB programs", "value": undergraduate_sb_count},
                {"kind": "catalog_count", "label": "Undergraduate minors", "value": undergraduate_minor_count},
                {"kind": "catalog_count", "label": "Graduate degree offerings", "value": graduate_count},
                {"kind": "structure_count", "label": "Cross-school catalog entries", "value": cross_school_count},
            ],
            "sample_children": sample_children,
            "related_entities": [],
            "available_topics": _topic_rows(facts=quick_facts, sources=source_registry),
            "source_ids": sample_source_ids[:15],
            "md_section_paths": sorted({str(row.get("raw_section_path")) for row in catalog_entries if row.get("raw_section_path")})[:5],
            "dataset_version": dataset_version,
            "status": "active",
        }
    ]

    for entry in sorted(catalog_entries, key=lambda row: str(row["entry_id"])):
        source = sources_by_id.get(entry.get("source_id"), {})
        entry_facts = _program_facts(entry, quick_facts)
        contexts.append(
            {
                "context_id": stable_id("ctx", university_id, "program", entry["entry_id"]),
                "entity_type": "program",
                "entity_id": entry["entry_id"],
                "university_id": university_id,
                "entry_id": entry["entry_id"],
                "title": _plain_program_name(str(entry.get("program_name") or "")),
                "display_label": _display_label(entry),
                "attributes": {
                    "course_code": entry.get("course_code"),
                    "course_code_system": "MIT Course number" if university_id == "mit" and entry.get("course_code") else None,
                    "program_id": entry.get("program_id"),
                    "degree_level": entry.get("degree_level"),
                    "degree_full_name": entry.get("degree_full_name"),
                    "level": entry.get("level"),
                    "department": entry.get("department"),
                    "school": entry.get("school"),
                    "discipline_ids": entry.get("discipline_ids") or [],
                    "cross_school": bool(entry.get("cross_school")),
                },
                "highlights": [],
                "sample_children": [],
                "related_entities": _related_entities(entry, catalog_entries),
                "available_topics": _topic_rows(facts=entry_facts, sources=[source] if source else []),
                "source_ids": [entry["source_id"]] if entry.get("source_id") else [],
                "md_section_paths": [entry["raw_section_path"]] if entry.get("raw_section_path") else [],
                "dataset_version": dataset_version,
                "status": "active",
            }
        )
    return contexts
