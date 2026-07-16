from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from catalog_parser.postgres_loader import load_dataset
from catalog_parser.validation import validate_school, write_validation_report


ROOT = Path(__file__).resolve().parents[1]
MIT_DATA = ROOT / "data/normalized/mit"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


class ValidationGateTests(unittest.TestCase):
    def copy_dataset(self, root: Path) -> Path:
        target = root / "mit"
        shutil.copytree(MIT_DATA, target)
        return target

    def test_validate_existing_mit_dataset_passes_data_gate(self) -> None:
        report = validate_school(MIT_DATA, "mit")

        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["counts"]["catalog_entries"], 157)
        self.assertEqual(report["checks"]["required_fields"]["complete_rate"], 1.0)
        self.assertEqual(report["checks"]["url_legal_rate"]["status"], "passed")
        self.assertEqual(report["checks"]["mit_reconciliation"]["status"], "passed")

    def test_invalid_url_fails_schema_and_url_rate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = self.copy_dataset(Path(temp_dir))
            rows = read_jsonl(data_dir / "source_registry.jsonl")
            for row in rows[:10]:
                row["canonical_url"] = "not-a-url"
                row["source_url"] = "not-a-url"
            write_jsonl(data_dir / "source_registry.jsonl", rows)

            report = validate_school(data_dir, "mit")

            self.assertEqual(report["status"], "failed")
            self.assertIn("url_legal_rate", report["failures"])

    def test_missing_cross_reference_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = self.copy_dataset(Path(temp_dir))
            rows = read_jsonl(data_dir / "catalog_entries.jsonl")
            rows[0]["source_id"] = "src_missing_reference"
            write_jsonl(data_dir / "catalog_entries.jsonl", rows)

            report = validate_school(data_dir, "mit")

            self.assertEqual(report["status"], "failed")
            self.assertIn("cross_references", report["failures"])

    def test_entity_context_missing_cross_references_fail(self) -> None:
        mutations = (
            ("program entry", lambda row: row.update(entry_id="ent_missing")),
            ("source", lambda row: row.update(source_ids=["src_missing"])),
            (
                "related program",
                lambda row: row.update(
                    related_entities=[
                        {
                            **row["related_entities"][0],
                            "entity_id": "ent_missing",
                            "entry_id": "ent_missing",
                        }
                    ]
                ),
            ),
        )
        for label, mutate in mutations:
            with self.subTest(label=label), tempfile.TemporaryDirectory() as temp_dir:
                data_dir = self.copy_dataset(Path(temp_dir))
                rows = load_dataset(data_dir, "mit")["entity_contexts"]
                program = next(
                    row
                    for row in rows
                    if row["entity_type"] == "program" and row["related_entities"]
                )
                mutate(program)
                write_jsonl(data_dir / "entity_contexts.jsonl", rows)

                report = validate_school(data_dir, "mit")

                self.assertEqual(report["status"], "failed")
                self.assertIn("cross_references", report["failures"])

    def test_mit_reconciliation_failure_blocks_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = self.copy_dataset(Path(temp_dir))
            rows = read_jsonl(data_dir / "catalog_entries.jsonl")
            write_jsonl(data_dir / "catalog_entries.jsonl", rows[1:])

            report = validate_school(data_dir, "mit")

            self.assertEqual(report["status"], "failed")
            self.assertIn("mit_reconciliation", report["failures"])

    def test_write_validation_report_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "validation.json"
            write_validation_report(path, {"status": "passed"})

            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "passed")


if __name__ == "__main__":
    unittest.main()
