# New York University (NYU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless) + JS DOM extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Scope**: New York (NYC) campus — 11 degree-granting UG schools + 15 grad/professional schools; NYU Abu Dhabi & NYU Shanghai (separate portal campuses) excluded

---

## SECTION 0 — 院校总览 (Institution overview)

NYU 是一所位于纽约市曼哈顿的私立研究型大学,主校区位于华盛顿广场,工程学院(Tandon)位于布鲁克林 downtown。NYU 由 11 所本科学院 + 数个研究生/专业学院组成,并在阿布扎比和上海设有独立学位授予校区(本文档聚焦纽约校区)。本科招生统一由 Office of Undergraduate Admissions 管理;研究生招生去中心化,由各学院自行管理,但各学院完整项目目录均可在 bulletins.nyu.edu 的 per-school programs 页面获取。

### 0.1 专业与项目总数

| 维度 | 数量 | 来源 |
|------|------|------|
| 本科学位专业 (BA/BS/BFA/BM + 双学位 + 副学士) | 181 | bulletins.nyu.edu/undergraduate/*/programs/ |
| 本科辅修 (Minor) | 146 | bulletins.nyu.edu/undergraduate/*/programs/ |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/DNP/JD/MD/DDS… 双学位) | 337 | bulletins.nyu.edu/graduate/*/programs/ |
| 研究生高级证书/文凭 (Advanced Certificate / Diploma) | 66 | bulletins.nyu.edu/graduate/*/programs/ |
| **学位项目总计 (UG + Grad, NYC only)** | **730** | reconciliation: 见 0.4 末尾 |
| 本科学院 / 学校总数 (NYC, UG-granting) | 13 | bulletins.nyu.edu/undergraduate/ |
| 研究生 / 专业学院总数 (NYC) | 15 | bulletins.nyu.edu/graduate/ |

> 计数方法:对每个 bulletins.nyu.edu 的 per-school programs 页面提取所有 `/programs/<slug>/` 链接(学位标注取自链接文本末尾括号),按 URL 全局去重(因为某些项目在多个学院页面上交叉列出,实际管理归属由 URL 路径中的 school slug 决定)。NYU Abu Dhabi / NYU Shanghai 已从计数中排除。

### 0.2 学院 / 系层级结构

```
New York University (NYU) — New York campus
│
│  === 本科学院 (Undergraduate, 13 schools grant UG degrees) ===
├── College of Arts & Science (CAS)                                  [学院]
│   ├── 人文/语言/哲学系 (Humanities)                                [系]
│   ├── 自然科学系 (Natural Sciences: Bio, Chem, Physics, Math, CNS)  [系]
│   ├── 社会科学系 (Social Sciences: Econ, Politics, Psych, Soc)     [系]
│   └── 跨学科/区域研究系                                            [系]
├── Tandon School of Engineering                                     [学院]
│   ├── Computer Science and Engineering Department                  [系]
│   ├── Electrical & Computer Engineering                            [系]
│   ├── Mechanical & Aerospace Engineering                           [系]
│   ├── Civil & Urban Engineering / CUSP                             [系]
│   ├── Chemical & Biomolecular Engineering / Applied Physics        [系]
│   ├── Technology Management & Innovation / IDM                     [系]
│   ├── Mathematics                                                  [系]
│   └── Center for K-12 STEM Education (Bridge)                      [系]
├── Tisch School of the Arts                                         [学院]
│   ├── Institute of Performing Arts (Drama, Dance, Grad Acting)     [系]
│   ├── Maurice Kanbar Institute of Film & Television                [系]
│   ├── Clive Davis Institute of Recorded Music                      [系]
│   ├── Photography & Imaging / Art & Public Policy                  [系]
│   └── Graduate Musical Theater Writing / ITP/IMA                   [系]
├── Stern School of Business                                         [学院]
│   └── (不再细分系; Core Business Program + BPE)                    [系]
├── Steinhardt School of Culture, Education, and Human Development   [学院]
│   ├── Department of Teaching & Learning                            [系]
│   ├── Department of Music & Performing Arts Professions            [系]
│   ├── Department of Art & Arts Professions                         [系]
│   ├── Department of Media, Culture, and Communication              [系]
│   ├── Department of Nutrition & Food Studies / Public Health       [系]
│   ├── Department of Occupational Therapy                           [系]
│   ├── Department of Physical Therapy                               [系]
│   └── Department of Communicative Sciences & Disorders             [系]
├── Rory Meyers College of Nursing                                   [学院]
│   └── (本研究生院不再细分系)                                        [系]
├── Silver School of Social Work                                     [学院]
│   └── (本研究生院不再细分系)                                        [系]
├── School of Global Public Health (joint w/ multiple schools)       [学院]
│   └── (跨 CAS / Nursing / Wagner / Steinhardt 的联合学院)          [系]
├── Gallatin School of Individualized Study                          [学院]
│   └── (个性化专业,不再细分系)                                       [系]
├── Liberal Studies                                                  [学院]
│   └── (Global Liberal Studies BA + LS Core 2-yr)                   [系]
├── School of Professional Studies (SPS)                             [学院]
│   ├── Tisch Center for Hospitality                                 [系]
│   ├── Tisch Institute for Global Sport                             [系]
│   └── Schack Institute of Real Estate                              [系]
├── College of Dentistry (UG: Dental Hygiene)                        [学院]
│   └── (Dental Hygiene programs)                                    [系]
│
│  === 研究生 / 专业学院 (Graduate/Professional, 15 schools in NYC) ===
├── Graduate School of Arts and Science (GSAS)                       [学院]
│   └── Courant Institute of Mathematical Sciences  ⚠ shared w/ Tandon (CS/Data) [系]
├── Tandon School of Engineering  (见上; 同时授予 MS/PhD)             [学院]
├── Stern School of Business  (见上; MBA/MS/PhD)                     [学院]
├── Steinhardt (见上; 同时授予 MA/MS/PhD/EdD/DPT/OTD)                [学院]
├── Tisch School of the Arts (见上; MFA/MA/PhD)                      [学院]
├── Robert F. Wagner Graduate School of Public Service               [学院]
│   └── (MPA/MPUP/EMPA/PhD; 不再细分系)                              [系]
├── Rory Meyers College of Nursing (见上; MS/DNP/PhD)                [学院]
├── School of Global Public Health (见上; MPH/DrPH/Adv Cert)         [学院]
├── Silver School of Social Work (见上; MSW/DSW/PhD)                 [学院]
├── Gallatin School of Individualized Study (见上; MA)               [学院]
├── School of Professional Studies (见上; MS/MPS)                    [学院]
├── College of Dentistry (见上; DDS/MS/AEGD)                         [学院]
├── School of Law  (JD/LLM/JSD/MSL; 独立招生)                        [学院]
├── NYU Grossman School of Medicine  (MD/MS/PhD; 独立招生)           [学院]
└── NYU Grossman Long Island School of Medicine  (MD; 独立招生)      [学院]
```

> 注:Courant Institute(CS、Data Science、Math)在 UG 隶属于 CAS,在 grad 跨 GSAS / Tandon — Data Science & CS 的 Courant 版本归 GSAS,Tandon 版本归 Tandon,两者并列(已通过 URL slug `courant-ms` vs `tandon-ms` 区分)。School of Global Public Health 是 CAS/Nursing/Wagner/Steinhardt 的跨校联合学院。

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 78 |
| BS | Bachelor of Science | 本科 | 64 |
| BFA | Bachelor of Fine Arts | 本科 | 10 |
| BM | Bachelor of Music | 本科 | 6 |
| BS/BS | Dual BS/BS (CAS + Tandon) | 本科 | 12 |
| BS/MS | Dual BS/MS | 本科 | 2 |
| BA/DDS | Dual BA/DDS | 本科 | 1 |
| BFA/MS | Dual BFA/MS | 本科 | 1 |
| AAS | Associate of Applied Science | 本科 | 5 |
| AA | Associate of Arts | 本科 | 1 |
| (Core) | Core program (non-degree) | 本科 | 1 |
| Minor | Undergraduate Minor | 本科辅修 | 146 |
| MA | Master of Arts | 研究生 | 90 |
| MS | Master of Science | 研究生 | 92 |
| MFA | Master of Fine Arts | 研究生 | 11 |
| MBA | Master of Business Administration | 研究生 | 6 |
| MPA | Master of Public Administration | 研究生 | 3 |
| MPS | Master of Professional Studies | 研究生 | 2 |
| MAT | Master of Arts in Teaching | 研究生 | 4 |
| MM | Master of Music | 研究生 | 5 |
| MHA | Master of Health Administration | 研究生 | 1 |
| MUP | Master of Urban Planning | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MS/MA | Dual MS/MA (grad) | 研究生 | 1 |
| MS/MS | Dual MS/MS (grad) | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生/博士 | 1 |
| PhD | Doctor of Philosophy | 研究生/博士 | 85 |
| EdD | Doctor of Education | 研究生/博士 | 4 |
| DNP | Doctor of Nursing Practice | 研究生/博士 | 6 |
| DPH | Doctor of Public Health | 研究生/博士 | 1 |
| DSW | Doctor of Social Work | 研究生/博士 | 1 |
| DPT | Doctor of Physical Therapy | 研究生/博士 | 2 |
| OTD | Doctor of Occupational Therapy | 研究生/博士 | 2 |
| MD | Doctor of Medicine | 研究生/博士 | 2 |
| DDS | Doctor of Dental Surgery | 研究生/博士 | 1 |
| JD | Juris Doctor | 研究生/博士 | 1 |
| LLM | Master of Laws | 研究生 | 10 |
| JSD | Doctor of Juridical Science | 研究生/博士 | 1 |
| MSL | Master of Studies in Law | 研究生 | 1 |
| Advanced Certificate | Advanced Certificate | 研究生证书 | 63 |
| Advanced Certificate of Achievement | Advanced Certificate of Achievement | 研究生证书 | 1 |
| Advanced Diploma | Advanced Diploma | 研究生证书 | 2 |
| **合计** | | | **730** |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 \ 级别 | UG Major | UG Minor | Grad Degree | Grad Cert/Diploma | 合计 |
|------------|----------|----------|-------------|-------------------|------|
| CAS / GSAS | 86 | 75 | 100 | 16 | 277 |
| Dentistry | 2 | 0 | 3 | 7 | 12 |
| Gallatin | 1 | 1 | 1 | 0 | 3 |
| Stern | 4 | 2 | 23 | 1 | 30 |
| Liberal Studies | 3 | 2 | 0 | 0 | 5 |
| Wagner | 0 | 2 | 7 | 7 | 16 |
| Nursing (Meyers) | 3 | 0 | 16 | 10 | 29 |
| Global Public Health | 0 | 2 | 6 | 4 | 12 |
| SPS | 18 | 3 | 23 | 0 | 44 |
| Social Work (Silver) | 2 | 3 | 3 | 0 | 8 |
| Steinhardt | 36 | 19 | 90 | 10 | 155 |
| Tandon | 15 | 25 | 33 | 3 | 76 |
| Tisch | 11 | 12 | 13 | 0 | 36 |
| Law | 0 | 0 | 15 | 3 | 18 |
| Grossman Med | 0 | 0 | 3 | 5 | 8 |
| Grossman LI Med | 0 | 0 | 1 | 0 | 1 |
| **合计** | **181** | **146** | **337** | **66** | **730** |

> **对账 (Reconciliation):**
> - Rule 1 (0.1) 学位项目总计 = 181 + 146 + 337 + 66 = **730**
> - Rule 3 (0.3) 学历级别求和 = **730**
> - Rule 4 (0.4) 矩阵单元格求和 = 730 (行和: UG Major 181 + UG Minor 146 + Grad Degree 337 + Grad Cert 66) = **730**
> - Rule 5 (Sections 1 & 2) 行数 = unique program URLs = **730**
> - ✅ 三个数字一致 (730 == 730 == 730)。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

> 本科由统一的 Office of Undergraduate Admissions (400 Lafayette St, NYC) 管理,所有申请者通过 Common Application 申请三个校区 (NY/Abu Dhabi/Shanghai)。NYC 校区 13 所本科学院授予本科项目;下面按 学院 → 学位级别 → 专业 列出全量 (共 181 个本科学位专业)。学院层级树见 0.2。NYU 多数本科学院不再细分 "系",因此本节采用 学院 → 学位级别 → 专业 的三层结构。

### 1.1 本科学院架构

13 所本科学院 (见 0.2 层级树)。最大的是 College of Arts & Science (CAS, 90+ areas of study)。

### 1.2 本科学位专业 — 按学院 > 学位级别 分组

<!-- ===== SECTION 1: UNDERGRADUATE ===== -->

#### College of Arts & Science (CAS)
##### BA  (69)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Africana Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/africana-studies-ba/ |
| 2 | American Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/american-studies-ba/ |
| 3 | Anthropology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/anthropology-ba/ |
| 4 | Anthropology and Classical Civilization | https://bulletins.nyu.edu/undergraduate/arts-science/programs/anthropology-classical-civilization-ba/ |
| 5 | Anthropology and Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/anthropology-linguistics-ba/ |
| 6 | Art History | https://bulletins.nyu.edu/undergraduate/arts-science/programs/art-history-ba/ |
| 7 | Asian/Pacific/American Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/asian-pacific-american-studies-ba/ |
| 8 | Biochemistry | https://bulletins.nyu.edu/undergraduate/arts-science/programs/biochemistry-ba/ |
| 9 | Biology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/biology-ba/ |
| 10 | Chemistry | https://bulletins.nyu.edu/undergraduate/arts-science/programs/chemistry-ba/ |
| 11 | Cinema Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/cinema-studies-ba/ |
| 12 | Classical Civilization | https://bulletins.nyu.edu/undergraduate/arts-science/programs/classical-civilization-ba/ |
| 13 | Classical Civilization and Hellenic Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/classical-civilization-hellenic-studies-ba/ |
| 14 | Classics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/classics-ba/ |
| 15 | Classics and Art History | https://bulletins.nyu.edu/undergraduate/arts-science/programs/classics-art-history-ba/ |
| 16 | Comparative Literature | https://bulletins.nyu.edu/undergraduate/arts-science/programs/comparative-literature-ba/ |
| 17 | Computer Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/computer-science-ba/ |
| 18 | Computer and Data Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/computer-data-science-ba/ |
| 19 | Data Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/data-science-ba/ |
| 20 | Data Science and Mathematics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/data-science-mathematics-ba/ |
| 21 | Dramatic Literature, Theatre History, and Cinema | https://bulletins.nyu.edu/undergraduate/arts-science/programs/dramatic-literature-theatre-history-cinema-ba/ |
| 22 | East Asian Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/east-asian-studies-ba/ |
| 23 | Economics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/economics-ba/ |
| 24 | Economics and Computer Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/economics-computer-science-ba/ |
| 25 | Economics and Mathematics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/economics-mathematics-ba/ |
| 26 | English and American Literature | https://bulletins.nyu.edu/undergraduate/arts-science/programs/english-american-literature-ba/ |
| 27 | Environmental Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/environmental-studies-ba/ |
| 28 | European and Mediterranean Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/european-mediterranean-studies-ba/ |
| 29 | French | https://bulletins.nyu.edu/undergraduate/arts-science/programs/french-ba/ |
| 30 | French and Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/french-linguistics-ba/ |
| 31 | Gender and Sexuality Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/gender-sexuality-studies-ba/ |
| 32 | German | https://bulletins.nyu.edu/undergraduate/arts-science/programs/german-ba/ |
| 33 | German and Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/german-linguistics-ba/ |
| 34 | Global Public Health and Anthropology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/global-public-health-anthropology-ba/ |
| 35 | Global Public Health and History | https://bulletins.nyu.edu/undergraduate/arts-science/programs/global-public-health-history-ba/ |
| 36 | Global Public Health and Sociology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/global-public-health-sociology-ba/ |
| 37 | Hebrew and Judaic Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/hebrew-judaic-studies-ba/ |
| 38 | Hellenic Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/hellenic-studies-ba/ |
| 39 | History | https://bulletins.nyu.edu/undergraduate/arts-science/programs/history-ba/ |
| 40 | International Relations | https://bulletins.nyu.edu/undergraduate/arts-science/programs/international-relations-ba/ |
| 41 | Italian | https://bulletins.nyu.edu/undergraduate/arts-science/programs/italian-ba/ |
| 42 | Italian and Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/italian-linguistics-ba/ |
| 43 | Journalism | https://bulletins.nyu.edu/undergraduate/arts-science/programs/journalism-ba/ |
| 44 | Language and Mind | https://bulletins.nyu.edu/undergraduate/arts-science/programs/language-mind-ba/ |
| 45 | Latin American and Caribbean Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/latin-american-caribbean-studies-ba/ |
| 46 | Latino Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/latino-studies-ba/ |
| 47 | Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/linguistics-ba/ |
| 48 | Mathematics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-ba/ |
| 49 | Mathematics and Computer Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-computer-science-ba/ |
| 50 | Medieval and Renaissance Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/medieval-renaissance-studies-ba/ |
| 51 | Middle Eastern Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/middle-eastern-studies-ba/ |
| 52 | Music | https://bulletins.nyu.edu/undergraduate/arts-science/programs/music-ba/ |
| 53 | Philosophy | https://bulletins.nyu.edu/undergraduate/arts-science/programs/philosophy-ba/ |
| 54 | Physics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-ba/ |
| 55 | Politics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/politics-ba/ |
| 56 | Psychology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/psychology-ba/ |
| 57 | Public Policy | https://bulletins.nyu.edu/undergraduate/arts-science/programs/public-policy-ba/ |
| 58 | Religious Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/religious-studies-ba/ |
| 59 | Romance Languages | https://bulletins.nyu.edu/undergraduate/arts-science/programs/romance-languages-ba/ |
| 60 | Russian and Slavic Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/russian-slavic-studies-ba/ |
| 61 | Social and Cultural Analysis | https://bulletins.nyu.edu/undergraduate/arts-science/programs/social-cultural-analysis-ba/ |
| 62 | Sociology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/sociology-ba/ |
| 63 | Spanish and Linguistics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/spanish-linguistics-ba/ |
| 64 | Spanish and Portuguese | https://bulletins.nyu.edu/undergraduate/arts-science/programs/spanish-portuguese-ba/ |
| 65 | Urban Design and Architecture Studies | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-design-architecture-studies-ba/ |
| 66 | Urban Studies and Anthropology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-studies-anthropology-ba/ |
| 67 | Urban Studies and History | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-studies-history-ba/ |
| 68 | Urban Studies and Social and Cultural Analysis | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-studies-social-cultural-analysis-ba/ |
| 69 | Urban Studies and Sociology | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-studies-sociology-ba/ |

##### BS  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Chemistry | https://bulletins.nyu.edu/undergraduate/arts-science/programs/chemistry-bs/ |
| 2 | Global Public Health and Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/global-public-health-science-bs/ |
| 3 | Neural Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/neural-science-bs/ |
| 4 | Physics | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-bs/ |

##### BS/BS  (12)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biology/Chemical and Biomolecular Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/biology-chemical-biomolecular-engineering-bs-bs/ |
| 2 | Chemistry/Chemical and Biomolecular Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/chemistry-chemical-biomolecular-engineering-bs-bs/ |
| 3 | Computer Science/Computer Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/computer-science-engineering-bs-bs/ |
| 4 | Computer Science/Electrical Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/computer-science-electrical-engineering-bs-bs/ |
| 5 | Mathematics/Civil Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-civil-engineering-bs-bs/ |
| 6 | Mathematics/Computer Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-computer-engineering-bs-bs/ |
| 7 | Mathematics/Electrical Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-electrical-engineering-bs-bs/ |
| 8 | Mathematics/Mechanical Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-mechanical-engineering-bs-bs/ |
| 9 | Physics/Civil Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-civil-engineering-bs-bs/ |
| 10 | Physics/Computer Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-computer-engineering-bs-bs/ |
| 11 | Physics/Electrical Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-electrical-engineering-bs-bs/ |
| 12 | Physics/Mechanical Engineering | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-mechanical-engineering-bs-bs/ |

##### BA/DDS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biology/Dentistry | https://bulletins.nyu.edu/undergraduate/arts-science/programs/biology-dentistry-ba-dds/ |

#### College of Dentistry
##### BS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Dental Hygiene | https://bulletins.nyu.edu/undergraduate/dentistry/programs/dental-hygiene-bachelor-science/ |

##### AAS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Dental Hygiene | https://bulletins.nyu.edu/undergraduate/dentistry/programs/dental-hygiene-associate-applied-science/ |

#### Gallatin School of Individualized Study
##### BA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Individualized Major | https://bulletins.nyu.edu/undergraduate/individualized-study/programs/individualized-major-ba/ |

#### Stern School of Business
##### BS  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Business | https://bulletins.nyu.edu/undergraduate/business/programs/business-bs/ |
| 2 | Business and Political Economy | https://bulletins.nyu.edu/undergraduate/business/programs/business-political-economy-bs/ |
| 3 | Business, Technology and Entrepreneurship | https://bulletins.nyu.edu/undergraduate/business/programs/business-technology-entrepreneurship-bs/ |

##### BS/MS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Business/Accounting | https://bulletins.nyu.edu/undergraduate/business/programs/accounting-bs-ms/ |

#### Liberal Studies
##### BA  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Global Liberal Studies | https://bulletins.nyu.edu/undergraduate/liberal-studies/programs/global-liberal-studies-ba/ |
| 2 | Global Public Health/Global Liberal Studies | https://bulletins.nyu.edu/undergraduate/liberal-studies/programs/global-liberal-studies-public-health-ba/ |

##### Core (non-degree)  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Liberal Studies Core | https://bulletins.nyu.edu/undergraduate/liberal-studies/programs/global-liberal-studies-core/ |

#### Rory Meyers College of Nursing
##### BS  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Nursing (BS) | https://bulletins.nyu.edu/undergraduate/nursing/programs/nursing-accelerated-15-month-bs/ |
| 2 | Nursing (BS) | https://bulletins.nyu.edu/undergraduate/nursing/programs/nursing-traditional-4-year-bs/ |
| 3 | Nursing/Global Public Health | https://bulletins.nyu.edu/undergraduate/nursing/programs/global-public-health-nursing-bs/ |

#### School of Professional Studies (SPS)
##### BA  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied General Studies | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/applied-general-studies-ba/ |
| 2 | Humanities | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/humanities-ba/ |
| 3 | Social Sciences | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/social-sciences-ba/ |

##### BS  (10)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Data Analytics and Visualization | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/applied-data-analytics-visualization-bs/ |
| 2 | Digital Communications and Media | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/digital-communications-media-bs/ |
| 3 | Healthcare Management | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/healthcare-management-bs/ |
| 4 | Hospitality, Travel and Tourism Management | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/hospitality-travel-tourism-management-bs/ |
| 5 | Information Systems and Technology | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/information-systems-technology-bs/ |
| 6 | Leadership and Management | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/leadership-management-bs/ |
| 7 | Marketing Analytics | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/marketing-analytics-bs/ |
| 8 | Real Estate | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/real-estate-bs/ |
| 9 | Real Estate and Urban Sustainability | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/real-estate-urban-sustainability-bs/ |
| 10 | Sport Management | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/sport-management-bs/ |

##### AAS  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Business | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/business-aas/ |
| 2 | Health Administration | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/health-administration-aas/ |
| 3 | Hospitality Management | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/hospitality-management-aas/ |
| 4 | Information Systems and Technology | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/information-systems-technology-aas/ |

##### AA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Liberal Arts | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/liberal-arts-aa/ |

#### Silver School of Social Work
##### BS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Global Public Health and Social Work | https://bulletins.nyu.edu/undergraduate/social-work/programs/global-public-health-social-work-bs/ |
| 2 | Social Work | https://bulletins.nyu.edu/undergraduate/social-work/programs/bachelor-science/ |

#### Steinhardt School of Culture, Education, and Human Development
##### BA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Education Studies | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/education-studies-ba/ |

##### BS  (27)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Psychology | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/applied-psychology-bs/ |
| 2 | Childhood Education/Childhood Special Education | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/childhood-education-childhood-special-education-bs/ |
| 3 | Communicative Sciences and Disorders | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/communicative-sciences-disorders-bs/ |
| 4 | Early Childhood Education/Early Childhood Special Education | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/early-childhood-education-special-bs/ |
| 5 | Educational Theatre | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/educational-theatre-bs/ |
| 6 | Global Public Health/Applied Psychology | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-public-health-applied-psychology-bs/ |
| 7 | Global Public Health/Communicative Sciences and Disorders | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-public-health-communicative-sciences-disorders-bs/ |
| 8 | Global Public Health/Food Studies | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-public-health-food-studies-bs/ |
| 9 | Global Public Health/Media, Culture, and Communication | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-public-health-media-culture-communication-bs/ |
| 10 | Global Public Health/Nutrition and Dietetics | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-public-health-nutrition-dietetics-bs/ |
| 11 | Health and Wellbeing Studies | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/health-wellbeing-studies-bs/ |
| 12 | Media, Culture, and Communication | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/media-culture-communication-bs/ |
| 13 | Music Business | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/music-business-bs/ |
| 14 | Nutrition and Food Studies | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/nutrition-food-studies-bs/ |
| 15 | Professional Studies | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/professional-studies-bs/ |
| 16 | Teaching Biology 7-12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-biology-7-12-bs/ |
| 17 | Teaching Chemistry 7-12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-chemistry-7-12-bs/ |
| 18 | Teaching Earth Science 7-12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-earth-science-7-12-bs/ |
| 19 | Teaching English 7–12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-english-712-bs/ |
| 20 | Teaching Mathematics 7–12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-mathematics-712-bs/ |
| 21 | Teaching Physics 7-12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-physics-7-12-bs/ |
| 22 | Teaching Social Studies 7–12 | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-social-studies-712-bs/ |
| 23 | Teaching a World Language 7-12: Chinese | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-world-language-7-12-chinese-bs/ |
| 24 | Teaching a World Language 7-12: French | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-world-language-7-12-french-bs/ |
| 25 | Teaching a World Language 7-12: Italian | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-world-language-7-12-italian-bs/ |
| 26 | Teaching a World Language 7-12: Japanese | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-world-language-7-12-japanese-bs/ |
| 27 | Teaching a World Language 7-12: Spanish | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teaching-world-language-7-12-spanish-bs/ |

##### BFA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Studio Art | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/studio-art-bfa/ |

##### BM  (6)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Instrumental Performance | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/instrumental-performance-bm/ |
| 2 | Music Business | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/music-business-bm/ |
| 3 | Music Technology | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/music-technology-bm/ |
| 4 | Music Theory and Composition | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/music-theory-composition-bm/ |
| 5 | Piano Performance | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/piano-performance-bm/ |
| 6 | Vocal Performance | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/vocal-performance-bm/ |

##### BFA/MS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Studio Art/Integrated Design and Media | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/studio-art-integrated-design-media-bfa-ms/ |

#### Tandon School of Engineering
##### BS  (14)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Physics | https://bulletins.nyu.edu/undergraduate/engineering/programs/applied-physics-bs/ |
| 2 | Biomolecular Science | https://bulletins.nyu.edu/undergraduate/engineering/programs/biomolecular-science-bs/ |
| 3 | Business and Technology Management | https://bulletins.nyu.edu/undergraduate/engineering/programs/business-technology-management-bs/ |
| 4 | Chemical and Biomolecular Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/chemical-biomolecular-engineering-bs/ |
| 5 | Civil Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/civil-engineering-bs/ |
| 6 | Computer Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-engineering-bs/ |
| 7 | Computer Science | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-science-bs/ |
| 8 | Electrical Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/electrical-engineering-bs/ |
| 9 | Electrical and Computer Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/electrical-computer-engineering-bs/ |
| 10 | Environmental Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/environmental-engineering-bs/ |
| 11 | Integrated Design and Media | https://bulletins.nyu.edu/undergraduate/engineering/programs/integrated-design-media-bs/ |
| 12 | Mathematics | https://bulletins.nyu.edu/undergraduate/engineering/programs/mathematics-bs/ |
| 13 | Mathematics and Physics | https://bulletins.nyu.edu/undergraduate/engineering/programs/mathematics-physics-bs/ |
| 14 | Mechanical Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/mechanical-engineering-bs/ |

##### BS/MS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Computer Science/Management of Technology | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-science-management-technology-bs-ms/ |

#### Tisch School of the Arts
##### BA  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Cinema Studies | https://bulletins.nyu.edu/undergraduate/arts/programs/cinema-studies-ba/ |
| 2 | Performance Studies | https://bulletins.nyu.edu/undergraduate/arts/programs/performance-studies-ba/ |

##### BFA  (9)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Collaborative Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/collaborative-arts-bfa/ |
| 2 | Dance | https://bulletins.nyu.edu/undergraduate/arts/programs/dance-bfa/ |
| 3 | Dramatic Writing | https://bulletins.nyu.edu/undergraduate/arts/programs/dramatic-writing-bfa/ |
| 4 | Film and Television | https://bulletins.nyu.edu/undergraduate/arts/programs/film-television-bfa/ |
| 5 | Game Design | https://bulletins.nyu.edu/undergraduate/arts/programs/game-design-bfa/ |
| 6 | Interactive Media Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/interactive-media-arts-bfa/ |
| 7 | Photography and Imaging | https://bulletins.nyu.edu/undergraduate/arts/programs/photography-imaging-bfa/ |
| 8 | Recorded Music | https://bulletins.nyu.edu/undergraduate/arts/programs/recorded-music-bfa/ |
| 9 | Theatre | https://bulletins.nyu.edu/undergraduate/arts/programs/theatre-bfa/ |


### 1.4 本科辅修 (Minors) — 全量列表

| # | Minor | 学院 (URL home) | URL |
|---|-------|------------------|-----|
| 1 | Applied Theatre | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/applied-theatre-minor/ |
| 2 | Art and Public Policy | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/art-public-policy-minor/ |
| 3 | Asian Film and Media | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/asian-film-media-minor/ |
| 4 | Cinema Studies | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/cinema-studies-minor/ |
| 5 | Dance | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/dance-minor/ |
| 6 | Documentary | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/documentary-minor/ |
| 7 | Dramaturgy | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/dramaturgy-minor/ |
| 8 | Film | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/film-minor/ |
| 9 | Game Design | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/game-design-minor/ |
| 10 | Interactive Media Arts | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/interactive-media-arts-minor/ |
| 11 | Performance Studies | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/performance-studies-minor/ |
| 12 | Producing | Tisch School of the Arts | https://bulletins.nyu.edu/undergraduate/arts/programs/producing-minor/ |
| 13 | Advanced Mathematical Methods (for Students in Stern) | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/advanced-mathematical-methods-minor/ |
| 14 | Africana Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/africana-studies-minor/ |
| 15 | American Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/american-studies-minor/ |
| 16 | Ancient Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/ancient-studies-minor/ |
| 17 | Animal Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/animal-studies-minor/ |
| 18 | Anthropology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/anthropology-minor/ |
| 19 | Archaeology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/archaeology-minor/ |
| 20 | Art History | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/art-history-minor/ |
| 21 | Asian Film and Media | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/asian-film-media-minor/ |
| 22 | Asian/Pacific/American Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/asian-pacific-american-studies-minor/ |
| 23 | Astronomy | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/astronomy-minor/ |
| 24 | Broadcast and Multimedia Journalism | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/broadcast-multimedia-journalism-minor/ |
| 25 | Business Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/business-studies-minor/ |
| 26 | Chemistry | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/chemistry-minor/ |
| 27 | Child and Adolescent Mental Health Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/child-adolescent-mental-health-studies-minor/ |
| 28 | Chinese | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/chinese-minor/ |
| 29 | Cinema Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/cinema-studies-minor/ |
| 30 | Classical Civilization | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/classical-civilization-minor/ |
| 31 | Comparative Literature | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/comparative-literature-minor/ |
| 32 | Computer Science | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/computer-science-minor/ |
| 33 | Creative Writing | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/creative-writing-minor/ |
| 34 | Creative Writing in Spanish | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/creative-writing-spanish-minor/ |
| 35 | Data Science | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/data-science-minor/ |
| 36 | Dramatic Literature, Theatre History, and Cinema | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/dramatic-literature-theatre-history-cinema-minor/ |
| 37 | East Asian Civilization | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/east-asian-civilization-minor/ |
| 38 | Economics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/economics-minor/ |
| 39 | English and American Literature | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/english-american-literature-minor/ |
| 40 | Environmental Biology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/environmental-biology-minor/ |
| 41 | Environmental Humanities | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/environmental-humanities-minor/ |
| 42 | Environmental Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/environmental-studies-minor/ |
| 43 | European and Mediterranean Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/european-mediterranean-studies-minor/ |
| 44 | Francophone Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/francophone-studies-minor/ |
| 45 | French | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/french-minor/ |
| 46 | French Studies in English Translation | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/french-studies-english-translation-minor/ |
| 47 | Gender and Sexuality Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/gender-sexuality-studies-minor/ |
| 48 | Genetics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/genetics-minor/ |
| 49 | Genomics and Bioinformatics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/genomics-bioinformatics-minor/ |
| 50 | German | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/german-minor/ |
| 51 | Hebrew and Judaic Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/hebrew-judaic-studies-minor/ |
| 52 | Hellenic Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/hellenic-studies-minor/ |
| 53 | History | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/history-minor/ |
| 54 | Irish Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/irish-studies-minor/ |
| 55 | Italian | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/italian-minor/ |
| 56 | Japanese | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/japanese-minor/ |
| 57 | Korean | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/korean-minor/ |
| 58 | Latin American and Caribbean Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/latin-american-caribbean-studies-minor/ |
| 59 | Latin and Ancient Greek | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/latin-ancient-greek-minor/ |
| 60 | Latino Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/latino-studies-minor/ |
| 61 | Law and Society | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/law-society-minor/ |
| 62 | Linguistics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/linguistics-minor/ |
| 63 | Literature in Translation | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/literature-translation-minor/ |
| 64 | Mathematics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-minor/ |
| 65 | Mathematics and Computer Science | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/mathematics-computer-science-minor/ |
| 66 | Medical Humanities | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/medical-humanities-minor/ |
| 67 | Medieval and Renaissance Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/medieval-renaissance-studies-minor/ |
| 68 | Middle Eastern Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/middle-eastern-studies-minor/ |
| 69 | Molecular and Cell Biology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/molecular-cell-biology-minor/ |
| 70 | Music | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/music-minor/ |
| 71 | Native American and Indigenous Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/native-american-indigenous-studies-minor/ |
| 72 | Philosophy | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/philosophy-minor/ |
| 73 | Physics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/physics-minor/ |
| 74 | Politics | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/politics-minor/ |
| 75 | Portuguese | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/portuguese-minor/ |
| 76 | Print and Online Journalism | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/print-online-journalism-minor/ |
| 77 | Psychology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/psychology-minor/ |
| 78 | Public Policy | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/public-policy-minor/ |
| 79 | Religious Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/religious-studies-minor/ |
| 80 | Russian and Slavic Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/russian-slavic-studies-minor/ |
| 81 | Science and Society | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/science-society-minor/ |
| 82 | Social and Cultural Analysis | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/social-cultural-analysis-minor/ |
| 83 | Sociology | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/sociology-minor/ |
| 84 | South Asian Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/south-asian-studies-minor/ |
| 85 | Spanish | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/spanish-minor/ |
| 86 | Urban Design and Architecture Studies | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/urban-design-architecture-studies-minor/ |
| 87 | Web Programming and Applications | College of Arts & Science | https://bulletins.nyu.edu/undergraduate/arts-science/programs/web-programming-applications-minor/ |
| 88 | Advanced Mathematical Methods | Stern School of Business | https://bulletins.nyu.edu/undergraduate/business/programs/advanced-mathematical-methods-minor/ |
| 89 | Business of Entertainment, Media and Technology | Stern School of Business | https://bulletins.nyu.edu/undergraduate/business/programs/business-entertainment-media-technology-minor/ |
| 90 | American Sign Language | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/american-sign-language-minor/ |
| 91 | Child Development and Social Intervention | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/child-development-social-intervention-minor/ |
| 92 | Communicative Sciences and Disorders | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/communicative-sciences-disorders-minor/ |
| 93 | Computer Science Education | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/computer-science-education-minor/ |
| 94 | Data and Education | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/data-education-minor/ |
| 95 | Digital Art and Design | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/digital-art-design-minor/ |
| 96 | Digital Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/digital-studies-minor/ |
| 97 | Disability Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/disability-studies-minor/ |
| 98 | Educational Theatre | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/educational-theatre-minor/ |
| 99 | Fashion Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/fashion-studies-minor/ |
| 100 | Food Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/food-studies-minor/ |
| 101 | Global and Urban Education Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/global-urban-education-studies-minor/ |
| 102 | Health and Wellbeing Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/health-wellbeing-studies-minor/ |
| 103 | Media, Culture, and Communication | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/media-culture-communication-minor/ |
| 104 | Music in Global Communities | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/music-global-communities-minor/ |
| 105 | Nutrition | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/nutrition-minor/ |
| 106 | Peace and Conflict Studies | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/peace-conflict-studies-minor/ |
| 107 | Studio Art | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/studio-art-minor/ |
| 108 | Teacher Education | Steinhardt School of Culture, Education, and Human Development | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/teacher-education-minor/ |
| 109 | Aerospace Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/aerospace-engineering-minor/ |
| 110 | Applied Physics | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/applied-physics-minor/ |
| 111 | Biomolecular Science | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/biomolecular-science-minor/ |
| 112 | Computer Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-engineering-minor/ |
| 113 | Computer Science | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-science-minor/ |
| 114 | Construction Management | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/construction-management-minor/ |
| 115 | Cybersecurity | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/cybersecurity-minor/ |
| 116 | Electrical Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/electrical-engineering-minor/ |
| 117 | Engineering Innovation | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/engineering-innovation-minor/ |
| 118 | English for Tandon Students | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/english-minor-tandon-students/ |
| 119 | Environmental Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/environmental-engineering-minor/ |
| 120 | Feminism and Science, Technology, Engineering and Math (FSTEM) | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/feminism-science-technology-engineering-math-fstem-minor/ |
| 121 | Finance | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/finance-minor/ |
| 122 | Game Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/game-engineering-minor/ |
| 123 | Integrated Design and Media | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/integrated-design-media-minor/ |
| 124 | Management | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/management-minor/ |
| 125 | Mathematics | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/mathematics-minor/ |
| 126 | Mechanical Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/mechanical-engineering-minor/ |
| 127 | Quantum Technology | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/quantum-technology-minor/ |
| 128 | Robotics | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/robotics-minor/ |
| 129 | Science and Technology Studies | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/science-technology-studies-minor/ |
| 130 | Structural Engineering | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/structural-engineering-minor/ |
| 131 | Sustainable Urban Environments | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/sustainable-urban-environments-minor/ |
| 132 | Technology, Management and Design | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/technology-management-design-minor/ |
| 133 | Transportation | Tandon School of Engineering | https://bulletins.nyu.edu/undergraduate/engineering/programs/transportation-minor/ |
| 134 | Bioethics | School of Global Public Health | https://bulletins.nyu.edu/undergraduate/global-public-health/programs/bioethics-minor/ |
| 135 | Public Health | School of Global Public Health | https://bulletins.nyu.edu/undergraduate/global-public-health/programs/public-health-minor/ |
| 136 | Psychoanalysis and the Humanities | Gallatin School of Individualized Study | https://bulletins.nyu.edu/undergraduate/individualized-study/programs/psychoanalysis-humanities-minor/ |
| 137 | Global Liberal Studies | Liberal Studies | https://bulletins.nyu.edu/undergraduate/liberal-studies/programs/global-liberal-studies-minor/ |
| 138 | Translation Studies | Liberal Studies | https://bulletins.nyu.edu/undergraduate/liberal-studies/programs/translation-studies-minor/ |
| 139 | Real Estate Development | School of Professional Studies | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/real-estate-development-minor/ |
| 140 | Sport Management | School of Professional Studies | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/sport-management-minor/ |
| 141 | Travel, Hospitality, and Tourism Management | School of Professional Studies | https://bulletins.nyu.edu/undergraduate/professional-studies/programs/travel-hospitality-tourism-management-minor/ |
| 142 | Public Policy and Management | Wagner School of Public Service | https://bulletins.nyu.edu/undergraduate/public-service/programs/public-policy-management-minor/ |
| 143 | Social Entrepreneurship | Wagner School of Public Service | https://bulletins.nyu.edu/undergraduate/public-service/programs/social-entrepreneurship-minor/ |
| 144 | Inequality Studies | Silver School of Social Work | https://bulletins.nyu.edu/undergraduate/social-work/programs/inequality-studies-minor/ |
| 145 | Leadership, Spirituality, and Social Innovation | Silver School of Social Work | https://bulletins.nyu.edu/undergraduate/social-work/programs/leadership-spirituality-social-innovation-minor/ |
| 146 | Social Work | Silver School of Social Work | https://bulletins.nyu.edu/undergraduate/social-work/programs/social-work-minor/ |



### 1.3 跨学院 / 双学位本科项目

NYU 设有多个正式双学位项目 (已在 1.2 各学院下以其双学位标签列出,如 BS/BS = CAS+Tandon、BA/DDS = CAS+Dentistry、BFA/MS = Steinhardt+Tandon IDM、BS/MS = Stern/Tandon + 本院)。代表性的跨学院双学位:

| # | 双学位项目 | 涉及学院 | URL |
|---|-----------|---------|-----|
| 1 | BS/BS (CAS + Tandon 双 BS) | CAS + Tandon | https://bulletins.nyu.edu/undergraduate/arts-science/programs/dual-degree-engineering-bs-bs/ |
| 2 | BA/DDS (CAS + Dentistry 7 年制) | CAS + Dentistry | https://bulletins.nyu.edu/undergraduate/arts-science/programs/ |
| 3 | BFA/MS Studio Art + Integrated Design & Media | Steinhardt + Tandon | https://bulletins.nyu.edu/undergraduate/culture-education-human-development/programs/studio-art-integrated-design-media-bfa-ms/ |
| 4 | BS/MS Computer Science + Management of Technology | Tandon + SPS | https://bulletins.nyu.edu/undergraduate/engineering/programs/computer-science-management-technology-bs-ms/ |

### 1.5 通识 / 核心课程要求

NYU 没有全校统一的 "Core Curriculum";各学院自有核心要求。例如:
- **CAS**: College Core Curriculum (Foundations of Scientific Inquiry / Contemporary Culture / Texts & Ideas),由 CAS 学生必修。
- **Liberal Studies**: LS Core (两年制小班核心课程,完成后转入其他学院专业)。
- **Stern**: Business Core + Liberal Arts Core。
- **Tandon**: Engineering Core (数学、科学、工程基础、EG-UY 1004 Engineering & Design)。
- **Tisch/Steinhardt**: 各专业自有工作室/理论核心。
- 全校均要求完成 **NYU 无障碍性要求 (Cultures & Contexts / Writing the Essay 等)** 及学院规定的写作要求。
来源: https://bulletins.nyu.edu/undergraduate/arts-science/academic-policies/

### 1.6 课程编号 → 专业 快速查找

NYU 不采用 MIT 式 "Course N" 编号系统。各学院有独立课程前缀 (例如 CAS 用 subject code 如 MATH-UA、ECON-UA;Tandon 用 CS-UY、MA-UY;Steinhardt 用 MPAPA-UE 等),专业本身以名称 + 学位标签标识,不分配全局编号。本项目文档以 bulletins program URL slug 作为唯一标识。

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by School > Department > Degree Level
(Rule 5 leaf enumeration — see `#### School / ##### Department / ###### Degree Level` tables immediately below for the exhaustive list.)

#### Graduate School of Arts and Science (GSAS)
##### MA  (41)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Africana Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/africana-studies-ma/ |
| 2 | American Journalism | https://bulletins.nyu.edu/graduate/arts-science/programs/american-journalism-ma/ |
| 3 | Animal Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/animal-studies-ma/ |
| 4 | Archives and Public History | https://bulletins.nyu.edu/graduate/arts-science/programs/archives-public-history-ma/ |
| 5 | Cinema Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/cinema-studies-ma/ |
| 6 | Classics | https://bulletins.nyu.edu/graduate/arts-science/programs/classics-ma/ |
| 7 | Comparative Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/comparative-literature-ma/ |
| 8 | East Asian Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/east-asian-studies-ma/ |
| 9 | Economics | https://bulletins.nyu.edu/graduate/arts-science/programs/economics-ma/ |
| 10 | English and American Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/english-ma/ |
| 11 | European and Mediterranean Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/european-mediterranean-studies-ma/ |
| 12 | French Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/french-literature-ma/ |
| 13 | French Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/french-studies-ma/ |
| 14 | German Thought and Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/german-thought-literature-ma/ |
| 15 | Hebrew and Judaic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/hebrew-judaic-studies-ma/ |
| 16 | Historical and Sustainable Architecture | https://bulletins.nyu.edu/graduate/arts-science/programs/historical-sustainable-architecture-ma/ |
| 17 | History | https://bulletins.nyu.edu/graduate/arts-science/programs/history-ma/ |
| 18 | History of Art and Archaeology | https://bulletins.nyu.edu/graduate/arts-science/programs/history-art-archaeology-ma/ |
| 19 | Industrial/Organizational Psychology | https://bulletins.nyu.edu/graduate/arts-science/programs/industrial-organizational-psychology-ma/ |
| 20 | Interdisciplinary Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/interdisciplinary-studies-ma/ |
| 21 | International Relations | https://bulletins.nyu.edu/graduate/arts-science/programs/international-relations-ma/ |
| 22 | Irish and Irish American Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/irish-american-studies-ma/ |
| 23 | Italian Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/italian-studies-ma/ |
| 24 | Journalism | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-ma/ |
| 25 | Journalism and Africana Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-africana-studies-ma/ |
| 26 | Journalism and East Asian Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-east-asian-studies-ma/ |
| 27 | Journalism and European and Mediterranean Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-european-mediterranean-studies-ma/ |
| 28 | Journalism and French Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-french-studies-ma/ |
| 29 | Journalism and International Relations | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-international-relations-ma/ |
| 30 | Journalism and Latin American and Caribbean Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-latin-american-caribbean-studies-ma/ |
| 31 | Journalism and Near Eastern Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-near-eastern-studies-ma/ |
| 32 | Journalism and Russian and Slavic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/journalism-russian-slavic-studies-ma/ |
| 33 | Latin American and Caribbean Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/latin-american-caribbean-studies-ma/ |
| 34 | Museum Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/museum-studies-ma/ |
| 35 | Near Eastern Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/near-eastern-studies-ma/ |
| 36 | Performance Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/performance-studies-ma/ |
| 37 | Politics | https://bulletins.nyu.edu/graduate/arts-science/programs/politics-ma/ |
| 38 | Psychology | https://bulletins.nyu.edu/graduate/arts-science/programs/psychology-ma/ |
| 39 | Religious Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/religious-studies-ma/ |
| 40 | Russian and Slavic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/russian-slavic-studies-ma/ |
| 41 | Social and Cultural Analysis | https://bulletins.nyu.edu/graduate/arts-science/programs/social-cultural-analysis-ma/ |

##### MS  (14)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biology | https://bulletins.nyu.edu/graduate/arts-science/programs/biology-ms/ |
| 2 | Biomedical Informatics | https://bulletins.nyu.edu/graduate/arts-science/programs/biomedical-informatics-ms/ |
| 3 | Chemistry | https://bulletins.nyu.edu/graduate/arts-science/programs/chemistry-ms/ |
| 4 | Computer Science Courant | https://bulletins.nyu.edu/graduate/arts-science/programs/computer-science-courant-ms/ |
| 5 | Computing, Entrepreneurship and Innovation | https://bulletins.nyu.edu/graduate/arts-science/programs/computing-entrepreneurship-innovation-ms/ |
| 6 | Data Science | https://bulletins.nyu.edu/graduate/arts-science/programs/data-science-ms/ |
| 7 | Environmental Health Science | https://bulletins.nyu.edu/graduate/arts-science/programs/environmental-health-science-ms/ |
| 8 | Human Skeletal Biology | https://bulletins.nyu.edu/graduate/arts-science/programs/human-skeletal-biology-ms/ |
| 9 | Information Systems | https://bulletins.nyu.edu/graduate/arts-science/programs/information-systems-ms/ |
| 10 | Mathematics | https://bulletins.nyu.edu/graduate/arts-science/programs/mathematics-ms/ |
| 11 | Mathematics in Finance | https://bulletins.nyu.edu/graduate/arts-science/programs/mathematics-finance-ms/ |
| 12 | Physics | https://bulletins.nyu.edu/graduate/arts-science/programs/physics-ms/ |
| 13 | Quantitative Economics | https://bulletins.nyu.edu/graduate/arts-science/programs/quantitative-economics-ms/ |
| 14 | Scientific Computing | https://bulletins.nyu.edu/graduate/arts-science/programs/scientific-computing-ms/ |

##### MFA  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Creative Writing | https://bulletins.nyu.edu/graduate/arts-science/programs/creative-writing-mfa/ |
| 2 | Creative Writing in Spanish | https://bulletins.nyu.edu/graduate/arts-science/programs/creative-writing-spanish-mfa/ |
| 3 | Literary Reportage | https://bulletins.nyu.edu/graduate/arts-science/programs/literary-reportage-mfa/ |

##### MS/MA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Conservation of Historic and Artistic Works/History of Art and Archaeology | https://bulletins.nyu.edu/graduate/arts-science/programs/conservation-historic-artistic-works-history-art-archaeology-ms-ma/ |

##### PhD  (41)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | American Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/american-studies-phd/ |
| 2 | Anthropology | https://bulletins.nyu.edu/graduate/arts-science/programs/anthropology-phd/ |
| 3 | Atmosphere and Ocean Science and Mathematics | https://bulletins.nyu.edu/graduate/arts-science/programs/atmosphere-ocean-science-phd/ |
| 4 | Biology | https://bulletins.nyu.edu/graduate/arts-science/programs/biology-phd/ |
| 5 | Biomedical Sciences | https://bulletins.nyu.edu/graduate/arts-science/programs/biomedical-sciences-phd/ |
| 6 | Chemistry | https://bulletins.nyu.edu/graduate/arts-science/programs/chemistry-phd/ |
| 7 | Cinema Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/cinema-studies-phd/ |
| 8 | Classics | https://bulletins.nyu.edu/graduate/arts-science/programs/classics-phd/ |
| 9 | Cognition and Perception | https://bulletins.nyu.edu/graduate/arts-science/programs/cognition-perception-phd/ |
| 10 | Comparative Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/comparative-literature-phd/ |
| 11 | Computer Science | https://bulletins.nyu.edu/graduate/arts-science/programs/computer-science-phd/ |
| 12 | Data Science | https://bulletins.nyu.edu/graduate/arts-science/programs/data-science-phd/ |
| 13 | East Asian Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/east-asian-studies-phd/ |
| 14 | Economics | https://bulletins.nyu.edu/graduate/arts-science/programs/economics-phd/ |
| 15 | English and American Literature | https://bulletins.nyu.edu/graduate/arts-science/programs/english-phd/ |
| 16 | Environmental Health Science | https://bulletins.nyu.edu/graduate/arts-science/programs/environmental-health-science-phd/ |
| 17 | Environmental Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/environmental-studies-phd/ |
| 18 | French | https://bulletins.nyu.edu/graduate/arts-science/programs/french-phd/ |
| 19 | French Studies and Anthropology | https://bulletins.nyu.edu/graduate/arts-science/programs/french-studies-anthropology-phd/ |
| 20 | French Studies and French | https://bulletins.nyu.edu/graduate/arts-science/programs/french-studies-french-phd/ |
| 21 | French Studies and History | https://bulletins.nyu.edu/graduate/arts-science/programs/french-studies-history-phd/ |
| 22 | German | https://bulletins.nyu.edu/graduate/arts-science/programs/german-phd/ |
| 23 | Hebrew and Judaic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/hebrew-judaic-studies-phd/ |
| 24 | Hebrew and Judaic Studies and History | https://bulletins.nyu.edu/graduate/arts-science/programs/hebrew-judaic-studies-history-phd/ |
| 25 | History | https://bulletins.nyu.edu/graduate/arts-science/programs/history-phd/ |
| 26 | History and Middle Eastern and Islamic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/history-middle-eastern-studies-phd/ |
| 27 | History of Art and Archaeology | https://bulletins.nyu.edu/graduate/arts-science/programs/history-art-archaeology-phd/ |
| 28 | Italian Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/italian-studies-phd/ |
| 29 | Linguistics | https://bulletins.nyu.edu/graduate/arts-science/programs/linguistics-phd/ |
| 30 | Mathematics | https://bulletins.nyu.edu/graduate/arts-science/programs/mathematics-phd/ |
| 31 | Middle Eastern and Islamic Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/middle-eastern-islamic-studies-phd/ |
| 32 | Music | https://bulletins.nyu.edu/graduate/arts-science/programs/music-phd/ |
| 33 | Neural Science | https://bulletins.nyu.edu/graduate/arts-science/programs/neural-science-phd/ |
| 34 | Performance Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/performance-studies-phd/ |
| 35 | Philosophy | https://bulletins.nyu.edu/graduate/arts-science/programs/philosophy-phd/ |
| 36 | Physics | https://bulletins.nyu.edu/graduate/arts-science/programs/physics-phd/ |
| 37 | Politics | https://bulletins.nyu.edu/graduate/arts-science/programs/politics-phd/ |
| 38 | Social Psychology | https://bulletins.nyu.edu/graduate/arts-science/programs/social-psychology-phd/ |
| 39 | Sociology | https://bulletins.nyu.edu/graduate/arts-science/programs/sociology-phd/ |
| 40 | Spanish | https://bulletins.nyu.edu/graduate/arts-science/programs/spanish-phd/ |
| 41 | The Ancient World | https://bulletins.nyu.edu/graduate/arts-science/programs/ancient-world-phd/ |

##### Advanced Certificate  (15)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Economic Analysis | https://bulletins.nyu.edu/graduate/arts-science/programs/applied-economic-analysis-advanced-certificate/ |
| 2 | Archives | https://bulletins.nyu.edu/graduate/arts-science/programs/archives-advanced-certificate/ |
| 3 | Comparative Approaches to the Literatures of Africa, the Middle East, and the Global South | https://bulletins.nyu.edu/graduate/arts-science/programs/comparative-approaches-literatures-africa-middle-east-global-south-advanced-certificate/ |
| 4 | Creative Writing in Spanish | https://bulletins.nyu.edu/graduate/arts-science/programs/creative-writing-spanish-advanced-certificate/ |
| 5 | Culture and Media | https://bulletins.nyu.edu/graduate/arts-science/programs/culture-media-advanced-certificate/ |
| 6 | Curatorial Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/curatorial-studies-advanced-certificate/ |
| 7 | Digital Humanities | https://bulletins.nyu.edu/graduate/arts-science/programs/digital-humanities-advanced-certificate/ |
| 8 | Experimental Writing | https://bulletins.nyu.edu/graduate/arts-science/programs/experimental-writing-advanced-certificate/ |
| 9 | Financial Mathematics | https://bulletins.nyu.edu/graduate/arts-science/programs/financial-mathematics-advanced-certificate/ |
| 10 | Management and Leadership of Public Service Organizations | https://bulletins.nyu.edu/graduate/arts-science/programs/management-leadership-public-service-organizations-advanced-certificate/ |
| 11 | Museum Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/museum-studies-advanced-certificate/ |
| 12 | Poetics and Theory | https://bulletins.nyu.edu/graduate/arts-science/programs/poetics-theory-advanced-certificate/ |
| 13 | Public History | https://bulletins.nyu.edu/graduate/arts-science/programs/public-history-advanced-certificate/ |
| 14 | Public Humanities | https://bulletins.nyu.edu/graduate/arts-science/programs/public-humanities-advanced-certificate/ |
| 15 | Social Data Science | https://bulletins.nyu.edu/graduate/arts-science/programs/social-data-science-advanced-certificate/ |

##### Advanced Certificate of Achievement  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | French Studies | https://bulletins.nyu.edu/graduate/arts-science/programs/french-studies-advanced-certificate-achievement/ |

#### Tandon School of Engineering
##### MS  (25)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Quantum Science and Technology | https://bulletins.nyu.edu/graduate/engineering/programs/applied-quantum-science-technology-ms/ |
| 2 | Bioinformatics | https://bulletins.nyu.edu/graduate/engineering/programs/bioinformatics-online-ms/ |
| 3 | Biomedical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/biomedical-engineering-ms/ |
| 4 | Biotechnology | https://bulletins.nyu.edu/graduate/engineering/programs/biotechnology-ms/ |
| 5 | Biotechnology and Entrepreneurship | https://bulletins.nyu.edu/graduate/engineering/programs/biotechnology-entrepreneurship-ms/ |
| 6 | Chemical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/chemical-engineering-ms/ |
| 7 | Civil Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/civil-engineering-ms/ |
| 8 | Computer Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/computer-engineering-ms/ |
| 9 | Computer Science Tandon | https://bulletins.nyu.edu/graduate/engineering/programs/computer-science-tandon-ms/ |
| 10 | Construction Management | https://bulletins.nyu.edu/graduate/engineering/programs/construction-management-ms/ |
| 11 | Cybersecurity | https://bulletins.nyu.edu/graduate/engineering/programs/cybersecurity-ms/ |
| 12 | Electrical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/electrical-engineering-ms/ |
| 13 | Emerging Technologies | https://bulletins.nyu.edu/graduate/engineering/programs/emerging-technologies-ms/ |
| 14 | Environmental Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/environmental-engineering-ms/ |
| 15 | Environmental Science | https://bulletins.nyu.edu/graduate/engineering/programs/environmental-science-ms/ |
| 16 | Financial Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/financial-engineering-ms/ |
| 17 | Industrial Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/industrial-engineering-ms/ |
| 18 | Integrated Design and Media | https://bulletins.nyu.edu/graduate/engineering/programs/integrated-design-media-ms/ |
| 19 | Management of Technology | https://bulletins.nyu.edu/graduate/engineering/programs/management-technology-ms/ |
| 20 | Mathematical Sciences | https://bulletins.nyu.edu/graduate/engineering/programs/mathematical-sciences-ms/ |
| 21 | Mechanical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/mechanical-engineering-ms/ |
| 22 | Mechatronics and Robotics | https://bulletins.nyu.edu/graduate/engineering/programs/mechatronics-robotics-ms/ |
| 23 | Transportation Systems | https://bulletins.nyu.edu/graduate/engineering/programs/transportation-systems-ms/ |
| 24 | Urban Data Science | https://bulletins.nyu.edu/graduate/engineering/programs/urban-data-science-ms/ |
| 25 | Urban Infrastructure Systems | https://bulletins.nyu.edu/graduate/engineering/programs/urban-infrastructure-systems-ms/ |

##### PhD  (8)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biomedical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/biomedical-engineering-phd/ |
| 2 | Chemical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/chemical-engineering-phd/ |
| 3 | Civil Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/civil-engineering-phd/ |
| 4 | Electrical and Computer Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/electrical-computer-engineering-phd/ |
| 5 | Human-Centered Technology, Innovation & Design | https://bulletins.nyu.edu/graduate/engineering/programs/human-centered-technology-innovation-design-phd/ |
| 6 | Mechanical Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/mechanical-engineering-phd/ |
| 7 | Transportation Systems | https://bulletins.nyu.edu/graduate/engineering/programs/transportation-systems-phd/ |
| 8 | Urban Systems | https://bulletins.nyu.edu/graduate/engineering/programs/urban-systems-phd/ |

##### Advanced Certificate  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Construction Management | https://bulletins.nyu.edu/graduate/engineering/programs/construction-management-advanced-certificate/ |
| 2 | Executive Construction Management | https://bulletins.nyu.edu/graduate/engineering/programs/executive-construction-management-advanced-certificate/ |
| 3 | Traffic Engineering | https://bulletins.nyu.edu/graduate/engineering/programs/traffic-engineering-advanced-certificate/ |

#### Stern School of Business
##### MS  (9)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Accounting | https://bulletins.nyu.edu/graduate/business/programs/accounting-ms/ |
| 2 | Business Analytics and AI | https://bulletins.nyu.edu/graduate/business/programs/business-analytics-ai-ms/ |
| 3 | Data Analytics and Business Computing | https://bulletins.nyu.edu/graduate/business/programs/data-analytics-business-computing-ms/ |
| 4 | Fintech | https://bulletins.nyu.edu/graduate/business/programs/fintech-ms/ |
| 5 | Global Finance | https://bulletins.nyu.edu/graduate/business/programs/global-finance-ms/ |
| 6 | Management | https://bulletins.nyu.edu/graduate/business/programs/management-ms/ |
| 7 | Marketing and Retail Science | https://bulletins.nyu.edu/graduate/business/programs/marketing-retail-science-ms/ |
| 8 | Organization Management and Strategy | https://bulletins.nyu.edu/graduate/business/programs/organization-management-strategy-ms/ |
| 9 | Quantitative Finance | https://bulletins.nyu.edu/graduate/business/programs/quantitative-finance-ms/ |

##### MBA  (6)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | General Management | https://bulletins.nyu.edu/graduate/business/programs/general-management-mba/ |
| 2 | General Management for Executives | https://bulletins.nyu.edu/graduate/business/programs/general-management-executives-mba/ |
| 3 | Global Executive MBA | https://bulletins.nyu.edu/graduate/business/programs/global-executive-mba/ |
| 4 | Luxury and Retail | https://bulletins.nyu.edu/graduate/business/programs/luxury-retail-mba/ |
| 5 | Stern at NYU Abu Dhabi | https://bulletins.nyu.edu/graduate/business/programs/stern-nyu-abu-dhabi-mba/ |
| 6 | Technology and Entrepreneurship | https://bulletins.nyu.edu/graduate/business/programs/technology-entrepreneurship-mba/ |

##### PhD  (8)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Accounting | https://bulletins.nyu.edu/graduate/business/programs/accounting-phd/ |
| 2 | Economics | https://bulletins.nyu.edu/graduate/business/programs/economics-phd/ |
| 3 | Finance | https://bulletins.nyu.edu/graduate/business/programs/finance-phd/ |
| 4 | Information Systems | https://bulletins.nyu.edu/graduate/business/programs/information-systems-phd/ |
| 5 | Management and Organizational Behavior | https://bulletins.nyu.edu/graduate/business/programs/management-organizational-behavior-phd/ |
| 6 | Marketing | https://bulletins.nyu.edu/graduate/business/programs/marketing-phd/ |
| 7 | Operations Management | https://bulletins.nyu.edu/graduate/business/programs/operations-management-phd/ |
| 8 | Statistics | https://bulletins.nyu.edu/graduate/business/programs/statistics-phd/ |

##### Advanced Certificate  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Law and Business | https://bulletins.nyu.edu/graduate/business/programs/law-business-advanced-certificate/ |

#### Steinhardt School of Culture, Education, and Human Development
##### MA  (43)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Advanced Occupational Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/advanced-occupational-therapy-ma/ |
| 2 | Art Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/art-therapy-ma/ |
| 3 | Art, Education, and Community Practice | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/art-education-community-practice-ma/ |
| 4 | Bilingual Education for Teachers | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/bilingual-education-teachers-ma/ |
| 5 | Childhood Education/Special Education: Childhood | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/childhood-education-special-education-childhood-ma/ |
| 6 | Childhood Special Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/childhood-special-education-ma/ |
| 7 | Costume Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/costume-studies-ma/ |
| 8 | Counseling for Mental Health and Wellness | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/counseling-mental-health-wellness-ma/ |
| 9 | Drama Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/drama-therapy-ma/ |
| 10 | Drama Therapy (Alternate Licensure) | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/drama-therapy-alternate-licensure-ma/ |
| 11 | Early Childhood Education/Special Education: Early Childhood | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/early-childhood-education-special-ma/ |
| 12 | Educational Leadership, Politics, and Advocacy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-leadership-politics-advocacy-ma/ |
| 13 | Educational Theatre, All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-theatre-all-grades-ma/ |
| 14 | Educational Theatre, All Grades, and English, 7-12 | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-theatre-all-grades-english-712-ma/ |
| 15 | Educational Theatre, All Grades, and Social Studies, 7–12 | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-theatre-all-grades-social-studies-712-ma/ |
| 16 | Environmental Conservation Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/environmental-conservation-education-ma/ |
| 17 | Food Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/food-studies-ma/ |
| 18 | Higher Education and Student Affairs | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/higher-education-student-affairs-ma/ |
| 19 | Human Development Research and Policy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/human-development-research-policy-ma/ |
| 20 | International Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/international-education-ma/ |
| 21 | Learning Technology and Experience Design | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/learning-technology-experience-design-ma/ |
| 22 | Media, Culture, and Communication | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/media-culture-communication-ma/ |
| 23 | Music Business | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-business-ma/ |
| 24 | Music Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-therapists-ma/ |
| 25 | Performing Arts Administration | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/performing-arts-administration-ma/ |
| 26 | Physical Therapists | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/physical-therapists-ma/ |
| 27 | Special Education: Early Childhood | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/special-education-early-childhood-ma/ |
| 28 | Specialized Studies in Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/specialized-studies-education-ma/ |
| 29 | Teacher of Dance, All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teacher-dance-all-grades-ma/ |
| 30 | Teachers of English 7-12 | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teachers-english-7-12-ma/ |
| 31 | Teachers of English Language and Literature in College | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-english-language-literature-college-ma/ |
| 32 | Teachers of Mathematics 7-12 | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teachers-mathematics-7-12-ma/ |
| 33 | Teaching Art, All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-art-all-grades-ma/ |
| 34 | Teaching Dance in the Professions | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-dance-professions-ma/ |
| 35 | Teaching Dance, All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-dance-all-grades-ma/ |
| 36 | Teaching English 7-12 with 5-6 Extension/Students with Disabilities 7-12 Generalist | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-english-7-12-5-6-extension-students-disabilities-7-12-generalist-ma/ |
| 37 | Teaching English to Speakers of Other Languages (TESOL) | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-english-speakers-other-languages-ma/ |
| 38 | Teaching English to Speakers of Other Languages (TESOL) All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-english-speakers-other-languages-all-grades-ma/ |
| 39 | Teaching Social Studies 7-12 with 5-6 Extension/Students with Disabilities 7-12 Generalist | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-social-studies-7-12-5-6-extension-students-disabilities-7-12-generalist-ma/ |
| 40 | Teaching World Languages 7-12/TESOL (All Grades) | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-world-languages-7-12-tesol-all-grades-ma/ |
| 41 | Theatre for Social and Civic Engagement | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/theatre-social-civic-engagement-ma/ |
| 42 | Visual Arts Administration | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/visual-arts-administration-ma/ |
| 43 | World Language Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/world-language-education-ma/ |

##### MS  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Statistics for Social Science Research | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/applied-statistics-social-science-research-ms/ |
| 2 | Communicative Sciences and Disorders | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/communicative-sciences-disorders-ms/ |
| 3 | Games for Learning | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/games-learning-ms/ |
| 4 | Nutrition and Dietetics | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/nutrition-dietetics-ms/ |

##### MFA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Studio Art | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/studio-art-mfa/ |

##### MAT  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Inclusive Childhood Teacher Residency | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/inclusive-childhood-teacher-residency-mat/ |
| 2 | Teacher Residency | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teacher-residency-mat/ |
| 3 | Transformational Teaching Students with Disabilities and Computer Science | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/transformational-teaching-students-disabilities-computer-science-mat/ |
| 4 | Transformational Teaching in Middle and High Schools | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/transformational-teaching-middle-high-schools-mat/ |

##### MM  (5)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Instrumental Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/instrumental-performance-mm/ |
| 2 | Music Technology | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-technology-mm/ |
| 3 | Music Theory and Composition | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-theory-composition-mm/ |
| 4 | Piano Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-performance-piano-mm/ |
| 5 | Vocal Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/vocal-performance-mm/ |

##### DMA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Music Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-performance-dma/ |

##### PhD  (24)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Applied Linguistics and Multilingual Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/applied-linguistics-multilingual-education-phd/ |
| 2 | Bilingual Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/bilingual-education-phd/ |
| 3 | Clinical/Counseling Psychology | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/clinical-counseling-psychology-phd/ |
| 4 | Communicative Sciences and Disorders | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/communicative-sciences-disorders-phd/ |
| 5 | Developmental Psychology | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/developmental-psychology-phd/ |
| 6 | Educational Communications and Technology | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-communications-technology-phd/ |
| 7 | Educational Leadership and Policy Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-leadership-policy-studies-phd/ |
| 8 | Educational Theatre in Colleges and Communities | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-theatre-colleges-communities-phd/ |
| 9 | English Education (Secondary and College) | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/english-education-secondary-college-phd/ |
| 10 | Food Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/food-studies-phd/ |
| 11 | Higher Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/higher-education-phd/ |
| 12 | International Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/international-education-phd/ |
| 13 | Media, Culture, and Communication | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/media-culture-communication-phd/ |
| 14 | Music Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-education-phd/ |
| 15 | Music Performance and Composition | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-performance-composition-phd/ |
| 16 | Music Technology | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/music-technology-phd/ |
| 17 | Nutrition and Dietetics | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/nutrition-dietetics-phd/ |
| 18 | Psychology and Social Intervention | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/psychology-social-intervention-phd/ |
| 19 | Rehabilitation Sciences | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/rehabilitation-sciences/ |
| 20 | Research in Occupational Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/research-occupational-therapy-phd/ |
| 21 | Research in Physical Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/research-physical-therapy-phd/ |
| 22 | Sociology of Education | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/sociology-education-phd/ |
| 23 | Statistics and Computational Social Science | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/statistics-computational-social-science-phd/ |
| 24 | Teaching and Learning | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-learning-phd/ |

##### EdD  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Educational Leadership and Policy Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-leadership-policy-studies-edd/ |
| 2 | Educational Theatre in Colleges and Communities | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/educational-theatre-colleges-communities-edd/ |
| 3 | Higher Education Administration | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/higher-education-administration-edd/ |
| 4 | Leadership and Innovation | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/leadership-innovation-edd/ |

##### DPT  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Physical Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/physical-therapy-entry-level-dpt/ |
| 2 | Physical Therapy for Practicing Physical Therapists | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/physical-therapy-practicing-physical-therapists-dpt/ |

##### OTD  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Occupational Therapy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/occupational-therapy-otd/ |
| 2 | Occupational Therapy for Practicing Occupational Therapists | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/occupational-therapy-practicing-occupational-therapists-otd/ |

##### Advanced Certificate  (8)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Bilingual Education for Teachers | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/bilingual-education-teachers-advanced-certificate/ |
| 2 | LGBTQ+ Health, Education, and Social Services | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/lgbtq-health-education-social-services-advanced-certificate/ |
| 3 | Piano Performance and Pedagogy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/piano-performance-pedagogy-advanced-certificate/ |
| 4 | Post-Baccalaureate Study in TESOL | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/post-baccalaureate-study-tesol-advanced-certificate/ |
| 5 | School Counseling | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/school-counseling-advanced-certificate/ |
| 6 | Teaching Dance, All Grades | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/teaching-dance-all-grades-advanced-certificate/ |
| 7 | Tonmeister Studies | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/tonmeister-studies-advanced-certificate/ |
| 8 | Vocal Pedagogy | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/vocal-pedagogy-advanced-certificate/ |

##### Advanced Diploma  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Classical Instrumental Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/classical-instrumental-performance-advanced-diploma/ |
| 2 | Jazz Instrumental Performance | https://bulletins.nyu.edu/graduate/culture-education-human-development/programs/jazz-studies-artist-diploma/ |

#### Tisch School of the Arts
##### MA  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Arts Politics | https://bulletins.nyu.edu/graduate/arts/programs/arts-politics-ma/ |
| 2 | Interactive Media Arts | https://bulletins.nyu.edu/graduate/arts/programs/interactive-media-arts-ma/ |
| 3 | Media Producing | https://bulletins.nyu.edu/graduate/arts/programs/media-producing-ma/ |
| 4 | Moving Image Archiving and Preservation | https://bulletins.nyu.edu/graduate/arts/programs/moving-image-archiving-preservation-ma/ |

##### MFA  (7)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Acting | https://bulletins.nyu.edu/graduate/arts/programs/acting-mfa/ |
| 2 | Dance: Interdisciplinary Research | https://bulletins.nyu.edu/graduate/arts/programs/dance-interdisciplinary-research-mfa/ |
| 3 | Design for Stage and Film | https://bulletins.nyu.edu/graduate/arts/programs/design-stage-film-mfa/ |
| 4 | Dramatic Writing | https://bulletins.nyu.edu/graduate/arts/programs/dramatic-writing-mfa/ |
| 5 | Film and Television | https://bulletins.nyu.edu/graduate/arts/programs/film-television-mfa/ |
| 6 | Game Design | https://bulletins.nyu.edu/graduate/arts/programs/game-design-mfa/ |
| 7 | Graduate Musical Theatre Writing | https://bulletins.nyu.edu/graduate/arts/programs/musical-theatre-writing-mfa/ |

##### MPS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Interactive Telecommunications | https://bulletins.nyu.edu/graduate/arts/programs/interactive-telecommunications-mps/ |
| 2 | Virtual Production | https://bulletins.nyu.edu/graduate/arts/programs/virtual-production-mps/ |

#### Robert F. Wagner Graduate School of Public Service
##### MS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Policy | https://bulletins.nyu.edu/graduate/public-service/programs/public-policy-ms/ |

##### MPA  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Executive MPA | https://bulletins.nyu.edu/graduate/public-service/programs/executive-master-public-administration-empa/ |
| 2 | Health Policy and Management | https://bulletins.nyu.edu/graduate/public-service/programs/health-policy-management-mpa/ |
| 3 | Public and Nonprofit Management and Policy | https://bulletins.nyu.edu/graduate/public-service/programs/public-nonprofit-management-policy-mpa/ |

##### MHA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Health Administration | https://bulletins.nyu.edu/graduate/public-service/programs/online-health-administration-mha/ |

##### MUP  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Urban Planning | https://bulletins.nyu.edu/graduate/public-service/programs/urban-planning-mup/ |

##### PhD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Administration | https://bulletins.nyu.edu/graduate/public-service/programs/public-administration-phd/ |

##### Advanced Certificate  (7)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Health Policy and Management: Financial Management | https://bulletins.nyu.edu/graduate/public-service/programs/health-policy-management-financial-management/ |
| 2 | Health Policy and Management: Health Policy Analysis | https://bulletins.nyu.edu/graduate/public-service/programs/health-policy-management-health-policy-analysis-advanced-certificate/ |
| 3 | Health Policy for Clinicians | https://bulletins.nyu.edu/graduate/public-service/programs/health-policy-clinicians-advanced-certificate/ |
| 4 | Program Evaluation and Impact Assessment | https://bulletins.nyu.edu/graduate/public-service/programs/program-evaluation-impact-assessment/ |
| 5 | Public and Nonprofit Management and Policy | https://bulletins.nyu.edu/graduate/public-service/programs/public-nonprofit-management-policy-advanced-certificate/ |
| 6 | Quantitative Methods for Policy Analysis | https://bulletins.nyu.edu/graduate/public-service/programs/quantitative-methods-policy-analysis-advanced-certificate/ |
| 7 | Social Finance | https://bulletins.nyu.edu/graduate/public-service/programs/social-finance-advanced-certificate/ |

#### Rory Meyers College of Nursing
##### MS  (9)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-acute-care-nurse-practitioner-ms/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-primary-care-nurse-practitioner-ms/ |
| 3 | Family Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/family-nurse-practitioner-ms/ |
| 4 | Nurse-Midwifery | https://bulletins.nyu.edu/graduate/nursing/programs/nurse-midwifery-ms/ |
| 5 | Nursing Education | https://bulletins.nyu.edu/graduate/nursing/programs/nursing-education-ms/ |
| 6 | Nursing Informatics | https://bulletins.nyu.edu/graduate/nursing/programs/nursing-informatics-ms/ |
| 7 | Pediatrics Nurse Practitioner Primary Care/Acute Care | https://bulletins.nyu.edu/graduate/nursing/programs/pediatrics-nurse-practitioner-primary-care-acute-ms/ |
| 8 | Pediatrics Primary Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/pediatrics-primary-care-nurse-practitioner-ms/ |
| 9 | Psychiatric-Mental Health Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/psychiatric-mental-health-nurse-practitioner-ms/ |

##### PhD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Nursing Research and Theory Development | https://bulletins.nyu.edu/graduate/nursing/programs/nursing-research-theory-development-phd/ |

##### DNP  (6)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-acute-care-nurse-practitioner-dnp/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-primary-care-nurse-practitioner-dnp/ |
| 3 | Family Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/family-nurse-practitioner-dnp/ |
| 4 | Nurse-Midwifery | https://bulletins.nyu.edu/graduate/nursing/programs/nurse-midwifery-dnp/ |
| 5 | Pediatric Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/pediatric-nurse-practitioner-dnp/ |
| 6 | Psychiatric-Mental Health Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/psychiatric-mental-health-nurse-practitioner-dnp/ |

##### Advanced Certificate  (10)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-acute-care-nurse-practitioner-advanced-certificate/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/adult-gerontology-primary-care-nurse-practitioner-advanced-certificate/ |
| 3 | Family Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/family-nurse-practitioner-advanced-certificate/ |
| 4 | Nurse-Midwifery | https://bulletins.nyu.edu/graduate/nursing/programs/nurse-midwifery-advanced-certificate/ |
| 5 | Nursing Education | https://bulletins.nyu.edu/graduate/nursing/programs/nursing-education-advanced-certificate/ |
| 6 | Nursing Informatics | https://bulletins.nyu.edu/graduate/nursing/programs/nursing-informatics-advanced-certificate/ |
| 7 | Palliative Care Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/palliative-care-nurse-practitioner-advanced-certificate/ |
| 8 | Pediatrics Nurse Practitioner Acute Care | https://bulletins.nyu.edu/graduate/nursing/programs/pediatrics-nurse-practitioner-acute-care-advanced-certificate/ |
| 9 | Pediatrics Nurse Practitioner Primary Care | https://bulletins.nyu.edu/graduate/nursing/programs/pediatrics-nurse-practitioner-primary-care-advanced-certificate/ |
| 10 | Psychiatric-Mental Health Nurse Practitioner | https://bulletins.nyu.edu/graduate/nursing/programs/psychiatric-mental-health-nurse-practitioner-advanced-certificate/ |

#### School of Global Public Health
##### MA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Bioethics | https://bulletins.nyu.edu/graduate/global-public-health/programs/bioethics-ma/ |

##### MS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biostatistics | https://bulletins.nyu.edu/graduate/global-public-health/programs/biostatistics-ms/ |
| 2 | Epidemiology | https://bulletins.nyu.edu/graduate/global-public-health/programs/epidemiology-ms/ |

##### MPH  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Health | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-mph/ |

##### PhD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Health | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-phd/ |

##### DPH  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Health | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-dph/ |

##### Advanced Certificate  (4)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Public Health | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-advanced-certificate/ |
| 2 | Public Health Data Science | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-data-science-advanced-certificate/ |
| 3 | Public Health Disaster Science, Policy and Practice | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-disaster-science-policy-practice-advanced-certificate/ |
| 4 | Public Health Nutrition | https://bulletins.nyu.edu/graduate/global-public-health/programs/public-health-nutrition-advanced-certificate/ |

#### Silver School of Social Work
##### MSW  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Social Work | https://bulletins.nyu.edu/graduate/social-work/programs/social-work-msw/ |

##### PhD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Social Work | https://bulletins.nyu.edu/graduate/social-work/programs/social-work-phd/ |

##### DSW  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Clinical Social Work | https://bulletins.nyu.edu/graduate/social-work/programs/clinical-social-work-dsw/ |

#### Gallatin School of Individualized Study
##### MA  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Individualized Study | https://bulletins.nyu.edu/graduate/individualized-study/programs/individualized-study-ma/ |

#### School of Professional Studies (SPS)
##### MS  (22)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Entrepreneurship and Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/entrepreneurship-management-ms/ |
| 2 | Event Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/event-management-ms/ |
| 3 | Executive Coaching and Organizational Consulting | https://bulletins.nyu.edu/graduate/professional-studies/programs/executive-coaching-organizational-consulting-ms/ |
| 4 | Financial Planning | https://bulletins.nyu.edu/graduate/professional-studies/programs/financial-planning-ms/ |
| 5 | Global Affairs | https://bulletins.nyu.edu/graduate/professional-studies/programs/global-affairs-ms/ |
| 6 | Global Hospitality Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/global-hospitality-management-ms/ |
| 7 | Global Security, Conflict, and Cyber Crime | https://bulletins.nyu.edu/graduate/professional-studies/programs/global-security-conflict-cyber-crime-ms/ |
| 8 | Global Sport | https://bulletins.nyu.edu/graduate/professional-studies/programs/global-sport-ms/ |
| 9 | Human Capital Analytics and Technology | https://bulletins.nyu.edu/graduate/professional-studies/programs/human-capital-analytics-technology-ms/ |
| 10 | Human Capital Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/human-capital-management-ms/ |
| 11 | Integrated Marketing | https://bulletins.nyu.edu/graduate/professional-studies/programs/integrated-marketing-ms/ |
| 12 | Management and Analytics | https://bulletins.nyu.edu/graduate/professional-studies/programs/management-analytics-ms/ |
| 13 | Marketing and Strategic Communications, Executive | https://bulletins.nyu.edu/graduate/professional-studies/programs/executive-masters-marketing-strategic-communications/ |
| 14 | Professional Writing | https://bulletins.nyu.edu/graduate/professional-studies/programs/professional-writing-ms/ |
| 15 | Project Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/project-management-ms/ |
| 16 | Public Relations and Corporate Communication | https://bulletins.nyu.edu/graduate/professional-studies/programs/public-relations-corporate-communication-ms/ |
| 17 | Publishing | https://bulletins.nyu.edu/graduate/professional-studies/programs/publishing-ms/ |
| 18 | Real Estate | https://bulletins.nyu.edu/graduate/professional-studies/programs/real-estate-ms/ |
| 19 | Real Estate Development | https://bulletins.nyu.edu/graduate/professional-studies/programs/real-estate-development-ms/ |
| 20 | Sports Business | https://bulletins.nyu.edu/graduate/professional-studies/programs/sports-business-ms/ |
| 21 | Translation and Interpreting | https://bulletins.nyu.edu/graduate/professional-studies/programs/translation-interpreting-ms/ |
| 22 | Travel and Tourism Management | https://bulletins.nyu.edu/graduate/professional-studies/programs/travel-tourism-management-ms/ |

##### MS/MS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Human Capital Management/Human Capital Analytics and Technology | https://bulletins.nyu.edu/graduate/professional-studies/programs/human-capital-management-human-capital-analytics-technology-ms-ms/ |

#### College of Dentistry
##### MS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Biomaterials Science | https://bulletins.nyu.edu/graduate/dentistry/programs/biomaterials-science-ms/ |
| 2 | Clinical Research | https://bulletins.nyu.edu/graduate/dentistry/programs/clinical-research-ms/ |

##### DDS  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Dentistry | https://bulletins.nyu.edu/graduate/dentistry/programs/dentistry-dds/ |

##### Advanced Certificate  (7)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Clinical Research | https://bulletins.nyu.edu/graduate/dentistry/programs/clinical-research-advanced-certificate/ |
| 2 | Endodontics | https://bulletins.nyu.edu/graduate/dentistry/programs/endodontics-advanced-certificate/ |
| 3 | Oral and Maxillofacial Surgery | https://bulletins.nyu.edu/graduate/dentistry/programs/oral-maxillofacial-surgery-advanced-certificate/ |
| 4 | Orthodontics and Dentofacial Orthopedics | https://bulletins.nyu.edu/graduate/dentistry/programs/orthodontics-dentofacial-orthopedics-advanced-certificate/ |
| 5 | Pediatric Dentistry | https://bulletins.nyu.edu/graduate/dentistry/programs/pediatric-dentistry-advanced-certificate/ |
| 6 | Periodontics | https://bulletins.nyu.edu/graduate/dentistry/programs/periodontics-advanced-certificate/ |
| 7 | Prosthodontics | https://bulletins.nyu.edu/graduate/dentistry/programs/prosthodontics-advanced-certificate/ |

#### School of Law
##### MS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Cybersecurity Risk and Strategy | https://bulletins.nyu.edu/graduate/law/programs/cybersecurity-risk-strategy-ms/ |
| 2 | Health Law and Strategy | https://bulletins.nyu.edu/graduate/law/programs/health-law-strategy-ms/ |

##### JD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Law | https://bulletins.nyu.edu/graduate/law/programs/law-jd/ |

##### LLM  (10)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Competition, Innovation & Information Law | https://bulletins.nyu.edu/graduate/law/programs/competition-innovation-information-law-llm/ |
| 2 | Corporate Law | https://bulletins.nyu.edu/graduate/law/programs/corporate-law-llm/ |
| 3 | Environmental and Energy Law | https://bulletins.nyu.edu/graduate/law/programs/environmental-energy-law-llm/ |
| 4 | International Business Regulation, Litigation & Arbitration | https://bulletins.nyu.edu/graduate/law/programs/international-business-regulation-litigation-arbitration-llm/ |
| 5 | International Legal Studies | https://bulletins.nyu.edu/graduate/law/programs/international-legal-studies-llm/ |
| 6 | International Taxation | https://bulletins.nyu.edu/graduate/law/programs/international-taxation-llm/ |
| 7 | Law | https://bulletins.nyu.edu/graduate/law/programs/law-llm/ |
| 8 | Legal Theory | https://bulletins.nyu.edu/graduate/law/programs/legal-theory-llm/ |
| 9 | Taxation | https://bulletins.nyu.edu/graduate/law/programs/taxation-llm/ |
| 10 | Taxation-Executive Program | https://bulletins.nyu.edu/graduate/law/programs/taxation-executive-program-llm/ |

##### JSD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Juridical Science | https://bulletins.nyu.edu/graduate/law/programs/juridical-science-jsd/ |

##### MSL  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Taxation | https://bulletins.nyu.edu/graduate/law/programs/taxation-msl/ |

##### Advanced Certificate  (3)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Corporate Taxation | https://bulletins.nyu.edu/graduate/law/programs/corporate-taxation-advanced-certificate/ |
| 2 | Estate Planning | https://bulletins.nyu.edu/graduate/law/programs/estate-planning-advanced-certificate/ |
| 3 | International Taxation | https://bulletins.nyu.edu/graduate/law/programs/international-taxation-advanced-certificate/ |

#### NYU Grossman School of Medicine
##### MS  (2)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Clinical Investigation | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/clinical-investigation-ms/ |
| 2 | Genome Health Analysis | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/genome-health-analysis-ms/ |

##### MD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Medicine | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/medicine-md/ |

##### Advanced Certificate  (5)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Clinical and Translational Investigation | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/clinical-translational-investigation-advanced-certificate/ |
| 2 | Comparative Effectiveness and Implementation Research Training Program | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/comparative-effectiveness-implementation-research-training-advanced-certificate/ |
| 3 | Determinants of Health in Research and Practice | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/determinants-health-research-practice-advanced-certificate/ |
| 4 | Health Innovations and Therapeutics | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/health-innovations-therapeutics-advanced-certificate/ |
| 5 | Healthcare Delivery Science | https://bulletins.nyu.edu/graduate/medicine-grossman/programs/healthcare-delivery-science-advanced-certificate/ |

#### NYU Grossman Long Island School of Medicine
##### MD  (1)

| # | 专业/项目 | URL |
|---|-----------|-----|
| 1 | Medicine | https://bulletins.nyu.edu/graduate/medicine-long-island/programs/medicine-md/ |


### 2.2 项目深度示例 — Tandon School of Engineering, Computer Science (MS)

NYU Tandon 是申请量最大的工程学院研究生项目之一。下表为 Computer Science (MS) 的完整招生信息:

| 字段 | 值 | 来源 |
|------|----|----|
| 所属学院 | Tandon School of Engineering | bulletins |
| 所属系 | Computer Science and Engineering Department | bulletins |
| NYSED/HEGIS/CIP | 85149 / 0701.00 / 11.0101 | bulletins |
| 项目 URL | https://bulletins.nyu.edu/graduate/engineering/programs/computer-science-tandon-ms/ | bulletins |
| 申请入口 | Office of Graduate Admissions (Tandon) | bulletins |
| 背景/前置课要求 | 本科学位 (CS/数学/科学/工程优先); 1 年大学科学; 高级编程语言 (C++ 优先); 计算机基础 (数据结构、计算机组成、体系结构); 微积分 | bulletins |
| GRE 政策 | 不强制 (满足 Bridge / 9-credit visiting / NYU CS BA&BS GPA 3.0+ 等条件者免交),但鼓励提交 | bulletins |
| 英语能力 | 外国学生可能需参加预备英语课程; 演示书面和口头英语沟通能力 | bulletins |
| 转学分上限 | 最多 9 个研究生学分可转入 MS | bulletins |
| Bridge 通道 | 无 CS 背景的申请者推荐先完成 NYU Tandon Bridge 项目 | bulletins |
| 学费 | 见 Section 4.3 (Bursar 工具按学分/项目查询) | bursar |

> 来源 snippet: "We offer a highly adaptive MS in Computer Science program that lets students shape the degree around their interests… Admission to this program requires applicants to have an undergraduate degree in computer science, mathematics, science, or engineering… GRE Requirements: Applicants who satisfy one of the following conditions are not required but encouraged to submit a GRE score…"

### 2.3 研究生招生模式 (去中心化)

NYU 研究生招生**完全去中心化** — 没有单一的研究生申请门户或统一申请表。每所研究生/专业学院独立管理申请、截止日期、费用、GRE/语言要求与资金。但所有学院的项目**目录**统一托管在 bulletins.nyu.edu,可通过 per-school programs 页面获取完整项目列表 (本文档 Section 2 已穷尽列出)。

研究生院的入口 (官方):
- GSAS: https://as.nyu.edu/admissions.html
- Tandon: https://engineering.nyu.edu/admissions/graduate
- Stern: https://www.stern.nyu.edu/programs-admissions
- Wagner: https://wagner.nyu.edu/admissions
- Tisch: https://tisch.nyu.edu/admissions
- Steinhardt: https://steinhardt.nyu.edu/admissions
- Meyers Nursing: https://nursing.nyu.edu/admissions
- Silver Social Work: https://socialwork.nyu.edu/admissions
- SPS: https://www.sps.nyu.edu/admissions
- Global Public Health: https://publichealth.nyu.edu/admissions
- Dentistry: https://dental.nyu.edu/admissions
- Law: https://www.law.nyu.edu/admissions
- Grossman Medicine: https://med.nyu.edu/education/md-degree/admissions

资金方面:GSAS / Tandon / Sackler (Vilcek) 等博士项目通常提供全额资助 (RA/TA + stipend + tuition);专业硕士 (MS/MA) 多为自费或竞争性奖学金;Stern MBA / Law JD / Medicine MD 各有独立资助体系。

---

## SECTION 3 — Application requirements & deadlines

### 3.1 本科 — 核心数据表 (First-Year)

| 维度 | 值 | 来源 |
|------|----|----|
| 招生官网 | https://www.nyu.edu/admissions/undergraduate-admissions.html | nyu.edu |
| 申请平台 | The Common Application | nyu.edu |
| 申请费 | $85.00 (不可退,可通过 Common App 在线支付;困难可申请 fee waiver) | E-U-005 |
| Early Decision I | 申请截止 **Nov 1** · 放榜 Dec 15 | E-U-001 |
| Early Decision II | 申请截止 **Jan 1** · 放榜 Feb 15 | E-U-001 |
| Regular Decision | 申请截止 **Jan 5** · 放榜 Apr 1 | E-U-001 |
| 截止时间 | 当地时区 11:59 pm | E-U-001 |
| 试镜/作品集 | 强烈建议提前一个月提交 Common App 以预留准备时间 | E-U-001 |
| SAT/ACT 政策 | **Test-optional 至 2026-2027 申请季**; 若提交,可从 SAT / ACT / AP / IB Diploma / GCE A-Level / 国际考试中选其一 | E-U-003 |
| Superscore | NYU 接受 superscore (取各次最高);不接受 TOEFL iBT "My Best" 与 IELTS One Skill Retake | E-U-004 |
| 送分 | 录取并入学后须送官方成绩;申请阶段可自报 (Applicant Portal) | E-U-003 |
| 面试政策 | **不要求且不可主动预约** (interviews are not required and cannot be requested) | E-U-004 |
| 推荐信 | 通常 1 封 counselor + 1-2 封 teacher (Common App 标准);见 Common App member questions | nyu.edu |
| 文件递交 | 接受官方或非官方成绩单;可上传至 Applicant Portal 或邮件 admissions.docs@nyu.edu;非英文需附认证翻译 (中文文件送 NYU Shanghai 例外) | E-U-002 |
| 邮寄地址 | NYU Office of Undergraduate Admissions, 400 Lafayette St 4th Fl, New York NY 10003 USA | E-U-002 |
| 联系电话/邮箱 | +1-212-998-4500 / admissions@nyu.edu | nyu.edu |
| 转学途径 | 单独 Transfer 申请 (transfer 学生**不**适用 NYU Promise,且除个别项目外不适用 NYU 奖学金/助学金) | E-U-006 |

### 3.2 本科英语能力要求

> 适用条件:若英语非第一语言,且过去 3 年非全英文授课 (世界语言课程除外),通常需提交近 2 年内的英语考试成绩。英语第一语言者或过去 3 年全英文授课者可免。

| 考试 | 最低要求 | 竞争性分数 | 来源 |
|------|---------|-----------|------|
| TOEFL iBT (2026-01-20 及之前) | 无最低分 | **100+** | E-U-004 |
| TOEFL iBT (2026-01-21 起, 新版) | 无最低分 | **5+ (overall 与各 sub, 新版评分)** | E-U-004 |
| Duolingo English Test | 无最低分 | **135+** | E-U-004 |
| IELTS Academic | 无最低分 | **7.5+** | E-U-004 |
| PTE Academic | 无最低分 | **70+** | E-U-004 |
| Cambridge English Scale (C1 Advanced / C2 Proficiency) | 无最低分 | **191+** | E-U-004 |

- **TOEFL 送分代码: 2562** (E-U-004)
- IELTS/PTE/Cambridge:搜索 "New York University" 并 release 至 Undergraduate Admissions (而非具体学院)
- 不接受 TOEFL iBT "My Best" 与 IELTS One Skill Retake
- Duolingo 不接受自报分,须官方送分 (免费)
- SAT/ACT/AP/IGCSE/A-Level/IB 等英语授课考试**不能**豁免 NYU 的英语能力要求

### 3.3 研究生 — 全局规则

| 维度 | 值 | 来源 |
|------|----|----|
| 招生模式 | **去中心化** — 各研究生/专业学院独立管理申请 | nyu.edu/admissions/graduate-admissions.html |
| 申请平台 | 各学院自有系统 (部分用 Common App graduate / Embark / 学校自建) | per-school |
| 标准申请费 | 无统一费用 — 因学院/项目而异 (GSAS ~$115, Tandon ~$125, SPS ~$125 等,以各学院页面为准) | per-school (P0 follow-up) |
| 商学院费用 | Stern MBA / MS 费用不同 (见 Stern admissions) | stern.nyu.edu |
| 4-15 协议 | NYU 多数 PhD 项目遵守 CGS 4-15 决议 (各院具体执行) | — |
| GRE/GMAT 政策 | 因项目而异 — GSAS 多数 PhD 要求 GRE; Tandon 多数 MS GRE optional/test-flexible; Stern MBA 接受 GMAT/GRE; Law LSAT/GRE; Medicine MCAT | per-program (见 2.2 CS-MS 示例) |
| 语言要求 | 因学院而异 — 大多数研究生院要求 TOEFL 100 / IELTS 7 / Duolingo 120 等;部分院 (如 GSAS) 有更细分的最低分 | per-school |
| 申请时间线 | 各院不同 — 多数 fall 入学 12-1 月截止; PhD 多在 12 月初截止 | per-school |
| 机构代码 | TOEFL 2562 (UG); grad 各院代码以院页面为准 | — |

---

## SECTION 4 — Costs & financial aid

### 4.1 本科 Cost of Attendance (2026-2027, 纽约校区)

> 来源: https://www.nyu.edu/admissions/financial-aid-and-scholarships/cost-of-attendance.html (capture 2026-07-04)。COA 因学院而异,下表为示例 (与 Stern 一致的代表性学校)。

**Stern / 代表性本科学院 2026-2027 估算 (住校或校外):**

| 项目 | 金额 (USD) | 类型 | 来源 |
|------|-----------|------|------|
| Tuition (学费) | **$68,576** | Direct | E-U-007 |
| Student Health Insurance | $2,308 | Direct | E-U-007 |
| Books and Supplies | $1,730 | Direct | E-U-007 |
| Food | $5,800 | Direct | E-U-007 |
| Housing | $6,000 | Direct | E-U-007 |
| **Direct Costs 合计 (NYU 直接计费)** | **$84,414** | Direct | E-U-007 |
| Transportation (通勤) | $3,550 | Indirect | E-U-007 |
| Personal Expenses (个人) | $2,364 | Indirect | E-U-007 |
| **Indirect Costs 合计** | **$5,914** | Indirect | E-U-007 |
| **Total Cost of Attendance (估算)** | **$90,328** | 总计 | E-U-007 |

> 另一示例学院 (CAS 类) 估算 COA ≈ $91,676 (Tuition $68,576; Direct $80,820; Indirect $10,856)。各学院学费在 Bursar Tuition & Fees Lookup Tool (https://www.nyu.edu/students/financial-services-and-bursar.html) 按学分/项目查询。

### 4.2 本科助学金政策 — NYU Promise

> 来源: https://www.nyu.edu/admissions/financial-aid-and-scholarships/cost-of-attendance.html (capture 2026-07-04)

| 政策 | 详情 | 来源 |
|------|------|------|
| **NYU Promise** — 满足 100% need | 对**首次入学的一年级** (first-time, first-year) 纽约校区本科生,NYU 满足 100% 经济需求 | E-U-006 |
| 学费免费门槛 | 家庭年收入 < $100,000 且资产 typical 者,**学费免费** | E-U-006 |
| 学费上涨保护 | 奖学金每年随学费上涨自动调整 (Scholarships adjusted to meet tuition increases each year) | E-U-006 |
| 适用对象限制 | **仅 first-time, first-year** (不含转学 Transfer) | E-U-006 |
| Transfer 政策 | Transfer 学生**不**适用 NYU Promise 及大多数 NYU 奖学金/助学金;可申请联邦助学金、外部奖学金、私人贷款 | E-U-006 |
| Need-blind / Need-aware | NYU 对国际生 need-aware (国际生申请经济资助会影响录取) | — (P1 follow-up) |
| 本科毕业生平均起薪 | 约 $76,000/年 (NYU 官方数据) | E-U-007 |

### 4.3 研究生费用与资助框架

| 类别 | 详情 |
|------|------|
| 资金类型分类 | (1) 全额资助博士 (GSAS/Tandon/Sackler PhD: 免学费 + stipend + 医保); (2) 部分资助硕士 (TA/RA 覆盖部分); (3) 自费专业硕士 (MS/MA/MBA/LLM/JD/MD 多为自费或竞争性奖) |
| 常见资助形式 | Teaching Assistantship (TA)、Research Assistantship (RA)、Fellowship、Grant、外部奖学金 |
| 申请费 | 因学院/项目而异 (见 3.3) |
| Fee waiver | 多数学院对符合条件者 (如美国少数族裔项目、McNair、GRE fee waiver 持有者) 提供; 各院独立申请 |
| Cost of Attendance | 各院 COA 在 https://www.nyu.edu/admissions/financial-aid-and-scholarships/cost-of-attendance.html graduate 区块 (按学院/项目/位置查询) |
| Stipend rates / 生活费 | 各院独立公布 (GSAS / Tandon / Vilcek 等 PhD stipend 通常 $40k-$50k/年区间) — **P0 follow-up: 未在本轮逐一抓取各院 stipend 表** |

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001: UG application deadlines
field: undergraduate.application.deadlines
value: { ED_I: "Nov 1 (decision Dec 15)", ED_II: "Jan 1 (decision Feb 15)", RD: "Jan 5 (decision Apr 1)", cutoff: "11:59 pm local time" }
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/how-to-apply/all-freshmen-applicants.html
source_snippet: "Notification Plan | Application Deadline* | Decision — Early Decision I | November 1 | December 15 — Early Decision II | January 1 | February 15 — Regular Decision | January 5 | April 1. *The cut-off time for applications is 11:59 pm in your local time zone."
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-002: UG document submission
field: undergraduate.application.documents
value: "Accepts official OR unofficial transcripts; upload via Applicant Portal or email admissions.docs@nyu.edu; non-English docs require certified English translation (exception: Mandarin Chinese for NYU Shanghai)"
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/how-to-apply/all-freshmen-applicants.html
source_snippet: "NYU will accept official or unofficial transcripts and test scores for the purposes of our application review process. Students can send unofficial documents by email to admissions.docs@nyu.edu... Include an official English translation if the document isn't in English... NYU will only make exceptions for documents in Mandarin Chinese submitted to NYU Shanghai."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-003: UG standardized testing policy
field: undergraduate.application.testing_policy
value: "Test-optional through 2026-2027 application cycle; if submitted, choose ONE of: SAT, ACT, AP Exams, IB Diploma, GCE A-Level, International Examinations"
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/how-to-apply/standardized-tests.html
source_snippet: "NYU will continue to remain test-optional through the 2026-2027 application cycle. For students who elect to submit testing... you can submit one of the following: SAT, ACT, Advanced Placement Exams, International Baccalaureate (IB) Diploma Program, GCE Advanced Level (A-Level), International Examinations."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-004: UG English language testing
field: undergraduate.application.english_language_testing
value: { required_if: "English not first language OR <3 yrs all-English instruction", competitive: { TOEFL_iBT_pre_2026_01_20: 100, TOEFL_iBT_post_2026_01_21: "5+ overall & subscores", Duolingo: 135, IELTS_Academic: 7.5, PTE_Academic: 70, Cambridge_Scale: 191 }, TOEFL_code: 2562, mybest_not_accepted: true, ielts_oneskillretake_not_accepted: true, interviews: "not required and cannot be requested" }
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/how-to-apply/standardized-tests/english-language-testing.html
source_snippet: "competitive applicants will receive: 100 and above on the TOEFL iBT taken on or before January 20, 2026. 5 or above (overall score and subscores) on the TOEFL iBT taken on or after January 21, 2026. 135 and above on the Duolingo English Test. 7.5 and above on the IELTS Academic. 70 and above on the PTE Academic. 191 and above on the Cambridge English Scale. ... For the TOEFL iBT, use NYU's code 2562. ... No. Interviews are not required and cannot be requested by candidates for admission to NYU."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-005: UG application fee
field: undergraduate.application.fee
value: "$85.00 USD, nonrefundable, paid online via Common Application; fee waiver available for financial hardship"
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/how-to-apply/application-fee-information.html
source_snippet: "For those who do pay the application fee of $85.00 US dollars, it is a nonrefundable fee that is paid online through the Common Application website... Students who feel that the application fee would be a financial hardship for their families can simply request a fee waiver on the Common Application."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-006: NYU Promise financial aid policy
field: undergraduate.financial_aid.nyu_promise
value: { meets_100_percent_need: true, tuition_free_threshold: "family income < $100,000 with typical assets", eligible: "first-time, first-year only (NOT transfers)", scholarships_adjust_with_tuition: true }
source_url: https://www.nyu.edu/admissions/financial-aid-and-scholarships/cost-of-attendance.html
source_snippet: "For first-time, first-year undergraduate students admitted to the New York campus, NYU will meet 100% demonstrated need, and families with income less than $100,000 and typical assets will not have to pay tuition. Scholarships will be adjusted to meet tuition increases each year. ... Transfer students are not eligible for the NYU Promise."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-007: UG Cost of Attendance 2026-2027
field: undergraduate.cost.attendance_2026_2027
value: { tuition: 68576, health_insurance: 2308, books: 1730, food: 5800, housing: 6000, direct_total: 84414, transportation: 3550, personal: 2364, indirect_total: 5914, total_COA: 90328, avg_starting_salary: 76000 }
source_url: https://www.nyu.edu/admissions/financial-aid-and-scholarships/cost-of-attendance.html
source_snippet: "Direct Costs: Tuition $68,576 — Student Health Insurance $2,308 — Books and Supplies $1,730 — Food $5,800 — Housing $6,000 — Estimated Total Direct Costs $84,414. Indirect Costs: Estimated Transportation $3,550 — Estimated Personal Expenses $2,364 — Estimated Total Indirect Costs $5,914. Total Cost of Attendance (estimated) $90,328. On average, recent NYU bachelor's degree graduates make about $76,000 per year."
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-008: UG schools/colleges (NYC 11 admissions-facing + Dentistry)
field: undergraduate.schools.nyc
value: 13 UG-degree-granting schools (CAS, Dentistry, Gallatin, Stern, Liberal Studies, Meyers Nursing, Steinhardt, Silver Social Work, SPS, Tandon, Tisch, Wagner, Global Public Health)
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/campuses-schools-and-colleges.html
source_snippet: "Our New York City campus is home to 11 schools and colleges... College of Arts & Science, College of Dentistry, Gallatin School of Individualized Study, Leonard N. Stern School of Business, Liberal Studies, Rory Meyers College of Nursing, Steinhardt School of Culture, Education, and Human Development, Silver School of Social Work, School of Professional Studies, Tandon School of Engineering, Tisch School of the Arts."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-009: 270+ areas of study
field: undergraduate.programs.areas_of_study_marketing
value: "270+ areas of study available to NYU students (cross-campus)"
source_url: https://www.nyu.edu/admissions/undergraduate-admissions/majors-and-programs.html
source_snippet: "With more than 270 areas of study, your fellow NYU community members are bound to be teaching, researching, or debating a topic that interests you."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-001: Graduate program directory structure
field: graduate.programs.directory
value: "Each graduate school's full program list is at bulletins.nyu.edu/graduate/<school-slug>/programs/ ; programs identified by links matching /programs/<slug>/ with degree in trailing parens"
source_url: https://bulletins.nyu.edu/graduate/arts-science/programs/
source_snippet: "Africana Studies (MA), American Journalism (MA), American Studies (PhD), Animal Studies (MA), Anthropology (PhD), Applied Economic Analysis (Advanced Certificate)..."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-002: Tandon CS MS deep-dive
field: graduate.tandon.cs_ms.admissions
value: { dept: "Computer Science and Engineering Department", background: "UG degree in CS/math/science/engineering preferred", gre: "not required but encouraged (waivers via Bridge / visiting credits / NYU CS BA&BS GPA 3.0+)", transfer_credit_max: 9, bridge: "NYU Tandon Bridge recommended for non-CS backgrounds" }
source_url: https://bulletins.nyu.edu/graduate/engineering/programs/computer-science-tandon-ms/
source_snippet: "Admission to this program requires applicants to have an undergraduate degree in computer science, mathematics, science, or engineering... GRE Requirements: Applicants who satisfy one of the following conditions are not required but encouraged to submit a GRE score... A maximum of 9 credits from previous graduate work at an accredited institution may be transferred to the MS degree."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-003: Graduate admissions decentralized
field: graduate.admissions.model
value: "Fully decentralized — each school manages own application, deadlines, fees, GRE/language policy, funding"
source_url: https://www.nyu.edu/admissions/graduate-admissions.html
source_snippet: "Already know which NYU school you're interested in? Connect with them here: [list of 22 graduate schools/units each with own admissions]"
capture_date: 2026-07-04
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: nyu-knowledge-base-v2
├── doc: nyu-overview                  (Section 0 — counts, hierarchy, matrix, degree inventory)
├── doc: nyu-ug-cas                    (Section 1.2 — CAS majors + 1.4 minors in CAS)
├── doc: nyu-ug-tandon                 (Section 1.2 — Tandon majors)
├── doc: nyu-ug-tisch                  (Section 1.2 — Tisch majors)
├── doc: nyu-ug-stern                  (Section 1.2 — Stern majors)
├── doc: nyu-ug-steinhardt             (Section 1.2 — Steinhardt majors)
├── doc: nyu-ug-other                  (Section 1.2 — Nursing/SocialWork/SPS/Gallatin/LS/Dentistry/GPH/Wagner majors)
├── doc: nyu-ug-minors                 (Section 1.4 — all 146 minors)
├── doc: nyu-grad-gsas                 (Section 2 — GSAS 116 programs)
├── doc: nyu-grad-steinhardt           (Section 2 — Steinhardt grad 100 programs)
├── doc: nyu-grad-tandon               (Section 2 — Tandon grad 36 programs)
├── doc: nyu-grad-nursing              (Section 2 — Meyers grad 26)
├── doc: nyu-grad-stern                (Section 2 — Stern grad 24)
├── doc: nyu-grad-sps                  (Section 2 — SPS grad 23)
├── doc: nyu-grad-tisch                (Section 2 — Tisch grad 13)
├── doc: nyu-grad-public-health        (Section 2 — GPH grad 10)
├── doc: nyu-grad-dentistry            (Section 2 — Dentistry grad 10)
├── doc: nyu-grad-wagner               (Section 2 — Wagner grad 14)
├── doc: nyu-grad-law                  (Section 2 — Law grad 18)
├── doc: nyu-grad-medicine             (Section 2 — Grossman + LI Med grad 9)
├── doc: nyu-grad-social-work          (Section 2 — Silver grad 3)
├── doc: nyu-grad-gallatin             (Section 2 — Gallatin MA)
├── doc: nyu-app-requirements          (Section 3 — deadlines, tests, English)
├── doc: nyu-costs-aid                 (Section 4 — COA, NYU Promise)
└── doc: nyu-evidence-index            (Section 5 — evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "nyu-knowledge-base-v2"
  school: "<home college, e.g. Tandon School of Engineering>"
  department: "<home department if applicable, else N/A>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <bulletins.nyu.edu program URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|---------|------|
| P0 | 各研究生院逐项目 GRE/语言最低分表 | per-program bulletin pages | 本轮以 Tandon CS-MS 为示例,其余 ~400 项目逐个展开为 P0 |
| P0 | 各研究生院逐项目申请费 & 截止日期 | per-school admissions pages | 因去中心化,需逐院抓取 |
| P0 | 各 PhD 项目 stipend / 资助金额 | per-school cost-of-attendance grad pages | GSAS/Tandon/Vilcek 等 |
| P1 | Stern 各 MBA/MS 学费 (区分项目) | bursar lookup + Stern admissions | 本轮仅抓取代表性 COA |
| P1 | NYU 对国际生 need-blind/need-aware 官方表述 | financial-aid FAQ | 本轮未单独抓取 |
| P1 | NYU Abu Dhabi (26 majors) & NYU Shanghai (18 majors) 完整目录 | bulletins.nyu.edu/undergraduate/{abu-dhabi,shanghai}/programs/ | 本轮按 focus 排除 |
| P2 | 各本科专业 Core/课程要求 detail | per-program bulletin | 本轮仅概括 |

---

## SECTION 7 — Cross-school comparison framework (NYU column)

| 维度 | NYU 值 | 备注 |
|------|--------|------|
| UG 总费用/年 (COA) | $90,328 | 2026-2027 estimated |
| 学费/年 | $68,576 | 2026-2027 |
| Need-blind (intl?) | Need-aware (intl) | P1 confirm |
| ED I 截止 | Nov 1 | |
| ED II 截止 | Jan 1 | |
| RD 截止 | Jan 5 | |
| SAT/ACT required? | Test-optional (through 2026-27) | |
| TOEFL 竞争分 | 100 (pre-2026-01-20) / 5+ (post) | 无最低分 |
| IELTS 竞争分 | 7.5 | |
| 学费免费门槛 | 家庭收入 < $100k (typical assets) | first-time first-year only |
| 本科生均起薪 | ~$76,000 | |
| 研究生申请费 | 因院而异 (无统一) | |
| 4-15 协议 | 多数 PhD 项目遵守 | |
| **总项目数 (Rule 1)** | **730** (NYC) | 181 UG majors + 146 minors + 337 grad deg + 66 grad cert |
| **学院/系总数 (Rule 2)** | 13 UG + 15 grad schools | NYC |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: nyu.edu (UG admissions, financial aid), bulletins.nyu.edu (undergraduate + graduate per-school programs pages), stern.nyu.edu, engineering.nyu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (`document.querySelectorAll('a')` filtered by `/programs/<slug>/` regex); cross-school dedup by URL; reconciliation 730 == 730 == 730.
> **Granularity**: school → department → degree-level → program
