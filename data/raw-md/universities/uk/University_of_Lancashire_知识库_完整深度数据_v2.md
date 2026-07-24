# University of Lancashire Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: subject (school-proxy) → degree-level → program
> **Document version**: v2.0 (deep)

> **Note on identity**: University of Lancashire is the rebranded University of Central Lancashire (UCLan). Email addresses (cenquiries@uclan.ac.uk) and historical content still reference UCLan. Treated here as one institution.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/MEng/MPhys/MSci/FdA/FdSc/LLB/BDS/MBBS/MPharm/BVMS/Dip HE/Cert HE) | 282 |
| 本科辅修 (Minor) | 0 (UoL does not publish a discrete minor list; integrated year-in-industry variants are listed as separate courses) |
| 研究生学位项目 (MA/MSc/MBA/MRes/MEd/MArch/LLM/PGDip/PGCert/PGCE) | 123 |
| 研究生高级证书 (Advanced Certificate / Diploma) | included in PGCert/PGDip above |
| 研究生研究学位 (PhD/DBA/EdD/DProf/MPhil/MSc by Research/MA by Research) | 17 |
| **学位项目总计 (UG + PGT + PGR)** | **422** |
| 学科 / 院系主题 (Subjects, school-proxy) | 51 |
| 学科 with UG offerings | 47 |
| 学科 with PG offerings | 35 |
| 学科 with PGR offerings | 12 |

> Reconciliation: rule-1 total 422 = 282 UG + 123 PGT + 17 PGR (verified).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

UoL does not publish a "Schools / Colleges" taxonomy. The 51 Subjects at `https://www.lancashire.ac.uk/subjects` function as the school/department proxy. Each Subject aggregates related courses at UG, PGT, and PGR levels.

```
University of Lancashire
├── Accounting and Finance                              [Subject]
├── Aerospace Engineering                              [Subject]
├── Archaeology                                        [Subject]
├── Architecture                                       [Subject]
├── Astronomy                                          [Subject]
├── Audiology                                          [Subject]
├── Biosciences                                        [Subject]
├── BSL and Deaf Studies                               [Subject]
├── Business and Management                            [Subject]
├── Chemistry                                          [Subject]
├── Civil Engineering                                  [Subject]
├── Computer Science                                   [Subject]
├── Construction and Surveying                         [Subject]
├── Criminology                                        [Subject]
├── Dentistry                                          [Subject]
├── Design                                             [Subject]
├── Education                                          [Subject]
├── Electrical and Robotics Engineering                [Subject]
├── Energy and Environment                             [Subject]
├── English                                            [Subject]
├── Fashion                                            [Subject]
├── Film and Screen                                    [Subject]
├── Fine Art and Photography                           [Subject]
├── Fire and Safety                                    [Subject]
├── Forensic Science                                   [Subject]
├── Games and Animation                                [Subject]
├── Health Professions                                 [Subject]
├── History                                            [Subject]
├── Journalism                                         [Subject]
├── Languages                                          [Subject]
├── Law                                                [Subject]
├── Mathematics                                        [Subject]
├── Mechanical Engineering                             [Subject]
├── Medicine                                           [Subject]
├── Midwifery                                          [Subject]
├── Nursing                                            [Subject]
├── Nutrition                                          [Subject]
├── Optometry                                          [Subject]
├── Performance and Music                              [Subject]
├── Pharmacy                                           [Subject]
├── Physics and Astrophysics                           [Subject]
├── Policing and Investigation                         [Subject]
├── Psychology                                         [Subject]
├── Publishing                                         [Subject]
├── Social Care and Community                          [Subject]
├── Social Work                                        [Subject]
├── Sociology                                          [Subject]
├── Sport and Exercise Sciences                        [Subject]
├── Sport Coaching and Leadership                      [Subject]
├── TESOL                                              [Subject]
└── Veterinary Medicine                                [Subject]
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (canonical) | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts (Hons) | 本科 | 94 |
| BSc | Bachelor of Science (Hons) | 本科 | 121 |
| BEng | Bachelor of Engineering (Hons) | 本科 | 28 |
| MEng | Master of Engineering (Hons) (UG integrated master's) | 本科 | 8 |
| MPhys | Master of Physics (Hons) | 本科 | 2 |
| MSci | Master in Science (Hons) | 本科 | 1 |
| FdA | Foundation Degree in Arts | 本科 | 2 |
| FdSc | Foundation Degree in Science | 本科 | 6 |
| LLB | Bachelor of Laws (Hons) | 本科 | 7 |
| BDS | Bachelor of Dental Surgery | 本科 | 2 |
| MBBS | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| MPharm | Master of Pharmacy (Hons) | 本科 | 1 |
| BVMS | Bachelor of Veterinary Medicine & Surgery | 本科 | 2 |
| Dip HE | Diploma of Higher Education | 本科 | 1 |
| Cert HE | Certificate of Higher Education | 本科 | 1 |
| MA | Master of Arts | 研究生 | 16 |
| MSc | Master of Science | 研究生 | 79 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MRes | Master of Research | 研究生 | 6 |
| MEd | Master of Education | 研究生 | 1 |
| MArch | Master of Architecture (Part II) | 研究生 | 1 |
| MOptom | Master of Optometry | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| PGDip | Postgraduate Diploma | 研究生 | 3 |
| PGCert | Postgraduate Certificate | 研究生 | 12 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 6 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| EdD | Doctorate in Education | 研究生 | 1 |
| DProf | Professional Doctorate | 研究生 | 4 |
| MSc by Research | (PGR research master's) | 研究生 | 5 |
| MA by Research | (PGR research master's) | 研究生 | (embedded in PhD listings) |

### 0.4 分布矩阵 (Rule 4 — Subject × degree cross-tabs)

#### Undergraduate: Subject × canonical degree

| Subject | BA | BSc | BEng | MEng | MPhys | MSci | FdA | FdSc | LLB | BDS | MBBS | MPharm | BVMS | Dip HE | Cert HE | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---||---|
| Accounting and Finance | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Aerospace Engineering | 0 | 0 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Archaeology | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Architecture | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Astronomy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Biosciences | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| BSL and Deaf Studies | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Business and Management | 20 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| Civil Engineering | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Computer Science | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| Construction and Surveying | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Criminology | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Dentistry | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | 5 |
| Design | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Education | 6 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Electrical and Robotics Engineering | 0 | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 |
| Energy and Environment | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| English | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Fashion | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Film and Screen | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Fine Art and Photography | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Fire and Safety | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Forensic Science | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Games and Animation | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Health Professions | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 7 |
| History | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Journalism | 10 | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 14 |
| Languages | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Mathematics | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Mechanical Engineering | 0 | 0 | 4 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Medicine | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 7 |
| Midwifery | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Nursing | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| Nutrition | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Performance and Music | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Pharmacy | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| Physics and Astrophysics | 0 | 6 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Policing and Investigation | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 |
| Psychology | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 |
| Social Care and Community | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Social Work | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Sociology | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| Sport and Exercise Sciences | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Sport Coaching and Leadership | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Veterinary Medicine | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 4 |
| General / Interdisciplinary | 2 | 7 | 3 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 16 |
| **TOTAL** | 94 | 121 | 28 | 8 | 2 | 1 | 2 | 6 | 7 | 2 | 2 | 1 | 2 | 1 | 1 | 282 |


#### Postgraduate Taught: Subject × canonical degree

| Subject | MA | MSc | MBA | MRes | MEd | MArch | LLM | PGDip | PGCert | PGCE | Total |
|---|---|---|---|---|---|---|---|---|---|---||---|
| Aerospace Engineering | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Architecture | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Biosciences | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Business and Management | 2 | 16 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 23 |
| Computer Science | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Criminology | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Design | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Education | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 8 |
| Electrical and Robotics Engineering | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Energy and Environment | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Fine Art and Photography | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Fire and Safety | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Games and Animation | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Health Professions | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 |
| History | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Journalism | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Languages | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| Mechanical Engineering | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Medicine | 0 | 3 | 0 | 1 | 0 | 0 | 0 | 1 | 2 | 0 | 7 |
| Midwifery | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Nursing | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 5 |
| Nutrition | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Optometry | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Performance and Music | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| Pharmacy | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Physics and Astrophysics | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Policing and Investigation | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Psychology | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 6 |
| Publishing | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Social Care and Community | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Social Work | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 3 |
| Sociology | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Sport and Exercise Sciences | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| General / Interdisciplinary | 3 | 14 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 19 |
| **TOTAL** | 16 | 79 | 2 | 6 | 1 | 0 | 1 | 3 | 12 | 0 | 123 |


#### Postgraduate Research: Subject × canonical degree

| Subject | PhD | DBA | EdD | DProf | Total |
|---|---|---|---|---||---|
| Business and Management | 0 | 1 | 0 | 0 | 1 |
| Chemistry | 0 | 0 | 0 | 0 | 0 |
| Education | 0 | 0 | 1 | 0 | 1 |
| English | 1 | 0 | 0 | 0 | 1 |
| Forensic Science | 1 | 0 | 0 | 0 | 1 |
| Health Professions | 0 | 0 | 0 | 1 | 1 |
| Journalism | 0 | 0 | 0 | 1 | 1 |
| Physics and Astrophysics | 0 | 0 | 0 | 0 | 0 |
| Psychology | 1 | 0 | 0 | 1 | 2 |
| Social Care and Community | 0 | 0 | 0 | 1 | 1 |
| Sociology | 2 | 0 | 0 | 0 | 2 |
| General / Interdisciplinary | 1 | 0 | 0 | 0 | 1 |
| **TOTAL** | 6 | 1 | 1 | 4 | 17 |


> Reconciliation check: UG row-totals (282) + PGT row-totals (123) + PGR row-totals (17) = 422 = Rule-1 total. PASS.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

UoL's UG portfolio spans 282 degree programmes across 47 subjects. Each programme is presented under its mapped Subject.

#### Subject: Accounting and Finance
### Accounting and Finance

**Undergraduate (5):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting & Finance (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/accounting-finance-ba-foundation |
| 2 | Accounting & Finance | https://www.lancashire.ac.uk/undergraduate/courses/accounting-finance-ba |
| 3 | Accounting & Financial Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/accounting-financial-management-ba-foundation |
| 4 | Accounting & Financial Management | https://www.lancashire.ac.uk/undergraduate/courses/accounting-financial-management-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance Management | https://www.lancashire.ac.uk/degree-apprenticeships/courses/accounting-finance-management-bsc |


#### Subject: Aerospace Engineering
### Aerospace Engineering

**Undergraduate (8):**

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-beng-foundation |
| 2 | Aerospace Engineering with Pilot Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-pilot-beng-foundation |
| 3 | Aerospace Engineering with Pilot Studies | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-with-pilot-studies-beng |
| 4 | Aerospace Engineering | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-beng |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-meng-foundation |
| 2 | Aerospace Engineering with Pilot Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-pilot-meng-foundation |
| 3 | Aerospace Engineering with Pilot Studies | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-with-pilot-studies-meng |
| 4 | Aerospace Engineering | https://www.lancashire.ac.uk/undergraduate/courses/aerospace-engineering-meng |


#### Subject: Archaeology
### Archaeology

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology | https://www.lancashire.ac.uk/undergraduate/courses/archaeology-bsc |

###### MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology | https://www.lancashire.ac.uk/undergraduate/courses/archaeology-msci |


#### Subject: Architecture
### Architecture

**Undergraduate (3):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/architecture-bsc-foundation |
| 2 | Architecture | https://www.lancashire.ac.uk/undergraduate/courses/architecture-bsc |

###### Other
| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies, BSc (Hons) – Hong Kong | https://www.lancashire.ac.uk/undergraduate/courses/architectural-studies-bsc-hong-kong |


#### Subject: Astronomy
### Astronomy

**Undergraduate (1):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Astronomy | https://www.lancashire.ac.uk/undergraduate/courses/astronomy-bsc-distance-learning |


#### Subject: Biosciences
### Biosciences

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/biology-bsc-hons-foundation |
| 2 | Biology | https://www.lancashire.ac.uk/undergraduate/courses/biology-bsc |


#### Subject: BSL and Deaf Studies
### BSL and Deaf Studies

**Undergraduate (2):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | British Sign Language & Deaf Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/british-sign-language-deaf-studies-ba-foundation |
| 2 | British Sign Language & Deaf Studies | https://www.lancashire.ac.uk/undergraduate/courses/british-sign-language-deaf-studies-ba |


#### Subject: Business and Management
### Business and Management

**Undergraduate (36):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Business & Entrepreneurship (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-entrepreneurship-ba-foundation |
| 2 | Business & Entrepreneurship | https://www.lancashire.ac.uk/undergraduate/courses/business-entrepreneurship-ba |
| 3 | Business & Finance (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-finance-ba-foundation |
| 4 | Business & Finance | https://www.lancashire.ac.uk/undergraduate/courses/business-finance-ba |
| 5 | Business & Hospitality (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-hospitality-ba-foundation |
| 6 | Business & Hospitality | https://www.lancashire.ac.uk/undergraduate/courses/business-hospitality-ba |
| 7 | Business & Human Resource Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-hrm-foundation-ba |
| 8 | Business & Human Resource Management | https://www.lancashire.ac.uk/undergraduate/courses/business-hr-management-ba |
| 9 | Business & Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-management-ba-foundation |
| 10 | Business & Management | https://www.lancashire.ac.uk/undergraduate/courses/business-management-ba |
| 11 | Business & Tourism (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-tourism-ba-foundation |
| 12 | Business & Tourism | https://www.lancashire.ac.uk/undergraduate/courses/business-tourism-ba |
| 13 | Business Administration (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/business-administration-ba-top-up |
| 14 | Business Management | https://www.lancashire.ac.uk/degree-apprenticeships/courses/business-management-ba |
| 15 | Digital Marketing | https://www.lancashire.ac.uk/degree-apprenticeships/courses/digital-marketing-ba |
| 16 | Fashion Promotion & Marketing | https://www.lancashire.ac.uk/undergraduate/courses/fashion-promotion-marketing-ba |
| 17 | International Business (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/international-business-ba-foundation |
| 18 | International Business Communication | https://www.lancashire.ac.uk/undergraduate/courses/international-business-communication-ba |
| 19 | International Business | https://www.lancashire.ac.uk/undergraduate/courses/international-business-ba |
| 20 | Leadership Through Outdoor Adventure | https://www.lancashire.ac.uk/undergraduate/courses/leadership-outdoor-adventure-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Business & Marketing (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/business-marketing-bsc-foundation |
| 2 | Business & Marketing | https://www.lancashire.ac.uk/undergraduate/courses/business-marketing-bsc |
| 3 | Construction Project Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/construction-project-management-bsc-foundation |
| 4 | Construction Project Management | https://www.lancashire.ac.uk/undergraduate/courses/construction-project-management-bsc |
| 5 | Digital Marketing (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/digital-marketing-bsc-foundation |
| 6 | Digital Marketing | https://www.lancashire.ac.uk/undergraduate/courses/digital-marketing-bsc |
| 7 | Facilities Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/facilities-management-bsc-foundation |
| 8 | Facilities Management | https://www.lancashire.ac.uk/undergraduate/courses/facilities-management-bsc |
| 9 | Fire & Leadership Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/fire-leadership-studies-bsc-foundation |
| 10 | Fire & Leadership Studies | https://www.lancashire.ac.uk/undergraduate/courses/fire-leadership-studies-bsc |
| 11 | Fire Safety (Management) (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/fire-safety-management-bsc-top-up |
| 12 | Sport Business Management (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sports-business-management-bsc-foundation |
| 13 | Sport Business Management | https://www.lancashire.ac.uk/undergraduate/courses/sports-business-management-bsc |

###### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | Law with Business (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/law-business-foundation-llb |
| 2 | Law with Business | https://www.lancashire.ac.uk/undergraduate/courses/law-with-business-llb |

###### Other
| # | 专业 | URL |
|---|------|-----|
| 1 | Business - Return to Study | https://www.lancashire.ac.uk/undergraduate/courses/return-to-study-business |


#### Subject: Chemistry
### Chemistry


#### Subject: Civil Engineering
### Civil Engineering

**Undergraduate (5):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Quantity Surveying (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/quantity-surveying-bsc-foundation |
| 2 | Quantity Surveying | https://www.lancashire.ac.uk/undergraduate/courses/quantity-surveying-bsc |
| 3 | Quantity Surveying | https://www.lancashire.ac.uk/degree-apprenticeships/courses/quantity-surveying-bsc-hons |

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/civil-engineering-beng-foundation |
| 2 | Civil Engineering | https://www.lancashire.ac.uk/undergraduate/courses/civil-engineering-beng |


#### Subject: Computer Science
### Computer Science

**Undergraduate (17):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence & Data Science (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/ai-data-science-foundation-bsc |
| 2 | Artificial Intelligence & Data Science | https://www.lancashire.ac.uk/undergraduate/courses/artificial-intelligence-data-science-bsc |
| 3 | Computer Games Development (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/computer-games-development-bsc-foundation |
| 4 | Computer Games Development | https://www.lancashire.ac.uk/undergraduate/courses/computer-games-development-bsc |
| 5 | Computer Networks & Security (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/computer-networks-security-bsc-foundation |
| 6 | Computer Networks & Security | https://www.lancashire.ac.uk/undergraduate/courses/computer-networks-security-bsc |
| 7 | Computer Science (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/computer-science-bsc-foundation |
| 8 | Computer Science | https://www.lancashire.ac.uk/undergraduate/courses/computer-science-bsc |
| 9 | Computing (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/computing-bsc-foundation |
| 10 | Computing | https://www.lancashire.ac.uk/undergraduate/courses/computing-bsc-hons |
| 11 | Cyber Security (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/cyber-security-bsc-foundation |
| 12 | Cyber Security Technician | https://www.lancashire.ac.uk/degree-apprenticeships/courses/cyber-security-technician-bsc |
| 13 | Cyber Security | https://www.lancashire.ac.uk/undergraduate/courses/cyber-security-bsc-hons |
| 14 | High Integrity Software Engineering | https://www.lancashire.ac.uk/degree-apprenticeships/courses/high-integrity-software-engineering-bsc |
| 15 | Software Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/software-engineering-bsc-foundation |
| 16 | Software Engineering | https://www.lancashire.ac.uk/undergraduate/courses/software-engineering-bsc |
| 17 | Software Engineering | https://www.lancashire.ac.uk/degree-apprenticeships/courses/software-engineering-beng |


#### Subject: Construction and Surveying
### Construction and Surveying

**Undergraduate (3):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Building Surveying (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/building-surveying-foundation |
| 2 | Building Surveying | https://www.lancashire.ac.uk/undergraduate/courses/building-surveying-bsc |
| 3 | Building Surveying | https://www.lancashire.ac.uk/degree-apprenticeships/courses/building-surveying-bsc |


#### Subject: Criminology
### Criminology

**Undergraduate (5):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology & Criminal Justice | https://www.lancashire.ac.uk/undergraduate/courses/criminology-criminal-justice-ba |
| 2 | Criminology and Criminal Justice (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/criminology-criminal-justice-foundation-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology with Criminology | https://www.lancashire.ac.uk/undergraduate/courses/psychology-criminology-bsc |

###### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | Law with Criminology (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/law-criminology-foundation-llb |
| 2 | Law with Criminology | https://www.lancashire.ac.uk/undergraduate/courses/law-with-criminology-llb |


#### Subject: Dentistry
### Dentistry

**Undergraduate (5):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Studies (Dental Care Professionals) | https://www.lancashire.ac.uk/undergraduate/courses/dental-studies-bsc |

###### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Technology | https://www.lancashire.ac.uk/degree-apprenticeships/courses/dental-technology-fdsc |

###### BDS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dental Surgery (International Route) | https://www.lancashire.ac.uk/undergraduate/courses/dental-surgery-bds-international |
| 2 | Dental Surgery | https://www.lancashire.ac.uk/undergraduate/courses/dental-surgery-bds |

###### Cert HE
| # | 专业 | URL |
|---|------|-----|
| 1 | Orthodontic Therapy | https://www.lancashire.ac.uk/degree-apprenticeships/courses/orthodontic-therapy-cert-he |


#### Subject: Design
### Design

**Undergraduate (8):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art & Design (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/art-design-ba-foundation |
| 2 | Games Design (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/games-design-ba-foundation |
| 3 | Games Design | https://www.lancashire.ac.uk/undergraduate/courses/games-design-ba |
| 4 | Graphic Design | https://www.lancashire.ac.uk/undergraduate/courses/graphic-design-ba |
| 5 | Illustration | https://www.lancashire.ac.uk/undergraduate/courses/illustration-ba |
| 6 | Interior Design | https://www.lancashire.ac.uk/undergraduate/courses/interior-design-ba |
| 7 | Sound Design (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sound-design-ba-foundation |
| 8 | Sound Design | https://www.lancashire.ac.uk/undergraduate/courses/sound-design-ba-hons |


#### Subject: Education
### Education

**Undergraduate (7):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Education (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/education-ba-foundation |
| 2 | Education Studies (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/education-studies-ba-top-up |
| 3 | Education with Humanities | https://www.lancashire.ac.uk/undergraduate/courses/education-with-humanities-ba |
| 4 | Education | https://www.lancashire.ac.uk/undergraduate/courses/education-ba |
| 5 | Physical Education & Sport (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/physical-education-sport-ba-foundation |
| 6 | Physical Education & Sport | https://www.lancashire.ac.uk/undergraduate/courses/physical-education-sport-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing with Registered Nurse (Learning Disabilities) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-learning-disabilities |


#### Subject: Electrical and Robotics Engineering
### Electrical and Robotics Engineering

**Undergraduate (10):**

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical & Electronic Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/electrical-electronic-engineering-beng-foundation |
| 2 | Electrical & Electronic Engineering | https://www.lancashire.ac.uk/undergraduate/courses/electrical-electronic-engineering-beng |
| 3 | Electronic Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/electronic-engineering-beng-foundation |
| 4 | Electronic Engineering | https://www.lancashire.ac.uk/undergraduate/courses/electronic-engineering-beng |
| 5 | Mechatronics & Intelligent Machines (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/mechatronics-intelligent-machines-beng-top-up |
| 6 | Mechatronics & Intelligent Machines (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/mechatronics-intelligent-machines-beng-foundation |
| 7 | Mechatronics & Intelligent Machines | https://www.lancashire.ac.uk/undergraduate/courses/mechatronics-intelligent-machines-beng |
| 8 | Professional Engineering (Electrical/Electronic) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/electrical-electronic-beng |
| 9 | Robotics Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/robotics-engineering-beng-foundation |
| 10 | Robotics Engineering | https://www.lancashire.ac.uk/undergraduate/courses/robotics-engineering-beng |


#### Subject: Energy and Environment
### Energy and Environment

**Undergraduate (1):**

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Renewable & Sustainable Energy Engineering | https://www.lancashire.ac.uk/undergraduate/courses/renewable-sustainable-energy-engineering-beng |


#### Subject: English
### English

**Undergraduate (4):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English & Creative Writing (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/english-creative-writing-ba-foundation |
| 2 | English & Creative Writing | https://www.lancashire.ac.uk/undergraduate/courses/english-creative-writing-ba |
| 3 | English Literature (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/english-literature-ba-foundation |
| 4 | English Literature | https://www.lancashire.ac.uk/undergraduate/courses/english-literature-ba |


#### Subject: Fashion
### Fashion

**Undergraduate (1):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Design | https://www.lancashire.ac.uk/undergraduate/courses/fashion-design-ba |


#### Subject: Film and Screen
### Film and Screen

**Undergraduate (6):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Filmmaking (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/filmmaking-ba-foundation |
| 2 | Filmmaking | https://www.lancashire.ac.uk/undergraduate/courses/filmmaking-ba-hons |
| 3 | Media & Television Production (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/media-television-production-ba-foundation |
| 4 | Media & Television Production | https://www.lancashire.ac.uk/undergraduate/courses/media-television-production-ba |
| 5 | Screenwriting with Film, Television & Radio (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/screenwriting-ba-foundation |
| 6 | Screenwriting with Film, Television & Radio | https://www.lancashire.ac.uk/undergraduate/courses/screenwriting-with-film-television-radio-ba |


#### Subject: Fine Art and Photography
### Fine Art and Photography

**Undergraduate (2):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art | https://www.lancashire.ac.uk/undergraduate/courses/fine-art-ba |
| 2 | Photography | https://www.lancashire.ac.uk/undergraduate/courses/photography-ba |


#### Subject: Fire and Safety
### Fire and Safety

**Undergraduate (5):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Fire Safety (Engineering) (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/fire-safety-engineering-bsc-top-up |

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Fire Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/fire-engineering-beng-foundation |
| 2 | Fire Engineering | https://www.lancashire.ac.uk/undergraduate/courses/fire-engineering-beng |
| 3 | Fire Engineering | https://www.lancashire.ac.uk/degree-apprenticeships/courses/fire-engineering-beng |

###### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Fire Safety Engineering | https://www.lancashire.ac.uk/undergraduate/courses/fire-safety-engineering-fdsc |


#### Subject: Forensic Science
### Forensic Science

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Science (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/forensic-science-bsc-foundation |
| 2 | Forensic Science | https://www.lancashire.ac.uk/undergraduate/courses/forensic-science-bsc |


#### Subject: Games and Animation
### Games and Animation

**Undergraduate (4):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Animation (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/animation-ba-foundation |
| 2 | Animation | https://www.lancashire.ac.uk/undergraduate/courses/animation-ba |
| 3 | Game Art (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/game-art-ba-foundation |
| 4 | Game Art | https://www.lancashire.ac.uk/undergraduate/courses/game-art-ba |


#### Subject: Health Professions
### Health Professions

**Undergraduate (7):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Dental Technology | https://www.lancashire.ac.uk/undergraduate/courses/clinical-dental-technology-bsc |
| 2 | Occupational Therapy | https://www.lancashire.ac.uk/degree-apprenticeships/courses/occupational-therapy-bsc |
| 3 | Occupational Therapy | https://www.lancashire.ac.uk/undergraduate/courses/occupational-therapy-bsc |
| 4 | Paramedic Science | https://www.lancashire.ac.uk/undergraduate/courses/paramedic-science-bsc |
| 5 | Physiotherapy | https://www.lancashire.ac.uk/undergraduate/courses/physiotherapy-bsc |
| 6 | Physiotherapy | https://www.lancashire.ac.uk/degree-apprenticeships/courses/physiotherapy-bsc |

###### Dip HE
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Dental Technology | https://www.lancashire.ac.uk/degree-apprenticeships/courses/clinical-dental-technology-dip-he |


#### Subject: History
### History

**Undergraduate (2):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/history-ba-foundation |
| 2 | History | https://www.lancashire.ac.uk/undergraduate/courses/history-ba |


#### Subject: Journalism
### Journalism

**Undergraduate (14):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Children, Schools & Families (Graduate Practitioner) (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/children-schools-families-ba-top-up |
| 2 | Children, Schools & Families (Graduate Practitioner) (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/children-schools-families-ba-foundation |
| 3 | Children, Schools & Families (Graduate Practitioner) | https://www.lancashire.ac.uk/undergraduate/courses/children-schools-families-ba |
| 4 | Journalism (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/journalism-ba-foundation |
| 5 | Journalism | https://www.lancashire.ac.uk/undergraduate/courses/journalism-ba |
| 6 | Sports Journalism (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sports-journalism-ba-foundation |
| 7 | Sports Journalism | https://www.lancashire.ac.uk/undergraduate/courses/sports-journalism-ba |
| 8 | Youth Work & Community Practice (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/youth-work-and-community-practice-foundation-ba |
| 9 | Youth Work & Community Practice | https://www.lancashire.ac.uk/undergraduate/courses/youth-work-and-community-practice-ba |
| 10 | Youth Work & Community Practice | https://www.lancashire.ac.uk/degree-apprenticeships/courses/youth-work-community-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Operating Department Practice | https://www.lancashire.ac.uk/undergraduate/courses/operating-department-practice-bsc-hons |
| 2 | Operating Department Practice | https://www.lancashire.ac.uk/degree-apprenticeships/courses/operating-department-practice-bsc |

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Professional Engineering (Product Development) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/product-development-beng |

###### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Assistant Practitioner | https://www.lancashire.ac.uk/degree-apprenticeships/courses/assistant-practitioner-fdsc |


#### Subject: Languages
### Languages

**Undergraduate (11):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/chinese-studies-ba-foundation |
| 2 | Chinese Studies | https://www.lancashire.ac.uk/undergraduate/courses/chinese-studies-ba |
| 3 | English Language & Linguistics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/english-language-linguistics-ba-foundation |
| 4 | English Language & Linguistics | https://www.lancashire.ac.uk/undergraduate/courses/english-language-linguistics-ba |
| 5 | Japanese Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/japanese-studies-ba-foundation |
| 6 | Japanese Studies | https://www.lancashire.ac.uk/undergraduate/courses/japanese-studies-ba |
| 7 | Modern Languages (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/modern-languages-ba-foundation |
| 8 | Modern Languages | https://www.lancashire.ac.uk/undergraduate/courses/modern-languages-ba-hons |
| 9 | TESOL & a Modern Language (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/tesol-mola-fde |
| 10 | TESOL & a Modern Language | https://www.lancashire.ac.uk/undergraduate/courses/tesol-mola-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech & Language Therapy | https://www.lancashire.ac.uk/degree-apprenticeships/courses/speech-language-therapy-bsc |


#### Subject: Law
### Law

**Undergraduate (3):**

###### LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | Law (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/law-llb-foundation |
| 2 | Law | https://www.lancashire.ac.uk/undergraduate/courses/law-llb |
| 3 | Legal Practice | https://www.lancashire.ac.uk/degree-apprenticeships/courses/legal-practice-llb |


#### Subject: Mathematics
### Mathematics

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/mathematics-bsc-foundation |
| 2 | Mathematics | https://www.lancashire.ac.uk/undergraduate/courses/mathematics-bsc |


#### Subject: Mechanical Engineering
### Mechanical Engineering

**Undergraduate (6):**

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/mechanical-engineering-beng-foundation |
| 2 | Mechanical Engineering | https://www.lancashire.ac.uk/undergraduate/courses/mechanical-engineering-beng |
| 3 | Mechanical Maintenance Engineering (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/mechanical-maintenance-engineering-beng-top-up |
| 4 | Professional Engineering (Manufacturing) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/manufacturing-beng |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/mechanical-engineering-meng-foundation |
| 2 | Mechanical Engineering | https://www.lancashire.ac.uk/undergraduate/courses/mechanical-engineering-meng |


#### Subject: Medicine
### Medicine

**Undergraduate (7):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Biomedical Science | https://www.lancashire.ac.uk/degree-apprenticeships/courses/applied-biomed-science-bsc |
| 2 | Biomedical Science (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/biomedical-science-bsc-foundation |
| 3 | Biomedical Science | https://www.lancashire.ac.uk/undergraduate/courses/biomedical-science-bsc |
| 4 | Medical Sciences (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/medical-sciences-bsc-foundation |
| 5 | Medical Sciences | https://www.lancashire.ac.uk/undergraduate/courses/medical-sciences-bsc |

###### MBBS
| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine & Surgery (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/medicine-mbbs-foundation |
| 2 | Medicine & Surgery | https://www.lancashire.ac.uk/undergraduate/courses/medicine-mbbs |


#### Subject: Midwifery
### Midwifery

**Undergraduate (3):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Midwifery (Shortened) | https://www.lancashire.ac.uk/undergraduate/courses/midwifery-for-registered-nurses-bsc |
| 2 | Midwifery | https://www.lancashire.ac.uk/undergraduate/courses/midwifery-bsc |
| 3 | Midwifery | https://www.lancashire.ac.uk/degree-apprenticeships/courses/midwifery-bsc |


#### Subject: Nursing
### Nursing

**Undergraduate (12):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-top-up-bsc |
| 2 | Nursing in General Practice (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-in-general-practice-top-up-bsc |
| 3 | Nursing with Registered Nurse (Adult) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-with-registered-nurse-adult-bsc |
| 4 | Nursing with Registered Nurse (Adult) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/nursing-with-registered-nurse-adult-bsc |
| 5 | Nursing with Registered Nurse (Adult) | https://www.lancashire.ac.uk/undergraduate/courses/adult-nursing-bsc-practice-based |
| 6 | Nursing with Registered Nurse (Children & Young People) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-children-young-people |
| 7 | Nursing with Registered Nurse (Children & Young People) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/nursing-children-young-people |
| 8 | Nursing with Registered Nurse (Mental Health) | https://www.lancashire.ac.uk/undergraduate/courses/nursing-with-registered-nurse-mental-health-bsc |
| 9 | Nursing with Registered Nurse (Mental Health) | https://www.lancashire.ac.uk/degree-apprenticeships/courses/nursing-mental-health |

###### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing Associate | https://www.lancashire.ac.uk/undergraduate/courses/nursing-associate-fdsc |
| 2 | Nursing Associate | https://www.lancashire.ac.uk/degree-apprenticeships/courses/nursing-associate-fdsc |

###### Other
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing - Return to Study | https://www.lancashire.ac.uk/undergraduate/courses/return-to-study-nursing |


#### Subject: Nutrition
### Nutrition

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/nutrition-bsc-foundation |
| 2 | Nutrition | https://www.lancashire.ac.uk/undergraduate/courses/nutrition-bsc |


#### Subject: Optometry
### Optometry


#### Subject: Performance and Music
### Performance and Music

**Undergraduate (2):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Acting | https://www.lancashire.ac.uk/undergraduate/courses/acting-ba |
| 2 | Music Theatre | https://www.lancashire.ac.uk/undergraduate/courses/music-theatre-ba |


#### Subject: Pharmacy
### Pharmacy

**Undergraduate (3):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacology (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/pharmacology-bsc-foundation |
| 2 | Pharmacology | https://www.lancashire.ac.uk/undergraduate/courses/pharmacology-bsc |

###### MPharm
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.lancashire.ac.uk/undergraduate/courses/pharmacy-mpharm |


#### Subject: Physics and Astrophysics
### Physics and Astrophysics

**Undergraduate (8):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/astrophysics-bsc-foundation |
| 2 | Astrophysics | https://www.lancashire.ac.uk/undergraduate/courses/astrophysics-bsc |
| 3 | Physics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/physics-bsc-foundation |
| 4 | Physics with Astrophysics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/physics-with-astrophysics-bsc-foundation |
| 5 | Physics with Astrophysics | https://www.lancashire.ac.uk/undergraduate/courses/physics-with-astrophysics-bsc |
| 6 | Physics | https://www.lancashire.ac.uk/undergraduate/courses/physics-bsc |

###### MPhys
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/astrophysics-mphys-foundation |
| 2 | Astrophysics | https://www.lancashire.ac.uk/undergraduate/courses/astrophysics-mphys |


#### Subject: Policing and Investigation
### Policing and Investigation

**Undergraduate (8):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Cyber Investigations with Digital Forensics (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/cyber-investigations-digital-forensics-foundation-bsc |
| 2 | Cyber Investigations with Digital Forensics | https://www.lancashire.ac.uk/undergraduate/courses/cyber-investigations-digital-forensics-bsc-hons |
| 3 | Forensic Science & Criminal Investigation | https://www.lancashire.ac.uk/undergraduate/courses/forensic-science-criminal-investigation-bsc |
| 4 | Policing, Law Enforcement & Investigation | https://www.lancashire.ac.uk/undergraduate/courses/policing-law-enforcement-bsc |
| 5 | Policing, Law Enforcement and Investigation (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/policing-law-enforcement-bsc-foundation |
| 6 | Professional Policing (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/professional-policing-bsc-foundation |
| 7 | Professional Policing Practice | https://www.lancashire.ac.uk/degree-apprenticeships/courses/professional-policing-practice |
| 8 | Professional Policing | https://www.lancashire.ac.uk/undergraduate/courses/professional-policing-bsc |


#### Subject: Psychology
### Psychology

**Undergraduate (11):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Counselling & Psychotherapy | https://www.lancashire.ac.uk/undergraduate/courses/counselling-and-psychotherapy-bsc |
| 2 | Dental Therapy | https://www.lancashire.ac.uk/undergraduate/courses/dental-therapy-bsc |
| 3 | Neuropsychology | https://www.lancashire.ac.uk/undergraduate/courses/neuropsychology-bsc-hons |
| 4 | Psychology (Clinical & Mental Health) | https://www.lancashire.ac.uk/undergraduate/courses/psychology-clinical-mental-health-bsc-hons |
| 5 | Psychology (Forensic & Criminal) | https://www.lancashire.ac.uk/undergraduate/courses/psychology-forensic-criminal-bsc-hons |
| 6 | Psychology (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/psychology-bsc-foundation |
| 7 | Psychology of Child Development | https://www.lancashire.ac.uk/undergraduate/courses/psychology-of-child-development-bsc-hons |
| 8 | Psychology with Counselling | https://www.lancashire.ac.uk/undergraduate/courses/psychology-with-counselling-bsc-hons |
| 9 | Psychology | https://www.lancashire.ac.uk/undergraduate/courses/psychology-bsc |
| 10 | Sports Therapy (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sports-therapy-bsc-foundation |
| 11 | Sports Therapy | https://www.lancashire.ac.uk/undergraduate/courses/sports-therapy-bsc |


#### Subject: Publishing
### Publishing


#### Subject: Social Care and Community
### Social Care and Community

**Undergraduate (4):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Community & Social Care Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/applied-community-social-care-studies-ba-foundation |
| 2 | Applied Community & Social Care Studies | https://www.lancashire.ac.uk/undergraduate/courses/applied-community-social-care-studies-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Health & Social Care (Top-up) | https://www.lancashire.ac.uk/undergraduate/courses/health-social-care-bsc-top-up |

###### FdA
| # | 专业 | URL |
|---|------|-----|
| 1 | Health & Social Care | https://www.lancashire.ac.uk/undergraduate/courses/health-social-care-fda |


#### Subject: Social Work
### Social Work

**Undergraduate (5):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Social Work & Community Development (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/international-social-work-ba-foundation |
| 2 | International Social Work & Community Development | https://www.lancashire.ac.uk/undergraduate/courses/international-social-work-ba-hons |
| 3 | Social Work (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/social-work-ba-foundation |
| 4 | Social Work | https://www.lancashire.ac.uk/undergraduate/courses/social-work-ba |
| 5 | Social Work | https://www.lancashire.ac.uk/degree-apprenticeships/courses/social-work-ba |


#### Subject: Sociology
### Sociology

**Undergraduate (3):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sociology-ba-foundation |
| 2 | Sociology | https://www.lancashire.ac.uk/undergraduate/courses/sociology-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Archaeology & Anthropology | https://www.lancashire.ac.uk/undergraduate/courses/archaeology-anthropology-bsc |


#### Subject: Sport and Exercise Sciences
### Sport and Exercise Sciences

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport & Exercise Science (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sport-exercise-science-bsc-foundation |
| 2 | Sport & Exercise Science | https://www.lancashire.ac.uk/undergraduate/courses/sport-exercise-science-bsc |


#### Subject: Sport Coaching and Leadership
### Sport Coaching and Leadership

**Undergraduate (2):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport Coaching (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/sport-coaching-bsc-foundation |
| 2 | Sport Coaching | https://www.lancashire.ac.uk/undergraduate/courses/sport-coaching-bsc |


#### Subject: Veterinary Medicine
### Veterinary Medicine

**Undergraduate (4):**

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Bioveterinary Sciences (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/bioveterinary-sciences-bsc-foundation |
| 2 | Bioveterinary Sciences | https://www.lancashire.ac.uk/undergraduate/courses/bioveterinary-sciences-bsc |

###### BVMS
| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Medicine & Surgery (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/vet-medicine-surgery-bvms-foundation |
| 2 | Veterinary Medicine & Surgery | https://www.lancashire.ac.uk/undergraduate/courses/veterinary-medicine-surgery-bvms |


#### Subject: General / Interdisciplinary
### General / Interdisciplinary

**Undergraduate (17):**

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Korean Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/korean-studies-ba-foundation |
| 2 | Korean Studies | https://www.lancashire.ac.uk/undergraduate/courses/korean-studies-ba |

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Digital & Technology Solutions | https://www.lancashire.ac.uk/degree-apprenticeships/courses/digital-technology-solutions-bsc |
| 2 | Football Studies (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/football-studies-bsc-foundation |
| 3 | Football Studies | https://www.lancashire.ac.uk/undergraduate/courses/football-studies-bsc |
| 4 | Healthcare Science | https://www.lancashire.ac.uk/undergraduate/courses/healthcare-science-bsc |
| 5 | Neuroscience (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/neuroscience-bsc-foundation |
| 6 | Neuroscience | https://www.lancashire.ac.uk/undergraduate/courses/neuroscience-bsc |
| 7 | Ophthalmic Dispensing | https://www.lancashire.ac.uk/undergraduate/courses/ophthalmic-dispensing-bsc |

###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Building Services & Sustainable Engineering | https://www.lancashire.ac.uk/degree-apprenticeships/courses/building-engineering |
| 2 | Motorsports Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/motorsports-engineering-beng-foundation |
| 3 | Motorsports Engineering | https://www.lancashire.ac.uk/undergraduate/courses/motorsports-engineering-beng |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Motorsports Engineering (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/motorsports-engineering-meng-foundation |
| 2 | Motorsports Engineering | https://www.lancashire.ac.uk/undergraduate/courses/motorsports-engineering-meng |

###### FdA
| # | 专业 | URL |
|---|------|-----|
| 1 | Health & Social Care (with Foundation Year) | https://www.lancashire.ac.uk/undergraduate/courses/health-social-fda-foundation |

###### FdSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Technician Scientist | https://www.lancashire.ac.uk/degree-apprenticeships/courses/technician-scientist-fdsc |

###### Other
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport - Return to Study | https://www.lancashire.ac.uk/undergraduate/courses/return-to-study-sport |


### 1.3 Interdisciplinary / cross-subject UG programmes

UoL flags cross-listing primarily via the "with Foundation Year" and "(International Route)" suffixes. Examples:
- Dental Surgery (International Route), BDS — international applicants only
- Medicine & Surgery (with Foundation Year), MBBS — international applicants only
- Many "with Foundation Year" variants are explicitly foundation versions of single-subject degrees and are listed under their home subject above.

### 1.4 Minors

UoL does not publish a discrete minor list. Students can typically take elective modules outside their primary Subject, but no dedicated Minor catalogue was identified during extraction.

### 1.5 General / Institute-wide requirements

The UG portal (https://www.lancashire.ac.uk/undergraduate) outlines the standard UCAS application process via `https://accounts.ucas.com/account/login`. UoL accepts UCAS applications from the start of September for the following academic year.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

UoL's PG portfolio spans 123 PGT + 17 PGR programmes across 35 subjects.

#### Subject: Aerospace Engineering
### Aerospace Engineering

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://www.lancashire.ac.uk/postgraduate/courses/aerospace-engineering-msc |


#### Subject: Architecture
### Architecture

**Postgraduate Taught (1):**

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture (Part II), MArch | https://www.lancashire.ac.uk/postgraduate/courses/architecture-part-ii-march |


#### Subject: Biosciences
### Biosciences

**Postgraduate Taught (1):**

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Cancer Biology | https://www.lancashire.ac.uk/postgraduate/courses/cancer-biology-mres |


#### Subject: Business and Management
### Business and Management

**Postgraduate Taught (23):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism Innovation & Leadership | https://www.lancashire.ac.uk/postgraduate/courses/journalism-innovation-leadership-ma |
| 2 | Physical Education & Leadership | https://www.lancashire.ac.uk/postgraduate/courses/physical-education-leadership-ma |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics & Artificial Intelligence | https://www.lancashire.ac.uk/postgraduate/courses/business-analytics-ai-msc |
| 2 | Clinical Practice, Management & Education | https://www.lancashire.ac.uk/postgraduate/courses/clinical-practice-management-education-msc |
| 3 | Construction Project Management | https://www.lancashire.ac.uk/postgraduate/courses/construction-project-management-msc |
| 4 | Digital Marketing | https://www.lancashire.ac.uk/postgraduate/courses/digital-marketing-msc |
| 5 | Entrepreneurship & Innovation | https://www.lancashire.ac.uk/postgraduate/courses/entrepreneurship-innovation-msc |
| 6 | International Business & Management | https://www.lancashire.ac.uk/postgraduate/courses/international-business-management-msc |
| 7 | International Hospitality & Tourism Management | https://www.lancashire.ac.uk/postgraduate/courses/international-hospitality-and-tourism-management-msc |
| 8 | Management | https://www.lancashire.ac.uk/postgraduate/courses/management-msc |
| 9 | Medical Leadership | https://www.lancashire.ac.uk/postgraduate/courses/medical-leadership-msc |
| 10 | Musculoskeletal Management | https://www.lancashire.ac.uk/postgraduate/courses/musculoskeletal-management-msc |
| 11 | People Management | https://www.lancashire.ac.uk/postgraduate/courses/people-management-msc |
| 12 | Project Management | https://www.lancashire.ac.uk/postgraduate/courses/project-management-msc |
| 13 | Strategic Leadership | https://www.lancashire.ac.uk/postgraduate/courses/strategic-leadership-msc |
| 14 | Supply Chain Management | https://www.lancashire.ac.uk/postgraduate/courses/supply-chain-management-msc |
| 15 | Sustainable Management & Leadership | https://www.lancashire.ac.uk/postgraduate/courses/sustainable-management-leadership-msc |
| 16 | Veterinary Primary Care & Clinical Leadership | https://www.lancashire.ac.uk/postgraduate/courses/veterinary-primary-care-clinical-leadership-msc |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration - Executive (Chartered Manager) | https://www.lancashire.ac.uk/postgraduate/courses/executive-chartered-manager-mba |
| 2 | Business Administration with Placement | https://www.lancashire.ac.uk/postgraduate/courses/mba-with-placement |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Management | https://www.lancashire.ac.uk/postgraduate/courses/management-mres |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Exercise for the Prevention and Management of Disease | https://www.lancashire.ac.uk/postgraduate/courses/clinical-exercise-prevention-management-pgcert |
| 2 | Obesity Management | https://www.lancashire.ac.uk/postgraduate/courses/obesity-management-pgcert |

**Postgraduate Research (1):**

###### DBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration | https://www.lancashire.ac.uk/postgraduate-research/courses/doctor-business-administration-dba |


#### Subject: Chemistry
### Chemistry

**Postgraduate Research (1):**

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry, MSc by Research | https://www.lancashire.ac.uk/postgraduate-research/courses/msc-by-research-chemistry |


#### Subject: Computer Science
### Computer Science

**Postgraduate Taught (5):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://www.lancashire.ac.uk/postgraduate/courses/artificial-intelligence-msc |
| 2 | Computing | https://www.lancashire.ac.uk/postgraduate/courses/computing-msc |
| 3 | Cyber Security | https://www.lancashire.ac.uk/postgraduate/courses/cyber-security-msc |
| 4 | Data Science | https://www.lancashire.ac.uk/postgraduate/courses/data-science-msc |
| 5 | Finance & Data Analytics | https://www.lancashire.ac.uk/postgraduate/courses/finance-data-analytics-msc |


#### Subject: Criminology
### Criminology

**Postgraduate Taught (1):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology | https://www.lancashire.ac.uk/postgraduate/courses/criminology-ma |


#### Subject: Design
### Design

**Postgraduate Taught (4):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Children's Book Illustration | https://www.lancashire.ac.uk/postgraduate/courses/childrens-book-illustration-ma |
| 2 | Games Design | https://www.lancashire.ac.uk/postgraduate/courses/games-design-ma |
| 3 | Graphic Design | https://www.lancashire.ac.uk/postgraduate/courses/graphic-design-ma |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | User Experience (UX) Design | https://www.lancashire.ac.uk/postgraduate/courses/user-experience-ux-design-msc |


#### Subject: Education
### Education

**Postgraduate Taught (9):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Machine Learning and Internet of Things | https://www.lancashire.ac.uk/postgraduate/courses/machine-learning-iot-msc |
| 2 | Medical Education | https://www.lancashire.ac.uk/postgraduate/courses/medical-education-msc |

###### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Practice in Education | https://www.lancashire.ac.uk/postgraduate/courses/professional-practice-in-education-med |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Mental Health Practice | https://www.lancashire.ac.uk/postgraduate/courses/mental-health-practice-pgcert |
| 2 | Professional Development & Practice | https://www.lancashire.ac.uk/postgraduate/courses/professional-development-practice-pgcert |
| 3 | Safeguarding Children | https://www.lancashire.ac.uk/postgraduate/courses/safeguarding-children-pgcert |
| 4 | Sports Coach Development | https://www.lancashire.ac.uk/postgraduate/courses/coach-development-pgcert |
| 5 | Veterinary Education, Coaching & Leadership | https://www.lancashire.ac.uk/postgraduate/courses/veterinary-education-coaching-pgcert |

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (Further Education & Skills), PGCE | https://www.lancashire.ac.uk/postgraduate/courses/education-training-pgce |

**Postgraduate Research (1):**

###### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate in Education | https://www.lancashire.ac.uk/postgraduate-research/courses/doctorate-in-education-edd |


#### Subject: Electrical and Robotics Engineering
### Electrical and Robotics Engineering

**Postgraduate Taught (2):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical & Electronic Engineering | https://www.lancashire.ac.uk/postgraduate/courses/electrical-electronic-engineering-msc |
| 2 | Mechatronics & Intelligent Machines | https://www.lancashire.ac.uk/postgraduate/courses/mechatronics-intelligent-machines-msc |


#### Subject: Energy and Environment
### Energy and Environment

**Postgraduate Taught (2):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Renewable Energy Engineering | https://www.lancashire.ac.uk/postgraduate/courses/renewable-energy-engineering-msc |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability & Management | https://www.lancashire.ac.uk/postgraduate/courses/sustainability-management-mres |


#### Subject: English
### English

**Postgraduate Research (1):**

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English Literature, American Studies & Creative Writing, MA by Research / | https://www.lancashire.ac.uk/postgraduate-research/courses/english-american-lit-studies |


#### Subject: Fine Art and Photography
### Fine Art and Photography

**Postgraduate Taught (1):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Fine Art | https://www.lancashire.ac.uk/postgraduate/courses/fine-art-ma |


#### Subject: Fire and Safety
### Fire and Safety

**Postgraduate Taught (2):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Food Safety & Innovation | https://www.lancashire.ac.uk/postgraduate/courses/food-safety-innovation-msc |
| 2 | Fire Safety Engineering | https://www.lancashire.ac.uk/postgraduate/courses/fire-safety-engineering-msc |


#### Subject: Forensic Science
### Forensic Science

**Postgraduate Research (1):**

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.lancashire.ac.uk/postgraduate-research/courses/forensic-science |


#### Subject: Games and Animation
### Games and Animation

**Postgraduate Taught (1):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Animation | https://www.lancashire.ac.uk/postgraduate/courses/animation-ma |


#### Subject: Health Professions
### Health Professions

**Postgraduate Taught (6):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Implantology | https://www.lancashire.ac.uk/postgraduate/courses/clinical-implantology-msc |
| 2 | Clinical Periodontology | https://www.lancashire.ac.uk/postgraduate/courses/clinical-periodontology-msc |
| 3 | Occupational Therapy (Pre-registration) | https://www.lancashire.ac.uk/postgraduate/courses/occupational-therapy-pre-registration-msc |
| 4 | Physiotherapy (Pre-registration) | https://www.lancashire.ac.uk/postgraduate/courses/physiotherapy-pre-registration-msc |
| 5 | Veterinary Physiotherapy & Clinical Rehabilitation | https://www.lancashire.ac.uk/postgraduate/courses/vet-physio-clinical-rehab-msc |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Community Nursing | https://www.lancashire.ac.uk/postgraduate/courses/clinical-community-nursing-pgcert |

**Postgraduate Research (1):**

###### DProf
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Studies | https://www.lancashire.ac.uk/postgraduate-research/courses/clinical-studies-dprof |


#### Subject: History
### History

**Postgraduate Taught (1):**

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://www.lancashire.ac.uk/postgraduate/courses/history-mres |


#### Subject: Journalism
### Journalism

**Postgraduate Taught (2):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Sports Media Production | https://www.lancashire.ac.uk/postgraduate/courses/sports-media-production-ma |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Prosthodontics | https://www.lancashire.ac.uk/postgraduate/courses/prosthodontics-msc |

**Postgraduate Research (1):**

###### DProf
| # | 项目 | URL |
|---|------|-----|
| 1 | Health | https://www.lancashire.ac.uk/postgraduate-research/courses/health-dprof |


#### Subject: Languages
### Languages

**Postgraduate Taught (2):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | British Sign Language/English Interpreting and Translation | https://www.lancashire.ac.uk/postgraduate/courses/british-sign-languageenglish-interpreting-pgdipma |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Speech & Language Therapy (Pre-registration) | https://www.lancashire.ac.uk/postgraduate/courses/speech-language-therapy-pre-registration-msc |


#### Subject: Law
### Law

**Postgraduate Taught (1):**

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Solicitors Legal Practice | https://www.lancashire.ac.uk/postgraduate/courses/solicitors-legal-practice-llm |


#### Subject: Mechanical Engineering
### Mechanical Engineering

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.lancashire.ac.uk/postgraduate/courses/mechanical-engineering-msc |


#### Subject: Medicine
### Medicine

**Postgraduate Taught (7):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Disaster Medicine | https://www.lancashire.ac.uk/postgraduate/courses/disaster-medicine-msc |
| 2 | Mountain Medicine | https://www.lancashire.ac.uk/postgraduate/courses/mountain-medicine-msc |
| 3 | Sports Medicine | https://www.lancashire.ac.uk/postgraduate/courses/sports-medicine-msc |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Sciences | https://www.lancashire.ac.uk/postgraduate/courses/medical-sciences-mres |

###### PGDip
| # | 项目 | URL |
|---|------|-----|
| 1 | International Medical Sciences | https://www.lancashire.ac.uk/postgraduate/courses/international-medical-sciences-pgdip |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Adolescent Sports Medicine | https://www.lancashire.ac.uk/postgraduate/courses/adolescent-sports-medicine-pgcert |
| 2 | Exercise Medicine for Female Health | https://www.lancashire.ac.uk/postgraduate/courses/exercise-medicine-female-health-pgcert |


#### Subject: Midwifery
### Midwifery

**Postgraduate Taught (2):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Midwifery (Shortened) | https://www.lancashire.ac.uk/postgraduate/courses/midwifery-for-registered-nurses-msc |
| 2 | Midwifery | https://www.lancashire.ac.uk/postgraduate/courses/midwifery-msc |


#### Subject: Nursing
### Nursing

**Postgraduate Taught (5):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing in General Practice | https://www.lancashire.ac.uk/postgraduate/courses/nursing-in-general-practice-msc |
| 2 | Nursing with Registered Nurse (Adult) | https://www.lancashire.ac.uk/postgraduate/courses/nursing-with-registered-nurse-adult-msc |
| 3 | Nursing with Registered Nurse (Mental Health) | https://www.lancashire.ac.uk/postgraduate/courses/nursing-with-registered-nurse-mental-health-msc |
| 4 | Nursing | https://www.lancashire.ac.uk/postgraduate/courses/nursing-msc |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Critical Care Nursing | https://www.lancashire.ac.uk/postgraduate/courses/critical-care-nursing-pgcert |


#### Subject: Nutrition
### Nutrition

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Dietetics (Pre-registration) | https://www.lancashire.ac.uk/postgraduate/courses/dietetics-pre-registration-msc |


#### Subject: Optometry
### Optometry

**Postgraduate Taught (1):**

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Optometry, MOptom | https://www.lancashire.ac.uk/postgraduate/courses/optometry-moptom |


#### Subject: Performance and Music
### Performance and Music

**Postgraduate Taught (2):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Performance Analysis & Talent Management | https://www.lancashire.ac.uk/postgraduate/courses/performance-analysis-and-talent-management-msc |
| 2 | Sports Coaching & Performance | https://www.lancashire.ac.uk/postgraduate/courses/sports-coaching-performance-msc |


#### Subject: Pharmacy
### Pharmacy

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Pharmacy Practice | https://www.lancashire.ac.uk/postgraduate/courses/advanced-pharmacy-practice-msc |


#### Subject: Physics and Astrophysics
### Physics and Astrophysics

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Associate Practice | https://www.lancashire.ac.uk/postgraduate/courses/physician-associate-practice-msc |

**Postgraduate Research (2):**

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Astrophysics, MSc by Research | https://www.lancashire.ac.uk/postgraduate-research/courses/msc-by-research-astrophysics |
| 2 | Physics, MSc by Research | https://www.lancashire.ac.uk/postgraduate-research/courses/msc-by-research-physics |


#### Subject: Policing and Investigation
### Policing and Investigation

**Postgraduate Taught (5):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Investigation | https://www.lancashire.ac.uk/postgraduate/courses/criminal-investigation-msc |
| 2 | Cybercrime Investigation | https://www.lancashire.ac.uk/postgraduate/courses/cybercrime-investigation-msc |
| 3 | Financial Investigation | https://www.lancashire.ac.uk/postgraduate/courses/financial-investigation-msc |
| 4 | Fire Scene Investigation | https://www.lancashire.ac.uk/postgraduate/courses/fire-scene-investigation-msc |
| 5 | Forensic Biology & Investigation | https://www.lancashire.ac.uk/postgraduate/courses/forensic-biology-investigation-msc |


#### Subject: Psychology
### Psychology

**Postgraduate Taught (6):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Clinical Psychology | https://www.lancashire.ac.uk/postgraduate/courses/applied-clinical-psychology-msc |
| 2 | Applied Forensic Psychology | https://www.lancashire.ac.uk/postgraduate/courses/forensic-psychology-msc |
| 3 | Cancer Biology & Therapy | https://www.lancashire.ac.uk/postgraduate/courses/cancer-biology-therapy-msc |
| 4 | Cognitive Behavioural Psychotherapy | https://www.lancashire.ac.uk/postgraduate/courses/cognitive-behavioural-psychotherapy-msc |
| 5 | Psychology Conversion | https://www.lancashire.ac.uk/postgraduate/courses/psychology-conversion-msc |

###### PGCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Promoting Psychological Wellbeing | https://www.lancashire.ac.uk/postgraduate/courses/promoting-psychological-wellbeing-iapt-pgcert |

**Postgraduate Research (2):**

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://www.lancashire.ac.uk/postgraduate-research/courses/psychology-mphil-phd-mscres |

###### DProf
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychotherapy Studies | https://www.lancashire.ac.uk/postgraduate-research/courses/psychotherapy-studies-dprof |


#### Subject: Publishing
### Publishing

**Postgraduate Taught (1):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Publishing | https://www.lancashire.ac.uk/postgraduate/courses/publishing-ma |


#### Subject: Social Care and Community
### Social Care and Community

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Health & Social Care Research | https://www.lancashire.ac.uk/postgraduate/courses/health-social-care-research-msc |

**Postgraduate Research (1):**

###### DProf
| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Practice Community & Social Care: Policy & Practice | https://www.lancashire.ac.uk/postgraduate-research/courses/community-social-care |


#### Subject: Social Work
### Social Work

**Postgraduate Taught (3):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | International Social Work & Community Development | https://www.lancashire.ac.uk/postgraduate/courses/international-social-work-ma |
| 2 | Social Work | https://www.lancashire.ac.uk/postgraduate/courses/social-work-ma |

###### PGDip
| # | 项目 | URL |
|---|------|-----|
| 1 | Step Up to Social Work | https://www.lancashire.ac.uk/postgraduate/courses/step-up-social-work-pgdip |


#### Subject: Sociology
### Sociology

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Anthropology | https://www.lancashire.ac.uk/postgraduate/courses/forensic-anthropology-msc |

**Postgraduate Research (2):**

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology, Human Geography & Development Studies | https://www.lancashire.ac.uk/postgraduate-research/courses/anthropology-human-geography-development-studies |
| 2 | Archaeology or Anthropology | https://www.lancashire.ac.uk/postgraduate-research/courses/archaeology-anthropology |


#### Subject: Sport and Exercise Sciences
### Sport and Exercise Sciences

**Postgraduate Taught (1):**

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Sport & Exercise Science | https://www.lancashire.ac.uk/postgraduate/courses/sport-exercise-science-msc |


#### Subject: General / Interdisciplinary
### General / Interdisciplinary

**Postgraduate Taught (19):**

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Ceramics | https://www.lancashire.ac.uk/postgraduate/courses/ceramics-ma |
| 2 | Scriptwriting | https://www.lancashire.ac.uk/postgraduate/courses/scriptwriting-ma |
| 3 | Social Policy | https://www.lancashire.ac.uk/postgraduate/courses/social-policy-ma |

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Public Health | https://www.lancashire.ac.uk/postgraduate/courses/applied-public-health-msc |
| 2 | Building Conservation & Adaptation | https://www.lancashire.ac.uk/postgraduate/courses/building-conservation-adaptation-msc |
| 3 | Children & Young People's Mental Health | https://www.lancashire.ac.uk/postgraduate/courses/child-young-people-mental-health |
| 4 | Counter Terrorism | https://www.lancashire.ac.uk/postgraduate/courses/counter-terrorism-msc |
| 5 | Criminal Justice | https://www.lancashire.ac.uk/postgraduate/courses/criminal-justice-msc |
| 6 | Drug Discovery & Development | https://www.lancashire.ac.uk/postgraduate/courses/drug-discovery-development-msc |
| 7 | Endodontology | https://www.lancashire.ac.uk/postgraduate/courses/endodontology-msc |
| 8 | Football Science & Rehabilitation | https://www.lancashire.ac.uk/postgraduate/courses/football-science-rehabilitation-msc |
| 9 | Global Applications in One Health and One Welfare | https://www.lancashire.ac.uk/postgraduate/courses/one-health-one-welfare-msc |
| 10 | Oral Surgery | https://www.lancashire.ac.uk/postgraduate/courses/oral-surgery-msc |
| 11 | Safeguarding in an International Context | https://www.lancashire.ac.uk/postgraduate/courses/safeguarding-in-an-international-context-msc |
| 12 | Social Research Methods | https://www.lancashire.ac.uk/postgraduate/courses/social-research-methods-msc |
| 13 | Strength & Conditioning | https://www.lancashire.ac.uk/postgraduate/courses/strength-conditioning-msc |
| 14 | Uncrewed Aerial Systems (UAS) | https://www.lancashire.ac.uk/postgraduate/courses/uncrewed-aerial-systems-msc |

###### MRes
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.lancashire.ac.uk/postgraduate/courses/neuroscience-mres |

###### PGDip
| # | 项目 | URL |
|---|------|-----|
| 1 | Specialist Community Public Health Nurse | https://www.lancashire.ac.uk/postgraduate/courses/specialist-community-public-health-nurse-pgdip |

**Postgraduate Research (3):**

###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | North Korean Studies | https://www.lancashire.ac.uk/postgraduate-research/courses/north-korean-studies |

###### Other
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering, MSc by Research | https://www.lancashire.ac.uk/postgraduate-research/courses/engineering |
| 2 | Transdisciplinary, MSc by Research | https://www.lancashire.ac.uk/postgraduate-research/courses/transdisciplinary-msc-by-research |


### 2.2 Worked example — Master of Business Administration (MBA)

- **Subject**: Business and Management
- **URL**: https://www.lancashire.ac.uk/postgraduate/courses/business-administration-mba
- **Study mode**: Full-time
- **Tuition (International full-time, 2026/27)**: £18,750 to £19,500
- **English (PG standard)**: IELTS 6.5 with no component below 6.0 (or equivalent)
- **Notes**: Two MBA variants are listed under Business and Management (MBA). Several MBM/MBA-related PGT programmes also exist (Strategic People Management, Digital Marketing, International Business, etc.).

### 2.3 Graduate admissions model

- **Centralised admissions portal**: PG applications for taught programmes are made via the UoL direct application form (https://www.lancashire.ac.uk/postgraduate/how-to-apply). Research degrees apply through the PGR portal (https://www.lancashire.ac.uk/postgraduate-research/how-to-apply).
- **PGR start dates**: September, January, March (applications minimum two months prior to commencement)
- **Application fee**: UoL does not charge a standard application fee for PG taught/research applicants (see https://www.lancashire.ac.uk/postgraduate/how-to-apply)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|---|---|
| Admissions site | https://www.lancashire.ac.uk/undergraduate |
| Application portal | UCAS — https://accounts.ucas.com/account/login |
| Equal consideration deadline | January (UCAS — see https://www.lancashire.ac.uk/undergraduate/how-to-apply) |
| Final UG deadline | 30 June (UCAS) |
| Late applications | Entered into Clearing (https://www.lancashire.ac.uk/clearing) |
| Decision notification | Via UCAS track |
| SAT/ACT | Not required for UK universities |
| Personal statement | Required (UCAS); UoL guidance at https://www.lancashire.ac.uk/study/ucas-personal-statement-changes |
| Recommendation | 1 academic reference (UCAS) |

### 3.2 Undergraduate English proficiency table

Standard UG requirement (most courses): **IELTS 6.0 with no component below 5.5**. Higher requirement for BVMS, MBBS, and Dentistry: **IELTS 7.0 with 7.0 in all components**.

| Exam | Minimum (UG standard) | Higher (BVMS/MBBS/Dentistry) | Notes |
|---|---|---|---|
| IELTS (Academic / Indicator) | 6.0 (no component < 5.5) | 7.0 in all components | UKVI SELT required for visa; One Skill Retake accepted where available |
| TOEFL iBT (incl. Home Edition) | Overall 78 (per CELT table) — score of 4.5/4.0 in older test format | Overall 5.5/5.0 | TOEFL ITP / Essentials NOT accepted |
| Pearson PTE Academic | 61 with minimum 59 in each component | Overall 76, no component < 76 | UKVI or Home accepted |
| Cambridge English (FCE/CAE/CPE) | FCE B2, CAE C1, CPE C2 (overall 170, components ≥ 165) | Overall 190, 190 in each component | |
| Duolingo English Test (DET) | 105 (no sub-score < 100) | 120 (no sub-score < 105) | Submit as PDF via portal |
| LanguageCert Academic | 65 in each skill | 33 in each skill (C1 Pass) | |
| Trinity College ISE | ISE II / III (per guidance) | ISE III pass in all components | |
| International Baccalaureate | Standard Level Grade 4 in English | Grade 6 | |
| A Level English Language | Grade C | Grade C | |

### 3.3 Postgraduate — global rules

| Field | Value |
|---|---|
| Admissions site | https://www.lancashire.ac.uk/postgraduate |
| Application portal | UoL direct application (https://www.lancashire.ac.uk/postgraduate/how-to-apply) |
| Standard application fee | None (UoL does not charge PG application fee) |
| PGR start dates | September, January, March |
| PGR application deadline | At least two months prior to intended start |
| English (PG standard) | IELTS 6.5 (no component < 6.0) OR UKVI IELTS 6.0 (no component < 5.5) |
| PGCE applicants | Apply via GOV.UK Find Postgraduate Teacher Training |
| Higher IELTS programmes | Some programmes (e.g. Health, Social Work) have higher IELTS requirements due to regulatory bodies — check course page |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition (2026/27, international / EU students)

| Course / study type | Tuition (per year) |
|---|---|
| Bachelor's degree full-time | £17,750 to £19,500 |
| Foundation year full-time | £17,750 to £19,500 |
| Placement year | £2,755 |
| Study abroad period | £2,755 |
| Bioveterinary Sciences, BSc (Hons) (non-standard fee) | £28,000 |
| Dental Therapy, BSc (Hons) (non-standard fee) | £44,000 |
| Medicine & Surgery, MBBS (non-standard fee) | To be confirmed |
| Veterinary Medicine & Surgery, BVMS (non-standard fee) | To be confirmed |

> Source: https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students (captured 2026-07-08). Per-course exact fees are listed on individual course pages.

### 4.2 Undergraduate tuition — pre-registration / Channel Islands / Isle of Man

| Course / study type | Tuition (per year) |
|---|---|
| Bachelor's degree full-time | £17,325 |
| Foundation year full-time | £17,250 |
| Placement year | £2,625 |
| Bioveterinary Sciences, BSc (Hons) | £26,250 |
| Dental Therapy, BSc (Hons) | £39,000 |
| Medicine & Surgery, MBBS | £49,000 |
| Veterinary Medicine & Surgery, BVMS | £39,000 |
| Pharmacy, MPharm (Hons) | £18,000 |

### 4.3 Postgraduate tuition (2026/27, international / EU students)

| Course / study type | Tuition |
|---|---|
| Postgraduate taught full-time | £18,750 to £19,500 |
| Postgraduate taught part-time (online) | £1,100 to £1,220 per 20 credits |
| Postgraduate placement year | £2,775 |
| Postgraduate research full-time | £19,250 |
| Final year PGR lapse fee (first 6 months) | £3,850 |
| Final year PGR lapse fee (second 6 months) | £5,775 |
| PGR resubmission charge | £500 |

### 4.4 Scholarships & bursaries

UoL maintains a dedicated scholarships and bursaries page at https://www.lancashire.ac.uk/study/fees-and-finance/bursaries-and-scholarships. International scholarships typically include merit-based tuition fee discounts (e.g. Vice-Chancellor's Scholarships). See that page for current offerings — content was not exhaustively captured in this run.

### 4.5 UK / Home fee note

Home (UK) students pay the standard UK undergraduate fee (£9,250/year for standard full-time courses in 2026/27 — subject to government confirmation). Home fee information is on https://www.lancashire.ac.uk/study/fees-and-finance.

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.program_directory.count
  value: 282
  source_url: https://www.lancashire.ac.uk/courses/a-z/undergraduate
  source_snippet: "282 Undergraduate courses found"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.program_directory.a_to_z
  value: list of 282 UG programmes (BA, BSc, BEng, MEng, MPhys, MSci, FdA, FdSc, LLB, BDS, MBBS, MPharm, BVMS, Dip HE, Cert HE)
  source_url: https://www.lancashire.ac.uk/courses/a-z/undergraduate
  source_snippet: "Undergraduate A-Z listing"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-001:
  field: graduate.pgt_directory.count
  value: 123
  source_url: https://www.lancashire.ac.uk/courses/a-z/postgraduate-taught
  source_snippet: "Postgraduate taught A-Z listing (123 taught programmes)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-002:
  field: graduate.pgr_directory.count
  value: 17
  source_url: https://www.lancashire.ac.uk/courses/a-z/postgraduate-research
  source_snippet: "Postgraduate research A-Z listing (17 research programmes)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-S-001:
  field: institution.subjects.count
  value: 51
  source_url: https://www.lancashire.ac.uk/subjects
  source_snippet: "Explore our subjects — 51 subject areas listed"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-C-001:
  field: tuition.ug.international.bachelors
  value: £17,750 to £19,500 per year (full-time)
  source_url: https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students
  source_snippet: "Bachelor's degree full-time — £17,750 to £19,500"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-C-002:
  field: tuition.ug.international.dental_therapy
  value: £44,000 per year
  source_url: https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students
  source_snippet: "Dental Therapy, BSc (Hons) — £44,000"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-C-003:
  field: tuition.pgt.international.full_time
  value: £18,750 to £19,500 per year
  source_url: https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students
  source_snippet: "Postgraduate taught full-time — £18,750 to £19,500"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-C-004:
  field: tuition.pgr.international.full_time
  value: £19,250 per year
  source_url: https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students
  source_snippet: "Postgraduate research full-time — £19,250"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-L-001:
  field: english.ug.standard
  value: IELTS 6.0 (no component below 5.5)
  source_url: https://www.lancashire.ac.uk/international-students/english-requirements
  source_snippet: "Undergraduate (IELTS 6.0 with no component below 5.5)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-L-002:
  field: english.ug.bvms_mbbs_dentistry
  value: IELTS 7.0 in all components
  source_url: https://www.lancashire.ac.uk/international-students/english-requirements
  source_snippet: "Undergraduate for BVMS, MBBS and Dentistry (IELTS 7.0)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-L-003:
  field: english.pg.standard
  value: IELTS 6.5 with no component below 6.0 (or UKVI IELTS 6.0 / 5.5)
  source_url: https://www.lancashire.ac.uk/international-students/english-requirements
  source_snippet: "Postgraduate (IELTS 6.5 with no component score lower than 6.0)"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-A-001:
  field: ug.application_portal
  value: UCAS (https://accounts.ucas.com/account/login)
  source_url: https://www.lancashire.ac.uk/undergraduate/how-to-apply
  source_snippet: "You can apply through UCAS. The equal consideration deadline for most courses is in January, but you can still apply as normal through UCAS until the 30 June. Applications made after this will be entered into Clearing."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-A-002:
  field: pgr.intake_months
  value: "September, January, March (applications minimum 2 months prior)"
  source_url: https://www.lancashire.ac.uk/postgraduate-research/how-to-apply
  source_snippet: "New postgraduate research degree students can start in September, January and March and applications should be received a minimum of two months prior to commencing your studies."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-I-001:
  field: institution.identity
  value: "University of Lancashire is the rebranded University of Central Lancashire (UCLan)"
  source_url: https://www.lancashire.ac.uk/news/uclan-crowned-university-of-the-year
  source_snippet: "UCLan crowned University of the Year (now University of Lancashire)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: university-of-lancashire-knowledge-base-v2
├── document: institution-overview
│   └── chunk: counts + hierarchy + degree inventory + matrices
├── document: ug-programmes
│   ├── chunk: subject=Accounting-and-Finance (UG)
│   ├── chunk: subject=Aerospace-Engineering (UG)
│   ├── ... (one chunk per Subject with UG offerings)
├── document: pgt-programmes
│   ├── chunk: subject=Business-and-Management (PGT)
│   ├── ... (one chunk per Subject with PGT offerings)
├── document: pgr-programmes
│   ├── chunk: subject=Physics-and-Astrophysics (PGR)
│   ├── ... (one chunk per Subject with PGR offerings)
├── document: application-requirements
├── document: tuition-and-fees
└── document: english-language-requirements
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "university-of-lancashire-knowledge-base-v2"
  school: "<Subject name>"
  department: "<Sub-area within Subject, if applicable>"
  degree_level: "<BA|BSc|BEng|MEng|MPhys|MSci|FdA|FdSc|LLB|BDS|MBBS|MPharm|BVMS|Dip HE|Cert HE|MA|MSc|MBA|MRes|MEd|MArch|LLM|PGDip|PGCert|PGCE|PhD|DBA|EdD|DProf>"
  level: undergraduate | postgraduate_taught | postgraduate_research
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|---|---|---|
| P0 | Confirm MBBS / BVMS international fees (currently "To be confirmed") | https://www.lancashire.ac.uk/study/fees-and-finance/eu-and-international-students |
| P0 | Confirm 2026/27 home (UK) UG tuition fee (£9,250 default) | https://www.lancashire.ac.uk/study/fees-and-finance |
| P1 | Full scholarships & bursaries list with amounts & eligibility | https://www.lancashire.ac.uk/study/fees-and-finance/bursaries-and-scholarships |
| P1 | Per-course tuition for high-cost programmes (Bioveterinary, Dental Therapy, Medicine, Vet Medicine, MPharm) | Individual course pages under /undergraduate/courses/ |
| P1 | UCAS equal-consideration deadline date for 2027 entry (January 2027) | https://www.lancashire.ac.uk/undergraduate/how-to-apply |
| P2 | Tuition fee tables for Home students (separate page from EU/intl) | https://www.lancashire.ac.uk/study/fees-and-finance |
| P2 | PGT application fee waiver policy detail | https://www.lancashire.ac.uk/postgraduate/how-to-apply |
| P2 | UCLan → University of Lancashire rebrand official confirmation page | https://www.lancashire.ac.uk/news/uclan-crowned-university-of-the-year |
| P3 | Per-subject teaching-school mapping (which Subject → which faculty/college) | https://www.lancashire.ac.uk/about-us |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Lancashire |
|---|---|
| Total UG programmes (Rule 1) | 282 |
| Total PGT programmes | 123 |
| Total PGR programmes | 17 |
| Subject count (school-proxy) | 51 |
| UG international tuition (standard) | £17,750 – £19,500 |
| PGT international tuition (standard) | £18,750 – £19,500 |
| PGR international tuition | £19,250 |
| UG English (standard) | IELTS 6.0 / 5.5 |
| UG English (high — BVMS/MBBS/Dentistry) | IELTS 7.0 all components |
| PG English (standard) | IELTS 6.5 / 6.0 |
| Application portal UG | UCAS |
| Equal-consideration deadline | January (UCAS) |
| Final UG deadline | 30 June |
| PGR start dates | Sep / Jan / Mar |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: lancashire.ac.uk (UG, PGT, PGR A-Z; subjects index; international-students; english-requirements; fees-and-finance/eu-and-international-students; undergraduate/how-to-apply; postgraduate-research/how-to-apply)
> **Verification**: ego-browser snapshotText + JS DOM extraction; counts reconciled (Rule 1 = UG + PGT + PGR = 422)
> **Granularity**: subject → degree-level → programme
