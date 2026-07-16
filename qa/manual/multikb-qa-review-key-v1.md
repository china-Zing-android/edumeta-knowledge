# 多院校 L1 + WeKnora 人工 QA 评审答案 v1

## 评分原则

每题检查五项：范围、结论、证据、缺失处理、响应时间。以下情况直接阻断：

- 返回错误学校、项目或学位层级。
- evidence URL 存在，但正文不支持 Agent 的结论。
- 没有 evidence 却对申请资格、材料、截止日期、费用或分数作确定回答。
- `upward/range` 调用了 WeKnora，即 `weknora_ms > 0`。
- HTTP 原始结构正确，但 Agent 改写后引入新事实。
- 当前状态为已知失败的诊断题被标记为“通过”。

## 客观答案

| ID | 预期检查点 |
|---|---|
| D01 | `mode=l1`；至少命中 MIT Economics，Course `14-1`，SB；不得返回其他学校。 |
| D02 | `mode=l1`；Course `6-4` 为 Artificial Intelligence and Decision Making。 |
| D03 | `mode=l1`；Caltech Computer Science 本科 SB；HTTP 必须显式传 `university_id=caltech`。 |
| D04 | `mode=l1`；Duke 至少命中 Computer Science BA/BS；HTTP 必须显式传 `university_id=duke`。 |
| D05 | `mode=l1`；原始 tuition 值 `$66,720`，必须带数据周期和来源；不可把总就读成本当学费。 |
| D06 | `mode=l1`；EECS TOEFL `100`、IELTS `7`；不得混入其他项目标准。 |
| U01 | `mode=upward`；当前应返回 `caltech, duke, mit, stanford`，每校有 `matched_programs`；`weknora_ms=0`。 |
| U02 | `mode=upward`；当前应返回 `caltech, duke, mit`；`weknora_ms=0`。 |
| U03 | `mode=upward`；当前应返回 `caltech, duke, mit`；例如 Medical Engineering、Biomedical Engineering、Health Sciences and Technology；`weknora_ms=0`。 |
| R01 | `mode=range`；只返回 `caltech, stanford`；`weknora_ms=0`。 |
| R02 | `mode=range`；只返回 `duke`；`weknora_ms=0`。 |
| R03 | `mode=not_found`，`matches=[]`；不能调用外部发现或返回未入库学校。 |
| X01 | 没有学校范围时应 `clarification`，`missing_slots` 包含 `university_id`；不能默认 MIT。 |
| X02 | `mode=not_found`；不能回退到 MIT 或相似学校。 |
| X03 | 显式 `direction=upward` 时应 `clarification`，`missing_slots` 包含 `discipline`。 |
| E01 | `mode=l1_l2`；来源必须为 MIT EECS graduate 页面。证据至少覆盖 online application、两篇 essay、三封推荐信、transcripts、英语成绩；GRE not required 可作为补充。 |
| E02 | 应使用同一个 MIT EECS graduate source；结论应说明不提供独立 terminal master's，未持硕士的 PhD 学生会先取得 SM，MEng 面向 MIT 本科生。若召回本科 degree chart 为主要证据则失败。 |
| E03 | 当前是诊断题。此前返回 `not_found`，不能算通过。只有对应 Caltech source 导入成功且返回 scoped evidence 后才能转为正式通过题。 |
| E04 | 当前是诊断题。此前返回 `not_found`，不能算通过。只有对应 Duke source 导入成功且返回 scoped evidence 后才能转为正式通过题。 |
| M01 | 第二轮必须切换到 Duke，不能沿用 MIT scope；应返回 Duke Computer Science BA/BS。 |
| M02 | 第二轮只保留 California 范围，应返回 Caltech、Stanford；不得继续显示 Duke、MIT。 |
| M03 | 两轮都保持 MIT EECS scope；第二轮应得到 TOEFL `100`，不得切换到其他 MIT 项目。 |
| I01 | 状态为 `unchanged`；`weknora_jobs={}` 或没有新增 job；current version 和 KB ID 不变。 |
| I02 | `operation=update`、最终 `status=published`、`weknora_kb_operation=reuse`；current 唯一；未变化 URL 继承原 knowledge ID。 |
| I03 | 新院校默认为 `weknora_kb_operation=create` 且绑定独立 KB；显式目标为 `explicit`；强制新建为 `create`，不得写入其他学校 KB。 |

## 时间门槛

- L1、upward、range：单次 `total_ms < 1000`，正式报告看 5 次运行的 p95。
- L1、upward、range：`weknora_ms = 0`。
- 已 ready 的 L2：目标 `total_ms < 1000`；超时或远端波动必须保留 `trace_id` 单独归因。
- MCP 比 HTTP 多出的转发耗时不应改变 `mode/matches/evidence` 语义。

## 当前基线说明

2026-07-16 的实测基线：

- D01 HTTP 约 `62 ms`。
- U01 HTTP 约 `25 ms`，返回 Caltech、Duke、MIT、Stanford。
- R01 HTTP 约 `32 ms`，返回 Caltech、Stanford。
- E01 HTTP 约 `692 ms`，其中 WeKnora 约 `630 ms`。
- E03、E04 是已知诊断失败，不属于当前通过集。

正式验收必须重新执行，不能直接引用本基线代替测试结果。
