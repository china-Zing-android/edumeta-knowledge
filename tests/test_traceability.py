from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from fast_router.traceability import TraceabilityIndex


class TraceabilityIndexTests(unittest.TestCase):
    def test_loads_mapping_for_a_current_dataset_version(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            path = root / "example" / "ing_1" / "normalized"
            path.mkdir(parents=True)
            mapping = {
                "mapping_id": "prov_1",
                "university_id": "example",
                "dataset_version": "example_v1",
                "jsonl": {"entity": "catalog_entries", "record_id": "ent_1"},
                "md": {"sha256": "abc", "line_start": 7, "line_end": 7, "section_path": "Catalog"},
                "verification": {"status": "verified", "version_match": True},
            }
            (path / "provenance.jsonl").write_text(json.dumps(mapping) + "\n", encoding="utf-8")

            found = TraceabilityIndex(root).lookup("example", "example_v1", "catalog_entries", "ent_1")

        self.assertIsNotNone(found)
        self.assertEqual(found["mapping_id"], "prov_1")
        self.assertEqual(found["md"]["line_start"], 7)

    def test_missing_old_artifact_returns_none(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            found = TraceabilityIndex(Path(temp_dir)).lookup("example", "example_v1", "catalog_entries", "ent_1")

        self.assertIsNone(found)


if __name__ == "__main__":
    unittest.main()
