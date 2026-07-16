# 增量更新设计

## 更新粒度

系统必须支持四级增量：

```text
school-level
program-level
source-url-level
fact-level
```

最小实际更新粒度是 `source-url-level`。

## 单 URL 更新链路

```text
source_url changed
  -> source_registry diff
  -> trigger WeKnora URL re-import
  -> update url_manifest import metadata
  -> update affected facts
  -> update OpenSearch docs
  -> run affected eval subset
  -> publish if gates pass
```

## Diff 状态

```text
added
changed
unchanged
removed
conflict
```

规则：
- `unchanged` 不重导 WeKnora，不重写 OpenSearch。
- `removed` 标记 `deprecated/inactive`，不物理删除。
- `conflict` 进入 `review_required`，不能自动发布为权威事实。
- `diff-school` 对 active 记录的物理删除直接失败；删除必须以 `inactive/deprecated/superseded` tombstone 形式保留。

## Hash 策略

至少维护：
- `content_hash`：URL 或导入内容 hash。
- `normalized_record_hash`：parser 输出标准化记录 hash。
- `source_version`：单 source 版本。
- `dataset_version`：学校数据批次版本。

`normalized_record_hash` 不包含 WeKnora import metadata、crawl/import status、capture/dataset version 等运行态字段，避免 URL import 状态变化误触发 parser 增量。事实 `raw_value/normalized_value`、URL、entry、source scope 等业务字段变化必须触发 diff。

## Diff Gate

命令：

```bash
PYTHONPATH=pipelines/catalog-parser/src python3 -m catalog_parser.cli diff-school \
  --university-id mit \
  --previous-data-dir data/normalized/mit.previous \
  --data-dir data/normalized/mit \
  --output-path qa/reports/mit-diff-gate-2026-07-09.json
```

输出必须包含：

```text
entities.*.added_ids
entities.*.changed_ids
entities.*.removed_ids
entities.*.removed_active_ids
affected.source_ids
affected.entry_ids
affected.fact_ids
affected.url_ids
weknora_reimport_source_ids
single_source_update
publishable
```

通过标准：
- `removed_active_ids` 为空。
- 单 URL 更新时 `single_source_update=true`，且 `weknora_reimport_source_ids` 只包含受影响 source。
- 事实变更只影响 `affected.fact_ids/source_ids`，不触发 WeKnora 重导，除非 source/url scope 同时变化。

## 禁止事项

- 不允许为了单 URL 更新重建整校，除非 source scope 明确扩大。
- 不允许直接覆盖 current index。
- 不允许物理删除旧 source/fact/entry。
- 不允许 parser 修改导致稳定 ID 全量变化。

## 300 校扩展路径

多学校目录结构：

```text
data/raw-md/{university_id}.md
data/normalized/{university_id}/source_registry.jsonl
data/normalized/{university_id}/catalog_entries.jsonl
data/normalized/{university_id}/url_manifest.jsonl
data/normalized/{university_id}/quick_facts.jsonl
qa/{university_id}-gold-cases.jsonl
```

批量准备命令：

```text
parse-school --all --input-root data/raw-md --out-root data/normalized
validate-school --all --data-root data/normalized
diff-school --all --previous-data-root data/normalized.prev --data-root data/normalized
```

生产导入不执行 JSONL WeKnora 同步命令。每所学校通过 `POST /v1/university-ingestions`
上传 MD；Fast Router 在 PostgreSQL 中完成版本化入库与 OpenSearch 发布，并只为
新增或变化 URL 创建 `weknora_import_jobs`。内置 worker 异步导入和轮询，旧版本
未完成 job 在版本切换时标记为 `superseded`。

版本切换时，已成功 URL 直接继承 WeKnora 标识；未完成 URL 在新 current 版本创建续接 job，携带原 `knowledge_id` 继续轮询，避免 source 状态失去对应 job。

继承条件包含 `canonical_url + weknora_knowledge_base_id`。显式切换到另一个 KB 时不得继承旧 KB 的 knowledge/document/chunk ID，所有 current URL 在目标 KB 重新导入。

新增学校要求：
- 如果 MD 符合结构化通用契约，批量解析时显式使用 `--default-adapter generic_structured`。
- 如果 MD 是特殊格式，先在 parser adapter registry 中注册 `university_id -> parser`。
- 新 adapter 必须输出同一组 `source_registry/catalog_entries/url_manifest/quick_facts` schema。
- 新 adapter 不得修改 CLI 主链路、Source Registry、Fact Store、OpenSearch mapping 或 MCP tool contract。
- 如果原始 MD 格式不同，只允许在 adapter 内部处理格式差异。
