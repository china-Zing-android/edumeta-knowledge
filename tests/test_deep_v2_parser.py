from __future__ import annotations

import unittest
import tempfile
from pathlib import Path

from catalog_parser.deep_v2_parser import _clean_url, parse_deep_v2_markdown


ROOT = Path("docs/测试文件/院校明细")


class DeepV2ParserTests(unittest.TestCase):
    def parse_text(self, text: str):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "school.md"
            path.write_text(text, encoding="utf-8")
            return parse_deep_v2_markdown("example", path)

    def test_clean_url_prefers_complete_url_before_relative_path(self) -> None:
        self.assertEqual(
            _clean_url(
                "https://gsas.harvard.edu/program/computer-science",
                "https://www.harvard.edu/about",
            ),
            "https://gsas.harvard.edu/program/computer-science",
        )

    def test_clean_url_does_not_treat_degree_abbreviation_as_domain(self) -> None:
        self.assertIsNone(_clean_url("B.Com. (Honours)", "https://www.mcgill.ca/about"))

    def test_evidence_rows_cannot_be_reinterpreted_as_program_table_headers(self) -> None:
        result = self.parse_text(
            """# Example University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://www.example.edu/about

## Undergraduate programs
| Program | Degree | URL |
| --- | --- | --- |
| Computer Science | BS | https://www.example.edu/programs/computer-science |

## Evidence registry
| Evidence ID | Data key | Value | URL |
| --- | --- | --- | --- |
| E-001 | computing.programs | List of programs | https://www.example.edu/computing |
| E-002 | degrees.taxonomy | Degree levels offered | composite |
"""
        )

        self.assertEqual([row["program_name"] for row in result.catalog_entries], ["Computer Science"])

    def test_summary_and_policy_tables_do_not_generate_catalog_entries(self) -> None:
        result = self.parse_text(
            """# Example University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://www.example.edu/about

## Undergraduate programs
| Program Name | Degree Type | URL |
| --- | --- | --- |
| Economics | BA | https://www.example.edu/programs/economics-ba |

## Admission categories
| Admission Category | Description | Typical future program directions |
| --- | --- | --- |
| Humanities | Broad entry category | Multiple |
| Sciences | Broad entry category | degrees.taxonomy |
"""
        )

        self.assertEqual([row["program_name"] for row in result.catalog_entries], ["Economics"])

    def test_program_labeled_fact_table_does_not_generate_catalog_entries(self) -> None:
        result = self.parse_text(
            """# Example University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://www.example.edu/about

| Program | Degree | URL |
| --- | --- | --- |
| Economics | BA | https://www.example.edu/programs/economics |

## Application policy
| 项目 | 内容 |
| --- | --- |
| 申请材料 | Transcript and recommendations |
| 申请费用 | 100 USD |
"""
        )

        self.assertEqual([row["program_name"] for row in result.catalog_entries], ["Economics"])

    def test_same_program_name_preserves_ba_bs_and_minor_offerings(self) -> None:
        result = self.parse_text(
            """# Example University Knowledge Base
> **Data capture date**: 2026-07-24
> Official website: https://catalog.example.edu

## Undergraduate majors & minors
### College of Arts and Sciences
#### BA/BS
| # | Program | URL |
| --- | --- | --- |
| 1 | Computer Science | https://catalog.example.edu/programs/computer-science-ba |
| 2 | Computer Science | https://catalog.example.edu/programs/computer-science-bs |

#### Minor
| # | Program | URL |
| --- | --- | --- |
| 1 | Computer Science | https://catalog.example.edu/programs/computer-science-minor |
"""
        )

        self.assertEqual(len(result.catalog_entries), 3)
        self.assertEqual(
            {(row["level"], row["degree_level"], row.get("degree_full_name")) for row in result.catalog_entries},
            {
                ("undergraduate", "SB", "BA"),
                ("undergraduate", "SB", "BS"),
                ("undergraduate", "Minor", "Minor"),
            },
        )
        self.assertEqual(len({row["entry_id"] for row in result.catalog_entries}), 3)

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
