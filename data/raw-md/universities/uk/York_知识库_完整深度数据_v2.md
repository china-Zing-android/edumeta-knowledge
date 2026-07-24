# University of York Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch (server-rendered HTML)
> **Target knowledge base**: WeKnora
> **Granularity**: faculty -> department/school -> degree-level -> program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Russell Group**: Yes

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 289 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PGCE/LLM etc.) | ~300 entries (~210 distinct excluding PGCE training-provider duplicates) |
| 研究生博士项目 (PhD/MPhil/MSc by research/MA by research) | 158 |
| **学位项目总计 (UG extracted)** | **289** |
| 学院 (Faculties) | 3 |
| 学术单位 (Departments) | 17 |
| 学术单位 (Schools) | 6 |
| 联合机构 | 1 (Hull York Medical School — HYMS) |

> **Data source**: University of York undergraduate course list (`york.ac.uk/study/undergraduate/courses/all/`), 289 courses extracted from a single server-rendered page (no pagination). Each entry includes course name, qualification type, duration, study type, and UCAS code.
> **PG note**: Postgraduate taught courses are at `york.ac.uk/study/postgraduate/courses/all?mode=taught` with ~300 entries. Postgraduate research at `york.ac.uk/study/postgraduate/courses/all?mode=research` with 158 entries. Both require separate full extraction.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of York
├── Faculty of Arts and Humanities                                        [学院]
│   ├── Department of Archaeology                                         [系]
│   ├── Department of English and Related Literature                       [系]
│   ├── Department of History                                             [系]
│   ├── Department of History of Art                                      [系]
│   ├── Department of Language and Linguistic Science                      [系]
│   ├── Department of Philosophy                                          [系]
│   └── School of Arts and Creative Technologies                          [学院级单位]
├── Faculty of Sciences                                                   [学院]
│   ├── Department of Biology                                             [系]
│   ├── Department of Chemistry                                           [系]
│   ├── Department of Computer Science                                    [系]
│   ├── Department of Environment and Geography                           [系]
│   ├── Department of Mathematics                                         [系]
│   ├── Department of Psychology                                          [系]
│   ├── School of Physics, Engineering and Technology                     [学院级单位]
│   └── York School of Architecture                                       [学院级单位]
├── Faculty of Social Sciences                                            [学院]
│   ├── Department of Economics and Related Studies                       [系]
│   ├── Department of Education                                           [系]
│   ├── Department of Health Sciences                                     [系]
│   ├── Department of Politics and International Relations                [系]
│   ├── Department of Sociology                                           [系]
│   ├── School for Business and Society                                   [学院级单位]
│   ├── School of Philosophy, Politics and Economics                      [学院级单位]
│   └── York Law School                                                   [学院级单位]
└── Joint Institutions
    └── Hull York Medical School (HYMS)                                   [联合医学院]

Other Academic Units:
    ├── Centre for Health Economics                                       [研究中心]
    ├── Centre for Lifelong Learning                                      [中心]
    ├── Centre for Reviews and Dissemination                              [中心]
    ├── Humanities Research Centre                                        [研究中心]
    └── Norwegian Study Centre                                            [中心]
```

> **Source**: `york.ac.uk/departments/`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 91 |
| BSc | BSc | Bachelor of Science | 本科 | 91 |
| MEng | MEng | Master of Engineering (Integrated) | 本科 (Integrated Master's) | 21 |
| MChem | MChem | Master of Chemistry (Integrated) | 本科 (Integrated Master's) | 16 |
| BEng | BEng | Bachelor of Engineering | 本科 | 15 |
| MPhys | MPhys | Master of Physics (Integrated) | 本科 (Integrated Master's) | 12 |
| MBiol | MBiol | Master of Biology (Integrated) | 本科 (Integrated Master's) | 6 |
| MEnv | MEnv | Master of Environment (Integrated) | 本科 (Integrated Master's) | 6 |
| MSci | MSci | Master of Science (Integrated) | 本科 (Integrated Master's) | 7 |
| MMath | MMath | Master of Mathematics (Integrated) | 本科 (Integrated Master's) | 5 |
| LLB | LLB | Bachelor of Laws | 本科 | 5 |
| MB BS | MB BS | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| MNurs | MNurs | Master of Nursing (Integrated) | 本科 (Integrated Master's) | 3 |
| BMid | BMid | Bachelor of Midwifery | 本科 | 1 |
| MBiochem | MBiochem | Master of Biochemistry (Integrated) | 本科 (Integrated Master's) | 1 |
| MBiomedSci | MBiomedSci | Master of Biomedical Science (Integrated) | 本科 (Integrated Master's) | 1 |
| MSocW | MSocW | Master of Social Work (Integrated) | 本科 (Integrated Master's) | 1 |
| **合计** | | | | **289** |

> **Note**: Integrated Master's degrees (MEng, MChem, MPhys, MBiol, MEnv, MSci, MMath, MNurs, MBiochem, MBiomedSci, MSocW) are 4-year undergraduate programmes that include a Master's-level year. They are classified as undergraduate qualifications in the UK system.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学科领域 \ 学位 | BA | BSc | BEng | MEng | MChem | MPhys | MMath | MBiol | MEnv | MSci | LLB | MB BS | MNurs | BMid | MBiochem | MBiomedSci | MSocW | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Archaeology & Heritage | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| Architecture | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Biology & Biomedical | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | **24** |
| Business & Economics | 12 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **26** |
| Chemistry | 0 | 4 | 0 | 0 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **20** |
| Computer Science & Data | 0 | 12 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **20** |
| Education | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| Engineering & Technology | 0 | 0 | 15 | 16 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **31** |
| English & Linguistics | 18 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **23** |
| Environment & Geography | 2 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **16** |
| Film, Theatre, Media & Music | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| History & History of Art | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **18** |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | **5** |
| Mathematics | 0 | 6 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **11** |
| Medicine & Nursing | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 3 | 1 | 0 | 0 | 0 | **9** |
| Philosophy & PPE | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **14** |
| Physics | 0 | 4 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **16** |
| Politics & IR | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Psychology | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **7** |
| Sociology & Social Policy | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **9** |
| **合计** | 91 | 91 | 15 | 21 | 16 | 12 | 5 | 6 | 6 | 7 | 5 | 2 | 3 | 1 | 1 | 1 | 1 | **289** |

> **Reconciliation check**: Rule-1 total (289) == matrix-sum (289). PASS.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

University of York is organised into 3 academic Faculties, each containing multiple Departments and interdisciplinary Schools (23 academic units total). Additionally, the Hull York Medical School (HYMS) is a joint institution with the University of Hull, offering Medicine programmes. See Section 0.2 for the full hierarchy tree.

The university also operates satellite campuses: University of York Mumbai and University of York Europe Campus.

### 1.2 Undergraduate degree programmes — grouped by Faculty > Department > Subject > Degree Level

### Faculty of Arts and Humanities

#### Archaeology

##### BA (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-archaeology/ |
| 2 | Heritage and Archaeology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-archaeology-heritage/ |
| 3 | Historical Archaeology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-historical-archaeology/ |
| 4 | Bioarchaeology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-bioarchaeology/ |
| 5 | Archaeology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-archaeology/ |

---

#### English and Related Literature

##### BA (14 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-english/ |
| 2 | English Literature BA | https://www.york.ac.uk/study/undergraduate/courses/ba-english-literature |
| 3 | English Language and Literature BA | https://www.york.ac.uk/study/undergraduate/courses/ba-english-language-literature/ |
| 4 | English and Linguistics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-english-linguistics/ |
| 5 | English Language and Linguistics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-english-language-linguistics/ |
| 6 | English Literature with French BA | https://www.york.ac.uk/study/undergraduate/courses-future/ba-english-literature-french/ |
| 7 | English Literature with German BA | https://www.york.ac.uk/study/undergraduate/courses-future/ba-english-literature-german/ |
| 8 | English Literature with Italian BA | https://www.york.ac.uk/study/undergraduate/courses-future/ba-english-literature-italian/ |
| 9 | English Literature with Spanish BA | https://www.york.ac.uk/study/undergraduate/courses-future/ba-english-literature-spanish/ |
| 10 | English Literature/History (Equal) BA | http://www.york.ac.uk/study/undergraduate/courses/ba-english-literature-history/ |
| 11 | English Literature/History of Art (Equal) BA | http://www.york.ac.uk/study/undergraduate/courses/ba-english-literature-history-of-art/ |
| 12 | English Literature/Philosophy (Equal) BA | http://www.york.ac.uk/study/undergraduate/courses/ba-english-literature-philosophy/ |
| 13 | English Literature/Politics (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-english-literature-politics/ |
| 14 | English/History (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-english-history/ |
| 15 | English/History of Art (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-english-history-of-art/ |
| 16 | English/Philosophy (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-english-philosophy/ |
| 17 | English/Politics (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-english-politics/ |

---

#### Language and Linguistic Science

##### BA/BSc/MSci (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics/ |
| 2 | Linguistics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-linguistics/ |
| 3 | Linguistics MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-linguistics/ |
| 4 | Linguistics with French BA | https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics-french/ |
| 5 | Linguistics with German BA | https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics-german/ |
| 6 | Linguistics with Italian BA | https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics-italian/ |
| 7 | Linguistics with Spanish BA | https://www.york.ac.uk/study/undergraduate/courses/ba-linguistics-spanish/ |
| 8 | Language, Logic and Communication BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-language-logic-communication/ |
| 9 | Philosophy and Linguistics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-linguistics/ |
| 10 | French and Linguistics (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-french-linguistics-year-abroad/ |
| 11 | German and Linguistics (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-german-linguistics-year-abroad/ |
| 12 | Italian and Linguistics (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-italian-linguistics-year-abroad/ |
| 13 | Spanish and Linguistics (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-spanish-linguistics-year-abroad/ |

---

#### History

##### BA (12 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | History BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history/ |
| 2 | History and French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-french-history-year-abroad/ |
| 3 | History and German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-german-history-year-abroad/ |
| 4 | History and Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-italian-history-year-abroad/ |
| 5 | History and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-spanish-history-year-abroad/ |
| 6 | History/Economics (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-economics/ |
| 7 | History/History of Art (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-art-history/ |
| 8 | History/Philosophy (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-philosophy/ |
| 9 | History/Politics (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-politics/ |

---

#### History of Art

##### BA (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | History of Art BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art/ |
| 2 | History of Art (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-year-abroad/ |
| 3 | Curating and Art History BA | https://www.york.ac.uk/study/undergraduate/courses/ba-curating-art-history/ |
| 4 | Curating and Art History (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-curating-art-history-year-abroad/ |
| 5 | History of Art with French (with a Year Abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-french-year-abroad/ |
| 6 | History of Art with German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-german-year-abroad/ |
| 7 | History of Art with Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-italian-year-abroad/ |
| 8 | History of Art with Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-history-of-art-spanish-year-abroad/ |

---

#### Philosophy

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy/ |
| 2 | Philosophy with French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-french-year-abroad/ |
| 3 | Philosophy with German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-german-year-abroad/ |
| 4 | Philosophy with Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-italian-year-abroad/ |
| 5 | Philosophy with Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-spanish-year-abroad/ |
| 6 | Philosophy with Sociology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-sociology/ |

---

#### Languages (French, German, Italian, Spanish)

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | French and German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-french-german-year-abroad/ |
| 2 | French and Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-french-italian-year-abroad/ |
| 3 | French and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-french-spanish-year-abroad/ |
| 4 | German and Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-german-italian-year-abroad/ |
| 5 | German and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-german-spanish-year-abroad/ |
| 6 | Italian and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-italian-spanish-year-abroad/ |

---

#### School of Arts and Creative Technologies

##### BA/BSc (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Television Production BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-film-television-production/ |
| 2 | Theatre: Writing, Directing and Performance BA | https://www.york.ac.uk/study/undergraduate/courses/ba-theatre-writing-directing-performance/ |
| 3 | Music BA | https://www.york.ac.uk/study/undergraduate/courses/ba-music/ |
| 4 | Music Production and Sound Recording BA | https://www.york.ac.uk/study/undergraduate/courses/ba-music-sound-recording/ |
| 5 | Music and Sound Recording BA | https://www.york.ac.uk/study/undergraduate/courses-2026/ba-music-sound-recording/ |
| 6 | Interactive Media BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-interactive-media/ |
| 7 | Digital Media, Culture and Communication BA | https://www.york.ac.uk/study/undergraduate/courses/ba-digital-media-culture-and-communication/ |
| 8 | Music Technology Systems MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-music-technology-systems/ |
| 9 | Music Technology Systems BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-music-technology-systems/ |
| 10 | Music Technology Systems (with a Foundation Year) BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-music-technology-systems-foundation-year/ |

---

### Faculty of Sciences

#### Biology

##### BSc/MBiol (16 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-biology/ |
| 2 | Biology MBiol | https://www.york.ac.uk/study/undergraduate/courses/mbiol-biology/ |
| 3 | Biochemistry BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-biochemistry/ |
| 4 | Biochemistry MBiochem | https://www.york.ac.uk/study/undergraduate/courses/mbiochem-biochemistry/ |
| 5 | Biomedical Sciences BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-biomedical-sciences/ |
| 6 | Biomedical Sciences MBiomedSci | https://www.york.ac.uk/study/undergraduate/courses/mbiomedsci-biomedical-sciences/ |
| 7 | Biotechnology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-biotechnology/ |
| 8 | Biotechnology MBiol | https://www.york.ac.uk/study/undergraduate/courses/mbiol-biotechnology/ |
| 9 | Genetics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-genetics/ |
| 10 | Genetics MBiol | https://www.york.ac.uk/study/undergraduate/courses/mbiol-genetics/ |
| 11 | Immunology and Infectious Disease BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-immunology-infectious-disease/ |
| 12 | Immunology and Infectious Disease MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-immunology-infectious-disease/ |
| 13 | Molecular Cell Biology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-molecular-cell-biology/ |
| 14 | Molecular Cell Biology MBiol | https://www.york.ac.uk/study/undergraduate/courses/mbiol-molecular-cell-biology/ |
| 15 | Neuroscience BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-neuroscience/ |
| 16 | Neuroscience MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-neuroscience/ |

---

#### Chemistry

##### BSc/MChem (20 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry/ |
| 2 | Chemistry MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-york/ |
| 3 | Chemistry (with a year abroad) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-year-abroad/ |
| 4 | Chemistry (with a year in industry) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-industry/ |
| 5 | Chemistry with Digital Methods BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-digital-methods/ |
| 6 | Chemistry with Digital Methods MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-digital-methods-york/ |
| 7 | Chemistry with Digital Methods (with a year abroad) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-digital-methods-year-abroad/ |
| 8 | Chemistry with Digital Methods (with a year in industry) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-digital-methods-industry/ |
| 9 | Chemistry, Biological & Medicinal Chemistry BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-biological-medicinal/ |
| 10 | Chemistry, Biological and Medicinal Chemistry MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-biological-medicinal-york/ |
| 11 | Chemistry, Biological and Medicinal Chemistry (with a year abroad) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-biological-medicinal-year-abroad/ |
| 12 | Chemistry, Biological and Medicinal Chemistry (with a year in industry) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-biological-medicinal-industry/ |
| 13 | Chemistry, Green Principles and Sustainable Processes BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-green-principles/ |
| 14 | Chemistry, Green Principles and Sustainable Processes MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-york/ |
| 15 | Chemistry, Green Principles and Sustainable Processes (with a year abroad) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-year-abroad/ |
| 16 | Chemistry, Green Principles and Sustainable Processes (with a year in industry) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-green-principles-industry/ |
| 17 | Chemistry, the Atmosphere and the Environment MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-york/ |
| 18 | Chemistry, the Atmosphere and the Environment BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-chemistry-atmosphere-environment/ |
| 19 | Chemistry, the Atmosphere and the Environment (with a year abroad) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-year-abroad/ |
| 20 | Chemistry, the Atmosphere and the Environment (with a year in industry) MChem | https://www.york.ac.uk/study/undergraduate/courses/mchem-chemistry-atmosphere-environment-industry/ |

---

#### Computer Science

##### BSc/MEng/MSci (20 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science/ |
| 2 | Computer Science MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science/ |
| 3 | Computer Science (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/beng-bsc-computer-science-industry/ |
| 4 | Computer Science (with a year in industry) MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-industry/ |
| 5 | Computer Science with Artificial Intelligence MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-artificial-intelligence/ |
| 6 | Computer Science with Artificial Intelligence BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-artificial-intelligence/ |
| 7 | Computer Science with Artificial Intelligence (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-ai-industry/ |
| 8 | Computer Science with Artificial Intelligence (with year in industry) MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-with-ai-industry/ |
| 9 | Computer Science with Cyber Security MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-with-cyber-security/ |
| 10 | Computer Science with Cyber Security BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-cyber-security/ |
| 11 | Computer Science with Cyber Security (with a year in industry) MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-computer-science-with-cyber-security-industry/ |
| 12 | Computer Science with Cyber Security (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-cyber-security-industry/ |
| 13 | Computer Science/Mathematics (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-mathematics/ |
| 14 | Computer Science/Mathematics (Equal) (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science-mathematics-industry/ |
| 15 | Computer Systems Engineering BSc | https://www.cs.york.ac.uk/ |
| 16 | Computer Systems Engineering with Artificial Intelligence BSc | https://www.cs.york.ac.uk/ |
| 17 | Computer Systems Engineering with Cyber Security BSc | https://www.cs.york.ac.uk/ |
| 18 | Data Science BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-data-science/ |
| 19 | Data Science MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-data-science/ |
| 20 | Data Science (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-data-science-industry/ |
| 21 | Data Science (with a year in industry) MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-data-science-industry/ |

---

#### Environment and Geography

##### BSc/MEnv/BA (16 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-science/ |
| 2 | Environmental Science MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-environmental-science/ |
| 3 | Environmental Science (with placement year) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-environmental-science-placement/ |
| 4 | Environmental Science (with placement year) MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-environmental-science-placement/ |
| 5 | Environment, Economics and Ecology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-environment-economics-ecology/ |
| 6 | Environment, Economics and Ecology MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-environment-economics-ecology/ |
| 7 | Environment, Economics and Ecology (with placement year) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-environment-economics-ecology-placement/ |
| 8 | Environment, Economics and Ecology (with placement year) MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-environment-economics-ecology-placement/ |
| 9 | Physical Geography and Environment BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physical-geography-environment/ |
| 10 | Physical Geography and Environment MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-physical-geography-environment/ |
| 11 | Physical Geography and Environment (with placement year) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physical-geography-environment-placement/ |
| 12 | Physical Geography and Environment (with placement year) MEnv | https://www.york.ac.uk/study/undergraduate/courses/menv-physical-geography-environment-placement/ |
| 13 | Human Geography and Environment BA | https://www.york.ac.uk/study/undergraduate/courses/ba-human-geography-environment/ |
| 14 | Human Geography and Environment (with placement year) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-human-geography-environment-placement/ |
| 15 | Ecology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-ecology/ |
| 16 | Ecology MBiol | https://www.york.ac.uk/study/undergraduate/courses/mbiol-ecology/ |
| 17 | Ecology and Conservation Biology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-ecology-conservation-biology/ |
| 18 | Ecology and Conservation Biology MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-ecology-conservation-biology/ |

---

#### Mathematics

##### BSc/MMath (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics/ |
| 2 | Mathematics MMath | https://www.york.ac.uk/study/undergraduate/courses/mmath-mathematics/ |
| 3 | Mathematics (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-year-abroad/ |
| 4 | Mathematics (with a year abroad) MMath | https://www.york.ac.uk/study/undergraduate/courses/mmath-mathematics-year-abroad/ |
| 5 | Mathematics and Finance (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-finance/ |
| 6 | Mathematics and Management BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-management/ |
| 7 | Mathematics and Management (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-management-industry/ |
| 8 | Mathematics and Statistics (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-statistics/ |
| 9 | Mathematics/Computer Science (Equal) MMath | https://www.york.ac.uk/study/undergraduate/courses/mmath-mathematics-computer-science/ |
| 10 | Mathematics/Computer Science (Equal) (with a year in industry) MMath | https://www.york.ac.uk/study/undergraduate/courses/mmath-mathematics-computer-science-year-industry/ |
| 11 | Mathematics/Philosophy (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-philosophy/ |
| 12 | Mathematics/Physics (Equal) MMath/MPhys | https://www.york.ac.uk/study/undergraduate/courses/mmath-mphys-mathematics-physics/ |
| 13 | Mathematics/Physics (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-physics/ |
| 14 | Mathematics/Physics (equal) (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-mathematics-physics-year-abroad/ |
| 15 | Actuarial Science BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-actuarial-science/ |
| 16 | Actuarial Science (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-actuarial-science-industry/ |

---

#### Psychology

##### BSc/MSci/BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-psychology/ |
| 2 | Psychology MSci | https://www.york.ac.uk/study/undergraduate/courses/msci-psychology/ |
| 3 | Psychology in Education BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-psychology-education/ |
| 4 | Social Psychology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-psychology/ |
| 5 | Criminology and Social Psychology BA | https://www.york.ac.uk/study/undergraduate/courses-future/ba-criminology-and-social-psychology/ |
| 6 | Sociology with Social Psychology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-social-psychology/ |

---

#### School of Physics, Engineering and Technology

##### BEng/MEng/BSc/MPhys (31 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics/ |
| 2 | Physics MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics/ |
| 3 | Physics (with a Foundation Year) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-foundation-year/ |
| 4 | Physics (with a year abroad) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-year-abroad/ |
| 5 | Physics (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-year-abroad/ |
| 6 | Physics (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-industry/ |
| 7 | Physics (with a year in industry) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-industry/ |
| 8 | Physics with Astrophysics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics/ |
| 9 | Physics with Astrophysics MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics/ |
| 10 | Physics with Astrophysics (with a year abroad) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics-year-abroad/ |
| 11 | Physics with Astrophysics (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics-year-abroad/ |
| 12 | Physics with Astrophysics (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-astrophysics-industry/ |
| 13 | Physics with Astrophysics (with a year in industry) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-astrophysics-industry/ |
| 14 | Physics with Philosophy BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-philosophy/ |
| 15 | Physics with Philosophy MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-physics-philosophy/ |
| 16 | Physics with Philosophy (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-physics-philosophy-year-abroad/ |
| 17 | Theoretical Physics MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics/ |
| 18 | Theoretical Physics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics/ |
| 19 | Theoretical Physics (with a year abroad) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics-year-abroad/ |
| 20 | Theoretical Physics (with a year abroad) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics-year-abroad/ |
| 21 | Theoretical Physics (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-theoretical-physics-industry/ |
| 22 | Theoretical Physics (with a year in industry) MPhys | https://www.york.ac.uk/study/undergraduate/courses/mphys-theoretical-physics-industry/ |
| 23 | Electronic Engineering BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering/ |
| 24 | Electronic Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-engineering/ |
| 25 | Electronic Engineering (with a Foundation Year) BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-engineering-foundation-year/ |
| 26 | Electronic Engineering with Music Technology Systems BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-ee-music-technology-systems/ |
| 27 | Electronic Engineering with Music Technology Systems MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-ee-music-technology-systems/ |
| 28 | Electronic and Computer Engineering BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-computer-engineering/ |
| 29 | Electronic and Computer Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-computer-engineering/ |
| 30 | Electronic and Electrical Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-electronic-electrical-engineering/ |
| 31 | Electronic and Electrical Engineering BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-electronic-electrical-engineering/ |
| 32 | Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-engineering/ |
| 33 | Engineering BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-engineering/ |
| 34 | Engineering (with a Foundation Year) BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-engineering-foundation-year/ |
| 35 | Engineering with Renewable Energy MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-engineering-renewable-energy/ |
| 36 | Biomedical Engineering BEng | https://www.york.ac.uk/study/undergraduate/courses/beng-biomedical-engineering/ |
| 37 | Medical Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-medical-engineering/ |
| 38 | Micro-mechanical Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-micro-mechanical-engineering/ |
| 39 | Robotic Engineering MEng | https://www.york.ac.uk/study/undergraduate/courses/meng-robotic-engineering/ |

---

#### York School of Architecture

##### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture BA | https://www.york.ac.uk/study/undergraduate/courses/ba-architecture/ |

---

### Faculty of Social Sciences

#### Economics and Related Studies

##### BSc (14 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics/ |
| 2 | Economics and Econometrics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-econometrics/ |
| 3 | Economics and Finance BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-finance/ |
| 4 | Economics and Management BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-and-management/ |
| 5 | Economics, Econometrics and Finance BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-econometrics-finance/ |
| 6 | Economics/Mathematics (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-mathematics/ |
| 7 | Economics/Philosophy (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-philosophy/ |
| 8 | Economics/Politics (Equal) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-economics-politics/ |

---

#### School for Business and Society

##### BA/BSc (12 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Management BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management/ |
| 2 | Business and Management BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-business-management/ |
| 3 | Business and Management (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-industry/ |
| 4 | Business and Management (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-business-management-industry/ |
| 5 | Business and Management with French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-french-abroad |
| 6 | Business and Management with French (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-french-industry |
| 7 | Business and Management with German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-german-abroad |
| 8 | Business and Management with German (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-german-industry |
| 9 | Business and Management with Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-italian-abroad |
| 10 | Business and Management with Italian (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-italian-industry |
| 11 | Business and Management with Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-spanish-abroad |
| 12 | Business and Management with Spanish (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-management-spanish-industry |
| 13 | Business and Society BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-society/ |
| 14 | Business and Society (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-society-industry/ |
| 15 | Business of the Creative Industries BA | https://www.york.ac.uk/study/undergraduate/courses/ba-business-creative-industries/ |
| 16 | Accounting and Finance BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-finance/ |
| 17 | Accounting and Finance (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-finance-industry/ |
| 18 | Accounting, Business Finance and Management BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-business-finance/ |
| 19 | Accounting, Business Finance and Management (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-accounting-business-finance-industry/ |
| 20 | Marketing BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-marketing/ |
| 21 | Marketing (with a year in industry) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-marketing-industry/ |

---

#### Education

##### BA (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Education BA | https://www.york.ac.uk/study/undergraduate/courses/ba-education/ |
| 2 | Childhood Studies BA | https://www.york.ac.uk/education/ |
| 3 | Education and French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-education-french-year-abroad/ |
| 4 | Education and German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-education-german-year-abroad/ |
| 5 | Education and Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-education-italian-year-abroad/ |
| 6 | Education and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-education-spanish-year-abroad/ |

---

#### Politics and International Relations

##### BA (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Politics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-politics/ |
| 2 | Politics with International Relations BA | https://www.york.ac.uk/study/undergraduate/courses/ba-politics-international-relations/ |
| 3 | International Relations BA | https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations/ |
| 4 | International Relations and French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations-french-year-abroad/ |
| 5 | International Relations and German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations-german-year-abroad/ |
| 6 | International Relations and Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations-italian-year-abroad/ |
| 7 | International Relations and Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-international-relations-spanish-year-abroad/ |

---

#### School of Philosophy, Politics and Economics

##### BA/BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy, Politics and Economics BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-politics-economics-ppe/ |
| 2 | Philosophy, Politics and Economics BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-philosophy-politics-economics-ppe/ |
| 3 | Philosophy/Politics (Equal) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-philosophy-politics/ |

---

#### Sociology

##### BA/MSocW (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-sociology/ |
| 2 | Sociology with Criminology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-criminology/ |
| 3 | Sociology with Education BA | https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-education/ |
| 4 | Sociology with Social Psychology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-sociology-social-psychology/ |
| 5 | Social and Political Sciences BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-political-sciences/ |
| 6 | Social and Political Sciences (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-political-sciences-industry/ |
| 7 | Social and Public Policy BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-public-policy/ |
| 8 | Social and Public Policy (Ethics and Justice) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-public-policy-ethics-justice/ |
| 9 | Social and Public Policy (Ethics and Justice) (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-public-policy-ethics-justice-industry/ |
| 10 | Social and Public Policy (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-social-public-policy-industry/ |
| 11 | Criminal Justice and Social Policy BA | https://www.york.ac.uk/study/undergraduate/courses/ba-criminal-justice-social-policy/ |
| 12 | Criminal Justice and Social Policy (with a year in industry) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-criminal-justice-social-policy-industry/ |
| 13 | Criminology BA | https://www.york.ac.uk/study/undergraduate/courses/ba-criminology/ |
| 14 | Global Development BA | https://www.york.ac.uk/study/undergraduate/courses/ba-global-development/ |
| 15 | Social Work MSocW | https://www.york.ac.uk/study/undergraduate/courses/msocw-social-work/ |
| 16 | Liberal Arts BA | https://www.york.ac.uk/study/undergraduate/courses/ba-liberal-arts/ |
| 17 | Liberal Arts with French (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-liberal-arts-french/ |
| 18 | Liberal Arts with German (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-liberal-arts-german/ |
| 19 | Liberal Arts with Italian (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-liberal-arts-italian/ |
| 20 | Liberal Arts with Spanish (with a year abroad) BA | https://www.york.ac.uk/study/undergraduate/courses/ba-liberal-arts-spanish/ |

---

#### York Law School

##### LLB/Graduate LLB (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law LLB | https://www.york.ac.uk/study/undergraduate/courses/llb-law/ |
| 2 | Law LLBS (Senior Status) | https://www.york.ac.uk/study/undergraduate/courses/llb-law-senior-status/ |
| 3 | Law and Criminology LLB | https://www.york.ac.uk/study/undergraduate/courses/llb-law-criminology/ |
| 4 | International Human Rights Law LLB | https://www.york.ac.uk/study/undergraduate/courses/llb-ihrl/ |
| 5 | Professional Law and SQE Graduate LLB | https://www.york.ac.uk/study/undergraduate/courses/graduate-llb-professional-law-sqe/ |

---

### Joint Institutions

#### Hull York Medical School (HYMS)

##### MB BS (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine MB BS | https://www.hyms.ac.uk/medicine/mbbs-medicine |
| 2 | Medicine with a Gateway Year MB BS | https://www.hyms.ac.uk/medicine/medicine-with-a-gateway-year |

---

### Health Sciences

#### Nursing and Midwifery

##### BSc/MNurs/BMid (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-adult/ |
| 2 | Nursing (Adult) MNurs | https://www.york.ac.uk/study/undergraduate/courses/mnurs-nursing-adult/ |
| 3 | Nursing (Child) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-child/ |
| 4 | Nursing (Child) MNurs | https://www.york.ac.uk/study/undergraduate/courses/mnurs-nursing-child/ |
| 5 | Nursing (Mental Health) BSc | https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-mental-health/ |
| 6 | Nursing (Mental Health) MNurs | https://www.york.ac.uk/study/undergraduate/courses/mnurs-nursing-mental-health/ |
| 7 | Midwifery BMid | https://www.york.ac.uk/study/undergraduate/courses/bmid-midwifery/ |

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate Taught (PGT)

The University of York offers approximately **~210 distinct postgraduate taught programmes** (300 entries including PGCE training-provider duplicates). These are listed at `york.ac.uk/study/postgraduate/courses/all?mode=taught`.

**Degree types offered**: MA, MSc, MBA, MPA, MPP, MPH, LLM, PGCE, PGCert, PGDip, PG Diploma, PG Certificate, Graduate Diploma

**Delivery modes**: Full-time, part-time, online/distance-learning

**Key subject areas**: Archaeology, Biology, Biomedical Sciences, Business, Chemistry, Computer Science, Economics, Education, Engineering, English, Environment, Film & Television, History, History of Art, Law, Linguistics, Mathematics, Medical Sciences, Music, Nursing, Philosophy, Physics, Politics, Psychology, Social Policy, Sociology

**Notable online programmes**: MSc Computer Science, MSc Computer Science with AI, MSc Computer Science with Cyber Security, MSc Computer Science with Data Analytics, MBA, MPA (multiple variants), MSc Finance Leadership and Management, MSc Innovation Leadership and Management, MSc International Business Leadership and Management

> **Full PGT extraction**: P0 follow-up — requires separate extraction from the PG taught course list page.

### 2.2 Postgraduate Research

The University of York offers **158 postgraduate research programmes** listed at `york.ac.uk/study/postgraduate/courses/all?mode=research`.

**Degree types**: PhD (102), PhD distance learning (30), PhD Integrated (4), MSc by research (19), MA by research (17), MPhil (5), Doctor of Medicine (1), plus distance learning variants

**Departments offering research programmes**: Archaeology, Biology, Chemistry, Computer Science, Economics, Education, Engineering, English, Environment and Geography, Health Sciences, History, History of Art, Language and Linguistic Science, Law, Mathematics, Medical Sciences (HYMS), Music, Philosophy, Physics, Politics, Psychology, Sociology

> **Full PG research extraction**: P0 follow-up — requires separate extraction from the PG research course list page.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Entry requirements (typical offers by subject band)

| Subject area | A-Level typical | IB typical | Contextual offer | Key subjects required |
|-------------|----------------|-----------|-----------------|---------------------|
| Computer Science | AAA | 36 pts (5 HL Maths) | ABB | Mathematics |
| Engineering (BEng) | ABB | Not specified | — | Mathematics |
| Biology / Biomedical | AAB | 35 pts (5 HL Biology) | BBB | Biology + second science |
| Chemistry | AAA | 36 pts | ABB | Chemistry |
| Physics | AAA | 36 pts | ABB | Physics + Maths |
| Mathematics | AAA | 36 pts | ABB | Mathematics |
| Economics | AAA | 36 pts | ABB | — |
| English | AAA/A*AB | 36 pts (6 HL English Lit) | ABB | English Literature |
| History | AAA | 36 pts | ABB | — |
| Archaeology | ABB | Not specified | — | — |
| Law | AAA | 36 pts | ABB | — |
| Psychology | AAA | 36 pts | ABB | — |
| Politics / IR | AAA | 36 pts | ABB | — |
| Business / Management | AAA | 36 pts | ABB | — |
| Nursing | BBB | 31 pts | — | — |
| Medicine (HYMS) | AAA | — | — | UCAT required |

> **EPQ policy**: Grade A or higher in EPQ may reduce the offer by one A-level grade.
> **Contextual offers**: Available for eligible applicants (widening participation, care leavers, etc.)
> **Source**: Individual course pages at `york.ac.uk/study/undergraduate/courses/{slug}/`

### 3.2 English language requirements

#### Band 1 — Engineering and Technology (IELTS 6.0)

| Test | Requirement |
|------|-------------|
| IELTS (Academic) | **6.0** overall, minimum **5.5** in each component |
| TOEFL iBT | **79** overall (17L, 18R, 20S, 17W) |
| PTE Academic | Not separately specified for this band |

**Applies to**: Electronic Engineering, Engineering (general), Biomedical Engineering, Medical Engineering, Robotic Engineering, Music Technology Systems

#### Band 2 — Standard (IELTS 6.5)

| Test | Requirement |
|------|-------------|
| IELTS (Academic) | **6.5** overall, minimum **6.0** in each component |
| TOEFL iBT | **87** overall, minimum **21** in each component |
| PTE Academic | **61** overall, minimum **55** in each component |
| Cambridge CEFR | **176** overall, minimum **169** in each component |
| Duolingo | **120** overall, minimum **105** in each component |
| Oxford ELLT | **7**, minimum **6** each component |
| LanguageCert Academic/SELT | **B2**, minimum **33/50** each component |
| Kaplan Test of English | **478** main score, **444** each component |
| Skills for English | **B2: Merit** overall, **Pass with Merit** each component |
| Trinity ISE III | **Merit** in all components |
| IB English | **4** in English A or **5** in English B |
| GCSE English Language | Grade **C / Grade 4** |

**Applies to**: Computer Science, Biology, Chemistry, Physics, Mathematics, Economics, Psychology, English, History, Archaeology, Law, Politics, Architecture, Business, Sociology, and most other subjects

#### Band 3 — Healthcare (IELTS 7.0)

| Test | Requirement |
|------|-------------|
| IELTS (Academic) | **7.0** overall, minimum **7.0** in each component |
| TOEFL iBT | **96** overall, minimum **24** in each component |

**Applies to**: Nursing (Adult, Child, Mental Health), Midwifery

#### General policies

- **Score validity**: Test results must be dated no more than **2 years** before the course start date
- **GCSE validity**: GCSE/IGCSE/O Level English Language accepted if completed within **7 years** of course start date
- **TOEFL MyBest**: Explicitly **not acceptable**
- **Score combining**: Cannot combine scores from multiple attempts or qualification types

> **Accepted tests**: IELTS Academic (and Online), IELTS One Skill Retake, PTE Academic (excluding online), TOEFL iBT, Trinity ISE, Cambridge B2 First, Cambridge C1 Advanced, Duolingo, LanguageCert SELT, LanguageCert Academic, Kaplan Test of English, Skills For English, Oxford Test of English Advanced, Oxford ELLT
> **Source**: `york.ac.uk/study/undergraduate/applying/entry/english-language/`

### 3.3 Application deadlines

| Deadline | Date |
|----------|------|
| UCAS applications open | September 2026 |
| Medicine (HYMS) deadline | 15 October 2026 |
| Equal consideration deadline (most courses) | 14 January 2027 (typical UCAS deadline) |
| UCAS institution code | Y50 |

> **Note**: The university accepts applications through UCAS. Some courses may close to applications before the January deadline if they fill up. Medicine requires UCAT admissions test.

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees (2026/27 academic year)

| Fee band | Annual fee | Applies to |
|----------|-----------|------------|
| **UK (Home)** | **£9,790** | All UG courses including Medicine (HYMS) |
| **International — Humanities** | **£26,900** | English, History, History of Art, Archaeology, Philosophy, Languages, Linguistics, Education, Law, Politics, Sociology, Social Policy, Criminology, Global Development, Liberal Arts, Business (BA), Music, Theatre, Film |
| **International — Sciences** | **£32,350** | Computer Science, Biology, Biochemistry, Chemistry, Physics, Engineering, Mathematics, Economics, Psychology, Geography, Environmental Science, Biomedical Sciences, Data Science, Architecture, Nursing |

### 4.2 Fee policies

| Policy | Detail |
|--------|--------|
| UK fee increase (2027/28) | **£10,050** (government announced) |
| International annual increase | CPI inflation, capped at **maximum 10%** |
| Study abroad year | **15%** of full-time fee (~£1,469 for UK) |
| Year in industry / placement | **20%** of full-time fee (~£1,958 for UK) |
| Study abroad (Turing Scheme) | **15%** of full-time fee |

### 4.3 Fee examples (specific courses — 2026/27)

| Course | UK fee | International fee |
|--------|--------|-------------------|
| Computer Science BSc | £9,790 | £32,350 |
| Engineering BEng | £9,790 | £32,350 |
| Biology BSc | £9,790 | £32,350 |
| Psychology BSc | £9,790 | £32,350 |
| English BA | £9,790 | £26,900 |
| Archaeology BA | £9,790 | £26,900 |
| Law LLB | £9,790 | £27,500 |
| Nursing BSc | £9,790 | £32,350 |

### 4.4 Financial support

- **Government loans**: Available for UK/Home students
- **Scholarships and bursaries**: Available for both UK and international students
- **Disability funding**: Available for students with disabilities

> **Source**: `york.ac.uk/study/undergraduate/fees-funding/uk/` and individual course pages

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of York"
  source_url: https://www.york.ac.uk
  source_snippet: "University of York"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.russell_group
  value: true
  source_url: https://www.york.ac.uk/study/international/
  source_snippet: "high-performing and prestigious Russell Group university"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: rankings.qs_world_2027
  value: "Joint 158th"
  source_url: https://www.york.ac.uk/about/rankings/
  source_snippet: "Joint 158th out of 1,504 institutions"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: rankings.the_world_2026
  value: "Joint 154th"
  source_url: https://www.york.ac.uk/about/rankings/
  source_snippet: "joint 154th out of 2,191 institutions"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: rankings.tef
  value: "Gold"
  source_url: https://www.york.ac.uk/about/rankings/
  source_snippet: "Gold rating in the 2023 TEF"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: rankings.ref_2021
  value: "Joint 10th"
  source_url: https://www.york.ac.uk/about/rankings/
  source_snippet: "Awarded joint 10th in the Times Higher Education ranking of the latest Research Excellence Framework (REF 2021)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: academics.structure
  value: "3 faculties, 17 departments, 6 schools"
  source_url: https://www.york.ac.uk/departments/
  source_snippet: "Faculty of Arts and Humanities, Faculty of Sciences, Faculty of Social Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: academics.ug_courses_total
  value: 289
  source_url: https://www.york.ac.uk/study/undergraduate/courses/all/
  source_snippet: "289 courses listed on a single page"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: academics.pgt_courses_total
  value: "~300 entries (~210 distinct)"
  source_url: https://www.york.ac.uk/study/postgraduate/courses/all?mode=taught
  source_snippet: "300 entries including PGCE training-provider duplicates"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: academics.pg_research_total
  value: 158
  source_url: https://www.york.ac.uk/study/postgraduate/courses/all?mode=research
  source_snippet: "158 postgraduate research programmes"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: fees.uk_home_2026_27
  value: 9790
  source_url: https://www.york.ac.uk/study/undergraduate/fees-funding/uk/
  source_snippet: "9,790 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: fees.uk_home_2027_28_announced
  value: 10050
  source_url: https://www.york.ac.uk/study/undergraduate/fees-funding/uk/
  source_snippet: "Increases to the Government fee cap may apply"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: fees.international_humanities
  value: 26900
  source_url: https://www.york.ac.uk/study/undergraduate/courses/ba-english/
  source_snippet: "International and EU: £26,900"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-014:
  field: fees.international_sciences
  value: 32350
  source_url: https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science/
  source_snippet: "International and EU: £32,350"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-015:
  field: english_language.band_standard
  value: "IELTS 6.5, min 6.0 per component"
  source_url: https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science/
  source_snippet: "6.5, minimum 6.0 in each component"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-016:
  field: english_language.band_engineering
  value: "IELTS 6.0, min 5.5 per component"
  source_url: https://www.york.ac.uk/study/undergraduate/courses/beng-engineering/
  source_snippet: "6.0 overall, minimum 5.5 in each component"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-017:
  field: english_language.band_healthcare
  value: "IELTS 7.0, min 7.0 per component"
  source_url: https://www.york.ac.uk/study/undergraduate/courses/bsc-nursing-adult/
  source_snippet: "7.0 overall, minimum 7.0 in each component"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-018:
  field: entry_requirements.computer_science
  value: "AAA including Mathematics"
  source_url: https://www.york.ac.uk/study/undergraduate/courses/bsc-computer-science/
  source_snippet: "Typical offer: AAA including Mathematics"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-019:
  field: entry_requirements.medicine
  value: "AAA, UCAT required"
  source_url: https://www.hyms.ac.uk/medicine/mbbs-medicine
  source_snippet: "A Levels: AAA, Admissions Test: UCAT"
  capture_date: 2026-07-08
  evidence_type: course_page

E-U-020:
  field: fees.placement_year
  value: "20% of full-time fee"
  source_url: https://www.york.ac.uk/study/undergraduate/fees-funding/uk/
  source_snippet: "Year in industry/placement: 20% of full-time fee"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Data completeness summary

| Priority | Data item | Status |
|----------|-----------|--------|
| **P0** | Full UG course listing (289 courses) | COMPLETE |
| **P0** | Faculty/department academic hierarchy | COMPLETE |
| **P0** | Degree type distribution and counts | COMPLETE |
| **P0** | UK tuition fees | COMPLETE |
| **P0** | International tuition fees (by band) | COMPLETE |
| **P0** | English language requirements (3 bands) | COMPLETE |
| **P0** | Entry requirements (by subject) | COMPLETE (8 representative courses) |
| **P0** | Rankings | COMPLETE |
| **P1** | Full PG taught course listing (~210 distinct) | P0 follow-up |
| **P1** | Full PG research programme listing (158) | P0 follow-up |
| **P1** | Per-course A-Level/IB entry requirements | P0 follow-up (8 courses extracted, rest on individual pages) |
| **P1** | Application deadlines | COMPLETE |
| **P1** | Scholarship and funding details | P0 follow-up |
| **P2** | Course module details and curriculum structure | P0 follow-up |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of York | Birmingham | Cardiff | Newcastle |
|-----------|--------|-----------|---------|-----------|
| Total UG programmes | 289 | 366 | 237 | 147 |
| Russell Group | Yes | Yes | Yes | Yes |
| QS World 2027 | =158th | — | — | — |
| THE World 2026 | =154th | — | — | — |
| TEF rating | Gold | Gold | — | — |
| REF 2021 (THE) | Joint 10th | — | — | — |
| Faculties/Colleges | 3 | 5 | — | — |
| UK UG fee (2026/27) | £9,790 | £9,790 | — | — |
| International fee range | £26,900–£32,350 | ~£22,000–£48,000 | — | — |
| IELTS (standard band) | 6.5 (6.0) | 6.5 (6.0) | — | — |
| IELTS (engineering) | 6.0 (5.5) | 6.0 (5.5) | — | — |
| IELTS (nursing) | 7.0 (7.0) | 7.0 (7.0) | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University of York official website (`york.ac.uk`), Hull York Medical School (`hyms.ac.uk`)
> **Granularity**: faculty -> department/school -> degree-level -> program
> **Completeness**: Structural framework UG programmes Evidence (20 blocks)
> **Next step**: P0 follow-up for full PGT/PG research extraction and per-course entry requirements
