# Markdown–JSONL Traceability Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make every published catalog/fact result traceable from JSONL back to the exact Markdown snapshot, line range, field origin, and verification state.

**Architecture:** Keep the existing JSONL schemas and OpenSearch documents compact. Generate a separate `provenance.jsonl` sidecar per ingestion run, keyed by entity and record ID, containing the Markdown snapshot hash, line range, section path, direct/derived field mapping, and deterministic verification checks. The retrieval response exposes a lightweight `traceability` summary; the admin UI loads the sidecar and shows the JSONL record beside highlighted Markdown lines.

**Tech Stack:** Python parser/FastAPI ingestion, PostgreSQL/OpenSearch version metadata, React/Vite/Carbon admin UI, pytest, TypeScript typecheck/build.

---

### Task 1: Define the provenance contract and parser-side tests

**Files:**
- Create: `pipelines/catalog-parser/src/catalog_parser/provenance.py`
- Create: `tests/test_provenance.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/mit_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/deep_v2_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/structured_markdown_parser.py`

**Steps:**

1. Add failing tests for a catalog row and quick fact row that require `record_id`, `md_snapshot.sha256`, `line_start`, `line_end`, and field mappings.
2. Add a test that rejects a provenance record whose line range is outside the Markdown snapshot.
3. Add a test that marks taxonomy fields as `derived` and source values as `direct`.
4. Implement a small provenance builder using parser row metadata, preserving existing record schemas.
5. Run `pytest tests/test_provenance.py -q` and keep the scope limited to the new contract.

### Task 2: Generate and retain `provenance.jsonl`

**Files:**
- Modify: `pipelines/catalog-parser/src/catalog_parser/mit_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/deep_v2_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/structured_markdown_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/validation.py`
- Modify: `apps/fast-router/src/fast_router/ingestion.py`
- Modify: `apps/fast-router/src/fast_router/admin.py`
- Modify: `tests/test_parser_contracts.py`
- Modify: `tests/test_ingestion_quality_gate.py`

**Steps:**

1. Add row start/end and table header metadata at parser boundaries for catalog and fact records.
2. Compute the Markdown SHA-256 from the exact stored `input.md` snapshot.
3. Write `provenance.jsonl` after parser output and before publication; preserve it through WeKnora enrichment.
4. Add provenance coverage checks: every catalog/fact record maps to the same snapshot, every range is valid, and direct values can be read from the mapped row.
5. Add `provenance` to the downloadable artifact list and ZIP bundle without changing the five business JSONL contracts.
6. Run parser, validation, and focused ingestion tests.

### Task 3: Expose traceability in retrieval

**Files:**
- Create: `apps/fast-router/src/fast_router/traceability.py`
- Modify: `apps/fast-router/src/fast_router/retrieval.py`
- Modify: `apps/fast-router/src/fast_router/main.py`
- Modify: `tests/test_fast_router_api.py`

**Steps:**

1. Add failing API tests requiring a discovery/fact match to include a compact traceability summary when the current version has a mapping.
2. Decorate L1 matches using the stable `university_id`, `dataset_version`, and record ID; do not call WeKnora for this lookup.
3. Return `traceability.status` as `verified`, `unavailable`, or `version_mismatch` with the mapping ID, entity, record ID, and Markdown line range.
4. Keep WeKnora evidence explicitly separate as external evidence; do not label it as MD-derived.
5. Run the focused Fast Router API tests.

### Task 4: Add side-by-side admin inspection

**Files:**
- Modify: `apps/md-admin/src/api.ts`
- Modify: `apps/md-admin/src/App.tsx`
- Modify: `apps/md-admin/src/styles.css`

**Steps:**

1. Add typed provenance records and an API fetcher for a run's mapping by entity/record ID.
2. Add a “来源映射” action in the JSONL viewer.
3. Show the JSONL record, field origin labels, verification badges, and the exact Markdown line range with highlighted lines.
4. Show direct, derived, and system-generated fields distinctly in plain Chinese.
5. Keep the existing paginated artifact viewer as the fallback when no provenance is available.
6. Run `npm run typecheck` and `npm run build` in `apps/md-admin`.

### Task 5: Final verification and handoff

**Files:**
- Modify: `docs/work/md-jsonl-traceability-handoff.md`

**Steps:**

1. Run the new focused parser/API tests, existing relevant tests, frontend checks, and `git diff --check`.
2. Inspect the diff stat and confirm unrelated dirty files were not changed by this task.
3. Record exact verification results, known limitations, and deployment follow-up in the handoff.
