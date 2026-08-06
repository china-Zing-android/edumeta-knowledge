Status: done

# Markdown–JSONL 来源映射 Handoff

## Goal

让 `catalog_entries` 和 `quick_facts` 的检索结果能够回到同一份 Markdown 快照的精确行范围，并在管理端展示 JSONL、字段来源、Markdown 原文和校验状态。

## Current decision

- Markdown 是业务事实的唯一输入；JSONL 继续作为结构化检索产物。
- 新增独立 `provenance.jsonl` 旁车道，不把大段原文复制进业务 JSONL 或 OpenSearch。
- 每条映射绑定 `university_id`、`dataset_version`、MD SHA-256、JSONL 实体/记录 ID、原文行范围和字段来源类型。
- 字段来源分为 `direct`（原文直接读取）、`derived`（固定规则推导）和 `system`（运行时状态）。
- L1 JSONL 结果可以标记为 MD-derived；WeKnora 结果必须单独标记为外部官网证据。
- 管理端通过 provenance endpoint 展示 JSONL 记录、字段来源、Markdown 高亮行和核验状态。
- 不承诺抽象的“100% 正确”；发布门禁固化为 100% 可追溯、100% 版本一致、100% 可复现、无映射不得发布。
- 当前工作区仍有与本任务无关的未提交 QA/admin 改动，未回退或覆盖这些文件。

## Relevant files

- `pipelines/catalog-parser/src/catalog_parser/mit_parser.py`
- `pipelines/catalog-parser/src/catalog_parser/deep_v2_parser.py`
- `pipelines/catalog-parser/src/catalog_parser/structured_markdown_parser.py`
- `apps/fast-router/src/fast_router/ingestion.py`
- `apps/fast-router/src/fast_router/retrieval.py`
- `apps/fast-router/src/fast_router/admin.py`
- `apps/md-admin/src/App.tsx`
- `apps/md-admin/src/api.ts`
- `apps/md-admin/src/styles.css`
- `tests/test_provenance.py`
- `tests/test_traceability.py`
- `tests/test_admin_control_plane.py`
- `tests/test_fast_router_api.py`

## Verification target

- Every published catalog/fact record has a valid provenance mapping.
- Mapping MD hash equals the stored `input.md` snapshot hash.
- Direct field values match the mapped Markdown row after the parser's documented cleanup.
- Retrieval output exposes a compact verified/unavailable/mismatch state.
- Admin UI can show the JSONL record beside the highlighted Markdown lines.
- Admin artifact browsing resolves JSONL files from the run's `normalized/` snapshot and bundles them with the same layout.

## Verification

- `.venv/bin/python -m pytest tests/test_provenance.py tests/test_traceability.py tests/test_admin_control_plane.py tests/test_fast_router_api.py tests/test_discovery_context_retrieval.py tests/test_cross_university_retrieval.py -q` → 57 passed, 1 warning, 4 subtests passed.
- `apps/md-admin`: `npm run typecheck` → passed.
- `apps/md-admin`: `npm run build` → passed.
- `git diff --check` → passed.
- MIT parser sample: `catalog_entries=157`, `quick_facts=241`, `provenance mappings=398`, `unmapped=0`, `review_required=3`.

## Known limitations

- Existing release runs without `normalized/provenance.jsonl` show “没有来源映射” until re-ingested.
- `entry_id` currently includes some program name values, so explicit stable Markdown anchors may be a later follow-up for rename tracking.
- WeKnora evidence remains intentionally separate from Markdown-derived provenance.
