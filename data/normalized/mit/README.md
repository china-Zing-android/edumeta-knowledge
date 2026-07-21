# MIT 标准化 JSONL 案例

该目录是 `docs/MIT_知识库_完整深度数据_v2.md` 的预整理结果，可作为其他院校准备结构化数据时的参考案例。

## 文件清单

| 文件 | 数量 | 用途 |
|---|---:|---|
| `catalog_entries.jsonl` | 157 | 本科、辅修和研究生专业目录，一行一个学位/专业条目。 |
| `quick_facts.jsonl` | 241 | 学费、截止时间、语言要求、申请费、资助等关键事实。 |
| `source_registry.jsonl` | 112 | 官网 URL 主账本，记录来源、主题、状态和 WeKnora 导入状态。 |
| `url_manifest.jsonl` | 112 | 专业/事实与官网 URL、WeKnora 文档之间的关联。 |
| `entity_contexts.jsonl` | 158 | 1 条学校总览和 157 条专业上下文，用于返回简介、相关方向和可继续追问的主题。 |

## 数据关系

```text
catalog entry / quick fact
        -> source_id
        -> source_registry + url_manifest
        -> WeKnora 官网页面

catalog entry
        -> entity_context
        -> 专业简介、相关专业、可继续追问内容
```

稳定关联字段是 `entry_id`、`fact_id`、`source_id` 和 `context_id`。不要用数组行号或专业名称作为关联主键。

## 从 Markdown 重新生成

```bash
PYTHONPATH=pipelines/catalog-parser/src .venv/bin/python -m catalog_parser.cli \
  parse-school \
  --university-id mit \
  --input docs/MIT_知识库_完整深度数据_v2.md \
  --out-dir /tmp/mit-normalized

PYTHONPATH=pipelines/catalog-parser/src .venv/bin/python -m catalog_parser.cli \
  validate-school \
  --university-id mit \
  --data-dir /tmp/mit-normalized
```

Parser 重新生成的 `source_registry.jsonl` 和 `url_manifest.jsonl` 是初始导入状态；本目录中的对应文件可能已经包含 WeKnora 运行时回写结果，因此不要用离线生成文件直接覆盖线上 current 数据。

## 是否应该提前整理

批量接入 300 所核心院校时，建议在发布前提前生成并审核这五类 JSONL。这样可以提前发现目录数量错误、事实缺少来源、URL 关联错误和实体上下文不足。

提前整理不等于绕过系统：预整理数据仍必须经过 schema 校验、交叉引用校验、版本 diff、PostgreSQL staging、OpenSearch 发布和 WeKnora URL 导入。当前运行时上传接口接收完整 Markdown；预整理 JSONL 包的运行时上传入口尚未开放。
