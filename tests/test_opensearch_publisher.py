from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from indexer.opensearch_publisher import (
    _ensure_index_and_alias,
    audit_staged_school,
    bulk_actions,
    dry_run_report,
    load_publish_plan,
    publish_school,
)


class OpenSearchPublisherTests(unittest.TestCase):
    def test_new_index_waits_for_primary_shard_before_aliasing(self) -> None:
        calls: list[str] = []

        class FakeIndices:
            def exists(self, **kwargs):
                return False

            def create(self, **kwargs):
                calls.append("create")

            def get_alias(self, **kwargs):
                calls.append("get_alias")
                return {}

            def put_alias(self, **kwargs):
                calls.append("put_alias")

        class FakeCluster:
            def health(self, **kwargs):
                calls.append("health")
                self.kwargs = kwargs
                return {"status": "yellow", "timed_out": False}

        class FakeClient:
            def __init__(self):
                self.indices = FakeIndices()
                self.cluster = FakeCluster()

        item = load_publish_plan(Path("data/normalized/mit"), "mit")["catalog_entries"]
        client = FakeClient()

        _ensure_index_and_alias(client, item)

        self.assertEqual(calls, ["create", "health", "get_alias", "put_alias"])
        self.assertEqual(client.cluster.kwargs["index"], item["write_index"])
        self.assertEqual(client.cluster.kwargs["timeout"], "120s")

    def test_schema_upgrade_reindexes_legacy_alias_before_atomic_switch(self) -> None:
        calls: list[tuple[str, dict]] = []
        state = {"target_count": 0}

        class FakeIndices:
            def exists(self, **kwargs):
                return False

            def create(self, **kwargs):
                calls.append(("create", kwargs))

            def get_mapping(self, **kwargs):
                raise AssertionError("legacy mappings must not be mutated in place")

            def get_alias(self, **kwargs):
                return {"l1_catalog_entries_v1": {"aliases": {kwargs["name"]: {}}}}

            def update_aliases(self, **kwargs):
                calls.append(("update_aliases", kwargs))

            def refresh(self, **kwargs):
                calls.append(("refresh", kwargs))

        class FakeCluster:
            def health(self, **kwargs):
                calls.append(("health", kwargs))
                return {"status": "yellow", "timed_out": False}

        class FakeClient:
            def __init__(self):
                self.indices = FakeIndices()
                self.cluster = FakeCluster()
                self.tasks = self

            def reindex(self, **kwargs):
                calls.append(("reindex", kwargs))
                return {"task": "node:12"}

            def get(self, **kwargs):
                calls.append(("task_get", kwargs))
                state["target_count"] = 12
                return {"completed": True, "response": {"created": 12, "updated": 0, "failures": []}}

            def count(self, **kwargs):
                return {"count": 12 if kwargs["index"] == "l1_catalog_entries_v1" else state["target_count"]}

        item = load_publish_plan(Path("data/normalized/mit"), "mit")["catalog_entries"]
        _ensure_index_and_alias(FakeClient(), item)

        self.assertEqual(item["write_index"], "l1_catalog_entries_v2")
        self.assertEqual(
            [name for name, _ in calls],
            ["create", "health", "reindex", "task_get", "refresh", "update_aliases"],
        )
        reindex = calls[2][1]
        self.assertEqual(reindex["body"]["source"]["index"], ["l1_catalog_entries_v1"])
        self.assertEqual(reindex["body"]["dest"]["index"], "l1_catalog_entries_v2")
        self.assertFalse(reindex["wait_for_completion"])
        actions = calls[5][1]["body"]["actions"]
        self.assertEqual(actions, [
            {"remove": {"index": "l1_catalog_entries_v1", "alias": "l1_catalog_entries_current"}},
            {"add": {"index": "l1_catalog_entries_v2", "alias": "l1_catalog_entries_current"}},
        ])

    def test_schema_upgrade_keeps_legacy_alias_when_reindex_count_mismatches(self) -> None:
        class FakeIndices:
            def exists(self, **kwargs):
                return False

            def create(self, **kwargs):
                return None

            def get_alias(self, **kwargs):
                return {"l1_catalog_entries_v1": {}}

            def update_aliases(self, **kwargs):
                raise AssertionError("alias must not move when migration validation fails")

            def refresh(self, **kwargs):
                return None

        class FakeCluster:
            def health(self, **kwargs):
                return {"status": "yellow", "timed_out": False}

        class FakeClient:
            def __init__(self):
                self.indices = FakeIndices()
                self.cluster = FakeCluster()
                self.tasks = self

            def reindex(self, **kwargs):
                return {"task": "node:11"}

            def get(self, **kwargs):
                return {"completed": True, "response": {"created": 11, "updated": 0, "failures": []}}

            def count(self, **kwargs):
                return {"count": 12 if kwargs["index"] == "l1_catalog_entries_v1" else 11}

        item = load_publish_plan(Path("data/normalized/mit"), "mit")["catalog_entries"]
        with self.assertRaisesRegex(RuntimeError, "schema migration count mismatch"):
            _ensure_index_and_alias(FakeClient(), item)

    def test_completed_schema_reindex_resumes_at_alias_switch_without_reindex(self) -> None:
        alias_updates: list[dict] = []

        class FakeIndices:
            def exists(self, **kwargs):
                return True

            def get_mapping(self, **kwargs):
                return {kwargs["index"]: {"mappings": {"_meta": {"edumeta_schema_version": "2"}}}}

            def get_alias(self, **kwargs):
                return {"l1_catalog_entries_v1": {}}

            def update_aliases(self, **kwargs):
                alias_updates.append(kwargs)

        class FakeClient:
            def __init__(self):
                self.indices = FakeIndices()

            def count(self, **kwargs):
                return {"count": 100732}

            def reindex(self, **kwargs):
                raise AssertionError("a complete destination must not be reindexed again")

        item = load_publish_plan(Path("data/normalized/mit"), "mit")["catalog_entries"]
        _ensure_index_and_alias(FakeClient(), item)

        self.assertEqual(len(alias_updates), 1)
        self.assertEqual(alias_updates[0]["body"]["actions"][-1], {
            "add": {"index": "l1_catalog_entries_v2", "alias": "l1_catalog_entries_current"}
        })

    def test_post_index_audit_rejects_wrong_top_catalog_match(self) -> None:
        class FakeClient:
            def search(self, **kwargs):
                return {
                    "hits": {
                        "hits": [{"_source": {"entry_id": "ent_wrong", "program_name": "Wrong Program"}}]
                    }
                }

        report = audit_staged_school(
            Path("data/normalized/mit"),
            "mit",
            "http://unused",
            client=FakeClient(),
            max_probes=1,
        )

        self.assertEqual(report["audit_status"], "failed")
        self.assertIn("retrieval_regression", report["failures"])

    def test_staging_publish_does_not_deactivate_current_documents(self) -> None:
        class FakeIndices:
            def __init__(self):
                self.refresh_calls = []

            def exists(self, **kwargs):
                return True

            def create(self, **kwargs):
                return None

            def get_mapping(self, **kwargs):
                index = kwargs["index"]
                return {index: {"mappings": {"_meta": {"edumeta_schema_version": "2"}}}}

            def get_alias(self, **kwargs):
                index = kwargs["name"].removesuffix("_current") + "_v2"
                return {index: {}}

            def put_alias(self, **kwargs):
                return None

            def refresh(self, **kwargs):
                self.refresh_calls.append(kwargs)
                return None

        class FakeClient:
            def __init__(self):
                self.indices = FakeIndices()
                self.update_calls = []

            def update_by_query(self, **kwargs):
                self.update_calls.append(kwargs)

            def delete_by_query(self, **kwargs):
                return None

            def count(self, **kwargs):
                version = next(
                    clause["term"]["dataset_version"]
                    for clause in kwargs["body"]["query"]["bool"]["filter"]
                    if "dataset_version" in clause.get("term", {})
                )
                plan = load_publish_plan(Path("data/normalized/mit"), "mit")
                return {"count": next(item["count"] for item in plan.values() if item["dataset_version"] == version and item["alias"] == kwargs["index"])}

        fake = FakeClient()

        publish_school(
            Path("data/normalized/mit"),
            "mit",
            "http://unused",
            activate=False,
            client=fake,
            bulk_writer=lambda client, actions: (len(list(actions)), []),
        )

        self.assertEqual(fake.update_calls, [])
        self.assertEqual(len(fake.indices.refresh_calls), 1)
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
        self.assertEqual(report["indexes"]["catalog_entries"]["write_index"], "l1_catalog_entries_v2")
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
