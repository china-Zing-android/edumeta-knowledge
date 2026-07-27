# 批量院校 MD 增量导入

## 目标

将 `data/raw-md/universities/` 中通过 preflight 的院校按现有完整快照 API 逐校导入。该流程不绕过 Parser、PostgreSQL staging/current、OpenSearch alias 和增量 diff。

## 首次部署

```bash
git pull
```

在 `.env` 中设置：

```text
WEKNORA_IMPORT_ENABLED=false
```

重新创建 Fast Router，使原始 MD 只读挂载和 import state volume 生效：

```bash
docker compose --env-file .env up -d --build --force-recreate fast-router tool-gateway
```

检查闸门：

```bash
curl -fsS http://127.0.0.1:8000/health | jq '.weknora | {import_enabled,worker_alive}'
```

预期均为 `false`。

## 小批验证

```bash
./scripts/import_universities.sh --dry-run --country US --limit 3
./scripts/import_universities.sh --country US --limit 3
```

导入命令会立即显示选中数量、当前学校、`run_id`、处理阶段及耗时；阶段没有变化时每 10 秒输出一次心跳。可用 `--progress-interval-seconds 5` 调整心跳间隔。

旧版本脚本正在执行且暂时没有输出时，可在另一个终端查看服务端状态：

```bash
watch -n 2 'docker compose exec -T postgres psql -U edumeta -d edumeta -c "SELECT university_id,status,operation,updated_at,error_message FROM ingestion_runs ORDER BY created_at DESC LIMIT 8;"'
```

检查批次状态：

```bash
docker compose exec -T fast-router \
  cat /app/data/import-state/university-md-batch.jsonl
```

每所学校必须达到 `published` 或 `unchanged`。`failed` 会记录错误，修复后重复运行即可继续。

## 验证新增和幂等

选择本批次中尚未入库且 preflight 通过的学校，例如 Cornell：

```bash
./scripts/import_universities.sh --university-id cornell
```

验证 L1：

```bash
curl -fsS http://127.0.0.1:8000/v1/retrieve \
  -H 'Content-Type: application/json' \
  -d '{"query":"Cornell 有哪些 Computer Science 项目？","university_id":"cornell","direction":"downward","filters":{},"context":{},"max_results":5}' \
  | jq '{mode,scope,matches,warnings,timings,trace_id}'
```

清除该校本地批次完成标记后再次运行，用于验证服务端幂等：

```bash
docker compose exec -T fast-router sh -lc \
  "grep -v '\"university_id\": \"cornell\"' /app/data/import-state/university-md-batch.jsonl > /tmp/state && mv /tmp/state /app/data/import-state/university-md-batch.jsonl"

./scripts/import_universities.sh --university-id cornell
```

第二次应返回 `operation=unchanged`、`status=unchanged`，不产生新 current version。

## 全量导入

```bash
./scripts/import_universities.sh
```

默认仅导入 preflight `passed` 且哈希一致的 276 所。75 所 `needs_review` 和 88 所 `failed` 不会自动导入。串行发布是有意设计，用于避免并发切换 OpenSearch current 状态。不要用 shell 并行启动多个批次。

续跑状态不仅检查 `published/unchanged`，还检查 Markdown 哈希和质量规则版本。升级 Parser 或审计规则后，旧状态会自动失效并重新导入通过门禁的院校。

若服务器已经导入过旧批次，先执行 `./scripts/quarantine_unverified_universities.sh` 预览，再用 `--apply` 隔离当前不再通过门禁的旧院校；否则这些旧 current 数据仍可能被检索到。

## 恢复 WeKnora

L1 验收完成后，在 `.env` 中设置：

```text
WEKNORA_IMPORT_ENABLED=true
```

然后重建 Fast Router。此前 queued URL job 会继续导入，不需要重新上传 MD。
