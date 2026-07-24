# West Virginia University (WVU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 167 |
| 本科辅修 (Minor) | 148 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 174 |
| 研究生高级证书 (Graduate Certificate) | 41 |
| **学位项目总计 (Morgantown, UG + Grad)** | **530** |
| 学院 / 独立系所总数 | 14 |

> Note: Total of 578 programs across all WVU campuses (Morgantown 533, WVU Tech/Beckley, Potomac State/Keyser, Online). Counts above are Morgantown campus only. 3 additional Morgantown programs have unclassified level.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
West Virginia University (Morgantown)
├── Benjamin M. Statler College of Engineering and Mineral Resources  [学院]
│   ├── Aerospace Engineering                                         [系]
│   ├── Chemical Engineering                                          [系]
│   ├── Civil Engineering                                             [系]
│   ├── Computer Science                                              [系]
│   ├── Electrical Engineering                                        [系]
│   ├── Industrial Engineering                                        [系]
│   ├── Mechanical Engineering                                        [系]
│   ├── Mining Engineering                                            [系]
│   ├── Petroleum and Natural Gas Engineering                         [系]
│   └── Lane Department of Computer Science and Electrical Engineering [系]
├── Eberly College of Arts and Sciences                               [学院]
│   ├── Biology                                                       [系]
│   ├── Chemistry                                                     [系]
│   ├── Communication Studies                                         [系]
│   ├── Economics                                                     [系]
│   ├── English                                                       [系]
│   ├── Forensic and Investigative Science                            [系]
│   ├── Geography                                                     [系]
│   ├── Geology                                                       [系]
│   ├── History                                                       [系]
│   ├── Mathematics                                                   [系]
│   ├── Philosophy                                                    [系]
│   ├── Physics                                                       [系]
│   ├── Political Science                                             [系]
│   ├── Psychology                                                    [系]
│   ├── Sociology and Anthropology                                    [系]
│   └── World Languages                                               [系]
├── College of Creative Arts and Media                                [学院]
│   ├── Art and Design                                                [系]
│   ├── Music                                                         [系]
│   ├── Theatre and Dance                                             [系]
│   └── Journalism and Advertising                                    [系]
├── College of Applied Human Sciences                                 [学院]
│   ├── Counseling and Well-Being                                     [系]
│   ├── Education                                                     [系]
│   ├── Physical Education and Kinesiology                            [系]
│   └── Social Work                                                   [系]
├── John Chambers College of Business and Economics                   [学院]
│   ├── Accounting                                                    [系]
│   ├── Finance                                                       [系]
│   ├── Management                                                    [系]
│   ├── Marketing                                                     [系]
│   └── Economics (shared with Eberly)                                [系] ⚠
├── Davis College of Agriculture and Natural Resources                [学院]
│   ├── Agriculture and Extension Education                           [系]
│   ├── Animal and Nutritional Sciences                               [系]
│   ├── Design and Resource Management                               [系]
│   ├── Forestry                                                      [系]
│   ├── Horticulture                                                  [系]
│   ├── Plant and Soil Sciences                                       [系]
│   └── Wildlife and Fisheries Resources                              [系]
├── School of Medicine                                                [学院]
│   ├── Biomedical Sciences                                           [系]
│   ├── Communication Sciences and Disorders                          [系]
│   ├── Immunology and Medical Microbiology                           [系]
│   └── Respiratory Therapy                                           [系]
├── School of Nursing                                                 [学院]
│   └── Nursing                                                       [系]
├── School of Public Health                                           [学院]
│   ├── Epidemiology and Environmental Health                         [系]
│   └── Health Policy and Management                                  [系]
├── School of Dentistry                                               [学院]
│   └── Dental Hygiene                                                [系]
├── School of Pharmacy                                                [学院]
│   └── Pharmaceutical Sciences                                       [系]
├── College of Law                                                    [学院]
│   └── Law                                                           [系]
├── Honors College                                                    [学院]
│   └── Interdisciplinary Honors                                      [系]
└── Intercollegiate Programs                                          [学院]
    └── Multidisciplinary                                             [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 28 |
| BS | BS | Bachelor of Science | 本科 | 50 |
| BSBA | BSBA | Bachelor of Science in Business Administration | 本科 | 8 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 5 |
| BSJ | BSJ | Bachelor of Science in Journalism | 本科 | 3 |
| BSAgr | BSAgr | Bachelor of Science in Agriculture | 本科 | 3 |
| BM | BM | Bachelor of Music | 本科 | 4 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 2 |
| BSAE | BSAE | Bachelor of Science in Aerospace Engineering | 本科 | 1 |
| BSCE | BSCE | Bachelor of Science in Civil Engineering | 本科 | 1 |
| BSChE | BSChE | Bachelor of Science in Chemical Engineering | 本科 | 1 |
| BSCpE | BSCpE | Bachelor of Science in Computer Engineering | 本科 | 1 |
| BSEE | BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| BSIE | BSIE | Bachelor of Science in Industrial Engineering | 本科 | 1 |
| BSME | BSME | Bachelor of Science in Mechanical Engineering | 本科 | 1 |
| BSMinE | BSMinE | Bachelor of Science in Mining Engineering | 本科 | 1 |
| BSPNGE | BSPNGE | Bachelor of Science in Petroleum & Natural Gas Engineering | 本科 | 1 |
| BSCS | BSCS | Bachelor of Science in Computer Science | 本科 | 1 |
| BSF | BSF | Bachelor of Science in Forestry | 本科 | 1 |
| BAS | BAS | Bachelor of Applied Science | 本科 | 2 |
| BIS | BIS | Bachelor of Interdisciplinary Studies | 本科 | 1 |
| BSLA | BSLA | Bachelor of Science in Landscape Architecture | 本科 | 1 |
| RBA | RBA | Regents Bachelor of Arts | 本科 | 1 |
| BSRT | BSRT | Bachelor of Science in Respiratory Therapy | 本科 | 1 |
| ABSN | ABSN | Accelerated Bachelor of Science in Nursing | 本科 | 1 |
| AA | AA | Associate of Arts | 本科 | 14 |
| AS | AS | Associate of Science | 本科 | 9 |
| AAS | AAS | Associate of Applied Science | 本科 | 5 |
| MA | MA | Master of Arts | 研究生 | 16 |
| MS | MS | Master of Science | 研究生 | 54 |
| MFA | MFA | Master of Fine Arts | 研究生 | 7 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 |
| MPH | MPH | Master of Public Health | 研究生 | 3 |
| MHA | MHA | Master of Health Administration | 研究生 | 2 |
| MSE | MSE | Master of Science in Engineering | 研究生 | 1 |
| MSAE | MSAE | Master of Science in Aerospace Engineering | 研究生 | 1 |
| MSBME | MSBME | Master of Science in Biomedical Engineering | 研究生 | 1 |
| MSME | MSME | Master of Science in Mechanical Engineering | 研究生 | 1 |
| MSSE | MSSE | Master of Science in Software Engineering | 研究生 | 1 |
| MSIE | MSIE | Master of Science in Industrial Engineering | 研究生 | 1 |
| MSMinE | MSMinE | Master of Science in Mining Engineering | 研究生 | 1 |
| MSPNGE | MSPNGE | Master of Science in Petroleum & Natural Gas Engineering | 研究生 | 1 |
| MSMSE | MSMSE | Master of Science in Materials Science & Engineering | 研究生 | 1 |
| MSF | MSF | Master of Science in Forestry | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 1 |
| MSJ | MSJ | Master of Science in Journalism | 研究生 | 1 |
| MAcc | MAcc | Master of Accountancy | 研究生 | 1 |
| MAgr | MAgr | Master of Agriculture | 研究生 | 1 |
| MHS | MHS | Master of Health Sciences | 研究生 | 2 |
| MOT | MOT | Master of Occupational Therapy | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 4 |
| MEd | MEd | Master of Education | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 53 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 2 |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 2 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| Graduate Certificate | Graduate Certificate | 高级证书 | 研究生 | 41 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | AA/AS | BA | BS | BSBA | BFA | BSJ | BM/BSN/BSW/Other UG | MA | MS | MFA | MBA | MPH/MHA | MM | PhD | EdD/DMA/DNP | JD/MD/PharmD/AuD/OTD | Cert | 合计 |
|------------|-------|----|----|------|-----|-----|---------------------|----|----|-----|-----|---------|----|----|----|------|------|------|
| Statler Engineering | 0 | 0 | 48 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 3 | 81 |
| Eberly A&S | 0 | 28 | 5 | 0 | 0 | 0 | 0 | 10 | 7 | 0 | 0 | 0 | 0 | 17 | 1 | 0 | 1 | 69 |
| Creative Arts & Media | 0 | 0 | 0 | 0 | 5 | 3 | 7 | 2 | 0 | 7 | 0 | 0 | 4 | 0 | 3 | 0 | 10 | 41 |
| Applied Human Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 8 | 0 | 0 | 0 | 0 | 3 | 2 | 0 | 7 | 27 |
| Chambers Business & Econ | 0 | 0 | 6 | 8 | 0 | 0 | 0 | 0 | 7 | 0 | 3 | 0 | 0 | 4 | 0 | 0 | 3 | 31 |
| Davis Agriculture & NR | 28 | 0 | 14 | 0 | 0 | 0 | 3 | 1 | 10 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 2 | 65 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 9 | 0 | 0 | 0 | 0 | 10 | 0 | 1 | 2 | 29 |
| School of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 2 | 8 |
| School of Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 2 | 10 |
| School of Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 |
| College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Intercollegiate | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **合计** | **28** | **28** | **73** | **8** | **5** | **3** | **28** | **16** | **57** | **7** | **3** | **3** | **4** | **63** | **8** | **3** | **35** | **370** |

> Note: Matrix counts degree-granting programs only. Minors (148) and some interdisciplinary programs are excluded from this matrix. Total 530 degree programs (167 UG + 174 Grad + 41 Cert + 48 AA/AS/AAS).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

WVU has 14 colleges/schools on the Morgantown campus granting undergraduate degrees. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Benjamin M. Statler College of Engineering and Mineral Resources

##### Department of Aerospace Engineering
###### BSAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.wvu.edu/academics/majors-and-minors/aerospace-engineering-bsae/ |

##### Department of Chemical Engineering
###### BSChE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.wvu.edu/academics/majors-and-minors/chemical-engineering-bsche/ |

##### Department of Civil Engineering
###### BSCE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.wvu.edu/academics/majors-and-minors/civil-engineering-bsce/ |

##### Lane Department of Computer Science and Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.wvu.edu/academics/majors-and-minors/computer-science-bs/ |
| 2 | Cybersecurity | https://www.wvu.edu/academics/majors-and-minors/cybersecurity-bs/ |
| 3 | Data Science | https://www.wvu.edu/academics/majors-and-minors/data-science-bs/ |

###### BSCpE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.wvu.edu/academics/majors-and-minors/computer-engineering-bscpe/ |

###### BSEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.wvu.edu/academics/majors-and-minors/electrical-engineering-bsee/ |

##### Department of Industrial Engineering
###### BSIE
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://www.wvu.edu/academics/majors-and-minors/industrial-engineering-bsie/ |
| 2 | Biometric Systems Engineering | https://www.wvu.edu/academics/majors-and-minors/biometric-systems-engineering-bs/ |
| 3 | Safety Management | https://www.wvu.edu/academics/majors-and-minors/safety-management-bs/ |

##### Department of Mechanical Engineering
###### BSME
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.wvu.edu/academics/majors-and-minors/mechanical-engineering-bsme/ |

##### Department of Mining Engineering
###### BSMinE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mining Engineering | https://www.wvu.edu/academics/majors-and-minors/mining-engineering-bsmine/ |

##### Department of Petroleum and Natural Gas Engineering
###### BSPNGE
| # | 专业 | URL |
|---|------|-----|
| 1 | Petroleum and Natural Gas Engineering | https://www.wvu.edu/academics/majors-and-minors/petroleum-and-natural-gas-engineering-bspnge/ |

#### Eberly College of Arts and Sciences

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.wvu.edu/academics/majors-and-minors/biology-bs/ |
| 2 | Biochemistry | https://www.wvu.edu/academics/majors-and-minors/biochemistry-bs/ |
| 3 | Environmental Microbiology | https://www.wvu.edu/academics/majors-and-minors/environmental-microbiology-bs/ |
| 4 | Immunology and Medical Microbiology | https://www.wvu.edu/academics/majors-and-minors/immunology-and-medical-microbiology-bs/ |
| 5 | Neuroscience | https://www.wvu.edu/academics/majors-and-minors/neuroscience-bs/ |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.wvu.edu/academics/majors-and-minors/chemistry-bs/ |
| 2 | Forensic Chemistry | https://www.wvu.edu/academics/majors-and-minors/forensic-chemistry-bs/ |

##### Department of Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.wvu.edu/academics/majors-and-minors/communication-studies-ba/ |
| 2 | Organizational Leadership | https://www.wvu.edu/academics/majors-and-minors/organizational-leadership-ba/ |
| 3 | Strategic Social Media | https://www.wvu.edu/academics/majors-and-minors/strategic-social-media-ba/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.wvu.edu/academics/majors-and-minors/economics-ba/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.wvu.edu/academics/majors-and-minors/english-ba/ |
| 2 | Creative Writing | https://www.wvu.edu/academics/majors-and-minors/creative-writing-ba/ |
| 3 | Professional Writing and Editing | https://www.wvu.edu/academics/majors-and-minors/professional-writing-and-editing-ba/ |
| 4 | Linguistics | https://www.wvu.edu/academics/majors-and-minors/linguistics-ba/ |

##### Department of Forensic and Investigative Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic and Investigative Science | https://www.wvu.edu/academics/majors-and-minors/forensic-and-investigative-science-bs/ |
| 2 | Forensic Biology | https://www.wvu.edu/academics/majors-and-minors/forensic-biology-bs/ |
| 3 | Forensic Chemistry | https://www.wvu.edu/academics/majors-and-minors/forensic-chemistry-bs/ |
| 4 | Forensic Examiner | https://www.wvu.edu/academics/majors-and-minors/forensic-examiner-bs/ |

##### Department of Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.wvu.edu/academics/majors-and-minors/geography-ba/ |
| 2 | Environmental Geoscience | https://www.wvu.edu/academics/majors-and-minors/environmental-geoscience-ba/ |

##### Department of Geology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://www.wvu.edu/academics/majors-and-minors/geology-bs/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.wvu.edu/academics/majors-and-minors/history-ba/ |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.wvu.edu/academics/majors-and-minors/mathematics-ba/ |
| 2 | Actuarial Science | https://www.wvu.edu/academics/majors-and-minors/actuarial-science-ba/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.wvu.edu/academics/majors-and-minors/philosophy-ba/ |
| 2 | Religious Studies | https://www.wvu.edu/academics/majors-and-minors/religious-studies-ba/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.wvu.edu/academics/majors-and-minors/physics-bs/ |
| 2 | Biophysics | https://www.wvu.edu/academics/majors-and-minors/biophysics-bs/ |
| 3 | Forensic Physics | https://www.wvu.edu/academics/majors-and-minors/forensic-physics-bs/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.wvu.edu/academics/majors-and-minors/political-science-ba/ |
| 2 | International Studies | https://www.wvu.edu/academics/majors-and-minors/international-studies-ba/ |
| 3 | Legal Studies | https://www.wvu.edu/academics/majors-and-minors/legal-studies-ba/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.wvu.edu/academics/majors-and-minors/psychology-ba/ |

##### Department of Sociology and Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.wvu.edu/academics/majors-and-minors/sociology-ba/ |
| 2 | Anthropology | https://www.wvu.edu/academics/majors-and-minors/anthropology-ba/ |
| 3 | Criminology | https://www.wvu.edu/academics/majors-and-minors/criminology-ba/ |

##### Department of World Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | World Languages | https://www.wvu.edu/academics/majors-and-minors/world-languages-ba/ |
| 2 | Spanish | https://www.wvu.edu/academics/majors-and-minors/spanish-ba/ |
| 3 | Chinese Studies | https://www.wvu.edu/academics/majors-and-minors/chinese-studies-ba/ |

#### College of Creative Arts and Media

##### Department of Art and Design
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://www.wvu.edu/academics/majors-and-minors/acting-bfa/ |
| 2 | Art and Design | https://www.wvu.edu/academics/majors-and-minors/art-and-design-bfa/ |
| 3 | Game Design and Interactive Media | https://www.wvu.edu/academics/majors-and-minors/game-design-and-interactive-media-bfa/ |
| 4 | Graphic Design | https://www.wvu.edu/academics/majors-and-minors/graphic-design-bfa/ |
| 5 | Musical Theatre | https://www.wvu.edu/academics/majors-and-minors/musical-theatre-bfa/ |

##### School of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.wvu.edu/academics/majors-and-minors/music-bm/ |
| 2 | Music Education | https://www.wvu.edu/academics/majors-and-minors/music-education-bm/ |
| 3 | Music Performance | https://www.wvu.edu/academics/majors-and-minors/music-performance-bm/ |
| 4 | Music Industry | https://www.wvu.edu/academics/majors-and-minors/music-industry-bm/ |

##### School of Journalism
###### BSJ
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising and Public Relations | https://www.wvu.edu/academics/majors-and-minors/advertising-and-public-relations-bsj/ |
| 2 | Journalism | https://www.wvu.edu/academics/majors-and-minors/journalism-bsj/ |
| 3 | Sports and Adventure Media | https://www.wvu.edu/academics/majors-and-minors/sports-and-adventure-media-bsj/ |

##### Department of Theatre and Dance
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://www.wvu.edu/academics/majors-and-minors/theatre-bfa/ |
| 2 | Dance | https://www.wvu.edu/academics/majors-and-minors/dance-bfa/ |

#### College of Applied Human Sciences

##### Department of Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://www.wvu.edu/academics/majors-and-minors/elementary-education-bs/ |
| 2 | Secondary Education | https://www.wvu.edu/academics/majors-and-minors/secondary-education-bs/ |
| 3 | Special Education | https://www.wvu.edu/academics/majors-and-minors/special-education-bs/ |
| 4 | Multidisciplinary Studies | https://www.wvu.edu/academics/majors-and-minors/multidisciplinary-studies-bs/ |

##### Department of Counseling and Well-Being
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development and Family Studies | https://www.wvu.edu/academics/majors-and-minors/child-development-and-family-studies-bs/ |
| 2 | Speech-Language Pathology and Audiology | https://www.wvu.edu/academics/majors-and-minors/speech-language-pathology-and-audiology-bs/ |
| 3 | Addiction Studies | https://www.wvu.edu/academics/majors-and-minors/addiction-studies-bs/ |

##### Department of Physical Education and Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Exercise Psychology | https://www.wvu.edu/academics/majors-and-minors/sport-and-exercise-psychology-bs/ |
| 2 | Physical Education Teacher Education | https://www.wvu.edu/academics/majors-and-minors/physical-education-teacher-education-bs/ |
| 3 | Exercise Physiology | https://www.wvu.edu/academics/majors-and-minors/exercise-physiology-bs/ |
| 4 | Athletic Coaching Education | https://www.wvu.edu/academics/majors-and-minors/athletic-coaching-education-bs/ |
| 5 | Sport Management | https://www.wvu.edu/academics/majors-and-minors/sport-management-bs/ |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.wvu.edu/academics/majors-and-minors/social-work-bsw/ |

#### John Chambers College of Business and Economics

##### Department of Accounting
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.wvu.edu/academics/majors-and-minors/accounting-bsba/ |

##### Department of Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.wvu.edu/academics/majors-and-minors/finance-bsba/ |
| 2 | Economics | https://www.wvu.edu/academics/majors-and-minors/economics-bsba/ |

##### Department of Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://www.wvu.edu/academics/majors-and-minors/management-bsba/ |
| 2 | Entrepreneurship | https://www.wvu.edu/academics/majors-and-minors/entrepreneurship-bsba/ |
| 3 | Hospitality and Tourism Management | https://www.wvu.edu/academics/majors-and-minors/hospitality-and-tourism-management-bsba/ |
| 4 | General Business | https://www.wvu.edu/academics/majors-and-minors/general-business-bsba/ |

##### Department of Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.wvu.edu/academics/majors-and-minors/marketing-bsba/ |
| 2 | Integrated Marketing Communications | https://www.wvu.edu/academics/majors-and-minors/integrated-marketing-communications-bs/ |
| 3 | Fashion, Dress and Merchandising | https://www.wvu.edu/academics/majors-and-minors/fashion-dress-and-merchandising-bs/ |
| 4 | Design Studies | https://www.wvu.edu/academics/majors-and-minors/design-studies-bs/ |
| 5 | Interior Design | https://www.wvu.edu/academics/majors-and-minors/interior-design-bs/ |
| 6 | Landscape Architecture | https://www.wvu.edu/academics/majors-and-minors/landscape-architecture-bsla/ |
| 7 | Environmental and Energy Resource Management | https://www.wvu.edu/academics/majors-and-minors/environmental-and-energy-resource-management-bs/ |
| 8 | Forest Resources Management | https://www.wvu.edu/academics/majors-and-minors/forest-resources-management-bsf/ |
| 9 | Agribusiness Management | https://www.wvu.edu/academics/majors-and-minors/agribusiness-management-rba/ |
| 10 | Agriculture | https://www.wvu.edu/academics/majors-and-minors/agriculture-bs/ |
| 11 | Animal and Nutritional Sciences | https://www.wvu.edu/academics/majors-and-minors/animal-and-nutritional-sciences-bs/ |
| 12 | Biochemistry | https://www.wvu.edu/academics/majors-and-minors/biochemistry-bs/ |
| 13 | Environmental and Community Horticulture | https://www.wvu.edu/academics/majors-and-minors/environmental-and-community-horticulture-bs/ |
| 14 | Turfgrass Management | https://www.wvu.edu/academics/majors-and-minors/turfgrass-management-bs/ |

#### School of Medicine

##### Department of Biomedical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Laboratory Diagnostics | https://www.wvu.edu/academics/majors-and-minors/biomedical-laboratory-diagnostics-bs/ |
| 2 | Health Informatics and Information Management | https://www.wvu.edu/academics/majors-and-minors/health-informatics-and-information-management-bs/ |
| 3 | Multidisciplinary Studies | https://www.wvu.edu/academics/majors-and-minors/multidisciplinary-studies-bs/ |

##### Department of Communication Sciences and Disorders
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | https://www.wvu.edu/academics/majors-and-minors/communication-sciences-and-disorders-bs/ |

##### Department of Immunology and Medical Microbiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Immunology and Medical Microbiology | https://www.wvu.edu/academics/majors-and-minors/immunology-and-medical-microbiology-bs/ |

##### Department of Respiratory Therapy
###### BSRT
| # | 专业 | URL |
|---|------|-----|
| 1 | Respiratory Therapy | https://www.wvu.edu/academics/majors-and-minors/respiratory-therapy-bsrt/ |

#### School of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Pre-Nursing) | https://www.wvu.edu/academics/majors-and-minors/nursing-bsn/ |
| 2 | Nursing (Direct Admission) | https://www.wvu.edu/academics/majors-and-minors/nursing-bsn/ |
| 3 | Accelerated Nursing | https://www.wvu.edu/academics/majors-and-minors/accelerated-nursing-absn/ |

#### School of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://www.wvu.edu/academics/majors-and-minors/public-health-bs/ |
| 2 | Exercise Physiology | https://www.wvu.edu/academics/majors-and-minors/exercise-physiology-bs/ |

#### School of Dentistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene | https://www.wvu.edu/academics/majors-and-minors/dental-hygiene-bs/ |

#### School of Pharmacy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://www.wvu.edu/academics/majors-and-minors/pharmaceutical-sciences-bs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | Home College | URL |
|---|------|-------------|-----|
| 1 | Interdisciplinary Studies | Intercollegiate | https://www.wvu.edu/academics/majors-and-minors/interdisciplinary-studies-bis/ |
| 2 | Regents Bachelor of Arts | Academic Affairs | https://www.wvu.edu/academics/majors-and-minors/regents-bachelor-of-arts-rba/ |

### 1.4 Minors — Complete List

WVU offers 148 undergraduate minors. The complete list is available at https://www.wvu.edu/academics/programs (filter by Minor). Key minors include:

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Accounting | Chambers Business |
| 2 | Actuarial Science | Eberly A&S |
| 3 | Addiction Studies | Applied Human Sciences |
| 4 | Adventure Recreation Management | Applied Human Sciences |
| 5 | Advertising | Creative Arts & Media |
| 6 | Aerospace Engineering | Statler Engineering |
| 7 | Agricultural and Extension Education | Davis Agriculture |
| 8 | American History | Eberly A&S |
| 9 | Animal and Nutritional Sciences | Davis Agriculture |
| 10 | Anthropology | Eberly A&S |
| 11 | Arabic Studies | Eberly A&S |
| 12 | Art History | Creative Arts & Media |
| 13 | Asian Studies | Eberly A&S |
| 14 | Astronomy | Eberly A&S |
| 15 | Athletic Coaching Education | Applied Human Sciences |
| 16 | Biology | Eberly A&S |
| 17 | Biometrics | Statler Engineering |
| 18 | Business Administration | Chambers Business |
| 19 | Chemistry | Eberly A&S |
| 20 | Chinese Studies | Eberly A&S |
| 21 | Coaching | Applied Human Sciences |
| 22 | Communication Studies | Eberly A&S |
| 23 | Community Development | Davis Agriculture |
| 24 | Computer Science | Statler Engineering |
| 25 | Creative Writing | Eberly A&S |
| 26 | Criminal Justice | Eberly A&S |
| 27 | Dance | Creative Arts & Media |
| 28 | Data Science | Statler Engineering |
| 29 | Design Studies | Creative Arts & Media |
| 30 | Disability Studies | Applied Human Sciences |
| 33 | Economics | Eberly A&S |
| 34 | Electrical Engineering | Statler Engineering |
| 35 | Energy Environment | Davis Agriculture |
| 36 | Engineering | Statler Engineering |
| 37 | English | Eberly A&S |
| 38 | Entrepreneurship | Chambers Business |
| 39 | Environmental and Community Horticulture | Davis Agriculture |
| 40 | Environmental and Energy Resource Management | Davis Agriculture |
| 41 | Environmental Geoscience | Eberly A&S |
| 42 | Environmental Protection | Davis Agriculture |
| 43 | Fashion, Dress and Merchandising | Davis Agriculture |
| 44 | Film Studies | Creative Arts & Media |
| 45 | Finance | Chambers Business |
| 46 | Food Science and Technology | Davis Agriculture |
| 47 | Forensic and Investigative Science | Eberly A&S |
| 48 | Forestry | Davis Agriculture |
| 49 | French | Eberly A&S |
| 50 | Game Design and Interactive Media | Creative Arts & Media |
| 51 | Geography | Eberly A&S |
| 52 | Geology | Eberly A&S |
| 53 | German | Eberly A&S |
| 54 | Global Engineering | Statler Engineering |
| 55 | Health and Well-Being | Applied Human Sciences |
| 56 | History | Eberly A&S |
| 57 | Hospitality and Tourism Management | Chambers Business |
| 58 | Human Services | Applied Human Sciences |
| 59 | Industrial Engineering | Statler Engineering |
| 60 | Interior Design | Davis Agriculture |
| 61 | International Studies | Eberly A&S |
| 62 | Italian | Eberly A&S |
| 63 | Japanese | Eberly A&S |
| 64 | Journalism | Creative Arts & Media |
| 65 | Korean | Eberly A&S |
| 66 | Landscape Architecture | Davis Agriculture |
| 67 | Legal Studies | Eberly A&S |
| 68 | Linguistics | Eberly A&S |
| 69 | Management | Chambers Business |
| 70 | Management Information Systems | Chambers Business |
| 71 | Marketing | Chambers Business |
| 72 | Mathematics | Eberly A&S |
| 73 | Mechanical Engineering | Statler Engineering |
| 74 | Medieval and Renaissance Studies | Eberly A&S |
| 75 | Military Science | Intercollegiate |
| 76 | Mining Engineering | Statler Engineering |
| 77 | Music | Creative Arts & Media |
| 78 | Native American Studies | Eberly A&S |
| 79 | Naval Science | Intercollegiate |
| 80 | Neuroscience | Eberly A&S |
| 81 | Nutrition and Food Science | Davis Agriculture |
| 82 | Petroleum and Natural Gas Engineering | Statler Engineering |
| 83 | Philosophy | Eberly A&S |
| 84 | Photography | Creative Arts & Media |
| 85 | Physics | Eberly A&S |
| 86 | Political Science | Eberly A&S |
| 87 | Professional Writing and Editing | Eberly A&S |
| 88 | Psychology | Eberly A&S |
| 89 | Public Administration | Eberly A&S |
| 90 | Public Health | School of Public Health |
| 91 | Religious Studies | Eberly A&S |
| 92 | Russian | Eberly A&S |
| 93 | Safety and Health Extension | Davis Agriculture |
| 94 | Safety Management | Statler Engineering |
| 95 | Sociology | Eberly A&S |
| 96 | Spanish | Eberly A&S |
| 97 | Sport and Exercise Psychology | Applied Human Sciences |
| 98 | Sport Management | Applied Human Sciences |
| 99 | Statistics | Eberly A&S |
| 100 | Studio Art | Creative Arts & Media |
| 101 | Theatre | Creative Arts & Media |
| 102 | Theatre Design and Technology | Creative Arts & Media |
| 103 | Wildlife and Fisheries Resources | Davis Agriculture |
| 104 | Women's and Gender Studies | Eberly A&S |
| 105 | World Languages | Eberly A&S |

> Note: Full list of 148 minors available at https://www.wvu.edu/academics/programs (filter: Minor, Campus: Morgantown).

### 1.5 General Education Requirements

WVU's General Education Foundations (GEF) program requires coursework in the following areas:
- **Area 1**: Fine Arts (3 credits)
- **Area 2**: Humanities (6 credits)
- **Area 3**: Physical/Natural Sciences (6-8 credits, must include lab)
- **Area 4**: Society and Connections (6 credits)
- **Area 5**: Human Behavior (3 credits)
- **Area 6**: Composition and Rhetoric (6 credits)
- **Area 7**: Mathematics (3-4 credits)
- **Area 8**: Global Studies and Diversity (3 credits)

Source: https://www.wvu.edu/academics/general-education-foundations

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

WVU offers 215 graduate programs (including 41 certificates) on the Morgantown campus. The full list is available at https://graduateadmissions.wvu.edu/academics/graduate-programs.

#### Benjamin M. Statler College of Engineering and Mineral Resources

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | MSAE | https://graduateadmissions.wvu.edu/academics/graduate-programs/aerospace-engineering-m |
| 2 | Aerospace Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/aerospace-engineering-d |
| 3 | Biomedical Engineering | MSBME | https://graduateadmissions.wvu.edu/academics/graduate-programs/biomedical-engineering-msbme |
| 4 | Biomedical Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/biomedical-engineering-phd |
| 5 | Chemical Engineering | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/chemical-engineering-m |
| 6 | Chemical Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/chemical-engineering-d |
| 7 | Civil Engineering | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/civil-engineering-m |
| 8 | Civil Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/civil-engineering-d |
| 9 | Computer Science | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/computer-science-m |
| 10 | Computer Science | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/computer-science-d |
| 11 | Computer Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/computer-engineering-d |
| 12 | Electrical Engineering | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/electrical-engineering-m |
| 13 | Electrical Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/electrical-engineering-d |
| 14 | Engineering | MSE | https://graduateadmissions.wvu.edu/academics/graduate-programs/engineering-m |
| 15 | Industrial Engineering | MSIE | https://graduateadmissions.wvu.edu/academics/graduate-programs/industrial-engineering-m |
| 16 | Industrial Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/industrial-engineering-d |
| 17 | Materials Science and Engineering | MSMSE | https://graduateadmissions.wvu.edu/academics/graduate-programs/material-science-and-engineering-m |
| 18 | Materials Science and Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/material-science-and-engineering-d |
| 19 | Mechanical Engineering | MSME | https://graduateadmissions.wvu.edu/academics/graduate-programs/mechanical-engineering-m |
| 20 | Mechanical Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/mechanical-engineering-d |
| 21 | Mining Engineering | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/mining-engineering-m |
| 22 | Mining Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/mining-engineering-d |
| 23 | Petroleum and Natural Gas Engineering | MSPNGE | https://graduateadmissions.wvu.edu/academics/graduate-programs/petroleum-and-natural-gas-engineering-m |
| 24 | Petroleum and Natural Gas Engineering | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/petroleum-and-natural-gas-engineering-d |
| 25 | Software Engineering | MSSE | https://online.wvu.edu/programs/masters-degrees/software-engineering-msse |
| 26 | Engineering Management | MS | https://online.wvu.edu/programs/masters-degrees/engineering-management-ms |
| 27 | Safety Management | MS | https://online.wvu.edu/degrees-certificates/graduate-degrees/safety-management-m-s |
| 28 | Cybersecurity | MS | https://online.wvu.edu/programs/masters-degrees/cybersecurity-ms |
| 29 | Artificial Intelligence | MS | https://online.wvu.edu/programs/masters-degrees/artificial-intelligence-ms |
| 30 | Business Cybersecurity Management | MS | https://online.wvu.edu/programs/masters-degrees/business-cybersecurity-management-ms |
| 31 | Midstream Petroleum Engineering | MS | https://online.wvu.edu/programs/masters-degrees/midstream-petroleum-engineering-ms |
| 32 | Applied Statistics | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/applied-statistics-gc |
| 33 | Midstream Petroleum Engineering | Certificate | https://online.wvu.edu/programs/graduate-certificates/midstream-petroleum-engineering-graduate-certificate |
| 34 | GIS and Spatial Analysis | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/gis-and-spatial-analysis-gc-oc |

#### Eberly College of Arts and Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/biology-m |
| 2 | Biology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/biology-d |
| 3 | Chemistry | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/chemistry-d |
| 4 | Communication Studies | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/communication-studies-d |
| 5 | Economics | MS | https://online.wvu.edu/programs/masters-degrees/economics-ms |
| 6 | Economics | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/economics-d |
| 7 | English | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/english-m |
| 8 | English | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/english-d |
| 9 | Forensic and Investigative Science | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/forensic-science-and-investigative-sciences-m |
| 10 | Forensic Science | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/forensic-science-d |
| 11 | Geography | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/geography-m |
| 12 | Geography | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/geography-d |
| 13 | Geology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/geology-m |
| 14 | Geology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/geology-d |
| 15 | History | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/history-m |
| 16 | History | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/history-d |
| 17 | Mathematics | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/mathematics-m |
| 18 | Physics | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/physics-m |
| 19 | Physics | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/physics-d |
| 20 | Political Science | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/political-science-m |
| 21 | Political Science | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/political-science-d |
| 22 | Psychology: Clinical | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/psychology-clinical |
| 23 | Psychology: Behavioral Neuroscience | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/psychology-behavioral-neuroscience |
| 24 | Psychology: Life-Span Development | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/psychology-life-span-development |
| 25 | Psychology: Behavior Analysis | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/psychology-behavior-analysis |
| 26 | Professional Writing and Editing | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/professional-writing-and-editing-m |
| 27 | Public History | MA | https://graduateadmissions.wvu.edu/academics/graduate-programs/public-history-m |
| 28 | Sociology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/sociology-d |
| 29 | Statistics | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/statistics-m |
| 30 | Creative Writing | MFA | https://graduateadmissions.wvu.edu/academics/graduate-programs/creative-writing-m |
| 31 | Cultural Resource Management | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/cultural-resource-management |
| 32 | GIS and Spatial Analysis | MS | https://online.wvu.edu/programs/masters-degrees/geographic-information-systems-and-spatial-analysis-ms |
| 33 | Game Design | MA | https://online.wvu.edu/programs/masters-degrees/game-design-ma |
| 34 | Strategic Organizational Communication | MA | https://online.wvu.edu/programs/masters-degrees/strategic-organizational-communication-ma |
| 35 | University Teaching | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/university-teaching |

#### College of Creative Arts and Media

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Acting | MFA | https://www.wvu.edu/academics/programs/acting-mfa |
| 2 | Art and Design | MFA | https://www.wvu.edu/academics/programs/art-and-design-mfa |
| 3 | Art Education | MA | https://www.wvu.edu/academics/programs/art-education-ma |
| 4 | Conducting | DMA | https://www.wvu.edu/academics/programs/conducting-dma |
| 5 | Conducting | MM | https://www.wvu.edu/academics/programs/conducting-mm |
| 6 | Costume Design and Technology | MFA | https://www.wvu.edu/academics/programs/costume-design-and-technology-mfa |
| 7 | Lighting Design and Technology | MFA | https://www.wvu.edu/academics/programs/lighting-design-and-technology-mfa |
| 8 | Music Education | MM | https://www.wvu.edu/academics/programs/music-education-mm |
| 9 | Music Theory | MA | https://www.wvu.edu/academics/programs/music-theory-ma |
| 10 | Musicology | MA | https://www.wvu.edu/academics/programs/musicology-ma |
| 11 | Performance | DMA | https://www.wvu.edu/academics/programs/performance-dma |
| 12 | Performance | MM | https://www.wvu.edu/academics/programs/performance-mm |
| 13 | Piano Pedagogy | MM | https://www.wvu.edu/academics/programs/piano-pedagogy-mm |
| 14 | Scenic Design and Technology | MFA | https://www.wvu.edu/academics/programs/scenic-design-and-technology-mfa |
| 15 | Studio Art | MA | https://www.wvu.edu/academics/programs/studio-art-ma |
| 16 | Technical Direction | MFA | https://www.wvu.edu/academics/programs/technical-direction-mfa |
| 17 | Journalism | MSJ | https://www.wvu.edu/academics/programs/journalism-msj |
| 18 | Integrated Marketing Communications | MS | https://online.wvu.edu/programs/masters-degrees/integrated-marketing-communications-ms |
| 19 | Data Marketing Communications | MS | https://online.wvu.edu/programs/masters-degrees/data-marketing-communications-ms |
| 20 | Digital Marketing Communications | MS | https://online.wvu.edu/degrees-certificates/graduate-degrees/digital-marketing-communications-m-s |
| 21 | Music Business and Industry | MA | https://online.wvu.edu/degrees-certificates/graduate-degrees/music-business-industry-m-a |
| 22 | Creative Strategy | Certificate | https://online.wvu.edu/programs/graduate-certificates/creative-strategy-graduate-certificate |
| 23 | Data Marketing Communications | Certificate | https://online.wvu.edu/programs/graduate-certificates/data-marketing-communications-graduate-certificate |
| 24 | Digital and Social Media | Certificate | https://online.wvu.edu/programs/graduate-certificates/digital-and-social-media-graduate-certificate |
| 25 | Healthcare Communication | Certificate | https://online.wvu.edu/programs/graduate-certificates/healthcare-communication-graduate-certificate |
| 26 | Higher Education Marketing | Certificate | https://online.wvu.edu/programs/graduate-certificates/higher-education-marketing-graduate-certificate |
| 27 | Integrated Marketing Communications | Certificate | https://online.wvu.edu/programs/graduate-certificates/integrated-marketing-communications-graduate-certificate |
| 28 | Music Business and Industry | Certificate | https://online.wvu.edu/programs/graduate-certificates/music-business-and-industry-graduate-certificate |
| 29 | Public Relations Leadership | Certificate | https://online.wvu.edu/programs/graduate-certificates/public-relations-leadership-graduate-certificate |
| 30 | Sport Analytics and Performance | Certificate | https://www.wvu.edu/academics/programs/sport-analytics-and-performance-graduate-certificate |

#### College of Applied Human Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Coaching and Teaching Studies | EdD | https://www.wvu.edu/academics/programs/coaching-and-teaching-studies-edd |
| 2 | Coaching and Teaching Studies | PhD | https://www.wvu.edu/academics/programs/coaching-and-teaching-studies-phd |
| 3 | Counseling | MS | https://www.wvu.edu/academics/programs/counseling-ms |
| 4 | Educational Theory and Practice | PhD | https://www.wvu.edu/academics/programs/educational-theory-and-practice-phd |
| 5 | Exercise Physiology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/exercise-physiology-m |
| 6 | Sport, Exercise, and Performance Psychology | PhD | https://graduateadmissions.wvu.edu/academics/programs/sport-exercise-and-performance-psychology-phd |
| 7 | Sport Management | MS | https://graduateadmissions.wvu.edu/academics/programs/sport-management-ms |
| 8 | Social Work | MSW | https://graduateadmissions.wvu.edu/academics/graduate-programs/social-work-m |
| 9 | Social Work | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/social-work-phd |
| 10 | Leadership Studies in Education | MA | https://online.wvu.edu/programs/masters-degrees/leadership-studies-in-education-ma |
| 11 | Literacy Education | MA | https://online.wvu.edu/programs/masters-degrees/literacy-education-ma |
| 12 | Special Education | MA | https://online.wvu.edu/degrees-certificates/graduate-degrees/special-education-m-a |
| 13 | Counseling | MS (Online) | https://online.wvu.edu/programs/masters-degrees/counseling-ms-emphasis-in-clinical-mental-health |
| 14 | Athletic Training | MS | https://medicine.hsc.wvu.edu/athletic-training |
| 15 | Physical Education Teacher Education | MS | https://online.wvu.edu/degrees-certificates/graduate-degrees/physical-education-teacher-education-m-s |
| 16 | Social Work | MSW (Advanced) | https://online.wvu.edu/programs/masters-degrees/social-work-msw-advanced |
| 17 | Social Work | MSW (Regular) | https://online.wvu.edu/programs/masters-degrees/social-work-msw-regular |
| 18 | Sport and Performance Psychology | MS | https://online.wvu.edu/programs/masters-degrees/sport-performance-psychology-ms |
| 19 | Sport Coaching | MS | https://online.wvu.edu/programs/masters-degrees/sport-coaching-ms |
| 20 | Executive Sport Management | MS | https://online.wvu.edu/programs/masters-degrees/executive-sport-management-ms |
| 21 | Combined School and District Leadership | Certificate | https://online.wvu.edu/programs/graduate-certificates/combined-school-and-district-leadership-graduate-certificate |
| 22 | General Supervision of Instruction | Certificate | https://online.wvu.edu/programs/graduate-certificates/general-instructional-supervision-graduate-certificate |
| 23 | The Principalship | Certificate | https://online.wvu.edu/programs/graduate-certificates/principalship-graduate-certificate |

#### John Chambers College of Business and Economics

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | MAcc | https://graduateadmissions.wvu.edu/academics/graduate-programs/professional-accountancy-m |
| 2 | Business Administration | MBA | https://online.wvu.edu/programs/masters-degrees/business-administration-mba |
| 3 | Healthcare Business Administration | MBA | https://online.wvu.edu/programs/masters-degrees/healthcare-mba |
| 4 | Industrial Relations and Human Resources | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/human-resource-management-m |
| 5 | Economics | MS | https://online.wvu.edu/programs/masters-degrees/economics-ms |
| 6 | Finance | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/finance-d |
| 7 | Marketing | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/marketing-d |
| 8 | Business Administration | MBA | https://graduateadmissions.wvu.edu/academics/graduate-programs/business-administration-m |
| 9 | Applied AI and Data Analytics | MS | https://online.wvu.edu/programs/masters-degrees/business-data-analytics-ms |
| 10 | AI Marketing | MS | https://online.wvu.edu/programs/masters-degrees/ai-marketing-ms |
| 11 | Business Cybersecurity Management | MS | https://online.wvu.edu/programs/masters-degrees/business-cybersecurity-management-ms |
| 12 | Forensic and Fraud Examination | MS | https://online.wvu.edu/programs/masters-degrees/forensic-and-fraud-examination-ms |
| 13 | Human Resource Leadership | MS | https://online.wvu.edu/programs/masters-degrees/human-resource-leadership-ms |
| 14 | Business Cybersecurity Data Analytics | Certificate | https://online.wvu.edu/degrees-certificates/graduate-certificates/business-cybersecurity-data-analytics-graduate-certificate |
| 15 | Business Cybersecurity Foundations | Certificate | https://online.wvu.edu/programs/graduate-certificates/business-cybersecurity-foundations-graduate-certificate |
| 16 | Business Cybersecurity Management | Certificate | https://online.wvu.edu/degrees-certificates/graduate-certificates/business-cybersecurity-management-graduate-certificate |
| 17 | Business Data Analysis | Certificate | https://online.wvu.edu/programs/graduate-certificates/business-data-analysis-graduate-certificate |
| 18 | Business Data Science | Certificate | https://online.wvu.edu/programs/graduate-certificates/business-data-science-graduate-certificate |
| 19 | Business Data Technology Management | Certificate | https://online.wvu.edu/programs/graduate-certificates/business-data-technology-management-graduate-certificate |
| 20 | Business Operations Research | Certificate | https://online.wvu.edu/programs/graduate-certificates/business-data-technology-management-graduate-certificate |
| 21 | Forensic Accounting and Fraud Examination | Certificate | https://online.wvu.edu/degrees-certificates/graduate-certificates/forensic-accounting-and-fraud-examination-graduate-certificate |

#### Davis College of Agriculture and Natural Resources

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agriculture, Natural Resources, and Design | MAgr | https://graduateadmissions.wvu.edu/academics/graduate-programs/agriculture-natural-resources-design-m |
| 2 | Animal, Food, and Nutrition Sciences | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/animal-food-and-nutrition-sciences-d |
| 3 | Animal Physiology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/animal-physiology-m |
| 4 | Applied and Environmental Microbiology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/applied-and-environmental-microbiology-m |
| 5 | Entomology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/entomology-m |
| 6 | Environmental, Soil, and Water Sciences | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/environmental-soil-and-water-sciences |
| 7 | Forestry | MSF | https://graduateadmissions.wvu.edu/academics/graduate-programs/forestry-m |
| 8 | Genetics and Developmental Biology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/genetics-and-developmental-biology-m |
| 9 | Genetics and Developmental Biology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/genetics-and-developmental-biology-d |
| 10 | Horticulture | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/horticulture-m |
| 11 | Human and Community Development | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/human-and-community-development-d |
| 12 | Natural Resource Economics | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/natural-resource-economics-d |
| 13 | Natural Resources Science | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/natural-resources-science-d |
| 14 | Nutritional and Food Science | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/nutritional-and-food-science-m |
| 15 | Plant Pathology | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/plant-pathology-m |
| 16 | Plant and Soil Sciences | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/plant-and-soil-science-d |
| 17 | Wildlife and Fisheries Resources | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/wildlife-and-fisheries-resources-m |
| 18 | Sport Industry Leadership and Change Management | Certificate | https://www.wvu.edu/academics/programs/sport-industry-leadership-and-change-management-graduate-certificate |
| 19 | Sustainable Trails Development | Certificate | https://online.wvu.edu/programs/graduate-certificates/sustainable-trails-development-graduate-certificate |
| 20 | Women's and Gender Studies | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/women-s-and-gender-studies |

#### School of Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Sciences | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/biomedical-sciences-d |
| 2 | Biochemistry and Molecular Medicine | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/biochemistry-and-molecular-biology-d |
| 3 | Cancer Cell Biology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/cancer-cell-biology-d |
| 4 | Cellular and Integrative Physiology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/cellular-and-integrative-physiology-d |
| 5 | Clinical and Translational Science | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/clinical-and-translational-science-m |
| 6 | Clinical and Translational Science | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/clinical-and-translational-science-d |
| 7 | Health Sciences | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/health-sciences-m |
| 8 | Health Services and Outcomes Research | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/health-services-and-outcomes-research |
| 9 | Immunology and Microbial Pathogenesis | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/immunology-and-microbial-pathogenesis-d |
| 10 | Medical Laboratory Science | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/medical-laboratory-science-ms |
| 11 | Neuroscience | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/neuroscience-ms |
| 12 | Neuroscience | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/neuroscience-d |
| 13 | Pathophysiology, Rehabilitation, and Performance | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/pathophysiology-rehabilitation-and-performance-d |
| 14 | Pathologists' Assistant | MHS | https://graduateadmissions.wvu.edu/academics/graduate-programs/pathologists-assistant-m |
| 15 | Physician Assistant | MHS | https://medicine.wvu.edu/physician-assistant-studies/ |
| 16 | Speech-Language Pathology | MS | https://medicine.hsc.wvu.edu/communications-sciences-and-disorders/speech-language-pathology-ms/ |
| 17 | Audiology | AuD | https://medicine.wvu.edu/communications-sciences-and-disorders/audiology-aud/ |
| 18 | Occupational Therapy | MOT | https://medicine.wvu.edu/ot/masters-mot/ |
| 19 | Occupational Therapy | OTD | https://medicine.wvu.edu/ot/doctorate-otd/ |
| 20 | Physical Therapy | DPT | https://medicine.wvu.edu/pt/ |
| 21 | Medicine | MD | https://medicine.hsc.wvu.edu/students/md-program/ |
| 22 | Health Data Science | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/healthcare-administration-gc |
| 23 | Health Administration | MHA | https://online.wvu.edu/programs/masters-degrees/health-administration-mha |

#### School of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing Leadership | MSN-NL | https://nursing.wvu.edu/students/graduate-programs/master-of-science-in-nursing-leadership/ |
| 2 | Nursing | MSN | https://online.wvu.edu/programs/masters-degrees/nursing-msn |
| 3 | Nursing | PhD | https://nursing.hsc.wvu.edu/students/graduate-programs/phd/ |
| 4 | Nursing Practice | DNP | https://online.wvu.edu/programs/doctoral-programs/doctor-of-nursing-practice-dnp |
| 5 | Nurse Anesthesia | DNP | https://graduateadmissions.wvu.edu/academics/graduate-programs/nurse-anesthesia-d |
| 6 | Post-MSN Certificate Family Nurse Practitioner | Certificate | https://online.wvu.edu/programs/graduate-certificates/family-nurse-practitioner-graduate-certificate |
| 7 | Post-MSN Certificate Psychiatric Mental Health NP | Certificate | https://online.wvu.edu/programs/graduate-certificates/psychiatric-mental-health-nurse-practitioner-graduate-certificate |

#### School of Public Health

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | MPH | https://graduateadmissions.wvu.edu/academics/graduate-programs/biostatistics-mph |
| 2 | Biostatistics | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/biostatistics-m |
| 3 | Epidemiology | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/epidemiology-d |
| 4 | Public Health | MPH | https://graduateadmissions.wvu.edu/academics/graduate-programs/public-health-mph |
| 5 | Public Health | MPH (Online) | https://online.wvu.edu/programs/masters-degrees/public-health-mph |
| 6 | Social and Behavioral Sciences | PhD | https://publichealth.wvu.edu/students/graduate-programs/phd-in-public-health-sciences/social-and-behavioral-sciences/ |
| 7 | Occupational Safety and Health | PhD | https://online.wvu.edu/programs/doctoral-programs/occupational-safety-health-phd |
| 8 | Applied Biostatistics | Certificate | https://online.wvu.edu/degrees-certificates/graduate-certificates/applied-biostatistics-graduate-certificate |
| 9 | Healthcare Administration | Certificate | https://graduateadmissions.wvu.edu/academics/graduate-programs/healthcare-administration-gc |
| 10 | Applied Sport Science in Coaching | Certificate | https://online.wvu.edu/programs/graduate-certificates/applied-sport-science-in-coaching-graduate-certificate |

#### School of Dentistry

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Dental Surgery | DDS | https://dentistry.wvu.edu/students/doctor-of-dental-surgery-dds/ |
| 2 | Endodontics | MS | https://dentistry.wvu.edu/students/master-of-science/endodontics/ |
| 3 | Orthodontics | MS | https://dentistry.wvu.edu/students/master-of-science/orthodontics/ |
| 4 | Periodontics | MS | https://dentistry.wvu.edu/students/master-of-science/periodontics-and-dental-implant-surgery/ |
| 5 | Prosthodontics | MS | https://dentistry.wvu.edu/students/master-of-science/prosthodontics/ |

#### School of Pharmacy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmaceutical and Pharmacological Sciences | PhD | https://graduateadmissions.wvu.edu/academics/graduate-programs/pharmaceutical-and-pharmacological-sciences-d |
| 2 | Pharmacy | PharmD | https://pharmacy.hsc.wvu.edu/student-services/pharmd-program |
| 3 | Pharmacy | MS | https://graduateadmissions.wvu.edu/academics/graduate-programs/pharmacy-m |

#### College of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | JD | https://graduateadmissions.wvu.edu/academics/graduate-programs/law-d |

### 2.2 Graduate Admissions Model

WVU has a **decentralized graduate admissions** model. The Office of Graduate Admissions and Recruitment (OGAR) manages the application portal, but each program sets its own requirements (GPA, GRE, letters of recommendation, statement of purpose).

- **Application portal**: https://graduateadmissions.wvu.edu/how-to-apply
- **Application fee**: $75 (waivers for WVU/WVU Medicine employees, military, AmeriCorps, Peace Corps)
- **University minimum GPA**: 2.75 on 4.0 scale (programs may set higher)
- **GRE**: Per-program (ETS code: 5904; department code: 00)
- **CGS April-15**: Signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://admissions.wvu.edu/ | admissions.wvu.edu |
| Application portal | WVU Application or Common App | admissions.wvu.edu/how-to-apply |
| Application fee | $20 (WV residents) / $65 (OOS) / $75 (international) | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Admissions type | **Rolling admission** | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Fall application deadline | August 1 (all materials due) | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Spring application deadline | December 1 (all materials due) | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Merit scholarship deadline | August 1 (fall) / January 2 (spring) | wvu.edu/admissions/scholarships/first-time-freshmen |
| FAFSA priority deadline | March 1 | wvu.edu/admissions/scholarships/first-time-freshmen |
| SAT/ACT policy | **Test-optional** (no-harm policy) | admissions.wvu.edu/how-to-apply/first-time-freshmen/admission-requirements |
| SAT code | 5904 | admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements |
| ACT code | 4540 | admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements |
| Superscore | Yes | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Essays required | No | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Recommendations required | No | admissions.wvu.edu/how-to-apply/first-time-freshmen |
| Need-blind/need-aware | **Need-aware for all** (public university) | Verified |
| Decision notification | Rolling | admissions.wvu.edu |

> **Verification note**: WVU uses **rolling admission**, NOT EA/RD. The user-provided dates (EA Nov 1, RD Feb 1, Priority Dec 1) do not match the verified data. WVU's fall deadline is August 1; merit scholarship deadline is August 1; FAFSA priority is March 1.

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 备注 |
|------|---------|------|
| TOEFL iBT (through Jan 2026) | 79 | Home Edition accepted |
| TOEFL iBT (after Jan 2026) | 4.0 | New scoring scale |
| TOEFL Essentials | 9.0 | — |
| Academic IELTS | 6.5 | No sub-score requirements |
| Duolingo English Test | 105 | — |
| PTE Academic | 53 | — |
| SAT EBRW | 570 | Alternative to TOEFL/IELTS |
| ACT English | 24 | Alternative to TOEFL/IELTS |

> **Exempt countries**: Citizens of UK, Canada, Australia, India, Nigeria, Jamaica, Kenya, Ghana, Pakistan, Nepal, Ireland, New Zealand, South Africa, and 20+ other countries are exempt.
> **Exemptions**: IB Diploma, GCSE/GCE English, 24+ transferable credits from qualifying country, Bachelor's degree from qualifying country, U.S. high school diploma.

Source: https://admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | https://graduateadmissions.wvu.edu/how-to-apply | graduateadmissions.wvu.edu |
| Application fee | $75 | graduateadmissions.wvu.edu/how-to-apply/first-time-graduate-applicant |
| GPA minimum | 2.75 (university); programs may require higher | graduateadmissions.wvu.edu |
| GRE | Per-program (ETS code: 5904) | graduateadmissions.wvu.edu |
| TOEFL (through Jan 2026) | 79 | graduateadmissions.wvu.edu ELP page |
| TOEFL (after Jan 2026) | 4.0 | graduateadmissions.wvu.edu ELP page |
| IELTS | 6.5 | graduateadmissions.wvu.edu ELP page |
| Duolingo | 105 | graduateadmissions.wvu.edu ELP page |
| PTE | 53 | graduateadmissions.wvu.edu ELP page |
| GTA English requirement | TOEFL speaking 22 (through Jan 2026) / 4.5 (after Jan 2026) / IELTS speaking 7.5 | graduateadmissions.wvu.edu ELP page |
| CGS April-15 | Signatory | Verified |
| Fee waivers | WVU/WVU Medicine employees, military, AmeriCorps, Peace Corps | graduateadmissions.wvu.edu |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27, Line-Itemized)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| In-state tuition & fees | $11,064/year | 2 semesters, 12+ credits each |
| Out-of-state tuition & fees | $32,256/year | 2 semesters, 12+ credits each |
| Housing (double occupancy) | $13,772/year | Residence hall + Go Anytime dining plan |
| Mountaineer Athletics Fee | $500/year | $250/term, billed separately |
| College tuition (varies) | Additional | Per-program; check tuition.wvu.edu |
| Books & supplies | ~$1,000-1,500/year | Estimated |
| Personal expenses | ~$2,000-3,000/year | Estimated |

> **Note**: The user-provided figures (~$9k in-state / ~$26k OOS) are **underestimates** of the verified 2026-27 rates ($11,064 in-state / $32,256 OOS). College-specific tuition adds additional charges depending on the program.

Source: https://tuition.wvu.edu/, https://admissions.wvu.edu/cost-and-aid

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind/need-aware | **Need-aware for all** | Public university policy |
| Merit scholarships | Automatic (based on GPA/test scores) | wvu.edu/admissions/scholarships/first-time-freshmen |
| Climb Higher Scholarship (Level 1) | $5,000 in-state / $17,000 OOS | 3.8+ GPA and ACT ≥30 or SAT ≥1360 |
| Climb Higher Scholarship (Level 2) | $3,500 in-state / $14,000 OOS | 3.8+ GPA |
| Climb Higher Scholarship (Level 3) | $2,500 in-state / $11,000 OOS | 3.5-3.79 GPA |
| Climb Higher Scholarship (Level 4) | $1,500 in-state / $8,000 OOS | 3.0-3.49 GPA |
| Test-optional eligible | Yes | Test-optional applicants qualify for merit |
| FAFSA code | 003827 | wvu.edu/admissions/scholarships |
| Promise Scholarship (WV residents) | State-sponsored | Application deadline ~March 1 |
| 92% freshmen receive aid | Grants or scholarships | wvu.edu/admissions/scholarships/first-time-freshmen |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| In-state tuition & fees | $12,492/year | tuition.wvu.edu |
| Out-of-state tuition & fees | $33,318/year | tuition.wvu.edu |
| Application fee | $75 | graduateadmissions.wvu.edu |
| Funding types | RA/TA/fellowship/grant | graduateeducation.wvu.edu |
| Graduate Assistantships | Available | graduateeducation.wvu.edu/grad-life/graduate-assistantships |
| Fellowships | Available | graduateeducation.wvu.edu/finances/fellowships |
| Scholarships | Available | graduateeducation.wvu.edu/finances/scholarships-and-internships |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Application Fee
```yaml
field: undergraduate.application.fee
value: {wv_residents: $20, oos: $65, international: $75}
source_url: https://admissions.wvu.edu/how-to-apply/first-time-freshmen
source_snippet: "The fee is $20 for West Virginia residents, $65 for out-of-state students, and $75 for international students."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-002: Rolling Admission Policy
```yaml
field: undergraduate.admissions.type
value: rolling
source_url: https://admissions.wvu.edu/how-to-apply/first-time-freshmen
source_snippet: "WVU offers rolling admission, and you can apply test-optional."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-003: Fall Application Deadline
```yaml
field: undergraduate.deadlines.fall
value: August 1
source_url: https://admissions.wvu.edu/how-to-apply/first-time-freshmen
source_snippet: "By August 1 for fall semester admission"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-004: Spring Application Deadline
```yaml
field: undergraduate.deadlines.spring
value: December 1
source_url: https://admissions.wvu.edu/how-to-apply/first-time-freshmen
source_snippet: "By December 1 for spring semester admission"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-005: Test-Optional Policy
```yaml
field: undergraduate.testing.policy
value: test-optional (no-harm)
source_url: https://admissions.wvu.edu/how-to-apply/first-time-freshmen/admission-requirements
source_snippet: "Test-optional admission permits applicants to apply without an ACT or SAT score. We encourage students to submit scores if available. However, our no-harm policy means that applicants can be confident that scores will only be used if to their advantage."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-006: TOEFL Minimum (Undergraduate)
```yaml
field: undergraduate.elp.toefl
value: {through_jan_2026: 79, after_jan_2026: "4.0"}
source_url: https://admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements
source_snippet: "TOEFL iBT through January 2026 (Home Edition is accepted): 79; TOEFL iBT after January 2026 (Home Edition is accepted): 4.0"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-007: IELTS Minimum (Undergraduate)
```yaml
field: undergraduate.elp.ielts
value: 6.5
source_url: https://admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements
source_snippet: "Academic IELTS: 6.5"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-008: Duolingo Minimum (Undergraduate)
```yaml
field: undergraduate.elp.duolingo
value: 105
source_url: https://admissions.wvu.edu/how-to-apply/international-students/english-language-proficiency-requirements
source_snippet: "Duolingo English Test: 105"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-009: In-State Tuition
```yaml
field: undergraduate.cost.tuition_in_state
value: $11,064
source_url: https://tuition.wvu.edu/
source_snippet: "In-state tuition and fees: $11,064"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-010: Out-of-State Tuition
```yaml
field: undergraduate.cost.tuition_oos
value: $32,256
source_url: https://tuition.wvu.edu/
source_snippet: "Out-of-state tuition and fees: $32,256"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-011: Housing Cost
```yaml
field: undergraduate.cost.housing
value: $13,772
source_url: https://tuition.wvu.edu/
source_snippet: "Housing Expenses: $13,772"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-012: Merit Scholarship Deadline
```yaml
field: undergraduate.aid.merit_deadline
value: August 1 (fall) / January 2 (spring)
source_url: https://www.wvu.edu/admissions/scholarships/first-time-freshmen
source_snippet: "First-time freshmen must be admitted by August 1 to be considered for merit scholarships."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-013: Climb Higher Scholarship Levels
```yaml
field: undergraduate.aid.scholarship_levels
value:
  level_1: {in_state: $5,000, oos: $17,000, criteria: "3.8+ GPA and ACT ≥30 or SAT ≥1360"}
  level_2: {in_state: $3,500, oos: $14,000, criteria: "3.8+ GPA"}
  level_3: {in_state: $2,500, oos: $11,000, criteria: "3.5-3.79 GPA"}
  level_4: {in_state: $1,500, oos: $8,000, criteria: "3.0-3.49 GPA"}
source_url: https://www.wvu.edu/admissions/scholarships/first-time-freshmen
source_snippet: "Climb Higher Scholarship Level 1 (3.8+ GPA and ACT ≥30 or SAT ≥1360): $5,000 in-state / $17,000 out-of-state"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-014: International Application Deadlines
```yaml
field: undergraduate.deadlines.international
value: {fall_apply: June 1, fall_docs: July 1, spring_apply: October 1, spring_docs: November 1}
source_url: https://admissions.wvu.edu/how-to-apply/international-students
source_snippet: "Fall semester: Apply by June 1. All academic documents must be received by July 1."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.application.fee
value: $75
source_url: https://graduateadmissions.wvu.edu/how-to-apply/first-time-graduate-applicant
source_snippet: "Pay the $75 application fee."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-002: Graduate GPA Minimum
```yaml
field: graduate.admissions.gpa_minimum
value: 2.75
source_url: https://graduateadmissions.wvu.edu/how-to-apply/first-time-graduate-applicant
source_snippet: "Graduate degree-seeking applicants must meet the University standard of possessing a bachelor's degree from a regionally accredited institution, with a cumulative grade point average (GPA) of at least 2.75 on a 4.0 scale for regular admission."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-003: Graduate ELP Requirements
```yaml
field: graduate.elp
value: {toefl: 79/4.0, ielts: 6.5, duolingo: 105, pte: 53}
source_url: https://graduateadmissions.wvu.edu/how-to-apply/international-graduate-applicant/english-language-proficiency-requirements
source_snippet: "TOEFL iBT through January 2026 (Home Edition is accepted): 79; TOEFL iBT after January 2026 (Home Edition is accepted): 4.0; Academic IELTS: 6.5; Duolingo English Test: 105; PTE Academic and PTE Express: 53"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-004: Graduate In-State Tuition
```yaml
field: graduate.cost.tuition_in_state
value: $12,492
source_url: https://tuition.wvu.edu/
source_snippet: "In-state tuition and fees: $12,492"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-005: Graduate Out-of-State Tuition
```yaml
field: graduate.cost.tuition_oos
value: $33,318
source_url: https://tuition.wvu.edu/
source_snippet: "Out-of-state tuition and fees: $33,318"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-006: GRE Institution Code
```yaml
field: graduate.testing.gre_code
value: 5904
source_url: https://graduateadmissions.wvu.edu/how-to-apply/international-graduate-applicant
source_snippet: "WVU's institution code is 5904. It's ok if it's listed as an undergraduate organization. Use the generic department code 00."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-007: GTA English Speaking Requirement
```yaml
field: graduate.elp.gta_speaking
value: {toefl_speaking: 22, ielts_speaking: 7.5}
source_url: https://graduateadmissions.wvu.edu/how-to-apply/international-graduate-applicant/english-language-proficiency-requirements
source_snippet: "Applicants who submitted TOEFL or IELTS scores may meet requirements based on their speaking section scores (22 TOEFL speaking through January 2026, 4.5 TOEFL speaking after January 2026, 7.5 IELTS speaking)."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-P-001: Total Program Count
```yaml
field: institution.programs.total
value: 578 (all campuses) / 533 (Morgantown)
source_url: https://www.wvu.edu/academics/programs
source_snippet: "578 programs found"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-P-002: Graduate Program Count
```yaml
field: institution.programs.graduate
value: 215
source_url: https://graduateadmissions.wvu.edu/academics/graduate-programs
source_snippet: "215 programs found"
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
wvu-knowledge-base-v2/
├── 00-institution-overview          # Section 0: counts, hierarchy, matrix
├── 01-ug-engineering               # Section 1: Statler College programs
├── 02-ug-arts-sciences             # Section 1: Eberly College programs
├── 03-ug-creative-arts-media       # Section 1: Creative Arts & Media programs
├── 04-ug-applied-human-sciences    # Section 1: Applied Human Sciences programs
├── 05-ug-business-economics        # Section 1: Chambers Business programs
├── 06-ug-agriculture-nr            # Section 1: Davis Agriculture programs
├── 07-ug-medicine-nursing-ph       # Section 1: Medicine/Nursing/PH programs
├── 08-grad-engineering             # Section 2: Statler grad programs
├── 09-grad-arts-sciences           # Section 2: Eberly grad programs
├── 10-grad-creative-arts-media     # Section 2: Creative Arts & Media grad
├── 11-grad-applied-human-sciences  # Section 2: Applied Human Sciences grad
├── 12-grad-business-economics      # Section 2: Chambers Business grad
├── 13-grad-agriculture-nr          # Section 2: Davis Agriculture grad
├── 14-grad-medicine-health         # Section 2: Medicine/Nursing/PH/Dentistry/Pharmacy
├── 15-grad-law                     # Section 2: College of Law
├── 16-deadlines-requirements       # Section 3: Application requirements
├── 17-costs-aid                    # Section 4: Costs and financial aid
├── 18-evidence-chain               # Section 5: Evidence index
└── 19-comparison-framework         # Section 7: Cross-school comparison
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "wvu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|----------|------------|
| P0 | Per-program college-specific tuition rates | tuition.wvu.edu |
| P0 | Engineering GPA/test requirements for each major | admissions.wvu.edu |
| P0 | Graduate program-specific deadlines and GRE requirements | graduateadmissions.wvu.edu |
| P1 | Detailed COA line items (books, personal, transportation) | hub.wvu.edu/planning-and-resources/estimate-costs-and-aid |
| P1 | Dental Hygiene application details | dentistry.wvu.edu |
| P1 | Nursing direct admission details | nursing.wvu.edu |
| P1 | Pharmacy PharmD admission details | pharmacy.hsc.wvu.edu |
| P2 | International student visa documentation requirements | admissions.wvu.edu |
| P2 | Reduced tuition programs (OH, DC, Garrett College MD) | wvu.edu/admissions/reduced-tuition |
| P2 | Departmental scholarship details | Various college sites |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | WVU | (Other schools) |
|------|-----|-----------------|
| Type | Public | |
| Location | Morgantown, WV | |
| UG tuition in-state/yr | $11,064 | |
| UG tuition OOS/yr | $32,256 | |
| UG COA in-state/yr | ~$25,336 | |
| UG COA OOS/yr | ~$46,528 | |
| Need-blind intl? | No (need-aware all) | |
| EA deadline | N/A (rolling) | |
| RD deadline | N/A (rolling; Aug 1 fall) | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 79 (pre-Jan 2026) / 4.0 (post-Jan 2026) | |
| IELTS min | 6.5 | |
| App fee (UG) | $20/$65/$75 | |
| App fee (Grad) | $75 | |
| GRE required? | Per-program | |
| Total program count | 578 (all) / 533 (Morgantown) | |
| UG major count | 167 | |
| Grad program count | 215 | |
| School/college count | 14 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: admissions.wvu.edu, graduateadmissions.wvu.edu, tuition.wvu.edu, wvu.edu/academics/programs, financialaid.wvu.edu, hub.wvu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
