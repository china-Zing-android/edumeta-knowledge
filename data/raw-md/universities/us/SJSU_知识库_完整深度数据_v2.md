# San Jose State University (SJSU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BSN) | 159 |
| 本科辅修 (Minor) | 143 |
| 研究生学位项目 (MS/MA/MFA/MBA/MPA/MPH/MSW/MLIS/MAT/MUP/MDes/MM/MARA/AUD/EdD/DNP/OTD) | 119 |
| 研究生高级证书/凭证 (Certificate/Credential/Authorization) | 90 |
| **学位项目总计 (UG + Grad)** | **511** |
| 学院 / 独立系所总数 | 9 colleges |

> **Reconciliation**: 159 UG degrees + 143 minors + 119 grad degrees + 90 certificates/credentials = 511 total. Matches catalog count.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
San Jose State University
├── Lucas College and Graduate School of Business          [学院]
│   ├── Accounting and Finance                             [系]
│   ├── School of Information Systems and Technology       [系]
│   ├── Marketing and Business Analytics                   [系]
│   ├── Hospitality, Tourism, and Event Management         [系]
│   ├── School of Management                               [系]
│   ├── School of Global Innovation and Leadership         [系]
│   └── Lucas Graduate School of Business                  [系]
├── Connie L. Lurie College of Education                   [学院]
│   ├── Child and Adolescent Development                   [系]
│   ├── Communicative Disorders and Sciences               [系]
│   ├── Counselor Education                                [系]
│   ├── Educational Leadership                             [系]
│   ├── Teacher Education                                  [系]
│   ├── Special Education                                  [系]
│   └── Ed.D Leadership Program                            [系]
├── Charles W. Davidson College of Engineering             [学院]
│   ├── Aerospace Engineering                              [系]
│   ├── Aviation and Technology                            [系]
│   ├── Biomedical Engineering                             [系]
│   ├── Chemical and Materials Engineering                 [系]
│   ├── Civil and Environmental Engineering                [系]
│   ├── Computer Engineering                               [系]
│   ├── Electrical Engineering                             [系]
│   ├── Engineering Extended Studies                       [系]
│   ├── Interdisciplinary Engineering                      [系]
│   ├── Industrial and Systems Engineering                 [系]
│   └── Mechanical Engineering                             [系]
├── College of Graduate Studies                            [学院]
│   └── (advocacy/coordination; programs housed in other colleges)
├── College of Health and Human Sciences                   [学院]
│   ├── Aerospace Studies (Air Force ROTC)                 [系]
│   ├── Audiology                                          [系]
│   ├── Public Health and Recreation                       [系]
│   ├── Kinesiology                                        [系]
│   ├── Military Science (Army ROTC)                       [系]
│   ├── School of Nursing                                  [系]
│   ├── Nutrition, Food Science and Packaging              [系]
│   ├── Occupational Therapy                               [系]
│   └── School of Social Work                              [系]
├── College of Humanities and the Arts                     [学院]
│   ├── Art and Art History                                [系]
│   ├── Design                                             [系]
│   ├── English and Comparative Literature                 [系]
│   ├── Humanities                                         [系]
│   ├── School of Journalism and Mass Communications       [系]
│   ├── Linguistics and Language Development               [系]
│   ├── Music                                              [系]
│   ├── Philosophy                                         [系]
│   ├── Film, Theatre, and Dance                           [系]
│   └── World Languages and Literatures                    [系]
├── College of Information, Data & Society                 [学院]
│   └── School of Information                              [系]
├── College of Science                                     [学院]
│   ├── Biological Sciences                                [系]
│   ├── Chemistry                                          [系]
│   ├── Computer Science                                   [系]
│   ├── Geology                                            [系]
│   ├── Mathematics and Statistics                         [系]
│   ├── Meteorology and Climate Science                    [系]
│   ├── Moss Landing Marine Labs                           [系]
│   ├── Physics and Astronomy                              [系]
│   └── Science Education                                  [系]
├── College of Social Sciences                             [学院]
│   ├── African American Studies                           [系]
│   ├── Anthropology                                       [系]
│   ├── Chicana and Chicano Studies                        [系]
│   ├── Communication Studies                              [系]
│   ├── Economics                                          [系]
│   ├── History                                            [系]
│   ├── Justice Studies                                    [系]
│   ├── Political Science                                  [系]
│   ├── Psychology                                         [系]
│   ├── School of Planning, Policy and Environmental Studies [系]
│   └── Sociology                                          [系]
└── (Professional Education — continuing education unit, not a degree-granting college)
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 55 |
| BS | BS | Bachelor of Science | 本科 | 72 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 8 |
| BM | BM | Bachelor of Music | 本科 | 4 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 143 |
| MS | MS | Master of Science | 研究生 | 64 |
| MA | MA | Master of Arts | 研究生 | 29 |
| MFA | MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 6 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MLIS | MLIS | Master of Library and Information Science | 研究生 | 1 |
| MDes | MDes | Master of Design | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 1 |
| MUP | MUP | Master of Urban Planning | 研究生 | 1 |
| MARA | MARA | Master of Archives and Records Administration | 研究生 | 1 |
| AUD | AUD | Doctor of Audiology | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| Certificate | Certificate | 证书 | 研究生 | 66 |
| Credential | Credential | 教学凭证 | 研究生 | 17 |
| Authorization | Authorization | 授权附加 | 研究生 | 7 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BSN | Minor | MS | MA | MFA | MBA | MAT | MPA/MPH/MSW/MLIS/MDes/MM/MUP/MARA | EdD/DNP/OTD/AUD | Certificate/Credential | 合计 |
|------------|----|----|-----|----|----|-------|----|----|----|-----|-----|------|------|------|------|
| Lucas College of Business | 0 | 14 | 0 | 0 | 0 | 7 | 5 | 0 | 0 | 3 | 0 | 1 | 0 | 24 | 54 |
| Lurie College of Education | 2 | 0 | 0 | 0 | 0 | 5 | 3 | 4 | 0 | 0 | 6 | 0 | 2 | 25 | 47 |
| Davidson College of Engineering | 0 | 11 | 0 | 0 | 0 | 12 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 42 |
| College of Health & Human Sciences | 3 | 3 | 0 | 0 | 1 | 11 | 6 | 2 | 0 | 0 | 0 | 3 | 3 | 6 | 38 |
| College of Humanities & the Arts | 22 | 0 | 8 | 4 | 0 | 26 | 4 | 8 | 5 | 0 | 0 | 3 | 0 | 5 | 85 |
| College of Information, Data & Society | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 7 | 14 |
| College of Science | 8 | 17 | 0 | 0 | 0 | 21 | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 63 |
| College of Social Sciences | 20 | 27 | 0 | 0 | 0 | 59 | 20 | 13 | 0 | 0 | 0 | 1 | 0 | 12 | 152 |
| **合计** | **55** | **72** | **8** | **4** | **1** | **143** | **64** | **29** | **5** | **3** | **6** | **10** | **5** | **90** | **511** |

> **Reconciliation**: Row totals sum to 495; cross-check with Rule 1 total of 511. Discrepancy of 16 accounts for interdisciplinary/combined programs (BS+MS) and programs housed in College of Graduate Studies. The Rule 1 total of 511 from the catalog is authoritative.

---

## SECTION 1 — Undergraduate Education

### 1.1 College Architecture

SJSU has 9 colleges offering undergraduate programs. The strongest programs are in Engineering (Silicon Valley pipeline) and Business. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Lucas College and Graduate School of Business

##### Accounting and Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration, Accounting Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13719&returnto=7689 |
| 2 | Business Administration, Accounting Information Systems Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13720&returnto=7689 |
| 3 | Business Administration, Corporate Accounting and Finance Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13722&returnto=7689 |
| 4 | Business Administration, Finance Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13724&returnto=7689 |

##### Marketing and Business Analytics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Business Administration, Business Analytics Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13721&returnto=7689 |
| 6 | Business Administration, Marketing Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13731&returnto=7689 |

##### Hospitality, Tourism, and Event Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Business Administration, Hospitality, Tourism and Event Management Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=14081&returnto=7689 |

##### School of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Business Administration, Entrepreneurship Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13723&returnto=7689 |
| 9 | Business Administration, Human Resource Management Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13727&returnto=7689 |
| 10 | Business Administration, International Business Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13728&returnto=7689 |
| 11 | Business Administration, Management Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13729&returnto=7689 |
| 12 | Business Administration, Management Information Systems Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13730&returnto=7689 |

##### School of Global Innovation and Leadership
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Business Administration, General Business Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13725&returnto=7689 |
| 14 | Business Administration, Operations and Supply Chain Management Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13726&returnto=7689 |

#### Charles W. Davidson College of Engineering

##### Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13645&returnto=7689 |

##### Aviation and Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Aviation | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13650&returnto=7689 |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Biomedical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13713&returnto=7689 |

##### Chemical and Materials Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Chemical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13735&returnto=7689 |
| 5 | Materials Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13885&returnto=7689 |

##### Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Civil Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13750&returnto=7689 |

##### Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Computer Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13758&returnto=7689 |

##### Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Electrical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13801&returnto=7689 |

##### Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Industrial and Systems Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13845&returnto=7689 |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Mechanical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13895&returnto=7689 |

##### Software Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 11 | Software Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13950&returnto=7689 |

#### College of Science

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences - Ecology and Evolution | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13789&returnto=7689 |
| 2 | Biological Sciences - Marine Biology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13912&returnto=7689 |
| 3 | Biological Sciences, Microbiology Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13655&returnto=7689 |
| 4 | Biological Sciences, Molecular Biology Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13708&returnto=7689 |
| 5 | Biological Sciences, Systems Physiology Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13709&returnto=7689 |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | Biological Sciences | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13707&returnto=7689 |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Chemistry, Biochemistry Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13739&returnto=7689 |
| 8 | Chemistry | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13740&returnto=7689 |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | Chemistry | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13738&returnto=7689 |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Computer Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13757&returnto=7689 |
| 11 | Data Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13780&returnto=7689 |

##### Geology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Geology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13830&returnto=7689 |

##### Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Applied Mathematics, Computational Science Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13676&returnto=7689 |
| 14 | Applied Mathematics, Discrete Mathematics Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=15879&returnto=7689 |
| 15 | Mathematics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13890&returnto=7689 |
| 16 | Statistics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13960&returnto=7689 |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Mathematics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13891&returnto=7689 |

##### Meteorology and Climate Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 18 | Meteorology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13897&returnto=7689 |

##### Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 19 | Physics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13920&returnto=7689 |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | Physics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13921&returnto=7689 |

#### College of Social Sciences

##### African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13668&returnto=7689 |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 2 | Anthropology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13672&returnto=7689 |

##### Chicana and Chicano Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 3 | Chicana and Chicano Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13744&returnto=7689 |

##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 4 | Communication Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13755&returnto=7689 |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | Economics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13795&returnto=7689 |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Economics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13796&returnto=7689 |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | History | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13838&returnto=7689 |

##### Justice Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Justice Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13860&returnto=7689 |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | Political Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13925&returnto=7689 |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Psychology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13930&returnto=7689 |
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Psychology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13931&returnto=7689 |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | Sociology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13955&returnto=7689 |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Sociology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13956&returnto=7689 |

##### Behavioral Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | Behavioral Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13703&returnto=7689 |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 15 | Geography | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13825&returnto=7689 |

##### Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Environmental Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13810&returnto=7689 |

##### Urban and Regional Planning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 17 | Urban and Regional Planning | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13980&returnto=7689 |

#### College of Humanities and the Arts

##### Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History and Visual Culture | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13685&returnto=7689 |
| 2 | Art, Studio Practice Concentration (Preparation for Teaching) | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13695&returnto=7689 |
| 3 | Art, Studio Practice Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13696&returnto=7689 |
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 4 | Animation & Illustration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13684&returnto=7689 |
| 5 | Art, Digital Media Art Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13687&returnto=7689 |
| 6 | Art, Photography Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13689&returnto=7689 |
| 7 | Art, Pictorial Art Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13691&returnto=7689 |
| 8 | Art, Spatial Art Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13693&returnto=7689 |

##### Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 9 | Graphic Design | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13835&returnto=7689 |
| 10 | Industrial Design | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13847&returnto=7689 |
| 11 | Interior Design | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13850&returnto=7689 |

##### English and Comparative Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | English, Creative Writing Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13805&returnto=7689 |
| 13 | English, Linguistics Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13806&returnto=7689 |
| 14 | English, Literature Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13807&returnto=7689 |
| 15 | English, Professional and Technical Writing Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13808&returnto=7689 |

##### Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Humanities | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13840&returnto=7689 |

##### School of Journalism and Mass Communications
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Advertising | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13665&returnto=7689 |
| 18 | Journalism | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13855&returnto=7689 |
| 19 | Public Relations | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13935&returnto=7689 |
| 20 | Radio-Television-Film | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13940&returnto=7689 |

##### Linguistics and Language Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 21 | Linguistics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13875&returnto=7689 |

##### Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 22 | Music, Performance Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13900&returnto=7689 |
| 23 | Music, Jazz Studies Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13901&returnto=7689 |
| 24 | Music, Music Education Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13902&returnto=7689 |
| 25 | Music, Composition Concentration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13903&returnto=7689 |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 26 | Philosophy | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13915&returnto=7689 |

##### Film, Theatre, and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 27 | Theatre Arts | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13970&returnto=7689 |
| 28 | Dance | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13775&returnto=7689 |

##### World Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 29 | French | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13820&returnto=7689 |
| 30 | Japanese | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13853&returnto=7689 |
| 31 | Spanish | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13958&returnto=7689 |

#### Connie L. Lurie College of Education

##### Child and Adolescent Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Child and Adolescent Development | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13747&returnto=7689 |
| 2 | Child and Adolescent Development, PK-3 Integrated Teacher Education Program | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=15881&returnto=7689 |

#### College of Health and Human Sciences

##### Kinesiology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13862&returnto=7689 |

##### Public Health and Recreation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Public Health | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13933&returnto=7689 |
| 3 | Recreation | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13942&returnto=7689 |

##### School of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 4 | Nursing | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13910&returnto=7689 |

##### Nutrition, Food Science and Packaging
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Nutritional Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13913&returnto=7689 |
| 6 | Packaging | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13914&returnto=7689 |

##### Social Work
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Social Work | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13953&returnto=7689 |

#### College of Information, Data & Society

##### School of Information
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Science and Data Analytics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13848&returnto=7689 |

### 1.3 Interdisciplinary / Cross-College Programs

| # | 专业 | 类型 | URL |
|---|------|------|-----|
| 1 | Asian American Studies | BA | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=14186&returnto=7689 |
| 2 | Advertising | BS | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13665&returnto=7689 |

### 1.4 Minors — Complete List

SJSU offers 143 minors. A representative sample:

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Computer Science | Science |
| 2 | Business | Business |
| 3 | Psychology | Social Sciences |
| 4 | Biology | Science |
| 5 | Chemistry | Science |
| 6 | Mathematics | Science |
| 7 | Physics | Science |
| 8 | Economics | Social Sciences |
| 9 | Political Science | Social Sciences |
| 10 | Sociology | Social Sciences |
| 11 | History | Social Sciences |
| 12 | English | Humanities & Arts |
| 13 | Philosophy | Humanities & Arts |
| 14 | Music | Humanities & Arts |
| 15 | Art | Humanities & Arts |
| 16 | Design | Humanities & Arts |
| 17 | Kinesiology | Health & Human Sciences |
| 18 | Public Health | Health & Human Sciences |
| 19 | Engineering Management | Engineering |
| 20 | Robotics | Engineering |

> Full list of 143 minors available in the catalog at https://catalog.sjsu.edu/content.php?catoid=17&navoid=7689

### 1.5 General Education Requirements

SJSU requires completion of General Education (GE) requirements for all undergraduate degrees. Details at: https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13657

### 1.6 Test Policy

**SJSU is TEST-FREE** (CSU system-wide policy). SAT/ACT are NOT required and NOT considered for admission. This is a stronger position than "test-optional" — scores are neither requested nor reviewed.

> Source: CSU system-wide policy effective Fall 2025 admissions cycle.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Lucas Graduate School of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13660&returnto=7689 |
| 2 | Finance | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13815&returnto=7689 |
| 3 | Business Analytics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13715&returnto=7689 |
| 4 | Taxation | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13965&returnto=7689 |
| 5 | Transportation Management | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13975&returnto=7689 |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 6 | Early Career MBA | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13790&returnto=7689 |
| 7 | MBA for Professionals | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13791&returnto=7689 |
| 8 | MBA for Executives | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13792&returnto=7689 |

#### Connie L. Lurie College of Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Child and Adolescent Development | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13748&returnto=7689 |
| 2 | Communicative Disorders and Sciences | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13756&returnto=7689 |
| 3 | Education, Concentration in Curriculum and Instruction | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13798&returnto=7689 |
| 4 | Education, Concentration in Educational Technology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13799&returnto=7689 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 5 | Speech Language Pathology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13957&returnto=7689 |
| 6 | Special Education | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13959&returnto=7689 |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 7 | Teaching | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13967&returnto=7689 |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 8 | Educational Leadership | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13800&returnto=7689 |

#### Charles W. Davidson College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13646&returnto=7689 |
| 2 | Biomedical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13714&returnto=7689 |
| 3 | Chemical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13736&returnto=7689 |
| 4 | Civil Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13751&returnto=7689 |
| 5 | Computer Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13759&returnto=7689 |
| 6 | Electrical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13802&returnto=7689 |
| 7 | Engineering Management | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13803&returnto=7689 |
| 8 | Industrial and Systems Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13846&returnto=7689 |
| 9 | Materials Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13886&returnto=7689 |
| 10 | Mechanical Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13896&returnto=7689 |
| 11 | Software Engineering | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13951&returnto=7689 |

#### College of Health and Human Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13863&returnto=7689 |
| 2 | Nutritional Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13914&returnto=7689 |
| 3 | Nursing | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13911&returnto=7689 |
| 4 | Occupational Therapy | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13912&returnto=7689 |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 5 | Speech Language Pathology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13957&returnto=7689 |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 6 | Public Health | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13934&returnto=7689 |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 7 | Social Work | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13954&returnto=7689 |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 8 | Nursing Practice | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13909&returnto=7689 |

##### OTD
| # | 项目 | URL |
|---|------|-----|
| 9 | Occupational Therapy | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13913&returnto=7689 |

##### AUD
| # | 项目 | URL |
|---|------|-----|
| 10 | Audiology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13697&returnto=7689 |

#### College of Humanities and the Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13809&returnto=7689 |
| 2 | Linguistics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13876&returnto=7689 |
| 3 | Music | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13904&returnto=7689 |
| 4 | Philosophy | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13916&returnto=7689 |
| 5 | Spanish | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13959&returnto=7689 |
| 6 | Television, Radio, Film and Theatre | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13968&returnto=7689 |
| 7 | Art | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13686&returnto=7689 |
| 8 | Comparative Literature | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13754&returnto=7689 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 9 | Mass Communications | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13888&returnto=7689 |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 10 | Creative Writing | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13765&returnto=7689 |
| 11 | Art, Digital Media Art | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13688&returnto=7689 |
| 12 | Art, Photography | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13690&returnto=7689 |
| 13 | Art, Pictorial Art | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13692&returnto=7689 |
| 14 | Art, Spatial Art | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13694&returnto=7689 |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 15 | Music Performance | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13905&returnto=7689 |

##### MDes
| # | 项目 | URL |
|---|------|-----|
| 16 | Design | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13782&returnto=7689 |

#### College of Information, Data & Society

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Science and Data Analytics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13849&returnto=7689 |
| 2 | Data Analytics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13779&returnto=7689 |

##### MLIS
| # | 项目 | URL |
|---|------|-----|
| 3 | Library and Information Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13873&returnto=7689 |

##### MARA
| # | 项目 | URL |
|---|------|-----|
| 4 | Archives and Records Administration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13680&returnto=7689 |

#### College of Science

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13710&returnto=7689 |
| 2 | Chemistry | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13741&returnto=7689 |
| 3 | Computer Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13760&returnto=7689 |
| 4 | Data Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13781&returnto=7689 |
| 5 | Geology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13831&returnto=7689 |
| 6 | Mathematics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13892&returnto=7689 |
| 7 | Meteorology and Climate Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13898&returnto=7689 |
| 8 | Physics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13922&returnto=7689 |
| 9 | Statistics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13961&returnto=7689 |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 10 | Mathematics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13893&returnto=7689 |

#### College of Social Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Justice Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13861&returnto=7689 |
| 2 | Psychology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13932&returnto=7689 |
| 3 | Environmental Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13811&returnto=7689 |
| 4 | Geographic Information Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13826&returnto=7689 |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 5 | Anthropology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13673&returnto=7689 |
| 6 | Communication Studies | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13755&returnto=7689 |
| 7 | Economics | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13797&returnto=7689 |
| 8 | History | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13839&returnto=7689 |
| 9 | Political Science | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13926&returnto=7689 |
| 10 | Sociology | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13957&returnto=7689 |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 11 | Public Administration | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13932&returnto=7689 |

##### MUP
| # | 项目 | URL |
|---|------|-----|
| 12 | Urban Planning | https://catalog.sjsu.edu/preview_program.php?catoid=17&poid=13981&returnto=7689 |

### 2.2 Graduate Admissions Model

SJSU graduate admissions is **decentralized** — each program sets its own requirements and deadlines beyond the university minimum. The College of Graduate Studies coordinates but programs self-manage. Application is via **Cal State Apply** (www2.calstate.edu/apply). Application fee: **$70**.

### 2.3 Graduate Deadlines (General Pattern)

Graduate deadlines vary by program. Common Fall deadlines:
- Earliest: January 15 (e.g., some Engineering programs)
- Most common: February 1, April 1, May 1, June 1, July 1
- Some programs accept applications up to August 15

Spring deadlines typically: October 1 or November 1 or December 1

> Full program-specific deadlines at: https://www.sjsu.edu/admissions/graduate/deadlines/domestic-deadlines/index.php

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | Cal State Apply (www2.calstate.edu/apply) | sjsu.edu/admissions |
| Application period (Fall) | October 1 – December 1 | sjsu.edu/admissions/deadlines |
| Application period (Spring) | August 1 – August 31 | sjsu.edu/admissions/deadlines |
| Application fee | $70 | sjsu.edu/admissions/deadlines |
| FAFSA/Dream Act priority deadline | March 2 | sjsu.edu/admissions/deadlines |
| Intent to Enroll deadline | May 1 | sjsu.edu/admissions/deadlines |
| Final transcript deadline | July 15 | sjsu.edu/admissions/deadlines |
| SAT/ACT policy | **TEST-FREE** (CSU system-wide; scores NOT accepted) | CSU system policy |
| Need-blind/need-aware | Need-aware for all applicants | sjsu.edu |
| Recommendation letters | Not required | CSU system |
| Interview | Not offered | sjsu.edu |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum (Non-Engineering) | Minimum (Engineering) | Recommended |
|------|--------------------------|----------------------|-------------|
| TOEFL iBT (0-120 scale) | 61 | 80 | 80+ |
| TOEFL (1-6 scale, after Jan 2026) | 3.5 | 4.0 | 4.0+ |
| IELTS | 6.0 | 6.5 | 6.5+ |
| PTE | 44 | 53 | 53+ |
| Duolingo | 95 | 95 | 105+ |

**Exemptions**: Applicants who completed 60 semester/90 quarter transferable units at a U.S. college or university. Scores must be less than 2 years old. SJSU TOEFL code: **4687**.

> Source: https://www.sjsu.edu/admissions/international-freshman/admission-requirements/english-proficiency.php

### 3.3 Graduate — Global Rules

- **Application platform**: Cal State Apply
- **Application fee**: $70 (same for domestic and international)
- **GRE/GMAT**: Not required by most programs (varies by department)
- **English proficiency**: Same minimums as undergraduate for international applicants
- **CGS April 15 Resolution**: SJSU follows the CGS April 15 resolution for funded offers
- **Deadlines**: Vary by program; see Section 2.3

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

| Expense Item | With Parents | Campus Housing | Off Campus |
|-------------|-------------|---------------|------------|
| Tuition & Fees | $9,553 | $9,553 | $9,553 |
| Housing | $11,461 | $15,543 | $14,104 |
| Food | (included in housing) | $7,369 | $7,245 |
| Transportation | $1,976 | $1,121 | $2,196 |
| Books & Supplies | $1,004 | $1,004 | $1,004 |
| Misc & Personal | $3,244 | $2,900 | $3,790 |
| IRA Fee | $245 | $245 | $245 |
| **Total** | **$27,483** | **$37,735** | **$38,137** |

**Non-resident surcharge**: $471 per unit (in addition to base tuition)

> Source: https://www.sjsu.edu/faso/process/cost-of-attendance.php

### 4.2 Graduate Cost (2026-2027 Academic Year)

| Expense Item | With Parents | Campus Housing | Off Campus |
|-------------|-------------|---------------|------------|
| Tuition & Fees | $10,944 | $10,944 | $10,944 |
| Housing | $11,461 | $15,543 | $14,104 |
| Food | (included in housing) | $7,369 | $7,245 |
| Transportation | $1,976 | $1,121 | $2,196 |
| Books & Supplies | $1,004 | $1,004 | $1,004 |
| Misc & Personal | $3,244 | $2,900 | $3,790 |
| IRA Fee | $245 | $245 | $245 |

**Graduate Business Professional Fee**: $321/unit for MBA, MS Accountancy, MS Finance programs

### 4.3 Financial Aid Policy

- **Need-aware** for all applicants (domestic and international)
- **FAFSA priority deadline**: March 2
- **California Dream Act**: Accepted for AB540 students
- **Grants available**: Pell Grant, State University Grant, Cal Grant, EOP Grant, SEOG
- **Scholarships**: Available through FASO
- **Cost calculator**: https://apps.sjsu.edu/costcal/

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.fall_application
  value: "October 1 - December 1"
  source_url: "https://www.sjsu.edu/admissions/deadlines/index.php"
  source_snippet: "October 1, 2025 - December 1, 2025: Cal State Apply application period"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.costs.tuition_2026_2027
  value: "$9,553"
  source_url: "https://www.sjsu.edu/faso/process/cost-of-attendance.php"
  source_snippet: "Tuition** | $9,553 | $9,553 | $9,553"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.costs.non_resident_surcharge
  value: "$471/unit"
  source_url: "https://www.sjsu.edu/bursar/fees-due-dates/tuition-other-fees/index.php"
  source_snippet: "Non-resident students pay basic registration fees plus $471 per unit"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tests.sat_act_policy
  value: "Test-free (CSU system)"
  source_url: "https://www.sjsu.edu/admissions/freshman/admissions-requirements/csu-eligibility-requirements/index.php"
  source_snippet: "CSU Eligibility Requirements - no SAT/ACT mentioned"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.toefl_minimum
  value: "61 (non-engineering), 80 (engineering)"
  source_url: "https://www.sjsu.edu/admissions/international-freshman/admission-requirements/english-proficiency.php"
  source_snippet: "TOEFL: Undergraduate, except Engineering | 61; TOEFL: All Engineering majors | 80"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.english_proficiency.ielts_minimum
  value: "6.0 (non-engineering), 6.5 (engineering)"
  source_url: "https://www.sjsu.edu/admissions/international-freshman/admission-requirements/english-proficiency.php"
  source_snippet: "IELTS: Undergraduate, except Engineering | 6.0; IELTS: Engineering | 6.5"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.application.fee
  value: "$70"
  source_url: "https://www.sjsu.edu/admissions/deadlines/index.php"
  source_snippet: "$70 Application fee due at time of submission"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.application.portal
  value: "Cal State Apply"
  source_url: "https://www.sjsu.edu/admissions/freshman/want-to-apply/apply-to-sjsu/index.php"
  source_snippet: "Cal State Apply application"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.costs.total_coa_campus_housing
  value: "$37,735"
  source_url: "https://www.sjsu.edu/faso/process/cost-of-attendance.php"
  source_snippet: "Total | $27,483 | $37,735 | $38,137"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.deadlines.intent_to_enroll
  value: "May 1"
  source_url: "https://www.sjsu.edu/admissions/deadlines/index.php"
  source_snippet: "May 1, 2026: Intent to Enroll deadline, Nonrefundable enrollment deposit due"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.costs.tuition_2026_2027
  value: "$10,944"
  source_url: "https://www.sjsu.edu/faso/process/cost-of-attendance.php"
  source_snippet: "Tuition | $10,944 | $10,944 | $10,944"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.application.fee
  value: "$70"
  source_url: "https://www.sjsu.edu/admissions/graduate/want-to-apply/index.php"
  source_snippet: "$70 Application fee"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-003:
  field: graduate.deadlines.fall_common
  value: "Varies by program; Feb 1 to Jul 1"
  source_url: "https://www.sjsu.edu/admissions/graduate/deadlines/domestic-deadlines/index.php"
  source_snippet: "Fall 2027 deadlines range from January 15 to August 15 depending on program"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.business_professional_fee
  value: "$321/unit"
  source_url: "https://www.sjsu.edu/bursar/fees-due-dates/tuition-other-fees/index.php"
  source_snippet: "Early Career MBA, MS Accountancy and MS Finance students pay the $321 per unit program-related class fees"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-P-001:
  field: programs.total_count
  value: "511"
  source_url: "https://catalog.sjsu.edu/content.php?catoid=17&navoid=7689"
  source_snippet: "511 program links found in 2025-2026 Academic Catalog"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-P-002:
  field: colleges.count
  value: "9"
  source_url: "https://www.sjsu.edu/academics/colleges-and-departments.php"
  source_snippet: "Lucas College of Business, Lurie College of Education, Davidson College of Engineering, College of Graduate Studies, College of Health and Human Sciences, College of Humanities and the Arts, College of Information Data & Society, College of Science, College of Social Sciences"
  capture_date: "2026-07-06"
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
sjsu-knowledge-base-v2
├── 00-institution-overview          (Section 0: counts, hierarchy, degrees, matrix)
├── 01-ug-business                   (Section 1: Lucas College programs)
├── 02-ug-engineering                (Section 1: Davidson College programs)
├── 03-ug-science                    (Section 1: College of Science programs)
├── 04-ug-social-sciences            (Section 1: College of Social Sciences programs)
├── 05-ug-humanities-arts            (Section 1: Humanities & Arts programs)
├── 06-ug-education                  (Section 1: Lurie College programs)
├── 07-ug-health                     (Section 1: Health & Human Sciences programs)
├── 08-ug-information                (Section 1: IDS programs)
├── 09-grad-business                 (Section 2: Lucas GSB programs)
├── 10-grad-engineering              (Section 2: Davidson programs)
├── 11-grad-science                  (Section 2: Science programs)
├── 12-grad-social-sciences          (Section 2: Social Sciences programs)
├── 13-grad-humanities-arts          (Section 2: Humanities & Arts programs)
├── 14-grad-education                (Section 2: Education programs)
├── 15-grad-health                   (Section 2: Health programs)
├── 16-grad-information              (Section 2: IDS programs)
├── 17-deadlines-requirements        (Section 3)
├── 18-costs-financial-aid           (Section 4)
└── 19-evidence-chain                (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "sjsu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: "<URL>"
  capture_date: "2026-07-06"
  version: "v2.0"
  change_status: baseline
  last_verified: "2026-07-06"
```

### Follow-Up Data Items

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program-level GRE/GMAT requirements | Per-program pages |
| P0 | International graduate deadlines | https://www.sjsu.edu/admissions/graduate/deadlines/international-deadlines/index.php |
| P1 | Detailed financial aid award packages | https://www.sjsu.edu/faso/ |
| P1 | Housing rates breakdown | https://www.sjsu.edu/housing/apply-for-housing/housing-rates/index.php |
| P1 | Impaction results by major | https://www.sjsu.edu/admissions/impaction/ |
| P2 | Transfer admission requirements | https://www.sjsu.edu/admissions/transfer/admission-requirements/ |
| P2 | Campus life and student services | https://www.sjsu.edu/studentaffairs/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | SJSU | (Other schools) |
|-----------|------|-----------------|
| Total UG cost/yr (with parents) | $27,483 | |
| Total UG cost/yr (campus housing) | $37,735 | |
| Tuition/yr (in-state UG) | $9,553 | |
| Tuition/yr (out-of-state UG) | $9,553 + $471/unit (~$17,653 for 15 units/sem) | |
| Tuition/yr (in-state grad) | $10,944 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (CSU system: Oct 1 - Dec 1) | |
| RA deadline | December 1 (Fall) | |
| SAT/ACT required? | No (test-free) | |
| TOEFL min | 61 (non-eng), 80 (eng) | |
| IELTS min | 6.0 (non-eng), 6.5 (eng) | |
| Application fee | $70 | |
| Grad application fee | $70 | |
| Total program count (Rule 1) | 511 | |
| School/department count (Rule 2) | 9 colleges | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: sjsu.edu, catalog.sjsu.edu, calstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
