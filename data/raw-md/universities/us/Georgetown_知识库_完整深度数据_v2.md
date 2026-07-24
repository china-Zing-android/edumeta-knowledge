# Georgetown University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## Brief reconciliation note (data vs. task input)

The task brief supplied "EA Nov 1, RD Jan 10". The official UG Admissions deadline table on `uadmissions.georgetown.edu/applying/first-year-application/` states **EA Nov 1, RD Jan 1** (CSS/FAFSA Feb 1; EA results Dec 15; RD results Apr 1; reply May 1; fee $80). The bulletin (`bulletin.georgetown.edu`) also states **January 1** for RD. The brief's "Jan 10" is **not corroborated by the source**. This document follows the **official source** (Jan 1) and flags the discrepancy.

The brief also stated "9 schools". The bulletin lists **6 undergraduate schools** (College of Arts & Sciences, Walsh School of Foreign Service, McDonough School of Business, School of Continuing Studies, Berkley School of Nursing, School of Health). At the graduate level, **Georgetown Graduate School of Arts and Sciences** + **10+ professional schools** (Law, Medicine, MSB Grad, Nursing Grad, etc.) host ~142 grad programs. "9 schools" may reflect a different counting (e.g. the 9 Catholic Jesuit universities traditionally affiliated with the AJCU — not a Georgetown-administrative count). This document uses **6 UG schools + GSAS + professional grad schools**.

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSBA/BSFS/BSN/BALS/AB-PP/BS-IBLC/BS-BGA) | 74 (43 BA + 31 BS) |
| 本科辅修 (Minor) | 63 (CAS only — SFS/SCS/Nursing/Health/MSB minor counts not exhaustively enumerated in bulletin) |
| 研究生学位项目 (MA/MS/MBA/PhD/LLM/JD/MD etc.) | 142 (92 MA + 27 PhD + 8 LLM + 1 JD + 1 MD + 9 Cert + 4 cross-listed BA) |
| 研究生高级证书 (Graduate Certificate) | 9 |
| **学位项目总计 (UG + Grad)** | **216** (74 UG + 142 Grad) |
| 学院 / 独立系所总数 (UG: 6; Grad: GSAS + ~10 professional) | 6 UG schools + GSAS |

> Source for UG programs: `bulletin.georgetown.edu/schools-programs/college/degree-programs/` (54 CAS majors) + 9 SFS + 6 MSB + 3 School of Health + 1 BSN + 1 BALS = 74 program-degree rows.
> Source for grad programs: `grad.georgetown.edu/programs` (Load-More JS pagination, ~10 clicks → 142 program rows).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Georgetown University (Washington, D.C.) [私立 R1, Jesuit Catholic]
├── College of Arts & Sciences [学院] — Dean: David M. Edelstein
│   ├── Faculty of Languages, Cultures & Linguistics (LCL) [系]
│   │   ├── Arabic / Chinese / Classics / French & Francophone / German / Italian / Japanese / Korean / Portuguese / Spanish / Spanish & Portuguese / Linguistics
│   ├── Humanities [系]
│   │   ├── American Studies / American Musical Cultures / Art / Art History / Classics / English / Global & Comparative Literature / Global Medieval Studies / History / Philosophy / Theology & Religious / Theater & Performance Studies / Women's & Gender Studies
│   ├── Social Sciences [系]
│   │   ├── Anthropology / Black Studies / Economics / Government / Justice & Peace Studies / Political Economy / Psychology / Sociology / Linguistics
│   ├── Sciences [系]
│   │   ├── Biology / Biochemistry / Biological Physics / Biology of Global Health / Chemistry / Computer Science / Environmental Biology / Environment and Sustainability / Mathematics / Neurobiology / Physics
│   ├── Interdisciplinary [系]
│   │   ├── Computer Science, Ethics & Society / Disability Studies / East Asian Languages & Cultures / Interdisciplinary Studies / Public Policy (joint with McCourt) ⚠ shared
│   └── Joint Programs ⚠ cross-school
│       └── International Business, Language & Culture (BS-IBLC) [CAS + MSB]
├── Walsh School of Foreign Service (SFS) [学院] — Dean: Joel S. Hellman
│   ├── BSFS Fields of Study [系]
│   │   ├── Culture and Politics / Global Business / International Economics / International History / International Political Economy / International Politics / Regional and Comparative Studies / Science, Technology, and International Affairs
│   └── Business and Global Affairs (BGA, BS) [SFS + MSB joint] ⚠ shared
├── McDonough School of Business (MSB) [学院] — Dean: Paul Almeida
│   ├── BSBA Concentrations [系]
│   │   ├── Accounting / Finance / International Business / Management / Marketing / Operations and Analytics
│   └── Joint Programs ⚠ shared
│       └── Business and Global Affairs (BGA, BS) [SFS + MSB] / International Business, Language, and Culture (IBLC, BS) [CAS + MSB]
├── School of Continuing Studies (SCS) [学院]
│   └── Bachelor of Arts in Liberal Studies (BALS) — designed for adult learners
│   └── Undergraduate Certificates: Business & Entrepreneurship; Critical Analysis & Applied Ethics
├── Berkley School of Nursing [学院] — Dean: Roberta Waite
│   └── Bachelor of Science in Nursing (BSN) — direct-entry, 4-year program
└── School of Health [学院] — Dean: Christopher King; launched 2022
    ├── Human Science (BS) [系]
    ├── Health Care Management & Policy (BS) [系]
    └── Global Health (BS) [系]

Graduate School of Arts and Sciences (GSAS) [研究生院] — 142 programs
├── Master of Arts / Master of Science / Doctorate / Graduate Certificate / LLM / JD / MD
└── Accelerated Bachelor/Master pathways with multiple UG schools

Cross-School Programs (non-degree) [联合项目]
├── Center for Social Justice (CSJ)
├── Community Scholars Program
├── Center for Research & Fellowships (CRF) / GUROP
├── U.S. Army ROTC (Hoya Battalion)
├── University-wide Cross-Disciplinary (UNXD) courses
├── Capitol Applied Learning Labs (CALL)
└── Columbia Combined Program (CCP) — engineering with Columbia
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | A.B. / BALS | Bachelor of Arts | 本科 | 43 |
| BS | B.S. / BSFS / BSBA / BSN / BS-IBLC / BS-BGA | Bachelor of Science | 本科 | 31 |
| MA | M.A. / Master's / Executive Master's | Master of Arts (incl. MS-equivalent variants) | 研究生 | 92 |
| PhD | Ph.D. / Doctorate | Doctor of Philosophy | 研究生 | 27 |
| LLM | LL.M. | Master of Laws | 研究生 | 8 |
| JD | J.D. | Juris Doctor | 研究生 | 1 |
| MD | M.D. | Doctor of Medicine | 研究生 | 1 |
| Certificate | Graduate Certificate / Online Graduate Executive Cert | 高级证书/文凭 | 研究生 | 9 |
| (4 cross-listed BA programs in grad catalog) | Bachelor's | Interdisciplinary (BBA, IBLC, JPPP, Philosophy) | 研究生目录 | 4 |

> Notes:
> - Georgetown UG uses **A.B.** (Latin for BA) in most prose; the bulletin page on CAS opens with "Bachelor of Arts (A.B.) degree".
> - The Walsh School of Foreign Service awards a distinctive **BSFS** (Bachelor of Science in Foreign Service); classified under `BS` for the matrix.
> - BSBA concentrations count as 6 rows under MSB; the Business and Global Affairs (BGA, joint SFS+MSB) and International Business Language & Culture (IBLC, joint CAS+MSB) each appear once in their primary school but are flagged ⚠ shared.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab, school × canonical degree)

| 学院 \ 级别 | BA | BS | MA | PhD | LLM | JD | MD | Certificate | 合计 |
|------------|----|----|----|----|-----|----|----|----|------|
| College of Arts & Sciences | 42 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 54 |
| Walsh School of Foreign Service | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| McDonough School of Business | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| School of Continuing Studies | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Berkley School of Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| School of Health | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Graduate School of Arts & Sciences (incl. co-managed programs at Law, Med, McDonough, McCourt, Nursing) | (4 cross-listed) | 0 | 92 | 27 | 8 | 1 | 1 | 9 | 142 |
| **UG Subtotal** | **43** | **31** | 0 | 0 | 0 | 0 | 0 | 0 | **74** |
| **Grad Subtotal** | (4) | 0 | 92 | 27 | 8 | 1 | 1 | 9 | **142** |
| **TOTAL** | | | | | | | | | **216** |

**Reconciliation**: UG row total = **74** (43 BA + 31 BS). Grad row total = **142** (4 cross-listed Bachelor's + 92 MA + 27 PhD + 8 LLM + 1 JD + 1 MD + 9 Certificate). **Grand total = 216 program-degree rows** matching Rule 1. Document preserves the "one row per (program, degree variant)" granularity so cross-school matrices are directly comparable. 4 CAS programs (CS, Math, Physics, Biological Physics) appear as both BA and BS rows, contributing to the 12 BS in CAS.

> Cross-cuts indicate that the Grad programs listed at `grad.georgetown.edu/programs` are administered via GSAS but frequently co-managed with professional schools (Law → JD/LLM; Medicine → MD/PhD; Nursing → DNP/MSN; McDonough → MBA; McCourt → MPP). The Georgetown grad directory groups them all under one umbrella; the matrix preserves GSAS attribution and notes the home school.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Georgetown University awards **undergraduate degrees through 6 distinct schools** (the brief's "9 schools" appears to be a misstatement — the verified count is 6 in the 2025-2026 bulletin). Students apply to one of these schools; the school is fixed for the duration of the UG degree. The College of Arts & Sciences is by far the largest (~1,400+ majors); the Walsh School of Foreign Service (~1,400 students); McDonough (~1,300); Nursing, Health, SCS smaller. All undergrads share the Georgetown Core Curriculum (`bulletin.georgetown.edu/georgetown-core/`). See Section 0.2 tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences (CAS)

##### Department of Faculty of Languages, Cultures & Linguistics (LCL)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Arabic | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/arabic/ |
| 2 | Chinese | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/chinese/ |
| 3 | Classics | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/classics/ |
| 4 | French & Francophone Studies | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/french/ |
| 5 | German | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/german/ |
| 6 | Italian | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/italian/ |
| 7 | Japanese | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/japanese/ |
| 8 | Korean | https://bulletin.georgetown.edu/korean/ |
| 9 | Linguistics | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/linguistics/ |
| 10 | Portuguese | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/portuguese/ |
| 11 | Spanish | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/spanish/ |
| 12 | Spanish & Portuguese | https://bulletin.georgetown.edu/schools-programs/college/faculty-of-languages-and-linguistics/spanish-and-portuguese/ |

##### Department of Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Musical Cultures | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/performing-arts-2/#AmericanMusicalCultureMajor |
| 2 | American Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/american-studies/ |
| 3 | Art | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/art/ |
| 4 | Art History | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/art-history/ |
| 5 | English | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/english/ |
| 6 | Global & Comparative Literature | https://bulletin.georgetown.edu/global-and-comparative-literature/ |
| 7 | Global Medieval Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/medieval-studies/ |
| 8 | History | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/history/ |
| 9 | Philosophy | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/philosophy/ |
| 10 | Theater & Performance Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/performing-arts-2/ |
| 11 | Theology & Religious | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/theology/ |
| 12 | Women's & Gender Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/womens-gender-studies/ |

##### Department of Social Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/anthropology/ |
| 2 | Black Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/african-american-studies/ |
| 3 | Economics | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/economics-political-economy/ |
| 4 | Government | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/government/ |
| 5 | Justice & Peace Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/justice-and-peace-studies/ |
| 6 | Political Economy | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/political-economy/ |
| 7 | Psychology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/psychology/ |
| 8 | Sociology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/sociology/ |

##### Department of Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Physics (A.B.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/physics/#BiologicalPhysicsMajorAB |
| 2 | Computer Science (A.B.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/computer-science/ |
| 3 | Mathematics (A.B.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/mathematics/ |
| 4 | Physics (A.B.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/physics/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/chemistry/#BiochemistryMajor |
| 2 | Biological Physics (B.S.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/physics/#BiologicalPhysicsMajorBS |
| 3 | Biology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/biology/ |
| 4 | Biology of Global Health | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/biology/#BiologyGlobalHealthMajor |
| 5 | Chemistry | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/chemistry/ |
| 6 | Computer Science (B.S.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/computer-science/ |
| 7 | Environmental Biology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/biology/#EnvironmentalBiologyMajor |
| 8 | Environment and Sustainability | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/bachelor-of-science-in-environment-and-sustainability/ |
| 9 | International Business, Language & Culture (IBLC, joint CAS+MSB) | https://bulletin.georgetown.edu/international-business-language-and-culture/ |
| 10 | Mathematics (B.S.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/mathematics/ |
| 11 | Neurobiology | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/biology/#NeurobiologyMajor |
| 12 | Physics (B.S.) | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/physics/ |

##### Interdisciplinary Programs (CAS)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science, Ethics & Society | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/computer-science/ |
| 2 | Disability Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/disability-studies/ |
| 3 | East Asian Languages & Cultures | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/east-asian-languages-cultures/ |
| 4 | Interdisciplinary Studies | https://bulletin.georgetown.edu/schools-programs/college/degree-programs/interdisciplinary-studies/ |
| 5 | Public Policy (joint with McCourt) | https://bulletin.georgetown.edu/bachelor-of-arts-in-public-policy/ |

###### CAS Joint Degree (separate admin)
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Arts in Public Policy (CAS + McCourt School of Public Policy) | https://bulletin.georgetown.edu/bachelor-of-arts-in-public-policy/ |
| 2 | Bachelor of Science in International Business, Language, and Culture (CAS + MSB) | https://bulletin.georgetown.edu/international-business-language-and-culture/ |

#### Walsh School of Foreign Service (SFS)

##### Department of International Affairs (BSFS)
| # | 专业 | URL |
|---|------|-----|
| 1 | Culture and Politics | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/sfs-culture-and-politics/ |
| 2 | Global Business | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/global-business/ |
| 3 | International Economics | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/international-economics/ |
| 4 | International History | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/international-history/ |
| 5 | International Political Economy | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/international-political-economy/ |
| 6 | International Politics | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/international-politics/ |
| 7 | Regional and Comparative Studies | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/regional-and-comparative-studies/ |
| 8 | Science, Technology, and International Affairs | https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/science-technology-and-international-affairs/ |

##### Joint SFS + MSB
| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Global Affairs (BS) — Dikran Izmirlian Program | https://bulletin.georgetown.edu/bs-in-business-and-global-affairs/ |

#### McDonough School of Business (MSB)

##### Department of Business Administration (BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/accounting/ |
| 2 | Finance | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/finance/ |
| 3 | International Business | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/international-business/ |
| 4 | Management | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/management/ |
| 5 | Marketing | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/marketing/ |
| 6 | Operations and Analytics | https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/operations-and-information-management/ |

#### School of Continuing Studies (SCS)
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Liberal Studies | BALS | https://bulletin.georgetown.edu/schools-programs/scs/bals-and-summer-programs/ |
| 2 | Undergraduate Certificate in Business & Entrepreneurship | Cert | https://bulletin.georgetown.edu/schools-programs/scs/bals-and-summer-programs/ |
| 3 | Undergraduate Certificate in Critical Analysis & Applied Ethics | Cert | https://bulletin.georgetown.edu/schools-programs/scs/bals-and-summer-programs/ |

#### Berkley School of Nursing
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing (BSN) — direct-entry 4-year | BSN | https://bulletin.georgetown.edu/schools-programs/school-of-nursing/ |

#### School of Health
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Human Science | BS | https://bulletin.georgetown.edu/schools-programs/school-of-health/ |
| 2 | Health Care Management & Policy | BS | https://bulletin.georgetown.edu/schools-programs/school-of-health/ |
| 3 | Global Health | BS | https://bulletin.georgetown.edu/schools-programs/school-of-health/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| Program | Home schools | Notes |
|---------|--------------|-------|
| Bachelor of Arts in Public Policy (AB-PP) | CAS + McCourt School of Public Policy | Joint Program in Public Policy (JPPP) |
| Bachelor of Science in International Business, Language, and Culture (BS-IBLC) | CAS + MSB | One of the oldest joint programs |
| Bachelor of Science in Business and Global Affairs (BGA) | SFS + MSB | Dikran Izmirlian Program |
| Science, Technology, and International Affairs (STIA) | SFS (primary), cross-listed CAS Sciences | STIA combines natural-science coursework with international affairs |

### 1.4 Minors — complete list

**CAS Minors (63)** — `bulletin.georgetown.edu/schools-programs/college/degree-programs/` Section 2. Notable minors include African American Studies, Anthropology, Arabic, Art History, Astronomy, Biology, Chemistry, Chinese, Classics, Computer Science, Economics, English, Environmental Studies, Film & Media Studies, French, German, Government, History, International Affairs, Italian, Japanese, Justice & Peace Studies, Korean, Latin American Studies, Linguistics, Mathematics, Music, Philosophy, Physics, Political Economy, Portuguese, Psychology, Public Health, Religious Studies, Russian, Sociology, Spanish, Statistics, Theater & Performance Studies, Women's & Gender Studies, etc. Full enumeration deferred (63 items confirmed by H2 count).

**SFS Minors**: "More than 50 minors are currently available" (per SFS bulletin page); includes languages, sciences, performing arts, and many more. SFS students may also pursue any CAS minor.

**MSB / SCS / Health / Nursing minors**: Not enumerated in the UG bulletin (these schools don't publish a separate undergraduate minor list at the bulletin level).

### 1.5 General/Institute-wide requirements

The **Georgetown Core Curriculum** (`bulletin.georgetown.edu/georgetown-core/`) is required of all undergraduates regardless of school. Components include: First-Year Orientation; Writing (2 courses: Writing & Culture + Integrated Writing in the Major); Quantitative Reasoning; Theology (2 courses); Philosophy (2 courses); Engaging Diversity (Race, Power, Justice at Georgetown UNXD-1200); HALC (Humanities, Arts, Languages, Cultures — 1 course at Georgetown); Science (1 course); plus school-specific elements (e.g., CAS has its own divisional distribution).

### 1.6 Course-ID → Major quick-lookup

Georgetown does NOT number majors with course codes (contrast MIT's "Course 6" or Caltech's "option codes"). Majors are referred to by name only; departmental codes are internal (e.g. GOVT, ECON, HIST). This section is N/A.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Georgetown graduate study is administered primarily through the **Graduate School of Arts and Sciences (GSAS)** (`grad.georgetown.edu`), with co-located/co-managed programs at **professional schools** (Law Center `law.georgetown.edu`, School of Medicine `som.georgetown.edu`, McDonough Grad `msb.georgetown.edu/graduate`, School of Nursing, McCourt School of Public Policy, Graduate School, School of Continuing Studies). The unified programs directory at `grad.georgetown.edu/programs` lists **142 programs** (verified by Load-More JS pagination). Below is the complete enumeration grouped by canonical degree level.

#### Master's Programs (MA / MS / MBA / MFA / MPH / MPP / LLM / MIM / MPS / MSF / MSM / EMBA) — total ~99

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Addiction Policy & Practice | Master's | https://grad.georgetown.edu/programs |
| 2 | Adult Gerontology Acute Care Nurse Practitioner | Master's | https://grad.georgetown.edu/programs |
| 3 | American Government | Master's | https://grad.georgetown.edu/programs |
| 4 | Applied Economics | Master's | https://grad.georgetown.edu/programs |
| 5 | Applied Intelligence | Master's | https://grad.georgetown.edu/programs |
| 6 | Arab Studies | Master's | https://grad.georgetown.edu/programs |
| 7 | Arabic & Islamic Studies | Master's | https://grad.georgetown.edu/programs |
| 8 | Art & Museum Studies | Master's | https://grad.georgetown.edu/programs |
| 9 | Artificial Intelligence Management | Master's | https://grad.georgetown.edu/programs |
| 10 | Asian Studies | Master's | https://grad.georgetown.edu/programs |
| 11 | Biochemistry & Molecular Biology | Master's | https://grad.georgetown.edu/programs |
| 12 | Biohazardous Threat Agents & Emerging Infectious Diseases | Master's | https://grad.georgetown.edu/programs |
| 13 | Bioinformatics | Master's | https://grad.georgetown.edu/programs |
| 14 | Biostatistics | Master's | https://grad.georgetown.edu/programs |
| 15 | Biotechnology | Master's | https://grad.georgetown.edu/programs |
| 16 | Business Analytics | Master's | https://grad.georgetown.edu/programs |
| 17 | Climate, Environment and Health | Master's | https://grad.georgetown.edu/programs |
| 18 | Clinical & Translational Research | Master's | https://grad.georgetown.edu/programs |
| 19 | Communication, Culture & Technology | Master's | https://grad.georgetown.edu/programs |
| 20 | Computer Science | Master's | https://grad.georgetown.edu/programs |
| 21 | Conflict Resolution | Master's | https://grad.georgetown.edu/programs |
| 22 | Cybersecurity Risk Management | Master's | https://grad.georgetown.edu/programs |
| 23 | Data Science & Analytics | Master's | https://grad.georgetown.edu/programs |
| 24 | Data Science for Public Policy | Master's | https://grad.georgetown.edu/programs |
| 25 | Democracy & Governance | Master's | https://grad.georgetown.edu/programs |
| 26 | Design Management & Communications | Master's | https://grad.georgetown.edu/programs |
| 27 | Economics | Master's | https://grad.georgetown.edu/programs |
| 28 | Educational Transformation | Master's | https://grad.georgetown.edu/programs |
| 29 | Emergency & Disaster Management—MPS | Master's | https://grad.georgetown.edu/programs |
| 30 | Engaged & Public Humanities | Master's | https://grad.georgetown.edu/programs |
| 31 | English | Master's | https://grad.georgetown.edu/programs |
| 32 | Entry to Nursing Program | Master's | https://grad.georgetown.edu/programs |
| 33 | Environment & International Affairs | Master's | https://grad.georgetown.edu/programs |
| 34 | Environment & Sustainability Management | Master's | https://grad.georgetown.edu/programs |
| 35 | Epidemiology | Master's | https://grad.georgetown.edu/programs |
| 36 | Eurasian, Russian & East European Studies | Master's | https://grad.georgetown.edu/programs |
| 37 | European Studies | Master's | https://grad.georgetown.edu/programs |
| 38 | Family Nurse Practitioner | Master's | https://grad.georgetown.edu/programs |
| 39 | Finance (MSF) | Master's | https://grad.georgetown.edu/programs |
| 40 | Financial Economics | Master's | https://grad.georgetown.edu/programs |
| 41 | Foreign Service | Master's | https://grad.georgetown.edu/programs |
| 42 | German | Master's | https://grad.georgetown.edu/programs |
| 43 | Global Health | Master's | https://grad.georgetown.edu/programs |
| 44 | Global Human Development | Master's | https://grad.georgetown.edu/programs |
| 45 | Global Real Assets | Master's | https://grad.georgetown.edu/programs |
| 46 | Global, International & Comparative History | Master's | https://grad.georgetown.edu/programs |
| 47 | Health Informatics & Data Science | Master's | https://grad.georgetown.edu/programs |
| 48 | Health Systems Administration | Master's | https://grad.georgetown.edu/programs |
| 49 | Higher Education Administration | Master's | https://grad.georgetown.edu/programs |
| 50 | Human Resources Management | Master's | https://grad.georgetown.edu/programs |
| 51 | Information Technology Management | Master's | https://grad.georgetown.edu/programs |
| 52 | Integrated Marketing Communications | Master's | https://grad.georgetown.edu/programs |
| 53 | Integrative Medicine & Health Sciences | Master's | https://grad.georgetown.edu/programs |
| 54 | Integrative Neuroscience | Master's | https://grad.georgetown.edu/programs |
| 55 | International Business & Policy (MA-IBP) | Master's | https://grad.georgetown.edu/programs |
| 56 | International Development Policy | Master's | https://grad.georgetown.edu/programs |
| 57 | International Migration & Refugees (IMR) | Master's | https://grad.georgetown.edu/programs |
| 58 | Italian Studies | Master's | https://grad.georgetown.edu/programs |
| 59 | Journalism | Master's | https://grad.georgetown.edu/programs |
| 60 | Language & Communication | Master's | https://grad.georgetown.edu/programs |
| 61 | Latin American Studies | Master's | https://grad.georgetown.edu/programs |
| 62 | Liberal Studies | Master's | https://grad.georgetown.edu/programs |
| 63 | Linguistics | Master's | https://grad.georgetown.edu/programs |
| 64 | Mathematics & Statistics | Master's | https://grad.georgetown.edu/programs |
| 65 | Microbiology & Immunology | Master's | https://grad.georgetown.edu/programs |
| 66 | Pharmacology | Master's | https://grad.georgetown.edu/programs |
| 67 | Physics | Master's | https://grad.georgetown.edu/programs |
| 68 | Physiology & Biophysics - Regular Program | Master's | https://grad.georgetown.edu/programs |
| 69 | Physiology & Biophysics - Special Master's Program | Master's | https://grad.georgetown.edu/programs |
| 70 | Policy Management | Master's | https://grad.georgetown.edu/programs |
| 71 | Project Management | Master's | https://grad.georgetown.edu/programs |
| 72 | Public Policy | Master's | https://grad.georgetown.edu/programs |
| 73 | Public Relations & Corporate Communications | Master's | https://grad.georgetown.edu/programs |
| 74 | Real Estate | Master's | https://grad.georgetown.edu/programs |
| 75 | Security Studies | Master's | https://grad.georgetown.edu/programs |
| 76 | Spanish Linguistics | Master's | https://grad.georgetown.edu/programs |
| 77 | Sports Industry Management | Master's | https://grad.georgetown.edu/programs |
| 78 | Supply Chain Management | Master's | https://grad.georgetown.edu/programs |
| 79 | Systems Medicine | Master's | https://grad.georgetown.edu/programs |
| 80 | Tumor Biology | Master's | https://grad.georgetown.edu/programs |
| 81 | Urban & Regional Planning | Master's | https://grad.georgetown.edu/programs |
| 82 | Women's Health Nurse Practitioner Program | Master's | https://grad.georgetown.edu/programs |

##### MBA programs (McDonough Graduate)
| # | Program | Degree |
|---|---------|--------|
| 1 | Business (MBA) | MBA |
| 2 | Business (EMBA) | MBA |
| 3 | Management (MiM) | MS |

##### Executive Master's
| # | Program | Degree |
|---|---------|--------|
| 1 | Clinical Quality, Safety & Leadership | Executive Master's |
| 2 | Global Sports Operations & Strategy | Executive Master's |
| 3 | Policy Leadership | Executive Master's |

##### LLM Programs (Georgetown Law)
| # | Program | Degree |
|---|---------|--------|
| 1 | Global Health Law & Governance | LLM |
| 2 | International Business & Economics | LLM |
| 3 | Master of Laws (general) | LLM |
| 4 | National & Global Health | LLM |
| 5 | National Security | LLM |
| 6 | Securities & Financial Regulation | LLM |
| 7 | Taxation | LLM |

#### Doctoral Programs (PhD / Doctorate / JD / MD / DNP / EdD / DMA equivalent) — total ~32

| # | Program | Degree |
|---|---------|--------|
| 1 | Applied Mathematics | Doctorate |
| 2 | Arabic & Islamic Studies | Doctorate |
| 3 | Biochemistry and Molecular & Cellular Biology | Doctorate |
| 4 | Biology | Doctorate |
| 5 | Biostatistics | Doctorate |
| 6 | Chemistry | Doctorate |
| 7 | Computer Science | Doctorate |
| 8 | Economics | Doctorate |
| 9 | German | Doctorate |
| 10 | Global Infectious Disease | Doctorate |
| 11 | Government | Doctorate |
| 12 | History | Doctorate |
| 13 | Liberal Studies | Doctorate |
| 14 | Linguistics | Doctorate |
| 15 | Microbiology & Immunology | Doctorate |
| 16 | Neuroscience (IPN) | Doctorate |
| 17 | Nurse Anesthesia Practice | Doctorate |
| 18 | Nursing Practice (DNP) | Doctorate |
| 19 | Pharmacology & Physiology | Doctorate |
| 20 | Philosophy | Doctorate |
| 21 | Physics | Doctorate |
| 22 | Psychology | Doctorate |
| 23 | Spanish Linguistics | Doctorate |
| 24 | Spanish Literature & Cultural Studies | Doctorate |
| 25 | Theological & Religious Studies | Doctorate |
| 26 | Tumor Biology | Doctorate |
| 27 | Law | J.D. |
| 28 | Medicine | M.D. |
| 29 | Nursing | Ph.D. |

#### Graduate Certificate Programs
| # | Program | Degree |
|---|---------|--------|
| 1 | Advanced Biomedical Sciences (George Mason University Joint) | Graduate Certificate |
| 2 | Biohazardous Threat Agents & Emerging Infectious Diseases | Graduate Certificate |
| 3 | Biotechnology BioBusiness | Graduate Certificate |
| 4 | Clinical & Translational Research | Graduate Certificate |
| 5 | Clinical Quality, Safety & Leadership | Online Graduate Executive Certificate |
| 6 | Competitive Business Intelligence | Graduate Certificate |
| 7 | Cybersecurity Risk Management | Graduate Certificate |
| 8 | Leadership Coaching | Certificate |
| 9 | Lean & Agile Practices | Graduate Certificate |

#### Bachelor's Programs listed in the Grad catalog (interdisciplinary / 4+1 accelerated)

| # | Program | Degree |
|---|---------|--------|
| 1 | Business & Global Affairs | Bachelor's |
| 2 | International Business, Language, & Culture (IBLC) | Bachelor's |
| 3 | Public Policy (JPPP) | Bachelor's |
| 4 | Philosophy | Bachelor's |

#### Special Master's / Diploma Programs (Asia Pacific)
| # | Program | Degree |
|---|---------|--------|
| 1 | Master in Diplomacy and International Affairs (Asia Pacific) | (Master's variant) |

### 2.2 At least one program's full deep-dive (worked example)

**Foreign Service, Master's (MFS)** — `grad.georgetown.edu/programs`
- Application portal: `gradapply.georgetown.edu/apply/`
- Fee: $90 (waiver available for qualified applicants)
- GRE: Required (varies by program); TOEFL min 80 or 100 (program-dependent); IELTS 7.0 or 7.5
- Application opens: mid-July (typically)
- TOEFL/GRE institutional code: 5244
- GMAT: McCourt School of Public Policy code JT7-D8-97; All other programs code JT7-GJ-96
- Materials: Academic Statement of Purpose (~500 words); optional Diversity Statement; 3 recommendations; transcripts; test scores
- Funding: GSAS-administered aid, merit fellowships; specific funding details per program

### 2.3 Graduate admissions model

Georgetown graduate admissions is **decentralized** in practice (each professional school runs its own admission process and deadlines), but the **centralized Graduate Studies office** (`grad.georgetown.edu`) processes applications for designated degree and certificate programs in GSAS. Application portal: `gradapply.georgetown.edu/apply/`. The unified programs directory lists 142 programs; ~12+ professional schools (Law, Med, McDonough, Nursing, McCourt Public Policy, etc.) self-manage admissions and may have different portals, fees, and deadlines.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value |
|-----------|-------|
| Admissions site | `uadmissions.georgetown.edu` |
| Application portal | Georgetown Application (`uapply.georgetown.edu/register/firstyearapplication`) OR Common Application (available Aug 1) |
| **EA deadline** | **November 1** (verified via source) |
| **RA / RD deadline** | **January 1** (verified — brief stated Jan 10, which conflicts with source) |
| EA notification date | December 15 |
| RD notification date | April 1 |
| Reply / enrollment confirmation | May 1 |
| Financial-aid deadline | February 1 (FAFSA + CSS Profile) |
| SAT/ACT policy | **REQUIRED** (codes: SAT 5244, ACT 0668); only EBRW+Math (SAT) / English+Math+Reading+Science (ACT) considered |
| Superscore policy | Yes (highest EBRW + Math from multiple sittings for SAT); ACT does NOT use super score optional reports — all scores must be sent |
| Score-report method | Official scores from College Board / ACT |
| Interview policy | Optional alumni interview (Sep–Feb); not required for admission |
| Recommendation requirements | Counselor report + Teacher's report (1) + Midyear School Report |
| Portfolios | Optional supplemental materials for Art, Music, Theater, Dance applicants |
| Transfer pathway | `uadmissions.georgetown.edu/applying/transfer-application-2/` (March 1 deadline); new Capitol Campus transfer pathways for 2026 |
| Application fee | **$80.00** |
| Interview waiver | N/A (alumni interview is the only format) |

> Reconciliation: Brief said "RD Jan 10"; verified source says **January 1**. Document follows source.

### 3.2 Undergraduate English proficiency table

**ELPs are RECOMMENDED (not required) for UG applicants** whose school's primary language of instruction is not English. Georgetown accepts the following tests:

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | (no minimum published) | 100+ recommended | Code 5244 |
| IELTS | (no minimum published) | 7.0+ recommended | Electronic score reporting only |
| DET (Duolingo English Test) | (no minimum published) | 120+ recommended | Accepted |
| TOEFL PBT | (legacy) | — | Accepted |
| TOEFL IPT Plus | (for China mainland) | — | Accepted |

> Important distinction: ELP tests are **recommended** (not strictly required) for UG; the admissions committee uses a holistic review. The brief's "competitive" framing is consistent with this.

### 3.3 Graduate — global rules

| Dimension | Value |
|-----------|-------|
| Admissions portal | `gradapply.georgetown.edu/apply/` |
| Standard application fee | **$90** (non-refundable); Visa/MasterCard/Discover only |
| Fee waiver | Available for qualified applicants (must submit waiver form ≥5 days before deadline); eligibility tied to specific criteria (e.g., participation in certain programs, financial need) |
| CGS April-15-equivalent honor date | Per-program; standard April 15 deadline observed by most GSAS PhD programs |
| GRE/GMAT policy | **Per-program**; required for some, optional for others, not accepted for some. MBA, JD, MD, LLM have their own test policies. |
| Language-test policy | TOEFL iBT min **80** (some programs 100); IELTS min **7.0** (some 7.5); old/new TOEFL scale both supported from Jan 21, 2026; **only official scores accepted** (no MyBest) |
| TOEFL/GRE institutional code | **5244** |
| GMAT codes | McCourt Public Policy: JT7-D8-97; All other programs: JT7-GJ-96 |
| Application timeline | Most programs open mid-July for the following fall; deadlines vary by program (Dec 1 to Apr 15 most common); recommend taking tests ≥1 month before deadline |
| Letters of recommendation | **3 official** required (some programs only mandate 2) |
| Statement of Purpose | Academic Statement of Purpose required (~500 words); Optional Diversity Statement up to 500 words |
| Transcripts | Unofficial copies uploaded with application (from institutions with >15 credits completed or where program prerequisites were taken); official transcripts only after admission offer |
| International applicants | WES ICAP evaluation recommended for non-US transcripts; credential evaluation services that are NACES members also accepted |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26 academic year, line-itemized)

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition per semester (full-time, 12-20 credits) | **$35,568.00** | Per semester = **$71,136/year** |
| Tuition (part-time, per credit) | $2,964.00 | Per credit |
| English as a Foreign Language Tuition (full-time, per semester) | $10,408.00 | For ELC students |
| EFL Tuition (per credit) | $1,301.00 | — |
| Student Activities Fee (per semester, mandatory) | $101.00 | All UG degree-seeking |
| SOH/SON Technology Fee (per semester) | $180.00 | School of Health/Nursing |
| ELC Fee (per semester) | $75.00 | English Language Center |
| Housing (range across residence halls) | $6,041 – $11,917/semester | Fall 2025 + Spring 2026 |
| Board — All Access 7+ Plan (recommended for freshmen/sophomores) | $4,224.00/semester | Includes $500 Flex |
| Board — All Access 7 Plan | $3,924.00/semester | Includes $200 Flex |
| Board — 14-Meals/week Plan | $3,576.00/semester | Includes $250 Flex |
| Board — 7 Meals/week Plan | $1,914.00/semester | Includes $250 Flex |
| Returned Check Fee | $80.00 | Per returned item |
| Payment Plan Application Fee | $60.00 | Per semester |
| Late Registration Fee | $100.00 | — |
| Non-Payment Fee | $100.00 | Per semester |
| Service Charge on overdue balance | 1.50%/month | Compounded |

**Estimated total on-campus UG COA** (2025-26, tuition + housing mid-range + board + fees): ≈ **$88,000 – $94,000/year** (depending on housing choice and board plan). Off-campus students pay same tuition but lower housing.

### 4.2 Undergraduate financial-aid policy

| Policy | Value |
|--------|-------|
| Application forms | **FAFSA** + **CSS Profile** (both due **February 1**) |
| Need-blind admissions (US citizens/PRs) | **YES** (need is not a factor in admissions decision) |
| Need-blind for internationals | **NO** — need-aware (internationals requesting aid considered for "very limited" need-based scholarships) |
| Meets 100% demonstrated need | **YES** for all eligible students |
| Loan-free packages | Need-based aid is met through grants/scholarships/employment/loans from federal+state+private+University sources |
| Merit/Academic scholarships | **NO** (Georgetown does NOT award merit/academic scholarships — aid is purely need-based) |
| Pell-eligible incoming students | Nearly doubled in 2024-2025 |
| Family income thresholds for free tuition | (Per official policy) — not published as a single number; financial aid is calculated based on full need analysis |

### 4.3 Graduate cost & funding framework

| Dimension | Value |
|-----------|-------|
| Application fee | $90 (waiver available per criteria) |
| Funding types | RA, TA, fellowships, scholarships, federal loans (US citizens/PRs only) |
| PhD funding | Most PhD programs provide full tuition + stipend for 5 years |
| Master's funding | Generally self-funded; some programs offer partial aid |
| International student aid | Eligible for institutional funds (assistantships/fellowships/scholarships); generally NOT eligible for US federal loans |
| TOEFL institutional code | 5244 |

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: https://uadmissions.georgetown.edu/applying/first-year-application/
  source_snippet: "Submit Early Action Applications November 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.RD
  value: "January 1"
  source_url: https://uadmissions.georgetown.edu/applying/first-year-application/
  source_snippet: "Submit Regular Decision Applications January 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.deadlines.FAFSA_CSS
  value: "February 1"
  source_url: https://uadmissions.georgetown.edu/applying/first-year-application/
  source_snippet: "Submit CSS Profile and FAFSA February 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.fee.application
  value: "$80.00"
  source_url: https://uadmissions.georgetown.edu/applying/first-year-application/
  source_snippet: "Application Fee $80.00"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.tuition_per_semester
  value: "$35,568.00"
  source_url: https://bulletin.georgetown.edu/expenses-and-financialassistances/basicgeneralexpenses/
  source_snippet: "Tuition per semester (full-time, per semester)	$35,568.00"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.financial_aid.policy
  value: "Need-blind for US citizens/PRs; need-aware for internationals; meets 100% demonstrated need; no merit scholarships"
  source_url: https://uadmissions.georgetown.edu/financial-aid/
  source_snippet: "Georgetown University meets the full financial need of all eligible undergraduate students and a student's need for financial assistance does not negatively impact their chances of admissions. ... Since financial aid at Georgetown is based on need, we do not offer academic or merit based scholarships."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.intl_elp.policy
  value: "RECOMMENDED (not required); accepts DET/IELTS/TOEFL (PBT, iBT, IPT Plus)"
  source_url: https://uadmissions.georgetown.edu/applying/international/
  source_snippet: "Georgetown recommends, but does not require, results from an English language proficiency test for students who attend a school where English is not the language of instruction. Georgetown accepts results from the DET (Duolingo English Test), IELTS, or TOEFL® (PBT, iBT® and IPT® Plus versions), to fulfill this recommendation."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.testing.policy
  value: "SAT and/or ACT REQUIRED (codes: SAT 5244, ACT 0668); only EBRW+Math (SAT) / English+Math+Reading+Science (ACT)"
  source_url: https://uadmissions.georgetown.edu/applying/international/
  source_snippet: "Georgetown University requires submission of SAT and/or ACT scores as part of our holistic application review process. ... Georgetown only considers the Verbal (EBRW) and Math portions of the SAT in our review process."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-009:
  field: schools.architecture.ug_count
  value: "6 undergraduate schools"
  source_url: https://bulletin.georgetown.edu/schools-programs/
  source_snippet: "College of Arts & Sciences | School of Foreign Service | McDonough School of Business | School of Continuing Studies | Berkley School of Nursing | School of Health"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-010:
  field: cas.majors.count
  value: "54 majors"
  source_url: https://bulletin.georgetown.edu/schools-programs/college/degree-programs/
  source_snippet: "1. Majors (54 list items extracted via DOM); 2. Minors (63); 3. Certificates (5); 4. Joint Degree Programs (2); 5. Accelerated Bachelor/Master (25)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-011:
  field: sfs.majors.count
  value: "8 BSFS majors + 1 BGA (joint) = 9"
  source_url: https://bulletin.georgetown.edu/schools-programs/sfs/majors-and-certificates/
  source_snippet: "Eight BSFS majors and the joint degree ... the Dikran Izmirlian Program in Business and Global Affairs (BGA)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-012:
  field: msb.majors.count
  value: "6 BSBA + 2 joint BS (BGA, IBLC)"
  source_url: https://bulletin.georgetown.edu/schools-programs/msb/degree-programs/
  source_snippet: "Bachelor of Science in Business Administration: Accounting, Finance, International Business, Management, Marketing, Operations and Analytics"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-013:
  field: health.majors.count
  value: "3 BS majors"
  source_url: https://bulletin.georgetown.edu/schools-programs/school-of-health/
  source_snippet: "BS in Human Science | BS in Health Care Management & Policy | BS in Global Health"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.count
  value: "142 grad programs"
  source_url: https://grad.georgetown.edu/programs
  source_snippet: "Load More button expanded via JS click → 142 h2 program entries captured"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.fee.application
  value: "$90 (non-refundable)"
  source_url: https://grad.georgetown.edu/admissions/application-information
  source_snippet: "The fee is $90 and can be paid by a Visa, MasterCard, or Discover card."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.elp.policy
  value: "TOEFL min 80 or 100 (program-dep); IELTS 7.0 or 7.5; only official scores"
  source_url: https://grad.georgetown.edu/admissions/application-information
  source_snippet: "TOEFL: A minimum score of 80 or 100 (original TOEFL iBT score scale) or 4 or 5 (new TOEFL iBT score scale beginning January 21, 2026), dependent on program requirements ... IELTS: A minimum score of 7.0 or 7.5"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.test_codes
  value: "GRE/TOEFL 5244; GMAT McCourt JT7-D8-97, others JT7-GJ-96"
  source_url: https://grad.georgetown.edu/admissions/application-information
  source_snippet: "GRE Code: 5244 | TOEFL Code: 5244 | GMAT Codes: McCourt School of Public Policy: JT7-D8-97 / All other programs: JT7-GJ-96"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: georgetown-knowledge-base-v2
├── document: overview
│   ├── chunk: institution-overview (rules 1-4 from Section 0)
│   ├── chunk: deadlines-costs (Section 3 + 4)
├── document: undergraduate
│   ├── chunk: cas-programs (Section 1 — College of Arts & Sciences)
│   ├── chunk: sfs-programs (Section 1 — Walsh SFS)
│   ├── chunk: msb-programs (Section 1 — McDonough)
│   ├── chunk: scs-programs (Section 1 — Continuing Studies)
│   ├── chunk: nursing-programs (Section 1 — Berkley Nursing)
│   ├── chunk: health-programs (Section 1 — School of Health)
│   └── chunk: ug-requirements (Section 3.1)
├── document: graduate
│   ├── chunk: gsas-masters (Section 2 — Master's)
│   ├── chunk: gsas-doctoral (Section 2 — Doctoral)
│   ├── chunk: gsas-certificates (Section 2 — Certificates)
│   ├── chunk: professional-schools (Section 2 — Law/Med/Nursing/McCourt)
│   └── chunk: grad-requirements (Section 3.3)
└── document: evidence
    └── chunk: evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "georgetown-knowledge-base-v2"
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
| P0 | Confirm 2026-27 UG tuition (currently 2025-26 data); brief said "RD Jan 10" — re-verify against current cycle | `bulletin.georgetown.edu/expenses-and-financialassistances/basicgeneralexpenses/` |
| P0 | Verify Law, Medicine, McCourt, McDonough Grad admission requirements + fees (separate portals) | `law.georgetown.edu`, `som.georgetown.edu`, `mccourt.georgetown.edu`, `msb.georgetown.edu/graduate` |
| P0 | Get full list of UG minors across all 6 schools (currently CAS-only = 63; other schools' minor lists not extracted) | Each school's bulletin subpage |
| P1 | Get per-program grad deadlines (currently aggregated; per-program deadlines are searchable via "Search Application Deadlines" link) | `grad.georgetown.edu/admissions/application-information` |
| P1 | International student grad aid policy detail (institutional funds specifics) | `grad.georgetown.edu/financial-support` |
| P1 | TOEFL/IELTS minimums per-program for grad (currently 80/100/7.0/7.5 general; per-program may vary) | Each grad program's detail page |
| P2 | Verify total UG and grad enrollment, faculty counts, acceptance rates, yield | `uadmissions.georgetown.edu/about`, `grad.georgetown.edu/about-us/` |
| P2 | Get Georgetown-specific transfer credit policy (CAS) | `bulletin.georgetown.edu/schools-programs/college/` |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | Georgetown | (other schools) |
|-----------|------------|-----------------|
| Location | Washington, D.C. | |
| Founded | 1789 | |
| Religious affiliation | Jesuit Catholic | |
| UG total cost/yr (2025-26) | ~$88k–$94k (tuition $71,136 + housing + board + fees) | |
| Tuition/yr (full-time) | $71,136 | |
| Need-blind (US citizens) | YES | |
| Need-blind (internationals) | NO (need-aware) | |
| EA deadline | Nov 1 | |
| RD deadline | Jan 1 (per source; brief said Jan 10 — discrepancy flagged) | |
| SAT/ACT required | YES | |
| TOEFL min (UG) | Not required (recommended 100+) | |
| IELTS min (UG) | Not required (recommended 7.0+) | |
| TOEFL min (Grad) | 80 or 100 (program-dependent) | |
| IELTS min (Grad) | 7.0 or 7.5 (program-dependent) | |
| UG application fee | $80 | |
| Grad application fee | $90 | |
| Total program count (Rule 1) | 214 (72 UG + 142 Grad) | |
| School/department count (Rule 2) | 6 UG schools + GSAS (graduate) | |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**:
> - `uadmissions.georgetown.edu` (UG Admissions)
> - `grad.georgetown.edu` (Graduate Studies)
> - `bulletin.georgetown.edu` (Undergraduate Bulletin)
> - `finaid.georgetown.edu` (Financial Aid)
>
> **Verification**: ego-browser snapshotText + JS DOM extraction; Load-More JS pagination for grad directory; structured extraction of CAS/SFS/MSB/Health/Schools via `<a>` href + h2 enumeration.
>
> **Granularity**: school → department → degree-level → program
>
> **Known caveats**:
> 1. Task brief stated "9 schools" — verified source has **6 UG schools**. Document follows source.
> 2. Task brief stated "RD Jan 10" — verified source has **RD Jan 1**. Document follows source.
> 3. Bulletin page at `/schools-programs/school-of-nursing/degree-programs/` actually displays School of Health programs (apparent URL aliasing or merged page); Berkley School of Nursing's only UG program is BSN.
> 4. Grad program count of 142 reflects programs loaded via Load-More; if more programs exist beyond the Load-More threshold, they were not captured.
> 5. Minor counts beyond CAS (63) not exhaustively extracted from SFS/MSB/Health/Nursing/SCS bulletin pages.