from __future__ import annotations

import os
import tempfile
import unittest
from pathlib import Path

from fast_router.knowledge import KnowledgeStore, answer_from_facts, evidence_from_scope, infer_route
from fast_router.qa import evaluate_qa_gate, run_conversation_cases, run_qa_cases, write_qa_report


ROOT = Path(__file__).resolve().parents[1]


class QARunnerTests(unittest.TestCase):
    def test_mit_gold_cases_have_valid_shape(self) -> None:
        os.environ["KNOWLEDGE_DATA_ROOT"] = str(ROOT / "data/normalized")
        store = KnowledgeStore.from_env()

        def answer(question: str) -> dict:
            university = store.resolve_university(question)
            university_id = university["university_id"] or "mit"
            route = infer_route(question)
            if route == "catalog":
                results = store.search_catalog(university_id, question, level="undergraduate" if "本科" in question else None)
                return {
                    "mode": "fast",
                    "route": "catalog",
                    "answer": "\n".join(r["program_name"] + " " + r["source_url"] for r in results),
                    "evidence": [],
                    "trace_id": "test",
                }
            if route == "fact":
                facts = store.lookup_facts(university_id, question)
                return {
                    "mode": "fast",
                    "route": "fact",
                    "answer": answer_from_facts(facts),
                    "evidence": facts,
                    "trace_id": "test",
                }
            scopes = store.find_url_scope(university_id, question)
            evidence = evidence_from_scope(store, university_id, scopes, question)
            return {
                "mode": "deep" if evidence else "deep_required",
                "route": "deep" if route == "deep" else "clarification",
                "answer": "clarify" if route == "clarification" else "evidence",
                "evidence": evidence,
                "trace_id": "test",
            }

        report = run_qa_cases(ROOT / "qa/mit-gold-cases.jsonl", answer)
        self.assertEqual(report["total"], 30)
        # The skeleton runner should execute every case and keep failure data structured.
        self.assertIn("results", report)

    def test_mvp_uat_cases_are_release_gate_ready(self) -> None:
        cases_path = ROOT / "qa/mvp-uat-cases.jsonl"
        cases = [
            __import__("json").loads(line)
            for line in cases_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        self.assertGreaterEqual(len(cases), 200)
        self.assertFalse(any("placeholder" in case["qa_case_id"] for case in cases))
        self.assertEqual({"catalog", "fact", "deep", "clarification"}, {case["expected_route"] for case in cases})
        for case in cases:
            self.assertTrue(case["qa_case_id"])
            self.assertTrue(case["persona"])
            self.assertTrue(case["question"])
            self.assertTrue(case["expected_behavior"])
            self.assertIsInstance(case.get("must_include"), list)
            self.assertIsInstance(case.get("must_not_include"), list)
            self.assertIn(case["risk_level"], {"P0", "P1", "P2"})
            self.assertTrue(case["reviewer_owner"])

    def test_mvp_uat_conversation_cases_are_release_gate_ready(self) -> None:
        cases_path = ROOT / "qa/mvp-uat-conversations.jsonl"
        cases = [
            __import__("json").loads(line)
            for line in cases_path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

        self.assertGreaterEqual(len(cases), 50)
        self.assertFalse(any("placeholder" in case["qa_case_id"] for case in cases))
        self.assertEqual({"catalog", "fact", "deep", "clarification"}, {case["expected_route"] for case in cases})
        for case in cases:
            self.assertTrue(case["qa_case_id"])
            self.assertTrue(case["persona"])
            self.assertTrue(case["question"])
            self.assertTrue(case["expected_behavior"])
            self.assertIsInstance(case.get("conversation_context"), list)
            self.assertGreaterEqual(len(case["conversation_context"]), 1)
            self.assertIsInstance(case.get("must_include"), list)
            self.assertIsInstance(case.get("must_not_include"), list)
            self.assertIn(case["risk_level"], {"P0", "P1", "P2"})
            self.assertTrue(case["reviewer_owner"])

    def test_qa_report_can_be_written_to_disk(self) -> None:
        report = {"total": 1, "passed": 1, "failed": 0, "results": []}
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "qa-report.json"
            write_qa_report(output_path, report)

            self.assertTrue(output_path.exists())
            self.assertIn('"passed": 1', output_path.read_text(encoding="utf-8"))

    def test_conversation_cases_evaluate_each_user_turn(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "conversations.jsonl"
            path.write_text(
                '{"qa_case_id":"conv_001","persona":"graduate_applicant","question":"那 IELTS 呢？",'
                '"conversation_context":[{"role":"user","content":"MIT EECS TOEFL 要求是多少？",'
                '"expected_route":"fact","must_include":["TOEFL 100"]}],'
                '"expected_route":"fact","expected_behavior":"多轮追问仍保持同一项目 scope。",'
                '"must_include":["IELTS 7"],"must_not_include":["Stanford"],'
                '"required_source_url":null,"risk_level":"P1","reviewer_owner":"qa"}\n',
                encoding="utf-8",
            )

            def answer(question: str, context: dict) -> dict:
                if "TOEFL" in question:
                    text = "TOEFL 100"
                else:
                    text = "IELTS 7"
                return {"route": "fact", "mode": "fast", "answer": text, "evidence": [{"source_id": "src"}], "trace_id": f"tr_{len(context['transcript'])}"}

            report = run_conversation_cases(path, answer)

            self.assertEqual(report["conversation_count"], 1)
            self.assertEqual(report["total"], 2)
            self.assertEqual(report["failed"], 0)

    def test_qa_gate_blocks_p0_failure_and_missing_trace(self) -> None:
        cases = [{"qa_case_id": "case_001", "risk_level": "P0"}]
        report = {
            "total": 1,
            "passed": 0,
            "failed": 1,
            "results": [{"qa_case_id": "case_001", "passed": False, "trace_id": None}],
        }

        gate = evaluate_qa_gate(report, cases, min_total=1)

        self.assertEqual(gate["status"], "failed")
        self.assertTrue(any("P0 failures" in item for item in gate["failures"]))
        self.assertTrue(any("missing trace_id" in item for item in gate["failures"]))

    def test_qa_gate_can_require_conversation_count(self) -> None:
        report = {
            "total": 20,
            "passed": 20,
            "failed": 0,
            "conversation_count": 10,
            "results": [{"qa_case_id": "case_001", "passed": True, "trace_id": "tr_test"}],
        }

        gate = evaluate_qa_gate(report, [{"qa_case_id": "case_001", "risk_level": "P1"}], min_total=20, min_conversations=50)

        self.assertEqual(gate["status"], "failed")
        self.assertTrue(any("conversation_count below threshold" in item for item in gate["failures"]))


if __name__ == "__main__":
    unittest.main()
