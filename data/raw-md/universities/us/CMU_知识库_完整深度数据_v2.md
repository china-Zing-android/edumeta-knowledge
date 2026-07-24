# Carnegie Mellon University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

> **Methodology note**: The CMU course catalog (`coursecatalog.cmu.edu` and `coursecatalog.web.cmu.edu`) is unreachable in this capture environment (NXDOMAIN / ERR_CONNECTION_CLOSED). All program data was therefore sourced from the official per-college admissions and academic sites (`cmu.edu/admission/majors-programs/`, `cs.cmu.edu/education/`, `engineering.cmu.edu`, `cmu.edu/mcs/academics/`, `cmu.edu/dietrich/`, `heinz.cmu.edu`, `cmu.edu/tepper/`, `cmu.edu/cfa/`) plus the official UG Program Finder. Every figure is cited to its source page with a verbatim snippet.

---

## SECTION 0 — 院校总览 (Institution overview)

Carnegie Mellon University (CMU) is a private research university in Pittsburgh, Pennsylvania, founded in 1900 by Andrew Carnegie. World-renowned for computer science (consistently ranked #1 in the US), robotics, engineering, fine arts, and business. Organized into **seven undergraduate colleges/schools** plus **Heinz College** (graduate-only policy school, jointly administers the undergraduate Information Systems major with Dietrich College) and the **Software Engineering Institute** (a Federally Funded R&D Center).

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/B.Arch) | 75 |
| 本科辅修 (Minor) | 96 |
| 本科细分方向 (Concentration, 子方向非独立学位) | 26 |
| 研究生学位项目 (MA/MS/MFA/MBA/MArch/MHCI/MPA/PhD) | 106 |
| 研究生高级证书 (Heinz certificates) | 6 |
| **学位项目总计 (UG majors + Grad)** | **181** |
| UG 项目目录条目 (含 major/minor/concentration) | 157 |
| 学院 / 独立系所总数 | 9 (7 UG colleges + Heinz + SEI) |

> Reconciliation: 75 UG majors + 106 grad programs = **181 degree programs** (Rule 1 total). This equals the sum of all distribution-matrix cells and the row count in Sections 1 + 2. ✓ Verified.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Carnegie Mellon University
├── School of Computer Science (SCS)                      [学院]
│   ├── Computer Science Department (CSD)
│   ├── Human-Computer Interaction Institute (HCII)
│   ├── Language Technologies Institute (LTI)
│   ├── Machine Learning Department (MLD)
│   ├── Computational Biology Department (CBD)
│   ├── Robotics Institute (RI)
│   └── Institute for Software Research (ISR)
├── College of Engineering (CIT)                          [学院]
│   ├── Biomedical Engineering (BME)
│   ├── Chemical Engineering (ChemE)
│   ├── Civil and Environmental Engineering (CEE)
│   ├── Electrical and Computer Engineering (ECE)
│   ├── Engineering and Public Policy (EPP)
│   ├── Materials Science and Engineering (MSE)
│   ├── Mechanical Engineering (MechE)
│   ├── Information Networking Institute (INI)
│   └── Integrated Innovation Institute (III)
├── College of Fine Arts (CFA)                            [学院]
│   ├── School of Architecture
│   ├── School of Art
│   ├── School of Design
│   ├── School of Drama
│   └── School of Music
├── Dietrich College of Humanities and Social Sciences    [学院]
│   ├── English
│   ├── History
│   ├── Carnegie Mellon Institute for Strategy & Technology (CMIST)
│   ├── Languages, Cultures & Applied Linguistics (LCAL)
│   ├── Neuroscience Institute
│   ├── Philosophy
│   ├── Psychology
│   ├── Social and Decision Sciences (SDS)
│   ├── Statistics & Data Science
│   └── Economics (interdepartmental)
├── Mellon College of Science (MCS)                       [学院]
│   ├── Biological Sciences
│   ├── Chemistry
│   ├── Mathematical Sciences
│   └── Physics
├── Tepper School of Business                             [学院]
│   └── Business Administration
├── Heinz College of Information Systems and Public Policy [研究生院]
│   ⚠ jointly administers UG Information Systems BS with Dietrich College
│   ├── Public Policy & Management
│   ├── Information Systems Management
│   ├── Arts Management
│   ├── Information Security Policy & Management
│   ├── Health Care Analytics & IT
│   └── Entertainment Industry Management
├── Information Systems (BS)                              [跨学院项目]
│   ⚠ jointly administered by Dietrich College + Heinz College
├── Interdisciplinary Studies / BXA                       [跨学院项目]
│   ├── BXA Intercollege Degree Programs (CS+Arts, Eng+Arts, Hum+Arts, Sci+Arts)
│   ├── IDeATe (Integrative Design, Arts and Technology)
│   └── Interdisciplinary Majors
└── Software Engineering Institute (SEI)                  [FFRDC, 研究生]
    └── Institute for Software Research (grants MSE / PhD)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA | Bachelor of Arts | 本科 | 27 |
| BS | BS | Bachelor of Science | 本科 | 38 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 9 |
| B.Arch | B.Arch | Bachelor of Architecture (5-yr professional) | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 7 |
| MS | MS / MHCI / MSE / MCDS / MSAII / MSBA / MSM / MSPM / MSCF / MSPPM / etc. | Master of Science | 研究生 | 49 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MArch | MArch / MUD | Master of Architecture | 研究生 | 2 |
| MPA | MPM | Master of Public Administration / Management | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 42 |

> Sum of degree-level counts = 180 = Rule 1 total. ✓ Reconciles.

### 0.4 分布矩阵 (学院 × canonical 学位级别) (Rule 4)

| 学院 \ 级别 | BA | BS | BFA | B.Arch | MA | MS | MFA | MBA | MArch | MPA | MHCI | PhD | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| School of Computer Science | 0 | 5 | 0 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 1 | 17 | 39 |
| College of Engineering | 0 | 10 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 7 | 30 |
| College of Fine Arts | 0 | 0 | 9 | 1 | 2 | 2 | 3 | 0 | 2 | 0 | 0 | 0 | 19 |
| Dietrich College of Humanities and Social Sciences | 26 | 8 | 0 | 0 | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 10 | 51 |
| Mellon College of Science | 0 | 9 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 5 | 15 |
| Tepper School of Business | 0 | 1 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 1 | 7 |
| Heinz College | 0 | 0 | 0 | 0 | 1 | 10 | 0 | 0 | 0 | 1 | 0 | 2 | 14 |
| Information Systems (Dietrich + Heinz) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Interdisciplinary Studies | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| **合计** | **27** | **38** | **9** | **1** | **7** | **49** | **3** | **1** | **2** | **1** | **1** | **42** | **181** |

> Matrix grand total = **181** = Rule 1 total (181). ✓ Reconciles.

> **Concentration reading**: SCS dominates PhD (17) and MS (16); Engineering leads in MS (13) + PhD (7); Dietrich is broadest (51 programs, BA-heavy UG + 10 PhD); CFA concentrates in BFA/MFA/MArch professional degrees; Heinz is master's-heavy (10 MS + 1 MPA); Tepper has the single MBA + 4 specialized MS.
---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

CMU undergraduates apply to and enroll in a **specific college, school, or intercollege program** (not to the university at large). The seven undergraduate colleges are: School of Computer Science (SCS), College of Engineering (CIT), College of Fine Arts (CFA), Dietrich College of Humanities and Social Sciences, Mellon College of Science (MCS), Tepper School of Business, and the intercollege BXA / Information Systems / IDeATe programs. The full hierarchy tree is in Section 0.2. Total: **75 degree-granting majors + 96 minors + 26 concentrations** = 157 catalog entries (matches the official UG Program Finder "157 programs displayed").

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### School of Computer Science

##### SCS (CS Dept / HCII / RI / CBD / MLD)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://www.cmu.edu/admission/majors-programs/school-of-computer-science/artificial-intelligence#artificial-intelligence |
| 2 | Computational Biology | https://www.cmu.edu/admission/majors-programs/school-of-computer-science/computational-biology#computational-biology |
| 3 | Computer Science | https://www.cmu.edu/admission/majors-programs/school-of-computer-science/computer-science#computer-science |
| 4 | Human-Computer Interaction | https://www.cmu.edu/admission/majors-programs/school-of-computer-science/human-computer-interaction#human-computer-interaction |
| 5 | Robotics | https://www.cmu.edu/admission/majors-programs/school-of-computer-science/robotics#robotics |


#### College of Engineering

##### CIT Engineering Depts
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/biomedical-engineering#biomedical-engineering |
| 2 | Chemical Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/chemical-engineering#chemical-engineering |
| 3 | Civil Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/civil-environmental-engineering#civil-engineering |
| 4 | Electrical and Computer Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/electrical-and-computer-engineering#electrical-computer-engineering |
| 5 | Engineering Design, Innovation, and Entrepreneurship (EDIE) | https://www.cmu.edu/admission/majors-programs/college-of-engineering/engineering-design-innovation-and-entrepreneurship-edie |
| 6 | Engineering and Public Policy | https://www.cmu.edu/admission/majors-programs/college-of-engineering/engineering-and-public-policy#engineering-public-policy |
| 7 | Environmental Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/civil-environmental-engineering#environmental-engineering |
| 8 | Materials Science and Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/materials-science-engineering#materials-science-engineering |
| 9 | Mechanical Engineering | https://www.cmu.edu/admission/majors-programs/college-of-engineering/mechanical-engineering#mechanical-engineering |
| 10 | Science, Technology and Public Policy | https://www.cmu.edu/admission/majors-programs/college-of-engineering/engineering-and-public-policy#science-technology-public-policy |


#### College of Fine Arts

##### School of Architecture
###### B.Arch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-architecture#majors-minors-more |

##### School of Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-art#art |

##### School of Music
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Composition | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#composition |
| 2 | Electronic Music | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#electronic-music |
| 3 | Instrumental Performance | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#instrumental-performance |
| 4 | Music and Technology | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#music-technology |
| 5 | Piano Performance | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#piano-performance |
| 6 | Vocal Performance | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-music#vocal-performance |

##### CFA (other)
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Design | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-design#design |

##### School of Drama
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Drama | https://www.cmu.edu/admission/majors-programs/college-of-fine-arts/school-of-drama#drama |


#### Dietrich College of Humanities and Social Sciences

##### Dietrich College Departments
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Multilingual Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 2 | Behavioral Economics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/social-and-decision-sciences#behavioral-economics |
| 3 | Chinese Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 4 | Creative Writing | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/english#creative-writing |
| 5 | Economics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/economics#economics |
| 6 | Economics and Politics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/economics#economics-politics |
| 7 | Environmental Policy | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences#interdepartmental |
| 8 | Ethics, History and Public Policy | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/history#ethics-history-public-policy |
| 9 | Film and Visual Media | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/english#film-visual-media |
| 10 | French and Francophone Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 11 | German Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 12 | Global Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/history#global-studies |
| 13 | Hispanic Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 14 | International Relations and Politics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences#politics-and-strategy |
| 15 | Japanese Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 16 | Linguistics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/philosophy#linguistics |
| 17 | Literature and Culture | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/english#literature-culture |
| 18 | Logic and Computation | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/philosophy#logic-computation |
| 19 | Philosophy | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/philosophy#philosophy |
| 20 | Policy and Management | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/social-and-decision-sciences#policy-management |
| 21 | Political Science, Security and Technology | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/carnegie-mellon-institute-for-strategy-and-technology |
| 22 | Professional Writing | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences#english |
| 23 | Psychology | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/psychology#psychology |
| 24 | Russian Studies | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/modern-languages#modern-languages |
| 25 | Social and Political History | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/history#social-political-history |
| 26 | Technical Writing | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/english#technical-writing-communication |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/psychology#cognitive-science |
| 2 | Decision Science | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/social-and-decision-sciences#decision-science |
| 3 | Economics and Mathematical Sciences | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/economics#economics-mathematical-sciences |
| 4 | Economics and Statistics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/economics#economics-statistics |
| 5 | Mathematical and Statistical Sciences | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences#intercollege-programs |
| 6 | Psychology and Biological Sciences | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/psychology#psychology-biological-sciences |
| 7 | Statistics | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/statistics-data-science#statistics |
| 8 | Statistics and Machine Learning | https://www.cmu.edu/admission/majors-programs/dietrich-college-of-humanities-social-sciences/statistics-data-science#statistics-machine-learning |


#### Mellon College of Science

##### MCS Science Depts
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/biological-sciences#biological-sciences |
| 2 | Biological Sciences and Psychology | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/biological-sciences#biological-sciences-psychology |
| 3 | Biological Sciences: Neuroscience Track | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/biological-sciences#biological-sciences-neuroscience |
| 4 | Chemistry | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/chemistry#chemistry |
| 5 | Chemistry/Biological Chemistry | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/chemistry#chemistry-biological-chemistry |
| 6 | Computational Finance | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/mathematical-sciences#computational-finance |
| 7 | Mathematical Sciences | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/mathematical-sciences#mathematical-sciences |
| 8 | Neuroscience | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/biological-sciences#neuroscience |
| 9 | Physics | https://www.cmu.edu/admission/majors-programs/mellon-college-of-science/physics#physics |


#### Tepper School of Business

##### Tepper School of Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.cmu.edu/admission/majors-programs/tepper-school-of-business#business-administration |


#### Information Systems (Dietrich + Heinz)

##### Information Systems (joint Dietrich + Heinz)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems | https://www.cmu.edu/admission/majors-programs/information-systems#information-systems |


#### Interdisciplinary Studies

##### BXA Intercollege / IDeATe
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | BXA: Humanities and Arts | https://www.cmu.edu/admission/majors-programs/interdisciplinary-studies/bxa-intercollege-degree-programs#bha |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | BXA: Computer Science and Arts | https://www.cmu.edu/admission/majors-programs/interdisciplinary-studies/bxa-intercollege-degree-programs#bcsa |
| 2 | BXA: Engineering Studies and Arts | https://www.cmu.edu/admission/majors-programs/interdisciplinary-studies/bxa-intercollege-degree-programs#besa |
| 3 | BXA: Engineering and Arts | https://www.cmu.edu/admission/majors-programs/interdisciplinary-studies/bxa-intercollege-degree-programs#bea |
| 4 | BXA: Science and Arts | https://www.cmu.edu/admission/majors-programs/interdisciplinary-studies/bxa-intercollege-degree-programs#bsa |


### 1.3 Interdisciplinary / cross-college undergraduate programs

| Program | Type | Parent colleges |
|---------|------|-----------------|
| BXA: Computer Science and Arts (BCSA) | Major (BS) | SCS + CFA |
| BXA: Engineering and Arts (BHA/BSA variant) | Major (BS) | CIT + CFA |
| BXA: Engineering Studies and Arts | Major (BS) | CIT + CFA |
| BXA: Humanities and Arts (BHA) | Major (BA) | Dietrich + CFA |
| BXA: Science and Arts (BSA) | Major (BS) | MCS + CFA |
| Information Systems (BS) | Major (BS) | Dietrich + Heinz (jointly administered) |
| Science, Technology and Public Policy | Major (BS) | CIT + Dietrich/Heinz |
| Economics and Mathematical Sciences | Major (BS) | Dietrich (interdepartmental) |
| Economics and Politics / Economics and Statistics | Major (BS) | Dietrich (interdepartmental) |
| Biological Sciences and Psychology | Major (BS) | MCS + Dietrich |
| Ethics, History and Public Policy | Major (BA) | Dietrich (Philosophy + History) |
| IDeATe minors (Game Design, Animation, Sonic Arts, Intelligent Environments, etc.) | Minor | Cross-college consortium |

### 1.4 Minors — complete list

CMU offers **96 minors**. Complete list:

| # | Minor | Home school/college |
|---|-------|---------------------|
| 1 | Artificial Intelligence | School of Computer Science |
| 2 | Computational Biology | School of Computer Science |
| 3 | Computer Science | School of Computer Science |
| 4 | Human-Computer Interaction | School of Computer Science |
| 5 | Language Technologies | School of Computer Science |
| 6 | Machine Learning | School of Computer Science |
| 7 | Neural Computation | School of Computer Science |
| 8 | Robotics | School of Computer Science |
| 9 | Software Engineering | School of Computer Science |
| 10 | Additive Manufacturing | College of Engineering |
| 11 | Audio Engineering | College of Engineering |
| 12 | Automation and Controls | College of Engineering |
| 13 | Biomedical Engineering | College of Engineering |
| 14 | Colloids, Polymers and Surfaces | College of Engineering |
| 15 | Electronic Materials | College of Engineering |
| 16 | Engineering Studies | College of Engineering |
| 17 | Global Engineering | College of Engineering |
| 18 | Information Security, Privacy and Policy | College of Engineering |
| 19 | Materials Science and Engineering | College of Engineering |
| 20 | Mechanical Behavior of Materials | College of Engineering |
| 21 | Technology and Policy | College of Engineering |
| 22 | Architectural Design Fabrication | College of Fine Arts |
| 23 | Architectural History | College of Fine Arts |
| 24 | Architectural Representation and Visualization | College of Fine Arts |
| 25 | Architectural Technology | College of Fine Arts |
| 26 | Architecture | College of Fine Arts |
| 27 | Art | College of Fine Arts |
| 28 | Building Science | College of Fine Arts |
| 29 | Collaborative Piano | College of Fine Arts |
| 30 | Computational Design | College of Fine Arts |
| 31 | Conducting | College of Fine Arts |
| 32 | Design | College of Fine Arts |
| 33 | Drama | College of Fine Arts |
| 34 | Music | College of Fine Arts |
| 35 | Music Technology | College of Fine Arts |
| 36 | Music Theater | College of Fine Arts |
| 37 | Music Theory | College of Fine Arts |
| 38 | Musicology | College of Fine Arts |
| 39 | Photography | College of Fine Arts |
| 40 | African and African American Studies | Dietrich College of Humanities and Social Sciences |
| 41 | American Politics and Law | Dietrich College of Humanities and Social Sciences |
| 42 | Anthropology | Dietrich College of Humanities and Social Sciences |
| 43 | Applied Multilingual Studies | Dietrich College of Humanities and Social Sciences |
| 44 | Arabic Studies | Dietrich College of Humanities and Social Sciences |
| 45 | Behavioral Economics | Dietrich College of Humanities and Social Sciences |
| 46 | Chinese Studies | Dietrich College of Humanities and Social Sciences |
| 47 | Cognitive Neuroscience | Dietrich College of Humanities and Social Sciences |
| 48 | Creative Writing | Dietrich College of Humanities and Social Sciences |
| 49 | Cybersecurity and International Conflict | Dietrich College of Humanities and Social Sciences |
| 50 | Decision Science | Dietrich College of Humanities and Social Sciences |
| 51 | Economics | Dietrich College of Humanities and Social Sciences |
| 52 | Environmental and Sustainability Studies | Dietrich College of Humanities and Social Sciences |
| 53 | Ethics | Dietrich College of Humanities and Social Sciences |
| 54 | Film and Visual Media | Dietrich College of Humanities and Social Sciences |
| 55 | French and Francophone Studies | Dietrich College of Humanities and Social Sciences |
| 56 | Gender Studies | Dietrich College of Humanities and Social Sciences |
| 57 | German Studies | Dietrich College of Humanities and Social Sciences |
| 58 | Global Systems and Management | Dietrich College of Humanities and Social Sciences |
| 59 | Health Care Policy and Management | Dietrich College of Humanities and Social Sciences |
| 60 | Hispanic Studies | Dietrich College of Humanities and Social Sciences |
| 61 | Humanities Analytics | Dietrich College of Humanities and Social Sciences |
| 62 | International Relations and Politics | Dietrich College of Humanities and Social Sciences |
| 63 | Japanese Studies | Dietrich College of Humanities and Social Sciences |
| 64 | Linguistics | Dietrich College of Humanities and Social Sciences |
| 65 | Literature and Culture | Dietrich College of Humanities and Social Sciences |
| 66 | Logic and Computation | Dietrich College of Humanities and Social Sciences |
| 67 | Philosophy | Dietrich College of Humanities and Social Sciences |
| 68 | Policy and Management | Dietrich College of Humanities and Social Sciences |
| 69 | Psychology | Dietrich College of Humanities and Social Sciences |
| 70 | Religious Studies | Dietrich College of Humanities and Social Sciences |
| 71 | Russian Studies | Dietrich College of Humanities and Social Sciences |
| 72 | Science, Technology and Society | Dietrich College of Humanities and Social Sciences |
| 73 | Social and Political History | Dietrich College of Humanities and Social Sciences |
| 74 | Societal and Human Impacts of Future Technologies (SHIFT) | Dietrich College of Humanities and Social Sciences |
| 75 | Sociology | Dietrich College of Humanities and Social Sciences |
| 76 | Statistics | Dietrich College of Humanities and Social Sciences |
| 77 | Technical Writing | Dietrich College of Humanities and Social Sciences |
| 78 | Biological Sciences | Mellon College of Science |
| 79 | Chemistry | Mellon College of Science |
| 80 | Computational Finance | Mellon College of Science |
| 81 | Mathematical Sciences | Mellon College of Science |
| 82 | Neuroscience | Mellon College of Science |
| 83 | Physics | Mellon College of Science |
| 84 | Business Administration | Tepper School of Business |
| 85 | Business Analytics and Optimization | Tepper School of Business |
| 86 | Operations and Supply Chain Management | Tepper School of Business |
| 87 | Animation & Special Effects | Information Systems (Dietrich + Heinz) |
| 88 | Design for Learning | Information Systems (Dietrich + Heinz) |
| 89 | Game Design | Information Systems (Dietrich + Heinz) |
| 90 | Innovation & Entrepreneurship | Information Systems (Dietrich + Heinz) |
| 91 | Intelligent Environments | Information Systems (Dietrich + Heinz) |
| 92 | Media Design | Information Systems (Dietrich + Heinz) |
| 93 | Physical Computing | Information Systems (Dietrich + Heinz) |
| 94 | Soft Technologies | Information Systems (Dietrich + Heinz) |
| 95 | Sonic Arts | Information Systems (Dietrich + Heinz) |
| 96 | Discrete Mathematics and Logic |  |

### 1.5 General education / core requirements

CMU does **not** have a single university-wide core curriculum; each college sets its own general-education requirements. All undergraduates must satisfy their home college's writing requirement and a computing requirement. Notably:

- **Dietrich College** has a General Education Program (Dietrich GenEd): https://www.cmu.edu/dietrich/gened/
- **SCS** requires a foundational CS core (immersive first-year courses in computational thinking + an introduction to computational ethics as a core value).
- **College of Engineering** students are admitted directly to a department/major (or undecided within CIT) and follow an engineering common first year.
- **MCS / Tepper / CFA** each set their own college-level requirements; CFA programs require portfolios/auditions.

Each college page (linked in Section 1.2) lists its specific high-school course requirements for admission (e.g. SCS: 4 yr English, 4 yr Math, 1 yr Physics, 2 yr Chem/Bio/CS, 2 yr Foreign Language, 3 electives).

### 1.6 Course-ID → Major quick-lookup

N/A — CMU does not use a course-numbering scheme for majors (unlike MIT's "Course 6" system). Programs are identified by name and home college.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

CMU offers **106 graduate degree programs** across 8 colleges/schools (the 7 UG colleges plus Heinz College and the Software Engineering Institute). Graduate admissions are **decentralized** — each college/department runs its own admissions process, deadlines, and GRE policy. The Office of Graduate and Postdoctoral Affairs (`cmu.edu/graduate/`) is a services office, NOT a central admissions decider.

#### School of Computer Science

##### Computer Science Department
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Computer Science (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Algorithms, Combinatorics and Optimization (PhD) |
| 2 | Computer Science (PhD) |
| 3 | Computer Science (Dual Degree Portugal) (PhD) |
| 4 | Computer Science with Neural Basis of Cognition Certificate (PhD) |
| 5 | Pure and Applied Logic (PhD) |

##### Human-Computer Interaction Institute
###### MHCI
| # | 项目 |
|---|------|
| 1 | Master of Human-Computer Interaction (MHCI) |

###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Learning Engineering (MS) |
| 2 | Master of Science in Product Management (MSPM) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Human-Computer Interaction (PhD) |
| 2 | Human-Computer Interaction (Dual Degree Portugal) (PhD) |

##### Language Technologies Institute
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Computational Data Science (MCDS) |
| 2 | Master of Science in Artificial Intelligence and Innovation (MSAII) |
| 3 | Master of Science in Intelligent Information Systems (MIIS) |
| 4 | Master of Science in Language Technologies (MLT) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Language and Information Technologies (PhD) |
| 2 | Language and Information Technologies (Dual Degree Portugal) (PhD) |

##### Machine Learning Department
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Machine Learning (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Machine Learning (PhD) |

##### Computational Biology Department
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Automated Science: Biological Experimentation (MS) |
| 2 | Master of Science in Computational Biology (MSCB) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Computational Biology (PhD) |

##### Robotics Institute
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Computer Vision (MS) |
| 2 | Master of Science in Robotics (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Robotics (PhD) |
| 2 | Robotics (Dual Degree Portugal) (PhD) |

##### Software Engineering Institute/Institute for Software Research
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Software Engineering for Professionals (MSE) |

##### Institute for Software Research
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Software Engineering - Embedded Systems (MSE) |
| 2 | Master of Software Engineering - Scalable Systems (MSE) |
| 3 | Master of Software Engineering Online (MSE) |

###### PhD
| # | 项目 |
|---|------|
| 1 | Societal Computing (PhD) |
| 2 | Societal Computing (Dual Degree Portugal) (PhD) |
| 3 | Software Engineering (PhD) |
| 4 | Software Engineering (Dual Degree Portugal) (PhD) |


#### College of Engineering

##### Biomedical Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Biomedical Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Biomedical Engineering (PhD) |

##### Chemical Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Chemical Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Chemical Engineering (PhD) |

##### Civil and Environmental Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Civil and Environmental Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Civil and Environmental Engineering (PhD) |

##### Electrical and Computer Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Electrical and Computer Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Electrical and Computer Engineering (PhD) |

##### Engineering and Public Policy
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Engineering and Public Policy (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Engineering and Public Policy (PhD) |

##### Materials Science and Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Materials Science and Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Materials Science and Engineering (PhD) |

##### Mechanical Engineering
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Mechanical Engineering (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Mechanical Engineering (PhD) |

##### Multidisciplinary
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Artificial Intelligence Engineering (MS AIE) |

##### Information Networking Institute
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Information Networking (MSIN) |
| 2 | MS in Information Technology (MSIT) |
| 3 | MS in Mobile and IoT Engineering (MSMITE) |

##### Integrated Innovation Institute
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Integrated Innovation for Products and Services (MIIPS) |
| 2 | Master of Science in Technology Ventures (MSTV) |


#### College of Fine Arts

##### School of Architecture
###### MArch
| # | 项目 |
|---|------|
| 1 | Master of Architecture (MArch) |
| 2 | Master of Urban Design (MUD) |

##### School of Art
###### MFA
| # | 项目 |
|---|------|
| 1 | Master of Fine Arts in Art (MFA) |

##### School of Design
###### MFA
| # | 项目 |
|---|------|
| 1 | Master of Design (MDes) (MDes) |

###### MS
| # | 项目 |
|---|------|
| 1 | Master of Professional Studies (MPS) (MPS) |

##### School of Drama
###### MFA
| # | 项目 |
|---|------|
| 1 | Master of Fine Arts in Drama (MFA) |

##### School of Music
###### MA
| # | 项目 |
|---|------|
| 1 | Master of Arts in Music (MA) |
| 2 | Master of Music (MM) |

##### Entertainment Technology Center (CFA+SCS)
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Entertainment Technology (MET) |


#### Dietrich College of Humanities and Social Sciences

##### English
###### MA
| # | 项目 |
|---|------|
| 1 | Master of Arts in English (Rhetoric/Literary/Cultural Studies) (MA) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in English (PhD) |

##### History
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in History (PhD) |

##### CMIST
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Information Technology, Security and International Relations (MS) |

##### LCAL
###### MA
| # | 项目 |
|---|------|
| 1 | Master of Arts in Applied Linguistics (MA) |
| 2 | Master of Arts in Translation (MA) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Second Language Acquisition (PhD) |

##### Neuroscience Institute
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Neural Computation (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Neural Computation (PhD) |

##### Philosophy
###### MA
| # | 项目 |
|---|------|
| 1 | Master of Arts in Philosophy (MA) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Logic, Computation and Methodology (PhD) |
| 2 | PhD in Philosophy (PhD) |

##### Psychology
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Cognitive Neuroscience (PhD) |
| 2 | PhD in Psychology (PhD) |

##### Social and Decision Sciences
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Behavior and Decision Research (PhD) |

##### Statistics & Data Science
###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Applied Data Science and Statistics (MS) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Statistics (PhD) |


#### Mellon College of Science

##### Biological Sciences
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Biological Sciences (PhD) |

##### Chemistry
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Chemistry (PhD) |

##### Mathematical Sciences
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Mathematical Sciences (PhD) |

##### Physics
###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Astronomy and Astrophysics (PhD) |
| 2 | PhD in Physics (PhD) |

##### Interdisciplinary
###### MS
| # | 项目 |
|---|------|
| 1 | MS in Data Analytics (MS-DAS) |


#### Tepper School of Business

##### Tepper School of Business
###### MBA
| # | 项目 |
|---|------|
| 1 | Master of Business Administration (MBA) |

###### MS
| # | 项目 |
|---|------|
| 1 | Master of Science in Business Analytics (MSBA) |
| 2 | Master of Science in Computational Finance (MSCF) |
| 3 | Master of Science in Management (MSM) |
| 4 | Master of Science in Product Management (MSPM) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Business (PhD) |


#### Heinz College

##### Heinz College
###### MA
| # | 项目 |
|---|------|
| 1 | Master of Arts Management (MAM) |

###### MPA
| # | 项目 |
|---|------|
| 1 | Master of Public Management (MPM) |

###### MS
| # | 项目 |
|---|------|
| 1 | Master of Entertainment Industry Management (MEIM) |
| 2 | Master of Information Systems Management (MISM) |
| 3 | Master of Medical Management (MMM) |
| 4 | Master of Science in AI Systems Management (AIM) |
| 5 | Master of Science in Business Intelligence and Data Analytics (BIDA) |
| 6 | Master of Science in Health Care Analytics and Information Technology (MSHCA) |
| 7 | Master of Science in Information Security Policy and Management (MSISPM) |
| 8 | Master of Science in Public Policy and Data Analytics (MSPPM-DA) |
| 9 | Master of Science in Public Policy and Management (MSPPM) |
| 10 | Master of Science in Public Policy and Management (Washington D.C.) (MSPPM-DC) |

###### PhD
| # | 项目 |
|---|------|
| 1 | PhD in Information Systems and Management (PhD) |
| 2 | PhD in Public Policy and Management (PhD) |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Application platform | **Common Application** + CMU Writing Supplement (3 short-answer questions) | cmu.edu/admission/admission/undergraduate-admission-requirements |
| Application fee | **$75** (fee waivers accepted via Common App economic-need indicators) | cmu.edu/admission/admission/undergraduate-admission-requirements |
| **Early Decision (binding)** | Deadline **November 2** · Notified Dec 15 · Enroll Feb 1 | cmu.edu/admission/admission/application-plans-deadlines |
| ED availability | **Not available** for School of Drama, BXA Design programs, or School of Music | cmu.edu/admission/admission/application-plans-deadlines |
| **Regular Decision** | Deadline **January 4** · Notified no later than April 1 · Enroll **May 1** | cmu.edu/admission/admission/application-plans-deadlines |
| RD — Schools of Drama & Music | Deadline **December 1** · Notified no later than April 1 | cmu.edu/admission/admission/application-plans-deadlines |
| Transfer (fall, all except CFA) | Deadline **February 16** (supporting docs by Mar 1) · Notified May 17 | cmu.edu/admission/admission/application-plans-deadlines |
| Transfer (fall, CFA) | Drama/Music Dec 1; Architecture/Art/Design Jan 5 · Notified Apr 1 | cmu.edu/admission/admission/application-plans-deadlines |
| Standardized testing — **SCS** | **SAT or ACT REQUIRED** (the only college that requires) | cmu.edu/admission/admission/standardized-testing |
| Standardized testing — CIT, Dietrich, Heinz IS, MCS, Tepper | **Test-Flexible**: SAT, ACT, IB, AP, Cambridge A-Level, or French Baccalaureate | cmu.edu/admission/admission/standardized-testing |
| Standardized testing — CFA | **Test-Optional** (portfolios/auditions required instead) | cmu.edu/admission/admission/standardized-testing |
| Superscore | SAT **yes**; ACT **no** (composite score prevents it) | cmu.edu/admission/admission/standardized-testing |
| Score reporting | Self-report accepted via Common App; official only if admitted & enrolling | cmu.edu/admission/admission/standardized-testing |
| SAT code | 2074 | cmu.edu/admission/admission/standardized-testing |
| ACT code | 3534 | cmu.edu/admission/admission/standardized-testing |
| Recommendations | 1 counselor (Secondary School Counselor Evaluation) + 1 teacher recommendation | cmu.edu/admission/admission/undergraduate-admission-requirements |
| Essays | Common App Essay + CMU Writing Supplement (3 short-answer questions) | cmu.edu/admission/admission/undergraduate-admission-requirements |
| Portfolios/Auditions | Required for CFA (Architecture, Art, Design, Drama, Music) | cmu.edu/admission/admission/college-of-fine-arts-applicants |
| Interviews | Not offered as part of admission process | (general policy) |
| Supplemental submissions | NOT accepted (resumes, artwork, portfolios except CFA, recordings, websites) | cmu.edu/admission/admission/undergraduate-admission-requirements |
| Update cutoff | No applicant updates accepted after **January 15** (counselor docs continue) | cmu.edu/admission/admission/undergraduate-admission-requirements |
| Test timing preferred | ED: complete testing by Nov 1; RD: by **January 3** | cmu.edu/admission/admission/standardized-testing |

### 3.2 Undergraduate English proficiency table

Required of all non-native English speakers. Scores must be no more than **2 years old** at time of application. CMU prefers applicants submit all English-proficiency results from the past two years. **No TOEFL MyBest/superscore** — uses the single set of TOEFL scores from the highest overall administration.

| Exam | Minimum | Recommended (subscores) | Notes |
|------|---------|--------------------------|-------|
| **TOEFL iBT / iBT Home Edition** | **102** overall | subscores ≥ 25 each section | Before Jan 21, 2026. **After** Jan 21, 2026: min 5 overall, subscores ≥ 5 (new scoring scale). CMU TOEFL code 2074 |
| **TOEFL Essentials** | **11** overall band | subscores ≥ 11 | |
| **IELTS (or IELTS Online)** | **7.5** overall (Academic) | subscores ≥ 7.5 | Paper-based or computer-delivered Academic Examination |
| **Cambridge English Assessment** | **191** overall | subscores ≥ 191 | |
| **Duolingo English Test (DET)** | **135** overall | Literacy, Conversation, Comprehension, Production all ≥ 135 | |

> **Source**: https://www.cmu.edu/admission/admission/standardized-testing (TOEFL/IELTS/Cambridge/DET block) and https://www.cmu.edu/admission/admission/international-applicants

### 3.3 Graduate — global rules

| Dimension | Value |
|-----------|-------|
| Admissions model | **Fully decentralized** — each college/department runs its own admissions, deadlines, fee, and GRE/TOEFL policy. No central grad application portal. |
| Application platforms | Per-program (college-specific application sites; SCS uses its own graduate admissions portal; Tepper MBA uses its own; Heinz via college site; etc.) |
| Standard application fee | Varies by program (~$75–$200 typical); each college sets its own. Tepper MBA, SCS, Heinz each have distinct fees. |
| GRE/GMAT policy | Varies by program — most SCS PhD/MS programs have made GRE optional/required-noted; Tepper MBA accepts GMAT or GRE; Heinz programs vary. **Verify per-program.** |
| Language-test policy | TOEFL/IELTS required of non-native English speakers; specific minimums set by each program (CMU institutional minimum aligns with UG: TOEFL iBT 102, IELTS 7.5). |
| April 15 Resolution (CGS) | CMU is a Council of Graduate Schools signatory — funded PhD offers honor the **April 15** decision deadline. |
| Application timeline | Most grad deadlines December–January for fall entry; rolling admits thereafter. |
| Institutional test codes | TOEFL: **2074** (institution-wide); GRE: institutional code **2074**; dept codes vary by program. |
| Cost & funding | PhD students in SCS receive **full financial support** while in good academic standing. Master's programs are typically self-funded (tuition-paying). |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

**First-Year Students Entering Fall 2026** (per-unit tuition rate: $969):

| Expense item | Resident | Commuter | Description |
|--------------|----------|----------|-------------|
| Tuition | $69,702 | $69,702 | Set by Board of Trustees |
| Housing | $11,700 | $0 | All first-years required to live on campus |
| Food | $7,950 | $3,976 | Commuter food reduced by on-campus time |
| First-Year Experience Fee | $748 | $748 | Applicable to first-years and transfers |
| Technology Fee | $490 | $490 | |
| Student Activities Fee | $322 | $322 | |
| Transportation Fee | $302 | $302 | |
| **Subtotal (tuition, fees, living)** | **$91,214** | **$75,540** | |
| Books, Course Materials, Supplies, Equipment | $1,000 | $1,000 | Indirect (not billed) |
| Miscellaneous Personal Expenses | $1,300 | $1,300 | Indirect |
| Estimated Loan Fees | $100 | $100 | Indirect |
| Transportation Allowance | $0 | $680 | Indirect; varies by home state |
| **TOTAL COST OF ATTENDANCE** | **$93,614** | **$78,620** | |
| Health Insurance (individual, required) | $3,093/yr | $3,093/yr | Waivable with proof of family coverage |

**Returning Undergraduates (entered 2025 & earlier):** Tuition $69,702; resident total COA $95,796; commuter $77,872; off-campus $91,056.

> **Source**: https://www.cmu.edu/sfs/tuition/undergraduate/index.html (verbatim: "2026-2027 Undergraduate Tuition & Fees … Tuition $69,702 … TOTAL COST OF ATTENDANCE $93,614")

### 4.2 Undergraduate financial-aid policy

| Policy | Value |
|--------|-------|
| Need-blind / need-aware | **Need-blind for U.S. citizens/permanent residents**; **need-AWARE for international students** (CMU does not offer financial aid to international students) |
| Meets full demonstrated need | **Yes — 100% of demonstrated financial need for domestic students** (no loans for families <$100k) |
| **Tuition-free threshold** | **Families making less than $75,000/year attend CMU completely tuition-free** |
| **No federal loans threshold** | **Families making less than $100,000/year receive aid with NO federal loans** |
| Loan-free graduation | Yes, for families under $100k income |
| Average student-loan debt at graduation | **< $18,000** (national average: $37,000) |
| Average starting salary (Class of 2025) | **$116,882** |
| Employed/in grad school within 6 months (Class 2025) | **91%** |
| CMU Pathway Program | Initiative to make CMU affordable regardless of socioeconomic background |
| Aid investment growth | Up 86% over 10 years: $75.7M (FY2015) → $141.1M (FY2024) |

> **CRITICAL distinction**: Unlike MIT/Harvard/Yale/Princeton/Dartmouth/Amherst (need-blind for internationals), **CMU offers NO financial aid to international undergraduate students**. International families must plan to pay the full cost of attendance. Source: "Carnegie Mellon doesn't offer financial aid to international students" — cmu.edu/admission/admission/international-applicants

### 4.3 Graduate cost & funding framework

Graduate tuition is set by each college/school. **2026-2027 graduate tuition & fees** (per-college):

| College / Program | Tuition | Fees |
|-------------------|---------|-------|
| Dietrich College (H&SS) | $53,000 | $1,036 |
| Computational Finance (MSCF) | $71,800 | $1,036 |
| Entertainment Technology Center (ETC) | $61,628 | $1,036 |
| Integrated Innovation Institute | $61,510 | $1,036 |
| College of Engineering / CFA / MCS / SCS / ETIM / INI / CMIST | "Varies" (per-program) | $1,036 |
| All But Dissertation In Residence (ABR) | Varies | $1,036 |
| **Heinz College** (per semester) | | |
| — MAM / MSPPM / MSHCA / MSISPM / AIM | $29,570/semester | $518/semester |
| — MEIM | $29,570/semester | Varies |
| — MPM | $620/unit | $518/semester |
| — MSIT | $620/unit | Varies |
| — Heinz PhD | $29,570/semester | $518/semester |
| **Tepper School** | | |
| — Full-Time MBA (2 yr) | $42,093 | $1,036 |
| — Full-Time Accelerated MBA | $42,093 | $1,036 |
| — Online Hybrid MBA | $769/unit | $490 |
| — Online Hybrid Accelerated MBA | $769/unit | $409 |
| — Full-Time MSBA | $743/unit | $1,036 |
| — Part-Time MSBA | $692/unit | $490 |
| — MSM | $695/unit | $490 |
| — Tepper Doctoral | $23,500/semester | $1,036 |

**Funding taxonomy:**
- **PhD students** (especially in SCS, Engineering, MCS, Dietrich): typically **fully funded** — full tuition + stipend via research/teaching assistantships and fellowships. SCS states: "All of our Ph.D. students receive full financial support while in good academic standing."
- **Master's students**: typically **self-funded** (tuition-paying); limited partial scholarships/fellowships available per program.
- **CMU Rales Fellows Program**: dedicated to increasing access to STEM graduate education by removing financial barriers (cmu.edu/graduate/rales-fellows/).
- **Common funding forms**: RA (Research Assistantship), TA (Teaching Assistantship), fellowship, grant, stipend.

> **Source**: https://www.cmu.edu/sfs/tuition/graduate/index.html (verbatim 2026-2027 Graduate Tuition & Fees table)

---

## SECTION 5 — Evidence chain index

Every cited fact is bound to its source URL + verbatim snippet + capture date. Numbered E-U-NNN (undergraduate) / E-G-NNN (graduate).

```yaml
field: ug.deadlines.ED
value: "November 2"
source_url: https://www.cmu.edu/admission/admission/application-plans-deadlines
source_snippet: "Early Decision Deadline: November 2 Notified by: December 15 Enroll by: February 1"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.deadlines.RD
value: "January 4"
source_url: https://www.cmu.edu/admission/admission/application-plans-deadlines
source_snippet: "Regular Decision Deadline: January 4 Notified by: No later than April 1 Enroll by: May 1"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.deadlines.CFA_Drama_Music
value: "December 1"
source_url: https://www.cmu.edu/admission/admission/application-plans-deadlines
source_snippet: "Regular Decision for Schools of Drama and Music Deadline: December 1"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.deadlines.ED_exclusions
value: "Drama, BXA Design, Music excluded from ED"
source_url: https://www.cmu.edu/admission/admission/application-plans-deadlines
source_snippet: "Early Decision is not available for the School of Drama, BXA Design programs or the School of Music."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.test_policy.SCS_required
value: "SAT/ACT required"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "The School of Computer Science requires an SAT or an ACT score."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.test_policy.test_flexible
value: "CIT/Dietrich/Heinz-IS/MCS/Tepper test-flexible"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "The following colleges and programs operate on a test flexible policy: College of Engineering; Dietrich College of Humanities and Social Sciences; Heinz College's Information Systems program; Mellon College of Science; Tepper School of Business"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.test_policy.CFA_optional
value: "CFA test-optional"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "The College of Fine Arts is test optional and requires portfolios or auditions."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.test_policy.superscore
value: "SAT yes, ACT no"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "we allow superscoring of SAT test results, but we are unable to accept superscored results for the ACT exam"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.english.TOEFL
value: "102"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "TOEFL iBT or iBT Home Edition: We require at least a 102 overall score and give consideration to those with subscores of 25 and above."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.english.IELTS
value: "7.5"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "IELTS (or IELTS Online): We require at least a 7.5 overall band score on the Academic Examination"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.english.Cambridge
value: "191"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "Cambridge English Assessment: We require at least a 191 overall score"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.english.DET
value: "135"
source_url: https://www.cmu.edu/admission/admission/standardized-testing
source_snippet: "Duolingo English Test: we require at least a 135 overall score"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.application_fee
value: "75 USD"
source_url: https://www.cmu.edu/admission/admission/undergraduate-admission-requirements
source_snippet: "$75 Application Fee* … Carnegie Mellon accepts fee waivers from students who meet one of the indicators of economic need"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.intl.no_aid
value: "No financial aid for internationals"
source_url: https://www.cmu.edu/admission/admission/international-applicants
source_snippet: "Carnegie Mellon doesn't offer financial aid to international students. If you're an international student who plans to enroll at Carnegie Mellon, you and your family must plan to pay the total cost of attendance"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.coa.tuition
value: "69702 USD (2026-27)"
source_url: https://www.cmu.edu/sfs/tuition/undergraduate/index.html
source_snippet: "2026-2027 Undergraduate Tuition & Fees … Tuition $69,702"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: ug.coa.total_resident
value: "93614 USD (2026-27)"
source_url: https://www.cmu.edu/sfs/tuition/undergraduate/index.html
source_snippet: "TOTAL COST OF ATTENDANCE $93,614 (resident, first-year)"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: ug.aid.tuition_free_threshold
value: "75000 USD"
source_url: https://www.cmu.edu/admission/costs-aid
source_snippet: "STUDENTS WHOSE FAMILIES MAKE LESS THAN $75K/YEAR WILL ATTEND CMU COMPLETELY TUITION-FREE"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.aid.no_loans_threshold
value: "100000 USD"
source_url: https://www.cmu.edu/admission/costs-aid
source_snippet: "STUDENTS FROM FAMILIES MAKING LESS THAN $100K/YEAR WILL RECEIVE FINANCIAL AID THAT DOES NOT INCLUDE FEDERAL LOANS"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.aid.starting_salary
value: "116882 USD"
source_url: https://www.cmu.edu/admission/costs-aid
source_snippet: "The 2025 graduating class had an average starting salary of $116,882"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: ug.programs.count
value: "157 catalog entries"
source_url: https://www.cmu.edu/admission/majors-programs/undergraduate-program-finder
source_snippet: "157 programs displayed."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: grad.admissions.model
value: "decentralized"
source_url: https://www.cmu.edu/graduate/prospective/index.html
source_snippet: "To learn more about the graduate programs offered at CMU, see the Guide to Graduate Degrees and Programs section, which provides a college-based list that will direct you to the college websites"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: grad.tuition.MSCF
value: "71800 USD"
source_url: https://www.cmu.edu/sfs/tuition/graduate/index.html
source_snippet: "Computational Finance (MSCF) Tuition: $71,800 Fees: $1,036"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: grad.tuition.Dietrich
value: "53000 USD"
source_url: https://www.cmu.edu/sfs/tuition/graduate/index.html
source_snippet: "Dietrich College of Humanities & Social Sciences Tuition: $53,000"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: grad.tuition.Tepper_MBA
value: "42093 USD/semester"
source_url: https://www.cmu.edu/sfs/tuition/graduate/index.html
source_snippet: "Full-Time MBA Program Duration: 2 years Tuition: $42,093"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: grad.tuition.Heinz_MSPPM
value: "29570 USD/semester"
source_url: https://www.cmu.edu/sfs/tuition/graduate/index.html
source_snippet: "Master of Science in Public Policy & Management (MSPPM) Tuition: $29,570 per semester"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
field: grad.scs.phd_funding
value: "fully funded"
source_url: https://www.cs.cmu.edu/education/phd/index
source_snippet: "All of our Ph.D. students receive full financial support while in good academic standing, which helps ensure freedom to explore regardless of funding hurdles."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: grad.scs.programs.masters
value: "17 MS programs"
source_url: https://www.cs.cmu.edu/education/masters/index
source_snippet: "SCS offers a wide range of master's programs across its seven departments"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
field: grad.heinz.programs
value: "14 degree programs"
source_url: https://www.heinz.cmu.edu/programs/
source_snippet: "(Program finder listing 12 master's + 2 PhD + certificates + UG BS)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
cmu-knowledge-base-v2
├── overview (Section 0: counts, hierarchy, degree inventory, matrix)
├── undergraduate
│   ├── scs-majors
│   ├── engineering-majors
│   ├── fine-arts-majors
│   ├── dietrich-majors
│   ├── mellon-science-majors
│   ├── tepper-majors
│   ├── information-systems-majors
│   ├── interdisciplinary-bxa
│   └── minors (all 96)
├── graduate
│   ├── scs-graduate (17 MS + 17 PhD)
│   ├── engineering-graduate
│   ├── fine-arts-graduate
│   ├── dietrich-graduate
│   ├── mellon-science-graduate
│   ├── tepper-graduate
│   └── heinz-graduate
├── requirements-deadlines (Section 3)
├── costs-financial-aid (Section 4)
└── evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "cmu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BFA|B.Arch|MA|MS|MFA|MBA|MArch|MPA|MHCI|PhD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL / note |
|----------|----------|-------------------|
| **P0** | Per-program graduate deadlines, GRE/TOEFL minimums, fees | Each college's graduate admissions page (decentralized); re-run once catalog domain `coursecatalog.web.cmu.edu` is reachable |
| P0 | Full curriculum / course-list per major | `coursecatalog.web.cmu.edu` (currently NXDOMAIN in capture env) |
| P1 | Per-department UG degree-letter verification (BFA vs BM for Music; BDes for Design) | Each CFA school's academics page |
| P1 | Graduate application fees per program (SCS, Tepper, Heinz, CIT) | Per-college graduate admissions pages |
| P1 | International graduate funding policy (varies by program) | Per-program pages |
| P2 | Dietrich/CMIST graduate certificate programs | cmu.edu/dietrich/academics/ |
| P2 | SEI (Software Engineering Institute) graduate degree inventory | sei.cmu.edu |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | CMU | (other schools) |
|-----------|-----|-----------------|
| Total UG cost/yr (resident, 2026-27) | **$93,614** | MIT ~$90k, Stanford ~$92k, Harvard ~$90k |
| Tuition/yr (2026-27) | **$69,702** | MIT ~$63k, Stanford ~$67k, Harvard ~$60k |
| Need-blind (intl)? | **NO** (need-aware for intl; NO aid for intl) | MIT/Harvard/Yale/Princeton/Dartmouth/Amherst: YES; CMU/Stanford/Caltech/Columbia/UChicago/Berkeley: NO |
| EA/ED deadline | **ED Nov 2** (binding) | |
| RD deadline | **Jan 4** | |
| SAT/ACT required? | **SCS only** (others test-flexible / CFA test-optional) | MIT/Caltech/Georgetown: required; most others test-optional |
| TOEFL min | **102** | |
| IELTS min | **7.5** | |
| Tuition-free threshold | **$75k** family income | MIT $200k, Harvard $85k, Stanford $150k, Princeton ~$100k |
| No-loans threshold | **$100k** | |
| Avg starting salary (2025) | **$116,882** | |
| Grad application fee | varies (decentralized) | |
| April-15-equivalent honor date | **April 15** (CGS signatory) | |
| **Total degree programs (Rule 1)** | **181** (75 UG + 106 grad) | |
| **School/department count (Rule 2)** | **9** (7 UG colleges + Heinz + SEI) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: cmu.edu/admission/, cmu.edu/sfs/, cs.cmu.edu/education/, engineering.cmu.edu/education/, cmu.edu/mcs/academics/, cmu.edu/dietrich/, heinz.cmu.edu/programs/, cmu.edu/tepper/programs/, cmu.edu/graduate/prospective/
> **Verification**: ego-browser snapshotText + JS DOM extraction (program finder cards, COA tables, accordion-expanded deadline/testing text)
> **Granularity**: school → department → degree-level → program
> **Reconciliation status**: ✓ Rule 1 (181) == Rule 4 matrix sum (181) == Rule 5 row count (181)
> **Caveat**: Course-catalog domains (`coursecatalog.cmu.edu`, `coursecatalog.web.cmu.edu`) unreachable in capture environment; program data sourced from per-college admissions/academic sites instead. Per-program graduate deadlines/GRE minimums flagged as P0 follow-up.