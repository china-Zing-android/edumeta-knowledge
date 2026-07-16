from __future__ import annotations

import unittest
from pathlib import Path

from catalog_parser.deep_v2_parser import parse_deep_v2_markdown


ROOT = Path("docs/测试文件/院校明细")


class DeepV2ParserTests(unittest.TestCase):
    def test_selected_v2_documents_produce_catalog_and_source_relationships(self) -> None:
        cases = {
            "asu": ("ASU_知识库_完整深度数据_v2.md", 1000, 1000),
            "harvard": ("Harvard_知识库_完整深度数据_v2.md", 150, 100),
            "caltech": ("Caltech_知识库_完整深度数据_v2.md", 70, 40),
            "duke": ("Duke_知识库_完整深度数据_v2.md", 200, 10),
        }

        for university_id, (filename, minimum_entries, minimum_sources) in cases.items():
            with self.subTest(university_id=university_id):
                result = parse_deep_v2_markdown(university_id, ROOT / filename)
                self.assertGreaterEqual(len(result.catalog_entries), minimum_entries)
                self.assertGreaterEqual(len(result.source_registry), minimum_sources)
                self.assertTrue(all(entry["source_id"] and entry["source_url"] for entry in result.catalog_entries))
                self.assertEqual(len({entry["entry_id"] for entry in result.catalog_entries}), len(result.catalog_entries))


if __name__ == "__main__":
    unittest.main()
