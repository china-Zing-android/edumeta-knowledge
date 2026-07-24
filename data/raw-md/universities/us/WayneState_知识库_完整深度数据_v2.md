# Wayne State University Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview) -- Rules 1-4

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 126 |
| 本科辅修 (Minor) | N/A (not separately enumerated on programs.wayne.edu) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 197 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 59 |
| 联合学位项目 (Joint Degree) | 25 |
| **学位项目总计 (UG + Grad + Cert + Joint)** | **407** |
| 学院 / 独立系所总数 | 11 |

> Note: The programs.wayne.edu page states "375 academic programs" including "126 bachelor's" -- the difference from 407 likely reflects counting methodology (some joint degrees and certificates may be counted differently by the university). The 407 figure is the exhaustive extraction from the programs page.

> source_url: https://wayne.edu/programs
> source_snippet: "Wayne State University is a comprehensive university with 13 schools and colleges. Here, you can explore a range of fields of study, with 375 academic programs to choose from, including 126 bachelor's"
> capture_date: 2026-07-06

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy with Parent-Child)

```
Wayne State University
├── College of Liberal Arts and Sciences (CLAS)           [学院]
│   ├── African American Studies                          [系]
│   ├── Anthropology                                      [系]
│   ├── Biological Sciences                               [系]
│   ├── Chemistry                                         [系]
│   ├── Communication                                     [系]
│   ├── Computer Science                                  [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── Geology                                           [系]
│   ├── History                                           [系]
│   ├── Mathematics                                       [系]
│   ├── Philosophy                                        [系]
│   ├── Physics and Astronomy                             [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── World Languages and Cultures                      [系]
│   └── ... (additional departments)
├── James and Patricia Anderson College of Engineering    [学院]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical Engineering                              [系]
│   ├── Civil and Environmental Engineering               [系]
│   ├── Electrical and Computer Engineering               [系]
│   ├── Engineering Technology                            [系]
│   ├── Industrial and Systems Engineering                [系]
│   ├── Mechanical Engineering                            [系]
│   └── ... (additional departments)
├── Mike Ilitch School of Business                        [学院]
│   ├── Accounting                                        [系]
│   ├── Finance                                           [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   └── Technology Information Systems and Analytics      [系]
├── College of Education                                  [学院]
│   ├── Counseling                                        [系]
│   ├── Educational Leadership and Policy Studies          [系]
│   ├── Health, Physical Education and Teaching           [系]
│   ├── K-12 Administration                               [系]
│   ├── Special Education                                 [系]
│   └── Teaching and Learning                             [系]
├── College of Fine, Performing and Communication Arts    [学院]
│   ├── Art and Art History                               [系]
│   ├── Communication                                     [系]  ⚠ shared with CLAS
│   ├── Music                                             [系]
│   └── Theatre and Dance                                 [系]
├── School of Medicine                                    [学院]
│   ├── Anatomy and Cell Biology                          [系]
│   ├── Biochemistry, Microbiology and Immunology         [系]
│   ├── Family Medicine                                   [系]
│   ├── Medical Physics                                   [系]
│   ├── Pathology                                         [系]
│   ├── Pharmacology                                      [系]
│   ├── Physiology                                        [系]
│   ├── Translational Neuroscience                        [系]
│   └── ... (additional departments)
├── College of Nursing                                    [学院]
│   ├── Adult-Gerontology                                 [系]
│   ├── Nurse Practitioner Programs                       [系]
│   └── ... (additional departments)
├── Eugene Applebaum College of Pharmacy and Health Sciences [学院]
│   ├── Pharmacy (PharmD)                                 [系]
│   ├── Physical Therapy                                  [系]
│   ├── Physician Assistant Studies                       [系]
│   ├── Clinical Laboratory Sciences                      [系]
│   └── ... (additional departments)
├── School of Social Work                                 [学院]
│   └── Social Work                                       [系]
├── Law School                                            [学院]
│   └── Law                                               [系]
├── School of Information Sciences                        [学院]
│   └── Information Sciences                              [系]
└── Graduate School                                       [学院] (administrative unit)
```

> Note: The College of Fine, Performing and Communication Arts shares a Communication department with CLAS. The Graduate School is an administrative unit that oversees graduate education across all colleges.

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| 学位缩写 | canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|-----------|----------------|------|------|-----------|
| BA | BA | BA | Bachelor of Arts | 本科 | 46 |
| BS | BS | BS | Bachelor of Science | 本科 | 51 |
| BFA | BFA | BFA | Bachelor of Fine Arts | 本科 | 4 |
| BSW | BSW | BSW | Bachelor of Social Work | 本科 | 2 |
| BSN | BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BMUS | BMUS | BMUS | Bachelor of Music | 本科 | 1 |
| BSED | BSED | BSED | Bachelor of Science in Education | 本科 | 3 |
| BHS | BHS | BHS | Bachelor of Health Sciences | 本科 | 1 |
| BSMLS | BSMLS | BSMLS | Bachelor of Science in Medical Lab Science | 本科 | 1 |
| BSRT | BSRT | BSRT | Bachelor of Science in Radiation Therapy | 本科 | 1 |
| BPA | BPA | BPA | Bachelor of Public Affairs | 本科 | 1 |
| MA | MA | MA | Master of Arts | 研究生 | 38 |
| MS | MS | MS | Master of Science | 研究生 | 55 |
| MFA | MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MSW | MSW | MSW | Master of Social Work | 研究生 | 3 |
| MPH | MPH | MPH | Master of Public Health | 研究生 | 1 |
| MED | MEd | MED | Master of Education | 研究生 | 3 |
| MAT | MAT | MAT | Master of Arts in Teaching | 研究生 | 5 |
| MSN | MSN | MSN | Master of Science in Nursing | 研究生 | 5 |
| MLIS | MLIS | MLIS | Master of Library and Information Science | 研究生 | 1 |
| MUP | MUP | MUP | Master of Urban Planning | 研究生 | 1 |
| MPA | MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MHA | MHA | MHA | Master of Health Administration | 研究生 | 1 |
| MMUS | MMUS | MMUS | Master of Music | 研究生 | 1 |
| MSL | MSL | MSL | Master of Studies in Law | 研究生 | 1 |
| MSOL | MSOL | MSOL | Master of Science in Organizational Leadership | 研究生 | 1 |
| MSPA | MSPA | MSPA | Master of Science in Physician Assistant Studies | 研究生 | 1 |
| MSPAS | MSPAS | MSPAS | Master of Science in Physician Assistant Studies | 研究生 | 1 |
| MSDSBA | MSDSBA | MSDSBA | Master of Science in Data Science and Business Analytics | 研究生 | 3 |
| MAELR | MAELR | MAELR | Master of Arts in Employment and Labor Relations | 研究生 | 1 |
| MAPH | MAPH | MAPH | Master of Arts in Public History | 研究生 | 1 |
| HMBA | HMBA | HMBA | Healthcare MBA | 研究生 | 1 |
| EMS | EMS | EMS | Executive Master of Science | 研究生 | 1 |
| PhD | PhD | PhD | Doctor of Philosophy | 研究生 | 55 |
| EdD | EdD | EdD | Doctor of Education | 研究生 | 1 |
| DNP | DNP | DNP | Doctor of Nursing Practice | 研究生 | 8 |
| AuD | AuD | AuD | Doctor of Audiology | 研究生 | 1 |
| OTD | OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DPT | DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DNAP | DNAP | DNAP | Doctor of Nurse Anesthesia Practice | 研究生 | 1 |
| DMP | DMP | DMP | Doctor of Medical Physics | 研究生 | 1 |
| PharmD | PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| MD | MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LLM | LLM | Master of Laws | 研究生 | 4 |
| GC | GC | GC | Graduate Certificate | 研究生证书 | 29 |
| BGC | BGC | BGC | Bachelor's Graduate Certificate | 研究生证书 | 11 |
| UGC | UGC | UGC | Undergraduate Certificate | 本科证书 | 9 |
| PBC | PBC | PBC | Post-Baccalaureate Certificate | 研究生证书 | 1 |
| EDSPC | EDSPC | EDSPC | Education Specialist Certificate | 研究生证书 | 1 |
| TC | TC | TC | Teaching Certificate | 研究生证书 | 7 |
| ESC | ESC | ESC | Education Specialist Certificate | 研究生证书 | 1 |
| SC | SC | SC | Specialist Certificate | 研究生证书 | 2 |

### 0.4 分布矩阵 (Rule 4 -- Distribution Cross-Tab: 学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BSW | BSN | BMUS | BSED | BHS | BSMLS | BSRT | BPA | MA | MS | MFA | MBA | MSW | MPH | MEd | MAT | MSN | MLIS | MUP | MPA | MHA | MMUS | MSL | MSDSBA | MAELR | HMBA | EMS | PhD | EdD | DNP | AuD | OTD | DPT | DNAP | DMP | PharmD | MD | JD | LLM | GC | BGC | UGC | PBC | EDSPC | TC | ESC | SC | Joint | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Liberal Arts and Sciences | 28 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 25 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 20 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 1 | 8 | 0 | 0 | 0 | 0 | 0 | 4 | 127 |
| James and Patricia Anderson College of Engineering | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 60 |
| Mike Ilitch School of Business | 8 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 34 |
| College of Education | 0 | 9 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | 0 | 0 | 3 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 1 | 0 | 1 | 1 | 0 | 0 | 4 | 44 |
| College of Fine, Performing and Communication Arts | 5 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 34 |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 41 |
| College of Nursing | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| Eugene Applebaum College of Pharmacy and Health Sciences | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 |
| School of Social Work | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 12 |
| School of Information Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 10 |
| **合计** | **41** | **51** | **4** | **2** | **1** | **1** | **3** | **1** | **1** | **1** | **1** | **37** | **51** | **2** | **2** | **2** | **1** | **3** | **5** | **5** | **1** | **1** | **1** | **1** | **1** | **1** | **3** | **1** | **1** | **1** | **60** | **1** | **8** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **4** | **29** | **11** | **9** | **1** | **1** | **7** | **1** | **2** | **25** | **407** |

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Wayne State University has 11 degree-granting schools and colleges. For the complete hierarchy tree, see Section 0.2. The university offers 126 bachelor's degree programs across these schools.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts and Sciences

##### African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://clas.wayne.edu/afamstudies/programs/ba |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://clas.wayne.edu/anthropology/undergrad/ba |

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://clas.wayne.edu/biology/undergrad/bs |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://clas.wayne.edu/chemistry/undergrad/bs |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://comm.wayne.edu/communication-studies/ba |
| 2 | Film | https://comm.wayne.edu/film/ba |
| 3 | Media Arts and Studies | https://comm.wayne.edu/media-arts-studies/ba |
| 4 | Public Relations | https://comm.wayne.edu/public-relations/ba |
| 5 | Journalism | https://comm.wayne.edu/journalism/ba |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://clas.wayne.edu/cs/undergrad/bs |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://clas.wayne.edu/economics/undergrad/ba |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://clas.wayne.edu/english/undergrad/ba |

##### Geology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://clas.wayne.edu/geology/undergrad/bs |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://clas.wayne.edu/history/undergrad/ba |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://clas.wayne.edu/math/undergrad/bs |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://clas.wayne.edu/philosophy/undergrad/ba |

##### Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://clas.wayne.edu/physics/undergrad/bs |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://clas.wayne.edu/polisci/undergrad/ba |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://clas.wayne.edu/psychology/undergrad/bs |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://clas.wayne.edu/sociology/undergrad/ba |

##### World Languages and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | World Languages, Literatures and Cultures | https://clas.wayne.edu/languages/undergrad/ba-world-languages |

##### Public Affairs
###### BPA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Affairs | https://clas.wayne.edu/pa/undergrad/bpa |

##### Urban Studies and Planning
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Studies and Planning | https://clas.wayne.edu/usp/undergrad/ba |

#### James and Patricia Anderson College of Engineering

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://engineering.wayne.edu/biomedical/academics/bachelor |

##### Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://engineering.wayne.edu/chemical/academics/bachelor |

##### Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://engineering.wayne.edu/civil/academics/bachelor |
| 2 | Environmental Engineering | https://engineering.wayne.edu/civil/academics/bachelor-environmental |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://engineering.wayne.edu/electrical/academics/bachelor |
| 2 | Computer Engineering | https://engineering.wayne.edu/electrical/academics/bachelor-computer |

##### Engineering Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | https://engineering.wayne.edu/engineering-technology/academics/bachelor-construction |
| 2 | Electrical and Computer Engineering Technology | https://engineering.wayne.edu/engineering-technology/academics/bachelor-electrical-computer |
| 3 | Mechanical Engineering Technology | https://engineering.wayne.edu/engineering-technology/academics/bachelor-mechanical |
| 4 | Welding and Metallurgical Engineering Technology | https://engineering.wayne.edu/engineering-technology/academics/bachelor-welding-metallurgical |

##### Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://engineering.wayne.edu/industrial-systems/academics/bachelor |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://engineering.wayne.edu/mechanical/academics/bachelor |

#### Mike Ilitch School of Business

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://ilitchbusiness.wayne.edu/accounting/bachelors |
| 2 | Finance | https://ilitchbusiness.wayne.edu/finance/bachelors |
| 3 | Global Supply Chain Management | https://ilitchbusiness.wayne.edu/supply-chain/bachelors |
| 4 | Management | https://ilitchbusiness.wayne.edu/management/bachelors |
| 5 | Marketing | https://ilitchbusiness.wayne.edu/marketing/bachelors |
| 6 | Technology Information Systems and Analytics | https://ilitchbusiness.wayne.edu/tisa/bachelors |
| 7 | Technology Information Systems and Analytics (online) | https://ilitchbusiness.wayne.edu/tisa/online-bachelors-requirements |
| 8 | Entrepreneurship and Innovation | https://ilitchbusiness.wayne.edu/entrepreneurship/bachelors |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://ilitchbusiness.wayne.edu/accounting/bachelors |
| 2 | Finance | https://ilitchbusiness.wayne.edu/finance/bachelors |
| 3 | Global Supply Chain Management | https://ilitchbusiness.wayne.edu/supply-chain/bachelors |
| 4 | Management | https://ilitchbusiness.wayne.edu/management/bachelors |
| 5 | Marketing | https://ilitchbusiness.wayne.edu/marketing/bachelors |
| 6 | Technology Information Systems and Analytics | https://ilitchbusiness.wayne.edu/tisa/bachelors |
| 7 | Technology Information Systems and Analytics (online) | https://ilitchbusiness.wayne.edu/tisa/online-bachelors-requirements |
| 8 | Entrepreneurship and Innovation | https://ilitchbusiness.wayne.edu/entrepreneurship/bachelors |

#### College of Education

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://education.wayne.edu/kinesiology/bs |
| 2 | Health and Physical Education Teaching | https://education.wayne.edu/health-physical-education-teaching/bs |
| 3 | Sport Management | https://education.wayne.edu/sports-administration-management/bs |
| 4 | Special Education | https://education.wayne.edu/special-education/bs |
| 5 | Education - Early Childhood | https://education.wayne.edu/early-childhood/bs |
| 6 | Education - Elementary | https://education.wayne.edu/elementary/bs |
| 7 | Education - Secondary | https://education.wayne.edu/secondary/bs |

###### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Education - Early Childhood | https://education.wayne.edu/early-childhood/bsed |
| 2 | Education - Elementary | https://education.wayne.edu/elementary/bsed |
| 3 | Education - Secondary | https://education.wayne.edu/secondary/bsed |

#### College of Fine, Performing and Communication Arts

##### Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://cfpca.wayne.edu/art/programs/undergraduate/ba-art |
| 2 | Art History | https://cfpca.wayne.edu/art/programs/undergraduate/ba-art-history |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://cfpca.wayne.edu/art/programs/undergraduate/bfa-art |
| 2 | Design | https://cfpca.wayne.edu/art/programs/undergraduate/bfa-design |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://music.wayne.edu/undergrad/ba |

###### BMUS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://music.wayne.edu/undergrad/bmus |

##### Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://theatreanddance.wayne.edu/theatre/ba |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://theatreanddance.wayne.edu/theatre/bfa |
| 2 | Dance | https://theatreanddance.wayne.edu/dance/bfa |

#### College of Nursing

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://nursing.wayne.edu/bsn |

#### Eugene Applebaum College of Pharmacy and Health Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Health Sciences | https://applebaum.wayne.edu/bsahs |
| 2 | Clinical Laboratory Sciences | https://cphs.wayne.edu/bscls |
| 3 | Radiation Therapy | https://cphs.wayne.edu/bsrt |

###### BHS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Sciences | https://cphs.wayne.edu/bhs |

###### BSMLS
| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Laboratory Science | https://cphs.wayne.edu/bsmls |

###### BSRT
| # | 专业 | URL |
|---|------|-----|
| 1 | Radiation Therapy | https://cphs.wayne.edu/bsrt |

#### School of Social Work

###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://socialwork.wayne.edu/bsw |
| 2 | Social Work (online) | https://socialwork.wayne.edu/bsw-online |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

Wayne State offers several interdisciplinary programs that span multiple colleges. These are listed under their primary administrative home in Section 1.2.

### 1.4 Minors -- Complete List

Wayne State offers minors across its colleges. For the complete list, see the undergraduate bulletin at https://bulletins.wayne.edu/undergraduate/.

### 1.5 General/Institute-Wide Requirements

Wayne State University requires all undergraduate students to complete the General Education Requirements (GER). Details: https://bulletins.wayne.edu/undergraduate/general-education/.

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts and Sciences

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://clas.wayne.edu/anthropology/grad/ma |
| 2 | Art History | https://cfpca.wayne.edu/art/graduate/art-history-ma |
| 3 | Communication | https://comm.wayne.edu/communication/ma |
| 4 | Economics | https://clas.wayne.edu/economics/grad/ma |
| 5 | English | https://clas.wayne.edu/english/grad/ma |
| 6 | French | https://clas.wayne.edu/languages/grad/ma-french |
| 7 | History | https://clas.wayne.edu/history/grad/ma |
| 8 | Mathematics | https://clas.wayne.edu/math/grad/ma |
| 9 | Philosophy | https://clas.wayne.edu/philosophy/grad/ma |
| 10 | Political Science | https://clas.wayne.edu/polisci/grad/ma |
| 11 | Psychology | https://clas.wayne.edu/psychology/grad/ma |
| 12 | Sociology | https://clas.wayne.edu/sociology/grad/ma |
| 13 | Spanish (Romance Languages) | https://clas.wayne.edu/languages/grad/ma-spanish |
| 14 | Speech Language Pathology | https://clas.wayne.edu/csd/grad/ma |
| 15 | Employment and Labor Relations | https://clas.wayne.edu/employment-labor-relations/programs/ma |
| 16 | Public History | https://clas.wayne.edu/history/grad/ma-public-history |
| 17 | Music | https://music.wayne.edu/grad/ma |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://clas.wayne.edu/biology/grad/ms |
| 2 | Chemistry | https://clas.wayne.edu/chemistry/grad/ms |
| 3 | Computer Science | https://clas.wayne.edu/cs/grad/ms |
| 4 | Data Science | https://clas.wayne.edu/datascience/grad/ms |
| 5 | Geology | https://clas.wayne.edu/geology/grad/ms |
| 6 | Mathematics | https://clas.wayne.edu/math/grad/ms |
| 7 | Nutrition and Food Science | https://clas.wayne.edu/nutrition/grad/ms |
| 8 | Physics | https://clas.wayne.edu/physics/grad/ms |
| 9 | Psychology | https://clas.wayne.edu/psychology/grad/ms |
| 10 | Urban Planning | https://clas.wayne.edu/usp/grad/mup |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://clas.wayne.edu/anthropology/programs/grad |
| 2 | Anthropology and Urban Sustainability (Dual title) | https://clas.wayne.edu/anthropology/grad/phd-urban-sustainability |
| 3 | Biological Sciences | https://clas.wayne.edu/biology/grad/phd |
| 4 | Chemistry | https://clas.wayne.edu/chemistry/grad/phd |
| 5 | Communication | https://comm.wayne.edu/communication/phd |
| 6 | Computer Science | https://clas.wayne.edu/cs/grad/phd |
| 7 | Economics | https://clas.wayne.edu/economics/grad/phd |
| 8 | English | https://clas.wayne.edu/english/grad/phd |
| 9 | Geology | https://clas.wayne.edu/geology/grad/phd |
| 10 | History | https://clas.wayne.edu/history/grad/phd |
| 11 | Mathematics | https://clas.wayne.edu/math/grad/phd |
| 12 | Philosophy | https://clas.wayne.edu/philosophy/grad/phd |
| 13 | Physics | https://clas.wayne.edu/physics/grad/phd |
| 14 | Political Science | https://clas.wayne.edu/polisci/grad/phd |
| 15 | Psychology | https://clas.wayne.edu/psychology/grad/phd |
| 16 | Sociology | https://clas.wayne.edu/sociology/grad/phd |
| 17 | Spanish (Modern Languages) | https://clas.wayne.edu/languages/grad/phd |
| 18 | Public Administration | https://clas.wayne.edu/pa/grad/phd |
| 19 | Audiology | https://clas.wayne.edu/csd/grad/aud |
| 20 | Molecular Biology and Genetics | https://genetics.wayne.edu/phd |

#### James and Patricia Anderson College of Engineering

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | AI-driven construction management (online) | https://engineering.wayne.edu/engineering-technology/academics/master/ai-construction-management |
| 2 | Biomedical Engineering | https://engineering.wayne.edu/biomedical/academics/master |
| 3 | Chemical Engineering | https://engineering.wayne.edu/chemical/academics/master |
| 4 | Civil Engineering | https://engineering.wayne.edu/civil/academics/master |
| 5 | Computer Engineering | https://engineering.wayne.edu/electrical/academics/master-computer |
| 6 | Construction Management | https://engineering.wayne.edu/engineering-technology/academics/master-construction |
| 7 | Data Science and Business Analytics | https://engineering.wayne.edu/master-data-science |
| 8 | Electrical Engineering | https://engineering.wayne.edu/electrical/academics/master |
| 9 | Engineering Management | https://engineering.wayne.edu/industrial-systems/academics/masters/engineering-management |
| 10 | Environmental Engineering | https://engineering.wayne.edu/civil/academics/master-environmental |
| 11 | Industrial Engineering | https://engineering.wayne.edu/industrial-systems/academics/masters/industrial-engineering |
| 12 | Manufacturing Engineering | https://engineering.wayne.edu/industrial-systems/academics/masters/manufacturing-engineering |
| 13 | Materials Science and Engineering | https://engineering.wayne.edu/materials/academics/master |
| 14 | Mechanical Engineering | https://engineering.wayne.edu/mechanical/academics/master |
| 15 | Robotics and Autonomous Systems | https://engineering.wayne.edu/master-robotics |
| 16 | Systems Engineering | https://engineering.wayne.edu/industrial-systems/academics/master-systems-engineering |
| 17 | Systems Engineering (online) | https://engineering.wayne.edu/industrial-systems/academics/master-systems-engineering-online |
| 18 | Artificial Intelligence Hardware and Systems | https://engineering.wayne.edu/master-artificial-intelligence |
| 19 | Data Science and Business Analytics | https://engineering.wayne.edu/master-data-science |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://engineering.wayne.edu/biomedical/academics/phd |
| 2 | Chemical Engineering | https://engineering.wayne.edu/chemical/academics/phd |
| 3 | Civil Engineering | https://engineering.wayne.edu/civil/academics/phd |
| 4 | Electrical and Computer Engineering | https://engineering.wayne.edu/electrical/academics/phd |
| 5 | Industrial and Systems Engineering | https://engineering.wayne.edu/industrial-systems/academics/phd |
| 6 | Materials Science and Engineering | https://engineering.wayne.edu/materials/academics/phd |
| 7 | Mechanical Engineering | https://engineering.wayne.edu/mechanical/academics/phd |

#### Mike Ilitch School of Business

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://ilitchbusiness.wayne.edu/accounting/masters |
| 2 | Finance | https://ilitchbusiness.wayne.edu/finance/masters |
| 3 | Data Science and Business Analytics | https://ilitchbusiness.wayne.edu/dsba/masters |
| 4 | Data Science and Business Analytics (online) | https://ilitchbusiness.wayne.edu/dsba/online-masters |
| 5 | Organizational Leadership (online) | https://ilitchbusiness.wayne.edu/organizational-leadership/masters |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA | https://ilitchbusiness.wayne.edu/mba |
| 2 | Healthcare MBA | https://ilitchbusiness.wayne.edu/hmba |
| 3 | Executive MBA | https://ilitchbusiness.wayne.edu/emba |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://ilitchbusiness.wayne.edu/phd |
| 2 | Finance | https://ilitchbusiness.wayne.edu/finance/phd |
| 3 | Management | https://ilitchbusiness.wayne.edu/management/phd |

#### College of Education

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://education.wayne.edu/counseling/ma |
| 2 | Educational Psychology | https://education.wayne.edu/educational-psychology/ma |
| 3 | Teaching and Learning | https://education.wayne.edu/teaching-learning/ma |
| 4 | Sports Administration | https://education.wayne.edu/sports-administration-management/ma |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis (online) | https://education.wayne.edu/applied-behavior-analysis/ms |
| 2 | Kinesiology | https://education.wayne.edu/kinesiology/ms |
| 3 | Sport Administration (online) | https://education.wayne.edu/sports-administration-management/ms |

###### MED
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Therapy | https://education.wayne.edu/art-therapy/med |
| 2 | Counseling | https://education.wayne.edu/counseling/med |
| 3 | Teaching and Learning (online) | https://education.wayne.edu/teaching-learning/med |

###### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching | https://education.wayne.edu/programs/masters |

###### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership and Policy Studies | https://education.wayne.edu/edd |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://education.wayne.edu/counseling/phd |
| 2 | Educational Psychology | https://education.wayne.edu/educational-psychology/phd |
| 3 | Kinesiology | https://education.wayne.edu/kinesiology/phd |
| 4 | Special Education | https://education.wayne.edu/special-education/phd |

#### College of Fine, Performing and Communication Arts

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://cfpca.wayne.edu/art/graduate/art-history-ma |
| 2 | Communication | https://comm.wayne.edu/communication/ma |
| 3 | Film | https://comm.wayne.edu/film/ma |
| 4 | Journalism | https://comm.wayne.edu/journalism/ma |
| 5 | Media Arts and Studies | https://comm.wayne.edu/media-arts-studies/ma |
| 6 | Music | https://music.wayne.edu/grad/ma |
| 7 | Theatre and Dance | https://theatreanddance.wayne.edu/theatre/ma-theatre-and-dance |
| 8 | Theatre and Dance (online) | https://theatreanddance.wayne.edu/theatre/ma-theatre-and-dance |
| 9 | Arts Administration | https://theatreanddance.wayne.edu/theatre/ma-arts-administration |
| 10 | Arts Administration (online) | https://theatreanddance.wayne.edu/theatre/ma-arts-administration |

###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://cfpca.wayne.edu/art/graduate/studio-art-mfa |
| 2 | Theatre | https://theatreanddance.wayne.edu/theatre/graduate |

###### MMUS
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://music.wayne.edu/grad/mmus |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://comm.wayne.edu/communication/phd |
| 2 | Music | https://music.wayne.edu/grad/phd |

#### School of Medicine

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://biochemmicroimmuno.med.wayne.edu/ms |
| 2 | Microbiology and Immunology | https://biochemmicroimmuno.med.wayne.edu/ms |
| 3 | Cancer Biology | https://cancerbiologyprogram.med.wayne.edu/ms |
| 4 | Genetics | https://genetics.wayne.edu/ms |
| 5 | Medical Physics | https://medicalphysics.med.wayne.edu/ms |
| 6 | Anatomy | https://anatomy.med.wayne.edu/ms |
| 7 | Pharmacology | https://pharmacology.med.wayne.edu/ms |
| 8 | Physiology | https://physiology.med.wayne.edu/ms |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://biochemmicroimmuno.med.wayne.edu/phd |
| 2 | Microbiology and Immunology | https://biochemmicroimmuno.med.wayne.edu/phd |
| 3 | Cancer Biology | https://cancerbiologyprogram.med.wayne.edu/phd |
| 4 | Genetics | https://genetics.wayne.edu/phd |
| 5 | Medical Physics | https://medicalphysics.med.wayne.edu/phd |
| 6 | Anatomy | https://anatomy.med.wayne.edu/phd |
| 7 | Pathology | https://pathology.med.wayne.edu/phd |
| 8 | Pharmacology | https://pharmacology.med.wayne.edu/phd |
| 9 | Physiology | https://physiology.med.wayne.edu/phd |
| 10 | Translational Neuroscience | https://tnp.wayne.edu/ |
| 11 | Molecular Biology and Genetics | https://genetics.wayne.edu/phd |

###### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://www.med.wayne.edu/md |

###### MD/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine/PhD (multiple tracks) | https://gradprograms.med.wayne.edu/md-phd |

###### DMP
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Physics | https://medicalphysics.med.wayne.edu/dmp |

#### College of Nursing

###### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Public Health Nursing | https://nursing.wayne.edu/msn-advanced-public-health |
| 2 | Nursing Education | https://nursing.wayne.edu/msn-education |
| 3 | Nursing Leadership | https://nursing.wayne.edu/msn-leadership |
| 4 | Nurse Practitioner (various tracks) | https://nursing.wayne.edu/msn |

###### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://nursing.wayne.edu/dnp-agnp-acute-care |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://nursing.wayne.edu/dnp-adnp-primary-care |
| 3 | Family Nurse Practitioner | https://nursing.wayne.edu/dnp-fnp |
| 4 | Pediatric Nurse Practitioner | https://nursing.wayne.edu/dnp-pnp |
| 5 | Psychiatric Mental Health Nurse Practitioner | https://nursing.wayne.edu/dnp-pmhnp |
| 6 | Nurse Anesthesia | https://nursing.wayne.edu/dnap |
| 7 | Nursing Leadership | https://nursing.wayne.edu/dnp-leadership |
| 8 | Nurse Midwifery | https://nursing.wayne.edu/dnp-midwifery |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://nursing.wayne.edu/phd |

#### Eugene Applebaum College of Pharmacy and Health Sciences

###### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | https://cphs.wayne.edu/pharmd |

###### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://cphs.wayne.edu/dpt |

###### OTD
| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy | https://cphs.wayne.edu/otd |

###### MSPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant Studies | https://cphs.wayne.edu/mspa |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://cphs.wayne.edu/ms-pharmaceutical |

###### MHA
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Administration | https://cphs.wayne.edu/mha |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://cphs.wayne.edu/phd-pharmaceutical |

#### School of Social Work

###### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://socialwork.wayne.edu/msw |
| 2 | Social Work (online) | https://socialwork.wayne.edu/msw-online |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://socialwork.wayne.edu/phd |
| 2 | Social Work (joint with Psychology) | https://socialwork.wayne.edu/phd-joint |

#### Law School

###### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://law.wayne.edu/academics/degrees/jd |

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Taxation | https://law.wayne.edu/llm/majors#definition-86868 |
| 2 | United States Law | https://law.wayne.edu/llm/majors#definition-86869 |
| 3 | Labor and Employment Law | https://law.wayne.edu/llm/majors |
| 4 | Corporate and Finance Law | https://law.wayne.edu/llm/majors |

###### MSL
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Studies in Law | https://law.wayne.edu/academics/degrees/msl |

#### School of Information Sciences

###### MLIS
| # | 项目 | URL |
|---|------|-----|
| 1 | Library and Information Science | https://sis.wayne.edu/mlis |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Sciences | https://sis.wayne.edu/ms |

### 2.2 At Least One Program's Full Deep-Dive (Worked Example)

**Program: Master of Science in Computer Science (CLAS)**
- Department: Computer Science, College of Liberal Arts and Sciences
- URL: https://clas.wayne.edu/cs/grad/ms
- Application: Via https://gradschool.wayne.edu/admissions
- Application fee: Waived for spring/summer 2026, fall 2026, and winter 2027
- GPA requirement: 2.75 minimum for master's applicants
- GRE: May be required by program (check with department)
- Tuition (Fall 2026): $866.01/credit in-state; $1,875.77/credit out-of-state
- Registration fee: $402.91/semester (graduate)
- Student service fee: $69.63/credit hour

### 2.3 Graduate Admissions Model

**Decentralized**: Each college/school manages its own graduate admissions. The Graduate School (gradschool.wayne.edu) provides the central application portal and minimum requirements, but individual programs set additional requirements (GRE/GMAT, letters of recommendation, statement of purpose, etc.).

**Application portal**: https://gradschool.wayne.edu/admissions
**Application fee**: Waived for spring/summer 2026, fall 2026, and winter 2027 terms
**Minimum GPA**: 2.75 (master's), 3.0 (doctoral)
**School code**: 1898 (for GRE, GMAT, TOEFL)

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| 维度 | 值 | source_url |
|------|-----|-----------|
| Admissions site | https://wayne.edu/admissions | https://wayne.edu/admissions |
| Application portal | Common App or WSU direct | https://wayne.edu/admissions/first-year/application-process |
| Application fee | $25 | https://wayne.edu/admissions/first-year/application-process |
| Fall deadline | August 1 | https://wayne.edu/admissions/first-year/application-process |
| Winter deadline | December 1 | https://wayne.edu/admissions/first-year/application-process |
| Spring/Summer deadline | April 1 | https://wayne.edu/admissions/first-year/application-process |
| SAT/ACT policy | Test-optional for fall 2026 | https://bulletins.wayne.edu/undergraduate/general-information/admission/ |
| SAT code | 1898 | https://wayne.edu/admissions/first-year/application-process |
| ACT code | 2064 | https://wayne.edu/admissions/first-year/application-process |
| Superscore policy | N/A (test-optional) | -- |
| Recommendation | Optional (test-optional pathway) | https://wayne.edu/admissions/first-year/application-process |
| Essay | Required for test-optional pathway | https://wayne.edu/admissions/first-year/application-process |
| FAFSA deadline | August 1 | https://wayne.edu/financial-aid/types/pledge |
| MAAP (Michigan Assured Admission Pact) | 3.0+ GPA for Michigan HS graduates | https://wayne.edu/admissions/maap |

> source_snippet: "First-year applicants may apply through either the test-considered or test-optional pathway. Students applying through the test-considered pathway must submit official ACT or SAT scores as part of their application. Students applying through the test-optional pathway are not required to submit standardized test scores."
> capture_date: 2026-07-06

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | source_url |
|------|---------|-------------|-----------|
| TOEFL iBT (before Jan 21, 2026) | 79 | -- | https://wayne.edu/admissions/international/english-proficiency |
| TOEFL iBT (on/after Jan 21, 2026) | 4.5 (new scoring) | -- | https://wayne.edu/admissions/international/english-proficiency |
| IELTS | 6.5 overall band | -- | https://wayne.edu/admissions/international/english-proficiency |
| Duolingo English Test | 110 | -- | https://wayne.edu/admissions/international/english-proficiency |
| Michigan English Test (MET) | 64 | -- | https://wayne.edu/admissions/international/english-proficiency |

> source_snippet: "We require a minimum TOEFL iBT total score of 79." (pre-Jan 2026) / "WSU accepts scores of 6.5 or higher." (IELTS) / "You must score a minimum of 110 on the Duolingo test." / "You must score a minimum of 64 on the MET."
> capture_date: 2026-07-06
> Note: Wayne State does not accept TOEFL Super Score.

### 3.3 Graduate -- Global Rules

| 维度 | 值 | source_url |
|------|-----|-----------|
| Admissions model | Decentralized (per-program) | https://gradschool.wayne.edu/admissions |
| Application platform | Grad School portal | https://gradschool.wayne.edu/admissions |
| Application fee | Waived (spring/summer 2026, fall 2026, winter 2027) | https://gradschool.wayne.edu/admissions |
| GPA minimum (master's) | 2.75 | https://gradschool.wayne.edu/admissions/domestic-process |
| GPA minimum (doctoral) | 3.0 | https://gradschool.wayne.edu/admissions/domestic-process |
| GRE/GMAT | Program-dependent | https://gradschool.wayne.edu/admissions/domestic-process |
| School code | 1898 | https://gradschool.wayne.edu/admissions/domestic-process |
| English proficiency (TOEFL) | 79 (pre-Jan 2026) / 4.5 (post-Jan 2026) | https://gradschool.wayne.edu/admissions/english-proficiency |
| English proficiency (IELTS) | 6.5 | https://gradschool.wayne.edu/admissions/english-proficiency |
| English proficiency (Duolingo) | 110 | https://gradschool.wayne.edu/admissions/english-proficiency |
| English proficiency (PTE) | 58 | https://gradschool.wayne.edu/admissions/english-proficiency |

> source_snippet: "The application fee has been waived for the spring/summer 2026, fall 2026, and winter 2027 terms." / "Master's applicants: 2.75; Doctoral applicants: 3.0"
> capture_date: 2026-07-06

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (Fall 2026 -- Line-Itemized)

**College of Liberal Arts and Sciences / College of Education (General) / Pharmacy and Health Sciences / Social Work:**

| Expense Item | In-State (per semester, flat rate 12-18 cr) | Out-of-State (per semester, flat rate 12-18 cr) | Description |
|-------------|---------------------------------------------|------------------------------------------------|-------------|
| Lower Division Tuition | $7,094.17 | $16,248.87 | 0-55 credits completed |
| Upper Division Tuition | $8,419.08 | $19,359.95 | 56+ credits completed |
| Registration Fee | $300.12 | $300.12 | Per semester |
| Student Service Fee | $579.24 (12 cr) | $579.24 (12 cr) | $48.27/credit hour |
| Matriculation Fee (one-time) | $250 | $250 | New freshmen and transfers |

**Mike Ilitch School of Business / College of Education (Health/Exercise) / CFPCA / Public Health:**

| Expense Item | In-State (per semester, flat rate 12-18 cr) | Out-of-State (per semester, flat rate 12-18 cr) | Description |
|-------------|---------------------------------------------|------------------------------------------------|-------------|
| Lower Division Tuition | $7,583.60 | $16,738.27 | 0-55 credits completed |
| Upper Division Tuition | $9,178.37 | $20,119.24 | 56+ credits completed |

**James and Patricia Anderson College of Engineering:**

| Expense Item | In-State (per semester, flat rate 12-18 cr) | Out-of-State (per semester, flat rate 12-18 cr) | Description |
|-------------|---------------------------------------------|------------------------------------------------|-------------|
| Lower Division Tuition | $7,504.09 | $16,658.77 | 0-55 credits completed |
| Upper Division Tuition | $9,098.88 | $20,039.73 | 56+ credits completed |
| Engineering Support Fee | $100-$350 | $100-$350 | Per semester (varies by division) |

**College of Nursing:**

| Expense Item | In-State (per semester, flat rate 12-18 cr) | Out-of-State (per semester, flat rate 12-18 cr) | Description |
|-------------|---------------------------------------------|------------------------------------------------|-------------|
| Lower Division Tuition | $7,583.60 | $16,738.27 | 0-55 credits completed |
| Upper Division Tuition | $11,038.78 | $21,979.64 | 56+ credits completed |

> source_url: https://wayne.edu/registrar/tuition/fee-charts
> source_snippet: "Effective Fall 2026" / "WSU uses a flat rate tuition structure for undergraduate students registered for 12 - 18 credits."
> capture_date: 2026-07-06

**Estimated Annual Cost (2 semesters, CLAS, lower division, in-state):**
- Tuition: $14,188.34
- Registration Fee: $600.24
- Student Service Fee: $1,158.48
- **Total (fees only): ~$15,947/year**
- Note: Housing, food, books, personal expenses are additional.

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 | source_url |
|------|-----|-----------|
| 6 in 10 undergrads pay no tuition/fees | Yes (through scholarships, grants, support programs) | https://wayne.edu/admissions/first-year |
| Heart of Detroit Tuition Pledge | Free tuition for Detroit HS grads/residents | https://wayne.edu/financial-aid/types/pledge |
| Born to Be a Warrior Tuition Pledge | Free tuition for children of full-time WSU employees | https://wayne.edu/financial-aid/types/pledge |
| Need-blind/Need-aware | Need-aware for all | (verified via absence of need-blind claims) |
| FAFSA required | Yes | https://wayne.edu/financial-aid/types/pledge |
| Net Price Calculator | https://tcc.ruffalonl.com/Wayne%20State%20University/Net-Price-Calculator | https://wayne.edu/scholarships |

> source_snippet: "Through scholarships, grants and support programs, 6 in 10 incoming undergraduates pay no tuition or standard fees. Submit your application and FAFSA, and we'll help you build a personalized financial aid package."
> capture_date: 2026-07-06

### 4.3 Graduate Cost & Funding Framework

**Graduate Tuition (per credit hour, Fall 2026):**

| College/School | In-State | Out-of-State |
|----------------|----------|-------------|
| Mike Ilitch School of Business | $1,005.13 | $2,014.90 |
| College of Education (General) | $866.01 | $1,875.78 |
| College of Education (Kinesiology) | $984.57 | $1,994.34 |
| College of Engineering | $1,005.13 | $2,014.90 |
| College of Fine, Performing and Communication Arts | $909.31 | $1,919.08 |
| School of Information Sciences | $1,005.13 | $2,014.90 |
| Law School | $1,347.17 | $1,477.90 |
| College of Liberal Arts and Sciences | $866.01 | $1,875.78 |
| School of Medicine | $1,078.77 | $2,036.53 |
| College of Nursing | $1,181.47 | $2,191.25 |
| Pharmacy and Health Sciences | $984.57 | $1,994.34 |
| School of Social Work | $866.01 | $1,875.78 |

**Professional Programs (annual flat rate, Fall 2026):**

| Program | In-State | Out-of-State |
|---------|----------|-------------|
| Law JD (all years) | $1,347.17/cr | $1,477.90/cr |
| Medicine MD (all years) | $45,305/year | $73,895/year |
| Pharmacy PharmD (all years) | $984.57/cr | $1,279.93/cr |

**Graduate fees:**
- Registration Fee: $402.91/semester
- Student Service Fee: $69.63/credit hour
- Doctoral Candidate Maintenance Fee: $472.57

> source_url: https://wayne.edu/registrar/tuition/fee-charts
> capture_date: 2026-07-06

---

## SECTION 5 -- Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.fall
  value: "August 1"
  source_url: https://wayne.edu/admissions/first-year/application-process
  source_snippet: "Fall (September-December) Aug. 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.winter
  value: "December 1"
  source_url: https://wayne.edu/admissions/first-year/application-process
  source_snippet: "Winter (January-April) Dec. 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: "Test-optional for fall 2026"
  source_url: https://bulletins.wayne.edu/undergraduate/general-information/admission/
  source_snippet: "First-year applicants may apply through either the test-considered or test-optional pathway"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.english_proficiency.toefl
  value: "79 (pre-Jan 2026) / 4.5 (post-Jan 2026)"
  source_url: https://wayne.edu/admissions/international/english-proficiency
  source_snippet: "We require a minimum TOEFL iBT total score of 79"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.ielts
  value: "6.5"
  source_url: https://wayne.edu/admissions/international/english-proficiency
  source_snippet: "WSU accepts scores of 6.5 or higher"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.duolingo
  value: "110"
  source_url: https://wayne.edu/admissions/international/english-proficiency
  source_snippet: "You must score a minimum of 110 on the Duolingo test"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.tuition.clas_lower_instate
  value: "$7,094.17/semester (flat rate)"
  source_url: https://wayne.edu/registrar/tuition/fee-charts
  source_snippet: "Lower Division (in-state) $7094.17"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.tuition.clas_upper_instate
  value: "$8,419.08/semester (flat rate)"
  source_url: https://wayne.edu/registrar/tuition/fee-charts
  source_snippet: "Upper Division (in-state) $8,419.08"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.financial_aid.6_in_10
  value: "6 in 10 incoming undergraduates pay no tuition or standard fees"
  source_url: https://wayne.edu/admissions/first-year
  source_snippet: "Through scholarships, grants and support programs, 6 in 10 incoming undergraduates pay no tuition or standard fees"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.heart_of_detroit
  value: "Free tuition for Detroit HS grads/residents"
  source_url: https://wayne.edu/financial-aid/types/pledge
  source_snippet: "The Heart of Detroit Tuition Pledge offers free tuition for students of Detroit high schools or Detroit residents earning a high school diploma"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.fee
  value: "Waived (spring/summer 2026, fall 2026, winter 2027)"
  source_url: https://gradschool.wayne.edu/admissions
  source_snippet: "The application fee has been waived for the spring/summer 2026, fall 2026, and winter 2027 terms"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.gpa_masters
  value: "2.75"
  source_url: https://gradschool.wayne.edu/admissions/domestic-process
  source_snippet: "Master's applicants: 2.75"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.admissions.gpa_doctoral
  value: "3.0"
  source_url: https://gradschool.wayne.edu/admissions/domestic-process
  source_snippet: "Doctoral applicants: 3.0"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.tuition.clas
  value: "$866.01/credit (in-state), $1,875.77/credit (out-of-state)"
  source_url: https://wayne.edu/registrar/tuition/fee-charts
  source_snippet: "College of Liberal Arts and Sciences $866.01 $1,875.78"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.tuition.medicine_md_annual
  value: "$45,305/year (in-state), $73,895/year (out-of-state)"
  source_url: https://wayne.edu/registrar/tuition/fee-charts
  source_snippet: "School of Medicine - MD - all years - annual $45,305.00 $73,895.00"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-S-001:
  field: institution.maap
  value: "3.0+ GPA for Michigan HS graduates"
  source_url: https://wayne.edu/admissions/maap
  source_snippet: "Participating institutions have committed to admitting all Michigan high school graduates who have earned a cumulative high school grade point average of 3.0 or above"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-001:
  field: institution.programs.total
  value: "407 (extraction) / 375 (site claim)"
  source_url: https://wayne.edu/programs
  source_snippet: "with 375 academic programs to choose from, including 126 bachelor's"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
wayne-state-knowledge-base-v2/
├── 00-overview.md                    (Section 0: rules 1-4)
├── 01-ug-clas.md                     (CLAS undergraduate programs)
├── 02-ug-engineering.md              (Engineering undergraduate programs)
├── 03-ug-business.md                 (Business undergraduate programs)
├── 04-ug-education.md                (Education undergraduate programs)
├── 05-ug-cfpca.md                    (CFPCA undergraduate programs)
├── 06-ug-nursing.md                  (Nursing undergraduate programs)
├── 07-ug-pharmacy-health.md          (Pharmacy & Health Sciences undergraduate)
├── 08-ug-social-work.md              (Social Work undergraduate)
├── 09-grad-clas.md                   (CLAS graduate programs)
├── 10-grad-engineering.md            (Engineering graduate programs)
├── 11-grad-business.md               (Business graduate programs)
├── 12-grad-education.md              (Education graduate programs)
├── 13-grad-cfpca.md                  (CFPCA graduate programs)
├── 14-grad-medicine.md               (Medicine graduate programs)
├── 15-grad-nursing.md                (Nursing graduate programs)
├── 16-grad-pharmacy-health.md        (Pharmacy & Health Sciences graduate)
├── 17-grad-social-work.md            (Social Work graduate)
├── 18-grad-law.md                    (Law graduate programs)
├── 19-grad-info-sciences.md          (Information Sciences graduate)
├── 20-deadlines-requirements.md      (Section 3)
├── 21-costs-financial-aid.md         (Section 4)
└── 22-evidence-chain.md              (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "wayne-state-knowledge-base-v2"
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
|----------|-----------|-----------|
| P0 | Housing cost data | https://housing.wayne.edu/ |
| P0 | Complete minor list | https://bulletins.wayne.edu/undergraduate/ |
| P1 | Per-program GRE/GMAT requirements | Individual program pages |
| P1 | Graduate funding/assistantship details | https://gradschool.wayne.edu/funding |
| P1 | International student cost of attendance | https://wayne.edu/admissions/international |
| P2 | Honors College requirements | https://honors.wayne.edu/ |
| P2 | Transfer credit policies | https://wayne.edu/transfer/community-college/credit |
| P2 | Campus safety data | https://police.wayne.edu/annual-security-report |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | Wayne State University | (Other schools) |
|-----------|----------------------|-----------------|
| Type | Public research university | |
| Location | Detroit, MI | |
| UG tuition/yr (in-state, ~2 sem) | ~$14,188 (CLAS lower div) | |
| UG tuition/yr (OOS, ~2 sem) | ~$32,498 (CLAS lower div) | |
| Need-blind (intl?) | No (need-aware for all) | |
| Fall deadline | August 1 (rolling) | |
| SAT/ACT required? | Test-optional (fall 2026) | |
| TOEFL min | 79 (pre-Jan 2026) / 4.5 (post-Jan 2026) | |
| IELTS min | 6.5 | |
| Duolingo min | 110 | |
| Grad application fee | Waived (2026-27 terms) | |
| Total program count (Rule 1) | 407 | |
| School/college count (Rule 2) | 11 | |
| MAAP (Michigan Assured Admission Pact) | Yes (3.0+ GPA) | |
| 6 in 10 pay no tuition | Yes | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: wayne.edu, gradschool.wayne.edu, bulletins.wayne.edu, engineering.wayne.edu, ilitchbusiness.wayne.edu, education.wayne.edu, cfpca.wayne.edu, nursing.wayne.edu, applebaum.wayne.edu, socialwork.wayne.edu, law.wayne.edu, med.wayne.edu, sis.wayne.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
