# 质量闸门与验收标准

对应计划 §11 Acceptance Gates。所有 gate 的真实判断脚本在 `scripts/`；release gate 聚合下列子门。

## Data & Incremental Gate

检查项：
- MIT MD 产出 157 catalog entries，通过全部 schema 与引用校验。
- 每个有效 HTTP(S) URL 在 `source_registry` 恰好一次（规范化后）。
- 每个 catalog/fact source 关系可通过 `source_entry_links` 查询。
- 未变更 MD 不触发 OpenSearch 发布与 WeKnora 导入。
- 单个 URL 变更恰好创建一个受影响 WeKnora job。
- 某校更新从不改写其他学校 current 版本。
- 新校注册、同校更新与 unchanged 操作可区分；院校元数据进入 PostgreSQL 和 OpenSearch。
- 版本切换时非终态 WeKnora source 在新 current 版本有续接 job。
- 失败 parse/index/import 保留旧 current 学校版本。

通过标准：上述全为真。

## Retrieval Precision Gate

检查项：
- 精确标识符 / course-code Precision@1 = 100%。
- 手工标注 L1 Precision@5 ≥ 95%。
- 错误 university/program/source 的 evidence 接受数 = 0。
- 未批准或冲突事实被标为 confirmed 的数 = 0。
- 返回的 WeKnora evidence 有真实 chunk 文本与 current source/version 链接。
- range/upward 只返回已入库院校；国家、地区、学位层级、学校 tier 过滤无泄漏。
- 学科向上检索按院校聚合，且不调用 WeKnora、不产生排名语义。
- 院校/单专业/多专业 discovery 返回 MD context，Course 编号均带可读名称。
- discovery 与 Fact Store 命中请求的 `weknora_ms=0`，mock/spy WeKnora 调用次数为 0。
- 多专业 primary 最多 3 个；related 不重复 primary，且每个 primary 最多 2 个确定性关系。
- `context` 始终为对象，且不被记录为 WeKnora evidence。

通过标准：上述全部满足。低于 min score 的结果被 omit；禁止用无关结果填 top_k。

## Performance Gate

检查项：
- warm HTTP L1 p95 < 500ms。
- warm MCP L1 p95 < 1s。
- L1 + WeKnora p95 < 3s（真实服务配置后）。
- upload 与 retrieval 请求中无同步 WeKnora import。
- 每响应报告 `total_ms` / `l1_ms` / `weknora_ms`。
- MIT 本地 challenge 的 MD-first discovery/fact 请求应显著低于 1 秒；2026-07-16 实测 L1 约 20-62ms，仅作为环境基线，不替代 p95 benchmark。

通过标准：`scripts/retrieval_benchmark.py` 五次运行结果一致且达标。

## Evidence Gate

检查项：
- evidence 含 `evidence_id` / `source_id` / `source_url` / `knowledge_id` / `document_id` / `chunk_id` / `chunk_text` / `score` / `capture_date` / `dataset_version`。
- 无 scope 映射、无真实 chunk 文本、非 current source/version 的 evidence 被丢弃。
- 无本地 fact snippet 冒充 WeKnora evidence。
- WeKnora 搜索按 KB / `knowledge_ids` 服务端过滤（已 capability test 验证），并对 `source_registry` 严格二次 post-filter。

通过标准：错误学校/项目/source 的 evidence 通过率 = 0。

## Deployment Gate

检查项：
- Core Compose（postgres + opensearch + fast-router）启动健康。
- MCP profile（编译后的 TS Gateway）启动健康。
- `/health` 分别报告 PostgreSQL、OpenSearch aliases、WeKnora 配置、current-version cache 状态。
- L1 可在无 WeKnora 配置时运行；L1+WeKnora 发布需真实 WeKnora 连通性与 scope-filter 验证。
- 活跃部署中无 L0 / Redis / MinIO / Langfuse / mock evidence / 运行时 JSONL 依赖。

通过标准：`scripts/release_gate.py` 输出 `status=passed`；**运行时 JSONL / mock evidence 路径启用时阻断 release**。

## QA Gate（真人客观）

检查项：
- 30 个手工标注 case：15 L1 + 10 L1+WeKnora + 5 clarification/not_found。
- 包含手工 Claude QA session 发现的所有 failure。
- field-aware evaluation（排除 trace_id 与随机 metadata）。
- suite 跑五次结果完全一致。

通过标准：
- 上述全通过。
- 用真人客观 QA 验证检索效果（测试阶段准备）。

## 已移除的 gate

下列 gate 不再存在（对应已移除的能力）：
- L0 readiness gate（无 L0）。
- Langfuse trace sink gate（无 Langfuse）。
- HTTP/CLI/legacy MCP/SDK MCP 四入口一致性 gate（仅一个 MCP 工具 + HTTP）。
- MVP 5 校 UAT scope gate（先 MIT，再增量验证若干所）。
- PostgreSQL QA 表相关 gate（`qa_cases` / `qa_reviews` 已移除）。
