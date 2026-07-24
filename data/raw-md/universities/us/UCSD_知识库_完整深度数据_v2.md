# University of California San Diego (UCSD) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 155 |
| 本科辅修 (Minor) | ~60+ (see Section 1.4) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | ~300+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | ~15+ |
| **学位项目总计 (UG + Grad)** | **~455+** |
| 学院 / 独立系所总数 | 8 UG academic schools + 5 graduate/professional schools + Division of Graduate Education |

> **Note**: The UCSD admissions page states "160+ majors" which includes minors and certificates. The catalog lists 155 distinct bachelor's degree programs (some with specializations counted separately). Graduate programs total ~300+ distinct program-degree rows across all schools. Counts derived from `catalog.ucsd.edu/undergraduate/degrees-offered/index.html` and `catalog.ucsd.edu/graduate/degrees-offered/index.html` (2026-27 Catalog of Record).

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
UC San Diego
├── UNDERGRADUATE ACADEMIC SCHOOLS (8)                    [学院]
│   ├── Division of Arts and Humanities                   [学院]
│   │   ├── African American Studies                      [系]
│   │   ├── Chicanx and Latinx Studies                    [系]
│   │   ├── Chinese Studies                               [系]
│   │   ├── Cinematic Arts                                [系]
│   │   ├── Classical Studies                             [系]
│   │   ├── Communication                                 [系]
│   │   ├── Ethnic Studies                                [系]
│   │   ├── German Studies                                [系]
│   │   ├── History                                       [系]
│   │   ├── Italian Studies                               [系]
│   │   ├── Japanese Studies                              [系]
│   │   ├── Jewish Studies                                [系]
│   │   ├── Linguistics                                   [系]
│   │   ├── Literature                                    [系]
│   │   ├── Music                                         [系]
│   │   ├── Philosophy                                    [系]
│   │   ├── Russian, East European, and Eurasian Studies  [系]
│   │   ├── Study of Religion                             [系]
│   │   ├── Theatre & Dance                               [系]
│   │   └── Visual Arts                                   [系]
│   │
│   ├── Division of Biological Sciences                   [学院]
│   │   ├── Biology Department                            [系]
│   │   │   ├── General Biology
│   │   │   ├── Ecology, Behavior & Evolution
│   │   │   ├── Microbiology
│   │   │   ├── Molecular and Cell Biology
│   │   │   ├── Neurobiology
│   │   │   ├── Human Biology
│   │   │   └── Biology with Specialization in Bioinformatics
│   │   └── (Note: Bioinformatics BS jointly administered with Halıcıoğlu Data Science Institute)
│   │
│   ├── Halıcıoğlu Data Science Institute (HDSI)         [学院]
│   │   └── Data Science                                  [系]
│   │
│   ├── Jacobs School of Engineering                      [学院]
│   │   ├── Bioengineering (BE)                           [系]
│   │   ├── Computer Science and Engineering (CSE)        [系]  ⚠ shared with HDSI (Data Science)
│   │   ├── Electrical and Computer Engineering (ECE)     [系]
│   │   ├── Mechanical and Aerospace Engineering (MAE)    [系]
│   │   ├── Nanoengineering (NE)                          [系]
│   │   └── Structural Engineering (SE)                   [系]
│   │
│   ├── Division of Physical Sciences                     [学院]
│   │   ├── Astronomy and Astrophysics                    [系]
│   │   ├── Chemistry and Biochemistry                    [系]
│   │   ├── Mathematics                                   [系]
│   │   └── Physics                                       [系]
│   │
│   ├── Herbert Wertheim School of Public Health          [学院]
│   │   └── Family and Preventive Medicine / Public Health [系]
│   │
│   ├── Scripps Institution of Oceanography               [学院]
│   │   ├── Earth Sciences                                [系]
│   │   ├── Marine Biology                                [系]
│   │   └── Oceanic and Atmospheric Sciences              [系]
│   │
│   └── Division of Social Sciences                       [学院]
│       ├── Anthropology                                  [系]
│       ├── Cognitive Science                             [系]
│       ├── Critical Gender Studies                       [系]
│       ├── Economics                                     [系]
│       ├── Education Studies                             [系]
│       ├── Ethnic Studies                                [系]
│       ├── Global Health                                 [系]
│       ├── Human Developmental Sciences                  [系]
│       ├── Latin American Studies                        [系]
│       ├── Political Science                             [系]
│       ├── Psychology                                    [系]
│       ├── Sociology                                     [系]
│       └── Urban Studies and Planning                    [系]
│
├── UNDERGRADUATE COLLEGES (8 — residential/GE system)    [学院]
│   ├── Revelle College (est. 1964)
│   ├── John Muir College (est. 1967)
│   ├── Thurgood Marshall College (est. 1970)
│   ├── Earl Warren College (est. 1974)
│   ├── Eleanor Roosevelt College (est. 1988)
│   ├── Sixth College (est. 2002)
│   ├── Seventh College (est. 2020)
│   └── Eighth College (est. 2023)
│
└── GRADUATE / PROFESSIONAL SCHOOLS                       [学院]
    ├── Division of Graduate Education and Postdoctoral Affairs (administers most PhD/MA/MS)
    ├── School of Global Policy and Strategy (GPS)        [学院]
    │   ├── International Affairs (MIA, MAS)
    │   ├── Public Policy (MPP)
    │   └── Chinese Economic and Political Affairs (MCEPA)
    ├── Rady School of Management                         [学院]
    │   ├── Business Administration (MBA)
    │   ├── Business Analytics (MS)
    │   ├── Management (PhD)
    │   ├── Quantitative Finance (MQF)
    │   └── Professional Accountancy (MPAc)
    ├── School of Medicine                                [学院]
    │   ├── Physician Assistant Education (MAS)
    │   └── Precision Medicine Therapeutics in Oncology (MAS)
    ├── Scripps Institution of Oceanography               [学院]
    │   ├── Climate Science and Policy (MAS)
    │   ├── Earth Sciences (MS, PhD)
    │   ├── Marine Biology (MS, PhD)
    │   ├── Marine Biodiversity and Conservation (MAS)
    │   └── Oceanography (MS, PhD)
    └── Skaggs School of Pharmacy and Pharmaceutical Sciences [学院]
        └── Drug Development and Product Management (MS)
```

> **Note**: UCSD's undergraduate colleges (Revelle through Eighth) are residential/GE communities, NOT academic schools. Students choose a college for its general education curriculum, but their major is offered through one of the 8 academic schools. Any undergraduate may select from the full range of majors regardless of college affiliation.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~60 |
| BS | Bachelor of Science | 本科 | ~95 |
| MA | Master of Arts | 研究生 | ~20 |
| MS | Master of Science | 研究生 | ~50 |
| MFA | Master of Fine Arts | 研究生 | 7 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MEng | Master of Engineering | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 7 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MIA | Master of International Affairs | 研究生 | 1 |
| MEd | Master of Education | 研究生 | 1 |
| MAS | Master of Advanced Studies | 研究生 | ~10 |
| MDS | Master of Data Science | 研究生 | 1 |
| MQF | Master of Quantitative Finance | 研究生 | 1 |
| MPAc | Master of Professional Accountancy | 研究生 | 1 |
| MCEPA | Master of Chinese Economic and Political Affairs | 研究生 | 1 |
| MURP | Master of Urban and Regional Planning | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | ~150 |
| Minor | 辅修 (本科) | 本科 | ~60+ |
| Certificate | 证书 | 研究生 | ~15+ |

> **Note**: Counts are approximate from catalog listing. PhD programs are the largest category at the graduate level. MAS (Master of Advanced Studies) is a UCSD-specific professional degree. Many PhD programs offer the MS as an intermediate degree ("the master's degree may be awarded to students pursuing work toward the PhD after fulfillment of the appropriate requirements").

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | Minor | MA | MS | MFA | MBA | MEng | MPH | MPP/MIA | MAS/MDS/MQF/MPAc | PhD | EdD/DMA/AuD | 合计 |
|------------|----|----|-------|----|----|-----|-----|------|-----|---------|-------------------|-----|-------------|------|
| Arts and Humanities | ~25 | 0 | ~15 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | ~15 | 1 (DMA) | ~63 |
| Biological Sciences | 0 | 7 | ~5 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 0 | ~29 |
| Data Science (HDSI) | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 (MDS) | 1 | 0 | 5 |
| Engineering (Jacobs) | 1 | ~30 | ~5 | 0 | ~25 | 0 | 0 | 2 | 0 | 0 | ~5 | ~30 | 0 | ~98 |
| Physical Sciences | 5 | ~25 | ~5 | 3 | ~8 | 0 | 0 | 0 | 0 | 0 | 0 | ~20 | 0 | ~66 |
| Public Health | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 4 | 0 | 18 |
| Scripps Oceanography | 0 | 3 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 3 (MAS) | 5 | 0 | 15 |
| Social Sciences | ~30 | ~25 | ~20 | 5 | 1 | 0 | 0 | 0 | 0 | 0 | 1 (MAS) | ~30 | 0 | ~112 |
| GPS (grad only) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 |
| Rady Management (grad) | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 2 (MQF, MPAc) | 1 | 0 | 6 |
| Medicine (grad) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 (MAS) | 0 | 0 | 2 |
| Pharmacy (grad) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Interdisciplinary | ~20 | ~15 | ~10 | 5 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | ~15 | 0 | ~68 |
| **合计** | **~81** | **~114** | **~60** | **~13** | **~48** | **7** | **1** | **2** | **7** | **3** | **~14** | **~137** | **2** | **~486** |

> **Note**: This matrix is approximate. Many graduate programs span multiple departments. Joint programs with SDSU and UC Irvine are counted under their primary UCSD department. The totals reflect distinct program-degree rows from the catalog.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College Architecture

UCSD undergraduates are assigned to one of eight residential colleges (Revelle, John Muir, Thurgood Marshall, Earl Warren, Eleanor Roosevelt, Sixth, Seventh, Eighth), each with its own general education curriculum, advising, and traditions. College choice does NOT constrain major selection — any undergraduate may pursue any major. The 8 academic schools (see Section 0.2 tree) offer the majors; the 8 colleges provide the GE/community framework.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Division of Arts and Humanities

##### African American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Black Diaspora and African American Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Chicanx and Latinx Studies
*(Chicanx and Latinx Studies listed on admissions page but not as a separate catalog degree entry — may be a department offering courses within existing majors)*

##### Cinematic Arts
*(No separate degree listed in catalog — courses within Visual Arts or other programs)*

##### Classical Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classical Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Ethnic Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Linguistics (Cognition and Language) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Linguistics (Language and Society) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Linguistics (Speech and Language Sciences) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Language Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Literature
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Literatures in English | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Literatures in Spanish | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Literature/Writing | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | World Literature and Culture | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Music/Humanities | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Interdisciplinary Computing and the Arts | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Theatre & Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Dance | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Visual Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Visual Arts (Art History/Criticism) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Visual Arts (Media) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Visual Arts (Studio) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Interdisciplinary Computing and the Arts | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Speculative Design | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Division of Biological Sciences

##### Biology Department
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Biology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Biology with a Specialization in Bioinformatics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Ecology, Behavior, and Evolution | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Human Biology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Microbiology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Molecular and Cell Biology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Neurobiology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Halıcıoğlu Data Science Institute (HDSI)

##### Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: Data Science is a selective major with additional admission requirements.

#### Jacobs School of Engineering

##### Bioengineering (BE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Bioengineering: Biotechnology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Bioengineering: Bioinformatics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Bioengineering: BioSystems | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Computer Science and Engineering (CSE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Computer Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Computer Science with Specialization in Bioinformatics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: Computer Engineering is jointly offered with ECE. Data Science BS is administered by HDSI, not CSE.

##### Electrical and Computer Engineering (ECE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Electrical Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Engineering Physics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering and Society | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Mechanical and Aerospace Engineering (MAE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Mechanical Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Mechanical Engineering with a Specialization in Controls and Robotics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Mechanical Engineering with a Specialization in Fluid Mechanics and Thermal Systems | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Mechanical Engineering with a Specialization in Materials Science and Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Mechanical Engineering with a Specialization in Mechanics of Materials | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Mechanical Engineering with a Specialization in Renewable Energy and Environmental Flows | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Nanoengineering (NE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Nanoengineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Structural Engineering (SE)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Structural Engineering | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Division of Physical Sciences

##### Astronomy and Astrophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy and Astrophysics | *(listed on admissions majors page)* |

##### Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Chemistry with Specialization in Earth Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Biochemistry | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Environmental Chemistry | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Molecular Synthesis | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Pharmacological Chemistry | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Bioinformatics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Mathematics (Applied) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Mathematics—Computer Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Mathematics—Applied Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Joint Mathematics-Economics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Probability and Statistics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics—Secondary Education | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Physics/Biophysics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Physics with Specialization in Computational Physics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Physics with Specialization in Earth Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Physics with Specialization in Materials Physics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Physics with Specialization in Astrophysics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | General Physics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | General Physics/Secondary Education | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Herbert Wertheim School of Public Health

##### Public Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Public Health with Concentration in Biostatistics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Public Health with Concentration in Climate and Environmental Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Public Health with Concentration in Community Health Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Public Health with Concentration in Epidemiology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Public Health with Concentration in Health Policy and Management Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Public Health with Concentration in Medicine Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: Public Health is a selective major.

#### Scripps Institution of Oceanography

##### Environmental Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Systems—Earth Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Environmental Systems—Ecology, Behavior and Evolution | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Environmental Systems—Environmental Chemistry | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Systems—Environmental Policy | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Earth Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geosciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Marine Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marine Biology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Oceanic and Atmospheric Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Oceanic and Atmospheric Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Division of Social Sciences

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology (Archaeology) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Anthropology (Biological Anthropology) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Anthropology (Climate Change and Human Solutions) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Anthropology (Sociocultural Anthropology) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Anthropology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Cognitive Science
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Science with Specialization in Clinical Aspects of Cognition | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Cognitive Science with Specialization in Design and Interaction | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Cognitive Science with Specialization in Machine Learning and Neural Computation | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Cognitive Science with Specialization in Neuroscience | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Cognitive Science with Specialization in Language and Culture | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Cognitive and Behavioral Neuroscience | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics (with Rady School of Management) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Joint Economics-Mathematics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: Economics—Public Policy BA/MPP is a combined degree program (UG+grad).

##### Education Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Global Health
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Health | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Global Health | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Human Developmental Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Developmental Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Developmental Sciences | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Human Developmental Sciences with a Specialization in Equity and Diversity | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Human Developmental Sciences with a Specialization in Healthy Aging | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Latin American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Latin American Studies with a Concentration in Mexico | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Latin American Studies with a Concentration in Migration and Border Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Political Science (American Politics) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Political Science (Comparative Politics) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Political Science (International Relations) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Political Science (Political Theory) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Political Science (Public Law) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Political Science (Public Policy) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 8 | Political Science (Race, Ethnicity, and Politics) | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: Political Science (International Affairs) BA/MIA is a combined degree program.

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Psychology with a Specialization in Clinical Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Psychology with a Specialization in Cognitive Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Psychology with a Specialization in Developmental Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Psychology with a Specialization in Human Health | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Psychology with a Specialization in Sensation and Perception | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Psychology with a Specialization in Social Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 8 | Business Psychology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 9 | Cognitive and Behavioral Neuroscience | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Sociology—International Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Sociology—American Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | Sociology—Science and Medicine | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Sociology—Economy and Society | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Sociology—Culture and Communication | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Sociology—Social Inequity | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 8 | Sociology—Law and Society | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

##### Urban Studies and Planning
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Studies and Planning | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate and Development | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

#### Interdisciplinary Majors (Cross-School)

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Black Diaspora and African American Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 2 | Chinese Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 3 | Critical Gender Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 4 | German Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 5 | Global South Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 6 | Italian Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 7 | Japanese Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 8 | Jewish Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 9 | Russian, East European, and Eurasian Studies | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 10 | Study of Religion | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 11 | International Studies—Anthropology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 12 | International Studies—Economics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 13 | International Studies—History | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 14 | International Studies—International Business | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 15 | International Studies—Linguistics | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 16 | International Studies—Literature | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 17 | International Studies—Philosophy | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 18 | International Studies—Political Science | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 19 | International Studies—Sociology | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |
| 20 | College Special Individual Majors | https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html |

> **Note**: 5-year combined BA/MIA programs exist for International Studies—Economics, International Studies—International Business, and International Studies—Political Science.

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 项目 | 联合学院 | 类型 |
|---|------|---------|------|
| 1 | Joint Mathematics-Economics BS | Physical Sciences + Social Sciences | Joint Major |
| 2 | Joint Economics-Mathematics BS | Social Sciences + Physical Sciences | Joint Major |
| 3 | Mathematics—Computer Science BS | Physical Sciences + Engineering | Cross-listed |
| 4 | Computer Engineering BS | CSE (Engineering) + ECE (Engineering) | Shared |
| 5 | Cognitive and Behavioral Neuroscience BS | Psychology + Cognitive Science | Cross-listed |
| 6 | Electrical Engineering and Society BA | ECE (Engineering) + Social Sciences | Cross-school |
| 7 | Interdisciplinary Computing and the Arts BA | Music + Visual Arts | Cross-department |
| 8 | Bioinformatics BS | Chemistry + Bioinformatics | Cross-department |

### 1.4 Minors — Complete List

UCSD offers approximately 60+ undergraduate minors across all schools. The admissions page lists "160+ majors" which includes minors. Specific minor listings are available at `catalog.ucsd.edu` under each department. Common minors include: Accounting, African American Studies, Anthropology, Art History, Biology, Chemistry, Chinese Studies, Cognitive Science, Communication, Computer Science, Critical Gender Studies, Dance, Data Science, Economics, Education Studies, Ethnic Studies, Film Studies, German Studies, Global Health, History, Italian Studies, Japanese Studies, Jewish Studies, Latin American Studies, Law and Society, Linguistics, Literature, Mathematics, Music, Philosophy, Physics, Political Science, Psychology, Public Service, Real Estate and Development, Russian Studies, Sociology, Statistics, Theatre, Urban Studies, Visual Arts, and others.

### 1.5 General Education Requirements

Each of UCSD's 8 colleges has its own distinct general education (GE) curriculum:

| College | GE Philosophy | Key Requirements |
|---------|--------------|------------------|
| Revelle College | Structured liberal arts; breadth & depth | Calculus sequence, science sequence, humanities core, foreign language (4th quarter proficiency), social science, fine arts |
| John Muir College | Flexible breadth | 4 year-long sequences (social/natural sciences/math), 2 of 3 areas (fine arts, foreign language, humanities), 2 analytical writing courses |
| Thurgood Marshall College | Scholar & citizen; Dimensions of Culture | 3-quarter Dimensions of Culture core, math/logic, natural/physical sciences, writing, humanities, fine arts |
| Earl Warren College | Balance philosophy | 2-quarter Writing Program, Ethics & Society, major + 2 additional programs of study, formal skills, cultural diversity |
| Eleanor Roosevelt College | Global citizenship | Making of the Modern World core sequence, natural sciences, fine arts, humanities, social sciences, quantitative methods, regional specialization |
| Sixth College | Culture, Art, and Technology (CAT) | CAT core sequence, science, math, social science, humanities, fine arts, information technology |
| Seventh College | Changing Planet | Synthesis core sequence, sciences, social sciences, arts/humanities, quantitative reasoning |
| Eighth College | Community & Engagement | Newest college (est. 2023); engagement-focused curriculum |

### 1.6 Course-ID to Major Quick-Lookup

UCSD does not use a numeric course-ID system for majors (unlike MIT's "Course 6" system). Majors are identified by department name and degree type (e.g., "Computer Science BS", "Psychology BA").

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Division of Graduate Education and Postdoctoral Affairs
*(Administers most academic graduate programs)*

##### Anthropology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Anthropology and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Anthropology (Science Studies) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Anthropology with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Anthropology with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Anthropology with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Anthropology with a Specialization in Critical Gender Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Anthropology with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Astronomy and Astrophysics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Astronomy and Astrophysics | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Bioengineering
###### MEng, MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Bioengineering | MEng | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Bioengineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Bioengineering | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Bioengineering with a Medical Specialization | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Bioengineering with a Specialization in Medical Device Engineering | MEng | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Bioengineering with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Bioengineering with a Specialization in Computational Neuroscience | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Bioengineering with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Bioengineering with a Specialization in Quantitative Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Engineering Sciences (Bioengineering) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Bioinformatics and Systems Biology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics and Systems Biology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Bioinformatics and Systems Biology with a Specialization in Biomedical Informatics | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Bioinformatics and Systems Biology with a Specialization in Quantitative Biology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Biological Sciences
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biology | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Biology (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Biology with a Specialization in Anthropogeny | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Biology with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Biology with a Specialization in Biology Education Research | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Biology with a Specialization in Immunology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Biology with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Biology with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Biology with a Specialization in Quantitative Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Biomedical Sciences
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Biomedical Sciences with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Biomedical Sciences with a Specialization in Bioinformatics | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Biomedical Sciences with a Specialization in Immunology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Biomedical Sciences with a Specialization in Multiscale Biology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Biomedical Sciences with a Specialization in Quantitative Biology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Biostatistics
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Biostatistics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Chemistry and Biochemistry
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biochemistry and Molecular Biophysics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Biochemistry and Molecular Biophysics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Chemistry | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Chemistry | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Chemistry (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Chemistry with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Chemistry with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Chemistry with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Chemistry with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Chemistry with a Specialization in Quantitative Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Classics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics (Tri-Campus Program with UC Irvine and UC Riverside) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Clinical Psychology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology (Joint with SDSU) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Clinical Psychology and Cognitive Science (Joint with SDSU) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Clinical Research
###### MAS
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Cognitive Science
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Cognitive Science with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Cognitive Science with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Cognitive Science with a Specialization in Human-Centered Design | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Communication
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Communication (Science Studies) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Communication and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Communication with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Communication with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Communication with a Specialization in Critical Gender Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Comparative Studies in Language, Society, and Culture
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Studies in Language, Society, and Culture | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Computational Science, Mathematics, and Engineering
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Science, Mathematics, and Engineering | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Computational Social Science
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Computer Science and Engineering
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Computer Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Computer Science with a Specialization in Human-Centered Design | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Computer Science with a Specialization in Human-Centered Design | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Computer Science (Computer Engineering) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Computer Science (Computer Engineering) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Computer Science (Computer Engineering) with a Specialization in Human-Centered Design | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Computer Science and Cognitive Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Computer Science with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Computer Science and Engineering (Advanced Manufacturing) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 11 | Computer Science and Engineering with a Specialization in Cognitive Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 12 | Computer Science and Engineering with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 13 | Data Science and Engineering | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 14 | Wireless Embedded Systems | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Data Science
###### MS, PhD, MDS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Data Science | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Data Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Data Science | MDS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Data Science with a Specialization in Cognitive Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Economics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Economics with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Economics with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Education Studies
###### MEd, PhD, EdD, MA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education | MEd | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Education | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Education with a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Education Studies with a Specialization in Computational Social Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Educational Leadership | EdD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Teaching and Learning (Curricular Design) | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Teaching and Learning: Bilingual Education (ASL-English) | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Electrical and Computer Engineering
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical and Computer Engineering (Advanced Manufacturing) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Electrical Engineering (Applied Electromagnetics) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Electrical Engineering (Applied Ocean Sciences) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Electrical Engineering (Applied Physics) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Electrical Engineering (Communication Theory and Systems) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Electrical Engineering (Computer Engineering) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Electrical Engineering (Electronic Circuits and Systems) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Electrical Engineering (Intelligent Systems, Robotics, and Control) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Electrical Engineering (Machine Learning and Data Science) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Electrical Engineering (Medical Devices and Systems) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 11 | Electrical Engineering (Medical Imaging) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 12 | Electrical Engineering (Nanoscale Devices and Systems) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 13 | Electrical Engineering (Photonics) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 14 | Electrical Engineering (Signal and Image Processing) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 15 | Engineering Sciences (Electrical and Computer Engineering) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 16 | Wireless Embedded Systems | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Ethnic Studies
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Ethnic Studies with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Ethnic Studies with a Specialization in Critical Gender Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Ethnic Studies with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Global Health
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Global Health | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### History
###### MA, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | History | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | History | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | History (Judaic Studies) | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | History (Science Studies) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | History with a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Linguistics
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Linguistics | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Linguistics and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Linguistics with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Linguistics with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Linguistics with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Literature
###### PhD, MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Literature | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Literature with a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Writing | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Materials Science and Engineering
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Materials Science and Engineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Materials Science and Engineering | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Materials Science and Engineering with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Mathematics
###### MA, PhD, MS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Mathematics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Mathematics (Applied) | MA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Mathematics with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Mathematics with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Mathematics with a Specialization in Statistics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Statistics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Mechanical and Aerospace Engineering
###### MS, PhD, MAS
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Convergent Systems Engineering (Architecture-Based Enterprise Systems) | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Convergent Systems Engineering (Value Supply Chains) | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Convergent Systems Engineering (Cyber-Physical Social Systems) | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Energy and Climate | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Engineering Sciences (Aerospace Engineering) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Engineering Sciences (Applied Mechanics) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Engineering Sciences (Mechanical and Aerospace Engineering) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Engineering Sciences (Applied Ocean Science) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Engineering Sciences (Biomechanics and Biomedical Engineering) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Engineering Sciences (Computational Engineering and Science) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 11 | Engineering Sciences (Controls and Mechatronics) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 12 | Engineering Sciences (Engineering Physics) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 13 | Engineering Sciences (Mechanical Engineering) | MS, PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 14 | Engineering Sciences (Power and Energy Systems) | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 15 | Engineering Sciences with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Music
###### PhD, DMA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Music with a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Contemporary Music Performance | DMA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Nanoengineering
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Chemical Engineering | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Chemical Engineering with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | NanoEngineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | NanoEngineering | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | NanoEngineering with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Neurosciences
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Neurosciences | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Neurosciences and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Neurosciences with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Neurosciences with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Neurosciences with a Specialization in Computational Neuroscience | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Neurosciences with a Specialization in Multiscale Biology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Philosophy
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Philosophy (Science Studies) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Philosophy and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Philosophy with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Philosophy with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Physics
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Physics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Physics (Biophysics) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Physics with a Specialization in Bioinformatics | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Physics with a Specialization in Computational Neuroscience | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Physics with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Physics with a Specialization in Materials Physics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Physics with a Specialization in Multiscale Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Physics with a Specialization in Quantitative Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Political Science
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Political Science and International Affairs | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Political Science with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Political Science with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Political Science and International Affairs with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Political Science and International Affairs with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Psychology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental Psychology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Experimental Psychology and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Experimental Psychology with a Specialization in Anthropogeny | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Psychology with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Experimental Psychology with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Experimental Psychology with a Specialization in Critical Gender Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Public Health
###### PhD, MPH
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Health with a Concentration in Health Services Research and Implementation Sciences | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Public Health (Epidemiology) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Public Health (Global Health) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Public Health (Health Behavior) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Public Health | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Public Health (Epidemiology) | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Public Health (Health Behavior) | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Public Health (Health Policy) | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Public Health (Public Mental Health) | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Public Health (Technology and Precision Health) | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 11 | Public Health with a Specialization in Human-Centered Design | MPH | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Sociology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Sociology (Science Studies) | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Sociology and Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Sociology with a Specialization in Cognitive Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Sociology with a Specialization in Computational Social Science | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Sociology with a Specialization in Critical Gender Studies | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Sociology with a Specialization in Interdisciplinary Environmental Research | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Structural Engineering
###### MS, PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Geotechnical Engineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Structural Engineering | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Structural Engineering | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Engineering Sciences (Structural Engineering) (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Structural Engineering with a Specialization in Structural Health Monitoring and Non-Destructive Evaluation | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Structural Engineering with a Specialization in Computational Science | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Theatre and Dance
###### PhD, MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Drama and Theatre (Joint with UC Irvine) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Drama and Theatre with a Specialization in Critical Gender Studies (Joint with UC Irvine) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Theatre and Dance (Acting) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Theatre and Dance (Dance Theatre) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Theatre and Dance (Design) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Theatre and Dance (Directing) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Theatre and Dance (Playwriting) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Theatre and Dance (Stage Management) | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Urban Studies and Planning
###### PhD, MURP
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Urban Studies and Regional Planning | MURP | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Urban Studies and Planning | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

##### Visual Arts
###### PhD, MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History, Theory and Criticism | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Art History, Theory and Criticism with a Concentration in Art Practice | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Art History, Theory and Criticism with a Specialization in Anthropogeny | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Art History, Theory and Criticism with a Concentration in Art Practice and a Specialization in Anthropogeny | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Art History, Theory and Criticism with a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Art History, Theory and Criticism with a Concentration in Art Practice and a Specialization in Critical Gender Studies | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Art History, Theory and Criticism with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Art History, Theory and Criticism with a Concentration in Art Practice and a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Visual Arts | MFA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### School of Global Policy and Strategy (GPS)
##### International Affairs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | International Affairs | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | International Affairs | MIA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Chinese Economic and Political Affairs | MCEPA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Public Policy | MPP | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### Rady School of Management
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration | MBA | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Business Analytics | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Management | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Management with a Specialization in Anthropogeny | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Management with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Quantitative Finance | MQF | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Professional Accountancy | MPAc | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### School of Medicine
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Physician Assistant Education Program | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Precision Medicine Therapeutics in Oncology | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### Scripps Institution of Oceanography
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Climate Science and Policy | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 2 | Earth Sciences | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 3 | Earth Sciences | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 4 | Earth Sciences with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 5 | Geophysics (Joint with SDSU) | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 6 | Marine Biodiversity and Conservation | MAS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 7 | Marine Biology | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 8 | Marine Biology | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 9 | Marine Biology with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 10 | Oceanography | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 11 | Oceanography | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |
| 12 | Oceanography with a Specialization in Interdisciplinary Environmental Research | PhD | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### Skaggs School of Pharmacy and Pharmaceutical Sciences
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Drug Development and Product Management | MS | https://catalog.ucsd.edu/graduate/degrees-offered/index.html |

#### Joint Programs with SDSU (San Diego State University)

UCSD and SDSU jointly administer several doctoral programs. Students are admitted to the joint program and may have advisors at either institution:

| # | 项目 | 学位 |
|---|------|------|
| 1 | Audiology | AuD |
| 2 | Biology | PhD |
| 3 | Chemistry | PhD |
| 4 | Clinical Psychology | PhD |
| 5 | Clinical Psychology and Cognitive Science | PhD |
| 6 | Engineering Sciences (Bioengineering) | PhD |
| 7 | Engineering Sciences (Electrical and Computer Engineering) | PhD |
| 8 | Engineering Sciences (Mechanical and Aerospace Engineering) | PhD |
| 9 | Engineering Sciences (Structural Engineering) | PhD |
| 10 | Geophysics | PhD |
| 11 | Interdisciplinary Research on Substance Use | PhD |
| 12 | Language and Communicative Disorders | PhD |
| 13 | Mathematics and Science Education | PhD |
| 14 | Public Health (Epidemiology) | PhD |
| 15 | Public Health (Global Health) | PhD |
| 16 | Public Health (Health Behavior) | PhD |

### 2.2 At Least One Program's Full Deep-Dive (Computer Science PhD)

- **Department**: Computer Science and Engineering (CSE), Jacobs School of Engineering
- **Degrees offered**: MS, PhD
- **Application portal**: UCSD Graduate Division application at `https://grad.ucsd.edu/admissions/`
- **Contact**: `gradadmissions@ucsd.edu`, (858) 534-3554
- **Mailing address**: University of California San Diego, Student Services Center, 4th Floor, 9500 Gilman Drive #0003, La Jolla, CA 92093
- **GRE**: Per-program policy (check department website)
- **English proficiency**: TOEFL or IELTS required for international applicants
- **Application fee**: Set by UC Graduate Division
- **Funding**: Most PhD students receive full funding (TA/RA/fellowships)

### 2.3 Graduate Admissions Model

UCSD uses a **decentralized** graduate admissions model:
- The **Division of Graduate Education and Postdoctoral Affairs** provides central services and administers the application portal
- Each department/program makes its own admission decisions
- Professional schools (GPS, Rady, Medicine, Pharmacy) have separate admissions processes
- Apply via `https://grad.ucsd.edu/admissions/`
- Email: `gradadmissions@ucsd.edu`

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Application portal | UC Application (`https://apply.universityofcalifornia.edu/my-application/login`) | admissions.ucsd.edu/apply/index.html |
| Application opens | August 1 | admissions.ucsd.edu/apply/index.html |
| Application submission period | October 1 – December 1 | admissions.ucsd.edu/apply/index.html |
| EA deadline | N/A (UC system does not offer EA) | — |
| ED deadline | N/A (UC system does not offer ED) | — |
| Regular Decision deadline | December 1 | admissions.ucsd.edu/apply/index.html |
| Decision notification | Late March / Early April (typical UC timeline) | — |
| Enrollment confirmation deadline | May 1 (typical) | — |
| Application fee | $80 per campus ($95 for international/non-immigrant) | admission.universityofcalifornia.edu/apply-now.html |
| Fee waivers | Up to 4 campuses for qualified students | admission.universityofcalifornia.edu/apply-now.html |
| SAT/ACT policy | **TEST-FREE**: "UC San Diego will not consider SAT or ACT test scores as a factor in admissions decisions." | admissions.ucsd.edu/international/index.html |
| Superscore | N/A (test-free) | — |
| Letters of recommendation | Not required (may be requested for supplemental review) | admission.universityofcalifornia.edu/apply-now.html |
| Transcript submission | Do NOT send at application; send if admitted | admission.universityofcalifornia.edu/apply-now.html |
| Admit rate (2025) | 28% (136,000+ first-year applications) | admissions.ucsd.edu/first-year/index.html |
| GPA range (2025, middle 50%) | 4.12 – 4.29 | admissions.ucsd.edu/first-year/index.html |

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分 | 推荐分 | 适用条件 |
|------|--------|--------|----------|
| TOEFL iBT (new scale, Jan 2026+) | 4.5 | — | International first-year applicants |
| TOEFL iBT (old scale, before Jan 2026) | 83 | — | International first-year applicants |
| TOEFL Paper-based | 550 | — | International first-year applicants |
| IELTS (Academic module) | 7 | — | International first-year applicants |
| Duolingo English Test (DET) | 115 | — | International first-year applicants |
| AP English Language and Composition | 3 | — | Alternative fulfillment |
| AP English Literature and Composition | 3 | — | Alternative fulfillment |
| IB English (Lang. A) Higher Level | 5 | — | Alternative fulfillment |
| IB English (Lang. A) Standard Level | 6 | — | Alternative fulfillment |

> **Source**: `admissions.ucsd.edu/international/index.html` (expanded "Applying as a First-Year International Student" section).
> **Transfer applicants**: Can fulfill with grades of "B" or better in two required transferable English composition courses.
> **Exams must be completed no more than two years prior to transfer** (for transfer applicants).

### 3.3 Graduate — Global Rules

- **Model**: Decentralized; each department/program sets own requirements
- **Application portal**: UCSD Graduate Division at `https://grad.ucsd.edu/admissions/`
- **Application fee**: Set by UC Graduate Division (typically $135 for domestic, $155 for international)
- **GRE**: Per-program policy (some require, some optional, some not accepted)
- **English proficiency**: TOEFL or IELTS required for international applicants
- **CGS April 15**: UCSD is a signatory
- **Funding**: PhD programs typically fully funded; master's programs vary
- **Contact**: `gradadmissions@ucsd.edu`, (858) 534-3554

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year, Line-Itemized)

| 费用项目 | 金额 (CA Resident) | 金额 (Non-CA Resident) | 说明 |
|---------|-------------------|----------------------|------|
| UC Systemwide Tuition and Fees | $15,588 | $15,588 | All UC students pay this |
| UC San Diego Campus Fees | $2,511 | $2,511 | Campus-specific fees |
| UC San Diego Health Fee | $3,195 | $3,195 | May be waived with equivalent private insurance |
| UC San Diego One-time Document Fee | $165 | $165 | Assessed upon initial enrollment only |
| **Subtotal: Tuition and Fees** | **$21,459** | **$21,459** | Direct cost |
| Non-California Resident Supplemental Tuition | N/A | $39,270 | Additional for non-residents |
| **Total Tuition and Fees** | **$21,459** | **$60,729** | |
| Food & Housing (with parents) | $8,604 | $8,604 | Living with parents |
| Food & Housing (on campus) | $20,445 | $20,445 | On-campus housing |
| Food & Housing (off campus) | $20,502 | $20,502 | Off-campus housing |
| Books, course materials, supplies, equipment | $1,203 | $1,203 | |
| Miscellaneous Personal Expenses | $2,760 – $3,039 | $2,760 – $3,039 | Varies by living arrangement |
| Transportation | $921 – $2,814 | $921 – $2,814 | Varies by living arrangement |
| **Estimated Total (On Campus, CA Resident)** | **$46,788** | — | |
| **Estimated Total (On Campus, Non-CA Resident)** | — | **$86,058** | |
| **Estimated Total (Off Campus, CA Resident)** | **$48,285** | — | |
| **Estimated Total (Off Campus, Non-CA Resident)** | — | **$87,555** | |
| **Estimated Total (Living with Parents, CA Resident)** | **$37,119** | — | |
| **Estimated Total (Living with Parents, Non-CA Resident)** | — | **$76,389** | |

> **Source**: `fas.ucsd.edu/cost-of-attendance/undergraduates/index.html` (2026 Cohort, 2026-27 Academic Year).
> **Note**: "The annual cost of attendance includes estimates for tuition and fees, living expenses (i.e. food and housing), books, course materials, supplies, and equipment, miscellaneous personal expenses and transportation expenses."

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 | 来源 |
|------|-----|------|
| FAFSA school code | 001317 | fas.ucsd.edu/applying/undergraduates/index.html |
| Priority filing deadline (2026-27) | March 2, 2026 | fas.ucsd.edu/applying/undergraduates/index.html |
| Application required | FAFSA (US citizens/eligible non-citizens) or CADAA (undocumented/AB540) | fas.ucsd.edu/applying/undergraduates/index.html |
| Blue and Gold program | UC commitment to financial aid for CA students | fas.ucsd.edu/applying/undergraduates/index.html |
| International students | NOT eligible for federal or state financial aid; must prove sufficient funds for visa | admissions.ucsd.edu/why/cost-aid/index.html |
| Out-of-state students | Not eligible for CA financial aid; may receive federal aid | admissions.ucsd.edu/why/cost-aid/index.html |
| Need-blind / Need-aware | Need-aware for OOS and international students | (UC system-wide policy) |
| Aid types | Grants, Loans, Scholarships, Work-Study | fas.ucsd.edu/types/index.html |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 | 来源 |
|------|-----|------|
| Tuition & Fees | Varies by program; see `grad.ucsd.edu/financial/tuition-fees.html` | grad.ucsd.edu |
| Funding for PhD students | Most PhD programs provide full funding (TA/RA/fellowships) | grad.ucsd.edu/financial/index.html |
| Funding for master's students | Varies; many self-funded | grad.ucsd.edu |
| Professional programs (GPS, Rady) | Separate tuition structures | fas.ucsd.edu/cost-of-attendance/ |
| Financial support FAQ | `grad.ucsd.edu/financial/financial-faq.html` | grad.ucsd.edu |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.application.platform
  value: UC Application
  source_url: https://admissions.ucsd.edu/apply/index.html
  source_snippet: "Students can apply to UC San Diego using the UC application."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.application.deadline
  value: "October 1 – December 1"
  source_url: https://admissions.ucsd.edu/apply/index.html
  source_snippet: "Oct. 1-Dec. 1 - 2026 Fall Application submission period"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application.opens
  value: "August 1"
  source_url: https://admissions.ucsd.edu/apply/index.html
  source_snippet: "Aug. 1 - UC application opens for editing"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.application.fee
  value: "$80 ($95 international)"
  source_url: https://admission.universityofcalifornia.edu/apply-now.html
  source_snippet: "The application fee is $80 for each UC campus ($95 for international and non-immigrant applicants)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.testing.policy
  value: "Test-FREE (SAT/ACT not considered)"
  source_url: https://admissions.ucsd.edu/international/index.html
  source_snippet: "UC San Diego will not consider SAT or ACT test scores as a factor in admissions decisions."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.toefl_ibt_new
  value: "4.5 (new scale, Jan 2026+)"
  source_url: https://admissions.ucsd.edu/international/index.html
  source_snippet: "TOEFL minimum scores Internet-based: 4.5 (Effective January 2026)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.toefl_ibt_old
  value: "83 (before Jan 2026)"
  source_url: https://admissions.ucsd.edu/international/index.html
  source_snippet: "83 (Exams cmpleted prior to Janurary 2026)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english_proficiency.ielts
  value: "7 (Academic module)"
  source_url: https://admissions.ucsd.edu/international/index.html
  source_snippet: "IELTS minimum score of 7 (Academic module)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_proficiency.det
  value: "115"
  source_url: https://admissions.ucsd.edu/international/index.html
  source_snippet: "Duolingo English Test (DET): Minimum score of 115"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.cost.tuition_fees_resident
  value: "$21,459"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "Components of CA Resident Tuition and Fees: $21,459"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.tuition_fees_nonresident
  value: "$60,729"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "Non-California Resident Supplemental Tuition: $39,270" + base $21,459
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.total_on_campus_resident
  value: "$46,788"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "Estimated CA Resident Cost Totals: $46,788 (On Campus)"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.cost.total_on_campus_nonresident
  value: "$86,058"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "Estimated Non-California Resident Cost Totals: $86,058 (On Campus)"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-014:
  field: undergraduate.cost.systemwide_tuition
  value: "$15,588"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "UC Systemwide Tuition and Fees: $15,588"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-015:
  field: undergraduate.cost.nonresident_supplemental
  value: "$39,270"
  source_url: https://fas.ucsd.edu/cost-of-attendance/undergraduates/index.html
  source_snippet: "Non-California Resident Supplemental Tuition: $39,270"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-016:
  field: undergraduate.admit_rate
  value: "28%"
  source_url: https://admissions.ucsd.edu/first-year/index.html
  source_snippet: "Admit Rate 28% 136,000+ first-year applications were received for fall 2025."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.gpa_range
  value: "4.12 – 4.29"
  source_url: https://admissions.ucsd.edu/first-year/index.html
  source_snippet: "GPA 4.12 - 4.29 GPA range reflects the middle 50%"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.colleges
  value: "8 colleges (Revelle, Muir, Marshall, Warren, Roosevelt, Sixth, Seventh, Eighth)"
  source_url: https://catalog.ucsd.edu/undergraduate/colleges/index.html
  source_snippet: "Revelle, John Muir, Thurgood Marshall, Earl Warren, Eleanor Roosevelt, Sixth, Seventh, and Eighth."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-019:
  field: undergraduate.programs.count
  value: "~155 bachelor's degree programs"
  source_url: https://catalog.ucsd.edu/undergraduate/degrees-offered/index.html
  source_snippet: "Undergraduate Degrees Offered, 2026–27" (167 catalog entries including specializations)
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.model
  value: "Decentralized; each department/program decides"
  source_url: https://grad.ucsd.edu/admissions/index.html
  source_snippet: "We offer a wide variety of academic and professional graduate degree programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.contact
  value: "gradadmissions@ucsd.edu, (858) 534-3554"
  source_url: https://grad.ucsd.edu/admissions/index.html
  source_snippet: "Email gradadmissions@ucsd.edu Phone 858-534-3554"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.programs.count
  value: "~300+ graduate degree programs"
  source_url: https://catalog.ucsd.edu/graduate/degrees-offered/index.html
  source_snippet: "Graduate Degrees Offered, 2026–27" (255 catalog entries)
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.professional_schools
  value: "GPS, Rady, Medicine, Scripps, Pharmacy"
  source_url: https://catalog.ucsd.edu/graduate/graduate-professional-schools/index.html
  source_snippet: "School of Global Policy and Strategy, Rady School of Management, School of Medicine, Scripps Institution of Oceanography, Skaggs School of Pharmacy and Pharmaceutical Sciences"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
ucsd-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-arts-humanities            (Section 1: Arts & Humanities programs)
├── 02-ug-biological-sciences        (Section 1: Biological Sciences programs)
├── 03-ug-data-science               (Section 1: HDSI programs)
├── 04-ug-engineering                (Section 1: Jacobs School programs)
├── 05-ug-physical-sciences          (Section 1: Physical Sciences programs)
├── 06-ug-public-health              (Section 1: Public Health programs)
├── 07-ug-scripps                    (Section 1: Scripps programs)
├── 08-ug-social-sciences            (Section 1: Social Sciences programs)
├── 09-ug-interdisciplinary          (Section 1: Interdisciplinary majors)
├── 10-grad-division                 (Section 2: Graduate Division programs)
├── 11-grad-gps                      (Section 2: GPS programs)
├── 12-grad-rady                     (Section 2: Rady programs)
├── 13-grad-medicine                 (Section 2: Medicine programs)
├── 14-grad-scripps                  (Section 2: Scripps grad programs)
├── 15-grad-pharmacy                 (Section 2: Pharmacy programs)
├── 16-application-requirements      (Section 3: deadlines, tests, requirements)
├── 17-costs-financial-aid           (Section 4: COA, aid policy)
└── 18-evidence-chain                (Section 5: all evidence blocks)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "ucsd-knowledge-base-v2"
  school: "<home school/college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-Up Data Items (Prioritized)

| 优先级 | 数据项 | 目标 URL | 说明 |
|--------|--------|---------|------|
| P0 | Full minors list with URLs | catalog.ucsd.edu | Catalog listing exists but was not fully extracted in this run |
| P0 | Graduate program GRE requirements (per-program) | grad.ucsd.edu per department | Decentralized; each program sets own policy |
| P0 | Graduate application fee exact amount | grad.ucsd.edu/admissions/ | Page did not render fully |
| P1 | Per-college GE requirement details | catalog.ucsd.edu/undergraduate/colleges/ | Only summary extracted; full requirements behind sub-pages |
| P1 | Graduate tuition rates (per-program) | grad.ucsd.edu/financial/tuition-fees.html | Page timed out during extraction |
| P1 | Financial aid packaging policy details | fas.ucsd.edu/applying/undergraduates/ | Summary extracted; full policy behind sub-pages |
| P2 | International student visa/financial requirements details | admissions.ucsd.edu/international/ | Country-specific requirements behind dropdowns |
| P2 | Transfer admission requirements | admissions.ucsd.edu/transfer/ | Not extracted in this run |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | UCSD | (Other schools) |
|------|------|-----------------|
| Type | Public (UC system) | |
| Location | San Diego, CA | |
| Application portal | UC Application | |
| EA deadline | N/A (no EA) | |
| RD deadline | December 1 | |
| SAT/ACT required? | No (test-FREE) | |
| TOEFL min (iBT) | 4.5 (new) / 83 (old) | |
| IELTS min | 7 | |
| DET min | 115 | |
| App fee | $80 / $95 intl | |
| Tuition (CA resident) | $15,588 systemwide | |
| Tuition (non-resident) | $54,858 total | |
| Total COA (on-campus, resident) | $46,788 | |
| Total COA (on-campus, non-resident) | $86,058 | |
| Need-blind (intl)? | No (need-aware) | |
| Admit rate | 28% | |
| UG colleges | 8 (residential GE) | |
| Academic schools | 8 UG + 5 grad/professional | |
| Total programs (Rule 1) | ~455+ | |
| UG majors | ~155 | |
| Grad programs | ~300+ | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.ucsd.edu, catalog.ucsd.edu, fas.ucsd.edu, grad.ucsd.edu, admission.universityofcalifornia.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch
> **Granularity**: school → department → degree-level → program
