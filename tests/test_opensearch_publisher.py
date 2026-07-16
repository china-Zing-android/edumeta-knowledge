from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from indexer.opensearch_publisher import bulk_actions, dry_run_report, load_publish_plan


class OpenSearchPublisherTests(unittest.TestCase):
    def test_publish_plan_allows_empty_optional_entity_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = Path(temp_dir)
            source_dir = Path("data/normalized/mit")
            (data_dir / "catalog_entries.jsonl").write_text(
                source_dir.joinpath("catalog_entries.jsonl").read_text("utf-8").splitlines()[0] + "\n",
                "utf-8",
            )
            (data_dir / "quick_facts.jsonl").write_text("", "utf-8")
            (data_dir / "url_manifest.jsonl").write_text(
                source_dir.joinpath("url_manifest.jsonl").read_text("utf-8").splitlines()[0] + "\n",
                "utf-8",
            )

            plan = load_publish_plan(data_dir, "mit")

        self.assertEqual(plan["quick_facts"]["count"], 0)
        self.assertEqual(plan["quick_facts"]["dataset_version"], plan["catalog_entries"]["dataset_version"])

    def test_dry_run_uses_global_aliases(self) -> None:
        report = dry_run_report(Path("data/normalized/mit"), "mit")

        self.assertEqual(report["status"], "validated")
        self.assertEqual(report["indexes"]["catalog_entries"]["count"], 157)
        self.assertEqual(report["indexes"]["sources"]["count"], 112)
        self.assertEqual(report["indexes"]["quick_facts"]["count"], 241)
        self.assertEqual(report["indexes"]["universities"]["count"], 1)
        self.assertEqual(report["indexes"]["entity_contexts"]["count"], 158)
        self.assertEqual(report["indexes"]["catalog_entries"]["alias"], "l1_catalog_entries_current")
        self.assertEqual(report["indexes"]["sources"]["alias"], "l1_sources_current")
        self.assertEqual(report["indexes"]["entity_contexts"]["alias"], "l1_entity_contexts_current")

    def test_bulk_actions_use_entity_primary_key(self) -> None:
        plan = load_publish_plan(Path("data/normalized/mit"), "mit")
        item = plan["catalog_entries"]
        actions = bulk_actions(item["write_index"], "entry_id", item["records"][:1])

        self.assertEqual(actions[0]["_index"], item["write_index"])
        self.assertEqual(
            actions[0]["_id"],
            f"mit:{item['records'][0]['dataset_version']}:{item['records'][0]['entry_id']}",
        )
        self.assertEqual(actions[0]["_source"]["university_id"], "mit")

    def test_school_update_writes_only_that_school_documents(self) -> None:
        plan = load_publish_plan(Path("data/normalized/mit"), "mit")

        for item in plan.values():
            self.assertTrue(all(row["university_id"] == "mit" for row in item["records"]))

    def test_entity_context_projection_is_current_and_uses_stable_context_ids(self) -> None:
        plan = load_publish_plan(Path("data/normalized/mit"), "mit")
        contexts = plan["entity_contexts"]["records"]

        self.assertTrue(contexts)
        self.assertTrue(all(row["is_current"] is True for row in contexts))
        self.assertEqual(len({row["context_id"] for row in contexts}), len(contexts))
        self.assertTrue(any(row["entity_type"] == "university" for row in contexts))
        self.assertTrue(any(row["entity_type"] == "program" for row in contexts))

    def test_publish_plan_enriches_current_catalog_with_university_range_metadata(self) -> None:
        plan = load_publish_plan(
            Path("data/normalized/mit"),
            "mit",
            university_metadata={
                "university_name": "Massachusetts Institute of Technology",
                "aliases": ["MIT"],
                "country_code": "US",
                "region": "Massachusetts",
                "school_tier": "core",
            },
        )

        university = plan["universities"]["records"][0]
        catalog = plan["catalog_entries"]["records"][0]
        self.assertTrue(university["is_current"])
        self.assertEqual(university["country_code"], "US")
        self.assertTrue(catalog["is_current"])
        self.assertEqual(catalog["school_tier"], "core")
        self.assertTrue(catalog["discipline_ids"])


if __name__ == "__main__":
    unittest.main()
