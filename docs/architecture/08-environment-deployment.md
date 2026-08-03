# 环境与部署

## Compose

核心服务：PostgreSQL、OpenSearch、一次性 bootstrap、Fast Router、TypeScript Tool Gateway。WeKnora 是外部可选服务。

```bash
docker compose up -d --build
```

bootstrap 只幂等执行全部 migration，不装载或发布仓库内的 fixture 数据。真实院校必须通过带 pre-publish/post-publish 门禁的 Markdown 导入链路进入 PostgreSQL 和 OpenSearch，避免服务重启把已隔离院校重新设为 current。只有 bootstrap `Exited (0)` 后 Router 才启动；只有 Router healthy 后 MCP 才启动。首次 clone 启动后需要执行受审计的批量导入或上传单校 Markdown。

默认端口：Fast Router `127.0.0.1:8000`，MCP `127.0.0.1:8765/mcp`，PostgreSQL `127.0.0.1:5432`，OpenSearch `0.0.0.0:9200`。

远程访问时，只允许 Fast Router 和 MCP Gateway 改绑到可信私网/VPN 地址：

```text
FAST_ROUTER_BIND_HOST=100.74.163.113
MCP_BIND_HOST=100.74.163.113
```

PostgreSQL 继续保持 localhost-only。OpenSearch 固定发布到 `0.0.0.0`，以便其他容器通过宿主机 IP 访问；由于当前关闭 Security Plugin，必须用防火墙或可信网络限制该端口，不能直接暴露到公网。相同 Compose 网络内的服务仍优先使用 `http://opensearch:9200`。

## 配置

```text
POSTGRES_DSN
OPENSEARCH_URL
INGESTION_DATA_ROOT
WEKNORA_BASE_URL
WEKNORA_API_KEY
WEKNORA_KB_TEMPLATE_ID
WEKNORA_KNOWLEDGE_BASE_ID (仅旧数据 fallback，正常多 KB 部署留空)
WEKNORA_API_KEY_HEADER
WEKNORA_SEARCH_TIMEOUT_SECONDS
FAST_ROUTER_BASE_URL
FAST_ROUTER_TIMEOUT_MS
TRACE_LOG_PATH
```

真实密钥只放未跟踪的 `.env`。L1 可在未配置 WeKnora 时运行；L1+WeKnora 发布验收必须配置真实服务。正常检索从每条 source 读取实际 KB ID；模板 KB 只用于新建院校 KB 时复制配置，不是统一检索目标。

宿主端口可通过 `POSTGRES_PORT/OPENSEARCH_PORT/FAST_ROUTER_PORT/MCP_PORT` 覆盖。OpenSearch 的宿主绑定固定为 `0.0.0.0`；Fast Router 和 MCP 的宿主监听地址可通过 `FAST_ROUTER_BIND_HOST/MCP_BIND_HOST` 覆盖，容器内部调用地址不变。

PG 集成测试必须使用独立数据库，例如 `edumeta_test`，禁止指向运行库：

```bash
EDUMETA_TEST_DSN=postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta_test \
  .venv/bin/python -m pytest -q tests/test_postgres_loader.py
```
