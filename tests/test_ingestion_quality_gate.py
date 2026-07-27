from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, Mock, patch

from fast_router.ingestion import IngestionService, QualityGateError, run_pre_publish_audit


ROOT = Path(__file__).resolve().parents[1]


class IngestionQualityGateTests(unittest.TestCase):
    def test_service_startup_reconciles_interrupted_in_memory_runs(self) -> None:
        connection = MagicMock()
        transaction = MagicMock()
        cursor = MagicMock()
        connection.transaction.return_value.__enter__.return_value = transaction
        connection.cursor.return_value.__enter__.return_value = cursor
        cursor.execute.return_value = None
        cursor.fetchall.return_value = [("mit", "ver_interrupted")]

        psycopg = MagicMock()
        psycopg.connect.return_value.__enter__.return_value = connection
        jsonb = Mock(side_effect=lambda value: value)
        with patch.dict("sys.modules", {
            "psycopg": psycopg,
            "psycopg.types.json": Mock(Jsonb=jsonb),
        }):
            service = object.__new__(IngestionService)
            service.postgres_dsn = "postgresql://unused"
            service._fail_interrupted_runs()

        statements = [call.args[0] for call in cursor.execute.call_args_list]
        self.assertTrue(any("service_restarted_before_ingestion_completed" in sql for sql in statements))
        self.assertTrue(any("publication_state='failed'" in sql for sql in statements))

    def test_pre_publish_audit_blocks_invalid_catalog_before_staging(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir) / "normalized"
            shutil.copytree(ROOT / "data/normalized/mit", data_dir)
            path = data_dir / "catalog_entries.jsonl"
            rows = [json.loads(line) for line in path.read_text("utf-8").splitlines() if line]
            rows[0]["program_name"] = "degrees.taxonomy"
            path.write_text("".join(json.dumps(row) + "\n" for row in rows), "utf-8")

            with self.assertRaises(QualityGateError) as caught:
                run_pre_publish_audit(data_dir, "mit")

        self.assertEqual(caught.exception.report["audit_status"], "failed")
        self.assertIn("entity_validity", caught.exception.report["failures"])

    def test_pre_publish_audit_blocks_needs_review_from_automatic_activation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir) / "normalized"
            shutil.copytree(ROOT / "data/normalized/mit", data_dir)
            path = data_dir / "catalog_entries.jsonl"
            rows = [json.loads(line) for line in path.read_text("utf-8").splitlines() if line]
            generic_url = rows[0]["source_url"]
            for row in rows:
                row["source_url"] = generic_url
            path.write_text("".join(json.dumps(row) + "\n" for row in rows), "utf-8")

            with self.assertRaises(QualityGateError) as caught:
                run_pre_publish_audit(data_dir, "mit")

        self.assertEqual(caught.exception.report["audit_status"], "failed")
        self.assertIn("source_specificity", caught.exception.report["warnings"])


if __name__ == "__main__":
    unittest.main()
