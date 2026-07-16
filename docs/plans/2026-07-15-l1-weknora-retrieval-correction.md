# L1 + WeKnora Retrieval Correction Implementation Plan

**Implementation status (2026-07-15): MIT automated release scope completed.** The release report is `qa/reports/release-gate-2026-07-15.json`; human QA remains user-operated by explicit decision.

> **For Claude:** REQUIRED SUB-SKILL: Use `executing-plans` to implement this plan task-by-task.

**Goal:** Build a stable retrieval submodule that ingests incremental university Markdown, publishes precise L1 indexes, imports every extracted URL into WeKnora with traceable relationships, and returns L1 results through HTTP/MCP within one second.

**Architecture:** PostgreSQL is the data control plane, OpenSearch is the online L1 retrieval store, and external WeKnora supplies scoped page evidence. FastAPI owns ingestion and retrieval APIs; a thin TypeScript MCP Gateway exposes the same retrieval contract to Agents without entering the HTTP hot path.

**Tech Stack:** Python 3.11, FastAPI, Pydantic, PostgreSQL 16, OpenSearch 2.15, httpx, TypeScript, Node.js 20, official MCP SDK, Docker Compose, external WeKnora.

---

## 1. Locked Scope

### Product goals

1. Use a long-term architecture while validating first with the smallest complete MIT implementation.
2. L1 retrieval must meet HTTP p95 `< 500ms` and MCP p95 `< 1s` while preserving precision.
3. Accept incremental Markdown uploads, parse structured L1 records, extract all contained URLs, import changed URLs into WeKnora, and preserve MD-to-entry-to-source-to-WeKnora relationships.
4. Keep the schema and ingestion path suitable for 300+ core and 10000 non-core universities.
5. Validate MIT first, then perform incremental updates on several additional universities.

### Explicitly removed

- L0 clients, configuration, routes, tests, readiness checks, and documentation.
- Country-level discovery, rankings, recommendations, reports, and cross-university metric workflows.
- Redis, MinIO, Langfuse, reranker, semantic cache, NestJS, and additional vector databases.
- Runtime JSONL retrieval and mock evidence fallback.
- Natural-language answer generation inside the retrieval module.
- Legacy stateless `/mcp`, five separate public MCP tools, and HTTP/CLI/MCP four-way consistency gates.
- PostgreSQL QA tables, conversation state, Agent traces, and report workflow tables.
- Per-university OpenSearch indexes and aliases.

### Retained middleware

```text
Core Compose: PostgreSQL + OpenSearch + FastAPI Retrieval Service
Optional MCP profile: TypeScript MCP Gateway
External dependency: WeKnora
```

PostgreSQL does not participate in the normal query hot path. It stores authoritative ingestion, version, source, fact-review, and WeKnora job state.

## 2. Public Contracts

### Retrieval API

Add `POST /v1/retrieve`:

```json
{
  "query": "MIT Course 6-3 本科专业是什么？",
  "university_id": "mit",
  "context": {
    "level": "undergraduate",
    "program_id": null,
    "entry_id": null
  },
  "max_results": 5
}
```

Response:

```json
{
  "trace_id": "tr_xxx",
  "mode": "l1",
  "scope": {
    "university_id": "mit",
    "dataset_version": "mit_20260704_v2"
  },
  "matches": [],
  "evidence": [],
  "missing_slots": [],
  "warnings": [],
  "timings": {
    "total_ms": 0,
    "l1_ms": 0,
    "weknora_ms": 0
  }
}
```

Allowed modes:

```text
l1
l1_l2
clarification
not_found
error
```

Rules:

- `matches` contains structured catalog records or raw fact values; the service does not generate prose answers.
- Facts include `review_status`, `conflict_status`, `capture_date`, and source metadata.
- `review_required` facts may be returned as records but must include a warning and must not be labeled confirmed.
- If `university_id` is absent, resolve only through the local university alias index.
- Unknown universities return `not_found`; never default to MIT.
- L1 exact catalog and approved fact matches do not trigger WeKnora.
- Policies, eligibility, curriculum details, or insufficient L1 support trigger WeKnora after L1 scope resolution.

### Ingestion API

Add `POST /v1/ingestions` as multipart upload:

```text
university_id: required
school_tier: core | non_core
file: Markdown file
```

Return HTTP `202`:

```json
{
  "run_id": "ing_xxx",
  "university_id": "mit",
  "status": "accepted",
  "input_hash": "sha256..."
}
```

Add `GET /v1/ingestions/{run_id}` returning stage status, counts, failures, OpenSearch publication state, and WeKnora job summary.

The CLI command `ingest-school` must call these HTTP endpoints rather than implement a second ingestion path.

### MCP contract

Expose one tool only:

```text
retrieve_university_knowledge
```

Its input and output are identical to `POST /v1/retrieve`. The TypeScript Gateway contains no retrieval, routing, caching, or evidence logic.

## 3. Data Control Plane

### PostgreSQL schema

Replace the current duplicated control-plane schema with these tables:

```text
school_versions
ingestion_runs
ingestion_records
catalog_entries
source_registry
source_entry_links
fact_store
weknora_import_jobs
```

Responsibilities:

- `school_versions`: staging/current dataset version per university and publication state.
- `ingestion_runs`: one row per uploaded MD, including input hash and stage failures.
- `ingestion_records`: validated staging JSON records for the run.
- `catalog_entries`: authoritative normalized catalog records.
- `source_registry`: one canonical URL per university/source with WeKnora IDs and lifecycle state.
- `source_entry_links`: many-to-many association between sources and catalog entries.
- `fact_store`: authoritative raw/normalized facts and review/conflict state.
- `weknora_import_jobs`: asynchronous import/poll/retry state.

Remove `qa_cases`, `qa_reviews`, duplicate `url_manifest` storage, and JSON arrays used as relational links.

Use PostgreSQL constraints for stable IDs, canonical URL uniqueness within a university, foreign keys, status enums/checks, and current-version integrity.

### Version publication

For each school update:

1. Create an `ingestion_run` and staging records.
2. Validate all schemas and references.
3. Diff against the current school version.
4. Transactionally write the new authoritative version without changing `current_version`.
5. Index the new version into OpenSearch.
6. Verify document counts and required records.
7. Switch `school_versions.current_version` in one PostgreSQL transaction.
8. Refresh the Retrieval Service in-process version map.
9. Retain the previous version for rollback and clean it asynchronously after the retention window.

No Redis is used. The service loads the approximately 10300 current-version mappings into memory and refreshes them after publication and on a short polling interval.

## 4. Markdown Parsing And URL Association

### Parser behavior

Keep the MIT adapter and generic structured adapter, but move shared extraction into one parser core.

Extract URLs from:

- Markdown links: `[label](https://...)`.
- Autolinks: `<https://...>`.
- Bare HTTP/HTTPS URLs.
- Structured catalog and fact table URL fields.

Canonicalization rules:

- Normalize scheme and hostname casing.
- Remove fragments.
- Remove known tracking parameters while retaining functional query parameters.
- Normalize empty paths and trailing slash consistently.
- Reject non-HTTP(S), malformed, localhost, and private-network URLs.
- Generate deterministic `source_id` from `university_id + canonical_url`.

Association rules:

- A URL in a catalog/fact table row links directly to that row's `entry_id` or `fact_id`.
- A URL in prose inherits the nearest Markdown heading path and topic classification.
- Repeated URLs merge topics and entry links instead of creating duplicate sources.
- Every extracted URL is recorded in `source_registry`, including URLs without a catalog entry.
- The run report lists unclassified URLs for review but does not discard them.

### Diff behavior

- MD input hash unchanged: mark run `unchanged`, skip OpenSearch and WeKnora.
- Catalog/fact-only change: publish affected L1 records; do not reimport unchanged URLs.
- New URL: create source and WeKnora job.
- Changed canonical URL or source content hash: supersede the old source and create a replacement job.
- Removed URL: mark source inactive; do not physically delete history.
- Failed parsing or reference validation: do not publish any part of the school version.

## 5. OpenSearch L1

### Index topology

Use four global aliases, not per-school aliases:

```text
l1_universities_current
l1_catalog_entries_current
l1_quick_facts_current
l1_sources_current
```

Documents include `university_id`, `dataset_version`, and status. Document IDs include the university, dataset version, and stable entity ID so old and new versions can coexist during publication.

### Retrieval strategy

One L1 request performs an OpenSearch `_msearch` covering:

1. Exact IDs and exact normalized `course_code`.
2. Catalog BM25 query with field boosts and university/level/version filters.
3. Fact lookup filtered by fact type, review status, university, program, and version.
4. Source-scope lookup for possible WeKnora use.

Precision rules:

- Exact identifier or course-code match suppresses weaker alternatives.
- Results below the configured minimum score are omitted; never fill `top_k` with unrelated records.
- Every match returns `match_reason`, `_score`, source ID, source URL, and dataset version.
- Facts with conflicts or non-approved review state are explicitly marked and cannot be promoted as confirmed.
- Search mappings must provide normalized keyword subfields for aliases, course codes, program names, departments, and degree levels.

Use a persistent OpenSearch client created during FastAPI lifespan. Runtime JSONL loading is prohibited outside tests.

## 6. WeKnora Import And Evidence

### Import worker

Use PostgreSQL as the job queue; do not introduce Redis or Celery.

- Claim jobs with `FOR UPDATE SKIP LOCKED`.
- Use bounded concurrency and a persistent async HTTP client.
- Import every active URL from core and non-core universities.
- Treat duplicate URL responses as idempotent reuse.
- Persist knowledge, document, chunk, tag, status, retry count, and failure reason.
- Retry transient import/status errors asynchronously with bounded backoff.
- Never make MD upload wait for all WeKnora imports.

### Scope requirement

Before implementation, run an authenticated capability test proving that WeKnora hybrid search supports server-side filtering by `tag_ids`, knowledge IDs, or document IDs.

Preferred implementation:

- Maintain one university tag per school, for example `university:mit`.
- Attach the tag during URL import.
- L1 resolves university/source scope before WeKnora search.
- Send the university tag and supported knowledge/document filters in the WeKnora request.
- Strictly post-filter returned evidence against `source_registry` as a second gate.

If authenticated testing proves that no server-side scope filter exists, stop the all-university WeKnora rollout and record a blocking architecture decision. Global top-k followed only by client-side filtering is not an accepted fallback.

### Evidence contract

Evidence must contain:

```text
evidence_id
source_id
source_url
knowledge_id
document_id
chunk_id
chunk_text
score
capture_date
dataset_version
```

Evidence without a scope mapping, real chunk text, or current source/version is discarded. No local fact snippet may be presented as WeKnora evidence.

## 7. FastAPI Retrieval Service

Replace keyword route selection with a fixed retrieval flow:

```text
normalize request
-> resolve local university/context
-> OpenSearch L1 msearch
-> precision/fact gate
-> return L1 when sufficient
-> otherwise derive source scope
-> scoped WeKnora search
-> evidence gate
-> structured response
```

Runtime behavior:

- No LLM calls.
- No country/ranking/L0 fallback.
- No request-time retries.
- Use persistent clients and explicit deadlines.
- Return L1 results when WeKnora times out, with `warnings=["evidence_timeout"]` where appropriate.
- Record stage timings in every response and structured log.

Latency budgets:

```text
HTTP L1 p95: < 500ms
MCP L1 p95: < 1s
L1 + WeKnora p95: < 3s
```

The WeKnora latency target is separate from the one-second L1 requirement. Claude/Codex/Hermes answer-generation time is outside the retrieval SLO.

## 8. TypeScript MCP Gateway

Migrate all Tool Gateway source and tests from JavaScript to TypeScript.

- Add strict `tsconfig.json` and compile to `dist/`.
- Use a multi-stage Docker build: install dev dependencies, compile, then run production dependencies plus compiled output.
- Keep the official MCP SDK Streamable HTTP endpoint only.
- Remove legacy SSE RPC handling.
- Expose only `retrieve_university_knowledge`.
- Forward trace IDs and structured errors unchanged.
- Add request timeout slightly above the Retrieval Service L1/L2 budgets.
- Keep Gateway deployable as an optional Compose profile; HTTP clients bypass it.

## 9. Compose And Configuration

Core services:

```text
postgres
opensearch
fast-router
```

Optional profile:

```text
tool-gateway
```

External:

```text
WeKnora
```

Remove MinIO and all L0/Langfuse/Redis environment variables and readiness checks.

Use an untracked local environment file for WeKnora credentials. `/health` must report PostgreSQL, OpenSearch aliases, WeKnora configuration, and current-version cache state separately. Missing WeKnora configuration allows L1-only development but blocks L1+WeKnora release acceptance.

## 10. Implementation Tasks

### Task 1: Replace the active architecture baseline

**Files:**

- Modify: `docs/architecture/00-overview.md`
- Modify: `docs/architecture/01-system-architecture.md`
- Modify: `docs/architecture/03-runtime-call-flow.md`
- Modify: `docs/architecture/05-agent-tooling-architecture.md`
- Modify: `docs/architecture/07-quality-gates-acceptance.md`

Steps:

1. Write the L1 + WeKnora architecture and remove L0 from active diagrams/contracts.
2. Document Gateway as optional MCP edge only.
3. Document the one-second L1 and three-second WeKnora SLOs.
4. Mark prior Agent-platform design documents as historical rather than active baseline.

### Task 2: Normalize the PostgreSQL control plane

**Files:**

- Modify: `infra/postgres/001_initial_schema.sql`
- Remove/replace: `infra/postgres/002_ingestion_staging.sql`
- Modify: `pipelines/catalog-parser/src/catalog_parser/postgres_loader.py`
- Test: `tests/test_postgres_loader.py`

Steps:

1. Write failing schema/loader tests for versioning, URL uniqueness, links, facts, and jobs.
2. Replace duplicated and QA tables with the locked control-plane schema.
3. Implement transactional staging/current publication helpers.
4. Verify rollback leaves the previous school version current.
5. Reset the local development PostgreSQL volume once because no production migration compatibility is required yet.

### Task 3: Build the unified Markdown extraction pipeline

**Files:**

- Modify: `pipelines/catalog-parser/src/catalog_parser/mit_parser.py`
- Modify: `pipelines/catalog-parser/src/catalog_parser/structured_markdown_parser.py`
- Create: `pipelines/catalog-parser/src/catalog_parser/markdown_sources.py`
- Test: `tests/test_parser_contracts.py`

Steps:

1. Add failing tests for Markdown links, autolinks, bare URLs, deduplication, heading context, entry links, and invalid URLs.
2. Implement shared URL extraction and canonicalization.
3. Merge structured table sources with prose-extracted sources.
4. Preserve deterministic IDs and many-to-many relationships.
5. Verify the MIT reconciliation remains 157 catalog entries while source coverage increases only when previously unrecorded URLs exist.

### Task 4: Add HTTP ingestion and asynchronous jobs

**Files:**

- Modify: `apps/fast-router/src/fast_router/main.py`
- Create: `apps/fast-router/src/fast_router/ingestion.py`
- Modify: `scripts/router_cli.py`
- Test: `tests/test_fast_router_api.py`

Steps:

1. Add failing API tests for upload, duplicate input, invalid MD, status polling, and failed publication.
2. Implement `POST /v1/ingestions` and `GET /v1/ingestions/{run_id}`.
3. Persist raw MD on a mounted durable volume keyed by run ID and input hash.
4. Make CLI ingestion call the HTTP API.
5. Verify upload returns `202` without waiting for WeKnora.

### Task 5: Replace per-school OpenSearch indexes

**Files:**

- Modify: `pipelines/indexer/src/indexer/opensearch_publisher.py`
- Modify: `infra/opensearch/l1_catalog_entries_mapping.json`
- Modify: `infra/opensearch/l1_quick_facts_mapping.json`
- Modify: `infra/opensearch/l1_url_manifest_mapping.json`
- Test: `tests/test_opensearch_publisher.py`

Steps:

1. Add failing tests for global aliases, versioned document IDs, exact course code, and school-only updates.
2. Replace per-school index creation with global versioned indexes.
3. Publish one school's new version without rebuilding other schools.
4. Verify previous-version documents remain queryable for rollback.
5. Add the university metadata/source index required by local alias and scope resolution.

### Task 6: Implement the OpenSearch L1 retrieval client

**Files:**

- Replace runtime behavior in: `apps/fast-router/src/fast_router/knowledge.py`
- Create: `apps/fast-router/src/fast_router/opensearch_retrieval.py`
- Test: `tests/test_router_core.py`

Steps:

1. Add failing tests reproducing Course 6-3 noise, AI false positives, fact review gating, and unknown-school behavior.
2. Implement exact-first `_msearch` with strict filters and score thresholds.
3. Add match reasons and current-version filtering.
4. Remove runtime JSONL reads.
5. Verify no unrelated result is used to fill `top_k`.

### Task 7: Make WeKnora import and search real-only

**Files:**

- Modify: `pipelines/catalog-parser/src/catalog_parser/weknora_importer.py`
- Modify: `scripts/weknora_import_worker.py`
- Modify: `apps/fast-router/src/fast_router/weknora_client.py`
- Test: `tests/test_weknora_importer.py`
- Test: `tests/test_weknora_search_client.py`

Steps:

1. Run the authenticated scope-filter capability test and record the accepted request contract.
2. Add failing tests for university tags, source filtering, retries, duplicate URLs, and out-of-scope chunks.
3. Replace JSONL mutation with PostgreSQL job/state updates.
4. Implement bounded async import workers using PostgreSQL job claims.
5. Remove mock mode from production CLI/service paths.
6. Enforce real chunk evidence and current-version checks.

### Task 8: Replace Router endpoints with the unified retrieval API

**Files:**

- Modify: `apps/fast-router/src/fast_router/main.py`
- Create: `apps/fast-router/src/fast_router/retrieval.py`
- Modify: `apps/fast-router/src/fast_router/tracing.py`
- Test: `tests/test_fast_router_api.py`

Steps:

1. Add failing contract tests for all five response modes.
2. Implement `POST /v1/retrieve` and the fixed L1-first flow.
3. Remove L0 initialization, old route heuristics, mock evidence, and public legacy endpoints.
4. Add stage timing and deadline handling.
5. Verify L1 can operate when WeKnora is unavailable and reports that state accurately.

### Task 9: Migrate Gateway to TypeScript and one MCP tool

**Files:**

- Replace: `apps/tool-gateway/src/server.js` with `apps/tool-gateway/src/server.ts`
- Replace: `apps/tool-gateway/src/sdk_client_call.js` with `apps/tool-gateway/src/sdk_client_call.ts`
- Replace: `apps/tool-gateway/test/server.test.js` with `apps/tool-gateway/test/server.test.ts`
- Modify: `apps/tool-gateway/package.json`
- Modify: `apps/tool-gateway/Dockerfile`
- Create: `apps/tool-gateway/tsconfig.json`

Steps:

1. Add TypeScript compile/test scripts and strict types.
2. Port existing transport tests before changing behavior.
3. Remove legacy MCP and register `retrieve_university_knowledge` only.
4. Build a multi-stage production image.
5. Verify MCP responses match the HTTP retrieval contract.

### Task 10: Minimize Compose and release gates

**Files:**

- Modify: `infra/docker-compose.yml`
- Modify: `.env.example`
- Modify: `scripts/release_gate.py`
- Modify: `docs/operations/eval-and-release-runbook.md`

Steps:

1. Remove L0, MinIO, Langfuse, and obsolete Agent-gate configuration.
2. Define core and MCP profiles.
3. Add real OpenSearch alias, version-map, PostgreSQL, and WeKnora readiness checks.
4. Block release if runtime JSONL/mock evidence paths are enabled.

### Task 11: Build precision, incremental, and latency acceptance gates

**Files:**

- Replace/refine: `qa/mit-gold-cases.jsonl`
- Create: `qa/retrieval-acceptance-cases.jsonl`
- Create: `scripts/retrieval_benchmark.py`
- Modify: `apps/fast-router/src/fast_router/qa.py`

Steps:

1. Create 30 manually labeled cases: 15 L1, 10 L1+WeKnora, and 5 clarification/not-found.
2. Include all failures discovered during the manual Claude QA session.
3. Make evaluation field-aware and exclude trace IDs and random metadata.
4. Run the suite five times and require identical outcomes.
5. Benchmark warm HTTP and MCP paths.
6. Verify MIT initial ingestion and retrieval.
7. Update several university MDs and verify only those schools and changed URLs are republished/reimported.

## 11. Acceptance Gates

### Data and incremental

- MIT MD produces 157 catalog entries and passes all schema/reference checks.
- Every valid HTTP(S) URL in the MD appears exactly once in `source_registry` after canonicalization.
- Every catalog/fact source relationship is queryable through `source_entry_links`.
- An unchanged MD performs no OpenSearch publication and no WeKnora import.
- A single URL change creates exactly one affected WeKnora job.
- A school update never rewrites or changes another school's current version.
- Failed parse/index/import stages preserve the previous current school version.

### Retrieval precision

- Exact identifier/course-code Precision@1 is `100%`.
- Manually labeled L1 Precision@5 is at least `95%`.
- Wrong university/program/source evidence acceptance count is `0`.
- Confirmed fact answers from non-approved or conflicting facts are `0`.
- Returned WeKnora evidence has real chunk text and current source/version linkage.

### Performance

- Warm HTTP L1 p95 `< 500ms`.
- Warm MCP L1 p95 `< 1s`.
- L1 + WeKnora p95 `< 3s` after real service configuration.
- No synchronous WeKnora import occurs in upload or retrieval requests.
- Each response reports total/L1/WeKnora timing fields.

### Deployment

- Core Compose starts PostgreSQL, OpenSearch, and Retrieval Service healthy.
- MCP profile starts the compiled TypeScript Gateway healthy.
- L1 works without WeKnora configuration; L1+WeKnora release is blocked without real WeKnora connectivity and scope-filter verification.
- No L0, Redis, MinIO, Langfuse, mock evidence, or runtime JSONL dependency remains in the active deployment.

## 12. Assumptions

- This is a new, unreleased project; breaking old HTTP/MCP contracts and resetting local development data are allowed.
- MIT is the first acceptance school; architecture and IDs remain multi-school from the first implementation.
- All core and non-core schools may create WeKnora import jobs, subject to server-side scope-filter capability.
- Raw Markdown is retained on a persistent local/server volume; object storage is deferred until deployment requirements justify it.
- PostgreSQL is the only control-plane state store; OpenSearch and WeKnora can be rebuilt from authoritative data and import state.
- The repository currently has no usable Git history, so implementation checkpoints use test reports rather than mandatory commits.
