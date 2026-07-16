from __future__ import annotations

import unittest

from catalog_parser.disciplines import (
    classify_catalog_entry,
    enrich_catalog_entries,
    resolve_discipline_query,
)


class DisciplineTaxonomyTests(unittest.TestCase):
    def test_medical_query_expands_to_controlled_related_disciplines(self) -> None:
        resolved = resolve_discipline_query("医学专业的院校有哪些？")

        self.assertEqual(resolved.primary_id, "medicine")
        self.assertEqual(
            set(resolved.expanded_ids),
            {"medicine", "health_sciences", "biomedical_engineering"},
        )

    def test_catalog_classification_separates_medicine_from_general_biology(self) -> None:
        biomedical = classify_catalog_entry(
            {"program_name": "Biomedical Engineering", "department": "Engineering", "school": "Engineering", "topics": []}
        )
        health = classify_catalog_entry(
            {"program_name": "Health Sciences and Technology", "department": "Health Sciences", "school": "Science", "topics": []}
        )
        biology = classify_catalog_entry(
            {"program_name": "Biology", "department": "Biology", "school": "Science", "topics": []}
        )

        self.assertIn("biomedical_engineering", biomedical)
        self.assertIn("health_sciences", health)
        self.assertEqual(biology, ["biology"])

    def test_enrichment_adds_stable_ids_and_labels_to_every_entry(self) -> None:
        entries = [
            {"program_name": "Economics", "department": "Economics", "school": "Humanities", "topics": []},
            {"program_name": "Unclassified Studies", "department": "Other", "school": "Other", "topics": []},
        ]

        enrich_catalog_entries(entries)

        self.assertEqual(entries[0]["discipline_ids"], ["economics"])
        self.assertEqual(entries[0]["discipline_labels"], ["Economics"])
        self.assertEqual(entries[1]["discipline_ids"], ["other"])


if __name__ == "__main__":
    unittest.main()
