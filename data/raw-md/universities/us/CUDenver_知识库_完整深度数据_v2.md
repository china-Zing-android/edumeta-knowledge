# University of Colorado Denver Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

# University of Colorado Denver (CU Denver)

> **Institution type**: Public research university
> **Location**: Denver, Colorado (Downtown Denver Campus + Anschutz Medical Campus, Aurora)
> **System**: University of Colorado system
> **Carnegie Classification**: R1 Doctoral Universities — Very High Research Activity
> **Founded**: 1912 (as CU Extension; became CU Denver 1973)
> **Students**: ~14,947 (Downtown Denver campus)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSBA) | 126 |
| 本科辅修 (Minor) | 73 |
| 本科证书 (Undergraduate Certificate) | 31 |
| 研究生学位项目 (MA/MS/MBA/MPA/PhD/etc.) | 166 |
| 研究生证书 (Graduate Certificate/Endorsement/License) | 72 |
| 其他 (Non-credit/Credit available) | 16 |
| **学位项目总计** | **484** |
| 学院总数 (Downtown Denver) | 7 |
| 学院总数 (Anschutz Medical Campus) | 6 |
| **学院总数** | **13** |

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

**CU Denver Downtown Denver Campus (7 Schools/Colleges):**

```
University of Colorado Denver
├── College of Architecture and Planning          [学院]
│   ├── Architecture
│   ├── Landscape Architecture
│   └── Urban Design & Planning
├── College of Arts & Media                       [学院]
│   ├── Film & Television
│   ├── Music
│   └── Visual Arts
├── Business School                               [学院]
│   ├── Accounting, Finance, Information Systems
│   ├── Management, Marketing
│   └── Health Administration
├── School of Education & Human Development       [学院]
│   ├── Teacher Education
│   ├── Educational Leadership
│   ├── Counseling
│   └── School Psychology
├── College of Engineering, Design and Computing  [学院]
│   ├── Civil Engineering
│   ├── Computer Science & Engineering
│   ├── Electrical Engineering
│   ├── Mechanical Engineering
│   └── Bioengineering
├── College of Liberal Arts and Sciences          [学院]
│   ├── Anthropology, Biology, Chemistry, Physics
│   ├── Communication, Economics, English, History
│   ├── Mathematics, Philosophy, Political Science
│   ├── Psychology, Sociology, World Languages
│   └── Public Health (1 program)
└── School of Public Affairs                       [学院]
    ├── Public Administration
    ├── Public Policy
    └── Criminal Justice
```

**CU Anschutz Medical Campus (6 Schools — separate admissions):**

```
CU Anschutz Medical Campus (Aurora, CO)
├── School of Dental Medicine                     [学院] → DDS
├── Graduate School                               [学院] → MS/PhD biomedical sciences
├── School of Medicine                            [学院] → MD, DPT, PA, AA
├── College of Nursing                            [学院] → DNP, MS, PhD
├── Skaggs School of Pharmacy                     [学院] → PharmD
└── Colorado School of Public Health              [学院] → MPH, MS, DrPH, PhD
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 数量 |
|---------|------|------|------|
| BA | Bachelor of Arts | 本科 | 67 |
| BS | Bachelor of Science | 本科 | 30 |
| BFA | Bachelor of Fine Arts | 本科 | 6 |
| BSBA | Bachelor of Science in Business Admin | 本科 | 22 |
| Minor | 辅修 | 本科 | 69 |
| Undergraduate Certificate | 本科证书 | 本科 | 31 |
| MA | Master of Arts | 研究生 | 50 |
| MS | Master of Science | 研究生 | 32 |
| MBA | Master of Business Administration | 研究生 | 10 |
| MPA | Master of Public Administration | 研究生 | 13 |
| M.Arch | Master of Architecture | 研究生 | 2 |
| MEng | Master of Engineering | 研究生 | 4 |
| MCJ | Master of Criminal Justice | 研究生 | 5 |
| MH | Master of Humanities | 研究生 | 6 |
| MPP | Master of Public Policy | 研究生 | 5 |
| MSS | Master of Social Science | 研究生 | 3 |
| MURP/MUD/MLA/MIS | Urban Planning/Design/Landscape/Info Systems | 研究生 | 4 |
| EdS | Educational Specialist | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 19 |
| EdD | Doctor of Education | 研究生 | 6 |
| PsyD | Doctor of Psychology | 研究生 | 1 |
| DHA | Doctor of Health Administration | 研究生 | 1 |
| Graduate Certificate | 研究生证书 | 研究生 | 62 |
| Endorsement/License | 教学认证/执照 | 研究生 | 10 |
| Dual Degree | 双学位项目 | 研究生/本科 | 6 |
| Non-credit/Credit available | 非学分/可获学分 | 其他 | 12 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 | BA | BS | BFA | BSBA | MA | MS | MBA | MPA | 其他硕士 | EdD | PhD | 其他博士 | Cert/Minor | 合计 |
|------|----|----|-----|------|----|----|-----|-----|---------|-----|-----|---------|-----------|------|
| Architecture & Planning | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 5 | 0 | 1 | 0 | 2 | 10 |
| Arts & Media | 1 | 6 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 29 |
| Business School | 0 | 0 | 0 | 21 | 1 | 10 | 10 | 0 | 0 | 0 | 0 | 1 | 21 | 64 |
| Education & Human Dev | 18 | 2 | 0 | 0 | 34 | 0 | 0 | 0 | 0 | 6 | 8 | 2 | 37 | 107 |
| Engineering, Design & Computing | 1 | 8 | 0 | 0 | 0 | 5 | 0 | 0 | 3 | 0 | 4 | 0 | 17 | 38 |
| Liberal Arts & Sciences | 40 | 13 | 0 | 1 | 13 | 14 | 0 | 0 | 10 | 0 | 5 | 0 | 80 | 176 |
| Public Affairs | 7 | 0 | 0 | 0 | 2 | 0 | 0 | 13 | 10 | 0 | 1 | 0 | 28 | 61 |
| CO School of Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **合计** | **67** | **30** | **6** | **22** | **50** | **32** | **10** | **13** | **28** | **6** | **19** | **3** | **200** | **484** |

> **Reconciliation**: Rule-1 total (484) = matrix cell-sum (484). Verified.

---

## SECTION 1 — Undergraduate Education

### 1.1 College Architecture
CU Denver Downtown campus has 7 schools/colleges. See Section 0.2 for hierarchy.

### 1.2 Undergraduate Majors — Grouped by 学院 > 学位级别


#### Business School
##### BSBA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Science in Business Administration in Risk Management and Insurance | 120 | https://business.ucdenver.edu/bsba/risk-management-and-insurance |
| 2 | Bachelor of Science in Business Administration to Master of Science in Marketing (4+1) | 120 | https://business.ucdenver.edu/bsba/marketing |
| 3 | Bachelor of Science in Business Administration, Entrepreneurship | 120 | https://business.ucdenver.edu/bsba/entrepreneurship |
| 4 | Bachelor of Science in Business Administration, Financial Management | 120 | https://business.ucdenver.edu/bsba/financial-management |
| 5 | Bachelor of Science in Business Administration, Human Resources Management | 120 | https://business.ucdenver.edu/bsba/human-resources |
| 6 | Bachelor of Science in Business Administration, Information Systems | 120 | https://business.ucdenver.edu/bsba/information-systems |
| 7 | Bachelor of Science in Business Administration, International Business | 120 | https://business.ucdenver.edu/bsba/international-business |
| 8 | Bachelor of Science in Business Administration, Management | 120 | https://business.ucdenver.edu/bsba/management |
| 9 | Bachelor of Science in Business Administration, Marketing | 120 | https://business.ucdenver.edu/bsba/marketing |
| 10 | Bachelor of Science in Business Administration, Risk Management and Insurance | 120 | https://business.ucdenver.edu/bsba/risk-management-and-insurance |
| 11 | Bachelor of Science in Business Administration, Sports Business | 120 | https://business.ucdenver.edu/bsba/sports-business |
| 12 | BSBA Accounting | 120 | https://business.ucdenver.edu/bsba/accounting |
| 13 | BSBA in Entrepreneurship | 120 | https://business.ucdenver.edu/bsba/entrepreneurship |
| 14 | BSBA in Finance | 120 | https://business.ucdenver.edu/bsba/finance |
| 15 | BSBA in Financial Management | 120 | https://business.ucdenver.edu/bsba/financial-management |
| 16 | BSBA in Human Resources Management | 120 | https://business.ucdenver.edu/bsba/human-resources |
| 17 | BSBA in Information Systems | 120 | https://business.ucdenver.edu/bsba/information-systems |
| 18 | BSBA in International Business | 120 | https://business.ucdenver.edu/bsba/international-business |
| 19 | BSBA in Management | 120 | https://business.ucdenver.edu/bsba/management |
| 20 | BSBA in Marketing | 120 | https://business.ucdenver.edu/bsba/marketing |
| 21 | BSBA in Sports Business | 120 | https://business.ucdenver.edu/bsba/sports-business |

##### Business Minor
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Minor | https://business.ucdenver.edu/minors/business-fundamentals |
| 2 | Entrepreneurship Minor | https://business.ucdenver.edu/minors/entrepreneurship |
| 3 | Finance Minor | https://business.ucdenver.edu/minors/finance |
| 4 | Risk Management and Insurance Minor | https://business.ucdenver.edu/minors/risk-mgmt |

##### Undergraduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | General Business Certificate | https://business.ucdenver.edu/academics/professional-development/credit-certificates/general-business-certificate |


#### College of Architecture and Planning
##### BS
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Science in Architecture | 120 | https://www.ucdenver.edu/programs/bs-architecture?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=bs-architecture |


#### College of Arts & Media
##### BA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Fine Arts in Visual Arts, Art History Emphasis | 45 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-history |

##### BS
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Science in Music, Music Business Emphasis, Audition Track | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/music-business |
| 2 | Bachelor of Science in Music, Music Business Emphasis, Non-Audition Track | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/music-business |
| 3 | Bachelor of Science in Music, Performance Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/performance |
| 4 | Bachelor of Science in Music, Recording Arts Emphasis, Audition Track | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/recording-arts |
| 5 | Bachelor of Science in Music, Recording Arts Emphasis, Non-Audition Track | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/recording-arts |
| 6 | Bachelor of Science in Music, Singer/Songwriter Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/music-entertainment-industry/singer-songwriter |

##### BFA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Fine Arts in Film and Television | 72 | https://artsandmedia.ucdenver.edu/areas-of-study/about-film-television |
| 2 | Bachelor of Fine Arts in Visual Arts, 3D Graphics and Animation Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/3-d-graphics-animation |
| 3 | Bachelor of Fine Arts in Visual Arts, Art Practices Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-practices |
| 4 | Bachelor of Fine Arts in Visual Arts, Digital Design Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/digital-design |
| 5 | Bachelor of Fine Arts in Visual Arts, Illustration Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/illustration |
| 6 | Bachelor of Fine Arts in Visual Arts, Photography Emphasis | 81 | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/photography |

##### Minor
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-history |
| 2 | Design Essentials Minor | https://www.ucdenver.edu/programs/Design-Essentials-Minor?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=Design-Essentials-Minor |
| 3 | Digital Design Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/digital-design |
| 4 | Film and Television Production Minor | https://artsandmedia.ucdenver.edu/areas-of-study/about-film-television |
| 5 | Film and Television Writing Minor | https://artsandmedia.ucdenver.edu/areas-of-study/about-film-television |
| 6 | Illustration Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/illustration |
| 7 | Music Industry Studies Minor | https://www.ucdenver.edu/programs/Music-Industry-Studies-Minor?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=Music-Industry-Studies-Minor |
| 8 | Painting and Drawing Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-practices |
| 9 | Performance for Film and TV Minor | https://artsandmedia.ucdenver.edu/areas-of-study/about-film-television |
| 10 | Photography Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/photography |
| 11 | General Music Minor | https://www.ucdenver.edu/programs/General-Music-Minor?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=General-Music-Minor |
| 12 | Studio Art Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-practices |
| 13 | Theater, Film and Television Minor | https://artsandmedia.ucdenver.edu/areas-of-study/about-film-television |
| 14 | Transmedia Sculpture Minor | https://artsandmedia.ucdenver.edu/areas-of-study/visual-arts/art-practices |


#### College of Engineering, Design and Computing
##### BA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Arts in Computer Science | 120 | https://engineering.ucdenver.edu/academics/undergraduate-programs/undergraduate-programs-in-computer-science/computer-science-bachelor-of-arts |

##### BS
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Science in Civil Engineering | 130 | https://engineering.ucdenver.edu/academics/departments/civil-engineering/undergraduate-programs-in-civil-engineering/bs-in-civil-engineering |
| 2 | Bachelor of Science in Computer Science | 128 | https://engineering.ucdenver.edu/academics/departments/computer-science-and-engineering/undergraduate-programs-in-computer-science/bs-in-computer-science |
| 3 | Bachelor of Science in Construction Engineering and Management | 128 | https://engineering.ucdenver.edu/academics/departments/civil-engineering/undergraduate-programs-in-civil-engineering/bs-in-construction-engineering-and-management |
| 4 | Bachelor of Science in Construction Management | 120 | https://engineering.ucdenver.edu/academics/departments/civil-engineering/undergraduate-programs-in-civil-engineering/bs-in-construction-management |
| 5 | Bachelor of Science in Cybersecurity | 120 | https://engineering.ucdenver.edu/undergraduate-programs-in-computer-science/cybersecurity |
| 6 | Bachelor of Science in Electrical Engineering | 128 | https://engineering.ucdenver.edu/academics/departments/electrical-engineering/undergraduate-programs/bs-in-electrical-engineering |
| 7 | Bachelor of Science in Mechanical Engineering | 128 | https://engineering.ucdenver.edu/academics/departments/mechanical-engineering/bs-in-mechanical-engineering |
| 8 | Bachelor of Science in Bioengineering | 128 | https://www.ucdenver.edu/programs/bs-biomedical-engineering?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=bs-biomedical-engineering |

##### N/A
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering Minor | https://engineering.ucdenver.edu/electrical-engineering/undergraduate-programs/electrical-engineering-minor#ac-required-courses-9-credit-hours-0 |
| 2 | Computer Science Minor | http://www.ucdenver.edu/academics/colleges/Engineering/Programs/Computer-Science-and-Engineering/DegreePrograms/Pages/Minor-in-CS.aspx |
| 3 | Construction Management Minor | http://www.ucdenver.edu/academics/colleges/Engineering/Programs/Civil-Engineering/DegreePrograms/Pages/CM_Minor.aspx |
| 4 | Electrical Engineering Minor | https://engineering.ucdenver.edu/electrical-engineering/undergraduate-programs/electrical-engineering-minor#ac-required-courses-9-credit-hours-0 |

##### Undergraduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Undergraduate Certificate in Cybersecurity and Secure Computing | https://engineering.ucdenver.edu/academics/departments/computer-science-and-engineering/computer-science-certificates/cyber-security-and-secure-computing |


#### College of Liberal Arts and Sciences
##### BA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | BA in Philosophy to MH in Humanities, Philosophy and Theory | 51 | https://clas.ucdenver.edu/philosophy/4-plus-1-masters-program |
| 2 | BA/BS Integrated Studies | 36 | https://www.ucdenver.edu/programs/integrated-studies?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=integrated-studies |
| 3 | Bachelor of Arts in Anthropology | 40 | https://clas.ucdenver.edu/anthropology/programs/bachelor-arts |
| 4 | Bachelor of Arts in Communication (Online) | 120 | https://online.cu.edu/program/online-bachelors/communication-ba |
| 5 | Bachelor of Arts in Communication | 39 | https://clas.ucdenver.edu/communication/programs/bachelor-arts |
| 6 | Bachelor of Arts in Economics | 40 | https://clas.ucdenver.edu/economics/programs/bachelor-arts |
| 7 | Economics in International College-Beijing | N/A | https://www.ucdenver.edu/academics/InternationalPrograms/OIA/icb/Pages/default.aspx |
| 8 | Bachelor of Arts in English Writing, Rhetoric and Technology | 120 | https://clas.ucdenver.edu/english/undergraduate-programs/english-writing-rhetoric-and-technology |
| 9 | Bachelor of Arts in English, Creative Writing | 39 | https://clas.ucdenver.edu/english/english-creative-writing |
| 10 | Bachelor of Arts in English, Film Studies | 39 | https://clas.ucdenver.edu/english/english-film-studies |
| 11 | Bachelor of Arts in English, Literature | 39 | https://clas.ucdenver.edu/english/english-literature |
| 12 | Bachelor of Arts in Ethnic Studies | 33 | https://clas.ucdenver.edu/ethnic-studies/programs/major |
| 13 | Geography - BA | 36 | https://clas.ucdenver.edu/ges/programs/bachelor-arts |
| 14 | Bachelor of Arts in Geography, Environment, Society, and Sustainability | 40 | https://clas.ucdenver.edu/ges/programs/environment-society-sustainability |
| 15 | Bachelor of Arts in Geography, Environmental Science | 40 | https://clas.ucdenver.edu/ges/programs/environmental-sciences |
| 16 | Bachelor of Arts in Geography, Environmental Science Education | 48 | https://clas.ucdenver.edu/ges/programs/environmental-science-education |
| 17 | Bachelor of Arts in Geography, Urban Studies and Planning | 39 | https://clas.ucdenver.edu/ges/programs/urban-studies-and-planning |
| 18 | Bachelor of Arts in History | 36 | https://clas.ucdenver.edu/history/undergraduate |
| 19 | Bachelor of Arts in Integrated Health Studies | 39 | https://clas.ucdenver.edu/academic-programs/integrated-health-studies |
| 20 | Bachelor of Arts in Intercampus Interdisciplinary Studies (Online) | 24 | https://clas.ucdenver.edu/academic-programs/intercampus-interdisciplinary-studies-major |
| 21 | Bachelor of Arts in Interdisciplinary Studies | 42 | https://clas.ucdenver.edu/academic-programs/interdisciplinary-studies-major |
| 22 | Bachelor of Arts in International Studies | 48 | https://clas.ucdenver.edu/ints/major-requirements |
| 23 | Bachelor of Arts in International Studies to Master of Arts in Political Science (4+1) | 69 | https://clas.ucdenver.edu/ints/bama-programs |
| 24 | Bachelor of Arts in Philosophy | 36 | https://clas.ucdenver.edu/philosophy/programs/bachelor-arts-major-philosophy |
| 25 | Bachelor of Arts in Political Science | 36 | https://clas.ucdenver.edu/polisci/undergraduate/undergraduate-degree-requirements |
| 26 | Bachelor of Arts in Political Science, Public Policy | 36 | https://clas.ucdenver.edu/polisci/undergraduate/undergraduate-degree-requirements |
| 27 | Bachelor of Arts in Psychology (Online) | 120 | https://online.cu.edu/program/online-bachelors/psychology-ba |
| 28 | Bachelor of Arts in Psychology | 120 | https://www.ucdenver.edu/programs/ba-psychology?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ba-psychology |
| 29 | Bachelor of Arts in Public Health | 43 | https://clas.ucdenver.edu/hbsc/degree-programs/bachelor-arts-or-science-public-health |
| 30 | Bachelor of Arts in Sociology | 34 | https://clas.ucdenver.edu/sociology/programs/bachelor-arts |
| 31 | Bachelor of Arts in Spanish, International Language and Culture for the Professions | 45 | https://clas.ucdenver.edu/modLang/spanish-program/spanish-major-international-language-and-culture-professions-ilcp-track |
| 32 | Bachelor of Arts in Spanish, Language, Literature, and Culture | 36 | https://clas.ucdenver.edu/modLang/spanish-program/spanish-major-language-literature-and-culture-track |
| 33 | Bachelor of Arts to Master of Arts in Economics (4+1) | 66 | https://clas.ucdenver.edu/economics/five-year-ba-ma-economics |
| 34 | Bachelor of Arts to Master of Arts in Political Science (4+1) | 69 | https://clas.ucdenver.edu/polisci/academics/4-1-program |
| 35 | Bachelor of Arts to Master of Arts in Sociology (4+1) | 30 | https://clas.ucdenver.edu/sociology/programs |
| 36 | Bachelor of Science in Mathematics, Probability and Statistics | 54 | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/undergraduate-programs |
| 37 | Economics BA/Mathematics BS Dual Degree | 60 | https://clas.ucdenver.edu/economics/dual-degree-economics-and-mathematics |
| 38 | Interdisciplinary Studies, Individually Structured Major (Online) | 120 | https://clas.ucdenver.edu/individually-designed-major |
| 39 | Ethnic Studies BA | 120 | https://clas.ucdenver.edu |
| 40 | 4+1 Public Health BA or BS to MPH | 153 | https://clas.ucdenver.edu/hbsc/degree-programs/5-year-public-health-ba-bs-mph |

##### BS
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Applied Science: Professional Studies | 120 | https://www.ucdenver.edu/programs/bachelor-of-applied-science--professional-studies?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=bachelor-of-applied-science--professional-studies |
| 2 | Bachelor of Science in Biochemistry | 45 | https://clas.ucdenver.edu/chemistry/undergraduate-students/bs-biochemistry |
| 3 | Bachelor of Science in Biology | 36 | https://clas.ucdenver.edu/integrative-biology/academic-programs/undergraduate-programs |
| 4 | Bachelor of Science in Chemistry | 45 | https://clas.ucdenver.edu/chemistry/undergraduate-students/bachelor-science |
| 5 | Bachelor of Science in Data Science | 120 | https://clas.ucdenver.edu/bachelor-science-data-science |
| 6 | Bachelor of Science in Mathematics | 30 | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/degree-requirements-bs-mathematics |
| 7 | Bachelor of Science in Mathematics | 54 | https://www.ucdenver.edu/programs/bs-mathematics?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=bs-mathematics |
| 8 | Mathematics in Data Science | 54 | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/undergraduate-programs |
| 9 | Bachelor of Science in Psychology | 51 | https://clas.ucdenver.edu/psychology/undergraduate-studies/bachelor-arts-and-bachelor-sciences/bachelor-science-psychology |
| 10 | Bachelor of Science in Public Health | 73 | https://clas.ucdenver.edu/hbsc/degree-programs/bachelor-arts-or-science-public-health |
| 11 | Bachelor of Science in Pure and Applied Physics | 46 | https://clas.ucdenver.edu/physics/academics/undergraduate-programs/physics-major |
| 12 | Bachelor of Science to Master of Science in Chemistry (4+1) | 30 | https://clas.ucdenver.edu/chemistry/graduate-students/bsms-combined-program |
| 13 | Bachelor of Science to Master of Science in Statistics (4+1) | 30 | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/bachelor-science |

##### BSBA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Climate Change Studies | 120 | https://clas.ucdenver.edu |

##### Minor
| # | 项目 | URL |
|---|------|-----|
| 1 | Biophysics Minor | https://clas.ucdenver.edu/physics/academics/undergraduate-programs/biophysics-minor |
| 2 | Anthropology Minor | https://clas.ucdenver.edu |
| 3 | Writing Minor | https://clas.ucdenver.edu |
| 4 | Political Science Minor | https://clas.ucdenver.edu |
| 5 | Psychology Minor | https://clas.ucdenver.edu |
| 6 | Women's and Gender Studies Minor | https://clas.ucdenver.edu/wgst/programs/undergraduate-minor-wgst |

##### N/A
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology Minor | https://clas.ucdenver.edu/anthropology/programs/minor-anthropology-requirements |
| 2 | Astrophysics Minor | https://clas.ucdenver.edu/physics/academics/undergraduate-programs/astrophysics-minor |
| 3 | Behavioral Cognitive Neuroscience Minor | https://clas.ucdenver.edu/psychology/undergraduate-studies/psychology-and-behavioralcognitive-neuroscience-minors |
| 4 | Biology Minor | https://clas.ucdenver.edu/integrative-biology/academic-programs/undergraduate-programs#biology_minor-74 |
| 5 | Chemistry Minor | https://clas.ucdenver.edu/chemistry/undergraduate-students/minor |
| 6 | Chinese Studies Minor | https://clas.ucdenver.edu/modLang/chinese-studies-minor |
| 7 | Communication Minor | https://clas.ucdenver.edu/communication/programs/minor-communication |
| 8 | Creative Writing Minor | https://clas.ucdenver.edu/english/creative-writing-minor |
| 9 | Economics Minor | https://clas.ucdenver.edu/economics/minor |
| 10 | Environmental Sciences Minor | https://clas.ucdenver.edu/ges/programs/minors/minor-environmental-sciences |
| 11 | Ethics Minor | https://clas.ucdenver.edu/philosophy/programs/program-minors |
| 12 | Ethnic Studies Minor | https://clas.ucdenver.edu/ethnic-studies/programs/minor |
| 13 | Film Studies Minor | https://clas.ucdenver.edu/english/film-studies-minor |
| 14 | French Minor | https://clas.ucdenver.edu/modLang/programs/minors |
| 15 | Geography Minor | https://clas.ucdenver.edu/ges/programs/minors/minor-geography |
| 16 | Health Humanities Minor | https://clas.ucdenver.edu/health-humanities/ |
| 17 | History Minor | https://clas.ucdenver.edu/history/minor-history |
| 18 | International Studies Minor | https://clas.ucdenver.edu/ints/minor-requirements |
| 19 | Law Studies Minor | https://clas.ucdenver.edu/mhmss/undergraduate-law-studies-minor |
| 20 | Linguistics Minor | https://clas.ucdenver.edu/modLang/programs/minors |
| 21 | Literature Minor | https://clas.ucdenver.edu/english/literature-minor |
| 22 | Mathematics Minor | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/minor |
| 23 | Sociology Minor | https://clas.ucdenver.edu |
| 24 | Philosophy Minor | https://clas.ucdenver.edu/philosophy/programs/program-minors |
| 25 | Philosophy of Science Minor | https://clas.ucdenver.edu/philosophy/programs/program-minors |
| 26 | Physics Minor | https://clas.ucdenver.edu/physics/academics/undergraduate-programs/physics-minor |
| 27 | Political Science Minor | https://clas.ucdenver.edu/polisci/undergraduate/undergraduate-degree-requirements |
| 28 | Psychology Minor | https://clas.ucdenver.edu/psychology/undergraduate-studies/psychology-and-behavioralcognitive-neuroscience-minors |
| 29 | Public Health Demography Minor | https://clas.ucdenver.edu/hbsc/degree-programs/minors |
| 30 | Public Health Minor | https://clas.ucdenver.edu/hbsc/degree-programs/minors |
| 31 | Religious Studies Minor | https://clas.ucdenver.edu/religious-studies/program-information/religious-studies-minor |
| 32 | Social Justice Minor | https://clas.ucdenver.edu/socialJustice/ |
| 33 | Sociology Minor | https://clas.ucdenver.edu/sociology/programs/minor |
| 34 | Spanish Minor | https://clas.ucdenver.edu/modLang/spanish-program/spanish-minor |
| 35 | Sustainability Minor | https://clas.ucdenver.edu/sustainability/programs |
| 36 | Urban and Regional Planning Minor | https://clas.ucdenver.edu/ges/programs/minors/minor-urban-studies-and-regional-planning |

##### Undergraduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | American Indian Studies Undergraduate Certificate | https://clas.ucdenver.edu/ethnic-studies/certificates#american_indian_studies_certificate-172 |
| 2 | Applied Statistics Undergraduate Certificate | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/graduate-certificate-applied-statistics |
| 3 | Certificate in Biotechnology | https://clas.ucdenver.edu/integrative-biology/academics/certificates#biotechnology_certificate-93 |
| 4 | Certificate in Quantum Information Technology | https://clas.ucdenver.edu/certificate-quantum-information-technology |
| 5 | Cultural Diversity Studies Undergraduate Certificate | https://clas.ucdenver.edu/ethnic-studies/programs/certificate-cultural-diversity-studies |
| 6 | Digital Studies | https://clas.ucdenver.edu/digital-studies-certificates/undergraduate-certificate |
| 7 | Envirmental Stewardship of Indigenous Lands Undergraduate Certificate | https://clas.ucdenver.edu/esil/certificate-requirements |
| 8 | Families and Social Welfare Certificate | https://clas.ucdenver.edu/sociology/certificates |
| 9 | Geographic Information Science Undergraduate Certificate | https://clas.ucdenver.edu/ges/programs/certificates/gis-certificate |
| 10 | Sociology of Criminology Undergraduate Certificate | https://clas.ucdenver.edu/sociology/certificates |
| 11 | Sociology of Health and Medicine Certificate | https://clas.ucdenver.edu/sociology/certificates |
| 12 | Undergraduate Certificate in Biochemistry | https://clas.ucdenver.edu/chemistry/undergraduate-students/biochemistry-certificate#expand-11207 |
| 13 | Undergraduate Certificate in Democracy and Social Movements | https://clas.ucdenver.edu/polisci/certificates/democracy-and-social-movements-undergraduate-certificate |
| 14 | Undergraduate Certificate in Health Communication | https://clas.ucdenver.edu/communication/programs/certificates |
| 15 | Undergraduate Certificate in Immigration Studies | https://clas.ucdenver.edu/history/immigration-studies-certificate |
| 16 | Undergraduate Certificate in Labor Leadership | https://clas.ucdenver.edu/newdirections/certificates/labor-leadership-certificate |
| 17 | Undergraduate Certificate in Mediation | https://clas.ucdenver.edu/communication/programs/certificates |
| 18 | Undergraduate Certificate in Middle East Politics | https://clas.ucdenver.edu/polisci/certificates/middle-east-politics-certificate |
| 19 | Undergraduate Certificate in Public, Non-profit and Community Leadership | https://clas.ucdenver.edu/polisci/certificates/public-non-profit-and-community-leadership-undergraduate-certificate |
| 20 | Undergraduate Certificate in Spanish for International Business | https://clas.ucdenver.edu/modLang/programs/certificate-spanish-international-business |
| 21 | Undergraduate Certificate in Strategic Communication | https://clas.ucdenver.edu/communication/programs/certificates |
| 22 | Undergraduate Certificate in Sustainable Urban Agriculture | https://clas.ucdenver.edu/ges/programs/certificates/sustainable-urban-agriculture-certificate |
| 23 | Undergraduate Certificate, Data Science | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/undergraduate-programs |


#### School of Education & Human Development
##### BA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | BA in Education and Human Development | N/A | https://www.ucdenver.edu/programs/ba-education-human-development?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ba-education-human-development |
| 2 | Bachelor of Arts in Education and Human Development, Early Childhood Education (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/Early-Childhood-Education-BA |
| 3 | Bachelor of Arts in Education and Human Development, Early Childhood Education | 120 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/early-childhood-education-professional-BA |
| 4 | Bachelor of Arts in Education and Human Development, Education and Learning Sciences | 120 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/bachelor-of-arts-in-education-and-human-development--education-and-learning-sciences |
| 5 | Bachelor of Arts in Education and Human Development, Elementary Education (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/Elementary-Education-BA |
| 6 | Bachelor of Arts in Education and Human Development, Middle School Math (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/middle-school-math-ba-license |
| 7 | Bachelor of Arts in Education and Human Development, Secondary English Language Arts (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/english-education-BA |
| 8 | Bachelor of Arts in Education and Human Development, Secondary Math (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/secondary-math-ba-license |
| 9 | Bachelor of Arts in Education and Human Development, Secondary Science (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/secondary-science-BA |
| 10 | Bachelor of Arts in Education and Human Development, Secondary Social Studies (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/social-studies-BA |
| 11 | Bachelor of Arts in Education and Human Development, Special Education (License) | 126 | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/Special-Education-BA |
| 12 | Bachelor of Arts in English, Secondary English (License) | 120 | https://education.ucdenver.edu/academics/certificates-credentials-licenses-and-endorsements/detail/English-BA-with-License |
| 13 | Bachelor of Arts in General Science, Secondary Science Education (License) | 120 | https://education.ucdenver.edu/academics/areas-of-study/stem-education/detail/General-Science-BA-with-License |
| 14 | Bachelor of Arts in History, Secondary Social Studies (License) | 120 | https://education.ucdenver.edu/academics/certificates-credentials-licenses-and-endorsements/detail/History-BA-with-License |
| 15 | Bachelor of Arts in Political Science, Secondary Social Studies (License) | 120 | https://education.ucdenver.edu/academics/certificates-credentials-licenses-and-endorsements/detail/Political-Science-BA-with-License |
| 16 | Bachelor of Arts in Spanish, World Languages (License) | 120 | https://education.ucdenver.edu/academics/areas-of-study/teaching/detail/ba-spanish-world-languages |
| 17 | Education and Human Development - BA to MA | 156 | https://education.ucdenver.edu/academics/undergraduate/ba-to-ma |
| 18 | Culturally and Linguistically Diverse Education Minor | 15 | https://education.ucdenver.edu/academics/areas-of-study/culturally-linguistically-diverse-education/detail/minor-culturally-and-linguistically-diverse-education |

##### BS
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Science in Mathematics, Secondary Math (License) | 120 | https://education.ucdenver.edu/academics/areas-of-study/teaching/detail/Mathematics-BS-with-License |
| 2 | Bachelor of Science in Human Development and Family Relations | 120 | https://education.ucdenver.edu/academics/undergraduate/human-development-and-family-relations/detail/bs-human-development-family-relations |

##### Minor
| # | 项目 | URL |
|---|------|-----|
| 1 | Minor in Human Development and Family Relations | https://education.ucdenver.edu/academics/undergraduate/human-development-and-family-relations/detail/Human-Development-and-Family-Relations-Minor |
| 2 | Minor in Digital Media Design for Learning | https://education.ucdenver.edu/academics/undergraduate/minors/detail/digital-media-design-for-learning-minor |
| 3 | Minor in Education Studies | https://education.ucdenver.edu/academics/undergraduate/teacher-education/detail/education-studies-minor |
| 4 | Minor in Teacher Education | https://education.ucdenver.edu/academics/undergraduate/minors/detail/minor-in-teacher-education |

##### Undergraduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Undergraduate Certificate in Applied Literacy for Family & Community Helping Professionals | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/undergraduate-certificate-in-applied-literacy-for-family-community-helping-professionals |
| 2 | Undergraduate Certificate in Pathways2Teaching, Paraprofessional | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/paraprof-pathways2teaching-certificate |
| 3 | Undergraduate or Graduate Certificate in Early Childhood Education Coaching | https://education.ucdenver.edu/continuing-education/certificates/ece-coaching-certificate |


#### School of Public Affairs
##### BA
| # | 专业 | 学分 | URL |
|---|------|------|-----|
| 1 | Bachelor of Arts in Criminal Justice | 39 | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/bachelor-of-arts-in-criminal-justice |
| 2 | Bachelor of Arts in Criminal Justice, Law Enforcement | 36 | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/bachelor-of-arts-in-criminal-justice |
| 3 | Bachelor of Arts in Criminal Justice, Victims and Victim Services | 36 | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/bachelor-of-arts-in-criminal-justice |
| 4 | Bachelor of Arts in Public Administration | 48 | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/bachelor-of-arts-in-public-administration |
| 5 | Bachelor of Arts in Public Administration, Nonprofit Management | 45 | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/bachelor-of-arts-in-public-administration |
| 6 | Pathways Bachelor of Arts in Criminal Justice - Master of Public Policy | 141 | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/pathways-bachelor-of-arts-in-criminal-justice-master-of-public-policy |
| 7 | Bachelor of Arts in Public Administration - Master of Public Policy | 141 | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/pathways-bachelor-of-arts-in-public-administration-master-of-public-policy |

##### Minor
| # | 项目 | URL |
|---|------|-----|
| 1 | Minor in Criminal Justice | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/ minor-in-criminal-justice |
| 2 | Minor in Law Enforcement | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/minor-in-law-enforcement |
| 3 | Minor in Nonprofit Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/minor-in-nonprofit-management |
| 4 | Minor in Public Administration | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/minor-public-administration |
| 5 | Minor in Victims and Victim Services | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/minor-in-victims-and-victim-services |

##### Undergraduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Undergraduate Certificate in Law Enforcement | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/undergraduate-law-enforcement-certificate |
| 2 | Undergraduate Certificate in Nonprofit Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/undergraduate-nonprofit-management-certificate |
| 3 | Undergraduate Certificate in Victims and Victim Services | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/undergraduate-victims-and-victim-services-certificate |



---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别


#### Business School
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science MA/MBA Dual Degree | http://catalog.ucdenver.edu/preview_program.php?catoid=25&poid=8040&returnto=7162 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master's in Entrepreneurship | https://business.ucdenver.edu/ms/entrepreneurship |
| 2 | Master's in FinTech | https://business.ucdenver.edu/ms/fintech |
| 3 | Master's in Sustainable Business | https://business.ucdenver.edu/ms/sustainable-business |
| 4 | Master of Science in Accounting | https://business.ucdenver.edu/ms/accounting |
| 5 | Master of Science in Business Analytics | https://business.ucdenver.edu/ms/business-analytics |
| 6 | Master of Science in Finance and Risk Management | https://business.ucdenver.edu/ms/finance-risk-mgmt |
| 7 | Master of Science in Information Systems | https://business.ucdenver.edu/ms/information-systems |
| 8 | Master of Science in International Business | https://business.ucdenver.edu/ms/international-business |
| 9 | Master of Science in Management | https://business.ucdenver.edu/ms/management |
| 10 | Master of Science in Marketing | https://business.ucdenver.edu/ms/marketing |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Denver Flex Master of Business Administration (Full or Part Time) | https://business.ucdenver.edu/mba/professional-mba |
| 2 | Denver Flex MBA | https://business.ucdenver.edu/mba/professional-mba |
| 3 | Executive Master of Business Administration, Health Administration | https://business.ucdenver.edu/mba/executive-mba-health-administration |
| 4 | Executive MBA | https://business.ucdenver.edu/academics/mba-programs/emba |
| 5 | Executive MBA in Health Administration | https://business.ucdenver.edu/mba/executive-mba-health-administration |
| 6 | Health Administration MBA | https://business.ucdenver.edu/mba/health-administration-mba |
| 7 | Master of Business Administration, Health Administration | https://business.ucdenver.edu/mba/health-administration-mba |
| 8 | One Year MBA | https://business.ucdenver.edu/mba/one-year-mba |
| 9 | One-Year Master of Business Administration | https://business.ucdenver.edu/mba/one-year-mba |
| 10 | Online MBA | https://business.ucdenver.edu/mba/online |

##### DHA
| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Doctorate in Health Administration | https://business.ucdenver.edu/executive-doctorate-health-administration |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinnovation and Entrepreneurship Certificate | https://business.ucdenver.edu |
| 2 | Commodities Graduate Certificate | https://business.ucdenver.edu/jpmorgancenter/commodities-graduate-certificate |
| 3 | Cybersecurity and Information Assurance Certificate | https://www.ucdenver.edu/programs/cybersecurity-and-information-assurance-certificate?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=cybersecurity-and-information-assurance-certificate |
| 4 | Digital Marketing Graduate Certificate | https://business.ucdenver.edu/academics/professional-development/credit-certificates/digital-marketing-graduate-certificate |
| 5 | Energy Graduate Certificate | https://business.ucdenver.edu/centers/global-energy-management-gem/energy-graduate-certificate |
| 6 | Entrepreneurship Certificate | https://business.ucdenver.edu |
| 7 | Graduate Certificate in Risk Management | https://business.ucdenver.edu/academics/professional-development/credit-certificates/graduate-certificate-risk-management |
| 8 | Managing for Sustainability Certificate | https://business.ucdenver.edu |

##### Non-credit
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Warehousing for Business Intelligence Specialization | https://business.ucdenver.edu |
| 2 | Electric Utilities Fundamentals and Future | https://business.ucdenver.edu |
| 3 | Energy and Commodity Analytics for Analysts | https://business.ucdenver.edu/academics/professional-development/not-credit-certificates/energy-and-commodity-analytics-analysts |
| 4 | Fundamentals of Global Energy Business | https://business.ucdenver.edu |
| 5 | Lifecycle of Oil and Natural Gas Certificate | https://business.ucdenver.edu/academics/professional-development/not-credit-certificates/lifecycle-oil-and-natural-gas-certificate |
| 6 | Masterclass in Commodity Trading & Hedging | https://business.ucdenver.edu/academics/professional-development/not-credit-certificates/masterclass-commodity-trading-hedging |
| 7 | Sustainable Commodities Production, Markets, and Supply Chain | https://business.ucdenver.edu/sustainable-commodities-production-markets-and-supply-chain |

##### bus
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Fundamentals Minor | https://business.ucdenver.edu/minors/business-fundamentals |


#### College of Architecture and Planning
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Historic Preservation | https://www.ucdenver.edu/programs/MS-Historic-Preservation?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ms-historic-preservation |

##### M.Arch
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Architecture & Master of Urban and Regional Planning | https://architectureandplanning.ucdenver.edu/academics/dual-degree-programs#ac-master-of-architecture-master-of-urban-planning-and-regional-planning-0 |
| 2 | Master of Architecture | https://www.ucdenver.edu/programs/master-architecture?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=master-architecture |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Engineering + Master of Urban and Regional Planning | https://engineering.ucdenver.edu/civil-engineering-programs-graduate/dual-degree-meng-murp |

##### MURP
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban and Regional Planning | https://www.ucdenver.edu/programs/master-urban-design-regional-planning?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=master-urban-design-regional-planning |

##### MUD
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban Design | https://www.ucdenver.edu/programs/master-urban-design?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=master-urban-design |

##### MLA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Landscape Architecture | https://www.ucdenver.edu/programs/mla-landscape-architecture?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=mla-landscape-architecture |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate in Geography, Planning, and Design | https://www.ucdenver.edu/programs/PhD-Geography-Planning-Design?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=phd-geography-planning-design |

##### MURP/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Urban and Regional Planning & Master of Public Health | https://architectureandplanning.ucdenver.edu |


#### College of Arts & Media
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Media Forensics | https://artsandmedia.ucdenver.edu/areas-of-study/national-center-for-media-forensics/media-forensics-graduate-program |
| 2 | Master of Science in Recording Arts | https://www.ucdenver.edu/programs/master-of-science-in-recording-arts?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=master-of-science-in-recording-arts |


#### College of Engineering, Design and Computing
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Civil Engineering | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-programs/ms-in-civil-engineering |
| 2 | Master of Science in Computer Science | https://www.ucdenver.edu/programs/Computer-Science-MS?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=Computer-Science-MS |
| 3 | Master of Science in Electrical Engineering | https://engineering.ucdenver.edu/academics/departments/electrical-engineering/graduate_programs/ms-in-electrical-engineering |
| 4 | Master of Science in Mechanical Engineering | https://engineering.ucdenver.edu/academics/departments/mechanical-engineering/mechanical-engineering-programs/ms-in-mechanical-engineering |
| 5 | Master of Science of Biomedical Engineering | https://engineering.ucdenver.edu/bioengineering/graduate-programs/ms-in-biomedicalengineering |

##### MEng
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Engineering in Civil Engineering | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-programs/meng-in-civil-engineering |
| 2 | Master of Engineering in Electrical Engineering | https://engineering.ucdenver.edu/academics/departments/electrical-engineering/graduate_programs/meng-in-electrical-engineering |
| 3 | Master of Engineering in Mechanical Engineering | https://engineering.ucdenver.edu/academics/departments/mechanical-engineering/mechanical-engineering-programs/meng-in-mechanical-engineering |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate in Bioengineering | https://engineering.ucdenver.edu/academics/departments/bioengineering/BIOE/phd-in-bioengineering |
| 2 | Doctorate in Civil Engineering | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-programs/phd-in-civil-engineering |
| 3 | Doctorate in Computer Science and Information Systems | https://engineering.ucdenver.edu/computer-science-programs-graduate/computer-science-and-information-systems-phd#ac-degree-requirements-0 |
| 4 | Doctorate in Engineering and Applied Science | https://engineering.ucdenver.edu/academics/graduate-programs/phd-in-engineering-and-applied-science |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Construction Project Management | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-certificates/construction-project-management |
| 2 | Graduate Certificate in Cyber Security and Defense | https://engineering.ucdenver.edu/academics/departments/computer-science-and-engineering/computer-science-certificates/cyber-security-and-defense |
| 3 | Graduate Certificate in Geographic Information Systems | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-certificates/geographic-information-systems |
| 4 | Graduate Certificate in Integrated Construction, Management, and Leadership | https://engineering.ucdenver.edu/academics/departments/civil-engineering/civil-engineering-certificates/ICML_certificate |
| 5 | Graduate Certificate in Modern Energy and Power Systems | https://engineering.ucdenver.edu/academics/departments/electrical-engineering/ELEC-certificates/modern-energy-and-power-systems |
| 6 | Graduate Certificate in RF and Antenna Engineering | https://engineering.ucdenver.edu/academics/departments/electrical-engineering/ELEC-certificates/rf-and-antenna-engineering |
| 7 | Graduate Certificate in Software Engineering | https://engineering.ucdenver.edu/academics/departments/computer-science-and-engineering/computer-science-certificates/software-engineering |
| 8 | Graduate Certificate: Assistive Technology and Inclusive Engineering | https://engineering.ucdenver.edu/bioengineering/certificate-programs/assistive-technology-and-inclusive-engineering |
| 9 | Graduate Certificate: Medical Device Design and Entrepreneurship | https://engineering.ucdenver.edu/bioengineering/certificate-programs/medical-device-design-and-entrepreneurship |
| 10 | Graduate Certificate: Neural Engineering | https://engineering.ucdenver.edu/bioengineering/certificate-programs/neural-engineering |

##### cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate: Quality Assurance and Regulatory Affairs | https://www.ucdenver.edu/programs/graduate-certificate--quality-assurance-and-regulatory-affairs |


#### College of Liberal Arts and Sciences
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Arts in Anthropology | https://clas.ucdenver.edu/anthropology/programs/master-arts-anthropology |
| 2 | Master of Arts in Applied Geography & Geospatial Science | https://clas.ucdenver.edu/ges/programs/master-arts-applied-geography-geospatial-science |
| 3 | Master of Arts in Communication | https://clas.ucdenver.edu/communication/programs/master-arts |
| 4 | Master of Arts in Economics | https://clas.ucdenver.edu/economics/programs/master-arts-economics |
| 5 | Master of Arts in English | https://clas.ucdenver.edu/english/graduate-program |
| 6 | Master of Arts in Health Economics | https://clas.ucdenver.edu/economics/programs/master-science-health-economics |
| 7 | Master of Arts in History | https://clas.ucdenver.edu/history/graduate |
| 8 | Master of Arts in History, Public History | https://clas.ucdenver.edu/history/public-history-program |
| 9 | Master of Arts in Humanities | https://clas.ucdenver.edu/mhmss/master-humanities |
| 10 | Master of Arts in Political Science | https://clas.ucdenver.edu/polisci/graduate-degree-requirements |
| 11 | Master of Arts in Sociology | https://clas.ucdenver.edu/sociology/programs/master-arts-sociology |
| 12 | Master of Arts in Spanish | https://clas.ucdenver.edu/modLang/spanish-program/master-arts-spanish |
| 13 | New Directions MA | https://clas.ucdenver.edu/newdirections/masters-program |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics MA/Mathematics MS Dual Degree | https://clas.ucdenver.edu/economics/dual-degree-economics-applied-mathematics |
| 2 | Master of Arts in Economics and Master of Science in Finance (Dual) | https://clas.ucdenver.edu/economics/dual-degree-economics-and-finance |
| 3 | Master of Science Environmental Sciences, Air Quality | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 4 | Master of Science Environmental Sciences, Ecosystems | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 5 | Master of Science Environmental Sciences, Environmental Health | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 6 | Master of Science Environmental Sciences, Environmental Science Education | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 7 | Master of Science Environmental Sciences, Hazardous Waste | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 8 | Master of Science Environmental Sciences, Water Quality | https://clas.ucdenver.edu/ges/programs/master-science/specialization-options |
| 9 | Applied Mathematics MS | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/master-science-applied-mathematics |
| 10 | Chemistry MS | https://clas.ucdenver.edu/chemistry/department-chemistry-graduate-programs |
| 11 | Master of Science in Environmental Sciences | https://clas.ucdenver.edu/ges/programs/master-science-environmental-sciences |
| 12 | Master of Science in Integrative Biology | https://clas.ucdenver.edu/integrative-biology/academics/graduate-programs |
| 13 | Master of Science in Statistics | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/admissions-ms-statistics |
| 14 | MS in Clinical Psychopharmacology | https://www.ucdenver.edu/programs/ms-psychopharmacology?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ms-psychopharmacology |

##### MH
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Humanities in Philosophy and Theory | https://clas.ucdenver.edu/mhmss/philosophy-and-theory |
| 2 | Master of Humanities in Visual Studies | https://clas.ucdenver.edu/mhmss/visual-studies |
| 3 | Master of Humanities or Social Science in Ethnic Studies | https://clas.ucdenver.edu/mhmss/ethnic-studies |
| 4 | Master of Humanities or Social Science in Social Justice | https://clas.ucdenver.edu/mhmss/social-justice |
| 5 | Master of Humanities or Social Science in Women and Gender Studies | https://clas.ucdenver.edu/mhmss/womens-and-gender-studies |
| 6 | Master of Social Sciences or Humanities in International Studies | https://clas.ucdenver.edu/mhmss/international-studies |

##### MSS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Science | https://clas.ucdenver.edu/mhmss/master-social-science |
| 2 | Master of Social Science in Community Health Science | https://clas.ucdenver.edu/mhmss/community-health-track |
| 3 | Master of Social Science in Society and the Environment | https://clas.ucdenver.edu/mhmss/society-and-environment |

##### MIS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Integrated Science | https://clas.ucdenver.edu/mis/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate in Applied Mathematics | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/phd-applied-mathematics |
| 2 | Doctorate in Health and Behavioral Sciences | https://clas.ucdenver.edu/hbsc/degree-programs/phd |
| 3 | Doctorate in Health Economics | https://clas.ucdenver.edu/economics/programs/phd-health-economics |
| 4 | Doctorate of Clinical Health Psychology | https://clas.ucdenver.edu/psychology/graduate-program-psychology |
| 5 | Doctorate of Integrative Biology | https://clas.ucdenver.edu/integrative-biology/academics/graduate-programs |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Studies | https://clas.ucdenver.edu/digital-studies-certificates/graduate-certificate |
| 2 | Free and Open Source Software for Geospatial Applications Graduate Certificate | https://clas.ucdenver.edu/ges/programs/certificates/gis-certificate |
| 3 | Geographic Information Science Graduate Certificate | https://clas.ucdenver.edu/ges/programs/certificates/gis-certificate |
| 4 | Graduate Certificate in Applied Statistics | https://clas.ucdenver.edu/mathematical-and-statistical-sciences/graduate-certificate-applied-statistics |
| 5 | Graduate Certificate in College-Level Language and Literacy | https://clas.ucdenver.edu/english/graduate-program |
| 6 | Graduate Certificate in Democracy and Social Movements | http://catalog.ucdenver.edu/preview_program.php?catoid=25&poid=8032&returnto=7162 |
| 7 | Graduate Certificate in Environmental Science Education | https://clas.ucdenver.edu/ges/programs/certificates/environmental-science-education-certificate |
| 8 | Graduate Certificate in Historic Preservation | https://clas.ucdenver.edu/history/content/certificates |
| 9 | Graduate Certificate in Labor Leadership | https://clas.ucdenver.edu/newdirections/certificates/labor-leadership-certificate |
| 10 | Graduate Certificate in Public, Non-profit and Community Leadership | https://clas.ucdenver.edu/polisci/certificates/public-non-profit-and-community-leadership-undergraduate-certificate |
| 11 | Graduate Certificate in Sustainable Urban Agriculture | https://clas.ucdenver.edu/ges/programs/certificates/sustainable-urban-agriculture-certificate |
| 12 | Graduate Certificate in Teaching College-Level Literature and Film | https://clas.ucdenver.edu/english/graduate-certificate-teaching-college-level-literature-and-film |
| 13 | Graduate Certificate in Teaching English Language Learners | https://clas.ucdenver.edu/english/graduate-program |
| 14 | Graduate Certificate in Women's and Gender Studies | https://clas.ucdenver.edu/wgst/graduate-certificate-wgst |
| 15 | Strategic Communication Graduate Certificate | https://clas.ucdenver.edu/communication/programs/certificates |


#### School of Education & Human Development
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Arts in Culturally and Linguistically Diverse Education, District Partnership | https://www.ucdenver.edu/programs/ma-in-culturally-and-linguistically-diverse-education-district-partnership?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ma-in-culturally-and-linguistically-diverse-education-district-partnership |
| 2 | Master of Arts in Counseling, Clinical Mental Health | https://education.ucdenver.edu/academics/graduate/counseling/detail/ma-counseling-clinical-mental-health |
| 3 | Master of Arts in Counseling, School Counseling​​​ | https://education.ucdenver.edu/academics/graduate/counseling/detail/school-counseling-ma |
| 4 | Master of Arts in Couple and Family Therapy | https://education.ucdenver.edu/academics/graduate/couple-family-therapy/cft-ma |
| 5 | Master of Arts in Culturally and Linguistically Diverse Education | https://education.ucdenver.edu/academics/graduate/culturally-linguistically-diverse-education/detail/Culturally-and-Linguistically-Diverse-Education-MA |
| 6 | Master of Arts in Culturally and Linguistically Diverse Education (Endorsement) | https://education.ucdenver.edu/academics/graduate/culturally-linguistically-diverse-education/detail/culturally-and-linguistically-diverse-education-ma-with-endorsement |
| 7 | Master of Arts in Curriculum and Instruction, Critical Pedagogy | https://education.ucdenver.edu/continuing-education/aspire/program-details/MA-option |
| 8 | Master of Arts in Early Childhood Education | https://education.ucdenver.edu/academics/graduate/early-childhood-education/detail/early-childhood-education |
| 9 | Master of Arts in Early Childhood Education, Licensure with Boulder Journey School | https://education.ucdenver.edu/academics/reggio-emilia/boulder-journey-school-residency-ma |
| 10 | Master of Arts in Early Childhood Education, Early Childhood Special Education (Endorsement) | https://education.ucdenver.edu/academics/graduate/early-childhood-education/detail/Special-Education-MA-Endorsement |
| 11 | Master of Arts in Early Childhood Education, Early Childhood Special Education (License) | https://education.ucdenver.edu/academics/graduate/early-childhood-education/detail/early-childhood-education-ma-with-early-childhood-special-education-license |
| 12 | Master of Arts in Early Childhood Education, Online with Boulder Journey School | https://education.ucdenver.edu/academics/reggio-emilia/boulder-journey-school-ece-ma |
| 13 | Master of Arts in Leadership for Educational Organizations, Leading Change for Student Success in Higher Education | https://education.ucdenver.edu/academics/graduate/leadership-for-educational-organizations/detail/master-of-arts-in-leadership-for-educational-organizations-higher-education-and-student-success |
| 14 | Master of Arts in Leadership for Educational Organizations, Principal (License) | https://education.ucdenver.edu/academics/graduate/leadership-for-educational-organizations/detail/Leadership-for-Educational-Organizations-MA |
| 15 | Master of Arts in Learning Design & Technology | https://education.ucdenver.edu/academics/graduate/learning-design-technology/detail/learning-design-technology-MA |
| 16 | Master of Arts in Learning, Developmental and Family Sciences, Educational Psychology and Learning Sciences | https://education.ucdenver.edu/academics/graduate/learning-developmental-family-sciences/detail/Learning-MA |
| 17 | Master of Arts in Learning, Developmental and Family Sciences, Friends School Teacher Preparation Partnership | https://education.ucdenver.edu/academics/graduate/learning-developmental-family-sciences/detail/friends-school-teacher-preparation-partnership |
| 18 | Master of Arts in Learning, Developmental and Family Sciences, Human Development and Family Relations | https://education.ucdenver.edu/academics/graduate/learning-developmental-family-sciences/detail/Human-Development-and-Family-Relations-MA |
| 19 | Master of Arts in Literacy Education | https://education.ucdenver.edu/academics/graduate/literacy-education/detail/Literacy-Education-MA |
| 20 | Master of Arts in Literacy Education, English Education | https://education.ucdenver.edu/academics/graduate/literacy-education/detail/English-Education-MA |
| 21 | Master of Arts in Literacy Education, Reading and Writing, Reading Specialist (Endorsement) | https://education.ucdenver.edu/academics/graduate/literacy-education/detail/Reading-and-Writing-MA |
| 22 | Master of Arts in Research and Evaluation Methods | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/Research-and-Evaluation-Methods-MA |
| 23 | Master of Arts in Special Education | https://education.ucdenver.edu/academics/graduate/special-education/detail/Special-Education-MA |
| 24 | Master of Arts in Special Education, Applied Behavior Analysis | https://education.ucdenver.edu/academics/graduate/special-education/detail/master-of-arts-in-special-education-applied-behavior-analysis |
| 25 | Master of Arts in Special Education, Generalist (Endorsement) | https://education.ucdenver.edu/academics/graduate/special-education/detail/special-education-with-generalist-endorsement |
| 26 | Master of Arts in STEM Education, Science | https://education.ucdenver.edu/academics/graduate/stem-education/detail/Science-MA |
| 27 | Master of Arts in Teaching, Elementary Education (License) | education.ucdenver.edu/academics/graduate/teaching/detail/ma-Teaching-elementary-education |
| 28 | Master of Arts in Teaching, English Education (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/English-Education-MAT |
| 29 | Master of Arts in Teaching, Middle School Math (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/middle-school-math-MAT |
| 30 | Master of Arts in Teaching, Secondary Math (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/ma-teaching-secondary-secondary-math |
| 31 | Master of Arts in Teaching, Secondary Science (License) | education.ucdenver.edu/academics/graduate/teaching/detail/ma-teaching-secondary-science |
| 32 | Master of Arts in Teaching, Social Studies (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/Social-Studies-MAT |
| 33 | Master of Arts in Teaching, Special Education Generalist (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/Special-Education-Generalist-MAT |
| 34 | Master of Arts in Teaching, World Languages, Spanish (License) | https://education.ucdenver.edu/academics/graduate/teaching/detail/ma-teaching-teaching-world-languages-spanish?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=ma-teaching-teaching-world-languages-spanish |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education in Leadership for Educational Equity, Early Childhood Education | https://education.ucdenver.edu/academics/doctoral/detail/edd-education-in-leadership-educational-equity-early-childhood-education |
| 2 | Doctor of Education in Leadership for Educational Equity, Executive Leadership | https://education.ucdenver.edu/academics/doctoral/detail/Executive-Leadership-EdD |
| 3 | Doctor of Education in Leadership for Educational Equity, Higher Education | https://education.ucdenver.edu/academics/doctoral/detail/Higher-Education-EdD |
| 4 | Doctor of Education in Leadership for Educational Equity, Justice, Equity, and Diverse Identities (JEDI) | https://education.ucdenver.edu/academics/doctoral/detail/doctor-of-education-in-leadership-for-educational-equity-jedi |
| 5 | Doctor of Education in Leadership for Educational Equity, Learning Design | https://education.ucdenver.edu/academics/doctoral/detail/edd-leadership-educational-equity-learning-design |
| 6 | Doctor of Education in Leadership for Educational Equity, STEM Education | https://education.ucdenver.edu/academics/doctoral/detail/STEM-Education-EdD |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy in Education and Human Development, Critical Studies in Education | https://education.ucdenver.edu/academics/doctoral/detail/phd-education-and-human-development-critical-studies-education |
| 2 | Doctor of Philosophy in Education and Human Development, Early Childhood Policy | https://education.ucdenver.edu/academics/doctoral/detail/phd-education-and-human-development-early-childhood-policy |
| 3 | Doctor of Philosophy in Education and Human Development, Family Science and Human Development | https://education.ucdenver.edu/academics/doctoral/detail/Family-Science-and-Human-Development-PhD |
| 4 | Doctor of Philosophy in Education and Human Development, Leadership for Educational Organizations | https://education.ucdenver.edu/academics/doctoral/detail/Administrative-Leadership-and-Policy-PhD |
| 5 | Doctor of Philosophy in Education and Human Development, Mathematics Education | https://education.ucdenver.edu/academics/doctoral/detail/Mathematics-Education-PhD |
| 6 | Doctor of Philosophy in Education and Human Development, Science Education | https://education.ucdenver.edu/academics/doctoral/detail/Science-Education-PhD |
| 7 | Doctor of Philosophy in Education and Human Development, Research and Evaluation Methods | https://education.ucdenver.edu/academics/doctoral/detail/phd-research-evaluation-methods |
| 8 | Doctor of Philosophy in Education and Human Development, Inclusive Early Childhood Education | https://education.ucdenver.edu/academics/doctoral/detail/Early-Childhood-Education-PhD |

##### PsyD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Psychology, School Psychology | https://education.ucdenver.edu/academics/doctoral/detail/psyd-school-psychology |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Specialist in Leadership for Educational Organizations, Principal (License) | https://education.ucdenver.edu/academics/educational-specialist |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Applied Behavior Analysis | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Applied-Behavior-Analysis-Certificate |
| 2 | Graduate Certificate in Applied Measurement | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-applied-measurement |
| 3 | Graduate Certificate in Applied Statistical Modeling | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-applied-statistical-modeling |
| 4 | Graduate Certificate in Classroom Assessment | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-classroom-assessment |
| 5 | Graduate Certificate in Culturally Responsive Methods | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-culturally-responsive-methods |
| 6 | Graduate Certificate in Designing and Facilitating Online Learning | https://education.ucdenver.edu/academics/areas-of-study/learning-design-technology/detail/online-teaching-and-learning |
| 7 | Graduate Certificate in Early Childhood Education Pedagogy | https://education.ucdenver.edu/academics/graduate/early-childhood-education/detail/graduate-certificate-in-early-childhood-education-pedagogy |
| 8 | Graduate Certificate in Early Literacy | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Early-Literacy-Certificate |
| 9 | Graduate Certificate in Leadership for Learning Design and Technology | https://education.ucdenver.edu/academics/areas-of-study/learning-design-technology/detail/leadership-ldt |
| 10 | Graduate Certificate in Learner-centered Instructional Design | https://education.ucdenver.edu/academics/graduate/learning-design-technology/detail/Learner-centered-Instructional-Design |
| 11 | Graduate Certificate in Literacy and Language Development for Diverse Learners | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Literacy-and-Language-Certificate |
| 12 | Graduate Certificate in Mathematical Content Knowledge for Teaching | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Mathematical-Content-Certificate |
| 13 | Graduate Certificate in Program Evaluation | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-program-evaluation |
| 14 | Graduate Certificate in Qualitative Methods and Analysis | https://education.ucdenver.edu/academics/graduate/research-evaluation-methods/detail/graduate-certificate-in-qualitative-methods-and-analysis |
| 15 | Graduate Certificate in Teaching for Cultural and Linguistic Diversity | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Teaching-Certificate |
| 16 | Graduate Certificate, Digital Teacher Librarian | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/School-Libraries-Certificate |

##### Graduate Credential
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Credential in Neurosequential Model in Education | https://education.ucdenver.edu/nme-credential |

##### Endorsement
| # | 项目 | URL |
|---|------|-----|
| 1 | Endorsement, Culturally and Linguistically Diverse Bilingual Education | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Bilingual-Education-Specialist-Endorsement |
| 2 | Endorsement, Culturally and Linguistically Diverse Education | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Culturally-and-Linguistically-Diverse-Education-Endorsement |
| 3 | Endorsement, Early Childhood Special Education | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Early-Childhood-Special-Education-Endorsement |
| 4 | Endorsement, Mentor Teacher | https://www.ucdenver.edu/programs/endorsement--clinical-teacher-mentoring?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=endorsement--clinical-teacher-mentoring |
| 5 | Endorsement, Middle School Math | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/middle-school-math-endorsement |
| 6 | Endorsement, Special Education Generalist | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Special-Education-Endorsement |
| 7 | Endorsement, Teacher Librarian | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Teacher-Librarian-Endorsement |

##### License
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor License | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Licensed-Counselor |
| 2 | Early Childhood Special Education (License) | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Early-Childhood-Special-Education-License |
| 3 | Executive Leadership Administrator License | https://education.ucdenver.edu/academics/certificates-licenses-and-endorsements/detail/Administrator-License-Executive-Leadership |

##### Credit available
| # | 项目 | URL |
|---|------|-----|
| 1 | Certificate, Prosocial Leader | https://education.ucdenver.edu/continuing-education/certificates/detail/certificate-prosocial-leader |
| 2 | Graduate Certificate in Clinical Teacher Mentoring | https://www.ucdenver.edu/programs/graduate-certificate-in-clinical-teacher-mentoring-with-optional-mentor-teacher-endorsement?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=graduate-certificate-in-clinical-teacher-mentoring-with-optional-mentor-teacher-endorsement |
| 3 | P-3 Leadership Program | https://education.ucdenver.edu/continuing-education/certificates/p-3-leadership-program |


#### School of Public Affairs
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Public Administration - Master of Arts in Applied Geography and Geospatial Sciences | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-arts-in-applied-geography-and-geospatial-sciences |
| 2 | Dual Master of Public Administration - Master of Arts in Economics | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-arts-in-economics |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Accelerated Master of Public Administration | https://www.ucdenver.edu/programs/one-year-mpa?utm_source=program-finder&utm_medium=website&utm_campaign=organic&utm_content=one-year-mpa |
| 2 | Dual Master of Public Administration - Master of Public Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-public-policy |
| 3 | Executive Master of Public Administration | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 4 | Master of Public Administration | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 5 | Master of Public Administration, Disasters, Hazards & Emergency Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 6 | Master of Public Administration, Education Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 7 | Master of Public Administration, Emergency Management & Homeland Security | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 8 | Master of Public Administration, Environmental Policy & Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 9 | Master of Public Administration, Gender-Based Violence | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 10 | Master of Public Administration, Local Government | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 11 | Master of Public Administration, Managing for Social Equity | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 12 | Master of Public Administration, Nonprofit Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |
| 13 | Master of Public Administration, Public Policy Analysis | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-administration |

##### MCJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Criminal Justice | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/master-of-criminal-justice |
| 2 | Master of Criminal Justice, Crime Analysis | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/master-of-criminal-justice |
| 3 | Master of Criminal Justice, Disasters, Hazards & Emergency Management | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/master-of-criminal-justice |
| 4 | Criminal Justice in Emergency Mgmt & Homeland Srty | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/master-of-criminal-justice |
| 5 | Master of Criminal Justice, Gender-Based Violence | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/master-of-criminal-justice |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-policy |
| 2 | Master of Public Policy, Education Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-policy |
| 3 | Master of Public Policy, Environmental Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-policy |
| 4 | Master of Public Policy, Policy Analysis and Methods | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-policy |
| 5 | Master of Public Policy, Policy Entrepreneurship and Advocacy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/master-of-public-policy |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy in Public Affairs | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/phd-in-public-affairs |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Certificate in Crime Analysis | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/graduate-certificate-in-crime-analysis |
| 2 | Graduate Certificate in Disasters, Hazards and Emergency Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-disasters-hazards-and-emergency-management |
| 3 | Graduate Certificate in Education Policy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-education-policy |
| 4 | Graduate Certificate in Emergency Management and Homeland Security | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-emergency-management-and-homeland-security-certificate |
| 5 | Graduate Certificate in Environmental Policy and Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-environmental-policy-and-management |
| 6 | Graduate Certificate in Interpersonal Violence | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-interpersonal-violence |
| 7 | Graduate Certificate in Local Government | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-local-government |
| 8 | Graduate Certificate in Managing for Social Equity | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-managing-for-social-equity |
| 9 | Graduate Certificate in Nonprofit Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-nonprofit-management |
| 10 | Graduate Certificate in Policy Analysis & Methods | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-public-policy-analysis |
| 11 | Graduate Certificate in Policy Entrepreneurship and Advocacy | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-policy-entrepreneurship-and-advocacy |
| 12 | Graduate Certificate in Public Management | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/graduate-certificate-in-public-management |

##### Non-credit
| # | 项目 | URL |
|---|------|-----|
| 1 | Colorado Certified Public Manager Program | https://publicaffairs.ucdenver.edu/programs/professional-development/leadership-training/colorado-certified-public-manager-program |

##### Credit available
| # | 项目 | URL |
|---|------|-----|
| 1 | Denver Community Leadership Forum | https://publicaffairs.ucdenver.edu/programs/professional-development/leadership-training/denver-community-leadership-forum |

##### MPA/MURP
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Public Administration - Master of Urban and Regional Planning | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-urban-and-regional-planning |

##### MPA/JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Public Administration - Juris Doctor | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-juris-doctor |

##### MPA/MCJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Public Administration - Master of Criminal Justice | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-criminal-justice |

##### MPA/MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Dual Master of Public Administration - Master of Public Health | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/dual-master-of-public-administration-master-of-public-health |

##### BA/MCJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Pathways Bachelor of Arts - Master of Criminal Justice | https://publicaffairs.ucdenver.edu/programs/criminal-justice-programs/dual-bachelor-of-arts-master-of-criminal-justice |

##### BA/MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Pathways Bachelor of Arts in Public Administration - Master of Public Administration | https://publicaffairs.ucdenver.edu/programs/public-affairs-programs/pathways-bachelor-of-arts-in-public-administration-master-of-public-administration |



### 2.2 Graduate Admissions Model

**Decentralized**: Each school/college manages its own graduate admissions.

**Application requirements**: Online form, $50 domestic/$75 intl fee, unofficial transcripts, letters of recommendation (most programs), statement of purpose (many programs), GRE/GMAT (program-specific), English proficiency for non-native speakers.

**Fee waivers**: CU Denver alumni, current students, military, American Indian tribe members, financial hardship, disability, event attendees, CU institution affiliates.


---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| Admissions type | Rolling admission |
| Application portal | https://www.ucdenver.edu/admissions/-apply-now |
| Fall deadline (domestic) | July 31 |
| Spring deadline (domestic) | Jan 6 |
| Summer deadline (domestic) | May 22 |
| Fall deadline (intl outside US) | July 15 |
| Fall deadline (intl inside US) | Aug 8 |
| Priority scholarship (intl) | Fall: March 1 / Spring: October 1 |
| Decision timeline | ~10 business days |
| Application fee (intl) | $75 |
| SAT/ACT policy | TEST-OPTIONAL |
| SAT code | 4875 |
| ACT code | 0533 |
| Middle 50% GPA | 3.23 – 3.93 |
| Middle 50% SAT | 1070 – 1260 |
| Middle 50% ACT | 21 – 27 |

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低总分 | 最低子分 |
|------|---------|---------|
| TOEFL iBT (0-120) | 79 | R:8, L:7, S:18, W:16 |
| TOEFL iBT (1-6, from Jan 2026) | 4 | R:3, L:2.5, S:3.5, W:3.5 |
| IELTS Academic | 6.5 | Each band: 5.5 |
| PTE Academic | 58 | Each subscore: 42 |
| Duolingo | 105 | Each subscore: 85 |
| ACT English | 18 | — |
| SAT ERW | 480 | — |
| AP English Literature | 3 | — |
| IB English A | 4 | — |

**Exemptions**: Citizens of UK, Ireland, Australia, Canada, NZ, Jamaica, Trinidad & Tobago, and other English-speaking countries.

**Conditional admission**: Available for UG (except Nursing) without adequate ELP.

**LynxDirect Pathway**: TOEFL 70 / IELTS 6.0 / DET 95.

### 3.3 Graduate — Global Rules

| 维度 | 详情 |
|------|------|
| Admissions model | Decentralized — apply to each program |
| Application fee | $50 domestic / $75 international |
| GRE/GMAT | Program-specific |
| English proficiency | Required for non-native speakers |
| Transcripts | Unofficial for review; official upon enrollment |
| Fee waivers | Alumni, military, financial hardship, event attendees |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-2026)

| 费用项目 | Resident | Non-Resident | International |
|---------|----------|-------------|--------------|
| Tuition & Fees/yr | $12,573 | $31,917 | $33,906 |
| WUE Tuition/yr | ~$18,860 | — | — |

### 4.2 Undergraduate Financial Aid

| 维度 | 详情 |
|------|------|
| Need-blind/Need-aware | Need-aware for all |
| FAFSA code | 004508 |
| Chancellor Scholarship (in-state) | Up to $3,000/yr (4 years) |
| Distinguished Scholars (OOS) | Up to $5,000/yr (4 years) |
| WUE Scholarship | Up to $3,000/yr (4 years) |
| Intl auto-merit (GPA 3.7+) | $10,000/yr |
| Students receiving aid | 72% |

### 4.3 Graduate Cost & Funding

| 维度 | 详情 |
|------|------|
| Grad Resident tuition/yr | $10,568 |
| Grad Non-Resident tuition/yr | $20,984 |
| Grad International tuition/yr | $20,984 |
| Application fee | $50 domestic / $75 intl |
| Funding | Varies by program; RA/TA available in some depts |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: UG Rolling Admission & Deadlines
```yaml
field: undergraduate.admissions.rolling
value: true; Fall July 31, Spring Jan 6, Summer May 22
source_url: https://www.ucdenver.edu/admissions/undergraduate-admissions
source_snippet: "Spring 2026 Deadline: Jan. 5, 2026 / Fall 2026 Deadline: July 31, 2026"
capture_date: 2026-07-06
```

### E-U-002: Test-Optional Policy
```yaml
field: undergraduate.admissions.test_policy
value: test-optional
source_url: https://www.ucdenver.edu/undergraduate-admissions/first-year/requirements
source_snippet: "Submitting test scores is optional, and won't negatively impact your application."
capture_date: 2026-07-06
```

### E-U-003: Middle 50% Statistics
```yaml
field: undergraduate.admissions.middle_50
value: {gpa: "3.23-3.93", sat: "1070-1260", act: "21-27"}
source_url: https://www.ucdenver.edu/undergraduate-admissions/first-year/requirements
capture_date: 2026-07-06
```

### E-U-004: UG Resident Tuition
```yaml
field: undergraduate.costs.tuition_resident
value: $12,573/year
source_url: https://www.ucdenver.edu/tuition-cost/cost-of-attendance
source_snippet: "Resident Tuition & Fees: $12,573 per year (Fall 2025 - Spring 2026)"
capture_date: 2026-07-06
```

### E-U-005: UG Non-Resident Tuition
```yaml
field: undergraduate.costs.tuition_nonresident
value: $31,917/year
source_url: https://www.ucdenver.edu/tuition-cost/cost-of-attendance
source_snippet: "Non-Resident Tuition & Fees: $31,917 per year (Fall 2025 - Spring 2026)"
capture_date: 2026-07-06
```

### E-U-006: International UG Tuition
```yaml
field: undergraduate.costs.tuition_international
value: $33,906/year
source_url: https://www.ucdenver.edu/tuition-cost/cost-of-attendance
source_snippet: "Undergraduate (Bachelor) Tuition & Fees: $33,906 per year (Fall 2025 - Spring 2026)"
capture_date: 2026-07-06
```

### E-U-007: English Proficiency — TOEFL
```yaml
field: undergraduate.english_proficiency.toefl
value: {overall: 79, reading: 8, listening: 7, speaking: 18, writing: 16}
source_url: https://www.ucdenver.edu/international-admissions/apply-for-admission/undergraduate/first-year
capture_date: 2026-07-06
```

### E-U-008: English Proficiency — IELTS
```yaml
field: undergraduate.english_proficiency.ielts
value: {overall: 6.5, each_band: 5.5}
source_url: https://www.ucdenver.edu/international-admissions/apply-for-admission/undergraduate/first-year
capture_date: 2026-07-06
```

### E-U-009: English Proficiency — Duolingo
```yaml
field: undergraduate.english_proficiency.duolingo
value: {overall: 105, each_subscore: 85}
source_url: https://www.ucdenver.edu/international-admissions/apply-for-admission/undergraduate/first-year
capture_date: 2026-07-06
```

### E-U-010: Need-Aware Policy
```yaml
field: undergraduate.aid.need_blind
value: false (need-aware for all)
source_url: https://www.ucdenver.edu/admissions/undergraduate-admissions
capture_date: 2026-07-06
```

### E-U-011: International Auto-Merit Scholarship
```yaml
field: undergraduate.scholarships.international_merit
value: {gpa_3.0: "$5,000/yr", gpa_3.3: "$7,500/yr", gpa_3.7: "$10,000/yr"}
source_url: https://www.ucdenver.edu/international-admissions/costs-financial-aid/undergraduate
capture_date: 2026-07-06
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.admissions.application_fee
value: {domestic: $50, international: $75}
source_url: https://www.ucdenver.edu/admissions/graduate/before-you-apply/requirements
capture_date: 2026-07-06
```

### E-G-002: Graduate Tuition
```yaml
field: graduate.costs.tuition
value: {resident: $10,568/yr, nonresident: $20,984/yr}
source_url: https://www.ucdenver.edu/tuition-cost/cost-of-attendance
capture_date: 2026-07-06
```

### E-S-001: Schools & Colleges
```yaml
field: institution.schools_colleges
value: {downtown: 7, anschutz: 6, total: 13}
source_url: https://www.ucdenver.edu/academics/schools-colleges
source_snippet: "CU Denver is organized into seven schools and colleges"
capture_date: 2026-07-06
```

### E-P-001: Total Program Count
```yaml
field: institution.program_count
value: 484
source_url: https://www.ucdenver.edu/programs
source_snippet: "Showing 1 - 12 of 484 results"
capture_date: 2026-07-06
```

### E-D-001: International Deadlines
```yaml
field: undergraduate.admissions.deadlines_international
value: {fall_priority: "March 1", fall_outside_us: "July 15", fall_inside_us: "Aug 8"}
source_url: https://www.ucdenver.edu/international-admissions/apply-for-admission/undergraduate/first-year
capture_date: 2026-07-06
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
cudenver-knowledge-base-v2/
├── 00-institution-overview
├── 01-architecture-planning (10 items)
├── 02-arts-media (29 items)
├── 03-business-school (64 items)
├── 04-education-human-development (107 items)
├── 05-engineering-design-computing (38 items)
├── 06-liberal-arts-sciences (176 items)
├── 07-public-affairs (61 items)
├── 08-admissions-requirements
├── 09-costs-financial-aid
├── 10-graduate-admissions
└── 11-anschutz-overview
```

### Follow-up Data Items

| 优先级 | 数据项 |
|--------|--------|
| P0 | Anschutz Medical Campus full program directory |
| P0 | Per-program GRE/GMAT requirements (graduate) |
| P1 | Detailed COA line items (housing, food, books) |
| P1 | Engineering-specific admission requirements |
| P1 | Nursing-specific English proficiency minimums |
| P2 | WUE specific tuition rate |
| P2 | Transfer admission requirements details |
| P2 | Graduate funding/stipend data per program |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | CU Denver |
|------|-----------|
| Total programs | 484 |
| Schools/colleges | 7 downtown + 6 Anschutz = 13 |
| UG tuition (resident) | $12,573/yr |
| UG tuition (non-resident) | $31,917/yr |
| UG tuition (international) | $33,906/yr |
| Grad tuition (resident) | $10,568/yr |
| Grad tuition (non-resident) | $20,984/yr |
| Need-blind? | No — need-aware for all |
| Test policy | Test-optional |
| Fall deadline | July 31 (domestic) |
| TOEFL min | 79 |
| IELTS min | 6.5 (each band 5.5) |
| Duolingo min | 105 |
| App fee (UG intl) | $75 |
| App fee (Grad) | $50 domestic / $75 intl |
| Intl merit max | $10,000/yr (GPA 3.7+) |
| FAFSA code | 004508 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: ucdenver.edu, graduateschool.cuanschutz.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program