from __future__ import annotations

import unittest

from fast_router.opensearch_retrieval import CurrentVersionMap, OpenSearchRetrievalClient
from fast_router.retrieval import RetrievalEngine, infer_search_direction


class FakeSearchClient:
    def __init__(self) -> None:
        self.last_body = None

    def search(self, *, index: str, body: dict) -> dict:
        self.last_body = body
        self.last_index = index
        if index == "l1_universities_current":
            return {
                "hits": {"hits": [{"_score": 1, "_source": {
                    "university_id": "mit",
                    "university_name": "Massachusetts Institute of Technology",
                    "country_code": "US",
                    "region": "Massachusetts",
                    "school_tier": "core",
                    "dataset_version": "mit_v2",
                    "status": "active",
                    "is_current": True,
                }}]}
            }
        return {
            "hits": {
                "hits": [
                    {
                        "_score": 8.5,
                        "_source": {
                            "university_id": "mit",
                            "university_name": "Massachusetts Institute of Technology",
                            "country_code": "US",
                            "region": "Massachusetts",
                            "school_tier": "core",
                            "entry_id": "ent_mit_health",
                            "program_name": "Health Sciences and Technology (Harvard-MIT)",
                            "degree_level": "PhD",
                            "level": "graduate",
                            "discipline_ids": ["health_sciences"],
                            "discipline_labels": ["Health Sciences"],
                            "source_id": "src_mit_health",
                            "source_url": "https://example.edu/health",
                            "dataset_version": "mit_v2",
                            "status": "active",
                            "is_current": True,
                        },
                    },
                    {
                        "_score": 7.5,
                        "_source": {
                            "university_id": "mit",
                            "university_name": "Massachusetts Institute of Technology",
                            "country_code": "US",
                            "region": "Massachusetts",
                            "school_tier": "core",
                            "entry_id": "ent_mit_biomed",
                            "program_name": "Biomedical Engineering",
                            "degree_level": "Minor",
                            "level": "undergraduate",
                            "discipline_ids": ["biomedical_engineering"],
                            "discipline_labels": ["Biomedical Engineering"],
                            "source_id": "src_mit_biomed",
                            "source_url": "https://example.edu/biomed",
                            "dataset_version": "mit_v2",
                            "status": "active",
                            "is_current": True,
                        },
                    },
                ]
            }
        }


class FakeCrossUniversityL1:
    def resolve_university(self, query, requested_id):
        if "mit" in query.lower() or requested_id == "mit":
            return "mit", "mit_v2"
        return None, None

    def search(self, **kwargs):
        self.search_kwargs = kwargs
        return type("Result", (), {
            "catalog": [{"entry_id": "ent_mit_economics", "program_name": "Economics"}],
            "facts": [],
            "sources": [],
            "contexts": [],
            "elapsed_ms": 3.0,
        })()

    def search_across_universities(self, **kwargs):
        self.kwargs = kwargs
        return type("Result", (), {"matches": [{"university_id": "mit", "matched_programs": []}], "elapsed_ms": 4.2})()


class CrossUniversityRetrievalTests(unittest.TestCase):
    def test_auto_direction_detects_discipline_to_university_query(self) -> None:
        self.assertEqual(infer_search_direction("医学专业的院校有哪些？", None, {}, "auto"), "upward")
        self.assertEqual(infer_search_direction("MIT 有哪些医学相关项目？", "mit", {}, "auto"), "downward")
        self.assertEqual(infer_search_direction("有哪些院校？", None, {"country_codes": ["US"]}, "auto"), "range")
        self.assertEqual(infer_search_direction("Duke University Computer Science", None, {}, "auto"), "downward")

    def test_version_map_resolves_ingested_university_aliases_without_opensearch(self) -> None:
        versions = CurrentVersionMap(
            initial={"asu": "asu_v1"},
            initial_aliases={"asu": ["Arizona State University", "ASU"]},
        )
        client = OpenSearchRetrievalClient("http://unused", versions, client=FakeSearchClient())

        self.assertEqual(
            client.resolve_university("Arizona State University Computer Science", None),
            ("asu", "asu_v1"),
        )

    def test_opensearch_groups_medical_programs_by_ingested_university(self) -> None:
        fake = FakeSearchClient()
        client = OpenSearchRetrievalClient("http://unused", CurrentVersionMap(initial={"mit": "mit_v2"}), client=fake)

        result = client.search_across_universities(
            query="医学专业的院校有哪些？",
            discipline_ids=["medicine", "health_sciences", "biomedical_engineering"],
            filters={"country_codes": ["US"], "school_tiers": ["core"]},
            max_results=10,
        )

        self.assertEqual(len(result.matches), 1)
        self.assertEqual(result.matches[0]["university_id"], "mit")
        self.assertEqual(len(result.matches[0]["matched_programs"]), 2)
        query_filters = fake.last_body["query"]["bool"]["filter"]
        self.assertIn({"term": {"is_current": True}}, query_filters)
        self.assertIn({"terms": {"discipline_ids": ["medicine", "health_sciences", "biomedical_engineering"]}}, query_filters)
        self.assertIn({"terms": {"country_code": ["US"]}}, query_filters)

    def test_range_without_discipline_uses_university_index(self) -> None:
        fake = FakeSearchClient()
        client = OpenSearchRetrievalClient("http://unused", CurrentVersionMap(initial={"mit": "mit_v2"}), client=fake)

        result = client.search_across_universities(
            query="美国核心院校有哪些？",
            discipline_ids=[],
            filters={"country_codes": ["US"], "school_tiers": ["core"]},
            max_results=20,
        )

        self.assertEqual(fake.last_index, "l1_universities_current")
        self.assertEqual(result.matches[0]["university_id"], "mit")
        self.assertEqual(result.matches[0]["matched_programs"], [])

    def test_retrieval_engine_returns_upward_without_weknora(self) -> None:
        l1 = FakeCrossUniversityL1()
        engine = RetrievalEngine(l1, weknora=object())

        result = engine.retrieve(
            query="医学专业的院校有哪些？",
            university_id=None,
            context={},
            filters={},
            direction="auto",
            max_results=20,
        )

        self.assertEqual(result["mode"], "upward")
        self.assertEqual(result["matches"][0]["university_id"], "mit")
        self.assertEqual(result["timings"]["weknora_ms"], 0)

    def test_known_university_is_resolved_before_discipline_direction(self) -> None:
        l1 = FakeCrossUniversityL1()
        engine = RetrievalEngine(l1)

        result = engine.retrieve(
            query="MIT Economics graduate programs",
            university_id=None,
            context={},
            filters={},
            direction="auto",
            max_results=5,
        )

        self.assertEqual(result["scope"]["university_id"], "mit")
        self.assertEqual(result["scope"]["direction"], "downward")
        self.assertFalse(hasattr(l1, "kwargs"))

    def test_invalid_explicit_university_id_never_broadens_to_range(self) -> None:
        l1 = FakeCrossUniversityL1()
        engine = RetrievalEngine(l1)

        result = engine.retrieve(
            query="Computer Science programs",
            university_id="unknown_u",
            context={},
            filters={"country_codes": ["US"]},
            direction="auto",
            max_results=5,
        )

        self.assertEqual(result["mode"], "not_found")
        self.assertIn("unknown_university", result["warnings"])
        self.assertFalse(hasattr(l1, "kwargs"))


if __name__ == "__main__":
    unittest.main()
