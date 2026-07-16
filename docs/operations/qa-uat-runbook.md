# QA/UAT Runbook

自动验收使用 `qa/retrieval-acceptance-cases.jsonl`：20 个 L1、5 个 clarification/not-found、5 个真实 L1+WeKnora case。执行五轮并比较稳定实体字段，不比较 trace、score、timing 或可变化的 chunk 排序。

```bash
.venv/bin/python scripts/retrieval_benchmark.py --runs 5
```

人工 QA 由业务用户在 Claude/Codex/Hermes 中执行。每个失败记录问题、返回 JSON、`trace_id`、预期行为和归因：parser、PostgreSQL、OpenSearch、WeKnora import、evidence scope、MCP 或交互理解。

P0 阻断：错误学校/项目证据、无证据强答、deadline/fee/test/tuition 错误、应反问却返回无关记录、HTTP 与 MCP 契约不一致。
