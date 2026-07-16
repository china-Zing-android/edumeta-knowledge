# Agent 工具架构

## 边界

Claude、Codex、Hermes、自研 Agent 只能通过 MCP `retrieve_university_knowledge`（经可选 TS Gateway）或直接 HTTP `POST /v1/retrieve` 调用能力。

禁止 Agent 直连：
- OpenSearch。
- PostgreSQL。
- WeKnora。

## MCP 工具（仅一个）

```text
retrieve_university_knowledge
```

- 输入输出与 `POST /v1/retrieve` **完全一致**。
- TS Gateway 是 thin 转发层：不含检索、路由、缓存、证据逻辑，只把请求转发给 Retrieval Service，并把 trace ID 与结构化错误原样转发。
- 请求 timeout 略高于 Retrieval Service 的 L1/L2 预算。

**已移除**（不再暴露）：

```text
fast_university_answer      # 旧 L0 路由
deep_university_search      # 旧 L0 路由
search_catalog_entries      # 被统一检索吸收
lookup_quick_facts          # 被统一检索吸收
find_url_scope              # 被 source-scope 阶段吸收
```

## MCP Transport

仅保留官方 MCP SDK 的 **Streamable HTTP endpoint**。

**已移除**：
- legacy stateless JSON-RPC over SSE `/mcp`。
- HTTP/CLI/legacy MCP/SDK MCP 四入口一致性 gate。

## 工具返回结构

```text
trace_id
mode          (l1 | l1_l2 | clarification | not_found | error)
scope         {university_id, dataset_version}
matches
evidence
missing_slots
warnings
timings       {total_ms, l1_ms, weknora_ms}
```

Agent 自行决定如何把 `matches` / `evidence` 组织成自然语言答案（答案生成在检索模块之外）。

## Agent Prompt/Profile 建议

- 事实/目录类问题调用 `retrieve_university_knowledge`，从 `matches` 取结构化记录。
- 需要页面证据时依赖 `mode=l1_l2` 的 `evidence`（真实 chunk + current source/version）。
- `review_required` 事实或 `conflict_status` 不可作为 confirmed 结论。
- 不允许基于模型常识回答 deadline、fee、test、tuition。

## Smoke Test

MCP smoke test 至少覆盖：
- 精确目录命中（mode=l1）。
- 事实查找与 review/conflict 标记。
- L1+WeKnora 证据（mode=l1_l2）。
- 未知大学（mode=not_found）。
- WeKnora 超时降级（warnings 含 evidence_timeout）。

通过标准：
- 每次调用有 `trace_id`；响应含 `timings`；工具失败有结构化错误。
- MCP 响应与 HTTP `POST /v1/retrieve` 契约一致。
