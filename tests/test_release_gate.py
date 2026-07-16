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

from release_gate import GateSpec, evaluate_release_gate, gate_specs_for_profile, latest_report_path, write_report  # noqa: E402


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload), encoding="utf-8")


class ReleaseGateTests(unittest.TestCase):
    def test_all_specs_pass_when_statuses_and_details_pass(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            a = root / "a.json"
            b = root / "b.json"
            write_json(a, {"status": "passed", "failed": 0, "failures": []})
            write_json(b, {"status": "ready", "failures": []})
            specs = [
                GateSpec("qa", a, frozenset({"passed"})),
                GateSpec("readiness", b, frozenset({"ready"})),
            ]

            report = evaluate_release_gate(specs)

            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["failed"], 0)

    def test_missing_report_blocks_release(self) -> None:
        specs = [GateSpec("missing", Path("/tmp/does-not-exist-release-gate.json"), frozenset({"passed"}))]

        report = evaluate_release_gate(specs)

        self.assertEqual(report["status"], "failed")
        self.assertIn("report file missing", report["failures"][0])

    def test_unaccepted_status_blocks_release(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "readiness.json"
            write_json(path, {"status": "not_ready", "failures": ["weknora missing"]})

            report = evaluate_release_gate([GateSpec("external_readiness", path, frozenset({"ready"}))])

            self.assertEqual(report["status"], "failed")
            self.assertTrue(any("not_ready" in failure for failure in report["failures"]))

    def test_manual_qa_can_be_explicitly_deferred_without_being_marked_passed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            automated = root / "automated.json"
            human = root / "human.json"
            write_json(automated, {"status": "passed", "failed": 0, "failures": []})
            write_json(human, {"status": "not_ready", "failures": ["human review file is missing"]})

            report = evaluate_release_gate(
                [
                    GateSpec("automated", automated, frozenset({"passed"})),
                    GateSpec("human_qa", human, frozenset({"passed"}), defer_allowed=True),
                ],
                manual_qa_mode="deferred",
            )

        self.assertEqual(report["status"], "passed_with_deferred_manual_qa")
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["deferred_gates"], ["human_qa"])

    def test_latest_report_path_prefers_newest_matching_external_report(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            reports = Path(temp_dir)
            older = reports / "external-live-smoke-2026-07-09.json"
            newer = reports / "external-live-smoke-2026-07-10.json"
            write_json(older, {"status": "not_ready"})
            write_json(newer, {"status": "passed"})

            selected = latest_report_path(reports, "external-live-smoke-*.json", older.name)

        self.assertEqual(selected.name, newer.name)

    def test_mit_profile_uses_current_retrieval_gates(self) -> None:
        names = [spec.name for spec in gate_specs_for_profile("mit")]

        self.assertEqual(
            names,
            ["retrieval_acceptance", "cross_university_acceptance", "mcp_benchmark", "incremental_update", "runtime_compose"],
        )

    def test_release_profile_selects_latest_retrieval_reports(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            reports = root / "qa/reports"
            write_json(reports / "retrieval-acceptance-2026-07-15.json", {"status": "failed"})
            write_json(reports / "retrieval-acceptance-2026-07-16.json", {"status": "passed"})
            write_json(reports / "cross-university-acceptance-2026-07-16.json", {"status": "passed"})

            specs = gate_specs_for_profile("mit", root)

        self.assertEqual(specs[0].path.name, "retrieval-acceptance-2026-07-16.json")
        self.assertEqual(specs[1].path.name, "cross-university-acceptance-2026-07-16.json")

    def test_write_report_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "release.json"
            write_report(path, {"status": "failed"})

            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "failed")


if __name__ == "__main__":
    unittest.main()
