# MIT 人工 QA 评审答案 v1

> 评审前先阅读 `qa/manual/md-first-l1-weknora-qa-guide.md`。特别检查：L1 discovery/fact
> 的 `weknora_ms` 必须为 0；只有明确 detail 且 scope 已解析时允许 WeKnora；`context`
> 不是 evidence；当前数据不支持的排名、优势和录取概率不得强答。

## 评分规则

每题五项，每项 `0-2` 分：

```text
route_and_scope       路由、学校、项目、学位层级是否正确
answer_correctness    结论和原始值是否正确
evidence_match        引用是否真实支持结论
uncertainty_handling  模糊或缺证据时是否反问/保留不确定性
task_completion       是否完成用户实际任务
```

单题满分 10 分，`>= 8` 为通过。以下任一项直接判定阻断：

- 错学校、错项目、错学位层级。
- 引用 URL 存在，但内容不支持结论。
- 没有证据却给出确定性申请资格、deadline、费用或分数。
- 模糊问题不反问，擅自选择项目。
- L2 问题引用本科 degree chart 代替对应研究生项目页面。

## 客观检查点

| ID | 预期行为与事实检查点 |
|---|---|
| Q01 | `l1`；应命中 Economics，Course `14-1`，SB，本科目录来源。 |
| Q02 | `l1`；Course `6-4` 为 Artificial Intelligence and Decision Making。 |
| Q03 | `l1`；Course `6-9` 为 Computation and Cognition；不得答成通用 CS。 |
| Q04 | `l1`；应命中 Course `6-14`，Computer Science, Economics, and Data Science。 |
| Q05 | `l1`；存在 Astronomy Minor。 |
| Q06 | `l1`；Course `16` 为 Aerospace Engineering。 |
| Q07 | `l1`；EECS 来源；TOEFL `100`、IELTS `7`。不得混入其他项目标准。 |
| Q08 | `l1`；Biology 来源；IELTS `6.5`、TOEFL `100`。 |
| Q09 | `l1`；Economics 来源；`December 15 at 11:59 PM Eastern Time`。 |
| Q10 | `l1`；Microbiology 来源；申请费 `$90.00`。 |
| Q11 | `l1`；本科 tuition 原始值 `$66,720`，应说明数据周期和来源。 |
| Q12 | `l1`；Early Action `November 1`，Regular Action `January 5`。 |
| Q13 | `l1`；EECS 来源；应表达 fellowship/RA/TA 及全额资助语义。事实目前带 `review_required` 时，Agent 不应包装成无条件保证。 |
| Q14 | `l1`；Economics 来源；当前原始值为 `Required`。 |
| Q15 | `l1_l2`；只接受 EECS graduate 页面证据。至少覆盖 online application、两篇 essay、三封推荐信、transcripts、英语成绩；不得引用本科 6-3 degree chart 作为主要证据。 |
| Q16 | `l1_l2`；只接受 Sloan MBA 项目证据。应覆盖申请材料、GRE/GMAT、费用或轮次 deadline 中与问题相关的内容。 |
| Q17 | `l1_l2`；必须使用 EECS graduate evidence。若证据未明确规定本科专业限制，应明确“当前证据未发现绝对禁止/仍需按项目要求评估”，不得自行保证可录取。 |
| Q18 | `l1_l2`；必须使用 Biology 项目 evidence。若页面没有明确跨专业资格结论，应说明证据边界，不得从常识推断。 |
| Q19 | `l1_l2`；只接受 Microbiology 项目 evidence，应给材料/考试/截止日期等实际证据，不得混入 Biology 或 EECS。 |
| Q20 | 应纠正问题前提并使用 EECS graduate evidence：EECS 不提供 terminal master's；MEng 仅面向 MIT 本科生；PhD 路径中可先取得 SM。若主要召回 6-3、6-7、18-C 本科 degree chart，判失败。 |
| Q21 | `clarification`；必须追问具体研究生项目，不能给出一个 MIT 全校 deadline。 |
| Q22 | `clarification`；至少追问本科/研究生以及具体项目。 |
| Q23 | 应先澄清申请类别和教育经历，并要求核对 MIT 官方 eligibility；当前检索模块若只返回 `clarification` 可通过路由项。Agent 不得无证据直接断言“能”或“不能”。 |
| Q24 | `clarification`；缺少大学，必须先问学校，不能默认 MIT。 |
| Q25 | `not_found`；不能回退到 MIT 或返回其他学校。 |
| Q26 | `not_found`；不能用相似专业凑结果。 |
| Q27 | 三轮都保持 EECS scope；依次应得到 TOEFL 100、December 1 11:59 PM ET、EECS funding；不得跨到其他项目。 |
| Q28 | 三轮都保持 Biology scope；依次应得到 IELTS 6.5/TOEFL 100、December 1 11:59 PM ET、GRE not required。 |
| Q29 | 第一轮返回本科 Course 14-1；第二轮必须切换到 Economics graduate source 和 December 15 deadline。 |
| Q30 | 第二轮必须切换到 unknown scope 并返回 not found；不得沿用第一轮 MIT 结果。 |

## 整体验收线

- P0：Q07-Q14 事实错误数为 `0`。
- 错学校/错项目 evidence 为 `0`。
- Q21-Q24 合理反问率 `100%`。
- Q25-Q26 无关结果填充数为 `0`。
- Q27-Q30 多轮 scope 串线数为 `0`。
- 30 题总通过率建议 `>= 90%`；Q20 是重点挑战题，不应因为其难度而降低阻断标准。
