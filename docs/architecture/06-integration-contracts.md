# 集成契约

## HTTP

```text
POST /v1/retrieve
POST /v1/university-ingestions
GET  /v1/university-ingestions/{run_id}
GET  /health
```

`/v1/retrieve` 只返回结构化 `matches/context/evidence/missing_slots/warnings/timings`，不生成自然语言答案。`context` 始终为对象且来自 MD 物化投影；`evidence` 仅来自 scoped WeKnora。允许模式为 `l1`、`l1_l2`、`range`、`upward`、`clarification`、`not_found`、`error`。

Discovery 请求（院校、专业、多专业关系、“怎么样/介绍”）不得调用 WeKnora。事实请求先查 `quick_facts`；只有明确 detail 或 fact miss、且实体与 source scope 均已解析时才允许 WeKnora。`review_required/conflict` 事实返回原始值和 warning，不自动核验。

`POST /v1/university-ingestions` 使用 multipart：必填 `university_id`、`school_tier`、Markdown `file`，可选 `university_name`、`country_code`、`region`、逗号分隔 `aliases`、`weknora_knowledge_base_id`、`create_new_weknora_kb`。返回 202 和 `operation=create|update|unchanged`，不等待 URL 导入完成。`weknora_knowledge_base_id` 与 `create_new_weknora_kb=true` 互斥。`/v1/ingestions` 是兼容别名。

## WeKnora

```text
POST /api/v1/knowledge-bases/{kb_id}/knowledge/url
GET  /api/v1/knowledge/{knowledge_id}
POST /api/v1/knowledge-bases/{kb_id}/hybrid-search
```

新院校默认创建独立 KB；同院校更新复用绑定 KB。导入携带学校 tag。检索按 source 的 KB ID 分组，每个请求必须发送 L1 解析得到的 `knowledge_ids`；远端服务端限定后，本地再次按 source、学校和 dataset version 过滤。禁止跨 KB 全局 top-k 后仅做客户端过滤。

## MCP

Tool Gateway 仅提供 Streamable HTTP `/mcp` 和一个工具：`retrieve_university_knowledge`。其输入输出与 `/v1/retrieve` 一致并原样透传 `context`，Gateway 不包含检索、缓存、会话或路由逻辑。
