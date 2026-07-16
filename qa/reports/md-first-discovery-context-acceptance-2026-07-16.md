# MD-First Discovery Context Challenge 验收报告

日期：2026-07-16

## 结论

状态：**passed**。

本挑战完成了长期架构中的最小稳定切片：新增版本化 `entity_contexts` 投影与第五个 OpenSearch alias；Fast Router 对院校、单专业和多专业 discovery 返回 MD context；Fact Store 命中不调用 WeKnora；只有明确 detail 且 source scope 已解析时才执行 scoped WeKnora。MCP 仍只有一个 TypeScript 工具，Gateway 无业务逻辑。

## 自动验收

- Python：`171 passed`、`11 subtests passed`；仅有现存 Starlette/httpx deprecation warning。
- TypeScript Gateway：typecheck、build、`8/8` tests passed。
- HTTP challenge：9 cases × 5 runs，失败 `0`，非确定性 case `0`；新增 `entry_id` 多轮 Economics curriculum scope。
- HTTP L1：p50 `19.698ms`，p95 `65.725ms`。
- HTTP L1 + WeKnora：p95 `692.024ms`。
- Upward：p95 `14.039ms`。
- MCP：50 runs，p50 `15.365ms`，p95 `32.750ms`，max `51.659ms`。
- WeKnora disabled：6 discovery/fact cases × 5 runs，失败 `0`，L1 p95 `25.897ms`。
- Runtime：PostgreSQL、OpenSearch、Fast Router、Tool Gateway 全健康；5 个 current schools；5 个 aliases；169/169 current sources import success；169/169 success job audit 完整。

## 数据与 Evidence

- MIT：157 catalog entries、241 quick facts、158 entity contexts。
- 新 MIT KB `1b91fcff-ce72-4e97-9de0-f23a8ba419d9`：112/112 URL knowledge 与 manifest canonical URL 完整映射。
- EECS materials challenge 只返回 EECS graduate source，包含真实 chunk、knowledge/document/chunk ID。
- Discovery 与 L1 fact case 的 `weknora_ms=0`；`context` 未伪装为 evidence。
- 多轮 `context.entry_id` 在 source index 查询阶段直接使用 `entry_ids` filter；“那课程设置呢？”只返回 Economics 14-1 degree-chart evidence。

## 增量隔离

- Context-only diff 可发布，但 `weknora_reimport_source_ids=[]`。
- PostgreSQL 集成测试改为只清理 fixture university，不再 drop 共享 Compose 表；tearDown 后不残留测试学校。
- `scripts/backfill_weknora_success_jobs.py` 可幂等恢复已有 source 的 success job；runtime gate 阻断缺失审计的 current source。
- 根目录 `.env` 已使用 `.gitignore` 排除并设为本机私密配置；Compose 使用 `--env-file .env` 重建后 WeKnora 配置仍存在。
- 当前控制面只保留 MIT、Stanford、Harvard、Princeton、Berkeley 五个 current schools。

## 人工评审边界

当前 MIT MD 没有 14-1 Economics 的课程细节、项目优势、就业结果或适合人群等定性内容。首答可以提供 `14-1 Economics`、SB、Economics department、所属学院、`14-2`/`6-14` 确定性关系和可继续主题，但不得生成无来源“更数学”“更适合某类学生”“就业更好”等评价。

人工评审 key：`qa/manual/discovery-context-challenge-review-key.md`。

## 证据文件

- `qa/reports/md-first-discovery-context-final-v2-2026-07-16.json`
- `qa/reports/md-first-discovery-no-weknora-2026-07-16.json`
- `qa/reports/mcp-benchmark-post-audit-2026-07-16.json`
- `qa/reports/runtime-compose-post-audit-final-2026-07-16.json`
