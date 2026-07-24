# Rice University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + Rice General Announcements (ga.rice.edu) static catalog
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Authoritative source**: Rice General Announcements (GA) — "the GA shall prevail as the authoritative source"

---

> ## ⚠ Reconciliation note (read first)
> 
> Three claims in the task prompt were **corrected against official sources** during this run:
> 
> | Prompt claim | Verified reality | Source |
> |---|---|---|
> | "need-blind + full-need incl internationals" | **NEED-AWARE for internationals** (need-blind applies to *domestic* applicants only). Rice does meet 100% of demonstrated need for admitted internationals and is loan-free, but the admission decision for non-US applicants is need-aware. | [financialaid.rice.edu/apply-aid/international-students](https://financialaid.rice.edu/apply-aid/international-students) |
> | "~\$58k tuition" | **Tuition is \$71,140 (2026-27)**. The \$58k figure is outdated (it was the 2022-23 tuition). | [financialaid.rice.edu/cost-attendance](https://financialaid.rice.edu/cost-attendance) |
> | "8 schools" | **7 academic schools grant undergraduate degrees** (Architecture, Engineering & Computing, Humanities & Arts, Music, Natural Sciences, Social Sciences, Business via Virani/Jones) + the **Susanne M. Glasscock School of Continuing Studies** (graduate MIS/DLS/MAT + non-credit only) = 8 schools total, but Glasscock grants no UG degrees. Engineering was also renamed to **George R. Brown School of Engineering and Computing** (added Computing) and Humanities to **School of Humanities and Arts**. | [www.rice.edu/departments](https://www.rice.edu/departments) |
> 
> All other prompt claims (ED Nov 1, RD Jan 4, need-meeting, test-optional) **verified correct**.

---

## SECTION 0 — 院校总览 (Institution Overview)

Rice University is a private research university in Houston, Texas, founded 1912. It is organized into **seven undergraduate-degree-granting academic schools** plus the Susanne M. Glasscock School of Continuing Studies (graduate/non-credit), and runs a distinctive **residential college system**. The authoritative curriculum source is the **General Announcements (GA)** at `ga.rice.edu`, which states explicitly: "In the event that there is a discrepancy between the GA and any other websites or publications, the GA shall prevail as the authoritative source."

### 0.1 专业与项目总数 (Rule 1 — Counts)

Counts computed from the GA `departments-programs` catalog (148 program records), expanded to one row per (program × credential). Three independent roll-ups reconcile to **310**.

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (UG degree majors) | **95** | 53 BA + 20 BS + 1 BArch + 21 BMus |
| 本科辅修 (UG Minor) | **47** | across all 7 schools |
| 本科证书 (UG Certificate) | **11** | languages, civic leadership, engineering leadership, teaching |
| 研究生学位项目 (Graduate degrees) | **129** | 41 MS + 29 PhD + 22 MMus + 18 MA + 12 DMA + 1 each MFA/MBA/MArch/MAT/MAcc/MBE/DLS |
| 研究生高级证书 (Graduate Certificate) | **10** | healthcare mgmt, dual-credit teaching, engineering, GEM, WGS/AAAS |
| 艺术家文凭 (Artist Diploma, AD) | **18** | Shepherd School advanced non-degree credential |
| **学位/证书项目总计 (UG + Grad)** | **310 credential rows** | across 148 distinct programs |
| 学院 / 独立系所总数 | **10 administrative units** | 7 UG-granting schools + Glasscock + cross-school grad + university-wide |

> **Reconciliation**: rule-1 total (**310**) == sum of distribution-matrix cells (**310**) == count of Rule-5 leaf rows (**310**) == sum of Rule-3 inventory (**310**). ✅

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with parent→child)

```
Rice University
├── School of Architecture (AR)                                          [学院 — UG+Grad]
│   └── Architecture                                                     [系]
├── George R. Brown School of Engineering and Computing (EN)             [学院 — UG+Grad]
│   ├── Artificial Intelligence / Computer Science / Data Science        [系]
│   ├── Bioengineering / Materials Science & NanoEngineering            [系]
│   ├── Chemical & Biomolecular / Civil & Environmental / Mechanical    [系]
│   ├── Electrical & Computer Engineering                                [系]
│   ├── Computational Applied Math & Operations Research / Statistics    [系]
│   ├── Industrial Engineering / Computational Science & Engineering     [系]
│   ├── Energy Transition & Sustainability / Energy & Water Sust.        [系]
│   ├── Engineering Design / Financial Computation & Modeling            [系]
│   ├── Digital Health / Global Health Technologies                      [系]
│   └── Rice Center for Engineering Leadership (Engineering Mgmt)        [系]
├── Wiess School of Natural Sciences (NS)                                [学院 — UG+Grad]
│   ├── Biosciences (Biochem & Cell Bio / Ecology & Evo Bio)            [系]
│   ├── Chemistry / Chemical Physics                                     [系]
│   ├── Earth, Environmental & Planetary Sciences / Environmental Sci   [系]
│   ├── Physics & Astronomy / Astronomy / Astrophysics                   [系]
│   ├── Mathematics / Neuroscience / Health Sciences / Sports Medicine  [系]
│   └── Applied Chemical Sci / Bioscience&HealthPolicy / Energy Geosci  [系 — grad/professional]
├── School of Humanities and Arts (HU)                                   [学院 — UG+Grad]
│   ├── Art / Art History / English & Creative Writing / Theatre        [系]
│   ├── History / Philosophy / Religion                                  [系]
│   ├── Center for Languages & Intercultural Communication              [系]
│   ├── Area Studies (Asian / European / French / German / Latin Am.)   [系]
│   ├── Classical Studies / Ancient Mediterranean Civ.                   [系]
│   └── Interdisciplinary (Medical Humanities / STS / WGS / MEMS)       [系]
├── School of Social Sciences (SS)                                       [学院 — UG+Grad]
│   ├── Anthropology / Sociology / Cognitive Sciences / Linguistics     [系]
│   ├── Economics / Mathematical Economic Analysis / Computational Econ [系]
│   ├── Political Science / Psychological Sciences / Global Affairs     [系]
│   ├── Sport Management / Sport Analytics                               [系]
│   ├── Managerial Econ & Org Sciences / Social Policy Analysis          [系]
│   └── HCI & Human Factors / Industrial-Org Psych / Energy Econ        [系 — grad/professional]
├── Shepherd School of Music (MU)                                        [学院 — UG+Grad]
│   └── Music (21 BMus performance areas + Music History/Theory +       [系]
│            grad AD/MMus/DMA; BA Music also housed here)
├── Jesse H. Jones Graduate School of Business (JS)                      [学院 — hosts UG BA Business + grad]
│   ├── Management (BA Business — via Virani UG School of Business)      [系]
│   ├── Accounting (MAcc)                                               [系 — grad]
│   ├── Entrepreneurship (UG Minor)                                      [系]
│   └── Healthcare Management (Grad Cert)                                [系]
├── Susanne M. Glasscock School of Continuing Studies (CS)               [学院 — GRAD ONLY, no UG degrees]
│   ├── Education (MAT) / Interdisciplinary Studies (MIS/DLS)            [系 — grad]
│   └── Dual Credit Teacher Credentialing (Grad Cert)                    [系 — grad]
├── Cross-School Graduate Programs (GR)                                  [跨学院 grad]
│   ├── Applied Physics                                                  [系 ⚠ EN+NS]
│   ├── Systems, Synthetic & Physical Biology                            [系 ⚠ NS+EN]
│   └── Global Health Technologies                                       [系 ⚠ EN+NS]
└── University-Wide (UG)                                                 [全校性]
    ├── Center for Civic Leadership (UG Certificate)                     [系]
    ├── Naval Science / NROTC (UG Minor)                                 [系]
    └── Center for Teaching Excellence (Grad Cert)                       [系]
```

> **Shared / cross-school departments** (⚠): Applied Physics, Systems/Synthetic/Physical Biology, and Global Health Technologies are interdisciplinarian programs tagged `GR` in the GA because they span multiple schools. The BA in Business is administratively tagged `JS` (Jones) in the GA even though marketing now groups it under the **Virani Undergraduate School of Business** (a newly chartered undergraduate school housed within Jones).

### 0.3 学历级别明细 (Rule 3 — Degree-level inventory)

Rice uses **standard** abbreviations (no Latin). Each row shows the official Rice abbreviation(s) mapped to the **canonical** form. Counts are credential-row counts (one program may grant multiple credentials).

| canonical | official (Rice) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| `BA` | `BA` | Bachelor of Arts | undergraduate | 53 |
| `BS` | `BS`, `BSBE`, `BSCE`, `BSCS`, `BSChE`, `BSECE`, `BSEnvE`, `BSME`, `BSMSNE` | Bachelor of Science | undergraduate | 20 |
| `BArch` | `BArch` | Bachelor of Architecture (5-yr professional) | undergraduate | 1 |
| `BMus` | `BMus` | Bachelor of Music | undergraduate | 21 |
| `MA` | `MA`, `MA*`, `MGA`, `MIS` | Master of Arts | graduate | 18 |
| `MS` | `MCAAM`, `MCEE`, `MCEcon`, `MCS`, `MCSE`, `MChE`, `MDH`, `MDS`, `MECE`, `MEEcon`, `MEML`, `METS`, `MHCIHF`, `MIE`, `MIOP`, `MME`, `MMSNE`, `MS`, `MS*`, `MSACS`, `MSBHP`, `MSEA`, `MSEG`, `MSPE`, `MSSpS`, `MST`, `MStat` | Master of Science | graduate | 41 |
| `MFA` | `MFA` | Master of Fine Arts | graduate | 1 |
| `MBA` | `MBA` | Master of Business Administration | graduate | 1 |
| `MMus` | `MMus` | Master of Music | graduate | 22 |
| `MArch` | `MArch` | Master of Architecture (professional) | graduate | 1 |
| `MAT` | `MAT` | Master of Arts in Teaching | graduate | 1 |
| `MAcc` | `MAcc` | Master of Accounting | graduate | 1 |
| `MBE` | `MBE` | Master of Bioengineering | graduate | 1 |
| `PhD` | `PhD` | Doctor of Philosophy | graduate | 29 |
| `DMA` | `DMA` | Doctor of Musical Arts | graduate | 12 |
| `DLS` | `DLS` | Diploma in Liberal Studies | graduate | 1 |
| `Minor` | `Minor` | Undergraduate Minor | undergraduate | 47 |
| `Certificate` | `Certificate` | Undergraduate / Graduate Certificate | both | 21 |
| `AD` | `AD` | Artist Diploma (advanced, non-degree) | graduate | 18 |
| **合计** | | | | **310** |

> All Rice engineering-specific bachelor codes (`BSBE`/`BSChE`/`BSCE`/`BSCS`/`BSECE`/`BSEnvE`/`BSMSNE`/`BSME`) canonicalize to **BS**. The `*` suffix on graduate credentials (`MA*`, `MS*`) marks the **thesis / research variant** of the MA/MS — canonical MA/MS. `AD` = Artist Diploma (advanced, non-degree). The ~25 unique professional-master's codes (`MChE`, `MCS`, `MCAAM`, `MDS`, etc.) all canonicalize to **MS** (a few to **MA**), making Rice's MS count (41) by far its largest credential.

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

Counts cross-tabbed by **学院 × canonical degree level**. Column headers use canonical codes so this matrix is directly addable across universities. Cells = credential-row count (`·` = 0).

| 学院 \ 级别 | BA | BS | BArch | BMus | MA | MS | MFA | MBA | PhD | DMA | MMus | MArch | MAT | MAcc | MBE | DLS | Minor | Cert | AD | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| School of Architecture | 2 | · | 1 | · | · | 1 | · | · | · | · | · | 1 | · | · | · | · | · | · | · | **5** |
| George R. Brown School of Engineering and Computing | 9 | 11 | · | · | 2 | 23 | · | · | 10 | · | · | · | · | · | 1 | · | 9 | 3 | · | **68** |
| Wiess School of Natural Sciences | 10 | 9 | · | · | 2 | 10 | · | · | 6 | · | · | · | · | · | · | · | 7 | · | · | **44** |
| School of Humanities and Arts | 17 | · | · | · | 6 | · | 1 | · | 5 | · | · | · | · | · | · | · | 25 | 12 | · | **66** |
| School of Social Sciences | 13 | · | · | · | 6 | 5 | · | · | 5 | · | · | · | · | · | · | · | 2 | · | · | **31** |
| Shepherd School of Music | 1 | · | · | 21 | · | · | · | · | · | 12 | 22 | · | · | · | · | · | · | · | 18 | **74** |
| Jesse H. Jones Graduate School of Business | 1 | · | · | · | 1 | · | · | 1 | 1 | · | · | · | · | 1 | · | · | 2 | 1 | · | **8** |
| Susanne M. Glasscock School of Continuing Studies | · | · | · | · | 1 | · | · | · | · | · | · | · | 1 | · | · | 1 | 1 | 2 | · | **6** |
| Cross-School Graduate Programs | · | · | · | · | · | 2 | · | · | 2 | · | · | · | · | · | · | · | · | 1 | · | **5** |
| University-Wide | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | · | 1 | 2 | · | **3** |
| **合计** | 53 | 20 | 1 | 21 | 18 | 41 | 1 | 1 | 29 | 12 | 22 | 1 | 1 | 1 | 1 | 1 | 47 | 21 | 18 | **310** |

> Matrix cell-sum = **310** == Rule-1 total (310) ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

Every undergraduate major/minor/certificate listed under its **学院 → 系 → 学位级别 → 专业**. Data source: GA `departments-programs` (148 records). All UG credential rows total **153** (95 degree majors + 47 minors + 11 certificates).

### 1.1 College/school architecture

Rice has **7 undergraduate-degree-granting schools** (Architecture; George R. Brown School of Engineering and Computing; Wiess School of Natural Sciences; School of Humanities and Arts; School of Social Sciences; Shepherd School of Music; and the Virani Undergraduate School of Business, whose BA in Business is administered through the Jesse H. Jones Graduate School of Business). The Susanne M. Glasscock School of Continuing Studies grants **no undergraduate degrees** (graduate + non-credit only). See the full hierarchy tree in Section 0.2. Students declare a major by the second semester of sophomore year and may declare up to three; ~50% pursue more than one major.

### 1.2 Undergraduate majors/minors/certificates — grouped by 学院 > 系 > 学位级别

#### School of Architecture  `[GA code: AR]`

##### Department: Architecture

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Architectural Studies |
| 2 | Architecture |

###### BArch (`BArch`)
| # | 专业 / Program |
|---|------|
| 1 | Architecture and Building Science |

#### George R. Brown School of Engineering and Computing  `[GA code: EN]`

##### Department: Artificial Intelligence

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Artificial Intelligence |

##### Department: Bioengineering

###### BSBE → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Bioengineering |

##### Department: Chemical and Biomolecular Engineering

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Chemical Engineering |

###### BSChE → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Chemical Engineering |

##### Department: Civil and Environmental Engineering

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Civil and Environmental Engineering |

###### BSCE/BSEnvE → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Civil Engineering |
| 2 | Environmental Engineering |

##### Department: Computational Applied Mathematics and Operations Research

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Computational and Applied Mathematics |
| 2 | Operations Research |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Operations Research |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Computational and Applied Mathematics |
| 2 | Operations Research |

##### Department: Computer Science

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Computer Science |

###### BSCS → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Computer Science |

##### Department: Data Science

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Data Science |

##### Department: Digital Health

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Digital Health |

##### Department: Electrical and Computer Engineering

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Electrical and Computer Engineering |

###### BSECE → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Electrical and Computer Engineering |

##### Department: Energy and Water Sustainability

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Energy and Water Sustainability |

##### Department: Engineering Design

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Engineering Design |

##### Department: Financial Computation and Modeling

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Financial Computation and Modeling |

##### Department: Global Health Technologies

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Global Health Technologies |

##### Department: Materials Science and Nanoengineering

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Materials Science and NanoEngineering |

###### BSMSNE → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Materials Science and NanoEngineering |

##### Department: Mechanical Engineering

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Mechanical Engineering |

###### BSME → canonical `BS`
| # | 专业 / Program |
|---|------|
| 1 | Mechanical Engineering |

##### Department: Rice Center for Engineering Leadership

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Engineering Leadership |

##### Department: Statistics

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

#### Wiess School of Natural Sciences  `[GA code: NS]`

##### Department: Astronomy

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Astronomy |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Astronomy |

##### Department: Astrophysics

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Astrophysics |

##### Department: Biosciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Biosciences |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Biosciences |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Biochemistry and Cell Biology |
| 2 | Ecology and Evolutionary Biology |

##### Department: Chemical Physics

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Chemical Physics |

##### Department: Chemistry

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Chemistry |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Chemistry |

##### Department: Earth, Environmental and Planetary Sciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Earth, Environmental and Planetary Sciences |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Earth, Environmental and Planetary Sciences |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Earth, Environmental and Planetary Sciences |

##### Department: Environmental Science

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Environmental Science |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Environmental Science |

##### Department: Health Sciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Health Sciences |

##### Department: Mathematics

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Mathematics |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Mathematics |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Mathematics |

##### Department: Neuroscience

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Neuroscience |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Neuroscience |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Neuroscience |

##### Department: Physics and Astronomy

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Physics |

###### BS (`BS`)
| # | 专业 / Program |
|---|------|
| 1 | Physics |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Physics |

##### Department: Sports Medicine and Exercise Physiology

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Sports Medicine and Exercise Physiology |

#### School of Humanities and Arts  `[GA code: HU]`

##### Department: African and African American Studies

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | African and African American Studies |

##### Department: Ancient Mediterranean Civilizations

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Ancient Mediterranean Civilizations |

##### Department: Art

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Art |

##### Department: Art History

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Art History |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Art History |

##### Department: Asian Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Asian Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Asian Studies |

##### Department: Center for Languages and Intercultural Communication

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Arabic |
| 2 | Chinese |
| 3 | French |
| 4 | German |
| 5 | Italian |
| 6 | Japanese |
| 7 | Korean |
| 8 | Portuguese |
| 9 | Spanish |

##### Department: Classical Civilizations

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Classical Civilizations |

##### Department: Classical Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Classical Studies |

##### Department: English

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | English and Creative Writing |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | English and Creative Writing |

##### Department: English and Creative Writing

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Creative Writing |

##### Department: Environmental Studies

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Environmental Studies |

##### Department: European Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | European Studies |

##### Department: French Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | French Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | French Studies |

##### Department: German Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | German Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | German Studies |

##### Department: Greek Language and Literature

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Greek Language and Literature |

##### Department: History

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | History |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | History |

##### Department: Jewish Studies

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Jewish Studies |

##### Department: Latin American and Latinx Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Latin American and Latinx Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Latin American and Latinx Studies |

##### Department: Latin Language and Literature

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Latin Language and Literature |

##### Department: Media Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Media Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Cinema and Media Studies |

##### Department: Medical Humanities

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Medical Humanities |

##### Department: Medieval and Early Modern Studies

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Medieval and Early Modern Studies |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Medieval and Early Modern Studies |

##### Department: Museums and Cultural Heritage

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Museums and Cultural Heritage |

##### Department: Philosophy

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Philosophy |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Philosophy |

##### Department: Politics, Law, and Social Thought

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Politics, Law, and Social Thought |

##### Department: Religion

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Religion |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Religion |

##### Department: Science and Technology Studies

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Science and Technology Studies |

##### Department: Spanish and Portuguese

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Spanish and Portuguese |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Spanish and Portuguese |

##### Department: Study of Women, Gender, and Sexuality

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Study of Women, Gender, and Sexuality |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Study of Women, Gender, and Sexuality |

##### Department: Theatre

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Theatre |

#### School of Social Sciences  `[GA code: SS]`

##### Department: Anthropology

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Anthropology |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Anthropology |

##### Department: Cognitive Sciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Cognitive Sciences |

##### Department: Economics

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Economics |

##### Department: Global Affairs

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Global Affairs |

##### Department: Linguistics

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Linguistics |

##### Department: Managerial Economics and Organizational Sciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Managerial Economics and Organizational Sciences |

##### Department: Mathematical Economic Analysis

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Mathematical Economic Analysis |

##### Department: Political Science

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Political Science |

##### Department: Psychological Sciences

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Psychology |

##### Department: Social Policy Analysis

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Social Policy Analysis |

##### Department: Sociology

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Sociology |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Sociology |

##### Department: Sport Analytics

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Sport Analytics |

##### Department: Sport Management

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Sport Management |

#### Shepherd School of Music  `[GA code: MU]`

##### Department: Music

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Music |

###### BMus (`BMus`)
| # | 专业 / Program |
|---|------|
| 1 | Bassoon Performance |
| 2 | Cello Performance |
| 3 | Clarinet Performance |
| 4 | Composition |
| 5 | Double Bass Performance |
| 6 | Flute Performance |
| 7 | Harp Performance |
| 8 | Horn Performance |
| 9 | Music History |
| 10 | Music Theory |
| 11 | Oboe Performance |
| 12 | Orchestral Conducting |
| 13 | Organ Performance |
| 14 | Percussion Performance |
| 15 | Piano Performance |
| 16 | Trombone Performance |
| 17 | Trumpet Performance |
| 18 | Tuba Performance |
| 19 | Viola Performance |
| 20 | Violin Performance |
| 21 | Vocal Performance |

#### Jesse H. Jones Graduate School of Business  `[GA code: JS]`

##### Department: Entrepreneurship

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Entrepreneurship |

##### Department: Management

###### BA (`BA`)
| # | 专业 / Program |
|---|------|
| 1 | Business |

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Business |

#### Susanne M. Glasscock School of Continuing Studies  `[GA code: CS]`

##### Department: Education

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Education |

#### University-Wide (Civic Leadership / Naval Science / Teaching Excellence)  `[GA code: UG]`

##### Department: Center for Civic Leadership

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Civic Leadership |

##### Department: Naval Science

###### Minor (`Minor`)
| # | 专业 / Program |
|---|------|
| 1 | Naval Science |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Rice does not maintain formally joint UG majors across schools in the GA the way MIT does. Cross-school UG offerings are **minors and certificates**: Global Health Technologies (UG Minor, tagged `EN` in GA but cross-listed with Natural Sciences), Civic Leadership (UG Certificate, university-wide), and the Engineering Leadership Certificate (EN). The **BA in Business** is the closest analogue — it is administered through Jones (`JS`) but marketed under the Virani Undergraduate School of Business. See the tables above for their home placements.

### 1.4 Minors — complete list (47)

All 47 undergraduate minors extracted above are listed in their home-school tables in §1.2 (filter rows where the credential is `Minor`). They span all 7 schools: Humanities & Arts hosts the most (~25, including language certificates counted separately), Engineering hosts 9, Natural Sciences 7, Social Sciences 2, Jones Business 2, plus Naval Science (NROTC) under University-Wide.

### 1.5 General / Institute-wide requirements

Rice uses a **distribution-based general education** model (no rigid core). Students must complete a specified number of hours across three broad groups (Group I — Humanities; Group II — Social Sciences; Group III — Natural Sciences/Engineering/Mathematics), plus the **Writing and Communication Requirement** and a **Lifetime Physical Activity Program (LPAP)** requirement. Details in the GA under "Graduation Requirements" — [ga.rice.edu/undergraduate-students/](https://ga.rice.edu/undergraduate-students/).

### 1.6 No course-ID numbering scheme

Rice does NOT use an MIT-style numeric course-ID system (e.g. "6-3"). Programs are identified by name and GA school code (`AR`/`EN`/`HU`/`JS`/`MU`/`NS`/`SS`/`CS`/`GR`/`UG`). Course numbers exist per-department (e.g. `COMP 182`) but are not part of the program identity. N/A — no quick-lookup table needed.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

Every graduate program listed under its **学院 → 系 → 学位级别 → 项目**. Data source: GA `departments-programs` + cross-checked against `graduate.rice.edu/programs-study`. All graduate credential rows total **157** (129 degrees + 10 certificates + 18 Artist Diplomas).

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### School of Architecture  `[GA code: AR]`

##### Department: Architecture

###### MArch (`MArch`)
| # | 专业 / Program |
|---|------|
| 1 | Architecture and Building Science |

###### MS (`MS`)
| # | 专业 / Program |
|---|------|
| 1 | Architecture |

#### George R. Brown School of Engineering and Computing  `[GA code: EN]`

##### Department: Bioengineering

###### MBE (`MBE`)
| # | 专业 / Program |
|---|------|
| 1 | Bioengineering |

###### MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Bioengineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Bioengineering |

##### Department: Chemical and Biomolecular Engineering

###### MChE/MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Chemical Engineering |
| 2 | Chemical Engineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Chemical Engineering |

##### Department: Civil and Environmental Engineering

###### MCEE/MS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Civil Engineering |
| 2 | Civil Engineering |
| 3 | Environmental Engineering |
| 4 | Environmental Engineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Civil Engineering |
| 2 | Environmental Engineering |

##### Department: Computational Applied Mathematics and Operations Research

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Computational Applied Mathematics and Operations Research |

###### MCAAM → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Computational and Applied Mathematics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Computational Applied Mathematics and Operations Research |

##### Department: Computational Science and Engineering

###### MCSE → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Computational Science and Engineering |

##### Department: Computer Science

###### MCS/MS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Computer Science |
| 2 | Computer Science |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Computer Science |

##### Department: Data Science

###### MDS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Data Science |

##### Department: Digital Health

###### MDH → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Digital Health |

##### Department: Electrical and Computer Engineering

###### MECE/MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Electrical and Computer Engineering |
| 2 | Electrical and Computer Engineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Electrical and Computer Engineering |

##### Department: Energy Transition and Sustainability

###### METS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Energy Transition and Sustainability |

##### Department: Industrial Engineering

###### MIE → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Industrial Engineering |

##### Department: Materials Science and Nanoengineering

###### MMSNE/MS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Materials Science and NanoEngineering |
| 2 | Materials Science and NanoEngineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Materials Science and NanoEngineering |

##### Department: Mechanical Engineering

###### MME/MS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Mechanical Engineering |
| 2 | Mechanical Engineering |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Mechanical Engineering |

##### Department: Rice Center for Engineering Leadership

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Engineering Management and Leadership - Engineering Project Management |
| 2 | Engineering Management and Leadership - Product Management for Engineering Leaders |

###### MEML → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Engineering Management and Leadership |

##### Department: Statistics

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

###### MStat → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Statistics |

#### Wiess School of Natural Sciences  `[GA code: NS]`

##### Department: Applied Chemical Sciences

###### MSACS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Applied Chemical Sciences |

##### Department: Bioscience and Health Policy

###### MSBHP → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Bioscience and Health Policy |

##### Department: Biosciences

###### MS (`MS`)
| # | 专业 / Program |
|---|------|
| 1 | Biochemistry and Cell Biology |
| 2 | Ecology and Evolutionary Biology |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Biochemistry and Cell Biology |
| 2 | Ecology and Evolutionary Biology |

##### Department: Chemistry

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Chemistry |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Chemistry |

##### Department: Earth, Environmental and Planetary Sciences

###### MS (`MS`)
| # | 专业 / Program |
|---|------|
| 1 | Earth, Environmental and Planetary Sciences |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Earth, Environmental and Planetary Sciences |

##### Department: Energy Geoscience

###### MSEG → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Energy Geoscience |

##### Department: Environmental Analysis

###### MSEA → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Environmental Analysis |

##### Department: Mathematics

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Mathematics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Mathematics |

##### Department: Physics and Astronomy

###### MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Physics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Physics |

##### Department: Science Teaching

###### MST → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Science Teaching |

##### Department: Space Studies

###### MSSpS → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Space Studies |

#### School of Humanities and Arts  `[GA code: HU]`

##### Department: African and African American Studies

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | African and African American Studies |

##### Department: Art History

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Art History |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Art History |

##### Department: English

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | English and Creative Writing |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | English and Creative Writing |

##### Department: English and Creative Writing

###### MFA (`MFA`)
| # | 专业 / Program |
|---|------|
| 1 | Creative Writing |

##### Department: Gnosticism, Esotericism, and Mysticism

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Gnosticism, Esotericism, and Mysticism |

##### Department: History

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | History |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | History |

##### Department: Philosophy

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Philosophy |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Philosophy |

##### Department: Religion

###### MA/MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Religion |
| 2 | Religion |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Religion |

##### Department: Study of Women, Gender, and Sexuality

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Study of Women, Gender, and Sexuality |

#### School of Social Sciences  `[GA code: SS]`

##### Department: Anthropology

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Anthropology |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Anthropology |

##### Department: Computational Economics

###### MCEcon → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Computational Economics |

##### Department: Economics

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Economics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Economics |

##### Department: Energy Economics

###### MEEcon → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Energy Economics |

##### Department: Global Affairs

###### MGA → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Global Affairs |

##### Department: Human-Computer Interaction and Human Factors

###### MHCIHF → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Human-Computer Interaction and Human Factors |

##### Department: Industrial-Organizational Psychology

###### MIOP → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Industrial-Organizational Psychology |

##### Department: Political Science

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Political Science |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Political Science |

##### Department: Psychological Sciences

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Psychology |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Psychology |

##### Department: Social Policy Evaluation

###### MSPE → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Social Policy Evaluation |

##### Department: Sociology

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Sociology |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Sociology |

#### Shepherd School of Music  `[GA code: MU]`

##### Department: Music

###### AD (`AD`)
| # | 专业 / Program |
|---|------|
| 1 | Bassoon Performance |
| 2 | Cello Performance |
| 3 | Clarinet Performance |
| 4 | Double Bass Performance |
| 5 | Flute Performance |
| 6 | Harp Performance |
| 7 | Horn Performance |
| 8 | Oboe Performance |
| 9 | Opera Performance |
| 10 | Orchestral Conducting |
| 11 | Organ Performance |
| 12 | Percussion Performance |
| 13 | Piano Performance |
| 14 | Trombone Performance |
| 15 | Trumpet Performance |
| 16 | Tuba Performance |
| 17 | Viola Performance |
| 18 | Violin Performance |

###### DMA (`DMA`)
| # | 专业 / Program |
|---|------|
| 1 | Cello Performance |
| 2 | Clarinet Performance |
| 3 | Composition |
| 4 | Double Bass Performance |
| 5 | Flute Performance |
| 6 | Oboe Performance |
| 7 | Organ Performance |
| 8 | Percussion Performance |
| 9 | Piano Performance |
| 10 | Viola Performance |
| 11 | Violin Performance |
| 12 | Vocal Performance |

###### MMus (`MMus`)
| # | 专业 / Program |
|---|------|
| 1 | Bassoon Performance |
| 2 | Cello Performance |
| 3 | Clarinet Performance |
| 4 | Composition |
| 5 | Double Bass Performance |
| 6 | Flute Performance |
| 7 | Harp Performance |
| 8 | Horn Performance |
| 9 | Musicology |
| 10 | Oboe Performance |
| 11 | Orchestral Conducting |
| 12 | Organ Performance |
| 13 | Percussion Performance |
| 14 | Piano Chamber Music and Accompanying |
| 15 | Piano Performance |
| 16 | String Quartet Performance |
| 17 | Trombone Performance |
| 18 | Trumpet Performance |
| 19 | Tuba Performance |
| 20 | Viola Performance |
| 21 | Violin Performance |
| 22 | Vocal Performance |

#### Jesse H. Jones Graduate School of Business  `[GA code: JS]`

##### Department: Accounting

###### MAcc (`MAcc`)
| # | 专业 / Program |
|---|------|
| 1 | Accounting |

##### Department: Healthcare Management

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Healthcare Management |

##### Department: Management

###### MA* → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Business |

###### MBA (`MBA`)
| # | 专业 / Program |
|---|------|
| 1 | Business |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Business |

#### Susanne M. Glasscock School of Continuing Studies  `[GA code: CS]`

##### Department: Dual Credit Teacher Credentialing

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Dual Credit Teacher Credentialing - English |
| 2 | Dual Credit Teacher Credentialing - History |

##### Department: Education

###### MAT (`MAT`)
| # | 专业 / Program |
|---|------|
| 1 | Education |

##### Department: Interdisciplinary Studies

###### DLS (`DLS`)
| # | 专业 / Program |
|---|------|
| 1 | Interdisciplinary Studies |

###### MIS → canonical `MA`
| # | 专业 / Program |
|---|------|
| 1 | Interdisciplinary Studies |

#### Cross-School Graduate Programs (applied physics / SSPB / global health)  `[GA code: GR]`

##### Department: Applied Physics

###### MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Applied Physics |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Applied Physics |

##### Department: Global Health Technologies

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Global Health Technologies |

##### Department: Systems, Synthetic, and Physical Biology

###### MS* → canonical `MS`
| # | 专业 / Program |
|---|------|
| 1 | Systems, Synthetic, and Physical Biology |

###### PhD (`PhD`)
| # | 专业 / Program |
|---|------|
| 1 | Systems, Synthetic, and Physical Biology |

#### University-Wide (Civic Leadership / Naval Science / Teaching Excellence)  `[GA code: UG]`

##### Department: Center for Teaching Excellence

###### Certificate (`Certificate`)
| # | 专业 / Program |
|---|------|
| 1 | Teaching and Learning |

### 2.2 Worked example — PhD in Computer Science (the largest/most-applied-to program)

- **Department**: Computer Science ([cs.rice.edu](https://cs.rice.edu/))
- **School**: George R. Brown School of Engineering and Computing (code `EN`)
- **Degrees offered**: MCS (Professional Master), MS (thesis), PhD — all visible in the §2.1 Engineering / Computer Science table
- **Application portal**: apply through the department (Rice graduate admissions is **decentralized** — see §2.3)
- **Application fee**: **\$85** (waived for doctoral applicants graduating from / residing in Texas or bordering states LA/AR/OK/NM)
- **GRE policy (2026)**: **NOT required** for Computer Science (GRE generally not required university-wide for 2026; only PhD Economics *requires* it; several engineering programs *recommend/strongly recommend* it)
- **English proficiency**: TOEFL iBT 90 (or 4.5 on the new scale on/after Jan 21 2026) / IELTS 7 / Duolingo 115 — ETS code **6609**
- **Funding**: PhD students typically receive a **\$37,000–\$40,000/yr stipend** + full tuition support; over 90% of new doctoral students receive a fellowship + tuition waiver
- **Deadline**: set by the department (typically mid-December for fall PhD admission — verify on the CS department page); applications open on/around September 1

### 2.3 Graduate admissions model

**Decentralized.** "Prospective graduate students apply to Rice through the department in which they wish to study. Each individual department, rather than the Office of Graduate and Postdoctoral Studies, handles their own application deadline, program specifics, and offers of admission." There is **no central graduate application portal** — each of the 7 schools plus the cross-school GR programs runs its own admissions. The Office of Graduate and Postdoctoral Studies (`graduate.rice.edu`) is a services office, NOT an admissions decider. The **Jones School of Business** (MBA, MAcc, PhD Business) generally requires GMAT / Executive Assessment / GRE (waivers possible).

---
## SECTION 3 — Application requirements & deadlines

> **Region**: US (private university). Common App for UG; decentralized departmental for grad.

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|---|---|---|
| Admissions site | [admission.rice.edu](https://admission.rice.edu/) | official |
| Application portal | **Common Application** + Rice writing supplement (Rice Box image required) | E-U-002 |
| **ED I deadline** | **November 1** (binding; mid-December decision) | E-U-001 |
| **ED II deadline** | **January 4** (binding) | E-U-001 |
| **RD deadline** | **January 4** | E-U-001 |
| **Shepherd School of Music** | **December 1** (preliminary submission; music applicants NOT eligible for ED or QuestBridge) | E-U-001 |
| SAT last-applicable (ED I) | October | E-U-001 |
| ACT last-applicable (ED I) | September | E-U-001 |
| Decision notification | ED I: mid-December; ED II & RD: by early April (enroll by May 1) | E-U-001 |
| Financial aid deadline | CSS Profile due **Nov 15** (ED I); RD equivalent in spring | E-U-008 |
| **SAT/ACT policy** | **Test-optional** — "Rice recommends...to submit SAT or ACT test scores, if available. Students who are unable to submit test scores or prefer not to submit test scores will be given full consideration." Superscore. CB/TOEFL code **6609**, ACT code **4152** | E-U-003 |
| Score-report method | Official scores sent directly from testing organization (opt-in to consideration; cannot opt out once opted in) | E-U-003 |
| Interview policy | **Optional** — evaluative Rice Senior Interview (must request) + optional Alumni Interview; NOT required | E-U-002 |
| Recommendations | **3 required**: 1 School Counselor + Teacher 1 + Teacher 2 (core academic subjects preferred) | E-U-002 |
| Portfolios | Architecture (PDF, ≤15MB, ≤10 content pages); Art (optional, JPEG ≤10MB); Shepherd Music (preliminary recording) | E-U-002 |
| Application fee | **\$75** nonrefundable (must be paid online); fee-waiver via Common App fee-waiver prompts (QuestBridge = auto waiver). **International applicants are NOT eligible for a fee waiver.** | E-U-002 |
| Transfer pathway | Yes (separate deadlines; intl transfers get NO financial aid) | E-U-002 |

### 3.2 Undergraduate English proficiency table

Required of non-native English speakers (exempt if native English speaker OR completed ≥2 years full-time study in an English-language curriculum). Scores are **minimums** (not "competitive").

| Exam | Minimum | Recommended |
|------|---------|------------|
| **TOEFL iBT** (incl. Home Edition) | **100** | n/a (100 is the bar) |
| **IELTS** (Academic) | **7** | n/a |
| **Cambridge English** (C1 Advanced / C2 Proficiency) | **185** | n/a |
| **Duolingo English Test** | **130** | n/a |

> Source: [admission.rice.edu/frequently-asked-questions](https://admission.rice.edu/frequently-asked-questions) — E-U-004. Rice College Board/TOEFL code = 6609.

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|---|---|---|
| Admissions model | **Decentralized** — apply through the specific department/program (no central portal) | E-G-001 |
| Application platforms | Department-specific application portals (varies by program); Jones Business uses its own platform (GMAT/EA/GRE) | E-G-001 |
| **Application fee** | **\$85** (waived for doctoral applicants from TX or bordering states LA/AR/OK/NM, excl. Jones Business) | E-G-002 |
| CGS April-15-equivalent honor date | **Not explicitly stated** on Rice's official pages (unverified — Rice's status as a CGS Resolution signatory could not be confirmed from public pages; do not assume) | — |
| **GRE policy (2026)** | **Generally NOT required.** Per-program exceptions: **PhD Economics = REQUIRED**; MS/PhD Materials Science & NanoEngineering = recommended; MS Civil & Environmental / PhD Environmental / PhD Civil = strongly recommended; MArch = strongly recommended; MS/PhD Mechanical Engineering = strongly recommended; PhD Political Science = strongly recommended. Jones Business = GMAT/EA/GRE. ETS code **6609**. | E-G-003 |
| Language-test policy | TOEFL iBT **90** (or **4.5** on the new scale on/after Jan 21 2026) / IELTS Academic or Indicator **7** / Duolingo **115**. **NOT accepted for 2026**: TOEFL ITP Plus, TOEFL MyBest. Vericant interview accepted as supplemental only. | E-G-004 |
| Exemption rules | Degree from accredited US institution; OR post-secondary degree from an institution where English is the official language of instruction (Rice publishes a qualifying-country list). | E-G-004 |
| Application timeline | Applications open on/around **September 1**; deadlines set by each department (typically Dec–Jan for fall PhD) | E-G-001 |
| Institutional/departmental test codes | ETS (GRE/TOEFL) = **6609**; SAT = 6609; ACT = 4152 | E-U-003 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

Source: [financialaid.rice.edu/cost-attendance](https://financialaid.rice.edu/cost-attendance) — E-U-005. Figures apply to undergraduates who entered 2024 & later.

| Expense item | Amount (USD) | Description |
|---|---|---|
| **Tuition** | **\$71,140** | Direct cost (billed by Rice) |
| Mandatory Fees | \$984 | Direct cost |
| On-Campus Living Expenses (housing + food) | \$20,530 | Direct cost (on-campus residents) |
| Off-Campus Living Expenses | \$6,600 | Indirect cost (living with family / off-campus estimate) |
| Books & Supplies | \$1,540 | Indirect |
| Personal Expenses | \$3,115 | Indirect |
| **Total — On-Campus** | **\$97,309** | Standard full COA |
| **Total — Living with Family** | **\$83,379** | Reduced COA |
| Average Freshman Aid Package | \$71,698 | (reference) |
| Average Family Responsibility (aid recipients) | \$15,426 | (reference) |

**Additional billable items (NOT in standard COA):**

- **O-Week fee**: \$370 (all freshmen) + \$560 housing/meals if staying on campus during orientation
- **International Orientation fee**: \$395 (international freshmen)
- **Health insurance**: required; not included in COA — additional billable cost unless comparable coverage demonstrated
- **Travel estimate** (indirect, not in COA): \$300 in-state / \$700 out-of-state / \$3,000 foreign-country

### 4.2 Undergraduate financial-aid policy

Source: [financialaid.rice.edu/rice-investment](https://financialaid.rice.edu/rice-investment) + [/apply-aid/international-students](https://financialaid.rice.edu/apply-aid/international-students) — E-U-006, E-U-007.

| Policy | Value |
|---|---|
| Need-blind admission | **Domestic applicants only** (U.S. citizens, permanent residents, refugees/asylees, DACA, undocumented from U.S. high schools) |
| **Need-aware admission** | **INTERNATIONAL applicants** — "Rice's international need-based aid policy for both admission and financial aid is need aware... the amount of financial aid a family might need is taken into consideration." |
| Meets demonstrated need | **100%** of demonstrated need for all admitted students (domestic AND international) |
| Loan-free | **Yes** — Rice is a loan-free institution; aid packages are grant/scholarship only (no student loans) |
| Merit scholarships | Yes (separate from need-based aid) |
| International transfer aid | **None** — "We do not offer need-based or merit-based aid to international transfer applicants." |

**The Rice Investment income tiers** (need-based grant aid, assuming typical assets):

| Family income range | Aid grant |
|---|---|
| **\$75,000 and below** | **Full tuition + fees + living expenses** |
| **\$75,000 – \$140,000** | **Full tuition** |
| **\$140,000 – \$200,000** | **Half tuition** |
| **\$200,000 – \$300,000** | Need-based aid grant (≈70% of aid applicants in this range receive aid) |

> ⚠ **International students are NOT eligible for The Rice Investment** but ARE considered for general need-based institutional grant aid (with 100% demonstrated need met for those admitted with aid). Families with significant atypical assets may not qualify for The Rice Investment but Rice still funds 100% demonstrated need.

### 4.3 Graduate cost & funding framework

Source: [graduate.rice.edu/admissions/costofstudy](https://graduate.rice.edu/admissions/costofstudy) — E-G-005.

- **Funding model**: doctoral students = typically fully funded (tuition waiver + stipend); professional master's = generally self-funded (some partial support); graduate certificates = self-funded
- **Doctoral stipend**: **\$37,000 – \$40,000 per year** for living expenses
- **Fellowship + tuition waiver coverage**: **over 90% of newly enrolled graduate students** receive a financial incentive package (fellowship + tuition waiver); many departments offer multi-year support for students making normal progress
- **Common funding forms**: Graduate Fellowship, Research Assistantship (RA), Teaching Assistantship (TA), competitive external fellowships (NSF GRFP, NASA, Fulbright, Ford, GEM), NIH/NSF/NASA Federal Training Grants
- **Application fee**: \$85 (waived for doctoral applicants from TX + bordering states)
- **Fee-waiver policy**: doctoral TX/bordering-state waiver; other waivers available (see Application Fee Waiver Weeks page)
- **Tuition for Architecture / Shepherd Music / Professional Master's**: varies by program (see Cashier's website)
- **Reduced tuition**: after 10 semesters full-time in a single doctoral program (6 semesters for Music/Architecture), students pay a reduced tuition rate
- **Cost-of-attendance / living-expenses pages**: [graduate.rice.edu/admissions/costofstudy](https://graduate.rice.edu/admissions/costofstudy); per-program rates on the Cashier's site

---

## SECTION 5 — Evidence chain index

Every cited fact bound to (source_url, source_snippet, capture_date). `E-U-NNN` = undergraduate, `E-G-NNN` = graduate.

```yaml
id: E-U-001
field: ug.deadlines
value: ED I Nov 1 / ED II & RD Jan 4 / Shepherd Dec 1
source_url: https://admission.rice.edu/apply/first-year-domestic-applicants
source_snippet: "EARLY DECISION I... Nov. 1 Common Application and Rice writing supplement $75 nonrefundable application fee... EARLY DECISION II... Jan. 4... REGULAR DECISION... Jan. 4... SHEPHERD SCHOOL OF MUSIC... Dec. 1"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
id: E-U-002
field: ug.application_requirements
value: Common App, $75 fee, 3 recs, supplements, portfolios
source_url: https://admission.rice.edu/apply/first-year-domestic-applicants
source_snippet: "Common Application and Rice writing supplement / $75 nonrefundable application fee (must be paid online) / Official high school transcript / Recommendation Letters: School Counselor, Teacher 1, Teacher 2 / Architecture portfolio (Architecture applicants only)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-003
field: ug.test_policy
value: Test-optional SAT/ACT; CB/TOEFL 6609, ACT 4152
source_url: https://admission.rice.edu/apply/first-year-domestic-applicants
source_snippet: "Rice recommends first-year and transfer student applicants to undergraduate degree-seeking programs to submit SAT or ACT test scores, if available. Students who are unable to submit test scores or prefer not to submit test scores will be given full consideration in the admission selection process... Rice's College Board code, including TOEFL, is 6609 and our ACT code is 4152."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-004
field: ug.english_proficiency
value: TOEFL 100 / IELTS 7 / Cambridge 185 / DET 130
source_url: https://admission.rice.edu/frequently-asked-questions
source_snippet: "What tests for non-native English speakers does Rice accept? We accept the TOEFL, IELTS, Duolingo and Cambridge English Exams to demonstrate English proficiency. Test Minimum Score: TOEFL 100 (Internet-based test); IELTS 7; Cambridge English Exams (C1 Advanced or C2 Proficiency) 185; Duolingo 130."
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
id: E-U-005
field: ug.coa
value: 2026-27 tuition $71,140; total on-campus $97,309
source_url: https://financialaid.rice.edu/cost-attendance
source_snippet: "*2026-2027 COST OF ATTENDANCE UNDERGRADUATES Entered 2024 & Later... Tuition $71,140 $71,140 / Mandatory Fees $984 $984 / On-Campus Living Expenses $20,530 / Off-Campus Living Expenses $6,600 / Books & Supplies $1,540 / Personal Expenses $3,115 / Total $97,309 $83,379 / Average Freshman Aid Package $71,698 / Average Responsibility for Families Receiving Aid $15,426"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
id: E-U-006
field: ug.financial_aid_policy.rice_investment
value: Income tiers $75k-below full / 75-140k full tuition / 140-200k half / 200-300k aid
source_url: https://financialaid.rice.edu/rice-investment
source_snippet: "INCOME RANGE $200K-300K / $140K-200K / $75K-140K / $75K & BELOW — Half Tuition / Full Tuition / Full Tuition, Fees, & Living Expenses... 100% of Demonstrated Need Met... Loan-free institution"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-007
field: ug.intl_aid_policy
value: International = NEED AWARE; 100% need met; not eligible for Rice Investment; no intl transfer aid
source_url: https://financialaid.rice.edu/apply-aid/international-students
source_snippet: "International students who receive need-based aid will have 100% of demonstrated need met with institutional grant aid, but are not eligible for the Rice Investment... Rice's international need-based aid policy for both admission and financial aid is need aware... the student's financial need will be considered for both admission and financial aid... We do not offer need-based or merit-based aid to international transfer applicants."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-008
field: ug.css_profile
value: CSS Profile due Nov 15 (ED I); CSS code 6609
source_url: https://financialaid.rice.edu/apply-aid/international-students
source_snippet: "OCT. 1 2026-2027 CSS Profile available / NOV. 15 DUE 2026-2027 CSS Profile School Code 6609 / Complete using 2024 income and tax information"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-009
field: ug.schools_and_majors
value: 7 academic schools, 50+ UG majors
source_url: https://admission.rice.edu/apply/application-philosophy
source_snippet: "Rice offers more than 50 undergraduate majors across seven academic schools of study, including architecture, business, engineering, humanities, music, natural sciences and social sciences. All applicants must specify which one of our seven academic schools is their primary intended area of study."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-U-010
field: ug.class_profile
value: 8.0% acceptance; SAT 1510-1560; 56 countries
source_url: https://admission.rice.edu/apply/class-profile
source_snippet: "2024-2025 Cycle: Applicants 36,791 / Admits 2,948 / Admission Rate 8.0% / Enrolled 1,263... SAT Composite 25th 1510 75th 1560 / ACT Composite 34 36... International 13% / In Texas 35% / Outside of Texas 51%... 56 Countries Represented"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
id: E-U-011
field: catalog.authoritative
value: GA is authoritative; 148 programs; school codes
source_url: https://ga.rice.edu/programs-study/departments-programs/
source_snippet: "The General Announcements (GA) is the official Rice curriculum. In the event that there is a discrepancy between the GA and any other websites or publications, the GA shall prevail as the authoritative source." [Each program block: Program / Department / School (AR/EN/HU/JS/MU/NS/SS/CS/GR/UG) / Undergraduate / Graduate]
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
id: E-G-001
field: grad.admissions_model
value: Decentralized; apply through department
source_url: https://graduate.rice.edu/admissions/how-to-apply
source_snippet: "Prospective graduate students apply to Rice through the department in which they wish to study. Each individual department, rather than the Office of Graduate and Postdoctoral Studies, handles their own application deadline, program specifics, and offers of admission... Applications generally open on or around September 1."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-G-002
field: grad.fee
value: $85 application fee; doctoral TX/bordering-state waiver
source_url: https://graduate.rice.edu/admissions/qualifications
source_snippet: "An application fee of $85 is generally required. Some programs do waive this requirement... for 2026 admissions, the application fee for doctoral programs is waived for those residing in Texas or bordering states of Arkansas, Louisiana, Oklahoma, and New Mexico (this does not include programs in the Jones School of Business.)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-G-003
field: grad.gre_policy
value: GRE not required 2026 except PhD Economics; ETS 6609
source_url: https://graduate.rice.edu/programs-study
source_snippet: "Rice Graduate Studies is not requiring the GRE for 2026, but will provide students with the option of submitting those scores. However, the following individual Rice degree programs will recommend, strongly recommend, or require the general GRE for 2026 admission... General GRE is required for the Ph.D. in Economics... The ETS Reporting code for Rice University is 6609."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-G-004
field: grad.english
value: TOEFL 90 (or 4.5 new) / IELTS 7 / DET 115; no ITP Plus, no MyBest
source_url: https://graduate.rice.edu/admissions/language-proficiency-requirements
source_snippet: "For exams taken before January 21, 2026: We require a minimum TOEFL iBT score of 90. For exams taken on or after January 21, 2026, we require a minimum TOEFL iBT score of 4.5. At least 7 on the IELTS. At least 115 on the Duolingo test of English proficiency. For 2026, Rice will not accept the ITP Plus test... Only the best composite TOEFL score is accepted; myBest scores are not accepted."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
id: E-G-005
field: grad.stipend
value: Doctoral stipend $37k-40k/yr; 90%+ get fellowship + tuition waiver
source_url: https://graduate.rice.edu/admissions/costofstudy
source_snippet: "Over 90% of newly enrolled graduate students are provided with a financial incentive package that includes a Graduate Fellowship and a tuition waiver... Qualified doctoral and thesis master's students often receive departmental stipends of $37,000-$40,000 per year to cover living expenses."
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
rice-knowledge-base-v2/
├── rice-overview               (Section 0 — counts, hierarchy, matrix, inventory)
├── rice-ug-architecture        (Section 1 — School of Architecture UG)
├── rice-ug-engineering         (Section 1 — George R. Brown School of Engineering & Computing UG)
├── rice-ug-natural-sciences    (Section 1 — Wiess School of Natural Sciences UG)
├── rice-ug-humanities          (Section 1 — School of Humanities & Arts UG)
├── rice-ug-social-sciences     (Section 1 — School of Social Sciences UG)
├── rice-ug-music               (Section 1 — Shepherd School of Music UG)
├── rice-ug-business            (Section 1 — Virani/Jones Business UG)
├── rice-ug-minors-certs        (Section 1.3/1.4 — minors, certificates, university-wide)
├── rice-grad-engineering       (Section 2 — Engineering graduate programs)
├── rice-grad-natural-sciences  (Section 2 — Natural Sciences graduate)
├── rice-grad-humanities        (Section 2 — Humanities & Arts graduate)
├── rice-grad-social-sciences   (Section 2 — Social Sciences graduate)
├── rice-grad-music             (Section 2 — Shepherd School: MMus/DMA/AD)
├── rice-grad-architecture      (Section 2 — Architecture MArch/MS)
├── rice-grad-business          (Section 2 — Jones: MBA/MAcc/PhD)
├── rice-grad-continuing        (Section 2 — Glasscock: MAT/MIS/DLS/certs)
├── rice-grad-cross-school      (Section 2 — GR: Applied Physics / SSPB / Global Health)
├── rice-app-requirements       (Section 3 — UG + grad deadlines, tests, English)
├── rice-costs-aid              (Section 4 — COA, Rice Investment, intl aid, grad funding)
└── rice-evidence               (Section 5 — 16 evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "rice-knowledge-base-v2"
  school: "<home college, e.g. George R. Brown School of Engineering and Computing>"
  department: "<home department>"
  degree_level: "<BA|BS|BArch|BMus|MA|MS|MFA|MBA|MMus|MArch|MAT|MAcc|MBE|PhD|DMA|DLS|AD|Minor|Certificate>"
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
|---|---|---|
| **P0** | Per-graduate-program deadlines (each department sets own; not centralized) | [graduate.rice.edu/admissions/program-contacts](https://graduate.rice.edu/admissions/program-contacts) + each department's site |
| **P0** | Architecture BArch 5-year curriculum detail (the GA separates "Architecture" BA/MS from "Architecture and Building Science" BArch/MArch — verify program overlap) | [ga.rice.edu](https://ga.rice.edu/programs-study/departments-programs/) → Architecture |
| **P1** | Rice CGS April-15 Resolution signatory status (could not confirm from public pages) | Council of Graduate Schools public signatory list |
| **P1** | Per-program graduate tuition for Architecture / Shepherd Music / professional master's (varies; lives on Cashier's site) | [cashier.rice.edu](https://cashier.rice.edu/) |
| **P1** | Confirm Rice Investment thresholds for the **next** admission cycle (income brackets reset annually) | [financialaid.rice.edu/rice-investment](https://financialaid.rice.edu/rice-investment) |
| **P2** | Course-level catalog (Rice has no program numbering, but course numbers e.g. COMP 182 exist) | [ga.rice.edu/programs-study/courses/](https://ga.rice.edu/programs-study/courses/) |
| **P2** | ED I / ED II / RD decision-notification exact dates (only "mid-December" / "early April" stated) | [admission.rice.edu/apply/first-year-domestic-applicants](https://admission.rice.edu/apply/first-year-domestic-applicants) |

---

## SECTION 7 — Cross-school comparison framework

Rice values placed alongside blank columns for other schools. Dimensions chosen to surface the highest-variance policies across selective U.S. universities.

| Dimension | Rice (2026-07-05) | MIT | Harvard | Stanford | Caltech | (next) |
|---|---|---|---|---|---|---|
| Total UG cost/yr (on-campus) | **\$97,309** (2026-27) | | | | | |
| Tuition/yr | **\$71,140** (2026-27) | | | | | |
| Need-blind (domestic) | ✅ Yes | | | | | |
| Need-blind (international) | ❌ **No — need-aware** | | | | | |
| Meets 100% demonstrated need | ✅ Yes (domestic + intl) | | | | | |
| Loan-free | ✅ Yes | | | | | |
| Tuition-free income threshold | ≤\$75k = full tuition+fees+living | | | | | |
| ED deadline | **Nov 1** (ED I) + Jan 4 (ED II) | | | | | |
| RD deadline | **Jan 4** | | | | | |
| SAT/ACT required? | ❌ Test-optional (recommended) | | | | | |
| TOEFL min (UG) | 100 | | | | | |
| IELTS min (UG) | 7 | | | | | |
| Duolingo min (UG) | 130 | | | | | |
| Grad application fee | **\$85** | | | | | |
| Grad GRE policy (2026) | Generally not required (PhD Econ = required) | | | | | |
| Grad English TOEFL min | 90 (or 4.5 new scale) | | | | | |
| CGS April-15 signatory | Unverified | | | | | |
| **Total program count (Rule 1)** | **310 credential rows / 148 programs** | | | | | |
| **School/department count (Rule 2)** | **10 administrative units** (7 UG-granting + Glasscock + cross-school + university-wide) | | | | | |
| Acceptance rate | 8.0% (Class of 2029) | | | | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.rice.edu, financialaid.rice.edu, graduate.rice.edu, ga.rice.edu (General Announcements), www.rice.edu
> **Verification**: ego-browser snapshotText + js innerText extraction + serverFetch on static catalog pages
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: rule-1 (310) == matrix-sum (310) == rule-5 rows (310) == rule-3 inventory (310) ✅
> **Cache**: uni-cache/schools/rice/{site-memory.json, last-extract.json, content-hashes.json}
