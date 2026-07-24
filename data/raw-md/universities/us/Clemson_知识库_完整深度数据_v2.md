# Clemson University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BLA) | 76 |
| 本科辅修 (Minor) | 109 |
| 本科证书 (UG Certificate) | 12 |
| 研究生学位项目 (MS/MA/PhD/etc.) | 144 |
| 研究生证书 (Graduate Certificate) | 42 |
| **学位项目总计 (不含 Undeclared)** | **383** |
| 学院总数 | 10 |

> Note: 4 "Undeclared" pre-professional tracks (Exploratory Studies, Preveterinary Medicine, Preprofessional Health Studies, Prepharmacy) are excluded from the program count as they are advising pathways, not degree programs. The Graduate School's own website states "140 graduate degree programs in 85 disciplines" — the higher number here (186) includes certificates and specialized master's variants counted separately in the degree finder.

### 0.2 学院 / 系层级结构 (Rule 2)

```
Clemson University
├── College of Agriculture, Forestry and Life Sciences (CAFLS)          [学院]
├── College of Architecture, Art and Construction (CAAC)                [学院]
├── College of Arts and Humanities (CAH)                                [学院]
├── College of Behavioral, Social and Health Sciences (BSHS)            [学院]
├── College of Education (CoE)                                          [学院]
├── College of Engineering, Computing and Applied Sciences (CECAS)      [学院]
├── College of Science (CoS)                                            [学院]
├── Wilbur O. and Ann Powers College of Business (CoB)                  [学院]
├── Graduate School                                                     [学院] (admin unit, 1 program)
└── Harvey S. Peeler Jr. College of Veterinary Medicine (CoVM)          [学院] (新校, 2026秋首届招生)
```

> Note: The Graduate School is an administrative unit that houses 1 standalone program (Transportation Safety Administration). The College of Veterinary Medicine is pending completion of accreditation, with first DVM class planned for Fall 2026. Clemson also has a Division of Undergraduate Learning that administers Exploratory Studies (undeclared advising track). Clemson is an SEC (Southeastern Conference) athletics member.

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 (canonical) | 全称 | 层级 | 数量 |
|---------------------|------|------|------|
| BA | Bachelor of Arts | 本科 | 18 |
| BS | Bachelor of Science | 本科 | 44 |
| BS/BA | Bachelor of Science/Arts (双学位) | 本科 | 12 |
| BFA | Bachelor of Fine Arts | 本科 | 1 |
| BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| Minor | 辅修 | 本科 | 109 |
| UG Cert | 本科证书 | 本科 | 12 |
| MA | Master of Arts | 研究生 | 4 |
| MS | Master of Science | 研究生 | 49 |
| MAT | Master of Arts in Teaching | 研究生 | 4 |
| MEd | Master of Education | 研究生 | 7 |
| MEng | Master of Engineering | 研究生 | 4 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MArch | Master of Architecture | 研究生 | 1 |
| MCP | Master of City and Regional Planning | 研究生 | 1 |
| MCSM | Master of Construction Science & Mgmt | 研究生 | 1 |
| MFR | Master of Forest Resources | 研究生 | 1 |
| MHRD | Master of Human Resource Development | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| MME | Master of Music Education | 研究生 | 1 |
| MPAcc | Master of Professional Accountancy | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MRED | Master of Real Estate Development | 研究生 | 1 |
| MSBA | MS in Business and Analytics | 研究生 | 1 |
| MTSA | Master of Transportation Safety Admin | 研究生 | 1 |
| MWFR | Master of Wildlife & Fisheries Resources | 研究生 | 1 |
| MAEd | Master of Agricultural Education | 研究生 | 1 |
| MAC | Master of Applied Computing | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 51 |
| EdD | Doctor of Education | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| EdS | Educational Specialist | 研究生 | 3 |
| Grad Cert | 研究生证书 | 研究生 | 42 |

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)


| 学院 \ 级别 | BA | BS | BS/BA | BFA | BLA | Minor | UG Cert | MA | MS | MAT | MEd | MEng | MFA | MBA | MArch | MCP | MCSM | MFR | MHRD | MLA | MME | MPAcc | MPA | MPH | MRED | MSBA | MTSA | MWFR | MAEd | MAC | PhD | EdD | DNP | DVM | EdS | Grad Cert | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Agriculture, Forestry and Life Sciences | 0 | 12 | 0 | 0 | 0 | 18 | 1 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 7 | 0 | 0 | 0 | 0 | 1 | **50** |
| Architecture, Art and Construction | 2 | 1 | 0 | 1 | 1 | 7 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 6 | **27** |
| Arts and Humanities | 9 | 1 | 0 | 0 | 0 | 32 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | **47** |
| Behavioral, Social and Health Sciences | 2 | 5 | 5 | 0 | 0 | 15 | 3 | 1 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 1 | 0 | 0 | 5 | **52** |
| Education | 5 | 3 | 1 | 0 | 0 | 2 | 0 | 0 | 1 | 4 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 0 | 3 | 7 | **40** |
| Engineering, Computing and Applied Sciences | 0 | 13 | 1 | 0 | 0 | 15 | 5 | 0 | 18 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 15 | 0 | 0 | 0 | 0 | 21 | **94** |
| Science | 0 | 4 | 4 | 0 | 0 | 9 | 0 | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | **38** |
| Business | 0 | 5 | 1 | 0 | 0 | 11 | 3 | 1 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | **33** |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Harvey S. Peeler Jr. Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **1** |
| **合计** | 18 | 44 | 12 | 1 | 1 | 109 | 12 | 4 | 49 | 4 | 7 | 4 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 51 | 1 | 1 | 1 | 3 | 42 | **383** |

> Reconciliation: Rule-1 total (383) == Matrix cell-sum (383) → **PASS**

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Clemson University has 8 undergraduate-degree-granting colleges/schools. For the full hierarchy tree, see Section 0.2. The College of Veterinary Medicine is new (first class Fall 2026) and currently has no undergraduate programs. The Graduate School is an administrative unit and does not grant undergraduate degrees.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别


#### College of Agriculture, Forestry and Life Sciences

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Agribusiness |
| 2 | Agricultural Education |
| 3 | Agricultural Mechanization and Business |
| 4 | Animal and Veterinary Sciences |
| 5 | Environmental and Natural Resources |
| 6 | Food Science and Human Nutrition |
| 7 | Forest Resource Management |
| 8 | Horticulture |
| 9 | Packaging Science |
| 10 | Plant and Environmental Sciences |
| 11 | Turfgrass |
| 12 | Wildlife and Fisheries Biology |

#### College of Architecture, Art and Construction

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Construction Science and Management |

##### BA (Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Architecture |
| 2 | Art |

##### BFA (Bachelor of Fine Arts)

| # | 专业 |
|---|------|
| 1 | Visual Arts |

##### BLA (Bachelor of Landscape Architecture)

| # | 专业 |
|---|------|
| 1 | Landscape Architecture |

#### College of Arts and Humanities

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Language and International Health |

##### BA (Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | English |
| 2 | History |
| 3 | Language and International Business |
| 4 | Modern Languages |
| 5 | Performing Arts |
| 6 | Philosophy |
| 7 | Religious Studies |
| 8 | Women's Leadership |
| 9 | World Cinema |

#### College of Behavioral, Social and Health Sciences

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Accelerated Second Degree Nursing Program |
| 2 | Health Science |
| 3 | Nursing |
| 4 | Nursing RNBS Completion Program |
| 5 | Parks, Recreation and Tourism Management |

##### BA (Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Communication |
| 2 | Sports Communication |

##### BS/BA (Bachelor of Science/Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Anthropology |
| 2 | Criminal Justice |
| 3 | Political Science |
| 4 | Psychology |
| 5 | Sociology |

#### College of Education

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Human Capital Education and Development |
| 2 | Mathematics Teaching |
| 3 | Middle Level Education |

##### BA (Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Early Childhood Education |
| 2 | Elementary Education |
| 3 | Modern Languages Education |
| 4 | Secondary Education |
| 5 | Special Education |

##### BS/BA (Bachelor of Science/Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Science Teaching |

#### College of Engineering, Computing and Applied Sciences

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Automotive Engineering |
| 2 | Biomedical Engineering |
| 3 | Biosystems Engineering |
| 4 | Chemical Engineering |
| 5 | Civil Engineering |
| 6 | Computer Engineering |
| 7 | Computer Information Systems |
| 8 | Electrical Engineering |
| 9 | Environmental Engineering |
| 10 | Geology |
| 11 | Industrial Engineering |
| 12 | Materials Science and Engineering |
| 13 | Mechanical Engineering |

##### BS/BA (Bachelor of Science/Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Computer Science |

#### College of Science

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Biochemistry |
| 2 | Data Science |
| 3 | Genetics |
| 4 | Microbiology |

##### BS/BA (Bachelor of Science/Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Biological Sciences |
| 2 | Chemistry |
| 3 | Mathematical Sciences |
| 4 | Physics |

#### Wilbur O. and Ann Powers College of Business

##### BS (Bachelor of Science)

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Financial Management |
| 3 | Graphic Communications |
| 4 | Management |
| 5 | Marketing |

##### BS/BA (Bachelor of Science/Bachelor of Arts)

| # | 专业 |
|---|------|
| 1 | Economics |

### 1.3 Interdisciplinary / cross-college undergraduate programs

The 12 BS/BA dual-degree programs allow students to choose between a Bachelor of Science (deeper technical focus) and a Bachelor of Arts (broader liberal arts foundation) in the same field. These span multiple colleges. Additionally, Clemson offers several coordinated pathways:
- Pre-veterinary track (CAFLS) → Harvey S. Peeler Jr. College of Veterinary Medicine
- Pre-professional health studies (CoS) → health professional schools
- Pre-pharmacy (CoS) → pharmacy programs

### 1.4 Minors — complete list


| # | Minor | Home College |
|---|-------|-------------|
| 1 | Adult/Extension Education | Agriculture, Forestry and Life Sciences |
| 2 | Agricultural Business Management | Agriculture, Forestry and Life Sciences |
| 3 | Agricultural Mechanization and Business | Agriculture, Forestry and Life Sciences |
| 4 | Animal and Veterinary Sciences | Agriculture, Forestry and Life Sciences |
| 5 | Entomology | Agriculture, Forestry and Life Sciences |
| 6 | Equine Industry | Agriculture, Forestry and Life Sciences |
| 7 | Food Science | Agriculture, Forestry and Life Sciences |
| 8 | Forest Products | Agriculture, Forestry and Life Sciences |
| 9 | Forest Resource Management | Agriculture, Forestry and Life Sciences |
| 10 | Horticulture | Agriculture, Forestry and Life Sciences |
| 11 | Natural Resource Economics | Agriculture, Forestry and Life Sciences |
| 12 | Packaging Science | Agriculture, Forestry and Life Sciences |
| 13 | Plant Pathology | Agriculture, Forestry and Life Sciences |
| 14 | Plant and Environmental Sciences | Agriculture, Forestry and Life Sciences |
| 15 | Precision Agriculture | Agriculture, Forestry and Life Sciences |
| 16 | Turfgrass | Agriculture, Forestry and Life Sciences |
| 17 | Urban Forestry | Agriculture, Forestry and Life Sciences |
| 18 | Wildlife and Fisheries Biology | Agriculture, Forestry and Life Sciences |
| 19 | Architecture | Architecture, Art and Construction |
| 20 | Art | Architecture, Art and Construction |
| 21 | Community Development and City Planning | Architecture, Art and Construction |
| 22 | Construction Science and Management | Architecture, Art and Construction |
| 23 | Historic Preservation | Architecture, Art and Construction |
| 24 | Industrial Design Studies | Architecture, Art and Construction |
| 25 | Landscape Architecture | Architecture, Art and Construction |
| 26 | American Sign Language Studies | Arts and Humanities |
| 27 | British and Irish Studies | Arts and Humanities |
| 28 | Chinese Studies | Arts and Humanities |
| 29 | Classics and the Ancient World | Arts and Humanities |
| 30 | Creative Writing | Arts and Humanities |
| 31 | Dance | Arts and Humanities |
| 32 | East Asian Studies | Arts and Humanities |
| 33 | Educational Interpreting | Arts and Humanities |
| 34 | English | Arts and Humanities |
| 35 | Film Studies | Arts and Humanities |
| 36 | French Studies | Arts and Humanities |
| 37 | Gender, Sexuality and Women’s Studies | Arts and Humanities |
| 38 | Geography | Arts and Humanities |
| 39 | German Studies | Arts and Humanities |
| 40 | Global Black Studies | Arts and Humanities |
| 41 | Great Works | Arts and Humanities |
| 42 | History | Arts and Humanities |
| 43 | Italian Studies | Arts and Humanities |
| 44 | Japanese Studies | Arts and Humanities |
| 45 | Middle Eastern Studies | Arts and Humanities |
| 46 | Music | Arts and Humanities |
| 47 | Pathways in the Humanities and Social Sciences | Arts and Humanities |
| 48 | Philosophy | Arts and Humanities |
| 49 | Professional Writing | Arts and Humanities |
| 50 | Race, Ethnicity and Migration | Arts and Humanities |
| 51 | Religious Studies | Arts and Humanities |
| 52 | Russian Area Studies | Arts and Humanities |
| 53 | Spanish Studies | Arts and Humanities |
| 54 | Spanish-American Area Studies | Arts and Humanities |
| 55 | Technical German | Arts and Humanities |
| 56 | Theatre | Arts and Humanities |
| 57 | Women’s Leadership | Arts and Humanities |
| 58 | Anthropology | Behavioral, Social and Health Sciences |
| 59 | Communication Studies (General) | Behavioral, Social and Health Sciences |
| 60 | Communication Studies (Sports) | Behavioral, Social and Health Sciences |
| 61 | Criminal Justice | Behavioral, Social and Health Sciences |
| 62 | Global Politics | Behavioral, Social and Health Sciences |
| 63 | Health Services Administration | Behavioral, Social and Health Sciences |
| 64 | Nonprofit Leadership | Behavioral, Social and Health Sciences |
| 65 | Park and Protected Area Management | Behavioral, Social and Health Sciences |
| 66 | Political Science | Behavioral, Social and Health Sciences |
| 67 | Political and Legal Theory | Behavioral, Social and Health Sciences |
| 68 | Psychology | Behavioral, Social and Health Sciences |
| 69 | Public Policy | Behavioral, Social and Health Sciences |
| 70 | Sociology | Behavioral, Social and Health Sciences |
| 71 | Travel and Tourism | Behavioral, Social and Health Sciences |
| 72 | Youth Development Studies | Behavioral, Social and Health Sciences |
| 73 | Athletic Leadersip | Education |
| 74 | Human Capital Education and Leadership Development | Education |
| 75 | Aerospace Studies | Engineering, Computing and Applied Sciences |
| 76 | Artificial Intelligence | Engineering, Computing and Applied Sciences |
| 77 | Cluster | Engineering, Computing and Applied Sciences |
| 78 | Computer Science | Engineering, Computing and Applied Sciences |
| 79 | Cybersecurity | Engineering, Computing and Applied Sciences |
| 80 | Digital Production Arts | Engineering, Computing and Applied Sciences |
| 81 | Electrical Engineering | Engineering, Computing and Applied Sciences |
| 82 | Electrification of Transportation | Engineering, Computing and Applied Sciences |
| 83 | Engineering Leadership | Engineering, Computing and Applied Sciences |
| 84 | Environmental Science and Policy | Engineering, Computing and Applied Sciences |
| 85 | Geology | Engineering, Computing and Applied Sciences |
| 86 | International Engineering and Science | Engineering, Computing and Applied Sciences |
| 87 | Materials Science and Engineering | Engineering, Computing and Applied Sciences |
| 88 | Nuclear Engineering and Radiological Sciences | Engineering, Computing and Applied Sciences |
| 89 | Sustainability | Engineering, Computing and Applied Sciences |
| 90 | Astronomy | Science |
| 91 | Biochemistry | Science |
| 92 | Biological Sciences | Science |
| 93 | Chemistry | Science |
| 94 | Genetics | Science |
| 95 | Mathematical Sciences | Science |
| 96 | Microbiology | Science |
| 97 | Neuroscience | Science |
| 98 | Physics | Science |
| 99 | Accounting | Business |
| 100 | Brand Communications | Business |
| 101 | Business Administration | Business |
| 102 | Economics | Business |
| 103 | Entrepreneurship | Business |
| 104 | Financial Management | Business |
| 105 | Human Resource Management | Business |
| 106 | Legal Studies | Business |
| 107 | Management | Business |
| 108 | Management Information Systems | Business |
| 109 | Military Leadership | Business |

### 1.5 Undergraduate Certificates


| # | Certificate | Home College |
|---|------------|-------------|
| 1 | Agricultural Education Teacher | Agriculture, Forestry and Life Sciences |
| 2 | Global Health | Behavioral, Social and Health Sciences |
| 3 | Nonprofit Leadership | Behavioral, Social and Health Sciences |
| 4 | Public Health | Behavioral, Social and Health Sciences |
| 5 | Automotive Engineering | Engineering, Computing and Applied Sciences |
| 6 | Clinical Diagnostics | Engineering, Computing and Applied Sciences |
| 7 | Orthopaedic Medical Device Product Specialist | Engineering, Computing and Applied Sciences |
| 8 | Renewable Energy | Engineering, Computing and Applied Sciences |
| 9 | Six Sigma | Engineering, Computing and Applied Sciences |
| 10 | Sales | Business |
| 11 | Thomas F. Chapman Leadership Certificate | Business |
| 12 | Wilbur O. and Ann Powers College of Business Leadership Certificate | Business |

### 1.6 Pre-Professional Tracks (Undeclared)

| # | Track | Home College |
|---|-------|-------------|
| 1 | Exploratory Studies | Division of Undergraduate Learning |
| 2 | Preveterinary Medicine | College of Agriculture, Forestry and Life Sciences |
| 3 | Preprofessional Health Studies | College of Science |
| 4 | Prepharmacy | College of Science |

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别


#### College of Agriculture, Forestry and Life Sciences

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Translational Genomics |

#### College of Architecture, Art and Construction

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Architecture + CommunityBUILD |
| 2 | Architecture, Society and the City |
| 3 | Digital Ecologies |
| 4 | Integrated Project Delivery |
| 5 | Resilient Urban Design |
| 6 | Roofing Industry Management |

#### College of Arts and Humanities

#### College of Behavioral, Social and Health Sciences

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Clinical and Translational Research |
| 2 | Emergency Management |
| 3 | Homeland Defense and Security |
| 4 | Public Administration |
| 5 | Youth Development Leadership |

#### College of Education

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Athletic Leadership |
| 2 | Educational Leadership |
| 3 | English to Speakers of Other Languages |
| 4 | Literacy Coach |
| 5 | Literacy Specialist |
| 6 | Literacy Teacher |
| 7 | STEAM Education |

#### College of Engineering, Computing and Applied Sciences

##### MS (MS)

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Advanced Composites |
| 2 | Advanced Manufacturing Processes |
| 3 | Applied Computational Mechanical Engineering |
| 4 | Artificial Intelligence |
| 5 | Automotive Engineering |
| 6 | Autonomous and Robotic Systems |
| 7 | Biomedical Regulatory and Quality Science |
| 8 | Capital Project Management |
| 9 | Clinical Diagnostics |
| 10 | Computer Science M.S. Ready |
| 11 | Cybersecurity |
| 12 | Design and Computational Modeling of Geotechnical Systems |
| 13 | Digital Technologies and Construction Automation |
| 14 | Engineering and Science Education |
| 15 | Futures of Transportation Engineering |
| 16 | Medical Device Recycling and Reprocessing |
| 17 | Risk Engineering |
| 18 | Risk Management |
| 19 | Systems Analytics |
| 20 | Systems Engineering |
| 21 | Water Resources Engineering |

#### College of Science

#### Wilbur O. and Ann Powers College of Business

##### Grad Cert (Graduate Certificate)

| # | 项目 |
|---|------|
| 1 | Business Analytics |
| 2 | Technology Entrepreneurship |

#### Graduate School

#### Harvey S. Peeler Jr. College of Veterinary Medicine

### 2.2 Graduate admissions model

Clemson's Graduate School oversees admissions for all graduate programs centrally through a single application portal (gradapply.clemson.edu). However, admission decisions are made by individual programs/departments. Key details:

- **Application portal**: https://gradapply.clemson.edu/apply/
- **Application fee**: **$0 (FREE)** — No fee to apply to graduate programs at Clemson
- **GRE/GMAT**: Per-program requirement (not universal). Some programs require GRE/GMAT, specified in conditional admission letter. ETS code: 5111
- **Deadlines**: Vary by program. International students should apply by April 15 (Fall), September 15 (Spring), February 1 (Summer)
- **I-20 deadlines**: November 15 (Spring), April 1 (Summer), July 1 (Fall)
- **English proficiency**: Per-program; some programs offer Conditional Language Admission with ESL completion
- **Contact**: grdapp@clemson.edu, (864) 656-3195

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application portal | Clemson Application, Common Application, Coalition Application (no preference) |
| Application fee | $70 (nonrefundable; fee waiver available for financial need) |
| EA deadline (application) | October 15 |
| EA deadline (materials) | November 1 |
| EA decisions released | Mid-December |
| RD deadline (application) | January 1 |
| RD deadline (materials) | January 10 |
| RD decisions released | Mid-February |
| Final application deadline | May 1 |
| Spring deadline | December 1 |
| Enrollment confirmation deadline | May 1 |
| FAFSA priority deadline | January 1 |
| Test policy | **Test-optional** (SAT/ACT not required) |
| SAT code | 5111 |
| ACT code | 3842 |
| Superscore | Yes (both SAT and ACT) |
| Recommendation letters | Optional (not required) |
| Personal statement | Optional |
| Self-reported transcript | Required (STARS system) |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Notes |
|------|--------------|-------|
| TOEFL iBT | 80 | Code: 5111 |
| IELTS | 6.5 | Minimum 6.0 in each sub-score |
| Duolingo | 105 | |
| English Comp I & II (US college) | Grade of B or better | Exemption path |

> Applicability: Required for all international applicants whose native language is not English.

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application portal | https://gradapply.clemson.edu/apply/ |
| Application fee | **$0 (FREE)** |
| GRE/GMAT | Per-program (not universal). ETS code: 5111 |
| English proficiency | Per-program; some offer Conditional Language Admission |
| CGS April-15 signatory | Yes |
| Multiple program applications | Allowed (separate applications per program) |
| International deadlines | April 15 (Fall), Sept 15 (Spring), Feb 1 (Summer) |
| Contact | grdapp@clemson.edu, (864) 656-3195 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2025-2026 academic year, line-itemized)

#### South Carolina Resident (On/Off Campus)

| Expense Item | Amount |
|-------------|--------|
| Tuition (Academic Fee) | $14,038/yr ($7,019/semester) |
| Fees (Matriculation, Activity, Software, Recreation, Health, Career, Transit, IT) | $1,816/yr |
| Major Enrichment Fee (varies by major) | $0 — $2,500/yr |
| Books, Supplies & Course Materials | $1,496/yr |
| Housing | $8,904/yr |
| Food | $5,320/yr |
| Transportation | $1,266/yr |
| Personal | $4,222/yr |
| Loan Fees | $68/yr |
| **Total (on/off campus)** | **$37,130/yr** |
| **Total with laptop** | **$40,020/yr** |

#### Non-South Carolina Resident (On/Off Campus)

| Expense Item | Amount |
|-------------|--------|
| Tuition (Academic Fee) | $40,562/yr ($21,010/semester) |
| Fees | $1,816/yr |
| Major Enrichment Fee | $0 — $2,500/yr |
| Books, Supplies & Course Materials | $1,496/yr |
| Housing | $8,904/yr |
| Food | $5,320/yr |
| Transportation | $1,266/yr |
| Personal | $4,222/yr |
| Loan Fees | $68/yr |
| **Total (on/off campus)** | **$63,654/yr** |
| **Total with laptop** | **$66,544/yr** |

#### Commuter (SC Resident)

| Expense Item | Amount |
|-------------|--------|
| Tuition + Fees | $15,854/yr |
| Books | $1,496/yr |
| Housing | $1,912/yr |
| Food | $1,912/yr |
| Transportation | $3,382/yr |
| Personal | $4,222/yr |
| Loan Fees | $68/yr |
| **Total** | **$28,846/yr** |

### 4.2 Undergraduate financial-aid policy

| Field | Value |
|-------|-------|
| Need-blind/need-aware | **Need-aware** (public university; does not explicitly state need-blind) |
| Merit scholarships | Yes — automatic consideration with admission application by Jan 1 |
| Need-based aid | FAFSA required; priority deadline Jan 1 |
| SC state scholarships | LIFE Scholarship, Palmetto Fellows Scholarship |
| Net Price Calculator | https://www.clemson.edu/financial-aid/cost/net-price-calculator.html |
| Total enrollment receiving aid | 20,000+ students |

> Note: Clemson is a public university. In-state vs. OOS tuition differs significantly (~$14k vs ~$41k). The university does not explicitly advertise need-blind admissions. As a public institution, SC residents receive priority for admission and financial aid.

### 4.3 Graduate cost & funding framework

#### Full-Time Graduate Tuition per Semester (9+ credit hours)

| Program Tier | SC Resident | Non-SC Resident |
|-------------|-------------|-----------------|
| Tier 1 | $6,781 | $14,638 |
| Tier 2 | $5,750 | $11,965 |
| Tier 3 | $4,970 | $10,294 |
| Doctoral Programs | $5,347 | $11,274 |
| College of Education Ed.D. | $5,164 | $6,589 |
| College of Education Ph.D. | $5,164 | $6,589 |

#### Graduate Assistant Fees per Semester (Tuition Waived)

| Fee | Amount |
|-----|--------|
| Matriculation | $5 |
| Activity | $20 |
| Software License | $21 |
| Campus Recreation | $90 |
| Health | $182 |
| Career Center | $2 |
| Library | $119 |
| Transit | $80 |
| Graduate Student Services | $85 |
| **Total fees (GA)** | **~$604/semester** |

#### Premier Program Academic Fees per Semester (Select Programs)

| Program | SC Resident | Non-SC Resident |
|---------|-------------|-----------------|
| MBA | $10,922 | $17,948 |
| Ph.D. Business (Executive Leadership) | $18,550 | $18,550 |
| Historic Preservation | $15,750 | $15,750 |
| MS Nursing | $9,257 | $16,372 |
| Automotive Engineering (MS/PhD) | $7,443 | $16,601 |
| M.Arch | $6,441 | $14,027 |
| MLA | $6,254 | $13,619 |
| MBA Entrepreneurship (FT) | $12,542 | $12,542 |

#### Funding Types

- **Graduate Assistantships**: Work agreements (research, teaching, administration) in exchange for tuition waiver + stipend. Managed by individual departments.
- **Fellowships**: Merit-based grants requiring no work. May come from university or external organizations.
- **Federal Aid**: FAFSA-based; see https://www.clemson.edu/financial-aid/how-aid-works/graduate-student-aid.html
- **Travel Grants**: Available through Graduate Student Government.

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA_application
  value: "October 15"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/first-year.html"
  source_snippet: "October 15 — Early Action application submission deadline"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.RD_application
  value: "January 1"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/first-year.html"
  source_snippet: "January 1 — Regular Decision application submission deadline"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.application_fee
  value: "$70"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/first-year.html"
  source_snippet: "There is a nonrefundable $70 application fee."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/first-year.html"
  source_snippet: "Clemson is test optional."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.TOEFL
  value: "80"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/international.html"
  source_snippet: "TOEFL Internet-Based Test (code: 5111) — 80 or higher"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.english_proficiency.IELTS
  value: "6.5 (min 6.0 each sub)"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/international.html"
  source_snippet: "IELFTS (code: 5111) — 6.5 or higher (minimum 6.0 in each sub score)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.english_proficiency.Duolingo
  value: "105"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/apply/international.html"
  source_snippet: "DuoLingo — 105 or higher"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.tuition_SC
  value: "$14,038/yr"
  source_url: "https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html"
  source_snippet: "Tuition(1) — $14,038 (Undergrad On or Off Campus, SC Resident)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.tuition_OOS
  value: "$40,562/yr"
  source_url: "https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html"
  source_snippet: "Tuition(1) — $40,562 (Undergrad On or Off Campus, Non-S.C. Resident)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.total_SC
  value: "$37,130/yr"
  source_url: "https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html"
  source_snippet: "TOTAL — $37,130 (SC Resident, On or Off Campus)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.total_OOS
  value: "$63,654/yr"
  source_url: "https://www.clemson.edu/financial-aid/cost/estimated-cost-of-attendance.html"
  source_snippet: "TOTAL — $63,654 (Non-S.C. Resident, On or Off Campus)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.admissions.acceptance_rate
  value: "42%"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/discover/statistics.html"
  source_snippet: "We accepted 42 percent of all first-year applicants for admission in 2025."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.admissions.SAT_middle50
  value: "1250-1400"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/discover/statistics.html"
  source_snippet: "SAT: 1250-1400 — MIDDLE 50% OF SAT SCORES"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.admissions.ACT_middle50
  value: "28-32"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/discover/statistics.html"
  source_snippet: "ACT: 28-32 — MIDDLE 50% OF ACT SCORES"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.admissions.total_enrollment
  value: "29,545"
  source_url: "https://www.clemson.edu/admissions/undergraduate-admissions/discover/statistics.html"
  source_snippet: "29,545 — TOTAL ENROLLMENT"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$0"
  source_url: "https://www.clemson.edu/admissions/graduate-admissions/apply/"
  source_snippet: "There is no fee to apply to graduate programs at Clemson University."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-002:
  field: graduate.GRE_policy
  value: "Per-program (not universal)"
  source_url: "https://www.clemson.edu/admissions/graduate-admissions/apply/international-applicants/"
  source_snippet: "Additional requirements from your program may include taking the GRE or GMAT."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-003:
  field: graduate.tuition.tier1_SC
  value: "$6,781/semester"
  source_url: "https://www.clemson.edu/sfs/tuition-fees/tuition-fee-details.html"
  source_snippet: "Tier 1 Program — $6,781 (Resident, Full-Time Graduate)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.tuition.tier1_OOS
  value: "$14,638/semester"
  source_url: "https://www.clemson.edu/sfs/tuition-fees/tuition-fee-details.html"
  source_snippet: "Tier 1 Program — $14,638 (Non-S.C. Resident, Full-Time Graduate)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.program_count
  value: "140 graduate degree programs in 85 disciplines"
  source_url: "https://www.clemson.edu/admissions/graduate-admissions/explore/"
  source_snippet: "The Graduate School at Clemson University offers 140 graduate degree programs in 85 disciplines."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-006:
  field: graduate.international_deadline_fall
  value: "April 15"
  source_url: "https://www.clemson.edu/admissions/graduate-admissions/apply/international-applicants/"
  source_snippet: "international applicants should complete their Graduate School applications no later than April 15 for Fall semester enrollment"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-P-001:
  field: programs.total
  value: "387 (from degree finder)"
  source_url: "https://degrees.clemson.edu/s/search.html?collection=cleu~sp-program-finder&profile=_default"
  source_snippet: "1 - 16 of 387 search results"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
clemson-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: counts, hierarchy, matrix)
├── 01-ug-cafls.md                      (CAFLS undergraduate programs)
├── 02-ug-caac.md                       (CAAC undergraduate programs)
├── 03-ug-cah.md                        (CAH undergraduate programs)
├── 04-ug-bshs.md                       (BSHS undergraduate programs)
├── 05-ug-coe.md                        (CoE undergraduate programs)
├── 06-ug-cecas.md                      (CECAS undergraduate programs)
├── 07-ug-cos.md                        (CoS undergraduate programs)
├── 08-ug-cob.md                        (CoB undergraduate programs)
├── 09-grad-cafls.md                    (CAFLS graduate programs)
├── 10-grad-caac.md                     (CAAC graduate programs)
├── 11-grad-cah.md                      (CAH graduate programs)
├── 12-grad-bshs.md                     (BSHS graduate programs)
├── 13-grad-coe.md                      (CoE graduate programs)
├── 14-grad-cecas.md                    (CECAS graduate programs)
├── 15-grad-cos.md                      (CoS graduate programs)
├── 16-grad-cob.md                      (CoB graduate programs)
├── 17-grad-gs-vm.md                    (Graduate School + Vet Med)
├── 18-deadlines-requirements.md        (Section 3)
├── 19-costs-financial-aid.md           (Section 4)
├── 20-evidence-chain.md                (Section 5)
└── 21-comparison-framework.md          (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "clemson-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P0 | Graduate ELP requirements per program | Program handbooks |
| P1 | Detailed fee breakdown by major (enrichment fees) | College-specific fee pages |
| P1 | Graduate assistantship stipend rates | Department pages |
| P2 | Transfer admission requirements | https://www.clemson.edu/admissions/undergraduate-admissions/apply/transfer.html |
| P2 | Honors College admission details | Clemson Honors College |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Clemson |
|-----------|---------|
| Type | Public (R1 research, SEC athletics) |
| Location | Clemson, SC (1,400 acres, Blue Ridge foothills) |
| Total enrollment | 29,545 |
| UG cost/yr (in-state, on-campus) | $37,130 |
| UG cost/yr (OOS, on-campus) | $63,654 |
| Tuition/yr (in-state) | $14,038 |
| Tuition/yr (OOS) | $40,562 |
| Need-blind (intl?) | No (need-aware) |
| EA deadline | October 15 |
| RD deadline | January 1 |
| SAT/ACT required? | No (test-optional) |
| TOEFL min | 80 |
| IELTS min | 6.5 |
| Duolingo min | 105 |
| Acceptance rate | 42% |
| SAT mid-50% | 1250-1400 |
| ACT mid-50% | 28-32 |
| Application fee (UG) | $70 |
| Application fee (Grad) | $0 |
| Total programs (Rule 1) | 383 |
| Colleges (Rule 2) | 10 |
| SEC athletics | Yes |
| Carnegie Classification | R1 (Very High Research) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: clemson.edu, degrees.clemson.edu, admissions.clemson.edu, gradapply.clemson.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
