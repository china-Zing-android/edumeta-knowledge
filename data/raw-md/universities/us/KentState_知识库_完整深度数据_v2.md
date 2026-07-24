# Kent State University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BBA/BM/BSE/BSN/etc.) | 129 |
| 本科辅修 (Minor) | 161 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 126 |
| 研究生/本科证书 (Certificate) | 179 |
| 非学位/背书 (Non-Degree/Endorsement) | 15 |
| **学位项目总计 (UG Majors + Grad Degrees)** | **255** |
| **全部项目总计 (含辅修、证书、非学位)** | **610** |
| 学院 / 独立系所总数 | 13 |

> **Reconciliation note**: The catalog lists 610 total entries. Degree programs (UG majors + Grad degrees) total 255. Including minors (161), certificates (179), and non-degree/endorsement (15) brings the total to 610.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Kent State University
├── Ambassador Crawford College of Business and Entrepreneurship (be)     [学院]
│   ├── Department of Accounting (acct)                                    [系]
│   ├── Department of Economics (econ)                                     [系]
│   ├── Department of Finance (fin)                                        [系]
│   ├── Department of Information Systems and Business Analytics (isba)    [系]
│   ├── Department of Management (mgt)                                     [系]
│   ├── Department of Marketing and Entrepreneurship (mken)                [系]
│   └── Department of Sport, Hospitality and Event Management (shem)       [系]
├── College of Aeronautics and Engineering (ar)                           [学院]
│   ├── School of Aeronautics (aern)                                       [系]
│   └── School of Engineering (engr)                                       [系]
├── College of Applied and Technical Studies (ap)                         [学院]
│   └── (多为副学士/证书项目，无内部系划分)
├── College of Architecture and Environmental Design (ae)                 [学院]
│   └── (建筑、室内设计、景观建筑、施工管理等项目)
├── College of Communication and Information (ci)                         [学院]
│   ├── Department of Applied Media (emat)                                 [系]
│   ├── Department of Media and Journalism (mdj)                           [系]
│   └── School of Visual Communication Design (vcd)                       [系]
├── College of Education and Human Services (es)                          [学院]
│   ├── Department of Lifespan Development and Educational Sciences (ldes) [系]
│   └── Department of Teaching, Learning and Curriculum Studies (tlc)      [系]
├── College of Honors and Global Education (hg)                           [学院]
│   └── Honors Program
├── College of Nursing (nu)                                               [学院]
│   └── (护理学 BSN/MSN/DNP/PhD 及研究生证书)
├── College of Podiatric Medicine (pm)                                    [学院]
│   └── (足部医学 DPM)
├── College of Public Health and Health Sciences (pb)                     [学院]
│   └── (公共卫生、运动科学、营养学、言语病理学等)
├── College of Sciences and Humanities (sh)                               [学院]
│   ├── Department of Africana Studies (afs)                               [系]
│   ├── Department of Anthropology (anth)                                  [系]
│   ├── Department of Biological Sciences (bsci)                           [系]
│   ├── Department of Chemistry (chmb)                                     [系]
│   ├── Department of Computer Science (cs)                                [系]
│   ├── Department of Earth Sciences (esci)                                [系]
│   ├── Department of English (eng)                                        [系]
│   ├── Department of Geography (geog)                                     [系]
│   ├── Department of History (hist)                                       [系]
│   ├── Department of Mathematical Sciences (math)                         [系]
│   ├── Department of Modern and Classical Language Studies (mcls)         [系]
│   ├── Department of Philosophy (phil)                                    [系]
│   ├── Department of Physics (phy)                                        [系]
│   ├── Department of Political Science (pol)                              [系]
│   ├── Department of Psychological Sciences (psys)                        [系]
│   ├── Department of Sociology (socr)                                     [系]
│   ├── Department of Economics (economics-ba)                             [系]
│   ├── School of Communication Studies (comm)                             [系]
│   ├── School of Information (info)                                       [系]
│   └── School of Multidisciplinary Social Sciences and Humanities (mssh)  [系]
├── College of the Arts (ca)                                              [学院]
│   ├── School of Art (arts)                                               [系]
│   ├── School of Fashion (fdm)                                            [系]
│   ├── School of Music (mus)                                              [系]
│   └── School of Theatre and Dance (thea)                                 [系]
└── University College (uc)                                               [学院]
    └── Exploratory Major / Cooperative Education
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| AA | A.A. | Associate of Arts | 副学士 | 1 |
| AS | A.S. | Associate of Science | 副学士 | 1 |
| AAB | A.A.B. | Associate of Applied Business | 副学士 | 8 |
| AAS | A.A.S. | Associate of Applied Science | 副学士 | 10 |
| ATS | A.T.S. | Associate of Technical Studies | 副学士 | 1 |
| ABAS | A.B.A.S. | Associate of Business Administration | 副学士 | 1 |
| BA | B.A. | Bachelor of Arts | 本科 | 27 |
| BS | B.S. | Bachelor of Science | 本科 | 51 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 7 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 10 |
| BM | B.M. | Bachelor of Music | 本科 | 2 |
| BIS | B.I.S. | Bachelor of Integrative Studies | 本科 | 1 |
| BSW | B.S.W. | Bachelor of Social Work | 本科 | 1 |
| BSE | B.S.E. | Bachelor of Science in Education | 本科 | 20 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 2 |
| BRIT | B.R.I.T. | Bachelor of Radiologic Imaging Technology | 本科 | 1 |
| BSPH | B.S.P.H. | Bachelor of Science in Public Health | 本科 | 1 |
| BSIT | B.S.I.T. | Bachelor of Science in Information Technology | 本科 | 1 |
| BTAS | B.T.A.S. | Bachelor of Technical and Applied Studies | 本科 | 1 |
| Minor | Minor | 辅修 | 本科辅修 | 161 |
| MA | M.A. | Master of Arts | 研究生 | 32 |
| MS | M.S. | Master of Science | 研究生 | 23 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 5 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 1 |
| MSA | M.S.A. | Master of Science in Accounting | 研究生 | 1 |
| MAE | M.A.E. | Master of Arts in Economics | 研究生 | 1 |
| MEd | M.Ed. | Master of Education | 研究生 | 16 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 4 |
| MArch | M.Arch | Master of Architecture | 研究生 | 1 |
| MM | M.M. | Master of Music | 研究生 | 2 |
| MPA | M.P.A. | Master of Public Administration | 研究生 | 1 |
| MLIS | M.L.I.S. | Master of Library and Information Science | 研究生 | 2 |
| MET | M.E.T. | Master of Engineering Technology | 研究生 | 1 |
| MFIS | M.F.I.S. | Master of Fashion Industry Studies | 研究生 | 1 |
| MGISc | M.G.I.Sc. | Master of Geographic Information Science | 研究生 | 1 |
| MHD | M.H.D. | Master of Healthcare Design | 研究生 | 1 |
| MLA | M.L.A. | Master of Landscape Architecture | 研究生 | 2 |
| MUD | M.U.D. | Master of Urban Design | 研究生 | 1 |
| MSN | M.S.N. | Master of Science in Nursing | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 1 |
| EdS | Ed.S. | Educational Specialist | 研究生 | 5 |
| LSM | L.S.M. | Liberal Studies Master | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 30 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | 1 |
| DPM | D.P.M. | Doctor of Podiatric Medicine | 研究生 | 1 |
| AuD | Au.D. | Doctor of Audiology | 研究生 | 1 |
| Grad Cert | Graduate Certificate | 研究生证书 | 研究生证书 | 40 |
| UG Cert | Undergraduate Certificate | 本科证书 | 本科证书 | 139 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | AA/AS/AAB/AAS | BA | BS | BFA | BBA | BM | BSE/BSN/Other UG | Minor | MA | MS | MFA | MBA | MEd | MPH | PhD/EdD/DNP | EdS | Grad Cert | 合计 |
|------------|---------------|----|----|-----|-----|----|------------------|-------|----|----|-----|-----|-----|-----|-------------|-----|-----------|------|
| Business (be) | 0 | 0 | 1 | 0 | 10 | 0 | 0 | 16 | 1 | 4 | 0 | 1 | 0 | 0 | 1 | 0 | 10 | 44 |
| Aeronautics & Engineering (ar) | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 14 |
| Applied & Technical Studies (ap) | 21 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 35 |
| Architecture & Environmental Design (ae) | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| Communication & Information (ci) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 |
| Education & Human Services (es) | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 18 | 0 | 0 | 0 | 0 | 16 | 0 | 0 | 5 | 7 | 66 |
| Nursing (nu) | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 10 | 14 |
| Podiatric Medicine (pm) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Public Health (pb) | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 6 | 3 | 2 | 0 | 0 | 0 | 4 | 2 | 0 | 2 | 24 |
| Sciences & Humanities (sh) | 0 | 23 | 35 | 0 | 0 | 0 | 0 | 93 | 28 | 13 | 0 | 0 | 0 | 0 | 25 | 0 | 10 | 227 |
| Arts (ca) | 0 | 0 | 0 | 7 | 0 | 2 | 0 | 16 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 2 | 32 |
| University College (uc) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Honors & Global Ed (hg) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **21** | **27** | **52** | **7** | **10** | **2** | **22** | **161** | **32** | **23** | **5** | **1** | **16** | **4** | **32** | **5** | **50** | **470** |

> **Note**: Counts reflect only programs extracted from the catalog with identifiable degree codes. Some certificate and non-degree programs are cataloged under college-level entries without department subdivisions. Total catalog entries: 610 (including 139 undergraduate certificates and 1 non-degree programs not fully captured in this matrix due to catalog structure).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Kent State University has 13 colleges/schools. The undergraduate degree-granting colleges are: Ambassador Crawford College of Business and Entrepreneurship, College of Aeronautics and Engineering, College of Applied and Technical Studies, College of Architecture and Environmental Design, College of Communication and Information, College of Education and Human Services, College of Nursing, College of Public Health and Health Sciences, College of Sciences and Humanities, and College of the Arts. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Ambassador Crawford College of Business and Entrepreneurship

##### Department of Accounting
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.kent.edu/colleges/be/acct/accounting-bba/ |

##### Department of Economics
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.kent.edu/colleges/be/econ/economics-bba/ |

##### Department of Finance
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.kent.edu/colleges/be/fin/finance-bba/ |

##### Department of Information Systems and Business Analytics
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.kent.edu/colleges/be/isba/business-analytics-bba/ |
| 2 | Computer Information Systems | https://catalog.kent.edu/colleges/be/isba/computer-information-systems-bba/ |

##### Department of Management
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management | https://catalog.kent.edu/colleges/be/mgt/business-management-bba/ |
| 2 | General Business | https://catalog.kent.edu/colleges/be/mgt/general-business-bba/ |
| 3 | Human Resource Management | https://catalog.kent.edu/colleges/be/mgt/human-resource-management-bba/ |

##### Department of Marketing and Entrepreneurship
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://catalog.kent.edu/colleges/be/mken/entrepreneurship-bba/ |
| 2 | Marketing | https://catalog.kent.edu/colleges/be/mken/marketing-bba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://catalog.kent.edu/colleges/be/mken/advertising-bs/ |

##### Department of Sport, Hospitality and Event Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality and Event Management | https://catalog.kent.edu/colleges/be/shem/hospitality-event-management-bs/ |

---

#### College of Aeronautics and Engineering

##### School of Aeronautics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautical Studies | https://catalog.kent.edu/colleges/ar/aern/aeronautical-studies-bs/ |
| 2 | Air Traffic and Airspace Management | https://catalog.kent.edu/colleges/ar/aern/air-traffic-airspace-management-bs/ |

##### School of Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.kent.edu/colleges/ar/engr/aerospace-engineering-bs/ |
| 2 | Aerospace Engineering Technology | https://catalog.kent.edu/colleges/ar/engr/aerospace-engineering-technology-bs/ |

---

#### College of Applied and Technical Studies

###### A.A.B.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting Technology | https://catalog.kent.edu/colleges/ap/accounting-technology-aab/ |
| 2 | Business Management Technology | https://catalog.kent.edu/colleges/ap/business-management-technology-aab/ |
| 3 | Cybersecurity | https://catalog.kent.edu/colleges/ap/cybersecurity-aab/ |
| 4 | Information Technology | https://catalog.kent.edu/colleges/ap/information-technology-aab/ |
| 5 | Office Technology | https://catalog.kent.edu/colleges/ap/office-technology-aab/ |

###### A.A.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Justice Studies | https://catalog.kent.edu/colleges/ap/criminology-justice-studies-aas/ |
| 2 | Early Years Education and Care | https://catalog.kent.edu/colleges/ap/early-years-education-and-care-aas/ |
| 3 | Electrical/Electronic Engineering Technology | https://catalog.kent.edu/colleges/ap/electrical-electronic-engineering-technology-aas/ |
| 4 | Human Services | https://catalog.kent.edu/colleges/ap/human-services-aas/ |
| 5 | Mechanical Engineering Technology | https://catalog.kent.edu/colleges/ap/mechanical-engineering-technology-aas/ |
| 6 | Nursing (ADN) | https://catalog.kent.edu/colleges/ap/nursing-adn-aas/ |
| 7 | Occupational Therapy Assistant | https://catalog.kent.edu/colleges/ap/occupational-therapy-assistant-aas/ |
| 8 | Physical Therapist Assistant Technology | https://catalog.kent.edu/colleges/ap/physical-therapist-assistant-technology-aas/ |
| 9 | Radiologic Technology | https://catalog.kent.edu/colleges/ap/radiologic-technology-aas/ |
| 10 | Respiratory Therapy | https://catalog.kent.edu/colleges/ap/respiratory-therapy-aas/ |
| 11 | Technical Modeling Design | https://catalog.kent.edu/colleges/ap/technical-modeling-design-aas/ |
| 12 | Veterinary Technology | https://catalog.kent.edu/colleges/ap/veterinary-technology-aas/ |

###### A.T.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Individualized Program | https://catalog.kent.edu/colleges/ap/individualized-program-ats/ |

###### A.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Associate of Arts | https://catalog.kent.edu/colleges/ap/aa/ |

###### A.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Associate of Science | https://catalog.kent.edu/colleges/ap/as/ |

###### A.B.A.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Organizational Leadership | https://catalog.kent.edu/colleges/ap/applied-organizational-leadership-abas/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Technology | https://catalog.kent.edu/colleges/ap/engineering-technology-bs/ |
| 2 | Information Technology | https://catalog.kent.edu/colleges/ap/information-technology-bsit/ |
| 3 | Radiologic Imaging Sciences | https://catalog.kent.edu/colleges/ap/radiologic-imaging-sciences-brit/ |

###### B.S.W.
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.kent.edu/colleges/ap/social-work-bsw/ |

###### B.T.A.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Technical and Applied Studies | https://catalog.kent.edu/colleges/ap/technical-applied-studies-btas/ |

---

#### College of Architecture and Environmental Design

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://catalog.kent.edu/colleges/ae/architectural-studies-ba/ |
| 2 | Interior Design | https://catalog.kent.edu/colleges/ae/interior-design-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.kent.edu/colleges/ae/architecture-bs/ |
| 2 | Construction Management | https://catalog.kent.edu/colleges/ae/construction-management-bs/ |

---

#### College of Communication and Information

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Media | https://catalog.kent.edu/colleges/ci/applied-media-ba/ |

---

#### College of Education and Human Services

###### B.S.E.
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://catalog.kent.edu/colleges/es/early-childhood-education-bse/ |
| 2 | Integrated Language Arts | https://catalog.kent.edu/colleges/es/integrated-language-arts-bse/ |
| 3 | Integrated Mathematics | https://catalog.kent.edu/colleges/es/integrated-mathematics-bse/ |
| 4 | Integrated Science | https://catalog.kent.edu/colleges/es/integrated-science-bse/ |
| 5 | Integrated Social Studies | https://catalog.kent.edu/colleges/es/integrated-social-studies-bse/ |
| 6 | Middle Childhood Education | https://catalog.kent.edu/colleges/es/middle-childhood-education-bse/ |
| 7 | Special Education | https://catalog.kent.edu/colleges/es/special-education-bse/ |

---

#### College of Nursing

###### B.S.N.
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.kent.edu/colleges/nu/nursing-bsn/ |
| 2 | Nursing for Registered Nurses | https://catalog.kent.edu/colleges/nu/nursing-for-registered-nurses-bsn/ |

---

#### College of Public Health and Health Sciences

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Exercise Science | https://catalog.kent.edu/colleges/pb/exercise-science-bs/ |
| 2 | Integrated Health Studies | https://catalog.kent.edu/colleges/pb/integrated-health-studies-bs/ |
| 3 | Long-Term Care Administration | https://catalog.kent.edu/colleges/pb/long-term-care-administration-bs/ |
| 4 | Nutrition | https://catalog.kent.edu/colleges/pb/nutrition-bs/ |
| 5 | Speech Pathology and Audiology | https://catalog.kent.edu/colleges/pb/speech-pathology-audiology-bs/ |
| 6 | Sport and Exercise Performance Psychology | https://catalog.kent.edu/colleges/pb/sport-exercise-performance-psychology-bs/ |
| 7 | Sports Medicine | https://catalog.kent.edu/colleges/pb/sports-medicine-bs/ |

###### B.S.P.H.
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.kent.edu/colleges/pb/public-health-bsph/ |

---

#### College of Sciences and Humanities

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language | https://catalog.kent.edu/colleges/sh/mcls/american-sign-language-ba/ |
| 2 | Anthropology | https://catalog.kent.edu/colleges/sh/anth/anthropology-ba/ |
| 3 | Applied Communication | https://catalog.kent.edu/colleges/sh/comm/applied-communication-ba/ |
| 4 | Art History | https://catalog.kent.edu/colleges/sh/arts/art-history-ba/ |
| 5 | Asian Studies | https://catalog.kent.edu/colleges/sh/mcls/asian-studies-ba/ |
| 6 | Chemistry | https://catalog.kent.edu/colleges/sh/chmb/chemistry-ba/ |
| 7 | Classics | https://catalog.kent.edu/colleges/sh/mcls/classics-ba/ |
| 8 | Communication Studies | https://catalog.kent.edu/colleges/sh/comm/communication-studies-ba/ |
| 9 | Computer Science | https://catalog.kent.edu/colleges/sh/cs/computer-science-ba/ |
| 10 | Economics | https://catalog.kent.edu/colleges/sh/economics-ba/ |
| 11 | English | https://catalog.kent.edu/colleges/sh/eng/english-ba/ |
| 12 | French | https://catalog.kent.edu/colleges/sh/mcls/french-ba/ |
| 13 | Geography | https://catalog.kent.edu/colleges/sh/geog/geography-ba/ |
| 14 | German | https://catalog.kent.edu/colleges/sh/mcls/german-ba/ |
| 15 | History | https://catalog.kent.edu/colleges/sh/hist/history-ba/ |
| 16 | Liberal Studies | https://catalog.kent.edu/colleges/sh/mcls/liberal-studies-ba/ |
| 17 | Philosophy | https://catalog.kent.edu/colleges/sh/phil/philosophy-ba/ |
| 18 | Political Science | https://catalog.kent.edu/colleges/sh/pol/political-science-ba/ |
| 19 | Psychology | https://catalog.kent.edu/colleges/sh/psys/psychology-ba/ |
| 20 | Sociology | https://catalog.kent.edu/colleges/sh/socr/sociology-ba/ |
| 21 | Spanish | https://catalog.kent.edu/colleges/sh/mcls/spanish-ba/ |
| 22 | Studio Art | https://catalog.kent.edu/colleges/sh/arts/studio-art-ba/ |
| 23 | Theatre Studies | https://catalog.kent.edu/colleges/sh/thea/theatre-studies-ba/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics | https://catalog.kent.edu/colleges/sh/math/actuarial-mathematics-bs/ |
| 2 | American Sign Language/English Interpreting | https://catalog.kent.edu/colleges/sh/ldes/american-sign-language-english-interpreting-bs/ |
| 3 | Anthropology | https://catalog.kent.edu/colleges/sh/anth/anthropology-bs/ |
| 4 | Applied Mathematics | https://catalog.kent.edu/colleges/sh/math/applied-mathematics-bs/ |
| 5 | Biochemistry | https://catalog.kent.edu/colleges/sh/chmb/biochemistry-bs/ |
| 6 | Biological Sciences | https://catalog.kent.edu/colleges/sh/bsci/biological-sciences-bs/ |
| 7 | Biotechnology | https://catalog.kent.edu/colleges/sh/bsci/biotechnology-bs/ |
| 8 | Chemistry | https://catalog.kent.edu/colleges/sh/chmb/chemistry-bs/ |
| 9 | Computer Science | https://catalog.kent.edu/colleges/sh/cs/computer-science-bs/ |
| 10 | Computer Science (Cybersecurity) | https://catalog.kent.edu/colleges/sh/cs/computer-science-cybersecurity-bs/ |
| 11 | Conservation | https://catalog.kent.edu/colleges/sh/bsci/conservation-bs/ |
| 12 | Earth Science | https://catalog.kent.edu/colleges/sh/esci/earth-science-bs/ |
| 13 | Economics | https://catalog.kent.edu/colleges/sh/econ/economics-bs/ |
| 14 | Environmental Studies | https://catalog.kent.edu/colleges/sh/geog/environmental-studies-bs/ |
| 15 | Forensic Biology | https://catalog.kent.edu/colleges/sh/bsci/forensic-biology-bs/ |
| 16 | Forensic Chemistry | https://catalog.kent.edu/colleges/sh/chmb/forensic-chemistry-bs/ |
| 17 | Geography | https://catalog.kent.edu/colleges/sh/geog/geography-bs/ |
| 18 | Geology | https://catalog.kent.edu/colleges/sh/esci/geology-bs/ |
| 19 | Information Science | https://catalog.kent.edu/colleges/sh/info/information-science-bs/ |
| 20 | Mathematical Sciences | https://catalog.kent.edu/colleges/sh/math/mathematical-sciences-bs/ |
| 21 | Mathematics | https://catalog.kent.edu/colleges/sh/math/mathematics-bs/ |
| 22 | Medical Laboratory Science | https://catalog.kent.edu/colleges/sh/bms/medical-laboratory-science-bs/ |
| 23 | Molecular Biology | https://catalog.kent.edu/colleges/sh/bsci/molecular-biology-bs/ |
| 24 | Neuroscience | https://catalog.kent.edu/colleges/sh/psys/neuroscience-bs/ |
| 25 | Physics | https://catalog.kent.edu/colleges/sh/phy/physics-bs/ |
| 26 | Psychology | https://catalog.kent.edu/colleges/sh/psys/psychology-bs/ |
| 27 | Science and Technology | https://catalog.kent.edu/colleges/sh/esci/science-technology-bs/ |
| 28 | Sociology | https://catalog.kent.edu/colleges/sh/socr/sociology-bs/ |
| 29 | Statistics | https://catalog.kent.edu/colleges/sh/math/statistics-bs/ |

###### B.I.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Integrative Studies | https://catalog.kent.edu/colleges/sh/integrative-studies-bis/ |

---

#### College of the Arts

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Ceramics | https://catalog.kent.edu/colleges/ca/arts/ceramics-bfa/ |
| 2 | Glass | https://catalog.kent.edu/colleges/ca/arts/glass-bfa/ |
| 3 | Jewelry and Metals | https://catalog.kent.edu/colleges/ca/arts/jewelry-metals-bfa/ |
| 4 | Painting | https://catalog.kent.edu/colleges/ca/arts/painting-bfa/ |
| 5 | Photography | https://catalog.kent.edu/colleges/ca/arts/photography-bfa/ |
| 6 | Print Media and Photography | https://catalog.kent.edu/colleges/ca/arts/print-media-photography-bfa/ |
| 7 | Sculpture and Expanded Media | https://catalog.kent.edu/colleges/ca/arts/sculpture-expanded-media-bfa/ |

###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation Game Design | https://catalog.kent.edu/colleges/ca/arts/animation-game-design-bs/ |
| 2 | Fashion Design | https://catalog.kent.edu/colleges/ca/fdm/fashion-design-bs/ |
| 3 | Fashion Merchandising | https://catalog.kent.edu/colleges/ca/fdm/fashion-merchandising-bs/ |
| 4 | Visual Communication Design | https://catalog.kent.edu/colleges/ca/vcd/visual-communication-design-bs/ |

###### B.M.
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.kent.edu/colleges/ca/mus/music-bm/ |
| 2 | Music Education | https://catalog.kent.edu/colleges/ca/mus/music-education-bm/ |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

No formally designated interdisciplinary undergraduate majors were identified in the catalog. Programs are administratively housed within a single college.

### 1.4 Minors — Complete List

The catalog lists 161 minors. Key minors by college:

| # | Minor | Home College | URL |
|---|-------|-------------|-----|
| 1 | Accessories | Arts | https://catalog.kent.edu/colleges/ca/arts/accessories-minor/ |
| 2 | Accounting | Business | https://catalog.kent.edu/colleges/be/acct/accounting-minor/ |
| 3 | Advertising | Business | https://catalog.kent.edu/colleges/be/mken/advertising-minor/ |
| 4 | Aerospace Engineering | Aeronautics & Engineering | https://catalog.kent.edu/colleges/ar/engr/aerospace-engineering-minor/ |
| 5 | African Studies | Sciences & Humanities | https://catalog.kent.edu/colleges/sh/afs/african-studies-minor/ |
| 6 | Africana Studies | Sciences & Humanities | https://catalog.kent.edu/colleges/sh/afs/africana-studies-minor/ |
| 7 | Aircraft Dispatch | Aeronautics & Engineering | https://catalog.kent.edu/colleges/ar/aern/aircraft-dispatch-minor/ |
| 8 | American Sign Language | Sciences & Humanities | https://catalog.kent.edu/colleges/sh/mcls/american-sign-language-minor/ |
| ... | *(153 additional minors — full list in last-extract.json)* | ... | ... |

> **Note**: The complete list of 161 minors is available in the cached `last-extract.json` file. The catalog page at `https://catalog.kent.edu/programs/` contains the full A-Z listing.

### 1.5 General Education Requirements

Kent State University requires all undergraduate students to complete the Kent Core (general education requirements). Details available at: https://www.kent.edu/admissions

### 1.6 Course-ID → Major Quick-Lookup

Kent State uses a college/department code system in its catalog URLs:
- `be` = Business and Entrepreneurship
- `ar` = Aeronautics and Engineering
- `ap` = Applied and Technical Studies
- `ae` = Architecture and Environmental Design
- `ci` = Communication and Information
- `es` = Education and Human Services
- `nu` = Nursing
- `pm` = Podiatric Medicine
- `pb` = Public Health
- `sh` = Sciences and Humanities
- `ca` = Arts
- `hg` = Honors and Global Education
- `uc` = University College

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Ambassador Crawford College of Business and Entrepreneurship

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.kent.edu/colleges/be/business-administration-phd/ |

##### M.S.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.kent.edu/colleges/be/acct/accounting-msa/ |

##### M.A.E.
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.kent.edu/colleges/be/econ/economics-mae/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting, Business Technology and Analytics | https://catalog.kent.edu/colleges/be/acct/accounting-business-technology-analytics-ms/ |
| 2 | Business Analytics | https://catalog.kent.edu/colleges/be/isba/business-analytics-ms/ |
| 3 | Hospitality and Tourism Management | https://catalog.kent.edu/colleges/be/shem/hospitality-tourism-management-ms/ |

##### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.kent.edu/colleges/be/mgt/business-administration-mba/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting Analytics | https://catalog.kent.edu/colleges/be/acct/accounting-analytics-graduate-certificate/ |
| 2 | Accounting Fundamentals | https://catalog.kent.edu/colleges/be/acct/accounting-fundamentals-graduate-certificate/ |
| 3 | Advanced Accounting CPA Track | https://catalog.kent.edu/colleges/be/acct/advanced-accounting-cpa-track-graduate-certificate/ |
| 4 | Quantitative Business Management | https://catalog.kent.edu/colleges/be/isba/quantitative-business-management-graduate-certificate/ |
| 5 | Human Resource Management | https://catalog.kent.edu/colleges/be/mgt/human-resource-management-graduate-certificate/ |
| 6 | International Business | https://catalog.kent.edu/colleges/be/mgt/international-business-graduate-certificate/ |
| 7 | Leadership and Management | https://catalog.kent.edu/colleges/be/mgt/leadership-and-management-graduate-certificate/ |
| 8 | Leading Through Challenge | https://catalog.kent.edu/colleges/be/mgt/leading-through-challenge-graduate-certificate/ |
| 9 | Sport and Recreation Management | https://catalog.kent.edu/colleges/be/shem/sport-recreation-management-graduate-certificate/ |
| 10 | Esports Management | https://catalog.kent.edu/colleges/be/shem/esports-management-graduate-certificate/ |

---

#### College of Aeronautics and Engineering

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.kent.edu/colleges/ar/engr/aerospace-engineering-phd/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.kent.edu/colleges/ar/engr/aerospace-engineering-ms/ |
| 2 | Engineering and Technology (Applied) | https://catalog.kent.edu/colleges/ar/engr/engineering-technology-applied-ms/ |

---

#### College of Architecture and Environmental Design

##### M.Arch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.kent.edu/colleges/ae/architecture-march/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture and Environmental Design | https://catalog.kent.edu/colleges/ae/architecture-environmental-design-ms/ |
| 2 | Construction Management | https://catalog.kent.edu/colleges/ae/construction-management-ms/ |

##### M.L.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture (First Professional) | https://catalog.kent.edu/colleges/ae/landscape-architecture-mla-i/ |
| 2 | Landscape Architecture (Post-Professional) | https://catalog.kent.edu/colleges/ae/landscape-architecture-mla-ii/ |

##### M.H.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Healthcare Design | https://catalog.kent.edu/colleges/ae/healthcare-design-mhd/ |

##### M.U.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Design | https://catalog.kent.edu/colleges/ae/urban-design-mud/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Systems and Facilities Design | https://catalog.kent.edu/colleges/ae/health-systems-and-facilities-design-graduate-certificate/ |

---

#### College of Communication and Information

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication and Information | https://catalog.kent.edu/colleges/ci/communication-information-phd/ |

---

#### College of Education and Human Services

##### M.Ed.
| # | 项目 | URL |
|---|------|-----|
| 1 | Cultural Foundations of Education | https://catalog.kent.edu/colleges/es/ldes/cultural-foundations-education-med/ |
| 2 | Educational Psychology | https://catalog.kent.edu/colleges/es/ldes/educational-psychology-med/ |
| 3 | Higher Education Administration | https://catalog.kent.edu/colleges/es/ldes/higher-education-administration-med/ |
| 4 | Instructional Technology | https://catalog.kent.edu/colleges/es/tlc/instructional-technology-med/ |
| 5 | Library and Information Science (K-12) | https://catalog.kent.edu/colleges/es/ldes/library-information-science-k12-med/ |
| 6 | Literacy Education | https://catalog.kent.edu/colleges/es/tlc/literacy-education-med/ |
| 7 | Mathematics Education | https://catalog.kent.edu/colleges/es/tlc/mathematics-education-med/ |
| 8 | Music Education | https://catalog.kent.edu/colleges/es/tlc/music-education-med/ |
| 9 | Science Education | https://catalog.kent.edu/colleges/es/tlc/science-education-med/ |
| 10 | Social Studies Education | https://catalog.kent.edu/colleges/es/tlc/social-studies-education-med/ |
| 11 | Special Education | https://catalog.kent.edu/colleges/es/ldes/special-education-med/ |
| 12 | Sport, Leisure and Recreation Management | https://catalog.kent.edu/colleges/es/ldes/sport-leisure-recreation-management-med/ |
| 13 | Teaching and Learning (General) | https://catalog.kent.edu/colleges/es/tlc/teaching-learning-med/ |
| 14 | Workforce Education | https://catalog.kent.edu/colleges/es/tlc/workforce-education-med/ |

##### Ed.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling and Mental Wellness | https://catalog.kent.edu/colleges/es/ldes/counseling-mental-wellness-eds/ |
| 2 | Higher Education Administration | https://catalog.kent.edu/colleges/es/ldes/higher-education-administration-eds/ |
| 3 | School Psychology | https://catalog.kent.edu/colleges/es/ldes/school-psychology-eds/ |
| 4 | Special Education | https://catalog.kent.edu/colleges/es/ldes/special-education-eds/ |
| 5 | Teaching, Learning and Curriculum Studies | https://catalog.kent.edu/colleges/es/tlc/teaching-learning-curriculum-studies-eds/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Addictions Counseling | https://catalog.kent.edu/colleges/es/ldes/addictions-counseling-graduate-certificate/ |
| 2 | College Teaching | https://catalog.kent.edu/colleges/es/tlc/college-teaching-graduate-certificate/ |
| 3 | Disability Studies and Community Inclusion | https://catalog.kent.edu/colleges/es/ldes/disability-studies-community-inclusion-graduate-certificate/ |
| 4 | Health and Physical Education | https://catalog.kent.edu/colleges/es/tlc/health-physical-education-graduate-certificate/ |
| 5 | Library and Information Science | https://catalog.kent.edu/colleges/es/ldes/library-information-science-graduate-certificate/ |
| 6 | Online Learning and Teaching | https://catalog.kent.edu/colleges/es/tlc/online-learning-teaching-graduate-certificate/ |
| 7 | Qualitative Research Methods in Education | https://catalog.kent.edu/colleges/es/tlc/qualitative-research-methods-education-graduate-certificate/ |

---

#### College of Nursing

##### M.S.N.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.kent.edu/colleges/nu/nursing-msn/ |

##### D.N.P.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.kent.edu/colleges/nu/nursing-dnp/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.kent.edu/colleges/nu/nursing-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult Gerontology Acute Care Nurse Practitioner | https://catalog.kent.edu/colleges/nu/adult-gerontology-acute-care-nurse-practitioner-graduate-certificate/ |
| 2 | Adult Gerontology Clinical Nurse Specialist | https://catalog.kent.edu/colleges/nu/adult-gerontology-clinical-nurse-specialist-graduate-certificate/ |
| 3 | Adult Gerontology Primary Care Nurse Practitioner | https://catalog.kent.edu/colleges/nu/adult-gerontology-primary-care-nurse-practitioner-graduate-certificate/ |
| 4 | Adult/Adolescent Sexual Assault Nurse Examiner | https://catalog.kent.edu/colleges/nu/adult-adolescent-sexual-assault-nurse-examiner-graduate-certificate/ |
| 5 | Family Nurse Practitioner | https://catalog.kent.edu/colleges/nu/family-nurse-practitioner-graduate-certificate/ |
| 6 | Nurse Educator | https://catalog.kent.edu/colleges/nu/nurse-educator-graduate-certificate/ |
| 7 | Nursing Administration and Health System Leadership | https://catalog.kent.edu/colleges/nu/nursing-administration-health-system-leadership-graduate-certificate/ |
| 8 | Pediatric Primary Care Nurse Practitioner | https://catalog.kent.edu/colleges/nu/pediatric-primary-care-nurse-practitioner-graduate-certificate/ |
| 9 | Psychiatric Mental Health Nurse Practitioner | https://catalog.kent.edu/colleges/nu/psychiatric-mental-health-nurse-practitioner-graduate-certificate/ |
| 10 | Women's Health Nurse Practitioner | https://catalog.kent.edu/colleges/nu/womens-health-nurse-practitioner-graduate-certificate/ |

---

#### College of Podiatric Medicine

##### D.P.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Podiatric Medicine | https://catalog.kent.edu/colleges/pm/podiatric-medicine-dpm/ |

---

#### College of Public Health and Health Sciences

##### Au.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | https://catalog.kent.edu/colleges/pb/audiology-aud/ |

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | https://catalog.kent.edu/colleges/pb/audiology-ma/ |
| 2 | Speech-Language Pathology | https://catalog.kent.edu/colleges/pb/speech-language-pathology-ma/ |
| 3 | Sociology (Applied) | https://catalog.kent.edu/colleges/pb/sociology-applied-ma/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.kent.edu/colleges/pb/athletic-training-ms/ |
| 2 | Clinical Epidemiology | https://catalog.kent.edu/colleges/pb/clinical-epidemiology-ms/ |
| 3 | Exercise Physiology | https://catalog.kent.edu/colleges/pb/exercise-physiology-ms/ |
| 4 | Nutrition | https://catalog.kent.edu/colleges/pb/nutrition-ms/ |

##### M.P.H.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://catalog.kent.edu/colleges/pb/biostatistics-mph/ |
| 2 | Epidemiology | https://catalog.kent.edu/colleges/pb/epidemiology-mph/ |
| 3 | Health Policy and Management | https://catalog.kent.edu/colleges/pb/health-policy-management-mph/ |
| 4 | Social and Behavioral Sciences | https://catalog.kent.edu/colleges/pb/social-behavioral-sciences-mph/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://catalog.kent.edu/colleges/pb/communication-sciences-disorders-phd/ |
| 2 | Exercise Physiology | https://catalog.kent.edu/colleges/pb/exercise-physiology-phd/ |
| 3 | Public Health | https://catalog.kent.edu/colleges/pb/public-health-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Research | https://catalog.kent.edu/colleges/pb/clinical-research-graduate-certificate/ |
| 2 | Healthcare Compliance | https://catalog.kent.edu/colleges/pb/healthcare-compliance-graduate-certificate/ |

---

#### College of Sciences and Humanities

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.kent.edu/colleges/sh/bsci/biological-sciences-phd/ |
| 2 | Chemistry | https://catalog.kent.edu/colleges/sh/chmb/chemistry-phd/ |
| 3 | Clinical Psychology | https://catalog.kent.edu/colleges/sh/psys/clinical-psychology-phd/ |
| 4 | Computer Science | https://catalog.kent.edu/colleges/sh/cs/computer-science-phd/ |
| 5 | Counselor Education and Supervision | https://catalog.kent.edu/colleges/sh/ldes/counselor-education-supervision-phd/ |
| 6 | Earth Sciences | https://catalog.kent.edu/colleges/sh/esci/earth-sciences-phd/ |
| 7 | Economics | https://catalog.kent.edu/colleges/sh/econ/economics-phd/ |
| 8 | Educational Psychology | https://catalog.kent.edu/colleges/sh/ldes/educational-psychology-phd/ |
| 9 | English | https://catalog.kent.edu/colleges/sh/eng/english-phd/ |
| 10 | Evaluation and Measurement | https://catalog.kent.edu/colleges/sh/ldes/evaluation-measurement-phd/ |
| 11 | Geography | https://catalog.kent.edu/colleges/sh/geog/geography-phd/ |
| 12 | History | https://catalog.kent.edu/colleges/sh/hist/history-phd/ |
| 13 | Materials Science | https://catalog.kent.edu/colleges/sh/materials-science-phd/ |
| 14 | Mathematical Sciences | https://catalog.kent.edu/colleges/sh/math/mathematical-sciences-phd/ |
| 15 | Philosophy | https://catalog.kent.edu/colleges/sh/phil/philosophy-phd/ |
| 16 | Physics | https://catalog.kent.edu/colleges/sh/phy/physics-phd/ |
| 17 | Political Science | https://catalog.kent.edu/colleges/sh/pol/political-science-phd/ |
| 18 | Psychology (General) | https://catalog.kent.edu/colleges/sh/psys/psychology-phd/ |
| 19 | School Psychology | https://catalog.kent.edu/colleges/sh/ldes/school-psychology-phd/ |
| 20 | Sociology | https://catalog.kent.edu/colleges/sh/socr/sociology-phd/ |
| 21 | Speech-Language Pathology | https://catalog.kent.edu/colleges/sh/ldes/speech-language-pathology-phd/ |
| 22 | Translation Studies | https://catalog.kent.edu/colleges/sh/mcls/translation-studies-phd/ |

##### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://catalog.kent.edu/colleges/sh/education-edd/ |

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.kent.edu/colleges/sh/anth/anthropology-ma/ |
| 2 | Applied Mathematics | https://catalog.kent.edu/colleges/sh/math/applied-mathematics-ma/ |
| 3 | Chemistry | https://catalog.kent.edu/colleges/sh/chmb/chemistry-ma/ |
| 4 | Communication Studies | https://catalog.kent.edu/colleges/sh/comm/communication-studies-ma/ |
| 5 | Computer Science | https://catalog.kent.edu/colleges/sh/cs/computer-science-ma/ |
| 6 | Economics | https://catalog.kent.edu/colleges/sh/econ/economics-ma/ |
| 7 | English | https://catalog.kent.edu/colleges/sh/eng/english-ma/ |
| 8 | Geography | https://catalog.kent.edu/colleges/sh/geog/geography-ma/ |
| 9 | History | https://catalog.kent.edu/colleges/sh/hist/history-ma/ |
| 10 | Philosophy | https://catalog.kent.edu/colleges/sh/phil/philosophy-ma/ |
| 11 | Physics | https://catalog.kent.edu/colleges/sh/phy/physics-ma/ |
| 12 | Political Science | https://catalog.kent.edu/colleges/sh/pol/political-science-ma/ |
| 13 | Psychology | https://catalog.kent.edu/colleges/sh/psys/psychology-ma/ |
| 14 | Sociology | https://catalog.kent.edu/colleges/sh/socr/sociology-ma/ |
| 15 | Spanish | https://catalog.kent.edu/colleges/sh/mcls/spanish-ma/ |
| 16 | Teaching English as a Second Language | https://catalog.kent.edu/colleges/sh/mcls/teaching-english-second-language-ma/ |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.kent.edu/colleges/sh/bsci/biological-sciences-ms/ |
| 2 | Chemistry | https://catalog.kent.edu/colleges/sh/chmb/chemistry-ms/ |
| 3 | Computer Science | https://catalog.kent.edu/colleges/sh/cs/computer-science-ms/ |
| 4 | Earth Sciences | https://catalog.kent.edu/colleges/sh/esci/earth-sciences-ms/ |
| 5 | Geography | https://catalog.kent.edu/colleges/sh/geog/geography-ms/ |
| 6 | Materials Science | https://catalog.kent.edu/colleges/sh/materials-science-ms/ |
| 7 | Mathematical Sciences | https://catalog.kent.edu/colleges/sh/math/mathematical-sciences-ms/ |
| 8 | Physics | https://catalog.kent.edu/colleges/sh/phy/physics-ms/ |
| 9 | Psychology (Experimental) | https://catalog.kent.edu/colleges/sh/psys/psychology-experimental-ms/ |

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Acting | https://catalog.kent.edu/colleges/ca/thea/acting-mfa/ |
| 2 | Creative Writing | https://catalog.kent.edu/colleges/sh/eng/creative-writing-mfa/ |
| 3 | Design and Technology | https://catalog.kent.edu/colleges/ca/thea/design-technology-mfa/ |
| 4 | Drawing | https://catalog.kent.edu/colleges/ca/arts/drawing-mfa/ |
| 5 | Playwriting | https://catalog.kent.edu/colleges/ca/thea/playwriting-mfa/ |

##### L.S.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Liberal Studies | https://catalog.kent.edu/colleges/sh/liberal-studies-lsm/ |

##### M.G.I.Sc.
| # | 项目 | URL |
|---|------|-----|
| 1 | Geographic Information Science | https://catalog.kent.edu/colleges/sh/geog/geographic-information-science-mgisc/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Data Science | https://catalog.kent.edu/colleges/sh/cs/applied-data-science-graduate-certificate/ |
| 2 | Cybersecurity | https://catalog.kent.edu/colleges/sh/cs/cybersecurity-graduate-certificate/ |
| 3 | Data Science | https://catalog.kent.edu/colleges/sh/math/data-science-graduate-certificate/ |
| 4 | Geographic Information Science | https://catalog.kent.edu/colleges/sh/geog/geographic-information-science-graduate-certificate/ |
| 5 | Health Policy | https://catalog.kent.edu/colleges/sh/pol/health-policy-graduate-certificate/ |
| 6 | Nonprofit Management | https://catalog.kent.edu/colleges/sh/pol/nonprofit-management-graduate-certificate/ |
| 7 | Peace and Conflict Studies | https://catalog.kent.edu/colleges/sh/pol/peace-conflict-studies-graduate-certificate/ |
| 8 | Social and Behavioral Health | https://catalog.kent.edu/colleges/sh/socr/social-behavioral-health-graduate-certificate/ |
| 9 | Teaching English as a Second Language | https://catalog.kent.edu/colleges/sh/mcls/teaching-english-second-language-graduate-certificate/ |
| 10 | Women's and Gender Studies | https://catalog.kent.edu/colleges/sh/mssh/womens-gender-studies-graduate-certificate/ |

---

#### College of the Arts

##### M.F.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Acting | https://catalog.kent.edu/colleges/ca/thea/acting-mfa/ |
| 2 | Design and Technology | https://catalog.kent.edu/colleges/ca/thea/design-technology-mfa/ |
| 3 | Drawing | https://catalog.kent.edu/colleges/ca/arts/drawing-mfa/ |
| 4 | Playwriting | https://catalog.kent.edu/colleges/ca/thea/playwriting-mfa/ |
| 5 | Visual Communication Design | https://catalog.kent.edu/colleges/ca/vcd/visual-communication-design-mfa/ |

##### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | https://catalog.kent.edu/colleges/ca/mus/music-education-mm/ |
| 2 | Music Performance | https://catalog.kent.edu/colleges/ca/mus/music-performance-mm/ |

##### M.F.I.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Industry Studies | https://catalog.kent.edu/colleges/ca/fdm/fashion-industry-studies-mfis/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Industry Studies | https://catalog.kent.edu/colleges/ca/fdm/fashion-industry-studies-graduate-certificate/ |
| 2 | Music Performance | https://catalog.kent.edu/colleges/ca/mus/music-performance-graduate-certificate/ |

---

### 2.2 Program Deep-Dive: Computer Science (Ph.D.)

- **Department**: Department of Computer Science, College of Sciences and Humanities
- **Address**: Kent State University, Kent, OH 44242
- **Application portal**: https://apply.kent.edu/apply/
- **Application fee**: $50
- **GPA requirement**: 2.750 minimum (program may require higher)
- **GRE**: Program-specific; check department requirements
- **English proficiency**: TOEFL 71 / IELTS 6.0 / Duolingo 100 (international applicants)
- **Deadlines**: Rolling; recommended to apply early
- **Catalog page**: https://catalog.kent.edu/colleges/sh/cs/computer-science-phd/

### 2.3 Graduate Admissions Model

**Centralized application portal** with program-specific requirements:
- All graduate applications go through https://apply.kent.edu/apply/
- Minimum university requirements: bachelor's degree, 2.750 GPA
- Programs set additional requirements (GRE, portfolios, writing samples, etc.)
- Graduate admissions office: 330-672-2444, gradadmissions@kent.edu
- Over 200 graduate programs available on campus or online

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | https://apply.kent.edu/apply/ | kent.edu/admissions/apply |
| Common App | https://apply.commonapp.org/login?ma=862 | kent.edu/admissions/apply |
| Application fee | $50 (non-refundable) | kent.edu/admissions/first-year-student-requirements |
| Priority deadline | November 1 | kent.edu/admissions/first-year-student-requirements |
| Applications open | August 1 | kent.edu/admissions/first-year-student-requirements |
| National Decision Day | May 1 | kent.edu/admissions/first-year-student-requirements |
| Merit scholarship deadline extension | August 1 | kent.edu/admissions/first-year-student-requirements |
| Admission type | Rolling | kent.edu/admissions/first-year-student-requirements |
| Test policy | Test-optional | kent.edu/admissions/first-year-student-requirements |
| GPA requirement | 2.0 minimum | kent.edu/admissions/first-year-student-requirements |
| Recommendation letters | Not required | kent.edu/admissions/first-year-student-requirements |
| Interview | Not required | kent.edu/admissions/first-year-student-requirements |

**International First-Year Deadlines**:
| 学期 | 截止日期 |
|------|---------|
| Spring | October 1 |
| Fall | June 1 |

**Transfer Student Requirements**: Application + transcripts from all colleges attended.

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分 | 备注 |
|------|--------|------|
| TOEFL iBT | 71 | Institution code: 1367 |
| IELTS Academic | 6.0 | Must upload scanned PDF |
| Duolingo | 100 | Accepted |
| PTE | Accepted | Check website for minimum |

> **Source**: https://www.kent.edu/admissions/international-first-year-student-requirements
> **Applicability**: Required for all international applicants whose native language is not English

### 3.3 Graduate — Global Rules

- **Application portal**: https://apply.kent.edu/apply/
- **Application fee**: $50
- **Minimum GPA**: 2.750 (some programs require higher)
- **GRE/GMAT**: Program-specific; not universally required
- **English proficiency**: Same as undergraduate (TOEFL 71 / IELTS 6.0 / Duolingo 100)
- **Bachelor's degree**: Required from accredited institution
- **Admission type**: Rolling (program-specific deadlines may apply)
- **Graduate admissions office**: 330-672-2444, gradadmissions@kent.edu
- **International graduate requirements**: https://www.kent.edu/node/951871

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| 费用项目 | Ohio Resident | Non-Ohio Resident |
|---------|---------------|-------------------|
| Tuition (12-18 credit hours) | $13,848.40 | $24,298.00 |
| Food & Housing | $14,360.00 | $14,360.00 |
| **Total** | **$28,208.40** | **$38,658.00** |

**International Student Additional Costs**:
| 费用项目 | 金额 |
|---------|------|
| Tuition | $24,298.00 |
| Food & Housing | $14,360.00 |
| Medical Insurance, Books & Supplies | $3,704.00 |
| **Total** | **$42,362.00** |

**Per Credit Hour Rates (Ohio Resident, Lower Division)**:
| Credit Hours | Instructional Fee | General Fee | Total |
|-------------|-------------------|-------------|-------|
| 1 | $540.30 | $88.76 | $629.06 |
| 12-18 | $5,947.20 | $977.00 | $6,924.20 |

> **Source**: https://www.kent.edu/tuition
> **Note**: Tuition is guaranteed for 4 years (Golden Guarantee)

### 4.2 Undergraduate Financial Aid Policy

- **Financial aid awarded**: $375+ million (2024-2025)
- **First-year students receiving aid**: 93%
- **Scholarships to first-year students**: $80+ million
- **Transfer students receiving aid**: 85%
- **Transfer scholarships**: $2.5+ million
- **Debt-free graduation rate**: 36% of Kent Campus students
- **Tuition guarantee**: 4 years locked in for tuition, housing and food
- **Need-blind/need-aware**: Need-aware for all applicants
- **Flashes Go Further Scholarship**: Covers gap between grants/scholarships and full tuition for Ohio students
- **Net Price Calculator**: https://www.kent.edu/node/62621

### 4.3 Graduate Cost & Funding Framework

**Graduate Tuition (2026-2027)**:
| 费用项目 | Ohio Resident | Non-Ohio Resident |
|---------|---------------|-------------------|
| Tuition | $13,445.20 | $23,894.80 |
| Food & Housing | $13,920.00 | $13,920.00 |
| **Total** | **$27,365.20** | **$37,814.80** |

**In-State Tuition Discount**: Ohio bachelor's degree holders may qualify for in-state rates for graduate programs.

**Graduate funding types**:
- Research Assistantships (RA)
- Teaching Assistantships (TA)
- Fellowships
- Grants
- Graduate assistantships

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Application Fee
```yaml
field: undergraduate.application.fee
value: 50
source_url: https://www.kent.edu/admissions/first-year-student-requirements
source_snippet: "Pay the non-refundable $50 application fee."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Priority Deadline
```yaml
field: undergraduate.deadlines.priority
value: "November 1"
source_url: https://www.kent.edu/admissions/first-year-student-requirements
source_snippet: "Nov. 1 Priority Application Deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test Policy
```yaml
field: undergraduate.testing.policy
value: "Test-optional"
source_url: https://www.kent.edu/admissions/first-year-student-requirements
source_snippet: "Test Scores (Optional)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: UG Tuition Ohio Resident
```yaml
field: undergraduate.cost.tuition_ohio_resident
value: 13848.40
source_url: https://www.kent.edu/tuition
source_snippet: "Tuition1 | $13,848.40 | $24,298.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: UG Tuition Non-Ohio Resident
```yaml
field: undergraduate.cost.tuition_non_resident
value: 24298.00
source_url: https://www.kent.edu/tuition
source_snippet: "Tuition1 | $13,848.40 | $24,298.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: UG Housing & Food
```yaml
field: undergraduate.cost.housing_food
value: 14360.00
source_url: https://www.kent.edu/tuition
source_snippet: "Food & Housing2 | $14,360.00 | $14,360.00"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: TOEFL Minimum
```yaml
field: undergraduate.english_proficiency.toefl_ibt
value: 71
source_url: https://www.kent.edu/admissions/international-first-year-student-requirements
source_snippet: "TOEFL iBT: 71"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: IELTS Minimum
```yaml
field: undergraduate.english_proficiency.ielts
value: 6.0
source_url: https://www.kent.edu/admissions/international-first-year-student-requirements
source_snippet: "IELTS Academic and IELTS indicator: 6"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: Duolingo Minimum
```yaml
field: undergraduate.english_proficiency.duolingo
value: 100
source_url: https://www.kent.edu/admissions/international-first-year-student-requirements
source_snippet: "Duolingo:100"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: International Deadlines
```yaml
field: undergraduate.deadlines.international
value: {spring: "October 1", fall: "June 1"}
source_url: https://www.kent.edu/admissions/international-first-year-student-requirements
source_snippet: "Oct. 1 Spring Semester Application Deadline | June 1 Fall Semester Application Deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate GPA Requirement
```yaml
field: graduate.admissions.minimum_gpa
value: 2.750
source_url: https://www.kent.edu/admissions/graduate-degree-student-requirements
source_snippet: "A total undergraduate grade point average (GPA) of at least 2.750 on a 4.000 point scale."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Tuition Ohio Resident
```yaml
field: graduate.cost.tuition_ohio_resident
value: 13445.20
source_url: https://www.kent.edu/tuition
source_snippet: "Tuition1 | $13,445.20 | $23,894.80"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-003: Graduate Program Count
```yaml
field: graduate.programs.total_count
value: "200+"
source_url: https://www.kent.edu/admissions/graduate-degree-student-requirements
source_snippet: "Explore over 200 graduate programs available on campus or online."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Financial Aid Stats
```yaml
field: undergraduate.financial_aid.total_awarded
value: "$375+ million (2024-2025)"
source_url: https://www.kent.edu/admissions/cost-aid
source_snippet: "$375+ Million in Financial Aid Awarded in 2024-2025"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-005: Catalog Program Count
```yaml
field: institution.programs.total_catalog_entries
value: 610
source_url: https://catalog.kent.edu/programs/
source_snippet: "370+ world-class programs of study" (marketing) / 610 (actual catalog count)
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
kent-state-knowledge-base-v2
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-business.md                   (Section 1: Business college programs)
├── 02-ug-aeronautics-engineering.md    (Section 1: A&E programs)
├── 03-ug-applied-technical.md          (Section 1: Applied & Technical)
├── 04-ug-architecture.md               (Section 1: Architecture)
├── 05-ug-communication.md              (Section 1: Communication)
├── 06-ug-education.md                  (Section 1: Education)
├── 07-ug-nursing.md                    (Section 1: Nursing)
├── 08-ug-public-health.md              (Section 1: Public Health)
├── 09-ug-sciences-humanities.md        (Section 1: Sciences & Humanities)
├── 10-ug-arts.md                       (Section 1: Arts)
├── 11-grad-business.md                 (Section 2: Business graduate)
├── 12-grad-aeronautics-engineering.md  (Section 2: A&E graduate)
├── 13-grad-architecture.md             (Section 2: Architecture graduate)
├── 14-grad-communication.md            (Section 2: Communication graduate)
├── 15-grad-education.md                (Section 2: Education graduate)
├── 16-grad-nursing.md                  (Section 2: Nursing graduate)
├── 17-grad-podiatric-medicine.md       (Section 2: Podiatric Medicine)
├── 18-grad-public-health.md            (Section 2: Public Health graduate)
├── 19-grad-sciences-humanities.md      (Section 2: Sciences & Humanities graduate)
├── 20-grad-arts.md                     (Section 2: Arts graduate)
├── 21-deadlines-requirements.md        (Section 3)
├── 22-costs-financial-aid.md           (Section 4)
├── 23-evidence-chain.md                (Section 5)
└── 24-monitoring-watchlist.md          (Section 4 monitoring)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "kent-state-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BFA|BBA|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Full per-program GRE/GMAT requirements | Catalog per-program pages |
| P0 | Graduate application fee (if different from UG) | https://www.kent.edu/admissions/graduate-degree-student-requirements |
| P1 | Detailed Kent Core requirements | https://www.kent.edu/admissions |
| P1 | Per-college department subdivisions for applied/technical studies | https://catalog.kent.edu/colleges/ap/ |
| P1 | International graduate tuition breakdown | https://www.kent.edu/tuition |
| P2 | Regional campus tuition rates | https://www.kent.edu/admissions/regional-campus-cost-aid-and-scholarships |
| P2 | Graduate funding/stipend details | Graduate college website |
| P2 | Online program tuition rates | https://onlinedegrees.kent.edu/tuition-costs/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Kent State | *(Other schools)* |
|------|-----------|-------------------|
| Type | Public Research | |
| Location | Kent, Ohio | |
| UG Tuition (In-State) | $13,848.40 | |
| UG Tuition (Out-of-State) | $24,298.00 | |
| UG Total COA (In-State) | $28,208.40 | |
| UG Total COA (Out-of-State) | $38,658.00 | |
| Need-Blind (Intl?) | Need-aware for all | |
| EA Deadline | N/A (Rolling) | |
| Priority Deadline | November 1 | |
| RA Deadline | Rolling | |
| SAT/ACT Required? | Test-optional | |
| TOEFL Min | 71 | |
| IELTS Min | 6.0 | |
| Duolingo Min | 100 | |
| Application Fee | $50 | |
| Grad GPA Min | 2.750 | |
| Total Program Count | 610 (catalog entries) | |
| UG Majors | 129 | |
| Grad Degrees | 126 | |
| School/Department Count | 13 colleges | |
| Tuition Guarantee | 4 years | |
| Financial Aid Awarded | $375+ million | |
| Debt-Free Graduation Rate | 36% | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: kent.edu, catalog.kent.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
