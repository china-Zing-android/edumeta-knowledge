from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from catalog_parser.mit_parser import parse_mit_markdown


ROOT = Path(__file__).resolve().parents[1]
MIT_MD = ROOT / "docs" / "MIT_知识库_完整深度数据_v2.md"


class EntityContextTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = parse_mit_markdown(MIT_MD)
        cls.contexts = cls.result.entity_contexts

    def test_mit_has_one_university_context_and_one_context_per_catalog_entry(self) -> None:
        university_contexts = [row for row in self.contexts if row["entity_type"] == "university"]
        program_contexts = [row for row in self.contexts if row["entity_type"] == "program"]

        self.assertEqual(len(university_contexts), 1)
        self.assertEqual(len(program_contexts), 157)
        self.assertEqual(university_contexts[0]["entity_id"], "mit")

    def test_university_context_is_useful_without_claiming_rank_or_advantages(self) -> None:
        context = next(row for row in self.contexts if row["entity_type"] == "university")

        self.assertGreaterEqual(len(context["sample_children"]), 3)
        self.assertLessEqual(len(context["sample_children"]), 5)
        self.assertTrue(all(child["entity_type"] == "school" for child in context["sample_children"]))
        self.assertTrue(all(child.get("sample_departments") for child in context["sample_children"]))
        sampled_schools = {child["title"] for child in context["sample_children"]}
        self.assertIn("School of Engineering", sampled_schools)
        self.assertIn("School of Science", sampled_schools)
        self.assertIn("School of Humanities, Arts, and Social Sciences", sampled_schools)
        self.assertLessEqual(len(context["md_section_paths"]), 5)
        self.assertLessEqual(len(context["source_ids"]), 15)
        self.assertTrue(all(len(topic["source_ids"]) <= 5 for topic in context["available_topics"]))
        self.assertTrue(all(topic["source_count"] >= len(topic["source_ids"]) for topic in context["available_topics"]))
        self.assertTrue(any(item["topic"] == "tuition" and item["availability"] == "l1" for item in context["available_topics"]))
        labels = {item["label"] for item in context["highlights"]}
        highlights = {item["label"]: item["value"] for item in context["highlights"]}
        self.assertEqual(highlights["Undergraduate SB programs"], 55)
        self.assertEqual(highlights["Undergraduate minors"], 17)
        self.assertEqual(highlights["Graduate degree offerings"], 85)
        self.assertNotIn("Undergraduate catalog entries", labels)
        self.assertNotIn("School/group labels represented in the catalog", labels)
        self.assertNotIn("advantage", json.dumps(context, ensure_ascii=False).lower())
        self.assertNotIn("ranking", json.dumps(context, ensure_ascii=False).lower())

    def test_economics_context_explains_related_course_codes_with_names_and_relationships(self) -> None:
        context = next(
            row
            for row in self.contexts
            if row["entity_type"] == "program" and row["attributes"].get("course_code") == "14-1"
        )
        related_by_code = {
            row["attributes"].get("course_code"): row for row in context["related_entities"]
        }

        self.assertEqual(context["display_label"], "14-1 Economics")
        self.assertIn("14-2", related_by_code)
        self.assertIn("6-14", related_by_code)
        self.assertEqual(related_by_code["14-2"]["display_label"], "14-2 Mathematical Economics")
        self.assertEqual(
            related_by_code["14-2"]["relation_reason"],
            "Same university, department, study level, and degree level as 14-1 Economics.",
        )
        self.assertIn("Computer Science, Economics, and Data Science", related_by_code["6-14"]["display_label"])
        self.assertNotEqual(related_by_code["14-2"]["display_label"], "14-2")

    def test_graduate_program_labels_include_degree_to_avoid_ambiguous_duplicates(self) -> None:
        graduate_contexts = [
            row
            for row in self.contexts
            if row["entity_type"] == "program" and row["attributes"].get("level") == "graduate"
        ]

        self.assertTrue(all(row["attributes"]["degree_level"] in row["display_label"] for row in graduate_contexts))
        for context in graduate_contexts:
            labels = [row["display_label"] for row in context["related_entities"]]
            self.assertEqual(len(labels), len(set(labels)), context["display_label"])

    def test_entity_context_records_conform_to_schema(self) -> None:
        schema = json.loads((ROOT / "docs/schemas/entity_contexts.schema.json").read_text("utf-8"))
        validator = Draft202012Validator(schema)

        for row in self.contexts:
            errors = sorted(validator.iter_errors(row), key=lambda error: list(error.path))
            self.assertEqual([], [error.message for error in errors], row)

    def test_parse_result_writes_entity_context_jsonl(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            out_dir = Path(temp_dir)
            self.result.write_jsonl(out_dir)
            rows = [
                json.loads(line)
                for line in (out_dir / "entity_contexts.jsonl").read_text("utf-8").splitlines()
                if line.strip()
            ]

        self.assertEqual(rows, self.contexts)


if __name__ == "__main__":
    unittest.main()
