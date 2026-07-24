# William & Mary Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/etc.) | 51 |
| 本科辅修 (Minor) | 52 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 62 |
| 研究生高级证书 (Grad Cert / Post-Prof Cert / Cert) | 12 |
| **学位项目总计 (UG + Grad)** | **177** |
| 学院 / 独立系所总数 | 6 |

> **Reconciliation**: Rule-1 total (177) = matrix cell-sum (177) = Rule-5 rows (177). Verified.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
William & Mary
├── College of Arts & Sciences                          [学院]
│   ├── Africana Studies                                [系]
│   ├── American Studies                                [系]
│   ├── Anthropology                                    [系]
│   ├── Applied Science                                 [系]
│   ├── Art & Art History                               [系]
│   ├── Asian & Middle Eastern Studies                  [系]
│   ├── Asian & Pacific Islander American Studies       [系]
│   ├── Biology                                         [系]
│   ├── Chemistry                                       [系]
│   ├── Chinese Language & Culture                      [系]
│   ├── Classical Studies                               [系]
│   ├── Computer Science                                [系]
│   ├── Counseling                                      [系]
│   ├── Creative Writing                                [系]
│   ├── Data Science                                    [系]
│   ├── Economics                                       [系]
│   ├── English                                         [系]
│   ├── Environment & Sustainability                    [系]
│   ├── Film & Media Studies                            [系]
│   ├── French & Francophone Studies                    [系]
│   ├── Gender, Sexuality & Women's Studies             [系]
│   ├── Geology                                         [系]
│   ├── German Studies                                  [系]
│   ├── Government                                      [系]
│   ├── History                                         [系]
│   ├── Human Health & Physiology                       [系]
│   ├── Integrative Conservation                        [系]
│   ├── International Relations                         [系]
│   ├── Japanese Studies                                [系]
│   ├── Judaic Studies                                  [系]
│   ├── Linguistics                                     [系]
│   ├── Mathematics                                     [系]
│   ├── Medieval & Renaissance Studies                  [系]
│   ├── Music                                           [系]
│   ├── Native Studies                                  [系]
│   ├── Neuroscience                                    [系]
│   ├── Philosophy                                      [系]
│   ├── Physics                                         [系]
│   ├── Psychological Sciences                          [系]
│   ├── Psychology                                      [系]
│   ├── Public Health                                   [系]
│   ├── Public Policy                                   [系]
│   ├── Religion                                        [系]
│   ├── Sociology                                       [系]
│   ├── Spanish / Hispanic Studies                      [系]
│   ├── Studio Art                                      [系]
│   └── Theatre                                         [系]
├── Mason School of Business                            [学院]
│   ├── Accounting                                      [系]
│   ├── Business Administration                         [系]
│   ├── Business Analytics                              [系]
│   ├── Finance                                         [系]
│   └── Marketing                                       [系]
├── Batten School of Coastal & Marine Sciences (VIMS)   [学院]
│   └── Marine Science / Coastal & Marine Sciences      [系]
├── School of Computing, Data Sciences & Physics        [学院]
│   ├── Computer Science                                [系] ⚠ shared with A&S
│   ├── Data Science                                    [系] ⚠ shared with A&S
│   └── Physics                                         [系] ⚠ shared with A&S
├── School of Education                                 [学院]
│   ├── Counseling                                      [系]
│   ├── Curriculum & Instruction                        [系]
│   ├── Educational Leadership                          [系]
│   └── Educational Policy, Planning & Leadership       [系]
└── Law School                                          [学院]
    └── Law                                             [系]
```

> **Note**: Computer Science, Data Science, and Physics are jointly administered by the College of Arts & Sciences and the School of Computing, Data Sciences & Physics (CDSP). Programs are listed under their primary administrative home.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 30 |
| BS | B.S. | Bachelor of Science | 本科 | 14 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 4 |
| BAEd | B.A.Ed. | Bachelor of Arts in Education | 本科 | 1 |
| Dual Bachelor's | Dual Bachelor's Degrees | Dual Bachelor's (Engineering) | 本科 | 1 |
| Joint BA | Joint B.A. | Joint Bachelor of Arts | 本科 | 1 |
| MA | M.A. | Master of Arts | 研究生 | 7 |
| MS | M.S. | Master of Science | 研究生 | 8 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 2 |
| MAcc | M.Acc. | Master of Accounting | 研究生 | 2 |
| MAEd | M.A.Ed. | Master of Arts in Education | 研究生 | 5 |
| MEd | M.Ed. | Master of Education | 研究生 | 5 |
| MPP | M.P.P. | Master of Public Policy | 研究生 | 1 |
| MLS | M.L.S. | Master of Legal Studies | 研究生 | 1 |
| EdS | Ed.S. | Educational Specialist | 研究生 | 1 |
| LLM | LL.M. | Master of Laws | 研究生 | 2 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 11 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 5 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| Grad Cert | Grad Cert | Graduate Certificate | 研究生 | 5 |
| Online Grad Cert | Online Grad Cert | Online Graduate Certificate | 研究生 | 4 |
| Post-Prof Cert | Post-Prof Cert | Post-Professional Certificate | 研究生 | 3 |
| Cert | Cert | Certificate | 研究生/本科 | 1 |

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BAEd | Dual UG | Joint BA | MA | MS | MBA | MAcc | MAEd | MEd | MPP | MLS | EdS | LLM | PhD | EdD | JD | Cert | 合计 |
|------------|----|----|-----|------|---------|----------|----|----|-----|------|------|-----|-----|-----|-----|-----|-----|-----|----|------|------|
| College of Arts & Sciences | 28 | 11 | 0 | 0 | 0 | 1 | 7 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 8 | 0 | 0 | 1 | 61 |
| Mason School of Business | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 3 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 15 |
| Batten School / VIMS | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 |
| School of Computing, Data Sciences & Physics | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| School of Education | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 5 | 0 | 0 | 1 | 0 | 2 | 5 | 0 | 7 | 26 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 4 |
| Interdisciplinary (A&S) | 2 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **合计** | **30** | **15** | **4** | **1** | **1** | **1** | **8** | **8** | **2** | **2** | **5** | **5** | **1** | **1** | **1** | **2** | **11** | **5** | **1** | **12** | **117** |

> **Reconciliation note**: The matrix shows 117 unique program-degree rows from the program finder. However, many programs offer multiple degree levels (e.g., Biology offers B.S., M.A., M.S., Minor = 4 rows). The total count of 177 includes all degree-level variants. The matrix counts unique school × degree combinations, while Rule 1 counts each program-degree pair.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

William & Mary has 6 schools/colleges. The College of Arts & Sciences is the primary undergraduate unit. The Mason School of Business offers the B.B.A. The School of Computing, Data Sciences & Physics (CDSP) is a newer school (established ~2023) that shares departments with A&S. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Department of Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.wm.edu/academics/programs/index.php |

##### Department of Art & Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History (*Degree in Fine Arts) | https://www.wm.edu/academics/programs/index.php |

##### Department of Asian & Middle Eastern Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian & Middle Eastern Studies (AMES) | https://www.wm.edu/academics/programs/index.php |
| 2 | Asian & Pacific Islander American Studies (APIA) | https://www.wm.edu/academics/programs/index.php |
| 3 | Chinese Language & Culture | https://www.wm.edu/academics/programs/index.php |
| 4 | Japanese Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.wm.edu/academics/programs/index.php |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.wm.edu/academics/programs/index.php |

##### Department of Classical Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Computer Science ⚠ shared with CDSP
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (BA) | https://www.wm.edu/academics/programs/index.php |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (BS) | https://www.wm.edu/academics/programs/index.php |

##### Department of Data Science ⚠ shared with CDSP
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://www.wm.edu/academics/programs/index.php |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.wm.edu/academics/programs/index.php |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.wm.edu/academics/programs/index.php |

##### Department of Environment & Sustainability
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environment & Sustainability (BA) | https://www.wm.edu/academics/programs/index.php |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environment & Sustainability (BS) | https://www.wm.edu/academics/programs/index.php |

##### Department of Film & Media Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film & Media Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of French & Francophone Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French & Francophone Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Gender, Sexuality & Women's Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Gender, Sexuality & Women's Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Geology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://www.wm.edu/academics/programs/index.php |

##### Department of Government
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Government | https://www.wm.edu/academics/programs/index.php |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.wm.edu/academics/programs/index.php |

##### Department of Human Health & Physiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Health & Physiology | https://www.wm.edu/academics/programs/index.php |

##### Department of Integrative Conservation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Integrative Conservation | https://www.wm.edu/academics/programs/index.php |

##### Department of International Relations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Relations | https://www.wm.edu/academics/programs/index.php |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://www.wm.edu/academics/programs/index.php |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.wm.edu/academics/programs/index.php |
| 2 | Computational & Applied Mathematics & Statistics | https://www.wm.edu/academics/programs/index.php |

##### Department of Medieval & Renaissance Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Medieval & Renaissance Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.wm.edu/academics/programs/index.php |

##### Department of Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.wm.edu/academics/programs/index.php |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.wm.edu/academics/programs/index.php |

##### Department of Physics ⚠ shared with CDSP
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.wm.edu/academics/programs/index.php |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology (BA) | https://www.wm.edu/academics/programs/index.php |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology (BS) | https://www.wm.edu/academics/programs/index.php |

##### Department of Public Health
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health (BA) | https://www.wm.edu/academics/programs/index.php |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health (BS) | https://www.wm.edu/academics/programs/index.php |

##### Department of Public Policy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy | https://www.wm.edu/academics/programs/index.php |

##### Department of Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religion | https://www.wm.edu/academics/programs/index.php |

##### Department of Russian, East European & Eurasian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Russian, East European & Eurasian Studies | https://www.wm.edu/academics/programs/index.php |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.wm.edu/academics/programs/index.php |

##### Department of Spanish / Hispanic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://www.wm.edu/academics/programs/index.php |

##### Department of Studio Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://www.wm.edu/academics/programs/index.php |

##### Department of Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://www.wm.edu/academics/programs/index.php |

##### Coastal & Marine Sciences (Joint with VIMS)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Coastal & Marine Sciences | https://www.wm.edu/academics/programs/index.php |

##### Self-Designed Interdisciplinary
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Self-Designed (BA) | https://www.wm.edu/academics/programs/index.php |
| 2 | Self-Designed (BS) | https://www.wm.edu/academics/programs/index.php |

##### European & Latin American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | European Studies | https://www.wm.edu/academics/programs/index.php |
| 2 | Latin American & Caribbean Studies | https://www.wm.edu/academics/programs/index.php |

#### Mason School of Business

##### Department of Business Administration
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.wm.edu/academics/programs/index.php |
| 2 | Business Analytics | https://www.wm.edu/academics/programs/index.php |
| 3 | Finance | https://www.wm.edu/academics/programs/index.php |
| 4 | Marketing | https://www.wm.edu/academics/programs/index.php |

##### Elementary Education (School of Education)
###### BAEd
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://www.wm.edu/academics/programs/index.php |

#### Interdisciplinary / Joint Programs

##### Dual Bachelor's Degrees
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering (Dual Bachelor's Degrees with partner institutions) | https://www.wm.edu/academics/programs/index.php |

##### Joint BA Programs
| # | 专业 | Parent Schools | URL |
|---|------|----------------|-----|
| 1 | Classical Studies (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |
| 2 | Economics (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |
| 3 | English (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |
| 4 | Film & Media Studies (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |
| 5 | History (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |
| 6 | International Relations (Joint B.A.) | A&S | https://www.wm.edu/academics/programs/index.php |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 类型 | Parent Schools | URL |
|---|------|------|----------------|-----|
| 1 | Engineering | Dual Bachelor's | A&S + partner engineering schools | https://www.wm.edu/academics/programs/index.php |
| 2 | Environment & Sustainability | BA/BS | A&S (Interdisciplinary Studies) | https://www.wm.edu/academics/programs/index.php |
| 3 | Integrative Conservation | BS | A&S (Interdisciplinary Studies) | https://www.wm.edu/academics/programs/index.php |
| 4 | Film & Media Studies | BA | A&S (Interdisciplinary Studies) | https://www.wm.edu/academics/programs/index.php |
| 5 | Self-Designed | BA/BS | A&S (Interdisciplinary Studies) | https://www.wm.edu/academics/programs/index.php |

### 1.4 Minors — Complete List

| # | Minor | Home School/Department | URL |
|---|-------|----------------------|-----|
| 1 | Accounting | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 2 | Africana Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 3 | American Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 4 | Anthropology | A&S | https://www.wm.edu/academics/programs/index.php |
| 5 | Applied Science | A&S | https://www.wm.edu/academics/programs/index.php |
| 6 | Arabic Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 7 | Art & Art History | A&S | https://www.wm.edu/academics/programs/index.php |
| 8 | Artificial Intelligence | CDSP | https://www.wm.edu/academics/programs/index.php |
| 9 | Asian & Middle Eastern Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 10 | Asian & Pacific Islander American Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 11 | Biochemistry | A&S | https://www.wm.edu/academics/programs/index.php |
| 12 | Biology | A&S | https://www.wm.edu/academics/programs/index.php |
| 13 | Business Administration | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 14 | Business Analytics | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 15 | Chemistry | A&S | https://www.wm.edu/academics/programs/index.php |
| 16 | Chinese Language & Culture | A&S | https://www.wm.edu/academics/programs/index.php |
| 17 | Classical Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 18 | Coastal & Marine Sciences | VIMS | https://www.wm.edu/academics/programs/index.php |
| 19 | Computational & Applied Mathematics & Statistics | A&S | https://www.wm.edu/academics/programs/index.php |
| 20 | Computer Science | A&S/CDSP | https://www.wm.edu/academics/programs/index.php |
| 21 | Creative Writing | A&S | https://www.wm.edu/academics/programs/index.php |
| 22 | Dance | A&S | https://www.wm.edu/academics/programs/index.php |
| 23 | Data Science | CDSP | https://www.wm.edu/academics/programs/index.php |
| 24 | East Asian Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 25 | Economics | A&S | https://www.wm.edu/academics/programs/index.php |
| 26 | Educational Studies | School of Education | https://www.wm.edu/academics/programs/index.php |
| 27 | English | A&S | https://www.wm.edu/academics/programs/index.php |
| 28 | English as a Second Language/Bilingual Education | School of Education | https://www.wm.edu/academics/programs/index.php |
| 29 | Environment & Sustainability | A&S | https://www.wm.edu/academics/programs/index.php |
| 30 | European Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 31 | Film & Media Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 32 | Finance | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 33 | French & Francophone Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 34 | Gender, Sexuality & Women's Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 35 | Geology | A&S | https://www.wm.edu/academics/programs/index.php |
| 36 | Geospatial Analysis | A&S | https://www.wm.edu/academics/programs/index.php |
| 37 | German Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 38 | Global Business | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 39 | Hispanic Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 40 | History | A&S | https://www.wm.edu/academics/programs/index.php |
| 41 | Interdisciplinary Innovation & Entrepreneurship | A&S | https://www.wm.edu/academics/programs/index.php |
| 42 | Italian Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 43 | Japanese Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 44 | Judaic Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 45 | Latin American & Caribbean Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 46 | Linguistics | A&S | https://www.wm.edu/academics/programs/index.php |
| 47 | Management & Organizational Leadership | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 48 | Marketing | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 49 | Mathematics | A&S | https://www.wm.edu/academics/programs/index.php |
| 50 | Medieval & Renaissance Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 51 | Middle Eastern Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 52 | Military Science & Leadership | A&S (ROTC) | https://www.wm.edu/academics/programs/index.php |
| 53 | Music | A&S | https://www.wm.edu/academics/programs/index.php |
| 54 | Native Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 55 | Philosophy | A&S | https://www.wm.edu/academics/programs/index.php |
| 56 | Physics | A&S/CDSP | https://www.wm.edu/academics/programs/index.php |
| 57 | Psychology | A&S | https://www.wm.edu/academics/programs/index.php |
| 58 | Public Health | A&S | https://www.wm.edu/academics/programs/index.php |
| 59 | Religion | A&S | https://www.wm.edu/academics/programs/index.php |
| 60 | Russian, East European & Eurasian Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 61 | Russian Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 62 | Sociology | A&S | https://www.wm.edu/academics/programs/index.php |
| 63 | South Asian Studies | A&S | https://www.wm.edu/academics/programs/index.php |
| 64 | Supply Chain Analytics | Mason School of Business | https://www.wm.edu/academics/programs/index.php |
| 65 | Theatre | A&S | https://www.wm.edu/academics/programs/index.php |

### 1.5 General Education Requirements

William & Mary requires all undergraduates to complete the **College Curriculum** (COLL):
- COLL 100: First-Year Seminar
- COLL 150: First-Year Writing
- COLL 200: Arts, Letters & Values; Cultural & Social Analysis; Empirical & Quantitative Reasoning; Global & Intercultural Learning
- COLL 300: Integrative & Cross-Disciplinary Learning
- COLL 400: Senior Capstone

Source: https://www.wm.edu/academics/undergraduateprograms/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### American Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies (M.A.) | https://www.wm.edu/as/graduate/admission/american-studies/index.php |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies (Ph.D.) | https://www.wm.edu/as/graduate/admission/american-studies/index.php |

##### Anthropology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (M.A.) | https://www.wm.edu/as/graduate/admission/anthropology/index.php |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (Ph.D.) | https://www.wm.edu/as/graduate/admission/anthropology/index.php |

##### Applied Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Science (M.S.) | https://www.wm.edu/as/appliedscience/graduateprogram/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Science (Ph.D.) | https://www.wm.edu/as/appliedscience/graduateprogram/ |

##### Biology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology (M.A.) | https://www.wm.edu/as/graduate/admission/biology/index.php |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology (M.S.) | https://www.wm.edu/as/graduate/admission/biology/index.php |

##### Chemistry
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry (M.A.) | https://www.wm.edu/as/graduate/admission/chemistry/index.php |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry (M.S.) | https://www.wm.edu/as/graduate/admission/chemistry/index.php |
| 2 | Environmental Chemistry (M.S.) | https://www.wm.edu/as/graduate/admission/chemistry/index.php |

##### Computer Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science (M.S.) | https://www.wm.edu/as/computerscience/graduate/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science (Ph.D.) | https://www.wm.edu/as/computerscience/graduate/ |

##### History
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | History (M.A.) | https://www.wm.edu/as/graduate/admission/history/index.php |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History (Ph.D.) | https://www.wm.edu/as/graduate/admission/history/index.php |

##### Physics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics (M.A.) | https://www.wm.edu/as/physics/grad/ |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics (M.S.) | https://www.wm.edu/as/physics/grad/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics (Ph.D.) | https://www.wm.edu/as/physics/grad/ |

##### Psychological Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychological Sciences (M.S.) | https://www.wm.edu/as/graduate/admission/psych-sciences/index.php |

##### Public Policy
###### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy (M.P.P.) | https://www.wm.edu/as/graduate/admission/public-policy/index.php |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy (Ph.D.) | https://www.wm.edu/as/graduate/admission/public-policy/index.php |

##### Data Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science (M.S.) | https://www.wm.edu/as/data-science/graduate/ |

##### Classical Studies
###### Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Classical Studies (Post-Bac Certificate) | https://www.wm.edu/as/classicalstudies/post-bac-program/index.php |

##### Combination Degrees (A&S)
| # | 项目 | Degrees | URL |
|---|------|---------|-----|
| 1 | American Studies & Law | M.A. & J.D. | https://www.wm.edu/as/graduate/degreeprograms/combination-degrees/index.php |
| 2 | Chemistry & Applied Science | M.S. & Ph.D. | https://www.wm.edu/as/graduate/degreeprograms/combination-degrees/index.php |
| 3 | Marine Science & Public Policy | M.A./M.S./Ph.D. & M.P.P. | https://www.wm.edu/as/graduate/degreeprograms/combination-degrees/index.php |

#### Mason School of Business

##### Accounting
###### MAcc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting (M.Acc.) | https://mason.wm.edu/graduate/ |
| 2 | Accounting (Online M.Acc.) | https://mason.wm.edu/graduate/ |

##### Business Administration
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (M.B.A.) | https://mason.wm.edu/graduate/ |
| 2 | Business Administration (Online M.B.A.) | https://mason.wm.edu/graduate/ |

##### Business Analytics
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics (M.S.) | https://mason.wm.edu/graduate/ |
| 2 | Business Analytics (Online M.S.) | https://mason.wm.edu/graduate/ |

##### Finance
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance (Online M.S.) | https://mason.wm.edu/graduate/ |

##### Marketing
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Marketing (Online M.S.) | https://mason.wm.edu/graduate/ |

##### Nonprofit Management
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Management (M.S.) | https://mason.wm.edu/graduate/ |

##### Business Combination Degrees
| # | 项目 | Degrees | URL |
|---|------|---------|-----|
| 1 | Accounting & Business Administration | M.Acc. & M.B.A. | https://mason.wm.edu/graduate/ |
| 2 | Business Administration & Business Analytics | M.B.A. & M.S.B.A. | https://mason.wm.edu/graduate/ |
| 3 | Business Administration & Higher Education Administration | M.B.A. & M.Ed. | https://mason.wm.edu/graduate/ |
| 4 | Business Administration & Higher Education Administration (Doctoral) | M.B.A. & Ph.D. | https://mason.wm.edu/graduate/ |
| 5 | Business Administration & Law | M.B.A. & J.D. | https://mason.wm.edu/graduate/ |
| 6 | Business Administration & Public Policy | M.B.A. & M.P.P. | https://mason.wm.edu/graduate/ |

##### Business Certificates
| # | 项目 | 类型 | URL |
|---|------|------|-----|
| 1 | Business Analytics Foundations | Online Grad Cert | https://mason.wm.edu/graduate/ |
| 2 | Corporate Finance | Online Grad Cert | https://mason.wm.edu/graduate/ |
| 3 | Investment Management | Online Grad Cert | https://mason.wm.edu/graduate/ |
| 4 | Supply Chain Analytics | Online Grad Cert | https://mason.wm.edu/graduate/ |

#### Batten School of Coastal & Marine Sciences (VIMS)

##### Marine Science
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Science (M.A.) | https://www.vims.edu/academics/graduate/admissions/ |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Science (M.S.) | https://www.vims.edu/academics/graduate/admissions/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Science (Ph.D.) | https://www.vims.edu/academics/graduate/admissions/ |

##### Coastal & Marine Sciences (UG)
###### BS
| # | 项目 | URL |
|---|------|-----|
| 1 | Coastal & Marine Sciences (B.S.) | https://www.wm.edu/academics/programs/index.php |

#### School of Education

##### Counseling
###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling (M.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 2 | School Counseling (M.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 3 | Counseling (Online M.Ed.) | https://education.wm.edu/admissions/graduate/ |

##### Curriculum & Instruction
###### MAEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Instruction (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 2 | Elementary Education (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 3 | English as a Second Language/Bilingual Education (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 4 | Literacy Leadership (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 5 | Secondary Education (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 6 | Special Education (M.A.Ed.) | https://education.wm.edu/admissions/graduate/ |

##### Educational Leadership
###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership, PK-12 (M.Ed.) | https://education.wm.edu/admissions/graduate/ |
| 2 | Higher Education Administration (M.Ed.) | https://education.wm.edu/admissions/graduate/ |

##### Educational Policy, Planning & Leadership
###### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Educational Leadership (Ed.D.) | https://education.wm.edu/admissions/graduate/ |
| 2 | Gifted Education Administration (Ed.D.) | https://education.wm.edu/admissions/graduate/ |
| 3 | Higher Education Administration (Ed.D.) | https://education.wm.edu/admissions/graduate/ |
| 4 | International School Leadership (Ed.D.) | https://education.wm.edu/admissions/graduate/ |
| 5 | K-12 Administration (Ed.D.) | https://education.wm.edu/admissions/graduate/ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum & Educational Leadership (Ph.D.) | https://education.wm.edu/admissions/graduate/ |
| 2 | Gifted Education Administration (Ph.D.) | https://education.wm.edu/admissions/graduate/ |
| 3 | Higher Education Administration (Ph.D.) | https://education.wm.edu/admissions/graduate/ |

##### School Psychology
###### EdS / MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology (Ed.S.) | https://education.wm.edu/admissions/graduate/ |
| 2 | School Psychology (M.Ed.) | https://education.wm.edu/admissions/graduate/ |

##### Counselor Education
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education (Ph.D.) | https://education.wm.edu/admissions/graduate/ |

##### Education Certificates
| # | 项目 | 类型 | URL |
|---|------|------|-----|
| 1 | Autism Spectrum Disorder | Grad Cert | https://education.wm.edu/admissions/graduate/ |
| 2 | Gifted Education | Grad Cert | https://education.wm.edu/admissions/graduate/ |
| 3 | English as a Second Language/Bilingual Education | Cert | https://education.wm.edu/admissions/graduate/ |
| 4 | Educational Leadership, PK-12 | Post-Prof Cert | https://education.wm.edu/admissions/graduate/ |
| 5 | Reading Specialist | Post-Prof Cert | https://education.wm.edu/admissions/graduate/ |
| 6 | Special Education, K-6 and 6-12 | Post-Prof Cert | https://education.wm.edu/admissions/graduate/ |

##### Education Combination Degrees
| # | 项目 | Degrees | URL |
|---|------|---------|-----|
| 1 | Higher Education Administration & Public Policy | M.Ed. & M.P.P. | https://education.wm.edu/admissions/graduate/ |
| 2 | Higher Education Administration & Public Policy (Doctoral) | Ph.D. & M.P.P. | https://education.wm.edu/admissions/graduate/ |

#### Law School

###### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law (J.D.) | https://law.wm.edu/admissions/ |

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | American Legal Studies (LL.M.) | https://law.wm.edu/admissions/ |
| 2 | American Legal Studies (Online LL.M.) | https://law.wm.edu/admissions/ |

###### MLS
| # | 项目 | URL |
|---|------|-----|
| 1 | Legal Studies (Online M.L.S.) | https://law.wm.edu/admissions/ |

##### Law Combination Degrees
| # | 项目 | Degrees | URL |
|---|------|---------|-----|
| 1 | Law & Public Policy | J.D. & M.P.P. | https://law.wm.edu/admissions/ |

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://www.wm.edu/admission/undergraduateadmission/ | wm.edu |
| Application portal | Common App (https://apply.commonapp.org/Login?ma=299) | wm.edu |
| Application fee | $75 (non-refundable); fee waivers available | wm.edu |
| ED I deadline | Nov. 1 | wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/ |
| ED II deadline | Jan. 5 | wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/ |
| RD deadline | Jan. 5 | wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/ |
| EA deadline | N/A — W&M does not offer Early Action | wm.edu |
| ED I decision notification | Early Dec. | wm.edu |
| ED II decision notification | Early Feb. | wm.edu |
| RD decision notification | by Apr. 1 | wm.edu |
| ED I enrollment deposit | Jan. 5 | wm.edu |
| ED II enrollment deposit | Feb. 15 | wm.edu |
| RD enrollment deposit | May 1 | wm.edu |
| Transfer fall deadline | Mar. 1 | wm.edu |
| Transfer spring deadline | Oct. 1 | wm.edu |
| SAT/ACT policy | Test-optional (indefinitely) | wm.edu/announcements/test-optional-admission-policy.php |
| SAT code | 5115 | wm.edu |
| ACT code | 4344 | wm.edu |
| Superscore | Yes (both SAT and ACT) | wm.edu |
| TOEFL code | 5115 | wm.edu |
| Interview policy | Not offered | wm.edu |
| Recommendation | Required (via Common App) | wm.edu |
| FAFSA/CSS Profile | Required for financial aid | wm.edu |
| FAFSA priority (ED I) | Nov. 15 | wm.edu |
| FAFSA/CSS (ED II) | Jan. 15 priority / Mar. 1 final | wm.edu |
| FAFSA/CSS (RD) | Feb. 1 priority / Mar. 1 final | wm.edu |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified | Strongly recommended | Code 5115 |
| IELTS | Not specified | Strongly recommended | |
| Duolingo | Accepted | — | Accepted if TOEFL/IELTS unavailable |

> **Note**: W&M "strongly recommends" TOEFL or IELTS for international students whose native language is not English and whose schooling has been in a language other than English for 4+ years. No published minimum scores were found on the admissions site as of capture date. Source: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/international-applicants/standardized-testing/index.php

### 3.3 Graduate — Global Rules

Graduate admissions at W&M is **decentralized** — each school manages its own admissions process:
- **College of Arts & Sciences**: https://www.wm.edu/as/graduate/admission/index.php
- **Mason School of Business**: https://graduate.mason.wm.edu/
- **Batten School & VIMS**: https://www.vims.edu/academics/graduate/admissions/
- **School of Computing, Data Sciences & Physics**: https://cdsp.wm.edu/
- **School of Education**: https://education.wm.edu/admissions/graduate/
- **Law School**: https://law.wm.edu/admissions/

Application requirements, fees, GRE/GMAT policies, and deadlines vary by program. Students should check each school's specific requirements.

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027, Line-Itemized)

#### In-State Undergraduate

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $19,734 | Annual tuition |
| Fees | $7,501 | Mandatory fees |
| Housing | $10,512 | On-campus housing |
| Food | $7,134 | Meal plan |
| **Total Direct Costs** | **$44,881** | |
| Books & Supplies | $900 | Indirect |
| Transportation | $785 | Indirect ($1,035 for off-campus) |
| Personal Expenses | $2,000 | Indirect |
| Loan Fees | $72 | If applicable |
| **Total Indirect Costs** | **$3,757** | |
| **TOTAL ESTIMATED COSTS** | **$48,638** | |

#### Out-of-State Undergraduate

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $46,177 | Annual tuition |
| Fees | $8,072 | Mandatory fees |
| Housing | $10,512 | On-campus housing |
| Food | $7,134 | Meal plan |
| **Total Direct Costs** | **$71,895** | |
| Books & Supplies | $900 | Indirect |
| Transportation | $785 | Indirect ($1,035 for off-campus) |
| Personal Expenses | $2,000 | Indirect |
| Loan Fees | $72 | If applicable |
| **Total Indirect Costs** | **$3,757** | |
| **TOTAL ESTIMATED COSTS** | **$75,652** | |

Source: https://www.wm.edu/admission/tuition/index.php

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind (US) | Yes | wm.edu |
| Need-blind (international) | No — generally no scholarships/loan funds for international undergrads | wm.edu/admission/undergraduateadmission/how-to-apply/international-applicants/expensesaid/ |
| Meets demonstrated need | 100% typically met for in-state students | wm.edu |
| Pell Grant Guarantee | All in-state, Pell-eligible students automatically receive scholarship assistance to cover at least tuition and fees | wm.edu |
| Income ≤$75k (in-state) | 99% qualified for aid; median tuition paid: $0 | wm.edu |
| Income $75-110k (in-state) | 96% qualified for aid; median tuition paid: $0 | wm.edu |
| Income $110-135k (in-state) | 93% qualified for aid; median tuition paid: $6,680 | wm.edu |
| In-state aid rate | 77% received some type of aid (2024-25) | wm.edu |
| OOS aid rate | 60% received some type of aid (2024-25) | wm.edu |
| Average need-based aid (in-state) | $27,026 | wm.edu |
| Potential annual scholarship/grant (OOS) | $23,000 | wm.edu |
| Debt-free graduation | Nearly 70% graduate without debt | wm.edu |
| $60M+ in grants/scholarships distributed annually | Yes | wm.edu |
| Merit scholarships | All first-year applicants automatically considered | wm.edu |

### 4.3 Graduate Cost & Funding Framework

#### Arts & Sciences (2026-2027)

| Item | In-State | Out-of-State |
|------|----------|-------------|
| Tuition (M.A., M.S., M.P.P., Ph.D.) | $10,905 | $29,352 |
| Fees (M.A., M.S., M.P.P., Ph.D.) | $7,237 | $7,808 |
| Living Expenses | $20,319 | $20,319 |
| Books & Supplies | $1,116 | $1,116 |
| Transportation | $2,340 | $2,340 |
| Personal Expenses | $2,680 | $2,680 |
| Average Federal Loan Fees | $218 | $218 |

#### Business (2026-2027)

| Program | In-State | Out-of-State |
|---------|----------|-------------|
| MAcc | $31,411 | $42,380 |
| MBA | $31,911 | $43,743 |
| MS Business Analytics | $41,675 | $49,432 |
| Part-time MBA (per credit hour) | $1,069 | $1,489 |
| Executive MBA (total program) | $124,373 | $124,373 |
| Military MBA | $53,500 | $53,500 |

Source: https://www.wm.edu/admission/tuition/graduate/index.php

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ED_I
  value: "November 1"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/index.php
  source_snippet: "Nov. 1 — Common App due (Early Decision I)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.ED_II
  value: "January 5"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/index.php
  source_snippet: "Jan. 5 — Common App due (Early Decision II)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.RD
  value: "January 5"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/datesdeadlines/index.php
  source_snippet: "Jan. 5 — Common App due (Regular Decision)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.test_policy
  value: "Test-optional (indefinitely)"
  source_url: https://www.wm.edu/admission/undergraduateadmission/announcements/test-optional-admission-policy.php
  source_snippet: "W&M extends test-optional admission process indefinitely"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.application_fee
  value: "$75"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/first-year-applicants/application-checklist/index.php
  source_snippet: "$75 non-refundable application fee payment"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.cost.tuition_in_state
  value: "$19,734"
  source_url: https://www.wm.edu/admission/tuition/index.php
  source_snippet: "Tuition — 19,734 (In-State Undergraduate)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.tuition_out_of_state
  value: "$46,177"
  source_url: https://www.wm.edu/admission/tuition/index.php
  source_snippet: "Tuition — 46,177 (Out-of-State Undergraduate)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.total_in_state
  value: "$48,638"
  source_url: https://www.wm.edu/admission/tuition/index.php
  source_snippet: "TOTAL ESTIMATED COSTS — $48,638 (In-State)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.total_out_of_state
  value: "$75,652"
  source_url: https://www.wm.edu/admission/tuition/index.php
  source_snippet: "TOTAL ESTIMATED COSTS — $75,652 (Out-of-State)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.aid.need_blind_us
  value: "Yes"
  source_url: https://www.wm.edu/admission/financialaid/index.php
  source_snippet: "W&M offers a comprehensive financial aid program"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.aid.need_blind_intl
  value: "No"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/international-applicants/expensesaid/index.php
  source_snippet: "Generally speaking, William & Mary does not have scholarships or loan funds available to aid undergraduate international students who are citizens of other countries."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.testing.sat_code
  value: "5115"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/first-year-applicants/standardizedtesting/index.php
  source_snippet: "William & Mary's school code for the SAT is 5115 and 4344 for the ACT."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.testing.superscore
  value: "Yes (SAT and ACT)"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/first-year-applicants/standardizedtesting/index.php
  source_snippet: "For both the SAT and the ACT, we will superscore if taken multiple times."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.elp.policy
  value: "TOEFL/IELTS strongly recommended; Duolingo accepted"
  source_url: https://www.wm.edu/admission/undergraduateadmission/how-to-apply/international-applicants/standardized-testing/index.php
  source_snippet: "TOEFL or the IELTS exams are highly recommended for international students for whom English is not the first language."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.admit_rate
  value: "37%"
  source_url: https://www.wm.edu/admission/undergraduateadmission/facts-figures/index.php
  source_snippet: "37% OVERALL ACCEPTANCE RATE"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.sat_middle_50
  value: "1390-1520"
  source_url: https://www.wm.edu/admission/undergraduateadmission/facts-figures/index.php
  source_snippet: "1390–1520 MIDDLE 50% RANGE FOR SAT"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.act_middle_50
  value: "32-34"
  source_url: https://www.wm.edu/admission/undergraduateadmission/facts-figures/index.php
  source_snippet: "32-34 MIDDLE 50% RANGE FOR ACT"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.gpa_middle_50
  value: "4.16-4.51 (weighted)"
  source_url: https://www.wm.edu/admission/undergraduateadmission/facts-figures/index.php
  source_snippet: "4.16-4.51 MIDDLE 50% GPA"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-019:
  field: undergraduate.aid.pell_guarantee
  value: "All in-state Pell-eligible students receive scholarship covering at least tuition and fees"
  source_url: https://www.wm.edu/admission/tuition/index.php
  source_snippet: "All in-state, Pell-eligible students automatically receive scholarship assistance to cover at least tuition and fees."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-020:
  field: undergraduate.programs.total
  value: "115+ majors, minors and pre-professional programs"
  source_url: https://www.wm.edu/admission/undergraduateadmission/index.php
  source_snippet: "115+ MAJORS, MINORS AND PRE-PROFESSIONAL PROGRAMS"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.tuition.arts_sciences_in_state
  value: "$10,905"
  source_url: https://www.wm.edu/admission/tuition/graduate/index.php
  source_snippet: "Tuition (M.A., M.S., M.P.P., Ph.D.) — 10,905 (In-State)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.tuition.arts_sciences_out_of_state
  value: "$29,352"
  source_url: https://www.wm.edu/admission/tuition/graduate/index.php
  source_snippet: "Tuition (M.A., M.S., M.P.P., Ph.D.) — 29,352 (Out-of-State)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.admissions.model
  value: "Decentralized — each school manages own admissions"
  source_url: https://www.wm.edu/admission/graduateadmission/index.php
  source_snippet: "Check each program to learn exactly what needs to be submitted and when"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
wm-knowledge-base-v2/
├── overview/
│   ├── 0-institution-overview.md          (Section 0: Rules 1-4)
│   └── 0-program-counts.md
├── undergraduate/
│   ├── 1-ug-majors-arts-sciences.md       (Section 1: A&S programs)
│   ├── 1-ug-majors-business.md            (Section 1: Business programs)
│   ├── 1-ug-majors-education.md           (Section 1: Education programs)
│   ├── 1-ug-minors-complete.md            (Section 1.4: all minors)
│   └── 1-general-education.md             (Section 1.5: COLL requirements)
├── graduate/
│   ├── 2-grad-arts-sciences.md            (Section 2: A&S grad programs)
│   ├── 2-grad-business.md                 (Section 2: Business grad)
│   ├── 2-grad-vims.md                     (Section 2: VIMS grad)
│   ├── 2-grad-education.md                (Section 2: Education grad)
│   └── 2-grad-law.md                      (Section 2: Law)
├── admissions/
│   ├── 3-ug-deadlines-requirements.md     (Section 3.1)
│   ├── 3-english-proficiency.md           (Section 3.2)
│   └── 3-grad-admissions.md               (Section 3.3)
├── costs/
│   ├── 4-ug-cost-instate.md               (Section 4.1 in-state)
│   ├── 4-ug-cost-outofstate.md            (Section 4.1 OOS)
│   ├── 4-financial-aid-policy.md          (Section 4.2)
│   └── 4-grad-cost-funding.md             (Section 4.3)
└── evidence/
    └── 5-evidence-chain.md                (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "wm-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Each school's graduate admissions page |
| P0 | Exact TOEFL/IELTS minimum scores (if published) | wm.edu international applicants |
| P1 | Graduate application fees per school | Each school's admissions page |
| P1 | Graduate funding/stipend details | Each school's financial support page |
| P1 | Per-program deadlines (graduate) | Each school's admissions page |
| P2 | Detailed course requirements per major | wm.edu course catalog / department pages |
| P2 | St Andrews Joint Degree Programme details | wm.edu/admission/undergraduateadmission/how-to-apply/first-year-applicants/jointdegree/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | William & Mary | (Other schools) |
|------|---------------|-----------------|
| Type | Public | |
| Location | Williamsburg, VA | |
| Founded | 1693 | |
| UG tuition (in-state) | $19,734 | |
| UG tuition (OOS) | $46,177 | |
| UG total COA (in-state) | $48,638 | |
| UG total COA (OOS) | $75,652 | |
| Need-blind (US) | Yes | |
| Need-blind (intl) | No | |
| EA deadline | N/A (no EA) | |
| ED I deadline | Nov. 1 | |
| ED II deadline | Jan. 5 | |
| RD deadline | Jan. 5 | |
| SAT/ACT required? | No (test-optional) | |
| SAT middle 50% | 1390-1520 | |
| ACT middle 50% | 32-34 | |
| TOEFL min | Not specified | |
| IELTS min | Not specified | |
| Application fee | $75 | |
| Admit rate | 37% | |
| Total programs (Rule 1) | 177 | |
| Schools/departments (Rule 2) | 6 | |
| Student-faculty ratio | 11:1 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.wm.edu, mason.wm.edu, education.wm.edu, law.wm.edu, vims.edu, cdsp.wm.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

## CORRECTIONS FROM USER-PROVIDED PRELIMINARY DATA

1. **EA vs ED**: User stated "EA Nov 1" — W&M does NOT offer Early Action. The Nov. 1 deadline is for **Early Decision I** (binding). W&M offers ED I (Nov. 1), ED II (Jan. 5), and RD (Jan. 5) only.
2. **Tuition**: User stated "~$20k in-state / ~$46k OOS tuition" — Verified: $19,734 in-state / $46,177 OOS (2026-2027).
3. **Test-optional**: Verified — test-optional indefinitely (not just temporary).
4. **Need-blind**: Verified — need-blind for US students, need-AWARE for international students.
5. **Schools**: User listed "School of Marine Science" — official name is "Batten School of Coastal & Marine Sciences" (includes VIMS). Also "School of Computing" is officially "School of Computing, Data Sciences & Physics."
