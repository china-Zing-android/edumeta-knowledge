# Murdoch University — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: college → school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU) — Western Australia
> **Platform**: ASP.NET on Microsoft Azure (IIS 10.0)

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科课程/专业 (Undergraduate) | 149 |
| 研究生授课型项目 (Postgraduate taught) | 127 |
| 荣誉学士项目 (Honours) | 57 |
| 研究型项目 (Research) | 17 |
| 预科/桥梁项目 (Enabling) | 6 |
| **总计 (Total items)** | **356** |
| 课程 (Courses) | 189 |
| 主修方向 (Majors) | 167 |
| 学院 (Colleges) | 5 |
| 学术院系 (Schools) | 12+ |
| 学习领域 (Study Areas) | 17 |
| 校区 (Campuses) | 5（Perth, Rockingham, Mandurah, Singapore, Dubai）|

### 0.2 学院 / 系层级结构 (Hierarchy Tree)

```
Murdoch University
├── College of Business
│   └── School of Business
├── College of Environmental and Life Sciences
│   ├── School of Agricultural Sciences
│   ├── School of Environmental and Conservation Sciences
│   ├── School of Medical, Molecular and Forensic Sciences
│   └── School of Veterinary Medicine
├── College of Health and Education
│   ├── School of Allied Health
│   ├── School of Education
│   ├── School of Nursing
│   └── School of Psychology
├── College of Law, Arts and Social Sciences
│   ├── School of Humanities, Arts and Social Sciences
│   ├── School of Indigenous Knowledges
│   ├── School of Law and Criminology
│   └── School of Media and Communication
└── College of Science, Technology, Engineering and Mathematics (STEM)
    ├── School of Engineering and Energy
    ├── School of Information Technology
    └── School of Mathematics, Statistics, Chemistry and Physics
```

### 0.3 学历级别明细 (Degree-level Inventory)

| 学位级别 | 英文名称 | 缩写 | 数量 |
|---------|---------|------|------|
| 本科课程 | Bachelor's Degree | Bxxx | 149 |
| 研究生授课型课程 | Master's Degree / Graduate Certificate / Graduate Diploma | Mxxx/Cxxx/Gxxx | 127 |
| 荣誉学士 | Honours Degree | Hxxx/BH- | 57 |
| 研究型学位 | Research Degree (PhD/MPhil/LLM by Research) | - | 17 |
| 预科/桥梁课程 | Enabling / Pathway Programs | - | 6 |

### 0.4 分布矩阵 (Distribution Matrix by Study Area × Level)

| Study Area | UG | PG | Honours | Research | Enabling | Total |
|-----------|----|----|---------|----------|----------|-------|
| Agricultural Science | - | - | - | - | - | 22 |
| Allied Health | - | - | - | - | - | 29 |
| Business | - | - | - | - | - | 47 |
| Creative Media and Communication | - | - | - | - | - | 30 |
| Criminology | - | - | - | - | - | 24 |
| Education | - | - | - | - | - | 42 |
| Engineering and Energy | - | - | - | - | - | 26 |
| Environmental and Conservation Sciences | - | - | - | - | - | 23 |
| Humanities, Arts and Social Sciences | - | - | - | - | - | 57 |
| Indigenous Knowledges | - | - | - | - | - | 8 |
| Information Technology | - | - | - | - | - | 47 |
| Law | - | - | - | - | - | 28 |
| Medical, Molecular and Forensic Sciences | - | - | - | - | - | 48 |
| Nursing | - | - | - | - | - | 19 |
| Physical Sciences and Mathematics | - | - | - | - | - | 17 |
| Psychology | - | - | - | - | - | 20 |
| Veterinary Science | - | - | - | - | - | 14 |
| **Total** | **149** | **127** | **57** | **17** | **6** | **356** |

> 注：Funnelback 搜索过滤器按 Study Area 统计总数（不分学历级别）。以上 Study Area 总数为 filter sidebar 直接提供，合计 356，与按学历级别加总一致。学院维度的分布矩阵因 Funnelback 搜索结果未标注学院归属，需后续通过课程代码前缀推断后补全。

---

## Section 1 — Undergraduate Education

### 1.1 本科课程 / 专业全量列表（按 College → School 分组）

> ⚠️ 以下为从 Murdoch Funnelback 课程搜索引擎提取的前 20 条结果（page 1 of 18）。全量 149 个 UG 项目需通过逐页翻页提取（Funnelback SPA 架构，不支持一次性导出）。以下为采样证明数据存在。

#### College of Business
**School of Business**

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Bachelor of Business | B1367 | BBus | 70 | [Link](https://www.murdoch.edu.au/course/undergraduate/b1367) |

#### College of Environmental and Life Sciences
**School of Agricultural Sciences**

*(Data not yet extracted from Funnelback pagination)*

**School of Environmental and Conservation Sciences**

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Marine Biology | MJ-MB | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-mb) |

**School of Medical, Molecular and Forensic Sciences**

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Forensic Biology | MJ-FBIO | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-fbio) |
| Microbiology and Immunology | MJ-MIIM | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-miim) |

#### College of Health and Education
**School of Nursing / School of Allied Health / School of Education / School of Psychology**

*(Data extraction pending full Funnelback pagination)*

#### College of Law, Arts and Social Sciences

**School of Media and Communication**

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Communication and Media Studies | MJ-CAMS | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-cams) |
| Screen Production | MJ-SCP | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-scp) |

**School of Law and Criminology**

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Bachelor of Laws / Bachelor of Criminology | B1346 | BSc/LLB | 90 | [Link](https://www.murdoch.edu.au/course/undergraduate/b1346) |

#### College of STEM

*(Data extraction pending full Funnelback pagination)*

#### Other UG Courses (sampled from search results)

| Program Name | Code | Degree Type | ATAR/Selection Rank | URL |
|-------------|------|-------------|---------------------|-----|
| Bachelor of Communication | B1342 | BComm | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1342) |
| Bachelor of Creative Media | B1343 | BCM | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1343) |
| Bachelor of Communication / Bachelor of Creative Media | B1344 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1344) |
| Bachelor of Criminology | B1345 | BCrim | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1345) |
| Bachelor of Sport and Exercise Science | B1348 | BSportExSc | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1348) |
| Bachelor of Arts | B1356 | BA | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1356) |
| Bachelor of Global Security | B1363 | BGS | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1363) |
| Bachelor of Education (Secondary Teaching) | B1368 | BEd | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1368) |
| Bachelor of Laboratory Medicine | B1374 | BLabMed | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1374) |
| Bachelor of Information Technology and Business | B1375 | BIT/Bus | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1375) |
| Bachelor of Food Science and Nutrition | B1389 | BSc | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1389) |
| Bachelor of Sport and Exercise Science / Master of High Performance Sport | B1421 | Combined | 70 | [Link](https://www.murdoch.edu.au/course/undergraduate/b1421) |
| Indigenous Knowledges and Practices | MJ-IKP | Major (UG) | - | [Link](https://www.murdoch.edu.au/course/undergraduate/mj-ikp) |
| Bachelor of Laws / Bachelor of Communication | B1353 | LLB/BComm | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1353) |
| Bachelor of Criminology / Bachelor of Communication | B1362 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1362) |
| Bachelor of Laws / Bachelor of Global Security | B1365 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1365) |
| Bachelor of Criminology / Bachelor of Global Security | B1366 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1366) |
| Bachelor of Laws / Bachelor of Business | B1369 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1369) |
| Bachelor of Laws / Bachelor of Arts | B1370 | Double | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1370) |
| Bachelor of Laws (LLB) - Graduate Entry | B1340 | LLB | - | [Link](https://www.murdoch.edu.au/course/undergraduate/b1340) |

---

## Section 2 — Graduate Education

### 2.1 研究生授课型项目 (Postgraduate Taught)

| Program Name | Code | Degree Type | URL |
|-------------|------|-------------|-----|
| Graduate Certificate in Advanced Wound Care | C1169 | GradCert | [Link](https://www.murdoch.edu.au/course/postgraduate/c1169) |
| Master of Food Security | M1311 | MSc | [Link](https://www.murdoch.edu.au/course/postgraduate/m1311) |
| Master of Health Care Management (Specialisation) | M1358 | MHealCareMgt | [Link](https://www.murdoch.edu.au/course/postgraduate/m1358) |
| Graduate Certificate in Design Thinking | C1146 | GradCert | [Link](https://www.murdoch.edu.au/course/postgraduate/c1146) |
| Graduate Certificate in Contemporary Mental Health | C1166 | GradCert | [Link](https://www.murdoch.edu.au/course/postgraduate/c1166) |
| Master of High Performance Sport | M1400 | MSc | [Link](https://www.murdoch.edu.au/course/postgraduate/m1400) |
| Graduate Diploma in Information Technology | G1086 | GradDip | [Link](https://www.murdoch.edu.au/course/postgraduate/g1086) |
| IT Management | MJ-ITMC | Major (PG) | [Link](https://www.murdoch.edu.au/course/postgraduate/mj-itmc) |

> ⚠️ 以上仅为 page 1 采样。全量 127 个 PG 项目需通过 Funnelback 逐页翻页提取。

### 2.2 研究型项目 (Research Degrees)

| Program Name | Code | Degree Type | URL |
|-------------|------|-------------|-----|
| Master of Laws by Research | M1235 | LLM by Research | [Link](https://www.murdoch.edu.au/course/research/m1235) |

### 2.3 荣誉学士项目 (Honours)

| Program Name | Code | Degree Type | URL |
|-------------|------|-------------|-----|
| Internetworking and Network Security | BH-INW | BSc(Hons) Major | [Link](https://www.murdoch.edu.au/course/honours/bh-inw) |
| Law Honours | H1267 | LLB(Hons) | [Link](https://www.murdoch.edu.au/course/honours/h1267) |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Entry Requirements

#### Undergraduate (Domestic)
- **High school leavers**: ATAR-based admission via TISC (Tertiary Institutions Service Centre)
- **ATAR range observed**: 70–90 (Bachelor of Business: 70, Bachelor of Laws/ Criminology: 90)
- **Selection Rank**: 70+ observed for most courses
- **Enabling pathways**: Ngoolark, Law Start, Pre-Law, Experience Based Entry, K-Track (Indigenous)
- **Vocational education**: Pathway from VET qualifications
- **Higher education**: Previous tertiary study considered

#### Undergraduate (International)
- Equivalent academic qualifications from home country
- English proficiency test scores required (see below)
- Genuine Student (GS) requirements

#### Postgraduate
- Completion of a recognised bachelor's degree
- English proficiency test scores required
- Specific prerequisites per course

### 3.2 English Language Requirements

| Test | Undergraduate | Postgraduate | Research |
|------|-------------|-------------|----------|
| IELTS Academic | 6.0 overall (no band < 6.0) | 6.0 overall (no band < 6.0) | 6.5 overall (no band < 6.0) |
| TOEFL iBT | 60 overall (R13, W21, S18, L12) | 60 overall (R13, W21, S18, L12) | 79 overall (R13, W21, S18, L12) |
| PTE Academic | 50 overall (R53, W54, S50, L50) | 50 overall (R53, W54, S50, L50) | 58 overall (R53, W58, S50, L50) |
| Cambridge CAE | 169 overall (no band < 169) | 169 overall (no band < 169) | 176 overall (no band < 169) |
| Duolingo (DET) | 115 overall (R110, W110, S110, L105) | 115 overall (R110, W110, S110, L105) | 120 overall (R110, W110, S110, L105) |
| Kaplan Test of English (KTE) | 444 overall (all bands 444) | 444 overall (all bands 444) | 478 overall (R444, W444, S444, L444) |
| OET | C (250-290) all bands | C (250-290) all bands | Three Cs and one B |
| LanguageCert Academic | 65 overall (R60, W64, S70, L57) | 65 overall (R60, W64, S70, L57) | 70 overall (R60, W64, S70, L57) |
| STAT | 140 Written English | - | - |

### 3.3 Application Deadlines

- **2027 TISC applications**: Now open (as of July 2026)
- Year 12 Early Offer Program available for 2027 entry
- **Domestic**: Apply through TISC or direct to Murdoch
- **International**: Apply directly or through authorised education agents
- **Research degrees**: Apply directly throughout the year

### 3.4 Application Methods
- **Year 12 school leavers**: Through TISC (tisc.edu.au)
- **Direct application**: Via Murdoch website
- **International students**: Through education agents or direct
- **Research degrees**: Direct application to Murdoch

---

## Section 4 — Costs & Financial Aid

### 4.1 International Fees (2027 Indicative)

#### Undergraduate International Fees (Sample)

| Course | First Year Fee (AUD) | Total Course Fee (AUD) |
|--------|---------------------|----------------------|
| Bachelor of Arts (B1356) | $36,720 | $110,160 |
| Bachelor of Communication (B1342) | $37,800 | $113,400 |
| Bachelor of Creative Media (B1343) | $37,800 | $113,400 |
| Bachelor of Business (B1367) | $37,800 | $113,400 |
| Bachelor of Education (Secondary Teaching) (B1368) | $37,800 | $151,200 |
| Bachelor of Laws (LLB) - Graduate Entry (B1340) | $39,360 | $118,080 |
| Bachelor of Criminology (B1345) | $39,600 | $118,800 |
| Bachelor of Information Technology and Business (B1375) | $39,600 | $118,800 |
| Bachelor of Global Security (B1363) | $36,720 | $110,160 |
| Bachelor of Laboratory Medicine (B1374) | $43,200 | $172,800 |
| Bachelor of Sport and Exercise Science (B1348) | $44,040 | $132,120 |
| Bachelor of Food Science and Nutrition (B1389) | $44,040 | $132,120 |
| Bachelor of Communication / Bachelor of Creative Media (B1344) | $37,800 | $151,200 |
| Bachelor of Laws / Bachelor of Criminology (B1346) | $39,600 | $198,000 |
| Bachelor of Laws / Bachelor of Business (B1369) | $39,600 | $198,000 |
| Bachelor of Laws / Bachelor of Arts (B1370) | $39,600 | $198,000 |

> **UG Fee Range**: $36,720 – $44,040 per year (first year indicative)
> **Total Course Fee Range**: $110,160 – $198,000

> ⚠️ 以上为第 1 页采样（20/120条）。全量 120+ 条费用记录需通过费用表格逐页提取（6 pages × 20 rows）。PG 费用数据需从费用搜索表的后续页面提取。

### 4.2 Domestic Fees (Sample)

| Course | First Year CSP Fee (AUD) | Total CSP Fee (AUD) |
|--------|-------------------------|-------------------|
| Bachelor of Business (B1367) | $17,392 | $52,176 |

> Domestic students: Commonwealth Supported Place (CSP) with government subsidy. HECS-HELP loan available.
> Student Services and Amenities Fee (SSAF) applicable.

### 4.3 Scholarships
- Wide range of scholarships available for commencing students
- Research scholarships available
- Canadian and US student loan programs available (US William D. Ford Direct Loan Program, Canadian Student Loans)
- US Department of Veterans Affairs benefits

### 4.4 Living Costs
- Various accommodation options on/off campus
- Budget for accommodation, travel, food, clothing, and entertainment
- OSHC (Overseas Student Health Cover) required for international students

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-U-001 | institution.name | "Murdoch University" | https://www.murdoch.edu.au/ | official_webpage |
| E-U-002 | colleges.count | 5 | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-003 | college.business.head | Professor Antonia Girardi | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-004 | college.env-life-sciences.head | Professor Jennifer Verduin | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-005 | college.health-edu.head | Professor Guillermo Campitelli | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-006 | college.law-arts-socsci.head | Professor Deborah Gare | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-007 | college.stem.head | Professor Parisa Bahri | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-008 | schools.list | 12+ schools across 5 colleges | https://www.murdoch.edu.au/explore/about-murdoch/our-colleges | official_webpage |
| E-U-009 | course.total_count | 356 (189 courses + 167 majors) | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-010 | course.ug_count | 149 | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-011 | course.pg_count | 127 | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-012 | course.honours_count | 57 | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-013 | course.research_count | 17 | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-014 | course.enabling_count | 6 | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-015 | study_areas.list | 17 study areas with counts | https://search.murdoch.edu.au/?collection=mu-course-search&tab=Courses&query=a | official_webpage |
| E-U-016 | english.ielts.ug | 6.0 (no band < 6.0) | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-017 | english.ielts.pg | 6.0 (no band < 6.0) | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-018 | english.ielts.research | 6.5 (no band < 6.0) | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-019 | english.toefl.ug | 60 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-020 | english.toefl.pg | 60 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-021 | english.toefl.research | 79 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-022 | english.pte.ug | 50 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-023 | english.pte.pg | 50 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-024 | english.pte.research | 58 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-025 | english.cae.ug | 169 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-026 | english.duolingo.ug | 115 overall | https://www.murdoch.edu.au/study/how-to-apply/entry-requirements/english-proficiency-tests | official_webpage |
| E-U-027 | fees.intl.2027 | Table with course codes and fees | https://www.murdoch.edu.au/study/fees/course-fees/2027-fees | official_webpage |
| E-U-028 | fees.domestic.sample | $17,392 CSP/year (Bachelor of Business) | https://www.murdoch.edu.au/course/undergraduate/b1367 | official_webpage |
| E-U-029 | campus.locations | Perth, Rockingham, Mandurah, Singapore, Dubai | https://www.murdoch.edu.au/explore/about-murdoch/our-locations | official_webpage |
| E-U-030 | platform | ASP.NET on Microsoft Azure (IIS 10.0) | https://www.murdoch.edu.au/ | server_header |
| E-U-031 | course.business.example | Bachelor of Business (B1367), ATAR 70 | https://www.murdoch.edu.au/course/undergraduate/b1367 | official_webpage |
| E-U-032 | course.law-crim.example | Bachelor of Laws / Criminology (B1346), ATAR 90 | search.murdoch.edu.au (Funnelback) | official_webpage |

---

## Section 6 — WeKnora Import Manifest & Follow-up Items

### 6.1 P0 — Immediate Follow-up (Required)

| # | Data Item | Priority | Reason |
|---|-----------|----------|--------|
| 1 | 全量 UG 课程列表（149条） | P0 | Funnelback 仅提取 page 1（20条），需翻页提取全部 8 页 UG 数据 |
| 2 | 全量 PG 课程列表（127条） | P0 | 需通过 Funnelback 逐页翻页提取 |
| 3 | 全量 Honours 列表（57条） | P0 | 需通过 Funnelback 翻页提取 |
| 4 | 全量 Research 列表（17条） | P0 | 需通过 Funnelback 翻页提取 |
| 5 | 全量国际生费用表（120+条，6页） | P0 | 费用表有 6 页分页（Kendo UI grid），需逐页提取 |
| 6 | 研究生国际生费用 | P0 | 费用表仅看到 UG 部分的前 20 条，PG 费用在后续页面 |

### 6.2 P1 — Medium Priority

| # | Data Item | Priority | Reason |
|---|-----------|----------|--------|
| 1 | 按学院维度的分布矩阵 | P1 | 当前只有 Study Area 维度。学院归属需通过课程代码前缀推断 |
| 2 | Domestic 费用全量 | P1 | 当前仅有 Bachelor of Business 样本 |
| 3 | 各课程的 ATAR/Selection Rank | P1 | 在课程详情页中有，需批量提取 |
| 4 | Course structure / curriculum per program | P1 | 在课程详情页的"Course structure"选项卡中 |
| 5 | 奖学金详情 | P1 | 有专门奖学金页面，需单独提取 |
| 6 | 申请截止日期明细 | P1 | 当前仅有泛泛信息（2027 TISC open） |

### 6.3 P2 — Nice-to-Have

| # | Data Item | Priority | Reason |
|---|-----------|----------|--------|
| 1 | 学费历史趋势（2025-2026） | P2 | 辅助分析学费增长 |
| 2 | 教员/学生比例 | P2 | 需从其他来源获取 |
| 3 | QS/The 排名数据 | P2 | 需从排名网站获取 |
| 4 | Student satisfaction / graduate outcomes | P2 | Good Universities Guide 数据 |

---

## Section 7 — Cross-school Comparison Framework

| Dimension | Murdoch University | Curtin University (WA) | UWA |
|-----------|-------------------|----------------------|-----|
| Location | Perth, WA | Perth, WA | Perth, WA |
| Total programmes | 356 (189 courses + 167 majors) | TBD | TBD |
| Colleges | 5 | TBD | TBD |
| ATAR range (observed) | 70-90 | TBD | TBD |
| IELTS UG minimum | 6.0 (no band < 6.0) | TBD | TBD |
| International UG fees (range/year) | $36,720 - $44,040 | TBD | TBD |
| Domestic CSP (sample) | $17,392 (Business) | TBD | TBD |
| Platform | ASP.NET/Azure (Funnelback search) | TBD | TBD |

---

## Appendix A — Study Areas Detail (with Funnelback filter counts)

| Study Area | Course Count | 
|-----------|-------------|
| Agricultural Science | 22 |
| Allied Health | 29 |
| Business | 47 |
| Creative Media and Communication | 30 |
| Criminology | 24 |
| Education | 42 |
| Engineering and Energy | 26 |
| Environmental and Conservation Sciences | 23 |
| Humanities, Arts and Social Sciences | 57 |
| Indigenous Knowledges | 8 |
| Information Technology | 47 |
| Law | 28 |
| Medical, Molecular and Forensic Sciences | 48 |
| Nursing | 19 |
| Physical Sciences and Mathematics | 17 |
| Psychology | 20 |
| Veterinary Science | 14 |
| **Total** | **356** |

## Appendix B — Available Course Codes (Sample from Search Page 1)

Sample course codes observed:
- **Undergraduate**: B1340 (LLB Grad Entry), B1342 (BComm), B1343 (BCM), B1344 (Double), B1345 (BCrim), B1346 (LLB/BCrim), B1348 (BSportExSc), B1353 (LLB/BComm), B1356 (BA), B1362 (BCrim/BComm), B1363 (BGS), B1365 (Double), B1366 (Double), B1367 (BBus), B1368 (BEd), B1369 (Double), B1370 (Double), B1374 (BLabMed), B1375 (BIT/Bus), B1389 (BSc), B1421 (Combined)
- **UG Majors**: MJ-CAMS, MJ-MIIM, MJ-FBIO, MJ-SCP, MJ-MB, MJ-IKP
- **Postgraduate**: C1169, M1311, M1358, C1146, C1166, M1400, G1086, MJ-ITMC
- **Research**: M1235 (LLM by Research)
- **Honours**: BH-INW, H1267 (Law Honours)

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Murdoch University official website (murdoch.edu.au)
> **Granularity**: college → school → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ⚠️ (sampled, full 149 pending Funnelback pagination) | PG programmes ⚠️ (sampled, full 127 pending) | Evidence (32 blocks) ✅
> **Next step**: Execute P0 follow-ups (Funnelback pagination extraction for all 356 courses + Kendo UI grid fees extraction for all 120+ fee entries)
