Status: testing

# OpenSearch Schema Migration Handoff

## Goal

Make OpenSearch mapping upgrades non-destructive and automatic so an existing index never receives an incompatible in-place field type change.

## Root Cause

- All physical indexes were permanently named `*_v1` even after mapping `_meta.edumeta_schema_version` advanced to `2`.
- `_ensure_index_and_alias` called `put_mapping` when the schema version changed.
- The server's legacy entity-context index dynamically mapped `attributes.course_code_system` as `text`; the current explicit mapping requires `keyword`.
- OpenSearch rejects an in-place `text -> keyword` change, so every university ingestion failed during the publishing stage.

## Decision

- Derive physical index names from the committed mapping schema version.
- On an alias schema upgrade, create the new physical index, reindex all legacy alias documents, verify counts, and atomically move the alias.
- Never delete Docker volumes or mutate incompatible mappings in place.
- Keep the migration generic for future mapping versions and all L1 entity indexes.

## Current Verification

- Five server failures share the exact same OpenSearch mapping exception.
- All five passed pre-publish parsing and quality audits; the failure is isolated to index publication.
- Failing regression test reproduced the fixed `*_v1` physical index naming and passed after the implementation.
- A real OpenSearch 2.15 exercise migrated `course_code_system` from a legacy `text` index to a new `keyword` index, retained the document, and moved the alias only after count verification.
- Local MIT full ingestion migrated all five L1 aliases from `*_v1` to `*_v2` and published 157 catalog entries, 241 facts, 112 sources, and 158 entity contexts with both quality audits passing.
- The local database currently contains only five current universities, so the 30-school/cross-school QA suite is not a valid local release result. The full suite must run on the server after 276-school re-ingestion.
