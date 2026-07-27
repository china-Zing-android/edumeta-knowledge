# 服务器更新、批量导入与验证手册

本文是当前服务器的推荐执行顺序。所有命令都在仓库根目录执行，适用于保留现有 PostgreSQL、OpenSearch 和导入状态卷的代码更新。

## 目标地址

使用仓库内已提交的 `compose.server.yaml` 后：

| 服务 | 服务器本机 | Tailscale |
|---|---|---|
| Fast Router HTTP | `http://127.0.0.1:8000` | `http://100.74.163.113:8000` |
| MCP Gateway | `http://127.0.0.1:18765/mcp` | `http://100.74.163.113:18765/mcp` |
| MCP 健康检查 | `http://127.0.0.1:18765/health` | `http://100.74.163.113:18765/health` |

宿主机原有 `8765` 端口不会被占用。PostgreSQL 和 OpenSearch 仍只绑定 `127.0.0.1`。

服务器 profile 默认 `WEKNORA_IMPORT_ENABLED=false`。这表示 Markdown 仍会解析、入 PostgreSQL、发布 OpenSearch、提取 URL 并生成 queued job，但不会把 URL 发送给 WeKnora。

## 一、更新前检查

进入项目目录：

```bash
cd /path/to/edumeta-knowledge
```

确认当前容器状态：

```bash
docker compose -f compose.yaml -f compose.server.yaml ps -a
```

可选但推荐：更新前备份 PostgreSQL 控制面数据。

```bash
BACKUP_DIR="${HOME}/edumeta-backups"
mkdir -p "$BACKUP_DIR"
docker compose exec -T postgres \
  pg_dump -U edumeta -d edumeta -Fc \
  > "$BACKUP_DIR/edumeta-$(date +%Y%m%d-%H%M%S).dump"
```

禁止执行：

```bash
docker compose down -v
```

`-v` 会删除 PostgreSQL、OpenSearch、原始上传记录和批量导入进度。

## 二、拉取代码并重建服务

```bash
git pull origin main

docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  up -d --build
```

这里不需要手工创建端口配置文件。`bootstrap` 会自动执行尚未执行的 PostgreSQL migration，然后退出；Fast Router 会在 migration 成功后启动，MCP 会在 Fast Router healthy 后启动。

查看状态：

```bash
docker compose -f compose.yaml -f compose.server.yaml ps -a
```

通过标准：

- `postgres`、`opensearch`、`fast-router`、`tool-gateway` 为 `healthy`。
- `bootstrap` 为 `Exited (0)`。
- 不应出现反复重启的容器。

如果 bootstrap 不是 `Exited (0)`：

```bash
docker compose -f compose.yaml -f compose.server.yaml logs --tail=200 bootstrap
```

## 三、验证 HTTP 和 MCP 双地址

服务器本机验证：

```bash
curl -fsS http://127.0.0.1:8000/health | jq
curl -fsS http://127.0.0.1:18765/health | jq
```

Tailscale 地址验证：

```bash
curl -fsS http://100.74.163.113:8000/health | jq
curl -fsS http://100.74.163.113:18765/health | jq
```

检查端口监听：

```bash
ss -lntp | grep -E ':(8000|18765)\b'
```

应同时看到 `127.0.0.1` 和 `100.74.163.113` 的监听记录。

## 四、数据更新脚本的固定执行顺序

每次 Parser、质量规则或批量数据发生变化，按以下顺序执行。不要交换隔离、导入和 QA 的顺序。

### 1. 预览旧数据隔离范围

```bash
./scripts/quarantine_unverified_universities.sh \
  | tee /tmp/edumeta-quarantine-dry-run.json \
  | jq '{status,count}'
```

这一步只预览，不修改数据。当前规则集 `2026-07-27.1` 的基准是：

- `276` 所 `passed`，允许自动导入。
- `75` 所 `needs_review`，不自动发布。
- `88` 所 `failed`，阻断发布。

### 2. 隔离旧版本中不再合格的院校

确认预览结果后执行：

```bash
./scripts/quarantine_unverified_universities.sh --apply \
  | tee /tmp/edumeta-quarantine-applied.json \
  | jq '{status,count,postgres_updates,opensearch_updates}'
```

该操作不会删除历史版本，只会停止检索当前规则下不合格的学校，避免旧数据继续污染范围搜索。

### 3. 预览本次需要重导的院校

```bash
./scripts/import_universities.sh --dry-run \
  | tee /tmp/edumeta-import-dry-run.json \
  | jq '{selected,pending}'
```

`selected` 应为当前通过门禁的总数。`pending` 只表示本次真正需要处理的数量；已经使用相同 Markdown、规则版本和 Parser contract 成功发布的学校会被自动跳过。

### 4. 可选：先跑 5 所冒烟测试

首次部署这套版本时，建议先执行：

```bash
./scripts/import_universities.sh \
  --progress-interval-seconds 5 \
  --timeout-seconds 1200 \
  --university-id mit \
  --university-id cornell \
  --university-id nus \
  --university-id harvard \
  --university-id mcgill_university
```

每所学校应最终显示 `published` 或 `unchanged`。`accepted`、`parsing`、`validating`、`publishing` 都是中间状态，不是完成状态。

### 5. 导入全部通过门禁的院校

```bash
./scripts/import_universities.sh \
  --progress-interval-seconds 5 \
  --timeout-seconds 1200 \
  2>&1 | tee /tmp/edumeta-import-all.log
```

该命令串行执行且可以续跑。终端中断、SSH 断开或单校失败后，重新执行同一命令即可；脚本会根据 Markdown hash、质量规则版本、Parser contract 和持久化状态跳过已完成学校。

不要并行运行多个 `import_universities.sh`，也不要为提高速度绕过逐校发布门禁。

### 6. 查看导入是否结束

查看批量状态文件：

```bash
docker compose exec -T fast-router \
  cat /app/data/import-state/university-md-batch.jsonl \
  | jq -s '{
      total: length,
      completed: map(select(.status == "published" or .status == "unchanged")) | length,
      failed: map(select(.status == "failed")) | length
    }'
```

查看数据库中是否还有未结束任务：

```bash
docker compose exec -T postgres \
  psql -U edumeta -d edumeta -c "
    SELECT status, count(*)
    FROM ingestion_runs
    GROUP BY status
    ORDER BY status;
  "
```

只看仍在处理的任务：

```bash
docker compose exec -T postgres \
  psql -U edumeta -d edumeta -c "
    SELECT run_id, university_id, status, updated_at, error_message
    FROM ingestion_runs
    WHERE status NOT IN ('published', 'unchanged', 'failed')
    ORDER BY updated_at DESC;
  "
```

完成标准：

- 批量脚本最后输出 `failed: 0`。
- 通过门禁的 276 所全部为 `published` 或 `unchanged`。
- 非终态查询返回 0 行。
- `needs_review` 和 `failed` 院校没有被 `--allow-unverified` 强制导入。

## 五、运行 30 问五轮回归

导入完成后执行当前后置门禁题集：

```bash
docker compose exec -T fast-router \
  python /app/scripts/retrieval_benchmark.py \
  --base-url http://127.0.0.1:8000 \
  --cases /app/qa/live-batch-student-qa-post-audit-2026-07-27.jsonl \
  --runs 5 \
  --output-path /tmp/live-batch-student-qa-post-audit-server.json
```

取出报告：

```bash
docker compose cp \
  fast-router:/tmp/live-batch-student-qa-post-audit-server.json \
  qa/reports/live-batch-student-qa-post-audit-server.json

jq '{
  status,
  cases,
  runs,
  failures,
  nondeterministic_cases,
  http_l1_p50_ms,
  http_l1_p95_ms,
  http_upward_p95_ms,
  http_range_p95_ms
}' qa/reports/live-batch-student-qa-post-audit-server.json
```

通过标准：

- `status` 为 `passed`。
- `cases` 为 `30`，`runs` 为 `5`。
- `failures` 和 `nondeterministic_cases` 均为空。
- L1、upward、range 的 p95 均小于 `1000 ms`。
- 当前本地基准为：L1 p95 约 `108 ms`、upward p95 约 `134 ms`、range p95 约 `409 ms`。

## 六、验证一条真实检索

本机 HTTP：

```bash
curl -fsS http://127.0.0.1:8000/v1/retrieve \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "MIT 有 Economics 本科专业吗？",
    "university_id": "mit",
    "direction": "downward",
    "filters": {},
    "context": {},
    "max_results": 5
  }' | jq '{mode,scope,matches,context,warnings,timings,trace_id}'
```

另一台 Tailscale 设备只需把地址改为：

```text
http://100.74.163.113:8000/v1/retrieve
```

## 七、配置并验证 MCP

MCP 客户端与服务运行在同一台服务器时：

```json
{
  "mcpServers": {
    "edumeta-local": {
      "url": "http://127.0.0.1:18765/mcp"
    }
  }
}
```

Claude/Codex 在另一台 Tailscale 设备时：

```json
{
  "mcpServers": {
    "edumeta-server": {
      "url": "http://100.74.163.113:18765/mcp"
    }
  }
}
```

Codex CLI 也可以直接注册：

```bash
codex mcp add edumeta-server \
  --url http://100.74.163.113:18765/mcp
```

添加配置后重启 Agent 会话，确认服务器状态为已连接，并调用 `retrieve_university_knowledge` 测试：

```text
只使用 edumeta-server，查询：MIT 有 Economics 本科专业吗？
```

## 八、以后每次更新如何选择执行范围

仅改 README、文档或 MCP 端口配置：

```text
拉代码 -> Compose 重建 -> 健康检查 -> MCP 验证
```

修改 Fast Router 或 Tool Gateway，但未修改 Parser、质量规则和数据：

```text
拉代码 -> Compose 重建 -> 健康检查 -> 30 问回归 -> MCP 验证
```

修改 Parser、质量规则、Markdown 或 preflight 结果：

```text
拉代码 -> Compose 重建 -> 隔离预览 -> 隔离 apply -> 导入 dry-run
-> 可选 5 校冒烟 -> 全量续跑 -> 30 问回归 -> MCP 验证
```

仅新增或更新一所已经通过门禁的院校：

```bash
./scripts/import_universities.sh \
  --progress-interval-seconds 5 \
  --timeout-seconds 1200 \
  --university-id <university_id>
```

## 九、故障定位

```bash
docker compose -f compose.yaml -f compose.server.yaml logs --tail=200 fast-router
docker compose -f compose.yaml -f compose.server.yaml logs --tail=200 tool-gateway
docker compose -f compose.yaml -f compose.server.yaml logs --tail=200 postgres
docker compose -f compose.yaml -f compose.server.yaml logs --tail=200 opensearch
```

- 长时间停在 `accepted`：检查 Fast Router 日志和非终态数据库查询。
- `failed`：查看该 run 的 `error_message`、`stage_failures` 和 `quality_audits`。
- HTTP 正常、MCP 不通：先检查 `18765/health`，再确认客户端使用的是新端口且已重启会话。
- Tailscale 地址不通、本机地址正常：检查服务器是否确实拥有 `100.74.163.113`，以及主机防火墙是否允许 tailnet 访问 `8000/18765`。
- QA 失败：不要强制发布或写学校特例；按失败类型回到 Parser、质量门禁、OpenSearch scope 或 MCP 契约修复。

## 十、恢复 WeKnora URL 导入

只有在 L1 全量导入和 30 问回归通过后才恢复。真实 WeKnora 地址和密钥不能提交到 Git。

在服务器已有的私有环境配置中设置：

```text
WEKNORA_IMPORT_ENABLED=true
WEKNORA_BASE_URL=<真实地址>
WEKNORA_API_KEY=<真实密钥>
WEKNORA_KB_TEMPLATE_ID=<可选模板 KB>
```

然后只重建 Fast Router 和 MCP：

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  up -d --force-recreate fast-router tool-gateway
```

此前 queued 的 URL job 会继续消费，不需要重新上传 Markdown。正常多 KB 检索从每个学校和 source 的实际 KB ID 路由，不依赖一个全局默认知识库。
