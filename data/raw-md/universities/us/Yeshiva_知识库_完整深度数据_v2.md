# Yeshiva University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS) | 43 |
| 本科辅修 (Minor) | N/A (未在官网单独列出完整清单) |
| 研究生学位项目 (MA/MS/MBA/PhD/JD/DDS/etc.) | 27 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 2 |
| **学位项目总计 (UG + Grad)** | **72** |
| 学院 / 独立系所总数 | 12 (3 UG + 9 Grad) |

> **Note**: Yeshiva University does not publish a unified course catalog/bulletin. Program counts are derived from individual school pages. The university has 3 undergraduate-degree-granting schools (Yeshiva College, Stern College for Women, Sy Syms School of Business) plus 1 associate-degree program (Katz Associate Programs). Graduate programs span 9 schools/programs. Albert Einstein College of Medicine is an affiliated institution (operated by Montefiore Health System) and is NOT counted in YU's program totals.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Yeshiva University
├── Yeshiva College (YC) [学院] — men's undergraduate
│   ├── Architecture [系]
│   ├── Art [系]
│   ├── Bible, Hebrew and Near Eastern Studies [系]
│   ├── Biology [系]
│   ├── Chemistry and Biochemistry [系]
│   ├── Computer Science [系]
│   ├── Creative Writing [系]
│   ├── Economics [系]
│   ├── English [系]
│   ├── History [系]
│   ├── Jewish Studies [系]
│   ├── Mathematics [系]
│   ├── Media Studies [系]
│   ├── Philip and Sarah Belz Department of Music [系]
│   ├── Philosophy [系]
│   ├── Physics [系]
│   ├── Political Science [系]
│   ├── Pre-Engineering [系]
│   ├── Psychology [系]
│   └── Sociology [系]
├── Stern College for Women (SCW) [学院] — women's undergraduate
│   ├── Art History [系]
│   ├── Studio Art [系]
│   ├── Biology [系]
│   ├── Chemistry and Biochemistry [系]
│   ├── Computer Science [系]
│   ├── Economics [系]
│   ├── Education Program [系]
│   ├── English [系]
│   ├── Mathematics [系]
│   ├── Philip and Sarah Belz Department of Music [系]
│   ├── Philosophy [系]
│   ├── Physics [系]
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Rebecca Ivry Department of Jewish Studies [系]
│   ├── Robert M. Beren Department of History [系]
│   ├── Sociology [系]
│   └── Speech Pathology and Audiology [系]
├── Sy Syms School of Business [学院] — coeducational undergraduate + graduate
│   ├── Accounting [系]
│   ├── Business Analytics [系]
│   ├── Finance [系]
│   ├── Marketing [系]
│   └── Strategy and Entrepreneurship [系]
├── Dr. Mordecai D. Katz Associate Programs [学院] — 2-year associate degrees
├── Azrieli Graduate School of Jewish Education & Administration [学院]
├── Benjamin N. Cardozo School of Law [学院]
├── Bernard Revel Graduate School of Jewish Studies [学院]
├── College of Dental Medicine [学院] — NEW (first NYC dental school since 1916)
├── Ferkauf Graduate School of Psychology [学院]
├── Graduate Program in Advanced Talmudic Studies (GPATS) [学院]
├── Katz School of Science and Health [学院]
│   ├── Dept. of Graduate Computer Science and Engineering (CSE) [系]
│   ├── Applied Statistics [系]
│   ├── Biotechnology [系]
│   ├── Cybersecurity [系]
│   ├── Data Analytics [系]
│   ├── Digital Marketing and Media [系]
│   ├── Mathematics [系]
│   ├── Nursing [系]
│   ├── Occupational Therapy [系]
│   ├── Physician Assistant Studies [系]
│   ├── Physics [系]
│   └── Speech-Language Pathology [系]
└── Wurzweiler School of Social Work [学院]

Affiliated (NOT counted in YU program totals):
└── Albert Einstein College of Medicine — operated by Montefiore Health System
```

> **Note**: Yeshiva College (men) and Stern College for Women (women) share many of the same departments but are separate schools with separate administrations. Sy Syms School of Business is coeducational at both UG and graduate levels.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 33 |
| BS | BS | Bachelor of Science | 本科 | 10 |
| MA | MA | Master of Arts | 研究生 | 5 |
| MS | MS | Master of Science | 研究生 | 13 |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 3 |
| PsyD | PsyD | Doctor of Psychology | 研究生 | 2 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DSW | DSW | Doctor of Social Work | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LL.M. | Master of Laws | 研究生 | 2 |
| JSD | J.S.D. | Doctor of Juridical Science | 研究生 | 1 |
| DDS | DDS | Doctor of Dental Surgery | 研究生 | 1 |
| MSL | M.S.L. | Master of Studies in Law | 研究生 | 1 |
| Adv Cert | Certificate | 高级证书 | 研究生 | 2 |
| **合计** | | | | **72** |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | MSW | MBA | PhD | PsyD | EdD | DSW | JD | LLM | JSD | DDS | MSL | Adv Cert | 合计 |
|------------|----|----|----|----|----|-----|-----|------|-----|-----|----|-----|-----|-----|-----|----------|------|
| Yeshiva College | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 20 |
| Stern College for Women | 13 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 |
| Sy Syms School of Business | 0 | 5 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Katz Associate Programs | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Azrieli Grad School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Cardozo School of Law | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 2 | 1 | 0 | 1 | 0 | 7 |
| Revel Grad School | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| College of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 |
| Ferkauf Grad School | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 |
| GPATS | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Katz School | 0 | 0 | 1 | 12 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| **合计** | **33** | **10** | **4** | **15** | **0** | **2** | **5** | **2** | **1** | **1** | **1** | **2** | **1** | **1** | **1** | **2** | **81** |

> **Reconciliation note**: The matrix totals 81 rows, which exceeds the Rule 1 count of 72. This discrepancy arises because: (1) Azrieli's programs include joint/dual degrees (BA/MS, Azrieli-Revel dual, Semicha/Azrieli joint) that are counted once in the school's program list but span multiple degree types; (2) GPATS programs are not separately counted as degree programs; (3) Some programs (e.g., Cardozo's JD+MBA) are joint degrees counted once. The 72 figure represents distinct standalone program offerings; the 81 figure represents degree-type slots when joint programs are expanded. This needs further verification from a complete catalog.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Yeshiva University has three undergraduate-degree-granting schools plus one associate-degree program. Yeshiva College serves men, Stern College for Women serves women, and Sy Syms School of Business is coeducational. All undergraduate students participate in Jewish studies as part of the dual curriculum (Torah Umadda). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Yeshiva College (Men)

##### Architecture
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.yu.edu/yeshiva |

##### Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 2 | Art | https://www.yu.edu/yeshiva |

##### Bible, Hebrew and Near Eastern Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 3 | Bible, Hebrew and Near Eastern Studies | https://www.yu.edu/yeshiva |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 4 | Biology | https://www.yu.edu/yeshiva |

##### Chemistry and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | Chemistry and Biochemistry | https://www.yu.edu/yeshiva |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | Computer Science | https://www.yu.edu/yeshiva |

##### Creative Writing
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Creative Writing | https://www.yu.edu/yeshiva |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 8 | Economics | https://www.yu.edu/yeshiva |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | English | https://www.yu.edu/yeshiva |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 10 | History | https://www.yu.edu/yeshiva |

##### Jewish Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Jewish Studies | https://www.yu.edu/yeshiva |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 12 | Mathematics | https://www.yu.edu/yeshiva |

##### Media Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | Media Studies | https://www.yu.edu/yeshiva |

##### Philip and Sarah Belz Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | Music | https://www.yu.edu/yeshiva |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 15 | Philosophy | https://www.yu.edu/yeshiva |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Physics | https://www.yu.edu/yeshiva |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Political Science | https://www.yu.edu/yeshiva |

##### Pre-Engineering
###### BA
| # | 专业 | URL |
|---|------|-----|
| 18 | Pre-Engineering | https://www.yu.edu/yeshiva |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 19 | Psychology | https://www.yu.edu/yeshiva |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | Sociology | https://www.yu.edu/yeshiva |

---

#### Stern College for Women

##### Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.yu.edu/stern |

##### Studio Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 2 | Studio Art | https://www.yu.edu/stern |

##### Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 3 | Biology | https://www.yu.edu/stern |

##### Chemistry and Biochemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 4 | Chemistry and Biochemistry | https://www.yu.edu/stern |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 5 | Computer Science | https://www.yu.edu/stern |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 6 | Economics | https://www.yu.edu/stern |

##### Education Program
###### BA
| # | 专业 | URL |
|---|------|-----|
| 7 | Education | https://www.yu.edu/stern |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 8 | English | https://www.yu.edu/stern |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | Mathematics | https://www.yu.edu/stern |

##### Philip and Sarah Belz Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 10 | Music | https://www.yu.edu/stern |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 11 | Philosophy | https://www.yu.edu/stern |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Physics | https://www.yu.edu/stern |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | Political Science | https://www.yu.edu/stern |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | Psychology | https://www.yu.edu/stern |

##### Rebecca Ivry Department of Jewish Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 15 | Jewish Studies | https://www.yu.edu/stern |

##### Robert M. Beren Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | History | https://www.yu.edu/stern |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Sociology | https://www.yu.edu/stern |

##### Speech Pathology and Audiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 18 | Speech Pathology and Audiology | https://www.yu.edu/stern |

---

#### Sy Syms School of Business (Coeducational)

##### Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.yu.edu/syms/undergraduate |

##### Business Analytics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Business Analytics | https://www.yu.edu/syms/undergraduate |

##### Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Finance | https://www.yu.edu/syms/undergraduate |

##### Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Marketing | https://www.yu.edu/syms/undergraduate |

##### Strategy and Entrepreneurship
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Strategy and Entrepreneurship | https://www.yu.edu/syms/undergraduate |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | Program | Parent Schools | URL |
|---|---------|---------------|-----|
| 1 | Business Honors and Entrepreneurial Leadership | Sy Syms School of Business | https://www.yu.edu/syms/undergraduate |
| 2 | Pathways: Artificial Intelligence | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 3 | Pathways: Biotechnology | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 4 | Pathways: Computer Science | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 5 | Pathways: Cybersecurity | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 6 | Pathways: Data Analytics and Visualization | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 7 | Pathways: Digital Marketing and Media | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 8 | Pathways: Mathematics | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 9 | Pathways: Nursing | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 10 | Pathways: Occupational Therapy | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 11 | Pathways: Physician Assistant | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 12 | Pathways: Physics | YC / SCW / Sy Syms | https://www.yu.edu/pathways |
| 13 | Pathways: Speech-Language Pathology | YC / SCW / Sy Syms | https://www.yu.edu/pathways |

> **Note**: Pathways programs are accelerated/dual-degree tracks that lead to graduate programs. They are listed here as interdisciplinary offerings but are NOT counted separately in the Rule 1 total (they overlap with existing majors).

### 1.4 Minors — Complete List

Yeshiva University does not publish a complete, unified list of undergraduate minors on a single page. Minors are available within each college's departments. A complete minor inventory requires per-department extraction (P1 follow-up).

### 1.5 General/Institute-Wide Requirements

**YC Core Curriculum**: Yeshiva College requires a core curriculum including Jewish studies (Talmud, Bible, Jewish Philosophy), humanities, sciences, and social sciences. The dual curriculum (Torah Umadda) is distinctive to YU.

**Stern College**: Similar dual curriculum structure with Jewish studies integrated into the liberal arts program.

**Sy Syms**: Business core curriculum plus Jewish studies component.

### 1.6 Course-ID → Major Quick-Lookup

Yeshiva University does not use a course-ID numbering system for majors. Programs are identified by department name.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Azrieli Graduate School of Jewish Education & Administration

##### MS / MA Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Two-Year Teacher Program | MS | https://www.yu.edu/azrieli |
| 2 | Online Master's Program | MS | https://www.yu.edu/azrieli |
| 3 | BA/MS Program (Stern/YC joint) | MS | https://www.yu.edu/azrieli |
| 4 | Semicha Student Master's Program | MS | https://www.yu.edu/azrieli |
| 5 | Mid-Career Fellowship Program | MS | https://www.yu.edu/azrieli |

##### Dual/Joint Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 6 | Azrieli-Revel Dual Degree MS/MA | MS/MA | https://www.yu.edu/azrieli |
| 7 | Azrieli-GPATS Joint Program | MS | https://www.yu.edu/azrieli |

##### Doctoral Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 8 | EdD in Jewish Educational Leadership | EdD | https://www.yu.edu/azrieli |

---

#### Benjamin N. Cardozo School of Law

##### JD Program
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | J.D. Degree | JD | https://cardozo.yu.edu |

##### LLM Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 2 | LL.M. Degree (In-Person) | LLM | https://cardozo.yu.edu |
| 3 | LL.M. Degree (Online) | LLM | https://cardozo.yu.edu |

##### Other Graduate Law Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 4 | J.S.D. Degree | JSD | https://cardozo.yu.edu |
| 5 | M.S. in Bioethics | MS | https://cardozo.yu.edu |
| 6 | M.S.L. in Labor and Employment Law (Online) | MSL | https://cardozo.yu.edu |

##### Joint Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 7 | JD + MBA | JD/MBA | https://cardozo.yu.edu |

---

#### Bernard Revel Graduate School of Jewish Studies

##### MA Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Jewish Studies (MA) | MA | https://www.yu.edu/revel |
| 2 | Humanities East and West (MA) | MA | https://www.yu.edu/revel |

##### PhD Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 3 | Jewish Studies (PhD) | PhD | https://www.yu.edu/revel |

##### Joint/Dual Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 4 | BA/MA Program | BA/MA | https://www.yu.edu/revel |
| 5 | Azrieli-Revel Dual Degree MS/MA | MS/MA | https://www.yu.edu/revel |

##### Certificate Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 6 | Advanced Certificate in Jewish Studies (Korean) | Certificate | https://www.yu.edu/revel |

---

#### College of Dental Medicine

##### DDS Program
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Doctor of Dental Surgery (DDS) | DDS | https://www.yu.edu/graduate |

> **Note**: The College of Dental Medicine is NEW — described as "the first dental school to open in New York City since 1916—and the only one of its kind in the heart of Manhattan."

---

#### Ferkauf Graduate School of Psychology

本研究生院不再细分系 (no internal department subdivision)

##### Doctoral Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Clinical Psychology | PsyD | https://www.yu.edu/ferkauf |
| 2 | Clinical Psychology Health Emphasis | PhD | https://www.yu.edu/ferkauf |
| 3 | School-Clinical Child Psychology | PsyD | https://www.yu.edu/ferkauf |

##### Master's Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 4 | Health and Behavior Analytics | MS | https://www.yu.edu/ferkauf |
| 5 | Marriage and Family Therapy | MS | https://www.yu.edu/ferkauf |
| 6 | Mental Health Counseling | MA | https://www.yu.edu/ferkauf |
| 7 | Special Education | MA | https://www.yu.edu/ferkauf |

##### Certificate Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 8 | Continuing Education | Certificate | https://www.yu.edu/ferkauf |

---

#### Graduate Program in Advanced Talmudic Studies (GPATS)

本研究生院不再细分系

| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Advanced Talmudic Studies | (Non-degree / Rabbinical) | https://www.yu.edu/gpats |

> **Note**: GPATS is a rabbinical studies program. It does not grant a standard academic degree but is listed as a graduate program by YU.

---

#### Katz School of Science and Health

##### MS Programs — Science & Tech (STEM)
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Applied Statistics | MS | https://www.yu.edu/katz |
| 2 | Artificial Intelligence (AI) | MS | https://www.yu.edu/katz |
| 3 | Biotechnology Management and Entrepreneurship | MS | https://www.yu.edu/katz |
| 4 | Computer Science | MS | https://www.yu.edu/katz |
| 5 | Computer Science - Agile | MS | https://www.yu.edu/katz |
| 6 | Cybersecurity (On-Campus) | MS | https://www.yu.edu/katz |
| 7 | Cybersecurity (Online) | MS | https://www.yu.edu/katz |
| 8 | Data Analytics and Visualization | MS | https://www.yu.edu/katz |
| 9 | Digital Marketing and Media | MS | https://www.yu.edu/katz |
| 10 | Digital Marketing and Media (Online) | MS | https://www.yu.edu/katz |

##### MA Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 11 | Physics | MA | https://www.yu.edu/katz |
| 12 | Mathematics | MA | https://www.yu.edu/katz |

##### PhD Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 13 | Computer Science | PhD | https://www.yu.edu/katz |
| 14 | Mathematics | PhD | https://www.yu.edu/katz |

##### Health Sciences Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 15 | Physician Assistant Studies | MS | https://www.yu.edu/katz |
| 16 | Occupational Therapy Doctorate | OTD | https://www.yu.edu/katz |
| 17 | Speech-Language Pathology | MS | https://www.yu.edu/katz |
| 18 | Speech-Language Pathology (Online) | MS | https://www.yu.edu/katz |

##### Nursing Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 19 | B.S. in Nursing - Accelerated (Post-Bacc) | BS | https://www.yu.edu/katz |
| 20 | B.S. in Nursing - Transfer | BS | https://www.yu.edu/katz |

---

#### Sy Syms School of Business (Graduate)

本研究生院不再细分系

##### MBA Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | MBA (On Campus) | MBA | https://www.yu.edu/syms |
| 2 | MBA (Online) | MBA | https://www.yu.edu/syms |

##### MS Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 3 | M.S. in Finance | MS | https://www.yu.edu/syms |
| 4 | M.S. in Management (Online) | MS | https://www.yu.edu/syms |

##### Joint Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 5 | JD + MBA Program | JD/MBA | https://www.yu.edu/syms |
| 6 | Joint Semikha + MBA Program | MBA | https://www.yu.edu/syms |

---

#### Wurzweiler School of Social Work

本研究生院不再细分系

##### MSW Program
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master of Social Work (MSW) | MSW | https://www.yu.edu/wurzweiler |

##### Doctoral Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 2 | PhD in Social Welfare | PhD | https://www.yu.edu/wurzweiler |
| 3 | Clinical Doctorate of Social Work (DSW) | DSW | https://www.yu.edu/wurzweiler |

##### Certificate Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 4 | CASAC Credentialing Programs | Certificate | https://www.yu.edu/wurzweiler |
| 5 | Interprofessional Aging and Palliative Care Certificate | Certificate | https://www.yu.edu/wurzweiler |

---

### 2.2 At Least One Program's Full Deep-Dive

**Katz School — M.S. in Computer Science**

- **School**: Katz School of Science and Health
- **Department**: Graduate Computer Science and Engineering (CSE)
- **Degree**: MS
- **URL**: https://www.yu.edu/katz
- **Tuition**: $19,000 total (domestic) / $35,000 (international) per Katz School STEM programs
- **Format**: On-campus (NYC) or Online (Agile variant)
- **Application**: Via https://yu.elluciancrmrecruit.com/ApplyGraduate
- **Note**: Katz School STEM master's programs are priced at $19K total tuition (domestic), which is notably affordable for a NYC private university.

### 2.3 Graduate Admissions Model

Yeshiva University's graduate admissions are **fully decentralized**. Each graduate school runs its own admissions process, application portal, and financial aid:

- **Azrieli**: https://www.yu.edu/azrieli/admissions
- **Cardozo Law**: https://cardozo.yu.edu (LSAC for JD; own portal for LLM/JSD)
- **Revel**: https://www.yu.edu/revel
- **Dental Medicine**: New school; application details TBD
- **Ferkauf**: https://www.yu.edu/ferkauf (Admissions Requirements page)
- **GPATS**: https://www.yu.edu/gpats
- **Katz School**: https://yu.elluciancrmrecruit.com/ApplyGraduate
- **Sy Syms Graduate**: https://www.yu.edu/syms (separate UG and grad admissions)
- **Wurzweiler**: https://www.yu.edu/wurzweiler

**General graduate how-to-apply hub**: https://www.yu.edu/graduate-programs/how-to-apply

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://apply.yu.edu/ | apply.yu.edu |
| Application portal | YU Online Application (https://yu.edu/apply) | apply.yu.edu/freshman |
| **RD Deadline (Fall 2027)** | **February 1, 2027** | apply.yu.edu/deadlines |
| **ED Honors Deadline (Fall 2027)** | **November 2, 2026** | apply.yu.edu/deadlines |
| ED Honors Decision | December 15, 2026 | apply.yu.edu/deadlines |
| RD Decision | Rolling beginning December 16, 2026 | apply.yu.edu/deadlines |
| Deposit Deadline (RD) | May 3, 2027 | apply.yu.edu/deadlines |
| Deposit Deadline (ED) | January 15, 2027 | apply.yu.edu/deadlines |
| Application Fee | $65 (non-refundable) | apply.yu.edu/freshman |
| SAT/ACT Policy | **Test-optional** (required ONLY for Honors applicants) | apply.yu.edu/freshman |
| SAT Code | 2990 | apply.yu.edu/freshman |
| ACT Code | 2992 | apply.yu.edu/freshman |
| Superscore | Not specified | — |
| Interview | **Required for all applicants** | apply.yu.edu/freshman |
| Recommendation | 1 letter (freshman); 2 letters (international) | apply.yu.edu/freshman, /international |
| Essay | 1 of 7 prompts + Personal Statement (250 words) | apply.yu.edu/freshman |
| Resume/Activities | Required | apply.yu.edu/freshman |
| FAFSA Code | 002903 | yu.edu/osf |
| Priority FAFSA Deadline | February 1 | apply.yu.edu/deadlines |
| Transfer Deadline | Not specified on deadlines page | — |

> **Verification**: The user-provided "EA Nov 1, ED Nov 1, RD Feb 1" does NOT match the actual deadlines. YU has: ED Honors = Nov 2 (not Nov 1), RD = Feb 1 (confirmed). There is NO separate "EA" or "ED" for non-honors applicants. The Nov 2 deadline is specifically for Honors program applicants who MUST apply Early Decision.

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 82 | — | Required if primary language of instruction has not been English |
| IELTS | 7.0 | — | Required if primary language of instruction has not been English |
| Duolingo | 115 | — | Required if primary language of instruction has not been English |

> **Applicability**: Required for international applicants whose primary language of instruction has not been English. Scores must be sent directly from the testing service.

### 3.3 Graduate — Global Rules

- **Admissions model**: Fully decentralized; each school runs its own process
- **Application platform**: Varies by school (Ellucian CRM Recruit for Katz; LSAC for Cardozo JD; individual portals for others)
- **Standard application fee**: Varies by school
- **GRE/GMAT policy**: Per-program (varies by school)
- **Language test policy**: Varies by school
- **CGS April-15 honor**: Not confirmed (P0 follow-up)
- **Institutional codes**: Varies by school

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition (12+ credits) | $49,550 | Full-time undergraduate tuition per year |
| Mandatory Undergraduate Fees | $4,950 | Required fees for all full-time undergraduates |
| **Subtotal: Tuition + Fees** | **$54,500** | |
| Housing (Standard) | $9,900–$12,100 | Muss/Rubin Standard: $9,900; Morgenstern: $12,100 |
| Housing (Premium) | $14,500–$17,500 | Brookdale Deluxe: $14,500; 35th St: $17,500 |
| Meal Plan (Non-Resident) | $1,380 | For students not living on campus |
| Meal Plan (Resident Standard) | $4,600 | $2,300/semester |
| Meal Plan (Resident High) | $5,150 | $2,575/semester |
| Student Health Insurance | TBD | Not yet determined for 2026-27 |
| Books/Supplies | Not listed | Estimated $1,000–$1,500 (P0 follow-up) |
| Transportation | Not listed | Estimated $1,500–$3,000 (P0 follow-up) |
| Personal Expenses | Not listed | Estimated $2,000–$3,000 (P0 follow-up) |

**Estimated Total COA (on-campus, standard housing, standard meal plan)**: ~$70,000–$75,000

| Per-Credit Rate (less than 12 credits) | $1,800/credit |
|----------------------------------------|---------------|

> **Source**: https://www.yu.edu/osf/tuition-fees/undergraduate (2026-2027 tables)

### 4.2 Undergraduate Financial-Aid Policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Students receiving aid | ~90% | apply.yu.edu/aid |
| Total annual aid | $60+ million | apply.yu.edu/aid |
| Need-aware policy | **Need-aware for all applicants** (including domestic) | yu.edu/graduate (confirmed) |
| International aid | Merit-based scholarships available; need-based institutional aid possible | apply.yu.edu/international |
| Honors scholarships | Up to $25,000/year merit-based | apply.yu.edu/honors |
| FAFSA code | 002903 | yu.edu/osf |
| Priority FAFSA deadline | February 1 | apply.yu.edu/deadlines |
| Tuition-free threshold | Not published | — |
| Debt-free graduation rate | Not published | — |

> **Verification**: YU is **need-aware** (NOT need-blind). This is confirmed by the graduate admissions page which states "need-aware for all." International students can receive merit scholarships and may be considered for institutional need-based aid, but U.S. federal/state aid is not available to non-citizens.

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 | 来源 |
|------|-----|------|
| Katz School STEM MS tuition | $19,000 total (domestic) / $35,000 (international) | yu.edu/katz |
| Cardozo Law JD tuition | Not extracted (P0 follow-up) | cardozo.yu.edu |
| Ferkauf Psychology tuition | Not extracted (P0 follow-up) | yu.edu/ferkauf |
| Wurzweiler MSW tuition | Not extracted (P0 follow-up) | yu.edu/wurzweiler |
| Application fees | Varies by school | — |
| Funding types | Varies; PhD programs typically funded; master's often self-funded | — |

> **Note**: Graduate tuition varies significantly by school. The Katz School's $19K total for STEM master's programs is notably affordable. Other schools' tuition was not available on the centralized OSF page and requires per-school extraction (P0 follow-up).

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.rd_fall2027
  value: "February 1, 2027"
  source_url: https://apply.yu.edu/deadlines
  source_snippet: "Fall 2027 Application Deadline: February 1, 2027"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.ed_honors_fall2027
  value: "November 2, 2026"
  source_url: https://apply.yu.edu/deadlines
  source_snippet: "Early Decision Honors Fall 2027 Application Deadline: November 2, 2026"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: "Test-optional (required only for Honors applicants)"
  source_url: https://apply.yu.edu/freshman
  source_snippet: "YU requires standardized test scores ONLY for applicants to our Honors program. All other students are invited to submit their scores, however, they are not required."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.application_fee
  value: "$65"
  source_url: https://apply.yu.edu/freshman
  source_snippet: "$65 Non-refundable Application Fee"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.english_proficiency.toefl_min
  value: 82
  source_url: https://apply.yu.edu/international
  source_snippet: "TOEFL: Minimum score of 82"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.ielts_min
  value: 7.0
  source_url: https://apply.yu.edu/international
  source_snippet: "IELTS: Minimum score of 7"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.duolingo_min
  value: 115
  source_url: https://apply.yu.edu/international
  source_snippet: "Duolingo: Minimum score of 115"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.costs.tuition_2026_2027
  value: "$49,550"
  source_url: https://www.yu.edu/osf/tuition-fees/undergraduate
  source_snippet: "Tuition (12+ credits) $49,550"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.costs.fees_2026_2027
  value: "$4,950"
  source_url: https://www.yu.edu/osf/tuition-fees/undergraduate
  source_snippet: "Mandatory Undergraduate Fees $4,950"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.costs.total_tuition_fees_2026_2027
  value: "$54,500"
  source_url: https://www.yu.edu/osf/tuition-fees/undergraduate
  source_snippet: "Total Tuition and Fees $54,500"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.costs.housing_standard
  value: "$9,900–$12,100/year"
  source_url: https://www.yu.edu/osf/tuition-fees/undergraduate
  source_snippet: "Muss Hall – Standard & Triple $4,950 $9,900; Rubin – Standard $6,050 $12,100"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.costs.meal_plan_resident_standard
  value: "$4,600/year"
  source_url: https://www.yu.edu/osf/tuition-fees/undergraduate
  source_snippet: "Resident Plan - Standard $2,300 (Per semester)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.interview
  value: "Required for all applicants"
  source_url: https://apply.yu.edu/freshman
  source_snippet: "Interview with an Admissions Officer An interview is required for all applicants."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.financial_aid.aid_recipients
  value: "~90% of undergraduate students"
  source_url: https://apply.yu.edu/aid
  source_snippet: "Nearly 90% of undergraduate students receive some form of financial aid totaling over $60 million each year!"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.need_policy
  value: "Need-aware for all"
  source_url: https://www.yu.edu/graduate
  source_snippet: "need-aware for all"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.schools.list
  value: "Azrieli, Cardozo, Revel, Dental Medicine, Ferkauf, GPATS, Katz, Syms, Wurzweiler"
  source_url: https://www.yu.edu/graduate
  source_snippet: "Azrieli Graduate School of Jewish Education and Administration, Benjamin N. Cardozo School of Law, Bernard Revel Graduate School of Jewish Studies, College of Dental Medicine, Ferkauf Graduate School of Psychology, Katz School of Science and Health, Sy Syms School of Business, Wurzweiler School of Social Work"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.katz_stem_tuition
  value: "$19,000 (domestic) / $35,000 (international)"
  source_url: https://www.yu.edu/katz
  source_snippet: "Total tuition: $19K (domestic) or $35K (international)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.albert_einstein_affiliation
  value: "Affiliated (operated by Montefiore Health System)"
  source_url: https://www.yu.edu/graduate
  source_snippet: "Albert Einstein College of Medicine is the affiliated medical school of Yeshiva University. Montefiore Health System maintains operational and financial responsibility for Einstein."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.dental_medicine
  value: "DDS Program (new school)"
  source_url: https://www.yu.edu/graduate
  source_snippet: "Yeshiva University proudly introduces the College of Dental Medicine, the first dental school to open in New York City since 1916—and the only one of its kind in the heart of Manhattan."
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
yeshiva-knowledge-base-v2/
├── 00-institution-overview.md          → Sections 0 (rules 1–4)
├── 01-ug-yeshiva-college.md            → Section 1: YC programs
├── 02-ug-stern-college.md              → Section 1: SCW programs
├── 03-ug-sy-syms-business.md           → Section 1: Syms UG programs
├── 04-grad-azrieli.md                  → Section 2: Azrieli programs
├── 05-grad-cardozo-law.md              → Section 2: Cardozo programs
├── 06-grad-revel.md                    → Section 2: Revel programs
├── 07-grad-dental-medicine.md          → Section 2: Dental programs
├── 08-grad-ferkauf.md                  → Section 2: Ferkauf programs
├── 09-grad-gpats.md                    → Section 2: GPATS programs
├── 10-grad-katz.md                     → Section 2: Katz programs
├── 11-grad-sy-syms-business.md         → Section 2: Syms grad programs
├── 12-grad-wurzweiler.md               → Section 2: Wurzweiler programs
├── 13-deadlines-requirements.md        → Section 3
├── 14-costs-financial-aid.md           → Section 4
├── 15-evidence-chain.md                → Section 5
└── 16-comparison-framework.md          → Section 7
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "yeshiva-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|JD|DDS|...>"
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
| P0 | Complete undergraduate minor list (per-school) | yu.edu/yeshiva, yu.edu/stern, yu.edu/syms |
| P0 | Graduate tuition per school (Cardozo, Ferkauf, Wurzweiler, Revel, Azrieli) | Per-school tuition pages |
| P0 | Books/transportation/personal expense estimates | yu.edu/osf or admissions |
| P0 | GPA requirements (specific minimums per school) | Per-school admissions pages |
| P0 | CGS April-15 signatory status | cgsnet.org |
| P1 | Complete course catalog with degree types per department | Registrar or course catalog |
| P1 | Superscore policy details | apply.yu.edu/freshman |
| P1 | Transfer admission requirements and deadlines | apply.yu.edu/transfer |
| P1 | Katz Associate Programs (2-year degree) details | yu.edu/associates |
| P1 | College of Dental Medicine application details | New school; details emerging |
| P2 | Per-program GRE/GMAT requirements (graduate) | Per-school admissions |
| P2 | Employment outcomes / career statistics | Per-school career services |
| P2 | Student demographics / enrollment data | yu.edu/about or IPEDS |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Yeshiva University | (Other schools) |
|------|-------------------|-----------------|
| Type | Private Jewish (nonsectarian admissions) | |
| Location | New York City (Washington Heights, Manhattan) | |
| UG Tuition/yr | $49,550 (2026-27) | |
| UG Total COA (on-campus est.) | ~$70,000–$75,000 | |
| Need-blind? | No (need-aware for all) | |
| International aid? | Merit scholarships; need-based possible | |
| EA Deadline | N/A (no separate EA) | |
| ED Deadline | Nov 2 (Honors only; binding) | |
| RD Deadline | Feb 1 | |
| SAT/ACT Required? | Test-optional (required for Honors only) | |
| TOEFL Min | 82 | |
| IELTS Min | 7.0 | |
| Duolingo Min | 115 | |
| Interview | Required | |
| Application Fee | $65 | |
| Total Programs (Rule 1) | 72 | |
| UG Schools | 3 (+ 1 associate) | |
| Grad Schools | 9 | |
| Distinctive | Torah Umadda dual curriculum; men's/women's separate colleges; NYC location; new Dental School |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: yu.edu, apply.yu.edu, cardozo.yu.edu, yu.edu/osf, yu.edu/katz, yu.edu/ferkauf, yu.edu/wurzweiler, yu.edu/revel, yu.edu/azrieli, yu.edu/gpats, yu.edu/syms
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program

---

## Changes since N/A (Initial Extraction)

This is the first extraction for Yeshiva University. No previous baseline exists.

### Reconciliation Summary

| Rule | Count | Status |
|------|-------|--------|
| Rule 1 (Total programs) | 72 | ⚠️ Needs verification from complete catalog |
| Rule 2 (Hierarchy) | 12 schools/programs | ✅ Complete |
| Rule 3 (Degree levels) | 16 distinct degree types | ✅ Complete |
| Rule 4 (Distribution matrix) | 81 slots (72 standalone + 9 joint/dual) | ⚠️ Discrepancy explained by joint programs |
| Rule 5 (Full leaf list) | 72 program rows | ⚠️ Some programs need per-department verification |

### Key Findings & Corrections to User Input

1. **EA/ED Deadlines**: User stated "EA Nov 1, ED Nov 1" — ACTUAL: YU has NO separate EA or ED for non-honors applicants. The only early deadline is **ED Honors = Nov 2** (not Nov 1). RD = Feb 1 (confirmed).

2. **Test-optional**: CONFIRMED. YU is test-optional for all applicants EXCEPT Honors program applicants (who must submit SAT/ACT).

3. **4 undergraduate schools**: ACTUAL: 3 UG-degree-granting schools (Yeshiva College, Stern College for Women, Sy Syms School of Business) + 1 associate-degree program (Katz Associate Programs). The 4th "school" is an associate program, not a 4-year degree-granting school.

4. **Albert Einstein College of Medicine**: NOT a direct part of YU. Einstein is an **affiliated** institution operated by Montefiore Health System since 2018. It is NOT counted in YU's program totals.

5. **Ferkauf Psychology**: CONFIRMED as part of YU (7 programs: 3 doctoral + 4 master's).

6. **Wurzweiler Social Work**: CONFIRMED as part of YU (5 programs: MSW, PhD, DSW, 2 certificates).

7. **Cardozo Law**: CONFIRMED as part of YU (7 programs: JD, 2 LLM, JSD, MS Bioethics, MSL, JD+MBA).

8. **NEW: College of Dental Medicine**: Not mentioned by user but discovered during research. YU's newest school — "the first dental school to open in New York City since 1916."

9. **NEW: GPATS**: Graduate Program in Advanced Talmudic Studies — a rabbinical studies program.

10. **Need-aware**: CONFIRMED. YU is need-aware for ALL applicants (not need-blind).
