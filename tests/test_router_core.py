from __future__ import annotations

import os
import unittest
from pathlib import Path

from fast_router.knowledge import KnowledgeStore, answer_from_facts, evidence_from_scope, infer_route


ROOT = Path(__file__).resolve().parents[1]


class RouterCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        os.environ["KNOWLEDGE_DATA_ROOT"] = str(ROOT / "data/normalized")
        cls.store = KnowledgeStore.from_env()

    def test_catalog_search_finds_ai_undergrad(self) -> None:
        results = self.store.search_catalog("mit", "MIT 有哪些 AI 相关本科专业？", level="undergraduate")
        names = [row["program_name"] for row in results]
        self.assertEqual(names, ["Artificial Intelligence and Decision Making"])

    def test_catalog_search_keeps_broad_minor_query_within_matching_degree_type(self) -> None:
        results = self.store.search_catalog("mit", "MIT 有哪些 minor？", level="undergraduate")

        self.assertTrue(results)
        self.assertTrue(all(row["degree_level"] == "Minor" for row in results))

    def test_fact_lookup_finds_eecs_toefl(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT EECS PhD TOEFL 要求是多少？")
        text = answer_from_facts(facts)
        self.assertIn("TOEFL 100", text)
        self.assertIn("electrical-engineering-and-computer-science", text)

    def test_fact_lookup_finds_undergrad_ea_deadline(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT 本科 EA 截止日是什么时候？")
        text = answer_from_facts(facts)
        self.assertIn("November 1", text)

    def test_route_does_not_treat_analytics_as_cs_master(self) -> None:
        route = infer_route("MIT Sloan Master of Business Analytics 研究生 program 有哪些信息？")

        self.assertEqual(route, "catalog")

    def test_route_prioritizes_catalog_and_fact_terms_over_policy_word_in_program_name(self) -> None:
        self.assertEqual(infer_route("MIT Data, Economics, and Design of Policy 研究生 program 有哪些信息？"), "catalog")
        self.assertEqual(infer_route("MIT technology and policy program application fee 是多少？"), "fact")

    def test_yes_no_high_risk_program_questions_use_deep_route(self) -> None:
        self.assertEqual(infer_route("MIT Sloan MBA 是否要求 GRE 或 GMAT？"), "deep")
        self.assertEqual(infer_route("MIT Biology 是否要求 TOEFL 100？"), "deep")
        self.assertEqual(infer_route("MIT EECS PhD TOEFL 要求是多少？"), "fact")

    def test_fact_lookup_does_not_treat_linguistics_as_cs(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT linguistics application deadline 是什么时候？")
        text = answer_from_facts(facts)

        self.assertIn("linguistics", text)
        self.assertIn("December 15 at 11:59 PM Eastern Time", text)

    def test_fact_lookup_prefers_exact_program_slug_over_broader_program(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT economics application fee 是多少？")
        text = answer_from_facts(facts)

        self.assertIn("https://oge.mit.edu/programs/economics", text)
        self.assertNotIn("data-economics-and-development-policy", text)

    def test_fact_lookup_does_not_treat_microbiology_as_biology_hint(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT microbiology application fee 是多少？")
        text = answer_from_facts(facts)

        self.assertIn("https://oge.mit.edu/programs/microbiology", text)
        self.assertNotIn("https://oge.mit.edu/programs/biology", text)

    def test_fact_lookup_distinguishes_regular_action_deadline(self) -> None:
        facts = self.store.lookup_facts("mit", "MIT undergraduate regular action deadline 是什么时候？")
        text = answer_from_facts(facts)

        self.assertIn("January 5", text)

    def test_deep_scope_returns_evidence(self) -> None:
        scopes = self.store.find_url_scope("mit", "MIT EECS PhD 是否接受非 CS 背景？")
        urls = [row["source_url"] for row in scopes]
        self.assertTrue(any("electrical-engineering-and-computer-science" in url for url in urls))

    def test_find_url_scope_can_filter_by_source_id(self) -> None:
        source_id = "src_mit_oge_mit_edu_programs_electrical_engineering_and_computer_science"
        scopes = self.store.find_url_scope(
            "mit",
            "MIT EECS PhD TOEFL",
            source_id=source_id,
        )

        self.assertTrue(scopes)
        self.assertTrue(all(row["source_id"] == source_id for row in scopes))


if __name__ == "__main__":
    unittest.main()
