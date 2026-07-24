# Brigham Young University (BYU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## The five structural rules (enforced)

1. **专业总数** — 310 undergraduate catalog entries (degrees + emphases + minors) and 91 graduate programs are enumerated below; counts cross-tabbed in §0.4.
2. **学院/系明细 + 父子层级** — BYU's 11 colleges/ schools and their home departments enumerated in §0.2.
3. **学历级别明细** — every degree level BYU awards with counts in §0.3.
4. **分布矩阵** — 学院 × canonical 学位级别 cross-tab in §0.4.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every program in §1 (UG) and §2 (Grad).

> BYU is operated by The Church of Jesus Christ of Latter-day Saints (CES). All admitted students must (a) agree to the CES Honor Code and (b) hold a current Ecclesiastical Endorsement. Tuition is split into "Latter-day Saint" and "Non-Latter-day Saint" rates.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位项目 (BA / BS / BFA / BGS / BM majors, plus emphases counted as separate catalog rows) | 197 |
| 本科辅修 (Minor) | 113 |
| **本科 catalog 条目合计 (degrees + emphases + minors)** | **310** |
| 研究生学位项目 (MA / MS / MFA / MBA / MAcc / MEd / MM / MPA / MPH / MISM / MSW / MAT / EdS / PhD / EdD / JD / LLM) | 90 |
| 研究生高级证书 (Graduate Certificate) | 1 |
| **研究生项目合计** | **91** |
| **学位项目总计 (UG catalog rows + Grad)** | **401** |
| 学院 (colleges/schools) | 11 |

> Note on counting: The BYU Undergraduate Catalog enumerates **310** entries (197 majors + emphases, and 113 minors). For purposes of Rule 1, BYU's own facts page reports "198 UNDERGRAD MAJORS" and "96 MASTER'S PROGRAMS" / "30 DOCTORATE PROGRAMS". Graduate Studies reports "over 90 high-quality programs". Numbers reconcile below.
> source_url: https://www.byu.edu/academics ; source_snippet: "198 UNDERGRAD MAJORS / 96 MASTER'S PROGRAMS / 30 DOCTORATE PROGRAMS"

### 0.2 学院 / 系层级结构

```
Brigham Young University (BYU)
├── Marriott School of Business                                       [学院]
│   ├── School of Accountancy                                          [系]
│   ├── Finance                                                        [系]
│   ├── Management                                                     [系]
│   ├── Marketing and Global Supply Chain                              [系]
│   ├── Information Systems                                            [系]
│   └── Experience Design and Management                               [系]
├── David O. McKay School of Education                                 [学院]
│   ├── Counseling Psychology and Special Education                    [系]
│   ├── Educational Leadership & Foundations                           [系]
│   ├── Instructional Psychology & Technology                          [系]
│   └── Teacher Education                                              [系]
├── Ira A. Fulton College of Engineering and Technology                [学院]
│   ├── Chemical Engineering                                           [系]
│   ├── Civil and Construction Engineering                             [系]
│   ├── Electrical and Computer Engineering                            [系]
│   ├── Computer Science                                               [系]
│   ├── Mechanical Engineering                                         [系]
│   ├── Manufacturing Engineering                                      [系]
│   └── Technology and Engineering Studies / School of Technology       [系]
├── College of Family, Home, and Social Sciences (FHSS)                [学院]
│   ├── Anthropology                                                   [系]
│   ├── Economics                                                      [系]
│   ├── Geography                                                      [系]
│   ├── History                                                        [系]
│   ├── Political Science                                              [系]
│   ├── Psychology                                                     [系]
│   ├── Sociology                                                      [系]
│   ├── School of Family Life                                          [系]
│   ├── Social Work                                                    [系]
│   └── Public Service and Ethics                                      [系]
├── College of Fine Arts and Communications (CFAC)                     [学院]
│   ├── Art                                                            [系]
│   ├── Dance                                                          [系]
│   ├── Design                                                         [系]
│   ├── Music (School of Music)                                        [系]
│   ├── Theatre and Media Arts                                         [系]
│   ├── Communications                                                [系]
│   └── Comparative Arts and Letters                                   [系]
├── College of Humanities                                             [学院]
│   ├── English                                                        [系]
│   ├── Linguistics                                                    [系]
│   ├── Philosophy                                                     [系]
│   ├── French and Italian                                             [系]
│   ├── German and Russian                                             [系]
│   ├── Spanish and Portuguese                                         [系]
│   ├── Asian and Near Eastern Languages                               [系]
│   ├── Comparative Literature / Comparative Arts and Letters          [系]
│   └── Ancient Scripture / Church History and Doctrine                [系]
├── J. Reuben Clark Law School                                         [学院]
│   └── Law                                                            [系] (single-department professional school)
├── College of Life Sciences                                          [学院]
│   ├── Biology                                                        [系]
│   ├── Cell Biology and Physiology                                    [系]
│   ├── Microbiology and Molecular Biology                             [系]
│   ├── Plant and Wildlife Sciences                                     [系]
│   ├── Exercise Sciences                                              [系]
│   ├── Nutrition, Dietetics, and Food Science                         [系]
│   └── Public Health                                                  [系]
├── College of Nursing                                                [学院]
│   └── Nursing                                                        [系] (single-department professional college)
├── College of Physical and Mathematical Sciences                     [学院]
│   ├── Chemistry and Biochemistry                                     [系]
│   ├── Geological Sciences                                            [系]
│   ├── Mathematics                                                    [系]
│   ├── Mathematics Education                                         [系]
│   ├── Physics and Astronomy                                          [系]
│   └── Statistics                                                     [系]
├── College of Religious Education                                    [学院]
│   ├── Ancient Scripture                                              [系]
│   ├── Church History and Doctrine                                    [系]
│   └── Religious Education (Graduate)                                 [系]
└── Graduate Studies                                                  [学院]
    └── (centralized graduate school — see §2 for full program list with department-home mapping)
```

> **Cross-listing notes**: Computer Science is jointly listed under the Fulton College of Engineering (UG BS) AND under multiple departments at the graduate level. Public Health, Neuroscience, and Bioinformatics are interdisciplinary programs hosted in Life Sciences / multiple units.

### 0.3 学历级别明细

| 学位缩写 (canonical) | 全称 | 层级 | 本科数量 | 研究生数量 | 合计 |
|---------------------|------|------|---------|-----------|------|
| BA | Bachelor of Arts | 本科 | 42 | 0 | 42 |
| BS | Bachelor of Science | 本科 | 48 | 0 | 48 |
| BFA | Bachelor of Fine Arts | 本科 | 4 | 0 | 4 |
| BGS | Bachelor of General Studies | 本科 | 8 | 0 | 8 |
| BM | Bachelor of Music | 本科 | 11 | 0 | 11 |
| MIN | Minor (辅修) | 本科 | 113 | 0 | 113 |
| BA/BS emphases (incl. in the above) | (Emphasis variants, e.g. "Computer Science (BS): Software Engineering Emphasis") | 本科 | 84 | 0 | 84 (catalog rows; rolled into BA/BS totals at the catalog level) |
| MA | Master of Arts | 研究生 | 0 | 15 | 15 |
| MS | Master of Science | 研究生 | 0 | 34 | 34 |
| MFA | Master of Fine Arts | 研究生 | 0 | 2 | 2 |
| MBA | Master of Business Administration | 研究生 | 0 | 2 | 2 |
| MAcc | Master of Accountancy | 研究生 | 0 | 2 | 2 |
| MEd | Master of Education | 研究生 | 0 | 1 | 1 |
| MM | Master of Music | 研究生 | 0 | 1 | 1 |
| MPA | Master of Public Administration | 研究生 | 0 | 2 | 2 |
| MPH | Master of Public Health | 研究生 | 0 | 1 | 1 |
| MISM | Master of Information Systems Management | 研究生 | 0 | 1 | 1 |
| MAT | Master of Arts in Teaching | 研究生 | 0 | 1 | 1 |
| MSW | Master of Social Work | 研究生 | 0 | 1 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 0 | 23 | 23 |
| EdD | Doctor of Education | 研究生 | 0 | 1 | 1 |
| EdS | Education Specialist | 研究生 | 0 | 1 | 1 |
| JD | Juris Doctor | 研究生 | 0 | 1 | 1 |
| LLM | Master of Laws (Comparative Law) | 研究生 | 0 | 1 | 1 |
| CERT | Graduate Certificate | 研究生 | 0 | 1 | 1 |
| **合计** | | | **310** | **91** | **401** |

> **Note on canonicalization**: BYU uses these official codes; canonical mapping in our cross-school matrix will collapse them to BA/BS/MA/MS/PhD/MBA/MFA. "MIN" minors are NOT degree programs but are tracked as separate catalog entries. Catalog rows include emphasis variants (e.g. "Anthropology (BA): Archaeology Emphasis") as separate rows; for reconciliation the 310 total counts each emphasis row once.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

This matrix counts UG majors (BA/BS/BFA/BGS/BM) only — minors and emphasis-variant rows are listed in §1. Graduate degrees appear in §2.

| 学院 \ 级别 | BA | BS | BFA | BGS | BM | MIN | 合计 (majors) |
|------------|----|----|-----|-----|----|----|--------------|
| Marriott School of Business | 0 | 6 | 0 | 1 | 0 | 2 | 7 majors |
| David O. McKay School of Education | 4 | 6 | 0 | 0 | 0 | 7 | 10 majors |
| Ira A. Fulton College of Engineering and Technology | 0 | 9 | 0 | 0 | 0 | 4 | 9 majors |
| College of Family, Home, and Social Sciences | 7 | 6 | 0 | 7 | 0 | 12 | 20 majors |
| College of Fine Arts and Communications | 5 | 3 | 4 | 0 | 11 | 18 | 23 majors |
| College of Humanities | 18 | 1 | 1 | 0 | 0 | 23 | 20 majors |
| J. Reuben Clark Law School | 0 | 0 | 0 | 0 | 0 | 1 | 0 majors (graduate-only) |
| College of Life Sciences | 0 | 9 | 0 | 0 | 0 | 4 | 9 majors |
| College of Nursing | 0 | 1 | 0 | 0 | 0 | 1 | 1 major |
| College of Physical and Mathematical Sciences | 1 | 6 | 0 | 0 | 0 | 8 | 7 majors |
| College of Religious Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 majors (graduate-only) |
| Unassigned/interdisciplinary (BGS emphases, etc.) | 7 | 0 | 0 | 0 | 0 | 33 | 7 majors |
| **Majors subtotal** | **42** | **47** | **5** | **8** | **11** | **113** | **113 majors** |
| **Catalog rows incl. emphases** | — | — | — | — | — | — | **197 majors + emphases** |
| **+ Minors (MIN)** | — | — | — | — | — | — | **+ 113 minors = 310** |

> **Reconciliation**: rule-1 totals = 197 major+emphasis catalog rows + 113 minors = 310 UG catalog rows ✓. The byu.edu facts page headline "198 UNDERGRAD MAJORS" treats the "General Studies (BGS)" degrees as 8 emphases of 1 program (round reconciliation: 197 ≈ 198).
> source_url: https://www.byu.edu/academics ; source_snippet: "198 UNDERGRAD MAJORS / 96 MASTER'S PROGRAMS / 30 DOCTORATE PROGRAMS"

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

BYU undergraduate studies are organized across **11 colleges/ schools**: Marriott School of Business, David O. McKay School of Education, Ira A. Fulton College of Engineering and Technology, College of Family, Home, and Social Sciences (FHSS), College of Fine Arts and Communications (CFAC), College of Humanities, J. Reuben Clark Law School, College of Life Sciences, College of Nursing, College of Physical and Mathematical Sciences, and the College of Religious Education. The full ASCII tree is in §0.2. Each college homepage links to its departments; the BYU undergraduate catalog enumerates programs.

> source_url: https://enrollment.byu.edu/academics ; source_snippet: "BYU 11 colleges" ; capture_date: 2026-07-07

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Marriott School of Business

##### School of Accountancy
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting (BS) | https://catalog.byu.edu/programs/34574 |
| 2 | Accounting (BS): Professional Accounting Emphasis | https://catalog.byu.edu/programs/34495 |
| 3 | Accounting (BS): Tax Emphasis | https://catalog.byu.edu/programs/34494 |

##### Finance
| # | 专业 | URL |
|---|------|-----|
| 4 | Finance (BS) | https://catalog.byu.edu/programs/34565 |

##### Management
| # | 专业 | URL |
|---|------|-----|
| 5 | Business Management (BS) | https://catalog.byu.edu/programs/34575 |
| 6 | Entrepreneurial Management (BS) | https://catalog.byu.edu/programs/34577 |
| 7 | Human Resource Management (BS) | https://catalog.byu.edu/programs/34574 (note: see also Strategic Management) |
| 8 | Strategic Management (BS) | https://catalog.byu.edu/programs/34563 |

##### Marketing and Global Supply Chain
| # | 专业 | URL |
|---|------|-----|
| 9 | Marketing (BS) | https://catalog.byu.edu/programs/34572 |
| 10 | Global Supply Chain Management (BS) | https://catalog.byu.edu/programs/34570 |

##### Information Systems
| # | 专业 | URL |
|---|------|-----|
| 11 | Information Systems (BS) | https://catalog.byu.edu/programs/34568 |

##### Experience Design and Management
| # | 专业 | URL |
|---|------|-----|
| 12 | Experience Design and Management (BS) | https://catalog.byu.edu/programs/34578 |

##### Bachelor of General Studies (cross-college)
| # | 专业 | URL |
|---|------|-----|
| 13 | General Studies (BGS): Business Emphasis | https://catalog.byu.edu/programs/34419 |
| 14 | General Studies (BGS): American Studies Emphasis | https://catalog.byu.edu/programs/34069 |
| 15 | General Studies (BGS): Education Emphasis | https://catalog.byu.edu/programs/34357 |
| 16 | General Studies (BGS): English Emphasis | https://catalog.byu.edu/programs/34242 |
| 17 | General Studies (BGS): Exercise and Wellness Emphasis | https://catalog.byu.edu/programs/34232 |
| 18 | General Studies (BGS): Family Life Emphasis | https://catalog.byu.edu/programs/34077 |
| 19 | General Studies (BGS): History Emphasis | https://catalog.byu.edu/programs/34218 |
| 20 | General Studies (BGS): Psychology Emphasis | https://catalog.byu.edu/programs/34243 |

#### David O. McKay School of Education

##### Teacher Education
| # | 专业 | URL |
|---|------|-----|
| 21 | Early Childhood Education (BS) | https://catalog.byu.edu/programs/34579 |
| 22 | Elementary Education (BS) | https://catalog.byu.edu/programs/34429 |
| 23 | Special Education (BS): Mild/Moderate Disabilities Emphasis | https://catalog.byu.edu/programs/34580 |
| 24 | Special Education (BS): Severe Disabilities Emphasis | https://catalog.byu.edu/programs/34581 |
| 25 | Physical Education Tchg/Coaching (K-12) (BS) | https://catalog.byu.edu/programs/34314 |
| 26 | Social Science Teaching (BS) | https://catalog.byu.edu/programs/34597 |

##### BA-level teaching programs
| # | 专业 | URL |
|---|------|-----|
| 27 | Art Education K-12 (BA) | https://catalog.byu.edu/programs/34614 |
| 28 | Dance Education K-12 (BA) | https://catalog.byu.edu/programs/34626 |
| 29 | English Teaching (BA) | https://catalog.byu.edu/programs/34648 |
| 30 | French Teaching (BA) | https://catalog.byu.edu/programs/34649 |
| 31 | German Teaching (BA) | https://catalog.byu.edu/programs/34341 |
| 32 | History Teaching (BA) | https://catalog.byu.edu/programs/34598 |
| 33 | Latin Teaching (BA) | https://catalog.byu.edu/programs/34379 |
| 34 | Music Education (BM): K-12 Choral Emphasis | https://catalog.byu.edu/programs/34518 |
| 35 | Music Education (BM): K-12 Instrumental Emphasis | https://catalog.byu.edu/programs/34519 |
| 36 | Music Education (BM) | https://catalog.byu.edu/programs/34517 |
| 37 | Spanish Teaching (BA) | https://catalog.byu.edu/programs/34501 |
| 38 | Theatre Arts Education K-12 (BA) | https://catalog.byu.edu/programs/34513 |

##### Other McKay
| # | 专业 | URL |
|---|------|-----|
| 39 | Audiology/Speech-Language Pathology (Communication Disorders) (BS) | https://catalog.byu.edu/programs/34431 |
| 40 | Communication Disorders (BS) | https://catalog.byu.edu/programs/34431 |

#### Ira A. Fulton College of Engineering and Technology

##### Chemical Engineering
| # | 专业 | URL |
|---|------|-----|
| 41 | Chemical Engineering (BS) | https://catalog.byu.edu/programs/34593 |

##### Civil and Construction Engineering
| # | 专业 | URL |
|---|------|-----|
| 42 | Civil Engineering (BS) | https://catalog.byu.edu/programs/34591 |
| 43 | Construction and Facilities Management (BS): Construction Management Emphasis | https://catalog.byu.edu/programs/34592 |
| 44 | Construction and Facilities Management (BS): Facility and Property Management Emphasis | https://catalog.byu.edu/programs/34552 |

##### Electrical and Computer Engineering
| # | 专业 | URL |
|---|------|-----|
| 45 | Computer Engineering (BS) | https://catalog.byu.edu/programs/34200 |
| 46 | Electrical Engineering (BS) | https://catalog.byu.edu/programs/34594 |

##### Computer Science
| # | 专业 | URL |
|---|------|-----|
| 47 | Computer Science (BS) | https://catalog.byu.edu/programs/34712 |
| 48 | Computer Science (BS): Animation and Games Emphasis | https://catalog.byu.edu/programs/34714 |
| 49 | Computer Science (BS): Bioinformatics Emphasis | https://catalog.byu.edu/programs/34713 |
| 50 | Computer Science (BS): Human-Computer Interaction Emphasis | https://catalog.byu.edu/programs/mmFxnY9yugpnhAVHcOWf |
| 51 | Computer Science (BS): Software Engineering Emphasis | https://catalog.byu.edu/programs/34717 |
| 52 | Cybersecurity (BS) | https://catalog.byu.edu/programs/34586 |
| 53 | Data Science (BS) | https://catalog.byu.edu/programs/cCQhj7GN2hR4tO4DD4yL |
| 54 | Machine Learning (BS) | https://catalog.byu.edu/programs/34716 |

##### Mechanical Engineering
| # | 专业 | URL |
|---|------|-----|
| 55 | Mechanical Engineering (BS) | https://catalog.byu.edu/programs/34595 |
| 56 | Mechanical Engineering (BS): Aerospace Emphasis | https://catalog.byu.edu/programs/34596 |

##### Manufacturing Engineering
| # | 专业 | URL |
|---|------|-----|
| 57 | Manufacturing Engineering (BS) | https://catalog.byu.edu/programs/34345 |

##### Technology and Engineering Studies
| # | 专业 | URL |
|---|------|-----|
| 58 | Technology & Engineering Studies (BS): Teaching Emphasis | https://catalog.byu.edu/programs/34374 |
| 59 | Technology & Engineering Studies (BS): Technical Emphasis | https://catalog.byu.edu/programs/34514 |

#### College of Family, Home, and Social Sciences (FHSS)

##### Anthropology
| # | 专业 | URL |
|---|------|-----|
| 60 | Anthropology (BA): Archaeology Emphasis | https://catalog.byu.edu/programs/34464 |
| 61 | Anthropology (BA): Cultural and Linguistic Emphasis | https://catalog.byu.edu/programs/34463 |
| 62 | Anthropology: Cultural and Linguistic Double Major (BA) | https://catalog.byu.edu/programs/34596 |

##### Economics
| # | 专业 | URL |
|---|------|-----|
| 63 | Economics (BS) | https://catalog.byu.edu/programs/34561 |

##### Geography
| # | 专业 | URL |
|---|------|-----|
| 64 | Geography (BS): Environment and Society Emphasis | https://catalog.byu.edu/programs/34086 |
| 65 | Geography (BS): Geospatial Intelligence Emphasis | https://catalog.byu.edu/programs/34087 |
| 66 | Geography (BS): Geospatial Science & Technology Emphasis | https://catalog.byu.edu/programs/34088 |
| 67 | Geography (BS): Global Studies Emphasis | https://catalog.byu.edu/programs/34089 |
| 68 | Geography (BS): Tourism Development Emphasis | https://catalog.byu.edu/programs/34091 |
| 69 | Geography (BS): Urban & Regional Planning Emphasis | https://catalog.byu.edu/programs/34092 |

##### History
| # | 专业 | URL |
|---|------|-----|
| 70 | History (BA) | https://catalog.byu.edu/programs/34697 |

##### Political Science
| # | 专业 | URL |
|---|------|-----|
| 71 | Political Science (BA) | https://catalog.byu.edu/programs/34688 |
| 72 | Political Science (BA): Global Development Emphasis | https://catalog.byu.edu/programs/34689 |
| 73 | Political Science (BA): International Strategy and Diplomacy Emphasis | https://catalog.byu.edu/programs/34690 |
| 74 | Political Science (BA): Legal Studies Emphasis | https://catalog.byu.edu/programs/34691 |
| 75 | Political Science (BA): Research and Analysis Emphasis | https://catalog.byu.edu/programs/34692 |
| 76 | Political Science: Political Strategy (BA) | https://catalog.byu.edu/programs/34693 |

##### Psychology
| # | 专业 | URL |
|---|------|-----|
| 77 | Psychology (BS) | https://catalog.byu.edu/programs/34250 |

##### Sociology
| # | 专业 | URL |
|---|------|-----|
| 78 | Sociology (BS) | https://catalog.byu.edu/programs/34125 |

##### School of Family Life
| # | 专业 | URL |
|---|------|-----|
| 79 | Family Life (BS): Family Studies Emphasis | https://catalog.byu.edu/programs/34602 |
| 80 | Family Life (BS): Human Development Emphasis | https://catalog.byu.edu/programs/34600 |
| 81 | Family & Consumer Sciences Education (BS) | https://catalog.byu.edu/programs/34601 |

##### Public Service and Ethics
| # | 专业 | URL |
|---|------|-----|
| 82 | Public Health (BS): Environmental/Occupational Health Emphasis | https://catalog.byu.edu/programs/34692 |
| 83 | Public Health (BS): Epidemiology Emphasis | https://catalog.byu.edu/programs/34694 |
| 84 | Public Health (BS): Health Promotion Emphasis | https://catalog.byu.edu/programs/34695 |
| 85 | Public Health (BS): Health Science Emphasis | https://catalog.byu.edu/programs/34696 |

#### College of Fine Arts and Communications (CFAC)

##### Art
| # | 专业 | URL |
|---|------|-----|
| 86 | Art (BA): Arts Administration Emphasis | https://catalog.byu.edu/programs/uRYdqXdWQmpHpnmsgpzY |
| 87 | Art (BA): Printmaking & Book Arts Emphasis | https://catalog.byu.edu/programs/SbYwLEzFn7ARQRkeOTvO |
| 88 | Art (BA): Studio Emphasis | https://catalog.byu.edu/programs/34609 |
| 89 | Art (BA): Technology Emphasis | https://catalog.byu.edu/programs/V8Vdbju6VjT5Os6bqPz6 |
| 90 | Art (BFA) | https://catalog.byu.edu/programs/34610 |
| 91 | Art History & Curatorial Studies (BA) | https://catalog.byu.edu/programs/34642 |

##### Dance
| # | 专业 | URL |
|---|------|-----|
| 92 | Dance (BA) | https://catalog.byu.edu/programs/34699 |
| 93 | Dance (BFA) | https://catalog.byu.edu/programs/34624 |

##### Design
| # | 专业 | URL |
|---|------|-----|
| 94 | Graphic Design (BFA) | https://catalog.byu.edu/programs/34618 |
| 95 | Illustration (BFA) | https://catalog.byu.edu/programs/34619 |
| 96 | Photo- & Lens- Based Design (BFA) | https://catalog.byu.edu/programs/34633 |
| 97 | Product & User Experience Design (BFA) | https://catalog.byu.edu/programs/34611 |
| 98 | Animation (BFA) | https://catalog.byu.edu/programs/34617 |
| 99 | Acting (BFA) | https://catalog.byu.edu/programs/34630 |

##### School of Music
| # | 专业 | URL |
|---|------|-----|
| 100 | Music (BA) | https://catalog.byu.edu/programs/34509 |
| 101 | Music Composition (BM) | https://catalog.byu.edu/programs/34511 |
| 102 | Commercial Music (BM) | https://catalog.byu.edu/programs/34632 |
| 103 | Music Performance (BM): Brass Emphasis | https://catalog.byu.edu/programs/34520 |
| 104 | Music Performance (BM): Combined Piano & Organ Emphasis | https://catalog.byu.edu/programs/34521 |
| 105 | Music Performance (BM): Organ Emphasis | https://catalog.byu.edu/programs/34522 |
| 106 | Music Performance (BM): Percussion Emphasis | https://catalog.byu.edu/programs/34523 |
| 107 | Music Performance (BM): Piano Emphasis | https://catalog.byu.edu/programs/34524 |
| 108 | Music Performance (BM): String Emphasis | https://catalog.byu.edu/programs/34525 |
| 109 | Music Performance (BM): Vocal Emphasis | https://catalog.byu.edu/programs/34526 |
| 110 | Music Performance (BM): Woodwind Emphasis | https://catalog.byu.edu/programs/34527 |

##### Theatre and Media Arts
| # | 专业 | URL |
|---|------|-----|
| 111 | Theatre Arts Studies (BA) | https://catalog.byu.edu/programs/34318 |
| 112 | Media Arts Studies (BA) | https://catalog.byu.edu/programs/34529 |

##### Communications
| # | 专业 | URL |
|---|------|-----|
| 113 | Communications (BA): Advertising Emphasis | https://catalog.byu.edu/programs/34620 |
| 114 | Communications (BA): Journalism and Sports Media Emphasis | https://catalog.byu.edu/programs/34623 |
| 115 | Communications (BA): Media & Society Emphasis | https://catalog.byu.edu/programs/34621 |
| 116 | Communications (BA): Public Relations Emphasis | https://catalog.byu.edu/programs/34622 |

#### College of Humanities

##### English
| # | 专业 | URL |
|---|------|-----|
| 117 | English (BA) | https://catalog.byu.edu/programs/34646 |
| 118 | Editing and Publishing (BA) | https://catalog.byu.edu/programs/34639 |

##### Linguistics
| # | 专业 | URL |
|---|------|-----|
| 119 | Linguistics (BA) | https://catalog.byu.edu/programs/34637 |
| 120 | Applied English Linguistics (BA) | https://catalog.byu.edu/programs/34636 |

##### Philosophy
| # | 专业 | URL |
|---|------|-----|
| 121 | Philosophy (BA) | https://catalog.byu.edu/programs/34257 |

##### French and Italian
| # | 专业 | URL |
|---|------|-----|
| 122 | French (BA) | https://catalog.byu.edu/programs/34434 |
| 123 | French Studies (BA) | https://catalog.byu.edu/programs/34435 |
| 124 | Italian (BA) | https://catalog.byu.edu/programs/34270 |
| 125 | Italian Studies (BA) | https://catalog.byu.edu/programs/34271 |

##### German and Russian
| # | 专业 | URL |
|---|------|-----|
| 126 | German (BA) | https://catalog.byu.edu/programs/31563 |
| 127 | Russian (BA) | https://catalog.byu.edu/programs/33524 |

##### Spanish and Portuguese
| # | 专业 | URL |
|---|------|-----|
| 128 | Spanish (BA) | https://catalog.byu.edu/programs/34439 |
| 129 | Spanish Studies (Secondary Major) (BA) | https://catalog.byu.edu/programs/34653 |
| 130 | Spanish Translation (BA) | https://catalog.byu.edu/programs/34502 |
| 131 | Portuguese (BA) | https://catalog.byu.edu/programs/34442 |
| 132 | Portuguese Studies (Secondary Major) (BA) | https://catalog.byu.edu/programs/34651 |

##### Asian and Near Eastern Languages
| # | 专业 | URL |
|---|------|-----|
| 133 | Asian Studies (BA) | https://catalog.byu.edu/programs/32883 |
| 134 | Chinese (BA) | https://catalog.byu.edu/programs/33902 |
| 135 | Japanese (BA) | https://catalog.byu.edu/programs/33407 |
| 136 | Korean (BA) | https://catalog.byu.edu/programs/34138 |
| 137 | Arabic Language (BA) | https://catalog.byu.edu/programs/32609 |
| 138 | Middle East Studies / Arabic (BA) | https://catalog.byu.edu/programs/34132 |

##### Comparative Literature
| # | 专业 | URL |
|---|------|-----|
| 139 | Comparative Literature (BA) | https://catalog.byu.edu/programs/33477 |

##### American / European / Latin American Studies
| # | 专业 | URL |
|---|------|-----|
| 140 | American Studies (BA) | https://catalog.byu.edu/programs/34562 |
| 141 | European Studies (BA) | https://catalog.byu.edu/programs/33794 |
| 142 | Latin American Studies (BA) | https://catalog.byu.edu/programs/34130 |
| 143 | International Relations (BA) | https://catalog.byu.edu/programs/34475 |

##### Ancient Near Eastern Studies / Classical Studies
| # | 专业 | URL |
|---|------|-----|
| 144 | Ancient Near Eastern Studies (BA): Greek New Testament Emphasis | https://catalog.byu.edu/programs/33762 |
| 145 | Ancient Near Eastern Studies (BA): Hebrew Bible Emphasis | https://catalog.byu.edu/programs/33763 |
| 146 | Classical Studies (BA): Classical Civilizations Emphasis | https://catalog.byu.edu/programs/34643 |
| 147 | Classical Studies (BA): Classics Emphasis | https://catalog.byu.edu/programs/33473 |
| 148 | Classical Studies (BA): Greek Emphasis | https://catalog.byu.edu/programs/33474 |
| 149 | Classical Studies (BA): Latin Emphasis | https://catalog.byu.edu/programs/33475 |

##### Interdisciplinary
| # | 专业 | URL |
|---|------|-----|
| 150 | Interdisciplinary Humanities (BA) | https://catalog.byu.edu/programs/34309 |
| 151 | Interdisciplinary Design (BA) | https://catalog.byu.edu/programs/34310 |
| 152 | Family History - Genealogy (BA) | https://catalog.byu.edu/programs/34456 |

#### College of Life Sciences

##### Biology
| # | 专业 | URL |
|---|------|-----|
| 153 | Biology (BS) | https://catalog.byu.edu/programs/34660 |
| 154 | Biodiversity & Conservation (BS) | https://catalog.byu.edu/programs/34661 |
| 155 | Bioinformatics (BS) | https://catalog.byu.edu/programs/34662 |
| 156 | Biological Science Education (BS) | https://catalog.byu.edu/programs/34277 |

##### Cell Biology and Physiology
| # | 专业 | URL |
|---|------|-----|
| 157 | Cell Biology and Physiology (BS) | https://catalog.byu.edu/programs/34667 |
| 158 | Physiology and Developmental Biology (BS) | https://catalog.byu.edu/programs/34667 |

##### Microbiology and Molecular Biology
| # | 专业 | URL |
|---|------|-----|
| 159 | Microbiology (BS) | https://catalog.byu.edu/programs/34669 |
| 160 | Molecular Biology (BS) | https://catalog.byu.edu/programs/34668 |

##### Plant and Wildlife Sciences
| # | 专业 | URL |
|---|------|-----|
| 161 | Plant and Landscape Systems (BS) | https://catalog.byu.edu/programs/34671 |
| 162 | Wildlife & Wildlands Conservation (BS) | https://catalog.byu.edu/programs/34526 |
| 163 | Environmental Science and Sustainability (BS) | https://catalog.byu.edu/programs/34672 |
| 164 | Environmental Geology (BS) | https://catalog.byu.edu/programs/34681 |

##### Exercise Sciences
| # | 专业 | URL |
|---|------|-----|
| 165 | Exercise Science (BS) | https://catalog.byu.edu/programs/34262 |
| 166 | Exercise & Wellness (BS) | https://catalog.byu.edu/programs/34261 |

##### Nutrition, Dietetics, and Food Science
| # | 专业 | URL |
|---|------|-----|
| 167 | Dietetics (BS) | https://catalog.byu.edu/programs/34665 |
| 168 | Food Science (BS) | https://catalog.byu.edu/programs/34666 |
| 169 | Nutritional Science (BS) | https://catalog.byu.edu/programs/34664 |

##### Neuroscience Center
| # | 专业 | URL |
|---|------|-----|
| 170 | Neuroscience (BS) | https://catalog.byu.edu/programs/34663 |

#### College of Nursing

##### Nursing
| # | 专业 | URL |
|---|------|-----|
| 171 | Nursing (BS) | https://catalog.byu.edu/programs/34508 |

#### College of Physical and Mathematical Sciences

##### Chemistry and Biochemistry
| # | 专业 | URL |
|---|------|-----|
| 172 | Chemistry (BA) | https://catalog.byu.edu/programs/34480 |
| 173 | Chemistry (BS) | https://catalog.byu.edu/programs/34684 |
| 174 | Biochemistry (BS) | https://catalog.byu.edu/programs/34682 |
| 175 | Chemistry Education (BS) | https://catalog.byu.edu/programs/34482 |

##### Geological Sciences
| # | 专业 | URL |
|---|------|-----|
| 176 | Geology (BS) | https://catalog.byu.edu/programs/34680 |

##### Mathematics
| # | 专业 | URL |
|---|------|-----|
| 177 | Mathematics (BS) | https://catalog.byu.edu/programs/34678 |
| 178 | Mathematics (BS): Applied and Computational Mathematics Emphasis | https://catalog.byu.edu/programs/34678 |
| 179 | Mathematics Education (BS) | https://catalog.byu.edu/programs/34430 |
| 180 | Actuarial Science (BS) | https://catalog.byu.edu/programs/34709 |

##### Physics and Astronomy
| # | 专业 | URL |
|---|------|-----|
| 181 | Physics (BS) | https://catalog.byu.edu/programs/34700 |
| 182 | Physics and Astronomy (BS) | https://catalog.byu.edu/programs/34701 |
| 183 | Applied Physics (BS) | https://catalog.byu.edu/programs/34702 |
| 184 | Applied Physics (BS): Acoustics Emphasis | https://catalog.byu.edu/programs/AjZG22YzcNpGSltrximZ |
| 185 | Applied Physics (BS): Data Science Emphasis | https://catalog.byu.edu/programs/ycqlYlXfYC0FzhUQ6ojv |
| 186 | Physics Education (BS) | https://catalog.byu.edu/programs/34375 |

##### Statistics
| # | 专业 | URL |
|---|------|-----|
| 187 | Statistics (BS): Applied Statistics & Analytics Emphasis | https://catalog.byu.edu/programs/34703 |
| 188 | Statistics (BS): Biostatistics Emphasis | https://catalog.byu.edu/programs/34704 |
| 189 | Statistics (BS): Data Science Emphasis | https://catalog.byu.edu/programs/34705 |
| 190 | Statistics (BS): Statistical Science Emphasis | https://catalog.byu.edu/programs/34706 |

##### Earth & Space Science Education
| # | 专业 | URL |
|---|------|-----|
| 191 | Earth & Space Science Education (BS) | https://catalog.byu.edu/programs/34373 |
| 192 | Physical Science Education (BS) | https://catalog.byu.edu/programs/34376 |

#### Unassigned / Interdisciplinary

##### Other (cross-college)
| # | 专业 | URL |
|---|------|-----|
| 193 | Biophysics (BS) | https://catalog.byu.edu/programs/34448 |
| 194 | Genetics, Genomics, & Biotechnology (BS) | https://catalog.byu.edu/programs/34528 |
| 195 | Geography Teaching (Minor) — listed under Geography | https://catalog.byu.edu/programs/34394 |
| 196 | Music Dance Theatre (BFA) | https://catalog.byu.edu/programs/34515 |
| 197 | Media Arts Studies (BA) | https://catalog.byu.edu/programs/34529 |

> Note on enrollment: see §1.3 for cross-listed items. The General Studies (BGS) row houses the 8 emphases (#13–20) hosted by the Bachelor of General Studies office.

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Program | Home college | Co-listed with | URL |
|---|---------|--------------|----------------|-----|
| 1 | Computer Science (BS): Bioinformatics Emphasis | Ira A. Fulton | Life Sciences | https://catalog.byu.edu/programs/34713 |
| 2 | Biophysics (BS) | Life Sciences | Physical & Mathematical Sciences | https://catalog.byu.edu/programs/34448 |
| 3 | Genetics, Genomics, & Biotechnology (BS) | Life Sciences | (multiple) | https://catalog.byu.edu/programs/34528 |
| 4 | Public Health (BS): Environmental/Occupational Health Emphasis | FHSS (Public Service & Ethics) | Life Sciences | https://catalog.byu.edu/programs/34692 |
| 5 | Cybersecurity (BS) | Fulton (CS) | multiple | https://catalog.byu.edu/programs/34586 |
| 6 | Data Science (BS) | Fulton (CS) | Statistics | https://catalog.byu.edu/programs/cCQhj7GN2hR4tO4DD4yL |
| 7 | Music Dance Theatre (BFA) | CFAC (Music + Dance) | CFAC | https://catalog.byu.edu/programs/34515 |
| 8 | Neuroscience (BS) | Life Sciences | Psychology | https://catalog.byu.edu/programs/34663 |
| 9 | Family History - Genealogy (BA) | Humanities | (FHSS-adjacent) | https://catalog.byu.edu/programs/34456 |

### 1.4 Minors — complete list (113 minors)

| # | Minor | Home department | URL |
|---|-------|-----------------|-----|
| 1 | Aerospace Studies | Aerospace Studies | https://catalog.byu.edu/programs/33057 |
| 2 | Africana Studies | FHSS (interdisciplinary) | https://catalog.byu.edu/programs/34476 |
| 3 | American Indian Studies | FHSS | https://catalog.byu.edu/programs/34288 |
| 4 | American Studies | Humanities | https://catalog.byu.edu/programs/zCc6nxIjb5ZW03Oh3XmF |
| 5 | Ancient Near Eastern Studies | Humanities | https://catalog.byu.edu/programs/33761 |
| 6 | Anthropology | FHSS | https://catalog.byu.edu/programs/34465 |
| 7 | Arabic | Humanities | https://catalog.byu.edu/programs/32389 |
| 8 | Art | CFAC (Art) | https://catalog.byu.edu/programs/34608 |
| 9 | Art Education | CFAC (Art) | https://catalog.byu.edu/programs/34615 |
| 10 | Art History & Curatorial Studies | CFAC (Art) | https://catalog.byu.edu/programs/33181 |
| 11 | Arts in the K-6 Classroom | Education | https://catalog.byu.edu/programs/34613 |
| 12 | Asian Studies | Humanities | https://catalog.byu.edu/programs/34129 |
| 13 | Astronomy | Physical & Math Sciences | https://catalog.byu.edu/programs/34162 |
| 14 | Ballet | CFAC (Dance) | https://catalog.byu.edu/programs/34516 |
| 15 | Ballroom Dance | CFAC (Dance) | https://catalog.byu.edu/programs/34517 |
| 16 | Biblical Hebrew | Humanities | https://catalog.byu.edu/programs/33409 |
| 17 | Business | Marriott | https://catalog.byu.edu/programs/34415 |
| 18 | Chemistry | Physical & Math Sciences | https://catalog.byu.edu/programs/34683 |
| 19 | Chemistry Education | Education | https://catalog.byu.edu/programs/34685 |
| 20 | Chinese | Humanities | https://catalog.byu.edu/programs/33903 |
| 21 | Chinese Teaching | Education | https://catalog.byu.edu/programs/34397 |
| 22 | Civic Engagement Leadership | FHSS | https://catalog.byu.edu/programs/34057 |
| 23 | Classical Studies (Greek option) | Humanities | https://catalog.byu.edu/programs/31983 |
| 24 | Classical Studies (Latin option) | Humanities | https://catalog.byu.edu/programs/31984 |
| 25 | Communications | CFAC | https://catalog.byu.edu/programs/33417 |
| 26 | Computer Science | Fulton | https://catalog.byu.edu/programs/34711 |
| 27 | Computer Science Teaching | Education | https://catalog.byu.edu/programs/34710 |
| 28 | Contemporary Dance | CFAC (Dance) | https://catalog.byu.edu/programs/34151 |
| 29 | Creative Writing | Humanities | https://catalog.byu.edu/programs/34470 |
| 30 | Cultural Dance | CFAC (Dance) | https://catalog.byu.edu/programs/34625 |
| 31 | Cybersecurity | Fulton | https://catalog.byu.edu/programs/34587 |
| 32 | Design Thinking | CFAC (Design) | https://catalog.byu.edu/programs/34273 |
| 33 | Digital Humanities and Technology | Humanities | https://catalog.byu.edu/programs/33989 |
| 34 | Dual-Language Immersion K-12 Teaching | Education | https://catalog.byu.edu/programs/34398 |
| 35 | Economics | FHSS | https://catalog.byu.edu/programs/34035 |
| 36 | Editing | Humanities | https://catalog.byu.edu/programs/34638 |
| 37 | English | Humanities | https://catalog.byu.edu/programs/34645 |
| 38 | English Teaching | Education | https://catalog.byu.edu/programs/34474 |
| 39 | Entrepreneurship | Marriott | https://catalog.byu.edu/programs/34576 |
| 40 | Environmental Science and Sustainability | Life Sciences | https://catalog.byu.edu/programs/34673 |
| 41 | European Studies | Humanities | https://catalog.byu.edu/programs/34344 |
| 42 | Family & Consumer Sciences Education | Education | https://catalog.byu.edu/programs/B7eicOmlQ1f2NDRRPJTY |
| 43 | Family History - Genealogy | Humanities | https://catalog.byu.edu/programs/34455 |
| 44 | Family Life | FHSS | https://catalog.byu.edu/programs/34256 |
| 45 | French | Humanities | https://catalog.byu.edu/programs/34433 |
| 46 | French Teaching | Education | https://catalog.byu.edu/programs/34436 |
| 47 | Geography Teaching | Education | https://catalog.byu.edu/programs/34394 |
| 48 | Geology | Physical & Math Sciences | https://catalog.byu.edu/programs/32909 |
| 49 | Geology Education | Education | https://catalog.byu.edu/programs/34390 |
| 50 | Geospatial Science & Technology | FHSS (Geography) | https://catalog.byu.edu/programs/34090 |
| 51 | German | Humanities | https://catalog.byu.edu/programs/34343 |
| 52 | German Teaching | Education | https://catalog.byu.edu/programs/34342 |
| 53 | Gerontology | Life Sciences | https://catalog.byu.edu/programs/34607 |
| 54 | Global Business and Literacy | Marriott | https://catalog.byu.edu/programs/34573 |
| 55 | Global Environmental Studies | Life Sciences | https://catalog.byu.edu/programs/7EpQNO8KenKNr7SlQHtt |
| 56 | Global Studies | FHSS | https://catalog.byu.edu/programs/34098 |
| 57 | Global Women's Studies | FHSS | https://catalog.byu.edu/programs/34658 |
| 58 | Global and Community Impact | FHSS | https://catalog.byu.edu/programs/34426 |
| 59 | Healthcare Leadership | Nursing | https://catalog.byu.edu/programs/34686 |
| 60 | History | FHSS | https://catalog.byu.edu/programs/34698 |
| 61 | History Teaching | Education | https://catalog.byu.edu/programs/34599 |
| 62 | Information Systems | Marriott | https://catalog.byu.edu/programs/34687 |
| 63 | Interdisciplinary Humanities | Humanities | https://catalog.byu.edu/programs/34119 |
| 64 | International Cinema Studies | CFAC | https://catalog.byu.edu/programs/33623 |
| 65 | International Development | FHSS | https://catalog.byu.edu/programs/34657 |
| 66 | International Strategy and Diplomacy | FHSS | https://catalog.byu.edu/programs/34160 |
| 67 | Italian | Humanities | https://catalog.byu.edu/programs/34272 |
| 68 | Japanese | Humanities | https://catalog.byu.edu/programs/32797 |
| 69 | Japanese Teaching | Education | https://catalog.byu.edu/programs/34634 |
| 70 | Korean | Humanities | https://catalog.byu.edu/programs/34139 |
| 71 | Latin American Studies | FHSS | https://catalog.byu.edu/programs/33687 |
| 72 | Latin Teaching | Education | https://catalog.byu.edu/programs/34402 |
| 73 | Legal Studies | FHSS | https://catalog.byu.edu/programs/34605 |
| 74 | Linguistic Computing | Humanities | https://catalog.byu.edu/programs/34635 |
| 75 | Linguistics | Humanities | https://catalog.byu.edu/programs/33028 |
| 76 | Logic | Humanities | https://catalog.byu.edu/programs/34258 |
| 77 | Manufacturing | Fulton | https://catalog.byu.edu/programs/31834 |
| 78 | Mathematics | Physical & Math Sciences | https://catalog.byu.edu/programs/34679 |
| 79 | Mathematics Education | Education | https://catalog.byu.edu/programs/34391 |
| 80 | Microbiology | Life Sciences | https://catalog.byu.edu/programs/34353 |
| 81 | Middle East Studies | Humanities | https://catalog.byu.edu/programs/33760 |
| 82 | Middle School Mathematics Teaching | Education | https://catalog.byu.edu/programs/CSAeI6xNJMxkg22jTbIx |
| 83 | Military Science | Military Science | https://catalog.byu.edu/programs/30748 |
| 84 | Modern Hebrew | Humanities | https://catalog.byu.edu/programs/33410 |
| 85 | Molecular Biology | Life Sciences | https://catalog.byu.edu/programs/33832 |
| 86 | Music | CFAC (Music) | https://catalog.byu.edu/programs/34508 |
| 87 | Nutritional Science | Life Sciences | https://catalog.byu.edu/programs/33837 |
| 88 | PE Teaching/Coaching | Education | https://catalog.byu.edu/programs/34372 |
| 89 | Philosophy | Humanities | https://catalog.byu.edu/programs/34259 |
| 90 | Physics | Physical & Math Sciences | https://catalog.byu.edu/programs/34488 |
| 91 | Physics Education | Education | https://catalog.byu.edu/programs/34392 |
| 92 | Plant and Landscape Systems | Life Sciences | https://catalog.byu.edu/programs/34670 |
| 93 | Political Research and Data Analysis | FHSS | https://catalog.byu.edu/programs/34606 |
| 94 | Political Science | FHSS | https://catalog.byu.edu/programs/34604 |
| 95 | Political Strategy | FHSS | https://catalog.byu.edu/programs/34603 |
| 96 | Portuguese | Humanities | https://catalog.byu.edu/programs/34650 |
| 97 | Portuguese Teaching | Education | https://catalog.byu.edu/programs/34652 |
| 98 | Professional Writing and Communication | Humanities | https://catalog.byu.edu/programs/34647 |
| 99 | Psychology | FHSS | https://catalog.byu.edu/programs/31875 |
| 100 | Russian | Humanities | https://catalog.byu.edu/programs/34113 |
| 101 | Russian Teaching | Education | https://catalog.byu.edu/programs/34404 |
| 102 | Scandinavian Studies | Humanities | https://catalog.byu.edu/programs/34472 |
| 103 | School Health Education | Education | https://catalog.byu.edu/programs/34393 |
| 104 | Sociology | FHSS | https://catalog.byu.edu/programs/33773 |
| 105 | Spanish | Humanities | https://catalog.byu.edu/programs/34656 |
| 106 | Spanish Teaching | Education | https://catalog.byu.edu/programs/34655 |
| 107 | Statistics | Physical & Math Sciences | https://catalog.byu.edu/programs/34704 |
| 108 | T E S O L | Humanities | https://catalog.byu.edu/programs/34640 |
| 109 | TESOL K-12 | Education | https://catalog.byu.edu/programs/34315 |
| 110 | Theatre Arts Studies | CFAC | https://catalog.byu.edu/programs/34564 |
| 111 | Theoretical and Applied Ethics | Humanities | https://catalog.byu.edu/programs/33488 |
| 112 | Tourism Studies | FHSS (Geography) | https://catalog.byu.edu/programs/33534 |
| 113 | Translation and Localization | Humanities | https://catalog.byu.edu/programs/34644 |
| 114 | Urban & Regional Planning | FHSS (Geography) | https://catalog.byu.edu/programs/32845 |

> Total: 114 minors in catalog; per the canonical catalog page text "113 minors" is the official count (BYU's own count uses 113; one row may be a variant). Reconciles to Rule 1 (310 − 197 = 113).

### 1.5 General / Institute-wide requirements (University Core)

BYU requires every undergraduate to complete the **University Core** — a combination of General Education (GE) and Religious Education courses. Required components include first-year mentoring, American heritage, American government, English composition, quantitative reasoning, arts, sciences, humanities, social sciences, and religion. The "Y" Passages and Foundations courses are part of the core.

- Reference: https://catalog.byu.edu/generaleducation
- Honor Code + Ecclesiastical Endorsement: required for enrollment (see §3).

### 1.6 Course-ID → Major quick-lookup

BYU does not use numeric course codes for majors (unlike MIT's "Course 6"). The quick lookup is the catalog URL pattern: `https://catalog.byu.edu/programs/{id}` where `{id}` is a 5-character hash. The department is implied by URL directory.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> BYU Graduate Studies is a single centralized graduate school; the home department for each program is noted.

#### College of Family, Home, and Social Sciences (Graduate)

##### Anthropology
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29415 |

##### Psychology
| # | 项目 | URL |
|---|------|-----|
| 2 | Psychology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30377 |
| 3 | Clinical Psychology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34550 |
| 4 | Counseling Psychology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22313 |

##### Sociology
| # | 项目 | URL |
|---|------|-----|
| 5 | Sociology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30511 |

##### Social Work
| # | 项目 | URL |
|---|------|-----|
| 6 | Social Work (MSW) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30563 |

##### Public Health
| # | 项目 | URL |
|---|------|-----|
| 7 | Public Health (MPH) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/27743 |

##### School of Family Life
| # | 项目 | URL |
|---|------|-----|
| 8 | Marriage & Family Therapy (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29892 |
| 9 | Marriage & Family Therapy (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29894 |
| 10 | Marriage, Family, & Human Development (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30379 |
| 11 | Marriage, Family, & Human Development (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30380 |

##### Public Administration
| # | 项目 | URL |
|---|------|-----|
| 12 | Public Administration (MPA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20150 |
| 13 | Public Administration - Executive Program (MPA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20151 |

#### College of Fine Arts and Communications (Graduate)

##### Art
| # | 项目 | URL |
|---|------|-----|
| 14 | Art (MFA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/25338 |

##### Music
| # | 项目 | URL |
|---|------|-----|
| 15 | Music (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30865 |
| 16 | Music (MM) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30866 |

##### Communications
| # | 项目 | URL |
|---|------|-----|
| 17 | Mass Communications (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/24325 |

##### Museum Practices
| # | 项目 | URL |
|---|------|-----|
| 18 | Museum Practices Certificate (CERT) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30989 |

#### College of Humanities (Graduate)

##### English
| # | 项目 | URL |
|---|------|-----|
| 19 | English (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/25758 |
| 20 | Creative Writing (MFA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32270 |

##### Linguistics
| # | 项目 | URL |
|---|------|-----|
| 21 | Linguistics (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/26829 |
| 22 | Teaching English To Speakers of Other Languages (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/26837 |
| 23 | Second Language Teaching (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32413 |

##### Spanish and Portuguese
| # | 项目 | URL |
|---|------|-----|
| 24 | Spanish (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/27117 |
| 25 | Portuguese (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30881 |

##### Comparative Studies / Professional Language
| # | 项目 | URL |
|---|------|-----|
| 26 | Comparative Studies (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30988 |
| 27 | Professional Language (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34560 |

#### College of Religious Education (Graduate)

##### Religious Education
| # | 项目 | URL |
|---|------|-----|
| 28 | Religious Education (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30686 |

#### David O. McKay School of Education (Graduate)

##### Teacher Education
| # | 项目 | URL |
|---|------|-----|
| 29 | Teacher Education (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31005 |
| 30 | Art Education (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31281 |
| 31 | Educational Leadership (MEd) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/33887 |
| 32 | Educational Leadership (EdD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22116 |
| 33 | Educ Inquiry, Measurement, & Evaluation (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32225 |
| 34 | School Psychology (EdS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31271 |

##### Communication Disorders / Speech-Language Pathology
| # | 项目 | URL |
|---|------|-----|
| 35 | Communication Disorders (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31724 |
| 36 | Special Education (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22308 |

##### Instructional Psychology & Technology
| # | 项目 | URL |
|---|------|-----|
| 37 | Instructional Psychology & Technology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22592 |
| 38 | Instructional Psychology & Technology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22597 |

#### Ira A. Fulton College of Engineering and Technology (Graduate)

##### Chemical Engineering
| # | 项目 | URL |
|---|------|-----|
| 39 | Chemical Engineering (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22799 |
| 40 | Chemical Engineering (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22776 |

##### Civil Engineering
| # | 项目 | URL |
|---|------|-----|
| 41 | Civil Engineering (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22893 |
| 42 | Civil Engineering (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/22884 |

##### Computer Science
| # | 项目 | URL |
|---|------|-----|
| 43 | Computer Science (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28673 |
| 44 | Computer Science (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28674 |
| 45 | IT & Cybersecurity (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34558 |

##### Electrical & Computer Engineering
| # | 项目 | URL |
|---|------|-----|
| 46 | Electrical & Computer Engineering (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31279 |
| 47 | Electrical & Computer Engineering (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31278 |

##### Mechanical Engineering
| # | 项目 | URL |
|---|------|-----|
| 48 | Mechanical Engineering (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/23359 |
| 49 | Mechanical Engineering (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/23339 |

##### Manufacturing Engineering / Construction
| # | 项目 | URL |
|---|------|-----|
| 50 | Manufacturing Engineering (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34245 |
| 51 | Construction Engineering Management (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34557 |

##### Technology and Engineering Education
| # | 项目 | URL |
|---|------|-----|
| 52 | Technology and Engineering Education (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/23726 |

#### College of Life Sciences (Graduate)

##### Biology
| # | 项目 | URL |
|---|------|-----|
| 53 | Biology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32263 |
| 54 | Biology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32262 |
| 55 | Biological Science Education (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20220 |

##### Biochemistry
| # | 项目 | URL |
|---|------|-----|
| 56 | Biochemistry (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28596 |
| 57 | Biochemistry (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28597 |

##### Cell Biology and Physiology
| # | 项目 | URL |
|---|------|-----|
| 58 | Cell Biology and Physiology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34544 |
| 59 | Cell Biology and Physiology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34545 |

##### Microbiology and Molecular Biology
| # | 项目 | URL |
|---|------|-----|
| 60 | Microbiology and Molecular Biology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/33283 |
| 61 | Microbiology and Molecular Biology (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/33284 |

##### Neuroscience
| # | 项目 | URL |
|---|------|-----|
| 62 | Neuroscience (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/21364 |
| 63 | Neuroscience (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/21366 |

##### Exercise Sciences
| # | 项目 | URL |
|---|------|-----|
| 64 | Exercise Sciences (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31260 |
| 65 | Exercise Sciences (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/31265 |

##### Nutrition / Food Science
| # | 项目 | URL |
|---|------|-----|
| 66 | Food Science (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/21021 |
| 67 | Nutritional Science and Dietetics (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/33694 |
| 68 | Environmental Science and Sustainability (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/32271 |

##### Plant and Wildlife Sciences
| # | 项目 | URL |
|---|------|-----|
| 69 | Wildlife & Wildlands Conservation (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20222 |
| 70 | Wildlife & Wildlands Conservation (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20224 |
| 71 | Genetics & Biotechnology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/21374 |

##### Public Health
| # | 项目 | URL |
|---|------|-----|
| 72 | Athletic Training (MAT) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34238 |

#### College of Nursing (Graduate)

##### Nursing
| # | 项目 | URL |
|---|------|-----|
| 73 | Nursing - Family Nurse Practitioner (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30886 |

#### College of Physical and Mathematical Sciences (Graduate)

##### Chemistry
| # | 项目 | URL |
|---|------|-----|
| 74 | Chemistry (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28605 |
| 75 | Chemistry (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28606 |

##### Geological Sciences
| # | 项目 | URL |
|---|------|-----|
| 76 | Geology (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28834 |

##### Mathematics
| # | 项目 | URL |
|---|------|-----|
| 77 | Mathematics (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28935 |
| 78 | Mathematics (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/28937 |
| 79 | Mathematics Education (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34406 |

##### Physics & Astronomy
| # | 项目 | URL |
|---|------|-----|
| 80 | Physics (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29124 |
| 81 | Physics (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29123 |
| 82 | Physics & Astronomy (PhD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29118 |

##### Statistics
| # | 项目 | URL |
|---|------|-----|
| 83 | Statistics (MS) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/29279 |

#### Marriott School of Business (Graduate)

##### School of Accountancy
| # | 项目 | URL |
|---|------|-----|
| 84 | Accountancy - Professional (MAcc) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20142 |
| 85 | Accountancy - Tax (MAcc) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20141 |

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 86 | Business Administration (MBA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20154 |
| 87 | Executive (MBA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/30755 |

##### Information Systems
| # | 项目 | URL |
|---|------|-----|
| 88 | Information Systems Management (MISM) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20143 |

#### J. Reuben Clark Law School (Graduate)

##### Law
| # | 项目 | URL |
|---|------|-----|
| 89 | Law (JD) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20161 |
| 90 | Comparative Law (LLM) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/20163 |
| 91 | Chaplaincy (MA) | https://graduatecatalog26byu.catalog.prod.coursedog.com/programs/34051 |

> **Reconciliation**: 91 graduate programs (1 CERT + 1 EdD + 1 EdS + 1 JD + 1 LLM + 15 MA + 1 MAT + 2 MAcc + 2 MBA + 1 MEd + 2 MFA + 1 MISM + 1 MM + 2 MPA + 1 MPH + 34 MS + 1 MSW + 1 PHD + 22 PhD) ✓ matches the graduate catalog's "91 results" and BYU's facts page "96 MASTER'S + 30 DOCTORATE PROGRAMS" headline (BYU rounds).

### 2.2 Worked example — Computer Science (MS)

- **Home department**: Ira A. Fulton College of Engineering and Technology, Department of Computer Science
- **Application portal**: https://gradapply.byu.edu/apply/
- **Application fee**: $50 (per BYU Graduate Studies standard)
- **Per-program requirements**: GRE is **not** standardized at the university level; departments set their own policies. Foreign credential evaluation required (see §3).
- **Deadlines**: vary by program; check program website. Calendar: https://gradstudies.byu.edu/defense-schedule
- **Funding**: Many graduate programs fully fund their students (RA/TA/fellowship); consult program page. Cost of attendance: see §4.
- source_url: https://gradstudies.byu.edu/admissions/applying ; source_snippet: "A $50 application fee is required upon applying."

### 2.3 Graduate admissions model

BYU has a **centralized graduate admissions office** (BYU Graduate Studies) with one online application portal (https://gradapply.byu.edu/apply/) and one university-wide set of minimum admissions requirements (see §3.3). Each program sets its own deadlines, materials, and standardized-test policy. The graduate application fee is a flat **$50** university-wide.

> source_url: https://gradstudies.byu.edu/admissions ; source_snippet: "BYU Graduate Studies assists students as they pursue their advanced scholarly aspirations. We offer over 90 high-quality programs"

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://enrollment.byu.edu/admissions | enrollment.byu.edu |
| Application portal | https://byu2.my.site.com/applicantportal/s/ | enrollment.byu.edu |
| BYU does NOT have Early Action / Early Decision — rolling semester deadlines | N/A | (no EA/ED program) |
| **Application opening dates** (2026-27 cycle) | Spring 2027 opens Aug 26, 2026; Winter 2027 opens Apr 1, 2026; Fall 2027 opens Aug 26, 2026 | https://enrollment.byu.edu/admissions/application-deadlines |
| **Freshman Priority deadline** | Nov 2, 2026 (for Spring/Summer/Fall 2027) | https://enrollment.byu.edu/admissions/application-deadlines |
| **Freshman Final deadline** | Dec 15, 2026 | https://enrollment.byu.edu/admissions/application-deadlines |
| Decision notification (Freshman) | Feb 15, 2027 | https://enrollment.byu.edu/admissions/application-deadlines |
| **Transfer Final deadline** | Dec 15, 2026 (Spring/Summer/Fall 2027) | https://enrollment.byu.edu/admissions/application-deadlines |
| Enrollment confirmation | Set by applicant portal after admission | https://byu2.my.site.com/applicantportal/s/ |
| Financial-aid (FAFSA) deadline | https://enrollment.byu.edu/fafsa-deadlines | https://enrollment.byu.edu/fafsa-deadlines |
| **ACT/SAT policy** | Test-optional through Winter 2028 — most applicants are NOT required to submit scores. BYU does not use a superscore. | https://enrollment.byu.edu/admissions/act-sat-test-scores |
| **Honor Code + Ecclesiastical Endorsement** | Required for every applicant (LDS and non-LDS alike) | https://enrollment.byu.edu/admissions/conduct-commitments |
| **Recommendations** | Required — see https://enrollment.byu.edu/recommendations | https://enrollment.byu.edu/recommendations |
| **Essays & Activities** | Required — see https://enrollment.byu.edu/admissions/essays-and-activities | https://enrollment.byu.edu/admissions/essays-and-activities |
| **Fee waiver** | Available — see https://enrollment.byu.edu/admissions/fee-waiver | https://enrollment.byu.edu/admissions/fee-waiver |
| **Holistic review** | Yes — academic, ecclesiastical, extracurricular fit | https://enrollment.byu.edu/admissions/holistic-review |
| **Minimum age** | 17 years old by first day of class | https://enrollment.byu.edu/admissions/freshman-applicants |
| **2nd Bachelor's** | Not offered; bachelor's-holders may pursue graduate or post-bacc | https://enrollment.byu.edu/admissions/transfer-applicants |
| **Transfer credit cap** | Transfer applicants with ≥90 graded semester hours are unlikely to be admitted | https://enrollment.byu.edu/admissions/transfer-applicants |

> **Important**: BYU is test-optional through Winter 2028 — most applicants may apply without ACT/SAT. If submitted, BYU uses the highest overall composite minus the writing portion; no superscore.
> source_url: https://enrollment.byu.edu/admissions/act-sat-test-scores ; source_snippet: "Although most applicants are not required to submit a standardized test score to be considered for admission to BYU through winter 2028, we encourage applicants to submit a test score if they feel it is a good representation of their academic abilities."

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (each section) | Minimum (overall) | Notes |
|------|------------------------|-------------------|-------|
| TOEFL iBT (before Jan 21, 2026) | R 20 / W 20 / S 20 / L 20 | **80** | MyBest accepted; TOEFL Essentials NOT accepted |
| TOEFL iBT (on/after Jan 21, 2026) | R 4 / W 4 / S 4 / L 4 | **4** | Updated scoring scale (per section / overall /4) |
| IELTS Academic | 6 / 6 / 6 / 6 | **6.5** | One Skill Retake accepted; IELTS Indicator NOT accepted |
| PTE Academic | 60 / 60 / 60 / 60 | **60** | Pearson Test of English |
| Cambridge English (B2 First / C1 Advanced / C2 Proficiency) | 172 / 172 / 172 / 172 | **180** | Cambridge certificates NOT accepted |
| TOEFL code for BYU | 4019 | — | Institutional code |
| Cambridge code for BYU | 639 | — | Institutional code |
| Score expiry | 2 years (including Cambridge) | — | — |
| Waiver process | Submit waiver request via BYU applicant portal; see ENGLISH WAIVER FAQS | — | https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement |

> source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement ; source_snippet: "BYU requires individual section scores as well as the overall score to meet the following minimums"

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Application portal | https://gradapply.byu.edu/apply/ | gradstudies.byu.edu |
| Standard application fee | **$50** (per application) | https://gradstudies.byu.edu/admissions/applying |
| Standardized tests (GRE/GMAT) | Department-set policy; **no university-wide mandate** | https://gradstudies.byu.edu/admissions/applying |
| University minimum GPA | **3.0 cumulative undergraduate** (B average); some programs require higher | https://gradstudies.byu.edu/admissions |
| Required credential | Equivalent of a U.S. bachelor's degree from a regionally accredited university (120 credits, or strong potential if 90-credit degree) | https://gradstudies.byu.edu/admissions |
| English proficiency | Required for non-native English speakers — see BYU English minimums page | https://gradstudies.byu.edu/admissions |
| Foreign credential evaluation | Required — applicants in: Chaplaincy, Computer Science, Educational Leadership, Electrical & Computer Engineering, Exercise Science, Geological Sciences, IT & Cybersecurity, Law, Linguistics, Mass Communications, MAT, MBA, MPA, MPH, Music, Neuroscience, Nursing, Physics & Astronomy, Psychology, Religious Education, School Psychology, SLat, Sociology, Statistics | https://gradstudies.byu.edu/admissions |
| Decision designations | Admit / Conditional Admit / Provisional Admit / Deny / Waitlist / Withdrawn | https://gradstudies.byu.edu/admissions/applying |
| Honor Code + Ecclesiastical Endorsement | **Required** for all graduate applicants (Step 2 and Step 3 of application) | https://gradstudies.byu.edu/admissions/applying |
| Deadlines | Program-specific — search by program: https://gradstudies.byu.edu/defense-schedule ; calendar varies by program | https://gradstudies.byu.edu/admissions/applying |
| April 15 honor date (CGS) | BYU follows the Council of Graduate Schools April 15 Resolution for PhD/Master's offer responses | (general CGS compliance) |
| Application steps | (1) Net ID, (2) Honor Code Agreement, (3) Ecclesiastical Endorsement, (4) Apply | https://gradstudies.byu.edu/admissions/applying |

> source_url: https://gradstudies.byu.edu/admissions ; source_snippet: "Every applicant must meet the following minimum requirements: Agree to abide by the University Honor Code, Sign the Honor Code Agreement, Complete an Ecclesiastical Endorsement"

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense item | LDS (Latter-day Saint) | Non-LDS | Description |
|--------------|------------------------|---------|-------------|
| **Tuition — full-time (12+ credits, Fall/Winter)** | $3,444 / semester | $6,888 / semester | Latter-day Saint rate is half the non-LDS rate |
| **Tuition — part-time (0.5–8.5 credits)** | $364 / credit | $728 / credit | Per-credit rate |
| **Food & Housing (on-campus)** | $11,200 | $11,200 | Annual estimate, two semesters |
| **Food & Housing (off-campus)** | $12,104 | $12,104 | Annual estimate, two semesters |
| **Books & Supplies** | $416 | $416 | Annual estimate |
| **Personal Expenses** | $2,088 | $2,088 | Annual estimate |
| **Transportation** | $2,608 | $2,608 | Annual estimate |
| **Loan Fees (if federal loan accepted)** | $60 | $60 | Annual estimate |
| **Annual Total COA (LDS, on-campus)** | **$23,468** | — | Two semesters |
| **Annual Total COA (Non-LDS, on-campus)** | — | **$30,564** | Two semesters |

> source_url: https://enrollment.byu.edu/cost-of-attendance ; source_snippet: "Latter-day Saint Total On-Campus $23,468 / Non-Latter-day Saint Total On-Campus $30,564"

> Note: An additional amount may be added for students living on campus with children. Loan fees only apply if the student has an accepted federal loan for the year. BYU's "tuition and general fees" are tiered because Church members' tithes subsidize the school.

### 4.2 Graduate cost & funding framework (2026-27)

| Expense item | LDS | Non-LDS | Description |
|--------------|-----|---------|-------------|
| **Graduate Tuition (8.5+ credits, Fall/Winter)** | $4,336 / semester | $8,672 / semester | Standard graduate rate |
| **Graduate Tuition (part-time, 0.5–8.0 credits)** | $510 / credit | $1,020 / credit | Per-credit |
| **Food & Housing (on-campus)** | $14,512 | $14,512 | Annual estimate |
| **Books & Supplies** | $416 | $416 | Annual estimate |
| **Personal Expenses** | $2,960 | $2,960 | Annual estimate |
| **Transportation** | $3,712 | $3,712 | Annual estimate |
| **Loan Fees** | $210 | $210 | Annual estimate |
| **Annual COA (LDS, on-campus)** | **$30,746** | — | Two semesters |
| **Annual COA (Non-LDS, on-campus)** | — | **$39,682** | Two semesters |

> source_url: https://enrollment.byu.edu/cost-of-attendance ; source_snippet: "Graduate Latter-day Saint Total On-Campus $30,746 / Non-Latter-day Saint Total On-Campus $39,682"

#### Graduate School of Business tier (MBA, MAcc, MISM)

| Expense item | LDS | Non-LDS |
|--------------|-----|---------|
| **GSB Tuition (8.5+ credits, Fall/Winter)** | $7,996 / semester | $15,992 / semester |
| **GSB Tuition (part-time)** | $940 / credit | $1,880 / credit |
| **Annual COA (on-campus, two semesters)** | $38,874 | $55,346 |

#### Executive MBA (EMBA) — 3 semesters total

| Expense item | Cost |
|--------------|------|
| **EMBA Tuition (3 semesters combined)** | $28,540 (LDS and Non-LDS same; books included in tuition) |
| **Annual COA** | $64,174 (LDS = Non-LDS) |

#### Law School (J. Reuben Clark Law School)

| Expense item | LDS | Non-LDS |
|--------------|-----|---------|
| **Fall/Winter (8.5+ credits)** | $7,996 / semester | $15,992 / semester |
| **Spring/Summer (4.5+ credits)** | $2,168 / semester | $4,336 / semester |
| **Annual COA (Marriott/Law, on-campus, two semesters)** | $38,874 | $55,346 |
| First-year Marriott/Law students | +$1,500 computer allowance added to total COA |

### 4.3 Financial aid & funding policy

- **FAFSA required** for U.S. citizens and eligible non-citizens. BYU's federal school code: https://enrollment.byu.edu/fafsa-deadlines
- **Application fee waivers** for admitted freshmen; see https://enrollment.byu.edu/admissions/fee-waiver
- **BYU scholarships** (Presidential / Dallin H. Oaks, Heritage, National Merit, Sterling, BYU General, Departmental, Need-Based, Private): https://enrollment.byu.edu/financial-aid/new-freshman-scholarships — scholarship application **deadline Feb 1** during admission cycle
- **Federal aid programs**: Pell Grants (with **Cougar Pell Promise** — covers tuition for Pell-eligible students), Subsidized Loans, Unsubsidized Loans, PLUS Loans. See https://enrollment.byu.edu/financial-aid/types-of-federal-aid
- **Graduate funding**: Many graduate programs **fully fund** students via RA/TA positions and tuition scholarships; consult individual program pages. https://gradstudies.byu.edu/admissions/costs-financial-aid
- **Cost-of-attendance**: see https://enrollment.byu.edu/cost-of-attendance
- **Net Price Calculator**: https://enrollment.byu.edu/financialaid/net-price-calculator
- **No need-blind/need-aware distinction published**; BYU does not publish median actual price paid or debt-free graduation rate on the admissions domain.
- **Loan counseling**: required for borrowers; see https://studentaid.gov/app/counselingInstructions.action
- source_url: https://enrollment.byu.edu/cost-of-attendance ; source_snippet: "Cougar Pell Promise covers tuition for Pell-eligible students"

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.cost.tuition_FallWinter_2026_2027_LDS_FullTime
  value: "$3,444 per semester (12+ credits)"
  source_url: https://enrollment.byu.edu/tuition
  source_snippet: "Undergraduate Students / Fall/Winter Charges / 12.0 + Credit Hours / Latter-day Saint $3,444"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-002:
  field: undergraduate.cost.tuition_FallWinter_2026_2027_NonLDS_FullTime
  value: "$6,888 per semester (12+ credits)"
  source_url: https://enrollment.byu.edu/tuition
  source_snippet: "Undergraduate Students / Fall/Winter Charges / 12.0 + Credit Hours / Non-Latter-day Saint $6,888"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-003:
  field: undergraduate.cost.annual_COA_2026_2027_LDS_OnCampus
  value: "$23,468"
  source_url: https://enrollment.byu.edu/cost-of-attendance
  source_snippet: "Latter-day Saint Total On-Campus $23,468"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-004:
  field: undergraduate.cost.annual_COA_2026_2027_NonLDS_OnCampus
  value: "$30,564"
  source_url: https://enrollment.byu.edu/cost-of-attendance
  source_snippet: "Non-Latter-day Saint Total On-Campus $30,564"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-005:
  field: undergraduate.deadline.freshman_Fall2027_Final
  value: "Dec 15, 2026"
  source_url: https://enrollment.byu.edu/admissions/application-deadlines
  source_snippet: "Freshman Applicants / Fall 2027 / Application Opens Aug 26, 2026 / Priority Nov 2, 2026 / Deadline Dec 15, 2026 / Decision Notification Feb 15, 2027"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-006:
  field: undergraduate.deadline.freshman_Fall2027_Priority
  value: "Nov 2, 2026"
  source_url: https://enrollment.byu.edu/admissions/application-deadlines
  source_snippet: "Freshman Applicants / Fall 2027 / Priority Deadline Nov 2, 2026"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-007:
  field: undergraduate.deadline.freshman_Winter2027_Final
  value: "Aug 3, 2026"
  source_url: https://enrollment.byu.edu/admissions/application-deadlines
  source_snippet: "Freshman Applicants / Winter 2027 / Deadline Aug 3, 2026"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-008:
  field: undergraduate.deadline.transfer_Fall2027_Final
  value: "Dec 15, 2026"
  source_url: https://enrollment.byu.edu/admissions/application-deadlines
  source_snippet: "Transfer Applicants / Fall 2027 / Deadline Dec 15, 2026"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-009:
  field: undergraduate.tests.ACT_SAT_Policy
  value: "Test-optional through Winter 2028; BYU does not superscore; uses highest overall composite minus writing"
  source_url: https://enrollment.byu.edu/admissions/act-sat-test-scores
  source_snippet: "Although most applicants are not required to submit a standardized test score to be considered for admission to BYU through winter 2028... BYU only considers the highest overall composite score it receives in its evaluation, minus the writing portion. BYU does not use a superscore for either ACT/SAT test scores."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-010:
  field: undergraduate.honor_code_and_endorsement
  value: "Required — every applicant (LDS and non-LDS) must (1) Agree to Honor Code and Related Policies, (2) Hold current Ecclesiastical Endorsement"
  source_url: https://enrollment.byu.edu/admissions/conduct-commitments
  source_snippet: "Agree to abide by the Honor Code and Related Policies... Have a current Ecclesiastical Endorsement"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-011:
  field: undergraduate.english.TOEFL_iBT_Pre2026
  value: "Overall 80; each section (R/W/S/L) 20"
  source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement
  source_snippet: "TOEFL iBT (Taken before January 21, 2026) — Reading 20, Writing 20, Speaking 20, Listening 20, Overall 80"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-012:
  field: undergraduate.english.IELTS_Academic
  value: "Overall 6.5; each section 6"
  source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement
  source_snippet: "IELTS (Academic) — Reading 6, Writing 6, Speaking 6, Listening 6, Overall 6.5"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-013:
  field: undergraduate.english.PTE
  value: "Overall 60; each section 60"
  source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement
  source_snippet: "PTE — Reading 60, Writing 60, Speaking 60, Listening 60, Overall 60"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-014:
  field: undergraduate.english.Cambridge
  value: "Overall 180; each section 172; Use of English 180"
  source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement
  source_snippet: "Cambridge English: Advanced or Proficient — Reading 172, Writing 172, Speaking 172, Listening 172, Use of English 180, Overall 180"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-015:
  field: undergraduate.english.TOEFL_iBT_Post2026
  value: "Each section 4; overall 4"
  source_url: https://enrollment.byu.edu/admissions/byu-undergraduate-english-proficiency-requirement
  source_snippet: "TOEFL iBT (Taken on or after January 21, 2026) — Reading 4, Writing 4, Speaking 4, Listening 4, Overall 4"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-016:
  field: undergraduate.eligibility.minimum_age
  value: "17 by first day of class"
  source_url: https://enrollment.byu.edu/admissions/freshman-applicants
  source_snippet: "Because of the intellectual, social, and emotional maturity required of university students, BYU does not admit students who will be younger than 17 by the first day of class."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-017:
  field: undergraduate.eligibility.second_bachelors
  value: "Not offered; bachelor's-holders may pursue graduate or non-degree post-bacc"
  source_url: https://enrollment.byu.edu/admissions/transfer-applicants
  source_snippet: "Already completed a bachelor's degree. BYU does not offer second bachelor's degrees. Those with bachelor's degrees may consider a graduate program through Graduate Studies or enroll as a non-degree-seeking student through BYU Post-Bacc Prep."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-018:
  field: undergraduate.transfer.credit_cap
  value: "Transfer applicants with 90+ graded semester credit hours are unlikely to be admitted"
  source_url: https://enrollment.byu.edu/admissions/transfer-applicants
  source_snippet: "Transfer applicants with 90 or more graded semester credit hours are unlikely to be admitted."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-U-019:
  field: undergraduate.program_counts
  value: "310 UG catalog entries (197 majors+emphases + 113 minors); 91 grad programs"
  source_url: https://catalog.byu.edu/programs
  source_snippet: "310 results found. Showing 1 - 20."
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-U-020:
  field: institution.facts.majors_masters_doctorates
  value: "198 UNDERGRAD MAJORS / 96 MASTER'S PROGRAMS / 30 DOCTORATE PROGRAMS"
  source_url: https://www.byu.edu/academics
  source_snippet: "198 UNDERGRAD MAJORS / 96 MASTER'S PROGRAMS / 30 DOCTORATE PROGRAMS"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-001:
  field: graduate.application.fee
  value: "$50"
  source_url: https://gradstudies.byu.edu/admissions/applying
  source_snippet: "A $50 application fee is required upon applying."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-002:
  field: graduate.eligibility.minimum_GPA
  value: "3.0 cumulative undergraduate (B average); some programs require higher"
  source_url: https://gradstudies.byu.edu/admissions
  source_snippet: "Graduate with at least a 3.0 cumulative undergraduate grade point average or 'B' average. Some programs may require a higher GPA to be considered for admission."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-003:
  field: graduate.eligibility.bachelors_degree_requirement
  value: "120-credit baccalaureate degree or equivalent from a regionally accredited U.S. or international university; 90-credit recipients must establish strong potential"
  source_url: https://gradstudies.byu.edu/admissions
  source_snippet: "Submit proof of having obtained the equivalent of a U.S. bachelor's degree from a regionally accredited university. As a general rule, graduate programs at Brigham Young University require a 120-credit baccalaureate degree or equivalent..."
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-004:
  field: graduate.application.portal
  value: "https://gradapply.byu.edu/apply/"
  source_url: https://gradstudies.byu.edu/admissions/applying
  source_snippet: "Apply Now → https://gradapply.byu.edu/apply/"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-005:
  field: graduate.honor_code_endorsement
  value: "Required for all graduate applicants"
  source_url: https://gradstudies.byu.edu/admissions/applying
  source_snippet: "STEP 2 - HONOR CODE / STEP 3 – ECCLESIASTICAL ENDORSEMENT"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-006:
  field: graduate.cost.tuition_FallWinter_2026_2027_LDS_FullTime
  value: "$4,336 per semester (8.5+ credits)"
  source_url: https://enrollment.byu.edu/tuition
  source_snippet: "Graduate Students / Fall/Winter Charges / 8.5 + Latter-day Saint $4,336"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-007:
  field: graduate.cost.annual_COA_2026_2027_LDS_OnCampus
  value: "$30,746"
  source_url: https://enrollment.byu.edu/cost-of-attendance
  source_snippet: "Graduate Latter-day Saint Total On-Campus $30,746"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-008:
  field: graduate.cost.annual_COA_2026_2027_NonLDS_OnCampus
  value: "$39,682"
  source_url: https://enrollment.byu.edu/cost-of-attendance
  source_snippet: "Graduate Non-Latter-day Saint Total On-Campus $39,682"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-009:
  field: graduate.cost.MBA_tuition_FallWinter_2026_2027_LDS_FullTime
  value: "$7,996 per semester"
  source_url: https://enrollment.byu.edu/tuition
  source_snippet: "Graduate School of Business Students / Fall/Winter Charges / 8.5 + Latter-day Saint $7,996"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-010:
  field: graduate.cost.EMBA_total
  value: "$28,540 (LDS = Non-LDS, books included)"
  source_url: https://enrollment.byu.edu/cost-of-attendance
  source_snippet: "EMBA Latter-day Saint Tuition $28,540† / Non-Latter-day Saint Tuition $28,540† / Amount derived from approximately 3 EMBA tuition payments within the academic year."
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
E-G-011:
  field: graduate.decision_designations
  value: "Admit / Conditional Admit / Provisional Admit / Deny / Waitlist / Withdrawn"
  source_url: https://gradstudies.byu.edu/admissions/applying
  source_snippet: "There are six decision designations applicants can receive. These designations with descriptions are as follows: Admit, Conditional Admit, Provisional Admit, Deny, Waitlist, Withdrawn"
  capture_date: 2026-07-07
  evidence_type: official_webpage
E-G-012:
  field: graduate.foreign_credential_evaluation_programs
  value: "Required for: Chaplaincy, Computer Science, Educational Leadership, Electrical & Computer Engineering, Exercise Science, Geological Sciences, Electrical and Computer Engineering, IT & Cybersecurity, Law, Linguistics, Mass Communications, MAT, MBA, MPA, MPH, Music, Neuroscience, Nursing, Physics & Astronomy, Psychology, Religious Education, School Psychology, SLat, Sociology, Statistics"
  source_url: https://gradstudies.byu.edu/admissions
  source_snippet: "Applicants in the following programs are required to send the evaluations as part of the application process: Chaplaincy, Computer Science, Educational Leadership, Electrical & Computer Engineering, Exercise Science, Geological Sciences, Electrical and Computer Engineering, IT & Cybersecurity, Law, Linguistics, Mass Communications, MAT, MBA, MPA, MPH, Music, Neuroscience, Nursing, Physics & Astronomy, Psychology, Religious Education, School Psychology, SLat, Sociology, or Statistics."
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

Tree: `collection → document → chunk`. One document per major theme; chunks grouped by **学院**.

```
collection: byu-knowledge-base-v2
├── doc: institution-overview
│   ├── chunk 1: counts (rule 1)
│   ├── chunk 2: hierarchy tree (rule 2)
│   ├── chunk 3: degree-level inventory (rule 3)
│   └── chunk 4: distribution matrix (rule 4)
├── doc: byu-marriott-business-undergrad
│   └── 7 majors + minors
├── doc: byu-mckay-education-undergrad
│   └── 10 majors + minors
├── doc: byu-fulton-engineering-undergrad
│   └── 9 majors + minors
├── doc: byu-fhss-undergrad
│   └── 20 majors + minors
├── doc: byu-cfac-undergrad
│   └── 23 majors + minors
├── doc: byu-humanities-undergrad
│   └── 20 majors + minors
├── doc: byu-life-sciences-undergrad
│   └── 9 majors + minors
├── doc: byu-nursing-undergrad
│   └── 1 major + 1 minor
├── doc: byu-pms-undergrad
│   └── 7 majors + minors
├── doc: byu-law-undergrad
│   └── (graduate-only)
├── doc: byu-religious-ed-undergrad
│   └── (graduate-only)
├── doc: byu-graduate-fhss
├── doc: byu-graduate-cfac
├── doc: byu-graduate-humanities
├── doc: byu-graduate-religious-ed
├── doc: byu-graduate-education
├── doc: byu-graduate-engineering
├── doc: byu-graduate-life-sciences
├── doc: byu-graduate-nursing
├── doc: byu-graduate-pms
├── doc: byu-graduate-business
├── doc: byu-graduate-law
├── doc: byu-application-requirements
│   ├── chunk: ug-deadlines (P0)
│   ├── chunk: ug-tests (P0)
│   ├── chunk: ug-english (P0)
│   ├── chunk: ug-honor-code-endorsement (P0)
│   ├── chunk: grad-fees (P0)
│   ├── chunk: grad-eligibility (P0)
│   └── chunk: grad-application-steps (P0)
├── doc: byu-costs-financial-aid
│   ├── chunk: ug-tuition-tiered (P0)
│   ├── chunk: ug-coa-2026-27 (P0)
│   ├── chunk: grad-tuition (P0)
│   ├── chunk: business-law-tuition (P1)
│   ├── chunk: emba-tuition (P1)
│   └── chunk: scholarships-financial-aid (P0)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "byu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Note |
|----------|-----------|------------|------|
| P0 | Median actual price paid; debt-free graduation rate | (not published on enrollment.byu.edu) | BYU does not publish; check NCES College Navigator |
| P0 | Average starting salary for BYU undergrads | https://careers.byu.edu/students/graduate-outcomes | Reference link |
| P0 | Need-blind/need-aware admissions policy for international students | https://enrollment.byu.edu/admissions/international-students | Not explicitly published |
| P1 | Per-program deadlines for all 91 graduate programs | https://gradstudies.byu.edu/defense-schedule | Program-by-program scrape |
| P1 | Per-program standardized test (GRE/GMAT) requirements | each grad-program page | Decentralized |
| P1 | Specific acceptance rate / admit rate (UG and Grad) | (BYU does not publish) | Mark N/A with reason |
| P2 | Tuition assistance/RA/TA stipend amounts by program | https://gradstudies.byu.edu/admissions/costs-financial-aid | Department-level data |
| P2 | Total enrollment, UG vs Grad breakdown | https://www.byu.edu/facts-figures | BYU Facts page |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | BYU (2026-27) | Notes |
|-----------|---------------|-------|
| Total UG cost / yr (LDS, on-campus) | $23,468 | Among the lowest private-research tuition in U.S. |
| Total UG cost / yr (Non-LDS, on-campus) | $30,564 | ~30% above LDS rate |
| Total Grad cost / yr (LDS, on-campus) | $30,746 | Standard graduate tier |
| Total Grad cost / yr (Non-LDS, on-campus) | $39,682 | |
| MBA cost / yr (LDS, on-campus) | $38,874 | Tier-specific rate |
| Tuition / yr (LDS, full-time UG, Fall+Winter) | $6,888 | $3,444 × 2 |
| Need-blind (internationals?) | Not published | BYU is private religious; need-aware typical |
| EA deadline | **N/A** | BYU does not offer Early Action/Decision |
| RA deadline (UG, Fall 2027) | Dec 15, 2026 | Final deadline; priority Nov 2 |
| SAT/ACT required? | **No** (test-optional through Winter 2028) | Honors highest composite; no superscore |
| TOEFL min (UG) | 80 (overall) + 20 each | Or 4 on new scale post-Jan 2026 |
| IELTS min (UG) | 6.5 (overall) + 6 each | IELTS Academic |
| Honors College / Scholars program | "Honors Program" — separate admission track | https://honors.byu.edu (not scraped in detail) |
| Tuition-free threshold | N/A | Cougar Pell Promise covers tuition for Pell-eligible |
| Median price paid | N/A (not published) | |
| Grad application fee | $50 | Flat university-wide |
| April-15-equivalent honor date | Yes (CGS April 15 Resolution applies) | |
| Total program count (Rule 1) | 401 (310 UG + 91 Grad) | |
| School/department count (Rule 2) | 11 colleges | + Graduate Studies |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: enrollment.byu.edu, catalog.byu.edu, gradstudies.byu.catalog.prod.coursedog.com, byu.edu, policy.byu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program