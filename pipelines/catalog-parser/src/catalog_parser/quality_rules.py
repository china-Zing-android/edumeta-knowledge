from __future__ import annotations

import re
from typing import Any


QUALITY_RULESET_VERSION = "2026-07-27.1"

QUALITY_RULES: dict[str, dict[str, str]] = {
    "CAT-ENTITY-001": {"category": "entity_validity", "description": "Reject summary, taxonomy, URL, numeric, and policy values as catalog entities."},
    "CAT-URL-001": {"category": "url_integrity", "description": "Reject malformed or double-domain source URLs."},
    "CAT-DEGREE-001": {"category": "degree_consistency", "description": "Reject incompatible degree, level, and source URL combinations."},
    "CAT-COVERAGE-001": {"category": "catalog_completeness", "description": "Compare parsed records with explicit complete-catalog declarations."},
    "CAT-SOURCE-001": {"category": "source_specificity", "description": "Review catalogs whose entries mostly share one generic source URL."},
    "RET-SCOPE-001": {"category": "retrieval_regression", "description": "Require exact positive, degree-scoped, and negative retrieval probes before activation."},
}

INVALID_PROGRAM_NAMES = {
    "n/a", "none", "total", "合计", "多种", "multiple", "various", "degrees.taxonomy",
    "computing.programs", "not applicable", "tbd", "unknown",
}


def program_name_issue(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return "empty_name"
    normalized = value.strip()
    lowered = normalized.lower()
    if lowered in INVALID_PROGRAM_NAMES:
        return "reserved_or_summary_value"
    if len(normalized) > 180:
        return "name_too_long"
    if re.fullmatch(r"[\d\W_]+", normalized):
        return "numeric_or_punctuation_only"
    if re.fullmatch(r"[a-z][a-z0-9_-]*(?:\.[a-z0-9_-]+)+", lowered):
        return "machine_taxonomy_key"
    if re.fullmatch(r"https?://\S+", normalized, re.IGNORECASE):
        return "url_used_as_name"
    return None
