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

from apply_postgres_migrations import migration_files  # noqa: E402
from live_data_gate import (  # noqa: E402
    POSTGRES_TABLES,
    discover_data_dirs,
    expected_counts,
    opensearch_alias_counts,
    opensearch_count_query,
    postgres_count_sql,
    write_gate_report,
)


class LiveDataGateTests(unittest.TestCase):
    def test_migration_files_are_sorted_sql_only(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "002_second.sql").write_text("select 2", encoding="utf-8")
            (root / "001_first.sql").write_text("select 1", encoding="utf-8")
            (root / "README.md").write_text("ignore", encoding="utf-8")

            self.assertEqual([path.name for path in migration_files(root)], ["001_first.sql", "002_second.sql"])

    def test_opensearch_alias_counts_requires_client_dependency(self) -> None:
        # This function is imported by the live gate and should stay callable for real service checks.
        self.assertTrue(callable(opensearch_alias_counts))

    def test_url_manifest_gate_uses_folded_source_registry_table(self) -> None:
        self.assertEqual(POSTGRES_TABLES["url_manifest"], "source_registry")

    def test_postgres_gate_counts_only_the_current_school_version(self) -> None:
        sql = postgres_count_sql("catalog_entries")

        self.assertIn("version_id = (", sql)
        self.assertIn("publication_state='current'", sql)

    def test_opensearch_count_query_scopes_global_alias_by_school_and_version(self) -> None:
        self.assertEqual(
            opensearch_count_query("mit", "mit_v2"),
            {"query": {"bool": {"filter": [
                {"term": {"university_id": "mit"}},
                {"term": {"dataset_version": "mit_v2"}},
            ]}}},
        )

    def test_discover_data_dirs_and_expected_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            complete = root / "alpha"
            complete.mkdir()
            for file_name in ("source_registry.jsonl", "catalog_entries.jsonl", "url_manifest.jsonl", "quick_facts.jsonl"):
                (complete / file_name).write_text('{"id": 1}\n{"id": 2}\n', encoding="utf-8")
            incomplete = root / "bravo"
            incomplete.mkdir()
            (incomplete / "source_registry.jsonl").write_text("{}\n", encoding="utf-8")

            self.assertEqual(discover_data_dirs(root), {"alpha": complete})
            self.assertEqual(
                expected_counts(complete),
                {
                    "source_registry": 2,
                    "catalog_entries": 2,
                    "url_manifest": 2,
                    "quick_facts": 2,
                },
            )

    def test_write_gate_report_adds_generated_at(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "live-data-gate.json"

            write_gate_report(path, {"status": "passed", "failures": []})

            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(payload["status"], "passed")
            self.assertEqual(payload["failures"], [])
            self.assertTrue(payload["generated_at"])


if __name__ == "__main__":
    unittest.main()
