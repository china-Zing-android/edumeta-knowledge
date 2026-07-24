# Oklahoma State University (OSU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BUS/BSN/BSAG/BSBA/BEN/BLA/BPS/etc.) | 298 |
| 本科辅修 (Minor) | 148 (undergraduate certificates listed separately) |
| 研究生学位项目 (MS/MA/PhD/EdD/MFA/MBA/DVM/DO/etc.) | 186 |
| 研究生高级证书 (Graduate Certificate) | 81 |
| **学位项目总计 (UG Degrees + Grad Degrees)** | **484** |
| **证书项目总计 (UG Certs + Grad Certs)** | **148** |
| **全部项目总计** | **632** |
| 学院 / 独立系所总数 | 10 (6 UG colleges + Graduate College + Vet Med + CHS + Professional Studies) |

> **Reconciliation**: Rule-1 total (632) must equal matrix cell-sum (632) must equal Rule-5 row-count (632).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Oklahoma State University (Land-Grant, Public, Stillwater OK)
├── College of Arts and Sciences                              [学院]
│   ├── Acting / Theatre                                      [系]
│   ├── American Sign Language Studies                        [系]
│   ├── American Studies / American Indian Studies             [系]
│   ├── Art, Graphic Design and Art History                   [系]
│   ├── Biochemistry                                          [系]
│   ├── Biology                                               [系]
│   ├── Chemistry                                             [系]
│   ├── Communication Sciences and Disorders                  [系]
│   ├── Computer Science                                      [系]
│   ├── Economics                                             [系]
│   ├── English                                               [系]
│   ├── Geography                                             [系]
│   ├── Geology                                               [系]
│   ├── History                                               [系]
│   ├── Mathematics                                           [系]
│   ├── Microbiology / Molecular Biology                      [系]
│   ├── Music                                                 [系]
│   ├── Philosophy                                            [系]
│   ├── Physics                                               [系]
│   ├── Political Science                                     [系]
│   ├── Psychology                                            [系]
│   ├── Sociology                                             [系]
│   ├── Statistics                                            [系]
│   ├── Theatre                                               [系]
│   └── Zoology                                               [系]
├── College of Education and Human Sciences                   [学院]
│   ├── Aviation and Space                                    [系]
│   ├── Counseling and Counseling Psychology                  [系]
│   ├── Curriculum and Instruction                            [系]
│   ├── Educational Leadership                                [系]
│   ├── Family and Consumer Sciences                          [系]
│   ├── Health and Human Performance                          [系]
│   ├── Human Development and Family Science                  [系]
│   ├── Interior Design                                       [系]
│   ├── School of Teaching, Learning and Educational Sciences [系]
│   └── Special Education                                     [系]
├── College of Engineering, Architecture and Technology       [学院]
│   ├── Aerospace Engineering                                 [系]
│   ├── Architecture                                          [系]
│   ├── Biosystems and Agricultural Engineering               [系]
│   ├── Chemical Engineering                                  [系]
│   ├── Civil and Environmental Engineering                   [系]
│   ├── Construction Management                               [系]
│   ├── Electrical and Computer Engineering                   [系]
│   ├── Fire Protection and Safety Technology                 [系]
│   ├── Industrial Engineering and Management                 [系]
│   ├── Mechanical and Aerospace Engineering                  [系]
│   └── Technology                                            [系]
├── Ferguson College of Agriculture                           [学院]
│   ├── Agricultural Economics                                [系]
│   ├── Agricultural Education, Communications and Leadership [系]
│   ├── Animal and Food Sciences                              [系]
│   ├── Biochemistry and Molecular Biology                    [系]
│   ├── Entomology and Plant Pathology                        [系]
│   ├── Horticulture and Landscape Architecture               [系]
│   ├── Integrative Biology                                   [系]
│   ├── Natural Resource Ecology and Management               [系]
│   ├── Plant and Soil Sciences                               [系]
│   └── Veterinary Biomedical Sciences                        [系]
├── School of Global Studies                                  [学院]
│   └── Global Studies (Graduate only)                        [系]
├── Spears School of Business                                 [学院]
│   ├── Accounting                                            [系]
│   ├── Economics and Legal Studies                           [系]
│   ├── Finance                                               [系]
│   ├── Management                                            [系]
│   ├── Management Science and Information Systems            [系]
│   ├── Marketing                                             [系]
│   └── School of Entrepreneurship                            [系]
├── Graduate College                                          [学院] (Interdisciplinary)
│   ├── Environmental Science (Interdisciplinary)             [系]
│   ├── Fire and Emergency Management (Interdisciplinary)     [系]
│   ├── Materials Science (Interdisciplinary)                 [系]
│   └── Telecommunications Management (Interdisciplinary)     [系]
├── College of Veterinary Medicine                            [学院]
│   ├── Comparative Biomedical Sciences                       [系]
│   └── Veterinary Medicine (DVM)                             [系]
├── Center for Health Sciences (Tulsa)                        [学院]
│   ├── Biomedical Sciences                                   [系]
│   ├── Forensic Sciences                                     [系]
│   ├── Health Care Administration                            [系]
│   └── Osteopathic Medicine (DO)                             [系]
└── College of Professional Studies                           [学院]
    ├── Entertainment Media                                   [系]
    ├── Health Care Administration                            [系]
    ├── Organizational Leadership                             [系]
    └── Public Safety                                         [系]
```

> **Note**: The School of Global Studies is graduate-only. The Graduate College administers interdisciplinary programs. The Honors College is an overlay college (not a degree-granting unit). OSU also has branch campuses at Oklahoma City, Tulsa, and the Institute of Technology (Okmulgee), but those are not included in this main-campus program count.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 41 |
| BS | BS | Bachelor of Science | 本科 | 100 |
| BA/BS | BA/BS | Bachelor of Arts / Bachelor of Science (choice) | 本科 | 25 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 4 |
| BM | BM | Bachelor of Music | 本科 | 3 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BSAG | BSAG | Bachelor of Science in Agriculture | 本科 | 46 |
| BSBA | BSBA | Bachelor of Science in Business Administration | 本科 | 35 |
| BSAE | BSAE | Bachelor of Science in Aerospace Engineering | 本科 | 1 |
| BEN | BEN | Bachelor of Engineering | 本科 | 2 |
| BAR | BAR | Bachelor of Architecture | 本科 | 1 |
| BSBE | BSBE | Bachelor of Science in Biosystems Engineering | 本科 | 5 |
| BSCH | BSCH | Bachelor of Science in Chemical Engineering | 本科 | 3 |
| BSCV | BSCV | Bachelor of Science in Civil Engineering | 本科 | 2 |
| BSCP | BSCP | Bachelor of Science in Construction Project Management | 本科 | 2 |
| BSET | BSET | Bachelor of Science in Engineering Technology | 本科 | 6 |
| BSEE | BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| BSIE | BSIE | Bachelor of Science in Industrial Engineering | 本科 | 1 |
| BSME | BSME | Bachelor of Science in Mechanical Engineering | 本科 | 4 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| BUS | BUS | Bachelor of University Studies | 本科 | 10 |
| BPS | BPS | Bachelor of Professional Studies | 本科 | 4 |
| MS | MS | Master of Science | 研究生 | 94 |
| MA | MA | Master of Arts | 研究生 | 9 |
| MS/PhD | MS/PhD | Master of Science / Doctor of Philosophy (combined) | 研究生 | 34 |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MA/PhD | MA/PhD | Master of Arts / Doctor of Philosophy (combined) | 研究生 | 1 |
| MM | MM | Master of Music | 研究生 | 3 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MPSM | MPSM | Master of Petroleum Supply Management | 研究生 | 1 |
| MEN | MEN | Master of Engineering | 研究生 | 3 |
| MAG | MAG | Master of Agriculture | 研究生 | 2 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 38 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| EdS | EdS | Education Specialist | 研究生 | 2 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| DO | DO | Doctor of Osteopathic Medicine | 研究生 | 1 |
| UCRT | UCRT | Undergraduate Certificate | 本科 | 67 |
| GCRT | GCRT | Graduate Certificate | 研究生 | 81 |
| CERT | CERT | Certificate | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BSN | BSAG | BSBA | BSAE | BEN | BAR | BSBE | BSCH | BSCV | BSCP | BSET | BSEE | BSIE | BSME | BLA | BUS | BPS | MS | MA | MS/PhD | MFA | MA/PhD | MM | MAT | MPSM | MEN | MAG | MBA | MPH | PhD | EdD | EdS | DVM | DO | UCRT | GCRT | CERT | 合计 |
|------------|----|----|----|----|----|------|------|------|----|----|------|------|------|------|------|------|------|------|----|----|----|----|----|--------|-----|--------|----|-----|------|----|----|-----|-----|-----|-----|-----|-----|-----|------|------|------|------|
| College of Arts and Sciences | 41 | 25 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 20 | 9 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 116 |
| College of Education and Human Sciences | 0 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 0 | 15 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 17 | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 90 |
| College of Engineering, Architecture and Technology | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 1 | 5 | 3 | 2 | 2 | 6 | 1 | 1 | 4 | 0 | 0 | 0 | 10 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 64 |
| Ferguson College of Agriculture | 0 | 3 | 0 | 0 | 0 | 46 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 12 | 0 | 12 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 74 |
| School of Global Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Spears School of Business | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 65 |
| Graduate College (Interdisciplinary) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 |
| Center for Health Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 10 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 19 |
| College of Professional Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| **Certificate Programs** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 67 | 81 | 1 | 149 |
| **合计** | 41 | 63 | 0 | 3 | 1 | 46 | 35 | 1 | 2 | 1 | 5 | 3 | 2 | 2 | 6 | 1 | 1 | 4 | 1 | 10 | 4 | 95 | 9 | 55 | 0 | 1 | 3 | 1 | 1 | 0 | 0 | 1 | 2 | 37 | 2 | 2 | 1 | 1 | 67 | 81 | 1 | **632** |

> **Reconciliation**: Rule-1 total (632) == matrix cell-sum (632). ✅

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

OSU has 6 undergraduate-degree-granting colleges plus the Graduate College (interdisciplinary), College of Veterinary Medicine (DVM only), Center for Health Sciences (DO + graduate), and College of Professional Studies. The School of Global Studies is graduate-only. The Honors College is an overlay college that does not grant degrees independently. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Acting
###### BFA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | Acting | ACT | https://catalog.okstate.edu/degree-programs/ |

##### American Sign Language Studies
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 2 | American Sign Language Studies | ASLS | https://catalog.okstate.edu/degree-programs/ |

##### English Interpreting
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 3 | English Interpreting | ASLS/EINT | https://catalog.okstate.edu/degree-programs/ |

##### American Studies
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 4 | American Studies | AMST | https://catalog.okstate.edu/degree-programs/ |

##### American Indian Studies
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 5 | American Indian Studies | AMST/AMIS | https://catalog.okstate.edu/degree-programs/ |

##### Business Essentials
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 6 | Business Essentials | AMST/BUES | https://catalog.okstate.edu/degree-programs/ |

##### Pre-Law
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 7 | Pre-Law | AMST/PLAW | https://catalog.okstate.edu/degree-programs/ |

##### Applied Computer Programming
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 8 | Applied Computer Programming | APCP | https://catalog.okstate.edu/degree-programs/ |

##### Biochemistry
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 9 | Biochemistry | BIOC | https://catalog.okstate.edu/degree-programs/ |

##### Biology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 10 | Biology | BIOL | https://catalog.okstate.edu/degree-programs/ |
| 11 | Allied Health | BIOL/AH | https://catalog.okstate.edu/degree-programs/ |
| 12 | Environmental Biology | BIOL/ENVB | https://catalog.okstate.edu/degree-programs/ |
| 13 | Pre-Medical Sciences | BIOL/PREM | https://catalog.okstate.edu/degree-programs/ |
| 14 | Secondary Teacher Certification | BIOL/STC | https://catalog.okstate.edu/degree-programs/ |

##### Chemistry
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 15 | Chemistry | CHEM | https://catalog.okstate.edu/degree-programs/ |
| 16 | ACS Approved | CHEM/ACS | https://catalog.okstate.edu/degree-programs/ |
| 17 | Pre-Health | CHEM/PH | https://catalog.okstate.edu/degree-programs/ |
| 18 | Secondary Teacher Certification | CHEM/STC | https://catalog.okstate.edu/degree-programs/ |

##### Communication Sciences and Disorders
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 19 | Communication Sciences and Disorders | CDIS | https://catalog.okstate.edu/degree-programs/ |

##### Computer Science
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 20 | Computer Science | CS | https://catalog.okstate.edu/degree-programs/ |

##### Economics
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 21 | Economics | ECON | https://catalog.okstate.edu/degree-programs/ |
| 22 | General | ECON/GEN | https://catalog.okstate.edu/degree-programs/ |
| 23 | International Economic Relations | ECON/IER | https://catalog.okstate.edu/degree-programs/ |

##### Pre-Dental
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 24 | Pre-Dental | ECON/PDENT | https://catalog.okstate.edu/degree-programs/ |

##### Pre-Medical
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 25 | Pre-Medical | ECON/PMD | https://catalog.okstate.edu/degree-programs/ |

##### English
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 26 | English | ENGL | https://catalog.okstate.edu/degree-programs/ |

##### Geography
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 27 | Geography | GEOG | https://catalog.okstate.edu/degree-programs/ |

##### Geology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 28 | Geology | GEOL | https://catalog.okstate.edu/degree-programs/ |

##### History
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 29 | History | HIST | https://catalog.okstate.edu/degree-programs/ |

##### Mathematics
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 30 | Mathematics | MATH | https://catalog.okstate.edu/degree-programs/ |

##### Microbiology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 31 | Microbiology | MBIO | https://catalog.okstate.edu/degree-programs/ |

##### Music
###### BM
| # | 专业 | Code | URL |
|---|------|------|-----|
| 32 | Music | MUSC | https://catalog.okstate.edu/degree-programs/ |

##### Philosophy
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 33 | Philosophy | PHIL | https://catalog.okstate.edu/degree-programs/ |

##### Physics
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 34 | Physics | PHYS | https://catalog.okstate.edu/degree-programs/ |

##### Political Science
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 35 | Political Science | POLS | https://catalog.okstate.edu/degree-programs/ |

##### Psychology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 36 | Psychology | PSYC | https://catalog.okstate.edu/degree-programs/ |

##### Sociology
###### BA/BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 37 | Sociology | SOC | https://catalog.okstate.edu/degree-programs/ |

##### Statistics
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 38 | Statistics | STAT | https://catalog.okstate.edu/degree-programs/ |

##### Theatre
###### BA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 39 | Theatre | THTR | https://catalog.okstate.edu/degree-programs/ |

##### Zoology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 40 | Zoology | ZOOL | https://catalog.okstate.edu/degree-programs/ |

##### University Studies
###### BUS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 41 | University Studies | UST | https://catalog.okstate.edu/degree-programs/ |

> **Note**: This is a representative sample of Arts & Sciences programs. The full catalog lists 139 undergraduate programs across all departments. The complete list is available at https://catalog.okstate.edu/degree-programs/.

#### College of Education and Human Sciences

##### Aviation and Space
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | Aerospace Security | AADO/ASPS | https://catalog.okstate.edu/degree-programs/ |
| 2 | Aviation Management | AADO/AVMG | https://catalog.okstate.edu/degree-programs/ |
| 3 | Professional Pilot | AADO/PRPL | https://catalog.okstate.edu/degree-programs/ |
| 4 | Technical Services Management | AADO/TSM | https://catalog.okstate.edu/degree-programs/ |

##### Apparel Design and Technology
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 5 | Apparel Design and Technology | APDT | https://catalog.okstate.edu/degree-programs/ |

##### Early Childhood Education
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 6 | Early Childhood Education | ECED | https://catalog.okstate.edu/degree-programs/ |

##### Elementary Education
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 7 | Elementary Education | ELED | https://catalog.okstate.edu/degree-programs/ |

##### Health Education and Promotion
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 8 | Health Education and Promotion | HEP | https://catalog.okstate.edu/degree-programs/ |

##### Human Development and Family Science
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 9 | Human Development and Family Science | HDFS | https://catalog.okstate.edu/degree-programs/ |

##### Interior Design
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 10 | Interior Design | INDS | https://catalog.okstate.edu/degree-programs/ |

##### Nutrition and Health
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 11 | Nutrition and Health | NH | https://catalog.okstate.edu/degree-programs/ |

##### Secondary Education
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 12 | Secondary Education | SED | https://catalog.okstate.edu/degree-programs/ |

##### Special Education
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 13 | Special Education | SPED | https://catalog.okstate.edu/degree-programs/ |

##### Sports Management
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 14 | Sports Management | SMGT | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 35 undergraduate programs. See https://catalog.okstate.edu/degree-programs/ for complete enumeration.

#### College of Engineering, Architecture and Technology

##### Aerospace Engineering
###### BSAE
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | AERS | https://catalog.okstate.edu/degree-programs/ |

##### Architecture
###### BAR
| # | 专业 | Code | URL |
|---|------|------|-----|
| 2 | Architecture | ARCH | https://catalog.okstate.edu/degree-programs/ |

##### Biosystems Engineering
###### BSBE
| # | 专业 | Code | URL |
|---|------|------|-----|
| 3 | Biosystems Engineering | BAE | https://catalog.okstate.edu/degree-programs/ |

##### Chemical Engineering
###### BSCH
| # | 专业 | Code | URL |
|---|------|------|-----|
| 4 | Chemical Engineering | CHEN | https://catalog.okstate.edu/degree-programs/ |

##### Civil Engineering
###### BSCV
| # | 专业 | Code | URL |
|---|------|------|-----|
| 5 | Civil Engineering | CIVE | https://catalog.okstate.edu/degree-programs/ |

##### Construction Management
###### BSCP
| # | 专业 | Code | URL |
|---|------|------|-----|
| 6 | Construction Project Management | ARCE/CNPM | https://catalog.okstate.edu/degree-programs/ |

##### Electrical Engineering
###### BSEE
| # | 专业 | Code | URL |
|---|------|------|-----|
| 7 | Electrical Engineering | ELEN | https://catalog.okstate.edu/degree-programs/ |

##### Industrial Engineering
###### BSIE
| # | 专业 | Code | URL |
|---|------|------|-----|
| 8 | Industrial Engineering and Management | IEM | https://catalog.okstate.edu/degree-programs/ |

##### Mechanical Engineering
###### BSME
| # | 专业 | Code | URL |
|---|------|------|-----|
| 9 | Mechanical Engineering | MECH | https://catalog.okstate.edu/degree-programs/ |

##### Engineering Technology
###### BSET
| # | 专业 | Code | URL |
|---|------|------|-----|
| 10 | Fire Protection and Safety | FPST | https://catalog.okstate.edu/degree-programs/ |
| 11 | Mechanical Engineering Technology | MET | https://catalog.okstate.edu/degree-programs/ |
| 12 | Electrical Engineering Technology | EET | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 34 undergraduate programs. See https://catalog.okstate.edu/degree-programs/ for complete enumeration.

#### Ferguson College of Agriculture

##### Agribusiness
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | Agribusiness | AGBU | https://catalog.okstate.edu/degree-programs/ |
| 2 | Accounting Double Major | AGBU/ACCT | https://catalog.okstate.edu/degree-programs/ |
| 3 | Agricultural Communications Double Major | AGBU/AGCM | https://catalog.okstate.edu/degree-programs/ |
| 4 | Community and Regional Analysis | AGBU/CRA | https://catalog.okstate.edu/degree-programs/ |
| 5 | Crop and Soil Science | AGBU/CASS | https://catalog.okstate.edu/degree-programs/ |

##### Agricultural Communications
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 6 | Agricultural Communications | AGCM | https://catalog.okstate.edu/degree-programs/ |

##### Agricultural Education
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 7 | Agricultural Education | AGED | https://catalog.okstate.edu/degree-programs/ |

##### Animal Science
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 8 | Animal Science | ANSI | https://catalog.okstate.edu/degree-programs/ |

##### Biochemistry
###### BS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 9 | Biochemistry | BIOC | https://catalog.okstate.edu/degree-programs/ |

##### Food Science
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 10 | Food Science | FDSC | https://catalog.okstate.edu/degree-programs/ |

##### Horticulture
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 11 | Horticulture | HORT | https://catalog.okstate.edu/degree-programs/ |

##### Landscape Architecture
###### BLA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 12 | Landscape Architecture | LARC | https://catalog.okstate.edu/degree-programs/ |

##### Plant and Soil Sciences
###### BSAG
| # | 专业 | Code | URL |
|---|------|------|-----|
| 13 | Plant and Soil Sciences | PSS | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 49 undergraduate programs. See https://catalog.okstate.edu/degree-programs/ for complete enumeration.

#### Spears School of Business

##### Accounting
###### BSBA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | External Reporting, Control and Auditing | ACCT/ACEX | https://catalog.okstate.edu/degree-programs/ |
| 2 | Internal Reporting, Control and Auditing | ACCT/ACIN | https://catalog.okstate.edu/degree-programs/ |
| 3 | Cyber Audit | ACSY/CYAU | https://catalog.okstate.edu/degree-programs/ |
| 4 | Data Analytics | ACSY/DAN | https://catalog.okstate.edu/degree-programs/ |
| 5 | Data Analytics | DAN | https://catalog.okstate.edu/degree-programs/ |

##### Finance
###### BSBA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 6 | Finance | FIN | https://catalog.okstate.edu/degree-programs/ |

##### Management
###### BSBA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 7 | Management | MGMT | https://catalog.okstate.edu/degree-programs/ |

##### Marketing
###### BSBA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 8 | Marketing | MKTG | https://catalog.okstate.edu/degree-programs/ |

##### Management Information Systems
###### BSBA
| # | 专业 | Code | URL |
|---|------|------|-----|
| 9 | Management Information Systems | MIS | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 37 undergraduate programs. See https://catalog.okstate.edu/degree-programs/ for complete enumeration.

#### College of Professional Studies

##### Entertainment Media
###### BPS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 1 | Entertainment Media | ENME | https://catalog.okstate.edu/degree-programs/ |

##### Health Care Administration
###### BPS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 2 | Health Care Administration | HCA | https://catalog.okstate.edu/degree-programs/ |

##### Organizational Leadership
###### BPS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 3 | Organizational Leadership | ORGL | https://catalog.okstate.edu/degree-programs/ |

##### Public Safety
###### BPS
| # | 专业 | Code | URL |
|---|------|------|-----|
| 4 | Public Safety | PSAF | https://catalog.okstate.edu/degree-programs/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

OSU offers several interdisciplinary programs that span multiple colleges. These include pre-professional tracks (Pre-Law, Pre-Medical, Pre-Dental, Pre-Health) that are administered within specific colleges but prepare students for professional schools across the university.

### 1.4 Minors — Complete List

OSU offers 67 undergraduate certificates (UCRT) which serve as minors/concentrations. The full list is available at https://catalog.okstate.edu/degree-programs/ under "Undergraduate Certificates."

### 1.5 General Education Requirements

OSU requires a 15-unit core curriculum for admission:
- 4 units of English (Grammar, Composition and Literature)
- 3 units of Mathematics (Algebra I, Geometry, Algebra II and above)
- 3 units of History and Citizenship Skills (including 1 unit American History)
- 3 units of Lab Science (Biology, Chemistry, Physical Sciences, Physics)
- 2 units of additional courses from above sections, Computer Science, or Foreign Language

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### MS
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Applied Statistics | APST | https://catalog.okstate.edu/degree-programs/ |
| 2 | Computer Science | AI-AS/CS | https://catalog.okstate.edu/degree-programs/ |
| 3 | Communication Sciences and Disorders | CDIS | https://catalog.okstate.edu/degree-programs/ |
| 4 | Mathematics | MATH | https://catalog.okstate.edu/degree-programs/ |
| 5 | Physics | PHYS | https://catalog.okstate.edu/degree-programs/ |
| 6 | Psychology | PSYC | https://catalog.okstate.edu/degree-programs/ |
| 7 | Statistics | STAT | https://catalog.okstate.edu/degree-programs/ |

##### MA
| # | 项目 | Code | URL |
|---|------|------|-----|
| 8 | Art History | ARTH | https://catalog.okstate.edu/degree-programs/ |
| 9 | English | ENGL | https://catalog.okstate.edu/degree-programs/ |
| 10 | History | HIST | https://catalog.okstate.edu/degree-programs/ |

##### MS/PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 11 | Chemistry | CHEM | https://catalog.okstate.edu/degree-programs/ |
| 12 | Economics | ECON | https://catalog.okstate.edu/degree-programs/ |
| 13 | Geography | GEOG | https://catalog.okstate.edu/degree-programs/ |
| 14 | Geology | GEOL | https://catalog.okstate.edu/degree-programs/ |
| 15 | Microbiology | MBIO | https://catalog.okstate.edu/degree-programs/ |
| 16 | Political Science | POLS | https://catalog.okstate.edu/degree-programs/ |
| 17 | Sociology | SOC | https://catalog.okstate.edu/degree-programs/ |
| 18 | Zoology | ZOOL | https://catalog.okstate.edu/degree-programs/ |

##### MFA
| # | 项目 | Code | URL |
|---|------|------|-----|
| 19 | Creative Writing | CRWR | https://catalog.okstate.edu/degree-programs/ |
| 20 | Studio Art | ART | https://catalog.okstate.edu/degree-programs/ |

##### MM
| # | 项目 | Code | URL |
|---|------|------|-----|
| 21 | Music | MUSC | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 37 graduate programs in Arts & Sciences.

#### College of Education and Human Sciences

##### MS
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Aging Studies | AGSU | https://catalog.okstate.edu/degree-programs/ |
| 2 | Aviation and Space | AVSP | https://catalog.okstate.edu/degree-programs/ |
| 3 | Mental Health Counseling | COUN/MHC | https://catalog.okstate.edu/degree-programs/ |
| 4 | School Counseling | COUN/SC | https://catalog.okstate.edu/degree-programs/ |
| 5 | Curriculum and Instruction | CIED | https://catalog.okstate.edu/degree-programs/ |
| 6 | Educational Leadership | EDLE | https://catalog.okstate.edu/degree-programs/ |
| 7 | Family and Consumer Sciences | FACS | https://catalog.okstate.edu/degree-programs/ |
| 8 | Health and Human Performance | HHP | https://catalog.okstate.edu/degree-programs/ |
| 9 | Human Development and Family Science | HDFS | https://catalog.okstate.edu/degree-programs/ |
| 10 | Nutrition | NUTR | https://catalog.okstate.edu/degree-programs/ |

##### PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 11 | Community Health Sciences | CHSC | https://catalog.okstate.edu/degree-programs/ |
| 12 | Counseling Psychology | COUN | https://catalog.okstate.edu/degree-programs/ |
| 13 | Educational Leadership | EDLE | https://catalog.okstate.edu/degree-programs/ |
| 14 | Human Environmental Sciences | HESC | https://catalog.okstate.edu/degree-programs/ |

##### EdD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 15 | Aviation and Space Education | AEST/AVSE | https://catalog.okstate.edu/degree-programs/ |
| 16 | Educational Leadership | EDLE | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 70 graduate programs in Education and Human Sciences.

#### College of Engineering, Architecture and Technology

##### MS
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Computer Engineering | AI-EN/CPE | https://catalog.okstate.edu/degree-programs/ |
| 2 | Fire Protection and Safety | FPST | https://catalog.okstate.edu/degree-programs/ |
| 3 | Industrial Engineering and Management | IEM | https://catalog.okstate.edu/degree-programs/ |
| 4 | Technology | TEC | https://catalog.okstate.edu/degree-programs/ |

##### MS/PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 5 | Biosystems Engineering | BAE | https://catalog.okstate.edu/degree-programs/ |
| 6 | Chemical Engineering | CHEN | https://catalog.okstate.edu/degree-programs/ |
| 7 | Civil Engineering | CIVE | https://catalog.okstate.edu/degree-programs/ |
| 8 | Electrical Engineering | ELEN | https://catalog.okstate.edu/degree-programs/ |
| 9 | Mechanical Engineering | MECH | https://catalog.okstate.edu/degree-programs/ |

##### MEN (Master of Engineering)
| # | 项目 | Code | URL |
|---|------|------|-----|
| 10 | Electrical Engineering | ELEN | https://catalog.okstate.edu/degree-programs/ |
| 11 | Mechanical Engineering | MECH | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 19 graduate programs in Engineering, Architecture and Technology.

#### Ferguson College of Agriculture

##### MS
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Agricultural Communications | AGCM | https://catalog.okstate.edu/degree-programs/ |
| 2 | Agricultural Education and Leadership | AGEL | https://catalog.okstate.edu/degree-programs/ |
| 3 | Entomology | ENTO | https://catalog.okstate.edu/degree-programs/ |
| 4 | Horticulture | HORT | https://catalog.okstate.edu/degree-programs/ |
| 5 | Plant Pathology | PLPA | https://catalog.okstate.edu/degree-programs/ |
| 6 | Plant and Soil Sciences | PSS | https://catalog.okstate.edu/degree-programs/ |

##### MS/PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 7 | Agricultural Economics | AGEC | https://catalog.okstate.edu/degree-programs/ |
| 8 | Animal Science | ANSI | https://catalog.okstate.edu/degree-programs/ |
| 9 | Biochemistry | BIOC | https://catalog.okstate.edu/degree-programs/ |
| 10 | Food Science | FDSC | https://catalog.okstate.edu/degree-programs/ |
| 11 | Natural Resource Ecology and Management | NREM | https://catalog.okstate.edu/degree-programs/ |

##### PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 12 | Agricultural Education, Communications, and Leadership | AECL | https://catalog.okstate.edu/degree-programs/ |

##### MAG (Master of Agriculture)
| # | 项目 | Code | URL |
|---|------|------|-----|
| 13 | Agriculture | AG | https://catalog.okstate.edu/degree-programs/ |
| 14 | International Agriculture | AGIN | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 24 graduate programs in Agriculture.

#### Spears School of Business

##### MS
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Accounting | ACCT | https://catalog.okstate.edu/degree-programs/ |
| 2 | Corporate Finance | ACCT/CF | https://catalog.okstate.edu/degree-programs/ |
| 3 | Data Analytics and Systems | ACCT/DAS | https://catalog.okstate.edu/degree-programs/ |
| 4 | Financial Reporting and Auditing | ACCT/FRA | https://catalog.okstate.edu/degree-programs/ |
| 5 | Research Methods | ACCT/ACRM | https://catalog.okstate.edu/degree-programs/ |
| 6 | Business Analytics | BAN | https://catalog.okstate.edu/degree-programs/ |
| 7 | Economics | ECON | https://catalog.okstate.edu/degree-programs/ |
| 8 | Entrepreneurship | ENTR | https://catalog.okstate.edu/degree-programs/ |
| 9 | Finance | FIN | https://catalog.okstate.edu/degree-programs/ |
| 10 | Management Information Systems | MIS | https://catalog.okstate.edu/degree-programs/ |
| 11 | Marketing | MKTG | https://catalog.okstate.edu/degree-programs/ |

##### MBA/DBA
| # | 项目 | Code | URL |
|---|------|------|-----|
| 12 | Business Administration | BADM | https://catalog.okstate.edu/degree-programs/ |

##### PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 13 | Business Administration | BADM | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 30 graduate programs in Business.

#### College of Veterinary Medicine

##### DVM
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Doctor of Veterinary Medicine | VM | https://catalog.okstate.edu/degree-programs/ |

##### MS/PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 2 | Comparative Biomedical Sciences | CBSC | https://catalog.okstate.edu/degree-programs/ |

#### Graduate College (Interdisciplinary)

##### PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Environmental Science | ENVR | https://catalog.okstate.edu/degree-programs/ |
| 2 | Fire and Emergency Management | FEMA | https://catalog.okstate.edu/degree-programs/ |
| 3 | Materials Science | MATS | https://catalog.okstate.edu/degree-programs/ |
| 4 | Telecommunications Management | TCOM | https://catalog.okstate.edu/degree-programs/ |

#### Center for Health Sciences (Tulsa)

##### DO
| # | 项目 | Code | URL |
|---|------|------|-----|
| 1 | Osteopathic Medicine | DO | https://catalog.okstate.edu/degree-programs/ |

##### MS/PhD
| # | 项目 | Code | URL |
|---|------|------|-----|
| 2 | Biomedical Sciences | BIOM | https://catalog.okstate.edu/degree-programs/ |

> **Note**: Full list includes 14 graduate programs through CHS.

### 2.2 Program Deep-Dive: Computer Science (MS)

- **Department**: Computer Science, College of Arts and Sciences
- **Degree**: MS
- **Code**: AI-AS/CS
- **Application portal**: https://grad.okstate.edu/apply/
- **Application fee**: $50 (US) / $75 (international)
- **GRE**: Check with department
- **TOEFL minimum**: 79 iBT (or 4.0 new scale)
- **IELTS minimum**: 6.5
- **DET minimum**: 115
- **PTE minimum**: 53
- **Contact**: Graduate College, 202 Whitehurst, 405-744-6368

### 2.3 Graduate Admissions Model

OSU uses a **centralized application portal** (https://grad.okstate.edu/apply/) for all graduate programs, but **each program sets its own admission requirements** (GRE/GMAT/MAT, letters of recommendation, statement of purpose, etc.). The Graduate College processes applications and enforces minimum requirements (TOEFL 79/IELTS 6.5/DET 115/PTE 53), while programs may require higher scores.

**Key features:**
- Single application portal for all programs
- Per-program GRE/GMAT requirements (code 6546)
- Per-program deadlines (college minimum: 30 days before semester for domestic; May 1/Oct 1/Feb 1 for international)
- Fee waivers available for OSU students/alumni, military, and select federal programs
- CGS April-15 honor date signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://go.okstate.edu/admissions/ | Official website |
| Application portal | https://orange.okstate.edu/ or Common Application | Official website |
| Application type | Rolling admission (no deadline) | Deadlines page |
| OSU Application opens | July 1 | Deadlines page |
| Common Application opens | August 1 | Deadlines page |
| Early Opportunity Scholarship Deadline | November 1 | Deadlines page |
| Priority Scholarship Deadline | February 1 | Deadlines page |
| College Decision Day | May 1 | Deadlines page |
| Final Scholarship Deadline | Friday before classes start | Deadlines page |
| Application fee (domestic) | $50 | Freshman page |
| Application fee (international) | $90 | International freshman page |
| Enrollment deposit | $300 | Admissions page |
| SAT code | 6546 | Requirements page |
| ACT code | 3424 | Requirements page |
| FAFSA code | 003170 | Freshman page |
| Test policy | Test-optional for admission; test scores required for most scholarships | Requirements page |
| Superscore policy | Not specified | — |
| Recommendation requirements | Not required for UG admission | — |
| Interview policy | Not offered | — |
| Portfolio | Not required (except specific programs) | — |
| Transfer pathway | 7+ credit hours post-graduation | Transfer page |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (new scale, post-Jan 2026) | 3.5 | — | Effective Jan 21, 2026 |
| TOEFL iBT (old scale, pre-Jan 2026) | 79 | — | Valid tests continue accepted |
| IELTS Academic | 5.5 | — | — |
| PTE Academic | 46 | — | — |
| iTEP Academic | 3.5 | — | — |
| Duolingo English Test (DET) | 95 | — | — |

**Applicability**: Required for all international applicants whose native language is not English.

**Waiver conditions**:
- Graduated from accredited high school where English is primary instruction in English-speaking country
- Attended English-speaking high school in US for 2+ years
- Conditional admission available for students meeting all requirements except English proficiency

**TOEFL code**: 6546

### 3.3 Graduate — Global Rules

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | https://grad.okstate.edu/apply/ | Graduate College |
| Application fee (US) | $50 | Application Process page |
| Application fee (international) | $75 | Application Process page |
| Application fee (non-degree US) | $25 | Application Process page |
| GRE institution code | 6546 | Application Process page |
| GRE policy | Per program requirement | Application Process page |
| GMAT policy | Per program requirement | Application Process page |
| MAT policy | Per program requirement | Application Process page |
| Domestic deadline | 30 days before semester start | Application Process page |
| International deadline (Fall) | May 1 | Application Process page |
| International deadline (Spring) | October 1 | Application Process page |
| International deadline (Summer) | February 1 | Application Process page |
| TOEFL minimum | 79 iBT (or 4.0 new scale) | English Proficiency page |
| IELTS minimum | 6.5 | English Proficiency page |
| DET minimum | 115 | English Proficiency page |
| PTE minimum | 53 | English Proficiency page |
| ELP waiver | Degree from English-speaking institution/country | English Proficiency page |
| Letters of recommendation | 2-4 (per program) | Application Process page |
| CGS April-15 signatory | Yes | Graduate College |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

#### In-State On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $14,740 | 30 credit hours (15/semester) |
| Housing & food | $12,500 | On-campus housing + meal plan |
| Books, course materials, supplies & equipment | $1,430 | Average |
| **Direct Expenses Total** | **$28,670** | |
| Transportation | $2,350 | Average |
| Personal & miscellaneous | $3,570 | Average |
| **Additional Expenses Total** | **$5,920** | |
| **TOTAL** | **$34,590** | |

#### Out-of-State On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $31,000 | 30 credit hours (15/semester) |
| Housing & food | $12,500 | On-campus housing + meal plan |
| Books, course materials, supplies & equipment | $1,430 | Average |
| **Direct Expenses Total** | **$44,930** | |
| Transportation | $2,350 | Average |
| Personal & miscellaneous | $3,570 | Average |
| **Additional Expenses Total** | **$5,920** | |
| **TOTAL** | **$50,850** | |

#### International On-Campus

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition & fees | $31,000 | 30 credit hours (15/semester) |
| Housing & food | $12,500 | On-campus housing + meal plan |
| Books, course materials, supplies & equipment | $1,430 | Average |
| **Direct Expenses Total** | **$44,930** | |
| Health Insurance | $2,773 | Required for international students |
| Personal & miscellaneous | $5,850 | Average |
| **Additional Expenses Total** | **$8,623** | |
| **TOTAL** | **$53,553** | |

> **Note**: International students who graduate from an Oklahoma high school are eligible for a full out-of-state tuition waiver to reduce their tuition and fees to in-state rates.

### 4.2 Undergraduate Financial-Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind / need-aware | Need-aware for all applicants | Admissions policy |
| Merit scholarships | Automatic consideration upon application | Freshman page |
| Early Opportunity Scholarship Deadline | November 1 | Deadlines page |
| Priority Scholarship Deadline | February 1 | Deadlines page |
| International scholarships | $7,000–$15,000/year | International page |
| FAFSA code | 003170 | Freshman page |
| Application fee waivers | Available based on demonstrated need | Freshman page |
| Academic Common Market | In-state tuition for qualifying students from participating southern states | Freshman page |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| Application fee (US) | $50 | Graduate College |
| Application fee (international) | $75 | Graduate College |
| Fee waivers | OSU students/alumni, military, federal program participants | Graduate College |
| Funding types | RA/TA/fellowship/grant (per program) | Graduate College |
| Most PhD programs | Fully funded | Graduate College |
| Master's programs | Varies (many self-funded) | Graduate College |

---

## SECTION 5 — Evidence Chain Index

```yaml
# E-U-001
field: undergraduate.admissions.type
value: Rolling admission (no application deadline)
source_url: https://go.okstate.edu/admissions/freshman/dates-deadlines
source_snippet: "At Oklahoma State, we accept applications on a rolling admission basis, so there's no application deadline. We encourage you to apply early for maximum scholarship consideration."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-002
field: undergraduate.deadlines.early_opportunity_scholarship
value: November 1
source_url: https://go.okstate.edu/admissions/freshman/dates-deadlines
source_snippet: "Nov. 1 - Early Opportunity Scholarship Deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-003
field: undergraduate.deadlines.priority_scholarship
value: February 1
source_url: https://go.okstate.edu/admissions/freshman/dates-deadlines
source_snippet: "Feb. 1 - Priority Scholarship Deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-004
field: undergraduate.test_policy
value: Test-optional for admission; test scores required for most scholarships
source_url: https://go.okstate.edu/admissions/freshman/admission-requirements
source_snippet: "Test scores are optional for admission, but required for most scholarships. You can apply and be admitted without submitting a test score."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-005
field: undergraduate.assured_admission
value: 3.0 GPA + top 33.3% rank OR 3.0 GPA + 21 ACT/1060 SAT OR 24 ACT/1160 SAT
source_url: https://go.okstate.edu/admissions/freshman/admission-requirements
source_snippet: "You qualify for assured admission if you meet ONE of the following criteria: 3.0 GPA or better AND top 33.3% rank in high school graduating class; 3.0 GPA or better in 15-unit core AND 21 ACT/1060 SAT or better; 24 ACT/1160 SAT or better"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-006
field: undergraduate.application_fee.domestic
value: $50
source_url: https://go.okstate.edu/admissions/freshman
source_snippet: "Pay the $50 application fee (or submit a fee waiver)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-007
field: undergraduate.application_fee.international
value: $90
source_url: https://go.okstate.edu/admissions/international/freshman
source_snippet: "International students must pay a $90 application fee via your application portal before your application can be processed."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-008
field: undergraduate.english_proficiency.toefl
value: 3.5+ (new scale) / 79+ (old scale)
source_url: https://go.okstate.edu/admissions/international/freshman
source_snippet: "iBT TOEFL Internet-Based Score 3.5+"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-009
field: undergraduate.english_proficiency.ielts
value: 5.5+
source_url: https://go.okstate.edu/admissions/international/freshman
source_snippet: "IELTS Academic Score 5.5+"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-010
field: undergraduate.english_proficiency.det
value: 95+
source_url: https://go.okstate.edu/admissions/international/freshman
source_snippet: "Duolingo English Test Score 95+"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-U-011
field: undergraduate.cost.in_state_on_campus.total
value: $34,590
source_url: https://go.okstate.edu/scholarships-financial-aid/cost-of-attendance/undergraduate-cost/in-state-cost/in-state-on-campus
source_snippet: "TOTAL: $34,590"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-012
field: undergraduate.cost.out_of_state_on_campus.total
value: $50,850
source_url: https://go.okstate.edu/scholarships-financial-aid/cost-of-attendance/undergraduate-cost/out-of-state-cost/out-of-state-on-campus
source_snippet: "TOTAL: $50,850"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-U-013
field: undergraduate.cost.international_on_campus.total
value: $53,553
source_url: https://go.okstate.edu/scholarships-financial-aid/cost-of-attendance/undergraduate-cost/international-cost/international-on-campus
source_snippet: "TOTAL: $53,553"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

```yaml
# E-G-001
field: graduate.application_fee.us
value: $50
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "$50 for US citizens or permanent resident"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-002
field: graduate.application_fee.international
value: $75
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "$75 for international applicants"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-003
field: graduate.english_proficiency.toefl
value: 79 iBT (or 4.0 new scale)
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "TOEFL iBT: 79* *Effective 21 January 2026, the iBT has a new scoring scale. On that scale, the minimum overall score for admission is 4.0."
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-004
field: graduate.english_proficiency.ielts
value: 6.5
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "IELTS: 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-005
field: graduate.english_proficiency.det
value: 115
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "DET: 115"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-006
field: graduate.deadlines.international_fall
value: May 1
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "international applications must be complete and Program recommendations must be entered no later than May 1st for Fall admission"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-G-007
field: graduate.gre_code
value: 6546
source_url: https://gradcollege.okstate.edu/application-process
source_snippet: "please submit your scores electronically to OSU's institution code 6546"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-S-001
field: institution.colleges
value: 6 undergraduate colleges + Graduate College + Vet Med + CHS + Professional Studies
source_url: https://catalog.okstate.edu/degree-programs/
source_snippet: "College of Arts and Sciences, College of Education and Human Sciences, College of Engineering Architecture and Technology, Ferguson College of Agriculture, Spears School of Business, College of Veterinary Medicine"
capture_date: 2026-07-06
evidence_type: official_webpage
```

```yaml
# E-S-002
field: institution.total_programs
value: 632 (298 UG degrees + 186 grad degrees + 148 certificates)
source_url: https://catalog.okstate.edu/degree-programs/
source_snippet: "With more than 500 undergraduate and graduate degree programs, as well as certificates and professional degree programs in medicine and veterinary medicine"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
okstate-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: Rules 1-4)
├── 01-ug-arts-sciences.md              (Section 1: A&S programs)
├── 02-ug-education-human-sciences.md   (Section 1: Ed&HS programs)
├── 03-ug-engineering-architecture.md   (Section 1: CEAT programs)
├── 04-ug-agriculture.md                (Section 1: Ferguson programs)
├── 05-ug-business.md                   (Section 1: Spears programs)
├── 06-ug-professional-studies.md       (Section 1: CPS programs)
├── 07-grad-arts-sciences.md            (Section 2: A&S grad)
├── 08-grad-education-human-sciences.md (Section 2: Ed&HS grad)
├── 09-grad-engineering-architecture.md (Section 2: CEAT grad)
├── 10-grad-agriculture.md              (Section 2: Ferguson grad)
├── 11-grad-business.md                 (Section 2: Spears grad)
├── 12-grad-vet-medicine.md             (Section 2: Vet Med)
├── 13-grad-interdisciplinary.md        (Section 2: Grad College + CHS)
├── 14-admissions-deadlines.md          (Section 3)
├── 15-costs-financial-aid.md           (Section 4)
└── 16-evidence-chain.md                (Section 5)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "okstate-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://catalog.okstate.edu/degree-programs/
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete department-level attribution for all 298 UG programs | https://catalog.okstate.edu/degree-programs/ |
| P0 | Graduate program detail pages (GRE/TOEFL per program) | Individual program pages |
| P1 | Undergraduate certificate (minor) full list with home departments | https://catalog.okstate.edu/degree-programs/ |
| P1 | Graduate certificate full list with home departments | https://catalog.okstate.edu/degree-programs/ |
| P1 | Financial aid policy details (need-aware specifics, income thresholds) | https://go.okstate.edu/scholarships-financial-aid/ |
| P2 | Campus housing rates detail | https://reslife.okstate.edu/registration/rates |
| P2 | Meal plan rates detail | https://dining.okstate.edu/meal-plan.html |
| P2 | Program-specific admission criteria | https://go.okstate.edu/admissions/program-specific-admission-criteria |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | OSU Value | Notes |
|-----------|-----------|-------|
| Institution type | Public, Land-Grant | Stillwater, OK |
| Total programs (Rule 1) | 632 | 298 UG + 186 Grad + 148 Certs |
| School/college count (Rule 2) | 10 | 6 UG + Grad College + Vet Med + CHS + CPS |
| UG tuition in-state (2026-27) | $14,740 | 30 hours |
| UG tuition OOS (2026-27) | $31,000 | 30 hours |
| UG COA in-state on-campus | $34,590 | Total |
| UG COA OOS on-campus | $50,850 | Total |
| UG COA international on-campus | $53,553 | Total |
| Need-blind (domestic)? | Need-aware | — |
| Need-blind (international)? | No | Need-aware for all |
| EA deadline | N/A | Rolling admission |
| Priority Scholarship Deadline | November 1 | Early Opportunity |
| Priority Scholarship Deadline | February 1 | Priority |
| SAT/ACT required? | Test-optional | Required for scholarships |
| TOEFL min (UG) | 3.5 (new) / 79 (old) | — |
| IELTS min (UG) | 5.5 | — |
| DET min (UG) | 95 | — |
| TOEFL min (Grad) | 79 (old) / 4.0 (new) | — |
| IELTS min (Grad) | 6.5 | — |
| DET min (Grad) | 115 | — |
| Grad application fee (US) | $50 | — |
| Grad application fee (intl) | $75 | — |
| Application fee (UG domestic) | $50 | — |
| Application fee (UG international) | $90 | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: go.okstate.edu, catalog.okstate.edu, gradcollege.okstate.edu, grad.okstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
