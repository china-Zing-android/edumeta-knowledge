> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console + Python extraction
> **Target knowledge base**: WeKnora
> **Granularity**: division → faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Ontario) — Toronto (3 campuses)

# University of Toronto 知识库 — 完整深度数据

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科项目 (UG programmes) | 700+ (含 Specialist, Major, Minor) |
| 研究生项目 (Graduate programmes) | 300+ |
| 其中专业硕士项目 (Professional Master's) | 70+ |
| 联合培养项目 (Combined Programs) | 140+ |
| 双学位项目 (Dual Degree Programs) | 14 |
| 合作项目 (Collaborative Programs) | 40+ |
| 文凭项目 (Diploma Programs) | 4 |
| 学院/学部 (Faculties/Schools/Divisions) | 19 |
| 学术院系 (Departments/Schools/Institutes) | 100+ |
| 图书馆 | 40 |
| 学生社团/组织 | 1,700+ |

### 0.2 院校层级结构

```
University of Toronto (U of T)
├── St. George Campus (Downtown Toronto)
│   ├── Faculty of Arts & Science
│   │   ├── College System (7 Colleges)
│   │   │   ├── Innis College
│   │   │   ├── New College
│   │   │   ├── St. Michael's College
│   │   │   ├── Trinity College
│   │   │   ├── University College
│   │   │   ├── Victoria College
│   │   │   └── Woodsworth College
│   │   └── (Multiple departments across Humanities, Sciences, Social Sciences)
│   ├── Faculty of Applied Science & Engineering
│   ├── Faculty of Architecture, Landscape & Design (Daniels)
│   ├── Faculty of Dentistry
│   ├── Ontario Institute for Studies in Education (OISE)
│   ├── Faculty of Information (iSchool)
│   ├── Faculty of Kinesiology & Physical Education
│   ├── Faculty of Law
│   ├── Rotman School of Management
│   ├── Temerty Faculty of Medicine
│   ├── Faculty of Music
│   ├── Lawrence Bloomberg Faculty of Nursing
│   ├── Leslie Dan Faculty of Pharmacy
│   ├── Dalla Lana School of Public Health
│   └── Factor-Inwentash Faculty of Social Work
├── University of Toronto Mississauga (UTM)
│   └── (Multiple departments and programs)
├── University of Toronto Scarborough (UTSC)
│   └── (Multiple departments and programs)
├── School of Continuing Studies
├── School of Graduate Studies (SGS)
└── Other Centres & Institutes
```

### 0.3 学历级别明细

| 学历级别 | 代码 | 说明 |
|---------|------|------|
| Honours Bachelor of Arts | H.B.A. | Arts & Science, UTM, UTSC |
| Honours Bachelor of Science | H.B.Sc. | Sciences, Life Sciences |
| Bachelor of Applied Science | B.A.Sc. | Engineering |
| Bachelor of Engineering | B.Eng. | Engineering |
| Bachelor of Commerce | B.Com. | Rotman Commerce, UTM, UTSC |
| Bachelor of Science in Nursing | B.Sc.N. | Nursing |
| Bachelor of Music | B.Mus. | Music |
| Bachelor of Architecture | B.Arch. | Architecture |
| Bachelor of Landscape Architecture | B.L.A. | Architecture |
| Bachelor of Kinesiology | B.Kin. | Kinesiology & PE |
| Bachelor of Physical & Health Education | B.P.H.E. | Kinesiology & PE |
| Doctor of Dental Surgery (Second Entry) | D.D.S. | Dentistry |
| Juris Doctor (Second Entry) | J.D. | Law |
| Medical Doctor (Second Entry) | M.D. | Medicine |
| Doctor of Pharmacy (Second Entry) | Pharm.D. | Pharmacy |
| Bachelor of Education (Second Entry) | B.Ed. | Education |
| Bachelor of Social Work (Second Entry) | B.S.W. | Social Work |
| Certificate (UG) | Cert. | Various |
| Master of Arts | M.A. | Graduate |
| Master of Science | M.Sc. | Graduate |
| Master of Engineering | M.Eng. | Graduate |
| Master of Business Administration | M.B.A. | Rotman |
| Master of Education | M.Ed. | OISE |
| Master of Laws | LL.M. | Law |
| Master of Music | M.Mus. | Music |
| Master of Information | M.I. | iSchool |
| Master of Public Health | M.P.H. | Public Health |
| Master of Social Work | M.S.W. | Social Work |
| Doctor of Philosophy | Ph.D. | Graduate |
| Doctor of Musical Arts | D.M.A. | Music |
| Graduate Certificate | Gr. Cert. | Graduate |
| Graduate Diploma | Gr. Dip. | Graduate |

### 0.4 分布矩阵

#### Undergraduate Programs × Campus/Faculty

| Faculty/Division | B.A./H.B.A. | H.B.Sc. | B.A.Sc./B.Eng. | B.Com. | B.Mus. | B.Kin. | B.Arch. | Other | 合计(约) |
|----------------|------|-------|--------|-------|-------|--------|--------|-------|---------|
| Arts & Science (St. George) | ✓ | ✓ | — | ✓ (Rotman) | — | — | — | — | ~378* |
| Applied Science & Engineering | — | — | ✓ | — | — | — | — | — | ~17 |
| Architecture, Landscape & Design | — | — | — | — | — | — | ✓ | — | ~3 |
| Kinesiology & Physical Education | — | ✓ | — | — | — | ✓ | — | — | ~4 |
| Music | — | — | — | — | ✓ | — | — | — | ~10+ |
| U of T Mississauga (UTM) | ✓ | ✓ | — | ✓ | — | — | — | — | ~100+ |
| U of T Scarborough (UTSC) | ✓ | ✓ | — | ✓ | — | — | — | — | ~80+ |

> *注：Arts & Science St. George 有约 378 个 Program 搜索结果。UTM 和 UTSC 另有约 150+ Program。另有 Second-entry 项目。总计 700+ 本科项目。

#### Graduate Programs × Faculty

| Faculty/Division | MA/MSc | PhD | Professional Master's | Certificate/Diploma |
|----------------|--------|-----|---------------------|-------------------|
| Applied Science & Engineering | ✓ | ✓ | M.Eng. | ✓ |
| Arts & Science (SGS) | ✓ | ✓ | ✓ | ✓ |
| Dentistry | ✓ | ✓ | ✓ | — |
| Education (OISE) | ✓ | ✓ | M.Ed. | ✓ |
| Information (iSchool) | ✓ | ✓ | M.I. | ✓ |
| Kinesiology & PE | ✓ | ✓ | — | ✓ |
| Law | ✓ (LL.M.) | S.J.D. | ✓ | ✓ |
| Management (Rotman) | ✓ | ✓ | MBA, MFin | ✓ |
| Medicine (Temerty) | ✓ | ✓ | MD Program | ✓ |
| Music | ✓ | D.M.A. | M.Mus. | ✓ |
| Nursing | ✓ (MN) | ✓ | — | ✓ |
| Pharmacy | ✓ | ✓ | Pharm.D. | ✓ |
| Public Health | ✓ (MPH) | ✓ | — | ✓ |
| Social Work | ✓ (MSW) | ✓ | — | ✓ |

---

## Section 1 — Undergraduate Education

### 1.1 本科项目类别分布

通过 U of T 本科项目搜索工具分类，St. George 校区约 378 个 Program（含 Specialist、Major、Minor）：

| 项目类别 | 示例项目 |
|---------|---------|
| 商科与管理 | Accounting (B.Com.), Management, Finance |
| 计算机与数据科学 | Computer Science, Data Science, Statistics |
| 工程与技术 | Engineering Science, TrackOne (Undecided Engineering) |
| 生命科学 | Biology, Biochemistry, Neuroscience, Pharmacology |
| 健康科学 | Kinesiology, Nursing, Public Health |
| 人文与社会科学 | English, History, Philosophy, Political Science, Economics |
| 数学与物理科学 | Mathematics, Physics, Chemistry, Astronomy |
| 艺术与音乐 | Music Performance, Composition, Visual Studies |
| 建筑与设计 | Architecture, Landscape Architecture, Visual Studies |
| 环境与可持续发展 | Environment, Geography, Earth Sciences |
| 语言与语言学 | French, Linguistics, East Asian Studies |

### 1.2 Faculty of Arts & Science (St. George Campus) — 本科项目

通过 7 学院制运营，所有 Arts & Science 的本科生归属于一个学院。申请时按**录取类别 (Admission Category)** 申请：

| 录取类别 | 说明 | 典型后续专业方向 |
|----------|------|-----------------|
| Humanities | 人文学科 | English, History, Philosophy, Languages, Religion |
| Social Sciences | 社会科学 | Economics, Political Science, Sociology, Psychology |
| Life Sciences | 生命科学 | Biology, Biochemistry, Neuroscience, Pharmacology |
| Physical & Mathematical Sciences | 物理与数学科学 | Physics, Chemistry, Mathematics, Statistics |
| Computer Science | 计算机科学 | Computer Science, Data Science |
| Rotman Commerce | 商科 | Accounting, Finance, Management |
| Humanities (UTM) | UTM 人文学科 | 多种 |
| Sciences (UTM) | UTM 科学 | 多种 |
| Social Sciences (UTM) | UTM 社会科学 | 多种 |
| Sciences (UTSC) | UTSC 科学 | 多种 |
| Social Sciences & Humanities (UTSC) | UTSC 社科/人文 | 多种 |

**Arts & Science 项目结构**：学生可选择 Specialist（专精）、Major（主修）、Minor（辅修）任意组合。

### 1.3 Faculty of Applied Science & Engineering

提供了 17+ 个核心工程项目：

| 项目 | 学制 | 说明 |
|------|------|------|
| Engineering Science | 4+年 | 含 Aerospace, Biomedical, 等 8 个方向 |
| TrackOne (Undecided Engineering) | 第1年通识 | 第2年选择专业方向 |
| Chemical Engineering | 4年 | — |
| Civil Engineering | 4年 | — |
| Computer Engineering | 4年 | — |
| Electrical Engineering | 4年 | — |
| Industrial Engineering | 4年 | — |
| Materials Engineering | 4年 | — |
| Mechanical Engineering | 4年 | — |
| Mineral Engineering | 4年 | — |

### 1.4 其他 First-Entry 本科项目

| 学院 | 学位 |
|------|------|
| Architecture, Landscape & Design | B.Arch., B.L.A. |
| Kinesiology & Physical Education | B.Kin., B.P.H.E. |
| Music | B.Mus. (Performance, Composition, Education) |
| U of T Mississauga (UTM) | H.B.A., H.B.Sc., B.Com. |
| U of T Scarborough (UTSC) | H.B.A., H.B.Sc., B.Com. |

### 1.5 Second-Entry 专业本科项目

| 学院 | 学位 | 学制 | 入学要求 |
|------|------|------|---------|
| Law (Faculty of Law) | J.D. | 3年 | 前本科 + LSAT |
| Medicine (Temerty) | M.D. | 4年 | 前本科 + MCAT |
| Dentistry | D.D.S. | 4年 | 前本科 + DAT |
| Pharmacy (Leslie Dan) | Pharm.D. | 4年 | 前本科 |
| Education (OISE) | B.Ed. | 2年 | 前本科 |
| Nursing (Bloomberg) | B.Sc.N. (Accelerated) | 2年 | 前本科 |

---

## Section 2 — Graduate Education

### 2.1 研究生项目概况

| 类别 | 数量 |
|------|------|
| 研究生项目总数 | 300+ |
| 专业硕士项目 (Professional Master's) | 70+ |
| 联合培养项目 (Combined Programs) | 140+ |
| 双学位项目 (Dual Degree) | 14 |
| 合作项目 (Collaborative Programs) | 40+ |
| 文凭项目 | 4 |

### 2.2 研究生项目列举 (按学院)

| 学院/学部 | 代表硕士项目 | 代表博士项目 |
|-----------|------------|-------------|
| Applied Science & Engineering | M.Eng., M.A.Sc. | Ph.D. |
| Arts & Science (through SGS) | M.A., M.Sc. | Ph.D. |
| OISE (Education) | M.Ed., M.A. | Ph.D., Ed.D. |
| Law | LL.M., GPLLM | S.J.D. |
| Rotman Management | MBA, MFin, MMI | Ph.D. |
| Temerty Medicine | MSc, MPH | Ph.D. |
| Information | MI (Master of Information) | Ph.D. |
| Music | M.Mus., M.A. | D.M.A., Ph.D. |
| Nursing | MN (Master of Nursing) | Ph.D. |
| Pharmacy | MSc | Ph.D. |
| Public Health | MPH | Ph.D. |
| Social Work | MSW | Ph.D. |
| Dentistry | MSc | Ph.D. |

---

## Section 3 — 招生要求 (Admissions)

### 3.1 本科申请流程

**两步申请流程：**
1. **Step 1**: 通过 Ontario Universities' Application Centre (OUAC) 提交申请
2. **Step 2**: 完成 U of T 申请门户的后续步骤（Join U of T portal 或 Engineering Applicant Portal）

**申请数量限制**: 最多可申请 3 个不同的项目领域（如不同学院或校区），但每个领域只能提交一份申请。

### 3.2 本科申请截止日期 (2026 Admission)

| 项目领域 | 申请截止日期 | 补充材料截止日期 | 补充申请截止日期 |
|---------|------------|-----------------|----------------|
| Applied Science & Engineering | 1月15日 | 1月15日 | Online Student Profile 1月15日 |
| Architecture, Landscape & Design | 1月15日 | 延至2月16日 | One Idea Supplementary Application 2月16日 |
| Arts & Science (St. George) - Rotman Commerce | 1月15日 | 2月2日 | Rotman Commerce Supplementary App 2月2日 |
| Arts & Science - All other programs | 1月15日 | 2月2日 (1月15日前申请)/2月16日 (1月16日-2月2日申请) | — |
| Kinesiology & Physical Education | 1月15日 | 2月2日 (普通)/4月30日 (内部) | Statement of Interest 2月16日 |
| Music | 1月15日 | 1月15日 | Music Questionnaire 1月15日(延至1月22日) |
| UTM - Computer Science | 1月15日 | 延至2月16日 | — |
| UTM - Theatre & Drama | 1月15日 | 2月2日 | — |
| UTM - All other programs | 1月15日 | 延至7月27日 | — |
| UT Scarborough | 1月15日 | 延至7月27日 | — |

> **重要日期**: 
> - 早申请建议截止: 11月7日
> - 早申请文件建议提交: 12月2日
> - 常规申请截止: 1月15日
> - 录取结果发放: 1月至5月下旬
> - 住宿保证申请截止: 3月31日

### 3.3 加拿大高中生入学要求

- 完成 Ontario Secondary School Diploma (OSSD)
- 6 门 4U/M 课程
- 含 ENG4U/EAE4U 英语课程
- 具体专业有先修课程要求（如 Engineering 需 MCV4U Calculus 等）

其他省份学生参考相应的等效学术要求。

### 3.4 国际学生入学要求

各国家/地区的具体学历要求不同。基本要求：
- 完成本国高中教育或等效学历
- 满足特定专业的先修课程要求
- 提供英语能力证明（如适用）

### 3.5 英语语言要求

**豁免条件**（满足其一）：
- 在以英语教学的加拿大认可学校完成 4 年或以上全日制学习
- 在以英语为官方语言的国家完成 4 年或以上全日制英语学校学习
- 第一语言为法语且在加拿大学校完成 4 年或以上全日制学习

**接受的语言考试及最低分数要求**：

| 考试类型 | 最低要求 |
|---------|---------|
| **IELTS Academic** (含 IELTS Online) | 总分 6.5，单项不低于 6.0 |
| **TOEFL iBT** (含 Home Edition) | 2026年1月21日前考试: 总分 89，口语和写作不低于 22。2026年1月21日及之后考试: 总分 4.5，写作 4.5，口语 4.0 |
| **Duolingo English Test** | 2024年7月1日后: 总分 120，Production 120。2024年7月1日前: 总分 120，单项不低于 100 |
| **Cambridge English C1 Advanced/C2 Proficiency** | 总分 180，各单项不低于 170 |
| **CAEL (含 CAEL Online)** | 总分 70，各单项不低于 60 |
| **PTE Academic** (含 UKVI) | 总分 65，各单项不低于 60 |
| **ELDA/COPE** | 总分 86，写作 32，阅读和听力各 22 |
| **GCSE/IGCSE/GCE/AICE English** | GCSE/IGCSE: B级(6分)，GCE A Level/AS Level: C级 |
| **IB English** | SL/HL English A: Literature 或 Language and Literature 至少 4分；IB English B HL 7分 |
| **Caribbean Examinations Council (CSEC) English** | 最终成绩 A(I) 或 B(II) |
| **U of T Continuing Studies Academic English** | 60/Advanced 级别达到 B 级 |
| **University Studies** | 在以英语为官方语言国家的认可大学完成1年全日制学习 |

> **注意**: 
> - 不接受 IELTS Indicator、TOEFL Essentials、TOEFL ITP
> - 不接受拼分
> - 学校代码 TOEFL: 0982-00
> - IELTS 寄送到 "University of Toronto - Undergraduate and Graduate Programs"

### 3.6 补充申请 (Supplemental Applications)

需要补充申请的项目领域：
| 项目领域 | 补充申请类型 |
|---------|------------|
| Applied Science & Engineering | Online Student Profile |
| Architecture, Landscape & Design | One Idea Supplementary Application |
| Arts & Science - Rotman Commerce | Rotman Commerce Supplementary Application |
| Arts & Science - Computer Science | Computer Science Supplementary Application |
| Kinesiology & Physical Education | Statement of Interest |
| Music | Music Questionnaire, Audition/Interview |

---

## Section 4 — 学费与费用 (2025-26 参考)

### 4.1 本科学费 (First-Entry Programs)

| 学生类别 | 学费范围 (年) | 说明 |
|---------|-------------|------|
| 加拿大国内学生 | ~$6,100 - $16,090 | 按项目不同 |
| 国际学生 | ~$48,090 - $70,060 | 按项目不同 |

> *不含必修的非学术性杂费*

### 4.2 研究生学费

| 学生类别 | 学费范围 (年) | 说明 |
|---------|-------------|------|
| 国内博士 (Doctoral Stream) | 有最低资助保障 | 学校承诺前5年资助 |
| 国内硕士/专业硕士 | ~$5,940 - $46,270 | 按项目不同 |
| 国际博士 | ~$6,210 - $70,730 | 大部分国际博士生与国内生同价 |
| 国际硕士/专业硕士 | ~$6,210 - $70,730 | 按项目不同 |

### 4.3 其他费用

| 费用项目 | 说明 |
|---------|------|
| 住宿 (St. George) | 14 座宿舍楼，分属各学院 |
| 住宿 (UTM) | 可容纳 1,500+ 学生 |
| 住宿 (UTSC) | 可容纳 1,500+ 学生 |
| 住宿保证 | 首年全日制新生在3月31日前申请并6月2日前接受录取即保证住宿 |
| 学生健康保险 (UHIP) | 国际学生必修 |

### 4.4 学费分类

U of T 的学费分为：
- **Program-Based Fees**: 按学期固定收费（大部分全日制项目）
- **Course-Based Fees**: 按课程学分收费（部分项目）
- **Deregulated Program Fees**: 部分高成本专业可收取更高学费（如 Engineering, Computer Science, Rotman Commerce 等）

---

## Section 5 — 学生数据 (Fall 2024-25)

### 5.1 在学人数总览

| 校区 | 本科 | 研究生 | 合计 |
|------|------|--------|------|
| St. George | 49,425 | 20,551 | 69,976 |
| Mississauga (UTM) | 16,379 | 902 | 17,281 |
| Scarborough (UTSC) | 14,769 | 405 | 15,174 |
| **合计** | **80,573** | **21,858** | **102,431** |

### 5.2 国内 vs 国际学生

| 类别 | 数量 | 比例 |
|------|------|------|
| 国内学生 | 72,982 | ~71.3% |
| 国际学生 | 29,449 | ~28.7% |

### 5.3 国际学生来源 Top 5

| 国家/地区 | 学生人数 |
|-----------|---------|
| 中国 | 15,846 |
| 印度 | 2,527 |
| 美国 | 1,315 |
| 韩国 | 957 |
| 香港 | [详细数据] |

> 国际学生来自 175 个国家/地区

### 5.4 新生入学 (Fall 2024)

| 校区 | 新增全日制本科生 |
|------|----------------|
| St. George | 9,890 |
| Mississauga (UTM) | 4,047 |
| Scarborough (UTSC) | 3,821 |
| **合计** | **17,758** |

---

## Section 6 — 院校关键数据

### 6.1 排名与声誉

| 指标 | 排名 |
|------|------|
| U.S. News & World Report 2026 | 加拿大第1，全球第20 |
| QS World University Rankings 2026 | 加拿大第1，全球第25，所有学科领域全球前17 |
| Times Higher Education 2025 | 加拿大第1，所有学科全球前30 |
| THE Global Employability Ranking 2025 | 加拿大第1，全球前10 |
| NTU Ranking (Scientific Papers) 2025 | 加拿大第1 |
| QS Sustainability Ranking 2026 | 全球第2 |
| Nobel Laureates | 12位 |
| Canada Research Chairs | 323位 |
| 研究引用 | 加拿大第1 (Clarivate, Incites) |
| 医疗研究 | 全球前10 (U of T + Toronto hospitals) |
| QS 学科排名 2026 | 48个学科类别全球前50（全球最多） |
| 创业 | 加拿大第1，全球大学孵化器前5 |
| 初创公司 | 1,500+ 风投支持企业 |

### 6.2 校园与设施

| 指标 | 数据 |
|------|------|
| 校区数量 | 3 (St. George, Mississauga, Scarborough) |
| 图书馆数量 | 40 座 |
| 馆藏数量 | 1,200 万册（341种语言），近 400 万电子资源 |
| 图书馆系统规模 | 加拿大最大，北美第2 |
| 数字存储 | 1.5 PB |
| 学生社团 | 1,700+ |

### 6.3 运营预算与科研

| 指标 | 数据 |
|------|------|
| 运营预算 (2025-26) | $36.2 亿加元 |
| 研究引用 (学术产出一级) | 加拿大第1 |
| 创业投资 | 过去5年筹集 $140 亿+ |
| 创业就业创造 | 20,000+ 岗位 |
| 专利应用 (10年) | 1,000+ |
| 含学生/博后发明 | 80% |

---

## Section 7 — 联系信息与重要链接

### 7.1 联系方式

| 部门 | 信息 |
|------|------|
| 主校地址 | 27 King's College Circle, Toronto, Ontario, Canada M5S 1A1 |
| 大学官网 | https://www.utoronto.ca/ |
| 未来学生网站 | https://future.utoronto.ca/ |
| 申请人门户 | https://join.utoronto.ca/ (Join U of T portal) |
| 工程申请人门户 | Engineering Applicant Portal |
| OUAC | https://www.ouac.on.ca/ |
| ACORN (学生信息系统) | https://acorn.utoronto.ca/ |

### 7.2 重要页面链接

| 页面 | URL |
|------|-----|
| 本科项目 | https://www.utoronto.ca/academics/undergraduate-programs |
| 研究生项目 | https://www.utoronto.ca/academics/graduate-programs |
| 招生要求 | https://future.utoronto.ca/requirements |
| 英语语言要求 | https://future.utoronto.ca/english-language-requirements |
| 申请流程 | https://future.utoronto.ca/how-to-apply |
| 截止日期 | https://future.utoronto.ca/deadlines |
| 学费信息 | https://www.registrar.utoronto.ca/fees-payments/tuition-fee-schedules/ |
| 学费 Explorer | https://www.registrar.utoronto.ca/fees-payments/tuition-fee-schedules/#tuition-explorer |
| 奖学金 | https://future.utoronto.ca/scholarships/ |
| 学术单位 | https://www.utoronto.ca/academics/academic-units |
| 快速事实 | https://www.utoronto.ca/about-u-of-t/quick-facts |

---

## Appendix A — 学科方向分类（完整列举）

### A.1 本科方向（按字母序，来源：utoronto.ca 项目搜索工具，378个 Program in Arts & Science St. George + UTM + UTSC）

**注意：此处仅按字母序列出 Program 名称。完整课程描述请参见 U of T 官方网站。**

- Accounting (B.Com.) — St. George, UTM
- Actuarial Science — St. George
- African Studies — St. George, UTSC
- Aging and Society — UTSC
- American Studies — St. George
- Animal Physiology — St. George
- Anthropology (Arts) — UTM, UTSC
- Anthropology (Science) — UTM
- Anthropology: Evolutionary — St. George
- Archaeology — St. George, UTM
- Architectural Studies — St. George (Daniels)
- Art and Art History — UTM
- Art History — St. George
- Astronomy and Astrophysics — St. George
- Biochemistry — St. George, UTM
- Bioengineering — St. George (Engineering Science)
- Biology — St. George, UTM
- Biology (Co-op) — UTSC
- Biology for Health Sciences — UTM
- Biomedical Engineering — St. George (Engineering Science)
- Biomedical Sciences — UTSC
- Biophysics — St. George
- Biotechnology — UTM
- Book and Media Studies — St. Michael's College
- Buddhism, Psychology and Mental Health — St. George (New College)
- Buddhist Studies — St. George
- Business Administration — UTSC
- Canadian Studies — St. George, University College
- Caribbean Studies — St. George
- Cell and Molecular Biology — St. George, UTSC
- Chemical Engineering — St. George
- Chemical Physics — St. George
- Chemistry — St. George, UTM, UTSC
- Chemistry (Biological) — St. George
- Chemistry (Environmental) — St. George
- Chemistry (Materials) — St. George
- Cinema Studies — St. George (Innis College)
- Cities, Regions, Planning — St. George
- Civil Engineering — St. George
- Classical Civilization — St. George
- Classics — St. George
- Cognitive Science — St. George (University College), UTSC
- Communication, Culture, Information and Technology — UTM
- Communications — UTSC
- Community and Public Affairs — UTSC
- Comparative Literature — St. George
- Computer Engineering — St. George
- Computer Science — St. George, UTM, UTSC
- Computer Security — UTSC
- Conservation and Biodiversity — UTSC
- Contemporary Asian Studies — St. George
- Criminology and Sociolegal Studies — St. George
- Criminology and Sociolegal Studies — UTM
- Critical Development Studies — UTSC
- Culture, Creativity and Cities — UTM
- Diaspora and Transnational Studies — St. George
- Digital Enterprise Management — UTM
- Drama and Theatre Studies — St. George
- Earth Sciences — St. George
- East Asian Studies — St. George, UTM
- Ecology and Evolutionary Biology — St. George, UTSC
- Econometrics and Quantitative Economics — UTSC
- Economics — St. George, UTM, UTSC
- Education and Society — St. George
- Electrical Engineering — St. George
- Engineering Science — St. George
- English — St. George, UTM, UTSC
- Environment and Health — UTSC
- Environment and Society — UTSC
- Environmental Biology — UTM
- Environmental Chemistry — UTSC
- Environmental Ethics — UTM
- Environmental Geoscience — St. George
- Environmental Science — St. George, UTSC
- Environmental Studies — St. George
- Equity, Diversity, and Justice — UTSC
- Ethics, Society and Law — St. George (Trinity College)
- European Studies — St. George
- Evolutionary Anthropology — St. George
- Finance — UTM
- Financial Economics — UTM
- Financial Mathematics — UTSC
- Fine Art (History, Studio) — St. George
- Forensic Science — UTM
- Forest Conservation — St. George (Innis College)
- French — St. George, UTM, UTSC
- French and Linguistics — St. George
- Geography — St. George, UTM, UTSC
- Geoscience — UTM
- German — St. George
- Global and Area Studies — UTSC
- Global Asia Studies — UTSC
- Global Development Studies — St. George
- Global Health — St. George (New College)
- Global Migration — UTSC
- Health and Disease — St. George (New College)
- Health Studies — UTSC
- History — St. George, UTM, UTSC
- History of Art — UTM
- History and Philosophy of Science and Technology — St. George
- History of Religion — St. George
- Human Biology — St. George
- Human Geography — St. George, UTM, UTSC
- Humanities — UTM
- Immunology — St. George
- Indigenous Studies — St. George, UTSC
- Industrial Engineering — St. George
- Industrial Relations and Human Resources — St. George
- Information Ethics & Policy — St. George (iSchool)
- Information Security — UTM
- International Affairs — UTSC
- International Development Studies — UTM
- International Relations — St. George (Trinity College)
- Italian — St. George
- Jewish Studies — St. George
- Journalism — UTSC
- Justice and Leadership — UTM
- Kinesiology — St. George
- Laboratory Medicine and Pathobiology — St. George
- Languages and Linguistics — UTSC
- Latin American Studies — St. George
- Law and Business — UTM
- Law, Crime and Social Change — UTM
- Linguistics — St. George, UTM
- Literature and Critical Theory — UTM
- Management — UTSC
- Management and International Business — UTSC
- Materials Engineering — St. George
- Materials Science — St. George
- Mathematics — St. George, UTM, UTSC
- Mathematics and Its Applications (Specialist) — St. George
- Mechanical Engineering — St. George
- Media, Journalism and Digital Cultures — UTM
- Medieval Studies — St. George
- Mineral Engineering — St. George
- Molecular Genetics and Microbiology — St. George
- Music — St. George, UTM, UTSC
- Music and Culture — UTSC
- Music Education — St. George
- Neuroscience — St. George, UTSC
- New Media Studies — UTSC
- Nursing (B.Sc.N.) — St. George (Bloomberg)
- Nutritional Sciences — St. George
- Pathobiology — St. George (New College)
- Pharmacology — St. George
- Pharmacy (Pharm.D.) — St. George (Leslie Dan)
- Philosophy — St. George, UTM, UTSC
- Physical and Environmental Geography — St. George
- Physical Education and Health — St. George
- Physics — St. George, UTM
- Physiology — St. George
- Plant Biology — St. George, UTSC
- Political Science — St. George, UTM, UTSC
- Portuguese — St. George
- Professional Writing and Communication — UTM
- Psychology — St. George, UTM, UTSC
- Public Health — UTSC
- Public Policy — St. George
- Religion — St. George (Trinity College), UTM
- Renaissance Studies — St. George (Victoria College)
- Science and Technology Studies — St. George
- Sexual Diversity Studies — St. George
- Social and Political Philosophy — UTM
- Social Sciences — UTM
- Sociology — St. George
- Software Engineering — St. George (Engineering)
- South Asian Studies — St. George
- Spanish — St. George
- Spanish and Latin American Studies — UTM
- Spanish Languages and Linguistics — UTM
- Statistics — St. George, UTSC
- Statistics and Machine Learning — UTSC
- Statistical Science — UTM (co-op)
- Sustainability — St. George, UTSC
- Teaching English to Speakers of Other Languages (TESOL) — UTM
- Theatre and Drama Studies — UTM
- Theatre and Performance — UTSC
- Urban Studies — St. George (Innis College), UTSC
- Visual and Performing Arts, Education — UTM
- Visual Arts — UTSC
- Visual Culture and Communication — UTM
- Visual Studies — St. George (Daniels)
- Women and Gender Studies — St. George, UTM, UTSC
- World Literatures — UTSC
- Writing and Rhetoric — UTM
- Youth and Children's Studies — UTSC

---

## Appendix B — 本科录取类别 (Admission Categories)

| 录取类别 | 所属学部 | 说明 |
|---------|---------|------|
| Humanities | Arts & Science (St. George) | 人文学科 |
| Social Sciences | Arts & Science (St. George) | 社会科学 |
| Life Sciences | Arts & Science (St. George) | 生命科学 |
| Physical & Mathematical Sciences | Arts & Science (St. George) | 物理数学 |
| Computer Science | Arts & Science (St. George) | 计算机科学 |
| Rotman Commerce | Arts & Science (St. George) | 商科 |
| Engineering | Applied Science & Engineering | 工程 |
| Architectural Studies | Architecture, Landscape & Design | 建筑 |
| Kinesiology | Kinesiology & PE | 运动机能学 |
| Music | Music | 音乐 |
| Humanities/Social Sciences/Sciences | UTM | UTM 分类 |
| Social Sciences & Humanities/Sciences | UTSC | UTSC 分类 |
| Management & International Business | UTSC | UTSC 管理 |
| Paramedicine | UTSC | UTSC 急救医学 |

---

> **Document prepared**: 2026-07-10
> **Data sources**: utoronto.ca, future.utoronto.ca, registrar.utoronto.ca, OUAC
> **Methodology**: browser_navigate + browser_snapshot + browser_console JavaScript extraction
> **Disclaimer**: Program counts are approximate and may vary year-to-year. Tuition figures are based on 2025-26 published data for reference only. Always confirm with official U of T sources.
