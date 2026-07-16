from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from persist_qa_report import base_qa_case_id, load_jsonl, review_id_for_result, score_from_result, write_persistence_report  # noqa: E402


class QAPersistenceTests(unittest.TestCase):
    def test_load_jsonl_reads_cases(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "cases.jsonl"
            path.write_text('{"qa_case_id":"a"}\n{"qa_case_id":"b"}\n', encoding="utf-8")

            self.assertEqual([row["qa_case_id"] for row in load_jsonl(path)], ["a", "b"])

    def test_score_from_result_marks_pass_as_full_score(self) -> None:
        scores = score_from_result({"passed": True, "failures": []})

        self.assertEqual(scores["answer_correctness"], 2)
        self.assertFalse(scores["hallucination_flag"])
        self.assertIn("pass", scores["reviewer_notes"])

    def test_score_from_result_marks_must_not_include_as_hallucination(self) -> None:
        scores = score_from_result({"passed": False, "failures": ["contains must_not_include: wrong school"]})

        self.assertEqual(scores["answer_correctness"], 0)
        self.assertTrue(scores["hallucination_flag"])

    def test_conversation_turn_result_maps_to_base_case_but_keeps_distinct_review_id(self) -> None:
        self.assertEqual(base_qa_case_id("case_001::turn_1"), "case_001")
        self.assertEqual(base_qa_case_id("case_001"), "case_001")
        self.assertEqual(
            review_id_for_result("conv_run", {"qa_case_id": "case_001::turn_1"}),
            "auto_conv_run_case_001__turn_1",
        )

    def test_write_persistence_report_adds_generated_at(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "qa" / "report.json"

            write_persistence_report(path, {"status": "persisted", "cases": 30})

            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "persisted")
            self.assertEqual(payload["cases"], 30)
            self.assertTrue(payload["generated_at"])


if __name__ == "__main__":
    unittest.main()
