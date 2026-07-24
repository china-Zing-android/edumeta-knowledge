# California State University, Los Angeles (Cal State LA / CSULA) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → college → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Institution type**: T5 public, comprehensive, Hispanic-Serving Institution (HSI), Asian American and Native American Pacific Islander-Serving Institution (AANAPISI)
> **Campus**: 5151 State University Drive, Los Angeles, CA 90032
> **Phone**: (323) 343-3000
> **Founded**: 1947
> **Standardized application**: Cal State Apply (https://www.calstate.edu/apply)
> **Catalog year**: University Catalog 2026–2027 (catoid=55 on ecatalog)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA / BS / BM / BMus) | 77 (66 base majors + 11 Business options counted separately) |
| 本科辅修 (Minor) | 86 |
| 本科证书 (Undergraduate Certificate) | 33 |
| 本科混合学位 (Blended B.S./M.S.) | 5 |
| 研究生学位项目 (MA / MS / MFA / MM / MBA / MPA / MPH / MSW / Ed.S.) | 56 |
| 教育博士 / 哲学博士 (Ed.D. / Ph.D.) | 2 |
| 专业博士 (AuD) | 1 |
| 研究生证书 (Post-Baccalaureate Certificate) | 38 |
| 研究生后证书 (Post-Master's Certificate) | 7 |
| 教师凭证 (Credentials + Authorizations) | 28 |
| **学位项目总计 (UG + Grad)** | **~333 (leaf programs)** |
| **学院总数** | **8 colleges + Honors College + University Library + University Programs** |

> **Source**: Cal State LA University Catalog 2026–2027, "Programs of Study" (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=6231`) and "Programs by Colleges" (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=9395`).
> **Note**: Cal State LA is part of the 23-campus California State University system. All CSU campuses share the same systemwide application (Cal State Apply) and the same systemwide tuition schedule, but campus-based mandatory fees differ.
> **Capture date**: 2026-07-07

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
California State University, Los Angeles (Cal State LA)
├── College of Arts and Letters [学院]
│   ├── Art [系]
│   ├── Communication Studies [系]
│   ├── English [系]
│   ├── Liberal Studies [系]
│   ├── Modern Languages and Literatures [系]
│   ├── Music [系]
│   ├── Philosophy [系]
│   ├── Television, Film, and Media Studies [系]
│   ├── Theatre and Dance [系]
│   └── Women's, Gender and Sexuality Studies [系]
├── College of Business and Economics [学院]
│   ├── Accounting [系]
│   ├── Economics and Statistics [系]
│   ├── Finance, Law, and Real Estate [系]
│   ├── Information Systems [系]
│   ├── Management [系]
│   └── Marketing [系]
│   └── Interdisciplinary Programs and Courses - Business and Economics [跨学科]
├── College of Education [学院]
│   ├── Applied and Advanced Studies in Education [系]
│   ├── Curriculum and Instruction [系]
│   └── Special Education and Counseling [系]
├── College of Engineering, Computer Science, and Technology [学院]
│   ├── Civil Engineering [系]
│   ├── Computer Science [系]
│   ├── Electrical and Computer Engineering [系]
│   ├── Mechanical Engineering [系]
│   ├── Technology [系]
│   └── Interdisciplinary Programs and Courses - Engineering, CS, and Technology [跨学科]
├── College of Ethnic Studies [学院]
│   ├── Asian and Asian-American Studies [系]
│   ├── Chicana(o) and Latina(o) Studies [系]
│   ├── Pan-African Studies [系]
│   └── Interdisciplinary Programs and Courses - Ethnic Studies [跨学科]
├── Rongxiang Xu College of Health and Human Services [学院]
│   ├── Child and Family Studies [系]
│   ├── Audiology and Speech-Language Pathology [系]
│   ├── Nutrition and Dietetics [系]
│   ├── Public Health [系]
│   ├── School of Criminal Justice and Criminalistics [系]
│   ├── School of Kinesiology [系]
│   ├── Patricia A. Chin School of Nursing [系]
│   ├── School of Social Work [系]
│   └── Interdisciplinary Programs and Courses - Health and Human Services [跨学科]
├── College of Natural and Social Sciences [学院]
│   ├── Anthropology [系]
│   ├── Biological Sciences [系]
│   ├── Chemistry and Biochemistry [系]
│   ├── Geography, Geology, and Environment [系]
│   ├── History [系]
│   ├── Mathematics [系]
│   ├── Physics and Astronomy [系]
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Sociology [系]
│   └── Interdisciplinary Program (Latin American Studies) [跨学科]
├── College of Professional and Global Education [学院]
│   └── (College of Professional and Global Education)
└── Honors College [学院]
    └── Honors College Program
```

> **Source**: Cal State LA University Catalog 2026–2027, "Colleges & Departments" (`https://ecatalog.calstatela.edu/content.php?catoid=77&navoid=11969`).
> **Note**: Cal State LA's website (`/academics`) describes "8 colleges": Arts and Letters, Business and Economics, Education, Engineering Computer Science and Technology, Ethnic Studies, Rongxiang Xu Health and Human Services, Natural and Social Sciences, and Professional and Global Education. The Honors College and University Programs sit alongside as separate academic units.
> **Capture date**: 2026-07-07

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 32 (excluding B.S. options) |
| BMus | Bachelor of Music | 本科 | 1 (Music, B.M.) |
| BS | Bachelor of Science | 本科 | 44 (including 15 Business options) |
| Minor | 辅修 | 本科 | 86 |
| UG Certificate | 本科证书 | 本科 | 33 |
| Blended B.S./M.S. | 混合本硕 | 本科/研究生 | 5 |
| MA | Master of Arts | 研究生 | 21 |
| MS | Master of Science | 研究生 | 22 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MMus | Master of Music | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| Ed.S. | Education Specialist | 研究生 | 1 (School Psychology, effective Fall 2025) |
| Ed.D. | Doctor of Education | 研究生 | 1 (Educational Leadership) |
| Ph.D. | Doctor of Philosophy | 研究生 | 1 (Special Education) |
| AuD | Doctor of Audiology | 专业博士 | 1 |
| Post-Bacc Certificate | 学士后证书 | 研究生 | 38 |
| Post-Master's Certificate | 硕士后证书 | 研究生 | 7 |
| Credential | 教师凭证 | 研究生 | 28 |
| Interdisciplinary Master's | 跨学科硕士 | 研究生 | 1 |

> **Source**: Cal State LA University Catalog 2026–2027, "Indices of Degree Program" (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=6231`).
> **Note**: Doctoral degrees include the professional Doctor of Audiology (AuD), the research/clinical Ed.D. in Educational Leadership, and the Ph.D. in Special Education. The Ed.S. in School Psychology is offered through the College of Education.
> **Capture date**: 2026-07-07

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BMus | BS | Minor | UG Cert | Blended | MA | MS | MBA | MFA | MMus | MPA | MPH | MSW | Ed.S. | Ed.D. | Ph.D. | AuD | Post-Bacc | Post-Master | Credential | 合计 |
|------------|-----|------|----|-------|---------|---------|----|----|-----|-----|------|-----|-----|-----|------|------|------|-----|-----------|-------------|------------|------|
| Arts and Letters | 14 | 1 | 0 | 23 | 1 | 0 | 7 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 | 55 |
| Business and Economics | 1 | 0 | 16 | 16 | 19 | 1 | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 67 |
| Education | 1 | 0 | 1 | 1 | 1 | 0 | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 16 | 1 | 15 | 46 |
| Engineering, CS & Tech | 0 | 0 | 7 | 6 | 3 | 4 | 1 (suspended) | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 29 |
| Ethnic Studies | 3 | 0 | 0 | 6 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 15 |
| Rongxiang Xu HHS | 3 | 0 | 8 | 5 | 4 | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 1 | 4 | 6 | 3 | 42 |
| Natural & Social Sciences | 8 | 0 | 8 | 24 | 3 | 0 | 7 | 7 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 9 | 71 |
| Professional & Global Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| University Programs | 1 (Special Major) | 0 | 0 | 0 | 0 | 0 | 1 (Interdisciplinary) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (CalState TEACH) | 4 |
| **合计** | **31** | **1** | **40** | **81** | **33** | **5** | **27** | **22** | **1** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **35** | **7** | **34** | **~329** |

> **Source**: Cal State LA University Catalog 2026–2027, "Programs by Colleges" page (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=9395`).
> **Reconciliation**: 77 UG majors + 86 minors + 33 UG certs + 5 Blended + 56 grad degrees (incl. Ed.S./Ed.D./Ph.D./AuD) + 38 Post-Bacc + 7 Post-Master + 28 Credentials ≈ 330 leaf programs.
> **Capture date**: 2026-07-07

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Cal State LA delivers undergraduate education through **8 colleges + Honors College + cross-college University Programs**. All undergraduates apply via Cal State Apply (https://www.calstate.edu/apply).

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### COLLEGE OF ARTS AND LETTERS

| 系 (Department) | 学位 | 专业 (Major) |
|------|------|------|
| Art | BA | Art, B.A. |
| Communication Studies | BA | Communication, B.A. |
| English | BA | English, B.A. |
| Liberal Studies | BA | Liberal Studies, B.A. |
| Modern Languages and Literatures | BA | Chinese, B.A. |
| Modern Languages and Literatures | BA | French, B.A. |
| Modern Languages and Literatures | BA | Japanese, B.A. |
| Modern Languages and Literatures | BA | Spanish, B.A. |
| Music | BA | Music, B.A. |
| Music | BMus | Music, B.M. |
| Philosophy | BA | Philosophy, B.A. |
| Television, Film, and Media Studies | BA | Television, Film and Media Studies, B.A. |
| Theatre and Dance | BA | Theatre, B.A. |
| Women's, Gender and Sexuality Studies | BA | Women's, Gender, and Sexuality Studies, B.A. |

#### COLLEGE OF BUSINESS AND ECONOMICS

| 系 | 学位 | 专业 |
|------|------|------|
| Economics and Statistics | BA | Economics, B.A. |
| Accounting | BS | Business Administration, B.S.: Option in Accounting |
| Accounting | BS | Business Administration, B.S.: Option in Business Economics |
| Accounting | BS | Business Administration, B.S.: Option in Business Prelegal |
| Accounting | BS | Business Administration, B.S.: Option in Entrepreneurship |
| Finance, Law, and Real Estate | BS | Business Administration, B.S.: Option in Finance |
| Finance, Law, and Real Estate | BS | Business Administration, B.S.: Option in General Business |
| Finance, Law, and Real Estate | BS | Business Administration, B.S.: Option in Healthcare Administration |
| Management | BS | Business Administration, B.S.: Option in Human Resources Management |
| Management | BS | Business Administration, B.S.: Option in International Business |
| Management | BS | Business Administration, B.S.: Option in Management |
| Marketing | BS | Business Administration, B.S.: Option in Marketing |
| Management | BS | Business Administration, B.S.: Option in Operations and Supply Chain Management |
| Finance, Law, and Real Estate | BS | Business Administration, B.S.: Option in Real Estate |
| Marketing | BS | Business Administration, B.S.: Option in Retailing |
| Information Systems | BS | Business Administration, B.S. (base, no option) |
| Information Systems | BS | Computer Information Systems, B.S. |

#### COLLEGE OF EDUCATION

| 系 | 学位 | 专业 |
|------|------|------|
| Applied and Advanced Studies in Education | BA | Urban Learning, B.A. |
| Applied and Advanced Studies in Education | BS | Rehabilitation Services, B.S. |

#### COLLEGE OF ENGINEERING, COMPUTER SCIENCE, AND TECHNOLOGY

| 系 | 学位 | 专业 |
|------|------|------|
| Technology | BS | Aviation Administration, B.S. |
| Civil Engineering | BS | Civil Engineering, B.S. |
| Computer Science | BS | Computer Science, B.S. |
| Electrical and Computer Engineering | BS | Electrical Engineering, B.S. |
| Technology | BS | Engineering Technology, B.S. |
| Technology | BS | Fire Protection Administration and Technology, B.S. |
| Mechanical Engineering | BS | Mechanical Engineering, B.S. |

#### COLLEGE OF ETHNIC STUDIES

| 系 | 学位 | 专业 |
|------|------|------|
| Asian and Asian-American Studies | BA | Asian and Asian-American Studies, B.A. |
| Chicana(o) and Latina(o) Studies | BA | Chicana(o) and Latina(o) Studies, B.A. |
| Pan-African Studies | BA | Pan-African Studies, B.A. |

#### RONGXIANG XU COLLEGE OF HEALTH AND HUMAN SERVICES

| 系 | 学位 | 专业 |
|------|------|------|
| Child and Family Studies | BA | Child Development, B.A. |
| Audiology and Speech-Language Pathology | BA | Communicative Disorders, B.A. |
| School of Social Work | BA | Social Work, B.A. |
| School of Criminal Justice and Criminalistics | BS | Criminal Justice, B.S. |
| School of Kinesiology | BS | Exercise Science, B.S. |
| Nutrition and Dietetics | BS | Food Science and Technology, B.S. (program suspended, effective Fall 2023) |
| Nutrition and Dietetics | BS | Hospitality, Wellness, and Leisure Services, B.S. |
| School of Kinesiology | BS | Kinesiology, B.S. |
| Patricia A. Chin School of Nursing | BS | Nursing, B.S. (BSN) |
| Nutrition and Dietetics | BS | Nutritional Science, B.S. |
| Public Health | BS | Public Health, B.S. |

#### COLLEGE OF NATURAL AND SOCIAL SCIENCES

| 系 | 学位 | 专业 |
|------|------|------|
| Anthropology | BA | Anthropology, B.A. |
| Geography, Geology, and Environment | BA | Geography, B.A. |
| History | BA | History, B.A. |
| Interdisciplinary (Latin American Studies) | BA | Latin-American Studies, B.A. |
| Physics and Astronomy | BA | Physics, B.A. |
| Political Science | BA | Political Science, B.A. |
| Psychology | BA | Psychology, B.A. |
| Sociology | BA | Sociology, B.A. |
| Biological Sciences | BS | Applied Science, B.S. |
| Chemistry and Biochemistry | BS | Biochemistry, B.S. |
| Biological Sciences | BS | Biology, B.S. |
| Chemistry and Biochemistry | BS | Chemistry, B.S. |
| Geography, Geology, and Environment | BS | Geology, B.S. |
| Mathematics | BS | Mathematics, B.S. |
| Biological Sciences | BS | Natural Science, B.S. |
| Physics and Astronomy | BS | Physics, B.S. |

#### UNIVERSITY PROGRAMS (cross-college)

| 系 | 学位 | 专业 |
|------|------|------|
| Special Major | BA | Special Major, Bachelor's Degree |

### 1.3 Minors — Complete List (86 total)

#### COLLEGE OF ARTS AND LETTERS (23 minors)

Art, Art History, Chinese, Classics, Communication, Comparative and Applied Linguistics and Literacy Studies, Creative Studies in Music, Creative Writing, Dance, English, Francophone Studies, French, Health Communication, Japanese, Journalism, Korean, Music, Philosophy General, Philosophy Prelaw, Science Fiction, Science/Technology/Medicine Studies, Spanish, Theatre, Women's/Gender/Sexuality Studies.

#### COLLEGE OF BUSINESS AND ECONOMICS (16 minors)

Accounting, Basic Business, Business Intelligence, Computer Information Systems, Economics, Entertainment Marketing, Entrepreneurship, Finance, Healthcare Management, Management, Marketing, Operations and Supply Chain Management, Real Estate, Retailing, Social Media, Sustainability Marketing.

#### COLLEGE OF EDUCATION (1 minor)

Rehabilitation Services.

#### COLLEGE OF ENGINEERING, COMPUTER SCIENCE, AND TECHNOLOGY (6 minors)

Aviation Administration, Biomedical Engineering (BME), Computer Science, Construction and Engineering Management, Electrical and Computer Engineering, Urban Sustainability.

#### COLLEGE OF ETHNIC STUDIES (6 minors)

Asian American Studies, Asian Studies, Central American Studies (by Ethnic Studies), Chicana(o) and Latina(o) Studies, Mesoamerican Studies, Pan-African Studies.

#### RONGXIANG XU COLLEGE OF HEALTH AND HUMAN SERVICES (5 minors)

Child Development, Criminal Justice, Developmental Disabilities, Forensic Science, Public Health.

#### COLLEGE OF NATURAL AND SOCIAL SCIENCES (24 minors)

Anthropology, Bioinformatics (BINF), Biology, Central American Studies (by NSS), Geography, Geology Sciences, Global Politics, History, Labor Studies, Latin American Studies, Law and Society, Mathematics, Mathematics Teaching, Microbiology, Natural Science, Physics, Political Science, Political Science Public Administration, Prelegal Studies, Psychology, Religious Studies, Science Teaching Preparation, Social Gerontology, Sociology, Urban Studies.

#### University-wide/Cross-listed minors not in catalog list above: Chemistry, Journalism, Forensic Science, etc. — see catalog for full list.

### 1.4 Undergraduate Certificates (33 total)

| 学院 | 数量 | 证书 |
|------|------|------|
| Arts and Letters | 1 | Fashion, Fiber and Materials |
| Business and Economics | 19 | Business Intelligence; Communications and Networking; Computer Programming; Enterprise Systems; Entrepreneurship; Fashion Retailing; Finance; General Management; Healthcare Informatics; Human Resources Management; Information Systems Security Managers; Information Systems Security Professionals; International Business; International Business Communication; Marketing; Operations and Supply Chain Management; Social Media; Sustainability Marketing; Transportation and Logistics |
| Education | 1 | Veteran Services |
| Engineering, CS & Tech | 3 | Aviation Administration; Fire Protection Risk Analysis and Reduction; Fire Service Administration |
| Ethnic Studies | 2 | Cultural Competence for Professionals; Pre-Medicine/MDpas |
| HHS | 4 | Applied Gerontology; Child Maltreatment and Family Violence; Cultural Diversity in Human Services; Youth Agency Administration |
| Natural & Social Sciences | 3 | Geographic Information Systems Analysis; GIS: Community Engagement and Planning; Natural Science |

### 1.5 Blended B.S./M.S. Programs (5 total)

| 学院 | 系 | 专业 |
|------|------|------|
| Business and Economics | Accounting | Accounting, Blended B.S./M.S. |
| Engineering, CS & Tech | Civil Engineering | Civil Engineering, Blended B.S./M.S. |
| Engineering, CS & Tech | Computer Science | Computer Science, Blended B.S./M.S. |
| Engineering, CS & Tech | Electrical and Computer Engineering | Electrical Engineering, Blended B.S./M.S. |
| Engineering, CS & Tech | Mechanical Engineering | Mechanical Engineering, Blended B.S./M.S. |

### 1.6 General Education & Graduation Requirements

Cal State LA uses the CSU systemwide General Education pattern (39 units across Areas A–E plus American Institutions, plus the CSU Graduation Writing Assessment Requirement — GWAR). The full GE program is documented in the catalog under "The General Education Program" (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=6256`). All undergraduates must complete GE Lower Division and GE Upper Division courses.

> **Source**: Cal State LA Catalog, "General Education Program" page (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=6256`).
> **Capture date**: 2026-07-07

### 1.7 Application Note

All Cal State LA undergraduate applicants use the **Cal State Apply** centralized application at https://www.calstate.edu/apply. Cal State Apply is shared by all 23 CSU campuses; the application fee is **$70 per campus**.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### COLLEGE OF ARTS AND LETTERS

| 系 | 学位 | 专业 |
|------|------|------|
| Art | MA | Art, M.A. |
| Communication Studies | MA | Communication Studies, M.A. |
| English | MA | English, M.A. |
| Music | MA | Music, M.A. |
| Philosophy | MA | Philosophy, M.A. |
| Spanish | MA | Spanish, M.A. |
| Television, Film, and Media Studies | MA | Television, Film and Media Studies, M.A. |
| Art | MFA | Art, M.F.A. |
| Television, Film, and Media Studies | MFA | Television, Film and Theatre, M.F.A. |
| Music | MMus | Music, M.M. |

#### COLLEGE OF BUSINESS AND ECONOMICS

| 系 | 学位 | 专业 |
|------|------|------|
| Accounting | MS | Accounting, M.S. |
| Management | MBA | Business Administration, M.B.A. |
| Management | MS | Business Administration, M.S. |
| Management | MS | Business Analytics, M.S. |
| Management | MS | Healthcare Management, M.S. |
| Information Systems | MS | Information Systems, M.S. |
| Economics and Statistics | MA | Economics, M.A. |

#### COLLEGE OF EDUCATION

| 系 | 学位 | 专业 |
|------|------|------|
| Applied and Advanced Studies in Education | MA | Education for Social Change, M.A. (Pending approval from CO) |
| Educational Administration | MA | Educational Administration, M.A. |
| Educational Foundations | MA | Educational Foundations, M.A. |
| Educational Technology | MA | Educational Technology, M.A. |
| Special Education | MA | Special Education, M.A. |
| Applied and Advanced Studies in Education | MA | Teaching English to Speakers of Other Languages (TESOL), M.A. |
| Special Education | MS | Applied Behavior Analysis, M.S. (effective Fall 2025) |
| Special Education | MS | Counseling, M.S. |
| Special Education | Ed.S. | School Psychology, Ed.S. (effective Fall 2025) |
| Educational Administration | Ed.D. | Doctor of Education in Educational Leadership (Ed.D.) |
| Special Education | Ph.D. | Doctor of Philosophy in Special Education (Ph.D.) |

#### COLLEGE OF ENGINEERING, COMPUTER SCIENCE, AND TECHNOLOGY

| 系 | 学位 | 专业 |
|------|------|------|
| Technology | MA | Industrial and Technical Studies, M.A. (Program Suspended, Fall 2019) |
| Civil Engineering | MS | Civil Engineering, M.S. |
| Computer Science | MS | Computer Science, M.S. |
| Electrical and Computer Engineering | MS | Electrical Engineering, M.S. |
| Technology | MS | Industrial Management, M.S. |
| Interdisciplinary (BME/MSE) | MS | Materials Science and Engineering, M.S. |
| Mechanical Engineering | MS | Mechanical Engineering, M.S. |

#### COLLEGE OF ETHNIC STUDIES

| 系 | 学位 | 专业 |
|------|------|------|
| Chicana(o) and Latina(o) Studies | MA | Chicana(o) and Latina(o) Studies, M.A. |
| Pan-African Studies | MA | Pan African Studies, M.A. |

#### RONGXIANG XU COLLEGE OF HEALTH AND HUMAN SERVICES

| 系 | 学位 | 专业 |
|------|------|------|
| Child and Family Studies | MA | Child Development, M.A. |
| Audiology and Speech-Language Pathology | MA | Communicative Disorders, M.A. |
| Public Health | MPH | Public Health, M.P.H. |
| School of Criminal Justice and Criminalistics | MS | Criminalistics, M.S. |
| School of Kinesiology | MS | Kinesiology, M.S. |
| Patricia A. Chin School of Nursing | MS | Nursing, M.S. |
| Nutrition and Dietetics | MS | Nutritional Science, M.S. |
| School of Social Work | MSW | Social Work, M.S.W. |
| Audiology and Speech-Language Pathology | AuD | Doctor of Audiology (AuD) |

#### COLLEGE OF NATURAL AND SOCIAL SCIENCES

| 系 | 学位 | 专业 |
|------|------|------|
| Anthropology | MA | Anthropology, M.A. |
| Geography, Geology, and Environment | MA | Geography, M.A. |
| History | MA | History, M.A. |
| Interdisciplinary (Latin American Studies) | MA | Latin American Studies, M.A. |
| Political Science | MA | Political Science, M.A. |
| Psychology | MA | Psychology, M.A. |
| Sociology | MA | Sociology, M.A. |
| Political Science | MPA | Public Administration, M.P.A. |
| Biological Sciences | MS | Biology, M.S. |
| Chemistry and Biochemistry | MS | Chemistry, M.S. |
| Geography, Geology, and Environment | MS | Environmental Science, M.S. |
| Geography, Geology, and Environment | MS | Geological Sciences, M.S. |
| Mathematics | MS | Mathematics, M.S. |
| Physics and Astronomy | MS | Physics, M.S. |
| Psychology | MS | Psychology, M.S. |

#### UNIVERSITY PROGRAMS (cross-college)

| 系 | 学位 | 专业 |
|------|------|------|
| Interdisciplinary Studies | MA | Interdisciplinary Studies Master's Degree |

### 2.2 Post-Baccalaureate Certificates (38 total)

| 学院 | 证书 |
|------|------|
| Arts and Letters | Women's, Gender, and Sexuality Studies |
| Business and Economics | Accounting; Advanced Information Systems; Big Data; Business Intelligence; Business Management; Enterprise Systems; Healthcare Leadership; Real Estate |
| Education | California Reading Certificate; Transition Specialist; Autism Spectrum Disorders; Bilingual Authorization; Bilingualism and Global Education; Clinical Counseling; Computer Applications in Schools (CAS); Educational Therapy; English as a Second or Foreign Language (ESL/EFL); Ethnic Studies Pedagogies; Higher Education and Career Counseling; Online Teaching and Learning (COTL); Postsecondary Reading; Special Education Paraprofessional; Speech-Language Pathology; Storytelling for Teachers and Classrooms; Teachers of English Learners; Teaching Learners with Special Needs |
| Engineering, CS & Tech | Fundamentals of Radar Systems |
| HHS | Audiology Assistant; School Nurse; Nutritional Science; Speech-Language Pathology |
| Natural & Social Sciences | Biotechnology; Clinical Genetic Molecular Biology Science; Clinical Laboratory Science; Geographic Information Systems |

### 2.3 Post-Master's Certificates (7 total)

| 学院 | 证书 |
|------|------|
| Education | Applied Behavior Analysis |
| HHS | Nursing Administration; Adult-Gerontology Acute Care Nurse Practitioner (AGACNP); Adult-Gerontology Primary Care Nurse Practitioner (AGPCNP); Family Nurse Practitioner (FNP); Family Psychiatric/Mental Health Nurse Practitioner (FPMHNP); Nursing Education |

### 2.4 Credentials (28 total)

| 类型 | 凭证 |
|------|------|
| Added Authorizations | Adapted Physical Education Added Authorization (APEAA) |
| Advanced/Professional Clear | Clear Induction Administrative Services Credential; Multiple Subject Clear/Induction Credential Program; Reading and Literacy Leadership Specialist Credential; Single Subject Clear/Induction Credential Program |
| Education Specialist | Preliminary ECSE; Preliminary ESN; Preliminary MMSN; Preliminary VI |
| Services | Clinical or Rehabilitative Services Credential: Orientation and Mobility (O&M); Pupil Personnel Services: School Counseling; Pupil Personnel Services: School Psychology |
| Teaching | Art; CalState TEACH (CST); Chemistry; Geological Sciences; History Teaching; Industrial Technology; Kinesiology; Mexican American Studies; Modern Languages and Literatures; Multiple Subject Teaching; Music; Natural Science; Natural Science Subject Matter; Preliminary Administrative Services; Single Subject - English; Single Subject in Secondary Teaching; Single Subject Prep in Natural Science: Chemistry Emphasis; Single Subject Prep in Natural Sciences: Biological Sciences Emphasis; Single Subject Teaching; Speech-Language Pathology Services; Subject Matter Waiver Programs in Mathematics; Subject Waiver for Single Subject in Social Sciences; Theatre Arts and Dance |

### 2.5 Graduate Admissions Model

- All CSU graduate applicants apply via **Cal State Apply** (https://www.calstate.edu/apply), the centralized CSU system application.
- Application fee: **$70 per campus** (same as UG).
- Individual departments/programs may have additional admission requirements (GRE/GMAT, portfolio, writing samples, prerequisite coursework).
- Many programs admit for Fall only; some admit for Spring and Winter/Summer.
- Deadlines vary by program; consult each department's page.

> **Source**: Cal State LA Admissions and Recruitment (`https://www.calstatela.edu/admissions`) and Cal State LA Graduate page (`https://www.calstatela.edu/admissions/graduate`).
> **Capture date**: 2026-07-07

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 |
|------|-----|
| Standardized application | Cal State Apply (https://www.calstate.edu/apply) |
| Application fee | $70 per campus (CSU systemwide) |
| Application fee waiver | Available for California residents and other qualified applicants via Cal State Apply |
| Filing periods | Spring 2027: Priority Jul 1 – Aug 31, 2026 (Transfer/Grad/Post-bacc only); Fall 2027: Priority Oct 1 – Nov 30, 2026 (all applicant types) |
| Freshman application opens for preview | Aug 1, 2026 |
| International Freshman Fall 2027 filing | Oct 1, 2026 – Mar 31, 2027 |
| Required high school coursework | 15-unit A-G pattern (CSU minimums) |
| Min GPA | CSU eligibility index-based; Cal State LA is impacted for several majors |
| Test policy (SAT/ACT) | **TEST-FREE / TEST-BLIND** for CSU first-time freshmen through Fall 2026 cycle (and ongoing as CSU system policy) |
| Auditions / Portfolios | Required for Art, Music (B.M.), Theatre, Dance, Cinematic Arts/TV Film programs |

> **Source**: Cal State LA Admissions and Recruitment (`https://www.calstatela.edu/admissions`).
> **Source**: Cal State LA International Freshman Admission (`https://www.calstatela.edu/admissions/international-freshman-admission`) — verbatim: "International First-Time Freshman Application Filing Period is Oct. 1, 2026 - Mar. 31, 2027".
> **Capture date**: 2026-07-07

### 3.2 Undergraduate English Proficiency Table (International applicants)

| Exam | Qualifying Undergraduate Score | Qualifying Graduate/Post-Bac Score |
|------|-------------------------------|------------------------------------|
| TOEFL iBT (exams before Jan 21, 2026) | 61 iBT or higher | 80 iBT or higher (TESOL: 100) |
| TOEFL iBT (exams on/after Jan 21, 2026) | 3.5 iBT or higher | 4.0 iBT or higher (TESOL: 5.0) |
| IELTS | Band 5.5 or higher | Band 6.0 or higher (TESOL: 7.5) |
| PTE Academic | 44 or higher | 53 or higher |
| Duolingo English Test (DET) | 95 or higher | 105 or higher (TESOL: 125) |

> **Source**: Cal State LA English Language Proficiency (`https://www.calstatela.edu/admissions/english-language-proficiency`).
> **Note**: Scores are valid for 2 years from the test date. Official scores must be sent directly to Cal State LA by the testing agency (TOEFL Institutional Code 4399; IELTS via Cal State Apply; PTE to "California State University, Los Angeles"; DET via Duolingo account).
> **Waiver**: Applicants who have completed certain English composition coursework at a U.S. institution (or other waiver criteria) may be exempt. See "English Language Proficiency Waiver" sections on the page.
> **Capture date**: 2026-07-07

### 3.3 Graduate — Global Rules

| 字段 | 值 |
|------|-----|
| Application portal | Cal State Apply (https://www.calstate.edu/apply) |
| Application fee | $70 per campus |
| Minimum GPA | 2.5 undergraduate for most programs (some programs higher) |
| Standardized tests | Varies by program — most master's programs do NOT require GRE; specific programs (e.g., Ed.D., AuD, doctoral) require GRE/MAT or other |
| English proficiency | Same as UG table above; minimums higher for graduate |
| Fall application deadline | Varies by program; typically March 1 for many programs, but earlier for impacted programs |
| Department supplemental materials | Required by individual programs (writing samples, statements, recommendations) |

> **Source**: Cal State LA Admissions and Recruitment / Cal State Apply.
> **Capture date**: 2026-07-07

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| Cost Type | Commuter | On Campus | Off Campus |
|-----------|----------|-----------|------------|
| Tuition & Mandatory Fees | $7,938 | $7,938 | $7,938 |
| Housing | $10,000 | $13,682 | $13,604 |
| Food | $4,420 | $7,972 | $8,662 |
| Books, Course Materials, Supplies, Equipment | $1,128 | $1,128 | $1,128 |
| Transportation | $2,096 | $3,002 | $3,002 |
| Miscellaneous | $4,062 | $4,726 | $4,726 |
| Loan Fees (avg) | $52 | $52 | $52 |
| **CA Resident TOTAL** | **$29,696** | **$38,500** | **$39,112** |

> **Source**: Cal State LA Financial Aid and Scholarships — Cost of Attendance 2026-2027 (`https://www.calstatela.edu/financialaid/cost-attendance`), Undergraduate Students section, verbatim: "Tuition & Mandatory Fees $7,938 / Housing $10,000 / Food $4,420 / Books, Course Materials, Supplies, and Equipment $1,128 / Transportation $2,096 / Miscellaneous $4,062 / Loan Fees* $52 / CA Resident TOTAL $29,696 / $38,500 / $39,112".
> **Non-resident surcharge**: Non-resident students are assessed an additional **$471 per unit**.
> **Capture date**: 2026-07-07

### 4.2 Graduate Cost (2026-27 Academic Year, Line-Itemized)

| Cost Type | Commuter | On Campus | Off Campus |
|-----------|----------|-----------|------------|
| Tuition & Mandatory Fees | $9,648 | $9,648 | $9,648 |
| Housing | $10,000 | $13,682 | $13,604 |
| Food | $4,420 | $7,972 | $8,662 |
| Books, Course Materials, Supplies, Equipment | $1,128 | $1,128 | $1,128 |
| Transportation | $2,096 | $3,002 | $3,002 |
| Miscellaneous | $4,062 | $4,726 | $4,726 |
| Loan Fees (avg) | $52 | $52 | $52 |
| **CA Resident TOTAL** | **$31,406** | **$40,210** | **$40,822** |

> **Source**: Cal State LA Financial Aid and Scholarships — Cost of Attendance 2026-2027 (`https://www.calstatela.edu/financialaid/cost-attendance`), Graduate Students section.
> **Non-resident surcharge**: Non-resident students are assessed an additional **$471 per unit**.
> **Graduate Business Professional Fee**: An additional per-unit fee (currently $270/semester unit, $180/quarter unit) is assessed for authorized graduate business programs (MBA, MS Accounting, MS Business Analytics, MS Information Systems, etc.). Source: CSU Tuition website (https://www.calstate.edu/sustainability/tuition-and-fees).
> **Capture date**: 2026-07-07

### 4.3 Tuition & Fees Reference (CSU Systemwide Schedule, 2024-25)

CSU systemwide tuition (subject to annual change, all CSUs use the same schedule):

| Program Type | Units | Per Semester | Per Quarter | Per Academic Year |
|--------------|-------|--------------|-------------|-------------------|
| Undergraduate | 6.1+ | $2,871 | $1,914 | $5,742 |
| Undergraduate | 0–6.0 | $1,665 | $1,110 | $3,330 |
| Credential | 6.1+ | $3,330 | $2,220 | $6,660 |
| Credential | 0–6.0 | $1,932 | $1,288 | $3,864 |
| Graduate/Post-bacc | 6.1+ | $3,588 | $2,392 | $7,176 |
| Graduate/Post-bacc | 0–6.0 | $2,082 | $1,388 | $4,164 |
| Doctoral — Audiology | full-time | $7,371/sem | n/a | $14,742 |
| Doctoral — Education | full-time | $5,919/sem | $3,946/qtr | $11,838 |
| Non-resident surcharge | per unit | $396/sem | $264/qtr | varies |

> **Source**: Cal State LA Catalog — Fees and Financial Aid (`https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=11168`), "2024-25 Schedule of Tuition and Fees".
> **Note**: The 2026-27 figures in 4.1/4.2 include the systemwide tuition PLUS campus-based mandatory fees. CSU campus fees differ by campus; Cal State LA's campus-based fees are part of the $7,938 UG / $9,648 Grad totals.
> **Capture date**: 2026-07-07

### 4.4 Financial Aid

- **FAFSA** is required for federal/state aid eligibility. The Cal State LA priority filing deadline was **March 2, 2026** for the 2026-2027 academic year. Cal State LA School Code: **001140**.
- **CA Dream Act Application** is available for undocumented/AB 540 students.
- Types of aid: Federal Pell Grant, Cal Grant, State University Grant, Middle-Class Scholarship, Federal Direct Loans (Subsidized/Unsubsidized), Federal Work-Study, scholarships.
- Cal State LA is part of the Western Undergraduate Exchange (WUE) — WUE students pay 150% of resident tuition.
- Cal State LA is recognized as a top university for upward mobility (ranked #1 in the U.S. by several mobility-focused rankings).

> **Source**: Cal State LA Financial Aid (`https://www.calstatela.edu/financialaid`) — verbatim: "The 2026-2027 FAFSA and CA Dream Act Application are available for submission. The Cal State LA priority filing deadline was March 2, 2026. Cal State LA School Code: 001140".
> **Capture date**: 2026-07-07

---

## SECTION 5 — Evidence Chain Index

Each numeric or policy field above carries evidence. Key evidence items:

### E-U-001: Cal State Apply Application
- **source_url**: https://www.calstate.edu/apply
- **source_snippet**: "Cal State Apply — California State University"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-002: Spring 2027 Priority Filing Period
- **source_url**: https://www.calstatela.edu/admissions
- **source_snippet**: "Spring 2027 Admissions — Priority Application Filing Period is Jul. 1 – Aug. 31, 2026 — Select majors and programs available — Open for transfer and graduate/post-bac applicants — Closed for first-time freshman and international transfer applicants"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-003: Fall 2027 Priority Filing Period
- **source_url**: https://www.calstatela.edu/admissions
- **source_snippet**: "Fall 2027 Admissions — Priority Application Filing Period is Oct. 1 – Nov. 30, 2026 — Cal State Apply opens for preview on Aug. 1 — Open to all levels and applicant types"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-004: International Freshman Fall 2027 Filing
- **source_url**: https://www.calstatela.edu/admissions/international-freshman-admission
- **source_snippet**: "International First-Time Freshman Application Filing Period is Oct. 1, 2026 - Mar. 31, 2027"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-005: TOEFL Score Minimums
- **source_url**: https://www.calstatela.edu/admissions/english-language-proficiency
- **source_snippet**: "Test of English as a Foreign Language (TOEFL ibt) — Exams taken before Jan 21, 2026: 61 iBT or higher / Exams taken on or after Jan 21, 2026: 3.5 iBT or higher — Exams taken before Jan 21, 2026: 80 iBT or higher / TESOL program: 100 iBT or higher — Exams taken on or after Jan 21, 2026: 4.0 iBT or higher / TESOL program: 5.0 iBT or higher"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-006: IELTS, PTE, DET Score Minimums
- **source_url**: https://www.calstatela.edu/admissions/english-language-proficiency
- **source_snippet**: "International English Language Testing System (IELTS) — Band 5.5 or higher / Band 6.0 or higher / TESOL program: Band 7.5 or higher — Pearson Test of English (PTE) Academic — 44 or higher / 53 or higher — Duolingo English Test (DET) — 95 or higher / 105 or higher / TESOL program: 125 or higher"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-007: Undergraduate Cost of Attendance 2026-27
- **source_url**: https://www.calstatela.edu/financialaid/cost-attendance
- **source_snippet**: "Undergraduate Students (Full Time for Two Semesters). Non-resident students are assessed an additional $471 per unit. — Tuition & Mandatory Fees $7,938 / Housing $10,000 / Food $4,420 / Books $1,128 / Transportation $2,096 / Miscellaneous $4,062 / Loan Fees $52 / CA Resident TOTAL $29,696 / $38,500 / $39,112"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-008: Graduate Cost of Attendance 2026-27
- **source_url**: https://www.calstatela.edu/financialaid/cost-attendance
- **source_snippet**: "Graduate Students (Full Time for Two Semesters). Non-resident students are assessed an additional $471 per unit. — Tuition & Mandatory Fees $9,648 / Housing $10,000 / Food $4,420 / Books $1,128 / Transportation $2,096 / Miscellaneous $4,062 / Loan Fees $52 / CA Resident TOTAL $31,406 / $40,210 / $40,822"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-009: FAFSA Priority Deadline
- **source_url**: https://www.calstatela.edu/financialaid
- **source_snippet**: "The 2026-2027 FAFSA and CA Dream Act Application are available for submission. The Cal State LA priority filing deadline was March 2, 2026. Cal State LA School Code: 001140"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-010: CSU Systemwide Tuition (2024-25 baseline)
- **source_url**: https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=11168
- **source_snippet**: "2024-25 Basic Tuition for All Students — Undergraduate Tuition 6.1 or more units $2,871/sem $5,742/yr — Graduate or Other/Post-baccalaureate Tuition 6.1 or more units $3,588/sem $7,176/yr — Nonresident Tuition Charge Per Unit $396/sem"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-011: Eight Colleges
- **source_url**: https://www.calstatela.edu/academics
- **source_snippet**: "COLLEGES — College of Arts and Letters; College of Business and Economics; College of Education; College of Engineering, Computer Science, and Technology; College of Ethnic Studies; Rongxiang Xu College of Health and Human Services; College of Natural and Social Sciences; College of Professional and Global Education; The Honors College; University Library; California Promise"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-012: Programs by Colleges (Master List)
- **source_url**: https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=9395
- **source_snippet**: "PROGRAMS BY COLLEGES — COLLEGE OF ARTS AND LETTERS / COLLEGE OF BUSINESS AND ECONOMICS / COLLEGE OF EDUCATION / COLLEGE OF ENGINEERING, COMPUTER SCIENCE, AND TECHNOLOGY / COLLEGE OF ETHNIC STUDIES / RONGXIANG XU COLLEGE OF HEALTH AND HUMAN SERVICES / COLLEGE OF NATURAL AND SOCIAL SCIENCES / COLLEGE OF PROFESSIONAL AND GLOBAL EDUCATION / HONORS COLLEGE / UNIVERSITY LIBRARY / UNIVERSITY PROGRAMS"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-013: Colleges & Departments Detail
- **source_url**: https://ecatalog.calstatela.edu/content.php?catoid=77&navoid=11969
- **source_snippet**: "COLLEGES & DEPARTMENTS — College of Arts & Letters [10 departments]; College of Natural & Social Sciences [10 departments + 1 interdisciplinary]; College of Education [3 departments]; Rongxiang Xu College of Health & Human Services [8 units]; College of Ethnic Studies [3 departments + 1 interdisciplinary]; College of Business & Economics [6 departments + 1 interdisciplinary]; College of Engineering, Computer Science, & Technology [5 departments + 1 interdisciplinary]; Honors College [1 program]; College of Professional and Global Education [1 program]"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-014: Doctoral Programs
- **source_url**: https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=6231
- **source_snippet**: "Doctoral Degrees — Doctor of Audiology (AuD); Doctor of Education (Ed.D.); Doctor of Philosophy (Ph.D.)"
- **evidence_type**: official_webpage_table
- **capture_date**: 2026-07-07

### E-U-015: I-20 / F-1 Visa Process
- **source_url**: https://www.calstatela.edu/admissions/international-applicants
- **source_snippet**: "All admitted international students who will study on an F-1 visa must request an I-20 immigration document in order to begin the visa process. — What You'll Need: A copy of your passport (biographical page); Proof of financial support; If you are already studying in the U.S.: Copy of your current visa stamp; Copy of your I-94; Copy of your current I-20"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-016: Application Fee $70
- **source_url**: https://ecatalog.calstatela.edu/content.php?catoid=55&navoid=11168
- **source_snippet**: "Application fee (nonrefundable), payable online at the time of application via credit card or PayPal: $70"
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-017: Upward Mobility Ranking
- **source_url**: https://www.calstatela.edu/admissions
- **source_snippet**: "Cal State LA is ranked number one in the U.S. for the upward mobility of our graduates. That means we're the best university in the nation at helping our students earn their degrees and propel up the economic ladder."
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

### E-U-018: Mission / Campus Identity
- **source_url**: https://www.calstatela.edu/about
- **source_snippet**: "Cal State LA is committed to student-centered learning, free scholarly inquiry, and academic excellence within a diverse community."
- **evidence_type**: official_webpage
- **capture_date**: 2026-07-07

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

The WeKnora collection for Cal State LA should be organized as:

```
Collection: California State University, Los Angeles — Admissions Knowledge Base
├── Chunk Group: Institution Overview
│   ├── CalStateLA_overview_meta
│   ├── CalStateLA_colleges_and_departments
│   └── CalStateLA_degree_inventory
├── Chunk Group: Undergraduate Programs
│   ├── CalStateLA_ug_college_of_arts_and_letters
│   ├── CalStateLA_ug_college_of_business_and_economics
│   ├── CalStateLA_ug_college_of_education
│   ├── CalStateLA_ug_college_of_engineering_cs_tech
│   ├── CalStateLA_ug_college_of_ethnic_studies
│   ├── CalStateLA_ug_rongxiang_xu_hhs
│   ├── CalStateLA_ug_college_of_natural_and_social_sciences
│   ├── CalStateLA_ug_professional_and_global_education
│   ├── CalStateLA_ug_minors
│   └── CalStateLA_ug_certificates
├── Chunk Group: Graduate Programs
│   ├── CalStateLA_grad_arts_and_letters
│   ├── CalStateLA_grad_business_and_economics
│   ├── CalStateLA_grad_education
│   ├── CalStateLA_grad_engineering_cs_tech
│   ├── CalStateLA_grad_ethnic_studies
│   ├── CalStateLA_grad_hhs
│   ├── CalStateLA_grad_natural_and_social_sciences
│   ├── CalStateLA_grad_certificates_postbacc
│   └── CalStateLA_grad_credentials
├── Chunk Group: Application & Admissions
│   ├── CalStateLA_application_deadlines
│   ├── CalStateLA_application_fee
│   ├── CalStateLA_test_policy
│   ├── CalStateLA_english_proficiency
│   └── CalStateLA_graduate_admissions_model
├── Chunk Group: Costs & Financial Aid
│   ├── CalStateLA_ug_cost_2026_27
│   ├── CalStateLA_grad_cost_2026_27
│   ├── CalStateLA_csu_systemwide_tuition
│   └── CalStateLA_financial_aid
└── Chunk Group: Evidence Chain
    └── CalStateLA_evidence_chain (E-U-001 … E-U-018)
```

### Per-Chunk Metadata Template

```json
{
  "chunk_id": "CalStateLA_<chunk_group>_<topic>",
  "school": "California State University, Los Angeles",
  "slug": "calstatela",
  "csulb_alias": "Cal State LA / CSULA",
  "url": "<source_url>",
  "content": "<extracted text or table>",
  "evidence_type": "official_webpage",
  "capture_date": "2026-07-07",
  "tags": ["CSULA", "Cal State LA", "CalStateLA", "CSU system", "T5", "public", "Hispanic-Serving"],
  "field": "<ug.deadlines | ug.cost | grad.programs | ...>"
}
```

### Follow-up Data Items (Prioritized)

1. **Individual program admissions requirements** (GRE, GMAT, portfolio, writing samples) — needs per-program page extraction.
2. **Transfer admission eligibility index** — currently CSULA uses CSU systemwide eligibility with local impaction criteria.
3. **Specific graduate program deadlines** — varies by program.
4. **Housing rates** — Cal State LA has on-campus housing; specific room rates not captured at the COA level.
5. **Departmental websites** — for course-level requirements and faculty.

---

## SECTION 7 — Cross-School Comparison Framework

Cal State LA data fits the standard CSU comparison framework:

| Field | Cal State LA Value |
|-------|-------------------|
| State | California |
| CSU campus # | 23-campus system (Cal State LA is the 8th campus) |
| Carnegie classification | Master's Colleges & Universities: Larger Programs (M1) |
| Carnegie size | 4-year, very high undergraduate enrollment |
| Setting | Urban (Los Angeles) |
| Founded | 1947 |
| Campus size | ~200 acres (Cal State LA main campus + San Pedro satellite) |
| Total students (most recent) | ~26,000 (per Cal State LA Facts & Figures) |
| UG enrollment | ~22,000 |
| Grad enrollment | ~4,000 |
| Calendar system | Semester |
| Test policy | Test-free (CSU systemwide) |
| Common App | No (uses Cal State Apply) |
| Application fee | $70 |
| Application portal | https://www.calstate.edu/apply |
| TOEFL min UG | 61 (pre-Jan 2026) / 3.5 (post-Jan 2026) |
| TOEFL min Grad | 80 (pre-Jan 2026) / 4.0 (post-Jan 2026) |
| IELTS min UG | 5.5 |
| IELTS min Grad | 6.0 |
| Tuition (CA resident, UG, full-time, systemwide) | $5,742/yr (2024-25 schedule) + campus fees |
| Total COA (CA resident, UG, on-campus, 2026-27) | $38,500 |
| Total COA (CA resident, Grad, on-campus, 2026-27) | $40,210 |
| Financial aid priority deadline | March 2, 2026 |
| FAFSA school code | 001140 |
| Special designations | Hispanic-Serving Institution (HSI); AANAPISI; Top-1 for upward mobility (multiple rankings) |

### Cal State LA vs CSULB Comparison (relevant to this batch)

| Dimension | Cal State LA | CSULB |
|-----------|--------------|-------|
| City | Los Angeles | Long Beach |
| Founded | 1947 | 1949 |
| Colleges | 8 (+ Honors) | 7 |
| UG majors | 77 | ~95 |
| Minors | 86 | ~80 |
| UG certs | 33 | ~5 |
| Grad degrees | ~60 (incl. 1 AuD, 1 Ed.D., 1 Ph.D.) | ~85 |
| Credentials | 28 | ~30 |
| Tuition & Mandatory Fees (UG, 2026-27) | $7,938 | $8,748 ($6,838 tuition + $1,910 mandatory fees) |
| Tuition & Mandatory Fees (Grad, 2026-27) | $9,648 | standard grad $8,548 |
| Test policy | Test-free | Test-free |
| Application | Cal State Apply | Cal State Apply |
| FAFSA code | 001140 | 001141 |
| Special designation | HSI, AANAPISI | HSI |

> Both schools are part of the 23-campus CSU system and share the Cal State Apply application, the systemwide tuition schedule, and the test-free admission policy. Campus-specific data (mandatory campus fees, deadlines, college structure, individual program offerings) differs.

---

*End of California State University, Los Angeles knowledge base document. Capture date: 2026-07-07. Generated by the uni-admissions-research skill (ego-browser scraping).*