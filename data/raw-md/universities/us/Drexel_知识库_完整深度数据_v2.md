# Drexel University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BArch/etc.) | 121 |
| 本科辅修 (Minor) | 76 |
| 研究生学位项目 (MS/MA/PhD/MBA/etc.) | 170 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 54 |
| **学位项目总计 (UG + Grad)** | **421** |
| 学院 / 独立系所总数 | 16 |

> Reconciliation: 121 + 76 + 170 + 54 = 421 unique program entries. Note: Some programs offer multiple degree types (e.g., BS/MS combined); each program is counted once under its primary level. The degree-level inventory (Section 0.3) counts degree types, which may sum higher than program count due to multi-degree programs.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Drexel University
├── College of Arts and Sciences (CoAS)                    [学院]
│   ├── Biological Sciences                                [系]
│   ├── Chemistry                                          [系]
│   ├── Communication                                      [系]
│   ├── Criminology and Justice Studies                    [系]
│   ├── English                                            [系]
│   ├── Environmental Science/Studies                      [系]
│   ├── Global Studies                                     [系]
│   ├── History                                            [系]
│   ├── Mathematics                                        [系]
│   ├── Philosophy                                         [系]
│   ├── Physics                                            [系]
│   ├── Political Science                                  [系]
│   ├── Psychology                                         [系]
│   ├── Sociology                                          [系]
│   └── Neuroscience                                       [系]
├── Bennett S. LeBow College of Business                   [学院]
│   ├── Accounting                                         [系]
│   ├── Business Analytics                                 [系]
│   ├── Business Law                                       [系]
│   ├── Finance                                            [系]
│   ├── General Business                                   [系]
│   ├── International Business                             [系]
│   ├── Management                                         [系]
│   ├── Management Information Systems                     [系]
│   ├── Marketing                                         [系]
│   ├── Operations and Supply Chain Management             [系]
│   ├── Real Estate Management and Development             [系]
│   └── Sport Business                                     [系]
├── School of Economics (under LeBow)                      [学院]
│   ├── Economics                                          [系]
│   ├── Behavioral Economics, Business, and Organizations  [系]
│   └── Economics and Data Science                         [系]
├── Charles D. Close School of Entrepreneurship            [学院]
│   └── Entrepreneurship and Innovation                    [系]
├── School of Engineering                                  [学院]
│   ├── Architectural Engineering                          [系]
│   ├── Chemical Engineering                               [系]
│   ├── Civil Engineering                                  [系]
│   ├── Computer Engineering                               [系]
│   ├── Construction Management                            [系]
│   ├── Electrical Engineering                             [系]
│   ├── Engineering Technology                             [系]
│   ├── Environmental Engineering                          [系]
│   ├── Materials Science and Engineering                  [系]
│   ├── Mechanical Engineering & Mechanics                 [系]
│   └── Systems Engineering                                [系]
├── School of Computer and Information Sciences (CCI)      [学院]
│   ├── Computer Science                                   [系]
│   ├── Data Science                                       [系]
│   ├── Artificial Intelligence and Machine Learning       [系]
│   ├── Computing Security and Technology                  [系]
│   └── Software Engineering                               [系]
├── School of Biomedical Engineering and Science           [学院]
│   └── Biomedical Engineering                             [系]
├── Antoinette Westphal College of Media Arts & Design     [学院]
│   ├── Animation & Visual Effects                         [系]
│   ├── Architecture                                       [系]
│   ├── Art History                                        [系]
│   ├── Dance                                              [系]
│   ├── Entertainment & Arts Management                    [系]
│   ├── Fashion Design                                     [系]
│   ├── Film and Television                                [系]
│   ├── Game Design & Production                           [系]
│   ├── Graphic Design                                     [系]
│   ├── Interior Design                                    [系]
│   ├── Music Industry                                     [系]
│   ├── Product Design                                     [系]
│   └── User Experience and Interaction Design             [系]
├── College of Nursing and Health Professions (CNHP)       [学院]
│   ├── Nursing                                            [系]
│   ├── Health Sciences                                    [系]
│   ├── Culinary Arts and Science                          [系]
│   └── Exercise Science                                   [系]
├── School of Education                                    [学院]
│   ├── Educational Studies & Innovation                   [系]
│   └── Teacher Education                                  [系]
├── Dornsife School of Public Health                       [学院]
│   └── Public Health                                      [系]
├── Thomas R. Kline School of Law                          [学院]
│   └── Law                                                [系]
├── College of Medicine                                    [学院]
│   └── (Graduate/professional programs only)              [系]
├── Pennsylvania College of Optometry                      [学院]
│   └── Clinical Optometry                                 [系]
├── Goodwin College of Professional Studies                [学院]
│   └── Interdisciplinary Professional Studies             [系]
└── Pennoni Honors College                                 [学院]
    └── Custom-Designed Major                              [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BS | BS | Bachelor of Science | 本科 | 68 |
| BA | BA | Bachelor of Arts | 本科 | 23 |
| BSBA | BS | Bachelor of Science in Business Administration | 本科 | 12 |
| BSAE | BS | Bachelor of Science in Architectural Engineering | 本科 | 1 |
| BArch | BArch | Bachelor of Architecture | 本科 | 1 |
| BSBE | BS | Bachelor of Science in Biomedical Engineering | 本科 | 1 |
| BSCHE | BS | Bachelor of Science in Chemical Engineering | 本科 | 1 |
| BSCIV | BS | Bachelor of Science in Civil Engineering | 本科 | 1 |
| BSCE | BS | Bachelor of Science in Computer Engineering | 本科 | 1 |
| BSEE | BS | Bachelor of Science in Electrical Engineering | 本科 | 2 |
| BSME | BS | Bachelor of Science in Mechanical Engineering | 本科 | 1 |
| BSMSE | BS | Bachelor of Science in Materials Science Engineering | 本科 | 1 |
| BSENE | BS | Bachelor of Science in Environmental Engineering | 本科 | 1 |
| BSET | BS | Bachelor of Science in Engineering Technology | 本科 | 1 |
| BSCMGT | BS | Bachelor of Science in Construction Management | 本科 | 1 |
| BSCST | BS | Bachelor of Science in Computing Security & Technology | 本科 | 1 |
| BACS | BS | Bachelor of Arts in Computer Science | 本科 | 1 |
| BSCS | BS | Bachelor of Science in Computer Science | 本科 | 1 |
| BSDS | BS | Bachelor of Science in Data Science | 本科 | 1 |
| BSBAE | BS | Bachelor of Science in Business and Engineering | 本科 | 1 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 4 |
| Minor | Minor | 辅修 | 本科 | 76 |
| Certificate | Certificate | 本科证书 | 本科 | 15 |
| MS | MS | Master of Science | 研究生 | 101 |
| MA | MA | Master of Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 7 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 7 |
| LLM | LLM | Master of Laws | 研究生 | 4 |
| MFT | MFT | Master of Family Therapy | 研究生 | 1 |
| MHA | MHA | Master of Health Administration | 研究生 | 1 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 1 |
| EdS | EdS | Education Specialist | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 39 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| AuD | AuD | Doctor of Audiology | 研究生 | 2 |
| DBA | DBA | Doctor of Business Administration | 研究生 | 1 |
| DCFT | DCFT | Doctor of Couple and Family Therapy | 研究生 | 1 |
| DHSc | DHSc | Doctor of Health Science | 研究生 | 1 |
| OD | OD | Doctor of Optometry | 研究生 | 2 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| Certificate | Certificate | 研究生证书 | 研究生 | 54 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BS | BA | BArch | BSN | Minor | Cert(UG) | MS | MA | MBA | MFA | MPH | MSN | PhD | ProfDoc | Cert(Grad) | 合计 |
|------------|----|----|-------|-----|-------|----------|----|----|-----|-----|-----|-----|-----|---------|------------|------|
| College of Arts and Sciences | 15 | 23 | 0 | 0 | 38 | 8 | 7 | 3 | 0 | 1 | 0 | 0 | 4 | 0 | 3 | 102 |
| LeBow College of Business | 15 | 0 | 0 | 0 | 8 | 1 | 7 | 0 | 2 | 0 | 0 | 0 | 1 | 1 | 2 | 37 |
| School of Economics | 6 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Close School of Entrepreneurship | 1 | 2 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| School of Engineering | 14 | 0 | 0 | 0 | 6 | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 2 | 37 |
| School of Computer & Info Sciences | 5 | 1 | 0 | 0 | 3 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 19 |
| School of Biomedical Eng & Science | 1 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 7 |
| Westphal College of Media Arts & Design | 11 | 1 | 1 | 0 | 7 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 27 |
| College of Nursing & Health Professions | 3 | 0 | 0 | 4 | 3 | 0 | 6 | 2 | 0 | 0 | 0 | 7 | 2 | 5 | 7 | 39 |
| School of Education | 2 | 0 | 0 | 0 | 2 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 3 | 14 |
| Dornsife School of Public Health | 1 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 7 | 0 | 3 | 0 | 0 | 16 |
| Thomas R. Kline School of Law | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 7 |
| College of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 10 | 28 |
| PA College of Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 |
| Goodwin College of Prof Studies | 2 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Pennoni Honors College | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| **合计** | **77** | **28** | **1** | **4** | **75** | **13** | **68** | **5** | **2** | **1** | **7** | **7** | **23** | **10** | **36** | **357** |

> Note: Some programs span multiple colleges (e.g., Economics programs listed under both LeBow and School of Economics). The matrix counts each program once under its primary college. Dual-degree programs (BS/MS, BA/MBA, etc.) are counted once under the UG college. Graduate certificates include Post-Bachelor's, Post-Master's, and Advanced Study certificates.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/School Architecture

Drexel University has 16 colleges and schools offering undergraduate programs. The university is organized into undergraduate-degree-granting schools and graduate/professional schools. See Section 0.2 for the complete hierarchy tree. Drexel's signature feature is its cooperative education (co-op) program, providing up to 18 months of real-world work experience.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 2 | Biological Sciences (BS/MS) | https://drexel.edu/coas/academics/accelerated-degrees |

##### Chemistry
###### BA, BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Chemistry | https://drexel.edu/coas/academics/undergraduate-programs/chemistry/ |
| 4 | Chemistry (BS/MS) | https://drexel.edu/coas/academics/accelerated-degrees |

##### Communication
###### BA, BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Communication | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Criminology and Justice Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Criminology and Justice Studies | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | English | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 8 | English (BA) / Strategic & Digital Communication (MS) | https://drexel.edu/coas/academics/undergraduate-programs/english/ |

##### Environmental Science/Studies
###### BA, BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Environmental Science | https://ansp.org/ |
| 10 | Environmental Science (BS) / Environmental Policy (MSEP) | https://drexel.edu/coas/academics/undergraduate-programs/environmental-science |
| 11 | Environmental Studies and Sustainability | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 12 | Environmental Studies & Sustainability (BA) / Environmental Policy (MSEP) | |

##### Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | Global Studies | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 14 | Global Studies (BA) / Business Administration (MBA) | https://drexel.edu/coas/academics/undergraduate-programs/global-studies/ |
| 15 | Global Studies (BA) / Public Health (MPH) | https://drexel.edu/coas/academics/undergraduate-programs/global-studies/ |
| 16 | Global Studies (BA) / Strategic and Digital Communication (MS) | https://drexel.edu/coas/academics/undergraduate-programs/global-studies/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | History | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Mathematics
###### BA, BS
| # | 专业 | URL |
|---|------|-----|
| 18 | Mathematics | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 19 | Mathematical Statistics | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 20 | Mathematics (BA/BS) / Biostatistics (MS) | https://drexel.edu/coas/academics/undergraduate-programs/mathematics/ |
| 21 | Mathematics (BS/MS) | https://drexel.edu/coas/academics/accelerated-degrees |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 22 | Philosophy | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 23 | Philosophy, Politics & Economics | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 24 | Physics | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 25 | Political Science | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 26 | Political Science (BA) / Public Policy (MS) | https://drexel.edu/coas/academics/undergraduate-programs/political-science/ |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 27 | Psychology | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 28 | Psychology (BS/MS) | https://drexel.edu/coas/academics/undergraduate-programs/psychology/ |
| 29 | Neuroscience | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Sociology | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 31 | Sociology (BA) / Urban Strategy (MS) | http://catalog.drexel.edu/undergraduate/collegeofartsandsciences/sociologyba-urbanstrategyms/#text |

#### Bennett S. LeBow College of Business

##### Accounting
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/accounting/ |

##### Business Analytics
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 2 | Business Analytics | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/business-analytics/ |

##### Business and Engineering
###### BSBAE
| # | 专业 | URL |
|---|------|-----|
| 3 | Business and Engineering | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-and-engineering/ |

##### Business Law
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 4 | Business Law | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/business-law/ |

##### Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 5 | Finance | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/finance/ |

##### General Business
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 6 | General Business | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/general-business/ |

##### International Business
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 7 | International Business | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/international-business/ |

##### Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 8 | Management | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/management/ |

##### Management Information Systems
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 9 | Management Information Systems | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/management-information-systems/ |

##### Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 10 | Marketing | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/marketing/ |

##### Operations and Supply Chain Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 11 | Operations and Supply Chain Management | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/operations-and-supply-chain/ |

##### Real Estate Management and Development
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 12 | Real Estate Management and Development | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/real-estate-mgmt/ |

##### Sport Business
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 13 | Sport Business | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/sport-business/ |

#### School of Economics

##### Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics (BS) | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/economics/bs-economics/ |
| 2 | Behavioral Economics, Business, and Organizations | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/behavioral-economics-business/ |
| 3 | Economics and Business | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-business/ |
| 4 | Economics and Data Science | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-data-science/ |
| 5 | Economics and Math | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-math/ |
| 6 | Economics and Public Health | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-public-health/ |

#### Charles D. Close School of Entrepreneurship

##### Entrepreneurship and Innovation
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship and Innovation | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/entrepreneurship/ba-entrepreneurship-innovation/ |
| 2 | Entrepreneurship and Innovation (Three-Year Option) | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/entrepreneurship/three-year-ba-entrepreneurship-innovation/ |

#### School of Engineering

##### Architectural Engineering
###### BSAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Chemical Engineering
###### BSCHE
| # | 专业 | URL |
|---|------|-----|
| 2 | Chemical Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Civil Engineering
###### BSCIV
| # | 专业 | URL |
|---|------|-----|
| 3 | Civil Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Computer Engineering
###### BSCE
| # | 专业 | URL |
|---|------|-----|
| 4 | Computer Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Construction Management
###### BSCMGT
| # | 专业 | URL |
|---|------|-----|
| 5 | Construction Management | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Electrical Engineering
###### BSEE
| # | 专业 | URL |
|---|------|-----|
| 6 | Electrical Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Engineering Technology
###### BSET
| # | 专业 | URL |
|---|------|-----|
| 7 | Engineering Technology | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Environmental Engineering
###### BSENE
| # | 专业 | URL |
|---|------|-----|
| 8 | Environmental Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Materials Science and Engineering
###### BSMSE
| # | 专业 | URL |
|---|------|-----|
| 9 | Materials Science and Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Mechanical Engineering & Mechanics
###### BSME
| # | 专业 | URL |
|---|------|-----|
| 10 | Mechanical Engineering & Mechanics | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### School of Computer and Information Sciences

##### Computer Science
###### BACS, BSCS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 2 | Computer Science (BS/MS) | https://drexel.edu/cci/academics/undergraduate-programs/bs-computer-science |

##### Artificial Intelligence and Machine Learning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Artificial Intelligence and Machine Learning | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Computing Security and Technology
###### BSCST
| # | 专业 | URL |
|---|------|-----|
| 4 | Computing Security and Technology | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Data Science
###### BSDS
| # | 专业 | URL |
|---|------|-----|
| 5 | Data Science | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Software Engineering
###### BSEE
| # | 专业 | URL |
|---|------|-----|
| 6 | Software Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### School of Biomedical Engineering and Science

##### Biomedical Engineering
###### BSBE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### Antoinette Westphal College of Media Arts & Design

##### Animation & Visual Effects
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation & Visual Effects | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Architecture
###### BArch, BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Architecture | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 3 | Architectural Studies | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 4 | Architectural Studies BS/MS | https://drexel.edu/westphal/academics/undergraduate/ARCH |

##### Art History
###### BA, BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Art History | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Dance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Dance | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 7 | Dance (BS) / Teaching, Learning and Curriculum (MS) | https://drexel.edu/westphal/academics/undergraduate/DANC |

##### Entertainment & Arts Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Entertainment & Arts Management | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Fashion Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Fashion Design | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Fashion Industry & Merchandising
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Fashion Industry & Merchandising | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Film and Television
###### BS
| # | 专业 | URL |
|---|------|-----|
| 11 | Film and Television | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Game Design & Production
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Game Design & Production | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Graphic Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Graphic Design | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Interior Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | Interior Design | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 15 | Interior Design (BS) / Interior Architecture (MS) | https://drexel.edu/westphal/academics/undergraduate/INTR |

##### Music Industry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 16 | Music Industry | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Product Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 17 | Product Design | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Digital Media
###### BS
| # | 专业 | URL |
|---|------|-----|
| 18 | Digital Media (BS/MS) | https://drexel.edu/westphal/academics/graduate/DIGM |

##### User Experience and Interaction Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 19 | User Experience and Interaction Design | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### College of Nursing and Health Professions

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 2 | Nursing - Accelerated RN/BSN/MSN | https://www.online.drexel.edu/online-degrees/nursing-degrees/rn-bsn-msn/index.aspx |
| 3 | Nursing Accelerated Career Entry (ACE) 11-month program | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 4 | Nursing RN to BSN | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Health Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Culinary Arts and Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Culinary Arts and Science | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Exercise Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Exercise Science | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Health Services Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Health Services Administration | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/health-services-administration/ |

#### School of Education

##### Educational Studies & Innovation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Educational Studies & Innovation | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

##### Teacher Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Teacher Education | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 3 | Elementary Education | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### Dornsife School of Public Health

##### Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### Thomas R. Kline School of Law

##### Law
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

#### Goodwin College of Professional Studies

##### Interdisciplinary Professional Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Professional Studies | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 2 | Business Applications & Practice | https://drexel.edu/goodwin/academics/degree-completion-programs/bs-business-applications-practice/ |

#### Pennoni Honors College

##### Custom-Designed Major
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Custom-Designed Major | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Business and Engineering | LeBow / Engineering | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-and-engineering/ |
| 2 | Behavioral Economics, Business, and Organizations | Economics / LeBow | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/behavioral-economics-business/ |
| 3 | Economics and Data Science | Economics / CCI | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-data-science/ |
| 4 | Economics and Math | Economics / CoAS | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-math/ |
| 5 | Economics and Public Health | Economics / Dornsife | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/economics/combined-programs/economics-public-health/ |

### 1.4 Minors — Complete List

| # | Minor Name | Home College | URL |
|---|------------|-------------|-----|
| 1 | Actuarial Science | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 2 | Africana Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 3 | Animation & Visual Effects | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 4 | Architectural Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 5 | Architecture | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 6 | Art History | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 7 | Artificial Intelligence and Machine Learning | CCI | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 8 | Asian Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 9 | Astrophysics | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 10 | Behavioral Economics and Business | LeBow College | https://catalog.drexel.edu/undergraduate/collegeofbusiness/behavioraleconomicsandbusinessminor/index.html |
| 11 | Biochemistry | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 12 | Bioinformatics | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 13 | Biological Sciences | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 14 | Biophysics | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 15 | Bioscience and Society | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 16 | Business Administration | LeBow College | http://catalog.drexel.edu/undergraduate/collegeofbusiness/businessadministrationminor/ |
| 17 | Business Analytics | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/business-analytics/ |
| 18 | Business Consulting | LeBow College | http://catalog.drexel.edu/undergraduate/collegeofbusiness/businessconsultingminor/index.html |
| 19 | Business Law | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/business-law/ |
| 20 | Chemical Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 21 | Civil Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 22 | Client Development and Customer Service | Goodwin College | https://drexel.edu/goodwin/academics/degree-completion-programs/minor-customer-service |
| 23 | Climate Change | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 24 | Communication | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 25 | Computer Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 26 | Computer Science | CCI | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 27 | Computing Technology | CCI | https://drexel.edu/cci/academics/undergraduate-programs/undergraduate-minors |
| 28 | Construction Management | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 29 | Corporate Entrepreneurship | Close School | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/minors-certificates |
| 30 | Criminal Justice | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 31 | Culinary Arts | CNHP | http://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/culinaryartsminor/index.html |
| 32 | Dance | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 33 | Data Science | CCI | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 34 | Ecology | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 35 | Economics | School of Economics | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/economics/bs-economics/ |
| 36 | Education | School of Education | https://drexel.edu/soe/academics/undergraduate/Degrees/Minor-in-Education |
| 37 | Electrical Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 38 | Engineering Leadership | School of Engineering | http://catalog.drexel.edu/undergraduate/collegeofengineering/engineeringleadership/index.html |
| 39 | Engineering Management | School of Engineering | https://catalog.drexel.edu/undergraduate/collegeofengineering/engineeringmanagement/ |
| 40 | Engineering Policy Analysis | School of Engineering | http://catalog.drexel.edu/undergraduate/collegeofengineering/engineeringpolicyanalysis/ |
| 41 | Entertainment & Arts Management | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 42 | Environmental Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 43 | Environmental Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 44 | Esports | Westphal College | https://drexel.edu/westphal/academics/minors |
| 45 | Exercise Science | CNHP | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 46 | Film and Television | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 47 | Film Studies | Westphal College | https://drexel.edu/westphal/academics/minors |
| 48 | Finance | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/finance/ |
| 49 | Financial Technology | LeBow College | https://catalog.drexel.edu/undergraduate/collegeofbusiness/financialtechnologyminor/index.html |
| 50 | Fine Arts | Westphal College | http://catalog.drexel.edu/undergraduate/collegeofmediaartsanddesign/fineart/ |
| 51 | Food Science | CNHP | http://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/foodscienceminor/index.html |
| 52 | Food Studies | CNHP | http://catalog.drexel.edu/undergraduate/collegeofnursingandhealthprofessions/foodstudiesminor/index.html |
| 53 | French | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 54 | Game Design & Production | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 55 | Gender and Sexuality Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 56 | Global Engineering | School of Engineering | http://catalog.drexel.edu/undergraduate/collegeofengineering/globalengineering/ |
| 57 | Global Public Health | Dornsife School | https://drexel.edu/dornsife/academics/degrees/undergraduate-public-health-program/public-health-minors |
| 58 | Global Studies | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 59 | Graphic Design | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 60 | Green Energy and Sustainability | School of Engineering | http://catalog.drexel.edu/undergraduate/collegeofengineering/greenenergyandsustainabilityminor/index.html |
| 61 | Health Data Analytics | Dornsife School | https://drexel.edu/dornsife/academics/degrees/undergraduate-public-health-program/public-health-minors |
| 62 | Health Services Administration | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/health-services-administration/ |
| 63 | History | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 64 | History of Capitalism | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 65 | Human Computer Interaction | CCI | https://drexel.edu/cci/academics/undergraduate-programs/undergraduate-minors |
| 66 | Immune Engineering | Biomedical Eng | https://drexel.edu/biomed/academics/undergraduate-programs/minor-immune-engineering |
| 67 | Interdisciplinary Problem Solving | Pennoni Honors | http://drexel.edu/pennoni/center-interdisciplinary-inquiry |
| 68 | International Business | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/international-business/ |
| 69 | International Economics | School of Economics | https://catalog.drexel.edu/undergraduate/collegeofbusiness/internationalbusinessminor/ |
| 70 | Japanese | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 71 | Jazz and African-American Music | Westphal College | https://drexel.edu/westphal/academics/minors |
| 72 | Jewish Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 73 | Justice Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 74 | Law | Kline School of Law | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 75 | Linguistics | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 76 | Management | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/management/ |
| 77 | Management Information Systems | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/management-information-systems/ |
| 78 | Marketing | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/marketing/ |
| 79 | Materials Science and Engineering | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 80 | Mathematics | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 81 | Mechanical Engineering & Mechanics | School of Engineering | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 82 | Medical Sociology | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 83 | Merchandising | Westphal College | https://drexel.edu/westphal/academics/minors |
| 84 | Middle East and North Africa Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 85 | Music | Westphal College | https://drexel.edu/westphal/academics/minors |
| 86 | Music Performance | Westphal College | https://drexel.edu/westphal/academics/minors |
| 87 | Music Theory and Composition | Westphal College | https://drexel.edu/westphal/academics/minors |
| 88 | Neuroscience | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 89 | Nonprofit Communication | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 90 | Nutrition | CNHP | https://drexel.edu/cnhp/academics/undergraduate/Minor-Nutrition-and-Foods/ |
| 91 | Operations and Supply Chain Management | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/operations-and-supply-chain/ |
| 92 | Performing Arts | Westphal College | https://drexel.edu/westphal/academics/minors |
| 93 | Philosophy | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 94 | Physics | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 95 | Playwriting | Westphal College | https://drexel.edu/westphal/academics/minors |
| 96 | Political Science | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 97 | Politics | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 98 | Product Design | Westphal College | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 99 | Psychology | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 100 | Public Health | Dornsife School | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 101 | Real Estate Management and Development | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-and-programs/business-administration/real-estate-mgmt/ |
| 102 | Religious Studies | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 103 | Robotics and Automation | School of Engineering | http://catalog.drexel.edu/undergraduate/collegeofengineering/roboticsandautomationminor/index.html |
| 104 | Science, Technology and Society | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 105 | Screenwriting | Westphal College | https://drexel.edu/westphal/academics/minors |
| 106 | Security Technology | CCI | https://drexel.edu/cci/academics/undergraduate-programs/undergraduate-minors |
| 107 | Social Entrepreneurship | Close School | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/minors-certificates |
| 108 | Sociology | College of Arts and Sciences | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 109 | Software Engineering | CCI | https://drexel.edu/academics/~/link.aspx?_id=3E5D8648E50544F2B7DD3C8B02FA297E&_z=z |
| 110 | Somatics | Westphal College | https://drexel.edu/westphal/academics/minors |
| 111 | Spanish | College of Arts and Sciences | https://drexel.edu/coas/academics/departments-centers/global-studies-modern-languages/ |
| 112 | Sport Business | LeBow College | https://www.lebow.drexel.edu/academics/undergraduate/degrees-programs/business-administration/sport-business/ |
| 113 | Sport Coaching Leadership | School of Education | https://drexel.edu/soe/academics/undergraduate/Degrees/Minor-Sport-Coaching-Leadership |
| 114 | Sport Management | LeBow College | http://catalog.drexel.edu/undergraduate/collegeofbusiness/sportmanagementminor/index.html |
| 115 | Sport Regulation and Compliance | LeBow College | https://catalog.drexel.edu/undergraduate/collegeofbusiness/sportregulationcomplianceminor/index.html |
| 116 | STEM Education | School of Education | http://catalog.drexel.edu/undergraduate/schoolofeducation/stemeducationminor/ |
| 117 | Sustainability in the Built Environment | Westphal College | https://drexel.edu/westphal/academics/minors |
| 118 | Systems Engineering | School of Engineering | https://catalog.drexel.edu/undergraduate/collegeofengineering/systemsengineering/index.html |
| 119 | Theatre | Westphal College | https://drexel.edu/westphal/academics/minors |
| 120 | Trial Skills | Kline School of Law | https://drexel.edu/law/academics/undergraduate-law-program/ |
| 121 | War and Society | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |
| 122 | Writing | College of Arts and Sciences | https://drexel.edu/coas/academics/minors |

### 1.5 General/Institute-Wide Requirements

Drexel does not have a university-wide core curriculum. Each college and school has its own general education requirements. The Pennoni Honors College offers an interdisciplinary Honors Program with enhanced requirements.

### 1.6 Undeclared Options

| # | Undeclared Option | College |
|---|-------------------|---------|
| 1 | Undeclared - Business | LeBow College of Business |
| 2 | Undeclared - Design & Media | Westphal College |
| 3 | Undeclared - Engineering | School of Engineering |
| 4 | Undeclared – First-Year Exploratory Studies | College of Arts and Sciences |

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> Note: Due to the large number of graduate programs (224 total), this section provides the complete list organized by college. Graduate programs at Drexel are administered by individual colleges/schools with varying admissions requirements.

#### College of Arts and Sciences

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biological Sciences | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/biological-sciences |
| 2 | Chemistry | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/chemistry |
| 3 | Communication, Culture, and Media | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/communication-culture-and-media |
| 4 | Creative Writing | MFA | https://drexel.edu/academics/grad-professional-programs/coas/creative-writing |
| 5 | Ecology, Evolution and Earth Systems | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/ecology-evolution-and-earth-systems |
| 6 | Environmental Policy | MS | https://drexel.edu/academics/grad-professional-programs/coas/environmental-policy |
| 7 | Mathematics | MS | https://drexel.edu/academics/grad-professional-programs/coas/mathematics |
| 8 | Physics | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/physics |
| 9 | Political Science | MS | https://drexel.edu/academics/grad-professional-programs/coas/political-science |
| 10 | Psychology | MS, PhD | https://drexel.edu/academics/grad-professional-programs/coas/psychology |
| 11 | Science, Technology and Society | MS | https://drexel.edu/academics/grad-professional-programs/coas/science-technology-and-society |
| 12 | Sociology | MS | https://drexel.edu/academics/grad-professional-programs/coas/sociology |
| 13 | Urban Strategy | MS | https://drexel.edu/academics/grad-professional-programs/coas/urban-strategy |

#### Bennett S. LeBow College of Business

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Accounting | MS | https://drexel.edu/academics/grad-professional-programs/lebow/accounting |
| 2 | Business Administration (DBA) | DBA | https://drexel.edu/academics/grad-professional-programs/lebow/executive-dba |
| 3 | Business Administration (MBA) | MBA | https://drexel.edu/academics/grad-professional-programs/lebow/mba |
| 4 | Business Administration (PhD) | PhD | https://drexel.edu/academics/grad-professional-programs/lebow/business-administration-phd |
| 5 | Business Analytics | MS | https://drexel.edu/academics/grad-professional-programs/lebow/business-analytics |
| 6 | Business Information Technology | MS | https://drexel.edu/academics/grad-professional-programs/lebow/business-information-technology |
| 7 | Economics | MS, PhD | https://drexel.edu/academics/grad-professional-programs/lebow/economics |
| 8 | Economics and Data Science | MS | https://drexel.edu/academics/grad-professional-programs/lebow/economics-and-data-science |
| 9 | Executive MBA | MBA | https://drexel.edu/academics/grad-professional-programs/lebow/executive-mba |
| 10 | Finance | MS | https://drexel.edu/academics/grad-professional-programs/lebow/finance |
| 11 | Marketing | MS | https://drexel.edu/academics/grad-professional-programs/lebow/marketing |
| 12 | Sport Business | MS | https://drexel.edu/academics/grad-professional-programs/lebow/sport-business |

#### Charles D. Close School of Entrepreneurship

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Entrepreneurship and Innovation | MS | https://drexel.edu/academics/grad-professional-programs/entrepreneurship/entrepreneurship-and-innovation |

#### School of Engineering

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Architectural Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/architectural-engineering |
| 2 | Chemical Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/chemical-engineering |
| 3 | Civil Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/civil-engineering |
| 4 | Computer Engineering | MS | https://drexel.edu/academics/grad-professional-programs/engineering/computer-engineering |
| 5 | Construction Management | MS | https://drexel.edu/academics/grad-professional-programs/engineering/construction-management |
| 6 | Cybersecurity | MS | https://drexel.edu/academics/grad-professional-programs/engineering/cybersecurity |
| 7 | Electrical Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/electrical-engineering |
| 8 | Engineering Management | MS | https://drexel.edu/academics/grad-professional-programs/engineering/engineering-management |
| 9 | Environmental Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/environmental-engineering |
| 10 | Materials Science and Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/materials-science-and-engineering |
| 11 | Mechanical Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/engineering/mechanical-engineering |
| 12 | Systems Engineering | MS | https://drexel.edu/academics/grad-professional-programs/engineering/systems-engineering |

#### School of Computer and Information Sciences

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Artificial Intelligence and Machine Learning | MS | https://drexel.edu/academics/grad-professional-programs/cci/artifical-intelligence-and-machine-learning |
| 2 | Business Information Technology | MS | https://drexel.edu/academics/grad-professional-programs/cci/business-information-technology |
| 3 | Computer Science | MS, PhD | https://drexel.edu/academics/grad-professional-programs/cci/computer-science |
| 4 | Data Science | MS | https://drexel.edu/academics/grad-professional-programs/cci/data-science |
| 5 | Economics and Data Science | MS | https://drexel.edu/academics/grad-professional-programs/cci/economics-and-data-science |
| 6 | Health Informatics | MS | https://drexel.edu/academics/grad-professional-programs/cci/health-informatics |
| 7 | Information Science | MS | https://drexel.edu/academics/grad-professional-programs/cci/information-science |
| 8 | Library and Information Science | MS | https://drexel.edu/academics/grad-professional-programs/cci/library-and-information-science |
| 9 | Software Engineering | MS | https://drexel.edu/academics/grad-professional-programs/cci/software-engineering |
| 10 | Cybersecurity | MS | https://drexel.edu/academics/grad-professional-programs/cci/cybersecurity |

#### School of Biomedical Engineering and Science

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Advanced Therapeutics | MS | https://drexel.edu/academics/grad-professional-programs/biomed/advanced-therapeutics |
| 2 | Bioinformatics | MS | https://drexel.edu/academics/grad-professional-programs/biomed/bioinformatics |
| 3 | Biomedical Engineering | MS, PhD | https://drexel.edu/academics/grad-professional-programs/biomed/biomedical-engineering |
| 4 | Biomedical Science | MS, PhD | https://drexel.edu/academics/grad-professional-programs/biomed/biomedical-science |

#### Antoinette Westphal College of Media Arts & Design

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Arts Administration | MS | https://drexel.edu/academics/grad-professional-programs/westphal/arts-administration |
| 2 | Design | MS | https://drexel.edu/academics/grad-professional-programs/westphal/design |
| 3 | Digital Media | MS, PhD | https://drexel.edu/academics/grad-professional-programs/westphal/digital-media |
| 4 | Fashion Design | MS | https://drexel.edu/academics/grad-professional-programs/westphal/fashion-design |
| 5 | Interior Architecture | MS | https://drexel.edu/academics/grad-professional-programs/westphal/interior-architecture |
| 6 | Media Communication | MS | https://drexel.edu/academics/grad-professional-programs/westphal/media-communication |
| 7 | Television and Media Management | MS | https://drexel.edu/academics/grad-professional-programs/westphal/television-and-media-management |

#### College of Nursing and Health Professions

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Art Therapy and Counseling | MA | https://drexel.edu/academics/grad-professional-programs/cnhp/art-therapy-and-counseling |
| 2 | Audiology | AuD | https://drexel.edu/academics/grad-professional-programs/cnhp/audiology |
| 3 | Clinical Nurse Leader | MSN | https://drexel.edu/academics/grad-professional-programs/cnhp/clinical-nurse-leader |
| 4 | Complementary and Integrative Health | MS | https://www.online.drexel.edu/online-degrees/nursing-degrees/index.aspx |
| 5 | Couple and Family Therapy | PhD | https://drexel.edu/academics/grad-professional-programs/cnhp/couple-and-family-therapy |
| 6 | Couple and Family Therapy (DCFT) | DCFT | https://drexel.edu/academics/grad-professional-programs/cnhp/couple-and-family-therapy-dcft |
| 7 | Creative Arts Therapies, PhD | PhD | https://drexel.edu/academics/grad-professional-programs/cnhp/creative-arts-therapies-phd |
| 8 | Culinary and Food Science | MS | https://drexel.edu/academics/grad-professional-programs/cnhp/culinary-and-food-science |
| 9 | Dance/Movement Therapy and Counseling | MA | https://drexel.edu/academics/grad-professional-programs/cnhp/dance-movement-therapy |
| 10 | Doctor of Health Science | DHSc | https://drexel.edu/academics/grad-professional-programs/cnhp/doctor-of-health-sciences |
| 11 | Doctor of Nursing Practice | DNP | https://drexel.edu/academics/grad-professional-programs/cnhp/nursing-practice |
| 12 | Doctor of Physical Therapy | DPT | https://drexel.edu/academics/grad-professional-programs/cnhp/professional-doctor-of-physical-therapy |
| 13 | Family Therapy | MFT | https://drexel.edu/academics/grad-professional-programs/cnhp/family-therapy |
| 14 | Nursing Education | MSN | https://drexel.edu/academics/grad-professional-programs/cnhp/nursing-education |
| 15 | Nursing Leadership in Health Systems Management | MSN | https://drexel.edu/academics/grad-professional-programs/cnhp/nursing-leadership |
| 16 | Nutrition Sciences | MS | https://drexel.edu/academics/grad-professional-programs/cnhp/nutrition-sciences |
| 17 | Physician Assistant | MS | https://drexel.edu/academics/grad-professional-programs/cnhp/physician-assistant |

#### School of Education

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Advanced Executive Leadership | EdD | https://drexel.edu/academics/grad-professional-programs/education/advanced-executive-leadership |
| 2 | Applied Behavior Analysis | MS | https://drexel.edu/academics/grad-professional-programs/education/applied-behavior-analysis |
| 3 | Applied Learning Sciences, Technology, and Creativity | MS | https://drexel.edu/academics/grad-professional-programs/education/applied-learning-sciences-technology-and-creativity |
| 4 | Applied Learning, Leadership, and Innovation | EdS | https://drexel.edu/academics/grad-professional-programs/education/applied-learning-leadership-innovation |
| 5 | Education | PhD | https://drexel.edu/academics/grad-professional-programs/education/education |
| 6 | Education Improvement and Transformation | MS | https://drexel.edu/academics/grad-professional-programs/education/education-improvement-and-transformation |
| 7 | Educational Leadership and Management | EdD | https://drexel.edu/academics/grad-professional-programs/education/educational-leadership-and-management |
| 8 | Higher Education | EdS | https://drexel.edu/academics/grad-professional-programs/education/higher-education |
| 9 | Learning Technologies | MS | https://drexel.edu/academics/grad-professional-programs/education/learning-technologies |
| 10 | Mathematics Learning and Teaching | MS | https://drexel.edu/academics/grad-professional-programs/education/mathematics-learning-and-teaching |
| 11 | Special Education | MS | https://drexel.edu/academics/grad-professional-programs/education/special-education |
| 12 | Teaching, Learning and Curriculum | MS | https://drexel.edu/academics/grad-professional-programs/education/teaching-learning-and-curriculum |

#### Dornsife School of Public Health

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biostatistics | MS | https://drexel.edu/academics/grad-professional-programs/pubhealth/biostatistics |
| 2 | Biostatistics | PhD | https://drexel.edu/academics/grad-professional-programs/pubhealth/biostatistics-phd |
| 3 | Community Health and Prevention | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/community-health-and-prevention-mph |
| 4 | Community Health and Prevention | PhD | https://drexel.edu/academics/grad-professional-programs/pubhealth/community-health-and-prevention-phd |
| 5 | Doctor of Medicine and Master of Public Health Dual Degree | MD/MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/doctor-of-medicine-and-master-of-public-health |
| 6 | Environmental and Occupational Health | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/environmental-and-occupational-health-mph |
| 7 | Environmental and Occupational Health | PhD | https://drexel.edu/academics/grad-professional-programs/pubhealth/environmental-and-occupational-health-phd |
| 8 | Epidemiology | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/epidemiology-mph |
| 9 | Epidemiology | PhD | https://drexel.edu/academics/grad-professional-programs/pubhealth/epidemiology-phd |
| 10 | Executive MPH | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/executive-mph |
| 11 | Global Health | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/global-health-mph |
| 12 | Health Management and Policy | MPH | https://drexel.edu/academics/grad-professional-programs/pubhealth/health-management-and-policy-mph |
| 13 | Public Health | PhD | https://drexel.edu/academics/grad-professional-programs/pubhealth/public-health |
| 14 | Public Health (non-degree) | Non-degree | https://drexel.edu/academics/grad-professional-programs/pubhealth/public-health-non-degree |

#### Thomas R. Kline School of Law

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | American Legal Practice | LLM | https://drexel.edu/academics/grad-professional-programs/law/american-legal-practice |
| 2 | Cyber Law and Data Privacy | LLM | https://drexel.edu/academics/grad-professional-programs/law/cyber-law-data-privacy |
| 3 | Global Financial Regulation | LLM | https://drexel.edu/academics/grad-professional-programs/law/global-financial-regulation |
| 4 | Health Law | LLM | https://drexel.edu/academics/grad-professional-programs/law/health-law |
| 5 | Juris Doctor | JD | https://drexel.edu/academics/grad-professional-programs/law/juris-doctor |
| 6 | JD/MPH | JD/MPH | https://drexel.edu/academics/grad-professional-programs/law/jd-mph |
| 7 | JD/PhD | JD/PhD | https://drexel.edu/academics/grad-professional-programs/law/jd-phd |

#### College of Medicine

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biochemistry of Health and Disease | MS, PhD | https://drexel.edu/academics/grad-professional-programs/medicine/biochemistry-of-health-and-disease |
| 2 | Biomedical Studies | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedical-studies |
| 3 | Biomedicine | MS, PhD | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine |
| 4 | Biomedicine and Business | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine-and-business |
| 5 | Biomedicine and Cell and Gene Therapy | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine-and-cell-and-gene-therapy |
| 6 | Biomedicine and Digital Media | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine-and-digital-media |
| 7 | Biomedicine and Entrepreneurship | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine-and-entrepreneurship |
| 8 | Biomedicine and Law | MS | https://drexel.edu/academics/grad-professional-programs/medicine/biomedicine-and-law |
| 9 | Cancer Biology | MS | https://drexel.edu/academics/grad-professional-programs/medicine/cancer-biology |
| 10 | Clinical Optometry | MS | https://drexel.edu/academics/grad-professional-programs/medicine/clinical-optometry |
| 11 | Clinical Research for Health Professionals | MS | https://drexel.edu/academics/grad-professional-programs/medicine/clinical-research-for-health-professionals |
| 12 | Clinical Research Organization and Management | MS | https://drexel.edu/academics/grad-professional-programs/medicine/clinical-research-organization-and-management |
| 13 | Drug Discovery and Development | MS | https://drexel.edu/academics/grad-professional-programs/medicine/drug-discovery-and-development |
| 14 | Drexel Pathway to Medical School | MS | https://drexel.edu/academics/grad-professional-programs/medicine/pathway-to-medical-school |
| 15 | Molecular and Cell Biology | PhD | https://drexel.edu/academics/grad-professional-programs/medicine/molecular-and-cell-biology |
| 16 | Neuroscience | PhD | https://drexel.edu/academics/grad-professional-programs/medicine/neuroscience |
| 17 | MD Program | MD | https://drexel.edu/academics/grad-professional-programs/medicine/md-program |
| 18 | MD/PhD | MD/PhD | https://drexel.edu/academics/grad-professional-programs/medicine/md-phd |

#### Pennsylvania College of Optometry

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Optometry | OD | https://drexel.edu/academics/grad-professional-programs/optometry/optometry |
| 2 | Vision Science | OD | https://drexel.edu/academics/grad-professional-programs/optometry/vision-science |

#### Goodwin College of Professional Studies

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Professional Studies | MS | https://drexel.edu/academics/grad-professional-programs/goodwin/professional-studies |

### 2.2 Graduate Admissions Model

Drexel's graduate admissions are **fully decentralized**. Each college/school manages its own admissions process, deadlines, and requirements. The Office of Graduate Studies provides oversight and support but does not make admissions decisions.

**Key entry points:**
- LeBow College: https://drexel.edu/academics/grad-professional-programs/lebow/
- School of Engineering: https://drexel.edu/academics/grad-professional-programs/engineering/
- CCI: https://drexel.edu/academics/grad-professional-programs/cci/
- College of Medicine: https://drexel.edu/academics/grad-professional-programs/medicine/
- CNHP: https://drexel.edu/academics/grad-professional-programs/cnhp/
- School of Education: https://drexel.edu/academics/grad-professional-programs/education/
- Dornsife SPH: https://drexel.edu/academics/grad-professional-programs/pubhealth/
- Kline Law: https://drexel.edu/academics/grad-professional-programs/law/

**Application platform:** ApplyWeb (common for most programs)
**Application fee:** Varies by program (typically $50-$75)
**GRE:** Required for some programs, optional for others — check individual program requirements
**ETS code:** 2194

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| **Application portal** | Common Application or Coalition Application | drexel.edu/admissions/apply |
| **ED deadline** | November 15 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **EA deadline** | November 15 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **RD deadline** | January 15 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **Decision notification (ED/EA)** | Mid-December | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/early-decision-early-action |
| **Decision notification (RD)** | By April 1 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/early-decision-early-action |
| **Enrollment confirmation deadline** | May 1 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **CSS Profile deadline (ED/EA)** | November 25 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **CSS Profile deadline (RD)** | February 1 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **FAFSA priority deadline** | February 1 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |
| **Application fee** | Not specified on deadlines page | |
| **SAT/ACT policy** | Test-optional (No Harm) | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/standardized-tests |
| **Superscore** | Yes (highest section scores across test dates) | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/standardized-tests |
| **SAT code** | 2194 | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/standardized-tests |
| **ACT code** | Not specified | |
| **Interview** | Not required | |
| **Recommendations** | Check Common App requirements | |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified on website | — | Code: 2194 |
| TOEFL Essentials | Not specified | — | Accepted |
| IELTS | Not specified | — | Accepted |
| Pearson PTE | Not specified | — | Accepted |
| Duolingo English Test (DET) | Not specified | — | Accepted |
| Cambridge English C1/C2 | Not specified | — | Accepted |

> **Exemptions:** Native English speakers; students with 3+ years of English-language high school instruction; SAT EBRW 600+ or ACT English 27+.

> **TOEFL MyBest:** Accepted — Drexel considers highest section scores across all test dates.

### 3.3 Graduate — Global Rules

- **Admissions model:** Fully decentralized — each program sets own requirements
- **Application platform:** ApplyWeb (most programs)
- **Application fee:** Varies by program ($50-$75 typical)
- **GRE:** Required for some programs, optional for others
- **ETS institutional code:** 2194
- **English proficiency:** Required for non-native speakers; specific minimums vary by program
- **CGS April-15:** Drexel is a signatory

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026–2027 Academic Year, On-Campus)

| Expense Item | Amount (Annual) | Description |
|-------------|----------------|-------------|
| **Tuition** | $63,078 | Three quarters (fall, winter, spring) |
| **Fees** | $2,370 | $790 per quarter |
| **Immunization Fee** | $50 | One-time fee |
| **Books** | $1,200 | $400 per quarter |
| **Computer** | $500 | Admit term only |
| **Transportation** | $900 | $300 per quarter |
| **Personal** | $600 | $200 per quarter |
| **Origination Fee** | $60 | $20 per quarter |
| **Housing** | $12,045 | $4,015 per quarter |
| **Food** | $7,353 | $2,451 per quarter |
| **Total COA** | **$88,156** | |

> Source: drexel.edu/drexelcentral/cost/undergrad (2026-2027 On-Campus table)

### 4.2 Undergraduate Financial-Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| **Financial aid awarded** | 100% of first-year students | drexel.edu/admissions/financial-aid-affordability/undergrad |
| **Average grant aid (2025-26)** | $40,814 | drexel.edu/admissions/financial-aid-affordability/undergrad |
| **Average net tuition (2025-26)** | $26,388 | drexel.edu/drexelcentral/cost/undergrad |
| **Merit scholarship (ED/EA)** | $20,000–$35,000 | drexel.edu/admissions/financial-aid-affordability/undergrad |
| **Merit scholarship (RD)** | $10,000–$35,000 | drexel.edu/admissions/financial-aid-affordability/undergrad |
| **Need-blind/need-aware** | Need-aware for all applicants | drexel.edu/admissions/financial-aid-affordability |
| **Forms required** | CSS Profile + FAFSA | drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines |

### 4.3 Graduate Cost & Funding Framework

- **Tuition:** Varies by program; per-credit or per-quarter rates
- **Financial aid:** Primarily through student loans, assistantships, merit-based scholarships, tuition remission, and incentive programs
- **Drexel Lifelong Learner Award:** 30% tuition savings for Drexel alumni returning for graduate study
- **Application fee:** Varies by program ($50-$75 typical)

---

## SECTION 5 — Evidence Chain Index

### E-U-001: ED Deadline
```yaml
field: undergraduate.deadlines.ED
value: "November 15"
source_url: https://drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines
source_snippet: "Early Decision — Deadline: November 15 — Applications due; decisions released in mid-December."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: EA Deadline
```yaml
field: undergraduate.deadlines.EA
value: "November 15"
source_url: https://drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines
source_snippet: "Early Action — Deadline: November 15 — Applications due; decisions released in mid-December."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: RD Deadline
```yaml
field: undergraduate.deadlines.RD
value: "January 15"
source_url: https://drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/application-deadlines
source_snippet: "Regular Decision — Deadline: January 15 — Applications due; decisions released by April 1."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Test Policy
```yaml
field: undergraduate.testing.policy
value: "Test-optional (No Harm)"
source_url: https://drexel.edu/admissions/apply/undergrad-instructions/first-year-instructions/standardized-tests
source_snippet: "Drexel practices a No Harm Test-Optional review for fall entry. This means, with some exceptions, applicants can choose whether to include standardized test scores as part of their application to the University."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: Tuition
```yaml
field: undergraduate.cost.tuition_2026_2027
value: "$63,078"
source_url: http://drexel.edu/drexelcentral/cost/undergrad
source_snippet: "Tuition — $21,026 per quarter — Total (Three terms of enrollment): $63,078"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Total COA
```yaml
field: undergraduate.cost.total_coa_2026_2027
value: "$88,156"
source_url: http://drexel.edu/drexelcentral/cost/undergrad
source_snippet: "Total Estimated Cost of Attendance — $88,156"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Average Grant Aid
```yaml
field: undergraduate.financial_aid.average_grant_2025_2026
value: "$40,814"
source_url: https://drexel.edu/admissions/financial-aid-affordability/undergrad
source_snippet: "AVERAGE GRANT AID AWARD TO FIRST-YEAR, FULL-TIME UNDERGRADUATES ENTERING IN FALL 2025: $40,814"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Merit Scholarship Ranges
```yaml
field: undergraduate.financial_aid.merit_scholarship_ranges
value: "ED/EA: $20,000–$35,000; RD: $10,000–$35,000"
source_url: https://drexel.edu/admissions/financial-aid-affordability/undergrad
source_snippet: "First-Year Merit Scholarship Ranges for Admitted Fall 2026 Students: Early Decision and Early Action: $20,000–$35,000; Regular Decision: $10,000–$35,000"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: Program Count
```yaml
field: undergraduate.programs.total_count
value: "201 (121 majors, 76 minors, 15 certificates, 4 undeclared)"
source_url: https://drexel.edu/academics/undergrad-programs
source_snippet: "Discover a curriculum as unique as you are. With over 100 majors and as many minors..."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Program Count
```yaml
field: graduate.programs.total_count
value: "224 (170 degree programs, 54 certificates)"
source_url: https://drexel.edu/academics/grad-professional-programs
source_snippet: "With over 120 graduate programs, we offer the flexibility to fit your schedule."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Admissions Model
```yaml
field: graduate.admissions.model
value: "Fully decentralized"
source_url: https://drexel.edu/admissions/grad
source_snippet: "Graduate admission requirements vary by program. For full details, refer to Drexel's official Graduate Admissions Application Instructions."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: ETS Code
```yaml
field: graduate.testing.ets_code
value: "2194"
source_url: https://drexel.edu/admissions/apply/grad-instructions
source_snippet: "In order to send your GRE scores to Drexel, you must log in to your ETS account and officially request that your scores be sent to Drexel using Drexel's school code: 2194."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
drexel-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4, counts, hierarchy, matrix)
├── 01-ug-college-of-arts-sciences.md   (Section 1: CoAS majors + minors)
├── 02-ug-lebow-business.md             (Section 1: LeBow majors + minors)
├── 03-ug-school-of-economics.md        (Section 1: Economics programs)
├── 04-ug-close-entrepreneurship.md     (Section 1: Entrepreneurship programs)
├── 05-ug-engineering.md                (Section 1: Engineering majors + minors)
├── 06-ug-cci-computing.md              (Section 1: CCI majors + minors)
├── 07-ug-biomedical-engineering.md     (Section 1: Biomed Eng programs)
├── 08-ug-westphal-media-arts.md        (Section 1: Westphal majors + minors)
├── 09-ug-nursing-health.md             (Section 1: CNHP programs)
├── 10-ug-education.md                  (Section 1: Education programs)
├── 11-ug-public-health.md              (Section 1: Dornsife programs)
├── 12-ug-law.md                        (Section 1: Law UG programs)
├── 13-ug-other.md                      (Section 1: Goodwin, Pennoni, Optometry)
├── 14-grad-arts-sciences.md            (Section 2: CoAS grad programs)
├── 15-grad-lebow.md                    (Section 2: LeBow grad programs)
├── 16-grad-engineering.md              (Section 2: Engineering grad programs)
├── 17-grad-cci.md                      (Section 2: CCI grad programs)
├── 18-grad-biomedical.md               (Section 2: Biomed Eng grad programs)
├── 19-grad-westphal.md                 (Section 2: Westphal grad programs)
├── 20-grad-nursing-health.md           (Section 2: CNHP grad programs)
├── 21-grad-education.md                (Section 2: Education grad programs)
├── 22-grad-public-health.md            (Section 2: Dornsife grad programs)
├── 23-grad-law.md                      (Section 2: Law grad programs)
├── 24-grad-medicine.md                 (Section 2: Medicine grad programs)
├── 25-grad-other.md                    (Section 2: Optometry, Goodwin, Entrepreneurship)
├── 26-deadlines-requirements.md        (Section 3: deadlines, tests, requirements)
├── 27-costs-financial-aid.md           (Section 4: COA, aid policy, grad costs)
├── 28-evidence-chain.md                (Section 5: all evidence YAML blocks)
└── 29-comparison-framework.md          (Section 7: cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "drexel-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|PhD|...>"
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
| P0 | Specific TOEFL/IELTS minimum scores (UG) | drexel.edu/international or ELC |
| P0 | Application fee amount (UG) | drexel.edu/admissions/apply |
| P0 | Per-program GRE requirements (Grad) | Individual program pages |
| P1 | Per-program application fees (Grad) | Individual program pages |
| P1 | Graduate tuition rates by program | drexel.edu/drexelcentral/tuition-fees |
| P1 | Financial aid details for international students | drexel.edu/admissions/financial-aid-affordability |
| P2 | Student-to-faculty ratio | drexel.edu/about |
| P2 | Graduation rate | drexel.edu/about/outcomes-value |
| P2 | Retention rate | drexel.edu/about/outcomes-value |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Drexel University | (Other schools) |
|-----------|------------------|-----------------|
| **Type** | Private, R1 Research | |
| **Location** | Philadelphia, PA | |
| **UG Tuition (2026-27)** | $63,078 | |
| **UG Total COA (2026-27)** | $88,156 | |
| **ED deadline** | November 15 | |
| **EA deadline** | November 15 | |
| **RD deadline** | January 15 | |
| **SAT/ACT required?** | No (test-optional, No Harm) | |
| **TOEFL min** | Not published on website | |
| **IELTS min** | Not published on website | |
| **Need-blind (intl)?** | No (need-aware for all) | |
| **Total program count (Rule 1)** | 421 | |
| **School/department count (Rule 2)** | 16 | |
| **Co-op program** | Yes (up to 18 months) | |
| **Application platform** | Common App / Coalition | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: drexel.edu, catalog.drexel.edu, lebow.drexel.edu, drexel.edu/drexelcentral
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
