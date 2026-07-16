from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from runtime_acceptance import REQUIRED_ALIASES, current_source_import_failures, current_source_job_failures  # noqa: E402


class RuntimeAcceptanceTests(unittest.TestCase):
    def test_entity_context_alias_is_required(self) -> None:
        self.assertIn("l1_entity_contexts_current", REQUIRED_ALIASES)

    def test_current_sources_must_have_terminal_successful_imports(self) -> None:
        self.assertEqual(current_source_import_failures({"success": 127}), [])
        self.assertEqual(
            current_source_import_failures({"success": 125, "running": 1, "failed": 1}),
            ["current_sources_running=1", "current_sources_failed=1"],
        )

    def test_current_success_sources_require_success_job_audit(self) -> None:
        self.assertEqual(current_source_job_failures(0), [])
        self.assertEqual(current_source_job_failures(3), ["current_success_sources_without_success_job=3"])


if __name__ == "__main__":
    unittest.main()
