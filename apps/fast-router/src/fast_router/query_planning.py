from __future__ import annotations

import re
from dataclasses import dataclass


FACT_TYPE_TERMS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("deadline", ("deadline", "截止")),
    ("application_fee", ("申请费", "application fee")),
    ("english_requirement", ("toefl", "ielts", "det", "语言")),
    ("gre_gmat_policy", ("gre", "gmat", "标化")),
    ("funding_model", ("funding", "资助", "奖学金")),
    ("tuition", ("学费", "tuition")),
    ("cost_of_attendance", ("cost", "coa", "费用")),
)

DETAIL_ASPECT_TERMS: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("application_materials", ("申请材料", "提交哪些材料", "需要哪些材料", "application materials", "required materials", "required documents", "application documents", "transcript", "transcripts", "recommendation letter")),
    ("curriculum_detail", ("课程设置", "课程内容", "有哪些课程", "curriculum", "coursework")),
    ("eligibility_policy", ("申请资格", "能不能申请", "是否可以申请", "eligibility", "eligible")),
    ("student_culture", ("校园文化", "学生文化", "student culture", "campus culture")),
    ("application_requirements", ("申请要求", "入学要求", "application requirements", "admission requirements", "complete requirements")),
)


def infer_fact_types(query: str) -> list[str]:
    lowered = query.lower()
    return [fact_type for fact_type, terms in FACT_TYPE_TERMS if any(term in lowered for term in terms)]


def detect_course_codes(query: str) -> tuple[str, ...]:
    codes = re.findall(r"(?<!\d)(\d{1,2}-\d{1,2})(?!\d)", query)
    course_numbers = re.findall(r"\bcourse\s+(\d{1,2})\b", query, re.IGNORECASE)
    return tuple(dict.fromkeys([*codes, *course_numbers]))


@dataclass(frozen=True)
class QueryPlan:
    stage: str
    requested_aspects: tuple[str, ...]
    course_codes: tuple[str, ...]
    max_primary_entities: int


def plan_query(query: str) -> QueryPlan:
    lowered = query.lower()
    max_primary_entities = 3 if any(term in lowered for term in ("关系", "比较", "对比", "compare", "relationship")) else 1
    aspects = tuple(
        aspect
        for aspect, terms in DETAIL_ASPECT_TERMS
        if any(term in lowered for term in terms)
    )
    if aspects:
        return QueryPlan(
            stage="detail",
            requested_aspects=aspects,
            course_codes=detect_course_codes(query),
            max_primary_entities=max_primary_entities,
        )
    fact_types = infer_fact_types(query)
    if fact_types:
        return QueryPlan(
            stage="fact",
            requested_aspects=tuple(fact_types),
            course_codes=detect_course_codes(query),
            max_primary_entities=1,
        )
    return QueryPlan(
        stage="discovery",
        requested_aspects=(),
        course_codes=detect_course_codes(query),
        max_primary_entities=max_primary_entities,
    )
