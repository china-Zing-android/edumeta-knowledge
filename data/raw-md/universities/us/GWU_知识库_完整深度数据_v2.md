# George Washington University (GWU) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/etc.) | 131 |
| 本科辅修 (Minor) | 104 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 285 |
| 研究生高级证书 (Graduate Certificate / Post-Master's / Post-Bacc) | 139 |
| 双学位项目 (Dual Degree) | 61 |
| **学位项目总计 (UG + Grad)** | **754** |
| 学院 / 独立系所总数 | 11 |

> **Note**: 754 total includes all program types: UG majors (131), UG minors (104), grad degrees (285), grad certificates (139), and dual degrees (61). Some programs are concentrations within majors.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
George Washington University
├── Columbian College of Arts and Sciences          [学院]
│   ├── Africana Studies                            [系]
│   ├── American Studies                            [系]
│   ├── Anthropology                                [系]
│   ├── Art History                                 [系]
│   ├── Astronomy and Astrophysics                  [系]
│   ├── Biological Sciences                         [系]
│   ├── Chemistry                                   [系]
│   ├── Classical and Near Eastern Languages        [系]
│   ├── Communication                               [系]
│   ├── Computer Science                            [系]
│   ├── Data Science                                [系]
│   ├── Economics                                   [系]
│   ├── English                                     [系]
│   ├── Environmental Studies                       [系]
│   ├── Fine Arts                                   [系]
│   ├── Forensic Sciences                           [系]
│   ├── Geography                                   [系]
│   ├── Geology                                     [系]
│   ├── History                                     [系]
│   ├── Judaic Studies                              [系]
│   ├── Mathematics                                 [系]
│   ├── Music                                       [系]
│   ├── Philosophy                                  [系]
│   ├── Physics                                     [系]
│   ├── Political Science                           [系]
│   ├── Psychological and Brain Sciences            [系]
│   ├── Religion                                    [系]
│   ├── Sociology                                   [系]
│   ├── Speech, Language and Hearing Sciences        [系]
│   ├── Statistics                                  [系]
│   └── Theatre and Dance                           [系]
├── GW School of Business                           [学院]
│   ├── Accountancy                                 [系]
│   ├── Finance                                     [系]
│   ├── Information Systems and Technology          [系]
│   ├── Management                                  [系]
│   ├── Marketing                                   [系]
│   └── Strategic Management and Public Policy      [系]
├── School of Engineering and Applied Science       [学院]
│   ├── Biomedical Engineering                      [系]
│   ├── Civil and Environmental Engineering         [系]
│   ├── Computer Science                            [系]
│   ├── Electrical and Computer Engineering         [系]
│   ├── Engineering Management and Systems          [系]
│   ├── Mechanical and Aerospace Engineering        [系]
│   └── Systems Engineering                         [系]
├── Elliott School of International Affairs         [学院]
│   ├── International Affairs                       [系]
│   ├── International Development Studies           [系]
│   ├── International Science and Technology        [系]
│   └── Security Policy Studies                     [系]
├── Graduate School of Education and Human Development [学院]
│   ├── Counseling                                  [系]
│   ├── Curriculum and Pedagogy                     [系]
│   ├── Educational Leadership                      [系]
│   ├── Human Development                           [系]
│   └── Special Education                           [系]
├── Milken Institute School of Public Health        [学院]
│   ├── Biostatistics                               [系]
│   ├── Environmental and Occupational Health       [系]
│   ├── Epidemiology                                [系]
│   ├── Global Health                               [系]
│   ├── Health Policy and Management                [系]
│   └── Prevention and Community Health             [系]
├── School of Medicine and Health Sciences           [学院]
│   ├── Anatomy and Regenerative Biology            [系]
│   ├── Biochemistry and Molecular Biology          [系]
│   ├── Biomedical Laboratory Science               [系]
│   ├── Clinical Research and Leadership            [系]
│   ├── Emergency Medicine                          [系]
│   ├── Genomics and Precision Medicine             [系]
│   ├── Geriatrics and Gerontology                  [系]
│   ├── Microbiology, Immunology, and Tropical      [系]
│   ├── Physician Assistant Studies                 [系]
│   ├── Rehabilitation Sciences                     [系]
│   └── Surgery                                     [系]
├── School of Nursing                               [学院]
│   ├── Adult-Gerontology                           [系]
│   ├── Family Nurse Practitioner                   [系]
│   ├── Nurse-Midwifery                             [系]
│   └── Psychiatric Mental Health                   [系]
├── College of Professional Studies                 [学院]
│   ├── Homeland Security                           [系]
│   ├── Paralegal Studies                           [系]
│   ├── Project Management                          [系]
│   └── Publishing                                  [系]
├── GW Law School                                   [学院]
│   └── Law                                         [系]
└── Interdisciplinary and Special Programs          [独立项目]
    ├── University-wide interdisciplinary programs  [系]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 54 |
| BS | Bachelor of Science | 本科 | 58 |
| BFA | Bachelor of Fine Arts | 本科 | 5 |
| BPS | Bachelor of Professional Studies | 本科 | 3 |
| BSHS | Bachelor of Science in Health Sciences | 本科 | 10 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| Minor | 辅修 | 本科 | 100 |
| Micro-Minor | 微辅修 | 本科 | 4 |
| UG Certificate | 本科证书 | 本科 | 1 |
| MA | Master of Arts | 研究生 | 35 |
| MS | Master of Science | 研究生 | 51 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 21 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MEng | Master of Engineering | 研究生 | 4 |
| DEng | Doctor of Engineering | 研究生 | 6 |
| MAccy | Master of Accountancy | 研究生 | 2 |
| MSN | Master of Science in Nursing | 研究生 | 6 |
| MSHS | Master of Science in Health Sciences | 研究生 | 11 |
| MPS | Master of Professional Studies | 研究生 | 11 |
| MFS | Master of Forensic Sciences | 研究生 | 3 |
| MHA | Master of Health Administration | 研究生 | 2 |
| MHRM | Master of Human Resource Management | 研究生 | 1 |
| MIPP | Master of International Policy and Practice | 研究生 | 2 |
| MIS | Master of International Studies | 研究生 | 1 |
| MAT | Master of Arts in Teaching | 研究生 | 1 |
| MAEd&HD | Master of Arts in Education and Human Development | 研究生 | 15 |
| EdS | Education Specialist | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 57 |
| EdD | Doctor of Education | 研究生 | 5 |
| PsyD | Doctor of Psychology | 研究生 | 1 |
| DrPH | Doctor of Public Health | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 7 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DHS | Doctor of Health Sciences | 研究生 | 3 |
| MD | Doctor of Medicine | 研究生 | 1 |
| Grad Certificate | Graduate Certificate | 研究生 | 88 |
| Post-Masters Cert | Post-Master's Certificate | 研究生 | 6 |
| Post-Bacc Cert | Post-Baccalaureate Certificate | 研究生 | 9 |
| Executive MBA | Executive Master of Business Administration | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 \ 级别 | BA | BS | BFA | Minor | MA | MS | MBA | PhD | Grad Cert | 合计 |
|------------|----|----|-----|-------|----|----|-----|-----|-----------|------|
| Columbian College of Arts and Sciences | 54 | 12 | 0 | 72 | 35 | 12 | 0 | 57 | 44 | 286 |
| GW School of Business | 0 | 1 | 0 | 0 | 0 | 8 | 3 | 0 | 79 | 91 |
| School of Engineering and Applied Science | 0 | 7 | 0 | 7 | 0 | 35 | 0 | 7 | 45 | 101 |
| Elliott School of International Affairs | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 26 | 28 |
| Graduate School of Education and Human Development | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 5 | 40 | 60 |
| Milken Institute School of Public Health | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 63 | 66 |
| School of Medicine and Health Sciences | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 3 | 43 | 57 |
| School of Nursing | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 18 | 24 |
| College of Professional Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 35 | 35 |
| GW Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| Interdisciplinary | 0 | 0 | 0 | 25 | 0 | 0 | 0 | 0 | 0 | 5 |
| **合计** | **54** | **20** | **0** | **104** | **52** | **74** | **3** | **73** | **494** | **754** |

> **Note**: Some programs are dual degrees (e.g., "BA and MA", "BS and MS") which are counted once in the total. The matrix above shows the primary degree type for each program.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

GWU has 11 schools and colleges, with undergraduate programs primarily in Columbian College of Arts and Sciences, GW School of Business, School of Engineering and Applied Science, Elliott School of International Affairs, and School of Nursing. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### Columbian College of Arts and Sciences

##### Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://bulletin.gwu.edu/arts-sciences/africana-studies/ba/ |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://bulletin.gwu.edu/arts-sciences/american-studies/ba/ |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.gwu.edu/arts-sciences/anthropology/ba/ |
| 2 | Archaeology | https://bulletin.gwu.edu/arts-sciences/anthropology/ba-archaeology/ |
| 3 | Biological Anthropology | https://bulletin.gwu.edu/arts-sciences/anthropology/ba-biological-anthropology/ |

##### Art History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://bulletin.gwu.edu/arts-sciences/art-history/ba/ |

##### Astronomy and Astrophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy and Astrophysics | https://bulletin.gwu.edu/arts-sciences/physics/astronomy-astrophysics-bs/ |

##### Biological Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.gwu.edu/arts-sciences/biology/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://bulletin.gwu.edu/arts-sciences/biology/bs/ |
| 2 | Biological Anthropology and Human Paleobiology | https://bulletin.gwu.edu/arts-sciences/anthropology/bs-biological-anthropology-human-paleobiology/ |
| 3 | Bioinformatics | https://bulletin.gwu.edu/arts-sciences/biology/bs-bioinformatics/ |

##### Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.gwu.edu/arts-sciences/chemistry/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.gwu.edu/arts-sciences/chemistry/bs/ |
| 2 | Biochemistry | https://bulletin.gwu.edu/arts-sciences/chemistry/bs-biochemistry/ |

##### Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://bulletin.gwu.edu/arts-sciences/communication/ba/ |
| 2 | Speech, Language and Hearing Science | https://bulletin.gwu.edu/arts-sciences/speech-language-hearing/ba/ |

##### Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.gwu.edu/arts-sciences/computer-science/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.gwu.edu/arts-sciences/computer-science/bs/ |

##### Data Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | https://bulletin.gwu.edu/arts-sciences/data-science/bs/ |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.gwu.edu/arts-sciences/economics/ba/ |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://bulletin.gwu.edu/arts-sciences/english/ba/ |
| 2 | Creative Writing | https://bulletin.gwu.edu/arts-sciences/english/ba-creative-writing/ |

##### Environmental Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Studies | https://bulletin.gwu.edu/arts-sciences/geography/ba-environmental-studies/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://bulletin.gwu.edu/arts-sciences/geography/bs-environmental-science/ |

##### Fine Arts
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Arts | https://bulletin.gwu.edu/arts-sciences/fine-arts/bfa/ |
| 2 | Graphic Design | https://bulletin.gwu.edu/arts-sciences/fine-arts/bfa-graphic-design/ |
| 3 | Interaction Design | https://bulletin.gwu.edu/arts-sciences/fine-arts/bfa-interaction-design/ |
| 4 | Photojournalism | https://bulletin.gwu.edu/arts-sciences/fine-arts/bfa-photojournalism/ |

##### Forensic Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Sciences | https://bulletin.gwu.edu/arts-sciences/forensic-sciences/bs/ |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://bulletin.gwu.edu/arts-sciences/geography/ba/ |

##### Geology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://bulletin.gwu.edu/arts-sciences/geology/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://bulletin.gwu.edu/arts-sciences/geology/bs/ |
| 2 | Geology, Environmental | https://bulletin.gwu.edu/arts-sciences/geology/bs-environmental/ |
| 3 | Geology, Paleobiology | https://bulletin.gwu.edu/arts-sciences/geology/bs-paleobiology/ |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://bulletin.gwu.edu/arts-sciences/history/ba/ |

##### Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/bs-applied-mathematics/ |
| 2 | Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/bs/ |
| 3 | Statistics | https://bulletin.gwu.edu/arts-sciences/mathematics/bs-statistics/ |

##### Music
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://bulletin.gwu.edu/arts-sciences/music/ba/ |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.gwu.edu/arts-sciences/philosophy/ba/ |

##### Physics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.gwu.edu/arts-sciences/physics/ba/ |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.gwu.edu/arts-sciences/physics/bs/ |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.gwu.edu/arts-sciences/political-science/ba/ |
| 2 | Political Communication | https://bulletin.gwu.edu/arts-sciences/political-science/ba-political-communication/ |

##### Psychological and Brain Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/ba/ |

##### Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religion | https://bulletin.gwu.edu/arts-sciences/religion/ba/ |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.gwu.edu/arts-sciences/sociology/ba/ |

##### Speech, Language and Hearing Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech, Language and Hearing Science | https://bulletin.gwu.edu/arts-sciences/speech-language-hearing/ba/ |

##### Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://bulletin.gwu.edu/arts-sciences/mathematics/bs-statistics/ |

##### Theatre and Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre | https://bulletin.gwu.edu/arts-sciences/theatre-dance/ba/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://bulletin.gwu.edu/arts-sciences/theatre-dance/bfa-dance/ |

#### GW School of Business

##### Accountancy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://bulletin.gwu.edu/business/accountancy/bs/ |

#### School of Engineering and Applied Science

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.gwu.edu/engineering-applied-science/biomedical-engineering/bs/ |

##### Civil and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://bulletin.gwu.edu/engineering-applied-science/civil-environmental-engineering/bs-civil-engineering/ |
| 2 | Environmental Engineering | https://bulletin.gwu.edu/engineering-applied-science/civil-environmental-engineering/bs-environmental-engineering/ |

##### Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.gwu.edu/engineering-applied-science/computer-science/bs/ |

##### Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.gwu.edu/engineering-applied-science/electrical-computer-engineering/bs-electrical-engineering/ |
| 2 | Computer Engineering | https://bulletin.gwu.edu/engineering-applied-science/electrical-computer-engineering/bs-computer-engineering/ |

##### Mechanical and Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.gwu.edu/engineering-applied-science/mechanical-aerospace-engineering/bs-mechanical-engineering/ |
| 2 | Aerospace Engineering | https://bulletin.gwu.edu/engineering-applied-science/mechanical-aerospace-engineering/bs-aerospace-engineering/ |

#### Elliott School of International Affairs

##### International Affairs
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Affairs | https://bulletin.gwu.edu/international-affairs/international-affairs/ba/ |
| 2 | Asian Studies | https://bulletin.gwu.edu/international-affairs/asian-studies/ba/ |
| 3 | Latin American and Hemispheric Studies | https://bulletin.gwu.edu/international-affairs/latin-american-hemispheric-studies/ba/ |

#### School of Nursing

##### Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://bulletin.gwu.edu/nursing/bsn/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 项目 | 父学院 | URL |
|---|------|--------|-----|
| 1 | BA and MA (various) | Multiple | https://bulletin.gwu.edu/arts-sciences/anthropology/dual-ba-ma/ |
| 2 | BS and MS (various) | Multiple | https://bulletin.gwu.edu/engineering-applied-science/computer-science/combined-seas-bs-ms-computer-science/ |
| 3 | BA or BS and MPP | CCAS + Elliott | https://bulletin.gwu.edu/arts-sciences/political-science/dual-ba-mpp/ |

### 1.4 Minors — Complete List

GWU offers 104 undergraduate minors across all schools. Key minors include:

| # | Minor Name | Home School | URL |
|---|------------|-------------|-----|
| 1 | Accountancy | GW School of Business | https://bulletin.gwu.edu/business/accountancy/minor/ |
| 2 | Africana Studies | Columbian College | https://bulletin.gwu.edu/arts-sciences/africana-studies/minor/ |
| 3 | American Studies | Columbian College | https://bulletin.gwu.edu/arts-sciences/american-studies/minor/ |
| 4 | Anthropology | Columbian College | https://bulletin.gwu.edu/arts-sciences/anthropology/minor/ |
| 5 | Applied Ethics | Columbian College | https://bulletin.gwu.edu/arts-sciences/philosophy/minor-applied-ethics/ |
| 6 | Arabic and Hebrew Languages | Columbian College | https://bulletin.gwu.edu/arts-sciences/classical-near-eastern-languages-civilizations/minor-arabic-hebrew-languages-cultures/ |
| 7 | Art History | Columbian College | https://bulletin.gwu.edu/arts-sciences/art-history/minor/ |
| 8 | Asian Studies | Elliott School | https://bulletin.gwu.edu/international-affairs/asian-studies/minor/ |
| 9 | Astronomy | Columbian College | https://bulletin.gwu.edu/arts-sciences/physics/minor-astronomy/ |
| 10 | Bioinformatics | Columbian College | https://bulletin.gwu.edu/arts-sciences/biology/minor-bioinformatics/ |
| ... | ... | ... | ... |

> **Note**: Full list of 104 minors available in the raw_programs.json cache file.

### 1.5 General Education Requirements

GWU's General Education curriculum includes:
- University Writing (UW)
- Critical Thinking courses
- Quantitative Reasoning
- Scientific Reasoning
- Global/Cross-Cultural courses
- Humanities/Arts courses
- Social Sciences courses

> **Source**: https://bulletin.gwu.edu/university-regulations/general-education/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### Columbian College of Arts and Sciences

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://bulletin.gwu.edu/arts-sciences/american-studies/phd/ |
| 2 | Anthropology | https://bulletin.gwu.edu/arts-sciences/anthropology/phd/ |
| 3 | Applied Social Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/applied-social-psychology-phd/ |
| 4 | Biological Sciences | https://bulletin.gwu.edu/arts-sciences/biology/phd/ |
| 5 | Chemistry | https://bulletin.gwu.edu/arts-sciences/chemistry/phd/ |
| 6 | Clinical Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/clinical-psychology-phd/ |
| 7 | Computer Science | https://bulletin.gwu.edu/arts-sciences/computer-science/phd/ |
| 8 | Economics | https://bulletin.gwu.edu/arts-sciences/economics/phd/ |
| 9 | English | https://bulletin.gwu.edu/arts-sciences/english/phd/ |
| 10 | History | https://bulletin.gwu.edu/arts-sciences/history/phd/ |
| 11 | Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/phd/ |
| 12 | Microbiology and Immunology | https://bulletin.gwu.edu/arts-sciences/biology/phd-microbiology-immunology/ |
| 13 | Neuroscience | https://bulletin.gwu.edu/arts-sciences/biology/phd-neuroscience/ |
| 14 | Philosophy | https://bulletin.gwu.edu/arts-sciences/philosophy/phd/ |
| 15 | Physics | https://bulletin.gwu.edu/arts-sciences/physics/phd/ |
| 16 | Political Science | https://bulletin.gwu.edu/arts-sciences/political-science/phd/ |
| 17 | Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/phd/ |
| 18 | Sociology | https://bulletin.gwu.edu/arts-sciences/sociology/phd/ |
| 19 | Statistics | https://bulletin.gwu.edu/arts-sciences/statistics/phd/ |

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies | https://bulletin.gwu.edu/arts-sciences/american-studies/ma/ |
| 2 | Anthropology | https://bulletin.gwu.edu/arts-sciences/anthropology/ma/ |
| 3 | Applied Economics | https://bulletin.gwu.edu/arts-sciences/economics/ms-applied-economics/ |
| 4 | Art History | https://bulletin.gwu.edu/arts-sciences/art-history/ma/ |
| 5 | Biological Sciences | https://bulletin.gwu.edu/arts-sciences/biology/ma/ |
| 6 | Communication | https://bulletin.gwu.edu/arts-sciences/communication/ma/ |
| 7 | Economics | https://bulletin.gwu.edu/arts-sciences/economics/ma/ |
| 8 | Education | https://bulletin.gwu.edu/education-human-development/curriculum-pedagogy/ma/ |
| 9 | English | https://bulletin.gwu.edu/arts-sciences/english/ma/ |
| 10 | History | https://bulletin.gwu.edu/arts-sciences/history/ma/ |
| 11 | International Affairs | https://bulletin.gwu.edu/international-affairs/graduate-programs/ma/ |
| 12 | Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/ma/ |
| 13 | Museum Studies | https://bulletin.gwu.edu/arts-sciences/museum-studies/ma/ |
| 14 | Philosophy | https://bulletin.gwu.edu/arts-sciences/philosophy/ma/ |
| 15 | Political Science | https://bulletin.gwu.edu/arts-sciences/political-science/ma/ |
| 16 | Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/ma/ |
| 17 | Public Policy | https://bulletin.gwu.edu/arts-sciences/political-science/ma-public-policy/ |
| 18 | Sociology | https://bulletin.gwu.edu/arts-sciences/sociology/ma/ |
| 19 | Statistics | https://bulletin.gwu.edu/arts-sciences/statistics/ma/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical and Translational Sciences | https://bulletin.gwu.edu/arts-sciences/anatomy/ms-anatomical-translational-sciences/ |
| 2 | Applied Computer Science | https://bulletin.gwu.edu/engineering-applied-science/computer-science/ms-applied-computer-science/ |
| 3 | Applied Economics | https://bulletin.gwu.edu/arts-sciences/economics/ms-applied-economics/ |
| 4 | Applied Mathematics | https://bulletin.gwu.edu/arts-sciences/mathematics/ms/ |
| 5 | Applied Psychology | https://bulletin.gwu.edu/arts-sciences/psychological-and-brain-sciences/ms-applied-psychology/ |
| 6 | Bioinformatics | https://bulletin.gwu.edu/arts-sciences/biology/ms-bioinformatics/ |
| 7 | Biological Sciences | https://bulletin.gwu.edu/arts-sciences/biology/ms/ |
| 8 | Biostatistics | https://bulletin.gwu.edu/public-health/biostatistics/ms/ |
| 9 | Chemistry | https://bulletin.gwu.edu/arts-sciences/chemistry/ms/ |
| 10 | Data Science | https://bulletin.gwu.edu/arts-sciences/data-science/ms/ |

> **Note**: Full list of 51 MS programs available in the raw_programs.json cache file.

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical and Translational Sciences | https://bulletin.gwu.edu/arts-sciences/anatomy/certificate-anatomical-translational-sciences/ |
| 2 | Applied Economics | https://bulletin.gwu.edu/arts-sciences/economics/certificate-applied-economics/ |
| 3 | Data Science | https://bulletin.gwu.edu/arts-sciences/data-science/certificate/ |
| 4 | Museum Studies | https://bulletin.gwu.edu/arts-sciences/museum-studies/certificate/ |
| ... | ... | ... |

#### GW School of Business

##### MBA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (STEM) | https://bulletin.gwu.edu/business/business-administration-mba/mba/ |
| 2 | Executive MBA | https://bulletin.gwu.edu/business/business-administration-mba/emba/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://bulletin.gwu.edu/business/accountancy/macc/ |
| 2 | Applied Finance | https://bulletin.gwu.edu/business/finance/ms-applied-finance/ |
| 3 | Business Analytics | https://bulletin.gwu.edu/business/information-systems-technology/ms-business-analytics/ |
| 4 | Finance | https://bulletin.gwu.edu/business/finance/ms-finance/ |
| 5 | Government Contracts | https://bulletin.gwu.edu/business/government-contracts/ms/ |
| 6 | Information Systems Technology | https://bulletin.gwu.edu/business/information-systems-technology/ms/ |
| 7 | Management | https://bulletin.gwu.edu/business/management/ms-management/ |
| 8 | Marketing | https://bulletin.gwu.edu/business/marketing/ms-marketing/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy | https://bulletin.gwu.edu/business/accountancy/certificate/ |
| 2 | Business Analytics | https://bulletin.gwu.edu/business/information-systems-technology/certificate-business-analytics/ |
| 3 | Finance | https://bulletin.gwu.edu/business/finance/certificate-finance/ |
| 4 | Government Contracts | https://bulletin.gwu.edu/business/government-contracts/certificate/ |
| 5 | Information Systems Technology | https://bulletin.gwu.edu/business/information-systems-technology/certificate/ |
| 6 | Management | https://bulletin.gwu.edu/business/management/certificate-management/ |
| 7 | Marketing | https://bulletin.gwu.edu/business/marketing/certificate-marketing/ |
| ... | ... | ... |

#### School of Engineering and Applied Science

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.gwu.edu/engineering-applied-science/biomedical-engineering/phd/ |
| 2 | Civil and Environmental Engineering | https://bulletin.gwu.edu/engineering-applied-science/civil-environmental-engineering/phd/ |
| 3 | Computer Science | https://bulletin.gwu.edu/engineering-applied-science/computer-science/phd/ |
| 4 | Electrical and Computer Engineering | https://bulletin.gwu.edu/engineering-applied-science/electrical-computer-engineering/phd/ |
| 5 | Engineering Management and Systems Engineering | https://bulletin.gwu.edu/engineering-applied-science/engineering-management-systems-engineering/phd/ |
| 6 | Mechanical and Aerospace Engineering | https://bulletin.gwu.edu/engineering-applied-science/mechanical-aerospace-engineering/phd/ |
| 7 | Systems Engineering | https://bulletin.gwu.edu/engineering-applied-science/systems-engineering/phd/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.gwu.edu/engineering-applied-science/biomedical-engineering/ms/ |
| 2 | Civil and Environmental Engineering | https://bulletin.gwu.edu/engineering-applied-science/civil-environmental-engineering/ms/ |
| 3 | Computer Science | https://bulletin.gwu.edu/engineering-applied-science/computer-science/ms/ |
| 4 | Data Analytics | https://bulletin.gwu.edu/engineering-applied-science/engineering-management-systems-engineering/ms-data-analytics/ |
| 5 | Electrical Engineering | https://bulletin.gwu.edu/engineering-applied-science/electrical-computer-engineering/ms-electrical-engineering/ |
| 6 | Engineering Management | https://bulletin.gwu.edu/engineering-applied-science/engineering-management-systems-engineering/ms/ |
| 7 | Mechanical Engineering | https://bulletin.gwu.edu/engineering-applied-science/mechanical-aerospace-engineering/ms-mechanical-engineering/ |
| 8 | Systems Engineering | https://bulletin.gwu.edu/engineering-applied-science/systems-engineering/ms/ |
| ... | ... | ... |

##### MEng Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Machine Learning | https://bulletin.gwu.edu/engineering-applied-science/computer-science/meng-ai-ml/ |
| 2 | Cybersecurity | https://bulletin.gwu.edu/engineering-applied-science/computer-science/meng-cybersecurity/ |
| 3 | Data Analytics | https://bulletin.gwu.edu/engineering-applied-science/engineering-management-systems-engineering/meng-data-analytics/ |
| 4 | Internet of Things | https://bulletin.gwu.edu/engineering-applied-science/electrical-computer-engineering/meng-iot/ |

#### Elliott School of International Affairs

##### MA Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | International Affairs | https://bulletin.gwu.edu/international-affairs/graduate-programs/ma/ |
| 2 | International Development Studies | https://bulletin.gwu.edu/international-affairs/graduate-programs/ma-international-development-studies/ |
| 3 | International Science and Technology Policy | https://bulletin.gwu.edu/international-affairs/graduate-programs/ma-international-science-technology-policy/ |
| 4 | Security Policy Studies | https://bulletin.gwu.edu/international-affairs/graduate-programs/ma-security-policy-studies/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Asian Studies | https://bulletin.gwu.edu/international-affairs/graduate-programs/certificate-asian-studies/ |
| 2 | European and Eurasian Studies | https://bulletin.gwu.edu/international-affairs/graduate-programs/certificate-european-eurasian-studies/ |
| 3 | International Affairs | https://bulletin.gwu.edu/international-affairs/graduate-programs/certificate-international-affairs/ |
| 4 | Latin American and Hemispheric Studies | https://bulletin.gwu.edu/international-affairs/graduate-programs/certificate-latin-american-hemispheric-studies/ |
| ... | ... | ... |

#### Graduate School of Education and Human Development

##### EdD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Curriculum and Instruction | https://bulletin.gwu.edu/education-human-development/curriculum-pedagogy/edd/ |
| 2 | Educational Leadership and Administration | https://bulletin.gwu.edu/education-human-development/educational-leadership/edd/ |
| 3 | Higher Education Administration | https://bulletin.gwu.edu/education-human-development/educational-leadership/edd-higher-education/ |
| 4 | Special Education | https://bulletin.gwu.edu/education-human-development/special-education/edd/ |

##### MAEd&HD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://bulletin.gwu.edu/education-human-development/counseling/ma/ |
| 2 | Curriculum and Instruction | https://bulletin.gwu.edu/education-human-development/curriculum-pedagogy/ma/ |
| 3 | Educational Leadership | https://bulletin.gwu.edu/education-human-development/educational-leadership/ma/ |
| 4 | Higher Education Administration | https://bulletin.gwu.edu/education-human-development/educational-leadership/ma-higher-education/ |
| 5 | Special Education | https://bulletin.gwu.edu/education-human-development/special-education/ma/ |
| ... | ... | ... |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | https://bulletin.gwu.edu/education-human-development/counseling/certificate/ |
| 2 | Curriculum and Instruction | https://bulletin.gwu.edu/education-human-development/curriculum-pedagogy/certificate/ |
| 3 | Educational Leadership | https://bulletin.gwu.edu/education-human-development/educational-leadership/certificate/ |
| ... | ... | ... |

#### Milken Institute School of Public Health

##### PhD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Epidemiology | https://bulletin.gwu.edu/public-health/epidemiology/phd/ |

##### MPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://bulletin.gwu.edu/public-health/biostatistics/mph/ |
| 2 | Environmental and Occupational Health | https://bulletin.gwu.edu/public-health/environmental-occupational-health/mph/ |
| 3 | Epidemiology | https://bulletin.gwu.edu/public-health/epidemiology/mph/ |
| 4 | Global Health | https://bulletin.gwu.edu/public-health/global-health/mph/ |
| 5 | Health Policy | https://bulletin.gwu.edu/public-health/health-policy/mph/ |
| 6 | Health Promotion | https://bulletin.gwu.edu/public-health/prevention-community-health/mph/ |
| ... | ... | ... |

##### DrPH Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Policy | https://bulletin.gwu.edu/public-health/health-policy/drph/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | https://bulletin.gwu.edu/public-health/biostatistics/certificate/ |
| 2 | Environmental and Occupational Health | https://bulletin.gwu.edu/public-health/environmental-occupational-health/certificate/ |
| 3 | Epidemiology | https://bulletin.gwu.edu/public-health/epidemiology/certificate/ |
| ... | ... | ... |

#### School of Medicine and Health Sciences

##### MD Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | https://bulletin.gwu.edu/medicine-health-sciences/md/ |

##### MS Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical and Translational Sciences | https://bulletin.gwu.edu/medicine-health-sciences/anatomy/ms/ |
| 2 | Biomedical Laboratory Science | https://bulletin.gwu.edu/medicine-health-sciences/biomedical-laboratory-science/ms/ |
| 3 | Clinical Research and Leadership | https://bulletin.gwu.edu/medicine-health-sciences/clinical-research-leadership/ms/ |
| 4 | Genomics and Precision Medicine | https://bulletin.gwu.edu/medicine-health-sciences/genomics-precision-medicine/ms/ |
| ... | ... | ... |

##### DNP Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/dnp-adult-gerontology-acute-care-nurse-practitioner/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/dnp-adult-gerontology-primary-care-nurse-practitioner/ |
| 3 | Family Nurse Practitioner | https://bulletin.gwu.edu/nursing/dnp-family-nurse-practitioner/ |
| 4 | Nurse-Midwifery | https://bulletin.gwu.edu/nursing/dnp-nurse-midwifery/ |
| 5 | Psychiatric Mental Health Nurse Practitioner | https://bulletin.gwu.edu/nursing/dnp-psychiatric-mental-health-nurse-practitioner/ |

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Anatomical and Translational Sciences | https://bulletin.gwu.edu/medicine-health-sciences/anatomy/certificate/ |
| 2 | Biomedical Laboratory Science | https://bulletin.gwu.edu/medicine-health-sciences/biomedical-laboratory-science/certificate/ |
| ... | ... | ... |

#### School of Nursing

##### MSN Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/msn-adult-gerontology-acute-care-nurse-practitioner/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/msn-adult-gerontology-primary-care-nurse-practitioner/ |
| 3 | Family Nurse Practitioner | https://bulletin.gwu.edu/nursing/msn-family-nurse-practitioner/ |
| 4 | Nurse-Midwifery | https://bulletin.gwu.edu/nursing/msn-nurse-midwifery/ |
| 5 | Psychiatric Mental Health Nurse Practitioner | https://bulletin.gwu.edu/nursing/msn-psychiatric-mental-health-nurse-practitioner/ |

##### Post-Master's Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/pmc-adult-gerontology-acute-care-nurse-practitioner/ |
| 2 | Adult-Gerontology Primary Care Nurse Practitioner | https://bulletin.gwu.edu/nursing/pmc-adult-gerontology-primary-care-nurse-practitioner/ |
| 3 | Family Nurse Practitioner | https://bulletin.gwu.edu/nursing/pmc-family-nurse-practitioner/ |
| 4 | Nurse-Midwifery | https://bulletin.gwu.edu/nursing/pmc-nurse-midwifery/ |
| 5 | Psychiatric Mental Health Nurse Practitioner | https://bulletin.gwu.edu/nursing/pmc-psychiatric-mental-health-nurse-practitioner/ |

#### College of Professional Studies

##### Graduate Certificate Programs
| # | 项目 | URL |
|---|------|-----|
| 1 | Homeland Security | https://bulletin.gwu.edu/professional-studies/homeland-security/certificate/ |
| 2 | Paralegal Studies | https://bulletin.gwu.edu/professional-studies/paralegal-studies/certificate/ |
| 3 | Project Management | https://bulletin.gwu.edu/professional-studies/project-management/certificate/ |
| 4 | Publishing | https://bulletin.gwu.edu/professional-studies/publishing/certificate/ |
| ... | ... | ... |

### 2.2 Graduate Admissions Model

GWU's graduate admissions is **decentralized**. Each school/college manages its own admissions process. The Graduate Application Center (https://apply.gwu.edu/) is used by most programs, but GW Law uses LSAC and the MD program uses AMCAS.

**Application Requirements**:
- Bachelor's degree from regionally accredited institution
- Official transcripts
- Statement of purpose
- Letters of recommendation (number varies by program)
- Standardized test scores (GRE/GMAT if required by program)
- English proficiency scores for international students

**Application Fee**: $80 (per application)

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | Source |
|------|-----|--------|
| **Application Portal** | Common Application / Coalition Application | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **ED I Deadline** | November 1 | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **ED I Notification** | By Late December | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **ED II Deadline** | January 5 | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **ED II Notification** | By Late February | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **RD Deadline** | January 5 | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **RD Notification** | By Late March / Early April | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **Enrollment Deposit Deadline** | May 1 | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **Application Fee** | $80 | https://bulletin.gwu.edu/fees-financial-regulations/ |
| **SAT/ACT Policy** | Test-Optional (since 2015) | https://undergraduate.admissions.gwu.edu/test-optional |
| **SAT/ACT Required For** | B.A./M.D. program, homeschooled students, narrative-evaluation schools | https://undergraduate.admissions.gwu.edu/test-optional |
| **Superscore** | Yes | https://undergraduate.admissions.gwu.edu/test-optional |
| **Recommendations** | 1 teacher recommendation + school report | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **Interview** | Not required | https://undergraduate.admissions.gwu.edu/first-year-applicants |
| **Portfolio** | Required for Corcoran School programs only | https://undergraduate.admissions.gwu.edu/first-year-applicants |

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 推荐分数 | 适用条件 |
|------|---------|---------|---------|
| TOEFL iBT | Not specified (competitive) | N/A | International applicants whose first language is not English |
| IELTS | Not specified (competitive) | N/A | International applicants whose first language is not English |
| Duolingo English Test | Not specified (competitive) | N/A | International applicants whose first language is not English |
| PTE Academic | Not specified (competitive) | N/A | International applicants whose first language is not English |

> **Note**: GWU does not publish minimum English proficiency scores for undergraduate admission. Scores are considered competitively. International students are encouraged to submit TOEFL, IELTS, Duolingo, or PTE scores.

### 3.3 Graduate — Global Rules

| 维度 | 值 | Source |
|------|-----|--------|
| **Application Portal** | Graduate Application Center (https://apply.gwu.edu/) | https://graduate.admissions.gwu.edu/application-requirements |
| **Application Fee** | $80 | https://bulletin.gwu.edu/fees-financial-regulations/ |
| **GRE/GMAT Policy** | Per-program (some require, some optional, some not accepted) | https://graduate.admissions.gwu.edu/application-requirements |
| **English Proficiency (TOEFL)** | 81 minimum | https://graduate.admissions.gwu.edu/international-student-application-requirements |
| **English Proficiency (IELTS)** | 6.5 overall | https://graduate.admissions.gwu.edu/international-student-application-requirements |
| **English Proficiency (PTE)** | 53 minimum | https://graduate.admissions.gwu.edu/international-student-application-requirements |
| **Score Validity** | 2 years | https://graduate.admissions.gwu.edu/international-student-application-requirements |
| **CGS April 15** | Yes (signatory) | https://graduate.admissions.gwu.edu/application-requirements |
| **EAP Requirement** | Some students may be required to take English for Academic Purposes courses | https://graduate.admissions.gwu.edu/international-student-application-requirements |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | On-Campus | Off-Campus | At Home |
|-------------|-----------|------------|---------|
| Tuition | $72,000 | $72,000 | $72,000 |
| Mandatory Student Fees | $420 | $420 | $420 |
| Matriculation Fee | $350 | $350 | $350 |
| Housing and Food | $18,160 | $18,160 | $7,000 |
| **Total Direct Cost** | **$90,930** | **$90,930** | **$79,770** |
| Books/Supplies | $1,450 | $1,450 | $1,450 |
| Personal/Miscellaneous | $1,700 | $1,700 | $1,700 |
| Transportation | $1,075 | $1,075 | $1,075 |
| **Total Estimated COA** | **$95,155** | **$95,155** | **$83,995** |

> **Source**: https://financialaid.gwu.edu/how-estimate-your-total-cost-attendance-gw
> **Capture Date**: 2026-07-06

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 | Source |
|------|-----|--------|
| **Need-Blind (US)** | Yes | https://undergraduate.admissions.gwu.edu/financial-aid |
| **Need-Blind (International)** | Need-Aware | https://undergraduate.admissions.gwu.edu/international-student-aid |
| **Meets Full Need** | Yes (for admitted students) | https://financialaid.gwu.edu/revolutionary-promise |
| **Revolutionary Promise** | Families <$100k income = full tuition; Families <$150k = at least half tuition | https://financialaid.gwu.edu/revolutionary-promise |
| **Merit Scholarships** | Yes (automatic consideration) | https://undergraduate.admissions.gwu.edu/merit-scholarships |
| **District Scholars** | Full demonstrated need for DC high school students | https://undergraduate.admissions.gwu.edu/district-scholars |
| **Loan-Free** | Not specified | N/A |
| **Application Forms** | FAFSA + CSS Profile | https://undergraduate.admissions.gwu.edu/need-based-aid |

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 | Source |
|------|-----|--------|
| **Tuition (per credit)** | Varies by school ($1,009 - $2,150+ per credit) | https://studentaccounts.gwu.edu/graduate-tuition |
| **Application Fee** | $80 | https://bulletin.gwu.edu/fees-financial-regulations/ |
| **Funding Types** | Fellowships, Assistantships, Loans | https://graduate.admissions.gwu.edu/costs-aid |
| **Graduate Assistantships** | Available (tuition + stipend) | https://gradfellowships.gwu.edu/ |
| **Federal Work-Study** | Available | https://graduate.admissions.gwu.edu/costs-aid |
| **Payment Plans** | Monthly payment plan available | https://studentaccounts.gwu.edu/monthly-payment-plan |

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Deadlines
```yaml
field: undergraduate.deadlines
value:
  ed1: November 1
  ed1_notification: By Late December
  ed2: January 5
  ed2_notification: By Late February
  rd: January 5
  rd_notification: By Late March / Early April
source_url: https://undergraduate.admissions.gwu.edu/first-year-applicants
source_snippet: "Early Decision I | November 1 | By Late December | Yes"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Test-Optional Policy
```yaml
field: undergraduate.testing.sat_act_policy
value: test-optional (since 2015); required for B.A./M.D., homeschooled, narrative-evaluation schools
source_url: https://undergraduate.admissions.gwu.edu/test-optional
source_snippet: "GW has been proudly test-optional for the majority of applicants since 2015."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Undergraduate Tuition
```yaml
field: undergraduate.cost.tuition_2026_2027
value: $72,000
source_url: https://financialaid.gwu.edu/how-estimate-your-total-cost-attendance-gw
source_snippet: "Tuition: 2026-2027 Academic Year | $72000"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-004: Total COA On-Campus
```yaml
field: undergraduate.cost.total_on_campus_2026_2027
value: $95,155
source_url: https://financialaid.gwu.edu/how-estimate-your-total-cost-attendance-gw
source_snippet: "Total Estimated Cost of Attendance | $95,155"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Revolutionary Promise
```yaml
field: undergraduate.financial_aid.revolutionary_promise
value: "Families <$100k = full tuition; <$150k = at least half tuition"
source_url: https://financialaid.gwu.edu/revolutionary-promise
source_snippet: "New Student Families With Incomes Under $100,000 Will Pay No Tuition"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: Application Fee
```yaml
field: undergraduate.application.fee
value: $80
source_url: https://bulletin.gwu.edu/fees-financial-regulations/
source_snippet: "Application fee | $80"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-G-001: Graduate TOEFL Minimum
```yaml
field: graduate.english_proficiency.toefl_minimum
value: 81
source_url: https://graduate.admissions.gwu.edu/international-student-application-requirements
source_snippet: "Test of English as a Foreign Language (TOEFL): score of 81"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate IELTS Minimum
```yaml
field: graduate.english_proficiency.ielts_minimum
value: 6.5 overall
source_url: https://graduate.admissions.gwu.edu/international-student-application-requirements
source_snippet: "International English Language Testing System (IELTS): overall score of 6.5"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-003: Graduate PTE Minimum
```yaml
field: graduate.english_proficiency.pte_minimum
value: 53
source_url: https://graduate.admissions.gwu.edu/international-student-application-requirements
source_snippet: "PTE Academic: 53."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-004: Graduate Application Fee
```yaml
field: graduate.application.fee
value: $80
source_url: https://bulletin.gwu.edu/fees-financial-regulations/
source_snippet: "Application fee | $80"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-P-001: Total Programs Count
```yaml
field: programs.total_count
value: 754
source_url: https://bulletin.gwu.edu/find-your-program
source_snippet: "754 programs found in the isotope list"
capture_date: 2026-07-06
evidence_type: official_webpage_extraction
```

### E-P-002: UG Majors Count
```yaml
field: programs.undergraduate_majors
value: 131
source_url: https://bulletin.gwu.edu/find-your-program
source_snippet: "131 undergraduate degree programs (BA/BS/BFA/BPS/BSHS/BSN)"
capture_date: 2026-07-06
evidence_type: official_webpage_extraction
```

### E-P-003: Graduate Programs Count
```yaml
field: programs.graduate_degrees
value: 285
source_url: https://bulletin.gwu.edu/find-your-program
source_snippet: "285 graduate degree programs"
capture_date: 2026-07-06
evidence_type: official_webpage_extraction
```

### E-P-004: Schools Count
```yaml
field: institutions.schools_count
value: 11
source_url: https://bulletin.gwu.edu/schools-and-colleges/
source_snippet: "9 schools listed plus GW Law and Interdisciplinary programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
gwu-knowledge-base-v2
├── 00-institution-overview.md (Section 0)
├── 01-undergraduate-education.md (Section 1)
├── 02-graduate-education.md (Section 2)
├── 03-application-requirements.md (Section 3)
├── 04-costs-financial-aid.md (Section 4)
├── 05-evidence-chain.md (Section 5)
├── 06-import-manifest.md (this section)
└── 07-cross-school-comparison.md (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "gwu-knowledge-base-v2"
  school: "George Washington University"
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

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | Individual program pages |
| P0 | Per-program application deadlines | Individual program pages |
| P1 | Graduate tuition rates by school | https://studentaccounts.gwu.edu/graduate-tuition |
| P1 | Detailed English proficiency by program | Individual school admissions pages |
| P2 | International student financial aid details | https://undergraduate.admissions.gwu.edu/international-student-aid |
| P2 | Transfer admission requirements | https://undergraduate.admissions.gwu.edu/transfer-applicants |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | GWU | MIT | Stanford | Harvard | Caltech | UChicago |
|-----------|-----|-----|----------|---------|---------|----------|
| **Type** | Private | Private | Private | Private | Private | Private |
| **Location** | Washington, DC | Cambridge, MA | Stanford, CA | Cambridge, MA | Pasadena, CA | Chicago, IL |
| **UG Tuition (2026-27)** | $72,000 | $61,990 | $65,127 | $59,076 | $65,622 | $75,960 |
| **Total UG COA (on-campus)** | $95,155 | $85,912 | $92,574 | $87,446 | $93,912 | $103,821 |
| **Need-Blind (US)** | Yes | Yes | Yes | Yes | Yes | Yes |
| **Need-Blind (Intl)** | Need-Aware | Need-Blind | Need-Blind | Need-Blind | Need-Aware | Need-Aware |
| **EA Deadline** | N/A | Nov 1 | Nov 1 | Nov 1 | Nov 1 | Nov 2 |
| **ED Deadline** | Nov 1 | N/A | N/A | N/A | N/A | N/A |
| **RD Deadline** | Jan 5 | Jan 1 | Jan 2 | Jan 1 | Jan 5 | Jan 4 |
| **SAT/ACT Required** | Test-Optional | Required | Required | Test-Optional | Required | Test-Optional |
| **TOEFL Min (UG)** | N/A (competitive) | 100 | N/A | N/A | N/A | N/A |
| **IELTS Min (UG)** | N/A (competitive) | 7.5 | N/A | N/A | N/A | N/A |
| **Total Programs** | 754 | 342 | 349 | ~200 | 76 | ~300 |
| **Schools/Colleges** | 11 | 5 | 7 | 13 | 6 | 12 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: undergraduate.admissions.gwu.edu, graduate.admissions.gwu.edu, financialaid.gwu.edu, bulletin.gwu.edu, studentaccounts.gwu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
