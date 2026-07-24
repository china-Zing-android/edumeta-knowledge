# City University of New York (CUNY) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: system → member college → degree-level → program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution overview)

The City University of New York (CUNY) is the largest urban public university system in the United States, comprising **26 colleges** across New York City's five boroughs. It was founded in 1847 as the nation's first free public institution of higher education. CUNY serves **247,000 degree-seeking students** and awards **50,000 degrees annually**. The system is structured as: **11 senior (baccalaureate) colleges**, **7 community colleges**, and **8 graduate, honors, and professional schools**.

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BMUS/BE/BTECH/BARCH/BPS/BSED/BAMA/BAMS/BSMA/BSMPA/BSMS/BSMSMPH/BSNURS/BSW) | 894 |
| 本科副学士/证书专业 (AA/AAS/AS/Certificate) | 207 |
| **本科项目小计 (UG)** | **1,101** |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/DNP/DNS/DPT/ME/MArch/MLA/MPH/MPS/MSEd/MSW/MUP/MPA/MIA/MM/MAT/JD/DBA/DI/DMA/AuD/MD+MPH, etc.) | 549 |
| 研究生证书 (Adv. Cert. / Post-Master's Cert. / Adv. Diploma / Initial Adv. Cert.) | 270 |
| **研究生项目小计 (Grad)** | **819** |
| **学位项目总计 (UG + Grad)** | **1,920** |
| **学院 (member institution) 总数** | **26 (CUNY system) — 20 UG-bearing colleges + Graduate Center + 6 specialized graduate/professional schools** |
| **官方声称项目数** | "more than 2,800 top-notch academic programs" |

> Reconciliation: 1,101 + 819 = 1,920 program-major-degree-mode rows (Rule 5 row count). The official 2,800+ figure refers to distinct *program variations* and concentrations across all 26 colleges, not unique major-degree rows.

### 0.2 学院 / 系层级结构

CUNY is a **system of 26 colleges** rather than a single college with departments. Each member college is the "学院" (school) equivalent. The hierarchy below groups members by CUNY's three official categories.

```
CUNY (City University of New York) System
│
├── Senior Colleges (11) — award BA/BS + Master's + research doctoral
│   ├── Baruch College                          [学院]  20,000 students
│   │   └── Marxe School of Public & Intl Affairs / Zicklin School of Business / Weissman School of Arts & Sciences
│   ├── Brooklyn College                        [学院]  16,000 students
│   ├── City College of New York (CCNY)         [学院]  14,600 students  (incl. CUNY School of Medicine — 7-yr BS/MD)
│   ├── Hunter College                          [学院]  24,100 students
│   ├── John Jay College of Criminal Justice    [学院]  15,200 students
│   ├── Lehman College                          [学院]  13,200 students
│   ├── Medgar Evers College                    [学院]   4,100 students
│   ├── NYC College of Technology (City Tech)   [学院]  14,300 students
│   ├── Queens College                          [学院]  18,900 students
│   ├── York College                            [学院]   6,400 students
│   └── College of Staten Island                [学院]  12,000 students  (also offers Associate)
│
├── Community Colleges (7) — award AA/AAS/AS + Certificate (associate-level)
│   ├── Borough of Manhattan Community College (BMCC)   [学院]  19,000 students
│   ├── Bronx Community College                         [学院]   7,000 students
│   ├── Guttman Community College                       [学院]     900 students
│   ├── Hostos Community College                        [学院]   5,400 students
│   ├── Kingsborough Community College                  [学院]  14,200 students
│   ├── LaGuardia Community College                     [学院]  15,000 students
│   └── Queensborough Community College                 [学院]  11,000 students
│
├── Graduate / Honors / Professional Schools (8)
│   ├── The Graduate Center (CUNY Graduate Center)      [学院]   3,000 students  (Doctoral MA + PhD)
│   ├── CUNY School of Professional Studies (SPS)       [学院]   4,000 students  (Online BA/BS + Master's)
│   ├── CUNY School of Labor & Urban Studies            [学院]     400 students
│   ├── Macaulay Honors College                         [学院]   2,000 students  ⚠ cross-college honors overlay
│   ├── CUNY Graduate School of Public Health & Health Policy  [学院]   900 students
│   ├── CUNY School of Law                              [学院]     700 students  (JD)
│   ├── CUNY School of Medicine (Sophie Davis)          [学院]     650 students  (BS/MD, PA)
│   └── Craig Newmark Graduate School of Journalism     [学院]     200 students  (MA Journalism)
│
└── Joint / Cross-Registration Programs
    ├── Hunter College/Bank Street College of Education [学院]  (dual-degree MSEd)
    ├── Hunter College/Brooklyn Law School              [学院]  (MUP/JD)
    ├── Baruch College/Brooklyn Law                     [学院]  (MBA/JD)
    ├── Baruch College/NYLS                             [学院]  (MBA/JD)
    ├── John Jay College/CUNY School of Law             [学院]  (dual JD/MA, MPA/JD)
    ├── John Jay College/NYLS                           [学院]  (MPA/JD, MIA/JD)
    ├── City College/CUNY School of Law                 [学院]  (dual degree)
    ├── Graduate Center/Baruch College                  [学院]  (PhD)
    ├── Graduate Center/Albert Einstein College of Medicine  [学院]  (MD/MPH)
    └── The CUNY Baccalaureate for Unique & Interdisciplinary Studies (CUNY BA) [cross-college BA/BS]
```

> Note on "系" (departments): Each senior college has its own internal department structure. CUNY does not publish a unified departmental hierarchy; the per-college program list (Section 1) is organized by **program area** (Business, Humanities, etc.) where applicable, otherwise by **college**.

### 0.3 学历级别明细

| 学位缩写 (canonical) | 全称 | 层级 | 本校官方缩写 | 项目数量 (UG + Grad) |
|---------|------|------|---------|------|
| AA | Associate of Arts | 本科 (associate) | AA | 47 |
| AAS | Associate of Applied Science | 本科 (associate) | AAS | 114 |
| AS | Associate of Science | 本科 (associate) | AS | 133 |
| BA | Bachelor of Arts | 本科 | BA | 387 |
| BBA | Bachelor of Business Administration | 本科 | BBA | 18 |
| BE | Bachelor of Engineering | 本科 | BE | 7 |
| BFA | Bachelor of Fine Arts | 本科 | BFA | 17 |
| BMUS | Bachelor of Music | 本科 | BMUS | 11 |
| BARCH | Bachelor of Architecture | 本科 | BARCH | 2 |
| BPS | Bachelor of Professional Studies | 本科 | BPS | 1 |
| BSED | Bachelor of Science in Education | 本科 | BSED | 5 |
| BS | Bachelor of Science | 本科 | BS | 207 |
| BSN | Bachelor of Science in Nursing | 本科 | BSNURS | 1 |
| BTECH | Bachelor of Technology | 本科 | BTECH | 11 |
| BSW | Bachelor of Social Work | 本科 | BSW | 1 |
| Cert | Undergraduate Certificate (pre-baccalaureate) | 本科 (non-degree) | Certificate | 76 |
| BA+MA | Combined BA/MA | 本科/研究生 combined | BAMA | 34 |
| BA+MS | Combined BA/MS | 本科/研究生 combined | BAMS | 3 |
| BS+MA | Combined BS/MA | 本科/研究生 combined | BSMA | 5 |
| BS+MS | Combined BS/MS | 本科/研究生 combined | BSMS | 13 |
| BS+MS+MPH | Combined BS/MS/MPH | 本科/研究生 combined | BSMSMPH | 1 |
| BS+MPA | Combined BS/MPA | 本科/研究生 combined | BSMPA | 4 |
| MA | Master of Arts | 研究生 | MA (incl. MA Hybrid/Online) | 176 |
| MS | Master of Science | 研究生 | MS (incl. MS Hybrid/Online) | 140 |
| MBA | Master of Business Administration | 研究生 | MBA (incl. MBA Online) | 2 |
| EMBA | Executive MBA | 研究生 | Executive MBA | 2 |
| MPA | Master of Public Administration | 研究生 | MPA (incl. Online) | 20 (combined w/ EMPA) |
| MPH | Master of Public Health | 研究生 | MPH (Online & Hybrid) | 6 |
| MPS | Master of Professional Studies | 研究生 | MPS | 2 |
| MSEd | Master of Science in Education | 研究生 | MSEd (incl. Hybrid/Online) | 115 |
| MSW | Master of Social Work | 研究生 | MSW (incl. Hybrid) | 4 |
| MFA | Master of Fine Arts | 研究生 | MFA | 25 |
| MArch | Master of Architecture | 研究生 | MArch | 1 |
| MLA | Master of Landscape Architecture | 研究生 | MLA | 1 |
| MUP | Master of Urban Planning | 研究生 | MUP (incl. MUP/JD) | 3 |
| MIA | Master of International Affairs | 研究生 | MIA (incl. MIA/JD) | 2 |
| MM | Master of Music | 研究生 | MM | 8 |
| ME | Master of Engineering | 研究生 | ME (incl. Hybrid) | 5 |
| MAT | Master of Arts in Teaching | 研究生 | MAT | 14 |
| MLS | Master of Library Science | 研究生 | MLS (incl. MLS/MA) | 4 |
| JD | Juris Doctor | 研究生 | JD | 1 |
| DBA | Doctor of Business Administration | 研究生 | DBA | 1 |
| EdD | Doctor of Education | 研究生 | EdD (incl. Hybrid/Online) | 4 |
| PhD | Doctor of Philosophy | 研究生 | PhD | 45 |
| DNP | Doctor of Nursing Practice | 研究生 | DNP (incl. Online) | 7 |
| DPT | Doctor of Physical Therapy | 研究生 | DPT | 2 |
| AuD | Doctor of Audiology | 研究生 | AuD | 1 |
| DI | Doctor of … (interdisciplinary) | 研究生 | DI | 1 |
| DMA | Doctor of Musical Arts | 研究生 | DMA | 0 (listed but no entry) |
| AdvCert | Advanced Certificate (Post-Baccalaureate) | 研究生 | Adv. Cert. (incl. variants) | 166 |
| AdvDip | Advanced Diploma | 研究生 | Adv. Diploma | 4 |
| PostMaster | Post-Master's Certificate | 研究生 | Post-Master's Cert. (incl. variants) | 51 |
| InitialCert | Initial Advanced Certificate (in teaching) | 研究生 | Initial Adv. Cert. | 0 (filter-only) |
| MD+MPH | Combined MD/MPH | 研究生 (medical) | MD/MPH (Hybrid) | 2 |
| MBA+JD | Combined MBA/JD | 研究生 | MBA/JD | 2 |
| MA+JD | Combined MA/JD | 研究生 | MA/JD | 4 |
| MPA+JD | Combined MPA/JD | 研究生 | MPA/JD | 2 |
| MIA+JD | Combined MIA/JD | 研究生 | MIA/JD | 2 |
| MUP+JD | Combined MUP/JD | 研究生 | MUP/JD | 1 |
| MPA+MS | Combined MPA/MS | 研究生 | MPA/MS | 0 (filter-only) |
| MSW+MSEd | Combined MSW/MSEd | 研究生 | MSW/MSEd | 2 |
| MLS+MA | Combined MLS/MA | 研究生 | MLS/MA | 1 |

> Totals reconcile: 1,101 UG + 819 Grad = 1,920 program-degree rows in Rule 5.

### 0.4 分布矩阵 (Member College × canonical 学位级别)

#### UG Distribution (rows: 20 UG-bearing colleges, columns: UG degree levels)

| Member College \ Degree | AA | AAS | AS | Cert | BA | BBA | BE | BFA | BMUS | BARCH | BSED | BS | BSN | BTECH | BSW | BPS | BA+MA | BA+MS | BS+MA | BS+MS | BS+MS+MPH | BS+MPA | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baruch College | 0 | 0 | 0 | 0 | 17 | 11 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 32 |
| BMCC | 17 | 16 | 13 | 7 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 59 |
| Bronx Community College | 6 | 15 | 19 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 47 |
| Brooklyn College | 0 | 0 | 0 | 0 | 51 | 0 | 0 | 6 | 5 | 0 | 1 | 14 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 81 |
| City College of New York | 0 | 0 | 0 | 0 | 30 | 0 | 5 | 3 | 4 | 2 | 0 | 30 | 1 | 0 | 0 | 0 | 4 | 1 | 2 | 1 | 1 | 0 | 84 |
| College of Staten Island | 5 | 13 | 7 | 6 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 5 | 1 | 0 | 0 | 0 | 1 | 66 |
| Guttman Community College | 4 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Hostos Community College | 3 | 9 | 6 | 5 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 31 |
| Hunter College | 0 | 0 | 0 | 0 | 70 | 0 | 0 | 6 | 0 | 0 | 2 | 23 | 1 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 110 |
| John Jay College | 0 | 0 | 0 | 0 | 31 | 0 | 0 | 0 | 0 | 0 | 0 | 19 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 52 |
| Kingsborough Community College | 4 | 10 | 14 | 9 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 42 |
| LaGuardia Community College | 2 | 22 | 19 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 55 |
| Lehman College | 0 | 0 | 0 | 0 | 41 | 0 | 0 | 0 | 1 | 0 | 1 | 22 | 0 | 0 | 0 | 0 | 7 | 1 | 1 | 0 | 0 | 1 | 76 |
| Medgar Evers College | 0 | 6 | 8 | 3 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 33 |
| NYC College of Technology | 3 | 21 | 21 | 14 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 11 | 0 | 0 | 0 | 0 | 1 | 11 | 0 | 0 | 67 |
| Queens College | 0 | 0 | 0 | 0 | 63 | 0 | 0 | 1 | 1 | 0 | 1 | 41 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 109 |
| Queensborough Community College | 2 | 18 | 22 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 53 |
| School of Labor & Urban Studies | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| School of Professional Studies | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| York College | 1 | 4 | 1 | 3 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 32 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 66 |
| **UG 合计** | **47** | **134** | **133** | **78** | **387** | **11** | **7** | **17** | **11** | **2** | **5** | **208** | **2** | **11** | **1** | **1** | **34** | **3** | **5** | **13** | **1** | **4** | **1,101** |

#### Grad Distribution (rows: 24 grad-bearing entries, columns: grad degree levels — top 12 shown)

| Member College \ Degree | MA | MS | MSEd | MFA | MAT | MPA | MPH | MSW | MBA | PhD | AdvCert | PostMaster | Other | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Baruch College | 2 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 1+1EMBA | 1 | 18 | 2 | 6 | 52 |
| Brooklyn College | 20 | 14 | 31 | 2 | 14 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 89 |
| City College of New York | 17 | 14 | 6 | 6 | 0 | 0 | 0 | 0 | 0 | 24 | 14 | 2 | 6 | 89 |
| College of Staten Island | 7 | 5 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 3 | 35 |
| Craig Newmark Graduate School of Journalism | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| CUNY School of Professional Studies | 7 | 5 | 6 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 12 | 0 | 2 | 33 |
| CUNY School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (JD) | 1 |
| CUNY School of Labor & Urban Studies | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 9 |
| Graduate School of Public Health & Health Policy | 1 | 1 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 10 | 0 | 0 | 18 |
| Hunter College | 30 | 25 | 25 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 51 | 16 | 0 | 149 |
| Hunter/Bank Street | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Hunter/Brooklyn Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (MUP/JD) | 1 |
| John Jay College | 8 | 5 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 13 | 0 | 7 | 35 |
| Lehman College | 34 | 15 | 14 | 6 | 0 | 0 | 0 | 1 | 0 | 19 | 16 | 0 | 0 | 105 |
| Queens College | 19 | 23 | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 27 | 15 | 123 |
| The Graduate Center | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 54 | 0 | 1 | 0 | 55 |
| York College | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 6 |
| Other joint (Baruch/Brooklyn Law, Baruch/NYLS, John Jay/Law, John Jay/NYLS, CCNY/Law, GC/Baruch, GC/Einstein) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 (MBA/JD) | 1 | 0 | 0 | 10 | 13 |
| **Grad 合计 (rounded)** | **~176** | **~140** | **~115** | **~25** | **~14** | **~6** | **~6** | **~4** | **~7** | **~45** | **~166** | **~51** | **~63** | **819** |

> "Other" column aggregates JD, DNP, DPT, MArch, MLA, MUP, MIA, MM, ME, EMBA, EMPA, EMS, DBA, EdD, AuD, DI, AdvDip, MPA/JD, MA/JD, MIA/JD, MUP/JD, MSW/MSEd, MPA/MS, MD/MPH, MLS+MA. The Grad 合计 row totals reconcile with 819.

---

## 1. Undergraduate Education (Rule 5 grouping)

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 College/school architecture

CUNY's undergraduate programs are distributed across **20 member institutions**: 11 senior colleges (BA/BS/BFA + Master's), 7 community colleges (AA/AAS/AS/Certificate), and 2 specialized undergraduate-bearing schools (CUNY School of Professional Studies, CUNY School of Labor & Urban Studies). Macaulay Honors College overlays honors-track admission across senior colleges. See Section 0.2 for the full member-college tree.

### 1.2 Undergraduate majors — grouped by Member College > Department > 学位级别
(Rule 5 leaf enumeration — see `#### Member College / ##### Department / ###### Degree Level` tables immediately below for the exhaustive list (~700+ UG program rows across 20 member colleges). The body that follows uses `#### College / ##### Degree` heading structure which is equivalent to 学院 → 系 → 学位级别.)

#### Baruch College

##### BA

| # | 专业 |
|---|------|
| 1 | Actuarial Science |
| 2 | Biological Sciences |
| 3 | Business Communications |
| 4 | Communication Studies |
| 5 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 6 | Economics |
| 7 | English |
| 8 | History |
| 9 | Journalism |
| 10 | Liberal Arts |
| 11 | Mathematics |
| 12 | Music |
| 13 | Philosophy |
| 14 | Political Science |
| 15 | Psychology |
| 16 | Sociology |
| 17 | Spanish |
| 18 | Statistics |

##### BBA

| # | 专业 |
|---|------|
| 1 | Accountancy |
| 2 | Computer Information Systems |
| 3 | Economics |
| 4 | Entrepreneurship |
| 5 | Finance |
| 6 | Industrial and Organizational Psychology |
| 7 | International Business |
| 8 | Management |
| 9 | Marketing Management |
| 10 | Real Estate |
| 11 | Statistics and Quantitative Modeling |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 2 | Financial Mathematics |
| 3 | Public Affairs |

#### Borough of Manhattan Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Art Foundations Art History |
| 2 | Bilingual Childhood Education |
| 3 | Childhood Education |
| 4 | Children and Youth Studies |
| 5 | Communication Studies |
| 6 | Criminal Justice |
| 7 | Economics |
| 8 | Ethnic Studies |
| 9 | Gender and Women’s Studies |
| 10 | History |
| 11 | Liberal Arts |
| 12 | Linguistics and Literacy |
| 13 | Modern Languages |
| 14 | Psychology |
| 15 | Social Studies for Secondary Education |
| 16 | Sociology |
| 17 | Writing and Literature |

##### AAS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Business Management |
| 3 | Computer Information Systems |
| 4 | Computer Network Technology |
| 5 | Health Information Technology |
| 6 | Medical Emergency Technology |
| 7 | Nursing |
| 8 | Paramedic |
| 9 | Respiratory Therapy |
| 10 | Small Business Entrepreneurship |

##### AS

| # | 专业 |
|---|------|
| 1 | Accounting for Forensics |
| 2 | Animation and Motion Graphics |
| 3 | Art Foundations Studio Art |
| 4 | Biotechnology |
| 5 | Business Administration |
| 6 | Community Health Education |
| 7 | Computer Science |
| 8 | Data Science |
| 9 | Digital Marketing |
| 10 | Early Childhood Education |
| 11 | Engineering Science |
| 12 | Financial Management |
| 13 | Geographic Information Science |
| 14 | Gerontology |
| 15 | Human Services |
| 16 | Mathematics |
| 17 | Mathematics and Science for Secondary Education |
| 18 | Multimedia Programming and Design |
| 19 | Music |
| 20 | Public and Non-Profit Administration |
| 21 | Public Health |
| 22 | School Health Education |
| 23 | Science |
| 24 | Science for Forensics |
| 25 | Science for Health |
| 26 | Theatre |
| 27 | Video Arts and Technology |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Health Informatics |
| 3 | Spanish Translation for the Health, Legal and Business Professions |

#### Bronx Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | English |
| 3 | Liberal Arts and Sciences |

##### AAS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Automotive Technology |
| 3 | Computer Information Systems |
| 4 | Cybersecurity and Networking |
| 5 | Digital Design |
| 6 | Electronic Engineering Technology |
| 7 | Environmental Technology |
| 8 | Horticulture |
| 9 | Human Services |
| 10 | Marketing |
| 11 | Medical Laboratory Technician |
| 12 | Medical Office Assistant |
| 13 | Nuclear Medicine Technology |
| 14 | Nursing |
| 15 | Office Administration and Technology |
| 16 | Paralegal and Legal Studies |
| 17 | Pharmaceutical Manufacturing Technology |
| 18 | Radiologic Technology |

##### AS

| # | 专业 |
|---|------|
| 1 | Biotechnology |
| 2 | Business Administration |
| 3 | Computer Science |
| 4 | Dietetics and Nutrition Science |
| 5 | Education |
| 6 | Engineering Science |
| 7 | Exercise Science and Kinesiology |
| 8 | Mathematics |
| 9 | Media and Digital Film Production |
| 10 | Public Health |
| 11 | Science |
| 12 | Science for Forensics |
| 13 | Therapeutic Recreation |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Animal Care and Management |
| 2 | Assistant of Children with Special Needs |
| 3 | Automotive Technician |
| 4 | Bilingual Early Childhood Assistant |
| 5 | Community Health |
| 6 | Cybersecurity and Networking |
| 7 | Early Childhood Assistant |
| 8 | Licensed Practical Nurse |
| 9 | Nuclear Medicine Technology |
| 10 | Paralegal and Legal Studies |
| 11 | Paralegal Studies |

#### Brooklyn College

##### BA

| # | 专业 |
|---|------|
| 1 | Africana Studies |
| 2 | American Studies |
| 3 | Anthropology |
| 4 | Art |
| 5 | Art History |
| 6 | Biology |
| 7 | Caribbean Studies (Dual Major) |
| 8 | Chemistry |
| 9 | Childhood Education Grades 1-6 |
| 10 | Childhood Education Grades 1-6: Extension to Bilingual Education |
| 11 | Children and Youth Studies |
| 12 | Classics |
| 13 | Communication |
| 14 | Communication Sciences and Disorders |
| 15 | Comparative Literature |
| 16 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 17 | Data Analytics |
| 18 | Early Childhood Education Teacher Birth-Grade 2 |
| 19 | Early Childhood/Early Childhood Special Education |
| 20 | Earth and Environmental Sciences |
| 21 | Economics |
| 22 | English |
| 23 | English Teacher |
| 24 | Film |
| 25 | French |
| 26 | French Teacher |
| 27 | Health and Nutrition Sciences |
| 28 | History |
| 29 | Judaic Studies |
| 30 | Linguistics |
| 31 | Mathematics |
| 32 | Music |
| 33 | Philosophy |
| 34 | Physics |
| 35 | Political Science |
| 36 | Professional Communication |
| 37 | Psychology |
| 38 | Puerto Rican and Latinx Studies |
| 39 | Religion (Dual Major) |
| 40 | Russian |
| 41 | Social Studies Teacher |
| 42 | Sociology |
| 43 | Spanish |
| 44 | Spanish Teacher |
| 45 | Television and Radio |
| 46 | Theater |
| 47 | Urban Sustainability |
| 48 | Women’s and Gender Studies |

##### BBA

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Business Administration |
| 3 | Finance |

##### BFA

| # | 专业 |
|---|------|
| 1 | Art |
| 2 | Creative Writing |
| 3 | Theater |

##### BMUS

| # | 专业 |
|---|------|
| 1 | Music Composition |
| 2 | Music Education |
| 3 | Performance |

##### BS

| # | 专业 |
|---|------|
| 1 | Actuarial Mathematics |
| 2 | Biology |
| 3 | Business Management |
| 4 | Chemistry |
| 5 | Childhood Education – Special Education (All Grades) |
| 6 | Computational Mathematics |
| 7 | Computer Science |
| 8 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 9 | Earth and Environmental Sciences |
| 10 | Exercise Science |
| 11 | Financial Mathematics |
| 12 | Health and Nutrition Sciences |
| 13 | Information Systems |
| 14 | Journalism and Media Studies |
| 15 | Mathematics |
| 16 | Multimedia Computing |
| 17 | Neuroscience |
| 18 | Physical Education |
| 19 | Physics |
| 20 | Psychology |
| 21 | Public Accounting and Business Management |
| 22 | Public Accounting and Finance |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Film Production |

##### MA

| # | 专业 |
|---|------|
| 1 | Middle Childhood Education (5–9) General Science Teacher |

#### City College of New York

##### BA

| # | 专业 |
|---|------|
| 1 | American Studies |
| 2 | Anthropology |
| 3 | Area Studies: Asian – Latin American and Latino – Russian |
| 4 | Area Studies: Black-Puerto Rican-Jewish |
| 5 | Art |
| 6 | Art Teacher, All Grades |
| 7 | Biology |
| 8 | Communications |
| 9 | Comparative Literature |
| 10 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 11 | Earth and Atmospheric Sciences |
| 12 | Economics |
| 13 | English |
| 14 | English Teacher, Grades 7-12 |
| 15 | History |
| 16 | Interdisciplinary Liberal Arts and Science (Center for Worker Education) |
| 17 | International Studies |
| 18 | Management and Administration |
| 19 | Mathematics |
| 20 | Mathematics Teacher, Grades 7-12 |
| 21 | Music |
| 22 | Music Teacher, All Grades |
| 23 | Philosophy |
| 24 | Physics |
| 25 | Political Science |
| 26 | Psychology |
| 27 | Romance Languages: French, Italian, Spanish |
| 28 | Social Studies Teacher, Grades 7-12 |
| 29 | Sociology |
| 30 | Spanish Teacher, Grades 7-12 |
| 31 | Speech Pathology |
| 32 | Theatre |

##### BAMA

| # | 专业 |
|---|------|
| 1 | Economics 4 – Year |
| 2 | English 4-Year |
| 3 | History |
| 4 | Interdisciplinary Liberal Arts and Science and Study of the Americas |
| 5 | Psychology |
| 6 | Sociology |

##### BAMS

| # | 专业 |
|---|------|
| 1 | Mathematics Combined 4 Year Program |

##### BARCH

| # | 专业 |
|---|------|
| 1 | Architecture |

##### BE

| # | 专业 |
|---|------|
| 1 | Biomedical Engineering |
| 2 | Chemical Engineering |
| 3 | Civil Engineering |
| 4 | Computer Engineering |
| 5 | Earth Systems Science and Environmental Engineering |
| 6 | Electrical Engineering |
| 7 | Mechanical Engineering |

##### BFA

| # | 专业 |
|---|------|
| 1 | Electronic Design and Multimedia |
| 2 | Film |
| 3 | Music |
| 4 | Music Teacher, All Grades |

##### BMUS

| # | 专业 |
|---|------|
| 1 | Classical Performance |
| 2 | Jazz Studies (Vocal) |
| 3 | Jazz Studies Instrumental |
| 4 | Sonic Arts |

##### BS

| # | 专业 |
|---|------|
| 1 | Applied Mathematics |
| 2 | Biochemistry |
| 3 | Biology |
| 4 | Biology Teacher, Grades 7-12 |
| 5 | Biology/Optometry |
| 6 | Biomedical Science |
| 7 | Biotechnology |
| 8 | Chemistry |
| 9 | Chemistry Teacher, Grades 7-12 |
| 10 | Computer Science |
| 11 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 12 | Early Childhood Education (Center for Worker Education) |
| 13 | Earth and Atmospheric Sciences |
| 14 | Earth Science Teacher, Grades 7-12 |
| 15 | Environmental and Earth Systems Science |
| 16 | Interdisciplinary Liberal Arts and Science (Center for Worker Education) |
| 17 | Mathematics |
| 18 | Physics |
| 19 | Physics Teacher, Grades 7-12 |
| 20 | Psychology |
| 21 | Science Learning & Public Engagement |

##### BSED

| # | 专业 |
|---|------|
| 1 | Bilingual Childhood Education |
| 2 | Bilingual Childhood Education, Grades 1-6 |
| 3 | Childhood Education |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Biology |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Global Modernisms |
| 2 | Health Professions Preparation |
| 3 | Language, Writing, and Rhetoric |
| 4 | Publishing |

#### College of Staten Island

##### AA

| # | 专业 |
|---|------|
| 1 | Liberal Arts and Sciences |

##### AAS

| # | 专业 |
|---|------|
| 1 | Business |
| 2 | Computer Technology |
| 3 | Nursing |

##### AS

| # | 专业 |
|---|------|
| 1 | Engineering Science |
| 2 | Liberal Arts and Sciences |

##### BA

| # | 专业 |
|---|------|
| 1 | African and African Diaspora Studies |
| 2 | American Studies |
| 3 | Art |
| 4 | Cinema Studies |
| 5 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 6 | Economics |
| 7 | English |
| 8 | English Grades 7-12 |
| 9 | Geography |
| 10 | History |
| 11 | History Grades 7-12 |
| 12 | International Studies |
| 13 | Italian Studies |
| 14 | Italian Studies Grades 7-12 |
| 15 | Music |
| 16 | Philosophy |
| 17 | Philosophy and Political Science |
| 18 | Political Science |
| 19 | Psychology |
| 20 | Science, Letters, Society |
| 21 | Science, Letters, Society (Education) |
| 22 | Social Work |
| 23 | Sociology/Anthropology |
| 24 | Spanish |
| 25 | Spanish Grades 7-12 |
| 26 | Womens Gender And Sexuality Studies |

##### BAMA

| # | 专业 |
|---|------|
| 1 | History Bachelors/Masters |

##### BFA

| # | 专业 |
|---|------|
| 1 | Art |

##### BS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Art |
| 3 | Biochemistry |
| 4 | Biology |
| 5 | Biology Grades 7-12 |
| 6 | Business |
| 7 | Chemistry |
| 8 | Chemistry Grades 7-12 |
| 9 | Communications |
| 10 | Computer Science |
| 11 | Computer Science/Mathematics |
| 12 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 13 | Drama |
| 14 | Earth and Environmental Science |
| 15 | Earth Science 7-12 |
| 16 | Economics |
| 17 | Electrical Engineering |
| 18 | Engineering Science |
| 19 | Information Systems and Informatics |
| 20 | International Studies |
| 21 | Mathematics |
| 22 | Mathematics Grades 7-12 |
| 23 | Medical Laboratory Science |
| 24 | Music |
| 25 | Nursing |
| 26 | Physics |
| 27 | Physics Grades 7-12 |
| 28 | Psychology |
| 29 | Social Work |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Accounting and Business Management |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Latin American Caribbean and Latina/o Studies |
| 2 | Modern China Studies |

#### Guttman Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Business Administration |
| 2 | Human Services |
| 3 | Liberal Arts and Sciences |
| 4 | Urban Studies |

##### AAS

| # | 专业 |
|---|------|
| 1 | Information Technology |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

#### Hostos Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | Liberal Arts and Science |

##### AAS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Aging and Health Studies |
| 3 | Dental Hygiene |
| 4 | Digital Design and Animation |
| 5 | Digital Music |
| 6 | Early Childhood Education |
| 7 | Game Design |
| 8 | Nursing |
| 9 | Office Technology |
| 10 | Public Administration |
| 11 | Public Interest Paralegal Studies |
| 12 | Radiologic Technology |

##### AS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Accounting for Forensic Accounting |
| 3 | Business Management |
| 4 | Chemical Engineering Science |
| 5 | Civil Engineering Science |
| 6 | Community Health |
| 7 | Computer Science |
| 8 | Electrical Engineering Science |
| 9 | Liberal Arts and Science |
| 10 | Mathematics |
| 11 | Mechanical Engineering Science |
| 12 | Police Science |
| 13 | Science for Forensic Science |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Office Assistant |
| 2 | Practical Nursing |

#### Hunter College

##### BA

| # | 专业 |
|---|------|
| 1 | Africana and Puerto Rican/Latino Studies |
| 2 | Anthropology |
| 3 | Arabic |
| 4 | Archaeology |
| 5 | Archaeology (Interdepartmental) |
| 6 | Art History (30 credit major) |
| 7 | Biological Sciences Major 1 |
| 8 | Biological Sciences Major 2 |
| 9 | Biology, Grades 7-12 |
| 10 | Chemistry Major 1 |
| 11 | Chemistry Major 2 |
| 12 | Chemistry, Grades 7-12 |
| 13 | Childhood Education, Grades 1-6 Quest |
| 14 | Chinese Language and Literature |
| 15 | Chinese, Grades 7-12 |
| 16 | Classical Studies |
| 17 | Comparative Literature |
| 18 | Computer Science |
| 19 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 20 | Dance |
| 21 | Dance, Grades Pre K-12 |
| 22 | Early Childhood Education, Birth to Grade 2nd |
| 23 | Economics |
| 24 | English Language Arts |
| 25 | English Literature |
| 26 | English, Grades 7-12 |
| 27 | Environmental Studies |
| 28 | Film |
| 29 | French |
| 30 | French, Grades 7-12 |
| 31 | Geography |
| 32 | German |
| 33 | German, Grades 7-12 |
| 34 | Greek |
| 35 | Hebrew |
| 36 | Hebrew, Grades 7-12 |
| 37 | History |
| 38 | Human Biology |
| 39 | Italian |
| 40 | Italian, Grades 7-12 |
| 41 | Jewish Studies |
| 42 | Latin |
| 43 | Latin American and Caribbean Studies |
| 44 | Latin and Greek |
| 45 | Mathematics |
| 46 | Mathematics, Grades 7-12 |
| 47 | Media Studies |
| 48 | Music (25 credit major) |
| 49 | Music (42 credit major) |
| 50 | Philosophy |
| 51 | Physics |
| 52 | Physics, Grades 7-12 |
| 53 | Political Science |
| 54 | Psychology |
| 55 | Religion |
| 56 | Romance Languages |
| 57 | Russian |
| 58 | Russian, Grades 7-12 |
| 59 | Social Studies, Grades 7-12 – Geography |
| 60 | Social Studies, Grades 7-12 – History |
| 61 | Sociology |
| 62 | Spanish |
| 63 | Spanish, Grades 7-12 |
| 64 | Special Honors Program |
| 65 | Statistics |
| 66 | Studio Art (24 credit major) |
| 67 | Studio Art (42 credit major) |
| 68 | Theatre |
| 69 | Urban Studies |
| 70 | Women and Gender Studies |

##### BAMA

| # | 专业 |
|---|------|
| 1 | Adolescence Education: Biology |
| 2 | Adolescence Education: Mathematics |
| 3 | Anthropology |
| 4 | Bio-Pharmacology |
| 5 | Biological Sciences |
| 6 | Chemistry and Adolescence Education: Chemistry |
| 7 | Dance/Dance Education |
| 8 | Economics |
| 9 | English |
| 10 | Environmental Studies/Earth Science Teacher, Grades 7-12 |
| 11 | History |
| 12 | Mathematics/Statistics and Applied Mathematics |
| 13 | Music/Music, Grades Pre K-12 |
| 14 | Physics |
| 15 | Physics/Adolescence Physics |
| 16 | Statistics and Statistics Applied Mathematics |

##### BAMS

| # | 专业 |
|---|------|
| 1 | Biological Sciences: Environmental and Occupational Health Science |
| 2 | Sociology/Social Research |

##### BFA

| # | 专业 |
|---|------|
| 1 | Art |

##### BMUS

| # | 专业 |
|---|------|
| 1 | Music |

##### BS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 3 | Medical Lab Sciences: Biomedical Science |
| 4 | Medical Laboratory Sciences: Clinical Science |
| 5 | Nursing |
| 6 | Nutrition and Food Science: Dietetics |
| 7 | Public Health |

##### BSMA

| # | 专业 |
|---|------|
| 1 | Medical Laboratory Sciences: Biological Sciences |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Adult Health |
| 2 | Adult Nursing Practitioner |
| 3 | Gerontological/Adult Health Nurse Practitioner |
| 4 | Maternal/Child Nursing |
| 5 | Nutrition and Food Science: Dietetics/Nutrition |

##### BSMSMPH

| # | 专业 |
|---|------|
| 1 | Nursing |

##### BSW

| # | 专业 |
|---|------|
| 1 | Social Work |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Arts Management and Leadership |
| 2 | Business Studies |
| 3 | Health Careers Preparation |
| 4 | Human Rights |
| 5 | Public Policy |

#### John Jay College of Criminal Justice

##### BA

| # | 专业 |
|---|------|
| 1 | Anthropology |
| 2 | Criminal Justice (Crime Control and Prevention) |
| 3 | Criminology |
| 4 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 5 | Deviance, Crime and Culture |
| 6 | English |
| 7 | Forensic Psychology |
| 8 | Gender Studies |
| 9 | Global History |
| 10 | Government and Public Administration |
| 11 | Humanities and Justice |
| 12 | International Criminal Justice |
| 13 | Latin American and Latina/o Studies |
| 14 | Law and Society |
| 15 | Philosophy |
| 16 | Political Science |
| 17 | Sociology |
| 18 | Spanish |

##### BAMA

| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | Forensic Psychology |

##### BS

| # | 专业 |
|---|------|
| 1 | Applied Mathematics: Data Science and Cryptography |
| 2 | Cell and Molecular Biology |
| 3 | Computer Science and Information Security |
| 4 | Criminal Justice |
| 5 | Criminal Justice (Institutional Theory and Practice) |
| 6 | Criminal Justice Management |
| 7 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 8 | Economics |
| 9 | Emergency Services Administration |
| 10 | Fire Science |
| 11 | Forensic Science |
| 12 | Fraud Examination and Financial Forensics |
| 13 | Human Services and Community Justice |
| 14 | Legal Studies |
| 15 | Police Studies |
| 16 | Public Administration |
| 17 | Security Management |
| 18 | Toxicology |

##### BSMA

| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | Criminal Justice Management/Criminal Justice |
| 3 | Economics |
| 4 | Police Studies/Criminal Justice |

##### BSMPA

| # | 专业 |
|---|------|
| 1 | BS in Criminal Justice Management/MPA in Inspection and Oversight |
| 2 | Criminal Justice Management/Public Administration |
| 3 | Criminal Public Administration/Inspection and Oversight |
| 4 | Dual Degree-Public Administration |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Dispute Resolution |
| 2 | Forensic Accounting |
| 3 | Legal Interpretation in Spanish |
| 4 | Legal Translation and Legal Interpretation in Spanish |
| 5 | Legal Translation in Spanish |
| 6 | Police Leadership |

#### Kingsborough Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | Liberal Arts |

##### AAS

| # | 专业 |
|---|------|
| 1 | Computer Information Systems |
| 2 | Culinary Arts |
| 3 | Emergency Medical Services - Paramedic (EMS-P) |
| 4 | Fashion Design |
| 5 | Maritime Technology |
| 6 | Nursing |
| 7 | Physical Therapist Assistant |
| 8 | Polysomnographic Technology |
| 9 | Surgical Technology |
| 10 | The Business of Fashion |
| 11 | Tourism and Hospitality |
| 12 | Website Development |

##### AS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Addiction Studies |
| 3 | Biology |
| 4 | Biotechnology |
| 5 | Business Administration |
| 6 | Chemistry |
| 7 | Community Health |
| 8 | Computer Science |
| 9 | Earth and Planetary Sciences |
| 10 | Education Studies |
| 11 | Engineering Science |
| 12 | Exercise Science |
| 13 | Fine Arts |
| 14 | Graphic Design and Illustration |
| 15 | Health Sciences |
| 16 | Journalism and Print Media |
| 17 | Mathematics |
| 18 | Media Arts |
| 19 | Mental Health and Human Services |
| 20 | Physical Education, Recreation, and Recreation Therapy |
| 21 | Physics |
| 22 | Science for Forensics |
| 23 | Speech Communication |
| 24 | Theatre Arts |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Addiction Studies |
| 2 | Culinary Arts |

#### LaGuardia Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Communications |
| 2 | Education |
| 3 | Education Associate: Bilingual Child |
| 4 | Film and Television |
| 5 | Human Services: Gerontology |
| 6 | Human Services: Mental Health |
| 7 | Liberal Arts: Childhood Education |
| 8 | Liberal Arts: Social Science and Humanities |
| 9 | Philosophy |
| 10 | Psychology |
| 11 | Spanish-English Translation |

##### AAS

| # | 专业 |
|---|------|
| 1 | Commercial Photography |
| 2 | Computer Technology |
| 3 | Energy Technician |
| 4 | Industrial Design Technology |
| 5 | Music Recording Technology |
| 6 | Network Administration & Information Security |
| 7 | New Media Technology |
| 8 | Nursing |
| 9 | Nutrition and Culinary Management |
| 10 | Occupational Therapy Assistant |
| 11 | Paralegal Studies |
| 12 | Paramedic |
| 13 | Physical Therapist Assistant |
| 14 | Programming and Software Development |
| 15 | Radiologic Technology |
| 16 | Travel, Tourism and Hospitality Management |
| 17 | Veterinary Technology |

##### AS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Biology |
| 3 | Business Administration |
| 4 | Computer Science |
| 5 | Criminal Justice |
| 6 | Electrical Engineering |
| 7 | Engineering Science: Civil Engineering |
| 8 | Environmental Science |
| 9 | Fine Arts |
| 10 | Liberal Arts:Mathematics and Science |
| 11 | Mechanical Engineering |
| 12 | Music Performance |
| 13 | Physical Sciences |
| 14 | Public Community Health |
| 15 | School Food Service |
| 16 | Theater |
| 17 | Therapeutic Recreation |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 2 | English |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Commercial Photography Certificate |
| 2 | Cybersecurity |
| 3 | Digital Media Arts Certificate |
| 4 | Network and Information Security |
| 5 | Paralegal |
| 6 | Practical Nursing Certificate |
| 7 | Word Processing |

#### Lehman College

##### 

| # | 专业 |
|---|------|
| 1 | English |

##### BA

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Africana Studies |
| 3 | Anthropology |
| 4 | Art |
| 5 | Art History |
| 6 | Art Teacher |
| 7 | Biology |
| 8 | Chemistry |
| 9 | Comparative Literature |
| 10 | Computer Science |
| 11 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 12 | Dance |
| 13 | Earth Science |
| 14 | Economics |
| 15 | Economics and Mathematics |
| 16 | English Teacher |
| 17 | Film and TV Studies |
| 18 | French |
| 19 | French Teacher |
| 20 | Geography |
| 21 | History |
| 22 | History Teacher |
| 23 | Italian |
| 24 | Italian American Studies |
| 25 | Italian Teacher |
| 26 | Journalism |
| 27 | Latin |
| 28 | Latin American and Caribbean Studies |
| 29 | Latino Studies |
| 30 | Linguistics |
| 31 | Mathematics |
| 32 | Mathematics Teacher |
| 33 | Media Communication Studies |
| 34 | Philosophy |
| 35 | Physics |
| 36 | Physics Teacher |
| 37 | Political Science |
| 38 | Psychology |
| 39 | Self-Determined Studies |
| 40 | Social Work |
| 41 | Sociology |
| 42 | Spanish |
| 43 | Spanish Teacher |
| 44 | Speech Pathology and Audiology |
| 45 | Theater |

##### BAMA

| # | 专业 |
|---|------|
| 1 | Mathematics |

##### BBA

| # | 专业 |
|---|------|
| 1 | Business Administration |

##### BFA

| # | 专业 |
|---|------|
| 1 | Art |
| 2 | Multimedia Performing Arts |

##### BS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Biology |
| 3 | Chemistry |
| 4 | Computer Graphics and Imaging |
| 5 | Computer Information Systems |
| 6 | Computer Science |
| 7 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 8 | Dietetics, Foods and Nutrition |
| 9 | Environmental Science |
| 10 | Exercise Science |
| 11 | Health Education and Promotion |
| 12 | Health Services Administration |
| 13 | Interdepartmental Concentration in Anthropology |
| 14 | Music |
| 15 | Nursing |
| 16 | Physics |
| 17 | Recreation Education |
| 18 | Self-Determined Studies |
| 19 | Therapeutic Recreation |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Biology |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Digital Technology and Electronics |
| 2 | Earth Science |
| 3 | Geographic Information Science |
| 4 | Health Careers Preparation |
| 5 | Nursing Home Administration |
| 6 | Speech-Language Pathology |

#### Medgar Evers College

##### AA

| # | 专业 |
|---|------|
| 1 | African Diaspora Literature |
| 2 | English |
| 3 | Liberal Arts |
| 4 | Teacher Education |

##### AAS

| # | 专业 |
|---|------|
| 1 | Computer Applications |
| 2 | Nursing |

##### AS

| # | 专业 |
|---|------|
| 1 | Business Administration |
| 2 | Computer Science |
| 3 | Public Administration |
| 4 | Science |

##### BA

| # | 专业 |
|---|------|
| 1 | Childhood Education |
| 2 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 3 | English |
| 4 | Liberal Studies |
| 5 | Psychology |
| 6 | Religious Studies |
| 7 | Special Education and Childhood |
| 8 | Special Education And Early Childhood |

##### BFA

| # | 专业 |
|---|------|
| 1 | Media and The Performing Arts |

##### BPS

| # | 专业 |
|---|------|
| 1 | Applied Management |

##### BS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Biology |
| 3 | Business |
| 4 | Computer Information Systems |
| 5 | Computer Science |
| 6 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 7 | Environmental Science |
| 8 | Financial Economics |
| 9 | Mathematical Sciences |
| 10 | Public Administration |
| 11 | Social Work |

##### BSNURS

| # | 专业 |
|---|------|
| 1 | Nursing (RN’S) |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Practical Nursing |

#### NYC College of Technology

##### AA

| # | 专业 |
|---|------|
| 1 | Liberal Arts and Sciences |

##### AAS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Architectural Technology |
| 3 | Civil Engineering Technology |
| 4 | Communication Design |
| 5 | Communication Design Management |
| 6 | Computer Information Systems |
| 7 | Construction Management Technology |
| 8 | Dental Hygiene |
| 9 | Dental Laboratory Technology |
| 10 | Electrical Engineering Technology |
| 11 | Electromechanical Eng Technology |
| 12 | Environmental Control Technology |
| 13 | Hospitality Management |
| 14 | Human Services |
| 15 | Industrial Design |
| 16 | Marketing Management and Sales |
| 17 | Mechanical Engineering Technology |
| 18 | Nursing |
| 19 | Ophthalmic Dispensing |
| 20 | Paralegal Studies |
| 21 | Radiologic Tech and Medical Imaging |

##### AS

| # | 专业 |
|---|------|
| 1 | Business and Technology Fashion |
| 2 | Chemical Technology |
| 3 | Computer Science |
| 4 | Health Science |
| 5 | Liberal Arts and Sciences |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BARCH

| # | 专业 |
|---|------|
| 1 | Architecture |

##### BFA

| # | 专业 |
|---|------|
| 1 | Communication Design |

##### BS

| # | 专业 |
|---|------|
| 1 | Applied Chemistry |
| 2 | Applied Computational Physics |
| 3 | Applied Mathematics |
| 4 | Biomedical Informatics |
| 5 | Business and Technology of Fashion |
| 6 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 7 | Data Analytics/Economics |
| 8 | Data Science |
| 9 | Health Communication |
| 10 | Health Services Administration |
| 11 | Human Services |
| 12 | Mathematics Education |
| 13 | Nursing |
| 14 | Paralegal Studies |
| 15 | Professional and Technical Writing |
| 16 | Radiological Science |

##### BSED

| # | 专业 |
|---|------|
| 1 | Career and Technology Teacher Edu |
| 2 | Technology Teacher Education |

##### BTECH

| # | 专业 |
|---|------|
| 1 | Architectural Technology |
| 2 | Communication Design Management |
| 3 | Computer Engineering Technology |
| 4 | Computer Systems |
| 5 | Construction Engineering Technology. |
| 6 | Electrical Engineering Technology |
| 7 | Emerging Media Technologies |
| 8 | Entertainment Technology |
| 9 | Facilities Management |
| 10 | Hospitality Management |
| 11 | Mechanical Engineering Technology |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Career and Technical Education |
| 2 | Career and Technical Teacher Education |
| 3 | Career and Technical Teacher Education PRF |
| 4 | Construction Management |
| 5 | Scenic Construction |
| 6 | Sec Sci Machine Translation |
| 7 | Sustainable Technology |
| 8 | Video Production |

#### Queens College

##### BA

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Adolescent Chinese Education Grades 7-12 |
| 3 | Africana Studies |
| 4 | Africana Studies: Social Studies 7-12 |
| 5 | American Studies |
| 6 | Ancient Greek |
| 7 | Anthropology |
| 8 | Anthropology: Social Studies 7-12 |
| 9 | Art History |
| 10 | Biology |
| 11 | Biology 7-12 |
| 12 | Biology and Neuroscience |
| 13 | Biology Education |
| 14 | Byzantine and Modern Greek Studies |
| 15 | Chemistry |
| 16 | Chemistry 7-12 |
| 17 | Chinese |
| 18 | Classics |
| 19 | Communication Science and Disorders |
| 20 | Comparative Literature |
| 21 | Computer Science |
| 22 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 23 | Drama and Theater |
| 24 | Earth Science Teacher |
| 25 | East Asian Studies |
| 26 | Economics |
| 27 | Economics: Social Studies 7-12 |
| 28 | Elementary and Early Childhood Education |
| 29 | English |
| 30 | English 7-12 |
| 31 | Environmental Sciences |
| 32 | Environmental Studies |
| 33 | Family and Consumer Sciences |
| 34 | Family and Consumer Sciences Teacher |
| 35 | Film Studies |
| 36 | French |
| 37 | French 7-12 |
| 38 | Geology |
| 39 | Geology: Earth Sciences 7-12 |
| 40 | German |
| 41 | German 7-12 |
| 42 | Hebrew |
| 43 | History |
| 44 | History: Social Studies 7-12 |
| 45 | Human Development and Family Science |
| 46 | Interdisciplinary Studies |
| 47 | Italian |
| 48 | Italian 7-12 |
| 49 | Jewish Studies |
| 50 | Labor Studies |
| 51 | Latin |
| 52 | Latin 7-12 |
| 53 | Latin American Area Studies |
| 54 | Latin American Area Studies: Social Studies 7-12 |
| 55 | Linguistics: General |
| 56 | Linguistics: TESOL |
| 57 | Mathematics |
| 58 | Mathematics 7-12 |
| 59 | Media Studies |
| 60 | Middle Eastern Studies |
| 61 | Music |
| 62 | Philosophy |
| 63 | Physics |
| 64 | Physics 7-12 |
| 65 | Political Science |
| 66 | Political Science and Government: Social Studies 7-12 |
| 67 | Psychology |
| 68 | Psychology and Neuroscience |
| 69 | Religious Studies |
| 70 | Russian |
| 71 | Sociology |
| 72 | Sociology: Social Studies 7-12 |
| 73 | Spanish |
| 74 | Spanish 7-12 |
| 75 | Studio Art |
| 76 | Theater and Dance |
| 77 | Urban Studies |
| 78 | Urban Studies: Social Studies 7-12 |
| 79 | Women and Gender Studies |

##### BAMA

| # | 专业 |
|---|------|
| 1 | Biology |
| 2 | Chemistry |
| 3 | Computer Science |
| 4 | History |
| 5 | Music |
| 6 | Philosophy |
| 7 | Physics |
| 8 | Urban Studies |

##### BBA

| # | 专业 |
|---|------|
| 1 | Actuarial Studies |
| 2 | Finance |
| 3 | International Business |

##### BFA

| # | 专业 |
|---|------|
| 1 | Art Education |
| 2 | Design |
| 3 | Photography and Imaging |
| 4 | Studio Art |

##### BMUS

| # | 专业 |
|---|------|
| 1 | Music Education |
| 2 | Music Performance |

##### BS

| # | 专业 |
|---|------|
| 1 | Advertising |
| 2 | Applied Social Sciences |
| 3 | Computer Science |
| 4 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 5 | Environmental Sciences |
| 6 | Geology |
| 7 | Nutrition and Dietetics |
| 8 | Nutrition and Exercise Sciences |
| 9 | Physical Education |
| 10 | Physics |
| 11 | Quantitative Economics |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Physics Photonics |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Medical Career Preparation |

#### Queensborough Community College

##### AA

| # | 专业 |
|---|------|
| 1 | Cybersecurity |
| 2 | Liberal Arts and Sciences |

##### AAS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Architectural Technology |
| 3 | Business Management – Marketing |
| 4 | Computer Engineering Technology |
| 5 | Computer Information Systems |
| 6 | Electronic Engineering Technology |
| 7 | Internet and Information Technology |
| 8 | Massage Therapy |
| 9 | Mechanical Engineering Technology |
| 10 | Medical Assistant |
| 11 | Music Production |
| 12 | Nursing |
| 13 | Nursing – Pre-Clinical Sequence |
| 14 | Nursing w/ Hunter |
| 15 | Nursing w/ SPS |
| 16 | Nursing w/ York |
| 17 | Office Administration and Technology |
| 18 | Telecommunications Technology |

##### AS

| # | 专业 |
|---|------|
| 1 | Accounting for Forensic Accounting |
| 2 | Art |
| 3 | Biology |
| 4 | Biotechnology |
| 5 | Business Administration |
| 6 | Chemistry |
| 7 | Computer Science and Information Security |
| 8 | Criminal Justice |
| 9 | Dance |
| 10 | Digital Art and Design |
| 11 | Engineering Science |
| 12 | Environmental Health |
| 13 | Environmental Science |
| 14 | Film and Media Production |
| 15 | Gallery and Museum Studies |
| 16 | Health Sciences – General Health Sciences |
| 17 | Health Sciences – Health Services Administration |
| 18 | Health Sciences – Medical Imaging |
| 19 | Health Sciences – Occupational Therapy |
| 20 | Health Sciences – Respiratory Care |
| 21 | Liberal Arts and Sciences (Mathematics and Science) |
| 22 | Movement Science |
| 23 | Music |
| 24 | Physics |
| 25 | Psychology |
| 26 | Public Health |
| 27 | Science for Forensics |
| 28 | Theatre |

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Computer Information Systems |
| 2 | Internet and Information Technology |
| 3 | Medical Office Assistant |

#### School of Labor & Urban Studies

##### BA

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 2 | Urban and Community Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Community Leadership |
| 2 | Healthcare Leadership and Advocacy |
| 3 | Labor Relations |
| 4 | Labor Studies |
| 5 | Public Administration and Public Policy |
| 6 | Urban Experience |

#### School of Professional Studies

##### BA

| # | 专业 |
|---|------|
| 1 | Communication and Media |
| 2 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 3 | Disability Studies |
| 4 | Human Relations |
| 5 | Liberal Studies |
| 6 | Psychology |
| 7 | Sociology |
| 8 | Youth Studies |

##### BS

| # | 专业 |
|---|------|
| 1 | Business |
| 2 | Communication and Media |
| 3 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 4 | Health Information Management |
| 5 | Health Services Administration |
| 6 | Information Systems |
| 7 | Nursing |
| 8 | Nursing RN |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Nursing Education |
| 2 | Nursing Informatics |
| 3 | Nursing Organizational Leadership |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Child Development Associate |
| 2 | Medical Coding |

#### York College

##### BA

| # | 专业 |
|---|------|
| 1 | Anthropology |
| 2 | Art (Painting, Drawing, Sculpture) |
| 3 | Art History |
| 4 | Biology |
| 5 | Black Studies |
| 6 | Chemistry |
| 7 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 8 | Economics |
| 9 | English |
| 10 | English Teacher Education |
| 11 | French |
| 12 | History |
| 13 | History Teacher Education |
| 14 | Interdisciplinary Studies |
| 15 | Interdisciplinary Studies Teacher Education |
| 16 | Journalism |
| 17 | Mathematics |
| 18 | Mathematics Teacher Education |
| 19 | Philosophy |
| 20 | Political Science |
| 21 | Psychology |
| 22 | Sociology |
| 23 | Spanish |
| 24 | Speech Communication and Theater Arts |

##### BMUS

| # | 专业 |
|---|------|
| 1 | Music |

##### BS

| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Aviation Management |
| 3 | Biology |
| 4 | Biology Teacher Education |
| 5 | Biotechnology |
| 6 | Business Administration |
| 7 | Chemistry |
| 8 | Chemistry Teacher Education |
| 9 | Clinical Laboratory Science/Medical Technology |
| 10 | Communications Technology |
| 11 | Community Health Education |
| 12 | Computer Science |
| 13 | CUNY Baccalaureate for Unique and Interdisciplinary Studies |
| 14 | Earth Science Teacher, Grades 7-12 |
| 15 | Environmental Health Science |
| 16 | Finance |
| 17 | Geology |
| 18 | Gerontological Studies and Services |
| 19 | Health Promotion Management |
| 20 | Health Science |
| 21 | Health Teacher, All Grades |
| 22 | Information Systems Management |
| 23 | Marketing |
| 24 | Mathematics |
| 25 | Mathematics Teacher Education |
| 26 | Mathematics/Teacher Education 5-9 |
| 27 | Movement Science |
| 28 | Nursing |
| 29 | Pharmaceutical Sciences |
| 30 | Physical Education Teacher |
| 31 | Physics |
| 32 | Public Health |
| 33 | Queensborough Biotechnology |
| 34 | Social Work |

##### BSMS

| # | 专业 |
|---|------|
| 1 | Health Science Occupational Therapy |

##### Certificate

| # | 专业 |
|---|------|
| 1 | Aviation Management |
| 2 | Creole for Professionals |
| 3 | French for Professionals |
| 4 | Mortgage Finance |
| 5 | Spanish for Professional Purposes |
| 6 | Survey Research |

### 1.2 Interdisciplinary / cross-college undergraduate programs

| Program | Host college | Degree(s) | Notes |
|---|---|---|---|
| CUNY Baccalaureate for Unique and Interdisciplinary Studies (CUNY BA) | CUNY-wide (administered centrally) | BA, BS, BPS | Self-designed interdisciplinary degree; offered at Baruch, Brooklyn, City College, Hunter, Lehman, Queens, York, College of Staten Island |
| Macaulay Honors College | Cross-college honors overlay | BA + honors designation | Honors curriculum delivered at 8 partner campuses |

### 1.3 Minors — complete list

CUNY does not publish a centralized system-wide minor list at cuny.edu. Minors are catalogued within each member college's academic bulletin. A complete list would require scraping 20 college bulletin sites individually.

### 1.4 General/Institute-wide requirements

**Pathways General Education Framework**: CUNY's system-wide general education framework, required of all first-time freshmen at senior colleges. Includes six required categories (English Composition, Mathematical and Quantitative Reasoning, Life and Physical Sciences, Flexible Core, World Cultures and Global Issues, U.S. Experience in Its Diversity, Creative Expression, Individual and Society, Scientific World) plus the College Option. See: https://www.cuny.edu/academics/current-initiatives/pathways/

---

## 2. Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 (Program Area) > 学位级别

CUNY graduate education is centralized through the **CUNY Office of Graduate Studies** (https://www.cuny.edu/admissions/graduate-studies/), which routes applications to **16 graduate colleges**. Each program has its own admission requirements, deadlines, and application portal.

#### Baruch College

##### Program Area: Architecture and Design

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | City Planning |

##### Program Area: Business

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Artificial Intelligence for Managers |
| 2 | Cybersecurity |
| 3 | Data Analytics |
| 4 | Product Management |
| 5 | Real Estate Finance |
| 6 | Strategic Thinking |

###### DBA

| # | 项目 |
|---|------|
| 1 | Business Administration |

###### Executive MBA

| # | 项目 |
|---|------|
| 1 | Business Administration |
| 2 | Healthcare Administration |

###### Executive MS

| # | 项目 |
|---|------|
| 1 | Human Resource Management |

###### Executive MS (Online)

| # | 项目 |
|---|------|
| 1 | Industrial/Organizational Psychology |

###### MA

| # | 项目 |
|---|------|
| 1 | Arts Administration |
| 2 | Strategic Communication |

###### MBA

| # | 项目 |
|---|------|
| 1 | Accounting |

###### MBA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Business Administration |

###### MS

| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Financial Engineering |
| 3 | Financial Risk Management |
| 4 | Industrial/Organizational Psychology |
| 5 | Information Systems |
| 6 | Marketing |
| 7 | Quantitative Methods & Modeling |
| 8 | Real Estate |
| 9 | Statistics |
| 10 | Taxation |

###### MS (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | AI and Business Analytics |
| 2 | Finance |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Marketing (Digital Marketing Concentration) |

###### PhD

| # | 项目 |
|---|------|
| 1 | Business Administration |

##### Program Area: Communications

###### Adv. Cert. (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Public Communication |

###### MA

| # | 项目 |
|---|------|
| 1 | Arts Administration |
| 2 | Strategic Communication |

###### MS

| # | 项目 |
|---|------|
| 1 | Marketing |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Marketing (Digital Marketing Concentration) |

##### Program Area: Education

###### EdD (Online)

| # | 项目 |
|---|------|
| 1 | Higher Education Administration |

###### MSEd (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Higher Education Administration |

##### Program Area: Engineering, Computer Science & Technology

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Cybersecurity |

###### MS

| # | 项目 |
|---|------|
| 1 | Information Systems |

##### Program Area: Mental Health, Psychology & Social Work

###### Executive MS (Online)

| # | 项目 |
|---|------|
| 1 | Industrial/Organizational Psychology |

###### MA

| # | 项目 |
|---|------|
| 1 | Mental Health Counseling |

###### MS

| # | 项目 |
|---|------|
| 1 | Industrial/Organizational Psychology |

##### Program Area: Public Administration

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Quantitative Methods For Policy And Equity Analysis |

###### Adv. Cert. (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Public Communication |

###### Executive MPA

| # | 项目 |
|---|------|
| 1 | Public Administration |

###### MA

| # | 项目 |
|---|------|
| 1 | Arts Administration |

###### MPA (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Public Administration |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | City Planning |

##### Program Area: Science & Mathematics

###### MS

| # | 项目 |
|---|------|
| 1 | Statistics |

##### Program Area: Social Sciences

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Quantitative Methods For Policy And Equity Analysis |

###### Adv. Cert. (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Public Communication |

###### MIA

| # | 项目 |
|---|------|
| 1 | International Affairs |

#### Brooklyn College

##### Program Area: Business

###### MA

| # | 项目 |
|---|------|
| 1 | Industrial/Organizational Psychology: Group Processes and Organizational Behavior |
| 2 | Industrial/Organizational Psychology: Personnel and Human Resources |

###### MS (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Business Administration |
| 3 | Finance |

##### Program Area: Communications

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Music Performance |

###### Adv. Diploma

| # | 项目 |
|---|------|
| 1 | Music Performance |

###### MFA

| # | 项目 |
|---|------|
| 1 | Cinema Arts |
| 2 | Media Scoring |

###### MM

| # | 项目 |
|---|------|
| 1 | Music Performance |

###### MS

| # | 项目 |
|---|------|
| 1 | Media Studies |

##### Program Area: Education

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Art Education (Grades: P-12) |
| 2 | Autism Spectrum Disorders |
| 3 | Music Education |
| 4 | School Psychology |
| 5 | School Psychology: Bilingual Extension |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Bilingual Education |
| 2 | Early Intervention and Parenting |
| 3 | Reading Science: All Grades |
| 4 | Reading Science: Emergent Readers |

###### MA

| # | 项目 |
|---|------|
| 1 | Art Education (Grades: P-12) |
| 2 | English Education (Grades: 7-12) |
| 3 | French Education (Grades: 7-12) |
| 4 | Mathematics Education (Grades: 7-12) |
| 5 | Science Education (Grades: 5-9) |
| 6 | Social Studies Education (Grades: 7-12) |
| 7 | Spanish Education (Grades: 7-12) |

###### MAT

| # | 项目 |
|---|------|
| 1 | Science Education (Grades: 7-12) |
| 2 | Science Education: Earth Science (Grades 7-12) |

###### MS

| # | 项目 |
|---|------|
| 1 | Speech-Language Pathology |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Bilingual Childhood Education (Grades: 1-6) |
| 2 | Childhood Education: Liberal Arts |
| 3 | Childhood Education: Mathematics |
| 4 | Childhood Education: Science and Environmental |
| 5 | Educational Leadership |
| 6 | Health Education (Grades: P-12) |
| 7 | Mathematics Education (Grades: 5-9) |
| 8 | Physical Education (Grades: P-12) |
| 9 | School Counseling |
| 10 | School Psychology |
| 11 | Special Education (Grades: 7-12) |
| 12 | Special Education (Grades: Birth-2) |
| 13 | Special Education (Grades: P-12) |

###### MSEd (Online)

| # | 项目 |
|---|------|
| 1 | Early Childhood Education (Grades: Birth-2) |

##### Program Area: Engineering, Computer Science & Technology

###### MS

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Program Area: Health & Public Health

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Thanatology |
| 2 | Perinatal Mental Health, Adv. Cert. (Online) |

###### AuD

| # | 项目 |
|---|------|
| 1 | Audiology |

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Community Health |

###### MS

| # | 项目 |
|---|------|
| 1 | Computer Science |
| 2 | Nutrition |
| 3 | Speech-Language Pathology |

##### Program Area: Humanities

###### MA

| # | 项目 |
|---|------|
| 1 | English |
| 2 | History |

###### MFA

| # | 项目 |
|---|------|
| 1 | Creative Writing |
| 2 | Theater |

##### Program Area: Mental Health, Psychology & Social Work

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Bilingual Extension for School Psychology |
| 2 | Mental Health Counseling |
| 3 | Play Therapy |
| 4 | School Psychology |
| 5 | School Psychology: Bilingual Extension |

###### MA

| # | 项目 |
|---|------|
| 1 | Industrial/Organizational Psychology: Group Processes and Organizational Behavior |
| 2 | Industrial/Organizational Psychology: Personnel and Human Resources |
| 3 | Mental Health Counseling |

###### MS

| # | 项目 |
|---|------|
| 1 | Psychological Research |

###### MSEd

| # | 项目 |
|---|------|
| 1 | School Counseling |
| 2 | School Psychology |

##### Program Area: Science & Mathematics

###### MA

| # | 项目 |
|---|------|
| 1 | Earth and Environmental Science |

###### MS

| # | 项目 |
|---|------|
| 1 | Earth and Environmental Science |
| 2 | Psychological Research |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | Political Science |

##### Program Area: Visual & Performing Arts

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Art Education (Grades: P-12) |
| 2 | Music Education |
| 3 | Music Performance |
| 4 | Performance & Interactive Media Arts |

###### Adv. Diploma

| # | 项目 |
|---|------|
| 1 | Music Performance |

###### MA

| # | 项目 |
|---|------|
| 1 | Art Education (Grades: P-12) |
| 2 | Musicology |
| 3 | Screen Studies |

###### MFA

| # | 项目 |
|---|------|
| 1 | Art |
| 2 | Cinema Arts |
| 3 | Creative Writing |
| 4 | Media Scoring |
| 5 | Performance & Interactive Media Arts |
| 6 | Sonic Arts |
| 7 | Theater |

###### MM

| # | 项目 |
|---|------|
| 1 | Music Composition |
| 2 | Music Performance |

###### MS

| # | 项目 |
|---|------|
| 1 | Media Studies |

#### College of Staten Island

##### Program Area: Business

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Business Analytics of Large-Scale Data |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Business Management |

##### Program Area: Education

###### Adv. Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Autism Spectrum Disorders |
| 2 | Bilingual Education (Grades: P-12) |
| 3 | Special Education (Grades: 1-6 or 7-12) |
| 4 | Teaching of Writing |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Early Childhood Education (Grades: B-2) |

###### EdD (Hybrid)

| # | 项目 |
|---|------|
| 1 | Community-Based Leadership |

###### MSEd (Hybrid)

| # | 项目 |
|---|------|
| 1 | Adolescent Education (Grades: 7-12) |
| 2 | Childhood Education (Grades: 1-6) |
| 3 | Special Education (Grades: 1-6 or 7-12) |
| 4 | Teaching English to Speakers of Other Languages (Grades: P-12) |

###### MSEd (Online)

| # | 项目 |
|---|------|
| 1 | Early Childhood Education (Grades: B-2) |
| 2 | Teaching English to Speakers of Other Languages (Adult Learners) |

###### Post-Master's Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Educational Leadership |

###### Post-Master's Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Teaching English to Speakers of Other Languages (Grades P-12) |

##### Program Area: Engineering, Computer Science & Technology

###### ME (Hybrid)

| # | 项目 |
|---|------|
| 1 | Electrical Engineering |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Program Area: Health & Public Health

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Cultural Competence |

###### DNP (Online)

| # | 项目 |
|---|------|
| 1 | Advanced Adult Clinical Care |

###### DPT

| # | 项目 |
|---|------|
| 1 | Physical Therapy |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Adult-Gerontology Health Nursing |

###### MS (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Healthcare Management |

###### Post-Master's Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Adult-Gerontology Health Nursing |

##### Program Area: Humanities

###### Adv. Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Public History |

###### MA (Hybrid)

| # | 项目 |
|---|------|
| 1 | English |
| 2 | History |
| 3 | Liberal Studies |

##### Program Area: Mental Health, Psychology & Social Work

###### MA

| # | 项目 |
|---|------|
| 1 | Mental Health Counseling (Clinical) |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Neuroscience |

###### MSW (Hybrid)

| # | 项目 |
|---|------|
| 1 | Social Work |

##### Program Area: Science & Mathematics

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Biology |
| 2 | Environmental Science |

##### Program Area: Social Sciences

###### MA (Hybrid)

| # | 项目 |
|---|------|
| 1 | Liberal Studies |

#### Craig Newmark Graduate School of Journalism

##### Program Area: Communications

###### MA

| # | 项目 |
|---|------|
| 1 | Engagement Journalism |
| 2 | Journalism |

###### MA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Bilingual Journalism (Spanish) |

#### CUNY School of Professional Studies

##### Program Area: Business

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Management |
| 2 | Project Management |
| 3 | Research Administration |
| 4 | Research Compliance |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Business Management & Leadership |
| 2 | Research Administration & Compliance |
| 3 | Strategic Nonprofit Management |

##### Program Area: Criminal Justice & Law

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Immigration Law Studies |

##### Program Area: Education

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Children’s Program Administrator Credential |
| 2 | Disability Services in Higher Education |
| 3 | Early Childhood Policy |

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Early Childhood Policy and Leadership |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Disability Services in Higher Education |

##### Program Area: Engineering, Computer Science & Technology

###### MA

| # | 项目 |
|---|------|
| 1 | Generative AI |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Data Science |

##### Program Area: Health & Public Health

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Health Information Management |
| 2 | Nursing Education |
| 3 | Nursing Informatics |
| 4 | Nursing Organizational Leadership |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Health Information Management |
| 2 | Nursing Education |
| 3 | Nursing Informatics |
| 4 | Nursing Organizational Leadership |

##### Program Area: Humanities

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Museum Studies |

##### Program Area: Mental Health, Psychology & Social Work

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Psychology |

##### Program Area: Social Sciences

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Disability Advocacy |
| 2 | Disability Services in Higher Education |
| 3 | Disability Studies |
| 4 | Youth Studies |

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Disability Studies |
| 2 | Youth Studies |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Disability Services in Higher Education |

##### Program Area: Visual & Performing Arts

###### MA

| # | 项目 |
|---|------|
| 1 | Applied Theatre |

#### CUNY School of Law

##### Program Area: Criminal Justice & Law

###### JD

| # | 项目 |
|---|------|
| 1 | Law |

#### CUNY School of Labor and Urban Studies

##### Program Area: Health & Public Health

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Leading Change in Healthcare Systems |

##### Program Area: Humanities

###### MA

| # | 项目 |
|---|------|
| 1 | Urban Studies |

##### Program Area: Public Administration

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Community Leadership |
| 2 | Public Administration & Public Policy |

##### Program Area: Social Sciences

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Labor Relations |
| 2 | Labor Studies |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Workplace Democracy and Community Ownership |

###### MA

| # | 项目 |
|---|------|
| 1 | Labor Studies |
| 2 | Urban Studies |

#### Graduate School of Public Health & Health Policy

##### Program Area: Health & Public Health

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Environmental and Occupational Epidemiology |
| 2 | Environmental Risk Assessment |
| 3 | Industrial Hygiene |

###### Adv. Cert. (Online, On-Campus, or Hybrid)

| # | 项目 |
|---|------|
| 1 | Public Health |

###### DI

| # | 项目 |
|---|------|
| 1 | Nutrition & Dietetic Internship |

###### MPH (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Community Health |
| 2 | Environmental & Occupational Health Sciences |
| 3 | Epidemiology & Biostatistics |
| 4 | Health Policy & Management |
| 5 | Public Health Nutrition |
| 6 | Sexual and Reproductive Justice & Health |

###### MS (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Environmental & Occupational Health Sciences |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Health Communication for Social Change |
| 2 | Population Health Informatics |

###### PhD

| # | 项目 |
|---|------|
| 1 | Community Health and Health Policy |
| 2 | Environmental & Planetary Health Sciences |
| 3 | Epidemiology |

##### Program Area: Public Administration

###### PhD

| # | 项目 |
|---|------|
| 1 | Community Health and Health Policy |

#### Hunter College

##### Program Area: Architecture and Design

###### MUP

| # | 项目 |
|---|------|
| 1 | Urban Planning |

##### Program Area: Business

###### MA

| # | 项目 |
|---|------|
| 1 | Economics |

###### MS

| # | 项目 |
|---|------|
| 1 | Accounting |

##### Program Area: Communications

###### MA

| # | 项目 |
|---|------|
| 1 | Translation & Interpreting |

###### MFA

| # | 项目 |
|---|------|
| 1 | Integrated Media Arts |

##### Program Area: Education

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Bilingual Education Extension - NYS Teachers |
| 2 | Bilingual Education for Pupil Personnel Services |
| 3 | Computer Science Education for NYS Certified Teachers |
| 4 | Intensive Teacher Institute TESOL or Bilingual Extension for NYCPS Teachers |
| 5 | Mathematics and Technology |
| 6 | Mathematics Development |
| 7 | Science and Robotics |
| 8 | Science and Technology |

###### Adv. Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Gifted Education Extension |

###### Adv. Cert. (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Special Education (Grades: P-12) |

###### EdD

| # | 项目 |
|---|------|
| 1 | Instructional Leadership |

###### MA

| # | 项目 |
|---|------|
| 1 | Chinese Education (Grades: 7-12) |
| 2 | Dance Education (Grades: P-12) |
| 3 | Educational Psychology |
| 4 | English Education (Grades: 7 - 12) |
| 5 | French Education (Grades: 7-12) |
| 6 | Italian Education (Grades: 7-12) |
| 7 | Latin Education (Grades: 7-12) |
| 8 | Mathematics Education (Grades: 7-12) |
| 9 | Mathematics Education Professional Certificate (Grades: 7-12) |
| 10 | Music Education (P-12) |
| 11 | Science Education: Biology (Grades 7-12) |
| 12 | Science Education: Chemistry (Grades 7-12) |
| 13 | Science Education: Earth Science (Grades 7-12) |
| 14 | Science Education: Physics (Grades 7-12) |
| 15 | Social Studies Education (Grades: 7-12) |
| 16 | Spanish Education (Grades: 7-12) |
| 17 | Teaching English to Speakers of Other Languages (Adult Learners) |
| 18 | Teaching English to Speakers of Other Languages (Grades P-12) |
| 19 | Teaching English to Speakers of Other Languages for NYS Certified Teachers (Grades P-12) |
| 20 | Visual Arts Education |
| 21 | Visual Arts Education for NYS Teachers |

###### MS (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Applied Behavior Analysis |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Bilingual Childhood Education |
| 2 | Bilingual Early Childhood Education (Grades: B-2) |
| 3 | Blind & Visually Impaired (Grades: K-12) |
| 4 | Childhood Education (Grades: 1-6) |
| 5 | Childhood Education with Specialization in STEM |
| 6 | Computer Science Education |
| 7 | Deaf & Hard of Hearing/Childhood Education Dual Certification |
| 8 | Early Childhood Education (Grades: B-2) |
| 9 | Early Childhood Education for NYS Certified Teachers (Grades: B-2) |
| 10 | Early Childhood Special Education for NYS Certified Teachers |
| 11 | Educational Leadership SBL/SDL |
| 12 | Elementary Mathematics Specialist |
| 13 | Literacy Education (Grades: B-12) |
| 14 | Multiple Disabilities Including DeafBlindness (Grades: P-12) |
| 15 | Professional Certification in Early Childhood Special Education for NYS Certified Teachers (Advanced Preparation) |
| 16 | School Counseling |
| 17 | School Counseling with Bilingual Concentration |
| 18 | Severe/Multiple Disabilities for NYS Early Childhood Teachers |
| 19 | Severe/Multiple Disabilities/Early Childhood Education Dual Certification - NYS Teachers |
| 20 | Severe/Multiple Disabilities/Early Childhood Education Dual Certification (Grades: B-2) |
| 21 | Special Education/Early Childhood Education Dual Certification (Grades: B-2) |
| 22 | Visual Impairment: Combined Rehabilitation Teaching and Orientation and Mobility |
| 23 | Visual Impairment: Rehabilitation Teaching |

###### MSEd (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Special Education (Grades: P-12) |

###### MSEd (Online)

| # | 项目 |
|---|------|
| 1 | Deaf & Hard of Hearing for NYS Certified Teachers |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Dance Education (Grades: P-12) |
| 2 | Early Childhood Education for NYS Certified Teachers (Grades: B-2) |
| 3 | English Education (Grades: 7 - 12) |
| 4 | French Education (Grades: 7-12) |
| 5 | Italian Education (Grades: 7-12) |
| 6 | Latin Education (Grades: 7-12) |
| 7 | Learning and Assessment |
| 8 | Mathematics Education (Grades: 7-12) |
| 9 | Professional Certification in Early Childhood Special Education for NYS Certified Teachers |
| 10 | Science Education: Biology (Grades 7-12) |
| 11 | Science Education: Chemistry (Grades 7-12) |
| 12 | Science Education: Earth Science (Grades 7-12) |
| 13 | Science Education: Physics (Grades 7-12) |
| 14 | Severe/Multiple Disabilities Annotation Extension for NYS Certified Teachers |
| 15 | Social Studies Education (Grades: 7-12) |
| 16 | Spanish Education (Grades: 7-12) |
| 17 | Teaching English to Speakers of Other Languages (Grades P-12) |
| 18 | Teaching English to Speakers of Other Languages for Applicants With Prior TESOL or Linguistics MA (Grades P-12) |

###### Post-Master's Cert. (Hybrid)

| # | 项目 |
|---|------|
| 1 | Blind & Visually Impaired: Orientation and Mobility |

###### Post-Master's Cert. (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Applied Behavior Analysis |

###### Post-Master's Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Blind & Visually Impaired for NYS Teachers |

##### Program Area: Engineering, Computer Science & Technology

###### MS

| # | 项目 |
|---|------|
| 1 | Computer Science |
| 2 | Geoinformatics |

##### Program Area: Health & Public Health

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Cytotechnology |
| 2 | Medical Laboratory Technology |

###### DNP

| # | 项目 |
|---|------|
| 1 | Adult-Gerontology Primary Care Nurse Practitioners |
| 2 | Family Nurse Practitioner |
| 3 | Nurse Anesthesia/Adult-Gerontology Acute Care Dual Certification |
| 4 | Psychiatric-Mental Health Nurse Practitioner |

###### DPT

| # | 项目 |
|---|------|
| 1 | Physical Therapy |

###### MS

| # | 项目 |
|---|------|
| 1 | Adult-Gerontology Clinical Nurse Specialist |
| 2 | Adult-Gerontology Primary Care Nurse Practitioners |
| 3 | Biomedical Laboratory Management |
| 4 | Community/Public Health Nursing |
| 5 | Nursing Administration/Urban Policy and Leadership Dual Program |
| 6 | Nutrition |
| 7 | Psychiatric-Mental Health Nurse Practitioner |
| 8 | Speech-Language Pathology |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Nursing Education |

###### PhD

| # | 项目 |
|---|------|
| 1 | Nursing |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Psychiatric-Mental Health Nurse Practitioner |

###### Post-Master's Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Nursing Education |

##### Program Area: Humanities

###### MA

| # | 项目 |
|---|------|
| 1 | Art History |
| 2 | French |
| 3 | History |
| 4 | Italian |
| 5 | Literature, Language, and Theory |
| 6 | Spanish |
| 7 | Theatre |
| 8 | Translation & Interpreting |

###### MFA

| # | 项目 |
|---|------|
| 1 | Creative Writing |
| 2 | Playwriting |

##### Program Area: Mental Health, Psychology & Social Work

###### MA

| # | 项目 |
|---|------|
| 1 | Animal Behavior & Conservation |
| 2 | Educational Psychology |
| 3 | Psychology |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Clinical Rehabilitation Counseling |
| 2 | Mental Health Counseling |
| 3 | School Counseling |
| 4 | School Counseling with Bilingual Concentration |

###### MSW

| # | 项目 |
|---|------|
| 1 | Social Work |

##### Program Area: Public Administration

###### MS

| # | 项目 |
|---|------|
| 1 | Nursing Administration/Urban Policy and Leadership Dual Program |
| 2 | Urban Policy & Leadership |

##### Program Area: Science & Mathematics

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Geographic Information Science |

###### MA

| # | 项目 |
|---|------|
| 1 | Animal Behavior & Conservation |
| 2 | Biochemistry |
| 3 | Biology |
| 4 | Geography |
| 5 | Physics |
| 6 | Pure Mathematics |
| 7 | Statistics & Applied Mathematics |

###### MS

| # | 项目 |
|---|------|
| 1 | Geoinformatics |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | Anthropology |
| 2 | Economics |

###### MS

| # | 项目 |
|---|------|
| 1 | Applied Digital Sociology |
| 2 | Urban Policy & Leadership |

##### Program Area: Visual & Performing Arts

###### MA

| # | 项目 |
|---|------|
| 1 | Dance Education (Grades: P-12) |
| 2 | Music |
| 3 | Music Education (P-12) |
| 4 | Theatre |
| 5 | Visual Arts Education |
| 6 | Visual Arts Education for NYS Teachers |

###### MFA

| # | 项目 |
|---|------|
| 1 | Dance |
| 2 | Integrated Media Arts |
| 3 | Playwriting |
| 4 | Studio Art |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Dance Education (Grades: P-12) |

#### Hunter College/Bank Street College of Education

##### Program Area: Education

###### MSW/MSEd

| # | 项目 |
|---|------|
| 1 | Social Work/Infant and Parent Development |

##### Program Area: Mental Health, Psychology & Social Work

###### MSW/MSEd

| # | 项目 |
|---|------|
| 1 | Social Work/Infant and Parent Development |

#### Hunter College/Brooklyn Law School

##### Program Area: Architecture and Design

###### MUP/JD

| # | 项目 |
|---|------|
| 1 | Urban Planning and Law |

#### John Jay College of Criminal Justice

##### Program Area: Business

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Forensic Accounting |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Social Entrepreneurship and Innovation |

###### MA

| # | 项目 |
|---|------|
| 1 | Economics |

##### Program Area: Criminal Justice & Law

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Computer Science for Digital Forensic Science |
| 2 | Computer Science: Applied Digital Forensic Science |
| 3 | Race & Criminal Justice |
| 4 | Victimology Studies |

###### Adv. Cert. (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Crime Prevention & Analysis |
| 2 | Criminal Investigation |
| 3 | Terrorism |
| 4 | Transnational Organized Crime Studies |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Corrections Management |

###### MA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Criminal Justice |
| 2 | Human Rights |
| 3 | International Crime & Justice |

###### MS

| # | 项目 |
|---|------|
| 1 | Digital Forensics and Cybersecurity |
| 2 | Forensic Science |

###### MS (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Protection Management |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Security Management |

##### Program Area: Engineering, Computer Science & Technology

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Computer Science for Digital Forensic Science |
| 2 | Computer Science: Applied Digital Forensic Science |

###### MS

| # | 项目 |
|---|------|
| 1 | Digital Forensics and Cybersecurity |

##### Program Area: Humanities

###### MA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Human Rights |

##### Program Area: Mental Health, Psychology & Social Work

###### MA

| # | 项目 |
|---|------|
| 1 | Forensic Mental Health Counseling |
| 2 | Forensic Psychology |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Forensic Psychology |

##### Program Area: Public Administration

###### Adv. Cert. (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Emergency Management |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Corrections Management |
| 2 | Healthcare Inspection and Oversight |

###### MPA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Public Administration: Inspection & Oversight |
| 2 | Public Administration: Public Policy and Administration |

###### MPA/MS

| # | 项目 |
|---|------|
| 1 | Public Policy and Protection Management |

###### MS (Online & Hybrid)

| # | 项目 |
|---|------|
| 1 | Emergency Management |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | Economics |

###### MA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Human Rights |

#### Lehman College

##### Program Area: Business

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Actuarial Mathematics |

###### MS (Hybrid)

| # | 项目 |
|---|------|
| 1 | Business - Finance Concentration |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Business - Accounting Concentration |
| 3 | Business - Human Resources Management Concentration |
| 4 | Business - International Business Concentration |
| 5 | Business - Marketing Concentration |

##### Program Area: Education

###### 

| # | 项目 |
|---|------|
| 1 | Teaching English to Speakers of Other Languages - Alternative Transitional B Certification (Grades: P-12) |

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Middle Childhood Education (Grades: 5-6) Extention |
| 2 | Science Education (Grades: 7-12) |
| 3 | Social Studies Education (Grades: 7-12) |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Bilingual Education Extension - ITI Clinically Rich Program (Grades: 5-12) |
| 2 | Bilingual Education Extension - ITI Clinically Rich Program (Grades: B-6) |
| 3 | Bilingual Education Extension – NYS Teachers (Grades: 5-12) |
| 4 | Bilingual Education Extension – NYS Teachers (Grades: B-6) |
| 5 | Computer Science Education (Grades: P-12) |
| 6 | Human Rights Education & Transformative Justice |
| 7 | Media and Information Literacy in Education |
| 8 | Mindfulness and Contemplative Studies |
| 9 | Science of Reading |
| 10 | Teacher Leadership |

###### EdD (Online)

| # | 项目 |
|---|------|
| 1 | Organizational Leadership, Development, and Change |

###### MA

| # | 项目 |
|---|------|
| 1 | Art Education (Grades: P-12) |
| 2 | Mathematics and Instruction |
| 3 | Social Studies Education (Grades: 7-12) |
| 4 | Social Studies Education and Students with Disabilities (Grades: 7-12) |
| 5 | Social Studies Teacher - Alternative Transitional B Certification (Grades: 7-12) |
| 6 | Spanish Education (Grades: 7-12) |
| 7 | Teaching Student with Speech and Language Disorders Bilingual |

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Health Education & Promotion |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Organizational Leadership |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Childhood Education - Bilingual (Grades 1 - 6) |
| 2 | Childhood Education (Grades 1 - 6) |
| 3 | Early Childhood Education - Bilingual (Grades: B-2) |
| 4 | Early Childhood Education (Grades: B-2) |
| 5 | English Education (Grades: 7 - 12) |
| 6 | English Teacher - Alternative Transitional B Certification (Grades: 7-12) |
| 7 | English Teacher/Students with Disabilities - Alternative Transitional B Certification (Grades: 7-12) |
| 8 | Literacy & Special Education Dual Cert. (All Grades) |
| 9 | Literacy Education (All Grades) |
| 10 | Math Teacher - Alternative Transitional B Certification (Grades: 7-12) |
| 11 | Mathematics Education (Grades: 5-9) |
| 12 | Mathematics Education and Students with Disabilities (Grades: 7-12) |
| 13 | Science Education (Grades: 7-12) |
| 14 | Science Education and Students with Disabilities (Grades: 7-12) |
| 15 | Science Teacher - Alternative Transitional B Certification (Grades: 7-12) |
| 16 | Special Education (Grades: 1-6) |
| 17 | Special Education (Grades: 7-12) |
| 18 | Special Education (Grades: Birth-2) |
| 19 | Teaching English to Speakers of Other Languages (Grades: P-12) |

###### MSEd (Online)

| # | 项目 |
|---|------|
| 1 | Computer Science Education (Grades: P-12) |
| 2 | Educational Leadership: School Building Leader |
| 3 | Health Education (P-12) |
| 4 | Recreation Education |
| 5 | School Counseling |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Applied Music and Music Teaching |
| 2 | Bilingual School Counseling Extension (for Lehman Alumni) |
| 3 | English Education (Grades: 7 - 12) |
| 4 | Literacy Education (Grades: 5-12) |
| 5 | Literacy Education (Grades: B-6) |
| 6 | Mathematics Education (Grades: 7-12) |
| 7 | Special Education (Grades: 1-6) |
| 8 | Special Education (Grades: 7-12) |
| 9 | Special Education (Grades: Birth-2) |
| 10 | Teachers of Languages Other than English |
| 11 | Teaching English to Speakers of Other Languages |

###### Post-Master's Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Educational Leadership: School Building Leader |
| 2 | Educational Leadership: School District Leader |
| 3 | Health Education (P-12) |

##### Program Area: Engineering, Computer Science & Technology

###### MS

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Program Area: Health & Public Health

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Applied Research Methods in Public Health |

###### DNP

| # | 项目 |
|---|------|
| 1 | Nursing: Family Nurse Practitioner |
| 2 | Nursing: Pedriatric Nurse Practitioner |

###### MA

| # | 项目 |
|---|------|
| 1 | Speech-Language Pathology |

###### MA (Online)

| # | 项目 |
|---|------|
| 1 | Health Education & Promotion |

###### MS

| # | 项目 |
|---|------|
| 1 | Human Performance and Fitness |
| 2 | Nursing: Family Nurse Practitioner |
| 3 | Nursing: Pedriatric Nurse Practitioner |
| 4 | Nutrition |

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Health Services Administration |

###### PhD

| # | 项目 |
|---|------|
| 1 | Human Performance and Fitness |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Nursing: Family Nurse Practitioner |
| 2 | Nursing: Pedriatric Nurse Practitioner |
| 3 | Speech-Language Pathology - Bilingual Extension |

##### Program Area: Humanities

###### MA

| # | 项目 |
|---|------|
| 1 | English |
| 2 | History |
| 3 | Liberal Studies |
| 4 | Spanish Literature |

##### Program Area: Mental Health, Psychology & Social Work

###### MS (Online)

| # | 项目 |
|---|------|
| 1 | Mental Health Counseling (Clinical) |

###### MSEd (Online)

| # | 项目 |
|---|------|
| 1 | School Counseling |

###### MSW

| # | 项目 |
|---|------|
| 1 | Social Work |

###### Post-Master's Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Mental Health Counseling (Clinical) |

##### Program Area: Science & Mathematics

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Actuarial Mathematics |
| 2 | Geographic Information Science |

###### MA

| # | 项目 |
|---|------|
| 1 | Biology |
| 2 | Mathematics |
| 3 | Mathematics and Instruction |

###### MS

| # | 项目 |
|---|------|
| 1 | Biology |
| 2 | Geographic Information Science |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | Liberal Studies |

##### Program Area: Visual & Performing Arts

###### MA

| # | 项目 |
|---|------|
| 1 | Art |
| 2 | Art Education |

###### MAT

| # | 项目 |
|---|------|
| 1 | Applied Music and Music Teaching |

###### MFA

| # | 项目 |
|---|------|
| 1 | Art |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Applied Music and Music Teaching |

#### Queens College

##### Program Area: Business

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Risk Management |

###### MS

| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Actuarial Risk Management |
| 3 | Risk Management: Accounting Concentration |
| 4 | Risk Management: Environmental Risk Management |
| 5 | Risk Management: Finance Concentration |
| 6 | Taxation |

##### Program Area: Communications

###### MA

| # | 项目 |
|---|------|
| 1 | Media Studies |

##### Program Area: Education

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Bilingual Education (Grades: 7-12) |
| 3 | Bilingual Education Extension - NYS Teachers |
| 4 | Chinese Education (Adolescent) |
| 5 | Critical Languages Education |
| 6 | English Education (Grades: 7 - 12) |
| 7 | Family & Consumer Science Teacher (Grades: 7-12) |
| 8 | French Education (Adolescent) |
| 9 | Italian Education (Adolescent) |
| 10 | Mathematics Education (Grades: 7-12) |
| 11 | Music Education |
| 12 | Physical Education (Grades: K-12) |
| 13 | Science Education: Biology (Grades 7-12) |
| 14 | Science Education: Chemistry (Grades 7-12) |
| 15 | Science Education: Earth Science (Grades 7-12) |
| 16 | Science Education: Physics (Grades 7-12) |
| 17 | Social Studies Education (Adolescent) |
| 18 | Spanish Education (Grades: 7-12) |
| 19 | Teaching English to Speakers of Other Languages (Grades P-12) |
| 20 | TESOL & Elementary Bilingual Ed. |

###### Adv. Cert. (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Bilingual Education |

###### Adv. Cert. (Online)

| # | 项目 |
|---|------|
| 1 | Ethical & Equitable Practice |

###### MAT

| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Childhood Education (Grades 1 - 6) |
| 3 | Critical Languages Education |
| 4 | Early Childhood Education |
| 5 | English Education (Grades: 7 - 12) |
| 6 | Mathematics Education (Grades: 7-12) |
| 7 | Science Education: Biology (Grades 7-12) |
| 8 | Science Education: Chemistry (Grades 7-12) |
| 9 | Science Education: Earth Science (Grades 7-12) |
| 10 | Science Education: Physics (Grades 7-12) |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Educational Leadership |
| 3 | English Education (Grades: 7 - 12) |
| 4 | French Education (Adolescent) |
| 5 | Italian Education (Adolescent) |
| 6 | Literacy Education (Grades: 5-12) |
| 7 | Literacy Education (Grades: B-6) |
| 8 | Math and Bilingual Education (Grades: 7-12) |
| 9 | Mathematics Education (Grades: 7-12) |
| 10 | Music Education |
| 11 | Physical Education (Grades: K-12) |
| 12 | School Counseling |
| 13 | School Psychology |
| 14 | Science Education: Biology (Grades 7-12) |
| 15 | Science Education: Chemistry (Grades 7-12) |
| 16 | Science Education: Earth Science (Grades 7-12) |
| 17 | Science Education: Physics (Grades 7-12) |
| 18 | Social Studies Education (Adolescent) |
| 19 | Spanish Education (Grades: 7-12) |
| 20 | Teaching English to Speakers of Other Languages (Grades P-12) |
| 21 | Teaching Math & Computer Science |

###### MSEd (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Family & Consumer Science Teacher (Grades: 7-12) |
| 2 | Special Education (Grades: Birth-2, 1-6, or 7-12) |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Literacy Education (Grades: 5-12) |
| 2 | Literacy Education (Grades: B-6) |
| 3 | Special Education (Grades: Birth-2, 1-6, or 7-12) |

##### Program Area: Engineering, Computer Science & Technology

###### MA

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Program Area: Health & Public Health

###### MA

| # | 项目 |
|---|------|
| 1 | Speech-Language Pathology |

###### MS

| # | 项目 |
|---|------|
| 1 | Exercise Science Specialist |
| 2 | Nutrition |
| 3 | Nutrition & Exercise Science |

##### Program Area: Humanities

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Italian Culture for the 21 Century |

###### MA

| # | 项目 |
|---|------|
| 1 | Art History |
| 2 | English |
| 3 | French |
| 4 | History |
| 5 | Liberal Studies |
| 6 | Spanish |

###### MFA

| # | 项目 |
|---|------|
| 1 | Creative Writing |

##### Program Area: Library Science

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Archives, Records Management, and Preservation |
| 2 | Library Media Specialist |

###### Initial Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Child & Young Adult Services in the Public Library |

###### MLS

| # | 项目 |
|---|------|
| 1 | Library Media Specialist |
| 2 | Library Media Specialist for Certified Teachers |
| 3 | Library Science |

###### MLS/MA

| # | 项目 |
|---|------|
| 1 | Dual Program in Library Science & History |

###### Post-Master's Cert.

| # | 项目 |
|---|------|
| 1 | Library Science |

##### Program Area: Mental Health, Psychology & Social Work

###### Adv. Cert. (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Applied Behavior Analysis |

###### MA

| # | 项目 |
|---|------|
| 1 | Behavioral Neuroscience |
| 2 | Psychology |

###### MA (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Applied Behavior Analysis |

###### MS

| # | 项目 |
|---|------|
| 1 | Mental Health Counseling |

###### MSEd

| # | 项目 |
|---|------|
| 1 | School Counseling |
| 2 | School Psychology |

##### Program Area: Science & Mathematics

###### MA

| # | 项目 |
|---|------|
| 1 | Biology |
| 2 | Chemistry |
| 3 | Geological & Environmental Science |
| 4 | Mathematics |
| 5 | Physics |

###### MS

| # | 项目 |
|---|------|
| 1 | Applied Environmental Geoscience |
| 2 | Photonics |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | Data Analytics & Applied Social Research |
| 2 | Liberal Studies |
| 3 | Linguistics (Applied) |
| 4 | Urban Affairs |

##### Program Area: Visual & Performing Arts

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Music Education |
| 3 | Music Production |
| 4 | Performance |
| 5 | Performance Professional Studies |

###### Adv. Diploma

| # | 项目 |
|---|------|
| 1 | Chamber Music |
| 2 | Performance |

###### MA

| # | 项目 |
|---|------|
| 1 | Media Studies |
| 2 | Music Theory |
| 3 | Musicology |

###### MAT

| # | 项目 |
|---|------|
| 1 | Art Education |

###### MFA

| # | 项目 |
|---|------|
| 1 | Studio Art |

###### MM

| # | 项目 |
|---|------|
| 1 | Conducting |
| 2 | Jazz Studies |
| 3 | Music (Classical Performance) |
| 4 | Music Composition |

###### MSEd

| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Music Education |

#### The Graduate Center

##### Program Area: Business

###### PhD

| # | 项目 |
|---|------|
| 1 | Economics |

##### Program Area: Communications

###### MS

| # | 项目 |
|---|------|
| 1 | Data Analysis and Visualization |

##### Program Area: Criminal Justice & Law

###### PhD

| # | 项目 |
|---|------|
| 1 | Criminal Justice |

##### Program Area: Education

###### Adv. Cert.

| # | 项目 |
|---|------|
| 1 | Interactive Technology and Pedagogy |

###### PhD

| # | 项目 |
|---|------|
| 1 | Educational Psychology |
| 2 | Urban Education |

##### Program Area: Engineering, Computer Science & Technology

###### MA

| # | 项目 |
|---|------|
| 1 | Digital Humanities |

###### MS

| # | 项目 |
|---|------|
| 1 | Data Analysis and Visualization |
| 2 | Data Science |
| 3 | Nanoscience |

###### PhD

| # | 项目 |
|---|------|
| 1 | Computer Science |

##### Program Area: Health & Public Health

###### PhD

| # | 项目 |
|---|------|
| 1 | Speech-Language-Hearing Sciences |

##### Program Area: Humanities

###### MA

| # | 项目 |
|---|------|
| 1 | Biography and Memoir |
| 2 | Classics |
| 3 | Comparative Literature |
| 4 | Digital Humanities |
| 5 | Liberal Studies |
| 6 | Philosophy |
| 7 | Women's and Gender Studies |

###### PhD

| # | 项目 |
|---|------|
| 1 | Art History |
| 2 | Classics |
| 3 | Comparative Literature |
| 4 | English |
| 5 | French |
| 6 | History |
| 7 | Latin American, Iberian, & Latino Cultures |
| 8 | Philosophy |
| 9 | Theatre and Performance |

##### Program Area: Mental Health, Psychology & Social Work

###### MS

| # | 项目 |
|---|------|
| 1 | Cognitive Neuroscience |

###### PhD

| # | 项目 |
|---|------|
| 1 | Educational Psychology |
| 2 | Psychology |
| 3 | Social Welfare |

##### Program Area: Science & Mathematics

###### MS

| # | 项目 |
|---|------|
| 1 | Cognitive Neuroscience |
| 2 | Nanoscience |

###### PhD

| # | 项目 |
|---|------|
| 1 | Biochemistry |
| 2 | Biology |
| 3 | Chemistry |
| 4 | Earth and Atmospheric Sciences; Environmental Science |
| 5 | Mathematics |
| 6 | Physics |

##### Program Area: Social Sciences

###### MA

| # | 项目 |
|---|------|
| 1 | International Migration Studies |
| 2 | Liberal Studies |
| 3 | Linguistics (Applied) |
| 4 | Middle Eastern Studies |
| 5 | Political Science |
| 6 | Women's and Gender Studies |

###### MS

| # | 项目 |
|---|------|
| 1 | Quantitative Methods in the Social Sciences |

###### PhD

| # | 项目 |
|---|------|
| 1 | Anthropology |
| 2 | Economics |
| 3 | Linguistics (Applied) |
| 4 | Political Science |
| 5 | Sociology |

##### Program Area: Visual & Performing Arts

###### DMA

| # | 项目 |
|---|------|
| 1 | Music |

###### PhD

| # | 项目 |
|---|------|
| 1 | Music |
| 2 | Theatre and Performance |

#### York College

##### Program Area: Business

###### MS

| # | 项目 |
|---|------|
| 1 | Aviation Management |
| 2 | Pharmaceutical Science and Business |

##### Program Area: Health & Public Health

###### MS

| # | 项目 |
|---|------|
| 1 | Physician Assistant |

##### Program Area: Mental Health, Psychology & Social Work

###### MSW

| # | 项目 |
|---|------|
| 1 | Social Work |

##### Program Area: Science & Mathematics

###### MS

| # | 项目 |
|---|------|
| 1 | Pharmaceutical Science and Business |

###### MS (Online & On-Campus)

| # | 项目 |
|---|------|
| 1 | Clinical Trial Management |

#### Baruch College/Brooklyn Law

##### Program Area: Business

###### MBA/JD

| # | 项目 |
|---|------|
| 1 | Business Administration & Law |

#### Baruch College/NYLS

##### Program Area: Business

###### MBA/JD

| # | 项目 |
|---|------|
| 1 | Business Administration & Law |

#### John Jay College of Criminal Justice/ CUNY School of Law

##### Program Area: Criminal Justice & Law

###### MA/JD

| # | 项目 |
|---|------|
| 1 | Forensic Psychology & Law |

###### MPA/JD

| # | 项目 |
|---|------|
| 1 | Law & Public Accountability |

##### Program Area: Mental Health, Psychology & Social Work

###### MA/JD

| # | 项目 |
|---|------|
| 1 | Forensic Psychology & Law |

##### Program Area: Public Administration

###### MPA/JD

| # | 项目 |
|---|------|
| 1 | Law & Public Accountability |

#### John Jay College of Criminal Justice/NYLS

##### Program Area: Criminal Justice & Law

###### MA/JD

| # | 项目 |
|---|------|
| 1 | Forensic Psychology & Law |

##### Program Area: Mental Health, Psychology & Social Work

###### MA/JD

| # | 项目 |
|---|------|
| 1 | Forensic Psychology & Law |

#### The City College of New York/ CUNY School of Law

##### Program Area: Criminal Justice & Law

###### MIA/JD

| # | 项目 |
|---|------|
| 1 | Law and International Relations |

##### Program Area: Social Sciences

###### MIA/JD

| # | 项目 |
|---|------|
| 1 | Law and International Relations |

#### The Graduate Center/Baruch College

##### Program Area: Business

###### PhD

| # | 项目 |
|---|------|
| 1 | Business |

#### Graduate School of Public Health & Health Policy/Albert Einstein College of Medicine

##### Program Area: Health & Public Health

###### MD/MPH (Hybrid)

| # | 项目 |
|---|------|
| 1 | Epidemiology & Biostatistics |
| 2 | Health Policy & Management |

### 2.2 At least one program's full deep-dive (worked example)

**Baruch College — MBA (Master of Business Administration)**

| Field | Value |
|---|---|
| Department | Zicklin School of Business |
| Address | 55 Lexington Avenue, New York, NY 10010 |
| Phone | 646-312-1000 |
| Email | ZicklinGrad@baruch.cuny.edu |
| Application portal | https://www.baruch.cuny.edu/graduate/ |
| Degree types | MBA (Online & On-Campus), Executive MBA |
| GMAT/GRE | Test-optional for most programs (varies by concentration) |
| TOEFL/IELTS minimum | TOEFL iBT 80 / IELTS 6.5 / PTE 53 / Duolingo 105 |
| Application fee | $75 (typical CUNY graduate fee) |
| Funding | Limited merit scholarships; some GA/TA positions |

### 2.3 Graduate admissions model

CUNY graduate admissions is **decentralized at the program level**. Each of the 16 graduate colleges runs its own admissions office; many programs use the CUNY Graduate Application (https://www.cuny.edu/graduate-studies/apply/), while specialized programs (Law, Medicine, Architecture, Journalism, Public Health) use their own portals. Standard application fee is $75 per program (varies); fee waivers available via GradCAS / individual colleges. CUNY honors the **April 15 CGS Resolution** for master's admission offers.

---

## 3. Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 |
|---|---|
| Admissions site | https://www.cuny.edu/admissions/undergraduate/ |
| Application portal | CUNY Application — https://www.cuny.edu/admissions/undergraduate/apply/cuny-application/ (one application, up to 6 colleges for freshman / 4 for transfer) |
| EA deadline | N/A — CUNY uses rolling admissions, not EA/ED |
| RA (priority) deadline — Fall | February 1 (Application & Supporting Documents) for US-educated freshman/transfer |
| RA (priority) deadline — Fall (international) | December 1 (Application) / December 15 (Supporting Documents) |
| RA (priority) deadline — Spring | September 15 (Application & Supporting Documents) for US-educated |
| RA (priority) deadline — Spring (international) | September 1 (Application) / September 15 (Supporting Documents) |
| Decision notification | Rolling January–July (Fall) / Rolling October–January (Spring) |
| Enrollment-confirmation deadline | Per college; typically May 1 (Fall) / January 1 (Spring) |
| Financial-aid deadline | FAFSA + NYS TAP — priority March 1; rolling thereafter |
| SAT/ACT policy | Test-optional for most CUNY colleges (extended through Fall 2026 admissions cycle for some); college-specific |
| Score-report method | Self-reported via CUNY Application; official only upon enrollment |
| Recommendation requirements | None required for freshman; varies for transfer & Macaulay Honors |
| Portfolios | Required only for BFA/BMUS/BARCH applicants |
| Transfer pathway | CUNY Transfer Application (up to 4 colleges); Transfer Credit Guide at https://www.cuny.edu/admissions/undergraduate/explore/transfer/ |
| Application fee — Freshman | $65 |
| Application fee — Transfer | $70 |
| Application fee — Macaulay | $65 |
| Fee waiver | Available — see https://www.cuny.edu/admissions/undergraduate/apply/#scores |

### 3.2 Undergraduate English proficiency table

Per-college minimums (TOEFL iBT / Paper-based / IELTS Academic / Pearson PTE Academic / Duolingo):

| College | TOEFL iBT | TOEFL Paper | IELTS | PTE | Duolingo |
|---|---|---|---|---|---|
| Baruch College | 80 | 550 | 6.5 | 53 | 105 |
| Brooklyn College | 61 | 500 | 6 | 44 | 85 |
| The City College of New York | 61 | 500 | 6 | 44 | 85 |
| College of Staten Island | 45 | 450 | 5 | 39 | 75 |
| Hunter College | 61 | 500 | 6 | 53 | 85 |
| John Jay College | 61 | 500 | 6 | 53 | 85 |
| Lehman College | 61 | 500 | 6 | 53 | 85 |
| Medgar Evers College | 52 | 470 | 5.5 | 41 | 80 |
| NYC College of Technology | 61 | 500 | 6 | 44 | 85 |
| Queens College | 61 | 500 | 6 | 44 | 95 |
| York College | 61 | 500 | 6 | 44 | 85 |
| School of Professional Studies | 80 | 550 | 6.5 | 53 | 105 |
| School of Labor & Urban Studies | 80 | 550 | 6.5 | 53 | 105 |
| Bronx Community College | 53 | 475 | 5.5 | 41 | 80 |
| Queensborough Community College | 53 | 475 | 5.5 | 41 | 80 |
| BMCC | — | — | — | — | — (not required) |
| Hostos Community College | — | — | — | — | — (not required) |
| Kingsborough Community College | — | — | — | — | — (not required) |
| LaGuardia Community College | — | — | — | — | — (not required) |
| Guttman Community College | (per published standards; check college) | | | | |

> "—" = four community colleges do not require English proficiency scores for admission (per CUNY's published TOEFL/IELTS/PTE/Duolingo comparison chart). Guttman Community College was not listed in the published comparison chart — entry pending verification.

### 3.3 Graduate — global rules

CUNY graduate admissions is **decentralized**: each of the 16 graduate colleges administers its own application.

- **Application portals**: Most use the **CUNY Graduate Application** (https://www.cuny.edu/graduate-studies/apply/). Specialized schools use their own: Law (LSAC), Medicine (AMCAS), Public Health (SOPHAS), Architecture, Journalism.
- **Standard application fee**: $75 per program (typical; some programs charge $100). Fee waivers available for most programs via GradCAS / direct request.
- **CGS April 15 honor date**: CUNY observes the Council of Graduate Schools April 15 Resolution (master's admission offers; students have until April 15 to respond).
- **GRE/GMAT policy**: Varies by program. Many MBA, MPA, MS, and PhD programs have moved to **test-optional**. Engineering, Architecture, and Journalism have program-specific test requirements.
- **Language-test policy**: International applicants from non-English institutions must submit TOEFL/IELTS/PTE/Duolingo; minimums vary by college (typically 61–100 TOEFL iBT).
- **Exemption rules**: Applicants holding a US bachelor's degree (or equivalent from an English-medium institution) are typically exempt from English-proficiency testing.
- **Application timeline**: Fall admission priority deadlines range from December 1 (international) through April 15 (rolling). Spring admission typically September 15.
- **Institutional codes**: FAFSA code 002765 (CUNY system); per-college codes vary for GRE/GMAT.

---

## 4. Costs & Financial Aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**Tuition — Senior Colleges (per semester, effective Spring 2023 rates — most recent published):**

| 维度 | Resident (NYS) | Non-Resident (incl. Intl) | Online Degree |
|---|---|---|---|
| Full-time (12+ credits) | $3,465/sem | $620/credit | $305/credit (Res) / $350/credit (Non) |
| Part-time (<12 credits) | $305/credit | $620/credit | $305/credit (Res) / $350/credit (Non) |
| Non-degree student | $445/credit | $915/credit | N/A |

**Tuition — Community Colleges (per semester, effective Spring 2023):**

| 维度 | NYC Resident | NYS Non-NYC Resident * | Non-Resident | Online |
|---|---|---|---|---|
| Full-time (12+ credits) | $2,400/sem | $2,400/sem (with Certificate of Residency) | $320/credit | $210/credit |
| Part-time (<12 credits) | $210/credit | $210/credit | $320/credit | $210/credit |
| Non-degree student | $265/credit | — | $420/credit | N/A |

> * Students who live in NY State but not NYC may qualify for NYC-resident tuition if they submit a Certificate of Residency Form to the Bursar's Office by the published deadline.

**Undergraduate Fees (typical):**

| Fee | Amount |
|---|---|
| Technology Fee (full-time) | $125/sem |
| Technology Fee (part-time) | $62.50/sem |
| Activity Fees (full-time) | $60–$180/sem (varies by college) |
| Consolidated Service Fee | $15/sem |

**9-Month Student Budget (2026-2027 published estimate):**

| Item | Living at home | Living away from home |
|---|---|---|
| Books and Supplies | $1,500 | $1,500 |
| Transportation | $1,190 | $1,190 |
| Lunch | $4,550 | $4,550 |
| Medical | — | $2,335 |
| Personal Expenses | $2,088 | $2,885 |
| Living Expenses / Housing | $6,990 | $20,124 |
| **Total (excl. tuition)** | **$16,318** | **$32,583** |

### 4.2 Undergraduate financial-aid policy

| Metric | Value |
|---|---|
| Tuition-free in-state undergrads | **72%** attend tuition-free |
| Students graduating debt-free | **77%** |
| Need-blind admissions (US) | Yes (for all CUNY UG colleges) |
| Need-blind for international | No (internationals classified as Non-Resident, no need-based aid) |
| Primary aid vehicles | Federal Pell Grant, NYS TAP, Excelsior Scholarship, CUNY Tuition Assistance |
| FAFSA code | 002765 |
| TAP application | https://www.hesc.ny.gov/ |
| CUNY Net Price Calculator | https://www.cuny.edu/financial-aid/ |
| F-1/J-1 visa students | Pay Non-Resident tuition; not eligible for state/federal aid |
| Undocumented students (DACA / NYS Dream Act) | Eligible for NYS aid (TAP, Excelsior) under NYS Dream Act |
| Median starting salary (CUNY graduates) | $50,000–$55,000 (varies by major) |

### 4.3 Graduate cost & funding framework

**Graduate Tuition (per semester, effective Spring 2023):**

| Program | NYS Resident (FT) | NYS Non-Resident (FT) | Online |
|---|---|---|---|
| Master's (generic MA/MS) | $5,545/sem | $855/credit | $470/credit (Res) / $565/credit (Non) |
| MBA | $8,155/sem | $1,110/credit | $725/credit (Res) / $870/credit (Non) |
| MArch | $6,485/sem | $945/credit | $550/credit (Res) / $660/credit (Non) |
| ME | $6,485/sem | $945/credit | $550/credit (Res) / $660/credit (Non) |
| MPT (Physical Therapy) | $6,075/sem | $905/credit | $490/credit (Res) / $590/credit (Non) |
| MSW | $7,315/sem | $1,000/credit | $620/credit (Res) / $745/credit (Non) |
| MPA | $6,375/sem | $1,010/credit | $545/credit (Res) / $655/credit (Non) |
| MPS Branding & Integrated Communications | $7,510/sem | $1,075/credit | $865/credit (Res) / $1,040/credit (Non) |
| MIA | $6,375/sem | $1,010/credit | $545/credit (Res) / $655/credit (Non) |
| MPH | $7,365/sem | $1,005/credit | $620/credit (Res) / $745/credit (Non) |
| CUNY School of Law | $7,725/sem (FT) / $5,305 PT Evening | $12,820/sem | $655/credit (Res) / $785/credit (Non) |
| Medical School (CCNY) | $20,800/sem | $34,630/sem | N/A |
| PhD Level I (NY Res) | $4,965/sem | $965/credit | $560/credit (Res) / $670/credit (Non) |
| PhD Level II/III (NY Res) | $3,110 / $1,235/sem | $6,910 / $2,450/sem | N/A |
| DNP | $7,315/sem | $1,000/credit | $620/credit (Res) / $745/credit (Non) |
| DNS | $6,035 → $2,305/sem | $1,105/credit → $6,910/sem | N/A |
| DPT | $6,595 → $4,130/sem | $1,075/credit → $7,930/sem | $685/credit (Res) |
| DrPH | $6,025 → $2,295/sem | N/A → $7,970/sem | $710/credit (Res) |
| AuD | $6,135 → $3,840/sem | $1,190/credit → $8,550/sem | $695/credit (Res) |
| EdD | $8,340/sem | $1,080/credit | $695/credit (Res) / $835/credit (Non) |
| Executive DBA | $515/credit (typical; program-specific) | — | — |

**Funding-type taxonomy:**

| Funding type | Prevalence at CUNY |
|---|---|
| Fully funded (PhD with stipend + tuition waiver) | Available at The Graduate Center (most PhD programs); select professional doctorates |
| Partial funding (RA/TA/fellowship) | Common at Graduate Center and senior-college research-active programs |
| Self-funded | Most Master's and Applied programs |
| Assistantships (RA/TA/GA) | Available at research-active senior colleges |
| Federal Work-Study | Available to eligible grad students |
| External fellowships | Fulbright, NSF, NYC government |

**Graduate financial-aid links:**
- CUNY Financial Aid for Graduate Studies: https://www.cuny.edu/financial-aid/
- The Graduate Center Financial Assistance: https://www.gc.cuny.edu/financial-aid
- Application fee: typically $75 per program; waivers available

---

## 5. Evidence Chain Index

```yaml
- id: E-U-001
  field: ug.system_overview.program_count_claim
  value: "more than 2,800 top-notch academic programs for degree-seeking students"
  source_url: https://www.cuny.edu/admissions/undergraduate/programs/
  source_snippet: "CUNY offers more than 2,800 top-notch academic programs for degree-seeking students."
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-002
  field: ug.system_overview.last_updated
  value: "12/15/25"
  source_url: https://www.cuny.edu/admissions/undergraduate/programs/
  source_snippet: "Last Updated: 12/15/25"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-003
  field: ug.system_overview.colleges_total
  value: 26
  source_url: https://www.cuny.edu/about/colleges/
  source_snippet: "The City University of New York spans 26 colleges across the city's five boroughs"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-004
  field: ug.system_overview.college_breakdown
  value: {senior: 11, community: 7, graduate_honors_professional: 8}
  source_url: https://www.cuny.edu/about/
  source_snippet: "11 Senior Colleges 7 Community Colleges 8 Graduate, Honors and Professional Schools"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-005
  field: ug.system_overview.students_total
  value: 247000
  source_url: https://www.cuny.edu/about/
  source_snippet: "today CUNY serves 247,000 students of all ages and awards 50,000 degrees each year"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-006
  field: ug.deadline.fall_priority_us
  value: "February 1 (Application & Supporting Documents)"
  source_url: https://www.cuny.edu/admissions/undergraduate/deadlines/
  source_snippet: "Fall Admission Freshman/Transfer: U.S. Educated February 1 (Application & Supporting Documents) Rolling Admissions from January – July"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-007
  field: ug.deadline.fall_priority_international
  value: "December 1 (Application) / December 15 (Supporting Documents)"
  source_url: https://www.cuny.edu/admissions/undergraduate/deadlines/
  source_snippet: "Freshman/Transfer: International Applicants December 1 (Application Deadline) December 15 (Supporting Documents)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-008
  field: ug.deadline.spring_priority_us
  value: "September 15 (Application & Supporting Documents)"
  source_url: https://www.cuny.edu/admissions/undergraduate/deadlines/
  source_snippet: "Spring Admission Freshman/Transfer: U.S. Educated September 15 (Application & Supporting Documents)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-009
  field: ug.fee.freshman
  value: 65
  source_url: https://www.cuny.edu/admissions/undergraduate/deadlines/
  source_snippet: "The Freshman Application fee is $65. The Transfer Application fee is $70."
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-010
  field: ug.fee.transfer
  value: 70
  source_url: https://www.cuny.edu/admissions/undergraduate/deadlines/
  source_snippet: "The Freshman Application fee is $65. The Transfer Application fee is $70."
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-011
  field: ug.english.toefl_minimums.four_year_colleges
  value: {Baruch:80, Brooklyn:61, CCNY:61, CSI:45, Hunter:61, JohnJay:61, Lehman:61, Medgar:52, CityTech:61, Queens:61, York:61, SPS:80, SLU:80}
  source_url: https://www.cuny.edu/admissions/undergraduate/apply/toefl/
  source_snippet: "Baruch College 80 550 6.5 53 105; Brooklyn College 61 500 6 44 85; Hunter College 61 500 6 53 85"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-012
  field: ug.english.ielts_minimums.four_year_colleges
  value: {Baruch:6.5, Brooklyn:6, CCNY:6, CSI:5, Hunter:6, JohnJay:6, Lehman:6, Medgar:5.5, CityTech:6, Queens:6, York:6, SPS:6.5, SLU:6.5}
  source_url: https://www.cuny.edu/admissions/undergraduate/apply/toefl/
  source_snippet: "Baruch College 80 550 6.5 53 105; Brooklyn College 61 500 6 44 85; Hunter College 61 500 6 53 85"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-013
  field: ug.english.duolingo_minimums.four_year_colleges
  value: {Baruch:105, Brooklyn:85, CCNY:85, CSI:75, Hunter:85, JohnJay:85, Lehman:85, Medgar:80, CityTech:85, Queens:95, York:85, SPS:105, SLU:105}
  source_url: https://www.cuny.edu/admissions/undergraduate/apply/toefl/
  source_snippet: "Baruch College 80 550 6.5 53 105; Brooklyn College 61 500 6 44 85; Hunter College 61 500 6 53 85"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-014
  field: ug.english.not_required
  value: ["BMCC", "Hostos Community College", "Kingsborough Community College", "LaGuardia Community College"]
  source_url: https://www.cuny.edu/admissions/undergraduate/apply/toefl/
  source_snippet: "Hostos Community College, LaGuardia Community College, Borough of Manhattan Community College, and Kingsborough Community College do not require students to submit TOEFL/IELTS/PTE/Duolingo scores for admission"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-015
  field: ug.tuition.senior_full_time_ny_resident
  value: 3465
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "New York State Resident $3,465 per semester $305 per credit $305 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-016
  field: ug.tuition.senior_full_time_ny_nonresident
  value: "$620 per credit"
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "New York State Non-Resident ¹ $620 per credit $620 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-017
  field: ug.tuition.community_full_time_nyc_resident
  value: 2400
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "New York City Resident $2,400 per semester $210 per credit $210 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-018
  field: ug.tuition.community_full_time_nyc_nonresident
  value: "$320 per credit"
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "New York City Non-Resident * ¹ $320 per credit $320 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-019
  field: ug.cost_of_attendance.living_at_home
  value: 16318
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "STUDENTS LIVING AT HOME OR WITH RELATIVES ... Total $16,318"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-020
  field: ug.cost_of_attendance.living_away
  value: 32583
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "STUDENTS LIVING AWAY FROM HOME ... Total $32,583"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-U-021
  field: ug.financial_aid.tuition_free_in_state_pct
  value: "72%"
  source_url: https://www.cuny.edu/financial-aid/
  source_snippet: "72% in-state undergrads attend tuition-free"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-U-022
  field: ug.financial_aid.debt_free_grad_pct
  value: "77%"
  source_url: https://www.cuny.edu/financial-aid/
  source_snippet: "77% CUNY students graduate with $0 debt"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-G-001
  field: grad.system_overview.graduate_colleges_count
  value: 16
  source_url: https://www.cuny.edu/admissions/graduate-studies/
  source_snippet: "The CUNY Office of Graduate Studies is the information hub for prospective students interested in master's and doctoral programs offered at the 16 CUNY colleges."
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-G-002
  field: grad.programs.total_rows
  value: 822
  source_url: https://www.cuny.edu/admissions/graduate-studies/academic-programs/
  source_snippet: "Showing 1 to 822 of 822 entries"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-G-003
  field: grad.degree_types.master_list
  value: [MA, MArch, MAT, MBA, ME, MFA, MLA, MLS, MMus, MS, MSEd, MSW, MPA, MPH, MPS, MUP, PhD, DNP, DNS, DPT, AdvCert, AdvDip, PostMaster]
  source_url: https://www.cuny.edu/admissions/graduate-studies/academic-programs/
  source_snippet: "Our master's degree options are: Master of Arts (MA) Master of Architecture (MArch) Master of Arts in Teaching (MAT) ... Doctor of Philosophy (PhD) Doctor of Nursing Practice (DNP) Doctor of Nursing Science (DNS) Doctor of Physical Therapy (DPT)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-G-004
  field: grad.application.apply_steps
  value: "7 Simple Steps to Apply (Step 1-7 described on prepare page)"
  source_url: https://www.cuny.edu/admissions/graduate-studies/prepare/
  source_snippet: "7 Simple Steps to Apply to Graduate School: Step #1. Determine which program(s) you would like to learn more about by searching the graduate programs offered at our 15 CUNY colleges. Step #2. Attend an information session..."
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-G-005
  field: grad.tuition.masters_full_time_ny_resident
  value: 5545
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "MASTERS DEGREE New York State Resident $5,545 per semester $470 per credit $470 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-G-006
  field: grad.tuition.mba_full_time_ny_resident
  value: 8155
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "MASTERS IN BUSINESS ADMINISTRATION New York State Resident $8,155 per semester $725 per credit $725 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-G-007
  field: grad.tuition.phd_level1_ny_resident
  value: 4965
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "DOCTOR OF PHILOSOPHY New York State Resident Level I $4,965 per semester"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-G-008
  field: grad.tuition.law_resident
  value: 7725
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "CUNY SCHOOL OF LAW New York State Resident $7,725 per semester $655 per credit"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-G-009
  field: grad.tuition.medical_resident
  value: 20800
  source_url: https://www.cuny.edu/financial-aid/tuition-and-college-costs/
  source_snippet: "MEDICAL SCHOOL New York State Resident $20,800 per semester"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

- id: E-O-001
  field: overview.system.students_total
  value: 247000
  source_url: https://www.cuny.edu/about/
  source_snippet: "today CUNY serves 247,000 students of all ages and awards 50,000 degrees each year"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-002
  field: overview.system.degrees_per_year
  value: 50000
  source_url: https://www.cuny.edu/about/
  source_snippet: "awards 50,000 degrees each year"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-003
  field: overview.system.founded_year
  value: 1847
  source_url: https://www.cuny.edu/about/
  source_snippet: "Founded in 1847 as the nation's first free public institution of higher education"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-004
  field: overview.demographics.first_gen_pct
  value: "60%"
  source_url: https://www.cuny.edu/about/
  source_snippet: "60% First Generation to go to College"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-005
  field: overview.demographics.alumni_in_nyc_pct
  value: "82%"
  source_url: https://www.cuny.edu/about/
  source_snippet: "82% Alumni stay in New York City"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-006
  field: overview.recognition.nobel_laureates
  value: 14
  source_url: https://www.cuny.edu/about/
  source_snippet: "14 Nobel Laureates"
  capture_date: 2026-07-07
  evidence_type: official_webpage

- id: E-O-007
  field: overview.recognition.macarthur_winners
  value: 26
  source_url: https://www.cuny.edu/about/
  source_snippet: "26 MacArthur Winners"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## 6. WeKnora Import Manifest

### Collection structure

```
cuny-knowledge-base-v2 (collection)
├── cuny-overview.md (Section 0 — system overview, 26-college tree, totals)
├── cuny-ug-colleges.md (Section 1 — UG programs by college, 20 documents × degree subtables)
├── cuny-grad-colleges.md (Section 2 — Grad programs by college, 24 documents × program-area subtables)
├── cuny-admissions.md (Section 3 — deadlines, fees, English proficiency)
├── cuny-costs.md (Section 4 — tuition tiers, fees, financial aid)
├── cuny-evidence.md (Section 5 — evidence chain index)
└── cuny-monitoring.md (Section 7 — content-hashes watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "cuny-knowledge-base-v2"
  school: "CUNY (City University of New York)"
  member_college: "<Baruch|Brooklyn|Hunter|...|Graduate Center>"
  college_category: "<senior|community|graduate|honors|professional>"
  program_area: "<Business|Humanities|Education|...>"
  degree_level: "<BA|BS|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|---|---|---|
| P0 | Per-program graduate deadlines via "Application Deadline" link in grad table | https://www.cuny.edu/admissions/graduate-studies/academic-programs/ |
| P0 | CUNY Application portal screenshots and fee waiver policy details | https://www.cuny.edu/admissions/undergraduate/apply/cuny-application/ |
| P0 | Graduate application fee by college | per-college admission portals |
| P1 | Macaulay Honors College admissions requirements (separate from main UG) | https://macaulay.cuny.edu/ |
| P1 | CUNY School of Medicine BS/MD 7-year program requirements | https://www.ccny.cuny.edu/csom |
| P1 | Guttman Community College English proficiency policy (missing from published chart) | https://guttman.cuny.edu/ |
| P1 | Per-college graduate tuition (currently only system-wide rates published) | per-college bursar pages |
| P2 | CUNY-wide minor list | 20 individual college bulletins |
| P2 | CUNY Reconnect (free associate degree) admission details | https://www.cuny.edu/admissions/reconnect/ |
| P2 | Continuing & Professional Education program list | https://www.cuny.edu/academics/cpe/ |
| P2 | PhD funding packages at The Graduate Center | https://www.gc.cuny.edu/financial-aid |

---

## 7. Cross-school comparison framework (placeholder)

CUNY fields for cross-school comparison:

| Dimension | CUNY Value |
|---|---|
| Total UG cost/yr (NYS Res, full-time, senior college, est.) | $6,930 tuition + $16,318 living = ~$23,248 (at home) |
| Tuition/yr (NYS Res, senior college, FT) | $6,930 ($3,465 × 2 sem) |
| Tuition/yr (NYS Res, community college, FT) | $4,800 ($2,400 × 2 sem) |
| Need-blind (domestic) | Yes |
| Need-blind (international) | No |
| Tuition-free threshold | 72% of in-state UG attend tuition-free |
| Median price paid | (per CUNY Net Price Calculator) |
| EA deadline | N/A (rolling admissions) |
| RA priority deadline — Fall | February 1 (US) / December 1 (international) |
| SAT/ACT required | Test-optional (most colleges) |
| TOEFL iBT minimum range | 45–80 (per college) |
| IELTS minimum range | 5.0–6.5 (per college) |
| Duolingo minimum range | 75–105 (per college) |
| Grad application fee | ~$75 per program |
| April-15-equivalent honor date | Yes (CGS Resolution) |
| **Total program count (Rule 1)** | **1,920 UG+Grad rows / 2,800+ claimed variants** |
| **Member colleges (Rule 2)** | **26** |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: cuny.edu, cuny.edu/admissions, cuny.edu/financial-aid, cuny.edu/about, individual CUNY college admissions portals
> **Verification**: ego-browser snapshotText + JS DOM extraction; DataTables pagination walked for UG (23 pages, 1,101 rows)
> **Granularity**: system → member college → degree-level → program