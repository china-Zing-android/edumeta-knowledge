# L1 + WeKnora 检索子系统总览

> 本文档是当前 **active baseline**。先前的 L0/L1/L2 Agent 平台设计见 `docs/大学数据平台Agent建设方案_v3.md`、`docs/大学数据平台Agent检索架构方案_v3.md`（已标记为 historical，不再是实现基线）。

## 定位

这是一个聚焦的 **L1 + WeKnora 检索子系统**：从大学 Markdown 增量入库，发布精确的 L1 索引，把所有提取出的 URL 导入 WeKnora 并保留可追溯关系，通过 HTTP/MCP 在一秒内返回 L1 结果。先用最小完整实现（MIT）验证，再增量验证若干所大学。

架构从第一天起就为 300+ 核心大学与 10000 非核心大学设计，但本阶段不追求全量导入。

## 数据控制平面分层

```text
PostgreSQL   = 数据控制平面（ingestion / 版本 / 来源 / 事实治理 / WeKnora job 状态），不参与查询热路径
OpenSearch   = 在线 L1 检索存储（五个全局别名，非 per-school 索引）
WeKnora      = 外部依赖，每个院校完整 MD 绑定一个当前 KB，并按 knowledge_ids 提供 scoped 页面证据
FastAPI      = ingestion + retrieval HTTP 服务（ owns 解析、发布、检索）
TS MCP Gateway = 可选 profile，向 Agent 暴露同一检索契约的 thin 转发层
```

PostgreSQL 不参与正常查询热路径；它存储权威的 ingestion、version、source、fact-review 和 WeKnora job 状态。OpenSearch 和 WeKnora 都可从权威数据和导入状态重建。

## 主链路（数据构建）

```text
学校 MD (增量上传)
  -> POST /v1/university-ingestions (multipart, 返回 202 + run_id)
  -> Markdown 提取核心 (目录条目 + 事实 + entity context + 所有 URL 规范化)
  -> staging：ingestion_run + ingestion_records (校验 / diff)
  -> 事务写新版本（不改 current_version）
  -> 发布 OpenSearch L1（五个全局别名，版本化文档 ID）
  -> 切换 school_versions.current_version（单事务）
  -> 新院校创建 KB / 同院校更新复用 KB / 显式参数切换 KB
  -> 异步 WeKnora URL import（PG 作 job queue）
```

## 主链路（检索）

```text
POST /v1/retrieve
  -> normalize request
  -> resolve local university/context（仅本地 alias index，未知 -> not_found）
  -> 本地保守 QueryPlan（discovery / fact / detail）
  -> OpenSearch L1 _msearch（目录、事实、source-scope、entity context）
  -> precision/fact/context gate
  -> discovery 与 fact hit 直接返回，WeKnora 不预取
  -> 明确 detail + L1 不足 + 已解析 source scope 时才 scoped WeKnora search
  -> evidence gate（真实 chunk + current source/version）
  -> 结构化响应
```

固定检索流使用少量保守确定性规则，只决定 discovery/fact/detail 和上下文数量；无运行时 LLM、无 L0/country/ranking fallback、无请求时重试。

## 公共契约

- **检索 API**：`POST /v1/retrieve`，响应含 `trace_id`、`mode`、`scope`、`matches`、`context`、`evidence`、`missing_slots`、`warnings`、`timings`。`matches` 是结构化目录记录或原始事实值；`context` 是 MD 投影；`evidence` 仅来自 WeKnora；**服务不生成散文答案**。
- **Ingestion API**：`POST /v1/university-ingestions`（multipart，返回 202）、`GET /v1/university-ingestions/{run_id}`；`/v1/ingestions` 仅保留兼容别名。
- **MCP 契约**：只暴露一个工具 `retrieve_university_knowledge`，输入输出与 `POST /v1/retrieve` 完全一致。Gateway 不含检索/路由/缓存/证据逻辑。

## SLO（服务等级目标）

```text
HTTP L1 p95        : < 500ms
MCP L1 p95         : < 1s
L1 + WeKnora p95   : < 3s（WeKnora 延迟目标独立于 1 秒 L1 要求）
```

Claude/Codex/Hermes 的答案生成时间不在检索 SLO 内。WeKnora 超时时返回 L1 结果并附 `warnings=["evidence_timeout"]`。

## 第一阶段保留

- 稳定 ID：`university_id`、`program_id`、`entry_id`、`source_id`、`fact_id`、`source_entry_links` 多对多关系。
- Source Registry：所有 URL 的生命周期主表（每大学内 canonical URL 唯一）。
- Fact Store：高价值事实的治理层，含 `review_status` / `conflict_status`。
- 版本发布：staging/current 双轨，失败不切 current，可回滚。
- Evidence Gate：WeKnora 证据必须真实 chunk + current source/version，且与 source_registry scope 匹配。
- MCP Gateway：可选 MCP edge，Agent 只通过 `retrieve_university_knowledge` 调用。

## 明确移除（不在第一阶段）

- L0 客户端、配置、路由、测试、readiness、文档。
- 国家级 discovery、排名、推荐、报告、跨大学指标工作流。
- Redis、MinIO、Langfuse、reranker、semantic cache、NestJS、额外向量库。
- 运行时 JSONL 检索、mock evidence fallback、per-school OpenSearch 索引。
- 检索模块内的自然语言答案生成。
- legacy stateless `/mcp`、五个独立 MCP 工具、HTTP/CLI/MCP 四入口一致性 gate。
- PostgreSQL QA 表（`qa_cases` / `qa_reviews`）、会话状态、Agent trace、报告工作流表。

## 成功定义

- MIT MD 产出 157 catalog entries，通过全部 schema/引用校验。
- 每个有效 HTTP(S) URL 在 `source_registry` 恰好出现一次（规范化后）。
- 未变更 MD 不触发 OpenSearch 发布与 WeKnora 导入；单个 URL 变更恰好创建一个受影响 WeKnora job。
- 某校更新从不改写其他学校 current 版本；失败 parse/index/import 保留旧 current。
- 精确标识符/course-code Precision@1 = 100%；手工标注 L1 Precision@5 ≥ 95%。
- warm HTTP L1 p95 < 500ms、MCP L1 p95 < 1s。
- L1 可在无 WeKnora 配置时运行；L1+WeKnora 发布需真实 WeKnora 连通性与 scope-filter 验证。
