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

from generate_release_artifacts import failures_by_gate, generate_artifacts, review_failure_categories  # noqa: E402


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


class GenerateReleaseArtifactsTests(unittest.TestCase):
    def test_failures_by_gate_groups_release_failures(self) -> None:
        grouped = failures_by_gate({"failures": ["mvp_scope: missing schools", "external: missing env", "plain failure"]})

        self.assertEqual(grouped["mvp_scope"], ["missing schools"])
        self.assertEqual(grouped["external"], ["missing env"])
        self.assertEqual(grouped["unknown"], ["plain failure"])

    def test_review_failure_categories_counts_low_scores_and_flags(self) -> None:
        counts = review_failure_categories(
            [
                {"answer_correctness": 2, "evidence_match": 1, "failure_category": "evidence_gate"},
                {"answer_correctness": 2, "evidence_match": 2, "hallucination_flag": True, "failure_category": "llm_generation"},
                {"answer_correctness": 2, "evidence_match": 2, "hallucination_flag": False},
            ]
        )

        self.assertEqual(counts["evidence_gate"], 1)
        self.assertEqual(counts["llm_generation"], 1)

    def test_generate_artifacts_writes_acceptance_qa_and_failure_markdown(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_json(
                root / "release.json",
                {
                    "status": "failed",
                    "total": 2,
                    "passed": 1,
                    "failed": 1,
                    "failures": ["mvp_scope: normalized school count below threshold"],
                    "results": [
                        {"name": "data_validation", "status": "passed", "passed": True, "failures": []},
                        {"name": "mvp_scope", "status": "failed", "passed": False, "failures": ["missing schools"]},
                    ],
                },
            )
            write_json(
                root / "scope.json",
                {
                    "normalized_schools": {"count": 1},
                    "uat_cases": {"university_count": 1},
                    "conversation_cases": {"university_count": 1},
                },
            )
            write_json(
                root / "human-review.json",
                {
                    "status": "failed",
                    "reviewed_case_count": 1,
                    "reviewed_conversation_count": 0,
                    "failures": ["P0 blocking review failures: case_001"],
                    "metrics": {"evidence_match_rate": 0.0, "clarification_quality_rate": 1.0, "task_completion_rate": 0.0},
                },
            )
            write_json(root / "mit-gold.json", {"status": "report", "total": 30, "passed": 30, "failed": 0})
            write_json(root / "uat.json", {"status": "report", "total": 200, "passed": 199, "failed": 1})
            write_json(root / "conv.json", {"status": "report", "total": 100, "passed": 100, "failed": 0})
            write_jsonl(
                root / "human-reviews.jsonl",
                [{"qa_case_id": "case_001", "answer_correctness": 1, "evidence_match": 0, "failure_category": "llm_generation"}],
            )

            result = generate_artifacts(
                release_report_path=root / "release.json",
                scope_report_path=root / "scope.json",
                human_review_gate_path=root / "human-review.json",
                human_reviews_path=root / "human-reviews.jsonl",
                qa_report_paths={
                    "mit_gold": root / "mit-gold.json",
                    "mvp_uat": root / "uat.json",
                    "mvp_conversations": root / "conv.json",
                },
                output_dir=root / "qa",
                report_date="2026-07-09",
            )

            self.assertEqual(result["status"], "written")
            acceptance = (root / "qa/acceptance-report-2026-07-09.md").read_text(encoding="utf-8")
            qa_report = (root / "qa/qa-report-2026-07-09.md").read_text(encoding="utf-8")
            failure = (root / "qa/failure-analysis-2026-07-09.md").read_text(encoding="utf-8")
            self.assertIn("NOT RELEASE READY", acceptance)
            self.assertIn("| mvp_uat | report | 200 | 199 | 1 |", qa_report)
            self.assertIn("normalized school count below threshold", failure)
            self.assertIn("llm_generation: 1", failure)

    def test_generate_mit_profile_artifacts_use_mit_scope_text(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            write_json(
                root / "release.json",
                {
                    "status": "failed",
                    "total": 1,
                    "passed": 0,
                    "failed": 1,
                    "failures": ["human_qa_review_mit: not ready"],
                    "results": [
                        {"name": "human_qa_review_mit", "status": "not_ready", "passed": False, "failures": ["not ready"]},
                    ],
                },
            )
            write_json(
                root / "live-data.json",
                {
                    "status": "passed",
                    "schools": {
                        "mit": {
                            "expected_counts": {
                                "catalog_entries": 157,
                                "url_manifest": 107,
                                "quick_facts": 241,
                            }
                        }
                    },
                },
            )
            write_json(root / "human-review.json", {"status": "not_ready", "reviewed_case_count": 0, "reviewed_conversation_count": 0})
            write_json(root / "mit-gold.json", {"status": "report", "total": 30, "passed": 30, "failed": 0})
            write_json(root / "mit-conv.json", {"status": "report", "total": 6, "passed": 6, "failed": 0})

            generate_artifacts(
                release_report_path=root / "release.json",
                scope_report_path=root / "live-data.json",
                human_review_gate_path=root / "human-review.json",
                human_reviews_path=root / "human-reviews.jsonl",
                qa_report_paths={
                    "mit_gold": root / "mit-gold.json",
                    "mit_conversations": root / "mit-conv.json",
                },
                output_dir=root / "qa",
                report_date="mit-2026-07-09",
                profile="mit",
            )

            acceptance = (root / "qa/acceptance-report-mit-2026-07-09.md").read_text(encoding="utf-8")
            failure = (root / "qa/failure-analysis-mit-2026-07-09.md").read_text(encoding="utf-8")
            self.assertIn("MIT Acceptance Report", acceptance)
            self.assertIn("Acceptance profile: MIT only", acceptance)
            self.assertIn("MIT catalog entries: 157", acceptance)
            self.assertNotIn("At least five normalized schools", failure)


if __name__ == "__main__":
    unittest.main()
