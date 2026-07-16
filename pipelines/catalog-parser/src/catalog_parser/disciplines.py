from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DisciplineDefinition:
    discipline_id: str
    label: str
    aliases: tuple[str, ...]


@dataclass(frozen=True)
class ResolvedDiscipline:
    primary_id: str
    expanded_ids: tuple[str, ...]


DISCIPLINES: tuple[DisciplineDefinition, ...] = (
    DisciplineDefinition("medicine", "Medicine", ("medicine", "medical science", "医学", "临床医学")),
    DisciplineDefinition(
        "health_sciences",
        "Health Sciences",
        ("health sciences", "health science", "public health", "健康科学", "公共卫生"),
    ),
    DisciplineDefinition(
        "biomedical_engineering",
        "Biomedical Engineering",
        ("biomedical engineering", "medical engineering", "生物医学工程", "医学工程"),
    ),
    DisciplineDefinition("biology", "Biology", ("biology", "biological science", "microbiology", "生物学", "生物科学", "微生物")),
    DisciplineDefinition("computer_science", "Computer Science", ("computer science", "computing", "informatics", "计算机", "计算科学")),
    DisciplineDefinition("artificial_intelligence", "Artificial Intelligence", ("artificial intelligence", "machine learning", "人工智能", "机器学习")),
    DisciplineDefinition("data_science", "Data Science", ("data science", "analytics", "数据科学", "数据分析")),
    DisciplineDefinition("economics", "Economics", ("economics", "economic", "经济学", "经济")),
    DisciplineDefinition("business", "Business and Management", ("business", "management", "mba", "商业", "工商管理", "管理学")),
    DisciplineDefinition("engineering", "Engineering", ("engineering", "工程学", "工程")),
    DisciplineDefinition("mathematics", "Mathematics", ("mathematics", "mathematical", "数学")),
    DisciplineDefinition("physics", "Physics", ("physics", "物理学", "物理")),
    DisciplineDefinition("chemistry", "Chemistry", ("chemistry", "chemical science", "化学")),
    DisciplineDefinition("architecture", "Architecture", ("architecture", "architectural", "建筑学", "建筑")),
    DisciplineDefinition("other", "Other", ()),
)

DISCIPLINE_BY_ID = {item.discipline_id: item for item in DISCIPLINES}

QUERY_EXPANSIONS: dict[str, tuple[str, ...]] = {
    "medicine": ("medicine", "health_sciences", "biomedical_engineering"),
}


def _normalized_text(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", " ", value)
    return " ".join(value.split())


def _contains_alias(text: str, alias: str) -> bool:
    normalized_alias = _normalized_text(alias)
    if not normalized_alias:
        return False
    if re.search(r"[\u4e00-\u9fff]", normalized_alias):
        return normalized_alias in text
    return re.search(rf"(?<![a-z0-9]){re.escape(normalized_alias)}(?![a-z0-9])", text) is not None


def classify_catalog_entry(entry: dict[str, Any]) -> list[str]:
    text = _normalized_text(
        " ".join(
            str(entry.get(key) or "")
            for key in ("program_name", "canonical_program_name", "department", "school", "search_text")
        )
        + " "
        + " ".join(str(value) for value in entry.get("topics") or [])
    )
    matches = [
        definition.discipline_id
        for definition in DISCIPLINES
        if definition.discipline_id != "other"
        and any(_contains_alias(text, alias) for alias in definition.aliases)
    ]
    return matches or ["other"]


def enrich_catalog_entries(entries: list[dict[str, Any]]) -> None:
    for entry in entries:
        discipline_ids = classify_catalog_entry(entry)
        entry["discipline_ids"] = discipline_ids
        entry["discipline_labels"] = [DISCIPLINE_BY_ID[item].label for item in discipline_ids]


def resolve_discipline_query(query: str) -> ResolvedDiscipline | None:
    text = _normalized_text(query)
    candidates: list[tuple[int, str]] = []
    for definition in DISCIPLINES:
        if definition.discipline_id == "other":
            continue
        for alias in definition.aliases:
            if _contains_alias(text, alias):
                candidates.append((len(_normalized_text(alias)), definition.discipline_id))
    if not candidates:
        return None
    _, primary_id = max(candidates, key=lambda item: item[0])
    return ResolvedDiscipline(primary_id, QUERY_EXPANSIONS.get(primary_id, (primary_id,)))
