Status: done

# L1 + WeKnora Retrieval Handoff

## Goal

Replace the previous L0/L1/L2 Agent-platform direction with a focused L1 + WeKnora retrieval submodule that supports precise sub-second L1 HTTP/MCP retrieval and incremental Markdown-to-PostgreSQL/OpenSearch/WeKnora ingestion.

## Current Decision

- Active implementation plan: `docs/plans/2026-07-15-l1-weknora-retrieval-correction.md`.
- Keep PostgreSQL as the data control plane, OpenSearch as the L1 query store, external WeKnora as scoped evidence, FastAPI as the HTTP service, and a thin TypeScript MCP Gateway.
- Remove L0, Redis, MinIO, Langfuse, NestJS, mock evidence, runtime JSONL retrieval, per-school indexes, and Agent/report workflows.
- Validate MIT first, then verify incremental updates for several universities.

## Delivered

- MIT end-to-end ingestion and retrieval: 157 catalog entries, 241 facts, 112 current canonical sources.
- PostgreSQL version control, global OpenSearch aliases, current-version in-memory map, real WeKnora import/search, FastAPI retrieval/ingestion, and one-tool TypeScript MCP Gateway.
- Old JSONL mock WeKnora sync CLI and legacy `/mcp-sdk` smoke/consistency scripts removed.
- Version activation marks old queued/running WeKnora jobs `superseded`; the worker only claims jobs from current school versions.
- Human QA remains user-operated and is intentionally outside the automated release gate.

## Verified Technical Check

Authenticated WeKnora testing verified server-side `knowledge_ids` scope. Sending `knowledge_ids` and `tag_ids` together returns empty results on the current service, so runtime search uses exact knowledge IDs; university tags remain import-governance metadata.

## Verification

- Python: `113 passed, 6 skipped`; PostgreSQL integration: `10 passed`.
- TypeScript Gateway: `7 passed`.
- Retrieval acceptance: 30 cases x 5 runs, no failures or nondeterministic cases; HTTP L1 p95 `37.335ms`, L1+WeKnora p95 `713.887ms`.
- MCP benchmark: 50 calls, p95 `31.384ms`.
- Runtime Compose: PostgreSQL, OpenSearch, Fast Router, and MCP Gateway healthy; current MIT WeKnora jobs `112 success`.
- Incremental report: one URL change created exactly one WeKnora job.
- MIT release gate: `4/4 passed` in `qa/reports/release-gate-2026-07-15.json`.

## Residual Risk

During one acceptance attempt, WeKnora returned an isolated empty result for the Sloan MBA case. The same scoped query then passed 30 consecutive reproductions and the complete 30-case suite passed five consecutive runs. No request-time retry was added because the architecture explicitly forbids it; external evidence-service availability remains separately observable from L1 correctness.
