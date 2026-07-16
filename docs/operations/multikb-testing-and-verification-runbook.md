# 多院校 L1 + WeKnora 测试与验收操作手册

## 1. 验证目标

本手册分别验证三个层次：

1. HTTP 检索层是否返回正确的结构化 `matches/evidence`。
2. MCP + Agent 是否正确传参，并且没有篡改或虚构检索结果。
3. 增量 MD 是否完成解析、PostgreSQL 入库、OpenSearch 发布、URL 提取、WeKnora 独立 KB 导入与关联。

人工题卷与答案分开：

- `qa/manual/multikb-qa-question-sheet-v1.md`
- `qa/manual/multikb-qa-review-key-v1.md`
- MIT 深度题补充：`qa/manual/mit-qa-question-sheet-v1.md`

## 2. 启动与健康检查

在项目根目录执行：

```bash
docker compose --env-file .env -f infra/docker-compose.yml --profile mcp up -d --build
docker compose -f infra/docker-compose.yml ps
curl -fsS http://127.0.0.1:8000/health
curl -fsS http://127.0.0.1:8765/health
```

必须满足：

- `postgres`、`opensearch`、`fast-router`、`tool-gateway` 全部 healthy。
- Router 返回 `status=ok`。
- `weknora.configured=true`、`worker_alive=true`、`worker_last_error=null`。
- Gateway 返回 `status=ok`。

查看故障日志：

```bash
docker compose -f infra/docker-compose.yml logs --tail=200 fast-router
docker compose -f infra/docker-compose.yml logs --tail=200 tool-gateway
```

不要在测试记录、截图或提交文件中暴露 `.env` 内的 WeKnora API Key。

## 3. Claude/Codex MCP 配置

```json
{
  "mcpServers": {
    "edumeta-local": {
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

重启 Agent 会话后确认：

1. `edumeta-local` 已连接。
2. 工具列表只有本模块的高层工具 `retrieve_university_knowledge`。
3. 告诉 Agent：“本轮所有院校问题必须调用 edumeta-local，不要用模型常识补事实；保留引用和 trace_id。”

Agent 测试不能替代 HTTP 测试。若 HTTP 正确而 Agent 回答错误，归因到 MCP 参数选择或 Agent 表达；若 HTTP 已错，归因到检索链路。

### 3.1 Codex 全局绑定

在终端执行：

```bash
codex mcp add edumeta-local --url http://127.0.0.1:8765/mcp
codex mcp get edumeta-local --json
```

为避免只读检索工具在非交互测试中等待人工审批，在 `~/.codex/config.toml` 中保留：

```toml
[mcp_servers.edumeta-local]
url = "http://127.0.0.1:8765/mcp"
enabled_tools = ["retrieve_university_knowledge"]
default_tools_approval_mode = "approve"

[mcp_servers.edumeta-local.tools.retrieve_university_knowledge]
approval_mode = "approve"
```

新增 MCP 后开启新的 Codex 任务或 CLI 会话。当前已经打开的任务不作为热加载验证依据。

Codex CLI smoke：

```bash
codex exec --ephemeral --skip-git-repo-check --sandbox read-only \
  -C /Volumes/Disk/jishu/PycharmProjects/edumeta-knowledge \
  '必须调用 edumeta-local MCP 的 retrieve_university_knowledge 工具，参数 university_id=mit，query="MIT 有 Economics 本科专业吗？"。不要使用网页或终端检索。最后只输出 mode、首个 match 的 program_name/course_code、trace_id、total_ms。'
```

2026-07-16 实测结果：`mode=l1`、`Economics / 14-1`、`total_ms=28.396`。

## 4. HTTP 基线测试

### 4.1 单院校向下检索

```bash
.venv/bin/python scripts/router_cli.py retrieve \
  --university-id mit \
  --query "MIT 有 Economics 本科专业吗？"

.venv/bin/python scripts/router_cli.py retrieve \
  --university-id caltech \
  --query "Caltech 有 Computer Science 本科专业吗？"
```

当前路由边界：单院校 HTTP 测试必须传 `--university-id`。不传时出现错误方向，属于 Agent 参数/路由待改进问题，不能用来否定已经显式限定范围后的 L1 检索质量。

### 4.2 专业向上检索

```bash
.venv/bin/python scripts/router_cli.py retrieve \
  --direction upward \
  --query "计算机专业的院校有哪些？" \
  --max-results 10
```

预期：`mode=upward`，每个 `matches[]` 是院校组，内部 `matched_programs[]` 是该校相关项目；`weknora_ms=0`。

### 4.3 范围检索

```bash
.venv/bin/python scripts/router_cli.py retrieve \
  --direction range \
  --country-code US \
  --region California \
  --query "加州已入库院校有哪些？" \
  --max-results 10
```

预期只返回 Caltech 和 Stanford，且 `weknora_ms=0`。

### 4.4 L2 证据检索

先确认目标 URL 已导入成功，再执行：

```bash
.venv/bin/python scripts/router_cli.py retrieve \
  --university-id mit \
  --query "MIT EECS PhD 申请需要提交哪些材料？" \
  --max-results 5
```

预期：`mode=l1_l2`，`evidence[]` 非空，所有 evidence 的 `source_id/source_url/dataset_version` 都属于 MIT EECS 当前版本。

## 5. 如何阅读检索结果

| 字段 | 验证方法 |
|---|---|
| `trace_id` | 每题必须记录，用于查日志和回放。 |
| `mode` | `l1/l1_l2/upward/range/clarification/not_found` 必须符合问题类型。 |
| `scope` | 检查 `university_id/dataset_version/direction/filters`，防止串校和串版本。 |
| `matches` | L1 目录或事实原始记录；检查 `entry_id/fact_id/source_id/raw_value`。 |
| `evidence` | L2 chunk；正文必须支持结论，且 URL、学校、版本正确。 |
| `missing_slots` | 模糊问题必须明确缺少 `university_id`、`discipline` 或项目范围。 |
| `warnings` | `fact_review_required/fact_conflict/missing_evidence` 不能被 Agent 隐藏。 |
| `timings` | L1/upward/range 的 `weknora_ms` 必须为 0；记录 `total_ms` 做 p95。 |

自然语言回答只允许基于 `matches/evidence` 组织。原始结果未提供的排名、录取概率、资格保证和推测不得加入答案。

## 6. L2 就绪检查

查看每所学校当前 URL 状态：

```bash
docker compose -f infra/docker-compose.yml exec -T postgres \
  psql -U edumeta -d edumeta -P pager=off -c "
select university_id, weknora_import_status, count(*)
from source_registry s
join school_versions v using (university_id, version_id)
where v.publication_state='current'
group by university_id, weknora_import_status
order by university_id, weknora_import_status;"
```

检查某个 L2 问题要求的具体来源：

```bash
docker compose -f infra/docker-compose.yml exec -T postgres \
  psql -U edumeta -d edumeta -P pager=off -c "
select s.university_id, s.source_id, s.canonical_url,
       s.weknora_import_status, s.weknora_knowledge_base_id,
       s.weknora_knowledge_id, s.error_message
from source_registry s
join school_versions v using (university_id, version_id)
where v.publication_state='current'
  and s.university_id='mit'
  and s.canonical_url ilike '%electrical-engineering-and-computer-science%';"
```

只有 `weknora_import_status=success` 且 `weknora_knowledge_id` 非空时，该来源对应的 L2 题才可正式判定。`running` 只能记为环境未就绪，`failed` 必须查看 `error_message/failure_reason`。

## 7. 自动基准与运行闸门

运行跨院校 L1 接受测试：

```bash
.venv/bin/python scripts/retrieval_benchmark.py \
  --cases qa/cross-university-acceptance-cases.jsonl \
  --runs 5 \
  --output-path qa/reports/cross-university-manual-baseline.json
```

运行完整运行时闸门：

```bash
.venv/bin/python scripts/runtime_acceptance.py \
  --output-path qa/reports/runtime-compose-manual.json
```

运行时闸门会在任一 current source 仍为 `pending/running/failed` 时失败，这是预期的发布阻断，不应通过忽略错误来变绿。

## 8. 增量 MD 验证

当前 API 接收“该院校完整快照 MD”，不接受只含几段内容的 patch。

### 8.1 新院校：自动创建独立 KB

```bash
.venv/bin/python scripts/router_cli.py ingest-school \
  --university-id harvard \
  --school-tier core \
  --university-name "Harvard University" \
  --country-code US \
  --region Massachusetts \
  --aliases "Harvard" \
  --file "/Volumes/Disk/jishu/PycharmProjects/edumeta-knowledge/docs/测试文件/院校明细/Harvard_知识库_完整深度数据_v2.md"
```

保存返回的 `run_id` 并轮询：

```bash
.venv/bin/python scripts/router_cli.py ingestion-status --run-id <run_id>
```

预期：`operation=create`、最终 `status=published`、`weknora_kb_operation=create`，返回独立 `weknora_knowledge_base_id`。发布表示 L1 已可用；URL 导入仍由 worker 异步完成。

### 8.2 相同 MD：unchanged

使用完全相同的文件和 `university_id` 再上传一次。预期：

```text
operation=unchanged
status=unchanged
不产生新 current version
不产生新 WeKnora job
KB ID 不变
```

### 8.3 同院校完整更新：复用 KB

先复制并修改完整 MD 中一个目录事实或新增一个测试 URL，再用相同 `university_id` 上传：

```bash
.venv/bin/python scripts/router_cli.py ingest-school \
  --university-id harvard \
  --school-tier core \
  --file /absolute/path/to/harvard-updated-full.md
```

预期：`operation=update`、`weknora_kb_operation=reuse`，旧 current 变为 superseded，新版本成为唯一 current；仅新增/变化 URL 创建导入 job，未变化 URL 继承同一 KB 中的 knowledge ID。

### 8.4 显式更新指定 KB

```bash
.venv/bin/python scripts/router_cli.py ingest-school \
  --university-id mit \
  --school-tier core \
  --weknora-knowledge-base-id 1b91fcff-ce72-4e97-9de0-f23a8ba419d9 \
  --file /absolute/path/to/mit-updated-full.md
```

预期 `weknora_kb_operation=explicit`。所有新 job 的 `knowledge_base_id` 必须等于参数值。

### 8.5 强制创建新 KB

```bash
.venv/bin/python scripts/router_cli.py ingest-school \
  --university-id harvard \
  --school-tier core \
  --create-new-weknora-kb \
  --file /absolute/path/to/harvard-updated-full.md
```

预期创建并重新绑定新 KB。切换 KB 后不得继承旧 KB 的 knowledge/document/chunk ID。此操作只用于明确迁移或隔离测试，不是普通更新默认路径。

`--weknora-knowledge-base-id` 与 `--create-new-weknora-kb` 互斥。

## 9. PostgreSQL 验证

### 9.1 current 唯一与 KB 绑定

```sql
select u.university_id, u.weknora_knowledge_base_id,
       v.version_id, v.dataset_version, v.publication_state
from universities u
join school_versions v using (university_id)
where v.publication_state='current'
order by u.university_id;
```

每校只能有一个 current，且新院校的 KB ID 不得与其他院校误共享。

### 9.2 入库运行与 job 数量

```sql
select run_id, university_id, operation, status,
       weknora_kb_operation, weknora_knowledge_base_id,
       error_message, created_at
from ingestion_runs
order by created_at desc
limit 20;

select run_id, university_id, knowledge_base_id, status, count(*)
from weknora_import_jobs
group by run_id, university_id, knowledge_base_id, status
order by run_id, status;
```

### 9.3 URL 与 MD 关系

```sql
select s.university_id, s.source_id, s.canonical_url,
       s.weknora_knowledge_base_id, s.weknora_knowledge_id,
       s.weknora_import_status, count(l.entry_id) as linked_entries
from source_registry s
join school_versions v using (university_id, version_id)
left join source_entry_links l
  on l.university_id=s.university_id
 and l.version_id=s.version_id
 and l.source_id=s.source_id
where v.publication_state='current'
group by s.university_id, s.source_id, s.canonical_url,
         s.weknora_knowledge_base_id, s.weknora_knowledge_id,
         s.weknora_import_status
order by s.university_id, s.source_id;
```

这一步验证 MD 中提取的 URL 已进入 Source Registry，并能关联目录项和 WeKnora knowledge。

## 10. WeKnora 验证

在 WeKnora 管理端按 `universities.weknora_knowledge_base_id` 打开目标 KB，逐项核对：

1. 新院校有独立 KB，不写入 MIT 或其他学校 KB。
2. URL 数量与该 run 产生的 job 数量合理一致。
3. 成功 URL 的 knowledge/document ID 与 PostgreSQL 一致。
4. 同院校普通更新仍在原 KB；显式 KB 更新只写目标 KB。
5. 强制新 KB 后，检索只使用 current source 实际绑定的 KB，不全局搜索旧 KB。

## 11. MCP 人工盲测流程

1. 先执行 HTTP 题，确认检索基线。
2. 新开 Agent 会话，只打开问题卷，不打开答案。
3. 每题要求 Agent 展示：结论、来源 URL、`trace_id`、`mode`、总耗时。
4. 单轮题使用新会话；M01-M03 使用同一会话。
5. 完成后用评审答案逐题判定，并保存 HTTP 与 MCP 两份结果。
6. 对失败题先比较 MCP 工具原始 JSON：原始 JSON 正确则归因 Agent；原始 JSON 错误则归因检索层。

## 12. 发布通过标准

- D01-D06、U01-U03、R01-R03、X01-X03 无错校、错项目、错层级。
- 所有 L1/upward/range 请求 `weknora_ms=0`，5 次运行 p95 小于 1 秒。
- E01 必须返回 scoped MIT EECS evidence；L2 ready case 目标 p95 小于 1 秒。
- E03/E04 在当前版本只用于暴露缺陷，修复并补回归后才能纳入通过率。
- evidence 支持结论，P0 事实不得由 Agent 自行补充。
- 相同 MD 不产生版本/job；普通同校更新复用 KB；新校自动新建 KB；显式/强制参数行为正确。
- 每个失败都有 `trace_id` 和唯一主要归因：data、parser、L1、routing、WeKnora、evidence、MCP 或 Agent。

任何错学校、无证据强答、跨 KB 污染、非 L2 调用 WeKnora、相同 MD 重复建 KB，均为阻断项。
