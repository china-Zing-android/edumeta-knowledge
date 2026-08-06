"""Runtime lookup and compact summaries for Markdown provenance sidecars."""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any


class TraceabilityIndex:
    """Read per-run provenance sidecars without adding a database table.

    The ingestion pipeline keeps immutable run artifacts under one university
    directory.  Retrieval only needs the current version's small mapping, so
    the index lazily scans and caches the newest sidecar for each university.
    """

    def __init__(self, raw_root: Path | None) -> None:
        self.raw_root = raw_root.resolve() if raw_root else None
        self._cache: dict[str, tuple[tuple[tuple[str, int], ...], dict[tuple[str, str, str], dict[str, Any]]]] = {}
        self._lock = threading.Lock()

    def _sidecars(self, university_id: str) -> list[Path]:
        if not self.raw_root:
            return []
        university_root = self.raw_root / university_id
        if not university_root.is_dir():
            return []
        return sorted(
            (
                path
                for path in university_root.glob("*/normalized/provenance.jsonl")
                if path.is_file()
            ),
            key=lambda path: path.stat().st_mtime_ns,
            reverse=True,
        )

    def _load(self, university_id: str) -> dict[tuple[str, str, str], dict[str, Any]]:
        sidecars = self._sidecars(university_id)
        signature = tuple((str(path), path.stat().st_mtime_ns) for path in sidecars)
        cached = self._cache.get(university_id)
        if cached and cached[0] == signature:
            return cached[1]

        records: dict[tuple[str, str, str], dict[str, Any]] = {}
        for path in sidecars:
            try:
                rows = [
                    json.loads(line)
                    for line in path.read_text(encoding="utf-8").splitlines()
                    if line.strip()
                ]
            except (OSError, json.JSONDecodeError):
                continue
            for row in rows:
                identity = row.get("jsonl") or {}
                key = (
                    str(row.get("dataset_version") or ""),
                    str(identity.get("entity") or ""),
                    str(identity.get("record_id") or ""),
                )
                if all(key):
                    records.setdefault(key, row)
        self._cache[university_id] = (signature, records)
        return records

    def lookup(
        self,
        university_id: str,
        dataset_version: str | None,
        entity: str,
        record_id: str,
    ) -> dict[str, Any] | None:
        with self._lock:
            return self._load(university_id).get((str(dataset_version or ""), entity, record_id))


def traceability_summary(
    row: dict[str, Any],
    *,
    university_id: str | None,
    dataset_version: str | None,
    resolver: Any | None,
) -> dict[str, Any]:
    """Return a safe, small payload suitable for a retrieval result card."""

    entity = "catalog_entries" if row.get("entry_id") else "quick_facts" if row.get("fact_id") else None
    record_id = row.get("entry_id") or row.get("fact_id")
    effective_university = university_id or row.get("university_id")
    effective_version = dataset_version or row.get("dataset_version")
    base = {
        "status": "unavailable",
        "source": "markdown",
        "entity": entity,
        "record_id": record_id,
        "dataset_version": effective_version,
        "reason": "provenance_not_available",
    }
    if not resolver or not entity or not record_id or not effective_university:
        return base
    mapping = resolver.lookup(effective_university, effective_version, entity, str(record_id))
    if not mapping:
        return base
    verification = mapping.get("verification") or {}
    md = mapping.get("md") or {}
    status = str(verification.get("status") or "review_required")
    return {
        "status": status,
        "source": "markdown",
        "mapping_id": mapping.get("mapping_id"),
        "entity": entity,
        "record_id": record_id,
        "dataset_version": mapping.get("dataset_version") or effective_version,
        "md": {
            "file": md.get("file"),
            "sha256": md.get("sha256"),
            "line_start": md.get("line_start"),
            "line_end": md.get("line_end"),
            "section_path": md.get("section_path"),
        },
        "verification": {
            "version_match": verification.get("version_match") is True,
            "line_match": verification.get("line_match") is True,
            "all_fields_mapped": verification.get("all_fields_mapped") is True,
        },
        "reason": None if status == "verified" else "mapping_requires_review",
    }
