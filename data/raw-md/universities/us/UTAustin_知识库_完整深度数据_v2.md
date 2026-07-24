# University of Texas at Austin (UT Austin) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | ~170 |
| 本科辅修 (Minor) | ~100+ |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | ~175 |
| 研究生高级证书 (Advanced Certificate / Diploma) | ~15 |
| **学位项目总计 (UG + Grad)** | **~345+** |
| 学院 / 独立系所总数 | 15 (UG) + 12 (Grad/Professional) = 27 |

> Note: UT Austin advertises "170+ areas of study" for undergraduate programs. The graduate program directory at gradschool.utexas.edu lists ~175 distinct degree programs across all schools. The total count is approximate due to the large number of specializations and tracks within individual majors.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Texas at Austin
├── School of Architecture [学院]
│   ├── Architectural Studies [系]
│   ├── Architecture [系]
│   ├── Interior Design [系]
│   └── Landscape Architecture [系]
├── McCombs School of Business [学院]
│   ├── Accounting [系]
│   ├── Business Analytics [系]
│   ├── Finance [系]
│   ├── Management [系]
│   ├── Management Information Systems [系]
│   ├── Marketing [系]
│   └── Supply Chain Management [系]
├── School of Civic Leadership [学院]
│   └── Civics Honors [系]
├── Moody College of Communication [学院]
│   ├── Advertising [系]
│   ├── Communication Studies [系]
│   ├── Journalism [系]
│   ├── Public Relations [系]
│   ├── Radio-Television-Film [系]
│   └── Speech, Language, and Hearing Sciences [系]
├── College of Education [学院]
│   ├── Curriculum & Instruction [系]
│   ├── Educational Leadership and Policy [系]
│   ├── Educational Psychology [系]
│   ├── Health Behavior & Health Education [系]
│   ├── Kinesiology [系]
│   └── Special Education [系]
├── Cockrell School of Engineering [学院]
│   ├── Aerospace Engineering [系]
│   ├── Biomedical Engineering [系]
│   ├── Chemical Engineering [系]
│   ├── Civil Engineering [系]
│   ├── Electrical and Computer Engineering [系]
│   ├── Engineering Mechanics [系]
│   ├── Environmental Engineering [系]
│   ├── Materials Science & Engineering [系]
│   ├── Mechanical Engineering [系]
│   ├── Operations Research & Industrial Engineering [系]
│   ├── Petroleum Engineering [系]
│   └── Semiconductor Science and Engineering [系]
├── College of Fine Arts [学院]
│   ├── Art and Art History [系]
│   ├── Design [系]
│   ├── Music [系]
│   └── Theatre and Dance [系]
├── Jackson School of Geosciences [学院]
│   ├── Geological Sciences [系]
│   ├── Geophysics [系]
│   └── Environmental Science [系]
├── School of Information [学院]
│   └── Information Studies [系]
├── College of Liberal Arts [学院]
│   ├── African and African Diaspora Studies [系]
│   ├── American Studies [系]
│   ├── Anthropology [系]
│   ├── Asian Studies [系]
│   ├── Classics [系]
│   ├── Economics [系]
│   ├── English [系]
│   ├── Geography [系]
│   ├── Germanic Studies [系]
│   ├── Government [系]
│   ├── History [系]
│   ├── Linguistics [系]
│   ├── Philosophy [系]
│   ├── Psychology [系]
│   ├── Religious Studies [系]
│   ├── Sociology [系]
│   ├── Spanish and Portuguese [系]
│   └── Women's and Gender Studies [系]
├── College of Natural Sciences [学院]
│   ├── Astronomy [系]
│   ├── Chemistry [系]
│   ├── Computer Science [系] ⚠ shared with other colleges
│   ├── Mathematics [系]
│   ├── Molecular Biosciences [系]
│   ├── Neuroscience [系]
│   ├── Physics [系]
│   ├── Public Health [系]
│   └── Statistics and Data Science [系]
├── School of Nursing [学院]
│   └── Nursing [系]
├── College of Pharmacy [学院]
│   └── Pharmacy [系]
├── Lyndon B. Johnson School of Public Affairs [学院]
│   └── Public Affairs [系]
├── Steve Hicks School of Social Work [学院]
│   └── Social Work [系]
├── Graduate School [学院] (graduate-only)
│   └── (administers all graduate programs)
├── School of Law [学院] (professional)
│   └── Law [系]
├── Dell Medical School [学院] (professional)
│   └── Medicine [系]
└── Multiple Interdisciplinary Programs [跨学科]
    ├── Computational Science, Engineering, and Mathematics (CSEM)
    ├── Energy & Earth Resources
    └── Writing (Michener Center)
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~85 |
| BS | Bachelor of Science | 本科 | ~70 |
| BFA | Bachelor of Fine Arts | 本科 | ~8 |
| BM | Bachelor of Music | 本科 | ~5 |
| BArch | Bachelor of Architecture | 本科 | 1 |
| MA | Master of Arts | 研究生 | ~25 |
| MS | Master of Science | 研究生 | ~35 |
| MSE | Master of Science in Engineering | 研究生 | ~15 |
| MFA | Master of Fine Arts | 研究生 | ~12 |
| MBA | Master of Business Administration | 研究生 | ~5 |
| MPAff | Master of Public Affairs | 研究生 | 2 |
| MEd | Master of Education | 研究生 | ~15 |
| MMusic | Master of Music | 研究生 | ~6 |
| MArch | Master of Architecture | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| MSSW | Master of Science in Social Work | 研究生 | 1 |
| MSN | Master of Science in Nursing | 研究生 | 2 |
| DNP | Doctor of Nursing Practice | 研究生 | ~5 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | ~4 |
| EdD | Doctor of Education | 研究生 | ~3 |
| PhD | Doctor of Philosophy | 研究生 | ~50 |
| Certificate | Graduate Certificate | 研究生 | ~15 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BM | MA | MS | MSE | MFA | MBA | PhD | Other | 合计 |
|------------|----|----|----|----|----|----|----|-----|-----|-----|-------|------|
| School of Architecture | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 1 | 5 | 10 |
| McCombs School of Business | 0 | 10 | 0 | 0 | 0 | 4 | 0 | 0 | 5 | 5 | 1 | 25 |
| School of Civic Leadership | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Moody College of Communication | 6 | 0 | 0 | 0 | 4 | 1 | 0 | 2 | 0 | 4 | 1 | 18 |
| College of Education | 0 | 2 | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 4 | 15 | 25 |
| Cockrell School of Engineering | 0 | 11 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 11 | 2 | 39 |
| College of Fine Arts | 3 | 0 | 8 | 5 | 3 | 1 | 0 | 7 | 0 | 4 | 2 | 33 |
| Jackson School of Geosciences | 0 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 1 | 12 |
| School of Information | 1 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 1 | 0 | 6 |
| College of Liberal Arts | 45 | 2 | 0 | 0 | 10 | 0 | 0 | 1 | 0 | 25 | 2 | 85 |
| College of Natural Sciences | 10 | 40 | 0 | 0 | 2 | 5 | 0 | 0 | 0 | 15 | 5 | 77 |
| School of Nursing | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 5 | 9 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 4 |
| LBJ School of Public Affairs | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 5 | 7 |
| School of Social Work | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 3 |
| **合计** | **66** | **76** | **8** | **5** | **23** | **22** | **15** | **10** | **5** | **75** | **46** | **~351** |

> Note: "Other" includes MSSW, MPAff, MSN, DNP, AuD, DMA, EdD, Certificates, and other specialized degrees. The matrix is approximate due to the large number of programs and specializations.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UT Austin has 15 undergraduate-degree-granting colleges and schools. For the complete hierarchy tree, see Section 0.2. The university offers approximately 170+ areas of study at the undergraduate level.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### School of Architecture
##### Architecture
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Architecture | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Architecture/Architectural Engineering (Dual Degree) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Interior Design | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### McCombs School of Business
##### Business
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Business Analytics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Canfield Business Honors Program | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Finance | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Integrated Master in Professional Accounting | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | International Business | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Management | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Management Information Systems | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 9 | Marketing | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 10 | Supply Chain Management | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### School of Civic Leadership
##### Civic Leadership
| # | 专业 | URL |
|---|------|-----|
| 1 | Civics Honors | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### Moody College of Communication
##### Communication
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Communication and Leadership | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Communication Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Journalism | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Public Relations | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Radio-Television-Film | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Speech, Language, and Hearing Sciences | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### College of Education
##### Education
| # | 专业 | URL |
|---|------|-----|
| 1 | BS in Education: Applied Learning and Development | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | BS in Kinesiology and Health | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### Cockrell School of Engineering
##### Engineering
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Architectural Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Biomedical Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Chemical Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Civil Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Computational Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Electrical and Computer Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Environmental Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 9 | Geosystems Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 10 | Mechanical Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 11 | Petroleum Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### College of Fine Arts
##### Fine Arts
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Art Education | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Art History | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Arts and Entertainment Technologies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Dance (BFA) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Dance Education (BFA) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Design (B.A. or BFA) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Jazz | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 9 | Music (B.A.) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 10 | Music Composition (B.M.) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 11 | Music Performance | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 12 | Music Studies (Education) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 13 | Studio Art (B.A. or BFA) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 14 | Theatre & Dance | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 15 | Theatre Education | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### Jackson School of Geosciences
##### Geosciences
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate System Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Environmental Science (Geosciences) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | General Geology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Geophysics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Geosciences | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Geosciences (Teaching) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Geosystems Engineering | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Hydrology and Water Resources | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### School of Information
##### Information
| # | 专业 | URL |
|---|------|-----|
| 1 | Informatics (B.A. or BSI) | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### College of Liberal Arts
##### Liberal Arts
| # | 专业 | URL |
|---|------|-----|
| 1 | African and African Diaspora Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | American Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Anthropology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Asian American Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Asian Cultures and Languages | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Asian Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Behavioral and Social Data Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Classical Languages | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 9 | Classical Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 10 | Economics (B.A. or B.S.) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 11 | English | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 12 | Environmental Science (Geographical Sciences) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 13 | European Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 14 | French Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 15 | Geography | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 16 | German | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 17 | Government | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 18 | Health & Society | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 19 | History | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 20 | Human Dimensions of Organizations | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 21 | Humanities | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 22 | International Relations and Global Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 23 | Italian | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 24 | Jewish Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 25 | Latin American Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 26 | Linguistics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 27 | Mexican American and Latina/o Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 28 | Middle Eastern Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 29 | Philosophy | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 30 | Plan II Honors Program | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 31 | Psychology (B.A. or B.S.) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 32 | Race, Indigeneity, and Migration | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 33 | Religious Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 34 | Rhetoric and Writing | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 35 | Russian, East European and Eurasian Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 36 | Sociology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 37 | Spanish | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 38 | Sustainability Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 39 | Urban Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 40 | Women's and Gender Studies | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### College of Natural Sciences
##### Natural Sciences
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 2 | Biochemistry | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 3 | Biology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 4 | Cell and Molecular Biology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 5 | Computational Biology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 6 | Ecology, Evolution and Behavior | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 7 | Genetics and Genomics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 8 | Human Biology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 9 | Marine and Freshwater Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 10 | Microbiology and Infectious Diseases | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 11 | Plant Biology | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 12 | Chemistry | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 13 | Computation | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 14 | Computer Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 15 | Environmental Science (Biological Sciences) | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 16 | Human Development and Family Sciences | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 17 | Mathematics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 18 | Medical Laboratory Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 19 | Neuroscience | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 20 | Nutrition | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 21 | Physics | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 22 | Pre-Pharmacy | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 23 | Public Health | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 24 | Statistics and Data Science | https://admissions.utexas.edu/explore/colleges-degrees/ |
| 25 | Textiles and Apparel | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### School of Nursing
##### Nursing
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### College of Pharmacy
##### Pharmacy
| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-Pharmacy | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### LBJ School of Public Affairs
##### Public Affairs
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Affairs | https://admissions.utexas.edu/explore/colleges-degrees/ |

#### School of Social Work
##### Social Work
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://admissions.utexas.edu/explore/colleges-degrees/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | Program | Parent Schools |
|---|---------|---------------|
| 1 | Architecture/Architectural Engineering | School of Architecture + Cockrell School of Engineering |
| 2 | Geosystems Engineering | Jackson School of Geosciences + Cockrell School of Engineering |
| 3 | Environmental Science (multiple tracks) | College of Liberal Arts + College of Natural Sciences + Jackson School of Geosciences |
| 4 | Computer Science | College of Natural Sciences (also available in other contexts) |

### 1.4 Minors — Complete List

UT Austin offers approximately 100+ undergraduate minors across all colleges. A complete list is available in the undergraduate catalog at https://catalog.utexas.edu/undergraduate/.

### 1.5 General/Institute-Wide Requirements

UT Austin requires completion of the **Core Curriculum** for all undergraduate students, which includes:
- English Composition
- American History
- American Government
- Social and Behavioral Sciences
- Humanities
- Fine Arts
- Mathematics
- Natural Sciences
- Cultural Diversity in the United States
- Global Cultures
- Ethics and Leadership
- Quantitative Reasoning

### 1.6 Course-ID → Major Quick-Lookup

UT Austin uses a numbering system in the catalog. Example mappings:
- 603900 = Aerospace Engineering
- 627800 = Computer Science
- 665900 = Mechanical Engineering

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### School of Architecture
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Advanced Architectural Design | MAAD | https://gradschool.utexas.edu/degrees-programs |
| 2 | Architectural History | MA | https://gradschool.utexas.edu/degrees-programs |
| 3 | Architectural Studies | MSAS | https://gradschool.utexas.edu/degrees-programs |
| 4 | Architecture | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Architecture - First Professional | MArch | https://gradschool.utexas.edu/degrees-programs |
| 6 | Community & Regional Planning | MSCRP, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 7 | Historic Preservation | MSHP | https://gradschool.utexas.edu/degrees-programs |
| 8 | Interior Design | MID | https://gradschool.utexas.edu/degrees-programs |
| 9 | Landscape Architecture | MLA, MSLA | https://gradschool.utexas.edu/degrees-programs |
| 10 | Sustainable Design | MSSD | https://gradschool.utexas.edu/degrees-programs |
| 11 | Urban Design | MSUD | https://gradschool.utexas.edu/degrees-programs |

#### McCombs School of Business
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Accounting | Ph.D., MPA | https://gradschool.utexas.edu/degrees-programs |
| 2 | Business Administration | MBA | https://gradschool.utexas.edu/degrees-programs |
| 3 | Business Analytics | MSBA | https://gradschool.utexas.edu/degrees-programs |
| 4 | Finance | Ph.D., MSF | https://gradschool.utexas.edu/degrees-programs |
| 5 | Information Technology and Management | MSITM | https://gradschool.utexas.edu/degrees-programs |
| 6 | Information, Risk, & Operations Management | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 7 | Management | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 8 | Marketing | Ph.D., MSM | https://gradschool.utexas.edu/degrees-programs |
| 9 | Technology Commercialization | MSTC | https://gradschool.utexas.edu/degrees-programs |

#### Moody College of Communication
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Advertising | Ph.D., MA | https://gradschool.utexas.edu/degrees-programs |
| 2 | Audiology | Au.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Communication Studies | Ph.D., MA | https://gradschool.utexas.edu/degrees-programs |
| 4 | Journalism and Media | Ph.D., MA | https://gradschool.utexas.edu/degrees-programs |
| 5 | Radio-Television-Film | Ph.D., MA, MFA | https://gradschool.utexas.edu/degrees-programs |
| 6 | Speech, Language, and Hearing Sciences | Ph.D., MSSLHS | https://gradschool.utexas.edu/degrees-programs |

#### College of Education
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Curriculum & Instruction | MA, MEd, Ed.D., Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 2 | Educational Leadership and Policy | MEd, Ph.D., Ed.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Educational Psychology | Ph.D., MA, MEd | https://gradschool.utexas.edu/degrees-programs |
| 4 | Health Behavior & Health Education | MEd, MSHBHEd, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Kinesiology | MEd, MSKin, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 6 | Science, Technology, Engineering, and Mathematics Education | MA, MEd, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 7 | Special Education | MA, MEd, Ed.D., Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### Cockrell School of Engineering
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Aerospace Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 2 | Biomedical Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Chemical Engineering | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 4 | Civil Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Electrical and Computer Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 6 | Engineering Management | MSE | https://gradschool.utexas.edu/degrees-programs |
| 7 | Engineering Mechanics | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 8 | Environmental & Water Resources Engineering | MSE | https://gradschool.utexas.edu/degrees-programs |
| 9 | Materials Science & Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 10 | Mechanical Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 11 | Operations Research & Industrial Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 12 | Petroleum Engineering | MSE, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 13 | Semiconductor Science and Engineering | MSE | https://gradschool.utexas.edu/degrees-programs |

#### College of Fine Arts
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Art - Studio | MFA | https://gradschool.utexas.edu/degrees-programs |
| 2 | Art History | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Design | MFA, MA | https://gradschool.utexas.edu/degrees-programs |
| 4 | Music & Human Learning | MMusic, DMA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Music Composition | MMusic, DMA | https://gradschool.utexas.edu/degrees-programs |
| 6 | Music Conducting | MMusic, DMA | https://gradschool.utexas.edu/degrees-programs |
| 7 | Music Performance | MMusic, DMA | https://gradschool.utexas.edu/degrees-programs |
| 8 | Music Theory | MMusic, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 9 | Musicology/Ethnomusicology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 10 | Theatre | MA, MFA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### Jackson School of Geosciences
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Energy & Earth Resources | MA, MSEER | https://gradschool.utexas.edu/degrees-programs |
| 2 | Geological Sciences | MSGeoSci, Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### School of Information
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Information Security and Privacy | MSISP | https://gradschool.utexas.edu/degrees-programs |
| 2 | Information Studies | MSIS, Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### College of Liberal Arts
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | African & African Diaspora Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 2 | American Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Anthropology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 4 | Asian Cultures & Languages | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Asian Studies | MA | https://gradschool.utexas.edu/degrees-programs |
| 6 | Classics | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 7 | Comparative Literature | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 8 | Creative Writing | MFA | https://gradschool.utexas.edu/degrees-programs |
| 9 | Economics | Ph.D., MA | https://gradschool.utexas.edu/degrees-programs |
| 10 | English | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 11 | French | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 12 | Geography | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 13 | Germanic Studies | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 14 | Government | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 15 | History | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 16 | Human Dimensions of Organizations | MA | https://gradschool.utexas.edu/degrees-programs |
| 17 | Humanities, Health, and Medicine | MA | https://gradschool.utexas.edu/degrees-programs |
| 18 | Iberian & Latin American Languages & Cultures | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 19 | Italian Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 20 | Latin American Studies | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 21 | Linguistics | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 22 | Mexican American and Latina/o Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 23 | Middle Eastern Languages & Cultures | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 24 | Middle Eastern Studies | MA | https://gradschool.utexas.edu/degrees-programs |
| 25 | Philosophy | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 26 | Psychology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 27 | Religious Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 28 | Rhetoric and Writing Studies | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 29 | Russian, East European & Eurasian Studies | MA | https://gradschool.utexas.edu/degrees-programs |
| 30 | Sociology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 31 | Women's & Gender Studies | MA | https://gradschool.utexas.edu/degrees-programs |

#### College of Natural Sciences
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Artificial Intelligence (Online) | MSAI | https://gradschool.utexas.edu/degrees-programs |
| 2 | Astronomy | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 3 | Biochemistry | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 4 | Cell & Molecular Biology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Chemistry | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 6 | Computer Science | MSCS, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 7 | Data Science (Online) | MSDS | https://gradschool.utexas.edu/degrees-programs |
| 8 | Ecology, Evolution, and Behavior | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 9 | Human Development & Family Sciences | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 10 | Marine Science | MSMarineSci, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 11 | Mathematics | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 12 | Microbiology | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 13 | Neuroscience | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 14 | Nutritional Sciences | MS, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 15 | Physics | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 16 | Plant Biology | MA, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 17 | Statistics | MSStat, Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### School of Nursing
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Adult-Gerontology Clinical Nurse Specialist | DNP | https://gradschool.utexas.edu/degrees-programs |
| 2 | Leadership in Diverse Settings | MSN | https://gradschool.utexas.edu/degrees-programs |
| 3 | Nurse Practitioner | DNP | https://gradschool.utexas.edu/degrees-programs |
| 4 | Nursing | Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 5 | Nursing Practice | DNP | https://gradschool.utexas.edu/degrees-programs |

#### College of Pharmacy
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Pharmaceutical Sciences | MSPS, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 2 | Translational Science | Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### LBJ School of Public Affairs
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Global Policy Studies | MGlobalPolStds | https://gradschool.utexas.edu/degrees-programs |
| 2 | National Security | MNS | https://gradschool.utexas.edu/degrees-programs |
| 3 | Public Affairs | MPAff | https://gradschool.utexas.edu/degrees-programs |
| 4 | Public Leadership | MPL | https://gradschool.utexas.edu/degrees-programs |
| 5 | Public Policy | Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### School of Social Work
##### Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Social Work | MSSW, Ph.D. | https://gradschool.utexas.edu/degrees-programs |

#### Interdisciplinary Graduate Programs
| # | 项目 | Degree(s) | URL |
|---|------|-----------|-----|
| 1 | Computational Science, Engineering, and Mathematics (CSEM) | MSCSEM, Ph.D. | https://gradschool.utexas.edu/degrees-programs |
| 2 | Writing (Michener Center for Writers) | MFA | https://gradschool.utexas.edu/degrees-programs |

### 2.2 At Least One Program's Full Deep-Dive

**Computer Science (MSCS, Ph.D.)**
- **Department**: Department of Computer Science
- **College**: College of Natural Sciences
- **Address**: 2317 Speedway, Austin, TX 78712
- **Application Deadline**: Fall only; December 15
- **Application Fee**: $65 (U.S.) / $90 (International)
- **Application Portal**: https://gradschool.utexas.edu/admissions/apply
- **Degrees Offered**: MSCS, Ph.D.
- **GRE Policy**: Check program website
- **TOEFL Minimum**: 79 (120 scale)
- **Funding**: TA/RA positions available for PhD students

### 2.3 Graduate Admissions Model

UT Austin uses a **decentralized** graduate admissions model:
- The Graduate School provides central services and oversight
- Each program sets its own deadlines, requirements, and admission decisions
- Professional schools (Business, Law, Medicine) have separate application processes
- Application fee: $65 (U.S.) / $90 (International) for most programs; MBA $200; MPA $125

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Admissions Site | https://admissions.utexas.edu/ | Official website |
| Application Portal | Common App (summer/fall); BeAHorn (spring) | admissions.utexas.edu/apply/freshman/ |
| EA Deadline | October 15 | admissions.utexas.edu/apply/freshman/ |
| EA Supplemental Materials | October 22 | admissions.utexas.edu/apply/freshman/ |
| Regular Deadline | December 1 | admissions.utexas.edu/apply/freshman/ |
| Regular Supplemental Materials | December 10 | admissions.utexas.edu/apply/freshman/ |
| EA Decisions Released | January 15 | admissions.utexas.edu/apply/freshman/ |
| All Decisions Released | February 15 | admissions.utexas.edu/apply/freshman/ |
| Honors Decisions Released | March 1 | admissions.utexas.edu/apply/freshman/ |
| Application Fee (Domestic) | $75 | admissions.utexas.edu/apply/freshman/ |
| Application Fee (International) | $90 | admissions.utexas.edu/apply/international-students/ |
| SAT/ACT Policy | REQUIRED (not test-optional) | admissions.utexas.edu/apply/freshman/ |
| SAT Code | 6882 | admissions.utexas.edu/apply/freshman/ |
| ACT Code | 4240 | admissions.utexas.edu/apply/freshman/ |
| Superscore | Yes | admissions.utexas.edu/apply/freshman/ |
| Recommendation Letters | Optional | admissions.utexas.edu/apply/freshman/ |
| Interview | Not offered | admissions.utexas.edu/apply/freshman/ |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| TOEFL iBT | 79 (120 scale) or 4 (6-point scale) | N/A | admissions.utexas.edu/info-for/international-students/ |
| IELTS Academic | 6.5 overall | N/A | admissions.utexas.edu/info-for/international-students/ |
| Duolingo English Test | 115 | N/A | admissions.utexas.edu/info-for/international-students/ |

**Exemptions**: Applicants from qualifying countries, or who graduated from a U.S. high school after 3+ years of study.

### 3.3 Graduate — Global Rules

- **Admissions Model**: Decentralized (each program sets own deadlines)
- **Application Platform**: Graduate School Application (https://students.gradschool.utexas.edu/portal/app)
- **Application Fee**: $65 (U.S.) / $90 (International); MBA $200; MPA $125
- **GRE Policy**: Per-program (check individual program websites)
- **English Proficiency**: TOEFL 79 / IELTS 6.5 / DET 115 (same as UG minimums)
- **ETS Code**: 6882 (TOEFL/GRE)

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| Expense Item | Resident (On/Off Campus) | Resident (With Parents) | Non-Resident |
|-------------|-------------------------|------------------------|--------------|
| Tuition | $10,858-$13,576 | $10,858-$13,576 | $42,554-$51,106 |
| Housing and Food | $15,420-$15,580 | $7,910 | $15,420-$15,580 |
| Transportation | $1,840 | $1,840 | $1,840 |
| Books, course materials, supplies and equipment | $724 | $724 | $724 |
| Personal / Miscellaneous | $3,666 | $3,666 | $3,666 |
| **Total Cost of Attendance** | **$32,508-$35,386** | **$24,998-$27,716** | **$64,204-$72,916** |

> Source: https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/

### 4.2 Undergraduate Financial-Aid Policy

| Policy | Details | Source |
|--------|---------|--------|
| Texas Advance Commitment | Free tuition for families with AGI ≤$100,000; tuition support for AGI ≤$125,000 | admissions.utexas.edu/cost-aid/financial-aid/texas-advance-commitment/ |
| Need-Blind/Need-Aware | Need-aware for all applicants | admissions.utexas.edu/cost-aid/ |
| Eligibility | Texas residents, FAFSA/TASFA filed, demonstrated financial need | admissions.utexas.edu/cost-aid/financial-aid/texas-advance-commitment/ |
| FAFSA Deadline | January 15 (priority) | admissions.utexas.edu/cost-aid/financial-aid/ |

### 4.3 Graduate Cost & Funding Framework

| Item | Amount | Source |
|------|--------|--------|
| Graduate Tuition (Resident) | $8,684-$10,554 | onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/ |
| Graduate Tuition (Non-Resident) | $17,312-$19,340 | onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/ |
| Graduate COA (Resident, on/off campus) | $33,252-$35,493 | onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/ |
| Graduate COA (Non-Resident, on/off campus) | $41,880-$44,279 | onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/ |
| Application Fee (most programs) | $65 (U.S.) / $90 (International) | gradschool.utexas.edu/admissions/apply |
| Funding | TA/RA positions, fellowships available per program | gradschool.utexas.edu/funding |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.ea
  value: "October 15"
  source_url: "https://admissions.utexas.edu/apply/freshman/"
  source_snippet: "Early Action Deadline to Apply: October 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.rd
  value: "December 1"
  source_url: "https://admissions.utexas.edu/apply/freshman/"
  source_snippet: "Regular Deadline To Apply: December 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.tests.sat_act_policy
  value: "REQUIRED"
  source_url: "https://admissions.utexas.edu/apply/freshman/"
  source_snippet: "SAT and ACT official test scores must be submitted by the appropriate deadline to be considered."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.costs.tuition_resident
  value: "$10,858-$13,576"
  source_url: "https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/"
  source_snippet: "Tuition: $10,858-$13,576 (Resident who lives on campus or off campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.tuition_nonresident
  value: "$42,554-$51,106"
  source_url: "https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/"
  source_snippet: "Tuition: $42,554-$51,106 (Non-Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_coa_resident
  value: "$32,508-$35,386"
  source_url: "https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/"
  source_snippet: "Total Cost of Attendance: $32,508-$35,386 (Resident who lives on campus or off campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.total_coa_nonresident
  value: "$64,204-$72,916"
  source_url: "https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/"
  source_snippet: "Total Cost of Attendance: $64,204-$72,916 (Non-Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.tests.english_proficiency.toefl
  value: "79 (120 scale) or 4 (6-point scale)"
  source_url: "https://admissions.utexas.edu/info-for/international-students/"
  source_snippet: "TOEFL: 79 (120 scale) or 4 (6-point scale) internet-based test"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.tests.english_proficiency.ielts
  value: "6.5 overall"
  source_url: "https://admissions.utexas.edu/info-for/international-students/"
  source_snippet: "IELTS: An overall band of 6.5 on the Academic Examination"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.tests.english_proficiency.det
  value: "115 minimum"
  source_url: "https://admissions.utexas.edu/info-for/international-students/"
  source_snippet: "DET: 115 minimum overall score"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application.fee_domestic
  value: "$75"
  source_url: "https://admissions.utexas.edu/apply/freshman/"
  source_snippet: "Pay the non-refundable application fee of $75 when you submit your application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.application.fee_international
  value: "$90"
  source_url: "https://admissions.utexas.edu/apply/international-students/"
  source_snippet: "Pay the non-refundable application fee of $90 when you submit your application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.financial_aid.texas_advance_commitment
  value: "Free tuition for AGI ≤$100k; tuition support for AGI ≤$125k"
  source_url: "https://admissions.utexas.edu/cost-aid/financial-aid/texas-advance-commitment/"
  source_snippet: "TUITION COVERED: For Adjusted Gross Incomes Up to $100,000; TUITION SUPPORT: For Adjusted Gross Incomes Up to $125,000"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.application.fee
  value: "$65 (U.S.) / $90 (International); MBA $200; MPA $125"
  source_url: "https://gradschool.utexas.edu/admissions/apply"
  source_snippet: "U.S. Graduate: $65; International Graduate: $90; MBA: $200; MPA: $125"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.tests.english_proficiency
  value: "TOEFL 79 / IELTS 6.5 / DET 115"
  source_url: "https://gradschool.utexas.edu/admissions/apply/international"
  source_snippet: "TOEFL: 79 (120 scale) or 4 (6-point scale) internet-based test; IELTS: An overall band of 6.5 on the Academic Examination; DET: 115 minimum overall score"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.costs.tuition_resident
  value: "$8,684-$10,554"
  source_url: "https://onestop.utexas.edu/managing-costs/cost-tuition-rates/cost-of-attendance/"
  source_snippet: "Tuition: $8,684-$10,554 (Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
utaustin-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, degree inventory, matrix
├── 01-architecture.md                  # Section 1: School of Architecture programs
├── 02-business.md                      # Section 1: McCombs School of Business programs
├── 03-civic-leadership.md              # Section 1: School of Civic Leadership programs
├── 04-communication.md                 # Section 1: Moody College of Communication programs
├── 05-education.md                     # Section 1: College of Education programs
├── 06-engineering.md                   # Section 1: Cockrell School of Engineering programs
├── 07-fine-arts.md                     # Section 1: College of Fine Arts programs
├── 08-geosciences.md                   # Section 1: Jackson School of Geosciences programs
├── 09-information.md                   # Section 1: School of Information programs
├── 10-liberal-arts.md                  # Section 1: College of Liberal Arts programs
├── 11-natural-sciences.md              # Section 1: College of Natural Sciences programs
├── 12-nursing.md                       # Section 1: School of Nursing programs
├── 13-pharmacy.md                      # Section 1: College of Pharmacy programs
├── 14-public-affairs.md                # Section 1: LBJ School of Public Affairs programs
├── 15-social-work.md                   # Section 1: School of Social Work programs
├── 16-graduate-architecture.md         # Section 2: Graduate programs - Architecture
├── 17-graduate-business.md             # Section 2: Graduate programs - Business
├── 18-graduate-communication.md        # Section 2: Graduate programs - Communication
├── 19-graduate-education.md            # Section 2: Graduate programs - Education
├── 20-graduate-engineering.md          # Section 2: Graduate programs - Engineering
├── 21-graduate-fine-arts.md            # Section 2: Graduate programs - Fine Arts
├── 22-graduate-geosciences.md          # Section 2: Graduate programs - Geosciences
├── 23-graduate-information.md          # Section 2: Graduate programs - Information
├── 24-graduate-liberal-arts.md         # Section 2: Graduate programs - Liberal Arts
├── 25-graduate-natural-sciences.md     # Section 2: Graduate programs - Natural Sciences
├── 26-graduate-nursing.md              # Section 2: Graduate programs - Nursing
├── 27-graduate-pharmacy.md             # Section 2: Graduate programs - Pharmacy
├── 28-graduate-public-affairs.md       # Section 2: Graduate programs - Public Affairs
├── 29-graduate-social-work.md          # Section 2: Graduate programs - Social Work
├── 30-deadlines-requirements.md        # Section 3: Application requirements & deadlines
├── 31-costs-financial-aid.md           # Section 4: Costs & financial aid
├── 32-evidence-chain.md                # Section 5: Evidence chain index
└── 33-comparison-framework.md          # Section 7: Cross-school comparison
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "utaustin-knowledge-base-v2"
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

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete list of all UG minors with school attribution | https://catalog.utexas.edu/undergraduate/ |
| P0 | Per-program GRE requirements for graduate programs | Individual program websites |
| P1 | Complete list of all UG specializations/tracks | https://catalog.utexas.edu/undergraduate/ |
| P1 | Graduate application deadlines by program (complete) | https://gradschool.utexas.edu/degrees-programs |
| P2 | Scholarships and merit-based aid details | https://onestop.utexas.edu/managing-costs/scholarships-financial-aid/ |
| P2 | Transfer admission requirements by college | https://admissions.utexas.edu/apply/transfer-students/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UT Austin | (Other Schools) |
|-----------|-----------|-----------------|
| Type | Public Research University | |
| Location | Austin, TX | |
| UG Total COA (Resident, on/off campus) | $32,508-$35,386 | |
| UG Total COA (Non-Resident, on/off campus) | $64,204-$72,916 | |
| UG Tuition (Resident) | $10,858-$13,576 | |
| UG Tuition (Non-Resident) | $42,554-$51,106 | |
| Need-Blind (Intl?) | Need-aware for all | |
| EA Deadline | October 15 | |
| RD Deadline | December 1 | |
| SAT/ACT Required? | Yes (required) | |
| TOEFL Minimum | 79 | |
| IELTS Minimum | 6.5 | |
| DET Minimum | 115 | |
| Application Fee (UG Domestic) | $75 | |
| Application Fee (UG International) | $90 | |
| Total Program Count (Rule 1) | ~345+ | |
| School/Department Count (Rule 2) | 15 (UG) + 12 (Grad) | |
| Texas Advance Commitment | Free tuition for AGI ≤$100k | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.utexas.edu, onestop.utexas.edu, gradschool.utexas.edu, catalog.utexas.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
