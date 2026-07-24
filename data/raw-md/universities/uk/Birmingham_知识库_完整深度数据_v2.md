# University of Birmingham Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: college -> subject area -> degree-level -> program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Russell Group**: Yes

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 366 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | P0 follow-up (56 pages, ~10 per page, ~560 estimated) |
| 研究生博士项目 (PhD/Doctoral) | P0 follow-up (separate research programme listing) |
| **学位项目总计 (UG extracted)** | **366** |
| 学院 (Colleges) | 5 |
| 学术单位 (Schools/Departments) | ~80 |

> **Data source**: University of Birmingham undergraduate course search (`birmingham.ac.uk/study/undergraduate/course-search`), 366 courses extracted across 37 paginated pages. Each page yields 10 courses (some pages have 9 due to varying card heights).
> **PG note**: Postgraduate taught courses are in a separate search at `birmingham.ac.uk/study/postgraduate/taught/course-search` with 56 pages — requires separate extraction (P0 follow-up).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Birmingham
├── College of Arts and Law                                              [学院]
│   ├── African Studies and Anthropology                                  [系]
│   ├── Art History, Curating and Visual Studies                          [系]
│   ├── Birmingham Law School                                             [系]
│   ├── Classics, Ancient History and Archaeology                         [系]
│   ├── Drama and Theatre Arts                                            [系]
│   ├── English Literature                                                [系]
│   ├── English, Drama and Creative Studies                               [系]
│   ├── Film and Creative Writing                                         [系]
│   ├── History                                                           [系]
│   ├── History and Cultures                                              [系]
│   ├── Languages, Cultures, Art History and Music                        [系]
│   ├── Liberal Arts and Sciences                                         [系]
│   ├── Linguistics and Communication                                     [系]
│   ├── Modern Languages                                                  [系]
│   ├── Music                                                             [系]
│   ├── Philosophy                                                        [系]
│   ├── Philosophy, Theology and Religion                                 [系]
│   ├── Shakespeare Institute                                             [研究所]
│   └── Theology and Religion                                             [系]
├── College of Engineering and Physical Sciences                         [学院]
│   ├── Chemical Engineering                                              [系]
│   ├── Chemistry                                                         [系]
│   ├── Civil Engineering                                                 [系]
│   ├── Computer Science                                                  [系]
│   ├── Electronic, Electrical and Systems Engineering                    [系]
│   ├── Engineering                                                       [系]
│   ├── Mathematics                                                       [系]
│   ├── Mechanical Engineering                                            [系]
│   ├── Metallurgy and Materials                                          [系]
│   └── Physics and Astronomy                                             [系]
├── College of Life and Environmental Sciences                           [学院]
│   ├── Biosciences (School of)                                           [系]
│   ├── Geography, Earth and Environmental Sciences (School of)           [系]
│   ├── Psychology (School of)                                            [系]
│   └── Sport, Exercise and Rehabilitation Sciences (School of)           [系]
├── College of Medicine and Health                                       [学院]
│   ├── Applied Health Sciences                                           [系]
│   ├── Biomedical Sciences                                               [系]
│   ├── Birmingham Medical School                                         [系]
│   ├── Cancer and Genomic Sciences                                       [系]
│   ├── Cardiovascular Sciences                                           [系]
│   ├── Clinical Immunology Services                                      [系]
│   ├── Dentistry (School of)                                             [系]
│   ├── Health Sciences                                                   [系]
│   ├── Immunology and Immunotherapy                                      [系]
│   ├── Infection, Inflammation and Immunology                            [系]
│   ├── Inflammation and Ageing                                           [系]
│   ├── Medical Sciences                                                  [系]
│   ├── Metabolism and Systems Science                                    [系]
│   ├── Microbes, Infection and Microbiomes                               [系]
│   ├── Nursing and Midwifery (School of)                                 [系]
│   └── Pharmacy (School of)                                              [系]
└── College of Social Sciences                                           [学院]
    ├── Accounting (Department of)                                        [系]
    ├── Birmingham Business School                                        [系]
    ├── Disability, Inclusion and Special Needs (Department of)           [系]
    ├── Economics (Department of)                                         [系]
    ├── Education (School of)                                             [系]
    ├── Education and Social Justice (Department of)                      [系]
    ├── Finance (Department of)                                           [系]
    ├── Government (School of)                                            [系]
    ├── Health Services Management Centre                                 [系]
    ├── International Development (Department of)                         [系]
    ├── Management (Department of)                                        [系]
    ├── Marketing (Department of)                                         [系]
    ├── Political Science and International Studies (Department of)       [系]
    ├── Public Administration and Policy (Department of)                  [系]
    ├── Social Policy and Society (School of)                             [系]
    ├── Social Policy, Sociology and Criminology (Department of)          [系]
    ├── Social Work and Social Care (Department of)                       [系]
    ├── Strategy and International Business (Department of)               [系]
    └── Teacher Education (Department of)                                 [系]
```

> **Source**: `birmingham.ac.uk/about/colleges-schools-and-departments`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 114 |
| BSc | BSc | Bachelor of Science | 本科 | 128 |
| MSci | MSci | Integrated Master of Science | 本科 (Integrated Master's) | 50 |
| BEng | BEng | Bachelor of Engineering | 本科 | 28 |
| MEng | MEng | Master of Engineering (Integrated) | 本科 (Integrated Master's) | 28 |
| LLB | LLB | Bachelor of Laws | 本科 | 5 |
| BNurs | BNurs | Bachelor of Nursing | 本科 | 3 |
| BCL | BCL | Bachelor of Commercial Law (Dubai) | 本科 | 2 |
| BASc | BASc | Bachelor of Arts and Sciences | 本科 | 1 |
| BDS | BDS | Bachelor of Dental Surgery | 本科 | 1 |
| BMedSci | BMedSci | Bachelor of Medical Science (Intercalated) | 本科 | 1 |
| MBChB | MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 |
| BMus | BMus | Bachelor of Music | 本科 | 1 |
| MPharm | MPharm | Master of Pharmacy (Integrated) | 本科 (Integrated Master's) | 1 |
| EAP | EAP | English for Academic Purposes (Presessional) | 本科 (Foundation) | 1 |
| FDSc | FDSc | Foundation Degree in Science | 本科 (Foundation) | 1 |
| **合计** | | | | **366** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学位 | BA | BSc | MSci | BEng | MEng | LLB | BNurs | BCL | BASc | BDS | BMedSci | MBChB | BMus | MPharm | EAP | FDSc | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Arts and Law | 69 | 0 | 0 | 0 | 0 | 5 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | **78** |
| Engineering and Physical Sciences | 0 | 35 | 22 | 28 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **113** |
| Life and Environmental Sciences | 3 | 41 | 21 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **66** |
| Medicine and Health | 1 | 5 | 7 | 0 | 0 | 0 | 3 | 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | **20** |
| Social Sciences | 41 | 47 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **89** |
| **合计** | 114 | 128 | 50 | 28 | 28 | 5 | 3 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | **366** |

> **Reconciliation check**: Rule-1 total (366) == matrix-sum (366) == Rule-5 rows (366). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

University of Birmingham is organised into 5 academic Colleges, each containing multiple Schools and Departments (~80 units total). See Section 0.2 for the full hierarchy tree. All undergraduate degree programmes are administered by one of these Colleges.

The university also operates a Dubai campus, offering a subset of programmes. Courses offered at the Dubai campus are noted in the listing below.

### 1.2 Undergraduate degree programmes — grouped by College > Subject > Degree Level### College of Arts and Law

#### Anthropology

##### BA (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Anthropology and African Studies BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-and-african-studies-ba |
| 2 | Social Anthropology and Archaeology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-and-archaeology-ba |
| 3 | Social Anthropology and Classical Literature and Civilisation BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-and-classical-literature-and-civilisation-ba |
| 4 | Social Anthropology and Politics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-and-politics-ba |
| 5 | Social Anthropology and History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-and-history-ba |
| 6 | Social Anthropology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/anthropology-courses/social-anthropology-ba |

---

#### Classics Ancient History And Archaeology

##### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient History and Archaeology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/ancient-history-and-archaeology-ba |
| 2 | Ancient History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/ancient-history-ba |
| 3 | Archaeology and History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/archaeology-and-history-ba |
| 4 | Classical Literature & Civilisation and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/classical-literature-civilisation-and-philosophy-ba |
| 5 | Classics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/classics-ba |
| 6 | English Literature and Classical Literature & Civilisation BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/english-literature-and-classical-literature-civilisation-ba |
| 7 | Classical Literature and Civilisation BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/classics-ancient-history-and-archaeology-courses/classical-literature-and-civilisation-ba |

---

#### Drama

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media and Creative Industries BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/drama-courses/digital-media-and-creative-industries-ba |
| 2 | Drama and Creative Writing BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/drama-courses/drama-and-creative-writing-ba |
| 3 | Drama and English Literature BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/drama-courses/drama-and-english-literature-ba |
| 4 | Drama and Film BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/drama-courses/drama-and-film-ba |

---

#### English Language And Linguistics

##### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Language and Linguistics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/english-language-and-linguistics-courses/english-language-and-linguistics-ba |
| 2 | Digital Media and Communications BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/english-language-and-linguistics-courses/digital-media-and-communications-ba |
| 3 | English Language and Literature BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/english-language-and-linguistics-courses/english-language-and-literature-ba |

---

#### English Literature

##### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Literature and History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/english-literature-courses/english-literature-and-history-ba |
| 2 | English Literature BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/english-literature-courses/english-literature-ba |

---

#### Film Creative Writing

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Literature and Creative Writing BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/film-creative-writing-courses/english-literature-and-creative-writing-ba |
| 2 | English Literature and Film BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/film-creative-writing-courses/english-literature-and-film-ba |
| 3 | Film and Television BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/film-creative-writing-courses/film-and-television-ba |
| 4 | Film and Creative Writing BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/film-creative-writing-courses/film-and-creative-writing-ba |

---

#### History

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient and Medieval History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-courses/ancient-and-medieval-history-ba |
| 2 | History and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-courses/history-and-philosophy-ba |
| 3 | History and Politics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-courses/history-and-politics-ba |
| 4 | History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-courses/history-ba |

---

#### History Of Art

##### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Literature and History of Art BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-of-art-courses/english-literature-and-history-of-art-ba |
| 2 | History and History of Art BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-of-art-courses/history-and-history-of-art-ba |
| 3 | History of Art BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/history-of-art-courses/history-of-art-ba |

---

#### Law

##### BCL (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Commercial Law BCL | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/law-courses/bachelor-commercial-law |
| 2 | Bachelor of Commercial Law with Integrated Foundation Year BCL | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/law-courses/bachelor-of-commercial-law-with-integrated-foundation-year-bcl |

---

##### LLB (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | International Law and Globalisation LLB | https://www.birmingham.ac.uk/study/undergraduate/subjects/law-courses/international-law-and-globalisation-llb |
| 2 | Law LLB | https://www.birmingham.ac.uk/study/undergraduate/subjects/law-courses/law-llb |
| 3 | LLB for Graduates LLB | https://www.birmingham.ac.uk/study/undergraduate/subjects/law-courses/llb-for-graduates |
| 4 | Law with Business Studies LLB | https://www.birmingham.ac.uk/study/undergraduate/subjects/law-courses/law-with-business-studies-llb |
| 5 | Law with Criminology LLB | https://www.birmingham.ac.uk/study/undergraduate/subjects/law-courses/law-with-criminology-llb |

---

#### Liberal Arts

##### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Arts BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/liberal-arts-courses/liberal-arts-ba |

---

#### Modern Languages

##### BA (22 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | French BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-ba |
| 2 | French and German BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-and-german-ba |
| 3 | French and Italian BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-and-italian-ba |
| 4 | French and Portuguese BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-and-portuguese-ba |
| 5 | French and Russian BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-and-russian-ba |
| 6 | French and Spanish BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/french-and-spanish-ba |
| 7 | German and Italian BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/german-and-italian-ba |
| 8 | German and Russian BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/german-and-russian-ba |
| 9 | German and Spanish BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/german-and-spanish-ba |
| 10 | Modern Languages and English Literature BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-and-english-literature-ba |
| 11 | Modern Languages and History of Art BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-and-history-of-art-ba |
| 12 | Modern Languages and Linguistics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-and-linguistics-ba |
| 13 | Modern Languages and Music BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-and-music-ba |
| 14 | Modern Languages with Business Management BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-with-business-management-ba |
| 15 | Modern Languages with Digital Communications BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-with-digital-communications-ba |
| 16 | Modern Languages with Translation Studies BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-with-translation-ba |
| 17 | Spanish BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/spanish-ba |
| 18 | Spanish and Italian  BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/spanish-and-italian-ba |
| 19 | Spanish and Portuguese BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/spanish-and-portuguese-ba |
| 20 | Spanish and Russian BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/spanish-and-russian-ba |
| 21 | Modern Languages and History BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-and-history-ba |
| 22 | Modern Languages BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/modern-languages-courses/modern-languages-ba |

---

#### Music

##### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics and Music BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/music-courses/mathematics-and-music-ba |

---

##### BMus (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music BMus | https://www.birmingham.ac.uk/study/undergraduate/subjects/music-courses/music-bmus |

---

#### Philosophy

##### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English Language and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/english-language-and-philosophy-ba |
| 2 | English Literature and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/english-literature-and-philosophy-ba |
| 3 | Mathematics and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/mathematics-and-philosophy-ba |
| 4 | Philosophy and Sociology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/philosophy-and-sociology-ba |
| 5 | Politics and Philosophy with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/politics-and-philosophy-year-abroad-ba |
| 6 | Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/philosophy-ba |
| 7 | Philosophy, Politics and Law BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/philosophy-courses/philosophy-politics-and-law-ba |

---

#### Pre Sessional English

##### EAP (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Presessional English, English for Academic Purposes | https://www.birmingham.ac.uk/study/undergraduate/subjects/pre-sessional-english-courses/english-for-academic-purposes |

---

#### Theology And Religion

##### BA (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy, Religion and Ethics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/theology-and-religion-courses/philosophy-religion-and-ethics-ba |
| 2 | Politics, Religion and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/theology-and-religion-courses/politics-religion-and-philosophy-ba |
| 3 | Psychology and Religion BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/theology-and-religion-courses/psychology-and-religion-ba |
| 4 | History and Theology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/theology-and-religion-courses/history-and-theology-ba |
| 5 | Theology and Religion BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/theology-and-religion-courses/theology-and-religion-ba |

---

### College of Engineering and Physical Sciences

#### Aerospace Engineering

##### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/aerospace-engineering-courses/aerospace-engineering-beng |

---

##### MEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/aerospace-engineering-courses/aerospace-engineering-meng |

---

#### Chemical Engineering

##### BEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-beng |
| 2 | Chemical Engineering with Industrial Study BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-industrial-beng |
| 3 | Energy Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/energy-engineering-beng |
| 4 | Energy Engineering with Industrial Study BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/energy-engineering-industrial-study-beng |

---

##### MEng (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering (International Study)  MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-international-meng |
| 2 | Chemical Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-meng |
| 3 | Chemical Engineering with Industrial Study MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-industrial-meng |
| 4 | Chemical Engineering with International and Industrial Study MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/chemical-engineering-international-industrial-meng |
| 5 | Energy Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/energy-engineering-meng |
| 6 | Energy Engineering with Industrial Study MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemical-engineering-courses/energy-engineering-industrial-study-meng |

---

#### Chemistry

##### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-bsc |
| 2 | Chemistry with a Modern Language BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-modern-language-bsc |
| 3 | Chemistry with a Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-industry-bsc |
| 4 | Chemistry with Business Management BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-business-management-bsc |
| 5 | Chemistry with Foundation Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-foundation-year |
| 6 | Chemistry with Medicinal Chemistry and Drug Discovery BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-medicinal-drug-discovery-bsc |
| 7 | Chemistry with Sustainability BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-sustainability-bsc |

---

##### MSci (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-msci |
| 2 | Chemistry with a Modern Language MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-modern-language-msci |
| 3 | Chemistry with a Year in Industry MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-industry-msci |
| 4 | Chemistry with Business Management  MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-business-management-msci |
| 5 | Chemistry with Medicinal Chemistry and Drug Discovery MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-medicinal-chemistry-drug-discovery-msci |
| 6 | Chemistry with Study Abroad MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-study-abroad-msci |
| 7 | Chemistry with Sustainability MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/chemistry-courses/chemistry-sustainability-msci |

---

#### Civil Engineering

##### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/civil-engineering-courses/civil-engineering-beng |

---

##### MEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/civil-engineering-courses/civil-engineering-meng |
| 2 | Civil Engineering with Industrial Experience MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/civil-engineering-courses/civil-engineering-industrial-experience-meng |
| 3 | Civil Engineering with Industrial Year MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/civil-engineering-courses/civil-engineering-industrial-year-meng |
| 4 | Civil Engineering with International Study MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/civil-engineering-courses/civil-engineering-international-meng |

---

#### Computer Science

##### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence (AI) and Computer Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/artificial-intelligence-ai-computer-science-bsc |
| 2 | Artificial Intelligence (AI) and Computer Science with a Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/artificial-intelligence-ai-computer-science-industry-bsc |
| 3 | Artificial Intelligence (AI) and Computer Science BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/artificial-intelligence-and-computer-science-bsc |
| 4 | Artificial Intelligence (AI) and Computer Science with Integrated Foundation Year  BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/artificial-intelligence-and-computer-science-with-foundation-bsc |
| 5 | Computer Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-bsc |
| 6 | Computer Science BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/computer-science-bsc |
| 7 | Computer Science with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/computer-science-with-foundation-year-bsc |
| 8 | Computer Science with a Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-industry-bsc |
| 9 | Computer Science with Study Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-study-abroad-bsc |

---

##### MEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Software Engineering MEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/computer-science-and-software-engineering-meng |
| 2 | Computer Science and Software Engineering with Integrated Foundation Year MEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/computer-science-courses/computer-science-and-software-engineering-with-foundation-year-meng |
| 3 | Computer Science/Software Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-software-engineering-meng |
| 4 | Computer Science/Software Engineering with a Year in Industry MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-software-engineering-industry-meng |

---

##### MSci (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-msci |
| 2 | Computer Science with a Year in Industry MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-industry-msci |
| 3 | Computer Science with Study Abroad MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/computer-science-courses/computer-science-study-abroad-msci |

---

#### Electronic Electrical And Systems Engineering

##### BEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electronic and Electrical Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-engineering-beng |
| 2 | Electronic and Electrical Engineering with Industrial Year BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-engineering-industrial-beng |
| 3 | Mechatronic and Robotic Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/mechatronic-robotic-engineering-beng |
| 4 | Mechatronic and Robotic Engineering with Industrial Year BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/mechatronic-robotic-engineering-industrial-beng |

---

##### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/computer-engineering-bsc |

---

##### MEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electronic and Electrical Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-engineering-meng |
| 2 | Electronic and Electrical Engineering with Industrial Year  MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/electronic-electrical-engineering-industrial-meng |
| 3 | Mechatronic and Robotic Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/mechatronic-robotic-engineering-meng |
| 4 | Mechatronic and Robotic Engineering with Industrial Year MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/electronic-electrical-and-systems-engineering-courses/mechatronic-robotic-engineering-industrial-meng |

---

#### Engineering

##### BEng (14 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/civil-engineering-beng |
| 2 | Civil Engineering with Integrated Foundation Year BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/civil-engineering-with-foundation-year-beng |
| 3 | Computer Engineering BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/computer-engineering-beng |
| 4 | Computer Engineering with Integrated Foundation Year BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/computer-engineering-with-foundation-year-beng |
| 5 | Electronic and Electrical Engineering BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/electronic-electrical-engineering |
| 6 | Electronic and Electrical Engineering with Integrated Foundation Year BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/electronic-electrical-engineering-integrated-foundation-year-beng |
| 7 | Engineering and Physical Sciences Foundation Year BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/engineering-courses/engineering-physical-sciences-foundation-year |
| 8 | Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/engineering-courses/engineering-beng |
| 9 | Mechanical Engineering (Biomedical) BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-biomedical-beng |
| 10 | Mechanical Engineering (Biomedical) with Integrated Foundation Year  BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-biomedical-foundation-year-beng |
| 11 | Mechanical Engineering BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-beng |
| 12 | Mechanical Engineering with Integrated Foundation Year BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-with-foundation-year-beng |
| 13 | Robotics and Artificial Intelligence (AI) BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/robotics-artificial-intelligence-ai-beng-dubai |
| 14 | Robotics and Artificial Intelligence (AI) with Integrated Foundation Year BEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/robotics-and-artificial-intelligence-ai-foundation-year-beng |

---

##### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/engineering-courses/engineering-meng |
| 2 | Mechanical Engineering MEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-meng |
| 3 | Mechanical Engineering with Integrated Foundation Year  MEng | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/engineering-courses/mechanical-engineering-with-foundation-year-meng |

---

#### Materials Science And Engineering

##### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/materials-science-and-engineering-courses/materials-science-and-engineering-beng |

---

##### MEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/materials-science-and-engineering-courses/materials-science-and-engineering-meng |
| 2 | Materials Science and Engineering with Industrial Experience MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/materials-science-and-engineering-courses/materials-science-engineering-industrial-experience-meng |

---

#### Mathematics

##### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Sciences BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematical-sciences-bsc |
| 2 | Mathematics and Computer Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-computer-science-bsc |
| 3 | Mathematics and Computer Science with Industrial Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-computer-science-industrial-bsc |
| 4 | Mathematics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-bsc |
| 5 | Mathematics with a Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-industry-bsc |
| 6 | Mathematics with an International Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-international-bsc |
| 7 | Mathematics with Business Management BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-business-management-bsc |
| 8 | Mathematics with Study in Continental Europe BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-continental-europe-bsc |
| 9 | Mathematics, Statistics and Data Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-statistics-data-science-bsc |

---

##### MSci (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics and Computer Science  MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-computer-science-msci |
| 2 | Mathematics and Computer Science with Industrial Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-computer-science-industrial-msci |
| 3 | Mathematics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-msci |
| 4 | Mathematics with Business Management MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/mathematics-courses/mathematics-business-management-msci |

---

#### Mechanical Engineering

##### BEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (Automotive) BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-automotive-beng |
| 2 | Mechanical Engineering BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-beng |
| 3 | Mechanical Engineering with Industrial Year BEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-industrial-beng |

---

##### MEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (Automotive)  MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-automotive-meng |
| 2 | Mechanical Engineering MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-meng |
| 3 | Mechanical Engineering with a Year Abroad MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-year-abroad-meng |
| 4 | Mechanical Engineering with Industrial Year MEng | https://www.birmingham.ac.uk/study/undergraduate/subjects/mechanical-engineering-courses/mechanical-engineering-industrial-meng |

---

#### Physics And Astronomy

##### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics (International Study) BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-international-bsc |
| 2 | Physics and Astrophysics (International Study) BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-astrophysics-international-bsc |
| 3 | Physics and Astrophysics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-astrophysics-bsc |
| 4 | Physics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-bsc |
| 5 | Physics with Data Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-data-science-bsc |
| 6 | Physics with Medical Physics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-medical-physics-bsc |
| 7 | Physics with Particle Physics and Cosmology BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-particle-physics-cosmology-bsc |
| 8 | Theoretical Physics and Applied Mathematics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/theoretical-physics-applied-mathematics-bsc |
| 9 | Theoretical Physics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/theoretical-physics-bsc |

---

##### MSci (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics (International Study) MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-international-msci |
| 2 | Physics and Astrophysics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-astrophysics-msci |
| 3 | Physics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-msci |
| 4 | Physics with Data Science  MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-data-science-msci |
| 5 | Physics with Medical Physics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-medical-physics-msci |
| 6 | Physics with Particle Physics and Cosmology MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/physics-particle-physics-cosmology-msci |
| 7 | Theoretical Physics and Applied Mathematics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/theoretical-physics-applied-mathematics-msci |
| 8 | Theoretical Physics MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physics-and-astronomy-courses/theoretical-physics-msci |

---

### College of Life and Environmental Sciences

#### Biosciences

##### BSc (13 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biochemistry-bsc |
| 2 | Biological Sciences BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biological-sciences-bsc |
| 3 | Biotechnology BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biotechnology-bsc |
| 4 | Biochemistry with an International Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biochemistry-with-an-international-year-bsc |
| 5 | Biochemistry with Study in Continental Europe BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biochemistry-with-study-in-continental-europe-bsc |
| 6 | Biological Sciences with an International Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biological-sciences-with-an-international-year-bsc |
| 7 | Biological Sciences with Study in Continental Europe BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biological-sciences-with-study-in-continental-europe-bsc |
| 8 | Biotechnology with International Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biotechnology-with-international-year-bsc |
| 9 | Medical Biochemistry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/medical-biochemistry-bsc |
| 10 | Microbiology BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/microbiology-bsc |
| 11 | Microbiology with International Year BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/microbiology-bsc-with-international-year |
| 12 | Microbiology with Study in Continental Europe BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/microbiology-bsc-with-study-in-continental-europe |
| 13 | Human Sciences BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/human-sciences-bsc |

---

##### MSci (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry with Professional Placement MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biochemistry-with-professional-placement-msci |
| 2 | Biological Sciences with Professional Placement MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biological-sciences-with-professional-placement-msci |
| 3 | Biotechnology with Placement Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biotechnology-with-placement-year-msci |
| 4 | Biochemistry MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biochemistry-msci |
| 5 | Biological Sciences MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biological-sciences-msci |
| 6 | Biotechnology MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/biotechnology-msci |
| 7 | Human Sciences MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/human-sciences-msci |
| 8 | Microbiology MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/microbiology-msci |
| 9 | Microbiology with Professional Placement MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/biosciences-courses/microbiology-msci-with-professional-placement |

---

#### Geography Earth And Environmental Sciences

##### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sustainability BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/geography-earth-and-environmental-sciences-courses/sustainability-bsc |
| 2 | Sustainability with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/geography-earth-and-environmental-sciences-courses/bsc-sustainability-with-integrated-foundation-year-dubai |

---

#### Geography Urban Planning And Environmental Sciences

##### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-with-year-abroad-ba |
| 2 | Geography BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-ba |
| 3 | Geography with Business BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-with-business-ba |

---

##### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science with International Research Placement BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/environmental-science-with-international-research-placement-bsc |
| 2 | Environmental Science with Year Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/environmental-science-with-year-abroad-bsc |
| 3 | Geography and Urban and Regional Planning with Year Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-and-urban-and-regional-planning-with-year-abroad-bsc |
| 4 | Geography with Year Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-with-year-abroad-bsc |
| 5 | Environmental Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/environmental-science-bsc |
| 6 | Geography and Urban and Regional Planning BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-and-urban-and-regional-planning-bsc |
| 7 | Geography BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-bsc |

---

##### MSci (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/environmental-science-msci |
| 2 | Geography MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-msci |
| 3 | Geography with International Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geography-urban-planning-and-environmental-sciences-courses/geography-with-international-year-msci |

---

#### Geology And Earth Sciences

##### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Change and Sustainability with Year Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/environmental-change-and-sustainability-with-year-abroad-bsc |
| 2 | Geology and Physical Geography BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-and-physical-geography-bsc |
| 3 | Palaeontology and Geology  BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/palaeontology-and-geology-bsc |
| 4 | Environmental and Engineering Geoscience BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/environmental-and-engineering-geoscience-bsc |
| 5 | Environmental Change and Sustainability BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/environmental-change-and-sustainability-bsc |
| 6 | Geology BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-bsc |
| 7 | Natural Sciences BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/natural-sciences-bsc |

---

##### MSci (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Change and Sustainability MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/environmental-change-and-sustainability-msci |
| 2 | Geology MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-msci |
| 3 | Geology and Physical Geography MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-and-physical-geography-msci |
| 4 | Geology and Physical Geography with an International Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-and-physical-geography-with-an-international-year-msci |
| 5 | Geology with International Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/geology-with-an-international-year-msci |
| 6 | Natural Sciences MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/natural-sciences-msci |
| 7 | Palaeontology and Geology MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/palaeontology-and-geology-msci |
| 8 | Palaeontology and Geology with an International Year MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/geology-and-earth-sciences-courses/palaeontology-and-geology-with-an-international-year-msci |

---

#### Golf Management

##### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Golf Management Studies BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/golf-management-courses/applied-golf-management-studies-bsc |

---

##### FDSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Professional Golf Studies | https://www.birmingham.ac.uk/study/undergraduate/subjects/golf-management-courses/professional-golf-studies-fdsc |

---

#### Psychology

##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology with Business Management BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/psychology-courses/psychology-with-business-management-bsc |
| 2 | Psychology with Business Management Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/psychology-courses/psychology-with-business-management-bsc-integrated |
| 3 | Psychology BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/psychology-courses/psychology-bsc |
| 4 | Psychology with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/psychology-courses/psychology-bsc-integrated-foundation-year |

---

#### Psychology And Neuroscience

##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology with Year Abroad BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/psychology-and-neuroscience-courses/psychology-with-year-abroad-bsc |
| 2 | Human Neuroscience BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/psychology-and-neuroscience-courses/human-neuroscience-bsc |
| 3 | Psychology BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/psychology-and-neuroscience-courses/psychology-bsc |

---

##### MSci (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology and Psychological Practice MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/psychology-and-neuroscience-courses/psychology-and-psychological-practice-msci |

---

#### Sport Sciences

##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Sciences with Business BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/sport-sciences-courses/sport-sciences-with-business |
| 2 | Sport, Coaching Sciences and Business BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/sport-sciences-courses/sport-coaching-sciences-and-business-bsc |
| 3 | Sport, Exercise and Health Sciences BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/sport-sciences-courses/sport-exercise-and-health-sciences-bsc |
| 4 | Sport, PE and Coaching Science BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/sport-sciences-courses/sport-pe-and-coaching-science-bsc |

---

### College of Medicine and Health

#### Biomedical Science

##### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/biomedical-science-courses/biomedical-science-bsc |
| 2 | Biomedical Sciences with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/biomedical-science-courses/biomedical-science-bsc-with-integrated-foundation-year |

---

##### MSci (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences MSci | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/biomedical-science-courses/biomedical-science-msci |

---

#### Dentistry

##### BDS (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Surgery BDS | https://www.birmingham.ac.uk/study/undergraduate/subjects/dentistry-courses/dental-surgery-bds |

---

##### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene and Therapy BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/dentistry-courses/dental-hygiene-and-therapy-bsc |

---

#### Medicine

##### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Humanities (Intercalated degree) BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/medical-humanities-intercalated-degree |

---

##### BMedSci (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Science (Intercalated Degree)  BMedSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/medical-science-bmedsc-intercalated-degree |

---

##### BNurs (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) BNurs | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/nursing-bnurs-adult |
| 2 | Nursing (Child) BNurs | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/nursing-bnurs-child |
| 3 | Nursing (Mental Health) BNurs | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/nursing-bnurs-mental-health |

---

##### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Midwifery BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/bsc-midwifery |
| 2 | Midwifery Degree Apprenticeship BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/midwifery-bsc-degree-apprenticeship |

---

##### MBChB (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine and Surgery MBChB | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/medicine-and-surgery-mbchb |

---

##### MPharm (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy MPharm | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/mpharm-pharmacy-4-year |

---

##### MSci (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/biomedical-science-msci |
| 2 | Clinical Anatomy (Intercalated degree) MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/clinical-anatomy-msci-intercalated-degree |
| 3 | Clinical Science (Intercalated degree) MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/clinical-science-msci-intercalated-degree |
| 4 | Health Management and Leadership (Intercalated Degree) MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/health-management-and-leadership-msci-intercalated-degree |
| 5 | Medical Sciences (Intercalated degree) MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/medicine-courses/medical-sciences-msci-intercalated-degree |

---

#### Physiotherapy

##### MSci (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physiotherapy MSci | https://www.birmingham.ac.uk/study/undergraduate/subjects/physiotherapy-courses/physiotherapy-msci |

---

### College of Social Sciences

#### Accounting And Finance

##### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/accounting-and-finance-courses/accounting-and-finance-bsc |
| 2 | Accounting and Finance with Business Analytics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/accounting-and-finance-courses/accounting-and-finance-with-business-analytics-bsc |

---

#### Business And Finance

##### BSc (22 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/accounting-and-finance-bsc |
| 2 | Accounting and Finance with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/accounting-and-finance-with-foundation-bsc |
| 3 | Business Management BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-bsc |
| 4 | Business Management with Economics BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-economics-bsc |
| 5 | Business Management with Economics with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-economics-with-foundation-bsc |
| 6 | Business Management with Finance BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-finance-bsc |
| 7 | Business Management with Finance with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-finance-with-foundation-bsc |
| 8 | Business Management with Industrial Placement BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-industrial-placement-bsc |
| 9 | Business Management with Integrated Foundation Year and Industrial Placement BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-foundation-and-industrial-placement-bsc |
| 10 | Business Management with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-foundation-bsc |
| 11 | Business Management with Marketing  BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-marketing-bsc |
| 12 | Business Management with Marketing with Industrial Placement and Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-marketing-with-placement-and-foundation-year-bsc |
| 13 | Business Management with Marketing and Industrial Placement BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-marketing-industrial-placement-bsc |
| 14 | Business Management with Marketing and Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-marketing-and-foundation-year-bsc |
| 15 | Business Management with Psychology BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-psychology-bsc |
| 16 | Business Management with Psychology with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/business-management-with-psychology-with-foundation-bsc |
| 17 | Economics BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/economics-bsc |
| 18 | Economics with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/economics-with-foundation-bsc |
| 19 | Marketing BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/bsc-marketing-dubai |
| 20 | Marketing with Industrial Placement BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/bsc-marketing-and-industrial-placement-dubai |
| 21 | Money, Banking and Finance  BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/money-banking-and-finance-bsc |
| 22 | Money, Banking and Finance with Integrated Foundation Year BSc | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/business-and-finance-courses/money-banking-and-finance-with-foundation-bsc |

---

#### Business And Management

##### BSc (17 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-bsc |
| 2 | Business Management with Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-year-in-industry-bsc |
| 3 | Business Management with Business Analytics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-business-analytics-bsc |
| 4 | Business Management with Business Analytics and Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-business-analytics-and-year-in-industry-bsc |
| 5 | Business Management with Communications BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-communications-bsc |
| 6 | BSc Business Management with Communications and Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-comms-and-year-in-industry-bsc |
| 7 | Business Management with Human Resource Management BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-human-resource-management-bsc |
| 8 | Business Management with Human Resource Management with Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-human-resource-management-with-year-in-industry-bsc |
| 9 | Business Management with Marketing BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-marketing-bsc |
| 10 | Business Management with Marketing and Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-marketing-and-year-in-industry-bsc |
| 11 | Business Management with Operations and Supply Chain Management BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/business-management-with-operations-and-supply-chain-management-bsc |
| 12 | Business Management with Operations and Supply Chain Management and Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/bsc-business-management-with-operations-and-supply-chain-management-and-year-in-industry-bsc |
| 13 | International Business BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/international-business-bsc |
| 14 | Marketing BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/marketing-bsc |
| 15 | Marketing with Business Analytics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/marketing-with-business-analytics-bsc |
| 16 | Marketing with Business Analytics and Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/marketing-with-business-analytics-and-year-in-industry-bsc |
| 17 | Marketing with Year in Industry BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/business-and-management-courses/marketing-with-year-in-industry-bsc |

---

#### Economics

##### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/economics-ba |
| 2 | International Relations with Economics with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/international-relations-with-economics-with-year-abroad-ba |
| 3 | International Relations with Economics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/international-relations-with-economics-ba |

---

##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics and Politics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/economics-and-politics-bsc |
| 2 | Mathematical Economics and Statistics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/mathematical-economics-and-statistics-bsc |
| 3 | Economics BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/economics-bsc |
| 4 | Money, Banking and Finance BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/economics-courses/money-banking-and-finance-bsc |

---

#### Education

##### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Education and Sociology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/education-courses/education-and-sociology-ba |
| 2 | Education BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/education-courses/education-ba |

---

##### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology in Education BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/education-courses/psychology-in-education-bsc |

---

#### Media And Marketing

##### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media and Communications BA | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/media-and-marketing-courses/digital-media-and-communications-ba |
| 2 | Digital Media and Communications with Integrated Foundation Year BA | https://www.birmingham.ac.uk/dubai/study/undergraduate/subjects/media-and-marketing-courses/digital-media-and-communications-with-foundation-ba |

---

#### Politics International Relations And Development

##### BA (20 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | International Development and Politics with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-development-and-politics-with-year-abroad-ba |
| 2 | International Relations and Development with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-and-development-with-year-abroad-ba |
| 3 | International Relations with French BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-with-french-ba |
| 4 | International Relations with German BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-with-german-ba |
| 5 | International Relations with Spanish BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-with-spanish-ba |
| 6 | International Relations with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-with-year-abroad-ba |
| 7 | Politics and International Relations with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-international-relations-with-year-abroad-ba |
| 8 | Politics and Philosophy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-philosophy-ba |
| 9 | Politics and Social Policy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-social-policy-ba |
| 10 | Politics and Social Policy with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-social-policy-with-year-abroad-ba |
| 11 | Politics and Sociology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-sociology-ba |
| 12 | Politics and Sociology with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-sociology-with-year-abroad-ba |
| 13 | Politics with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-with-year-abroad-ba |
| 14 | Politics, Philosophy and Economics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-philosophy-and-economics-ba |
| 15 | International Development and Politics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-development-and-politics-ba |
| 16 | International Relations and Development BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-and-development-ba |
| 17 | International Relations BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/international-relations-ba |
| 18 | Policy, Politics and Economics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/policy-politics-and-economics-ba |
| 19 | Politics and International Relations BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-and-international-relations-ba |
| 20 | Politics BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/politics-ba |

---

##### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Public Policy BSc | https://www.birmingham.ac.uk/study/undergraduate/subjects/politics-international-relations-and-development-courses/artificial-intelligence-and-public-policy-bsc |

---

#### Social Policy Sociology And Criminology

##### BA (13 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/criminology-with-year-abroad-ba |
| 2 | Policy, Politics and Economics with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/policy-politics-economics-with-year-abroad-ba |
| 3 | Social Policy and Criminology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/social-policy-and-criminology-ba |
| 4 | Social Policy and Criminology with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/social-policy-and-criminology-with-year-abroad-ba |
| 5 | Sociology and Criminology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/sociology-and-criminology-ba |
| 6 | Sociology and Criminology with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/sociology-and-criminology-with-year-abroad-ba |
| 7 | Sociology and Social Policy  BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/social-policy-and-sociology-ba |
| 8 | Sociology and Social Policy with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/sociology-and-social-policy-with-year-abroad-ba |
| 9 | Sociology with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/sociology-with-year-abroad-ba |
| 10 | Criminology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/criminology-ba |
| 11 | Social Policy BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/social-policy-ba |
| 12 | Social Policy with Year Abroad BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/social-policy-with-year-abroad-ba |
| 13 | Sociology BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/sociology-ba |

---

##### BASc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Sciences BASc | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-policy-sociology-and-criminology-courses/ba-social-sciences |

---

#### Social Work

##### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work  BA | https://www.birmingham.ac.uk/study/undergraduate/subjects/social-work-courses/social-work-ba |

---

---

## SECTION 2 — Graduate education

> ⚠ P0: Postgraduate programme listing requires separate extraction. The postgraduate taught course search at `birmingham.ac.uk/study/postgraduate/taught/course-search` shows 56 pages of results (~560 estimated programmes). Postgraduate research programmes are listed separately. This is a P0 follow-up item.

### 2.1 Postgraduate taught (PGT)

The University of Birmingham offers MSc, MA, MBA, MRes, PG Cert, and PG Dip programmes across all 5 colleges. The PG taught course search shows 56 pages of results with approximately 10 programmes per page.

Example PG taught programmes (from first page of search):
- Accounting and Finance MSc (Dubai)
- Advanced Chemical Engineering MSc / PGDip
- Acute Medicine for Advanced Clinical Practice (PG micro-credential)

### 2.2 Postgraduate research (PGR)

PhD and MPhil programmes are offered across all 5 colleges. The Doctoral School (`birmingham.ac.uk/study/postgraduate/research/doctoral-school`) coordinates research degree admissions.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Application process

All undergraduate applications are submitted through UCAS. The University of Birmingham's UCAS campus code is **B32**.

### 3.2 Application deadlines

| Deadline | Applies to |
|----------|-----------|
| **15 October 2025** | Medicine (MBChB) and Dentistry (BDS) |
| **14 January 2026** | All other undergraduate courses (equal consideration deadline) |
| Applications open | September 2025 (via UCAS) |

> **Source**: `birmingham.ac.uk/study/undergraduate/apply`

### 3.3 Academic entry requirements

Entry requirements vary by course. General requirements include:
- Three GCE A levels (including International A Levels)
- International Baccalaureate Diploma
- SQA Highers and Advanced Highers
- Cambridge Pre-U (minimum 3 separate subjects)
- Irish Leaving Certificate Higher Level
- European Baccalaureate

Specific A-Level requirements are listed on individual course pages. Example: Accounting and Finance BSc requires AAA with GCSE Mathematics grade 6.

### 3.4 English language requirements

English proficiency can be demonstrated through IELTS, TOEFL, PTE, Cambridge English, Language Cert, Trinity ISE, or Oxford ELLT. Tests must be taken within two years of the programme start date.

Undergraduate courses are divided into 4 groups (A-D) based on subject area:

#### Group A — Engineering, Sciences, Geography, Maths, Computer Science, Sport Science

| Test | Minimum Score |
|------|--------------|
| IELTS Academic | 6.0 overall, no less than 5.5 in any band |
| TOEFL iBT | 80 overall (19R, 19L, 21S, 19W) |
| PTE Academic | 64 with no less than 59 in all four skills |
| Cambridge English (Advanced) | 169 overall, no less than 162 in any component |
| Language Cert ESOL SELT (UKVI) | B2 Communicator, no less than 25 in each skill |
| Trinity ISE II | Distinction in all skills |
| Language Cert Academic | 60 in all skills |
| Oxford ELLT | 6 overall, no less than 5 in each skill |

#### Group B — Business, Social Sciences, Arts, Law, Education, Psychology, Liberal Arts

| Test | Minimum Score |
|------|--------------|
| IELTS Academic | 6.5 overall, no less than 6.0 in any band |
| TOEFL iBT | 88 overall (21R, 20L, 22S, 21W) |
| PTE Academic | 67 with no less than 64 in all four skills |
| Cambridge English (Advanced) | 176 overall, no less than 169 in any component |
| Language Cert ESOL SELT (UKVI) | B2 Communicator, no less than 33 in each skill |
| Trinity ISE III | Pass in each skill |
| Language Cert Academic | 65 in all skills |
| Oxford ELLT | 7 overall, no less than 7 in speaking and writing |

> **Business School note**: IELTS 6.5 overall with minimum 6.5 in Writing and Speaking.

#### Group C — Dental Hygiene, Pharmacy, Physiotherapy, Social Work

| Test | Minimum Score |
|------|--------------|
| IELTS Academic | 7.0 overall, no less than 6.5 in any band |
| TOEFL iBT | 95 overall, no less than 22 in any band |
| PTE Academic | 76 with no less than 67 in all four skills |
| Cambridge English | 185 overall, no less than 176 in any component |
| Language Cert ESOL SELT (UKVI) | C1 Expert, no less than 25 in each skill |
| Trinity ISE III | Merit in Writing, Pass in other skills |
| Language Cert Academic | 70 in all skills |

#### Group D — Dentistry BDS, Medicine MBChB, Nursing

| Test | Minimum Score |
|------|--------------|
| IELTS Academic | 7.0 overall, no less than 7.0 in any band |
| TOEFL iBT | 95 overall, no less than 23 in any band |
| PTE Academic | 67 in all four skills |
| Cambridge English | 185 overall, no less than 185 in any component |
| Trinity ISE IV | Pass in each skill |
| Language Cert Academic | 70 in all skills |

> **Source**: `birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements`

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees

#### UK (Home) students

| Academic Year | Annual Tuition Fee |
|--------------|-------------------|
| 2026/27 | £9,790 |
| 2025/26 | £9,535 |
| 2024/25 | £9,250 |

#### International students

International tuition fees vary by programme and are displayed on individual course pages after selecting a country. Example fees:

| Course | International Fee (2026) |
|--------|------------------------|
| Accounting and Finance BSc | £29,160 |
| Typical lab/science subjects | ~£28,000 - £32,000 |
| Typical classroom subjects | ~£22,000 - £28,000 |
| Clinical subjects (Medicine/Dentistry) | ~£40,000 - £48,000 |

> **Note**: International fees are dynamic on each course page. Selecting a non-UK country from the dropdown reveals the international fee. The fee paid in the first year remains constant with no inflationary increase for the duration of the course (except clinical courses and International Foundation Programme).

#### Placement year fees

| Fee status | Study abroad year | Industrial placement year |
|-----------|------------------|--------------------------|
| Home (UK) | 15% of tuition fee | 20% of tuition fee |
| International | 50% of tuition fee | 50% of tuition fee |

### 4.2 Living costs

> ⚠ P1: Living costs page available at `birmingham.ac.uk/study/undergraduate/fees-funding/living-costs` — requires separate extraction.

### 4.3 Scholarships

International students can explore scholarships at `birmingham.ac.uk/study/international/fees/scholarships`. The University offers a range of scholarships, bursaries, and other awards for both UK and international students.

> **Sources**:
> - `birmingham.ac.uk/study/undergraduate/fees-funding/tuition`
> - `birmingham.ac.uk/study/international/fees`
> - Individual course pages for international fee amounts

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Birmingham"
  source_url: https://www.birmingham.ac.uk
  source_snippet: "University of Birmingham"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.ug_course_count
  value: "366 undergraduate degree programmes"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/course-search
  source_snippet: "37 paginated pages, 10 courses per page, 366 total unique courses extracted"
  capture_date: 2026-07-08
  evidence_type: extracted_data

E-U-003:
  field: institution.colleges
  value: "5 colleges: Arts and Law, Engineering and Physical Sciences, Life and Environmental Sciences, Medicine and Health, Social Sciences"
  source_url: https://www.birmingham.ac.uk/about/colleges-schools-and-departments
  source_snippet: "A-Z listing of all colleges, schools, and departments at the University of Birmingham"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.schools_count
  value: "~80 academic units across 5 colleges"
  source_url: https://www.birmingham.ac.uk/about/colleges-schools-and-departments
  source_snippet: "A-Z listing of all academic units"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: costs.ug_home_tuition_2026_27
  value: "£9,790"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/fees-funding/tuition
  source_snippet: "If your offer is for 2026 year of entry, we expect that the tuition fee for your first year of study will be £9,790"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: costs.ug_home_tuition_2025_26
  value: "£9,535"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/fees-funding/tuition
  source_snippet: "If your offer is for 2025 year of entry, we expect that the tuition fee for your first year of study will be £9,535"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: costs.ug_international_example_accounting
  value: "£29,160"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/subjects/accounting-and-finance-courses/accounting-and-finance-bsc
  source_snippet: "Fees (international): £29,160 (after selecting China from country dropdown)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: costs.international_fee_policy
  value: "Fee paid in first year remains constant with no inflationary increase for duration of course (except clinical courses and IFP)"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/fees-funding/tuition
  source_snippet: "The fee paid in your first year will remain constant with no inflationary increase for the duration of your course, with the exception of the International Foundation Programme and clinical courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: costs.placement_year_fees
  value: "Home: 15% (study abroad) / 20% (placement); International: 50% for both"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/fees-funding/tuition
  source_snippet: "International students who spend an entire year studying abroad or on an industrial placement will pay 50% of their agreed tuition fee"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: admissions.deadlines.medicine_dentistry
  value: "15 October 2025"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply
  source_snippet: "For Medicine and Dentistry, the deadline was Wednesday 15 October 2025"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: admissions.deadlines.most_courses
  value: "14 January 2026"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply
  source_snippet: "The application deadline for most courses was Wednesday 14 January 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: admissions.ucas_code
  value: "B32"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply
  source_snippet: "The University of Birmingham's UCAS campus code number is B32"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: admissions.english.group_a_ielts
  value: "IELTS 6.0 overall, no less than 5.5 in any band"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements
  source_snippet: "Group A: IELTS 6.0 overall with no less than 5.5 in any band"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: admissions.english.group_b_ielts
  value: "IELTS 6.5 overall, no less than 6.0 in any band"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements
  source_snippet: "Group B: IELTS 6.5 overall with no less than 6.0 in any band"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: admissions.english.group_c_ielts
  value: "IELTS 7.0 overall, no less than 6.5 in any band"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements
  source_snippet: "Group C: IELTS 7.0 overall with no less than 6.5 in any band"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: admissions.english.group_d_ielts
  value: "IELTS 7.0 overall, no less than 7.0 in any band"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements
  source_snippet: "Group D: IELTS 7.0 overall with no less than 7.0 in any band"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: admissions.english.accepted_tests
  value: "IELTS Academic, TOEFL iBT, PTE Academic, Cambridge English, Language Cert ESOL SELT, Trinity ISE, Language Cert Academic, Oxford ELLT"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/apply/entry-requirements/international-entry-requirements
  source_snippet: "For those joining us for 2026, we will accept the following additional tests as evidence of English language proficiency"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: admissions.ug_course_count
  value: "366 unique undergraduate degree programmes"
  source_url: https://www.birmingham.ac.uk/study/undergraduate/course-search
  source_snippet: "37 pages extracted via Next-button pagination, 366 unique courses identified"
  capture_date: 2026-07-08
  evidence_type: extracted_data
```

---

## SECTION 6 — WeKnora import manifest

### 6.1 Chunking recommendations

| Chunk level | Granularity | Approx count | Recommended chunk size |
|------------|-------------|-------------|----------------------|
| L0: Institution | Full document | 1 | ~5,000 tokens |
| L1: Section | Sections 0-7 | 8 | ~2,000 tokens each |
| L2: College | Per-college course listings | 5 | ~3,000 tokens each |
| L3: Subject | Per-subject course tables | 47 | ~500 tokens each |
| L4: Programme | Individual programme entry | 366 | ~100 tokens each |

### 6.2 Follow-up data items (prioritized)

| Priority | Data item | Current status |
|----------|-----------|---------------|
| **P0** | Full PG taught course listing (MSc/MA/MBA) | 56 pages, ~560 programmes, needs extraction |
| **P0** | Full PG research programme listing (PhD/MPhil) | Separate listing, needs extraction |
| **P0** | International tuition fees by course (complete table) | Dynamic per course page, needs systematic extraction |
| **P1** | Per-course A-Level/IB entry requirements | Available on individual course pages |
| **P1** | Living costs (accommodation, food, etc.) | Page exists, needs extraction |
| **P1** | Scholarship and funding details | Page exists, needs extraction |
| **P2** | Course module details and curriculum structure | Available on individual course pages |
| **P2** | Dubai campus programme details | 2 BCL programmes + others, needs extraction |

### 6.3 Data freshness schedule

| Data category | Change frequency | Recommended re-check |
|--------------|-----------------|---------------------|
| Course listings | Medium (annual update) | Every 6 months |
| Tuition fees | High (annual increase) | Every 3 months |
| English language requirements | Low (policy change) | Every 12 months |
| Application deadlines | High (annual cycle) | Every 6 months |
| College/school structure | Low (organisational change) | Every 12 months |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Birmingham | Cardiff | Newcastle | Durham |
|-----------|--------|---------|-----------|--------|
| Total UG programmes | 366 | 237 | 147 | P0 |
| Colleges | 5 | 3 | 3 | 3 |
| Academic units | ~80 | 24 | 30 | 26 |
| Russell Group | Yes | Yes | Yes | Yes |
| Region | England (West Midlands) | Wales | England (North East) | England (North East) |
| UG home tuition (2026/27) | £9,790 | P0 | P0 | P0 |
| UG international range | £22K-£48K | P0 | P0 | P0 |
| IELTS minimum (UG) | 6.0 (Group A) | P0 | P0 | P0 |
| UCAS deadline (most) | 14 Jan 2026 | 14 Jan 2026 | 14 Jan 2026 | 14 Jan 2026 |
| Medicine/Dentistry deadline | 15 Oct 2025 | 15 Oct 2025 | 15 Oct 2025 | 15 Oct 2025 |
| Dubai/international campus | Yes | No | No | No |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University of Birmingham official website (`birmingham.ac.uk`)
> **Granularity**: college -> subject area -> degree-level -> program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (366) | PG programmes ⚠ P0 | Evidence (18 blocks) ✅ | Language requirements ✅ (4 groups) | Tuition fees ✅ (home + international examples)
> **Next step**: PG extraction (taught + research), international fees per course, per-course entry requirements

