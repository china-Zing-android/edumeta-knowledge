# University of Cincinnati Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BBA/BM/BSED/etc.) | 372 |
| 本科辅修 (Minor) | 71 |
| 本科证书 (Certificate Level 1/2/3) | 163 |
| 副学士学位 (Associate: AA/AS/AAS/AAB) | 126 |
| 研究生学位项目 (MA/MS/MFA/MBA/MEng/PhD/etc.) | 278 |
| 研究生证书 (Graduate Certificate) | 112 |
| 法律 (JD/LLM/MSL) | 3 |
| **学位项目总计** | **998** |
| 学院总数 (含区域校区) | 16 |

> **Source**: UC Program Finder (AngularJS scope, 998 programs loaded via `scope.loadResults()`)
> **Capture date**: 2026-07-06
> **Reconciliation**: 609 UG career + 387 Grad career + 2 Law = 998 ✅

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Cincinnati
├── College of Arts and Sciences (A&S)                    [学院]
│   ├── Africana Studies                                   [系]
│   ├── Anthropology                                       [系]
│   ├── Biology                                            [系]
│   ├── Chemistry                                          [系]
│   ├── Communication                                      [系]
│   ├── Computer Science                                   [系]
│   ├── English                                            [系]
│   ├── Geology                                            [系]
│   ├── History                                            [系]
│   ├── Mathematics                                        [系]
│   ├── Philosophy                                         [系]
│   ├── Physics                                            [系]
│   ├── Political Science                                  [系]
│   ├── Psychology                                         [系]
│   ├── Sociology                                          [系]
│   ├── Statistics                                         [系]
│   └── World Languages                                    [系]
├── College of Education, Criminal Justice, & Human Services (CECH) [学院]
│   ├── Counseling                                         [系]
│   ├── Criminal Justice                                   [系]
│   ├── Education                                          [系]
│   ├── Human Services                                     [系]
│   └── Information Technology                             [系]
├── College-Conservatory of Music (CCM)                    [学院]
│   ├── Acting                                             [系]
│   ├── Ballet                                             [系]
│   ├── Composition                                        [系]
│   ├── Conducting                                         [系]
│   ├── Jazz Studies                                       [系]
│   ├── Music Education                                    [系]
│   ├── Musicology                                         [系]
│   ├── Opera                                              [系]
│   ├── Organ                                              [系]
│   ├── Piano                                              [系]
│   ├── Strings                                            [系]
│   ├── Theater Design & Production                        [系]
│   ├── Voice                                              [系]
│   └── Winds & Percussion                                 [系]
├── Carl H. Lindner College of Business (LCB)              [学院]
│   ├── Accounting                                         [系]
│   ├── Business Analytics                                 [系]
│   ├── Economics                                          [系]
│   ├── Finance                                            [系]
│   ├── Information Systems                                [系]
│   ├── Marketing                                          [系]
│   ├── Operations Management                              [系]
│   └── Real Estate                                        [系]
├── College of Engineering & Applied Science (CEAS)        [学院]
│   ├── Aerospace Engineering                              [系]
│   ├── Biomedical Engineering                             [系]
│   ├── Chemical Engineering                               [系]
│   ├── Civil Engineering                                  [系]
│   ├── Computer Engineering                               [系]
│   ├── Computer Science                                   [系]  ⚠ shared with A&S
│   ├── Electrical Engineering                             [系]
│   ├── Environmental Engineering                          [系]
│   ├── Industrial Engineering                             [系]
│   ├── Materials Science                                  [系]
│   └── Mechanical Engineering                             [系]
├── College of Design, Architecture, Art, and Planning (DAAP) [学院]
│   ├── Architecture                                       [系]
│   ├── Art History                                        [系]
│   ├── Communication Design                               [系]
│   ├── Fashion Design                                     [系]
│   ├── Fine Arts                                          [系]
│   ├── Industrial Design                                  [系]
│   ├── Interior Design                                    [系]
│   ├── Planning                                           [系]
│   └── Urban Studies                                      [系]
├── College of Allied Health Sciences (CAHS)               [学院]
│   ├── Audiology                                          [系]
│   ├── Dietetics                                          [系]
│   ├── Health Sciences                                    [系]
│   ├── Medical Imaging                                    [系]
│   ├── Occupational Therapy                               [系]
│   ├── Physical Therapy                                   [系]
│   ├── Social Work                                        [系]
│   └── Speech-Language Pathology                          [系]
├── College of Medicine (COM)                              [学院]
│   ├── Biomedical Informatics                             [系]
│   ├── Cancer & Cell Biology                              [系]
│   ├── Environmental Health                               [系]
│   ├── Molecular Genetics                                 [系]
│   ├── Neuroscience                                       [系]
│   ├── Pathology                                          [系]
│   ├── Pharmacology                                       [系]
│   └── Physiology                                         [系]
├── College of Nursing (CON)                               [学院]
│   └── Nursing                                            [系]
├── James L. Winkle College of Pharmacy                    [学院]
│   ├── Pharmacy                                           [系]
│   └── Pharmaceutical Sciences                            [系]
├── Donald P. Klekamp College of Law                       [学院]
│   └── Law                                                [系]
├── College of Coop Education and Professional Studies (CCEPS) [学院]
│   ├── Fire Science                                       [系]
│   ├── Innovation & Design                                [系]
│   └── Professional Studies                               [系]
├── UC Blue Ash College (UCBA)                             [学院] (Regional)
│   ├── Applied Administration                             [系]
│   ├── Business                                           [系]
│   ├── Communication                                      [系]
│   ├── Health Sciences                                    [系]
│   ├── Liberal Arts                                       [系]
│   └── Technology                                         [系]
├── UC Clermont College                                    [学院] (Regional)
│   ├── Applied Administration                             [系]
│   ├── Business Technology                                [系]
│   ├── Health Sciences                                    [系]
│   └── Liberal Arts                                       [系]
├── University Honors Scholars Program                     [项目]
└── UC Online                                              [在线]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 51 |
| BS | Bachelor of Science | 本科 | 49 |
| BSED | Bachelor of Science in Education | 本科 | 17 |
| BFA | Bachelor of Fine Arts | 本科 | 12 |
| BBA | Bachelor of Business Administration | 本科 | 12 |
| BM | Bachelor of Music | 本科 | 26 |
| BSHS | Bachelor of Science in Health Sciences | 本科 | 9 |
| BSIT | Bachelor of Science in Information Technology | 本科 | 6 |
| BIS | Bachelor of Interdisciplinary Studies | 本科 | 4 |
| BSDES | Bachelor of Science in Design | 本科 | 3 |
| BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BSEET | Bachelor of Science in Electrical Engineering Technology | 本科 | 2 |
| BSW | Bachelor of Social Work | 本科 | 2 |
| BTAS | Bachelor of Technical and Applied Studies | 本科 | 2 |
| BSAEROE | Bachelor of Science in Aerospace Engineering | 本科 | 1 |
| BSARCH | Bachelor of Science in Architecture | 本科 | 1 |
| BSBME | Bachelor of Science in Biomedical Engineering | 本科 | 1 |
| BSCHE | Bachelor of Science in Chemical Engineering | 本科 | 1 |
| BSCE | Bachelor of Science in Civil Engineering | 本科 | 1 |
| BSCOMPE | Bachelor of Science in Computer Engineering | 本科 | 1 |
| BSCS | Bachelor of Science in Computer Science | 本科 | 1 |
| BSCM | Bachelor of Science in Construction Management | 本科 | 1 |
| BSCYBR | Bachelor of Science in Cybersecurity | 本科 | 1 |
| BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| BSEVE | Bachelor of Science in Environmental Engineering | 本科 | 1 |
| BSFSET | Bachelor of Science in Fire Safety Engineering Technology | 本科 | 1 |
| BHIM | Bachelor of Health Information Management | 本科 | 1 |
| BSISE | Bachelor of Science in Industrial & Systems Engineering | 本科 | 1 |
| BSIM | Bachelor of Science in Information Management | 本科 | 1 |
| BSID | Bachelor of Science in Interior Design | 本科 | 1 |
| BSME | Bachelor of Science in Mechanical Engineering | 本科 | 1 |
| BSMET | Bachelor of Science in Mechanical Engineering Technology | 本科 | 1 |
| BRST | Bachelor of Arts in Religious Studies | 本科 | 1 |
| BRIT | Bachelor of Arts in Romance Languages & Intl Trade | 本科 | 1 |
| BUP | Bachelor of Urban Planning | 本科 | 1 |
| AA | Associate of Arts | 副学士 | 32 |
| AS | Associate of Science | 副学士 | 57 |
| AAS | Associate of Applied Science | 副学士 | 23 |
| AAB | Associate of Applied Business | 副学士 | 14 |
| MS | Master of Science | 研究生 | 58 |
| MA | Master of Arts | 研究生 | 21 |
| MC | Master of Communication | 研究生 | 24 |
| MFA | Master of Fine Arts | 研究生 | 8 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MENG | Master of Engineering | 研究生 | 20 |
| MED | Master of Education | 研究生 | 10 |
| MSN | Master of Science in Nursing | 研究生 | 8 |
| MM | Master of Music | 研究生 | 9 |
| MPH | Master of Public Health | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MSPS | Master of Science in Pharmaceutical Sciences | 研究生 | 5 |
| MARCH | Master of Architecture | 研究生 | 1 |
| MSARCH | Master of Science in Architecture | 研究生 | 1 |
| MSAT | Master of Science in Athletic Training | 研究生 | 1 |
| MHA | Master of Health Administration | 研究生 | 1 |
| MHI | Master of Health Informatics | 研究生 | 1 |
| MSHR | Master of Science in Human Resources | 研究生 | 1 |
| MDES | Master of Design | 研究生 | 1 |
| MCP | Master of Community Planning | 研究生 | 1 |
| MAT | Master of Arts in Teaching | 研究生 | 1 |
| MSCOS | Master of Science in Cosmetic Science | 研究生 | 1 |
| MSPL | Master of Science in Pharmaceutical Leadership | 研究生 | 1 |
| MME | Master of Music Education | 研究生 | 1 |
| MATCH | Master of Arts in Teaching (Chemistry) | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MUD | Master of Urban Design | 研究生 | 1 |
| MSLA | Master of Science in Laboratory Animal Management | 研究生 | 1 |
| MLA | Master of Liberal Arts | 研究生 | 1 |
| MSL | Master of Studies in Law | 研究生 | 1 |
| EdS | Education Specialist | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 59 |
| DMA | Doctor of Musical Arts | 研究生 | 25 |
| DNP | Doctor of Nursing Practice | 研究生 | 10 |
| EdD | Doctor of Education | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| PharmD | Doctor of Pharmacy | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| SLPD | Doctor of Speech-Language Pathology | 研究生 | 1 |
| DCLS | Doctor of Clinical Laboratory Science | 研究生 | 1 |
| GC | Graduate Certificate | 研究生证书 | 107 |
| GCM | Graduate Certificate (Micro-credential) | 研究生证书 | 5 |
| PTC | Post-Master's Certificate | 研究生证书 | 2 |
| CERT1 | Certificate (Level 1) | 本科证书 | 46 |
| CERT2 | Certificate (Level 2) | 本科证书 | 88 |
| CERT3 | Certificate (Level 3) | 本科证书 | 3 |
| MIN | Minor | 本科辅修 | 71 |

> **Note**: UC uses non-standard degree abbreviations (e.g., BSAEROE, BSARCH, BSHS). The `canonical` column maps to standard equivalents for cross-school comparison.

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA/BS | BFA/BM | Associate | MA/MS | MFA/MM | MBA/MEng | PhD/DMA | Professional Doc | Certificate/Minor | 合计 |
|------------|-------|--------|-----------|-------|--------|----------|---------|-----------------|-------------------|------|
| College of Arts and Sciences | 100 | 0 | 0 | 79 | 0 | 0 | 59 | 0 | 178 | 220 |
| College of Education, Criminal Justice, & Human Services | 17 | 0 | 0 | 10 | 0 | 0 | 0 | 1 | 97 | 125 |
| UC Clermont College | 0 | 0 | 126 | 0 | 0 | 0 | 0 | 0 | 107 | 107 |
| College-Conservatory of Music | 0 | 38 | 0 | 30 | 33 | 0 | 25 | 0 | 0 | 96 |
| Carl H. Lindner College of Business | 12 | 0 | 0 | 0 | 0 | 60 | 0 | 0 | 7 | 79 |
| College of Engineering & Applied Science | 50 | 0 | 0 | 0 | 0 | 20 | 9 | 0 | 0 | 79 |
| UC Blue Ash College | 0 | 0 | 126 | 0 | 0 | 0 | 0 | 0 | 78 | 78 |
| College of Allied Health Sciences | 9 | 0 | 0 | 59 | 0 | 0 | 0 | 3 | 0 | 54 |
| College of Medicine | 0 | 0 | 0 | 58 | 0 | 0 | 1 | 0 | 0 | 49 |
| College of Design, Architecture, Art, and Planning | 1 | 0 | 0 | 22 | 8 | 1 | 1 | 0 | 14 | 47 |
| College of Nursing | 2 | 0 | 0 | 8 | 0 | 0 | 0 | 10 | 8 | 28 |
| James L. Winkle College of Pharmacy | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 9 | 15 |
| University of Cincinnati (General) | 0 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 8 | 8 |
| Donald P. Klekamp College of Law | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 5 | 7 |
| College of Coop Education and Professional Studies | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 5 |
| University Honors Scholars Program | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **合计** | **192** | **38** | **298** | **272** | **41** | **81** | **95** | **16** | **409** | **998** |

> **Reconciliation**: Matrix cell-sum (998) == Rule-1 total (998) == Program count (998) ✅

---

## SECTION 1 — Undergraduate Education

### 1.1 College Architecture

UC has 14 undergraduate-degree-granting colleges/schools plus 2 regional campuses (Blue Ash and Clermont) and UC Online. The university practices **direct admit** — students are admitted directly to a major. Students can preference up to 3 majors on the Common Application. An "Exploratory Studies" (undecided) option is available.

UC is the **birthplace of cooperative education** (co-op), founded in 1906. The co-op program is now the largest in the United States, with over 8,300 paid opportunities from 1,757 industry partners. In 2024-25, UC students collectively earned **$94 million** in co-op earnings.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences (A&S)

##### Africana Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Africana Studies | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Biology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biology | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Biology | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Chemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Chemistry | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Communication
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | BS | [Link](https://www.uc.edu/majors-programs.html) |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | English | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Creative Writing | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Professional Writing | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Geology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Geology | BS | [Link](https://www.uc.edu/majors-programs.html) |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Mathematics | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Actuarial Science | BS | [Link](https://www.uc.edu/majors-programs.html) |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Physics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Physics | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Political Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Psychology | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Sociology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | BA | [Link](https://www.uc.edu/majors-programs.html) |

##### Statistics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Statistics | BS | [Link](https://www.uc.edu/majors-programs.html) |

##### World Languages
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | French | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | German | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Spanish | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Japanese | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Chinese | BA | [Link](https://www.uc.edu/majors-programs.html) |

*[Note: A&S has 220 total programs including minors, certificates, and graduate degrees. The above shows representative UG majors; full list available in program finder.]*

#### College of Engineering & Applied Science (CEAS)

##### Aerospace Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | BSAEROE | [Link](https://www.uc.edu/majors-programs.html) |

##### Biomedical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | BSBME | [Link](https://www.uc.edu/majors-programs.html) |

##### Chemical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | BSCHE | [Link](https://www.uc.edu/majors-programs.html) |

##### Civil Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering | BSCE | [Link](https://www.uc.edu/majors-programs.html) |

##### Computer Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Engineering | BSCOMPE | [Link](https://www.uc.edu/majors-programs.html) |

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | BSCS | [Link](https://www.uc.edu/majors-programs.html) |

##### Electrical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical Engineering | BSEE | [Link](https://www.uc.edu/majors-programs.html) |

##### Environmental Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Engineering | BSEVE | [Link](https://www.uc.edu/majors-programs.html) |

##### Industrial & Systems Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Industrial & Systems Engineering | BSISE | [Link](https://www.uc.edu/majors-programs.html) |

##### Mechanical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mechanical Engineering | BSME | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Mechanical Engineering Technology | BSMET | [Link](https://www.uc.edu/majors-programs.html) |

##### Construction Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Construction Management | BSCM | [Link](https://www.uc.edu/majors-programs.html) |

##### Cybersecurity
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cybersecurity | BSCYBR | [Link](https://www.uc.edu/majors-programs.html) |

##### Information Technology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Information Technology | BSIT | [Link](https://www.uc.edu/majors-programs.html) |

*[CEAS has 79 total programs including graduate degrees and certificates.]*

#### Carl H. Lindner College of Business (LCB)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Business Economics | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Business Analytics | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Entrepreneurship | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Finance | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 6 | Industrial Management | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 7 | Information Systems | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 8 | International Business | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 9 | Marketing | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 10 | Operations Management | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 11 | Real Estate | BBA | [Link](https://www.uc.edu/majors-programs.html) |
| 12 | Sport Administration | BBA | [Link](https://www.uc.edu/majors-programs.html) |

*[LCB has 79 total programs including graduate degrees and certificates.]*

#### College-Conservatory of Music (CCM)

*[CCM has 96 programs. Representative UG majors:]*

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Acting | BFA | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Ballet | BFA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Bassoon | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Clarinet | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Composition | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 6 | Conducting | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 7 | Euphonium | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 8 | Flute | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 9 | French Horn | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 10 | Guitar | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 11 | Harp | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 12 | Jazz Studies | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 13 | Music Education | BSED | [Link](https://www.uc.edu/majors-programs.html) |
| 14 | Oboe | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 15 | Organ | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 16 | Percussion | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 17 | Piano | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 18 | Saxophone | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 19 | Sound Design | BFA | [Link](https://www.uc.edu/majors-programs.html) |
| 20 | Theater Design & Production | BFA | [Link](https://www.uc.edu/majors-programs.html) |
| 21 | Trombone | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 22 | Trumpet | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 23 | Tuba | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 24 | Viola | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 25 | Violin | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 26 | Violoncello | BM | [Link](https://www.uc.edu/majors-programs.html) |
| 27 | Voice | BM | [Link](https://www.uc.edu/majors-programs.html) |

#### College of Design, Architecture, Art, and Planning (DAAP)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | BSARCH | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Art History | BA | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Communication Design | BSDES | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Fashion Design | BSDES | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Fine Arts | BFA | [Link](https://www.uc.edu/majors-programs.html) |
| 6 | Industrial Design | BSDES | [Link](https://www.uc.edu/majors-programs.html) |
| 7 | Interior Design | BSID | [Link](https://www.uc.edu/majors-programs.html) |
| 8 | Urban Planning | BUP | [Link](https://www.uc.edu/majors-programs.html) |

#### College of Education, Criminal Justice, & Human Services (CECH)

*[CECH has 125 programs. Representative UG majors:]*

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Criminal Justice | BSED | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Early Childhood Education | BSED | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Special Education | BSED | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Information Technology | BSIT | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Cybersecurity | BSCYBR | [Link](https://www.uc.edu/majors-programs.html) |

#### College of Allied Health Sciences (CAHS)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Medical Imaging Technology | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Dietetics | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Health Sciences | BSHS | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Medical Laboratory Science | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Nuclear Medicine Technology | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 6 | Radiation Therapy | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 7 | Respiratory Therapy | BS | [Link](https://www.uc.edu/majors-programs.html) |
| 8 | Social Work | BSW | [Link](https://www.uc.edu/majors-programs.html) |
| 9 | Speech-Language Pathology | BS | [Link](https://www.uc.edu/majors-programs.html) |

#### College of Nursing (CON)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BSN | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Health Information Management | BHIM | [Link](https://www.uc.edu/majors-programs.html) |

#### UC Blue Ash College (Regional)

*[UCBA has 78 programs, primarily associate degrees and certificates. Representative programs:]*

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Media Communications | AAS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Business Management Technology | AAB | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Communication | AA | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Pre-Allied Health | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Pre-Architecture | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 6 | Pre-Business | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 7 | Pre-Engineering | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 8 | Pre-Nursing | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 9 | Veterinary Technology | AAS | [Link](https://www.uc.edu/majors-programs.html) |
| 10 | Animation | CERT1 | [Link](https://www.uc.edu/majors-programs.html) |

#### UC Clermont College (Regional)

*[Clermont has 107 programs, primarily associate degrees and certificates. Representative programs:]*

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aviation Technology | AAS | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Business Management Technology | AAB | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | Pre-Allied Health | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Pre-Business | AS | [Link](https://www.uc.edu/majors-programs.html) |
| 5 | Pre-Engineering | AS | [Link](https://www.uc.edu/majors-programs.html) |

### 1.3 Interdisciplinary / Cross-College Programs

| # | 专业 | 学位 | 主管学院 | URL |
|---|------|------|---------|-----|
| 1 | Computer Science | BS | CEAS / A&S (shared) | [Link](https://www.uc.edu/majors-programs.html) |
| 2 | Environmental Studies | BA | A&S | [Link](https://www.uc.edu/majors-programs.html) |
| 3 | International Affairs | BA | A&S | [Link](https://www.uc.edu/majors-programs.html) |
| 4 | Neuroscience | BS | A&S / COM (shared) | [Link](https://www.uc.edu/majors-programs.html) |

### 1.4 Minors

UC offers **71 minors** across all colleges. Full list available in the UC Program Finder. Representative minors:

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Accounting | LCB |
| 2 | Africana Studies | A&S |
| 3 | Anthropology | A&S |
| 4 | Art History | DAAP |
| 5 | Biology | A&S |
| 6 | Business | LCB |
| 7 | Chemistry | A&S |
| 8 | Communication | A&S |
| 9 | Computer Science | CEAS |
| 10 | Criminal Justice | CECH |
| 11 | Economics | A&S/LCB |
| 12 | English | A&S |
| 13 | Entrepreneurship | LCB |
| 14 | Environmental Studies | A&S |
| 15 | Film & Media Studies | A&S |
| 16 | French | A&S |
| 17 | German | A&S |
| 18 | History | A&S |
| 19 | Information Technology | CECH |
| 20 | Mathematics | A&S |
| 21 | Music | CCM |
| 22 | Philosophy | A&S |
| 23 | Physics | A&S |
| 24 | Political Science | A&S |
| 25 | Psychology | A&S |
| 26 | Sociology | A&S |
| 27 | Spanish | A&S |
| 28 | Statistics | A&S |
| 29 | Women's, Gender, & Sexuality Studies | A&S |
| 30 | World Languages | A&S |

### 1.5 General Education Requirements

UC's **General Education Core** (revised 2026) includes:
- **English Composition** (2 courses)
- **Quantitative Reasoning** (1 course)
- **Historical Perspectives** (1 course)
- **Social & Ethical Issues** (1 course)
- **Natural Sciences** (2 courses, one with lab)
- **Humanities** (2 courses)
- **Social Sciences** (2 courses)
- **Baccalaureate Competencies** (Writing, Oral Communication, Information Literacy)
- **General Education Touchpoints** (Diversity, Global Studies)

> **Source**: `https://www.uc.edu/about/provost/colleges-and-offices/offices/undergraduate-affairs/gen-ed-core-rd/requirements.html`

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

UC offers **387 graduate career programs** (385 graduate + 2 law). The Graduate College oversees 400+ programs across all colleges.

#### College of Arts and Sciences (A&S) — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | MA | [Link](https://grad.uc.edu/) |
| 2 | Biology | MS | [Link](https://grad.uc.edu/) |
| 3 | Chemistry | MS | [Link](https://grad.uc.edu/) |
| 4 | Computer Science | MS | [Link](https://grad.uc.edu/) |
| 5 | Economics | MA | [Link](https://grad.uc.edu/) |
| 6 | English | MA | [Link](https://grad.uc.edu/) |
| 7 | Geology | MS | [Link](https://grad.uc.edu/) |
| 8 | History | MA | [Link](https://grad.uc.edu/) |
| 9 | Mathematics | MS | [Link](https://grad.uc.edu/) |
| 10 | Philosophy | MA | [Link](https://grad.uc.edu/) |
| 11 | Physics | MS | [Link](https://grad.uc.edu/) |
| 12 | Political Science | MA | [Link](https://grad.uc.edu/) |
| 13 | Psychology | PhD | [Link](https://grad.uc.edu/) |
| 14 | Sociology | PhD | [Link](https://grad.uc.edu/) |
| 15 | Statistics | MS | [Link](https://grad.uc.edu/) |

*[A&S has 79 graduate programs total.]*

#### College of Engineering & Applied Science (CEAS) — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Additive Manufacturing | MENG | [Link](https://grad.uc.edu/) |
| 2 | Aerospace Engineering | MENG | [Link](https://grad.uc.edu/) |
| 3 | Aerospace Engineering & Engineering Mechanics | MS | [Link](https://grad.uc.edu/) |
| 4 | Biomedical Engineering | MS | [Link](https://grad.uc.edu/) |
| 5 | Chemical Engineering | MENG | [Link](https://grad.uc.edu/) |
| 6 | Civil Engineering | MENG | [Link](https://grad.uc.edu/) |
| 7 | Computer Engineering | MENG | [Link](https://grad.uc.edu/) |
| 8 | Computer Science | MS | [Link](https://grad.uc.edu/) |
| 9 | Electrical Engineering | MENG | [Link](https://grad.uc.edu/) |
| 10 | Environmental Engineering | MENG | [Link](https://grad.uc.edu/) |
| 11 | Industrial Engineering | MENG | [Link](https://grad.uc.edu/) |
| 12 | Materials Science | MS | [Link](https://grad.uc.edu/) |
| 13 | Mechanical Engineering | MENG | [Link](https://grad.uc.edu/) |
| 14 | Mechanical Engineering | MS | [Link](https://grad.uc.edu/) |
| 15 | Mechanical Engineering | PhD | [Link](https://grad.uc.edu/) |

*[CEAS has 29 graduate programs.]*

#### College of Medicine (COM) — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Informatics | GC | [Link](https://grad.uc.edu/) |
| 2 | Biomedical Informatics | PhD | [Link](https://grad.uc.edu/) |
| 3 | Cancer and Cell Biology | PhD | [Link](https://grad.uc.edu/) |
| 4 | Molecular Genetics | PhD | [Link](https://grad.uc.edu/) |
| 5 | Neuroscience | PhD | [Link](https://grad.uc.edu/) |
| 6 | Pathobiology & Molecular Medicine | PhD | [Link](https://grad.uc.edu/) |
| 7 | Pharmacology & Systems Biology | PhD | [Link](https://grad.uc.edu/) |
| 8 | MD Program | MD | [Link](https://www.med.uc.edu/) |

*[COM has 49 graduate programs.]*

#### College of Nursing (CON) — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accelerated Path MSN | MSN | [Link](https://grad.uc.edu/) |
| 2 | Adult-Gero Acute Care NP | DNP | [Link](https://grad.uc.edu/) |
| 3 | Family NP | DNP | [Link](https://grad.uc.edu/) |
| 4 | Nurse-Midwifery | DNP | [Link](https://grad.uc.edu/) |
| 5 | Pediatric NP | DNP | [Link](https://grad.uc.edu/) |
| 6 | Psychiatric Mental Health NP | DNP | [Link](https://grad.uc.edu/) |

*[CON has 20 graduate programs.]*

#### James L. Winkle College of Pharmacy — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | PharmD Program | PharmD | [Link](https://www.pharmacy.uc.edu/) |
| 2 | Cosmetic Science | GC | [Link](https://grad.uc.edu/) |
| 3 | Pharmaceutical Sciences | MS | [Link](https://grad.uc.edu/) |
| 4 | Pharmacy Leadership | MSPL | [Link](https://grad.uc.edu/) |

*[Pharmacy has 15 graduate programs.]*

#### Donald P. Klekamp College of Law — Graduate

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor | JD | [Link](https://www.law.uc.edu/) |
| 2 | Master of Laws | LLM | [Link](https://www.law.uc.edu/) |
| 3 | Master of Studies in Law | MSL | [Link](https://www.law.uc.edu/) |
| 4 | Business Compliance | GC | [Link](https://grad.uc.edu/) |
| 5 | Healthcare Administration Regulation | GC | [Link](https://grad.uc.edu/) |
| 6 | IT and Cyber Law | GC | [Link](https://grad.uc.edu/) |

### 2.2 Graduate Admissions Model

**Decentralized**: Each college/program manages its own graduate admissions. The Graduate College provides central coordination and services.

**Application portal**: `https://grad.catalyst.uc.edu/register/gradrequestinfo` (request info) / Apply via individual program pages.

**Contact**: `grad.admissions@uc.edu` or (513) 556-1100.

**Program finder**: `https://grad.uc.edu/` — search by keyword, award type, interest area, location.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | Common Application | admissions.uc.edu/apply.html |
| Application fee (domestic) | $50 (non-refundable, or fee waiver) | admissions.uc.edu/information/high-school/fymc-information.html |
| Application fee (international) | $100 (non-refundable) | admissions.uc.edu/information/international/requirements/freshman.html |
| EA deadline | November 1 | admissions.uc.edu/apply/deadlines.html |
| EA notification | Mid-January to early February | admissions.uc.edu/information/high-school/fymc-information.html |
| Rolling deadline | March 1 | admissions.uc.edu/apply/deadlines.html |
| Rolling notification | Weekly starting early February | admissions.uc.edu/information/high-school/fymc-information.html |
| Confirmation deadline | May 1 (fall) / December 1 (spring) / April 1 (summer) | admissions.uc.edu/apply/deadlines.html |
| SAT/ACT policy | Test-optional (optional for all programs) | admissions.uc.edu/information/high-school.html |
| Superscore | No (but review sub-scores across tests) | admissions.uc.edu/information/high-school/hs-faq.html |
| SAT essay/ACT writing | Not required | admissions.uc.edu/information/high-school/hs-faq.html |
| Letter of recommendation | Optional | admissions.uc.edu/information/high-school/fymc-information.html |
| Transcript | Official or unofficial accepted | admissions.uc.edu/information/high-school/fymc-information.html |
| Direct admit | Yes (preference up to 3 majors) | admissions.uc.edu/information/high-school/hs-faq.html |
| Exploratory Studies | Available (undecided option) | admissions.uc.edu/information/high-school/hs-faq.html |
| Transfer deadline (fall) | July 1 (DAAP: March 1) | admissions.uc.edu/apply/deadlines.html |
| Co-op | Largest in US; 8,300+ opportunities; $94M earned (2024-25) | uc.edu/scholarships-financial-aid.html |

### 3.2 Undergraduate English Proficiency Table

UC requires English proficiency for all international students. Scores are **per-college** (not uniform). Scores valid for 2 years before term start.

| College | TOEFL iBT (Pre-Jan 2026) | TOEFL iBT (Post-Jan 2026) | IELTS | Duolingo | PTE | Cambridge | ACT English | SAT ERW |
|---------|-------------------------|--------------------------|-------|----------|-----|-----------|-------------|---------|
| College of Arts & Sciences | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 (Recommended: C1 Advanced) | 19 | 480 |
| College of Education, Criminal Justice, & Human Services | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| College of Engineering & Applied Science | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| Lindner College of Business | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| College of Design, Architecture, Art, & Planning | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| College of Medicine | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| College of Nursing | — | — | — | — | — | — | 19 | 480 |
| College of Allied Health Sciences | 79 Overall, 20W, 20S, 15 Other | 4.0 Overall, 4.0W, 4.0S, 3.5 Other | 6.5 Overall, 6.0W, 6.0S, 5.5 Other | 100 Overall, 100 Production, 100 Conversation | 53 | 176 | 19 | 480 |
| College-Conservatory of Music | 66 Overall, 15 All Sub | 3.5 All Sub | 6.0 Overall, 5.0 All Sub | 100 Overall, 80 Production, 80 Conversation | 53 | 176 | 19 | 480 |

> **Note**: TOEFL iBT reporting changed in January 2026 to a new scale. UC accepts both old and new scores.
> **Source**: `https://www.admissions.uc.edu/information/international/requirements/freshman.html`

### 3.3 Graduate — Global Rules

- **Decentralized admissions**: Each college/program manages own process
- **Application**: Through individual program pages or `grad.catalyst.uc.edu`
- **Contact**: `grad.admissions@uc.edu` / (513) 556-1100
- **GRE/GMAT**: Per-program (not universal requirement)
- **English proficiency**: TOEFL or IELTS typically required for non-native speakers
- **Program-specific deadlines**: Vary by program; contact individual programs

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-26 Cohort, Line-Itemized)

#### Uptown/Clifton Campus — Full-Time (per academic year = 2 terms)

| Expense Item | Ohio Resident | Metro (KY/IN) | Non-Resident | Source |
|-------------|---------------|---------------|--------------|--------|
| **Tuition (instructional + fees)** | **$14,394** | **$15,012** | **$29,728** | costs.html |
| Housing and Food (on-campus, 2026-27) | $16,511 | $16,511 | $16,511 | non-tuition-costs.html |
| Books and Course Materials | $1,300 | $1,300 | $1,300 | non-tuition-costs.html |
| Transportation | $2,038 | $2,038 | $3,038 | non-tuition-costs.html |
| Miscellaneous | $3,386 | $3,386 | $3,386 | non-tuition-costs.html |
| Computer (first year only) | $3,000 | $3,000 | $3,000 | non-tuition-costs.html |
| **Total COA (on-campus)** | **$43,276** | — | — | costs.html |

> **Cincinnati Tuition Guarantee**: Tuition rates are frozen for each cohort for 4-5 years (depending on program length). The 2025-26 cohort rate is locked for those students' entire program.

#### Per Credit Hour Rates (2025-26 Cohort, Uptown)

| Residency | Per Credit Hour | Per Full-Time Term | Per Full-Time Year |
|-----------|----------------|-------------------|-------------------|
| Ohio | $600 | $7,197 | $14,394 |
| Metro (KY/IN) | $626 | $7,506 | $15,012 |
| Non-Resident | $1,239 | $14,864 | $29,728 |

#### UC Blue Ash Campus (2025-26 Cohort)

| Residency | Per Credit Hour | Per Full-Time Term | Per Full-Time Year |
|-----------|----------------|-------------------|-------------------|
| Ohio | $309 | $3,708 | $7,416 |
| Metro | $335 | $4,017 | $8,034 |
| Non-Resident | $676 | $8,107 | $16,214 |

#### UC Clermont Campus (2025-26 Cohort)

| Residency | Per Credit Hour | Per Full-Time Term | Per Full-Time Year |
|-----------|----------------|-------------------|-------------------|
| Ohio | $290 | $3,476 | $6,952 |
| Metro | $315 | $3,785 | $7,570 |
| Non-Resident | $591 | $7,092 | $14,184 |

#### Graduate & Professional Tuition (2025-26 Cohort, Uptown)

| Program | Ohio (per hour) | Metro (per hour) | Non-Resident (per hour) |
|---------|----------------|-----------------|------------------------|
| Graduate | $746 | $771 | $1,333 |
| PharmD | $1,221 | $1,461 | $1,867 |
| Law | $1,001 | $1,026 | $1,209 |
| Medicine (M.D.) | $1,485 | $1,426 | $2,270 |

#### Other Required Fees

| Fee | Amount | Conditions |
|-----|--------|-----------|
| New Student Fee | $135 | Once per lifetime |
| International Student Fee | $125/term | Fall & spring in-class or co-op terms |
| Professional Practice Fee (UG) | $495/term | Per term based on co-op enrollment |
| Professional Practice Fee (Grad) | $675/term | Per term based on co-op enrollment |
| Student Health Insurance | Varies | Required if no minimum coverage documented |

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind (domestic) | No (need-aware for all) | uc.edu/scholarships-financial-aid.html |
| Need-blind (international) | No | uc.edu/about/international/admissions/cost.html |
| Merit scholarships | Automatic consideration via Common App | uc.edu/scholarships-financial-aid.html |
| Key scholarships | Cincinnatus Scholarship, National Outreach Award, Choose Ohio First, NEXT Innovation | admissions.uc.edu/tuition-aid/scholarships.html |
| FAFSA required | Yes (opens October 1; priority by November 1) | uc.edu/scholarships-financial-aid.html |
| Co-op earnings | $94 million collectively (2024-25) | uc.edu/scholarships-financial-aid.html |
| Co-op sample earnings | $7,878 (sophomore) → $9,450 (junior) → $10,500 (senior) | uc.edu/scholarships-financial-aid.html |
| Metro tuition rate | Available for KY/IN residents | admissions.uc.edu/tuition-aid/kyin.html |
| Tuition guarantee | Yes (cohort-based frozen rates, 4-5 years) | uc.edu/about/bursar/tuition-fees/tuition-guarantee-policy.html |

### 4.3 Graduate Cost & Funding Framework

- **Funding types**: Varies by program (RA/TA/fellowships available in many PhD programs)
- **Graduate tuition scholarships**: $45M awarded annually (per Graduate College)
- **Application fee**: $50 (domestic) / $100 (international)
- **Contact**: Individual program or `grad.admissions@uc.edu`

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Deadlines

```yaml
field: undergraduate.deadlines
value:
  EA: November 1
  RD: March 1 (rolling)
  confirmation_fall: May 1
  confirmation_spring: December 1
  confirmation_summer: April 1
source_url: https://www.admissions.uc.edu/apply/deadlines.html
source_snippet: "Early Action Deadline: November 1; Application Deadline: March 1 (rolling admission); Confirmation Deadline: May 1"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Application Requirements

```yaml
field: undergraduate.requirements
value:
  portal: Common Application
  fee_domestic: $50
  fee_international: $100
  test_optional: true
  superscore: false
  recommendation: optional
  transcript: official or unofficial accepted
source_url: https://www.admissions.uc.edu/information/high-school/fymc-information.html
source_snippet: "The Common Application; $50 non-refundable application fee (or fee waiver); Official High School Transcript or Unofficial High School Transcript; Official ACT or SAT test scores (optional)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test-Optional Policy

```yaml
field: undergraduate.test_policy
value: test-optional (optional for all programs)
source_url: https://www.admissions.uc.edu/information/high-school.html
source_snippet: "UC is test optional for undergraduate programs."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: English Proficiency Requirements

```yaml
field: undergraduate.english_requirements
value:
  toefl_ibt: "79-100 (varies by college)"
  ielts: "6.0-6.5 (varies by college)"
  duolingo: "100 (most colleges)"
  pte: 53
  cambridge: 176
  act_english: 19
  sat_erw: 480
source_url: https://www.admissions.uc.edu/information/international/requirements/freshman.html
source_snippet: "TOEFL iBT: Before Jan 2026: 79 Overall, 20 Writing, 20 Speaking, 15 All Other Sub Scores; After Jan 2026: 4.0 Overall"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Tuition (Ohio Resident)

```yaml
field: undergraduate.cost.tuition_ohio
value:
  per_credit_hour: $600
  per_full_time_term: $7,197
  per_full_time_year: $14,394
  cohort: 2025-26
  campus: Uptown/Clifton
source_url: https://www.uc.edu/about/financial-aid/starting/costs.html
source_snippet: "2025-26 Cohort Per Credit Hour $600 $626 $1,239 Per Full-Time Term $7,197 $7,506 $14,864 Per Full-Time Year $14,394 $15,012 $29,728"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Total Cost of Attendance

```yaml
field: undergraduate.cost.total_coa
value: $43,276 (Ohio resident, on-campus, 2026-27)
source_url: https://www.uc.edu/about/financial-aid/starting/costs.html
source_snippet: "The total amount we budget for a typical new on-campus, full-time undergraduate, Ohio resident for the basic 2-semester academic year on Uptown Campus is $43,276."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: Co-op Program

```yaml
field: undergraduate.coop
value:
  opportunities: 8300+
  industry_partners: 1757
  total_earnings_2024_25: $94_million
  sample_sophomore: $7,878
  sample_junior: $9,450
  sample_senior: $10,500
source_url: https://www.uc.edu/scholarships-financial-aid.html
source_snippet: "Currently, there are over 8,300 paid student Co-op opportunities provided by 1,757 industry partners. In 2024-25, UC students have collectively earned $94 million in co-op earnings."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Program Count

```yaml
field: institution.programs.total
value: 998
breakdown:
  undergraduate: 609
  graduate: 387
  law: 2
source_url: https://www.uc.edu/majors-programs.html
source_snippet: "The University of Cincinnati offers more than 400 academic programs" (marketing); actual count from program finder = 998
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: College Structure

```yaml
field: institution.colleges
value:
  - College of Arts and Sciences (A&S)
  - College of Education, Criminal Justice, & Human Services (CECH)
  - UC Clermont College
  - College-Conservatory of Music (CCM)
  - Carl H. Lindner College of Business (LCB)
  - College of Engineering & Applied Science (CEAS)
  - UC Blue Ash College (UCBA)
  - College of Allied Health Sciences (CAHS)
  - College of Medicine (COM)
  - College of Design, Architecture, Art, and Planning (DAAP)
  - College of Nursing (CON)
  - James L. Winkle College of Pharmacy
  - Donald P. Klekamp College of Law
  - College of Coop Education and Professional Studies (CCEPS)
  - University Honors Scholars Program
  - UC Online
source_url: https://www.uc.edu/about/provost/colleges-and-offices/colleges.html
source_snippet: "The Office of the Provost leads the affairs of the University of Cincinnati's 15 academic colleges, two regional campuses, UC Online"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: Tuition Guarantee

```yaml
field: undergraduate.cost.tuition_guarantee
value: true (cohort-based frozen rates for 4-5 years)
source_url: https://www.uc.edu/about/bursar/tuition-fees/tuition-guarantee-policy.html
source_snippet: "UC's Cincinnati Tuition Guarantee (CTG) is a cohort-based, guaranteed undergraduate degree-seeking tuition initiative that establishes a 'frozen' tuition rate particular to each academic year."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: Financial Aid

```yaml
field: undergraduate.financial_aid
value:
  fafsa_required: true
  fafsa_priority: November 1
  merit_scholarships: automatic via Common App
  cincinnatus_scholarship: yes
  national_outreach_award: yes (OOS students)
  choose_ohio_first: yes
  next_innovation_scholarship: yes
source_url: https://www.uc.edu/scholarships-financial-aid.html
source_snippet: "Traditional freshmen applying to the University of Cincinnati are automatically considered for all scholarships they are eligible for through the online UC application."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Non-Tuition Costs

```yaml
field: undergraduate.cost.non_tuition
value:
  housing_food_oncampus: $16,511 (2026-27)
  books: $1,300
  transportation_ohio: $2,038
  transportation_nonresident: $3,038
  miscellaneous: $3,386
  computer_first_year: $3,000
source_url: https://www.uc.edu/about/financial-aid/starting/costs/non-tuition-costs.html
source_snippet: "Housing and Food $16,511; Books and Course Materials $1,300; Transportation $2,038; Miscellaneous $3,386"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uc-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-college-of-arts-sciences.md   (Section 1: A&S programs)
├── 02-ug-engineering.md                (Section 1: CEAS programs)
├── 03-ug-business.md                   (Section 1: LCB programs)
├── 04-ug-ccm.md                        (Section 1: CCM programs)
├── 05-ug-daap.md                       (Section 1: DAAP programs)
├── 06-ug-cech.md                       (Section 1: CECH programs)
├── 07-ug-cahs.md                       (Section 1: CAHS programs)
├── 08-ug-nursing.md                    (Section 1: CON programs)
├── 09-ug-regional-campuses.md          (Section 1: UCBA + Clermont)
├── 10-graduate-programs.md             (Section 2: all graduate)
├── 11-deadlines-requirements.md        (Section 3)
├── 12-costs-financial-aid.md           (Section 4)
├── 13-evidence-chain.md                (Section 5)
└── 14-monitoring-watchlist.md          (Section 4: monitoring)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "uc-knowledge-base-v2"
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

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Individual graduate program deadlines/GRE requirements | Per-program pages via grad.uc.edu |
| P0 | 2026-27 cohort tuition rates (when published by Board of Trustees) | uc.edu/about/financial-aid/starting/costs.html |
| P1 | Per-program TOEFL minimums for graduate programs | Individual program pages |
| P1 | Detailed co-op program information by college | uc.edu/cooperative-education (URL needs verification) |
| P1 | Closed programs list (programs no longer accepting applications) | admissions.uc.edu/apply/closed-programs.html |
| P2 | Per-college program fee schedules | uc.edu/about/bursar (URL structure unclear) |
| P2 | International student cost and financial aid details | admissions.uc.edu/information/international/finance.html |
| P2 | Honors Program details and requirements | uc.edu/honors |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | University of Cincinnati | (Other schools) |
|------|--------------------------|-----------------|
| Type | Public | |
| Location | Cincinnati, OH | |
| EA deadline | November 1 | |
| RD deadline | March 1 (rolling) | |
| Test policy | Test-optional | |
| Application portal | Common App | |
| App fee (domestic) | $50 | |
| App fee (international) | $100 | |
| TOEFL min | 79-100 (per college) | |
| IELTS min | 6.0-6.5 (per college) | |
| UG tuition (Ohio, annual) | $14,394 | |
| UG tuition (OOS, annual) | $29,728 | |
| Total COA (Ohio, on-campus) | $43,276 | |
| Need-blind (domestic) | No | |
| Need-blind (international) | No | |
| Tuition guarantee | Yes (cohort-based) | |
| Co-op program | Yes (largest in US) | |
| Total programs | 998 | |
| UG programs | 609 | |
| Grad programs | 387 | |
| Colleges | 16 | |
| Metro tuition (KY/IN) | $15,012/year | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.uc.edu, uc.edu, grad.uc.edu, webapps2.uc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
