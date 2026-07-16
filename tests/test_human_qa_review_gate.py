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

from human_qa_review_gate import build_gate_report, evaluate_human_reviews, write_report  # noqa: E402
from release_gate import default_gate_specs  # noqa: E402


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def case(case_id: str, *, risk_level: str = "P1", expected_route: str = "fact", conversation: bool = False) -> dict:
    return {
        "qa_case_id": case_id,
        "persona": "graduate_applicant",
        "question": "Question?",
        "conversation_context": [{"role": "user", "content": "Previous?"}] if conversation else [],
        "expected_route": expected_route,
        "expected_behavior": "Expected behavior",
        "must_include": [],
        "must_not_include": [],
        "required_source_url": "https://example.edu",
        "risk_level": risk_level,
        "reviewer_owner": "qa",
    }


def review(case_id: str, **overrides: object) -> dict:
    payload = {
        "review_id": f"hr_{case_id}",
        "qa_case_id": case_id,
        "trace_id": f"tr_{case_id}",
        "reviewer_id": "human_reviewer",
        "answer_correctness": 2,
        "evidence_match": 2,
        "freshness_version_correctness": 2,
        "clarification_quality": 2,
        "task_completion": 2,
        "hallucination_flag": False,
        "unsafe_or_overconfident_flag": False,
        "failure_category": None,
        "reviewer_notes": "human reviewed",
    }
    payload.update(overrides)
    return payload


class HumanQAReviewGateTests(unittest.TestCase):
    def test_missing_review_file_is_not_ready(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            cases_path = root / "cases.jsonl"
            write_jsonl(cases_path, [case("case_001")])

            report = build_gate_report(
                case_paths=[cases_path],
                reviews_path=root / "missing.jsonl",
                min_reviewed_cases=1,
                min_reviewed_conversations=0,
            )

            self.assertEqual(report["status"], "not_ready")
            self.assertTrue(any("missing or empty" in item for item in report["failures"]))

    def test_passing_human_reviews_pass_gate(self) -> None:
        cases = {
            "case_001": case("case_001", risk_level="P0"),
            "case_002": case("case_002", expected_route="clarification", conversation=True),
        }
        reviews = [review("case_001"), review("case_002")]

        report = evaluate_human_reviews(
            cases=cases,
            reviews=reviews,
            min_reviewed_cases=2,
            min_reviewed_conversations=1,
        )

        self.assertEqual(report["status"], "passed", report["failures"])
        self.assertEqual(report["metrics"]["evidence_match_rate"], 1.0)
        self.assertEqual(report["reviewed_conversation_count"], 1)

    def test_p0_incorrect_review_blocks_release(self) -> None:
        cases = {"case_001": case("case_001", risk_level="P0")}
        reviews = [review("case_001", answer_correctness=1, evidence_match=2, failure_category="llm_generation")]

        report = evaluate_human_reviews(
            cases=cases,
            reviews=reviews,
            min_reviewed_cases=1,
            min_reviewed_conversations=0,
        )

        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("P0 blocking" in item for item in report["failures"]))

    def test_partial_or_flagged_review_requires_failure_category(self) -> None:
        cases = {"case_001": case("case_001", risk_level="P1")}
        reviews = [review("case_001", evidence_match=1)]

        report = evaluate_human_reviews(
            cases=cases,
            reviews=reviews,
            min_reviewed_cases=1,
            min_reviewed_conversations=0,
        )

        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("missing valid failure_category" in item for item in report["failures"]))

    def test_write_report_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "human-review.json"
            write_report(path, {"status": "not_ready"})

            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "not_ready")

    def test_release_gate_leaves_human_review_user_operated(self) -> None:
        names = [spec.name for spec in default_gate_specs(ROOT)]

        self.assertNotIn("human_qa_review", names)


if __name__ == "__main__":
    unittest.main()
