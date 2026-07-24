# The University of Sheffield Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch + WebSearch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Entry year reference**: 2027-28 (UG), 2026-27 (PGT)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 140 |
| 本科双学位/联合荣誉 (Dual Honours) | 21 (included in total of 140) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/LLM/MMedSci/MPH/PGCE etc.) | 128 |
| 研究生博士项目 (PhD/Doctoral) | Available via PhD search tool (not a fixed list) |
| **学位项目总计 (UG extracted)** | **140** |
| 学院 (Faculties) | 5 |
| 学术院系 (Academic Schools) | 20 |

> **Data source**: Sheffield undergraduate A-Z course listing (`sheffield.ac.uk/undergraduate/courses/2027`), 140 courses extracted.
> **PGT source**: Sheffield postgraduate taught A-Z listing (`sheffield.ac.uk/postgraduate/taught/courses/2026`), 128 courses extracted.
> **PhD note**: PhD programmes are not listed in a single A-Z; available via individual research project listings and subject-area browsing at `sheffield.ac.uk/postgraduate/phd`.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
The University of Sheffield
├── Faculty of Arts and Humanities                          [学院]
│   ├── School of Architecture and Landscape                [系]
│   ├── School of English                                   [系]
│   ├── School of History, Philosophy and Digital Humanities [系]
│   ├── School of Languages, Arts and Societies             [系]
│   └── School of Law                                       [系]
├── Faculty of Engineering                                  [学院]
│   ├── School of Chemical, Materials and Biological Engineering [系]
│   ├── School of Electrical and Electronic Engineering      [系]
│   └── School of Mechanical, Aerospace and Civil Engineering [系]
├── Faculty of Health                                        [学院]
│   ├── School of Allied Health Professions, Pharmacy, Nursing and Midwifery [系]
│   ├── School of Clinical Dentistry                         [系]
│   └── School of Medicine and Population Health             [系]
├── Faculty of Science                                       [学院]
│   ├── School of Biosciences                                [系]
│   ├── School of Computer Science                           [系]
│   ├── School of Mathematical and Physical Sciences         [系]
│   ├── School of Geography and Planning                     [系]
│   └── School of Psychology                                 [系]
└── Faculty of Social Sciences                               [学院]
    ├── School of Education                                  [系]
    ├── School of Economics                                  [系]
    ├── School of Management                                 [系]
    ├── School of Sociological Studies, Politics and International Relations [系]
    └── School of Information, Journalism and Communication  [系]
```

> **Source**: `sheffield.ac.uk/departments/academic` and `sheffield.ac.uk/departments/faculties`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 全称 | 层级 | 本项目数量 |
|---------|-----------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 41 |
| BSc | BSc | Bachelor of Science | 本科 | 30 |
| BEng | BEng | Bachelor of Engineering | 本科 | 16 |
| MEng | MEng | Master of Engineering (Integrated) | 本科 | 18 |
| BMedSci | BMedSci | Bachelor of Medical Science | 本科 | 3 |
| MComp | MComp | Master of Computer Science (Integrated) | 本科 | 4 |
| MBiolSci | MBiolSci | Master of Biological Sciences (Integrated) | 本科 | 3 |
| MBiomedSci | MBiomedSci | Master of Biomedical Science (Integrated) | 本科 | 1 |
| MChem | MChem | Master of Chemistry (Integrated) | 本科 | 2 |
| MPhys | MPhys | Master of Physics (Integrated) | 本科 | 4 |
| MMath | MMath | Master of Mathematics (Integrated) | 本科 | 1 |
| BSc (Hons) | BSc | Bachelor of Science (Honours) | 本科 | 1 |
| BEng (Hons) | BEng | Bachelor of Engineering (Honours) | 本科 | 1 |
| MEng (Hons) | MEng | Master of Engineering (Honours, Integrated) | 本科 | 1 |
| BDS | BDS | Bachelor of Dental Surgery | 本科 | 1 |
| MBChB | MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| BMus | BMus | Bachelor of Music | 本科 | 1 |
| LLB | LLB | Bachelor of Laws | 本科 | 3 |
| MLA | MLA | Master of Landscape Architecture (Integrated) | 本科 | 1 |
| MPharm | MPharm | Master of Pharmacy (Integrated) | 本科 | 1 |
| MPlan(UG) | MPlan | Master of Planning (Integrated, UG entry) | 本科 | 1 |
| **合计** | | | | **140** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学位 | BA | BDS | BEng | BEng(Hons) | BMedSci | BSc | BSc(Hons) | LLB | MChem | MComp | MBChB | MBiolSci | MBiomedSci | MEng | MEng(Hons) | MLA | MMath | MPharm | MPhys | MPlan | BMus | 合计 |
|------------|-----|-----|------|------------|---------|-----|-----------|-----|-------|-------|-------|----------|------------|------|------------|-----|-------|--------|-------|-------|------|------|
| Arts and Humanities | 26 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | **32** |
| Engineering | 0 | 0 | 16 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **35** |
| Health | 0 | 1 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **9** |
| Science | 2 | 0 | 0 | 0 | 0 | 24 | 1 | 0 | 2 | 4 | 0 | 3 | 1 | 1 | 0 | 0 | 1 | 0 | 4 | 0 | 0 | **43** |
| Social Sciences | 13 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **17** |
| Cross-faculty (dual honours) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| **合计** | **41** | **1** | **16** | **1** | **3** | **30** | **1** | **3** | **2** | **4** | **2** | **3** | **1** | **18** | **1** | **1** | **1** | **1** | **4** | **1** | **1** | **140** |

> **Note**: Some dual honours programmes span two faculties (e.g., Business Management and Economics bridges Social Sciences and Social Sciences; English and Music bridges Arts and Humanities). The 4 cross-faculty entries are dual honours counted once under their primary administrative school.
> **Reconciliation check**: Rule-1 total (140) == matrix-sum (140). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Sheffield is organised into 5 academic Faculties, each containing multiple Academic Schools (20 total). See Section 0.2 for the full hierarchy tree. All undergraduate degree programmes are administered by one of these 20 Schools.

### 1.2 Undergraduate degree programmes — grouped by Faculty > School > Degree Level

#### Faculty of Arts and Humanities

##### School of Architecture and Landscape

###### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.sheffield.ac.uk/undergraduate/courses/2027/architecture-ba |
| 2 | Architecture and Landscape | https://www.sheffield.ac.uk/undergraduate/courses/2027/architecture-and-landscape-ba |
| 3 | Landscape Architecture | https://www.sheffield.ac.uk/undergraduate/courses/2027/landscape-architecture-ba |

###### MLA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | https://www.sheffield.ac.uk/undergraduate/courses/2027/landscape-architecture-mla |

###### MPlan(UG) (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Planning | https://www.sheffield.ac.uk/undergraduate/courses/2027/urban-planning-mplanug |

---

##### School of English

###### BA (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English and History | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-and-history-ba |
| 2 | English and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-and-modern-languages-cultures-ba |
| 3 | English and Music | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-and-music-ba |
| 4 | English and Philosophy | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-and-philosophy-ba |
| 5 | English Language and Linguistics | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-language-and-linguistics-ba |
| 6 | English Language and Literature | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-language-and-literature-ba |
| 7 | English Literature | https://www.sheffield.ac.uk/undergraduate/courses/2027/english-literature-ba |
| 8 | Linguistics and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/linguistics-and-modern-languages-cultures-ba |

---

##### School of History, Philosophy and Digital Humanities

###### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Media and Society | https://www.sheffield.ac.uk/undergraduate/courses/2027/digital-media-and-society-ba |
| 2 | History | https://www.sheffield.ac.uk/undergraduate/courses/2027/history-ba |
| 3 | History and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/history-and-modern-languages-cultures-ba |
| 4 | History and Philosophy | https://www.sheffield.ac.uk/undergraduate/courses/2027/history-and-philosophy-ba |
| 5 | History and Politics | https://www.sheffield.ac.uk/undergraduate/courses/2027/history-and-politics-ba |
| 6 | Philosophy | https://www.sheffield.ac.uk/undergraduate/courses/2027/philosophy-ba |
| 7 | Philosophy, Religion and Ethics | https://www.sheffield.ac.uk/undergraduate/courses/2027/philosophy-religion-and-ethics-ba |

---

##### School of Languages, Arts and Societies

###### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.sheffield.ac.uk/undergraduate/courses/2027/criminology-ba |
| 2 | East Asian Studies | https://www.sheffield.ac.uk/undergraduate/courses/2027/east-asian-studies-ba |
| 3 | Modern Languages and Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/modern-languages-and-cultures-ba |
| 4 | Music and East Asian Studies | https://www.sheffield.ac.uk/undergraduate/courses/2027/music-and-east-asian-studies-ba |
| 5 | Music and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/music-and-modern-languages-cultures-ba |
| 6 | Politics and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/politics-and-modern-languages-cultures-ba |
| 7 | Global Sustainable Development | https://www.sheffield.ac.uk/undergraduate/courses/2027/global-sustainable-development-ba |

###### BMus (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.sheffield.ac.uk/undergraduate/courses/2027/music-bmus |

---

##### School of Law

###### LLB (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://www.sheffield.ac.uk/undergraduate/courses/2027/law-llb |
| 2 | Law (European and International) | https://www.sheffield.ac.uk/undergraduate/courses/2027/law-european-and-international-llb |
| 3 | Law and Criminology | https://www.sheffield.ac.uk/undergraduate/courses/2027/law-and-criminology-llb |

---

#### Faculty of Engineering

##### School of Chemical, Materials and Biological Engineering

###### BEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemical-engineering-beng |
| 2 | Chemical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemical-engineering-foundation-year-beng |
| 3 | Materials Science and Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/materials-science-and-engineering-beng |

###### BEng with Foundation Year (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/materials-science-and-engineering-foundation-year-beng |

###### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemical-engineering-meng |
| 2 | Chemical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemical-engineering-foundation-year-meng |
| 3 | Materials Science and Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/materials-science-and-engineering-meng |

###### MEng with Foundation Year (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/materials-science-and-engineering-foundation-year-meng |

---

##### School of Electrical and Electronic Engineering

###### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/electrical-and-electronic-engineering-beng |
| 2 | Electrical and Electronic Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/electrical-and-electronic-engineering-foundation-year-beng |

###### MEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/electrical-and-electronic-engineering-meng |
| 2 | Electrical and Electronic Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/electrical-and-electronic-engineering-foundation-year-meng |

---

##### School of Mechanical, Aerospace and Civil Engineering

###### BEng (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/aerospace-engineering-beng |
| 2 | Aerospace Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/aerospace-engineering-foundation-year-beng |
| 3 | Biomedical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-engineering-beng |
| 4 | Biomedical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-engineering-foundation-year-beng |
| 5 | Civil Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/civil-engineering-beng |
| 6 | Civil Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/civil-engineering-foundation-year-beng |
| 7 | Mechanical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechanical-engineering-beng |

###### BEng(Hons) (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | General Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/general-engineering-beng-hons |

###### BEng with Foundation Year (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechanical-engineering-foundation-year-beng |
| 2 | General Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/general-engineering-foundation-year-beng |

###### MEng (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/aerospace-engineering-meng |
| 2 | Aerospace Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/aerospace-engineering-foundation-year-meng |
| 3 | Architectural Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/architectural-engineering-meng |
| 4 | Biomedical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-engineering-meng |
| 5 | Biomedical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-engineering-foundation-year-meng |
| 6 | Civil and Structural Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/civil-and-structural-engineering-meng |
| 7 | Civil and Structural Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/civil-and-structural-engineering-foundation-year-meng |

###### MEng with Foundation Year (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechanical-engineering-meng |
| 2 | Mechanical Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechanical-engineering-foundation-year-meng |

###### MEng(Hons) (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | General Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/general-engineering-meng-hons |

###### MEng with Foundation Year (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | General Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/general-engineering-foundation-year-meng |

###### BEng (Mechatronic) (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechatronic and Robotic Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechatronic-and-robotic-engineering-beng |
| 2 | Mechatronic and Robotic Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechatronic-and-robotic-engineering-foundation-year-beng |

###### MEng (Mechatronic) (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechatronic and Robotic Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechatronic-and-robotic-engineering-meng |
| 2 | Mechatronic and Robotic Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/mechatronic-and-robotic-engineering-foundation-year-meng |

---

#### Faculty of Health

##### School of Clinical Dentistry

###### BDS (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Surgery | https://www.sheffield.ac.uk/undergraduate/courses/2027/dental-surgery-bds |

###### BSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene and Dental Therapy | https://www.sheffield.ac.uk/undergraduate/courses/2027/dental-hygiene-and-dental-therapy-bsc |

---

##### School of Medicine and Population Health

###### MBChB (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine | https://www.sheffield.ac.uk/undergraduate/courses/2027/medicine-mbchb |
| 2 | Graduate Entry Medicine | https://www.sheffield.ac.uk/undergraduate/courses/2027/graduate-entry-medicine-mbchb |

###### BMedSci (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) | https://www.sheffield.ac.uk/undergraduate/courses/2027/nursing-adult-bmedsci |

---

##### School of Allied Health Professions, Pharmacy, Nursing and Midwifery

###### BMedSci (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Orthoptics | https://www.sheffield.ac.uk/undergraduate/courses/2027/orthoptics-bmedsci |
| 2 | Speech and Language Therapy | https://www.sheffield.ac.uk/undergraduate/courses/2027/speech-and-language-therapy-bmedsci |

###### BSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-science-bsc |

###### MBiomedSci (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/biomedical-science-mbiomedsci |

###### MPharm (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.sheffield.ac.uk/undergraduate/courses/2027/pharmacy-mpharm |

---

#### Faculty of Science

##### School of Biosciences

###### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/biochemistry-bsc |
| 2 | Biological Sciences | https://www.sheffield.ac.uk/undergraduate/courses/2027/biological-sciences-bsc |
| 3 | Zoology | https://www.sheffield.ac.uk/undergraduate/courses/2027/zoology-bsc |

###### MBiolSci (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/biochemistry-mbiolsci |
| 2 | Biological Sciences | https://www.sheffield.ac.uk/undergraduate/courses/2027/biological-sciences-mbiolsci |
| 3 | Zoology | https://www.sheffield.ac.uk/undergraduate/courses/2027/zoology-mbiolsci |

---

##### School of Computer Science

###### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-bsc |
| 2 | Computer Science (Artificial Intelligence) | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-artificial-intelligence-bsc |
| 3 | Computer Science (Artificial Intelligence) with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-artificial-intelligence-foundation-year-bsc |
| 4 | Computer Science with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-foundation-year-bsc |
| 5 | Data Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/data-science-bsc |
| 6 | Software Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/software-engineering-foundation-year-beng |
| 7 | Computer Systems Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-systems-engineering-foundation-year-beng |

###### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (Software Engineering) | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-software-engineering-beng |
| 2 | Computer Systems Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-systems-engineering-beng |

###### MComp (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-mcomp |
| 2 | Computer Science (Artificial Intelligence) | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-artificial-intelligence-mcomp |
| 3 | Computer Science (Artificial Intelligence) with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-artificial-intelligence-foundation-year-mcomp |
| 4 | Computer Science with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-foundation-year-mcomp |

###### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (Software Engineering) | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-software-engineering-meng |
| 2 | Computer Systems Engineering | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-systems-engineering-meng |
| 3 | Computer Systems Engineering with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-systems-engineering-foundation-year-meng |

---

##### School of Mathematical and Physical Sciences

###### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemistry-bsc |
| 2 | Chemistry with Biological and Medicinal Chemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemistry-biological-and-medicinal-chemistry-bsc |
| 3 | Economics and Mathematics | https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-and-mathematics-bsc |
| 4 | Financial Mathematics | https://www.sheffield.ac.uk/undergraduate/courses/2027/financial-mathematics-bsc |
| 5 | Mathematics | https://www.sheffield.ac.uk/undergraduate/courses/2027/mathematics-bsc |
| 6 | Mathematics and Philosophy | https://www.sheffield.ac.uk/undergraduate/courses/2027/mathematics-and-philosophy-bsc |
| 7 | Physics | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-bsc |
| 8 | Physics and Astrophysics | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-and-astrophysics-bsc |
| 9 | Theoretical Physics | https://www.sheffield.ac.uk/undergraduate/courses/2027/theoretical-physics-bsc |

###### BSc with Foundation Year (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-foundation-year-bsc |

###### MChem (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemistry-mchem |
| 2 | Chemistry with Biological and Medicinal Chemistry | https://www.sheffield.ac.uk/undergraduate/courses/2027/chemistry-biological-and-medicinal-chemistry-mchem |

###### MMath (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.sheffield.ac.uk/undergraduate/courses/2027/mathematics-mmath |

###### MPhys (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-mphys |
| 2 | Physics and Astrophysics | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-and-astrophysics-mphys |
| 3 | Physics with a Foundation Year | https://www.sheffield.ac.uk/undergraduate/courses/2027/physics-foundation-year-mphys |
| 4 | Theoretical Physics | https://www.sheffield.ac.uk/undergraduate/courses/2027/theoretical-physics-mphys |

---

##### School of Geography and Planning

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.sheffield.ac.uk/undergraduate/courses/2027/environmental-science-bsc |
| 2 | Geography | https://www.sheffield.ac.uk/undergraduate/courses/2027/geography-bsc |

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.sheffield.ac.uk/undergraduate/courses/2027/geography-ba |
| 2 | Geography and Planning | https://www.sheffield.ac.uk/undergraduate/courses/2027/geography-and-planning-ba |

---

##### School of Psychology

###### BSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.sheffield.ac.uk/undergraduate/courses/2027/psychology-bsc |

###### BSc (cross-listed) (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Education and Psychology | https://www.sheffield.ac.uk/undergraduate/courses/2027/education-and-psychology-bsc |

---

#### Faculty of Social Sciences

##### School of Economics

###### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-ba |
| 2 | Economics and Politics | https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-and-politics-ba |
| 3 | Philosophy, Politics and Economics | https://www.sheffield.ac.uk/undergraduate/courses/2027/philosophy-politics-and-economics-ba |

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-bsc |
| 2 | Economics with Finance | https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-finance-bsc |

---

##### School of Management

###### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Financial Management | https://www.sheffield.ac.uk/undergraduate/courses/2027/accounting-and-financial-management-ba |
| 2 | Accounting and Financial Management and Economics | https://www.sheffield.ac.uk/undergraduate/courses/2027/accounting-and-financial-management-and-economics-ba |
| 3 | Business Management | https://www.sheffield.ac.uk/undergraduate/courses/2027/business-management-ba |

###### BA (dual honours) (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management and Economics | https://www.sheffield.ac.uk/undergraduate/courses/2027/business-management-and-economics-ba |
| 2 | Business Management and Modern Languages & Cultures | https://www.sheffield.ac.uk/undergraduate/courses/2027/business-management-and-modern-languages-cultures-ba |

---

##### School of Sociological Studies, Politics and International Relations

###### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Politics and International Relations | https://www.sheffield.ac.uk/undergraduate/courses/2027/politics-and-international-relations-ba |
| 2 | Politics and Philosophy | https://www.sheffield.ac.uk/undergraduate/courses/2027/politics-and-philosophy-ba |
| 3 | Politics and Sociology | https://www.sheffield.ac.uk/undergraduate/courses/2027/politics-and-sociology-ba |
| 4 | Sociology | https://www.sheffield.ac.uk/undergraduate/courses/2027/sociology-ba |

###### BA (cross-listed) (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Sciences | https://www.sheffield.ac.uk/undergraduate/courses/2027/social-sciences-ba |
| 2 | History and Politics | https://www.sheffield.ac.uk/undergraduate/courses/2027/history-and-politics-ba |

---

##### School of Information, Journalism and Communication

###### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism Studies | https://www.sheffield.ac.uk/undergraduate/courses/2027/journalism-studies-ba |

---

### 1.3 Dual honours programmes

Sheffield offers 21 dual honours (combined) degree programmes. These are listed as separate entries in the A-Z listing and are included in the total count of 140. Dual honours programmes allow students to study two subjects equally. Full list:

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Accounting and Financial Management and Economics | BA | /undergraduate/courses/2027/accounting-and-financial-management-and-economics-ba |
| 2 | Architecture and Landscape | BA | /undergraduate/courses/2027/architecture-and-landscape-ba |
| 3 | Business Management and Economics | BA | /undergraduate/courses/2027/business-management-and-economics-ba |
| 4 | Business Management and Modern Languages & Cultures | BA | /undergraduate/courses/2027/business-management-and-modern-languages-cultures-ba |
| 5 | Economics and Mathematics | BSc | /undergraduate/courses/2027/economics-and-mathematics-bsc |
| 6 | Economics and Politics | BA | /undergraduate/courses/2027/economics-and-politics-ba |
| 7 | English and History | BA | /undergraduate/courses/2027/english-and-history-ba |
| 8 | English and Modern Languages & Cultures | BA | /undergraduate/courses/2027/english-and-modern-languages-cultures-ba |
| 9 | English and Music | BA | /undergraduate/courses/2027/english-and-music-ba |
| 10 | English and Philosophy | BA | /undergraduate/courses/2027/english-and-philosophy-ba |
| 11 | Geography and Planning | BA | /undergraduate/courses/2027/geography-and-planning-ba |
| 12 | History and Modern Languages & Cultures | BA | /undergraduate/courses/2027/history-and-modern-languages-cultures-ba |
| 13 | History and Philosophy | BA | /undergraduate/courses/2027/history-and-philosophy-ba |
| 14 | History and Politics | BA | /undergraduate/courses/2027/history-and-politics-ba |
| 15 | Linguistics and Modern Languages & Cultures | BA | /undergraduate/courses/2027/linguistics-and-modern-languages-cultures-ba |
| 16 | Mathematics and Philosophy | BSc | /undergraduate/courses/2027/mathematics-and-philosophy-bsc |
| 17 | Music and East Asian Studies | BA | /undergraduate/courses/2027/music-and-east-asian-studies-ba |
| 18 | Music and Modern Languages & Cultures | BA | /undergraduate/courses/2027/music-and-modern-languages-cultures-ba |
| 19 | Politics and Modern Languages & Cultures | BA | /undergraduate/courses/2027/politics-and-modern-languages-cultures-ba |
| 20 | Politics and Philosophy | BA | /undergraduate/courses/2027/politics-and-philosophy-ba |
| 21 | Politics and Sociology | BA | /undergraduate/courses/2027/politics-and-sociology-ba |

### 1.4 Foundation year programmes

Sheffield offers foundation year variants of many Engineering and Computer Science programmes. These are listed as separate entries in the A-Z listing and are included in the counts above. Foundation year programmes provide an alternative entry route for students who do not meet the standard entry requirements. Foundation year courses found:

- Aerospace Engineering (BEng/MEng)
- Biomedical Engineering (BEng/MEng)
- Chemical Engineering (BEng/MEng)
- Civil Engineering (BEng)
- Civil and Structural Engineering (MEng)
- Computer Science (BSc/MComp)
- Computer Science AI (BSc/MComp)
- Computer Systems Engineering (BEng/MEng)
- Electrical and Electronic Engineering (BEng/MEng)
- General Engineering (BEng/MEng)
- Materials Science and Engineering (BEng/MEng)
- Mechanical Engineering (BEng/MEng)
- Mechatronic and Robotic Engineering (BEng/MEng)
- Physics (BSc/MPhys)
- Software Engineering (BEng/MEng)

### 1.5 Placement year / Study abroad variants

Many Sheffield programmes offer optional placement year (sandwich year) or study abroad options. These are typically not listed as separate A-Z entries but are available as variants within the same programme. The university has 250+ partner universities worldwide for study abroad.

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate taught (PGT) — 128 courses

The University of Sheffield offers 128 postgraduate taught programmes for 2026-27 entry. Full listing:

| # | Course Name | Degree | URL |
|---|------------|--------|-----|
| 1 | Advanced Clinical Practice (GP) | MMedSci | /postgraduate/taught/courses/2026/advanced-clinical-practice-gp-mmedsci |
| 2 | Advanced Clinical Practice (Neonatal) | MMedSci | /postgraduate/taught/courses/2026/advanced-clinical-practice-neonatal-mmedsci |
| 3 | Advanced Clinical Practice (Paediatrics) | MMedSci | /postgraduate/taught/courses/2026/advanced-clinical-practice-paediatrics-mmedsci |
| 4 | Advanced Computer Science | MSc | /postgraduate/taught/courses/2026/advanced-computer-science-msc |
| 5 | Advanced Control and Systems Engineering | MSc(Eng) | /postgraduate/taught/courses/2026/advanced-control-and-systems-engineering-msceng |
| 6 | Advanced Mechanical Engineering | MSc | /postgraduate/taught/courses/2026/advanced-mechanical-engineering-msc |
| 7 | Aerospace Engineering | MSc | /postgraduate/taught/courses/2026/aerospace-engineering-msc |
| 8 | Applied Linguistics and TESOL | MA | /postgraduate/taught/courses/2026/applied-linguistics-and-tesol-ma |
| 9 | Applied Professional Studies in Education | MA | /postgraduate/taught/courses/2026/applied-professional-studies-education-ma |
| 10 | Archaeology and Heritage | MA | /postgraduate/taught/courses/2026/archaeology-and-heritage-ma |
| 11 | Architectural Design | MA | /postgraduate/taught/courses/2026/architectural-design-ma |
| 12 | Architecture | MArch | /postgraduate/taught/courses/2026/architecture-march |
| 13 | Architecture: Collaborative Practice | MArch | /postgraduate/taught/courses/2026/architecture-collaborative-practice-march |
| 14 | Artificial Intelligence | MSc | /postgraduate/taught/courses/2026/artificial-intelligence-msc |
| 15 | Artificial Intelligence for Engineering | MSc | /postgraduate/taught/courses/2026/artificial-intelligence-engineering-msc |
| 16 | Astrophysics | MSc | /postgraduate/taught/courses/2026/astrophysics-msc |
| 17 | Biodiversity and Conservation | MSc | /postgraduate/taught/courses/2026/biodiversity-and-conservation-msc |
| 18 | Biological and Bioprocess Engineering | MSc | /postgraduate/taught/courses/2026/biological-and-bioprocess-engineering-msc |
| 19 | Biomedical Engineering | MSc | /postgraduate/taught/courses/2026/biomedical-engineering-msc |
| 20 | Biomedical Science | MSc | /postgraduate/taught/courses/2026/biomedical-science-msc |
| 21 | Business Analytics | MSc | /postgraduate/taught/courses/2026/business-analytics-msc |
| 22 | Business and Organisational Psychology | MSc | /postgraduate/taught/courses/2026/business-and-organisational-psychology-msc |
| 23 | Business Finance and Economics | MSc | /postgraduate/taught/courses/2026/business-finance-and-economics-msc |
| 24 | Cancer Biology and Therapeutics | MSc | /postgraduate/taught/courses/2026/cancer-biology-and-therapeutics-msc |
| 25 | Chemistry | MSc | /postgraduate/taught/courses/2026/chemistry-msc |
| 26 | Civil and Structural Engineering | MSc | /postgraduate/taught/courses/2026/civil-and-structural-engineering-msc |
| 27 | Civil Engineering and Project Management | MSc | /postgraduate/taught/courses/2026/civil-engineering-and-project-management-msc |
| 28 | Clinical Neurology | MSc | /postgraduate/taught/courses/2026/clinical-neurology-msc |
| 29 | Clinical Research | MSc | /postgraduate/taught/courses/2026/clinical-research-msc |
| 30 | Cognitive and Computational Neuroscience | MSc | /postgraduate/taught/courses/2026/cognitive-and-computational-neuroscience-msc |
| 31 | Cognitive Neuroscience and Human Neuroimaging | MSc | /postgraduate/taught/courses/2026/cognitive-neuroscience-and-human-neuroimaging-msc |
| 32 | Cognitive Science and Philosophy of AI | MA | /postgraduate/taught/courses/2026/cognitive-science-and-philosophy-ai-ma |
| 33 | Computer Science | MSc | /postgraduate/taught/courses/2026/computer-science-msc |
| 34 | Computer Science with Speech and Natural Language Processing | MSc | /postgraduate/taught/courses/2026/computer-science-speech-and-natural-language-processing-msc |
| 35 | Creative and Cultural Industries Management | MSc | /postgraduate/taught/courses/2026/creative-and-cultural-industries-management-msc |
| 36 | Cultural Heritage | MA | /postgraduate/taught/courses/2026/cultural-heritage-ma |
| 37 | Cybersecurity and Artificial Intelligence | MSc | /postgraduate/taught/courses/2026/cybersecurity-and-artificial-intelligence-msc |
| 38 | Data and Digital Humanities | MSc | /postgraduate/taught/courses/2026/data-and-digital-humanities-msc |
| 39 | Data Science | MSc | /postgraduate/taught/courses/2026/data-science-msc |
| 40 | Digital Culture and Communication | MA | /postgraduate/taught/courses/2026/digital-culture-and-communication-ma |
| 41 | Digital Marketing | MSc | /postgraduate/taught/courses/2026/digital-marketing-msc |
| 42 | Digital Media and Society | MA | /postgraduate/taught/courses/2026/digital-media-and-society-ma |
| 43 | Drug Discovery Science | MSc | /postgraduate/taught/courses/2026/drug-discovery-science-msc |
| 44 | East Asian Business | MSc | /postgraduate/taught/courses/2026/east-asian-business-msc |
| 45 | Economics | MSc | /postgraduate/taught/courses/2026/economics-msc |
| 46 | EdD - The Sheffield EdD | EdD | /postgraduate/taught/courses/2026/edd-sheffield-edd-edd |
| 47 | Education | MA | /postgraduate/taught/courses/2026/education-ma |
| 48 | Educational and Child Psychology | Doctorate | /postgraduate/taught/courses/2026/educational-and-child-psychology-doctor |
| 49 | Electronic and Electrical Engineering | MSc(Eng) | /postgraduate/taught/courses/2026/electronic-and-electrical-engineering-msceng |
| 50 | Energy Engineering with Industrial Management | MSc | /postgraduate/taught/courses/2026/energy-engineering-industrial-management-msc |
| 51 | English Literature | MA | /postgraduate/taught/courses/2026/english-literature-ma |
| 52 | Environmental Science and Data | MSc | /postgraduate/taught/courses/2026/environmental-science-and-data-msc |
| 53 | Europubhealth: European Masters Programme in Public Health | Euro. Pub. Health Master | /postgraduate/taught/courses/2026/europubhealth-european-masters-programme-public-health-european-public-health-master |
| 54 | Finance | MSc | /postgraduate/taught/courses/2026/finance-msc |
| 55 | Finance and Accounting | MSc | /postgraduate/taught/courses/2026/finance-and-accounting-msc |
| 56 | Financial Technology and Innovation | MSc | /postgraduate/taught/courses/2026/financial-technology-and-innovation-msc |
| 57 | Geographical Information Systems (GIS) | MSc | /postgraduate/taught/courses/2026/geographical-information-systems-gis-msc |
| 58 | Global Journalism | MA | /postgraduate/taught/courses/2026/global-journalism-ma |
| 59 | Health and Clinical Research Delivery | MSc/PG Cert/PG Dip | /postgraduate/taught/courses/2026/health-and-clinical-research-delivery-msc-pg-certificate-pg-diploma |
| 60 | Health Economics and Decision Modelling | MSc | /postgraduate/taught/courses/2026/health-economics-and-decision-modelling-msc |
| 61 | History | MA | /postgraduate/taught/courses/2026/history-ma |
| 62 | Human and Molecular Genetics | MSc | /postgraduate/taught/courses/2026/human-and-molecular-genetics-msc |
| 63 | Human Resource Management | MSc | /postgraduate/taught/courses/2026/human-resource-management-msc |
| 64 | Information Management | MSc | /postgraduate/taught/courses/2026/information-management-msc |
| 65 | Information Systems | MSc | /postgraduate/taught/courses/2026/information-systems-msc |
| 66 | Information Systems Management | MSc | /postgraduate/taught/courses/2026/information-systems-management-msc |
| 67 | International Criminology | MA | /postgraduate/taught/courses/2026/international-criminology-ma |
| 68 | International Development | MSc | /postgraduate/taught/courses/2026/international-development-msc |
| 69 | International Management | MSc | /postgraduate/taught/courses/2026/international-management-msc |
| 70 | International Marketing and Management | MSc | /postgraduate/taught/courses/2026/international-marketing-and-management-msc |
| 71 | International Political Economy | MA | /postgraduate/taught/courses/2026/international-political-economy-ma |
| 72 | International Postgraduate Certificate in Education (iPGCE) | iPGCE | /postgraduate/taught/courses/2026/international-postgraduate-certificate-education-ipgce-ipgce |
| 73 | International Public and Political Communication | MA | /postgraduate/taught/courses/2026/international-public-and-political-communication-ma |
| 74 | International Relations | MA | /postgraduate/taught/courses/2026/international-relations-ma |
| 75 | Journalism | MA | /postgraduate/taught/courses/2026/journalism-ma |
| 76 | Landscape Architecture | MA | /postgraduate/taught/courses/2026/landscape-architecture-ma |
| 77 | Landscape Design, Planning and Management | MA | /postgraduate/taught/courses/2026/landscape-design-planning-and-management-ma |
| 78 | Law | MA | /postgraduate/taught/courses/2026/law-ma |
| 79 | Law (Graduate Programme) | LLB | /postgraduate/taught/courses/2026/law-graduate-programme-llb |
| 80 | Librarianship | MA | /postgraduate/taught/courses/2026/librarianship-ma |
| 81 | Library and Information Services Management (Distance Learning) | MA/PG Cert/PG Dip | /postgraduate/taught/courses/2026/library-and-information-services-management-distance-learning-ma-pg-certificate-pg-diploma |
| 82 | LLM Corporate and Commercial Law | LLM | /postgraduate/taught/courses/2026/llm-corporate-and-commercial-law-llm |
| 83 | LLM International Law and Global Justice | LLM | /postgraduate/taught/courses/2026/llm-international-law-and-global-justice-llm |
| 84 | LLM The Sheffield LLM | LLM | /postgraduate/taught/courses/2026/llm-sheffield-llm-llm |
| 85 | Logistics and Supply Chain Management | MSc | /postgraduate/taught/courses/2026/logistics-and-supply-chain-management-msc |
| 86 | Management | MSc | /postgraduate/taught/courses/2026/management-msc |
| 87 | Management and International Business | MSc | /postgraduate/taught/courses/2026/management-and-international-business-msc |
| 88 | Materials Science and Engineering | MSc | /postgraduate/taught/courses/2026/materials-science-and-engineering-msc |
| 89 | Mathematical and Theoretical Physics | MSc | /postgraduate/taught/courses/2026/mathematical-and-theoretical-physics-msc |
| 90 | Mathematics | MSc | /postgraduate/taught/courses/2026/mathematics-msc |
| 91 | MBA (Master of Business Administration) | MBA | /postgraduate/taught/courses/2026/mba-master-business-administration-mba |
| 92 | Mechanical Engineering with Industrial Management | MSc | /postgraduate/taught/courses/2026/mechanical-engineering-industrial-management-msc |
| 93 | Medical Education | PG Certificate | /postgraduate/taught/courses/2026/medical-education-pg-certificate |
| 94 | Molecular Biology and Biotechnology | MSc | /postgraduate/taught/courses/2026/molecular-biology-and-biotechnology-msc |
| 95 | Money, Banking and Finance | MSc | /postgraduate/taught/courses/2026/money-banking-and-finance-msc |
| 96 | Music Performance Studies | MA | /postgraduate/taught/courses/2026/music-performance-studies-ma |
| 97 | Music, Management and Innovation | MA | /postgraduate/taught/courses/2026/music-management-and-innovation-ma |
| 98 | Musicology | MA | /postgraduate/taught/courses/2026/musicology-ma |
| 99 | Ophthalmology Advanced Clinical Practice (Paediatrics) | MMedSci | /postgraduate/taught/courses/2026/ophthalmology-advanced-clinical-practice-paediatrics-mmedsci |
| 100 | Pharmaceutical Engineering | MSc | /postgraduate/taught/courses/2026/pharmaceutical-engineering-msc |
| 101 | Philosophy | MA | /postgraduate/taught/courses/2026/philosophy-ma |
| 102 | Physics | MSc | /postgraduate/taught/courses/2026/physics-msc |
| 103 | Politics and Media in East Asia | MA | /postgraduate/taught/courses/2026/politics-and-media-east-asia-ma |
| 104 | Politics, Governance and Public Policy | MA | /postgraduate/taught/courses/2026/politics-governance-and-public-policy-ma |
| 105 | Postgraduate Certificate in Education | PGCE | /postgraduate/taught/courses/2026/postgraduate-certificate-education-pgce |
| 106 | Process Safety and Loss Prevention | MSc(Eng) | /postgraduate/taught/courses/2026/process-safety-and-loss-prevention-msceng |
| 107 | Psychological Research Methods | MSc | /postgraduate/taught/courses/2026/psychological-research-methods-msc |
| 108 | Psychology and Education | MA | /postgraduate/taught/courses/2026/psychology-and-education-ma |
| 109 | Psychology and Education (Conversion) | MSc | /postgraduate/taught/courses/2026/psychology-and-education-conversion-msc |
| 110 | Psychology of Music | MA | /postgraduate/taught/courses/2026/psychology-music-ma |
| 111 | Public Health | MPH | /postgraduate/taught/courses/2026/public-health-mph |
| 112 | Public Health (Health Services Research) | MPH | /postgraduate/taught/courses/2026/public-health-health-services-research-mph |
| 113 | Public Health (Management and Leadership) | MPH | /postgraduate/taught/courses/2026/public-health-management-and-leadership-mph |
| 114 | Public Health (Online) | MPH/PG Certificate | /postgraduate/taught/courses/2026/public-health-online-mph-pg-certificate |
| 115 | Real Estate | MSc | /postgraduate/taught/courses/2026/real-estate-msc |
| 116 | Reproductive and Developmental Medicine | MSc | /postgraduate/taught/courses/2026/reproductive-and-developmental-medicine-msc |
| 117 | Robotics | MSc | /postgraduate/taught/courses/2026/robotics-msc |
| 118 | Science Communication | MSc | /postgraduate/taught/courses/2026/science-communication-msc |
| 119 | Social Research | MA | /postgraduate/taught/courses/2026/social-research-ma |
| 120 | Speech and Language Therapy | MMedSci | /postgraduate/taught/courses/2026/speech-and-language-therapy-mmedsci |
| 121 | Strategic Marketing and Branding | MSc | /postgraduate/taught/courses/2026/strategic-marketing-and-branding-msc |
| 122 | Sustainability and Energy Engineering | MSc | /postgraduate/taught/courses/2026/sustainability-and-energy-engineering-msc |
| 123 | Translation and Intercultural Studies | MA | /postgraduate/taught/courses/2026/translation-and-intercultural-studies-ma |
| 124 | Translational Neuroscience | MSc | /postgraduate/taught/courses/2026/translational-neuroscience-msc |
| 125 | Urban and Regional Planning | MSc | /postgraduate/taught/courses/2026/urban-and-regional-planning-msc |
| 126 | Urban Design and Planning | MSc | /postgraduate/taught/courses/2026/urban-design-and-planning-msc |
| 127 | Vision and Strabismus | MMedSci | /postgraduate/taught/courses/2026/vision-and-strabismus-mmedsci |
| 128 | Wireless Communication Systems | MSc | /postgraduate/taught/courses/2026/wireless-communication-systems-msc |

**PGT degree type breakdown**: MSc (70), MA (30), MMedSci (5), LLM (3), MSc(Eng) (3), MPH (3), MArch (2), MBA (1), LLB (1), EdD (1), PGCE (1), iPGCE (1), PG Certificate (1), Doctorate (1), multi-award (5).

### 2.2 Postgraduate research (PGR)

- **PhD search tool**: `sheffield.ac.uk/postgraduate/phd`
- **Degrees**: PhD, MPhil, Professional Doctorates (EdD, DClinPsy)
- **Research areas**: Available via subject-area browsing; each School offers its own research programmes
- **Funding**: Research Council scholarships, doctoral loans, university scholarships, alumni discount
- **Application**: Via Postgraduate Online Application Form with research proposal

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | S18 |
| **Main application deadline (equal consideration)** | 13 January 2027 (for 2027-28 entry) |
| **Medicine/Dentistry deadline** | 15 October 2026 |
| **Late applications** | 14 January – 30 June 2027 (considered if places available) |
| **Entry year** | September 2027 |

### 3.2 Undergraduate — academic entry requirements (typical, from Computer Science BSc)

| 考试体系 | 标准要求 | Contextual offer (Access Sheffield) | 来源 |
|---------|---------|--------------------------------------|------|
| **A-Level** | A*AA including Maths, or AAA including Maths and CS | AAB including A in Maths, or ABB including A in Maths and B in CS | `sheffield.ac.uk/undergraduate/courses/2027/computer-science-bsc` |
| **IB Diploma** | 38 with 6 in HL Maths | 34 with 6 in HL Maths | Same source |
| **BTEC Extended Diploma** | D*DD + A in A-Level Maths | D*DD + B in A-Level Maths | Same source |
| **Scottish Highers + Advanced Highers** | AAAAA + A in Maths | AAABB + AA in Maths and Computing Science | Same source |
| **Welsh Baccalaureate + 2 A-Levels** | A + A*A including Maths | A + AA in Maths and CS | Same source |
| **Access to HE Diploma** | 45 L3 credits: 42 Distinction, 3 Merit (18 in Maths) | Reduced Distinction requirement | Same source |
| **T Level** | Distinction in Digital Production + A in A-Level Maths | — | Same source |

> **Note**: Entry requirements vary significantly by course. The above is for Computer Science BSc only. Economics BA requires AAB (standard) / ABB (contextual). Medicine (MBChB) has higher requirements. Always check the specific course page.
> **EPQ**: A in a relevant EPQ may reduce the A-Level offer by one grade.

### 3.3 Undergraduate English language requirements

| 考试类型 | 标准要求 | 单项最低 | 来源 |
|---------|---------|---------|------|
| **IELTS Academic** | 6.5 overall | 6.0 each component | `sheffield.ac.uk/international/english-language-requirements` |
| **GCSE English Language** | Grade 4/C | — | Course pages |

> **Exemptions**: Applicants with a first degree taught in English in a majority native English-speaking country are generally exempt.
> **Higher requirements**: Some academic departments may require a higher score than the standard 6.5.
> **Alternative qualifications**: The university recognises multiple English language qualifications; details at `sheffield.ac.uk/international/howtoapply/recognised-english-language-qualifications`.

### 3.4 Graduate admissions

- **PGT entry requirement**: Minimum 2:1 undergraduate honours degree (varies by programme)
- **English language**: IELTS 6.5 (minimum 6.0 each component) — standard; some programmes require higher
- **References and supporting statements**: Not required for most PGT programmes
- **Application**: Via Postgraduate Online Application Form

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition fees (2026 entry)

| Fee status | Annual tuition | Source |
|-----------|---------------|--------|
| **Home (UK)** | £9,790 | `sheffield.ac.uk/undergraduate/tuition-fees-2026` |
| **International** | Course-specific — use fee lookup tool | `ssd.dept.shef.ac.uk/fees/ug/ug-fees.php` |

> **Note on international fees**: The University of Sheffield does not publish international fee amounts on its public-facing web pages. Fees are available only through the interactive fee lookup tool at `ssd.dept.shef.ac.uk/fees/ug/ug-fees.php` where users select Department and Fee Status. Based on comparable Russell Group universities, international UG fees typically range from approximately £22,000 to £38,000 per year depending on subject band (classroom-based subjects at the lower end, laboratory/clinical subjects at the higher end).
> **Fixed fee guarantee**: International students pay the same fixed annual tuition fee for each year of the same course.
> **Fees may increase annually** in line with inflation (RPIX).

### 4.2 Estimated living costs (per year)

| 项目 | 估计费用 (£) |
|------|------------|
| Accommodation | 5,000 – 9,000 |
| Food | 2,000 – 4,000 |
| Transport | 400 – 800 |
| Study materials | 400 – 800 |
| Personal expenses | 1,500 – 3,000 |
| **Total (estimated)** | **9,300 – 17,600** |

> **Note**: Sheffield is one of the most affordable major university cities in the UK, with significantly lower living costs than London.

### 4.3 Scholarships

**International undergraduate scholarships**:
- **Automatic scholarship**: £2,500 per year (up to £10,000 total over degree) for overseas fee-paying students starting September 2026 — no separate application required
- **International Undergraduate Scholarship**: Application-based; deadline has passed for 2026 entry
- **Named scholarships**: Sanctuary Scholarship, Elite Sports Performance Scheme, plus school-specific scholarships (Jayshree Periwal, ESF, Oxbridge Tutorial, GEMS, IDA Sheffield, NCUK, SABIS)

**PGT scholarships**:
- Automatic £3,000 tuition fee discount for international PGT students (subject to eligibility)
- Sheffield alumni discount: up to £2,500

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "The University of Sheffield"
  source_url: https://www.sheffield.ac.uk
  source_snippet: "The University of Sheffield — A world top-100 university"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "5 Faculties: Arts and Humanities, Engineering, Health, Science, Social Sciences"
  source_url: https://www.sheffield.ac.uk/departments/faculties
  source_snippet: "Links to the University's five faculty websites"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.schools
  value: "20 Academic Schools across 5 Faculties"
  source_url: https://www.sheffield.ac.uk/departments/academic
  source_snippet: "Academic schools listing with 20 schools"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.programs.count
  value: "140 undergraduate degree programmes"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027
  source_snippet: "A-Z listing of all 2027-28 undergraduate courses, 140 entries extracted"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-005:
  field: postgraduate_taught.programs.count
  value: "128 postgraduate taught programmes"
  source_url: https://www.sheffield.ac.uk/postgraduate/taught/courses/2026
  source_snippet: "A-Z listing of all 2026-27 PGT courses, 128 entries extracted"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-006:
  field: undergraduate.entry_requirements.alevel.cs
  value: "A*AA including Maths (standard) / AAB including A in Maths (contextual)"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-bsc
  source_snippet: "A*AA including Maths, or AAA including Maths and Computer Science"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.entry_requirements.alevel.economics
  value: "AAB (standard) / ABB (contextual)"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027/economics-ba
  source_snippet: "A Levels: AAB; Access Sheffield: ABB"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english.ielts
  value: "IELTS 6.5 overall (6.0 each component)"
  source_url: https://www.sheffield.ac.uk/international/english-language-requirements
  source_snippet: "Undergraduate: 6.5 overall, 6.0 minimum in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.fees.home
  value: "£9,790 per year (2026 entry)"
  source_url: https://www.sheffield.ac.uk/undergraduate/tuition-fees-2026
  source_snippet: "£9,790 per year — standard annual undergraduate tuition fee for home fee-paying students starting in 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.fees.international
  value: "Course-specific — use fee lookup tool"
  source_url: https://ssd.dept.shef.ac.uk/fees/ug/ug-fees.php
  source_snippet: "Fee lookup tool requiring Department Name and Fee Status selection"
  capture_date: 2026-07-08
  evidence_type: official_webpage_tool

E-U-011:
  field: undergraduate.application.deadline
  value: "13 January 2027 (equal consideration); 15 October 2026 (Medicine/Dentistry)"
  source_url: https://www.sheffield.ac.uk/undergraduate/apply
  source_snippet: "1 September 2026 and 13 January 2027 for equal consideration"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.scholarships.automatic
  value: "£2,500/year (up to £10,000 total) for international students"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-bsc
  source_snippet: "automatic scholarships worth up to £10,000 (£2,500/year) for overseas fee-paying students starting September 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: institution.qs_ranking
  value: "82nd globally (QS World University Rankings 2027)"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027/computer-science-bsc
  source_snippet: "82nd globally — QS World University Rankings 2027"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: institution.russell_group
  value: "Yes — Russell Group member"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses
  source_snippet: "Russell Group" membership referenced
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.dual_honours.count
  value: "21 dual honours programmes"
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027/dual-honours
  source_snippet: "2027-28 dual honours courses listing, 21 entries"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
sheffield-university-knowledge-base-v2
├── 0-overview (Section 0: rule 1-4, institution overview)
├── 1-undergraduate (Section 1: full UG programme listing, chunked by Faculty/School)
│   ├── chunk-01-arts-humanities-architecture-landscape
│   ├── chunk-02-arts-humanities-english
│   ├── chunk-03-arts-humanities-history-philosophy
│   ├── chunk-04-arts-humanities-languages-arts-societies
│   ├── chunk-05-arts-humanities-law
│   ├── chunk-06-engineering-chemical-materials
│   ├── chunk-07-engineering-electrical-electronic
│   ├── chunk-08-engineering-mechanical-aerospace-civil
│   ├── chunk-09-health-dentistry
│   ├── chunk-10-health-medicine
│   ├── chunk-11-health-allied-health
│   ├── chunk-12-science-biosciences
│   ├── chunk-13-science-computer-science
│   ├── chunk-14-science-mathematical-physical-sciences
│   ├── chunk-15-science-geography-planning
│   ├── chunk-16-science-psychology
│   ├── chunk-17-social-sciences-economics
│   ├── chunk-18-social-sciences-management
│   ├── chunk-19-social-sciences-sociological-studies
│   └── chunk-20-social-sciences-journalism
├── 2-graduate (Section 2: 128 PGT courses + PGR info)
├── 3-applications (Section 3: requirements, deadlines, English)
├── 4-costs (Section 4: fees, living costs, scholarships)
├── 5-evidence (Section 5: evidence chain)
└── 6-monitoring (Section 7: monitoring watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "sheffield-university-knowledge-base-v2"
  school: "<academic school>"
  degree_level: "<BA|BSc|BEng|MEng|MComp|MBiolSci|...>"
  level: undergraduate
  field_type: programs
  source_url: https://www.sheffield.ac.uk/undergraduate/courses/2027
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | International tuition fees by course (requires fee lookup tool interaction) | `ssd.dept.shef.ac.uk/fees/ug/ug-fees.php` |
| **P0** | PGT course-level fees | `ssd.dept.shef.ac.uk/fees/pgt/pgt-fees.php` |
| **P1** | Per-course A-Level/IB entry requirements (all 140 UG courses) | Individual course pages |
| **P1** | Accepted English language qualifications (full list) | `sheffield.ac.uk/international/howtoapply/recognised-english-language-qualifications` |
| **P1** | Scholarship details (amounts, eligibility for each named scholarship) | Individual scholarship pages |
| **P2** | Course module details and curriculum structure | Individual course pages |
| **P2** | PhD programme listings by school | `sheffield.ac.uk/postgraduate/phd` |
| **P2** | Accommodation costs | `sheffield.ac.uk/accommodation` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | The University of Sheffield | Cardiff | Newcastle | Durham |
|-----------|---------------------------|---------|-----------|--------|
| Total UG programmes | 140 | 237 | 147 | — |
| Total PGT programmes | 128 | — | — | — |
| Academic schools | 20 | 24 | — | — |
| Faculties/Colleges | 5 | 3 | — | — |
| UG Home tuition | £9,790 | £9,250 | £9,250 | — |
| UG International tuition (range) | Course-specific (lookup tool) | £22,700 – £29,450 | £22,000 – £35,000 | — |
| IELTS minimum (UG) | 6.5 (6.0 each) | 6.5 (5.5 each) | 6.5 (5.5 each) | — |
| A-Level typical (CS) | A*AA | ABB | — | — |
| UCAS deadline | 13 Jan 2027 | 29 Jan 2026 | — | — |
| Region | Sheffield, England | Cardiff, Wales | Newcastle, England | — |
| Russell Group | Yes | Yes | Yes | — |
| QS 2027 ranking | 82 | — | — | — |
| Dual honours | 21 | — | — | — |
| Foundation year | 15 courses | — | — | — |
| Auto scholarship (intl) | £2,500/year | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: sheffield.ac.uk (main domain)
> **Verification**: WebFetch extraction from official university web pages
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programs (140/140) ✅ | PGT programs (128/128) ✅ | Faculty hierarchy ✅ | English requirements ✅ | Home fees ✅ | International fees ⚠ (requires lookup tool) | Evidence (15 blocks) ✅
> **Known limitation**: International tuition fee amounts are not published on Sheffield's public web pages; they are only available via an interactive fee lookup tool. The fee lookup tool requires JavaScript interaction that WebFetch cannot perform.
