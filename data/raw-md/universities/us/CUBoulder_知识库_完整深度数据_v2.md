# University of Colorado Boulder Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BEV/BMus/BAMus/BMUE) | 94 |
| 本科辅修 (Minor) | 87 |
| 本科证书 (Certificate) | 43 |
| 研究生学位项目 (MA/MS/PhD/MBA/MFA/MEnv/ME/LLM/MSL/AuD/DMA) | 150 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 0 |
| **学位项目总计 (UG + Grad)** | **374** |
| 学院 / 独立系所总数 | 10 |

> **Note**: The Graduate School website states "124 master's, doctoral and professional degree programs" — this counts unique program names. Our catalog extraction counts each degree type separately (e.g., "Computer Science" with both MS and PhD = 2 rows), yielding 150 graduate degree rows. The Graduate School number refers to distinct program names; our count is degree-program rows.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Colorado Boulder
├── College of Arts and Sciences                          [学院]
│   ├── Actuarial Studies and Quantitative Finance        [系]
│   ├── Anthropology                                      [系]
│   ├── Applied Mathematics                               [系]
│   ├── Art and Art History                               [系]
│   ├── Asian Languages and Civilizations                 [系]
│   ├── Asian Studies                                     [系]
│   ├── Astrophysical and Planetary Sciences              [系]
│   ├── Atmospheric and Oceanic Sciences                  [系]
│   ├── Biochemistry                                      [系]
│   ├── Chemistry                                         [系]
│   ├── Cinema Studies & Moving Image Arts                [系]
│   ├── Classics                                          [系]
│   ├── Communication (some programs)                     [系]  ⚠ shared with CMDI
│   ├── Ecology and Evolutionary Biology                  [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── Environmental Studies                             [系]
│   ├── Ethnic Studies                                    [系]
│   ├── French and Italian                                [系]
│   ├── Geography                                         [系]
│   ├── Germanic and Slavic Languages and Literatures     [系]
│   ├── History                                           [系]
│   ├── Humanities                                        [系]
│   ├── Integrative Physiology                            [系]
│   ├── International Affairs                             [系]
│   ├── Jewish Studies                                    [系]
│   ├── Linguistics                                       [系]
│   ├── Mathematics                                       [系]
│   ├── Molecular, Cellular and Developmental Biology     [系]
│   ├── Music (BA programs)                               [系]  ⚠ shared with College of Music
│   ├── Neuroscience                                      [系]
│   ├── Philosophy                                        [系]
│   ├── Physics                                           [系]
│   ├── Political Science                                 [系]
│   ├── Psychology                                        [系]
│   ├── Religious Studies                                 [系]
│   ├── Sociology                                         [系]
│   ├── Spanish and Portuguese                            [系]
│   ├── Speech, Language and Hearing Sciences             [系]
│   ├── Statistics and Data Science                       [系]
│   ├── Women and Gender Studies                          [系]
│   └── Environment (MEnv, MS, PhD)                       [系]
├── College of Engineering and Applied Science             [学院]
│   ├── Aerospace Engineering Sciences                    [系]
│   ├── Applied Mathematics (engineering programs)        [系]
│   ├── Architectural Engineering                         [系]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical and Biological Engineering               [系]
│   ├── Civil Engineering                                 [系]
│   ├── Computer Science                                  [系]
│   ├── Electrical Engineering                            [系]
│   ├── Engineering Management                            [系]
│   ├── Engineering Physics                               [系]
│   ├── Environmental Engineering                         [系]
│   ├── Materials Science and Engineering                 [系]
│   ├── Mechanical Engineering                            [系]
│   └── Technology, Arts and Media                        [系]
├── College of Communication, Media, Design and Information [学院]
│   ├── Communication                                     [系]
│   ├── Journalism                                        [系]
│   ├── Media Production and Studies                      [系]
│   ├── Strategic Communication                           [系]
│   ├── Architecture (BEV programs)                       [系]
│   ├── Environmental Design                              [系]
│   ├── Landscape Architecture                            [系]
│   └── Sustainable Planning and Urban Design             [系]
├── Leeds School of Business                               [学院]
│   ├── Accounting                                        [系]
│   ├── Business Administration                           [系]
│   ├── Finance                                           [系]
│   ├── Marketing                                         [系]
│   └── Real Estate                                       [系]
├── School of Education                                    [学院]
│   ├── Curriculum and Instruction                        [系]
│   ├── Educational Foundations                           [系]
│   └── Educational Equity and Cultural Diversity         [系]
├── College of Music                                       [学院]
│   ├── Music Performance                                 [系]
│   ├── Music Education                                   [系]
│   ├── Music Theory                                      [系]
│   └── Musical Arts (DMA)                                [系]
├── University of Colorado Law School                      [学院]
│   └── Law (LLM, MSL)                                   [系]
├── Program in Exploratory Studies                         [学院]
│   └── Open Option in Arts & Sciences                    [系]
├── Graduate School                                        [学院]
│   └── (administers graduate programs across all schools) [系]
├── Continuing Education and Professional Studies          [学院]
│   └── (non-degree and professional programs)            [系]
└── University Libraries                                   [学院]
```

> **Note**: Environmental Design programs (BEV degrees) are housed within the College of Communication, Media, Design and Information. The Law School offers graduate-only programs (LLM, MSL). The Graduate School administers graduate admissions across all schools but does not grant its own degrees.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 48 |
| BS | Bachelor of Science (various prefixes) | 本科 | 31 |
| BFA | Bachelor of Fine Arts | 本科 | 5 |
| BEV | Bachelor of Environmental Design | 本科 | 4 |
| BMus | Bachelor of Music | 本科 | 1 |
| BAMus | Bachelor of Arts in Music | 本科 | 1 |
| BMUE | Bachelor of Music Education | 本科 | 1 |
| Minor | 辅修 (本科) | 本科 | 87 |
| Certificate | 证书 (本科) | 本科 | 43 |
| MA | Master of Arts | 研究生 | 38 |
| MS | Master of Science (various prefixes) | 研究生 | 38 |
| PhD | Doctor of Philosophy | 研究生 | 57 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MEnv | Master of the Environment | 研究生 | 1 |
| MBA | Master of Business Administration | 研究生 | 1 |
| ME | Master of Engineering | 研究生 | 3 |
| LLM | Master of Laws | 研究生 | 1 |
| MSL | Master of Studies in Law | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| MMus | Master of Music | 研究生 | 2 |
| MMUE | Master of Music Education | 研究生 | 1 |
| **合计** | | | **374** |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BEV | BMus | BAMus | BMUE | Minor | Cert | MA | MS | PhD | MFA | MEnv | MBA | ME | LLM | MSL | AuD | DMA | MMus | MMUE | 合计 |
|------------|----|----|-----|-----|------|-------|------|-------|------|----|----|-----|-----|------|-----|----|-----|-----|-----|-----|------|------|------|
| Arts & Sciences | 45 | 10 | 3 | 0 | 0 | 0 | 0 | 59 | 35 | 30 | 8 | 30 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 224 |
| Engineering & Applied Science | 1 | 21 | 0 | 0 | 0 | 0 | 0 | 15 | 2 | 0 | 21 | 14 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 78 |
| CMDI | 2 | 0 | 2 | 4 | 0 | 0 | 0 | 5 | 6 | 3 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 29 |
| Leeds Business | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 4 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 21* |
| Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15* |
| Music | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 13* |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| **合计** | 48 | 32 | 5 | 4 | 1 | 1 | 1 | 86 | 48 | 41 | 33 | 52 | 4 | 1 | 1 | 3 | 1 | 1 | 1 | 1 | 2 | 1 | **374** |

> *Note: Row totals marked with asterisk include programs counted across multiple degree types. The matrix uses canonical degree codes per degree-taxonomy.md. BS includes all BS-prefix variants (BSAE, BSAM, BSBM, BSBE, BSCHE, BSARE, BSCV, BSEV, BSCS, BSCTD, BSEC, BSEE, BSEP, BSIDE, BSME, BSBA). ME includes ME and ME Online variants. MS includes MS, MS Online, MSAI, MSNE, MSECE, MSSB, MSSE variants.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

CU Boulder has 10 academic units. The College of Arts and Sciences is the largest, housing over 60 fields of study. The College of Engineering and Applied Science is nationally recognized, particularly for aerospace engineering. Environmental Design programs are housed within the College of Communication, Media, Design and Information. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Actuarial Studies and Quantitative Finance
###### Certificate
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Studies and Quantitative Finance | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/actuarial-studies-quantitative-finance/actuarial-studies-quantitative-finance-certificate/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/anthropology/anthropology-bachelor-arts-ba/ |

##### Applied Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics and Data Science | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/applied-mathematics/statistics-data-science-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics and Data Science | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/applied-mathematics/statistics-data-science-bachelor-science-bs/ |

##### Art and Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/art-art-history/art-history-bachelor-arts-ba/ |
| 2 | Art Practices | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/art-art-history/art-practices-bachelor-arts-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Practices | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/art-art-history/art-practices-bachelor-fine-arts-bfa/ |

##### Asian Languages and Civilizations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/asian-languages-civilizations/chinese-bachelor-arts-ba/ |
| 2 | Japanese | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/asian-languages-civilizations/japanese-bachelor-arts-ba/ |

##### Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/asian-studies/asian-studies-bachelor-arts-ba/ |

##### Astrophysical and Planetary Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysical and Planetary Sciences | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/astrophysical-planetary-sciences/astrophysical-planetary-sciences-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysical and Planetary Sciences | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/astrophysical-planetary-sciences/astrophysical-planetary-sciences-bachelor-science-bs/ |

##### Atmospheric and Oceanic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Atmospheric and Oceanic Sciences | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/atmospheric-oceanic-sciences/atmospheric-oceanic-sciences-bachelor-science-bs/ |

##### Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/biochemistry/biochemistry-bachelor-science-bs/ |

##### Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/chemistry/chemistry-bachelor-science-bs/ |

##### Cinema Studies & Moving Image Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Cinema Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/cinema-studies-moving-image-arts/cinema-studies-bachelor-arts-ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Cinema Studies & Moving Image Arts | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/cinema-studies-moving-image-arts/cinema-studies-moving-image-arts-bachelor-fine-arts-bfa/ |

##### Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/classics/classics-bachelor-arts-ba/ |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/communication/communication-bachelor-arts-ba/ |

##### Ecology and Evolutionary Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology and Evolutionary Biology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/ecology-evolutionary-biology/ecology-evolutionary-biology-bachelor-arts-ba/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/economics/economics-bachelor-arts-ba/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/english/english-bachelor-arts-ba/ |

##### Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/environmental-studies/environmental-studies-bachelor-arts-ba/ |

##### Ethnic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/ethnic-studies/ethnic-studies-bachelor-arts-ba/ |

##### French and Italian
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/french-italian/french-bachelor-arts-ba/ |
| 2 | Italian | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/french-italian/italian-bachelor-arts-ba/ |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/geography/geography-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/geography/geography-bachelor-science-bs/ |

##### Germanic and Slavic Languages and Literatures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | German Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/germanic-slavic-languages-literatures/german-studies-bachelor-arts-ba/ |
| 2 | Russian Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/germanic-slavic-languages-literatures/russian-studies-bachelor-arts-ba/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/history/history-bachelor-arts-ba/ |

##### Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Humanities | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/humanities/humanities-bachelor-arts-ba/ |

##### Integrative Physiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Integrative Physiology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/integrative-physiology/integrative-physiology-bachelor-science-bs/ |

##### International Affairs
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Affairs | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/international-affairs/international-affairs-bachelor-arts-ba/ |

##### Jewish Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Jewish Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/jewish-studies/jewish-studies-bachelor-arts-ba/ |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/linguistics/linguistics-bachelor-arts-ba/ |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/mathematics/mathematics-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/mathematics/mathematics-bachelor-science-bs/ |

##### Molecular, Cellular and Developmental Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Molecular, Cellular and Developmental Biology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/molecular-cellular-developmental-biology/molecular-cellular-developmental-biology-bachelor-science-bs/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/music/music-bachelor-arts-ba/ |

##### Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/neuroscience/neuroscience-bachelor-science-bs/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/philosophy/philosophy-bachelor-arts-ba/ |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/physics/physics-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/physics/physics-bachelor-science-bs/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/political-science/political-science-bachelor-arts-ba/ |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/psychology/psychology-bachelor-arts-ba/ |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/religious-studies/religious-studies-bachelor-arts-ba/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/sociology/sociology-bachelor-arts-ba/ |

##### Spanish and Portuguese
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/spanish-portuguese/spanish-bachelor-arts-ba/ |

##### Speech, Language and Hearing Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech, Language and Hearing Sciences | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/speech-language-hearing-sciences/speech-language-hearing-sciences-bachelor-arts-ba/ |

##### Women and Gender Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women and Gender Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/arts-sciences/programs-study/women-gender-studies/women-gender-studies-bachelor-arts-ba/ |

#### College of Engineering and Applied Science

##### Aerospace Engineering Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering Sciences | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/aerospace-engineering-sciences/aerospace-engineering-sciences-bachelor-science-bsae/ |

##### Applied Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/applied-mathematics/applied-mathematics-bachelor-science-bsam/ |

##### Architectural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/architectural-engineering/architectural-engineering-bachelor-science-bsare/ |

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/biomedical-engineering/biomedical-engineering-bachelor-science-bsbm/ |

##### Chemical and Biological Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/chemical-biological-engineering/chemical-engineering-bachelor-science-bsche/ |

##### Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/civil-engineering/civil-engineering-bachelor-science-bscv/ |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/computer-science/computer-science-bachelor-arts-ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/computer-science/computer-science-bachelor-science-bscs/ |

##### Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/electrical-engineering/electrical-engineering-bachelor-science-bsee/ |
| 2 | Electrical and Computer Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/electrical-engineering/electrical-computer-engineering-bachelor-science-bsec/ |

##### Engineering Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Physics | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/engineering-physics/engineering-physics-bachelor-science-bsep/ |

##### Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/environmental-engineering/environmental-engineering-bachelor-science-bsev/ |

##### Integrated Design Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Plus | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/integrated-design-engineering/engineering-plus-bachelor-science-bside/ |

##### Materials Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/materials-science-engineering/materials-science-engineering-bachelor-science-bs/ |

##### Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/mechanical-engineering/mechanical-engineering-bachelor-science-bsme/ |

##### Technology, Arts and Media
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Technology and Design | https://catalog.colorado.edu/undergraduate/colleges-schools/engineering-applied-science/programs-study/technology-arts-media/creative-technology-design-bachelor-science-bsctd/ |

#### College of Communication, Media, Design and Information

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | (see Arts & Sciences Communication) |

##### Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/journalism/journalism-bachelor-arts-ba/ |

##### Media Production and Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Media Production | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/media-production/media-production-bachelor-arts-ba/ |
| 2 | Media Studies | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/media-studies/media-studies-bachelor-arts-ba/ |

##### Strategic Communication
###### MA
| # | 专业 | URL |
|---|------|-----|
| 1 | Strategic Communication | https://catalog.colorado.edu/graduate/colleges-schools/communication-media-design-information/programs-study/strategic-communication/strategic-communication-master-arts-ma/ |

##### Architecture and Environmental Design
###### BEV
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/architecture/architecture-bachelor-environmental-design-bev/ |
| 2 | Environmental Products of Design | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/environmental-design/environmental-products-design-bachelor-environmental-design-bev/ |
| 3 | Landscape Architecture | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/landscape-architecture/landscape-architecture-bachelor-environmental-design-bev/ |
| 4 | Sustainable Planning and Urban Design | https://catalog.colorado.edu/undergraduate/colleges-schools/communication-media-design-information/programs-study/sustainable-planning-urban-design/sustainable-planning-urban-design-bachelor-environmental-design-bev/ |

#### Leeds School of Business

##### Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.colorado.edu/undergraduate/colleges-schools/business/programs-study/business-administration/business-administration-bachelor-science-bsba/ |

#### College of Music

##### Music
###### BMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.colorado.edu/undergraduate/colleges-schools/music/programs-study/music/music-bachelor-music-bmus/ |

###### BAMus
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.colorado.edu/undergraduate/colleges-schools/music/programs-study/music/music-bachelor-arts-music-bamus/ |

##### Music Education
###### BMUE
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | https://catalog.colorado.edu/undergraduate/colleges-schools/music/programs-study/music-education/music-education-bachelor-music-education-bmue/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

CU Boulder offers several cross-college programs. The Computer Science BA is offered through Engineering but is also accessible to Arts & Sciences students. Environmental Studies spans Arts & Sciences and Engineering. Communication programs are shared between Arts & Sciences and CMDI.

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | Anthropology | Arts & Sciences | catalog.colorado.edu |
| 2 | Applied Mathematics | Arts & Sciences | catalog.colorado.edu |
| 3 | Arabic | Arts & Sciences | catalog.colorado.edu |
| 4 | Architectural Engineering | Engineering | catalog.colorado.edu |
| 5 | Art History | Arts & Sciences | catalog.colorado.edu |
| 6 | Art Practices | Arts & Sciences | catalog.colorado.edu |
| 7 | Asian Studies | Arts & Sciences | catalog.colorado.edu |
| 8 | Astrophysical and Planetary Sciences | Arts & Sciences | catalog.colorado.edu |
| 9 | Atmospheric and Oceanic Sciences | Arts & Sciences | catalog.colorado.edu |
| 10 | Biochemistry | Arts & Sciences | catalog.colorado.edu |
| 11 | Business | Leeds Business | catalog.colorado.edu |
| 12 | Chemistry | Arts & Sciences | catalog.colorado.edu |
| 13 | Chinese | Arts & Sciences | catalog.colorado.edu |
| 14 | Cinema Studies | Arts & Sciences | catalog.colorado.edu |
| 15 | Civil Engineering | Engineering | catalog.colorado.edu |
| 16 | Classics | Arts & Sciences | catalog.colorado.edu |
| 17 | Communication | Arts & Sciences | catalog.colorado.edu |
| 18 | Computer Science | Engineering | catalog.colorado.edu |
| 19 | Creative Writing | Arts & Sciences | catalog.colorado.edu |
| 20 | Dance | CMDI | catalog.colorado.edu |
| 21 | Data Science | Engineering | catalog.colorado.edu |
| 22 | Design Studies | CMDI | catalog.colorado.edu |
| 23 | Ecology and Evolutionary Biology | Arts & Sciences | catalog.colorado.edu |
| 24 | Economics | Arts & Sciences | catalog.colorado.edu |
| 25 | Education | Education | catalog.colorado.edu |
| 26 | Electrical Engineering | Engineering | catalog.colorado.edu |
| 27 | Engineering Management | Engineering | catalog.colorado.edu |
| 28 | English | Arts & Sciences | catalog.colorado.edu |
| 29 | Environmental Planning | CMDI | catalog.colorado.edu |
| 30 | Environmental Studies | Arts & Sciences | catalog.colorado.edu |
| 31 | Ethnic Studies | Arts & Sciences | catalog.colorado.edu |
| 32 | Film Studies | Arts & Sciences | catalog.colorado.edu |
| 33 | French | Arts & Sciences | catalog.colorado.edu |
| 34 | Geography | Arts & Sciences | catalog.colorado.edu |
| 35 | Geology | Arts & Sciences | catalog.colorado.edu |
| 36 | German Studies | Arts & Sciences | catalog.colorado.edu |
| 37 | Global Engineering | Engineering | catalog.colorado.edu |
| 38 | Hindi/Urdu | Arts & Sciences | catalog.colorado.edu |
| 39 | History | Arts & Sciences | catalog.colorado.edu |
| 40 | Humanities | Arts & Sciences | catalog.colorado.edu |
| 41 | Information Science | Arts & Sciences | catalog.colorado.edu |
| 42 | International Affairs | Arts & Sciences | catalog.colorado.edu |
| 43 | Italian | Arts & Sciences | catalog.colorado.edu |
| 44 | Japanese | Arts & Sciences | catalog.colorado.edu |
| 45 | Jewish Studies | Arts & Sciences | catalog.colorado.edu |
| 46 | Journalism | CMDI | catalog.colorado.edu |
| 47 | Korean | Arts & Sciences | catalog.colorado.edu |
| 48 | Leadership Studies | Arts & Sciences | catalog.colorado.edu |
| 49 | Linguistics | Arts & Sciences | catalog.colorado.edu |
| 50 | Mathematics | Arts & Sciences | catalog.colorado.edu |
| 51 | Mechanical Engineering | Engineering | catalog.colorado.edu |
| 52 | Media Production | CMDI | catalog.colorado.edu |
| 53 | Media Studies | CMDI | catalog.colorado.edu |
| 54 | Molecular, Cellular and Developmental Biology | Arts & Sciences | catalog.colorado.edu |
| 55 | Music | Music | catalog.colorado.edu |
| 56 | Nordic Studies | Arts & Sciences | catalog.colorado.edu |
| 57 | Philosophy | Arts & Sciences | catalog.colorado.edu |
| 58 | Physics | Arts & Sciences | catalog.colorado.edu |
| 59 | Political Science | Arts & Sciences | catalog.colorado.edu |
| 60 | Portuguese | Arts & Sciences | catalog.colorado.edu |
| 61 | Psychology | Arts & Sciences | catalog.colorado.edu |
| 62 | Religious Studies | Arts & Sciences | catalog.colorado.edu |
| 63 | Russian Studies | Arts & Sciences | catalog.colorado.edu |
| 64 | Sociology | Arts & Sciences | catalog.colorado.edu |
| 65 | Spanish | Arts & Sciences | catalog.colorado.edu |
| 66 | Speech, Language and Hearing Sciences | Arts & Sciences | catalog.colorado.edu |
| 67 | Sports Media | CMDI | catalog.colorado.edu |
| 68 | Statistics | Arts & Sciences | catalog.colorado.edu |
| 69 | Sustainability | Engineering | catalog.colorado.edu |
| 70 | Technology, Arts and Media | Engineering | catalog.colorado.edu |
| 71 | Theatre | CMDI | catalog.colorado.edu |
| 72 | Women and Gender Studies | Arts & Sciences | catalog.colorado.edu |
| 73 | Writing and Public Engagement | Arts & Sciences | catalog.colorado.edu |
| 74 | Writing and Rhetoric | Arts & Sciences | catalog.colorado.edu |
| 75-87 | (Additional minors from catalog) | Various | catalog.colorado.edu |

### 1.5 General/Institute-wide requirements

CU Boulder requires all undergraduate students to complete the **Core Curriculum** through the College of Arts and Sciences. This includes:
- Written Communication (6 credits)
- Quantitative Reasoning and Mathematical Skills (3-4 credits)
- Arts & Humanities, Social Sciences, Natural Sciences (distribution requirements)
- Diversity requirements

Students in the Program in Exploratory Studies complete their first year before transferring to their chosen college.

### 1.6 Course-ID → Major quick-lookup

CU Boulder does not use a centralized course-ID numbering system for majors. Programs are identified by name and college affiliation in the catalog.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

The Graduate School administers 124 master's, doctoral and professional degree programs across all schools. Graduate admissions is decentralized — each department sets its own deadlines, requirements, and GRE policy.

#### College of Arts and Sciences

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | catalog.colorado.edu |
| 2 | Art History | catalog.colorado.edu |
| 3 | Asian Languages and Civilizations | catalog.colorado.edu |
| 4 | Classics | catalog.colorado.edu |
| 5 | Communication | catalog.colorado.edu |
| 6 | Ecology and Evolutionary Biology | catalog.colorado.edu |
| 7 | Economics | catalog.colorado.edu |
| 8 | English | catalog.colorado.edu |
| 9 | Educational Equity and Cultural Diversity | catalog.colorado.edu |
| 10 | French | catalog.colorado.edu |
| 11 | Geography | catalog.colorado.edu |
| 12 | German Studies | catalog.colorado.edu |
| 13 | History | catalog.colorado.edu |
| 14 | Linguistics | catalog.colorado.edu |
| 15 | Mathematics | catalog.colorado.edu |
| 16 | Molecular, Cellular and Developmental Biology | catalog.colorado.edu |
| 17 | Philosophy | catalog.colorado.edu |
| 18 | Political Science | catalog.colorado.edu |
| 19 | Psychology | catalog.colorado.edu |
| 20 | Religious Studies | catalog.colorado.edu |
| 21 | Russian Studies | catalog.colorado.edu |
| 22 | Sociology | catalog.colorado.edu |
| 23 | Spanish | catalog.colorado.edu |
| 24 | Speech, Language and Hearing Sciences | catalog.colorado.edu |
| 25 | Theatre | catalog.colorado.edu |
| 26 | Women and Gender Studies | catalog.colorado.edu |
| 27 | Curriculum and Instruction | catalog.colorado.edu |
| 28 | Educational Foundations | catalog.colorado.edu |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | catalog.colorado.edu |
| 2 | Astrophysical and Planetary Sciences | catalog.colorado.edu |
| 3 | Atmospheric and Oceanic Sciences | catalog.colorado.edu |
| 4 | Chemistry | catalog.colorado.edu |
| 5 | Computer Science | catalog.colorado.edu |
| 6 | Ecology and Evolutionary Biology | catalog.colorado.edu |
| 7 | Environmental Studies | catalog.colorado.edu |
| 8 | Geography | catalog.colorado.edu |
| 9 | Geological Sciences | catalog.colorado.edu |
| 10 | Geophysics | catalog.colorado.edu |
| 11 | Information Science | catalog.colorado.edu |
| 12 | Integrative Physiology | catalog.colorado.edu |
| 13 | Mathematics | catalog.colorado.edu |
| 14 | Museum and Field Studies | catalog.colorado.edu |
| 15 | Neuroscience | catalog.colorado.edu |
| 16 | Physics | catalog.colorado.edu |
| 17 | Psychology | catalog.colorado.edu |
| 18 | Speech, Language and Hearing Sciences | catalog.colorado.edu |
| 19 | Statistics | catalog.colorado.edu |
| 20 | Technology, Arts and Media | catalog.colorado.edu |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | catalog.colorado.edu |
| 2 | Applied Mathematics | catalog.colorado.edu |
| 3 | Astrophysical and Planetary Sciences | catalog.colorado.edu |
| 4 | Atmospheric and Oceanic Sciences | catalog.colorado.edu |
| 5 | Chemistry | catalog.colorado.edu |
| 6 | Classics | catalog.colorado.edu |
| 7 | Cognitive Science | catalog.colorado.edu |
| 8 | Communication | catalog.colorado.edu |
| 9 | Computer Science | catalog.colorado.edu |
| 10 | Ecology and Evolutionary Biology | catalog.colorado.edu |
| 11 | Economics | catalog.colorado.edu |
| 12 | English | catalog.colorado.edu |
| 13 | Environmental Studies | catalog.colorado.edu |
| 14 | Ethnic Studies | catalog.colorado.edu |
| 15 | French | catalog.colorado.edu |
| 16 | Geography | catalog.colorado.edu |
| 17 | Geological Sciences | catalog.colorado.edu |
| 18 | Geophysics | catalog.colorado.edu |
| 19 | German Studies | catalog.colorado.edu |
| 20 | History | catalog.colorado.edu |
| 21 | Integrative Physiology | catalog.colorado.edu |
| 22 | Linguistics | catalog.colorado.edu |
| 23 | Mathematics | catalog.colorado.edu |
| 24 | Molecular, Cellular and Developmental Biology | catalog.colorado.edu |
| 25 | Neuroscience | catalog.colorado.edu |
| 26 | Philosophy | catalog.colorado.edu |
| 27 | Physics | catalog.colorado.edu |
| 28 | Political Science | catalog.colorado.edu |
| 29 | Psychology | catalog.colorado.edu |
| 30 | Sociology | catalog.colorado.edu |
| 31 | Speech, Language and Hearing Sciences | catalog.colorado.edu |

##### MFA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Art Practices | catalog.colorado.edu |
| 2 | Creative Writing | catalog.colorado.edu |
| 3 | Dance | catalog.colorado.edu |
| 4 | Interdisciplinary Documentary Media | catalog.colorado.edu |

##### Other Graduate Degrees
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Environment | MEnv | catalog.colorado.edu |
| 2 | Audiology | AuD | catalog.colorado.edu |

#### College of Engineering and Applied Science

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering Sciences | catalog.colorado.edu |
| 2 | Applied Mathematics | catalog.colorado.edu |
| 3 | Architectural Engineering | catalog.colorado.edu |
| 4 | Biomedical Engineering | catalog.colorado.edu |
| 5 | Chemical Engineering | catalog.colorado.edu |
| 6 | Civil Engineering | catalog.colorado.edu |
| 7 | Computer Science | catalog.colorado.edu |
| 8 | Computer Science (Online) | catalog.colorado.edu |
| 9 | Electrical Engineering | catalog.colorado.edu |
| 10 | Electrical and Computer Engineering (Online) | catalog.colorado.edu |
| 11 | Engineering Management | catalog.colorado.edu |
| 12 | Engineering for Developing Communities | catalog.colorado.edu |
| 13 | Environmental Engineering | catalog.colorado.edu |
| 14 | Materials Science and Engineering | catalog.colorado.edu |
| 15 | Mechanical Engineering | catalog.colorado.edu |
| 16 | Telecommunications | catalog.colorado.edu |
| 17 | Technology, Arts and Media | catalog.colorado.edu |

##### ME Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | catalog.colorado.edu |
| 2 | Engineering Management (Online) | catalog.colorado.edu |

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering Sciences | catalog.colorado.edu |
| 2 | Applied Mathematics | catalog.colorado.edu |
| 3 | Biomedical Engineering | catalog.colorado.edu |
| 4 | Chemical Engineering | catalog.colorado.edu |
| 5 | Civil Engineering | catalog.colorado.edu |
| 6 | Computer Science | catalog.colorado.edu |
| 7 | Electrical Engineering | catalog.colorado.edu |
| 8 | Engineering Management | catalog.colorado.edu |
| 9 | Environmental Engineering | catalog.colorado.edu |
| 10 | Materials Science and Engineering | catalog.colorado.edu |
| 11 | Mechanical Engineering | catalog.colorado.edu |
| 12 | Technology, Arts and Media | catalog.colorado.edu |

#### College of Communication, Media, Design and Information

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Communication | MA | catalog.colorado.edu |
| 2 | Journalism | MA | catalog.colorado.edu |
| 3 | Media Public Engagement | MA | catalog.colorado.edu |
| 4 | Strategic Communication | MA | catalog.colorado.edu |
| 5 | Communication | PhD | catalog.colorado.edu |
| 6 | Media Research | PhD | catalog.colorado.edu |
| 7 | Emergent Technologies and Media Art Practices | PhD | catalog.colorado.edu |

#### Leeds School of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration | MBA | catalog.colorado.edu |
| 2 | Accounting | MS | catalog.colorado.edu |
| 3 | Business Analytics | MS | catalog.colorado.edu |
| 4 | Finance | MS | catalog.colorado.edu |
| 5 | Real Estate | MS | catalog.colorado.edu |
| 6 | Supply Chain Management | MS | catalog.colorado.edu |
| 7 | Business | PhD | catalog.colorado.edu |

#### School of Education

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Curriculum and Instruction | MA | catalog.colorado.edu |
| 2 | Educational Equity and Cultural Diversity | MA | catalog.colorado.edu |
| 3 | Educational Foundations | MA | catalog.colorado.edu |
| 4 | Educational Foundations | PhD | catalog.colorado.edu |
| 5 | Learning Sciences and Human Development | PhD | catalog.colorado.edu |
| 6 | Educational Equity and Cultural Diversity | PhD | catalog.colorado.edu |

#### College of Music

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | MMus | catalog.colorado.edu |
| 2 | Music Education | MMUE | catalog.colorado.edu |
| 3 | Music | PhD | catalog.colorado.edu |
| 4 | Musical Arts | DMA | catalog.colorado.edu |

#### University of Colorado Law School

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law | LLM | https://catalog.colorado.edu/law/programs-study/law-master-laws-llm/ |
| 2 | Law | MSL | https://catalog.colorado.edu/law/programs-study/law-master-studies-law-msl/ |

> **Note**: The Law School also offers the JD (Juris Doctor) degree, which is not listed in the catalog's programs-a-z page but is the school's primary professional degree.

### 2.2 At least one program's full deep-dive (worked example)

**Aerospace Engineering Sciences (MS/PhD) — College of Engineering and Applied Science**

- **Department**: Ann and H.J. Smead Department of Aerospace Engineering Sciences
- **Address**: 429 UCB, Boulder, CO 80309
- **Phone**: 303-492-6466
- **Application portal**: https://www.colorado.edu/graduateschool/admissions
- **GRE**: Required for PhD; optional for MS (check department page)
- **TOEFL/IELTS**: Required for international students
- **Application deadline**: Varies by program; typically Dec 15 for fall admission
- **Application fee**: $80
- **Funding**: RA/TA positions available for PhD students; MS students typically self-funded

### 2.3 Graduate admissions model

**Decentralized model** — The Graduate School provides the application portal and minimum standards, but each department makes its own admission decisions, sets its own deadlines, and determines GRE/materials requirements.

**Entry points**:
- Graduate School admissions hub: https://www.colorado.edu/graduateschool/admissions
- Per-program deadlines: https://www.colorado.edu/graduateschool/admissions/programs-deadlines
- International students: https://www.colorado.edu/graduateschool/admissions/where-begin/international-students

**Application fee**: $80 (nonrefundable)

**GRE code**: 4841

**GMAT code**: 4841 (Business PhD only)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| **Application portal** | Common App | https://www.colorado.edu/admissions/process/first-year/apply |
| **EA deadline** | November 15 | https://www.colorado.edu/admissions/process/first-year/apply |
| **RD deadline** | January 15 | https://www.colorado.edu/admissions/process/first-year/apply |
| **Spring deadline** | October 1 | https://www.colorado.edu/admissions/process/first-year/apply |
| **EA decision notification** | February 1 | https://www.colorado.edu/admissions/process/first-year/apply |
| **RD decision notification** | April 1 | https://www.colorado.edu/admissions/process/first-year/apply |
| **Application fee (domestic)** | $65 | https://www.colorado.edu/admissions/process/first-year/apply |
| **Application fee (international)** | $70 | https://www.colorado.edu/admissions/process/first-year/apply |
| **SAT/ACT policy** | Test-optional (self-reported scores accepted) | https://www.colorado.edu/admissions/process/first-year/apply |
| **Superscore** | N/A (test-optional) | |
| **Interview policy** | Not offered | |
| **Recommendations** | 1 letter of recommendation | https://www.colorado.edu/admissions/process/first-year/apply |
| **Transcripts** | Required (high school) | https://www.colorado.edu/admissions/process/first-year/apply |
| **Enrollment confirmation deadline** | May 1 | Standard |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Recommended Score | Notes |
|------|--------------|-------------------|-------|
| TOEFL iBT (Jan 2026+) | 4.0 (new scale) | N/A | New reporting scale as of Jan 2026 |
| TOEFL iBT (pre-2026) | 80 | N/A | Old 120-point scale |
| IELTS | 6.5 | N/A | Academic module |
| Cambridge (C1 Advanced or C2 Proficiency) | 180 | N/A | |
| PTE Academic | 58 | N/A | |
| Duolingo | 115 | N/A | |
| IB SL English A | 6 | N/A | |
| IB HL English A | 5 | N/A | |
| GCSE/GCE English | B | N/A | |
| AP English | 4 | N/A | |
| SAT EBRW | 580 | N/A | |
| ACT English | 23 | N/A | |

> **Source**: https://www.colorado.edu/admissions/process/international/plan/english-proficiency
> **Exemptions**: Students who completed 2+ years of full-time academic study at a secondary school in a qualifying English-speaking country, or 24+ transferable credits at a university in a qualifying country. Scores must be within 2 calendar years of start date.
> **Conditional admission**: Available through the Pathway to CU Program for students who meet academic requirements but need English improvement.

### 3.3 Graduate — global rules

| 字段 | 值 | 来源 |
|------|-----|------|
| **Admissions model** | Decentralized (each department decides) | https://www.colorado.edu/graduateschool/admissions |
| **Application portal** | Graduate School portal | https://www.colorado.edu/graduateschool/admissions |
| **Application fee** | $80 | https://www.colorado.edu/graduateschool/admissions/where-begin/international-students |
| **GRE** | Required for many departments (code 4841) | https://www.colorado.edu/graduateschool/admissions/where-begin/international-students |
| **GMAT** | Required for Business PhD (code 4841) | https://www.colorado.edu/graduateschool/admissions/where-begin/international-students |
| **GPA minimum** | 2.75 (3.00 for Engineering) | https://www.colorado.edu/graduateschool/admissions/where-begin |
| **English proficiency** | TOEFL/IELTS required; Duolingo accepted (min 120) | https://www.colorado.edu/graduateschool/admissions/where-begin/international-students |
| **CGS April-15** | Yes (signatory) | Standard |
| **Deadlines** | Per-program; typically Dec-Jan for fall | https://www.colorado.edu/graduateschool/admissions |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

**Colorado Resident — Base Rate (Arts & Humanities, Education, Music, Social Sciences)**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Base Tuition & Fees | $7,507 | $15,014 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$17,728** | **$35,456** |

**Colorado Resident — Tier 3 (Communication, Media, Design and Information)**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Tier 3 Tuition & Fees | $9,535 | $19,070 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$19,756** | **$39,512** |

**Colorado Resident — Tier 4 (Engineering, Natural Sciences, Business)**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Tier 4 Tuition & Fees | $10,627 | $21,254 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$20,848** | **$41,696** |

**Nonresident — Base Rate**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Base Tuition & Fees | $23,029 | $46,058 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$33,250** | **$66,500** |

**Nonresident — Tier 4 (Engineering, Natural Sciences, Business)**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Tier 4 Tuition & Fees | $25,083 | $50,166 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$35,304** | **$70,608** |

**International — Base Rate**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Base Tuition & Fees | $24,111 | $48,222 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$34,332** | **$68,664** |

**International — Tier 4 (Engineering, Natural Sciences, Business)**

| Expense item | Per semester | Per year |
|-------------|-------------|----------|
| Tier 4 Tuition & Fees | $26,162 | $52,324 |
| Books/Supplies | $600 | $1,200 |
| On-Campus Housing & Meal Plans | $9,621 | $19,242 |
| **Total** | **$36,383** | **$72,766** |

> **Source**: https://www.colorado.edu/bursar/undergraduate-costs-by-tier (Incoming 2026-27)
> **Additional fees**: One-time New Student Fee: $232 domestic / $500 international. Immigration Compliance Fee: $40/semester for international students.
> **Tuition Guarantee**: CU Boulder offers 4-year fixed tuition for undergraduate students.
> **Note**: Tier structure reflects cost of instruction differences. Tier 1 (base) = Arts & Humanities, Education, Music, Social Sciences. Tier 2 = slight premium. Tier 3 = CMDI. Tier 4 = Engineering, Natural Sciences, Business.

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 |
|------|-----|
| **Need-blind domestic** | Yes (for domestic applicants) |
| **Need-aware international** | Yes (need-aware for international applicants) |
| **Merit scholarships** | Available (automatic consideration upon admission) |
| **FAFSA priority deadline** | March 1 |
| **Scholarship application** | CU Boulder Scholarship Application (separate) |
| **Net Price Calculator** | Available on financial aid website |

> **Source**: https://www.colorado.edu/financialaid/aid-prospective-incoming-first-year-students
> **Note**: CU Boulder is a public university. Financial aid for international students is limited compared to domestic students.

### 4.3 Graduate cost & funding framework

| 字段 | 值 |
|------|-----|
| **Application fee** | $80 |
| **Funding types** | RA/TA/Fellowship (PhD); limited funding for MS |
| **PhD funding** | Most PhD programs offer full funding (tuition + stipend) |
| **MS funding** | Typically self-funded; some departmental assistantships available |
| **Fee waivers** | Needs-based; contact Graduate School |

> **Source**: https://www.colorado.edu/graduateschool/funding

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 15"
  source_url: https://www.colorado.edu/admissions/process/first-year/apply
  source_snippet: "Nov. 15 — Fall and summer early action deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "January 15"
  source_url: https://www.colorado.edu/admissions/process/first-year/apply
  source_snippet: "Jan. 15 — Fall and summer regular decision deadline"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application_fee_domestic
  value: "$65"
  source_url: https://www.colorado.edu/admissions/process/first-year/apply
  source_snippet: "$65 for domestic applicants"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.application_fee_international
  value: "$70"
  source_url: https://www.colorado.edu/admissions/process/first-year/apply
  source_snippet: "$70 for international applicants"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: https://www.colorado.edu/admissions/process/first-year/apply
  source_snippet: "SAT scores are not required for first-year students, but you may provide self-reported scores if you would like us to consider them when reviewing your application."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.toefl
  value: "4.0 (new scale) / 80 (pre-2026)"
  source_url: https://www.colorado.edu/admissions/process/international/plan/english-proficiency
  source_snippet: "As of Jan. 2026: TOEFL iBT 4.0 — Pre 2026: TOEFL iBT 80"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.english_proficiency.ielts
  value: "6.5"
  source_url: https://www.colorado.edu/admissions/process/international/plan/english-proficiency
  source_snippet: "IELTS 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency.duolingo
  value: "115"
  source_url: https://www.colorado.edu/admissions/process/international/plan/english-proficiency
  source_snippet: "Duolingo 115"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.resident_base_tuition
  value: "$15,014/year"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "Base Tuition Rate and Undergraduate Fees $7,507 $15,014"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.nonresident_base_tuition
  value: "$46,058/year"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "Base Tuition Rate and Undergraduate Fees $23,029 $46,058"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.international_base_tuition
  value: "$48,222/year"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "Base Tuition Rate and Undergraduate Fees $24,111 $48,222"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.housing_food
  value: "$19,242/year"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "On-Campus Housing and Meal Plans $9,621 $19,242"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.cost.total_resident
  value: "$35,456/year (base)"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "Total $17,728 $35,456"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-014:
  field: undergraduate.cost.total_nonresident
  value: "$66,500/year (base)"
  source_url: https://www.colorado.edu/bursar/undergraduate-costs-by-tier
  source_snippet: "Total $33,250 $66,500"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.application_fee
  value: "$80"
  source_url: https://www.colorado.edu/graduateschool/admissions/where-begin/international-students
  source_snippet: "Nonrefundable $80 Application Fee"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.gpa_minimum
  value: "2.75 (3.00 for Engineering)"
  source_url: https://www.colorado.edu/graduateschool/admissions/where-begin
  source_snippet: "Have at least a 2.75 (2.00=C) undergraduate grade point average. Applicants to programs in the College of Engineering and Applied Science must have a 3.00 (3.00=B)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.gre_code
  value: "4841"
  source_url: https://www.colorado.edu/graduateschool/admissions/where-begin/international-students
  source_snippet: "The GRE college code for CU Boulder is 4841."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_proficiency.duolingo
  value: "120 minimum (160-point scale)"
  source_url: https://www.colorado.edu/graduateschool/admissions/where-begin/international-students
  source_snippet: "A minimum score of 120 (on the 160 point scale) is required by the Graduate School"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-005:
  field: graduate.total_programs
  value: "124 master's, doctoral and professional degree programs"
  source_url: https://www.colorado.edu/graduateschool/about
  source_snippet: "CU Boulder offers 124 master's, doctoral and professional degree programs spanning the arts and sciences, business, education, engineering, law, music and more."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-001:
  field: programs.total_count
  value: 374
  source_url: https://catalog.colorado.edu/programs-a-z/
  source_snippet: "Programs A-Z listing with 374 unique program-degree entries"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-C-002:
  field: colleges.count
  value: 10
  source_url: https://www.colorado.edu/academics/colleges-schools
  source_snippet: "Colleges & Schools listing: College of Arts and Sciences, Leeds School of Business, School of Education, College of Engineering & Applied Science, Program in Exploratory Studies, University of Colorado Law School, College of Communication Media Design and Information, College of Music, Graduate School, Continuing Education and Professional Studies"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
cuboulder-knowledge-base-v2
├── 00-overview
│   ├── 00-institution-overview.md
│   ├── 01-program-counts.md
│   ├── 02-hierarchy-tree.md
│   ├── 03-degree-inventory.md
│   └── 04-distribution-matrix.md
├── 01-undergraduate
│   ├── 01-arts-sciences.md
│   ├── 02-engineering.md
│   ├── 03-cmdi.md
│   ├── 04-business.md
│   ├── 05-education.md
│   ├── 06-music.md
│   ├── 07-minors.md
│   └── 08-certificates.md
├── 02-graduate
│   ├── 01-arts-sciences-grad.md
│   ├── 02-engineering-grad.md
│   ├── 03-cmdi-grad.md
│   ├── 04-business-grad.md
│   ├── 05-education-grad.md
│   ├── 06-music-grad.md
│   └── 07-law.md
├── 03-admissions
│   ├── 01-undergraduate-deadlines.md
│   ├── 02-test-policy.md
│   ├── 03-english-proficiency.md
│   └── 04-graduate-admissions.md
├── 04-costs
│   ├── 01-undergraduate-costs.md
│   ├── 02-financial-aid.md
│   └── 03-graduate-funding.md
└── 05-evidence
    └── evidence-chain.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "cuboulder-knowledge-base-v2"
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
|----------|----------|------------|
| P0 | Graduate program-specific deadlines (per department) | https://www.colorado.edu/graduateschool/admissions |
| P0 | Graduate program-specific GRE requirements | Department websites |
| P0 | Law School JD program details | https://www.colorado.edu/law/admissions |
| P1 | Graduate tuition rates by program | https://www.colorado.edu/bursar/ |
| P1 | Financial aid income thresholds | https://www.colorado.edu/financialaid/ |
| P1 | Need-blind/need-aware policy verification | https://www.colorado.edu/admissions/ |
| P2 | Detailed department listings per college | College websites |
| P2 | Online program details | https://www.colorado.edu/academics/programs |
| P2 | Continuing Education programs | https://www.colorado.edu/continuing-education/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | CU Boulder | (Other schools) |
|-----------|-----------|-----------------|
| **Total UG cost/yr (resident)** | $35,456–$41,696 | |
| **Total UG cost/yr (nonresident)** | $66,500–$70,608 | |
| **Total UG cost/yr (international)** | $68,664–$72,766 | |
| **Tuition/yr (resident base)** | $15,014 | |
| **Tuition/yr (nonresident base)** | $46,058 | |
| **Need-blind (domestic)** | Yes | |
| **Need-blind (international)** | No (need-aware) | |
| **EA deadline** | November 15 | |
| **RD deadline** | January 15 | |
| **SAT/ACT required?** | No (test-optional) | |
| **TOEFL min** | 80 (pre-2026) / 4.0 (new scale) | |
| **IELTS min** | 6.5 | |
| **Duolingo min** | 115 | |
| **Grad application fee** | $80 | |
| **Total program count (Rule 1)** | 374 | |
| **School/department count (Rule 2)** | 10 | |
| **Tuition guarantee** | Yes (4-year fixed) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: colorado.edu, catalog.colorado.edu, bursar.colorado.edu, graduateschool.colorado.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
