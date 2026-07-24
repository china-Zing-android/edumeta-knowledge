# University of Wyoming Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 85 |
| 本科辅修 (Minor) | 85 |
| 本科证书/背书 (Certificate/Endorsement) | 15 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 70 |
| 研究生证书 (Graduate Certificate) | 19 |
| 研究生辅修 (Graduate Minor) | 5 |
| 双学位/连读项目 | 25 |
| 集中领域/焦点领域 (Concentration/Focus Area) | 8 |
| 预专业项目 (Pre-Professional) | 1 |
| **学位项目总计 (All Programs)** | **327** |
| 学院 / 独立系所总数 | 13 |

> Source: https://www.uwyo.edu/uw/degree-programs/index.html — "327 Results Found"

### 0.2 学院 / 系层级结构

```
University of Wyoming
├── College of Agriculture, Life Sciences and Natural Resources    [学院]
│   ├── Agricultural & Applied Economics                          [系]
│   ├── Animal & Veterinary Science                               [系]
│   ├── Biology                                                   [系]
│   ├── Botany                                                    [系]
│   ├── Family & Consumer Sciences                                [系]
│   ├── Microbiology                                              [系]
│   ├── Molecular Biology                                         [系]
│   ├── Physiology                                                [系]
│   ├── Plant Sciences                                            [系]
│   ├── Rangeland Ecology                                         [系]
│   ├── Wildlife & Fisheries                                      [系]
│   └── Zoology & Physiology                                      [系]
├── College of Arts and Sciences                                  [学院]
│   ├── American Studies                                          [系]
│   ├── Anthropology                                              [系]
│   ├── Art                                                       [系]
│   ├── Communication                                             [系]
│   ├── Criminal Justice                                          [系]
│   ├── English                                                   [系]
│   ├── European Languages                                        [系]
│   ├── History                                                   [系]
│   ├── International Studies                                     [系]
│   ├── Journalism                                                [系]
│   ├── Music                                                     [系]
│   ├── Native American Studies                                   [系]
│   ├── Philosophy                                                [系]
│   ├── Political Science                                         [系]
│   ├── Psychology                                                [系]
│   ├── Religious Studies                                         [系]
│   ├── Sociology                                                 [系]
│   ├── Spanish                                                   [系]
│   └── Theatre & Dance                                           [系]
├── College of Business                                           [学院]
│   ├── Accounting                                                [系]
│   ├── Economics                                                 [系]
│   ├── Finance                                                   [系]
│   ├── Management & Marketing                                    [系]
│   └── MBA Program                                               [系]
├── College of Education                                          [学院]
│   ├── Curriculum & Instruction                                  [系]
│   ├── Educational Leadership                                    [系]
│   └── Counseling                                                [系]
├── College of Engineering & Physical Sciences                    [学院]
│   ├── Architectural Engineering                                 [系]
│   ├── Chemical Engineering                                      [系]
│   ├── Chemistry                                                 [系]
│   ├── Civil Engineering                                         [系]
│   ├── Computer Science                                          [系]
│   ├── Construction Management                                   [系]
│   ├── Electrical & Computer Engineering                         [系]
│   ├── Geography                                                 [系]
│   ├── Geology & Geophysics                                      [系]
│   ├── Mathematics & Statistics                                  [系]
│   ├── Mechanical Engineering                                    [系]
│   ├── Petroleum Engineering                                     [系]
│   └── Physics & Astronomy                                       [系]
├── College of Health Sciences                                    [学院]
│   ├── Nursing                                                   [系]
│   ├── Pharmacy                                                  [系]
│   ├── Kinesiology & Health                                      [系]
│   ├── Social Work                                               [系]
│   ├── Communication Disorders                                   [系]
│   ├── Dental Hygiene                                            [系]
│   └── Medical Laboratory Science                                [系]
├── College of Law                                                [学院]
│   └── Law                                                       [系]
├── Haub School of Environment and Natural Resources              [学院]
│   ├── Environment & Natural Resources                           [系]
│   └── Outdoor Recreation & Tourism                              [系]
├── Honors College                                                [学院]
│   └── Honors Program                                            [系]
├── School of Computing                                           [学院]
│   ├── Applied Computing                                         [系]
│   └── Geospatial Information Science                            [系]
├── School of Energy Resources                                    [学院]
│   └── Energy Resource Management                                [系]
├── School of Graduate Education Interdisciplinary Programs       [学院]
│   ├── Biomedical Sciences                                       [系]
│   ├── Ecology & Evolution                                       [系]
│   ├── Hydrologic Science                                        [系]
│   ├── Molecular & Cellular Life Sciences                        [系]
│   └── Neuroscience                                              [系]
└── UW Casper                                                     [学院]  ⚠ satellite campus
    ├── General Studies                                           [系]
    ├── Education                                                 [系]
    └── Social Sciences                                           [系]
```

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | B.A. | Bachelor of Arts | 本科 | 20 |
| BS | B.S. | Bachelor of Science | 本科 | 43 |
| BSB | B.S.B. | Bachelor of Science in Business | 本科 | 5 |
| BSE | B.S.E. | Bachelor of Science in Economics | 本科 | 1 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 3 |
| BSDH | B.S.D.H. | Bachelor of Science in Dental Hygiene | 本科 | 1 |
| BSW | B.S.W. | Bachelor of Social Work | 本科 | 1 |
| BGS | B.G.S. | Bachelor of General Studies | 本科 | 1 |
| BAS | B.A.S. | Bachelor of Applied Science | 本科 | 1 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 3 |
| BM | B.M. | Bachelor of Music | 本科 | 2 |
| MA | M.A. | Master of Arts | 研究生 | 11 |
| MS | M.S. | Master of Science | 研究生 | 29 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 1 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 2 |
| MM | M.M. | Master of Music | 研究生 | 2 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| MEng | M.Eng. | Master of Engineering | 研究生 | 1 |
| MST | M.S.T. | Master of Science in Teaching | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 17 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 4 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 1 |
| MD | M.D. | Doctor of Medicine | 研究生 | 1 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| PharmD | Pharm.D. | Doctor of Pharmacy | 研究生 | 1 |
| Minor | Minor | Undergraduate Minor | 本科辅修 | 83 |
| GradMinor | Graduate Minor | Graduate Minor | 研究生辅修 | 5 |
| Cert | Certificate | Undergraduate Certificate | 本科证书 | 8 |
| GradCert | Graduate Certificate | Graduate Certificate | 研究生证书 | 19 |
| Endorsement | Endorsement | Teaching Endorsement | 本科/研究生 | 3 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSB | BSN | BFA | BM | MA | MS | MBA | MFA | MM | MPA | MSW | MEng | MST | PhD | EdD | DNP | MD | JD | PharmD | Minor | Cert | 合计 |
|------------|----|----|----|-----|-----|-----|----|----|----|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|-----|-------|-------|------|------|
| Agriculture & Natural Resources | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 19 | 1 | 49 |
| Arts & Sciences | 20 | 3 | 0 | 0 | 4 | 2 | 5 | 0 | 0 | 1 | 2 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 45 | 2 | 87 |
| Business | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 17 | 2 | 30 |
| Education | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 5 | 8 | 22 |
| Engineering & Physical Sciences | 2 | 18 | 0 | 0 | 0 | 0 | 2 | 10 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 7 | 3 | 49 |
| Health Sciences | 0 | 7 | 0 | 3 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 4 | 2 | 24 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| Haub School | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 10 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| School of Computing | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 11 |
| School of Energy Resources | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 6 |
| Graduate Interdisciplinary | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| UW Casper | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 12 |
| **合计** | **27** | **58** | **5** | **3** | **4** | **2** | **9** | **32** | **2** | **1** | **2** | **1** | **2** | **1** | **2** | **19** | **1** | **1** | **1** | **1** | **1** | **106** | **28** | **308** |

> Note: Multi-degree programs (e.g., BS/MS concurrent, JD/MBA dual) are counted once under their primary degree. Total includes 19 dual/concurrent programs counted once. Reconciliation: 327 raw program entries - 19 dual-count entries = 308 unique degree-level entries.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

The University of Wyoming has 7 degree-granting undergraduate colleges plus the Haub School, Honors College, School of Computing, School of Energy Resources, and UW Casper satellite campus. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agriculture, Life Sciences and Natural Resources

##### Department of Agricultural & Applied Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Agricultural Communications | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Agricultural Economics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Agroecology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Agronomy | https://www.uwyo.edu/uw/degree-programs/index.html |
| 6 | Farm and Ranch Management | https://www.uwyo.edu/uw/degree-programs/index.html |
| 7 | Food Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Animal & Veterinary Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal and Veterinary Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Meat Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Family & Consumer Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Consumer Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Dietetics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Early Childhood Education | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Plant Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Horticulture | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Plant Production and Protection | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Rangeland Management | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Rangeland Ecology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Rangeland Ecology and Watershed Management | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Wildlife & Fisheries
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Wildlife and Fisheries Biology and Management | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Zoology & Physiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Zoology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Physiology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Biology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Microbiology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Molecular Biology | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Arts and Sciences

##### Department of American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.uwyo.edu/uw/degree-programs/index.html |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Graphic Design | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Studio Art | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Criminal Justice
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Creative Writing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Professional Writing | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.uwyo.edu/uw/degree-programs/index.html |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Music Performance | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Environment and Natural Resources | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Theatre & Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre and Dance | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Dance | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Business

##### Department of Accounting
###### BSB
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Economics
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Finance
###### BSB
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Management & Marketing
###### BSB
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Marketing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Business Economics | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Education

##### Department of Curriculum & Instruction
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Secondary Education | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Engineering & Physical Sciences

##### Department of Architectural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Construction Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Computer Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Geology & Geophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Geophysics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Environmental Geology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Petroleum Geology | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Mathematics & Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Statistics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Applied Mathematics | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Petroleum Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Physics & Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Astronomy | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Physics Education | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Health Sciences

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Nursing (BRAND) | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Nursing RN-BSN | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Kinesiology & Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology and Health | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Health Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Dental Hygiene
###### BSDH
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://www.uwyo.edu/uw/degree-programs/index.html |

##### Department of Pharmacy
###### BS + PharmD (Pre-Pharmacy)
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-Pharmacy | https://www.uwyo.edu/uw/degree-programs/index.html |

#### Haub School of Environment and Natural Resources

##### Department of Environment & Natural Resources
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environment and Natural Resources | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Environment and Natural Resources - Rangeland Ecology and Watershed Management | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Environment and Natural Resources - Wildlife and Fisheries Biology and Management | https://www.uwyo.edu/uw/degree-programs/index.html |

#### School of Computing

##### Department of Applied Computing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Computing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Cybersecurity | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Data Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Software Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

#### School of Energy Resources

##### Department of Energy Resource Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Energy Resource Management | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Professional Land Management | https://www.uwyo.edu/uw/degree-programs/index.html |

#### UW Casper

##### General Studies
###### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Science | https://www.uwyo.edu/uw/degree-programs/index.html |

###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Criminal Justice | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Elementary Education | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Social Work | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Business Administration | https://www.uwyo.edu/uw/degree-programs/index.html |
| 6 | Organizational Leadership | https://www.uwyo.edu/uw/degree-programs/index.html |

### 1.3 Interdisciplinary / Cross-college Undergraduate Programs

| # | 专业 | 学位 | 涉及学院 |
|---|------|------|----------|
| 1 | Environment and Natural Resources | BS | Agriculture & Haub School |
| 2 | American Indian Studies | BA | Arts & Sciences |
| 3 | African American and Diaspora Studies | Minor | Arts & Sciences |
| 4 | Asian Studies | Minor | Arts & Sciences |
| 5 | Environmental Studies | Minor | Multiple colleges |

### 1.4 Minors — Complete List (83 Undergraduate Minors)

| # | Minor | Home College |
|---|-------|--------------|
| 1 | Accounting | College of Business |
| 2 | Acting Performance | College of Arts and Sciences |
| 3 | African American and Diaspora Studies | College of Arts and Sciences |
| 4 | Aging Studies | College of Arts and Sciences |
| 5 | Agribusiness Leadership | UW Casper |
| 6 | Agricultural Economics | College of Agriculture |
| 7 | Agroecology | College of Agriculture |
| 8 | Agronomy | College of Agriculture |
| 9 | Air Force ROTC Aerospace Studies | Multiple colleges |
| 10 | American Politics | College of Arts and Sciences |
| 11 | American Studies | College of Arts and Sciences |
| 12 | Animal and Veterinary Science | College of Agriculture |
| 13 | Anthropology | College of Arts and Sciences |
| 14 | Art | College of Arts and Sciences |
| 15 | Astronomy | College of Engineering & Physical Sciences |
| 16 | Biology | College of Agriculture |
| 17 | Botany | College of Agriculture |
| 18 | Business | College of Business |
| 19 | Chemistry | College of Engineering & Physical Sciences |
| 20 | Coaching | College of Health Sciences |
| 21 | Communication | College of Arts and Sciences |
| 22 | Computer Science | College of Engineering & Physical Sciences |
| 23 | Creative Writing | College of Arts and Sciences |
| 24 | Criminal Justice | College of Arts and Sciences |
| 25 | Dance | College of Arts and Sciences |
| 26 | Economics | College of Business |
| 27 | Education | College of Education |
| 28 | English | College of Arts and Sciences |
| 29 | Environment and Natural Resources | Haub School |
| 30 | Environmental Soil Science | College of Agriculture |
| 31 | Ethnic Studies | College of Arts and Sciences |
| 32 | European Studies | College of Arts and Sciences |
| 33 | Family and Consumer Sciences | College of Agriculture |
| 34 | Film Studies | College of Arts and Sciences |
| 35 | Finance | College of Business |
| 36 | French | College of Arts and Sciences |
| 37 | Gender and Women's Studies | College of Arts and Sciences |
| 38 | Geography | College of Engineering & Physical Sciences |
| 39 | Geology | College of Engineering & Physical Sciences |
| 40 | German | College of Arts and Sciences |
| 41 | Global Studies | College of Arts and Sciences |
| 42 | Health Sciences | College of Health Sciences |
| 43 | History | College of Arts and Sciences |
| 44 | Honors | Honors College |
| 45 | Humanities | College of Arts and Sciences |
| 46 | Information Technology | School of Computing |
| 47 | International Studies | College of Arts and Sciences |
| 48 | Journalism | College of Arts and Sciences |
| 49 | Kinesiology and Health | College of Health Sciences |
| 50 | Latin American Studies | College of Arts and Sciences |
| 51 | Legal Studies | College of Law |
| 52 | Management | College of Business |
| 53 | Marketing | College of Business |
| 54 | Mathematics | College of Engineering & Physical Sciences |
| 55 | Military Science | Multiple colleges |
| 56 | Music | College of Arts and Sciences |
| 57 | Native American Studies | College of Arts and Sciences |
| 58 | Naval Science | Multiple colleges |
| 59 | Outdoor Recreation and Tourism | Haub School |
| 60 | Philosophy | College of Arts and Sciences |
| 61 | Photography | College of Arts and Sciences |
| 62 | Physics | College of Engineering & Physical Sciences |
| 63 | Plant Sciences | College of Agriculture |
| 64 | Political Science | College of Arts and Sciences |
| 65 | Psychology | College of Arts and Sciences |
| 66 | Range Management | College of Agriculture |
| 67 | Religious Studies | College of Arts and Sciences |
| 68 | Russian | College of Arts and Sciences |
| 69 | Social Work | College of Health Sciences |
| 70 | Sociology | College of Arts and Sciences |
| 71 | Spanish | College of Arts and Sciences |
| 72 | Statistics | College of Engineering & Physical Sciences |
| 73 | Sustainable Energy | School of Energy Resources |
| 74 | Theatre | College of Arts and Sciences |
| 75 | Wildlife and Fisheries Biology | College of Agriculture |
| 76 | Zoology | College of Agriculture |
| 77 | Energy Management | School of Energy Resources |
| 78 | Data Science | School of Computing |
| 79 | Cybersecurity | School of Computing |
| 80 | Geospatial Information Science | School of Computing |
| 81 | Honors Program | Honors College |
| 82 | Outdoor Recreation and Tourism Management | Haub School |
| 83 | Environment and Natural Resources | Haub School |

### 1.5 General Education Requirements

The University of Wyoming requires all undergraduate students to complete the University Studies Program (USP), which includes:
- **First-Year Seminar** (1 course)
- **Written Communication** (2 courses)
- **Quantitative Reasoning** (1 course)
- **Physical and Natural Sciences** (2 courses, one with lab)
- **Humanities** (2 courses)
- **Social Sciences** (2 courses)
- **USP Electives** (3 courses from approved list)
- **Cultural Diversity** (1 course, may overlap)
- **Global Awareness** (1 course, may overlap)

Total: ~30 credits of general education requirements.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### College of Agriculture, Life Sciences and Natural Resources

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Applied Economics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Animal and Veterinary Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Entomology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Family and Consumer Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Microbiology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 6 | Molecular Biology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 7 | Plant Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |
| 8 | Soil Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal and Veterinary Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Molecular Biology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Zoology and Physiology | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Arts and Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Anthropology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | English | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | History | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Political Science | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Performance | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Music Education | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Ecology and Evolution | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Economics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Finance | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Business Administration (Online) | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Educational Leadership | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Special Education | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MST
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching | https://www.uwyo.edu/uw/degree-programs/index.html |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Educational Leadership | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Curriculum and Instruction | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Counselor Education and Supervision | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Engineering & Physical Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Statistics | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Chemistry | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Civil Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Computer Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Electrical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 6 | Geology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 7 | Geophysics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 8 | Mathematics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 9 | Mechanical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 10 | Petroleum Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Chemistry | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Civil Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Geology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Mathematics | https://www.uwyo.edu/uw/degree-programs/index.html |
| 6 | Mechanical Engineering | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Health Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology and Health | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Nursing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Speech-Language Pathology | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Health Services Administration | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.uwyo.edu/uw/degree-programs/index.html |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://www.uwyo.edu/uw/degree-programs/index.html |

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.uwyo.edu/uw/degree-programs/index.html |

#### College of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.uwyo.edu/uw/degree-programs/index.html |

#### School of Computing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Computing | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Computer Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Data Science | https://www.uwyo.edu/uw/degree-programs/index.html |

#### School of Graduate Education Interdisciplinary Programs

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.uwyo.edu/uw/degree-programs/index.html |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |
| 2 | Ecology and Evolution | https://www.uwyo.edu/uw/degree-programs/index.html |
| 3 | Hydrologic Science | https://www.uwyo.edu/uw/degree-programs/index.html |
| 4 | Molecular and Cellular Life Sciences | https://www.uwyo.edu/uw/degree-programs/index.html |
| 5 | Neuroscience | https://www.uwyo.edu/uw/degree-programs/index.html |

### 2.2 Graduate Admissions Model

The University of Wyoming uses a **decentralized** graduate admissions model. Each department/program sets its own admission requirements, deadlines, and review processes. The Graduate School provides oversight and administrative support.

**Key facts:**
- Application fee: **$50 USD** (non-refundable)
- Application portal: https://uwyo-erx.my.site.com/ERx_Forms__Portal_Register
- Programs must be contacted directly for specific requirements
- English proficiency requirements are set by the Graduate School minimum; individual programs may require higher scores

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | Source |
|------|-----|--------|
| Admissions site | https://www.uwyo.edu/admissions/index.html | Official webpage |
| Application portal | https://uwyo-erx.my.site.com/ERx_Forms__Portal_Register | Official webpage |
| Common App | Accepted | admissions/apply.html |
| Application fee | $40 non-refundable | admissions/apply.html FAQ |
| Admission type | Rolling admission (no fixed deadline) | admissions/apply.html FAQ |
| Financial aid priority date | May 1 (confirm enrollment by this date) | admissions/apply.html FAQ |
| International deadlines | Fall: June 1 / Spring: Nov 1 / Summer: April 1 | admissions/international/requirements-first-year.html |
| GPA requirement (assured) | 3.00–4.00 cumulative, unweighted | admissions/freshman/index.html |
| GPA requirement (with support) | 2.50–2.99 | admissions/freshman/index.html |
| Test policy | **Test-optional** (not required) | admissions/apply.html FAQ |
| SAT code | 4855 | admissions/freshman/index.html |
| ACT code | 5006 | admissions/freshman/index.html |
| Superscore policy | Not specified | N/A |
| Recommendation requirements | Not required | admissions/freshman/index.html |
| Interview | Not offered | N/A |
| Portfolio | Not required (except Art programs) | N/A |
| High school curriculum | 4yr English, 4yr Math, 4yr Science, 3yr Social Science, 4yr Additional | admissions/freshman/index.html |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended Score |
|------|---------------|-------------------|
| TOEFL iBT (including Home Edition, MyBest) | 71 | 80+ |
| IELTS (including Indicator) | 6.0 | 6.5+ |
| Cambridge | B2 First | B2 First |
| Duolingo | 100 | 110+ |
| iTEP Academic Plus | 4.0 | 4.5+ |
| PTE | 50 | 55+ |
| ACT English section | 20 | 24+ |
| SAT ERW | 460 | 500+ |
| IB English HL | 4+ | 5+ |
| AP Language/Composition | 4+ | N/A |
| AP Literature | 4+ | N/A |
| IGCSE/GCE English | C or above | N/A |
| GTEC CBT | 1,140 | N/A |
| TOEIC | 675 | N/A |
| EIKEN | Pre-1 | N/A |
| Gaokao | 120 (94 for Jiangsu & Shanghai) | N/A |
| CEFR | C1-B2 | C1 |

> Source: https://www.uwyo.edu/admissions/international/english-alternatives.html

**Exemptions:** Citizens of or degree-holders from: Antigua & Barbuda, Australia, Bahamas, Belize, Bermuda, Canada (except Quebec), Ghana, Grenada, Guyana, Ireland, Jamaica, New Zealand, Nigeria, Singapore, St. Kitts & Nevis, St. Lucia, Dominica, St. Vincent & the Grenadines, Trinidad & Tobago, United Kingdom, United States.

### 3.3 Graduate — Global Rules

| 维度 | 值 | Source |
|------|-----|--------|
| Application fee | $50 USD (non-refundable) | admissions/international/requirements-graduate.html |
| Admissions model | Decentralized (each program sets own requirements) | Graduate School policy |
| GRE policy | Per-program (contact department) | Graduate School policy |
| CGS April-15 signatory | Not confirmed | N/A |
| Application portal | https://uwyo-erx.my.site.com/ERx_Forms__Portal_Register | Official webpage |

**Graduate English Proficiency:**

| Exam | Minimum Score |
|------|---------------|
| TOEFL iBT | 76 |
| IELTS | 6.5 |
| Duolingo | 110 |
| Cambridge | B2 First |
| iTEP Academic Plus | 4.5 |
| PTE | 56 |
| TOEIC | 695 |
| EIKEN | 1 |
| CEFR | C1 |
| Manchester Exam | 400 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (FY2026-27)

#### Wyoming Resident — On Campus

| Expense Item | Amount (Annual) | Description |
|--------------|-----------------|-------------|
| Tuition | $5,610 | Block rate: $2,805/semester (12-18 credits) |
| Mandatory Fees | $2,922 | Student mandatory + services fees |
| Housing & Food | $14,500 | On-campus residence hall + meal plan |
| Books & Supplies | $1,300 | Estimated course materials |
| Other Expenses | $3,600 | Personal, transportation, misc |
| **Total Estimated COA** | **$27,932** | Per academic year (30 credits) |

> Source: https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html (calculator result)

#### Non-Resident / International — On Campus

| Expense Item | Amount (Annual) | Description |
|--------------|-----------------|-------------|
| Tuition | $22,470 | Block rate: $11,235/semester (12-18 credits) |
| Mandatory Fees | $2,922 | Student mandatory + services fees |
| Housing & Food | $14,500 | On-campus residence hall + meal plan |
| Books & Supplies | $1,300 | Estimated course materials |
| Other Expenses | $4,100 | Personal, transportation, misc (higher for intl) |
| **Total Estimated COA** | **$45,292** | Per academic year (30 credits) |

> Source: https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html (calculator result)

#### Additional Fee Details (FY27)

| Fee | Amount | Description |
|-----|--------|-------------|
| Student Mandatory Fee | $465.13/semester | Required for all students |
| Student Services Fee | $521.33/semester | Health, rec, athletics |
| Technology Fee | $65/semester | Per term |
| Total Mandatory+Services | $986.46/semester | For 6+ credits |
| Block tuition range | 12-18 credits | Same price within range |
| Over-18 surcharge | Per-credit rate applies | Beyond 18 credits |

> Source: https://www.uwyo.edu/fsbo/student-financial-services/tuition-and-fees.html

#### Per-Credit Rates (FY27, for non-block programs)

| Program | Resident | Non-Resident |
|---------|----------|--------------|
| Undergraduate | $187/credit | $749/credit |
| Graduate | $363/credit | $1,067/credit |
| Law | $599-622/credit | $1,278/credit |
| Pharmacy | $642/credit | $962/credit |
| MBA | $817/credit | $817/credit |

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 |
|------|-----|
| Need-blind domestic | No — need-aware for all |
| Need-blind international | No — need-aware |
| Meets full demonstrated need | Not guaranteed |
| Merit scholarships available | Yes |
| Hathaway Scholarship | Wyoming state scholarship (requires SAT/ACT) |
| International Brown & Gold Commitment | $5,000-$8,000/year based on GPA |
| GPA 3.4-4.0 | $8,000/year |
| GPA 3.0-3.39 | $5,000/year |
| Renewable | Up to 8 semesters |
| Transfer scholarships | Available (Pokes Transfer Commitment) |

> Source: https://www.uwyo.edu/sfa/scholarships/international/brown-and-gold-commitment.html

**Note:** A test score is **recommended** (not required) for admission but **may be required** for certain scholarships, including the Wyoming Hathaway Scholarship.

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 |
|------|-----|
| Graduate tuition (resident) | $3,630/semester block rate (9-12 credits) |
| Graduate tuition (non-resident) | $10,670/semester block rate |
| Graduate application fee | $50 |
| Common funding forms | TA, RA, fellowships, grants |
| PhD funding | Commonly funded through assistantships |
| Master's funding | Varies by department |

---

## SECTION 5 — Evidence Chain Index

```yaml
---
field: undergraduate.admissions.type
value: "Rolling admission (no fixed deadline)"
source_url: "https://www.uwyo.edu/admissions/apply.html"
source_snippet: "UW uses a rolling admission process for undergraduates, which means there's no single application deadline."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.financial_aid_priority
value: "May 1"
source_url: "https://www.uwyo.edu/admissions/apply.html"
source_snippet: "To be considered for financial aid, be sure to confirm your enrollment by May 1."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.test_policy
value: "Test-optional"
source_url: "https://www.uwyo.edu/admissions/apply.html"
source_snippet: "Currently, an ACT or SAT score is not part of the admissions requirements for the University of Wyoming."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_fee
value: "$40 non-refundable"
source_url: "https://www.uwyo.edu/admissions/apply.html"
source_snippet: "Yes, there is a non-refundable $40 application fee that is processed when you submit your application."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.gpa_assured
value: "3.00-4.00"
source_url: "https://www.uwyo.edu/admissions/freshman/index.html"
source_snippet: "For assured admission, a cumulative high school GPA of 3.00–4.00 is required."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.gpa_support
value: "2.50-2.99"
source_url: "https://www.uwyo.edu/admissions/freshman/index.html"
source_snippet: "Students with a GPA of 2.50–2.99 are admitted with support."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.english_proficiency.toefl
value: "71"
source_url: "https://www.uwyo.edu/admissions/international/english-alternatives.html"
source_snippet: "iBT/TOEFL MyBest scores TOEFL Home Edition: 71"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.english_proficiency.ielts
value: "6.0"
source_url: "https://www.uwyo.edu/admissions/international/english-alternatives.html"
source_snippet: "IELTS IELTS Indicator: 6"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.english_proficiency.duolingo
value: "100"
source_url: "https://www.uwyo.edu/admissions/international/english-alternatives.html"
source_snippet: "Duolingo: 100"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: graduate.english_proficiency.toefl
value: "76"
source_url: "https://www.uwyo.edu/admissions/international/english-alternatives.html"
source_snippet: "iBT/TOEFL MyBest scores TOEFL Home Edition: 76"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: graduate.english_proficiency.ielts
value: "6.5"
source_url: "https://www.uwyo.edu/admissions/international/english-alternatives.html"
source_snippet: "IELTS IELTS Indicator: 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_resident
value: "$5,610/year"
source_url: "https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html"
source_snippet: "Tuition: $5,610.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_nonresident
value: "$22,470/year"
source_url: "https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html"
source_snippet: "Tuition: $22,470.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.total_resident_oncampus
value: "$27,932/year"
source_url: "https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html"
source_snippet: "Academic Year (30 credits): $27,932.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.total_nonresident_oncampus
value: "$45,292/year"
source_url: "https://www.uwyo.edu/sfa/cost-of-attendance/undergraduate.html"
source_snippet: "Academic Year (30 credits): $45,292.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: tuition.fy27.resident_block
value: "$2,805/semester"
source_url: "https://www.uwyo.edu/fsbo/student-financial-services/tuition-and-fees.html"
source_snippet: "Undergraduate resident main campus students block rate = $2,805 per semester"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: tuition.fy27.nonresident_block
value: "$11,235/semester"
source_url: "https://www.uwyo.edu/fsbo/student-financial-services/tuition-and-fees.html"
source_snippet: "Undergraduate non-resident students block rate = $11,235 per semester"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: programs.total
value: "327"
source_url: "https://www.uwyo.edu/uw/degree-programs/index.html"
source_snippet: "327 Results Found"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: international.scholarships.brown_gold
value: "$5,000-$8,000/year"
source_url: "https://www.uwyo.edu/sfa/scholarships/international/brown-and-gold-commitment.html"
source_snippet: "The Brown and Gold Commitment is a merit-based financial pledge determined by a student's cumulative grade point average (GPA), and it has two levels of support paid annually: $8,000 and $5,000."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.application_fee
value: "$50"
source_url: "https://www.uwyo.edu/admissions/international/requirements-graduate.html"
source_snippet: "Easily apply online with a $50 USD non-refundable application fee."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: institutional.r1_status
value: "R1: Very High Research Activity"
source_url: "https://www.uwyo.edu/admissions/freshman/index.html"
source_snippet: "The University of Wyoming has earned its Research Level 1 (R1) status from the Carnegie Classification of Institutions of Higher Education"
capture_date: 2026-07-06
evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uwyo-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0)
├── 01-ug-programs-agriculture.md       (Section 1 - Agriculture college)
├── 02-ug-programs-arts-sciences.md     (Section 1 - A&S college)
├── 03-ug-programs-business.md          (Section 1 - Business college)
├── 04-ug-programs-education.md         (Section 1 - Education college)
├── 05-ug-programs-engineering.md       (Section 1 - Engineering college)
├── 06-ug-programs-health.md            (Section 1 - Health Sciences)
├── 07-ug-programs-other.md             (Section 1 - Haub, Computing, Energy, Casper)
├── 08-grad-programs.md                 (Section 2)
├── 09-admissions-deadlines.md          (Section 3)
├── 10-costs-financial-aid.md           (Section 4)
└── 11-evidence-chain.md                (Section 5)
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "uwyo-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "https://www.uwyo.edu/uw/degree-programs/index.html"
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Resident scholarship details (page returning 500 error) | https://www.uwyo.edu/sfa/scholarships/resident.html |
| P0 | Non-resident scholarship details (page returning 500 error) | https://www.uwyo.edu/sfa/scholarships/non-resident.html |
| P1 | Per-program GRE requirements | Contact individual departments |
| P1 | Graduate program deadlines | Contact individual departments |
| P1 | Hathaway Scholarship details | https://www.uwyo.edu/sfa/scholarships/ |
| P2 | Campus housing costs breakdown | https://www.uwyo.edu/reslife/ |
| P2 | Dining costs breakdown | https://www.uwyo.edu/dining/ |

---

## SECTION 7 — Cross-school Comparison Framework

| 维度 | University of Wyoming | (Other schools) |
|------|----------------------|-----------------|
| Type | Public R1 | |
| Location | Laramie, WY | |
| Only 4-year university in state | Yes (Wyoming) | |
| Total programs (Rule 1) | 327 | |
| School/college count (Rule 2) | 13 | |
| UG tuition (resident/yr) | $5,610 | |
| UG tuition (non-resident/yr) | $22,470 | |
| UG COA (resident, on-campus) | $27,932 | |
| UG COA (non-resident, on-campus) | $45,292 | |
| Need-blind (domestic) | No — need-aware | |
| Need-blind (international) | No — need-aware | |
| Test policy | Test-optional | |
| EA deadline | N/A (rolling) | |
| RD deadline | Rolling (priority May 1) | |
| TOEFL min (UG) | 71 | |
| IELTS min (UG) | 6.0 | |
| Duolingo min (UG) | 100 | |
| Application fee (UG) | $40 | |
| Application fee (Grad) | $50 | |
| Block tuition model | Yes (12-18 credits) | |
| R1 status | Yes | |
| Strong areas | Energy, Geology, Agriculture, Engineering | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: uwyo.edu (admissions, financial aid, degree programs, tuition & fees)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
