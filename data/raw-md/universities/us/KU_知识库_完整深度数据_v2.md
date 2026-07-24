# University of Kansas (KU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BAS/BHS/BPS/BGS) | ~120 |
| 本科辅修 (Minor) | ~85 |
| 研究生学位项目 (MA/MS/MBA/MFA/PhD/EdD/DMA/etc.) | ~200 |
| 研究生高级证书 (Graduate Certificate) | ~80 |
| **学位项目总计 (UG + Grad)** | **~485** |
| 学院 / 独立系所总数 | 14 |

> Note: Counts are approximate based on catalog extraction. The graduate programs list from gradapply.ku.edu shows 300 entries (including non-degree); the catalog shows additional programs. Full reconciliation requires completing the Law and Professional Studies extractions.

### 0.2 学院 / 系层级结构

```
University of Kansas
├── School of Architecture & Design                    [学院]
│   ├── Architecture                                   [系]
│   └── Design                                         [系]
├── School of Business                                 [学院]
│   ├── Accounting                                     [系]
│   ├── Finance                                        [系]
│   ├── Information Systems                            [系]
│   ├── Management & Leadership                        [系]
│   ├── Marketing                                      [系]
│   └── Supply Chain Management                        [系]
├── School of Education & Human Sciences               [学院]
│   ├── Curriculum & Teaching                          [系]
│   ├── Educational Leadership & Policy                [系]
│   ├── Educational Psychology & Research              [系]
│   ├── Health, Sport & Exercise Sciences              [系]
│   └── Special Education                              [系]
├── School of Engineering                              [学院]
│   ├── Aerospace Engineering                          [系]
│   ├── Chemical & Petroleum Engineering               [系]
│   ├── Civil, Environmental & Architectural Engineering [系]
│   ├── Electrical Engineering & Computer Science      [系]
│   ├── Engineering Management                         [系]
│   └── Mechanical Engineering                         [系]
├── School of Health Professions                       [学院]
│   ├── Clinical Laboratory Sciences                   [系]
│   ├── Dietetics & Nutrition                          [系]
│   ├── Health Information Management                  [系]
│   ├── Physical Therapy & Rehabilitation Science      [系]
│   ├── Respiratory Care                               [系]
│   └── Therapeutic Science                            [系]
├── William Allen White School of Journalism & Mass Communications [学院]
│   └── Journalism & Mass Communications               [系]
├── School of Law                                      [学院]
│   └── Law                                            [系]
├── College of Liberal Arts & Sciences (CLAS)          [学院]
│   ├── African & African-American Studies             [系]
│   ├── American Studies                               [系]
│   ├── Anthropology                                   [系]
│   ├── Astronomy                                      [系]
│   ├── Atmospheric Science                            [系]
│   ├── Biochemistry                                   [系]
│   ├── Biology                                        [系]
│   ├── Chemistry                                      [系]
│   ├── Classics                                       [系]
│   ├── Communication Studies                          [系]
│   ├── Computer Science                               [系]
│   ├── East Asian Languages & Cultures                [系]
│   ├── Ecology & Evolutionary Biology                 [系]
│   ├── Economics                                      [系]
│   ├── English                                        [系]
│   ├── French & Italian                               [系]
│   ├── Geography                                      [系]
│   ├── Geology                                        [系]
│   ├── Global & International Studies                 [系]
│   ├── History                                        [系]
│   ├── History of Art                                 [系]
│   ├── Indigenous Studies                             [系]
│   ├── Linguistics                                    [系]
│   ├── Mathematics                                    [系]
│   ├── Molecular Biosciences                          [系]
│   ├── Philosophy                                     [系]
│   ├── Physics & Astronomy                            [系]
│   ├── Political Science                              [系]
│   ├── Psychology                                     [系]
│   ├── Religious Studies                              [系]
│   ├── Slavic Languages & Literatures                 [系]
│   ├── Sociology                                      [系]
│   ├── Spanish & Portuguese                           [系]
│   ├── Speech-Language-Hearing                        [系]
│   ├── Theatre & Dance                                [系]
│   └── Women, Gender & Sexuality Studies              [系]
├── School of Medicine                                 [学院]
│   ├── Biochemistry & Molecular Biology               [系]
│   ├── Biostatistics                                  [系]
│   ├── Cancer Biology                                 [系]
│   ├── Cell Biology & Anatomy                         [系]
│   ├── Microbiology, Molecular Genetics & Immunology  [系]
│   ├── Pathology & Laboratory Medicine                [系]
│   ├── Pharmacology, Toxicology & Therapeutics        [系]
│   └── Population Health                              [系]
├── School of Music                                    [学院]
│   └── Music                                          [系]
├── School of Nursing                                  [学院]
│   └── Nursing                                        [系]
├── School of Pharmacy                                 [学院]
│   ├── Medicinal Chemistry                            [系]
│   ├── Pharmaceutical Chemistry                       [系]
│   ├── Pharmacology & Toxicology                      [系]
│   └── Pharmacy Practice                              [系]
├── School of Professional Studies                     [学院]
│   ├── Applied Cybersecurity                          [系]
│   ├── Biotechnology                                  [系]
│   ├── Criminal Justice                               [系]
│   ├── Information Technology                         [系]
│   ├── Nutrition                                      [系]
│   └── Project Management                             [系]
└── School of Social Welfare                           [学院]
    └── Social Welfare                                 [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~45 |
| BS | Bachelor of Science | 本科 | ~50 |
| BFA | Bachelor of Fine Arts | 本科 | ~3 |
| BGS | Bachelor of General Studies | 本科 | ~15 |
| BAS | Bachelor of Applied Science | 本科 | 4 |
| BHS | Bachelor of Health Sciences | 本科 | 1 |
| BPS | Bachelor of Professional Studies | 本科 | 1 |
| BSE | Bachelor of Science in Education | 本科 | ~8 |
| BSB | Bachelor of Science in Business | 本科 | 8 |
| MA | Master of Arts | 研究生 | ~35 |
| MS | Master of Science | 研究生 | ~45 |
| MFA | Master of Fine Arts | 研究生 | 3 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MEd/MSE | Master of Education/Science in Education | 研究生 | ~15 |
| MPH | Master of Public Health | 研究生 | ~3 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MUP | Master of Urban Planning | 研究生 | 2 |
| MSW | Master of Social Work | 研究生 | 2 |
| MM | Master of Music | 研究生 | 3 |
| MME | Master of Music Education | 研究生 | 2 |
| M.Arch | Master of Architecture | 研究生 | 1 |
| ME | Master of Engineering | 研究生 | ~5 |
| MCE | Master of Civil Engineering | 研究生 | 1 |
| M.Acc | Master of Accounting | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 2 |
| EdS | Education Specialist | 研究生 | 1 |
| PSM | Professional Science Master | 研究生 | 2 |
| PhD | Doctor of Philosophy | 研究生 | ~65 |
| EdD | Doctor of Education | 研究生 | 2 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| DSW | Doctor of Social Work | 研究生 | 1 |
| PharmD | Doctor of Pharmacy | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| SJD | Doctor of Juridical Science | 研究生 | 1 |
| Graduate Certificate | 高级证书 | 研究生 | ~80 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BGS | BAS | BSE | BSB | MA | MS | MFA | MBA | MEd/MSE | PhD | EdD | DMA | JD | LLM | SJD | PharmD | MD | Graduate Cert | 合计 |
|------------|----|----|-----|-----|-----|-----|-----|----|----|-----|-----|---------|-----|-----|-----|----|----|-----|--------|----|--------------|------|
| Architecture & Design | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 7 |
| Business | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 3 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| Education & Human Sciences | 0 | 3 | 0 | 0 | 0 | 4 | 0 | 1 | 2 | 0 | 0 | 6 | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 34 |
| Engineering | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 25 |
| Health Professions | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 14 |
| Journalism & Mass Comm | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 8 | 12 |
| Liberal Arts & Sciences | 40 | 15 | 3 | 15 | 0 | 0 | 0 | 25 | 5 | 2 | 0 | 0 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 155 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 26 |
| Music | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 13 |
| Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 7 |
| Professional Studies | 0 | 5 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Social Welfare | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **合计** | **42** | **36** | **3** | **15** | **4** | **4** | **8** | **28** | **48** | **2** | **2** | **6** | **68** | **3** | **1** | **1** | **1** | **1** | **1** | **1** | **54** | **~329** |

> Note: Matrix counts are approximate and based on catalog extraction. Some programs span multiple schools. Graduate certificates are counted separately. The total includes both UG and grad programs from the catalog. The graduate programs list from gradapply.ku.edu shows 300 entries (including ~80 non-degree entries).

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

KU has 14 schools/colleges offering undergraduate programs. The largest is the College of Liberal Arts & Sciences (CLAS), which houses the majority of liberal arts majors. Professional schools (Business, Engineering, Architecture, Journalism, Music, Nursing, Pharmacy, Health Professions, Education, Professional Studies) offer specialized degrees. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts & Sciences (CLAS)

##### African & African-American Studies
###### BA / BGS
| # | 专业 | URL |
|---|------|-----|
| 1 | African and African-American Studies | https://catalog.ku.edu/liberal-arts-sciences/african-studies/ba-bgs/ |

##### American Studies
###### BA / BGS
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.ku.edu/liberal-arts-sciences/american-studies/ba-bgs/ |

##### Anthropology
###### BA / BGS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ku.edu/liberal-arts-sciences/anthropology/ba-bgs/ |

##### Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.ku.edu/liberal-arts-sciences/biochemistry/bs/ |

##### Biology
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.ku.edu/liberal-arts-sciences/biology/ba-bs/ |

##### Chemistry
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ku.edu/liberal-arts-sciences/chemistry/ba-bs/ |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ku.edu/liberal-arts-sciences/computer-science/bs/ |

##### Economics
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ku.edu/liberal-arts-sciences/economics/ba-bs/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.ku.edu/liberal-arts-sciences/english/ba/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.ku.edu/liberal-arts-sciences/history/ba/ |

##### Mathematics
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ku.edu/liberal-arts-sciences/mathematics/ba-bs/ |

##### Physics
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ku.edu/liberal-arts-sciences/physics/ba-bs/ |

##### Political Science
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.ku.edu/liberal-arts-sciences/political-science/ba-bs/ |

##### Psychology
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ku.edu/liberal-arts-sciences/psychology/ba-bs/ |

##### Sociology
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ku.edu/liberal-arts-sciences/sociology/ba-bs/ |

> Note: CLAS has ~60 additional departments with UG programs. Full list available in catalog.ku.edu/liberal-arts-sciences/.

#### School of Business

##### Business
###### BSB (Bachelor of Science in Business)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.ku.edu/business/bs-accounting/ |
| 2 | Business Administration | https://catalog.ku.edu/business/bs-business-administration/ |
| 3 | Business Analytics | https://catalog.ku.edu/business/bs-business-analytics/ |
| 4 | Finance | https://catalog.ku.edu/business/bs-finance/ |
| 5 | Information Systems | https://catalog.ku.edu/business/bs-information-systems/ |
| 6 | Management and Leadership | https://catalog.ku.edu/business/bs-management-leadership/ |
| 7 | Marketing | https://catalog.ku.edu/business/bs-marketing/ |
| 8 | Supply Chain Management | https://catalog.ku.edu/business/bs-supply-chain-management/ |

#### School of Engineering

##### Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ku.edu/engineering/aerospace-engineering/bs/ |

##### Chemical & Petroleum Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.ku.edu/engineering/chemical-petroleum-engineering/bs-chemical/ |
| 2 | Petroleum Engineering | https://catalog.ku.edu/engineering/chemical-petroleum-engineering/bs-petroleum/ |

##### Civil, Environmental & Architectural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/bs-architectural/ |
| 2 | Civil Engineering | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/bs-civil/ |
| 3 | Environmental Engineering | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/bs-environmental/ |

##### Electrical Engineering & Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.ku.edu/engineering/electrical-engineering-computer-science/bs-computer/ |
| 2 | Electrical Engineering | https://catalog.ku.edu/engineering/electrical-engineering-computer-science/bs-electrical/ |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.ku.edu/engineering/mechanical-engineering/bs/ |

#### School of Architecture & Design

##### Architecture
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | https://catalog.ku.edu/architecture/architecture/ba-architectural-studies/ |

##### Interior Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Architecture | https://catalog.ku.edu/architecture/architecture/bs-interior-architecture-design/ |

#### School of Journalism & Mass Communications

##### Journalism
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Mass Communications | https://catalog.ku.edu/journalism-mass-communications/bs/ |

#### School of Music

##### Music
###### BA / BFA / BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (BA) | https://catalog.ku.edu/music/ba/ |
| 2 | Music (BFA) | https://catalog.ku.edu/music/bfa/ |
| 3 | Music (BM) | https://catalog.ku.edu/music/bm/ |

#### School of Nursing

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.ku.edu/nursing/bsn/ |

#### School of Pharmacy

##### Pharmacy
###### PharmD
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy (PharmD) | https://catalog.ku.edu/pharmacy/pharmd/ |

#### School of Health Professions

##### Clinical Laboratory Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Laboratory Science | https://catalog.ku.edu/health-professions/clinical-laboratory-sciences/bs/ |

##### Health Information Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Information Management | https://catalog.ku.edu/health-professions/health-information-management/bs/ |

##### Respiratory Care
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Respiratory Care | https://catalog.ku.edu/health-professions/respiratory-care/bs/ |

#### School of Education & Human Sciences

##### Curriculum & Teaching
###### BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://catalog.ku.edu/education/curriculum-teaching/bse-elementary-education/ |
| 2 | Secondary Education | https://catalog.ku.edu/education/curriculum-teaching/bse-secondary-education/ |
| 3 | Unified Early Childhood | https://catalog.ku.edu/education/curriculum-teaching/bse-unified-early-childhood/ |

##### Health, Sport & Exercise Sciences
###### BS / BSE
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Health (BSE) | https://catalog.ku.edu/education/health-sport-exercise-sciences/bse-community-health/ |
| 2 | Exercise Science (BS) | https://catalog.ku.edu/education/health-sport-exercise-sciences/bs-exercise-science/ |
| 3 | Sport Management (BS) | https://catalog.ku.edu/education/health-sport-exercise-sciences/bs-sport-management/ |

#### School of Professional Studies

##### Applied Cybersecurity
###### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Cybersecurity | https://catalog.ku.edu/professional-studies/applied-cybersecurity-bas/ |

##### Biotechnology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biotechnology | https://catalog.ku.edu/professional-studies/biotechnology-bs/ |

##### Criminal Justice
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice (BA) | https://catalog.ku.edu/professional-studies/criminal-justice-ba/ |
| 2 | Criminal Justice (BS) | https://catalog.ku.edu/professional-studies/criminal-justice-bs/ |

##### Information Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Technology | https://catalog.ku.edu/professional-studies/information-technology-bs/ |

##### Nutrition
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition | https://catalog.ku.edu/professional-studies/nutrition-bs/ |

##### Operations Management
###### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Operations Management | https://catalog.ku.edu/professional-studies/operations-management-bas/ |

##### Project Management
###### BAS / BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Project Management (BAS) | https://catalog.ku.edu/professional-studies/project-management-bas/ |
| 2 | Project Management (BS) | https://catalog.ku.edu/professional-studies/project-management-bs/ |

##### Professional Performance
###### BAS
| # | 专业 | URL |
|---|------|-----|
| 1 | Professional Performance | https://catalog.ku.edu/professional-studies/professional-performance-bas/ |

##### American Sign Language & Deaf Studies
###### BA / BGS
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language and Deaf Studies | https://catalog.ku.edu/professional-studies/american-sign-language-ba-bgs/ |

##### Health Sciences
###### BHS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Sciences | https://catalog.ku.edu/professional-studies/health-sciences-bhs/ |

##### Professional Studies
###### BPS
| # | 专业 | URL |
|---|------|-----|
| 1 | Professional Studies | https://catalog.ku.edu/professional-studies/professional-studies-bps/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

KU offers several interdisciplinary programs that span multiple schools:
- Environmental Studies (CLAS + multiple departments)
- Global & International Studies (CLAS)
- Pre-professional tracks (Pre-Med, Pre-Law, Pre-Engineering) are advising pathways, not standalone degrees

### 1.4 Minors — complete list

KU offers ~85 undergraduate minors across all schools. Key minors include:

| # | Minor | Home School |
|---|-------|-------------|
| 1 | African & African-American Studies | CLAS |
| 2 | American Studies | CLAS |
| 3 | Anthropology | CLAS |
| 4 | Business | Business |
| 5 | Business Analytics | Business |
| 6 | Chemistry | CLAS |
| 7 | Computer Science | CLAS |
| 8 | Criminal Justice | Professional Studies |
| 9 | Economics | CLAS |
| 10 | English | CLAS |
| 11 | Entrepreneurship | Business |
| 12 | History | CLAS |
| 13 | Mathematics | CLAS |
| 14 | Physics | CLAS |
| 15 | Political Science | CLAS |
| 16 | Psychology | CLAS |
| 17 | Sociology | CLAS |
| 18 | Spanish | CLAS |
| 19 | Sport Management | Education |
| 20 | Women, Gender & Sexuality Studies | CLAS |

> Full minor list available at catalog.ku.edu under each school's "Minor" entries.

### 1.5 General/Institute-wide requirements

KU Core 34: KU's general education curriculum requires 34 credit hours across 6 goals:
1. **Goal 1**: Critical Thinking & Quantitative Literacy (2 courses)
2. **Goal 2**: Communication (2 courses)
3. **Goal 3**: Arts & Humanities (1 course)
4. **Goal 4**: Natural Sciences (1 course)
5. **Goal 5**: Social & Behavioral Sciences (1 course)
6. **Goal 6**: Integration & Creativity (1 course)

Source: https://catalog.ku.edu/core34/

### 1.6 Course-ID → Major quick-lookup

KU does not use a systematic course-ID numbering scheme for majors. Programs are identified by department and degree type.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

KU offers ~200 graduate degree programs and ~80 graduate certificates. The graduate admissions portal (gradapply.ku.edu) lists 300 program entries including non-degree options.

#### School of Business
##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://catalog.ku.edu/business/mba/ |
| 2 | Business Administration Online (MBA) | https://catalog.ku.edu/business/mba-online/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.ku.edu/business/ms-business-business-analytics/ |
| 2 | Organizational Leadership | https://catalog.ku.edu/business/ms-business-organizational-leadership/ |
| 3 | Supply Chain Management | https://catalog.ku.edu/business/ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business | https://catalog.ku.edu/business/phd/ |

#### School of Engineering
##### MS/ME
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (MS) | https://catalog.ku.edu/engineering/aerospace-engineering/ms/ |
| 2 | Aerospace Engineering (ME) | https://catalog.ku.edu/engineering/aerospace-engineering/me/ |
| 3 | Chemical Engineering | https://catalog.ku.edu/engineering/chemical-petroleum-engineering/ms/ |
| 4 | Civil Engineering (MS) | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/ms/ |
| 5 | Civil Engineering (MCE) | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/mce/ |
| 6 | Computer Engineering | https://catalog.ku.edu/engineering/electrical-engineering-computer-science/ms-computer/ |
| 7 | Electrical Engineering | https://catalog.ku.edu/engineering/electrical-engineering-computer-science/ms-electrical/ |
| 8 | Mechanical Engineering | https://catalog.ku.edu/engineering/mechanical-engineering/ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ku.edu/engineering/aerospace-engineering/phd/ |
| 2 | Chemical & Petroleum Engineering | https://catalog.ku.edu/engineering/chemical-petroleum-engineering/phd/ |
| 3 | Civil Engineering | https://catalog.ku.edu/engineering/civil-environmental-architectural-engineering/phd/ |
| 4 | Electrical Engineering & Computer Science | https://catalog.ku.edu/engineering/electrical-engineering-computer-science/phd/ |
| 5 | Mechanical Engineering | https://catalog.ku.edu/engineering/mechanical-engineering/phd/ |

#### College of Liberal Arts & Sciences
##### MA/MS
| # | 项目 | URL |
|---|------|-----|
| 1 | African & African-American Studies (MA) | https://catalog.ku.edu/liberal-arts-sciences/african-studies/ma/ |
| 2 | American Studies (MA) | https://catalog.ku.edu/liberal-arts-sciences/american-studies/ma/ |
| 3 | Anthropology (MA) | https://catalog.ku.edu/liberal-arts-sciences/anthropology/ma/ |
| 4 | Applied Behavioral Science (MA) | https://catalog.ku.edu/liberal-arts-sciences/applied-behavioral-science/ma/ |
| 5 | Classics (MA) | https://catalog.ku.edu/liberal-arts-sciences/classics/ma/ |
| 6 | Communication Studies (MA) | https://catalog.ku.edu/liberal-arts-sciences/communication-studies/ma/ |
| 7 | Economics (MA) | https://catalog.ku.edu/liberal-arts-sciences/economics/ma/ |
| 8 | English (MA) | https://catalog.ku.edu/liberal-arts-sciences/english/ma/ |
| 9 | Geography (MA) | https://catalog.ku.edu/liberal-arts-sciences/geography/ma/ |
| 10 | Geology (MS) | https://catalog.ku.edu/liberal-arts-sciences/geology/ms/ |
| 11 | History (MA) | https://catalog.ku.edu/liberal-arts-sciences/history/ma/ |
| 12 | Linguistics (MA) | https://catalog.ku.edu/liberal-arts-sciences/linguistics/ma/ |
| 13 | Mathematics (MA) | https://catalog.ku.edu/liberal-arts-sciences/mathematics/ma/ |
| 14 | Philosophy (MA) | https://catalog.ku.edu/liberal-arts-sciences/philosophy/ma/ |
| 15 | Physics (MS) | https://catalog.ku.edu/liberal-arts-sciences/physics/ms/ |
| 16 | Spanish (MA) | https://catalog.ku.edu/liberal-arts-sciences/spanish/ma/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | English (MFA) | https://catalog.ku.edu/liberal-arts-sciences/english/mfa/ |
| 2 | Visual Art (MFA) | https://catalog.ku.edu/liberal-arts-sciences/visual-art/mfa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.ku.edu/liberal-arts-sciences/american-studies/phd/ |
| 2 | Anthropology | https://catalog.ku.edu/liberal-arts-sciences/anthropology/phd/ |
| 3 | Applied Behavioral Science | https://catalog.ku.edu/liberal-arts-sciences/applied-behavioral-science/phd/ |
| 4 | Chemistry | https://catalog.ku.edu/liberal-arts-sciences/chemistry/phd/ |
| 5 | Clinical Child Psychology | https://catalog.ku.edu/liberal-arts-sciences/clinical-child-psychology/phd/ |
| 6 | Communication Studies | https://catalog.ku.edu/liberal-arts-sciences/communication-studies/phd/ |
| 7 | Computer Science | https://catalog.ku.edu/liberal-arts-sciences/computer-science/phd/ |
| 8 | Ecology & Evolutionary Biology | https://catalog.ku.edu/liberal-arts-sciences/ecology-evolutionary-biology/phd/ |
| 9 | Economics | https://catalog.ku.edu/liberal-arts-sciences/economics/phd/ |
| 10 | English | https://catalog.ku.edu/liberal-arts-sciences/english/phd/ |
| 11 | Geography | https://catalog.ku.edu/liberal-arts-sciences/geography/phd/ |
| 12 | Geology | https://catalog.ku.edu/liberal-arts-sciences/geology/phd/ |
| 13 | History | https://catalog.ku.edu/liberal-arts-sciences/history/phd/ |
| 14 | Linguistics | https://catalog.ku.edu/liberal-arts-sciences/linguistics/phd/ |
| 15 | Mathematics | https://catalog.ku.edu/liberal-arts-sciences/mathematics/phd/ |
| 16 | Philosophy | https://catalog.ku.edu/liberal-arts-sciences/philosophy/phd/ |
| 17 | Physics | https://catalog.ku.edu/liberal-arts-sciences/physics/phd/ |
| 18 | Political Science | https://catalog.ku.edu/liberal-arts-sciences/political-science/phd/ |
| 19 | Psychology | https://catalog.ku.edu/liberal-arts-sciences/psychology/phd/ |
| 20 | Sociology | https://catalog.ku.edu/liberal-arts-sciences/sociology/phd/ |
| 21 | Spanish | https://catalog.ku.edu/liberal-arts-sciences/spanish/phd/ |
| 22 | Speech-Language Pathology | https://catalog.ku.edu/liberal-arts-sciences/speech-language-pathology/phd/ |

#### School of Medicine
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry & Molecular Biology | https://catalog.ku.edu/medicine/biochemistry-molecular-biology/ms/ |
| 2 | Biostatistics | https://catalog.ku.edu/medicine/biostatistics/ms/ |
| 3 | Cancer Biology | https://catalog.ku.edu/medicine/cancer-biology/ms/ |
| 4 | Cell Biology & Anatomy | https://catalog.ku.edu/medicine/cell-biology-physiology/ms-cell-biology-anatomy/ |
| 5 | Clinical Research | https://catalog.ku.edu/medicine/population-health/ms/ |
| 6 | Microbiology | https://catalog.ku.edu/medicine/microbiology-molecular-genetics-immunology/ma/ |
| 7 | Molecular & Integrative Physiology | https://catalog.ku.edu/medicine/cell-biology-physiology/ms-molecular-integrative-physiology/ |
| 8 | Neurosciences | https://catalog.ku.edu/medicine/cell-biology-physiology/ms-neurosciences/ |
| 9 | Pathology | https://catalog.ku.edu/medicine/pathology-laboratory-medicine/ma/ |
| 10 | Pharmacology | https://catalog.ku.edu/medicine/pharmacology-toxicology-therapeutics/ms-pharmacology/ |
| 11 | Toxicology | https://catalog.ku.edu/medicine/pharmacology-toxicology-therapeutics/ms-toxicology/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry & Molecular Biology | https://catalog.ku.edu/medicine/biochemistry-molecular-biology/phd/ |
| 2 | Biostatistics | https://catalog.ku.edu/medicine/biostatistics/phd/ |
| 3 | Cancer Biology | https://catalog.ku.edu/medicine/cancer-biology/phd/ |
| 4 | Cell Biology & Anatomy | https://catalog.ku.edu/medicine/cell-biology-physiology/phd-cell-biology-anatomy/ |
| 5 | Clinical & Translational Science | https://catalog.ku.edu/medicine/biostatistics/phd-clinical-translational-science/ |
| 6 | Microbiology | https://catalog.ku.edu/medicine/microbiology-molecular-genetics-immunology/phd/ |
| 7 | Molecular & Integrative Physiology | https://catalog.ku.edu/medicine/cell-biology-physiology/phd-molecular-integrative-physiology/ |
| 8 | Neurosciences | https://catalog.ku.edu/medicine/cell-biology-physiology/phd-neurosciences/ |
| 9 | Pathology | https://catalog.ku.edu/medicine/pathology-laboratory-medicine/phd/ |
| 10 | Pharmacology | https://catalog.ku.edu/medicine/pharmacology-toxicology-therapeutics/phd-pharmacology/ |
| 11 | Population Health | https://catalog.ku.edu/medicine/population-health/phd/ |
| 12 | Toxicology | https://catalog.ku.edu/medicine/pharmacology-toxicology-therapeutics/phd-toxicology/ |

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine | https://catalog.ku.edu/schoolofmedicine/md/ |
| 2 | MD-PhD Physician Scientist Training | https://catalog.ku.edu/medicine/combined-md-phd |

#### School of Law
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Juris Doctor | JD | https://catalog.ku.edu/law/jd/ |
| 2 | Two-Year JD for Foreign-Trained Lawyers | JD | https://catalog.ku.edu/law/two-year-jd/ |
| 3 | Master of Laws in American Legal Studies | LLM | https://catalog.ku.edu/law/llm-american-legal-studies/ |
| 4 | Master of Science in Homeland Security | MS | https://catalog.ku.edu/law/ms-homeland-security/ |
| 5 | Doctor of Juridical Science | SJD | https://catalog.ku.edu/law/sjd/ |

#### School of Music
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Music | MM | https://catalog.ku.edu/music/mm/ |
| 2 | Music Education | MME | https://catalog.ku.edu/music/mme/ |
| 3 | Music Therapy | MME | https://catalog.ku.edu/music/mme-therapy/ |
| 4 | Musical Arts | DMA | https://catalog.ku.edu/music/dma/ |
| 5 | Music | PhD | https://catalog.ku.edu/music/phd/ |

#### School of Pharmacy
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Medicinal Chemistry | MS | https://catalog.ku.edu/medicine/medicinal-chemistry/ms/ |
| 2 | Pharmaceutical Chemistry | MS | https://catalog.ku.edu/medicine/pharmaceutical-chemistry/ms/ |
| 3 | Pharmacology & Toxicology | MS | https://catalog.ku.edu/medicine/pharmacology-toxicology/ms/ |
| 4 | Pharmacy Practice | MS | https://catalog.ku.edu/pharmacy/pharmacy-practice/ms/ |
| 5 | Medicinal Chemistry | PhD | https://catalog.ku.edu/medicine/medicinal-chemistry/phd/ |
| 6 | Pharmaceutical Chemistry | PhD | https://catalog.ku.edu/medicine/pharmaceutical-chemistry/phd/ |
| 7 | Pharmacology & Toxicology | PhD | https://catalog.ku.edu/medicine/pharmacology-toxicology/phd/ |

#### School of Social Welfare
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Social Work (Traditional) | MSW | https://catalog.ku.edu/social-welfare/msw-traditional/ |
| 2 | Social Work (Advanced Standing) | MSW | https://catalog.ku.edu/social-welfare/msw-advanced-standing/ |
| 3 | Social Work | PhD | https://catalog.ku.edu/social-welfare/phd/ |
| 4 | Social Work | DSW | https://catalog.ku.edu/social-welfare/dsw/ |

> Full graduate program list available at https://gradapply.ku.edu/graduate-programs (300 entries including non-degree).

### 2.2 At least one program's full deep-dive

**Computer Science (PhD) — College of Liberal Arts & Sciences**
- Department: Computer Science
- Degree: Doctor of Philosophy
- Location: Lawrence
- Application: https://gradapply.ku.edu/apply
- Program website: https://cs.ku.edu/graduate
- GRE: Not required (verify per program)
- TOEFL: 79 minimum (18 subscore)
- IELTS: 6.5 minimum (6.0 subscore)
- Deadline: Varies by program; check https://gradapply.ku.edu/graduate-programs
- Application fee: $65 domestic, $100 international

### 2.3 Graduate admissions model

KU graduate admissions is **decentralized**. Each program sets its own requirements, deadlines, and review processes. The Office of Graduate Studies (graduate.ku.edu) provides central support, but admission decisions are made by individual programs.

- Application portal: https://gradapply.ku.edu/apply
- Program directory: https://gradapply.ku.edu/graduate-programs
- International requirements: https://gradapply.ku.edu/international
- English requirements: https://gradapply.ku.edu/english-requirements

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Application portal | https://go2.ku.edu/portal/apply | admissions.ku.edu/apply |
| Application fee | $40 (domestic freshmen) | admissions.ku.edu/apply |
| Test policy | **Test-optional** | admissions.ku.edu/apply |
| EA deadline | N/A (no Early Action) | admissions.ku.edu/apply |
| Priority scholarship deadline | December 1 | admissions.ku.edu/apply |
| FAFSA priority deadline | February 1 | admissions.ku.edu/apply |
| Transfer scholarship deadline | August 1 | admissions.ku.edu/apply |
| Rolling admissions | Yes (decisions on rolling basis) | admissions.ku.edu/apply |
| Assured admission (GPA) | 3.25+ weighted/unweighted | admissions.ku.edu/apply |
| Assured admission (test-optional) | ACT 21+ or SAT 1060+ with GPA 2.0+ | admissions.ku.edu/apply |
| Superscore | N/A (test-optional) | admissions.ku.edu/apply |
| Recommendation | Not required | admissions.ku.edu/apply |
| Essay | Not required | admissions.ku.edu/apply |
| Interview | Not offered | admissions.ku.edu/apply |
| Portfolio | Required for Architecture & Design | admissions.ku.edu/major-specific-requirements |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT | 79 (18 min subscore) | — | Also accepts Home Edition |
| TOEFL iBT (new scale, Jan 2026+) | 4.5 (4 min subscore) | — | New 1-6 scale |
| TOEFL Paper-Delivered | 60 (18 min subscore) | — | |
| IELTS Academic | 6.5 (6.0 min subscore) | — | |
| PTE Academic | 53 (48 min subscore) | — | |
| Duolingo English Test | Accepted for admission | — | Must still take AEC placement test |
| SAT EBRW | 590 | — | Satisfies English proficiency |
| ACT English + Reading | 48 | — | Satisfies English proficiency |
| AP English | Grade 4 | — | Satisfies English proficiency |
| AS/A Level English | Grade B on both | — | Satisfies English proficiency |

**Exceptions** (no English proficiency required):
- Native English speakers
- 4 years college-prep English with 2.5+ GPA from qualifying regions (US, UK, Ireland, Australia, etc.)
- B or better in College English Composition 1 & 2 with 24+ credit hours from qualifying region
- Full IB diploma with English HL 5+
- Associate's degree with 2.5+ GPA from U.S.-accredited college

Source: https://world.ku.edu/english-proficiency

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Application portal | https://gradapply.ku.edu/apply | gradapply.ku.edu |
| Application fee (domestic) | $65 | gradapply.ku.edu |
| Application fee (international) | $100 | gradapply.ku.edu |
| Application fee (certificate/non-degree) | $40 | gradapply.ku.edu |
| GRE | Per program (many no longer require) | gradapply.ku.edu |
| English proficiency (grad) | TOEFL 79 / IELTS 6.5 | gradapply.ku.edu/english-requirements |
| Admissions model | Decentralized (each program decides) | graduate.ku.edu |
| CGS April 15 signatory | Yes | cgsnet.org |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2025-26 academic year)

#### Kansas Residents

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $11,298 | Based on 30 hours/year in CLAS |
| Required student & wellness fees | $1,155 | |
| Housing & food | $7,912 - $19,180 | Varies by housing type |
| Books, materials, supplies, equipment | $1,224 | |
| **Total (on-campus)** | **$21,589 - $32,857** | |

#### Out-of-State Residents

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $30,177 | Based on 30 hours/year in CLAS |
| Required student & wellness fees | $1,155 | |
| Housing & food | $7,912 - $19,180 | Varies by housing type |
| Books, materials, supplies, equipment | $1,224 | |
| **Total (on-campus)** | **$40,468 - $51,736** | |

> Note: Additional program course fees may apply. Estimates based on CLAS; other schools may differ.
> Source: https://admissions.ku.edu/costs, https://financialaid.ku.edu/calculate-costs/tuition-and-fees

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind/need-aware | **Need-aware for all** (domestic and international) | admissions.ku.edu |
| Merit scholarships | Available (Dec 1 priority deadline) | admissions.ku.edu/afford/scholarships |
| Need-based aid | Available (FAFSA required) | financialaid.ku.edu |
| Net Price Calculator | https://ku.studentaidcalculator.com/survey.aspx | admissions.ku.edu/costs |
| Tuition-free threshold | N/A (no published tuition-free program) | — |
| Loan-free policy | N/A | — |

### 4.3 Graduate cost & funding framework

| 维度 | 值 | 来源 |
|------|-----|------|
| Graduate tuition (in-state) | Varies by program | financialaid.ku.edu |
| Graduate tuition (out-of-state) | Varies by program | financialaid.ku.edu |
| Funding types | RA/TA/Fellowship/Grant | graduate.ku.edu |
| Application fee | $65 domestic / $100 international | gradapply.ku.edu |
| Fee waivers | Available for eligible applicants | gradapply.ku.edu |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.admissions.test_policy
  value: "Test-optional"
  source_url: https://admissions.ku.edu/apply
  source_snippet: "No test scores are necessary, and we strive to respond as quickly as possible to every complete, submitted application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.priority_scholarship
  value: "December 1"
  source_url: https://admissions.ku.edu/apply
  source_snippet: "FALL ADMISSION DEADLINES Dec. 1 Freshman scholarship deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.fafsa_priority
  value: "February 1"
  source_url: https://admissions.ku.edu/apply
  source_snippet: "Feb. 1 FAFSA priority deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.tuition_in_state
  value: "$11,298"
  source_url: https://admissions.ku.edu/costs
  source_snippet: "Estimated tuition: $11,298"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.tuition_oos
  value: "$30,177"
  source_url: https://admissions.ku.edu/costs
  source_snippet: "Estimated tuition: $30,177"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.fees
  value: "$1,155"
  source_url: https://admissions.ku.edu/costs
  source_snippet: "Required student and wellness fees: $1,155"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_in_state
  value: "$21,589 - $32,857"
  source_url: https://admissions.ku.edu/costs
  source_snippet: "Total: $21,589 - $32,857"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.total_oos
  value: "$40,468 - $51,736"
  source_url: https://admissions.ku.edu/costs
  source_snippet: "Total: $40,468 - $51,736"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.application_fee
  value: "$40"
  source_url: https://admissions.ku.edu/apply
  source_snippet: "We charge a non-refundable $40 fee for domestic degree-seeking freshmen."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.toefl
  value: "79 (18 min subscore)"
  source_url: https://world.ku.edu/english-proficiency
  source_snippet: "TOEFL iBT or TOEFL iBT Special Home Edition: Outgoing scale: 79 (18 minimum subscore)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.ielts
  value: "6.5 (6.0 min subscore)"
  source_url: https://world.ku.edu/english-proficiency
  source_snippet: "IELTS Academic: 6.5 (6.0 minimum subscore)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.assured_admission
  value: "GPA 3.25+ OR ACT 21/SAT 1060 with GPA 2.0+"
  source_url: https://admissions.ku.edu/apply
  source_snippet: "A cumulative high school GPA (weighted or unweighted) of 3.25 or higher OR An official ACT score of at least 21 or an official SAT score of at least 1060 with a minimum GPA of 2.0 on a 4.0 scale"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.financial_aid.need_aware
  value: "Need-aware for all"
  source_url: https://admissions.ku.edu/afford
  source_snippet: "KU is need-aware for all students"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee_domestic
  value: "$65"
  source_url: https://gradapply.ku.edu/graduate-application-faqs-ku-admissions-support
  source_snippet: "Domestic degree-seeking: $65"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_fee_international
  value: "$100"
  source_url: https://gradapply.ku.edu/graduate-application-faqs-ku-admissions-support
  source_snippet: "International degree-seeking: $100"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.programs.total
  value: "~300 program entries (including non-degree)"
  source_url: https://gradapply.ku.edu/graduate-programs
  source_snippet: "Total graduate programs found: 300"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.english_proficiency
  value: "TOEFL 79 / IELTS 6.5"
  source_url: https://gradapply.ku.edu/english-requirements
  source_snippet: "English proficiency requirements for graduate programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-001:
  field: institution.schools
  value: "14 schools/colleges"
  source_url: https://catalog.ku.edu/
  source_snippet: "Architecture & Design, Business, Education and Human Sciences, Engineering, Health Professions, Journalism & Mass Communications, Law, Liberal Arts & Sciences, Medicine, Music, Nursing, Pharmacy, Professional Studies, Social Welfare"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-002:
  field: institution.location
  value: "Lawrence, Kansas"
  source_url: https://ku.edu/
  source_snippet: "The University of Kansas - Lawrence, KS"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-003:
  field: institution.type
  value: "Public"
  source_url: https://ku.edu/
  source_snippet: "The University of Kansas is a public research university"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
ku-knowledge-base-v2/
├── 00-institution-overview
│   ├── 01-counts.md
│   ├── 02-hierarchy.md
│   ├── 03-degree-inventory.md
│   └── 04-distribution-matrix.md
├── 01-undergraduate-education
│   ├── clas-programs.md
│   ├── business-programs.md
│   ├── engineering-programs.md
│   ├── architecture-design-programs.md
│   ├── journalism-programs.md
│   ├── music-programs.md
│   ├── nursing-programs.md
│   ├── pharmacy-programs.md
│   ├── health-professions-programs.md
│   ├── education-programs.md
│   ├── professional-studies-programs.md
│   └── minors-complete-list.md
├── 02-graduate-education
│   ├── business-grad.md
│   ├── engineering-grad.md
│   ├── clas-grad.md
│   ├── medicine-grad.md
│   ├── law-grad.md
│   ├── music-grad.md
│   ├── pharmacy-grad.md
│   ├── social-welfare-grad.md
│   └── full-program-directory.md
├── 03-application-requirements
│   ├── ug-deadlines-requirements.md
│   ├── ug-english-proficiency.md
│   └── grad-admissions.md
├── 04-costs-financial-aid
│   ├── ug-cost-breakdown.md
│   ├── ug-financial-aid.md
│   └── grad-cost-funding.md
└── 05-evidence-chain
    └── evidence-index.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ku-knowledge-base-v2"
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

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete CLAS program list (all ~60 departments) | https://catalog.ku.edu/liberal-arts-sciences/ |
| P0 | Verify EA deadline (user stated Nov 1; not found on site) | https://admissions.ku.edu/apply |
| P1 | Graduate program deadlines per program | https://gradapply.ku.edu/graduate-programs |
| P1 | Graduate GRE requirements per program | https://gradapply.ku.edu/apply |
| P1 | School-specific admission requirements | https://admissions.ku.edu/major-specific-requirements |
| P2 | Housing options and costs | https://housing.ku.edu/ |
| P2 | Scholarship details and criteria | https://admissions.ku.edu/afford/scholarships |
| P2 | Transfer credit policies | https://registrar.ku.edu/transfer-credit |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | KU | (Other schools) |
|------|-----|-----------------|
| Type | Public | |
| Location | Lawrence, KS | |
| UG tuition (in-state) | $11,298 | |
| UG tuition (OOS) | $30,177 | |
| UG total COA (in-state) | $21,589-$32,857 | |
| UG total COA (OOS) | $40,468-$51,736 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | N/A (no EA) | |
| Priority deadline | Dec 1 (scholarship) | |
| RD deadline | Rolling | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 79 | |
| IELTS min | 6.5 | |
| Application fee (UG) | $40 | |
| Application fee (grad) | $65 domestic / $100 intl | |
| Total program count | ~485 | |
| School/college count | 14 | |
| Conference | Big 12 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.ku.edu, catalog.ku.edu, gradapply.ku.edu, world.ku.edu, financialaid.ku.edu, graduate.ku.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
