from __future__ import annotations

import unittest

from fast_router.opensearch_retrieval import CurrentVersionMap, L1SearchResult, OpenSearchRetrievalClient
from fast_router.query_planning import plan_query
from fast_router.retrieval import RetrievalEngine, compose_context


def university_context() -> dict:
    return {
        "context_id": "ctx_mit_university_mit",
        "entity_type": "university",
        "entity_id": "mit",
        "university_id": "mit",
        "entry_id": None,
        "title": "Massachusetts Institute of Technology",
        "display_label": "Massachusetts Institute of Technology",
        "attributes": {"country_code": "US", "region": "Massachusetts"},
        "highlights": [{"kind": "catalog_count", "label": "Undergraduate SB programs", "value": 55}],
        "sample_children": [{"entity_type": "school", "entity_id": "school_engineering", "title": "School of Engineering"}],
        "related_entities": [],
        "available_topics": [{"topic": "tuition", "availability": "l1", "source_ids": ["src_tuition"], "source_count": 1}],
        "source_ids": ["src_catalog"],
        "dataset_version": "mit_v2",
        "status": "active",
    }


def program_context(code: str, title: str, entry_id: str) -> dict:
    return {
        "context_id": f"ctx_{entry_id}",
        "entity_type": "program",
        "entity_id": entry_id,
        "university_id": "mit",
        "entry_id": entry_id,
        "title": title,
        "display_label": f"{code} {title}",
        "attributes": {
            "course_code": code,
            "degree_level": "SB",
            "level": "undergraduate",
            "department": "Economics",
            "school": "School of Humanities, Arts, and Social Sciences",
        },
        "highlights": [],
        "sample_children": [],
        "related_entities": [],
        "available_topics": [{"topic": "curriculum", "availability": "weknora", "source_ids": [f"src_{code}"], "source_count": 1}],
        "source_ids": [f"src_{code}"],
        "dataset_version": "mit_v2",
        "status": "active",
    }


class FakeL1:
    def __init__(self) -> None:
        self.search_calls: list[dict] = []

    def resolve_university(self, query: str, requested_id: str | None):
        return ("mit", "mit_v2")

    def search(self, **kwargs):
        self.search_calls.append(kwargs)
        query = kwargs["query"]
        contexts = [university_context()]
        catalog: list[dict] = []
        facts: list[dict] = []
        sources: list[dict] = []
        if "Economics" in query or "14-" in query or "6-14" in query:
            economics = program_context("14-1", "Economics", "ent_economics")
            mathematical = program_context("14-2", "Mathematical Economics", "ent_math_econ")
            interdisciplinary = program_context("6-14", "Computer Science, Economics, and Data Science", "ent_6_14")
            economics["related_entities"] = [
                {**mathematical, "relation_type": "same_department_and_degree", "relation_reason": "Same university, department, study level, and degree level as 14-1 Economics."},
                {**interdisciplinary, "relation_type": "interdisciplinary_related", "relation_reason": "Same university and study level as 14-1 Economics; shares economics and is marked cross-school."},
            ]
            contexts = [economics, mathematical, interdisciplinary]
            catalog = [{"entry_id": "ent_economics", "program_name": "Economics", "course_code": "14-1", "source_id": "src_14-1"}]
        if "学费" in query:
            facts = [{
                "fact_id": "fact_tuition",
                "fact_type": "tuition",
                "raw_value": "$64,310",
                "source_id": "src_tuition",
                "review_status": "approved",
                "conflict_status": "none",
            }]
        if "材料" in query:
            contexts = [program_context("6", "Electrical Engineering and Computer Science (PhD)", "ent_eecs_phd")]
            facts = [{
                "fact_id": "fact_eecs_english",
                "fact_type": "english_requirement",
                "raw_value": "TOEFL 100",
                "source_id": "src_eecs",
                "review_status": "review_required",
                "conflict_status": "none",
            }]
            sources = [{
                "source_id": "src_eecs",
                "entry_ids": ["ent_eecs_phd"],
                "source_url": "https://eecs.mit.edu/admissions",
                "weknora_knowledge_id": "wk_eecs",
                "import_status": "success",
            }]
        return L1SearchResult(
            university_id="mit",
            dataset_version="mit_v2",
            catalog=catalog,
            facts=facts,
            sources=sources,
            contexts=contexts,
            elapsed_ms=4.0,
        )


class SpyWeknora:
    def __init__(self) -> None:
        self.calls: list[tuple] = []

    def search(self, university_id, query, sources, top_k):
        self.calls.append((university_id, query, sources, top_k))
        return [{"source_id": sources[0]["source_id"], "text": "Required application materials."}]


class RecordingMsearchClient:
    def __init__(self) -> None:
        self.body = None

    def msearch(self, *, body):
        self.body = body
        return {"responses": [{"hits": {"hits": []}} for _ in range(4)]}


class ProgramContextOnlyL1(FakeL1):
    def search(self, **kwargs):
        return L1SearchResult(
            university_id="mit",
            dataset_version="mit_v2",
            catalog=[],
            facts=[],
            sources=[],
            contexts=[program_context("14-1", "Economics", "ent_economics")],
            elapsed_ms=1.0,
        )


class ProgramScopedMsearchClient:
    def __init__(self) -> None:
        self.bodies: list[list[dict]] = []

    @staticmethod
    def _hits(*rows: dict) -> dict:
        return {"hits": {"hits": [{"_score": 1.0, "_source": row} for row in rows]}}

    def msearch(self, *, body):
        self.bodies.append(body)
        economics_source = "src_mit_oge_mit_edu_programs_economics"
        dedp_source = "src_mit_oge_mit_edu_programs_data_economics_and_development_policy"
        if len(self.bodies) == 1:
            return {"responses": [
                self._hits(),
                self._hits(
                    {"fact_id": "fact_economics_deadline", "fact_type": "deadline", "source_id": economics_source},
                    {"fact_id": "fact_dedp_deadline", "fact_type": "deadline", "source_id": dedp_source},
                ),
                self._hits(
                    {"source_id": economics_source, "entry_ids": ["ent_economics_phd"], "import_status": "success"},
                    {"source_id": dedp_source, "entry_ids": ["ent_dedp"], "import_status": "success"},
                ),
                self._hits({
                    "entity_type": "program",
                    "entity_id": "ent_economics_phd",
                    "entry_id": "ent_economics_phd",
                    "display_label": "Economics PhD",
                    "source_ids": [economics_source],
                }),
            ]}
        return {"responses": [
            self._hits({"fact_id": "fact_economics_deadline", "fact_type": "deadline", "source_id": economics_source}),
            self._hits({"source_id": economics_source, "entry_ids": ["ent_economics_phd"], "import_status": "success"}),
        ]}


class DiscoveryContextRetrievalTests(unittest.TestCase):
    def setUp(self) -> None:
        self.l1 = FakeL1()
        self.weknora = SpyWeknora()
        self.engine = RetrievalEngine(self.l1, self.weknora)

    def retrieve(self, query: str, context: dict | None = None) -> dict:
        return self.engine.retrieve(
            query=query,
            university_id="mit",
            context=context or {},
            filters={},
            direction="auto",
            max_results=5,
        )

    def test_query_plan_keeps_overview_language_in_discovery(self) -> None:
        self.assertEqual(plan_query("MIT").stage, "discovery")
        overview = plan_query("MIT 有 Economics 本科专业吗？这个专业怎么样？")
        self.assertEqual(overview.stage, "discovery")
        self.assertEqual(overview.max_primary_entities, 1)
        self.assertEqual(plan_query("MIT Economics、Mathematical Economics 和 6-14 有什么关系？").max_primary_entities, 3)
        self.assertEqual(plan_query("MIT 本科 2026-2027 学费是多少？").stage, "fact")
        detail = plan_query("MIT EECS PhD 申请需要提交哪些材料？")
        self.assertEqual(detail.stage, "detail")
        self.assertIn("application_materials", detail.requested_aspects)

    def test_specific_detail_intent_takes_precedence_over_fact_terms(self) -> None:
        materials = plan_query(
            "MIT EECS PhD application requirements required materials transcripts letters CV GRE TOEFL IELTS"
        )
        self.assertEqual(materials.stage, "detail")
        self.assertIn("application_materials", materials.requested_aspects)

        english_minimum = plan_query("MIT EECS PhD TOEFL minimum requirement")
        self.assertEqual(english_minimum.stage, "fact")
        self.assertEqual(english_minimum.requested_aspects, ("english_requirement",))

        complete_requirements = plan_query("MIT EECS PhD complete application requirements")
        self.assertEqual(complete_requirements.stage, "detail")
        self.assertIn("application_requirements", complete_requirements.requested_aspects)

    def test_materials_science_name_is_not_application_materials_intent(self) -> None:
        discovery = plan_query("MIT Materials Science graduate programs")
        self.assertEqual(discovery.stage, "discovery")

        detail = plan_query("MIT application materials for Materials Science")
        self.assertEqual(detail.stage, "detail")
        self.assertIn("application_materials", detail.requested_aspects)

    def test_program_context_prioritizes_entity_specific_exploration_topics(self) -> None:
        row = program_context("14-1", "Economics", "ent_economics")
        row["available_topics"] = [
            {"topic": "cost_of_attendance", "availability": "l1"},
            {"topic": "deadline", "availability": "l1"},
            {"topic": "curriculum", "availability": "weknora"},
            {"topic": "application_requirements", "availability": "weknora"},
            {"topic": "tuition", "availability": "l1"},
        ]

        payload = compose_context([row], "mit_v2", 1)

        self.assertEqual(
            [item["topic"] for item in payload["available_topics"]],
            ["curriculum", "application_requirements", "tuition", "deadline"],
        )

    def test_university_fact_context_does_not_apply_program_level_filter(self) -> None:
        fake = RecordingMsearchClient()
        client = OpenSearchRetrievalClient(
            "http://unused",
            CurrentVersionMap(initial={"mit": "mit_v2"}),
            client=fake,
        )

        client.search(
            query="MIT 本科 2026-2027 学费是多少？",
            university_id="mit",
            dataset_version="mit_v2",
        )

        context_filters = fake.body[7]["query"]["bool"]["filter"]
        self.assertIn({"term": {"entity_type": "university"}}, context_filters)
        self.assertNotIn({"term": {"attributes.level": "undergraduate"}}, context_filters)

    def test_degree_intent_adds_hard_catalog_filters(self) -> None:
        cases = (
            ("MIT EECS PhD", {"term": {"degree_level": "PhD"}}, None),
            ("MIT Computer Science master", {"terms": {"degree_level": ["SM", "MEng", "MArch", "MCP", "MASc", "MBA", "MBAn", "MFin", "MSMS"]}}, None),
            ("MIT Economics undergraduate major", None, {"terms": {"degree_level": ["Minor", "Certificate"]}}),
            ("MIT Economics minor", {"term": {"degree_level": "Minor"}}, None),
        )
        for query, expected_filter, expected_must_not in cases:
            with self.subTest(query=query):
                fake = RecordingMsearchClient()
                client = OpenSearchRetrievalClient(
                    "http://unused",
                    CurrentVersionMap(initial={"mit": "mit_v2"}),
                    client=fake,
                )

                client.search(query=query, university_id="mit", dataset_version="mit_v2")

                catalog_bool = fake.body[1]["query"]["bool"]
                if expected_filter:
                    self.assertIn(expected_filter, catalog_bool["filter"])
                if expected_must_not:
                    self.assertIn(expected_must_not, catalog_bool["must_not"])

    def test_explicit_entry_context_scopes_source_query_before_top_k(self) -> None:
        fake = RecordingMsearchClient()
        client = OpenSearchRetrievalClient(
            "http://unused",
            CurrentVersionMap(initial={"mit": "mit_v2"}),
            client=fake,
        )

        client.search(
            query="那课程设置呢？",
            university_id="mit",
            dataset_version="mit_v2",
            context={"entry_id": "ent_economics", "level": "undergraduate"},
        )

        source_filters = fake.body[5]["query"]["bool"]["filter"]
        self.assertIn({"term": {"entry_ids": "ent_economics"}}, source_filters)
        self.assertEqual(fake.body[5]["query"]["bool"]["minimum_should_match"], 0)

    def test_program_context_rescopes_facts_and_sources_by_exact_source_id(self) -> None:
        fake = ProgramScopedMsearchClient()
        client = OpenSearchRetrievalClient(
            "http://unused",
            CurrentVersionMap(initial={"mit": "mit_v2"}),
            client=fake,
        )

        result = client.search(
            query="MIT Economics graduate application deadline 是什么时候？",
            university_id="mit",
            dataset_version="mit_v2",
        )

        self.assertEqual([row["fact_id"] for row in result.facts], ["fact_economics_deadline"])
        self.assertEqual([row["source_id"] for row in result.sources], ["src_mit_oge_mit_edu_programs_economics"])
        self.assertEqual(len(fake.bodies), 2)
        scoped_fact_filters = fake.bodies[1][1]["query"]["bool"]["filter"]
        scoped_source_filters = fake.bodies[1][3]["query"]["bool"]["filter"]
        expected_scope = {"terms": {"source_id": ["src_mit_oge_mit_edu_programs_economics"]}}
        self.assertIn(expected_scope, scoped_fact_filters)
        self.assertIn(expected_scope, scoped_source_filters)
        self.assertFalse(any("wildcard" in clause for clause in scoped_fact_filters))

    def test_university_discovery_returns_md_context_without_weknora(self) -> None:
        result = self.retrieve("MIT")

        self.assertEqual(result["mode"], "l1")
        self.assertEqual(result["scope"]["stage"], "discovery")
        self.assertEqual(result["context"]["primary_entities"][0]["entity_type"], "university")
        self.assertTrue(result["context"]["sample_children"])
        self.assertEqual(self.weknora.calls, [])
        self.assertEqual(result["timings"]["weknora_ms"], 0)

    def test_program_overview_returns_readable_related_entities_without_weknora(self) -> None:
        result = self.retrieve("MIT 有 Economics 本科专业吗？这个专业怎么样？")

        self.assertEqual(result["context"]["primary_entities"][0]["display_label"], "14-1 Economics")
        self.assertEqual(len(result["context"]["primary_entities"]), 1)
        labels = [row["display_label"] for row in result["context"]["related_entities"]]
        self.assertIn("14-2 Mathematical Economics", labels)
        self.assertTrue(all("relation_reason" in row for row in result["context"]["related_entities"]))
        self.assertEqual(self.weknora.calls, [])

    def test_program_context_without_catalog_match_is_not_returned_as_formal_match(self) -> None:
        engine = RetrievalEngine(ProgramContextOnlyL1(), self.weknora)

        result = engine.retrieve(
            query="MIT Economics undergraduate major",
            university_id="mit",
            context={},
            filters={},
            direction="auto",
            max_results=5,
        )

        self.assertEqual(result["matches"], [])
        self.assertEqual(result["mode"], "not_found")
        self.assertIn("catalog_match_missing", result["warnings"])

    def test_multi_program_discovery_returns_at_most_three_primary_entities(self) -> None:
        result = self.retrieve("MIT Economics、Mathematical Economics 和 6-14 有什么关系？")

        self.assertEqual(len(result["context"]["primary_entities"]), 3)
        self.assertEqual(
            {row["display_label"] for row in result["context"]["primary_entities"]},
            {"14-1 Economics", "14-2 Mathematical Economics", "6-14 Computer Science, Economics, and Data Science"},
        )
        primary_ids = {row["entity_id"] for row in result["context"]["primary_entities"]}
        related_ids = {row["entity_id"] for row in result["context"]["related_entities"]}
        self.assertTrue(primary_ids.isdisjoint(related_ids))
        self.assertEqual(self.weknora.calls, [])

    def test_fact_hit_returns_fact_and_context_without_weknora(self) -> None:
        result = self.retrieve("MIT 本科 2026-2027 学费是多少？")

        self.assertEqual(result["matches"][0]["raw_value"], "$64,310")
        self.assertEqual(result["scope"]["stage"], "fact")
        self.assertEqual(result["context"]["primary_entities"][0]["entity_type"], "university")
        self.assertEqual(self.weknora.calls, [])

    def test_explicit_detail_uses_weknora_only_with_resolved_source_scope(self) -> None:
        result = self.retrieve(
            "MIT EECS PhD 申请需要提交哪些材料？TOEFL、IELTS 和 GRE 也一起查",
            context={"entry_id": "ent_eecs_phd", "level": "graduate"},
        )

        self.assertEqual(result["mode"], "l1_l2")
        self.assertEqual(result["scope"]["stage"], "detail")
        self.assertEqual(result["matches"], [])
        self.assertEqual(result["evidence"][0]["source_id"], "src_eecs")
        self.assertEqual(len(self.weknora.calls), 1)

    def test_ambiguous_detail_returns_clarification_without_weknora(self) -> None:
        result = self.retrieve("MIT 申请需要提交哪些材料？")

        self.assertEqual(result["mode"], "clarification")
        self.assertIn("program_id_or_entry_id", result["missing_slots"])
        self.assertEqual(self.weknora.calls, [])


if __name__ == "__main__":
    unittest.main()
