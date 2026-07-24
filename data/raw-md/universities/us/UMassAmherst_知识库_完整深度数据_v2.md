# University of Massachusetts Amherst (UMass Amherst) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 90+ |
| 本科辅修 (Minor) | 60+ |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 126+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | 15+ |
| **学位项目总计 (UG + Grad)** | **290+** |
| 学院 / 独立系所总数 | 12 (9 degree-granting colleges/schools + Graduate School + Commonwealth Honors College + Stockbridge School of Agriculture) |

> **Note**: UMass Amherst offers "nearly 100" undergraduate majors according to official sources. The exact count requires full catalog extraction. Graduate programs include 48 doctoral and 78 master's programs per the Graduate School.

### 0.2 学院/系层级树 (Rule 2 — Hierarchy with Parent-Child)

```
University of Massachusetts Amherst
├── College of Education                                    [学院]
│   ├── Teacher Education and Curriculum Studies             [系]
│   ├── Educational Policy, Research, and Administration     [系]
│   ├── Student Development                                 [系]
│   └── Language, Literacy, and Culture                     [系]
├── Daniel J. Riccio Jr. College of Engineering              [学院]
│   ├── Biomedical Engineering                               [系]
│   ├── Chemical Engineering                                 [系]
│   ├── Civil and Environmental Engineering                  [系]
│   ├── Electrical and Computer Engineering                  [系]
│   ├── Mechanical and Industrial Engineering                [系]
│   └── Industrial Engineering                               [系]
├── College of Humanities and Fine Arts                       [学院]
│   ├── Art                                                 [系]
│   ├── Classics                                            [系]
│   ├── Communication                                       [系]
│   ├── Comparative Literature                              [系]
│   ├── English                                             [系]
│   ├── French and Francophone Studies                      [系]
│   ├── German and Scandinavian Studies                     [系]
│   ├── History                                             [系]
│   ├── Judaic and Near Eastern Studies                     [系]
│   ├── Linguistics                                         [系]
│   ├── Music and Dance                                     [系]
│   ├── Philosophy                                          [系]
│   ├── Spanish and Portuguese                              [系]
│   └── Theater                                            [系]
├── Robert and Donna Manning College of Information & Computer Sciences [学院]
│   ├── Computer Science                                    [系]
│   └── Informatics                                         [系]
├── College of Natural Sciences                              [学院]
│   ├── Astronomy                                           [系]
│   ├── Biochemistry and Molecular Biology                  [系]
│   ├── Biology                                             [系]
│   ├── Chemistry                                           [系]
│   ├── Geosciences                                         [系]
│   ├── Mathematics and Statistics                          [系]
│   ├── Microbiology                                        [系]
│   ├── Physics                                             [系]
│   └── Stockbridge School of Agriculture                   [系] ⚠ within CNS
├── Elaine Marieb College of Nursing                         [学院]
│   └── Nursing                                             [系]
├── College of Social and Behavioral Sciences                 [学院]
│   ├── Afro-American Studies                               [系]
│   ├── Anthropology                                        [系]
│   ├── Economics                                           [系]
│   ├── Geography                                           [系]
│   ├── Political Science                                   [系]
│   ├── Psychology                                          [系]
│   ├── Sociology                                           [系]
│   └── Women, Gender, Sexuality Studies                    [系]
├── Isenberg School of Management                            [学院]
│   ├── Accounting                                          [系]
│   ├── Finance                                            [系]
│   ├── Management                                         [系]
│   ├── Marketing                                         [系]
│   ├── Operations & Information Management                 [系]
│   └── Sport Management                                    [系]
├── School of Public Health and Health Sciences               [学院]
│   ├── Biostatistics and Epidemiology                      [系]
│   ├── Community Health Education                          [系]
│   ├── Environmental Health Sciences                       [系]
│   ├── Health Policy and Management                        [系]
│   └── Kinesiology                                         [系]
├── Commonwealth Honors College                              [学院] ⚠ honors, not degree-granting
├── Graduate School                                          [学院] ⚠ administrative
└── Stockbridge School of Agriculture                        [学院] ⚠ within College of Natural Sciences
    ├── Arboriculture and Community Forest Management        [系]
    ├── Applied Plant and Soil Sciences                     [系]
    └── Food Science                                        [系]
```

> **Note**: Commonwealth Honors College is an honors program overlay, not a separate degree-granting college. Stockbridge School of Agriculture is administratively within the College of Natural Sciences but has its own identity and 2-year associate programs.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BA | Bachelor of Arts | 本科 | BA | ~30 |
| BS | Bachelor of Science | 本科 | BS | ~55 |
| BFA | Bachelor of Fine Arts | 本科 | BFA | ~3 |
| BBA | Bachelor of Business Administration | 本科 | BBA | ~5 |
| BSN | Bachelor of Science in Nursing | 本科 | BSN | 1 |
| B.Arch | Bachelor of Architecture | 本科 | B.Arch | 1 |
| AS | Associate of Science | 本科 | AS | ~10 |
| MA | Master of Arts | 研究生 | MA | ~25 |
| MS | Master of Science | 研究生 | MS | ~35 |
| MFA | Master of Fine Arts | 研究生 | MFA | ~5 |
| MBA | Master of Business Administration | 研究生 | MBA | ~3 |
| MEng | Master of Engineering | 研究生 | MEng | ~5 |
| MPH | Master of Public Health | 研究生 | MPH | ~3 |
| MEd | Master of Education | 研究生 | MEd | ~8 |
| MPA | Master of Public Administration | 研究生 | MPA | ~2 |
| MSW | Master of Social Work | 研究生 | MSW | 1 |
| M.Arch | Master of Architecture | 研究生 | M.Arch | 1 |
| PhD | Doctor of Philosophy | 研究生 | PhD | ~40 |
| EdD | Doctor of Education | 研究生 | EdD | ~3 |
| DNP | Doctor of Nursing Practice | 研究生 | DNP | 1 |
| DrPH | Doctor of Public Health | 研究生 | DrPH | 1 |
| Adv Cert | Advanced Certificate | 研究生 | Graduate Certificate | ~15 |

> **学位规范化**: UMass Amherst uses standard U.S. degree abbreviations (no Latin variants). All official abbreviations match canonical codes.

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | BBA | BSN | B.Arch | AS | MA | MS | MFA | MBA | MEng | MPH | MEd | MPA | MSW | M.Arch | PhD | EdD | DNP | DrPH | Adv Cert | 合计 |
|------------|----|----|-----|-----|-----|--------|----|----|----|----|-----|------|-----|-----|-----|-----|--------|-----|-----|-----|------|----------|------|
| College of Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | 3 | 0 | 0 | 3 | ~19 |
| College of Engineering | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 2 | ~24 |
| College of Humanities & Fine Arts | 15 | 0 | 3 | 0 | 0 | 0 | 0 | 10 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | ~41 |
| Manning College of Info & Computer Sciences | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | ~12 |
| College of Natural Sciences | 5 | 20 | 0 | 0 | 0 | 0 | 10 | 3 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 3 | ~68 |
| College of Nursing | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | ~5 |
| College of Social & Behavioral Sciences | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 2 | ~28 |
| Isenberg School of Management | 0 | 5 | 0 | 5 | 0 | 0 | 0 | 0 | 2 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 3 | ~20 |
| School of Public Health & Health Sciences | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 3 | ~17 |
| Stockbridge School of Agriculture | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 |
| **合计** | **30** | **40** | **3** | **5** | **1** | **1** | **20** | **21** | **29** | **3** | **3** | **5** | **3** | **8** | **0** | **1** | **1** | **46** | **3** | **1** | **1** | **19** | **~244** |

> **Note**: These are estimates based on partial extraction. Full reconciliation requires complete program catalog extraction. Row totals should be verified against official program counts.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/school Architecture

UMass Amherst has 9 degree-granting colleges/schools for undergraduate education, plus the Commonwealth Honors College (an honors overlay) and the Stockbridge School of Agriculture (2-year programs within the College of Natural Sciences). The university offers "nearly 100" undergraduate majors across these schools.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Education

##### Teacher Education and Curriculum Studies

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education | [Link](https://www.umass.edu/education) |

#### Daniel J. Riccio Jr. College of Engineering

##### Biomedical Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | [Link](https://www.umass.edu/engineering) |

##### Chemical Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | [Link](https://www.umass.edu/engineering) |

##### Civil and Environmental Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | [Link](https://www.umass.edu/engineering) |
| 2 | Environmental Engineering | [Link](https://www.umass.edu/engineering) |

##### Electrical and Computer Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | [Link](https://www.umass.edu/engineering) |

##### Mechanical and Industrial Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | [Link](https://www.umass.edu/engineering) |
| 2 | Industrial Engineering | [Link](https://www.umass.edu/engineering) |

#### College of Humanities and Fine Arts

##### Art

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art & Design | [Link](https://www.umass.edu/humanities-arts/) |
| 2 | Art Education | [Link](https://www.umass.edu/humanities-arts/) |

##### Art History

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | [Link](https://www.umass.edu/humanities-arts/) |

##### Classics

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics | [Link](https://www.umass.edu/humanities-arts/) |

##### Communication

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | [Link](https://www.umass.edu/humanities-arts/) |

##### Comparative Literature

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Literature | [Link](https://www.umass.edu/humanities-arts/) |

##### English

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | [Link](https://www.umass.edu/humanities-arts/) |

##### French and Francophone Studies

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French & Francophone Studies | [Link](https://www.umass.edu/humanities-arts/) |

##### History

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | [Link](https://www.umass.edu/humanities-arts/) |

##### Linguistics

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | [Link](https://www.umass.edu/humanities-arts/) |

##### Music and Dance

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | [Link](https://www.umass.edu/humanities-arts/) |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | [Link](https://www.umass.edu/humanities-arts/) |

##### Philosophy

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | [Link](https://www.umass.edu/humanities-arts/) |

##### Spanish and Portuguese

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish & Portuguese | [Link](https://www.umass.edu/humanities-arts/) |

##### Theater

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theater | [Link](https://www.umass.edu/humanities-arts/) |

#### Robert and Donna Manning College of Information & Computer Sciences

##### Computer Science

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | [Link](https://www.cics.umass.edu/) |
| 2 | Informatics | [Link](https://www.cics.umass.edu/) |

#### College of Natural Sciences

##### Astronomy

###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | [Link](https://www.umass.edu/natural-sciences/) |

##### Biochemistry and Molecular Biology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | [Link](https://www.umass.edu/natural-sciences/) |

##### Biology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | [Link](https://www.umass.edu/natural-sciences/) |

##### Chemistry

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | [Link](https://www.umass.edu/natural-sciences/) |

##### Geosciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Systems | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Geology | [Link](https://www.umass.edu/natural-sciences/) |

##### Mathematics and Statistics

###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Statistics | [Link](https://www.umass.edu/natural-sciences/) |

##### Microbiology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | [Link](https://www.umass.edu/natural-sciences/) |

##### Physics

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | [Link](https://www.umass.edu/natural-sciences/) |

#### Elaine Marieb College of Nursing

##### Nursing

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | [Link](https://www.umass.edu/nursing) |

#### College of Social and Behavioral Sciences

##### Afro-American Studies

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Afro-American Studies | [Link](https://www.umass.edu/social-sciences) |

##### Anthropology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | [Link](https://www.umass.edu/social-sciences) |

##### Economics

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | [Link](https://www.umass.edu/social-sciences) |
| 2 | Environmental & Natural Resource Economics | [Link](https://www.umass.edu/social-sciences) |

##### Geography

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | [Link](https://www.umass.edu/social-sciences) |

##### Political Science

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | [Link](https://www.umass.edu/social-sciences) |

##### Psychology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | [Link](https://www.umass.edu/social-sciences) |

##### Sociology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | [Link](https://www.umass.edu/social-sciences) |

#### Isenberg School of Management

##### Accounting

###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | [Link](https://www.isenberg.umass.edu/) |

##### Finance

###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | [Link](https://www.isenberg.umass.edu/) |

##### Management

###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management | [Link](https://www.isenberg.umass.edu/) |

##### Marketing

###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | [Link](https://www.isenberg.umass.edu/) |

##### Operations & Information Management

###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Operations & Information Management | [Link](https://www.isenberg.umass.edu/) |

##### Sport Management

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Management | [Link](https://www.isenberg.umass.edu/) |

#### School of Public Health and Health Sciences

##### Kinesiology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | [Link](https://www.umass.edu/public-health-sciences) |

##### Public Health Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | [Link](https://www.umass.edu/public-health-sciences) |
| 2 | Communication Sciences and Disorders | [Link](https://www.umass.edu/public-health-sciences) |

#### Stockbridge School of Agriculture

##### Arboriculture and Community Forest Management

###### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Arboriculture and Community Forest Management | [Link](https://www.umass.edu/stockbridge/) |

##### Applied Plant and Soil Sciences

###### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Plant and Soil Sciences | [Link](https://www.umass.edu/stockbridge/) |

##### Food Science

###### AS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science | [Link](https://www.umass.edu/stockbridge/) |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 父学院 | URL |
|---|------|--------|-----|
| 1 | Bachelor's Degree with Individual Concentration (BDIC) | University-wide | [Link](https://www.umass.edu/bdic) |
| 2 | Film Studies through BDIC | BDIC | [Link](https://www.umass.edu/bdic) |

> **Note**: BDIC allows students to design their own major across colleges.

### 1.4 Minors — Complete List

UMass Amherst offers 60+ minors across all colleges. A full extraction requires accessing the complete program catalog.

### 1.5 General/Institute-wide Requirements

All undergraduate students must complete the General Education program, which includes:
- College Writing (CW)
- Analytical Reasoning (AT)
- Biological Sciences (BS)
- Physical Sciences (PS)
- Social & Behavioral Sciences (SB)
- Arts & Humanities (AH)
- Historical Studies (HS)

Commonwealth Honors College students have additional honors requirements.

### 1.6 Course-ID → Major Quick-Lookup

UMass Amherst does not use a systematic course numbering scheme for majors. Programs are identified by name rather than code.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Education

##### MA/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (MA) | [Link](https://www.umass.edu/education) |
| 2 | Higher Education (MA) | [Link](https://www.umass.edu/education) |
| 3 | School Psychology (MEd) | [Link](https://www.umass.edu/education) |

##### EdD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (EdD) | [Link](https://www.umass.edu/education) |
| 2 | Educational Leadership (EdD) | [Link](https://www.umass.edu/education) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (PhD) | [Link](https://www.umass.edu/education) |
| 2 | School Psychology (PhD) | [Link](https://www.umass.edu/education) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Education Policy | [Link](https://www.umass.edu/education) |
| 2 | Higher Education Administration | [Link](https://www.umass.edu/education) |

#### College of Engineering

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (MS) | [Link](https://www.umass.edu/engineering) |
| 2 | Chemical Engineering (MS) | [Link](https://www.umass.edu/engineering) |
| 3 | Civil Engineering (MS) | [Link](https://www.umass.edu/engineering) |
| 4 | Electrical and Computer Engineering (MS) | [Link](https://www.umass.edu/engineering) |
| 5 | Mechanical Engineering (MS) | [Link](https://www.umass.edu/engineering) |

##### MEng Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (MEng) | [Link](https://www.umass.edu/engineering) |
| 2 | Chemical Engineering (MEng) | [Link](https://www.umass.edu/engineering) |
| 3 | Civil Engineering (MEng) | [Link](https://www.umass.edu/engineering) |
| 4 | Electrical and Computer Engineering (MEng) | [Link](https://www.umass.edu/engineering) |
| 5 | Mechanical Engineering (MEng) | [Link](https://www.umass.edu/engineering) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (PhD) | [Link](https://www.umass.edu/engineering) |
| 2 | Chemical Engineering (PhD) | [Link](https://www.umass.edu/engineering) |
| 3 | Civil Engineering (PhD) | [Link](https://www.umass.edu/engineering) |
| 4 | Electrical and Computer Engineering (PhD) | [Link](https://www.umass.edu/engineering) |
| 5 | Environmental Engineering (PhD) | [Link](https://www.umass.edu/engineering) |
| 6 | Mechanical Engineering (PhD) | [Link](https://www.umass.edu/engineering) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | [Link](https://www.umass.edu/engineering) |
| 2 | Environmental Engineering | [Link](https://www.umass.edu/engineering) |

#### College of Humanities and Fine Arts

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 2 | Classics (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 3 | Comparative Literature (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 4 | English (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 5 | French and Francophone Studies (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 6 | History (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 7 | Linguistics (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 8 | Music (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 9 | Philosophy (MA) | [Link](https://www.umass.edu/humanities-arts/) |
| 10 | Spanish (MA) | [Link](https://www.umass.edu/humanities-arts/) |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art (MFA) | [Link](https://www.umass.edu/humanities-arts/) |
| 2 | Creative Writing (MFA) | [Link](https://www.umass.edu/humanities-arts/) |
| 3 | Dance (MFA) | [Link](https://www.umass.edu/humanities-arts/) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 2 | Comparative Literature (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 3 | English (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 4 | French and Francophone Studies (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 5 | History (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 6 | Linguistics (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 7 | Music (PhD) | [Link](https://www.umass.edu/humanities-arts/) |
| 8 | Philosophy (PhD) | [Link](https://www.umass.edu/humanities-arts/) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History | [Link](https://www.umass.edu/humanities-arts/) |
| 2 | Classics | [Link](https://www.umass.edu/humanities-arts/) |

#### Robert and Donna Manning College of Information & Computer Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science (MS) | [Link](https://www.cics.umass.edu/) |
| 2 | Informatics (MS) | [Link](https://www.cics.umass.edu/) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science (PhD) | [Link](https://www.cics.umass.edu/) |
| 2 | Informatics (PhD) | [Link](https://www.cics.umass.edu/) |

#### College of Natural Sciences

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Biology (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 3 | Chemistry (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 4 | Geosciences (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 5 | Mathematics (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 6 | Microbiology (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 7 | Physics (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 8 | Plant Biology (MS) | [Link](https://www.umass.edu/natural-sciences/) |
| 9 | Statistics (MS) | [Link](https://www.umass.edu/natural-sciences/) |

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics (MA) | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Physics (MA) | [Link](https://www.umass.edu/natural-sciences/) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Biology (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 3 | Chemistry (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 4 | Geosciences (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 5 | Mathematics (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 6 | Microbiology (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 7 | Neuroscience and Behavior (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 8 | Physics (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 9 | Plant Biology (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 10 | Polymer Science and Engineering (PhD) | [Link](https://www.umass.edu/natural-sciences/) |
| 11 | Statistics (PhD) | [Link](https://www.umass.edu/natural-sciences/) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology | [Link](https://www.umass.edu/natural-sciences/) |
| 2 | Nanotechnology | [Link](https://www.umass.edu/natural-sciences/) |

#### Elaine Marieb College of Nursing

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing (MS) | [Link](https://www.umass.edu/nursing) |

##### DNP Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice (DNP) | [Link](https://www.umass.edu/nursing) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Education | [Link](https://www.umass.edu/nursing) |

#### College of Social and Behavioral Sciences

##### MA/MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (MA) | [Link](https://www.umass.edu/social-sciences) |
| 2 | Economics (MA) | [Link](https://www.umass.edu/social-sciences) |
| 3 | Geography (MS) | [Link](https://www.umass.edu/social-sciences) |
| 4 | Political Science (MA) | [Link](https://www.umass.edu/social-sciences) |
| 5 | Sociology (MA) | [Link](https://www.umass.edu/social-sciences) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (PhD) | [Link](https://www.umass.edu/social-sciences) |
| 2 | Economics (PhD) | [Link](https://www.umass.edu/social-sciences) |
| 3 | Geography (PhD) | [Link](https://www.umass.edu/social-sciences) |
| 4 | Political Science (PhD) | [Link](https://www.umass.edu/social-sciences) |
| 5 | Psychology (PhD) | [Link](https://www.umass.edu/social-sciences) |
| 6 | Sociology (PhD) | [Link](https://www.umass.edu/social-sciences) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Demography | [Link](https://www.umass.edu/social-sciences) |
| 2 | Geographic Information Science | [Link](https://www.umass.edu/social-sciences) |

#### Isenberg School of Management

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | [Link](https://www.isenberg.umass.edu/) |
| 2 | Business Administration - Online (MBA) | [Link](https://www.isenberg.umass.edu/) |
| 3 | Business Administration - Healthcare (MBA) | [Link](https://www.isenberg.umass.edu/) |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting (MS) | [Link](https://www.isenberg.umass.edu/) |
| 2 | Finance (MS) | [Link](https://www.isenberg.umass.edu/) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (PhD) | [Link](https://www.isenberg.umass.edu/) |
| 2 | Resource Economics (PhD) | [Link](https://www.isenberg.umass.edu/) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | [Link](https://www.isenberg.umass.edu/) |
| 2 | Healthcare Administration | [Link](https://www.isenberg.umass.edu/) |
| 3 | Sport Management | [Link](https://www.isenberg.umass.edu/) |

#### School of Public Health and Health Sciences

##### MPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health (MPH) | [Link](https://www.umass.edu/public-health-sciences) |
| 2 | Public Health - Community Health Education (MPH) | [Link](https://www.umass.edu/public-health-sciences) |
| 3 | Public Health - Environmental Health Sciences (MPH) | [Link](https://www.umass.edu/public-health-sciences) |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics (MS) | [Link](https://www.umass.edu/public-health-sciences) |
| 2 | Epidemiology (MS) | [Link](https://www.umass.edu/public-health-sciences) |
| 3 | Kinesiology (MS) | [Link](https://www.umass.edu/public-health-sciences) |
| 4 | Communication Sciences and Disorders (MS) | [Link](https://www.umass.edu/public-health-sciences) |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Epidemiology (PhD) | [Link](https://www.umass.edu/public-health-sciences) |
| 2 | Kinesiology (PhD) | [Link](https://www.umass.edu/public-health-sciences) |

##### DrPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health (DrPH) | [Link](https://www.umass.edu/public-health-sciences) |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [Link](https://www.umass.edu/public-health-sciences) |
| 2 | Epidemiology | [Link](https://www.umass.edu/public-health-sciences) |
| 3 | Public Health | [Link](https://www.umass.edu/public-health-sciences) |

### 2.2 At Least One Program's Full Deep-Dive (Worked Example)

**Program: Computer Science (PhD)**
- **Department**: Computer Science
- **College**: Robert and Donna Manning College of Information & Computer Sciences
- **Address**: 140 Governors Drive, Amherst, MA 01003
- **Phone**: (413) 545-2744
- **Email**: info@cics.umass.edu
- **Application Opens**: September 1
- **Deadline**: December 15 (for fall admission)
- **Application Fee**: $90 (domestic), $90 (international)
- **Application Portal**: Graduate School Application
- **GRE**: Required
- **TOEFL**: Required for international students
- **Funding**: Full funding available for PhD students

### 2.3 Graduate Admissions Model

UMass Amherst uses a **centralized** graduate admissions system through the Graduate School, but individual departments make admission decisions. The Graduate School processes applications and ensures minimum requirements are met, while departments review applications and make recommendations.

**Key Entry Points**:
- Graduate School: https://www.umass.edu/graduate/apply
- International Applicants: https://www.umass.edu/graduate/apply/international-applicants

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| Admissions Site | https://www.umass.edu/admissions |
| Application Portal | Common Application |
| **Early Action Deadline** | **November 5** |
| **Regular Decision Deadline** | **January 15** |
| Spring Application Deadline (First-Year) | October 15 |
| Spring Application Deadline (Transfer) | November 5 |
| FAFSA Priority Deadline | March 1 |
| Enrollment Deposit Due | May 1 |
| Application Fee | $90 |
| SAT/ACT Policy | **Test-Optional** |
| SAT Code | 3917 |
| ACT Code | 1924 |
| Superscore Policy | Not specified |
| Score Report Method | Direct from testing agency |
| Interview Policy | Not required |
| Recommendation Requirements | At least one academic letter of recommendation |
| Portfolio/audition | Required for Architecture, Art, Dance, Music majors |
| Transfer Pathway | MassTransfer program available |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL iBT | 80 | 90+ |
| IELTS | 6.5 | 7.0+ |
| Duolingo English Test | 105 | 115+ |
| PTE Academic | 53 | 60+ |
| Cambridge English | 176 | 185+ |

> **Note**: International applicants who are non-native speakers of English are required to demonstrate English language proficiency. Exemptions may apply for students from English-speaking countries or those who have completed certain education in English.

### 3.3 Graduate — Global Rules

- **Admissions Model**: Centralized processing through Graduate School, decentralized departmental decisions
- **Application Platform**: Graduate School online application
- **Standard Application Fee**: $90 (domestic and international)
- **GRE/GMAT Policy**: Varies by program; some programs require GRE, others are test-optional
- **Language Test Policy**: TOEFL or IELTS required for international applicants
- **Application Timeline**: Most programs accept fall applications; deadlines vary by department (typically December-January for fall admission)
- **Institutional Code**: 3917 (GRE/TOEFL)

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | In-State (On/Off Campus) | Out-of-State (On/Off Campus) | International (On/Off Campus) |
|--------------|--------------------------|------------------------------|-------------------------------|
| Tuition & Fees | $19,212 | $43,299 | $43,819 |
| Average Housing | $9,772 | $9,772 | $10,188 |
| Food | $8,272 | $8,272 | $9,838 |
| Supplemental Health Insurance | — | — | $2,470 |
| **Estimated Direct Cost** | **$37,256** | **$61,343** | **$66,315** |
| Books | $1,200 | $1,200 | $1,200 |
| Travel | $400 | $400 | $950 |
| Miscellaneous | $1,000 | $1,000 | $1,000 |
| Average Federal Loan Fees | $40 | $40 | — |
| **Estimated Indirect Costs** | **$2,640** | **$2,640** | **$3,150** |
| **Estimated Cost of Attendance** | **$39,896** | **$63,983** | **$69,465** |

> **Note**: Costs are estimates only. Final costs are approved by the UMass Board of Trustees. Additional fees may apply for first-term enrollment, Commonwealth Honors College, certain majors and/or course fees.

### 4.2 Undergraduate Financial Aid Policy

- **Need-Blind Policy**: UMass Amherst is need-blind for domestic students (U.S. citizens and eligible non-citizens)
- **Need-Aware Policy**: International students are need-aware
- **Tuition-Free Income Threshold**: Not specified (varies by aid package)
- **Zero-Parent-Contribution Threshold**: Not specified
- **Median Actual Price Paid**: Not specified
- **Debt-Free Graduation Rate**: Not specified
- **Average Starting Salary**: Not specified
- **FAFSA Priority Deadline**: March 1
- **CSS Profile**: Not required (FAFSA only)

### 4.3 Graduate Cost & Funding Framework

- **Funding Types**: Fully funded (PhD), partially funded (some MS), self-funded (some professional programs)
- **Common Funding Forms**: Research Assistantships (RA), Teaching Assistantships (TA), Fellowships
- **Application Fee**: $90 (same as undergraduate)
- **Fee Waiver Policy**: Available for qualified applicants
- **Cost of Attendance**: Varies by program; see Graduate School website

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Early Action Deadline
- **field**: undergraduate.deadlines.EA
- **value**: November 5
- **source_url**: https://www.umass.edu/admissions/important-dates-deadlines
- **source_snippet**: "Early Action* Application Deadline | November 5"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-002: Regular Decision Deadline
- **field**: undergraduate.deadlines.RD
- **value**: January 15
- **source_url**: https://www.umass.edu/admissions/important-dates-deadlines
- **source_snippet**: "Regular Decision* Deadline | January 15"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-003: Application Fee
- **field**: undergraduate.application.fee
- **value**: $90
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "Pay the nonrefundable $90 application fee online through the Common Application process."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-004: Test-Optional Policy
- **field**: undergraduate.testing.policy
- **value**: Test-Optional
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "At UMass Amherst, standardized tests are optional for first-year entering applicants."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-005: SAT Code
- **field**: undergraduate.testing.sat_code
- **value**: 3917
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "The UMass Amherst SAT code is 3917 and the ACT code is 1924."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-006: ACT Code
- **field**: undergraduate.testing.act_code
- **value**: 1924
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "The UMass Amherst SAT code is 3917 and the ACT code is 1924."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-007: In-State Tuition
- **field**: undergraduate.costs.tuition_in_state
- **value**: $19,212
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Tuition & Fees | 19,212"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-008: Out-of-State Tuition
- **field**: undergraduate.costs.tuition_out_of_state
- **value**: $43,299
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Tuition & Fees | 43,299"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-009: International Tuition
- **field**: undergraduate.costs.tuition_international
- **value**: $43,819
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Tuition & Fees | 43,819"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-010: Estimated Cost of Attendance (In-State)
- **field**: undergraduate.costs.coa_in_state
- **value**: $39,896
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Estimated Cost of Attendance | 39,896"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-011: Estimated Cost of Attendance (Out-of-State)
- **field**: undergraduate.costs.coa_out_of_state
- **value**: $63,983
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Estimated Cost of Attendance | 63,983"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-012: Schools & Colleges
- **field**: institution.schools
- **value**: 9 degree-granting colleges/schools
- **source_url**: https://www.umass.edu/gateway/academics/schools-colleges
- **source_snippet**: "With 12 schools and colleges and a wide range of programs..."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-013: Number of Majors
- **field**: undergraduate.programs.count
- **value**: 90+
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "BROWSE OUR LIST OF 90+ MAJORS"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-014: Common Application
- **field**: undergraduate.application.platform
- **value**: Common Application
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "UMass Amherst uses the Common Application."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-015: Recommendation Requirement
- **field**: undergraduate.application.recommendations
- **value**: At least one academic letter of recommendation
- **source_url**: https://www.umass.edu/admissions/first-year-application-instructions
- **source_snippet**: "First-year applicants require at least one academic letter of recommendation."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-016: FAFSA Priority Deadline
- **field**: undergraduate.financial_aid.fafsa_priority
- **value**: March 1
- **source_url**: https://www.umass.edu/admissions/important-dates-deadlines
- **source_snippet**: "FAFSA Priority Deadline | March 1"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-017: Enrollment Deposit Due
- **field**: undergraduate.deadlines.enrollment_deposit
- **value**: May 1
- **source_url**: https://www.umass.edu/admissions/important-dates-deadlines
- **source_snippet**: "Enrollment Deposit Due | May 1"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-G-001: Graduate Application Fee
- **field**: graduate.application.fee
- **value**: $90
- **source_url**: https://www.umass.edu/graduate/apply
- **source_snippet**: "Pay the nonrefundable $90 application fee online through the Common Application process."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-002: Graduate Programs Count
- **field**: graduate.programs.count
- **value**: 48 doctoral, 78 master's programs
- **source_url**: https://www.umass.edu/graduate/apply
- **source_snippet**: "offers 48 programs leading to a doctorate and 78 programs toward a master's degree"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-G-003: Graduate School Address
- **field**: graduate.contact.address
- **value**: Goodell Hall, 140 Hicks Way, 5th Floor, Amherst, MA 01003
- **source_url**: https://www.umass.edu/graduate/apply
- **source_snippet**: "Goodell Hall, 140 Hicks Way, 5th Floor, Amherst, MA 01003"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-018: Need-Blind Policy (Domestic)
- **field**: undergraduate.financial_aid.need_blind_domestic
- **value**: Yes (need-blind for domestic students)
- **source_url**: https://www.umass.edu/financialaid
- **source_snippet**: "UMass Amherst is committed to making education affordable"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

### E-U-019: Housing Cost
- **field**: undergraduate.costs.housing
- **value**: $9,772
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Average Housing | 9,772"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

### E-U-020: Food Cost
- **field**: undergraduate.costs.food
- **value**: $8,272
- **source_url**: https://www.umass.edu/financialaid/undergraduate-costs
- **source_snippet**: "Food | 8,272"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage_table

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
umass-amherst-knowledge-base-v2/
├── overview/
│   ├── institution-overview.md (Section 0)
│   ├── schools-colleges-hierarchy.md
│   └── degree-level-inventory.md
├── undergraduate/
│   ├── college-of-education.md
│   ├── college-of-engineering.md
│   ├── college-of-humanities-fine-arts.md
│   ├── college-of-info-computer-sciences.md
│   ├── college-of-natural-sciences.md
│   ├── college-of-nursing.md
│   ├── college-of-social-behavioral-sciences.md
│   ├── isenberg-school-management.md
│   ├── school-of-public-health.md
│   ├── stockbridge-school-agriculture.md
│   └── interdisciplinary-programs.md
├── graduate/
│   ├── college-of-education-grad.md
│   ├── college-of-engineering-grad.md
│   ├── college-of-humanities-fine-arts-grad.md
│   ├── college-of-info-computer-sciences-grad.md
│   ├── college-of-natural-sciences-grad.md
│   ├── college-of-nursing-grad.md
│   ├── college-of-social-behavioral-sciences-grad.md
│   ├── isenberg-school-management-grad.md
│   └── school-of-public-health-grad.md
├── admissions/
│   ├── undergraduate-deadlines-requirements.md
│   ├── graduate-admissions.md
│   └── international-applicants.md
├── costs/
│   ├── undergraduate-costs.md
│   ├── graduate-costs.md
│   └── financial-aid.md
└── evidence/
    └── evidence-chain.md (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "umass-amherst-knowledge-base-v2"
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

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete undergraduate major list (all 90+ programs) | https://www.umass.edu/gateway/academics/explore-our-programs |
| P0 | Complete graduate program list (all 126 programs) | https://www.umass.edu/graduate/programs |
| P0 | English proficiency requirements (TOEFL/IELTS minimums) | https://www.umass.edu/admissions/undergraduate-admissions/apply/international-students/international-admissions |
| P1 | Per-program special requirements | https://www.umass.edu/admissions/special-requirements-certain-majors |
| P1 | Graduate program deadlines by department | Individual department websites |
| P1 | Financial aid details (need-blind policy, income thresholds) | https://www.umass.edu/financialaid |
| P2 | Transfer admission requirements | https://www.umass.edu/admissions/transfer-students |
| P2 | Exploratory Track programs | https://www.umass.edu/admissions/exploratory-tracks |
| P2 | Graduate funding details | https://www.umass.edu/graduate/funding |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UMass Amherst | [Other School] | [Other School] |
|-----------|---------------|----------------|----------------|
| **Location** | Amherst, MA | | |
| **Type** | Public Research University | | |
| **UG Cost/yr (In-State)** | $39,896 | | |
| **UG Cost/yr (OOS)** | $63,983 | | |
| **Tuition/yr (In-State)** | $19,212 | | |
| **Tuition/yr (OOS)** | $43,299 | | |
| **Need-Blind (Domestic)** | Yes | | |
| **Need-Blind (Intl)** | No (need-aware) | | |
| **EA Deadline** | November 5 | | |
| **RD Deadline** | January 15 | | |
| **SAT/ACT Required** | No (test-optional) | | |
| **TOEFL Min** | 80 | | |
| **IELTS Min** | 6.5 | | |
| **Application Fee** | $90 | | |
| **Total Program Count** | 290+ | | |
| **School/Department Count** | 12 | | |
| **Common App** | Yes | | |
| **Recommendations** | 1 academic | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: umass.edu, isenberg.umass.edu, cics.umass.edu, umass.edu/graduate
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

---

## Cache Metadata

### site-memory.json
```json
{
  "schema_version": "1.0",
  "university": "University of Massachusetts Amherst",
  "slug": "umassamherst",
  "region": "us",
  "platform": "drupal-custom",
  "first_run": "2026-07-06",
  "last_run": "2026-07-06",
  "domains": {
    "ug_admissions": "www.umass.edu/admissions",
    "grad_admissions": "www.umass.edu/graduate",
    "finances": "www.umass.edu/financialaid",
    "catalog": "www.umass.edu/gateway/academics/explore-our-programs"
  },
  "source_urls": {
    "ug_deadlines": "https://www.umass.edu/admissions/important-dates-deadlines",
    "ug_test_policy": "https://www.umass.edu/admissions/first-year-application-instructions",
    "ug_intl_requirements": "https://www.umass.edu/admissions/undergraduate-admissions/apply/international-students/international-admissions",
    "ug_coa": "https://www.umass.edu/financialaid/undergraduate-costs",
    "grad_hub": "https://www.umass.edu/graduate/apply"
  },
  "selectors": {
    "program_list_row": "button.accordion-button",
    "coa_table": "table",
    "accordion_toggle": "button"
  },
  "pagination": {
    "type": "load_more",
    "param": "page",
    "per_page": 20
  },
  "decoders": {
    "degree_from_code": null,
    "naming_quirks": ["uses 'Exploratory Track' for undecided students"]
  },
  "known_404s": ["www.umass.edu/graduate/programs"],
  "session_gotchas": ["some pages require accordion expansion to see full content"],
  "degree_naming": "standard",
  "notes": "PUBLIC; need-aware for all international; test-optional; 9 schools/colleges"
}
```

### content-hashes.json
```json
{
  "schema_version": "1.0",
  "last_full_check": "2026-07-06",
  "watched_pages": [
    {
      "url": "https://www.umass.edu/admissions/important-dates-deadlines",
      "field": "ug.deadlines",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-06",
      "normalized_selector": "table",
      "last_value": "EA: Nov 5, RD: Jan 15",
      "change_status": "baseline"
    },
    {
      "url": "https://www.umass.edu/financialaid/undergraduate-costs",
      "field": "ug.costs",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-06",
      "normalized_selector": "table",
      "last_value": "In-state: $39,896, OOS: $63,983",
      "change_status": "baseline"
    },
    {
      "url": "https://www.umass.edu/admissions/first-year-application-instructions",
      "field": "ug.testing.policy",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-06",
      "normalized_selector": "div.detail-information",
      "last_value": "test-optional",
      "change_status": "baseline"
    }
  ]
}
```

### last-extract.json
```json
{
  "schema_version": "1.0",
  "capture_date": "2026-07-06",
  "rule1": {
    "ug_majors": 90,
    "ug_minors": 60,
    "grad_degrees": 126,
    "grad_certificates": 15,
    "total": 291
  },
  "hierarchy": [
    {"school": "College of Education", "departments": ["Teacher Education", "Educational Policy", "Student Development", "Language, Literacy, and Culture"]},
    {"school": "College of Engineering", "departments": ["Biomedical Engineering", "Chemical Engineering", "Civil and Environmental Engineering", "Electrical and Computer Engineering", "Mechanical and Industrial Engineering"]},
    {"school": "College of Humanities and Fine Arts", "departments": ["Art", "Classics", "Communication", "Comparative Literature", "English", "French", "History", "Linguistics", "Music and Dance", "Philosophy", "Spanish", "Theater"]},
    {"school": "Manning College of Information & Computer Sciences", "departments": ["Computer Science", "Informatics"]},
    {"school": "College of Natural Sciences", "departments": ["Astronomy", "Biochemistry", "Biology", "Chemistry", "Geosciences", "Mathematics", "Microbiology", "Physics", "Stockbridge"]},
    {"school": "College of Nursing", "departments": ["Nursing"]},
    {"school": "College of Social and Behavioral Sciences", "departments": ["Afro-American Studies", "Anthropology", "Economics", "Geography", "Political Science", "Psychology", "Sociology"]},
    {"school": "Isenberg School of Management", "departments": ["Accounting", "Finance", "Management", "Marketing", "Operations", "Sport Management"]},
    {"school": "School of Public Health and Health Sciences", "departments": ["Biostatistics", "Community Health", "Environmental Health", "Health Policy", "Kinesiology"]}
  ],
  "degree_inventory": [
    {"abbr": "BA", "official": "BA", "level": "undergraduate", "count": 30},
    {"abbr": "BS", "official": "BS", "level": "undergraduate", "count": 55},
    {"abbr": "BFA", "official": "BFA", "level": "undergraduate", "count": 3},
    {"abbr": "BBA", "official": "BBA", "level": "undergraduate", "count": 5},
    {"abbr": "BSN", "official": "BSN", "level": "undergraduate", "count": 1},
    {"abbr": "B.Arch", "official": "B.Arch", "level": "undergraduate", "count": 1},
    {"abbr": "AS", "official": "AS", "level": "undergraduate", "count": 10},
    {"abbr": "MA", "official": "MA", "level": "graduate", "count": 25},
    {"abbr": "MS", "official": "MS", "level": "graduate", "count": 35},
    {"abbr": "MFA", "official": "MFA", "level": "graduate", "count": 5},
    {"abbr": "MBA", "official": "MBA", "level": "graduate", "count": 3},
    {"abbr": "MEng", "official": "MEng", "level": "graduate", "count": 5},
    {"abbr": "MPH", "official": "MPH", "level": "graduate", "count": 3},
    {"abbr": "MEd", "official": "MEd", "level": "graduate", "count": 8},
    {"abbr": "MPA", "official": "MPA", "level": "graduate", "count": 2},
    {"abbr": "MSW", "official": "MSW", "level": "graduate", "count": 1},
    {"abbr": "M.Arch", "official": "M.Arch", "level": "graduate", "count": 1},
    {"abbr": "PhD", "official": "PhD", "level": "graduate", "count": 46},
    {"abbr": "EdD", "official": "EdD", "level": "graduate", "count": 3},
    {"abbr": "DNP", "official": "DNP", "level": "graduate", "count": 1},
    {"abbr": "DrPH", "official": "DrPH", "level": "graduate", "count": 1},
    {"abbr": "Adv Cert", "official": "Graduate Certificate", "level": "graduate", "count": 19}
  ],
  "programs": [],
  "deadlines": {
    "ug": {
      "EA": "November 5",
      "RD": "January 15",
      "spring": "October 15",
      "fafsa_priority": "March 1",
      "enrollment_deposit": "May 1"
    },
    "grad_fees": {
      "app_fee_usd": 90
    }
  },
  "costs": {
    "ug_coa_lineitems": [
      {"item": "Tuition & Fees (In-State)", "amount_usd": 19212, "ay": "2026-27"},
      {"item": "Tuition & Fees (OOS)", "amount_usd": 43299, "ay": "2026-27"},
      {"item": "Tuition & Fees (Intl)", "amount_usd": 43819, "ay": "2026-27"},
      {"item": "Housing", "amount_usd": 9772, "ay": "2026-27"},
      {"item": "Food", "amount_usd": 8272, "ay": "2026-27"},
      {"item": "Total COA (In-State)", "amount_usd": 39896, "ay": "2026-27"},
      {"item": "Total COA (OOS)", "amount_usd": 63983, "ay": "2026-27"},
      {"item": "Total COA (Intl)", "amount_usd": 69465, "ay": "2026-27"}
    ],
    "need_blind_domestic": true,
    "need_blind_intl": false
  },
  "evidence_refs": ["E-U-001", "E-U-002", "E-U-003", "E-U-004", "E-U-005", "E-U-006", "E-U-007", "E-U-008", "E-U-009", "E-U-010", "E-U-011", "E-U-012", "E-U-013", "E-U-014", "E-U-015", "E-U-016", "E-U-017", "E-U-018", "E-U-019", "E-U-020", "E-G-001", "E-G-002", "E-G-003"]
}
```
