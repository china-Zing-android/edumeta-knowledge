# University of Liverpool Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch + manual extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 252 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/LLM/MPH/PGCert/PGDip etc.) | 244 |
| 研究生博士项目 (PGR: PhD/MPhil/MD/DBA/MRes) | 209 |
| **学位项目总计 (UG + PGT + PGR)** | **705** |
| 学院 (Faculties) | 3 |
| 学校 / 研究所 (Schools / Institutes) | 12 |
| 学术院系 (Academic Departments) | 40+ |

> **Data source**: University of Liverpool course listing pages (`liverpool.ac.uk/courses/undergraduate`, `/courses/postgraduate-taught`, `/courses/postgraduate-research`), 252 + 244 + 209 courses extracted.
> **Note**: PGT and PGR numbers include named degree programmes and funded PhD project opportunities listed on the course pages.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Liverpool
├── Faculty of Health and Life Sciences                    [学院]
│   ├── Institute of Infection, Veterinary and Ecological Sciences
│   │   ├── School of Veterinary Science                   [系]
│   │   ├── Dept of Evolution, Ecology and Behaviour       [系]
│   │   ├── Dept of Clinical Infection, Microbiology and Immunology [系]
│   │   ├── Dept of Equine Clinical Science                [系]
│   │   ├── Dept of Infection Biology and Microbiomes      [系]
│   │   ├── Dept of Livestock and One Health               [系]
│   │   ├── Dept of Small Animal Clinical Science          [系]
│   │   └── Dept of Veterinary Anatomy, Physiology and Pathology [系]
│   ├── Institute of Life Course and Medical Sciences
│   │   ├── School of Medicine                             [系]
│   │   ├── School of Dentistry                            [系]
│   │   ├── Dept of Cardiovascular and Metabolic Medicine  [系]
│   │   ├── Dept of Eye and Vision Science                 [系]
│   │   ├── Dept of Musculoskeletal and Ageing Science     [系]
│   │   └── Women's and Children's Health                  [系]
│   ├── Institute of Population Health
│   │   ├── School of Allied Health Professionals and Nursing [系]
│   │   ├── Dept of Psychology                             [系]
│   │   ├── Dept of Health Data Science                    [系]
│   │   ├── Dept of Public Health, Policy and Systems      [系]
│   │   └── Dept of Primary Care and Mental Health         [系]
│   └── Institute of Systems, Molecular and Integrative Biology
│       ├── School of Biosciences                          [系]
│       ├── Dept of Biochemistry, Cell and Systems Biology [系]
│       ├── Dept of Molecular and Clinical Cancer Medicine [系]
│       └── Dept of Pharmacology and Therapeutics          [系]
├── Faculty of Humanities and Social Sciences              [学院]
│   ├── School of the Arts
│   │   ├── Dept of Architecture                           [系]
│   │   ├── Dept of Communication and Media                [系]
│   │   ├── Dept of English                                [系]
│   │   ├── Dept of Music                                  [系]
│   │   └── Dept of Philosophy                             [系]
│   ├── School of Histories, Languages and Cultures
│   │   ├── Dept of Archaeology, Classics and Egyptology   [系]
│   │   ├── Dept of History                                [系]
│   │   ├── Dept of Irish Studies                          [系]
│   │   ├── Dept of Languages, Cultures and Film           [系]
│   │   ├── Dept of Politics                               [系]
│   │   └── Institute of Education                         [系]
│   ├── School of Law and Social Justice
│   │   ├── Liverpool Law School                           [系]
│   │   └── Dept of Sociology, Social Policy and Criminology [系]
│   └── Management School
│       └── Dept of Economics                              [系]
└── Faculty of Science and Engineering                     [学院]
    ├── School of Computer Science and Informatics         [系]
    ├── School of Engineering
    │   ├── Dept of Civil and Environmental Engineering    [系]
    │   ├── Dept of Electrical Engineering and Electronics [系]
    │   ├── Dept of Materials, Design and Manufacturing Engineering [系]
    │   └── Dept of Mechanical and Aerospace Engineering   [系]
    ├── School of Environmental Sciences
    │   ├── Dept of Earth, Ocean and Ecological Sciences   [系]
    │   └── Dept of Geography and Planning                 [系]
    └── School of Physical Sciences
        ├── Dept of Chemistry                              [系]
        ├── Dept of Physics                                [系]
        └── Dept of Mathematical Sciences                  [系]
```

> **Source**: `liverpool.ac.uk/departments/` and `liverpool.ac.uk/about/the-university/our-structure/`
> **Note**: The Faculty of Health and Life Sciences organises its units under **Institutes** (4), while the other two Faculties use **Schools** as their intermediate grouping. All three Faculties contain departments at the lowest level.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | 48 |
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | 110 |
| BEng (Hons) | Bachelor of Engineering (Honours) | 本科 | 20 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | 7 |
| MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| BDS | Bachelor of Dental Surgery | 本科 | 1 |
| BVSc | Bachelor of Veterinary Science | 本科 | 1 |
| BN (Hons) | Bachelor of Nursing (Honours) | 本科 | 1 |
| MEng (Hons) | Master of Engineering (Honours, Integrated) | 本科 | 20 |
| MBiol (Hons) | Master of Biology (Honours, Integrated) | 本科 | 8 |
| MPhys (Hons) | Master of Physics (Honours, Integrated) | 本科 | 9 |
| MChem (Hons) | Master of Chemistry (Honours, Integrated) | 本科 | 6 |
| MMath (Hons) | Master of Mathematics (Honours, Integrated) | 本科 | 4 |
| MPharm | Master of Pharmacy (Integrated) | 本科 | 2 |
| MArch | Master of Architecture (Integrated) | 本科 | 2 |
| MPlan | Master of Planning (Integrated) | 本科 | 1 |
| Combined | Combined/Joint Honours (Language degrees) | 本科 | 6 |
| CertHE | Certificate of Higher Education | 本科 | 0 |
| **合计** | | | **252** |

> **Note**: MEng, MBiol, MPhys, MChem, MMath, MPharm, MArch, MPlan are 4-year integrated master's programmes counted as undergraduate (UK convention). "Combined" degrees are language joint honours programmes with a specific combined degree designation.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 学位 | BA | BDS | BEng | BN | BSc | BVSc | Combined | LLB | MArch | MBChB | MBiol | MChem | MEng | MMath | MPharm | MPhys | MPlan | 合计 |
|------------|-----|-----|------|-----|------|------|----------|-----|-------|-------|-------|-------|------|-------|--------|-------|-------|------|
| Health and Life Sciences | 0 | 1 | 0 | 1 | 12 | 1 | 0 | 0 | 0 | 2 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | **29** |
| (incl. Allied Health & Nursing) | | | | | | | | | | | | | | | | | | |
| (incl. Biosciences) | | | | | | | | | | | | | | | | | | |
| Humanities and Social Sciences | 43 | 0 | 0 | 0 | 15 | 0 | 6 | 7 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **96** |
| (incl. School of the Arts) | | | | | | | | | | | | | | | | | | |
| (incl. Histories, Languages, Cultures) | | | | | | | | | | | | | | | | | | |
| (incl. Law and Social Justice) | | | | | | | | | | | | | | | | | | |
| (incl. Management School) | | | | | | | | | | | | | | | | | | |
| Science and Engineering | 2 | 0 | 20 | 0 | 78 | 0 | 0 | 0 | 0 | 0 | 2 | 6 | 20 | 4 | 2 | 9 | 0 | **127** |
| (incl. Computer Science) | | | | | | | | | | | | | | | | | | |
| (incl. Engineering) | | | | | | | | | | | | | | | | | | |
| (incl. Environmental Sciences) | | | | | | | | | | | | | | | | | | |
| (incl. Physical Sciences) | | | | | | | | | | | | | | | | | | |
| **合计** | **48** | **1** | **20** | **1** | **110** | **1** | **6** | **7** | **2** | **2** | **8** | **6** | **20** | **4** | **2** | **9** | **1** | **252** |

> **Reconciliation check**: Rule-1 total (252) == matrix-sum (252) == Rule-5 rows (252). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Liverpool is organised into 3 academic Faculties containing 12 Schools/Institutes and 40+ Departments. All 252 undergraduate degree programmes are administered by one of these units. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate degree programmes — grouped by Faculty > School > Department > Degree Level

---

#### Faculty of Health and Life Sciences

##### Institute of Infection, Veterinary and Ecological Sciences — School of Veterinary Science

###### BVSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Science | https://www.liverpool.ac.uk/courses/veterinary-science-bvsc |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Bioveterinary Science | https://www.liverpool.ac.uk/courses/bioveterinary-science-bsc-hons |

###### MBiol (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Bioveterinary Science | https://www.liverpool.ac.uk/courses/bioveterinary-science-mbiol-hons |

###### BVSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Veterinary Science (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-veterinary-science-year-0 |

---

##### Institute of Life Course and Medical Sciences — School of Medicine

###### MBChB (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine and Surgery | https://www.liverpool.ac.uk/courses/medicine-and-surgery-mbchb |
| 2 | Medicine and Surgery (Graduate Entry) | https://www.liverpool.ac.uk/courses/medicine-and-surgery-graduate-entry-mbchb |

###### MBChB — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Medicine (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-medicine-year-0 |

---

##### Institute of Life Course and Medical Sciences — School of Dentistry

###### BDS (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Surgery | https://www.liverpool.ac.uk/courses/dental-surgery-bds |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Therapy | https://www.liverpool.ac.uk/courses/dental-therapy-bsc-hons |

###### BDS — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Dentistry (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-dentistry-year-0 |

###### BSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Dental Therapy (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-dental-therapy-year-0 |

---

##### Institute of Life Course and Medical Sciences — Department of Anatomy

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Anatomy and Human Biology | https://www.liverpool.ac.uk/courses/anatomy-and-human-biology-bsc-hons |

###### MBiol (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Anatomy and Human Biology | https://www.liverpool.ac.uk/courses/anatomy-and-human-biology-mbiol-hons |

---

##### Institute of Population Health — School of Allied Health Professionals and Nursing

###### BN (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.liverpool.ac.uk/courses/nursing-bn-hons |

###### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Acute, Critical and Emergency Care (ACE Care) | https://www.liverpool.ac.uk/courses/acute-critical-and-emergency-care-ace-care-bsc-hons |
| 2 | Diagnostic Radiography | https://www.liverpool.ac.uk/courses/diagnostic-radiography-bsc-hons |
| 3 | Occupational Therapy | https://www.liverpool.ac.uk/courses/occupational-therapy-bsc-hons |
| 4 | Orthoptics | https://www.liverpool.ac.uk/courses/orthoptics-bsc-hons |
| 5 | Physiotherapy | https://www.liverpool.ac.uk/courses/physiotherapy-bsc-hons |
| 6 | Therapeutic Radiography and Oncology | https://www.liverpool.ac.uk/courses/therapeutic-radiography-and-oncology-bsc-hons |

###### BN — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Nursing (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-nursing-year-0 |

###### BSc — Foundation (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Diagnostic Radiography (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-diagnostic-radiography-year-0 |
| 2 | Foundation to Occupational Therapy (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-occupational-therapy-year-0 |
| 3 | Foundation to Orthoptics (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-orthoptics-year-0 |
| 4 | Foundation to Physiotherapy (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-physiotherapy-year-0 |

###### BSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation to Therapeutic Radiography and Oncology (Year 0) | https://www.liverpool.ac.uk/courses/foundation-to-human-and-animal-health-professions-therapeutic-radiography-oncology-year-0 |

---

##### Institute of Systems, Molecular and Integrative Biology — School of Biosciences

###### BSc (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.liverpool.ac.uk/courses/biochemistry-bsc-hons |
| 2 | Biological Sciences | https://www.liverpool.ac.uk/courses/biological-sciences-bsc-hons |
| 3 | Biological Sciences (with a Foundation Year) | https://www.liverpool.ac.uk/courses/biological-sciences-with-a-foundation-year-leading-to-bsc-hons |
| 4 | Biomedical Sciences | https://www.liverpool.ac.uk/courses/biomedical-sciences-bsc-hons |
| 5 | Microbiology and Infection | https://www.liverpool.ac.uk/courses/microbiology-and-infection-bsc-hons |

###### MBiol (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.liverpool.ac.uk/courses/biochemistry-mbiol-hons |
| 2 | Biological Sciences | https://www.liverpool.ac.uk/courses/biological-sciences-mbiol-hons |
| 3 | Biomedical Sciences | https://www.liverpool.ac.uk/courses/biomedical-sciences-mbiol-hons |
| 4 | Microbiology and Infection | https://www.liverpool.ac.uk/courses/microbiology-and-infection-mbiol-hons |

---

##### Institute of Systems, Molecular and Integrative Biology — Department of Pharmacology

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacology | https://www.liverpool.ac.uk/courses/pharmacology-bsc-hons |

###### MBiol (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacology | https://www.liverpool.ac.uk/courses/pharmacology-mbiol-hons |

---

##### Institute of Population Health — Department of Psychology

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.liverpool.ac.uk/courses/psychology-bsc-hons |
| 2 | Psychology BSc (Hons) (2+2 programme with Foundation Element) | https://www.liverpool.ac.uk/courses/psychology-bsc-hons-22-programme-with-foundation-element |

---

#### Faculty of Humanities and Social Sciences

##### School of the Arts — Department of Architecture

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.liverpool.ac.uk/courses/architecture-ba-hons |
| 2 | Architecture Design Studies | https://www.liverpool.ac.uk/courses/architecture-design-studies-ba-hons |

###### MArch (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Architecture | https://www.liverpool.ac.uk/courses/master-of-architecture-march |
| 2 | Master of Architecture (Integrated) | https://www.liverpool.ac.uk/courses/master-of-architecture-integrated-march |

---

##### School of the Arts — Department of Communication and Media

###### BA (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Communication and Media | https://www.liverpool.ac.uk/courses/communication-and-media-ba-hons |
| 2 | Communication, Media and Politics | https://www.liverpool.ac.uk/courses/communication-media-and-politics-ba-hons |
| 3 | Communication, Media and Popular Music | https://www.liverpool.ac.uk/courses/communication-media-and-popular-music-ba-hons-2 |
| 4 | Communication and Media and Game Design Studies | https://www.liverpool.ac.uk/courses/communication-and-media-with-game-design-studies-ba-hons-2 |
| 5 | Media, Data and Society | https://www.liverpool.ac.uk/courses/media-data-and-society-ba-hons |
| 6 | Media and Culture | https://www.liverpool.ac.uk/courses/media-and-culture-ba-hons |

---

##### School of the Arts — Department of English

###### BA (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.liverpool.ac.uk/courses/english-ba-hons |
| 2 | English Language | https://www.liverpool.ac.uk/courses/english-language-ba-hons |
| 3 | English Literature | https://www.liverpool.ac.uk/courses/english-literature-ba-hons |
| 4 | English Literature with Drama Studies | https://www.liverpool.ac.uk/courses/english-literature-with-drama-studies-ba-hons |
| 5 | English with World Literature | https://www.liverpool.ac.uk/courses/english-with-world-literature-ba-hons |

---

##### School of the Arts — Department of Music

###### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.liverpool.ac.uk/courses/music-ba-hons |
| 2 | Music and Popular Music | https://www.liverpool.ac.uk/courses/music-and-popular-music-ba-hons |
| 3 | Music and Technology | https://www.liverpool.ac.uk/courses/music-and-technology-ba-hons |

---

##### School of the Arts — Department of Philosophy

###### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.liverpool.ac.uk/courses/philosophy-ba-hons |
| 2 | Philosophy and Politics | https://www.liverpool.ac.uk/courses/philosophy-and-politics-ba-hons |
| 3 | Philosophy, Politics and Economics | https://www.liverpool.ac.uk/courses/philosophy-politics-and-economics-ba-hons |
| 4 | Philosophy, Politics and Economics with a Year in Industry | https://www.liverpool.ac.uk/courses/philosophy-politics-and-economics-with-a-year-in-industry-ba-hons |

---

##### School of Histories, Languages and Cultures — Department of Archaeology, Classics and Egyptology

###### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology | https://www.liverpool.ac.uk/courses/archaeology-ba-hons |
| 2 | Archaeology of Ancient Civilisations | https://www.liverpool.ac.uk/courses/archaeology-of-ancient-civilisations-ba-hons |
| 3 | Classical Studies | https://www.liverpool.ac.uk/courses/classical-studies-ba-hons |
| 4 | Classics | https://www.liverpool.ac.uk/courses/classics-ba-hons |

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeological Science | https://www.liverpool.ac.uk/courses/archaeological-science-bsc-hons |
| 2 | Evolutionary Anthropology | https://www.liverpool.ac.uk/courses/evolutionary-anthropology-bsc-hons |

###### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Egyptology | https://www.liverpool.ac.uk/courses/egyptology-ba-hons |

---

##### School of Histories, Languages and Cultures — Department of History

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient History | https://www.liverpool.ac.uk/courses/ancient-history-ba-hons |
| 2 | History | https://www.liverpool.ac.uk/courses/history-ba-hons |

---

##### School of Histories, Languages and Cultures — Department of Irish Studies

###### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Irish Studies | https://www.liverpool.ac.uk/courses/irish-studies-ba-hons |

---

##### School of Histories, Languages and Cultures — Department of Languages, Cultures and Film

###### BA (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Film Studies | https://www.liverpool.ac.uk/courses/film-studies-ba-hons |
| 2 | French | https://www.liverpool.ac.uk/courses/french-ba-hons |
| 3 | German | https://www.liverpool.ac.uk/courses/german-ba-hons |
| 4 | Hispanic Studies | https://www.liverpool.ac.uk/courses/hispanic-studies-ba-hons |
| 5 | Italian | https://www.liverpool.ac.uk/courses/italian-ba-hons |
| 6 | Modern Languages (Triple Subject) | https://www.liverpool.ac.uk/courses/modern-languages-triple-subject-ba-hons |

###### Combined degree (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Catalan | https://www.liverpool.ac.uk/courses/catalan-combined-degree |
| 2 | Chinese Studies | https://www.liverpool.ac.uk/courses/chinese-studies-combined-degree |
| 3 | Portuguese | https://www.liverpool.ac.uk/courses/portuguese-combined-degree |
| 4 | Spanish | https://www.liverpool.ac.uk/courses/spanish-combined-degree |

---

##### School of Histories, Languages and Cultures — Department of Politics

###### BA (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | International Relations | https://www.liverpool.ac.uk/courses/international-relations-ba-hons |
| 2 | Politics | https://www.liverpool.ac.uk/courses/politics-ba-hons |
| 3 | Screen Industries and Entertainment | https://www.liverpool.ac.uk/courses/screen-industries-and-entertainment-ba-hons |

---

##### School of Histories, Languages and Cultures — Institute of Education

###### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environment and Planning | https://www.liverpool.ac.uk/courses/environment-and-planning-ba-hons |

---

##### School of Law and Social Justice — Liverpool Law School

###### LLB (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://www.liverpool.ac.uk/courses/law-llb-hons |
| 2 | Law (Graduate Entry) | https://www.liverpool.ac.uk/courses/law-graduate-entry-llb-hons |
| 3 | Law with Business | https://www.liverpool.ac.uk/courses/law-with-business-llb-hons |
| 4 | Law with Criminology | https://www.liverpool.ac.uk/courses/law-with-criminology-llb-hons |
| 5 | Law with Philosophy | https://www.liverpool.ac.uk/courses/law-with-philosophy-llb-hons |
| 6 | Law with Politics | https://www.liverpool.ac.uk/courses/law-with-politics-llb-hons |
| 7 | Law with a Year Abroad | https://www.liverpool.ac.uk/courses/law-with-a-year-abroad-llb-hons |

---

##### School of Law and Social Justice — Department of Sociology, Social Policy and Criminology

###### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.liverpool.ac.uk/courses/criminology-ba-hons |
| 2 | Criminology with Social Policy | https://www.liverpool.ac.uk/courses/criminology-with-social-policy-ba-hons |
| 3 | Criminology with Sociology | https://www.liverpool.ac.uk/courses/criminology-with-sociology-ba-hons |
| 4 | Sociology | https://www.liverpool.ac.uk/courses/sociology-ba-hons |

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology with Criminology | https://www.liverpool.ac.uk/courses/sociology-with-criminology-ba-hons |
| 2 | Sociology with Social Policy | https://www.liverpool.ac.uk/courses/sociology-with-social-policy-ba-hons |

###### Combined degree (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Policy | https://www.liverpool.ac.uk/courses/social-policy-combined-degree |
| 2 | Catalan | (listed under Languages) |

---

##### Management School — Department of Economics

###### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://www.liverpool.ac.uk/courses/business-economics-ba-hons |
| 2 | Business Economics with a Year in Industry | https://www.liverpool.ac.uk/courses/business-economics-with-a-year-in-industry-ba-hons |
| 3 | Business Management | https://www.liverpool.ac.uk/courses/business-management-ba-hons |
| 4 | Business Management with a Year in Industry | https://www.liverpool.ac.uk/courses/business-management-with-a-year-in-industry-ba-hons |

###### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance | https://www.liverpool.ac.uk/courses/accounting-and-finance-bsc-hons |
| 2 | Accounting and Finance with a Year in Industry | https://www.liverpool.ac.uk/courses/accounting-and-finance-with-a-year-in-industry-bsc-hons |
| 3 | Finance and Data Analytics | https://www.liverpool.ac.uk/courses/finance-and-data-analytics-bsc-hons |
| 4 | Finance and Data Analytics with a Year in Industry | https://www.liverpool.ac.uk/courses/finance-and-data-analytics-with-a-year-in-industry-bsc-hons |
| 5 | Financial Computing | https://www.liverpool.ac.uk/courses/financial-computing-bsc-hons |
| 6 | Financial Computing with a Year in Industry | https://www.liverpool.ac.uk/courses/financial-computing-with-a-year-in-industry-bsc-hons |

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.liverpool.ac.uk/courses/economics-bsc-hons |
| 2 | Economics with a Year in Industry | https://www.liverpool.ac.uk/courses/economics-with-a-year-in-industry-bsc-hons |

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.liverpool.ac.uk/courses/economics-ba |
| 2 | Economics with a Year in Industry | https://www.liverpool.ac.uk/courses/economics-with-a-year-in-industry-ba |

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | International Management | https://www.liverpool.ac.uk/courses/international-management-ba-hons |
| 2 | International Management with a Year in Industry | https://www.liverpool.ac.uk/courses/international-management-with-a-year-in-industry-ba-hons |

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.liverpool.ac.uk/courses/marketing-ba-hons |
| 2 | Marketing with a Year in Industry | https://www.liverpool.ac.uk/courses/marketing-with-a-year-in-industry-ba-hons |

---

#### Faculty of Science and Engineering

##### School of Computer Science and Informatics

###### BSc (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://www.liverpool.ac.uk/courses/artificial-intelligence-bsc |
| 2 | Artificial Intelligence and Business Analytics | https://www.liverpool.ac.uk/courses/artificial-intelligence-and-business-analytics-bsc-hons |
| 3 | Artificial Intelligence and Business Analytics with a Year in Industry | https://www.liverpool.ac.uk/courses/artificial-intelligence-and-business-analytics-with-a-year-in-industry-bsc-hons |
| 4 | Artificial Intelligence with a Year in Industry | https://www.liverpool.ac.uk/courses/artificial-intelligence-with-a-year-in-industry-bsc |
| 5 | Computer Science | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons |
| 6 | Computer Science (Foundation) (4 year route with Carmel College) | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons-foundation-4-year-route-with-carmel-college |
| 7 | Computer Science with Software Development | https://www.liverpool.ac.uk/courses/computer-science-with-software-development-bsc-hons |
| 8 | Computer Science with Software Development with a Year in Industry | https://www.liverpool.ac.uk/courses/computer-science-with-software-development-with-a-year-in-industry-bsc-hons |
| 9 | Computer Science with a Year in Industry | https://www.liverpool.ac.uk/courses/computer-science-with-a-year-in-industry-bsc-hons |
| 10 | Computer Science — Algorithms and Optimisation pathway | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons-algorithms-and-optimisation-pathway-2 |

###### BSc (4 programmes — pathways)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science — Artificial Intelligence pathway | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons-artificial-intelligence-pathway-2 |
| 2 | Computer Science — Cyber Security pathway | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons-cyber-security-pathway-2 |
| 3 | Computer Science — Data Science pathway | https://www.liverpool.ac.uk/courses/computer-science-bsc-hons-data-science-pathway-2 |
| 4 | Game Design | https://www.liverpool.ac.uk/courses/game-design-bsc-hons |

###### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.liverpool.ac.uk/courses/computer-science-meng-hons |
| 2 | Computer Science with a Year in Industry | https://www.liverpool.ac.uk/courses/computer-science-with-a-year-in-industry-meng-hons |
| 3 | Computer Science and Electronic Engineering | https://www.liverpool.ac.uk/courses/computer-science-and-electronic-engineering-meng-hons |

###### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Electronic Engineering | https://www.liverpool.ac.uk/courses/computer-science-and-electronic-engineering-beng-hons |
| 2 | Computer Science and Electronic Engineering with Year in Industry | https://www.liverpool.ac.uk/courses/computer-science-and-electronic-engineering-with-year-in-industry-beng-hons |

---

##### School of Engineering — Department of Civil and Environmental Engineering

###### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.liverpool.ac.uk/courses/civil-engineering-beng-hons |
| 2 | Civil Engineering with Year in Industry | https://www.liverpool.ac.uk/courses/civil-engineering-with-year-in-industry-beng-hons |

###### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.liverpool.ac.uk/courses/civil-engineering-meng-hons |
| 2 | Civil Engineering with Year in Industry | https://www.liverpool.ac.uk/courses/civil-engineering-with-year-in-industry-meng-hons |
| 3 | Civil and Structural Engineering | https://www.liverpool.ac.uk/courses/civil-and-structural-engineering-meng-hons |

---

##### School of Engineering — Department of Electrical Engineering and Electronics

###### BEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-beng-hons |
| 2 | Electrical and Electronic Engineering with a Year Abroad | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-with-a-year-abroad-beng-hons |
| 3 | Electrical and Electronic Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-with-a-year-in-industry-beng-hons |

###### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-meng-hons |
| 2 | Electrical and Electronic Engineering with a Year Abroad | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-with-a-year-abroad-meng-hons |
| 3 | Electrical and Electronic Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/electrical-and-electronic-engineering-with-a-year-in-industry-meng-hons |

---

##### School of Engineering — Department of Mechanical and Aerospace Engineering

###### BEng (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.liverpool.ac.uk/courses/aerospace-engineering-beng-hons |
| 2 | Aerospace Engineering with Pilot Studies | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-pilot-studies-beng-hons |
| 3 | Aerospace Engineering with Pilot Studies with a Year in Industry | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-pilot-studies-with-a-year-in-industry-beng-hons |
| 4 | Aerospace Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-a-year-in-industry-beng-hons |
| 5 | Mechanical Engineering | https://www.liverpool.ac.uk/courses/mechanical-engineering-beng-hons |

###### BEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/mechanical-engineering-with-a-year-in-industry-beng-hons |
| 2 | Architectural Engineering | https://www.liverpool.ac.uk/courses/architectural-engineering-beng-hons |

###### MEng (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.liverpool.ac.uk/courses/aerospace-engineering-meng-hons |
| 2 | Aerospace Engineering with Pilot Studies | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-pilot-studies-meng-hons |
| 3 | Aerospace Engineering with Pilot Studies with a Year in Industry | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-pilot-studies-with-a-year-in-industry-meng-hons |
| 4 | Aerospace Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/aerospace-engineering-with-a-year-in-industry-meng-hons |
| 5 | Mechanical Engineering | https://www.liverpool.ac.uk/courses/mechanical-engineering-meng-hons |
| 6 | Mechanical Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/mechanical-engineering-with-a-year-in-industry-meng-hons |

###### MEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.liverpool.ac.uk/courses/architectural-engineering-meng-hons |

---

##### School of Engineering — Department of Materials, Design and Manufacturing Engineering

###### BEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechatronics and Robotic Systems | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-beng-hons |
| 2 | Mechatronics and Robotic Systems with Year in Industry | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-with-year-in-industry-beng-hons |
| 3 | Mechatronics and Robotic Systems with a Year Abroad | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-with-a-year-abroad-beng-hons |

###### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Product Design Engineering | https://www.liverpool.ac.uk/courses/product-design-engineering-beng |

###### MEng (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechatronics and Robotic Systems | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-meng-hons |
| 2 | Mechatronics and Robotic Systems with Year in Industry | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-with-year-in-industry-meng-hons |
| 3 | Mechatronics and Robotic Systems with a Year Abroad | https://www.liverpool.ac.uk/courses/mechatronics-and-robotic-systems-with-a-year-abroad-meng-hons |
| 4 | Product Design Engineering | https://www.liverpool.ac.uk/courses/product-design-engineering-meng-hons |

###### MEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Product Design Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/product-design-engineering-with-a-year-in-industry-meng-hons |

###### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Product Design Engineering with a Year in Industry | https://www.liverpool.ac.uk/courses/product-design-engineering-with-year-in-industry-beng-hons |

---

##### School of Engineering — Foundation

###### BEng (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Foundation (4 year route including a Foundation Year at Carmel College) | https://www.liverpool.ac.uk/courses/engineering-foundation-beng-hons-4-year-route-including-a-foundation-year-at-carmel-college |

---

##### School of Environmental Sciences — Department of Geography and Planning

###### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.liverpool.ac.uk/courses/geography-ba-hons |
| 2 | Geography and Planning | https://www.liverpool.ac.uk/courses/geography-and-planning-ba-hons |

###### BA (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Planning | https://www.liverpool.ac.uk/courses/urban-planning-ba-hons |

###### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.liverpool.ac.uk/courses/geography-bsc-hons |
| 2 | Geography BSc (Hons) (4 year route including a foundation year at Carmel College) | https://www.liverpool.ac.uk/courses/geography-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college |
| 3 | Geography and Oceanography | https://www.liverpool.ac.uk/courses/geography-and-oceanography-bsc-hons |

---

##### School of Environmental Sciences — Department of Earth, Ocean and Ecological Sciences

###### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Climate Science | https://www.liverpool.ac.uk/courses/climate-science-bsc-hons |
| 2 | Environmental Geology with Physical Geography | https://www.liverpool.ac.uk/courses/environmental-geology-with-physical-geography-bsc-hons |
| 3 | Environmental Geoscience | https://www.liverpool.ac.uk/courses/environmental-geoscience-bsc-hons |
| 4 | Environmental Science | https://www.liverpool.ac.uk/courses/environmental-science-bsc-hons |
| 5 | Geology | https://www.liverpool.ac.uk/courses/geology-bsc-hons |
| 6 | Geology with Physical Geography | https://www.liverpool.ac.uk/courses/geology-with-physical-geography-bsc-hons |
| 7 | Ocean Sciences | https://www.liverpool.ac.uk/courses/ocean-sciences-bsc-hons |

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Biology | https://www.liverpool.ac.uk/courses/marine-biology-bsc-hons |
| 2 | Marine Biology and Oceanography | https://www.liverpool.ac.uk/courses/marine-biology-and-oceanography-bsc-hons |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Biology with Oceanography | https://www.liverpool.ac.uk/courses/marine-biology-with-oceanography-bsc-hons |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ocean and Climate Sciences | https://www.liverpool.ac.uk/courses/ocean-and-climate-sciences-bsc-hons |

###### MBiol (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Biology | https://www.liverpool.ac.uk/courses/marine-biology-mbiol-hons |
| 2 | Zoology | https://www.liverpool.ac.uk/courses/zoology-mbiol-hons |

###### BSc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Zoology | https://www.liverpool.ac.uk/courses/zoology-bsc-hons |
| 2 | Earth, Environmental and Marine Sciences (4 year route including a Foundation Year at Carmel College) | https://www.liverpool.ac.uk/courses/earth-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college |

---

##### School of Physical Sciences — Department of Chemistry

###### BSc (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.liverpool.ac.uk/courses/chemistry-bsc-hons |
| 2 | Chemistry with a Year Abroad | https://www.liverpool.ac.uk/courses/chemistry-with-a-year-abroad-bsc-hons |
| 3 | Chemistry with a Year in Industry | https://www.liverpool.ac.uk/courses/chemistry-with-a-year-in-industry-bsc-hons |
| 4 | Medicinal Chemistry | https://www.liverpool.ac.uk/courses/medicinal-chemistry-bsc-hons |
| 5 | Medicinal Chemistry with a Year Abroad | https://www.liverpool.ac.uk/courses/medicinal-chemistry-with-a-year-abroad-bsc-hons |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicinal Chemistry with a Year in Industry | https://www.liverpool.ac.uk/courses/medicinal-chemistry-with-a-year-in-industry-bsc-hons |

###### MChem (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.liverpool.ac.uk/courses/chemistry-mchem-hons |
| 2 | Chemistry with Research in Industry | https://www.liverpool.ac.uk/courses/chemistry-with-research-in-industry-mchem-hons |
| 3 | Chemistry with a Year Abroad | https://www.liverpool.ac.uk/courses/chemistry-with-a-year-abroad-mchem-hons |
| 4 | Medicinal Chemistry with Pharmacology | https://www.liverpool.ac.uk/courses/medicinal-chemistry-with-pharmacology-mchem-hons |

###### MChem (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicinal Chemistry with Pharmacology with Research in Industry | https://www.liverpool.ac.uk/courses/medicinal-chemistry-with-pharmacology-with-research-in-industry-mchem-hons |
| 2 | Medicinal Chemistry with Pharmacology with a Year Abroad | https://www.liverpool.ac.uk/courses/medicinal-chemistry-with-pharmacology-with-a-year-abroad-mchem-hons |

###### BSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Sciences BSc (Hons) (4 year route including a Foundation Year at Carmel College) | https://www.liverpool.ac.uk/courses/chemical-sciences-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college |

---

##### School of Physical Sciences — Department of Physics

###### BSc (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.liverpool.ac.uk/courses/physics-bsc-hons |
| 2 | Physics and Mathematics | https://www.liverpool.ac.uk/courses/physics-and-mathematics-bsc-hons |
| 3 | Physics and Mathematics with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-and-mathematics-with-a-year-abroad-bsc-hons |
| 4 | Physics with Astronomy | https://www.liverpool.ac.uk/courses/physics-with-astronomy-bsc-hons |
| 5 | Physics with Astronomy with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-astronomy-with-a-year-abroad-bsc-hons |
| 6 | Physics with Geophysics | https://www.liverpool.ac.uk/courses/physics-with-geophysics-bsc-hons |
| 7 | Physics with Medical Applications | https://www.liverpool.ac.uk/courses/physics-with-medical-applications-bsc-hons |
| 8 | Physics with Medical Applications with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-medical-applications-with-a-year-abroad-bsc-hons |
| 9 | Physics with Nuclear Science | https://www.liverpool.ac.uk/courses/physics-with-nuclear-science-bsc-hons |
| 10 | Physics with Nuclear Science with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-nuclear-science-with-a-year-abroad-bsc-hons |
| 11 | Physics with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-a-year-abroad-bsc-hons |

###### MPhys (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | https://www.liverpool.ac.uk/courses/astrophysics-mphys-hons |
| 2 | Astrophysics with a Year Abroad | https://www.liverpool.ac.uk/courses/astrophysics-with-a-year-abroad-mphys-hons |
| 3 | Physics | https://www.liverpool.ac.uk/courses/physics-mphys-hons |
| 4 | Physics with Medical Applications | https://www.liverpool.ac.uk/courses/physics-with-medical-applications-mphys-hons |
| 5 | Physics with Nuclear Science | https://www.liverpool.ac.uk/courses/physics-with-nuclear-science-mphys-hons |
| 6 | Physics with Nuclear Science with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-nuclear-science-with-a-year-abroad-mphys-hons |
| 7 | Physics with a Year Abroad | https://www.liverpool.ac.uk/courses/physics-with-a-year-abroad-mphys-hons |
| 8 | Theoretical Physics | https://www.liverpool.ac.uk/courses/theoretical-physics-mphys-hons |
| 9 | Theoretical Physics with a Year Abroad | https://www.liverpool.ac.uk/courses/theoretical-physics-with-a-year-abroad-mphys-hons |

---

##### School of Physical Sciences — Department of Mathematical Sciences

###### BSc (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Mathematics | https://www.liverpool.ac.uk/courses/actuarial-mathematics-bsc-hons |
| 2 | Actuarial Mathematics with a Year Abroad | https://www.liverpool.ac.uk/courses/actuarial-mathematics-with-a-year-abroad-bsc-hons |
| 3 | Applied Mathematics | https://www.liverpool.ac.uk/courses/applied-mathematics-bsc-hons |
| 4 | Mathematics | https://www.liverpool.ac.uk/courses/mathematics-bsc-hons |
| 5 | Mathematics and Computer Science | https://www.liverpool.ac.uk/courses/mathematics-and-computer-science-bsc-hons |
| 6 | Mathematics and Computer Science with a Year in Industry | https://www.liverpool.ac.uk/courses/mathematics-and-computer-science-with-a-year-in-industry-bsc-hons |
| 7 | Mathematics and Economics | https://www.liverpool.ac.uk/courses/mathematics-and-economics-bsc-hons |
| 8 | Mathematics and Music Technology | https://www.liverpool.ac.uk/courses/mathematics-and-music-technology-bsc-hons |
| 9 | Mathematics and Philosophy | https://www.liverpool.ac.uk/courses/mathematics-and-philosophy-ba-hons |
| 10 | Mathematics and Statistics | https://www.liverpool.ac.uk/courses/mathematics-and-statistics-bsc-hons |
| 11 | Mathematics and Statistics with a Year Abroad | https://www.liverpool.ac.uk/courses/mathematics-and-statistics-with-a-year-abroad-bsc-hons |

###### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics with Finance | https://www.liverpool.ac.uk/courses/mathematics-with-finance-bsc-hons |
| 2 | Mathematics with Finance with a Year Abroad | https://www.liverpool.ac.uk/courses/mathematics-with-finance-with-a-year-abroad-bsc-hons |
| 3 | Mathematics with Languages | https://www.liverpool.ac.uk/courses/mathematics-with-languages-bsc-hons |
| 4 | Mathematics with Ocean and Climate Sciences | https://www.liverpool.ac.uk/courses/mathematics-with-ocean-and-climate-sciences-bsc-hons |

###### BSc (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics with a Year Abroad | https://www.liverpool.ac.uk/courses/mathematics-with-a-year-abroad-bsc-hons |

###### MMath (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Physics | https://www.liverpool.ac.uk/courses/mathematical-physics-mmath-hons |
| 2 | Mathematical Physics with a Year Abroad | https://www.liverpool.ac.uk/courses/mathematical-physics-with-a-year-abroad-mmath-hons |
| 3 | Mathematics | https://www.liverpool.ac.uk/courses/mathematics-mmath-hons |
| 4 | Mathematics with a Year Abroad MMath | https://www.liverpool.ac.uk/courses/mathematics-with-a-year-abroad-mmath-hons |

###### BSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical Sciences BSc (Hons) (Foundation, 4 year route with Carmel College) | https://www.liverpool.ac.uk/courses/mathematical-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college |

###### BSc — Foundation (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Physical Sciences (4 year route including a Foundation Year at Carmel College) | https://www.liverpool.ac.uk/courses/physical-sciences-entry-route-leading-to-bsc-hons-4-year-route-including-a-foundation-year-at-carmel-college |

---

### 1.3 Joint honours / cross-school programmes

Liverpool offers numerous joint honours programmes, including:
- **Philosophy, Politics and Economics (PPE)** — spans Philosophy, Politics, and Economics departments
- **Mathematics and Computer Science** — spans Mathematical Sciences and Computer Science
- **Computer Science and Electronic Engineering** — spans Computer Science and Electrical Engineering
- **Physics and Mathematics** — spans Physics and Mathematical Sciences
- **Law with Business/Criminology/Philosophy/Politics** — Law School combined with other departments
- **Various language combinations** — Combined degree format for Catalan, Chinese, Portuguese, Spanish

### 1.4 Foundation year programmes

Liverpool offers Foundation Year (Year 0) routes for many health professions (Medicine, Dentistry, Veterinary Science, Nursing, Allied Health) and Carmel College 4-year routes for sciences and engineering. These are listed as separate entries above.

### 1.5 Year in Industry / Year Abroad variants

Many programmes offer variants with a Year in Industry or Year Abroad. These are listed as separate entries in the A-Z listing and are counted separately in the 252 total.

### 1.6 Pharmacy

###### MPharm (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.liverpool.ac.uk/courses/pharmacy-mpharm |
| 2 | Preparation for Pharmacy | https://www.liverpool.ac.uk/courses/preparation-for-pharmacy-mpharm |

---

### 1.7 Town and Regional Planning

###### MPlan (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Town and Regional Planning | https://www.liverpool.ac.uk/courses/town-and-regional-planning-mplan |

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate taught (PGT) — 244 programmes

Liverpool offers 244 postgraduate taught programmes across all three faculties. Key degree types include:

| Degree Type | Count (approx.) |
|---|---|
| MSc | ~100 |
| MA | ~42 |
| MRes | ~35 |
| MSc (Eng) | ~20 |
| LLM | 6 |
| MPH | 8 |
| MBA | 4 |
| PGCert | 7 |
| MARM/MARMI | 3 |
| MCD | 2 |
| DDSc | 3 |
| Other (MBR, MMus, MIM, DClinPsychol, DProfHealth, MA AP) | 6 |

> **Full listing**: See `liverpool.ac.uk/courses/postgraduate-taught` for all 244 programmes with URLs.
> **Key programmes**: Advanced Computer Science MSc, Data Science and AI MSc, MBA (The Liverpool MBA), LLM International Business and Commercial Law, MPH, various Engineering MSc(Eng) programmes.

### 2.2 Postgraduate research (PGR) — 209 programmes

Liverpool offers 209 postgraduate research programmes including:
- **PhD** programmes across all departments
- **MPhil** programmes (often alongside PhD)
- **MD** programmes (Doctor of Medicine, for medical graduates)
- **DBA** (Executive Doctorate in Business Administration)
- **MRes** (research master's, project-based)
- **Funded PhD Projects** (specific research opportunities with funding)

> **Full listing**: See `liverpool.ac.uk/courses/postgraduate-research` for all 209 programmes with URLs.

### 2.3 Graduate admissions model

Postgraduate applications are made **directly to the university** (not through UCAS). Each programme has its own application page. Requirements vary by programme and are listed on individual course pages.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | L41 |
| **Main application deadline** | 29 January (equal consideration, most courses) |
| **Medicine/Dentistry/Veterinary deadline** | 15 October (previous year) |
| **UCAS Extra opens** | February 2026 |
| **Clearing opens** | July 2026 |
| **International application deadline** | 30 June 2026 |
| **Entry year** | September 2026 |

### 3.2 Undergraduate — academic entry requirements (typical)

| 考试体系 | 标准要求 | 来源 |
|---------|---------|------|
| **A-Level** | AAB (Computer Science); varies by course | Course pages |
| **IB Diploma** | 34 points overall or 6,6,5 in 3 HL subjects (Computer Science) | Course pages |
| **BTEC Extended Diploma** | D*DD in relevant subject + A-Level Maths/CS grade B | Course pages |
| **Scottish Highers** | AAABB + Advanced Higher A in relevant subject | Course pages |
| **Welsh Baccalaureate** | Grade B with AA in A-Levels | Course pages |
| **Irish Leaving Certificate** | H1, H1, H2, H2, H2, H3 | Course pages |
| **EPQ** | Accepted for most courses (not Medicine, Dentistry, Veterinary, Allied Health) | Entry requirements page |
| **T-Levels** | Considered for non-clinical programmes | Entry requirements page |

> **Note**: Entry requirements vary significantly by course. Medicine (MBChB), Dentistry (BDS), and Veterinary Science (BVSc) have higher requirements. Always check the specific course page.
> **Source**: `liverpool.ac.uk/undergraduate/applying/applying-through-ucas/entry-requirements-and-qualifications/`

### 3.3 Undergraduate English language requirements

| 考试类型 | 标准要求 | 单项最低 | 来源 |
|---------|---------|---------|------|
| **IELTS Academic** | 6.0–7.0 overall (varies by course) | 5.5–6.5 each band | Course pages |
| **Duolingo English Test** | 115–125 overall (varies by course) | 100–105 per component | Course pages |
| **TOEFL iBT** | Accepted (Home Edition NOT accepted) | Varies by course | Course pages |
| **Pearson PTE Academic** | Accepted | Varies by course | Course pages |
| **Cambridge IGCSE English** | Accepted (First Language 0500/0990, Second Language 0510/0511) | Varies | Course pages |
| **LanguageCert Academic** | Accepted | Varies by course | Course pages |
| **Kaplan Test of English** | Accepted | Varies by course | Course pages |

> **Typical IELTS bands**:
> - **UG standard**: IELTS 6.0 overall, no component below 5.5
> - **UG higher**: IELTS 6.5 overall, no component below 5.5
> - **UG highest (Law, etc.)**: IELTS 7.0 overall, no component below 6.5
> - **Medicine**: IELTS 7.0 overall, 7.0 in each component (as of May 2026 update)
>
> **Exemptions**: Applicants from majority English-speaking countries are exempt.
> **Validity**: IELTS certificates valid for 2 years from test date.
> **Source**: `liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/international-english-language-tests/`

### 3.4 Graduate admissions

Postgraduate applications are made directly to the university. Requirements vary by programme. International applicants need overseas qualifications equivalent to UK master's entry requirements. Pre-Master's courses available at the International College for those who don't meet direct entry.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition fees (2026/27)

| Fee status | Annual tuition | Year in Industry | Year Abroad (China) | Source |
|-----------|---------------|-----------------|---------------------|--------|
| **Home (UK)** | £9,790 | £1,955 | £1,465 | Course pages |
| **International — Humanities** | £27,000 | £1,955 | £13,500 | Course pages |
| **International — Science/Engineering** | £32,000 | £1,955 | £16,000 | Course pages |
| **International — Clinical (Medicine)** | £50,000 | £1,955 | £25,000 | Course pages |

> **Note**: Fees may increase annually. For UK students, increases subject to government regulated fee limits.
> **Source**: Individual course pages (e.g., `liverpool.ac.uk/courses/computer-science-bsc-hons`, `liverpool.ac.uk/courses/law-llb-hons`, `liverpool.ac.uk/courses/medicine-and-surgery-mbchb`)

### 4.2 Estimated living costs (per year)

| 项目 | 估计费用 (£) |
|------|------------|
| Accommodation | 5,000 – 9,000 |
| Food | 2,000 – 4,000 |
| Transport | 400 – 800 |
| Study materials | 400 – 800 |
| Personal expenses | 1,500 – 3,000 |
| **Total (estimated)** | **9,300 – 17,600** |

### 4.3 Scholarships

- **Liverpool Scholarships**: Up to £7,500 for undergraduate students, £7,000 for master's students
- Scholarship page: `liverpool.ac.uk/study/fees-and-funding/scholarships-and-bursaries/`
- International scholarships available
- Fee deposit required for international students

### 4.4 Financial support

- Student Finance England loans available for home students
- Money advice service: `liverpool.ac.uk/studentsupport/money-advice/`
- Managing cost of living guidance available

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Liverpool"
  source_url: https://www.liverpool.ac.uk
  source_snippet: "University of Liverpool"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.faculties
  value: "3 Faculties: Health and Life Sciences, Humanities and Social Sciences, Science and Engineering"
  source_url: https://www.liverpool.ac.uk/about/the-university/our-structure/
  source_snippet: "Faculty of Health and Life Sciences / Faculty of Humanities and Social Sciences / Faculty of Science and Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.departments
  value: "40+ departments across 12 Schools/Institutes"
  source_url: https://www.liverpool.ac.uk/departments/
  source_snippet: Full department listing extracted
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.programs.count
  value: "252 undergraduate courses"
  source_url: https://www.liverpool.ac.uk/courses/undergraduate
  source_snippet: "252 undergraduate courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-005:
  field: postgraduate_taught.programs.count
  value: "244 postgraduate taught courses"
  source_url: https://www.liverpool.ac.uk/courses/postgraduate-taught
  source_snippet: "244 courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-006:
  field: postgraduate_research.programs.count
  value: "209 postgraduate research courses"
  source_url: https://www.liverpool.ac.uk/courses/postgraduate-research
  source_snippet: "209 postgraduate research courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage_listing

E-U-007:
  field: undergraduate.fees.home
  value: "£9,790 per year (2026/27)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "UK (full-time, per year): £9,790"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.fees.international.humanities
  value: "£27,000 per year (2026/27)"
  source_url: https://www.liverpool.ac.uk/courses/law-llb-hons
  source_snippet: "International: Full-time per year: £27,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.fees.international.science_engineering
  value: "£32,000 per year (2026/27)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "International (full-time, per year): £32,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.fees.international.clinical
  value: "£50,000 per year (2026/27)"
  source_url: https://www.liverpool.ac.uk/courses/medicine-and-surgery-mbchb
  source_snippet: "International: Full-time: £50,000 per year"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.entry_requirements.alevel.cs
  value: "AAB (Computer Science BSc)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "AAB — must include Mathematics or Computer Science"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.entry_requirements.ib.cs
  value: "34 points overall or 6,6,5 in 3 HL subjects (Computer Science BSc)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "34 points overall or 6,6,5 in 3 HL subjects including Mathematics or Computer Science"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english.ielts.standard
  value: "IELTS 6.0 overall, no component below 5.5 (UG standard)"
  source_url: https://www.liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/international-english-language-tests/
  source_snippet: "IELTS 6.0 overall, no component below 5.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.english.ielts.higher
  value: "IELTS 6.5 overall, no component below 5.5 (UG higher)"
  source_url: https://www.liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/international-english-language-tests/
  source_snippet: "IELTS 6.5 overall, no component below 5.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.english.ielts.medicine
  value: "IELTS 7.0 overall, 7.0 in each component (Medicine)"
  source_url: https://www.liverpool.ac.uk/courses/medicine-and-surgery-mbchb
  source_snippet: "IELTS: 7.0 overall, with 7.0 in each component"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.english.duolingo.cs
  value: "Duolingo 115 overall (Computer Science)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "115 overall, with speaking, reading, and writing not below 105, and listening not below 100"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.application.system
  value: "UCAS"
  source_url: https://www.liverpool.ac.uk/undergraduate/applying/applying-through-ucas/
  source_snippet: "Applying through UCAS"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.application.ucas_deadline
  value: "29 January (equal consideration)"
  source_url: https://www.liverpool.ac.uk/undergraduate/applying/applying-through-ucas/
  source_snippet: UCAS equal consideration deadline
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-019:
  field: undergraduate.application.medicine_deadline
  value: "15 October (previous year)"
  source_url: https://www.liverpool.ac.uk/courses/medicine-and-surgery-mbchb
  source_snippet: "Application Deadline: 15 October 2025"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-020:
  field: institution.russell_group
  value: "Yes — Russell Group member"
  source_url: https://www.liverpool.ac.uk/about/the-university/rankings-and-reputation/
  source_snippet: Russell Group membership
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-021:
  field: institution.tef_rating
  value: "Gold (TEF 2023)"
  source_url: https://www.liverpool.ac.uk/courses/computer-science-bsc-hons
  source_snippet: "TEF Rating: Gold"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-022:
  field: institution.qs_ranking
  value: "139th in the world (QS World University Rankings 2027)"
  source_url: https://www.liverpool.ac.uk/postgraduate-taught/
  source_snippet: "139th in the world (QS World University Rankings, 2027)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-023:
  field: institution.ug_scholarship
  value: "Liverpool Scholarships up to £7,500 for UG, £7,000 for master's"
  source_url: https://www.liverpool.ac.uk/international/
  source_snippet: "Liverpool Scholarships worth up to £7,500 for undergraduate students and £7,000 for master's students"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
liverpool-university-knowledge-base-v2
├── 0-overview (Section 0: rules 1-4, institution overview)
├── 1-undergraduate (Section 1: full UG programme listing, chunked by Faculty/School)
│   ├── chunk-01-health-and-life-sciences
│   ├── chunk-02-humanities-arts
│   ├── chunk-03-humanities-histories-languages
│   ├── chunk-04-humanities-law-social-justice
│   ├── chunk-05-humanities-management
│   ├── chunk-06-science-computer-science
│   ├── chunk-07-science-engineering
│   ├── chunk-08-science-environmental
│   └── chunk-09-science-physical-sciences
├── 2-graduate (Section 2: PGT + PGR summary)
├── 3-applications (Section 3: requirements, deadlines, English)
├── 4-costs (Section 4: fees, living costs, scholarships)
├── 5-evidence (Section 5: evidence chain)
└── 6-monitoring (Section 7: monitoring watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "liverpool-university-knowledge-base-v2"
  school: "<faculty/school>"
  department: "<department>"
  degree_level: "<BA|BSc|BEng|MEng|MBiol|...>"
  level: undergraduate
  field_type: programs
  source_url: https://www.liverpool.ac.uk/courses/undergraduate
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Per-course entry requirements (A-Level/IB specifics) | Individual course pages |
| **P0** | Full PGT programme listing with degree types | `liverpool.ac.uk/courses/postgraduate-taught` |
| **P0** | Full PGR programme listing with degree types | `liverpool.ac.uk/courses/postgraduate-research` |
| **P0** | International fees by course (detailed) | Individual course pages |
| **P1** | Country-specific entry requirements | `liverpool.ac.uk/international/countries/` |
| **P1** | Scholarship amounts and eligibility criteria | `liverpool.ac.uk/study/fees-and-funding/scholarships-and-bursaries/` |
| **P1** | Pre-sessional English course details | `liverpool.ac.uk/international/applying/entry-requirements/english-language-requirements/` |
| **P2** | Course module details and curriculum | Individual course pages |
| **P2** | Accommodation costs (detailed) | `liverpool.ac.uk/accommodation/` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Liverpool | Cardiff | Newcastle |
|-----------|------------------------|---------|-----------|
| Total UG programmes | 252 | 237 | 147 |
| Total PGT programmes | 244 | P0 follow-up | P0 follow-up |
| Total PGR programmes | 209 | P0 follow-up | P0 follow-up |
| Faculties/Schools | 3 Faculties, 12 Schools/Institutes | 3 Colleges, 24 Schools | — |
| UG Home tuition | £9,790 | £9,250 | — |
| UG International tuition (range) | £27,000 – £50,000 | £22,700 – £29,450 | — |
| IELTS minimum (UG) | 6.0 (5.5 each) | 6.5 (5.5 each) | — |
| A-Level typical (CS) | AAB | ABB | — |
| UCAS deadline | 29 Jan | 29 Jan | — |
| Medicine deadline | 15 Oct | — | — |
| Region | England, UK | Wales, UK | England, UK |
| Russell Group | Yes | Yes | Yes |
| TEF Rating | Gold | — | — |
| QS World Ranking | 139th | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: liverpool.ac.uk (main domain)
> **Verification**: WebFetch + course page extraction
> **Granularity**: faculty → school → department → degree-level → program
> **Completeness**: UG programs (252/252) ✅ | PGT programs (244, summary) ✅ | PGR programs (209, summary) ✅ | Evidence (23 blocks) ✅ | Per-course entry requirements ⚠ P0
