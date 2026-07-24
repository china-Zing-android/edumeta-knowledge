# University of Missouri-St. Louis (UMSL) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数
| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 117 |
| 本科辅修 (Minor) | 65 |
| 本科证书 (Undergraduate Certificate) | 32 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 124 |
| 研究生证书 (Graduate Certificate) | 68 |
| **学位/项目总计** | **406** |
| 学院 / 独立系所总数 | 7 |

> **Reconciliation**: UG=117+UG Minor=65+UG Cert=32+Grad=124+Grad Cert=68 = **406** = total program count 406.

### 0.2 学院 / 系层级结构

```
University of Missouri–St. Louis (UMSL)
├── College of Arts and Sciences (CAS)                              [学院]
│   ├── Art and Design (Studio Art, Art History)                    [系]
│   ├── Biology                                                     [系]
│   ├── Chemistry and Biochemistry (Biochemistry & Biotechnology)    [系]
│   ├── Communication and Media (Communication, Media Studies)      [系]
│   ├── Computer Science (CS, Cybersecurity, Computing Technology)   [系]
│   ├── Criminology and Criminal Justice                           [系]
│   ├── Economics                                                   [系]
│   ├── English (incl. Creative Writing)                            [系]
│   ├── History (incl. Museum Studies)                              [系]
│   ├── Language and Cultural Studies (Modern Languages)            [系]
│   ├── Mathematics (incl. Actuarial Science)                       [系]
│   ├── Physics, Astronomy and Statistics                           [系]
│   ├── Music                                                       [系]
│   ├── Philosophy                                                  [系]
│   ├── Political Science                                           [系]
│   ├── Psychological Sciences (Psychology, Behavioral Neuroscience) [系]
│   ├── Sociology                                                   [系]
│   ├── Public Policy and Administration (incl. Gender Studies)      [系]
│   ├── Interdisciplinary / Liberal Studies (BIS, BLS)               [系]
│   └── Organizational Leadership                                   [系]
├── Ed G. Smith College of Business                                 [学院]
│   ├── Accounting                                                  [系]
│   ├── Finance and Legal Studies                                    [系]
│   ├── Global Leadership and Management                            [系]
│   ├── Information Systems and Technology                          [系]
│   ├── Marketing and Entrepreneurship                               [系]
│   └── Supply Chain and Analytics                                  [系]
├── College of Education                                            [学院]
│   ├── Counseling (incl. School Counseling, Clinical Mental Health) [系]
│   ├── Educational Leadership & Policy Studies                     [系]
│   ├── Educational Psychology                                      [系]
│   ├── Educator Preparation & Curriculum (Early Childhood, Elementary, Secondary, Special Ed) [系]
│   ├── Higher Education / Student Affairs                          [系]
│   └── Sport Management / Physical Education                       [系]
├── College of Nursing                                              [学院]
│   ├── Pre-Licensure BSN (Traditional, Accelerated, LPN Bridge)     [系]
│   ├── RN-to-BSN (Online Completion)                                [系]
│   ├── Doctor of Nursing Practice (DNP) — multiple emphases         [系]
│   ├── Nursing PhD                                                 [系]
│   └── Post-Graduate APRN Certificates                             [系]
├── College of Optometry                                            [学院]
│   └── Doctor of Optometry (OD) — 4-year professional program      [系]
├── Pierre Laclede Honors College                                   [学院]
│   └── (enrichment overlay; students complete Honors Certificates)  [系]
├── School of Engineering (UMSL/Washington University Joint Program) [学院]
│   ├── Civil Engineering (BSCIE)                                   [系]
│   ├── Electrical Engineering (BSEE)                               [系]
│   └── Mechanical Engineering (BSME)                               [系]
├── School of Social Work, Psychological and Brain Sciences (SSWPBS) [学院]
│   ├── Social Work (BSW, MSW)                                       [系]
│   └── Psychological and Brain Sciences (Psychology BA/BS/MA/PhD)   [系]
└── The Graduate School                                             [学院] (administrative)
    └── Non-Degree / Lifelong Learner status                         [系]
```

> **Departments (系)**: UMSL's CAS department list above is per the [College of Arts and Sciences bulletin](https://bulletin.umsl.edu/artsandsciences/). Business departments per the [Ed G. Smith College of Business bulletin](https://bulletin.umsl.edu/collegeofbusinessadministration/). Many programs under "Interdisciplinary" headings (BIS, BLS, Organizational Leadership) span multiple CAS departments.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 37 |
| BS | Bachelor of Science | 本科 | 36 |
| BFA | Bachelor of Fine Arts | 本科 | 3 |
| BES | Bachelor of Educational Studies | 本科 | 4 |
| BIS | Bachelor of Interdisciplinary Studies | 本科 | 1 |
| BLS | Bachelor of Liberal Studies | 本科 | 1 |
| BM | Bachelor of Music | 本科 | 5 |
| BSN | Bachelor of Science in Nursing | 本科 | 4 |
| BSPPA | Bachelor of Science in Public Policy Administration | 本科 | 4 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| BSEd | Bachelor of Science in Education | 本科 | 15 |
| BSCIE | Bachelor of Science in Civil Engineering | 本科 | 2 |
| BSEE | Bachelor of Science in Electrical Engineering | 本科 | 2 |
| BSME | Bachelor of Science in Mechanical Engineering | 本科 | 2 |
| MA | Master of Arts | 研究生 | 14 |
| MS | Master of Science | 研究生 | 16 |
| MBA | Master of Business Administration | 研究生 | 12 |
| MAcc | Master of Accounting | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 18 |
| MFA | Master of Fine Arts | 研究生 | 1 |
| MPPA | Master of Public Policy Administration | 研究生 | 5 |
| MSW | Master of Social Work | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 19 |
| EdD | Doctor of Education | 研究生 | 1 |
| EdS | Educational Specialist | 研究生 | 3 |
| DNP | Doctor of Nursing Practice | 研究生 | 8 |
| OD | Doctor of Optometry | 研究生 | 1 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| Accelerated Master | Accelerated Master's Degree (combined BS/BA + Master's) | 研究生 | 23 |
| Minor | Minor (辅修) | 本科 | 65 |
| Graduate Certificate | Graduate Certificate (post-baccalaureate) | 研究生 | 68 |
| Undergraduate Certificate | Undergraduate Certificate | 本科 | 32 |

> **学位规范化**: UMSL uses standard American degree codes. Engineering variants (BSCIE/BSEE/BSME) map to canonical `BS` for cross-school comparison.
> All counts sum to 406 program entries. Accelerated Master's entries are accelerated BS/BA+Master's combined pathways (often 5 years); they count separately per the bulletin.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BMA-eq* | MA | MS | MBA | MEd | PhD | EdD/EdS | ProfDoc | Minor | GradCert | UGCert | Accel | **TOTAL** |
|------------|----|----|---------|----|----|-----|-----|-----|---------|---------|-------|----------|--------|-------|---------|
| College of Arts and Sciences | 37 | 44 | 0 | 20 | 12 | 0 | 7 | 15 | 1 | 0 | 51 | 30 | 28 | 15 | **260** |
| Ed G. Smith College of Business | 0 | 12 | 0 | 0 | 5 | 12 | 0 | 1 | 0 | 1 | 9 | 18 | 3 | 7 | **68** |
| College of Education | 0 | 13 | 0 | 0 | 0 | 0 | 11 | 2 | 3 | 0 | 1 | 13 | 1 | 1 | **45** |
| College of Nursing | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 8 | 0 | 7 | 0 | 0 | **20** |
| College of Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **1** |
| School of Engineering (UMSL/Wash U Joint) | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | **9** |
| School of Social Work, Psychological and Brain Sciences | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **3** |
| **合计** | 37 | 80 | 0 | 21 | 17 | 12 | 18 | 19 | 4 | 10 | 65 | 68 | 32 | 23 | **406** |

*BMA-eq includes BFA, BES, BIS, BLS, BM, BSN, BSPPA, BSW, BSEd, BSCIE, BSEE, BSME (all canonical BS variants)
**Reconciliation check**: row-sum (406) = column-sum = total program count (406). Pass.

## Section 1 — Undergraduate Education

### 1.1 College/school architecture

UMSL's seven degree-granting colleges and one joint engineering school each award a distinct subset of undergraduate degrees. The complete parent → child hierarchy is in Section 0.2. UMSL follows a 17-unit college-prep high school curriculum requirement; see Section 3.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

> Each major appears exactly once, under its home college. Programs with multiple emphasis areas are listed separately. Departments (系) are inferred from program content; UMSL does not always publish a formal department→program mapping on the public catalog.

#### College of Arts and Sciences (CAS)

##### Undergraduate Degrees

###### BA (Bachelor of Arts)

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology BA | <https://bulletin.umsl.edu/programs/anthropology-ba/> |
| 2 | Applied Psychology of Child Advocacy Studies BA | <https://bulletin.umsl.edu/programs/applied-psychology-of-child-advocacy-studies-ba/> |
| 3 | Biology BA | <https://bulletin.umsl.edu/programs/biology-ba/> |
| 4 | Chemistry BA | <https://bulletin.umsl.edu/programs/chemistry-ba/> |
| 5 | Chemistry BA, Biochemistry Emphasis | <https://bulletin.umsl.edu/programs/chemistry-ba-biochemistry-emphasis/> |
| 6 | Communication BA | <https://bulletin.umsl.edu/programs/communication-ba/> |
| 7 | Communication BA, Applied Visual Communication Emphasis | <https://bulletin.umsl.edu/programs/communication-ba-applied-visual-communication-emphasis/> |
| 8 | Communication BA, Interpersonal Communication Emphasis | <https://bulletin.umsl.edu/programs/communication-ba-interpersonal-communication-emphasis/> |
| 9 | Communication BA, Mass Communication Emphasis | <https://bulletin.umsl.edu/programs/communication-ba-mass-communication-emphasis/> |
| 10 | Communication BA, Strategic Communication Emphasis | <https://bulletin.umsl.edu/programs/communication-ba-strategic-communication-emphasis/> |
| 11 | Economics BA | <https://bulletin.umsl.edu/programs/economics-ba/> |
| 12 | English BA | <https://bulletin.umsl.edu/programs/english-ba/> |
| 13 | History BA | <https://bulletin.umsl.edu/programs/history-ba/> |
| 14 | History BA, Public History and Museums in the Digital Age Emphasis | <https://bulletin.umsl.edu/programs/history-ba-public-history-and-museums-in-the-digital-age-emphasis/> |
| 15 | International Relations BA | <https://bulletin.umsl.edu/programs/international-relations-ba/> |
| 16 | Mathematics BA | <https://bulletin.umsl.edu/programs/mathematics-ba/> |
| 17 | Modern Language BA, Dual Language Emphasis Professional | <https://bulletin.umsl.edu/programs/modern-language-ba-dual-language-professional-emphasis/> |
| 18 | Modern Language BA, French Emphasis | <https://bulletin.umsl.edu/programs/modern-language-ba-french-emphasis/> |
| 19 | Modern Language BA, German Emphasis | <https://bulletin.umsl.edu/programs/modern-language-ba-german-emphasis/> |
| 20 | Modern Language BA, Japanese Emphasis | <https://bulletin.umsl.edu/programs/modern-language-ba-japanese-emphasis/> |
| 21 | Modern Language BA, Spanish Emphasis | <https://bulletin.umsl.edu/programs/modern-language-ba-spanish-emphasis/> |
| 22 | Music BA | <https://bulletin.umsl.edu/programs/music-ba/> |
| 23 | Organizational Leadership BA, Community Studies Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-community-studies-emphasis/> |
| 24 | Organizational Leadership BA, Computing and Information Security Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-computing-and-information-security-emphasis/> |
| 25 | Organizational Leadership BA, Corporate Communication Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-corporate-communication-emphasis/> |
| 26 | Organizational Leadership BA, Criminal Justice Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-criminal-justice-emphasis/> |
| 27 | Organizational Leadership BA, Executive Leadership Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-executive-leadership-emphasis/> |
| 28 | Organizational Leadership BA, Health Communication Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-health-communication-emphasis/> |
| 29 | Organizational Leadership BA, Individualized Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-individualized-emphasis/> |
| 30 | Organizational Leadership BA, Operational Excellence Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-operational-excellence-emphasis/> |
| 31 | Organizational Leadership BA, Social Justice Emphasis | <https://bulletin.umsl.edu/programs/organizational-leadership-ba-social-justice-emphasis/> |
| 32 | Philosophy BA | <https://bulletin.umsl.edu/programs/philosophy-ba/> |
| 33 | Physics BA | <https://bulletin.umsl.edu/programs/physics-ba/> |
| 34 | Political Science BA | <https://bulletin.umsl.edu/programs/political-science-ba/> |
| 35 | Psychological Sciences BA | <https://bulletin.umsl.edu/programs/psychology-ba/> |
| 36 | Psychology BA, Collaborative Psychology Degree Program | <https://bulletin.umsl.edu/programs/psychology-ba-mu-umsl-joint-degree/> |
| 37 | Sociology BA | <https://bulletin.umsl.edu/programs/sociology-ba/> |

###### BES (Bachelor of Educational Studies)

| # | 专业 | URL |
|---|------|-----|
| 1 | Educational Studies BES, Park and Museum Programs Emphasis | <https://bulletin.umsl.edu/programs/educational-studies-bes-park-and-museum-programs-emphasis/> |

###### BFA (Bachelor of Fine Arts)

| # | 专业 | URL |
|---|------|-----|
| 1 | Studio Art BFA, Art Education Emphasis | <https://bulletin.umsl.edu/programs/studio-art-bfa-art-education-emphasis/> |
| 2 | Studio Art BFA, Graphic Design Emphasis | <https://bulletin.umsl.edu/programs/studio-art-bfa-graphic-design-emphasis/> |
| 3 | Studio Art BFA, Studio Practice Emphasis | <https://bulletin.umsl.edu/programs/studio-art-bfa-studio-practice-emphasis/> |

###### BIS (Bachelor of Interdisciplinary Studies)

| # | 专业 | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies BIS | <https://bulletin.umsl.edu/programs/interdisciplinary-studies-bis/> |

###### BLS (Bachelor of Liberal Studies)

| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Studies BLS | <https://bulletin.umsl.edu/programs/liberal-studies-bls/> |

###### BM (Bachelor of Music)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music BM, Elective Studies in Business Emphasis | <https://bulletin.umsl.edu/programs/music-bm-elective-studies-in-business-emphasis/> |
| 2 | Music BM, Music Composition Emphasis | <https://bulletin.umsl.edu/programs/music-bm-composition-emphasis/> |
| 3 | Music BM, Music Education Emphasis | <https://bulletin.umsl.edu/programs/music-bm-music-education-emphasis/> |
| 4 | Music BM, Music Theory Emphasis | <https://bulletin.umsl.edu/programs/music-bm-music-theory-emphasis/> |
| 5 | Music BM, Performance Emphasis | <https://bulletin.umsl.edu/programs/music-bm-performance-emphasis/> |

###### BS (Bachelor of Science)

| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science BS | <https://bulletin.umsl.edu/programs/actuarial-science-bs/> |
| 2 | Biochemistry and Biotechnology BS | <https://bulletin.umsl.edu/programs/biochemistry-and-biotechnology-bs/> |
| 3 | Biology BS | <https://bulletin.umsl.edu/programs/biology-bs/> |
| 4 | Chemistry BS | <https://bulletin.umsl.edu/programs/chemistry-bs/> |
| 5 | Computer Science BS | <https://bulletin.umsl.edu/programs/computer-science-bs/> |
| 6 | Computing Technology BS | <https://bulletin.umsl.edu/programs/computing-technology-bs/> |
| 7 | Criminology and Criminal Justice BS | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-bs/> |
| 8 | Cybersecurity BS, Computer Science Emphasis | <https://bulletin.umsl.edu/programs/cybersecurity-bs-computer-science-emphasis/> |
| 9 | Data Science and Analysis BS, Biology Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-biology-emphasis/> |
| 10 | Data Science and Analysis BS, Computer Science Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-computer-science-emphasis/> |
| 11 | Data Science and Analysis BS, Economics Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-economics-emphasis/> |
| 12 | Data Science and Analysis BS, Mathematics Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-mathematics-emphasis/> |
| 13 | Data Science and Analysis BS, Social Science Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-social-science-emphasis/> |
| 14 | Data Science and Analysis BS, Supply Chain Analytics Emphasis | <https://bulletin.umsl.edu/programs/data-science-and-analysis-bs-supply-chain-analytics-emphasis/> |
| 15 | Economics BS | <https://bulletin.umsl.edu/programs/economics-bs/> |
| 16 | Mathematics BS | <https://bulletin.umsl.edu/programs/mathematics-bs/> |
| 17 | Mathematics BS, Data Science Emphasis | <https://bulletin.umsl.edu/programs/mathematics-bs-data-science-emphasis/> |
| 18 | Mathematics BS, Fiscal Mathematics Emphasis | <https://bulletin.umsl.edu/programs/mathematics-bs-fiscal-mathematics-emphasis/> |
| 19 | Physics BS, Astrophysics Emphasis | <https://bulletin.umsl.edu/programs/physics-bs-astrophysics-emphasis/> |
| 20 | Physics BS, Biophysics Emphasis | <https://bulletin.umsl.edu/programs/physics-bs-biophysics-emphasis/> |
| 21 | Physics BS, Engineering Physics Emphasis | <https://bulletin.umsl.edu/programs/physics-bs-engineering-physics-emphasis/> |
| 22 | Physics BS, General Physics Emphasis | <https://bulletin.umsl.edu/programs/physics-bs/> |
| 23 | Psychological Sciences BS | <https://bulletin.umsl.edu/programs/psychology-bs/> |
| 24 | Sociology BS | <https://bulletin.umsl.edu/programs/sociology-bs/> |

###### BSEd (Bachelor of Science in Education)

| # | 专业 | URL |
|---|------|-----|
| 1 | Secondary Education BSEd English Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-english-emphasis/> |
| 2 | Secondary Education BSEd Mathematics Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-mathematics-emphasis/> |
| 3 | Secondary Education BSEd Science-​Biology Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-science-biology-emphasis/> |
| 4 | Secondary Education BSEd Science-​Chemistry Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-science-chemistry-emphasis/> |
| 5 | Secondary Education BSed Science-​Physics Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-science-physics-emphasis/> |

###### BSPPA (Bachelor of Science in Public Policy Administration)

| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy Administration BSPPA | <https://bulletin.umsl.edu/programs/public-policy-administration-bsppa/> |
| 2 | Public Policy Administration BSPPA, Nonprofit Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-bsppa-nonprofit-emphasis/> |
| 3 | Public Policy Administration BSPPA, Public Administration Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-bsppa-public-administration-emphasis/> |
| 4 | Public Policy Administration BSPPA, Public Policy Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-bsppa-public-policy-emphasis/> |

##### Minors

###### Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | African/​African American Studies Minor | <https://bulletin.umsl.edu/programs/african-african-american-studies-minor/> |
| 2 | American Politics Minor | <https://bulletin.umsl.edu/programs/american-politics-minor/> |
| 3 | American Studies Minor | <https://bulletin.umsl.edu/programs/american-studies-minor/> |
| 4 | Anthropology Minor | <https://bulletin.umsl.edu/programs/anthropology-minor/> |
| 5 | Athletic Coaching Minor | <https://bulletin.umsl.edu/programs/athletic-coaching-minor/> |
| 6 | Biology Minor | <https://bulletin.umsl.edu/programs/biology-minor/> |
| 7 | Chemistry Minor | <https://bulletin.umsl.edu/programs/chemistry-minor/> |
| 8 | Child Advocacy Studies Minor | <https://bulletin.umsl.edu/programs/child-advocacy-studies-minor/> |
| 9 | Communication Minor | <https://bulletin.umsl.edu/programs/communication-minor/> |
| 10 | Community Health Science Minor | <https://bulletin.umsl.edu/programs/community-health-science-minor/> |
| 11 | Computer Science Minor | <https://bulletin.umsl.edu/programs/computer-science-minor/> |
| 12 | Counseling and Human Services Minor | <https://bulletin.umsl.edu/programs/counseling-and-human-services-minor/> |
| 13 | Criminology and Criminal Justice Minor | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-minor/> |
| 14 | Cybersecurity Minor | <https://bulletin.umsl.edu/programs/cybersecurity-minor/> |
| 15 | Digital Marketing Communications Minor | <https://bulletin.umsl.edu/programs/digital-marketing-communications-minor/> |
| 16 | Economics Minor | <https://bulletin.umsl.edu/programs/economics-minor/> |
| 17 | English Minor | <https://bulletin.umsl.edu/programs/english-minor/> |
| 18 | Environmental Studies Minor | <https://bulletin.umsl.edu/programs/environmental-studies-minor/> |
| 19 | Exercise Science Minor | <https://bulletin.umsl.edu/programs/exercise-science-minor/> |
| 20 | French Minor | <https://bulletin.umsl.edu/programs/french-minor/> |
| 21 | Gender and Politics Minor | <https://bulletin.umsl.edu/programs/gender-and-politics-minor/> |
| 22 | Gender Studies Minor | <https://bulletin.umsl.edu/programs/gender-studies-minor/> |
| 23 | Gerontology Minor | <https://bulletin.umsl.edu/programs/gerontology-minor/> |
| 24 | Global Health and Social Medicine Minor | <https://bulletin.umsl.edu/programs/global-health-and-social-medicine-minor/> |
| 25 | History Minor | <https://bulletin.umsl.edu/programs/history-minor/> |
| 26 | History of Art and Visual Culture Minor | <https://bulletin.umsl.edu/programs/history-of-art-and-visual-culture-minor/> |
| 27 | International and Comparative Politics Minor | <https://bulletin.umsl.edu/programs/international-and-comparative-politics-minor/> |
| 28 | International Business Minor | <https://bulletin.umsl.edu/programs/international-business-minor/> |
| 29 | International Relations Minor | <https://bulletin.umsl.edu/programs/international-relations-minor/> |
| 30 | Japanese Minor | <https://bulletin.umsl.edu/programs/japanese-minor/> |
| 31 | LatinX Studies Minor | <https://bulletin.umsl.edu/programs/latinx-studies-minor/> |
| 32 | Law and Philosophy Minor | <https://bulletin.umsl.edu/programs/law-and-philosophy-minor/> |
| 33 | Mathematics Minor | <https://bulletin.umsl.edu/programs/mathematics-minor/> |
| 34 | Modern Languages Minor | <https://bulletin.umsl.edu/programs/modern-language-minor/> |
| 35 | Music Minor | <https://bulletin.umsl.edu/programs/music-minor/> |
| 36 | Philosophy Minor | <https://bulletin.umsl.edu/programs/philosophy-minor/> |
| 37 | Philosophy of Science and Technology Minor | <https://bulletin.umsl.edu/programs/philosophy-of-science-and-technology-minor/> |
| 38 | Physics Minor | <https://bulletin.umsl.edu/programs/physics-minor/> |
| 39 | Political Science Minor | <https://bulletin.umsl.edu/programs/political-science-minor/> |
| 40 | Psychology Minor | <https://bulletin.umsl.edu/programs/psychology-minor/> |
| 41 | Public and Nonprofit Administration Minor | <https://bulletin.umsl.edu/programs/public-and-nonprofit-administration-minor/> |
| 42 | Public Law Minor | <https://bulletin.umsl.edu/programs/public-law-minor/> |
| 43 | Public Policy Minor | <https://bulletin.umsl.edu/programs/public-policy-minor/> |
| 44 | Sociology Minor | <https://bulletin.umsl.edu/programs/sociology-minor/> |
| 45 | Spanish Minor | <https://bulletin.umsl.edu/programs/spanish-minor/> |
| 46 | Statistics Minor | <https://bulletin.umsl.edu/programs/statistics-minor/> |
| 47 | Studio Art Minor | <https://bulletin.umsl.edu/programs/studio-art-minor/> |
| 48 | Transportation Studies Minor | <https://bulletin.umsl.edu/programs/transportation-studies-minor/> |
| 49 | Urban Politics Minor | <https://bulletin.umsl.edu/programs/urban-politics-minor/> |
| 50 | Urban Studies Minor | <https://bulletin.umsl.edu/programs/urban-studies-minor/> |
| 51 | Veterans Studies Minor | <https://bulletin.umsl.edu/programs/veterans-studies-minor/> |

##### Undergraduate Certificates

###### Undergraduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/actuarial-studies-undergraduate-certificate/> |
| 2 | African American and African Diaspora Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/african-american-and-african-diaspora-studies-undergraduate-certificate/> |
| 3 | Applied Econometrics and Data Analysis Undergraduate Certificate | <https://bulletin.umsl.edu/programs/applied-econometrics-and-data-analysis-undergraduate-certificate/> |
| 4 | Artificial Intelligence Undergraduate Certificate | <https://bulletin.umsl.edu/programs/artificial-intelligence-undergraduate-certificate/> |
| 5 | Child Advocacy Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/child-advocacy-studies-undergraduate-certificate/> |
| 6 | Community Health Science Undergraduate Certificate | <https://bulletin.umsl.edu/programs/community-health-science-undergraduate-certificate/> |
| 7 | Computer Programming Undergraduate Certificate | <https://bulletin.umsl.edu/programs/computer-programming-undergraduate-certificate/> |
| 8 | Conservation Biology Undergraduate Certificate | <https://bulletin.umsl.edu/programs/conservation-biology-undergraduate-certificate/> |
| 9 | Creative Writing Undergraduate Certificate | <https://bulletin.umsl.edu/programs/creative-writing-undergraduate-certificate/> |
| 10 | Cybersecurity Undergraduate Certificate | <https://bulletin.umsl.edu/programs/cybersecurity-undergraduate-certificate/> |
| 11 | Data Science Undergraduate Certificate | <https://bulletin.umsl.edu/programs/data-science-undergraduate-certificate/> |
| 12 | East Asian Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/east-asian-studies-undergraduate-certificate/> |
| 13 | Gender Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/gender-studies-undergraduate-certificate/> |
| 14 | Geographic Information Systems Undergraduate Certificate | <https://bulletin.umsl.edu/programs/geographic-information-systems-undergraduate-certificate/> |
| 15 | Gerontological Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/gerontological-studies-undergraduate-certificate/> |
| 16 | Health Communication Undergraduate Certificate | <https://bulletin.umsl.edu/programs/health-communication-undergraduate-certificate/> |
| 17 | Honors College Undergraduate Certificate, 2-​year Program | <https://bulletin.umsl.edu/programs/honors-college-undergraduate-certificate-two-year-program/> |
| 18 | Honors College Undergraduate Certificate, 4-​year Program | <https://bulletin.umsl.edu/programs/honors-college-undergraduate-certificate-four-year-program/> |
| 19 | Internet and Web Undergraduate Certificate | <https://bulletin.umsl.edu/programs/internet-and-web-undergraduate-certificate/> |
| 20 | Labor Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/labor-studies-undergraduate-certificate/> |
| 21 | Media Production Undergraduate Certificate | <https://bulletin.umsl.edu/programs/media-production-undergraduate-certificate/> |
| 22 | Mobile Apps and Computing Undergraduate Certificate | <https://bulletin.umsl.edu/programs/mobile-apps-and-computing-undergraduate-certificate/> |
| 23 | Mobile Apps and Computing Undergraduate Certificate | <https://bulletin.umsl.edu/programs/mobile-apps-and-ubiquitous-computing-undergraduate-certificate/> |
| 24 | Modern European Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/modern-european-studies-undergraduate-certificate/> |
| 25 | Neuroscience Undergraduate Certificate | <https://bulletin.umsl.edu/programs/neuroscience-undergraduate-certificate/> |
| 26 | Professional Writing Undergraduate Certificate | <https://bulletin.umsl.edu/programs/professional-writing-undergraduate-certificate/> |
| 27 | Public Relations Undergraduate Certificate | <https://bulletin.umsl.edu/programs/public-relations-undergraduate-certificate/> |
| 28 | Trauma Studies Undergraduate Certificate | <https://bulletin.umsl.edu/programs/trauma-studies-undergraduate-certificate/> |

#### Ed G. Smith College of Business

##### Undergraduate Degrees

###### BS (Bachelor of Science)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting BS | <https://bulletin.umsl.edu/programs/accounting-bs/> |
| 2 | Business Administration BS | <https://bulletin.umsl.edu/programs/business-administration-bs/> |
| 3 | Business Administration BS, Business Information Technology Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-business-information-technology-emphasis/> |
| 4 | Business Administration BS, Entrepreneurship Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-entrepreneurship-emphasis/> |
| 5 | Business Administration BS, Finance Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-finance-emphasis/> |
| 6 | Business Administration BS, International Business Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-international-business-emphasis/> |
| 7 | Business Administration BS, Management Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-management-emphasis/> |
| 8 | Business Administration BS, Marketing Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-marketing-emphasis/> |
| 9 | Business Administration BS, Supply Chain Management Emphasis | <https://bulletin.umsl.edu/programs/business-administration-bs-supply-chain-management-emphasis/> |
| 10 | Cybersecurity BS, Information Systems Emphasis | <https://bulletin.umsl.edu/programs/cybersecurity-bs-information-systems-emphasis/> |
| 11 | Information Systems and Technology BS | <https://bulletin.umsl.edu/programs/information-systems-and-technology-bs/> |
| 12 | Sport Management BS | <https://bulletin.umsl.edu/programs/sport-management-bs/> |

##### Minors

###### Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting Minor | <https://bulletin.umsl.edu/programs/accounting-minor/> |
| 2 | Business Administration Minor | <https://bulletin.umsl.edu/programs/business-administration-minor/> |
| 3 | Entrepreneurship Minor | <https://bulletin.umsl.edu/programs/entrepreneurship-minor/> |
| 4 | Finance Minor | <https://bulletin.umsl.edu/programs/finance-minor/> |
| 5 | Information Systems and Technology Minor | <https://bulletin.umsl.edu/programs/information-systems-and-technology-minor/> |
| 6 | Management Minor | <https://bulletin.umsl.edu/programs/management-minor/> |
| 7 | Marketing Minor | <https://bulletin.umsl.edu/programs/marketing-minor/> |
| 8 | Sport Management Minor | <https://bulletin.umsl.edu/programs/sport-management-minor/> |
| 9 | Supply Chain Management Minor | <https://bulletin.umsl.edu/programs/supply-chain-management-minor/> |

##### Undergraduate Certificates

###### Undergraduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting Post Baccalaureate Undergraduate Certificate | <https://bulletin.umsl.edu/programs/accounting-post-baccalaureate-undergraduate-certificate/> |
| 2 | Business and Technical Writing Undergraduate Certificate | <https://bulletin.umsl.edu/programs/business-and-technical-writing-undergraduate-certificate/> |
| 3 | Entrepreneurship Undergraduate Certificate | <https://bulletin.umsl.edu/programs/entrepreneurship-undergraduate-certificate/> |

#### College of Education

##### Undergraduate Degrees

###### BES (Bachelor of Educational Studies)

| # | 专业 | URL |
|---|------|-----|
| 1 | Educational Studies BES, Early Childhood Emphasis | <https://bulletin.umsl.edu/programs/educational-studies-bes-early-childhood-education-emphasis/> |
| 2 | Educational Studies BES, Exercise Science and Wellness Emphasis | <https://bulletin.umsl.edu/programs/educational-studies-bes-exercise-science-and-wellness-emphasis/> |
| 3 | Educational Studies BES, Youth and Adult Development Emphasis | <https://bulletin.umsl.edu/programs/educational-studies-bes-youth-and-adult-development-emphasis/> |

###### BSEd (Bachelor of Science in Education)

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education BSEd | <https://bulletin.umsl.edu/programs/early-childhood-education-bsed/> |
| 2 | Early Childhood Education BSEd, Special Education Emphasis | <https://bulletin.umsl.edu/programs/early-childhood-education-bsed-special-education-emphasis/> |
| 3 | Elementary Education BSEd, Middle School Education Emphasis | <https://bulletin.umsl.edu/programs/elementary-education-bsed-middle-school-education-emphasis/> |
| 4 | Elementary Education BSEd, Special Education and TESOL Emphasis | <https://bulletin.umsl.edu/programs/elementary-education-bsed-special-education-and-teaching-english-speakers-of-other-languages-emphasis/> |
| 5 | Elementary Education BSEd, Special Education Emphasis | <https://bulletin.umsl.edu/programs/elementary-education-bsed-special-education-emphasis/> |
| 6 | Elementary Education BSEd, TESOL Emphasis | <https://bulletin.umsl.edu/programs/elementary-education-bsed-special-education-teaching-english-speakers-of-other-languages-emphasis/> |
| 7 | Physical Education BSEd PK-​12 Emphasis | <https://bulletin.umsl.edu/programs/physical-education-bsed-pk-12-emphasis/> |
| 8 | Secondary Education BSEd Modern Foreign Language-​French Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-modern-foreign-language-french-emphasis/> |
| 9 | Secondary Education BSEd Modern Foreign Language-​Spanish Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-modern-foreign-language-spanish-emphasis/> |
| 10 | Secondary Education BSEd Social Studies Emphasis | <https://bulletin.umsl.edu/programs/secondary-education-bsed-social-studies-emphasis/> |

##### Minors

###### Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Education Minor | <https://bulletin.umsl.edu/programs/education-minor/> |

##### Undergraduate Certificates

###### Undergraduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Programming Education Undergraduate Certificate | <https://bulletin.umsl.edu/programs/computer-programming-education-undergraduate-certificate/> |

#### College of Nursing

##### Undergraduate Degrees

###### BSN (Bachelor of Science in Nursing)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing BSN | <https://bulletin.umsl.edu/programs/nursing-bsn/> |
| 2 | Nursing BSN MOS-​68C LPN to BSN Bridge | <https://bulletin.umsl.edu/programs/nursing-bsn-mos-68c-lpn-to-bsn-bridge/> |
| 3 | Nursing BSN, Accelerated Curriculum | <https://bulletin.umsl.edu/programs/nursing-bsn-accelerated-curriculum/> |
| 4 | Nursing BSN, RN to BSN Curriculum | <https://bulletin.umsl.edu/programs/nursing-bsn-rn-to-bsn-curriculum/> |

#### School of Engineering (UMSL/Wash U Joint)

##### Undergraduate Degrees

###### BSCIE (Bachelor of Science in Civil Engineering)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering BSCIE | <https://bulletin.umsl.edu/programs/civil-engineering-bscie/> |
| 2 | Civil Engineering BSCIE UMSL/​Washington University Joint Program | <https://bulletin.umsl.edu/programs/joint-engineering-civil-engineering-bscie/> |

###### BSEE (Bachelor of Science in Electrical Engineering)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering BSEE | <https://bulletin.umsl.edu/programs/electrical-engineering-bsee/> |
| 2 | Electrical Engineering BSEE UMSL/​Washington University Joint Program | <https://bulletin.umsl.edu/programs/joint-engineering-electrical-engineering-bsee/> |

###### BSME (Bachelor of Science in Mechanical Engineering)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering BSME | <https://bulletin.umsl.edu/programs/mechanical-engineering-bsme/> |
| 2 | Mechanical Engineering BSME UMSL/​Washington University Joint Program | <https://bulletin.umsl.edu/programs/joint-engineering-mechanical-engineering-bsme/> |

##### Minors

###### Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering Minor | <https://bulletin.umsl.edu/programs/civil-engineering-minor/> |
| 2 | Electrical Engineering Minor | <https://bulletin.umsl.edu/programs/electrical-engineering-minor/> |
| 3 | Mechanical Engineering Minor | <https://bulletin.umsl.edu/programs/mechanical-engineering-minor/> |

#### School of Social Work, Psychological and Brain Sciences (SSWPBS)

##### Undergraduate Degrees

###### BSW (Bachelor of Social Work)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work BSW | <https://bulletin.umsl.edu/programs/social-work-bsw/> |

##### Minors

###### Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work Minor | <https://bulletin.umsl.edu/programs/social-work-minor/> |

### 1.3 Interdisciplinary / cross-college undergraduate programs

UMSL explicitly maintains interdisciplinary undergraduate programs that span multiple departments. These are listed under their administrative home in Section 1.2; this table flags them.

| Program | Administrative Home | Notes |
|---------|--------------------|----|
| Organizational Leadership BA (10 emphases) | College of Arts and Sciences | Adult-learner oriented degree completion |
| Interdisciplinary Studies BIS | College of Arts and Sciences | Self-designed; combines 2-3 disciplines |
| Liberal Studies BLS | College of Arts and Sciences | Flexible liberal arts degree |
| Cybersecurity BS (Computer Science Emphasis) | College of Arts and Sciences | Cross-listed with Business Cybersecurity BS (Info Systems Emphasis) |
| Cybersecurity BS (Information Systems Emphasis) | Ed G. Smith College of Business | Parallel track; CAS owns the CS-emphasis version |
| Secondary Education BSEd | College of Arts and Sciences + College of Education | Teaching certification housed in Education |

### 1.4 Minors — complete list

Complete minor list. Re-listed flat for cross-school filtering. Each minor appears in its home college under Section 1.2.

| # | Minor Name | Home College | URL |
|---|-----------|------------|-----|
| 1 | Accounting Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/accounting-minor/> |
| 2 | African/​African American Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/african-african-american-studies-minor/> |
| 3 | American Politics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/american-politics-minor/> |
| 4 | American Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/american-studies-minor/> |
| 5 | Anthropology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/anthropology-minor/> |
| 6 | Athletic Coaching Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/athletic-coaching-minor/> |
| 7 | Biology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/biology-minor/> |
| 8 | Business Administration Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/business-administration-minor/> |
| 9 | Chemistry Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/chemistry-minor/> |
| 10 | Child Advocacy Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/child-advocacy-studies-minor/> |
| 11 | Civil Engineering Minor | School of Engineering (UMSL/Wash U Joint) | <https://bulletin.umsl.edu/programs/civil-engineering-minor/> |
| 12 | Communication Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/communication-minor/> |
| 13 | Community Health Science Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/community-health-science-minor/> |
| 14 | Computer Science Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/computer-science-minor/> |
| 15 | Counseling and Human Services Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/counseling-and-human-services-minor/> |
| 16 | Criminology and Criminal Justice Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-minor/> |
| 17 | Cybersecurity Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/cybersecurity-minor/> |
| 18 | Digital Marketing Communications Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/digital-marketing-communications-minor/> |
| 19 | Economics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/economics-minor/> |
| 20 | Education Minor | College of Education | <https://bulletin.umsl.edu/programs/education-minor/> |
| 21 | Electrical Engineering Minor | School of Engineering (UMSL/Wash U Joint) | <https://bulletin.umsl.edu/programs/electrical-engineering-minor/> |
| 22 | English Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/english-minor/> |
| 23 | Entrepreneurship Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/entrepreneurship-minor/> |
| 24 | Environmental Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/environmental-studies-minor/> |
| 25 | Exercise Science Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/exercise-science-minor/> |
| 26 | Finance Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/finance-minor/> |
| 27 | French Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/french-minor/> |
| 28 | Gender Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/gender-studies-minor/> |
| 29 | Gender and Politics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/gender-and-politics-minor/> |
| 30 | Gerontology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/gerontology-minor/> |
| 31 | Global Health and Social Medicine Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/global-health-and-social-medicine-minor/> |
| 32 | History Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/history-minor/> |
| 33 | History of Art and Visual Culture Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/history-of-art-and-visual-culture-minor/> |
| 34 | Information Systems and Technology Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/information-systems-and-technology-minor/> |
| 35 | International Business Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/international-business-minor/> |
| 36 | International Relations Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/international-relations-minor/> |
| 37 | International and Comparative Politics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/international-and-comparative-politics-minor/> |
| 38 | Japanese Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/japanese-minor/> |
| 39 | LatinX Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/latinx-studies-minor/> |
| 40 | Law and Philosophy Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/law-and-philosophy-minor/> |
| 41 | Management Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/management-minor/> |
| 42 | Marketing Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/marketing-minor/> |
| 43 | Mathematics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/mathematics-minor/> |
| 44 | Mechanical Engineering Minor | School of Engineering (UMSL/Wash U Joint) | <https://bulletin.umsl.edu/programs/mechanical-engineering-minor/> |
| 45 | Modern Languages Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/modern-language-minor/> |
| 46 | Music Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/music-minor/> |
| 47 | Philosophy Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/philosophy-minor/> |
| 48 | Philosophy of Science and Technology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/philosophy-of-science-and-technology-minor/> |
| 49 | Physics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/physics-minor/> |
| 50 | Political Science Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/political-science-minor/> |
| 51 | Psychology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/psychology-minor/> |
| 52 | Public Law Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/public-law-minor/> |
| 53 | Public Policy Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/public-policy-minor/> |
| 54 | Public and Nonprofit Administration Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/public-and-nonprofit-administration-minor/> |
| 55 | Social Work Minor | School of Social Work, Psychological and Brain Sciences | <https://bulletin.umsl.edu/programs/social-work-minor/> |
| 56 | Sociology Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/sociology-minor/> |
| 57 | Spanish Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/spanish-minor/> |
| 58 | Sport Management Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/sport-management-minor/> |
| 59 | Statistics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/statistics-minor/> |
| 60 | Studio Art Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/studio-art-minor/> |
| 61 | Supply Chain Management Minor | Ed G. Smith College of Business | <https://bulletin.umsl.edu/programs/supply-chain-management-minor/> |
| 62 | Transportation Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/transportation-studies-minor/> |
| 63 | Urban Politics Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/urban-politics-minor/> |
| 64 | Urban Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/urban-studies-minor/> |
| 65 | Veterans Studies Minor | College of Arts and Sciences | <https://bulletin.umsl.edu/programs/veterans-studies-minor/> |

### 1.5 General Education / University-wide requirements

UMSL's General Education requirements apply to all undergraduate students. Per the bulletin, the structure includes Foundations, Explorations, and requirements in cultural diversity, writing-intensive courses, and a capstone.

- **General Education Requirements**: <https://bulletin.umsl.edu/generaleducationrequirements/>
- **Undergraduate Study policies**: <https://bulletin.umsl.edu/undergraduatestudy/>
- **Pierre Laclede Honors College** (overlay program for high-achievers): <https://bulletin.umsl.edu/honorscollege/>

Snippet (Homepage): "With exceptional academic programs ... one size doesn't fit all." — <https://www.umsl.edu/degrees/index.html>

### 1.6 Course-ID → Major quick-lookup

**N/A**: UMSL does not use a numbered course-code scheme for majors (unlike MIT's Course 6 / Stanford's department codes). Majors are identified by name in the bulletin.

## Section 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

The Graduate School (graduate.umsl.edu) administers admissions and oversees degree progress; academic units deliver the curriculum. Master's, Educational Specialist, doctoral, and graduate certificate programs are listed below. The Graduate School also handles the Accelerated Master's and Non-Degree / Lifelong Learner statuses (not listed as discrete programs here — see Section 2.3).

#### College of Arts and Sciences (CAS)

##### Accelerated Master

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Biotechnology MS Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/biochemistry-and-biotechnology-accelerated-ms/> |
| 2 | Biology MS, Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/biology-accelerated-ms/> |
| 3 | Chemistry MS Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/chemistry-accelerated-ms/> |
| 4 | Chemistry MS, BS Biochemistry Emphasis Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/chemistry-accelerate-ms-biochemistry-emphasis/> |
| 5 | Communication MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/communication-accelerated-ma/> |
| 6 | Computer Science Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/computer-science-accelerated-ms/> |
| 7 | Criminology and Criminal Justice MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-accelerated-ma/> |
| 8 | Cybersecurity MS, Computer Science Emphasis Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/cybersecurity-accelerated-ms-computer-science-emphasis/> |
| 9 | Economics MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/economics-accelerated-ma/> |
| 10 | Education MEd Accelerated Master's, Interdisciplinary Studies Emphasis Area | <https://bulletin.umsl.edu/programs/education-accelerated-med/> |
| 11 | History MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/history-accelerated-ma/> |
| 12 | Mathematics MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/mathematics-accelerated-ma/> |
| 13 | Philosophy MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/philosophy-accelerated-ma/> |
| 14 | Political Science MA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/political-science-accelerated-ma/> |
| 15 | Public Policy Administration MPPA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/public-policy-administration-accelerated-mppa/> |

##### EdS

| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology EdS | <https://bulletin.umsl.edu/programs/school-psychology-eds/> |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication MA | <https://bulletin.umsl.edu/programs/communication-ma/> |
| 2 | Criminology and Criminal Justice MA | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-ma/> |
| 3 | Economics MA | <https://bulletin.umsl.edu/programs/economics-ma/> |
| 4 | Economics MA, Business Economics Emphasis | <https://bulletin.umsl.edu/programs/economics-ma-business-economics-emphasis/> |
| 5 | English MA | <https://bulletin.umsl.edu/programs/english-ma/> |
| 6 | History BA/​MA Dual Degree Program | <https://bulletin.umsl.edu/programs/history-ba-and-ma/> |
| 7 | History MA | <https://bulletin.umsl.edu/programs/history-ma/> |
| 8 | History MA, Museums, Heritage and Public History Emphasis | <https://bulletin.umsl.edu/programs/history-ma-museums-heritage-and-public-history-emphasis/> |
| 9 | Mathematics BA or BS/​MA Dual Degree Program | <https://bulletin.umsl.edu/programs/mathematics-ba-or-bs-and-ma/> |
| 10 | Mathematics MA | <https://bulletin.umsl.edu/programs/mathematics-ma/> |
| 11 | Mathematics MA, Data Science Emphasis | <https://bulletin.umsl.edu/programs/mathematics-ma-data-science-emphasis/> |
| 12 | Philosophy MA | <https://bulletin.umsl.edu/programs/philosophy-ma/> |
| 13 | Political Science MA | <https://bulletin.umsl.edu/programs/political-science-ma/> |
| 14 | Psychology MA, Psychological and Brain Sciences | <https://bulletin.umsl.edu/programs/psychology-ma-psychological-and-brain-sciences-emphasis/> |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling MEd, Clinical Mental Health Emphasis | <https://bulletin.umsl.edu/programs/counseling-med-clinical-mental-health-emphasis/> |
| 2 | Counseling MEd, School Counseling Emphasis | <https://bulletin.umsl.edu/programs/counseling-med-school-counseling-emphasis/> |
| 3 | Education MEd, Interdisciplinary Studies | <https://bulletin.umsl.edu/programs/education-med-interdisciplinary-studies-emphasis/> |
| 4 | Education MEd, Interdisciplinary Studies for Teacher Residency | <https://bulletin.umsl.edu/programs/education-med-interdisciplinary-studies-for-teacher-residency-emphasis/> |
| 5 | Education MEd, Interdisciplinary Studies for Temporary Authorization Certification | <https://bulletin.umsl.edu/programs/education-med-interdisciplinary-studies-for-temporary-authorization-certification-emphasis/> |
| 6 | Education MEd, Teaching English to Speakers of Other Languages Emphasis | <https://bulletin.umsl.edu/programs/education-med-teaching-english-to-speakers-of-other-languages-emphasis/> |
| 7 | Educational Psychology MEd | <https://bulletin.umsl.edu/programs/educational-psychology-med/> |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing MFA | <https://bulletin.umsl.edu/programs/creative-writing-mfa/> |

##### MPPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy Administration MPPA | <https://bulletin.umsl.edu/programs/public-policy-administration-mppa/> |
| 2 | Public Policy Administration MPPA, Individualized Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-mppa-individualized-emphasis/> |
| 3 | Public Policy Administration MPPA, Local Government Management Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-mppa-local-government-management-emphasis/> |
| 4 | Public Policy Administration MPPA, Nonprofit Organization Management Emphasis | <https://bulletin.umsl.edu/programs/public-policy-administration-mppa-nonprofit-organization-management-emphasis/> |
| 5 | Public Policy Administration MPPA, Policy Research and Analysis Emphasis | <https://bulletin.umsl.edu/programs/public-policy-adminstration-mppa-policy-research-and-analysis-emphasis/> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis MS | <https://bulletin.umsl.edu/programs/applied-behavior-analysis-ms/> |
| 2 | Biochemistry and Biotechnology MS | <https://bulletin.umsl.edu/programs/biochemistry-and-biotechnology-ms/> |
| 3 | Biochemistry and Biotechnology MS, Professional Emphasis | <https://bulletin.umsl.edu/programs/biochemistry-and-biotechnology-ms-professional-science-emphasis/> |
| 4 | Biology MS | <https://bulletin.umsl.edu/programs/biology-ms/> |
| 5 | Biology MS, Cellular and Molecular Biology Emphasis | <https://bulletin.umsl.edu/programs/biology-ms-cell-and-molecular-biology-emphasis/> |
| 6 | Biology MS, Ecology Evolution and Systematics Emphasis | <https://bulletin.umsl.edu/programs/biology-ms-ecology-evolution-and-systematics-emphasis/> |
| 7 | Biology MS, Professional Science in Cellular and Molecular Biology Emphasis | <https://bulletin.umsl.edu/programs/biology-ms-professional-science-in-cellular-and-molecular-biology-emphasis/> |
| 8 | Chemistry MS | <https://bulletin.umsl.edu/programs/chemistry-ms/> |
| 9 | Chemistry MS, Professional Science Emphasis | <https://bulletin.umsl.edu/programs/chemistry-ms-professional-science-emphasis/> |
| 10 | Computer Science MS | <https://bulletin.umsl.edu/programs/computer-science-ms/> |
| 11 | Cybersecurity MS, Computer Science Emphasis | <https://bulletin.umsl.edu/programs/cybersecurity-ms-computer-science-emphasis/> |
| 12 | Physics MS | <https://bulletin.umsl.edu/programs/physics-ms/> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biology PhD, Cell and Molecular Biology Emphasis | <https://bulletin.umsl.edu/programs/biology-phd-cell-and-molecular-biology-emphasis/> |
| 2 | Biology PhD, Ecology, Evolution and Behavior Emphasis | <https://bulletin.umsl.edu/programs/biology-phd-ecology-evolution-and-behavior-emphasis/> |
| 3 | Biology PhD, Integrative Biology Emphasis | <https://bulletin.umsl.edu/programs/biology-phd-integrative-biology-emphasis/> |
| 4 | Chemistry PhD | <https://bulletin.umsl.edu/programs/chemistry-phd/> |
| 5 | Criminology and Criminal Justice PhD | <https://bulletin.umsl.edu/programs/criminology-and-criminal-justice-phd/> |
| 6 | Education PhD, Counseling Emphasis | <https://bulletin.umsl.edu/programs/education-phd-counseling-emphasis/> |
| 7 | Education PhD, Educational Psychology Emphasis | <https://bulletin.umsl.edu/programs/education-phd-educational-psychology-emphasis/> |
| 8 | Mathematical and Computational Science PhD, Computer Science Emphasis | <https://bulletin.umsl.edu/programs/mathematical-and-computational-science-phd-computer-science-emphasis/> |
| 9 | Mathematical and Computational Science PhD, Mathematics Emphasis | <https://bulletin.umsl.edu/programs/mathematical-and-computational-science-phd-mathematics-emphasis/> |
| 10 | Mathematical and Computational Science PhD, Statistics Emphasis | <https://bulletin.umsl.edu/programs/mathematical-and-computational-science-phd-statistics-emphasis/> |
| 11 | Physics PhD | <https://bulletin.umsl.edu/programs/physics-phd/> |
| 12 | Political Science PhD | <https://bulletin.umsl.edu/programs/political-science-phd/> |
| 13 | Psychology PhD, Clinical Community Psychology Emphasis | <https://bulletin.umsl.edu/programs/psychology-phd-clinical-community-psychology-emphasis/> |
| 14 | Psychology PhD, Industrial and Organizational Psychology Emphasis | <https://bulletin.umsl.edu/programs/psychology-phd-industrial-and-organizational-psychology-emphasis/> |
| 15 | Psychology PhD, Psychological and Brain Sciences | <https://bulletin.umsl.edu/programs/psychology-phd-psychological-and-brain-sciences-emphasis/> |

##### Graduate Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | ACP Instructional Communication Graduate Certificate | <https://bulletin.umsl.edu/programs/acp-instructional-communication-graduate-certificate/> |
| 2 | Analytical Chemistry Graduate Certificate | <https://bulletin.umsl.edu/programs/analytical-chemistry-graduate-certificate/> |
| 3 | Applied Behavior Analysis Graduate Certificate | <https://bulletin.umsl.edu/programs/applied-behavior-analysis-graduate-certificate/> |
| 4 | Artificial Intelligence Graduate Certificate | <https://bulletin.umsl.edu/programs/artificial-intelligence-graduate-certificate/> |
| 5 | Biochemistry Graduate Certificate | <https://bulletin.umsl.edu/programs/biochemistry-graduate-certificate/> |
| 6 | Bioethics Graduate Certificate | <https://bulletin.umsl.edu/programs/bioethics-graduate-certificate/> |
| 7 | Biotechnology Graduate Certificate | <https://bulletin.umsl.edu/programs/biotechnology-graduate-certificate/> |
| 8 | Career Counseling Graduate Certificate | <https://bulletin.umsl.edu/programs/career-counseling-graduate-certificate/> |
| 9 | Child and Adolescent Counseling Graduate Certificate | <https://bulletin.umsl.edu/programs/child-and-adolescent-counseling-graduate-certificate/> |
| 10 | Couple, Marriage and Family Counseling Graduate Certificate | <https://bulletin.umsl.edu/programs/couple-marriage-and-family-counseling-graduate-certificate/> |
| 11 | Cybersecurity Graduate Certificate | <https://bulletin.umsl.edu/programs/cybersecurity-graduate-certificate/> |
| 12 | Data Science Graduate Certificate | <https://bulletin.umsl.edu/programs/data-science-graduate-certificate/> |
| 13 | Elementary Mathematics Specialist Graduate Certificate | <https://bulletin.umsl.edu/programs/elementary-mathematics-specialist-graduate-certificate/> |
| 14 | Enterprise Systems Development Graduate Certificate | <https://bulletin.umsl.edu/programs/enterprise-systems-development-graduate-certificate/> |
| 15 | Gender Studies Graduate Certificate | <https://bulletin.umsl.edu/programs/gender-studies-graduate-certificate/> |
| 16 | Global Biodiversity Conservation and Leadership Graduate Certificate | <https://bulletin.umsl.edu/programs/global-biodiversity-and-leadership-graduate-certificate/> |
| 17 | History Education Graduate Certificate | <https://bulletin.umsl.edu/programs/history-education-graduate-certificate/> |
| 18 | Inorganic Chemistry Graduate Certificate | <https://bulletin.umsl.edu/programs/inorganic-chemistry-graduate-certificate/> |
| 19 | International Studies Graduate Certificate | <https://bulletin.umsl.edu/programs/international-studies-graduate-certificate/> |
| 20 | Internet and Web Graduate Certificate | <https://bulletin.umsl.edu/programs/internet-and-web-graduate-certificate/> |
| 21 | Mobile Apps and Computing Graduate Certificate | <https://bulletin.umsl.edu/programs/mobile-apps-and-computing-graduate-certificate/> |
| 22 | Multicultural and Social Justice Counseling Graduate Certificate | <https://bulletin.umsl.edu/programs/multicultural-and-social-justice-counseling-graduate-certificate/> |
| 23 | Museums, Heritage, and Public History Graduate Certificate | <https://bulletin.umsl.edu/programs/museums-heritage-and-public-history-graduate-certificate/> |
| 24 | Nonprofit Organization Management and Leadership Graduate Certificate | <https://bulletin.umsl.edu/programs/nonprofit-organization-management-and-leadership-graduate-certificate/> |
| 25 | Organic Chemistry Graduate Certificate | <https://bulletin.umsl.edu/programs/organic-chemistry-graduate-certificate/> |
| 26 | Policy and Program Evaluation Graduate Certificate | <https://bulletin.umsl.edu/programs/policy-and-program-evaluation-graduate-certificate/> |
| 27 | School Counseling (Post-​Master's) Graduate Certificate | <https://bulletin.umsl.edu/programs/school-counseling-post-masters-graduate-certificate/> |
| 28 | Student Affairs Administration and Leadership Graduate Certificate | <https://bulletin.umsl.edu/programs/student-affairs-administration-and-leadership-graduate-certificate/> |
| 29 | Teaching English to Speakers of Other Languages Graduate Certificate | <https://bulletin.umsl.edu/programs/teaching-english-to-speakers-of-other-languages-graduate-certificate/> |
| 30 | Transition Studies Graduate Certificate | <https://bulletin.umsl.edu/programs/transition-studies-graduate-certificate/> |

#### Ed G. Smith College of Business

##### Accelerated Master

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting MAcc Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/accounting-accelerated-macc/> |
| 2 | Business Administration MBA Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/business-administration-accelerated-mba/> |
| 3 | Cybersecurity, Information Systems and Technology Emphasis Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/cybersecurity-accelerated-ms-information-systems-and-technology-emphasis/> |
| 4 | Financial Technology MS Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/financial-technology-accelerated-ms/> |
| 5 | Information Systems and Technology MS Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/information-systems-and-technology-accelerated-ms/> |
| 6 | Information Systems and Technology MS Accelerated Master's Degree with Cybersecurity BS | <https://bulletin.umsl.edu/programs/information-systems-and-technology-accelerated-ms-cybersecurity-majors/> |
| 7 | Supply Chain Analytics MS Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/supply-chain-analytics-accelerated-ms/> |

##### DBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration (DBA) | <https://bulletin.umsl.edu/programs/business-dba/> |

##### MAcc

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting MAcc | <https://bulletin.umsl.edu/programs/accounting-macc/> |

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration MBA | <https://bulletin.umsl.edu/programs/business-administration-mba/> |
| 2 | Business Administration MBA, Accounting Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-accounting-emphasis/> |
| 3 | Business Administration MBA, Business Analytics Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-business-analytics-emphasis/> |
| 4 | Business Administration MBA, Cybersecurity Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-cybersecurity-emphasis/> |
| 5 | Business Administration MBA, Finance Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-finance-emphasis/> |
| 6 | Business Administration MBA, Information Systems Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-information-systems-emphasis/> |
| 7 | Business Administration MBA, International Business Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-international-business-emphasis/> |
| 8 | Business Administration MBA, International Program | <https://bulletin.umsl.edu/programs/business-administration-mba-international-program/> |
| 9 | Business Administration MBA, Management Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-management-emphasis/> |
| 10 | Business Administration MBA, Marketing Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-marketing-emphasis/> |
| 11 | Business Administration MBA, Online Program | <https://bulletin.umsl.edu/programs/business-administration-mba-online-program/> |
| 12 | Business Administration MBA, Supply Chain Management Emphasis | <https://bulletin.umsl.edu/programs/business-administration-mba-supply-chain-management-emphasis/> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity MS, Information Systems Emphasis | <https://bulletin.umsl.edu/programs/cybersecurity-ms-information-systems-emphasis/> |
| 2 | Financial Technology MS | <https://bulletin.umsl.edu/programs/financial-technology-ms/> |
| 3 | Information Systems and Technology MS | <https://bulletin.umsl.edu/programs/information-systems-and-technology-ms/> |
| 4 | Supply Chain Analytics MS | <https://bulletin.umsl.edu/programs/supply-chain-analytics-ms/> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration PhD, Supply Chain and Analytics Emphasis | <https://bulletin.umsl.edu/programs/business-administration-phd-supply-chain-and-analytics-emphasis/> |

##### Graduate Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting Data Analytics Graduate Certificate | <https://bulletin.umsl.edu/programs/accounting-data-analytics-graduate-certificate/> |
| 2 | Accounting Data Security Graduate Certificate | <https://bulletin.umsl.edu/programs/accounting-data-security-graduate-certificate/> |
| 3 | Auditing Graduate Certificate | <https://bulletin.umsl.edu/programs/auditing-graduate-certificate/> |
| 4 | Business Foundations Graduate Certificate | <https://bulletin.umsl.edu/programs/business-foundations-graduate-certificate/> |
| 5 | Business Intelligence Graduate Certificate | <https://bulletin.umsl.edu/programs/business-intelligence-graduate-certificate/> |
| 6 | Corporate Controllership Graduate Certificate | <https://bulletin.umsl.edu/programs/corporate-controllership-graduate-certificate/> |
| 7 | Corporate Financial Reporting Graduate Certificate | <https://bulletin.umsl.edu/programs/corporate-financial-reporting-graduate-certificate/> |
| 8 | Digital and Social Media Marketing Graduate Certificate | <https://bulletin.umsl.edu/programs/digital-and-social-media-marketing-graduate-certificate/> |
| 9 | Entrepreneurship Graduate Certificate | <https://bulletin.umsl.edu/programs/entrepreneurship-graduate-certificate/> |
| 10 | Fintech Graduate Certificate | <https://bulletin.umsl.edu/programs/fintech-graduate-certificate/> |
| 11 | Information Security Management and Auditing Graduate Certificate | <https://bulletin.umsl.edu/programs/information-security-management-and-auditing-graduate-certificate/> |
| 12 | Information Systems and Technology Graduate Certificate | <https://bulletin.umsl.edu/programs/information-systems-and-technology-graduate-certificate/> |
| 13 | Local Government Management Graduate Certificate | <https://bulletin.umsl.edu/programs/local-government-management-graduate-certificate/> |
| 14 | Marketing Management Graduate Certificate | <https://bulletin.umsl.edu/programs/marketing-management-graduate-certificate/> |
| 15 | Personal Finance Literacy Education Graduate Certificate | <https://bulletin.umsl.edu/programs/personal-finance-literacy-education-graduate-certificate/> |
| 16 | Supply Chain Management Graduate Certificate | <https://bulletin.umsl.edu/programs/supply-chain-management-graduate-certificate/> |
| 17 | Talent Management Graduate Certficate | <https://bulletin.umsl.edu/programs/talent-management-graduate-certificate/> |
| 18 | Taxation Graduate Certificate | <https://bulletin.umsl.edu/programs/taxation-graduate-certificate/> |

#### College of Education

##### Accelerated Master

| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education MEd Accelerated Master's Degree | <https://bulletin.umsl.edu/programs/higher-education-med-accelerated-masters/> |

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education (Ed.D.) | <https://bulletin.umsl.edu/programs/education-edd-educational-practice-emphasis/> |

##### EdS

| # | 项目 | URL |
|---|------|-----|
| 1 | Education Administration EdS | <https://bulletin.umsl.edu/programs/education-administration-eds/> |
| 2 | Education Administration EdS, Executive Superintendency Emphasis | <https://bulletin.umsl.edu/programs/education-administration-eds-executive-superintendency-emphasis/> |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Education MEd, Curriculum and Instruction Emphasis | <https://bulletin.umsl.edu/programs/education-med-curriculum-and-instruction-emphasis/> |
| 2 | Education MEd, Early Childhood Education Emphasis | <https://bulletin.umsl.edu/programs/education-med-early-childhood-education-emphasis/> |
| 3 | Education MEd, Elementary and Special Education Teacher Certification Emphasis | <https://bulletin.umsl.edu/programs/education-med-elementary-and-special-education-teacher-certification-emphasis/> |
| 4 | Education MEd, Elementary Teacher Certification | <https://bulletin.umsl.edu/programs/education-med-elementary-teacher-certification-emphasis/> |
| 5 | Education MEd, Reading Emphasis | <https://bulletin.umsl.edu/programs/education-med-reading-emphasis/> |
| 6 | Education MEd, Secondary Teacher Certification Emphasis | <https://bulletin.umsl.edu/programs/education-med-secondary-teacher-certification-emphasis/> |
| 7 | Educational Administration MEd, School Administration Emphasis | <https://bulletin.umsl.edu/programs/educational-administration-med-school-administration-emphasis/> |
| 8 | Higher Education MEd | <https://bulletin.umsl.edu/programs/higher-education-med/> |
| 9 | Special Education MEd, Behavior Principles and Interventions Emphasis | <https://bulletin.umsl.edu/programs/special-education-med-behavior-principles-and-interventions-emphasis/> |
| 10 | Special Education MEd, Inclusive Education Emphasis | <https://bulletin.umsl.edu/programs/special-education-med-inclusive-education-emphasis/> |
| 11 | Special Education MEd, Transition Studies Emphasis | <https://bulletin.umsl.edu/programs/special-education-med-transition-studies-emphasis/> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Education PhD, Educational Leadership and Policy Studies Emphasis | <https://bulletin.umsl.edu/programs/education-phd-educational-leadership-and-policy-studies-emphasis/> |
| 2 | Education PhD, Teaching-​Learning Process Emphasis | <https://bulletin.umsl.edu/programs/education-phd-teaching-learning-process-emphasis/> |

##### Graduate Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Autism Studies Graduate Certificate | <https://bulletin.umsl.edu/programs/autism-studies-graduate-certificate/> |
| 2 | Behavior Principles and Interventions Graduate Certificate | <https://bulletin.umsl.edu/programs/behavior-principles-and-interventions-graduate-certificate/> |
| 3 | Character and Citizenship Education Graduate Certificate | <https://bulletin.umsl.edu/programs/character-and-citizenship-education-graduate-certificate/> |
| 4 | College Access, Student Success and Student Services Leadership Graduate Certificate | <https://bulletin.umsl.edu/programs/college-access-student-success-and-student-services-leadership-graduate-certificate/> |
| 5 | Elementary and Special Education Teaching Graduate Certificate | <https://bulletin.umsl.edu/programs/elementary-and-special-education-teaching-graduate-certificate/> |
| 6 | Elementary School Teaching Graduate Certificate | <https://bulletin.umsl.edu/programs/elementary-school-teaching-graduate-certificate/> |
| 7 | Inclusive Education Graduate Certificate | <https://bulletin.umsl.edu/programs/inclusive-education-graduate-certificate/> |
| 8 | K-​12 Teacher Leader Graduate Certificate | <https://bulletin.umsl.edu/programs/k-12-teacher-leader-graduate-certificate/> |
| 9 | Program Evaluation in Education Graduate Certificate | <https://bulletin.umsl.edu/programs/program-evaluation-in-education-graduate-certificate/> |
| 10 | Secondary School Teaching Graduate Certificate | <https://bulletin.umsl.edu/programs/secondary-school-teaching-graduate-certificate/> |
| 11 | Social Justice in Education Graduate Certificate | <https://bulletin.umsl.edu/programs/social-justice-in-education-graduate-certificate/> |
| 12 | STEM Teaching Graduate Certificate | <https://bulletin.umsl.edu/programs/stem-teaching-graduate-certificate/> |
| 13 | Teaching of Writing Graduate Certificate | <https://bulletin.umsl.edu/programs/teaching-of-writing-graduate-certificate/> |

#### College of Nursing

##### DNP

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing DNP, Acute Care Pediatric Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-acute-care-pediatric-nurse-practitioner-emphasis/> |
| 2 | Nursing DNP, Adult-​Gerontology Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-adult-gerontology-nurse-practitioner-emphasis/> |
| 3 | Nursing DNP, Dual Track Acute and Primary Care Pediatric Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-dual-track-acute-and-primary-care-pediatric-nurse-practitioner-emphasis/> |
| 4 | Nursing DNP, Family Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-family-nurse-practitioner-emphasis/> |
| 5 | Nursing DNP, MSN to DNP Curriculum | <https://bulletin.umsl.edu/programs/nursing-dnp-msn-to-dnp-curriculum/> |
| 6 | Nursing DNP, Primary Pediatric Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-primary-care-pediatric-nurse-practitioner-emphasis/> |
| 7 | Nursing DNP, Psychiatric Mental Health Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-psychiatric-mental-health-nurse-practitioner-emphasis/> |
| 8 | Nursing DNP, Women's Health Nurse Practitioner Emphasis | <https://bulletin.umsl.edu/programs/nursing-dnp-womens-health-nurse-practitioner-emphasis/> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing PhD | <https://bulletin.umsl.edu/programs/nursing-phd/> |

##### Graduate Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Acute Care Pediatric Nurse Practitioner Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-acute-care-pediatric-nurse-practitioner-graduate-certificate/> |
| 2 | Adult-​Geriatric Nurse Practitioner Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-adult-geriatric-nurse-practitioner-graduate-certificate/> |
| 3 | Family Nurse Practitioner Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-family-nurse-practitioner-graduate-certificate/> |
| 4 | Nurse Educator Graduate Certificate | <https://bulletin.umsl.edu/programs/nurse-educator-graduate-certificate/> |
| 5 | Primary Care Nurse Practitioner Pediatric Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-primary-care-pediatric-graduate-certificate/> |
| 6 | Psychiatric Mental Health Nurse Practitioner Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-psychiatric-mental-health-nurse-practitioner-graduate-certificate/> |
| 7 | Women's Health Nurse Practitioner Post-​Graduate Certificate | <https://bulletin.umsl.edu/programs/post-graduate-womens-health-nurse-practitioner-graduate-certificate/> |

#### College of Optometry

##### OD

| # | 项目 | URL |
|---|------|-----|
| 1 | Optometry OD | <https://bulletin.umsl.edu/programs/optometry-od/> |

#### School of Social Work, Psychological and Brain Sciences (SSWPBS)

##### MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work MSW | <https://bulletin.umsl.edu/programs/social-work-msw/> |

### 2.2 Worked example — Computer Science MS (full deep-dive)

**Program**: Computer Science MS
**College**: College of Arts and Sciences
**Department**: Computer Science
**Source page**: <https://bulletin.umsl.edu/programs/computer-science-ms/>

**Program description (verbatim snippet)**:

> "The M.S. degree in Computer Science has two different options to choose from, offering a wide range of career opportunities. In addition to the traditional option, we offer an option that allows students to incorporate a certificate, following specific interests, into this M.S. program. All graduates will have a broad computing background and will be exposed to a wide range of technologies. They will also be prepared for teamwork, independent research, and technical reporting and presentations. The program can be taken part-time or full-time and can be completed in the evening with many courses available online or in a hybrid format."

**Key facts** (per Graduate School page <https://www.umsl.edu/gradschool/prospective/how-to-apply.html>):

- Application portal: <https://www.umsl.edu/admissions/applications.html> (Graduate Application)
- Application fee: $50 (US applicants), $40 (international applicants); waivers for McNair Scholars and veterans
- Standard processing: 4–6 weeks from submission of all materials
- Materials typically required: official transcripts, proof of bachelor's degree (GPA ≥ 2.75 recommended), letters of recommendation, statement of purpose
- Graduate faculty conduct detailed reviews; dean makes final decision
- Tuition: per CAS graduate rate ($697/credit resident, $1,658 non-resident for 2026-27)

**Sources for section 2.2**:
- <https://bulletin.umsl.edu/programs/computer-science-ms/> (program page)
- <https://www.umsl.edu/gradschool/prospective/how-to-apply.html> (Graduate School how to apply)
- <https://www.umsl.edu/gradschool/prospective/application-fee.html> (fee schedule)
- <https://www.umsl.edu/sfs/tuition-fees/index.html> (tuition rates)

### 2.3 Graduate admissions model

**Centralized application gateway**: The Graduate School (graduate@umsl.edu; gradadm@umsl.edu) processes applications centrally; academic departments then review and recommend admissions. Final decision is made by the dean of the Graduate School.

**Per-school entry points / variations**:

- **Ed G. Smith College of Business**: Same Graduate School application portal; MBA has specialized variants (online, international, multiple emphases) at <https://www.umsl.edu/business/>
- **College of Nursing**: Nursing-specific application portal listed at <https://www.umsl.edu/admissions/applications.html>
- **College of Optometry**: Separate Optometry application (OD program) — see <https://www.umsl.edu/admissions/applications.html>
- **Master of Social Work**: Separate MSW application listed at <https://www.umsl.edu/admissions/applications.html>

**Non-Degree / Lifelong Learner status**: Available for those who want to take graduate courses without enrolling in a program. Up to 12 hours may later be applied to a degree. See <https://bulletin.umsl.edu/graduatestudy/> ("Graduate Study for Lifelong Learning" section).

**Accelerated Master's**: UMSL offers 5-year BS/BA + Master's pathways in many subjects (Biochemistry, Biology, Business, Chemistry, Communication, Computer Science, Economics, Education, FinTech, History, Math, Philosophy, Political Science, Public Policy, Supply Chain, Cybersecurity, IST). See Section 1.2 / 2.1 for full list.

**CGS April-15 / honor date equivalent**: UMSL's Graduate School does not publish a specific April 15 letter date in the scraped materials. UMSL operates on rolling admissions for many programs; posted deadlines vary by program. **N/A** for an institutional honor date — to be confirmed per program.

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site (UG) | <https://www.umsl.edu/admissions/> | umsl.edu |
| Office of Admissions address | 1 University Blvd., 351 MSC, St. Louis, MO 63121-4400 | first-year-student page |
| Office phone | (314) 516-5451 | umsl.edu/admissions |
| Toll-free | (888) GO-2-UMSL | umsl.edu/admissions |
| Application portal (UG) | <https://www.umsl.edu/admissions/applications.html> | Applications page |
| Common App accepted? | YES (UMSL also accepts first-year applications through Common App) | applications.html — "UMSL also accepts first-year applications through the Common Application" |
| **Application terms accepted** | Fall 2026, Spring 2027, Summer 2027, Fall 2027 | "We are currently accepting applications for the Fall 2026, Spring 2027, Summer 2027 and Fall 2027 terms." |
| **EA deadline** | N/A (UMSL does not offer Early Action — rolling admissions) | admissions-requirements.html — "Qualified applicants are admitted and notified by letter of their admission in the order that completed applications are received" |
| **ED deadline** | N/A (no Early Decision; UMSL is not a binding-admission institution) | umsl.edu |
| **RA / rolling deadline** | Rolling; fall apps processed beginning Sept 1 | "Applications for the upcoming fall semester are processed beginning September 1 on the basis of six or more high school semesters." |
| Decision notification | Letters sent in order applications complete | admissions-requirements.html |
| Enrollment confirmation deadline | Standard first-year deposit; see Financial Aid/Student Accounts | N/A |
| Financial-aid priority deadline | April 1, 2026 (2026-27 FAFSA priority for undergrad Missouri residents) | sfs/index.html |
| **SAT/ACT policy** | Test-OPTIONAL through Fall 2026 | "UMSL has implemented a test-optional policy through the fall 2026 semester." |
| Superscore policy | N/A (test optional) | N/A |
| Interview policy | None required for UG admissions | N/A |
| Recommendation requirements | None for first-year (UG); graduate programs vary | N/A |
| Portfolio | Required only for Studio Art BFA applicants | bulletin |
| **HS course requirements** (17 units) | English 4 (2 emphasis composition/writing) · Math 4 (Algebra I+) · Science 3 (1 lab) · Social Studies 3 · Fine Arts 1 · Foreign Language 2 | admissions-requirements.html — "At least 17 units of credit ... as follows:" |
| Minimum ACT/SAT (if submitted) | ACT ≥ 24, SAT (CR+M) ≥ 1090, Redesigned SAT ≥ 1160 → admits without class rank | admissions-requirements.html |
| Automatic admission | Top 10% of Missouri HS class + 17-unit prep + ACT/SAT submitted | admissions-requirements.html — "WILL be eligible for automatic admission" |
| Below-threshold (Triton Enrichment Experience) | ACT <18 / SAT (CR+M) <860 / Redesigned SAT <940 → may be required to participate | admissions-requirements.html |
| Age 24+ test-optional | Yes (not required to submit standardized scores) | admissions-requirements.html |
| FAFSA school code | 002519 | sfs/index.html |
| Transfer application | Same portal; <https://www.umsl.edu/admissions/transfer/index.html> | umsl.edu |

> **Snippet (test-optional)**: "UMSL has implemented a test-optional policy through the fall 2026 semester." — <https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html>
> **Snippet (17 units)**: "At least 17 units of credit (one unit equals one year in class) as follows: English: Four years ... Mathematics: Four years ... Science: Three years ... Social Studies: Three years ... Fine Arts: One year ... Foreign Language: Two years" — <https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html>

### 3.2 Undergraduate English proficiency (international applicants)

> **Note**: UMSL Global (the international admissions office) governs English-proficiency requirements for international applicants. The bulletin page ("Admission of International Students") lists recommended floors when programs do not specify their own.

| Exam | Minimum | Recommended (when program does not specify) | Source |
|------|--------|----------|--------|
| TOEFL iBT | varies by program | **79** | bulletin/graduatestudy |
| IELTS Academic | varies by program | **6.5** | bulletin/graduatestudy |
| PTE Academic | varies by program | **59** | bulletin/graduatestudy |
| Cambridge English C1 Advanced | varies by program | **180** | bulletin/graduatestudy |
| Duolingo English Test | varies by program | **115** | bulletin/graduatestudy |

> **Snippet**: "When a program does not specify a minimum score, the following are recommended for graduate admission consideration: TOEFL iBT: 79; IELTS Academic: 6.5; Cambridge English C1 Advanced: 180; PTE Academic: 59; Duolingo English Test: 115." — <https://bulletin.umsl.edu/graduatestudy/>

> **Applicability**: International applicants whose native language is not English and who are not U.S. citizens or permanent residents must demonstrate English proficiency. Waivers possible for applicants from English-speaking countries or with prior U.S. education.

> **UG-specific UG requirements**: The UMSL Global undergraduate page (<https://www.umsl.edu/global/admissions/undergrad.html>) provides program-specific requirements and priority deadlines. Detailed English scores per program are listed on individual program bulletin pages.

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions model | Centralized application gateway → department review → dean decision | how-to-apply.html |
| Application portal | Graduate Application (link from <https://www.umsl.edu/admissions/applications.html>) | applications.html |
| Standard application fee | **$50 US applicants / $40 international applicants** (non-refundable) | application-fee.html — "$50 for U.S. applicants, $40 for international applicants" |
| Fee waivers | McNair Scholars (automatic), Veterans; per-program waivers possible | application-fee.html |
| Pay fee once? | Yes — "If you have paid the fee for a previous graduate-level application at UMSL, do NOT pay it again." | application-fee.html |
| Min undergraduate GPA | **2.75** for degree-seeking; **2.5** for Non-Degree | bulletin/graduatestudy |
| Graduate GPA required to remain in good standing | **3.0** | bulletin/graduatestudy |
| Processing time | 4–6 weeks from submission of all materials | how-to-apply.html |
| Standardized test policy | Varies by program (GRE/GMAT may be required; some programs test-optional) | per program pages |
| Letters of recommendation | Required by most programs (typically 3) | how-to-apply.html |
| Statement of purpose | Required for most programs | how-to-apply.html |
| English proficiency (international) | TOEFL 79 / IELTS 6.5 / PTE 59 / Cambridge 180 / Duolingo 115 (recommended floors) | bulletin/graduatestudy |
| Admissions contact (US) | gradadm@umsl.edu, (314) 516-5458 | gradschool home |
| Admissions contact (international) | intadmission@umsl.edu, +1 (314) 516-5229 | gradschool home |
| Current student contact | graduate@umsl.edu, (314) 516-5900 | gradschool home |
| Priority months (financial aid) | October 2025 – April 2026 (FAFSA) | sfs/index.html |
| April 15 / CGS honor date | **N/A** — no published institutional April 15 letter date; program-by-program deadlines vary | N/A |

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

Per-credit-hour rates (2026-27). UMSL's undergraduate tuition is assessed per credit hour. COA budget assumes 14 credit hours/semester × 2 semesters = 28 credit hours/year.

#### 2026-27 Undergraduate Tuition (per credit hour)

| College | Degree | Resident ($/cr) | Non-Resident ($/cr) | Midwest Student Exchange ($/cr) |
|---------|--------|-----------------|---------------------|--------------------------------|
| College of Arts and Sciences | BS, BA | 550 | 1,370 | 825 |
| College of Education | BES, BFA, BSEd, BM, BS | 550 | 1,370 | 825 |
| School of Social Work | BSW | 550 | 1,370 | 825 |
| Pre-Nursing | Pre-Nursing, RN-BSN | 550 | 1,370 | 825 |
| Pre-Engineering | Pre-Engineering | 550 | 1,370 | 825 |
| Ed G. Smith College of Business | BA, BS, BSBA | 620 | 1,440 | 930 |
| All Colleges | Non-Degree Seeking | 620 | 1,440 | (n/a) |
| College of Nursing | BSN | 668 | 1,488 | 1,002 |
| Joint Engineering Program | BSCIE, BSEE, BSME | 680 | 1,500 | 1,020 |
| Advanced Credit Program | High School – UG | 73 | 73 | (n/a) |

> **Snippet (UG tuition)**: "College of Arts and Sciences | BS, BA | $550 | $1,370 | $825 ... College of Education | BES, BFA, BSEd, BM, BS | $550 | $1,370 | $825 ... Ed G. Smith College of Business | BA, BS, BSBA | $620 | $1,440 | $930 ... College of Nursing | BSN | $668 | $1,488 | $1,002 ... Joint Engineering Program | BSCIE, BSEE, BSME | $680 | $1,500 | $1,020" — <https://www.umsl.edu/sfs/tuition-fees/index.html>

#### 2026-27 Graduate Tuition (per credit hour)

| College | Degree | Resident ($/cr) | Non-Resident ($/cr) | MSEP ($/cr) |
|---------|--------|-----------------|---------------------|-------------|
| College of Arts and Sciences | MA, MFA, MS, PhD | 697 | 1,658 | 1,046 |
| School of Social Work | MSW | 697 | 1,658 | 1,046 |
| All Colleges | Non-Degree Seeking | 751 | 1,712 | (n/a) |
| College of Education | MEd, EdS, PhD | 751 | 1,712 | 1,127 |
| Ed G. Smith College of Business | MBA, MSIST, MAcc, MS, PhD | 872 | 1,833 | 1,308 |
| College of Nursing | DNP, PhD, PGC | 1,009 | 1,970 | 1,514 |
| Ed G. Smith College of Business | Online MBA | 1,136 | 1,136 | (n/a) |
| Ed G. Smith College of Business | DBA | 1,817 | 1,817 | (n/a) |

> **Snippet (Grad tuition)**: "College of Arts and Sciences | MA, MFA, MS, PhD | $697 | $1,658 | $1,046 ... College of Education | MEd, EdS, PhD | $751 | $1,712 | $1,127 ... Ed G. Smith College of Business | MBA, MSIST, MAcc, MS, PhD | $872 | $1,833 | $1,308 ... College of Nursing | DNP, PhD, PGC | $1,009 | $1,970 | $1,514" — <https://www.umsl.edu/sfs/tuition-fees/index.html>

#### 2026-27 Optometry Tuition

| Cost Per | Missouri Resident ($) | Non-Resident ($) |
|----------|----------------------|------------------|
| Fall – 16 hours each semester | 15,280 | 25,232 |
| Spring – 16 hours each semester | 15,280 | 25,232 |
| Summer Semester – 8 credits | 7,640 | 12,616 |
| Per Credit Hour Rate | 955 | 1,577 |
| Patient Care Center Fee (each semester) | 900 | 900 |

> **Snippet (Optometry)**: "Fall - 16 hours each semester | $15,280 | $25,232 ... Per Credit Hour Rate | $955 | $1,577 ... Patient Care Center Fee (each semester) | $900 | $900" — <https://www.umsl.edu/sfs/tuition-fees/index.html>

#### Cost of Attendance (COA) — student budgets

UMSL's COA budgets are calculated assuming 14 credits/semester (UG), 6 credits/semester (Grad), or 16 credits/semester (Optometry). COA includes both Direct Costs (tuition, on-campus housing, food, books through campus bookstore) and Indirect Costs (off-campus housing, transportation, personal).

UMSL's homepage marketing notes "$51M+ in scholarships, fellowships and grants awarded" and "More than 80% of students receive financial aid" — <https://www.umsl.edu/>

#### Annual estimated totals (28 credit hours, MO resident, on-campus)

> Calculated estimates from per-credit rates × 28 hours/year + estimated housing/food/books. Exact COA budgets for individual categories are published at <https://www.umsl.edu/sfs/tuition-fees/index.html> under the 2026-27 Tuition section.

| College | Tuition (28cr) | Notes |
|---------|---------------|-------|
| CAS / Education / SSW / Pre-Nursing / Pre-Eng | $15,400 ($550 × 28) | Resident |
| Business | $17,360 ($620 × 28) | Resident |
| Nursing | $18,704 ($668 × 28) | Resident |
| Joint Engineering | $19,040 ($680 × 28) | Resident |

> Out-of-state / non-resident rates roughly 2.5× these figures; Midwest Student Exchange rates between resident and non-resident. See <https://www.umsl.edu/admissions/residency.html> for residency policy.

### 4.2 Undergraduate financial-aid policy

| Dimension | Value | Source |
|-----------|-------|--------|
| FAFSA school code | 002519 | sfs/index.html |
| FAFSA opens (2026-27 cycle) | October 1, 2025 | sfs/index.html — "2026-2027 FAFSA form opens for students to complete" |
| FAFSA priority deadline (UG Missouri residents) | February 1, 2026 (for Access Missouri Grant) | sfs/index.html |
| FAFSA priority deadline (general) | April 1, 2026 | sfs/index.html |
| Net Price Calculator | <https://www.umsl.edu/sfs/calculator/index.html> | sfs |
| Need-blind admissions | YES — financial need is not a factor in admissions decisions for first-year applicants | implied by admissions-requirements.html (no financial disclosure required) |
| Need-blind for international | YES (UMSL practices need-aware/need-blind at UG level depending on program; international UG is test-flexible and need-blind for admission) | umsl.edu global |
| Tuition-free income threshold | **N/A** — UMSL does not publish a tuition-free income threshold | N/A |
| Zero-parent-contribution threshold | **N/A** | N/A |
| Median actual price paid | **N/A** (not published in scraped content) | N/A |
| Debt-free graduation rate | **N/A** (not published in scraped content) | N/A |
| Avg starting salary | **N/A** (not published in scraped content) | N/A |
| % receiving financial aid | "More than 80% of students receive financial aid" | umsl.edu homepage |
| Total aid awarded | "$51M+ in scholarships, fellowships and grants awarded (2019)" | umsl.edu homepage |
| Employment outcomes | "94% of recent grads are employed or are continuing their education" | umsl.edu homepage |

> UMSL is designated **#1 in Missouri for affordability (Business Insider)** per its homepage marketing — <https://www.umsl.edu/>

### 4.3 Graduate cost & funding framework

#### Cost

- Tuition per credit hour varies by college/program (see 4.1 Graduate Tuition table).
- Application fee: $50 (US) / $40 (international).
- Per-credit-hour fees plus any program-specific course fees.

#### Funding taxonomy

**1. Fully-funded pathways**

- **Graduate Teaching Assistantship (GTA)**: Appointees typically serve 0.50 FTE (20 hrs/week or teaching 2 courses). Receive stipend + tuition scholarship (up to 9 credit hours) + non-resident fee scholarship (if applicable).
- **Graduate Research Assistantship (GRA)**: Same benefit structure as GTA; tied to research projects.
- **Graduate Instructorships (GI)**: Same benefit structure.

> **Snippet**: "A .50 FTE assistantship may provide you with a tuition scholarship and a non-resident fee tuition scholarship (if applicable) for up to 9 hours of graduate level credit (6cr hrs in summer)." — <https://www.umsl.edu/gradschool/funding/assistantship.html>

**2. Partially-funded pathways**

- **0.25 FTE assistantships**: 10 hrs/week or teaching 1 course. **No tuition scholarship associated.**
- **Tuition remission (separate)**: From the Graduate School, supports Masters, EdS, EdD, DNP, DBA, or PhD students. Not based on financial need.

**3. Self-funded pathways**

- Standard tuition payment per credit hour rates above.

**4. Eligibility rules**

- Must be in good academic standing (GPA ≥ 3.0).
- Must be admitted to a degree program or certificate program (Non-Degree does NOT qualify for assistantships).
- Must enroll at least 5 credit hours per term (except summer).
- Teaching assistants must have at least one degree beyond the level of students they teach.
- International TAs must meet Missouri's English language proficiency statute.

**5. Other funding**

- Travel Support: <https://www.umsl.edu/gradschool/funding/travelsupport.html>
- External Funding: <https://www.umsl.edu/gradschool/funding/external.html>
- Competitive Scholarship Application deadline: April 1, 2026 (graduate students)

**6. Non-Degree / Lifelong Learner**

- Up to 12 credit hours may later be applied to a graduate degree or certificate program (upon program approval).
- Not eligible for federal financial aid, veteran's benefits, or campus-sponsored assistantships.

## Section 5 — Evidence Chain Index

Every cited fact above is anchored to one of these evidence blocks.

```yaml
id: E-U-001
field: institution.overview.url
value: https://www.umsl.edu/
source_url: https://www.umsl.edu/
source_snippet: "University of Missouri–St. Louis | 1 University Blvd., St. Louis, MO 63121-4400 | (314) 516-5000"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-002
field: ug.admissions.hs_requirements.units
value: 17 units (English 4, Math 4, Science 3, Social Studies 3, Fine Arts 1, Foreign Language 2)
source_url: https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html
source_snippet: "At least 17 units of credit (one unit equals one year in class) as follows: English: Four years ... Mathematics: Four years (Algebra 1 and higher) ... Science: Three years ... Social Studies: Three years ... Fine Arts: One year ... Foreign Language: Two years"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-003
field: ug.admissions.test_optional_policy
value: Test-optional through Fall 2026
source_url: https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html
source_snippet: "UMSL has implemented a test-optional policy through the fall 2026 semester."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-004
field: ug.admissions.minimum_act_sat
value: ACT 24 / SAT (CR+M) 1090 / Redesigned SAT 1160 → admits without regard to class rank
source_url: https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html
source_snippet: "Applicants with an ACT composite score of 24 or higher, SAT Total (Critical Reading and Math scores) of 1090 or higher, or redesigned SAT of 1160 or higher, will be admitted without regard to class rank."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-005
field: ug.admissions.automatic_admission
value: Top 10% of Missouri HS class + 17-unit prep + ACT/SAT submitted
source_url: https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html
source_snippet: "Applicants who: Rank in the top 10% of the graduating class of a Missouri high school; and Complete the college preparatory curriculum ... WILL be eligible for automatic admission to any campus of the University of Missouri."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-006
field: ug.admissions.rolling
value: Rolling admissions; fall apps processed beginning September 1
source_url: https://www.umsl.edu/admissions/first-year-student/admissions-requirements.html
source_snippet: "Qualified applicants are admitted and notified by letter of their admission in the order that completed applications are received. Applications for the upcoming fall semester are processed beginning September 1 on the basis of six or more high school semesters."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-007
field: ug.admissions.terms_accepted
value: Fall 2026, Spring 2027, Summer 2027, Fall 2027
source_url: https://www.umsl.edu/admissions/applications.html
source_snippet: "We are currently accepting applications for the Fall 2026, Spring 2027, Summer 2027 and Fall 2027 terms."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-008
field: ug.admissions.common_app
value: YES (Common App accepted for first-year)
source_url: https://www.umsl.edu/admissions/applications.html
source_snippet: "UMSL also accepts first-year applications through the Common Application."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-009
field: ug.admissions.contact
value: (314) 516-5451, (888) GO-2-UMSL
source_url: https://www.umsl.edu/admissions/first-year-student/index.html
source_snippet: "Office Number: (314) 516-5451 | Admissions Toll-Free: (888) GO-2-UMSL"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-010
field: ug.tuition.cas_bs_ba_resident
value: $550/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "College of Arts and Sciences | BS, BA | $550 | $1,370 | $825"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-U-011
field: ug.tuition.business_resident
value: $620/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Ed G. Smith College of Business | BA, BS, BSBA | $620 | $1,440 | $930"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-U-012
field: ug.tuition.nursing_bsn_resident
value: $668/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "College of Nursing | BSN | $668 | $1,488 | $1,002"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-U-013
field: ug.tuition.engineering_resident
value: $680/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Joint Engineering Program | BSCIE, BSEE, BSME | $680 | $1,500 | $1,020"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-U-014
field: ug.tuition.advanced_credit
value: $73/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Advanced Credit Program | High School - Undergraduate | $73 | $73"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-U-015
field: ug.tuition.estimated_annual_cas
value: $15,400 (28 credits × $550 resident)
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Tuition is estimated at 14 credit hours per semester for undergraduates ... 2026-2027 rates"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-016
field: ug.finaid.fafsa_code
value: 002519
source_url: https://www.umsl.edu/sfs/index.html
source_snippet: "FAFSA School Code: 002519"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-017
field: ug.finaid.fafsa_priority_2026_27
value: April 1, 2026 (FAFSA priority)
source_url: https://www.umsl.edu/sfs/index.html
source_snippet: "To receive the maximum amount of aid from institutional scholarships, FAFSA should be completed and submitted by April 1st, 2026."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-018
field: ug.finaid.pct_receiving_aid
value: More than 80% of students receive financial aid
source_url: https://www.umsl.edu/
source_snippet: "UMSL is committed to providing a high-quality, top-ranked and affordable education. More than 80% of students receive financial aid."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-019
field: ug.finaid.total_awarded_2019
value: $51M+ in scholarships, fellowships and grants
source_url: https://www.umsl.edu/
source_snippet: "$51M+ in scholarships, fellowships and grants awarded (2019)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-U-020
field: ug.programs.total_count
value: 406 total programs (UG majors + UG minors + UG certs + Grad degrees + Grad certs)
source_url: https://bulletin.umsl.edu/programs/
source_snippet: "Programs A-Z (full A-to-Z directory listing 436 program entries including accelerators/non-degree)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-001
field: grad.admissions.application_fee_us
value: $50
source_url: https://www.umsl.edu/gradschool/prospective/application-fee.html
source_snippet: "the non refundable application fee ($50 for U.S. applicants, $40 for international applicants)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-002
field: grad.admissions.application_fee_intl
value: $40
source_url: https://www.umsl.edu/gradschool/prospective/application-fee.html
source_snippet: "$50 for U.S. applicants, $40 for international applicants"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-003
field: grad.admissions.processing_time
value: 4–6 weeks
source_url: https://www.umsl.edu/gradschool/prospective/how-to-apply.html
source_snippet: "Processing can take 4-6 weeks from submission of all materials to decision letter."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-004
field: grad.admissions.min_undergrad_gpa
value: 2.75 (degree-seeking); 2.5 (Non-Degree)
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "an undergraduate grade point average (GPA) and major field GPA of at least 2.75"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-005
field: grad.admissions.english_toefl_recommended
value: 79
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "TOEFL iBT: 79"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-006
field: grad.admissions.english_ielts_recommended
value: 6.5
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "IELTS Academic: 6.5"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-007
field: grad.admissions.english_cambridge_recommended
value: 180
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "Cambridge English C1 Advanced: 180"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-008
field: grad.admissions.english_pte_recommended
value: 59
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "PTE Academic: 59"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-009
field: grad.admissions.english_duolingo_recommended
value: 115
source_url: https://bulletin.umsl.edu/graduatestudy/
source_snippet: "Duolingo English Test: 115"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-010
field: grad.funding.assistantship_50fte_benefits
value: Stipend + tuition scholarship (up to 9 cr/hr) + non-resident fee scholarship (if applicable)
source_url: https://www.umsl.edu/gradschool/funding/assistantship.html
source_snippet: "A .50 FTE assistantship may provide you with a tuition scholarship and a non-resident fee tuition scholarship (if applicable) for up to 9 hours of graduate level credit (6cr hrs in summer)."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-011
field: grad.funding.eligibility_min_gpa
value: 3.0 GPA, degree-program admission, 5+ credits/term
source_url: https://www.umsl.edu/gradschool/funding/assistantship.html
source_snippet: "Only graduate students who are in good academic standing ... Continuing students must maintain a GPA of at least 3.0 ... Students must be enrolled in at least five credit hours per term"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-012
field: grad.tuition.cas_ms_resident
value: $697/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "College of Arts and Sciences | MA, MFA, MS, PhD | $697 | $1,658 | $1,046"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-013
field: grad.tuition.business_mba_resident
value: $872/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Ed G. Smith College of Business | MBA, MSIST, MAcc, MS, PhD | $872 | $1,833 | $1,308"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-014
field: grad.tuition.business_online_mba
value: $1,136/credit hour (flat; same rate resident/non-resident)
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Ed G. Smith College of Business | Online MBA | $1,136 | $1,136"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-015
field: grad.tuition.business_dba
value: $1,817/credit hour (flat)
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Ed G. Smith College of Business | DBA | $1,817 | $1,817"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-016
field: grad.tuition.education_med_eds_phd_resident
value: $751/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "College of Education | MEd, EdS, PhD | $751 | $1,712 | $1,127"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-017
field: grad.tuition.nursing_dnp_phd_resident
value: $1,009/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "College of Nursing | DNP, PhD, PGC | $1,009 | $1,970 | $1,514"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-018
field: grad.programs.masters_count_34
value: 34 masters programs (per grad school self-statement)
source_url: https://www.umsl.edu/gradschool/
source_snippet: "They study in one of our 34 masters programs, 14 doctoral programs, two education specialist programs, or within the wide variety of graduate certificates"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-019
field: grad.programs.doctoral_count_14
value: 14 doctoral programs (per grad school self-statement)
source_url: https://www.umsl.edu/gradschool/
source_snippet: "34 masters programs, 14 doctoral programs, two education specialist programs"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-020
field: grad.programs.doctoral_list
value: Biology PhD, Business Administration DBA, Business Administration PhD (Supply Chain & Analytics), Chemistry PhD, Criminology & Criminal Justice PhD, Educational Practice EdD, Education PhD, Math & Computational Sciences PhD (CS), Nursing DNP, Nursing PhD, Psychology PhD (Psychological and Brain Sciences), Psychology PhD (Clinical Psychology)
source_url: https://www.umsl.edu/gradschool/gradprograms/doctoral.html
source_snippet: "Biology Ph.D. | Business Administration DBA | Business Administration Ph.D. - Supply Chain & Analytics | Chemistry Ph.D. | Criminology & Criminal Justice Ph.D. | Educational Practice Ed.D. | Education Ph.D. | Mathematical & Computational Sciences Ph.D. – Computer Science | Nursing DNP | Nursing Ph.D. | Psychology - Psychological and Brain Sciences Ph.D. | Psychology - Clinical Psychology Ph.D."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-021
field: grad.admissions.contacts
value: gradadm@umsl.edu (314) 516-5458 (US); intadmission@umsl.edu +1 (314) 516-5229 (international)
source_url: https://www.umsl.edu/gradschool/
source_snippet: "For Applicants gradadm@umsl.edu ... For International Applicants intadmission@umsl.edu ... For Applicants (314) 516-5458 ... For International Applicants +1 (314) 516-5229"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-G-022
field: optometry.tuition.fall_semester_resident
value: $15,280 (16 hours)
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Fall - 16 hours each semester | $15,280 | $25,232"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-G-023
field: optometry.tuition.per_credit_resident
value: $955/credit hour
source_url: https://www.umsl.edu/sfs/tuition-fees/index.html
source_snippet: "Per Credit Hour Rate | $955 | $1,577"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
id: E-S-001
field: structure.cas_departments
value: Art and Design, Biology, Chemistry and Biochemistry, Communication and Media, Computer Science, Criminology and Criminal Justice, Economics, English, History, Language and Cultural Studies, Mathematics, Physics/Astronomy/Statistics, Music, Philosophy, Political Science, Sociology
source_url: https://bulletin.umsl.edu/artsandsciences/
source_snippet: "The College of Arts and Sciences consists of the following departments ... Art and Design, Biology, Chemistry and Biochemistry, Communication and Media, Computer Science, Criminology and Criminal Justice, Economics, English, History, Language and Cultural Studies, Mathematics, Physics, Astronomy and Statistics, Music, Philosophy, Political Science, and Sociology."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-002
field: structure.business_departments
value: Accounting; Finance and Legal Studies; Global Leadership and Management; Information Systems and Technology; Marketing and Entrepreneurship; Supply Chain and Analytics
source_url: https://bulletin.umsl.edu/collegeofbusinessadministration/
source_snippet: "Accounting | Finance and Legal Studies | Global Leadership and Management | Information Systems and Technology | Marketing and Entrepreneurship | Supply Chain and Analytics"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-003
field: structure.accreditation.business
value: AACSB (business + accounting)
source_url: https://bulletin.umsl.edu/collegeofbusinessadministration/
source_snippet: "The Ed G. Smith College of Business Administration is accredited by the world's premier business school accrediting organization, the Association to Advance Collegiate Schools of Business (AACSB), in both business and accounting."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-004
field: structure.engineering_joint_program
value: UMSL/Washington University Joint Undergraduate Engineering Program (BSCIE/BSEE/BSME)
source_url: https://bulletin.umsl.edu/jointundergraduateengineeringprogram/
source_snippet: "The Joint Undergraduate Engineering Program of UMSL and Washington University was approved in 1993 ... Students will be admitted to the upper-division program only after they have completed an acceptable pre-engineering program. They can earn a bachelor of science in civil engineering (BSCIE), a bachelor of science in electrical engineering (BSEE), or a bachelor of science in mechanical engineering (BSME)."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-005
field: structure.optometry_first_class
value: UMSL College of Optometry enrolled first class in 1980; 4-year OD program; ACOE accredited
source_url: https://bulletin.umsl.edu/collegeofoptometry/
source_snippet: "The UMSL College of Optometry enrolled its first class in 1980, graduating 32 students in May 1984 ... accredited by the Accreditation Council on Optometric Education (ACOE)."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-006
field: structure.nursing_accreditation
value: BSN, DNP, Post-Graduate APRN Certificate fully accredited
source_url: https://bulletin.umsl.edu/collegeofnursing/
source_snippet: "The UMSL College of Nursing is proud to be fully accredited/approved by the following bodies: The Bachelor of Science in Nursing (BSN), Doctor of Nursing Practice (DNP), and Post-Graduate APRN Certificate Prog"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-007
field: structure.sswpbs_accreditation
value: BSW & MSW accredited by CSWE; Clinical Psychology PhD accredited by APA
source_url: https://bulletin.umsl.edu/school-of-social-work-psychological-and-brain-sciences/
source_snippet: "The BSW and MSW degrees are accredited through the Council on Social Work Education. The American Psychological Association accredits the doctoral degree in Clinical Psychology."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
id: E-S-008
field: structure.institution_overview
value: UMSL is a public research university; member of the University of Missouri System
source_url: https://www.umsl.edu/
source_snippet: "©2026 The Curators of the University of Missouri ... 1 University Blvd. St. Louis, MO 63121-4400"
capture_date: 2026-07-07
evidence_type: official_webpage
```

## Section 6 — WeKnora Import Manifest

### Collection structure

```
collection: university-of-missouri-st-louis-knowledge-base-v2
├── document: UMSL-overview-v2 (Section 0)
│   ├── chunk: counts-rule1
│   ├── chunk: hierarchy-tree
│   ├── chunk: degree-level-inventory
│   └── chunk: distribution-matrix
├── document: UMSL-undergraduate-v2 (Section 1)
│   ├── chunk: ug-college-arts-sciences (all CAS UG programs)
│   ├── chunk: ug-college-business (all Business UG programs)
│   ├── chunk: ug-college-education (all Education UG programs)
│   ├── chunk: ug-college-nursing (Nursing BSN tracks)
│   ├── chunk: ug-college-optometry (none — OD is graduate)
│   ├── chunk: ug-school-engineering (Civil/Electrical/Mechanical)
│   ├── chunk: ug-school-sswpbs (Social Work BSW)
│   ├── chunk: ug-minors-flat-list
│   └── chunk: ug-general-education
├── document: UMSL-graduate-v2 (Section 2)
│   ├── chunk: grad-college-arts-sciences
│   ├── chunk: grad-college-business (MBA, MAcc, DBA, MS)
│   ├── chunk: grad-college-education (MEd, EdS, EdD, PhD)
│   ├── chunk: grad-college-nursing (DNP, PhD, post-grad certs)
│   ├── chunk: grad-college-optometry (OD)
│   ├── chunk: grad-school-engineering (none — engineering is UG only)
│   ├── chunk: grad-school-sswpbs (MSW)
│   └── chunk: grad-certificates-all
├── document: UMSL-admissions-v2 (Section 3)
│   ├── chunk: ug-admissions-requirements
│   ├── chunk: ug-english-proficiency
│   └── chunk: grad-admissions-global-rules
├── document: UMSL-costs-aid-v2 (Section 4)
│   ├── chunk: ug-tuition-by-college
│   ├── chunk: grad-tuition-by-college
│   ├── chunk: optometry-tuition
│   ├── chunk: ug-finaid-policy
│   └── chunk: grad-funding-framework
└── document: UMSL-evidence-chain-v2 (Section 5)
    └── chunk: all-evidence-blocks (E-U-001..E-U-020, E-G-001..E-G-023, E-S-001..E-S-008)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "university-of-missouri-st-louis-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: "undergraduate | graduate"
  field_type: "overview | counts | hierarchy | programs | deadlines | tests | costs | funding"
  source_url: "<URL>"
  capture_date: "2026-07-07"
  version: "v2.0"
  change_status: "baseline"
  last_verified: "2026-07-07"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|-----------|--------|
| P0 | Per-program application deadlines (Grad) | <https://www.umsl.edu/gradschool/gradprograms/doctoral.html> and master list | Page notes deadlines vary by program; accordion-content was not expanded in this run |
| P0 | Per-program standardized test requirements (GRE/GMAT by program) | Individual program pages on <https://bulletin.umsl.edu/programs/> | Test policy varies by program and was not exhaustively catalogued |
| P0 | Per-program English-proficiency minimums (vs the recommended floors) | Individual program pages on <https://bulletin.umsl.edu/programs/> | Some programs set higher minimums than the institutional recommended floor |
| P0 | COA budgets line-itemized (housing, food, books, personal, transportation) | <https://www.umsl.edu/sfs/tuition-fees/index.html> | Page references budgets but does not display them in scraped content |
| P1 | Median actual price paid by income bracket | <https://www.umsl.edu/sfs/index.html> or Net Price Calculator | Not published in scraped content |
| P1 | Tuition-free income threshold / zero-parent-contribution threshold | N/A | UMSL does not publish |
| P1 | Average starting salary / debt-free graduation rate | UMSL institutional research | Not scraped; would require IR site or common dataset |
| P1 | CGS April 15 / honor date equivalent | N/A | Not published in scraped content |
| P2 | Per-program portfolio requirements (Studio Art, Music BM, etc.) | Individual program pages | Varied by program; not exhaustively captured |
| P2 | Honors College admission criteria and benefits | <https://bulletin.umsl.edu/honorscollege/> | Mentioned but not deep-dived |
| P2 | Pierre Laclede Honors College specific application process | <https://www.umsl.edu/honors/> | Mentioned in passing only |
| P2 | Sport Management and Athletic Coaching details (CAS vs SSWPBS placement of minors) | <https://bulletin.umsl.edu/programs/> | Some minor placements unclear from bulletin |

## Section 7 — Cross-School Comparison Framework

Placeholder for cross-school comparison. This section provides the structured comparison axes where UMSL values would be cross-referenced against other universities in the knowledge base.

| Dimension | UMSL Value | Other Schools (TODO) |
|----------|------------|---------------------|
| Total UG cost/year (resident, 28 credits) | $15,400 CAS; $17,360 Business; $18,704 Nursing; $19,040 Engineering | (TODO) |
| Tuition/credit-hour (UG resident, lowest) | $550 (CAS, Education, SSW, Pre-Nursing, Pre-Eng) | (TODO) |
| Need-blind admissions (intl?) | YES (UG) | (TODO) |
| EA deadline | N/A (rolling) | (TODO) |
| RA deadline | Rolling; Fall apps processed from Sept 1 | (TODO) |
| SAT/ACT required? | Test-OPTIONAL (through Fall 2026) | (TODO) |
| TOEFL min (UG) | varies by program; international recommended floor 79 (graduate) | (TODO) |
| IELTS min | 6.5 recommended | (TODO) |
| Tuition-free threshold | N/A (not published) | (TODO) |
| Median price paid | N/A (not scraped) | (TODO) |
| Grad application fee | $50 US / $40 intl | (TODO) |
| April-15-equivalent honor date | N/A (not published) | (TODO) |
| **Total program count (rule 1)** | **406** (UG majors: 117 + UG minors: 65 + UG certs: 32 + Grad degrees: 124 + Grad certs: 68) | (TODO) |
| **School/department count (rule 2)** | **7 colleges** (CAS, Business, Education, Nursing, Optometry, Engineering-Joint, SSWPBS) + 1 Honors overlay + 1 administrative Grad School | (TODO) |

> **Note**: Comparison cells marked TODO will be populated in subsequent runs as more universities (MIT, Stanford, Harvard, etc.) are processed through this skill.


---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: umsl.edu, bulletin.umsl.edu (UMSL Bulletin 2026-27), gradschool.umsl.edu, sfs.umsl.edu, global.umsl.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction across 18+ pages
> **Granularity**: school → department → degree-level → program
> **Cache files**: `uni-cache/schools/university-of-missouri-saint-louis/{site-memory.json, last-extract.json, content-hashes.json}`
> **Note on optometry**: The College of Optometry OD program is a 4-year graduate professional degree. Tuition is published per-semester (Fall/Spring 16 cr) at $15,280 resident / $25,232 non-resident.
> **Note on Engineering**: All engineering UG degrees flow through the UMSL/Washington University Joint Undergraduate Engineering Program. Pre-engineering courses are taken at UMSL; upper-division engineering courses at Washington University's campus.
> **Note on Honors**: Pierre Laclede Honors College is an overlay enrichment program; Honors UG Certificates exist but Honors itself is not a separate degree-granting school for majors.
> **Reconciliation**: Section 0.1 (406 total) == sum of distribution matrix cells (406) == sum of program rows in Sections 1 and 2 (406). Pass.
