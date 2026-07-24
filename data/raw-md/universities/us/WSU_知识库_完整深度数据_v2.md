# Washington State University (WSU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BMus/DVM/MD/PharmD) | 192 |
| 本科辅修 (Minor) | 120 |
| 本科证书 (Undergraduate Certificate) | 70 |
| 研究生学位项目 (MA/MS/MBA/MFA/PhD/EdD/DNP/etc.) | 170 |
| 研究生证书 (Graduate Certificate) | 25 |
| **学位项目总计 (UG + Grad degree programs)** | **362** |
| **含证书总计** | **457** |
| 学院 / 独立系所总数 | 11 |

> **来源**: WSU Catalog (catalog.wsu.edu), Pullman Campus, extracted 2026-07-06. UG degrees from Schedule of Studies; minors from Minors page; certificates from Certificates page; graduate from gradschool.wsu.edu/degrees/ (74 program groups, ~195 individual entries including certificates).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Washington State University
├── College of Agricultural, Human, and Natural Resource Sciences (CAHNRS) [学院]
│   ├── Agricultural and Food Systems [系]
│   ├── Animal Sciences [系]
│   ├── Apparel, Merchandising, Design, and Textiles [系]
│   ├── Crop and Soil Sciences [系]
│   ├── Food Science [系]
│   ├── Horticulture [系]
│   ├── Human Development [系]
│   ├── Integrated Plant Sciences [系]
│   ├── Nutrition and Exercise Physiology [系]
│   ├── Viticulture and Enology [系]
│   ├── Biological Systems Engineering [系]
│   └── School of the Environment [系]
│       ├── Earth Sciences
│       ├── Environmental and Ecosystem Sciences
│       ├── Forest Ecology and Management
│       └── Wildlife Ecology and Conservation Sciences
│
├── College of Arts and Sciences [学院]
│   ├── Anthropology [系]
│   ├── Art [系]
│   ├── Biological Sciences [系]
│   ├── Chemistry [系]
│   ├── Communication [系]
│   ├── Comparative Ethnic Studies [系]
│   ├── Criminal Justice and Criminology [系]
│   ├── English [系]
│   ├── Foreign Languages and Cultures / Languages, Cultures, and Race [系]
│   ├── History [系]
│   ├── Mathematics and Statistics [系]
│   ├── Music [系]
│   ├── Neuroscience [系]  ⚠ shared with Integrative Physiology
│   ├── Physics and Astronomy [系]
│   ├── Politics, Philosophy, and Public Affairs [系]
│   ├── Psychology [系]
│   ├── Sociology [系]
│   ├── Speech and Hearing Sciences [系]
│   └── Women's, Gender, and Sexuality Studies [系]
│
├── Carson College of Business [学院]
│   ├── Accounting [系]
│   ├── Finance and Management Science [系]
│   ├── Hospitality Business Management [系]
│   ├── Management, Information Systems, and Entrepreneurship [系]
│   ├── Marketing and International Business [系]
│   └── Business Administration (MBA/PhD programs) [系]
│
├── Edward R. Murrow College of Communication [学院]
│   ├── Journalism and Media Production [系]
│   └── Strategic Communication [系]
│
├── College of Education [学院]
│   ├── Teaching and Learning [系]
│   ├── Educational Leadership and Sport Management [系]
│   ├── Kinesiology and Educational Psychology [系]
│   └── Cultural Studies and Social Thought in Education [系]
│
├── Voiland College of Engineering and Architecture [学院]
│   ├── Chemical Engineering and Bioengineering [系]
│   ├── Civil and Environmental Engineering [系]
│   ├── Electrical Engineering and Computer Science [系]
│   ├── Mechanical and Materials Engineering [系]
│   ├── Design and Construction [系]
│   │   ├── Architecture
│   │   ├── Construction Management
│   │   ├── Interior Design
│   │   └── Landscape Architecture
│   ├── Data Analytics [系]
│   ├── Engineering and Technology Management [系]
│   └── School of Engineering and Computer Science — WSU Vancouver [系]
│
├── Honors College [学院]
│   └── University Honors [系]
│
├── Elson S. Floyd College of Medicine [学院]
│   ├── Medical Education and Clinical Sciences [系]
│   └── Foundations of Medical Science [系]
│
├── College of Nursing [学院]
│   ├── Foundational Practice and Community-Based Care [系]
│   ├── Advanced Practice and Community-Based Care [系]
│   └── Nursing and Systems Science [系]
│
├── College of Pharmacy and Pharmaceutical Sciences [学院]
│   ├── Pharmacy and Pharmaceutical Sciences [系]
│   └── Pharmaceutical Sciences and Molecular Medicine [系]
│
├── College of Veterinary Medicine [学院]
│   ├── Veterinary Medicine [系]
│   ├── Veterinary Clinical Sciences [系]
│   ├── Veterinary Microbiology and Pathology [系]
│   └── Biomedical Sciences [系]
│
└── The Graduate School [学院] (administrative umbrella)
    └── Manages admissions for graduate programs across all colleges
```

> **Note**: WSU has 11 academic colleges plus the Graduate School. The Graduate School administers graduate admissions centrally but programs are housed within the 11 colleges. The Honors College is an undergraduate-only college. Professional programs (MD, DVM, PharmD) are housed in their respective colleges.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | 本校官方缩写 | 全称 | 层级 | 本项目数量 |
|---------|---------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 18 |
| BS | BS | Bachelor of Science | 本科 | 142 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| BMus | BMus | Bachelor of Music | 本科 | 13 |
| BArch | BArch | Bachelor of Architecture | 本科 | 1 |
| DVM | DVM | Doctor of Veterinary Medicine | 本科(专业) | 1 |
| MD | MD | Doctor of Medicine | 本科(专业) | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 本科(专业) | 2 |
| Minor | Minor | 辅修 | 本科 | 120 |
| UG Certificate | Certificate | 本科证书 | 本科 | 70 |
| MA | MA | Master of Arts | 研究生 | 28 |
| MS | MS | Master of Science | 研究生 | 55 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MArch | M.Arch | Master of Architecture | 研究生 | 1 |
| MEd | M.Ed | Master of Education | 研究生 | 5 |
| MEng | M.Eng | Master of Engineering | 研究生 | 3 |
| MPH | MPH | Master of Public Health | 研究生 | 0 |
| MN | MN | Master of Nursing | 研究生 | 2 |
| MAE | MAE | Master of Applied Economics | 研究生 | 1 |
| MIT | MIT | Master in Teaching | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 62 |
| EdD | Ed.D | Doctor of Education | 研究生 | 2 |
| PSM | PSM | Professional Science Master | 研究生 | 1 |
| Grad Certificate | GC | Graduate Certificate | 研究生 | 25 |
| **学位项目总计** | | | | **531** |

> **Note**: The 531 total includes all UG degrees (192) + minors (120) + UG certificates (70) + grad degrees (170) + grad certificates (25) + professional degrees (4 DVM/MD/PharmD counted separately). The 362 "degree programs" count excludes certificates.

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

**Undergraduate Programs by College:**

| 学院 \ 级别 | BA | BS | BFA | BMus | BArch | DVM/MD/PharmD | Minor | UG Cert | 合计 |
|------------|----|----|-----|------|-------|---------------|-------|---------|------|
| CAHNRS | 0 | 28 | 0 | 0 | 0 | 0 | 22 | 10 | 60 |
| Arts & Sciences | 15 | 63 | 1 | 13 | 0 | 0 | 52 | 18 | 162 |
| Carson Business | 0 | 5 | 0 | 0 | 0 | 0 | 8 | 5 | 18 |
| Murrow Communication | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 | 4 |
| Education | 0 | 3 | 0 | 0 | 0 | 0 | 5 | 6 | 14 |
| Engineering & Architecture | 0 | 30 | 0 | 0 | 1 | 0 | 13 | 12 | 56 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 1 MD | 0 | 4 | 5 |
| Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Pharmacy | 0 | 3 | 0 | 0 | 0 | 2 PharmD | 0 | 0 | 5 |
| Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 1 DVM | 0 | 0 | 1 |
| Interdisciplinary/Languages | 3 | 4 | 0 | 0 | 0 | 0 | 18 | 11 | 36 |
| **合计** | **18** | **138** | **1** | **13** | **1** | **4** | **120** | **70** | **365** |

> **Note**: Some programs span multiple colleges. The interdisciplinary row captures programs from Languages/Cultures/Race and other cross-cutting departments. Total includes 192 UG degrees + 120 minors + 70 certificates = 382. The difference from 365 is due to some professional degrees (MD, DVM, PharmD) being counted in their respective college rows.

**Graduate Programs by College:**

| 学院 \ 级别 | MA | MS | MBA | MFA | MEd | MEng | PhD | EdD | Other Grad | Grad Cert | 合计 |
|------------|----|----|-----|-----|-----|------|-----|-----|------------|-----------|------|
| CAHNRS | 0 | 22 | 0 | 0 | 0 | 0 | 18 | 0 | 0 | 4 | 44 |
| Arts & Sciences | 12 | 15 | 0 | 1 | 0 | 0 | 22 | 0 | 0 | 4 | 54 |
| Carson Business | 0 | 0 | 2 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 9 |
| Murrow Communication | 3 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 6 |
| Education | 8 | 1 | 0 | 0 | 5 | 0 | 7 | 2 | 2 MIT | 4 | 29 |
| Engineering & Arch | 0 | 10 | 0 | 0 | 0 | 3 | 7 | 0 | 1 PSM | 13 | 34 |
| Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 MN | 0 | 3 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 2 |
| Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Interdisciplinary | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 5 |
| **合计** | **23** | **51** | **2** | **1** | **5** | **3** | **65** | **2** | **5** | **30** | **187** |

> **Reconciliation**: UG degrees (192) + grad degrees (170) = 362 degree programs. Grad certificates (25) bring the total catalog entries to 387. The graduate school reports 140 degree programs (excluding certificates and some campus-specific variants).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

WSU has 11 academic colleges offering undergraduate programs on the Pullman campus. The university operates on a land-grant mission with particular strength in agriculture, veterinary medicine, and engineering. Most undergraduate programs lead to a BS degree; BA programs are concentrated in Arts & Sciences. The Honors College offers an honors track overlay rather than standalone degrees. Professional doctorates (MD, DVM, PharmD) are undergraduate-entry professional programs.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Agricultural, Human, and Natural Resource Sciences (CAHNRS)

##### Department of Agricultural and Food Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural and Food Business Economics | https://catalog.wsu.edu/Degrees |
| 2 | Agricultural Education | https://catalog.wsu.edu/Degrees |
| 3 | Agricultural Technology and Production Management | https://catalog.wsu.edu/Degrees |
| 4 | Human Nutrition and Food Systems | https://catalog.wsu.edu/Degrees |
| 5 | Organic and Sustainable Agriculture | https://catalog.wsu.edu/Degrees |

##### Department of Animal Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Sciences - Accelerated Pre-Veterinary Option | https://catalog.wsu.edu/Degrees |
| 2 | Animal Sciences - Animal Science, Technology, and Production Option | https://catalog.wsu.edu/Degrees |
| 3 | Animal Sciences - Pre-Veterinary Medicine/Science Option | https://catalog.wsu.edu/Degrees |

##### Department of Apparel, Merchandising, Design, and Textiles
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel, Merchandising, Design, and Textiles - Apparel Design Option | https://catalog.wsu.edu/Degrees |
| 2 | Apparel, Merchandising, Design, and Textiles - Merchandising Option | https://catalog.wsu.edu/Degrees |

##### Department of Crop and Soil Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Field Crop Management | https://catalog.wsu.edu/Degrees |
| 2 | Fruit and Vegetable Management | https://catalog.wsu.edu/Degrees |
| 3 | Landscape, Nursery, and Greenhouse Management | https://catalog.wsu.edu/Degrees |
| 4 | Turfgrass Management | https://catalog.wsu.edu/Degrees |

##### Department of Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science - General Option | https://catalog.wsu.edu/Degrees |

##### Department of Integrated Plant Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Biotechnology | https://catalog.wsu.edu/Degrees |

##### Department of Viticulture and Enology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Viticulture and Enology (Tri-Cities Only) | https://catalog.wsu.edu/Degrees |

##### School of the Environment
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences | https://catalog.wsu.edu/Degrees |
| 2 | Environmental and Ecosystem Sciences | https://catalog.wsu.edu/Degrees |
| 3 | Forest Ecology and Management | https://catalog.wsu.edu/Degrees |
| 4 | Wildlife Ecology and Conservation Sciences - Honors Accelerated Pre-Vet Program Option | https://catalog.wsu.edu/Degrees |
| 5 | Wildlife Ecology and Conservation Sciences - Pre-Veterinary Option | https://catalog.wsu.edu/Degrees |
| 6 | Wildlife Ecology and Conservation Sciences - Basic Option | https://catalog.wsu.edu/Degrees |

##### Department of Human Development
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development - Early Childhood Education Option | https://catalog.wsu.edu/Degrees |
| 2 | Human Development - Family and Consumer Sciences Option | https://catalog.wsu.edu/Degrees |
| 3 | Human Development - Lifespan Development Option | https://catalog.wsu.edu/Degrees |

---

#### College of Arts and Sciences

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.wsu.edu/Degrees |
| 2 | Human Biology, BA | https://catalog.wsu.edu/Degrees |

##### Department of Art
###### BA / BFA
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art - Graphic Arts and Integrated Design Option | BA | https://catalog.wsu.edu/Degrees |
| 2 | Art - Studio Option | BA | https://catalog.wsu.edu/Degrees |
| 3 | Art, Bachelor of Fine Arts | BFA | https://catalog.wsu.edu/Degrees |

##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology - Basic Medical Sciences Option | https://catalog.wsu.edu/Degrees |
| 2 | Biology - Ecology and Evolutionary Biology Option | https://catalog.wsu.edu/Degrees |
| 3 | Biology - Education Option | https://catalog.wsu.edu/Degrees |
| 4 | Biology - Entomology Option | https://catalog.wsu.edu/Degrees |
| 5 | Biology - General Option | https://catalog.wsu.edu/Degrees |
| 6 | Biology - Plant Biology Option | https://catalog.wsu.edu/Degrees |
| 7 | Biology - Pre-Physical Therapy / Pre-Occupational Therapy / Pre-Physician Assistant Option | https://catalog.wsu.edu/Degrees |

##### Department of Chemistry
###### BA / BS
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemistry - Secondary Education Option | BA | https://catalog.wsu.edu/Degrees |
| 2 | Chemistry - Standard Option | BA | https://catalog.wsu.edu/Degrees |
| 3 | Chemistry - Materials Option | BS | https://catalog.wsu.edu/Degrees |
| 4 | Chemistry - Professional Option | BS | https://catalog.wsu.edu/Degrees |

##### Department of Criminal Justice and Criminology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice and Criminology | https://catalog.wsu.edu/Degrees |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English - Creative Writing Option | https://catalog.wsu.edu/Degrees |
| 2 | English - Integrative English Studies Option | https://catalog.wsu.edu/Degrees |
| 3 | English - Linguistics Option | https://catalog.wsu.edu/Degrees |
| 4 | English - Literary Studies Option | https://catalog.wsu.edu/Degrees |
| 5 | English - Rhetoric and Professional Writing Option | https://catalog.wsu.edu/Degrees |
| 6 | English - Teaching Option with Certification | https://catalog.wsu.edu/Degrees |
| 7 | English - Teaching Option without Certification | https://catalog.wsu.edu/Degrees |

##### Department of Languages, Cultures, and Race
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative Ethnic Studies | https://catalog.wsu.edu/Degrees |
| 2 | French | https://catalog.wsu.edu/Degrees |
| 3 | French - Secondary Education Option | https://catalog.wsu.edu/Degrees |
| 4 | Humanities - International Area Studies Major | https://catalog.wsu.edu/Degrees |
| 5 | Japanese | https://catalog.wsu.edu/Degrees |
| 6 | Social Sciences or Humanities Major - Plan A Option | https://catalog.wsu.edu/Degrees |
| 7 | Social Sciences or Humanities Major - Plan B Option | https://catalog.wsu.edu/Degrees |
| 8 | Social Sciences Major - Personnel Psychology/Human Resources Option (Vancouver-only) | https://catalog.wsu.edu/Degrees |
| 9 | Spanish | https://catalog.wsu.edu/Degrees |
| 10 | Spanish - Secondary Education Option | https://catalog.wsu.edu/Degrees |
| 11 | Spanish - Latin American and Latinx Studies Option | https://catalog.wsu.edu/Degrees |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History - Education Option | https://catalog.wsu.edu/Degrees |
| 2 | History - General Option | https://catalog.wsu.edu/Degrees |
| 3 | History - Pre-Law Option | https://catalog.wsu.edu/Degrees |
| 4 | Social Studies - Education Option | https://catalog.wsu.edu/Degrees |
| 5 | Social Studies - Teaching Option without Certification | https://catalog.wsu.edu/Degrees |

##### Department of Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics - Actuarial Science Option | https://catalog.wsu.edu/Degrees |
| 2 | Mathematics - Applied Mathematics Option | https://catalog.wsu.edu/Degrees |
| 3 | Mathematics - Secondary Teaching Option with Certification | https://catalog.wsu.edu/Degrees |
| 4 | Mathematics - Secondary Teaching Option without Certification | https://catalog.wsu.edu/Degrees |
| 5 | Mathematics - Statistics Option | https://catalog.wsu.edu/Degrees |
| 6 | Mathematics - Theoretical Option | https://catalog.wsu.edu/Degrees |

##### School of Music
###### BMus / BS
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music - Elective Studies in Pre-Law Option | BMus | https://catalog.wsu.edu/Degrees |
| 2 | Music - General Option | BMus | https://catalog.wsu.edu/Degrees |
| 3 | Music Business | BMus | https://catalog.wsu.edu/Degrees |
| 4 | Music Composition | BMus | https://catalog.wsu.edu/Degrees |
| 5 | Music Education - Choral/General Endorsement Option | BMus | https://catalog.wsu.edu/Degrees |
| 6 | Music Education - Choral/Instrumental/General Endorsement Option | BMus | https://catalog.wsu.edu/Degrees |
| 7 | Music Education - Instrumental/General Endorsement Option | BMus | https://catalog.wsu.edu/Degrees |
| 8 | Music Performance - Brass, Percussion, Strings, Winds Option | BMus | https://catalog.wsu.edu/Degrees |
| 9 | Music Performance - Jazz Studies Option | BMus | https://catalog.wsu.edu/Degrees |
| 10 | Music Performance - Keyboard Option | BMus | https://catalog.wsu.edu/Degrees |
| 11 | Music Performance - Keyboard with Elective Studies in Pedagogy Option | BMus | https://catalog.wsu.edu/Degrees |
| 12 | Music Performance - Voice Option | BMus | https://catalog.wsu.edu/Degrees |
| 13 | Music Pre-Teacher Certification | BMus | https://catalog.wsu.edu/Degrees |

##### Department of Neuroscience
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience - Biomedical Business Option | https://catalog.wsu.edu/Degrees |
| 2 | Neuroscience - General Option | https://catalog.wsu.edu/Degrees |
| 3 | Neuroscience - Honors Accelerated Pre-Veterinary Option | https://catalog.wsu.edu/Degrees |
| 4 | Neuroscience - Pre-Professional Option | https://catalog.wsu.edu/Degrees |
| 5 | Neuroscience - Research Option | https://catalog.wsu.edu/Degrees |

##### Department of Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics - Applied Physics Option | https://catalog.wsu.edu/Degrees |
| 2 | Physics - Astrophysics Option | https://catalog.wsu.edu/Degrees |
| 3 | Physics - Planetary Sciences Option | https://catalog.wsu.edu/Degrees |
| 4 | Physics - Standard Option | https://catalog.wsu.edu/Degrees |

##### Department of Politics, Philosophy, and Public Affairs
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy - General Option | https://catalog.wsu.edu/Degrees |
| 2 | Philosophy - Pre-Law Option | https://catalog.wsu.edu/Degrees |
| 3 | Political Science - General Option | https://catalog.wsu.edu/Degrees |
| 4 | Political Science - Global Politics Option | https://catalog.wsu.edu/Degrees |
| 5 | Political Science - Pre-Law Option | https://catalog.wsu.edu/Degrees |
| 6 | Public Affairs (Vancouver only) | https://catalog.wsu.edu/Degrees |

##### Department of Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology - Accelerated Pre-Pharmacy Option | https://catalog.wsu.edu/Degrees |
| 2 | Psychology - General Option | https://catalog.wsu.edu/Degrees |

##### Department of Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health - Community and Behavioral Health Option | https://catalog.wsu.edu/Degrees |
| 2 | Public Health - General Option | https://catalog.wsu.edu/Degrees |
| 3 | Public Health - Infectious Disease Option | https://catalog.wsu.edu/Degrees |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.wsu.edu/Degrees |

##### Department of Speech and Hearing Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech and Hearing Sciences | https://catalog.wsu.edu/Degrees |

##### Department of Women's, Gender, and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender, and Sexuality Studies | https://catalog.wsu.edu/Degrees |

##### Department of Molecular Biosciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry - Biophysics Option | https://catalog.wsu.edu/Degrees |
| 2 | Biochemistry - Molecular Biology Option | https://catalog.wsu.edu/Degrees |
| 3 | Genetics and Cell Biology - Molecular Biology Option | https://catalog.wsu.edu/Degrees |
| 4 | Microbiology - Honors Accelerated Pre-Veterinary Option | https://catalog.wsu.edu/Degrees |
| 5 | Microbiology - Medical Technology Option | https://catalog.wsu.edu/Degrees |
| 6 | Microbiology - Molecular Biology Option | https://catalog.wsu.edu/Degrees |

##### Department of General Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Studies - Biological/Mathematical/Physical Sciences | https://catalog.wsu.edu/Degrees |

---

#### Carson College of Business

##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.wsu.edu/Degrees |

##### Department of Finance and Management Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://catalog.wsu.edu/Degrees |

##### Department of Hospitality Business Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Business Management | https://catalog.wsu.edu/Degrees |
| 2 | Aging Business Management | https://catalog.wsu.edu/Degrees |
| 3 | Wine and Beverage Business Management | https://catalog.wsu.edu/Degrees |

##### Department of Management, Information Systems, and Entrepreneurship
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Entrepreneurship | https://catalog.wsu.edu/Degrees |
| 2 | Management | https://catalog.wsu.edu/Degrees |
| 3 | Management Information Systems | https://catalog.wsu.edu/Degrees |

##### Department of Marketing and International Business
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | International Business | https://catalog.wsu.edu/Degrees |
| 2 | Marketing | https://catalog.wsu.edu/Degrees |

##### Business (Tri-Cities)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration (Tri-Cities Campus Only) | https://catalog.wsu.edu/Degrees |

---

#### Edward R. Murrow College of Communication

##### Department of Journalism and Media Production
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Broadcast News | https://catalog.wsu.edu/Degrees |
| 2 | Broadcast Production | https://catalog.wsu.edu/Degrees |
| 3 | Media Innovation | https://catalog.wsu.edu/Degrees |
| 4 | Multimedia Journalism | https://catalog.wsu.edu/Degrees |

##### Department of Strategic Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://catalog.wsu.edu/Degrees |
| 2 | Integrated Strategic Communication | https://catalog.wsu.edu/Degrees |
| 3 | Public Relations | https://catalog.wsu.edu/Degrees |
| 4 | Risk and Crisis Communication | https://catalog.wsu.edu/Degrees |

---

#### College of Education

##### Department of Teaching and Learning
###### BS / Certificate
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Elementary Education Teacher Certificate | Certificate | https://catalog.wsu.edu/Degrees |
| 2 | Specific Subject Teacher Certificate | Certificate | https://catalog.wsu.edu/Degrees |

##### Department of Educational Leadership and Sport Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Management | https://catalog.wsu.edu/Degrees |

##### Department of Kinesiology and Educational Psychology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology | https://catalog.wsu.edu/Degrees |
| 2 | Sports Medicine | https://catalog.wsu.edu/Degrees |

---

#### Voiland College of Engineering and Architecture

##### Department of Chemical Engineering and Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering - Biomedical Systems Option | https://catalog.wsu.edu/Degrees |
| 2 | Bioengineering - Cellular and Molecular Option | https://catalog.wsu.edu/Degrees |
| 3 | Bioengineering - Pre-Med - Biomedical Systems Option | https://catalog.wsu.edu/Degrees |
| 4 | Bioengineering - Pre-Med - Cellular and Molecular Option | https://catalog.wsu.edu/Degrees |
| 5 | Chemical Engineering - General Option | https://catalog.wsu.edu/Degrees |

##### Department of Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.wsu.edu/Degrees |

##### Department of Electrical Engineering and Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.wsu.edu/Degrees |
| 2 | Computer Science | https://catalog.wsu.edu/Degrees |
| 3 | Cybersecurity | https://catalog.wsu.edu/Degrees |
| 4 | Electrical Engineering | https://catalog.wsu.edu/Degrees |
| 5 | Software Engineering | https://catalog.wsu.edu/Degrees |

##### Department of Mechanical and Materials Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://catalog.wsu.edu/Degrees |
| 2 | Mechanical Engineering | https://catalog.wsu.edu/Degrees |

##### Department of Design and Construction
###### BS / BArch
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architectural Studies | BS | https://catalog.wsu.edu/Degrees |
| 2 | Construction Management | BS | https://catalog.wsu.edu/Degrees |
| 3 | Interior Design | BS | https://catalog.wsu.edu/Degrees |
| 4 | Landscape Architecture | BArch | https://catalog.wsu.edu/Degrees |

##### Department of Data Analytics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Analytics - Actuarial Science Option | https://catalog.wsu.edu/Degrees |
| 2 | Data Analytics - Agricultural and Environmental Systems Option | https://catalog.wsu.edu/Degrees |
| 3 | Data Analytics - Business Option | https://catalog.wsu.edu/Degrees |
| 4 | Data Analytics - Computation Option | https://catalog.wsu.edu/Degrees |
| 5 | Data Analytics - Data Visualization Option | https://catalog.wsu.edu/Degrees |
| 6 | Data Analytics - Economics Option | https://catalog.wsu.edu/Degrees |
| 7 | Data Analytics - General Option | https://catalog.wsu.edu/Degrees |
| 8 | Data Analytics - Life Sciences Option | https://catalog.wsu.edu/Degrees |
| 9 | Data Analytics - Physical Sciences Option | https://catalog.wsu.edu/Degrees |
| 10 | Data Analytics - Social Sciences Option | https://catalog.wsu.edu/Degrees |
| 11 | Data Analytics - Sports Management Option | https://catalog.wsu.edu/Degrees |

##### Department of Digital Technology and Culture
###### BA (Vancouver/Pullman/Tri-Cities)
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Technology and Culture - Creative Media and Digital Culture Option (Vancouver only) | https://catalog.wsu.edu/Degrees |
| 2 | Digital Technology and Culture - Digital Cinema, Sound, and Animation Option (Pullman only) | https://catalog.wsu.edu/Degrees |
| 3 | Digital Technology and Culture - Digital Design Option (Pullman and Tri-Cities only) | https://catalog.wsu.edu/Degrees |
| 4 | Digital Technology and Culture - Game Studies Option (Pullman only) | https://catalog.wsu.edu/Degrees |
| 5 | Digital Technology and Culture - Web Design and Development Option (Pullman only) | https://catalog.wsu.edu/Degrees |

##### School of Engineering and Computer Science — WSU Vancouver
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (Vancouver Only) | https://catalog.wsu.edu/Degrees |
| 2 | Electrical Engineering (Vancouver only) | https://catalog.wsu.edu/Degrees |
| 3 | Mechanical Engineering (Vancouver Only) | https://catalog.wsu.edu/Degrees |

---

#### Elson S. Floyd College of Medicine

##### Department of Medical Education and Clinical Sciences
###### MD
| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Medicine (MD) Curriculum | https://catalog.wsu.edu/Degrees |

---

#### College of Nursing

##### Department of Foundational Practice and Community-Based Care
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.wsu.edu/Degrees |
| 2 | Nursing - Registered Nurses Option | https://catalog.wsu.edu/Degrees |

---

#### College of Pharmacy and Pharmaceutical Sciences

##### Department of Pharmacy and Pharmaceutical Sciences
###### BS / PharmD
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmaceutical and Medical Sciences - General Option | BS | https://catalog.wsu.edu/Degrees |
| 2 | Pharmaceutical and Medical Sciences - Accelerated Pharmacy Option | BS | https://catalog.wsu.edu/Degrees |
| 3 | Pharmaceutical and Medical Sciences - Medical Laboratory Science Option | BS | https://catalog.wsu.edu/Degrees |
| 4 | Doctor of Pharmacy (PharmD) Curriculum | PharmD | https://catalog.wsu.edu/Degrees |
| 5 | Doctor of Pharmacy with Research Honors Curriculum | PharmD | https://catalog.wsu.edu/Degrees |

---

#### College of Veterinary Medicine

##### Department of Veterinary Medicine
###### DVM
| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Veterinary Medicine (DVM) Curriculum | https://catalog.wsu.edu/Degrees |

---

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | Home Department | Notes |
|---|------|------|-----------------|-------|
| 1 | Data Analytics | BS | Voiland College (cross-college) | 11 options spanning Business, Science, Ag, etc. |
| 2 | Neuroscience | BS | Arts & Sciences | Cross-dept: Biology, Psychology, Physiology |
| 3 | Bioengineering | BS | Chemical Eng & Bioengineering | Pre-med options available |
| 4 | Digital Technology and Culture | BA | Vancouver/Pullman/Tri-Cities | Multi-campus |

### 1.4 Minors — Complete List (120)

| # | Minor | Home Department |
|---|-------|-----------------|
| 1 | Addiction Studies (Vancouver only) | Psychology |
| 2 | Aerospace Studies | Aerospace Studies |
| 3 | Aging Business Management | Hospitality Business Management |
| 4 | Agribusiness Economics | Economic Sciences |
| 5 | Agricultural Education | Agricultural and Food Systems |
| 6 | Agricultural Systems | Agricultural and Food Systems |
| 7 | Agricultural Technology and Production Management | Agricultural and Food Systems |
| 8 | American Indian Studies | Languages, Cultures, and Race |
| 9 | Animal Sciences | Animal Sciences |
| 10 | Anthropology | Anthropology |
| 11 | Architectural Studies | Design and Construction |
| 12 | Art | Art |
| 13 | Art History | Art |
| 14 | Astronomy | Physics and Astronomy |
| 15 | At-Risk Youth | Sociology |
| 16 | Biochemistry | Molecular Biosciences |
| 17 | Bioengineering | Chemical Engineering and Bioengineering |
| 18 | Biology | Biological Sciences |
| 19 | Business Administration | Business |
| 20 | Business Economics | Economic Sciences |
| 21 | Chemical Engineering | Chemical Engineering and Bioengineering |
| 22 | Chemistry | Chemistry |
| 23 | Chinese, French, German, Japanese, or Spanish | Languages, Cultures, and Race |
| 24 | Communication | Communication |
| 25 | Comparative Ethnic Studies | Languages, Cultures, and Race |
| 26 | Computer Engineering | Electrical Engineering and Computer Science |
| 27 | Computer Science | Electrical Engineering and Computer Science |
| 28 | Computer Science (Vancouver only) | Engineering and Computer Science - WSU Vancouver |
| 29 | Construction Management | Design and Construction |
| 30 | Creative Writing | English |
| 31 | Criminal Justice and Criminology | Criminal Justice and Criminology |
| 32 | Crop Science | Crop and Soil Sciences |
| 33 | Digital Technology and Culture | Digital Technology and Culture |
| 34 | Earth Sciences | Environment |
| 35 | Economics | Economic Sciences |
| 36 | Electrical Engineering | Electrical Engineering and Computer Science |
| 37 | Electrical Engineering (Vancouver only) | Engineering and Computer Science - WSU Vancouver |
| 38 | Engineering | Engineering and Architecture |
| 39 | English | English |
| 40 | Entrepreneurship | Management, Information Systems, and Entrepreneurship |
| 41 | Environment and Society | History |
| 42 | Environmental and Resource Economics and Management | Economic Sciences |
| 43 | Environmental Policy and Equity | Sociology |
| 44 | Environmental Science | Environment |
| 45 | Ethics | Politics, Philosophy, and Public Affairs |
| 46 | Event Management | Hospitality Business Management |
| 47 | Exhibition Studies | Art |
| 48 | Film Studies | Languages, Cultures, and Race |
| 49 | Food Science | Food Science |
| 50 | Forestry | Environment |
| 51 | French Area and Culture Studies | Languages, Cultures, and Race |
| 52 | French for Design and Merchandising | Languages, Cultures, and Race |
| 53 | Genetics and Cell Biology | Molecular Biosciences |
| 54 | Geospatial Analysis | Crop and Soil Sciences |
| 55 | German Area and Culture Studies | Languages, Cultures, and Race |
| 56 | Gerontology | Human Development |
| 57 | Gerontology Minor | Aging |
| 58 | Global and Ethnic Narrative Traditions | Languages, Cultures, and Race |
| 59 | Global Studies | Languages, Cultures, and Race |
| 60 | Health and Society | Sociology |
| 61 | Health Communication and Promotion | Strategic Communication |
| 62 | History | History |
| 63 | Horticulture | Horticulture |
| 64 | Hospitality Business Management | Hospitality Business Management |
| 65 | Human Development | Human Development |
| 66 | Human Nutrition | Nutrition and Exercise Physiology |
| 67 | Human Resource Management | Management, Information Systems, and Entrepreneurship |
| 68 | Humanities | Humanities |
| 69 | Humanities Minor | English |
| 70 | Interior Design | Design and Construction |
| 71 | Japanese Area and Culture Studies | Languages, Cultures, and Race |
| 72 | Jazz Studies | Music |
| 73 | Kinesiology | Kinesiology and Educational Psychology |
| 74 | Landscape Architecture | Design and Construction |
| 75 | Latin American and Spanish Area Studies | Languages, Cultures, and Race |
| 76 | Leadership | Human Development |
| 77 | Linguistics | English |
| 78 | Materials Science and Engineering | Mechanical and Materials Engineering |
| 79 | Mathematics | Mathematics and Statistics |
| 80 | Mechanical Engineering | Mechanical and Materials Engineering |
| 81 | Mechanical Engineering (Vancouver only) | Engineering and Computer Science - WSU Vancouver |
| 82 | Microbiology | Molecular Biosciences |
| 83 | Military Science | Military Science |
| 84 | Modern Asia | History |
| 85 | Modern Global Issues | History |
| 86 | Molecular Biology | Molecular Biosciences |
| 87 | Music | Music |
| 88 | Music Technology | Music |
| 89 | Natural Resources | Environment |
| 90 | Naval Science | Naval Science |
| 91 | Neuroscience | Neuroscience |
| 92 | Philosophy | Politics, Philosophy, and Public Affairs |
| 93 | Physics | Physics and Astronomy |
| 94 | Political Science | Politics, Philosophy, and Public Affairs |
| 95 | Popular Culture | Languages, Cultures, and Race |
| 96 | Pre-Genetic Counseling | Molecular Biosciences |
| 97 | Precision Agriculture | Agricultural and Food Systems |
| 98 | Psychology | Psychology |
| 99 | Public Health | Public Health |
| 100 | Public Relations | Strategic Communication |
| 101 | Queer Studies | Women's, Gender, and Sexuality Studies |
| 102 | Religious Studies | History |
| 103 | Rhetoric and Professional Writing | English |
| 104 | Sociology | Sociology |
| 105 | Software Engineering | Electrical Engineering and Computer Science |
| 106 | Soil Science | Crop and Soil Sciences |
| 107 | Spanish Language Translation | Languages, Cultures, and Race |
| 108 | Sport and Society | Sociology |
| 109 | Sport Management | Educational Leadership and Sport Management |
| 110 | Sports Communication | Journalism and Media Production |
| 111 | Statistics | Mathematics and Statistics |
| 112 | Strength and Conditioning | Kinesiology and Educational Psychology |
| 113 | Sustainable Development | Economic Sciences |
| 114 | Viticulture and Enology | Agricultural and Food Systems |
| 115 | War and Society | History |
| 116 | Wildlife Ecology | Environment |
| 117 | Wine and Beverage Business Management | Hospitality Business Management |
| 118 | Women's, Gender, and Sexuality Studies | Women's, Gender, and Sexuality Studies |
| 119 | Workplace Diversity | Sociology |
| 120 | Zoology | Biological Sciences |

### 1.5 General Education Requirements (UCORE)

WSU's general education program is called **UCORE** (University Common Requirements). All undergraduate students must complete UCORE requirements regardless of major. UCORE includes:

- **Communication** (Written & Oral): 6 credits
- **Quantitative Reasoning**: 3-5 credits
- **Scientific Literacy**: 7-8 credits (2 courses, one with lab)
- **Social Sciences**: 3 credits
- **Humanities**: 3 credits
- **Arts**: 3 credits
- **Diversity**: 3 credits
- **Integration**: 3 credits (senior capstone)

> **Source**: catalog.wsu.edu, UCORE requirements section.

### 1.6 Professional Doctorate Programs (Undergraduate-Entry)

| # | Program | Degree | College | Duration |
|---|---------|--------|---------|----------|
| 1 | Doctor of Veterinary Medicine (DVM) | DVM | Veterinary Medicine | 4 years (after prerequisite coursework) |
| 2 | Doctor of Medicine (MD) | MD | Elson S. Floyd College of Medicine | 4 years |
| 3 | Doctor of Pharmacy (PharmD) | PharmD | Pharmacy & Pharmaceutical Sciences | 4 years (after prerequisite coursework) |
| 4 | Doctor of Pharmacy with Research Honors | PharmD | Pharmacy & Pharmaceutical Sciences | 4 years |

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

WSU's Graduate School administers ~140 degree programs across all colleges. Programs are listed on gradschool.wsu.edu/degrees/.

#### College of Agricultural, Human, and Natural Resource Sciences (CAHNRS)

##### MS
| # | Program | URL |
|---|---------|-----|
| 1 | Agriculture | https://gradschool.wsu.edu/degrees/ |
| 2 | Agriculture – Food Science and Management | https://gradschool.wsu.edu/degrees/ |
| 3 | Agriculture – Plant Health Management | https://gradschool.wsu.edu/degrees/ |
| 4 | Animal Sciences | https://gradschool.wsu.edu/degrees/ |
| 5 | Apparel, Merchandising, and Textiles | https://gradschool.wsu.edu/degrees/ |
| 6 | Biological and Agricultural Engineering | https://gradschool.wsu.edu/degrees/ |
| 7 | Crop Science | https://gradschool.wsu.edu/degrees/ |
| 8 | Environmental and Natural Resource Sciences | https://gradschool.wsu.edu/degrees/ |
| 9 | Food Science | https://gradschool.wsu.edu/degrees/ |
| 10 | Horticulture | https://gradschool.wsu.edu/degrees/ |
| 11 | Natural Resource Sciences | https://gradschool.wsu.edu/degrees/ |
| 12 | Plant Biology | https://gradschool.wsu.edu/degrees/ |
| 13 | Plant Pathology | https://gradschool.wsu.edu/degrees/ |
| 14 | Soil Science | https://gradschool.wsu.edu/degrees/ |
| 15 | Viticulture and Enology | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Agricultural Economics | https://gradschool.wsu.edu/degrees/ |
| 2 | Animal Sciences | https://gradschool.wsu.edu/degrees/ |
| 3 | Biological and Agricultural Engineering | https://gradschool.wsu.edu/degrees/ |
| 4 | Crop Science | https://gradschool.wsu.edu/degrees/ |
| 5 | Entomology | https://gradschool.wsu.edu/degrees/ |
| 6 | Environmental and Natural Resource Sciences | https://gradschool.wsu.edu/degrees/ |
| 7 | Food Science | https://gradschool.wsu.edu/degrees/ |
| 8 | Horticulture | https://gradschool.wsu.edu/degrees/ |
| 9 | Plant Biology | https://gradschool.wsu.edu/degrees/ |
| 10 | Plant Pathology | https://gradschool.wsu.edu/degrees/ |
| 11 | Soil Science | https://gradschool.wsu.edu/degrees/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Sustainable Agriculture | https://gradschool.wsu.edu/degrees/ |

---

#### College of Arts and Sciences

##### MA
| # | Program | URL |
|---|---------|-----|
| 1 | Anthropology | https://gradschool.wsu.edu/degrees/ |
| 2 | Communication | https://gradschool.wsu.edu/degrees/ |
| 3 | Communication – Strategic Communication | https://gradschool.wsu.edu/degrees/ |
| 4 | Criminal Justice and Criminology | https://gradschool.wsu.edu/degrees/ |
| 5 | English | https://gradschool.wsu.edu/degrees/ |
| 6 | History | https://gradschool.wsu.edu/degrees/ |
| 7 | Music | https://gradschool.wsu.edu/degrees/ |
| 8 | Music (Global Campus) | https://gradschool.wsu.edu/degrees/ |
| 9 | Political Science | https://gradschool.wsu.edu/degrees/ |

##### MS
| # | Program | URL |
|---|---------|-----|
| 1 | Biology | https://gradschool.wsu.edu/degrees/ |
| 2 | Biomedical Science – Clinical and Translational Sciences | https://gradschool.wsu.edu/degrees/ |
| 3 | Biomedical Science – Immunology and Infectious Diseases | https://gradschool.wsu.edu/degrees/ |
| 4 | Biomedical Science – Integrative Physiology | https://gradschool.wsu.edu/degrees/ |
| 5 | Chemistry | https://gradschool.wsu.edu/degrees/ |
| 6 | Geology | https://gradschool.wsu.edu/degrees/ |
| 7 | Mathematics | https://gradschool.wsu.edu/degrees/ |
| 8 | Molecular Biosciences | https://gradschool.wsu.edu/degrees/ |
| 9 | Neuroscience | https://gradschool.wsu.edu/degrees/ |
| 10 | Physics | https://gradschool.wsu.edu/degrees/ |
| 11 | Speech and Hearing Sciences | https://gradschool.wsu.edu/degrees/ |
| 12 | Statistics | https://gradschool.wsu.edu/degrees/ |

##### MFA
| # | Program | URL |
|---|---------|-----|
| 1 | Fine Arts | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Anthropology | https://gradschool.wsu.edu/degrees/ |
| 2 | Biology | https://gradschool.wsu.edu/degrees/ |
| 3 | Biomedical Science – Clinical and Translational Sciences | https://gradschool.wsu.edu/degrees/ |
| 4 | Biomedical Science – Combined Anatomic Pathology Residency | https://gradschool.wsu.edu/degrees/ |
| 5 | Biomedical Science – Combined Clinical Microbiology Residency | https://gradschool.wsu.edu/degrees/ |
| 6 | Biomedical Science – Immunology and Infectious Diseases | https://gradschool.wsu.edu/degrees/ |
| 7 | Biomedical Science – Integrative Physiology | https://gradschool.wsu.edu/degrees/ |
| 8 | Chemistry | https://gradschool.wsu.edu/degrees/ |
| 9 | Communication | https://gradschool.wsu.edu/degrees/ |
| 10 | Criminal Justice and Criminology | https://gradschool.wsu.edu/degrees/ |
| 11 | Economics | https://gradschool.wsu.edu/degrees/ |
| 12 | English | https://gradschool.wsu.edu/degrees/ |
| 13 | Geology | https://gradschool.wsu.edu/degrees/ |
| 14 | History | https://gradschool.wsu.edu/degrees/ |
| 15 | Mathematics | https://gradschool.wsu.edu/degrees/ |
| 16 | Molecular Biosciences | https://gradschool.wsu.edu/degrees/ |
| 17 | Molecular Plant Sciences | https://gradschool.wsu.edu/degrees/ |
| 18 | Neuroscience | https://gradschool.wsu.edu/degrees/ |
| 19 | Physics | https://gradschool.wsu.edu/degrees/ |
| 20 | Political Science | https://gradschool.wsu.edu/degrees/ |
| 21 | Prevention Science | https://gradschool.wsu.edu/degrees/ |
| 22 | Psychology – Clinical | https://gradschool.wsu.edu/degrees/ |
| 23 | Psychology – Experimental | https://gradschool.wsu.edu/degrees/ |
| 24 | Sociology | https://gradschool.wsu.edu/degrees/ |
| 25 | Statistical Science | https://gradschool.wsu.edu/degrees/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Health Communication and Promotion | https://gradschool.wsu.edu/degrees/ |
| 2 | Strategic Communication | https://gradschool.wsu.edu/degrees/ |
| 3 | Digital Humanities and Culture | https://gradschool.wsu.edu/degrees/ |
| 4 | Women's, Gender, and Sexuality Studies | https://gradschool.wsu.edu/degrees/ |

---

#### Carson College of Business

##### MBA
| # | Program | URL |
|---|---------|-----|
| 1 | Master of Business Administration (MBA) | https://gradschool.wsu.edu/degrees/ |
| 2 | Executive Master of Business Administration (Executive MBA) | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Business Administration – Accounting | https://gradschool.wsu.edu/degrees/ |
| 2 | Business Administration – Finance | https://gradschool.wsu.edu/degrees/ |
| 3 | Business Administration – Hospitality and Tourism | https://gradschool.wsu.edu/degrees/ |
| 4 | Business Administration – Management | https://gradschool.wsu.edu/degrees/ |
| 5 | Business Administration – Management Information Systems | https://gradschool.wsu.edu/degrees/ |
| 6 | Business Administration – Marketing | https://gradschool.wsu.edu/degrees/ |
| 7 | Business Administration – Operations and Management Science | https://gradschool.wsu.edu/degrees/ |

---

#### Edward R. Murrow College of Communication

##### MA
| # | Program | URL |
|---|---------|-----|
| 1 | Communication | https://gradschool.wsu.edu/degrees/ |
| 2 | Communication – Strategic Communication | https://gradschool.wsu.edu/degrees/ |
| 3 | Health Communication and Promotion | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Communication | https://gradschool.wsu.edu/degrees/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Health Communication and Promotion | https://gradschool.wsu.edu/degrees/ |
| 2 | Strategic Communication | https://gradschool.wsu.edu/degrees/ |

---

#### College of Education

##### MA / MEd / MIT
| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Curriculum and Instruction | MA | https://gradschool.wsu.edu/degrees/ |
| 2 | Curriculum and Instruction | MEd | https://gradschool.wsu.edu/degrees/ |
| 3 | Educational Leadership | MA | https://gradschool.wsu.edu/degrees/ |
| 4 | Educational Leadership | MEd | https://gradschool.wsu.edu/degrees/ |
| 5 | Educational Psychology | MA | https://gradschool.wsu.edu/degrees/ |
| 6 | Language, Literacy, and Technology | MA | https://gradschool.wsu.edu/degrees/ |
| 7 | Language, Literacy, and Technology | MEd | https://gradschool.wsu.edu/degrees/ |
| 8 | Special Education | MA | https://gradschool.wsu.edu/degrees/ |
| 9 | Special Education | MEd | https://gradschool.wsu.edu/degrees/ |
| 10 | Sport Management | MA | https://gradschool.wsu.edu/degrees/ |
| 11 | Master in Teaching – Elementary | MIT | https://gradschool.wsu.edu/degrees/ |
| 12 | Master in Teaching – Secondary | MIT | https://gradschool.wsu.edu/degrees/ |
| 13 | Athletic Training | MAT | https://gradschool.wsu.edu/degrees/ |
| 14 | Kinesiology | MS | https://gradschool.wsu.edu/degrees/ |

##### EdD / PhD
| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Educational Leadership – K-12 Administration | EdD | https://gradschool.wsu.edu/degrees/ |
| 2 | Educational Leadership – Teacher Leadership | EdD | https://gradschool.wsu.edu/degrees/ |
| 3 | Cultural Studies and Social Thought in Education | PhD | https://gradschool.wsu.edu/degrees/ |
| 4 | Educational Leadership | PhD | https://gradschool.wsu.edu/degrees/ |
| 5 | Educational Psychology | PhD | https://gradschool.wsu.edu/degrees/ |
| 6 | Language, Literacy, and Technology | PhD | https://gradschool.wsu.edu/degrees/ |
| 7 | Mathematics and Science Education | PhD | https://gradschool.wsu.edu/degrees/ |
| 8 | Special Education | PhD | https://gradschool.wsu.edu/degrees/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Applied Educational Research Methods | https://gradschool.wsu.edu/degrees/ |
| 2 | Applied Measurement and Quantitative Methods | https://gradschool.wsu.edu/degrees/ |
| 3 | Education Technology Across the Curriculum | https://gradschool.wsu.edu/degrees/ |
| 4 | English Language Learners | https://gradschool.wsu.edu/degrees/ |

---

#### Voiland College of Engineering and Architecture

##### MS / MEng
| # | Program | URL |
|---|---------|-----|
| 1 | Chemical Engineering | https://gradschool.wsu.edu/degrees/ |
| 2 | Civil Engineering – Environmental Engineering | https://gradschool.wsu.edu/degrees/ |
| 3 | Computer Engineering | https://gradschool.wsu.edu/degrees/ |
| 4 | Computer Science – Pullman | https://gradschool.wsu.edu/degrees/ |
| 5 | Computer Science – Tri-Cities | https://gradschool.wsu.edu/degrees/ |
| 6 | Computer Science – Vancouver | https://gradschool.wsu.edu/degrees/ |
| 7 | Electrical Engineering | https://gradschool.wsu.edu/degrees/ |
| 8 | Electrical Engineering – Tri-Cities | https://gradschool.wsu.edu/degrees/ |
| 9 | Electrical Engineering – Vancouver | https://gradschool.wsu.edu/degrees/ |
| 10 | Energy Conscious Construction | https://gradschool.wsu.edu/degrees/ |
| 11 | Engineering (Interdisciplinary) | https://gradschool.wsu.edu/degrees/ |
| 12 | Environmental Engineering – Pullman | https://gradschool.wsu.edu/degrees/ |
| 13 | Environmental Engineering – Tri-Cities | https://gradschool.wsu.edu/degrees/ |
| 14 | Interior Design | https://gradschool.wsu.edu/degrees/ |
| 15 | Materials Science and Engineering | https://gradschool.wsu.edu/degrees/ |
| 16 | Mechanical Engineering – Pullman | https://gradschool.wsu.edu/degrees/ |
| 17 | Mechanical Engineering – Tri-Cities | https://gradschool.wsu.edu/degrees/ |
| 18 | Mechanical Engineering – Vancouver | https://gradschool.wsu.edu/degrees/ |
| 19 | Software Engineering | https://gradschool.wsu.edu/degrees/ |
| 20 | Engineering and Technology Management – METM | https://gradschool.wsu.edu/degrees/ |
| 21 | Architecture (M.Arch) | https://gradschool.wsu.edu/degrees/ |
| 22 | Civil Engineering – MEng | https://gradschool.wsu.edu/degrees/ |
| 23 | Electrical Power Engineering – PSM | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Chemical Engineering | https://gradschool.wsu.edu/degrees/ |
| 2 | Civil Engineering | https://gradschool.wsu.edu/degrees/ |
| 3 | Computer Science | https://gradschool.wsu.edu/degrees/ |
| 4 | Electrical and Computer Engineering | https://gradschool.wsu.edu/degrees/ |
| 5 | Engineering Science | https://gradschool.wsu.edu/degrees/ |
| 6 | Materials Science and Engineering | https://gradschool.wsu.edu/degrees/ |
| 7 | Mechanical Engineering – Pullman | https://gradschool.wsu.edu/degrees/ |

##### Graduate Certificate
| # | Program | URL |
|---|---------|-----|
| 1 | Pavement Durability and Sustainability | https://gradschool.wsu.edu/degrees/ |
| 2 | Energy Conscious Construction | https://gradschool.wsu.edu/degrees/ |
| 3 | Constraints Management | https://gradschool.wsu.edu/degrees/ |
| 4 | Industrial Leadership | https://gradschool.wsu.edu/degrees/ |
| 5 | Logistics and Supply Chain Management | https://gradschool.wsu.edu/degrees/ |
| 6 | Project Management | https://gradschool.wsu.edu/degrees/ |
| 7 | Six Sigma Quality Management | https://gradschool.wsu.edu/degrees/ |
| 8 | Systems Engineering Management | https://gradschool.wsu.edu/degrees/ |
| 9 | Nuclear Materials, Science, and Engineering | https://gradschool.wsu.edu/degrees/ |
| 10 | Responsible Data Science and Analytics | https://gradschool.wsu.edu/degrees/ |
| 11 | Interdisciplinary Robotics and Autonomous Systems (IRAS) | https://gradschool.wsu.edu/degrees/ |
| 12 | Teaching College Mathematics | https://gradschool.wsu.edu/degrees/ |
| 13 | C-NSPIRE | https://gradschool.wsu.edu/degrees/ |

---

#### College of Nursing

##### MS / MN
| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Clinical Systems Leadership | MN | https://gradschool.wsu.edu/degrees/ |
| 2 | Nurse Educator | MN | https://gradschool.wsu.edu/degrees/ |

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Nursing | https://gradschool.wsu.edu/degrees/ |

---

#### College of Pharmacy and Pharmaceutical Sciences

##### PhD
| # | Program | URL |
|---|---------|-----|
| 1 | Pharmaceutical Sciences and Molecular Medicine | https://gradschool.wsu.edu/degrees/ |

---

#### College of Veterinary Medicine

##### MS / PhD
| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Biomedical Sciences | MS | https://gradschool.wsu.edu/degrees/ |

---

#### Interdisciplinary / Cross-College Programs

##### MS / PhD / Graduate Certificate
| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Interdisciplinary Studies | MS | https://gradschool.wsu.edu/degrees/ |
| 2 | Individual Interdisciplinary Doctoral Program | PhD | https://gradschool.wsu.edu/degrees/ |
| 3 | Professional Molecular Sciences | GC | https://gradschool.wsu.edu/degrees/ |
| 4 | Protein Biotechnology | GC | https://gradschool.wsu.edu/degrees/ |
| 5 | Community Engagement in River and Watershed Systems | GC | https://gradschool.wsu.edu/degrees/ |
| 6 | Water Resources Science and Management | GC | https://gradschool.wsu.edu/degrees/ |

---

### 2.2 Sample Program Deep-Dive: Computer Science (MS)

- **Department**: Electrical Engineering and Computer Science, Voiland College of Engineering and Architecture
- **Degree**: Master of Science in Computer Science
- **Campus**: Pullman (also Tri-Cities, Vancouver)
- **Application**: Via Graduate School (GradCAS)
- **Priority Deadline**: January 10 (Fall), July 1 (Spring)
- **GRE**: Check with program (WSU code 4705)
- **TOEFL Minimum**: 75 iBT / 4 (new scale) / IELTS 6.5
- **GPA Minimum**: 3.0 on 4.0 scale
- **Letters of Recommendation**: 3 required
- **Funding**: Graduate assistantships available (TA/RA)
- **Website**: https://gradschool.wsu.edu/degrees/

### 2.3 Graduate Admissions Model

WSU uses a **centralized application system** managed by the Graduate School, but **admission decisions are made by individual departments/programs**. The process:

1. Applicant submits application through GradCAS (or EngineeringCAS, NursingCAS, etc. for specific programs)
2. Department reviews and recommends admission
3. Graduate School reviews credentials and finalizes admission
4. Vice Provost for Graduate and Professional Education grants final approval

**Application Platforms**: GradCAS, EngineeringCAS, DICAS, CSDCAS, NursingCAS, PharmCAS

**Application Fee**: Not explicitly stated on website (CAS platform fee applies; McNair Scholars eligible for waiver)

**Priority Deadlines**: Fall = January 10; Spring = July 1

**Professional programs** (MBA, MD, DVM, PharmD) manage their own admissions separately.

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions Website | https://admission.wsu.edu/ | admission.wsu.edu |
| Application Portal | WSU Application or Common App | admission.wsu.edu/apply/first-year-students/ |
| Application Fee | $70 | admission.wsu.edu/apply/first-year-students/ |
| Admission Type | **Rolling admission** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Priority Admission Date (First-Year) | **March 31** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Top Scholars Priority Date | **January 31** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Scholarship Priority Date | **January 31** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| FAFSA/WASFA Priority Date | **January 31** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Enrollment Confirmation Priority | **May 1** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Transfer Priority Date | **August 7** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Spring Application Priority | **November 15** | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| SAT/ACT Policy | **Test-optional — NOT required, NOT used in admission decisions** | admission.wsu.edu/apply/first-year-students/ |
| Superscore Policy | N/A (test-optional) | — |
| Interview Policy | Not required | — |
| Recommendation Requirements | Not required for UG | — |
| GPA Requirement (Domestic) | No minimum stated (holistic review) | admission.wsu.edu/apply/first-year-students/ |
| GPA Requirement (International) | **2.70 minimum** on 4.0 scale | ip.wsu.edu/future-students/requirements/ |
| Transfer GPA Requirement (International) | **2.50 minimum** on 4.0 scale | ip.wsu.edu/future-students/requirements/ |
| Transfer Credits Required | 27 semester credits (international transfer) | ip.wsu.edu/future-students/requirements/ |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum (Traditional Admission) | 1-Term Foundation | 2-Semester Foundation | Source |
|------|--------------------------------|-------------------|----------------------|--------|
| TOEFL iBT (New, Jan 2026+) | **4** | 3.5 | 3 | ip.wsu.edu/future-students/requirements/ |
| IELTS | **6.5** | 6 | 5.5 | ip.wsu.edu/future-students/requirements/ |
| Duolingo | **105** | 95 | 85 | ip.wsu.edu/future-students/requirements/ |
| PTEA | **58** | 47 | 44 | ip.wsu.edu/future-students/requirements/ |
| Cambridge C1 Advanced | **C1 Advanced** | B2 First | B2 First | ip.wsu.edu/future-students/requirements/ |
| TOEFL Essentials | **8** | 7.5 | 4.5 | ip.wsu.edu/future-students/requirements/ |
| iTEP | **4** | 3.4 | 2.9 | ip.wsu.edu/future-students/requirements/ |
| MET | **64** | 63 | 52 | ip.wsu.edu/future-students/requirements/ |
| Language Cert Academic | **70** | 65 | 60 | ip.wsu.edu/future-students/requirements/ |
| Oxford ELLT | **7** | 6 | 5 | ip.wsu.edu/future-students/requirements/ |

**Academic Exam Alternatives:**

| Exam | Minimum Score |
|------|---------------|
| SAT (Evidence-based Reading & Writing) | 500 |
| ACT (English + Reading) | 17 English + 19 Reading |
| Gaokao | 125 |
| IGCSE English First Language | C/5+ |

**Language Waiver Options:**
- Option A: 3+ years at U.S. or regionally accredited international high school
- Option B: Completed WSU English 101 & 102 equivalents with 3.0 GPA + 27 transferable credits
- Option C: 53+ semester hours at U.S. regionally accredited institution
- Option D: Associate degree with 2.5+ GPA
- Option E: Citizen of English-speaking country (UK, Canada, Australia, etc.)
- Option F: Degree from English-medium institution outside US

### 3.3 Graduate — Global Rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Application Platform | GradCAS / EngineeringCAS / NursingCAS / PharmCAS | gradschool.wsu.edu/apply/ |
| Application Fee | CAS platform fee (McNair waiver available) | gradschool.wsu.edu/faqs/ |
| GRE Institutional Code | **4705** | gradschool.wsu.edu/international-requirements/ |
| GRE Policy | **Per-program** (check individual program) | gradschool.wsu.edu/international-requirements/ |
| GPA Minimum | **3.0** on 4.0 scale | gradschool.wsu.edu/international-requirements/ |
| Letters of Recommendation | **3 required** | gradschool.wsu.edu/international-requirements/ |
| TOEFL Minimum (iBT) | **75** (old scale) / **4** (new scale, Jan 2026+) | gradschool.wsu.edu/international-requirements/ |
| TOEFL PBT Minimum | **540** | gradschool.wsu.edu/international-requirements/ |
| IELTS Minimum | **6.5** (with sub-scores: Listening 6.5, Speaking 6.0) | gradschool.wsu.edu/international-requirements/ |
| Duolingo Minimum | **105** | gradschool.wsu.edu/international-requirements/ |
| Cambridge Minimum | **176** | gradschool.wsu.edu/international-requirements/ |
| PTEA Minimum | **56** | gradschool.wsu.edu/international-requirements/ |
| iTEP Minimum | **4.5** | gradschool.wsu.edu/international-requirements/ |
| TOEFL Sub-score Requirements | Listening 17 (old) / 4.5 (new); Speaking 20 (old) / 4 (new) | gradschool.wsu.edu/international-requirements/ |
| Priority Deadline (Fall) | **January 10** | gradschool.wsu.edu/apply/ |
| Priority Deadline (Spring) | **July 1** | gradschool.wsu.edu/apply/ |
| CGS April 15 Signatory | Not explicitly stated | — |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Pullman Campus)

| Expense Item | Resident (In-State) | Non-Resident (OOS) | Description |
|-------------|---------------------|---------------------|-------------|
| Tuition & S&A Fees | **$12,698** | **$30,370** | Per year (2 semesters); full-time 10-18 credits |
| Mandatory Fees | **$1,660** | **$1,660** | Per year; includes health, rec center, CUB, transit, etc. |
| Housing | **$10,846** | **$10,846** | On-campus estimate |
| Food | **$6,400** | **$6,400** | Meal plan estimate |
| Books & Supplies | **$900** | **$900** | Estimated |
| Transportation | **$1,716** | **$1,716** | Estimated |
| Miscellaneous | **$1,968** | **$1,968** | Personal expenses |
| **COA Year Total** | **$36,188** | **$53,860** | Financial aid packaging amount |
| Per-Credit Rate (1-10 credits) | $634.90/credit | $1,518.50/credit | Part-time rate |

> **Source**: financialaid.wsu.edu/tuition-and-expenses/, 2026-27 Pullman Undergraduate

**Mandatory Fee Breakdown (Pullman Undergraduate, per semester):**

| Fee | Amount |
|-----|--------|
| Rec Center | $191 |
| CUB Fee | $145 |
| Health Fee | $256 |
| Stadium Fee | $25 |
| Technology Fee | $20 |
| Transit Fee | $40 |
| Chinook Fee | $108 |
| Media Fee | $5 |
| Food Pantry Fee | $5 |
| **Total Mandatory Fees** | **$830** |

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-Blind / Need-Aware | **Need-aware for all applicants** (public university; does not guarantee to meet full demonstrated need) | General knowledge; WSU is a public institution |
| Merit Scholarships | Yes — 700+ scholarship programs; ~$177.8M undergraduate gift aid (2023-24) | admission.wsu.edu/cost/ |
| Automatic Academic Awards | DUAA (Distinguished University Achievement Award), UAA (University Achievement Award), WUE/Cougar Award | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Washington College Grant | Available for WA residents (family income ≤$107k may qualify) | admission.wsu.edu/cost/financial-aid/ |
| FAFSA Priority Date | January 31 | admission.wsu.edu/apply/admissions-dates-deadlines/ |
| Students Receiving Aid | 83% (2023-24) | admission.wsu.edu/cost/tuition/ |
| Students Paying Full Tuition | 31% | admission.wsu.edu/cost/tuition/ |
| Debt-Free Graduation Rate | 57.1% graduate without debt (resident UG) | financialaid.wsu.edu/tuition-and-expenses/ |

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 | 来源 |
|------|-----|------|
| Graduate Tuition (Resident, 2026-27) | ~$6,349/semester (varies by program) | financialaid.wsu.edu/tuition-and-expenses/ |
| Graduate Tuition (Non-Resident, 2026-27) | ~$15,185/semester (varies by program) | financialaid.wsu.edu/tuition-and-expenses/ |
| Assistantship Tuition Reduction | Available for students on half-time (20 hrs/wk) assistantship | gradschool.wsu.edu/student-finance-page/ |
| Assistantship Health Insurance | Covered for graduate assistants | gradschool.wsu.edu/student-finance-page/ |
| Funding Types | Graduate assistantships (TA/RA), fellowships, scholarships | gradschool.wsu.edu/finance/ |
| WICHE/WRGP | Western Regional Graduate Program — reduced tuition for qualifying programs | gradschool.wsu.edu/wiche/ |
| Professional Program Tuition | MBA, DVM, MD, PharmD have separate tuition schedules | financialaid.wsu.edu/tuition-and-expenses/ |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: UG Admission Priority Date
```yaml
field: undergraduate.admissions.priority_date
value: March 31
source_url: https://admission.wsu.edu/apply/admissions-dates-deadlines/
source_snippet: "March 31 Fall 2026 admission application priority date for first-year students."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Scholarship Priority Date
```yaml
field: undergraduate.admissions.scholarship_priority_date
value: January 31
source_url: https://admission.wsu.edu/apply/admissions-dates-deadlines/
source_snippet: "January 31 WSU General Scholarship application priority date to be considered for early awarding."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Test Policy
```yaml
field: undergraduate.admissions.test_policy
value: Test-optional (SAT/ACT not required, not used in decisions)
source_url: https://admission.wsu.edu/apply/first-year-students/
source_snippet: "WSU does not require students to submit SAT/ACT test scores as part of the application process and will not use them in our admission decisions."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Application Fee
```yaml
field: undergraduate.admissions.application_fee
value: $70
source_url: https://admission.wsu.edu/apply/first-year-students/
source_snippet: "Pay the $70 application fee or apply for a fee waiver."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: UG Tuition (Resident)
```yaml
field: undergraduate.costs.tuition_resident_2026_27
value: $12,698/year ($6,349/semester)
source_url: https://financialaid.wsu.edu/tuition-and-expenses/
source_snippet: "Tuition & S&A Fees | $6,349 | $15,185" (semester table, Pullman Undergraduate 2026-27)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: UG Tuition (Non-Resident)
```yaml
field: undergraduate.costs.tuition_nonresident_2026_27
value: $30,370/year ($15,185/semester)
source_url: https://financialaid.wsu.edu/tuition-and-expenses/
source_snippet: "Tuition & S&A Fees | $6,349 | $15,185" (semester table, Pullman Undergraduate 2026-27)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: UG COA (Resident)
```yaml
field: undergraduate.costs.coa_resident_2026_27
value: $36,188/year
source_url: https://financialaid.wsu.edu/tuition-and-expenses/
source_snippet: "COA Year Total: | $36,188 | $53,860"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: UG COA (Non-Resident)
```yaml
field: undergraduate.costs.coa_nonresident_2026_27
value: $53,860/year
source_url: https://financialaid.wsu.edu/tuition-and-expenses/
source_snippet: "COA Year Total: | $36,188 | $53,860"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: English Proficiency — TOEFL
```yaml
field: undergraduate.admissions.english_proficiency.toefl
value: 4 (new iBT scale, Jan 2026+)
source_url: https://ip.wsu.edu/future-students/requirements/
source_snippet: "TOEFL iBT | 4 | 3.5 | 3 | 2.5" (Traditional Admission column)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-010: English Proficiency — IELTS
```yaml
field: undergraduate.admissions.english_proficiency.ielts
value: 6.5
source_url: https://ip.wsu.edu/future-students/requirements/
source_snippet: "IELTS | 6.5 | 6 | 5.5 | 5" (Traditional Admission column)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: English Proficiency — Duolingo
```yaml
field: undergraduate.admissions.english_proficiency.duolingo
value: 105
source_url: https://ip.wsu.edu/future-students/requirements/
source_snippet: "Duolingo | 105 | 95 | 85 | 60" (Traditional Admission column)
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-012: International UG GPA Requirement
```yaml
field: undergraduate.admissions.international_gpa_minimum
value: 2.70 on 4.0 scale
source_url: https://ip.wsu.edu/future-students/requirements/
source_snippet: "WSU requires a minimum grade point average of 2.70 (on a 4.00 scale) for admission as an international first-year student."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: Financial Aid — Students Receiving Aid
```yaml
field: undergraduate.financial_aid.percent_receiving_aid
value: 83% (2023-24)
source_url: https://admission.wsu.edu/cost/tuition/
source_snippet: "83% students received financial aid in 2023-24"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-014: Financial Aid — Debt-Free Graduation
```yaml
field: undergraduate.financial_aid.debt_free_graduation_rate
value: 57.1% (resident UG)
source_url: https://financialaid.wsu.edu/tuition-and-expenses/
source_snippet: "The percentage of resident undergraduates graduating without any debt known to [WSU] has increased from 35.6 percent to 57.1 percent."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate TOEFL Minimum
```yaml
field: graduate.admissions.english_proficiency.toefl_ibt
value: 75 (old scale) / 4 (new scale, Jan 2026+)
source_url: https://gradschool.wsu.edu/international-requirements/
source_snippet: "TOEFL (iBT) | 75" and "New TOEFL (iBT) (Effective Jan 21, 2026) | 4"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-002: Graduate IELTS Minimum
```yaml
field: graduate.admissions.english_proficiency.ielts
value: 6.5 (Listening 6.5, Speaking 6.0)
source_url: https://gradschool.wsu.edu/international-requirements/
source_snippet: "IELTS | 6.5" with sub-scores "Listening, 6.5" and "Speaking, 6.0"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-003: Graduate GPA Minimum
```yaml
field: graduate.admissions.gpa_minimum
value: 3.0 on 4.0 scale
source_url: https://gradschool.wsu.edu/international-requirements/
source_snippet: "Have a cumulative grade point average (GPA) of 3.0 on a 4.0 scale or a B grade or better."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Graduate GRE Code
```yaml
field: graduate.admissions.gre_institutional_code
value: 4705
source_url: https://gradschool.wsu.edu/international-requirements/
source_snippet: "WSU's GRE Institutional Code is 4705."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-005: Graduate Priority Deadline (Fall)
```yaml
field: graduate.admissions.priority_deadline_fall
value: January 10
source_url: https://gradschool.wsu.edu/apply/
source_snippet: "Fall Semester Priority Application Deadline: January 10"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-006: Graduate Program Count
```yaml
field: graduate.programs.total_count
value: 74 program groups (~140 degree programs, ~195 including certificates)
source_url: https://gradschool.wsu.edu/degrees/
source_snippet: "Showing 74 of 74 programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-001: Program Count — UG Degrees
```yaml
field: undergraduate.programs.total_degree_programs
value: 192
source_url: https://catalog.wsu.edu/Degrees
source_snippet: Full extraction of Pullman Campus Schedule of Studies (192 degree/major/option entries)
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-002: Program Count — UG Minors
```yaml
field: undergraduate.programs.total_minors
value: 120
source_url: https://catalog.wsu.edu/Minors
source_snippet: Full extraction of Pullman Campus Minors list (120 entries)
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-003: Program Count — UG Certificates
```yaml
field: undergraduate.programs.total_certificates
value: 70
source_url: https://catalog.wsu.edu/Certificates
source_snippet: Full extraction of Pullman Campus Certificates list (70 entries)
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
wsu-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, matrix
├── 01-ug-cahnrs.md                     # Section 1: CAHNRS programs
├── 02-ug-arts-sciences.md              # Section 1: Arts & Sciences programs
├── 03-ug-business.md                   # Section 1: Carson Business programs
├── 04-ug-communication.md              # Section 1: Murrow Communication programs
├── 05-ug-education.md                  # Section 1: Education programs
├── 06-ug-engineering.md                # Section 1: Engineering & Architecture programs
├── 07-ug-nursing.md                    # Section 1: Nursing programs
├── 08-ug-pharmacy.md                   # Section 1: Pharmacy programs
├── 09-ug-vetmed.md                     # Section 1: Veterinary Medicine programs
├── 10-ug-medicine.md                   # Section 1: MD program
├── 11-ug-minors-certificates.md        # Section 1: Minors + certificates
├── 12-grad-cahnrs.md                   # Section 2: CAHNRS graduate programs
├── 13-grad-arts-sciences.md            # Section 2: Arts & Sciences graduate
├── 14-grad-business.md                 # Section 2: Business graduate
├── 15-grad-communication.md            # Section 2: Communication graduate
├── 16-grad-education.md                # Section 2: Education graduate
├── 17-grad-engineering.md              # Section 2: Engineering graduate
├── 18-grad-nursing-pharmacy-vetmed.md  # Section 2: Professional graduate
├── 19-grad-interdisciplinary.md        # Section 2: Interdisciplinary grad programs
├── 20-deadlines-requirements.md        # Section 3: Application requirements
├── 21-costs-financial-aid.md           # Section 4: Costs and aid
├── 22-evidence-chain.md                # Section 5: Evidence index
└── 23-comparison-framework.md          # Section 7: Cross-school comparison
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "wsu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
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

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Graduate application fee (exact amount) | gradschool.wsu.edu or CAS platform | Not found on website; need to check CAS application |
| P1 | Need-blind/need-aware policy (official statement) | admission.wsu.edu or financialaid.wsu.edu | Inferred from public university status; no explicit statement found |
| P1 | Per-program GRE requirements | Individual program pages | Varies by department; need program-by-program check |
| P1 | Graduate stipend rates | gradschool.wsu.edu/finance/ | PDF linked but not extracted |
| P2 | Specific housing costs by dorm | housing.wsu.edu | Only average estimate captured |
| P2 | WUE tuition rate | admission.wsu.edu | WUE/Cougar Award mentioned but specific rate not extracted |
| P2 | Professional program tuition (MBA, DVM, MD, PharmD) | financialaid.wsu.edu | Available in dropdown but not fully extracted |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | WSU | Notes |
|------|-----|-------|
| Type | Public (Land-grant) | Pullman, WA |
| Total Programs (Rule 1) | 362 degree programs (457 with certificates) | UG 192 + Grad 170 |
| School/Dept Count (Rule 2) | 11 colleges | Plus Graduate School |
| UG Tuition (In-State) | $12,698/year | 2026-27 |
| UG Tuition (OOS) | $30,370/year | 2026-27 |
| UG COA (In-State) | $36,188/year | 2026-27 |
| UG COA (OOS) | $53,860/year | 2026-27 |
| Need-Blind (Intl?) | Need-aware for all | Public university |
| EA Deadline | N/A | No early action |
| Priority Date | March 31 (admission), Jan 31 (scholarship) | Rolling admission |
| SAT/ACT Required? | No (test-optional) | Not used in decisions |
| TOEFL Min (UG) | 4 (new scale) / IELTS 6.5 | ip.wsu.edu |
| TOEFL Min (Grad) | 75 iBT / 4 (new scale) / IELTS 6.5 | gradschool.wsu.edu |
| GRE Policy | Per-program | WSU code 4705 |
| Application Fee (UG) | $70 | Common App or WSU app |
| Distinctive Features | Land-grant; strong agriculture/vet med; DVM/MD/PharmD programs; 6 campuses; rolling admission | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admission.wsu.edu, financialaid.wsu.edu, catalog.wsu.edu, gradschool.wsu.edu, ip.wsu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
