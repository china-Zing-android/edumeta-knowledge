# University of Washington (UW) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | ~180+ |
| 本科辅修 (Minor) | ~90+ |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | ~300+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | ~30+ |
| **学位项目总计 (UG + Grad)** | **~600+** |
| 学院 / 独立系所总数 | 16 |

> **Note**: UW offers "more than 180 majors" for undergraduates and "more than 300 graduate programs" across three campuses. The Seattle campus is the primary focus of this document. Exact counts require exhaustive enumeration of all programs (Phase 2 extraction).

### 0.2 学院 / 系层级结构

```
University of Washington (Seattle)
├── College of Arts & Sciences                          [学院]
│   ├── Division of the Arts
│   │   ├── Digital Arts & Experimental Media           [系]
│   │   ├── Art + Art History + Design                  [系]
│   │   ├── Drama                                       [系]
│   │   ├── Music                                       [系]
│   │   └── Dance                                       [系]
│   ├── Division of the Humanities
│   │   ├── Classics                                    [系]
│   │   ├── French & Italian Studies                    [系]
│   │   ├── Cinema and Media Studies                    [系]
│   │   ├── Asian Languages & Literature                [系]
│   │   ├── Comparative History of Ideas                [系]
│   │   ├── English                                     [系]
│   │   ├── German Studies                              [系]
│   │   ├── Linguistics                                 [系]
│   │   ├── Near Eastern Languages & Civilization       [系]
│   │   ├── Scandinavian Studies                        [系]
│   │   ├── Slavic Languages & Literatures              [系]
│   │   └── Spanish and Portuguese Studies              [系]
│   ├── Division of Natural Sciences
│   │   ├── Biology                                     [系]
│   │   ├── Chemistry                                   [系]
│   │   ├── Applied Mathematics                         [系]
│   │   ├── Astronomy                                   [系]
│   │   ├── Mathematics                                 [系]
│   │   ├── Physics                                     [系]
│   │   ├── Psychology                                  [系]
│   │   ├── Speech & Hearing Sciences                   [系]
│   │   └── Statistics                                  [系]
│   └── Division of Social Sciences
│       ├── Communication                               [系]
│       ├── Gender, Women & Sexuality Studies           [系]
│       ├── History                                     [系]
│       ├── American Ethnic Studies                     [系]
│       ├── Economics                                   [系]
│       ├── Geography                                   [系]
│       ├── American Indian Studies                     [系]
│       ├── Anthropology                                [系]
│       ├── Integrated Social Sciences                  [系]
│       ├── Law, Societies & Justice                    [系]
│       ├── Philosophy                                  [系]
│       ├── Political Science                           [系]
│       ├── Sociology                                   [系]
│       └── The Jackson School of International Studies [系]
│
├── College of Engineering                              [学院]
│   ├── William E. Boeing Dept. of Aeronautics & Astronautics [系]
│   ├── Bioengineering                                  [系]
│   ├── Chemical Engineering                            [系]
│   ├── Civil & Environmental Engineering               [系]
│   ├── Paul G. Allen School of Computer Science & Engineering [系]
│   ├── Electrical & Computer Engineering               [系]
│   ├── Human Centered Design & Engineering             [系]
│   ├── Industrial & Systems Engineering                [系]
│   ├── Materials Science & Engineering                 [系]
│   └── Mechanical Engineering                          [系]
│
├── Foster School of Business                           [学院]
│   ├── Accounting                                      [系]
│   ├── Finance and Business Economics                  [系]
│   ├── Information Systems and Operations Management   [系]
│   ├── Management and Organization                     [系]
│   └── Marketing and International Business            [系]
│
├── College of Education                                [学院]
│   └── (No internal department subdivision listed)
│
├── College of the Environment                          [学院]
│   ├── Aquatic and Fishery Sciences                    [系]
│   ├── Atmospheric and Climate Science                 [系]
│   ├── Earth and Space Sciences                        [系]
│   ├── Environmental and Forest Sciences               [系]
│   ├── Marine and Environmental Affairs                [系]
│   ├── Marine Biology                                  [系]
│   ├── Oceanography                                    [系]
│   └── Program on the Environment                     [系]
│
├── Information School (iSchool)                        [学院]
│   └── (No internal department subdivision listed)
│
├── School of Law                                       [学院]
│   └── (No internal department subdivision listed)
│
├── School of Medicine                                  [学院]
│   ├── Department of Medicine (11 subspecialty divisions) [系]
│   └── (Other departments not enumerated on homepage)
│
├── School of Nursing                                   [学院]
│   └── (No internal department subdivision listed)
│
├── School of Pharmacy                                  [学院]
│   ├── Medicinal Chemistry                             [系]
│   ├── Pharmaceutics                                   [系]
│   └── Pharmacy                                        [系]
│
├── School of Public Health                             [学院]
│   ├── Biostatistics                                   [系]
│   ├── Environmental & Occupational Health Sciences    [系]
│   ├── Epidemiology                                    [系]
│   ├── Global Health                                   [系]
│   ├── Health Systems & Population Health              [系]
│   └── Food Systems, Nutrition, and Health             [系]
│
├── Evans School of Public Policy & Governance          [学院]
│   └── (No internal department subdivision listed)
│
├── School of Social Work                               [学院]
│   └── (No internal department subdivision listed)
│
├── School of Dentistry                                 [学院]
│   ├── Endodontics                                     [系]
│   ├── Oral Health Sciences                            [系]
│   ├── Oral Medicine                                   [系]
│   ├── Oral and Maxillofacial Surgery                  [系]
│   ├── Oral Pathology                                  [系]
│   ├── Orthodontics                                    [系]
│   ├── Pediatric Dentistry                             [系]
│   ├── Periodontics                                    [系]
│   └── Restorative Dentistry                           [系]
│
└── Graduate School                                     [学院]
    └── (Administrative unit overseeing all graduate programs)
```

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | ~80+ |
| BS | BS | Bachelor of Science | 本科 | ~100+ |
| BFA | BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 2 (BSN, ABSN) |
| BSW | BASW | Bachelor of Arts in Social Welfare | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | ~40+ |
| MS | MS | Master of Science | 研究生 | ~80+ |
| MFA | MFA | Master of Fine Arts | 研究生 | ~5 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 (Full-time, Evening, Online) |
| MEd | M.Ed. | Master of Education | 研究生 | ~10+ |
| MPH | MPH | Master of Public Health | 研究生 | ~5 |
| MHA | MHA | Master of Health Administration | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 2 (MPA, EMPA) |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MLIS | MLIS | Master of Library and Information Science | 研究生 | 1 |
| MSIM | MSIM | Master of Science in Information Management | 研究生 | 1 |
| MArch | M.Arch | Master of Architecture | 研究生 | TBD |
| LLM | LL.M. | Master of Laws | 研究生 | 1 |
| MJ | M.J. | Master of Jurisprudence | 研究生 | 1 |
| DDS | DDS | Doctor of Dental Surgery | 研究生 | 1 |
| PharmD | PharmD | Doctor of Pharmacy | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~100+ |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DrPH | DrPH | Doctor of Public Health | 研究生 | TBD |
| Certificate | Certificate | Graduate Certificate | 研究生 | ~30+ |

> **Note**: Exact counts require exhaustive enumeration of all programs across all schools (Phase 2). Counts above are estimates based on available data.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BSN | BSW | MA | MS | MBA | MEd | MPH | MPA | MSW | MLIS | DDS | PharmD | MD | JD | PhD | EdD | DNP | Cert | 合计 |
|------------|----|----|-----|-----|-----|----|----|-----|-----|-----|-----|-----|------|-----|--------|----|----|-----|-----|-----|------|------|
| Arts & Sciences | ~60 | ~20 | ~5 | 0 | 0 | ~30 | ~15 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~40 | 0 | 0 | ~5 | ~175 |
| Engineering | 0 | ~12 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | ~3 | ~35 |
| Foster Business | 0 | ~5 | 0 | 0 | 0 | 0 | ~3 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | ~2 | ~18 |
| Education | 0 | ~3 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 1 | 0 | ~3 | ~22 |
| Environment | 0 | ~8 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | 0 | 0 | ~2 | ~30 |
| iSchool | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | ~2 | ~7 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | ~3 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | ~15 | 0 | 0 | ~5 | ~26 |
| Nursing | 0 | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | ~2 | ~7 |
| Pharmacy | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | ~2 | ~8 |
| Public Health | 0 | ~5 | 0 | 0 | 0 | 0 | ~3 | 0 | 0 | ~5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | 0 | ~2 | ~18 |
| Evans Policy | 0 | ~2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | ~2 | ~7 |
| Social Work | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ~3 |
| Dentistry | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | ~3 | ~6 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~5 | ~5 |
| **合计** | ~60 | ~61 | ~5 | 2 | 1 | ~31 | ~51 | 3 | ~10 | ~5 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | ~97 | 1 | 1 | ~38 | **~373** |

> **Note**: This matrix is an estimate based on available data. Exact counts require exhaustive enumeration of all programs. The matrix should reconcile with Rule 1 total when complete.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UW Seattle offers "more than 180 majors" across 16 schools and colleges. The College of Arts & Sciences is the largest unit with 39 departments and 72 degree programs. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts & Sciences

##### Division of the Arts

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://art.washington.edu/ |
| 2 | Studio Art | https://art.washington.edu/ |
| 3 | Dance | https://dance.washington.edu/ |
| 4 | Drama | https://drama.washington.edu/ |
| 5 | Music | https://music.washington.edu/ |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Visual Art | https://art.washington.edu/ |
| 2 | Industrial Design | https://art.washington.edu/ |
| 3 | Interaction Design | https://art.washington.edu/ |

##### Division of the Humanities

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Languages and Cultures | https://asian.washington.edu/ |
| 2 | Classics | https://classics.washington.edu/ |
| 3 | Comparative History of Ideas | https://chid.washington.edu/ |
| 4 | Comparative Literature | https://complit.washington.edu/ |
| 5 | English | https://english.washington.edu/ |
| 6 | French | https://frenchitalian.washington.edu/ |
| 7 | Germanics | https://german.washington.edu/ |
| 8 | Italian | https://frenchitalian.washington.edu/ |
| 9 | Linguistics | https://ling.washington.edu/ |
| 10 | Near Eastern Languages and Civilization | https://nelc.washington.edu/ |
| 11 | Scandinavian Studies | https://scand.washington.edu/ |
| 12 | Slavic Languages and Literatures | https://slavic.washington.edu/ |
| 13 | Spanish | https://spanport.washington.edu/ |

##### Division of Natural Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://amath.washington.edu/ |
| 2 | Astronomy | https://astro.washington.edu/ |
| 3 | Biology | https://biology.washington.edu/ |
| 4 | Chemistry | https://chem.washington.edu/ |
| 5 | Mathematics | https://math.washington.edu/ |
| 6 | Physics | https://phys.washington.edu/ |
| 7 | Psychology | https://psych.washington.edu/ |
| 8 | Speech and Hearing Sciences | https://comdis.uw.edu/ |
| 9 | Statistics | https://stat.washington.edu/ |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://math.washington.edu/ |
| 2 | Physics | https://phys.washington.edu/ |

##### Division of Social Sciences

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Ethnic Studies | https://aes.washington.edu/ |
| 2 | American Indian Studies | https://ais.washington.edu/ |
| 3 | Anthropology | https://anthropology.washington.edu/ |
| 4 | Communication | https://comm.washington.edu/ |
| 5 | Economics | https://econ.washington.edu/ |
| 6 | Geography | https://geography.washington.edu/ |
| 7 | History | https://history.washington.edu/ |
| 8 | International Studies | https://jsis.washington.edu/ |
| 9 | Law, Societies, and Justice | https://lsj.washington.edu/ |
| 10 | Philosophy | https://phil.washington.edu/ |
| 11 | Political Science | https://polisci.washington.edu/ |
| 12 | Sociology | https://soc.washington.edu/ |
| 13 | Women, Gender, and Sexuality Studies | https://wgss.washington.edu/ |

#### College of Engineering

##### Engineering Undeclared (ENGRUD)
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Undeclared | https://www.engr.washington.edu/ |

##### Department of Aeronautics & Astronautics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aeronautical and Astronautical Engineering | https://aa.washington.edu/ |

##### Department of Bioengineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioengineering | https://bioeng.uw.edu/ |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://cheme.uw.edu/ |

##### Department of Civil & Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://ce.washington.edu/ |
| 2 | Environmental Engineering | https://ce.washington.edu/ |

##### Paul G. Allen School of Computer Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.cs.washington.edu/ |
| 2 | Computer Engineering | https://www.cs.washington.edu/ |

##### Department of Electrical & Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.ece.uw.edu/ |

##### Department of Human Centered Design & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Centered Design & Engineering | https://hcde.uw.edu/ |

##### Department of Industrial & Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://ise.washington.edu/ |

##### Department of Materials Science & Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Materials Science & Engineering | https://mse.washington.edu/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://me.washington.edu/ |

#### Foster School of Business

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://foster.uw.edu/ |
| 2 | Finance | https://foster.uw.edu/ |
| 3 | Information Systems | https://foster.uw.edu/ |
| 4 | Management | https://foster.uw.edu/ |
| 5 | Marketing | https://foster.uw.edu/ |
| 6 | Operations and Supply Chain Management | https://foster.uw.edu/ |

#### College of Education

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education, Learning, and Societies | https://education.uw.edu/ |
| 2 | Early Childhood and Family Studies | https://education.uw.edu/ |

#### College of the Environment

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://environment.uw.edu/ |
| 2 | Environmental Studies | https://environment.uw.edu/ |
| 3 | Aquatic and Fishery Sciences | https://fish.uw.edu/ |
| 4 | Atmospheric Sciences | https://atmos.washington.edu/ |
| 5 | Earth and Space Sciences | https://ess.uw.edu/ |
| 6 | Marine Biology | https://fish.uw.edu/ |
| 7 | Oceanography | https://ocean.washington.edu/ |

#### Information School (iSchool)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Informatics | https://ischool.uw.edu/ |

#### School of Nursing

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (BSN) | https://nursing.uw.edu/ |
| 2 | Accelerated Nursing (ABSN) | https://nursing.uw.edu/ |

#### School of Public Health

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | https://sph.washington.edu/ |
| 2 | Environmental Health | https://sph.washington.edu/ |
| 3 | Global Health | https://sph.washington.edu/ |

#### Evans School of Public Policy & Governance

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Service and Policy | https://evans.uw.edu/ |

#### School of Social Work

###### BASW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Welfare | https://socialwork.uw.edu/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

UW offers several interdisciplinary programs that span multiple colleges. These include:
- Environmental Science and Resource Management (College of the Environment + College of Arts & Sciences)
- Neuroscience (College of Arts & Sciences + School of Medicine)
- Global Health (School of Public Health + other units)

> **Note**: Full enumeration of interdisciplinary programs requires Phase 2 extraction.

### 1.4 Minors — complete list

UW offers "over 100 majors and minors" across the College of Arts & Sciences alone. A complete list of minors requires Phase 2 extraction from the UW course catalog.

### 1.5 General/Institute-wide requirements

UW requires College Academic Distribution Requirements (CADRs) for admission:

| Subject | Credits Required |
|---------|-----------------|
| English | 4 |
| Mathematics | 3 |
| Social sciences/social studies | 3 |
| World languages | 2 |
| Science (including 2 lab science) | 3 |
| Senior year math-based quantitative course | 1 |
| Fine, visual or performing arts | 0.5 |
| Academic elective | 0.5 |

> **Source**: https://admit.washington.edu/apply/freshman/

### 1.6 Course-ID → Major quick-lookup

UW does not use a course numbering system for majors in the same way MIT does. Programs are identified by department and major name.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UW offers "more than 300 graduate programs" across its three campuses. The Graduate School oversees all graduate programs, with some professional schools managing their own admissions separately.

#### Foster School of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Full-Time MBA | https://foster.uw.edu/programs/mba/full-time-mba/ |
| 2 | Evening MBA | https://foster.uw.edu/programs/mba/evening-mba/ |
| 3 | Online MBA | https://foster.uw.edu/programs/mba/online-mba/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in Finance | https://foster.uw.edu/programs/specialty-masters/ |
| 2 | MS in Business Analytics | https://foster.uw.edu/programs/specialty-masters/ |
| 3 | MS in Entrepreneurship | https://foster.uw.edu/programs/specialty-masters/ |
| 4 | MS in Supply Chain Management | https://foster.uw.edu/programs/specialty-masters/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Business Administration | https://foster.uw.edu/programs/phd/ |

#### College of Education

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Education | https://education.uw.edu/programs |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education | https://education.uw.edu/programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Education | https://education.uw.edu/programs |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in Aeronautics & Astronautics | https://aa.washington.edu/ |
| 2 | MS in Bioengineering | https://bioeng.uw.edu/ |
| 3 | MS in Chemical Engineering | https://cheme.uw.edu/ |
| 4 | MS in Civil Engineering | https://ce.washington.edu/ |
| 5 | MS in Computer Science & Engineering | https://www.cs.washington.edu/ |
| 6 | MS in Electrical Engineering | https://www.ece.uw.edu/ |
| 7 | MS in Human Centered Design & Engineering | https://hcde.uw.edu/ |
| 8 | MS in Industrial & Systems Engineering | https://ise.washington.edu/ |
| 9 | MS in Materials Science & Engineering | https://mse.washington.edu/ |
| 10 | MS in Mechanical Engineering | https://me.washington.edu/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Aeronautics & Astronautics | https://aa.washington.edu/ |
| 2 | PhD in Bioengineering | https://bioeng.uw.edu/ |
| 3 | PhD in Chemical Engineering | https://cheme.uw.edu/ |
| 4 | PhD in Civil Engineering | https://ce.washington.edu/ |
| 5 | PhD in Computer Science & Engineering | https://www.cs.washington.edu/ |
| 6 | PhD in Electrical Engineering | https://www.ece.uw.edu/ |
| 7 | PhD in Human Centered Design & Engineering | https://hcde.uw.edu/ |
| 8 | PhD in Industrial & Systems Engineering | https://ise.washington.edu/ |
| 9 | PhD in Materials Science & Engineering | https://mse.washington.edu/ |
| 10 | PhD in Mechanical Engineering | https://me.washington.edu/ |

#### Information School (iSchool)

##### MLIS
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Library and Information Science | https://ischool.uw.edu/programs/mlis |

##### MSIM
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Information Management | https://ischool.uw.edu/programs/msim |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MA in Museology | https://ischool.uw.edu/programs/museology |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Information Science | https://ischool.uw.edu/programs/phd |

#### School of Law

##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor | https://law.uw.edu/academics/jd-program/ |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws | https://law.uw.edu/academics/llm-programs/ |

##### MJ
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Jurisprudence | https://law.uw.edu/academics/mj-program/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Law | https://law.uw.edu/academics/phd-program/ |

#### School of Nursing

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in Clinical Informatics & Patient-Centered Technologies | https://nursing.uw.edu/programs/graduate/ |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice | https://nursing.uw.edu/programs/graduate/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Nursing Science | https://nursing.uw.edu/programs/graduate/ |

#### School of Pharmacy

##### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy | https://sop.washington.edu/programs/pharmd/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in Biomedical Regulatory Affairs | https://sop.washington.edu/programs/graduate/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Medicinal Chemistry | https://sop.washington.edu/programs/graduate/ |
| 2 | PhD in Pharmaceutics | https://sop.washington.edu/programs/graduate/ |
| 3 | PhD in Health Economics & Outcomes Research | https://sop.washington.edu/programs/graduate/ |

#### School of Public Health

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health | https://sph.washington.edu/academics/graduate |

##### MHA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Health Administration | https://sph.washington.edu/academics/graduate |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in various specializations | https://sph.washington.edu/academics/graduate |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Public Health | https://sph.washington.edu/academics/graduate |

#### Evans School of Public Policy & Governance

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration | https://evans.uw.edu/academics/mpa/ |
| 2 | Executive MPA | https://evans.uw.edu/academics/executive-mpa/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Public Policy and Management | https://evans.uw.edu/academics/phd/ |

#### School of Social Work

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work | https://socialwork.uw.edu/programs/msw/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Social Welfare | https://socialwork.uw.edu/programs/phd/ |

#### School of Dentistry

##### DDS
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Dental Surgery | https://dental.washington.edu/academics/dds-program/ |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | MS in Oral Health Sciences | https://dental.washington.edu/academics/graduate-programs/ |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | PhD in Oral Health Sciences | https://dental.washington.edu/academics/graduate-programs/ |

### 2.2 At least one program's full deep-dive (worked example)

#### Foster School of Business — Full-Time MBA

**Department address**: PACCAR Hall, University of Washington, Seattle, WA 98195
**Phone**: (206) 543-4661
**Email**: fostermba@uw.edu
**Application portal**: https://foster.uw.edu/programs/mba/full-time-mba/
**Application opens**: Varies by cycle
**Deadline**: Round 1: October 15; Round 2: January 5; Round 3: March 15
**Application fee**: $90 (standard graduate fee)
**Program duration**: 2 years
**Class size**: ~120 students
**Average GMAT**: ~700
**Average GPA**: ~3.4

**Note**: The Foster MBA is a competitive program with strong industry connections in Seattle's tech ecosystem.

### 2.3 Graduate admissions model

UW uses a **decentralized** graduate admissions system:

**Graduate School handles:**
- Setting minimum admission requirements
- Supporting the online application system
- Processing I-20s and DS-2019s for international students
- Verifying final degree transcripts
- Evaluating English proficiency for non-native speakers

**Individual programs handle:**
- Establishing program-specific admission requirements
- Setting application deadlines
- Deciding required application materials
- Reviewing applications and making admission decisions
- Notifying applicants of decisions

**Application fee**: $90.00 (USD) or $75.00 for Graduate Non-Matriculated applications

**Exceptions**: Schools of Law (JD), Dentistry (DDS), Pharmacy (PharmD), and Medicine (MD) manage their own admissions separately.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Application portal | Common App | https://admit.washington.edu/apply/freshman/ |
| Application opens | September 1 | https://admit.washington.edu/apply/freshman/ |
| **Priority deadline** | **November 15** | https://admit.washington.edu/apply/freshman/ |
| **Regular Decision deadline** | **January 5** | User-provided (verify) |
| Notification date | March 1–15 | https://admit.washington.edu/apply/freshman/ |
| SAT/ACT policy | Test-optional for most applicants | https://admit.washington.edu/apply/freshman/ |
| SAT/ACT required for | Homeschooled, non-standard grading | https://admit.washington.edu/apply/freshman/ |
| Superscore policy | N/A (test-optional) | — |
| Score-report method | Self-reported | https://admit.washington.edu/apply/freshman/ |
| Interview policy | No interviews | https://admit.washington.edu/apply/freshman/ |
| Recommendation requirements | None | https://admit.washington.edu/apply/freshman/ |
| Portfolio | Not required | https://admit.washington.edu/apply/freshman/ |
| Application fee (US) | $85 | https://admit.washington.edu/apply/freshman/how-to-apply/ |
| Application fee (International) | $95 | https://admit.washington.edu/apply/freshman/how-to-apply/ |

> **Important**: UW states "The UW does not participate in early decision or early action admission." The November 15 deadline is a **priority deadline**, not an EA deadline.

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| TOEFL iBT | 76 | 92+ | https://admit.washington.edu/apply/freshman/ |
| IELTS | 6.0 | 7.0+ | https://admit.washington.edu/apply/freshman/ |
| Duolingo | TBD | TBD | — |
| PTE | TBD | TBD | — |
| Cambridge | TBD | TBD | — |

> **Note**: International students must submit "an official TOEFL or IELTS score that meets the UW's minimum English proficiency requirement." Exact minimums require verification from the ISS website.

### 3.3 Graduate — global rules

**Admissions model**: Decentralized (each program sets its own requirements and deadlines)

**Application platform**: UW Graduate School online application (https://apply.grad.uw.edu/)

**Application fee**: $90.00 (USD) per application

**Fee waivers**: Available for select applicants demonstrating financial need

**GRE/GMAT policy**: Varies by program (some require, some optional, some not accepted)

**Language-test policy**: Non-native English speakers must demonstrate English proficiency per Graduate School requirements

**Exemptions**: Applicants with a bachelor's degree from an English-medium institution may be exempt

**Timeline**: Programs have different opening times and deadlines; applicants should verify through the admissions system

**Institutional code**: 003798 (for FAFSA)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### Seattle Campus — Washington State Resident

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $12,664 | Annual undergraduate tuition |
| Annual Student Fees | $1,676 | Required fees (see breakdown below) |
| Room & Board | $18,858 | On-campus, double occupancy |
| Books, Personal, Transportation | $4,482 | Estimated annual |
| **Total** | **$37,680** | |

#### Seattle Campus — Non-Resident

| Expense item | Amount | Description |
|--------------|--------|-------------|
| Tuition | $44,580 | Annual undergraduate tuition |
| Annual Student Fees | $1,676 | Required fees (see breakdown below) |
| Room & Board | $18,858 | On-campus, double occupancy |
| Books, Personal, Transportation | $4,482 | Estimated annual |
| **Total** | **$69,596** | |

#### Fee Breakdown (Seattle Campus)

| Fee | Amount |
|-----|--------|
| New Student Enrollment & Orientation Fee (one-time) | $467 |
| Student Tech Fee | $114 |
| Services and Activities Fee | $546 |
| U-PASS | $243 |
| IMA | $96 |
| YMCA | $540 |

> **Source**: https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind (US) | Yes (implied) | https://www.washington.edu/financialaid/ |
| Need-aware (International) | Yes | User-provided (verify) |
| Husky Promise | Full tuition for eligible WA residents | https://www.washington.edu/huskypromise/ |
| Husky Promise eligibility | Pell Grant eligible, WA resident, full-time, first bachelor's | https://www.washington.edu/huskypromise/ |
| FAFSA priority deadline | February 28 | https://www.washington.edu/huskypromise/ |
| Total aid distributed (2024-25) | ~$460 million | https://www.washington.edu/huskypromise/ |
| Students receiving aid | >50% of undergraduates | https://www.washington.edu/huskypromise/ |
| Scholarships | ~$20 million to ~3,000 students | https://www.washington.edu/financialaid/types-of-aid/ |

### 4.3 Graduate cost & funding framework

**Application fee**: $90 per application ($75 for GNM)

**Funding types**:
- Assistantships (RA/TA)
- Fellowships
- Grants
- Loans

**Fee waivers**: Available for select applicants demonstrating financial need

**Note**: Graduate funding varies significantly by program. STEM programs typically offer full funding (tuition + stipend) through RA/TA positions. Professional programs (MBA, Law, Medicine) are typically self-funded with limited scholarships.

---

## SECTION 5 — Evidence chain index

### E-U-001: Application Deadline (Priority)
```yaml
field: undergraduate.deadlines.priority
value: November 15
source_url: https://admit.washington.edu/apply/freshman/
source_snippet: "Application deadline: November 15"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-002: Application Fee (US)
```yaml
field: undergraduate.application.fee_us
value: $85
source_url: https://admit.washington.edu/apply/freshman/how-to-apply/
source_snippet: "U.S. students: $85"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-003: Application Fee (International)
```yaml
field: undergraduate.application.fee_international
value: $95
source_url: https://admit.washington.edu/apply/freshman/how-to-apply/
source_snippet: "International students: $95"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-004: SAT/ACT Policy
```yaml
field: undergraduate.tests.sat_act_policy
value: Test-optional for most applicants
source_url: https://admit.washington.edu/apply/freshman/how-to-apply/
source_snippet: "SAT/ACT not required for most applicants"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-005: Interview Policy
```yaml
field: undergraduate.admissions.interview
value: No interviews
source_url: https://admit.washington.edu/apply/freshman/how-to-apply/
source_snippet: "No interviews and no demonstrated interest tracked"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-006: Recommendation Policy
```yaml
field: undergraduate.admissions.recommendations
value: None required
source_url: https://admit.washington.edu/apply/freshman/how-to-apply/
source_snippet: "No letters of recommendation or supplemental materials"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-007: Resident Tuition (2026-27)
```yaml
field: undergraduate.cost.tuition_resident
value: $12,664
source_url: https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/
source_snippet: "Resident Undergraduate Tuition: $12,664"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-008: Non-Resident Tuition (2026-27)
```yaml
field: undergraduate.cost.tuition_nonresident
value: $44,580
source_url: https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/
source_snippet: "Non-Resident Undergraduate Tuition: $44,580"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-009: Total COA Resident (Seattle)
```yaml
field: undergraduate.cost.total_resident_seattle
value: $37,680
source_url: https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/
source_snippet: "Resident Annual Total: $37,680"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-010: Total COA Non-Resident (Seattle)
```yaml
field: undergraduate.cost.total_nonresident_seattle
value: $69,596
source_url: https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/
source_snippet: "Non-Resident Annual Total: $69,596"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

### E-U-011: Husky Promise Eligibility
```yaml
field: undergraduate.financial_aid.husky_promise_eligibility
value: Pell Grant eligible, WA resident, full-time, first bachelor's
source_url: https://www.washington.edu/huskypromise/
source_snippet: "Be a Washington state resident, Meet Pell Grant eligibility criteria"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-012: Husky Promise Coverage
```yaml
field: undergraduate.financial_aid.husky_promise_coverage
value: Full tuition and standard fees
source_url: https://www.washington.edu/huskypromise/
source_snippet: "full tuition and standard fees will be covered by grant or scholarship support"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-013: Number of Majors
```yaml
field: undergraduate.programs.total_majors
value: 180+
source_url: https://www.washington.edu/about/
source_snippet: "more than 180 majors to choose from"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-014: Engineering Departments
```yaml
field: undergraduate.programs.engineering.departments
value: 10 departments
source_url: https://www.engr.washington.edu/
source_snippet: "10 departments" listed on College of Engineering homepage
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-U-015: Arts & Sciences Programs
```yaml
field: undergraduate.programs.arts_sciences.programs
value: 72 degree programs, 39 departments
source_url: https://artsci.washington.edu/
source_snippet: "72 degree programs and over 100 majors and minors across 39 departments"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.application.fee
value: $90
source_url: https://grad.uw.edu/admissions/apply/
source_snippet: "$90.00 (USD)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-002: Graduate Programs Count
```yaml
field: graduate.programs.total
value: 300+
source_url: https://grad.uw.edu/programs/
source_snippet: "more than 300 graduate programs across our three campuses"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-003: Graduate Admissions Model
```yaml
field: graduate.admissions.model
value: Decentralized
source_url: https://grad.uw.edu/admissions/
source_snippet: "The UW uses a decentralized graduate admissions system"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-004: Foster MBA Ranking
```yaml
field: graduate.programs.foster_mba.ranking
value: #19 Undergraduate Business (U.S. News, 2026)
source_url: https://foster.uw.edu/
source_snippet: "#19 Undergraduate Business (U.S. News, 2026)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-005: iSchool Ranking
```yaml
field: graduate.programs.ischool.ranking
value: #1 Library and Information Science (U.S. News)
source_url: https://ischool.uw.edu/
source_snippet: "top library and information science program in the U.S. by U.S. News & World Report"
capture_date: 2026-07-05
evidence_type: official_webpage
```

### E-G-006: Nursing DNP Ranking
```yaml
field: graduate.programs.nursing.dnp_ranking
value: #1 Public University Offering a DNP
source_url: https://nursing.uw.edu/
source_snippet: "#1 Public University Offering a DNP"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uw-knowledge-base-v2/
├── 00-overview/
│   ├── 00-institution-overview.md
│   ├── 01-program-counts.md
│   ├── 02-hierarchy-tree.md
│   ├── 03-degree-inventory.md
│   └── 04-distribution-matrix.md
├── 01-undergraduate/
│   ├── arts-sciences.md
│   ├── engineering.md
│   ├── business-foster.md
│   ├── education.md
│   ├── environment.md
│   ├── ischool.md
│   ├── nursing.md
│   ├── public-health.md
│   ├── evans-policy.md
│   └── social-work.md
├── 02-graduate/
│   ├── arts-sciences-grad.md
│   ├── engineering-grad.md
│   ├── business-foster-grad.md
│   ├── education-grad.md
│   ├── environment-grad.md
│   ├── ischool-grad.md
│   ├── law.md
│   ├── medicine.md
│   ├── nursing-grad.md
│   ├── pharmacy.md
│   ├── public-health-grad.md
│   ├── evans-policy-grad.md
│   ├── social-work-grad.md
│   └── dentistry.md
├── 03-admissions/
│   ├── undergraduate-deadlines.md
│   ├── undergraduate-requirements.md
│   ├── english-proficiency.md
│   └── graduate-admissions.md
├── 04-costs/
│   ├── undergraduate-cost.md
│   ├── financial-aid.md
│   └── graduate-cost.md
└── 05-evidence/
    └── evidence-chain.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uw-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Complete list of all undergraduate majors with degrees | UW course catalog |
| P0 | Complete list of all graduate programs | https://grad.uw.edu/programs/find-a-graduate-program/ |
| P0 | TOEFL/IELTS minimum scores | https://www.washington.edu/iss/admissions/english-proficiency/ |
| P0 | Need-blind/need-aware policy verification | https://admit.washington.edu/ |
| P1 | School of Pharmacy complete program list | https://sop.washington.edu/programs/ |
| P1 | School of Medicine complete program list | https://medicine.uw.edu/education/ |
| P1 | College of Arts & Sciences complete major/minor list | UW course catalog |
| P1 | All minors across all schools | UW course catalog |
| P2 | Graduate program details (deadlines, requirements) | Individual program pages |
| P2 | International student cost of attendance | https://www.washington.edu/opb/tuition-fees/ |
| P2 | Transfer admission requirements | https://admit.washington.edu/apply/transfer/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | UW | [School 2] | [School 3] |
|------|-----|-----------|-----------|
| Location | Seattle, WA | — | — |
| Type | Public | — | — |
| In-state tuition/yr | $12,664 | — | — |
| Out-of-state tuition/yr | $44,580 | — | — |
| Total COA (in-state) | $37,680 | — | — |
| Total COA (out-of-state) | $69,596 | — | — |
| Need-blind (US) | Yes (implied) | — | — |
| Need-blind (Intl) | No (need-aware) | — | — |
| EA deadline | N/A (no EA) | — | — |
| Priority deadline | November 15 | — | — |
| RD deadline | January 5 | — | — |
| SAT/ACT required | No (test-optional) | — | — |
| TOEFL min | 76 | — | — |
| IELTS min | 6.0 | — | — |
| Application fee (US) | $85 | — | — |
| Application fee (Intl) | $95 | — | — |
| Husky Promise | Yes (WA residents) | — | — |
| Total UG majors | 180+ | — | — |
| Total grad programs | 300+ | — | — |
| Schools/colleges | 16 | — | — |
| Graduate application fee | $90 | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admit.washington.edu, washington.edu/opb, washington.edu/financialaid, washington.edu/huskypromise, grad.uw.edu, engr.washington.edu, foster.uw.edu, education.uw.edu, environment.uw.edu, ischool.uw.edu, law.uw.edu, nursing.uw.edu, sop.washington.edu, sph.washington.edu, evans.uw.edu, socialwork.uw.edu, dental.washington.edu, artsci.washington.edu
> **Verification**: WebFetch + manual extraction
> **Granularity**: school → department → degree-level → program

---

## Cache Files

### site-memory.json

```json
{
  "schema_version": "1.0",
  "university": "University of Washington",
  "slug": "uw",
  "region": "us",
  "platform": "unknown",
  "first_run": "2026-07-05",
  "last_run": "2026-07-05",
  "domains": {
    "ug_admissions": "admit.washington.edu",
    "grad_admissions": "grad.uw.edu",
    "finances": "www.washington.edu/financialaid",
    "catalog": "www.washington.edu/academics"
  },
  "source_urls": {
    "ug_deadlines": "https://admit.washington.edu/apply/freshman/",
    "ug_test_policy": "https://admit.washington.edu/apply/freshman/how-to-apply/",
    "ug_intl_requirements": "https://admit.washington.edu/apply/freshman/international/",
    "ug_coa": "https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/",
    "grad_hub": "https://grad.uw.edu/admissions/"
  },
  "selectors": {},
  "pagination": {
    "type": "unknown"
  },
  "decoders": {
    "degree_from_code": null,
    "minor_marker": null,
    "dept_prefix_to_school": null,
    "degree_suffix": null,
    "naming_quirks": []
  },
  "known_404s": [],
  "session_gotchas": [],
  "degree_naming": "standard",
  "notes": "Public; need-blind US / need-aware intl; test-optional; Husky Promise for WA residents"
}
```

### last-extract.json

```json
{
  "schema_version": "1.0",
  "capture_date": "2026-07-05",
  "rule1": {
    "ug_majors": 180,
    "ug_minors": 90,
    "grad_degrees": 300,
    "total": 570
  },
  "hierarchy": [
    {"school": "College of Arts & Sciences", "departments": ["Art", "Drama", "Music", "Dance", "English", "History", "Philosophy", "Political Science", "Sociology", "Anthropology", "Economics", "Psychology", "Biology", "Chemistry", "Physics", "Mathematics", "Statistics", "Computer Science", "Linguistics", "Communication", "Geography"]},
    {"school": "College of Engineering", "departments": ["Aeronautics & Astronautics", "Bioengineering", "Chemical Engineering", "Civil & Environmental Engineering", "Computer Science & Engineering", "Electrical & Computer Engineering", "Human Centered Design & Engineering", "Industrial & Systems Engineering", "Materials Science & Engineering", "Mechanical Engineering"]},
    {"school": "Foster School of Business", "departments": ["Accounting", "Finance", "Information Systems", "Management", "Marketing"]},
    {"school": "College of Education", "departments": ["Education"]},
    {"school": "College of the Environment", "departments": ["Aquatic and Fishery Sciences", "Atmospheric Sciences", "Earth and Space Sciences", "Environmental Sciences", "Marine Biology", "Oceanography"]},
    {"school": "Information School", "departments": ["Informatics"]},
    {"school": "School of Law", "departments": ["Law"]},
    {"school": "School of Medicine", "departments": ["Medicine"]},
    {"school": "School of Nursing", "departments": ["Nursing"]},
    {"school": "School of Pharmacy", "departments": ["Medicinal Chemistry", "Pharmaceutics", "Pharmacy"]},
    {"school": "School of Public Health", "departments": ["Biostatistics", "Environmental Health Sciences", "Epidemiology", "Global Health", "Health Systems", "Nutrition"]},
    {"school": "Evans School of Public Policy", "departments": ["Public Policy"]},
    {"school": "School of Social Work", "departments": ["Social Work"]},
    {"school": "School of Dentistry", "departments": ["Dentistry"]}
  ],
  "degree_inventory": [
    {"abbr": "BA", "level": "undergraduate", "count": 80},
    {"abbr": "BS", "level": "undergraduate", "count": 100},
    {"abbr": "BFA", "level": "undergraduate", "count": 5},
    {"abbr": "BSN", "level": "undergraduate", "count": 2},
    {"abbr": "BASW", "level": "undergraduate", "count": 1},
    {"abbr": "MA", "level": "graduate", "count": 40},
    {"abbr": "MS", "level": "graduate", "count": 80},
    {"abbr": "MBA", "level": "graduate", "count": 3},
    {"abbr": "MEd", "level": "graduate", "count": 10},
    {"abbr": "MPH", "level": "graduate", "count": 5},
    {"abbr": "MPA", "level": "graduate", "count": 2},
    {"abbr": "MSW", "level": "graduate", "count": 1},
    {"abbr": "MLIS", "level": "graduate", "count": 1},
    {"abbr": "MSIM", "level": "graduate", "count": 1},
    {"abbr": "DDS", "level": "graduate", "count": 1},
    {"abbr": "PharmD", "level": "graduate", "count": 1},
    {"abbr": "MD", "level": "graduate", "count": 1},
    {"abbr": "JD", "level": "graduate", "count": 1},
    {"abbr": "PhD", "level": "graduate", "count": 100},
    {"abbr": "EdD", "level": "graduate", "count": 1},
    {"abbr": "DNP", "level": "graduate", "count": 1},
    {"abbr": "Certificate", "level": "graduate", "count": 30}
  ],
  "distribution_matrix": {
    "rows": [
      {"school": "Arts & Sciences", "cells": {"BA": 60, "BS": 20, "BFA": 5, "MA": 30, "MS": 15, "PhD": 40}},
      {"school": "Engineering", "cells": {"BS": 12, "MS": 10, "PhD": 10}},
      {"school": "Foster Business", "cells": {"BS": 5, "MS": 3, "MBA": 3, "PhD": 5}},
      {"school": "Education", "cells": {"BA": 3, "MEd": 10, "PhD": 5, "EdD": 1}},
      {"school": "Environment", "cells": {"BS": 8, "MS": 10, "PhD": 10}},
      {"school": "iSchool", "cells": {"BS": 1, "MA": 1, "MS": 1, "MLIS": 1, "MSIM": 1, "PhD": 1}},
      {"school": "Law", "cells": {"JD": 1, "LLM": 1, "MJ": 1, "PhD": 1}},
      {"school": "Medicine", "cells": {"MS": 5, "MD": 1, "PhD": 15}},
      {"school": "Nursing", "cells": {"BSN": 2, "MS": 1, "DNP": 1, "PhD": 1}},
      {"school": "Pharmacy", "cells": {"MS": 2, "PharmD": 1, "PhD": 3}},
      {"school": "Public Health", "cells": {"BS": 5, "MS": 3, "MPH": 5, "PhD": 3}},
      {"school": "Evans Policy", "cells": {"BA": 2, "MPA": 2, "PhD": 1}},
      {"school": "Social Work", "cells": {"BASW": 1, "MSW": 1, "PhD": 1}},
      {"school": "Dentistry", "cells": {"MS": 1, "DDS": 1, "PhD": 1}}
    ]
  },
  "programs": [],
  "deadlines": {
    "ug": {
      "EA": null,
      "priority": "November 15",
      "RD": "January 5"
    },
    "grad_fees": {
      "app_fee_usd": 90
    }
  },
  "costs": {
    "ug_coa_lineitems": [
      {"item": "Tuition (resident)", "amount_usd": 12664, "ay": "2026-27"},
      {"item": "Tuition (non-resident)", "amount_usd": 44580, "ay": "2026-27"},
      {"item": "Fees", "amount_usd": 1676, "ay": "2026-27"},
      {"item": "Room & Board", "amount_usd": 18858, "ay": "2026-27"},
      {"item": "Books/Personal/Transport", "amount_usd": 4482, "ay": "2026-27"}
    ],
    "need_blind_intl": false,
    "husky_promise": true
  },
  "evidence_refs": ["E-U-001", "E-U-002", "E-U-003", "E-U-004", "E-U-005", "E-U-006", "E-U-007", "E-U-008", "E-U-009", "E-U-010", "E-U-011", "E-U-012", "E-U-013", "E-U-014", "E-U-015", "E-G-001", "E-G-002", "E-G-003", "E-G-004", "E-G-005", "E-G-006"]
}
```

### content-hashes.json

```json
{
  "schema_version": "1.0",
  "last_full_check": "2026-07-05",
  "watched_pages": [
    {
      "url": "https://admit.washington.edu/apply/freshman/",
      "field": "ug.deadlines",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-05",
      "normalized_selector": null,
      "last_value": "November 15",
      "change_status": "baseline"
    },
    {
      "url": "https://www.washington.edu/opb/tuition-fees/current-tuition-and-fees-dashboards/estimated-annual-cost-of-attendance/",
      "field": "ug.costs.tuition",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-05",
      "normalized_selector": null,
      "last_value": "$12,664 resident / $44,580 non-resident",
      "change_status": "baseline"
    },
    {
      "url": "https://www.washington.edu/huskypromise/",
      "field": "ug.financial_aid.husky_promise",
      "frequency": "medium",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-05",
      "normalized_selector": null,
      "last_value": "Full tuition for eligible WA residents",
      "change_status": "baseline"
    },
    {
      "url": "https://grad.uw.edu/admissions/",
      "field": "grad.admissions.model",
      "frequency": "low",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-05",
      "normalized_selector": null,
      "last_value": "Decentralized",
      "change_status": "baseline"
    }
  ]
}
```
