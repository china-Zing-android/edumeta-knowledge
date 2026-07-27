from __future__ import annotations

import unittest

from fast_router.ingestion import build_ingestion_input_hash, merge_university_metadata


class IngestionMetadataTests(unittest.TestCase):
    def test_request_metadata_is_part_of_ingestion_identity(self) -> None:
        content = b"# Stanford\n"

        california = build_ingestion_input_hash(content, {"country_code": "US", "region": "California"})
        unchanged = build_ingestion_input_hash(content, {"region": "California", "country_code": "US"})
        massachusetts = build_ingestion_input_hash(content, {"country_code": "US", "region": "Massachusetts"})

        self.assertEqual(california, unchanged)
        self.assertNotEqual(california, massachusetts)

    def test_pending_weknora_creation_uses_stable_ingestion_identity(self) -> None:
        content = b"# New University\n"
        first = build_ingestion_input_hash(
            content,
            {"country_code": "US", "weknora_knowledge_base_id": "create"},
        )
        retry = build_ingestion_input_hash(
            content,
            {"weknora_knowledge_base_id": "create", "country_code": "US"},
        )

        self.assertEqual(first, retry)

    def test_request_metadata_fills_and_overrides_parser_metadata(self) -> None:
        merged = merge_university_metadata(
            {
                "university_name": "Stanford",
                "country_code": None,
                "region": None,
                "aliases": ["Stanford University"],
            },
            {
                "university_name": "Stanford University",
                "country_code": "US",
                "region": "California",
                "aliases": ["Stanford", "SU"],
            },
        )

        self.assertEqual(merged["university_name"], "Stanford University")
        self.assertEqual(merged["country_code"], "US")
        self.assertEqual(merged["region"], "California")
        self.assertEqual(merged["aliases"], ["SU", "Stanford", "Stanford University"])


if __name__ == "__main__":
    unittest.main()
