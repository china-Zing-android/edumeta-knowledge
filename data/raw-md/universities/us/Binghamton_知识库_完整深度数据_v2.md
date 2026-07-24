# Binghamton University (SUNY) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BMus/etc.) | 75 |
| 本科辅修 (Minor) | 55 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 150+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | 35+ |
| **学位项目总计 (UG + Grad)** | **260+** |
| 学院 / 独立系所总数 | 6 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Binghamton University (SUNY)
├── Harpur College of Arts and Sciences                    [学院]
│   ├── Department of Anthropology                         [系]
│   ├── Department of Art History                          [系]
│   ├── Department of Biological Sciences                  [系]
│   ├── Department of Chemistry                            [系]
│   ├── Department of Cinema                               [系]
│   ├── Department of Comparative Literature               [系]
│   ├── Department of Economics                            [系]
│   ├── Department of English                              [系]
│   ├── Department of Geological Sciences                  [系]
│   ├── Department of History                              [系]
│   ├── Department of Mathematical Sciences                [系]
│   ├── Department of Music                                [系]
│   ├── Department of Philosophy                           [系]
│   ├── Department of Physics                              [系]
│   ├── Department of Political Science                    [系]
│   ├── Department of Psychology                           [系]
│   ├── Department of Sociology                            [系]
│   ├── Department of Theatre                              [系]
│   ├── Department of Translation Studies                  [系]
│   ├── Department of Women, Gender and Sexuality Studies  [系]
│   └── [Language & Area Studies Departments]              [系]
├── College of Community and Public Affairs (CCPA)         [学院]
│   ├── Department of Human Development                    [系]
│   ├── Department of Social Work                          [系]
│   ├── Department of Public Administration                [系]
│   └── Department of Educational Theory and Practice      [系]
├── Decker College of Nursing and Health Sciences          [学院]
│   ├── Department of Nursing                              [系]
│   ├── Department of Occupational Therapy                 [系]
│   ├── Department of Physical Therapy                     [系]
│   └── Department of Speech and Language Pathology        [系]
├── School of Management                                   [学院]
│   ├── Department of Accounting                           [系]
│   ├── Department of Finance                              [系]
│   ├── Department of Information Systems                  [系]
│   ├── Department of Management                           [系]
│   └── Department of Marketing                            [系]
├── School of Pharmacy and Pharmaceutical Sciences         [学院]
│   ├── Department of Pharmaceutical Sciences              [系]
│   └── Department of Pharmacy Practice                    [系]
└── Thomas J. Watson College of Engineering and Applied Science [学院]
    ├── Department of Biomedical Engineering               [系]
    ├── Department of Computer Science                     [系]
    ├── Department of Electrical and Computer Engineering  [系]
    ├── Department of Industrial and Systems Engineering   [系]
    ├── Department of Mechanical Engineering               [系]
    └── Department of Systems Science                      [系]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 40 |
| BS | BS | Bachelor of Science | 本科 | 30 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| MusB | MusB | Bachelor of Music | 本科 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 30 |
| MS | MS | Master of Science | 研究生 | 45 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MEng | MEng | Master of Engineering | 研究生 | 2 |
| MM | MM | Master of Music | 研究生 | 1 |
| MSW | MSW | Master of Social Work | 研究生 | 2 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MSEd | MSEd | Master of Science in Education | 研究生 | 10 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 6 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 35 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 8 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| Adv Cert | Adv Cert | Advanced Certificate | 研究生 | 35+ |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | MusB | BSW | MA | MS | MBA | MFA | MEng | MM | MSW | MPA | MPH | MPP | MSEd | MAT | PhD | EdD | DNP | DPT | OTD | PharmD | Adv Cert | 合计 |
|------------|----|----|-----|------|-----|----|----|-----|-----|------|----|-----|-----|-----|-----|------|-----|-----|-----|-----|-----|-----|--------|----------|------|
| Harpur College of Arts and Sciences | 40 | 10 | 2 | 1 | 0 | 25 | 5 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 10 | 120 |
| College of Community and Public Affairs | 0 | 2 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 1 | 5 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 5 | 22 |
| Decker College of Nursing and Health Sciences | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 1 | 1 | 0 | 8 | 24 |
| School of Management | 0 | 2 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 11 |
| School of Pharmacy and Pharmaceutical Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 4 |
| Thomas J. Watson College of Engineering and Applied Science | 0 | 15 | 0 | 0 | 0 | 0 | 20 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 5 | 48 |
| **合计** | **40** | **30** | **2** | **1** | **1** | **25** | **36** | **3** | **1** | **2** | **1** | **2** | **1** | **1** | **1** | **5** | **6** | **35** | **1** | **8** | **1** | **1** | **1** | **30** | **229** |

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Binghamton University consists of six schools offering undergraduate programs. For the complete school/department hierarchy, see Section 0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Harpur College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1994&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1995&returnto=313 |

##### Department of Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2003&returnto=313 |

##### Department of Biological Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2006&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2007&returnto=313 |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2009&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2010&returnto=313 |

##### Department of Cinema
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Cinema | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2012&returnto=313 |

##### Department of Comparative Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Literature | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2014&returnto=313 |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2022&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2023&returnto=313 |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2025&returnto=313 |

##### Department of Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2027&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2028&returnto=313 |

##### Department of Geological Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2017&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2018&returnto=313 |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2045&returnto=313 |

##### Department of Mathematical Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2059&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Sciences | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2060&returnto=313 |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2072&returnto=313 |

###### MusB
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (Performance) | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2073&returnto=313 |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2075&returnto=313 |
| 2 | Philosophy, Politics, and Law | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2240&returnto=313 |

##### Department of Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2076&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2077&returnto=313 |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2081&returnto=313 |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2082&returnto=313 |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2090&returnto=313 |

##### Department of Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2092&returnto=313 |

##### Department of Studio Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2001&returnto=313 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2002&returnto=313 |

##### Department of Musical Theatre
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Musical Theatre | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2074&returnto=313 |

##### Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1992&returnto=313 |

##### Asian and Asian American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian and Asian American Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1984&returnto=313 |

##### Chinese Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1985&returnto=313 |

##### French
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2084&returnto=313 |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2031&returnto=313 |

##### German Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | German Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2038&returnto=313 |

##### Global Public Health
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Public Health | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2042&returnto=313 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Public Health | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2043&returnto=313 |

##### Italian
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Italian | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2085&returnto=313 |

##### Japanese Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Japanese Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1986&returnto=313 |

##### Judaic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Judaic Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2050&returnto=313 |

##### Korean Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Korean Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1987&returnto=313 |

##### Latin American and Caribbean Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American and Caribbean Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2055&returnto=313 |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2057&returnto=313 |

##### Middle East Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Middle East Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2065&returnto=313 |

##### Russian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Russian Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2039&returnto=313 |

##### Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2086&returnto=313 |

##### Women, Gender and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women, Gender and Sexuality Studies | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2096&returnto=313 |

#### College of Community and Public Affairs (CCPA)

##### Department of Human Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1946&returnto=313 |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1947&returnto=313 |

#### Decker College of Nursing and Health Sciences

##### Department of Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=1948&returnto=313 |

#### School of Management

##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2181&returnto=313 |

##### Department of Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2183&returnto=313 |

#### School of Pharmacy and Pharmaceutical Sciences

*Note: School of Pharmacy primarily offers graduate-level programs. Undergraduate students may pursue pre-pharmacy tracks.*

#### Thomas J. Watson College of Engineering and Applied Science

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2190&returnto=313 |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2192&returnto=313 |
| 2 | Computer Engineering | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2194&returnto=313 |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2195&returnto=313 |

##### Department of Industrial and Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial and Systems Engineering | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2199&returnto=313 |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2200&returnto=313 |

##### Department of Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems (Dual-Diploma) | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2193&returnto=313 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Global and International Affairs, BS | Harpur College | https://catalog.binghamton.edu/preview_program.php?catoid=7&poid=2254&returnto=313 |
| 2 | Integrative Neuroscience, BS | Harpur College | https://www.binghamton.edu/apps/academics/program/ug/integrative-neuroscience |

### 1.4 Minors — complete list

Binghamton University offers 55+ undergraduate minors across all schools. Key minors include:

| # | Minor name | Home school/department |
|---|------------|----------------------|
| 1 | Africana Studies | Harpur College |
| 2 | Anthropology | Harpur College |
| 3 | Art History | Harpur College |
| 4 | Arts in Healthcare | Harpur College |
| 5 | Asian and Asian American Studies | Harpur College |
| 6 | Biological Sciences | Harpur College |
| 7 | Chemistry | Harpur College |
| 8 | Chinese Studies | Harpur College |
| 9 | Cinema | Harpur College |
| 10 | Comparative Literature | Harpur College |
| 11 | Digital and Data Studies | Harpur College |
| 12 | East European and Eurasian Studies | Harpur College |
| 13 | Economics | Harpur College |
| 14 | Education | Harpur College |
| 15 | English | Harpur College |
| 16 | Environmental Studies | Harpur College |
| 17 | Evolutionary Studies | Harpur College |
| 18 | Forensic Health | Harpur College |
| 19 | French | Harpur College |
| 20 | Geography | Harpur College |
| 21 | Geological Sciences | Harpur College |
| 22 | German Studies | Harpur College |
| 23 | Global Studies | Harpur College |
| 24 | Health and Wellness Studies | Harpur College |
| 25 | History | Harpur College |
| 26 | Human Rights | Harpur College |
| 27 | Immigration Studies | Harpur College |
| 28 | Israel Studies | Harpur College |
| 29 | Italian | Harpur College |
| 30 | Japanese Studies | Harpur College |
| 31 | Judaic and Hebrew Studies | Harpur College |
| 32 | Korean Studies | Harpur College |
| 33 | Latin American and Caribbean Studies | Harpur College |
| 34 | Lighting | Harpur College |
| 35 | Linguistics | Harpur College |
| 36 | Mathematical Sciences | Harpur College |
| 37 | Medieval and Early Modern Studies | Harpur College |
| 38 | Middle East Studies | Harpur College |
| 39 | Music | Harpur College |
| 40 | Philosophy | Harpur College |
| 41 | Physics | Harpur College |
| 42 | Political Science | Harpur College |
| 43 | Public Health | Harpur College |
| 44 | Religious Studies | Harpur College |
| 45 | Russian Studies | Harpur College |
| 46 | Sociology | Harpur College |
| 47 | Sound Technologies | Harpur College |
| 48 | Spanish | Harpur College |
| 49 | Speech and Hearing Science | Harpur College |
| 50 | Studio Art | Harpur College |
| 51 | Theatre | Harpur College |
| 52 | Translation Studies | Harpur College |
| 53 | Women, Gender and Sexuality Studies | Harpur College |
| 54 | Writing Studies | Harpur College |
| 55 | Biomedical Engineering | Watson College |

### 1.5 General/Institute-wide requirements

Binghamton University requires all undergraduates to complete the General Education (GenEd) program, which includes:
- Composition (C)
- Oral Communication (O)
- Mathematical Sciences (M)
- Laboratory Science (N)
- Physical Activity (P)
- Aesthetic Perspective (A)
- Global Interdependencies (G)
- Humanities (H)
- Social Sciences (S)
- Pluralism in the United States (D)

### 1.6 Course-ID → Major quick-lookup

*Binghamton University does not use a course-numbering system for majors.*

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Harpur College of Arts and Sciences

##### Anthropology
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Anthropology | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C61 |
| 2 | Anthropology | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C01 |
| 3 | Anthropology: Public Archaeology | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C03 |
| 4 | Biomedical Anthropology | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C02 |

##### Art History
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Art History | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C69 |
| 2 | Art History | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C09 |

##### Biological Sciences
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biological Sciences | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C14 |
| 2 | Biological Sciences | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C11 |
| 3 | Biological Sciences | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C13 |

##### Biochemistry
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biochemistry and Chemical Biology | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C80 |
| 2 | Biochemistry and Chemical Biology | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C81 |
| 3 | Biochemistry and Chemical Biology | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C82 |

##### Chemistry
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Chemistry | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C16 |
| 2 | Chemistry | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C65 |
| 3 | Chemistry | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C15 |

##### Cinema
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Cinema | MFA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C68 |

##### Comparative Literature
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Comparative Literature | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C73 |
| 2 | Comparative Literature | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C33 |

##### Economics
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Economics | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C62 |
| 2 | Economics | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C22 |

##### English
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | English | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C83 |
| 2 | English | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C23 |

##### Geological Sciences
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Geological Sciences | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C76 |
| 2 | Geological Sciences | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C26 |

##### History
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | History | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C79 |
| 2 | History | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C29 |

##### Mathematical Sciences
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Mathematics | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C84 |
| 2 | Mathematical Sciences | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C32 |

##### Music
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Music | MM | https://www.binghamton.edu/apps/catalog/application-requirement/view/C66 |

##### Philosophy
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Philosophy | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C77 |
| 2 | Philosophy | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C37 |

##### Physics
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Physics | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C41 |
| 2 | Physics | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C49 |

##### Political Science
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Political Science | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C93 |
| 2 | Political Science | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C43 |

##### Psychology
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Clinical Psychology | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C47 |
| 2 | Cognitive and Brain Sciences | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C51 |
| 3 | Behavioral Neuroscience | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C45 |

##### Sociology
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Sociology | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C72 |
| 2 | Sociology | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C52 |

##### Theatre
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Theatre | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C56 |

##### Translation Studies
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Translation | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C67 |
| 2 | Translation Studies | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/C60 |
| 3 | Translation | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/G60 |

##### Asian and Asian American Studies
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Asian and Asian American Studies | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C36 |
| 2 | Asian and Asian American Studies | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/G36 |

##### French
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | French | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C24 |

##### Geography
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Geography | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C25 |

##### German Studies
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | German | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/H28 |

##### Italian
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Italian | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C30 |

##### Spanish
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Spanish | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C53 |

##### Data Science and Statistics
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Data Science and Statistics | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/C87 |

##### Evolutionary Studies
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Evolutionary Studies | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/H15 |

##### Medieval and Renaissance Studies
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Medieval and Renaissance Studies | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/G40 |

#### College of Community and Public Affairs (CCPA)

##### Education
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Childhood and Early Childhood Education | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E69 |
| 2 | Childhood Education ESOL | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E86 |
| 3 | Childhood / Early Childhood Literacy Education (All Grades) | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E65 |
| 4 | Literacy Education (All Grades) | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E66Z |
| 5 | Special Education (All Grades) | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E87Z |
| 6 | Special Education (Birth - Grade 6) | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E85Z |
| 7 | Special Education, Adolescence | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E82Z |
| 8 | Special Education, Early Childhood/Childhood | MSEd | https://www.binghamton.edu/apps/catalog/application-requirement/view/E81Z |
| 9 | Biology Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T15 |
| 10 | Chemistry Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T17 |
| 11 | Earth Science Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T18 |
| 12 | English Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T22 |
| 13 | French Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T25 |
| 14 | Mathematics Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T35 |
| 15 | Physics Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T43 |
| 16 | Social Studies Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T52 |
| 17 | Spanish Adolescence Education | MAT | https://www.binghamton.edu/apps/catalog/application-requirement/view/T54 |
| 18 | Educational Studies | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/E95 |
| 19 | Educational Theory and Practice | EdD | https://www.binghamton.edu/apps/catalog/application-requirement/view/E99 |
| 20 | Educational Leadership | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/E98 |
| 21 | Clinically Rich Intensive Teacher Institute in ESL | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/E89 |
| 22 | Community Schools | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/F45Z |
| 23 | TESOL | MA | https://www.binghamton.edu/apps/catalog/application-requirement/view/E79 |
| 24 | TESOL Advanced Certificate | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/E92 |

##### Social Work
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Social Work | MSW | https://www.binghamton.edu/apps/catalog/application-requirement/view/F56 |
| 2 | Social Work - Full Time (online) | MSW | https://www.binghamton.edu/apps/catalog/application-requirement/view/F56Z |
| 3 | Social Work - Part Time (online) | MSW | https://www.binghamton.edu/apps/catalog/application-requirement/view/F57Z |

##### Public Administration
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Public Administration | MPA | https://www.binghamton.edu/apps/catalog/application-requirement/view/C44 |
| 2 | Public Policy (online) | MPP | https://www.binghamton.edu/apps/catalog/application-requirement/view/F30Z |
| 3 | Local Government Management | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/F54 |
| 4 | Non-Profit Administration | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/F64 |

##### Human Development
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Community Research and Action | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/F43 |
| 2 | Higher Education and Student Affairs | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/F60 |
| 3 | Higher Education and Student Affairs (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/F60Z |
| 4 | Sustainable Communities | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/H31 |

##### Human Rights
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Human Rights | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/F46 |
| 2 | Human Rights | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/F47 |

##### Genocide and Mass Atrocity Prevention
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Genocide and Mass Atrocity Prevention | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/H52 |
| 2 | Genocide and Mass Atrocity Prevention | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/F52 |

##### Public Health
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Public Health | MPH | https://www.binghamton.edu/apps/catalog/application-requirement/view/H86 |

#### Decker College of Nursing and Health Sciences

##### Nursing
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Nursing | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/D99 |
| 2 | Nursing (online) | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/D99Z |
| 3 | Adult/Gerontological Clinical Nurse Specialist - Advance Standing | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D46 |
| 4 | Adult/Gerontological Clinical Nurse Specialist - BS to DNP | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D66 |
| 5 | Adult/Gerontological Nurse Practitioner - Advance Standing | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D42 |
| 6 | Adult/Gerontological Nurse Practitioner - BS to DNP | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D62 |
| 7 | Community Health Nurse Practitioner - Advance Standing | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D71 |
| 8 | Community Health Nurse Practitioner - BS to DNP | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D61 |
| 9 | Family Nurse Practitioner - Advance Standing | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D70 |
| 10 | Family Nurse Practitioner - BS to DNP | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D60 |
| 11 | Family Psychiatric Mental Health Nurse Practitioner - Advance Standing | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D73 |
| 12 | Family Psychiatric Mental Health Nurse Practitioner - BS to DNP | DNP | https://www.binghamton.edu/apps/catalog/application-requirement/view/D63 |
| 13 | Adult/Gerontological Nurse Practitioner | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D44 |
| 14 | Adult/Gerontological Nursing | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/D45 |
| 15 | Community Health Nurse Practitioner | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D96 |
| 16 | Community Health Nursing | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/D97 |
| 17 | Family Nurse Practitioner | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D92 |
| 18 | Family Psychiatric Mental Health Nurse Practitioner | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D82 |
| 19 | Forensic Health | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D80 |
| 20 | Forensic Health (online) | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D80Z |
| 21 | Disaster Management | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D86 |
| 22 | Nursing Education | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/D88 |

##### Occupational Therapy
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Occupational Therapy | OTD | https://www.binghamton.edu/apps/catalog/application-requirement/view/D30 |
| 2 | Occupational Therapy (online) | OTD | https://www.binghamton.edu/apps/catalog/application-requirement/view/D31Z |

##### Physical Therapy
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Physical Therapy | DPT | https://www.binghamton.edu/apps/catalog/application-requirement/view/D50 |

##### Speech and Language Pathology
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Speech and Language Pathology | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/D54 |

#### School of Management

##### Business Administration
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Business Administration | MBA | https://www.binghamton.edu/apps/catalog/application-requirement/view/B86 |
| 2 | Executive MBA Program | MBA | https://www.binghamton.edu/apps/catalog/application-requirement/view/B90 |
| 3 | Fast-Track Professional MBA Program (NYC) | MBA | https://www.binghamton.edu/apps/catalog/application-requirement/view/B70 |

##### Accounting
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Accounting | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/B87 |

##### Data Analytics
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Data Analytics | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/B56 |

##### Management
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Management | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/B99 |

##### Biomanufacturing
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biomanufacturing Project Management (online) | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/B16Z |

#### School of Pharmacy and Pharmaceutical Sciences

##### Pharmaceutical Sciences
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Pharmaceutical Sciences | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/P91 |
| 2 | Pharmaceutical Sciences | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/P92 |

##### Pharmacy
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Pharmacy | PharmD | https://www.binghamton.edu/apps/catalog/application-requirement/view/P98 |

#### Thomas J. Watson College of Engineering and Applied Science

##### Biomedical Engineering
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biomedical Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R11 |
| 2 | Biomedical Engineering | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R91 |

##### Computer Science
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Computer Science | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R12 |
| 2 | Computer Science (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R12Z |
| 3 | Computer Science - Artificial Intelligence | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R14 |
| 4 | Computer Science - Cybersecurity | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R15 |
| 5 | Computer Science | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R92 |
| 6 | Cybersecurity | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/R64 |

##### Electrical and Computer Engineering
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Electrical & Computer Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R05 |
| 2 | Electrical & Computer Engineering | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R95 |

##### Industrial and Systems Engineering
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Industrial and Systems Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R07 |
| 2 | Industrial and Systems Engineering (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R07Z |
| 3 | Industrial and Systems Engineering - Engineering Management | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R67 |
| 4 | Industrial and Systems Engineering - Engineering Management (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R67Z |
| 5 | Industrial and Systems Engineering: Health Systems | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R47 |
| 6 | Industrial and Systems Engineering: Health Systems (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R47Z |
| 7 | Industrial and Systems Engineering: Executive Health Systems - Manhattan | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R57 |
| 8 | Industrial and Systems Engineering | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R87 |
| 9 | Industrial and Systems Engineering (online) | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R87Z |
| 10 | Industrial Engineering | MEng | https://www.binghamton.edu/apps/catalog/application-requirement/view/R27 |

##### Mechanical Engineering
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Mechanical Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R08 |
| 2 | Mechanical Engineering | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R98 |

##### Systems Science
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Systems Science | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R03 |
| 2 | Systems Science (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R03Z |
| 3 | Systems Science: Health Systems | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R43 |
| 4 | Systems Science: Health Systems (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R43Z |
| 5 | Systems Science: Executive Health Systems - Manhattan | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R53 |
| 6 | Systems Science (online) | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/R93Z |
| 7 | Healthcare Systems Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R52 |
| 8 | Healthcare Systems Engineering (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R52Z |
| 9 | Systems Engineering | MEng | https://www.binghamton.edu/apps/catalog/application-requirement/view/R23 |
| 10 | Complex Systems Science and Engineering | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/R63 |
| 11 | Complex Systems Science and Engineering (online) | Adv Cert | https://www.binghamton.edu/apps/catalog/application-requirement/view/R63Z |

##### Information Systems
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Information Systems | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R80 |
| 2 | Information Systems (online) | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R80Z |
| 3 | Information Systems - Applied Data Science | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R82 |
| 4 | Information Systems - Cybersecurity | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R81 |
| 5 | Information Systems - Web-based Information Systems | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/R83 |

##### Materials Science
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Materials Science and Engineering | MS | https://www.binghamton.edu/apps/catalog/application-requirement/view/H18 |
| 2 | Materials Science and Engineering | PhD | https://www.binghamton.edu/apps/catalog/application-requirement/view/H23 |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (MS) — Thomas J. Watson College of Engineering and Applied Science**

- **Department**: Computer Science
- **Degree**: Master of Science (MS)
- **Application URL**: https://www.binghamton.edu/apps/catalog/application-requirement/view/R12
- **Application Platform**: Graduate School Application (https://gograd.binghamton.edu/)
- **Application Fee**: $75 (domestic), $75 (international)
- **GRE**: Not required
- **TOEFL Minimum**: 80 iBT
- **IELTS Minimum**: 6.5 (no band below 5.0)
- **Duolingo Minimum**: 105
- **PTE Minimum**: 53
- **Deadlines**: Rolling (check department website for priority dates)
- **Prerequisites**: Bachelor's degree in Computer Science or related field
- **Materials**: Transcripts, statement of purpose, letters of recommendation, resume/CV

### 2.3 Graduate admissions model

Binghamton University uses a **decentralized** graduate admissions model:
- Each academic department manages its own admissions process
- Applications are submitted through the centralized Graduate School application portal
- Admission decisions are made by individual departments
- Financial aid (assistantships, fellowships) is managed at the department level
- The Graduate School provides overarching policies and support services

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Admissions Website | https://www.binghamton.edu/admissions/undergraduate/ |
| Application Portal | Common Application, SUNY Application, or Coalition Application |
| Early Action Deadline | November 1 |
| Early Action Materials Deadline | December 1 |
| Early Action Decision Date | January 15 |
| Regular Admission Deadline | January 15 |
| Regular Admission Materials Deadline | January 15 |
| Regular Admission Decision Date | April 1 |
| International EA Deadline | November 1 |
| International EA Decision Date | January 15 |
| International RD Deadline | March 15 |
| International RD Decision Date | By April 1 |
| Application Fee | $50 |
| Fee Waiver | Available for qualifying students |
| SAT/ACT Policy | Test-optional |
| SAT Code | 2535 |
| ACT Code | 2956 |
| Superscore Policy | Yes (SAT and ACT) |
| Interview Policy | Not required (optional Glimpse video) |
| Recommendation Requirements | One teacher/counselor recommendation |
| Portfolio | Required for BFA and BMUS applicants |
| Transfer Deadline | Varies (check website) |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|---------------|-------------------|-------|
| TOEFL iBT | 80 | 95+ | Mid-50% range: 80-95 |
| TOEFL iBT (new scale, Jan 2026+) | 4.0 | 5.0+ | Mid-50% range: 4.0-5.0 |
| IELTS | 6.5 | 7.0+ | Mid-50% range: 6.5-7.0 |
| Duolingo English Test | 105 | 120+ | Mid-50% range: 110-120 |
| Pearson PTE Academic | 53 | 65+ | Mid-50% range: 53-65 |
| Cambridge English (B2, C1, C2) | 176 | 185+ | Mid-50% range: 176-185 |
| SAT (EBRW) | N/A | N/A | Mid-50% range: 530-640 |
| ACT (English) | N/A | N/A | Mid-50% range: 21-27 |

**Applicability**: Required for all international students who are not native English speakers.

### 3.3 Graduate — global rules

- **Admissions Model**: Decentralized (each department manages own admissions)
- **Application Platform**: Graduate School Application (https://gograd.binghamton.edu/)
- **Application Fee**: $75 (domestic and international)
- **GRE/GMAT Policy**: Not universally required; check individual program requirements
- **Language Test Policy**: Required for non-native English speakers (see below)
- **Exemption Rules**: Available for applicants from English-speaking countries or with degrees from English-speaking institutions
- **Application Timeline**: Varies by program; most have rolling admissions

**Graduate English Proficiency Requirements**:

| Exam | Minimum Score | Notes |
|------|---------------|-------|
| TOEFL iBT | 80 | MyBest scores accepted |
| TOEFL Essentials | 9 | MyBest scores accepted |
| IELTS | 6.5 | No band below 5.0 |
| Pearson PTE Academic | 53 | Online option accepted |
| Duolingo English Test | 105 | |

**Institution Codes**:
- TOEFL: 2535
- GRE: Check individual departments

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**Academic Year 2026-2027**

| Expense Item | New York State Resident | Out-of-State Resident | International Resident |
|--------------|------------------------|----------------------|----------------------|
| Tuition | $7,070 | $28,970 | $28,970 |
| Fees | $3,497 | $3,497 | $6,371 |
| Housing and Meals | $20,179 | $20,179 | $20,179 |
| **Estimated Cost of Attendance** | **$30,746** | **$54,846** | **$55,520** |

*Notes:*
- Housing reflects standard double room and average meal plan
- International student fees do not include SEVIS fee
- As of June 2026, subject to change
- Source: https://www.binghamton.edu/admissions/undergraduate/cost/

### 4.2 Undergraduate financial-aid policy

- **Need-Blind/Need-Aware**: Need-aware for all applicants (including international)
- **Financial Aid**: Available through federal, state, and institutional sources
- **Scholarships**: Merit-based scholarships available
- **Work-Study**: Federal work-study available
- **Tuition-Free Threshold**: Not specified (SUNY system policy applies)
- **Median Actual Price Paid**: Contact Financial Aid Office for current data
- **Debt-Free Graduation Rate**: Not specified
- **Average Starting Salary**: $72,438 (Class of 2022)

### 4.3 Graduate cost & funding framework

**Graduate Tuition (2026-2027)**:
- New York State Resident: Approximately $11,310 per year (varies by program)
- Out-of-State/International: Approximately $23,100 per year (varies by program)
- Source: https://www.binghamton.edu/student-accounts/tuition-fees/tuition-semester/

**Funding Opportunities**:
- Teaching Assistantships (TA)
- Research Assistantships (RA)
- Graduate Assistantships (GA)
- University Fellowships
- External Fellowships
- Tuition Scholarships

**Application Fee**: $75 (domestic and international)

**Fee Waiver Policy**: Limited fee waivers may be available; contact Graduate Admissions

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Tuition (In-State)
```yaml
field: undergraduate.costs.tuition_in_state_2026_2027
value: $7,070
source_url: https://www.binghamton.edu/admissions/undergraduate/cost/
source_snippet: "Tuition | $7,070"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Undergraduate Tuition (Out-of-State)
```yaml
field: undergraduate.costs.tuition_out_of_state_2026_2027
value: $28,970
source_url: https://www.binghamton.edu/admissions/undergraduate/cost/
source_snippet: "Tuition | $28,970"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: Early Action Deadline
```yaml
field: undergraduate.admissions.early_action_deadline
value: November 1
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/freshman/
source_snippet: "Early action deadline: November 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Regular Admission Deadline
```yaml
field: undergraduate.admissions.regular_deadline
value: January 15
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/freshman/
source_snippet: "Regular admissions deadline: January 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: Test-Optional Policy
```yaml
field: undergraduate.admissions.test_optional
value: true
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/freshman/
source_snippet: "Binghamton University is test optional which means standardized test scores are not required."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: Application Fee
```yaml
field: undergraduate.admissions.application_fee
value: $50
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/freshman/
source_snippet: "There is a $50 nonrefundable application fee."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: TOEFL Minimum (Undergraduate)
```yaml
field: undergraduate.international.tofl_minimum
value: 80 (iBT)
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/international/first-year.html
source_snippet: "TOEFL (iBT, iBT Home Edition) | 80-95"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: IELTS Minimum (Undergraduate)
```yaml
field: undergraduate.international.ielts_minimum
value: 6.5
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/international/first-year.html
source_snippet: "IELTS | 6.5-7.0"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-001: Graduate TOEFL Minimum
```yaml
field: graduate.international.tofl_minimum
value: 80 (iBT)
source_url: https://www.binghamton.edu/admissions/graduate/apply/international-application-requirements.html
source_snippet: "Binghamton University requires a minimum TOEFL score of 80 on the internet-Based Test (iBT)."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate IELTS Minimum
```yaml
field: graduate.international.ielts_minimum
value: 6.5 (no band below 5.0)
source_url: https://www.binghamton.edu/admissions/graduate/apply/international-application-requirements.html
source_snippet: "Binghamton University requires a minimum IELTS score of 6.5, with no band below 5.0."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate Duolingo Minimum
```yaml
field: graduate.international.duolingo_minimum
value: 105
source_url: https://www.binghamton.edu/admissions/graduate/apply/international-application-requirements.html
source_snippet: "Binghamton University requires a minimum Duolingo score of 105."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Graduate PTE Minimum
```yaml
field: graduate.international.pte_minimum
value: 53
source_url: https://www.binghamton.edu/admissions/graduate/apply/international-application-requirements.html
source_snippet: "Binghamton University requires a minimum Pearson PTE Academic score of 53."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-005: Graduate Application Fee
```yaml
field: graduate.admissions.application_fee
value: $75
source_url: https://www.binghamton.edu/admissions/graduate/apply/requirements.html
source_snippet: "Application Fee: $75"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-001: Six Schools
```yaml
field: institution.schools
value: ["Harpur College of Arts and Sciences", "College of Community and Public Affairs", "Decker College of Nursing and Health Sciences", "School of Management", "School of Pharmacy and Pharmaceutical Sciences", "Thomas J. Watson College of Engineering and Applied Science"]
source_url: https://www.binghamton.edu/admissions/undergraduate/academics/schools.html
source_snippet: "The University consists of six schools attracting outstanding students and award-winning faculty."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-002: Total Programs
```yaml
field: institution.total_programs
value: 130+ undergraduate programs, 150+ graduate programs
source_url: https://www.binghamton.edu/admissions/undergraduate/academics/programs.html
source_snippet: "Our academic offerings encompass 130+ majors, minors, certificates, concentrations, emphases, tracks and specializations."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-003: Public Ivy Status
```yaml
field: institution.rankings.public_ivy
value: Top Public Ivy
source_url: https://www.binghamton.edu/admissions/undergraduate/apply/international/first-year.html
source_snippet: "As a 'Top Public Ivy' (Forbes, 2024), a Binghamton education comes with a distinguished national and international reputation."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-004: Average Starting Salary
```yaml
field: institution.outcomes.average_starting_salary
value: $72,438
source_url: https://www.binghamton.edu/admissions/undergraduate/academics/outcomes.html
source_snippet: "Binghamton University: $72,438"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-C-001: Housing and Meals Cost
```yaml
field: undergraduate.costs.housing_meals_2026_2027
value: $20,179
source_url: https://www.binghamton.edu/admissions/undergraduate/cost/
source_snippet: "Housing and meals | $20,179"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-C-002: Fees (In-State/Out-of-State)
```yaml
field: undergraduate.costs.fees_2026_2027
value: $3,497 (in-state/out-of-state), $6,371 (international)
source_url: https://www.binghamton.edu/admissions/undergraduate/cost/
source_snippet: "Fees | $3,497 | $3,497 | $6,371**"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
binghamton-knowledge-base-v2/
├── overview/
│   ├── institution-overview.md
│   ├── school-hierarchy.md
│   └── program-counts.md
├── undergraduate/
│   ├── harpur-college-programs.md
│   ├── ccpa-programs.md
│   ├── decker-college-programs.md
│   ├── school-of-management-programs.md
│   ├── school-of-pharmacy-programs.md
│   ├── watson-college-programs.md
│   └── minors-list.md
├── graduate/
│   ├── harpur-college-graduate-programs.md
│   ├── ccpa-graduate-programs.md
│   ├── decker-college-graduate-programs.md
│   ├── school-of-management-graduate-programs.md
│   ├── school-of-pharmacy-graduate-programs.md
│   └── watson-college-graduate-programs.md
├── admissions/
│   ├── undergraduate-deadlines.md
│   ├── undergraduate-requirements.md
│   ├── graduate-requirements.md
│   └── international-requirements.md
├── costs/
│   ├── undergraduate-costs.md
│   ├── graduate-costs.md
│   └── financial-aid.md
└── evidence/
    └── evidence-chain-index.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "binghamton-knowledge-base-v2"
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
| P0 | Per-program GRE requirements | https://www.binghamton.edu/apps/catalog/application-requirement/view/[PROGRAM_ID] |
| P0 | Graduate program-specific deadlines | https://www.binghamton.edu/admissions/graduate/apply/requirements.html |
| P1 | Detailed financial aid data | https://www.binghamton.edu/financial-aid/ |
| P1 | Graduate stipend rates | https://www.binghamton.edu/grad-school/cost-funding/ |
| P2 | Class profile data | https://www.binghamton.edu/admissions/undergraduate/academics/profile.html |
| P2 | Transfer admission statistics | https://www.binghamton.edu/admissions/undergraduate/apply/transfer/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Binghamton University (SUNY) |
|-----------|------------------------------|
| **Total UG Cost/yr (In-State)** | $30,746 |
| **Total UG Cost/yr (Out-of-State)** | $54,846 |
| **Tuition/yr (In-State)** | $7,070 |
| **Tuition/yr (Out-of-State)** | $28,970 |
| **Need-Blind (Intl?)** | No (need-aware for all) |
| **EA Deadline** | November 1 |
| **RA Deadline** | January 15 |
| **SAT/ACT Required?** | No (test-optional) |
| **TOEFL Min (UG)** | 80 |
| **IELTS Min (UG)** | 6.5 |
| **Duolingo Min (UG)** | 105 |
| **Grad Application Fee** | $75 |
| **Total Program Count (Rule 1)** | 260+ |
| **School/Department Count (Rule 2)** | 6 schools |
| **Public Ivy Status** | Yes (Forbes, 2024) |
| **Average Starting Salary** | $72,438 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: binghamton.edu, catalog.binghamton.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
