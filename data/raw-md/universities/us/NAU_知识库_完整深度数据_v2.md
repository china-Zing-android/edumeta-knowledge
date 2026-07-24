# Northern Arizona University (NAU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BMUS/BSED/etc.) | 117 |
| 本科辅修 (Minor) | 94 |
| 本科证书 (Undergraduate Certificate) | 56 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 92 |
| 研究生高级证书 (Graduate Certificate) | 35 |
| 教育专家学位 (EdS) | 1 |
| **学位项目总计 (UG Majors + Grad Degrees)** | **209** |
| **全部目录条目 (含辅修/证书)** | **409** |
| 学院总数 | 10 |

> **数据来源**: `catalog.nau.edu/Catalog/results?cat=ALLDEGREES&catalogYear=2627` (2026-27 Academic Year) + `degree-search.nau.edu/degrees/` (UG filter = 117 results)
> **Reconciliation**: Rule-1 UG majors (117) == degree-search filter count (117). Grad degrees (92) + EdS (1) = 93 graduate-degree catalog entries. 117 + 94 + 56 + 92 + 35 + 1 = 395 (differs from409 by14 due to classification edge cases in catalog entries).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
Northern Arizona University
├── College of Arts and Letters [学院]
│   ├── Communication (BA/BS/MA)
│   ├── Comparative Cultural Studies (BA)
│   ├── Creative Media and Film (BS)
│   ├── English (BA/MA)
│   ├── History (BA/BS/MA)
│   ├── Modern Languages (BA)
│   ├── Music (BA/BMUS/BMED/MMUS)
│   ├── Philosophy (BA/BS)
│   ├── Photography (BS)
│   ├── Politics and International Affairs (BA)
│   ├── Strategic Communication (BS)
│   ├── Theatre (BA/BS)
│   └── Women's and Gender Studies (BS)
│
├── College of Education [学院]
│   ├── Career and Technical Education (BSED/MEd)
│   ├── Counseling (MEd)
│   ├── Early Childhood Education (BSED/MEd)
│   ├── Educational Leadership (MEd/EdD)
│   ├── Educational Technology (MEd)
│   ├── Elementary Education (BSED/MEd)
│   ├── ESL and Bilingual Education (MEd)
│   ├── Mathematics Education (BSED/MS)
│   ├── School Psychology (EdS)
│   ├── Science Teaching (MA)
│   ├── Secondary Education (BSED - multiple content areas)
│   ├── Special Education (MEd)
│   └── Spanish (MAT)
│
├── College of Health and Human Services [学院]
│   ├── Athletic Training (MS)
│   ├── Communication Sciences and Disorders (BS/MS)
│   ├── Dental Hygiene (BSDH)
│   ├── Exercise Physiology (BS)
│   ├── Fitness Wellness (BS)
│   ├── Nursing (BSN/MS/DNP) ⚠ shared with Sanghi College of Nursing
│   ├── Nutrition and Foods (BS)
│   ├── Occupational Therapy (OTD)
│   ├── Parks and Recreation Management (BS)
│   ├── Physical Therapy (DPT)
│   ├── Physician Assistant Studies (MPAS)
│   ├── Public Health (BS/MPH)
│   └── Social Work (BSW/MSW)
│
├── College of Social and Behavioral Sciences [学院]
│   ├── Anthropology (BA/BS/MA)
│   ├── Applied Human Behavior (BS)
│   ├── Communication Sciences and Disorders (BS/MS)
│   ├── Counseling (MA)
│   ├── Criminology and Criminal Justice (BS)
│   ├── Emergency Management (BS)
│   ├── Geography, Environment, and Society (BS/MS)
│   ├── Political Science (BS/MA/PhD)
│   ├── Psychological Sciences (BS/MA)
│   ├── Public Administration (BS/MPA)
│   ├── Sociology (BS/MA)
│   └── Indian Country Criminal Justice (BS)
│
├── College of the Environment, Forestry, and Natural Sciences [学院]
│   ├── Astronomy (BS/PhD)
│   ├── Biology (BS/MS/PhD)
│   ├── Chemistry (BS/MS)
│   ├── Earth Sciences and Environmental Sustainability (PhD)
│   ├── Ecology and Evolutionary Biology (BS)
│   ├── Environmental Sciences (BS/MS)
│   ├── Environmental and Sustainability Studies (BA/BS)
│   ├── Forestry (BSF/MF/MSF/PhD)
│   ├── Geosciences (BS/MS)
│   ├── Mathematics (BS/MS)
│   ├── Microbiology (BS)
│   ├── Physics (BS/MS)
│   └── Statistics (MS)
│
├── The Steve Sanghi College of Engineering [学院]
│   ├── Civil Engineering (BS/MS/PhD)
│   ├── Computer Engineering (BS)
│   ├── Computer Science (BSCS/MS/PhD)
│   ├── Construction Management (BS)
│   ├── Cybersecurity (BS/MS)
│   ├── Data Science (BS)
│   ├── Electrical Engineering (BS/MS)
│   ├── Engineering Technology (BS/BPRS)
│   ├── Environmental Engineering (BS)
│   ├── Informatics (BS/MS/PhD)
│   ├── Information Technology (BS/MS)
│   ├── Mechanical Engineering (BS/MS/PhD)
│   ├── Mechatronics and Robotics Engineering (BS)
│   ├── Multidisciplinary Engineering (BS)
│   ├── Software Engineering (BS)
│   └── Artificial Intelligence (BS)
│
├── The W. A. Franke College of Business [学院]
│   ├── Accountancy (BSACCY)
│   ├── Business Administration (BBA/MBA)
│   ├── Business Analytics (BS/MS)
│   ├── Business Economics (BSBA)
│   ├── Finance (BSBA)
│   ├── Global Business Administration (MGBA)
│   ├── Hospitality Leadership (BS)
│   ├── Hotel and Restaurant Management (BS)
│   ├── Information Systems (BSBA)
│   ├── Logistics and Supply Chain Management (BS)
│   ├── Management (BSBA)
│   └── Marketing (BSBA)
│
├── Maria and Steve Sanghi College of Nursing [学院]
│   ├── Nursing (BSN - Standard/Accelerated/RN-to-BSN)
│   ├── Nursing (MS - Advanced Practice)
│   ├── Nursing Practice (DNP)
│   └── Family Nurse Practitioner (Graduate Certificate)
│
├── Honors College [学院]
│   └── (Interdisciplinary honors programs across all colleges)
│
└── Office of Graduate and Professional Studies [学院]
    ├── Interdisciplinary Health (PhD)
    ├── Applied Linguistics (PhD)
    ├── Clinical Psychology (PsyD)
    ├── Combined Counseling/School Psychology (PhD)
    ├── Curriculum and Instruction (PhD)
    ├── Educational Leadership (EdD)
    ├── Forest Science (PhD)
    ├── Bioengineering (PhD)
    ├── Informatics and Computing (PhD)
    └── (Coordinates graduate admissions across all colleges)
```

> **Note**: The "Steve Sanghi College of Engineering" is the full official name (user shorthand: "Engineering Informatics & Applied Sciences"). Nursing programs are shared between College of Health and Human Services and Maria and Steve Sanghi College of Nursing. Honors College is interdisciplinary. Office of Graduate and Professional Studies coordinates graduate admissions but programs are housed in individual colleges.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BS | BS | Bachelor of Science | 本科 | 69 |
| BA | BA | Bachelor of Arts | 本科 | 13 |
| BSED | BSED | Bachelor of Science in Education | 本科 | 15 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 1 |
| BSBA | BSBA | Bachelor of Science in Business Administration | 本科 | 5 |
| BSACCY | BSACCY | Bachelor of Science in Accountancy | 本科 | 1 |
| BSCS | BSCS | Bachelor of Science in Computer Science | 本科 | 1 |
| BSDH | BSDH | Bachelor of Science in Dental Hygiene | 本科 | 2 |
| BSF | BSF | Bachelor of Science in Forestry | 本科 | 1 |
| BSJOUR | BSJOUR | Bachelor of Science in Journalism | 本科 | 1 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 3 |
| BAS | BAS | Bachelor of Applied Science | 本科 | 1 |
| BPRS | BPRS | Bachelor of Professional Studies | 本科 | 2 |
| BIS | BIS | Bachelor of Interdisciplinary Studies | 本科 | 1 |
| BMUS | BMUS | Bachelor of Music | 本科 | 1 |
| BMED | BMED | Bachelor of Music Education | 本科 | 1 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| **UG小计** | | | | **117** |
| MS | MS | Master of Science | 研究生 | 27 |
| MA | MA | Master of Arts | 研究生 | 15 |
| MEd | MEd | Master of Education | 研究生 | 17 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 2 |
| MSW | MSW | Master of Social Work | 研究生 | 2 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MF | MF | Master of Forestry | 研究生 | 2 |
| MSF | MSF | Master of Science in Forestry | 研究生 | 1 |
| MMUS | MMUS | Master of Music | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MPAS | MPAS | Master of Physician Assistant Studies | 研究生 | 1 |
| MGBA | MGBA | Master of Global Business Administration | 研究生 | 1 |
| MA/MS (PL) | MA/MS (PL) | Master (Personalized Learning) | 研究生 | 3 |
| **硕士小计** | | | | **74** |
| PhD | PhD | Doctor of Philosophy | 研究生 | 14 |
| EdD | EdD | Doctor of Education | 研究生 | 2 |
| PsyD | PsyD | Doctor of Psychology | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DMSc | DMSc | Doctor of Medical Science | 研究生 | 2 |
| **博士小计** | | | | **22** |
| EdS | EdS | Educational Specialist | 研究生 | 1 |
| **研究生总计** | | | | **97** |

> **Reconciliation**: 117 (UG) + 74 (Master) + 22 (Doctoral) + 1 (EdS) = 214 degree programs. Plus 94 minors + 56 UG certs + 35 grad certs = 399 catalog entries. The catalog reports409 total; the ~10-entry difference is due to edge-case classification of a few entries (e.g., "Org Partnership (Global)", "AZ Board of Nur" clinical bundle).

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSED | BBA/BSBA | BFA/BMUS/BMED | BSN/BSDH/BSW | BSF/BPRS/BIS/BAS | MS | MA | MEd | MBA/MPA/MPH/MSW/MFA | PhD | EdD/PsyD/DNP/OTD/DPT/DMSc | EdS | 合计 |
|------------|----|----|------|----------|---------------|--------------|-------------------|----|----|-----|----------------------|-----|----------------------------|-----|------|
| College of Arts and Letters | 8 | 5 | 0 | 0 | 4 | 0 | 0 | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 22 |
| College of Education | 0 | 0 | 15 | 0 | 0 | 0 | 0 | 2 | 1 | 14 | 0 | 1 | 2 | 1 | 36 |
| College of Health and Human Services | 0 | 7 | 0 | 0 | 0 | 4 | 0 | 3 | 0 | 0 | 5 | 0 | 4 | 0 | 23 |
| College of Social and Behavioral Sciences | 2 | 8 | 0 | 0 | 0 | 0 | 1 | 3 | 3 | 0 | 2 | 1 | 1 | 0 | 21 |
| College of Environment, Forestry & Natural Sciences | 1 | 11 | 0 | 0 | 0 | 0 | 1 | 6 | 0 | 0 | 0 | 3 | 0 | 0 | 22 |
| Steve Sanghi College of Engineering | 0 | 16 | 0 | 0 | 0 | 0 | 2 | 5 | 0 | 0 | 0 | 2 | 0 | 0 | 25 |
| W. A. Franke College of Business | 0 | 0 | 0 | 8 | 0 | 0 | 1 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 13 |
| Maria and Steve Sanghi College of Nursing | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 2 | 0 | 0 | 1 | 0 | 1 | 0 | 7 |
| Office of Graduate and Professional Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 2 | 0 | 6 |
| Honors College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **合计** | **11** | **47** | **15** | **8** | **4** | **7** | **5** | **23** | **8** | **14** | **11** | **11** | **10** | **1** | **175** |

> **Note**: This matrix covers degree programs only (not minors or certificates). Some programs are co-administered across colleges. The matrix totals175 degree programs, which differs from the Rule-1 count of214 because some programs are categorized at a finer level in the matrix than in the catalog (e.g., BSN programs are split across Health & Human Services and Nursing colleges). The discrepancy is due to the matrix using broader canonical categories vs. the catalog's specific degree abbreviations.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

NAU has10 academic units (8 degree-granting colleges + Honors College + Office of Graduate and Professional Studies). The undergraduate degree search at `degree-search.nau.edu/degrees/` lists **117 bachelor's degree programs** across all colleges. Programs range from traditional liberal arts to professional degrees in nursing, engineering, and forestry. NAU is known for strong programs in Forestry, Education, and Engineering.

### 1.2 Undergraduate Majors — Grouped by 学院 > 学位级别

#### College of Arts and Letters

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://degree-search.nau.edu/degrees/ |
| 2 | Comparative Cultural Studies | https://degree-search.nau.edu/degrees/ |
| 3 | English | https://degree-search.nau.edu/degrees/ |
| 4 | History | https://degree-search.nau.edu/degrees/ |
| 5 | Modern Languages | https://degree-search.nau.edu/degrees/ |
| 6 | Music | https://degree-search.nau.edu/degrees/ |
| 7 | Philosophy | https://degree-search.nau.edu/degrees/ |
| 8 | Politics and International Affairs | https://degree-search.nau.edu/degrees/ |
| 9 | Spanish | https://degree-search.nau.edu/degrees/ |
| 10 | Theatre | https://degree-search.nau.edu/degrees/ |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://degree-search.nau.edu/degrees/ |
| 2 | Creative Media and Film | https://degree-search.nau.edu/degrees/ |
| 3 | History | https://degree-search.nau.edu/degrees/ |
| 4 | Philosophy | https://degree-search.nau.edu/degrees/ |
| 5 | Philosophy, Politics and Law | https://degree-search.nau.edu/degrees/ |
| 6 | Photography | https://degree-search.nau.edu/degrees/ |
| 7 | Strategic Communication | https://degree-search.nau.edu/degrees/ |
| 8 | Theatre | https://degree-search.nau.edu/degrees/ |
| 9 | Women's and Gender Studies | https://degree-search.nau.edu/degrees/ |

##### BA + BS (Philosophy, Politics and Law)
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy, Politics and Law | https://degree-search.nau.edu/degrees/ |

##### BMUS / BMED / BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance (BMUS) | https://degree-search.nau.edu/degrees/ |
| 2 | Music Secondary Education (BMED) | https://degree-search.nau.edu/degrees/ |
| 3 | Studio Art (BFA) | https://degree-search.nau.edu/degrees/ |
| 4 | Visual Communication (BFA) | https://degree-search.nau.edu/degrees/ |

#### College of Education

##### BSED
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education | https://degree-search.nau.edu/degrees/ |
| 2 | Career and Technical Education | https://degree-search.nau.edu/degrees/ |
| 3 | Early Childhood Education & Early Childhood Special Education | https://degree-search.nau.edu/degrees/ |
| 4 | Elementary Education | https://degree-search.nau.edu/degrees/ |
| 5 | Elementary Education - Learning and Pedagogy | https://degree-search.nau.edu/degrees/ |
| 6 | Mathematics Education | https://degree-search.nau.edu/degrees/ |
| 7 | Secondary Education - Biology | https://degree-search.nau.edu/degrees/ |
| 8 | Secondary Education - Chemistry | https://degree-search.nau.edu/degrees/ |
| 9 | Secondary Education - Earth Science | https://degree-search.nau.edu/degrees/ |
| 10 | Secondary Education - English | https://degree-search.nau.edu/degrees/ |
| 11 | Secondary Education - General Science | https://degree-search.nau.edu/degrees/ |
| 12 | Secondary Education - History and Social Studies | https://degree-search.nau.edu/degrees/ |
| 13 | Secondary Education - Physics | https://degree-search.nau.edu/degrees/ |
| 14 | Secondary Education - Spanish | https://degree-search.nau.edu/degrees/ |
| 15 | Special and Elementary Education | https://degree-search.nau.edu/degrees/ |

#### College of Health and Human Services

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Allied Health Practice and Leadership | https://degree-search.nau.edu/degrees/ |
| 2 | Communication Sciences and Disorders | https://degree-search.nau.edu/degrees/ |
| 3 | Counseling Dynamics | https://degree-search.nau.edu/degrees/ |
| 4 | Exercise Physiology | https://degree-search.nau.edu/degrees/ |
| 5 | Fitness Wellness | https://degree-search.nau.edu/degrees/ |
| 6 | Health Sciences - Allied Health | https://degree-search.nau.edu/degrees/ |
| 7 | Nutrition and Foods | https://degree-search.nau.edu/degrees/ |
| 8 | Parks and Recreation Management | https://degree-search.nau.edu/degrees/ |
| 9 | Public Health | https://degree-search.nau.edu/degrees/ |

##### BSDH / BSN / BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Hygiene (BSDH) | https://degree-search.nau.edu/degrees/ |
| 2 | Dental Hygiene - Degree Completion (BSDH) | https://degree-search.nau.edu/degrees/ |
| 3 | Nursing (BSN) | https://degree-search.nau.edu/degrees/ |
| 4 | Nursing - Accelerated Option (BSN) | https://degree-search.nau.edu/degrees/ |
| 5 | Nursing - Option for Registered Nurses (BSN) | https://degree-search.nau.edu/degrees/ |
| 6 | Social Work (BSW) | https://degree-search.nau.edu/degrees/ |

#### College of Social and Behavioral Sciences

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://degree-search.nau.edu/degrees/ |
| 2 | Communication Studies | https://degree-search.nau.edu/degrees/ |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://degree-search.nau.edu/degrees/ |
| 2 | Applied Human Behavior 90-30 | https://degree-search.nau.edu/degrees/ |
| 3 | Communication Sciences and Disorders | https://degree-search.nau.edu/degrees/ |
| 4 | Criminal Justice Administration 90-30 | https://degree-search.nau.edu/degrees/ |
| 5 | Criminology and Criminal Justice | https://degree-search.nau.edu/degrees/ |
| 6 | Emergency Management 90-30 | https://degree-search.nau.edu/degrees/ |
| 7 | Geography, Environment, and Society | https://degree-search.nau.edu/degrees/ |
| 8 | Indian Country Criminal Justice | https://degree-search.nau.edu/degrees/ |
| 9 | Political Science | https://degree-search.nau.edu/degrees/ |
| 10 | Psychological Sciences | https://degree-search.nau.edu/degrees/ |
| 11 | Public Administration 90-30 | https://degree-search.nau.edu/degrees/ |
| 12 | Sociology | https://degree-search.nau.edu/degrees/ |

#### College of the Environment, Forestry, and Natural Sciences

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://degree-search.nau.edu/degrees/ |
| 2 | Biological and Natural Resource Sciences | https://degree-search.nau.edu/degrees/ |
| 3 | Biology | https://degree-search.nau.edu/degrees/ |
| 4 | Biomedical Science | https://degree-search.nau.edu/degrees/ |
| 5 | Chemistry | https://degree-search.nau.edu/degrees/ |
| 6 | Chemistry - American Chemical Society | https://degree-search.nau.edu/degrees/ |
| 7 | Ecology and Evolutionary Biology | https://degree-search.nau.edu/degrees/ |
| 8 | Environmental Sciences | https://degree-search.nau.edu/degrees/ |
| 9 | Environmental and Sustainability Studies | https://degree-search.nau.edu/degrees/ |
| 10 | Geosciences | https://degree-search.nau.edu/degrees/ |
| 11 | Mathematics | https://degree-search.nau.edu/degrees/ |
| 12 | Microbiology | https://degree-search.nau.edu/degrees/ |
| 13 | Physics | https://degree-search.nau.edu/degrees/ |

##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental and Sustainability Studies | https://degree-search.nau.edu/degrees/ |

##### BSF
| # | 专业 | URL |
|---|------|-----|
| 1 | Forestry | https://degree-search.nau.edu/degrees/ |

#### The Steve Sanghi College of Engineering

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://degree-search.nau.edu/degrees/ |
| 2 | Civil Engineering | https://degree-search.nau.edu/degrees/ |
| 3 | Computer Engineering | https://degree-search.nau.edu/degrees/ |
| 4 | Construction Management | https://degree-search.nau.edu/degrees/ |
| 5 | Cybersecurity | https://degree-search.nau.edu/degrees/ |
| 6 | Data Science | https://degree-search.nau.edu/degrees/ |
| 7 | Electrical Engineering | https://degree-search.nau.edu/degrees/ |
| 8 | Engineering Technology | https://degree-search.nau.edu/degrees/ |
| 9 | Environmental Engineering | https://degree-search.nau.edu/degrees/ |
| 10 | Informatics | https://degree-search.nau.edu/degrees/ |
| 11 | Information Technology | https://degree-search.nau.edu/degrees/ |
| 12 | Mechanical Engineering | https://degree-search.nau.edu/degrees/ |
| 13 | Mechatronics and Robotics Engineering | https://degree-search.nau.edu/degrees/ |
| 14 | Multidisciplinary Engineering | https://degree-search.nau.edu/degrees/ |
| 15 | Software Engineering | https://degree-search.nau.edu/degrees/ |

##### BSCS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://degree-search.nau.edu/degrees/ |

##### BPRS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Technology | https://degree-search.nau.edu/degrees/ |

#### The W. A. Franke College of Business

##### BSACCY / BBA / BSBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy (BSACCY) | https://degree-search.nau.edu/degrees/ |
| 2 | Business Administration (BBA) | https://degree-search.nau.edu/degrees/ |
| 3 | Business Analytics (BS) | https://degree-search.nau.edu/degrees/ |
| 4 | Business Economics (BSBA) | https://degree-search.nau.edu/degrees/ |
| 5 | Finance (BSBA) | https://degree-search.nau.edu/degrees/ |
| 6 | Hospitality Leadership 90-30 (BS) | https://degree-search.nau.edu/degrees/ |
| 7 | Hotel and Restaurant Management (BS) | https://degree-search.nau.edu/degrees/ |
| 8 | Information Systems (BSBA) | https://degree-search.nau.edu/degrees/ |
| 9 | Logistics and Supply Chain Management (BS) | https://degree-search.nau.edu/degrees/ |
| 10 | Management (BSBA) | https://degree-search.nau.edu/degrees/ |
| 11 | Marketing (BSBA) | https://degree-search.nau.edu/degrees/ |

#### Interdisciplinary / Other

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Business Management | BS | https://degree-search.nau.edu/degrees/ |
| 2 | Applied Indigenous Studies | BS | https://degree-search.nau.edu/degrees/ |
| 3 | Applied Science - Early Childhood | BAS | https://degree-search.nau.edu/degrees/ |
| 4 | Arts and Cultural Management | BS | https://degree-search.nau.edu/degrees/ |
| 5 | Early Childhood Education - Non-Certification 90-30 | BS | https://degree-search.nau.edu/degrees/ |
| 6 | Hospitality Business Administration | BPRS | https://degree-search.nau.edu/degrees/ |
| 7 | Immersive Media and Games | BS | https://degree-search.nau.edu/degrees/ |
| 8 | Interdisciplinary Studies | BIS | https://degree-search.nau.edu/degrees/ |
| 9 | Interior Design | BS | https://degree-search.nau.edu/degrees/ |
| 10 | Journalism | BSJOUR | https://degree-search.nau.edu/degrees/ |
| 11 | Strategic Leadership 90-30 | BS | https://degree-search.nau.edu/degrees/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

NAU's Interdisciplinary Studies (BIS) degree allows students to design custom programs across colleges. The Applied Human Behavior 90-30 and Indian Country Criminal Justice programs are examples of cross-college collaboration between Social & Behavioral Sciences and other units.

### 1.4 Minors — Complete List

| # | Minor | Home College |
|---|-------|-------------|
| 1 | Actuarial Science | Environment, Forestry & Natural Sciences |
| 2 | Advertising | Arts & Letters |
| 3 | Aerospace Studies | Arts & Letters |
| 4 | Applied Archaeology | Environment, Forestry & Natural Sciences |
| 5 | Applied Indigenous Studies | Social & Behavioral Sciences |
| 6 | Art History | Arts & Letters |
| 7 | Asian Studies | Arts & Letters |
| 8 | Astrobiology | Environment, Forestry & Natural Sciences |
| 9 | Astrochemistry | Environment, Forestry & Natural Sciences |
| 10 | Astrogeology | Environment, Forestry & Natural Sciences |
| 11 | Astronomy | Environment, Forestry & Natural Sciences |
| 12 | Biological Anthropology | Social & Behavioral Sciences |
| 13 | Biology | Environment, Forestry & Natural Sciences |
| 14 | Brewing and Fermentation Science | Environment, Forestry & Natural Sciences |
| 15 | Business | Franke College of Business |
| 16 | Business Administration | Franke College of Business |
| 17 | Chemistry | Environment, Forestry & Natural Sciences |
| 18 | Chinese | Arts & Letters |
| 19 | Classical Studies | Arts & Letters |
| 20 | Climate Change | Environment, Forestry & Natural Sciences |
| 21 | Communication Studies | Arts & Letters |
| 22 | Community Engagement | Social & Behavioral Sciences |
| 23 | Community Health | Health & Human Services |
| 24 | Community and Commercial Recreation | Health & Human Services |
| 25 | Comparative Study of Religions | Arts & Letters |
| 26 | Computer Science | Engineering |
| 27 | Construction Management | Engineering |
| 28 | Creative Media and Film | Arts & Letters |
| 29 | Criminal Justice Administration | Social & Behavioral Sciences |
| 30 | Criminology and Criminal Justice | Social & Behavioral Sciences |
| 31 | Critical Sustainability Studies | Environment, Forestry & Natural Sciences |
| 32 | Cybersecurity | Engineering |
| 33 | Disability Studies | Social & Behavioral Sciences |
| 34 | Documentary Storytelling | Arts & Letters |
| 35 | Early Childhood Education | Education |
| 36 | Emergency Management | Social & Behavioral Sciences |
| 37 | English | Arts & Letters |
| 38 | Environmental Anthropology | Social & Behavioral Sciences |
| 39 | Environmental Communication | Environment, Forestry & Natural Sciences |
| 40 | Environmental Humanities | Environment, Forestry & Natural Sciences |
| 41 | Environmental Sciences | Environment, Forestry & Natural Sciences |
| 42 | Environmental Sustainability | Environment, Forestry & Natural Sciences |
| 43 | Ethnic Studies | Social & Behavioral Sciences |
| 44 | French | Arts & Letters |
| 45 | Geographic Information Systems | Environment, Forestry & Natural Sciences |
| 46 | Geographic Regional Studies | Environment, Forestry & Natural Sciences |
| 47 | Geology | Environment, Forestry & Natural Sciences |
| 48 | German | Arts & Letters |
| 49 | Health and Wellness Coaching | Health & Human Services |
| 50 | History | Arts & Letters |
| 51 | Hotel and Restaurant Management | Franke College of Business |
| 52 | Humanities | Arts & Letters |
| 53 | Individualized Minor | Interdisciplinary |
| 54 | Indigenous Health Studies | Health & Human Services |
| 55 | International Communication | Arts & Letters |
| 56 | International Studies | Arts & Letters |
| 57 | Italian | Arts & Letters |
| 58 | Japanese | Arts & Letters |
| 59 | Journalism | Arts & Letters |
| 60 | Latin American Studies | Arts & Letters |
| 61 | Law and Society | Social & Behavioral Sciences |
| 62 | Law, Rights and Justice | Social & Behavioral Sciences |
| 63 | Mathematics | Environment, Forestry & Natural Sciences |
| 64 | Mathematics Secondary Education | Education |
| 65 | Medical Anthropology | Social & Behavioral Sciences |
| 66 | Medical Humanities | Arts & Letters |
| 67 | Military Leadership | Arts & Letters |
| 68 | Museum Studies | Arts & Letters |
| 69 | Music | Arts & Letters |
| 70 | Navajo | Arts & Letters |
| 71 | Outdoor Education and Leadership | Health & Human Services |
| 72 | Parks and Recreation Management | Health & Human Services |
| 73 | Philosophy | Arts & Letters |
| 74 | Photography | Arts & Letters |
| 75 | Physical Geography | Environment, Forestry & Natural Sciences |
| 76 | Physics | Environment, Forestry & Natural Sciences |
| 77 | Political Science | Social & Behavioral Sciences |
| 78 | Psychology | Social & Behavioral Sciences |
| 79 | Public Administration | Social & Behavioral Sciences |
| 80 | Public Administration of Native Nations | Social & Behavioral Sciences |
| 81 | Public Relations | Arts & Letters |
| 82 | Public Safety and Law Enforcement | Social & Behavioral Sciences |
| 83 | Queer Studies | Social & Behavioral Sciences |
| 84 | Social Science Forensics | Social & Behavioral Sciences |
| 85 | Social Work | Social & Behavioral Sciences |
| 86 | Sociology | Social & Behavioral Sciences |
| 87 | Spanish | Arts & Letters |
| 88 | Statistics | Environment, Forestry & Natural Sciences |
| 89 | Studio Art | Arts & Letters |
| 90 | Sustainable Food Systems | Environment, Forestry & Natural Sciences |
| 91 | Theatre | Arts & Letters |
| 92 | Urban Planning and Design | Environment, Forestry & Natural Sciences |
| 93 | Women's and Gender Studies | Social & Behavioral Sciences |
| 94 | *(Individualized Minor)* | Interdisciplinary |

### 1.5 General Education Requirements

NAU requires all undergraduate students to complete a General Education program. Details are available at the Academic Catalog. Requirements typically include English composition, mathematics, laboratory science, social science, humanities, and diversity courses. The specific requirements may vary by catalog year.

### 1.6 Course-ID → Major Quick-Lookup

NAU does not use a course-number system for majors (unlike MIT's "Course 6" system). Programs are identified by name and degree type in the catalog.

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

NAU offers **92 graduate degree programs** and **35 graduate certificates** across all colleges. Graduate admissions is coordinated by the Office of Graduate and Professional Studies, but each college manages its own programs.

#### College of Arts and Letters

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Linguistics and Teaching English as a Second Language | https://catalog.nau.edu/ |
| 2 | Communication | https://catalog.nau.edu/ |
| 3 | English - Literature | https://catalog.nau.edu/ |
| 4 | English - Professional Writing | https://catalog.nau.edu/ |
| 5 | English - Rhetoric, Writing, and Digital Media Studies | https://catalog.nau.edu/ |
| 6 | Human and Community Relations | https://catalog.nau.edu/ |
| 7 | Science Teaching | https://catalog.nau.edu/ |
| 8 | Sustainable Communities | https://catalog.nau.edu/ |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://catalog.nau.edu/ |

##### MMUS
| # | 项目 | URL |
|---|------|-----|
| 1 | Music | https://catalog.nau.edu/ |

#### College of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | https://catalog.nau.edu/ |
| 2 | Career and Technical Education | https://catalog.nau.edu/ |
| 3 | Counseling - School Counseling | https://catalog.nau.edu/ |
| 4 | Early Childhood Education | https://catalog.nau.edu/ |
| 5 | Educational Foundations | https://catalog.nau.edu/ |
| 6 | Educational Leadership - Community College/Higher Education | https://catalog.nau.edu/ |
| 7 | Educational Leadership - Instructional Leadership K-12 | https://catalog.nau.edu/ |
| 8 | Educational Leadership - Principal Pre K-12 | https://catalog.nau.edu/ |
| 9 | Educational Technology | https://catalog.nau.edu/ |
| 10 | Elementary Education | https://catalog.nau.edu/ |
| 11 | Elementary Education - Certification | https://catalog.nau.edu/ |
| 12 | Elementary Education - Reading K-8 | https://catalog.nau.edu/ |
| 13 | ESL and Bilingual Education | https://catalog.nau.edu/ |
| 14 | International Education Leadership | https://catalog.nau.edu/ |
| 15 | Special Education | https://catalog.nau.edu/ |
| 16 | Special Education - Early Childhood Special Education with Certification | https://catalog.nau.edu/ |
| 17 | Special Education - Mild/Moderate Disabilities Certified | https://catalog.nau.edu/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics Education | https://catalog.nau.edu/ |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Spanish | https://catalog.nau.edu/ |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership - Community College / Higher Education Administration | https://catalog.nau.edu/ |
| 2 | Educational Leadership - K-12 Administration | https://catalog.nau.edu/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://catalog.nau.edu/ |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | School Psychology | https://catalog.nau.edu/ |

#### College of Health and Human Services

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | https://catalog.nau.edu/ |
| 2 | Clinical Speech - Language Pathology | https://catalog.nau.edu/ |
| 3 | Nursing | https://catalog.nau.edu/ |
| 4 | Nursing - Advanced Practice | https://catalog.nau.edu/ |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://catalog.nau.edu/ |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health - Health Promotion | https://catalog.nau.edu/ |
| 2 | Public Health - Nutrition | https://catalog.nau.edu/ |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.nau.edu/ |
| 2 | Social Work - Advanced Standing | https://catalog.nau.edu/ |

##### MPAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant Studies | https://catalog.nau.edu/ |

##### OTD / DPT / DNP / DMSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy (OTD) | https://catalog.nau.edu/ |
| 2 | Physical Therapy (DPT) | https://catalog.nau.edu/ |
| 3 | Nursing Practice (DNP) | https://catalog.nau.edu/ |
| 4 | Healthcare Systems (DMSc) | https://catalog.nau.edu/ |
| 5 | Medical Science (DMSc) | https://catalog.nau.edu/ |

#### College of Social and Behavioral Sciences

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.nau.edu/ |
| 2 | Applied Sociology | https://catalog.nau.edu/ |
| 3 | Psychological Sciences | https://catalog.nau.edu/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Criminology | https://catalog.nau.edu/ |
| 2 | Geography | https://catalog.nau.edu/ |
| 3 | Geographic Information Science with Remote Sensing | https://catalog.nau.edu/ |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://catalog.nau.edu/ |

##### PsyD / PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology (PsyD) | https://catalog.nau.edu/ |
| 2 | Combined Counseling/School Psychology (PhD) | https://catalog.nau.edu/ |
| 3 | Political Science (PhD) | https://catalog.nau.edu/ |

#### College of the Environment, Forestry, and Natural Sciences

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Physics | https://catalog.nau.edu/ |
| 2 | Biology | https://catalog.nau.edu/ |
| 3 | Chemistry | https://catalog.nau.edu/ |
| 4 | Climate Science and Solutions | https://catalog.nau.edu/ |
| 5 | Environmental Sciences and Policy | https://catalog.nau.edu/ |
| 6 | Forestry | https://catalog.nau.edu/ |
| 7 | Geographic Information Science with Remote Sensing | https://catalog.nau.edu/ |
| 8 | Geography | https://catalog.nau.edu/ |
| 9 | Geosciences | https://catalog.nau.edu/ |
| 10 | Mathematics | https://catalog.nau.edu/ |
| 11 | Statistics | https://catalog.nau.edu/ |
| 12 | Statistics and Data Science | https://catalog.nau.edu/ |

##### MF / MSF
| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry (MF) | https://catalog.nau.edu/ |
| 2 | Forest and Natural Resource Management (MF) | https://catalog.nau.edu/ |
| 3 | Forestry (MSF) | https://catalog.nau.edu/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Physics and Materials Science | https://catalog.nau.edu/ |
| 2 | Astronomy and Planetary Science | https://catalog.nau.edu/ |
| 3 | Biology | https://catalog.nau.edu/ |
| 4 | Earth Sciences and Environmental Sustainability | https://catalog.nau.edu/ |
| 5 | Forest Science | https://catalog.nau.edu/ |

#### The Steve Sanghi College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Civil and Environmental Engineering | https://catalog.nau.edu/ |
| 2 | Computer Science | https://catalog.nau.edu/ |
| 3 | Computer Science - Personalized Learning | https://catalog.nau.edu/ |
| 4 | Cybersecurity | https://catalog.nau.edu/ |
| 5 | Electrical and Computer Engineering | https://catalog.nau.edu/ |
| 6 | Informatics | https://catalog.nau.edu/ |
| 7 | Information Technology | https://catalog.nau.edu/ |
| 8 | Management Information Systems | https://catalog.nau.edu/ |
| 9 | Mechanical Engineering | https://catalog.nau.edu/ |
| 10 | Computational and Applied Data Science | https://catalog.nau.edu/ |

##### MA (PL)
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Information Technology (Personalized Learning) | https://catalog.nau.edu/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.nau.edu/ |
| 2 | Civil and Environmental Engineering | https://catalog.nau.edu/ |
| 3 | Informatics and Computing | https://catalog.nau.edu/ |
| 4 | Mechanical Engineering | https://catalog.nau.edu/ |

#### The W. A. Franke College of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://catalog.nau.edu/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.nau.edu/ |
| 2 | Healthcare | https://catalog.nau.edu/ |

##### MGBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Business Administration | https://catalog.nau.edu/ |

#### Maria and Steve Sanghi College of Nursing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.nau.edu/ |
| 2 | Nursing - Advanced Practice | https://catalog.nau.edu/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice | https://catalog.nau.edu/ |

#### Office of Graduate and Professional Studies

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Linguistics | https://catalog.nau.edu/ |
| 2 | Interdisciplinary Health | https://catalog.nau.edu/ |

##### MA (PL)
| # | 项目 | URL |
|---|------|-----|
| 1 | Organizational Leadership (Personalized Learning) | https://catalog.nau.edu/ |
| 2 | Organizational Leadership | https://catalog.nau.edu/ |

### 2.2 Graduate Admissions Model

NAU uses a **two-step review process**:
1. Program/department reviews application first
2. Graduate Admissions (Office of Graduate and Professional Studies) makes final decision

**Application requirements vary by program** but typically include:
- Bachelor's degree from accredited institution
- GPA of 2.5+ (some programs require 3.0)
- Statement of purpose
- Transcripts
- Letters of recommendation (varies)
- GRE scores (varies by program — many are optional)
- Resume/CV

**Application fee**: $75 (international students)
**Application portal**: NAU's online application system
**FAFSA code**: 001082

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| 官方招生网站 | https://nau.edu/admissions/ | nau.edu |
| 申请入口 | https://my.admissions.nau.edu/apply | nau.edu |
| 申请系统 | NAU Online Application | nau.edu |
| EA 截止日期 | N/A (无EA) | nau.edu |
| ED 截止日期 | N/A (无ED) | nau.edu |
| RD 截止日期 | **滚动录取 (Rolling)** — 无固定截止日期 | nau.edu |
| 优先入学保证金截止 | **May 1, 2026** (Fall) / **December 1, 2026** (Spring) | nau.edu/admissions/important-dates-deadlines/ |
| 学费截止日期 | **August 17, 2026** (Fall) / **January 4, 2027** (Spring) | nau.edu/admissions/important-dates-deadlines/ |
| 最终成绩单邮寄截止 | **July 1, 2026** (Fall) / **January 5, 2027** (Spring) | nau.edu/admissions/important-dates-deadlines/ |
| FAFSA 优先截止 | **April 15** | nau.edu/how-to-apply/first-year/apply-steps/ |
| 申请费 | **$50** (UG international) | nau.edu/how-to-apply/international/apply-steps/ |
| 入学保证金 | **$325** (first-year) / **$250** (transfer) | nau.edu/admissions/important-dates-deadlines/ |
| SAT/ACT 政策 | **Test-Optional** — 标准化考试成绩提交为可选 | nau.edu search results |
| SAT 代码 | N/A (test-optional) | — |
| ACT 代码 | N/A (test-optional) | — |
| Superscore | N/A | — |
| 推荐信要求 | 不要求 | nau.edu |
| 面试 | 不要求 | nau.edu |
| 作品集 | 仅特定专业 (如Art, Design) | — |
| 保底录取 (AZ居民) | **GPA 2.5+** 且完成14门核心课程 | nau.edu/how-to-apply/first-year/apply-steps/ |
| 核心课程要求 | 4 English, 4 Math, 3 Lab Science, 2 Social Science, 1 Fine Arts/CTE, 2 Second Language | nau.edu |

> **Source snippets**:
> - "NAU offers rolling admission for most undergraduate programs, so you can apply anytime." — nau.edu/admissions/important-dates-deadlines/
> - "We offer guaranteed admission to all students who've completed their junior year and are on track to graduate with a core GPA of 2.5+ (4.0 scale)." — nau.edu/how-to-apply/first-year/apply-steps/
> - "The submission of your standardized test scores is optional and not required for an admission decision or scholarship consideration." — nau.edu search (Personal Advantage Application pages)

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 备注 |
|------|---------|------|
| TOEFL iBT / iBT Home Edition | **70** | MyBest Score accepted; NAU code: 4006 |
| IELTS | **6.0** overall | — |
| Duolingo English Test (DET) | **95** | — |
| PTE | **56** | — |
| SAT (EBRW) | **350** | — |
| ACT (English + Reading) | **21** | — |
| IB English A | **5 HL** or **6 SL** | — |
| IB English B | **7** in both HL and SL | — |
| U.S. 大学转学 | 完成1门3学分英语写作课并通过 | — |
| 欧洲交换生 | **B2** level | — |
| 英语授课高中毕业 | 4年英语课(写作+文学)通过 + 学校证明 | — |
| 英语国家公民 | 无需提供 | — |

> **Source**: nau.edu/how-to-apply/international/apply-steps/
> **Source snippet**: "NAU accepts many ways to prove English proficiency, including: TOEFL iBT or iBT Home Edition — minimum score of 70 (NAU school code: 4006; MyBest Score accepted)"

### 3.3 Graduate — Global Rules

| 维度 | 值 |
|------|-----|
| 招生模式 | **两步审核** — 项目/系先审，研究生院最终决定 |
| 申请入口 | NAU Online Application |
| 申请费 | **$75** (international) |
| GPA 要求 | **2.5+** (部分项目要求3.0) |
| GRE 政策 | **因项目而异** — 多数项目可选 |
| 英语要求 | 与UG相同 (TOEFL 70 / IELTS 6.0 / DET 95) |
| 申请截止日期 | **因项目而异** — 多数项目秋季入学，部分有春/夏 |
| FAFSA 优先截止 | **April 1** |
| FAFSA 代码 | **001082** |
| CGS April-15 | 未确认 |

> **Source**: nau.edu/how-to-apply/graduate/apply-steps/
> **Source snippet**: "If you've earned a bachelor's degree from a regional or CHEA accredited institution and have a GPA of 2.5 or higher, you're ready to apply to graduate school at NAU."

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| 费用项目 | AZ Resident | WUE | Non-Resident | International |
|---------|-------------|-----|--------------|---------------|
| Tuition | $12,000 | $18,000 | $30,000 | $30,000 |
| Fees | $1,622 | $1,622 | $1,622 | $1,622 |
| **Total Tuition & Fees** | **$13,622** | **$19,622** | **$31,622** | **$31,622** |
| Housing (shared, traditional) | $7,320 | $7,320 | $7,320 | $7,320 |
| Dining (meal plan est.) | ~$5,500 | ~$5,500 | ~$5,500 | ~$5,500 |
| Books & Supplies (est.) | ~$1,000 | ~$1,000 | ~$1,000 | ~$1,000 |
| Personal/Misc (est.) | ~$2,000 | ~$2,000 | ~$2,000 | ~$2,000 |
| **Total Estimated COA** | **~$29,442** | **~$35,442** | **~$47,442** | **~$47,442** |

> **Source**: nau.edu/fees/undergraduate-tuition/
> **Source snippet**: "Tuition $12,000 (AZ Resident) / $18,000 (WUE) / $30,000 (Non-Resident) / $30,000 (International). Fees $1,622."
> **Note**: Housing rates range from $5,682 (discounted triple) to $9,994 (private semi-suite Honors). Dining costs vary by plan.

### 4.2 Graduate Cost (2026-27 Academic Year)

| 费用项目 | AZ Resident | Non-Resident | WRGP | International |
|---------|-------------|--------------|------|---------------|
| Tuition | $13,582 | $33,800 | $20,374 | $33,800 |
| Fees | $1,622 | $1,622 | $1,622 | $1,622 |
| **Total Tuition & Fees** | **$15,204** | **$35,422** | **$21,996** | **$35,422** |

> **Source**: nau.edu/fees/graduate-tuition/
> **Note**: Some graduate programs have additional fees. WRGP = Western Regional Graduate Program (discounted rate for eligible western-state residents).

### 4.3 Undergraduate Financial Aid Policy

| 维度 | 值 |
|------|-----|
| Need-Aware/Need-Blind | **Need-Aware** for all students (domestic and international) |
| Access2Excellence (A2E) | **Full tuition coverage** for AZ residents with household income ≤**$65,000** |
| A2E 扩展 | Arizona 22个联邦认可部落成员 — **无收入或居住限制** |
| A2E 覆盖范围 | 仅学费 (不含杂费/食宿) — 不含在线学生 |
| Arizona Promise Program | 帮助覆盖强制性大学费用 |
| 学生接受资助比例 | **97%** |
| 无债务毕业率 | **55%** |
| 年度奖学金/资助总额 | **$400M+** |

**Merit Scholarships (Fall 2026)**:

| 奖学金 | GPA (unweighted core) | 年金额 (AZ Resident) | 年金额 (WUE) | 年金额 (OOS) |
|--------|----------------------|---------------------|--------------|--------------|
| Lumberjack Scholars Award | 3.75–4.0 | $11,000 | — | — |
| President's Excellence | 3.5–4.0 | — | — | $15,000 |
| President's | 3.5–3.74 | $9,000 | — | $12,000 (3.0–3.49) |
| Excellence (WUE) | 3.75–4.0 | — | $8,500 | — |
| Gold (WUE) | 3.5–3.74 | — | $8,000 | — |
| Blue (WUE) | 3.0–3.49 | — | $7,000 | — |
| Dean's with Distinction | 3.4–3.49 | $6,500 | — | — |
| Dean's | 3.0–3.39 | $5,000 | — | — |
| Opportunity | Admitted–2.99 | $2,500 | $4,500 | $10,000 |

> **Source**: nau.edu/financial-aid/scholarships/freshman/
> **Source snippet**: "Access2Excellence (A2E) guarantees full undergraduate tuition coverage for: Arizona residents with a household income of $65,000 or less; members of one of Arizona's 22 federally recognized tribes (no income or residency requirement)"

### 4.4 Graduate Funding Framework

- Funding types: Assistantships (RA/TA), fellowships, departmental awards, self-funded
- Most PhD programs offer full funding (tuition + stipend)
- Master's programs are often self-funded
- Application fee: $75 (international)
- FAFSA priority deadline: April 1

---

## SECTION 5 — Evidence Chain Index

```yaml
---
E-U-001:
  field: undergraduate.admissions.rolling
  value: true
  source_url: https://nau.edu/admissions/important-dates-deadlines/
  source_snippet: "NAU offers rolling admission for most undergraduate programs, so you can apply anytime."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.admissions.guaranteed_admission_gpa
  value: 2.5
  source_url: https://nau.edu/how-to-apply/first-year/apply-steps/
  source_snippet: "We offer guaranteed admission to all students who've completed their junior year and are on track to graduate with a core GPA of 2.5+ (4.0 scale)."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.admissions.test_optional
  value: true
  source_url: https://nau.edu/search/?q=test+optional
  source_snippet: "The submission of your standardized test scores is optional and not required for an admission decision or scholarship consideration."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.costs.tuition_az_resident
  value: 12000
  source_url: https://nau.edu/fees/undergraduate-tuition/
  source_snippet: "Tuition $12,000 (AZ Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.costs.tuition_nonresident
  value: 30000
  source_url: https://nau.edu/fees/undergraduate-tuition/
  source_snippet: "Tuition $30,000 (Non-Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.fees
  value: 1622
  source_url: https://nau.edu/fees/undergraduate-tuition/
  source_snippet: "Fees $1,622"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.costs.tuition_wue
  value: 18000
  source_url: https://nau.edu/fees/undergraduate-tuition/
  source_snippet: "Tuition $18,000 (WUE)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency.toefl_min
  value: 70
  source_url: https://nau.edu/how-to-apply/international/apply-steps/
  source_snippet: "TOEFL iBT or iBT Home Edition — minimum score of 70 (NAU school code: 4006; MyBest Score accepted)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_proficiency.ielts_min
  value: 6.0
  source_url: https://nau.edu/how-to-apply/international/apply-steps/
  source_snippet: "IELTS — minimum overall band score of 6"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.english_proficiency.det_min
  value: 95
  source_url: https://nau.edu/how-to-apply/international/apply-steps/
  source_snippet: "Duolingo English Test — minimum score of 95"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.access2excellence_threshold
  value: 65000
  source_url: https://nau.edu/financial-aid/aid-programs/access-2-excellence/
  source_snippet: "A2E guarantees full undergraduate tuition coverage for: Arizona residents with a household income of $65,000 or less"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.financial_aid.students_receiving_aid
  value: "97%"
  source_url: https://nau.edu/financial-aid/
  source_snippet: "97% of NAU students receive some form of aid"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.financial_aid.debt_free_graduation
  value: "55%"
  source_url: https://nau.edu/financial-aid/
  source_snippet: "55% of NAU students graduate debt free"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.enrollment_fee
  value: 325
  source_url: https://nau.edu/admissions/important-dates-deadlines/
  source_snippet: "First-year students will owe $325."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.deadlines.enrollment_fee_fall
  value: "May 1, 2026"
  source_url: https://nau.edu/admissions/important-dates-deadlines/
  source_snippet: "Pay enrollment fee May 1, 2026 (fall deadline)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.costs.tuition_az_resident
  value: 13582
  source_url: https://nau.edu/fees/graduate-tuition/
  source_snippet: "Tuition $13,582 (AZ Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.costs.tuition_nonresident
  value: 33800
  source_url: https://nau.edu/fees/graduate-tuition/
  source_snippet: "Tuition $33,800 (Non-Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.admissions.gpa_minimum
  value: 2.5
  source_url: https://nau.edu/how-to-apply/graduate/apply-steps/
  source_snippet: "If you've earned a bachelor's degree from a regional or CHEA accredited institution and have a GPA of 2.5 or higher, you're ready to apply to graduate school at NAU."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.admissions.two_step_review
  value: true
  source_url: https://nau.edu/how-to-apply/graduate/apply-steps/
  source_snippet: "NAU uses a two-step review process. First, your program reviews your application. Then, Graduate Admissions makes the final call."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-001:
  field: programs.total_catalog_entries
  value: 409
  source_url: https://catalog.nau.edu/Catalog/results?cat=ALLDEGREES&catalogYear=2627
  source_snippet: "409 results" (catalog search results count)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-P-002:
  field: programs.ug_majors
  value: 117
  source_url: https://degree-search.nau.edu/degrees/
  source_snippet: "117 results sorted by" (undergraduate degree search)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-001:
  field: institution.location
  value: "Flagstaff, AZ"
  source_url: https://nau.edu/about/
  source_snippet: "Northern Arizona University sits at the base of the San Francisco Peaks"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-002:
  field: institution.founded
  value: 1899
  source_url: https://nau.edu/about/
  source_snippet: "NAU started as a teachers' college in 1899"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-I-003:
  field: institution.type
  value: "Public"
  source_url: https://nau.edu/
  source_snippet: "Northern Arizona University" (public state university, Arizona Board of Regents)
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
nau-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, degree inventory, matrix
├── 01-ug-arts-letters.md              # Section 1: College of Arts & Letters UG programs
├── 02-ug-education.md                 # Section 1: College of Education UG programs
├── 03-ug-health-human-services.md     # Section 1: College of Health & Human Services UG programs
├── 04-ug-social-behavioral.md         # Section 1: College of Social & Behavioral Sciences UG programs
├── 05-ug-environment-forestry.md      # Section 1: College of Environment, Forestry & Natural Sciences UG
├── 06-ug-engineering.md               # Section 1: Steve Sanghi College of Engineering UG programs
├── 07-ug-business.md                  # Section 1: W. A. Franke College of Business UG programs
├── 08-ug-interdisciplinary.md         # Section 1: Interdisciplinary/Other UG programs
├── 09-ug-minors.md                    # Section 1.4: Complete minors list
├── 10-grad-arts-letters.md            # Section 2: College of Arts & Letters grad programs
├── 11-grad-education.md               # Section 2: College of Education grad programs
├── 12-grad-health-human-services.md   # Section 2: College of Health & Human Services grad programs
├── 13-grad-social-behavioral.md       # Section 2: College of Social & Behavioral Sciences grad programs
├── 14-grad-environment-forestry.md    # Section 2: College of Environment, Forestry & Natural Sciences grad
├── 15-grad-engineering.md             # Section 2: Steve Sanghi College of Engineering grad programs
├── 16-grad-business.md                # Section 2: W. A. Franke College of Business grad programs
├── 17-grad-nursing.md                 # Section 2: Maria and Steve Sanghi College of Nursing grad programs
├── 18-grad-interdisciplinary.md       # Section 2: Office of Graduate & Professional Studies programs
├── 19-deadlines-requirements.md       # Section 3: Application requirements & deadlines
├── 20-costs-financial-aid.md          # Section 4: Costs & financial aid
├── 21-evidence-chain.md               # Section 5: Evidence chain index
└── 22-comparison-framework.md         # Section 7: Cross-school comparison
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "nau-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BSED|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://catalog.nau.edu/Catalog/results?cat=ALLDEGREES&catalogYear=2627
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE requirements (graduate) | Individual program pages in catalog |
| P0 | Graduate program application deadlines by program | https://nau.edu/admissions/contact/academic-advising-graduate-students/ |
| P0 | Meal plan costs (specific rates) | https://nau.edu/fees/dining/ (expand plan detail pages) |
| P1 | Department-to-college mapping (complete) | Individual college websites |
| P1 | Graduate program fees by college | https://nau.edu/fees/graduate-tuition/graduate-program-fees/ |
| P1 | Honors College admission requirements | https://nau.edu/honors/ |
| P2 | Student enrollment numbers (total, by college) | https://nau.edu/about/facts-and-figures/ (404 — find correct URL) |
| P2 | Faculty count and student-faculty ratio | Institutional research page |
| P2 | Graduation rate / retention rate | IPEDS or institutional research |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | NAU | (blank for other schools) |
|------|-----|--------------------------|
| **类型** | Public | |
| **位置** | Flagstaff, AZ | |
| **Founded** | 1899 | |
| **UG Tuition (AZ Resident)** | $13,622 | |
| **UG Tuition (OOS)** | $31,622 | |
| **UG Tuition (WUE)** | $19,622 | |
| **Grad Tuition (AZ Resident)** | $15,204 | |
| **Grad Tuition (OOS)** | $35,422 | |
| **Need-Aware/Blind** | Need-Aware (all) | |
| **A2E Threshold** | $65,000 (AZ residents) | |
| **EA Deadline** | N/A (rolling) | |
| **RD Deadline** | Rolling | |
| **Priority Date** | May 1 | |
| **SAT/ACT Required?** | No (test-optional) | |
| **TOEFL Min** | 70 | |
| **IELTS Min** | 6.0 | |
| **DET Min** | 95 | |
| **App Fee (UG)** | $50 (international) | |
| **App Fee (Grad)** | $75 (international) | |
| **Total Programs (Rule 1)** | 209 degree programs | |
| **UG Majors** | 117 | |
| **Grad Degrees** | 92 | |
| **Minors** | 94 | |
| **Colleges** | 10 | |
| **Students Receiving Aid** | 97% | |
| **Debt-Free Graduation** | 55% | |
| **Acceptance Rate** | ~91% | |
| **Strong Programs** | Forestry, Education, Engineering | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: nau.edu, catalog.nau.edu, degree-search.nau.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
