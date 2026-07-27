from __future__ import annotations

import unittest

from scripts.quarantine_unverified_universities import unverified_ids


class QualityReconciliationTests(unittest.TestCase):
    def test_only_non_passed_universities_are_quarantined(self) -> None:
        rows = [
            {"university_id": "good", "status": "passed"},
            {"university_id": "review", "status": "needs_review"},
            {"university_id": "bad", "status": "failed"},
        ]

        self.assertEqual(unverified_ids(rows), ["bad", "review"])


if __name__ == "__main__":
    unittest.main()
