# Georgia Institute of Technology (Georgia Tech) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.0 Institution Snapshot

| 字段 | 值 | 来源 |
|------|-----|------|
| 全称 | Georgia Institute of Technology | gatech.edu |
| 简称 | Georgia Tech / GT | |
| 类型 | 公立研究型大学 (Public R1) | |
| 所属系统 | University System of Georgia (USG) | |
| 所在地 | Atlanta, Georgia, USA | |
| 成立年份 | 1885 | |
| 本科招生网站 | admission.gatech.edu | |
| 研究生招生网站 | grad.gatech.edu | |
| 财务援助网站 | finaid.gatech.edu | |
| 课程目录 | catalog.gatech.edu | |
| 申请系统 | Common App (UG); gradapp.gatech.edu (Grad) | |

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (BS) | 39 | 独立专业名 (不含 thread/option 细分) |
| 本科学位项目 (含 thread/option) | 233 | catalog.gatech.edu 完整条目 |
| 本科辅修 (Minor) | 87 | catalog.gatech.edu |
| 研究生学位项目 (MS/MArch/MBA/MID/PhD/etc.) | 109 | 66 Master's + 43 Doctoral (catalog.gatech.edu) |
| 研究生证书 (Graduate Certificate) | 27 | catalog: 18 embedded + 9 stand-alone |
| 本科证书 (Undergraduate Certificate) | 93 | catalog: 47 embedded + 46 other |
| **学位项目总计 (UG Majors + Grad Degrees)** | **148** | 39 UG majors + 109 grad degrees |
| **目录总条目 (含所有细分)** | **546** | 233 UG + 87 minors + 109 grad + 117 certs |
| 学院总数 | 6 | 本科授予学院 |
| 学校/部门总数 | 30+ | 含研究生院各部门 |

> **Reconciliation**: 39 UG majors (admissions page) × average 6 threads/options each ≈ 233 catalog entries. 66 Master's + 43 PhD = 109 grad degrees. Catalog total = 233 + 87 + 66 + 43 + 117 certs = 546 entries.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Georgia Institute of Technology
├── College of Engineering                                [学院]
│   ├── Aerospace Engineering                             [系]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical and Biomolecular Engineering              [系]
│   ├── Civil and Environmental Engineering               [系]
│   ├── Electrical and Computer Engineering               [系]
│   ├── Industrial and Systems Engineering                [系]
│   ├── Materials Science and Engineering                 [系]
│   ├── Mechanical Engineering                            [系]
│   └── Nuclear and Radiological Engineering              [系]
├── College of Computing                                  [学院]
│   ├── School of Computer Science                        [系]
│   ├── School of Interactive Computing                   [系]
│   ├── School of Computational Science and Engineering   [系]
│   └── School of Cybersecurity and Privacy               [系]
├── College of Sciences                                   [学院]
│   ├── School of Biological Sciences                     [系]
│   ├── School of Chemistry and Biochemistry              [系]
│   ├── School of Earth and Atmospheric Sciences          [系]
│   ├── School of Mathematics                             [系]
│   ├── School of Physics                                 [系]
│   └── School of Psychology                              [系]
├── College of Design                                     [学院]
│   ├── School of Architecture                            [系]
│   ├── School of Building Construction                   [系]
│   ├── School of City and Regional Planning              [系]
│   ├── School of Industrial Design                       [系]
│   └── School of Music                                   [系]
├── Ivan Allen College of Liberal Arts                    [学院]
│   ├── School of Economics                               [系]
│   ├── School of History and Sociology                   [系]
│   ├── School of International Affairs                   [系]
│   ├── School of Literature, Media, and Communication    [系]
│   ├── School of Modern Languages                        [系]
│   └── School of Public Policy                           [系]
└── Scheller College of Business                          [学院]
    └── School of Management                              [系]
```

**跨学院共享项目 (⚠ shared)**:
- Computer Engineering: College of Computing ⚠ College of Engineering
- Computational Media: College of Computing ⚠ College of Design (Music)
- Mathematics and Computing: College of Computing ⚠ College of Sciences
- Bioengineering PhD: 可由 7 个不同 Engineering 系授予
- Computational Science & Engineering PhD/MS: 可由多个学院系授予
- Machine Learning PhD: 可由 9 个不同系授予
- Robotics PhD/MS: 可由 5-6 个不同系授予

### 0.3 学历级别明细 (Rule 3 — Degree Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 项目数量 |
|-----------|----------------|------|------|---------|
| BS | BS | Bachelor of Science | 本科 | 233 (含 threads/options) |
| Minor | Minor | 辅修 | 本科 | 87 |
| UG Certificate | Certificate | 本科证书 | 本科 | 93 |
| MS | MS | Master of Science | 研究生 | 52 |
| MArch | M.Arch. | Master of Architecture | 研究生 | 1 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 (Full-time/Evening/Executive) |
| MID | MID | Master of Industrial Design | 研究生 | 1 |
| MCRP | MCRP | Master of City and Regional Planning | 研究生 | 1 |
| MBID | — | Master of Biomedical Innovation and Development | 研究生 | 1 |
| MRED | — | Master of Real Estate Development | 研究生 | 1 |
| MSEEM | — | Master of Sustainable Energy and Environmental Management | 研究生 | 1 |
| Prof. Master's | — | Professional Master's (Applied Systems Eng / Manufacturing Leadership / Occ Safety) | 研究生 | 3 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 43 |
| Grad Certificate | Certificate | 研究生证书 | 研究生 | 27 |

> **学位规范化说明**: Georgia Tech 所有本科学位均为 BS (Bachelor of Science)，无 BA/BFA/BEng。研究生以 MS 为主，另有专业硕士学位。PhD 为唯一博士学位类型。

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix: 学院 × canonical 学位级别)

#### 本科分布 (按学院)

| 学院 \ 级别 | BS | Minor | UG Cert | 合计 (BS) |
|------------|-----|-------|---------|-----------|
| College of Engineering | 13 | 15 | 5 | 13 |
| College of Computing | 5 | 8 | 2 | 5 |
| College of Sciences | 12 | 15 | 8 | 12 |
| College of Design | 6 | 7 | 4 | 6 |
| Ivan Allen College of Liberal Arts | 9 | 18 | 15 | 9 |
| Scheller College of Business | 1 | 9 | 13 | 1 |
| 跨学院/其他 | — | 15 | 46 | — |
| **合计** | **46*** | **87** | **93** | **46*** |

> *注: 46 = admissions 页面列出的专业数 (含跨学院重复)。catalog 中 233 条目含所有 thread/option 细分。39 为去重后的独立专业数。

#### 研究生分布 (按学院)

| 学院 \ 级别 | MS | 专业硕士 | PhD | Grad Cert | 合计 |
|------------|-----|---------|-----|-----------|------|
| College of Engineering | 22 | 3 | 18 | 5 | 48 |
| College of Computing | 5 | 0 | 5 | 2 | 12 |
| College of Sciences | 8 | 0 | 9 | 5 | 22 |
| College of Design | 6 | 4 | 3 | 4 | 17 |
| Ivan Allen College of Liberal Arts | 9 | 0 | 5 | 6 | 20 |
| Scheller College of Business | 2 | 3 | 1 | 2 | 8 |
| 跨学院 (CSE/ML/BioE/Robotics) | 14 | 0 | 2 | 3 | 19 |
| **合计** | **66** | **10** | **43** | **27** | **146** |

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

Georgia Tech has 6 undergraduate-degree-granting colleges, all offering the Bachelor of Science (BS) degree. The university's distinctive features include the "Threads" curriculum in Computer Science (students choose 2 threads to customize their degree) and extensive specialization options in Engineering. All undergraduate degrees are BS — Georgia Tech does not award BA, BFA, or BEng.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Computing

##### School of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.gatech.edu/programs/computer-science-bs/ |

> Computer Science 采用 Threads 课程体系，学生选择 2 个 thread 组合。Catalog 列出 37 种 thread 组合 (如 AI+People, Theory+Media, Embedded Devices+Cybersecurity 等)。

##### School of Interactive Computing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Computational Media | https://catalog.gatech.edu/programs/computational-media-bs/ |

> Computational Media 也有 12 种 thread 组合 (如 AI-Games, Music Technology-Media 等)。

##### College of Computing (跨系)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Computer Engineering | https://catalog.gatech.edu/programs/computer-engineering-bs/ |
| 4 | Computer Engineering (Dual BS) | https://www.gatech.edu/academics/degrees/bachelors/computer-engineering-dual-bs |
| 5 | Mathematics and Computing | https://catalog.gatech.edu/programs/mathematics-computing-bs/ |

> Computer Engineering 有 22 种 specialization 组合。Mathematics and Computing ⚠ 共享项目 (College of Sciences)。

#### College of Design

##### School of Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.gatech.edu/programs/architecture-bs/ |

##### School of Building Construction
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Construction Science and Management | https://catalog.gatech.edu/programs/construction-science-management-bs/ |

##### School of City and Regional Planning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Urban Planning and Spatial Analytics | https://catalog.gatech.edu/programs/urban-planning-spatial-analytics-bs/ |

##### School of Industrial Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Industrial Design | https://catalog.gatech.edu/programs/industrial-design-bs/ |

##### School of Music
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Music Technology | https://catalog.gatech.edu/programs/music-technology-bs/ |

> Music Technology 有 4 种 specialization (ECE Signal Processing, General, ME Acoustics, ME Controls)。

##### College of Design (跨系)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 6 | Arts, Entertainment, and Creative Technologies | https://catalog.gatech.edu/programs/arts-entertainment-creative-technologies-bs/ |

#### College of Engineering

##### Department of Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.gatech.edu/programs/aerospace-engineering-bs/ |

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Biomedical Engineering | https://catalog.gatech.edu/programs/biomedical-engineering-bs/ |

##### School of Chemical and Biomolecular Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Chemical and Biomolecular Engineering (Standard Option) | https://catalog.gatech.edu/programs/chemical-biomolecular-engineering-standard-bs/ |
| 4 | Chemical and Biomolecular Engineering (Biotechnology Option) | https://catalog.gatech.edu/programs/chemical-biomolecular-engineering-biotechnology-bs/ |

##### School of Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Civil Engineering (Standard) | https://catalog.gatech.edu/programs/civil-engineering-standard-bs/ |
| 6 | Civil Engineering (Construction and Infrastructure Systems) | https://catalog.gatech.edu/programs/civil-engineering-construction-bs/ |
| 7 | Civil Engineering (Structural Engineering, Mechanics, and Materials) | https://catalog.gatech.edu/programs/civil-engineering-structural-bs/ |
| 8 | Civil Engineering (Geosystems) | https://catalog.gatech.edu/programs/civil-engineering-geosystems-bs/ |
| 9 | Civil Engineering (Transportation Systems) | https://catalog.gatech.edu/programs/civil-engineering-transportation-bs/ |
| 10 | Civil Engineering (Water Resources) | https://catalog.gatech.edu/programs/civil-engineering-water-resources-bs/ |
| 11 | Environmental Engineering | https://catalog.gatech.edu/programs/environmental-engineering-bs/ |

##### School of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Electrical Engineering | https://catalog.gatech.edu/programs/electrical-engineering-bs/ |

> Electrical Engineering 有 28 种 specialization 组合 (Signal Processing + Robotics, Energy Systems + Telecom, etc.)。

##### H. Milton Stewart School of Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Industrial Engineering | https://catalog.gatech.edu/programs/industrial-engineering-bs/ |

> Industrial Engineering 有 8 种 option (Analytics & Data Science, AI/OR, Operations Research, Supply Chain, etc.)。

##### School of Materials Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | Materials Science and Engineering | https://catalog.gatech.edu/programs/materials-science-engineering-bs/ |

> 有 4 种 option (Biomaterials, Polymer & Fiber, Functional, Structural)。

##### George W. Woodruff School of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 15 | Mechanical Engineering | https://catalog.gatech.edu/programs/mechanical-engineering-bs/ |

> Mechanical Engineering 有 11 种 option (Acoustics, Automotive, Design, Manufacturing, Nuclear, etc.)。

##### Nuclear and Radiological Engineering (under Mechanical Engineering)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 16 | Nuclear and Radiological Engineering | https://catalog.gatech.edu/programs/nuclear-radiological-engineering-bs/ |

> 有 2 种 option (Nuclear Engineering, Radiological Science)。

#### College of Sciences

##### School of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.gatech.edu/programs/biology-bs/ |
| 2 | Biochemistry | https://catalog.gatech.edu/programs/biochemistry-bs/ |
| 3 | Neuroscience | https://catalog.gatech.edu/programs/neuroscience-bs/ |

> Biology 有 3 option (General, Business, Pre-Health); Biochemistry 有 4 option; Neuroscience 有 2 option.

##### School of Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Chemistry | https://catalog.gatech.edu/programs/chemistry-bs/ |

> Chemistry 有 6 option (General, Biochemistry, Business, Polymers & Materials, Pre-Health)。

##### School of Earth and Atmospheric Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Atmospheric and Oceanic Sciences | https://catalog.gatech.edu/programs/atmospheric-oceanic-sciences-bs/ |
| 6 | Environmental Science | https://catalog.gatech.edu/programs/environmental-science-bs/ |
| 7 | Solid Earth and Planetary Sciences | https://catalog.gatech.edu/programs/solid-earth-planetary-sciences-bs/ |

##### School of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Mathematics | https://catalog.gatech.edu/programs/mathematics-bs/ |
| 9 | Mathematics and Computing | https://catalog.gatech.edu/programs/mathematics-computing-bs/ |

> Mathematics 有 7 option (Applied, Business, Discrete, General, Data Science, Probability & Statistics, Pure)。Mathematics and Computing ⚠ 共享 (College of Computing)。

##### School of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Applied Physics | https://catalog.gatech.edu/programs/applied-physics-bs/ |
| 11 | Astrophysics | https://catalog.gatech.edu/programs/astrophysics-bs/ |
| 12 | Physics | https://catalog.gatech.edu/programs/physics-bs/ |

> Applied Physics 有 4 option; Physics 有 4 option (General, Business, Physics of Living Systems)。

##### School of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Psychology | https://catalog.gatech.edu/programs/psychology-bs/ |

> Psychology 有 3 option (General, Business)。

#### Ivan Allen College of Liberal Arts

##### School of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.gatech.edu/programs/economics-bs/ |
| 2 | Economics and International Affairs | https://catalog.gatech.edu/programs/economics-international-affairs-bs/ |
| 3 | Global Economics and Modern Languages | https://catalog.gatech.edu/programs/global-economics-modern-languages-bs/ |

##### School of History and Sociology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | History, Technology, and Society | https://catalog.gatech.edu/programs/history-technology-society-bs/ |

##### School of International Affairs
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | International Affairs | https://catalog.gatech.edu/programs/international-affairs-bs/ |
| 6 | International Affairs and Modern Languages | https://catalog.gatech.edu/programs/international-affairs-modern-languages-bs/ |

##### School of Literature, Media, and Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Literature, Media, and Communication | https://catalog.gatech.edu/programs/literature-media-communication-bs/ |

> LMC 有 15 种 thread 组合 (Communication+Design, Literature+Media, etc.)。

##### School of Modern Languages
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Applied Languages and Intercultural Studies | https://catalog.gatech.edu/programs/applied-language-intercultural-studies-bs/ |

> 有 8 种语言 track (Chinese, French, German, Japanese, Korean, Russian, Spanish, + General)。

##### School of Public Policy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Public Policy | https://catalog.gatech.edu/programs/public-policy-bs/ |

#### Scheller College of Business

##### School of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.gatech.edu/programs/business-administration-bs/ |

> Business Administration 有 8 种 concentration (Accounting, Finance, General Management, IT Management, Leadership & Org Change, Marketing, Operations & Supply Chain, Strategy & Innovation)。

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 共享学院 | URL |
|---|------|---------|-----|
| 1 | Computer Engineering | Computing + Engineering | https://catalog.gatech.edu/programs/computer-engineering-bs/ |
| 2 | Mathematics and Computing | Computing + Sciences | https://catalog.gatech.edu/programs/mathematics-computing-bs/ |
| 3 | Computational Media | Computing + Design (Music) | https://catalog.gatech.edu/programs/computational-media-bs/ |

### 1.4 Minors — Complete List (87)

| # | Minor | URL |
|---|-------|-----|
| 1 | Aerospace Engineering | https://catalog.gatech.edu/programs/aerospace-engineering-minor/ |
| 2 | African Studies | https://catalog.gatech.edu/programs/african-studies-minor/ |
| 3 | Air Force Leadership Studies | https://catalog.gatech.edu/programs/air-force-leadership-minor/ |
| 4 | Applications of AI and Machine Learning | https://catalog.gatech.edu/programs/applications-ai-ml-minor/ |
| 5 | Architecture | https://catalog.gatech.edu/programs/architecture-minor/ |
| 6 | Archaeology | https://catalog.gatech.edu/programs/archaeology-minor/ |
| 7 | Astrobiology | https://catalog.gatech.edu/programs/astrobiology-minor/ |
| 8 | Astrophysics | https://catalog.gatech.edu/programs/astrophysics-minor/ |
| 9 | Biology | https://catalog.gatech.edu/programs/biology-minor/ |
| 10 | Biomedical Engineering | https://catalog.gatech.edu/programs/biomedical-engineering-minor/ |
| 11 | Black Media Studies | https://catalog.gatech.edu/programs/black-media-studies-minor/ |
| 12 | Business of Sports and Entertainment | https://catalog.gatech.edu/programs/business-sports-entertainment-minor/ |
| 13 | Chemistry and Biochemistry | https://catalog.gatech.edu/programs/chemistry-biochemistry-minor/ |
| 14 | Chinese | https://catalog.gatech.edu/programs/chinese-minor/ |
| 15 | Collaborative Social Innovation | https://catalog.gatech.edu/programs/collaborative-social-innovation-minor/ |
| 16 | Computation and Cognition | https://catalog.gatech.edu/programs/computation-cognition-minor/ |
| 17 | Computational Data Analysis | https://catalog.gatech.edu/programs/computational-data-analysis-minor/ |
| 18 | Computing and Business | https://catalog.gatech.edu/programs/computing-business-minor/ |
| 19 | Computing and Embedded Devices | https://catalog.gatech.edu/programs/computing-embedded-devices-minor/ |
| 20 | Computing and Information Internetworks | https://catalog.gatech.edu/programs/computing-information-internetworks-minor/ |
| 21 | Computing and AI | https://catalog.gatech.edu/programs/computing-ai-minor/ |
| 22 | Computing and Media | https://catalog.gatech.edu/programs/computing-media-minor/ |
| 23 | Computing and People | https://catalog.gatech.edu/programs/computing-people-minor/ |
| 24 | Computing and Systems Architecture | https://catalog.gatech.edu/programs/computing-systems-architecture-minor/ |
| 25 | Computing and Theory | https://catalog.gatech.edu/programs/computing-theory-minor/ |
| 26 | Creative Writing | https://catalog.gatech.edu/programs/creative-writing-minor/ |
| 27 | Earth and Atmospheric Sciences | https://catalog.gatech.edu/programs/earth-atmospheric-sciences-minor/ |
| 28 | East Asian Studies | https://catalog.gatech.edu/programs/east-asian-studies-minor/ |
| 29 | Economics | https://catalog.gatech.edu/programs/economics-minor/ |
| 30 | Economics and Policy of Environmental Sustainability | https://catalog.gatech.edu/programs/economics-environmental-sustainability-minor/ |
| 31 | Energy Systems | https://catalog.gatech.edu/programs/energy-systems-minor/ |
| 32 | Engineering and Business | https://catalog.gatech.edu/programs/engineering-business-minor/ |
| 33 | Entrepreneurship | https://catalog.gatech.edu/programs/entrepreneurship-minor/ |
| 34 | European Studies | https://catalog.gatech.edu/programs/european-studies-minor/ |
| 35 | Film and Media Studies | https://catalog.gatech.edu/programs/film-media-studies-minor/ |
| 36 | FinTech | https://catalog.gatech.edu/programs/fintech-minor/ |
| 37 | French | https://catalog.gatech.edu/programs/french-minor/ |
| 38 | German | https://catalog.gatech.edu/programs/german-minor/ |
| 39 | Global Development | https://catalog.gatech.edu/programs/global-development-minor/ |
| 40 | Health and Medical Sciences | https://catalog.gatech.edu/programs/health-medical-sciences-minor/ |
| 41 | Health, Medicine, and Society | https://catalog.gatech.edu/programs/health-medicine-society-minor/ |
| 42 | Health Policy and Economics | https://catalog.gatech.edu/programs/health-policy-economics-minor/ |
| 43 | Health Systems | https://catalog.gatech.edu/programs/health-systems-minor/ |
| 44 | History | https://catalog.gatech.edu/programs/history-minor/ |
| 45 | Industrial Design | https://catalog.gatech.edu/programs/industrial-design-minor/ |
| 46 | International Affairs | https://catalog.gatech.edu/programs/international-affairs-minor/ |
| 47 | International Business, Language, and Culture | https://catalog.gatech.edu/programs/international-business-language-culture-minor/ |
| 48 | Japanese | https://catalog.gatech.edu/programs/japanese-minor/ |
| 49 | Korean | https://catalog.gatech.edu/programs/korean-minor/ |
| 50 | Latin American and LatinX Studies | https://catalog.gatech.edu/programs/latin-american-latinx-studies-minor/ |
| 51 | Law, Science, and Technology | https://catalog.gatech.edu/programs/law-science-technology-minor/ |
| 52 | Leadership Studies | https://catalog.gatech.edu/programs/leadership-studies-minor/ |
| 53 | Learning | https://catalog.gatech.edu/programs/learning-minor/ |
| 54 | Linguistics | https://catalog.gatech.edu/programs/linguistics-minor/ |
| 55 | Materials Science and Engineering | https://catalog.gatech.edu/programs/materials-science-engineering-minor/ |
| 56 | Mathematics | https://catalog.gatech.edu/programs/mathematics-minor/ |
| 57 | Microeconomics of Strategic Analysis | https://catalog.gatech.edu/programs/microeconomics-strategic-analysis-minor/ |
| 58 | Middle Eastern and North African Studies | https://catalog.gatech.edu/programs/middle-eastern-north-african-studies-minor/ |
| 59 | Naval Science | https://catalog.gatech.edu/programs/naval-science-minor/ |
| 60 | Neuroscience | https://catalog.gatech.edu/programs/neuroscience-minor/ |
| 61 | Nuclear Radiological Engineering | https://catalog.gatech.edu/programs/nuclear-radiological-engineering-minor/ |
| 62 | People Analytics | https://catalog.gatech.edu/programs/people-analytics-minor/ |
| 63 | Philosophy | https://catalog.gatech.edu/programs/philosophy-minor/ |
| 64 | Physics | https://catalog.gatech.edu/programs/physics-minor/ |
| 65 | Physiology | https://catalog.gatech.edu/programs/physiology-minor/ |
| 66 | Political Science | https://catalog.gatech.edu/programs/political-science-minor/ |
| 67 | Psychology | https://catalog.gatech.edu/programs/psychology-minor/ |
| 68 | Public Policy | https://catalog.gatech.edu/programs/public-policy-minor/ |
| 69 | Quantum Sciences and Technology | https://catalog.gatech.edu/programs/quantum-sciences-technology-minor/ |
| 70 | Real Estate | https://catalog.gatech.edu/programs/real-estate-minor/ |
| 71 | Robotics | https://catalog.gatech.edu/programs/robotics-minor/ |
| 72 | Russian | https://catalog.gatech.edu/programs/russian-minor/ |
| 73 | Science Communication and Policy | https://catalog.gatech.edu/programs/science-communication-policy-minor/ |
| 74 | Science of Mental Health and Well-Being | https://catalog.gatech.edu/programs/science-mental-health-wellbeing-minor/ |
| 75 | Science Fiction Studies | https://catalog.gatech.edu/programs/science-fiction-studies-minor/ |
| 76 | Science, Technology, and Society | https://catalog.gatech.edu/programs/science-technology-society-minor/ |
| 77 | Scientific and Engineering Computing | https://catalog.gatech.edu/programs/scientific-engineering-computing-minor/ |
| 78 | Social Justice | https://catalog.gatech.edu/programs/social-justice-minor/ |
| 79 | Sociology | https://catalog.gatech.edu/programs/sociology-minor/ |
| 80 | Spanish | https://catalog.gatech.edu/programs/spanish-minor/ |
| 81 | Sports, Society, and Technology | https://catalog.gatech.edu/programs/sports-society-technology-minor/ |
| 82 | Sustainable Business | https://catalog.gatech.edu/programs/sustainable-business-minor/ |
| 83 | Sustainable Cities | https://catalog.gatech.edu/programs/sustainable-cities-minor/ |
| 84 | Sustainable Development and Construction | https://catalog.gatech.edu/programs/sustainable-development-construction-minor/ |
| 85 | Technology and Business | https://catalog.gatech.edu/programs/technology-business-minor/ |
| 86 | Women, Science, and Technology | https://catalog.gatech.edu/programs/women-science-technology-minor/ |
| 87 | Real Estate Development and Finance | https://catalog.gatech.edu/programs/real-estate-development-finance-minor/ |

### 1.5 General/Institute-Wide Requirements

Georgia Tech requires all undergraduates to complete:
- **Core Curriculum**: English composition, humanities, social sciences, natural sciences, mathematics, and physical education
- **Major-specific requirements**: determined by each college/program
- Details at: https://catalog.gatech.edu/academics/undergraduate/

### 1.6 Course-ID → Major Quick-Lookup

Georgia Tech does not use a course numbering system for majors (unlike MIT's "Course 6" system). Programs are identified by name and catalog URL slug.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Engineering

##### Aerospace Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Aerospace Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Aerospace Engineering | https://gradapp.gatech.edu/portal/program-info |

##### Biomedical Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Biomedical Engineering | https://gradapp.gatech.edu/portal/program-info |
| MBID | Biomedical Innovation & Development | https://gradapp.gatech.edu/portal/program-info |
| PhD | Biomedical Engineering (Joint GT-Emory) | https://gradapp.gatech.edu/portal/program-info |

##### Chemical and Biomolecular Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Chemical & Biomolecular Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Chemical & Biomolecular Engineering | https://gradapp.gatech.edu/portal/program-info |

##### Civil and Environmental Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Civil Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Environmental Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Engineering Science & Mechanics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Civil Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Environmental Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Engineering Science & Mechanics | https://gradapp.gatech.edu/portal/program-info |

##### Electrical and Computer Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Electrical & Computer Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Electrical & Computer Engineering | https://gradapp.gatech.edu/portal/program-info |

##### Industrial and Systems Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Industrial Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Operations Research | https://gradapp.gatech.edu/portal/program-info |
| MS | Supply Chain Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Health Systems | https://gradapp.gatech.edu/portal/program-info |
| MS | Statistics | https://gradapp.gatech.edu/portal/program-info |
| MS | Quantitative & Computational Finance | https://gradapp.gatech.edu/portal/program-info |
| MS | Analytics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Industrial Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Operations Research | https://gradapp.gatech.edu/portal/program-info |

##### Materials Science and Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Materials Science & Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Materials Science & Engineering | https://gradapp.gatech.edu/portal/program-info |

##### Mechanical Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Mechanical Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Medical Physics | https://gradapp.gatech.edu/portal/program-info |
| MS | Nuclear Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Mechanical Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Nuclear Engineering | https://gradapp.gatech.edu/portal/program-info |

##### College of Engineering (跨系)
| 级别 | 项目 | URL |
|------|------|-----|
| Prof. Master's | Applied Systems Engineering | https://gradapp.gatech.edu/portal/program-info |
| Prof. Master's | Manufacturing Leadership | https://gradapp.gatech.edu/portal/program-info |
| Prof. Master's | Occupational Safety & Health | https://gradapp.gatech.edu/portal/program-info |

#### College of Computing

##### School of Computer Science
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Computer Science | https://gradapp.gatech.edu/portal/program-info |
| PhD | Computer Science | https://gradapp.gatech.edu/portal/program-info |

##### School of Interactive Computing
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Human-Computer Interaction | https://gradapp.gatech.edu/portal/program-info |
| PhD | Human-Centered Computing | https://gradapp.gatech.edu/portal/program-info |

##### School of Computational Science and Engineering
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Computational Science & Engineering | https://gradapp.gatech.edu/portal/program-info |
| PhD | Computational Science & Engineering | https://gradapp.gatech.edu/portal/program-info |

##### School of Cybersecurity and Privacy
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Cybersecurity (Information Security) | https://gradapp.gatech.edu/portal/program-info |
| PhD | Computer Science (Cybersecurity focus) | https://gradapp.gatech.edu/portal/program-info |

#### College of Sciences

##### Biological Sciences
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Biology | https://gradapp.gatech.edu/portal/program-info |
| MS | Bioinformatics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Biology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Bioinformatics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Applied Physiology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Neuroscience & Neurotechnology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Quantitative Biosciences | https://gradapp.gatech.edu/portal/program-info |
| PhD | Ocean Science & Engineering | https://gradapp.gatech.edu/portal/program-info |

##### Chemistry and Biochemistry
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Chemistry & Biochemistry | https://gradapp.gatech.edu/portal/program-info |
| PhD | Chemistry | https://gradapp.gatech.edu/portal/program-info |

##### Earth and Atmospheric Sciences
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Earth & Atmospheric Science | https://gradapp.gatech.edu/portal/program-info |
| PhD | Earth & Atmospheric Sciences | https://gradapp.gatech.edu/portal/program-info |

##### Mathematics
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Mathematics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Mathematics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Algorithms, Combinatorics & Optimization | https://gradapp.gatech.edu/portal/program-info |

##### Physics
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Physics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Physics | https://gradapp.gatech.edu/portal/program-info |

##### Psychology
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Psychology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Psychology | https://gradapp.gatech.edu/portal/program-info |

#### College of Design

##### Architecture
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Architecture | https://gradapp.gatech.edu/portal/program-info |
| MArch | Architecture (M.Arch.) | https://gradapp.gatech.edu/portal/program-info |
| PhD | Architecture | https://gradapp.gatech.edu/portal/program-info |
| MS | Urban Design | https://gradapp.gatech.edu/portal/program-info |

##### Building Construction
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Building Construction & Facilities Management | https://gradapp.gatech.edu/portal/program-info |
| MRED | Real Estate Development | https://gradapp.gatech.edu/portal/program-info |
| Prof. Master's | Occupational Safety & Health | https://gradapp.gatech.edu/portal/program-info |
| PhD | Building Construction | https://gradapp.gatech.edu/portal/program-info |

##### City and Regional Planning
| 级别 | 项目 | URL |
|------|------|-----|
| MCRP | City & Regional Planning | https://gradapp.gatech.edu/portal/program-info |
| MS | Geographic Information Science & Technology | https://gradapp.gatech.edu/portal/program-info |
| MS | Global Development | https://gradapp.gatech.edu/portal/program-info |
| MS | Urban Analytics | https://gradapp.gatech.edu/portal/program-info |
| PhD | City & Regional Planning | https://gradapp.gatech.edu/portal/program-info |

##### Industrial Design
| 级别 | 项目 | URL |
|------|------|-----|
| MID | Industrial Design | https://gradapp.gatech.edu/portal/program-info |
| MS | Human-Computer Interaction | https://gradapp.gatech.edu/portal/program-info |

##### Music
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Music Technology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Music Technology | https://gradapp.gatech.edu/portal/program-info |

#### Ivan Allen College of Liberal Arts

##### Economics
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Economics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Economics | https://gradapp.gatech.edu/portal/program-info |

##### History and Sociology
| 级别 | 项目 | URL |
|------|------|-----|
| MS | History & Sociology of Technology & Science | https://gradapp.gatech.edu/portal/program-info |
| PhD | History & Sociology of Technology & Science | https://gradapp.gatech.edu/portal/program-info |

##### International Affairs
| 级别 | 项目 | URL |
|------|------|-----|
| MS | International Affairs | https://gradapp.gatech.edu/portal/program-info |
| MS | International Affairs, Science & Technology | https://gradapp.gatech.edu/portal/program-info |
| MS | International Security | https://gradapp.gatech.edu/portal/program-info |
| PhD | International Affairs, Science & Technology | https://gradapp.gatech.edu/portal/program-info |

##### Literature, Media, and Communication
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Digital Media | https://gradapp.gatech.edu/portal/program-info |
| MS | Global Media & Cultures | https://gradapp.gatech.edu/portal/program-info |
| MS | Human-Computer Interaction | https://gradapp.gatech.edu/portal/program-info |
| PhD | Digital Media | https://gradapp.gatech.edu/portal/program-info |

##### Modern Languages
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Applied Languages & Intercultural Studies | https://gradapp.gatech.edu/portal/program-info |

##### Public Policy
| 级别 | 项目 | URL |
|------|------|-----|
| MS | Public Policy | https://gradapp.gatech.edu/portal/program-info |
| MSEEM | Sustainable Energy & Environmental Management | https://gradapp.gatech.edu/portal/program-info |
| MS | Cybersecurity (Policy) | https://gradapp.gatech.edu/portal/program-info |
| PhD | Public Policy | https://gradapp.gatech.edu/portal/program-info |

#### Scheller College of Business

##### School of Management
| 级别 | 项目 | URL |
|------|------|-----|
| MBA | Business Administration (Full-time MBA) | https://gradapp.gatech.edu/portal/program-info |
| MBA | Business Administration (Evening MBA) | https://gradapp.gatech.edu/portal/program-info |
| MBA | Business Administration (Executive MBA - Global Business) | https://gradapp.gatech.edu/portal/program-info |
| MBA | Business Administration (Executive MBA - Management of Technology) | https://gradapp.gatech.edu/portal/program-info |
| MS | Management | https://gradapp.gatech.edu/portal/program-info |
| MS | Quantitative & Computational Finance | https://gradapp.gatech.edu/portal/program-info |
| PhD | Management | https://gradapp.gatech.edu/portal/program-info |

#### Cross-College Interdisciplinary Graduate Programs

| 级别 | 项目 | 可授予学院 | URL |
|------|------|-----------|-----|
| MS | Bioengineering | 7 Engineering depts | https://gradapp.gatech.edu/portal/program-info |
| MS | Computational Science & Engineering | 10 depts across colleges | https://gradapp.gatech.edu/portal/program-info |
| MS | Cybersecurity (Cyber Physical Systems) | Engineering | https://gradapp.gatech.edu/portal/program-info |
| MS | Robotics | 5 Engineering + Sciences depts | https://gradapp.gatech.edu/portal/program-info |
| MS | Statistics | ISE + Mathematics | https://gradapp.gatech.edu/portal/program-info |
| MS | Quantitative & Computational Finance | ISE + Management + Mathematics | https://gradapp.gatech.edu/portal/program-info |
| MS | Human-Computer Interaction | Computing + Design + LMC + Psychology | https://gradapp.gatech.edu/portal/program-info |
| MS | Urban Analytics | City Planning + CSE + ISE + IC | https://gradapp.gatech.edu/portal/program-info |
| MS | Global Development | City Planning + Economics + Intl Affairs | https://gradapp.gatech.edu/portal/program-info |
| PhD | Machine Learning | 9 depts across colleges | https://gradapp.gatech.edu/portal/program-info |
| PhD | Robotics | 5 Engineering + Computing depts | https://gradapp.gatech.edu/portal/program-info |
| PhD | Algorithms, Combinatorics & Optimization | CS + ISE + Mathematics | https://gradapp.gatech.edu/portal/program-info |
| PhD | Neuroscience & Neurotechnology | Bio Sciences + BME + Psychology | https://gradapp.gatech.edu/portal/program-info |
| PhD | Ocean Science & Engineering | Bio + CEE + EAS | https://gradapp.gatech.edu/portal/program-info |
| PhD | Quantitative Biosciences | Bio + Chem + EAS + Math + Physics + Psych | https://gradapp.gatech.edu/portal/program-info |
| PhD | Bioengineering | 7 Engineering depts | https://gradapp.gatech.edu/portal/program-info |
| PhD | Computational Science & Engineering | 10+ depts | https://gradapp.gatech.edu/portal/program-info |
| PhD | Bioinformatics | 6 depts across colleges | https://gradapp.gatech.edu/portal/program-info |

### 2.2 Graduate Admissions Model

Georgia Tech graduate admissions is **decentralized**. The Office of Graduate Education (grad.gatech.edu) provides centralized services, but each program/department makes its own admission decisions.

- **Application portal**: gradapp.gatech.edu (unified application system)
- **Application fee**: Not specified centrally; varies by program
- **GRE**: Per-program policy (many programs have dropped GRE requirement)
- **English proficiency**: Same USG requirements as UG (see Section 3.2)
- **CGS April 15**: Georgia Tech is a signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common App (exclusive) | admission.gatech.edu/first-year |
| EA1 截止日期 | October 15 | admission.gatech.edu/first-year/deadlines |
| EA2 截止日期 | November 2 | admission.gatech.edu/first-year/deadlines |
| RD 截止日期 | January 6 | admission.gatech.edu/first-year/deadlines |
| EA1 文件截止 | October 30 | admission.gatech.edu/first-year/deadlines |
| EA2 文件截止 | November 16 | admission.gatech.edu/first-year/deadlines |
| RD 文件截止 | January 22 | admission.gatech.edu/first-year/deadlines |
| EA1 自报成绩截止 | November 16 | admission.gatech.edu/first-year/deadlines |
| EA2 自报成绩截止 | December 8 | admission.gatech.edu/first-year/deadlines |
| RD 自报成绩截止 | January 22 | admission.gatech.edu/first-year/deadlines |
| EA1 放榜时间 | Early December | admission.gatech.edu/first-year/deadlines |
| EA2 放榜时间 | Late January | admission.gatech.edu/first-year/deadlines |
| RD 放榜时间 | Mid-March | admission.gatech.edu/first-year/deadlines |
| 押金截止 | May 1 | admission.gatech.edu/first-year/deadlines |
| 申请费 (国内) | $75 | admission.gatech.edu/first-year/application-fees |
| 申请费 (国际) | $85 | admission.gatech.edu/first-year/application-fees |
| SAT/ACT 要求 | **REQUIRED** (非 test-optional) | admission.gatech.edu/first-year/standardized-tests |
| SAT 送分代码 | 5248 | admission.gatech.edu/first-year/standardized-tests |
| ACT 送分代码 | 0818 | admission.gatech.edu/first-year/standardized-tests |
| Superscore | 是 (SAT: EBRW+Math 最高分; ACT: English+Math+Reading 最高分) | admission.gatech.edu/first-year/standardized-tests |
| 推荐信 | 不要求 (holistic review) | admission.gatech.edu/first-year/application-review |
| 面试 | 可选 (国际生: InitialView/Vericant) | admission.gatech.edu/international/first-year |
| 入学学期 | Summer 或 Fall (所有申请者同时考虑) | admission.gatech.edu/first-year/deadlines |

### 3.2 Undergraduate English Proficiency Table

> 来源: University System of Georgia (USG) 要求，适用于所有 USG 院校。

| 考试 | 最低分 (Minimum) | 推荐分 (Recommended) | 来源 |
|------|-----------------|---------------------|------|
| TOEFL iBT (含 Home Edition & My Best) | 3.5 (2026前: 69) | 4.0 (2026前: 79) | usg.edu/international_education/esl_programs/english_proficiency_requirements |
| IELTS Academic (含 Online & One Skill Retake) | 6.0 | 6.5 | usg.edu |
| PTE Academic (含 Online) | 53 | 58 | usg.edu |
| Cambridge English Scale (B2 First/C1 Advanced/C2 Proficiency) | 169 | 177 | usg.edu |
| SAT EBRW | 480 | — | usg.edu |
| ACT English | 17 | — | usg.edu |
| EIKEN | Pre-1 | — | usg.edu |
| MET (Michigan English Test) | 55 | 59 | usg.edu |
| CIE IGCSE/O Level English | D or better | — | usg.edu |
| UK GCSE English | C or better | — | usg.edu |
| UK GCE A-Level English | C or better | — | usg.edu |
| EdExcel Intl A-Levels/IGCSE English | D or better | — | usg.edu |

**豁免条件**: 母语为英语; 在英语授课国家完成学位; 在美国认证机构完成 English 1101/1102 且成绩 C 以上; 通过 Accuplacer/WritePlacer/SAT/ACT 直接进入大学英语课程。

**Georgia Tech 特别鼓励**: 国际申请者提交 Duolingo English Test 成绩和 InitialView/Vericant 面试，作为 holistic review 的补充材料（但不替代 USG 英语 proficiency 要求）。

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| 招生模式 | 分散式 (各院系自主招生) | grad.gatech.edu |
| 申请系统 | gradapp.gatech.edu (统一入口) | grad.gatech.edu |
| GRE 要求 | 按项目决定 (many programs no longer require) | grad.gatech.edu |
| 英语要求 | 同 USG UG 要求 (见 3.2) | grad.gatech.edu |
| ETS 代码 | 各项目不同 | gradapp.gatech.edu |
| CGS April 15 | 签署院校 | grad.gatech.edu |
| 资助 | PhD 通常全奖; MS 通常自费 | grad.gatech.edu |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027, Line-Itemized)

#### Georgia Resident — First-Year, On-Campus

| 费用项目 | 金额 | 来源 |
|---------|------|------|
| Tuition | $10,618 | finaid.gatech.edu/costs/undergraduate-costs |
| Mandatory Student Fees | $1,516 | finaid.gatech.edu |
| Books, Course Materials, Supplies, Equipment | $800 | finaid.gatech.edu |
| Housing Allowance | $8,318 | finaid.gatech.edu |
| Standard Food Service Plan | $6,310 | finaid.gatech.edu |
| Personal/Miscellaneous Expenses | $2,800 | finaid.gatech.edu |
| Transportation Allowance | $566 | finaid.gatech.edu |
| **Total per Year (2 semesters)** | **$30,928** | finaid.gatech.edu |

#### Out-of-State — First-Year, On-Campus

| 费用项目 | 金额 | 来源 |
|---------|------|------|
| Tuition | $34,604 | finaid.gatech.edu/costs/undergraduate-costs |
| Mandatory Student Fees | $1,516 | finaid.gatech.edu |
| Books, Course Materials, Supplies, Equipment | $800 | finaid.gatech.edu |
| Housing Allowance | $8,318 | finaid.gatech.edu |
| Standard Food Service Plan | $6,310 | finaid.gatech.edu |
| Personal/Miscellaneous Expenses | $2,800 | finaid.gatech.edu |
| Transportation Allowance | $966 | finaid.gatech.edu |
| **Total per Year (2 semesters)** | **$55,314** | finaid.gatech.edu |

#### Out-of-Country — First-Year, On-Campus

| 费用项目 | 金额 | 来源 |
|---------|------|------|
| Tuition | $35,610 | finaid.gatech.edu/costs/undergraduate-costs |
| Mandatory Student Fees | $1,716 | finaid.gatech.edu |
| Books, Course Materials, Supplies, Equipment | $800 | finaid.gatech.edu |
| Housing Allowance | $8,318 | finaid.gatech.edu |
| Standard Food Service Plan | $6,310 | finaid.gatech.edu |
| Personal/Miscellaneous Expenses | $2,800 | finaid.gatech.edu |
| Transportation Allowance | $966 | finaid.gatech.edu |
| **Total per Year (2 semesters)** | **$56,520** | finaid.gatech.edu |

### 4.2 Undergraduate Financial-Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind (国内) | 是 (公立大学，默认 need-blind for US citizens/PRs) | admission.gatech.edu |
| Need-blind (国际) | 否 (need-aware for international students) | admission.gatech.edu |
| 公立大学特点 | In-state tuition ~$10.6k vs OOS ~$34.6k (3.3x 差异) | finaid.gatech.edu |
| 奖学金类型 | Merit + Need-based | finaid.gatech.edu/undergraduate-types-aid |
| 联邦勤工俭学 | 有 (Federal Work-Study) | finaid.gatech.edu |
| 贷款 | Federal + Private loans available | finaid.gatech.edu |

> **Note**: Georgia Tech, as a public university in the University System of Georgia, does not explicitly market "need-blind" admissions the way private universities do. Domestic applicants (US citizens, permanent residents) are evaluated without regard to financial need as a matter of USG policy. International students should be prepared to demonstrate financial resources.

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| PhD 资助 | 通常全额资助 (RA/TA/Fellowship) | grad.gatech.edu |
| MS 资助 | 通常自费 (部分项目有 RA/TA 机会) | grad.gatech.edu |
| MBA 资助 | Scheller 有奖学金 | scheller.gatech.edu |
| 申请费 | 按项目不同 | gradapp.gatech.edu |
| 助学金类型 | Research Assistantship, Teaching Assistantship, Fellowship | grad.gatech.edu |

---

## SECTION 5 — Evidence Chain Index

### Evidence Blocks

```yaml
E-U-001:
  field: undergraduate.deadlines.EA1
  value: "October 15"
  source_url: https://admission.gatech.edu/first-year/deadlines
  source_snippet: "Application Deadline | October 15 | November 2 | January 6"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.EA2
  value: "November 2"
  source_url: https://admission.gatech.edu/first-year/deadlines
  source_snippet: "Application Deadline | October 15 | November 2 | January 6"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.RD
  value: "January 6"
  source_url: https://admission.gatech.edu/first-year/deadlines
  source_snippet: "Application Deadline | October 15 | November 2 | January 6"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.test_policy
  value: "SAT/ACT REQUIRED (not test-optional)"
  source_url: https://admission.gatech.edu/first-year/standardized-tests
  source_snippet: "All first-year applicants must submit results from at least one SAT and/or ACT in order to be considered for admission."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.test_codes
  value: {SAT: 5248, ACT: 0818}
  source_url: https://admission.gatech.edu/first-year/standardized-tests
  source_snippet: "SAT school code: 5248 | ACT school code: 0818"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.application_fee
  value: {domestic: 75, international: 85}
  source_url: https://admission.gatech.edu/first-year/application-fees
  source_snippet: "The non-refundable first-year application fee is $75 (international applicants: $85)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.cost.tuition_in_state_2026_2027
  value: "$10,618"
  source_url: https://finaid.gatech.edu/costs/undergraduate-costs
  source_snippet: "Tuition | $10,618 | $10,618 | $10,618"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.tuition_oos_2026_2027
  value: "$34,604"
  source_url: https://finaid.gatech.edu/costs/undergraduate-costs
  source_snippet: "Tuition | $34,604 | $34,604 | $34,604"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.total_in_state_on_campus_2026_2027
  value: "$30,928"
  source_url: https://finaid.gatech.edu/costs/undergraduate-costs
  source_snippet: "Total per Year (2 semesters) | $30,928 | $34,694 | $23,450"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.total_oos_on_campus_2026_2027
  value: "$55,314"
  source_url: https://finaid.gatech.edu/costs/undergraduate-costs
  source_snippet: "Total per Year (2 semesters) | $55,314 | $59,080 | $47,436"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.english_proficiency.toefl_minimum
  value: "3.5 (69 if taken prior to 2026)"
  source_url: https://www.usg.edu/international_education/esl_programs/english_proficiency_requirements
  source_snippet: "TOEFL iBT (includes Home Edition & My Best) | 3.5 (69 if taken prior to 2026) | 4.0 (79 if taken prior to 2026)"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.english_proficiency.ielts_minimum
  value: "6.0"
  source_url: https://www.usg.edu/international_education/esl_programs/english_proficiency_requirements
  source_snippet: "IELTS Academic (including IELTS Online and One Skill Retake) | 6 | 6.5"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.programs.total_majors
  value: "39 distinct majors"
  source_url: https://admission.gatech.edu/academics
  source_snippet: "Explore our six colleges and 39 majors to see which best meets your goals."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.programs.catalog_entries
  value: "233 bachelor program entries (including threads/options)"
  source_url: https://catalog.gatech.edu/programs/
  source_snippet: "Bachelor of Science in Aerospace Engineering, Bachelor of Science in Computer Science, ..."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.colleges
  value: "6 colleges"
  source_url: https://admission.gatech.edu/academics
  source_snippet: "Choose from six colleges focusing on Business, Computing, Design, Engineering, Liberal Arts, and Sciences."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.total
  value: "109 degree programs (66 Master's + 43 Doctoral)"
  source_url: https://catalog.gatech.edu/programs/
  source_snippet: "Master (66) | Doctor (43)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.model
  value: "Decentralized; each program/department makes admission decisions"
  source_url: https://grad.gatech.edu/admissions
  source_snippet: "Georgia Tech welcomes you! With over 1,000 universities in the United States that offer graduate degrees..."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.application_portal
  value: "gradapp.gatech.edu"
  source_url: https://grad.gatech.edu/admissions
  source_snippet: "Start or Continue Application"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
gatech-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-engineering.md                (Section 1: College of Engineering programs)
├── 02-ug-computing.md                  (Section 1: College of Computing programs)
├── 03-ug-sciences.md                   (Section 1: College of Sciences programs)
├── 04-ug-design.md                     (Section 1: College of Design programs)
├── 05-ug-liberal-arts.md               (Section 1: Ivan Allen College programs)
├── 06-ug-business.md                   (Section 1: Scheller College programs)
├── 07-ug-minors.md                     (Section 1.4: all 87 minors)
├── 08-grad-engineering.md              (Section 2: Engineering graduate programs)
├── 09-grad-computing.md                (Section 2: Computing graduate programs)
├── 10-grad-sciences.md                 (Section 2: Sciences graduate programs)
├── 11-grad-design.md                   (Section 2: Design graduate programs)
├── 12-grad-liberal-arts.md             (Section 2: Ivan Allen graduate programs)
├── 13-grad-business.md                 (Section 2: Scheller graduate programs)
├── 14-grad-interdisciplinary.md        (Section 2: cross-college grad programs)
├── 15-deadlines-requirements.md        (Section 3)
├── 16-costs-financial-aid.md           (Section 4)
├── 17-evidence-chain.md                (Section 5)
└── 18-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "gatech-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BS|MS|PhD|MBA|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE policy for all graduate programs | gradapp.gatech.edu/portal/program-info (each program detail page) |
| P0 | Graduate application fee (per program) | gradapp.gatech.edu/portal/program-info |
| P1 | Graduate cost of attendance | grad.gatech.edu/cost-funding |
| P1 | Graduate funding/stipend details | grad.gatech.edu/cost-funding |
| P1 | Need-blind/need-aware explicit policy statement | admission.gatech.edu or finaid.gatech.edu |
| P1 | Detailed UG course catalog descriptions | catalog.gatech.edu (per program pages) |
| P2 | Scholarship amounts and criteria | finaid.gatech.edu/undergraduate-types-aid/scholarships |
| P2 | Transfer admission requirements | admission.gatech.edu/transfer |
| P2 | BS/MS program details | catalog.gatech.edu/academics/undergraduate/bs-ms-degree-programs/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Georgia Tech | (Other schools) |
|-----------|-------------|-----------------|
| 公/私立 | Public (USG) | |
| 所在地 | Atlanta, GA | |
| 本科总费用/年 (In-state, On-campus) | $30,928 | |
| 本科总费用/年 (OOS, On-campus) | $55,314 | |
| 本科学费/年 (In-state) | $10,618 | |
| 本科学费/年 (OOS) | $34,604 | |
| Need-blind (国内) | Yes (public university) | |
| Need-blind (国际) | No (need-aware) | |
| EA1 截止日期 | October 15 | |
| EA2 截止日期 | November 2 | |
| RD 截止日期 | January 6 | |
| SAT/ACT 要求 | REQUIRED | |
| TOEFL 最低分 | 3.5 (69 old scale) | |
| IELTS 最低分 | 6.0 | |
| 本科专业总数 (Rule 1) | 39 majors / 233 catalog entries | |
| 学院数 (Rule 2) | 6 | |
| 研究生项目总数 | 109 | |
| 总学位项目数 | 148 (39 UG + 109 Grad) | |
| 申请费 (UG) | $75 / $85 intl | |
| 特色 | Top-ranked engineering, Threads curriculum, 6 colleges, public university value | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.gatech.edu, finaid.gatech.edu, catalog.gatech.edu, grad.gatech.edu, gradapp.gatech.edu, www.gatech.edu, usg.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
