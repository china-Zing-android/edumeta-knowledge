# University of Northern British Columbia (UNBC) — 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console + sitemap.xml
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (British Columbia)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~50+ (9个学位类别下分布) |
| 研究生授课型/研究型项目 (PGT: MA/MSc/MBA/MEd/MEng/MSW等) | ~25+ |
| 研究生博士项目 (PhD/Doctoral) | ~4 (PhD NRES, PhD Health Sciences, PhD Psychology, EdD) |
| 学位项目总计 | ~80+ |
| 学院/学部 (Faculties) | 5 + 1个Division of Medical Sciences |
| 学术院系 (Academic Schools/Departments) | ~20+ |
| 校区 | 4 (Prince George 主校区, Fort St. John, Quesnel, Terrace) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Northern British Columbia (est. 1990)
├── Prince George Campus (主校区)
│   ├── Faculty of Human and Health Sciences
│   │   ├── School of Health Sciences
│   │   ├── School of Nursing
│   │   ├── School of Social Work
│   │   └── School of Kinesiology
│   ├── Faculty of Indigenous Studies, Social Sciences and Humanities (FISSSH)
│   │   ├── Anthropology
│   │   ├── Economics
│   │   ├── English
│   │   ├── First Nations Studies
│   │   ├── Gender Studies
│   │   ├── Geography
│   │   ├── Global and International Studies
│   │   ├── History
│   │   ├── Political Science
│   │   ├── Psychology
│   │   ├── Sociology / Social Work
│   │   └── Environmental and Sustainability Studies
│   ├── Faculty of Science and Engineering
│   │   ├── School of Engineering (Civil, Environmental, Structural, Building Sciences)
│   │   ├── Biochemistry and Molecular Biology
│   │   ├── Chemistry
│   │   ├── Computer Science
│   │   ├── Mathematics and Statistics
│   │   └── Physics
│   ├── Faculty of Environment
│   │   ├── Natural Resources and Environmental Studies (NRES)
│   │   ├── Geography
│   │   ├── Environmental Science
│   │   ├── Biology
│   │   ├── Forestry
│   │   └── Outdoor Recreation, Conservation and Tourism
│   ├── Faculty of Business and Economics
│   │   ├── MBA Program
│   │   ├── BComm Programs (Accounting, Finance, General Business, HR, International Business, MIS, Marketing)
│   │   └── MSc Business Administration
│   └── Division of Medical Sciences
│       └── Biomedical Studies (BHSc)
├── Regional Campuses
│   ├── Fort St. John Campus
│   │   └── BScN Nursing, BSW Social Work
│   ├── Quesnel Campus
│   │   └── BEd Elementary, BScN Nursing, BSW Social Work
│   └── Terrace Campus
│       └── BEd Elementary, BScN Nursing, BSW Social Work, Integrated Science (BSc)
└── Office of Graduate Administration (全校研究生管理)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位级别 | 缩写 | 说明 |
|---------|------|------|
| 应用科学学士 | BASc | Bachelor of Applied Science |
| 文学士 | BA | Bachelor of Arts |
| 商学士 | BComm | Bachelor of Commerce |
| 教育学士 | BEd | Bachelor of Education |
| 健康科学学士 | BHSc | Bachelor of Health Sciences |
| 规划学士 | BPl | Bachelor of Planning |
| 理学士 | BSc | Bachelor of Science |
| 护理学学士 | BScN | Bachelor of Science in Nursing |
| 社会工作学士 | BSW | Bachelor of Social Work |
| 文学硕士 | MA | Master of Arts |
| 理学硕士 | MSc | Master of Science |
| 应用科学硕士 | MASc | Master of Applied Science |
| 工程硕士 | MEng | Master of Engineering |
| 工商管理硕士 | MBA | Master of Business Administration |
| 教育硕士 | MEd | Master of Education |
| 社会工作硕士 | MSW | Master of Social Work |
| 护理硕士 | MScN | Master of Science in Nursing |
| 自然资源与环境研究硕士 | MNRES | Master of Natural Resources and Environmental Studies |
| 博士 | PhD | Doctor of Philosophy |
| 研究生证书 | Grad Cert | Graduate Certificate |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院/学部 | UG | PGT/Research Master | PhD | 合计 |
|-----------|:--:|:---:|:---:|:----:|
| Faculty of Indigenous Studies, Social Sciences and Humanities | ~14 | ~9 | — | ~23 |
| Faculty of Science and Engineering | ~7 | ~6 | — | ~13 |
| Faculty of Environment (NRES) | ~5 | ~4 | ~1 | ~10 |
| Faculty of Business and Economics | ~7 | ~3 | — | ~10 |
| Faculty of Human and Health Sciences | ~5 | ~5 | ~1 | ~11 |
| Division of Medical Sciences | ~1 | — | — | ~1 |
| 跨学科/其他 | — | ~4 | ~2 | ~6 |
| **总计** | **~39** | **~31** | **~4** | **~74+** |

> **注**: 节目数量为基于学校课程搜索和研究生项目页面的分类整理。准确的全量清单需通过课程目录或 API 获取。

---

## Section 1 — Undergraduate education

### Faculty of Indigenous Studies, Social Sciences and Humanities (FISSSH)

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Anthropology | BA | Prince George |
| Economics | BA | Prince George |
| English | BA | Prince George |
| Environmental and Sustainability Studies | BA | Prince George |
| First Nations Studies | BA | Prince George |
| General Studies | BA | Prince George |
| Geography | BA | Prince George |
| Global and International Studies | BA | Prince George |
| History | BA | Prince George |
| Nature-Based Tourism Management | BA | Prince George |
| Northern Studies | BA | Prince George |
| Political Science | BA | Prince George |
| Public Administration and Community Development | BA | Prince George |
| Women's Studies | BA | Prince George |

### Faculty of Business and Economics

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Accounting | BComm | Prince George |
| Finance | BComm | Prince George |
| General Business | BComm | Prince George |
| Human Resources Management | BComm | Prince George |
| International Business | BComm | Prince George |
| Management Information Systems | BComm | Prince George |
| Marketing | BComm | Prince George |

### Faculty of Science and Engineering

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Civil Engineering | BASc | Prince George |
| Environmental Engineering | BASc | Prince George |
| Environmental Engineering (Joint UNBC and UBC) | BASc | Prince George |
| Biochemistry and Molecular Biology | BSc | Prince George |
| Biology | BSc | Prince George |
| Chemistry | BSc | Prince George |
| Computer Science | BSc | Prince George |
| Conservation Science and Practice | BSc | Prince George |
| Environmental Science | BSc | Prince George |
| Forest Ecology and Management | BSc | Prince George |
| Geography | BSc | Prince George |
| Integrated Science | BSc | Prince George, Terrace |
| Landscape Conservation and Management | BSc | Prince George |
| Mathematics and Statistics | BSc | Prince George |
| Physics | BSc | Prince George |
| Psychology | BSc | Prince George |
| Wildland Conservation and Recreation | BSc | Prince George |
| Wildlife and Fisheries | BSc | Prince George |

### Faculty of Environment

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Natural Resources Planning | BPl | Prince George |
| First Nations Planning | BPl | Prince George |
| Northern and Rural Community Planning | BPl | Prince George |
| *(NRES programs at graduate level)* | | |

### Faculty of Human and Health Sciences

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Biomedical Studies | BHSc | Prince George |
| Community and Population Health: Aboriginal and Rural Health | BHSc | Prince George |
| Community and Population Health: Environmental Health | BHSc | Prince George |
| Northern Baccalaureate Nursing | BScN | Fort St. John, Prince George |
| Northern Collaborative Baccalaureate Nursing | BScN | Prince George, Quesnel, Terrace |
| Social Work | BSW | Fort St. John, Prince George, Quesnel, Terrace |

### Faculty of Education

| 项目名称 | 学位类型 | 校区 |
|---------|---------|------|
| Education - Elementary (K-7) | BEd | Prince George, Quesnel, Terrace |
| Education - Secondary (8-12) | BEd | Prince George |

---

## Section 2 — Graduate education

### 2.1 PGT & Research — 授课型/研究型研究生项目

| 项目名称 | 学位类型 | 学院/系 | 备注 |
|---------|---------|---------|------|
| MA Development Economics | MA | FISSSH/Business | 无需预先联系导师 |
| MA Disability Management | MA | Health Sciences | 仅兼职/远程在线授课 |
| MA English | MA | FISSSH | 需预先联系导师；3种完成路线 |
| MA First Nations Studies | MA | FISSSH | ⚠️ 当前暂停招生 |
| MA Gender Studies | MA | FISSSH | 需预先联系导师 |
| MA History | MA | FISSSH | 仅秋季入学 |
| MA International Studies | MA | FISSSH | 有限名额 |
| MA Political Science | MA | FISSSH | GPA最低3.33(B+); 英语要求较高 |
| MA Natural Resources and Environmental Studies | MA | Environment | 需预先联系导师 |
| MSc Natural Resources and Environmental Studies | MSc | Environment | 需预先联系导师 |
| MNRES (Master of Natural Resources and Environmental Studies) | MNRES | Environment | 交叉学科 |
| MASc Engineering | MASc | Engineering | 需预先联系导师; 需面试 |
| MEng - Master of Engineering | MEng | Engineering | 课程型; 无需导师 |
| MEng - Wood Engineering | MEng | Engineering | 更高的英语要求(IELTS 7.0) |
| MBA - Master of Business Administration | MBA | Business | 需3年管理工作经验; Vancouver/Prince George |
| Graduate Certificate in Change Leadership | Grad Cert | Business | 仅限国内生; 限8人 |
| MSc Business Administration | MSc | Business | 研究型; 需预先联系导师 |
| MEd Counselling | MEd | Education | 高度竞争; 需相关经验 |
| Master of Education (MEd) | MEd | Education | 2个方向; Inclusive Education/Educational Leadership |
| MSc Health Sciences | MSc | Health Sciences | 需预先联系导师; 需统计学/研究方法论前置 |
| MSc Psychology | MSc | FISSSH | 研究型; GPA最低3.33; 非临床方向 |
| MScN Nurse Practitioner | MScN | Nursing | 需2年RN工作经验 |
| MScN Thesis or Project | MScN | Nursing | 研究型 |
| MSW - Master of Social Work | MSW | Social Work | 需60学分前置 |
| Indigenous Child and Youth Mental Health Grad Cert | Grad Cert | Social Work | 仅在线授课 |
| Interdisciplinary Studies (MA/MSc) | MA/MSc | 跨学科 | 学生自设计课程 |
| MSc Biochemistry | MSc | Science & Engineering | 需预先联系导师 |
| MSc Chemistry | MSc | Science & Engineering | 需预先联系导师 |
| MSc Computer Science | MSc | Science & Engineering | 高度竞争 |
| MSc Mathematics | MSc | Science & Engineering | — |
| MSc Physics | MSc | Science & Engineering | 需预先联系导师 |

### 2.2 PhD — 博士研究项目

| 项目名称 | 学位类型 | 学院/系 | 备注 |
|---------|---------|---------|------|
| PhD Natural Resources and Environmental Studies | PhD | Environment | GPA最低3.33(研究生课程) |
| PhD Health Sciences | PhD | Health Sciences | GPA最低3.67 |
| PhD Psychology | PhD | FISSSH | ⚠️ 当前不接受申请 |

### 2.3 研究生申请费

| 申请人类别 | 费用 (CAD) |
|-----------|-----------|
| 加拿大国内申请人 | $76.50 (non-refundable) |
| 国际申请人 | $153.00 (non-refundable) |

---

## Section 3 — Application requirements & deadlines

### 3.1 General Admission Requirements

**Undergraduate:**
- 完成高中毕业（Grade 12）
- 满足所选学科方向的课程先修要求
- 特定竞争性项目(Engineering, Health Sciences, Nursing, Education, Social Work)有额外要求

**Graduate (General Requirements):**
- 四年制学士学位（或同等学历）
- 大多数项目需要联系并确认潜在指导教授
- 学术兴趣陈述(Statement of Interest)
- 2-3封推荐信
- GPA要求因项目而异

### 3.2 Application Deadlines (Undergraduate)

#### 通用入学项目

**Bachelor of Arts (BA) / Bachelor of Commerce (BComm) / Bachelor of Planning (BPl) / Bachelor of Science (BSc)**

| 学期 | 国内生 | 国际生 |
|-----|-------|-------|
| 九月(秋季) | 3月1日 | 3月1日 |
| 九月(延期申请) | 持续接收 | 7月11日 |
| 一月(冬季) | 11月1日 | 6月1日 |
| 一月(延期申请) | 持续接收 | 11月8日 |

#### 竞争性入学项目

**Bachelor of Applied Science (Engineering) (BASc)**

| 学期 | 国内生 | 国际生 |
|-----|-------|-------|
| 九月 | 3月1日 | 3月1日 |
| 延期申请* | 8月1日 | 7月11日 |
| 一月 | 无招生 | 无招生 |

**Bachelor of Health Sciences (BHSc)**

| 学期 | 国内生 | 国际生 |
|-----|-------|-------|
| 九月 | 5月15日 | 5月15日 |
| 一月 | 无招生 | 无招生 |

**Bachelor of Science in Nursing (BScN) — Northern Collaborative**

| 学期 | 国内生 | 国际生 |
|-----|-------|-------|
| 九月 | 3月31日 | 无招生 |
| 一月 | 无招生 | 无招生 |

**Bachelor of Education (BEd)**

| 学期 | 国内生 | 国际生 |
|-----|-------|-------|
| 九月 | 2月15日 | 2月15日 |
| 延期申请* | 3月1日 | 3月1日 |
| 一月 | 无招生 | 无招生 |

**Bachelor of Science in Nursing (BScN) — Northern Baccalaureate (Fort St. John / Prince George)**

| 学期 | 国内生 | 国际生 | LPN Pathway |
|-----|-------|-------|-----------|
| 九月 | 1月15日 | 无招生 | 3月9日 |
| 延期申请* | 2月6日 | 无招生 | — |
| 一月 | 无招生 | 无招生 | 无招生 |

**Bachelor of Social Work (BSW)**

| 学期 | 校区 | 国内生 | 国际生 |
|-----|------|-------|-------|
| 九月 | Fort St. John/Quesnel/Terrace | 2月1日 | 2月1日 |
| 延期申请* | 同上 | 6月15日 | 6月15日 |
| 九月 | Prince George | 2月1日 | 2月1日 |
| 延期申请 | Prince George | 5月15日 | 5月15日 |
| 一月 | 所有校区 | 无招生 | 无招生 |

**奖学金截止日期：**
- **1月15日**: 早入学奖学金申请截止
- **4月1日**: 一般奖学金、助学金和奖项申请截止

### 3.3 English Language Requirements (英语语言要求)

#### 研究生标准要求

| 考试类型 | 最低分数 |
|---------|---------|
| TOEFL iBT | 90 (各单项不低于20); 学校代码0320 |
| IELTS Academic | 6.5 (各单项不低于6.0); 不接受IELTS Indicator |
| CAEL / CAEL CE | 70 (各单项不低于60) |
| PTE Academic | 65 (各单项不低于60) |
| Duolingo English Test | 125 (各单项不低于115) |
| MELAB | 85 (口语测试3分) |
| CELPIP | CELPIT-A 4H / CELL 4H / CELTOP 4H (CELPIP General 不被接受) |
| BCCAT EAP 4 | 最终成绩B或以上 |

#### 研究生更高要求 (MEng Wood Engineering / MA Political Science)

| 考试类型 | 最低分数 |
|---------|---------|
| IELTS Academic | 7.0 (各单项不低于6.5) |
| TOEFL iBT | 100 (各单项不低于25) |
| Duolingo | 135 (各单项不低于125) |

#### 示例豁免条件
1. 在加拿大或其他英语国家完成一定年限的高中/本科教育
2. 特定国际课程成绩达标

### 3.4 Graduate Deadlines

研究生截止日期因项目而异。部分项目有春季/夏季入学。请查看项目具体要求。

---

## Section 4 — Costs & financial aid

### 4.1 Undergraduate Tuition & Fees (2026-2027)

| 费用项目 | 金额 (CAD) |
|---------|-----------|
| **学费 - 国内生** | $207.69/学分 |
| **学费 - 国际生** | $1,040.15/学分 |
| 学生服务费 | $5.97/学分 (最高$89.55) |
| NUGSS Society Fee | $51.75/学期 (Prince George); $30.10/学期 (Regional) |
| NUGSS Health & Dental | $281.52/年 (全日制Prince George学生) |
| NUGSS Building Fee | $47.88/学期 (Prince George) |
| NUGSS U-Pass | $60.00/学期 (Prince George); $35.00/学期 (Quesnel) |
| NUGSS Intramural & Fitness | $68.12/学期 (Prince George) |
| 国际生医疗保险 | $190.00/学期 |
| 国际生费 | $125.00/学期 |
| **国际生学费押金** | **$9,000.00** (按录取通知要求缴纳) |
| 工科专业费 (EGBC) | $20.00 (仅秋季; 仅工科生) |
| 工科专业费 (Professional) | $56.30 (仅秋季; 仅工科生) |
| Co-op工作期费 | $623.10/工作期 |
| 新生入学指导费 | 见 Finance 网站 |
| 课程旁听费（兼读生） | $103.85/学分 (50%学费) |

> **国内生年均学费 (估算)**: 30学分/年 × $207.69 = ~$6,230 + 杂费 ≈ **$7,500-9,000**
> **国际生年均学费 (估算)**: 30学分/年 × $1,040.15 = ~$31,205 + 杂费 ≈ **$33,000-35,000**

### 4.2 Graduate Tuition & Fees (2026-2027)

#### 全日制硕士 - 国内生

基本学费单位: **$1,931.54/学期** (最低3个学费单位 = 约$5,795/年)

| 项目 | 学费单位/学期 |
|------|-------------|
| MA Disability Management | $2,450.26 |
| MEd | $2,638.73 |
| MEng | $532.68/学分 |
| MSc Health Sciences | $2,450.26 |
| MScN (Thesis/Project) | $2,450.26 |
| MScN Nurse Practitioner | $297.83/学分 |
| MSW | $2,261.78 |

#### 全日制硕士 - 国际生

基本学费单位: **$2,704.15/学期**

| 项目 | 学费单位/学期 |
|------|-------------|
| MA Disability Management | $3,430.37 |
| MEd | $3,694.22 |
| MEng | $745.76/学分 |
| MSc Health Sciences | $3,430.37 |
| MScN (Thesis/Project) | $3,430.37 |
| MScN Nurse Practitioner | $403.57/学分 |
| MSW | $3,166.49 |

#### MBA 项目费用

| 学生类别 | 学费 |
|---------|------|
| 国内生 | $989.00/学分 + $500 MBA费/学期 |
| 国际生 | $1,388.80/学分 + $500 MBA费/学期 |
| Pre-MBA课程费(国内) | $728.39 |
| Pre-MBA课程费(国际) | $886.93 |

> MBA首学期需在30天内缴纳$2,500定金

#### PhD 项目费用

| 学生类别 | 学费单位/学期 |
|---------|-------------|
| 国内生 | $1,931.54 (最低9个学费单位) |
| 国际生 | $2,704.15 (最低9个学费单位) |

#### 其他研究生杂费

| 费用项目 | 金额 (CAD) |
|---------|-----------|
| 学生社团费 (Prince George) | $81.80/学期 |
| 学生社团费 (Regional) | $75.20/学期 |
| GSS Health & Dental | $400.00/年 |
| GSS U-Pass | $60.00/学期 (Prince George) |
| 国际生费 | $125.00/学期 |
| 国际生医疗保险 | $190.00/学期 |
| 持续注册费 (硕士超2年) | $680.24/学期 |
| 持续注册费 (MBA超5学期-国内) | $1,456.79/学期 |
| 持续注册费 (MBA超5学期-国际) | $1,675.31/学期 |
| Co-op工作期费 | $864.37/工作期 |
| 毕业处理费 | $45.06 |
| 论文注册费 | $48.00 |

### 4.3 奖学金与资助

- **早入学奖学金**: 申请截止1月15日
- **一般奖学金/助学金**: 申请截止4月1日
- **研究生资助**: 各项目提供不同资助机会
- **博士学费奖学金**: 新入学博士可获得前两年学费奖学金，满意进展可续期两年

### 4.4 Housing & Residence

住宿详情通过校内住宿网站提供。

---

## Section 5 — Evidence chain index

### E-U-001: Institution Identity

| 字段 | 值 |
|------|-----|
| field | institution.name |
| value | University of Northern British Columbia |
| source_url | https://www.unbc.ca/ |
| source_snippet | "University of Northern British Columbia - Homepage | UNBC" |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-002: Academic Structure (Faculties)

| 字段 | 值 |
|------|-----|
| field | institution.academic_structure |
| value | 5 Faculties + Division of Medical Sciences |
| source_url | https://www.unbc.ca/programs-courses |
| source_snippet | "Discover UNBC's five faculties, the Division of Medical Sciences and the programs they support." |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-003: Undergraduate Programs (Full List)

| 字段 | 值 |
|------|-----|
| field | ug_programs |
| value | ~50+ UG programs across 9 degree types (BA, BSc, BComm, BASc, BEd, BHSc, BPl, BScN, BSW) |
| source_url | https://www.unbc.ca/programs-and-admissions/undergraduate/programs |
| source_snippet | Full accordion listing with degree type, program name, and campus per entry |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-004: Graduate Programs

| 字段 | 值 |
|------|-----|
| field | pg_programs |
| value | ~25+ PGT programs and ~4 PhD programs |
| source_url | https://www.unbc.ca/programs-and-admissions/graduate |
| source_snippet | Complete list of graduate programs with program-specific requirements |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-005: Application Deadlines

| 字段 | 值 |
|------|-----|
| field | application_deadlines |
| value | Detailed per-program deadlines for domestic/international by semester |
| source_url | https://www.unbc.ca/programs-and-admissions/undergraduate/undergraduate-application-deadlines |
| source_snippet | Tables showing deadlines for General Entry and Competitive Entry programs |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-006: English Language Proficiency

| 字段 | 值 |
|------|-----|
| field | english_language_requirements |
| value | TOEFL 90/IELTS 6.5/CAEL 70/PTE 65/Duolingo 125 (standard); MEng Wood Eng requires IELTS 7.0/TOEFL 100/Duolingo 135 |
| source_url | https://www.unbc.ca/admissions/graduate/english-language-proficiency |
| source_snippet | "TOEFL score of 90 or higher" and "IELTS Academic score of at least 6.5 overall" |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-007: Undergraduate Fees

| 字段 | 值 |
|------|-----|
| field | ug_tuition_fees |
| value | Domestic $207.69/credit hour; International $1,040.15/credit hour |
| source_url | https://www.unbc.ca/calendar/undergraduate/fees |
| source_snippet | Complete fee table with all mandatory fees per semester |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-008: Graduate Fees

| 字段 | 值 |
|------|-----|
| field | grad_tuition_fees |
| value | Domestic Master's $1,931.54/semester base; International Master's $2,704.15/semester base; PhD same rates |
| source_url | https://www.unbc.ca/calendar/graduate/fees |
| source_snippet | Full graduate fee schedule by program including MBA ($989/credit domestic) |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-009: Campuses

| 字段 | 值 |
|------|-----|
| field | campuses |
| value | 4 campuses: Prince George (main), Fort St. John, Quesnel, Terrace |
| source_url | https://www.unbc.ca/programs-and-admissions/undergraduate/programs |
| source_snippet | Campus filter checkboxes: Prince George, Fort St. John, Quesnel, Terrace |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

### E-U-010: Rankings & Recognition

| 字段 | 值 |
|------|-----|
| field | rankings |
| value | #2 in Maclean's Primarily Undergraduate category; #1 for students who win national awards for universities of its size |
| source_url | https://www.unbc.ca/ |
| source_snippet | "#1 for students who win national awards... #2 in the Maclean's rankings Primarily Undergraduate category" |
| capture_date | 2026-07-10 |
| evidence_type | official_webpage |

---

## Section 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 说明 |
|--------|--------|------|
| **P0** | 本科国际生ELP要求页面 | 需要在本科招生栏目(Undergraduate Programs and Admissions)通过JS导航查找English Proficiency子页面 |
| **P0** | 各项目每门课详情URL提取 | 项目详细页面URL可通过sitemap.xml获-get（7,249个URL） |
| **P1** | 各项目的具体录取平均分 | Canadian学生的具体Grade 12平均分要求因项目而异；需在Admission Requirements页查询 |
| **P1** | 各区域的详细学费差异 | Regional campus学生的部分费用略低（如NUGSS Society Fee） |
| **P2** | 国际学生各个国家具体要求 | Country-specific requirements可能通过interactive form提供，需交互访问 |
| **P2** | 校内工作/实习机会详情 | CO-OP/Internship项目的详细信息 |
| **P2** | 住宿及生活费用 | Residence和Meal Plan的具体费用 |

---

## Section 7 — Cross-school comparison framework

### Key Differentiators

| 维度 | UNBC特征 |
|------|---------|
| 学校类型 | Primarily Undergraduate University (Maclean's分类) |
| 成立年份 | 1990年 |
| 校区数量 | 4 (Prince George主 + Fort St. John + Quesnel + Terrace) |
| 国内本科学费 | $207.69/学分 (~$6,230/年30学分, +杂费~$7,500-9,000) |
| 国际本科学费 | $1,040.15/学分 (~$31,205/年30学分, +杂费~$33,000-35,000) |
| 标准语言要求 | IELTS 6.5 / TOEFL 90 / Duolingo 125 |
| 更高语言要求 | MEng Wood Engineering: IELTS 7.0 / TOEFL 100 / Duolingo 135 |
| 申请系统 | 直接申请(非OUAC) |
| 学年制度 | Semester制 (Fall/Winter/Spring-Summer) |
| 14%学生为原住民 | 原住民学生比例显著高于加拿大平均水平 |
| 绿色大学 | Canada's Green University™称号 |
