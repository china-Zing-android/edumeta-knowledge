Status: done

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

## Server Follow-up Root Cause

- The first migration implementation created `l1_universities_v2` and `l1_catalog_entries_v2` successfully.
- Server counts prove both destinations exactly match their `v1` sources: universities `355`, catalog entries `100732`.
- The synchronous OpenSearch `_reindex` response emitted more than 100 HTTP headers; Python `http.client` rejected the response after the server had already completed the copy.
- Because the client raised before alias activation, universities switched to `v2`, catalog stayed on `v1`, and later indexes were never attempted.
- The durable correction is resumable async reindex: pre-count, skip an already complete copy, otherwise submit an async task, wait through the tasks API, verify exact counts, then atomically switch the alias.

## Async Migration Verification

- Regression test proves a destination with matching source count skips `_reindex` and resumes directly at the alias switch.
- Migration tests use async task submission and refuse alias activation on a final count mismatch.
- Real OpenSearch 2.15 test asynchronously migrated 250 documents from a `text` index to a `keyword` index.
- The same real test moved the alias back to the legacy index while retaining the complete destination; rerunning migration detected matching counts and restored the alias without another reindex.
- Server verification on 2026-07-28: MIT run `ing_da403af4ee264ccab11e809926fdff28` reached `published` in 10.2 seconds with no failures.
- All five production aliases now point exclusively to their `*_v2` physical indexes: universities, catalog entries, quick facts, sources, and entity contexts.
- Server 30-question suite passed 5 runs with no failures or nondeterminism: L1 p95 `89.02 ms`, upward p95 `51.172 ms`, range p95 `24.172 ms`.
