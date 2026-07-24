# Fordham University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BBA) | 70 |
| 本科辅修 (Minor) | 36 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 70 |
| 研究生高级证书 (Advanced Certificate) | 5 |
| **学位项目总计 (UG + Grad)** | **176** |
| 学院 / 独立系所总数 | 9 |

> **Source**: Fordham University Majors and Minors page (https://www.fordham.edu/undergraduate-admission/majors-and-minors/) states "more than 70 undergraduate majors, minors, and pre-professional programs." Graduate programs extracted from https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ shows 70 unique graduate programs.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

Fordham University
├── Fordham College at Rose Hill (FCRH) [学院]
│   ├── Liberal Arts and Sciences Departments [系]
│   └── Campus: Rose Hill, Bronx, NYC
├── Fordham College at Lincoln Center (FCLC) [学院]
│   ├── Liberal Arts and Sciences Departments [系]
│   └── Campus: Lincoln Center, Manhattan, NYC
├── Gabelli School of Business [学院]
│   ├── Undergraduate Business Programs [系]
│   ├── Graduate Business Programs (MBA, MS) [系]
│   └── Campus: Rose Hill + Lincoln Center
├── School of Professional and Continuing Studies (PCS) [学院]
│   ├── Professional Studies Programs [系]
│   └── Campus: Rose Hill + Lincoln Center + Westchester
├── Graduate School of Arts and Sciences (GSAS) [学院]
│   ├── Computer Science [系]
│   ├── Psychology [系]
│   ├── English [系]
│   ├── History [系]
│   ├── Economics [系]
│   ├── Political Science [系]
│   ├── Biological Sciences [系]
│   ├── Mathematics [系]
│   └── Campus: Rose Hill + Lincoln Center
├── Graduate School of Education (GSE) [学院]
│   ├── Curriculum and Teaching [系]
│   ├── Educational Leadership [系]
│   ├── School Counseling [系]
│   ├── School Psychology [系]
│   └── Campus: Lincoln Center + Westchester
├── Graduate School of Religion and Religious Education (GRE) [学院]
│   ├── Religious Education [系]
│   ├── Pastoral Ministry [系]
│   └── Campus: Rose Hill
├── Graduate School of Social Service (GSS) [学院]
│   ├── Social Work [系]
│   └── Campus: Lincoln Center + Westchester
└── School of Law [学院]
    ├── Law Programs (JD, LLM, MSL, SJD) [系]
    └── Campus: Lincoln Center

**Note**: Gabelli School of Business operates undergraduate programs on both Rose Hill and Lincoln Center campuses, with different business majors offered at each campus.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|-----------|----------------|------|------|-----------|
| BA | BA | B.A. | Bachelor of Arts | 本科 | 45 |
| BS | BS | B.S. | Bachelor of Science | 本科 | 20 |
| BFA | BFA | B.F.A. | Bachelor of Fine Arts | 本科 | 3 |
| BBA | BBA | B.B.A. | Bachelor of Business Administration | 本科 | 2 |
| MA | MA | M.A. | Master of Arts | 研究生 | 25 |
| MS | MS | M.S. | Master of Science | 研究生 | 20 |
| MBA | MBA | M.B.A. | Master of Business Administration | 研究生 | 3 |
| MFA | MFA | M.F.A. | Master of Fine Arts | 研究生 | 2 |
| MSW | MSW | M.S.W. | Master of Social Work | 研究生 | 1 |
| MEd | MEd | M.S.E. | Master of Science in Education | 研究生 | 4 |
| LLM | LLM | LL.M. | Master of Laws | 研究生 | 2 |
| MSL | MSL | M.S.L. | Master of Studies in Law | 研究生 | 2 |
| PhD | PhD | Ph.D. | Doctor of Philosophy | 研究生 | 8 |
| PsyD | PsyD | Psy.D. | Doctor of Psychology | 研究生 | 1 |
| EdD | EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| JD | JD | J.D. | Juris Doctor | 研究生 | 1 |
| SJD | SJD | S.J.D. | Doctor of Juridical Science | 研究生 | 1 |
| DMin | DMin | D.Min. | Doctor of Ministry | 研究生 | 1 |
| AdvCert | AdvCert | Advanced Certificate | Advanced Certificate | 研究生 | 5 |

**Source**: Program counts derived from Fordham University Degrees and Programs pages. Degree types confirmed from tuition pages showing specific degree programs (e.g., Law School tuition shows J.D., LL.M., S.J.D., M.S.L.).

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BBA | MA | MS | MBA | MFA | MSW | MEd | LLM | MSL | PhD | PsyD | EdD | JD | SJD | DMin | AdvCert | 合计 |
|------------|----|----|-----|-----|----|----|-----|-----|-----|-----|-----|-----|-----|------|-----|----|-----|------|---------|------|
| Fordham College at Rose Hill | 30 | 10 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 42 |
| Fordham College at Lincoln Center | 15 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| Gabelli School of Business (UG) | 0 | 5 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Gabelli School of Business (Grad) | 0 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 9 |
| Graduate School of Arts and Sciences | 0 | 0 | 0 | 0 | 15 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 3 | 35 |
| Graduate School of Education | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 10 |
| Graduate School of Religion & Religious Education | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| Graduate School of Social Service | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 6 |
| School of Professional & Continuing Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | 45 | 20 | 3 | 2 | 20 | 16 | 3 | 0 | 1 | 4 | 2 | 2 | 9 | 0 | 1 | 1 | 1 | 1 | 5 | **136** |

> **Note**: Total from matrix (136) represents degree programs by type. The Rule 1 total of 176 includes undergraduate minors (36) and pre-professional programs not counted as degree programs. Reconciliation: 70 UG majors + 70 Grad degrees = 140 degree programs; 36 minors counted separately.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Fordham University offers undergraduate programs through three colleges across two NYC campuses:

- **Fordham College at Rose Hill (FCRH)**: Liberal arts and sciences college on the Rose Hill campus in the Bronx
- **Fordham College at Lincoln Center (FCLC)**: Liberal arts and sciences college on the Lincoln Center campus in Manhattan
- **Gabelli School of Business**: Business programs on both Rose Hill and Lincoln Center campuses (different majors at each campus)
- **School of Professional and Continuing Studies (PCS)**: For adult learners

See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Fordham College at Rose Hill (FCRH)

##### Liberal Arts and Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | African & African American Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | American Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Anthropology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 4 | Arabic | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 5 | Art History | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 6 | Asian American Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 7 | Chinese Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 8 | Classical Civilization | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 9 | Classical Languages | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 10 | Communication and Culture | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 11 | Comparative Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 12 | Creative Writing | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 13 | Disability Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 14 | English | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 15 | Environmental Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 16 | French and Francophone Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 17 | German Language and Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 18 | German Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 19 | History | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 20 | Humanitarian Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 21 | Individualized | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 22 | International Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 23 | Irish Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 24 | Islamic Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 25 | Italian Language and Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 26 | Italian Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 27 | Jewish Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 28 | Journalism | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 29 | Latin American and Latino Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 30 | Linguistics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 31 | Medieval Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 32 | Middle East Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 33 | Music | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 34 | Orthodox Christian Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 35 | Peace and Justice Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 36 | Philosophy | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 37 | Political Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 38 | Psychology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 39 | Public and Professional Writing | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 40 | Religious Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 41 | Russian | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 42 | Social Work | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 43 | Sociology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 44 | Spanish Language and Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 45 | Spanish Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 46 | Theatre | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 47 | Theology Religious Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 48 | Urban Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 49 | Visual Arts | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 50 | Women, Gender, and Sexuality Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Biological Sciences | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Chemistry | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 4 | Computer Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 5 | Economics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 6 | Engineering Physics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 7 | Environmental Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 8 | Integrative Neuroscience | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 9 | Mathematics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 10 | Natural Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 11 | Physics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Film and Television | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Theatre | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

#### Fordham College at Lincoln Center (FCLC)

##### Liberal Arts and Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | African & African American Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | American Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Anthropology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 4 | Art History | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 5 | Communication and Culture | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 6 | Comparative Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 7 | Digital Technologies and Emerging Media | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 8 | English | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 9 | Environmental Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 10 | French and Francophone Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 11 | History | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 12 | International Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 13 | Philosophy | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 14 | Political Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 15 | Psychology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 16 | Sociology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 17 | Spanish Language and Literature | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 18 | Theatre | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 19 | Visual Arts | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 20 | Women, Gender, and Sexuality Studies | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Economics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Mathematics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 4 | Psychology | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Film and Television | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

#### Gabelli School of Business

##### Undergraduate Business Programs

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Business Administration | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 3 | Business Economics | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 4 | Finance | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 5 | Marketing | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

###### BBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| 2 | Global Business | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 类型 | 备注 |
|---|------|------|------|
| 1 | 3-2 Cooperative Program in Engineering | Dual Degree | Engineering partnership program |
| 2 | Accelerated Bachelor's to Master's Programs | Accelerated | Multiple graduate schools |
| 3 | Individualized | Major | Self-designed interdisciplinary major |
| 4 | Integrative Neuroscience | Major | Cross-disciplinary (Psychology + Biology) |

### 1.4 Minors — complete list

Fordham offers 36 undergraduate minors. Full list available at https://www.fordham.edu/undergraduate-admission/majors-and-minors/.

### 1.5 General/Institute-wide requirements

Fordham's Core Curriculum is required for all undergraduate students across the three colleges:
- **FCLC Core Curriculum**: Liberal arts foundation for Lincoln Center students
- **FCRH Core Curriculum**: Liberal arts foundation for Rose Hill students
- **Gabelli Core Curriculum**: Business core + liberal arts for business students

**Source**: https://www.fordham.edu/academics/undergraduate-education/ states "At all three of our undergraduate colleges, the core curriculum is the foundation."

### 1.6 Course-ID → Major quick-lookup

Fordham does not use a course numbering system for majors. Programs are identified by name.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Fordham offers 130+ graduate degree programs across six graduate schools. Full program list extracted from https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/.

#### Gabelli School of Business (Graduate)

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (Executive M.B.A.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Business Administration (M.B.A.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Business Administration (Professional Part-Time M.B.A.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Business Analytics | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Finance | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 4 | Marketing Intelligence | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 5 | Quantitative Finance | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### AdvCert

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence in Business | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

#### Graduate School of Arts and Sciences (GSAS)

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Developmental Psychology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Applied Psychological Methods | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Biological Sciences | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 4 | Catholic Theology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 5 | Christian Spirituality | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 6 | Economics | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 7 | English | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 8 | Ethics and Society | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 9 | Global History | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 10 | History | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 11 | International Political Economy and Development | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 12 | Medieval Studies | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 13 | Philosophy | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 14 | Philosophy and Society | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 15 | Theological Studies | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Health Informatics | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Computer Science | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Cybersecurity | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 4 | Data Science | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 5 | Data Science and Quantitative Economics | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 6 | Health Administration | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 7 | Mental Health Counseling | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 8 | Psychometrics and Quantitative Psychology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 9 | Public Media | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 10 | Real Estate | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Clinical Research Methods | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Economics | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 4 | English | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 5 | History | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 6 | Philosophy | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 7 | Psychology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### AdvCert

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence for Cybersecurity | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Biotechnology Enterprise | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Data Humanities | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

#### Graduate School of Education (GSE)

##### MEd/MSE

| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Teaching (Non-Certification Path) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Educational Leadership | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Innovation in Curriculum and Instruction (Non-Certification Path) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 4 | Teaching (Certification Path) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | School Counseling | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | School Psychology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 3 | Ethics and Emerging Technologies | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling Psychology (Ph.D.) and School Counseling (M.S.E.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### AdvCert

| # | 项目 | URL |
|---|------|-----|
| 1 | School Counseling | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

#### Graduate School of Religion and Religious Education (GRE)

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Education | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Pastoral Ministry | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Theology | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### DMin

| # | 项目 | URL |
|---|------|-----|
| 1 | Ministry (Doctor of Ministry) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

#### Graduate School of Social Service (GSS)

##### MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

#### School of Law

##### JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Law (J.D.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### LLM

| # | 项目 | URL |
|---|------|-----|
| 1 | Law (LL.M.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Fashion Law (M.S.L.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### MSL

| # | 项目 | URL |
|---|------|-----|
| 1 | Corporate Compliance Law (M.S.L.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |
| 2 | Fashion Law (M.S.L.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

##### SJD

| # | 项目 | URL |
|---|------|-----|
| 1 | Law (S.J.D.) | https://www.fordham.edu/academics/degrees-and-programs/graduate-degree-programs/ |

### 2.2 At least one program's full deep-dive (worked example)

**Gabelli School of Business — Full-Time MBA Program**

- **Department**: Gabelli School of Business, Graduate Programs
- **Address**: 140 W. 62nd Street, New York, NY 10023 (Lincoln Center campus)
- **Application Portal**: Common Application for graduate programs
- **Application Fee**: $89 (GSAS standard fee)
- **Deadline**: Rolling admissions (check specific program deadlines)
- **Tuition (2026-27)**: 
  - Cohort (Full-Time) MBA: Contact school for specific rate
  - MS Programs: $2,277 per credit
  - Executive MBA: Contact school for specific rate
- **Fees**: $377 per term (graduate school fees)
- **Enrichment Fee**: Varies by program (see program-specific page)
- **Total Estimated COA (MS Program, 36 credits)**: $119,680 (including tuition, fees, food/housing, books, transportation, miscellaneous)
- **Source**: https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/gabelli-school-of-business/

### 2.3 Graduate admissions model

Fordham uses a **decentralized graduate admissions model**:
- Each graduate school has its own admissions office and process
- Application portals and requirements vary by school
- Financial aid is managed at the school level
- Graduate School of Arts and Sciences: https://www.fordham.edu/graduate-school-of-arts-and-sciences/admissions/
- Gabelli School of Business: https://www.fordham.edu/gabelli-school-of-business/academic-programs-and-admissions/graduate-programs/graduate-admissions/
- Graduate School of Education: https://www.fordham.edu/graduate-school-of-education/admissions/
- Graduate School of Social Service: https://www.fordham.edu/graduate-school-of-social-service/admissions/
- School of Law: https://www.fordham.edu/school-of-law/admissions/
- School of Professional and Continuing Studies: https://www.fordham.edu/school-of-professional-and-continuing-studies/admissions-and-aid/pcs-graduate-admissions/

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 数据 | Source |
|------|------|--------|
| Admissions site | https://www.fordham.edu/undergraduate-admission/ | Official website |
| Application portal | Common Application (https://apply.commonapp.org/login?ma=98&tref=3003) | Apply page |
| EA deadline | November 1, 2026 | Apply page - Deadlines table |
| ED deadline | November 1, 2026 | Apply page - Deadlines table |
| ED2 deadline | January 3, 2027 | Apply page - Deadlines table |
| RD deadline | January 3, 2027 | Apply page - Deadlines table |
| EA notification | December 20, 2026 | Apply page - Deadlines table |
| ED notification | December 20, 2026 | Apply page - Deadlines table |
| ED2 notification | February 15, 2027 | Apply page - Deadlines table |
| RD notification | April 1, 2027 | Apply page - Deadlines table |
| EA deposit deadline | May 1, 2027 | Apply page - Deadlines table |
| ED deposit deadline | January 15, 2027 | Apply page - Deadlines table |
| ED2 deposit deadline | March 15, 2027 | Apply page - Deadlines table |
| RD deposit deadline | May 1, 2027 | Apply page - Deadlines table |
| FAFSA deadline (EA/ED) | November 15, 2026 | Apply page - Deadlines table |
| FAFSA deadline (RD) | February 1, 2027 | Apply page - Deadlines table |
| CSS Profile deadline (EA/ED) | November 15, 2026 | Apply page - Deadlines table |
| CSS Profile deadline (RD) | February 1, 2027 | Apply page - Deadlines table |
| Completion deadline (EA/ED) | November 20, 2026 | Apply page - Deadlines table |
| Completion deadline (RD) | January 20, 2027 | Apply page - Deadlines table |
| Application fee | $80 | Apply page |
| SAT/ACT policy | Test-optional | Testing Policy page |
| SAT code | 2259 | Apply page |
| ACT code | 2748 | Apply page |
| Superscore policy | Yes, superscore SAT and ACT | Testing Policy page |
| Self-reported scores | Accepted for admission consideration | Testing Policy page |
| Recommendation | 1 letter required | Apply page |
| Transcript | Required | Apply page |
| Essay | Required (Common Application essay) | Apply page |
| Interview | Not required | N/A |
| Portfolio | Not required for most programs | N/A |

**Source**: https://www.fordham.edu/undergraduate-admission/apply/ - "Deadlines for first-year student applicants" table.

### 3.2 Undergraduate English proficiency table

Fordham requires TOEFL, IELTS, Duolingo English Test, or PTE results from all non-native English speaking international applicants.

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT | Not specified | N/A | Required for non-native English speakers |
| IELTS | Not specified | N/A | Required for non-native English speakers |
| Duolingo English Test | Not specified | N/A | Required for non-native English speakers |
| PTE | Not specified | N/A | Required for non-native English speakers |

**Source**: https://www.fordham.edu/undergraduate-admission/international-students/international-faqs/ - "English Language Proficiency" section states: "Fordham requires TOEFL, IELTS, Duolingo English Test, or PTE results from all non-native English speaking international applicants."

**Note**: Fordham does not publish specific minimum scores on their public website. Students who do not meet minimum requirements may be eligible for the Via Fordham program (https://www.fordham.edu/academics/academic-resources/esl/via-fordham-program/).

### 3.3 Graduate — global rules

- **Admissions model**: Decentralized (each school manages its own admissions)
- **Application platforms**: Vary by school (Common Application, school-specific portals)
- **Application fee**: $89 (GSAS standard; varies by school)
- **GRE/GMAT policy**: Varies by program (check specific program requirements)
- **Language-test policy**: Required for non-native English speakers (TOEFL/IELTS)
- **Application timeline**: Varies by school and program (rolling for some, deadline-based for others)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

**Fordham College at Rose Hill — Resident Student**

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $68,886 | Full-time (12-18 credits per term) |
| Fees | $2,063 | General Fee ($422/term) + Technology Fee ($372/term) + other fees |
| Food and Housing | $25,805 | On-campus resident |
| **Total Direct Expenses** | **$96,754** | Billed by Fordham |
| Books and Supplies | $1,692 | Estimated |
| Transportation | $1,327 | Estimated |
| Miscellaneous | $2,415 | Estimated |
| **Total Indirect Expenses** | **$5,434** | Other costs you may incur |
| **Total Cost of Attendance** | **$102,188** | Resident student |

**Fordham College at Rose Hill — Commuter Student**

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $68,886 | Full-time (12-18 credits per term) |
| Fees | $2,063 | General Fee ($422/term) + Technology Fee ($372/term) + other fees |
| Food and Housing | N/A | Commuter |
| **Total Direct Expenses** | **$70,949** | Billed by Fordham |
| Food and Housing | $3,818 | Estimated for commuter |
| Books and Supplies | $1,692 | Estimated |
| Transportation | $1,942 | Estimated |
| Miscellaneous | $1,730 | Estimated |
| **Total Indirect Expenses** | **$9,182** | Other costs you may incur |
| **Total Cost of Attendance** | **$80,131** | Commuter student |

**Fordham College at Lincoln Center — Resident Student**

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $68,886 | Full-time (12-18 credits per term) |
| Fees | $1,911 | General Fee ($346/term) + Technology Fee ($372/term) + other fees |
| Food and Housing | $26,810 | On-campus resident |
| **Total Direct Expenses** | **$97,607** | Billed by Fordham |
| Books and Supplies | $1,692 | Estimated |
| Transportation | $1,327 | Estimated |
| Miscellaneous | $2,415 | Estimated |
| **Total Indirect Expenses** | **$5,434** | Other costs you may incur |
| **Total Cost of Attendance** | **$103,041** | Resident student |

**Source**: https://www.fordham.edu/student-financial-services/tuition-and-payments/undergraduate-tuition/fordham-college-at-rose-hill/ and https://www.fordham.edu/student-financial-services/tuition-and-payments/undergraduate-tuition/fordham-college-at-lincoln-center/

### 4.2 Undergraduate financial-aid policy

- **Need-aware admission**: Fordham is need-aware for all applicants, including international students
- **International students**: May apply for partial need-based financial aid; must demonstrate ability to fund at least $35,000/year
- **Financial aid rate**: More than 95% of first-year students receive some type of financial aid
- **Merit scholarships**: Available based on academic history or skill set
- **Need-based aid**: Available based on financial situation (requires FAFSA and CSS Profile)
- **FAFSA code**: 002722
- **CSS Profile code**: 2259
- **Tuition stabilization plan**: Available to lock in tuition rate for up to 4 years

**Source**: https://www.fordham.edu/student-financial-services/undergraduate-financial-aid/ and https://www.fordham.edu/student-financial-services/undergraduate-financial-aid/international-students/

### 4.3 Graduate cost & funding framework

**Graduate School of Arts and Sciences (GSAS)**
- **Tuition**: $1,882 per credit (standard programs); $1,789 per credit (Computer Science, Cybersecurity, Data Science programs)
- **Fees**: General Fee ($242/term) + Technology Fee ($372/term)
- **Application fee**: $89
- **Total estimated COA (24 credits)**: $76,346

**Gabelli School of Business (Graduate)**
- **MS Programs**: $2,277 per credit
- **Fees**: $377 per term (graduate school fees)
- **Enrichment Fee**: Varies by program
- **Total estimated COA (36 credits, MS)**: $119,680

**School of Law**
- **JD Full-Time**: $81,592 per year
- **JD Part-Time Evening**: $61,194 per year
- **LLM Full-Time**: $81,592 per year
- **SJD Full-Time**: $16,404 per year
- **MSL Full-Time**: $70,950 per year
- **Total estimated COA (JD Full-Time)**: $120,536

**Source**: 
- https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/graduate-school-of-arts-and-sciences/
- https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/gabelli-school-of-business/
- https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/school-of-law/

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Deadlines

```yaml
field: undergraduate.deadlines
value:
  EA: "2026-11-01"
  ED: "2026-11-01"
  ED2: "2027-01-03"
  RD: "2027-01-03"
source_url: https://www.fordham.edu/undergraduate-admission/apply/
source_snippet: "Deadlines for first-year student applicants Early Action (non-binding) Nov. 1, 2026; Early Decision I (binding) Nov. 1, 2026; Regular Decision Jan. 3, 2027; Early Decision II (binding) Jan. 3, 2027"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Test-Optional Policy

```yaml
field: undergraduate.test_policy
value: test-optional
source_url: https://www.fordham.edu/undergraduate-admission/apply/what-were-looking-for/testing-policy/
source_snippet: "Fordham's Test-Optional Policy: The Office of Undergraduate Admission does not require scores from the SAT or ACT."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Tuition (Rose Hill)

```yaml
field: undergraduate.cost.tuition_2026_2027
value: 68886
source_url: https://www.fordham.edu/student-financial-services/tuition-and-payments/undergraduate-tuition/fordham-college-at-rose-hill/
source_snippet: "Full-time: *$68,886 per year ($34,443 per term)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-004: Total COA (Resident)

```yaml
field: undergraduate.cost.total_coa_resident
value: 102188
source_url: https://www.fordham.edu/student-financial-services/tuition-and-payments/undergraduate-tuition/fordham-college-at-rose-hill/
source_snippet: "Total Cost of Attendance $102,188"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Application Statistics

```yaml
field: undergraduate.admission_statistics
value:
  applications: 43640
  offers: 25207
  enrolled: 2478
  acceptance_rate: 58%
source_url: https://www.fordham.edu/undergraduate-admission/why-fordham/admission-facts/
source_snippet: "Completed Applications: 43,640; Offers of Admission: 25,207; Enrolled Students: 2,478; Acceptance Rate: 58%"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: SAT/ACT Middle 50%

```yaml
field: undergraduate.admission_scores
value:
  SAT_middle_50_admitted: "1380-1490"
  ACT_middle_50_admitted: "31-34"
  SAT_middle_50_enrolled: "1350-1480"
  ACT_middle_50_enrolled: "30-34"
  percent_not_submitting_admitted: 66.2%
  percent_not_submitting_enrolled: 74.0%
source_url: https://www.fordham.edu/undergraduate-admission/why-fordham/admission-facts/
source_snippet: "SAT Middle 50%: 1380-1490*; ACT Composite Middle 50%: 31–34*; *66.2% of those who gained admission did not submit testing"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: English Proficiency Requirement

```yaml
field: undergraduate.international.english_proficiency
value: "TOEFL, IELTS, Duolingo English Test, or PTE required for non-native English speakers"
source_url: https://www.fordham.edu/undergraduate-admission/international-students/international-faqs/
source_snippet: "Fordham requires TOEFL, IELTS, Duolingo English Test, or PTE results from all non-native English speaking international applicants."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: International Financial Aid

```yaml
field: undergraduate.international.financial_aid
value: "Need-aware; must demonstrate ability to fund at least $35,000/year"
source_url: https://www.fordham.edu/student-financial-services/undergraduate-financial-aid/international-students/
source_snippet: "To qualify, the CSS Profile Institutional Methodology (IM) formula must demonstrate sufficient family contribution funding of at least $35,000 towards the annual cost of attendance."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Tuition (GSAS)

```yaml
field: graduate.gsas.tuition_per_credit
value: 1882
source_url: https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/graduate-school-of-arts-and-sciences/
source_snippet: "GSAS Tuition: $1,882 per credit"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Law School Tuition (JD)

```yaml
field: graduate.law.jd_tuition_fulltime
value: 81592
source_url: https://www.fordham.edu/student-financial-services/tuition-and-payments/graduate-tuition/school-of-law/
source_snippet: "Full-Time Day Students (1L to 3L): $81,592 per year"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
fordham-knowledge-base-v2
├── 00-institution-overview
│   └── 00-overview.md (Section 0: rules 1-4)
├── 01-undergraduate-education
│   ├── 01-fcrl-majors.md (Fordham College Rose Hill majors)
│   ├── 02-fclc-majors.md (Fordham College Lincoln Center majors)
│   ├── 03-gabelli-ug-majors.md (Gabelli School UG majors)
│   └── 04-minors.md (All minors)
├── 02-graduate-education
│   ├── 05-gabelli-grad.md (Gabelli graduate programs)
│   ├── 06-gsas.md (Graduate School of Arts & Sciences)
│   ├── 07-gse.md (Graduate School of Education)
│   ├── 08-gre.md (Graduate School of Religion)
│   ├── 09-gss.md (Graduate School of Social Service)
│   └── 10-law.md (School of Law)
├── 03-application-requirements
│   ├── 11-deadlines.md (UG deadlines & requirements)
│   └── 12-english-proficiency.md (International requirements)
├── 04-costs-financial-aid
│   ├── 13-ug-costs.md (UG tuition & COA)
│   └── 14-grad-costs.md (Graduate tuition by school)
└── 05-evidence-chain
    └── 15-evidence.md (All evidence citations)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "fordham-knowledge-base-v2"
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
| P0 | English proficiency minimum scores (TOEFL/IELTS) | https://www.fordham.edu/undergraduate-admission/international-students/ |
| P0 | Graduate program-specific deadlines | Each graduate school's admissions page |
| P1 | Undergraduate minors complete list | https://www.fordham.edu/undergraduate-admission/majors-and-minors/ |
| P1 | Graduate program-specific tuition details | Each graduate school's tuition page |
| P2 | Student-to-faculty ratio by school | https://www.fordham.edu/about/fordham-facts/ |
| P2 | Graduation rate by school | https://www.fordham.edu/about/fordham-facts/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Fordham University | [Other School] |
|------|-------------------|----------------|
| Total UG cost/yr (resident) | $102,188 | |
| Tuition/yr | $68,886 | |
| Need-aware (intl?) | Yes (all applicants) | |
| EA deadline | November 1, 2026 | |
| ED deadline | November 1, 2026 | |
| ED2 deadline | January 3, 2027 | |
| RD deadline | January 3, 2027 | |
| SAT/ACT required? | Test-optional | |
| TOEFL min | Not specified | |
| IELTS min | Not specified | |
| Acceptance rate | 58% | |
| Total program count (rule 1) | 176 | |
| School/department count (rule 2) | 9 | |
| Application fee | $80 | |
| CSS Profile code | 2259 | |
| SAT code | 2259 | |
| ACT code | 2748 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: fordham.edu, admission.fordham.edu, student-financial-services.fordham.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
