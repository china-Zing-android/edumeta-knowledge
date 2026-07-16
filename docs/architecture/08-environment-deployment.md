# 环境与部署

## Compose

核心服务：PostgreSQL、OpenSearch、一次性 bootstrap、Fast Router、TypeScript Tool Gateway。WeKnora 是外部可选服务。

```bash
docker compose up -d --build
```

bootstrap 会幂等执行全部 migration，装载 `data/normalized/` 下的学校，发布五类 OpenSearch 投影并校验学校/版本计数。只有 bootstrap `Exited (0)` 后 Router 才启动；只有 Router healthy 后 MCP 才启动。因此首次 clone 不会得到“容器正常但数据库和索引为空”的假健康状态。

端口：Fast Router `127.0.0.1:8000`，MCP `127.0.0.1:8765/mcp`，PostgreSQL `5432`，OpenSearch `9200`。

## 配置

```text
POSTGRES_DSN
OPENSEARCH_URL
INGESTION_DATA_ROOT
WEKNORA_BASE_URL
WEKNORA_API_KEY
WEKNORA_KNOWLEDGE_BASE_ID
WEKNORA_KB_TEMPLATE_ID
WEKNORA_API_KEY_HEADER
WEKNORA_SEARCH_TIMEOUT_SECONDS
FAST_ROUTER_BASE_URL
FAST_ROUTER_TIMEOUT_MS
TRACE_LOG_PATH
```

真实密钥只放未跟踪的 `.env`。L1 可在未配置 WeKnora 时运行；L1+WeKnora 发布验收必须配置真实服务。

宿主端口可通过 `POSTGRES_PORT/OPENSEARCH_PORT/FAST_ROUTER_PORT/MCP_PORT` 覆盖，容器内部调用地址不变。

PG 集成测试必须使用独立数据库，例如 `edumeta_test`，禁止指向运行库：

```bash
EDUMETA_TEST_DSN=postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta_test \
  .venv/bin/python -m pytest -q tests/test_postgres_loader.py
```
