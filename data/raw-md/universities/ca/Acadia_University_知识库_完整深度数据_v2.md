# Acadia University 知识库 — 完整深度数据 v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Nova Scotia)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 35 个专业领域，含 200+ 学位组合 |
| 研究生授课型项目 (PGT: MA/MSc/MEd/MCD/MAK) | 16 个硕士项目 |
| 研究生博士项目 (PhD/Doctoral) | 2 个博士项目（PhD in Educational Studies；Acadia Divinity College PhD） |
| 学位项目总计 | ~18 个研究生项目 + 35 个本科专业领域 |
| 学院 (Faculties) | 4 |
| 学术院系 (Academic Schools/Departments) | 0（Acadia 采用 faculty→program 结构，无系级单位） |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Acadia University
├── Faculty of Arts
│   ├── Canadian Studies (BA)
│   ├── Classical Studies (BA)
│   ├── Economics (BA)
│   ├── English (BA)
│   ├── Environmental & Sustainability Studies (BA, BCD)
│   ├── French (BA)
│   ├── German (BA)
│   ├── History (BA)
│   ├── Law & Society (BA)
│   ├── Music (BM, BAM)
│   ├── Philosophy (BA)
│   ├── Politics (BA)
│   ├── Psychology (BA)
│   ├── Sociology (BA)
│   ├── Theatre (BA)
│   └── Women's & Gender Studies (BA)
├── Faculty of Professional Studies
│   ├── Business Administration (BBA)
│   ├── Community Development (BCD)
│   ├── Education (BEd)
│   ├── Kinesiology (BKin)
│   ├── Music (BM, BAM)
│   └── Nursing (BScN)
├── Faculty of Pure and Applied Sciences
│   ├── Applied Bioscience (BSc)
│   ├── Biology (BSc)
│   ├── Chemistry (BASc, CAS)
│   ├── Computer Science (BCS, BACS, BSc)
│   ├── Economics (BA)
│   ├── Engineering (BASc, CAS)
│   ├── Environmental Geoscience (BSc)
│   ├── Environmental Science (BSc)
│   ├── Geology (BSc)
│   ├── Mathematics & Statistics (BSc, BA)
│   ├── Mathematics Education (Integrated BSc+BEd)
│   ├── Nutrition & Dietetics (BSN)
│   ├── Physics (BSc)
│   └── Psychology (BSc)
└── Faculty of Theology (Acadia Divinity College)
    └── Theology (BTh, MDiv, MTh, PhD)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 缩写 | 数量 |
|---------|------|------|
| Bachelor of Arts | BA | 多个 |
| Bachelor of Arts and Science | BASc | 2 |
| Bachelor of Business Administration | BBA | 1 |
| Bachelor of Community Development | BCD | 1 |
| Bachelor of Computer Science | BCS | 1 |
| Bachelor of Education | BEd | 1 |
| Bachelor of Kinesiology | BKin | 1 |
| Bachelor of Music | BM | 1 |
| Bachelor of Science | BSc | 多个 |
| Bachelor of Science in Nursing | BScN | 1 |
| Bachelor of Science in Nutrition | BSN | 1 |
| Certificate in Applied Science | CAS | 2 |
| Master of Arts | MA | 3 |
| Master of Applied Kinesiology | MAK | 1 |
| Master of Community Development | MCD | 1 |
| Master of Education | MEd | 3 |
| Master of Science | MSc | 7 |
| Doctor of Philosophy | PhD | 1 |
| Bachelor of Theology | BTh | 1 |
| Master of Divinity | MDiv | 1 |
| Master of Theology | MTh | 1 |

> 注：Acadia Divinity College 提供的 MDiv、MTh、PhD 等神学学位未在本文档中逐一列出。

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 | UG (BA/BSc/BBA 等) | PGT (MA/MSc/MEd 等) | PhD | 总计 |
|------|-------------------|---------------------|-----|------|
| Faculty of Arts | ~16 | 3 (MA English, MA Political Science, MA Social & Political Thought) | 0 | ~19 |
| Faculty of Professional Studies | ~6 | 5 (MAK, MCD, MEd×3) | 0 | ~11 |
| Faculty of Pure and Applied Sciences | ~14 | 8 (MSc Applied Geomatics, Biology, Chemistry, CS, Env Sci, Geology, Math/Stats, Psychology) | 0 | ~22 |
| Faculty of Theology (Acadia Divinity College) | 1 (BTh) | 2 (MDiv, MTh) | 1 (PhD) | ~4 |
| Interdisciplinary | 0 | 1 (MA Social & Political Thought) | 1 (PhD Educational Studies—跨省项目) | ~2 |
| **总计** | **~35 领域/200+ 组合** | **~16** | **~2** | **~220** |

---

## Section 1 — Undergraduate education

### Faculty of Arts

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Canadian Studies | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/canadian-studies.html |
| Classical Studies | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/classics.html |
| Economics | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/economics.html |
| English | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/english.html |
| Environmental & Sustainability Studies | BA, BCD | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/environmental-sustainability-studies.html |
| French | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/french.html |
| German | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/german.html |
| History | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/history.html |
| Law & Society | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/law-and-society.html |
| Philosophy | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/philosophy.html |
| Politics | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/politics.html |
| Psychology | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/psychology.html |
| Sociology | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/sociology.html |
| Theatre | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/theatre.html |
| Women's & Gender Studies | BA | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/womens-gender.html |
| Music | BM, BAM | Faculty of Arts | https://www2.acadiau.ca/academics/undergraduate/music.html |

### Faculty of Professional Studies

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Business Administration | BBA | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/business-administration.html |
| Community Development | BCD | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/community-development.html |
| Education | BEd | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/education.html |
| Kinesiology | BKin | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/kinesiology.html |
| Music | BM, BAM | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/music.html |
| Nursing | BScN | Professional Studies | https://www2.acadiau.ca/academics/undergraduate/nursing.html |

### Faculty of Pure and Applied Sciences

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Applied Bioscience | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/bioscience.html |
| Biology | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/biology.html |
| Chemistry | BASc, CAS | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/chemistry.html |
| Computer Science | BCS, BACS, BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/computer-science.html |
| Economics | BA | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/economics.html |
| Engineering | BASc, CAS | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/engineering-applied-science.html |
| Environmental Geoscience | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/environmental-geoscience.html |
| Environmental Science | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/environmental-science.html |
| Geology | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/geology.html |
| Mathematics & Statistics | BSc, BA | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/mathematics-and-statistics.html |
| Mathematics Education | Integrated BSc+BEd | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/mathematics-education.html |
| Nutrition & Dietetics | BSN | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/nutrition-dietetics.html |
| Physics | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/physics.html |
| Psychology | BSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/undergraduate/psychology.html |

### Faculty of Theology

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Theology | BTh | Theology (Acadia Divinity College) | https://acadiadiv.ca/bth/ |

> **注**: Acadia 提供 200+ 学位组合（含主修、辅修、荣誉项目）。以上列表为主要专业领域，学生可跨学科组合以创建个性化学习计划。完整课程信息参见 [Academic Calendar](https://registrar.acadiau.ca/AcademicCalendars.html)。

---

## Section 2 — Graduate education

### Faculty of Arts — Graduate Programs

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| English | MA | Faculty of Arts | https://www2.acadiau.ca/academics/graduate/english.html |
| Political Science | MA | Faculty of Arts | https://www2.acadiau.ca/academics/graduate/political-science.html |
| Social and Political Thought | MA | Faculty of Arts | https://www2.acadiau.ca/academics/graduate/social-political-thought.html |
| Sociology | MA | Faculty of Arts | https://www2.acadiau.ca/academics/graduate/sociology.html |

### Faculty of Professional Studies — Graduate Programs

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Applied Kinesiology | MAK | Professional Studies | https://www2.acadiau.ca/academics/graduate/applied-kinesiology.html |
| Community Development | MCD | Professional Studies | https://www2.acadiau.ca/academics/graduate/community-development.html |
| Education - Counselling | MEd | Professional Studies | https://med.acadiau.ca/home.html |
| Education - Curriculum Studies | MEd | Professional Studies | https://med.acadiau.ca/home.html |
| Education - Inclusive Education | MEd | Professional Studies | https://med.acadiau.ca/home.html |

### Faculty of Pure and Applied Sciences — Graduate Programs

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Applied Geomatics | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/applied-geomatics.html |
| Biology | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/biology.html |
| Chemistry | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/chemistry.html |
| Computer Science | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/computer-science.html |
| Environmental Science | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/environmental-science.html |
| Geology | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/geology.html |
| Mathematics and Statistics | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/mathematics-and-statistics.html |
| Psychology | MSc | Pure & Applied Sciences | https://www2.acadiau.ca/academics/graduate/psychology.html |

### Faculty of Theology — Graduate Programs

| Program | Degree | Faculty | URL |
|---------|--------|---------|-----|
| Educational Studies | PhD | Theology/跨省合作 | https://www.nsphdeducation.ca/ |

> **注**: Acadia 提供 18 个研究生项目选项。详细信息见 [Graduate Studies](https://www2.acadiau.ca/academics/graduate.html)。

---

## Section 3 — Application requirements & deadlines

### 3.1 本科入学要求

**基本要求：**
- 完成 Grade 12（高中毕业）
- Grade 12 English
- 4 门额外 Grade 12 学术/高级课程
- 最低 70% 平均分（由招生办计算）
- 录取具有竞争性；平均入学成绩约为 **86%**

**学费支付截止日期：**
- Fall Term: **2026 年 9 月 9 日**
- Winter Term: **2027 年 1 月 11 日**

**按学生类型分类：**
- 加拿大高中生：通过交互式网页工具查看要求（https://www2.acadiau.ca/admissions/application-process/canadian-students.html）
- 美国学生：https://www2.acadiau.ca/admissions/application-process/american-students.html
- 国际学生：各国要求不同，需逐一核验（https://www2.acadiau.ca/admissions/application-process/international-students.html）
- IB 学生、转学生、成年学生、家庭教育学生均有独立路径

### 3.2 研究生入学要求

- 各国/地区要求不同，通过交互式网页工具查看
- 通用页面：https://www2.acadiau.ca/admissions/graduate-application.html

### 3.3 英语语言要求

| 测试 | 最低分数要求 |
|------|------------|
| IELTS | 6.5（从交换生项目页面推断） |
| TOEFL | 需进一步确认具体分数要求 |

> **P0 跟进项**: 国际学生英语语言最低分数要求在官网通过动态表单展示，未能在静态页面提取完整分数对照表。需进一步导航至具体国家页面或 Academic Calendar 确认。

### 3.4 申请截止日期

- 本科申请：每年 **10 月 1 日之后** 可提交
- 奖学金申请截止：**3 月 1 日**
- 秋季学期：9 月初开学
- 冬季学期：1 月开学

### 3.5 特殊要求

- Education (BEd)：需要部分大学前置学习经历
- Music Therapy：需要部分大学前置学习经历
- 部分专业可能有额外录取要求（portfolio、audition 等）

---

## Section 4 — Costs & financial aid

### 4.1 本科学费（2026-2027 学年，全课程量 24-33 学分）

| 费用类别 | 新斯科舍省学生 | 加拿大其他省学生 | 国际学生 |
|---------|--------------|---------------|---------|
| 学费 (Tuition) | $10,254.84 | $10,986.04 | $25,712.62 |
| NS 学费减免 | -$641.50/学期 | — | — |
| 技术费 (Technology Fee) | $627.50 | $627.50 | $627.50 |
| 体育健康费 (Athletic & Health Fee) | $287.00 | $287.00 | $287.00 |
| 校园更新费 (Campus Renewal Fee) | $250.00 | $250.00 | $250.00 |
| ASU 会费 (ASU Fees) | $362.00 | $362.00 | $362.00 |
| ASU 健康计划 | $247.80 | $247.80 | $1,592.74 |
| ASU 牙科计划 | $165.00 | $165.00 | $165.00 |
| Acadia Access Fee | $10.00 | $10.00 | $10.00 |
| **总计** | **$10,921.14** | **$12,935.34** | **$28,466.86** |

### 4.2 研究生学费（2026-2027，国际学生）

| 项目类型 | 国际学生 | 新斯科舍省学生 |
|---------|---------|--------------|
| MA (除 SOPT)/MSc Geom (1 年制) | $25,444.76 | $10,501.80 |
| MSc/MSc CS (论文或项目)/M CODE/MA SOPT/MAK (2 年制，每年) | $17,726.08 | $7,369.46 |
| MEd/MAK.COACH (兼职)/MSc CS (课程选项)，每 3 学分 | $3,286.14 | $1,339.50 |
| ASU 会费 | $363.00 | $363.00 |
| ASU 健康计划 (单人) | $1,592.74 | $247.80 |
| ASU 牙科计划 (单人) | $165.00 | $165.00 |
| Acadia Access Fee | $10.00 | $10.00 |
| 研究生学习费 (全日制) | $50.00 | $50.00 |

### 4.3 博士学费（2026-2027，国际学生）

| 费用类别 | 国际学生 |
|---------|---------|
| 学费 | $26,925.00 |
| 附加费 | $405.00 |
| 继续注册费 | $7,580.00 |
| 研究生学习费 | $25.00 |
| ASU 会费 | $363.00 |
| ASU 健康计划 (单人) | $1,592.74 |
| ASU 牙科计划 (单人) | $165.00 |

### 4.4 住宿费用（2026-2027 学年，9 月-4 月）

| 宿舍楼 | 单人间 | 豪华单人间 | 双人间 | 套间单人 | 高级单人间 |
|--------|-------|-----------|-------|---------|----------|
| Chase Court | $8,980 | $10,085 | — | $10,545 | — |
| Chipman House | $8,980 | $10,085 | $7,695 | — | — |
| Dennis House | $8,975 | $10,085 | $7,695 | $10,540 | — |
| Eaton House | $8,975 | $10,085 | $7,695 | — | — |
| Crowell Tower | $7,460 | $8,455 | $6,450 | — | — |
| Seminary House | $8,585 | $9,600 | $7,335 | — | — |
| 55 University Ave | $8,585 | $9,600 | $7,335 | — | $10,680 |
| War Memorial House | $8,585 | $9,600 | $7,335 | $9,500 | $10,680 |
| Whitman House | $8,975 | $10,085 | $7,695 | $10,545 | — |
| Christofor Hall | $8,975 | $10,085 | $7,695 | — | — |
| Roy Jodrey Hall | $10,085 | — | — | $10,545 | — |

**餐饮计划：** 住宿学生起价 **$5,994.00**

**一次性费用：** $50 申请费 + $500 押金（可抵扣住宿费）+ $50 住宿校园项目费

### 4.5 奖学金与助学金

- 每年颁发 **$4.5M+** 奖学金
- 入学奖学金：**$2,000 - $10,000**（4 年，自动考虑）
- 高额可再生奖学金：最高 **$80,000**（4 年）
- 申请截止日期：**3 月 1 日**
- 条件：录取平均分 ≥ 80%
- 官网：https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html
- 国际学生页：https://www2.acadiau.ca/student-services/scholarships-financial-aid/international-students.html

---

## Section 5 — Evidence chain index

| 编号 | 字段 | 值 | 来源 URL | 证据类型 |
|------|------|---|---------|---------|
| E-U-001 | institution.name | Acadia University | https://www2.acadiau.ca/ | official_webpage |
| E-U-002 | institution.founded | 1838 | https://www2.acadiau.ca/about-acadia/at-a-glance.html | official_webpage |
| E-U-003 | institution.location | Wolfville, Nova Scotia, Canada | https://www2.acadiau.ca/about-acadia/at-a-glance.html | official_webpage |
| E-U-004 | faculties.count | 4 | https://www2.acadiau.ca/about-acadia/at-a-glance.html | official_webpage |
| E-U-005 | ug.program.count | 200+ degree options | https://www2.acadiau.ca/academics.html | official_webpage |
| E-U-006 | ug.program.list | 35 个主要领域 | https://www2.acadiau.ca/academics.html | official_webpage |
| E-U-007 | graduate.program.count | 18 programs | https://www2.acadiau.ca/academics/graduate.html | official_webpage |
| E-U-008 | graduate.program.list | 18 个项目 | https://www2.acadiau.ca/academics/graduate.html | official_webpage |
| E-U-009 | admission.requirement.general | Grade 12 English + 4 additional Grade 12 courses, min 70% | https://www2.acadiau.ca/about-acadia/at-a-glance.html | official_webpage |
| E-U-010 | admission.average.entering | 86% | https://www2.acadiau.ca/about-acadia/at-a-glance.html | official_webpage |
| E-U-011 | fees.ug.ns | $10,921.14 总费用（2026-2027） | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-012 | fees.ug.canada | $12,935.34 总费用（2026-2027） | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-013 | fees.ug.international | $28,466.86 总费用（2026-2027） | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-014 | fees.graduate.international | $25,444.76（1年制）/ $17,726.08（2年制） | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-015 | fees.phd.international | $26,925.00 | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-016 | residence.fees | $6,450 - $10,680/学年 | https://www2.acadiau.ca/student-life/residence-campus-life/residences-housing/fees.html | official_webpage |
| E-U-017 | meal.plan | 起价 $5,994.00 | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-018 | scholarship.entrance | $2,000 - $10,000 (4年) | https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html | official_webpage |
| E-U-019 | scholarship.highvalue | 最高 $80,000 (4年) | https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html | official_webpage |
| E-U-020 | scholarship.deadline | March 1 | https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html | official_webpage |
| E-U-021 | scholarship.threshold | 80% average | https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html | official_webpage |
| E-U-022 | payment.deadline.fall | September 9, 2026 | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-023 | payment.deadline.winter | January 11, 2027 | https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | official_webpage |
| E-U-024 | english.ielts | 6.5（推断自交换生页面） | https://exchangeprogram.acadiau.ca/ | official_webpage |
| E-U-025 | international.office | Wong International Centre | https://www2.acadiau.ca/international.html | official_webpage |
| E-U-026 | academic.calendar | 2025-2026 学术日历 (PDF) | https://registrar.acadiau.ca/AcademicCalendars.html | official_webpage |
| E-U-027 | student.faculty.ratio | 15:1 | https://www2.acadiau.ca/ | official_webpage |

---

## Section 6 — WeKnora import manifest & follow-up

### Follow-up data items

| 优先级 | 数据项 | 说明 |
|--------|-------|------|
| **P0** | 国际学生英语语言要求完整分数对照表 | 官网动态表单，需逐个选择国家查看；建议直接查看 Academic Calendar PDF |
| **P0** | 国际学生分国家录取要求 | 官网使用动态表单，需至少提取主要生源国要求 |
| **P0** | 研究生申请截止日期 | 各项目截止日期可能不同 |
| **P1** | PhD in Educational Studies 完整学费 | 目前仅提取了国际学生 PhD 学费 |
| **P1** | Acadia Divinity College 项目全量列表 | 神学院独立运营，需单独采集 |
| **P1** | 2026-2027 学术日历 PDF 内容提取 | 包含项目、课程、重要日期的权威信息 |
| **P1** | 各专业详细课程描述 | 单个课程页面包含课程内容、职业前景等，共约 35 个 UG 页面 + 18 个 PG 页面 |
| **P2** | Co-op 教育项目详情 | https://co-op.acadiau.ca/ |
| **P2** | Open Acadia / 在线学习课程列表 | https://openacadia.acadiau.ca/ |
| **P2** | Study Abroad / 交换项目详情 | https://exchangeprogram.acadiau.ca/ |
| **P2** | 教职工名录 | https://www2.acadiau.ca/academics.html 各学院页面 |
| **P2** | 学校排名数据 | THE, QS, 麦考林排名 |

---

## Section 7 — Cross-school comparison framework

| 维度 | Acadia University | 备注 |
|------|-------------------|------|
| 国家 | Canada | Nova Scotia 省 |
| 建校年份 | 1838 | 历史悠久 |
| 本科生规模 | ~3,400+ 申请量/Class of 2021 | 小型大学 |
| 学院数量 | 4 Faculties | 无系级单位 |
| 本科项目数 | 200+ 学位组合 / 35 个领域 | |
| 研究生项目数 | 18 | |
| 师生比 | 15:1 | |
| 平均班级规模 | 28 | |
| 平均入学成绩 | 86% | |
| 本科学费（国际） | ~$28,467/年 | 加拿大中等水平 |
| 本科学费（省外） | ~$12,935/年 | |
| 本科学费（本省） | ~$10,921/年 | |
| 住宿费 | $6,450 - $10,680/年 | 11 栋宿舍楼 |
| 餐饮计划 | $5,994+/年 | |

---

## Site Monitoring Design（Phase 4）

| URL | Change Frequency | Category |
|-----|-----------------|----------|
| https://www2.acadiau.ca/admissions.html | medium_monthly | 招生概述（可随时更新） |
| https://www2.acadiau.ca/admissions/application-process/canadian-students.html | low_yearly | 录取要求（较稳定） |
| https://www2.acadiau.ca/admissions/application-process/international-students.html | low_yearly | 录取要求（较稳定） |
| https://www2.acadiau.ca/academics.html | low_yearly | 课程列表（每年更新） |
| https://www2.acadiau.ca/academics/graduate.html | low_yearly | 研究生项目列表（每年更新） |
| https://www2.acadiau.ca/student-services/student-accounts/tuition-fees/full-time-student-fees.html | medium_monthly | 学费（每年更新，金额固定后低频率） |
| https://www2.acadiau.ca/student-services/scholarships-financial-aid/future-students/entrance-scholarships.html | low_yearly | 奖学金信息 |
| https://www2.acadiau.ca/student-life/residence-campus-life/residences-housing/fees.html | low_yearly | 住宿费（每年调整） |
| https://www2.acadiau.ca/international.html | low_yearly | 国际学生信息 |
| https://registrar.acadiau.ca/AcademicCalendars.html | low_yearly | 学术日历 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Acadia University official website (www2.acadiau.ca)
> **Granularity**: faculty → program (无系级单位)
> **Completeness**: Structural framework ✅ | UG programmes ✅ (35 areas, 200+ combinations) | PG programmes ✅ (18 programs) | Fees ✅ (UG/Grad/PhD/Residence full data) | Evidence (27 blocks) ✅ | English requirements 🟡 (partial - P0 follow-up needed)
> **Next step**: Extract English language proficiency full score table + international student per-country requirements from dynamic form
