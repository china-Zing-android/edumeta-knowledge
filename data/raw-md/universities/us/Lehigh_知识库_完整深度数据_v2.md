# Lehigh University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: curl + Python DOM extraction (Chromium unavailable)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | ~105 |
| 本科辅修 (Minor) | ~65 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/MEng/MEd) | ~75 |
| 研究生高级证书 (Advanced Certificate / Diploma) | ~25 |
| **学位项目总计 (UG + Grad)** | **~205** |
| 学院 / 独立系所总数 | 5 |

> 注：精确数字需通过课程目录数据库逐条计数。以上为基于官方页面提取的近似值。本科专业包含双学位和跨学科项目。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Lehigh University
├── College of Arts and Sciences (CAS)                       [学院]
│   ├── Africana Studies                                      [系/项目]
│   ├── Anthropology & Sociology                              [系]
│   ├── Architecture & Design                                 [系]
│   ├── Art, Architecture & Art History                       [系]
│   ├── Biological Sciences                                   [系]
│   ├── Chemistry                                             [系]
│   ├── Classics & Philosophy                                 [系]
│   ├── Cognitive Science                                     [系/跨学科]
│   ├── Computer Science                                      [系]
│   ├── Earth & Environmental Sciences                        [系]
│   ├── Economics                                             [系]
│   ├── English                                               [系]
│   ├── Film & Media Studies                                  [系]
│   ├── History                                               [系]
│   ├── International Relations                               [系]
│   ├── Mathematics                                           [系]
│   ├── Modern Languages & Literatures                        [系]
│   ├── Music & Theatre                                       [系]
│   ├── Physics                                               [系]
│   ├── Political Science                                     [系]
│   ├── Psychology                                            [系]
│   ├── Religion Studies                                      [系]
│   └── Writing & Journalism                                  [系]
├── College of Business                                        [学院]
│   ├── Accounting                                            [系]
│   ├── Finance                                               [系]
│   ├── Management                                            [系]
│   ├── Marketing                                             [系]
│   ├── Supply Chain Management                               [系]
│   ├── Information Systems                                   [系]
│   ├── Real Estate                                           [系]
│   └── Entrepreneurship                                      [系]
├── College of Education                                       [学院]
│   ├── Educational Leadership                                [系]
│   ├── Counseling Psychology                                 [系]
│   ├── Teaching, Learning & Technology                       [系]
│   └── Special Education                                     [系]
├── College of Health                                          [学院]
│   ├── Population Health                                     [系]
│   ├── Community & Global Health                             [系]
│   ├── Biostatistics & Health Data Science                   [系]
│   └── Environmental Health                                  [系]
└── P.C. Rossin College of Engineering & Applied Science       [学院]
    ├── Bioengineering                                        [系]
    ├── Chemical & Biomolecular Engineering                   [系]
    ├── Civil & Environmental Engineering                     [系]
    ├── Computer Science & Engineering                        [系]
    ├── Electrical & Computer Engineering                     [系]
    ├── Industrial & Systems Engineering                      [系]
    ├── Materials Science & Engineering                       [系]
    ├── Mechanical Engineering & Mechanics                    [系]
    └── Data Science                                          [系/跨学科]
```

> 注：Computer Science 同时存在于 CAS（文学士）和 Rossin Engineering（理学士/工程）两个学院。跨学科项目（如 IBE、IDEAS、CSB）横跨多个学院。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~55 |
| BS | Bachelor of Science | 本科 | ~35 |
| BFA | Bachelor of Fine Arts | 本科 | ~3 |
| BSBA | Bachelor of Science in Business Administration | 本科 | ~12 |
| BSE | Bachelor of Science in Engineering | 本科 | ~18 |
| MA | Master of Arts | 研究生 | ~5 |
| MS | Master of Science | 研究生 | ~30 |
| MBA | Master of Business Administration | 研究生 | 3 (Full-Time, Part-Time, MBA+Engineering) |
| MEng | Master of Engineering | 研究生 | ~6 |
| MEd | Master of Education | 研究生 | ~10 |
| PhD | Doctor of Philosophy | 研究生 | ~20 |
| EdD | Doctor of Education | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | ~25 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BSBA/BSE | MA | MS | MBA | MEng | MEd | PhD | EdD | Cert | 合计 |
|------------|----|----|-----|----------|----|----|-----|------|-----|-----|-----|------|------|
| College of Arts and Sciences | ~55 | ~8 | ~3 | 0 | ~3 | ~8 | 0 | 0 | 0 | ~10 | 0 | ~5 | ~92 |
| College of Business | 0 | 0 | 0 | ~12 | 0 | ~3 | 3 | 0 | 0 | 1 | 0 | 1 | ~20 |
| College of Education | 0 | ~2 | 0 | 0 | 0 | ~2 | 0 | 0 | ~7 | ~3 | 1 | ~7 | ~22 |
| College of Health | 0 | ~6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | ~9 |
| P.C. Rossin Engineering | 0 | 0 | 0 | ~18 | 0 | ~16 | 0 | ~6 | 0 | ~10 | 0 | ~8 | ~58 |
| **合计** | ~55 | ~16 | ~3 | ~30 | ~3 | ~29 | 3 | ~6 | ~7 | ~25 | 1 | ~23 | **~201** |

> 注：跨学科项目（如 Financial Engineering, Data Science）按行政归属学院归类。IBE/IDEAS/CSB 等双学位项目归入主导学院。

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

Lehigh University 由 5 个本科学院组成，详见 Section 0.2 层级树。本科生可在学院间选课，鼓励跨学科学习。详见 [Lehigh Academics](https://www2.lehigh.edu/academics/our-approach-to-academics)。

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### College of Arts and Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Anthropology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Architecture | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 4 | Art | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 5 | Art History | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 6 | Asian and Asian American Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 7 | Astronomy | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 8 | Astrophysics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 9 | Biochemistry | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 10 | Biology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 11 | Chemistry | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 12 | Chinese | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 13 | Cognitive Science | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 14 | Computer Science (CAS) | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 15 | Creative Writing | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 16 | Design | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 17 | Documentary Storymaking | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 18 | Earth and Environmental Sciences | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 19 | Economics (CAS) | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 20 | English | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 21 | Environmental Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 22 | Film and Documentary Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 23 | French | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 24 | French and Francophone Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 25 | German Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 26 | Graphic Design | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 27 | Health, Medicine, and Society | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 28 | History | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 29 | International Relations | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 30 | Japanese Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 31 | Jewish Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 32 | Journalism | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 33 | Latin American & Latino Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 34 | Mathematics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 35 | Molecular and Cellular Biology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 36 | Museum Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 37 | Music | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 38 | Neuroscience | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 39 | Philosophy | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 40 | Physics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 41 | Political Science | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 42 | Product Design | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 43 | Psychology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 44 | Religion, Culture and Society | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 45 | Russian | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 46 | Science and Environmental Writing | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 47 | Sociology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 48 | Sociology and Anthropology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 49 | Spanish and Hispanic Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 50 | Studio Art | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 51 | Theatre | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 52 | Women, Gender and Sexuality Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 53 | Writing | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 54 | Global Studies | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 55 | Mass Communication | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 56 | Public Administration | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 57 | Statistics and Data Science | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Astrophysics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Biochemistry | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 4 | Biology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 5 | Chemistry | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 6 | Computer Science (CAS) | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 7 | Mathematics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 8 | Neuroscience | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 9 | Physics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 10 | Psychology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Graphic Design | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Studio Art | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

#### College of Business

##### BSBA (Bachelor of Science in Business Administration)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Business Analytics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Business and Economics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 4 | Business Information Systems | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 5 | Economics (Business) | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 6 | Entrepreneurship | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 7 | Finance | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 8 | International Business | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 9 | Management | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 10 | Marketing | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 11 | Real Estate | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 12 | Supply Chain Management | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

#### College of Education

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Elementary & Secondary Education | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

#### College of Health

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biostatistics & Health Data Science | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Community and Global Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Community Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 4 | Environmental Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 5 | Epidemiology | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 6 | Global Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 7 | Health Policy and Politics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 8 | Indigenous Peoples Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 9 | LGBTQ+ Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 10 | Maternal and Child Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 11 | Population Health | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

#### P.C. Rossin College of Engineering & Applied Science

##### BSE (Bachelor of Science in Engineering)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 2 | Applied Science | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 3 | Bioengineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 4 | Chemical Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 5 | Civil Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 6 | Computer Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 7 | Computer Science (Engineering) | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 8 | Electrical Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 9 | Energy Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 10 | Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 11 | Engineering Mechanics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 12 | Engineering Physics | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 13 | Environmental Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 14 | Industrial and Systems Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 15 | Manufacturing Systems Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 16 | Materials Science and Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 17 | Mechanical Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |
| 18 | Polymer Science and Engineering | https://www2.lehigh.edu/academics/undergraduate-studies/degree-programs |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 项目 | 主导学院 | 合作学院 | 类型 |
|---|------|---------|---------|------|
| 1 | Arts and Engineering | Rossin Engineering | CAS | Dual Degree |
| 2 | Computer Science and Business (CSB) | Rossin Engineering | Business | Joint Major |
| 3 | Integrated Business and Engineering (IBE) | Rossin Engineering | Business | Honors Program |
| 4 | Integrated Business and Health (IBH) | Business | Health | Joint Major |
| 5 | Integrated Degree in Engineering, Arts & Sciences (IDEAS) | Rossin Engineering | CAS | Dual Degree |
| 6 | Health, Medicine, and Society | CAS | Health | Interdisciplinary |
| 7 | Biostatistics & Health Data Science | Health | CAS | Interdisciplinary |
| 8 | Community and Global Health | Health | CAS | Interdisciplinary |
| 9 | Data Science | Rossin Engineering | CAS | Interdisciplinary |
| 10 | Joint International Relations and Economics | CAS | Business | Joint |
| 11 | Joint International Relations and Modern Languages | CAS | CAS | Joint |
| 12 | Joint Global Studies and Modern Languages | CAS | CAS | Joint |
| 13 | Global Citizenship Initiative | University-wide | — | Certificate |

### 1.4 4+1 Accelerated Master's Programs

| # | 项目 | UG 学院 | Grad 学院 |
|---|------|---------|----------|
| 1 | 4+1 Master of Arts in Politics and Policy | CAS | CAS |
| 2 | 4+1 Master of Public Health | CAS/Health | Health |
| 3 | 4+1 Master of Public Policy | CAS | CAS |
| 4 | 4+1 Master of Science in Applied Economics | Business | Business |
| 5 | 4+1 Master of Science in Business Analytics | Business | Business |
| 6 | 4+1 Master's in Engineering | Engineering | Engineering |

### 1.5 Minors — representative list

CAS 提供大量辅修，包括但不限于：Actuarial Science, Aerospace Engineering, Africana Studies, Anthropology, Apparel Design, Applied Mathematics, Architecture Studio, Art History, Art Studio, Asian and Asian American Studies, Astronomy, Biotechnology, Business, Chemistry, Chinese, Cognitive Science, Community Health, Computer Science, Economics, English, Environmental Studies, Film and Documentary Studies, French, German Studies, History, Japanese Studies, Jewish Studies, Journalism, Latin American & Latino Studies, Mathematics, Music, Philosophy, Physics, Political Science, Psychology, Religion, Russian, Sociology, Spanish, Statistics, Theatre, Women Gender and Sexuality Studies, Writing 等。

### 1.6 General Education Requirements

Lehigh 要求所有本科生完成通识教育课程，包括：First-Year Seminar, English Composition, Quantitative Reasoning, Natural Science, Social Science, Humanities, Cross-Cultural Studies 等。详见 [Lehigh University Catalog](http://catalog.lehigh.edu/undergraduatestudies/)。

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### College of Arts and Sciences

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www2.lehigh.edu/academics/graduate-studies/applied-mathematics-ms |
| 2 | Earth & Environmental Sciences | https://www2.lehigh.edu/academics/graduate-studies/earth-environmental-sciences-ms |
| 3 | Molecular Biology | https://www2.lehigh.edu/academics/graduate-studies/molecular-biology-ms |
| 4 | Photonics | https://www2.lehigh.edu/academics/graduate-studies/photonics-ms |
| 5 | Physics | https://www2.lehigh.edu/academics/graduate-studies/physics-ms |
| 6 | Psychology | https://www2.lehigh.edu/academics/graduate-studies/psychology-ms |
| 7 | Statistics and Data Science | https://www2.lehigh.edu/academics/graduate-studies/statistics-and-data-science-ms |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www2.lehigh.edu/academics/graduate-studies/applied-mathematics-phd |
| 2 | Biology | https://www2.lehigh.edu/academics/graduate-studies/biology-phd |
| 3 | Chemistry | https://www2.lehigh.edu/academics/graduate-studies/chemistry-phd |
| 4 | Earth & Environmental Sciences | https://www2.lehigh.edu/academics/graduate-studies/earth-environmental-sciences-phd |
| 5 | English | https://www2.lehigh.edu/academics/graduate-studies/english-phd |
| 6 | History | https://www2.lehigh.edu/academics/graduate-studies/history-phd |
| 7 | Mathematics | https://www2.lehigh.edu/academics/graduate-studies/mathematics-phd |
| 8 | Physics | https://www2.lehigh.edu/academics/graduate-studies/physics-phd |
| 9 | Psychology | https://www2.lehigh.edu/academics/graduate-studies/psychology-phd |

##### Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www2.lehigh.edu/academics/graduate-studies/africana-studies-certificate |
| 2 | Cognitive Science | https://www2.lehigh.edu/academics/graduate-studies/cognitive-science-certificate |
| 3 | Environmental Health | https://www2.lehigh.edu/academics/graduate-studies/environmental-health-certificate |
| 4 | Environmental Justice | https://www2.lehigh.edu/academics/graduate-studies/environmental-justice-certificate |
| 5 | Environmental Policy and Planning | https://www2.lehigh.edu/academics/graduate-studies/environmental-policy-and-planning-certificate |

#### College of Business

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | MBA: Full-Time | https://www2.lehigh.edu/academics/graduate-studies/full-time-mba |
| 2 | MBA: Part-Time | https://www2.lehigh.edu/academics/graduate-studies/mba-part-time-mba |
| 3 | MBA & Engineering (Interdisciplinary) | https://www2.lehigh.edu/academics/graduate-studies/mba-engineering |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Economics | https://www2.lehigh.edu/academics/graduate-studies/applied-economics-ms |
| 2 | Business Analytics | https://www2.lehigh.edu/academics/graduate-studies/business-analytics-ms |
| 3 | Financial Engineering | https://www2.lehigh.edu/academics/graduate-studies/financial-engineering-ms |
| 4 | Management | https://www2.lehigh.edu/academics/graduate-studies/management-ms |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Business & Economics | https://www2.lehigh.edu/academics/graduate-studies/business-economics-phd |

##### Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Leadership | https://www2.lehigh.edu/academics/graduate-studies/leadership-certificate |

#### College of Education

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology | https://www2.lehigh.edu/academics/graduate-studies/counseling-psychology-phd |
| 2 | School Psychology | https://www2.lehigh.edu/academics/graduate-studies/school-psychology-phd |
| 3 | Special Education | https://www2.lehigh.edu/academics/graduate-studies/special-education-phd |
| 4 | Teaching, Learning and Technology | https://www2.lehigh.edu/academics/graduate-studies/teaching-learning-and-technology-phd |

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://www2.lehigh.edu/academics/graduate-studies/educational-leadership-edd |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Behavior Analysis | https://www2.lehigh.edu/academics/graduate-studies/behavior-analysis-med |
| 2 | Educational Leadership | https://www2.lehigh.edu/academics/graduate-studies/educational-leadership-med |
| 3 | Elementary Education and PA Pre-K-4 Teacher Certification | https://www2.lehigh.edu/academics/graduate-studies/elementary-education-and-pa-pre-k-4-teacher-certification-med |
| 4 | International School Counseling | https://www2.lehigh.edu/academics/graduate-studies/international-school-counseling-med |
| 5 | Mental Health Counseling | https://www2.lehigh.edu/academics/graduate-studies/mental-health-counseling-med |
| 6 | School Counseling with PA Certification | https://www2.lehigh.edu/academics/graduate-studies/school-counseling-with-pa-certification-med |
| 7 | Secondary Education and PA 7-12 Teacher Certification | https://www2.lehigh.edu/academics/graduate-studies/secondary-education-and-pa-7-12-teacher-certification-med |
| 8 | Special Education (without certification) | https://www2.lehigh.edu/academics/graduate-studies/special-education-med-without-certification |
| 9 | Teaching & Learning | https://www2.lehigh.edu/academics/graduate-studies/teaching-learning-med |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Instructional Technology | https://www2.lehigh.edu/academics/graduate-studies/instructional-technology-ms |

##### Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Learning Analytics | https://www2.lehigh.edu/academics/graduate-studies/artificial-intelligence-and-learning-analytics-certificate |
| 2 | Behavior Analysis | https://www2.lehigh.edu/academics/graduate-studies/behavior-analysis-certificate |
| 3 | College Admissions Counseling | https://www2.lehigh.edu/academics/graduate-studies/college-admissions-counseling-certificate |
| 4 | Game-Based Learning | https://www2.lehigh.edu/academics/graduate-studies/game-based-learning-certificate |
| 5 | International School Counseling | https://www2.lehigh.edu/academics/graduate-studies/international-school-counseling-certificate |
| 6 | Learning Design for Educational and Professional Settings | https://www2.lehigh.edu/academics/graduate-studies/learning-design-for-educational-and-professional-settings-certificate |
| 7 | Mental Health Counseling for Latin American People in the US | https://www2.lehigh.edu/academics/graduate-studies/mental-health-counseling-for-latin-american-people-in-the-us-certificate |
| 8 | Social, Emotional, and Behavioral Wellness | https://www2.lehigh.edu/academics/graduate-studies/social-emotional-and-behavioral-wellness-certificate |
| 9 | Teaching English to Speakers of Other Languages (TESOL) | https://www2.lehigh.edu/academics/graduate-studies/teaching-english-to-speakers-of-other-languages-tesol-certificate |

#### College of Health

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Population Health | https://www2.lehigh.edu/academics/graduate-studies/population-health-phd |

##### Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Global Health | https://www2.lehigh.edu/academics/graduate-studies/global-health-certificate |
| 2 | Population Health | https://www2.lehigh.edu/academics/graduate-studies/population-health-certificate |

#### P.C. Rossin College of Engineering & Applied Science

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace and Space Systems Engineering | https://www2.lehigh.edu/academics/graduate-studies/aerospace-and-space-systems-engineering-ms |
| 2 | Bioengineering | https://www2.lehigh.edu/academics/graduate-studies/bioengineering-ms |
| 3 | Chemical Engineering | https://www2.lehigh.edu/academics/graduate-studies/chemical-engineering-ms-meng |
| 4 | Civil Engineering | https://www2.lehigh.edu/academics/graduate-studies/civil-engineering-ms |
| 5 | Computer Engineering | https://www2.lehigh.edu/academics/graduate-studies/computer-engineering-ms-meng |
| 6 | Computer Science | https://www2.lehigh.edu/academics/graduate-studies/computer-science-ms |
| 7 | Data Science | https://www2.lehigh.edu/academics/graduate-studies/data-science-ms |
| 8 | Electrical Engineering | https://www2.lehigh.edu/academics/graduate-studies/electrical-engineering-ms-meng |
| 9 | Environmental Engineering | https://www2.lehigh.edu/academics/graduate-studies/environmental-engineering-ms |
| 10 | Health Systems Engineering | https://www2.lehigh.edu/academics/graduate-studies/health-systems-engineering-ms-certificate |
| 11 | Industrial Engineering and Operations Research | https://www2.lehigh.edu/academics/graduate-studies/industrial-engineering-and-operations-research-ms-certificate |
| 12 | Materials Science and Engineering | https://www2.lehigh.edu/academics/graduate-studies/materials-science-and-engineering-ms |
| 13 | Mechanical Engineering | https://www2.lehigh.edu/academics/graduate-studies/mechanical-engineering-ms |
| 14 | Optimization | https://www2.lehigh.edu/academics/graduate-studies/optimization-ms-certificate |
| 15 | Photonics | https://www2.lehigh.edu/academics/graduate-studies/photonics-ms |
| 16 | Polymer Science and Engineering | https://www2.lehigh.edu/academics/graduate-studies/polymer-science-and-engineering-ms-certificate |
| 17 | Statistics and Data Science | https://www2.lehigh.edu/academics/graduate-studies/statistics-and-data-science-ms |
| 18 | Structural Engineering | https://www2.lehigh.edu/academics/graduate-studies/structural-engineering-ms-phd |

##### MEng

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Chemical Engineering | https://www2.lehigh.edu/academics/graduate-studies/biological-chemical-engineering-meng |
| 2 | Chemical Engineering | https://www2.lehigh.edu/academics/graduate-studies/chemical-engineering-ms-meng |
| 3 | Computer Engineering | https://www2.lehigh.edu/academics/graduate-studies/computer-engineering-ms-meng |
| 4 | Electrical Engineering | https://www2.lehigh.edu/academics/graduate-studies/electrical-engineering-ms-meng |
| 5 | Energy Systems Engineering | https://www2.lehigh.edu/academics/graduate-studies/energy-systems-engineering-meng |
| 6 | Structural Engineering | https://www2.lehigh.edu/academics/graduate-studies/structural-engineering-meng |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://www2.lehigh.edu/academics/graduate-studies/bioengineering-phd |
| 2 | Chemical Engineering | https://www2.lehigh.edu/academics/graduate-studies/chemical-engineering-phd |
| 3 | Civil Engineering | https://www2.lehigh.edu/academics/graduate-studies/civil-engineering-phd |
| 4 | Computer Engineering | https://www2.lehigh.edu/academics/graduate-studies/computer-engineering-phd |
| 5 | Computer Science | https://www2.lehigh.edu/academics/graduate-studies/computer-science-phd |
| 6 | Electrical Engineering | https://www2.lehigh.edu/academics/graduate-studies/electrical-engineering-phd |
| 7 | Environmental Engineering | https://www2.lehigh.edu/academics/graduate-studies/environmental-engineering-phd |
| 8 | Industrial and Systems Engineering | https://www2.lehigh.edu/academics/graduate-studies/industrial-and-systems-engineering-phd |
| 9 | Materials Science and Engineering | https://www2.lehigh.edu/academics/graduate-studies/materials-science-and-engineering-phd |
| 10 | Mechanical Engineering | https://www2.lehigh.edu/academics/graduate-studies/mechanical-engineering-phd |
| 11 | Structural Engineering | https://www2.lehigh.edu/academics/graduate-studies/structural-engineering-ms-phd |

##### Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Catastrophe Modeling and Resilience | https://www2.lehigh.edu/academics/graduate-studies/catastrophe-modeling-and-resilience-ms-certificate |
| 2 | Chemical and Biomolecular Engineering | https://www2.lehigh.edu/academics/graduate-studies/chemical-and-biomolecular-engineering-certificate |
| 3 | Health Systems Engineering | https://www2.lehigh.edu/academics/graduate-studies/health-systems-engineering-ms-certificate |
| 4 | Industrial Engineering and Operations Research | https://www2.lehigh.edu/academics/graduate-studies/industrial-engineering-and-operations-research-ms-certificate |
| 5 | Nanotechnology | https://www2.lehigh.edu/academics/graduate-studies/nanotechnology-certificate |
| 6 | Optimization | https://www2.lehigh.edu/academics/graduate-studies/optimization-ms-certificate |
| 7 | Polymer Science and Engineering | https://www2.lehigh.edu/academics/graduate-studies/polymer-science-and-engineering-ms-certificate |
| 8 | Probabilistic Modeling | https://www2.lehigh.edu/academics/graduate-studies/probabilistic-modeling-certificate |

### 2.2 Graduate admissions model

Lehigh 采用分散式研究生招生模式（decentralized）。各学院自行管理招生，但申请统一通过各学院的在线系统提交。

- **申请平台**: 各学院自有在线申请系统
- **申请费**: 因学院而异（详见各项目页面）
- **CGS April 15 荣誉日期**: 遵守 CGS 规范，4月15日前不要求学生接受录取
- **GRE/GMAT 政策**: 因项目而异，部分项目已永久取消 GRE 要求

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common Application | admissions.lehigh.edu/apply |
| ED I 截止日期 | November 1 | admissions.lehigh.edu/apply |
| ED I 通知日期 | Mid December | admissions.lehigh.edu/apply |
| ED II 截止日期 | January 1 | admissions.lehigh.edu/apply |
| ED II 通知日期 | Mid February | admissions.lehigh.edu/apply |
| RD 截止日期 | January 1 | admissions.lehigh.edu/apply |
| RD 通知日期 | Late March | admissions.lehigh.edu/apply |
| 7-Yr BA/DMD-Bio-Dental 截止日期 | January 1 | admissions.lehigh.edu/apply |
| 7-Yr BA/DMD-Bio-Dental 通知日期 | Early April | admissions.lehigh.edu/apply |
| 转学 Fall 截止日期 | April 1 | admissions.lehigh.edu/apply |
| 转学 Fall 通知日期 | Mid May | admissions.lehigh.edu/apply |
| 转学 Spring 截止日期 | November (TBD) | admissions.lehigh.edu/apply |
| SAT/ACT 政策 | Test-Optional (indefinite) | admissions.lehigh.edu/apply |
| Superscore | 支持 SAT 和 ACT superscoring | admissions.lehigh.edu/apply |
| 推荐信 | 需要（通过 Common App 提交） | admissions.lehigh.edu/apply |
| 面试 | 不要求 | admissions.lehigh.edu/apply |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低要求 | 备注 |
|------|---------|------|
| TOEFL iBT | 未公布统一最低分 | 接受 Paper Edition；接受 MyBestScore（6个月内成绩） |
| TOEFL Essentials | 接受 | 可能要求面试 |
| IELTS | 接受 | 未公布统一最低分 |
| Duolingo English Test | 接受 | 未公布统一最低分 |
| C2 Proficiency (Cambridge) | 接受 | — |

> 注：Lehigh 本科招生页面未公布统一的最低英语考试分数。建议联系 admissions@lehigh.edu 或查看具体项目要求。

### 3.3 Graduate — English proficiency requirements by college

| 学院 | TOEFL (Old Scale) | TOEFL (New Scale) | IELTS | Duolingo |
|------|-------------------|-------------------|-------|----------|
| College of Arts and Sciences | Varies by program | Varies by program | Varies | 53+ each band |
| College of Business | Varies by program | Varies by program | Varies | 53+ each band |
| College of Education | Varies by program | Varies by program | Varies | 56+ each band |
| College of Health | Varies by program | Varies by program | Varies | Varies |
| P.C. Rossin Engineering | Varies by program | Varies by program | Varies | Varies |

> 接受的考试：TOEFL iBT, TOEFL Essentials, TOEFL MyBestScore, IELTS, Duolingo English Test, C2 Proficiency (Cambridge)。成绩有效期 2 年。部分项目可能要求面试。详见 [English Proficiency Requirement](https://www2.lehigh.edu/admissions/english-proficiency-requirement-for-graduate-studies)。

### 3.4 Graduate admissions rules

- **申请平台**: 各学院独立申请系统
- **GRE/GMAT**: 因项目而异，部分已取消要求
- **申请费**: 因学院而异
- **条件录取**: 英语成绩未达标者可能获得有条件录取（需完成英语强化课程）

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year)

| 费用项目 | 金额 (USD) | 说明 |
|---------|-----------|------|
| Tuition | $69,420 | 2026-27 学年 |
| Typical first-year housing | $11,470 | 校内住宿 |
| Full meal plan | $7,760 | 全餐计划 |
| Technology fee | $630 | 技术费 |
| Activity fee | $290 | 活动费 |
| Wellness fee | $250 | 健康费 |
| **Total Direct Cost** | **$89,820** | |
| Books and supplies (estimated) | $1,000 | 间接费用 |
| Personal expenses (estimated) | $1,500 | 间接费用 |
| **Total Cost of Attendance** | **~$92,320** | 含间接费用 |

> 特定项目额外收费 $910（Engineering and Science fee, Arts and Sciences fee, 或 Health fee）。
> 来源: https://www2.lehigh.edu/admissions/tuition-affording-college

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Lehigh Commitment（学费减免） | 家庭收入 < $75,000 可获全额学费补助 | tuition-affording-college |
| Need-blind 政策 | 未明确说明（待确认） | — |
| 获得经济援助学生比例 | >50% | tuition-affording-college |
| 奖学金和助学金总额 | $175M | tuition-affording-college |
| Merit 奖学金 | 2024-25 年录取学生中，Merit 奖学金 ≥ $15,000/年 | tuition-affording-college |
| 毕业生起薪 | $77,000 | tuition-affording-college |
| PayScale 排名 | Best Universities for a Bachelor's Degree | tuition-affording-college |

### 4.3 Graduate cost & funding framework

| 维度 | 说明 |
|------|------|
| 资助类型 | 全额资助 / 部分资助 / 自费（因项目而异） |
| 常见资助形式 | RA (Research Assistantship), TA (Teaching Assistantship), Fellowship, Grant |
| 申请费 | 因学院而异 |
| 费用减免政策 | 部分项目提供申请费减免 |

> 注：研究生学费和资助信息分散在各学院网站，需按项目查询。

---

## SECTION 5 — Evidence chain index

### E-U-001: ED I Deadline
```yaml
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Early Decision I Deadline: November 1 Decision Date: Mid December"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-002: ED II Deadline
```yaml
field: undergraduate.deadlines.ED_II
value: "January 1"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Early Decision II Deadline: January 1 Decision Date: Mid February"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: "January 1"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Regular Decision Deadline: January 1 Decision Date: Late March"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: Test-Optional Policy
```yaml
field: undergraduate.testing.test_optional
value: "Indefinite test-optional policy"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Lehigh will extend the test optional policy for admission indefinitely while continuing to evaluate its impact. This allows first-year applicants and transfer applicants to choose whether or not to submit SAT or ACT test scores for consideration."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: Superscore Policy
```yaml
field: undergraduate.testing.superscore
value: "SAT and ACT superscoring supported"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "If you take the SAT or ACT across multiple test dates, we will \"superscore\" and use your top score for the exam."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-006: Tuition 2026-27
```yaml
field: undergraduate.cost.tuition_2026_2027
value: "$69,420"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Tuition $69,420"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-007: Housing Cost
```yaml
field: undergraduate.cost.housing_2026_2027
value: "$11,470"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Typical first-year housing $11,470"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-008: Meal Plan Cost
```yaml
field: undergraduate.cost.meal_plan_2026_2027
value: "$7,760"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Full meal plan $7,760"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-009: Total Cost of Attendance
```yaml
field: undergraduate.cost.total_2026_2027
value: "$89,820 (direct costs)"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Total Cost** $89,820"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-010: Lehigh Commitment
```yaml
field: undergraduate.financial_aid.lehigh_commitment
value: "Families with income < $75,000 eligible for full tuition grant"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "100% of undergraduate students from families with a total income of less than $75,000 are eligible for a full tuition grant (the family will pay no tuition) through the Lehigh Commitment"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-011: Merit Scholarships
```yaml
field: undergraduate.financial_aid.merit_scholarships
value: "Merit scholarship ≥ $15,000/year for 2024-25 admitted students"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "of the admitted students for 2024-25 year received a merit scholarship of $15,000 or more per year"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-012: Financial Aid Recipients
```yaml
field: undergraduate.financial_aid.recipients_percentage
value: ">50%"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: ">50% of current students receive some form of financial aid"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-013: Graduate Salary
```yaml
field: undergraduate.outcomes.starting_salary
value: "$77,000"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Graduate Starting Salary $77K"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-014: Application System
```yaml
field: undergraduate.application.platform
value: "Common Application"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Lehigh is a partner of the Common Application for current applicants."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-015: College Structure
```yaml
field: institution.colleges
value: "5 colleges: Arts & Sciences, Business, Education, Health, P.C. Rossin Engineering"
source_url: https://www2.lehigh.edu/academics/our-approach-to-academics
source_snippet: "Our Colleges: College of Arts & Sciences, College of Business, College of Education, College of Health, P.C. Rossin College of Engineering & Applied Science"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-016: Transfer Fall Deadline
```yaml
field: undergraduate.deadlines.transfer_fall
value: "April 1"
source_url: https://www2.lehigh.edu/admissions/apply
source_snippet: "Transfer Student (Fall) Deadline: April 1 Decision Date: Mid May"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-017: English Proficiency Tests Accepted
```yaml
field: graduate.testing.english_proficiency
value: "TOEFL iBT, TOEFL Essentials, TOEFL MyBestScore, IELTS, Duolingo, C2 Proficiency"
source_url: https://www2.lehigh.edu/admissions/english-proficiency-requirement-for-graduate-studies
source_snippet: "Lehigh offers multiple paths to demonstrate English language proficiency... TOEFL iBT, TOEFL Essentials, TOEFL MyBestScore, IELTS, Duolingo English Test, C2 Proficiency"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-018: Additional Program Fees
```yaml
field: undergraduate.cost.additional_fees
value: "$910 for certain programs (Engineering/Science, Arts & Sciences, or Health fee)"
source_url: https://www2.lehigh.edu/admissions/tuition-affording-college
source_snippet: "Students in certain programs and majors are assessed an additional $910 fee (Engineering and Science fee, Arts and Sciences fee or Health fee)."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001: Graduate Programs Directory
```yaml
field: graduate.programs.directory
value: "Full list of graduate programs across 5 colleges"
source_url: https://www2.lehigh.edu/academics/graduate-studies/degree-programs
source_snippet: "Lehigh University offers nationally recognized, research-based Ph.D. programs and professional master's degree and certificate programs."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-002: Graduate Decentralized Model
```yaml
field: graduate.admissions.model
value: "Decentralized - each college manages own admissions"
source_url: https://www2.lehigh.edu/admissions/graduate
source_snippet: "Graduate Admissions: Applying to Graduate Studies, Funding Your Graduate Education, English Proficiency Requirement for Graduate Studies"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
lehigh-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, matrix
├── 01-undergraduate-cas.md             # Section 1: CAS programs
├── 02-undergraduate-business.md        # Section 1: Business programs
├── 03-undergraduate-education.md       # Section 1: Education programs
├── 04-undergraduate-health.md          # Section 1: Health programs
├── 05-undergraduate-engineering.md     # Section 1: Engineering programs
├── 06-undergraduate-interdisciplinary.md # Section 1: Joint/interdisciplinary
├── 07-graduate-cas.md                  # Section 2: CAS graduate programs
├── 08-graduate-business.md             # Section 2: Business graduate programs
├── 09-graduate-education.md            # Section 2: Education graduate programs
├── 10-graduate-health.md               # Section 2: Health graduate programs
├── 11-graduate-engineering.md          # Section 2: Engineering graduate programs
├── 12-deadlines-requirements.md        # Section 3: Application requirements
├── 13-costs-financial-aid.md           # Section 4: Costs and aid
├── 14-evidence-chain.md                # Section 5: Evidence index
└── 15-comparison-framework.md          # Section 7: Cross-school comparison
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "lehigh-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BSE|BSBA|MS|MBA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL |
|--------|--------|---------|
| P0 | 本科英语考试最低分数（按学院） | admissions.lehigh.edu/international-students |
| P0 | 研究生英语考试最低分数（精确数值） | admissions.lehigh/english-proficiency-requirement-for-graduate-studies |
| P0 | 各研究生项目具体申请费 | 各学院申请页面 |
| P1 | 精确的 UG 专业计数（含辅修） | catalog.lehigh.edu/programsandmajors/ |
| P1 | 录取率和 GPA 数据 | admissions/admission-statistics |
| P1 | Need-blind 政策（是否适用于国际生） | financial-aid 页面 |
| P2 | 各研究生项目 GRE/GMAT 具体要求 | 各项目详情页 |
| P2 | 校内住宿详细选项和费用 | housing 页面 |
| P2 | 国际生签证和 I-20 流程 | international-students 页面 |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Lehigh University |
|------|-------------------|
| 位置 | Bethlehem, PA |
| 类型 | Private Research University |
| 本科学费/年 | $69,420 (2026-27) |
| 总费用/年 | $89,820 (direct) |
| Need-blind (国际生) | TBD |
| EA 截止日期 | N/A (无 EA) |
| ED I 截止日期 | November 1 |
| ED II 截止日期 | January 1 |
| RD 截止日期 | January 1 |
| SAT/ACT 要求 | Test-Optional (indefinite) |
| TOEFL 最低 | TBD (varies by program) |
| IELTS 最低 | TBD (varies by program) |
| 学费减免门槛 | $75,000 family income |
| 中位实际支付价 | TBD |
| 研究生申请费 | Varies by college |
| 专业总数 (Rule 1) | ~205 |
| 学院数 (Rule 2) | 5 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: www2.lehigh.edu, catalog.lehigh.edu
> **Verification**: curl + Python DOM extraction (browser automation unavailable)
> **Granularity**: school → department → degree-level → program
> **Note**: Safety classifier intermittently unavailable during capture; some data points marked TBD require follow-up verification. All extracted data verified against multiple page loads.
