# 数据导入 Runbook

```bash
.venv/bin/python scripts/router_cli.py ingest-school \
  --university-id mit --school-tier core \
  --university-name "Massachusetts Institute of Technology" \
  --country-code US --region Massachusetts \
  --file docs/MIT_知识库_完整深度数据_v2.md

.venv/bin/python scripts/router_cli.py ingestion-status --run-id <run_id>
```

HTTP 等价调用为 `POST /v1/university-ingestions` 和 `GET /v1/university-ingestions/{run_id}`。CLI 不实现第二条导入链路。

流水线：持久化原始 MD，解析 catalog/fact/source，提取 Markdown link/autolink/bare URL，执行发布前质量审计，PG staging，继承未变化 URL 的 WeKnora 状态，以 `is_current=false` 写入 OpenSearch，执行发布后检索探针，通过后切换 current version，异步消费 WeKnora job。

相同 MD、parser contract 和院校元数据返回 `unchanged`，不发布索引也不新增 job。单 canonical URL 变化只新增一个 WeKnora job。版本切换时未完成 URL 会在新 current 版本续接轮询。解析、审计或索引失败保留旧 current version。

审计规则、状态解释和规则升级流程见 `docs/operations/incremental-quality-audit-runbook.md`。

KB 选择：

```bash
# 默认：新院校创建 KB；同院校更新复用已绑定 KB
.venv/bin/python scripts/router_cli.py ingest-school ...

# 更新或切换到指定 KB
.venv/bin/python scripts/router_cli.py ingest-school ... \
  --weknora-knowledge-base-id <kb_id>

# 强制创建并重新绑定新 KB
.venv/bin/python scripts/router_cli.py ingest-school ... \
  --create-new-weknora-kb
```

完整的人工测试、同校完整快照更新和新学校接入步骤见
`docs/operations/manual-testing-and-incremental-ingestion.md`。
