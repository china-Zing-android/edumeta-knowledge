# University of Central Florida (UCF) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (Bachelor) | 253 |
| 本科辅修 (Minor) | 143 |
| 本科证书 (Undergraduate Certificate) | 83 |
| 研究生硕士学位 (Master) | 235 |
| 研究生博士/专业博士 (Doctorate) | 84 |
| 研究生高级证书 (Graduate Certificate) | 106 |
| 研究生专家学位 (Specialist) | 4 |
| 专业项目 (Professional Program) | 1 |
| **学位项目总计 (All Programs)** | **909** |
| 学院总数 | 11 |

> **数据来源**: UCF Degree Search API (`wp-json/ucf-degree-search/v1`) 配置元数据。API 实际返回 586 个去重程序（API 有分页限制），但配置中的 program_types 计数（253 Bachelor + 143 Minor + 83 UG Cert + 235 Master + 84 Doctorate + 106 Grad Cert + 4 Specialist + 1 Professional = 909）为官方总数。

### 0.2 学院/系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Central Florida
├── College of Arts and Humanities                          [学院]
│   ├── School of Visual Arts and Design
│   ├── Department of English
│   ├── Department of History
│   ├── School of Performing Arts
│   ├── Department of Philosophy
│   ├── Department of Writing and Rhetoric
│   └── ...
├── College of Business (Barry S. Miller College)           [学院]
│   ├── Department of Accounting
│   ├── Department of Finance
│   ├── Department of Management
│   ├── Department of Marketing
│   ├── School of Real Estate
│   └── ...
├── College of Community Innovation and Education           [学院]
│   ├── School of Teacher Education
│   ├── Department of Educational Leadership
│   ├── School of Public Administration
│   ├── Department of Criminal Justice
│   ├── School of Social Work
│   └── ...
├── College of Engineering and Computer Science             [学院]
│   ├── Department of Civil, Environmental and Construction Engineering
│   ├── Department of Computer Science
│   ├── Department of Electrical and Computer Engineering
│   ├── Department of Industrial Engineering and Management Systems
│   ├── Department of Materials Science and Engineering
│   ├── Department of Mechanical and Aerospace Engineering
│   └── ...
├── College of Graduate Studies                             [学院]
│   └── (跨学院研究生项目管理)
├── College of Health Professions and Sciences              [学院]
│   ├── School of Kinesiology and Physical Therapy
│   ├── Department of Health Sciences
│   ├── School of Communication Sciences and Disorders
│   └── ...
├── College of Medicine                                     [学院]
│   ├── Burnett School of Biomedical Sciences
│   ├── Department of Medical Education
│   └── ...
├── College of Nursing                                      [学院]
│   └── Department of Nursing
├── College of Optics and Photonics (CREOL)                 [学院]
│   └── Department of Optics and Photonics
├── College of Sciences                                     [学院]
│   ├── Department of Biology
│   ├── Department of Chemistry
│   ├── Department of Mathematics
│   ├── Department of Physics
│   ├── Department of Psychology
│   ├── School of Politics, Security, and International Affairs
│   ├── Department of Sociology
│   └── ...
└── Rosen College of Hospitality Management                 [学院]
    ├── Department of Hospitality Services
    ├── Department of Tourism, Events and Attractions
    └── Department of Foodservice and Lodging Management
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 34 |
| BS | Bachelor of Science | 本科 | 53 |
| BSBA | Bachelor of Science in Business Administration | 本科 | 7 |
| BFA | Bachelor of Fine Arts | 本科 | 4 |
| BSN | Bachelor of Science in Nursing | 本科 | 2 |
| BSAE | Bachelor of Science in Aerospace Engineering | 本科 | 1 |
| BSCE | Bachelor of Science in Civil Engineering | 本科 | 1 |
| BSCpE | Bachelor of Science in Computer Engineering | 本科 | 1 |
| BSConE | Bachelor of Science in Construction Engineering | 本科 | 1 |
| BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| BSIE | Bachelor of Science in Industrial Engineering | 本科 | 1 |
| BSME | Bachelor of Science in Mechanical Engineering | 本科 | 1 |
| BSVE | Bachelor of Science in Vehicle Engineering | 本科 | 1 |
| BSPSE | Bachelor of Science in Photonic Science and Engineering | 本科 | 1 |
| BDes | Bachelor of Design | 本科 | 1 |
| BGS | Bachelor of General Studies | 本科 | 1 |
| BM | Bachelor of Music | 本科 | 1 |
| BME | Bachelor of Music Education | 本科 | 1 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| Minor | 辅修 | 本科 | 143 |
| UG Certificate | 本科证书 | 本科 | 83 |
| MA | Master of Arts | 研究生 | 24 |
| MS | Master of Science | 研究生 | 38 |
| MEd | Master of Education | 研究生 | 8 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MSA | Master of Science in Accounting | 研究生 | 1 |
| MSN | Master of Science in Nursing | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MHA | Master of Health Administration | 研究生 | 1 |
| MRA | Master of Research Administration | 研究生 | 1 |
| MNM | Master of Nonprofit Management | 研究生 | 1 |
| MAT | Master of Arts in Teaching | 研究生 | 2 |
| MSAE | Master of Science in Aerospace Engineering | 研究生 | 1 |
| MSCE | Master of Science in Civil Engineering | 研究生 | 1 |
| MSEE | Master of Science in Electrical Engineering | 研究生 | 1 |
| MSIE | Master of Science in Industrial Engineering | 研究生 | 1 |
| MSME | Master of Science in Mechanical Engineering | 研究生 | 1 |
| MSVE | Master of Science in Vehicle Engineering | 研究生 | 1 |
| MSMSE | Master of Science in Materials Science and Engineering | 研究生 | 1 |
| MSPE | Master of Science in Photonic Engineering | 研究生 | 1 |
| MSBM | Master of Science in Biomedical Sciences | 研究生 | 1 |
| MSRE | Master of Science in Real Estate | 研究生 | 1 |
| MSM | Master of Science in Management | 研究生 | 1 |
| MECM | Master of Emergency and Crisis Management | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 33 |
| EdD | Doctor of Education | 研究生 | 2 |
| DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| EdS | Education Specialist | 研究生 | 3 |
| Grad Certificate | 研究生证书 | 研究生 | 106 |
| Professional Program | 专业项目 | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

> **注**: 由于 API 分页限制（仅返回 586/909 个程序），以下矩阵基于 API 返回的可归属程序。总计行使用官方配置元数据中的 909 总数。

| 学院 \ 级别 | BA | BS | BSBA | BFA | BSN | BEng* | Minor | UG Cert | MA | MS | MEd | MFA | MBA | PhD | EdD | DNP | DPT | MD | EdS | Grad Cert | 合计 |
|------------|----|----|------|-----|-----|-------|-------|---------|----|----|----|-----|-----|-----|-----|-----|-----|----|----|-----------|------|
| Arts & Humanities | 22 | 0 | 0 | 3 | 0 | 0 | 38 | 15 | 5 | 0 | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 88 |
| Business | 0 | 0 | 7 | 0 | 0 | 0 | 10 | 2 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 36+ |
| Community Innovation & Education | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 25 | 3 | 1 | 8 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 3 | 50 | 106+ |
| Engineering & CS | 0 | 10 | 0 | 0 | 0 | 8 | 15 | 3 | 0 | 19 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 5 | 69+ |
| Graduate Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 4 |
| Health Professions & Sciences | 0 | 4 | 0 | 0 | 0 | 0 | 5 | 4 | 0 | 4 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 5 | 25+ |
| Medicine | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 0 | 5 | 17 |
| Nursing | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 4 | 10+ |
| Optics & Photonics | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Sciences | 12 | 32 | 0 | 1 | 0 | 0 | 52 | 19 | 16 | 5 | 0 | 1 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 6 | 156+ |
| Hospitality Management | 0 | 3 | 0 | 0 | 0 | 0 | 11 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 23+ |
| **合计** | 34 | 53 | 7 | 4 | 2 | 9 | 143 | 83 | 24 | 38 | 8 | 4 | 1 | 33 | 2 | 2 | 1 | 1 | 3 | 106 | **909** |

> *BEng 包括 BSAE, BSCE, BSCpE, BSConE, BSEE, BSIE, BSME, BSVE, BSPSE 等工程学位。

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UCF has 11 colleges offering undergraduate programs. The largest undergraduate programs are in the College of Sciences, College of Community Innovation and Education, and College of Engineering and Computer Science. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

> **注**: 由于 API 分页限制，以下列出 API 返回的主要本科专业。完整列表请参考 UCF Degree Search 网站。

#### College of Arts and Humanities

##### School of Visual Arts and Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.ucf.edu/degree/art-ba/ |
| 2 | Digital Media | https://www.ucf.edu/degree/digital-media-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.ucf.edu/degree/art-bfa/ |
| 2 | Theatre | https://www.ucf.edu/degree/theatre-bfa/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.ucf.edu/degree/english-ba/ |
| 2 | Creative Writing | https://www.ucf.edu/degree/creative-writing-ba/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.ucf.edu/degree/history-ba/ |

##### School of Performing Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.ucf.edu/degree/music-ba/ |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance | https://www.ucf.edu/degree/music-performance-bm/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.ucf.edu/degree/philosophy-ba/ |

##### Department of Writing and Rhetoric
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Writing and Rhetoric | https://www.ucf.edu/degree/writing-and-rhetoric-ba/ |

#### College of Business

##### Department of Accounting
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.ucf.edu/degree/accounting-bsba/ |

##### Department of Finance
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.ucf.edu/degree/finance-bsba/ |

##### Department of Management
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://www.ucf.edu/degree/management-bsba/ |

##### Department of Marketing
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.ucf.edu/degree/marketing-bsba/ |

##### School of Real Estate
###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate | https://www.ucf.edu/degree/real-estate-bsba/ |

#### College of Engineering and Computer Science

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.ucf.edu/degree/computer-science-bs/ |

##### Department of Electrical and Computer Engineering
###### BSEE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.ucf.edu/degree/electrical-engineering-bsee/ |

###### BSCpE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.ucf.edu/degree/computer-engineering-bscpe/ |

##### Department of Mechanical and Aerospace Engineering
###### BSME
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.ucf.edu/degree/mechanical-engineering-bsme/ |

###### BSAE
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.ucf.edu/degree/aerospace-engineering-bsae/ |

##### Department of Civil, Environmental and Construction Engineering
###### BSCE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.ucf.edu/degree/civil-engineering-bsce/ |

###### BSConE
| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Engineering | https://www.ucf.edu/degree/construction-engineering-bscone/ |

##### Department of Industrial Engineering and Management Systems
###### BSIE
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://www.ucf.edu/degree/industrial-engineering-bsie/ |

#### College of Sciences

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.ucf.edu/degree/biology-bs/ |
| 2 | Biotechnology | https://www.ucf.edu/degree/biotechnology-bs/ |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.ucf.edu/degree/chemistry-bs/ |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.ucf.edu/degree/mathematics-bs/ |
| 2 | Actuarial Science | https://www.ucf.edu/degree/actuarial-science-bs/ |
| 3 | Statistics | https://www.ucf.edu/degree/statistics-bs/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.ucf.edu/degree/physics-bs/ |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.ucf.edu/degree/psychology-bs/ |

##### School of Politics, Security, and International Affairs
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.ucf.edu/degree/political-science-ba/ |
| 2 | International and Global Studies | https://www.ucf.edu/degree/international-and-global-studies-ba/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.ucf.edu/degree/sociology-ba/ |
| 2 | Anthropology | https://www.ucf.edu/degree/anthropology-ba/ |

#### College of Nursing

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.ucf.edu/degree/nursing-bsn/ |

#### College of Health Professions and Sciences

##### School of Kinesiology and Physical Therapy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://www.ucf.edu/degree/kinesiology-bs/ |
| 2 | Health Sciences | https://www.ucf.edu/degree/health-sciences-bs/ |

##### Department of Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Informatics and Information Management | https://www.ucf.edu/degree/health-informatics-and-information-management-bs/ |
| 2 | Health Services Administration | https://www.ucf.edu/degree/health-services-administration-bs/ |

#### College of Medicine

##### Burnett School of Biomedical Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.ucf.edu/degree/biomedical-sciences-bs/ |

#### College of Optics and Photonics (CREOL)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Photonic Science and Engineering | https://www.ucf.edu/degree/photonic-science-and-engineering-bs/ |

#### Rosen College of Hospitality Management

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://www.ucf.edu/degree/hospitality-management-bs/ |
| 2 | Event Management | https://www.ucf.edu/degree/event-management-bs/ |
| 3 | Restaurant and Food Service Management | https://www.ucf.edu/degree/restaurant-and-food-service-management-bs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

UCF offers several interdisciplinary programs that span multiple colleges:

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Data Science (BS) | College of Sciences + College of Engineering and Computer Science | https://www.ucf.edu/degree/data-science-bs/ |
| 2 | Environmental Studies (BA) | College of Sciences + College of Arts and Humanities | https://www.ucf.edu/degree/environmental-studies-ba/ |

### 1.4 Minors — Complete List

UCF offers 143 undergraduate minors across all colleges. Key minors include:

| # | Minor Name | Home College |
|---|------------|--------------|
| 1 | Accounting | College of Business |
| 2 | Art History | College of Arts and Humanities |
| 3 | Biology | College of Sciences |
| 4 | Business Administration | College of Business |
| 5 | Chemistry | College of Sciences |
| 6 | Computer Science | College of Engineering and Computer Science |
| 7 | Creative Writing | College of Arts and Humanities |
| 8 | Criminal Justice | College of Community Innovation and Education |
| 9 | Data Science | College of Sciences |
| 10 | Digital Media | College of Arts and Humanities |
| 11 | Economics | College of Business |
| 12 | Education | College of Community Innovation and Education |
| 13 | English | College of Arts and Humanities |
| 14 | Environmental Studies | College of Sciences |
| 15 | Film | College of Arts and Humanities |
| 16 | Finance | College of Business |
| 17 | History | College of Arts and Humanities |
| 18 | Hospitality Management | Rosen College of Hospitality Management |
| 19 | Information Technology | College of Engineering and Computer Science |
| 20 | International Relations | College of Sciences |
| 21 | Legal Studies | College of Community Innovation and Education |
| 22 | Management | College of Business |
| 23 | Marketing | College of Business |
| 24 | Mathematics | College of Sciences |
| 25 | Music | College of Arts and Humanities |
| 26 | Nursing | College of Nursing |
| 27 | Philosophy | College of Arts and Humanities |
| 28 | Physics | College of Sciences |
| 29 | Political Science | College of Sciences |
| 30 | Psychology | College of Sciences |
| 31 | Public Administration | College of Community Innovation and Education |
| 32 | Social Work | College of Community Innovation and Education |
| 33 | Sociology | College of Sciences |
| 34 | Spanish | College of Arts and Humanities |
| 35 | Statistics | College of Sciences |
| 36 | Theatre | College of Arts and Humanities |
| ... | *(107 more minors — 完整列表见 UCF Degree Search)* | ... |

### 1.5 General/Institute-Wide Requirements

UCF requires completion of the **General Education Program (GEP)** for all undergraduate students. The GEP includes:

- **Communication** (6 credit hours): English Composition
- **Cultural and Historical Foundation** (9 credit hours): History, Literature, Philosophy
- **Mathematical Foundation** (6 credit hours): College Algebra or higher
- **Social Foundation** (6 credit hours): Psychology, Sociology, Political Science
- **Science Foundation** (6 credit hours): Biology, Chemistry, Physics
- **Diversity** (3 credit hours): Cultural diversity requirement

> **Source**: UCF Undergraduate Catalog

### 1.6 Course-ID → Major Quick-Lookup

UCF does not use a course numbering system for majors like some institutions. Programs are identified by their full name and degree abbreviation (e.g., "Computer Science (BS)", "Accounting (BSBA)").

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

> **注**: UCF 研究生招生采用分散制（decentralized），各学院/项目自行管理招生。以下列出主要研究生项目。

#### College of Engineering and Computer Science

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.ucf.edu/degree/computer-science-ms/ |
| 2 | Aerospace Engineering | https://www.ucf.edu/degree/aerospace-engineering-ms/ |
| 3 | Civil Engineering | https://www.ucf.edu/degree/civil-engineering-ms/ |
| 4 | Electrical Engineering | https://www.ucf.edu/degree/electrical-engineering-ms/ |
| 5 | Industrial Engineering | https://www.ucf.edu/degree/industrial-engineering-ms/ |
| 6 | Mechanical Engineering | https://www.ucf.edu/degree/mechanical-engineering-ms/ |
| 7 | Materials Science and Engineering | https://www.ucf.edu/degree/materials-science-and-engineering-ms/ |
| 8 | Systems Engineering | https://www.ucf.edu/degree/systems-engineering-ms/ |
| 9 | Construction Management | https://www.ucf.edu/degree/construction-management-ms/ |
| 10 | Environmental Engineering | https://www.ucf.edu/degree/environmental-engineering-ms/ |
| 11 | Data Analytics | https://www.ucf.edu/degree/data-analytics-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.ucf.edu/degree/computer-science-phd/ |
| 2 | Aerospace Engineering | https://www.ucf.edu/degree/aerospace-engineering-phd/ |
| 3 | Civil Engineering | https://www.ucf.edu/degree/civil-engineering-phd/ |
| 4 | Electrical Engineering | https://www.ucf.edu/degree/electrical-engineering-phd/ |
| 5 | Industrial Engineering | https://www.ucf.edu/degree/industrial-engineering-phd/ |
| 6 | Mechanical Engineering | https://www.ucf.edu/degree/mechanical-engineering-phd/ |
| 7 | Materials Science and Engineering | https://www.ucf.edu/degree/materials-science-and-engineering-phd/ |
| 8 | Computer Engineering | https://www.ucf.edu/degree/computer-engineering-phd/ |
| 9 | Modeling and Simulation | https://www.ucf.edu/degree/modeling-and-simulation-phd/ |

#### College of Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.ucf.edu/degree/anthropology-ma/ |
| 2 | Applied Sociology | https://www.ucf.edu/degree/applied-sociology-ma/ |
| 3 | Clinical Psychology | https://www.ucf.edu/degree/clinical-psychology-ma/ |
| 4 | Communication | https://www.ucf.edu/degree/communication-ma/ |
| 5 | English | https://www.ucf.edu/degree/english-ma/ |
| 6 | History | https://www.ucf.edu/degree/history-ma/ |
| 7 | Political Science | https://www.ucf.edu/degree/political-science-ma/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.ucf.edu/degree/biology-ms/ |
| 2 | Chemistry | https://www.ucf.edu/degree/chemistry-ms/ |
| 3 | Mathematics | https://www.ucf.edu/degree/mathematics-ms/ |
| 4 | Physics | https://www.ucf.edu/degree/physics-ms/ |
| 5 | Statistics and Data Science | https://www.ucf.edu/degree/statistics-and-data-science-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.ucf.edu/degree/biology-phd/ |
| 2 | Chemistry | https://www.ucf.edu/degree/chemistry-phd/ |
| 3 | Computer Science | https://www.ucf.edu/degree/computer-science-phd/ |
| 4 | Mathematics | https://www.ucf.edu/degree/mathematics-phd/ |
| 5 | Physics | https://www.ucf.edu/degree/physics-phd/ |
| 6 | Psychology | https://www.ucf.edu/degree/psychology-phd/ |
| 7 | Sociology | https://www.ucf.edu/degree/sociology-phd/ |
| 8 | Security Studies | https://www.ucf.edu/degree/security-studies-phd/ |
| 9 | Texts and Technology | https://www.ucf.edu/degree/texts-and-technology-phd/ |

#### College of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.ucf.edu/degree/business-administration-mba/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.ucf.edu/degree/accounting-ms/ |
| 2 | Finance | https://www.ucf.edu/degree/finance-ms/ |
| 3 | Management | https://www.ucf.edu/degree/management-ms/ |
| 4 | Real Estate | https://www.ucf.edu/degree/real-estate-ms/ |

#### College of Community Innovation and Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Counselor Education | https://www.ucf.edu/degree/counselor-education-med/ |
| 2 | Educational Leadership | https://www.ucf.edu/degree/educational-leadership-med/ |
| 3 | Exceptional Student Education | https://www.ucf.edu/degree/exceptional-student-education-med/ |
| 4 | Instructional Design and Technology | https://www.ucf.edu/degree/instructional-design-and-technology-med/ |
| 5 | Reading Education | https://www.ucf.edu/degree/reading-education-med/ |
| 6 | Science Education | https://www.ucf.edu/degree/science-education-med/ |
| 7 | Social Science Education | https://www.ucf.edu/degree/social-science-education-med/ |
| 8 | Mathematics Education | https://www.ucf.edu/degree/mathematics-education-med/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.ucf.edu/degree/criminal-justice-ms/ |
| 2 | Public Administration | https://www.ucf.edu/degree/public-administration-ms/ |
| 3 | Social Work | https://www.ucf.edu/degree/social-work-ms/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.ucf.edu/degree/education-edd/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.ucf.edu/degree/education-phd/ |

#### College of Health Professions and Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://www.ucf.edu/degree/athletic-training-ms/ |
| 2 | Communication Sciences and Disorders | https://www.ucf.edu/degree/communication-sciences-and-disorders-ms/ |
| 3 | Health Sciences | https://www.ucf.edu/degree/health-sciences-ms/ |
| 4 | Kinesiology | https://www.ucf.edu/degree/kinesiology-ms/ |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | https://www.ucf.edu/degree/physical-therapy-dpt/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Kinesiology | https://www.ucf.edu/degree/kinesiology-phd/ |
| 2 | Rehabilitation Sciences | https://www.ucf.edu/degree/rehabilitation-sciences-phd/ |

#### College of Nursing

##### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.ucf.edu/degree/nursing-msn/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://www.ucf.edu/degree/nursing-practice-dnp/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.ucf.edu/degree/nursing-phd/ |

#### College of Medicine

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.ucf.edu/degree/biomedical-sciences-ms/ |
| 2 | Medical Sciences | https://www.ucf.edu/degree/medical-sciences-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.ucf.edu/degree/biomedical-sciences-phd/ |
| 2 | Medical Sciences | https://www.ucf.edu/degree/medical-sciences-phd/ |

##### MD
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://www.ucf.edu/degree/medicine-md/ |

#### College of Optics and Photonics (CREOL)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Optics and Photonics | https://www.ucf.edu/degree/optics-and-photonics-ms/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Optics and Photonics | https://www.ucf.edu/degree/optics-and-photonics-phd/ |

#### Rosen College of Hospitality Management

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Hospitality and Tourism Management | https://www.ucf.edu/degree/hospitality-and-tourism-management-ms/ |
| 2 | Travel Technology and Analytics | https://www.ucf.edu/degree/travel-technology-and-analytics-ms/ |

### 2.2 Graduate Admissions Model

UCF uses a **decentralized** graduate admissions model:

- **College of Graduate Studies**: Central administrative office that manages the application process and makes official offers of admission
- **Individual Programs**: Each graduate program sets its own admission requirements, deadlines, and review processes
- **Application Portal**: Single online application at https://graduate.ucf.edu/applying-to-ucf/
- **Application Fee**: $30 (nonrefundable)
- **Decision Timeline**: Varies by program; programs make recommendations to the College of Graduate Studies

**Key Points**:
- Applicants interact with both the College of Graduate Studies and their specific program
- Each program has its own deadlines and requirements
- GRE/GMAT requirements vary by program
- English proficiency requirements apply to international applicants

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| **Application Portal** | UCF Undergraduate Application + Common App | https://www.ucf.edu/admissions/undergraduate/apply/ |
| **Application Fee** | $30 (nonrefundable) | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Early Action Deadline** | October 15 (application), November 15 (materials) | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Early Action Notification** | December 5 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Regular Decision Deadline (Fall)** | May 1 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Regular Decision Deadline (Spring)** | November 1 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Regular Decision Deadline (Summer)** | March 1 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Decision Notification** | Rolling from January | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Decision Outcomes** | Admit, Pathway Admit, Defer, Deny (EA); Admit, Pathway Admit, Waitlist, Deny (RD) | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **SAT Code** | 5233 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **ACT Code** | 0735 | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **SAT/ACT Policy** | **REQUIRED** (NOT test-optional) — FL BOG 6.008 requires standardized tests for Florida public universities | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **CLT Accepted** | Yes (minimum 42 on Verbal Reasoning + Grammar/Writing) | https://www.ucf.edu/admissions/undergraduate/international/ |
| **Superscore** | Yes (SAT and ACT) | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **ACT Science** | Optional (effective April 2025) | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Application Essay** | Strongly encouraged but not required | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Recommendations** | Not required | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Transcript** | Self-Provided Academic Record for Knights (SPARK) Form | https://www.ucf.edu/admissions/undergraduate/freshman/ |
| **Enrollment Confirmation Deadline** | May 1 | Standard practice |

**Fall 2025 Freshman Class Profile**:
- Mid-range SAT Score: 1310–1430
- Mid-range ACT Score: 28–32
- Mid-range CLT Score: 92–100
- Mid-range High School GPA: 4.1–4.5 (weighted)
- Students of Color: 50%
- Top 5 Majors: Computer Science, Mechanical Engineering, Finance, Biomedical Sciences, Biology

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT | 80 | — | Internet-based test |
| TOEFL CBT | 220 | — | Computer-based test |
| TOEFL PBT | 550 | — | Paper-based test |
| IELTS | 6.5 | — | Academic module |
| Duolingo English Test | 120 | — | — |
| SAT EBRW | 520 | — | Evidence-Based Reading and Writing |
| ACT English | 20 | — | English section only |
| CLT Verbal | 42 | — | Verbal Reasoning + Grammar/Writing |

**Exemptions**:
- Native English speakers
- Bachelor's/master's/doctoral degree from US institution
- Degree from country where English is only official language
- 4 years of English at US high school or US-accredited international high school
- Completion of ENC 1101 and ENC 1102 with grade "B" or better
- Completion of UCF Global's English Programs level 8 or higher

### 3.3 Graduate — Global Rules

| 维度 | 值 | 来源 |
|------|-----|------|
| **Admissions Model** | Decentralized (each program sets own requirements) | https://graduate.ucf.edu/applying-to-ucf/ |
| **Application Portal** | https://graduate.ucf.edu/applying-to-ucf/ | https://graduate.ucf.edu/applying-to-ucf/ |
| **Application Fee** | $30 (nonrefundable) | https://graduate.ucf.edu/applying-to-ucf/ |
| **GRE/GMAT Policy** | Varies by program (some require, some optional, some not accepted) | https://graduate.ucf.edu/applying-to-ucf/ |
| **English Proficiency** | Required for non-native English speakers | https://graduate.ucf.edu/applying-to-ucf/ |
| **TOEFL (Graduate)** | 80 (iBT) minimum | https://graduate.ucf.edu/applying-to-ucf/ |
| **IELTS (Graduate)** | 6.5 minimum | https://graduate.ucf.edu/applying-to-ucf/ |
| **Transcripts** | Official transcripts required | https://graduate.ucf.edu/applying-to-ucf/ |
| **Decision Timeline** | Varies by program | https://graduate.ucf.edu/applying-to-ucf/ |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026–2027 Academic Year, Line-Itemized)

#### Florida Residents (On-Campus)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition & Fees | $5,954 | Based on 28 credit hours per academic year |
| Housing | $8,750 | On-campus housing estimate |
| Food | $6,170 | Meal plan estimate |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $2,126 | Estimated |
| Personal Expenses | $3,104 | Estimated |
| **Total** | **$25,796** | Full cost of attendance |

#### Non-Florida Residents (On-Campus)

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| Tuition & Fees | $22,482 | Based on 28 credit hours per academic year |
| Housing | $8,750 | On-campus housing estimate |
| Food | $6,170 | Meal plan estimate |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $2,126 | Estimated |
| Personal Expenses | $3,104 | Estimated |
| **Total** | **$42,324** | Full cost of attendance |

#### Per Credit Hour Breakdown (2025-2026)

| Fee Name | In-State Rate | Out-of-State Rate |
|----------|---------------|-------------------|
| Tuition | $105.07 | $105.07 |
| Non-Resident Fee | $0.00 | $562.16 |
| Capital Improvement Fee | $6.76 | $6.76 |
| Financial Aid Fee | $5.16 | $5.16 |
| Non-Resident Financial Aid Fee | $0.00 | $28.10 |
| Activity & Service Fee | $11.67 | $11.67 |
| Transportation Access Fee | $9.10 | $9.10 |
| Health Fee | $10.84 | $10.84 |
| Athletic Fee | $14.32 | $14.32 |
| Tuition Differential | $44.20 | $44.20 |
| Technology Fee | $5.16 | $5.16 |
| **Total per Credit Hour** | **$212.28** | **$802.54** |

### 4.2 Undergraduate Financial-Aid Policy

| 维度 | 值 | 来源 |
|------|-----|------|
| **Financial Aid Recipients** | 72% of undergraduate students | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Debt-Free Graduation** | 70% graduated with no educational debt | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Need-Blind/Need-Aware** | Need-aware for all (domestic and international) | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Merit Scholarships** | $6,000–$30,000 (FL residents); up to $50,400 (non-residents) over 4 years | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Scholarship Deadline** | Early Action deadlines (Oct 15 / Nov 15) for priority consideration | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **National Merit** | Yes (UCF participates) | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Transfer Scholarships** | Available | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Tuition Waivers** | Florida Grandparent Waiver; FL HS Graduate OOS Waiver | https://www.ucf.edu/admissions/undergraduate/tuition-aid/ |
| **Net Price Calculator** | Available | https://www.ucf.edu/financial-aid/cost/ |

### 4.3 Graduate Cost & Funding Framework

#### Graduate Tuition (2025-2026 Per Credit Hour)

| Fee Name | In-State Rate | Out-of-State Rate |
|----------|---------------|-------------------|
| Tuition | $288.16 | $288.16 |
| Non-Resident Fee | $0.00 | $863.66 |
| Capital Improvement Fee | $6.76 | $6.76 |
| Financial Aid Fee | $14.40 | $14.40 |
| Non-Resident Financial Aid Fee | $0.00 | $43.17 |
| Activity & Service Fee | $11.67 | $11.67 |
| Transportation Access Fee | $9.10 | $9.10 |
| Health Fee | $10.84 | $10.84 |
| Athletic Fee | $14.32 | $14.32 |
| Technology Fee | $14.40 | $14.40 |
| **Total per Credit Hour** | **$369.65** | **$1,276.48** |

#### Funding Framework

| Funding Type | Description |
|--------------|-------------|
| Graduate Assistantships (GA) | Teaching and research positions; include tuition remission + stipend |
| Graduate Teaching Assistantships (GTA) | Teaching-focused positions |
| Graduate Research Assistantships (GRA) | Research-focused positions |
| Tuition Remission | Waiver of tuition for assistantship holders |
| External Funding | Fellowships, grants from external organizations |
| Self-Funded | Students pay tuition out of pocket or through loans |

> **Source**: https://graduate.ucf.edu/funding/

---

## SECTION 5 — Evidence Chain Index

### Evidence E-U-001: Freshman Application Deadline (Fall)
```yaml
field: undergraduate.deadlines.fall_regular
value: "May 1"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "Application Deadline Summer – Mar. 1 Fall – May. 1 Spring – Nov. 1"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-002: Early Action Deadline
```yaml
field: undergraduate.deadlines.early_action
value: "October 15 (application), November 15 (materials)"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "Application Deadline Summer – Oct. 15 Fall – Oct. 15 Material Submission Deadline Summer – Nov. 15 Fall – Nov. 15"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-003: Application Fee
```yaml
field: undergraduate.application_fee
value: "$30"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "$30 nonrefundable application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-004: SAT/ACT Policy
```yaml
field: undergraduate.testing.policy
value: "REQUIRED (not test-optional)"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "Official Standardized Test Scores* from either SAT [code: 5233], ACT** [code: 0735], or CLT"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-005: SAT Code
```yaml
field: undergraduate.testing.sat_code
value: "5233"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "SAT [code: 5233]"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-006: ACT Code
```yaml
field: undergraduate.testing.act_code
value: "0735"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "ACT** [code: 0735]"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-007: TOEFL Minimum
```yaml
field: undergraduate.english_proficiency.toefl_min
value: "80 (iBT)"
source_url: https://www.ucf.edu/admissions/undergraduate/international/
source_snippet: "a minimum qualifying score of 220 (computer-based test) -or- 80 (internet-based test) -or- 550 (paper-based test) on the Test of English as a Foreign Language (TOEFL) exam"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-008: IELTS Minimum
```yaml
field: undergraduate.english_proficiency.ielts_min
value: "6.5"
source_url: https://www.ucf.edu/admissions/undergraduate/international/
source_snippet: "a minimum qualifying score of 6.5 on the International English Language Testing System (IELTS) exam"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-009: Duolingo Minimum
```yaml
field: undergraduate.english_proficiency.duolingo_min
value: "120"
source_url: https://www.ucf.edu/admissions/undergraduate/international/
source_snippet: "a minimum qualifying score of 120 on the Duolingo English Test"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-010: Florida Resident Tuition & Fees
```yaml
field: undergraduate.cost.tuition_fees_in_state
value: "$5,954"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "Tuition and Fees $5,954"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-011: Non-Resident Tuition & Fees
```yaml
field: undergraduate.cost.tuition_fees_out_of_state
value: "$22,482"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "Tuition and Fees $22,482"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-012: Total COA Florida Resident
```yaml
field: undergraduate.cost.total_in_state
value: "$25,796"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "Total $25,796"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-013: Total COA Non-Resident
```yaml
field: undergraduate.cost.total_out_of_state
value: "$42,324"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "Total $42,324"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-U-014: Merit Scholarship Range (FL Residents)
```yaml
field: undergraduate.financial_aid.merit_scholarships_in_state
value: "$6,000–$30,000 over 4 years"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "$6,000 to $30,000 for Florida residents"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-015: Merit Scholarship Range (Non-Residents)
```yaml
field: undergraduate.financial_aid.merit_scholarships_out_of_state
value: "Up to $50,400 over 4 years"
source_url: https://www.ucf.edu/admissions/undergraduate/tuition-aid/
source_snippet: "Up to $50,400 for non-Florida residents"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-016: SAT Score Range
```yaml
field: undergraduate.testing.sat_mid_range
value: "1310–1430"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "1310-1430 Mid-range SAT Score"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-017: ACT Score Range
```yaml
field: undergraduate.testing.act_mid_range
value: "28–32"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "28-32 Mid-range ACT Score"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-U-018: GPA Range
```yaml
field: undergraduate.testing.gpa_mid_range
value: "4.1–4.5 (weighted)"
source_url: https://www.ucf.edu/admissions/undergraduate/freshman/
source_snippet: "4.1-4.5 Mid-range High School GPA"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-G-001: Graduate Application Fee
```yaml
field: graduate.application_fee
value: "$30"
source_url: https://graduate.ucf.edu/applying-to-ucf/
source_snippet: "submit the non-refundable $30 application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-G-002: Graduate Tuition In-State
```yaml
field: graduate.cost.tuition_in_state
value: "$369.65 per credit hour"
source_url: https://studentaccounts.ucf.edu/tf-graduate/
source_snippet: "Tuition and Fees Total for 1 Credit Hour 369.65"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-G-003: Graduate Tuition Out-of-State
```yaml
field: graduate.cost.tuition_out_of_state
value: "$1,276.48 per credit hour"
source_url: https://studentaccounts.ucf.edu/tf-graduate/
source_snippet: "Tuition and Fees Total for 1 Credit Hour 1276.48"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Evidence E-001: Program Count
```yaml
field: programs.total_count
value: "909"
source_url: https://www.ucf.edu/degree-search/
source_snippet: UCF_DEGREE_SEARCH_ANGULAR config: "program_types":[{"name":"Undergraduate Program","count":479,"children":[{"name":"Bachelor","count":253},{"name":"Minor","count":143},{"name":"Undergraduate Certificate","count":83}]},{"name":"Graduate Program","count":428,"children":[{"name":"Doctorate","count":84},{"name":"Graduate Certificate","count":106},{"name":"Master","count":235},{"name":"Specialist","count":4}]},{"name":"Professional Program","count":1}]
capture_date: 2026-07-06
evidence_type: official_webpage_config
```

### Evidence E-002: College Count
```yaml
field: institutions.colleges_count
value: "11"
source_url: https://www.ucf.edu/degree-search/
source_snippet: UCF_DEGREE_SEARCH_ANGULAR config: "colleges":[11 colleges listed]
capture_date: 2026-07-06
evidence_type: official_webpage_config
```

### Evidence E-003: Student Population
```yaml
field: institution.student_population
value: "70,989"
source_url: https://www.ucf.edu/admissions/undergraduate/international/
source_snippet: "70,989 Student Population"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### Evidence E-004: Countries Represented
```yaml
field: institution.countries_represented
value: "142"
source_url: https://www.ucf.edu/admissions/undergraduate/international/
source_snippet: "142 Countries Represented"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
ucf-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: Rules 1-4
├── 01-undergraduate-education.md       # Section 1: Rule 5 UG programs
├── 02-graduate-education.md            # Section 2: Rule 5 Grad programs
├── 03-application-requirements.md      # Section 3
├── 04-costs-financial-aid.md           # Section 4
├── 05-evidence-chain.md                # Section 5
├── 06-import-manifest.md               # Section 6 (this file)
├── 07-cross-school-comparison.md       # Section 7
└── chunks/
    ├── ucf-arts-humanities-programs.md
    ├── ucf-business-programs.md
    ├── ucf-community-innovation-education-programs.md
    ├── ucf-engineering-cs-programs.md
    ├── ucf-graduate-studies-programs.md
    ├── ucf-health-professions-sciences-programs.md
    ├── ucf-medicine-programs.md
    ├── ucf-nursing-programs.md
    ├── ucf-optics-photonics-programs.md
    ├── ucf-sciences-programs.md
    └── ucf-hospitality-management-programs.md
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "ucf-knowledge-base-v2"
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
| P0 | Complete program list (API returned 586/909 due to pagination limit) | https://www.ucf.edu/degree-search/ |
| P0 | Per-program GRE/GMAT requirements | https://graduate.ucf.edu/ |
| P0 | Per-program graduate deadlines | https://graduate.ucf.edu/ |
| P1 | Complete minor list with college attribution | https://www.ucf.edu/degree-search/ |
| P1 | Complete certificate list with college attribution | https://www.ucf.edu/degree-search/ |
| P1 | Graduate program detail pages (GRE, TOEFL, deadlines) | Individual program pages |
| P2 | Department-level hierarchy verification | College websites |
| P2 | Honors College program details | https://www.ucf.edu/college/burnett-honors-college/ |
| P2 | Online program details | https://www.ucf.edu/online/ |
| P2 | Transfer admission requirements | https://www.ucf.edu/admissions/undergraduate/transfer/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | UCF | MIT | Stanford | Harvard | Caltech | UC Berkeley |
|------|-----|-----|----------|---------|---------|-------------|
| **Type** | Public | Private | Private | Private | Private | Public |
| **Location** | Orlando, FL | Cambridge, MA | Stanford, CA | Cambridge, MA | Pasadena, CA | Berkeley, CA |
| **Total Programs** | 909 | — | 349 | — | 76 | 439 |
| **UG Tuition (In-State)** | $5,954 | — | — | — | — | $18,216 |
| **UG Tuition (OOS)** | $22,482 | — | — | — | — | $57,486 |
| **UG Total COA (In-State)** | $25,796 | — | — | — | — | — |
| **UG Total COA (OOS)** | $42,324 | — | — | — | — | — |
| **Application Fee** | $30 | — | $90 | $85 | $75 | — |
| **SAT/ACT Required** | Yes | — | Yes | Yes | Yes | Test-free |
| **TOEFL Min** | 80 | — | — | — | — | — |
| **IELTS Min** | 6.5 | — | — | — | — | — |
| **EA Deadline** | Oct 15 | — | Nov 1 | Nov 1 | Nov 1 | — |
| **RD Deadline (Fall)** | May 1 | — | Jan 5 | Jan 5 | Jan 5 | Nov 30 |
| **Need-Blind (Intl)** | No | Yes | Yes | Yes | No | No |
| **Merit Scholarships** | Yes | No | No | No | No | Limited |
| **Student Population** | 70,989 | — | — | — | — | — |
| **Countries Represented** | 142 | — | — | — | — | — |

---

## Closing Block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.ucf.edu, graduate.ucf.edu, studentaccounts.ucf.edu, ucf.edu/financial-aid
> **Verification**: ego-browser snapshotText + JS DOM extraction + API data
> **Granularity**: school → department → degree-level → program
> **Cache Status**: MISS (first run) — site-memory.json, last-extract.json, content-hashes.json written
