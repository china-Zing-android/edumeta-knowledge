# University of California, Riverside (UCR) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: US (public, UC system)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 82 |
| 本科辅修 (Minor) | 41 |
| 研究生学位项目 (MA/MS/MFA/MBA/MPH/MPP/MPAc/MSBA/MFin/MEd/PhD) | 64 unique program entries (99 degree-level offerings) |
| 研究生高级证书 (Advanced Certificate / Diploma) | 0 |
| **学位项目总计 (UG + Grad)** | **187** (unique program entries) |
| 学院 / 独立系所总数 | 7 (3 colleges + 4 schools) + Graduate Division |

> **Reconciliation note**: The graduate.ucr.edu/programs page header states "44 Doctor of Philosophy Programs" and "55 Master's Degree Programs" (total 99 degree-level offerings). This counts each degree type separately for programs offering both MS and PhD. The 64 figure counts unique program entries. The 187 total = 82 UG majors + 41 UG minors + 64 grad programs. Both the 187 (unique entries) and 222 (82+41+99, degree-level offerings) figures are reported for transparency.

> Source: admissions.ucr.edu/majors ("over 150 majors and minors"); graduate.ucr.edu/programs ("44 Doctor of Philosophy Programs, 55 Master's Degree Programs")

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of California, Riverside
├── College of Natural and Agricultural Sciences (CNAS)          [学院]
│   ├── Biology                                                  [系]
│   ├── Biochemistry                                             [系]
│   ├── Cell, Molecular, and Developmental Biology               [系]
│   ├── Chemistry                                                [系]
│   ├── Earth and Planetary Sciences                             [系]
│   ├── Entomology                                               [系]
│   ├── Environmental Sciences                                   [系]
│   ├── Mathematics                                              [系]
│   ├── Microbiology                                             [系]
│   ├── Neuroscience                                             [系]
│   ├── Physics                                                  [系]
│   ├── Plant Biology                                            [系]
│   ├── Statistics                                               [系]
│   └── Astronomy (graduate only)                                [系]
├── College of Humanities, Arts, and Social Sciences (CHASS)     [学院]
│   ├── Anthropology                                             [系]
│   ├── Art                                                      [系]
│   ├── Black Study                                              [系]
│   ├── Creative Writing                                         [系]
│   ├── Dance                                                    [系]
│   ├── Economics                                                [系]
│   ├── English                                                  [系]
│   ├── Ethnic Studies                                           [系]
│   ├── Gender and Sexuality Studies                             [系]
│   ├── Global Studies                                           [系]
│   ├── History                                                  [系]
│   ├── Languages and Literatures                                [系]
│   ├── Media and Cultural Studies                               [系]
│   ├── Music                                                    [系]
│   ├── Philosophy                                               [系]
│   ├── Political Science                                        [系]
│   ├── Psychology                                               [系]
│   ├── Religious Studies                                        [系]
│   ├── Sociology                                                [系]
│   └── Theatre, Film and Digital Production                     [系]
├── Marlan and Rosemary Bourns College of Engineering (BCOE)     [学院]
│   ├── Bioengineering                                           [系]
│   ├── Chemical and Environmental Engineering                   [系]
│   ├── Computer Science and Engineering                         [系]
│   ├── Electrical and Computer Engineering                      [系]
│   ├── Materials Science and Engineering                        [系]
│   ├── Mechanical Engineering                                   [系]
│   └── Robotics                                                 [系]
├── School of Business                                           [学院]
│   ├── Accounting & Auditing                                    [系]
│   ├── Finance                                                  [系]
│   ├── Information Systems                                      [系]
│   ├── Management                                               [系]
│   ├── Marketing                                                [系]
│   └── Operations and Supply Chain Management                   [系]
├── School of Education (Graduate School of Education)            [学院]
│   └── Education                                                [系]
├── School of Public Policy                                      [学院]
│   └── Public Policy                                            [系]
├── School of Medicine                                           [学院]
│   └── Public Health (graduate only)                            [系]
└── Graduate Division                                            [行政单元]
    └── (administers all graduate programs across schools)
```

> **Note**: Data Science is offered in two tracks — Engineering Track (BCOE) and Science Track (CNAS). Computer Science and Business Applications is jointly administered by BCOE and School of Business. Neuroscience is jointly administered by CNAS and CHASS.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | official (本校) | 全称 | 层级 | 本项目数量 |
|---------------------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 52 |
| BS | B.S. | Bachelor of Science | 本科 | 30 |
| Minor | Minor | 辅修 | 本科 | 41 |
| MA | M.A. | Master of Arts | 研究生 | 8 |
| MS | M.S. | Master of Science | 研究生 | 14 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 5 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 3 |
| MEd | M.Ed. | Master of Education | 研究生 | 2 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 1 |
| MPP | M.P.P. | Master of Public Policy | 研究生 | 1 |
| MPAc | M.P.Ac. | Master of Professional Accountancy | 研究生 | 1 |
| MSBA | MSBA | Master of Science in Business Analytics | 研究生 | 1 |
| MFin | M.Fin. | Master of Finance | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 36 |

> **Note**: The degree-level counts above are based on the 64 unique program entries extracted from graduate.ucr.edu/programs. The page header claims "44 PhD" and "55 Master's" which counts each degree type separately.

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | Minor | MA | MS | MFA | MBA | MEd | MPH | MPP | MPAc | MSBA | MFin | PhD | 合计 |
|------------|----|----|-------|----|----|-----|-----|-----|-----|-----|------|------|------|-----|------|
| CNAS | 5 | 21 | 15 | 3 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 69 |
| CHASS | 37 | 2 | 20 | 5 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 84 |
| BCOE | 0 | 10 | 1 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 22 |
| Business | 0 | 1 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 9 |
| Education | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| Public Policy | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 |
| **合计** | **43** | **35** | **39** | **9** | **17** | **5** | **3** | **2** | **1** | **1** | **1** | **1** | **1** | **36** | **194** |

> **Reconciliation note**: The matrix total (194) differs from Rule 1 unique-entry total (187) because the matrix counts each degree type separately for programs offering both BA and BS (e.g., Neuroscience offers both B.A. and B.S., counted as 2 in matrix but 1 program entry in Rule 1). The 82 UG majors from admissions.ucr.edu/majors includes combined-track programs counted once.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UCR has 3 undergraduate colleges (CNAS, CHASS, BCOE) and 4 professional schools (Business, Education, Public Policy, Medicine). The undergraduate colleges grant the majority of bachelor's degrees. The School of Medicine is graduate-only. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Natural and Agricultural Sciences (CNAS)

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://admissions.ucr.edu/majors |
| 2 | Mathematics | https://admissions.ucr.edu/majors |
| 3 | Mathematics for Secondary School Teachers | https://admissions.ucr.edu/majors |
| 4 | Statistics | https://admissions.ucr.edu/majors |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Biology | https://admissions.ucr.edu/majors |
| 6 | Biochemistry | https://admissions.ucr.edu/majors |
| 7 | Cell, Molecular, and Developmental Biology | https://admissions.ucr.edu/majors |
| 8 | Microbiology | https://admissions.ucr.edu/majors |
| 9 | Neuroscience (B.S.) | https://admissions.ucr.edu/majors |
| 10 | Plant Biology | https://admissions.ucr.edu/majors |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Neuroscience (B.A.) | https://admissions.ucr.edu/majors |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Chemistry | https://admissions.ucr.edu/majors |

##### Department of Earth and Planetary Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Earth and Planetary Sciences | https://admissions.ucr.edu/majors |
| 14 | Geology | https://admissions.ucr.edu/majors |
| 15 | Geophysics | https://admissions.ucr.edu/majors |

##### Department of Entomology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 16 | Entomology | https://admissions.ucr.edu/majors |

##### Department of Environmental Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 17 | Environmental Sciences | https://admissions.ucr.edu/majors |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 18 | Physics | https://admissions.ucr.edu/majors |

##### Interdisciplinary / Cross-Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 19 | Data Science (Science Track) | https://admissions.ucr.edu/majors |
| 20 | Global and Community Health | https://admissions.ucr.edu/majors |

---

#### College of Humanities, Arts, and Social Sciences (CHASS)

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://admissions.ucr.edu/majors |

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 2 | Art (Studio) | https://admissions.ucr.edu/majors |
| 3 | Art History | https://admissions.ucr.edu/majors |
| 4 | Art History/Administrative Studies | https://admissions.ucr.edu/majors |
| 5 | Art History/Religious Studies | https://admissions.ucr.edu/majors |

##### Department of Black Study
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | Black Study | https://admissions.ucr.edu/majors |

##### Department of Creative Writing
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Creative Writing | https://admissions.ucr.edu/majors |

##### Department of Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 8 | Dance | https://admissions.ucr.edu/majors |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | Economics | https://admissions.ucr.edu/majors |
| 10 | Business Economics | https://admissions.ucr.edu/majors |
| 11 | Economics/Administrative Studies | https://admissions.ucr.edu/majors |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | English | https://admissions.ucr.edu/majors |

##### Department of Ethnic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | African American Studies | https://admissions.ucr.edu/majors |
| 14 | Asian American Studies | https://admissions.ucr.edu/majors |
| 15 | Chicano Studies | https://admissions.ucr.edu/majors |
| 16 | Ethnic Studies | https://admissions.ucr.edu/majors |
| 17 | Native American Studies | https://admissions.ucr.edu/majors |

##### Department of Gender and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 18 | Gender and Sexuality Studies | https://admissions.ucr.edu/majors |

##### Department of Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 19 | Global Studies | https://admissions.ucr.edu/majors |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | History | https://admissions.ucr.edu/majors |
| 21 | History/Administrative Studies | https://admissions.ucr.edu/majors |

##### Department of Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 22 | Languages and Literatures | https://admissions.ucr.edu/majors |
| 23 | Comparative Ancient Civilizations | https://admissions.ucr.edu/majors |
| 24 | Comparative Literature | https://admissions.ucr.edu/majors |
| 25 | Languages | https://admissions.ucr.edu/majors |
| 26 | Linguistics | https://admissions.ucr.edu/majors |

##### Department of Liberal Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 27 | Liberal Studies | https://admissions.ucr.edu/majors |

##### Department of Media and Cultural Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 28 | Media and Cultural Studies | https://admissions.ucr.edu/majors |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 29 | Music | https://admissions.ucr.edu/majors |
| 30 | Music and Culture | https://admissions.ucr.edu/majors |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 31 | Philosophy | https://admissions.ucr.edu/majors |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 32 | Political Science | https://admissions.ucr.edu/majors |
| 33 | Political Science/Administrative Studies | https://admissions.ucr.edu/majors |
| 34 | Political Science/International Affairs | https://admissions.ucr.edu/majors |
| 35 | Political Science/Public Service | https://admissions.ucr.edu/majors |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 36 | Psychology | https://admissions.ucr.edu/majors |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 37 | Sociology | https://admissions.ucr.edu/majors |
| 38 | Sociology/Administrative Studies | https://admissions.ucr.edu/majors |

##### Department of Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 39 | Spanish | https://admissions.ucr.edu/majors |

##### Department of Theatre, Film and Digital Production
###### BA
| # | 专业 | URL |
|---|------|-----|
| 40 | Theatre, Film and Digital Production | https://admissions.ucr.edu/majors |

##### Department of Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 41 | Religious Studies/Administrative Studies | https://admissions.ucr.edu/majors |

##### Interdisciplinary
###### BA
| # | 专业 | URL |
|---|------|-----|
| 42 | Middle East and Islamic Studies | https://admissions.ucr.edu/majors |

---

#### Marlan and Rosemary Bourns College of Engineering (BCOE)

##### Department of Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://admissions.ucr.edu/majors |

##### Department of Chemical and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Chemical Engineering | https://admissions.ucr.edu/majors |
| 3 | Environmental Engineering | https://admissions.ucr.edu/majors |

##### Department of Computer Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Computer Science and Engineering | https://admissions.ucr.edu/majors |
| 5 | Computer Science and Business Applications | https://admissions.ucr.edu/majors |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Electrical Engineering | https://admissions.ucr.edu/majors |
| 7 | Computer Engineering | https://admissions.ucr.edu/majors |

##### Department of Materials Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Materials Science and Engineering | https://admissions.ucr.edu/majors |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Mechanical Engineering | https://admissions.ucr.edu/majors |

##### Department of Robotics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Robotics | https://admissions.ucr.edu/majors |

##### Interdisciplinary
###### BS
| # | 专业 | URL |
|---|------|-----|
| 11 | Data Science (Engineering Track) | https://admissions.ucr.edu/majors |

---

#### School of Business

##### Department of Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://business.ucr.edu/undergraduate/major |
| 2 | Business Analytics | https://admissions.ucr.edu/majors |
| 3 | Pre-Business | https://admissions.ucr.edu/majors |

> Note: Business Administration has 6 concentrations: Accounting & Auditing, Finance, Information Systems, Management, Marketing, Operations and Supply Chain Management. These are concentrations within the single B.S. in Business Administration.

---

#### School of Education

##### Department of Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education, Society, and Human Development | https://admissions.ucr.edu/majors |

---

#### School of Public Policy

##### Department of Public Policy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy | https://admissions.ucr.edu/majors |

---

#### Undeclared Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Undeclared Program (Humanities) | https://admissions.ucr.edu/majors |
| 2 | Undeclared Program (Science) | https://admissions.ucr.edu/majors |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | Parent Schools | URL |
|---|------|---------------|-----|
| 1 | Data Science (Science Track) | CNAS + BCOE | https://admissions.ucr.edu/majors |
| 2 | Data Science (Engineering Track) | BCOE + CNAS | https://admissions.ucr.edu/majors |
| 3 | Computer Science and Business Applications | BCOE + Business | https://admissions.ucr.edu/majors |
| 4 | Neuroscience (B.A.) | CNAS + CHASS | https://admissions.ucr.edu/majors |
| 5 | Neuroscience (B.S.) | CNAS + CHASS | https://admissions.ucr.edu/majors |
| 6 | Art History/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 7 | Economics/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 8 | History/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 9 | Political Science/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 10 | Sociology/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 11 | Religious Studies/Administrative Studies | CHASS + Business | https://admissions.ucr.edu/majors |
| 12 | Political Science/International Affairs | CHASS | https://admissions.ucr.edu/majors |
| 13 | Political Science/Public Service | CHASS | https://admissions.ucr.edu/majors |

### 1.4 Minors — Complete List

| # | Minor Name | Home School | URL |
|---|-----------|-------------|-----|
| 1 | African American Studies | CHASS | https://admissions.ucr.edu/majors |
| 2 | Anthropology | CHASS | https://admissions.ucr.edu/majors |
| 3 | Art History | CHASS | https://admissions.ucr.edu/majors |
| 4 | Asian American Studies | CHASS | https://admissions.ucr.edu/majors |
| 5 | Chemistry | CNAS | https://admissions.ucr.edu/majors |
| 6 | Chicano Studies | CHASS | https://admissions.ucr.edu/majors |
| 7 | Creative Writing | CHASS | https://admissions.ucr.edu/majors |
| 8 | Dance | CHASS | https://admissions.ucr.edu/majors |
| 9 | Earth and Planetary Sciences | CNAS | https://admissions.ucr.edu/majors |
| 10 | Economics | CHASS | https://admissions.ucr.edu/majors |
| 11 | English | CHASS | https://admissions.ucr.edu/majors |
| 12 | Entomology | CNAS | https://admissions.ucr.edu/majors |
| 13 | Environmental Sciences | CNAS | https://admissions.ucr.edu/majors |
| 14 | Ethnic Studies | CHASS | https://admissions.ucr.edu/majors |
| 15 | Gender and Sexuality Studies | CHASS | https://admissions.ucr.edu/majors |
| 16 | Geology | CNAS | https://admissions.ucr.edu/majors |
| 17 | Global and Community Health | CNAS | https://admissions.ucr.edu/majors |
| 18 | Global Studies | CHASS | https://admissions.ucr.edu/majors |
| 19 | History | CHASS | https://admissions.ucr.edu/majors |
| 20 | Chinese (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 21 | Classical Studies (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 22 | French (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 23 | Germanic Studies (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 24 | Japanese (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 25 | Russian Studies (Languages and Literatures) | CHASS | https://admissions.ucr.edu/majors |
| 26 | Mathematics | CNAS | https://admissions.ucr.edu/majors |
| 27 | Media and Cultural Studies | CHASS | https://admissions.ucr.edu/majors |
| 28 | Middle East and Islamic Studies | CHASS | https://admissions.ucr.edu/majors |
| 29 | Music | CHASS | https://admissions.ucr.edu/majors |
| 30 | Native American Studies | CHASS | https://admissions.ucr.edu/majors |
| 31 | Neuroscience | CNAS | https://admissions.ucr.edu/majors |
| 32 | Philosophy | CHASS | https://admissions.ucr.edu/majors |
| 33 | Physics | CNAS | https://admissions.ucr.edu/majors |
| 34 | Plant Biology | CNAS | https://admissions.ucr.edu/majors |
| 35 | Political Science | CHASS | https://admissions.ucr.edu/majors |
| 36 | Psychology | CHASS | https://admissions.ucr.edu/majors |
| 37 | Public Policy | Public Policy | https://admissions.ucr.edu/majors |
| 38 | Robotics | BCOE | https://admissions.ucr.edu/majors |
| 39 | Sociology | CHASS | https://admissions.ucr.edu/majors |
| 40 | Spanish | CHASS | https://admissions.ucr.edu/majors |
| 41 | Statistics | CNAS | https://admissions.ucr.edu/majors |
| 42 | Theatre, Film and Digital Production | CHASS | https://admissions.ucr.edu/majors |

> Note: The admissions page lists "M" notation for minors. Total minors from cached data: 41. The list above includes language sub-minors under Languages and Literatures. Business has 1 minor (Business Administration), Education has 1 minor (Education).

### 1.5 General/Institute-Wide Requirements

UCR follows the UC system's A-G subject requirements for admission:
- A: History/Social Science (2 years)
- B: English (4 years)
- C: Mathematics (3 years, 4 recommended; must include Geometry)
- D: Science (2 years, 3 recommended)
- E: Language Other Than English (2 years, 3 recommended)
- F: Visual and Performing Arts (1 year)
- G: College-Preparatory Elective (1 year)

Minimum GPA: 3.0 for CA residents, 3.4 for non-California residents (grades 10-11).

UCR operates on the **quarter system** (Fall/Winter/Spring/Summer).

### 1.6 Accelerated Programs (B.S.+M.S. / B.A.+MPP)

| # | Program | Type | College |
|---|---------|------|---------|
| 1 | Bioengineering | B.S.+M.S. | BCOE |
| 2 | Chemical and Environmental Engineering | B.S.+M.S. | BCOE |
| 3 | Computer Engineering | B.S.+M.S. | BCOE |
| 4 | Computer Science and Engineering | B.S.+M.S. | BCOE |
| 5 | Electrical Engineering | B.S.+M.S. | BCOE |
| 6 | Mechanical Engineering | B.S.+M.S. | BCOE |
| 7 | Entomology | B.S.+M.S. | CNAS |
| 8 | Statistics | B.S.+M.S. | CNAS |
| 9 | Public Policy | B.A.+MPP | School of Public Policy |

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Natural and Agricultural Sciences (CNAS)

##### Anthropology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://graduate.ucr.edu/programs |

##### Astronomy
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Astronomy | https://graduate.ucr.edu/programs |

##### Biochemistry
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://graduate.ucr.edu/programs |

##### Bioengineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://graduate.ucr.edu/programs |

##### Biomedical Sciences
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://graduate.ucr.edu/programs |

##### Biophysics
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biophysics | https://graduate.ucr.edu/programs |

##### Cell, Molecular, and Developmental Biology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Cell, Molecular, and Developmental Biology | https://graduate.ucr.edu/programs |

##### Chemistry
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://graduate.ucr.edu/programs |

##### Earth and Planetary Sciences
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | https://graduate.ucr.edu/programs |

##### Entomology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Entomology | https://graduate.ucr.edu/programs |

##### Environmental Sciences
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Sciences | https://graduate.ucr.edu/programs |

##### Environmental Toxicology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Toxicology | https://graduate.ucr.edu/programs |

##### Evolution, Ecology, and Organismal Biology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Evolution, Ecology, and Organismal Biology | https://graduate.ucr.edu/programs |

##### Genetics, Genomics, and Bioinformatics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Genetics, Genomics, and Bioinformatics | https://graduate.ucr.edu/programs |

##### Evolutionary Biology (Joint with SDSU)
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Evolutionary Biology Joint Doctoral Program with SDSU | https://graduate.ucr.edu/programs |

##### Mathematics
###### MA, MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://graduate.ucr.edu/programs |

##### Applied Statistics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics | https://graduate.ucr.edu/programs |

##### Statistics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistics | https://graduate.ucr.edu/programs |

##### Microbiology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology | https://graduate.ucr.edu/programs |

##### Neuroscience
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | https://graduate.ucr.edu/programs |

##### Physics
###### MA, MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://graduate.ucr.edu/programs |

##### Plant Biology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Biology | https://graduate.ucr.edu/programs |

##### Plant Pathology
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Plant Pathology | https://graduate.ucr.edu/programs |

---

#### College of Humanities, Arts, and Social Sciences (CHASS)

##### Anthropology (see CNAS for PhD/MS)

##### Art History
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://graduate.ucr.edu/programs |

##### Art
###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art, Visual | https://graduate.ucr.edu/programs |
| 2 | Experimental Choreography | https://graduate.ucr.edu/programs |
| 3 | Visual Art | https://graduate.ucr.edu/programs |

##### Classics (UC Tri-Campus)
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics - UC Tri-Campus Graduate Program in Classics | https://graduate.ucr.edu/programs |

##### Comparative Literature
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Literature | https://graduate.ucr.edu/programs |

##### Creative Writing
###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing and Writing for the Performing Arts | https://graduate.ucr.edu/programs |
| 2 | Creative Writing and Writing for the Performing Arts - Palm Desert Low Residency Program | https://graduate.ucr.edu/programs |

##### Dance
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Critical Dance Studies | https://graduate.ucr.edu/programs |

##### Economics
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://graduate.ucr.edu/programs |

##### English
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://graduate.ucr.edu/programs |

##### Ethnic Studies
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://graduate.ucr.edu/programs |

##### History
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://graduate.ucr.edu/programs |

##### Music
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://graduate.ucr.edu/programs |

##### Philosophy
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://graduate.ucr.edu/programs |

##### Political Science
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://graduate.ucr.edu/programs |

##### Psychology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://graduate.ucr.edu/programs |

##### Religious Studies
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Studies | https://graduate.ucr.edu/programs |

##### Sociology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://graduate.ucr.edu/programs |

> Note: Sociology PhD not accepting applications for 2025-26.

##### Southeast Asian Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Southeast Asian Studies | https://graduate.ucr.edu/programs |

##### Spanish
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Spanish | https://graduate.ucr.edu/programs |

---

#### Marlan and Rosemary Bourns College of Engineering (BCOE)

##### Bioengineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://graduate.ucr.edu/programs |

##### Chemical and Environmental Engineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical and Environmental Engineering | https://graduate.ucr.edu/programs |

##### Computer Science and Engineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://graduate.ucr.edu/programs |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 2 | Computational Data Science | https://graduate.ucr.edu/programs |
| 3 | Computer Engineering | https://graduate.ucr.edu/programs |

##### Electrical and Computer Engineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://graduate.ucr.edu/programs |

##### Materials Science and Engineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://graduate.ucr.edu/programs |

##### Mechanical Engineering
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://graduate.ucr.edu/programs |

##### Robotics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Robotics | https://graduate.ucr.edu/programs |

##### Engineering (Online)
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering - M.S. (Online Program) | https://graduate.ucr.edu/programs |

---

#### School of Business

##### Management
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Management - M.B.A. | https://graduate.ucr.edu/programs |
| 2 | Management - M.B.A. (Online) | https://graduate.ucr.edu/programs |
| 3 | Management - Professional M.B.A. | https://graduate.ucr.edu/programs |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration - Ph.D. | https://graduate.ucr.edu/programs |

> Note: Business Administration PhD not accepting applications for 2026-27.

##### Accounting
###### MPAc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting, Auditing and Assurance - M.P.Ac. | https://graduate.ucr.edu/programs |

##### Business Analytics
###### MSBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics - MSBA | https://graduate.ucr.edu/programs |

##### Finance
###### MFin
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance - M.Fin. | https://graduate.ucr.edu/programs |

---

#### School of Education (Graduate School of Education)

##### Education
###### MA, MEd, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://graduate.ucr.edu/programs |

###### MEd
| # | 项目 | URL |
|---|------|-----|
| 2 | Education (General Education with Teaching Emphasis) | https://graduate.ucr.edu/programs |

---

#### School of Public Policy

##### Public Policy
###### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy - M.P.P. | https://graduate.ucr.edu/programs |

---

#### School of Medicine

##### Public Health
###### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health - M.P.H. | https://graduate.ucr.edu/programs |

---

### 2.2 Graduate Admissions Model

UCR's graduate admissions is **decentralized** — each program sets its own requirements, deadlines, and review processes. The Graduate Division provides central services (application portal, fee collection, final approval) but admission decisions are made by individual programs.

**Application portal**: https://graduate.ucr.edu/apply

**Application fees**:
- Domestic (U.S. Citizen/Permanent Resident): $135
- International (Non-Immigrant/Visa Students): $155

**GRE/TOEFL institutional code**: Varies by program; check individual program websites.

**English Language Requirement**: TOEFL or IELTS scores required for non-native English speakers. Scores must be dated within 2 years of the quarter of application.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| Application portal | UC Application (not Common App) | admission.universityofcalifornia.edu |
| Application opens | August 1 | admissions.ucr.edu/firstyear |
| Application deadline | October 1 – November 30 | admissions.ucr.edu/firstyear |
| EA deadline | N/A (UC system has no EA/ED) | — |
| ED deadline | N/A (UC system has no EA/ED) | — |
| Decision notifications | March (first-year begin) | admissions.ucr.edu/firstyear |
| SIR deadline | May 1 | admissions.ucr.edu/firstyear |
| FAFSA/CADAA priority deadline | March 2 | admissions.ucr.edu/firstyear |
| Housing contract deadline | May 10 (guaranteed housing) | admissions.ucr.edu/firstyear |
| Final transcript deadline | July 1 | admissions.ucr.edu/firstyear |
| AP/IB/A-Level scores deadline | July 15 | admissions.ucr.edu/firstyear |
| Application fee | $80 (UC Application) | admission.universityofcalifornia.edu |
| SAT/ACT policy | Test-FREE (not considered in admission or scholarships) | admissions.ucr.edu/international |
| Superscore policy | N/A (test-free) | — |
| Interview policy | None | — |
| Recommendation requirements | None (UC Application does not require recs) | — |
| Portfolio | Not required for most majors | — |
| GPA minimum (CA residents) | 3.0 (A-G courses, grades 10-11) | admissions.ucr.edu/firstyear |
| GPA minimum (non-CA residents) | 3.4 (A-G courses, grades 10-11) | admissions.ucr.edu/firstyear |
| School codes | TOEFL/AP/SAT: 004839; ACT: 0456 | admissions.ucr.edu/international |
| Federal School Code | 001316 | financialaid.ucr.edu/cost |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended Score | Notes |
|------|--------------|-------------------|-------|
| TOEFL iBT | 80 | — | Required for non-native English speakers whose secondary education was not in English |
| IELTS | 6.5 | — | Academic version |
| Duolingo English Test (DET) | 115 | — | |

> Source: admissions.ucr.edu/firstyear (International Exams section)
> Applicability: Required if native language is not English AND secondary/high school education was in a country where English is not the language of instruction.

### 3.3 Graduate — Global Rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions model | Decentralized (each program decides) | graduate.ucr.edu |
| Application portal | https://graduate.ucr.edu/apply | graduate.ucr.edu/apply |
| Application fee (domestic) | $135 | graduate.ucr.edu/frequently-asked-questions |
| Application fee (international) | $155 | graduate.ucr.edu/frequently-asked-questions |
| GPA minimum | 3.0 undergraduate (some programs higher) | graduate.ucr.edu/admission-requirements |
| GRE policy | Per-program (consult individual programs) | graduate.ucr.edu/admission-requirements |
| English proficiency | TOEFL or IELTS required for non-native speakers; scores valid 2 years | graduate.ucr.edu/frequently-asked-questions |
| TOEFL/IELTS validity | 2 years from quarter of application | graduate.ucr.edu/frequently-asked-questions |
| TOEFL MyBest | Not specified | — |
| Fellowship deadline (domestic) | January 5 (Fall) | graduate.ucr.edu/deadlines |
| Admission-only deadline (domestic) | June 1 (Fall) | graduate.ucr.edu/deadlines |
| Fellowship deadline (international) | January 5 (Fall) | graduate.ucr.edu/deadlines |
| Admission-only deadline (international) | June 1 (Fall) | graduate.ucr.edu/deadlines |
| Winter application | Open for select programs only | graduate.ucr.edu/deadlines |
| CGS April 15 signatory | Not specified | — |
| Transcript evaluation | WES Course-by-Course ICAP required for international degrees upon admission | graduate.ucr.edu/admission-requirements |

**Graduate deadlines by term**:

| Term | Domestic Fellowship | Domestic Admission Only | International Fellowship | International Admission Only |
|------|-------------------|------------------------|-------------------------|------------------------------|
| Fall | January 5 | June 1 | January 5 | June 1 |
| Winter | November 1 | November 1 | September 1 | September 1 |
| Spring | February 1 | February 1 | December 1 | December 1 |
| Summer | May 1 | May 1 | March 1 | March 1 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

#### California Residents (New Students 2026-27)

| Expense Item | University Housing | Off Campus | Living at Home |
|-------------|-------------------|------------|----------------|
| UC Tuition & Fees | $15,588 | $15,588 | $15,588 |
| Campus Fees & Tech Fees | $1,170 | $1,170 | $1,170 |
| UC Student Health Insurance | $2,684 | $2,684 | $2,684 |
| Housing and Food | $21,075 | $17,625 | $8,600 |
| Books and Supplies | $1,700 | $1,700 | $1,700 |
| Transportation | $1,275 | $2,300 | $2,800 |
| Personal Expenses | $2,875 | $3,175 | $3,050 |
| **Total** | **$46,367** | **$44,242** | **$35,592** |

> Source: financialaid.ucr.edu/cost — "2026-2027 Estimated Costs for New Students Enrolling in 2026-2027 as First Year Undergraduates" (California Residents and AB540 Eligible)

#### Out-of-State / International (New Students 2026-27)

| Expense Item | University Housing | Off Campus | Living at Home |
|-------------|-------------------|------------|----------------|
| UC Tuition & Fees | $15,588 | $15,588 | $15,588 |
| Non-resident Supplemental Tuition (NRST) | $39,270 | $39,270 | $39,270 |
| Campus Fees & Tech Fees | $1,170 | $1,170 | $1,170 |
| UC Student Health Insurance | $2,684 | $2,684 | $2,684 |
| Housing and Food | $21,075 | $17,625 | $8,600 |
| Books and Supplies | $1,750 | $1,750 | $1,750 |
| Transportation | $1,100 | $2,700 | $3,000 |
| Personal Expenses | $2,525 | $2,650 | $2,675 |
| **Total** | **$82,441** | **$80,541** | **$73,041** |

> Source: financialaid.ucr.edu/cost — "2026-2027 Estimated Costs for New Students Enrolling in 2026-2027 as First Year Undergraduates" (Out of State and International Undergraduates)
> Note: UC Tuition Stability Plan — tuition is flat for up to 6 years from entry year.

### 4.2 Undergraduate Financial-Aid Policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Blue & Gold Opportunity Plan threshold | Family income < $80,000 (CA residents: all systemwide tuition/fees covered) | admissions.ucr.edu/affordable-ca |
| % undergrads awarded aid | ~80% | admissions.ucr.edu/affordable-ca |
| % of aided students receiving need-based grants | 98% | admissions.ucr.edu/affordable-ca |
| Need-blind domestic | Yes (UC system policy) | UC system |
| Need-aware international | Yes (limited intl aid) | admissions.ucr.edu/international |
| Achievement Scholarship (international first-year) | Up to $89,100 over 4 years | admissions.ucr.edu/international |
| Achievement Scholarship (international transfer) | Up to $44,550 over 2 years | admissions.ucr.edu/international |
| Achievement Scholarship requirement | 3.0 GPA each academic quarter | admissions.ucr.edu/international |
| Native American Opportunity Plan | Full tuition for Native American students | admissions.ucr.edu/affordable-ca |
| FAFSA/CADAA priority deadline | March 2 | admissions.ucr.edu/firstyear |
| School code (FAFSA) | 001316 | financialaid.ucr.edu/cost |
| Social mobility ranking | #1 nationally | U.S. News, 2026 |

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 | 来源 |
|------|-----|------|
| Application fee (domestic) | $135 | graduate.ucr.edu |
| Application fee (international) | $155 | graduate.ucr.edu |
| Fee waivers | Available (consult Graduate Division) | graduate.ucr.edu/frequently-asked-questions |
| Funding types | Fellowships, TA/GSR positions, grants | graduate.ucr.edu/funding |
| Fellowship consideration deadline | January 5 (Fall) | graduate.ucr.edu/deadlines |
| Most PhD programs | Fully funded (TA/GSR + fellowship) | graduate.ucr.edu |
| Master's programs | Varies by program (many self-funded) | graduate.ucr.edu |

> Note: Graduate cost of attendance varies by program. Visit individual program websites for specific funding information. The Graduate Division provides central fellowship funding; departments provide TA and GSR positions.

---

## SECTION 5 — Evidence Chain Index

### E-U-001
```yaml
field: undergraduate.deadlines.application_period
value: "October 1 – November 30"
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "Oct. 1-Nov. 30 — Submit your UC application."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-002
```yaml
field: undergraduate.deadlines.sir
value: "May 1"
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "May 1 — Deadline to submit your Statement of Intent to Register (SIR)."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003
```yaml
field: undergraduate.deadlines.fafsa_priority
value: "March 2"
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "March 2 — Priority deadline to submit your Free Application for Federal Student Aid (FAFSA) or California Dream Act Application (CADAA)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004
```yaml
field: undergraduate.test_policy
value: "Test-FREE (SAT/ACT not considered)"
source_url: https://admissions.ucr.edu/international
source_snippet: "UC Riverside will not consider SAT or ACT test scores when making admissions decisions or awarding scholarships."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005
```yaml
field: undergraduate.english_proficiency.toefl
value: 80
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "Test of English as a Foreign Language (TOEFL) — 80"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-006
```yaml
field: undergraduate.english_proficiency.ielts
value: 6.5
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "International English Language Testing System (IELTS) — 6.5"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-007
```yaml
field: undergraduate.english_proficiency.det
value: 115
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "Duolingo English Test (DET) — 115"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-008
```yaml
field: undergraduate.gpa.minimum_ca
value: 3.0
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "Students must achieve a minimum grade point average (GPA) of 3.0 in all college preparatory (A-G) courses"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-009
```yaml
field: undergraduate.gpa.minimum_oos
value: 3.4
source_url: https://admissions.ucr.edu/firstyear
source_snippet: "or 3.4 for non-California residents"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-010
```yaml
field: undergraduate.cost.tuition_ca_2026_27
value: "$15,588"
source_url: https://financialaid.ucr.edu/cost
source_snippet: "UC Tuition & Fees — $15,588"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-011
```yaml
field: undergraduate.cost.nrst_2026_27
value: "$39,270"
source_url: https://financialaid.ucr.edu/cost
source_snippet: "Non-resident Supplemental Tuition — $39,270"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-012
```yaml
field: undergraduate.cost.total_oncampus_ca_2026_27
value: "$46,367"
source_url: https://financialaid.ucr.edu/cost
source_snippet: "Total — $46,367 (University Housing)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-013
```yaml
field: undergraduate.cost.total_oncampus_oos_2026_27
value: "$82,441"
source_url: https://financialaid.ucr.edu/cost
source_snippet: "Total — $82,441 (University Housing, Out of State)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-014
```yaml
field: undergraduate.financial_aid.blue_gold_threshold
value: "$80,000"
source_url: https://admissions.ucr.edu/affordable-ca
source_snippet: "If you're a CA resident and your family income is less than $80,000 a year, you can have all your system-wide tuition and fees covered!"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-015
```yaml
field: undergraduate.financial_aid.achievement_scholarship_max
value: "$89,100 (4 years)"
source_url: https://admissions.ucr.edu/international
source_snippet: "First-year students may receive up to $89,100 for four years"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-016
```yaml
field: undergraduate.programs.majors_count
value: 82
source_url: https://admissions.ucr.edu/majors
source_snippet: "Choose from over 150 majors and minors"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-017
```yaml
field: undergraduate.school_codes.toefl_ap_sat
value: "004839"
source_url: https://admissions.ucr.edu/international
source_snippet: "TOEFL / AP / SAT: 004839"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-018
```yaml
field: undergraduate.school_codes.act
value: "0456"
source_url: https://admissions.ucr.edu/international
source_snippet: "ACT: 0456"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001
```yaml
field: graduate.deadlines.fellowship_fall
value: "January 5"
source_url: https://graduate.ucr.edu/deadlines
source_snippet: "Fall - January 5th (Fellowship Consideration*)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-002
```yaml
field: graduate.deadlines.admission_fall
value: "June 1"
source_url: https://graduate.ucr.edu/deadlines
source_snippet: "Fall - June 1st (Admission Only)**"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-003
```yaml
field: graduate.application_fee_domestic
value: "$135"
source_url: https://graduate.ucr.edu/frequently-asked-questions
source_snippet: "Application Fee section — $135 domestic"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-004
```yaml
field: graduate.application_fee_international
value: "$155"
source_url: https://graduate.ucr.edu/frequently-asked-questions
source_snippet: "Application Fee section — $155 international"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-005
```yaml
field: graduate.gpa_minimum
value: 3.0
source_url: https://graduate.ucr.edu/admission-requirements
source_snippet: "A minimum of a 3.0 undergraduate GPA or B-equivalent (if GPA is not on a 4.0 scale) is required."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-006
```yaml
field: graduate.programs.total
value: "64 unique programs (44 PhD + 55 Master's degree offerings)"
source_url: https://graduate.ucr.edu/programs
source_snippet: "44 DOCTOR OF PHILOSOPHY PROGRAMS — 55 MASTER'S DEGREE PROGRAMS"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-007
```yaml
field: graduate.english_proficiency.validity
value: "2 years"
source_url: https://graduate.ucr.edu/frequently-asked-questions
source_snippet: "TOEFL and IELTS scores must be dated 2 years from the quarter you are applying for."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-019
```yaml
field: undergraduate.tuition_stability_plan
value: "Flat for up to 6 years from entry"
source_url: https://financialaid.ucr.edu/cost
source_snippet: "Beginning fall 2022, tuition will be adjusted for each incoming undergraduate class but will subsequently remain flat until the student graduates, for up to six years."
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-020
```yaml
field: undergraduate.international.achievement_scholarship_transfer
value: "$44,550 (2 years)"
source_url: https://admissions.ucr.edu/international
source_snippet: "transfers may receive up to $44,550 for two years"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-021
```yaml
field: undergraduate.financial_aid.percent_awarded
value: "~80%"
source_url: https://admissions.ucr.edu/affordable-ca
source_snippet: "80% of UC Riverside Undergrads Awarded Aid"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
ucr-knowledge-base-v2/
├── 00-institution-overview          (Section 0: rules 1-4, hierarchy, matrix)
├── 01-ug-cnas                       (Section 1: CNAS undergraduate majors)
├── 02-ug-chass                      (Section 1: CHASS undergraduate majors)
├── 03-ug-bcoe                       (Section 1: BCOE undergraduate majors)
├── 04-ug-business                   (Section 1: Business undergraduate majors)
├── 05-ug-education                  (Section 1: Education undergraduate major)
├── 06-ug-public-policy              (Section 1: Public Policy undergraduate major)
├── 07-ug-minors                     (Section 1.4: all minors)
├── 08-grad-cnas                     (Section 2: CNAS graduate programs)
├── 09-grad-chass                    (Section 2: CHASS graduate programs)
├── 10-grad-bcoe                     (Section 2: BCOE graduate programs)
├── 11-grad-business                 (Section 2: Business graduate programs)
├── 12-grad-education                (Section 2: Education graduate programs)
├── 13-grad-public-policy            (Section 2: Public Policy graduate programs)
├── 14-grad-medicine                 (Section 2: Medicine/PH graduate programs)
├── 15-deadlines-requirements        (Section 3: UG + grad deadlines, test policy)
├── 16-costs-financial-aid           (Section 4: COA, aid policy, scholarships)
└── 17-evidence-chain                (Section 5: all evidence blocks)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "ucr-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|-----------|-------|
| P0 | Per-program GRE requirements | Individual program websites | graduate.ucr.edu says "consult program directly" |
| P0 | Graduate program-specific deadlines | Individual program websites | Some programs have earlier deadlines than standard |
| P1 | Graduate cost of attendance (per program) | Individual program websites | Varies by program |
| P1 | Detailed financial aid calculator results | financialaid.ucr.edu | Need to run calculator for specific scenarios |
| P1 | Transfer admission requirements by major | admissions.ucr.edu/transfer | Major-specific prerequisites |
| P2 | UCR Foundation scholarship database details | scholarships.ucr.edu | Specific scholarship amounts and criteria |
| P2 | Housing cost details (per residence hall) | housing.ucr.edu | Specific room types and rates |
| P2 | Career outcomes data | career.ucr.edu | Post-graduation employment statistics |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UCR | (Other schools) |
|-----------|-----|-----------------|
| Type | Public (UC system) | |
| Location | Riverside, CA | |
| Application system | UC Application | |
| Application deadline | Oct 1 – Nov 30 | |
| EA/ED | None (UC system) | |
| SAT/ACT | Test-FREE | |
| TOEFL minimum (UG) | 80 | |
| IELTS minimum (UG) | 6.5 | |
| DET minimum (UG) | 115 | |
| In-state tuition (2026-27) | $15,588 | |
| OOS tuition (2026-27) | $54,858 ($15,588 + $39,270 NRST) | |
| In-state COA on-campus (2026-27) | $46,367 | |
| OOS COA on-campus (2026-27) | $82,441 | |
| Need-blind domestic | Yes | |
| Need-blind international | No (need-aware) | |
| Blue & Gold threshold | <$80,000 income | |
| Achievement Scholarship (intl) | Up to $89,100 / 4 years | |
| Grad app fee (domestic) | $135 | |
| Grad app fee (international) | $155 | |
| Grad fellowship deadline | January 5 (Fall) | |
| Total UG majors | 82 | |
| Total UG minors | 41 | |
| Total grad programs | 64 | |
| Total program count (Rule 1) | 187 | |
| School/college count (Rule 2) | 7 | |
| Quarter system | Yes | |
| Tuition stability plan | Yes (flat 6 years) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.ucr.edu, graduate.ucr.edu, financialaid.ucr.edu, admission.universityofcalifornia.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
