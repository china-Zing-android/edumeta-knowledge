# MIT 标准化 JSONL 案例

该目录是 `docs/MIT_知识库_完整深度数据_v2.md` 的预整理结果，可以作为其他院校准备结构化数据时的参考案例。这些文件共同组成一所院校的“标准化知识数据包”。

## 文件中文名称与主要意义

| 文件 | 中文名称 | 数量 | 主要意义 |
|---|---|---:|---|
| `catalog_entries.jsonl` | 专业与学位目录表 | 157 | 记录学校有哪些本科专业、辅修和研究生项目。 |
| `quick_facts.jsonl` | 关键事实表 | 241 | 记录学费、截止日期、语言要求、申请费和资助等明确事实。 |
| `source_registry.jsonl` | 官网来源登记表 | 112 | 管理所有官网 URL，记录来源状态以及 WeKnora 导入状态。 |
| `url_manifest.jsonl` | URL 关联清单 | 112 | 说明每个官网页面与哪些专业、主题以及 WeKnora 文档关联。 |
| `entity_contexts.jsonl` | 学校与专业上下文表 | 158 | 提供学校概览、专业说明、相关专业和可以继续追问的内容。 |
| `README.md` | 数据包使用说明 | 1 | 解释文件用途、关联方式、生成方法和使用边界。 |

## 1. 专业与学位目录表

文件：`catalog_entries.jsonl`，共 157 条。

一行代表一个可以检索的专业或学位项目，例如：

```text
MIT
-> School of Humanities, Arts, and Social Sciences
-> Economics Department
-> 本科
-> SB
-> Course 14-1 Economics
```

主要用于回答：

- MIT 有 Economics 本科专业吗？
- Course 6-4 是什么专业？
- MIT 有哪些计算机相关专业？
- 哪些学校开设物理专业？

MIT 的 157 条目录由以下内容组成：

```text
本科 SB：55 条
本科 Minor：17 条
研究生项目：85 条
合计：157 条
```

## 2. 关键事实表

文件：`quick_facts.jsonl`，共 241 条。

一行只记录一个明确事实，例如：

```text
MIT 本科学费 = 66,720 美元
MIT EECS PhD TOEFL 最低要求 = 100
MIT EECS PhD IELTS 最低要求 = 7.0
MIT Economics PhD 截止日期 = 12 月 15 日
```

主要用于快速回答：

- 学费是多少？
- 申请截止日期是什么时候？
- TOEFL 最低要求是多少？
- GRE 是否需要？
- 申请费是多少？
- PhD 如何资助？

每条事实都关联一个 `source_id`，用于说明这个数字或规则来自哪个官网页面。

## 3. 官网来源登记表

文件：`source_registry.jsonl`，共 112 条。

它是所有官网 URL 的“管理账本”。一行代表一个官网来源，例如：

```text
MIT Economics 14-1 课程页面
MIT EECS 研究生申请页面
MIT 本科学费页面
MIT 本科申请截止日期页面
```

主要记录：

- 官网地址。
- 来源属于哪个学校。
- 页面类型和涉及主题。
- 页面关联哪些专业。
- 是否为官方来源以及当前是否有效。
- 是否已经导入 WeKnora。
- 导入失败时的错误原因。

它决定“系统承认哪些 URL 是有效来源”。

## 4. URL 关联清单

文件：`url_manifest.jsonl`，共 112 条。

它相当于 L1 和 WeKnora 之间的“地址簿”，负责说明：

```text
这个专业或事实
-> 对应哪个 source_id
-> 对应哪个官网 URL
-> 对应哪个 WeKnora 知识库
-> 对应哪个 WeKnora 文档
```

例如：

```text
14-1 Economics
-> MIT Economics 课程页面
-> curriculum 主题
-> WeKnora 中对应的网页文档
```

主要用于：

- 限定 WeKnora 只查询相关页面。
- 防止检索到其他学校或其他专业。
- 判断 URL 是否导入成功。
- URL 更新时只更新受影响页面。

`source_registry` 负责管理 URL 本身，`url_manifest` 负责管理 URL 与专业、事实和 WeKnora 文档之间的关系。

## 5. 学校与专业上下文表

文件：`entity_contexts.jsonl`，共 158 条。

组成方式：

```text
MIT 学校总览：1 条
MIT 专业上下文：157 条
合计：158 条
```

它用于解决“回答只有有或没有，过于生硬”的问题。

例如用户问：

```text
MIT 有 Economics 本科专业吗？
```

只有目录表时，系统通常只能回答：

```text
有，Course 14-1 Economics。
```

加入上下文后，还可以提供：

- 所属学院和院系。
- 学位类型。
- 专业编号的含义。
- 相关专业。
- 可以继续查询哪些内容。

例如：

```text
MIT 提供 Course 14-1 Economics 本科 SB 专业，
隶属经济学系和 SHASS。

相关方向包括：
- 14-2 Mathematical Economics
- 6-14 Computer Science, Economics, and Data Science

还可以继续查询课程设置、学费和本科申请要求。
```

它不会代替 WeKnora。具体课程清单、完整申请材料和官网政策说明等页面细节仍由 WeKnora 提供。

## 6. 数据包使用说明

文件：`README.md`。

它不是检索数据，而是给数据准备人员和开发人员看的说明文件，主要解释：

- 每个 JSONL 文件的作用。
- 文件之间如何关联。
- 每类数据应该如何整理。
- 如何从 Markdown 重新生成。
- 哪些字段必须保持稳定。
- 哪些运行状态不能被离线文件覆盖。

## 文件关系

可以把整体关系理解为：

```text
专业与学位目录表
        ↓
学校与专业上下文表
        ↓
关键事实表
        ↓
官网来源登记表
        ↓
URL 关联清单
        ↓
WeKnora 官网全文
```

更准确的数据关联方式是：

```text
catalog entry / quick fact
        -> source_id
        -> source_registry + url_manifest
        -> WeKnora 官网页面

catalog entry
        -> entity_context
        -> 专业简介、相关专业、可继续追问内容
```

稳定关联字段是 `entry_id`、`fact_id`、`source_id` 和 `context_id`。不要使用数组行号或可能变化的专业名称作为关联主键。

一句话概括：

```text
catalog_entries：学校有什么
quick_facts：明确数字和规则是什么
source_registry：信息来自哪个官网
url_manifest：官网与专业、事实、WeKnora 如何关联
entity_contexts：如何让回答更完整、更像给学生讲解
README：如何正确生产和使用这些数据
```

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

Parser 重新生成的 `source_registry.jsonl` 和 `url_manifest.jsonl` 是初始导入状态。本目录中的对应文件可能已经包含 WeKnora 运行时回写结果，因此不要用离线生成文件直接覆盖线上 current 数据。

## 是否应该提前整理

批量接入 300 所核心院校时，建议在发布前提前生成并审核这五类 JSONL。这样可以提前发现目录数量错误、事实缺少来源、URL 关联错误和实体上下文不足。

提前整理不等于绕过系统：预整理数据仍必须经过 schema 校验、交叉引用校验、版本 diff、PostgreSQL staging、OpenSearch 发布和 WeKnora URL 导入。当前运行时上传接口接收完整 Markdown；预整理 JSONL 包的运行时上传入口尚未开放。
