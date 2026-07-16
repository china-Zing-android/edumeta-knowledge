from __future__ import annotations

import hashlib
import json
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

from .disciplines import enrich_catalog_entries
from .entity_contexts import build_entity_contexts


# ---------------------------------------------------------------------------
# Entity specs.
#
# These describe the parsed JSONL datasets and are a stable contract consumed by
# validation.py and diff.py. They intentionally do NOT map 1:1 to the control-
# plane tables: url_manifest is folded into source_registry (Plan §3 removes the
# duplicate url_manifest table), and source_entry_links are derived from the
# entry_ids arrays carried in source_registry records.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class EntitySpec:
    name: str
    file_name: str
    table_name: str
    primary_key: str
    jsonb_columns: frozenset[str]
    required_columns: tuple[str, ...]


ENTITY_SPECS: tuple[EntitySpec, ...] = (
    EntitySpec(
        name="source_registry",
        file_name="source_registry.jsonl",
        table_name="source_registry",
        primary_key="source_id",
        jsonb_columns=frozenset({"topics", "entry_ids"}),
        required_columns=(
            "source_id",
            "university_id",
            "canonical_url",
            "url_type",
            "topics",
            "official_source",
            "priority",
            "crawl_status",
            "parser_status",
            "weknora_import_status",
            "status",
            "capture_date",
            "last_verified",
            "dataset_version",
        ),
    ),
    EntitySpec(
        name="catalog_entries",
        file_name="catalog_entries.jsonl",
        table_name="catalog_entries",
        primary_key="entry_id",
        jsonb_columns=frozenset({"aliases", "cross_school_names", "topics"}),
        required_columns=(
            "entry_id",
            "university_id",
            "school",
            "department",
            "level",
            "degree_level",
            "program_name",
            "discipline_ids",
            "discipline_labels",
            "source_id",
            "source_url",
            "topics",
            "search_text",
            "capture_date",
            "dataset_version",
            "status",
        ),
    ),
    EntitySpec(
        name="url_manifest",
        file_name="url_manifest.jsonl",
        table_name="source_registry",  # folded into source_registry (Plan §3)
        primary_key="url_id",
        jsonb_columns=frozenset({"entry_ids", "topics", "weknora_chunk_ids"}),
        required_columns=(
            "url_id",
            "source_id",
            "university_id",
            "source_url",
            "canonical_url",
            "url_type",
            "topics",
            "official_source",
            "priority",
            "weknora_chunk_ids",
            "import_status",
            "capture_date",
            "dataset_version",
            "status",
        ),
    ),
    EntitySpec(
        name="quick_facts",
        file_name="quick_facts.jsonl",
        table_name="fact_store",
        primary_key="fact_id",
        jsonb_columns=frozenset({"normalized_value", "evidence_ids", "weknora_chunk_ids"}),
        required_columns=(
            "fact_id",
            "university_id",
            "fact_type",
            "fact_key",
            "raw_value",
            "source_id",
            "source_url",
            "evidence_ids",
            "weknora_chunk_ids",
            "capture_date",
            "dataset_version",
            "confidence",
            "review_status",
            "conflict_status",
            "status",
        ),
    ),
    EntitySpec(
        name="entity_contexts",
        file_name="entity_contexts.jsonl",
        table_name="entity_contexts",
        primary_key="context_id",
        jsonb_columns=frozenset({
            "attributes", "highlights", "sample_children", "related_entities",
            "available_topics", "source_ids", "md_section_paths",
        }),
        required_columns=(
            "context_id",
            "entity_type",
            "entity_id",
            "university_id",
            "title",
            "display_label",
            "attributes",
            "highlights",
            "sample_children",
            "related_entities",
            "available_topics",
            "source_ids",
            "md_section_paths",
            "dataset_version",
            "status",
        ),
    ),
)

# The set of entity names that map to authoritative control-plane tables.
# url_manifest is intentionally excluded — it enriches source_registry, not a table.
TABLE_ENTITY_SPECS: tuple[EntitySpec, ...] = tuple(
    spec for spec in ENTITY_SPECS if spec.name != "url_manifest"
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number} is not valid JSON: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number} must be a JSON object")
            records.append(record)
    return records


def record_hash(record: dict[str, Any]) -> str:
    payload = json.dumps(record, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def load_dataset(data_dir: Path, university_id: str) -> dict[str, list[dict[str, Any]]]:
    """Read and validate the four parsed datasets for a university.

    url_manifest records are returned under the ``url_manifest`` key (consumed by
    diff/validation and folded into source_registry at publish time), so the
    return shape stays a stable contract for diff.py / validation.py.
    """
    dataset: dict[str, list[dict[str, Any]]] = {}
    context_spec = next(spec for spec in ENTITY_SPECS if spec.name == "entity_contexts")
    for spec in ENTITY_SPECS:
        if spec.name == "entity_contexts":
            continue
        path = data_dir / spec.file_name
        if not path.exists():
            raise FileNotFoundError(f"missing {spec.file_name} in {data_dir}")
        records = read_jsonl(path)
        if spec.name == "catalog_entries":
            enrich_catalog_entries(records)
        validate_records(spec, records, university_id)
        dataset[spec.name] = records
    context_path = data_dir / context_spec.file_name
    if context_path.exists():
        context_records = read_jsonl(context_path)
    else:
        catalog = dataset["catalog_entries"]
        dataset_version = str(catalog[0].get("dataset_version") if catalog else university_id)
        context_records = build_entity_contexts(
            university_id=university_id,
            university_name=(
                "Massachusetts Institute of Technology"
                if university_id == "mit"
                else university_id.replace("_", " ").title()
            ),
            country_code=None,
            region=None,
            catalog_entries=catalog,
            quick_facts=dataset["quick_facts"],
            source_registry=dataset["source_registry"],
            dataset_version=dataset_version,
        )
    validate_records(context_spec, context_records, university_id)
    dataset[context_spec.name] = context_records
    return dataset


def validate_records(spec: EntitySpec, records: list[dict[str, Any]], university_id: str) -> None:
    seen: set[str] = set()
    for index, record in enumerate(records, start=1):
        missing = [column for column in spec.required_columns if column not in record or record[column] is None]
        if missing:
            raise ValueError(f"{spec.file_name}:{index} missing required columns: {', '.join(missing)}")
        if record.get("university_id") != university_id:
            raise ValueError(
                f"{spec.file_name}:{index} university_id={record.get('university_id')!r}, expected {university_id!r}"
            )
        pk = record[spec.primary_key]
        if pk in seen:
            raise ValueError(f"{spec.file_name}:{index} duplicate {spec.primary_key}: {pk}")
        seen.add(pk)


def build_upsert_sql(table_name: str, primary_key: str, columns: list[str]) -> str:
    quoted_columns = ", ".join(columns)
    placeholders = ", ".join(["%s"] * len(columns))
    update_columns = [column for column in columns if column != primary_key]
    assignments = ", ".join(f"{column}=EXCLUDED.{column}" for column in update_columns)
    return (
        f"INSERT INTO {table_name} ({quoted_columns}) VALUES ({placeholders}) "
        f"ON CONFLICT ({primary_key}) DO UPDATE SET {assignments}, updated_at=now()"
    )


def dry_run_report(data_dir: Path, university_id: str) -> dict[str, Any]:
    dataset = load_dataset(data_dir, university_id)
    return {
        "mode": "dry_run",
        "university_id": university_id,
        "data_dir": str(data_dir),
        "counts": {name: len(records) for name, records in dataset.items()},
        "tables": {spec.name: spec.table_name for spec in ENTITY_SPECS},
        "status": "validated",
    }


# ---------------------------------------------------------------------------
# Versioning helpers (Plan §3 Version publication).
#
# Flow: create ingestion_run + staging records -> validate schemas/refs -> diff
# current -> transactionally write the new version WITHOUT changing
# current_version -> index OpenSearch -> verify counts -> switch current_version
# in one transaction -> refresh version map -> retain previous for rollback.
# ---------------------------------------------------------------------------

def _link_id(source_id: str, target_entity: str, target_id: str) -> str:
    raw = f"{source_id}|{target_entity}|{target_id}"
    return f"lnk_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:24]}"


def _discipline_link_id(entry_id: str, discipline_id: str) -> str:
    raw = f"{entry_id}|{discipline_id}"
    return f"dlnk_{hashlib.sha256(raw.encode('utf-8')).hexdigest()[:24]}"


def upsert_university(
    cursor: Any,
    *,
    university_id: str,
    school_tier: str,
    university_name: str | None = None,
    aliases: list[str] | None = None,
    country_code: str | None = None,
    region: str | None = None,
    status: str = "pending",
) -> None:
    name = university_name or university_id.replace("_", " ").title()
    normalized_aliases = sorted(set([university_id, university_id.upper(), name, *(aliases or [])]))
    cursor.execute(
        """
        INSERT INTO universities
          (university_id, university_name, aliases, country_code, region, school_tier, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (university_id) DO UPDATE SET
          university_name=COALESCE(NULLIF(EXCLUDED.university_name, ''), universities.university_name),
          aliases=EXCLUDED.aliases,
          country_code=COALESCE(EXCLUDED.country_code, universities.country_code),
          region=COALESCE(EXCLUDED.region, universities.region),
          school_tier=EXCLUDED.school_tier,
          status=CASE WHEN universities.status='active' AND EXCLUDED.status='pending'
                      THEN 'active' ELSE EXCLUDED.status END,
          updated_at=now()
        """,
        (university_id, name, Jsonb(normalized_aliases), country_code, region, school_tier, status),
    )


def _normalize_source_row(
    university_id: str,
    version_id: str,
    source: dict[str, Any],
    manifest: dict[str, Any] | None,
) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    """Merge a source_registry row with its (optional) url_manifest row and emit
    the canonical source_registry columns plus the derived source_entry_links."""
    manifest = manifest or {}
    topics = source.get("topics") or manifest.get("topics") or []
    entry_ids = source.get("entry_ids") or manifest.get("entry_ids") or []
    weknora_kb_id = manifest.get("weknora_collection_id") or source.get("weknora_knowledge_base_id")
    weknora_kid = manifest.get("weknora_knowledge_id") or source.get("weknora_knowledge_id")
    row = {
        "source_id": source["source_id"],
        "university_id": university_id,
        "version_id": version_id,
        "program_id": source.get("program_id"),
        "source_url": source.get("source_url") or source.get("canonical_url"),
        "canonical_url": source["canonical_url"],
        "url_type": source["url_type"],
        "topics": topics,
        "official_source": bool(source.get("official_source", manifest.get("official_source"))),
        "priority": int(source.get("priority", manifest.get("priority", 1)) or 1),
        "content_hash": source.get("content_hash") or manifest.get("content_hash"),
        "weknora_content_hash": source.get("weknora_content_hash") or manifest.get("content_hash"),
        "crawl_status": source.get("crawl_status", "success"),
        "parser_status": source.get("parser_status", "parsed"),
        "weknora_import_status": source.get("weknora_import_status") or manifest.get("import_status") or "pending",
        "weknora_knowledge_base_id": weknora_kb_id,
        "weknora_knowledge_id": weknora_kid,
        "weknora_document_id": manifest.get("weknora_document_id") or source.get("weknora_document_id"),
        "weknora_chunk_ids": manifest.get("weknora_chunk_ids") or source.get("weknora_chunk_ids") or [],
        "weknora_tag_ids": source.get("weknora_tag_ids") or [],
        "weknora_import_job_id": source.get("weknora_import_job_id") or manifest.get("weknora_import_job_id"),
        "status": source.get("status", manifest.get("status", "active")),
        "capture_date": source["capture_date"],
        "last_verified": source.get("last_verified", source["capture_date"]),
        "dataset_version": source["dataset_version"],
        "source_version": source.get("source_version"),
        "error_message": source.get("error_message"),
    }
    links = [
        {
            "link_id": _link_id(source["source_id"], "catalog_entry", entry_id),
            "source_id": source["source_id"],
            "target_entity": "catalog_entry",
            "target_id": entry_id,
            "university_id": university_id,
            "version_id": version_id,
            "topics": topics,
        }
        for entry_id in entry_ids
    ]
    return row, links


def stage_school_records(
    cursor: Any,
    *,
    run_id: str,
    university_id: str,
    version_id: str,
    dataset: dict[str, list[dict[str, Any]]],
) -> dict[str, int]:
    """Write validated staging records into ingestion_records (staging, not current).

    url_manifest rows are folded into source_registry staging rows and their
    entry_ids are projected into source_entry_links. Returns per-entity counts.
    """
    manifests_by_source = {row["source_id"]: row for row in dataset.get("url_manifest", [])}
    counts: dict[str, int] = {}
    link_rows: list[dict[str, Any]] = []
    discipline_rows: list[dict[str, Any]] = []

    # source_registry staging (merged with url_manifest), also persisted as records.
    source_rows: list[dict[str, Any]] = []
    for source in dataset.get("source_registry", []):
        row, links = _normalize_source_row(university_id, version_id, source, manifests_by_source.get(source["source_id"]))
        source_rows.append(row)
        link_rows.extend(links)

    for entry in dataset.get("catalog_entries", []):
        for discipline_id, label in zip(entry.get("discipline_ids") or ["other"], entry.get("discipline_labels") or ["Other"]):
            discipline_rows.append({
                "link_id": _discipline_link_id(entry["entry_id"], discipline_id),
                "university_id": university_id,
                "version_id": version_id,
                "entry_id": entry["entry_id"],
                "discipline_id": discipline_id,
                "discipline_label": label,
                "match_method": "rule",
                "confidence": 1.0,
            })

    entity_record_sets: dict[str, list[dict[str, Any]]] = {
        "source_registry": source_rows,
        "catalog_entries": dataset.get("catalog_entries", []),
        "fact_store": dataset.get("quick_facts", []),
        "source_entry_links": link_rows,
        "catalog_entry_disciplines": discipline_rows,
        "entity_contexts": dataset.get("entity_contexts", []),
    }
    for entity_name, records in entity_record_sets.items():
        pk_field = "link_id" if entity_name in {"source_entry_links", "catalog_entry_disciplines"} else {
            "source_registry": "source_id",
            "catalog_entries": "entry_id",
            "fact_store": "fact_id",
            "entity_contexts": "context_id",
        }[entity_name]
        for record in records:
            cursor.execute(
                """
                INSERT INTO ingestion_records
                  (run_id, entity_name, record_id, university_id, record_hash, record)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (run_id, entity_name, record_id)
                DO UPDATE SET record_hash=EXCLUDED.record_hash, record=EXCLUDED.record
                """,
                (
                    run_id,
                    entity_name,
                    record[pk_field],
                    university_id,
                    record_hash(record),
                    Jsonb(record),
                ),
            )
        counts[entity_name] = len(records)
    counts["url_manifest"] = len(dataset.get("url_manifest", []))  # informational
    return counts


# lazily imported to keep psycopg optional for non-PG callers
def Jsonb(value: Any) -> Any:
    from psycopg.types.json import Jsonb as _Jsonb

    return _Jsonb(value)


def publish_school_version(
    connection: Any,
    *,
    run_id: str,
    university_id: str,
    version_id: str,
    input_hash: str,
    activate: bool = True,
) -> dict[str, Any]:
    """Transactionally write the new authoritative version WITHOUT changing
    current_version, then switch current_version in a single transaction.

    Staging records for this run (written by stage_school_records) are promoted
    into the authoritative tables scoped by version_id, the previous current
    version is demoted to superseded, and the new version becomes current.
    On any failure the whole promotion is rolled back and the previous current
    version is preserved.
    """
    cursor = connection.cursor()
    report: dict[str, Any] = {
        "run_id": run_id,
        "university_id": university_id,
        "version_id": version_id,
        "promoted": {},
    }

    cursor.execute(
        "SELECT entity_name, record FROM ingestion_records WHERE run_id=%s", (run_id,)
    )
    by_entity: dict[str, list[dict[str, Any]]] = {}
    for entity_name, record in cursor.fetchall():
        by_entity.setdefault(entity_name, []).append(record)

    for source_row in by_entity.get("source_registry", []):
        cols = list(source_row.keys())
        placeholders = ", ".join(["%s"] * len(cols))
        cursor.execute(
            f"INSERT INTO source_registry ({', '.join(cols)}) VALUES ({placeholders}) "
            "ON CONFLICT (university_id, version_id, source_id) DO NOTHING",
            _bind_values(source_row, cols),
        )
    report["promoted"]["source_registry"] = len(by_entity.get("source_registry", []))

    for entry in by_entity.get("catalog_entries", []):
        _promote_catalog_entry(cursor, university_id, version_id, entry)
    report["promoted"]["catalog_entries"] = len(by_entity.get("catalog_entries", []))

    for relation in by_entity.get("catalog_entry_disciplines", []):
        cursor.execute(
            """
            INSERT INTO catalog_entry_disciplines
              (link_id, university_id, version_id, entry_id, discipline_id,
               discipline_label, match_method, confidence)
            VALUES (%(link_id)s, %(university_id)s, %(version_id)s, %(entry_id)s,
                    %(discipline_id)s, %(discipline_label)s, %(match_method)s, %(confidence)s)
            ON CONFLICT (university_id, version_id, entry_id, discipline_id)
            DO UPDATE SET discipline_label=EXCLUDED.discipline_label,
                          match_method=EXCLUDED.match_method,
                          confidence=EXCLUDED.confidence
            """,
            relation,
        )
    report["promoted"]["catalog_entry_disciplines"] = len(by_entity.get("catalog_entry_disciplines", []))

    for fact in by_entity.get("fact_store", []):
        _promote_fact(cursor, university_id, version_id, fact)
    report["promoted"]["fact_store"] = len(by_entity.get("fact_store", []))

    for context in by_entity.get("entity_contexts", []):
        _promote_entity_context(cursor, university_id, version_id, context)
    report["promoted"]["entity_contexts"] = len(by_entity.get("entity_contexts", []))

    for link in by_entity.get("source_entry_links", []):
        link = {**link, "topics": Jsonb(link.get("topics") or [])}
        cursor.execute(
            """
            INSERT INTO source_entry_links
              (link_id, source_id, target_entity, target_id, university_id, version_id, topics)
            VALUES (%(link_id)s, %(source_id)s, %(target_entity)s, %(target_id)s, %(university_id)s, %(version_id)s, %(topics)s)
            ON CONFLICT (university_id, version_id, source_id, target_entity, target_id)
            DO UPDATE SET topics=EXCLUDED.topics
            """,
            link,
        )
    report["promoted"]["source_entry_links"] = len(by_entity.get("source_entry_links", []))

    if activate:
        activate_school_version(cursor, university_id=university_id, version_id=version_id, run_id=run_id)
    return report


def activate_school_version(cursor: Any, *, university_id: str, version_id: str, run_id: str) -> None:
    """Atomically move the current-version pointer after external index verification."""
    cursor.execute(
        """
        UPDATE weknora_import_jobs
           SET status='superseded', next_attempt_at=NULL,
               finished_at=COALESCE(finished_at, now()),
               failure_reason='dataset_version_superseded', updated_at=now()
         WHERE university_id=%s AND version_id<>%s
           AND status IN ('queued', 'running')
        """,
        (university_id, version_id),
    )
    cursor.execute(
        """
        UPDATE school_versions
           SET publication_state='superseded', superseded_at=now()
         WHERE university_id=%s AND publication_state='current' AND version_id<>%s
        """,
        (university_id, version_id),
    )
    cursor.execute(
        """
        UPDATE school_versions
           SET publication_state='current', published_at=now(), superseded_at=NULL
         WHERE university_id=%s AND version_id=%s
        """,
        (university_id, version_id),
    )
    cursor.execute(
        "UPDATE ingestion_runs SET status='published', updated_at=now() WHERE run_id=%s",
        (run_id,),
    )
    cursor.execute(
        "UPDATE universities SET status='active', updated_at=now() WHERE university_id=%s",
        (university_id,),
    )


def _bind_values(record: dict[str, Any], cols: list[str]) -> tuple[Any, ...]:
    values = []
    for col in cols:
        value = record.get(col)
        if col in {"topics", "weknora_chunk_ids", "weknora_tag_ids"} and not isinstance(value, (str, bytes)):
            value = Jsonb(value if value is not None else [])
        values.append(value)
    return tuple(values)


def _promote_catalog_entry(cursor: Any, university_id: str, version_id: str, record: dict[str, Any]) -> None:
    cols = [
        "entry_id", "university_id", "version_id", "program_id", "school", "department",
        "level", "degree_level", "degree_full_name", "course_code", "program_name",
        "canonical_program_name", "aliases", "source_id", "source_url", "topics",
        "search_text", "cross_school", "cross_school_names", "raw_section_path",
        "capture_date", "dataset_version", "source_version", "status",
    ]
    row = {
        **record,
        "university_id": university_id,
        "version_id": version_id,
    }
    cursor.execute(
        """
        INSERT INTO catalog_entries
          (entry_id, university_id, version_id, program_id, school, department, level,
           degree_level, degree_full_name, course_code, program_name, canonical_program_name,
           aliases, source_id, source_url, topics, search_text, cross_school,
           cross_school_names, raw_section_path, capture_date, dataset_version,
           source_version, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (university_id, version_id, entry_id) DO UPDATE SET
           program_name=EXCLUDED.program_name, search_text=EXCLUDED.search_text,
           topics=EXCLUDED.topics, aliases=EXCLUDED.aliases, status=EXCLUDED.status,
           dataset_version=EXCLUDED.dataset_version,
           updated_at=now()
        """,
        (
            row["entry_id"], university_id, version_id, row.get("program_id"), row["school"],
            row["department"], row["level"], row["degree_level"], row.get("degree_full_name"),
            row.get("course_code"), row["program_name"], row.get("canonical_program_name"),
            Jsonb(row.get("aliases") or []), row["source_id"], row["source_url"],
            Jsonb(row.get("topics") or []), row["search_text"], row.get("cross_school", False),
            Jsonb(row.get("cross_school_names") or []), row.get("raw_section_path"),
            row["capture_date"], row["dataset_version"], row.get("source_version"),
            row.get("status", "active"),
        ),
    )


def _promote_fact(cursor: Any, university_id: str, version_id: str, record: dict[str, Any]) -> None:
    row = {**record, "university_id": university_id, "version_id": version_id}
    cursor.execute(
        """
        INSERT INTO fact_store
          (fact_id, university_id, version_id, program_id, entry_id, fact_type, fact_key,
           raw_value, normalized_value, unit, currency, admission_cycle, term, source_id,
           source_url, evidence_ids, capture_date, dataset_version, source_version,
           confidence, review_status, conflict_status, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (university_id, version_id, fact_id) DO UPDATE SET
           raw_value=EXCLUDED.raw_value, normalized_value=EXCLUDED.normalized_value,
           review_status=EXCLUDED.review_status, conflict_status=EXCLUDED.conflict_status,
           dataset_version=EXCLUDED.dataset_version,
           updated_at=now()
        """,
        (
            row["fact_id"], university_id, version_id, row.get("program_id"), row.get("entry_id"),
            row["fact_type"], row["fact_key"], row["raw_value"], Jsonb(row.get("normalized_value")),
            row.get("unit"), row.get("currency"), row.get("admission_cycle"), row.get("term"),
            row["source_id"], row["source_url"], Jsonb(row.get("evidence_ids") or []),
            row["capture_date"], row["dataset_version"], row.get("source_version"),
            row.get("confidence", 1), row["review_status"], row["conflict_status"],
            row.get("status", "active"),
        ),
    )


def _promote_entity_context(cursor: Any, university_id: str, version_id: str, record: dict[str, Any]) -> None:
    row = {**record, "university_id": university_id, "version_id": version_id}
    cursor.execute(
        """
        INSERT INTO entity_contexts
          (context_id, university_id, version_id, entity_type, entity_id, entry_id,
           title, display_label, attributes, highlights, sample_children,
           related_entities, available_topics, source_ids, md_section_paths,
           dataset_version, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (university_id, version_id, context_id) DO UPDATE SET
          title=EXCLUDED.title, display_label=EXCLUDED.display_label,
          attributes=EXCLUDED.attributes, highlights=EXCLUDED.highlights,
          sample_children=EXCLUDED.sample_children,
          related_entities=EXCLUDED.related_entities,
          available_topics=EXCLUDED.available_topics,
          source_ids=EXCLUDED.source_ids, md_section_paths=EXCLUDED.md_section_paths,
          dataset_version=EXCLUDED.dataset_version, status=EXCLUDED.status,
          updated_at=now()
        """,
        (
            row["context_id"], university_id, version_id, row["entity_type"], row["entity_id"],
            row.get("entry_id"), row["title"], row["display_label"], Jsonb(row.get("attributes") or {}),
            Jsonb(row.get("highlights") or []), Jsonb(row.get("sample_children") or []),
            Jsonb(row.get("related_entities") or []), Jsonb(row.get("available_topics") or []),
            Jsonb(row.get("source_ids") or []), Jsonb(row.get("md_section_paths") or []),
            row["dataset_version"], row.get("status", "active"),
        ),
    )


def rollback_school_version(connection: Any, *, university_id: str, to_version_id: str) -> dict[str, Any]:
    """Re-promote a superseded version to current. Used to recover a failed
    publication; the previous current version stays queryable because documents
    are version-scoped and never physically deleted on demotion."""
    cursor = connection.cursor()
    cursor.execute(
        """
        UPDATE school_versions
           SET publication_state='superseded', superseded_at=now()
         WHERE university_id=%s AND publication_state='current'
        """,
        (university_id,),
    )
    cursor.execute(
        """
        UPDATE school_versions
           SET publication_state='current', superseded_at=NULL
         WHERE university_id=%s AND version_id=%s
        """,
        (university_id, to_version_id),
    )
    return {"university_id": university_id, "current_version": to_version_id}


def current_version(connection: Any, university_id: str) -> str | None:
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT version_id FROM school_versions
         WHERE university_id=%s AND publication_state='current'
        """,
        (university_id,),
    )
    row = cursor.fetchone()
    return row[0] if row else None


def load_school_to_postgres(
    data_dir: Path,
    university_id: str,
    dsn: str,
    run_id: str | None = None,
    *,
    school_tier: str = "core",
    publish: bool = True,
) -> dict[str, Any]:
    """End-to-end load: validate -> stage -> (optionally) publish.

    Implements Plan §3 version publication:
    1. create ingestion_run + school_version (staging)
    2. validate schemas/refs (load_dataset)
    3. stage records into ingestion_records
    4. when publish=True, promote to authoritative tables + switch current_version
       in a single transaction; on failure the previous current is preserved.
    """
    dataset = load_dataset(data_dir, university_id)
    run_id = run_id or f"ing_{uuid.uuid4().hex}"
    input_hash = _dataset_input_hash(dataset)
    version_id = f"ver_{university_id}_{input_hash[:16]}"

    try:
        import psycopg
    except ImportError as exc:
        raise RuntimeError("psycopg is required for Postgres loading. Install project dependencies first.") from exc

    with psycopg.connect(dsn) as connection:
        with connection.transaction():
            cursor = connection.cursor()
            upsert_university(
                cursor,
                university_id=university_id,
                school_tier=school_tier,
                status="pending",
            )
            cursor.execute(
                """
                INSERT INTO school_versions (version_id, university_id, dataset_version,
                                             publication_state, input_hash, record_counts)
                VALUES (%s, %s, %s, 'staging', %s, %s)
                ON CONFLICT (university_id, version_id) DO UPDATE SET input_hash=EXCLUDED.input_hash
                """,
                (
                    version_id,
                    university_id,
                    dataset.get("source_registry", [{}])[0].get("dataset_version", version_id),
                    input_hash,
                    Jsonb({name: len(rows) for name, rows in dataset.items()}),
                ),
            )
            cursor.execute(
                """
                INSERT INTO ingestion_runs (run_id, university_id, school_tier, version_id,
                                            input_hash, status)
                VALUES (%s, %s, %s, %s, %s, 'validating')
                ON CONFLICT (run_id) DO UPDATE SET status=EXCLUDED.status, updated_at=now()
                """,
                (run_id, university_id, school_tier, version_id, input_hash),
            )
            counts = stage_school_records(
                cursor,
                run_id=run_id,
                university_id=university_id,
                version_id=version_id,
                dataset=dataset,
            )
            cursor.execute(
                "UPDATE ingestion_runs SET status=%s, updated_at=now() WHERE run_id=%s",
                ("publishing" if publish else "accepted", run_id),
            )
            if publish:
                publish_school_version(
                    connection,
                    run_id=run_id,
                    university_id=university_id,
                    version_id=version_id,
                    input_hash=input_hash,
                )

    return {
        "mode": "postgres",
        "run_id": run_id,
        "university_id": university_id,
        "version_id": version_id,
        "input_hash": input_hash,
        "data_dir": str(data_dir),
        "counts": counts,
        "status": "published" if publish else "staged",
    }


def _dataset_input_hash(dataset: dict[str, list[dict[str, Any]]]) -> str:
    """Deterministic hash of the whole dataset for unchanged-input detection."""
    hasher = hashlib.sha256()
    for spec in ENTITY_SPECS:
        records = dataset.get(spec.name, [])
        hasher.update(spec.name.encode("utf-8"))
        hasher.update(str(len(records)).encode("utf-8"))
        for record in records:
            hasher.update(record_hash(record).encode("utf-8"))
    return hasher.hexdigest()
