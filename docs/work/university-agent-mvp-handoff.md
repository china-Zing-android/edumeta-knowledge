Status: superseded

> Superseded by `docs/work/l1-weknora-retrieval-handoff.md` and `docs/plans/2026-07-15-l1-weknora-retrieval-correction.md` after the project scope was corrected to an L1 + WeKnora retrieval submodule without L0.

# University Agent MVP Handoff

## Goal

Implement the university knowledge-base Agent MVP as a long-term architecture MVP slice, not a throwaway demo. Current user scope has been reduced to MIT-only acceptance: 5-school and 300-school acceptance are no longer release requirements for the active goal. Multi-school support remains implemented and verified as extra capacity, but MIT release readiness is now judged by the MIT profile gate.

## Latest External Integration (2026-07-10)

- Real WeKnora protocol is now verified against the supplied service:
  - Service roots accept either `http://host` or `http://host/api/v1`; the adapter normalizes to one API root.
  - Auth uses `X-API-Key`, not `Authorization: Bearer`.
  - URL import uses `POST /knowledge-bases/{kb_id}/knowledge/url` with WeKnora-supported fields only.
  - Duplicate URLs (`409`) are treated as idempotent reuse of the returned knowledge.
  - Status polling uses `GET /knowledge/{knowledge_id}` and maps `parse_status` to local import state, including `finalizing -> running`.
  - Search uses `POST /knowledge-bases/{kb_id}/hybrid-search`; returned `knowledge_id` is mapped to `url_manifest` locally before the Evidence Gate accepts it.
- Live smoke report: `qa/reports/external-live-smoke-2026-07-10.json` is `passed`.
  - The test performed real URL import/reuse, parse-state verification, and scoped hybrid search for MIT EECS URL `src_mit_oge_mit_edu_programs_electrical_engineering_and_computer_science`, returning 7 scoped evidence items.
  - L0 Streamable MCP `resolve_institution({"name":"MIT"})` resolved OpenAlex `I63966007` to internal `mit` with confidence `1.0`.
- `L0_MCP_URL` now takes precedence over the legacy HTTP L0 adapter. `L0_MCP_INSTITUTION_ID_MAP` supports explicit external-to-internal mappings; MIT is included by default.
- Langfuse remains optional observability. It records trace/tool/evidence/latency metadata; it does not retrieve evidence or generate answers. Without Langfuse keys, local JSONL tracing remains enabled.
- Manual QA remains `deferred_manual_qa`, not passed. `scripts/release_gate.py --manual-qa-mode deferred` can express functional readiness without falsely passing human review. Formal release must use `--manual-qa-mode required`.
- Current MIT aggregate report: `qa/reports/mit-release-gate-2026-07-10.json` has one functional blocker only: `TOOL_GATEWAY_MCP_SDK_URL` is not configured for the deployed external Agent endpoint. The human QA gate is explicitly deferred.

## Latest Local Compose Verification (2026-07-10)

- The local Compose stack is now fully containerized and healthy: `postgres`, `opensearch`, `minio`, `fast-router`, and `tool-gateway`.
- `fast-router` image installs pinned runtime dependencies inside `/opt/venv`; verified in the running container with `VIRTUAL_ENV=/opt/venv` and Python at `/opt/venv/bin/python`.
- Build sources are configurable and default to domestic mirrors:
  - Docker base images: `docker.m.daocloud.io`.
  - Python packages: `https://pypi.tuna.tsinghua.edu.cn/simple`.
  - Node packages: `https://registry.npmmirror.com` with `npm ci` and `package-lock.json`.
- `fast-router` and `tool-gateway` have Compose healthchecks. Tool Gateway waits for Fast Router health before starting; all host ports bind only to `127.0.0.1` for local testing.
- Local MCP smoke passed at `http://127.0.0.1:8765/mcp-sdk`: tool list plus fact/catalog/deep/clarification calls all passed. Report: `qa/reports/local-compose-agent-smoke-2026-07-10.json`.
- Local Claude Code verification passed: `edumeta-local: http://127.0.0.1:8765/mcp-sdk (HTTP) - connected`.

## Latest Claude Agent Regression (2026-07-10)

- Fixed a confirmed L1 catalog precision defect: `KnowledgeStore.search_catalog()` previously scored the university alias `MIT`, which appears in every MIT record's `search_text`. Specific catalog questions could therefore return one relevant record followed by arbitrary same-school entries.
- Catalog scoring now removes university-alias and catalog-intent terms before matching. Specific questions require a matching program/degree/department attribute; a scope-only question such as `MIT 本科专业` still browses the requested level.
- Regression coverage now requires both the Fast Router core and HTTP catalog endpoint to return exactly one result, `Artificial Intelligence and Decision Making`, for the MIT AI undergraduate question. Full automated regression is green: 142 Python tests and 7 Tool Gateway Node tests.
- Rebuilt local `fast-router` Compose image and verified through the real local MCP SDK endpoint that both `fast_university_answer` and `search_catalog_entries` return exactly the 6-4 AI entry.
- Ran a real non-interactive Claude CLI Agent session against the connected `edumeta-local` MCP configuration. Claude loaded and called `mcp__edumeta-local__fast_university_answer` with the exact query `MIT 有哪些 AI 相关本科专业？`; it returned the single 6-4 result and cited the MIT catalog URL. Fast Router trace `tr_e90c813544d644ee996282ef15f540ec` records `route=catalog`, `mode=fast`, and `university_id=mit`.
- Open manual QA observation: `qa/manual-qa-observations.jsonl` records `qa_obs_mit_clarification_001` for the generic clarification wording returned by `MIT CS master 要求是什么？` (trace `tr_5adae7a3f6374822a8f958b3dd59303d`). Routing was correct, but the wording unnecessarily asks for a school despite MIT being resolved; severity is P1 and status is `open`.

## Current State

Completed and verified:

- Phase 0 documentation baseline exists under `docs/architecture`, `docs/schemas`, `docs/operations`, and `qa`.
- MIT parser generates normalized JSONL:
  - `data/normalized/mit/catalog_entries.jsonl`: 157 rows.
  - `data/normalized/mit/source_registry.jsonl`: 107 rows.
  - `data/normalized/mit/url_manifest.jsonl`: 107 rows.
  - `data/normalized/mit/quick_facts.jsonl`: 241 rows.
- MIT reconciliation passes: 55 SB + 17 Minor + 85 grad offerings = 157.
- Parser now enforces unique primary IDs for `source_id`, `entry_id`, `url_id`, and `fact_id`.
- Parser adapter registry exists at `catalog_parser.adapters`; MIT is registered as the first adapter, and unknown schools fail with a clear `No parser adapter registered...` error instead of silently reusing MIT parsing.
- Generic structured Markdown parser exists at `catalog_parser.structured_markdown_parser` and can be enabled explicitly with `--adapter generic_structured` for one school or `--default-adapter generic_structured` for `parse-school --all`; default unknown-school behavior still fails instead of silently guessing.
- Data validation gate exists at `catalog_parser.validation` and CLI command `validate-school`; it validates JSON schemas, required-field completeness, URL legal rate, cross-file references, and MIT reconciliation.
- Incremental diff gate exists at `catalog_parser.diff` and CLI command `diff-school`; it compares normalized record hashes, reports affected source/entry/fact/url IDs, identifies `weknora_reimport_source_ids`, and blocks physical removal of active records.
- Batch ingestion/indexing exists for multi-school scaling:
  - `catalog_parser.cli parse-school --all --input-root ... --out-root ...`
  - `catalog_parser.cli parse-school --all --input-root ... --out-root ... --default-adapter generic_structured`
  - `catalog_parser.cli validate-school --all --data-root ...`
  - `catalog_parser.cli diff-school --all --previous-data-root ... --data-root ...`
  - `catalog_parser.cli sync-weknora-school --all --data-root ...`
  - `indexer.cli index-school --all --data-root ...`
- Fast Router implements `/health`, `/fast-answer`, `/deep-search`, `/resolve-scope`, `/catalog/search`, `/facts/lookup`, `/url-scope/find`, and `/eval/run` over local JSONL.
- Tool Gateway exposes stateless MCP JSON-RPC/SSE tools:
  - `fast_university_answer`
  - `deep_university_search`
  - `search_catalog_entries`
  - `lookup_quick_facts`
  - `find_url_scope`
- Tool Gateway also exposes an MCP SDK Streamable HTTP endpoint at `/mcp-sdk` with the same 5 tools.
- CLI entrypoint exists at `scripts/router_cli.py` and exposes:
  - `fast-answer`
  - `deep-search`
  - `search-catalog`
  - `lookup-facts`
  - `find-url-scope`
- HTTP/CLI/legacy MCP/SDK MCP consistency gate exists at `scripts/tool_consistency_gate.py`, with smoke cases in `qa/tool-consistency-cases.jsonl`.
- External MCP SDK Agent smoke script exists at `scripts/external_agent_smoke.py`; it uses `apps/tool-gateway/src/sdk_client_call.js` to list `/mcp-sdk` tools and call fact/catalog/deep/clarification smoke cases against a configured external URL.
- Release gate aggregator exists at `scripts/release_gate.py`; it aggregates Data, Diff, Live Data, QA, Tool, WeKnora worker, external readiness, external live smoke, and external Agent smoke reports into one acceptance report.
- Release gate now supports profiles:
  - `--profile full`: previous full MVP profile, including multi-school scope.
  - `--profile mit`: current active acceptance profile, excluding `mvp_scope` and 5-school UAT requirements.
- MVP scope gate exists at `scripts/mvp_scope_gate.py`; it blocks release until normalized data, batch gates, UAT cases, conversation cases, route distribution, and MCP/tool calling cases satisfy MVP thresholds across at least 5 schools.
- PostgreSQL migration baseline exists:
  - `infra/postgres/001_initial_schema.sql`
  - `infra/postgres/002_ingestion_staging.sql`
- Postgres migration runner exists at `scripts/apply_postgres_migrations.py`.
- Live data gate exists at `scripts/live_data_gate.py`; it applies migrations, loads MIT JSONL into Postgres, publishes OpenSearch aliases, and verifies counts when both services are available.
- External dependency readiness gate exists at `scripts/live_readiness_gate.py`; it checks required WeKnora, L0, Langfuse, and external `/mcp-sdk` configuration and can optionally probe configured health/base URLs.
- External business live smoke gate exists at `scripts/external_live_smoke.py`; it selects one active Source Registry URL, calls real WeKnora URL import/status/search without writing local JSONL, verifies L0 resolves MIT, posts one Langfuse ingestion trace/span, and writes a blocking report.
- PostgreSQL loader exists in `catalog_parser.postgres_loader` and supports:
  - JSONL validation/dry-run.
  - `ingestion_runs` and `jsonl_staging`.
  - current-table upsert when a real `--postgres-dsn` is provided.
- WeKnora mock importer exists in `catalog_parser.weknora_importer` and supports:
  - `import-weknora-url --source-id ...`
  - `sync-weknora-school --changed-only`
  - deterministic mock `weknora_collection_id`, `weknora_knowledge_id`, `weknora_document_id`, and `weknora_chunk_ids`.
- WeKnora real URL import adapter exists behind `--mode real` and supports:
  - `WEKNORA_BASE_URL`
  - `WEKNORA_KNOWLEDGE_BASE_ID`
  - `WEKNORA_API_KEY`
  - `POST /api/v1/knowledge-bases/{knowledge_base_id}/knowledge/url`
  - flexible normalization of `knowledge_id`, `document_id`, `chunk_ids`, `status`, and `content_hash`.
- WeKnora import status polling exists behind `poll-weknora-imports` and supports:
  - `WEKNORA_IMPORT_STATUS_PATH_TEMPLATE`
  - `weknora_import_job_id`
  - `pending/running/success/failed` normalization and JSONL writeback.
  - bounded retry/backoff with `--max-poll-attempts` and `--poll-interval-seconds`.
- WeKnora schedulable import worker exists at `scripts/weknora_import_worker.py`; it combines changed-only import plus pending/running job polling and writes an attribution report.
- Fast Router WeKnora scoped search adapter exists in `apps/fast-router/src/fast_router/weknora_client.py` and supports:
  - `WEKNORA_SEARCH_PATH_TEMPLATE`
  - scoped `source_ids` and `document_ids`
  - Router evidence normalization
  - second-pass filtering by `university_id` and `source_id`.
- Current MIT local data has all 107 URL manifest rows marked `import_status=success` through mock WeKnora import.
- Fast Router Evidence Gate now refuses L2 evidence unless both `url_manifest.import_status` and `source_registry.weknora_import_status` are `success`.
- L0 HTTP adapter exists in `apps/fast-router/src/fast_router/l0_client.py` and is used as Router fallback only when local resolution cannot identify the school and `L0_API_BASE_URL` is configured.
- OpenSearch publisher exists in `indexer.opensearch_publisher` and supports:
  - staging index planning.
  - per-school current aliases like `l1_catalog_entries_mit_current`.
  - bulk action construction.
  - alias switch action construction using actual existing alias bindings.
  - explicit refresh before alias verification.
  - real publish when an OpenSearch URL is available.
- MIT QA gold suite has been expanded to 30 cases:
  - 10 catalog cases.
  - 10 fact cases.
  - 7 deep/evidence cases.
  - 3 clarification cases.
- MIT multi-turn UAT smoke suite exists at `qa/mit-uat-conversations.jsonl` with 3 conversations / 6 evaluated user turns.
- MIT expanded MVP UAT single-turn suite exists at `qa/mvp-uat-cases.jsonl` with 200 generated, executable cases:
  - 80 catalog cases.
  - 80 fact cases.
  - 30 deep/evidence cases.
  - 10 clarification cases.
  - Generated reproducibly from normalized MIT data by `scripts/build_mit_uat_cases.py`.
- MIT expanded MVP UAT multi-turn suite exists at `qa/mvp-uat-conversations.jsonl` with 50 generated conversations / 100 evaluated user turns:
  - 20 fact follow-up conversations.
  - 15 catalog follow-up conversations.
  - 10 deep/evidence follow-up conversations.
  - 5 clarification follow-up conversations.
  - Generated reproducibly from normalized MIT data by `scripts/build_mit_uat_conversations.py`.
- Multi-school MVP UAT generator exists at `scripts/build_mvp_uat_suite.py`:
  - Reads `data/normalized/{university_id}` directories.
  - Requires at least 5 normalized schools by default.
  - Generates 200 single-turn cases by default: catalog 60, fact 60, deep 50, clarification 30.
  - Generates 50 conversation cases by default.
  - Adds `university_id`, `case_source=generated_from_normalized_data`, and `human_review_required=true`.
  - Samples by school in round-robin order so generated cases do not collapse onto one school.
- QA reports can be written from `/eval/run` with `output_path`; current report is `qa/reports/mit-gold-report-2026-07-09.json`.
- QA runner/gate scripts exist:
  - `scripts/run_qa_suite.py`
  - `scripts/qa_gate.py`
- Human QA/UAT review gate exists at `scripts/human_qa_review_gate.py`:
  - Reads one or more QA case JSONL files plus `qa/human-reviews.jsonl`.
  - Requires human `review_id/qa_case_id/trace_id/reviewer_id` and five 0-2 scores.
  - Blocks P0 factual/evidence/freshness failures, P0/P1 hallucination flags, weak evidence/task/clarification rates, and any low-score/flagged review without a valid failure category.
  - Current template is `qa/human-reviews.template.jsonl`.
- Release artifact generator exists at `scripts/generate_release_artifacts.py`; it writes `qa/acceptance-report-YYYY-MM-DD.md`, `qa/qa-report-YYYY-MM-DD.md`, and `qa/failure-analysis-YYYY-MM-DD.md` from current gate and QA reports without masking failed release state.
- QA review persistence exists in `scripts/persist_qa_report.py`; the live Postgres QA persistence report is `qa/reports/live-qa-postgres-gate-2026-07-09.json`.
- Fast Router has JSONL trace persistence in `apps/fast-router/src/fast_router/tracing.py`; `/fast-answer` and `/deep-search` write route, mode, latency, evidence source IDs, missing reasons, and next action types.
- Fast Router `KnowledgeStore.resolve_university` now discovers school IDs from `KNOWLEDGE_DATA_ROOT` and can resolve generic school aliases from catalog `search_text`, instead of only recognizing MIT.
- Fast Router has optional Langfuse legacy ingestion support in `apps/fast-router/src/fast_router/tracing.py`:
  - Enabled only when `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, and `LANGFUSE_SECRET_KEY` are all configured.
  - Posts `trace-create` and `span-create` events to `/api/public/ingestion` with Basic Auth.
  - HTTP failures are non-fatal and do not block Router responses or local JSONL trace writes.
  - `TRACE_LOG_PATH=off` disables only local JSONL tracing; configured Langfuse ingestion can still run.
- Docker Compose now mounts `data/normalized` into Fast Router with `KNOWLEDGE_DATA_ROOT=/app/data/normalized`.
- Docker Compose passes `WEKNORA_KNOWLEDGE_BASE_ID`, `WEKNORA_SEARCH_PATH_TEMPLATE`, `WEKNORA_IMPORT_STATUS_PATH_TEMPLATE`, and `L0_RESOLVE_UNIVERSITY_PATH` into Fast Router.
- Docker Compose now passes `TRACE_LOG_PATH`, `LANGFUSE_HOST`, `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_ENVIRONMENT`, `LANGFUSE_RELEASE`, and `LANGFUSE_TIMEOUT_SECONDS` into Fast Router.
- `.dockerignore` excludes local caches and `node_modules` from Docker build contexts.

## Important Decisions

- This remains a long-term MVP slice, not a temporary demo.
- Agent access must go through Tool Gateway/MCP; no direct DB/Search/RAG access from Agent clients.
- WeKnora is the evidence KB. Current implementation has unit-tested real import/search adapters, but local MIT evidence still uses deterministic mock import until live WeKnora credentials are available and verified.
- Deep evidence is gated by import success. Pending URLs cannot produce L2 evidence.
- OpenSearch aliases are per-school for MVP to preserve single-school incrementality. Global aliases are a later aggregation layer and must only switch from complete multi-school staging builds.
- Generated MIT UAT cases are a local executable QA gate for the active MIT-only profile, but they are not a substitute for human QA/UAT review.
- Generated five-school UAT cases remain available as an expansion proof, but they are no longer a release requirement for the current active goal.
- Router fact/catalog/deep route precedence is intentionally: ambiguity checks, yes/no high-risk program questions to deep, hard fact terms, catalog terms, then deep policy/background terms. This preserves gold deep evidence cases while preventing program names like `Business Analytics` or `Data, Economics, and Design of Policy` from being misrouted.

## Key Commands

Regenerate MIT JSONL:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli parse-school --university-id mit --input docs/MIT_知识库_完整深度数据_v2.md --out-dir data/normalized/mit
```

Run MIT validation gate:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli validate-school --university-id mit --data-dir data/normalized/mit --output-path qa/reports/mit-validation-gate-2026-07-09.json
```

Run batch validation/index gates:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli parse-school --all --input-root data/raw-md --out-root data/normalized --default-adapter generic_structured
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli validate-school --all --data-root data/normalized --output-path qa/reports/all-validation-gate-2026-07-09.json
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli diff-school --all --previous-data-root data/normalized --data-root data/normalized --output-path qa/reports/all-diff-gate-2026-07-09.json
PYTHONPATH=pipelines/indexer/src python3 -m indexer.cli index-school --all --data-root data/normalized --output-path qa/reports/all-index-gate-2026-07-09.json
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli sync-weknora-school --all --data-root data/normalized --changed-only --mode mock --output-path qa/reports/all-weknora-sync-gate-2026-07-09.json
```

Parse one structured generic school:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli parse-school --university-id exampleu --input data/raw-md/exampleu.md --out-dir data/normalized/exampleu --adapter generic_structured
```

Mock-import MIT URLs:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli sync-weknora-school --university-id mit --data-dir data/normalized/mit --mode mock
```

Real WeKnora URL import, once credentials and a live knowledge base exist:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli sync-weknora-school --university-id mit --data-dir data/normalized/mit --changed-only --mode real --weknora-base-url "$WEKNORA_BASE_URL" --weknora-knowledge-base-id "$WEKNORA_KNOWLEDGE_BASE_ID" --weknora-api-key "$WEKNORA_API_KEY"
```

Poll pending/running WeKnora imports:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli poll-weknora-imports --university-id mit --data-dir data/normalized/mit --mode real --weknora-base-url "$WEKNORA_BASE_URL" --weknora-knowledge-base-id "$WEKNORA_KNOWLEDGE_BASE_ID" --weknora-api-key "$WEKNORA_API_KEY"
```

Run schedulable WeKnora import worker:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 scripts/weknora_import_worker.py --university-id mit --data-dir data/normalized/mit --changed-only --mode real --max-poll-attempts 6 --poll-interval-seconds 10 --output-path qa/reports/weknora-import-worker-2026-07-09.json
```

Check external dependency readiness:

```bash
python3 scripts/live_readiness_gate.py --output-path qa/reports/live-readiness-gate-2026-07-09.json
```

Run external business live smoke when WeKnora, L0, and Langfuse envs are available:

```bash
python3 scripts/external_live_smoke.py --data-dir data/normalized/mit --university-id mit --output-path qa/reports/external-live-smoke-2026-07-09.json
```

Record missing external config locally without masking the release blocker:

```bash
python3 scripts/external_live_smoke.py --output-path qa/reports/external-live-smoke-2026-07-09.json --allow-not-ready
```

Run MIT diff gate:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli diff-school --university-id mit --previous-data-dir data/normalized/mit --data-dir data/normalized/mit --output-path qa/reports/mit-diff-gate-2026-07-09.json
```

Run external MCP SDK smoke when `TOOL_GATEWAY_MCP_SDK_URL` is available:

```bash
python3 scripts/external_agent_smoke.py --url "$TOOL_GATEWAY_MCP_SDK_URL" --output-path qa/reports/external-agent-smoke-2026-07-09.json
```

Run aggregate release gate:

```bash
python3 scripts/mvp_scope_gate.py --output-path qa/reports/mvp-scope-gate-2026-07-09.json
python3 scripts/release_gate.py --output-path qa/reports/mvp-release-gate-2026-07-09.json
```

Postgres loader dry-run:

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli load-school --university-id mit --data-dir data/normalized/mit --dry-run
```

OpenSearch indexer dry-run:

```bash
PYTHONPATH=pipelines/indexer/src python3 -m indexer.cli index-school --university-id mit --data-dir data/normalized/mit --dry-run
```

Apply Postgres migrations:

```bash
python3 scripts/apply_postgres_migrations.py --postgres-dsn postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta --migrations-dir infra/postgres
```

Run live Postgres/OpenSearch data gate once both services are available:

```bash
PYTHONPATH=pipelines/catalog-parser/src:pipelines/indexer/src python3 scripts/live_data_gate.py --output-path qa/reports/live-data-gate-2026-07-09.json
```

Generate and run the 200-case MIT MVP UAT suite:

```bash
python3 scripts/build_mit_uat_cases.py --data-dir data/normalized/mit --output-path qa/mvp-uat-cases.jsonl
KNOWLEDGE_DATA_ROOT=data/normalized TRACE_LOG_PATH=off PYTHONPATH=apps/fast-router/src python3 scripts/run_qa_suite.py --suite-path qa/mvp-uat-cases.jsonl --output-path qa/reports/mvp-uat-report-2026-07-09.json
python3 scripts/qa_gate.py --cases-path qa/mvp-uat-cases.jsonl --report-path qa/reports/mvp-uat-report-2026-07-09.json --min-total 200 --output-path qa/reports/mvp-uat-gate-2026-07-09.json
```

Generate 5-school MVP UAT suites only when validating the optional multi-school expansion profile:

```bash
python3 scripts/build_mvp_uat_suite.py --data-root data/normalized --single-output-path qa/mvp-uat-cases.jsonl --conversation-output-path qa/mvp-uat-conversations.jsonl --min-schools 5
```

Run MIT-only human QA/UAT review gate after reviewers fill `qa/human-reviews.jsonl`:

```bash
python3 scripts/human_qa_review_gate.py --cases-path qa/mit-gold-cases.jsonl --cases-path qa/mit-uat-conversations.jsonl --reviews-path qa/human-reviews.jsonl --min-reviewed-cases 30 --min-reviewed-conversations 3 --output-path qa/reports/human-qa-review-mit-gate-2026-07-09.json
```

Generate MIT-only release artifacts:

```bash
python3 scripts/generate_release_artifacts.py --profile mit --release-report-path qa/reports/mit-release-gate-2026-07-09.json --scope-report-path qa/reports/live-data-gate-2026-07-09.json --human-review-gate-path qa/reports/human-qa-review-mit-gate-2026-07-09.json --human-reviews-path qa/human-reviews.jsonl --mit-gold-report-path qa/reports/mit-gold-report-2026-07-09.json --mvp-uat-report-path qa/reports/mit-uat-conversations-report-2026-07-09.json --mvp-conversation-report-path qa/reports/mit-uat-conversations-report-2026-07-09.json --output-dir qa --report-date mit-2026-07-09
```

Generate and run the MIT conversation UAT suite:

```bash
python3 scripts/build_mit_uat_conversations.py --data-dir data/normalized/mit --output-path qa/mit-uat-conversations.jsonl
KNOWLEDGE_DATA_ROOT=data/normalized TRACE_LOG_PATH=off PYTHONPATH=apps/fast-router/src python3 scripts/run_qa_suite.py --suite-path qa/mit-uat-conversations.jsonl --output-path qa/reports/mit-uat-conversations-report-2026-07-09.json --mode conversation
python3 scripts/qa_gate.py --cases-path qa/mit-uat-conversations.jsonl --report-path qa/reports/mit-uat-conversations-report-2026-07-09.json --min-total 6 --min-conversations 3 --output-path qa/reports/mit-uat-conversations-gate-2026-07-09.json
```

Python tests:

```bash
PYTHONPATH=apps/fast-router/src:pipelines/catalog-parser/src:pipelines/indexer/src python3 -m unittest discover -s tests -v
```

Run Fast Router:

```bash
PYTHONPATH=apps/fast-router/src KNOWLEDGE_DATA_ROOT=data/normalized python3 -m uvicorn fast_router.main:app --host 127.0.0.1 --port 8000
```

Run Tool Gateway:

```bash
FAST_ROUTER_BASE_URL=http://127.0.0.1:8000 npm start
```

Run HTTP/CLI/legacy MCP/SDK MCP consistency gate:

```bash
python3 scripts/tool_consistency_gate.py --cases-path qa/tool-consistency-cases.jsonl --output-path qa/reports/tool-consistency-gate-2026-07-09.json
```

## Verification

Last verified:

- Python tests: 135 tests passed on 2026-07-09.
- Tool Gateway Node tests: 6 tests passed on 2026-07-09.
- Docker Compose config validation passed on 2026-07-09.
- Parser output: 157 catalog entries, 107 source registry rows, 107 URL manifest rows, 241 quick facts.
- MIT validation gate report `qa/reports/mit-validation-gate-2026-07-09.json`: status passed, required field completeness 100%, JSON schema validation passed, URL legal rate 100%, cross references passed, MIT reconciliation passed.
- MIT diff gate report `qa/reports/mit-diff-gate-2026-07-09.json`: status unchanged, change_count 0, publishable true.
- Five-school local MVP data now exists under `data/normalized` for `berkeley`, `harvard`, `mit`, `princeton`, and `stanford`.
- Four structured raw school seed files were added under `data/raw-md`:
  - `data/raw-md/berkeley.md`
  - `data/raw-md/harvard.md`
  - `data/raw-md/princeton.md`
  - `data/raw-md/stanford.md`
- Batch reports passed for the current five-school data root:
  - `qa/reports/all-validation-gate-2026-07-09.json`: 5/5 succeeded.
  - `qa/reports/all-diff-gate-2026-07-09.json`: 5/5 succeeded.
  - `qa/reports/all-index-gate-2026-07-09.json`: 5/5 succeeded.
  - `qa/reports/all-weknora-sync-gate-2026-07-09.json`: 5/5 succeeded.
- Generic structured adapter tests passed:
  - Single-school `parse_school_markdown(..., adapter_name="generic_structured")` outputs schema-valid `source_registry/catalog_entries/url_manifest/quick_facts`.
  - Batch `parse-school --all --default-adapter generic_structured` can parse an unknown structured school while default unknown-school parsing still fails.
- Multi-school UAT builder tests passed:
  - Five structured-school fixtures generated balanced single-turn and conversation QA cases with explicit `university_id`.
  - `mvp_scope_gate.evaluate_mvp_scope` passes against the five-school fixture and synthetic successful batch reports.
  - `KnowledgeStore.resolve_university` resolves a non-MIT generic school alias from catalog `search_text`.
- Human QA review gate tests passed:
  - Missing review file reports `status=not_ready`.
  - Passing human reviews pass the gate.
  - P0 incorrect reviews block release.
  - Low-score or flagged reviews require a valid `failure_category`.
- Release artifact generator tests passed:
  - Groups release failures by gate.
  - Counts human review failure categories.
  - Writes acceptance, QA, and failure-analysis Markdown.
- MVP scope gate report `qa/reports/mvp-scope-gate-2026-07-09.json`: status passed.
  - Normalized school count: 5.
  - UAT single-turn cases: 200 across 5 schools, route distribution `catalog=60`, `fact=60`, `deep=50`, `clarification=30`.
  - UAT conversation cases: 50 across 5 schools, route distribution includes `catalog`, `fact`, `deep`, and `clarification`.
  - MCP/tool calling cases: 12.
- Postgres loader dry-run: validated MIT counts and table mapping.
- Live Postgres container from `infra/docker-compose.yml` is healthy on `127.0.0.1:5432` at handoff time.
- Live OpenSearch container from `infra/docker-compose.yml` is healthy on `127.0.0.1:9200` at handoff time.
- Live Postgres migrations applied successfully: `001_initial_schema.sql`, `002_ingestion_staging.sql`.
- Live Postgres/OpenSearch data gate now supports `--data-root` and passed for all 5 normalized schools, writing `qa/reports/live-data-gate-2026-07-09.json`:
  - `berkeley`: 14 source registry, 12 catalog entries, 14 URL manifest, 12 quick facts.
  - `harvard`: 12 source registry, 12 catalog entries, 12 URL manifest, 12 quick facts.
  - `mit`: 107 source registry, 157 catalog entries, 107 URL manifest, 241 quick facts.
  - `princeton`: 16 source registry, 12 catalog entries, 16 URL manifest, 12 quick facts.
  - `stanford`: 15 source registry, 12 catalog entries, 15 URL manifest, 12 quick facts.
  - Per-school OpenSearch current aliases were published and count-verified for catalog entries, URL manifest, and quick facts.
- `infra/postgres/003_weknora_import_job_ids.sql` has been applied in the live Postgres container.
- Current MIT normalized `source_registry.crawl_status` values are schema-valid `success` for all 107 sources.
- Previous Postgres-only gate report remains at `qa/reports/live-postgres-gate-2026-07-09.json`.
- QA report persistence to live Postgres verified:
  - `qa_cases`: 30
  - current run reviews: 30
  - total `qa_reviews`: 60 because two automated runs now exist.
  - Report written to `qa/reports/live-qa-postgres-gate-2026-07-09.json`.
- WeKnora mock sync: 107 imported, 0 failed.
- WeKnora changed-only sync after import: 0 imported, 107 skipped, 0 failed.
- WeKnora import worker local mock report wrote `qa/reports/weknora-import-worker-2026-07-09.json`: status success, sync skipped 107, poll skipped 107.
- WeKnora real import, status polling/retry, and scoped search adapter unit tests passed with mocked HTTP transport; no live WeKnora API has been verified.
- External readiness report wrote `qa/reports/live-readiness-gate-2026-07-09.json`: status `not_ready` because real WeKnora, L0, Langfuse, and external Agent `/mcp-sdk` env/config are not present in the current local environment.
- External live smoke report wrote `qa/reports/external-live-smoke-2026-07-09.json`: status `not_ready` because real WeKnora, L0, and Langfuse env/config are not present in the current local environment. This gate now checks WeKnora import/status/search, L0 resolve, and Langfuse ingestion at business level once configured.
- External Agent smoke report wrote `qa/reports/external-agent-smoke-2026-07-09.json`: status `not_ready` because `TOOL_GATEWAY_MCP_SDK_URL` is not configured in the current local environment.
- Human QA review gate report wrote `qa/reports/human-qa-review-gate-2026-07-09.json`: status `not_ready` because `qa/human-reviews.jsonl` has not been provided yet. This is now a release-blocking gate for the full profile.
- MIT-only human QA review gate report wrote `qa/reports/human-qa-review-mit-gate-2026-07-09.json`: status `not_ready` because `qa/human-reviews.jsonl` has not been provided yet. It evaluates `qa/mit-gold-cases.jsonl` and `qa/mit-uat-conversations.jsonl`, requiring at least 30 reviewed MIT cases and 3 reviewed MIT conversations.
- Aggregate full-profile release gate report wrote `qa/reports/mvp-release-gate-2026-07-09.json`: status `failed`, 14 gates passed and 3 gates failed (`human_qa_review`, `external_readiness`, `external_live_smoke`).
- MIT release gate report wrote `qa/reports/mit-release-gate-2026-07-09.json`: status `failed`, 8 gates passed and 3 gates failed (`human_qa_review_mit`, `external_readiness`, `external_live_smoke`). This is the active acceptance report for the current user scope.
- Release artifacts generated:
  - `qa/acceptance-report-2026-07-09.md`: decision `NOT RELEASE READY`.
  - `qa/qa-report-2026-07-09.md`: automated QA summary plus human review gate state.
  - `qa/failure-analysis-2026-07-09.md`: current blockers grouped by gate and required next evidence, including route distribution and MCP/tool case deficits.
- MIT-only release artifacts generated:
  - `qa/acceptance-report-mit-2026-07-09.md`: decision `NOT RELEASE READY`.
  - `qa/qa-report-mit-2026-07-09.md`: MIT automated QA summary plus MIT human review gate state.
  - `qa/failure-analysis-mit-2026-07-09.md`: current MIT blockers grouped by gate and required next evidence.
- Langfuse optional ingestion unit tests passed with mocked HTTP transport; no live Langfuse project/API key has been verified.
- OpenSearch indexer dry-run: validated three per-school aliases and staging indexes.
- Fast Router runtime `/eval/run?suite_path=qa/mit-gold-cases.jsonl`: 30/30 passed.
- QA report written to `qa/reports/mit-gold-report-2026-07-09.json`.
- QA gate reports passed:
  - `qa/reports/mit-gold-gate-2026-07-09.json`: 30/30.
  - `qa/reports/mvp-uat-gate-2026-07-09.json`: 200/200.
  - `qa/reports/mvp-uat-conversations-gate-2026-07-09.json`: 50 conversations / 100 evaluated turns, 100/100.
  - `qa/reports/mit-uat-conversations-gate-2026-07-09.json`: 6/6 evaluated turns.
- MVP UAT report persistence to live Postgres verified:
  - `qa/reports/live-mvp-uat-postgres-gate-2026-07-09.json`
  - `qa_cases`: 200 persisted/upserted for the MVP UAT suite.
  - `qa_reviews`: 200 persisted/upserted for run `mvp_uat_2026_07_09`.
- MVP multi-turn UAT report persistence to live Postgres verified:
  - `qa/reports/live-mvp-uat-conversations-postgres-gate-2026-07-09.json`
  - `qa_cases`: 50 persisted/upserted for the MVP conversation suite.
  - `qa_reviews`: 100 persisted/upserted for run `mvp_uat_conversations_2026_07_09`.
  - `persist_qa_report.py` now maps `qa_case_id::turn_n` review results to their base `qa_case_id` while keeping turn-specific review IDs.
- HTTP/CLI/legacy MCP/SDK MCP consistency gate passed and wrote `qa/reports/tool-consistency-gate-2026-07-09.json`:
  - 12/12 cases passed.
  - Covered fact, catalog, deep, and clarification routes across MIT plus Stanford, Berkeley, Harvard, and Princeton smoke queries.
  - Each case called Fast Router HTTP `/fast-answer`, CLI `scripts/router_cli.py fast-answer`, Tool Gateway legacy `/mcp` `fast_university_answer`, and Tool Gateway SDK `/mcp-sdk` `fast_university_answer`.
  - Gate compares Router contract fields while allowing per-entrypoint `trace_id` differences.
- MIT-only HTTP/CLI/legacy MCP/SDK MCP consistency gate passed and wrote `qa/reports/tool-consistency-mit-gate-2026-07-09.json`:
  - 4/4 cases passed.
  - Covered MIT fact, catalog, deep, and clarification routes.
- Current full local verification:
  - Python unittest suite: 141/141 passed.
  - Tool Gateway Node tests: 7/7 passed.
  - Docker Compose config validation passed.
  - HTTP/CLI/legacy MCP/SDK MCP consistency gate: 12/12 passed.
  - MIT-only HTTP/CLI/legacy MCP/SDK MCP consistency gate: 4/4 passed.
  - External Agent MCP SDK smoke against a local Tool Gateway `/mcp-sdk`: 4/4 passed and wrote `qa/reports/external-agent-smoke-2026-07-09.json`.
- Router route/ranking regressions are covered by tests for:
  - `analytics` not being treated as `cs`.
  - `policy` in a program name not forcing deep route over catalog/fact.
  - school alias resolution preferring the earliest explicit school mention, so `MIT ... Harvard-MIT Health Sciences and Technology ...` resolves to MIT instead of Harvard.
  - yes/no high-risk program questions like Sloan MBA GRE/GMAT and Biology TOEFL going to deep, while direct EECS TOEFL fact questions remain fact.
  - `linguistics` not being treated as `cs`.
  - `microbiology` not being treated as `biology`.
  - `regular action deadline` not being confused with EA deadline.
- MCP smoke:
  - Node unit tests verify `tools/list`, tool forwarding, and unknown-tool errors.
  - Node unit tests verify SDK Streamable HTTP `/mcp-sdk` tools/list and tool calls through `@modelcontextprotocol/sdk`.
  - Live local smoke with Fast Router on `127.0.0.1:8000` and Tool Gateway on `127.0.0.1:8765/mcp` passed:
    - `tools/list` returned all 5 planned MVP tools.
    - `lookup_quick_facts` returned MIT EECS TOEFL fact with `trace_id`, answer, and evidence.

## Remaining Work

- Set `TOOL_GATEWAY_MCP_SDK_URL` to the deployed Tool Gateway endpoint and run `scripts/external_agent_smoke.py` from that environment. Local SDK smoke has passed, but the current readiness report correctly blocks an unspecified deployed endpoint.
- Optionally configure a Langfuse project and keys, then run its ingestion smoke. It is observability only and does not block MIT functional acceptance.
- Fill `qa/human-reviews.jsonl` from real QA/business review and pass the MIT-only human QA gate:
  `python3 scripts/human_qa_review_gate.py --cases-path qa/mit-gold-cases.jsonl --cases-path qa/mit-uat-conversations.jsonl --reviews-path qa/human-reviews.jsonl --min-reviewed-cases 30 --min-reviewed-conversations 3 --output-path qa/reports/human-qa-review-mit-gate-2026-07-09.json`
  Automated QA reports are not sufficient for release.

## Risks

- The supplied WeKnora key was shared in chat. Rotate it after placing a replacement in the deployment secret store; do not put it in `.env` under version control.
- A WeKnora URL becomes L2-eligible only after its remote `parse_status` reaches a success state. The adapter refuses pending/running evidence by design.
- External Agent integration remains deployment-specific until a stable Tool Gateway `/mcp-sdk` URL is available.
- Formal release still requires manual QA/UAT; deferred mode is a reporting state, not release approval.
