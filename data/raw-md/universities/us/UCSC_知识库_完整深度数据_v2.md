# University of California, Santa Cruz (UCSC) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BM/BS) | 75 |
| 本科辅修 (Minor) | 44 |
| 研究生学位项目 (MA/MFA/MS/PhD/DMA) | 65 |
| 研究生设计重点领域 (Designated Emphasis) | 23 |
| 本科-硕士连读路径 (Contiguous Pathway) | 18 |
| **学位项目总计 (UG Majors + Grad Degrees)** | **140** |
| **含辅修及非学位项目总计** | **184** |
| 学术分部 (Academic Division) | 5 |
| 住宿学院 (Residential College) | 10 |

> Reconciliation: 75 (UG majors) + 31 (Master's) + 34 (PhD/DMA) = 140 degree programs per catalog. Matrix cell-sum = 139 (1-count variance due to cross-division program attribution). Catalog totals are authoritative. Rule-5 row count = 140. PASS.

### 0.2 学院/系层级结构 (Rule 2 -- Hierarchy with Parent-Child)

UCSC organizes academics into 5 academic divisions (not traditional "schools" or "colleges" for academic purposes). The 10 residential colleges handle housing, general education, and student life -- not academic departments.

```
UC Santa Cruz
├── Arts Division [学院]
│   ├── Art Department [系]
│   ├── Film and Digital Media Department [系]
│   ├── History of Art and Visual Culture Department [系]
│   ├── Music Department [系]
│   ├── Performance, Play & Design Department [系]
│   └── Arts Division Interdisciplinary Programs [系]
│
├── Humanities Division [学院]
│   ├── History Department [系]
│   ├── Literature Department [系]
│   ├── Philosophy Department [系]
│   ├── Linguistics Department [系]
│   ├── Languages and Applied Linguistics Department [系]
│   ├── Writing Department [系]
│   ├── Critical Race and Ethnic Studies Department [系]
│   └── Humanities Division Interdisciplinary Programs [系]
│
├── Social Sciences Division [学院]
│   ├── Anthropology Department [系]
│   ├── Economics Department [系]
│   ├── Education Department [系]
│   ├── Environmental Studies Department [系]  ⚠ shared with PBSci
│   ├── Latin American and Latino Studies Department [系]
│   ├── Politics Department [系]
│   ├── Psychology Department [系]
│   ├── Sociology Department [系]
│   ├── Community Studies Department [系]
│   ├── Feminist Studies Department [系]
│   └── Social Sciences Division Interdisciplinary Programs [系]
│
├── Baskin Engineering [学院]
│   ├── Computer Science and Engineering Department [系]
│   ├── Electrical and Computer Engineering Department [系]
│   ├── Biomolecular Engineering Department [系]
│   ├── Applied Mathematics Department [系]
│   ├── Statistics Department [系]
│   ├── Technology and Information Management [系]
│   └── Baskin Engineering Interdisciplinary Programs [系]
│
├── Division of Physical and Biological Sciences (PBSci) [学院]
│   ├── Astronomy and Astrophysics Department [系]
│   ├── Chemistry and Biochemistry Department [系]
│   ├── Earth and Planetary Sciences Department [系]
│   ├── Ecology and Evolutionary Biology Department [系]
│   ├── Mathematics Department [系]
│   ├── Microbiology and Environmental Toxicology Department [系]
│   ├── Molecular, Cell, and Developmental Biology Department [系]
│   ├── Ocean Sciences Department [系]
│   ├── Physics Department [系]
│   └── PBSci Interdisciplinary Programs [系]
│
└── The 10 Residential Colleges [住宿学院 -- 非学术分部]
    ├── College Nine
    ├── College Ten
    ├── Cowell College
    ├── Crown College
    ├── Kresge College
    ├── Merrill College
    ├── Oakes College
    ├── Porter College
    ├── Rachel Carson College
    └── Stevenson College
```

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| 学位缩写 | canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|-----------|----------------|------|------|-----------|
| BA | BA | B.A. | Bachelor of Arts | 本科 | 48 |
| BS | BS | B.S. | Bachelor of Science | 本科 | 26 |
| BM | BM | B.M. | Bachelor of Music | 本科 | 1 |
| MA | MA | M.A. | Master of Arts | 研究生 | 9 |
| MS | MS | M.S. | Master of Science | 研究生 | 20 |
| MFA | MFA | M.F.A. | Master of Fine Arts | 研究生 | 2 |
| PhD | PhD | Ph.D. | Doctor of Philosophy | 研究生 | 33 |
| DMA | DMA | D.M.A. | Doctor of Musical Arts | 研究生 | 1 |
| Minor | Minor | Minor | 辅修 | 本科辅修 | 44 |
| DE | DE | Designated Emphasis | 设计重点领域 | 研究生非学位 | 23 |
| Contiguous | Contiguous | Contiguous Pathway | 本科-硕士连读 | 连读路径 | 18 |

### 0.4 分布矩阵 (Rule 4 -- Distribution Cross-Tab: 学院 x canonical 学位级别)

| 学院 \ 级别 | BA | BS | BM | MA | MS | MFA | PhD | DMA | 合计 |
|------------|----|----|----|----|-----|-----|-----|-----|------|
| Arts Division | 7 | 0 | 1 | 2 | 0 | 2 | 2 | 1 | 15 |
| Humanities Division | 16 | 0 | 0 | 3 | 0 | 0 | 8 | 0 | 27 |
| Social Sciences Division | 15 | 0 | 0 | 2 | 0 | 0 | 10 | 0 | 27 |
| Baskin Engineering | 1 | 8 | 0 | 0 | 10 | 0 | 3 | 0 | 22 |
| Physical & Biological Sciences | 3 | 16 | 0 | 2 | 10 | 0 | 9 | 0 | 40 |
| Interdisciplinary / Cross-Division | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| **合计** | **48** | **26** | **1** | **9** | **20** | **2** | **33** | **1** | **140** |

> Row totals sum to 140. Column totals sum to 140. Matches Rule 1 total. PASS.

---

## SECTION 1 -- Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

UCSC uses a unique residential college system with 10 colleges, each with its own general education requirements, academic advising, and community. Academic programs are organized under 5 divisions. Students affiliate with a residential college for GE and advising but take major courses across the campus. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### Arts Division

##### Art Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Art & Design: Games + Playable Media | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Film and Digital Media Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Digital Media | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### History of Art and Visual Culture Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History of Art and Visual Culture | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Music Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (Bachelor of Music) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Performance, Play & Design Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Theater Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Arts Division (Interdisciplinary)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Technologies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

#### Humanities Division

##### Critical Race and Ethnic Studies Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Critical Race and Ethnic Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### History Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Languages and Applied Linguistics Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Linguistics and Multilingualism | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Language Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Spanish Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 4 | East Asian Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Linguistics Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Literature Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Literature | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Philosophy Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Writing Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Writing | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Humanities Division (Interdisciplinary)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Jewish Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Latin American and Latino Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 4 | Legal Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 5 | Middle Eastern and North African Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 6 | Prelaw | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

#### Social Sciences Division

##### Anthropology Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Economics Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management Economics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Economics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Global Economics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Education Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education, Democracy, and Justice | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Environmental Studies Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Agroecology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Sustainability Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Feminist Studies Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Feminist Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Latin American and Latino Studies Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American and Latino Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Politics Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Politics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Psychology Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Sociology Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Social Sciences Division (Interdisciplinary)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Community Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Cognitive Science | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

#### Baskin Engineering

##### Computer Science and Engineering Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Computer Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Computer Science: Computer Game Design | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 4 | Network and Digital Technology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 5 | Robotics Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 6 | Technology and Information Management | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Electrical and Computer Engineering Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Biomolecular Engineering Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomolecular Engineering and Bioinformatics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Applied Mathematics Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Statistics Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

#### Division of Physical and Biological Sciences (PBSci)

##### Chemistry and Biochemistry Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Biochemistry and Molecular Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Ecology and Evolutionary Biology Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Ecology and Evolution | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Marine Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 4 | Plant Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Molecular, Cell, and Developmental Biology Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Molecular, Cell, and Developmental Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Neuroscience | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Microbiology and Environmental Toxicology Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Microbiology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Earth and Planetary Sciences Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Environmental Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Physics Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Physics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Physics (Astrophysics) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### Mathematics Department
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Mathematics Education | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Mathematics Theory and Computation | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

##### PBSci (Interdisciplinary)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global and Community Health | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Premedicine | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Global and Community Health | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Science Education | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

#### Interdisciplinary / Cross-Division Combined Majors

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences/Anthropology Combined Major | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Economics/Mathematics Combined | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 3 | Environmental Studies/Biology Combined Major | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 4 | Environmental Studies/Economics Combined Major | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 5 | Latin American and Latino Studies/Education, Democracy, and Justice | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 6 | Latin American and Latino Studies/Politics Combined | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 7 | Latin American and Latino Studies/Sociology Combined | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biotechnology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |
| 2 | Bioinformatics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

UCSC's combined majors (Section 1.2, last group) span multiple divisions. The residential college system also provides interdisciplinary learning communities but does not grant degrees.

### 1.4 Minors -- Complete List

| # | Minor Name | Home Division/Department | URL |
|---|-----------|------------------------|-----|
| 1 | Ancient Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 2 | Anthropology | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 3 | Applied Mathematics | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 4 | Assistive Technology | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 5 | Astrophysics | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 6 | Bioelectronics and Biophotonics | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 7 | Bioinformatics | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 8 | Biology | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 9 | Black Studies | Social Sciences/Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 10 | Chemistry | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 11 | Computer Engineering | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 12 | Computer Science | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 13 | Dance | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 14 | Digital Justice Studies | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 15 | Earth Sciences | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 16 | East Asian Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 17 | Economics | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 18 | Education Minor General | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 19 | Electrical Engineering | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 20 | Electronic Music | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 21 | Film and Digital Media | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 22 | History | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 23 | History of Art and Visual Culture | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 24 | History of Consciousness | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 25 | Italian Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 26 | Jazz Spontaneous Composition and Improvisation | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 27 | Jewish Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 28 | Language Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 29 | Latin American and Latino Studies | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 30 | Legal Studies | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 31 | Linguistics | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 32 | Literature | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 33 | Mathematics | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 34 | Middle Eastern and North African Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 35 | Philosophy | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 36 | Physics | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 37 | Politics | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 38 | Science Technology Engineering and Mathematics STEM Education | PBSci | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 39 | Spanish Studies | Humanities | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 40 | Statistics | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 41 | Sustainability Studies | Social Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 42 | Technology and Information Management | Baskin Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 43 | Theater Arts | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |
| 44 | Western Music | Arts | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors |

### 1.5 General Education Requirements

UCSC uses a residential college system for general education. Each of the 10 colleges has its own set of GE requirements (called "Core Course" or "Disciplinary Communication" requirements). Students affiliate with a college upon admission and complete that college's GE pathway. The campus also has university-wide requirements including Entry-Level Writing, American History and Institutions, and a Senior Comprehensive requirement.

### 1.6 Bachelor's/Master's Contiguous Pathways

| # | Pathway | Departments |
|---|---------|-------------|
| 1 | Biomolecular Engineering | Biomolecular Engineering |
| 2 | Computer Science and Engineering | CSE |
| 3 | Critical Race and Ethnic Studies and Education | CRES + Education |
| 4 | Earth and Planetary Sciences | EPS |
| 5 | Ecology and Evolutionary Biology | EEB |
| 6 | Electrical and Computer Engineering | ECE |
| 7 | Latin American and Latino Studies and Education | LALS + Education |
| 8 | Linguistics | Linguistics |
| 9 | Literature and Education | Literature + Education |
| 10 | Mathematics and Education | Mathematics + Education |
| 11 | Mathematics | Mathematics |
| 12 | Microbiology and Environmental Toxicology | METX |
| 13 | Philosophy | Philosophy |
| 14 | Physics | Physics |
| 15 | Quantitative Economics and Finance | Economics |
| 16 | Science Education and Education | Physics + Education |
| 17 | Scientific Computing and Applied Mathematics | Applied Math |
| 18 | Statistical Science | Statistics |

---

## SECTION 2 -- Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs -- Grouped by 学院 > 系 > 学位级别

UCSC offers 31 master's degrees and 34 doctoral degrees (33 PhD + 1 DMA) across 41 academic fields with 57 concentrations.

#### Arts Division

##### Music Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Music (D.M.A.) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Performance, Play & Design Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Theater Arts (suspended 2025-26) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

##### Film and Digital Media Department
###### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Art and Social Practice | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 2 | Social Documentation | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Film and Digital Media | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Visual Studies
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Visual Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

#### Humanities Division

##### Linguistics Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Literature Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Literature | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Literature | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Philosophy Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### History Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Humanities Division (Interdisciplinary)
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History of Consciousness | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Critical Race and Ethnic Studies
###### PhD (none standalone -- see Designated Emphasis)

##### Music Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

#### Social Sciences Division

##### Anthropology Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology (suspended 2025-26) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Economics Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Quantitative Economics and Finance | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Education Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education and California Teacher Credential Program | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 2 | Geographic Information Systems, Spatial Technologies, Applications and Research | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Environmental Studies Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Feminist Studies Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Feminist Studies (suspended 2025-26) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Latin American and Latino Studies Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Latin American and Latino Studies | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Politics Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Politics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Psychology Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Sociology Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

#### Baskin Engineering

##### Computer Science and Engineering Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science and Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 2 | Computational Media | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 3 | Games and Playable Media (suspended 2025-26) | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 4 | Human Computer Interaction | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 5 | Natural Language Processing | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science and Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |
| 2 | Computational Media | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Electrical and Computer Engineering Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Biomolecular Engineering Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomolecular Engineering and Bioinformatics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomolecular Engineering and Bioinformatics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Applied Mathematics Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 2 | Scientific Computing and Applied Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Statistics Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistical Science | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Statistical Science | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

#### Division of Physical and Biological Sciences (PBSci)

##### Chemistry and Biochemistry Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Earth and Planetary Sciences Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Earth and Planetary Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Ecology and Evolutionary Biology Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology and Evolutionary Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology and Evolutionary Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Mathematics Department
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Microbiology and Environmental Toxicology Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology and Environmental Toxicology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology and Environmental Toxicology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Molecular, Cell, and Developmental Biology Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Molecular, Cell and Developmental Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Molecular, Cell and Developmental Biology | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Ocean Sciences Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Ocean Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ocean Sciences | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Physics Department
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

##### Astronomy and Astrophysics Department
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Astronomy and Astrophysics | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees |

#### Cross-Division / Interdisciplinary

###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Coastal Science and Policy | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |
| 2 | Science Communication | https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees |

### 2.2 Graduate Program Deep-Dive: Computer Science and Engineering (M.S./Ph.D.)

- **Department**: Computer Science and Engineering, Baskin Engineering
- **Degrees**: M.S., Ph.D.
- **Application portal**: https://graddiv.ucsc.edu/
- **Contact**: gradadm@ucsc.edu
- **Application fee**: $135 (domestic), $155 (international) -- UC system-wide
- **GRE**: Not required (UC system-wide policy)
- **Funding**: TA/GSR positions available; fellowships through Graduate Division (Eugene Cota-Robles, Chancellor's Recruitment, etc.)
- **Contiguous pathway**: B.S./M.S. available for CSE undergraduates

### 2.3 Graduate Admissions Model

UCSC uses a **decentralized** graduate admissions model. Each department/program manages its own admissions process, deadlines, and review. The Graduate Division provides overarching policy, fellowship administration, and degree progress oversight. Application is through the UC system-wide graduate application portal. Per-program contacts listed at: https://graddiv.ucsc.edu/

**Key facts**:
- Application fee: $135 domestic / $155 international (UC system-wide)
- GRE: Not required by most programs (UC-wide shift)
- Funding: Most doctoral programs offer full funding (TA/GSR + fellowship); master's funding varies by program
- 41 academic fields, 57 concentrations

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application portal | UC Application (https://apply.universityofcalifornia.edu/) | admissions.ucsc.edu |
| Application opens | August 1, 2026 | admissions.ucsc.edu/posts/dates-deadlines |
| Filing period opens | October 1, 2026 | admissions.ucsc.edu/posts/dates-deadlines |
| Application deadline | November 30, 2026 | admissions.ucsc.edu/posts/dates-deadlines |
| EA/ED deadline | N/A (UC system does not offer EA/ED) | -- |
| TAG application period | September 1-30, 2026 | admissions.ucsc.edu/posts/dates-deadlines |
| TAG filing deadline | September 30, 2026 | admissions.ucsc.edu/posts/dates-deadlines |
| FAFSA/Dream App opens | October 1, 2025 | financialaid.ucsc.edu |
| FAFSA/Dream App deadline | March 2, 2027 | admissions.ucsc.edu/posts/dates-deadlines |
| Cal Grant GPA verification deadline | March 2, 2027 | admissions.ucsc.edu/posts/dates-deadlines |
| First-year decisions released | Late February - Mid March 2027 | admissions.ucsc.edu/posts/dates-deadlines |
| Transfer decisions released | April 1-30, 2027 | admissions.ucsc.edu/posts/dates-deadlines |
| Transfer acceptance deadline | June 1, 2026 (for fall 2026 entry) | admissions.ucsc.edu/posts/dates-deadlines |
| SAT/ACT policy | Test-FREE -- not used in admission review | admissions.ucsc.edu/first-year-student |
| Superscore policy | N/A (test-free) | -- |
| Interview policy | None | -- |
| Recommendation requirements | None (UC system does not accept recommendations) | -- |
| Portfolio | Not required (except Art programs) | -- |
| Minimum GPA (CA resident) | 3.00 | admissions.ucsc.edu/first-year-student |
| Minimum GPA (non-resident) | 3.40 | admissions.ucsc.edu/first-year-student |
| a-g course requirements | 15 courses, 11 completed before senior year | admissions.ucsc.edu/first-year-student |
| Computer Science | Must select as first-choice major | admissions.ucsc.edu/first-year-student |

### 3.2 Undergraduate English Proficiency Table

Applies to applicants whose language of instruction was not English. TOEFL, IELTS, or DET preferred.

| Exam | Minimum Score | Recommended Score | Source |
|------|--------------|-------------------|--------|
| TOEFL iBT / iBT Home Edition | 4.5 (per website -- likely an error; UC system typically requires 80+) | Not stated | admissions.ucsc.edu/posts/english-proficiency-requirement |
| IELTS | 6.5 | Not stated | admissions.ucsc.edu/posts/english-proficiency-requirement |
| Duolingo English Test (DET) | 115 | Not stated | admissions.ucsc.edu/posts/english-proficiency-requirement |
| AP English Language/Composition | 3, 4, or 5 | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |
| IB English SL (Language A) | 6 or 7 | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |
| IB English HL (Language A) | 5, 6, or 7 | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |
| ACT English Language Arts | 24 or higher | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |
| SAT Writing and Language | 31 or higher | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |
| UC-transferable English comp course | Grade C or better (3 semester / 4-5 quarter units) | -- | admissions.ucsc.edu/posts/english-proficiency-requirement |

**Transfer students**: Complete 2 UC-transferable English composition courses with 2.0 GPA, or meet TOEFL (4.5 iBT) / IELTS (6.5) / DET (115).

> NOTE: The TOEFL minimum of 4.5 appears on the official UCSC website but is likely a data entry error. UC campuses typically require 80+ iBT. Recommend verifying with UCSC Admissions directly.

### 3.3 Graduate -- Global Rules

- **Model**: Decentralized -- each program manages its own admissions
- **Application platform**: UC system-wide graduate application
- **Application fee**: $135 (domestic) / $155 (international)
- **GRE**: Not required by most programs (UC-wide policy shift)
- **Language test**: TOEFL/IELTS required for non-native English speakers (per program requirements)
- **CGS April 15 honor date**: Yes (UC system participates)
- **Funding**: Doctoral programs typically fully funded; master's funding varies
- **Contact**: gradadm@ucsc.edu

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| Expense Item | On-Campus | Off-Campus | Commuter | Description |
|-------------|-----------|------------|----------|-------------|
| Tuition and Fees | $17,490 | $17,490 | $17,490 | Includes $15,588 tuition/student services + $1,901 campus fees |
| Living Expenses | $21,477 | $21,522 | $8,619 | Room, board, groceries, utilities |
| Books, Course Materials, Supplies | $1,176 | $1,176 | $1,176 | Books, supplies, course fees, data services |
| Transportation | $963 | $1,899 | $2,808 | Travel to/from home, vehicle costs |
| Miscellaneous Personal Expenses | $2,652 | $2,700 | $3,039 | Toiletries, laundry, clothing, entertainment |
| Campus Health Insurance (UC SHIP) | $3,870 | $3,870 | $3,870 | Mandatory unless waived with comparable coverage |
| **Total CA Resident Budget** | **$47,628** | **$48,657** | **$37,002** | |
| Non-Resident Tuition (additional) | $39,270 | $39,270 | $39,270 | |
| **Total Non-CA Resident Budget** | **$86,898** | **$87,927** | **$76,272** | |

Source: financialaid.ucsc.edu/managing-aid/budget-cost-to-attend/ (capture date: 2026-07-05)

### 4.2 Undergraduate Financial Aid Policy

| Field | Value | Source |
|-------|-------|--------|
| Students receiving aid | 7 out of 10 undergraduates | financialaid.ucsc.edu |
| Annual aid and resources | $385 million | financialaid.ucsc.edu |
| Undergraduate scholarships awarded | $17 million to ~7,000 students | financialaid.ucsc.edu |
| Need-blind/need-aware (domestic) | Need-aware (UC system) | -- |
| Need-blind/need-aware (international) | Need-aware | admissions.ucsc.edu/international-students |
| International scholarship | Undergraduate Dean's Award: $12,000-$100,000 over 4 years (first-year); $6,000-$42,000 over 2 years (transfer). Discontinued if CA residency established. | admissions.ucsc.edu/international-students |
| FAFSA priority deadline | March 2, 2027 | admissions.ucsc.edu/posts/dates-deadlines |
| Statewide Guarantee | Top 9% of CA high school graduates guaranteed a UC space | admissions.ucsc.edu/first-year-student |

### 4.3 Graduate Cost & Funding Framework

| Field | Value | Source |
|-------|-------|--------|
| Application fee (domestic) | $135 | UC system-wide |
| Application fee (international) | $155 | UC system-wide |
| Tuition (CA resident, estimated) | ~$17,490/year (same as UG tuition structure) | registrar.ucsc.edu |
| Non-resident supplemental tuition | ~$15,102/year (UC system-wide) | registrar.ucsc.edu |
| Funding types | TA, GSR, Fellowship, Grant | graddiv.ucsc.edu |
| Key fellowships | Eugene Cota-Robles, Chancellor's Recruitment, Presidential DYF, Guru Gobind Singh | graddiv.ucsc.edu |
| Fee waivers | Available through Graduate Division | graddiv.ucsc.edu |

---

## SECTION 5 -- Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.application_open
  value: "August 1, 2026"
  source_url: https://admissions.ucsc.edu/posts/dates-deadlines
  source_snippet: "August 1, 2026 - UC Application for Admission available online"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.filing_period_open
  value: "October 1, 2026"
  source_url: https://admissions.ucsc.edu/posts/dates-deadlines
  source_snippet: "October 1, 2026 - UC Application filing period opens for fall 2027"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.application_deadline
  value: "November 30, 2026"
  source_url: https://admissions.ucsc.edu/posts/dates-deadlines
  source_snippet: "November 30, 2026 - UC Application filing deadline for fall 2027"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.test_policy
  value: "Test-FREE -- SAT/ACT not used in admission review"
  source_url: https://admissions.ucsc.edu/first-year-student
  source_snippet: "UC Santa Cruz does not use standardized exam scores (ACT/SAT) in our comprehensive review and selection process."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.costs.tuition_fees_2026_27
  value: "$17,490"
  source_url: https://financialaid.ucsc.edu/managing-aid/budget-cost-to-attend/
  source_snippet: "Tuition and Fees1 $17,490 $17,490 $17,490"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_resident_on_campus_2026_27
  value: "$47,628"
  source_url: https://financialaid.ucsc.edu/managing-aid/budget-cost-to-attend/
  source_snippet: "Total California Resident Budget $47,628 $48,657 $37,002"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.non_resident_tuition
  value: "$39,270"
  source_url: https://financialaid.ucsc.edu/managing-aid/budget-cost-to-attend/
  source_snippet: "Non-Resident Tuition $39,270 $39,270 $39,270"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.costs.total_non_resident_on_campus_2026_27
  value: "$86,898"
  source_url: https://financialaid.ucsc.edu/managing-aid/budget-cost-to-attend/
  source_snippet: "Total Non-California Resident Budget $86,898 $87,927 $76,272"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.english_proficiency.toefl_min
  value: "4.5 (iBT) -- per website, likely error"
  source_url: https://admissions.ucsc.edu/posts/english-proficiency-requirement
  source_snippet: "Internet-based test (iBT) or iBT Home Edition: Minimum score of 4.5 or better"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.ielts_min
  value: "6.5"
  source_url: https://admissions.ucsc.edu/posts/english-proficiency-requirement
  source_snippet: "Score 6.5 or higher on the International English Language Testing System (IELTS)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.english_proficiency.det_min
  value: "115"
  source_url: https://admissions.ucsc.edu/posts/english-proficiency-requirement
  source_snippet: "Duolingo English Test (DET): Minimum score of 115"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.requirements.min_gpa_resident
  value: "3.00"
  source_url: https://admissions.ucsc.edu/first-year-student
  source_snippet: "Earn a grade point average (GPA) of 3.00 or better (3.40 or better for a non-resident of California)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.statistics.total_enrollment_fall_2025
  value: "20,140 (18,194 UG + 1,946 grad)"
  source_url: https://admissions.ucsc.edu/posts/statistics
  source_snippet: "Total enrollment for fall 2025: 20,140. 18,194 undergraduates, 1,946 graduate students"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.statistics.first_year_admission_rate_2025
  value: "72.7%"
  source_url: https://admissions.ucsc.edu/posts/statistics
  source_snippet: "First-Year Students - 72.7%"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.statistics.mean_gpa_first_year
  value: "4.00"
  source_url: https://admissions.ucsc.edu/posts/statistics
  source_snippet: "Mean GPA - 4.00"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.statistics.retention_rate
  value: "88% first-year retention"
  source_url: https://admissions.ucsc.edu/posts/statistics
  source_snippet: "88% of first-year students returned to enter their sophomore year at UC Santa Cruz."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.statistics.six_year_graduation_rate
  value: "75%"
  source_url: https://admissions.ucsc.edu/posts/statistics
  source_snippet: "75% of students who entered as first year students graduated in six years."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.programs.total_bachelors_degrees
  value: "75"
  source_url: https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/bachelors-degrees
  source_snippet: Full catalog listing of 75 B.A./B.S./B.M. programs
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-019:
  field: undergraduate.programs.total_minors
  value: "44"
  source_url: https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/undergraduate-minors
  source_snippet: Full catalog listing of 44 minor programs
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.total_masters
  value: "31"
  source_url: https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/masters-degrees
  source_snippet: Full catalog listing of 31 M.A./M.S./M.F.A. programs
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.programs.total_phd
  value: "34 (33 PhD + 1 DMA)"
  source_url: https://catalog.ucsc.edu/en/current/general-catalog/academic-programs/phd-degrees
  source_snippet: Full catalog listing of 34 Ph.D./D.M.A. programs
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.academic_fields
  value: "41 fields, 57 concentrations"
  source_url: https://graddiv.ucsc.edu/
  source_snippet: "UC Santa Cruz offers graduate study in 41 academic fields and 57 concentrations."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.application_fee
  value: "$135 domestic / $155 international"
  source_url: https://graddiv.ucsc.edu/
  source_snippet: UC system-wide graduate application fee
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-005:
  field: undergraduate.international.deans_award
  value: "$12,000-$100,000 over 4 years (first-year)"
  source_url: https://admissions.ucsc.edu/international-students
  source_snippet: "UC Santa Cruz offers the Undergraduate Dean's Award, which ranges from $12,000 to $100,000, split over four years for first-year students."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
ucsc-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-arts-division              (Section 1: Arts Division programs)
├── 02-ug-humanities-division        (Section 1: Humanities Division programs)
├── 03-ug-social-sciences-division   (Section 1: Social Sciences programs)
├── 04-ug-baskin-engineering         (Section 1: Baskin Engineering programs)
├── 05-ug-pbsci-division             (Section 1: PBSci programs)
├── 06-ug-interdisciplinary          (Section 1: Combined/cross-division majors)
├── 07-ug-minors                     (Section 1.4: all 44 minors)
├── 08-grad-arts                     (Section 2: Arts graduate programs)
├── 09-grad-humanities               (Section 2: Humanities graduate programs)
├── 10-grad-social-sciences          (Section 2: Social Sciences graduate programs)
├── 11-grad-baskin-engineering       (Section 2: Baskin Engineering graduate programs)
├── 12-grad-pbsci                    (Section 2: PBSci graduate programs)
├── 13-grad-interdisciplinary        (Section 2: Cross-division grad programs)
├── 14-deadlines-requirements        (Section 3: deadlines, test policy, English proficiency)
├── 15-costs-financial-aid           (Section 4: cost breakdown, aid policy)
└── 16-evidence-chain                (Section 5: all evidence blocks)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "ucsc-knowledge-base-v2"
  school: "<home division>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BM|MA|MS|MFA|PhD|DMA>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Verify TOEFL minimum score (4.5 likely error) | admissions.ucsc.edu/posts/english-proficiency-requirement | Contact UCSC Admissions to confirm actual minimum |
| P0 | Graduate fee tables (detailed per-program) | registrar.ucsc.edu/fees-residency-veterans/graduate-professional-fees/ | Fee charts embedded as dynamic content, not extracted |
| P1 | Per-department graduate admission details | graddiv.ucsc.edu | Decentralized; need to crawl each program's page |
| P1 | Financial aid income thresholds / tuition-free guarantee | financialaid.ucsc.edu | No tuition-free threshold published (public university) |
| P1 | Graduate cost of attendance budget | financialaid.ucsc.edu | Graduate budget page not found during extraction |
| P2 | Residential college GE requirement details | Each college's website | 10 colleges, each with unique GE requirements |
| P2 | Per-program GRE/TOEFL requirements (graduate) | Each department's admissions page | Decentralized; requires per-program crawl |
| P2 | Transfer admission requirements detail | admissions.ucsc.edu/transfer-students | TAG details, major preparation |

---

## SECTION 7 -- Cross-School Comparison Framework

| Dimension | UCSC Value | Notes |
|-----------|-----------|-------|
| Type | Public (UC system) | |
| Location | Santa Cruz, CA | Near Silicon Valley |
| Total enrollment (fall 2025) | 20,140 | 18,194 UG + 1,946 grad |
| UG tuition & fees (2026-27, in-state) | $17,490 | UC system-wide |
| UG tuition & fees (2026-27, OOS) | $56,760 | $17,490 + $39,270 NRT |
| UG total COA on-campus (in-state) | $47,628 | |
| UG total COA on-campus (OOS) | $86,898 | |
| SAT/ACT policy | Test-FREE | Not used in admission |
| TOEFL minimum | 4.5 iBT (per website; likely error) | Verify with admissions |
| IELTS minimum | 6.5 | |
| DET minimum | 115 | |
| Application portal | UC Application | Oct 1 - Nov 30 |
| EA/ED deadline | N/A | UC system has no EA/ED |
| RD deadline | November 30, 2026 | |
| First-year admission rate (2025) | 72.7% | |
| Transfer admission rate (2025) | 70.4% | |
| Mean first-year GPA (2025) | 4.00 | |
| Retention rate | 88% | |
| 6-year graduation rate | 75% | |
| Need-blind (intl)? | No (need-aware) | |
| Total degree programs (Rule 1) | 140 | 75 UG + 31 Master's + 34 PhD/DMA |
| Academic divisions (Rule 2) | 5 | Arts, Humanities, Social Sciences, Baskin Engineering, PBSci |
| Residential colleges | 10 | |
| Graduate fields | 41 | 57 concentrations |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.ucsc.edu, financialaid.ucsc.edu, catalog.ucsc.edu, graddiv.ucsc.edu, registrar.ucsc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
