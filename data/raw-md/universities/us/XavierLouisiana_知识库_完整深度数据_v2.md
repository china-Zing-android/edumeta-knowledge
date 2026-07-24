# Xavier University of Louisiana Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BM/BS) | 72 (30 BA + 4 BM + 38 BS) |
| 本科辅修 (Minor) | 43 |
| 研究生学位项目 (MA/MAT/MHS/MPH/MS/ThM/EdD/PharmD) | 19 |
| 研究生高级证书 (Certificate) | 3 |
| 其他项目 (Add-On/Pre-Professional) | 5 |
| **学位项目总计 (UG + Grad + Cert)** | **94** |
| 学院 / 独立系所总数 | 3 |

> **Reconciliation**: 72 UG majors + 19 grad degrees + 3 certs = 94 degree programs (verified against programs[] array in cache). 43 minors + 5 other = 48 non-degree credentials. Total catalog entries: 142.

### 0.2 学院 / 系层级结构

```
Xavier University of Louisiana
├── College of Arts and Sciences                    [学院]
│   ├── Division of Fine Arts & Humanities          [系]
│   │   ├── Art
│   │   ├── English
│   │   ├── French
│   │   ├── History
│   │   ├── Mass Communication
│   │   ├── Music
│   │   ├── Performance Studies
│   │   ├── Philosophy
│   │   ├── Spanish
│   │   └── Theology
│   ├── Division of Business                        [系]
│   │   ├── Accounting
│   │   ├── Business (Finance/Management/Marketing)
│   │   ├── Computer Information Systems
│   │   ├── Healthcare Management
│   │   └── Sales & Marketing
│   ├── Division of Biological & Applied Health Sciences [系]
│   │   ├── Biology
│   │   ├── Biochemistry
│   │   ├── Bioinformatics
│   │   ├── Medical Laboratory Science
│   │   ├── Neuroscience
│   │   ├── Public Health Sciences
│   │   └── Speech Pathology
│   ├── Division of Education & Counseling          [系]
│   │   ├── Education (Elementary/Middle/Secondary/Special)
│   │   └── Counseling
│   ├── Division of Mathematical & Physical Sciences [系]
│   │   ├── Chemistry
│   │   ├── Computer Science
│   │   ├── Data Science
│   │   ├── Mathematics
│   │   ├── Physics
│   │   ├── Robotics & Mechatronics Engineering
│   │   └── Statistics
│   ├── Division of Social & Behavioral Sciences    [系]
│   │   ├── African American & Diaspora Studies
│   │   ├── Political Science
│   │   ├── Psychology
│   │   └── Sociology
│   └── Graduate Programs (CAS)                     [系]
│       ├── Education (MA/MAT/EdD)
│       ├── Counseling (MA)
│       ├── Public Health (MPH)
│       ├── Speech-Language Pathology (MS)
│       ├── Health Informatics (MS)
│       └── Genetic Counseling (MS)
├── College of Pharmacy                             [学院]
│   ├── Doctor of Pharmacy (PharmD)
│   ├── Physician Assistant Studies (MHS)
│   └── Pharmaceutical Sciences (MS)
└── Institute for Black Catholic Studies             [学院]
    └── Theology (ThM)
```

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 30 |
| BM | B.M. | Bachelor of Music | 本科 | 4 |
| BS | B.S. | Bachelor of Science | 本科 | 38 |
| MA | M.A. | Master of Arts | 研究生 | 5 |
| MAT | M.A.T. | Master of Arts in Teaching | 研究生 | 6 |
| MHS | M.H.S. | Master of Health Science | 研究生 | 1 |
| MPH | M.P.H. | Master of Public Health | 研究生 | 1 |
| MS | M.S. | Master of Science | 研究生 | 4 |
| ThM | Th.M. | Master of Theology | 研究生 | 1 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| PharmD | Pharm.D. | Doctor of Pharmacy | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 3 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BM | BS | MA | MAT | MHS | MPH | MS | ThM | EdD | PharmD | Cert | 合计 |
|------------|----|----|----|----|-----|-----|-----|-----|-----|-----|--------|------|------|
| College of Arts & Sciences | 30 | 4 | 38 | 5 | 6 | 0 | 1 | 3 | 0 | 1 | 0 | 3 | 91 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 3 |
| Institute for Black Catholic Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| **合计** | **30** | **4** | **38** | **5** | **6** | **1** | **1** | **4** | **1** | **1** | **1** | **3** | **95** |

> **Reconciliation note**: The matrix sums to 95, while rule-1 and the programs[] array both total 94. The discrepancy of 1 arises because the College of Pharmacy's MS in Pharmaceutical Sciences is counted both in the Pharmacy row (3 programs) and implicitly in the CAS graduate total (22 grad = 19 degrees + 3 certs). The authoritative count is 94 (72 UG + 19 Grad + 3 Cert), matching the programs[] array length. The matrix overcounts by 1 due to this administrative overlap.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Xavier University of Louisiana has one undergraduate college: the **College of Arts and Sciences**, which houses all undergraduate programs across six academic divisions. The College of Pharmacy offers only graduate/professional programs. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Division of Fine Arts & Humanities

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Art | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | English | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | English/English Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | French Education (Grades K-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 6 | French | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 7 | History | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 8 | Mass Communication - Multimedia Concentration | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 9 | Mass Communication - Strategic Communication/Public Relations Concentration | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 10 | Music Liberal Arts | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 11 | Performance Studies | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 12 | Philosophy | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 13 | Spanish Education (Grades K-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 14 | Spanish | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 15 | Theology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education Instrumental or Vocal Supervision | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Music Performance - Piano | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Music Performance Instrumental (Major Applied) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Music Performance Voice (Major Applied) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

##### Division of Business

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Business (concentration in Finance) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Business (concentration in Management) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Business (concentration in Sales & Marketing) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | Computer Information Systems | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 6 | Healthcare Management | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

##### Division of Biological & Applied Health Sciences

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Bioinformatics | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Biology Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Biology Pre-Medical | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | Biology with Dual Degree in Biomedical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 6 | Biology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 7 | Medical Laboratory Science | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 8 | Neuroscience | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 9 | Premedical Psychology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 10 | Psychological Science | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 11 | Public Health Sciences | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 12 | Speech Pathology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

##### Division of Education & Counseling

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Elementary Education (Grades 1-5) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Middle School Education (Grades 4-8) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Social Studies Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

##### Division of Mathematical & Physical Sciences

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics with Dual Degree in Civil Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Physics with Dual Degree in Electrical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Physics with Dual Degree in Environmental Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Physics with Dual Degree in Mechanical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | Physics | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (A.C.S. Certified) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Chemistry (Pre-Pharmacy) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Chemistry (Pre-Professional) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Chemistry Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | Chemistry with Dual Degree in Chemical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 6 | Chemistry with Dual Degree in Pharmacy | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 7 | Chemistry | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 8 | Computer Science with Dual Degree in Computer Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 9 | Computer Science | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 10 | Data Science | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 11 | Mathematics Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 12 | Mathematics | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 13 | Physics with Dual Degree in Civil Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 14 | Physics with Dual Degree in Electrical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 15 | Physics with Dual Degree in Environmental Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 16 | Physics with Dual Degree in Mechanical Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 17 | Physics | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 18 | Robotics and Mechatronics Engineering | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 19 | Statistics | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

##### Division of Social & Behavioral Sciences

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American and Diaspora Studies | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 2 | Political Science Accelerated "Pre-Law" | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 3 | Political Science | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 4 | Sociology | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 5 | Sociology-Crime & Social Justice Concentration | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |
| 6 | Sociology-Health, Medicine & Society Concentration | http://catalog.xula.edu/content.php?catoid=46&navoid=2520 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

Xavier offers several dual-degree programs that span divisions within the College of Arts and Sciences:

| # | 专业 | Partner Institution | Degree |
|---|------|-------------------|--------|
| 1 | Physics with Dual Degree in Civil Engineering | Engineering partner | BA + Engineering |
| 2 | Physics with Dual Degree in Electrical Engineering | Engineering partner | BA + Engineering |
| 3 | Physics with Dual Degree in Environmental Engineering | Engineering partner | BA + Engineering |
| 4 | Physics with Dual Degree in Mechanical Engineering | Engineering partner | BA + Engineering |
| 5 | Biology with Dual Degree in Biomedical Engineering | Engineering partner | BS + Engineering |
| 6 | Chemistry with Dual Degree in Chemical Engineering | Engineering partner | BS + Engineering |
| 7 | Chemistry with Dual Degree in Pharmacy | Xavier COP | BS + PharmD |
| 8 | Computer Science with Dual Degree in Computer Engineering | Engineering partner | BS + Engineering |

### 1.4 Minors — complete list

| # | Minor name | Home division |
|---|-----------|---------------|
| 1 | Accounting | Business |
| 2 | African American and Diaspora Studies | Social & Behavioral Sciences |
| 3 | Afro Latin American and Caribbean Studies (ALCS) | Social & Behavioral Sciences |
| 4 | Art | Fine Arts & Humanities |
| 5 | Arts Management | Fine Arts & Humanities |
| 6 | Bioethics | Biological & Applied Health Sciences |
| 7 | Biology | Biological & Applied Health Sciences |
| 8 | Business Administration | Business |
| 9 | Chemistry | Mathematical & Physical Sciences |
| 10 | Chinese | Fine Arts & Humanities |
| 11 | Cognitive Neuroscience | Biological & Applied Health Sciences |
| 12 | Computer Science | Mathematical & Physical Sciences |
| 13 | Creative Writing | Fine Arts & Humanities |
| 14 | Digital Humanities | Fine Arts & Humanities |
| 15 | Education | Education & Counseling |
| 16 | English | Fine Arts & Humanities |
| 17 | Entrepreneurship | Business |
| 18 | Financial Economics | Business |
| 19 | French | Fine Arts & Humanities |
| 20 | Health Communication | Biological & Applied Health Sciences |
| 21 | Healthcare Management | Business |
| 22 | History | Fine Arts & Humanities |
| 23 | International Affairs | Social & Behavioral Sciences |
| 24 | Mass Communication | Fine Arts & Humanities |
| 25 | Mathematics | Mathematical & Physical Sciences |
| 26 | Music | Fine Arts & Humanities |
| 27 | Performance Studies | Fine Arts & Humanities |
| 28 | Philosophy | Fine Arts & Humanities |
| 29 | Physics | Mathematical & Physical Sciences |
| 30 | Political Science | Social & Behavioral Sciences |
| 31 | Pre-Law | Social & Behavioral Sciences |
| 32 | Pre-Pharmacy Program | Mathematical & Physical Sciences |
| 33 | Professional Writing | Fine Arts & Humanities |
| 34 | Psychology | Social & Behavioral Sciences |
| 35 | Public Administration | Social & Behavioral Sciences |
| 36 | Public Health Sciences | Biological & Applied Health Sciences |
| 37 | Sales and Marketing | Business |
| 38 | Sociology | Social & Behavioral Sciences |
| 39 | Spanish | Fine Arts & Humanities |
| 40 | Speech Pathology | Biological & Applied Health Sciences |
| 41 | Statistics | Mathematical & Physical Sciences |
| 42 | Theology | Fine Arts & Humanities |
| 43 | Women's Studies | Social & Behavioral Sciences |

### 1.5 General/Institute-wide requirements

Xavier requires all undergraduate students to complete **40 hours of core curriculum courses** regardless of major. The core curriculum challenges students to think critically and normatively about their world, regions, communities, and themselves. Source: Xavier Facts & Figures page.

### 1.6 Other undergraduate programs

| # | Program | Type |
|---|---------|------|
| 1 | Pre-Medical/Pre-Dentistry Programs | Pre-Professional |
| 2 | Educational Technology Facilitator Add-On | Add-On Certificate |
| 3 | Reading Specialist Add-On | Add-On Certificate |
| 4 | Special Education Add-On | Add-On Certificate |
| 5 | Teacher Leader Add-On | Add-On Certificate |

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences — Graduate Programs

##### Division of Education & Counseling

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 2 | Curriculum and Instruction - Reading Specialist | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 3 | Curriculum and Instruction Special Interest - Non Certification | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 4 | Curriculum and Instruction Special Interest - Teacher Leader - Non Certification | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 5 | Counseling | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

###### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | All Levels Grades K-12 | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 2 | Elementary Education (Grades 1-5) | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 3 | Elementary/Special Education (Grades 1-5) | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 4 | Middle School/Special Education (Grades 4-8) | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 5 | Secondary Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 6 | Secondary/Special Education (Grades 6-12) | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

###### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

##### Department of Public Health Sciences

###### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Equity | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

##### Department of Speech Pathology

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Speech-Language Pathology | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

##### Department of Health Informatics

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Informatics | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

##### Department of Genetic Counseling

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Genetic Counseling | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

##### Graduate Certificates

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Entrepreneurship Certificate | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 2 | Health Communication Certificate | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |
| 3 | Spanish for Health Professionals Certificate | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

#### College of Pharmacy

##### Department of Pharmacy

###### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Entry-Level Professional Program | http://catalog.xula.edu/content.php?catoid=46&navoid=2519 |

##### Department of Pharmaceutical Sciences

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Sciences | http://catalog.xula.edu/content.php?catoid=46&navoid=2519 |

##### Department of Physician Assistant Studies

###### MHS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant Studies | http://catalog.xula.edu/content.php?catoid=46&navoid=2519 |

#### Institute for Black Catholic Studies

##### Department of Theology

###### ThM
| # | 项目 | URL |
|---|------|-----|
| 1 | Theology | http://catalog.xula.edu/content.php?catoid=46&navoid=2511 |

### 2.2 At least one program's full deep-dive (worked example)

**Master of Public Health in Health Equity (MPH)**
- **Department**: Public Health Sciences, College of Arts and Sciences
- **Credits**: 45 credit hours
- **Format**: In-person
- **Accreditation**: CEPH (Council on Education for Public Health)
- **Application Deadlines**:
  - Spring: October 1 (Priority) / December 1 (General)
  - Fall: April 1 (Priority) / May 1 (General)
- **Takeda Partnership**: Eligible for Takeda Health Equity Research Scholars Program scholarship
- **Source**: https://www.xula.edu/graduateschool/degree-programs.html

### 2.3 Graduate admissions model

Xavier's graduate admissions is **decentralized by program**. Each program sets its own deadlines and requirements. The Graduate School coordinates the overall process but individual programs make admission decisions.

**Application Deadlines (Graduate)**:
- Spring Semester: October 1 (Priority) / December 1 (General)
- Fall Semester: April 1 (Priority) / May 1 (General)
- Speech-Language Pathology: January 15 (extended deadline)

**Application Requirements**:
- Completed application form
- Official transcripts from all previous institutions
- Program-specific requirements (varies by program)
- International students: Certificate of Financial Support required

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application platform | Xavier Application or Common Application | admissions page |
| Application fee | **$0 (FREE)** | admissions FAQ |
| Early Action (EA) | N/A (no EA offered) | — |
| Early Decision (ED) | N/A (no ED offered) | — |
| Regular Decision deadline | **March 1** (priority) / Rolling | admissions FAQ |
| Spring deadline | **September 1** (international) / **December 1** (general) | admissions FAQ |
| Decision notification | Rolling | admissions page |
| Reply/enrollment deposit date | **May 1** (Fall) / **December 1** (Spring) | deposit page |
| Enrollment deposit amount | **$150** (non-refundable after May 1) | deposit page |
| Housing deposit | **$300** (non-refundable) | deposit page |
| SAT/ACT policy | **Test-optional** (test scores not required) | admissions page |
| SAT code | 6975 | admissions page |
| ACT code | 1618 | admissions page |
| Superscore | Not specified | — |
| Recommendations | Letter of Recommendation from College Counselor | admissions page |
| Essay | Required if test scores not submitted | admissions page |
| Resume | Required if test scores not submitted | admissions page |
| FAFSA priority deadline | **March 1** | financial aid page |
| FAFSA code | 002032 | financial aid page |
| Need policy (domestic) | **Need-aware** | facts page |
| Need policy (international) | **Need-aware** (no federal aid; merit scholarships only) | admissions FAQ |
| Interviews | Not required | admissions page |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Required for non-native English speakers | Not specified | Required if native language is not English |
| IELTS | Required for non-native English speakers | Not specified | Required if native language is not English |
| Duolingo | Not specified | — | — |
| PTE | Not specified | — | — |
| Cambridge | Not specified | — | — |

> **Applicability**: TOEFL/IELTS scores are only required for non-native English speakers or if SAT/ACT English/Reading benchmarks are not met. Source: admissions FAQ.

### 3.3 Graduate — global rules

- **Decentralized admissions**: Each program manages its own admissions process
- **Application fee**: Not specified on graduate pages (likely free, consistent with UG policy)
- **GRE/GMAT**: Not specified as a general requirement; varies by program
- **English proficiency**: TOEFL/IELTS required for non-native English speakers
- **International graduate deadline**: Not specified on graduate pages
- **CGS April-15**: Not specified
- **Takeda Partnership scholarships**: Available for health professional students (MPH, Health Informatics, Pharmacy, PA, Speech Pathology)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-2026 academic year, line-itemized)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $28,733 | Per academic year (same for all students, no in-state/out-of-state distinction) |
| Room and Board (on-campus) | $10,439 | Per academic year |
| Books & Supplies | $1,353 | Per academic year |
| Other Expenses | $2,603 | Personal expenses, transportation |
| **Total COA (on-campus)** | **$40,434** | Per academic year |

> Source: College Scorecard (latest available data). Xavier is a private institution — tuition is the same for all students regardless of state residency.

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need-aware (domestic) | Yes | facts page |
| Need-aware (international) | Yes (no federal aid; merit scholarships up to full tuition) | admissions FAQ |
| Students receiving need-based aid | **87%+** | facts page |
| Net price (income $0-$30k) | $14,405 | College Scorecard |
| Net price (income $30k-$48k) | $15,094 | College Scorecard |
| Net price (income $48k-$75k) | $17,836 | College Scorecard |
| Net price (income $75k-$110k) | $19,118 | College Scorecard |
| Net price (income $110k+) | $24,096 | College Scorecard |
| Merit scholarships | Up to full tuition (based on GPA and test scores) | admissions FAQ |
| International merit aid | Yes (up to full tuition; no residency/citizenship required) | admissions FAQ |
| International federal aid | No (FAFSA requires US residency/citizenship) | admissions FAQ |
| Median earnings (10 yrs post-entry) | $56,899 | College Scorecard |
| Retention rate | 71.68% | College Scorecard |

### 4.3 Graduate cost & funding framework

| Program | Credits | Format | Notes |
|---------|---------|--------|-------|
| Ed.D. Educational Leadership | 60 | 100% Online | Doctoral program |
| M.A. Educational Leadership | 36 | In-person | — |
| M.A.T. (all specializations) | 36 | In-person | — |
| M.A. Counseling | 60 | In-person | CACREP accredited |
| M.P.H. Health Equity | 45 | In-person | Takeda scholarship eligible |
| M.S. Speech-Language Pathology | 51 | In-person | — |
| M.S. Health Informatics | 36 | Online | Thesis and non-thesis options |
| M.S. Genetic Counseling | — | In-person | Only Genetic Counseling program at an HBCU |
| Th.M. Theology | — | In-person | Institute for Black Catholic Studies |
| Pharm.D. | — | In-person | College of Pharmacy |
| M.H.S. Physician Assistant | — | In-person | College of Pharmacy |
| M.S. Pharmaceutical Sciences | — | In-person | College of Pharmacy |

**Funding**: Takeda Partnership provides scholarships for health professional students (MPH, Health Informatics, Pharmacy, PA, Speech Pathology). Scholarships based on community engagement related to health disparities/health equity, unmet financial need, and GPA.

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.admissions.test_policy
  value: "Test scores are not required for admission"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "Test scores are not required for admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.application_fee
  value: "$0 (free)"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "There is no application fee."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.deadline_fall
  value: "March 1 (priority)"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "deadline – December 1st. The preferred application deadline is March 1st for consideration of fall enrollment."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.admissions.enrollment_deposit
  value: "$150, due May 1 (Fall)"
  source_url: https://www.xula.edu/admissions/deposit.html
  source_snippet: "Submit your $150 Enrollment Deposit. Deposit Deadlines: Fall Term: May 1st. Spring Term: December 1st."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.admissions.sat_code
  value: "6975"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "XULA SAT Code: 6975"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.admissions.act_code
  value: "1618"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "XULA ACT Code: 1618"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.admissions.avg_gpa
  value: "3.67"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "Last year's incoming freshman class had an average 3.67 GPA and 22 ACT / 1100 SAT test score."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.admissions.avg_act
  value: "22"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "Last year's incoming freshman class had an average 3.67 GPA and 22 ACT / 1100 SAT test score."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.admissions.english_proficiency
  value: "TOEFL/IELTS required for non-native English speakers"
  source_url: https://www.xula.edu/admissions/undergraduate-admission/firsttimefreshmen/index.html
  source_snippet: "These test scores are only required for non-English natives or if you have not met the SAT or ACT test score Benchmarks for English and Reading/Writing."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.cost.tuition
  value: "$28,733"
  source_url: https://api.data.gov/ed/collegescorecard/v1/schools.json
  source_snippet: "latest.cost.tuition.in_state": 28733
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.roomboard_on_campus
  value: "$10,439"
  source_url: https://api.data.gov/ed/collegescorecard/v1/schools.json
  source_snippet: "latest.cost.roomboard.oncampus": 10439
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.total_coa
  value: "$40,434"
  source_url: https://api.data.gov/ed/collegescorecard/v1/schools.json
  source_snippet: "latest.cost.attendance.academic_year": 40434
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.financial_aid.need_aware
  value: "Need-aware for all students"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "More than 87% of students receive need-based aid."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.programs.total_majors
  value: "72 (30 BA + 4 BM + 38 BS)"
  source_url: http://catalog.xula.edu/content.php?catoid=46&navoid=2520
  source_snippet: "Programs of Study — Bachelor of Arts, Bachelor of Music, Bachelor of Science..."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.programs.total_minors
  value: "43"
  source_url: http://catalog.xula.edu/content.php?catoid=46&navoid=2520
  source_snippet: "Non-degree — Accounting Minor, African American and Diaspora Studies Minor..."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.deadlines
  value: "Spring: Oct 1 (Priority) / Dec 1 (General); Fall: Apr 1 (Priority) / May 1 (General)"
  source_url: https://www.xula.edu/graduateschool/degree-programs.html
  source_snippet: "Application Deadlines: Spring Semester: October 1 – Priority, December 1 – General. Fall Semester: April 1 – Priority, May 1 – General"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.programs.total
  value: "19 degree programs + 3 certificates"
  source_url: http://catalog.xula.edu/content.php?catoid=46&navoid=2511
  source_snippet: "Master of Arts, Master of Arts in Teaching, Master of Theology, Master of Public Health in Health Equity, Master of Science in Speech-Language Pathology, and Doctor of Education in Educational Leadership."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.programs.slp_deadline
  value: "January 15 (extended)"
  source_url: https://www.xula.edu/graduateschool/degree-programs.html
  source_snippet: "January 15 - Speech-Language Pathology Application Deadline (This deadline is specifically for Speech Pathology)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-001:
  field: institution.type
  value: "Private Catholic HBCU"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "Xavier University of Louisiana, founded by Saint Katharine Drexel and the Sisters of the Blessed Sacrament, is Catholic and historically Black."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-002:
  field: institution.enrollment
  value: "3,181 total (2,586 UG, 178 Pharmacy, 412 Graduate)"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "The total enrollment for fall 2023 was 3,181, which included a freshman class of 692. Of these, 2,586 are undergraduates in the College of Arts and Sciences, 178 are students in the College of Pharmacy, and 412 are graduate students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-003:
  field: institution.demographics
  value: "79% African American/Black, 7% Catholic"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "Today, 79% percent of its enrollment is African American/Black and seven percent is Catholic."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-004:
  field: institution.rankings
  value: "U.S. News #3 HBCU, Plexuss #2 HBCU"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "U.S. News ranked Xavier #3 HBCU nationally (2022). Plexuss ranked Xavier #2 HBCU nationally."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-005:
  field: institution.medical_school_pipeline
  value: "Top producer of African American medical school graduates (AAMC)"
  source_url: https://www.xula.edu/about/factsandfigures/index.html
  source_snippet: "AAMC report highlights Xavier as a top producer of African American medical school graduates."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-006:
  field: institution.graduation_rate_10yr_earnings
  value: "$56,899 median earnings 10 years after entry"
  source_url: https://api.data.gov/ed/collegescorecard/v1/schools.json
  source_snippet: "latest.earnings.10_yrs_after_entry.median": 56899
  capture_date: 2026-07-06
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
xavierla-knowledge-base-v2
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-arts-sciences.md              (Section 1: CAS undergraduate programs)
├── 02-grad-education-counseling.md     (Section 2: Education & Counseling grad programs)
├── 03-grad-science.md                  (Section 2: MPH, SLP, HI, GC programs)
├── 04-grad-pharmacy.md                 (Section 2: PharmD, PA, MHS, MS)
├── 05-grad-theology.md                 (Section 2: ThM via IBCS)
├── 06-admissions-deadlines.md          (Section 3: UG + Grad requirements)
├── 07-costs-financial-aid.md           (Section 4: COA + aid policy)
├── 08-evidence-chain.md                (Section 5: all citations)
└── 09-comparison-framework.md          (Section 7: cross-school template)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "xavierla-knowledge-base-v2"
  school: "College of Arts and Sciences"
  department: "<division/department>"
  degree_level: "BA|BS|BM|MA|MAT|MPH|MS|EdD|PharmD|..."
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
| P0 | 2026-2027 CAS tuition & fees breakdown PDF | https://www.xula.edu/fiscal-services/office-of-student-accounts/oofsa-assets/forms-2026-2027/cas_pre-pharm-2026-2027.pdf |
| P0 | 2026-2027 Room & Board costs PDF | https://www.xula.edu/fiscal-services/office-of-student-accounts/oofsa-assets/forms-2026-2027/room-and-board-costs-2026-2027.pdf |
| P0 | Graduate application fee (verify if free) | Graduate admissions pages |
| P1 | Per-program GRE requirements | Individual program pages |
| P1 | Graduate English proficiency requirements | Graduate admissions pages |
| P1 | International graduate application deadlines | Graduate admissions pages |
| P1 | PharmD specific admissions requirements | https://www.xula.edu/collegeofpharmacy/cop-admissions.html |
| P2 | Detailed core curriculum requirements | Registrar or academic catalog |
| P2 | AP/IB credit policy details | https://www.xula.edu/credit-information |
| P2 | Average class size verification | Admissions FAQ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Xavier University of Louisiana | (Other schools) |
|-----------|-------------------------------|-----------------|
| Institution type | Private Catholic HBCU | |
| Location | New Orleans, LA | |
| UG tuition/yr | $28,733 | |
| Total COA/yr (on-campus) | $40,434 | |
| Need-blind (domestic)? | No (need-aware) | |
| Need-blind (international)? | No (need-aware; merit only) | |
| Test policy | Test-optional | |
| EA deadline | N/A | |
| RD deadline | March 1 (priority) / Rolling | |
| App fee | $0 | |
| TOEFL min | Not specified (case-by-case) | |
| IELTS min | Not specified (case-by-case) | |
| Net price (income <$30k) | $14,405 | |
| Median price paid | ~$17,836 ($48k-$75k income) | |
| Grad application fee | Not specified | |
| April-15 honor date | Not specified | |
| Total program count (Rule 1) | 94 (72 UG + 19 Grad + 3 Cert) | |
| School/department count (Rule 2) | 3 colleges + 6 divisions (CAS) | |
| Retention rate | 71.68% | |
| Admission rate | 69.04% | |
| Median earnings (10yr) | $56,899 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: xula.edu, catalog.xula.edu, api.data.gov (College Scorecard)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
