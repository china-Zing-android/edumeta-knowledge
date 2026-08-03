Status: testing

# Markdown 更新管理端 Handoff

## Goal

Implement an internal React and FastAPI control plane for Markdown ingestion, queue monitoring, raw and normalized artifact inspection, quality-gated force publish, L1 rollback, and optional WeKnora import.

## Current decision

- Add `apps/md-admin` as a standalone Vite React app using Carbon React primitives and a low-card, row-and-split-pane workbench layout.
- Keep the existing Markdown ingestion endpoints compatible with CLI callers.
- Add persistent batch metadata and queue scheduling around `ingestion_runs`; default ingestion concurrency remains 2.
- Normal uploads allow at most 20 Markdown files and 20 MiB per file. Server directory scans recurse without a file-count limit, but must pass preview validation.
- Same-batch duplicate `university_id` mappings are blocked with an impact explanation.
- `needs_review` can be force-published only after a reason and second confirmation. Parser/schema/empty-data failures cannot be force-published.
- Rollback restores PostgreSQL current state, OpenSearch current documents, and the Fast Router version cache. It does not delete or automatically re-import WeKnora documents.
- WeKnora import is disabled when the backend feature/configuration is unavailable. L1 remains publishable and the UI distinguishes disabled from failed imports.
- Current and failed artifacts are retained; superseded successful artifacts are retained for 90 days and are rollback-capable during that window.

## Relevant files

- `apps/fast-router/src/fast_router/main.py`
- `apps/fast-router/src/fast_router/ingestion.py`
- `pipelines/catalog-parser/src/catalog_parser/postgres_loader.py`
- `pipelines/indexer/src/indexer/opensearch_publisher.py`
- `infra/postgres/`
- `apps/md-admin/`
- `pipelines/catalog-parser/src/catalog_parser/diff.py`
- `infra/postgres/011_admin_ingestion_control_plane.sql`

## Verification

- Existing worktree changes are unrelated QA changes in `scripts/retrieval_benchmark.py`, its test, and `qa/`; preserve them.
- `npm run typecheck` passes in `apps/md-admin`.
- `npm run build` passes in `apps/md-admin` with Carbon/Vite production output.
- `docker compose -f infra/docker-compose.yml -f compose.server.yaml config --quiet` passes.
- Full Python suite passes with loopback binding allowed: `241 passed, 7 skipped, 15 subtests passed`.
- `tests/test_admin_control_plane.py` covers the 20-file limit, exact 20 MiB boundary, and duplicate-university impact blocking.
- `python3 -m compileall` passes for Fast Router, parser, and indexer modules.
- `git diff --check` passes.

## Current implementation

- `AdminControlPlane` now supports upload/directory previews, manifest or filename/title inference, duplicate-university blocking with explicit impact scope, per-item rejected batch records, artifact paging/download, schema docs, diff summaries, force publish, rollback, and explicit WeKnora current-version reimport.
- `IngestionService` persists `accepted` queue rows, claims them with database locking, resumes accepted work after restart, keeps 20 MiB validation, persists WeKnora preparation errors without blocking L1, and stores compact diff summaries for retention.
- WeKnora disabled or misconfigured runs create no import jobs and surface disabled state; enabled import failures surface `L1 已发布，WeKnora 部分失败` without L1 rollback.
- `apps/md-admin` is a Carbon React/Vite workbench with low-card row/split layout, raw search with line numbers, JSONL paging, force-publish/rollback confirmations, version history, explicit reimport, schema guide, and responsive keyboard-friendly controls.
- Added `GET /v1/admin/source-files` so configured server Markdown files are visible before preview/submit. The UI now separates `服务器源文件` from `已提交运行记录`, labels unsubmitted files explicitly, links submitted files to online inspection, and can open the source file's directory scan flow.
- The Fast Router container now mounts the complete `data/raw-md` tree at `/app/data/raw-md`. Source-root discovery prefers `/app/data/raw-md/universities` when present and otherwise scans `/app/data/raw-md`, with `INGESTION_SOURCE_ROOT` available as an explicit override.
- Source discovery now falls back from exact `source_relative_path` matching to the newest university run for legacy imports created before source-path fields existed.
- Added `GET /v1/admin/versions` and a top-level `版本历史` page that reads `school_versions` directly, including versions that have no linked run or source filename.
- Reframed `source_registry` as the URL/source master record and `url_manifest` as a compatibility association projection. The UI now explains that the MIT URL rows are one-to-one and PostgreSQL folds the projection into `source_registry`; the retrieval guide shows query and skip paths instead of implying all five JSONL files are queried together.
- Compose wiring exposes Fast Router and the admin UI on loopback plus the configured Tailscale host.

## UI follow-up delivered

- Desktop left navigation is fixed below the top bar and remains visible while the main content scrolls; mobile keeps a compact sticky navigation strip.
- Renamed the primary entry from `更新工作台` to `更新院校` and removed the `L1 / L2` plus `内部网络` header metadata.
- Added a dedicated `已上传文件` page with search, status filtering, row-level stage/error details, and an explicit `在线查看` action.
- Reworked `运行批次` into a list with file, accepted, published, failed, WeKnora-disabled, status, and update-time columns.
- `已上传文件` now groups both server source files and submitted runs by country plus region, with a region filter for each list. Missing regions fall back to `country · 未细分地区` or `未分区` and remain visible.
- Source metadata now reads Markdown metadata declarations and falls back to existing university metadata when `manifest.jsonl` has no region. Run status responses include university name, country code, and region for consistent grouping.
- Online artifact inspection now announces raw/JSONL viewing, loads 80 lines or records per page, and exposes previous/next pagination alongside download links.
- JSONL documentation now renders all schema fields with required markers, type, description, MIT examples, a copyable annotated JSONC minimum structure, and a retrieval flow for “mit里有哪些计算机相关的学科”.

## UI verification

- `apps/md-admin`: `npm run typecheck` passed.
- `apps/md-admin`: `npm run build` passed.
- Region inference tests, `tests.test_admin_control_plane`, and `tests.test_fast_router_api` passed after the region grouping change.
- `python3 -m compileall` passed for the updated admin and ingestion modules.
- `tests/test_admin_control_plane.py`: source files are returned as `not_submitted` before an ingestion run exists.
- `tests/test_fast_router_api.py`: `/v1/admin/source-files` contract passed.
- Legacy-run source association and global version-catalog API tests passed.
- `docker compose -f infra/docker-compose.yml -f compose.server.yaml config --quiet` passed; the rendered server config mounts `/app/data/raw-md` and sets `INGESTION_SOURCE_PARENT=/app/data/raw-md`.
- Full Python discovery was attempted: 238 tests ran, with the existing parser test ordering failure and sandbox loopback permission errors; focused admin/API tests and Python compilation passed.
- `git diff --check` passed.

## Remaining risks

- The directory/version-history changes are currently uncommitted local worktree changes; `HEAD` and `origin/main` are still `2157d1d`, so a deployed server will not show them until the changes are committed, pushed, and the Fast Router/admin images are rebuilt.
- Admin endpoint/database integration tests and an end-to-end browser test were not run because no live PostgreSQL/OpenSearch stack or browser runner was started; static checks, focused control-plane tests, full Python tests, Compose validation, and production frontend build passed.
- The new navigation, file list, artifact pagination, and documentation flow still need a browser pass against the live server after the rebuilt `md-admin` image is deployed.
- The source-file list scans configured roots on demand and defaults to metadata-only hashes for performance. `include_hash=true` enables SHA-256 when an operator needs it.
- Cross-system OpenSearch/PostgreSQL rollback remains operationally ordered rather than a true distributed transaction; failures should be surfaced and retried through the existing run/audit path.
- `cleanup_expired_artifacts()` is implemented as an operational hook but is not scheduled by a dedicated cron/worker yet.
