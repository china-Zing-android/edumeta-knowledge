# 2026-07 批量院校导入后的准留学生 QA

本题卷只测 HTTP Fast Router 的 L1 行为，服务器当前 `WEKNORA_IMPORT_ENABLED=false`。因此第 29 题用于验证 L2 未就绪时是否明确降级，不用于评价网页正文问答。

## 使用方法

```bash
.venv/bin/python scripts/retrieval_benchmark.py \
  --base-url http://100.74.163.113:8000 \
  --cases qa/live-batch-student-qa-2026-07-24.jsonl \
  --runs 5
```

每题都以真实学生可能使用的表达编写。自动检查返回模式、学校/项目/学位层级、稳定性及 HTTP 延迟；人工评审还必须检查项目名不是统计项、来源 URL 不畸形且确实支持该项目。

| 编号 | 场景 | 学生问题 |
|---|---|---|
| Q01 | 本科专业 | MIT 有 Economics 本科专业吗？ |
| Q02 | 专业代码 | MIT Course 6-4 是什么专业？ |
| Q03 | 辅修 | MIT 有 Astronomy minor 吗？ |
| Q04 | 本科学费 | MIT 本科 2026-2027 学费是多少？ |
| Q05 | 博士语言要求 | MIT EECS PhD 的 TOEFL 和 IELTS 最低要求分别是多少？ |
| Q06 | 博士截止日期 | MIT Economics graduate application deadline 是什么时候？ |
| Q07 | 应有反问 | MIT 研究生申请 deadline 是什么时候？ |
| Q08 | 不存在项目 | MIT 有 Quantum Basket Weaving 本科专业吗？ |
| Q09 | 美国研究生项目 | Harvard 有 Computer Science 研究生项目吗？ |
| Q10 | 美国硕士项目 | Stanford 有 Computer Science MS 吗？ |
| Q11 | 美国硕士项目 | UC Berkeley 有 Computer Science MS 吗？ |
| Q12 | 美国博士项目 | Princeton 有 Computer Science PhD 吗？ |
| Q13 | 美国本科项目 | Cornell 有 Computer Science 本科专业吗？ |
| Q14 | 澳大利亚本科项目 | 墨尔本大学有 Accounting 本科吗？ |
| Q15 | 澳大利亚荣誉学位 | ANU 有 Bachelor of Economics (Honours) 吗？ |
| Q16 | 澳大利亚本科项目 | Monash 有 Computer Science 本科吗？ |
| Q17 | 加拿大本科项目 | McGill 有 Agricultural Economics Major 吗？ |
| Q18 | 加拿大专业选择 | 多伦多大学有 Computer Science 或 Data Science 本科吗？ |
| Q19 | 新加坡本科项目 | NUS 有 Computer Science 本科吗？ |
| Q20 | 新加坡本科项目 | NTU 有 Data Science and Artificial Intelligence 本科吗？ |
| Q21 | 英国本科项目 | UCL 有 Computer Science 本科吗？ |
| Q22 | 英国本科项目 | Cambridge 有 Computer Science 本科吗？ |
| Q23 | 从专业找学校 | 计算机专业的院校有哪些？ |
| Q24 | 带国家范围的专业搜索 | 医学专业的美国院校有哪些？ |
| Q25 | 国家范围浏览 | 美国已入库的核心院校有哪些？ |
| Q26 | 国家范围浏览 | 澳大利亚已入库院校有哪些？ |
| Q27 | 缺少学校 | EECS PhD TOEFL 要求是多少？ |
| Q28 | 不存在学校 | Unknown University 有 Economics 本科吗？ |
| Q29 | L2 暂停降级 | MIT EECS PhD 申请需要提交哪些材料？ |
| Q30 | 不存在项目 | NUS 有 Quantum Basket Weaving 本科专业吗？ |

## 评审口径

- 对“有某专业吗”：返回必须是具体项目，学校、层级与用户问题一致；统计数字、分类名、URL 字符串都不能当作项目。
- 对事实题：原始值、项目范围和来源要一致；`fact_review_required` 是数据审核提醒，不能被 Agent 隐藏。
- 对范围题：结果必须满足国家过滤；“医学”不能被无说明地扩大成全部健康相关项目。
- 对反问/不存在题：不能回退到其他学校，也不能用相似项目填充。
- 对 L2 暂停：必须返回缺少证据的明确状态，不能编造申请材料。
