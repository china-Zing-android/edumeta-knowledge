# MCP Tool Contract

Endpoint: `POST /mcp` (Streamable HTTP)

唯一工具：`retrieve_university_knowledge`

输入：

```json
{
  "query": "MIT Course 6-3 本科专业是什么？",
  "university_id": "mit",
  "direction": "auto",
  "filters": {
    "country_codes": [],
    "regions": [],
    "degree_levels": [],
    "levels": [],
    "school_tiers": []
  },
  "context": {"level": "undergraduate", "program_id": null, "entry_id": null},
  "max_results": 5
}
```

输出与 `POST /v1/retrieve` 完全一致，包含 `trace_id`、`mode`、`scope`、`matches`、`context`、`evidence`、`missing_slots`、`warnings`、`timings`。

`context` 是 MD 物化投影，始终为对象，包含 `primary_entities`、`highlights`、`sample_children`、`related_entities`、`available_topics`、`presentation_hints` 和 `provenance`。它不是 WeKnora evidence；`available_topics` 只表示后续可查询，不表示已经执行深检索。

Agent 呈现顺序固定为：直接回答 -> 必要上下文 -> 少量相关实体 -> 可继续探索主题。Course 编号必须与可读名称一起展示，例如 `14-2 Mathematical Economics`，不能只展示裸编号。多轮 scope 由 Agent 保持并在下一次 `context.entry_id/program_id/level` 中回传，Fast Router 不保存会话。

`direction` 支持 `auto/downward/range/upward`。`range/upward` 只搜索已入库院校，返回聚合后的院校和命中专业，不执行院校排名，也不调用 WeKnora。

禁止暴露原始 PostgreSQL、OpenSearch 或 WeKnora 查询工具。
