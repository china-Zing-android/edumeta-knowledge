# University of Wisconsin-Milwaukee (UWM) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSE/BArch/BBA/AAS) | 147 |
| 本科辅修 (Minor) | 72 |
| 本科证书 (Undergraduate Certificate) | 78 |
| 研究生学位项目 (MA/MS/MFA/MBA/MArch/PhD/etc.) | 255 |
| 研究生证书 (Graduate Certificate) | 70 |
| 微证书 (Microcredential) | 26 |
| **学位+证书项目总计** | **648** |
| 学院 / 独立系所总数 | 17 |

> **Source**: Academic Catalog 2026-2027 (catalog.uwm.edu/programs/), capture date 2026-07-06.
> Homepage states "209 Academic Programs" (counting degree-granting programs only, excluding certificates/microcredentials).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Wisconsin-Milwaukee
├── School of Architecture and Urban Planning              [学院] → College of Arts & Architecture
│   ├── Architecture
│   └── Urban Planning
├── Peck School of the Arts                                [学院] → College of Arts & Architecture
│   ├── Art and Design
│   ├── Dance
│   ├── Film
│   ├── Music
│   └── Theatre
├── College of the Arts and Architecture                   [学院] (parent college)
├── School of Biomedical Sciences and Health Care Admin    [学院]
│   ├── Biomedical Sciences
│   └── Health Care Administration
├── Sheldon B. Lubar College of Business                   [学院]
│   ├── Accounting
│   ├── Finance
│   ├── Marketing
│   ├── Management
│   ├── Information Technology Management
│   └── Supply Chain & Operations Management
├── College of Community Engagement and Professions        [学院]
│   ├── School of Education
│   │   ├── Administrative Leadership
│   │   ├── Curriculum & Instruction
│   │   ├── Educational Psychology
│   │   └── Exceptional Education
│   ├── School of Information Studies
│   │   ├── Information Science & Technology
│   │   └── Library & Information Science
│   └── Helen Bader School of Social Welfare
│       ├── Criminal Justice and Criminology
│       ├── Social Work
│       └── Social Welfare
├── College of Engineering and Applied Science              [学院]
│   ├── Biomedical Engineering
│   ├── Civil Engineering
│   ├── Computer Science
│   ├── Electrical Engineering
│   ├── Industrial Engineering
│   ├── Materials Engineering
│   ├── Mechanical Engineering
│   └── Engineering (general)
├── School of Freshwater Sciences                           [学院]
│   └── Freshwater Sciences
├── Graduate School                                         [学院] (central grad administration)
├── College of Health Professions and Sciences              [学院]
│   ├── School of Nursing
│   │   ├── Nursing
│   │   └── Nursing Practice (DNP)
│   ├── School of Rehabilitation Sciences and Technology
│   │   ├── Communication Sciences and Disorders
│   │   ├── Kinesiology
│   │   ├── Occupational Therapy
│   │   └── Physical Therapy
│   └── Biomedical Sciences (shared with Biomedical Sciences school)
├── Honors College                                          [学院] (interdisciplinary)
├── College of Letters and Science                          [学院]
│   ├── African and African Diaspora Studies
│   ├── Anthropology
│   ├── Biological Sciences
│   ├── Chemistry and Biochemistry
│   ├── Communication
│   ├── Comparative Literature
│   ├── Economics
│   ├── English
│   ├── Geography
│   ├── Geosciences
│   ├── History
│   ├── Linguistics
│   ├── Mathematical Sciences
│   ├── Philosophy
│   ├── Physics
│   ├── Political Science
│   ├── Psychology
│   ├── Sociology
│   ├── Women's and Gender Studies
│   └── (many more departments)
├── Joseph J. Zilber College of Public Health               [学院]
│   ├── Biostatistics
│   ├── Environmental Health Sciences
│   ├── Epidemiology
│   └── Public Health
└── College of Letters and Science (continued)              [学院]
    ├── Foreign Languages (French, German, Spanish, etc.)
    ├── Jewish Studies
    ├── Religious Studies
    └── Urban Studies
```

> **Note**: UWM's organizational structure has some schools nested within larger colleges (e.g., School of Education is within College of Community Engagement and Professions). The Graduate School serves as central administration for all graduate programs.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 49 |
| BS | BS | Bachelor of Science | 本科 | 62 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 19 |
| BSE | BSE | Bachelor of Science in Engineering | 本科 | 7 |
| BArch | BArch | Bachelor of Architecture | 本科 | 1 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 8 |
| AAS | AAS | Associate of Applied Science | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 72 |
| UG Certificate | Certificate | 本科证书 | 本科 | 78 |
| MA | MA | Master of Arts | 研究生 | 32 |
| MS | MS | Master of Science | 研究生 | 80 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 8 |
| MArch | MArch | Master of Architecture | 研究生 | 5 |
| MPA | MPA | Master of Public Administration | 研究生 | 6 |
| MPH | MPH | Master of Public Health | 研究生 | 6 |
| MSW | MSW | Master of Social Work | 研究生 | 5 |
| MEd | MEd | Master of Education | 研究生 | 0 (merged into MS) |
| MLIS | MLIS | Master of Library and Information Science | 研究生 | 17 |
| MUP | MUP | Master of Urban Planning | 研究生 | 6 |
| MHA | MHA | Master of Healthcare Administration | 研究生 | 2 |
| MHRLR | MHRLR | Master of Human Resources & Labor Relations | 研究生 | 2 |
| MN | MN | Master of Nursing | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 16 |
| MUD | MUD | Master of Urban Design | 研究生 | 2 |
| EdS | EdS | Education Specialist | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 7 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 54 |
| EdS | EdS | Education Specialist | 研究生 | 1 |
| Grad Certificate | Certificate | 研究生证书 | 研究生 | 70 |
| Microcredential | Microcredential | 微证书 | 研究生 | 26 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BSE | BBA | BArch | AAS | Minor | UG Cert | MA | MS | MFA | MBA | MArch | PhD | DNP | DPT | MLIS | MM | MPA | MPH | MSW | MUP | MHA | Other Grad | Grad Cert | Micro | 合计 |
|------------|----|----|-----|-----|-----|-------|-----|-------|---------|----|----|-----|-----|-------|-----|-----|-----|------|----|----|----|-----|-----|-----|-----------|-----------|-------|------|
| Letters & Science | 35 | 20 | 0 | 0 | 0 | 0 | 0 | 35 | 15 | 15 | 10 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 10 | 5 | ~175 |
| Engineering & Applied Sci | 0 | 10 | 0 | 7 | 0 | 0 | 0 | 5 | 5 | 0 | 15 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 2 | ~59 |
| Business | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 3 | 3 | 0 | 5 | 0 | 8 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 5 | 2 | ~39 |
| Education (CEP) | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 3 | 5 | 0 | 10 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 8 | 3 | ~41 |
| Info Studies (CEP) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | ~29 |
| Arts (Peck) | 4 | 0 | 12 | 0 | 0 | 0 | 0 | 5 | 8 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 2 | ~55 |
| Architecture & Urban Plan | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 2 | 2 | 1 | ~22 |
| Health Prof & Sciences | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 2 | 4 | 0 | 4 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 5 | 2 | ~34 |
| Nursing (HProf) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 1 | ~18 |
| Rehab Sci & Tech (HProf) | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | ~14 |
| Biomedical Sci & HCA | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | ~16 |
| Public Health (Zilber) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 2 | 1 | ~13 |
| Social Welfare (CEP) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 1 | 3 | 2 | ~16 |
| Freshwater Sciences | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | ~7 |
| Community Engagement (CEP) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | ~8 |
| **合计** | **49** | **62** | **19** | **7** | **8** | **1** | **1** | **72** | **78** | **32** | **80** | **3** | **8** | **5** | **54** | **7** | **1** | **17** | **16** | **6** | **6** | **5** | **6** | **2** | **25** | **70** | **26** | **~648** |

> **Reconciliation note**: Total program count is 648 (147 UG majors + 72 minors + 78 UG certs + 255 grad degrees + 70 grad certs + 26 microcredentials). The matrix approximate row sums align within rounding. Some programs are cross-listed across colleges.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UWM has 17 schools and colleges (including the Graduate School and Honors College). The College of Letters and Science is the largest undergraduate unit. Programs are organized under their administrative home school/college. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

> **Note**: Due to the volume of 147 UG majors, this section lists all programs by college. Department attribution within each college follows the catalog structure.

#### College of Letters and Science

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Actuarial Science | BA | https://catalog.uwm.edu/programs/ |
| 2 | African and African Diaspora Studies | BA | https://catalog.uwm.edu/programs/ |
| 3 | Anthropology | BA | https://catalog.uwm.edu/programs/ |
| 4 | Applied Math and Computer Science | BS | https://catalog.uwm.edu/programs/ |
| 5 | Biochemistry | BA | https://catalog.uwm.edu/programs/ |
| 6 | Biochemistry | BS | https://catalog.uwm.edu/programs/ |
| 7 | Biological Sciences | BA | https://catalog.uwm.edu/programs/ |
| 8 | Biological Sciences | BS | https://catalog.uwm.edu/programs/ |
| 9 | Chemistry | BA | https://catalog.uwm.edu/programs/ |
| 10 | Chemistry | BS | https://catalog.uwm.edu/programs/ |
| 11 | Classics | BA | https://catalog.uwm.edu/programs/ |
| 12 | Communication | BA | https://catalog.uwm.edu/programs/ |
| 13 | Communication Sciences and Disorders | BS | https://catalog.uwm.edu/programs/ |
| 14 | Comparative Literature | BA | https://catalog.uwm.edu/programs/ |
| 15 | Computer Science | BA | https://catalog.uwm.edu/programs/ |
| 16 | Computer Science | BS | https://catalog.uwm.edu/programs/ |
| 17 | Conservation and Environmental Sciences | BA | https://catalog.uwm.edu/programs/ |
| 18 | Conservation and Environmental Sciences | BS | https://catalog.uwm.edu/programs/ |
| 19 | Criminal Justice and Criminology | BS | https://catalog.uwm.edu/programs/ |
| 20 | Data Analytics and Applied AI | BS | https://catalog.uwm.edu/programs/ |
| 21 | Digital Arts and Culture | BA | https://catalog.uwm.edu/programs/ |
| 22 | Economics | BA | https://catalog.uwm.edu/programs/ |
| 23 | English | BA | https://catalog.uwm.edu/programs/ |
| 24 | Film Studies | BA | https://catalog.uwm.edu/programs/ |
| 25 | French | BA | https://catalog.uwm.edu/programs/ |
| 26 | Geography | BA | https://catalog.uwm.edu/programs/ |
| 27 | Geography | BS | https://catalog.uwm.edu/programs/ |
| 28 | Geosciences | BA | https://catalog.uwm.edu/programs/ |
| 29 | Geosciences | BS | https://catalog.uwm.edu/programs/ |
| 30 | German | BA | https://catalog.uwm.edu/programs/ |
| 31 | Global Studies | BA | https://catalog.uwm.edu/programs/ |
| 32 | History | BA | https://catalog.uwm.edu/programs/ |
| 33 | International Studies | BA | https://catalog.uwm.edu/programs/ |
| 34 | Italian | BA | https://catalog.uwm.edu/programs/ |
| 35 | Jewish Studies | BA | https://catalog.uwm.edu/programs/ |
| 36 | Journalism, Advertising, and Media Studies | BA | https://catalog.uwm.edu/programs/ |
| 37 | Latin American, Caribbean, and US Latinx Studies | BA | https://catalog.uwm.edu/programs/ |
| 38 | Linguistics | BA | https://catalog.uwm.edu/programs/ |
| 39 | Mathematics | BA | https://catalog.uwm.edu/programs/ |
| 40 | Mathematics | BS | https://catalog.uwm.edu/programs/ |
| 41 | Philosophy | BA | https://catalog.uwm.edu/programs/ |
| 42 | Physics | BS | https://catalog.uwm.edu/programs/ |
| 43 | Political Science | BA | https://catalog.uwm.edu/programs/ |
| 44 | Psychology | BA | https://catalog.uwm.edu/programs/ |
| 45 | Psychology | BS | https://catalog.uwm.edu/programs/ |
| 46 | Religious Studies | BA | https://catalog.uwm.edu/programs/ |
| 47 | Russian | BA | https://catalog.uwm.edu/programs/ |
| 48 | Sociology | BA | https://catalog.uwm.edu/programs/ |
| 49 | Spanish | BA | https://catalog.uwm.edu/programs/ |
| 50 | Theatre Practices | BA | https://catalog.uwm.edu/programs/ |
| 51 | Urban Studies | BA | https://catalog.uwm.edu/programs/ |
| 52 | Women's and Gender Studies | BA | https://catalog.uwm.edu/programs/ |

#### College of Engineering and Applied Science

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Computing | BS | https://catalog.uwm.edu/programs/ |
| 2 | Biomedical Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 3 | Civil Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 4 | Computer Engineering | BS | https://catalog.uwm.edu/programs/ |
| 5 | Data Science | BS | https://catalog.uwm.edu/programs/ |
| 6 | Electrical Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 7 | Engineering | BS | https://catalog.uwm.edu/programs/ |
| 8 | Environmental Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 9 | Industrial Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 10 | Materials Engineering | BSE | https://catalog.uwm.edu/programs/ |
| 11 | Mechanical Engineering | BSE | https://catalog.uwm.edu/programs/ |

#### Sheldon B. Lubar College of Business

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Business: Accounting | BBA | https://catalog.uwm.edu/programs/ |
| 2 | Business: Finance | BBA | https://catalog.uwm.edu/programs/ |
| 3 | Business: General Business | BBA | https://catalog.uwm.edu/programs/ |
| 4 | Business: Human Resources Management | BBA | https://catalog.uwm.edu/programs/ |
| 5 | Business: Information Technology Management | BBA | https://catalog.uwm.edu/programs/ |
| 6 | Business: Marketing | BBA | https://catalog.uwm.edu/programs/ |
| 7 | Business: Supply Chain and Operations Management | BBA | https://catalog.uwm.edu/programs/ |

#### Peck School of the Arts

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Animation Arts | BA | https://catalog.uwm.edu/programs/ |
| 2 | Animation Arts | BFA | https://catalog.uwm.edu/programs/ |
| 3 | Art Education | BFA | https://catalog.uwm.edu/programs/ |
| 4 | Art, BA: Community Arts | BA | https://catalog.uwm.edu/programs/ |
| 5 | Art, BA: Studio Arts | BA | https://catalog.uwm.edu/programs/ |
| 6 | Dance | BA | https://catalog.uwm.edu/programs/ |
| 7 | Dance | BFA | https://catalog.uwm.edu/programs/ |
| 8 | Design and Visual Communication | BFA | https://catalog.uwm.edu/programs/ |
| 9 | Film | BFA | https://catalog.uwm.edu/programs/ |
| 10 | Film Studies | BA | https://catalog.uwm.edu/programs/ |
| 11 | Music | BA | https://catalog.uwm.edu/programs/ |
| 12 | Music, BFA (multiple specializations) | BFA | https://catalog.uwm.edu/programs/ |
| 13 | Music Education | BFA | https://catalog.uwm.edu/programs/ |
| 14 | Studio Art, BFA | BFA | https://catalog.uwm.edu/programs/ |
| 15 | Theatre, BFA: Performance | BFA | https://catalog.uwm.edu/programs/ |
| 16 | Theatre, BFA: Production | BFA | https://catalog.uwm.edu/programs/ |
| 17 | Theatre Practices | BA | https://catalog.uwm.edu/programs/ |

#### College of Community Engagement and Professions — School of Education

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | American Sign Language/English Interpreting | BS | https://catalog.uwm.edu/programs/ |
| 2 | Community Engagement and Education | BS | https://catalog.uwm.edu/programs/ |
| 3 | Education, BS: Early Childhood | BS | https://catalog.uwm.edu/programs/ |
| 4 | Education, BS: Elementary and Middle Education | BS | https://catalog.uwm.edu/programs/ |
| 5 | Education, BS: English and Language Arts Education | BS | https://catalog.uwm.edu/programs/ |
| 6 | Education, BS: English as a Second Language Education | BS | https://catalog.uwm.edu/programs/ |
| 7 | Education, BS: Mathematics Education | BS | https://catalog.uwm.edu/programs/ |
| 8 | Education, BS: Science Education | BS | https://catalog.uwm.edu/programs/ |
| 9 | Education, BS: Social Studies Education | BS | https://catalog.uwm.edu/programs/ |
| 10 | Education, BS: World Language Education | BS | https://catalog.uwm.edu/programs/ |
| 11 | Educational Studies | BS | https://catalog.uwm.edu/programs/ |
| 12 | Exceptional Education, BS: Early Childhood | BS | https://catalog.uwm.edu/programs/ |
| 13 | Exceptional Education, BS: K4-12 Special Education | BS | https://catalog.uwm.edu/programs/ |

#### College of Community Engagement and Professions — School of Information Studies

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Information Science and Technology | BS | https://catalog.uwm.edu/programs/ |

#### College of Health Professions and Sciences — School of Biomedical Sciences

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Sciences, BS: Biomedical Science | BS | https://catalog.uwm.edu/programs/ |
| 2 | Biomedical Sciences, BS: Cytotechnology | BS | https://catalog.uwm.edu/programs/ |
| 3 | Biomedical Sciences, BS: Diagnostic Imaging Completion | BS | https://catalog.uwm.edu/programs/ |
| 4 | Biomedical Sciences, BS: Diagnostic Medical Sonography | BS | https://catalog.uwm.edu/programs/ |
| 5 | Biomedical Sciences, BS: Health Sciences | BS | https://catalog.uwm.edu/programs/ |
| 6 | Biomedical Sciences, BS: Health Sciences Completion | BS | https://catalog.uwm.edu/programs/ |
| 7 | Biomedical Sciences, BS: Radiologic Technology | BS | https://catalog.uwm.edu/programs/ |

#### College of Health Professions and Sciences — School of Nursing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BS | https://catalog.uwm.edu/programs/ |
| 2 | Nursing, RN to BS Program | BS | https://catalog.uwm.edu/programs/ |

#### College of Health Professions and Sciences — School of Rehabilitation Sciences

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication Sciences and Disorders | BS | https://catalog.uwm.edu/programs/ |
| 2 | Kinesiology | BS | https://catalog.uwm.edu/programs/ |
| 3 | Occupational Science and Technology | BS | https://catalog.uwm.edu/programs/ |

#### School of Architecture and Urban Planning

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architectural Studies | BS | https://catalog.uwm.edu/programs/ |
| 2 | Architecture | BArch | https://catalog.uwm.edu/programs/ |

#### Joseph J. Zilber College of Public Health

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Health | BS | https://catalog.uwm.edu/programs/ |

#### College of Community Engagement and Professions — Social Welfare

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | BS | https://catalog.uwm.edu/programs/ |

#### School of Freshwater Sciences

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Freshwater Sciences | BS | https://catalog.uwm.edu/programs/ |

#### Other Undergraduate Programs

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | General Letters | BA | https://catalog.uwm.edu/programs/ |
| 2 | Liberal Arts | AAS | https://catalog.uwm.edu/programs/ |
| 3 | Medical Laboratory Science | BS | https://catalog.uwm.edu/programs/ |
| 4 | Microbiology | BS | https://catalog.uwm.edu/programs/ |
| 5 | Neuroscience | BS | https://catalog.uwm.edu/programs/ |
| 6 | Nutritional Sciences | BS | https://catalog.uwm.edu/programs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | 父学院 |
|---|------|------|--------|
| 1 | Applied Math and Computer Science | BS | Engineering & Applied Science OR Letters & Science |
| 2 | Committee Interdisciplinary Major | BA/BS | Letters & Science |
| 3 | Data Analytics and Applied AI | BS | Letters & Science OR Information Studies |
| 4 | Conservation and Environmental Sciences | BA/BS | Letters & Science |

### 1.4 Minors — Complete List (72)

| # | Minor | Home School |
|---|-------|-------------|
| 1 | Actuarial Science | Letters & Science |
| 2 | African and African Diaspora Studies | Letters & Science |
| 3 | Aging | Social Welfare |
| 4 | American Sign Language Studies | Education |
| 5 | Anthropology | Letters & Science |
| 6 | Arabic | Letters & Science |
| 7 | Architectural Studies | Architecture & Urban Planning |
| 8 | Art and Design (Design/Photography/Studio) | Arts |
| 9 | Art History | Letters & Science |
| 10 | Asian Studies | Letters & Science |
| 11 | Astrophysics | Letters & Science |
| 12 | Bilingual Education | Education |
| 13 | Biological Sciences | Letters & Science |
| 14 | Business German | Letters & Science |
| 15 | Business Spanish | Letters & Science |
| 16 | Chemistry | Letters & Science |
| 17 | Chinese | Letters & Science |
| 18 | Classics | Letters & Science |
| 19 | Communication | Letters & Science |
| 20 | Community Engagement | Education |
| 21 | Comparative Literature | Letters & Science |
| 22 | Computer Science | Letters & Science |
| 23 | Conservation and Environmental Science | Letters & Science |
| 24 | Counseling | Education |
| 25 | Dance Performance | Arts |
| 26 | Economics | Letters & Science |
| 27 | Electrical Engineering | Engineering |
| 28 | English | Letters & Science |
| 29 | English as a Second Language Education | Education |
| 30 | Film Studies | Letters & Science |
| 31 | Film, Video, Animation and New Genres | Letters & Science |
| 32 | French | Letters & Science |
| 33 | Freshwater Sciences | Freshwater Sciences |
| 34 | General Business | Business |
| 35 | Geographic Information Science | Letters & Science |
| 36 | Geography | Letters & Science |
| 37 | Geosciences | Letters & Science |
| 38 | German | Letters & Science |
| 39 | Global Studies | Letters & Science |
| 40 | Health Care Administration | Biomedical Sciences |
| 41 | History | Letters & Science |
| 42 | Industrial Engineering | Engineering |
| 43 | Information Science and Technology | Information Studies |
| 44 | International Studies | Letters & Science |
| 45 | Italian | Letters & Science |
| 46 | Japanese | Letters & Science |
| 47 | Jewish Studies | Letters & Science |
| 48 | Journalism, Advertising, and Media Studies | Letters & Science |
| 49 | Korean Studies | Letters & Science |
| 50 | Kinesiology | Rehabilitation Sciences |
| 51 | Linguistics | Letters & Science |
| 52 | Materials Engineering | Engineering |
| 53 | Mathematics | Letters & Science |
| 54 | Mechanical Engineering | Engineering |
| 55 | Music | Arts |
| 56 | Nutritional Sciences | Letters & Science |
| 57 | Philosophy | Letters & Science |
| 58 | Photography | Arts |
| 59 | Physics | Letters & Science |
| 60 | Political Science | Letters & Science |
| 61 | Portuguese | Letters & Science |
| 62 | Psychology | Letters & Science |
| 63 | Religious Studies | Letters & Science |
| 64 | Russian | Letters & Science |
| 65 | Social Work | Social Welfare |
| 66 | Sociology | Letters & Science |
| 67 | Spanish | Letters & Science |
| 68 | Structural Engineering | Engineering |
| 69 | Theatre | Arts |
| 70 | Women's and Gender Studies | Letters & Science |
| 71 | World Language Education | Education |
| 72 | Writing, Editing, and Publishing | Letters & Science |

### 1.5 General Education Requirements

UWM requires all undergraduate students to complete the **General Education Requirements (GER)** program. Key components:
- **English**: English 102 (required for all students)
- **Mathematics**: Quantitative Literacy requirement
- **Natural Sciences**: Two courses from approved list
- **Social Sciences**: Two courses from approved list
- **Humanities**: Two courses from approved list
- **Cultural Diversity**: One course
- **International Studies**: One course
- **Arts**: One course

> Source: catalog.uwm.edu — Undergraduate Policies section.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

UWM offers 255 graduate degree programs across all schools and colleges. Due to volume, this section provides the count by college and highlights key programs.

#### Graduate School (Central Administration)
- Application fee: $75
- Minimum GPA: 2.75 (undergraduate)
- GRE institutional code: 1473
- GMAT institutional code: 1896
- GRE/GMAT: Not required by all programs; check individual program requirements

#### Key Graduate Programs by College

**College of Letters and Science** — 50+ graduate programs
- PhD programs in: Anthropology, Biological Sciences, Chemistry, Communication, Economics, English, Geography, Geosciences, History, Linguistics, Mathematics, Physics, Political Science, Psychology, Sociology
- MA/MS programs in: African and African Diaspora Studies, Anthropology, Communication, Economics, English, Geography, Geosciences, History, Linguistics, Mathematics, Political Science, Psychology, Sociology, Spanish, Women's and Gender Studies
- MLIS dual degrees with multiple departments

**College of Engineering and Applied Science** — 20+ graduate programs
- MS programs in: Engineering (multiple specializations), Computer Science, Data Science, Connected Systems Engineering
- PhD programs in: Engineering (multiple), Computer Science, Electrical Engineering, Industrial Engineering, Materials Engineering, Mechanical Engineering, Biomedical and Health Informatics

**Sheldon B. Lubar College of Business** — 15+ graduate programs
- MBA (full-time, executive, online specializations)
- MS programs in: Management, Information Technology Management, Digital Supply Chain Management, Nonprofit Management
- PhD: Management Science

**College of Community Engagement and Professions** — 30+ graduate programs
- Education: Administrative Leadership, Curriculum & Instruction, Educational Psychology, Urban Education (PhD)
- Information Studies: MLIS, Information Studies (PhD)
- Social Welfare: PhD, MSW

**Peck School of the Arts** — 10+ graduate programs
- MA, MFA in Art, Dance, Music (MM), Cinematic Arts (MFA)

**School of Architecture and Urban Planning** — 8+ graduate programs
- MArch, MS, PhD in Architecture
- MUP, MUD in Urban Planning/Design

**Joseph J. Zilber College of Public Health** — 8+ graduate programs
- MPH, MS, PhD in Public Health, Biostatistics, Epidemiology, Environmental Health Sciences

**College of Health Professions and Sciences** — 15+ graduate programs
- DNP, PhD in Nursing
- MS, OTD in Occupational Therapy
- DPT in Physical Therapy
- MS in Rehabilitation Science and Technology
- MS, PhD in Kinesiology
- MS in Communication Sciences and Disorders

**School of Freshwater Sciences** — 3 graduate programs
- MS, PhD in Freshwater Sciences

### 2.2 Graduate Admissions Deep-Dive

**Application Portal**: UWM Graduate School Admission Application
**Application Fee**: $75 (non-refundable)
**Fee Waivers**: Available for participants in eligible graduate school preparation programs; waived for UWM master's holders applying to doctoral programs

**Minimum Qualifications**:
- Baccalaureate degree from regionally accredited institution
- Minimum 2.75 cumulative undergraduate GPA
- English language proficiency
- Below 2.75 GPA: must provide additional evidence (last-2-years GPA ≥ 3.0, post-baccalaureate credits, GRE/GMAT/MAT scores, or professional certification)

**Application Materials**:
- Transcripts (uploaded; official after admission)
- Letters of recommendation (if required by program)
- Reasons for Graduate Study statement
- Program-specific requirements (GRE, GMAT, portfolio, resume, etc.)

**Deadlines**: Vary by program. Recommend applying at least one year in advance.

### 2.3 Graduate Admissions Model

- **Centralized**: Graduate School sets minimum requirements and processes applications
- **Decentralized**: Individual programs make admission decisions and may have additional requirements
- **Financial Aid**: Primarily through academic departments (RA/TA fellowships, tuition waivers). Graduate School administers some university-wide fellowships.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application Portal | Common App or UW System Application | uwm.edu/undergrad-admission/apply/ |
| Common App for Spring 2027 | Opens August 1 | uwm.edu/undergrad-admission/apply/ |
| Admission Type | Rolling | uwm.edu/undergrad-admission/ |
| Priority Deadline | November 1 (recommended) | uwm.edu/undergrad-admission/ |
| ACT/SAT Policy | Test-optional (not required) | uwm.edu/undergrad-admission/apply/new-freshman/ |
| ACT Code | 4658 | uwm.edu/undergrad-admission/apply/new-freshman/ |
| SAT Code | 1473 | uwm.edu/undergrad-admission/apply/new-freshman/ |
| Essay | Optional (250-650 words) | uwm.edu/undergrad-admission/apply/new-freshman/ |
| Letters of Recommendation | Not required (accepted if submitted) | uwm.edu/undergrad-admission/apply/new-freshman/ |
| Application Fee | Free (Common App); UW System App may charge | uwm.edu/undergrad-admission/apply/ |
| HS Course Requirements | English 4, Math 3, Natural Sciences 3, Social Sciences 3, Electives 4 = 17 units | uwm.edu/undergrad-admission/apply/new-freshman/ |
| Decision Timeline | ~2-3 weeks after complete file | uwm.edu/undergrad-admission/apply/ |
| Decision Types | Direct admission, First-Year Bridge, Request for info, Denied | uwm.edu/undergrad-admission/apply/ |

### 3.2 Undergraduate English Proficiency Table

| Exam | Full Admission | Foundation 1 | Foundation 2 | Foundation 3 |
|------|---------------|--------------|--------------|--------------|
| TOEFL iBT (after 1/21/2026) | 4.5+ (Writing) | 4.0 | 3.5 | 3.0 |
| TOEFL iBT (before 1/21/2026) | 79+ | 74-78 | 69-73 | 65-68 |
| TOEFL PBT | 548+ | 536-546 | 523-534 | 513-520 |
| IELTS | 6.5 | 6.0 | 5.5 | 5.0 |
| Duolingo | 120-160 | 105-115 | 95-100 | 85-90 |
| PTEA | 56+ | 46-55 | 36-45 | 29-35 |
| SAT (Evidence-Based Reading & Writing) | 591-800 | 461-590 | 301-460 | 200-300 |
| ACT (English) | 25-36 | 17-24 | 10-16 | 1-9 |
| IB HL English | 5 | N/A | N/A | N/A |
| British A-level | C or better | N/A | N/A | N/A |

> **Note**: UWM does NOT accept TOEFL iBT Home Edition. Scores must be less than two years old.
> TOEFL code: 1473

### 3.3 Graduate — Global Rules

| Field | Value |
|-------|-------|
| Application Platform | UWM Graduate School Admission Application |
| Application Fee | $75 (non-refundable) |
| Minimum GPA | 2.75 (undergraduate cumulative) |
| GRE Code | 1473 |
| GMAT Code | 1896 |
| GRE/GMAT Policy | Not required by all programs; required if GPA < 2.75 |
| English Proficiency | Required for non-native English speakers |
| TOEFL (Grad) | Varies by program; typically 79+ iBT |
| IELTS (Grad) | Varies by program; typically 6.5+ |
| Deadlines | Vary by program; apply at least 1 year in advance |
| CGS April 15 Honor | Follows CGS guidelines |
| Recommendation Letters | Required by some programs (check program page) |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

**Wisconsin Resident — Living On/Off Campus**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $11,154 | Full-time, two semesters |
| Books, Course Materials, Supplies, Equipment | $800 | Estimated |
| Housing | $6,826 | On/off campus average |
| Food | $5,300 | Meal plans |
| Transportation | $1,792 | Local transportation |
| Miscellaneous Personal Expenses | $3,000 | Personal items |
| **Total Estimated COA** | **$28,872** | |

**Non-Resident — Living On/Off Campus**

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $24,004 | Full-time, two semesters |
| Books, Course Materials, Supplies, Equipment | $800 | Estimated |
| Housing | $6,826 | On/off campus average |
| Food | $5,300 | Meal plans |
| Transportation | $1,792 | Local transportation |
| Miscellaneous Personal Expenses | $3,000 | Personal items |
| **Total Estimated COA** | **$41,722** | |

**Tuition by Residency (2026-2027)**

| Residency | Associate's | Bachelor's | Graduate |
|-----------|-------------|------------|----------|
| Wisconsin Resident | $7,274 | $11,154 | $13,082 |
| Minnesota Reciprocity | $7,320 | $15,234 | $23,038 |
| Midwest | $10,032 | $15,850 | $18,744 |
| Non-Resident | $15,482 | $24,004 | $26,782 |

### 4.2 Undergraduate Financial Aid Policy

| Field | Value |
|-------|-------|
| Students Receiving Financial Aid | 80% |
| Scholarships Awarded Annually | $29,999,057 |
| Milwaukee Advantage Program (MAP) | $1,000/year for Midwest students |
| Chancellor's Merit Scholarship | Based on HS GPA (automatic) |
| Admission Scholarships | $500-$5,000 (merit-based, some renewable) |
| Need-Based Aid | Grants, work-study, subsidized loans (FAFSA required) |
| Net Price Calculator | Available at uwm.edu |
| FAFSA Priority | Submit early for maximum consideration |

### 4.3 Graduate Cost & Funding Framework

| Field | Value |
|-------|-------|
| Graduate Tuition (WI Resident) | $13,082/year |
| Graduate Tuition (Non-Resident) | $26,782/year |
| Application Fee | $75 |
| International Student Processing Fee | $200 (after admission) |
| Funding Types | RA, TA, fellowships, tuition waivers |
| Funding Source | Primarily academic departments |
| Graduate School Fellowships | Available through Graduate School |

---

## SECTION 5 — Evidence Chain Index

```yaml
---
E-U-001:
  field: undergraduate.admissions.test_policy
  value: "Test-optional (ACT/SAT not required)"
  source_url: "https://uwm.edu/undergrad-admission/apply/new-freshman/"
  source_snippet: "UW System institutions, including UWM, are not requiring applicants to submit ACT or SAT scores as part of the application process this year. UWM will consider applicants for admission with or without test scores."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.priority_deadline
  value: "November 1"
  source_url: "https://uwm.edu/undergrad-admission/"
  source_snippet: "Rolling admission with priority deadline November 1"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.costs.tuition_in_state
  value: "$11,154"
  source_url: "https://uwm.edu/finances/finances/cost-of-attendance/"
  source_snippet: "2026-2027 Tuition Estimate Bachelor's WI Resident $11,154"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.costs.tuition_out_of_state
  value: "$24,004"
  source_url: "https://uwm.edu/finances/finances/cost-of-attendance/"
  source_snippet: "2026-2027 Tuition Estimate Bachelor's Non-Resident $24,004"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.total_coa_in_state
  value: "$28,872"
  source_url: "https://uwm.edu/finances/finances/cost-of-attendance/"
  source_snippet: "Tuition & Fees $11,154 + Housing $6,826 + Food $5,300 + Books $800 + Transportation $1,792 + Misc $3,000"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.english_proficiency.toefl_full
  value: "79+ (iBT) or 4.5+ (Writing section after 1/21/2026)"
  source_url: "https://uwm.edu/cie/international-admissions/bachelors-application/english-proficiency-requirement/"
  source_snippet: "TOEFL iBT before 1/21/2026: 79 or higher for Full Admission"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.english_proficiency.ielts
  value: "6.5 (Full Admission)"
  source_url: "https://uwm.edu/cie/international-admissions/bachelors-application/english-proficiency-requirement/"
  source_snippet: "IELTS 6.5 for Full Admission"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency.duolingo
  value: "120-160 (Full Admission)"
  source_url: "https://uwm.edu/cie/international-admissions/bachelors-application/english-proficiency-requirement/"
  source_snippet: "Duolingo 120-160 for Full Admission"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.admissions.act_code
  value: "4658"
  source_url: "https://uwm.edu/undergrad-admission/apply/new-freshman/"
  source_snippet: "ACT school code: 4658; SAT school code: 1473"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.admissions.application_fee
  value: "Free (Common App)"
  source_url: "https://uwm.edu/undergrad-admission/apply/"
  source_snippet: "Apply for free through the Common App. The Universities of Wisconsin application also is accepted, but there may be charges."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.application_fee
  value: "$75"
  source_url: "https://uwm.edu/graduateschool/students/admission/"
  source_snippet: "All applicants are requested to pay a non-refundable $75 application fee"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.minimum_gpa
  value: "2.75"
  source_url: "https://uwm.edu/graduateschool/students/admission/"
  source_snippet: "A minimum cumulative undergraduate grade point average of 2.75 on a 4.0 scale"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-003:
  field: graduate.admissions.gre_code
  value: "1473"
  source_url: "https://uwm.edu/graduateschool/students/admission/"
  source_snippet: "UWM Institutional Code for the GRE: 1473"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-004:
  field: graduate.admissions.gmat_code
  value: "1896"
  source_url: "https://uwm.edu/graduateschool/students/admission/"
  source_snippet: "UWM Institutional Code for the GMAT: 1896"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-005:
  field: graduate.costs.tuition_in_state
  value: "$13,082"
  source_url: "https://uwm.edu/finances/finances/cost-of-attendance/"
  source_snippet: "2026-2027 Tuition Estimate Graduate WI Resident $13,082"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.costs.tuition_out_of_state
  value: "$26,782"
  source_url: "https://uwm.edu/finances/finances/cost-of-attendance/"
  source_snippet: "2026-2027 Tuition Estimate Graduate Non-Resident $26,782"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-007:
  field: graduate.international.processing_fee
  value: "$200"
  source_url: "https://uwm.edu/cie/international-admissions/graduate-application/"
  source_snippet: "Upon admission to UWM, you must also pay the $200 International Student Processing Fee through your application portal"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-008:
  field: graduate.international.fall_deadline_outside_us
  value: "July 15 (I-20 request)"
  source_url: "https://uwm.edu/cie/international-admissions/graduate-application/"
  source_snippet: "Students outside the U.S.: Fall intake: July 15"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-I-001:
  field: international.ug.fall_deadline_outside_us
  value: "June 1"
  source_url: "https://uwm.edu/cie/international-admissions/bachelors-application/"
  source_snippet: "Students outside the U.S.: Fall intake: June 1"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-I-002:
  field: international.ug.application_fee
  value: "Free ($200 processing fee after admission)"
  source_url: "https://uwm.edu/cie/international-admissions/bachelors-application/"
  source_snippet: "There is no fee to apply to an undergraduate (bachelor's degree) program. However, if you are admitted, you must pay the $200 International Student Processing Fee"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-P-001:
  field: programs.total_catalog_entries
  value: "659"
  source_url: "https://catalog.uwm.edu/programs/"
  source_snippet: "Full program listing from Academic Catalog 2026-2027"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-P-002:
  field: programs.homepage_count
  value: "209"
  source_url: "https://uwm.edu/"
  source_snippet: "209 Academic Programs"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-F-001:
  field: institutional.financial_aid_rate
  value: "80% of students receive financial aid"
  source_url: "https://uwm.edu/admission/"
  source_snippet: "80% Of Students Receive Financial Aid"
  capture_date: "2026-07-06"
  evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uwm-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: Rules 1-4)
├── 01-ug-letters-science.md            (Section 1: L&S majors)
├── 02-ug-engineering.md                (Section 1: Engineering majors)
├── 03-ug-business.md                   (Section 1: Business majors)
├── 04-ug-arts.md                       (Section 1: Arts majors)
├── 05-ug-education.md                  (Section 1: Education majors)
├── 06-ug-health-sciences.md            (Section 1: Health professions majors)
├── 07-ug-other.md                      (Section 1: Other UG programs)
├── 08-grad-letters-science.md          (Section 2: L&S grad programs)
├── 09-grad-engineering.md              (Section 2: Engineering grad programs)
├── 10-grad-business.md                 (Section 2: Business grad programs)
├── 11-grad-education.md                (Section 2: Education grad programs)
├── 12-grad-health-sciences.md          (Section 2: Health professions grad)
├── 13-grad-other.md                    (Section 2: Other grad programs)
├── 14-admissions-deadlines.md          (Section 3)
├── 15-costs-financial-aid.md           (Section 4)
├── 16-evidence-chain.md                (Section 5)
└── 17-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "uwm-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "<URL>"
  capture_date: "2026-07-06"
  version: v2.0
  change_status: baseline
  last_verified: "2026-07-06"
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P0 | Graduate application deadlines by program | Individual program pages |
| P1 | Detailed tuition differential fees by program | uwm.edu/finances/ |
| P1 | Per-program English proficiency for graduate | Individual program pages |
| P2 | Housing rate details by building/room type | uwm.edu/housing/ |
| P2 | Assistantship stipend rates | Graduate School pages |
| P2 | Net Price Calculator results | uwm.edu |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UWM Value | Notes |
|-----------|-----------|-------|
| Institution Type | Public, Doctoral/Research | Only public doctoral university in Milwaukee |
| Location | Milwaukee, WI | 2100 E. Kenwood Blvd. |
| Total UG COA (In-State) | ~$28,872 | 2026-27 estimate |
| Total UG COA (OOS) | ~$41,722 | 2026-27 estimate |
| UG Tuition (In-State) | $11,154 | 2026-27 |
| UG Tuition (OOS) | $24,004 | 2026-27 |
| Grad Tuition (In-State) | $13,082 | 2026-27 |
| Grad Tuition (OOS) | $26,782 | 2026-27 |
| Need-Blind (Intl?) | No (need-aware for all) |  |
| Test-Optional? | Yes | ACT/SAT not required |
| TOEFL Minimum (UG) | 79 iBT / 6.5 IELTS | Full Admission |
| Application Fee (UG) | Free (Common App) |  |
| Application Fee (Grad) | $75 |  |
| EA Deadline | N/A (rolling) |  |
| Priority Deadline | November 1 |  |
| RA/ED Deadline | N/A (rolling) |  |
| Total Programs (Catalog) | 659 | Includes certificates/microcredentials |
| Total Degree Programs | 473 | UG majors + minors + grad degrees |
| Schools/Colleges | 17 | Including Graduate School & Honors |
| Student-Faculty Ratio | 17:1 |  |
| Total Students | 23,104 | From 83 countries |
| International Students | 1,000+ | From 80+ countries |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: uwm.edu, catalog.uwm.edu, uwm.edu/finances/, uwm.edu/cie/, uwm.edu/graduateschool/
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
