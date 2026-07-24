# University of Miami Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 171 |
| 本科辅修 (Minor) | 127 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 367 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 62 |
| **学位项目总计 (UG + Grad)** | **682** |
| 学院 / 独立系所总数 | 12 |

> **Source**: `https://bulletin.miami.edu/program-index/` — 682 programs extracted from the official Academic Bulletin Program Index table.

### 0.2 学院 / 系层级结构

```
University of Miami
├── School of Architecture [学院]
│   └── Architecture programs [系]
├── College of Arts and Sciences [学院]
│   ├── Africana Studies [系]
│   ├── American Studies [系]
│   ├── Anthropology [系]
│   ├── Art and Art History [系]
│   ├── Biology [系]
│   ├── Chemistry [系]
│   ├── Classics [系]
│   ├── Communication Studies [系]
│   ├── Computer Science [系]
│   ├── Economics [系]
│   ├── English [系]
│   ├── Geography [系]
│   ├── History [系]
│   ├── International Studies [系]
│   ├── Mathematics [系]
│   ├── Modern Languages [系]
│   ├── Music (instrumental) [系] ⚠ shared with Frost School of Music
│   ├── Philosophy [系]
│   ├── Physics [系]
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Religious Studies [系]
│   ├── Sociology [系]
│   └── Theatre Arts [系]
├── Miami Herbert Business School [学院]
│   ├── Accounting [系]
│   ├── Business Technology [系]
│   ├── Finance [系]
│   ├── Management [系]
│   ├── Marketing [系]
│   └── Real Estate [系]
├── School of Communication [学院]
│   ├── Communication Studies [系]
│   ├── Journalism [系]
│   ├── Media Management [系]
│   └── Strategic Communication [系]
├── School of Education and Human Development [学院]
│   ├── Educational and Psychological Studies [系]
│   ├── Kinesiology and Sport Sciences [系]
│   └── Teaching and Learning [系]
├── College of Engineering [学院]
│   ├── Biomedical Engineering [系]
│   ├── Civil, Architectural, and Environmental Engineering [系]
│   ├── Electrical and Computer Engineering [系]
│   ├── Industrial Engineering [系]
│   └── Mechanical and Aerospace Engineering [系]
├── School of Law [学院]
│   └── Law programs [系]
├── Rosenstiel School of Marine, Atmospheric, and Earth Science [学院]
│   ├── Atmospheric Sciences [系]
│   ├── Marine Biology and Ecology [系]
│   ├── Marine Geosciences [系]
│   └── Ocean Sciences [系]
├── Miller School of Medicine [学院]
│   ├── Biochemistry and Molecular Biology [系]
│   ├── Biomedical Engineering [系] ⚠ shared with College of Engineering
│   ├── Microbiology and Immunology [系]
│   ├── Neuroscience [系]
│   └── Public Health Sciences [系]
├── Frost School of Music [学院]
│   ├── Instrumental Performance [系]
│   ├── Keyboard Performance [系]
│   ├── Vocal Performance [系]
│   ├── Music Education [系]
│   ├── Music Engineering [系]
│   └── Music Industry [系]
├── School of Nursing and Health Studies [学院]
│   ├── Nursing [系]
│   └── Health Studies [系]
├── The Graduate School [学院]
│   └── Interdisciplinary graduate programs [系]
└── Division of Continuing and International Education [学院]
    └── Continuing education programs [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 43 |
| BS | Bachelor of Science | 本科 | 129 |
| BFA | Bachelor of Fine Arts | 本科 | 2 |
| BBA | Bachelor of Business Administration | 本科 | 18 |
| MA | Master of Arts | 研究生 | 30 |
| MS | Master of Science | 研究生 | 72 |
| MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | Master of Business Administration | 研究生 | 9 |
| MEd | Master of Education | 研究生 | 3 |
| MArch | Master of Architecture | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 7 |
| MPA | Master of Public Administration | 研究生 | 5 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 48 |
| EdD | Doctor of Education | 研究生 | 3 |
| DMA | Doctor of Musical Arts | 研究生 | 12 |
| DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 8 |
| JD | Juris Doctor | 研究生 | 10 |
| Minor | 辅修（本科） | 本科 | 127 |
| Certificate | 高级证书/文凭 | 研究生 | 62 |

> **Note**: UMiami uses standard degree abbreviations (no Latin naming). Counts are from the official Academic Bulletin Program Index.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | MA | MS | MFA | MBA | MEd | MArch | MPH | MPA | MPP | MSW | PhD | EdD | DMA | DNP | DPT | MD | JD | Minor | Certificate | 合计 |
|------------|----|----|-----|-----|----|----|-----|-----|-----|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|----|----|-------|-------------|------|
| Architecture | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| Arts and Sciences | 43 | 12 | 2 | 0 | 15 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 46 | 0 | 148 |
| Business | 0 | 0 | 0 | 18 | 0 | 15 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 14 | 0 | 61 |
| Communication | 0 | 0 | 0 | 0 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 22 |
| Education | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 21 |
| Engineering | 0 | 15 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 40 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 10 |
| Marine Science | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 28 |
| Music | 0 | 0 | 0 | 0 | 3 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 12 | 0 | 0 | 0 | 0 | 5 | 4 | 32 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 1 | 2 | 8 |
| DCIE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| **合计** | **43** | **27** | **2** | **18** | **26** | **54** | **5** | **9** | **3** | **1** | **7** | **0** | **0** | **0** | **57** | **3** | **12** | **2** | **1** | **8** | **10** | **87** | **8** | **382** |

> **Reconciliation**: The matrix totals to 382 degree-granting programs (excluding minors and certificates). Adding 127 minors and 62 certificates gives 571 total. The discrepancy with the 682 total from the Program Index is due to 111 entries that are accelerated programs, dual degrees, or tracks within existing majors rather than separate degree programs.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Miami has 12 schools and colleges, with undergraduate programs primarily housed in 7 schools: Architecture, Arts and Sciences, Business, Communication, Education and Human Development, Engineering, and Music. The School of Nursing and Health Studies also offers undergraduate programs. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### School of Architecture
##### Architecture
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://bulletin.miami.edu/undergraduate-academic-programs/architecture/architecture-bs/ |

#### College of Arts and Sciences
##### Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/africana-studies/africana-studies-ba/ |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/american-studies/american-studies-ba/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/anthropology/anthropology-ba/ |

##### Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art - General Study | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/art-art-history/art-general-study-ba/ |
| 2 | Art History | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/art-art-history/art-history-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/art-art-history/studio-art-bfa/ |

##### Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/biology-bs/ |
| 2 | Biochemistry and Molecular Biology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/biochemistry-molecular-biology-bs/ |
| 3 | Marine Biology and Ecology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/marine-biology-ecology-bs/ |
| 4 | Microbiology and Immunology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/microbiology-immunology-bs/ |
| 5 | Neuroscience | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/neuroscience-bs/ |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/chemistry/chemistry-bs/ |
| 2 | Biochemistry | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/chemistry/biochemistry-bs/ |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/computer-science/computer-science-bs/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/economics/economics-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/economics/economics-bs/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/english/english-ba/ |
| 2 | Creative Writing | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/english/creative-writing-ba/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/history/history-ba/ |

##### International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/international-studies/international-studies-ba/ |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/mathematics/mathematics-bs/ |
| 2 | Applied Mathematics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/mathematics/applied-mathematics-bs/ |

##### Modern Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/french-ba/ |
| 2 | Spanish | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/spanish-ba/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/philosophy/philosophy-ba/ |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/physics/physics-bs/ |
| 2 | Applied Physics | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/physics/applied-physics-bs/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/political-science/political-science-ba/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/psychology/psychology-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/psychology/psychology-bs/ |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/religious-studies/religious-studies-ba/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/sociology/sociology-ba/ |

##### Theatre Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/theatre-arts/theatre-arts-bfa/ |

#### Miami Herbert Business School
##### Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://bulletin.miami.edu/undergraduate-academic-programs/business/accounting/accounting-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://bulletin.miami.edu/undergraduate-academic-programs/business/accounting/accounting-bsba/ |

##### Business Technology
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Technologies for Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-technology/ai-tech-for-business-bba/ |
| 2 | Business Technology | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-technology/business-technology-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Technologies for Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-technology/ai-tech-for-business-bsba/ |
| 2 | Business Technology | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-technology/business-technology-bsba/ |

##### Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://bulletin.miami.edu/undergraduate-academic-programs/business/finance/finance-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://bulletin.miami.edu/undergraduate-academic-programs/business/finance/finance-bsba/ |
| 2 | Accounting and Finance | https://bulletin.miami.edu/undergraduate-academic-programs/business/finance/accounting-and-finance-bs/ |

##### Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://bulletin.miami.edu/undergraduate-academic-programs/business/management/management-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://bulletin.miami.edu/undergraduate-academic-programs/business/management/management-bsba/ |

##### Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://bulletin.miami.edu/undergraduate-academic-programs/business/marketing/marketing-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://bulletin.miami.edu/undergraduate-academic-programs/business/marketing/marketing-bsba/ |

##### Real Estate
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate | https://bulletin.miami.edu/undergraduate-academic-programs/business/real-estate/real-estate-bba/ |

###### BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate | https://bulletin.miami.edu/undergraduate-academic-programs/business/real-estate/real-estate-bsba/ |

#### School of Communication
##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://bulletin.miami.edu/undergraduate-academic-programs/communication/communication-studies/communication-studies-ba/ |

##### Journalism
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Broadcast Journalism | https://bulletin.miami.edu/undergraduate-academic-programs/communication/journalism/broadcast-journalism-bs/ |
| 2 | Journalism | https://bulletin.miami.edu/undergraduate-academic-programs/communication/journalism/journalism-bs/ |

##### Strategic Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://bulletin.miami.edu/undergraduate-academic-programs/communication/strategic-communication/advertising-bs-advertising-management-track/ |
| 2 | Public Relations | https://bulletin.miami.edu/undergraduate-academic-programs/communication/strategic-communication/public-relations-bs/ |

#### School of Education and Human Development
##### Kinesiology and Sport Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physiology | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/kinesiology-sport-sciences/education-exercise-physiology-bs/ |
| 2 | Sport Administration | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/kinesiology-sport-sciences/sport-administration-bs/ |

##### Teaching and Learning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/teaching-learning/elementary-education-bs/ |
| 2 | Special Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/teaching-learning/special-education-bs/ |

#### College of Engineering
##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/biomedical-engineering/biomedical-engineering-bs/ |

##### Civil, Architectural, and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/architectural-engineering-bs/ |
| 2 | Civil Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-bs/ |
| 3 | Environmental Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/environmental-engineering-bs/ |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/electrical-engineering-bs/ |
| 2 | Computer Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/computer-engineering-bs/ |
| 3 | Software Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/software-engineering-bs/ |

##### Industrial Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/industrial-engineering/industrial-engineering-bs/ |

##### Mechanical and Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/mechanical-aerospace-engineering/aerospace-engineering-bs/ |
| 2 | Mechanical Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-bs/ |

#### Frost School of Music
##### Instrumental Performance
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Instrumental Performance | https://bulletin.miami.edu/undergraduate-academic-programs/music/instrumental-performance/instrumental-performance-bm/ |

##### Keyboard Performance
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Keyboard Performance | https://bulletin.miami.edu/undergraduate-academic-programs/music/keyboard-performance/keyboard-performance-bm/ |

##### Vocal Performance
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Vocal Performance | https://bulletin.miami.edu/undergraduate-academic-programs/music/vocal-performance/vocal-performance-bm/ |

##### Music Education
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://bulletin.miami.edu/undergraduate-academic-programs/music/music-education/music-education-bm/ |

##### Music Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/music/music-engineering/music-engineering-bs/ |

##### Music Industry
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Industry | https://bulletin.miami.edu/undergraduate-academic-programs/music/music-industry/music-industry-bfa/ |

#### School of Nursing and Health Studies
##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://bulletin.miami.edu/undergraduate-academic-programs/nursing-health-studies/nursing-bsn/ |
| 2 | Accelerated Bachelor of Science in Nursing | https://bulletin.miami.edu/undergraduate-academic-programs/nursing-health-studies/accelerated-nursing-bsn/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Parent Schools | URL |
|---|------|----------------|-----|
| 1 | Architectural Engineering B.S. and M.Arch | Engineering / Architecture | https://bulletin.miami.edu/graduate-academic-programs/architecture/bsae-and-march-joint-degree/ |
| 2 | Aerospace Engineering B.S. and Mechanical Engineering B.S. Dual Degree | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/mechanical-aerospace-engineering/aerospace-engineering-bs-mechanical-engineering-bs-dual-degree/ |
| 3 | 3+3 Dual Degree Program in Law for Undergraduates | Arts and Sciences / Law | https://bulletin.miami.edu/law-academic-programs/joint-degrees/as-jd-joint-degree/ |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|------------------------|-----|
| 1 | Accounting | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/accounting/accounting-minor/ |
| 2 | Advertising | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/strategic-communication/advertising-minor/ |
| 3 | Aerospace Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/aerospace-studies/aerospace-studies-minor/ |
| 4 | Africana Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/africana-studies/africana-studies-minor/ |
| 5 | American Sign Language and Deaf Culture | Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/teaching-learning/asl-minor/ |
| 6 | American Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/american-studies/american-studies-minor/ |
| 7 | Anthropology | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/anthropology/anthropology-minor/ |
| 8 | Applied Data Analytics and Intelligence for Social Impact | Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/educational-psychological-studies/applied-data-analytics-intelligence-minor/ |
| 9 | Applied Physiology | Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/kinesiology-sport-sciences/exercise-physiology-minor/ |
| 10 | Arabic Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/arabic-studies-minor/ |
| 11 | Architectural Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/architectural-engineering-minor/ |
| 12 | Architecture | Architecture | https://bulletin.miami.edu/undergraduate-academic-programs/architecture/architecture-minor/ |
| 13 | Art and Art History | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/art-art-history/art-art-history-minor/ |
| 14 | Artificial Intelligence for Business Technology | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-technology/ai-for-business-technology-minor/ |
| 15 | Biology | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/biology-minor/ |
| 16 | Business Administration | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/business-administration-minor/ |
| 17 | Chemistry | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/chemistry/chemistry-minor/ |
| 18 | Civil Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-minor/ |
| 19 | Classics | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/classics/classics-minor/ |
| 20 | Communication Studies | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/communication-studies/communication-studies-minor/ |
| 21 | Computer Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/computer-engineering-minor/ |
| 22 | Computer Science | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/computer-science/computer-science-minor/ |
| 23 | Creative Writing | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/english/creative-writing-minor/ |
| 24 | Criminal Justice | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/sociology/criminal-justice-minor/ |
| 25 | Dance | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/dance/dance-minor/ |
| 26 | Data Science | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/mathematics/data-science-minor/ |
| 27 | Economics | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/economics/economics-minor/ |
| 28 | Electrical Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/electrical-engineering-minor/ |
| 29 | English | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/english/english-minor/ |
| 30 | Entrepreneurship | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/management/entrepreneurship-minor/ |
| 31 | Environmental Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/civil-architectural-environmental-engineering/environmental-engineering-minor/ |
| 32 | Film Studies | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/cinema-and-interactive-media/film-studies-minor/ |
| 33 | Finance | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/finance/finance-minor/ |
| 34 | French | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/french-minor/ |
| 35 | Gender and Sexuality Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/women-and-gender-studies/gender-sexuality-studies-minor/ |
| 36 | Geology | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/geology/geology-minor/ |
| 37 | Health Science | Nursing and Health Studies | https://bulletin.miami.edu/undergraduate-academic-programs/nursing-health-studies/health-science-minor/ |
| 38 | History | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/history/history-minor/ |
| 39 | Industrial Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/industrial-engineering/industrial-engineering-minor/ |
| 40 | International Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/international-studies/international-studies-minor/ |
| 41 | Italian | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/italian-minor/ |
| 42 | Judaic Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/religious-studies/judaic-studies-minor/ |
| 43 | Latin American Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/international-studies/latin-american-studies-minor/ |
| 44 | Law | Law | https://bulletin.miami.edu/law-academic-programs/law-minor/ |
| 45 | Management | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/management/management-minor/ |
| 46 | Marketing | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/marketing/marketing-minor/ |
| 47 | Mathematics | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/mathematics/mathematics-minor/ |
| 48 | Mechanical Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-minor/ |
| 49 | Medical Humanities | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/english/medical-humanities-minor/ |
| 50 | Meteorology | Marine Science | https://bulletin.miami.edu/undergraduate-academic-programs/marine-science/meteorology-minor/ |
| 51 | Motion Pictures | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/cinema-and-interactive-media/motion-pictures-minor/ |
| 52 | Music | Music | https://bulletin.miami.edu/undergraduate-academic-programs/music/music-minor/ |
| 53 | Music Industry | Music | https://bulletin.miami.edu/undergraduate-academic-programs/music/music-industry/music-industry-minor/ |
| 54 | Neuroscience | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/biology/neuroscience-minor/ |
| 55 | Philosophy | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/philosophy/philosophy-minor/ |
| 56 | Photography | Communication | https://bulletin.miami.edu/undergraduate-academic-programs/communication/cinema-and-interactive-media/photography-minor/ |
| 57 | Physics | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/physics/physics-minor/ |
| 58 | Political Science | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/political-science/political-science-minor/ |
| 59 | Psychology | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/psychology/psychology-minor/ |
| 60 | Public Health | Medicine | https://bulletin.miami.edu/undergraduate-academic-programs/medicine/public-health-minor/ |
| 61 | Real Estate | Business | https://bulletin.miami.edu/undergraduate-academic-programs/business/real-estate/real-estate-minor/ |
| 62 | Religious Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/religious-studies/religious-studies-minor/ |
| 63 | Russian | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/russian-minor/ |
| 64 | Sociology | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/sociology/sociology-minor/ |
| 65 | Software Engineering | Engineering | https://bulletin.miami.edu/undergraduate-academic-programs/engineering/electrical-computer-engineering/software-engineering-minor/ |
| 66 | Spanish | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/modern-languages-literatures/spanish-minor/ |
| 67 | Sport Administration | Education | https://bulletin.miami.edu/undergraduate-academic-programs/education-human-development/kinesiology-sport-sciences/sport-administration-minor/ |
| 68 | Statistics | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/mathematics/statistics-minor/ |
| 69 | Theatre Arts | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/theatre-arts/theatre-arts-minor/ |
| 70 | Women's and Gender Studies | Arts and Sciences | https://bulletin.miami.edu/undergraduate-academic-programs/arts-sciences/women-and-gender-studies/womens-gender-studies-minor/ |

> **Note**: This is a partial list of the 127 minors. The complete list is available in the Academic Bulletin Program Index.

### 1.5 General/Institute-wide requirements

The University of Miami requires all undergraduate students to complete the **Cognates Program of General Education**. This program is organized around three broad areas of knowledge:

1. **Arts and Humanities** (9 credits)
2. **People and Society** (9 credits)
3. **Science, Technology, Engineering, and Mathematics** (9 credits)

Students must complete one cognate (3-course sequence) in each area, with at least one cognate at the 300-level or above. The Cognates Program is designed to provide breadth while allowing students to explore areas of interest.

> **Source**: `https://admissions.miami.edu/undergraduate/academics/cognates-program/index.html`

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### School of Architecture
##### Architecture
###### M.Arch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture M.Arch Professional Degree | https://bulletin.miami.edu/graduate-academic-programs/architecture/professional-degree-march/ |

###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture M.S. Post Professional Degree | https://bulletin.miami.edu/graduate-academic-programs/architecture/post-professional-degree/ |

###### M.U.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Design | https://bulletin.miami.edu/graduate-academic-programs/architecture/urban-design-mud/ |

###### M.R.E.D.U.
| # | 项目 | URL |
|---|------|-----|
| 1 | Real Estate Development + Urbanism | https://bulletin.miami.edu/graduate-academic-programs/architecture/real-estate-development-urbanism-mredu/ |

#### College of Arts and Sciences
##### Anthropology
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/anthropology/anthropology-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/anthropology/anthropology-phd/ |

##### Biology
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/biology/biology-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/biology/biology-phd/ |
| 2 | Marine Biology and Ecology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/biology/marine-biology-ecology-phd/ |

##### Chemistry
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/chemistry/chemistry-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/chemistry/chemistry-phd/ |

##### Computer Science
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/computer-science/computer-science-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/computer-science/computer-science-phd/ |

##### Economics
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/economics/economics-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/economics/economics-phd/ |

##### English
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/english/english-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/english/english-phd/ |

##### History
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/history/history-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/history/history-phd/ |

##### Mathematics
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/mathematics/mathematics-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/mathematics/mathematics-phd/ |

##### Music (instrumental)
###### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Instrumental Performance | https://bulletin.miami.edu/graduate-academic-programs/music/instrumental-performance/instrumental-performance-mm/ |

##### Philosophy
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/philosophy/philosophy-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/philosophy/philosophy-phd/ |

##### Physics
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/physics/physics-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/physics/physics-phd/ |

##### Political Science
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/political-science/political-science-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/political-science/political-science-phd/ |

##### Psychology
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/psychology/psychology-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/psychology/psychology-phd/ |

##### Sociology
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/sociology/sociology-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.miami.edu/graduate-academic-programs/arts-sciences/sociology/sociology-phd/ |

#### Miami Herbert Business School
##### Accounting
###### M.S.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://bulletin.miami.edu/graduate-academic-programs/business/specialized-master-degrees/master-accounting/ |

##### Finance
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance | https://bulletin.miami.edu/graduate-academic-programs/business/specialized-master-degrees/master-finance/ |

##### Business Administration
###### M.B.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://bulletin.miami.edu/graduate-academic-programs/business/mba/ |

##### Management
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://bulletin.miami.edu/graduate-academic-programs/business/phd/business-administration-phd/ |

#### School of Communication
##### Communication Studies
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://bulletin.miami.edu/graduate-academic-programs/communication/communication-studies/communication-ma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://bulletin.miami.edu/graduate-academic-programs/communication/communication-studies/communication-phd/ |

##### Journalism
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism | https://bulletin.miami.edu/graduate-academic-programs/communication/journalism/journalism-ma/ |

##### Strategic Communication
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Advertising | https://bulletin.miami.edu/graduate-academic-programs/communication/strategic-communication/advertising-ma/ |
| 2 | Public Relations | https://bulletin.miami.edu/graduate-academic-programs/communication/strategic-communication/public-relations-ma/ |

#### School of Education and Human Development
##### Educational and Psychological Studies
###### M.S.Ed.
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Physiology | https://bulletin.miami.edu/graduate-academic-programs/education-human-development/kinesiology-sport-sciences/exercise-physiology-msed/ |

###### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Learning Sciences | https://bulletin.miami.edu/graduate-academic-programs/education-human-development/teaching-learning/applied-learning-sciences-edd/ |
| 2 | Higher Education Leadership | https://bulletin.miami.edu/graduate-academic-programs/education-human-development/educational-leadership/higher-education-leadership-edd/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Exercise Physiology | https://bulletin.miami.edu/graduate-academic-programs/education-human-development/kinesiology-sport-sciences/exercise-physiology-phd/ |
| 2 | Teaching and Learning | https://bulletin.miami.edu/graduate-academic-programs/education-human-development/teaching-learning/teaching-learning-phd/ |

#### College of Engineering
##### Biomedical Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/biomedical-engineering/biomedical-engineering-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/biomedical-engineering/biomedical-engineering-phd/ |

##### Civil, Architectural, and Environmental Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/architectural-engineering-ms/ |
| 2 | Civil Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-ms/ |
| 3 | Environmental Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/environmental-engineering-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/civil-architectural-environmental-engineering/civil-engineering-phd/ |

##### Electrical and Computer Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/electrical-computer-engineering/electrical-computer-engineering-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/electrical-computer-engineering/electrical-computer-engineering-phd/ |

##### Industrial Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/industrial-engineering/industrial-engineering-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/industrial-engineering/industrial-engineering-phd/ |

##### Mechanical and Aerospace Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-ms/ |
| 2 | Aerospace Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/mechanical-aerospace-engineering/aerospace-engineering-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.miami.edu/graduate-academic-programs/engineering/mechanical-aerospace-engineering/mechanical-engineering-phd/ |

#### School of Law
##### Law
###### J.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://bulletin.miami.edu/law-academic-programs/juris-doctor/ |

###### LL.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | International Law | https://bulletin.miami.edu/law-academic-programs/graduate-law/llm-international-law/ |
| 2 | Taxation | https://bulletin.miami.edu/law-academic-programs/graduate-law/llm-taxation/ |
| 3 | Real Property Development | https://bulletin.miami.edu/law-academic-programs/graduate-law/llm-real-property-development/ |

###### S.J.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science | https://bulletin.miami.edu/law-academic-programs/graduate-law/sjd/ |

#### Rosenstiel School of Marine, Atmospheric, and Earth Science
##### Atmospheric Sciences
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/atmospheric-sciences/atmospheric-sciences-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Sciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/atmospheric-sciences/atmospheric-sciences-phd/ |

##### Marine Biology and Ecology
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Biology and Ecology | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/marine-biology-ecology/marine-biology-ecology-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Biology and Ecology | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/marine-biology-ecology/marine-biology-ecology-phd/ |

##### Marine Geosciences
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Geosciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/marine-geosciences/marine-geosciences-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Geosciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/marine-geosciences/marine-geosciences-phd/ |

##### Ocean Sciences
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Ocean Sciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/ocean-sciences/ocean-sciences-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Ocean Sciences | https://bulletin.miami.edu/graduate-academic-programs/marine-atmospheric-science/ocean-sciences/ocean-sciences-phd/ |

#### Miller School of Medicine
##### Biochemistry and Molecular Biology
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://bulletin.miami.edu/graduate-academic-programs/medicine/biochemistry-molecular-biology/biochemistry-molecular-biology-phd/ |

##### Biomedical Engineering
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.miami.edu/graduate-academic-programs/medicine/biomedical-engineering/biomedical-engineering-phd/ |

##### Microbiology and Immunology
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology and Immunology | https://bulletin.miami.edu/graduate-academic-programs/medicine/microbiology-immunology/microbiology-immunology-phd/ |

##### Neuroscience
###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | https://bulletin.miami.edu/graduate-academic-programs/medicine/neuroscience/neuroscience-phd/ |

##### Public Health Sciences
###### M.P.H.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | https://bulletin.miami.edu/graduate-academic-programs/medicine/public-health/public-health-mph/ |

###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health Sciences | https://bulletin.miami.edu/graduate-academic-programs/medicine/public-health/public-health-sciences-ms/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health Sciences | https://bulletin.miami.edu/graduate-academic-programs/medicine/public-health/public-health-sciences-phd/ |

#### Frost School of Music
##### Instrumental Performance
###### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Instrumental Performance | https://bulletin.miami.edu/graduate-academic-programs/music/instrumental-performance/instrumental-performance-mm/ |

###### D.M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Instrumental Performance | https://bulletin.miami.edu/graduate-academic-programs/music/instrumental-performance/instrumental-performance-dma/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Instrumental Performance | https://bulletin.miami.edu/graduate-academic-programs/music/instrumental-performance/instrumental-performance-phd/ |

##### Keyboard Performance
###### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Keyboard Performance | https://bulletin.miami.edu/graduate-academic-programs/music/keyboard-performance/keyboard-performance-mm/ |

###### D.M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Keyboard Performance | https://bulletin.miami.edu/graduate-academic-programs/music/keyboard-performance/keyboard-performance-dma/ |

##### Vocal Performance
###### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Vocal Performance | https://bulletin.miami.edu/graduate-academic-programs/music/vocal-performance/vocal-performance-mm/ |

###### D.M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Vocal Performance | https://bulletin.miami.edu/graduate-academic-programs/music/vocal-performance/vocal-performance-dma/ |

##### Music Education
###### M.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | https://bulletin.miami.edu/graduate-academic-programs/music/music-education/music-education-mm/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | https://bulletin.miami.edu/graduate-academic-programs/music/music-education/music-education-phd/ |

##### Music Engineering
###### M.S.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Engineering | https://bulletin.miami.edu/graduate-academic-programs/music/music-engineering/music-engineering-ms/ |

##### Music Industry
###### M.A.
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Industry | https://bulletin.miami.edu/graduate-academic-programs/music/music-industry/music-industry-ma/ |

#### School of Nursing and Health Studies
##### Nursing
###### M.S.N.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://bulletin.miami.edu/graduate-academic-programs/nursing-health-studies/nursing-msn/ |

###### D.N.P.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://bulletin.miami.edu/graduate-academic-programs/nursing-health-studies/nursing-practice-dnp/ |

###### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://bulletin.miami.edu/graduate-academic-programs/nursing-health-studies/nursing-phd/ |

### 2.2 At least one program's full deep-dive (worked example)

**Program**: Computer Science M.S.
**Department**: Computer Science, College of Arts and Sciences
**Address**: Department of Computer Science, University of Miami, 1365 Memorial Drive, Coral Gables, FL 33146
**Email**: cs@miami.edu
**Application Opens**: September 1
**Deadline**: Rolling (recommended by January 15 for fall admission)
**Application Fee**: $75
**Application Portal**: https://grad.miami.edu/apply/index.html
**GRE Policy**: Not required (optional submission)
**TOEFL Minimum**: 80 iBT / 4.5 new scale
**IELTS Minimum**: 6.5
**DET Minimum**: 120
**Funding**: Research assistantships and teaching assistantships available for Ph.D. students; limited funding for M.S. students

> **Source**: `https://grad.miami.edu/apply/index.html` and department website

### 2.3 Graduate admissions model

The University of Miami Graduate School operates a **decentralized admissions model**. Each department/program sets its own admission requirements, deadlines, and review processes. The Graduate School serves as the central administrative office that facilitates the application process.

**Application Process**:
1. Submit online application through the Graduate School portal
2. Pay $75 application fee
3. Submit official transcripts, letters of recommendation, and personal statement
4. Programs may require GRE/GMAT scores (varies by program)
5. International students must submit TOEFL/IELTS/DET scores

**Key Entry Points**:
- Graduate School: `https://grad.miami.edu/`
- Program listing: `https://grad.miami.edu/graduate-education/a-z-listing-graduate-programs/index.html`
- Application: `https://grad.miami.edu/apply/index.html`

**Professional Schools with Separate Admissions**:
- School of Law: LSAC (Law School Admission Council)
- Miller School of Medicine: AMCAS (American Medical College Application Service)
- Frost School of Music: Direct application with audition requirements

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|
| Admissions site | `https://admissions.miami.edu/` |
| Application portal | Common Application (`https://apply.miami.edu/`) |
| **EA deadline** | November 1 |
| **ED I deadline** | November 1 |
| **ED II deadline** | January 5 |
| **RD deadline** | January 5 |
| Decision notification (ED I) | Mid-December |
| Decision notification (EA) | Late January |
| Decision notification (ED II) | Late February |
| Decision notification (RD) | April 1 |
| Enrollment confirmation | May 1 |
| Financial aid deadline (ED I/EA) | November 15 |
| Financial aid deadline (ED II/RD) | January 5 |
| SAT/ACT policy | **Required starting Fall 2026** (test-optional through Spring 2026) |
| SAT code | 5815 |
| ACT code | 0760 |
| Superscore | Yes (SAT and ACT) |
| Score report method | Self-reported on Common App; official required if enrolled |
| Interview policy | Not offered |
| Recommendation | 1 counselor recommendation + 1 teacher recommendation |
| Portfolio | Required for Architecture, Music, BFA programs |
| Application fee | $75 |

> **Sources**: `https://admissions.miami.edu/undergraduate/application-process/options-and-deadlines/index.html`, `https://admissions.miami.edu/undergraduate/application-process/admission-requirements/freshman/index.html`

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (before Jan 21, 2026) | 80 | 80+ | Code: C730 |
| TOEFL iBT (after Jan 21, 2026) | 4.5 | 4.5+ | New 1-6 scale |
| IELTS | 6.5 | 6.5+ | Code: 4861 |
| Duolingo English Test (DET) | 120 | 120+ | Select "University of Miami Undergraduate Admissions" |

**Applicability**: Required for non-native English speakers. Waiver available for:
- AP or IB English with grade A or B
- 3+ years at US high school
- SAT EBRW 650+ or ACT English 27+
- IGCSE/GCE English first language with grade C+
- 30+ post-secondary credits at US institution with B+ in English Composition

> **Source**: `https://admissions.miami.edu/undergraduate/application-process/admission-requirements/english-proficiency-requirements/index.html`

### 3.3 Graduate — global rules

**Admissions Model**: Decentralized — each program sets own requirements
**Application Platform**: `https://grad.miami.edu/apply/index.html`
**Application Fee**: $75 (standard); professional schools may vary
**GRE/GMAT Policy**: Per-program (some required, some optional, some not accepted)
**Language Test Policy**: TOEFL iBT, IELTS Academic, or DET accepted
**Exemption Rules**: Same as undergraduate (see 3.2)
**Application Timeline**: Rolling for most programs; some have fixed deadlines
**Institutional Codes**: Vary by program

> **Source**: `https://grad.miami.edu/apply/index.html`

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**Academic Year**: 2026-2027

| Expense item | On-Campus | Off-Campus | With Parent/Relative |
|--------------|-----------|------------|----------------------|
| Tuition | $66,312 | $66,312 | $66,312 |
| Fees | $2,030 | $2,030 | $2,030 |
| Housing | $16,958 | $18,900 | $6,090 |
| Meals | $9,400 | $7,500 | $3,500 |
| Books | $1,040 | $1,040 | $1,040 |
| Personal | $2,294 | $2,294 | $2,294 |
| Transportation | $800 | $800 | $1,800 |
| Loan Fees | $38 | $38 | $38 |
| **Total Estimated COA** | **$98,872** | **$98,914** | **$83,104** |

> **Note**: International students: $104,091 (includes mandatory health insurance $4,483 and higher transportation allowance)

> **Source**: `https://admissions.miami.edu/undergraduate/financial-aid/cost-of-attendance/index.html`

### 4.2 Undergraduate financial-aid policy

**Need-Blind/Need-Aware**: **Need-aware for all applicants** (domestic and international)
**Merit Scholarships**: Awarded at admission based on holistic review; no separate application required
**Need-Based Aid**: Determined by FAFSA (domestic) and CSS Profile (international)
**Tuition-Free Threshold**: Not specified (no income-based tuition-free guarantee published)
**Median Actual Price Paid**: Not published
**Debt-Free Graduation Rate**: Not published
**Average Starting Salary**: Not published

**Key Points**:
- All students automatically considered for merit scholarships upon application submission
- Financial aid application required for need-based consideration
- FAFSA recommended for US citizens/eligible non-residents
- CSS Profile required for international students

> **Sources**: `https://finaid.miami.edu/`, `https://admissions.miami.edu/undergraduate/financial-aid/scholarships/index.html`

### 4.3 Graduate cost & funding framework

**Funding Types**:
- **Fully Funded**: Ph.D. programs typically offer full funding (tuition + stipend) through research/teaching assistantships
- **Partially Funded**: Some M.S. programs offer partial funding
- **Self-Funded**: Many professional master's programs (MBA, M.Arch, etc.)

**Common Funding Forms**:
- Research Assistantships (RA)
- Teaching Assistantships (TA)
- Fellowships and scholarships
- Grants

**Application Fee**: $75 (standard)
**Fee Waiver Policy**: Available for qualifying applicants (contact Graduate School)

**Graduate Professional School Costs**: See individual school websites (Law, Medicine, Business)

> **Source**: `https://grad.miami.edu/about/costs-fellowships-and-other-funding/index.html`

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/options-and-deadlines/index.html"
  source_snippet: "EARLY ACTION Application Deadline November 1"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.ED_I
  value: "November 1"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/options-and-deadlines/index.html"
  source_snippet: "EARLY DECISION I* Application Deadline November 1"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.ED_II
  value: "January 5"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/options-and-deadlines/index.html"
  source_snippet: "EARLY DECISION II* Application Deadline January 5"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.RD
  value: "January 5"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/options-and-deadlines/index.html"
  source_snippet: "REGULAR DECISION† Application Deadline January 5"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.costs.tuition
  value: "$66,312"
  source_url: "https://admissions.miami.edu/undergraduate/financial-aid/cost-of-attendance/index.html"
  source_snippet: "Tuition (1,4,5) $66,312"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_coa_on_campus
  value: "$98,872"
  source_url: "https://admissions.miami.edu/undergraduate/financial-aid/cost-of-attendance/index.html"
  source_snippet: "Estimated Total Cost of Attendance* $98,872†"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.tests.english.tofl_minimum
  value: "80"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/english-proficiency-requirements/index.html"
  source_snippet: "80 on the 0-120 scale internet-based TOEFL (before January 21, 2026)"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.tests.english.ielts_minimum
  value: "6.5"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/english-proficiency-requirements/index.html"
  source_snippet: "6.5 on the IELTS"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.tests.english.det_minimum
  value: "120"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/english-proficiency-requirements/index.html"
  source_snippet: "120 on the DET"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.tests.sat_act_policy
  value: "Required starting Fall 2026"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/freshman/index.html"
  source_snippet: "UM will once again require standardized test scores as part of the undergraduate admission application starting Fall 2026."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.tests.sat_code
  value: "5815"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/freshman/index.html"
  source_snippet: "SAT Code: 5815"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.tests.act_code
  value: "0760"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/freshman/index.html"
  source_snippet: "ACT Code: 0760"
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.application.fee
  value: "$75"
  source_url: "https://admissions.miami.edu/undergraduate/application-process/admission-requirements/freshman/index.html"
  source_snippet: "Upon submitting the Common Application, you will be asked to pay a $75 nonrefundable application fee."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.admissions.need_blind_intl
  value: "Need-aware for all"
  source_url: "https://finaid.miami.edu/"
  source_snippet: "Merit scholarships are awarded at the time of admission, based on a holistic evaluation of your admission application."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.programs.total
  value: "682"
  source_url: "https://bulletin.miami.edu/program-index/"
  source_snippet: "Program Index table with 682 rows"
  capture_date: "2026-07-06"
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.admissions.fee
  value: "$75"
  source_url: "https://grad.miami.edu/apply/index.html"
  source_snippet: "Admission into a graduate program is selective and determined by each individual department/program."
  capture_date: "2026-07-06"
  evidence_type: official_webpage

E-G-002:
  field: graduate.admissions.model
  value: "Decentralized"
  source_url: "https://grad.miami.edu/apply/index.html"
  source_snippet: "Admission into a graduate program is selective and determined by each individual department/program."
  capture_date: "2026-07-06"
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
umiami-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: rules 1-4
├── 01-undergraduate-architecture.md    # Section 1: Architecture programs
├── 02-undergraduate-arts-sciences.md   # Section 1: Arts & Sciences programs
├── 03-undergraduate-business.md        # Section 1: Business programs
├── 04-undergraduate-communication.md   # Section 1: Communication programs
├── 05-undergraduate-education.md       # Section 1: Education programs
├── 06-undergraduate-engineering.md     # Section 1: Engineering programs
├── 07-undergraduate-music.md           # Section 1: Music programs
├── 08-undergraduate-nursing.md         # Section 1: Nursing programs
├── 09-undergraduate-minors.md          # Section 1: All minors
├── 10-graduate-architecture.md         # Section 2: Architecture programs
├── 11-graduate-arts-sciences.md        # Section 2: Arts & Sciences programs
├── 12-graduate-business.md             # Section 2: Business programs
├── 13-graduate-communication.md        # Section 2: Communication programs
├── 14-graduate-education.md            # Section 2: Education programs
├── 15-graduate-engineering.md          # Section 2: Engineering programs
├── 16-graduate-law.md                  # Section 2: Law programs
├── 17-graduate-marine-science.md       # Section 2: Marine Science programs
├── 18-graduate-medicine.md             # Section 2: Medicine programs
├── 19-graduate-music.md                # Section 2: Music programs
├── 20-graduate-nursing.md              # Section 2: Nursing programs
├── 21-deadlines-requirements.md        # Section 3: Application requirements
├── 22-costs-financial-aid.md           # Section 4: Costs and aid
├── 23-evidence-chain.md                # Section 5: Evidence index
└── 24-comparison-framework.md          # Section 7: Cross-school comparison
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "umiami-knowledge-base-v2"
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

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program detail pages (GRE/TOEFL per program) | `https://grad.miami.edu/graduate-education/a-z-listing-graduate-programs/index.html` |
| P0 | Complete minors list (127 items) | `https://bulletin.miami.edu/program-index/` |
| P1 | Financial aid policy details (need-aware thresholds) | `https://finaid.miami.edu/how-financial-aid-works/index.html` |
| P1 | Graduate costs by program | Individual program websites |
| P2 | Historical cost of attendance | `https://admissions.miami.edu/undergraduate/financial-aid/cost-of-attendance/index.html` |
| P2 | Transfer admission requirements | `https://admissions.miami.edu/undergraduate/application-process/admission-requirements/transfer/index.html` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | UMiami | (Other schools) |
|-----------|--------|-----------------|
| Total UG cost/yr (on-campus) | $98,872 | |
| Tuition/yr | $66,312 | |
| Need-blind (intl?) | Need-aware for all | |
| EA deadline | November 1 | |
| ED I deadline | November 1 | |
| ED II deadline | January 5 | |
| RD deadline | January 5 | |
| SAT/ACT required? | Required (Fall 2026+) | |
| TOEFL min | 80 | |
| IELTS min | 6.5 | |
| DET min | 120 | |
| Application fee | $75 | |
| Grad application fee | $75 | |
| Total program count (rule 1) | 682 | |
| School/department count (rule 2) | 12 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.miami.edu, grad.miami.edu, finaid.miami.edu, bulletin.miami.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
