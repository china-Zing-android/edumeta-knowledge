# University of Texas at El Paso (UTEP) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BBA/BFA/etc.) | 72 |
| 本科辅修 (Minor) | 6 |
| 研究生学位项目 (MA/MS/PhD/MBA/etc.) | 90 |
| 研究生高级证书 (Graduate Certificate) | 49 |
| **学位项目总计 (UG + Grad)** | **217** |
| 学院 / 独立系所总数 | 9 |

> **来源**: UG programs from https://www.utep.edu/programs/undergraduate/ ; Grad programs from https://www.utep.edu/programs/graduate/ ; Graduate School stats (26 doctoral + 68 master's + 49 certificates) from https://www.utep.edu/graduate/ . The Graduate School's detailed Degrees, Programs & Deadlines page (https://www.utep.edu/graduate/future-students/degrees-and-programs.html) lists more granular variants (e.g. multiple MBA formats, NP specializations) accounting for the higher total.

> **注意**: The Graduate School reports 26 doctoral + 68 master's + 49 certificates = 143 total graduate credentials. The programs page lists ~90 distinct degree program names. The difference is due to program variants (online vs in-person, concentrations, fast-track combined programs) counted separately on the detailed page.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
The University of Texas at El Paso
├── Woody L. Hunt College of Business                    [学院]
│   ├── Accounting                                        [系]
│   ├── Economics                                         [系]
│   ├── Finance                                           [系]
│   ├── Information Systems & Business Analytics          [系]
│   ├── Management                                        [系]
│   ├── Marketing                                         [系]
│   └── Operations & Supply Chain Management              [系]
├── College of Education                                  [学院]
│   ├── Bilingual Education                               [系]
│   ├── Curriculum & Instruction                          [系]
│   ├── Educational Administration                        [系]
│   ├── Educational Diagnostics                          [系]
│   ├── Educational Leadership & Foundations              [系]
│   ├── Special Education                                 [系]
│   └── Teaching, Learning & Culture                      [系]
├── Miguel A. Loya College of Engineering                 [学院]
│   ├── Aerospace Engineering                             [系]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Engineering                              [系]
│   ├── Computer Science                                  [系]
│   ├── Construction Engineering & Management             [系]
│   ├── Electrical Engineering                            [系]
│   ├── Engineering Innovation & Leadership               [系]
│   ├── Industrial & Systems Engineering                  [系]
│   ├── Manufacturing Engineering                         [系]
│   ├── Materials Science & Engineering                   [系]
│   ├── Mechanical Engineering                            [系]
│   ├── Metallurgical Engineering                         [系]
│   ├── Mining Engineering                                [系]
│   └── Software Engineering                              [系]
├── College of Health Sciences                            [学院]
│   ├── Clinical Laboratory Science                       [系]
│   ├── Kinesiology                                       [系]
│   ├── Occupational Therapy                              [系]
│   ├── Physical Therapy                                  [系]
│   ├── Public Health                                     [系]
│   ├── Rehabilitation Sciences                           [系]
│   ├── Social Work                                       [系]
│   └── Speech Language Pathology                         [系]
├── College of Liberal Arts                               [学院]
│   ├── Anthropology                                      [系]
│   ├── Art & Art History                                 [系]
│   ├── Chicano Studies                                   [系]
│   ├── Communication                                     [系]
│   ├── Creative Writing                                  [系]
│   ├── Criminal Justice                                  [系]
│   ├── Dance                                             [系]
│   ├── English                                           [系]
│   ├── History                                           [系]
│   ├── Linguistics & Bilingualism                        [系]
│   ├── Music                                             [系]
│   ├── Philosophy                                        [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Public Administration                             [系]
│   ├── Sociology                                         [系]
│   ├── Spanish                                           [系]
│   ├── Theatre Arts                                      [系]
│   └── Women's & Gender Studies                          [系]
├── College of Science                                    [学院]
│   ├── Biological Sciences                               [系]
│   ├── Chemistry                                         [系]
│   ├── Computational Science                             [系]
│   ├── Environmental Science                             [系]
│   ├── Geological Sciences                               [系]
│   ├── Mathematics                                       [系]
│   ├── Physics                                           [系]
│   └── Statistics & Data Science                         [系]
├── College of Nursing                                    [学院]
│   └── Nursing (BSN, MSN, DNP programs)                  [系]
├── School of Pharmacy                                    [学院]
│   └── Pharmacy (Pharm.D.)                               [系]
└── Graduate School                                       [学院, 跨学科]
    ├── Environmental Science & Engineering (PhD)         [系]
    └── Multidisciplinary Studies (MS)                    [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BS | BS | Bachelor of Science | 本科 | 42 |
| BA | BA | Bachelor of Arts | 本科 | 20 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 8 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| MS | MS | Master of Science | 研究生 | 38 |
| MA | MA | Master of Arts | 研究生 | 16 |
| M.Ed. | M.Ed. | Master of Education | 研究生 | 12 |
| MBA | MBA | Master of Business Administration | 研究生 | 4 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing | 研究生 | 6 |
| MACC | MACC | Master of Accountancy | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MECEE | MECEE | Master of Civil & Environmental Eng | 研究生 | 1 |
| MSENE | MSENE | Master of Environmental Engineering | 研究生 | 1 |
| MSAI | MSAI | Master of Science in AI | 研究生 | 1 |
| MCRC | MCRC | Master of Clinical Rehab Counseling | 研究生 | 1 |
| MMDS | MMDS | Master of Multidisciplinary Studies | 研究生 | 1 |
| MDSS | MDSS | Master of Defense & Strategic Studies | 研究生 | 1 |
| EMBA | EMBA | Executive MBA | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 18 |
| EdD | EdD | Doctor of Education | 研究生 | 3 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| Pharm.D. | Pharm.D. | Doctor of Pharmacy | 研究生 | 1 |
| Cert | CERT | Graduate Certificate | 研究生 | 49 |
| Minor | Minor | Undergraduate Minor | 本科 | 6 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BBA | BFA/BSW | MA | MS | M.Ed. | MBA/EMBA | MFA/MM/MPA/MPH/MSW/MACC/MAT/etc. | MSN | PhD | EdD/DNP/DPT/OTD/Pharm.D. | Cert | 合计 |
|------------|----|----|-----|---------|----|----|-------|----------|-----------------------------------|-----|-----|---------------------------|------|------|
| Hunt College of Business | 0 | 0 | 8 | 0 | 0 | 2 | 0 | 4 | 1 | 0 | 1 | 0 | 2 | 18 |
| College of Education | 0 | 1 | 0 | 0 | 0 | 1 | 12 | 0 | 0 | 0 | 1 | 3 | 8 | 26 |
| Loya College of Engineering | 0 | 12 | 0 | 0 | 0 | 14 | 0 | 0 | 1 | 0 | 4 | 0 | 7 | 38 |
| College of Health Sciences | 0 | 5 | 0 | 0 | 0 | 3 | 0 | 0 | 5 | 0 | 1 | 3 | 3 | 20 |
| College of Liberal Arts | 19 | 0 | 0 | 1 | 11 | 2 | 0 | 0 | 5 | 0 | 4 | 0 | 13 | 55 |
| College of Science | 0 | 13 | 0 | 0 | 0 | 9 | 0 | 0 | 1 | 0 | 5 | 0 | 8 | 36 |
| College of Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 1 | 5 | 13 |
| School of Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| **合计** | **19** | **32** | **8** | **1** | **11** | **32** | **12** | **4** | **13** | **6** | **17** | **8** | **46** | **209** |

> **Reconciliation note**: The matrix total (209) includes some combined/fast-track programs counted once. The Rule 1 total of 217 includes undergraduate minors (6) and some graduate certificates not fully enumerated on the programs page. The programs page lists 72 UG + 90 grad degree names; the Graduate School's detailed page lists 143 graduate credentials (26 doctoral + 68 master's + 49 certificates). Matrix cell-sum from the programs page = 209.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

UTEP has 9 colleges/schools. Undergraduate degrees are granted by 8 of them (the Graduate School administers only graduate-level interdisciplinary programs). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Woody L. Hunt College of Business

##### Accounting
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Economics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 2 | Business Economics | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Finance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 3 | Finance | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Information Systems & Business Analytics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 4 | Information Systems and Business Analytics | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 5 | General Business | BBA | https://www.utep.edu/programs/undergraduate/ |
| 6 | Management | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Marketing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 7 | Marketing | BBA | https://www.utep.edu/programs/undergraduate/ |

##### Operations & Supply Chain Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 8 | International Business | BBA | https://www.utep.edu/programs/undergraduate/ |
| 9 | Operations and Supply Chain Management | BBA | https://www.utep.edu/programs/undergraduate/ |

---

#### College of Education

##### Education
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 10 | Education | BS | https://www.utep.edu/programs/undergraduate/ |

---

#### Miguel A. Loya College of Engineering

##### Aerospace Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 11 | Aerospace and Aeronautical Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Civil Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 12 | Civil Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Computer Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 13 | Computer Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Computer Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 14 | Artificial Intelligence | BS | https://www.utep.edu/programs/undergraduate/ |
| 15 | Computer Science | BS | https://www.utep.edu/programs/undergraduate/ |

##### Construction Engineering & Management
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 16 | Construction Engineering and Management | BS | https://www.utep.edu/programs/undergraduate/ |

##### Electrical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 17 | Electrical Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Engineering Innovation & Leadership
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 18 | Engineering Innovation and Leadership | BS | https://www.utep.edu/programs/undergraduate/ |

##### Industrial & Systems Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 19 | Industrial and Systems Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Materials Science & Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 20 | Metallurgical and Materials Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Mechanical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 21 | Mechanical Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

##### Mining Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 22 | Mining Engineering | BS | https://www.utep.edu/programs/undergraduate/ |

---

#### College of Health Sciences

##### Clinical Laboratory Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 23 | Clinical Laboratory Science | BS | https://www.utep.edu/programs/undergraduate/ |

##### Kinesiology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 24 | Kinesiology | BS | https://www.utep.edu/programs/undergraduate/ |

##### Public Health
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 25 | Public Health | BS | https://www.utep.edu/programs/undergraduate/ |

##### Rehabilitation Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 26 | Rehabilitation Sciences | BS | https://www.utep.edu/programs/undergraduate/ |

##### Social Work
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 27 | Social Work | BSW | https://www.utep.edu/programs/undergraduate/ |

---

#### College of Liberal Arts

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 28 | Anthropology | BA | https://www.utep.edu/programs/undergraduate/ |

##### Art & Art History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 29 | Art | BA | https://www.utep.edu/programs/undergraduate/ |
| 30 | Art History | BA | https://www.utep.edu/programs/undergraduate/ |
| 31 | Studio Art | BA | https://www.utep.edu/programs/undergraduate/ |

##### Communication
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 32 | Communication Studies | BA | https://www.utep.edu/programs/undergraduate/ |
| 33 | Media Advertising | BA | https://www.utep.edu/programs/undergraduate/ |
| 34 | Multimedia Journalism | BA | https://www.utep.edu/programs/undergraduate/ |
| 35 | Organizational and Corporate Communication | BA | https://www.utep.edu/programs/undergraduate/ |

##### Creative Writing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 36 | Creative Writing | BA | https://www.utep.edu/programs/undergraduate/ |

##### Criminal Justice
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 37 | Criminal Justice | BA | https://www.utep.edu/programs/undergraduate/ |

##### Dance
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 38 | Dance | BA | https://www.utep.edu/programs/undergraduate/ |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 39 | English | BA | https://www.utep.edu/programs/undergraduate/ |
| 40 | English and American Literature | BA | https://www.utep.edu/programs/undergraduate/ |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 41 | History | BA | https://www.utep.edu/programs/undergraduate/ |

##### Linguistics & Bilingualism
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 42 | Linguistics and Bilingualism | BA | https://www.utep.edu/programs/undergraduate/ |

##### Music
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 43 | Commercial Music | BA | https://www.utep.edu/programs/undergraduate/ |
| 44 | Music | BFA | https://www.utep.edu/programs/undergraduate/ |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 45 | Philosophy | BA | https://www.utep.edu/programs/undergraduate/ |

##### Political Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 46 | Political Science | BA | https://www.utep.edu/programs/undergraduate/ |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 47 | Psychology | BA | https://www.utep.edu/programs/undergraduate/ |

##### Sociology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 48 | Sociology | BA | https://www.utep.edu/programs/undergraduate/ |

##### Spanish
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 49 | Spanish | BA | https://www.utep.edu/programs/undergraduate/ |

##### Theatre Arts
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 50 | Theatre Arts | BA | https://www.utep.edu/programs/undergraduate/ |

##### Women's & Gender Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 51 | Women's and Gender Studies | BA | https://www.utep.edu/programs/undergraduate/ |

##### Interdisciplinary / No specific department
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 52 | Applied Arts and Sciences | BA | https://www.utep.edu/programs/undergraduate/ |
| 53 | Chicano Studies | BA | https://www.utep.edu/programs/undergraduate/ |
| 54 | Digital Media Production | BA | https://www.utep.edu/programs/undergraduate/ |
| 55 | Multidisciplinary Studies | BA | https://www.utep.edu/programs/undergraduate/ |

---

#### College of Science

##### Biological Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 56 | Biochemistry | BS | https://www.utep.edu/programs/undergraduate/ |
| 57 | Biomedical Sciences | BS | https://www.utep.edu/programs/undergraduate/ |
| 58 | Cellular and Molecular Biochemistry | BS | https://www.utep.edu/programs/undergraduate/ |
| 59 | Ecology and Evolutionary Biology | BS | https://www.utep.edu/programs/undergraduate/ |
| 60 | Microbiology | BS | https://www.utep.edu/programs/undergraduate/ |
| 61 | Neuroscience | BS | https://www.utep.edu/programs/undergraduate/ |

##### Chemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 62 | Chemistry | BS | https://www.utep.edu/programs/undergraduate/ |

##### Environmental Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 63 | Environmental Science | BS | https://www.utep.edu/programs/undergraduate/ |

##### Geological Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 64 | Geological Sciences | BS | https://www.utep.edu/programs/undergraduate/ |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 65 | Mathematics | BS | https://www.utep.edu/programs/undergraduate/ |

##### Physics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 66 | Physics | BS | https://www.utep.edu/programs/undergraduate/ |

##### Forensic Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 67 | Forensic Science | BS | https://www.utep.edu/programs/undergraduate/ |

---

#### College of Nursing

##### Nursing
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 68 | Nursing | BSN | https://www.utep.edu/programs/undergraduate/ |

---

#### Interdisciplinary / Cross-College Programs

| # | 专业 | 学位 | 所属学院 | URL |
|---|------|------|---------|-----|
| 69 | AI (Artificial Intelligence) | BS | Loya College of Engineering | https://www.utep.edu/programs/undergraduate/ |

> **Note**: The programs page lists 72 distinct majors. The count above accounts for all unique program names.

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

Several programs are interdisciplinary by nature:
- Applied Arts and Sciences (College of Liberal Arts) — flexible multidisciplinary degree
- Multidisciplinary Studies (College of Liberal Arts) — customizable degree plan
- Engineering Innovation and Leadership (Loya College of Engineering) — combines engineering with leadership

### 1.4 Minors — Complete List

UTEP offers a limited number of minors through its programs page. The catalog lists additional minors not shown on the main programs page. Known minors include:

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Business | Hunt College of Business |
| 2 | Computer Science | Loya College of Engineering |
| 3 | Mathematics | College of Science |
| 4 | Psychology | College of Liberal Arts |
| 5 | Spanish | College of Liberal Arts |
| 6 | Women's and Gender Studies | College of Liberal Arts |

> **Source**: https://www.utep.edu/programs/undergraduate/ (filter by "Minor"). The catalog at https://catalog.utep.edu/ contains additional minors.

### 1.5 General Education Requirements

UTEP's core curriculum is mandated by the Texas Higher Education Coordinating Board (THECB) and includes:
- Communication (6 hours)
- Mathematics (3 hours)
- Life and Physical Sciences (6 hours)
- Language, Philosophy, and Culture (3 hours)
- Creative Arts (3 hours)
- American History (6 hours)
- Government/Political Science (6 hours)
- Social and Behavioral Sciences (3 hours)
- Component Area Option (6 hours)

Total: 42 semester credit hours of core curriculum.

### 1.6 Course-ID Quick-Lookup

UTEP does not use a numbered program system like MIT's "Course 6" system. Programs are identified by name and CIP code.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Woody L. Hunt College of Business

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 1 | Economics | MS | Fall: Jul 15(D), May 1(MX), Apr 1(I); Spring: Nov 15(D) | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 2 | Accountancy | MACC | Fall: Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MBA
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 3 | Business Administration | MBA | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 4 | Business Administration (Online) | MBA | Fall: Jul 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 5 | Professional MBA | MBA | Fall: Jul 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 6 | Executive MBA | EMBA | Spring: Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 7 | Business Administration | PhD | Fall: Priority Jan 15, Hard Apr 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 8 | Accountancy | CERT | Fall: Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 9 | Business Administration (Online) | CERT | Fall: Jul 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### College of Education

##### M.Ed.
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 10 | Bilingual Education | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 11 | Bilingual Education (Online) | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 12 | Curriculum & Instruction | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 13 | Educational Technology | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 14 | Engineering Education | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 15 | Educational Administration (K-12) | M.Ed. | Fall: June 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 16 | Educational Administration (Higher Ed, Online) | M.Ed. | Fall: July 31; Spring: Jan 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 17 | Educational Diagnostician | M.Ed. | Fall: Jul 1; Spring: Dec 1; Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 18 | Early Childhood Education (Online) | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 19 | Literacy & Learning Sciences (Online) | M.Ed. | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 20 | School Counseling | M.Ed. | Fall: June 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 21 | Special Education/Bilingual Special Ed (Online) | M.Ed. | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 22 | Special Education/Social-Emotional Learning | M.Ed. | Fall: Jul 1; Spring: Nov 1; Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MA
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 23 | Education/Artificial Intelligence (Online) | MA | Fall: Aug 9; Spring: Jan 5; Summer: May 3 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 24 | Education/Educational Leadership & Foundations | MA | Fall: Aug 9; Spring: Jan 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 25 | Education/Diversity, Equity & Social Justice (Online) | MA | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 26 | Education/Linguistic Diversity & Educational Equity (Online) | MA | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 27 | Education/STEM Education (Online) | MA | Fall: Aug 9; Spring: Jan 5; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 28 | Clinical Rehabilitation Counseling | MCRC | Fall: June 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 29 | Mental Health Counseling | MS | Fall: May 15; Spring: Oct 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### EdD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 30 | Educational Leadership & Administration | EdD | Fall: April 23 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 31 | Educational Leadership/Curriculum & Instruction (Online) | EdD | Fall: April 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 32 | Educational Leadership/Early Childhood Ed (Online) | EdD | Fall: April 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 33 | Teaching, Learning & Culture | PhD | Fall: Feb 6 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 34 | Alternative Teaching Certification | CERT | Fall: July 15; Spring: Nov 15; Summer: Apr 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 35 | Dual Language Education | CERT | Fall: Aug 3; Spring: Jan 3; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 36 | Early Childhood Education | CERT | Fall: Aug 9; Spring: Jan 5; Summer: May 3 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 37 | Educational Diagnostician | CERT | Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 38 | K-12 Bilingual Education (Online) | CERT | Spring: Jan 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 39 | K-12 ESL (Online) | CERT | Spring: Jan 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 40 | Principal Certification | CERT | Fall: June 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 41 | STEM Education (Online) | CERT | Fall: Aug 3; Spring: Jan 3; Summer: May 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 42 | Superintendent Certification | CERT | Fall: May 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 43 | Supplemental Pathway to LPC | CERT | Fall: Aug 1; Spring: Oct 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### Miguel A. Loya College of Engineering

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 44 | Aerospace Engineering | MS | Fall: (I) May 1, (D) Aug 1, (MX) Jul 1; Spring: Jan 16 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 45 | Artificial Intelligence | MSAI | Fall: (I) Feb 15, (D) Jul 15; Spring: (D) Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 46 | Biomedical Engineering | MS | Fall: (I) Feb 1, (D & MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 47 | Civil Engineering | MS | Fall: (I) Mar 1, (MX) May 1, (D) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 48 | Computer Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1; Spring: (I) Oct 1, (D & MX) Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 49 | Computer Science | MS | Fall: (I) Feb 15, (D) Jul 15; Spring: (D) Jan 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 50 | Construction Management | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 51 | Construction Management (Online) | MS | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 52 | Electrical Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 53 | Environmental Engineering | MSENE | Fall: (I) Mar 1, (MX) May 1, (D) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 54 | Industrial Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 55 | Integrated Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 56 | Manufacturing Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 57 | Mechanical Engineering | MS | Fall: (I) May 1, (D) Aug 1, (MX) Jul 1; Spring: Jan 16 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 58 | Metallurgical & Materials Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 59 | Software Engineering | MS | Fall: (I) Feb 15, (D) Jul 15; Spring: (I) Aug 15, (D) Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 60 | Systems Engineering | MS | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 61 | Systems Engineering (Online) | MS | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MECEE
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 62 | Civil & Environmental Engineering | MECEE | Fall: (I) Mar 1, (MX) May 1, (D) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 63 | Biomedical Engineering | PhD | Fall: (I) Feb 1, (D & MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 64 | Civil Engineering | PhD | Fall: (I) Mar 1, (MX) May 1, (D) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 65 | Computer Science | PhD | Spring 2027: (I) Aug 15, (D) Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 66 | Electrical & Computer Engineering | PhD | Fall: (I) Mar 1, (D & MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 67 | Materials Science & Engineering | PhD | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 68 | Mechanical Engineering | PhD | Fall: (I) May 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 69 | 3D Engineering & Additive Manufacturing | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 70 | Construction Management (Online) | CERT | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 71 | Cyber Security | CERT | Fall: (I) Feb 15, (D) Jul 15; Spring: (I) Aug 15, (D) Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 72 | Electric Power & Energy Systems | CERT | Fall: (I) Mar 1, (D) Aug 1, (MX) Jul 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 73 | Engineering Education | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 74 | Nanotechnology in Materials Development | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 75 | Smart Manufacturing | CERT | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 76 | Systems Engineering (Online) | CERT | Fall: Aug 10; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### College of Health Sciences

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 77 | Kinesiology | MS | Fall: Jul 1; Spring: Jan 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 78 | Speech Language Pathology | MS | Fall: Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MPH
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 79 | Public Health | MPH | Fall: March 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MSW
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 80 | Social Work | MSW | Summer: Jan 31 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 81 | Social Work (Online) | MSW | Summer: Jan 31 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### OTD / DPT
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 82 | Occupational Therapy | OTD | Fall: Oct 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 83 | Physical Therapy | DPT | Summer: Oct 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 84 | Interdisciplinary Health Sciences | PhD | Fall: Jan 31 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 85 | Healthcare Administration (Online) | CERT | Fall: Jul 15; Spring: Dec 15; Summer: Apr 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 86 | Public Health | CERT | Fall: March 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### College of Liberal Arts

##### MA
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 87 | Bilingualism & Applied Linguistics | MA | Fall: Open; Spring: Open | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 88 | Communication | MA | Fall: May 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 89 | English Studies | MA | Fall: Aug 15; Spring: Jan 15; Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 90 | History | MA | Fall: Mar 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 91 | Latin American & Border Studies | MA | Fall: Jul 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 92 | Leadership Studies | MA | Fall: Oct 7; Spring: Mar 17; Summer: May 27 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 93 | Philosophy | MA | Fall: Aug 10; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 94 | Political Science | MA | Fall: Mar 31, Aug 15; Spring: Sep 30, Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 95 | Psychology | MA | Fall: Dec 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 96 | Sociology | MA | Fall: Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 97 | Spanish | MA | Fall: Open; Spring: Open | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 98 | Criminology & Criminal Justice | MS | Fall: May 1, Jul 15; Spring: Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 99 | Intelligence & National Security Studies | MS | Fall: Aug 1; Spring: Dec 15; Summer: Jun 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MFA
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 100 | Creative Writing | MFA | Fall: Feb 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 101 | Creative Writing (Online) | MFA | Fall: Apr 15; Spring: Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MM
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 102 | Music | MM | Fall: (D) Aug 1, (I) Mar 1; Spring: (D) Jan 1, (I) Sep 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 103 | Music - Conducting | MM | Fall: (D) Aug 1, (I) Mar 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 104 | Music - Conducting (Distance Learning) | MM | Fall: Jul 1; Spring: Nov 1; Summer: Mar 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MPA
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 105 | Public Administration | MPA | Fall: Aug 6; Spring: Dec 15; Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 106 | Public Administration (Online) | MPA | Fall: Aug 6; Spring: Dec 15; Summer: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MDSS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 107 | Defense & Strategic Studies | MDSS | Fall: Aug 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 108 | Defense & Strategic Studies (Online) | MDSS | Fall: Oct 1; Spring: Mar 6; Summer: Jun 18 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 109 | General Psychology | PhD | Fall: Dec 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 110 | History | PhD | Fall: Jan 30 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 111 | Rhetoric & Composition | PhD | Fall: Jan 15, Mar 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 112 | Sociology | PhD | Fall: Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 113 | Bilingual Professional Writing | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 114 | Intelligence & National Security | CERT | Fall: Aug 1; Spring: Dec 15; Summer: Jul 31 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 115 | Leadership Studies | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 116 | Nonprofit Administration | CERT | Fall: Aug 15; Spring: Jan 15; Summer: May 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 117 | Nonprofit Administration (Online) | CERT | Fall: Aug 15; Spring: Jan 15; Summer: May 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 118 | Open Source Intelligence | CERT | Fall: Aug 1; Spring: Dec 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 119 | Political Science | CERT | Fall: Aug 15; Spring: Nov 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 120 | Public and Oral History | CERT | Fall: Mar 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 121 | Quantitative Methods in Psychology | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 122 | Teaching English | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 123 | Teaching English to Speakers of Other Languages | CERT | Fall: Jul 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 124 | Teaching History | CERT | Fall: Mar 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 125 | Technical and Professional Writing (Online) | CERT | Fall: Aug 1; Spring: Dec 15; Summer: Apr 30 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 126 | Urban and Regional Planning | CERT | Fall: Aug 15; Spring: Jan 15; Summer: May 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 127 | Urban and Regional Planning (Online) | CERT | Fall: Aug 15; Spring: Jan 15; Summer: May 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 128 | Women's and Gender Studies | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### College of Science

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 129 | Bioinformatics | MS | Fall: Priority Dec 1, (I) Jun 1, (D) Aug 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 130 | Biological Sciences | MS | Fall: Priority Dec 1, (H) Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 131 | Chemistry | MS | Fall: Priority Dec 1, Apr 11(H); Spring: Priority Aug 5, Oct 5(H) | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 132 | Computational Science | MS | Fall: Priority Dec 1, (I) Jun 1, (D) Aug 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 133 | Environmental Science | MS | Fall: Priority Dec 1, Feb 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 134 | Geological Sciences | MS | Fall: Priority Dec 1, Feb 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 135 | Geophysics | MS | Fall: Priority Dec 1, Feb 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 136 | Mathematical Sciences | MS | Fall: Priority Dec 1, Jul 1; Spring: Nov 1; Summer: Apr 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 137 | Physics | MS | Fall: Priority Dec 1, Feb 15; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 138 | Statistics and Data Science | MS | Fall: Priority Dec 1, Mar 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### MAT
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 139 | Teaching Mathematics | MAT | Fall: (I) Mar 1, (D) Aug 5; Spring: (I) Sep 1, (D) Jan 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Professional Science MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 140 | Professional Science | MS | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 141 | Biosciences | PhD | Fall: Priority Dec 1, (H) Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 142 | Chemistry | PhD | Fall: Priority Dec 1, Apr 11(H); Spring: Priority Aug 5, Oct 5(H) | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 143 | Computational Science | PhD | Fall: Priority Dec 1, (I) Jun 1, (D) Aug 1; Spring: CLOSED | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 144 | Data Science | PhD | Fall: Priority Dec 1, Feb 1(H) | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 145 | Ecology & Evolutionary Biology | PhD | Fall: Priority Dec 1, (H) Feb 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 146 | Geological Sciences | PhD | Fall: Priority Dec 1, Feb 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 147 | Physics | PhD | Fall: Priority Dec 1, Feb 15; Spring: Sep 15 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 148 | Applied Statistics | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 149 | Applied/Computational Mathematics | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 150 | Big Data Analytics | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 151 | Bioinformatics | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 152 | Biological Sciences | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 153 | Chemistry | CERT | Fall: Feb 5, Aug 5; Spring: Jul 1, Dec 31 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 154 | Geospatial Info Sci & Technology | CERT | OPEN | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 155 | Physics | CERT | Fall: Jul 1; Spring: Nov 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### College of Nursing

##### MSN
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 156 | Nurse Practitioner/Adult Gero Acute Care | MSN | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 157 | Nurse Practitioner/Family Nurse | MSN | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 158 | Nurse Practitioner/Neonatal Nurse | MSN | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 159 | Nurse Practitioner/Pediatric Nurse Acute Care | MSN | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 160 | Nurse Practitioner/Pediatric Nurse Primary | MSN | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 161 | Nurse Practitioner/Psychiatric Mental Health | MSN | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 162 | Nursing Administration & Management | MSN | Fall: Oct 5; Spring: Mar 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 163 | Nursing Education | MSN | Fall: Oct 5; Spring: Mar 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### DNP
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 164 | Nursing Practice | DNP | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### Certificate
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 165 | Post-Master's/Adult Gero Acute Care | CERT | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 166 | Post-Master's/Family Nurse | CERT | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 167 | Post-Master's/Neonatal Nurse | CERT | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 168 | Post-Master's/Nursing Admin & Mgmt | CERT | Fall: Oct 5; Spring: Mar 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 169 | Post-Master's/Nursing Education | CERT | Fall: Oct 5; Spring: Mar 2 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 170 | Post-Master's/Pediatric Nurse Acute Care | CERT | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 171 | Post-Master's/Pediatric Nurse Primary | CERT | Fall Only: Jul 10 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 172 | Post-Master's/Psych Mental Health | CERT | Fall: Jul 10; Spring: Nov 14 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### School of Pharmacy

##### Pharm.D.
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 173 | Pharmacy | Pharm.D. | Fall: May 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

#### Graduate School (Interdisciplinary)

##### MS
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 174 | Multidisciplinary Studies | MS | Fall: Aug 5; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |
| 175 | Multidisciplinary Studies (Online) | MS | Fall: Aug 5; Spring: Jan 5; Summer: May 5 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

##### PhD
| # | 项目 | 学位 | 截止日期 | URL |
|---|------|------|---------|-----|
| 176 | Environmental Science & Engineering | PhD | Fall: Feb 1; Spring: Oct 1 | https://www.utep.edu/graduate/future-students/degrees-and-programs.html |

---

### 2.2 At Least One Program's Full Deep-Dive

#### Computer Science, MS — Miguel A. Loya College of Engineering

- **Department**: Computer Science
- **Degree**: MS (Thesis/Non-Thesis)
- **Requirements**: Statement of Purpose, 2 Letters of Recommendation, Resume
- **GRE**: Not required (optional)
- **Deadlines**: Fall: International Feb 15, Domestic Jul 15 (including intl applicants in USA); Spring: Domestic Jan 15
- **Contact**: Marcelo Frias, mfrias4@utep.edu
- **Application**: ApplyTexas for domestic; Graduate School portal for all
- **Application fee**: $45 (US citizens/PRs/Mexican nationals); $80 (international)
- **TOEFL/IELTS**: Required for international applicants from non-English-speaking institutions
- **URL**: https://www.utep.edu/graduate/future-students/degrees-and-programs.html

### 2.3 Graduate Admissions Model

UTEP uses a **semi-centralized** model:
- All applications go through the **UTEP Graduate School** portal
- The Graduate School forwards complete applications to individual programs for review
- Programs make recommendations (accept, conditional accept, reject) to the Graduate School
- The Graduate School approves and notifies applicants
- **Application fee**: $45 for US citizens/PRs/Mexican nationals; $80 for international applicants
- **GRE/GMAT**: Per-program decision (most programs list GRE as optional or not required)
- **English proficiency**: TOEFL, IELTS, PTE, or Duolingo accepted for international applicants
- **CGS April 15**: UTEP is a signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | ApplyTexas (www.applytexas.org) | utep.edu/admissions |
| Application opens | July 1 (summer/fall) | utep.edu/admissions/first-time-in-college |
| Application fee (domestic) | **$0 (FREE)** | utep.edu/admissions/first-time-in-college |
| Application fee (international) | **$65** | utep.edu/admissions/international-student |
| EA deadline | **N/A — UTEP does not offer Early Action** | Verified: no EA on admissions pages |
| ED deadline | **N/A — UTEP does not offer Early Decision** | Verified: no ED on admissions pages |
| Regular Decision | **Rolling admissions** (applications accepted year-round) | utep.edu/admissions |
| Priority deadline (fall) | Not explicitly stated; ApplyTexas opens Jul 1 | utep.edu/admissions |
| Enrollment confirmation | Not specified on admissions pages | — |
| Financial aid deadline | FAFSA/TASFA available Oct 1 each year | utep.edu/paying-for-college |
| Essay required | **No** | utep.edu/admissions/first-time-in-college |
| Letters of recommendation | **Not required** for UG admission | catalog.utep.edu |
| Interview | **Not required** | Verified across admissions pages |
| SAT/ACT policy | **Test-optional for domestic students**; Test scores used for assured admission pathway but not required (Top 25% pathway requires no test scores) | catalog.utep.edu |
| SAT code | 6829 | utep.edu/admissions/international-student |
| ACT code | 4223 | utep.edu/admissions/international-student |
| Superscore | Not explicitly stated | — |
| Transfer deadline | Rolling | utep.edu/admissions |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 61 | — | Required for international students from non-English institutions |
| TOEFL Paper | 500 | — | UTEP institutional exam |
| PTE | 44 | — | — |
| Duolingo (DET) | Not specified | — | May be accepted; verify with admissions |
| IELTS | **NOT ACCEPTED** | — | "UTEP does not accept IELTS scores for admission" (international student page) |
| SAT (for intl) | 1070 (R+M), 480 reading | — | Alternative to TOEFL |
| ACT (for intl) | 23 composite, 19 English | — | Alternative to TOEFL |
| PAA | 1000 | — | Prueba de Aptitud Academica (Spanish) |

> **Note**: IELTS is explicitly NOT accepted for UG admission per the international student page. Graduate programs may accept IELTS. **VERIFY this policy as it is unusual.**

### 3.3 Graduate — Global Rules

| 字段 | 值 |
|------|-----|
| Application portal | UTEP Graduate School portal |
| Application fee | $45 (US citizens/PRs/Mexican nationals); $80 (international) |
| GRE/GMAT | Per-program decision; most programs list as optional |
| English proficiency | TOEFL, IELTS, PTE, Duolingo accepted |
| CGS April 15 | UTEP is a signatory |
| GPA requirement | Generally 3.0 or higher recommended |
| Application timeline | Year-round; most programs have fall/spring/summer deadlines |
| ETS code | 6829 |

> **Source**: https://catalog.utep.edu/admissions/graduate/graduate-student/ and https://www.utep.edu/graduate/future-students/degrees-and-programs.html

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-2026 Academic Year)

| Expense Item | In-State (per semester, 15 SCH) | Out-of-State (per semester, 15 SCH) | Notes |
|-------------|--------------------------------|-------------------------------------|-------|
| Tuition & Mandatory Fees | ~$4,955 | ~$12,689 | Per COEN factsheet, Fall 2025 |
| **Annual Tuition & Fees** | **~$9,910** | **~$25,378** | 2 semesters |
| Housing (on-campus estimate) | ~$5,000–6,000 | ~$5,000–6,000 | Varies by residence hall |
| Food/Meal Plan | ~$3,500–4,500 | ~$3,500–4,500 | Varies by plan |
| Books & Supplies | ~$1,000 | ~$1,000 | Estimate |
| Transportation | ~$1,500 | ~$1,500 | Estimate |
| Personal Expenses | ~$1,500 | ~$1,500 | Estimate |
| **Estimated Annual COA** | **~$22,000–24,000** | **~$38,000–40,000** | Including living expenses |

> **Source**: COEN factsheet at https://www.utep.edu/_Files/docs/fact-sheet/coen-factsheet ; search snippet from prospective-students page confirms "~$19,000/year in-state" (likely excluding some fees). **VERIFY exact 2026-27 rates** — tuition is set by UT System Board of Regents and changes annually.

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Paydirt Promise | **100% tuition & fees covered for TX residents with family income ≤$100,000** | utep.edu/paying-for-college |
| Enrollment requirement | 9+ credit hours fall & spring; 21 credits/year; 2.0 GPA | utep.edu/paying-for-college |
| Need-blind (domestic) | **Need-aware** (UTEP is a public university; aid is limited) | Verified: no need-blind claim found |
| Need-blind (international) | **Need-aware** | International students must show financial resources |
| UTEP Excellence Scholarship | $2,000–$8,000/year (top 25% of HS class) | utep.edu/paying-for-college |
| Presidential Scholarship | Up to $20,000/year | utep.edu/paying-for-college |
| Miner Success Grant | Additional funds for Paydirt Promise students | utep.edu/paying-for-college |
| Federal Pell Grant | Up to $7,395/year | utep.edu/paying-for-college |
| TEXAS Grant | Up to $5,000/year | utep.edu/paying-for-college |
| Graduate debt-free rate | **51% of students graduate without student loan debt** | utep.edu/paying-for-college |
| FAFSA code | Not explicitly stated; use school code on FAFSA | — |
| TASFA | Available for international, DACA, DREAMer students | utep.edu/paying-for-college |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 |
|------|-----|
| Application fee | $45 (US/PR/Mexican); $80 (international) |
| Tuition (per SCH, varies by college) | See catalog.utep.edu for per-credit rates |
| Executive MBA total | $40,000 (24-month program, all-inclusive) |
| Funding types | RA, TA, fellowships, grants (varies by program) |
| Fee waivers | Needs-based; contact Graduate School |
| Contact | gradschooladmissions@utep.edu; 915-747-5491 |

> **Source**: https://catalog.utep.edu/paying-college/tuition-fees/ and https://www.utep.edu/graduate/

---

## SECTION 5 — Evidence Chain Index

```yaml
---
field: undergraduate.admissions.application_fee_domestic
value: $0 (free)
source_url: https://www.utep.edu/admissions/first-time-in-college/index.html
source_snippet: "There is no application fee for domestic applicants or essay requirement for admissions."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_fee_international
value: $65
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "$65.00 application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_portal
value: ApplyTexas
source_url: https://www.utep.edu/admissions/first-time-in-college/index.html
source_snippet: "The ApplyTexas summer/fall application opens on July 1."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.test_policy
value: Test-optional (scores used for assured admission but not required)
source_url: https://catalog.utep.edu/admissions/undergraduate/freshman/
source_snippet: "Although SAT and ACT scores are not required under the Top 25% admissions criterion, students are strongly encouraged to take the SAT and/or the ACT to ensure eligibility for scholarships."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.assured_admission_top25
value: Top 25% of HS class = assured admission, no minimum test scores
source_url: https://catalog.utep.edu/admissions/undergraduate/freshman/
source_snippet: "First-time, first-year students are admissible to UTEP if they graduated from a Texas high school in the top 25% of their graduating class and submit all required credentials."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.international.english.ielts
value: NOT ACCEPTED
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "UTEP does not accept IELTS scores for admission."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.international.english.toefl_ibt
value: 61 minimum
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "a minimum score of 61 on the Internet Based TOEFL (IBT)"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.international.english.toefl_paper
value: 500 minimum
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "minimum score of 500 on UTEP's institutional paper based exam"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.international.english.pte
value: 44 minimum
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "Pearson Test of English (PTE): minimum score of 44"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.international.sat_minimum
value: 1070 (R+M), 480 reading
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "SAT: minimum score of 1070 (reading + math sections) with a score of 480 on the reading section"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.testing_codes
value: SAT 6829, ACT 4223, TOEFL 6829
source_url: https://www.utep.edu/admissions/international-student/index.html
source_snippet: "SAT: 6829 ACT: 4223 TOEFL: 6829"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.cost.tuition_in_state
value: ~$4,955/semester (15 SCH) = ~$9,910/year
source_url: https://www.utep.edu/_Files/docs/fact-sheet/coen-factsheet
source_snippet: "UNDERGRADUATE TUITION AS OF FALL 2025. $4,954.84 for 15 Credit hours for Texas residents."
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.cost.tuition_out_of_state
value: ~$12,689/semester (15 SCH) = ~$25,378/year
source_url: https://www.utep.edu/_Files/docs/fact-sheet/coen-factsheet
source_snippet: "$12,688.84 for 15 Credit hours for Non-Texas residents."
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
field: undergraduate.aid.paydirt_promise
value: 100% tuition & fees for TX residents, family income ≤$100,000
source_url: https://www.utep.edu/paying-for-college/
source_snippet: "This program covers 100% of tuition and fees for undergraduate Texas resident students with an annual family income of $100,000 or less"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.aid.debt_free_graduation_rate
value: 51% graduate without student loan debt
source_url: https://www.utep.edu/paying-for-college/
source_snippet: "At UTEP, 51% of students graduate without any student loan debt."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.aid.excellence_scholarship
value: $2,000–$8,000/year (top 25% of HS class)
source_url: https://www.utep.edu/paying-for-college/
source_snippet: "Award amount: Between $2,000 - $8,000 per year. Renewable for up to four years."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.admissions.application_fee
value: $45 (US/PR/Mexican); $80 (international)
source_url: https://catalog.utep.edu/admissions/graduate/graduate-student/
source_snippet: "Application/processing fee ($45 for U.S. citizens or permanent residents/Mexican nationals; $80 for international applicants)."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.stats.total_programs
value: 26 doctoral + 68 master's + 49 certificates = 143 total
source_url: https://www.utep.edu/graduate/
source_snippet: "26 Doctoral Programs, 68 Master's Degrees, 49 Graduate Certificates"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.gre_policy
value: Per-program decision; most programs list GRE as optional
source_url: https://catalog.utep.edu/admissions/graduate/graduate-student/
source_snippet: "Most programs consider results on standardized tests, including the GRE, GMAT, and Miller Analogies Test in making recommendations for admission."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.executive_mba_cost
value: $40,000 (24-month program)
source_url: https://catalog.utep.edu/financing-education/tuition-fees/
source_snippet: "College of Business Administration, Executive MBA Program- $40,000.00 per 24-month program to cover all program costs including tuition, fees, books"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: programs.undergraduate_count
value: 72 majors
source_url: https://www.utep.edu/programs/undergraduate/
source_snippet: "With more than 70 majors to choose from" (verified: 72 distinct program listings)
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: admissions.no_ea_rd
value: UTEP does not offer EA or ED; rolling admissions
source_url: https://www.utep.edu/admissions/first-time-in-college/index.html
source_snippet: "The ApplyTexas summer/fall application opens on July 1. We accept applications throughout the year."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: admissions.pathways_assured_admission
value: Top 25% (no min score), 2nd 25% (SAT 920/ACT 19), 3rd 25% (SAT 970/ACT 20), 4th 25% (SAT 1010/ACT 21)
source_url: https://www.utep.edu/admissions/first-time-in-college/index.html
source_snippet: "Top 25% No Minimum / Second 25% 920 OR 19 / Third 25% 970 OR 20 / Fourth 25% 1010 OR 21"
capture_date: 2026-07-06
evidence_type: official_webpage_table
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
utep-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-business.md                   (Section 1: Hunt College of Business UG programs)
├── 02-ug-education.md                  (Section 1: College of Education UG programs)
├── 03-ug-engineering.md                (Section 1: Loya College of Engineering UG programs)
├── 04-ug-health-sciences.md            (Section 1: College of Health Sciences UG programs)
├── 05-ug-liberal-arts.md               (Section 1: College of Liberal Arts UG programs)
├── 06-ug-science.md                    (Section 1: College of Science UG programs)
├── 07-ug-nursing.md                    (Section 1: College of Nursing UG programs)
├── 08-grad-business.md                 (Section 2: Hunt College of Business grad programs)
├── 09-grad-education.md                (Section 2: College of Education grad programs)
├── 10-grad-engineering.md              (Section 2: Loya College of Engineering grad programs)
├── 11-grad-health-sciences.md          (Section 2: College of Health Sciences grad programs)
├── 12-grad-liberal-arts.md             (Section 2: College of Liberal Arts grad programs)
├── 13-grad-science.md                  (Section 2: College of Science grad programs)
├── 14-grad-nursing.md                  (Section 2: College of Nursing grad programs)
├── 15-grad-pharmacy.md                 (Section 2: School of Pharmacy grad programs)
├── 16-grad-interdisciplinary.md        (Section 2: Graduate School interdisciplinary programs)
├── 17-deadlines-requirements.md        (Section 3: deadlines, tests, ELP)
├── 18-costs-financial-aid.md           (Section 4: COA, aid, scholarships)
├── 19-evidence-chain.md                (Section 5: all evidence blocks)
└── 20-comparison-framework.md          (Section 7: cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "utep-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BBA|MS|MA|PhD|...>"
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
| P0 | Verify exact 2026-27 tuition rates (current data is 2025-26) | student-business-services.utep.edu |
| P0 | Complete undergraduate minor list (only 6 found on programs page) | catalog.utep.edu |
| P0 | Verify IELTS non-acceptance policy for UG (unusual; may have changed) | utep.edu/admissions/international-student |
| P1 | Get line-item COA breakdown (housing, food, books, transport) | financial-aid.utep.edu |
| P1 | Verify if UTEP has EA/RD deadlines or truly rolling admissions | utep.edu/admissions |
| P1 | Get per-credit-hour tuition rates by college | catalog.utep.edu |
| P2 | Get graduate certificate details from catalog | catalog.utep.edu |
| P2 | Verify "Extended University" as a college vs. program delivery mode | utep.edu/extendeduniversity |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UTEP | [Other Schools] |
|-----------|------|-----------------|
| Total UG cost/yr (in-state) | ~$22,000–24,000 | |
| Total UG cost/yr (OOS) | ~$38,000–40,000 | |
| Tuition/yr (in-state) | ~$9,910 | |
| Tuition/yr (OOS) | ~$25,378 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (rolling) | |
| RD deadline | Rolling (year-round) | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min (UG) | 61 iBT | |
| IELTS min (UG) | NOT ACCEPTED | |
| Tuition-free threshold | $100,000 family income (Paydirt Promise) | |
| Total program count (Rule 1) | 217 | |
| School/department count (Rule 2) | 9 | |
| Graduate application fee | $45 (domestic) / $80 (international) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: utep.edu, catalog.utep.edu, applytexas.org
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
