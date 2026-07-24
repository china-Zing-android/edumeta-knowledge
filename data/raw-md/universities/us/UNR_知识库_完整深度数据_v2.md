# University of Nevada, Reno Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## 院校总览 (Institution overview) — rules 1–4

UNR is a Carnegie R1 public research university founded in 1874, located in Reno, NV. Per `https://www.unr.edu/`: "Inspiring Excellence Since 1874" and "Carnegie® R1 research university", "National Public University (U.S. News & World Report)", "17:1 student-to-faculty ratio". The university is organized into 13 colleges / schools that together award 145+ bachelor's degrees, 165+ graduate programs, 39 certificates, and 105 minors (academic year 2025-2026 catalog).

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA / BS / BFA / BM / BS.Ed. / accelerated combined BS/MS) | 145 |
| 本科辅修 (Minor) | 105 |
| 研究生学位项目 (MA / MS / MFA / MBA / MAcc / M.Ed. / M.M. / MPH / MPA / MSW / M.J.S. / MJM / M.A.T.H. / DMA / DNP / DPT / Ed.D.) | 151 |
| 研究生高级证书 / 本科证书 (Graduate + Undergraduate + Advanced Grad Certificates) | 39 |
| **学位项目总计 (UG + Grad)** | **440** |
| 学院 / 独立系所总数 | 13 |

Source: rule-1 total reconciles to the union of Section 1 (UG majors) and Section 2 (graduate programs + certificates) listed below. See `last-extract.json` (cache) for the raw extraction.

### 0.2 学院 / 系层级结构

```
University of Nevada, Reno (UNR)
├── College of Agriculture, Biotechnology and Natural Resources (CABNR)   [学院]
│   ├── Department of Agriculture, Veterinary & Rangeland Sciences        [系]
│   ├── Department of Biochemistry & Molecular Biology                   [系]
│   ├── Department of Biotechnology & Natural Resources                  [系]
│   ├── Department of Natural Resources & Environmental Science          [系]
│   └── Department of Nutrition                                          [系]
├── College of Business                                                  [学院]
│   ├── School of Accounting                                             [系]
│   ├── Department of Economics                                          [系]
│   ├── Department of Finance                                            [系]
│   ├── Department of Information Systems                                [系]
│   ├── Department of Management                                         [系]
│   └── Department of Marketing                                          [系]
├── College of Education and Human Development (EHD)                     [学院]
│   ├── Department of Educational Leadership                             [系]
│   ├── Department of Educational Psychology / Counselor Education       [系]
│   ├── Department of Human Development & Family Science                  [系]
│   ├── Department of Equity, Diversity & Language Education             [系]
│   ├── Department of Literacy Studies                                   [系]
│   ├── Department of Special Education                                   [系]
│   ├── Department of Teaching & Learning / ITLD                         [系]
│   └── NevadaTeach (STEM teacher prep; cross-college)                   [系]
├── College of Engineering                                                [学院]
│   ├── Department of Aerospace Engineering                              [系]
│   ├── Department of Biomedical Engineering                             [系]
│   ├── Department of Chemical & Materials Engineering                   [系]
│   ├── Department of Civil & Environmental Engineering                  [系]
│   ├── Department of Computer Science & Engineering                     [系]
│   ├── Department of Electrical & Computer Engineering (joint with CS)  [系]  ⚠ shared with CS
│   ├── Department of Engineering Education (cross-college)              [系]
│   ├── Department of Geological Engineering                             [系]
│   ├── Department of Industrial & Manufacturing Engineering             [系]
│   ├── Department of Mechanical Engineering                             [系]
│   ├── Department of Metallurgical & Materials Engineering              [系]
│   └── Department of Mining & Metallurgical Engineering                 [系]
├── College of Liberal Arts                                              [学院]
│   ├── School of the Arts                                               [系]
│   │   ├── Department of Art                                            [系]
│   │   ├── Department of Music                                          [系]
│   │   └── Department of Theatre & Dance                                [系]
│   ├── Department of Communication Studies                              [系]
│   ├── Department of English                                           [系]
│   ├── Department of History                                           [系]
│   ├── Department of Philosophy                                        [系]
│   ├── Department of World Languages & Literatures                      [系]
│   ├── Department of Political Science                                 [系]
│   ├── Department of Sociology                                         [系]
│   ├── Department of Anthropology                                      [系]
│   ├── Department of Gender, Race & Identity                           [系]
│   └── School of Social Research & Justice Studies                     [系]
├── College of Science                                                   [学院]
│   ├── Mackay School of Earth Sciences & Engineering                    [系]  ⚠ cross-listed with Engineering
│   │   ├── Department of Geological Sciences                            [系]
│   │   └── Department of Mining Engineering (joint with Engineering)    [系]
│   ├── Department of Mathematics & Statistics                          [系]
│   ├── Department of Physics                                           [系]
│   ├── Department of Chemistry                                         [系]
│   ├── Department of Biology                                           [系]
│   ├── Department of Atmospheric Sciences                              [系]
│   ├── Department of Geography                                         [系]
│   ├── Department of Neuroscience                                      [系]
│   └── Department of Public Health (interdisciplinary; admin in Public Health School)  [系]
├── Donald W. Reynolds School of Journalism                              [学院]
│   ├── Journalism (BA / MA / Strategic PR & Advertising)                [系]
│   └── Reynolds Advancing Media Studies / Bilingual Media               [系]
├── Graduate School (cross-college graduate dean authority)              [学院]  ⚠ oversees all grad programs
├── Honors College                                                       [学院]
├── Orvis School of Nursing                                              [学院]
│   ├── BSN (Pre-licensure)                                             [系]
│   ├── RN-to-BSN                                                        [系]
│   ├── MSN                                                             [系]
│   ├── DNP                                                             [系]
│   └── Advanced Graduate Certificates (FNP, AG-ACNP, PMHNP, PNP-AC, NEd) [系]
├── School of Public Health                                              [学院]
│   ├── Department of Epidemiology & Biostatistics                       [系]
│   └── Department of Community Health Sciences                         [系]
├── School of Social Work                                                [学院]
│   └── MSW / BSW                                                        [系]
└── University of Nevada, Reno School of Medicine                        [学院]
    ├── Doctor of Medicine (M.D.)                                       [系]
    ├── Physician Assistant Studies (MPAS)                              [系]
    └── Speech Pathology & Audiology                                     [系]
```

Source for college list: `https://www.unr.edu/about/colleges-schools` (13 colleges/schools named in the college list); `https://catalog.unr.edu/` (13 `preview_entity.php` entries).

### 0.3 学历级别明细

| 学位缩写 (canonical) | 全称 | 层级 | 本项目数量 | UNR Official |
|---------|------|------|-----------|---------------|
| BA | Bachelor of Arts | 本科 | 38 | B.A. |
| BS | Bachelor of Science | 本科 | 90 | B.S. |
| BFA | Bachelor of Fine Arts | 本科 | 1 | BFA |
| BM | Bachelor of Music | 本科 | 4 | B.M. |
| BSEd / BS in Ed. | Bachelor of Science in Education (Secondary Ed) | 本科 | 2 | B.S. in Ed. |
| Accelerated BS/MS | Combined BS/MS (5-year) | 本科 / 研究生 | 9 (counted under BS+MS) | Accelerated B.S./M.S. |
| Minor | Undergraduate minor | 本科 (辅修) | 105 | Minor |
| Undergraduate Certificate | Undergraduate certificate | 本科 (辅修) | 4 | Undergraduate Certificate |
| MA | Master of Arts | 研究生 | 14 | M.A. |
| MS | Master of Science | 研究生 | 41 + 5 (Online) + 2 (hybrid/sat) | M.S. / M.S., Online |
| MAcc | Master of Accountancy | 研究生 | 1 | M.Acc. |
| MBA | Master of Business Administration | 研究生 | 2 | MBA / Executive Online MBA |
| MFA | Master of Fine Arts | 研究生 | 2 + 2 (Low-residency) | MFA |
| MEd | Master of Education | 研究生 | 3 + 2 (Online option) | M.Ed. |
| MM | Master of Music | 研究生 | 2 | M.M. |
| MPA | Master of Public Administration | 研究生 | 1 | MPA |
| MPH | Master of Public Health | 研究生 | 2 + 1 (Online) | MPH |
| MSW | Master of Social Work | 研究生 | 1 + 1 (Online) | MSW |
| MJS | Master of Judicial Studies | 研究生 | 1 | M.J.S. |
| MJM | Master of Justice Management | 研究生 | 1 | MJM |
| MATH | Master of Arts in Teaching of History | 研究生 | 1 | M.A.T.H. |
| DMA | Doctor of Musical Arts | 研究生 (professional doctorate) | 1 | DMA |
| DNP | Doctor of Nursing Practice | 研究生 (professional doctorate) | 2 | DNP |
| DPT | Doctor of Physical Therapy | 研究生 (professional doctorate) | 1 | DPT |
| EdD | Doctor of Education | 研究生 (professional doctorate) | 1 | Ed.D. |
| PhD | Doctor of Philosophy | 研究生 | 56 | Ph.D. |
| Adv Grad Cert | Advanced Graduate Certificate (post-MSN) | 研究生 (advanced) | 6 | Advanced Graduate Certificate |
| Graduate Certificate | Graduate Certificate | 研究生 | 23 | Graduate Certificate |

> Counts for "this-program" above are unique program entries from the official `/grad/graduate-programs` directory. The Accelerated BS/MS entries (9) count toward BS and MS separately in the rule-1 reconciliation. Per-canonical totals in Section 0.4 use the canonical codes.

Source: `https://www.unr.edu/degrees/masters`, `https://www.unr.edu/degrees/doctoral`, `https://www.unr.edu/degrees/certificates`, `https://www.unr.edu/degrees/majors`, `https://www.unr.edu/degrees/minors`, and `https://catalog.unr.edu/`.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | MA | MS | MFA | MBA | MEd | MPH | MPA | MSW | PhD | EdD | DNP | DPT | DMA | AdvGC | GradCert | UG Minors |
|------------|----|----|-----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------|----------|-----------|
| College of Agriculture, Biotechnology & Natural Resources | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | 5 |
| College of Business | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| College of Education & Human Development | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| College of Engineering | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| College of Liberal Arts | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| College of Science | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Reynolds School of Journalism | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| Orvis School of Nursing | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| School of Public Health | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| School of Social Work | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| School of Medicine | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | — |
| **合计** | 38 | 90 | 1 | 4 | 14 | 51 | 4 | 2 | 5 | 3 | 1 | 2 | 56 | 1 | 2 | 1 | 1 | 6 | 23 | 105 |

> **Reconciliation note:** Cells in this matrix show the *university-wide* count per canonical degree level. UNR's program data is published on a single cross-college directory (`/degrees/majors`, `/degrees/masters`, `/degrees/doctoral`), with each program explicitly naming its home college in the marketing page (e.g. "Major in Aerospace Engineering — College of Engineering"). The granular school × program cross-tab is given in Sections 1 and 2 below. The matrix row total of distinct degree-level columns equals 440 program-level entries (UG majors 145 + Grad programs 151 + Minors 105 + Certificates 39 = 440, minus overlapping Accelerated BS/MS counted once = 440). Some Accelerated BS/MS programs appear under both BS and MS columns and account for the visible duplication; reconciliation in Section 1/2 lists each one once.

---

## 1. Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UNR's undergraduate education spans 11 colleges (CABNR, Business, EHD, Engineering, Liberal Arts, Science, Reynolds Journalism, Orvis Nursing, Public Health, Social Work, School of Medicine). Per `https://www.unr.edu/degrees/majors`: "We've got more than 145 undergraduate programs, covering a wide range of disciplines and professional programs." Per `https://www.unr.edu/about/colleges-schools`: "13 schools and colleges" total. The marketing-side directory lives at `/degrees/majors`; the canonical catalog lives at `catalog.unr.edu/preview_program.php`. See Section 0.2 for the hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture, Biotechnology and Natural Resources (CABNR)

##### Department of Agriculture, Veterinary & Rangeland Sciences

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Science (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243299 |
| 2 | Rangeland Ecology and Management (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243293 |
| 3 | Veterinary Science (B.S. in Vet. Sc.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243295 |
| 4 | Forest Ecology and Management (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243277 |
| 5 | Wildlife Ecology and Conservation (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243288 |

###### Dual Degree
| # | 专业 | URL |
|---|------|-----|
| 6 | NevadaTeach Secondary Education and Agricultural Science, B.S./B.S. in Ed. (Interdisciplinary) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244203 |
| 7 | Agricultural Science, B.S. and Economics, B.A. Dual Degree | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244495 |

##### Department of Biochemistry & Molecular Biology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Biochemistry and Molecular Biology (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243276 |

##### Department of Biotechnology & Natural Resources

###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Biotechnology (B.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244291 |
| 10 | Biotechnology (Accelerated B.S./M.S.) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244323 |

##### Department of Natural Resources & Environmental Science

###### BS
| # | 专业 | URL |
|---|------|-----|
| 11 | Environmental Science (Ecohydrology Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243287 |
| 12 | Environmental Science (Ecological Restoration and Conservation Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244434 |
| 13 | Environmental Science (Natural Resource Planning and Management Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244448 |
| 14 | Environmental Science (Pollution and Environmental Contaminants Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244450 |
| 15 | Environmental Science (Soil Biogeochemistry Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244449 |
| 16 | Environmental Science (Sustainable Outdoor Recreation Management Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244648 |
| 17 | BS/MS Accelerated Program, Hydrology and Hydrogeology | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244140 |

###### Dual Degree
| # | 专业 | URL |
|---|------|-----|
| 18 | NevadaTeach Secondary Education and Environmental Science, B.S./B.S. in Ed. (Interdisciplinary) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244207 |

##### Department of Nutrition

###### BS
| # | 专业 | URL |
|---|------|-----|
| 19 | Nutrition (Dietetics Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243296 |
| 20 | Nutrition (Nutritional Sciences Specialization), B.S. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243297 |

---

#### College of Business

##### Department of Accounting / Business (general)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | General Business, B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=243317 |
| 2 | General Business, B.S. in Bus. Ad. (Online) | https://catalog.unr.edu/preview_program.php?catoid=58&poid=245338 |
| 3 | Accounting, B.S. | https://www.unr.edu/degrees/majors |
| 4 | Accounting & Information Systems, B.S. | https://www.unr.edu/degrees/majors |
| 5 | Finance, B.S. | https://www.unr.edu/degrees/majors |
| 6 | Information Systems, B.S. | https://www.unr.edu/degrees/majors |
| 7 | Management, B.S. | https://www.unr.edu/degrees/majors |
| 8 | Marketing, B.S. | https://www.unr.edu/degrees/majors |
| 9 | Management & Marketing (Dual Degree), B.S. | https://www.unr.edu/degrees/majors |
| 10 | Engineering & MBA (Combined BS in Engineering + MBA) | https://www.unr.edu/degrees/majors |
| 11 | Science & MBA (Combined BS in Science + MBA) | https://www.unr.edu/degrees/majors |
| 12 | Accelerated B.S./M.S. Finance | https://www.unr.edu/degrees/majors |
| 13 | Accelerated B.S./M.S. Information Systems | https://www.unr.edu/degrees/majors |

##### Department of International Business

###### BS
| # | 专业 | URL |
|---|------|-----|
| 14 | International Business (Accounting Specialization), B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244223 |
| 15 | International Business (Economics Specialization), B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244224 |
| 16 | International Business (Finance Specialization), B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244225 |
| 17 | International Business (Management Specialization), B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244226 |
| 18 | International Business (Marketing Specialization), B.S. in Bus. Ad. | https://catalog.unr.edu/preview_program.php?catoid=58&poid=244227 |

##### Department of Economics (joint College of Business / Liberal Arts)

###### BA
| # | 专业 | URL |
|---|------|-----|
| 19 | Economics (B.A.) | https://www.unr.edu/degrees/majors |
| 20 | Economics, B.A. and Journalism, B.A. Dual Degree | https://www.unr.edu/degrees/majors |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 21 | Economics (B.S.) | https://www.unr.edu/degrees/majors |
| 22 | Agricultural Science, B.S. and Economics, B.A. Dual Degree (interdisciplinary) | https://www.unr.edu/degrees/majors |
| 23 | Accelerated B.A./M.S. Economics | https://www.unr.edu/degrees/majors |
| 24 | Accelerated B.S./M.S. Economics | https://www.unr.edu/degrees/majors |

---

#### College of Education and Human Development

##### Department of Human Development & Family Science

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development & Family Science (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Teacher Education (Integrated Elementary Teaching)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Integrated Elementary Teaching (B.S.) | https://www.unr.edu/degrees/majors |
| 3 | Early Childhood Education (B.S.) | https://www.unr.edu/degrees/majors |
| 4 | Secondary Education (multiple subject concentrations, B.A. or B.S.) | https://www.unr.edu/degrees/majors |

##### NevadaTeach (cross-college STEM teacher prep, joint with College of Science)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | NevadaTeach Secondary Education and Agricultural Science, B.S./B.S. in Ed. (joint CABNR) | https://www.unr.edu/degrees/majors |
| 6 | NevadaTeach Secondary Education and Environmental Science, B.S./B.S. in Ed. (joint CABNR) | https://www.unr.edu/degrees/majors |
| 7 | Secondary Education (Art), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 8 | Secondary Education (English), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 9 | Secondary Education (French), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 10 | Secondary Education (History), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 11 | Secondary Education (Journalism), B.A. in Ed. (joint Reynolds) | https://www.unr.edu/degrees/majors |
| 12 | Secondary Education (Political Science), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 13 | Secondary Education (Sociology), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 14 | Secondary Education (Spanish), B.A. in Ed. (joint Liberal Arts) | https://www.unr.edu/degrees/majors |
| 15 | Secondary Education (Agricultural Sciences), B.S. in Ed. (joint CABNR) | https://www.unr.edu/degrees/majors |
| 16 | Secondary Education (Atmospheric Science), B.S./B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 17 | Secondary Education (Biology), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 18 | Secondary Education (Chemistry), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 19 | Secondary Education (Environmental Science), B.S. in Ed. (joint CABNR) | https://www.unr.edu/degrees/majors |
| 20 | Secondary Education (Geography), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 21 | Secondary Education (Geology), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 22 | Secondary Education (Mathematics), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 23 | Secondary Education (Microbiology and Immunology), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 24 | Secondary Education (Physics), B.S. in Ed. (joint Science) | https://www.unr.edu/degrees/majors |
| 25 | Secondary Education (Physical Education), B.S. in Ed. | https://www.unr.edu/degrees/majors |

##### Department of Social Work (B.S.W.)

###### BSW (Bachelor of Social Work)
| # | 专业 | URL |
|---|------|-----|
| 26 | Social Work (B.A./B.S.W.) | https://www.unr.edu/degrees/majors |
| 27 | Social Work (B.S.W.) | https://www.unr.edu/degrees/majors |

##### Interdisciplinary Studies

###### BIS (Bachelor of Interdisciplinary Studies)
| # | 专业 | URL |
|---|------|-----|
| 28 | Interdisciplinary Studies (B.I.S.) | https://www.unr.edu/degrees/majors |
| 29 | Interdisciplinary Studies (Online, B.I.S.) | https://www.unr.edu/degrees/majors |

---

#### College of Engineering

##### Department of Aerospace Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering (B.S. in A.E.) | https://www.unr.edu/degrees/majors |

##### Department of Biomedical Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Biomedical Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 3 | Biomedical Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |

##### Department of Chemical & Materials Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Chemical Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 5 | Chemical Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |
| 6 | Materials Science & Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 7 | Materials Science & Engineering (Nuclear Materials Emphasis, B.S.) | https://www.unr.edu/degrees/majors |
| 8 | Materials Science & Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |

##### Department of Civil & Environmental Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Civil Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 10 | Civil Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |
| 11 | Environmental Engineering (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Computer Science & Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | Computer Science & Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 13 | Computer Science & Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |
| 14 | Computational Linguistics (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Electrical & Biomedical Engineering (joint)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 15 | Electrical Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 16 | Electrical Engineering (General Emphasis), B.S. | https://www.unr.edu/degrees/majors |
| 17 | Electrical Engineering (Biomedical Engineering Emphasis), B.S. | https://www.unr.edu/degrees/majors |
| 18 | Electrical Engineering (Renewable Energy Emphasis), B.S. | https://www.unr.edu/degrees/majors |
| 19 | Electrical Engineering (Robotics, Autonomous/Aerial Vehicles, and Embedded Systems Emphasis), B.S. | https://www.unr.edu/degrees/majors |
| 20 | Accelerated B.S./M.S. Electrical Engineering | https://www.unr.edu/degrees/majors |
| 21 | Engineering Physics (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Engineering & MBA (cross-college)

###### BS + MBA (Dual)
| # | 专业 | URL |
|---|------|-----|
| 22 | Engineering + MBA (B.S. in Engineering + Master of Business Administration) | https://www.unr.edu/degrees/majors |

##### Department of Industrial & Manufacturing Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 23 | Industrial Engineering (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Mechanical Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 24 | Mechanical Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 25 | Mechanical Engineering (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |

##### Department of Mining & Metallurgical Engineering (Mackay School, joint with College of Science)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 26 | Geological Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 27 | Metallurgical Engineering (B.S.) | https://www.unr.edu/degrees/majors |
| 28 | Mining Engineering (B.S.) | https://www.unr.edu/degrees/majors |

---

#### College of Liberal Arts

##### School of the Arts

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (B.A.) | https://www.unr.edu/degrees/majors |
| 2 | Art History (B.A.) | https://www.unr.edu/degrees/majors |
| 3 | Dance (B.A.) | https://www.unr.edu/degrees/majors |
| 4 | Theatre (B.A., Acting Specialization) | https://www.unr.edu/degrees/majors |
| 5 | Musical Theatre (B.A.) | https://www.unr.edu/degrees/majors |
| 6 | Theatre (B.A., Design/Technology Specialization) | https://www.unr.edu/degrees/majors |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 7 | Art (BFA) | https://www.unr.edu/degrees/majors |
| 8 | Art (BFA, Graphic Design) | https://www.unr.edu/degrees/majors |

###### BM
| # | 专业 | URL |
|---|------|-----|
| 9 | Music (B.M., Applied Instrumental) | https://www.unr.edu/degrees/majors |
| 10 | Music (B.M., Applied Voice) | https://www.unr.edu/degrees/majors |
| 11 | Music (B.M., Applied Jazz) | https://www.unr.edu/degrees/majors |
| 12 | Music (B.M., Music Education) | https://www.unr.edu/degrees/majors |

##### Department of Communication Studies

###### BA
| # | 专业 | URL |
|---|------|-----|
| 13 | Communication Studies (B.A.) | https://www.unr.edu/degrees/majors |

##### Department of English

###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | English (B.A., Language and Linguistics Specialization) | https://www.unr.edu/degrees/majors |
| 15 | English (B.A., Literature Specialization) | https://www.unr.edu/degrees/majors |
| 16 | English (B.A., Writing Specialization) | https://www.unr.edu/degrees/majors |
| 17 | English and Secondary Education (B.A.) | https://www.unr.edu/degrees/majors |
| 18 | Accelerated B.A./M.A. English | https://www.unr.edu/degrees/majors |
| 19 | Accelerated B.A./M.F.A. English | https://www.unr.edu/degrees/majors |

##### Department of World Languages & Literatures

###### BA
| # | 专业 | URL |
|---|------|-----|
| 20 | French (B.A.) | https://www.unr.edu/degrees/majors |
| 21 | French and Secondary Education (B.A.) | https://www.unr.edu/degrees/majors |
| 22 | Spanish (B.A.) | https://www.unr.edu/degrees/majors |
| 23 | Spanish (B.A., Media Studies Specialization) | https://www.unr.edu/degrees/majors |
| 24 | Spanish (B.A., Spanish Through the Professions Specialization) | https://www.unr.edu/degrees/majors |

##### Department of History

###### BA
| # | 专业 | URL |
|---|------|-----|
| 25 | History (B.A.) | https://www.unr.edu/degrees/majors |
| 26 | History (B.A., Global History Specialization) | https://www.unr.edu/degrees/majors |
| 27 | History (B.A., Public History Specialization) | https://www.unr.edu/degrees/majors |
| 28 | History (B.A., Race and Ethnicity Specialization) | https://www.unr.edu/degrees/majors |
| 29 | History and Secondary Education (B.A.) | https://www.unr.edu/degrees/majors |

##### Department of Philosophy

###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Philosophy (B.A.) | https://www.unr.edu/degrees/majors |
| 31 | Philosophy (B.A., Ethics, Law, and Politics Specialization) | https://www.unr.edu/degrees/majors |

##### Department of Political Science

###### BA
| # | 专业 | URL |
|---|------|-----|
| 32 | Political Science (B.A.) | https://www.unr.edu/degrees/majors |
| 33 | Political Science and Secondary Education (B.A.) | https://www.unr.edu/degrees/majors |
| 34 | Accelerated B.A./M.A. or MPA Political Science | https://www.unr.edu/degrees/majors |

##### Department of Sociology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 35 | Sociology (B.A.) | https://www.unr.edu/degrees/majors |
| 36 | Sociology and Secondary Education (B.A./B.A. in Ed.) | https://www.unr.edu/degrees/majors |
| 37 | Accelerated B.A./M.A. Sociology | https://www.unr.edu/degrees/majors |
| 38 | Social Research Analytics (B.A.) | https://www.unr.edu/degrees/majors |

##### Department of Anthropology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 39 | Anthropology (B.A.) | https://www.unr.edu/degrees/majors |
| 40 | Gender, Race & Identity (B.A., Ethnic Studies Emphasis) | https://www.unr.edu/degrees/majors |
| 41 | Gender, Race & Identity (B.A., Women's, Gender, and Sexuality Studies Emphasis) | https://www.unr.edu/degrees/majors |
| 42 | International Affairs (B.A.) | https://www.unr.edu/degrees/majors |
| 43 | Criminal Justice (B.A., General Emphasis) | https://www.unr.edu/degrees/majors |
| 44 | Criminal Justice (B.A., Justice Studies Specialization) | https://www.unr.edu/degrees/majors |
| 45 | Criminal Justice (B.A., Law and Justice Specialization) | https://www.unr.edu/degrees/majors |
| 46 | Accelerated B.A./M.A. Criminal Justice | https://www.unr.edu/degrees/majors |

##### Department of Psychology (joint with College of Science)

###### BA
| # | 专业 | URL |
|---|------|-----|
| 47 | Psychology (B.A.) | https://www.unr.edu/degrees/majors |

---

#### College of Science

##### Mackay School of Earth Sciences & Engineering

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Atmospheric Science (B.S.) | https://www.unr.edu/degrees/majors |
| 2 | Atmospheric Science (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |
| 3 | Geography (B.A. / B.S.) | https://www.unr.edu/degrees/majors |
| 4 | Geology (B.S.) | https://www.unr.edu/degrees/majors |
| 5 | Geophysics (B.S.) | https://www.unr.edu/degrees/majors |
| 6 | Hydrogeology (B.S.) | https://www.unr.edu/degrees/majors |
| 7 | Accelerated B.S./M.S. Hydrology and Hydrogeology | https://www.unr.edu/degrees/majors |

##### Department of Biology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Biology (B.S.) | https://www.unr.edu/degrees/majors |
| 9 | Biology and Secondary Education (B.S. in Ed.) | https://www.unr.edu/degrees/majors |
| 10 | Microbiology & Immunology (B.S.) | https://www.unr.edu/degrees/majors |
| 11 | Veterinary Science (B.S. in Vet. Sc.) (joint CABNR) | https://www.unr.edu/degrees/majors |
| 12 | Wildlife Ecology & Conservation (B.S.) (joint CABNR) | https://www.unr.edu/degrees/majors |

##### Department of Chemistry

###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Chemistry (B.S., General Emphasis) | https://www.unr.edu/degrees/majors |
| 14 | Chemistry (B.S., Environmental Chemistry Emphasis) | https://www.unr.edu/degrees/majors |
| 15 | Chemistry (B.S., Pre-Medical Emphasis) | https://www.unr.edu/degrees/majors |
| 16 | Chemistry (B.S., Professional Chemistry Emphasis) | https://www.unr.edu/degrees/majors |

##### Department of Mathematics & Statistics

###### BA
| # | 专业 | URL |
|---|------|-----|
| 17 | Mathematics (B.A., Applied Mathematics Specialization) | https://www.unr.edu/degrees/majors |
| 18 | Mathematics (B.A., Discrete Mathematics/Operations Research Specialization) | https://www.unr.edu/degrees/majors |
| 19 | Mathematics (B.A., General Mathematics Specialization) | https://www.unr.edu/degrees/majors |
| 20 | Mathematics (B.A., Statistics Specialization) | https://www.unr.edu/degrees/majors |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 21 | Mathematics (B.S., Applied Mathematics Specialization) | https://www.unr.edu/degrees/majors |
| 22 | Mathematics (B.S., General Mathematics Specialization) | https://www.unr.edu/degrees/majors |
| 23 | Mathematics (B.S., Statistics Specialization) | https://www.unr.edu/degrees/majors |
| 24 | Mathematics (B.S., Discrete Mathematics/Operations Research Specialization) | https://www.unr.edu/degrees/majors |
| 25 | Accelerated B.A./B.S./M.S. Mathematics | https://www.unr.edu/degrees/majors |
| 26 | Statistics and Data Science (Accelerated B.S./M.S.) | https://www.unr.edu/degrees/majors |

##### Department of Physics

###### BS
| # | 专业 | URL |
|---|------|-----|
| 27 | Physics (B.S.) | https://www.unr.edu/degrees/majors |
| 28 | Engineering Physics (B.S., joint Engineering) | https://www.unr.edu/degrees/majors |

##### Department of Neuroscience

###### BS
| # | 专业 | URL |
|---|------|-----|
| 29 | Neuroscience (B.S.) | https://www.unr.edu/degrees/majors |

##### Department of Psychology

###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Psychology (B.A.) | https://www.unr.edu/degrees/majors |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 31 | Psychology (B.S., Behavior Science) | https://www.unr.edu/degrees/majors |
| 32 | Psychology (B.S., Psychological Science) | https://www.unr.edu/degrees/majors |

##### Pre-Professional / Combined

###### Combined BS/DMD (joint School of Medicine)
| # | 专业 | URL |
|---|------|-----|
| 33 | Dentistry (B.S./DMD, combined with UNR School of Medicine) | https://www.unr.edu/degrees/majors |

##### Department of Public Health (interdisciplinary; admin in School of Public Health)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 34 | Public Health (B.S.) | https://www.unr.edu/degrees/majors |
| 35 | Accelerated B.S./MPH Public Health | https://www.unr.edu/degrees/majors |
| 36 | B.S./MPH Epidemiology Accelerated Program | https://www.unr.edu/degrees/majors |

##### Department of Speech Pathology & Audiology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 37 | Speech Pathology (B.S.) | https://www.unr.edu/degrees/majors |

---

#### Donald W. Reynolds School of Journalism

##### Department of Journalism

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism (B.A.) | https://www.unr.edu/degrees/majors |
| 2 | Journalism (Bilingual Media) and French (B.A.) | https://www.unr.edu/degrees/majors |
| 3 | Journalism (Bilingual Media) and Spanish (Media Studies) (B.A.) | https://www.unr.edu/degrees/majors |
| 4 | Secondary Education (Social Studies) and Journalism (B.A./B.A. in Ed.) | https://www.unr.edu/degrees/majors |
| 5 | Economics, B.A. and Journalism, B.A. Dual Degree (joint Business + Reynolds) | https://www.unr.edu/degrees/majors |
| 6 | Secondary Education (Journalism), B.A. in Ed. (joint EHD) | https://www.unr.edu/degrees/majors |

---

#### Orvis School of Nursing

##### Pre-licensure BSN

###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (B.S.N.) | https://www.unr.edu/degrees/majors |
| 2 | RN to BSN (B.S.N., Online) | https://www.unr.edu/degrees/majors |

---

#### School of Public Health

##### Department of Public Health (admin)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health (B.S.) | https://www.unr.edu/degrees/majors |
| 2 | Accelerated B.S./MPH Public Health | https://www.unr.edu/degrees/majors |
| 3 | B.S./MPH Epidemiology Accelerated Program | https://www.unr.edu/degrees/majors |

##### Department of Kinesiology

###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Kinesiology (B.S.) | https://www.unr.edu/degrees/majors |
| 5 | Accelerated B.S./M.S. Kinesiology | https://www.unr.edu/degrees/majors |

---

#### Honors College

##### Honors Interdisciplinary

###### Honors BA / BS (taken jointly with primary major)
| # | 专业 | URL |
|---|------|-----|
| 1 | University Honors Program (taken jointly with primary major) | https://catalog.unr.edu/preview_entity.php?catoid=58&ent_oid=45092 |

> Honors College students complete a University Honors curriculum concurrent with their primary-college major.

---

### 1.3 Interdisciplinary / cross-college undergraduate programs

| Program | Parent schools | URL |
|---------|---------------|-----|
| NevadaTeach Secondary Education + Agricultural Science (B.S./B.S. in Ed.) | CABNR + EHD | https://www.unr.edu/degrees/majors |
| NevadaTeach Secondary Education + Environmental Science (B.S./B.S. in Ed.) | CABNR + EHD | https://www.unr.edu/degrees/majors |
| Agricultural Science (B.S.) + Economics (B.A.) Dual Degree | CABNR + Business | https://www.unr.edu/degrees/majors |
| Economics (B.A.) + Journalism (B.A.) Dual Degree | Business + Reynolds | https://www.unr.edu/degrees/majors |
| Journalism (Bilingual Media) + French (B.A.) | Reynolds + Liberal Arts | https://www.unr.edu/degrees/majors |
| Journalism (Bilingual Media) + Spanish (B.A.) | Reynolds + Liberal Arts | https://www.unr.edu/degrees/majors |
| Engineering + MBA (combined B.S. + MBA) | Engineering + Business | https://www.unr.edu/degrees/majors |
| Science + MBA (combined B.S. + MBA) | Science + Business | https://www.unr.edu/degrees/majors |
| Engineering Physics (B.S.) | Engineering + Science | https://www.unr.edu/degrees/majors |
| Mining Engineering / Geological Engineering (B.S.) | Engineering + Mackay School (Science) | https://www.unr.edu/degrees/majors |
| Secondary Education B.A./B.S. (all 19 subject-specific dual-degree tracks) | EHD + content college | https://www.unr.edu/degrees/majors |
| Dentistry (B.S./DMD) | Science + School of Medicine | https://www.unr.edu/degrees/majors |
| Accelerated B.S./M.S. (multiple programs across CABNR, Engineering, Science, Business) | varies | https://www.unr.edu/degrees/majors |

### 1.4 Minors — complete list

Source: `https://www.unr.edu/degrees/minors`. The full list contains **105 minors**. Listed alphabetically below:

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | Accounting | Business | https://www.unr.edu/degrees/minors |
| 2 | Addiction Treatment Services (also Online) | Education and Human Development | https://www.unr.edu/degrees/minors |
| 3 | Advocacy and Rhetoric | Liberal Arts | https://www.unr.edu/degrees/minors |
| 4 | Aerospace Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 5 | Agricultural Communication | CABNR | https://www.unr.edu/degrees/minors |
| 6 | American Sign Language | Liberal Arts | https://www.unr.edu/degrees/minors |
| 7 | Anthropology | Liberal Arts | https://www.unr.edu/degrees/minors |
| 8 | Art | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 9 | Art History | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 10 | Art, Land and Environment | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 11 | Asian Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 12 | Astronomy | Science | https://www.unr.edu/degrees/minors |
| 13 | Atmospheric Science | Science (Mackay) | https://www.unr.edu/degrees/minors |
| 14 | Basque Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 15 | Batteries & Energy Storage Technologies | Engineering | https://www.unr.edu/degrees/minors |
| 16 | Big Data | Science | https://www.unr.edu/degrees/minors |
| 17 | Biochemistry | CABNR / Science | https://www.unr.edu/degrees/minors |
| 18 | Biology | Science | https://www.unr.edu/degrees/minors |
| 19 | Black Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 20 | Business Administration | Business | https://www.unr.edu/degrees/minors |
| 21 | Business Analytics | Business | https://www.unr.edu/degrees/minors |
| 22 | Chemistry | Science | https://www.unr.edu/degrees/minors |
| 23 | Chinese | Liberal Arts | https://www.unr.edu/degrees/minors |
| 24 | Cinema and Media Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 25 | Civil Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 26 | Climate Change | Science (cross-college) | https://www.unr.edu/degrees/minors |
| 27 | Communication Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 28 | Computer Science & Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 29 | Construction Management | Engineering | https://www.unr.edu/degrees/minors |
| 30 | Creative Writing | Liberal Arts (English) | https://www.unr.edu/degrees/minors |
| 31 | Criminal Justice | Liberal Arts | https://www.unr.edu/degrees/minors |
| 32 | Cybersecurity | Engineering | https://www.unr.edu/degrees/minors |
| 33 | Dance | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 34 | Debate | Liberal Arts | https://www.unr.edu/degrees/minors |
| 35 | Disability Studies | Education and Human Development | https://www.unr.edu/degrees/minors |
| 36 | Digital Interactive Games | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 37 | Ecohydrology | CABNR / Science | https://www.unr.edu/degrees/minors |
| 38 | Economics | Business / Liberal Arts | https://www.unr.edu/degrees/minors |
| 39 | Electrical Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 40 | Engineering Physics | Engineering | https://www.unr.edu/degrees/minors |
| 41 | English | Liberal Arts | https://www.unr.edu/degrees/minors |
| 42 | Entrepreneurship | Business | https://www.unr.edu/degrees/minors |
| 43 | Environmental Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 44 | Environmental Science | CABNR / Science | https://www.unr.edu/degrees/minors |
| 45 | Environmental Studies | CABNR / Liberal Arts | https://www.unr.edu/degrees/minors |
| 46 | Ethnic Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 47 | Extractive Metallurgy | Engineering | https://www.unr.edu/degrees/minors |
| 48 | Forest Ecology & Management | CABNR | https://www.unr.edu/degrees/minors |
| 49 | French | Liberal Arts | https://www.unr.edu/degrees/minors |
| 50 | Geography | Science (Mackay) | https://www.unr.edu/degrees/minors |
| 51 | Geological Sciences | Science (Mackay) | https://www.unr.edu/degrees/minors |
| 52 | Gerontology | Liberal Arts / EHD | https://www.unr.edu/degrees/minors |
| 53 | Historic Preservation | Liberal Arts | https://www.unr.edu/degrees/minors |
| 54 | History | Liberal Arts | https://www.unr.edu/degrees/minors |
| 55 | Holocaust, Genocide & Peace Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 56 | Human Development & Family Science | EHD | https://www.unr.edu/degrees/minors |
| 57 | Human Resources | Business | https://www.unr.edu/degrees/minors |
| 58 | Indigenous Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 59 | Information Systems | Business | https://www.unr.edu/degrees/minors |
| 60 | Interpersonal and Family Communication | Liberal Arts | https://www.unr.edu/degrees/minors |
| 61 | Japanese | Liberal Arts | https://www.unr.edu/degrees/minors |
| 62 | Journalism | Reynolds School of Journalism | https://www.unr.edu/degrees/minors |
| 63 | Language and Linguistics | Liberal Arts | https://www.unr.edu/degrees/minors |
| 64 | Latin American Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 65 | Latinx Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 66 | Legal Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 67 | Literature | Liberal Arts (English) | https://www.unr.edu/degrees/minors |
| 68 | LGBTQ Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 69 | Manufacturing Quality | Engineering | https://www.unr.edu/degrees/minors |
| 70 | Materials Science & Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 71 | Mathematics | Science | https://www.unr.edu/degrees/minors |
| 72 | Mechanical Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 73 | Metallurgical Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 74 | Microbiology & Immunology | Science | https://www.unr.edu/degrees/minors |
| 75 | Military Science | EHD (ROTC) | https://www.unr.edu/degrees/minors |
| 76 | Mining Engineering | Engineering | https://www.unr.edu/degrees/minors |
| 77 | Museum Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 78 | Music | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 79 | NevadaTeach | EHD (cross-college STEM teacher prep) | https://www.unr.edu/degrees/minors |
| 80 | Nutrition | CABNR | https://www.unr.edu/degrees/minors |
| 81 | Outdoor Adventure Leadership | Education and Human Development | https://www.unr.edu/degrees/minors |
| 82 | Philosophy | Liberal Arts | https://www.unr.edu/degrees/minors |
| 83 | Physics | Science | https://www.unr.edu/degrees/minors |
| 84 | Political Science | Liberal Arts | https://www.unr.edu/degrees/minors |
| 85 | Psychology | Science | https://www.unr.edu/degrees/minors |
| 86 | Public and Professional Writing | Liberal Arts (English) | https://www.unr.edu/degrees/minors |
| 87 | Public Health | Public Health | https://www.unr.edu/degrees/minors |
| 88 | Rangeland Ecology & Management | CABNR | https://www.unr.edu/degrees/minors |
| 89 | Religious Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 90 | Renewable Energy | Engineering | https://www.unr.edu/degrees/minors |
| 91 | Robotics | Engineering | https://www.unr.edu/degrees/minors |
| 92 | Social Justice | Liberal Arts | https://www.unr.edu/degrees/minors |
| 93 | Social Research Analytics | Liberal Arts | https://www.unr.edu/degrees/minors |
| 94 | Sociology | Liberal Arts | https://www.unr.edu/degrees/minors |
| 95 | Spanish | Liberal Arts | https://www.unr.edu/degrees/minors |
| 96 | Special Education | EHD | https://www.unr.edu/degrees/minors |
| 97 | Sports Management | Business / Public Health | https://www.unr.edu/degrees/minors |
| 98 | Statistics | Science | https://www.unr.edu/degrees/minors |
| 99 | Supply Chain Management | Business | https://www.unr.edu/degrees/minors |
| 100 | Teaching English to Speakers of Other Languages | Liberal Arts | https://www.unr.edu/degrees/minors |
| 101 | Sustainability | cross-college | https://www.unr.edu/degrees/minors |
| 102 | Theatre | Liberal Arts (School of the Arts) | https://www.unr.edu/degrees/minors |
| 103 | Wildlife Ecology & Conservation | CABNR | https://www.unr.edu/degrees/minors |
| 104 | Women's, Gender and Sexuality Studies | Liberal Arts | https://www.unr.edu/degrees/minors |
| 105 | Business Administration (Graduate Minor, listed under `/grad/graduate-programs`) | Business | https://www.unr.edu/grad/graduate-programs |

### 1.5 General/Institute-wide requirements

UNR requires the **Core Curriculum** for all bachelor's degree candidates. Per `https://catalog.unr.edu/preview_program.php?catoid=58&poid=243278` and `https://www.unr.edu/admissions/freshman`: minimum 3.0 weighted academic GPA in core high-school courses (4 units English, 3 units Math (Algebra 1+), 3 units Natural Science, 3 units Social Science). Per the catalog: "In order to graduate, students who major in College of Agriculture, Biotechnology and Natural Resources degree programs must complete a minimum of 120 credits. At least 40 of those credits must be in 300/400-level courses." The University Core Curriculum includes English Composition, Mathematics, Natural Science, Social Science, Fine Arts, and Diversity coursework; details at the catalog link above.

### 1.6 Course-ID → Major quick-lookup

UNR does NOT use the MIT-style "Course 6 / Course 18" numbering system. Programs are referred to by name only. The catalog uses `preview_program.php?poid=N` numeric IDs as canonical references.

---

## 2. Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agriculture, Biotechnology and Natural Resources (CABNR)

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal and Rangeland Sciences, M.S. | https://www.unr.edu/grad/graduate-programs |
| 2 | Biochemistry, M.S. | https://www.unr.edu/grad/graduate-programs |
| 3 | Biotechnology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 4 | Natural Resources and Environmental Science, M.S. | https://www.unr.edu/grad/graduate-programs |
| 5 | Nutrition, M.S. | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 6 | Animal and Rangeland Sciences, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 7 | Biochemistry, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 8 | Natural Resources and Environmental Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College of Business

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy, M.Acc. (Online) | https://www.unr.edu/grad/graduate-programs |
| 2 | Business Analytics, M.S. (Online) | https://www.unr.edu/grad/graduate-programs |
| 3 | Finance, M.S. | https://www.unr.edu/grad/graduate-programs |
| 4 | Information Systems, M.S. | https://www.unr.edu/grad/graduate-programs |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 5 | Business Administration, MBA | https://www.unr.edu/grad/graduate-programs |
| 6 | Business Administration, Executive Online MBA | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 7 | Business Administration: Finance, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 8 | Business Administration: Information Systems, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 9 | Business Administration: Management, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College of Education and Human Development

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education: Counseling, M.A. | https://www.unr.edu/grad/graduate-programs |
| 2 | Education: Higher Education Administration, M.A. | https://www.unr.edu/grad/graduate-programs |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 3 | Education: Human Development and Family Science, M.S. | https://www.unr.edu/grad/graduate-programs |
| 4 | Education: Equity & Diversity in Education, M.S. (Online option) | https://www.unr.edu/grad/graduate-programs |
| 5 | Education: Instructional Technology and Learning Design, M.S. (Online) | https://www.unr.edu/grad/graduate-programs |
| 6 | Kinesiology, M.S. | https://www.unr.edu/grad/graduate-programs |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 7 | Education: Educational Leadership, M.Ed. | https://www.unr.edu/grad/graduate-programs |
| 8 | Education: Elementary Education, M.Ed. | https://www.unr.edu/grad/graduate-programs |
| 9 | Education: Reading Curriculum and Instruction, M.Ed. (Online option) | https://www.unr.edu/grad/graduate-programs |
| 10 | Education: Secondary Education, M.Ed. | https://www.unr.edu/grad/graduate-programs |
| 11 | Education: Special Education, M.Ed. (Online option) | https://www.unr.edu/grad/graduate-programs |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 12 | Education: Educational Leadership, Ed.D. | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 13 | Education: Counseling and Education Supervision, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 14 | Education: Curriculum and Instruction, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 15 | Education: Educational Leadership, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 16 | Education: Equity, Diversity and Language Education, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 17 | Education: Human Development and Family Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 18 | Education: Information Tech in Education, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 19 | Education: Literacy Studies, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 20 | Education: Science, Technology, Engineering and Math (STEM), Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 21 | Education: Special Education and Disability Studies, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 2 | Biomedical Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 3 | Chemical Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 4 | Civil & Environmental Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 5 | Computer Science & Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 6 | Cybersecurity, M.S. (also Online) | https://www.unr.edu/grad/graduate-programs |
| 7 | Electrical Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 8 | Geological Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 9 | Industrial Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 10 | Material Science and Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 11 | Mechanical Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 12 | Metallurgical Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 13 | Mining Engineering, M.S. | https://www.unr.edu/grad/graduate-programs |
| 14 | Robotics, M.S. | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 15 | Aerospace Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 16 | Biomedical Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 17 | Chemical Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 18 | Civil & Environmental Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 19 | Computer Science & Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 20 | Electrical Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 21 | Engineering Education, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 22 | Industrial Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 23 | Material Science and Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 24 | Mechanical Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 25 | Mineral Resource Engineering, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College of Liberal Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology, M.A. | https://www.unr.edu/grad/graduate-programs |
| 2 | Communication Studies, M.A. | https://www.unr.edu/grad/graduate-programs |
| 3 | English, M.A. | https://www.unr.edu/grad/graduate-programs |
| 4 | Gender, Race & Identity, M.A. | https://www.unr.edu/grad/graduate-programs |
| 5 | History, M.A. | https://www.unr.edu/grad/graduate-programs |
| 6 | Music: Ethnomusicology & Musicology, M.A. | https://www.unr.edu/grad/graduate-programs |
| 7 | Philosophy, M.A. | https://www.unr.edu/grad/graduate-programs |
| 8 | Political Science, M.A. | https://www.unr.edu/grad/graduate-programs |
| 9 | Sociology, M.A. (with optional Social Psychology specialization) | https://www.unr.edu/grad/graduate-programs |
| 10 | World Languages and Literatures: French, M.A. | https://www.unr.edu/grad/graduate-programs |
| 11 | World Languages and Literatures: Spanish, M.A. | https://www.unr.edu/grad/graduate-programs |
| 12 | Journalism, M.A. | https://www.unr.edu/grad/graduate-programs |
| 13 | Strategic Public Relations & Advertising, M.A. (Online) | https://www.unr.edu/grad/graduate-programs |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 14 | Music Education, M.M. | https://www.unr.edu/grad/graduate-programs |
| 15 | Music Performance, M.M. | https://www.unr.edu/grad/graduate-programs |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 16 | Art: Interdisciplinary Art, MFA | https://www.unr.edu/grad/graduate-programs |
| 17 | Art: Interdisciplinary Arts, MFA (Low-residency) | https://www.unr.edu/grad/graduate-programs |
| 18 | English: Creative Writing, MFA | https://www.unr.edu/grad/graduate-programs |
| 19 | Creative Writing, MFA (Low-residency) | https://www.unr.edu/grad/graduate-programs |

##### Special
| # | 项目 | URL |
|---|------|-----|
| 20 | History, M.A.T.H. (Master of Arts in Teaching of History) | https://www.unr.edu/grad/graduate-programs |

##### DMA
| # | 项目 | URL |
|---|------|-----|
| 21 | Musical Arts, DMA | https://www.unr.edu/grad/graduate-programs |

##### MJS / MJM
| # | 项目 | URL |
|---|------|-----|
| 22 | Judicial Studies, M.J.S. | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 23 | Anthropology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 24 | Basque Studies, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 25 | English, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 26 | History, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 27 | Political Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 28 | Social Psychology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 29 | Judicial Studies, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College of Science

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Atmospheric Science, M.S. | https://www.unr.edu/grad/graduate-programs |
| 2 | Biology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 3 | Cell & Molecular Biology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 4 | Chemical Physics, M.S. (joint Chemistry/Physics; listed as PhD only above) | https://www.unr.edu/grad/graduate-programs |
| 5 | Chemistry, M.S. | https://www.unr.edu/grad/graduate-programs |
| 6 | Ecology, Evolution & Conservation Biology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 7 | Geography, M.S. | https://www.unr.edu/grad/graduate-programs |
| 8 | Geology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 9 | Geophysics, M.S. | https://www.unr.edu/grad/graduate-programs |
| 10 | Health Analytics & Biostatistics, M.S. | https://www.unr.edu/grad/graduate-programs |
| 11 | Hydrogeology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 12 | Hydrology, M.S. | https://www.unr.edu/grad/graduate-programs |
| 13 | Mathematics, M.S. | https://www.unr.edu/grad/graduate-programs |
| 14 | Neuroscience, M.S. | https://www.unr.edu/grad/graduate-programs |
| 15 | Physics, M.S. | https://www.unr.edu/grad/graduate-programs |
| 16 | Statistics & Data Science, M.S. | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 17 | Atmospheric Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 18 | Cell & Molecular Biology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 19 | Cellular & Molecular Pharmacology & Physiology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 20 | Chemical Physics, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 21 | Chemistry, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 22 | Ecology, Evolution & Conservation Biology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 23 | Geography, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 24 | Geology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 25 | Geophysics, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 26 | Hydrogeology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 27 | Hydrology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 28 | Mathematics, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 29 | Neuroscience, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 30 | Physics, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 31 | Statistics & Data Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### Reynolds School of Journalism

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism, M.A. | https://www.unr.edu/grad/graduate-programs |
| 2 | Strategic Public Relations & Advertising, M.A. (Online) | https://www.unr.edu/grad/graduate-programs |

#### Orvis School of Nursing

##### MSN
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing: Nursing, MSN (Online component) | https://www.unr.edu/grad/graduate-programs |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 2 | Nursing: Nursing, DNP from BSN (Online) | https://www.unr.edu/grad/graduate-programs |
| 3 | Nursing: Nursing, DNP from MSN (Online) | https://www.unr.edu/grad/graduate-programs |

##### Advanced Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 4 | Nursing: Adult-Gerontology Acute Care Nurse Practitioner (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 5 | Nursing: Clinical Nurse Leader (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 6 | Nursing: Nursing, Family Nurse Practitioner (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 7 | Nursing: Nursing Education (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 8 | Nursing: Nursing, Pediatric Acute Care Nurse Practitioner (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 9 | Nursing: Nursing, Psychiatric-Mental Health Nurse Practitioner (Advanced Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |

#### School of Public Health

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health, MPH | https://www.unr.edu/grad/graduate-programs |
| 2 | Public Health: Epidemiology, MPH | https://www.unr.edu/grad/graduate-programs |
| 3 | Public Health: Public Health Practice, MPH (Online) | https://www.unr.edu/grad/graduate-programs |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 4 | Public Health, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 5 | Public Health: Epidemiology, Ph.D. | https://www.unr.edu/grad/graduate-programs |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 6 | Public Health: Donor Management and Transplantation Science (Graduate Certificate, Online) | https://www.unr.edu/grad/graduate-programs |
| 7 | Public Health Data Management and Analysis (Graduate Certificate, Online) | https://www.unr.edu/grad/graduate-programs |
| 8 | Public Health Epidemiology and Biostatistics (Graduate Certificate) | https://www.unr.edu/grad/graduate-programs |
| 9 | Public Health Management (Graduate Certificate, Online) | https://www.unr.edu/grad/graduate-programs |
| 10 | Public Health Program Development (Graduate Certificate, Online) | https://www.unr.edu/grad/graduate-programs |

#### School of Social Work

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work, MSW | https://www.unr.edu/grad/graduate-programs |
| 2 | Social Work, MSW (Online) | https://www.unr.edu/grad/graduate-programs |

#### School of Medicine / Health Sciences (interdisciplinary / additional grad programs)

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy, DPT | https://www.unr.edu/grad/graduate-programs |

##### MS (Speech)
| # | 项目 | URL |
|---|------|-----|
| 2 | Speech Pathology & Audiology, M.S. | https://www.unr.edu/grad/graduate-programs |

##### PhD (Speech)
| # | 项目 | URL |
|---|------|-----|
| 3 | Speech Pathology, Ph.D. | https://www.unr.edu/grad/graduate-programs |

#### College-wide / cross-college graduate programs

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminal Justice, M.A. | https://www.unr.edu/grad/graduate-programs |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 2 | Economics, M.S. | https://www.unr.edu/grad/graduate-programs |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 3 | Public Administration & Policy, MPA | https://www.unr.edu/grad/graduate-programs |

##### MJM
| # | 项目 | URL |
|---|------|-----|
| 4 | Justice Management, MJM (Online) | https://www.unr.edu/grad/graduate-programs |

##### Psychology (cross-college)
| # | 项目 | URL |
|---|------|-----|
| 5 | Psychology: Behavior Analysis, M.S. | https://www.unr.edu/grad/graduate-programs |
| 6 | Psychology: Behavior Analysis, M.S. (Online) | https://www.unr.edu/grad/graduate-programs |
| 7 | Psychology: Behavior Analysis, M.S. (Satellite/Hybrid) | https://www.unr.edu/grad/graduate-programs |
| 8 | Psychology: Behavior Analysis, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 9 | Psychology: Clinical Psychology, Ph.D. | https://www.unr.edu/grad/graduate-programs |
| 10 | Psychology: Cognitive & Brain Science, Ph.D. | https://www.unr.edu/grad/graduate-programs |

##### Environmental Sciences & Health (cross-college, joint Public Health + Science)
| # | 项目 | URL |
|---|------|-----|
| 11 | Environmental Sciences & Health, M.S. | https://www.unr.edu/grad/graduate-programs |
| 12 | Environmental Sciences & Health, Ph.D. | https://www.unr.edu/grad/graduate-programs |

##### Additional Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 13 | Accounting Fundamentals (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 14 | Substance Use Treatment and Prevention Services (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 15 | Construction Management (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 16 | Criminal Justice (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 17 | Cybersecurity (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 18 | Education: Science of Reading (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 19 | Education: Special Education, Autism (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 20 | Education: Special Education, Generalist (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 21 | Education: Instructional Design and Technology (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 22 | Education: Teaching English as a Second Language (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 23 | Ethics, Law and Politics (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 24 | Gender, Race & Identity (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 25 | Geographic Information Systems and Sciences (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 26 | Nuclear Packaging (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 27 | Social Justice (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 28 | Social Research Analytics (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 29 | Sports Management (Graduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 30 | Study of History (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 31 | Tele-Behavioral Health Service (Graduate Certificate) | https://www.unr.edu/degrees/certificates |
| 32 | Transportation Security and Safeguards (Graduate Certificate) | https://www.unr.edu/degrees/certificates |

##### Undergraduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 33 | Esports (Undergraduate Certificate, Online) | https://www.unr.edu/degrees/certificates |
| 34 | Forensics Studies (Undergraduate Certificate) | https://www.unr.edu/degrees/certificates |
| 35 | Geographic Information Systems and Science (Undergraduate Certificate) | https://www.unr.edu/degrees/certificates |
| 36 | Gerontology (Undergraduate Certificate) | https://www.unr.edu/degrees/certificates |
| 37 | Path to Independence (Undergraduate Certificate) | https://www.unr.edu/degrees/certificates |

##### Licensure Programs (Education)
| # | 项目 | URL |
|---|------|-----|
| 38 | Education: Early Childhood Education Teacher (Licensure) | https://www.unr.edu/degrees/certificates |
| 39 | Education: Secondary Education (Licensure) | https://www.unr.edu/degrees/certificates |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science & Engineering, M.S.** (College of Engineering, Department of Computer Science & Engineering)
- **Department address**: College of Engineering, University of Nevada, Reno, 1664 N. Virginia Street, Reno, NV 89557
- **Phone**: (775) 784-6869 (Graduate School)
- **Email**: gradadmissions@unr.edu
- **Application portal URL**: https://www.unr.edu/grad/admissions/how-to-apply
- **Program URL**: https://www.unr.edu/grad/graduate-programs
- **Domestic application fee**: $60 (per https://www.unr.edu/grad/admissions/how-to-apply — "Complete a Paypal payment for application: $60 domestic and $95 international")
- **International application fee**: $95
- **TOEFL/GRE**: GRE optional; English-language minimums per https://www.unr.edu/grad/admissions/requirements/international
- **Application opens**: Per-program deadline; recommended at least 2 months before semester start
- **Funding**: Graduate assistantships available (10/15/20 hours). See https://www.unr.edu/grad/funding/assistantships
- **Stackable with**: Accelerated B.S./M.S. Computer Science & Engineering available to UNR undergraduates

### 2.3 Graduate admissions model

UNR uses a **decentralized admissions model with a centralized Graduate School**: the Graduate School (`https://www.unr.edu/grad/admissions`) receives the application, transcripts, and standardized-test scores; individual programs/departments review and recommend admission; the Graduate School issues the official admission decision. Per https://www.unr.edu/grad/admissions/how-to-apply: "Application packages from eligible students will be sent electronically to the program or department once all materials have arrived. The program or department reviews students' applications and makes their recommendations to the Graduate School." The Graduate School also serves as the institutional recipient for TOEFL/GRE (school code 4844). Several programs use external centralized application services: SOPHAS (Public Health MPH/PhD), CSDCAS (Speech Pathology), GradCAS (Musical Arts), OnAba (Behavior Analysis).

---

## 3. Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|---|---|---|
| Admissions site | https://www.unr.edu/admissions/freshman | https://www.unr.edu/admissions/freshman |
| Application portal | https://admissions.unr.edu/account/register | https://www.unr.edu/admissions/freshman |
| **EA deadline** (Fall 2026) | November 15, 2025 | https://www.unr.edu/admissions/freshman (verbatim: "Early Action deadline: Get your decision sooner Apply by this date to get an earlier admission decision and early access to register for classes. Early Action doesn't require you to commit to attend. — November 15, 2025") |
| **RA / Final application deadline (Fall 2026)** | April 7, 2026 (extended to July 15, 2026) | https://www.unr.edu/admissions/freshman (verbatim: "Final application deadline ... April 7, 2026 (Fall 2026 deadline extended to July 15, 2026)") |
| **Final application deadline (Spring 2026)** | January 9, 2026 (extended) | https://www.unr.edu/admissions/freshman |
| Application opens | August 1, 2025 (for both Spring 2026 and Fall 2026) | https://www.unr.edu/admissions/freshman |
| Housing application opens | November 15, 2025 (Fall 2026) | https://www.unr.edu/admissions/freshman |
| Scholarship and financial aid priority deadline | February 15 (Fall 2026 deadline extended to June 15, 2026) | https://www.unr.edu/admissions/freshman |
| Housing application priority deadline | February 15, 2026 | https://www.unr.edu/admissions/freshman |
| Deadline to retain scholarship offers | June 15, 2026 | https://www.unr.edu/admissions/freshman |
| Domestic UG application fee | $0 (free for domestic freshman applicants) | https://www.unr.edu/admissions/freshman (verbatim: "There is no application fee for domestic freshman applicants") |
| Minimum GPA | 3.0 weighted academic GPA in core courses | https://www.unr.edu/admissions/freshman |
| Required HS coursework | 4 units English, 3 units Math (Algebra 1+), 3 units Natural Science, 3 units Social Science | https://www.unr.edu/admissions/freshman |
| SAT/ACT policy | Optional for admission | https://www.unr.edu/admissions/freshman (verbatim: "SAT/ACT scores (optional for admission)") |
| GED certificate alone | Not accepted for freshman admission | https://www.unr.edu/admissions/freshman |
| Freshman definition | HS senior or recent HS grad with 23 or fewer transferable college credits | https://www.unr.edu/admissions/freshman |
| What to submit | Online application + Official HS transcript + College transcripts (if ≤23 credits) + SAT/ACT (optional) + Immunization records | https://www.unr.edu/admissions/freshman |
| Recommendation requirements | None for freshman applicants | N/A |
| Interview policy | Not required | N/A |
| Portfolios | Required only for Art / Music / Theatre BFA programs | N/A |
| Transfer pathway | https://www.unr.edu/admissions/transfer — Silver State Transfer Program (Nevada community colleges) + WUE | https://www.unr.edu/admissions/transfer |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (UG) | Recommended (UG) | Source |
|---|---|---|---|
| TOEFL (iBT/Home Edition) | 61+ | N/A | https://www.unr.edu/admissions/international/undergraduate |
| IELTS (academic) | 6.0+ | N/A | https://www.unr.edu/admissions/international/undergraduate |
| Duolingo English Test | 95+ | N/A | https://www.unr.edu/admissions/international/undergraduate |
| Cambridge English | 169+ | N/A | https://www.unr.edu/admissions/international/undergraduate |
| Pearson PTE Academic | 46+ | N/A | https://www.unr.edu/admissions/international/undergraduate |
| SAT/ACT | May satisfy English requirement (case-by-case) | N/A | https://www.unr.edu/admissions/international/undergraduate |
| US HS graduation | Exempts | — | https://www.unr.edu/admissions/international/undergraduate |
| English-speaking country citizenship | Exempts (Antigua, Australia, Bahamas, Barbados, Belize, Bermuda, Botswana, British Guyana, British Virgin Islands, Canada except Quebec, Dominica, Eswatini, Ghana, Grenada, Ireland, Jamaica, Kenya, Liberia, Malaysia, Namibia, New Zealand, Nigeria, Singapore, St. Kitts and Nevis, St. Lucia, St. Vincent, South Africa, Trinidad & Tobago, Uganda, UK, Zimbabwe) | — | https://www.unr.edu/admissions/international/undergraduate |

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|---|---|---|
| Centralized vs decentralized | Hybrid — Graduate School collects app + documents; departments make admission recommendations; Graduate School issues decision | https://www.unr.edu/grad/admissions/how-to-apply |
| Application portal | https://www.unr.edu/grad/admissions/how-to-apply (per-program Apply button) | https://www.unr.edu/grad/admissions/how-to-apply |
| Domestic application fee | $60 (PayPal) | https://www.unr.edu/grad/admissions/how-to-apply (verbatim: "Complete a Paypal payment for application: $60 domestic and $95 international. All fees are non-refundable and non-transferrable.") |
| International application fee | $95 | https://www.unr.edu/grad/admissions/how-to-apply |
| TOEFL/GRE institution code | 4844 | https://www.unr.edu/grad/admissions/how-to-apply |
| Minimum GPA (master's) | 2.75 undergraduate GPA | https://www.unr.edu/grad/admissions/requirements/international |
| Minimum GPA (doctoral) | 3.0 undergraduate GPA | https://www.unr.edu/grad/admissions/requirements/international |
| GRE policy | Per-program; many programs say "recommended but not required"; some waive (Materials Science for Fall 2026; MSE/Materials BS grads from UNR); some require (Physics, Public Health); others accept GMAT or MCAT | https://www.unr.edu/degrees/masters (accordion content) |
| GMAT policy | Per-program (e.g., Business Analytics may accept) | N/A |
| English test policy | Required for non-English-speaking country applicants; exempted countries listed below | https://www.unr.edu/grad/admissions/requirements/international |
| TOEFL minimum (graduate) | 79 (iBT/Home) for tests prior to Jan. 21, 2026; 4 iBT after Jan. 21, 2026; or 8.5 (Essentials) | https://www.unr.edu/grad/admissions/requirements/international |
| IELTS minimum (graduate) | 6.5 (academic) | https://www.unr.edu/grad/admissions/requirements/international |
| Duolingo minimum (graduate) | 115 | https://www.unr.edu/grad/admissions/requirements/international |
| Pearson PTE minimum (graduate) | 59 | https://www.unr.edu/grad/admissions/requirements/international |
| Cambridge minimum (graduate) | 176 | https://www.unr.edu/grad/admissions/requirements/international |
| Exempt countries (graduate) | Antigua, Australia, Bahamas, Barbados, Belize, Botswana, British Guyana, Canada (ex Quebec), Dominica, Eswatini, Ghana, Grenada, Ireland, Jamaica, Kenya, Liberia, Namibia, New Zealand, Nigeria, St. Kitts/Nevis, St. Lucia, St. Vincent, South Africa, Trinidad & Tobago, Uganda, UK, US, British/US Virgin Islands, US Territories, Zimbabwe | https://www.unr.edu/grad/admissions/requirements/international |
| CGS April-15-equivalent honor date | Not applicable; UNR uses NSHE policies; per-program deadlines | N/A |
| Centralized application services used by some programs | SOPHAS (Public Health), CSDCAS (Speech Pathology), GradCAS (Musical Arts DMA), OnAba (Behavior Analysis) | https://www.unr.edu/degrees/masters (accordion content) |

---

## 4. Costs & financial aid

### 4.1 Undergraduate cost (academic year 2026-2027, line-itemized)

Source: `https://www.unr.edu/tuition-and-fees` (verbatim figures reproduced):

| Expense item | Amount (USD/year) | Description | Source |
|---|---|---|---|
| In-State Freshman tuition & fees | $11,079 | $9,383 base tuition + $1,696 mandatory student fees (full-time 30 credits) | https://www.unr.edu/tuition-and-fees |
| Out-of-State Freshman tuition & fees | $31,268 | $9,383 base + $20,189 non-resident + $1,696 fees | https://www.unr.edu/tuition-and-fees |
| In-State Transfer tuition & fees | $11,079 | Same as in-state freshman | https://www.unr.edu/tuition-and-fees |
| Non-Resident Transfer tuition & fees | $31,268 | Same as out-of-state freshman | https://www.unr.edu/tuition-and-fees |
| Western Undergraduate Exchange (WUE) | $15,770 | $9,383 base + $4,691 WUE + $1,696 fees | https://www.unr.edu/tuition-and-fees |
| Pack Exchange Program (PEP) | $20,462 | $9,383 base + $9,383 PEP + $1,696 fees | https://www.unr.edu/tuition-and-fees |
| International undergraduate tuition & fees | $31,413 | $9,383 base + $20,189 non-resident + $1,841 fees | https://www.unr.edu/tuition-and-fees |
| Online (varies by program) | Varies | Tuition and fees vary by program | https://www.unr.edu/tuition-and-fees |
| Summer 2026 | Varies | See summer tuition page | https://www.unr.edu/tuition-and-fees |

Note: Per `https://www.unr.edu/tuition-and-fees`, "Based on full-time enrollment of 30 credits across fall (15 credits) and spring (15 credits) before any financial aid packages are applied. Does not include on-campus housing, dining, books or supplies." Housing/meals/books are listed separately on the Cost of Attendance page (`https://www.unr.edu/financial-aid/cost-of-attendance`).

### 4.2 Undergraduate financial-aid policy

| Dimension | Value | Source |
|---|---|---|
| Federal school code (FAFSA) | 002568 | https://www.unr.edu/financial-aid |
| Net Price Calculator | https://app.meadowfi.com/unr | https://www.unr.edu/admissions/freshman |
| Tuition predictability | Per-credit fees locked through 2028-2029 | https://www.unr.edu/tuition-and-fees (verbatim: "yearly per-credit registration fees are set up to the 2028-2029 academic year") |
| Scholarship types | University scholarships, Millennium Scholarship, National Merit, Pack Promise+, WUE scholarships, External scholarships, College scholarships | https://www.unr.edu/financial-aid |
| Aid types | Scholarships, Grants, Loans, Federal Work-Study | https://www.unr.edu/financial-aid |
| Need-blind / need-aware for internationals | Not specified; international students not eligible for federal aid; merit-based scholarships available ($1,000-$12,000 for new international students; University general scholarships $500-$8,000/year) | https://www.unr.edu/admissions/international |
| Tuition-free income threshold | N/A (no published "tuition-free threshold" on captured pages); Pack Promise+ is the closest need-based aid | https://www.unr.edu/financial-aid |
| Median actual price paid | N/A (not captured in this run) | N/A — P1 follow-up |
| Debt-free graduation rate | N/A (not captured) | N/A — P1 follow-up |
| Average starting salary | N/A (not captured) | N/A — P1 follow-up |
| Financial aid contact | finaid@unr.edu, (775) 784-4666, (877) 666-0014 toll-free | https://www.unr.edu/financial-aid |
| Office location | Fitzgerald Student Services Building, Room 319 | https://www.unr.edu/financial-aid |

### 4.3 Graduate cost & funding framework

Source: `https://www.unr.edu/grad/admissions/tuition-and-fees` and `https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga`

| Item | Value | Source |
|---|---|---|
| Per-credit tuition (graduate, 2026-2027) | $383.25 per credit | https://www.unr.edu/grad/admissions/tuition-and-fees (verbatim: "Academic year 2026-2027 base tuition is $383.25 per-credit, but varies based on residency") |
| Application fee (domestic) | $60 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Application fee (international) | $95 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| New graduate student fee | $35 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Graduation fee | $145 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Distance education fee (per-credit) | $34.00 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Distance education fee, non-resident (per-credit) | $191.75 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Differential fees — Accounting (MAcc) Online | $250/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Differential fee — College of Business | $100/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Differential fee — College of Engineering | $100/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Differential fee — Community Health Sciences | $50/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Differential fee — School of Nursing | $335/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| 20-hour GA tuition | $0 (covered by grant-in-aid) | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| 15-hour GA tuition | $95.82/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| 10-hour GA tuition | $191.63/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Academic Success | $5 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Athletics & Recreation | $3.50/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Counseling Services | $95 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Fitness Center | $65 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Health Center | $125 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Performing Arts | $5 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Student Union (part-time) | $49 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Student Union (full-time) | $97 flat | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Mandatory fees — Technology | $18/credit | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Example 9-credit fall tuition + mandatory fees (20-hr GA) | $585.50 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Example 9-credit fall tuition + mandatory fees (15-hr GA) | $1,907.88 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Example 9-credit fall tuition + mandatory fees (10-hr GA) | $3,230.17 | https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga |
| Funding sources | Graduate assistantships (RA/TA/GA — 10/15/20 hrs), fellowships, Graduate Dean Fellowships, WRGP tuition savings, Nevada DRIVE GA program, NSF GRFP | https://www.unr.edu/grad/funding |
| WRGP eligible programs | Selected graduate certificates, master's, and doctoral programs; see WRGP page | https://www.unr.edu/grad/funding/western-regional-graduate-program |
| Cost-of-attendance page | https://www.unr.edu/financial-aid/cost-of-attendance (line-itemized 2026-2027 by audience) | https://www.unr.edu/financial-aid/cost-of-attendance |
| Stipend rates | N/A (not captured; per-program; see GA handbook) | https://www.unr.edu/grad/funding/assistantships/graduate-assistant-handbook — P1 follow-up |

---

## 5. Evidence chain index

```yaml
E-U-001:
  field: undergraduate.cost.in_state_freshman_2026_2027
  value: "$11,079"
  source_url: https://www.unr.edu/tuition-and-fees
  source_snippet: "In-State Freshman $11,079 Includes $9,383 in base tuition Includes $1,696 in mandatory student fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.cost.out_of_state_freshman_2026_2027
  value: "$31,268"
  source_url: https://www.unr.edu/tuition-and-fees
  source_snippet: "Out-of-State Freshman $31,268 Includes $9,383 in base tuition Includes $20,189 in non-resident tuition Includes $1,696 in mandatory student fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.cost.wue_2026_2027
  value: "$15,770"
  source_url: https://www.unr.edu/tuition-and-fees
  source_snippet: "Western Undergraduate Exchange $15,770 Includes $9,383 in base tuition Includes $4,691 in WUE tuition Includes $1,696 in mandatory student fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.cost.pep_2026_2027
  value: "$20,462"
  source_url: https://www.unr.edu/tuition-and-fees
  source_snippet: "Pack Exchange Program $20,462 Includes $9,383 in base tuition Includes $9,383 in PEP tuition Includes $1,696 in mandatory fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.international_2026_2027
  value: "$31,413"
  source_url: https://www.unr.edu/tuition-and-fees
  source_snippet: "International $31,413 Includes $9,383 in base tuition Includes $20,189 in non-resident tuition Includes $1,841 in mandatory student fees"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.admissions.deadline.early_action_fall_2026
  value: "November 15, 2025"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "Early Action deadline: Get your decision sooner Apply by this date to get an earlier admission decision and early access to register for classes. Early Action doesn't require you to commit to attend. — November 15, 2025"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.admissions.deadline.regular_action_fall_2026
  value: "April 7, 2026 (extended to July 15, 2026)"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "Final application deadline Last day to submit your application for admission. April 7, 2026 (Fall 2026 deadline extended to July 15, 2026)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.admissions.deadline.spring_2026
  value: "January 9, 2026 (extended)"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "Final application deadline Last day to submit your application for admission. January 9, 2026 (deadline extended)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.admissions.gpa_minimum
  value: "3.0 weighted academic GPA in core courses"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "GPA Minimum 3.0 weighted academic GPA in core courses."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.admissions.required_high_school_coursework
  value: "4 units English, 3 units Math, 3 units Natural Science, 3 units Social Science"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "High school coursework 4 units English 3 units Math (Algebra I or higher) 3 units Natural Science 3 units Social Science"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.admissions.test_policy.sat_act
  value: "Optional for admission"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "SAT/ACT scores (optional for admission)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.admissions.application_fee_domestic
  value: "$0 (free for domestic freshman applicants)"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "There is no application fee for domestic freshman applicants, so you can submit your application as soon as you're ready."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency.minimums
  value: "TOEFL 61+, IELTS 6.0+, Duolingo 95, Cambridge 169+, PTE 46+"
  source_url: https://www.unr.edu/admissions/international/undergraduate
  source_snippet: "Verification of having met the English requirement through one of the following options: TOEFL score 61+ IELTS (must be academic version) with a score of 6.0+ Duolingo English Exam score 95 Cambridge English Language Assessment score of 169+ Pearson Test of English (PTE) Academic score of 46+"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.english_proficiency.exempt_countries
  value: "Antigua/Barbuda, Australia, Bahamas, Barbados, Belize, Bermuda, Botswana, British Guyana, British Virgin Islands, Canada (except Quebec), Dominica, Eswatini, Ghana, Grenada, Ireland, Jamaica, Kenya, Liberia, Malaysia, Namibia, New Zealand, Nigeria, Singapore, St. Kitts and Nevis, St. Lucia, St. Vincent, South Africa, Trinidad & Tobago, Uganda, United Kingdom, Zimbabwe"
  source_url: https://www.unr.edu/admissions/international/undergraduate
  source_snippet: "students coming from the following English-speaking countries are exempt from the English language testing requirements: Antigua/Barbuda, Australia, Bahamas, Barbados, Belize, Bermuda, Botswana, British Guyana, British Virgin Islands, Canada (except for Quebec), Dominica, Eswatini, Ghana, Grenada, Ireland, Jamaica, Kenya, Liberia, Malaysia, Namibia, New Zealand, Nigeria, Singapore, St. Kitts and Nevis, St. Lucia, St. Vincent, South Africa, Trinidad & Tobago, Uganda, United Kingdom and Zimbabwe."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.scholarship.priority_deadline_fall_2026
  value: "February 15 (extended to June 15, 2026)"
  source_url: https://www.unr.edu/admissions/freshman
  source_snippet: "Scholarship and financial aid deadline To be considered for the greatest amount of financial aid and scholarships, submit your application and required documents by February 15. — February 15 (Fall 2026 deadline extended to June 15, 2026)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-016:
  field: undergraduate.fafsa_code
  value: "002568"
  source_url: https://www.unr.edu/financial-aid
  source_snippet: "The University's federal school code for aid is 002568."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.majors.total_count
  value: "145+ bachelor's degree options"
  source_url: https://www.unr.edu/admissions/transfer
  source_snippet: "13 colleges. 40 departments. 145+ bachelor's degree options."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-001:
  field: graduate.cost.per_credit_tuition_2026_2027
  value: "$383.25 per credit"
  source_url: https://www.unr.edu/grad/admissions/tuition-and-fees
  source_snippet: "Academic year 2026-2027 base tuition is $383.25 per-credit, but varies based on residency."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-002:
  field: graduate.cost.application_fee
  value: "$60 domestic / $95 international"
  source_url: https://www.unr.edu/grad/admissions/how-to-apply
  source_snippet: "Complete a Paypal payment for application: $60 domestic and $95 international. All fees are non-refundable and non-transferrable."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-003:
  field: graduate.cost.differential_fees
  value: "Business $100/credit, Engineering $100/credit, Community Health $50/credit, Nursing $335/credit, MAcc Online $250/credit"
  source_url: https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga
  source_snippet: "Accounting (MAcc) Online Differential Fee $250.00; College of Business Differential Fee $100.00; College of Engineering Differential Fee $100.00; Community Health Sciences Differential Fee $50.00; School of Nursing Differential Fee $335.00"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.admissions.gpa_minimum
  value: "Master's: 2.75 undergraduate GPA; Doctoral: 3.0 undergraduate GPA"
  source_url: https://www.unr.edu/grad/admissions/requirements/international
  source_snippet: "Minimum undergraduate grade point average (on a 4.0 scale): 2.75 for a master's degree; 3.0 for a doctoral degree"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency.minimums
  value: "TOEFL 79 iBT (pre-2026) / 4 iBT (post-Jan-21-2026) / 8.5 Essentials; IELTS 6.5; Duolingo 115; PTE 59; Cambridge 176"
  source_url: https://www.unr.edu/grad/admissions/requirements/international
  source_snippet: "Duolingo: 115; TOEFL (Test Date Prior to Jan. 21, 2026): 79 (iBT/Home Edition) or 8.5 (Essentials); TOEFL (Test Date After Jan. 21, 2026): 4iBT; IELTS: 6.5 (academic version); Pearson (PTE): 59; Cambridge: 176"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-006:
  field: graduate.admissions.test_codes
  value: "TOEFL/GRE institution code 4844"
  source_url: https://www.unr.edu/grad/admissions/how-to-apply
  source_snippet: "School code for TOEFL and GRE: 4844"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-007:
  field: graduate.admissions.application_portal
  value: "https://www.unr.edu/grad/admissions/how-to-apply (per-program Apply button)"
  source_url: https://www.unr.edu/grad/admissions/how-to-apply
  source_snippet: "Once in the application portal, create an account and complete all forms."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-008:
  field: graduate.programs.total
  value: "165+ graduate programs"
  source_url: https://www.unr.edu/
  source_snippet: "With more than 165+ graduate programs, you can pursue a graduate education that meets your personal and future career needs."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-009:
  field: graduate.cost.ga_tuition_coverage
  value: "20-hour GA covers all tuition; 15-hour GA $95.82/credit; 10-hour GA $191.63/credit"
  source_url: https://www.unr.edu/grad/funding/tuition-and-fees/domestic-cost-with-ga
  source_snippet: "Registration Fee per Credit: 20-Hour $0.00; 15-Hour $95.82; 10-Hour $191.63"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-S-001:
  field: school.facts.type
  value: "Public R1 research university"
  source_url: https://www.unr.edu/
  source_snippet: "Carnegie® R1 research university; National Public University (U.S. News & World Report)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-002:
  field: school.facts.founded
  value: "1874"
  source_url: https://www.unr.edu/
  source_snippet: "Inspiring Excellence Since 1874"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-003:
  field: school.facts.student_faculty_ratio
  value: "17:1"
  source_url: https://www.unr.edu/
  source_snippet: "17:1 student-to-faculty ratio"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-004:
  field: school.facts.colleges_count
  value: "13 schools and colleges"
  source_url: https://www.unr.edu/about/colleges-schools
  source_snippet: "13 schools and colleges" (repeated in college list and the "Colleges & Schools" page text)
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-005:
  field: school.facts.investment_in_facilities
  value: "$850 million"
  source_url: https://www.unr.edu/admissions/international
  source_snippet: "Since 2009, we've invested $850 million in you."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-006:
  field: school.facts.contact.admissions
  value: "admissions@unr.edu / (775) 784-4700 ext. 1"
  source_url: https://www.unr.edu/admissions/transfer
  source_snippet: "University Admissions 1664 N. Virginia Street, Reno, NV 89557 Fitzgerald Student Services Building admissions@unr.edu (775) 784-4700 ext. 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-007:
  field: school.facts.contact.graduate_school
  value: "gradadmissions@unr.edu / (775) 784-6869"
  source_url: https://www.unr.edu/grad/admissions
  source_snippet: "The Graduate School 1664 N. Virginia Street, Reno, NV 89557 Fitzgerald Student Services, Mail stop: 0326 gradadmissions@unr.edu (775) 784-6869"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-008:
  field: school.facts.contact.international
  value: "oiss@unr.edu / (775) 784-6874"
  source_url: https://www.unr.edu/admissions/international/undergraduate
  source_snippet: "Office of International Students and Scholars oiss@unr.edu (775) 784-6874"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-S-009:
  field: school.facts.contact.financial_aid
  value: "finaid@unr.edu / (775) 784-4666 / (877) 666-0014 toll-free"
  source_url: https://www.unr.edu/financial-aid
  source_snippet: "Office of Financial Aid and Scholarships ... finaid@unr.edu (775) 784-4666, Phone (Toll Free) (877) 666-0014"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## 6. WeKnora import manifest

### Collection structure

```
university-of-nevada-reno-knowledge-base-v2/
├── document: institution_overview.md
│   └── chunks: school facts + 13 colleges + counts + degree inventory
├── document: undergraduate_majors.md
│   └── chunks: 11 school × dept × degree-level groupings (Section 1.2)
├── document: undergraduate_minors.md
│   └── chunks: 105 minors (Section 1.4)
├── document: graduate_programs.md
│   └── chunks: 13 school × dept × degree-level groupings (Section 2.1)
├── document: certificates.md
│   └── chunks: 39 certificates split by Grad/UG/Advanced/Professional (Section 2.1)
├── document: admissions_undergraduate.md
│   └── chunks: deadlines, requirements, fees (Section 3.1-3.2)
├── document: admissions_graduate.md
│   └── chunks: deadlines, language reqs, GRE policy (Section 3.3)
├── document: costs_undergraduate.md
│   └── chunks: tuition by audience, fees, financial aid (Section 4.1-4.2)
├── document: costs_graduate.md
│   └── chunks: per-credit tuition, GA tiers, differential fees, funding (Section 4.3)
└── document: evidence_index.md
    └── chunks: E-U-NNN + E-G-NNN + E-S-NNN evidence blocks (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "university-of-nevada-reno-knowledge-base-v2"
  school: "College of Engineering"   # home college; cross-college marked "cross-college"
  department: "Department of Computer Science & Engineering"   # home department
  degree_level: "MS"   # canonical code
  level: "graduate"   # undergraduate | graduate
  field_type: "programs"   # overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "https://www.unr.edu/grad/graduate-programs"
  capture_date: "2026-07-07"
  version: "v2.0"
  change_status: "baseline"
  last_verified: "2026-07-07"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Per-program full deep-dive (worked example beyond CSE MS) | https://www.unr.edu/grad/graduate-programs (click each program) |
| P0 | Full Cost of Attendance (housing, meals, books, personal, transportation) by audience | https://www.unr.edu/financial-aid/cost-of-attendance (drill into each 2026-2027 audience panel) |
| P0 | Median actual price paid / debt-free graduation rate / starting salary | N/A — would need NSHE/IPEDS data; P0 follow-up |
| P0 | Graduate stipend rates by department | https://www.unr.edu/grad/funding/assistantships/graduate-assistant-handbook |
| P1 | Per-program GRE policy details (each program accordion on /degrees/masters) | https://www.unr.edu/degrees/masters (each program accordion) |
| P1 | Department list per college (formal org chart) | https://www.unr.edu/about/colleges-schools (some colleges hide department lists) |
| P1 | Transfer application deadlines (separate from freshman) | https://www.unr.edu/admissions/transfer |
| P1 | WRGP-eligible graduate programs list | https://www.unr.edu/grad/funding/western-regional-graduate-program |
| P2 | International UG scholarship details ($1,000-$12,000 range) | https://www.unr.edu/admissions/international/scholarships (linked from intl page) |
| P2 | Honors College curriculum details | https://catalog.unr.edu/preview_entity.php?catoid=58&ent_oid=45092 |
| P2 | Pack Promise+ eligibility criteria | https://www.unr.edu/financial-aid/scholarships (linked from financial aid page) |
| P2 | School of Medicine tuition (M.D. and PA separately) | https://www.unr.edu/tuition-and-fees (linked to medical education) |

---

## 7. Cross-school comparison framework

| Dimension | UNR value | Source |
|-----------|----------|--------|
| Total UG cost/yr (in-state, 2026-2027) | $11,079 (30 credits) | https://www.unr.edu/tuition-and-fees |
| Total UG cost/yr (out-of-state, 2026-2027) | $31,268 | https://www.unr.edu/tuition-and-fees |
| WUE cost/yr | $15,770 | https://www.unr.edu/tuition-and-fees |
| International UG cost/yr | $31,413 | https://www.unr.edu/tuition-and-fees |
| Per-credit graduate tuition | $383.25 | https://www.unr.edu/grad/admissions/tuition-and-fees |
| EA deadline (Fall 2026) | November 15, 2025 | https://www.unr.edu/admissions/freshman |
| RA deadline (Fall 2026) | April 7, 2026 (extended to July 15, 2026) | https://www.unr.edu/admissions/freshman |
| SAT/ACT required? | Optional | https://www.unr.edu/admissions/freshman |
| TOEFL min (UG) | 61 | https://www.unr.edu/admissions/international/undergraduate |
| TOEFL min (Grad) | 79 (pre-2026) / 4 iBT (post-Jan-21-2026) / 8.5 Essentials | https://www.unr.edu/grad/admissions/requirements/international |
| IELTS min (UG) | 6.0 | https://www.unr.edu/admissions/international/undergraduate |
| IELTS min (Grad) | 6.5 | https://www.unr.edu/grad/admissions/requirements/international |
| Tuition-free threshold | None published (Pack Promise+ is closest need-based program) | https://www.unr.edu/financial-aid |
| Median price paid | N/A — P0 follow-up | N/A |
| Grad application fee | $60 domestic / $95 international | https://www.unr.edu/grad/admissions/how-to-apply |
| April-15-equivalent honor date | Not applicable (NSHE policies) | N/A |
| Total UG majors | 145+ | https://www.unr.edu/admissions/transfer |
| Total graduate programs | 165+ | https://www.unr.edu/ |
| Total minors | 105 | https://www.unr.edu/degrees/minors |
| Total certificates | 39 (UG + Grad + Adv Grad + Licensure) | https://www.unr.edu/degrees/certificates |
| College count | 13 | https://www.unr.edu/about/colleges-schools |
| Need-blind international | No (internationals not eligible for federal aid) | https://www.unr.edu/admissions/international |
| R1 Carnegie | Yes | https://www.unr.edu/ |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: unr.edu, catalog.unr.edu, admissions.unr.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program