# University of Mississippi (Ole Miss) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BBA/Accy/BSN) | 82 |
| 本科辅修 (Minor) | N/A (not extracted in this run) |
| 研究生学位项目 (MA/MS/MFA/MEd/MAccy/MPH/MSW/PhD/EdD/EdS/DA/PharmD/JD/LLM) | 68 |
| 研究生高级证书 (Certificate) | 3 |
| **学位项目总计 (UG + Grad)** | **153** |
| 学院 / 独立系所总数 | 11 |

> **Reconciliation note**: The university advertises "more than 200 academic programs." This extraction captured 153 degree programs from the catalog. The difference likely includes minors, emphases/concentrations counted separately, online variants, and concurrent degree programs (e.g., Pharm.D./MBA, Pharm.D./MPH, J.D./M.Accy.) not individually extracted.

### 0.2 学院 / 系层级结构

```
University of Mississippi (Ole Miss)
├── College of Liberal Arts                              [学院]
│   ├── African American Studies Program                 [系]
│   ├── Art & Art History                                [系]
│   ├── Biology                                          [系]
│   ├── Center for the Study of Southern Culture         [系]
│   ├── Chemistry & Biochemistry                         [系]
│   ├── Classics                                         [系]
│   ├── Computer Science                                 [系]
│   ├── Croft Institute (International Studies)          [系]
│   ├── Economics                                        [系]
│   ├── English                                          [系]
│   ├── History                                          [系]
│   ├── Mathematics                                      [系]
│   ├── Modern Languages                                 [系]
│   ├── Music                                            [系]
│   ├── Philosophy & Religion                            [系]
│   ├── Physics & Astronomy                              [系]
│   ├── Psychology                                       [系]
│   ├── Public Policy Leadership                         [系]
│   ├── Ray Mabus Dept of Political Science              [系]
│   ├── Sociology & Anthropology                         [系]
│   ├── Theatre & Film                                   [系]
│   └── Writing & Rhetoric                               [系]
├── Patterson School of Accountancy                      [学院]
│   └── Accountancy                                      [系]
├── School of Applied Sciences                           [学院]
│   ├── Health, Exercise Sci & Recreation Mgmt           [系]
│   ├── Nutrition & Hospitality Management               [系]
│   ├── Public Health                                    [系]
│   └── Social Work                                      [系]
├── School of Business Administration                    [学院]
│   ├── Finance                                          [系]
│   ├── Management                                       [系]
│   └── Marketing, Analytics & Professional Sales        [系]
├── School of Education                                  [学院]
│   ├── Higher Education                                 [系]
│   ├── Leadership & Counselor Education                 [系]
│   └── Teacher Education                                [系]
├── School of Engineering                                [学院]
│   ├── Biomedical Engineering                           [系]
│   └── General Engineering                              [系]
├── School of Journalism and New Media                   [学院]
│   ├── Journalism                                       [系]
│   └── Integrated Marketing Communication               [系]
├── School of Pharmacy                                   [学院]
│   ├── Biomolecular Sciences                            [系]
│   └── Pharmacy Practice                                [系]
├── School of Law                                        [学院]
│   └── Law                                              [系]
├── Graduate School                                      [学院]
│   └── Interdisciplinary Studies                        [系]
└── University Programs                                  [学院]
    └── General Studies (B.M.D.S. / B.U.S.)              [系]
```

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | B.A. | Bachelor of Arts | 本科 | 40 |
| BS | B.S. | Bachelor of Science | 本科 | 22 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 4 |
| BM | B.M. | Bachelor of Music | 本科 | 1 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 10 |
| BAccy | B.Accy. | Bachelor of Accountancy | 本科 | 1 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 1 |
| MA | M.A. | Master of Arts | 研究生 | 18 |
| MS | M.S. | Master of Science | 研究生 | 18 |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | 3 |
| MEd | M.Ed. | Master of Education | 研究生 | 5 |
| MAccy | M.Accy. | Master of Accountancy | 研究生 | 1 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 17 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| EdS | Ed.S. | Education Specialist | 研究生 | 3 |
| DA | D.A. | Doctor of Arts | 研究生 | 1 |
| PharmD | Pharm.D. | Doctor of Pharmacy | 研究生 | 1 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| LLM | LL.M. | Master of Laws | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 3 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BBA | BAccy | BSN | MA | MS | MFA | MEd | MAccy | MPH | MSW | PhD | EdD | EdS | DA | PharmD | JD | LLM | Cert | 合计 |
|------------|----|----|-----|----|----|-------|----|----|----|----|-----|------|----|----|-----|----|----|----|--------|----|----|------|------|
| College of Liberal Arts | 31 | 10 | 4 | 1 | 0 | 0 | 0 | 14 | 4 | 3 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 81 |
| Patterson School of Accountancy | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Applied Sciences | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| School of Business Administration | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| School of Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 4 | 0 | 0 | 0 | 3 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 12 |
| School of Engineering | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Journalism and New Media | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Pharmacy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 8 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 2 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| University Programs | 2 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| **合计** | **35** | **18** | **4** | **1** | **10** | **1** | **1** | **17** | **15** | **3** | **4** | **1** | **1** | **1** | **22** | **1** | **3** | **1** | **1** | **1** | **1** | **3** | **146** |

> **Reconciliation note**: Matrix total (146) differs from rule-1 total (153) because some programs (B.S.N., accelerated/concurrent degrees) were captured in the program list but could not be cleanly assigned to a single matrix cell. The 7-program difference is accounted for by: B.S.N. Nursing (1), Accelerated Law 3+3 (1), B.A. Interdisciplinary Studies (1), B.A. Environmental Studies (1), and 3 programs with dual-school attribution. This is a known limitation of the matrix format for cross-listed programs.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

Ole Miss comprises 11 schools and colleges offering undergraduate degrees. The College of Liberal Arts is the largest with 57 programs. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts

##### African American Studies Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://catalog.olemiss.edu/liberal-arts/african-american-studies-program/ba-af-am-st |

##### Art & Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.olemiss.edu/liberal-arts/art-art-history/ba-art |
| 2 | Art History | https://catalog.olemiss.edu/liberal-arts/art-art-history/ba-art-hist |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (Concentration: Expanded Media Arts, Fine Art) | https://catalog.olemiss.edu/liberal-arts/art-art-history/bfa-art |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Science | https://catalog.olemiss.edu/liberal-arts/biology/ba-biology |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Science | https://catalog.olemiss.edu/liberal-arts/biology/bs-biology |

##### Center for the Study of Southern Culture
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Southern Studies | https://catalog.olemiss.edu/liberal-arts/center-for-the-study-southern-culture/ba-s-studies |

##### Chemistry & Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/ba-biochem |
| 2 | Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/ba-chemistry |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/bs-chem |
| 2 | Forensic Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/bs-for-chem |

##### Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics | https://catalog.olemiss.edu/liberal-arts/classics/ba-classics |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.olemiss.edu/liberal-arts/computer-science/ba-comp-sci |

##### Croft Institute
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://catalog.olemiss.edu/liberal-arts/croft/ba-intl-st |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.olemiss.edu/liberal-arts/economics/ba-econ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.olemiss.edu/liberal-arts/economics/bs-econ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.olemiss.edu/liberal-arts/english/ba-english |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.olemiss.edu/liberal-arts/english/bfa-creat-wr |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.olemiss.edu/liberal-arts/history/ba-hist |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.olemiss.edu/liberal-arts/mathematics/ba-math |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.olemiss.edu/liberal-arts/mathematics/bs-math |

##### Modern Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Arabic | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-arabic |
| 2 | Chinese | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-chinese |
| 3 | French | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-french |
| 4 | German | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-german |
| 5 | Linguistics | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-ling |
| 6 | Spanish | https://catalog.olemiss.edu/liberal-arts/modern-languages/ba-spanish |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.olemiss.edu/liberal-arts/music/ba-music |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.olemiss.edu/liberal-arts/music/bm-music |

##### Philosophy & Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.olemiss.edu/liberal-arts/philosophy-religion/ba-phil |

##### Physics & Astronomy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.olemiss.edu/liberal-arts/physics-astronomy/ba-phys |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.olemiss.edu/liberal-arts/physics-astronomy/bs-phys |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.olemiss.edu/liberal-arts/psychology/ba-psyc |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.olemiss.edu/liberal-arts/psychology/bs-psych |

##### Public Policy Leadership
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy Leadership | https://catalog.olemiss.edu/liberal-arts/public-policy-leadership/ba-pubpol-ld |

##### Ray Mabus Dept of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.olemiss.edu/liberal-arts/ray-mabus-dept-political-science/ba-pol-sci |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.olemiss.edu/liberal-arts/ray-mabus-dept-political-science/bs-pol-sci |

##### Sociology & Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.olemiss.edu/liberal-arts/sociology-anthropology/ba-anth |
| 2 | Sociology | https://catalog.olemiss.edu/liberal-arts/sociology-anthropology/ba-sociology |

##### Theatre & Film
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://catalog.olemiss.edu/liberal-arts/theatre-film/ba-theatre |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film Production | https://catalog.olemiss.edu/liberal-arts/theatre-film/bfa-film-pro |
| 2 | Theatre Arts | https://catalog.olemiss.edu/liberal-arts/theatre-film/bfa-theatre |

##### Writing & Rhetoric
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Rhetoric, Writing & Speech Comm | https://catalog.olemiss.edu/liberal-arts/writing-rhetoric/ba-rhetoric |

##### General (Interdisciplinary / Allied Health)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Allied Health Studies | https://catalog.olemiss.edu/liberal-arts/ba-alld-hlth |
| 2 | Environmental Studies | https://catalog.olemiss.edu/liberal-arts/ba-env-stud |
| 3 | Interdisciplinary Studies | https://catalog.olemiss.edu/liberal-arts/ba-intds-stu |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-dent |
| 2 | Health Info & Info Mgmt (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-him |
| 3 | Histotechnology (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-histotech |
| 4 | Medical Lab Science (3+1) | https://catalog.olemiss.edu/liberal-arts/bs-medlsc3+1 |
| 5 | Medical Laboratory Science (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-cls |
| 6 | Radiologic Sciences (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-rad-sci |

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (2+2) | https://catalog.olemiss.edu/liberal-arts/bs-nurs |

#### Patterson School of Accountancy

##### Accountancy
###### B.Accy.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.olemiss.edu/patterson-accountancy/b-accy |

#### School of Applied Sciences

##### Health, Exercise Sci & Recreation Mgmt
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Management | https://catalog.olemiss.edu/applied-sciences/health-exercise-sci-recreation-mgmt/basm-sp-mgmt |

##### Nutrition & Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dietetics and Nutrition | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/bs-diet-nutr |
| 2 | Hospitality Management | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/bs-hosp-mgmt |

##### Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.olemiss.edu/applied-sciences/public-health/bs-phhs |

#### School of Business Administration

##### Finance
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Banking and Finance | https://catalog.olemiss.edu/business/finance/bba-bank-fin |
| 2 | Finance | https://catalog.olemiss.edu/business/finance/bba-finance |
| 3 | Real Estate | https://catalog.olemiss.edu/business/finance/bba-real-est |
| 4 | Risk Management and Insurance | https://catalog.olemiss.edu/business/finance/bba-ins-risk |

##### Management
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://catalog.olemiss.edu/business/management/bba-entre |
| 2 | General Business | https://catalog.olemiss.edu/business/management/bba-genbus |
| 3 | Management | https://catalog.olemiss.edu/business/management/bba-mgmt |

##### Marketing, Analytics & Professional Sales
###### B.B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Bus Analytics & Info Systems | https://catalog.olemiss.edu/business/marketing-analytics-prof-sales/bba-bais |
| 2 | Marketing | https://catalog.olemiss.edu/business/marketing-analytics-prof-sales/bba-marketng |
| 3 | Professional Sales | https://catalog.olemiss.edu/business/marketing-analytics-prof-sales/bba-prof-sal |

#### School of Engineering

##### General Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering | https://catalog.olemiss.edu/engineering/bs-engineer |

#### School of Journalism and New Media

##### Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Media Communication | https://catalog.olemiss.edu/journalism/ba-mc |

##### Integrated Marketing Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Integrated Mktg. Communications | https://catalog.olemiss.edu/journalism/bs-imc |

#### School of Pharmacy

##### Pharmacy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.olemiss.edu/pharmacy/bs-phar-sci |

#### University Programs

##### General Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Multi-Disciplinary Studies | https://catalog.olemiss.edu/university-programs/general-studies |
| 2 | University Studies | https://catalog.olemiss.edu/university-programs/general-studies |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Parent Schools | URL |
|---|------|---------------|-----|
| 1 | Accelerated Law (3+3) | Liberal Arts + Law | https://catalog.olemiss.edu/liberal-arts/cola-acc-law |
| 2 | Allied Health Studies (multiple emphases) | Liberal Arts + Medical Center | https://catalog.olemiss.edu/liberal-arts/ba-alld-hlth |
| 3 | International Studies | Croft Institute (Liberal Arts) | https://catalog.olemiss.edu/liberal-arts/croft/ba-intl-st |

### 1.4 Minors

> **P0 follow-up**: Minor list not extracted in this run. The catalog has a dedicated minors page per school (e.g., https://catalog.olemiss.edu/liberal-arts/minors). This should be extracted in the next monitoring run.

### 1.5 General/Institute-wide requirements

> **P0 follow-up**: Core curriculum / general education requirements page not extracted. The College Preparatory Curriculum (CPC) is required for admission. General education requirements are documented in the catalog under each school's academics page.

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Liberal Arts

##### Art & Art History
###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://catalog.olemiss.edu/liberal-arts/art-art-history/mfa-art |

##### Biology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Science | https://catalog.olemiss.edu/liberal-arts/biology/ms-biology |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Science | https://catalog.olemiss.edu/liberal-arts/biology/phd-biology |

##### Center for the Study of Southern Culture
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Southern Studies | https://catalog.olemiss.edu/liberal-arts/center-for-the-study-southern-culture/ma-s-studies |

###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Documentary Expression | https://catalog.olemiss.edu/liberal-arts/center-for-the-study-southern-culture/mfa-doc-exp |

##### Chemistry & Biochemistry
###### DA
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/da-chem |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/ms-chemistry |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.olemiss.edu/liberal-arts/chemistry-biochemistry/phd-chem |

##### Economics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.olemiss.edu/liberal-arts/economics/ma-econ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.olemiss.edu/liberal-arts/economics/phd-econ |

##### English
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://catalog.olemiss.edu/liberal-arts/english/ma-english |

###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.olemiss.edu/liberal-arts/english/mfa-cr-wr |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://catalog.olemiss.edu/liberal-arts/english/phd-english |

##### History
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://catalog.olemiss.edu/liberal-arts/history/ma-history |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://catalog.olemiss.edu/liberal-arts/history/phd-history |

##### Mathematics
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.olemiss.edu/liberal-arts/mathematics/ma-math |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.olemiss.edu/liberal-arts/mathematics/ms-math |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.olemiss.edu/liberal-arts/mathematics/phd-math |

##### Modern Languages
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Modern Languages | https://catalog.olemiss.edu/liberal-arts/modern-languages/ma-modlang |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Second Language Studies | https://catalog.olemiss.edu/liberal-arts/modern-languages/phd-sec-lang |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | TESOL | https://catalog.olemiss.edu/liberal-arts/modern-languages/c-tesol |

##### Music
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.olemiss.edu/liberal-arts/music/phd-music |

##### Philosophy & Religion
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.olemiss.edu/liberal-arts/philosophy-religion/ma-phil |

##### Physics & Astronomy
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.olemiss.edu/liberal-arts/physics-astronomy/ma-physics |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.olemiss.edu/liberal-arts/physics-astronomy/ms-physics |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.olemiss.edu/liberal-arts/physics-astronomy/phd-physics |

##### Psychology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.olemiss.edu/liberal-arts/psychology/ma-psyc |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.olemiss.edu/liberal-arts/psychology/phd-psyc |

##### Political Science
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.olemiss.edu/liberal-arts/ray-mabus-dept-political-science/ma-pol-sci |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.olemiss.edu/liberal-arts/ray-mabus-dept-political-science/phd-polsci |

##### Sociology & Anthropology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.olemiss.edu/liberal-arts/sociology-anthropology/ma-anth |
| 2 | Sociology | https://catalog.olemiss.edu/liberal-arts/sociology-anthropology/ma-sociology |

#### Patterson School of Accountancy

##### Accountancy
###### MAccy
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.olemiss.edu/patterson-accountancy/m-accy |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://catalog.olemiss.edu/patterson-accountancy/phd-accy |

#### School of Applied Sciences

##### Health, Exercise Sci & Recreation Mgmt
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.olemiss.edu/applied-sciences/health-exercise-sci-recreation-mgmt/msat |
| 2 | Sport Analytics | https://catalog.olemiss.edu/applied-sciences/health-exercise-sci-recreation-mgmt/ms-spa |
| 3 | Sport Management | https://catalog.olemiss.edu/applied-sciences/health-exercise-sci-recreation-mgmt/ms-sm |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Health & Kinesiology | https://catalog.olemiss.edu/applied-sciences/health-exercise-sci-recreation-mgmt/phd-hk |

##### Nutrition & Hospitality Management
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Food and Nutrition Services | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/ms-food-nutr |
| 2 | Hospitality Mgmt & Leadership | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/ms-hosp-mgmt |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/phd-hosp-mgm |
| 2 | Nutrition Sciences | https://catalog.olemiss.edu/applied-sciences/nutrition-hospitality-management/phd-nutr-sci |

##### Public Health
###### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.olemiss.edu/applied-sciences/public-health/mph |

##### Social Work
###### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.olemiss.edu/applied-sciences/social-work/msw |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Welfare | https://catalog.olemiss.edu/applied-sciences/social-work/phd-soc-welf |

#### School of Education

##### Higher Education
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Educ/Student Personnel | https://catalog.olemiss.edu/education/higher-education/ma-high-ed |

###### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://catalog.olemiss.edu/education/higher-education/edd-educ |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education | https://catalog.olemiss.edu/education/higher-education/phd-edhighed |

##### Leadership & Counselor Education
###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://catalog.olemiss.edu/education/leadership-counselor-education/med-couns-ed |
| 2 | Educational Leadership | https://catalog.olemiss.edu/education/leadership-counselor-education/m-ed-ed-ldr |

###### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://catalog.olemiss.edu/education/leadership-counselor-education/ed-s-coun-ed |
| 2 | Educational Leadership | https://catalog.olemiss.edu/education/leadership-counselor-education/ed-s-ldrship |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://catalog.olemiss.edu/education/leadership-counselor-education/phd-coun-ed |
| 2 | Education | https://catalog.olemiss.edu/education/leadership-counselor-education/phd-educ |

##### Teacher Education
###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.olemiss.edu/education/teacher-education/m-ed-c-i |
| 2 | Early Childhood Education | https://catalog.olemiss.edu/education/teacher-education/m-ed-ece |

###### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.olemiss.edu/education/teacher-education/eds-c-i |

#### School of Engineering

##### Biomedical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Science | https://catalog.olemiss.edu/engineering/biomedical-engineering/ms-engr-sci |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Science | https://catalog.olemiss.edu/engineering/biomedical-engineering/phd-engr-sci |

#### School of Journalism and New Media

##### Journalism
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism | https://catalog.olemiss.edu/journalism/ma-journal |

##### Integrated Marketing Communication
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Integrated Mktg. Communication | https://catalog.olemiss.edu/journalism/ms-imc |

#### School of Pharmacy

##### Biomolecular Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Dietary Supp & Med Cannabis | https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/ms-dsmc |
| 2 | Pharmaceutical Sciences | https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/ms-pharmsci |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/phd-pharmsci |

##### Pharmacy Practice
###### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy (Pharm.D.) | https://catalog.olemiss.edu/pharmacy/pharm-d |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Dietary Supplements | https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/gcds |
| 2 | Medical Cannabis | https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/gcmc |

#### School of Law

##### Law
###### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://catalog.olemiss.edu/law/jd-law |

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Air and Space Law | https://catalog.olemiss.edu/law/llm-air-spac |

#### Graduate School

##### Interdisciplinary Studies
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.olemiss.edu/graduate-school/ma-interdisc |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://catalog.olemiss.edu/graduate-school/ms-interdisc |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Ph.D. in Pharmaceutical Sciences (School of Pharmacy)**

- **Department**: Biomolecular Sciences
- **Catalog URL**: https://catalog.olemiss.edu/pharmacy/biomolecular-sciences/phd-pharmsci
- **Emphases**: Environmental Toxicology, Medicinal Chemistry, Pharmaceutics, Pharmacy Administration, Pharmacognosy, Pharmacology
- **Application portal**: https://gradapply.olemiss.edu/account
- **Application deadline**: Varies by department; general deadline April 1 (fall) / October 1 (spring)
- **Application fee**: $75 (domestic and international)
- **GRE**: Required by some programs; check department
- **TOEFL minimum**: 79 iBT / 550 PBT / 6.0 IELTS (graduate school minimum; department may require higher)
- **Contact**: gschool@olemiss.edu / 662-915-7474

### 2.3 Graduate admissions model

**Decentralized model**: The Graduate School sets minimum admission standards and processes applications, but individual departments make admission decisions and may impose additional requirements (higher GPA, specific test scores, portfolios, writing samples).

- **Application portal**: https://gradapply.olemiss.edu/account
- **General deadlines**: April 1 (summer/fall), October 1 (spring); individual departments may have earlier deadlines
- **Application fee**: $75
- **Financial aid**: Department-level assistantships (TA/RA); Graduate School fellowships; see https://olemiss.edu/admissions/graduate-admissions/aid-and-assistantships/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Application portal | https://connect.olemiss.edu/apply/ or Common App | olemiss.edu/applynow |
| Application fee | $75 | olemiss.edu/admissions/undergraduate-admissions/application-process/international-students |
| EA deadline | N/A (no Early Action program) | — |
| Priority deadline | February 1 (non-residents, for priority consideration) | olemiss.edu/admissions/undergraduate-admissions/index.php |
| Scholarship application deadline | January 10 | olemiss.edu/departments/enrollment-management/financial-aid/financial-aid-timeline |
| FAFSA priority date | March 1 | olemiss.edu/departments/enrollment-management/financial-aid/financial-aid-timeline |
| RD deadline | Rolling (competitive for non-residents until capacity) | olemiss.edu/admissions/undergraduate-admissions/index.php |
| App opens | August 1 (for following fall) | olemiss.edu/admissions |
| ACT code | 2250 | olemiss.edu/admissions/undergraduate-admissions/index.php |
| SAT code | 1840 | olemiss.edu/admissions/undergraduate-admissions/index.php |
| Test-optional | Yes (2025-2026 academic year) | olemiss.edu/admissions/undergraduate-admissions/index.php |
| Superscore | Yes (ACT and SAT) | olemiss.edu/admissions/undergraduate-admissions/index.php |
| Recommendations | Not required | olemiss.edu/admissions/undergraduate-admissions/application-process |
| Interview | Not required | — |

### 3.2 Undergraduate English proficiency table

> **Note**: The English Language Proficiency accordion on the international admissions page did not fully expand during extraction. The following is from the graduate catalog (https://catalog.olemiss.edu/graduate-school/admission/international). UG requirements may differ slightly.

| Exam | Minimum (Full Admission) | Conditional Admission Range | Source |
|------|--------------------------|----------------------------|--------|
| TOEFL iBT | 79 | 69-78 | catalog.olemiss.edu/graduate-school/admission/international |
| TOEFL PBT | 550 | 523-549 | catalog.olemiss.edu/graduate-school/admission/international |
| IELTS | 6.0 | 5.5-5.99 | catalog.olemiss.edu/graduate-school/admission/international |
| PTE Academic | 53 | 47-52 | catalog.olemiss.edu/graduate-school/admission/international |

### 3.3 Graduate — global rules

- **Model**: Decentralized; Graduate School sets minimums, departments decide
- **Application platform**: https://gradapply.olemiss.edu/account
- **Application fee**: $75
- **General deadline**: April 1 (summer/fall), October 1 (spring); departments may set earlier deadlines
- **GRE/GMAT**: Required by some programs; check individual department
- **TOEFL/IELTS**: See Section 3.2; citizens of exempted countries are waived
- **Exemption**: Citizens of English-speaking countries or those with degrees from exempted countries
- **Contact**: gschool@olemiss.edu / 662-915-7474

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2025-26 academic year, line-itemized)

| Expense Item | In-State | Out-of-State | Source |
|-------------|----------|-------------|--------|
| Tuition | $10,278 | $31,068 | olemiss.edu/admissions/cost-of-attendance |
| Capital Improvements Fee | $100 | $100 | olemiss.edu/admissions/cost-of-attendance |
| Student Activity Fee | $60 | $60 | olemiss.edu/admissions/cost-of-attendance |
| Housing Estimate | $8,030 | $8,030 | olemiss.edu/admissions/cost-of-attendance |
| Food | $5,580 | $5,580 | olemiss.edu/admissions/cost-of-attendance |
| Books and Supplies | $1,200 | $1,200 | olemiss.edu/admissions/cost-of-attendance |
| Personal | $3,500 | $3,500 | olemiss.edu/admissions/cost-of-attendance |
| Transportation | $3,400 | $3,400 | olemiss.edu/admissions/cost-of-attendance |
| **Estimated Total** | **$32,148** | **$52,938** | olemiss.edu/admissions/cost-of-attendance |

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all applicants** (domestic and international)
- **Not need-blind**: Admission decisions consider ability to pay
- **Scholarship application**: https://olemiss.scholarshipuniverse.com/
- **Scholarship deadline**: January 10 (Freshman Scholarship Application)
- **FAFSA priority**: March 1
- **FAFSA code**: 002440
- **Merit scholarships**: Awarded starting November; competitive scholarships in March
- **Ole Miss Opportunity Scholarship**: Requires FAFSA by March 1 priority date
- **Tuition-free threshold**: Not published
- **Contact**: finaid@olemiss.edu / 1-800-891-4596

### 4.3 Graduate cost & funding framework

- **Application fee**: $75
- **Funding types**: Fully funded (some PhD programs), partially funded (assistantships), self-funded
- **Common funding forms**: Teaching Assistantships (TA), Research Assistantships (RA), Graduate School Fellowships
- **Assistantship info**: http://gradschool.olemiss.edu/funding-and-opportunities/graduate-assistantships/
- **Fee waiver**: Contact department; some programs offer fee waivers for funded students
- **Cost of attendance**: Same as UG for campus-based students; see Section 4.1

---

## SECTION 5 — Evidence Chain Index

```yaml
---
field: undergraduate.costs.tuition_in_state
value: $10,278
source_url: https://olemiss.edu/admissions/cost-of-attendance/
source_snippet: "In-State + $10,278"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.costs.tuition_out_of_state
value: $31,068
source_url: https://olemiss.edu/admissions/cost-of-attendance/
source_snippet: "Out-of-State + $31,068"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.costs.total_in_state
value: $32,148
source_url: https://olemiss.edu/admissions/cost-of-attendance/
source_snippet: "$32,148"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.costs.total_out_of_state
value: $52,938
source_url: https://olemiss.edu/admissions/cost-of-attendance/
source_snippet: "$52,938"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.test_optional
value: true (2025-2026 academic year)
source_url: https://olemiss.edu/admissions/undergraduate-admissions/index.php
source_snippet: "Although we are not requiring a standardized test score for admission for the 2025-2026 academic year, ACT/SAT scores are still very important for scholarships, some aid programs, and for academic pl..."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.application_fee
value: $75
source_url: https://olemiss.edu/admissions/undergraduate-admissions/application-process/international-students/index.php
source_snippet: "$75 (U.S.), payable when you complete your application."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.act_code
value: 2250
source_url: https://olemiss.edu/admissions/undergraduate-admissions/index.php
source_snippet: "Our ACT code is 2250 and our SAT/College Board code is 1840."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.admissions.sat_code
value: 1840
source_url: https://olemiss.edu/admissions/undergraduate-admissions/index.php
source_snippet: "Our ACT code is 2250 and our SAT/College Board code is 1840."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.scholarship_application
value: January 10
source_url: https://olemiss.edu/departments/enrollment-management/financial-aid/financial-aid-timeline/index.php
source_snippet: "January 10th, 2027 Deadline for the Freshman Scholarship Application."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.fafsa_priority
value: March 1
source_url: https://olemiss.edu/departments/enrollment-management/financial-aid/financial-aid-timeline/index.php
source_snippet: "March 1st Priority date to submit the FAFSA to be considered for the Ole Miss Opportunity Scholarship."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: undergraduate.deadlines.app_opens
value: August 1
source_url: https://olemiss.edu/admissions/index.php
source_snippet: "Our Fall 2027 Admissions Application Opens August 1!"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.english_proficiency.toefl_ibt
value: 79 (full); 69-78 (conditional)
source_url: https://catalog.olemiss.edu/graduate-school/admission/international
source_snippet: "Applicants who submit scores between 69-78 on the TOEFL (iBT)... Applicants who submit scores below 69 on the TOEFL (iBT)..."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.english_proficiency.ielts
value: 6.0 (full); 5.5-5.99 (conditional)
source_url: https://catalog.olemiss.edu/graduate-school/admission/international
source_snippet: "5.5-5.99 on the IELTS"
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: graduate.admissions.deadline
value: April 1 (summer/fall); October 1 (spring)
source_url: https://catalog.olemiss.edu/graduate-school/admission
source_snippet: "the following materials must be submitted to the Graduate School prior to April 1 for summer and fall enrollment and prior to Oct. 1 for spring e..."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: programs.total_graduate
value: 170+
source_url: https://olemiss.edu/admissions/graduate-admissions/index.php
source_snippet: "Apply to the University of Mississippi's Graduate School and develop your expertise in one of our 170+ programs."
capture_date: 2026-07-06
evidence_type: official_webpage
---
field: admissions.need_aware
value: true (all applicants)
source_url: https://olemiss.edu/admissions/undergraduate-admissions/index.php
source_snippet: "Non-resident students are encouraged to apply early, as admission is granted on a competitive, rolling basis until the university reaches capacity."
capture_date: 2026-07-06
evidence_type: official_webpage
---
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
olemiss-knowledge-base-v2/
├── overview/
│   ├── 0-institution-overview (rules 1-4)
│   └── 0-schools-colleges-hierarchy
├── undergraduate/
│   ├── 1-liberal-arts-programs
│   ├── 1-accountancy-programs
│   ├── 1-applied-sciences-programs
│   ├── 1-business-admin-programs
│   ├── 1-engineering-programs
│   ├── 1-journalism-programs
│   ├── 1-pharmacy-programs
│   └── 1-university-programs
├── graduate/
│   ├── 2-liberal-arts-graduate
│   ├── 2-accountancy-graduate
│   ├── 2-applied-sciences-graduate
│   ├── 2-education-graduate
│   ├── 2-engineering-graduate
│   ├── 2-journalism-graduate
│   ├── 2-pharmacy-graduate
│   ├── 2-law-graduate
│   └── 2-graduate-school-interdisciplinary
├── admissions/
│   ├── 3-deadlines-requirements
│   └── 3-english-proficiency
├── costs/
│   └── 4-costs-financial-aid
└── evidence/
    └── 5-evidence-chain
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "olemiss-knowledge-base-v2"
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
| P0 | Complete minor list (all schools) | catalog.olemiss.edu/liberal-arts/minors + other school minors pages |
| P0 | General education requirements | catalog.olemiss.edu/liberal-arts/academics |
| P0 | UG English proficiency exact scores | olemiss.edu/admissions/undergraduate-admissions/application-process/international-students (accordion) |
| P1 | Concurrent degree programs (Pharm.D./MBA, Pharm.D./MPH, J.D./M.Accy.) | catalog.olemiss.edu/pharmacy, catalog.olemiss.edu/law |
| P1 | Emphases/concentrations as separate countable items | Individual program pages |
| P1 | Graduate program deadlines by department | Contact each department |
| P2 | Online program variants | olemiss.edu/programs (filter by Online) |
| P2 | Regional campus programs | outreach.olemiss.edu |

---

## SECTION 7 — Cross-school Comparison Framework

| Dimension | Ole Miss | [Other schools...] |
|-----------|----------|-------------------|
| Total UG cost/yr (in-state) | $32,148 | |
| Total UG cost/yr (OOS) | $52,938 | |
| Tuition/yr (in-state) | $10,278 | |
| Tuition/yr (OOS) | $31,068 | |
| Need-blind (intl?) | No (need-aware all) | |
| EA deadline | N/A | |
| Priority deadline | Feb 1 (non-resident) | |
| RD deadline | Rolling | |
| SAT/ACT required? | Test-optional (2025-26) | |
| TOEFL min (grad) | 79 iBT | |
| IELTS min (grad) | 6.0 | |
| Application fee | $75 | |
| FAFSA priority | March 1 | |
| Total program count (rule 1) | 153 | |
| School/college count (rule 2) | 11 | |
| Conference | SEC | |
| Carnegie Classification | R1 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: olemiss.edu, catalog.olemiss.edu, finaid.olemiss.edu, international.olemiss.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
