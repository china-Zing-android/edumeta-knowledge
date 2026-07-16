# 系统架构

## 总体结构

```text
Claude / Codex / Hermes / CLI / 自研 Agent
        |  (可选：仅当走 MCP 时经过 Gateway；HTTP 客户端直连 FastAPI)
        v
TS MCP Gateway (可选 profile：retrieve_university_knowledge 转发)
        |
        v
FastAPI Retrieval Service
        |
        +--> OpenSearch L1（四个全局别名，持久 client，FastAPI lifespan 创建）
        +--> PostgreSQL 控制平面（version / source / fact / job，不参与查询热路径）
        +--> WeKnora（按 KB / knowledge_ids 服务端过滤的 scoped search）
        +--> Structured Logs（每响应记录 stage timing）
```

无 L0 adapter、无 Langfuse、无 Redis/MinIO、无 reranker。查询热路径只经过 OpenSearch（L1）与可选的 WeKnora（scoped evidence）。

## 模块职责

### TS MCP Gateway（可选）

职责：
- 仅暴露一个工具 `retrieve_university_knowledge`，输入输出与 `POST /v1/retrieve` 完全一致。
- 纯转发：不含检索、路由、缓存、证据逻辑。转发 trace ID 与结构化错误。
- 请求 timeout 略高于 Retrieval Service 的 L1/L2 预算。

不负责：
- 任何业务逻辑（精确转发即可）。

边界：
- 作为可选 Compose profile 部署；HTTP 客户端可绕过它直连 FastAPI。
- 只保留官方 MCP SDK 的 Streamable HTTP endpoint；移除 legacy SSE RPC `/mcp`。

### FastAPI Retrieval Service

职责：
- 固定检索流：normalize → resolve local university/context → OpenSearch L1 `_msearch` → precision/fact gate → L1 足够则返回 → 否则 derive source scope → scoped WeKnora search → evidence gate → 结构化响应。
- ingestion：`POST /v1/university-ingestions`（multipart，202）+ `GET /v1/university-ingestions/{run_id}`。
- 用持久 OpenSearch/WeKnora client 和显式 deadline。
- 每响应记录 stage timing（`total_ms` / `l1_ms` / `weknora_ms`）。

不负责：
- 自然语言答案生成（`matches` 是结构化目录记录或原始事实值）。
- L0 解析、country/ranking fallback。
- 请求时重试。

失败模式：
- 未知大学 → `mode=not_found`（绝不默认 MIT）。
- L1 不足且 WeKnora 超时 → 返回 L1 + `warnings=["evidence_timeout"]`。
- WeKnora 未配置 → L1-only 运行；`/health` 准确报告该状态。

### Data Pipeline（ingestion 路径）

职责：
- 解析学校 MD：统一 Markdown 提取核心（目录条目 + 事实 + 所有 URL）。
- URL 规范化与确定性 `source_id`。
- 校验 schema 与交叉引用；diff 当前版本。
- 事务写 staging → 发布 OpenSearch → 切换 current（单事务）。
- 异步 WeKnora import：每个院校完整 MD 绑定一个当前 KB，PG 作 job queue；版本切换时仅在同一 KB 内继承或续接 knowledge ID。

输出：
- `school_versions` / `ingestion_runs` / `ingestion_records` / `catalog_entries` / `source_registry` / `source_entry_links` / `fact_store` / `weknora_import_jobs`。
- OpenSearch 四个全局别名的版本化文档。

### PostgreSQL

职责：
- 数据控制平面：版本发布、来源生命周期、事实治理、WeKnora job 状态。
- 每 university 内 canonical URL 唯一约束；外键、状态枚举/check、current-version 完整性。
- WeKnora job queue（`FOR UPDATE SKIP LOCKED`）。

不负责：
- 全文检索主路径（那是 OpenSearch 的职责）。

### OpenSearch

职责：
- L1 在线检索：四个全局别名 `l1_universities_current` / `l1_catalog_entries_current` / `l1_quick_facts_current` / `l1_sources_current`。
- 版本化文档 ID（含 university + dataset_version + 稳定 entity ID），新旧版本发布期可共存。
- 一次 L1 请求做 `_msearch`：精确 ID/course_code、目录 BM25（字段 boost + 过滤）、事实查找（fact type/review status 过滤）、source-scope。

不负责：
- 事实权威存储、URL 生命周期治理（那是 PostgreSQL 的职责）。
- 运行时 JSONL 加载（测试除外，禁止）。

### WeKnora

职责：
- 新院校默认从 `WEKNORA_KB_TEMPLATE_ID` 克隆配置并创建 KB；同院校更新复用 `universities.weknora_knowledge_base_id`。
- 每个 source/job 保存实际 KB ID。检索按 KB 分组，并由 L1 选出的 `knowledge_ids` 限定搜索。
- `WEKNORA_KNOWLEDGE_BASE_ID` 只保留旧数据/兼容 fallback，不再作为唯一运行时 KB。
- URL 抓取与页面内容知识库化。
- scoped 检索：hybrid-search 支持 `knowledge_ids` 服务端过滤（已通过 capability test 验证）。

不负责：
- 目录主数据、事实权威治理。
- 是否可用于回答的最终判断（Evidence Gate 负责）。
