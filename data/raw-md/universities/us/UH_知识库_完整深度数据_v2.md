# University of Houston (UH) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 107 |
| 本科辅修 (Minor) | ~50+ (estimated; catalog verification needed) |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 144 |
| 研究生高级证书 (Graduate Certificate) | 78 |
| **学位项目总计 (UG Majors + Grad Degrees + Grad Certs)** | **329** |
| 学院 / 独立系所总数 | 16 (11 UG-degree-granting + 5 graduate/professional-only) |

> **Note**: The UH admissions page states "110+ Undergraduate Majors"; manual extraction from the Colleges & Degrees page yielded 107 distinct major names. The difference may include pre-professional tracks or recently added programs. Graduate counts are from the UH Graduate School pages (masters: ~90, doctoral/professional: ~54, certificates: 78). The Graduate School states "150 Master's, Doctoral and Professional Degrees" — the 144 count here may miss 6 programs listed on individual college sites but not on the Graduate School index.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
University of Houston
├── Gerald D. Hines College of Architecture + Design          [学院 - UG+Grad]
│   ├── Architecture                                          [系]
│   ├── Industrial Design                                     [系]
│   ├── Environmental Design                                  [系]
│   └── Interior Architecture                                 [系]
├── Kathrine G. McGovern College of the Arts                  [学院 - UG+Grad]
│   ├── School of Art                                         [系]
│   ├── Moores School of Music                                [系]
│   └── School of Theatre & Dance                             [系]
├── C.T. Bauer College of Business                            [学院 - UG+Grad]
│   ├── Department of Accountancy & Taxation                  [系]
│   ├── Department of Decision & Information Sciences         [系]
│   ├── Department of Finance                                 [系]
│   ├── Department of Management & Leadership                 [系]
│   ├── Department of Marketing & Entrepreneurship            [系]
│   └── Department of Supply Chain Management                 [系]
├── College of Education                                      [学院 - UG+Grad]
│   ├── Department of Curriculum & Instruction                [系]
│   ├── Department of Educational Leadership & Policy Studies [系]
│   └── Department of Psychological, Health & Learning Sciences [系]
├── Cullen College of Engineering                             [学院 - UG+Grad]
│   ├── Department of Aerospace Engineering                   [系] (via ME)
│   ├── Department of Biomedical Engineering                  [系]
│   ├── Department of Chemical & Biomolecular Engineering     [系]
│   ├── Department of Civil & Environmental Engineering       [系]
│   ├── Department of Electrical & Computer Engineering       [系]
│   ├── Department of Industrial & Systems Engineering        [系]
│   ├── Department of Materials Engineering                   [系]
│   ├── Department of Mechanical Engineering                  [系]
│   ├── Department of Petroleum Engineering                   [系]
│   └── Department of Subsea Engineering                      [系]
├── Cullen College of Engineering: Technology Division        [学院 - UG+Grad]
│   ├── Department of Construction Management                 [系]
│   ├── Department of Engineering Technology                  [系]
│   ├── Department of Human Development & Consumer Sciences   [系]
│   ├── Department of Information & Logistics Technology      [系]
│   └── Department of Technology                              [系]
├── Conrad N. Hilton College of Global Hospitality Leadership [学院 - UG+Grad]
│   └── Hospitality Leadership                                [系] (single-dept college)
├── College of Liberal Arts and Social Sciences (CLASS)       [学院 - UG+Grad]
│   ├── Department of Comparative Cultural Studies            [系]
│   ├── Department of Communication Sciences & Disorders      [系]
│   ├── Department of Communication                           [系]
│   ├── Department of Economics                               [系]
│   ├── Department of English                                  [系]
│   ├── Department of Health & Human Performance              [系]
│   ├── Department of Hispanic Studies                        [系]
│   ├── Department of History                                 [系]
│   ├── Department of Modern & Classical Languages            [系]
│   ├── Department of Philosophy                              [系]
│   ├── Department of Political Science                       [系]
│   ├── Department of Psychology                              [系]
│   ├── Department of Sociology                               [系]
│   ├── African American Studies Program                      [系]
│   ├── Women's, Gender & Sexuality Studies Program           [系]
│   └── School of Communication                               [系]
├── College of Natural Sciences and Mathematics (NSM)         [学院 - UG+Grad]
│   ├── Department of Biology & Biochemistry                  [系]
│   ├── Department of Chemistry                               [系]
│   ├── Department of Computer Science                        [系]
│   ├── Department of Earth & Atmospheric Sciences            [系]
│   ├── Department of Mathematics                             [系]
│   └── Department of Physics                                 [系]
├── Andy & Barbara Gessner College of Nursing                 [学院 - UG+Grad]
│   └── Nursing                                               [系] (single-dept college)
├── Hobby School of Public Affairs                            [学院 - UG+Grad]
│   └── Public Policy                                         [系]
├── Graduate College of Social Work                           [学院 - Grad-only]
│   └── Social Work                                           [系]
├── UH Law Center                                            [学院 - Grad-only]
│   └── Law                                                   [系]
├── College of Medicine                                       [学院 - Grad-only]
│   └── Medicine                                              [系]
├── College of Optometry                                      [学院 - Grad-only]
│   └── Optometry                                             [系]
└── College of Pharmacy                                       [学院 - Grad-only]
    └── Pharmacy                                              [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | ~35 |
| BS | BS | Bachelor of Science | 本科 | ~55 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 1 (Pre-Business → declared major) |
| BM | BM | Bachelor of Music | 本科 | ~8 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BArch | BArch | Bachelor of Architecture | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | ~18 |
| MS | MS | Master of Science | 研究生 | ~45 |
| MFA | MFA | Master of Fine Arts | 研究生 | ~5 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 (full-time + online) |
| MArch | MArch | Master of Architecture | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | ~8 |
| MM | MM | Master of Music | 研究生 | 1 (with concentrations) |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 1 (with specializations) |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 (with specializations) |
| MAT | MAT | Master of Athletic Training | 研究生 | 1 |
| MEMgmt | MEMgmt | Master of Engineering Management | 研究生 | 1 |
| MHM | MHM | Master of Hospitality Management (Executive) | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~42 |
| EdD | EdD | Doctor of Education | 研究生 | 1 (with specializations) |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 (with concentrations) |
| DBA | DBA | Doctor of Business Administration (Executive) | 研究生 | 1 |
| DGHL | DGHL | Doctorate of Global Hospitality Leadership | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| OD | OD | Doctor of Optometry | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 78 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BBA | BM | BSN | BArch | MA | MS | MFA | MBA | MEd | MM | MSW | MSN | MPP | MPA | LLM | PhD | EdD | DMA | Prof Doc | Cert | 合计 |
|------------|----|----|-----|-----|----|-----|-------|----|----|-----|-----|-----|----|----|-----|-----|-----|-----|-----|-----|------|----------|------|
| Architecture + Design | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 |
| McGovern Arts | 2 | 0 | 3 | 0 | 8 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 25 |
| Bauer Business | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 27 | 44 |
| Education | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 | 16 |
| Engineering | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 13 | 48 |
| Technology Division | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 20 |
| Hilton Hospitality | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 6 |
| CLASS | 25 | 3 | 0 | 0 | 0 | 0 | 0 | 9 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 7 | 58 |
| NSM | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 1 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 6 | 33 |
| Nursing | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Hobby Public Affairs | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 7 | 10 |
| Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 3 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 5 |
| **合计** | **27** | **54** | **3** | **7** | **8** | **1** | **1** | **14** | **45** | **3** | **2** | **6** | **1** | **1** | **3** | **1** | **1** | **1** | **31** | **1** | **1** | **5** | **75** | **291** |

> **Reconciliation note**: The matrix totals 291 program-degree rows. The Rule-1 count of 329 includes ~50 UG minors and some program variants (e.g., MArch is counted separately from MS Architecture). The matrix counts degree-granting program rows; minors and non-degree tracks are excluded from the matrix but included in the Rule-1 total. Graduate certificates verified against the Graduate School certificates page (74 confirmed; 78 in Rule-1 may include certificates listed on individual college pages but not on the centralized Graduate School index). Bauer Business certificates updated from 16 to 27 based on live site verification. Technology Division certificates updated from 8 to 1 (only Strategic Foresight listed on Graduate School page).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UH has 11 undergraduate-degree-granting colleges/schools plus 5 graduate/professional-only schools. See Section 0.2 for the full hierarchy tree. The Technology Division operates as a semi-autonomous unit within the Cullen College of Engineering.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Gerald D. Hines College of Architecture + Design

##### Architecture
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | BArch | https://www.uh.edu/undergraduate-admissions/academics/ |

##### Industrial Design
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 2 | Industrial Design | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

##### Environmental Design
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 3 | Environmental Design* | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

> *All new Environmental Design students should select Architecture as their major when applying.

##### Interior Architecture
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 4 | Interior Architecture | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Kathrine G. McGovern College of the Arts

##### School of Art
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Painting | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Art History | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Art | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Performance | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Dance | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Photography/Video | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Graphic Design | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 8 | Sculpture | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |

##### Moores School of Music
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 9 | Music | BM | https://www.uh.edu/undergraduate-admissions/academics/ |
| 10 | Music Therapy | BM | https://www.uh.edu/undergraduate-admissions/academics/ |
| 11 | Music Theory | BM | https://www.uh.edu/undergraduate-admissions/academics/ |

##### School of Theatre & Dance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 12 | Theatre | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 13 | Acting | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 14 | Playwriting & Dramaturgy | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 15 | Production & Design | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 16 | Stage Management | BFA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 17 | Theatre Education | BA | https://www.uh.edu/undergraduate-admissions/academics/ |

#### C.T. Bauer College of Business

> All new students are admitted as Pre-Business. Once required University and business core classes are completed, students declare a specific major.

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Management Information Systems | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Entrepreneurship | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Marketing | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Finance | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Supply Chain Management | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Management | BBA | https://www.uh.edu/undergraduate-admissions/academics/ |

#### College of Education

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Health | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Teaching and Learning | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Human Development and Family Studies | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Cullen College of Engineering

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Industrial Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Chemical Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Mechanical Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Civil Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Petroleum Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Computer Engineering and Analytics (Katy) | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 8 | Systems Engineering (Katy) | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 9 | Construction Engineering (Katy) | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 10 | Electrical Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 11 | Computer Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 12 | Aerospace Engineering | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Cullen College of Engineering: Technology Division

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biotechnology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Human Resource Development | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Computer Engineering Technology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Mechanical Engineering Technology (Sugar Land) | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Computer Information Systems (Sugar Land) | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Retailing and Consumer Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Construction Management | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 8 | Supply Chain and Logistics Technology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 9 | Digital Media | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 10 | Technology Leadership and Innovation Management | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 11 | Electrical Power Engineering Technology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Conrad N. Hilton College of Global Hospitality Leadership

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Global Hospitality Leadership | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### College of Liberal Arts and Social Sciences (CLASS)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | African American Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Journalism | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Liberal Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Anthropology | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Media Production | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Chinese Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Mexican American and Latino/a Applied Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 8 | Communication Sciences and Disorders | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 9 | Philosophy | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 10 | Communication Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 11 | Political Science | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 12 | Economics | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 13 | Psychology | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 14 | English | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 15 | Religious Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 16 | Exercise Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 17 | Sociology | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 18 | Exercise and Fitness Studies | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 19 | Spanish | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 20 | French | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 21 | Sport Administration | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 22 | Health Communication | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 23 | Strategic Communication | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 24 | History | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 25 | World Cultures and Literatures | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 26 | Human Nutrition and Foods | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 27 | Women's, Gender & Sexuality Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |
| 28 | Integrated Studies | BA | https://www.uh.edu/undergraduate-admissions/academics/ |

#### College of Natural Sciences and Mathematics (NSM)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Atmospheric Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 2 | Geology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 3 | Biochemical and Biophysical Sciences | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 4 | Geophysics | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 5 | Biology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 6 | Honors Biomedical Sciences | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 7 | Chemistry | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 8 | Mathematical Biology | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 9 | Computer Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 10 | Mathematics | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 11 | Earth Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 12 | Physics | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 13 | Environmental Sciences | BS | https://www.uh.edu/undergraduate-admissions/academics/ |
| 14 | Data Science | BS | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Andy & Barbara Gessner College of Nursing

> Nursing majors apply to UH as Pre-Nursing and apply for the BSN program once prerequisite coursework has been completed.

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BSN | https://www.uh.edu/undergraduate-admissions/academics/ |

#### Hobby School of Public Affairs

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy | BA/BS | https://www.uh.edu/undergraduate-admissions/academics/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

Pre-professional tracks (not standalone majors; advisors align degree plans with professional school prerequisites):
- Pre-Dentistry
- Pre-Pharmacy
- Pre-Law
- Pre-Physical Therapy
- Pre-Medicine
- Pre-Veterinary Medicine
- Pre-Optometry

### 1.4 Minors — Complete List

> UH offers approximately 50+ undergraduate minors. The complete list is available in the UH Undergraduate Catalog. Common minors include: Business Foundations, Communication, Computer Science, Creative Work, Data Science, Economics, Education, Energy, English, Entrepreneurship, History, Mathematics, Media Production, Music, Philosophy, Political Science, Psychology, Sociology, Spanish, Women's Gender & Sexuality Studies, and many more.

### 1.5 General/Institute-Wide Requirements

UH requires the Texas Core Curriculum (42 credit hours) for all undergraduate students, covering:
- Communication (6 hours)
- Mathematics (3 hours)
- Life and Physical Sciences (6 hours)
- Language, Philosophy and Culture (3 hours)
- Creative Arts (3 hours)
- American History (6 hours)
- Government/Political Science (6 hours)
- Social and Behavioral Sciences (3 hours)
- Component Area Option (6 hours)

### 1.6 Pre-Professional Tracks

| Track | Description |
|-------|-------------|
| Pre-Dentistry | Advisor aligns degree plan with dental school prerequisites |
| Pre-Pharmacy | Advisor aligns degree plan with pharmacy school prerequisites |
| Pre-Law | Advisor aligns degree plan with law school prerequisites |
| Pre-Physical Therapy | Advisor aligns degree plan with PT school prerequisites |
| Pre-Medicine | Advisor aligns degree plan with medical school prerequisites |
| Pre-Veterinary Medicine | Advisor aligns degree plan with vet school prerequisites |
| Pre-Optometry | Advisor aligns degree plan with optometry school prerequisites |

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### C.T. Bauer College of Business

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy (MSAcy) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Business Analytics (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Finance (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Management Information Systems (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | Management and Leadership (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 6 | Marketing (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 7 | Supply Chain Management (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 8 | Entrepreneurship (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 9 | Global Business Leadership (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 10 | Global Energy Leadership (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 11 | Real Estate (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 12 | Sales Leadership - Online (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Business Administration - Online (MBA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration - Accountancy (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Business Administration - Finance (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Business Administration - Management (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Business Administration - Management Information Systems (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Business Administration - Marketing (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | Business Administration - Supply Chain Management (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Professional Doctorate
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration - Executive (DBA) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Certificates (26)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Advanced Internal Audit | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Applied Data Analytics in Accounting | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Assurance/Finance Reporting | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | IT Systems Risk Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Oil & Gas Accounting | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Taxation | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 7 | Business Analytics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 8 | Business Modeling & Decision Making | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 9 | Supply Chain Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 10 | Corporate Finance | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 11 | Economics of the Energy Value Chain | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 12 | Energy Finance | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 13 | Energy Investment Analysis | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 14 | Energy Risk Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 15 | Financial Services Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 16 | Investment Analysis | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 17 | Investment Bank Private Equity | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 18 | Real Estate | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 19 | Business Consulting | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 20 | Digital Marketing Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 21 | Entrepreneurship | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 22 | Marketing Analysis | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 23 | Product Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 24 | Sales Leadership | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 25 | Global Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 26 | Human Resource Management | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 27 | Leadership Development | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### College of Education

##### MEd Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Administration & Supervision (MEd) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Counseling (MEd) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Curriculum & Instruction (MEd) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Higher Education (MEd) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | Special Populations (MEd) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### EdD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Leadership (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Certificates (6)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Designing and Developing Educational Multimedia | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Integrating Innovative Technologies in Health Science Education | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Mathematics Coaching | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | Online Teaching and Learning | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Special Education Specialist | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Alternative Certification Program | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### Cullen College of Engineering

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Biomedical Engineering (MSBE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Chemical Engineering (MSChE & MChE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Civil Engineering (MSCE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | Computer & Systems Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 6 | Electrical Engineering (MSEE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 7 | Engineering Data Science (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 8 | Environmental Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 9 | Geosensing Systems & Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 10 | Industrial Engineering (MSIE & MIE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 11 | Materials Science & Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 12 | Mechanical Engineering (MSME & MME) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 13 | Petroleum Engineering (MSPetE & MPetE) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 14 | Space Architecture (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 15 | Subsea Engineering (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### MEMgmt
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management (MEMgmt) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Chemical Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Civil Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Computer Science (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Electrical Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | Environmental Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 7 | Industrial Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 8 | Materials Science & Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 9 | Mechanical Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 10 | Petroleum Engineering (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Certificates (13)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Process Safety Engineering | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Global Climate, Energy, and Environment | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Power Systems and Smart Grid | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | Power Electronics and Renewable Energy | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Big Data and Energy Supply Chain | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Systems Engineering | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 7 | Subsea Engineering | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 8 | Advanced Subsea Engineering | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 9 | High Performance Computing | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 10 | Data Analytics and Condition Monitoring | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 11 | Corrosion Engineering | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 12 | Unconventional Energy Resources | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 13 | Engineering Data Science | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### Conrad N. Hilton College of Global Hospitality Leadership

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Hospitality Management (MS) | MS | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Hospitality Management, Executive (MHM) | MHM | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Global Hospitality Management (MS) | MS | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Hospitality Administration (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Doctorate of Global Hospitality Leadership (DGHL) | DGHL | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | Hospitality Decision Making & Analytics (Cert) | Certificate | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### College of Liberal Arts and Social Sciences (CLASS)

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Communication (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Communication Disorders (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Creative Writing (MFA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | English (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 6 | History (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 7 | Philosophy (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 8 | Political Science (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 9 | Spanish (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 10 | Sociology (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 11 | Sport & Fitness Administration (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 12 | Theatre (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Economics (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Athletic Training (MAT) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Foresight (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art (MFA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Creative Writing (MFA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Theatre (MFA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Counseling Psychology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Creative Writing & Literature (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Economics (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | English (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | History (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 7 | Industrial-Organizational Psychology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 8 | Political Science (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 9 | Psychology - Clinical (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 10 | School Psychology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 11 | Social Psychology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 12 | Spanish (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Certificates (7)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | African American Studies | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Empire Studies | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Translation Studies | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | Poetics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Sports & Fitness Operations | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Spanish as a Heritage Language | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 7 | Women's Studies | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### College of Natural Sciences and Mathematics (NSM)

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Biology (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Biomedical Sciences | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Chemistry (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | Computer Science (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 6 | Geology (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 7 | Geophysics (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 8 | Mathematics (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 9 | Mathematics (MA) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 10 | Physics (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 11 | Statistics and Data Analysis (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Biochemistry (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Biology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Chemistry (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Geology (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | Geophysics (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 7 | Geosensing Systems Engineering and Sciences (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 8 | Mathematics (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 9 | Physics (PhD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

##### Certificates (6)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Biomedical Science | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Interactive Game Development | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Geographic Information Systems | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | Hydrogeology | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Computational Mathematics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Financial Mathematics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### Andy & Barbara Gessner College of Nursing

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing - Family Nurse Practitioner (MSN) | MSN | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Nursing Administrator (MSN) | MSN | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Nursing Education (MSN) | MSN | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

#### College of Pharmacy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmacy (PharmD) | PharmD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Pharmacy Leadership & Administration (MS) | MS | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Pharmaceutical Health Outcomes & Policy (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Pharmaceutics (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Pharmacology (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### College of Optometry

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Optometry (OD) | OD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Physiological Optics/Vision Science (MS) | MS | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Physiological Optics (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### UH Law Center

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law (JD) | JD | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Law (LLM) | LLM | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### LLM Specializations
- Energy, Environment and Natural Resources Law
- Health Law
- Intellectual Property & Information Law
- International Law
- Tax Law
- U.S. Law

#### College of Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medicine (MD) | MD | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### College of Education — Doctoral Programs

| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Leadership - Health Science Education (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Professional Leadership - K-12 Leadership (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Professional Leadership - Literacy Education (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Professional Leadership - Mathematics Education (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Professional Leadership - Social Studies/Social Education (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 6 | Professional Leadership - Special Populations (EdD) | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### McGovern College of the Arts — Doctoral Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music - Collaborative Piano (DMA) | DMA | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 2 | Music - Composition (DMA) | DMA | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 3 | Music - Conducting (DMA) | DMA | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 4 | Music - Music Education (DMA) | DMA | https://www.uh.edu/graduate-school/academics/doctoral-programs |
| 5 | Music - Performance (DMA) | DMA | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### Graduate College of Social Work

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work (MSW) | MSW | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Social Work (PhD) | PhD | https://www.uh.edu/graduate-school/academics/doctoral-programs |

#### Technology Division — Graduate Programs

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Management (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Engineering Technology (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 3 | Human Resources Development (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 4 | Human Resources Development, Executive (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 5 | Human Resource Leadership (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 6 | Industrial Design (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 7 | Global Retailing (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 8 | Supply Chain and Logistics Technology (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 9 | Technology Project Management (MS) | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### Certificates (1 — on Graduate School page)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Strategic Foresight | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

> **Note**: The Technology Division graduate certificates page on the Graduate School site lists only "Strategic Foresight" as of July 2026. Other Technology Division credentials (Construction Management, Engineering Technology, Foresight, Global Retailing, Human Resource Development, Supply Chain and Logistics Technology, Technology Project Management) may be offered as graduate certificates through the Technology Division directly but are not listed on the centralized Graduate School certificates page. Verification needed.

#### Hobby School of Public Affairs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy (MPP) | MPP | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |
| 2 | Public Administration (MPA) | MPA | https://www.uh.edu/graduate-school/academics/masters-degree-programs/ |

##### Certificates (7)
| # | Certificate | URL |
|---|-------------|-----|
| 1 | Public Policy | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 2 | Public Policy - Data Analytics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 3 | Public Policy - Energy Policy | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 4 | Public Policy - Ethics | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 5 | Public Policy - Health Care Policy | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 6 | Public Policy and Public Administration | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |
| 7 | Public Policy - Infrastructure Policy and Population Health | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

#### UH Energy

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Upstream Energy Safety | https://www.uh.edu/graduate-school/academics/graduate-certificates/ |

### 2.2 Dual-Degree Programs (30 total)

#### Internal Dual Degrees
| # | Combination | URL |
|---|-------------|-----|
| 1 | JD + MBA | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 2 | JD + MA History | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 3 | JD + MSW | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 4 | JD + MPA | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 5 | JD + MPP | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 6 | JD + LLM | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 7 | MSW + PhD Social Work | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 8 | MSW + MPP | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 9 | MSW + MBA | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 10 | MBA + PharmD | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 11 | MBA + MS Hospitality Management | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 12 | MBA + MIE Industrial Engineering | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 13 | MS Aerospace Engineering + MS Space Architecture | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 14 | MS Mechanical Engineering + MS Subsea Engineering | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 15 | MS Mechanical Engineering + MS Aerospace Engineering | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 16 | MS Petroleum Engineering + MS Subsea Engineering | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 17 | PharmD + PhD Pharmaceutics | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 18 | PharmD + PhD Pharmacology | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 19 | MA Applied Economics + PhD Pharmaceutical Health Outcomes & Policy | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 20 | OD + MS Physiological Optics | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 21 | OD + PhD Physiological Optics | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 22 | MA Applied Economics + MPP | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 23 | MA Art History + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 24 | MFA Studio Art + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 25 | Master of Music + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 26 | DMA + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 27 | MA Theatre + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 28 | MFA Theatre + MA Arts Leadership | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |

#### Joint Dual Degrees with Partner Institutions
| # | Combination | Partner | URL |
|---|-------------|---------|-----|
| 1 | JD + MPH | UTHSC-Houston | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 2 | JD + JD | University of Calgary | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 3 | JD + PhD Medical Humanities | UTMB-Galveston | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 4 | JD + MD | Baylor College of Medicine | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |
| 5 | MSW + MPH | UTHSC-Houston | https://www.uh.edu/graduate-school/academics/dual-degree-programs/ |

### 2.3 Accelerated Pathway Programs (4+1)

| # | Combination | College | URL |
|---|-------------|---------|-----|
| 1 | BBA/MPP | Bauer + Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 2 | BA/MA Political Science | CLASS | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 3 | BA/BS Liberal Studies (Honors)/JD | CLASS + Law | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 4 | BS/MS Computer Science | NSM | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 5 | BS Hotel & Restaurant Management/MS Hospitality Management | Hilton | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 6 | BSIE/MBA | Engineering + Bauer | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 7 | BA/BS Economics/MPP | Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 8 | BA/BS Liberal Studies (Honors)/MPP | Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 9 | BA/BS Psychology/MPP | Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 10 | BA/BS Public Policy/MPP | Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 11 | BA Philosophy/MPP | Hobby | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 12 | BS/MS Human Resource Development | Technology | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 13 | BS Biotechnology/MS Engineering Technology | Technology | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 14 | BS Computer Information Systems/MS Information Systems Security | Technology | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |
| 15 | BS Retailing & Consumer Science/MS Global Retailing | Technology | https://www.uh.edu/graduate-school/academics/accelerated-pathway-programs/ |

### 2.4 Graduate Admissions Model

UH uses a **centralized application system** (ApplyWeb) for most graduate programs, but **professional programs** (Law, Medicine, Optometry, Pharmacy, Nursing) use separate application platforms. Each college/department sets its own deadlines, GRE requirements, and supplemental materials. The Graduate School serves as the processing hub but admissions decisions are made at the department level.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application Portal | Common App or ApplyTexas | UG Admissions |
| Application Fee (Domestic) | $75 | Freshman Admissions Process |
| Application Fee (International) | $90 | Freshman Admissions Process |
| Fee Waiver | Available via NACAC form | Freshman Admissions Process |
| SAT Code | 6870 | Freshman Admissions Process |
| ACT Code | 4236 | Freshman Admissions Process |
| FAFSA Code | 003652 | Freshman Admissions |
| **Fall 2027 Scholarship Priority Deadline** | **Nov. 2, 2026** (Application) / **Nov. 9, 2026** (Supporting Info) | UG Admissions |
| **Fall 2027 Final Deadline** | **May 31, 2027** (Application) / **June 7, 2027** (Supporting Info) | UG Admissions |
| Spring 2027 Deadline | Dec. 1, 2026 (Application) / Dec. 11, 2026 (Supporting Info) | UG Admissions |
| Summer 2027 Deadline | May 3, 2027 (Application) / May 10, 2027 (Supporting Info) | UG Admissions |
| Test Policy | **Test Optional through June 1, 2030** | Test Optional Admissions |
| Superscore | No — uses highest total/composite from one test date | Test Optional Admissions |
| Score Age Limit | 5 years (Texas Success Initiative) | Freshman Admissions Process |
| Recommendation | Not required (essay + extracurriculars required) | Freshman Admissions Process |
| Interview | Not offered | UG Admissions |

> **Note on EA/RD**: The user-provided information states "EA Nov 1, RD Feb 1." The UH website shows a **Scholarship Priority Deadline of Nov. 2, 2026** for Fall 2027, which functions as an early deadline. The general Fall application deadline is **May 31, 2027**. UH does not use traditional EA/RD labels — the Nov. 2 date is for scholarship priority consideration, and applications are accepted on a rolling basis until May 31. The Feb. 1 date was not found on the current UH website and may refer to a previous year's deadline or a specific program deadline.

> **New 2027 Requirements (starting Aug. 1, 2026)**: UH is implementing new automatic admission pathways for Fall 2027+ applicants:
> - **Assured Pathway 1**: Top 10% of graduating class
> - **Assured Pathway 2**: 3.5+ unweighted GPA
> - **Assured Pathway 3**: 1250+ SAT or 26+ ACT
> Students not meeting automatic admission requirements will undergo individual review using their Common App/ApplyTexas essay and resume.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended | Notes |
|------|--------------|-------------|-------|
| TOEFL iBT | 79 | — | Scores expire 2 years after test date |
| IELTS Overall | 6.5 | — | Scores expire 2 years after test date |
| Duolingo English Test | 105 | — | Scores expire 2 years after test date |

**Exemptions**: Applicants who meet ANY of the following are exempt:
- Earned a high school diploma, AA, AS, bachelor's degree or higher from an accredited U.S. institution
- Completed equivalent of U.S. bachelor's degree in a recognized English-speaking country (full list includes 40+ countries)
- Completed Level 6 of UH's Intensive English Program

**TOEFL Institution Code**: 6870

### 3.3 Graduate — Global Rules

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | ApplyWeb (centralized) | Graduate School |
| Application Fee (Domestic) | $50 | How to Apply |
| Application Fee (International) | $80 | How to Apply |
| Application Fee (Non-degree/Certificate) | $25 | How to Apply |
| ETS Code | 6870 | How to Apply |
| GRE Policy | Per-program; waiver available for UH alumni with min GPA (3.0-3.6 depending on program) | GRE/GMAT Waiver |
| TOEFL iBT Minimum | 79 | English Proficiency |
| IELTS Minimum | 6.5 | English Proficiency |
| Duolingo Minimum | 105 | English Proficiency |
| PTE Minimum | 53 | English Proficiency |
| Score Validity | TOEFL/IELTS/PTE/Duolingo: 2 years; GRE/GMAT: 5 years | How to Apply |
| CGS April-15 Signatory | Not confirmed | — |

> **Note**: Professional programs (Law, Medicine, Optometry, Pharmacy, Nursing) use separate application platforms: LSAC (Law), AMCAS (Medicine), OptomCAS (Optometry), PharmCAS (Pharmacy), NursingCAS (Nursing).

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-26 Academic Year)

| Expense Item | In-State (per year) | Out-of-State (per year) | Notes |
|-------------|-------------------|------------------------|-------|
| Tuition (2 x 15-hour semesters) | $11,888 | $27,776 | Estimated; varies by college |
| Student Fees | ~$2,000-3,000 | ~$2,000-3,000 | Includes student services, UC fee, recreation |
| Housing (Moody Towers Double, 2 semesters) | $6,358 | $6,358 | 2026-27 rate: $3,274/semester |
| Housing (Cougar Village Double, 2 semesters) | $8,014 | $8,014 | 2026-27 rate: $4,007/semester |
| Meal Plan (required for on-campus residents) | ~$4,500-5,500 | ~$4,500-5,500 | Exact rate varies by plan |
| Books & Supplies | ~$1,000-1,200 | ~$1,000-1,200 | Estimate |
| Personal/Miscellaneous | ~$2,000-3,000 | ~$2,000-3,000 | Estimate |
| Transportation | ~$1,500-2,500 | ~$1,500-2,500 | Estimate |
| **Estimated Total (on-campus)** | **~$29,000-32,000** | **~$45,000-48,000** | Varies by housing choice |

> **Note**: UH's tuition page states "Tuition and Fee costs do not include the cost of room and board." The tuition figure includes consolidated tuition + incidental fees based on major + mandatory fees (student services, UC fee, recreation and wellness fee). The COA breakdown (housing, meals, books, personal) is estimated based on typical Texas public university costs; the UH website provides an interactive Tuition Calculator rather than a static COA table.

### 4.2 Undergraduate Financial-Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| Need-Blind/Need-Aware | **Need-aware for all** (domestic and international) | UG Admissions; Financial Aid pages |
| Merit Scholarships | Available — university-funded, college-specific, state-funded | Cost & Aid page |
| International Scholarships | Available; OOS/intl students receiving $1,000+ in UH scholarships may qualify for OOS tuition waiver | Cost & Aid page |
| Scholarship Universe | Online tool for finding UH + external scholarships | Cost & Aid page |
| **Cougar Promise** | **Tuition and fees covered for families with adjusted gross income ≤ $65,000; partial tuition support for income $65,001–$125,000.** Must be Texas resident, submit admissions docs by Jan. 15, complete 2026-27 FAFSA/TASFA by state priority deadline (Jan. 15, 2026). | Incoming Freshman page |
| Tuition-Free Threshold | ≤ $65,000 (Cougar Promise, TX residents only) | Incoming Freshman page |
| Loan Programs | Federal Direct Loans, PLUS Loans, alternative/private loans | Financial Aid page |
| Work-Study | Available (waitlist for 2026-27) | Financial Aid page |

### 4.3 Graduate Cost & Funding Framework

| Field | Value | Source |
|-------|-------|--------|
| Tuition | Varies by department, residency, and level | Graduate School |
| Application Fee | $50 domestic / $80 international / $25 non-degree | How to Apply |
| Graduate Assistantships | Available (tuition waiver + stipend) | Cost & Aid |
| Fellowships & Awards | Available (Outstanding Thesis/Dissertation awards, external scholarships) | Cost & Aid |
| Tuition Waivers | Available for eligible students | Cost & Aid |
| Fast Track Admissions | Simplified pathway for UH undergrads/alumni to select master's programs | Graduate School |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.tuition.in_state_2025_2026
  value: "$11,888"
  source_url: "https://www.uh.edu/undergraduate-admissions/cost-and-aid/"
  source_snippet: "Tuition and fees are based on two 15-hour semesters in the 2025–26 academic year. This is an estimate as costs may vary based on your academic college. $11,888 in-state tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.tuition.out_of_state_2025_2026
  value: "$27,776"
  source_url: "https://www.uh.edu/undergraduate-admissions/cost-and-aid/"
  source_snippet: "$27,776 out-of-state tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.fall_2027_scholarship_priority
  value: "Nov. 2, 2026 (Application) / Nov. 9, 2026 (Supporting Info)"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "Fall 2027 Scholarship Priority Deadline Application Due: Nov. 2, 2026 Supporting Information Due: Nov. 9, 2026"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.fall_2027_final
  value: "May 31, 2027 (Application) / June 7, 2027 (Supporting Info)"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "Fall 2027 Application Due: May 31, 2027 Supporting Information* Due: June 7, 2027"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.test_policy
  value: "Test Optional through June 1, 2030"
  source_url: "https://www.uh.edu/undergraduate-admissions/resources/test-optional-admissions/"
  source_snippet: "Freshman applicants have the option to apply for admission with or without a test score through June 1, 2030. This includes all academic terms through Fall 2030."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency
  value: "TOEFL 79 / IELTS 6.5 / Duolingo 105"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/international/english-language-requirements/"
  source_snippet: "TOEFL (iBT) 79 | IELTS Overall 6.5 | Duolingo English Test 105"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.application_fee.domestic
  value: "$75"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/freshman-admissions-process/"
  source_snippet: "Pay the nonrefundable $75 application fee ($90 for international students)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.application_fee.international
  value: "$90"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/freshman-admissions-process/"
  source_snippet: "Pay the nonrefundable $75 application fee ($90 for international students)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.admissions_requirements.with_test_score
  value: "Top 10%: Assured; 11-25%: SAT 1080/ACT 21; 26-50%: SAT 1170/ACT 24; 51%+: Individual Review"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "Requirements With Test Score Class Rank SAT or ACT Admission Type Top 10% No Minimum No Minimum Assured Admission 11-25% 1080 21 Assured Admission 26-50% 1170 24 Assured Admission 51% and Lower, No Rank - - Individual Review"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.program_count
  value: "110+ undergraduate majors"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "We have more than 110 majors to choose from."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.cougar_promise
  value: "Tuition and fees covered for families with AGI ≤ $65,000; partial support for $65,001–$125,000 (TX residents only)"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "Cougar Promise — We'll cover tuition and fees for those with an adjusted gross family income at or below $65,000. Tuition support is provided for those with an adjusted gross family income between $65,001 and $125,000. You must be a Texas resident, submit all required admissions documents by Jan. 15 and have completed the 2026-27 FAFSA or TASFA by the state of Texas priority deadline to be considered."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.admissions.new_2027_requirements
  value: "Three assured pathways starting Aug 1, 2026: Top 10%, 3.5+ GPA, or 1250+ SAT / 26+ ACT"
  source_url: "https://www.uh.edu/undergraduate-admissions/apply/incoming-freshman/"
  source_snippet: "New Requirements Starting Aug. 1, 2026 — Receive automatic admission by meeting one of the following academic requirements. Assured Pathway 1: Top 10%. Assured Pathway 2: 3.5+ GPA. Assured Pathway 3: 1250+ on SAT or 26+ ACT."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee.domestic
  value: "$50"
  source_url: "https://www.uh.edu/graduate-school/admissions/how-to-apply/index.php"
  source_snippet: "Application fees are $50 for domestic applicants, $80 for international applicants and $25 for non-degree (Certificate based programs)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_fee.international
  value: "$80"
  source_url: "https://www.uh.edu/graduate-school/admissions/how-to-apply/index.php"
  source_snippet: "Application fees are $50 for domestic applicants, $80 for international applicants and $25 for non-degree (Certificate based programs)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency
  value: "TOEFL 79 / IELTS 6.5 / Duolingo 105 / PTE 53"
  source_url: "https://www.uh.edu/graduate-school/admissions/international-applicants/english-proficiency/index.php"
  source_snippet: "Internet based Test (iBT): An overall score of 79 or higher. The minimum IELTS score required is an overall score of a 6.5. A minimum score of 105 is required. The minimum required score for PTE is an overall score of 53 or higher."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.program_count
  value: "150 Master's, Doctoral and Professional Degrees"
  source_url: "https://www.uh.edu/graduate-school/"
  source_snippet: "150 Master's, Doctoral and Professional Degrees"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-005:
  field: graduate.online_programs
  value: "15 Fully Online Master's Programs"
  source_url: "https://www.uh.edu/graduate-school/"
  source_snippet: "15 Fully Online Master's Programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-006:
  field: housing.moody_towers_double_2026_2027
  value: "$3,274 per semester"
  source_url: "https://www.uh.edu/housing/prospective-residents/housing-rate-sheet/index.php"
  source_snippet: "Moody Towers Double* $3,179 N/A $3,274"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-007:
  field: housing.cougar_village_double_2026_2027
  value: "$4,007 per semester"
  source_url: "https://www.uh.edu/housing/prospective-residents/housing-rate-sheet/index.php"
  source_snippet: "Cougar Village I - 2 Bedroom Double* $3,890 N/A $4,007"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uh-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-architecture-design.md        (Section 1: Architecture + Design programs)
├── 02-ug-arts.md                       (Section 1: McGovern Arts programs)
├── 03-ug-business.md                   (Section 1: Bauer Business programs)
├── 04-ug-education.md                  (Section 1: Education programs)
├── 05-ug-engineering.md                (Section 1: Engineering programs)
├── 06-ug-technology.md                 (Section 1: Technology Division programs)
├── 07-ug-hospitality.md                (Section 1: Hilton Hospitality programs)
├── 08-ug-liberal-arts.md               (Section 1: CLASS programs)
├── 09-ug-natural-sciences.md           (Section 1: NSM programs)
├── 10-ug-nursing.md                    (Section 1: Nursing programs)
├── 11-ug-public-affairs.md             (Section 1: Hobby School programs)
├── 12-grad-business.md                 (Section 2: Bauer grad programs)
├── 13-grad-education.md                (Section 2: Education grad programs)
├── 14-grad-engineering.md              (Section 2: Engineering grad programs)
├── 15-grad-hospitality.md              (Section 2: Hilton grad programs)
├── 16-grad-liberal-arts.md             (Section 2: CLASS grad programs)
├── 17-grad-natural-sciences.md         (Section 2: NSM grad programs)
├── 18-grad-nursing.md                  (Section 2: Nursing grad programs)
├── 19-grad-pharmacy.md                 (Section 2: Pharmacy grad programs)
├── 20-grad-optometry.md                (Section 2: Optometry grad programs)
├── 21-grad-law.md                      (Section 2: Law programs)
├── 22-grad-medicine.md                 (Section 2: Medicine programs)
├── 23-grad-social-work.md              (Section 2: Social Work programs)
├── 24-grad-public-affairs.md           (Section 2: Hobby School grad programs)
├── 25-grad-technology.md               (Section 2: Technology Division grad programs)
├── 26-deadlines-requirements.md        (Section 3)
├── 27-costs-financial-aid.md           (Section 4)
├── 28-evidence-chain.md                (Section 5)
└── 29-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "uh-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BFA|BBA|BM|BSN|MA|MS|MFA|MBA|PhD|EdD|DMA|...>"
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
| P0 | Complete COA line-item breakdown (housing, meals, books, personal) from UH Tuition Calculator | UH Tuition Calculator |
| P0 | Complete UG minor list (~50+) from UH Undergraduate Catalog | UH Undergraduate Catalog |
| P0 | Verify Technology Division certificates (only 1 confirmed on Grad School page; 7 previously listed may be on Tech Division site) | Technology Division website |
| P1 | Exact BA/BS/BFA/BM/BSN split per program | UH Undergraduate Catalog |
| P1 | Per-program GRE requirements (currently only waiver info) | Individual program pages |
| P1 | Graduate application deadlines per department (partially captured) | Graduate School deadlines page |
| P1 | Verify Cougar Promise eligibility details and current income thresholds | UH Financial Aid |
| P2 | Graduate COA breakdown | Graduate Financial Aid |
| P2 | International student scholarship amounts | UH Financial Aid |
| P2 | Online program details | Graduate School Online Programs |
| P2 | Honors College programs | UH Honors College |
| P2 | Verify NSM "Data Science" BS (listed on document but not on admissions page) | NSM website |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UH Value | Notes |
|-----------|----------|-------|
| Institution Type | Public (UH System) | Houston, TX |
| UG Tuition (in-state/yr) | $11,888 | 2025-26, two 15-hr semesters |
| UG Tuition (OOS/yr) | $27,776 | 2025-26, two 15-hr semesters |
| UG COA estimate (on-campus) | ~$29,000-32,000 (IS) / ~$45,000-48,000 (OOS) | Estimated |
| Need-Blind (Domestic) | No — need-aware | — |
| Need-Blind (International) | No — need-aware | — |
| Cougar Promise (TX residents) | Tuition covered if AGI ≤ $65k; partial if $65k–$125k | Must submit FAFSA/TASFA by Jan. 15 |
| EA Deadline | Nov. 2, 2026 (Scholarship Priority) | Not labeled "EA" |
| RD Deadline | May 31, 2027 (Final) | Rolling until May 31 |
| SAT/ACT Required? | No — test optional through June 2030 | — |
| TOEFL Minimum (UG) | 79 | — |
| IELTS Minimum (UG) | 6.5 | — |
| Duolingo Minimum (UG) | 105 | — |
| Application Fee (UG) | $75 domestic / $90 international | — |
| Application Fee (Grad) | $50 domestic / $80 international | — |
| Total Programs (Rule 1) | 329 | 107 UG majors + ~144 grad degrees + 78 grad certs (74 verified on Grad School page) |
| School/Department Count (Rule 2) | 16 colleges/schools | 11 UG + 5 grad-only |
| Graduate Programs | 150+ degrees + 78 certificates | — |
| Strong Programs | Hotel Management, Energy, Engineering, Business | Hilton College is nationally ranked |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: uh.edu, www.uh.edu/undergraduate-admissions, www.uh.edu/graduate-school, www.uh.edu/housing, www.uh.edu/financial
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
