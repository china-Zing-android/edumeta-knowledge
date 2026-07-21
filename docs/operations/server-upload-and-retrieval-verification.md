# 服务器上传与检索验证

以下命令都在服务器的项目根目录执行。Compose 端口只绑定 `127.0.0.1`，因此不能直接从公网访问。

## 1. 健康检查

```bash
docker compose ps -a
curl -fsS http://127.0.0.1:8000/health | jq
curl -fsS http://127.0.0.1:8765/health | jq
```

应满足：

- `postgres`、`opensearch`、`fast-router`、`tool-gateway` 为 `healthy`。
- Fast Router 返回 `status: ok`，`opensearch.ready` 为 `true`。
- 配置 WeKnora 后，`weknora.configured`、`weknora.worker_alive` 为 `true`，`worker_last_error` 为 `null`。

## 2. 验证已有 MIT L1 检索

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
  }' | tee /tmp/mit-l1.json | jq '{mode,scope,matches,evidence,warnings,timings,trace_id}'
```

预期：`mode=l1`；`matches` 包含 Economics、课程号 14-1；`evidence` 为空；`timings.weknora_ms=0`。

关键事实测试：

```bash
curl -fsS http://127.0.0.1:8000/v1/retrieve \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "MIT 本科 2026-2027 学费是多少？",
    "university_id": "mit",
    "direction": "downward",
    "filters": {},
    "context": {},
    "max_results": 5
  }' | jq '{mode,matches,warnings,timings,trace_id}'
```

## 3. 上传一个新院校完整 Markdown

下面用 Caltech 测试。不要先用 ASU，ASU 有 1,100 多个 URL，不适合第一次验证。

```bash
UPLOAD_RESPONSE=$(curl -fsS -X POST http://127.0.0.1:8000/v1/university-ingestions \
  -F university_id=caltech \
  -F school_tier=core \
  -F 'university_name=California Institute of Technology' \
  -F country_code=US \
  -F region=California \
  -F 'aliases=Caltech' \
  -F 'file=@docs/测试文件/院校明细/Caltech_知识库_完整深度数据_v2.md;type=text/markdown')

echo "$UPLOAD_RESPONSE" | jq
RUN_ID=$(echo "$UPLOAD_RESPONSE" | jq -r '.run_id')
echo "$RUN_ID"
```

首次上传通常返回 `operation=create`；如果此前上传过相同文件，可能返回 `unchanged`，这是正确的幂等行为。

## 4. 轮询解析与发布状态

```bash
while true; do
  RESULT=$(curl -fsS "http://127.0.0.1:8000/v1/university-ingestions/$RUN_ID")
  echo "$RESULT" | jq '{run_id,operation,status,counts,weknora_kb_operation,weknora_knowledge_base_id,weknora_jobs,error_message}'
  STATUS=$(echo "$RESULT" | jq -r '.status')
  case "$STATUS" in
    published|unchanged|failed) break ;;
  esac
  sleep 2
done
```

`published` 表示 PostgreSQL 与 OpenSearch 的 L1 已经发布，可以立即检索。WeKnora URL 导入是异步任务，继续查询同一个 `run_id` 可观察 `weknora_jobs` 从 `queued/running` 变为 `success` 或 `failed`。

预期新建 Caltech 的核心数量约为：

```text
catalog_entries: 78
source_registry/url_manifest: 57
weknora_kb_operation: create
```

## 5. 验证上传后的 L1 检索

```bash
curl -fsS http://127.0.0.1:8000/v1/retrieve \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "Caltech 有 Computer Science 本科专业吗？",
    "university_id": "caltech",
    "direction": "downward",
    "filters": {},
    "context": {},
    "max_results": 5
  }' | tee /tmp/caltech-l1.json | jq '{mode,scope,matches,context,warnings,timings,trace_id}'
```

检查：学校必须是 `caltech`，不能混入 MIT；`mode=l1`；`matches` 非空；`weknora_ms=0`。

## 6. 验证 WeKnora 深度检索

先确认目标来源的 WeKnora job 已成功，再提问官网细节。MIT 已有稳定基线：

```bash
curl -fsS http://127.0.0.1:8000/v1/retrieve \
  -H 'Content-Type: application/json' \
  -d '{
    "query": "MIT EECS PhD 申请需要提交哪些材料？",
    "university_id": "mit",
    "direction": "downward",
    "filters": {},
    "context": {},
    "max_results": 5
  }' | tee /tmp/mit-l2.json | jq '{mode,scope,matches,evidence,warnings,timings,trace_id}'
```

预期：`mode=l1_l2`，`evidence` 非空；每条 evidence 的学校、URL 和 `source_id` 都属于 MIT EECS；`weknora_ms` 大于 0。

## 7. 验证 MCP

服务器本机：

```bash
curl -fsS http://127.0.0.1:8765/health | jq
```

如果 Claude/Codex 在另一台电脑，先建立 SSH 隧道：

```bash
ssh -N \
  -L 8765:127.0.0.1:8765 \
  -L 8000:127.0.0.1:8000 \
  user@your-server
```

Agent MCP 地址仍配置为 `http://127.0.0.1:8765/mcp`。

## 8. 失败定位

```bash
docker compose logs --tail=200 fast-router
docker compose logs --tail=200 tool-gateway
```

- 上传返回 `422`：Markdown、参数或 parser adapter 问题。
- `status=failed`：查看 `error_message` 和 `stage_failures`。
- L1 查不到：检查 `status=published`、OpenSearch alias 和 `scope.dataset_version`。
- L2 无 evidence：检查 WeKnora job、知识库 ID 和来源 URL 是否属于当前学校版本。
- HTTP 正确但 Agent 回答错误：属于 MCP 参数或 Agent 表达问题，不是检索层问题。
