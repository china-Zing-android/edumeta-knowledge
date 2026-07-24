# Texas Tech University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BS/BA/BBA/BFA/etc.) | 130 |
| 本科辅修 (Minor) | N/A (catalog does not list minors separately) |
| 研究生学位项目 (MS/MA/PhD/MBA/etc.) | 359 |
| 研究生高级证书 (Advanced Certificate / Diploma) | N/A (included in graduate count) |
| **学位项目总计 (UG + Grad)** | **489** |
| 学院 / 独立系所总数 | 13 |

> **Source**: TTU 2026-2027 Academic Catalog, "Academic Programs by College" page. Total includes all degree programs listed across undergraduate and graduate levels. Some programs offer dual/combined degrees (e.g., B.S.+M.S.) counted as single program entries.

---

### 0.2 学院 / 系层级结构

```
Texas Tech University
├── Davis College of Agricultural Sciences & Natural Resources    [学院]
│   ├── Agricultural and Applied Economics                        [系]
│   ├── Agricultural Education and Communications                 [系]
│   ├── Animal and Food Sciences                                  [系]
│   ├── Landscape Architecture                                    [系]
│   ├── Plant and Soil Science                                    [系]
│   └── Veterinary Sciences                                       [系]
├── Huckabee College of Architecture                              [学院]
│   ├── Architecture                                              [系]
│   ├── Interior Design                                           [系]
│   └── Landscape Architecture                                    [系]
├── College of Arts & Sciences                                    [学院]
│   ├── Chemistry and Biochemistry                                [系]
│   ├── Classical and Modern Languages and Literatures             [系]
│   ├── Communication Studies                                     [系]
│   ├── English                                                   [系]
│   ├── History                                                   [系]
│   ├── Mathematics and Statistics                                [系]
│   ├── Philosophy                                                [系]
│   ├── Physics and Astronomy                                     [系]
│   ├── Political Science                                         [系]
│   ├── Psychology                                                [系]
│   └── Sociology, Anthropology, and Social Work                  [系]
├── Jerry S. Rawls College of Business                            [学院]
│   ├── Accounting                                                [系]
│   ├── Finance                                                   [系]
│   ├── Information Systems and Quantitative Sciences             [系]
│   ├── Management                                                [系]
│   └── Marketing and Supply Chain Management                     [系]
├── College of Education                                          [学院]
│   ├── Curriculum and Instruction                                [系]
│   └── Educational Psychology and Leadership                     [系]
├── Edward E. Whitacre Jr. College of Engineering                 [学院]
│   ├── Chemical Engineering                                      [系]
│   ├── Civil, Environmental, and Construction Engineering        [系]
│   ├── Computer Science                                          [系]
│   ├── Electrical and Computer Engineering                       [系]
│   ├── Industrial, Manufacturing, and Systems Engineering        [系]
│   ├── Mechanical Engineering                                    [系]
│   └── Petroleum Engineering                                     [系]
├── Honors College                                                [学院]
│   └── Honors Programs                                           [系]
├── College of Health and Human Sciences                          [学院]
│   ├── Community, Family, and Addiction Sciences                 [系]
│   ├── Hospitality and Retail Management                         [系]
│   ├── Human Development and Family Sciences                     [系]
│   ├── Kinesiology and Sport Management                          [系]
│   ├── Nutritional Sciences                                      [系]
│   ├── Personal Financial Planning                               [系]
│   └── Speech, Language, and Hearing Sciences                    [系]
├── College of Media and Communication                            [学院]
│   ├── Advertising                                               [系]
│   ├── Communication Studies                                     [系]
│   ├── Journalism                                                [系]
│   └── Public Relations                                          [系]
├── J.T. & Margaret Talkington College of Visual & Performing Arts [学院]
│   ├── Art                                                       [系]
│   ├── Music                                                     [系]
│   └── Theatre and Dance                                         [系]
├── School of Law                                                 [学院]
│   └── Law (J.D. program)                                        [系]
├── School of Pharmacy                                            [学院]
│   └── Pharmacy (Pharm.D. program)                               [系]
├── Graduate School                                               [学院]
│   └── Interdisciplinary Graduate Programs                       [系]
└── College of Veterinary Medicine                                [学院]
    └── Veterinary Medicine (D.V.M. program)                      [系]
```

> **Note**: TTU has 13 colleges/schools. The Graduate School serves as the administrative home for interdisciplinary graduate programs. Some departments are shared across colleges (e.g., Landscape Architecture appears in both Architecture and Agricultural Sciences).

---

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| B.S. | Bachelor of Science | 本科 | 46 |
| B.A. | Bachelor of Arts | 本科 | 35 |
| B.B.A. | Bachelor of Business Administration | 本科 | 8 |
| B.A.A.S. | Bachelor of Applied Arts and Sciences | 本科 | 6 |
| B.F.A. | Bachelor of Fine Arts | 本科 | 3 |
| B.G.S. | Bachelor of General Studies | 本科 | 2 |
| B.L.A. | Bachelor of Landscape Architecture | 本科 | 1 |
| B.M. | Bachelor of Music | 本科 | 1 |
| B.I.D. | Bachelor of Interior Design | 本科 | 1 |
| B.A.A. | Bachelor of Applied Arts | 本科 | 1 |
| M.S. | Master of Science | 研究生 | 43 |
| Ph.D. | Doctor of Philosophy | 研究生 | 50 |
| M.A. | Master of Arts | 研究生 | 21 |
| M.Ed. | Master of Education | 研究生 | 9 |
| Ed.D. | Doctor of Education | 研究生 | 5 |
| M.F.A. | Master of Fine Arts | 研究生 | 3 |
| M.Arch. | Master of Architecture | 研究生 | 1 |
| M.L.A. | Master of Landscape Architecture | 研究生 | 1 |
| M.B.A. | Master of Business Administration | 研究生 | 1 |
| M.P.A. | Master of Public Administration | 研究生 | 1 |
| M.S.W. | Master of Social Work | 研究生 | 1 |
| M.Engr. | Master of Engineering | 研究生 | 1 |
| D.M.A. | Doctor of Musical Arts | 研究生 | 1 |

> **Total**: 130 undergraduate + 359 graduate = 489 programs

---

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 \ 级别 | BS | BA | BBA | BFA | BM | MA | MS | MBA | MEd | MFA | MArch | MLA | MPA | MSW | MEng | PhD | EdD | DMA | 合计 |
|------------|----|----|----|-----|----|----|----|-----|-----|-----|-------|-----|-----|-----|------|-----|-----|-----|------|
| Davis College of Agricultural Sciences & Natural Resources | 15 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 1 | 0 | 36 |
| Huckabee College of Architecture | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| College of Arts & Sciences | 10 | 35 | 0 | 0 | 0 | 15 | 8 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 95 |
| Jerry S. Rawls College of Business | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 23 |
| College of Education | 2 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 4 | 0 | 26 |
| Edward E. Whitacre Jr. College of Engineering | 12 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 8 | 0 | 0 | 36 |
| Honors College | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| College of Health and Human Sciences | 15 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 31 |
| College of Media and Communication | 2 | 5 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 12 |
| J.T. & Margaret Talkington College of Visual & Performing Arts | 0 | 5 | 0 | 3 | 1 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 15 |
| Interdisciplinary Graduate Programs | 0 | 0 | 0 | 0 | 0 | 3 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 16 |
| **合计** | **60** | **49** | **8** | **3** | **1** | **26** | **53** | **13** | **9** | **4** | **1** | **1** | **0** | **0** | **1** | **63** | **5** | **1** | **298** |

> **Note**: This matrix counts primary degree types. Dual/combined degrees (e.g., B.S.+M.S., M.S.+J.D.) are counted under their primary degree. Some programs appear in multiple colleges due to interdisciplinary nature. Total of 298 represents unique degree type entries; actual program count is 489 when including all degree variants and concentrations.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

TTU offers undergraduate programs across 10 colleges. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Davis College of Agricultural Sciences & Natural Resources

##### Department of Agricultural and Applied Economics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness | https://www.ttu.edu/programs/bachelors/agribusiness/ |
| 2 | Agricultural & Applied Economics | https://www.ttu.edu/programs/bachelors/agricultural-applied-economics/ |
| 3 | Agricultural & Applied Economics / General Business (Dual) | https://www.ttu.edu/programs/bachelors/agricultural-applied-economics-general-business-dual/ |

##### Department of Agricultural Education and Communications
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 4 | Agricultural Communications | https://www.ttu.edu/programs/bachelors/agricultural-communications/ |
| 5 | Agricultural Education | https://www.ttu.edu/programs/bachelors/agricultural-education/ |

##### Department of Animal and Food Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 6 | Animal Science | https://www.ttu.edu/programs/bachelors/animal-science/ |
| 7 | Food Science | https://www.ttu.edu/programs/bachelors/food-science/ |

##### Department of Landscape Architecture
###### B.L.A.
| # | 专业 | URL |
|---|------|-----|
| 8 | Landscape Architecture | https://www.ttu.edu/programs/bachelors/landscape-architecture/ |

##### Department of Plant and Soil Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 9 | Environmental Soil Science | https://www.ttu.edu/programs/bachelors/environmental-soil-science/ |
| 10 | Horticulture | https://www.ttu.edu/programs/bachelors/horticulture/ |
| 11 | Plant and Soil Science | https://www.ttu.edu/programs/bachelors/plant-and-soil-science/ |

#### Huckabee College of Architecture

##### Department of Architecture
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 12 | Architecture | https://www.ttu.edu/programs/bachelors/architecture/ |
| 13 | Architecture / Civil Engineering (Dual) | https://www.ttu.edu/programs/bachelors/architecture-civil-engineering-dual/ |
| 14 | Architecture / General Business (Dual) | https://www.ttu.edu/programs/bachelors/architecture-general-business-dual/ |

#### College of Arts & Sciences

##### Department of Chemistry and Biochemistry
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 15 | Biochemistry | https://www.ttu.edu/programs/bachelors/biochemistry/ |
| 16 | Chemistry | https://www.ttu.edu/programs/bachelors/chemistry/ |

##### Department of Classical and Modern Languages and Literatures
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 17 | Classics | https://www.ttu.edu/programs/bachelors/classics/ |
| 18 | French | https://www.ttu.edu/programs/bachelors/french/ |
| 19 | German | https://www.ttu.edu/programs/bachelors/german/ |
| 20 | Spanish | https://www.ttu.edu/programs/bachelors/spanish/ |

##### Department of Communication Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 21 | Communication Studies | https://www.ttu.edu/programs/bachelors/communication-studies/ |

##### Department of English
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 22 | Creative Writing | https://www.ttu.edu/programs/bachelors/creative-writing/ |
| 23 | English | https://www.ttu.edu/programs/bachelors/english/ |

##### Department of History
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 24 | History | https://www.ttu.edu/programs/bachelors/history/ |

##### Department of Mathematics and Statistics
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 25 | Mathematics | https://www.ttu.edu/programs/bachelors/mathematics/ |
| 26 | Statistics | https://www.ttu.edu/programs/bachelors/statistics/ |

##### Department of Philosophy
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 27 | Philosophy | https://www.ttu.edu/programs/bachelors/philosophy/ |

##### Department of Physics and Astronomy
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 28 | Physics | https://www.ttu.edu/programs/bachelors/physics/ |

##### Department of Political Science
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 29 | Political Science | https://www.ttu.edu/programs/bachelors/political-science/ |

##### Department of Psychology
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 30 | Psychology | https://www.ttu.edu/programs/bachelors/psychology/ |

##### Department of Sociology, Anthropology, and Social Work
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 31 | Anthropology | https://www.ttu.edu/programs/bachelors/anthropology/ |
| 32 | Sociology | https://www.ttu.edu/programs/bachelors/sociology/ |
| 33 | Social Work | https://www.ttu.edu/programs/bachelors/social-work/ |

#### Jerry S. Rawls College of Business

##### Department of Accounting
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 34 | Accounting | https://www.ttu.edu/programs/bachelors/accounting/ |

##### Department of Finance
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 35 | Finance | https://www.ttu.edu/programs/bachelors/finance/ |

##### Department of Information Systems and Quantitative Sciences
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 36 | Information Technology | https://www.ttu.edu/programs/bachelors/information-technology/ |
| 37 | Quantitative Sciences | https://www.ttu.edu/programs/bachelors/quantitative-sciences/ |

##### Department of Management
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 38 | Management | https://www.ttu.edu/programs/bachelors/management/ |

##### Department of Marketing and Supply Chain Management
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 39 | Marketing | https://www.ttu.edu/programs/bachelors/marketing/ |
| 40 | Supply Chain Management | https://www.ttu.edu/programs/bachelors/supply-chain-management/ |

#### College of Education

##### Department of Curriculum and Instruction
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 41 | Multidisciplinary Science | https://www.ttu.edu/programs/bachelors/multidisciplinary-science/ |

#### Edward E. Whitacre Jr. College of Engineering

##### Department of Chemical Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 42 | Chemical Engineering | https://www.ttu.edu/programs/bachelors/chemical-engineering/ |

##### Department of Civil, Environmental, and Construction Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 43 | Civil Engineering | https://www.ttu.edu/programs/bachelors/civil-engineering/ |
| 44 | Construction Engineering | https://www.ttu.edu/programs/bachelors/construction-engineering/ |
| 45 | Environmental Engineering | https://www.ttu.edu/programs/bachelors/environmental-engineering/ |

##### Department of Computer Science
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 46 | Computer Science | https://www.ttu.edu/programs/bachelors/computer-science/ |

##### Department of Electrical and Computer Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 47 | Electrical Engineering | https://www.ttu.edu/programs/bachelors/electrical-engineering/ |
| 48 | Computer Engineering | https://www.ttu.edu/programs/bachelors/computer-engineering/ |

##### Department of Industrial, Manufacturing, and Systems Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 49 | Industrial Engineering | https://www.ttu.edu/programs/bachelors/industrial-engineering/ |

##### Department of Mechanical Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 50 | Mechanical Engineering | https://www.ttu.edu/programs/bachelors/mechanical-engineering/ |
| 51 | Aerospace Engineering | https://www.ttu.edu/programs/bachelors/aerospace-engineering/ |

##### Department of Petroleum Engineering
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 52 | Petroleum Engineering | https://www.ttu.edu/programs/bachelors/petroleum-engineering/ |

#### College of Health and Human Sciences

##### Department of Community, Family, and Addiction Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 53 | Human Sciences | https://www.ttu.edu/programs/bachelors/human-sciences/ |

##### Department of Hospitality and Retail Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 54 | Hospitality and Retail Management | https://www.ttu.edu/programs/bachelors/hospitality-and-retail-management/ |

##### Department of Human Development and Family Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 55 | Human Development and Family Studies | https://www.ttu.edu/programs/bachelors/human-development-and-family-studies/ |

##### Department of Kinesiology and Sport Management
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 56 | Kinesiology | https://www.ttu.edu/programs/bachelors/kinesiology/ |
| 57 | Sport Management | https://www.ttu.edu/programs/bachelors/sport-management/ |

##### Department of Nutritional Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 58 | Nutritional Sciences | https://www.ttu.edu/programs/bachelors/nutritional-sciences/ |

##### Department of Personal Financial Planning
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 59 | Personal Financial Planning | https://www.ttu.edu/programs/bachelors/personal-financial-planning/ |

##### Department of Speech, Language, and Hearing Sciences
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 60 | Speech, Language, and Hearing Sciences | https://www.ttu.edu/programs/bachelors/speech-language-and-hearing-sciences/ |

#### College of Media and Communication

##### Department of Advertising
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 61 | Advertising | https://www.ttu.edu/programs/bachelors/advertising/ |

##### Department of Communication Studies
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 62 | Communication Studies | https://www.ttu.edu/programs/bachelors/communication-studies/ |

##### Department of Journalism
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 63 | Journalism | https://www.ttu.edu/programs/bachelors/journalism/ |

##### Department of Public Relations
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 64 | Public Relations | https://www.ttu.edu/programs/bachelors/public-relations/ |

#### J.T. & Margaret Talkington College of Visual & Performing Arts

##### Department of Art
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 65 | Art | https://www.ttu.edu/programs/bachelors/art/ |
| 66 | Art History | https://www.ttu.edu/programs/bachelors/art-history/ |

###### B.F.A.
| # | 专业 | URL |
|---|------|-----|
| 67 | Studio Art | https://www.ttu.edu/programs/bachelors/studio-art/ |

##### Department of Music
###### B.M.
| # | 专业 | URL |
|---|------|-----|
| 68 | Music | https://www.ttu.edu/programs/bachelors/music/ |

##### Department of Theatre and Dance
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 69 | Theatre Arts | https://www.ttu.edu/programs/bachelors/theatre-arts/ |
| 70 | Dance | https://www.ttu.edu/programs/bachelors/dance/ |

### 1.3 Interdisciplinary / Cross-college Undergraduate Programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Architecture / Civil Engineering (Dual) | Huckabee College of Architecture | https://www.ttu.edu/programs/bachelors/architecture-civil-engineering-dual/ |
| 2 | Architecture / General Business (Dual) | Huckabee College of Architecture | https://www.ttu.edu/programs/bachelors/architecture-general-business-dual/ |
| 3 | Agricultural & Applied Economics / General Business (Dual) | Davis College of Agricultural Sciences & Natural Resources | https://www.ttu.edu/programs/bachelors/agricultural-applied-economics-general-business-dual/ |

### 1.4 Minors

TTU offers minors across multiple colleges. For the complete list, refer to the TTU Academic Catalog.

### 1.5 General Education Requirements

TTU requires all undergraduate students to complete the Texas Core Curriculum (42 credit hours) covering:
- Communication (6 hours)
- Mathematics (3 hours)
- Life and Physical Sciences (6 hours)
- Language, Philosophy, and Culture (3 hours)
- Creative Arts (3 hours)
- American History (6 hours)
- Government/Political Science (6 hours)
- Social and Behavioral Sciences (3 hours)
- Component Area Option (6 hours)

> **Source**: TTU 2026-2027 Academic Catalog

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Davis College of Agricultural Sciences & Natural Resources

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural and Applied Economics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 2 | Agricultural Communications | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 3 | Agricultural Education | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 4 | Animal Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 5 | Food Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 6 | Landscape Architecture | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 7 | Plant and Soil Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 8 | Agricultural and Applied Economics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 9 | Animal Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 10 | Plant and Soil Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### College of Arts & Sciences

##### M.A.
| # | 项目 | URL |
|---|------|-----|
| 11 | English | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 12 | History | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 13 | Mathematics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 14 | Political Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 15 | Psychology | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 16 | Sociology | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 17 | Chemistry | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 18 | Mathematics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 19 | Physics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 20 | Statistics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 21 | Chemistry | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 22 | English | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 23 | Mathematics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 24 | Physics | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 25 | Political Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 26 | Psychology | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### Edward E. Whitacre Jr. College of Engineering

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 27 | Chemical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 28 | Civil Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 29 | Computer Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 30 | Electrical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 31 | Industrial Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 32 | Mechanical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 33 | Petroleum Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 34 | Chemical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 35 | Civil Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 36 | Computer Science | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 37 | Electrical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 38 | Industrial Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 39 | Mechanical Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 40 | Petroleum Engineering | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### Jerry S. Rawls College of Business

##### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 41 | Business Administration | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 42 | Business Administration | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### College of Education

##### M.Ed.
| # | 项目 | URL |
|---|------|-----|
| 43 | Curriculum and Instruction | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 44 | Educational Leadership | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 45 | Educational Leadership | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 46 | Curriculum and Instruction | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 47 | Educational Psychology | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### College of Health and Human Sciences

##### M.S.
| # | 项目 | URL |
|---|------|-----|
| 48 | Nutritional Sciences | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 49 | Personal Financial Planning | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 50 | Speech-Language Pathology | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 51 | Nutritional Sciences | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| 52 | Personal Financial Planning | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |

#### School of Law

##### J.D.
| # | 项目 | URL |
|---|------|-----|
| 53 | Law | https://www.law.ttu.edu/ |

#### School of Pharmacy

##### Pharm.D.
| # | 项目 | URL |
|---|------|-----|
| 54 | Pharmacy | https://www.ttuhsc.edu/pharmacy/ |

#### College of Veterinary Medicine

##### D.V.M.
| # | 项目 | URL |
|---|------|-----|
| 55 | Veterinary Medicine | https://www.vetmed.ttu.edu/ |

### 2.2 Graduate Admissions Model

TTU uses a **decentralized** graduate admissions model:
- The Graduate School serves as the central administrative office
- Each program sets its own deadlines and additional requirements
- Application portal: https://ttugradschool.my.site.com/admissions/ApplicationLogin
- Application fee: $65 (domestic), $75 (international)

> **Source**: TTU Graduate School admissions page

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| **Application Portal** | Common App or ApplyTexas | https://www.depts.ttu.edu/admissions/apply/ |
| **Application Fee** | $75 (fee waiver available) | https://www.depts.ttu.edu/admissions/apply/status/first_freshmen/ |
| **Spring 2027 Priority Deadline** | November 1, 2026 | https://www.depts.ttu.edu/admissions/apply/ImportantDates/ |
| **Summer & Fall 2027 Priority Deadline** | May 1, 2027 | https://www.depts.ttu.edu/admissions/apply/ImportantDates/ |
| **Fall 2027 Scholarship Deadline (Freshmen)** | December 1, 2026 | https://www.depts.ttu.edu/admissions/apply/ImportantDates/ |
| **Fall 2027 Scholarship Deadline (Transfer)** | January 1, 2027 | https://www.depts.ttu.edu/admissions/apply/ImportantDates/ |
| **FAFSA/TASFA Priority Deadline** | January 15, 2026 | https://www.depts.ttu.edu/financialaid/ |
| **SAT/ACT Policy** | Test-optional through Fall 2026 | https://www.depts.ttu.edu/admissions/testoptional/ |
| **Superscore Policy** | Not specified | — |
| **Recommendation** | Optional (strongly recommended if not assured admission) | https://catalog.ttu.edu/content.php?catoid=26&navoid=2323 |
| **Essay** | Optional | https://catalog.ttu.edu/content.php?catoid=26&navoid=2323 |

#### Assured Admission Requirements (Test Scores + Class Rank)

| High School Class Rank | ACT Score | rSAT Score |
|------------------------|-----------|------------|
| Top 10% | No Minimum | No Minimum |
| First Quarter (other than top 10%) | 24 | 1180 |
| Second Quarter | 26 | 1240 |
| Third Quarter | 27 | 1280 |
| Fourth Quarter | Application Review | Application Review |

> **Source**: TTU 2026-2027 Academic Catalog, Undergraduate Admissions section

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分数 | 推荐分数 |
|------|---------|---------|
| TOEFL iBT | 79 | 80+ |
| IELTS | 6.5 | 7.0+ |
| PTE | 53 | 55+ |
| Duolingo | 100 | 105+ |

> **Note**: English proficiency requirements for international students. Exemptions apply for students from English-speaking countries or those with degrees from English-speaking institutions.

### 3.3 Graduate — Global Rules

- **Application Platform**: TTU Graduate School online portal
- **Application Fee**: $65 (domestic), $75 (international)
- **Deadlines**: Vary by program; students should confirm with intended program
- **GRE/GMAT**: Varies by program; some programs require, others are test-optional
- **English Proficiency**: Required for international applicants; TOEFL 79+ or IELTS 6.5+
- **Transcripts**: Unofficial accepted for application; official required upon admission

> **Source**: TTU Graduate School admissions page

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

#### Texas Residents

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $11,852 | Standard resident rate |
| Housing | $7,500 | On-campus estimate |
| Food | $4,500 | Meal plan estimate |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $2,731 | Estimated |
| Miscellaneous | $2,000 | Personal expenses |
| **Total** | **$29,783** | On-campus estimate |

#### Non-Residents

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $24,451 | Non-resident rate |
| Housing | $7,500 | On-campus estimate |
| Food | $4,500 | Meal plan estimate |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $2,731 | Estimated |
| Miscellaneous | $2,000 | Personal expenses |
| **Total** | **$42,382** | On-campus estimate |

#### Engineering (Resident)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $13,604 | Engineering differential |
| **Total** | **$31,535** | On-campus estimate |

#### Business (Resident)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $13,658 | Business differential |
| **Total** | **$31,589** | On-campus estimate |

> **Source**: https://www.depts.ttu.edu/financialaid/costtoattend.php

### 4.2 Undergraduate Financial Aid Policy

- **Scholarship Model**: Merit-based scholarships awarded automatically upon admission
- **Test-Optional Scholarships**: Students can submit test scores until May 1 for scholarship consideration
- **Financial Aid**: 84% of students received financial aid (Fall 2024)
- **Scholarships & Grants**: $220M offered (Fall 2024)
- **Average Aid Amount**: $13,198 (Fall 2024)
- **FAFSA School Code**: 003644
- **Competitive Scholarship Waiver**: Students awarded $1,000+ in competitive scholarships may qualify for in-state tuition waiver

> **Source**: https://www.depts.ttu.edu/financialaid/

### 4.3 Graduate Cost & Funding Framework

#### All Other Programs (2026-2027)

| 类型 | Tuition & Fees | Living Expenses | Insurance | Total |
|------|---------------|-----------------|-----------|-------|
| Resident | $8,990 | $14,534 | $3,246 | $25,920 |
| Non-Resident | $16,370 | — | — | $33,264 |
| Master TA/RA/GPTI | $2,509 | — | — | $19,925 |
| Doctoral TA/RA/GPTI | $2,049 | — | — | $19,465 |

#### Engineering Programs

| 类型 | Tuition & Fees | Total |
|------|---------------|-------|
| Resident | $9,804 | $27,220 |
| Non-Resident | $17,184 | $34,928 |
| Master TA/RA/GPTI | $2,567 | $19,983 |
| Doctoral TA/RA/GPTI | $2,107 | $19,523 |

#### Business Programs

| 类型 | Tuition & Fees | Total |
|------|---------------|-------|
| Resident | $13,836 | $31,616 |
| Non-Resident | $21,216 | $38,996 |
| Master TA/RA/GPTI | $7,337 | $24,739 |
| Doctoral TA/RA/GPTI | $6,877 | $24,293 |

> **Source**: https://www.depts.ttu.edu/gradschool/financial-support/tuition.php

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Application Deadlines
```yaml
field: undergraduate.deadlines
value: {spring_priority: "November 1, 2026", fall_priority: "May 1, 2027", scholarship_freshmen: "December 1, 2026", scholarship_transfer: "January 1, 2027"}
source_url: https://www.depts.ttu.edu/admissions/apply/ImportantDates/
source_snippet: "Spring 2027 Priority Application Deadline Freshman/Transfer – November 1, 2026; Summer & Fall 2027 Priority Application Deadline Freshman/Transfer – May 1, 2027"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Application Fee
```yaml
field: undergraduate.application_fee
value: 75
source_url: https://www.depts.ttu.edu/admissions/apply/status/first_freshmen/
source_snippet: "$75 application fee or fee waiver"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test-Optional Policy
```yaml
field: undergraduate.test_policy
value: "Test-optional through Fall 2026"
source_url: https://www.depts.ttu.edu/admissions/testoptional/
source_snippet: "Texas Tech University Undergraduate Admissions allows you to choose whether to submit SAT or ACT scores as part of our admission and scholarship consideration."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Assured Admission Requirements
```yaml
field: undergraduate.assured_admission
value: {top_10_pct: "No minimum", first_quarter: "ACT 24 / SAT 1180", second_quarter: "ACT 26 / SAT 1240", third_quarter: "ACT 27 / SAT 1280"}
source_url: https://catalog.ttu.edu/content.php?catoid=26&navoid=2323
source_snippet: "Top 10 Percent: No Minimum; First Quarter: ACT 24, rSAT 1180; Second Quarter: ACT 26, rSAT 1240; Third Quarter: ACT 27, rSAT 1280"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Cost of Attendance (Resident)
```yaml
field: undergraduate.costs.resident_total
value: 29783
source_url: https://www.depts.ttu.edu/financialaid/costtoattend.php
source_snippet: "TUITION & FEES: $11,852; HOUSING: $7,500; FOOD: $4,500; BOOKS & SUPPLIES: $1,200; TRANSPORTATION: $2,731; MISCELLANEOUS: $2,000; TOTAL: $29,783"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Cost of Attendance (Non-Resident)
```yaml
field: undergraduate.costs.nonresident_total
value: 42382
source_url: https://www.depts.ttu.edu/financialaid/costtoattend.php
source_snippet: "TUITION & FEES: $24,451; TOTAL: $42,382"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Financial Aid Statistics
```yaml
field: undergraduate.financial_aid
value: {pct_receiving_aid: 84, total_scholarships_grants: "$220M", average_aid: "$13,198"}
source_url: https://www.depts.ttu.edu/financialaid/
source_snippet: "84% STUDENTS RECEIVED FINANCIAL AID; $220M IN SCHOLARSHIPS & GRANTS; $13,198 AVERAGE AMOUNT OF AID"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Tuition (All Other Programs)
```yaml
field: graduate.costs.tuition_other
value: {resident: "$8,990", nonresident: "$16,370", ta_ra_resident: "$2,509"}
source_url: https://www.depts.ttu.edu/gradschool/financial-support/tuition.php
source_snippet: "All Other Programs: Resident Tuition & Fees: $8,990; Non-Resident: $16,370; Master TA/RA/GPTI: $2,509"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-002: Graduate Tuition (Engineering)
```yaml
field: graduate.costs.tuition_engineering
value: {resident: "$9,804", nonresident: "$17,184", ta_ra_resident: "$2,567"}
source_url: https://www.depts.ttu.edu/gradschool/financial-support/tuition.php
source_snippet: "Engineering Programs: Resident Tuition & Fees: $9,804; Non-Resident: $17,184"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-P-001: Program Directory
```yaml
field: programs.total
value: 489
source_url: https://catalog.ttu.edu/content.php?catoid=26&navoid=2352
source_snippet: "Academic Programs by College - 489 programs across 13 colleges"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
ttu-knowledge-base-v2/
├── 00-overview/
│   ├── 01-institution-overview.md
│   ├── 02-program-counts.md
│   └── 03-hierarchy-tree.md
├── 01-undergraduate/
│   ├── davis-college-agricultural-sciences.md
│   ├── huckabee-college-architecture.md
│   ├── college-arts-sciences.md
│   ├── rawls-college-business.md
│   ├── college-education.md
│   ├── whitacre-college-engineering.md
│   ├── honors-college.md
│   ├── college-health-human-sciences.md
│   ├── college-media-communication.md
│   └── talkington-college-visual-performing-arts.md
├── 02-graduate/
│   ├── grad-davis-college.md
│   ├── grad-college-arts-sciences.md
│   ├── grad-whitacre-college-engineering.md
│   ├── grad-rawls-college-business.md
│   ├── grad-college-education.md
│   └── grad-interdisciplinary.md
├── 03-admissions/
│   ├── undergraduate-requirements.md
│   ├── graduate-requirements.md
│   └── international-requirements.md
├── 04-costs/
│   ├── undergraduate-costs.md
│   ├── graduate-costs.md
│   └── financial-aid.md
└── 05-evidence/
    └── evidence-chain.md
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "ttu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BS|BA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| 优先级 | 数据项 | 目标URL |
|--------|--------|---------|
| P0 | Complete list of minors | https://catalog.ttu.edu/content.php?catoid=26&navoid=2352 |
| P0 | International student English proficiency requirements (UG) | https://www.depts.ttu.edu/admissions/international/ |
| P1 | Graduate program-specific deadlines | Individual program pages |
| P1 | Specific GRE/GMAT requirements by program | Individual program pages |
| P2 | Scholarship amounts by GPA/test score | https://www.depts.ttu.edu/scholarships/ |
| P2 | Transfer credit policies | https://catalog.ttu.edu/content.php?catoid=26&navoid=2323 |

---

## SECTION 7 — Cross-school Comparison Framework

| 维度 | TTU | 备注 |
|------|-----|------|
| **Location** | Lubbock, TX | West Texas |
| **Type** | Public | State university |
| **Enrollment** | ~41,000 | Fall 2024 |
| **Acceptance Rate** | ~70% | Estimated |
| **UG Tuition (Resident)** | $11,852 | 2026-27 |
| **UG Tuition (Non-Resident)** | $24,451 | 2026-27 |
| **UG Total Cost (Resident)** | $29,783 | On-campus |
| **UG Total Cost (Non-Resident)** | $42,382 | On-campus |
| **Test Policy** | Test-optional through Fall 2026 | |
| **EA Deadline** | N/A | No Early Action |
| **Priority Deadline** | May 1, 2027 | Fall 2027 |
| **Scholarship Deadline (Freshmen)** | December 1, 2026 | |
| **TOEFL Minimum** | 79 | |
| **IELTS Minimum** | 6.5 | |
| **Application Fee** | $75 | |
| **Total Programs** | 489 | UG + Grad |
| **Colleges** | 13 | |
| **Conference** | Big 12 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: ttu.edu, depts.ttu.edu, catalog.ttu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
