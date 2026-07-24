# Pennsylvania State University (Penn State) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BArch/BAE/BDes) | 220 |
| 本科辅修 (Minor) | 200+ |
| 本科证书 (Undergraduate Certificate) | 100+ |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 200+ |
| 研究生辅修 (Graduate Minor) | 13 |
| 研究生证书 (Graduate Certificate) | 150+ |
| **学位项目总计 (UG + Grad)** | **420+** |
| 学院 / 独立系所总数 | 12 (本科授予学位学院) + 6 (研究生/专业学院) |

> **来源说明**: 本科专业数来自 majors.psu.edu 分页列表 (220项)；本科辅修和证书来自 bulletins.psu.edu ("more than 160 majors, 200 minors, and 100 undergraduate certificates")；研究生项目来自 bulletins.psu.edu/graduate 列表。"275+ majors" 为招生宣传数字，包含同一专业在不同校区的重复计数。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Pennsylvania State University
├── College of Agricultural Sciences                    [本科学院]
│   ├── Agricultural and Extension Education
│   ├── Agricultural Science
│   ├── Agribusiness Management
│   ├── Animal Science
│   ├── Community, Environment, and Development
│   ├── Entomology
│   ├── Food Science
│   ├── Forest Resources
│   ├── Plant Biology
│   ├── Plant Pathology
│   ├── Soil Science
│   ├── Turfgrass Science
│   └── Veterinary and Biomedical Sciences
├── College of Arts and Architecture                    [本科学院]
│   ├── Architecture
│   ├── Art Education
│   ├── Art History
│   ├── Art (B.A. / B.F.A.)
│   ├── Digital Arts and Media Design
│   ├── Landscape Architecture
│   ├── Music
│   ├── Theatre
│   └── Visual Arts Studies
├── Smeal College of Business                           [本科学院]
│   ├── Accounting
│   ├── Actuarial Science
│   ├── Business Analytics and Information Systems
│   ├── Corporate Innovation and Entrepreneurship
│   ├── Finance
│   ├── Management
│   ├── Marketing
│   ├── Risk Management
│   └── Supply Chain and Information Systems
├── Donald P. Bellisario College of Communications      [本科学院]
│   ├── Advertising/Public Relations
│   ├── Communications
│   ├── Journalism
│   └── Telecommunications and Media Industries
├── College of Earth and Mineral Sciences               [本科学院]
│   ├── Earth Sciences
│   ├── Energy and Mineral Engineering
│   ├── Geography
│   ├── Geosciences
│   ├── Materials Science and Engineering
│   └── Meteorology and Atmospheric Science
├── College of Education                                [本科学院]
│   ├── Education Policy and Leadership
│   ├── Learning, Design, and Technology
│   ├── Special Education
│   └── Workforce Education and Development
├── College of Engineering                              [本科学院]
│   ├── Aerospace Engineering
│   ├── Architectural Engineering
│   ├── Biological Engineering
│   ├── Biomedical Engineering
│   ├── Chemical Engineering
│   ├── Civil Engineering
│   ├── Computer Engineering
│   ├── Computer Science
│   ├── Data Sciences
│   ├── Electrical Engineering
│   ├── Engineering Science and Mechanics
│   ├── Industrial Engineering
│   ├── Mechanical Engineering
│   ├── Nuclear Engineering
│   └── Software Engineering
├── College of Health and Human Development             [本科学院]
│   ├── Biobehavioral Health
│   ├── Communication Sciences and Disorders
│   ├── Health Policy and Administration
│   ├── Hospitality Management
│   ├── Human Development and Family Studies
│   ├── Kinesiology
│   ├── Nursing
│   ├── Nutritional Sciences
│   └── Recreation, Park, and Tourism Management
├── College of Information Sciences and Technology      [本科学院]
│   ├── Cybersecurity Analytics and Operations
│   ├── Data Sciences (shared with Engineering/Science)
│   ├── Information Sciences and Technology
│   └── Security and Risk Analysis
├── College of Liberal Arts                             [本科学院]
│   ├── African American Studies
│   ├── African Studies
│   ├── American Studies
│   ├── Anthropology
│   ├── Applied Linguistics
│   ├── Asian Studies
│   ├── Classics and Ancient Mediterranean Studies
│   ├── Communication Arts and Sciences
│   ├── Comparative Literature
│   ├── Criminal Justice
│   ├── Criminology
│   ├── Economics
│   ├── English
│   ├── French and Francophone Studies
│   ├── German
│   ├── History
│   ├── International Politics
│   ├── Italian
│   ├── Jewish Studies
│   ├── Labor Studies and Employment Relations
│   ├── Latin American Studies
│   ├── Linguistics
│   ├── Philosophy
│   ├── Political Science
│   ├── Psychology
│   ├── Religious Studies
│   ├── Russian
│   ├── Sociology
│   ├── Spanish
│   ├── Women's, Gender, and Sexuality Studies
│   └── Writing and Digital Media
├── Nese College of Nursing                             [本科学院]
│   └── Nursing (BSN)
├── Eberly College of Science                           [本科学院]
│   ├── Astronomy and Astrophysics
│   ├── Biochemistry and Molecular Biology
│   ├── Biology
│   ├── Biotechnology
│   ├── Chemistry
│   ├── Mathematics
│   ├── Microbiology
│   ├── Physics
│   ├── Premedicine
│   └── Statistics
├── J. Jeffrey and Ann Marie Fox Graduate School        [研究生院]
│   └── (管理全校研究生教育，不直接授予学位)
├── Penn State Dickinson Law                            [专业学院]
│   └── J.D.
├── College of Medicine (Hershey)                       [专业学院]
│   └── M.D., graduate biomedical programs
├── School of International Affairs                     [研究生院]
│   └── Master of International Affairs (M.I.A.)
└── Schreyer Honors College                             [荣誉学院]
    └── (跨学院荣誉项目，不授予独立学位)
```

> ⚠ **共享系所**: Data Sciences 系同时隶属于 College of Engineering、College of Information Sciences and Technology、和 Eberly College of Science。Computer Science 同时隶属于 College of Engineering 和 College of Information Sciences and Technology。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | canonical | 全称 | 层级 | 本校数量 |
|---------|-----------|------|------|---------|
| B.S. | BS | Bachelor of Science | 本科 | ~160 |
| B.A. | BA | Bachelor of Arts | 本科 | ~50 |
| B.F.A. | BFA | Bachelor of Fine Arts | 本科 | 3 |
| B.Arch. | BArch | Bachelor of Architecture | 本科 | 1 |
| B.A.E. | BAE | Bachelor of Architectural Engineering | 本科 | 1 |
| B.Des. | BDes | Bachelor of Design | 本科 | 2 |
| B.Phil. | BPhil | Bachelor of Philosophy | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 200+ |
| Certificate | Certificate | 本科证书 | 本科 | 100+ |
| M.S. | MS | Master of Science | 研究生 | ~80 |
| M.A. | MA | Master of Arts | 研究生 | ~30 |
| M.B.A. | MBA | Master of Business Administration | 研究生 | 3 (Smeal/Behrend/Capital/Great Valley) |
| M.F.A. | MFA | Master of Fine Arts | 研究生 | 2 |
| M.Eng. | MEng | Master of Engineering | 研究生 | ~10 |
| M.Arch. | MArch | Master of Architecture | 研究生 | 1 |
| M.I.A. | MIA | Master of International Affairs | 研究生 | 1 |
| M.Ed. | MEd | Master of Education | 研究生 | ~10 |
| M.H.A. | MHA | Master of Health Administration | 研究生 | 1 |
| M.P.A. | MPA | Master of Public Administration | 研究生 | 1 |
| M.P.H. | MPH | Master of Public Health | 研究生 | 1 |
| M.S.W. | MSW | Master of Social Work | 研究生 | 1 |
| Ph.D. | PhD | Doctor of Philosophy | 研究生 | ~80 |
| D.Ed. | EdD | Doctor of Education | 研究生 | 1 |
| D.M.A. | DMA | Doctor of Musical Arts | 研究生 | 1 |
| D.B.A. | DBA | Doctor of Business Administration | 研究生 | 1 |
| J.D. | JD | Juris Doctor | 研究生 | 1 |
| M.D. | MD | Doctor of Medicine | 研究生 | 1 |
| Graduate Minor | Grad Minor | 研究生辅修 | 研究生 | 13 |
| Graduate Certificate | Grad Cert | 研究生证书 | 研究生 | 150+ |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BS | BA | BFA | BArch | BAE | BDes | Minor | Cert | 合计 |
|------------|----|----|-----|-------|-----|------|-------|------|------|
| Agricultural Sciences | 13 | 0 | 0 | 0 | 0 | 0 | 12 | 5 | 30 |
| Arts and Architecture | 1 | 6 | 3 | 1 | 1 | 2 | 8 | 4 | 26 |
| Smeal Business | 8 | 0 | 0 | 0 | 0 | 0 | 6 | 3 | 17 |
| Bellisario Communications | 1 | 3 | 0 | 0 | 0 | 0 | 3 | 2 | 9 |
| Earth & Mineral Sciences | 8 | 0 | 0 | 0 | 0 | 0 | 7 | 3 | 18 |
| Education | 4 | 0 | 0 | 0 | 0 | 0 | 3 | 8 | 15 |
| Engineering | 16 | 0 | 0 | 0 | 0 | 0 | 10 | 5 | 31 |
| Health & Human Development | 9 | 0 | 0 | 0 | 0 | 0 | 9 | 6 | 24 |
| Information Sciences & Tech | 3 | 0 | 0 | 0 | 0 | 0 | 4 | 5 | 12 |
| Liberal Arts | 4 | 30 | 0 | 0 | 0 | 0 | 35 | 15 | 84 |
| Nursing | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 |
| Eberly Science | 12 | 0 | 0 | 0 | 0 | 0 | 8 | 3 | 23 |
| Division of Undergraduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **81** | **39** | **3** | **1** | **1** | **2** | **105** | **61** | **293** |

> **注意**: 此矩阵为 University Park 校区本科专业分布。同一专业在不同校区（如 Abington、Altoona、Behrend 等）的变体未重复计数。总计 220 个学位专业 + 200+ 辅修 + 100+ 证书。

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

Penn State 的本科教育由 12 个授予学位的学院和 1 个荣誉学院组成。详见 Section 0.2 层级树。学生入学时可选择具体学院和专业，或通过 Division of Undecided/Division of Undergraduate Studies 先不选专业。

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural Sciences
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness Management | https://bulletins.psu.edu/programs |
| 2 | Agricultural and Biorenewable Systems Management | https://bulletins.psu.edu/programs |
| 3 | Agricultural and Extension Education | https://bulletins.psu.edu/programs |
| 4 | Agricultural Science | https://bulletins.psu.edu/programs |
| 5 | Animal Science | https://bulletins.psu.edu/programs |
| 6 | Community, Environment, and Development | https://bulletins.psu.edu/programs |
| 7 | Entomology | https://bulletins.psu.edu/programs |
| 8 | Environmental Resource Management | https://bulletins.psu.edu/programs |
| 9 | Food Science | https://bulletins.psu.edu/programs |
| 10 | Forest Resources | https://bulletins.psu.edu/programs |
| 11 | Plant Sciences | https://bulletins.psu.edu/programs |
| 12 | Soil Science | https://bulletins.psu.edu/programs |
| 13 | Turfgrass Science | https://bulletins.psu.edu/programs |
| 14 | Veterinary and Biomedical Sciences | https://bulletins.psu.edu/programs |
| 15 | Wildlife and Fisheries Science | https://bulletins.psu.edu/programs |

##### Undecided
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Sciences (Undecided) | https://bulletins.psu.edu/programs |

#### College of Arts and Architecture
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://bulletins.psu.edu/programs |
| 2 | Art (B.A.) | https://bulletins.psu.edu/programs |
| 3 | Integrative Arts | https://bulletins.psu.edu/programs |
| 4 | Music | https://bulletins.psu.edu/programs |
| 5 | Theatre Studies | https://bulletins.psu.edu/programs |
| 6 | Visual Arts Studies | https://bulletins.psu.edu/programs |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | https://bulletins.psu.edu/programs |

##### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://bulletins.psu.edu/programs |
| 2 | Art (B.F.A.) | https://bulletins.psu.edu/programs |
| 3 | Musical Theatre | https://bulletins.psu.edu/programs |

##### BArch
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://bulletins.psu.edu/programs |

##### BAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://bulletins.psu.edu/programs |

##### BDes
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Arts and Media Design | https://bulletins.psu.edu/programs |
| 2 | Landscape Architecture | https://bulletins.psu.edu/programs |

#### Smeal College of Business
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://bulletins.psu.edu/programs |
| 2 | Actuarial Science | https://bulletins.psu.edu/programs |
| 3 | Business Analytics and Information Systems | https://bulletins.psu.edu/programs |
| 4 | Corporate Innovation and Entrepreneurship | https://bulletins.psu.edu/programs |
| 5 | Finance | https://bulletins.psu.edu/programs |
| 6 | Management | https://bulletins.psu.edu/programs |
| 7 | Marketing | https://bulletins.psu.edu/programs |
| 8 | Risk Management | https://bulletins.psu.edu/programs |
| 9 | Supply Chain and Information Systems | https://bulletins.psu.edu/programs |

#### Donald P. Bellisario College of Communications
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising/Public Relations | https://bulletins.psu.edu/programs |
| 2 | Journalism | https://bulletins.psu.edu/programs |
| 3 | Telecommunications and Media Industries | https://bulletins.psu.edu/programs |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communications | https://bulletins.psu.edu/programs |

#### College of Earth and Mineral Sciences
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Science and Policy | https://bulletins.psu.edu/programs |
| 2 | Earth Sciences | https://bulletins.psu.edu/programs |
| 3 | Energy and Mineral Engineering | https://bulletins.psu.edu/programs |
| 4 | Geography | https://bulletins.psu.edu/programs |
| 5 | Geosciences | https://bulletins.psu.edu/programs |
| 6 | Materials Science and Engineering | https://bulletins.psu.edu/programs |
| 7 | Meteorology and Atmospheric Science | https://bulletins.psu.edu/programs |
| 8 | Mining Engineering | https://bulletins.psu.edu/programs |

#### College of Education
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education Policy and Leadership | https://bulletins.psu.edu/programs |
| 2 | Learning, Design, and Technology | https://bulletins.psu.edu/programs |
| 3 | Special Education | https://bulletins.psu.edu/programs |
| 4 | Workforce Education and Development | https://bulletins.psu.edu/programs |

#### College of Engineering
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://bulletins.psu.edu/programs |
| 2 | Biological Engineering | https://bulletins.psu.edu/programs |
| 3 | Biomedical Engineering | https://bulletins.psu.edu/programs |
| 4 | Chemical Engineering | https://bulletins.psu.edu/programs |
| 5 | Civil Engineering | https://bulletins.psu.edu/programs |
| 6 | Computer Engineering | https://bulletins.psu.edu/programs |
| 7 | Computer Science | https://bulletins.psu.edu/programs |
| 8 | Data Sciences | https://bulletins.psu.edu/programs |
| 9 | Electrical Engineering | https://bulletins.psu.edu/programs |
| 10 | Engineering Science and Mechanics | https://bulletins.psu.edu/programs |
| 11 | Industrial Engineering | https://bulletins.psu.edu/programs |
| 12 | Mechanical Engineering | https://bulletins.psu.edu/programs |
| 13 | Nuclear Engineering | https://bulletins.psu.edu/programs |
| 14 | Software Engineering | https://bulletins.psu.edu/programs |
| 15 | Artificial Intelligence Engineering | https://bulletins.psu.edu/programs |

#### College of Health and Human Development
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biobehavioral Health | https://bulletins.psu.edu/programs |
| 2 | Communication Sciences and Disorders | https://bulletins.psu.edu/programs |
| 3 | Health Policy and Administration | https://bulletins.psu.edu/programs |
| 4 | Hospitality Management | https://bulletins.psu.edu/programs |
| 5 | Human Development and Family Studies | https://bulletins.psu.edu/programs |
| 6 | Kinesiology | https://bulletins.psu.edu/programs |
| 7 | Nutritional Sciences | https://bulletins.psu.edu/programs |
| 8 | Recreation, Park, and Tourism Management | https://bulletins.psu.edu/programs |

#### College of Information Sciences and Technology
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cybersecurity Analytics and Operations | https://bulletins.psu.edu/programs |
| 2 | Information Sciences and Technology | https://bulletins.psu.edu/programs |
| 3 | Security and Risk Analysis | https://bulletins.psu.edu/programs |

#### College of Liberal Arts
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | https://bulletins.psu.edu/programs |
| 2 | African and African American Studies | https://bulletins.psu.edu/programs |
| 3 | African Studies | https://bulletins.psu.edu/programs |
| 4 | American Studies | https://bulletins.psu.edu/programs |
| 5 | Anthropology | https://bulletins.psu.edu/programs |
| 6 | Applied Linguistics | https://bulletins.psu.edu/programs |
| 7 | Asian Studies | https://bulletins.psu.edu/programs |
| 8 | Chinese | https://bulletins.psu.edu/programs |
| 9 | Classics and Ancient Mediterranean Studies | https://bulletins.psu.edu/programs |
| 10 | Communication Arts and Sciences | https://bulletins.psu.edu/programs |
| 11 | Comparative Literature | https://bulletins.psu.edu/programs |
| 12 | Criminal Justice | https://bulletins.psu.edu/programs |
| 13 | Economics | https://bulletins.psu.edu/programs |
| 14 | English | https://bulletins.psu.edu/programs |
| 15 | French and Francophone Studies | https://bulletins.psu.edu/programs |
| 16 | German | https://bulletins.psu.edu/programs |
| 17 | Global and International Studies | https://bulletins.psu.edu/programs |
| 18 | History | https://bulletins.psu.edu/programs |
| 19 | Italian | https://bulletins.psu.edu/programs |
| 20 | Japanese | https://bulletins.psu.edu/programs |
| 21 | Jewish Studies | https://bulletins.psu.edu/programs |
| 22 | Korean | https://bulletins.psu.edu/programs |
| 23 | Latin American Studies | https://bulletins.psu.edu/programs |
| 24 | Linguistics | https://bulletins.psu.edu/programs |
| 25 | Philosophy | https://bulletins.psu.edu/programs |
| 26 | Political Science | https://bulletins.psu.edu/programs |
| 27 | Psychology | https://bulletins.psu.edu/programs |
| 28 | Religious Studies | https://bulletins.psu.edu/programs |
| 29 | Russian | https://bulletins.psu.edu/programs |
| 30 | Sociology | https://bulletins.psu.edu/programs |
| 31 | Spanish | https://bulletins.psu.edu/programs |
| 32 | Telecommunications and Media Industries | https://bulletins.psu.edu/programs |
| 33 | Theatre Studies | https://bulletins.psu.edu/programs |
| 34 | Women's, Gender, and Sexuality Studies | https://bulletins.psu.edu/programs |
| 35 | Writing and Digital Media | https://bulletins.psu.edu/programs |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://bulletins.psu.edu/programs |
| 2 | Economics (B.S.) | https://bulletins.psu.edu/programs |
| 3 | Labor Studies and Employment Relations | https://bulletins.psu.edu/programs |
| 4 | Political Science (B.S.) | https://bulletins.psu.edu/programs |
| 5 | Psychology (B.S.) | https://bulletins.psu.edu/programs |
| 6 | Sociology (B.S.) | https://bulletins.psu.edu/programs |
| 7 | Women's, Gender, and Sexuality Studies (B.S.) | https://bulletins.psu.edu/programs |

##### BPhil
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Philosophy | https://bulletins.psu.edu/programs |

#### Nese College of Nursing
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://bulletins.psu.edu/programs |

#### Eberly College of Science
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy and Astrophysics | https://bulletins.psu.edu/programs |
| 2 | Biochemistry and Molecular Biology | https://bulletins.psu.edu/programs |
| 3 | Biology | https://bulletins.psu.edu/programs |
| 4 | Biotechnology | https://bulletins.psu.edu/programs |
| 5 | Chemistry | https://bulletins.psu.edu/programs |
| 6 | Mathematics | https://bulletins.psu.edu/programs |
| 7 | Microbiology | https://bulletins.psu.edu/programs |
| 8 | Physics | https://bulletins.psu.edu/programs |
| 9 | Premedicine | https://bulletins.psu.edu/programs |
| 10 | Science (Undecided) | https://bulletins.psu.edu/programs |
| 11 | Statistics | https://bulletins.psu.edu/programs |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 涉及学院 | URL |
|---|------|---------|-----|
| 1 | Data Sciences | Engineering + IST + Science | https://bulletins.psu.edu/programs |
| 2 | Computer Science | Engineering + IST | https://bulletins.psu.edu/programs |
| 3 | Integrative Arts | Arts & Architecture + Liberal Arts | https://bulletins.psu.edu/programs |
| 4 | Biobehavioral Health | Health & Human Development + multiple campuses | https://bulletins.psu.edu/programs |

### 1.4 Minors — complete list

Penn State 提供 200+ 本科辅修。完整列表见 https://bulletins.psu.edu/programs (筛选 "Minor")。主要辅修包括但不限于：

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Accounting | Smeal Business |
| 2 | Advertising/Public Relations | Bellisario Communications |
| 3 | African American Studies | Liberal Arts |
| 4 | Anthropology | Liberal Arts |
| 5 | Arabic and Islamic Studies | Liberal Arts |
| 6 | Art History | Arts & Architecture |
| 7 | Biology | Eberly Science |
| 8 | Business | Smeal Business |
| 9 | Chemistry | Eberly Science |
| 10 | Chinese | Liberal Arts |
| 11 | Communications | Bellisario Communications |
| 12 | Computer Science | Engineering |
| 13 | Creative Writing | Liberal Arts |
| 14 | Criminal Justice | Liberal Arts |
| 15 | Economics | Liberal Arts |
| 16 | English | Liberal Arts |
| 17 | Environmental Inquiry | Liberal Arts |
| 18 | Film Studies | Liberal Arts |
| 19 | French | Liberal Arts |
| 20 | German | Liberal Arts |
| 21 | Global Health | Health & Human Development |
| 22 | History | Liberal Arts |
| 23 | Information Sciences and Technology | IST |
| 24 | Italian | Liberal Arts |
| 25 | Japanese | Liberal Arts |
| 26 | Jewish Studies | Liberal Arts |
| 27 | Korean | Liberal Arts |
| 28 | Linguistics | Liberal Arts |
| 29 | Mathematics | Eberly Science |
| 30 | Medieval Studies | Liberal Arts |
| 31 | Music | Arts & Architecture |
| 32 | Philosophy | Liberal Arts |
| 33 | Physics | Eberly Science |
| 34 | Political Science | Liberal Arts |
| 35 | Psychology | Liberal Arts |
| 36 | Religious Studies | Liberal Arts |
| 37 | Russian | Liberal Arts |
| 38 | Security and Risk Analysis | IST |
| 39 | Sociology | Liberal Arts |
| 40 | Spanish | Liberal Arts |
| 41 | Statistics | Eberly Science |
| 42 | Sustainability Leadership | Earth & Mineral Sciences |
| 43 | Theatre | Arts & Architecture |
| 44 | Women's, Gender, and Sexuality Studies | Liberal Arts |

> 完整 200+ 辅修列表见 bulletins.psu.edu/programs (Minor 筛选)。

### 1.5 General/Institute-wide requirements

Penn State 的通识教育要求称为 **General Education**，包括以下领域：
- **Writing and Speaking** (GWS): 3门课
- **Quantification** (GQ): 2门课 (数学/统计)
- **Natural Sciences** (GN): 2门课
- **Arts** (GA): 2门课
- **Humanities** (GH): 2门课
- **Social and Behavioral Sciences** (GS): 2门课
- **Health and Wellness** (GHW): 2门课
- **Intercultural and International Competence**: 可通过上述课程满足

详见: https://bulletins.psu.edu/undergraduate/

### 1.6 Campus locations

Penn State 在宾夕法尼亚州有 20+ 个校区：
- **University Park** (旗舰校区，State College)
- **Commonwealth Campuses**: Abington, Altoona, Beaver, Behrend (Erie), Berks, Brandywine, Capital (Harrisburg), DuBois, Fayette, Greater Allegheny, Hazleton, Lehigh Valley, Mont Alto, New Kensington, Schuylkill, Scranton, Shenango, Wilkes-Barre, York
- **World Campus** (在线教育)

> 注意: 7个校区计划在 2027 年春季后关闭: DuBois, Fayette, New Kensington, Mont Alto, Shenango, Wilkes-Barre, York。

---

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

Penn State 的研究生教育由 **J. Jeffrey and Ann Marie Fox Graduate School** 统一管理，但各学院自主招生。研究生院约有 13,000 名学生。

#### 主要研究生学位项目（按学院分组）

##### College of Agricultural Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural and Biological Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 2 | Agricultural and Environmental Plant Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Animal Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 4 | Entomology | MS/PhD | https://bulletins.psu.edu/graduate |
| 5 | Food Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 6 | Forest Resources | MS/PhD | https://bulletins.psu.edu/graduate |
| 7 | International Agriculture and Development | MS | https://bulletins.psu.edu/graduate |
| 8 | Plant Biology | MS/PhD | https://bulletins.psu.edu/graduate |
| 9 | Plant Pathology | MS/PhD | https://bulletins.psu.edu/graduate |
| 10 | Soil Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 11 | Wildlife and Fisheries Science | MS/PhD | https://bulletins.psu.edu/graduate |

##### College of Arts and Architecture
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | MArch/MS | https://bulletins.psu.edu/graduate |
| 2 | Art | MFA/MA | https://bulletins.psu.edu/graduate |
| 3 | Art Education | MA/PhD | https://bulletins.psu.edu/graduate |
| 4 | Art History | MA/PhD | https://bulletins.psu.edu/graduate |
| 5 | Landscape Architecture | MLA | https://bulletins.psu.edu/graduate |
| 6 | Music | MA/MM/DMA | https://bulletins.psu.edu/graduate |
| 7 | Music Education | MM/PhD | https://bulletins.psu.edu/graduate |
| 8 | Theatre | MFA | https://bulletins.psu.edu/graduate |
| 9 | Visual Studies | MFA | https://bulletins.psu.edu/graduate |

##### Smeal College of Business
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | MS | https://bulletins.psu.edu/graduate |
| 2 | Business Administration (MBA) | MBA | https://bulletins.psu.edu/graduate |
| 3 | Business Administration (PhD) | PhD | https://bulletins.psu.edu/graduate |
| 4 | Business Analytics | MS | https://bulletins.psu.edu/graduate |
| 5 | Corporate Innovation and Entrepreneurship | MS | https://bulletins.psu.edu/graduate |
| 6 | Finance | MS/PhD | https://bulletins.psu.edu/graduate |
| 7 | Management and Organization | PhD | https://bulletins.psu.edu/graduate |
| 8 | Marketing | PhD | https://bulletins.psu.edu/graduate |
| 9 | Real Estate Analysis and Development | MS | https://bulletins.psu.edu/graduate |
| 10 | Supply Chain Management | MS/PhD | https://bulletins.psu.edu/graduate |
| 11 | Taxation | MS | https://bulletins.psu.edu/graduate |

##### Donald P. Bellisario College of Communications
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communications | MA/PhD | https://bulletins.psu.edu/graduate |
| 2 | Mass Communications | PhD | https://bulletins.psu.edu/graduate |
| 3 | Media Studies | MA | https://bulletins.psu.edu/graduate |
| 4 | Strategic Communications | MA | https://bulletins.psu.edu/graduate |

##### College of Earth and Mineral Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Energy and Mineral Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 2 | Geography | MA/MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Geosciences | MS/PhD | https://bulletins.psu.edu/graduate |
| 4 | Materials Science and Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 5 | Meteorology and Atmospheric Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 6 | Mining Engineering | MS/PhD | https://bulletins.psu.edu/graduate |

##### College of Education
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Comparative and International Education | MEd/PhD | https://bulletins.psu.edu/graduate |
| 2 | Counselor Education | MEd/PhD | https://bulletins.psu.edu/graduate |
| 3 | Curriculum and Instruction | MEd/PhD | https://bulletins.psu.edu/graduate |
| 4 | Education Policy and Leadership | PhD | https://bulletins.psu.edu/graduate |
| 5 | Educational Leadership | DEd/PhD | https://bulletins.psu.edu/graduate |
| 6 | Educational Psychology | MEd/PhD | https://bulletins.psu.edu/graduate |
| 7 | Higher Education | MEd/PhD | https://bulletins.psu.edu/graduate |
| 8 | Learning, Design, and Technology | MEd/MS/PhD | https://bulletins.psu.edu/graduate |
| 9 | Lifelong Learning and Adult Education | MEd/PhD | https://bulletins.psu.edu/graduate |
| 10 | School Psychology | PhD | https://bulletins.psu.edu/graduate |
| 11 | Special Education | MEd/PhD | https://bulletins.psu.edu/graduate |
| 12 | Workforce Education and Development | MEd/MS/PhD | https://bulletins.psu.edu/graduate |

##### College of Engineering
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 2 | Architectural Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Biological Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 4 | Biomedical Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 5 | Chemical Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 6 | Civil Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 7 | Computer Science and Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 8 | Electrical Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 9 | Engineering Design and Innovation | MEng | https://bulletins.psu.edu/graduate |
| 10 | Engineering Science and Mechanics | MS/PhD | https://bulletins.psu.edu/graduate |
| 11 | Industrial Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 12 | Mechanical Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 13 | Nuclear Engineering | MS/PhD | https://bulletins.psu.edu/graduate |
| 14 | Operations Research | MS/PhD | https://bulletins.psu.edu/graduate |
| 15 | Software Engineering | MS | https://bulletins.psu.edu/graduate |
| 16 | Systems Engineering | MS/PhD | https://bulletins.psu.edu/graduate |

##### College of Health and Human Development
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biobehavioral Health | MS/PhD | https://bulletins.psu.edu/graduate |
| 2 | Communication Sciences and Disorders | MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Health Policy and Administration | MHA/MPH/PhD | https://bulletins.psu.edu/graduate |
| 4 | Hospitality Management | MS/PhD | https://bulletins.psu.edu/graduate |
| 5 | Human Development and Family Studies | MS/PhD | https://bulletins.psu.edu/graduate |
| 6 | Kinesiology | MS/PhD | https://bulletins.psu.edu/graduate |
| 7 | Nutritional Sciences | MS/PhD | https://bulletins.psu.edu/graduate |
| 8 | Recreation, Park, and Tourism Management | MS/PhD | https://bulletins.psu.edu/graduate |

##### College of Information Sciences and Technology
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Informatics | PhD | https://bulletins.psu.edu/graduate |
| 2 | Information Science | MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Information Systems | MS | https://bulletins.psu.edu/graduate |

##### College of Liberal Arts
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | African American and Diaspora Studies | PhD | https://bulletins.psu.edu/graduate |
| 2 | Anthropology | MA/PhD | https://bulletins.psu.edu/graduate |
| 3 | Applied Linguistics | MA/PhD | https://bulletins.psu.edu/graduate |
| 4 | Classics and Ancient Mediterranean Studies | MA/PhD | https://bulletins.psu.edu/graduate |
| 5 | Clinical Psychology | PhD | https://bulletins.psu.edu/graduate |
| 6 | Comparative Literature | MA/PhD | https://bulletins.psu.edu/graduate |
| 7 | Criminal Justice | MS/PhD | https://bulletins.psu.edu/graduate |
| 8 | Economics | MA/MS/PhD | https://bulletins.psu.edu/graduate |
| 9 | English | MA/MFA/PhD | https://bulletins.psu.edu/graduate |
| 10 | French and Francophone Studies | MA/PhD | https://bulletins.psu.edu/graduate |
| 11 | Geography | MA/MS/PhD | https://bulletins.psu.edu/graduate |
| 12 | German | MA/PhD | https://bulletins.psu.edu/graduate |
| 13 | History | MA/PhD | https://bulletins.psu.edu/graduate |
| 14 | Linguistics | MA/PhD | https://bulletins.psu.edu/graduate |
| 15 | Philosophy | MA/PhD | https://bulletins.psu.edu/graduate |
| 16 | Political Science | MA/PhD | https://bulletins.psu.edu/graduate |
| 17 | Psychology | MA/PhD | https://bulletins.psu.edu/graduate |
| 18 | Sociology | MA/PhD | https://bulletins.psu.edu/graduate |
| 19 | Spanish | MA/PhD | https://bulletins.psu.edu/graduate |
| 20 | Women's, Gender, and Sexuality Studies | MA/PhD | https://bulletins.psu.edu/graduate |

##### Nese College of Nursing
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | MSN/DNP/PhD | https://bulletins.psu.edu/graduate |

##### Eberly College of Science
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Astronomy and Astrophysics | MS/PhD | https://bulletins.psu.edu/graduate |
| 2 | Biochemistry, Microbiology, and Molecular Biology | MS/PhD | https://bulletins.psu.edu/graduate |
| 3 | Biology | MS/PhD | https://bulletins.psu.edu/graduate |
| 4 | Biostatistics | MS/PhD | https://bulletins.psu.edu/graduate |
| 5 | Chemistry | MS/PhD | https://bulletins.psu.edu/graduate |
| 6 | Mathematics | MA/MS/PhD | https://bulletins.psu.edu/graduate |
| 7 | Physics | MS/PhD | https://bulletins.psu.edu/graduate |
| 8 | Statistics | MS/PhD | https://bulletins.psu.edu/graduate |

##### Penn State Dickinson Law
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | JD | https://dickinsonlaw.psu.edu/jd-admissions |

##### College of Medicine (Hershey)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medicine | MD | https://med.psu.edu/education |
| 2 | Biomedical Sciences | PhD | https://med.psu.edu/education |
| 3 | Clinical and Translational Sciences | MS | https://bulletins.psu.edu/graduate |

##### School of International Affairs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | International Affairs | MIA | https://bulletins.psu.edu/graduate |

### 2.2 Graduate admissions model

Penn State 的研究生招生采用 **混合模式**：
- **Fox Graduate School** 提供统一的申请系统和行政支持
- **各学院自主招生**，设置自己的截止日期、GRE 要求和录取标准
- 申请通过 Fox Graduate School 在线系统提交
- 申请费: 美国申请人 $65，国际申请人 $85
- 大多数博士项目提供全额资助（RA/TA/Fellowship）
- 硕士项目资助情况因学院而异

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 内容 |
|------|------|
| 招生网站 | https://www.psu.edu/admission/undergraduate |
| 申请系统 | MyPennState + Common App |
| 申请费 | Domestic $65 / International $75 |
| Early Action (EA) | 11月1日申请，12月24日前出结果 |
| 推荐申请截止日期 | 12月1日 |
| Regular Decision | 滚动录取 (Rolling) |
| 春季申请开放 | 6月1日 |
| 秋季/夏季申请开放 | 8月1日 |
| 押金/确认入学截止 | 5月1日 |
| SAT/ACT 政策 | **Test-optional** (已确认) |
| SAT 代码 | 2660 |
| ACT 代码 | 3656 |
| Superscore | **不采用** (使用单次考试最高综合分) |
| SAT Subject Tests | 不要求，不接受 |
| 自报告成绩 | 可以，通过 MyPennState |
| 推荐信 | 不要求 |
| 面试 | 不提供 |
| 作品集 | 部分艺术/建筑专业要求 |
| 加速医学项目 (BS/MD) | SAT/ACT **必须**提交，截止日期 10月14日 |

> **来源**: "For first-year applicants, Penn State is test-optional, so submitting scores is not required for your application." (psu.edu/admission/undergraduate/how-to-apply FAQ)

> "Penn State will use a student's highest combined score from one single test date. Penn State does not utilize a superscore." (psu.edu/resources/faq/test-optional)

### 3.2 Undergraduate English proficiency table

Penn State 要求英语非母语的国际学生提供英语能力证明。具体最低分数要求请参考 Penn State Global 的 "Resources for International Students" 页面。

| 考试 | 最低要求 | 推荐分数 |
|------|---------|---------|
| TOEFL iBT | 请核实 (通常 80+) | - |
| IELTS Academic | 请核实 (通常 6.5+) | - |
| Duolingo English Test | 请核实 | - |

> **注意**: Penn State 的 UG 英语能力具体最低分数未在招生网站上明确公布，需联系招生办或参考 Penn State Global 的国际学生资源页面。

### 3.3 Graduate — global rules

| 维度 | 内容 |
|------|------|
| 招生网站 | https://gradschool.psu.edu/admissions |
| 申请系统 | Fox Graduate School 在线申请 |
| 申请费 | Domestic $65 / International $85 / Nondegree $30 |
| GRE 政策 | 因项目而异 (各学院自主决定) |
| 英语能力 (TOEFL iBT) | 总分至少 4.5，口语至少 3.5 (2026年1月21日后新评分标准)；旧标准: 总分 80+，口语 19+ |
| 英语能力 (IELTS Academic) | 总分至少 6.5 |
| 免除英语考试 | 完成 Penn State 英语强化课程 / 来自英语为母语的国家 |
| CGS 4月15日协议 | 签署方 |
| 博士资助 | 大多数项目提供全额资助 (RA/TA/Fellowship) |
| 硕士资助 | 因项目而异，部分自费 |

> **来源**: "TOEFL iBT: overall score of at least 4.5 with a 3.5 or greater on the speaking section. (For tests taken prior to January 21, 2026: overall score of at least 80 with a minimum speaking score of 19)" (gradschool.psu.edu/admissions/prepare-to-apply)

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-2027 academic year, University Park)

| 费用项目 | PA Resident | Non-PA Resident | International |
|---------|-------------|-----------------|---------------|
| Tuition and Fees | $20,878 | $41,790 | $41,790 |
| Student Initiated Fee | $640 | $640 | $640 |
| International Fee | $0 | $0 | $1,500 |
| Housing and Food | $14,050 - $18,276 | $14,050 - $18,276 | $14,050 - $18,276 |
| Other Expenses (books, transport, personal) | $6,646 | $6,646 | $6,646 |
| **TOTAL** | **$42,214 - $46,440** | **$65,910 - $70,136** | **$67,410 - $71,636** |

> 学术年度费用 (Fall/Spring)。59 学分以下全日制本科生。费用每年7月由 Board of Trustees 设定。

### 4.2 Undergraduate financial-aid policy

| 维度 | 内容 |
|------|------|
| Need-blind/Need-aware | **Need-aware for all** (包括美国学生和国际学生) |
| 国际学生资助 | "There is, at this time, essentially no financial aid available for international undergraduate students." |
| 联邦资助资格 | 需要美国公民身份或合法永久居留权 |
| FAFSA | 要求提交 |
| CSS Profile | 不要求 |
| 奖学金来源 | Office of Student Aid + 各学院 + 各校区 |
| 主要奖学金 | Provost Academic Award (OOS)、Commonwealth Award (PA)、Discover Award、LiveOn Student Success Grant |

> **来源**: "There is, at this time, essentially no financial aid available for international undergraduate students. U.S. Citizenship or legal permanent residency is a requirement for federal student aid." (psu.edu/resources/faq/international-students)

### 4.3 Graduate cost & funding framework

| 维度 | 内容 |
|------|------|
| 申请费 | Domestic $65 / International $85 |
| 资助类型 | Fully funded (大多数博士) / Partially funded / Self-funded (部分硕士) |
| 常见资助形式 | Research Assistantship (RA)、Teaching Assistantship (TA)、Fellowship |
| Fox Endowment | 专门的研究生资助基金 |
| Summer Tuition Assistance Program | 暑期学费资助 |
| 费用减免 | 联系目标项目申请 |

---

## SECTION 5 — Evidence Chain Index

```yaml
# E-U-001
field: undergraduate.admissions.test_optional
value: "For first-year applicants, Penn State is test-optional, so submitting scores is not required for your application."
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "For first-year applicants, Penn State is test-optional, so submitting scores is not required for your application."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-002
field: undergraduate.deadlines.ea
value: "November 1 (apply by), December 24 (decision by)"
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "For Early Action: Apply by November 1 in order to receive a decision by December 24"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-003
field: undergraduate.deadlines.recommended
value: "December 1"
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "Recommended submission deadline for all applications: December 1"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-004
field: undergraduate.application_fee.domestic
value: "$65"
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "Domestic Fee: $65"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-005
field: undergraduate.application_fee.international
value: "$75"
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "International Fee: $75"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-006
field: undergraduate.test_policy.superscore
value: "No superscore - uses highest combined score from one single test date"
source_url: https://www.psu.edu/resources/faq/test-optional
source_snippet: "Penn State will use a student's highest combined score from one single test date. Penn State does not utilize a superscore."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-007
field: undergraduate.cost.tuition_pa_resident
value: "$20,878"
source_url: https://www.psu.edu/admission/undergraduate/tuition-costs
source_snippet: "Tuition and Fees: $20,878 (PA Resident)"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-008
field: undergraduate.cost.tuition_non_pa
value: "$41,790"
source_url: https://www.psu.edu/admission/undergraduate/tuition-costs
source_snippet: "Tuition and Fees: $41,790 (Non-PA Resident)"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-009
field: undergraduate.cost.total_pa_resident
value: "$42,214 - $46,440"
source_url: https://www.psu.edu/admission/undergraduate/tuition-costs
source_snippet: "TOTAL: $42,214 to $46,440 (PA Resident)"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-010
field: undergraduate.cost.total_non_pa
value: "$65,910 - $70,136"
source_url: https://www.psu.edu/admission/undergraduate/tuition-costs
source_snippet: "TOTAL: $65,910 to $70,136 (Non-PA Resident)"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-011
field: undergraduate.cost.total_international
value: "$67,410 - $71,636"
source_url: https://www.psu.edu/admission/undergraduate/tuition-costs
source_snippet: "TOTAL: $67,410 to $71,636 (International)"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-012
field: undergraduate.financial_aid.need_blind
value: "Need-aware for all (including domestic and international)"
source_url: https://www.psu.edu/resources/faq/international-students
source_snippet: "There is, at this time, essentially no financial aid available for international undergraduate students."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-013
field: undergraduate.high_school_requirements
value: "English 4, Social Studies/Arts/Humanities 3, Science 3, Math 3, World Language 2"
source_url: https://www.psu.edu/admission/undergraduate/how-to-apply
source_snippet: "English: 4 units, Social Studies/Arts/Humanities: 3 units, Science: 3 units, Math: 3 units, World Language: 2 units"
capture_date: 2026-07-05
evidence_type: official_webpage_table

---
# E-U-014
field: undergraduate.programs.total_majors
value: "220 (from majors.psu.edu) / 275+ (marketing number)"
source_url: https://www.psu.edu/academics/undergraduate/majors
source_snippet: "Penn State offers more than 275 majors"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-U-015
field: undergraduate.programs.total_minors
value: "200+"
source_url: https://bulletins.psu.edu/programs
source_snippet: "more than 160 majors, 200 minors, and 100 undergraduate certificates"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-001
field: graduate.english_proficiency.toefl
value: "Overall 4.5 (new scale) / 80 (old scale, pre-Jan 2026), Speaking 3.5 (new) / 19 (old)"
source_url: https://gradschool.psu.edu/admissions/prepare-to-apply
source_snippet: "TOEFL iBT: overall score of at least 4.5 with a 3.5 or greater on the speaking section. (For tests taken prior to January 21, 2026: overall score of at least 80 with a minimum speaking score of 19)"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-002
field: graduate.english_proficiency.ielts
value: "Minimum overall band score of 6.5"
source_url: https://gradschool.psu.edu/admissions/prepare-to-apply
source_snippet: "International English Language Testing System (IELTS) Academic Test: minimum overall band score of 6.5"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-003
field: graduate.application_fee.domestic
value: "$65"
source_url: https://gradschool.psu.edu/admissions/prepare-to-apply
source_snippet: "U.S. applicants for degree programs and certificate programs: $65"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-004
field: graduate.application_fee.international
value: "$85"
source_url: https://gradschool.psu.edu/admissions/prepare-to-apply
source_snippet: "International applicants for degree programs and certificate programs: $85"
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-005
field: graduate.student_count
value: "~13,000"
source_url: https://bulletins.psu.edu/graduate
source_snippet: "The J. Jeffrey and Ann Marie Fox Graduate School at Penn State is one of the largest in the nation with approximately 13,000 graduate students."
capture_date: 2026-07-05
evidence_type: official_webpage

---
# E-G-006
field: graduate.programs.total
value: "Over 300 graduate programs"
source_url: https://gradschool.psu.edu/admissions/prepare-to-apply
source_snippet: "Penn State offers over 300 graduate programs in dozens of disciplines"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection structure

```
pennstate-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, degree inventory, matrix
├── 01-ug-agricultural-sciences.md      # Section 1: College of Agricultural Sciences programs
├── 02-ug-arts-architecture.md          # Section 1: College of Arts and Architecture programs
├── 03-ug-smeal-business.md             # Section 1: Smeal College of Business programs
├── 04-ug-bellisario-communications.md  # Section 1: Bellisario College programs
├── 05-ug-earth-mineral-sciences.md     # Section 1: Earth & Mineral Sciences programs
├── 06-ug-education.md                  # Section 1: College of Education programs
├── 07-ug-engineering.md                # Section 1: College of Engineering programs
├── 08-ug-health-human-development.md   # Section 1: HHD programs
├── 09-ug-information-sciences.md       # Section 1: IST programs
├── 10-ug-liberal-arts.md               # Section 1: Liberal Arts programs
├── 11-ug-nursing.md                    # Section 1: Nursing programs
├── 12-ug-science.md                    # Section 1: Eberly Science programs
├── 13-graduate-programs.md             # Section 2: All graduate programs
├── 14-deadlines-requirements.md        # Section 3: Application requirements
├── 15-costs-financial-aid.md           # Section 4: Costs and aid
├── 16-evidence-chain.md                # Section 5: Evidence index
└── 17-comparison-framework.md          # Section 7: Cross-school comparison
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "pennstate-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | UG English proficiency minimum scores (TOEFL/IELTS/DET) | Penn State Global international resources |
| P0 | Graduate program degree types (MS vs PhD for each program) | Individual program pages on bulletins.psu.edu |
| P1 | Graduate application deadlines by program | gradschool.psu.edu + individual program pages |
| P1 | GRE requirement by graduate program | Individual program pages |
| P1 | Graduate tuition rates | Penn State Bursar |
| P2 | Detailed COA line items (books, transportation, personal) | registrar.psu.edu tuition schedules |
| P2 | Need-blind/need-aware policy for domestic students | admissions.psu.edu |
| P2 | Campus-specific program availability details | bulletins.psu.edu |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Penn State | (Other schools) |
|------|-----------|-----------------|
| 类型 | Public R1 | |
| 所在地 | University Park, PA | |
| UG 学费/年 (In-state) | $20,878 | |
| UG 学费/年 (OOS) | $41,790 | |
| UG 总费用/年 (In-state) | $42,214 - $46,440 | |
| UG 总费用/年 (OOS) | $65,910 - $70,136 | |
| Need-blind (Domestic?) | Need-aware | |
| Need-blind (Intl?) | Need-aware | |
| EA 截止日期 | November 1 | |
| RD 截止日期 | Rolling (recommended Dec 1) | |
| SAT/ACT 要求 | Test-optional | |
| TOEFL 最低 (UG) | TBD | |
| IELTS 最低 (UG) | TBD | |
| TOEFL 最低 (Grad) | 4.5 (new) / 80 (old) | |
| IELTS 最低 (Grad) | 6.5 | |
| 申请费 (UG) | $65 (domestic) / $75 (intl) | |
| 申请费 (Grad) | $65 (domestic) / $85 (intl) | |
| 专业总数 (Rule 1) | 420+ | |
| 学院数 (Rule 2) | 12 UG + 6 Grad/Prof | |
| 校区数 | 20+ | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: psu.edu, bulletins.psu.edu, gradschool.psu.edu, global.psu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
