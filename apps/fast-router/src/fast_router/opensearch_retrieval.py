from __future__ import annotations

import re
import threading
import time
from dataclasses import dataclass
from typing import Any

from .query_planning import QueryPlan, detect_course_codes, infer_fact_types, plan_query


CATALOG_INTENT_TERMS = (
    "有哪些", "专业", "项目", "program", "programs", "major", "minor", "本科", "研究生",
    "undergraduate", "graduate", "master", "phd", "要求", "是什么", "吗", "mit", "有", "相关",
)

PROGRAM_ALIASES = {
    "eecs": "electrical-engineering-and-computer-science",
    "electrical engineering and computer science": "electrical-engineering-and-computer-science",
    "cs": "computer-science",
    "computer science": "computer-science",
    "economics": "economics",
    "linguistics": "linguistics",
    "microbiology": "microbiology",
    "biology": "biology",
    "sloan mba": "mit-sloan-mba-program",
}


def infer_level(query: str) -> str | None:
    q = query.lower()
    if any(term in q for term in ("本科", "undergraduate", "bachelor")):
        return "undergraduate"
    if any(term in q for term in ("研究生", "graduate", "master", "phd", "ph.d")):
        return "graduate"
    return None


def infer_degree_constraint(query: str) -> tuple[str, list[str] | str | None]:
    q = query.lower()
    if re.search(r"\bph\.?d\b", q):
        return "include", "PhD"
    if "minor" in q or "辅修" in q:
        return "include", "Minor"
    if re.search(r"\bm\.?s\b", q) and "master" not in q:
        return "include", "SM"
    if any(term in q for term in ("master", "硕士")):
        return "include", ["SM", "MEng", "MArch", "MCP", "MASc", "MBA", "MBAn", "MFin", "MSMS"]
    if any(term in q for term in ("major", "本科专业", "undergraduate program", "undergraduate major")):
        return "exclude", ["Minor", "Certificate"]
    if any(term in q for term in ("graduate program", "研究生项目")):
        return "exclude", ["SB", "Minor"]
    return "none", None


def normalized_catalog_query(query: str) -> str:
    value = query.lower()
    value = re.sub(r"\bai\b", "artificial intelligence", value)
    value = re.sub(r"\beecs\b", "electrical engineering computer science", value)
    value = re.sub(r"\bcs\b", "computer science", value)
    for term in CATALOG_INTENT_TERMS:
        value = value.replace(term, " ")
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff-]+", " ", value)
    return " ".join(value.split())


def detected_course_code(query: str) -> str | None:
    codes = detect_course_codes(query)
    return codes[0] if codes else None


def detected_program_slug(query: str) -> str | None:
    q = query.lower()
    for alias in sorted(PROGRAM_ALIASES, key=len, reverse=True):
        if re.search(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", q):
            return PROGRAM_ALIASES[alias]
    return None


@dataclass(frozen=True)
class L1SearchResult:
    university_id: str
    dataset_version: str
    catalog: list[dict[str, Any]]
    facts: list[dict[str, Any]]
    sources: list[dict[str, Any]]
    contexts: list[dict[str, Any]]
    elapsed_ms: float


@dataclass(frozen=True)
class CrossUniversitySearchResult:
    matches: list[dict[str, Any]]
    elapsed_ms: float


class CurrentVersionMap:
    def __init__(
        self,
        postgres_dsn: str | None = None,
        *,
        initial: dict[str, str] | None = None,
        initial_aliases: dict[str, list[str]] | None = None,
    ) -> None:
        self.postgres_dsn = postgres_dsn
        self._versions = dict(initial or {})
        provided_aliases = initial_aliases or {}
        self._aliases = {
            university_id: {
                university_id,
                *(alias.lower() for alias in provided_aliases.get(university_id, []) if alias),
                *({"massachusetts institute of technology"} if university_id == "mit" else set()),
            }
            for university_id in self._versions
        }
        self._lock = threading.Lock()
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None

    def refresh(self) -> dict[str, str]:
        if not self.postgres_dsn:
            return self.snapshot()
        import psycopg

        with psycopg.connect(self.postgres_dsn) as connection, connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT sv.university_id, sv.dataset_version, u.university_name, u.aliases
                  FROM school_versions sv
                  JOIN universities u ON u.university_id = sv.university_id
                 WHERE sv.publication_state='current' AND u.status='active'
                """
            )
            rows = cursor.fetchall()
            versions = {row[0]: row[1] for row in rows}
            aliases = {
                row[0]: {
                    row[0],
                    *(str(alias).lower() for alias in (row[3] or []) if alias),
                    *({str(row[2]).lower()} if row[2] else set()),
                }
                for row in rows
            }
        with self._lock:
            self._versions = versions
            self._aliases = aliases
        return versions

    def snapshot(self) -> dict[str, str]:
        with self._lock:
            return dict(self._versions)

    def get(self, university_id: str) -> str | None:
        with self._lock:
            return self._versions.get(university_id)

    def resolve(self, query: str) -> str | None:
        lowered = query.lower()
        with self._lock:
            aliases = {key: set(values) for key, values in self._aliases.items()}
        for university_id, names in aliases.items():
            if any(re.search(rf"(?<![a-z0-9]){re.escape(name)}(?![a-z0-9])", lowered) for name in names):
                return university_id
        return None

    def start(self, interval_seconds: float = 5) -> None:
        if not self.postgres_dsn or (self._thread and self._thread.is_alive()):
            return

        def poll() -> None:
            while not self._stop.wait(interval_seconds):
                try:
                    self.refresh()
                except Exception:
                    continue

        self._thread = threading.Thread(target=poll, name="version-map-refresh", daemon=True)
        self._thread.start()

    def close(self) -> None:
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=2)


class OpenSearchRetrievalClient:
    def __init__(self, opensearch_url: str, version_map: CurrentVersionMap, *, client: Any | None = None) -> None:
        if client is None:
            from opensearchpy import OpenSearch

            client = OpenSearch(opensearch_url, timeout=0.45, max_retries=0, retry_on_timeout=False)
        self.client = client
        self.version_map = version_map

    def resolve_university(self, query: str, requested_id: str | None) -> tuple[str | None, str | None]:
        versions = self.version_map.snapshot()
        if requested_id:
            university_id = requested_id.strip().lower()
            return (university_id, versions.get(university_id)) if university_id in versions else (None, None)
        university_id = self.version_map.resolve(query)
        return (university_id, versions.get(university_id)) if university_id else (None, None)

    def search(self, *, query: str, university_id: str, dataset_version: str, max_results: int = 5, context: dict[str, Any] | None = None, query_plan: QueryPlan | None = None) -> L1SearchResult:
        started = time.perf_counter()
        context = context or {}
        query_plan = query_plan or plan_query(query)
        requested_entry_id = context.get("entry_id")
        requested_program_id = context.get("program_id")
        course_code = detected_course_code(query)
        program_slug = detected_program_slug(query)
        fact_types = infer_fact_types(query) if query_plan.stage == "fact" else []
        level = context.get("level") or infer_level(query)
        catalog_query = normalized_catalog_query(query)
        common_filters: list[dict[str, Any]] = [
            {"term": {"university_id": university_id}},
            {"term": {"dataset_version": dataset_version}},
            {"term": {"status": "active"}},
        ]
        catalog_filters = [*common_filters]
        catalog_must_not: list[dict[str, Any]] = []
        if level:
            catalog_filters.append({"term": {"level": level}})
        degree_mode, degree_values = infer_degree_constraint(query)
        if degree_mode == "include" and isinstance(degree_values, str):
            catalog_filters.append({"term": {"degree_level": degree_values}})
        elif degree_mode == "include" and degree_values:
            catalog_filters.append({"terms": {"degree_level": degree_values}})
        elif degree_mode == "exclude" and degree_values:
            catalog_must_not.append({"terms": {"degree_level": degree_values}})
        catalog_should: list[dict[str, Any]] = []
        entry_id_match = re.search(r"\bent_[a-z0-9_]+\b", query.lower())
        if entry_id_match:
            catalog_should.append({"term": {"entry_id": {"value": entry_id_match.group(0), "boost": 50}}})
        if course_code:
            catalog_should.append({"term": {"course_code": {"value": course_code, "boost": 30}}})
        if catalog_query:
            catalog_should.extend([
                {"match_phrase": {"program_name": {"query": catalog_query, "boost": 12}}},
                {"multi_match": {"query": catalog_query, "fields": ["program_name^6", "canonical_program_name^6", "aliases^5", "department^3", "school^2", "search_text"], "operator": "and"}},
            ])
        catalog_body = {
            "size": max_results,
            "track_total_hits": False,
            "query": {"bool": {
                "filter": catalog_filters,
                "must_not": catalog_must_not,
                "should": catalog_should,
                "minimum_should_match": 1 if catalog_should else 0,
            }},
            "min_score": 1.0,
        }

        fact_scope_filters = [*common_filters]
        if fact_types:
            fact_scope_filters.append({"terms": {"fact_type": fact_types}})
        if level == "undergraduate":
            fact_scope_filters.append({"bool": {"should": [
                {"wildcard": {"fact_id": {"value": "*undergraduate*"}}},
                {"wildcard": {"source_url": {"value": "*mitadmissions.org*"}}},
                {"wildcard": {"source_url": {"value": "*undergraduate-students*"}}},
            ], "minimum_should_match": 1}})
        fact_filters = [*fact_scope_filters]
        fact_should: list[dict[str, Any]] = []
        if program_slug:
            fact_filters.append({"bool": {"should": [
                {"wildcard": {"source_url": {"value": f"*{program_slug}*"}}},
                {"wildcard": {"fact_id": {"value": f"*{program_slug.replace('-', '_')}*"}}},
            ], "minimum_should_match": 1}})
        fact_should.append({"multi_match": {"query": query, "fields": ["raw_value^2", "fact_key^4"], "operator": "or"}})
        fact_body = {
            "size": max_results,
            "track_total_hits": False,
            "query": {"bool": {"filter": fact_filters, "should": fact_should}},
        }

        source_filters = [*common_filters, {"term": {"import_status": "success"}}]
        if requested_entry_id:
            source_filters.append({"term": {"entry_ids": requested_entry_id}})
        elif requested_program_id:
            source_filters.append({"term": {"program_id": requested_program_id}})
        source_should: list[dict[str, Any]] = [
            {"multi_match": {"query": catalog_query or query, "fields": ["topics^4", "url_type^3"], "operator": "or"}},
        ]
        if program_slug:
            source_should.extend([
                {"wildcard": {"source_url": {"value": f"*{program_slug}*", "boost": 20}}},
                {"wildcard": {"canonical_url": {"value": f"*{program_slug}*", "boost": 20}}},
            ])
        source_body = {
            "size": max_results,
            "track_total_hits": False,
            "query": {"bool": {
                "filter": source_filters,
                "should": source_should,
                "minimum_should_match": 0 if requested_entry_id or requested_program_id else 1,
            }},
        }

        context_filters = [*common_filters, {"term": {"is_current": True}}]
        program_context_requested = bool(
            requested_entry_id
            or requested_program_id
            or query_plan.course_codes
            or program_slug
            or (query_plan.stage == "discovery" and catalog_query)
        )
        if program_context_requested and level:
            context_filters.append({"term": {"attributes.level": level}})
        if degree_mode == "include" and isinstance(degree_values, str):
            context_filters.append({"term": {"attributes.degree_level": degree_values}})
        elif degree_mode == "include" and degree_values:
            context_filters.append({"terms": {"attributes.degree_level": degree_values}})
        context_should: list[dict[str, Any]] = []
        if requested_entry_id:
            context_should.extend([
                {"term": {"entry_id": {"value": requested_entry_id, "boost": 50}}},
                {"term": {"entity_id": {"value": requested_entry_id, "boost": 50}}},
            ])
        elif requested_program_id:
            context_should.append({"term": {"attributes.program_id": {"value": requested_program_id, "boost": 50}}})
        elif query_plan.course_codes:
            context_should.append({"terms": {"attributes.course_code": list(query_plan.course_codes), "boost": 30}})
            if catalog_query:
                context_should.append({"multi_match": {"query": catalog_query, "fields": ["display_label^8", "title^6", "attributes.department^2", "attributes.school"], "operator": "or"}})
        elif program_slug or (query_plan.stage == "discovery" and catalog_query):
            context_should.append({"multi_match": {"query": catalog_query or query, "fields": ["display_label^8", "title^6", "attributes.department^2", "attributes.school"], "operator": "or"}})
        if not program_context_requested:
            context_filters.append({"term": {"entity_type": "university"}})
        context_body = {
            "size": min(query_plan.max_primary_entities, max_results),
            "track_total_hits": False,
            "query": {"bool": {
                "filter": context_filters,
                "must_not": [{"terms": {"attributes.degree_level": degree_values}}] if degree_mode == "exclude" and degree_values else [],
                "should": context_should,
                "minimum_should_match": 1 if context_should else 0,
            }},
        }

        response = self.client.msearch(body=[
            {"index": "l1_catalog_entries_current"}, catalog_body,
            {"index": "l1_quick_facts_current"}, fact_body,
            {"index": "l1_sources_current"}, source_body,
            {"index": "l1_entity_contexts_current"}, context_body,
        ])
        responses = response.get("responses", [])
        if len(responses) != 4 or any("error" in item for item in responses):
            raise RuntimeError(f"OpenSearch msearch failed: {responses}")
        catalog = self._matches(responses[0], "exact_course_code" if course_code else "catalog_bm25")
        if course_code and catalog:
            exact = [row for row in catalog if str(row.get("course_code", "")).lower() == course_code.lower()]
            catalog = exact[:1]
        facts = self._matches(responses[1], "fact_lookup") if fact_types else []
        sources = self._matches(responses[2], "source_scope")
        contexts = self._matches(responses[3], "entity_context")

        program_contexts = [row for row in contexts if row.get("entity_type") == "program"]
        scoped_source_ids = sorted({
            str(source_id)
            for row in program_contexts
            for source_id in row.get("source_ids") or []
            if source_id
        })
        if scoped_source_ids and query_plan.stage in {"fact", "detail"}:
            scoped_requests: list[dict[str, Any]] = []
            response_kinds: list[str] = []
            exact_source_filter = {"terms": {"source_id": scoped_source_ids}}
            if fact_types:
                scoped_fact_bool = dict(fact_body["query"]["bool"])
                scoped_fact_bool["filter"] = [*fact_scope_filters, exact_source_filter]
                scoped_requests.extend([
                    {"index": "l1_quick_facts_current"},
                    {**fact_body, "query": {"bool": scoped_fact_bool}},
                ])
                response_kinds.append("facts")

            scoped_source_bool = dict(source_body["query"]["bool"])
            scoped_source_bool["filter"] = [*source_filters, exact_source_filter]
            scoped_source_bool["minimum_should_match"] = 0
            scoped_requests.extend([
                {"index": "l1_sources_current"},
                {**source_body, "query": {"bool": scoped_source_bool}},
            ])
            response_kinds.append("sources")

            scoped_response = self.client.msearch(body=scoped_requests)
            scoped_responses = scoped_response.get("responses", [])
            if len(scoped_responses) != len(response_kinds) or any("error" in item for item in scoped_responses):
                raise RuntimeError(f"OpenSearch scoped msearch failed: {scoped_responses}")
            for kind, item in zip(response_kinds, scoped_responses, strict=True):
                if kind == "facts":
                    facts = self._matches(item, "exact_entity_fact_lookup")
                else:
                    sources = self._matches(item, "exact_entity_source_scope")
        return L1SearchResult(
            university_id=university_id,
            dataset_version=dataset_version,
            catalog=catalog,
            facts=facts,
            sources=sources,
            contexts=contexts,
            elapsed_ms=round((time.perf_counter() - started) * 1000, 3),
        )

    def search_across_universities(
        self,
        *,
        query: str,
        discipline_ids: list[str],
        filters: dict[str, Any],
        max_results: int = 20,
    ) -> CrossUniversitySearchResult:
        started = time.perf_counter()
        if not discipline_ids and not filters.get("degree_levels") and not filters.get("levels"):
            university_filters: list[dict[str, Any]] = [
                {"term": {"is_current": True}},
                {"term": {"status": "active"}},
            ]
            for request_key, index_field in {
                "country_codes": "country_code",
                "regions": "region",
                "school_tiers": "school_tier",
            }.items():
                values = [str(value) for value in filters.get(request_key) or [] if value not in (None, "")]
                if values:
                    university_filters.append({"terms": {index_field: values}})
            response = self.client.search(index="l1_universities_current", body={
                "size": max_results,
                "track_total_hits": False,
                "query": {"bool": {"filter": university_filters}},
            })
            matches = []
            for hit in response.get("hits", {}).get("hits", []):
                row = dict(hit.get("_source") or {})
                matches.append({
                    "entity_type": "university",
                    "university_id": row.get("university_id"),
                    "university_name": row.get("university_name"),
                    "country_code": row.get("country_code"),
                    "region": row.get("region"),
                    "school_tier": row.get("school_tier"),
                    "dataset_version": row.get("dataset_version"),
                    "matched_programs": [],
                    "matched_disciplines": [],
                    "source_urls": [],
                    "match_reason": "range_filter",
                    "match_score": hit.get("_score"),
                })
            matches.sort(key=lambda item: str(item.get("university_name") or item.get("university_id")))
            return CrossUniversitySearchResult(matches=matches, elapsed_ms=round((time.perf_counter() - started) * 1000, 3))

        query_filters: list[dict[str, Any]] = [
            {"term": {"is_current": True}},
            {"term": {"status": "active"}},
        ]
        if discipline_ids:
            query_filters.append({"terms": {"discipline_ids": discipline_ids}})
        filter_fields = {
            "country_codes": "country_code",
            "regions": "region",
            "degree_levels": "degree_level",
            "levels": "level",
            "school_tiers": "school_tier",
        }
        for request_key, index_field in filter_fields.items():
            values = [str(value) for value in filters.get(request_key) or [] if value not in (None, "")]
            if values:
                query_filters.append({"terms": {index_field: values}})

        should: list[dict[str, Any]] = []
        if discipline_ids:
            should.append({"terms": {"discipline_ids": discipline_ids, "boost": 12}})
        else:
            normalized_query = normalized_catalog_query(query)
            if normalized_query:
                should.append({
                    "multi_match": {
                        "query": normalized_query,
                        "fields": ["program_name^6", "discipline_labels^5", "department^3", "school^2", "search_text"],
                        "operator": "or",
                    }
                })
        bool_query: dict[str, Any] = {"filter": query_filters}
        if should:
            bool_query.update({"should": should, "minimum_should_match": 1})
        body = {
            "size": min(1000, max(100, max_results * 20)),
            "track_total_hits": False,
            "query": {"bool": bool_query},
        }
        response = self.client.search(index="l1_catalog_entries_current", body=body)
        grouped: dict[str, dict[str, Any]] = {}
        for hit in response.get("hits", {}).get("hits", []):
            row = dict(hit.get("_source") or {})
            university_id = str(row.get("university_id") or "")
            if not university_id:
                continue
            score = float(hit.get("_score") or 0)
            group = grouped.setdefault(university_id, {
                "entity_type": "university_program_group",
                "university_id": university_id,
                "university_name": row.get("university_name") or university_id,
                "country_code": row.get("country_code"),
                "region": row.get("region"),
                "school_tier": row.get("school_tier"),
                "matched_programs": [],
                "matched_disciplines": [],
                "source_urls": [],
                "match_reason": "discipline_taxonomy" if discipline_ids else "range_filter",
                "match_score": score,
            })
            group["match_score"] = max(group["match_score"], score)
            program = {
                key: row.get(key)
                for key in (
                    "entry_id", "program_name", "course_code", "level", "degree_level",
                    "discipline_ids", "discipline_labels", "source_id", "source_url", "dataset_version",
                )
            }
            program["_score"] = score
            if program not in group["matched_programs"] and len(group["matched_programs"]) < 10:
                group["matched_programs"].append(program)
            group["matched_disciplines"] = sorted(set(group["matched_disciplines"]) | set(row.get("discipline_ids") or []))
            if row.get("source_url"):
                group["source_urls"] = sorted(set(group["source_urls"]) | {row["source_url"]})

        matches = sorted(grouped.values(), key=lambda item: (-item["match_score"], str(item["university_name"])))[:max_results]
        return CrossUniversitySearchResult(matches=matches, elapsed_ms=round((time.perf_counter() - started) * 1000, 3))

    @staticmethod
    def _matches(response: dict[str, Any], reason: str) -> list[dict[str, Any]]:
        rows: list[dict[str, Any]] = []
        for hit in response.get("hits", {}).get("hits", []):
            source = dict(hit.get("_source") or {})
            source["match_reason"] = reason
            source["_score"] = hit.get("_score")
            rows.append(source)
        return rows
