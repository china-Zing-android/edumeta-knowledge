# 人工测试与增量 MD 操作

> 本文是快速入口。多院校盲测、L2 就绪判断、每校独立 WeKnora KB、增量生命周期和发布闸门的完整步骤见
> `docs/operations/multikb-testing-and-verification-runbook.md`。

## 1. 如何进入测试

### 启动服务

真实 WeKnora 配置放在仓库根目录 `.env`，该文件已被 `.gitignore` 排除。首次配置后执行：

```bash
chmod 600 .env
docker compose --env-file .env -f infra/docker-compose.yml --profile mcp up -d
```

不要把 API Key 写入 `infra/docker-compose.yml` 或提交到版本库。密钥轮换后只更新本地 `.env` 并重建 `fast-router`。

### MCP 测试

Claude/Codex 配置：

```json
{
  "mcpServers": {
    "edumeta-local": {
      "url": "http://127.0.0.1:8765/mcp"
    }
  }
}
```

重启 Agent 会话后确认 `edumeta-local` 已连接，并要求 Agent 使用
`retrieve_university_knowledge`。人工盲测使用：

- 问题卷：`qa/manual/mit-qa-question-sheet-v1.md`
- 评审答案：`qa/manual/mit-qa-review-key-v1.md`

### HTTP 直测

```bash
.venv/bin/python scripts/router_cli.py retrieve \
  --university-id mit \
  --query "MIT EECS PhD 的 TOEFL 最低要求是多少？"
```

HTTP 直测用于判断检索层；MCP + Claude 测试用于判断“检索 + Agent 表达”。两层应分别记录，避免把 Agent 的总结错误误归因给检索。

## 2. 当前检索路径

```text
Claude / Codex / Hermes
  -> MCP Gateway :8765/mcp
  -> POST Fast Router :8000/v1/retrieve
  -> 本地 university alias + current version map
  -> OpenSearch L1 _msearch
       -> 精确 course/entry ID
       -> catalog BM25
       -> quick facts
       -> WeKnora source scope
       -> entity contexts
  -> discovery/fact 命中：返回 mode=l1 + matches + context，WeKnora 不预取
  -> L1 不足且问题需要详情：
       -> Agent 回传 entry_id/program_id 时先在 source index 强制 scope
       -> 按 current source 的 knowledge_ids 调 WeKnora
       -> Evidence Gate 校验学校/source/version/chunk
       -> 返回 mode=l1_l2 + evidence
  -> 信息模糊：clarification + missing_slots
  -> 学校/专业不存在：not_found
```

关键边界：

- PostgreSQL 不在普通查询热路径中，只维护 current version、source、fact 和 WeKnora job 状态。
- OpenSearch 负责快速 L1；WeKnora 只补充页面正文证据。
- MCP Gateway 不做路由、缓存或检索，只转发统一契约。
- 检索模块不生成自然语言答案；Agent 按直接答案、`context`、少量 related entities、available topics 的顺序组织回答。`context` 不是 evidence。
- 无 L0、无排名/推荐、无外部院校发现、无请求时 retry；允许在已入库院校中做 range/upward 检索。

## 3. 同院校 MD 更新

当前 API 使用 **完整快照更新**，不接收只包含新增段落的 patch MD。操作步骤：

1. 在原 MIT MD 上合并修改，形成新的完整 MD 文件。
2. 保持相同 `university_id=mit` 上传：

   ```bash
   .venv/bin/python scripts/router_cli.py ingest-school \
     --university-id mit \
     --school-tier core \
     --file /absolute/path/to/mit-updated.md
   ```

3. 记录返回的 `run_id`，轮询：

   ```bash
   .venv/bin/python scripts/router_cli.py ingestion-status --run-id <run_id>
   ```

4. 终态说明：

   ```text
   unchanged  完整 MD hash 未变化，不发布、不建 WeKnora job
   published  新版本已成为 current，L1 可查询；WeKnora job 可继续异步处理
   failed     解析/校验/索引失败，旧 current 版本继续服务
   ```

更新粒度：

- 该校会生成新的完整 dataset version，并重发该校 L1 文档。
- 其他学校的 current version 和 OpenSearch 文档不变。
- 事实/目录变化但 URL 不变：不新建 WeKnora job。
- 新增或 canonical URL 变化：只为受影响 URL 新建 job。
- 默认复用该校已绑定 KB；传 `--weknora-knowledge-base-id` 可更新指定 KB，传 `--create-new-weknora-kb` 可强制新建并重新绑定。
- 删除内容不会物理删除历史版本；旧版本继续保留用于追踪和回滚。

## 4. 新增其他院校 MD

1. 为学校确定永久稳定 ID，例如 `stanford`、`harvard`、`uc_berkeley`。
2. 准备该校完整 MD。结构与 MIT 不同但满足通用结构化格式时走 generic adapter；特殊格式需要新增 parser adapter，不能修改公共 schema。
3. 上传：

   ```bash
   .venv/bin/python scripts/router_cli.py ingest-school \
     --university-id stanford \
     --school-tier core \
     --university-name "Stanford University" \
     --country-code US --region California --aliases "Stanford,SU" \
     --file /absolute/path/to/stanford.md
   ```

   非核心学校使用 `--school-tier non_core`。

4. 轮询 `run_id` 到 `published` 或 `failed`。
5. 发布后先做三类 smoke：

   ```bash
   .venv/bin/python scripts/router_cli.py retrieve --university-id stanford --query "Stanford 有哪些本科 CS 相关专业？"
   .venv/bin/python scripts/router_cli.py retrieve --university-id stanford --query "Stanford 某项目申请截止日期是什么？"
   .venv/bin/python scripts/router_cli.py retrieve --university-id stanford --query "Stanford 某项目完整申请要求是什么？"
   .venv/bin/python scripts/router_cli.py retrieve --direction upward --query "计算机专业的院校有哪些？"
   .venv/bin/python scripts/router_cli.py retrieve --direction range --country-code US --region California --query "加州已入库院校有哪些？"
   ```

## 5. 入库后检查

```sql
select university_id, dataset_version, publication_state, published_at
from school_versions
order by published_at desc nulls last;

select run_id, university_id, status, error_message
from ingestion_runs
order by created_at desc limit 20;

select university_id, status, count(*)
from weknora_import_jobs
group by university_id, status
order by university_id, status;
```

恢复已有 WeKnora 数据但缺少 job 审计时，执行幂等回填：

```bash
.venv/bin/python scripts/backfill_weknora_success_jobs.py \
  --postgres-dsn postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta \
  --university-id mit
```

验收时至少确认：新版本 current 唯一、解析数量合理、无跨校污染、变化 URL job 数符合预期、每个 current success source 有 success job、L1 可立即查询、L2 在 WeKnora success 后返回正确 source evidence。
