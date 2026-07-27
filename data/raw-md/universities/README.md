# 批量院校 Markdown 数据集

该目录保存 2026-07 批次的院校完整 Markdown 原始资料，并作为增量上传 Fast Router 的输入。

## 目录统计

| 国家/地区目录 | Markdown 数量 |
|---|---:|
| `us` | 242 |
| `uk` | 98 |
| `ca` | 48 |
| `au` | 39 |
| `ie` | 8 |
| `sg` | 7 |
| `nz` | 5 |
| `ch` | 1 |
| 合计 | 448 |

`manifest.jsonl` 将同校重复文件归并后启用 439 所，9 份重复文件保留原文但不自动导入。跨国家同名学校使用不同稳定 ID，例如：

```text
Southern Methodist University -> us_smu
Singapore Management University -> sg_smu
```

## 文件说明

| 文件 | 用途 |
|---|---|
| `<country>/*.md` | 原始院校 Markdown，禁止批量改写。 |
| `manifest.jsonl` | 稳定学校 ID、国家、名称、别名、文件哈希和重复归并结果。 |
| `preflight-results.jsonl` | Parser、schema、交叉引用、五类质量审计和复核/阻断结果。 |
| `parser-compatibility-results.jsonl` | 逐校记录旧 Parser 与当前 Parser 的对照结果，并区分直接兼容、升级后兼容、条件审核和禁止导入。 |
| `README.md` | 批次结构、限制和运行方法。 |

## 当前质量闸门

全量 439 所启用学校的离线 preflight 结果：

```text
passed: 276
needs_review: 76
failed: 87
```

- `passed`：实体、URL、层级、完整度、来源精确度审计通过，允许一键导入。
- `needs_review`：结构可入库，但目录过少、显式完整度不足，或大量专业只关联学校首页，默认不导入。
- `failed`：伪实体、URL/层级冲突、严重目录残缺，或无法形成带来源的目录实体，默认不导入。

一键导入只选择 `passed` 且文件 SHA-256 与 preflight 完全一致的学校。修改任何 Markdown 后必须重新生成 manifest 并重新 preflight。

`passed` 表示 L1 结构与检索发布门禁可通过，不表示已经达到 MIT 的事实提取和人工 QA 完整度。规则说明见 `docs/operations/incremental-quality-audit-runbook.md`。

## 一键导入

先在 `.env` 中暂停 WeKnora URL 导入：

```text
WEKNORA_IMPORT_ENABLED=false
```

更新并重建 Fast Router 后，先查看待导入范围：

```bash
./scripts/import_universities.sh --dry-run --country US --limit 5
```

导入 5 所美国院校：

```bash
./scripts/import_universities.sh --country US --limit 5
```

导入指定学校：

```bash
./scripts/import_universities.sh --university-id cornell
```

导入全部通过闸门的院校：

```bash
./scripts/import_universities.sh
```

命令逐校执行 `upload -> wait published -> next`，状态保存在 Docker volume `batch_import_state` 中。命令中断后重新运行会跳过已经 `published/unchanged` 的学校。

## 重新生成闸门文件

在开发环境执行：

```bash
.venv/bin/python scripts/university_md_batch.py manifest
.venv/bin/python scripts/university_md_batch.py preflight
```

preflight 存在失败时返回非零退出码，这是发布闸门的正常行为；通过的学校仍会完整记录在结果文件中。
