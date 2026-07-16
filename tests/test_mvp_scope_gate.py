from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from mvp_scope_gate import evaluate_mvp_scope, infer_university_id, normalized_school_ids, write_report  # noqa: E402


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


class MvpScopeGateTests(unittest.TestCase):
    def test_normalized_school_ids_require_all_jsonl_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            school = root / "mit"
            school.mkdir()
            for file_name in ("source_registry.jsonl", "catalog_entries.jsonl", "url_manifest.jsonl", "quick_facts.jsonl"):
                (school / file_name).write_text("", encoding="utf-8")
            incomplete = root / "stanford"
            incomplete.mkdir()
            (incomplete / "catalog_entries.jsonl").write_text("", encoding="utf-8")

            self.assertEqual(normalized_school_ids(root), ["mit"])

    def test_infer_university_id_from_explicit_id_case_id_or_text(self) -> None:
        known = {"mit", "stanford"}

        self.assertEqual(infer_university_id({"university_id": "MIT"}, known), "mit")
        self.assertEqual(infer_university_id({"qa_case_id": "mvp_stanford_catalog_001"}, known), "stanford")
        self.assertEqual(infer_university_id({"question": "MIT TOEFL 要求是多少？"}, known), "mit")

    def test_scope_gate_fails_current_like_one_school_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_root = root / "normalized"
            shutil.copytree(ROOT / "data/normalized/mit", data_root / "mit")
            reports = root / "reports"
            for name in ("all-validation-gate", "all-diff-gate", "all-index-gate", "all-weknora-sync-gate"):
                write_json(reports / f"{name}-2026-07-09.json", {"status": "success", "total": 1, "succeeded": 1, "failed": 0})
            uat_path = root / "mvp-uat-cases.jsonl"
            conv_path = root / "mvp-uat-conversations.jsonl"
            write_jsonl(uat_path, [{"qa_case_id": "mvp_mit_fact_001", "question": "MIT TOEFL?"}] * 200)
            write_jsonl(conv_path, [{"qa_case_id": "mvp_mit_conv_001", "question": "MIT fee?"}] * 50)

            report = evaluate_mvp_scope(
                data_root=data_root,
                uat_cases_path=uat_path,
                conversation_cases_path=conv_path,
                reports_root=reports,
                min_mcp_tool_cases=0,
            )

            self.assertEqual(report["status"], "failed")
            self.assertTrue(any("normalized school count" in failure for failure in report["failures"]))
            self.assertTrue(any("UAT university coverage" in failure for failure in report["failures"]))

    def test_scope_gate_blocks_missing_route_distribution_and_mcp_cases(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            data_root = root / "normalized"
            for school_id in ["a", "b", "c", "d", "e"]:
                school = data_root / school_id
                school.mkdir(parents=True)
                for file_name in ("source_registry.jsonl", "catalog_entries.jsonl", "url_manifest.jsonl", "quick_facts.jsonl"):
                    write_jsonl(school / file_name, [{"id": f"{school_id}_{file_name}"}])
            reports = root / "reports"
            for name in ("all-validation-gate", "all-diff-gate", "all-index-gate", "all-weknora-sync-gate"):
                write_json(reports / f"{name}-2026-07-09.json", {"status": "success", "total": 5, "succeeded": 5, "failed": 0})
            uat_path = root / "mvp-uat-cases.jsonl"
            conv_path = root / "mvp-uat-conversations.jsonl"
            tool_path = root / "tool-cases.jsonl"
            write_jsonl(
                uat_path,
                [
                    {"qa_case_id": f"mvp_{school}_fact_{index}", "university_id": school, "expected_route": "fact", "question": school}
                    for index, school in enumerate(["a", "b", "c", "d", "e"], start=1)
                ],
            )
            write_jsonl(
                conv_path,
                [
                    {"qa_case_id": f"mvp_{school}_conv_{index}", "university_id": school, "expected_route": "fact", "question": school}
                    for index, school in enumerate(["a", "b", "c", "d", "e"], start=1)
                ],
            )
            write_jsonl(tool_path, [{"case_id": "tool_001"}])

            report = evaluate_mvp_scope(
                data_root=data_root,
                uat_cases_path=uat_path,
                conversation_cases_path=conv_path,
                tool_cases_path=tool_path,
                reports_root=reports,
                min_uat_cases=5,
                min_conversations=5,
                min_catalog_cases=1,
                min_fact_cases=1,
                min_deep_cases=1,
                min_clarification_cases=1,
                min_mcp_tool_cases=10,
            )

            self.assertEqual(report["status"], "failed")
            self.assertTrue(any("UAT catalog case count" in failure for failure in report["failures"]))
            self.assertTrue(any("conversation suite has no catalog" in failure for failure in report["failures"]))
            self.assertTrue(any("MCP/tool calling case count" in failure for failure in report["failures"]))

    def test_write_report_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "scope.json"
            write_report(path, {"status": "failed"})

            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "failed")


if __name__ == "__main__":
    unittest.main()
