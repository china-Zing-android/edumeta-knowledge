from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from catalog_parser.diff import diff_school, normalized_record_hash, write_diff_report
from catalog_parser.mit_parser import parse_mit_markdown


ROOT = Path(__file__).resolve().parents[1]
MIT_DATA = ROOT / "data/normalized/mit"
MIT_MD = ROOT / "docs/MIT_知识库_完整深度数据_v2.md"


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


class DiffSchoolTests(unittest.TestCase):
    def copy_dataset(self, root: Path, name: str) -> Path:
        target = root / name
        shutil.copytree(MIT_DATA, target)
        return target

    def test_identical_dataset_is_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous = self.copy_dataset(root, "previous")
            current = self.copy_dataset(root, "current")

            report = diff_school(previous, current, "mit")

            self.assertEqual(report["status"], "unchanged")
            self.assertEqual(report["change_count"], 0)
            self.assertEqual(report["affected"]["source_ids"], [])
            self.assertTrue(report["publishable"])

    def test_operational_weknora_metadata_is_ignored_by_normalized_hash(self) -> None:
        rows = read_jsonl(MIT_DATA / "url_manifest.jsonl")
        before = normalized_record_hash(rows[0])
        rows[0]["import_status"] = "running"
        rows[0]["weknora_document_id"] = "wk_doc_new"

        self.assertEqual(before, normalized_record_hash(rows[0]))

    def test_single_fact_change_reports_affected_source_without_reimport(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous = self.copy_dataset(root, "previous")
            current = self.copy_dataset(root, "current")
            facts = read_jsonl(current / "quick_facts.jsonl")
            facts[0]["raw_value"] = f"{facts[0]['raw_value']} updated"
            write_jsonl(current / "quick_facts.jsonl", facts)

            report = diff_school(previous, current, "mit")

            self.assertEqual(report["status"], "changed")
            self.assertEqual(report["entities"]["quick_facts"]["counts"]["changed"], 1)
            self.assertEqual(report["affected"]["fact_ids"], [facts[0]["fact_id"]])
            self.assertEqual(report["affected"]["source_ids"], [facts[0]["source_id"]])
            self.assertEqual(report["weknora_reimport_source_ids"], [])
            self.assertTrue(report["single_source_update"])

    def test_source_url_change_requires_weknora_reimport_for_that_source(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous = self.copy_dataset(root, "previous")
            current = self.copy_dataset(root, "current")
            sources = read_jsonl(current / "source_registry.jsonl")
            sources[0]["canonical_url"] = f"{sources[0]['canonical_url']}?updated=1"
            write_jsonl(current / "source_registry.jsonl", sources)

            report = diff_school(previous, current, "mit")

            self.assertEqual(report["status"], "changed")
            self.assertEqual(report["weknora_reimport_source_ids"], [sources[0]["source_id"]])
            self.assertTrue(report["single_source_update"])

    def test_context_only_change_is_publishable_without_weknora_reimport(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous = self.copy_dataset(root, "previous")
            current = self.copy_dataset(root, "current")
            contexts = parse_mit_markdown(MIT_MD).entity_contexts
            write_jsonl(previous / "entity_contexts.jsonl", contexts)
            changed_contexts = [dict(row) for row in contexts]
            economics = next(row for row in changed_contexts if row.get("display_label") == "14-1 Economics")
            economics["display_label"] = "14-1 Economics updated context"
            write_jsonl(current / "entity_contexts.jsonl", changed_contexts)

            report = diff_school(previous, current, "mit")

            self.assertEqual(report["status"], "changed")
            self.assertEqual(report["entities"]["entity_contexts"]["counts"]["changed"], 1)
            self.assertEqual(report["affected"]["context_ids"], [economics["context_id"]])
            self.assertEqual(report["weknora_reimport_source_ids"], [])
            self.assertTrue(report["publishable"])

    def test_physical_removal_of_active_record_blocks_publish(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            previous = self.copy_dataset(root, "previous")
            current = self.copy_dataset(root, "current")
            facts = read_jsonl(current / "quick_facts.jsonl")
            removed_fact_id = facts[0]["fact_id"]
            write_jsonl(current / "quick_facts.jsonl", facts[1:])

            report = diff_school(previous, current, "mit")

            self.assertEqual(report["status"], "failed")
            self.assertFalse(report["publishable"])
            self.assertIn(removed_fact_id, report["entities"]["quick_facts"]["removed_active_ids"])
            self.assertTrue(report["blocking_failures"])

    def test_write_diff_report_creates_parent_directory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "reports" / "diff.json"
            write_diff_report(path, {"status": "changed"})

            self.assertEqual(json.loads(path.read_text(encoding="utf-8"))["status"], "changed")


if __name__ == "__main__":
    unittest.main()
