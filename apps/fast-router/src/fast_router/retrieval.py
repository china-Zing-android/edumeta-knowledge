from __future__ import annotations

import time
import uuid
from typing import Any

from catalog_parser.disciplines import resolve_discipline_query
from .opensearch_retrieval import OpenSearchRetrievalClient, detected_course_code, detected_program_slug, infer_fact_types
from .query_planning import QueryPlan, plan_query


PROGRAM_TOPIC_PRIORITY = {
    "curriculum": 0,
    "application_requirements": 1,
    "tuition": 2,
    "deadline": 3,
    "student_culture": 4,
    "funding": 5,
    "english_requirement": 6,
    "standardized_tests": 7,
    "financial_aid": 8,
    "cost_of_attendance": 9,
    "application_fee": 10,
}


def empty_context() -> dict[str, Any]:
    return {
        "primary_entities": [],
        "highlights": [],
        "sample_children": [],
        "related_entities": [],
        "available_topics": [],
        "presentation_hints": {
            "order": ["direct_answer", "context", "related_entities", "available_topics"],
            "explain_course_codes": True,
            "allow_qualitative_inference": False,
            "max_related_entities": 2,
            "max_available_topics": 4,
        },
        "provenance": {"origin": "md_projection", "dataset_version": None},
    }


def _compact_entity(row: dict[str, Any]) -> dict[str, Any]:
    return {
        key: row.get(key)
        for key in (
            "entity_type", "entity_id", "entry_id", "title", "display_label",
            "attributes", "source_ids",
        )
    }


def compose_context(rows: list[dict[str, Any]], dataset_version: str | None, max_primary_entities: int = 3) -> dict[str, Any]:
    payload = empty_context()
    payload["provenance"]["dataset_version"] = dataset_version
    primary_rows = rows[:max_primary_entities]
    payload["primary_entities"] = [_compact_entity(row) for row in primary_rows]
    if not primary_rows:
        return payload

    payload["highlights"] = list(primary_rows[0].get("highlights") or [])
    payload["sample_children"] = list(primary_rows[0].get("sample_children") or [])[:5]
    related: list[dict[str, Any]] = []
    primary_entity_ids = {str(row.get("entity_id") or row.get("entry_id") or "") for row in primary_rows}
    seen_related: set[str] = set()
    for primary in primary_rows:
        for item in (primary.get("related_entities") or [])[:2]:
            entity_id = str(item.get("entity_id") or item.get("entry_id") or "")
            if not entity_id or entity_id in primary_entity_ids or entity_id in seen_related:
                continue
            seen_related.add(entity_id)
            related.append({
                **_compact_entity(item),
                "relation_type": item.get("relation_type"),
                "relation_reason": item.get("relation_reason"),
                "primary_entity_id": primary.get("entity_id"),
            })
    payload["related_entities"] = related

    topics: dict[str, dict[str, Any]] = {}
    for primary in primary_rows:
        for item in primary.get("available_topics") or []:
            topic = str(item.get("topic") or "")
            if not topic:
                continue
            current = topics.get(topic)
            if current is None or (current.get("availability") != "l1" and item.get("availability") == "l1"):
                topics[topic] = item
    if primary_rows[0].get("entity_type") == "program":
        topic_sort_key = lambda item: (
            PROGRAM_TOPIC_PRIORITY.get(str(item.get("topic")), 100),
            str(item.get("topic")),
        )
    else:
        topic_sort_key = lambda item: (
            item.get("availability") != "l1",
            str(item.get("topic")),
        )
    payload["available_topics"] = sorted(topics.values(), key=topic_sort_key)[:4]
    return payload


def scoped_sources(
    sources: list[dict[str, Any]],
    context_rows: list[dict[str, Any]],
    request_context: dict[str, Any],
    plan: QueryPlan,
) -> list[dict[str, Any]]:
    explicit_entry_id = request_context.get("entry_id") or request_context.get("program_id")
    relevant_contexts = context_rows
    if explicit_entry_id:
        relevant_contexts = [
            row for row in context_rows
            if row.get("entry_id") == explicit_entry_id or row.get("entity_id") == explicit_entry_id
        ]
    allowed_source_ids = {
        source_id
        for row in relevant_contexts
        for source_id in row.get("source_ids") or []
    }
    allowed_entry_ids = {
        str(row.get("entry_id") or row.get("entity_id"))
        for row in relevant_contexts
        if row.get("entity_type") == "program"
    }
    if explicit_entry_id:
        allowed_entry_ids.add(str(explicit_entry_id))
    scoped: list[dict[str, Any]] = []
    for source in sources:
        source_entries = {str(value) for value in source.get("entry_ids") or []}
        if source.get("source_id") in allowed_source_ids or source_entries & allowed_entry_ids:
            scoped.append(source)
    return scoped


def infer_search_direction(
    query: str,
    university_id: str | None,
    filters: dict[str, Any],
    requested_direction: str,
) -> str:
    if requested_direction != "auto":
        return requested_direction
    if university_id:
        return "downward"
    lowered = query.lower()
    explicit_upward_terms = (
        "哪些院校", "哪些学校", "院校有哪些", "学校有哪些", "什么院校", "什么学校",
        "which universities", "which colleges", "what universities", "what colleges",
    )
    if resolve_discipline_query(query) and any(term in lowered for term in explicit_upward_terms):
        return "upward"
    if any(filters.get(key) for key in ("country_codes", "regions", "degree_levels", "levels", "school_tiers")):
        return "range"
    return "downward"


class RetrievalEngine:
    def __init__(self, l1: OpenSearchRetrievalClient, weknora: Any | None = None) -> None:
        self.l1 = l1
        self.weknora = weknora

    def retrieve(
        self,
        *,
        query: str,
        university_id: str | None,
        context: dict[str, Any],
        max_results: int,
        filters: dict[str, Any] | None = None,
        direction: str = "auto",
    ) -> dict[str, Any]:
        started = time.perf_counter()
        trace_id = f"tr_{uuid.uuid4().hex}"
        filters = filters or {}
        resolved_id, dataset_version = self.l1.resolve_university(query, university_id)
        if university_id and not resolved_id:
            return self._response(
                trace_id, "not_found", None, [], [], [], ["unknown_university"], started, 0, 0,
            )
        resolved_direction = infer_search_direction(query, resolved_id, filters, direction)
        if resolved_direction in {"range", "upward"}:
            discipline = resolve_discipline_query(query)
            if resolved_direction == "upward" and not discipline:
                response = self._response(
                    trace_id, "clarification", None, [], [], ["discipline"], [], started, 0, 0,
                )
                response["scope"]["direction"] = resolved_direction
                return response
            cross = self.l1.search_across_universities(
                query=query if resolved_direction == "upward" else "",
                discipline_ids=list(discipline.expanded_ids) if discipline else [],
                filters=filters,
                max_results=max_results,
            )
            mode = resolved_direction if cross.matches else "not_found"
            response = self._response(
                trace_id, mode, None, cross.matches, [], [], [], started, cross.elapsed_ms, 0,
            )
            response["scope"].update({
                "direction": resolved_direction,
                "discipline_id": discipline.primary_id if discipline else None,
                "filters": filters,
            })
            return response
        if not resolved_id:
            mode = "not_found" if university_id else "clarification"
            return self._response(
                trace_id, mode, None, [], [], ["university_id"] if not university_id else [],
                ["unknown_university"] if university_id else [], started, 0, 0,
            )

        query_plan = plan_query(query)
        result = self.l1.search(
            query=query,
            university_id=resolved_id,
            dataset_version=dataset_version,
            max_results=max_results,
            context=context,
            query_plan=query_plan,
        )
        context_payload = compose_context(result.contexts, dataset_version, query_plan.max_primary_entities)
        warnings: list[str] = []
        fact_types = infer_fact_types(query)
        program_slug = detected_program_slug(query)
        course_code = detected_course_code(query)

        if query_plan.stage == "fact" and fact_types and result.facts:
            source_count = len({row.get("source_id") for row in result.facts})
            if source_count > 1 and not program_slug and fact_types not in (["tuition"], ["cost_of_attendance"]):
                return self._response(trace_id, "clarification", resolved_id, [], [], ["program_id"], [], started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)
            for fact in result.facts:
                if fact.get("review_status") != "approved":
                    warnings.append("fact_review_required")
                if fact.get("conflict_status") not in (None, "none"):
                    warnings.append("fact_conflict")
            return self._response(trace_id, "l1", resolved_id, result.facts, [], [], sorted(set(warnings)), started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)

        if query_plan.stage == "discovery" and (result.catalog or result.contexts):
            primary_ids = {row.get("entity_id") for row in context_payload["primary_entities"]}
            matches = [row for row in result.catalog if row.get("entry_id") in primary_ids]
            if not matches:
                matches = result.catalog[:query_plan.max_primary_entities]
            if not matches:
                matches = context_payload["primary_entities"]
            return self._response(trace_id, "l1", resolved_id, matches, [], [], [], started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)

        resolved_program_scope = bool(
            context.get("entry_id")
            or context.get("program_id")
            or program_slug
            or course_code
        )
        if query_plan.stage == "detail" and not resolved_program_scope:
            return self._response(trace_id, "clarification", resolved_id, [], [], ["program_id_or_entry_id"], [], started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)

        sources = scoped_sources(result.sources, result.contexts, context, query_plan)
        if query_plan.stage in {"detail", "fact"} and sources:
            if not self.weknora:
                return self._response(trace_id, "l1_l2", resolved_id, [], [], [], ["weknora_unavailable"], started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)
            wk_started = time.perf_counter()
            try:
                evidence = self.weknora.search(resolved_id, query, sources, top_k=max_results)
                wk_ms = round((time.perf_counter() - wk_started) * 1000, 3)
            except Exception:  # evidence is optional degradation; structured log carries trace.
                return self._response(trace_id, "l1_l2", resolved_id, [], [], [], ["evidence_timeout_or_error"], started, result.elapsed_ms, round((time.perf_counter() - wk_started) * 1000, 3), dataset_version, context_payload, query_plan)
            if evidence:
                return self._response(trace_id, "l1_l2", resolved_id, [], evidence, [], [], started, result.elapsed_ms, wk_ms, dataset_version, context_payload, query_plan)
            return self._response(trace_id, "not_found", resolved_id, [], [], [], ["missing_evidence"], started, result.elapsed_ms, wk_ms, dataset_version, context_payload, query_plan)
        warnings = ["missing_evidence"] if query_plan.stage in {"detail", "fact"} else []
        return self._response(trace_id, "not_found", resolved_id, [], [], [], warnings, started, result.elapsed_ms, 0, dataset_version, context_payload, query_plan)

    @staticmethod
    def _response(
        trace_id: str,
        mode: str,
        university_id: str | None,
        matches: list[dict[str, Any]],
        evidence: list[dict[str, Any]],
        missing_slots: list[str],
        warnings: list[str],
        started: float,
        l1_ms: float,
        weknora_ms: float,
        dataset_version: str | None = None,
        context_payload: dict[str, Any] | None = None,
        query_plan: QueryPlan | None = None,
    ) -> dict[str, Any]:
        query_plan = query_plan or QueryPlan(stage="discovery", requested_aspects=(), course_codes=(), max_primary_entities=1)
        return {
            "trace_id": trace_id,
            "mode": mode,
            "scope": {
                "university_id": university_id,
                "dataset_version": dataset_version,
                "direction": "downward",
                "stage": query_plan.stage,
                "requested_aspects": list(query_plan.requested_aspects),
            },
            "matches": matches,
            "context": context_payload or empty_context(),
            "evidence": evidence,
            "missing_slots": missing_slots,
            "warnings": warnings,
            "timings": {
                "total_ms": round((time.perf_counter() - started) * 1000, 3),
                "l1_ms": l1_ms,
                "weknora_ms": weknora_ms,
            },
        }
