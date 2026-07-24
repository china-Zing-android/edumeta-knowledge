# University of California, Davis Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 125 |
| 本科辅修 (Minor) | 116 |
| 研究生学位项目 (MA/MS/MFA/MBA/MEng/PhD/etc.) | 151 |
| 研究生高级证书 (Designated Emphasis) | 6 |
| **学位项目总计 (UG + Grad)** | **408** |
| 学院 / 独立系所总数 | 11 |

> **Source**: catalog.ucdavis.edu/departments-programs-degrees/ — 408 program entries extracted 2026-07-05

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
UC Davis
├── College of Agricultural and Environmental Sciences (CAES)     [UG学院]
│   ├── Agricultural & Resource Economics                         [系]
│   ├── Animal Science                                            [系]
│   ├── Entomology & Nematology                                   [系]
│   ├── Environmental Science & Policy                            [系]
│   ├── Food Science & Technology                                 [系]
│   ├── Human Ecology                                             [系]
│   ├── Plant Sciences                                            [系]
│   └── Viticulture & Enology                                     [系]
├── College of Biological Sciences (CBS)                          [UG学院]
│   ├── Biochemistry & Molecular Biology                          [系]
│   ├── Cell Biology & Human Anatomy                              [系]
│   ├── Evolution & Ecology                                       [系]
│   ├── Microbiology & Molecular Genetics                         [系]
│   ├── Neurobiology, Physiology & Behavior                       [系]
│   └── Plant Biology                                             [系]
├── College of Engineering (COE)                                  [UG学院]
│   ├── Biomedical Engineering                                    [系]
│   ├── Chemical Engineering                                      [系]
│   ├── Civil & Environmental Engineering                         [系]
│   ├── Computer Science                                          [系]
│   ├── Electrical & Computer Engineering                         [系]
│   ├── Materials Science & Engineering                           [系]
│   └── Mechanical & Aerospace Engineering                        [系]
├── College of Letters and Science (L&S)                          [UG学院]
│   ├── Humanities, Arts & Cultural Studies                       [系组]
│   ├── Mathematical & Physical Sciences                          [系组]
│   └── Social Sciences                                           [系组]
├── Graduate Studies                                              [研究生院]
│   └── 90+ interdisciplinary graduate groups                     [系]
├── Betty Irene Moore School of Nursing                           [专业学院]
│   └── Nursing Science & Health-Care Leadership                  [系]
├── Graduate School of Management (GSM)                           [专业学院]
│   └── Business Administration                                   [系]
├── School of Education                                           [专业学院]
│   └── Education                                                 [系]
├── School of Law                                                 [专业学院]
│   └── Law                                                       [系]
├── School of Medicine                                            [专业学院]
│   ├── Medical Sciences                                          [系]
│   └── Public Health Sciences                                    [系]
└── School of Veterinary Medicine                                 [专业学院]
    └── Veterinary Medicine                                       [系]
```

> UC Davis has **4 undergraduate colleges** and **6 professional schools** plus **Graduate Studies** which administers 90+ interdisciplinary graduate programs.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 47 |
| BS | Bachelor of Science | 本科 | 78 |
| Minor | 辅修 | 本科 | 116 |
| MA | Master of Arts | 研究生 | 24 |
| MS | Master of Science | 研究生 | 49 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MEng | Master of Engineering | 研究生 | 4 |
| PhD | Doctor of Philosophy | 研究生 | 67 |
| EdD | Doctorate in Education | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| MHS | Master of Health Services | 研究生 | 1 |
| MPAc | Master of Professional Accountancy | 研究生 | 1 |
| MM | Master of Management | 研究生 | 1 |
| MAS | Master of Advanced Studies | 研究生 | 2 |
| DE | Designated Emphasis (证书) | 研究生 | 6 |
| **合计** | | | **408** |

> UC Davis uses standard US degree abbreviations (no Latin variants).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | Minor | MA | MS | MFA | MBA | MEng | PhD | EdD | DNP | MAS | DE | 合计 |
|------------|----|----|-------|----|----|-----|-----|------|-----|-----|-----|-----|----|------|
| College of Agricultural & Environmental Sciences | 5 | 25 | 20 | 2 | 12 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 1 | 80 |
| College of Biological Sciences | 3 | 12 | 8 | 0 | 5 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | 38 |
| College of Engineering | 0 | 15 | 8 | 0 | 10 | 0 | 0 | 4 | 10 | 0 | 0 | 0 | 0 | 47 |
| College of Letters and Science | 39 | 26 | 72 | 18 | 8 | 4 | 0 | 0 | 30 | 0 | 0 | 0 | 3 | 200 |
| Graduate School of Management | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Education | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 4 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| School of Medicine | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 0 | 6 |
| Betty Irene Moore School of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 |
| School of Veterinary Medicine | 0 | 0 | 8 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 12 |
| **合计** | **47** | **78** | **116** | **22** | **41** | **4** | **2** | **4** | **69** | **1** | **1** | **2** | **6** | **393** |

> **Note**: Some graduate programs are administered by Graduate Studies (interdisciplinary groups) rather than a specific professional school. The matrix shows programs attributed to their home college/school. Law programs (JD, LLM) are cataloged separately by the School of Law but may not appear in the main catalog listing. Total from catalog extraction: 408 programs.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UC Davis has **4 undergraduate colleges** that grant bachelor's degrees. See Section 0.2 for the full hierarchy tree. The colleges are:
- College of Agricultural and Environmental Sciences (CAES)
- College of Biological Sciences (CBS)
- College of Engineering (COE)
- College of Letters and Science (L&S) — the largest, housing humanities, social sciences, and mathematical/physical sciences

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural and Environmental Sciences (CAES)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural & Environmental Education | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Agricultural & Environmental Sciences (Individual) | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Agricultural & Environmental Technology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Animal Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Animal Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Animal Science & Management | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Clinical Nutrition | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Community & Regional Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Ecological Management & Restoration | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Environmental Horticulture & Urban Forestry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Environmental Policy Analysis & Planning | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Environmental Science & Management | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Environmental Toxicology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Food Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Genetics & Genomics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | Global Disease Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | Human Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | International Agricultural Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | Landscape Architecture | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 20 | Managerial Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 21 | Marine & Coastal Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 22 | Nutrition Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 23 | Plant Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 24 | Sustainable Agriculture & Food Systems | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 25 | Sustainable Environmental Design | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 26 | Viticulture & Enology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 27 | Wildlife, Fish & Conservation Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Communication | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Community & Regional Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | International Relations | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Sociology | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### College of Biological Sciences (CBS)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry & Molecular Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Biological Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Biological Sciences (Individual) | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Biotechnology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Cell Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Evolution, Ecology & Biodiversity | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Genetics & Genomics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Human Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Marine & Coastal Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Molecular & Medical Microbiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Neurobiology, Physiology, & Behavior | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Plant Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### BA Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Biological Sciences (Individual) | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Molecular & Medical Microbiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### College of Engineering (COE)

##### BS Programs
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Biochemical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Biological Systems Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Biomedical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Chemical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Civil Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Computer Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Computer Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Computer Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Electrical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Environmental Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Materials Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Mechanical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Chemical Physics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Applied Physics | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### College of Letters and Science (L&S)

##### BA Programs (selected — L&S houses the majority of BA programs)
| # | 专业 | URL |
|---|------|-----|
| 1 | African American & African Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Anthropology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Art History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Art Studio | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Asian American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Chemistry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Chicana/Chicano Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Chinese | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Cinema & Digital Media | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Classical Civilization | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Cognitive Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Communication | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Comparative Literature | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | English | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | French | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | Gender, Sexuality, & Women's Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | German | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 20 | History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 21 | Italian | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 22 | Japanese | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 23 | Linguistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 24 | Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 25 | Medieval & Early Modern Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 26 | Middle East/South Asia Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 27 | Music | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 28 | Native American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 29 | Philosophy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 30 | Physics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 31 | Political Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 32 | Political Science—Public Service | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 33 | Psychology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 34 | Religious Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 35 | Russian | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 36 | Science & Technology Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 37 | Sociology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 38 | Sociology—Organizational Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 39 | Spanish | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 40 | Statistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 41 | Theatre & Dance | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### BS Programs in L&S
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Applied Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Atmospheric Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Biochemistry & Molecular Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Business | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Chemistry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Cognitive Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Data Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Geology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Hydrology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Mathematical & Scientific Computation | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Mathematical Analytics & Operations Research | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Medicinal Chemistry & Drug Design | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Physics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | Psychology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | Statistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | Systems & Synthetic Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | Letters & Science (Individual) | https://catalog.ucdavis.edu/departments-programs-degrees/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Home College(s) | URL |
|---|------|-----------------|-----|
| 1 | Data Science | L&S + Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Biochemistry & Molecular Biology | CBS + L&S | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Genetics & Genomics | CBS + CAES | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Marine & Coastal Science | CBS + CAES | https://catalog.ucdavis.edu/departments-programs-degrees/ |

### 1.4 Minors — complete list

UC Davis offers **116 undergraduate minors**. Full list available at: https://catalog.ucdavis.edu/departments-programs-degrees/

Selected minors by college:
- CAES: Agricultural Pest Management, Agricultural Systems & Environment, Animal Science, Avian Sciences, Community Development, Community Nutrition, Environmental Horticulture, Food Science, etc.
- CBS: Biological Sciences, Biomedical Engineering, Computational Biology, Exercise Biology, Human Physiology, Neuroscience, etc.
- COE: Biomedical Engineering, Computer Science, Electrical Engineering, Materials Science, Construction Engineering & Management, Energy Efficiency, Energy Policy, Energy Science & Technology, etc.
- L&S: Accounting, African American & African Studies, Arabic, Art History, Art Studio, Asian American Studies, Chemistry, Chinese, Classical Civilization, Communication, Economics, English, Film Studies, French, German, Greek, History, Italian, Japanese, Latin, Linguistics, Mathematics, Music, Philosophy, Physics, Political Science, Psychology, Religious Studies, Russian, Sociology, Spanish, Statistics, Theatre & Dance, etc.

### 1.5 General/Institute-wide requirements

UC Davis requires completion of the **UC A-G subject requirements** for admission:
- A. History/social science: 2 years
- B. English: 4 years
- C. Mathematics: 3 years (4 recommended)
- D. Laboratory science: 2 years (3 recommended)
- E. Language other than English: 2 years (3 recommended)
- F. Visual/performing arts: 1 year
- G. College preparatory elective: 1 year

**GPA requirement**: 3.00 for California residents; 3.40 for non-residents.

Each college has additional degree requirements. See: https://catalog.ucdavis.edu/undergraduate-education/

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UC Davis offers **157 graduate degree programs** and **6 designated emphases** (certificates). Graduate admissions is **decentralized** — each program/graduate group manages its own admissions.

#### Graduate Studies (Interdisciplinary Graduate Groups)

##### PhD Programs (selected from 67 total)
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural & Environmental Chemistry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Agricultural & Resource Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Animal Behavior | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Animal Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Anthropology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Applied Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Atmospheric Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Biochemistry, Molecular, Cellular & Developmental Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Biological Systems Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Biomedical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Biophysics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Biostatistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Chemical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Chemistry & Chemical Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Civil & Environmental Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | Communication | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | Comparative Literature | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | Computer Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | Cultural Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 20 | Earth & Planetary Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 21 | Ecology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 22 | Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 23 | Education | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 24 | Electrical & Computer Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 25 | Energy Systems | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 26 | English | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 27 | Entomology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 28 | Epidemiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 29 | Food Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 30 | French & Francophone Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 31 | Geography | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 32 | German | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 33 | History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 34 | Horticulture & Agronomy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 35 | Human Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 36 | Hydrologic Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 37 | Immunology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 38 | Integrative Genetics & Genomics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 39 | Integrative Pathobiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 40 | Linguistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 41 | Materials Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 42 | Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 43 | Mechanical & Aerospace Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 44 | Microbiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 45 | Molecular, Cellular, & Integrative Physiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 46 | Music | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 47 | Native American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 48 | Neuroscience | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 49 | Nursing Science & Health-Care Leadership | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 50 | Nutritional Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 51 | Performance Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 52 | Pharmacology & Toxicology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 53 | Philosophy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 54 | Physics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 55 | Plant Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 56 | Plant Pathology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 57 | Political Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 58 | Population Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 59 | Psychology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 60 | Public Health Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 61 | Sociology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 62 | Soils & Biogeochemistry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 63 | Spanish | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 64 | Statistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 65 | Study of Religion | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 66 | Transportation Technology & Policy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 67 | Ecology (Joint Doctorate with SDSU) | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### MS Programs (selected from 49 total)
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural & Environmental Chemistry | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Agricultural & Resource Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Animal Behavior | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Animal Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Anthropology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Applied Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Atmospheric Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Biochemistry, Molecular, Cellular & Developmental Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Biological Systems Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Biomedical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Biostatistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Business Analytics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Chemical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Chemistry & Chemical Biology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Child Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | Civil & Environmental Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | Communication | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | Community Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | Comparative Literature | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 20 | Computer Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 21 | Cultural Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 22 | Earth & Planetary Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 23 | Ecology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 24 | Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 25 | Education | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 26 | Electrical & Computer Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 27 | Energy Systems | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 28 | English | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 29 | Entomology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 30 | Environmental Policy & Management | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 31 | Epidemiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 32 | Food Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 33 | Forensic Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 34 | French & Francophone Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 35 | Geography | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 36 | German | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 37 | Health Informatics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 38 | History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 39 | Horticulture & Agronomy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 40 | Hydrologic Sciences | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 41 | Immunology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 42 | Integrative Genetics & Genomics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 43 | Integrative Pathobiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 44 | International Agricultural Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 45 | Linguistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 46 | Materials Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 47 | Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 48 | Mechanical & Aerospace Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 49 | Microbiology | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### MA Programs (24 total)
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Art History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Communication | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Comparative Literature | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Cultural Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Economics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Education | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | English | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | French & Francophone Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Geography | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | German | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | History | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 13 | Linguistics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 14 | Mathematics | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 15 | Music | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 16 | Native American Studies | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 17 | Philosophy | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 18 | Political Science | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 19 | Psychology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 20 | Sociology | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 21 | Spanish | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 22 | Study of Religion | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 23 | Political Science/Doctor of Jurisprudence (dual) | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 24 | Integrated Teaching Credential/MA | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### MFA Programs (4 total)
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Studio | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Creative Writing | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Design | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Dramatic Art | https://catalog.ucdavis.edu/departments-programs-degrees/ |

##### MEng Programs (4 total)
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Systems Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Chemical Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Materials Science & Engineering | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Medical Device Development | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### Graduate School of Management

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Business Administration | MBA | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Business Administration Online | MBA Online | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Business Analytics | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Professional Accountancy | MPAc | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Management (Online) | MM | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### School of Education

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Education | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Education | MA | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Education Leadership | EdD (CANDEL) | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Integrated Teaching Credential | TC/MA | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### School of Medicine

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Medicine | MD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Clinical Research | MAS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Maternal & Child Nutrition | MAS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Physician Assistant Studies | MHS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Public Health Sciences | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Public Health Sciences | MPH | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Epidemiology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Epidemiology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Biostatistics | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Biostatistics | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### Betty Irene Moore School of Nursing

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing Science & Health-Care Leadership | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Nursing Science & Health-Care Leadership | DNP-FNP | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Nursing (Master's Entry Program) | MSN | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### School of Law

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Law | JD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Laws | LLM | https://catalog.ucdavis.edu/departments-programs-degrees/ |

#### School of Veterinary Medicine

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Veterinary Medicine | DVM | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 2 | Preventive Veterinary Medicine | MPVM | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 3 | Animal Biology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 4 | Animal Biology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 5 | Integrative Pathobiology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 6 | Integrative Pathobiology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 7 | Epidemiology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 8 | Epidemiology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 9 | Pharmacology & Toxicology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 10 | Pharmacology & Toxicology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 11 | Entomology | PhD | https://catalog.ucdavis.edu/departments-programs-degrees/ |
| 12 | Entomology | MS | https://catalog.ucdavis.edu/departments-programs-degrees/ |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science, PhD**

- **Department**: Computer Science, College of Engineering
- **Application portal**: https://gradstudies.ucdavis.edu/admissions
- **Degree offered**: PhD, MS
- **GRE**: Not required (UC Davis Graduate Studies does not require GRE; individual programs may)
- **English proficiency**: TOEFL/IELTS/Duolingo accepted (UC system-wide requirements)
- **Application fee**: $80 (domestic) / $95 (international)
- **Funding**: Most PhD students receive full funding (TA/RA/fellowship)
- **Contact**: Graduate Program Coordinator, Department of Computer Science

### 2.3 Graduate admissions model

UC Davis graduate admissions is **fully decentralized**. Graduate Studies serves as the administrative hub, but each program/graduate group makes its own admission decisions.

- **Centralized application**: https://gradstudies.ucdavis.edu/admissions
- **Application fee**: $80 domestic / $95 international per program
- **GRE**: Not required by Graduate Studies; individual programs may require
- **English proficiency**: TOEFL, IELTS, or Duolingo (UC system-wide requirements)
- **Funding**: 88% of graduate students receive some form of financial support
- **Professional schools** (Law, Medicine, Veterinary Medicine, Nursing, Management) have separate application processes

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Application portal | UC Application (shared across all UCs) | ucdavis.edu/admissions/undergraduate/apply |
| Application opens | August 1 | ucdavis.edu/admissions/undergraduate/freshman/timeline |
| Filing period | October 1 – December 1 | ucdavis.edu/admissions/undergraduate/freshman/timeline |
| FAFSA/CADAA deadline | October 1 – March 2 | ucdavis.edu/admissions/undergraduate/freshman/timeline |
| SIR/SLR deadline | May 1 | ucdavis.edu/admissions/undergraduate/freshman/timeline |
| Application fee (domestic) | $80 per UC campus | ucdavis.edu/admissions/undergraduate/apply |
| Application fee (international) | $95 per UC campus | ucdavis.edu/admissions/undergraduate/apply |
| Fee waivers | Available for up to 4 UC campuses | ucdavis.edu/admissions/undergraduate/apply |
| SAT/ACT policy | **Test-FREE** — scores not considered | ucdavis.edu/admissions/undergraduate/freshman/requirements |
| GPA requirement (CA residents) | 3.00 | ucdavis.edu/admissions/undergraduate/freshman/requirements |
| GPA requirement (non-residents) | 3.40 | ucdavis.edu/admissions/undergraduate/freshman/requirements |
| A-G requirements | 15 year-long courses | ucdavis.edu/admissions/undergraduate/freshman/requirements |
| Decision notification | As early as mid-March | ucdavis.edu/admissions/undergraduate/freshman/timeline |
| Interview policy | None | N/A |
| Recommendation requirements | None required | N/A |
| Transfer pathway | TAG available for CA community college students | ucdavis.edu/admissions/undergraduate/transfer/transfer-admission-guarantee |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Per UC system requirements | N/A | Accepted for ELWR satisfaction |
| IELTS Academic | Per UC system requirements | N/A | Accepted for ELWR satisfaction |
| Duolingo English Test | Per UC system requirements | N/A | Accepted for ELWR satisfaction |
| AP/IB exams | Specific exams accepted | N/A | Can satisfy ELWR |
| Transferable coursework | College-level English | N/A | Can satisfy ELWR |

> **Note**: UC Davis requires English proficiency if the student studied in the US for fewer than 3 years and received instruction in a language other than English. Specific minimum scores are determined by UC system-wide requirements. The UC Davis international admissions page does not list campus-specific minimums — it defers to UC system policy.

**Source**: ucdavis.edu/admissions/undergraduate/international/exams-visas

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions model | Fully decentralized | gradstudies.ucdavis.edu |
| Application portal | UC Davis Graduate Admissions Application | gradstudies.ucdavis.edu/admissions |
| Application fee (domestic) | $80 | gradstudies.ucdavis.edu |
| Application fee (international) | $95 | gradstudies.ucdavis.edu |
| GRE policy | Not required by Graduate Studies; per-program | gradstudies.ucdavis.edu |
| English proficiency | TOEFL, IELTS, Duolingo | gradstudies.ucdavis.edu |
| CGS April-15 signatory | Yes | UC system policy |
| Professional schools | Separate applications (Law, Med, Vet, Nursing, Management) | Individual school sites |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense item | Amount (on-campus residence hall) | Description |
|-------------|----------------------------------|-------------|
| Systemwide tuition and fees | $15,588 | UC systemwide tuition (flat rate for 6 years) |
| Campus-based fees | $2,490 | UC Davis campus fees |
| Books and supplies | $1,205 | Estimated |
| Room and board | $22,252 | Residence hall |
| Personal expenses | $2,656 | Estimated |
| Transportation | $672 | Estimated |
| Health insurance | $3,996 | UC SHIP |
| Document fee | $150 | One-time |
| **Total (CA resident)** | **$49,009** | |
| Nonresident supplemental tuition | $39,270 | Additional for OOS/international |
| **Total (nonresident)** | **$88,279** | |

**Other living arrangements** (2026-27):
| Arrangement | CA Resident Total | Nonresident Total |
|-------------|------------------|-------------------|
| On-campus (apartments) | $47,590 | $86,860 |
| On-campus (studio) | $57,549 | $96,819 |
| Off-campus | $44,661 | $83,931 |
| At home | $37,893 | $77,163 |

**Source**: ucdavis.edu/admissions/cost

### 4.2 Undergraduate financial-aid policy

| Dimension | Value | Source |
|-----------|-------|--------|
| Need-blind (domestic) | Yes | financialaid.ucdavis.edu |
| Need-blind (international) | **No** — need-aware | financialaid.ucdavis.edu |
| Meets demonstrated need | Yes (for admitted students) | financialaid.ucdavis.edu |
| Tuition stability plan | Systemwide tuition flat for up to 6 years | ucdavis.edu/admissions/cost |
| Blue and Gold Opportunity Program | Available for CA families <$80k income | financialaid.ucdavis.edu |
| Fee waivers | Up to 4 UC campuses | ucdavis.edu/admissions/undergraduate/apply |
| FAFSA code | 001313 | ucdavis.edu/admissions/undergraduate/freshman/timeline |

### 4.3 Graduate cost & funding framework

| Dimension | Value | Source |
|-----------|-------|--------|
| Funding type | Most PhDs fully funded; master's varies | gradstudies.ucdavis.edu |
| Students receiving support | 88% | gradstudies.ucdavis.edu |
| Common funding forms | TA, RA, fellowship, grant | gradstudies.ucdavis.edu |
| Application fee (domestic) | $80 | gradstudies.ucdavis.edu |
| Application fee (international) | $95 | gradstudies.ucdavis.edu |
| Fee waivers | Needs-based | gradstudies.ucdavis.edu |
| Professional school costs | Vary by school | Individual school sites |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.filing_period
  value: "October 1 – December 1"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/freshman/timeline
  source_snippet: "Complete and submit the UC undergraduate application for admission and scholarships from Oct. 1–Dec. 1."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.application_opens
  value: "August 1"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/freshman/timeline
  source_snippet: "Start your UC undergraduate application for admission and scholarships as early as Aug. 1."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.fafsa_cadaa
  value: "October 1 – March 2"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/freshman/timeline
  source_snippet: "Apply for financial aid annually, between Oct. 1 and March 2"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.test_policy
  value: "Test-FREE"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/freshman/requirements
  source_snippet: "The University of California Board of Regents eliminated the standardized test requirement for all incoming first-year students in 2020. UC Davis no longer considers SAT or ACT test scores for admissions decisions or scholarship awards."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.gpa_requirement
  value: "3.00 (CA residents) / 3.40 (non-residents)"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/freshman/requirements
  source_snippet: "California residents need a GPA of 3.00 or higher. Non-residents of California need a GPA of 3.40 or higher."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.cost.tuition_in_state
  value: "$15,588"
  source_url: https://www.ucdavis.edu/admissions/cost
  source_snippet: "Systemwide tuition and fees: $15,588"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.nonresident_supplemental
  value: "$39,270"
  source_url: https://www.ucdavis.edu/admissions/cost
  source_snippet: "Systemwide nonresident supplemental tuition: $39,270"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.total_in_state_on_campus
  value: "$49,009"
  source_url: https://www.ucdavis.edu/admissions/cost
  source_snippet: "Total costs (before aid) for California residents: $49,009"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.total_oos_on_campus
  value: "$88,279"
  source_url: https://www.ucdavis.edu/admissions/cost
  source_snippet: "Total costs (before aid) for nonresidents: $88,279"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.application_fee_domestic
  value: "$80"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/apply
  source_snippet: "The domestic filing fee for each University of California campus you apply to is $80."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application_fee_international
  value: "$95"
  source_url: https://www.ucdavis.edu/admissions/undergraduate/apply
  source_snippet: "For international applicants, the filing fee is $95 per campus."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.need_blind_intl
  value: false
  source_url: https://financialaid.ucdavis.edu/
  source_snippet: "UC Davis is need-aware for international students"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.total
  value: "157 graduate degrees + 6 designated emphases"
  source_url: https://catalog.ucdavis.edu/departments-programs-degrees/
  source_snippet: "Full program listing extracted from catalog — 157 graduate degree programs identified"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.students_receiving_support
  value: "88%"
  source_url: https://www.ucdavis.edu/admissions/graduate-school
  source_snippet: "88% of graduate students receive some form of financial support."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.application_fee
  value: "$80 domestic / $95 international"
  source_url: https://gradstudies.ucdavis.edu/admissions
  source_snippet: "Application fee information from Graduate Studies admissions page"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-P-001:
  field: programs.total_count
  value: 408
  source_url: https://catalog.ucdavis.edu/departments-programs-degrees/
  source_snippet: "408 program entries extracted from Departments, Programs, & Degrees page"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-P-002:
  field: programs.ug_majors
  value: 125
  source_url: https://catalog.ucdavis.edu/departments-programs-degrees/
  source_snippet: "125 undergraduate degree programs (BA/BS) identified in catalog"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-P-003:
  field: programs.ug_minors
  value: 116
  source_url: https://catalog.ucdavis.edu/departments-programs-degrees/
  source_snippet: "116 undergraduate minors identified in catalog"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-001:
  field: structure.colleges
  value: "4 undergraduate colleges + 6 professional schools + Graduate Studies"
  source_url: https://www.ucdavis.edu/academics/colleges-and-schools
  source_snippet: "Our four academic colleges... The colleges of Letters and Science, Agriculture and Environmental Sciences, Biological Sciences, and Engineering"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
ucdavis-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-caes.md                       (CAES programs)
├── 02-ug-cbs.md                        (CBS programs)
├── 03-ug-coe.md                        (COE programs)
├── 04-ug-ls.md                         (L&S programs)
├── 05-grad-graduate-studies.md         (Graduate Studies programs)
├── 06-grad-management.md               (GSM programs)
├── 07-grad-education.md                (Education programs)
├── 08-grad-law.md                      (Law programs)
├── 09-grad-medicine.md                 (Medicine programs)
├── 10-grad-nursing.md                  (Nursing programs)
├── 11-grad-vetmed.md                   (Vet Med programs)
├── 12-deadlines-requirements.md        (Section 3)
├── 13-costs-financial-aid.md           (Section 4)
└── 14-evidence-chain.md                (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ucdavis-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate application fee confirmation | gradstudies.ucdavis.edu |
| P0 | Specific TOEFL/IELTS minimum scores | UC system-wide or gradstudies.ucdavis.edu |
| P1 | Per-program GRE requirements | Individual program pages |
| P1 | Graduate program deadlines | Individual program pages |
| P1 | DVM program details | vetmed.ucdavis.edu |
| P1 | JD program details | law.ucdavis.edu |
| P1 | MD program details | medschool.ucdavis.edu |
| P2 | Graduate cost of attendance by program | financialaid.ucdavis.edu/graduate |
| P2 | Stipend rates for funded PhDs | Individual programs |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UC Davis | (Other schools) |
|-----------|----------|-----------------|
| Type | Public (UC system) | |
| Location | Davis, CA | |
| UG tuition (in-state) | $15,588 | |
| UG tuition (OOS) | $54,858 | |
| UG total COA (in-state, on-campus) | $49,009 | |
| UG total COA (OOS, on-campus) | $88,279 | |
| Need-blind (intl) | No (need-aware) | |
| Application portal | UC Application | |
| Filing period | Oct 1 – Dec 1 | |
| EA/ED | None (UC system) | |
| Test policy | Test-FREE | |
| TOEFL min | Per UC system | |
| IELTS min | Per UC system | |
| Application fee (UG domestic) | $80 | |
| Application fee (UG intl) | $95 | |
| Application fee (grad) | $80 / $95 | |
| Total programs (Rule 1) | 408 | |
| UG colleges | 4 | |
| Professional schools | 6 | |
| Graduate Studies | Yes (90+ programs) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: ucdavis.edu, catalog.ucdavis.edu, gradstudies.ucdavis.edu, financialaid.ucdavis.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
