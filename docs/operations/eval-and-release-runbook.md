# Eval 与发布 Runbook

```bash
.venv/bin/python -m pytest -q
EDUMETA_TEST_DSN=postgresql://edumeta:edumeta@127.0.0.1:5432/edumeta_test \
  .venv/bin/python -m pytest -q tests/test_postgres_loader.py

cd apps/tool-gateway && npm test
.venv/bin/python scripts/retrieval_benchmark.py --runs 5
.venv/bin/python scripts/retrieval_benchmark.py --cases qa/cross-university-acceptance-cases.jsonl --runs 5
node apps/tool-gateway/dist/src/benchmark_client.js --url http://127.0.0.1:8765/mcp --runs 50
docker compose -f infra/docker-compose.yml config --quiet
docker compose -f infra/docker-compose.yml --profile mcp ps
```

发布阻断条件：MIT 或跨院校检索 case 任一失败、五轮结果模式/实体不一致、HTTP L1 p95 >= 500ms、MCP L1 p95 >= 1s、L1+WeKnora p95 >= 3s、错误 source evidence 被接受、current source 存在 pending/running/failed import、Compose 核心服务不健康。

人工 QA 由用户另行执行，不在自动 release gate 中伪造通过状态。
