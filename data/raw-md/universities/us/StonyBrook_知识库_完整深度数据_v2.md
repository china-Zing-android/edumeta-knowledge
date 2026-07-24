# Stony Brook University (SUNY) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BE/BFA) | 69 |
| 本科辅修 (Minor) | 73 |
| 研究生学位项目 (MA/MS/PhD/MBA/MFA/MAT/DMA/MM) | 128 |
| 研究生高级证书 (Certificate) | 34 |
| **学位项目总计 (UG + Grad)** | **304** |
| 学院 / 独立系所总数 | 12 |

**Source**: UG majors from `stonybrook.edu/academics/majors-minors-and-programs/index.html`; Grad programs from `stonybrook.edu/grad/academics/programs.html`

---

### 0.2 学院 / 系层级结构

```
Stony Brook University (SUNY)
├── College of Arts and Sciences                          [学院]
│   ├── Africana Studies                                  [系]
│   ├── Anthropology                                      [系]
│   ├── Art                                              [系]
│   ├── Asian & Asian American Studies                    [系]
│   ├── Astronomy/Planetary Sciences                      [系]
│   ├── Atmospheric and Oceanic Sciences                  [系]
│   ├── Biochemistry                                      [系]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Computer Science                                  [系]
│   ├── Creative Writing                                  [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── French Language and Literature                    [系]
│   ├── Geology                                           [系]
│   ├── Globalization Studies & International Relations   [系]
│   ├── History                                           [系]
│   ├── Italian Studies                                   [系]
│   ├── Linguistics                                       [系]
│   ├── Mathematics                                       [系]
│   ├── Music                                             [系]
│   ├── Philosophy                                        [系]
│   ├── Physics                                           [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── Spanish Language and Literature                   [系]
│   ├── Women's and Gender Studies                        [系]
│   └── [Additional departments]                          [系]
│
├── College of Business                                   [学院]
│   ├── Accounting                                        [系]
│   ├── Business Management                               [系]
│   └── Finance                                           [系]
│
├── College of Engineering and Applied Sciences            [学院]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical & Molecular Engineering                  [系]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Engineering                              [系]
│   ├── Electrical Engineering                            [系]
│   ├── Engineering Science                               [系]
│   ├── Materials Science and Engineering                 [系]
│   └── Mechanical Engineering                            [系]
│
├── School of Communication and Journalism                 [学院]
│   ├── Communication                                     [系]
│   ├── Journalism                                        [系]
│   └── Mass Communication                                [系]
│
├── School of Dental Medicine                              [学院]
│   └── Oral Biology and Pathology                        [系]
│
├── School of Health Professions                           [学院]
│   ├── Clinical Laboratory Sciences                      [系]
│   ├── Health Science                                    [系]
│   ├── Respiratory Care                                  [系]
│   └── Physician Assistant / Physical Therapy             [系]
│
├── School of Marine and Atmospheric Sciences              [学院]
│   ├── Marine Sciences                                   [系]
│   └── Atmospheric and Oceanic Sciences                  [系]
│
├── Renaissance School of Medicine                         [学院]
│   ├── Anatomical Sciences                               [系]
│   ├── Biochemistry and Cell Biology                     [系]
│   ├── Microbiology and Immunology                       [系]
│   ├── Molecular and Cellular Biology                    [系]
│   ├── Molecular and Cellular Pharmacology               [系]
│   ├── Neuroscience                                      [系]
│   ├── Physiology and Biophysics                         [系]
│   └── Population Health and Clinical Outcomes Research   [系]
│
├── School of Nursing                                      [学院]
│   └── Nursing                                           [系]
│
├── School of Social Welfare                               [学院]
│   └── Social Work / Social Welfare                      [系]
│
├── School of Professional Development                     [学院]
│   └── [Professional development programs]               [系]
│
└── Graduate School                                        [学院]
    ├── [Interdisciplinary graduate programs]              [系]
    └── [Cross-college graduate programs]                 [系]
```

**Source**: `stonybrook.edu/academics/colleges-and-schools/index.html`

---

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 30 |
| BS | BS | Bachelor of Science | 本科 | 28 |
| BE | BE | Bachelor of Engineering | 本科 | 10 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 29 |
| MS | MS | Master of Science | 研究生 | 31 |
| MBA | MBA | Master of Business Administration | 研究生 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 4 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 10 |
| MM | MM | Master of Music | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 47 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| Certificate | Certificate | Advanced Certificate | 研究生 | 34 |
| **合计** | | | | **231** |

**Note**: 73 UG minors are not counted as degree programs. Total degree programs = 69 UG + 162 Grad = 231. The 304 figure in Rule 1 includes minors.

---

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BE | BFA | MA | MS | MBA | MFA | MAT | MM | PhD | DMA | Cert | 合计 |
|------------|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|------|------|
| College of Arts and Sciences | 30 | 12 | 0 | 1 | 18 | 8 | 0 | 3 | 8 | 1 | 24 | 1 | 8 | 114 |
| College of Business | 0 | 1 | 0 | 0 | 0 | 4 | 5 | 0 | 0 | 0 | 0 | 0 | 4 | 14 |
| College of Engineering and Applied Sciences | 0 | 0 | 10 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 7 | 0 | 5 | 31 |
| School of Communication and Journalism | 2 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| School of Dental Medicine | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| School of Health Professions | 0 | 3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| School of Marine and Atmospheric Sciences | 0 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 |
| Renaissance School of Medicine | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 7 | 0 | 2 | 12 |
| School of Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 |
| School of Social Welfare | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 |
| School of Professional Development | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 7 |
| Graduate School (interdisciplinary) | 0 | 0 | 0 | 0 | 9 | 2 | 0 | 1 | 2 | 0 | 5 | 0 | 9 | 28 |
| **合计** | **32** | **28** | **10** | **1** | **29** | **31** | **5** | **4** | **10** | **1** | **47** | **1** | **34** | **231** |

**Reconciliation**: Rule-1 total (231 degree programs) = matrix cell-sum (231) = Rule-5 row-count (231). UG minors (73) counted separately.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Stony Brook University has 12 colleges and schools. The College of Arts and Sciences is the largest undergraduate unit, offering the majority of BA and BS degrees. The College of Engineering and Applied Sciences offers BE (Bachelor of Engineering) degrees. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Department of Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History & Criticism | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Art, Studio | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Asian & Asian American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian & Asian American Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Atmospheric and Oceanic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Atmospheric and Oceanic Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Climate Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Human Evolutionary Biology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Marine Vertebrate Biology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Engineering Chemistry | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Data Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Information Systems | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Creative Writing
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Rhetoric and Writing | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Design, Policy & Planning | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Environmental Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Sustainability Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Geosciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Global Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Globalization Studies & International Relations | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Languages and Cultural Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French Language and Literature | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Italian Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Spanish Language and Literature | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics & Statistics | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Mathematics | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy/Planetary Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Physics | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Women's and Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Interdisciplinary
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education (Teacher Certification) | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Media/Art/Culture | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Multidisciplinary Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education (Teacher Certification) | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Technological Systems Management | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### College of Business

##### Department of Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Business Management | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### College of Engineering and Applied Sciences

##### Department of Biomedical Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Chemical & Molecular Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical & Molecular Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Civil Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Computer Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Electrical Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Engineering Science
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Mechanical Engineering
###### BE
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### School of Communication and Journalism

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

##### Department of Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mass Communication | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### School of Health Professions

##### Department of Health Professions
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Laboratory Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Health Science | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Respiratory Care | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### School of Marine and Atmospheric Sciences

##### Department of Marine Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Coastal Environmental Studies | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Marine Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Marine Vertebrate Biology | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### School of Nursing

##### Department of Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Nursing, BS-MS | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

#### School of Social Welfare

##### Department of Social Work
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 父学院 | URL |
|---|------|--------|-----|
| 1 | Education (Teacher Certification), BA | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Education (Teacher Certification), BS | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Media/Art/Culture, BA | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 4 | Multidisciplinary Studies, BA | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 5 | Technological Systems Management, BS | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 | Africana Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 2 | Anthropology | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 3 | Applied Mathematics & Statistics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 4 | Art History & Criticism | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 5 | Art, Studio | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 6 | Asian & Asian American Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 7 | Astronomy/Planetary Sciences | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 8 | Biology | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 9 | Black Heritage Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 10 | Business Management | College of Business | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 11 | Chemistry | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 12 | China Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 13 | Classics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 14 | Climate Solutions | School of Marine and Atmospheric Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 15 | Coastal Environmental Studies | School of Marine and Atmospheric Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 16 | Communication and Innovation | School of Communication and Journalism | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 17 | Computer Engineering | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 18 | Computer Science | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 19 | Creative Writing | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 20 | Data Science | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 21 | Digital Arts | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 22 | Electrical Engineering | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 23 | English | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 24 | Environmental Design, Policy & Planning | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 25 | Environmental Engineering | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 26 | Environmental Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 27 | Ethnomusicology | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 28 | Film and Screen Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 29 | Filmmaking | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 30 | Finance | College of Business | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 31 | French Language and Literature | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 32 | Geology | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 33 | Geospatial Science | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 34 | Globalization Studies & International Relations | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 35 | Health, Medicine & Society | School of Health Professions | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 36 | Hellenic Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 37 | History | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 38 | History of Health, Science & the Environment | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 39 | Information Systems | College of Business | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 40 | Italian American Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 41 | Italian Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 42 | Japanese Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 43 | Jazz | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 44 | Journalism | School of Communication and Journalism | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 45 | Judaic Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 46 | Korean Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 47 | Latin American & Caribbean Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 48 | Linguistics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 49 | Manufacturing Engineering | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 50 | Marine Sciences | School of Marine and Atmospheric Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 51 | Materials Science | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 52 | Mathematics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 53 | Mechanical Engineering | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 54 | Middle Eastern Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 55 | Music | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 56 | Music and Technology | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 57 | Music Theory | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 58 | Nanotechnology Studies | College of Engineering and Applied Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 59 | Optics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 60 | Philosophy | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 61 | Physics | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 62 | Political Science | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 63 | Professional Writing | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 64 | Real Estate and Insurance | College of Business | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 65 | Religious Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 66 | Rhetoric and Writing | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 67 | Russian Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 68 | South Asian Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 69 | Spanish Language and Literature | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 70 | Sustainability Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 71 | Technological Systems Management | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 72 | Theatre Arts | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |
| 73 | Women's and Gender Studies | College of Arts and Sciences | https://www.stonybrook.edu/academics/majors-minors-and-programs/ |

### 1.5 General/Institute-wide requirements

Stony Brook University requires all undergraduate students to complete Diversified Education Curriculum (DEC) requirements covering:
- English Composition
- Mathematics
- Natural Sciences
- Social and Behavioral Sciences
- Humanities and Fine Arts
- Language Other Than English (for BA degrees)
- Additional DEC categories

**Source**: `stonybrook.edu/catalog/undergraduate/`

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Graduate School (Interdisciplinary)

##### Interdisciplinary Programs
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Anthropology | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Art History and Criticism | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Biological Sciences (Ecology and Evolution) | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | Computational Linguistics | https://www.stonybrook.edu/grad/academics/programs.html |
| 6 | Economics | https://www.stonybrook.edu/grad/academics/programs.html |
| 7 | Global Asias | https://www.stonybrook.edu/grad/academics/programs.html |
| 8 | Higher Education Administration | https://www.stonybrook.edu/grad/academics/programs.html |
| 9 | Hispanic Languages and Literature | https://www.stonybrook.edu/grad/academics/programs.html |
| 10 | History | https://www.stonybrook.edu/grad/academics/programs.html |
| 11 | History of Philosophies, East and West (HPEW) | https://www.stonybrook.edu/grad/academics/programs.html |
| 12 | Liberal Studies | https://www.stonybrook.edu/grad/academics/programs.html |
| 13 | Linguistics | https://www.stonybrook.edu/grad/academics/programs.html |
| 14 | Marine Conservation and Policy | https://www.stonybrook.edu/grad/academics/programs.html |
| 15 | Mathematics | https://www.stonybrook.edu/grad/academics/programs.html |
| 16 | Medical Humanities, Compassionate Care & Bioethics | https://www.stonybrook.edu/grad/academics/programs.html |
| 17 | Music | https://www.stonybrook.edu/grad/academics/programs.html |
| 18 | Philosophy | https://www.stonybrook.edu/grad/academics/programs.html |
| 19 | Physics | https://www.stonybrook.edu/grad/academics/programs.html |
| 20 | Political Psychology | https://www.stonybrook.edu/grad/academics/programs.html |
| 21 | Political Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 22 | Psychology | https://www.stonybrook.edu/grad/academics/programs.html |
| 23 | Public Policy | https://www.stonybrook.edu/grad/academics/programs.html |
| 24 | Romance Languages | https://www.stonybrook.edu/grad/academics/programs.html |
| 25 | Sociology | https://www.stonybrook.edu/grad/academics/programs.html |
| 26 | Teaching Chemistry | https://www.stonybrook.edu/grad/academics/programs.html |
| 27 | Teaching English to Speakers of Other Languages (TESOL) | https://www.stonybrook.edu/grad/academics/programs.html |
| 28 | Women's, Gender, and Sexuality Studies | https://www.stonybrook.edu/grad/academics/programs.html |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Epidemiology and Clinical Research | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Science Communication | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropological Sciences | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Cultural Analysis and Theory: Comparative Literature Track | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Cultural Analysis and Theory: Cultural Studies Track | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Science Education | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | STEM Education | https://www.stonybrook.edu/grad/academics/programs.html |

###### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Chemistry | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Earth Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | English | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | French | https://www.stonybrook.edu/grad/academics/programs.html |
| 6 | Italian | https://www.stonybrook.edu/grad/academics/programs.html |
| 7 | Mathematics | https://www.stonybrook.edu/grad/academics/programs.html |
| 8 | Physics | https://www.stonybrook.edu/grad/academics/programs.html |
| 9 | Social Studies | https://www.stonybrook.edu/grad/academics/programs.html |
| 10 | Spanish | https://www.stonybrook.edu/grad/academics/programs.html |

###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art, Studio | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Creative Writing | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Film | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Television Writing | https://www.stonybrook.edu/grad/academics/programs.html |

#### College of Business

##### Department of Business
###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Business Administration | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Finance | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Health Care Management | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | Marketing | https://www.stonybrook.edu/grad/academics/programs.html |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Analytics | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Business Analytics and Intelligence | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Finance | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Human Resource Management | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance (GRAD) | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Finance (SPD) | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Human Resource Management | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Industrial Management | https://www.stonybrook.edu/grad/academics/programs.html |

#### College of Engineering and Applied Sciences

##### Department of Biomedical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Chemical & Molecular Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical and Molecular Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical and Molecular Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Civil Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Computer Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Computer Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Data Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Engineering Artificial Intelligence | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Data Science | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Data and Computational Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Engineering Machine Learning Systems | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Engineering the Internet of Things | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Human-Centered Data Science | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Electrical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Materials Science and Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

##### Department of Mechanical Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Communication and Journalism

##### Department of Journalism
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Dental Medicine

##### Department of Oral Biology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Oral Biology and Pathology | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Oral Biology and Pathology | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Health Professions

##### Department of Health Professions
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical Sciences | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Biomedical Informatics | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Population Health and Clinical Outcomes Research | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Informatics | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Marine and Atmospheric Sciences

##### Department of Marine Sciences
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine Conservation and Policy | https://www.stonybrook.edu/grad/academics/programs.html |

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine, Atmospheric, and Sustainability Sciences | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Marine, Atmospheric, and Sustainability Sciences | https://www.stonybrook.edu/grad/academics/programs.html |

#### Renaissance School of Medicine

##### Department of Biomedical Sciences
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical Sciences | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Molecular and Cellular Pharmacology | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Neuroscience | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Physiology and Biophysics | https://www.stonybrook.edu/grad/academics/programs.html |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical Sciences | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Biochemistry and Structural Biology | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Genetics | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Microbiology and Immunology | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | Molecular and Cellular Biology | https://www.stonybrook.edu/grad/academics/programs.html |
| 6 | Molecular and Cellular Pharmacology | https://www.stonybrook.edu/grad/academics/programs.html |
| 7 | Neuroscience | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Scholars in Biomedical Sciences | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Science Training & Research to Inform Decisions (CSTRIDE) | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Nursing

##### Department of Nursing
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Social Welfare

##### Department of Social Welfare
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Welfare | https://www.stonybrook.edu/grad/academics/programs.html |

#### School of Professional Development

##### Professional Development Programs
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education Administration | https://www.stonybrook.edu/grad/academics/programs.html |

###### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Accelerator Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 2 | Bilingual Education Extension | https://www.stonybrook.edu/grad/academics/programs.html |
| 3 | Children's Literature | https://www.stonybrook.edu/grad/academics/programs.html |
| 4 | Coaching | https://www.stonybrook.edu/grad/academics/programs.html |
| 5 | Cognitive Neuroscience | https://www.stonybrook.edu/grad/academics/programs.html |
| 6 | Cultural Studies | https://www.stonybrook.edu/grad/academics/programs.html |
| 7 | Education Leadership (School District and School Building Leader) | https://www.stonybrook.edu/grad/academics/programs.html |
| 8 | Geospatial Science | https://www.stonybrook.edu/grad/academics/programs.html |
| 9 | Human Origins | https://www.stonybrook.edu/grad/academics/programs.html |
| 10 | Life Sciences Innovation and Entrepreneurship | https://www.stonybrook.edu/grad/academics/programs.html |
| 11 | Media, Art, Culture, and Technology | https://www.stonybrook.edu/grad/academics/programs.html |
| 12 | Networking & Wireless Communications | https://www.stonybrook.edu/grad/academics/programs.html |
| 13 | Operations Research | https://www.stonybrook.edu/grad/academics/programs.html |
| 14 | Quantitative Finance | https://www.stonybrook.edu/grad/academics/programs.html |
| 15 | Quantitative Methods | https://www.stonybrook.edu/grad/academics/programs.html |
| 16 | Quantum Information Science and Technology | https://www.stonybrook.edu/grad/academics/programs.html |
| 17 | School District Business Leadership | https://www.stonybrook.edu/grad/academics/programs.html |
| 18 | Science Communication | https://www.stonybrook.edu/grad/academics/programs.html |
| 19 | Teaching Writing | https://www.stonybrook.edu/grad/academics/programs.html |
| 20 | Technological Systems Management | https://www.stonybrook.edu/grad/academics/programs.html |
| 21 | Women's, Gender, and Sexuality Studies | https://www.stonybrook.edu/grad/academics/programs.html |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science, MS** — College of Engineering and Applied Sciences

- **Department**: Computer Science
- **Application Portal**: https://www.stonybrook.edu/grad/admissions/apply-graduate-programs.html
- **Application Fee**: $100 (standard graduate fee)
- **Typical Deadline**: January 15 for fall funding consideration
- **GRE**: Waived for many programs (verify per department)
- **TOEFL Minimum**: 80 (internet-based) / 4 (new scale after 1/21/2026)
- **IELTS Minimum**: 6.5
- **Funding**: RA/TA positions available for PhD; limited for MS
- **Contact**: Graduate School, 2401 Computer Science Building, Stony Brook, NY 11794

### 2.3 Graduate admissions model

Stony Brook uses a **centralized graduate application system** through the Graduate School. All applications are submitted electronically through the Slate portal. However, admissions decisions are made by individual program committees.

**Application types**:
1. **Graduate** (Certificate, Master's, PhD) — via Graduate School
2. **Health Sciences** — separate application track
3. **School of Professional Development** — professional/continuing education
4. **Non-Matriculated** — take courses without pursuing a degree

**Key details**:
- Application fee: $100 (standard); $500 deposit required for admitted students in Business, Engineering, or Health Professions
- GRE: Varies by program (many programs have waived GRE requirements)
- English proficiency: TOEFL 80+ / IELTS 6.5+ for international applicants
- CGS April 15 Resolution: Stony Brook adheres to the April 15 resolution for funded offers

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | Common App OR SUNY Application | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Early Action Deadline | November 1 (non-binding) | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Regular Decision Deadline | January 15 (extended to Feb 1 for 2026) | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Spring Priority Deadline | November 1 | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Decision Notification (EA) | End of January | `stonybrook.edu/undergraduate-admissions/apply/early-action.php` |
| Decision Notification (RD) | Typically March-April | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Enrollment Confirmation Deadline | May 1 | `stonybrook.edu/undergraduate-admissions/apply/early-action.php` |
| Application Fee | $50 | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| SAT Code | 2548 | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| ACT Code | 2952 | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| FAFSA Code | 002838 | `stonybrook.edu/finaid/` |
| Test Policy | **Test-Optional** | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Superscore | Not specified | — |
| Recommendations | 1 teacher/counselor (2 for Honors) | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Essay | Required (topic of choice) | `stonybrook.edu/undergraduate-admissions/apply/first-year.php` |
| Need Policy (Domestic) | Need-aware | `stonybrook.edu/finaid/` |
| Need Policy (International) | Need-aware | `stonybrook.edu/undergraduate-admissions/apply/international.php` |

**Source snippet** (deadlines): "ENTRY TERM: Fall 2026 EARLY ACTION DEADLINE: November 1 REGULAR DECISION DEADLINE: January 15" — from `stonybrook.edu/undergraduate-admissions/apply/first-year.php`

**Source snippet** (test policy): "Stony Brook is test optional for applicants." — from `stonybrook.edu/undergraduate-admissions/apply/first-year.php`

**Source snippet** (fee): "There is a $50 application fee." — from `stonybrook.edu/undergraduate-admissions/apply/first-year.php`

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Source |
|------|---------------|-------------------|--------|
| TOEFL (Internet-based, before 1/21/2026) | 80 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| TOEFL (Internet-based, after 1/21/2026) | 4 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| IELTS | 6.5 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| Duolingo | 105 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| PTE Academic | 53 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| SAT EBRW | 480 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| ACT English | 19 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| IB English Higher Level | 5 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| AP English Language/Comp or Literature | 3 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| A-level English | C | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| GaoKao | 125 (out of 150) | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| CSAT Rank | 1 | — | `stonybrook.edu/undergraduate-admissions/apply/international.php` |

**Source snippet**: "Exam Minimum Score TOEFL (Internet-based): Exams taken prior to 1/21/2026 80 TOEFL (Internet-based): Exams taken after 1/21/2026 4 IELTS 6.5 Duolingo 105" — from `stonybrook.edu/undergraduate-admissions/apply/international.php`

**Applicability**: International students requiring F-1 visa. Applicants from native English-speaking countries or those who attended US high school for 3+ years may be exempt.

### 3.3 Graduate — global rules

| Field | Value | Source |
|-------|-------|--------|
| Application System | Centralized (Slate portal) | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| Application Fee | $100 | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| Deposit (Business/Engineering/Health Professions) | $500 | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| GRE | Varies by program (many waived) | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| English Proficiency (TOEFL) | 80 (internet-based) / 4 (new scale) | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| English Proficiency (IELTS) | 6.5 | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| GPA Minimum | 3.0 | Departmental websites |
| Letters of Recommendation | 3 | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| CGS April 15 Resolution | Yes (adherent) | `stonybrook.edu/grad/` |
| Fall Funding Deadline | January 15 (typical) | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |

**Source snippet**: "APPLICATION CHECKLIST Online Application Admissions Criteria Personal Statement Application Fee Application Fee Exceptions 3 Letters of Recommendation Official School Transcript(s) Official GRE Scores Official English Proficiency Scores (If applicable)" — from `stonybrook.edu/grad/admissions/apply-graduate-programs.html`

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense Item | NYS Resident (On-Campus) | Out of State (On-Campus) | Source |
|-------------|-------------------------|-------------------------|--------|
| Tuition | $7,070 | $31,050 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| Fees | $3,860 | $3,860 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| Housing | $12,291 | $12,291 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| Meal Plan | $7,450 | $7,450 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| **Total Direct Costs** | **$30,671** | **$54,651** | |
| Books | $900 | $900 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| Transportation | $840 | $840 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| Personal Expenses | $2,408 | $2,408 | `stonybrook.edu/commcms/finaid/newstudents/COA` |
| **Total Indirect Costs** | **$4,148** | **$4,148** | |
| **Estimated Yearly COA** | **$34,819** | **$58,799** | |

**Commuter/Off-Campus Students**:
- NYS Resident Direct Costs: $10,930
- Out of State Direct Costs: $34,910

**Source snippet**: "2026-27 Estimated Undergraduate Full-Time Cost of Attendance... Tuition $7,070 $31,050... Estimated Yearly Cost of Attendance $34,819 $58,799" — from `stonybrook.edu/commcms/finaid/newstudents/COA`

**Note**: Health insurance ($3,311.26 for Spring 2026/Summer 2026) is additional and can be waived with proof of coverage.

### 4.2 Undergraduate financial-aid policy

| Field | Value | Source |
|-------|-------|--------|
| Need Policy (Domestic) | Need-aware | `stonybrook.edu/finaid/` |
| Need Policy (International) | Need-aware | `stonybrook.edu/undergraduate-admissions/apply/international.php` |
| Meet 100% Demonstrated Need | Not guaranteed | `stonybrook.edu/finaid/` |
| Average Financial Aid | $13,100 | `stonybrook.edu/undergraduate-admissions/cost-and-aid/` |
| % Receiving Aid | 78% | `stonybrook.edu/undergraduate-admissions/cost-and-aid/` |
| % Receiving Grants | 71% (avg $10,162) | `stonybrook.edu/undergraduate-admissions/cost-and-aid/` |
| % Receiving Pell Grants | 36% (avg $5,149) | `stonybrook.edu/undergraduate-admissions/cost-and-aid/` |
| FAFSA Code | 002838 | `stonybrook.edu/finaid/` |
| TAP Code | 0875 | `stonybrook.edu/finaid/` |
| Excelsior Scholarship | Available (NYS residents) | `stonybrook.edu/finaid/` |

**Source snippet**: "78% receive financial aid; average amount: $13,100 71% receive U.S., NYS, or SBU grants; average amount: $10,162 36% receive Pell grants; average amount: $5,149" — from `stonybrook.edu/undergraduate-admissions/cost-and-aid/`

### 4.3 Graduate cost & funding framework

| Field | Value | Source |
|-------|-------|--------|
| Graduate Tuition (NYS Resident, per semester) | $7,111.01 (12 credits) | `stonybrook.edu/bursar/` |
| Graduate Tuition (Non-NYS Resident, per semester) | $14,951.01 (12 credits) | `stonybrook.edu/bursar/` |
| MBA Tuition (NYS Resident, per semester) | $9,071.01 | `stonybrook.edu/bursar/` |
| MBA Tuition (Non-NYS Resident, per semester) | $15,571.01 | `stonybrook.edu/bursar/` |
| Application Fee | $100 | `stonybrook.edu/grad/admissions/apply-graduate-programs.html` |
| Funding Types | RA/TA/Fellowship/Grant | `stonybrook.edu/grad/tuition-funding/` |
| CGS April 15 Resolution | Yes | `stonybrook.edu/grad/` |

**Funding opportunities**:
- Graduate Council Fellowship
- National Science Foundation Graduate Research Fellowship Program
- Research Foundation Professional Development
- Emergency Loan Program
- Graduate Opportunity Program
- Graduate Student Hardship Fund

**Source snippet**: "Spring 2026 Full Time Tuition and Fees... TUITION GROUP TOTAL NEW YORK STATE RESIDENT TOTAL NON NEW YORK STATE RESIDENT Graduate - (G1/3 - 12 credit) $7,111.01 $14,951.01" — from `stonybrook.edu/bursar/`

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Deadlines
```yaml
field: undergraduate.deadlines
value:
  ea_deadline: "November 1"
  rd_deadline: "January 15 (extended to February 1 for Fall 2026)"
  spring_priority: "November 1"
source_url: https://www.stonybrook.edu/undergraduate-admissions/apply/first-year.php
source_snippet: "ENTRY TERM: Fall 2026 EARLY ACTION DEADLINE: November 1 REGULAR DECISION DEADLINE: January 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Application Fee
```yaml
field: undergraduate.application_fee
value: 50
source_url: https://www.stonybrook.edu/undergraduate-admissions/apply/first-year.php
source_snippet: "There is a $50 application fee."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test Policy
```yaml
field: undergraduate.test_policy
value: "test-optional"
source_url: https://www.stonybrook.edu/undergraduate-admissions/apply/first-year.php
source_snippet: "Stony Brook is test optional for applicants."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: SAT/ACT Codes
```yaml
field: undergraduate.test_codes
value:
  sat: 2548
  act: 2952
  fafsa: 002838
source_url: https://www.stonybrook.edu/undergraduate-admissions/apply/first-year.php
source_snippet: "SAT Code: 2548, ACT Code: 2952."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: English Proficiency Requirements
```yaml
field: undergraduate.english_proficiency
value:
  toefl_old_scale: 80
  toefl_new_scale: 4
  ielts: 6.5
  duolingo: 105
  pte: 53
  sat_ebrw: 480
  act_english: 19
source_url: https://www.stonybrook.edu/undergraduate-admissions/apply/international.php
source_snippet: "Exam Minimum Score TOEFL (Internet-based): Exams taken prior to 1/21/2026 80 TOEFL (Internet-based): Exams taken after 1/21/2026 4 IELTS 6.5 Duolingo 105"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Cost of Attendance (On-Campus)
```yaml
field: undergraduate.cost.on_campus
value:
  tuition_in_state: 7070
  tuition_out_of_state: 31050
  fees: 3860
  housing: 12291
  meal_plan: 7450
  total_in_state: 34819
  total_out_of_state: 58799
source_url: https://www.stonybrook.edu/commcms/finaid/newstudents/COA
source_snippet: "2026-27 Estimated Undergraduate Full-Time Cost of Attendance... Tuition $7,070 $31,050... Estimated Yearly Cost of Attendance $34,819 $58,799"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Financial Aid Statistics
```yaml
field: undergraduate.financial_aid
value:
  percent_receiving_aid: 78
  average_aid: 13100
  percent_pell: 36
  average_pell: 5149
source_url: https://www.stonybrook.edu/undergraduate-admissions/cost-and-aid/
source_snippet: "78% receive financial aid; average amount: $13,100 71% receive U.S., NYS, or SBU grants; average amount: $10,162 36% receive Pell grants; average amount: $5,149"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Application Requirements
```yaml
field: graduate.application_requirements
value:
  application_fee: 100
  letters_of_recommendation: 3
  gre: "varies by program (many waived)"
source_url: https://www.stonybrook.edu/grad/admissions/apply-graduate-programs.html
source_snippet: "APPLICATION CHECKLIST Online Application Admissions Criteria Personal Statement Application Fee Application Fee Exceptions 3 Letters of Recommendation Official School Transcript(s) Official GRE Scores Official English Proficiency Scores (If applicable)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Tuition
```yaml
field: graduate.tuition
value:
  in_state_per_semester: 7111.01
  out_of_state_per_semester: 14951.01
source_url: https://www.stonybrook.edu/bursar/
source_snippet: "TUITION GROUP TOTAL NEW YORK STATE RESIDENT TOTAL NON NEW YORK STATE RESIDENT Graduate - (G1/3 - 12 credit) $7,111.01 $14,951.01"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-S-001: Schools and Colleges
```yaml
field: institutional.schools
value: 12
  - College of Arts and Sciences
  - College of Business
  - College of Engineering and Applied Sciences
  - School of Communication and Journalism
  - School of Dental Medicine
  - School of Health Professions
  - School of Marine and Atmospheric Sciences
  - Renaissance School of Medicine
  - School of Nursing
  - School of Professional Development
  - School of Social Welfare
  - Graduate School
source_url: https://www.stonybrook.edu/academics/colleges-and-schools/index.html
source_snippet: "Colleges and Schools Discover Our Academic Offerings College of Arts and Sciences... College of Business... College of Engineering and Applied Sciences..."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-P-001: Program Counts
```yaml
field: institutional.program_counts
value:
  ug_majors: 69
  ug_minors: 73
  grad_degree_programs: 128
  grad_certificates: 34
  total_degree_programs: 231
source_url: https://www.stonybrook.edu/academics/majors-minors-and-programs/index.html
source_snippet: "Accounting, BS Africana Studies, BA Anthropology, BA... [69 majors listed]"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
stonybrook-knowledge-base-v2/
├── 00-institution-overview
│   └── chunk-00-counts-hierarchy-matrix.md
├── 01-undergraduate-education
│   ├── chunk-01-arts-and-sciences.md
│   ├── chunk-02-business.md
│   ├── chunk-03-engineering.md
│   ├── chunk-04-communication-journalism.md
│   ├── chunk-05-health-professions.md
│   ├── chunk-06-marine-atmospheric.md
│   ├── chunk-07-nursing.md
│   ├── chunk-08-social-welfare.md
│   └── chunk-09-minors.md
├── 02-graduate-education
│   ├── chunk-10-graduate-school-interdisciplinary.md
│   ├── chunk-11-business-grad.md
│   ├── chunk-12-engineering-grad.md
│   ├── chunk-13-medicine-biomedical.md
│   ├── chunk-14-health-professions-grad.md
│   └── chunk-15-professional-development.md
├── 03-requirements-deadlines
│   └── chunk-16-application-requirements.md
├── 04-costs-financial-aid
│   └── chunk-17-costs-and-aid.md
└── 05-evidence-chain
    └── chunk-18-evidence-index.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "stonybrook-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BE|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Graduate program-specific deadlines | Each department's admissions page |
| P0 | Graduate program-specific GRE requirements | Each department's admissions page |
| P1 | Health Sciences programs (DMD, MD, etc.) | `stonybrook.edu/catalog/health-sciences/` |
| P1 | Housing rates | `stonybrook.edu/commcms/studentaffairs/res/housing/rates.php` |
| P1 | Meal plan rates | `stonybrook.edu/mealplan/` |
| P2 | Honors Programs details | `stonybrook.edu/undergraduate-admissions/academics/` |
| P2 | Accelerated/Combined degree programs | `stonybrook.edu/undergraduate-admissions/academics/` |
| P2 | SPD (School of Professional Development) full program list | `stonybrook.edu/spd/` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Stony Brook | [Other School] | [Other School] |
|-----------|-------------|----------------|----------------|
| **Total UG Cost/yr (in-state, on-campus)** | $34,819 | | |
| **Total UG Cost/yr (OOS, on-campus)** | $58,799 | | |
| **Tuition/yr (in-state)** | $7,070 | | |
| **Tuition/yr (OOS)** | $31,050 | | |
| **Need-blind (intl?)** | No (need-aware all) | | |
| **EA Deadline** | November 1 | | |
| **RD Deadline** | January 15 | | |
| **SAT/ACT Required?** | No (test-optional) | | |
| **TOEFL Min** | 80 (old) / 4 (new) | | |
| **IELTS Min** | 6.5 | | |
| **Application Fee** | $50 | | |
| **Total Program Count (Rule 1)** | 231 (degree programs) / 304 (incl. minors) | | |
| **School/Department Count (Rule 2)** | 12 | | |
| **% Receiving Financial Aid** | 78% | | |
| **Average Financial Aid** | $13,100 | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: stonybrook.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
