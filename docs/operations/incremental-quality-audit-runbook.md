# 增量导入质量审计 Runbook

## 目标

每次新增或更新院校 Markdown，都必须检查同一组质量风险。规则适用于所有院校，不允许为单校写例外。`passed` 才可自动发布，`needs_review` 不进入默认批量导入，`failed` 必须阻断。

当前规则集版本：`2026-07-27.1`。

## 五类门禁

| 规则 ID | 检查内容 | 失败示例 | 处理 |
|---|---|---|---|
| `CAT-ENTITY-001` | 目录实体有效性 | `degrees.taxonomy`、`多种`、统计数字、政策字段被识别为专业 | 阻断 |
| `CAT-URL-001` | URL 完整性 | 双域拼接、非法 URL、来源字段损坏 | 阻断 |
| `CAT-DEGREE-001` | 学位与层级一致性 | Minor/本科、MS/PhD、URL 与项目类型错配 | 阻断 |
| `CAT-COVERAGE-001` | 目录完整度 | 文档声明 120 个项目但只解析出 1 个 | 低于 50% 阻断，50%-90% 复核 |
| `CAT-SOURCE-001` | 来源精确度 | 80% 以上专业只关联到学校首页 | 复核，不自动发布 |
| `RET-SCOPE-001` | 发布后检索回归 | 精确项目命中错误、学位过滤泄漏、不存在项目仍返回结果 | 阻断 |

`RET-SCOPE-001` 统一覆盖第五类检索问题，包含正例、层级约束和负例探针。跨校范围检索还必须通过学科分类测试和 QA 回归，不能仅以“OpenSearch 有结果”为通过。

## 自动流程

```text
上传 MD
  -> Parser
  -> pre_publish 静态审计
  -> PostgreSQL staging
  -> OpenSearch 写入 is_current=false
  -> post_publish 检索探针
  -> 两次审计均通过
  -> 激活 OpenSearch 新版本
  -> PostgreSQL current 指针切换
```

发布前失败时不会写入 staging。发布后失败时，新索引记录保持 `is_current=false`，旧 current 继续服务。

审计结果保存在 `ingestion_runs.quality_audits`，通过 `GET /v1/university-ingestions/{run_id}` 查看：

```json
{
  "pre_publish": {
    "audit_status": "passed",
    "audit_version": "2026-07-27.1",
    "matched_rule_ids": [],
    "checks": {},
    "failures": [],
    "warnings": [],
    "before_counts": {},
    "after_counts": {}
  },
  "post_publish": {}
}
```

## 单校预审

```bash
.venv/bin/python scripts/university_md_batch.py preflight \
  --university-id cornell \
  --output /tmp/cornell-preflight.jsonl

jq . /tmp/cornell-preflight.jsonl
```

只有以下条件同时满足才允许上传：

- `status == "passed"`
- Markdown SHA-256 与 `content_sha256` 一致
- `quality_audit.audit_status == "passed"`
- `failures` 为空

## 全量审计

```bash
.venv/bin/python scripts/university_md_batch.py preflight
```

默认结果写入 `data/raw-md/universities/preflight-results.jsonl`。默认批量导入只选择 `passed`。

批量续跑状态同时绑定 `content_sha256` 和 `audit_version`。Markdown 内容或规则集变化后，即使旧状态是 `published`，该院校也会重新进入待导入；旧版状态文件缺少这两个字段时同样不会被错误复用。

升级规则后，旧服务器可能仍保存此前已发布、但现在变为 `needs_review/failed` 的院校。先预览并隔离这些旧 current 数据：

```bash
./scripts/quarantine_unverified_universities.sh
./scripts/quarantine_unverified_universities.sh --apply
```

该命令只处理当前门禁不通过的院校：把 PostgreSQL 院校状态设为不可检索，并将 OpenSearch current 标记关闭。它不会删除历史版本。随后再运行 `import_universities.sh` 重导 276 所 `passed` 院校。

2026-07-27 规则集对 439 所的结果：

- `passed`: 276
- `needs_review`: 75
- `failed`: 88

主要复核原因是专业只关联到学校首页；主要阻断原因是 Markdown 无法形成带有效来源的目录实体。

## 规则沉淀流程

发现新问题后必须完成以下闭环，不能只改线上参数：

1. 保存最小失败 Markdown 或检索请求。
2. 判断它属于现有规则，还是需要新增规则 ID。
3. 先写失败测试并确认 RED。
4. 在 Parser、静态审计或发布后探针的最上游修复。
5. 将规则登记到 `catalog_parser/quality_rules.py`，提升 `QUALITY_RULESET_VERSION`。
6. 运行全量单元测试和 439 所 preflight，比较状态迁移。
7. 对新增 `failed` 和从 `failed` 变为 `passed` 的院校抽样核查。
8. 部署后只重导受影响院校，再跑 30 条 QA 回归。

规则升级不得自动放宽旧失败。任何放宽都必须有合法正例测试，同时保留对应负例测试。

## 部署后 30 问回归

原始 30 问题集保留为修复前基线。部署新门禁后使用问题文本相同的后置题集，其中未通过完整度门禁的 Princeton、墨尔本大学、多伦多大学必须返回 `not_found`，不能继续暴露旧 current 数据。

```bash
docker compose exec -T fast-router \
  python /app/scripts/retrieval_benchmark.py \
  --base-url http://127.0.0.1:8000 \
  --cases /app/qa/live-batch-student-qa-post-audit-2026-07-27.jsonl \
  --runs 5 \
  > qa/reports/live-batch-student-qa-post-audit-server.json
```

查看结果：

```bash
jq '{status,cases,runs,failures,nondeterministic_cases,http_l1_p50_ms,http_l1_p95_ms,http_upward_p95_ms,http_range_p95_ms}' \
  qa/reports/live-batch-student-qa-post-audit-server.json
```

通过要求：

- `status == "passed"`，30 题连续 5 轮无断言失败。
- `nondeterministic_cases` 为空。
- L1、upward、range 的 p95 均小于 1000 ms。
- 被隔离院校明确 `not_found`，通过门禁的院校返回精确项目和层级。

## 发布标准

- 伪实体、双域 URL、硬层级错配：0 条。
- 显式完整目录覆盖率：至少 90%；50%-90% 进入复核，低于 50% 阻断。
- 单一通用来源覆盖 80% 以上目录：进入复核。
- 发布后正例探针 Precision@1：100%。
- 不存在项目负例返回数：0。
- 失败 run 必须带规则 ID、记录 ID、审计阶段和原因。

自动审计不替代人工事实 QA。它保证结构、来源、层级、完整度和检索范围不退化；学费、截止日期等事实是否真实，仍需在部署后按 QA 文档抽样验证。
