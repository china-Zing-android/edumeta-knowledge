# Santa Clara University (SCU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS) | 53 |
| 本科辅修 (Minor) | 50+ |
| 研究生学位项目 (MA/MS/MBA/PhD/JD/etc.) | 60+ |
| 研究生高级证书 (Certificate) | 12+ |
| **学位项目总计 (UG + Grad)** | **~125** |
| 学院 / 独立系所总数 | 6 |

**Source**: SCU Undergraduate Programs page + Graduate Programs page + Bulletin 2026-27
**Source URL**: https://www.scu.edu/academics/undergraduate-programs/ ; https://www.scu.edu/academics/graduate-programs/

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Santa Clara University
├── College of Arts and Sciences (CAS)                          [学院 - UG+Grad]
│   ├── Anthropology                                            [系]
│   ├── Art and Art History                                     [系]
│   ├── Biology                                                 [系]
│   ├── Chemistry and Biochemistry                              [系]
│   ├── Child Studies                                           [系]
│   ├── Classics and Ancient Studies                            [系]
│   ├── Communication                                           [系]
│   ├── Economics                                               [系] ⚠ shared with Leavey
│   ├── English                                                 [系]
│   ├── Environmental Studies and Sciences                      [系]
│   ├── Ethnic Studies                                          [系]
│   ├── Gender and Sexuality Studies                            [系]
│   ├── History                                                 [系]
│   ├── Individual Studies                                      [系]
│   ├── Mathematics and Computer Science                        [系]
│   ├── Modern Languages and Literatures                        [系]
│   ├── Music                                                   [系]
│   ├── Neuroscience                                            [系]
│   ├── Philosophy                                              [系]
│   ├── Physics and Engineering Physics                         [系]
│   ├── Political Science                                       [系]
│   ├── Psychology                                              [系]
│   ├── Public Health Sciences                                  [系]
│   ├── Religious Studies                                       [系]
│   ├── Sociology                                               [系]
│   └── Theatre and Dance                                       [系]
├── Leavey School of Business                                   [学院 - UG+Grad]
│   ├── Accounting                                              [系]
│   ├── Economics                                               [系] ⚠ shared with CAS
│   ├── Finance                                                 [系]
│   ├── Information Systems and Analytics                       [系]
│   ├── Management and Entrepreneurship                         [系]
│   ├── Marketing                                               [系]
│   └── (Interdisciplinary: Entrepreneurship, International Business, Retail Studies, Sustainable Food Systems)
├── School of Engineering                                       [学院 - UG+Grad]
│   ├── Applied Mathematics                                     [系]
│   ├── Bioengineering                                          [系]
│   ├── Civil, Environmental, and Sustainable Engineering       [系]
│   ├── Computer Science and Engineering                        [系]
│   ├── Electrical and Computer Engineering                     [系]
│   ├── General Engineering                                     [系]
│   └── Mechanical Engineering                                  [系]
├── School of Education and Counseling Psychology               [学院 - Grad Only]
│   ├── Education                                               [系]
│   └── Counseling Psychology                                   [系]
├── School of Law                                               [学院 - Grad Only]
└── Jesuit School of Theology (JST)                             [学院 - Grad Only]
    └── Graduate Program in Pastoral Ministries                 [系]
```

**Source**: https://www.scu.edu/academics/schools-and-colleges/ ; https://www.scu.edu/bulletin/undergraduate/

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|-----------|----------------|------|------|-----------|
| BA | BA | B.A. | Bachelor of Arts | 本科 | 16 |
| BS | BS | B.S. | Bachelor of Science | 本科 | 19 |
| BSC | BS | B.S. in Commerce | Bachelor of Science in Commerce | 本科 | 9 |
| BSE | BS | B.S. | Bachelor of Science in Engineering | 本科 | 8 |
| MA | MA | M.A. | Master of Arts | 研究生 | 12 |
| MS | MS | M.S. | Master of Science | 研究生 | 16 |
| MBA | MBA | M.B.A. | Master of Business Administration | 研究生 | 3 |
| MDiv | MDiv | M.Div. | Master of Divinity | 研究生 | 1 |
| MTS | MA | M.T.S. | Master of Theological Studies | 研究生 | 1 |
| ThM | MA | Th.M. | Master of Theology | 研究生 | 1 |
| LLM | LLM | LL.M. | Master of Laws | 研究生 | 3 |
| JD | JD | J.D. | Juris Doctor | 研究生 | 2 |
| EdD | EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| PhD | PhD | Ph.D. | Doctor of Philosophy | 研究生 | 4 |
| STB | STB | S.T.B. | Bachelor of Sacred Theology | 研究生 | 1 |
| STL | STL | S.T.L. | Licentiate in Sacred Theology | 研究生 | 1 |
| STD | STD | S.T.D. | Doctor of Sacred Theology | 研究生 | 1 |
| Certificate | Certificate | Certificate | Graduate Certificate | 研究生 | 12+ |

**Source**: SCU Bulletin 2026-27 ; Graduate Programs page
**Source URL**: https://www.scu.edu/bulletin/undergraduate/ ; https://www.scu.edu/academics/graduate-programs/

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | MBA | JD | LLM | PhD | EdD | MDiv/MTS/ThM | STB/STL/STD | Certificate | 合计 |
|------------|----|----|----|----|-----|----|-----|-----|-----|--------------|-------------|-------------|------|
| College of Arts and Sciences | 16 | 27 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 48 |
| Leavey School of Business | 0 | 9 | 0 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 |
| School of Engineering | 0 | 8 | 0 | 10 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 8 | 30 |
| School of Education & Counseling Psychology | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 5 |
| Jesuit School of Theology | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 6 |
| **合计** | **16** | **44** | **7** | **14** | **3** | **2** | **3** | **4** | **1** | **3** | **3** | **9** | **~109** |

**Reconciliation**: Rule-1 total (~125) is approximate due to cross-listed programs (Economics in both CAS and Business; Computer Science in both CAS and Engineering). The matrix counts each program once under its primary administrative home.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

SCU has 3 undergraduate-degree-granting schools: College of Arts and Sciences (CAS), Leavey School of Business, and School of Engineering. Students select one school when applying; they may declare a major or remain undeclared. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences (CAS)

##### Department of Anthropology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/anthropology.html |

##### Department of Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/art-and-art-history.html |
| 2 | Studio Art | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/art-and-art-history.html |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/biology.html |

##### Department of Chemistry and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/chemistry-and-biochemistry.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/chemistry-and-biochemistry.html |
| 2 | Chemistry | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/chemistry-and-biochemistry.html |

##### Department of Child Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/child-studies.html |

##### Department of Classics and Ancient Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics and Ancient Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/classics-and-ancient-studies.html |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/communication.html |

##### Department of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/economics.html |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/english.html |

##### Department of Environmental Studies and Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/environmental-studies-and-sciences.html |
| 2 | Environmental Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/environmental-studies-and-sciences.html |

##### Department of Ethnic Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/ethnic-studies.html |

##### Department of Gender and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Gender and Sexuality Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/gender-and-sexuality-studies.html |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/history.html |

##### Department of Individual Studies
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Individual Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/individual-studies.html |

##### Department of Mathematics and Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/mathematics-and-computer-science.html |
| 2 | Computer Science | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/mathematics-and-computer-science.html |

##### Department of Modern Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French and Francophone Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/modern-languages-and-literatures.html |
| 2 | Italian Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/modern-languages-and-literatures.html |
| 3 | Spanish Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/modern-languages-and-literatures.html |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/music.html |

##### Department of Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/neuroscience.html |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/philosophy.html |

##### Department of Physics and Engineering Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/physics-and-engineering-physics.html |
| 2 | Engineering Physics | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/physics-and-engineering-physics.html |

##### Department of Political Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/political-science.html |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/psychology.html |

##### Department of Public Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health Science | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/public-health-sciences.html |

##### Department of Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/religious-studies.html |

##### Department of Sociology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/sociology.html |

##### Department of Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/theatre-and-dance.html |

---

#### Leavey School of Business

##### Department of Accounting
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/accounting.html |
| 2 | Accounting and Information Systems | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/accounting.html |

##### Department of Economics
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/economics.html |

##### Department of Finance
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/finance.html |

##### Department of Information Systems and Analytics
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/information-systems-and-analytics.html |
| 2 | Management Information Systems | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/information-systems-and-analytics.html |

##### Department of Management and Entrepreneurship
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/management.html |
| 2 | Individual Studies (Business) | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/management.html |

##### Department of Marketing
###### BS in Commerce
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/marketing.html |

---

#### School of Engineering

##### Department of Applied Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/applied-mathematics.html |

##### Department of Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/bioengineering.html |

##### Department of Civil, Environmental, and Sustainable Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/civil-environmental-and-sustainable-engineering.html |

##### Department of Computer Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/computer-science-and-engineering.html |
| 2 | Web Design and Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/computer-science-and-engineering.html |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/electrical-and-computer-engineering.html |
| 2 | Electrical and Computer Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/electrical-and-computer-engineering.html |

##### Department of General Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/general-engineering.html |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.scu.edu/bulletin/undergraduate/chapter-5-school-of-engineering/mechanical-engineering.html |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

SCU offers several interdisciplinary minors that span multiple schools:

| # | Minor | Home School(s) | URL |
|---|-------|---------------|-----|
| 1 | Entrepreneurship | Leavey School of Business | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/entrepreneurship.html |
| 2 | International Business | Leavey School of Business | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/international-business.html |
| 3 | Retail Studies | Leavey School of Business | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/retail-studies.html |
| 4 | Sustainable Food Systems | Leavey School of Business | https://www.scu.edu/bulletin/undergraduate/chapter-4-leavey-school-of-business/sustainable-food-systems.html |
| 5 | Arabic, Islamic, and Middle Eastern Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/arabic-islamic-and-middle-eastern-studies.html |
| 6 | Asian Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/asian-studies.html |
| 7 | Biotechnology | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/biotechnology.html |
| 8 | Catholic Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/catholic-studies.html |
| 9 | Gerontology | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/gerontology.html |
| 10 | International Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/international-studies.html |
| 11 | Latin American Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/latin-american-studies.html |
| 12 | Medical and Health Humanities | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/medical-and-health-humanities.html |
| 13 | Musical Theatre | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/musical-theatre.html |
| 14 | Premodern Studies | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/premodern-studies.html |
| 15 | Sustainability | CAS | https://www.scu.edu/bulletin/undergraduate/chapter-3-college-of-arts-and-sciences/sustainability.html |

### 1.4 Minors — Complete List

SCU offers minors in most departments. Key minors include:
- Business Analytics, Management Information Systems, Marketing, Real Estate (Leavey)
- All CAS departments offer minors
- Engineering departments offer minors
- Interdisciplinary minors listed in Section 1.3

### 1.5 Core Curriculum

SCU requires all undergraduates to complete the Core Curriculum, which includes:
- English (2 courses)
- Mathematics (1 course)
- Second Language (2 courses or proficiency)
- Religious Studies (2 courses)
- Philosophy (2 courses)
- Ethics (1 course)
- Social Science (2 courses)
- Natural Science (2 courses)
- Arts and Humanities (2 courses)
- Civic Engagement (1 course)
- Diversity (1 course)
- Experiential Learning (1 course)

**Source**: https://www.scu.edu/bulletin/undergraduate/chapter-2-transformative-experiences-and-learning-resources/the-core-curriculum.html

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Leavey School of Business

##### MBA Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MBA (Evening) | MBA | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Executive MBA | MBA | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Online MBA | MBA | https://www.scu.edu/academics/graduate-programs/ |

##### MS Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | M.S. Information Systems | MS | https://www.scu.edu/academics/graduate-programs/ |
| 2 | M.S. Business Analytics | MS | https://www.scu.edu/academics/graduate-programs/ |
| 3 | M.S. Finance and Analytics | MS | https://www.scu.edu/academics/graduate-programs/ |
| 4 | M.S. Marketing | MS | https://www.scu.edu/academics/graduate-programs/ |
| 5 | M.S. Sports Business | MS | https://www.scu.edu/academics/graduate-programs/ |

#### School of Engineering

##### MS Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | M.S. Aerospace Engineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 2 | M.S. Applied Mathematics | MS | https://www.scu.edu/academics/graduate-programs/ |
| 3 | M.S. Artificial Intelligence | MS | https://www.scu.edu/academics/graduate-programs/ |
| 4 | M.S. Bioengineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 5 | M.S. Civil, Environmental and Sustainable Engineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 6 | M.S. Computer Science and Engineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 7 | M.S. Electrical Engineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 8 | M.S. Engineering Management | MS | https://www.scu.edu/academics/graduate-programs/ |
| 9 | M.S. Mechanical Engineering | MS | https://www.scu.edu/academics/graduate-programs/ |
| 10 | M.S. Power Systems and Sustainable Energy | MS | https://www.scu.edu/academics/graduate-programs/ |
| 11 | M.S. Robotics and Automation | MS | https://www.scu.edu/academics/graduate-programs/ |

##### PhD Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Ph.D. Bioengineering | PhD | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Ph.D. Computer Science and Engineering | PhD | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Ph.D. Electrical Engineering | PhD | https://www.scu.edu/academics/graduate-programs/ |
| 4 | Ph.D. Mechanical Engineering | PhD | https://www.scu.edu/academics/graduate-programs/ |

##### Accelerated B.S./M.S. Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Civil Engineering B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Computer and Software Engineering B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 4 | Electrical and Computer Engineering B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 5 | Engineering Management & Leadership B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 6 | Mechanical Engineering B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |
| 7 | Power Systems and Sustainable Energy B.S./M.S. | https://www.scu.edu/academics/graduate-programs/ |

##### Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Mechanical Engineering | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Power Systems and Sustainable Energy | https://www.scu.edu/academics/graduate-programs/ |
| 4 | Robotics and Automation | https://www.scu.edu/academics/graduate-programs/ |
| 5 | Robotics and Automation (Online) | https://www.scu.edu/academics/graduate-programs/ |
| 6 | Applied Bioengineering (Online) | https://www.scu.edu/academics/graduate-programs/ |

#### School of Education and Counseling Psychology

##### MA Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | M.A. Applied Psychology | MA | https://www.scu.edu/academics/graduate-programs/ |
| 2 | M.A. Counseling | MA | https://www.scu.edu/academics/graduate-programs/ |
| 3 | M.A. Counseling Psychology | MA | https://www.scu.edu/academics/graduate-programs/ |
| 4 | M.A. Educational Leadership | MA | https://www.scu.edu/academics/graduate-programs/ |
| 5 | M.A. Teaching and Teaching Credential (MATTC) | MA | https://www.scu.edu/academics/graduate-programs/ |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Ed.D. Social Justice Leadership | EdD | https://www.scu.edu/academics/graduate-programs/ |

#### School of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor (J.D.) | JD | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Hybrid, Part-Time Flex J.D. | JD | https://www.scu.edu/academics/graduate-programs/ |
| 3 | J.D./MBA | JD/MBA | https://www.scu.edu/academics/graduate-programs/ |
| 4 | J.D./MSIS | JD/MS | https://www.scu.edu/academics/graduate-programs/ |
| 5 | LL.M. Intellectual Property | LLM | https://www.scu.edu/academics/graduate-programs/ |
| 6 | LL.M. International & Comparative Law | LLM | https://www.scu.edu/academics/graduate-programs/ |
| 7 | LL.M. United States Law | LLM | https://www.scu.edu/academics/graduate-programs/ |

#### College of Arts and Sciences — Graduate Program in Pastoral Ministries

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | M.A. Pastoral Ministries (Online & In-Person) | MA | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Graduate Certificate in Restorative Justice & Chaplaincy | Certificate | https://www.scu.edu/academics/graduate-programs/ |

#### Jesuit School of Theology (JST)

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Divinity (M.Div.) | MDiv | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Master of Theological Studies (M.T.S.) | MTS | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Master of Theology (Th.M.) | ThM | https://www.scu.edu/academics/graduate-programs/ |

##### Ecclesiastical Degree Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Bachelor of Sacred Theology (S.T.B.) | STB | https://www.scu.edu/academics/graduate-programs/ |
| 2 | Licentiate in Sacred Theology (S.T.L.) | STL | https://www.scu.edu/academics/graduate-programs/ |
| 3 | Doctor of Sacred Theology (S.T.D.) | STD | https://www.scu.edu/academics/graduate-programs/ |

### 2.2 Graduate Admissions Model

SCU graduate admissions is **decentralized** — each school manages its own admissions process:
- **Leavey School of Business**: Separate application portal; fee $100
- **School of Engineering**: Separate application portal; fee $100
- **School of Education & Counseling Psychology**: Fee $50
- **School of Law**: Fee varies; uses LSAC for J.D.
- **Jesuit School of Theology**: Fee $50
- **Pastoral Ministries**: Fee $50

**Source**: https://www.scu.edu/academics/graduate-programs/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common Application | https://www.scu.edu/admission/undergraduate/first-year-students/ |
| 申请费 | $75 (non-refundable) | https://www.scu.edu/admission/undergraduate/first-year-students/ |
| ED I 截止日期 | November 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| ED II 截止日期 | January 7 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| EA 截止日期 | November 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| RD 截止日期 | January 7 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| Winter First-Year 截止日期 | October 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| ED I 通知时间 | Late December | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| ED II 通知时间 | Mid-February | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| EA 通知时间 | Late December | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| RD 通知时间 | Late March | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| 入学押金截止 (ED I) | January 7 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| 入学押金截止 (ED II) | March 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| 入学押金截止 (EA/RD) | May 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| CSS Profile 截止 (ED I) | November 15 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| CSS Profile 截止 (ED II) | January 15 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| CSS Profile 截止 (EA) | November 15 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| CSS Profile 截止 (RD) | February 1 | https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/ |
| FAFSA Code | 001326 | https://www.scu.edu/admission/financial-aid/ |
| CSS Code | 4851 | https://www.scu.edu/admission/financial-aid/ |

**SAT/ACT Policy**: Test-optional (extended through 2026). Students who submit scores will have them considered; students who do not submit will not be disadvantaged. SCU superscores SAT and ACT.

**Source**: https://www.scu.edu/admission/undergraduate/first-year-students/test-optional/
**Source snippet**: "Santa Clara University is extending its test-optional policy for first-year and transfer students until 2026. Scores on the SAT or ACT (including the enhanced version) are not required for students applying to Santa Clara University for the 2026 term."

**Application Materials Required**:
- Official high school transcript (Grade 9 through most recently completed term)
- College transcripts (if applicable)
- One Academic Teacher Evaluation or Counselor Recommendation
- Secondary School Report
- Mid-Year Report (RD applicants or deferred EA candidates)
- $75 application fee or valid fee waiver

**Source**: https://www.scu.edu/admission/undergraduate/first-year-students/

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| IELTS | 6.5 | — | Academic module |
| TOEFL iBT | 90 (pre-Jan 2026) / 4.5 (post-Jan 2026, new scale) | — | SCU will honor scores ≥90 before Jan 2026 |
| Duolingo English Test | 120 | — | — |
| SAT EBRW | 630 | — | Can also be used for test-optional admission |
| ACT Reading + English | 27 each | — | Can also be used for test-optional admission |

**Exemptions**: Students attending secondary school in primarily anglophone countries (Australia, Anglophone Canada, Ireland, New Zealand, UK, US) AND completing 4 years at a school where the sole language of instruction was English.

**Source**: https://www.scu.edu/admission/undergraduate/international-students/undergraduate-english-proficiency/
**Source snippet**: "IELTS: 6.5; TOEFL (iBT): 90 before January 21, 2026. 4.5 after January 21, 2026; Duolingo English Test: 120"

### 3.3 Graduate — Global Rules

SCU graduate admissions is **decentralized**. Each school manages its own application:
- **Leavey School of Business**: Separate application; fee $100
- **School of Engineering**: Separate application; fee $100
- **School of Education & Counseling Psychology**: Fee $50
- **School of Law**: J.D. via LSAC; LLM via school portal
- **Jesuit School of Theology**: Fee $50
- **Pastoral Ministries**: Fee $50

**Source**: https://www.scu.edu/academics/graduate-programs/ ; Tuition PDF

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| 费用项目 | 金额 (Annual) | 备注 |
|---------|-------------|------|
| Tuition (full-time, 12+ units) | $64,956 | Per year |
| Tuition (part-time, <12 units) | $1,804 | Per unit |
| Standard Residence Hall Double (Room) | $13,383 | Annual |
| Nobili Double (Room) | $13,539 | Annual |
| Suite Double (Room) | $13,686 | Annual |
| Single Accommodations (Room) | $15,888–$23,052 | Varies by type |
| Dining Plan (Preferred) | $7,851 | Annual, 7,851 points |
| Dining Plan (Basic) | $6,711 | Annual, 6,711 points |
| Student Engagement and Well-Being Fee | $780 | Annual |
| Application Fee | $75 | One-time |
| First-Year Orientation Fee | $425 | One-time |
| Transfer Orientation Fee | $310 | One-time |
| International Student Fee | $180 | Annual ($45/quarter) |
| Tuition Insurance Refund Plan | $162 | Annual ($54/quarter) |
| Health Insurance (SHIP) | TBD | Annual |

**Estimated Total COA (on-campus, double room, preferred dining)**: ~$87,000–$90,000/year

**Source**: https://www.scu.edu/finance/bursar/tuition/ ; PDF: 2026-27-Tuition-&-Student-Fees-Schedule-UG-and-Graduate-Programs--Apr-2026.pdf
**Source snippet**: "Undergraduate Students, Employees, & Alumni Enrolled in 12 or more units $64,956 $21,652"

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| 接受经济援助学生比例 | 73% | https://www.scu.edu/admission/financial-aid/ |
| Need-blind/Need-aware | Need-aware for all (domestic and international) | https://www.scu.edu/admission/financial-aid/ |
| FAFSA Code | 001326 | https://www.scu.edu/admission/financial-aid/ |
| CSS Profile Code | 4851 | https://www.scu.edu/admission/financial-aid/ |

**Source**: https://www.scu.edu/admission/financial-aid/
**Source snippet**: "73% of Santa Clara University students receive financial aid."

### 4.3 Graduate Cost & Funding Framework

| 学院 | 学费 (per unit) | Application Fee | 备注 |
|------|----------------|-----------------|------|
| Leavey School of Business (Evening MBA/MSIS) | $1,436/unit | $100 | — |
| Leavey School of Business (Executive MBA) | $21,468–$22,327/term | $100 | Continuing vs New Cohort |
| Leavey School of Business (MS Finance) | $1,581/unit | $100 | — |
| Leavey School of Business (MS Business Analytics) | $1,581/unit | $100 | — |
| Leavey School of Business (MS Sports Business) | $1,333/unit | $100 | — |
| Leavey School of Business (MS Marketing) | $1,333/unit | $100 | — |
| School of Engineering (Graduate & Certificate) | $1,304/unit | $100 | — |
| School of Education | $816/unit | $50 | — |
| School of Education (MA Social Impact Leadership) | $875/unit | $50 | — |
| Counseling Psychology | $816/unit | $50 | — |
| Doctor of Education (EdD) | $816/unit | $50 | — |
| Pastoral Ministries | $728/unit | $50 | — |

**Source**: PDF: 2026-27-Tuition-&-Student-Fees-Schedule-UG-and-Graduate-Programs--Apr-2026.pdf

---

## SECTION 5 — Evidence Chain Index

### Evidence Blocks

```yaml
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/
source_snippet: "November 1 Deadline for Early Decision application"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.ED_II
value: "January 7"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/
source_snippet: "January 7 Deadline for Early Decision II application"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.EA
value: "November 1"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/
source_snippet: "November 1 Deadline for Early Action application"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.RD
value: "January 7"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/fy-key-deadlines/
source_snippet: "January 7 Deadline for Regular Decision application"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.test_policy
value: "test-optional (extended through 2026)"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/test-optional/
source_snippet: "Santa Clara University is extending its test-optional policy for first-year and transfer students until 2026. Scores on the SAT or ACT (including the enhanced version) are not required for students applying to Santa Clara University for the 2026 term."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.IELTS
value: 6.5
source_url: https://www.scu.edu/admission/undergraduate/international-students/undergraduate-english-proficiency/
source_snippet: "IELTS: 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.TOEFL
value: "90 (pre-Jan 2026) / 4.5 (post-Jan 2026, new scale)"
source_url: https://www.scu.edu/admission/undergraduate/international-students/undergraduate-english-proficiency/
source_snippet: "TOEFL (iBT): 90 before January 21, 2026. 4.5 after January 21, 2026"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.Duolingo
value: 120
source_url: https://www.scu.edu/admission/undergraduate/international-students/undergraduate-english-proficiency/
source_snippet: "Duolingo English Test: 120"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.costs.tuition_2026_2027
value: "$64,956/year"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Undergraduate Students, Employees, & Alumni Enrolled in 12 or more units $64,956 $21,652"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.costs.room_standard_double
value: "$13,383/year"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Standard Residence Hall Double $13,383"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.financial_aid.percent_receiving
value: "73%"
source_url: https://www.scu.edu/admission/financial-aid/
source_snippet: "73% of Santa Clara University students receive financial aid."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.application.fee
value: "$75"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/
source_snippet: "$75 non-refundable application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.application.system
value: "Common Application"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/
source_snippet: "SCU uses the Common Application for all first-year applicants."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: institution.type
value: "Private Jesuit university"
source_url: https://www.scu.edu/academics/schools-and-colleges/
source_snippet: "Santa Clara's six schools and colleges demonstrate commitment to undergraduate and graduate learning that encompasses the values of competence, conscience, and compassion."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: institution.schools
value: "6 schools/colleges"
source_url: https://www.scu.edu/academics/schools-and-colleges/
source_snippet: "The College of Arts and Sciences, the School of Engineering, and the Leavey School of Business offer undergraduate degrees. All SCU schools have graduate programs."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: graduate.tuition.engineering
value: "$1,304/unit"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "School of Engineering Graduate & Certificate Programs $1,304"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: graduate.tuition.business_evening_mba
value: "$1,436/unit"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Leavey School of Business Evening MBA/MSIS and Online Programs $1,436"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: graduate.application_fee.business
value: "$100"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Graduate Business Application Fee $100"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: graduate.application_fee.engineering
value: "$100"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Engineering Application Fee $100"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: graduate.application_fee.education
value: "$50"
source_url: https://www.scu.edu/finance/bursar/tuition/
source_snippet: "Education Application Fee $50"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
field: undergraduate.superscore
value: "Yes"
source_url: https://www.scu.edu/admission/undergraduate/first-year-students/test-optional/
source_snippet: "Yes. Students who choose to submit their test scores have the option to submit multiple scores. SCU is intere"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: institution.location
value: "Santa Clara, CA (Silicon Valley)"
source_url: https://www.scu.edu/aboutscu/
source_snippet: "Headquartered in the most innovative place on earth, Silicon Valley, Santa Clara University blends high-tech innovation with a social consciousness grounded in the Jesuit educational tradition."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
scu-knowledge-base-v2/
├── scu-overview                          # Section 0: counts, hierarchy, matrix
├── scu-cas-undergraduate                 # Section 1: CAS majors/minors
├── scu-business-undergraduate            # Section 1: Leavey majors/minors
├── scu-engineering-undergraduate         # Section 1: Engineering majors
├── scu-graduate-business                 # Section 2: Leavey grad programs
├── scu-graduate-engineering              # Section 2: Engineering grad programs
├── scu-graduate-education                # Section 2: Education/Counseling grad programs
├── scu-graduate-law                      # Section 2: Law programs
├── scu-graduate-theology                 # Section 2: JST programs
├── scu-deadlines-requirements            # Section 3: deadlines, test policy, ELP
├── scu-costs-financial-aid               # Section 4: tuition, COA, aid policy
└── scu-evidence-chain                    # Section 5: evidence blocks
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "scu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|MBA|PhD|JD|LLM|EdD|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| 优先级 | 数据项 | 目标 URL | 备注 |
|--------|--------|---------|------|
| P0 | Complete undergraduate minor list with URLs | https://www.scu.edu/bulletin/undergraduate/ | Minor count is approximate |
| P0 | Graduate program detail pages (GRE policy, deadlines per program) | Individual school pages | Decentralized; need per-program extraction |
| P0 | Net Price Calculator data | https://www.scu.edu/financialaid/net-price-calculator/ | Median actual price paid |
| P1 | Need-blind/need-aware policy details | Financial aid pages | Confirm if need-aware for internationals |
| P1 | TOEFL/IELTS requirements per graduate school | Individual school admissions pages | Decentralized |
| P1 | Graduate funding details (RA/TA/fellowship) | Individual school pages | Not centralized |
| P2 | Transfer admission requirements | https://www.scu.edu/admission/undergraduate/transfer-students/ | Not captured in this run |
| P2 | School of Law detailed program info | Law school pages | J.D./LL.M. details |
| P2 | Jesuit School of Theology detailed program info | JST pages | Ecclesiastical degree details |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | SCU | (Other Schools) |
|------|-----|-----------------|
| 所在城市 | Santa Clara, CA (Silicon Valley) | — |
| 学校性质 | Private Jesuit | — |
| 本科学费/年 | $64,956 | — |
| 预估总COA/年 (on-campus) | ~$87,000–$90,000 | — |
| Need-blind (国际生)? | Need-aware for all | — |
| EA 截止日期 | November 1 | — |
| ED 截止日期 | November 1 (ED I), January 7 (ED II) | — |
| RD 截止日期 | January 7 | — |
| SAT/ACT 要求? | Test-optional (through 2026) | — |
| TOEFL 最低 | 90 (pre-Jan 2026) / 4.5 (new scale) | — |
| IELTS 最低 | 6.5 | — |
| Duolingo 最低 | 120 | — |
| 申请费 | $75 | — |
| 研究生申请费 | $50–$100 (varies by school) | — |
| 学院/系总数 | 6 schools | — |
| 本科专业总数 | ~53 | — |
| 研究生项目总数 | ~60+ | — |
| 总项目数 (Rule 1) | ~125 | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: scu.edu (admission, academics, finance, bulletin)
> **Verification**: ego-browser snapshotText + JS DOM extraction + PDF text extraction
> **Granularity**: school → department → degree-level → program
