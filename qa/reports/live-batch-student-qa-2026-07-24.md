# 2026-07 批量院校导入后 L1 准留学生 QA 报告

## 结论

本轮未通过准确性验收，但性能通过。

- 测试对象：`http://100.74.163.113:8000/v1/retrieve`
- 服务状态：345 所 current version 已加载；OpenSearch ready；WeKnora URL 导入关闭。
- 题目：30 条准留学生单轮问题，连续执行 5 轮，共 150 次 HTTP 请求。
- 严格自动通过：22/30，73.3%。
- 固定失败：8/30，每一轮失败项一致；没有不稳定返回。
- L1 HTTP p50：113.486 ms。
- L1 HTTP p95：153.490 ms。
- 上行专业搜索 p95：259.206 ms。
- 国家范围浏览 p95：139.092 ms。

因此，当前实现已经满足“1 秒内返回”的性能目标，但不满足 L1 目录检索的准确性发布目标。建议的最低发布门槛是：P0 错误为 0、严格通过率至少 90%、无明显畸形来源 URL；本轮三项均未达标。

## 测试范围

题卷：[live-batch-student-qa-2026-07-24.md](../manual/live-batch-student-qa-2026-07-24.md)。

它覆盖：

- MIT 的目录、费用、语言要求、截止日期、反问和不存在项。
- 美国、英国、加拿大、澳大利亚、新加坡的本科和研究生项目查询。
- 从专业找院校、按国家找院校。
- 缺失学校、未知学校和不存在项目。
- WeKnora 关闭时的 L2 降级行为。

自动运行原始结果：[live-batch-student-qa-2026-07-24.json](live-batch-student-qa-2026-07-24.json)。

## 通过情况

MIT 基线 Q01-Q08 全部通过：专业、课程号、辅修、学费、EECS 语言要求、Economics 截止日期、模糊问题反问、明显不存在的项目拒答均符合预期。

外校项目中，Harvard CS PhD、Stanford CS MS、Berkeley CS MS、ANU Economics Honours、NUS CS、NTU Data Science and Artificial Intelligence、UCL CS 的项目名称或层级命中；但其中若干来源 URL 不可用，见“来源质量”。

跨校计算机专业、医学专业、美国范围、澳大利亚范围、缺少学校和未知学校的路由模式正确。Q29 在 WeKnora 关闭时返回 `not_found + missing_evidence`，属于明确降级，不是编造申请材料，符合当前环境预期。

## 固定失败的 8 题

| 题目 | 实际返回 | 判定 | 原因 |
|---|---|---|---|
| Q12 Princeton CS PhD | `Interview policy confirmation (Princeton UG does NOT interview) (MArch)` | P0 | 完全无关的 MArch/本科面试政策排在目标项目之前 |
| Q13 Cornell CS 本科 | `Computer Science`，但层级为 `Minor` | P0 | 用户问本科主修，系统返回辅修，学位层级错配 |
| Q14 Melbourne Accounting 本科 | 返回 `Accounting` entity context，缺少项目层级和来源字段 | P1 | 语义接近，但接口没有给出可验证的完整目录记录 |
| Q16 Monash CS 本科 | `Commerce and Computer Science`，来源指向不相关的 Digital Business 页面 | P1 | 联合学位替代了用户问的直接 CS 项目，且来源错配 |
| Q17 McGill Agricultural Economics Major | `Agricultural Economics Honours` | P1 | Major 与 Honours 项目混淆，未返回用户指定项目 |
| Q18 Toronto CS/Data Science 本科 | `多种` | P0 | 摘要词被当作项目，无法回答学生选择问题 |
| Q22 Cambridge CS 本科 | `not_found` | P1 | 已入库院校缺少该真实常见专业的可检索目录记录 |
| Q30 NUS 不存在专业 | `degrees.taxonomy` | P0 | 不存在项被分类/统计项误命中，属于错误肯定回答风险 |

严格正确为 22/30；Q14 只能算“部分命中”，不能计入学生可用的正确答案。

## 来源质量

在 16 条带单校项目或事实来源 URL 的题目中，8 条出现了明显不可用的 URL：域名被重复拼接，或域名错误。例如：

- Harvard：`https://www.harvard.edu/gsas.harvard.edu/program/computer-science`
- Stanford：`https://bulletin.stanford.edu/bulletin.stanford.edu/programs/CS-MS`
- Berkeley：`https://undergraduate.catalog.berkeley.edu/graduate.catalog.berkeley.edu/programs/16201MSG`
- Cornell：`https://catalog.cornell.edu/catalog.cornell.edu/programs/computer-science-ba`
- ANU：`https://www.anu.edu.au/programsandcourses.anu.edu.au/program/HECON`
- Monash：`https://www.monash.edu/www.monash.edu/study/...`
- McGill：`https://b.com/coursecatalogue.mcgill.ca/...`
- UCL：`https://www.ucl.ac.uk/www.ucl.ac.uk/prospective-students/...`

此外，两条跨校专业搜索返回的大量项目来源也有相同的双域拼接模式。即使项目名命中，这些 URL 不能作为给学生点击、也不能作为 WeKnora 后续抓取的官方证据。

## 根因归类

### 1. 摘要表、分类表被当成项目

`多种`、`degrees.taxonomy`、Princeton 的面试政策等不是学位项目，却进入 `catalog_entries` 并被正常排序。这是 Parser 的“表格即目录”假设过宽，没有项目实体有效性闸门。

应拒绝或降级以下内容：纯数字、统计标签、taxonomy、政策标题、URL 字符串、`多种`/`合计`等汇总值。

### 2. URL 规范化错误

批量 Markdown 中存在无 scheme 的绝对域名、相对路径和完整 URL 混用。当前处理把一部分已经是域名的地址当成相对路径拼到文档基础域名后，产生双域 URL。

这不是单校数据问题，必须在 URL 解析层按三类输入统一处理：完整 URL、无 scheme 域名、真正的相对路径。

### 3. 检索排序没有把“用户指定层级”作为强约束

Cornell 的本科主修问题返回 Minor；Monash 的直接 CS 问题返回联合学位；McGill Major 返回 Honours。当前 BM25 命中后没有对 `level/degree_level` 和项目名称精确度做足够的二次排序或拒答。

### 4. 已通过 preflight 不等于完整目录

Cambridge `not_found` 和 Toronto `多种` 说明“至少解析出 5 条”只能证明入库链路有输出，不能证明可用于专业检索。此前的完整性报告已识别该风险，本轮真实 QA 证实它会直接影响用户回答。

### 5. 学科范围过宽

“医学专业的美国院校”会混入公共卫生、健康科学、预医学、医学人类学等记录。技术上可返回相关学校，但对学生而言必须说明这是“医学/健康相关”而不是医学学位项目清单。

## 发布判断

| 闸门 | 目标 | 本轮结果 | 判定 |
|---|---:|---:|---|
| L1 HTTP p95 | < 1 秒 | 153 ms | 通过 |
| 稳定性 | 同题多轮一致 | 30/30 一致 | 通过 |
| 严格项目/层级准确率 | >= 90% | 73.3% | 不通过 |
| P0 错项目/错误肯定 | 0 | 4 个案例 | 不通过 |
| 返回来源 URL 可用性 | 100% | 单校来源题中至少 8/16 明显畸形 | 不通过 |
| WeKnora 关闭时不强答 | 100% | Q29 明确 `missing_evidence` | 通过 |

当前不建议把 345 所作为统一质量等级对外发布。MIT 可以继续作为完整基线；其他院校应至少先完成“目录实体有效性 + URL 规范化 + 学位层级排序 + 逐校完整性对账”四个修复闸门，再扩大真实用户测试。

## 复跑命令

```bash
.venv/bin/python scripts/retrieval_benchmark.py \
  --base-url http://100.74.163.113:8000 \
  --cases qa/live-batch-student-qa-2026-07-24.jsonl \
  --runs 5 \
  --output-path qa/reports/live-batch-student-qa-2026-07-24.json
```

本轮只记录问题和证据，不修改检索、Parser 或远端已发布数据。
