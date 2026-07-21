Status: done

# Server Verification And Preparsed JSONL Handoff

## Goal

Provide server-side upload/retrieval verification steps and complete the MIT normalized JSONL package as a reference for pre-processing school Markdown before publication.

## Delivered

- Added `docs/operations/server-upload-and-retrieval-verification.md` with health, MIT L1, Caltech upload, status polling, L1/L2, MCP tunnel, and failure-diagnosis commands.
- Added persisted `data/normalized/mit/entity_contexts.jsonl`: one university context plus 157 program contexts.
- Added `data/normalized/mit/README.md` describing all five entity files, relationships, regeneration, and pre-processing boundaries.

## Decision

- Pre-generating and reviewing the five JSONL files is recommended for the 300 core schools.
- Pre-generated data must still pass schema, cross-reference, diff, staging, publication, and WeKnora gates.
- The current runtime upload endpoint accepts complete Markdown only. A normalized JSONL bundle upload endpoint is not yet implemented and must not be simulated by direct database writes.
- Runtime WeKnora statuses in `source_registry.jsonl` and `url_manifest.jsonl` must not be overwritten by fresh parser output.

## Verification

- MIT normalized counts: catalog 157, facts 241, sources 112, URL manifest 112, entity contexts 158.
- Schema, required fields, URL legality, cross references, and MIT reconciliation passed.
- PostgreSQL dry-run load returned `status=validated`.
- Focused parser/validation/PostgreSQL/OpenSearch tests: 31 passed, 7 skipped.
