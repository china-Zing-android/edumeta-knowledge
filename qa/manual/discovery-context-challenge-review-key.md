# MD-First Discovery Context Challenge 人工评审 Key

评审日期基线：2026-07-16。Router 只提供结构化数据，最终自然语言由 Claude/Codex/Hermes 组织。

## 阻断项

- Discovery 或 L1 fact 请求出现 `weknora_ms > 0`。
- Economics 本科主实体不是 `14-1 Economics`，或混入 Economics PhD 作为主实体。
- Course 编号裸显示，未附可读专业名。
- related entity 重复 primary entity，或给出无来源“更强/更好/更数学”等评价。
- `context` 被当作 WeKnora evidence 引用。
- 缺学校时默认 MIT；缺项目的 detail 请求直接全局搜索 WeKnora。
- EECS 材料题 evidence 来自其他项目或本科 degree chart。

## 客观检查点

| Case | 通过标准 |
|---|---|
| MIT | `mode=l1`、`stage=discovery`；大学主实体；列出 3-5 个代表学院/专业；不宣称排名或优势；`weknora_ms=0`。 |
| Economics presence | 直接确认存在 `14-1 Economics`（SB）；相关项包含 `14-2 Mathematical Economics`、`6-14 Computer Science, Economics, and Data Science`；`weknora_ms=0`。 |
| Economics overview | 仍走 discovery；基于 MD 说明院系、学位层级、相关专业和可继续主题；不得为丰富回答主动查 WeKnora。 |
| Multi-program relationship | 三个可读主实体并列；关系原因只使用同校/同院系/同层级/交叉学科等确定性字段；primary 与 related 不重叠。 |
| Upward CS | 返回已入库院校及少量命中项目；不是排名；不调用 WeKnora。 |
| Tuition | Fact Store 原始值 `$66,720`，保留周期、source/review warning；大学 context 存在；不调用 WeKnora。 |
| EECS materials | 允许 `l1_l2`；evidence 只能来自 EECS graduate source，必须有真实 chunk 文本与 knowledge/document ID。 |
| Missing university | `clarification` 且 `missing_slots` 含 `university_id`；不得默认 MIT，不调用 WeKnora。 |

## Agent 呈现顺序

1. 先直接回答用户问题。
2. 再使用 `context.primary_entities/highlights/sample_children` 给必要背景。
3. 最多展示少量 `related_entities`，并解释确定性关系。
4. 最后用 `available_topics` 提示可继续追问的方向，不把它们当作已检索内容。

## WeKnora 关闭回归

关闭 WeKnora 配置后重复前六个非 detail case，结果结构和关键实体必须保持一致，且仍达到 HTTP L1 p95 `< 500ms`。EECS materials 可退化为 `l1_l2 + weknora_unavailable` 或缺 evidence，不得伪造材料答案。
