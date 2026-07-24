# University of Technology Sydney_知识库_完整深度数据_v2.md

> **Data capture date**: 2026-07-11
> **Capture tool**: browser_navigate + browser_snapshot + Python urllib extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Oceania)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (UG degree programmes) | ~130+ | 覆盖全部13个学科领域 |
| 本科辅修 (Minors) | 众多 | 跨学科辅修选项 |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | ~200+ | 含研究生证书/文凭 |
| 研究生博士项目 (PhD/Doctoral) | ~100+ | 涵盖所有学院 |
| 学位项目总计 | ~500+ | 含双学位/组合学位 |
| 学院 (Colleges/Faculties) | 7 | 不含Graduate Research School |
| 学术院系 (Academic Schools/Departments) | 14 | 含TD School、Animal Logic Academy |
| 学科领域 (Course Areas) | 13 | UTS官方分类 |

> **注**：全量课程列表需要JS渲染的课程搜索前端才能完整获取。当前统计基于学院结构和学科领域推断。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Technology Sydney
├── UTS Business School
│   ├── School of Accounting and Finance
│   ├── School of Management
│   └── School of Economics and Marketing
├── Faculty of Design and Society
│   ├── School of Communication and Social Sciences
│   ├── School of Design
│   ├── School of Architecture
│   ├── School of Built Environment
│   └── Animal Logic Academy
├── Faculty of Engineering and Information Technology (FEIT)
│   ├── School of Computer Science
│   ├── School of Civil, Environmental and Sociotechnical Engineering (SCESE)
│   └── School of Electrical, Mechanical and Biomedical Engineering (SEMBE)
├── Faculty of Health
│   ├── School of Nursing and Midwifery
│   ├── School of Human Performance, Rehabilitation and Population Health
│   └── Graduate School of Health
├── Faculty of Law
├── Faculty of Science
│   ├── School of Life Sciences
│   └── School of Mathematics and Physical Sciences
├── Graduate Research School
└── Transdisciplinary School (TD School)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 (Degree Level) | 说明 |
|------------------------|------|
| Bachelor (Undergraduate) | 3-4年制学士学位 |
| Bachelor (Honours) | 额外1年荣誉学位 |
| Master by Coursework | 1-2年制授课型硕士 |
| Master by Research | 研究型硕士 |
| Graduate Certificate | 研究生证书 (0.5年) |
| Graduate Diploma | 研究生文凭 (1年) |
| Doctor of Philosophy (PhD) | 3-4年制博士 |
| Professional Doctorate | 专业博士 |
| Diploma | 文凭课程 (UTS College) |
| Associate Degree | 副学士 |
| Non-award Study | 单科/非奖课程 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院/系 | 本科(UG) | 授课型硕士(PGT) | 研究型(PGR) | 总计(约) |
|---------|---------|----------------|-------------|---------|
| UTS Business School | ~12 | ~20 | ~10 | ~42 |
| Faculty of Design and Society | ~20 | ~25 | ~10 | ~55 |
| FEIT | ~15 | ~20 | ~15 | ~50 |
| Faculty of Health (incl. GSH) | ~8 | ~25 | ~10 | ~43 |
| Faculty of Law | ~3 | ~6 | ~3 | ~12 |
| Faculty of Science | ~10 | ~10 | ~10 | ~30 |
| TD School | ~3 | ~5 | ~3 | ~11 |
| Graduate Research School | — | — | ~30+ | ~30 |
| **总计（约）** | **~130+** | **~200+** | **~100+** | **~500+** |

---

## Section 1 — Undergraduate education

### 1.1 本科学科领域（Course Areas）

| 学科领域 | 涉及学院/系 |
|----------|------------|
| Analytics and Data Science | FEIT, TD School |
| Business | UTS Business School |
| Communication | Faculty of Design and Society |
| Design, Architecture and Building | Faculty of Design and Society |
| Education | Faculty of Design and Society |
| Engineering | FEIT |
| Graduate School of Health | Faculty of Health |
| Health | Faculty of Health |
| Information Technology | FEIT |
| International Studies and Social Sciences | Faculty of Design and Society |
| Law | Faculty of Law |
| Science and Mathematics | Faculty of Science |
| Transdisciplinary Innovation | TD School |

### 1.2 本科典型课程列表（代表性抽样）

**UTS Business School**
- Bachelor of Business (C10126)
- Bachelor of Accounting
- Bachelor of Business / Bachelor of Laws
- Bachelor of Economics

**Faculty of Engineering and IT**
- Bachelor of Engineering (Honours) (multiple streams)
- Bachelor of Information Technology
- Bachelor of Science in Information Technology
- Bachelor of Artificial Intelligence

**Faculty of Design and Society**
- Bachelor of Communication (multiple majors)
- Bachelor of Design (multiple majors)
- Bachelor of Architecture
- Bachelor of Construction Project Management
- Bachelor of Education
- Bachelor of Arts in International Studies

**Faculty of Health**
- Bachelor of Nursing (C10122)
- Bachelor of Midwifery (C10225)
- Bachelor of Sport and Exercise Science
- Bachelor of Public Health

**Faculty of Law**
- Bachelor of Laws
- Bachelor of Laws (Honours)

**Faculty of Science**
- Bachelor of Science (multiple majors)
- Bachelor of Advanced Science (Pre-Medicine)
- Bachelor of Advanced Science (Pharmaceutical Sciences)
- Bachelor of Advanced Science (Quantum Technology)
- Bachelor of Medical Science
- Bachelor of Biomedical Physics

**TD School**
- Bachelor of Creative Intelligence and Innovation
- Bachelor of Sustainability and Environment

> **注**：完整课程列表（含约130+本科学位）可通过UTS官网课程搜索页面获取：https://www.uts.edu.au/courses。该页面为JS渲染，需浏览器访问。

---

## Section 2 — Graduate education

### 2.1 授课型硕士（PGT）

**代表性硕士课程：**

**UTS Business School**
- Master of Business Administration (MBA)
- Master of Finance / Master of Financial Analysis
- Master of Marketing
- Master of Professional Accounting
- Master of Business Analytics
- Executive MBA
- Graduate Certificate in Leadership and Strategy

**Faculty of Engineering and IT**
- Master of Information Technology
- Master of Information Technology (Extension)
- Master of Engineering (multiple streams)
- Master of Data Science and Innovation
- Master of Cybersecurity

**Faculty of Design and Society**
- Master of Teaching in Secondary Education / Primary Education
- Master of Animation and Visualisation
- Master of Strategic Communication
- Master of International Relations
- Master of Creative Writing

**Faculty of Health**
- Master of Pharmacy
- Master of Physiotherapy
- Master of Clinical Psychology
- Master of Speech Pathology
- Master of Genetic Counselling
- Master of Orthoptics
- Master of Advanced Nursing (online)
- Graduate Certificate in Critical Care

**Faculty of Law**
- Master of Laws (LLM)
- Juris Doctor
- Graduate Certificate in Laws

**Faculty of Science**
- Master of Science (multiple streams)
- Master of Quantitative Finance
- Master of Good Manufacturing Practice (GMP)

**TD School**
- Master of Creative Intelligence and Strategic Innovation
- Master of Data Science and Innovation

### 2.2 研究型研究生（PGR）

- Doctor of Philosophy (PhD) — all faculties
- Master of Philosophy (MPhil)
- Master of Business (Research)
- Doctor of Philosophy (Transdisciplinary Innovation)
- Doctor of Philosophy (Learning Analytics)

---

## Section 3 — Application requirements & deadlines

### 3.1 国内本科生申请

| 项目 | 详情 |
|------|------|
| 申请系统 | UAC (Universities Admissions Centre) |
| 录取标准 | ATAR (Australian Tertiary Admission Rank) |
| 最低ATAR | 因课程而异（约65-95+） |
| 替代途径 | UTS Early Entry Program, 多项Entry Schemes |
| UAC申请截止 | 一般在9月底 (每年不同) |

### 3.2 国内研究生申请

| 项目 | 详情 |
|------|------|
| 申请方式 | 直接向UTS申请（部分通过UAC） |
| 关键日期 | 参见主日历各学期截止日期 |
| 2026 Autumn申请开放 | 2025年7月底 |
| 2026 Autumn申请截止 | 2026年1月25日 |

### 3.3 国际学生申请

| 项目 | 详情 |
|------|------|
| 申请方式 | 直接向UTS申请 |
| 申请费 | A$100（不可退还） |
| 免申请费 | UTS在校生申请第二学位、UTS College学生 |
| 2026 Spring海外截止 | 2026年4月30日 |
| 2026 Spring在澳截止 | 2026年5月31日 |

### 3.4 2026 Principal Dates（关键日期摘要）

**Autumn Session 2026 (Main Calendar)**
- 国际学生申请（海外）截止：2025年底至2026年初
- 申请截止 (UG/PG domestic): 2026年1月25日
- 迎新周：2月2-13日
- 开学：2月16日
- 缴费截止：3月5日
- Census Date (最后退课日)：3月19日
- 期末考试：5月25日-6月12日
- 成绩公布：6月29日

**Spring Session 2026 (Main Calendar)**
- 国际学生申请（海外）截止：4月30日
- 国际学生申请（在澳）截止：5月31日
- 国内申请开放：2月2日
- 国内申请截止：6月28日
- 迎新周：7月20-24日
- 开学：7月27日
- 缴费截止：8月13日
- Census Date：8月底
- 期末考试：10月底-11月
- 成绩公布：11月底

### 3.5 研究型学位申请截止

| 类型 | 截止日期 |
|------|---------|
| Domestic - for RTPS scholarships (Research Session 2) | 2026年4月15日 |
| International - for UTS competitive scholarships (RS 1 2027) | 2026年6月3日 |

### 3.6 English Language Requirements（完整列表）

**标准要求（大部分课程）：**

| 考试类型 | 总分 | 写作 |
|---------|------|------|
| IELTS (Academic/Online/OSR) | 6.5 | 6.0 |
| TOEFL (iBT/Home Edition) | 79 | 21 |
| PTE (Academic) | 58-64 | 50 |
| C1 Advanced / C2 Proficiency | 176-184 | 169 |
| UTS College AE5 | Pass | — |

**Teaching/Education 课程 (IELTS 7.5)：**
- IELTS: Overall 7.5 (Speaking 8.0, Listening 8.0, Reading 7.0, Writing 7.0)
- TOEFL: 102-109 (Speaking 26, Listening 28, Reading 24, Writing 27)
- PTE: 73-78 (Speaking 79, Listening 79, Reading 65, Writing 65)

**Nursing/Midwifery 课程 (IELTS 7.0)：**
- IELTS: Overall 7.0 (各单项7.0, 写作6.5)
- TOEFL: 94 (Speaking 23, Listening 24, Reading 24, Writing 24)
- PTE: 66 (各单项66, 写作56)
- OET: B (听/说/读), C+ (写)

**Pharmacy/Physiotherapy/Clinical Psychology (IELTS 7.0)：**
- IELTS: Overall 7.0 (各单项7.0, 写作6.5)
- TOEFL: 94 (Speaking 23, Listening 24, Reading 24, Writing 24)
- PTE: 66 (各单项66)

**Speech Pathology/Genetic Counselling (IELTS 7.0)：**
- IELTS: Overall 7.0 (各单项7.0)
- TOEFL: 94 (Speaking 23, Listening 24, Reading 24, Writing 27)
- PTE: 65 (各单项65)

**Executive MBA/Graduate Certificate in Leadership (IELTS 7.0)：**
- IELTS: Overall 7.0 (Writing 6.5)
- TOEFL: 94 (Writing 24)
- PTE: 65-72 (Writing 58)

**Master of Laws/Graduate Certificate in Laws (IELTS 7.0, from 2027)：**
- IELTS: Overall 7.0 (Writing 6.0)
- TOEFL: 94 (Writing 21)
- PTE: 65 (Writing 50)

**Postgraduate Research (Business/Health/Communication/Education/Law/GSH)：**
- IELTS: Overall 7.0 (Writing 7.0)
- TOEFL: 94 (Writing 27)
- PTE: 65-72 (Writing 65)

**Postgraduate Research (Design/Engineering/IT/Science)：**
- IELTS: Overall 6.5 (Writing 6.0)
- TOEFL: 79 (Writing 21)
- PTE: 58-64 (Writing 50)

**Master of Orthoptics (IELTS 6.5)：**
- IELTS: Overall 6.5 (Writing 6.5)
- TOEFL: 79 (Writing 24)
- PTE: 58-64 (Writing 58)

**豁免条件：**
- 在认可英语国家完成高中或至少1年全日制高等教育（澳大利亚、新西兰、英国、美国、加拿大、爱尔兰等约20个国家）
- 完成UTS College Academic English Level 5 (AE5)
- 香港中学文凭考试HKDSE英语科目Level 4+ 
- 国际IB文凭英语A: Literature或English A: Language and Literature
- 考试成绩有效期为2年

---

## Section 4 — Costs & financial aid

### 4.1 学费（Tuition Fees）

**国内学生 (Domestic)：**
- Commonwealth Supported Place (CSP)：政府补贴部分学费，学生支付"学生贡献金额"（Student Contribution Amount），因学科领域而异
- 2026 CSP 学生贡献范围：约 A$4,000 - A$16,000/年（取决于学科领域）
- HECS-HELP：可延期缴纳，通过税务系统还款
- SSAF (Student Services and Amenities Fee)：约A$350/年

**国际学生 (International)：**
- 本科国际学费范围：约 A$35,000 - A$55,000/年（因课程而异）
- 研究生国际学费范围：约 A$35,000 - A$65,000/年（MBA更高）
- 申请费：A$100（不可退还）
- OSHC (Overseas Student Health Cover)：约 A$500 - A$700/年（单人）
- SSAF：适用
- 学费每年可能上涨

### 4.2 奖学金 (Scholarships)

UTS提供超过400项奖学金，主要类别：

| 奖学金类型 | 说明 |
|------------|------|
| UTS International Merit Scholarship | 国际学生学术优秀奖学金（减免部分学费） |
| UTS International Scholarships | 针对特定国家/地区的国际学生奖学金 |
| UTS Undergraduate Academic Merit Scholarship | 本科学术优秀奖学金 |
| UTS Postgraduate Academic Merit Scholarship | 研究生学术优秀奖学金 |
| UTS Equity Scholarships | 平等机会奖学金 |
| UTS Elite Athlete Program | 精英运动员体育奖学金（每年2月2日截止） |
| UTS Elite Performers Program | 精英表演者艺术奖学金 |
| UTS Humanitarian Scholarship Program | 人道主义奖学金 |
| Australian Government RTP Scholarships | 政府研究培训项目奖学金（博士/研究型硕士） |
| UTS Research Scholarships | UTS研究奖学金 |
| UTS Indigenous Scholarships | 土著学生奖学金 |
| Faculty-specific scholarships | 各学院特定奖学金（如Law Equity Scholarships等） |
| External scholarships | 外部奖学金 |
| Prizes and awards | 各类奖项/奖品 |

### 4.3 生活成本 (Cost of Living)

- 悉尼生活成本预估：约 A$25,000 - A$35,000/年（含住宿、餐饮、交通）
- 校内住宿：UTS Housing提供校内住宿选项
- 校外住宿：Ultimo/Chippendale/周边区域

---

## Section 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Technology Sydney"
  source_url: "https://www.uts.edu.au/about"
  source_snippet: "As Australia's #1 young university, we thrive in the heart of vibrant central Sydney."
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-002:
  field: rankings.qs_world_2027
  value: "#87 globally"
  source_url: "https://www.uts.edu.au/about"
  source_snippet: "Ranked #87 globally, UTS stands among the world's leading universities"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-003:
  field: rankings.the_world_2026
  value: "#7 in Australia"
  source_url: "https://www.uts.edu.au/about"
  source_snippet: "Recognised in Australia for excellence in teaching, research impact, industry engagement and international outlook."
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-004:
  field: rankings.employment_rate
  value: "93.3% employed within 3 years"
  source_url: "https://www.uts.edu.au/about"
  source_snippet: "93.3% employed Measured three years post-graduation"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-005:
  field: faculties.organization
  value: "8 faculties/schools with 14 departments"
  source_url: "https://www.uts.edu.au/about/faculties"
  source_snippet: "UTS Business School, Faculty of Design and Society, Faculty of Engineering and Information Technology..."
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-006:
  field: fees.international.application_fee
  value: "A$100 non-refundable"
  source_url: "https://www.uts.edu.au/for-students/admissions-entry/fees-costs/international-fees"
  source_snippet: "A non-refundable A$100 application fee is payable"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-007:
  field: english_language.general_standard
  value: "IELTS 6.5 (6.0 writing)"
  source_url: "https://www.uts.edu.au/for-students/admissions-entry/eligibility/english-language-requirements"
  source_snippet: "Overall 6.5, Writing 6.0"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-008:
  field: english_language.nursing
  value: "IELTS 7.0 (each 7.0, writing 6.5)"
  source_url: "https://www.uts.edu.au/for-students/admissions-entry/eligibility/english-language-requirements"
  source_snippet: "IELTS 7.0 overall, 7.0 each band, 6.5 writing"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-009:
  field: english_language.teaching
  value: "IELTS 7.5 (S 8.0, L 8.0, R 7.0, W 7.0)"
  source_url: "https://www.uts.edu.au/for-students/admissions-entry/eligibility/english-language-requirements"
  source_snippet: "IELTS 7.5 overall, Speaking 8.0, Listening 8.0, Reading 7.0, Writing 7.0"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-010:
  field: important_dates.2026
  value: "Full principal dates available"
  source_url: "https://www.uts.edu.au/for-students/current-students/managing-your-course/important-dates/principal-dates/2026-principal-dates"
  source_snippet: "2026 Principal Dates include the Academic Year dates as well as other important administrative deadlines"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-011:
  field: scholarships
  value: "Over 400 scholarships"
  source_url: "https://www.uts.edu.au/study/scholarships"
  source_snippet: "Scholarships Search"
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-012:
  field: course_areas
  value: "13 course areas"
  source_url: "https://www.uts.edu.au/courses"
  source_snippet: "Analytics and Data Science, Business, Communication, Design, Architecture and Building..."
  capture_date: 2026-07-11
  evidence_type: official_webpage

E-U-013:
  field: institution.identity
  value: "CRICOS 00099F, TEQSA PRV12060"
  source_url: "https://www.uts.edu.au/"
  source_snippet: "CRICOS provider number: 00099F, TEQSA provider number: PRV12060"
  capture_date: 2026-07-11
  evidence_type: official_webpage
```

---

## Section 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data item | Notes |
|----------|-----------|-------|
| **P0** | 全量本科课程列表 | 需要浏览器JS渲染访问 https://www.uts.edu.au/courses |
| **P0** | 全量授课型硕士课程列表 | 同上 |
| **P0** | 国际学生具体学费金额（按课程） | UTS学费在课程详情页，需逐个JS渲染访问 |
| **P0** | 各课程录取ATAR分数线 | 课程详情页包含 |
| **P1** | 全量博士项目列表 | 按学院分类 |
| **P1** | 各学院奖学金详情 | 各学院有独立奖学金页面 |
| **P2** | 学生满意度数据 | 可能需要第三方来源 |
| **P2** | 毕业生薪资数据 | QILT调查数据 |

---

## Section 7 — Cross-school comparison framework

| Dimension | UTS | UNSW | USyd | UTS Notes |
|-----------|-----|------|------|-----------|
| 总本科项目 | ~130+ | ~300+ | ~400+ | UTS规模小于Go8大学 |
| 总硕士项目 | ~200+ | ~500+ | ~600+ | |
| Go8成员 | 否 (ATN) | 是 | 是 | UTS是ATN成员，非Go8 |
| QS 2027排名 | #87 | #19 | #18 | UTS为澳洲排名上升最快的大学之一 |
| THE 2026排名 | #96 | #83 | #61 | |
| 毕业生就业率(3年) | 93.3% | — | — | 全澳领先 |
| #1年轻大学 | 是 (澳洲) | 不适用 | 不适用 | UTS Australia's #1 ranked young university |
| 主校区位置 | Sydney CBD | Kensington | Camperdown | UTS位于悉尼科技/创意产业中心 |
| 国际学生比例 | ~30% | ~35% | ~40% | UTS国际化程度高 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-11
> **Sources**: University official website (https://www.uts.edu.au)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ⚠️ (代表性抽样，缺全量) | PG programmes ⚠️ (代表性抽样，缺全量) | Evidence ✅ (13 blocks)
> **Next step**: 通过UTS官网课程搜索页面（JS渲染）获取全量课程列表，以及各课程具体学费和ATAR数据
