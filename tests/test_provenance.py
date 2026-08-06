from __future__ import annotations

import hashlib
import unittest
from pathlib import Path

from catalog_parser.mit_parser import parse_mit_markdown
from catalog_parser.provenance import ProvenanceError, build_provenance, validate_provenance


ROOT = Path(__file__).resolve().parents[1]


class ProvenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.markdown = """# Example University

## Catalog Entries

| school | department | level | degree_level | program_name | source_url |
| --- | --- | --- | --- | --- | --- |
| School of Engineering | Computer Science | undergraduate | SB | Computer Science | https://example.edu/cs |

## Quick Facts

| fact_type | fact_key | raw_value | source_url | program_name |
| --- | --- | --- | --- | --- |
| deadline | application_deadline | December 1, 2026 | https://example.edu/admissions | Computer Science |
"""
        self.dataset = {
            "catalog_entries": [
                {
                    "entry_id": "ent_example_undergraduate_sb_computer_science",
                    "university_id": "example",
                    "school": "School of Engineering",
                    "department": "Computer Science",
                    "level": "undergraduate",
                    "degree_level": "SB",
                    "program_name": "Computer Science",
                    "canonical_program_name": "Computer Science",
                    "course_code": None,
                    "source_id": "src_example_example_edu_cs",
                    "source_url": "https://example.edu/cs",
                    "discipline_ids": ["computer_science"],
                    "discipline_labels": ["Computer Science"],
                    "dataset_version": "example_20260804_v1",
                }
            ],
            "quick_facts": [
                {
                    "fact_id": "fact_example_application_deadline",
                    "university_id": "example",
                    "fact_type": "deadline",
                    "fact_key": "application_deadline",
                    "raw_value": "December 1, 2026",
                    "source_id": "src_example_example_edu_admissions",
                    "source_url": "https://example.edu/admissions",
                    "normalized_value": {"date": "2026-12-01"},
                    "dataset_version": "example_20260804_v1",
                }
            ],
        }

    def test_maps_catalog_and_fact_records_to_markdown_rows(self) -> None:
        mappings = build_provenance(
            self.markdown,
            self.dataset,
            university_id="example",
            dataset_version="example_20260804_v1",
        )

        by_id = {item["jsonl"]["record_id"]: item for item in mappings}
        catalog = by_id["ent_example_undergraduate_sb_computer_science"]
        fact = by_id["fact_example_application_deadline"]

        self.assertEqual(catalog["jsonl"]["entity"], "catalog_entries")
        self.assertEqual(catalog["md"]["line_start"], 7)
        self.assertEqual(catalog["md"]["line_end"], 7)
        self.assertEqual(fact["md"]["line_start"], 13)
        self.assertEqual(catalog["md"]["sha256"], hashlib.sha256(self.markdown.encode()).hexdigest())
        self.assertEqual(catalog["verification"]["version_match"], True)

    def test_distinguishes_direct_and_derived_fields(self) -> None:
        mappings = build_provenance(
            self.markdown,
            self.dataset,
            university_id="example",
            dataset_version="example_20260804_v1",
        )
        fields = mappings[0]["fields"]

        self.assertEqual(fields["program_name"]["kind"], "direct")
        self.assertEqual(fields["source_url"]["kind"], "direct")
        self.assertEqual(fields["discipline_ids"]["kind"], "derived")
        self.assertIn("discipline_taxonomy", fields["discipline_ids"]["rule"])

    def test_validation_rejects_mapping_outside_markdown_snapshot(self) -> None:
        mappings = build_provenance(
            self.markdown,
            self.dataset,
            university_id="example",
            dataset_version="example_20260804_v1",
        )
        mappings[0]["md"]["line_start"] = 999

        with self.assertRaises(ProvenanceError):
            validate_provenance(mappings, self.markdown)

    def test_mit_catalog_and_facts_have_a_markdown_mapping(self) -> None:
        path = ROOT / "docs" / "MIT_知识库_完整深度数据_v2.md"
        result = parse_mit_markdown(path)
        mappings = build_provenance(
            path.read_text(encoding="utf-8"),
            {"catalog_entries": result.catalog_entries, "quick_facts": result.quick_facts},
            university_id="mit",
            dataset_version="mit_20260704_v2",
            source_path=str(path),
        )

        self.assertEqual(len(mappings), len(result.catalog_entries) + len(result.quick_facts))
        self.assertEqual(len({item["mapping_id"] for item in mappings}), len(mappings))
        self.assertEqual(sum(item["verification"]["status"] == "review_required" for item in mappings), 3)


if __name__ == "__main__":
    unittest.main()
