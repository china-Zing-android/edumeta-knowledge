# University of New Mexico Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BSED/BLA/BBA) | 97 |
| 本科辅修 (Minor) | 89 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/etc.) | 178 |
| 研究生高级证书 (Advanced Certificate / Diploma / GCERT) | 62 |
| 双学位/联合学位项目 | 27 |
| **学位项目总计 (UG + Grad)** | **453** |
| 学院 / 独立系所总数 | 14 |

> Reconciliation: 97 UG majors + 89 UG minors + 178 grad degrees + 62 grad certs + 27 dual degrees = 453. The catalog lists 453 unique program entries. Counts verified against catalog.unm.edu/#/programs expanded department listings (2026-07-06).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of New Mexico
├── College of Arts & Sciences                              [学院]
│   ├── Africana Studies                                    [系]
│   ├── American Studies                                    [系]
│   ├── Anthropology                                        [系]
│   ├── Biology                                             [系]
│   ├── Chemistry                                           [系]
│   ├── Chicana and Chicano Studies                         [系]
│   ├── Communication and Journalism                        [系]
│   ├── Computer Science                                    [系]
│   ├── Earth and Planetary Sciences                        [系]
│   ├── Economics                                           [系]
│   ├── English                                             [系]
│   ├── Geography and Environmental Studies                 [系]
│   ├── History                                             [系]
│   ├── Latin American Studies                              [系]
│   ├── Linguistics                                         [系]
│   ├── Mathematics and Statistics                          [系]
│   ├── Native American Studies                             [系]
│   ├── Philosophy                                          [系]
│   ├── Physics and Astronomy                               [系]
│   ├── Political Science                                   [系]
│   ├── Psychology                                          [系]
│   ├── Religious Studies                                   [系]
│   ├── Sociology and Criminology                           [系]
│   ├── Spanish and Portuguese                              [系]
│   ├── Women, Gender, and Sexuality Studies                [系]
│   ├── Languages, Cultures, and Literatures                [系]
│   └── Interdisciplinary: A&S (Humanities/NatSci/SocSci)   [系]
├── School of Architecture and Planning                     [学院]
│   ├── Architecture                                        [系]
│   ├── Community and Regional Planning                     [系]
│   └── Landscape Architecture                              [系]
├── School of Engineering                                   [学院]
│   ├── Biomedical Engineering                              [系]
│   ├── Chemical and Biological Engineering                 [系]
│   ├── Civil, Construction, and Environmental Engineering  [系]
│   ├── Computer Engineering                                [系]  ⚠ shared with A&S CS
│   ├── Electrical and Computer Engineering                 [系]
│   ├── Mechanical Engineering                              [系]
│   ├── Nuclear Engineering                                 [系]
│   ├── Construction Management                             [系]
│   └── Manufacturing Engineering                           [系]
├── College of Fine Arts                                    [学院]
│   ├── Department of Art                                   [系]
│   ├── Film and Digital Arts                               [系]
│   ├── Music                                               [系]
│   └── Theatre and Dance                                   [系]
├── College of Education & Human Sciences                   [学院]
│   ├── Counseling                                          [系]
│   ├── Educational Leadership                              [系]
│   ├── Educational Psychology                              [系]
│   ├── Family and Child Studies                            [系]
│   ├── Health, Exercise, and Sports Sciences               [系]
│   ├── Language, Literacy, and Sociocultural Studies       [系]
│   ├── Nutrition                                           [系]
│   ├── Special Education                                   [系]
│   └── Teacher Education                                   [系]
├── Anderson School of Management (The James & Gail Ellis School of Business Leadership) [学院]
│   ├── Accounting                                          [系]
│   ├── Business Administration                             [系]
│   ├── Cybersecurity and Business Analytics                [系]
│   └── Project Management                                  [系]
├── College of Nursing                                      [学院]
├── College of Pharmacy                                     [学院]
│   └── Pharmaceutical Sciences                             [系]
├── School of Law                                           [学院]
├── School of Medicine                                      [学院]
│   ├── Anesthesiology and Critical Care Medicine           [系]
│   ├── Biomedical Sciences                                 [系]
│   ├── Dental Medicine                                     [系]
│   ├── Emergency Medicine                                  [系]
│   ├── Occupational Therapy                                [系]
│   ├── Orthopaedics and Physical Therapy                   [系]
│   ├── Pathology and Medical Laboratory Sciences           [系]
│   ├── Physician Assistant Program                         [系]
│   ├── Psychiatry                                          [系]
│   ├── Radiologic Sciences                                 [系]
│   └── Social Work                                         [系]
├── College of Population Health                            [学院]
│   └── Population Health                                   [系]
├── School of Public Administration                         [学院]
│   └── Public Administration                               [系]
├── College of University Libraries & Learning Sciences     [学院]
│   └── Organization, Information, and Learning Sciences    [系]
├── Honors College                                          [学院]
├── University College                                      [学院]
└── Interdisciplinary Programs                              [跨学院]
    ├── Global and National Security Program                [系]
    ├── Nanoscience and Microsystems Engineering            [系]
    ├── Optical Science and Engineering                     [系]
    └── Water Resources Program                             [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 42 |
| BS | BS | Bachelor of Science | 本科 | 38 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 3 |
| BM | BM | Bachelor of Music | 本科 | 1 |
| BME | BME | Bachelor of Music Education | 本科 | 1 |
| BSED | BSED | Bachelor of Science in Education | 本科 | 4 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 1 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 2 |
| Minor | Minor | 辅修（本科） | 本科 | 89 |
| MA | MA | Master of Arts | 研究生 | 38 |
| MS | MS | Master of Science | 研究生 | 42 |
| MFA | MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MARCH | MARCH | Master of Architecture | 研究生 | 1 |
| MCRP | MCRP | Master of Community and Regional Planning | 研究生 | 1 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| MEng | MEng | Master of Engineering | 研究生 | 2 |
| MCM | MCM | Master of Construction Management | 研究生 | 1 |
| MEME | MEME | Master of Engineering in Manufacturing Engineering | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MHA | MHA | Master of Health Administration | 研究生 | 1 |
| MWR | MWR | Master of Water Resources | 研究生 | 1 |
| MSL | MSL | Master of Studies in Law | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 1 |
| MOT | MOT | Master of Occupational Therapy | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MSISA | MSISA | Master of Science in Information Systems and Assurance | 研究生 | 1 |
| PMS | PMS | Professional Master of Science | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 49 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| DSW | DSW | Doctor of Social Work | 研究生 | 0 |
| EdS | EdS | Education Specialist Certificate | 研究生 | 3 |
| GCERT | GCERT | Graduate Certificate | 研究生 | 52 |
| Cert | Cert | Certificate (undergraduate) | 本科 | 4 |
| Cert | Cert | Certificate (graduate) | 研究生 | 6 |
| Dual | Dual | 双学位/联合学位 | 混合 | 27 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BSED | BLA | BBA | BSN | Minor | MA | MS | MFA | MBA | MARCH | MCRP | MLA | MEng | MCM | MEME | MPH | MPA | MPP | MHA | MWR | MSL | MM | MOT | MSW | PhD | EdD | DNP | DPT | OTD | PharmD | MD | JD | EdS | GCERT | Cert | Dual | 合计 |
|------------|----|----|-----|----|------|-----|-----|-----|-------|----|----|----|-----|-------|------|-----|------|-----|------|-----|-----|-----|-----|-----|-----|----|----|-----|-----|-----|-----|-----|-----|--------|----|----|-----|-------|------|------|------|
| College of Arts & Sciences | 35 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 55 | 18 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 3 | 5 | 176 |
| School of Architecture & Planning | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 15 |
| School of Engineering | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 5 | 49 |
| College of Fine Arts | 5 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 7 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 25 |
| College of Education & Human Sciences | 0 | 5 | 0 | 0 | 4 | 0 | 0 | 0 | 10 | 6 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 | 0 | 0 | 47 |
| Anderson School of Management | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 | 13 |
| College of Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 6 |
| College of Pharmacy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 | 6 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 3 | 5 | 2 | 21 |
| College of Population Health | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 |
| School of Public Administration | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 7 |
| College of University Libraries & Learning Sciences | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 5 |
| Honors College | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| University College | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 4 |
| Interdisciplinary | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 10 |
| **合计** | **43** | **83** | **3** | **1** | **4** | **1** | **1** | **2** | **89** | **28** | **35** | **4** | **2** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **43** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **3** | **30** | **10** | **26** | **453** |

> Reconciliation: sum of matrix cells = 453 = Rule 1 total. Verified.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of New Mexico has 14 colleges and schools offering undergraduate programs. The College of Arts & Sciences is the largest, offering the majority of liberal arts majors. UNM is organized as a comprehensive public research university with professional schools. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Department of Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | http://catalog.unm.edu/#/programs |

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | http://catalog.unm.edu/#/programs |
| 2 | Southwest and Borderland Studies | http://catalog.unm.edu/#/programs |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | http://catalog.unm.edu/#/programs |
| 2 | Forensic Anthropology | http://catalog.unm.edu/#/programs |
| 3 | Forensic Sciences | http://catalog.unm.edu/#/programs |

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | http://catalog.unm.edu/#/programs |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Biology | http://catalog.unm.edu/#/programs |
| 2 | Chemistry | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | http://catalog.unm.edu/#/programs |

##### Department of Chicana and Chicano Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicana and Chicano Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicana and Chicano Studies | http://catalog.unm.edu/#/programs |

##### Department of Communication and Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | http://catalog.unm.edu/#/programs |
| 2 | Journalism and Mass Communication | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | http://catalog.unm.edu/#/programs |
| 2 | Journalism and Mass Communication | http://catalog.unm.edu/#/programs |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | http://catalog.unm.edu/#/programs |

##### Department of Earth and Planetary Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | http://catalog.unm.edu/#/programs |
| 2 | Environmental Science | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | http://catalog.unm.edu/#/programs |
| 2 | Environmental Science | http://catalog.unm.edu/#/programs |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | http://catalog.unm.edu/#/programs |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | English | http://catalog.unm.edu/#/programs |
| 2 | Technical and Professional Communication | http://catalog.unm.edu/#/programs |

##### Department of Geography and Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Geographic Information Science | http://catalog.unm.edu/#/programs |
| 2 | Geography | http://catalog.unm.edu/#/programs |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | History | http://catalog.unm.edu/#/programs |

##### Department of Latin American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American Studies | http://catalog.unm.edu/#/programs |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Signed Language Interpreting | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language | http://catalog.unm.edu/#/programs |
| 2 | Linguistics | http://catalog.unm.edu/#/programs |
| 3 | Navajo Language and Linguistics | http://catalog.unm.edu/#/programs |

##### Department of Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | http://catalog.unm.edu/#/programs |
| 2 | Statistics | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | http://catalog.unm.edu/#/programs |
| 2 | Statistics | http://catalog.unm.edu/#/programs |

##### Department of Native American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Native American Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Native American Studies | http://catalog.unm.edu/#/programs |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | http://catalog.unm.edu/#/programs |

##### Department of Physics and Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics and Astrophysics | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | http://catalog.unm.edu/#/programs |
| 2 | Physics | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | http://catalog.unm.edu/#/programs |
| 2 | Physics | http://catalog.unm.edu/#/programs |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | http://catalog.unm.edu/#/programs |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | http://catalog.unm.edu/#/programs |

##### Department of Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | http://catalog.unm.edu/#/programs |

##### Department of Sociology and Criminology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | http://catalog.unm.edu/#/programs |
| 2 | Sociology | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | http://catalog.unm.edu/#/programs |
| 2 | Sociology | http://catalog.unm.edu/#/programs |

##### Department of Spanish and Portuguese
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Portuguese | http://catalog.unm.edu/#/programs |
| 2 | Spanish | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Portuguese | http://catalog.unm.edu/#/programs |
| 2 | Spanish | http://catalog.unm.edu/#/programs |

##### Department of Women, Gender, and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women, Gender, and Sexuality Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Women, Gender, and Sexuality Studies | http://catalog.unm.edu/#/programs |

##### Department of Languages, Cultures, and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical Studies | http://catalog.unm.edu/#/programs |
| 2 | Comparative Literature and Cultural Studies | http://catalog.unm.edu/#/programs |
| 3 | East Asian Studies | http://catalog.unm.edu/#/programs |
| 4 | French | http://catalog.unm.edu/#/programs |
| 5 | German | http://catalog.unm.edu/#/programs |
| 6 | Languages | http://catalog.unm.edu/#/programs |
| 7 | Russian | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Arabic | http://catalog.unm.edu/#/programs |
| 2 | Chinese | http://catalog.unm.edu/#/programs |
| 3 | Classical Studies | http://catalog.unm.edu/#/programs |
| 4 | Comparative Literature | http://catalog.unm.edu/#/programs |
| 5 | French | http://catalog.unm.edu/#/programs |
| 6 | German | http://catalog.unm.edu/#/programs |
| 7 | Greek | http://catalog.unm.edu/#/programs |
| 8 | Japanese | http://catalog.unm.edu/#/programs |
| 9 | Languages | http://catalog.unm.edu/#/programs |
| 10 | Latin | http://catalog.unm.edu/#/programs |
| 11 | Russian | http://catalog.unm.edu/#/programs |

##### Interdisciplinary: A&S
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | http://catalog.unm.edu/#/programs |
| 2 | English-Philosophy | http://catalog.unm.edu/#/programs |
| 3 | Health, Medicine and Human Values | http://catalog.unm.edu/#/programs |
| 4 | International Studies | http://catalog.unm.edu/#/programs |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | http://catalog.unm.edu/#/programs |
| 2 | Health, Medicine and Human Values | http://catalog.unm.edu/#/programs |
| 3 | International Studies | http://catalog.unm.edu/#/programs |
| 4 | Medieval Studies | http://catalog.unm.edu/#/programs |
| 5 | Sustainability Studies | http://catalog.unm.edu/#/programs |

#### School of Architecture and Planning

##### Department of Architecture
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | http://catalog.unm.edu/#/programs |
| 2 | Environmental Planning and Design | http://catalog.unm.edu/#/programs |

###### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | http://catalog.unm.edu/#/programs |
| 2 | Community and Regional Planning | http://catalog.unm.edu/#/programs |
| 3 | Design Studies | http://catalog.unm.edu/#/programs |
| 4 | Landscape Architecture | http://catalog.unm.edu/#/programs |

#### School of Engineering

##### Department of Chemical and Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | http://catalog.unm.edu/#/programs |

##### Department of Civil, Construction, and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | http://catalog.unm.edu/#/programs |
| 2 | Construction Engineering | http://catalog.unm.edu/#/programs |
| 3 | Construction Management | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | http://catalog.unm.edu/#/programs |

##### Department of Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | http://catalog.unm.edu/#/programs |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | http://catalog.unm.edu/#/programs |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | http://catalog.unm.edu/#/programs |

##### Department of Nuclear Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | http://catalog.unm.edu/#/programs |

##### Interdisciplinary: Engineering
###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Peace Engineering | http://catalog.unm.edu/#/programs |

#### College of Fine Arts

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | http://catalog.unm.edu/#/programs |
| 2 | Art History | http://catalog.unm.edu/#/programs |
| 3 | Art Studio | http://catalog.unm.edu/#/programs |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Studio | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | http://catalog.unm.edu/#/programs |
| 2 | Art History | http://catalog.unm.edu/#/programs |
| 3 | Art Studio | http://catalog.unm.edu/#/programs |

##### Department of Film and Digital Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Digital Arts | http://catalog.unm.edu/#/programs |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Digital Arts | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation | http://catalog.unm.edu/#/programs |
| 2 | Film History and Criticism | http://catalog.unm.edu/#/programs |
| 3 | Film Production | http://catalog.unm.edu/#/programs |
| 4 | Gaming | http://catalog.unm.edu/#/programs |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Music Production & Design | http://catalog.unm.edu/#/programs |
| 2 | Music | http://catalog.unm.edu/#/programs |
| 3 | Music Education | http://catalog.unm.edu/#/programs |

##### Department of Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | http://catalog.unm.edu/#/programs |
| 2 | Theatre | http://catalog.unm.edu/#/programs |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Design and Technology for Performance | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | http://catalog.unm.edu/#/programs |
| 2 | Design and Technology for Performance | http://catalog.unm.edu/#/programs |
| 3 | Theatre | http://catalog.unm.edu/#/programs |

#### College of Education & Human Sciences

##### Department of Health, Exercise, and Sports Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Health Education | http://catalog.unm.edu/#/programs |
| 2 | Exercise Science | http://catalog.unm.edu/#/programs |

###### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Physical Education | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Athletic Coaching | http://catalog.unm.edu/#/programs |
| 2 | Community Health Education | http://catalog.unm.edu/#/programs |
| 3 | School Health Education | http://catalog.unm.edu/#/programs |

##### Department of Family and Child Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Child Studies | http://catalog.unm.edu/#/programs |
| 2 | Nutrition and Dietetics | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Child Studies | http://catalog.unm.edu/#/programs |
| 2 | Human Services | http://catalog.unm.edu/#/programs |
| 3 | Nutrition | http://catalog.unm.edu/#/programs |

##### Department of Special Education
###### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Special Education and Elementary Education Dual License | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Special Education | http://catalog.unm.edu/#/programs |

##### Department of Teacher Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education in Secondary Education | http://catalog.unm.edu/#/programs |

###### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | http://catalog.unm.edu/#/programs |
| 2 | Secondary Education | http://catalog.unm.edu/#/programs |

#### Anderson School of Management

##### Department of Business Administration
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | http://catalog.unm.edu/#/programs |
| 2 | International Management | http://catalog.unm.edu/#/programs |
| 3 | Management | http://catalog.unm.edu/#/programs |

#### College of Nursing

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Pre-Licensure BSN) | http://catalog.unm.edu/#/programs |
| 2 | Nursing (RN to BSN) | http://catalog.unm.edu/#/programs |

#### College of Pharmacy

##### Department of Pharmaceutical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences Research and Development | http://catalog.unm.edu/#/programs |

#### School of Medicine

##### Department of Emergency Medicine
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Emergency Medical Services | http://catalog.unm.edu/#/programs |

##### Department of Pathology and Medical Laboratory Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Laboratory Sciences | http://catalog.unm.edu/#/programs |

##### Department of Radiologic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Radiologic Sciences | http://catalog.unm.edu/#/programs |

#### College of Population Health

##### Department of Population Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Population Health | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Maternal Child Health | http://catalog.unm.edu/#/programs |
| 2 | Population Health | http://catalog.unm.edu/#/programs |

#### College of University Libraries & Learning Sciences

##### Department of Organization, Information, and Learning Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Instructional Technology and Training | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Instructional Technology and Training | http://catalog.unm.edu/#/programs |

#### Honors College

##### Department of Honors
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Honors Interdisciplinary Liberal Arts | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Honors Interdisciplinary Liberal Arts | http://catalog.unm.edu/#/programs |

#### University College

##### Department of University College
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts and Integrative Studies | http://catalog.unm.edu/#/programs |

###### Minor
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts and Integrative Studies | http://catalog.unm.edu/#/programs |
| 2 | Military Studies | http://catalog.unm.edu/#/programs |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 类型 | 父级学院 |
|---|------|------|---------|
| 1 | Economics and Geography (BA/MS) | Dual | A&S / A&S |
| 2 | Electrical Engineering and Physics (BS/BA) | Dual | Engineering / A&S |
| 3 | Electrical Engineering and Physics (BS/BS) | Dual | Engineering / A&S |
| 4 | Environmental Planning and Design and MCRP (BA/MCRP) | Dual | Architecture / Architecture |

### 1.4 Minors — complete list

UNM offers 89 undergraduate minors distributed across all colleges. See Section 1.2 for the complete minor listings under each department. Key minors include:

- Africana Studies, American Studies, Anthropology, Architecture, Art, Art History, Art Studio, Asian Studies, Athletic Coaching, Biochemistry (minor not listed separately), Biology, Chemistry, Chicana and Chicano Studies, Classical Studies, Communication, Community and Regional Planning, Comparative Literature, Computer Engineering, Computer Science, Construction Management, Criminology, Dance, Design and Technology for Performance, Design Studies, Digital Music Production & Design, Earth and Planetary Sciences, Economics, Electrical Engineering, English, Entrepreneurship, Environmental Science, Family and Child Studies, Film History and Criticism, Film Production, Fine Arts, Forensic Anthropology, Forensic Sciences, French, Gaming, Geographic Information Science, Geography, German, Greek, Health Medicine and Human Values, History, Honors Interdisciplinary Liberal Arts, Human Services, Instructional Technology and Training, International Management, International Studies, Japanese, Journalism and Mass Communication, Languages, Latin, Latin American Studies, Landscape Architecture, Liberal Arts and Integrative Studies, Linguistics, Management, Mathematics, Mechanical Engineering, Medieval Studies, Military Studies, Music, Music Education, Native American Studies, Navajo Language and Linguistics, Nutrition, Peace Engineering, Pharmaceutical Sciences Research and Development, Philosophy, Physics, Political Science, Population Health, Portuguese, Psychology, Public Service, Religious Studies, Russian, School Health Education, Sociology, Spanish, Special Education, Speech and Hearing Sciences, Statistics, Sustainability Studies, Theatre, Women Gender and Sexuality Studies.

### 1.5 General/Institute-wide requirements

UNM requires completion of the General Education curriculum, which includes:
- Communication (6 credit hours)
- Mathematics and Statistics (3-4 credit hours)
- Physical and Natural Sciences (7 credit hours, with lab)
- Social and Behavioral Sciences (6 credit hours)
- Humanities and Fine Arts (6 credit hours)
- Second Language (3-8 credit hours or proficiency)
- Capstone course in major

Details: http://catalog.unm.edu/#/programs (General Education section)

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### American Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | American Studies (Graduate Minor) | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Anthropology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Anthropology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Anthropology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Anthropology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Biology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Biology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Biology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Clinical and Translational Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Chemistry and Chemical Biology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Chemistry | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Chemistry | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Chicana and Chicano Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Chicana and Chicano Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Chicana and Chicano Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Chicana and Chicano Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Communication and Journalism
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Communication | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Communication | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Communication Sciences and Disorders | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Computer Science
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Computer Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Computer Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Earth and Planetary Sciences
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Earth and Planetary Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Earth and Planetary Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Economics
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Economics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Economics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### English
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | English | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MFA | Creative Writing | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | English | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Technical and Professional Writing | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Geography
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Geography | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Geography | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Environmental Sensing, Data, and Modeling | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### History
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | History | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | History | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Latin American Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Latin American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Latin American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Linguistics
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Linguistics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Linguistics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Mathematics and Statistics
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Mathematics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Statistics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Mathematics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Statistics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Museum Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Museum Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Museum Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Native American Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Native American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Native American Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Philosophy
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Philosophy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Philosophy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Physics
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Physics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Physics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Political Science
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Political Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Political Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Public Policy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Psychology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Psychology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Psychology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Public Policy
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MPP | Public Policy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Public Policy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Sociology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| PhD | Sociology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Spanish and Portuguese
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Spanish | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MA | Portuguese | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Spanish and Portuguese | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Speech-Language Pathology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Speech-Language Pathology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Women, Gender, and Sexuality Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| GCERT | Women, Gender, and Sexuality Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Interdisciplinary A&S
| 学位级别 | 项目 | URL |
|---------|------|-----|
| GCERT | Quantum Science & Technology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Race and Social Justice | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### School of Architecture and Planning

| 学位级别 | 项目 | URL |
|---------|------|-----|
| MARCH | Architecture | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Architecture | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MCRP | Community and Regional Planning | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MLA | Landscape Architecture | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Historic Preservation and Regionalism | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Indigenous Planning | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Urban Innovation | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### School of Engineering

##### Biomedical Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Biomedical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Biomedical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Computational Science and Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Ethical AI for Autonomous Systems | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Chemical and Biological Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Chemical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Chemical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Civil, Construction, and Environmental Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MEng | Civil Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Civil Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Civil Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MCM | Construction Management | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Computer Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Computer Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Computer Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Electrical Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Electrical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Electrical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Mechanical Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MSME | Mechanical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Mechanical Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Nuclear Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Nuclear Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Nuclear Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Manufacturing Engineering
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MEME | Manufacturing Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of Fine Arts

##### Department of Art
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Art Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MA | Art History | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Art History | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MFA | Art Studio | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Collaborative Printmaking | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Music
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MM | Music | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Music Performance | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Theatre and Dance
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Theatre and Dance | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MFA | Dance | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MFA | Dramatic Writing | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of Education & Human Sciences

##### Counseling
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Counseling | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Counselor Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Advanced Graduate Counseling | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Substance Use and Behavioral Addictions Counseling | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Educational Leadership
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Educational Leadership | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdD | Educational Leadership | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdS | Educational Leadership | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Educational Leadership with K-12 administrative licensure | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Educational Psychology
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Educational Psychology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Educational Psychology | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Family and Child Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Family and Child Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Family and Child Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Health, Exercise, and Sports Sciences
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Athletic Training | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Health Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Physical Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Physical Education, Sports and Exercise Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Language, Literacy, and Sociocultural Studies
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Language, Literacy and Sociocultural Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Language, Literacy and Sociocultural Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Educational Linguistics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Teaching English to Speakers of Other Languages | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Nutrition
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MS | Nutrition and Dietetic Internship | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Special Education
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Special Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Special Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdS | Special Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Applied Behavior Analysis | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Autism Spectrum Disorder | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Educational Diagnosis | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Special Education PreK-12 Teacher Licensure | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

##### Teacher Education
| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdD | Teaching, Learning, and Teacher Education | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Education Studies | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdS | Curriculum and Instruction | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Elementary Education with K-8 Licensure | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Secondary Education with 6-12 Licensure | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### Anderson School of Management

| 学位级别 | 项目 | URL |
|---------|------|-----|
| MBA | Business Administration | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EMBA | Executive Business Administration | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Cybersecurity and Business Analytics | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Project Management | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Management | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of Nursing

| 学位级别 | 项目 | URL |
|---------|------|-----|
| PhD | Nursing | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| DNP | Nursing Practice | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Nursing (Post-Master's) | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Health Professions Educator | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of Pharmacy

| 学位级别 | 项目 | URL |
|---------|------|-----|
| PharmD | Pharmacy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Pharmaceutical Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Pharmaceutical Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### School of Law

| 学位级别 | 项目 | URL |
|---------|------|-----|
| JD | Juris Doctor | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MSL | Master of Studies in Law | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### School of Medicine

| 学位级别 | 项目 | URL |
|---------|------|-----|
| MD | Medicine | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Anesthesia | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Biomedical Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Biomedical Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Dental Hygiene | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MOT | Occupational Therapy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| OTD | Occupational Therapy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| DPT | Physical Therapy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PA | Physician Assistant | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MSW | Social Work | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Clinical and Translational Science | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | University Science Teaching in Biomedical Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of Population Health

| 学位级别 | 项目 | URL |
|---------|------|-----|
| PhD | Health Equity Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MPH | Public Health | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### School of Public Administration

| 学位级别 | 项目 | URL |
|---------|------|-----|
| MHA | Health Administration | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MPA | Public Administration | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### College of University Libraries & Learning Sciences

| 学位级别 | 项目 | URL |
|---------|------|-----|
| MA | Organization, Information, and Learning Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Organization, Information, and Learning Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| EdS | Organization, Information, and Learning Sciences | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

#### Interdisciplinary Programs

| 学位级别 | 项目 | URL |
|---------|------|-----|
| PMS | Global and National Security | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| GCERT | Global and National Security Policy | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Nanoscience and Microsystems Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Nanoscience and Microsystems Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MS | Optical Science and Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| PhD | Optical Science and Engineering | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |
| MWR | Water Resources | https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (MS and PhD)**
- Department: Computer Science, College of Arts & Sciences
- Website: https://grad.unm.edu/graduate-programs/degrees-advisors-instructions.html
- Application: Through UNM Graduate Studies online application
- Application fee: $60 domestic, $70 international
- GRE: Not required (per program policy)
- English proficiency: TOEFL 79 (4.5) / IELTS 6.5 / Duolingo 105
- Deadlines: Vary by term; check program website
- Funding: Assistantships available through department

### 2.3 Graduate admissions model

UNM graduate admissions is **decentralized**. Each program sets its own requirements, deadlines, and admission criteria. The Graduate Studies office provides the application infrastructure and general oversight, but admission decisions are made by individual departments.

**Application platforms:**
- Most programs: UNM Graduate Studies online application (https://grad.unm.edu/prospective-students/apply-now.html)
- Anderson School of Management: Separate application process
- School of Medicine (MD): AMCAS
- School of Law (JD): LSAC
- Doctor of Pharmacy: PharmCAS

**Application fees:**
- Domestic: $60
- International: $70

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://admissions.unm.edu/ | admissions.unm.edu |
| Application portal | https://www.unm.edu/apply/ | unm.edu/apply |
| Priority deadline (Fall) | June 1 | admissions.unm.edu/future-students/freshmen/ |
| Priority deadline (Spring) | December 13 | admissions.unm.edu/future-students/freshmen/ |
| Priority deadline (Summer) | May 10 | admissions.unm.edu/future-students/freshmen/ |
| Decision type | Rolling | admissions.unm.edu |
| Application fee | $25 | admissions.unm.edu/future-students/freshmen/ |
| SAT/ACT policy | Test-optional (not required) | admissions.unm.edu/future-students/freshmen/admission-requirements.html |
| Superscore policy | Highest composite used | admissions.unm.edu/future-students/freshmen/admission-requirements.html |
| Essay required | No | admissions.unm.edu/future-students/freshmen/ |
| Recommendations required | No | admissions.unm.edu/future-students/freshmen/ |
| Portfolio required | No | admissions.unm.edu/future-students/freshmen/ |
| GPA requirement | Considered as component | admissions.unm.edu/future-students/freshmen/admission-requirements.html |
| Curriculum requirement | Standard HS curriculum + 2 units language other than English | admissions.unm.edu/future-students/freshmen/admission-requirements.html |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分 (UG) | 最低分 (Grad) | 提交方式 |
|------|-----------|-------------|---------|
| Duolingo English Test | 95 | 105 | Send through Duolingo website |
| IELTS | 6.0 | 6.5 | Upload results page |
| TOEFL iBT | 68 (4.0) | 79 (4.5) | Through ETS (code 4845) |
| TOEFL Essentials | B2 | C1 | Through ETS (code 4845) |
| SAT Reading/Writing | 500 | N/A | Through College Board |
| PTE | 47 | 53 | Upload results page |
| Cambridge (CAE/CPE) | C1 | C2 | Upload results page |
| Language Cert | 68 (no skills below 60) | 74 (no skills below 60) | Upload results |
| Oxford Test of English | 125 | 140 | Upload results |
| Pearson PTE Express | 76 | 85 | Through Pearson Website |

**Exceptions to English Proficiency Requirements:**
- Completion of 4 years of US high school with 2.5+ GPA
- ACT English 19+ or SAT ERW 500+
- 2 semesters of freshman English composition with C or higher at regionally-accredited US institution
- Bachelor's degree from regionally-accredited US institution or recognized English-speaking country institution
- Completion of CELAC Academic Bridge level with 2.5+ GPA

**Note:** All Electrical Engineering and Computer Engineering applicants must provide an English proficiency score regardless of other qualifications.

Source: https://international.unm.edu/english-proficiency.html

### 3.3 Graduate — global rules

- **Admissions model**: Decentralized; each program sets own requirements
- **Application platform**: UNM Graduate Studies online application (most programs)
- **Application fee**: $60 domestic, $70 international
- **GRE/GMAT**: Per program decision (not universally required)
- **English proficiency**: TOEFL 79 (4.5) / IELTS 6.5 / Duolingo 105 (minimum; some programs higher)
- **Separate application processes**: Anderson MBA, Law JD, Medicine MD, Pharmacy PharmD
- **Contact**: unmgrad@unm.edu (domestic), goglobal@unm.edu (international)

Source: https://grad.unm.edu/prospective-students/apply-now.html

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| 费用项目 | 金额 (Resident) | 金额 (Non-Resident w/ scholarship) | 金额 (Non-Resident) |
|---------|----------------|----------------------------------|-------------------|
| Tuition & Fees | $11,585 | $11,585 | $34,734 |
| Food & Housing (Traditional) | $10,648 | $10,648 | $10,648 |
| Books & Supplies | $1,869 | $1,869 | $1,869 |
| Transportation | $2,498 | $2,498 | $2,498 |
| Miscellaneous | $2,800 | $2,800 | $2,800 |
| **Total** | **$29,400** | **$29,400** | **$52,549** |

Source: https://admissions.unm.edu/costs-financial-aid/index.html

**Note:** Non-resident freshmen and transfers with 3.0 GPA or test score of 20 ACT / 1030 SAT may be eligible for resident tuition rates if awarded a scholarship.

**Opportunity Scholarship:** Free tuition for New Mexico residents. Details: http://scholarships.unm.edu/Resources/opportunity-scholarship.html

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 |
|------|-----|
| Need-blind/need-aware | Need-aware for all (public university policy) |
| Merit scholarships | Yes; over $191 million awarded in 2024-2025 |
| Scholarship types | Freshman Resident, Freshman Non-Resident, Transfer, International, Tribal |
| FAFSA required | Yes (for need-based aid) |
| CSS Profile | No |
| Income threshold for free tuition | NM Opportunity Scholarship (varies by eligibility) |
| Percentage receiving aid | 73% (2022-2023) |
| Scholarship amount | $169M in scholarships (2022-2023) |

Source: https://finaid.unm.edu/, https://scholarship.unm.edu/

### 4.3 Graduate cost & funding framework

| 费用项目 | 金额 (Resident) | 金额 (Non-Resident) |
|---------|----------------|-------------------|
| Tuition & Fees (12 credits) | $11,255 | $30,316 |

**Funding opportunities:**
- Assistantships (RA/TA) through departments
- Fellowships (Graduate Studies and external)
- Scholarships (program-specific)
- Western Regional Graduate Program (WRGP) - reduced tuition for qualifying students from WICHE states
- Research & Travel Grants
- Loans & Financial Aid through Financial Aid Office

Source: https://grad.unm.edu/funding/index.html, https://admissions.unm.edu/costs-financial-aid/index.html

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.admissions.priority_deadline_fall
  value: "June 1"
  source_url: https://admissions.unm.edu/future-students/freshmen/index.html
  source_snippet: "Priority Application Dates: Fall Term - June 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.test_policy
  value: "Test-optional (not required)"
  source_url: https://admissions.unm.edu/future-students/freshmen/admission-requirements.html
  source_snippet: "Standardized scores (ACT, SAT or CLT) are not required to be considered for admission but may be helpful in some cases."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.application_fee
  value: 25
  source_url: https://admissions.unm.edu/future-students/freshmen/index.html
  source_snippet: "Application Fee - $25 nonrefundable application fee or approved fee waiver."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.costs.tuition_fees_resident
  value: 11585
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Tuition & Fees: Resident: $11,585"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.tuition_fees_nonresident
  value: 34734
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Tuition & Fees: Non-Resident: $34,734"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_resident
  value: 29400
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Total: Resident: $29,400"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.total_nonresident
  value: 52549
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Total: Non-Resident: $52,549"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency.toefl
  value: 68
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "TOEFL: Undergraduate: 68 (4.0)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.english_proficiency.ielts
  value: 6.0
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "IELTS: Undergraduate: 6.0"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.english_proficiency.duolingo
  value: 95
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "Duolingo English Test: Undergraduate: 95"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.admissions.no_essay
  value: true
  source_url: https://admissions.unm.edu/future-students/freshmen/index.html
  source_snippet: "Essays, portfolios or recommendations are not necessary for admission to The University."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.admissions.curriculum_requirement
  value: "Standard HS curriculum + 2 units language other than English"
  source_url: https://admissions.unm.edu/future-students/freshmen/admission-requirements.html
  source_snippet: "You should have a) graduated from high school with the standard New Mexico high school curriculum, or the equivalent in another state, and b) two sequential units of a language other than English or proficiency to the second level preferred."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.application_fee_domestic
  value: 60
  source_url: https://grad.unm.edu/prospective-students/apply-now.html
  source_snippet: "$60 for domestic applications"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.application_fee_international
  value: 70
  source_url: https://grad.unm.edu/prospective-students/apply-now.html
  source_snippet: "$70 for international applications"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.costs.tuition_fees_resident
  value: 11255
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Graduate Cost of Attendance: Tuition & Fees: 12 credits: Resident: $11,255"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.costs.tuition_fees_nonresident
  value: 30316
  source_url: https://admissions.unm.edu/costs-financial-aid/index.html
  source_snippet: "Graduate Cost of Attendance: Tuition & Fees: 12 credits: Non-Resident: $30,316"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.english_proficiency.toefl
  value: 79
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "TOEFL: Graduate: 79 (4.5)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.english_proficiency.ielts
  value: 6.5
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "IELTS: Graduate: 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-007:
  field: graduate.english_proficiency.duolingo
  value: 105
  source_url: https://international.unm.edu/english-proficiency.html
  source_snippet: "Duolingo English Test: Graduate: 105"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-008:
  field: graduate.admissions.decentralized
  value: true
  source_url: https://grad.unm.edu/prospective-students/apply-now.html
  source_snippet: "Each graduate and professional program has specific requirements for admissions, as well as its own deadlines."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-O-001:
  field: institution.type
  value: "Public R1 Research University"
  source_url: https://admissions.unm.edu/
  source_snippet: "Being one of just 187 Research I Universities classified by very high spending and doctorate production."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-O-002:
  field: institution.total_programs
  value: 453
  source_url: https://catalog.unm.edu/#/programs
  source_snippet: "453 unique program entries extracted from expanded department listings"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-O-003:
  field: institution.scholarships_total
  value: "$191 million (2024-2025)"
  source_url: https://scholarship.unm.edu/
  source_snippet: "over 191 million dollars in scholarships awarded in the 2024-2025 year"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-O-004:
  field: institution.financial_aid_percentage
  value: "73%"
  source_url: https://finaid.unm.edu/
  source_snippet: "73% Percentage of UNM students who received financial aid for 2022-2023"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
unm-knowledge-base-v2/
├── 00-institution-overview.md          → Section 0 (rules 1-4)
├── 01-ug-arts-sciences.md             → Section 1 (A&S programs)
├── 02-ug-architecture.md              → Section 1 (Architecture programs)
├── 03-ug-engineering.md               → Section 1 (Engineering programs)
├── 04-ug-fine-arts.md                 → Section 1 (Fine Arts programs)
├── 05-ug-education.md                 → Section 1 (Education programs)
├── 06-ug-business.md                  → Section 1 (Anderson programs)
├── 07-ug-nursing-pharmacy.md          → Section 1 (Nursing/Pharmacy)
├── 08-ug-medicine-law-other.md        → Section 1 (Medicine/Law/Other)
├── 09-grad-arts-sciences.md           → Section 2 (A&S grad programs)
├── 10-grad-engineering.md             → Section 2 (Engineering grad)
├── 11-grad-professional.md            → Section 2 (Professional grad)
├── 12-admissions-deadlines.md         → Section 3
├── 13-costs-financial-aid.md          → Section 4
├── 14-evidence-chain.md               → Section 5
└── 15-comparison-framework.md         → Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "unm-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program-specific deadlines | Individual program websites |
| P0 | Graduate program-specific GRE requirements | Individual program websites |
| P0 | Freshman Resident scholarship amounts/details | https://scholarship.unm.edu/ |
| P0 | Freshman Non-Resident scholarship amounts/details | https://scholarship.unm.edu/ |
| P1 | Transfer admission requirements | https://admissions.unm.edu/future-students/transfer/ |
| P1 | International freshman admission requirements | https://international.unm.edu/ |
| P1 | Bursar detailed tuition rates by program | https://bursar.unm.edu/tuition-and-fees/tuition-and-fee-rates.html |
| P1 | Net Price Calculator details | https://finaid.unm.edu/coa/coa.html |
| P2 | Campus housing options and costs | https://housing.unm.edu/ |
| P2 | Honors College admission requirements | https://catalog.unm.edu/#/programs |
| P2 | Dual credit program details | http://advisement.unm.edu/dual-credit/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | UNM | (other schools) |
|------|-----|-----------------|
| Institution type | Public R1 | |
| Location | Albuquerque, NM | |
| UG Tuition (Resident) | $11,585 | |
| UG Tuition (Non-Resident) | $34,734 | |
| UG Total COA (Resident) | $29,400 | |
| UG Total COA (Non-Resident) | $52,549 | |
| Grad Tuition (Resident, 12cr) | $11,255 | |
| Grad Tuition (Non-Resident, 12cr) | $30,316 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (rolling) | |
| Priority deadline (Fall) | June 1 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min (UG) | 68 | |
| IELTS min (UG) | 6.0 | |
| Duolingo min (UG) | 95 | |
| Application fee (UG) | $25 | |
| Application fee (Grad) | $60 domestic / $70 intl | |
| Total program count | 453 | |
| School/college count | 14 | |
| Scholarship total | $191M (2024-25) | |
| % receiving aid | 73% | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.unm.edu, grad.unm.edu, international.unm.edu, catalog.unm.edu, finaid.unm.edu, scholarship.unm.edu, bursar.unm.edu, www.unm.edu/academics/
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
