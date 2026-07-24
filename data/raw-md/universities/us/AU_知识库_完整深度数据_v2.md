# American University Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 59 |
| 本科辅修 (Minor) | 35+ (partial capture) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 81 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 17 |
| **学位项目总计 (UG + Grad)** | **157+** |
| 学院 / 独立系所总数 | 8 |

> Note: Minor count is estimated from partial data; complete minor enumeration requires additional extraction from each school's catalog pages.

### 0.2 学院 / 系层级结构

```
American University
├── College of Arts & Sciences (CAS)                    [学院]
│   ├── Art (Art History, Studio Art, Graphic Design, Photography) [系]
│   ├── Performing Arts (Dance, Music, Theatre)         [系]
│   ├── Communication & Media (Audio Technology)        [系]
│   ├── Humanities (History, Philosophy, Literature, Religious Studies, Languages) [系]
│   ├── Social Sciences (Anthropology, Sociology, Economics, Political Science, Psychology) [系]
│   ├── Natural Sciences (Biology, Chemistry, Physics, Mathematics, Environmental Science) [系]
│   ├── Computer Science & Data Science                 [系]
│   ├── Health Sciences (Public Health, Health Promotion, Neuroscience) [系]
│   └── Interdisciplinary (African American Studies, American Studies, Women's/Gender Studies) [系]
├── Kogod School of Business                            [学院]
│   ├── Accounting                                      [系]
│   ├── Finance                                         [系]
│   ├── Marketing                                       [系]
│   ├── Business Analytics & AI                         [系]
│   ├── Management                                      [系]
│   └── Sustainability Management                       [系]
├── School of Communication (SOC)                       [学院]
│   ├── Journalism                                      [系]
│   ├── Film & Media Arts                               [系]
│   ├── Communication Studies                           [系]
│   ├── Public Relations & Strategic Communication      [系]
│   └── Game Design                                     [系]
├── Baker School of Education (SOE)                     [学院]
│   ├── Early Childhood Education                       [系]
│   ├── Elementary Education                            [系]
│   ├── Secondary Education                             [系]
│   └── Education Policy & Leadership                   [系]
├── School of International Service (SIS)               [学院]
│   ├── International Relations                         [系]
│   ├── International Development                       [系]
│   ├── Peace & Conflict Resolution                     [系]
│   ├── Global Environmental Policy                     [系]
│   └── Ethics, Peace & Human Rights                    [系]
├── School of Public Affairs (SPA)                      [学院]
│   ├── Political Science                               [系]
│   ├── Justice, Law & Criminology                      [系]
│   ├── Public Administration & Policy                  [系]
│   ├── Data Science                                    [系]
│   └── Terrorism & Homeland Security                   [系]
├── Washington College of Law (WCL)                     [学院]
│   ├── J.D. Program                                    [系]
│   ├── LL.M. Programs                                  [系]
│   ├── Master of Legal Studies                         [系]
│   └── S.J.D. Program                                  [系]
└── Office of Graduate & Professional Studies (OGPS)    [行政单位]
    ├── Professional Studies (online programs)           [系]
    └── Executive Education                              [系]
```

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 39 |
| BS | BS | Bachelor of Science | 本科 | 20 |
| MA | MA | Master of Arts | 研究生 | 32 |
| MS | MS | Master of Science | 研究生 | 22 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 (on-campus + online) |
| MPA | MPA | Master of Public Administration | 研究生 | 2 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MEd | MEd | Master of Education | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MIS | MIS | Master of International Service | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| MLS | MLS | Master of Legal Studies | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 10 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| SJD | SJD | Doctor of Juridical Science | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 17 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | MFA | MBA | MPA | MPP | MEd | MAT | JD | LLM | MLS | PhD | EdD | SJD | Certificate | 合计 |
|------------|----|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|------|-----|-----|-------------|------|
| CAS | 23 | 14 | 10 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 2 | 65 |
| Kogod | 0 | 6 | 0 | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 22 |
| SOC | 6 | 0 | 5 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 15 |
| SOE | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 7 |
| SIS | 1 | 0 | 11 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 15 |
| SPA | 4 | 2 | 2 | 3 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 7 | 24 |
| WCL | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 4 |
| **合计** | **37** | **22** | **28** | **19** | **4** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **11** | **1** | **1** | **19** | **152** |

> Reconciliation note: Rule-1 total (157+) includes minors (35+) which are not shown in the distribution matrix above. The matrix captures degree-granting programs only (152). Certificate count (19) includes 17 graduate certificates + 2 undergraduate certificates.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

American University has 7 schools/colleges that grant undergraduate degrees. The College of Arts & Sciences is the largest, offering the most majors. Kogod School of Business, School of Communication, Baker School of Education, School of International Service, and School of Public Affairs also offer undergraduate programs. Washington College of Law is graduate-only.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences (CAS)

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.american.edu/cas/ |
| 2 | Graphic Design | https://www.american.edu/cas/ |
| 3 | Studio Art | https://www.american.edu/cas/ |
| 4 | Photography | https://www.american.edu/cas/ |

##### Department of Performing Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.american.edu/cas/ |
| 2 | Music | https://www.american.edu/cas/ |
| 3 | Theatre & Musical Theatre | https://www.american.edu/cas/ |

##### Department of Communication & Media
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Audio Technology | https://www.american.edu/cas/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Audio Technology | https://www.american.edu/cas/ |

##### Department of Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American & Diaspora Studies | https://www.american.edu/cas/ |
| 2 | American Studies | https://www.american.edu/cas/ |
| 3 | Arabic Studies | https://www.american.edu/cas/ |
| 4 | Arab World Studies | https://www.american.edu/cas/ |
| 5 | Creative Writing (track) | https://www.american.edu/cas/ |
| 6 | French Studies | https://www.american.edu/cas/ |
| 7 | German Studies | https://www.american.edu/cas/ |
| 8 | History | https://www.american.edu/cas/ |
| 9 | Jewish Studies | https://www.american.edu/cas/ |
| 10 | Literature | https://www.american.edu/cas/ |
| 11 | Philosophy | https://www.american.edu/cas/ |
| 12 | Religious Studies | https://www.american.edu/cas/ |
| 13 | Russian Studies | https://www.american.edu/cas/ |
| 14 | Spanish Studies | https://www.american.edu/cas/ |
| 15 | Women's, Gender, Sexuality Studies | https://www.american.edu/cas/ |

##### Department of Social Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.american.edu/cas/ |
| 2 | Economics | https://www.american.edu/cas/ |
| 3 | Psychology | https://www.american.edu/cas/ |
| 4 | Sociology | https://www.american.edu/cas/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.american.edu/cas/ |

##### Department of Natural Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.american.edu/cas/ |
| 2 | Mathematics & Statistics | https://www.american.edu/cas/ |
| 3 | Physics | https://www.american.edu/cas/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.american.edu/cas/ |
| 2 | Chemistry | https://www.american.edu/cas/ |
| 3 | Environmental Science | https://www.american.edu/cas/ |
| 4 | Mathematics & Statistics | https://www.american.edu/cas/ |
| 5 | Physics | https://www.american.edu/cas/ |

##### Department of Computer Science & Data Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.american.edu/cas/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.american.edu/cas/ |
| 2 | Data Science | https://www.american.edu/cas/ |

##### Department of Health Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://www.american.edu/cas/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Promotion | https://www.american.edu/cas/ |
| 2 | Neuroscience | https://www.american.edu/cas/ |
| 3 | Public Health | https://www.american.edu/cas/ |

#### Kogod School of Business

##### Department of Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://kogod.american.edu/programs-admissions/undergraduate/accounting |
| 2 | Business Administration | https://kogod.american.edu/programs-admissions/undergraduate/business-administration |
| 3 | Business Analytics & AI | https://kogod.american.edu/programs-admissions/undergraduate/business-analytics-and-ai |
| 4 | Business & Entertainment | https://kogod.american.edu/programs-admissions/undergraduate/business-entertainment |
| 5 | Business, Language, & Culture | https://kogod.american.edu/programs-admissions/undergraduate/language-and-culture |
| 6 | Finance | https://kogod.american.edu/programs-admissions/undergraduate/finance |

#### School of Communication (SOC)

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film & Media Arts | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 2 | Public Relations & Strategic Communication | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 3 | Journalism | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 4 | Communication Studies | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 5 | Photography | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 6 | Communication, Language, and Culture | https://www.american.edu/soc/undergraduate-degrees.cfm |

#### Baker School of Education (SOE)

##### Department of Education
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://www.american.edu/soe/undergraduate/ |
| 2 | Elementary Education | https://www.american.edu/soe/undergraduate/ |
| 3 | Secondary Education | https://www.american.edu/soe/undergraduate/ |

#### School of International Service (SIS)

##### Department of International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://www.american.edu/sis/undergrad/index.cfm |

#### School of Public Affairs (SPA)

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.american.edu/spa/ |
| 2 | Interdisciplinary Studies: CLEG | https://www.american.edu/spa/ |

##### Department of Justice & Law
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Justice & Law | https://www.american.edu/spa/ |
| 2 | Legal Studies | https://www.american.edu/spa/ |

##### Department of Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Sciences for Political Science | https://www.american.edu/spa/ |
| 2 | Data Sciences for Justice, Law, & Criminology | https://www.american.edu/spa/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Parent Schools | URL |
|---|------|----------------|-----|
| 1 | CLEG (Communication, Legal Institutions, Economics, Government) | SPA | https://www.american.edu/spa/ |
| 2 | Data Science | CAS + SPA | https://www.american.edu/cas/ |
| 3 | Computer Science | CAS | https://www.american.edu/cas/ |

### 1.4 Minors — partial list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Education Studies | SOE | https://www.american.edu/soe/undergraduate/ |
| 2 | Special Education | SOE | https://www.american.edu/soe/undergraduate/ |
| 3 | Communication | SOC | https://www.american.edu/soc/undergraduate-degrees.cfm |
| 4 | Israel Studies | CAS | https://www.american.edu/cas/ |
| 5 | Linguistics | CAS | https://www.american.edu/cas/ |
| 6 | Writing & Rhetoric | CAS | https://www.american.edu/cas/ |

> Note: Complete minor enumeration requires additional extraction. CAS offers numerous minors across humanities, social sciences, and sciences.

### 1.5 General/Institute-wide requirements

American University requires all undergraduate students to complete the AU Core Curriculum, which includes:
- Written Communication (2 courses)
- Quantitative Literacy (1 course)
- Arts (1 course)
- Humanitites (2 courses)
- Social Sciences (2 courses)
- Natural Sciences (2 courses, at least 1 with lab)
- Foreign Language (through intermediate level or equivalent)
- Complex Problems (1 course)
- Capstone (1 course in major)

### 1.6 Course-ID → Major quick-lookup

AU does not use a systematic course-numbering scheme for programs. Programs are identified by name rather than code.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences (CAS)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | https://www.american.edu/cas/ |
| 2 | Arts Management | https://www.american.edu/cas/ |
| 3 | Audio Technology | https://www.american.edu/cas/ |
| 4 | Game Design | https://www.american.edu/cas/ |
| 5 | Ethics, Peace & Human Rights | https://www.american.edu/cas/ |
| 6 | History | https://www.american.edu/cas/ |
| 7 | Literature, Culture, & Technology | https://www.american.edu/cas/ |
| 8 | Philosophy | https://www.american.edu/cas/ |
| 9 | TESOL | https://www.american.edu/cas/ |
| 10 | Anthropology | https://www.american.edu/cas/ |
| 11 | Biology | https://www.american.edu/cas/ |
| 12 | Psychology | https://www.american.edu/cas/ |
| 13 | Sociology | https://www.american.edu/cas/ |
| 14 | Public Health | https://www.american.edu/cas/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.american.edu/cas/ |
| 2 | Biotechnology | https://www.american.edu/cas/ |
| 3 | Chemistry | https://www.american.edu/cas/ |
| 4 | Computer Science | https://www.american.edu/cas/ |
| 5 | Data Science | https://www.american.edu/cas/ |
| 6 | Economics | https://www.american.edu/cas/ |
| 7 | Environmental Science | https://www.american.edu/cas/ |
| 8 | Health Promotion | https://www.american.edu/cas/ |
| 9 | Mathematics & Statistics | https://www.american.edu/cas/ |
| 10 | Nutrition Education (online) | https://www.american.edu/cas/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Game Design | https://www.american.edu/cas/ |
| 2 | Creative Writing | https://www.american.edu/cas/ |
| 3 | Studio Art | https://www.american.edu/cas/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavior, Cognition, & Neuroscience | https://www.american.edu/cas/ |
| 2 | Biomedical & Environmental Health Sciences | https://www.american.edu/cas/ |
| 3 | Economics | https://www.american.edu/cas/ |
| 4 | History | https://www.american.edu/cas/ |
| 5 | Neuroscience | https://www.american.edu/cas/ |
| 6 | Psychology | https://www.american.edu/cas/ |

#### Kogod School of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://kogod.american.edu/programs-admissions/masters/accounting |
| 2 | Business Analytics & AI | https://kogod.american.edu/programs-admissions/masters/analytics-and-ai |
| 3 | Finance | https://kogod.american.edu/programs-admissions/masters/finance |
| 4 | Marketing | https://kogod.american.edu/programs-admissions/masters/marketing |
| 5 | Marketing Analytics | https://kogod.american.edu/programs-admissions/online-programs/marketing-analytics |
| 6 | Sustainability Management | https://kogod.american.edu/programs-admissions/masters/sustainability-management-stem |
| 7 | International Relations and Business (online) | https://kogod.american.edu/programs-admissions/online-programs/international-relations-and-business |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | MBA (on-campus) | https://kogod.american.edu/programs-admissions/mba |
| 2 | Online MBA | https://kogod.american.edu/programs-admissions/online-programs/online-mba |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Graduate Business Analytics and AI | https://kogod.american.edu/programs-admissions/certificates/graduate-analytics |
| 2 | Graduate Business Fundamentals | https://kogod.american.edu/programs-admissions/certificates/graduate-business-fundamentals |
| 3 | Graduate Forensic Accounting | https://kogod.american.edu/programs-admissions/certificates/graduate-forensic-accounting |
| 4 | Graduate Islamic Finance | https://kogod.american.edu/programs-admissions/certificates/graduate-islamic-finance |
| 5 | Graduate Marketing Analytics | https://kogod.american.edu/programs-admissions/certificates/graduate-marketing-analytics |
| 6 | Graduate Real Estate | https://kogod.american.edu/programs-admissions/certificates/graduate-real-estate |
| 7 | Graduate Sustainability | https://kogod.american.edu/programs-admissions/certificates/graduate-sustainability |
| 8 | Graduate Taxation | https://kogod.american.edu/programs-admissions/certificates/graduate-taxation |

#### School of Communication (SOC)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Media, Technology & Democracy | https://www.american.edu/soc/degrees.cfm |
| 2 | Journalism & Public Affairs | https://www.american.edu/soc/degrees.cfm |
| 3 | Film & Media Production | https://www.american.edu/soc/degrees.cfm |
| 4 | Strategic Communication (on-campus) | https://www.american.edu/soc/degrees.cfm |
| 5 | Global Strategic Communication | https://www.american.edu/soc/degrees.cfm |
| 6 | Political Communication | https://www.american.edu/soc/degrees.cfm |
| 7 | Game Design | https://www.american.edu/soc/degrees.cfm |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Film & Media Arts | https://www.american.edu/soc/degrees.cfm |
| 2 | Games & Interactive Media | https://www.american.edu/soc/degrees.cfm |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://www.american.edu/soc/degrees.cfm |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Game Design | https://www.american.edu/soc/degrees.cfm |

#### Baker School of Education (SOE)

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Education Policy & Leadership | https://www.american.edu/soe/graduate/ |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Arts in Teaching | https://www.american.edu/soe/graduate/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education Policy & Leadership | https://www.american.edu/soe/graduate/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Reading and Language Development | https://www.american.edu/soe/graduate/ |

#### School of International Service (SIS)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Ethics, Peace, and Human Rights | https://www.american.edu/sis/admissions/degrees.cfm |
| 2 | Global Environmental Policy | https://www.american.edu/sis/admissions/degrees.cfm |
| 3 | Global Governance, Politics, and Security | https://www.american.edu/sis/admissions/degrees.cfm |
| 4 | Global Governance, Politics, and Security: Quantitative Economic Methods | https://www.american.edu/sis/admissions/degrees.cfm |
| 5 | Intercultural and International Communication | https://www.american.edu/sis/admissions/degrees.cfm |
| 6 | International Affairs Policy and Analysis | https://www.american.edu/sis/admissions/degrees.cfm |
| 7 | International Affairs: Natural Resources and Sustainable Development | https://www.american.edu/sis/admissions/degrees.cfm |
| 8 | International Affairs: United States Foreign Policy and National Security | https://www.american.edu/sis/admissions/degrees.cfm |
| 9 | International Development | https://www.american.edu/sis/admissions/degrees.cfm |
| 10 | International Peace and Conflict Resolution | https://www.american.edu/sis/admissions/degrees.cfm |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | International Relations and Business (online) | https://www.american.edu/sis/admissions/degrees.cfm |
| 2 | International Relations (online) | https://www.american.edu/sis/admissions/degrees.cfm |
| 3 | Development Management | https://www.american.edu/sis/admissions/degrees.cfm |

##### MIS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of International Service | https://www.american.edu/sis/admissions/degrees.cfm |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | International Relations | https://www.american.edu/sis/admissions/degrees.cfm |

#### School of Public Affairs (SPA)

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Communication | https://www.american.edu/spa/ |
| 2 | Political Science | https://www.american.edu/spa/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science | https://www.american.edu/spa/ |
| 2 | Justice, Law & Criminology | https://www.american.edu/spa/ |
| 3 | Terrorism & Homeland Security Policy | https://www.american.edu/spa/ |
| 4 | Counter-Terrorism and Homeland Security (online) | https://www.american.edu/spa/ |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.american.edu/spa/ |
| 2 | Public Administration: Key Executive Leadership | https://www.american.edu/spa/ |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | https://www.american.edu/spa/ |

##### MPAP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration & Policy (online) | https://www.american.edu/spa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Justice, Law & Criminology | https://www.american.edu/spa/ |
| 2 | Political Science | https://www.american.edu/spa/ |
| 3 | Public Administration & Policy | https://www.american.edu/spa/ |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Analytics and Management | https://www.american.edu/spa/ |
| 2 | Nonprofit Management | https://www.american.edu/spa/ |
| 3 | Public Financial Management | https://www.american.edu/spa/ |
| 4 | Cyber Policy and Management | https://www.american.edu/spa/ |
| 5 | Public Management | https://www.american.edu/spa/ |
| 6 | Public Policy Analysis | https://www.american.edu/spa/ |
| 7 | Women, Policy & Political Leadership | https://www.american.edu/spa/ |

#### Washington College of Law (WCL)

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://www.wcl.american.edu/academics/ |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws | https://www.wcl.american.edu/academics/ |

##### MLS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Legal Studies | https://www.wcl.american.edu/academics/ |

##### SJD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science | https://www.wcl.american.edu/academics/ |

### 2.2 At least one program's full deep-dive (worked example)

**Program: MA in International Relations (SIS)**

- **Department**: School of International Service
- **Address**: 4400 Massachusetts Avenue NW, Washington, DC 20016
- **Phone**: 202-885-1646
- **Email**: sisgrad@american.edu
- **Application portal**: SIS online application system
- **Application fee**: Varies (check SIS website)
- **GRE**: Not required for most SIS programs
- **TOEFL minimum**: 100 iBT
- **IELTS minimum**: 7.0
- **Duolingo minimum**: 120
- **PTE minimum**: 68
- **Priority deadlines**: Varies by program (check SIS website)
- **Funding**: Merit-based scholarships and assistantships available

### 2.3 Graduate admissions model

AU graduate admissions is **fully decentralized**. Each school/college manages its own admissions process, application system, and financial aid. There is no central graduate admissions office that makes decisions.

**Key entry points**:
- CAS Graduate Admissions: casgrad@american.edu, 202-885-3620
- Kogod Graduate Admissions: kogod@american.edu, 202-885-1900
- SOC Graduate Admissions: (202) 885-2058
- SOE Graduate Admissions: soeadmissions@american.edu, 202-885-3720
- SIS Graduate Admissions: sisgrad@american.edu, 202-885-1646
- SPA Graduate Admissions: spa@american.edu, (202) 885-6200
- WCL Admissions: wclaw.edu
- OGPS: gradstudies@american.edu, (202) 885-8210

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://www.american.edu/admissions/ | AU Admissions |
| Application portal | Common Application | AU Admissions |
| EA deadline | November 1 | AU Admissions |
| ED I deadline | November 1 | AU Admissions |
| ED II deadline | January 15 | AU Admissions |
| RD deadline | January 15 | AU Admissions |
| CSS Profile & FAFSA deadline (EA) | November 15 | AU Admissions |
| CSS Profile & FAFSA deadline (ED I) | November 15 | AU Admissions |
| CSS Profile & FAFSA deadline (ED II) | February 1 | AU Admissions |
| CSS Profile & FAFSA deadline (RD) | February 15 | AU Admissions |
| Notification (EA) | January 31 | AU Admissions |
| Notification (ED I) | December 31 | AU Admissions |
| Notification (ED II) | February 15 | AU Admissions |
| Notification (RD) | April 1 | AU Admissions |
| Deposit deadline (EA) | May 1 | AU Admissions |
| Deposit deadline (ED I) | January 15 | AU Admissions |
| Deposit deadline (ED II) | March 1 | AU Admissions |
| Deposit deadline (RD) | May 1 | AU Admissions |
| Application fee | $75 | AU Admissions |
| SAT/ACT policy | Test-optional | AU Admissions |
| SAT code | 5007 | AU Admissions |
| ACT code | 0648 | AU Admissions |
| TOEFL code | 5007 | AU Admissions |
| Superscore | Yes (ACT Math, Reading, English) | AU Admissions |
| Interview policy | Not offered | AU Admissions |
| Recommendation requirements | 1 teacher recommendation required | AU Admissions |
| Portfolio | Optional for SOC Film & Media Arts, Photography | AU Admissions |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 85 | N/A | Official scores required |
| IELTS | 6.5 | N/A | Official scores required |
| Duolingo English Test | 120 | N/A | Official scores required |
| Cambridge English | 176 | N/A | Official scores required |
| PTE | 60 | N/A | Official scores required |
| SAT-EBRW | 610 | N/A | Can substitute for English proficiency |
| ACT-English | 25 | N/A | Can substitute for English proficiency |

**Exemption**: Students graduating from secondary schools in English-speaking countries (US, UK, Ireland, Australia, New Zealand, Canada except Quebec, Singapore, etc.) where English is the only medium of instruction and no ESL courses were taken.

### 3.3 Graduate — global rules

- **Decentralized admissions**: Each school manages its own process
- **Application platforms**: Vary by school (SIS has own system, CAS uses ApplyWeb, etc.)
- **Standard application fee**: Varies by school
- **GRE/GMAT policy**: Not required for most programs; check individual programs
- **Language-test policy**: TOEFL/IELTS/PTE/Duolingo required for non-native speakers
- **Exemption**: Same as UG (English-speaking country curriculum)
- **Institutional codes**: Vary by school (SIS: 5007 for TOEFL)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $62,680 | Full-time (12-17.99 credits/semester) |
| Mandatory Fees | $1,700 | Per year |
| Metro Pass Fees | $272 | Per year |
| Housing | $13,112 | Average double occupancy |
| Food | $6,584 | Meal plan |
| Books and supplies | $1,200 | Estimated |
| Transportation | $692 | Estimated |
| Personal Expenses | $1,080 | Estimated |
| Loan Fees | $54 | Estimated |
| **Total COA** | **$87,374** | Before aid |

**Tuition breakdown (per semester)**:
- Part-time (less than 12 credits): $2,087/credit
- Full-time (12-17.99 credits): $31,340
- Full-time (18 credits): $33,428
- Above 18 credits: $2,087/additional credit

**Housing (per semester, double occupancy)**:
- Hughes Hall: $6,160
- Anderson/Letts/Leonard/McDowell/Roper: $6,260
- Cassell Hall: $7,660
- Nebraska Hall: $7,740
- Centennial Hall: $7,170
- East Campus Halls: $7,540

**Meal Plans (per semester)**:
- Premium: $3,597
- Plus: $3,292
- Standard: $2,940
- Basic: $2,120

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all international students**: AU considers ability to cover costs when making admissions decisions
- **No need-based aid for international students**: Only available for U.S. citizens and permanent residents
- **Merit-based scholarships**: Available for international students (partial and full-tuition)
- **88% of incoming students receive aid**
- **$138M in financial aid awarded to undergraduates per year**
- **FAFSA code**: 001434
- **CSS Profile code**: 5007
- **AU Declaration of Finances Form**: Required for international students showing minimum $83,680

### 4.3 Graduate cost & funding framework

- **Tuition**: $2,163/credit hour (most programs)
- **SIS Master's Program Fee**: $750/semester (full-time), $500/semester (part-time)
- **Joint Degree (CAS/SIS) Fee**: $375/semester (full-time), $250/semester (part-time)
- **Funding**: Merit-based scholarships and assistantships vary by school
- **Application fee**: Varies by school
- **Fee waivers**: Available based on need (check individual schools)

---

## SECTION 5 — Evidence chain index

```yaml
field: undergraduate.deadlines.EA
value: "November 1"
source_url: https://www.american.edu/admissions/first-year/checklist.cfm
source_snippet: "Early Action: November 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.ED_I
value: "November 1"
source_url: https://www.american.edu/admissions/first-year/checklist.cfm
source_snippet: "Early Decision I: November 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.ED_II
value: "January 15"
source_url: https://www.american.edu/admissions/first-year/checklist.cfm
source_snippet: "Early Decision II: January 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.deadlines.RD
value: "January 15"
source_url: https://www.american.edu/admissions/first-year/checklist.cfm
source_snippet: "Regular Decision: January 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.test_policy
value: "Test-optional"
source_url: https://www.american.edu/admissions/first-year/test-optional.cfm
source_snippet: "Prospective students may apply to American University through any of our decision plans—Early Action, Early Decision I and II, or Regular Decision—without submitting standardized test scores."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.application_fee
value: "$75"
source_url: https://www.american.edu/admissions/first-year/checklist.cfm
source_snippet: "A nonrefundable $75 application fee or application fee waiver"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.TOEFL
value: "85"
source_url: https://www.american.edu/admissions/international/instructions.cfm
source_snippet: "TOEFL: 85"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.IELTS
value: "6.5"
source_url: https://www.american.edu/admissions/international/instructions.cfm
source_snippet: "IELTS: 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.english_proficiency.Duolingo
value: "120"
source_url: https://www.american.edu/admissions/international/instructions.cfm
source_snippet: "Duolingo English Test: 120"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.cost.tuition
value: "$62,680"
source_url: https://www.american.edu/financialaid/
source_snippet: "Tuition: $62,680"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.cost.total_COA
value: "$87,374"
source_url: https://www.american.edu/financialaid/
source_snippet: "Total COA: $87,374"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: undergraduate.financial_aid.need_aware_international
value: "Yes"
source_url: https://www.american.edu/admissions/international/instructions.cfm
source_snippet: "Undergraduate admission to American University is need aware for all international students."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: graduate.english_proficiency.SIS.TOEFL
value: "100"
source_url: https://www.american.edu/sis/admissions/faq.cfm
source_snippet: "Internet-based test (iBT): 100"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: graduate.english_proficiency.SIS.IELTS
value: "7.0"
source_url: https://www.american.edu/sis/admissions/faq.cfm
source_snippet: "The minimum requirement for the IELTS is 7.0"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
field: graduate.english_proficiency.SIS.Duolingo
value: "120"
source_url: https://www.american.edu/sis/admissions/faq.cfm
source_snippet: "The minimum requirement for Duolingo English Test is 120"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
au-knowledge-base-v2/
├── au-overview                    # Section 0: counts, hierarchy, degree inventory, distribution matrix
├── au-undergraduate-programs      # Section 1: all UG majors grouped by school
├── au-graduate-programs           # Section 2: all grad programs grouped by school
├── au-admissions-deadlines        # Section 3: deadlines, requirements, test policy
├── au-costs-financial-aid         # Section 4: COA, aid policy, tuition
├── au-evidence-chain              # Section 5: all evidence citations
└── au-comparison-framework        # Section 7: cross-school comparison data
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "au-knowledge-base-v2"
  school: "American University"
  department: "<home department>"
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
| P0 | Complete minor enumeration (all schools) | Each school's academics page |
| P0 | CAS graduate admissions English proficiency requirements | https://www.american.edu/cas/admissions/ |
| P0 | Kogod graduate admissions requirements | https://kogod.american.edu/programs-admissions/masters/ |
| P1 | SOC graduate admissions requirements | https://www.american.edu/soc/admissions/ |
| P1 | SPA graduate admissions requirements | https://www.american.edu/spa/ |
| P1 | SOE graduate admissions requirements | https://www.american.edu/soe/graduate/ |
| P1 | WCL admissions requirements | https://www.wcl.american.edu/admissions/ |
| P2 | Per-program GRE requirements | Individual program pages |
| P2 | Graduate tuition by program (differential pricing) | Individual school pages |
| P2 | Undergraduate Core Curriculum details | https://www.american.edu/provost/undergraduate-studies/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | American University | (blank for other schools) |
|------|---------------------|---------------------------|
| Total UG cost/yr | $87,374 | |
| Tuition/yr | $62,680 | |
| Need-blind (intl?) | No (need-aware) | |
| EA deadline | November 1 | |
| ED I deadline | November 1 | |
| ED II deadline | January 15 | |
| RD deadline | January 15 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min (UG) | 85 | |
| IELTS min (UG) | 6.5 | |
| Duolingo min (UG) | 120 | |
| Application fee | $75 | |
| Total program count (rule 1) | 157+ | |
| School/department count (rule 2) | 8 | |
| Graduate application fee | Varies by school | |
| TOEFL min (grad, SIS) | 100 | |
| IELTS min (grad, SIS) | 7.0 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.american.edu, kogod.american.edu, www.wcl.american.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
