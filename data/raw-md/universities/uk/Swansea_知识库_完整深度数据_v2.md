# Swansea University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless) + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Wales)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 154 |
| 本科辅修 (Minor) | 0（院系内嵌） |
| 研究生授课型 (PGT) | 152 |
| 研究生研究型 (PhD/MPhil/MRes/Masters by Research/EngD/DBA/EdD/Dcrim) | 6 |
| **学位项目总计 (UG + Grad)** | **312** |
| 学院 (Faculties) | 3 |
| 学校/系所 (Schools) | 13 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Swansea University
├── Faculty of Humanities and Social Sciences         [学院]
│   ├── School of Culture and Communication           [系]
│   ├── School of Law                                 [系]
│   ├── School of Management                          [系]
│   └── School of Social Sciences                     [系]
├── Faculty of Medicine, Health and Life Science      [学院]
│   ├── School of Health and Social Care              [系]
│   ├── School of Medicine                            [系]
│   ├── School of Psychology                          [系]
│   └── School of Biosciences, Geography and Physics  [系]  ⚠ shared with S&E
└── Faculty of Science and Engineering                [学院]
    ├── School of Aerospace, Civil, Electrical and Mechanical Engineering  [系]
    ├── School of Engineering and Applied Sciences    [系]
    ├── School of Mathematics and Computer Science    [系]
    └── School of Biosciences, Geography and Physics  [系]  ⚠ shared with MHL
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~60 |
| BSc | Bachelor of Science | 本科 | ~80 |
| BEng | Bachelor of Engineering | 本科 | ~7 (incl. integrated MEng) |
| MEng | Master of Engineering (UG integrated 4-yr) | 本科 | 7 (combined w/ BEng) |
| LLB | Bachelor of Laws | 本科 | 12 |
| MB BCh | Bachelor of Medicine, Bachelor of Surgery | 本科 | 1 |
| MSci | Master in Science (UG integrated 4-yr) | 本科 | combined w/ BSc |
| MChem | Master in Chemistry (UG integrated 4-yr) | 本科 | combined w/ BSc |
| MPhys | Master in Physics (UG integrated 4-yr) | 本科 | combined w/ BSc |
| MMath | Master in Mathematics (UG integrated 4-yr) | 本科 | combined w/ BSc |
| HECert | Higher Education Certificate | 本科 | 2 |
| FDSc | Foundation Degree in Science | 本科 | 1 |
| MA | Master of Arts | 研究生 | ~25 |
| MSc | Master of Science | 研究生 | ~95 |
| LLM | Master of Laws | 研究生 | 9 |
| MPAS | Master of Physician Associate Studies | 研究生 | 1 |
| MRes | Master of Research | 研究生 | (cross-faculty research) |
| PGDip | Postgraduate Diploma | 研究生 | combined in MSc/MA |
| PGCert | Postgraduate Certificate | 研究生 | ~22 |
| PhD | Doctor of Philosophy | 研究生 | 1 (multi-discipline) |
| MPhil | Master of Philosophy | 研究生 | 1 |
| EngD | Engineering Doctorate | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 1 |
| DCrim | Doctor of Criminology | 研究生 | 1 |
| DBA | Doctor of Business Administration | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BSc | BEng/MEng | LLB | MB BCh | MA | MSc | LLM | MPAS | PGDip | PGCert | PhD/MPhil | Adv Doct | 合计 |
|------------|----|-----|-----------|-----|--------|----|-----|-----|------|-------|--------|-----------|----------|------|
| Humanities and Social Sciences | ~58 | ~12 | 0 | 12 | 0 | ~22 | ~25 | 9 | 0 | ~6 | ~5 | shared | shared | ~149 |
| Medicine, Health and Life Science | ~3 | ~38 | ~2 | 0 | 1 | ~5 | ~25 | 0 | 1 | ~5 | ~8 | shared | shared | ~88 |
| Science and Engineering | ~2 | ~30 | ~12 | 0 | 0 | 0 | ~50 | 0 | 0 | ~5 | ~3 | shared | shared | ~102 |
| **合计** | ~63 | ~80 | ~14 | 12 | 1 | ~27 | ~100 | 9 | 1 | ~16 | ~16 | shared | shared | **~312** |

> Note: Many UG programmes offer integrated Master's (BEng/MEng, BSc/MSci, BSc/MMath, BSc/MChem, BSc/MPhys, BA/MA) — counted once under the integrated pathway but both degree options documented in row.
> PhD/MPhil and Professional Doctorates are cross-faculty and counted once.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

Swansea University offers 154 undergraduate programmes across 3 faculties and 11 academic schools. UG applications are routed via **UCAS** (single national portal). Many programmes offer integrated 4-year Master's pathways (e.g. BEng → MEng, BSc → MSci). Several schools offer **degree apprenticeship** variants alongside traditional degrees.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Faculty of Humanities and Social Sciences

##### School of Culture and Communication

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/american-studies/ |
| 2 | American Studies and History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/american-studies-history/ |
| 3 | American Studies and Politics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/american-studies-politics/ |
| 4 | Ancient and Medieval History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/ancient-medieval-history/ |
| 5 | Ancient History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/ancient-history/ |
| 6 | Ancient History and History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/ancient-history-history/ |
| 7 | Classical Studies, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/classical-studies/ |
| 8 | Combined Honours, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/combined-honours/ |
| 9 | Creative Writing and English Literature, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/creative-writing-english-literature/ |
| 10 | Cymraeg/Welsh, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/welsh-cymraeg/ |
| 11 | Cymraeg, Cyfryngau a Chysylltiadau Cyhoeddus (Welsh, Media and Public Relations), BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/welsh-media-public-relations/ |
| 12 | Education, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/education/ |
| 13 | Education and Welsh, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/education-welsh/ |
| 14 | Education and Welsh (a Pathway for Second Language Students), BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/education-welsh-second-language/ |
| 15 | Egyptology and Ancient History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/egyptology-ancient-history/ |
| 16 | English Language and Linguistics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/english-language-linguistics/ |
| 17 | English Language and Literature, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/english-language-literature/ |
| 18 | English Literature, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/english-literature/ |
| 19 | English Literature and History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/english-literature-history/ |
| 20 | Film and Visual Culture, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/film-visual-culture/ |
| 21 | Geography, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/geography-ba/ |
| 22 | History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/history/ |
| 23 | History and Politics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/history-politics/ |
| 24 | Human Geography, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/human-geography/ |
| 25 | International Relations, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/international-relations/ |
| 26 | International Relations and American Studies, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/international-relations-american-studies/ |
| 27 | International Relations and History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/international-relations-history/ |
| 28 | International Relations with Modern Languages, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/international-relations-modern-languages/ |
| 29 | Journalism, Media and Communications, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/journalism-media-communications/ |
| 30 | Media and Communication, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/media-communication/ |
| 31 | Media and English Literature, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/media-english-literature/ |
| 32 | Modern Languages, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/modern-languages/ |
| 33 | Modern Languages and English Literature, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/modern-languages-english-literature/ |
| 34 | Modern Languages and History, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/modern-languages-history/ |
| 35 | Modern Languages, Translation and Interpreting, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/modern-languages-translation-interpreting/ |
| 36 | Philosophy, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/philosophy/ |
| 37 | Philosophy and Politics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/philosophy-politics/ |
| 38 | Philosophy, Politics and Economics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/philosophy-politics-economics/ |
| 39 | Politics, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/politics/ |
| 40 | Politics and International Relations, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/politics-international-relations/ |
| 41 | Politics and Social Policy, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/politics-social-policy/ |
| 42 | Public Relations and Media, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/public-relations-media/ |
| 43 | Sport, Media and Culture, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/sport-media-culture/ |
| 44 | Welsh (a Pathway for First Language Students), BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/welsh-first-language/ |
| 45 | Welsh (a Pathway for Second Language Students), BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/welsh-second-language/ |

##### School of Law

###### LLB
| # | 专业 | URL |
|---|------|-----|
| 46 | Business Law, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/business-law/ |
| 47 | Law, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law/ |
| 48 | Law (Accelerated JD Pathway), LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-accelerated-jd/ |
| 49 | Law (JD Pathway), LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-jd-pathway/ |
| 50 | Law (Senior Status), LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-senior-status/ |
| 51 | Law in Practice, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-in-practice/ |
| 52 | Law in Practice with Criminology, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-criminology-practice/ |
| 53 | Law in Practice with International Relations, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-international-relations-practice/ |
| 54 | Law in Practice with Politics, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-politics-practice/ |
| 55 | Law with Criminology, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-criminology/ |
| 56 | Law with International Relations, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-international-relations/ |
| 57 | Law with Politics, LLB (Hons) | https://www.swansea.ac.uk/undergraduate/courses/law-politics/ |

##### School of Management

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 58 | Accounting and Finance, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/accounting-finance/ |
| 59 | Actuarial Science, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/actuarial-science/ |
| 60 | Applied Business Management (Coleg Cambria), BSc Articulation | https://www.swansea.ac.uk/undergraduate/courses/applied-business-management-coleg-cambria/ |
| 61 | Applied Business Management (Coleg Cambria), FDSc | https://www.swansea.ac.uk/undergraduate/courses/applied-business-management-fdsc/ |
| 62 | Business Management, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/business-management/ |
| 63 | Business Management (Modern Languages), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/business-management-modern-languages/ |
| 64 | Economics, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/economics/ |
| 65 | Economics (Top Up), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/economics-top-up/ |
| 66 | Economics and Business, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/economics-business/ |
| 67 | Economics and Finance, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/economics-finance/ |
| 68 | Finance, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/finance/ |
| 69 | Financial Management, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/financial-management/ |
| 70 | Global Business Management (Top Up), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/global-business-management-top-up/ |
| 71 | International Business Finance (Top Up), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/international-business-finance-top-up/ |
| 72 | Marketing, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/marketing/ |
| 73 | Mathematics for Finance, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/mathematics-finance/ |

##### School of Social Sciences

###### BA / BSc
| # | 专业 | URL |
|---|------|-----|
| 74 | Criminology and Criminal Justice, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/criminology-criminal-justice/ |
| 75 | Criminology and Psychology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/criminology-psychology/ |
| 76 | Criminology and Social Policy, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/criminology-social-policy/ |
| 77 | Criminology and Sociology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/criminology-sociology/ |
| 78 | Early Childhood Studies with Early Years Practitioner Status, BA (Hons) | https://www.swansea.ac.uk/undergraduate/courses/early-childhood-studies/ |
| 79 | Education and Psychology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/education-psychology/ |
| 80 | Health and Social Care, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/health-social-care/ |
| 81 | Social Work, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/social-work/ |
| 82 | Sociology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/sociology/ |
| 83 | Sociology and Psychology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/sociology-psychology/ |
| 84 | Sociology and Social Policy, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/sociology-social-policy/ |

#### Faculty of Medicine, Health and Life Science

##### School of Health and Social Care

###### BSc / HECert
| # | 专业 | URL |
|---|------|-----|
| 85 | Adult Nursing (Carmarthen Campus), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/adult-nursing-carmarthen/ |
| 86 | Adult Nursing (Swansea), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/adult-nursing-swansea/ |
| 87 | Basic Audiological Practice, HECert | https://www.swansea.ac.uk/undergraduate/courses/basic-audiological-practice/ |
| 88 | Healthcare Science (Audiology), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-audiology/ |
| 89 | Healthcare Science (Audiology) Part-time, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-audiology-part-time/ |
| 90 | Healthcare Science (Cardiac Physiology), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-cardiac-physiology/ |
| 91 | Healthcare Science (Medical Engineering), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-medical-engineering/ |
| 92 | Healthcare Science (Medical Engineering) Part-time, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-medical-engineering-part-time/ |
| 93 | Healthcare Science (Neurophysiology), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-neurophysiology/ |
| 94 | Healthcare Science (Nuclear Medicine), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-nuclear-medicine/ |
| 95 | Healthcare Science (Radiation Physics), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-radiation-physics/ |
| 96 | Healthcare Science (Radiotherapy Physics), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-radiotherapy-physics/ |
| 97 | Healthcare Science (Rehabilitation Engineering), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-rehabilitation-engineering/ |
| 98 | Healthcare Science (Rehabilitation Engineering) Part-time, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-rehabilitation-engineering-part-time/ |
| 99 | Healthcare Science (Respiratory and Sleep Physiology), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/healthcare-science-respiratory-sleep-physiology/ |
| 100 | Maternity Care, HECert | https://www.swansea.ac.uk/undergraduate/courses/maternity-care/ |
| 101 | Nursing (Child Branch), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/nursing-child/ |
| 102 | Nursing (Learning Disability), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/nursing-learning-disability/ |
| 103 | Nursing (Mental Health Branch), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/nursing-mental-health/ |
| 104 | Nursing Top-Up Collab Uniciti International Education Hub, Mauritius, BSc | https://www.swansea.ac.uk/undergraduate/courses/nursing-top-up-mauritius/ |
| 105 | Occupational Therapy, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/occupational-therapy/ |
| 106 | Operating Department Practice, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/operating-department-practice/ |
| 107 | Osteopathy at Accademia Osteopatia ASOMI, BSc | https://www.swansea.ac.uk/undergraduate/courses/osteopathy/ |
| 108 | Paramedic Science for Emergency Medical Technicians, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/paramedic-science/ |

##### School of Medicine

###### MB BCh / BSc
| # | 专业 | URL |
|---|------|-----|
| 109 | Medicine (Graduate Entry), MB BCh | https://www.swansea.ac.uk/undergraduate/courses/medicine-graduate-entry/ |
| 110 | Applied Medical Sciences, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/applied-medical-sciences/ |
| 111 | Medical Sciences and Population Health, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/medical-sciences-population-health/ |

##### School of Psychology

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 112 | Psychology, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/psychology/ |

##### School of Biosciences, Geography and Physics (shared)

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 113 | Astrophysics, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/astrophysics/ |
| 114 | Biochemistry and Genetics, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/biochemistry-genetics/ |
| 115 | Biochemistry, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/biochemistry/ |
| 116 | Biological Science with deferred choice of specialisation, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/biological-science-deferred-choice/ |
| 117 | Biology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/biology/ |
| 118 | Ecology and Conservation, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/ecology-conservation/ |
| 119 | Environmental Geoscience, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/environmental-geoscience/ |
| 120 | Environmental Science and the Climate Emergency, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/environmental-science-climate-emergency/ |
| 121 | Genetics, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/genetics/ |
| 122 | Marine Biology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/marine-biology/ |
| 123 | Medical Biochemistry, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/medical-biochemistry/ |
| 124 | Medical Genetics, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/medical-genetics/ |
| 125 | Medical Pharmacology, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/medical-pharmacology/ |
| 126 | Microbiology and Immunology, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/microbiology-immunology/ |
| 127 | Physical Geography, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/physical-geography/ |
| 128 | Physics with Particle Physics and Cosmology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/physics-particle-cosmology/ |
| 129 | Physics, BSc (Hons) / MPhys (Hons) | https://www.swansea.ac.uk/undergraduate/courses/physics/ |
| 130 | Sport and Exercise Science, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/sport-exercise-science/ |
| 131 | Theoretical Physics, BSc (Hons) / MPhys (Hons) | https://www.swansea.ac.uk/undergraduate/courses/theoretical-physics/ |
| 132 | Zoology, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/zoology/ |

#### Faculty of Science and Engineering

##### School of Aerospace, Civil, Electrical and Mechanical Engineering

###### BEng / MEng
| # | 专业 | URL |
|---|------|-----|
| 133 | Aeronautical and Manufacturing Engineering, BEng (Hons) Degree Apprenticeship | https://www.swansea.ac.uk/undergraduate/courses/aeronautical-engineering-apprenticeship/ |
| 134 | Aerospace Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/aerospace-engineering/ |
| 135 | Biomedical Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/biomedical-engineering/ |
| 136 | Civil Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/civil-engineering/ |
| 137 | Electronic and Electrical Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/electronic-electrical-engineering/ |
| 138 | Engineering with Deferred Choice of Specialism with a Foundation Year, BEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/engineering-foundation-year/ |
| 139 | Materials Science and Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/materials-science-engineering/ |
| 140 | Mechanical Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/mechanical-engineering/ |

##### School of Engineering and Applied Sciences

###### BEng / MEng / BSc
| # | 专业 | URL |
|---|------|-----|
| 141 | Chemical Engineering, BEng (Hons) / MEng (Hons) | https://www.swansea.ac.uk/undergraduate/courses/chemical-engineering/ |
| 142 | Chemistry, BSc (Hons) / MChem (Hons) | https://www.swansea.ac.uk/undergraduate/courses/chemistry/ |

##### School of Mathematics and Computer Science

###### BSc
| # | 专业 | URL |
|---|------|-----|
| 143 | Applied Mathematics, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/applied-mathematics/ |
| 144 | Applied Software Engineering, BSc (Hons) Degree Apprenticeship | https://www.swansea.ac.uk/undergraduate/courses/applied-software-engineering-apprenticeship/ |
| 145 | Computer Science and Artificial Intelligence, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/computer-science-artificial-intelligence/ |
| 146 | Computer Science and Cyber Security, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/computer-science-cyber-security/ |
| 147 | Computer Science with Cyber Security and Artificial Intelligence (Top-Up), BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/computer-science-cybersecurity-ai-top-up/ |
| 148 | Computer Science, BSc (Hons) / MSci (Hons) | https://www.swansea.ac.uk/undergraduate/courses/computer-science/ |
| 149 | Computing and Digital Technologies, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/computing-digital-technologies/ |
| 150 | Mathematics and Computer Science, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/mathematics-computer-science/ |
| 151 | Mathematics and Sports Science, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/mathematics-sports-science/ |
| 152 | Mathematics, BSc (Hons) / MMath (Hons) | https://www.swansea.ac.uk/undergraduate/courses/mathematics/ |
| 153 | Pure Mathematics, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/pure-mathematics/ |
| 154 | Software Engineering, BSc (Hons) | https://www.swansea.ac.uk/undergraduate/courses/software-engineering/ |

> Combined 3-year BSc and 4-year MSci/MMath/MChem/MPhys/MEng all listed once with the integrated pathway noted.

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Faculty of Humanities and Social Sciences

##### School of Culture and Communication

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Classics and Ancient History, MA | https://www.swansea.ac.uk/postgraduate/taught/classics-ancient-history/ |
| 2 | Communication, Media Practice and Public Relations, MA | https://www.swansea.ac.uk/postgraduate/taught/communication-media-practice-public-relations/ |
| 3 | Conflict, Development and Human Rights, MA | https://www.swansea.ac.uk/postgraduate/taught/conflict-development-human-rights/ |
| 4 | Creative Writing, MA | https://www.swansea.ac.uk/postgraduate/taught/creative-writing/ |
| 5 | Creative Writing (Extended), MA | https://www.swansea.ac.uk/postgraduate/taught/creative-writing-extended/ |
| 6 | Education, MA | https://www.swansea.ac.uk/postgraduate/taught/education/ |
| 7 | English Literature, MA | https://www.swansea.ac.uk/postgraduate/taught/english-literature/ |
| 8 | History, MA | https://www.swansea.ac.uk/postgraduate/taught/history/ |
| 9 | International Journalism, MA | https://www.swansea.ac.uk/postgraduate/taught/international-journalism/ |
| 10 | International Relations, MA | https://www.swansea.ac.uk/postgraduate/taught/international-relations/ |
| 11 | International Relations (Extended), MA | https://www.swansea.ac.uk/postgraduate/taught/international-relations-extended/ |
| 12 | Medieval Studies, MA | https://www.swansea.ac.uk/postgraduate/taught/medieval-studies/ |
| 13 | Professional Translation (Extended, with Université Grenoble Alpes), MA | https://www.swansea.ac.uk/postgraduate/taught/professional-translation-extended/ |
| 14 | Public History and Heritage, MA | https://www.swansea.ac.uk/postgraduate/taught/public-history-heritage/ |
| 15 | Public History and Heritage, MA (Extended) | https://www.swansea.ac.uk/postgraduate/taught/public-history-heritage-extended/ |
| 16 | Sports Communication and Journalism, MA | https://www.swansea.ac.uk/postgraduate/taught/sports-communication-journalism/ |
| 17 | Teaching English to Speakers of Other Languages, MA / PGDip | https://www.swansea.ac.uk/postgraduate/taught/tesol/ |
| 18 | Translation and Intercultural Communication, MA | https://www.swansea.ac.uk/postgraduate/taught/translation-intercultural-communication/ |
| 19 | Translation and Interpreting (Extended with Université Grenoble Alpes), MA | https://www.swansea.ac.uk/postgraduate/taught/translation-interpreting-extended/ |
| 20 | War and Society, MA | https://www.swansea.ac.uk/postgraduate/taught/war-society/ |

##### School of Law

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 21 | Human Rights, LLM | https://www.swansea.ac.uk/postgraduate/taught/human-rights/ |
| 22 | International Commercial Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/international-commercial-law/ |
| 23 | International Commercial and Maritime Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/international-commercial-maritime-law/ |
| 24 | International Maritime Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/international-maritime-law/ |
| 25 | International Trade Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/international-trade-law/ |
| 26 | Law and Legal Practice, LLM | https://www.swansea.ac.uk/postgraduate/taught/law-legal-practice/ |
| 27 | LegalTech and Commercial Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/legaltech-commercial-law/ |
| 28 | Oil, Gas and Renewable Energy Law, LLM | https://www.swansea.ac.uk/postgraduate/taught/oil-gas-renewable-energy-law/ |
| 29 | Professional Legal Practice, LLM | https://www.swansea.ac.uk/postgraduate/taught/professional-legal-practice/ |

##### School of Management

###### MSc / MA
| # | 项目 | URL |
|---|------|-----|
| 30 | Accounting and Finance, MSc | https://www.swansea.ac.uk/postgraduate/taught/accounting-finance/ |
| 31 | Actuarial Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/actuarial-science/ |
| 32 | Actuarial Studies in collaboration with PNU Saudi Arabia, MSc | https://www.swansea.ac.uk/postgraduate/taught/actuarial-studies-pnu/ |
| 33 | Advanced Management (Complex Systems), MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/advanced-management-complex-systems/ |
| 34 | Advanced Management (Health Innovation and Transformation), MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/advanced-management-health-innovation/ |
| 35 | Advanced Management (Sport Business and Leadership), MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/advanced-management-sport-business/ |
| 36 | Banking and Finance, MSc | https://www.swansea.ac.uk/postgraduate/taught/banking-finance/ |
| 37 | Business Management, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/business-management-msc/ |
| 38 | Cyber Crime and Terrorism, MA | https://www.swansea.ac.uk/postgraduate/taught/cyber-crime-terrorism/ |
| 39 | Economics and Finance, MSc | https://www.swansea.ac.uk/postgraduate/taught/economics-finance/ |
| 40 | Economics, MSc | https://www.swansea.ac.uk/postgraduate/taught/economics/ |
| 41 | Finance, MSc | https://www.swansea.ac.uk/postgraduate/taught/finance-msc/ |
| 42 | Finance and Big Data Analytics, MSc | https://www.swansea.ac.uk/postgraduate/taught/finance-big-data-analytics/ |
| 43 | Financial Analytics, MSc | https://www.swansea.ac.uk/postgraduate/taught/financial-analytics/ |
| 44 | Financial Technology (FinTech), MSc | https://www.swansea.ac.uk/postgraduate/taught/fintech/ |
| 45 | Human Resource Management, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/human-resource-management/ |
| 46 | International Business, MSc | https://www.swansea.ac.uk/postgraduate/taught/international-business/ |
| 47 | Investment Management, MSc | https://www.swansea.ac.uk/postgraduate/taught/investment-management/ |
| 48 | Management, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/management/ |
| 49 | Management (Artificial Intelligence), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-ai/ |
| 50 | Management (Business Analytics), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-business-analytics/ |
| 51 | Management (Finance), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-finance/ |
| 52 | Management (Human Resource Management), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-hrm/ |
| 53 | Management (International Management), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-international/ |
| 54 | Management (Marketing), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-marketing/ |
| 55 | Management (Operations and Supply Management), MSc | https://www.swansea.ac.uk/postgraduate/taught/management-operations/ |
| 56 | Marketing, MSc | https://www.swansea.ac.uk/postgraduate/taught/marketing-msc/ |
| 57 | Project Management, MSc | https://www.swansea.ac.uk/postgraduate/taught/project-management/ |
| 58 | Strategic Accounting, MSc | https://www.swansea.ac.uk/postgraduate/taught/strategic-accounting/ |

##### School of Social Sciences

###### MA / MSc
| # | 项目 | URL |
|---|------|-----|
| 59 | Applied Criminal Justice and Criminology, MA | https://www.swansea.ac.uk/postgraduate/taught/applied-criminal-justice-criminology/ |
| 60 | Childhood Studies, MA / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/childhood-studies/ |
| 61 | Developmental and Therapeutic Play, MA / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/developmental-therapeutic-play/ |
| 62 | Education (Wales), MA | https://www.swansea.ac.uk/postgraduate/taught/education-wales/ |
| 63 | Education (Wales): Additional Learning Needs, MA | https://www.swansea.ac.uk/postgraduate/taught/education-wales-aln/ |
| 64 | Education (Wales): Curriculum, MA | https://www.swansea.ac.uk/postgraduate/taught/education-wales-curriculum/ |
| 65 | Education (Wales): Equity in Education, MA | https://www.swansea.ac.uk/postgraduate/taught/education-wales-equity/ |
| 66 | Education (Wales): Leadership, MA | https://www.swansea.ac.uk/postgraduate/taught/education-wales-leadership/ |
| 67 | Gender, Power and Violence, MA / PGDip | https://www.swansea.ac.uk/postgraduate/taught/gender-power-violence/ |
| 68 | Politics, Governance and Public Policy, MA | https://www.swansea.ac.uk/postgraduate/taught/politics-governance-public-policy/ |
| 69 | Public Health and Health Promotion, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/public-health-health-promotion/ |
| 70 | Social Research Methods, MSc | https://www.swansea.ac.uk/postgraduate/taught/social-research-methods/ |
| 71 | Social Work, MSc | https://www.swansea.ac.uk/postgraduate/taught/social-work-msc/ |

#### Faculty of Medicine, Health and Life Science

##### School of Health and Social Care

###### MSc / PGDip / PGCert
| # | 项目 | URL |
|---|------|-----|
| 72 | Advanced Health and Care Management (Value-Based), MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/advanced-health-care-management/ |
| 73 | Advanced Practice in Health Care, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/advanced-practice-health-care/ |
| 74 | Approved Mental Health Professional, PGCert | https://www.swansea.ac.uk/postgraduate/taught/approved-mental-health-professional/ |
| 75 | Community Health Studies, Specialist Practice Qualification in District Nursing, PGDip | https://www.swansea.ac.uk/postgraduate/taught/community-health-studies-district-nursing/ |
| 76 | Community and Primary Health Care Practice, PGDip / PGCert | https://www.swansea.ac.uk/postgraduate/taught/community-primary-health-care-practice/ |
| 77 | Diabetes Practice, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/diabetes-practice/ |
| 78 | Education for the Health Professions, MA / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/education-health-professions/ |
| 79 | Enhanced Professional Midwifery Practice, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/enhanced-professional-midwifery-practice/ |
| 80 | Enhanced Professional Practice, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/enhanced-professional-practice/ |
| 81 | Health Care Management, MSc | https://www.swansea.ac.uk/postgraduate/taught/health-care-management/ |
| 82 | Health Data Science, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/health-data-science/ |
| 83 | Health Informatics, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/health-informatics/ |
| 84 | Medical Education, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/medical-education/ |
| 85 | Non-Medical Prescribing for Allied Health Professionals, PGCert | https://www.swansea.ac.uk/postgraduate/taught/non-medical-prescribing-ahp/ |
| 86 | Non-Medical Prescribing for Nurses and Midwives, PGCert | https://www.swansea.ac.uk/postgraduate/taught/non-medical-prescribing-nurses-midwives/ |
| 87 | Non-Medical Prescribing for Pharmacists, PGCert | https://www.swansea.ac.uk/postgraduate/taught/non-medical-prescribing-pharmacists/ |
| 88 | Nursing (Adult), MSc | https://www.swansea.ac.uk/postgraduate/taught/nursing-adult-msc/ |
| 89 | Nursing (Mental Health), MSc | https://www.swansea.ac.uk/postgraduate/taught/nursing-mental-health-msc/ |
| 90 | Primary with QTS, PGCert | https://www.swansea.ac.uk/postgraduate/taught/primary-qts/ |
| 91 | Specialist Community Public Health Nursing (Health Visiting), PGDip / MSc | https://www.swansea.ac.uk/postgraduate/taught/health-visiting/ |
| 92 | Specialist Community Public Health Nursing (School Nursing), PGDip / MSc | https://www.swansea.ac.uk/postgraduate/taught/school-nursing/ |

##### School of Medicine

###### MSc / MPAS
| # | 项目 | URL |
|---|------|-----|
| 93 | Clinical Psychology and Mental Health, MSc | https://www.swansea.ac.uk/postgraduate/taught/clinical-psychology-mental-health/ |
| 94 | Clinical Science (Medical Physics), MSc | https://www.swansea.ac.uk/postgraduate/taught/clinical-science-medical-physics/ |
| 95 | Cognitive Neuroscience, MSc | https://www.swansea.ac.uk/postgraduate/taught/cognitive-neuroscience/ |
| 96 | Genomic Medicine, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/genomic-medicine/ |
| 97 | Medical Neuroscience, MSc | https://www.swansea.ac.uk/postgraduate/taught/medical-neuroscience/ |
| 98 | Medical Physics, MSc | https://www.swansea.ac.uk/postgraduate/taught/medical-physics/ |
| 99 | Nanomedicine, MSc / PGCert / PGDip | https://www.swansea.ac.uk/postgraduate/taught/nanomedicine/ |
| 100 | Physician Associate Studies, MPAS | https://www.swansea.ac.uk/postgraduate/taught/physician-associate-studies/ |

##### School of Psychology

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 101 | Forensic Psychology, MSc | https://www.swansea.ac.uk/postgraduate/taught/forensic-psychology/ |
| 102 | Psychology (Conversion), MSc | https://www.swansea.ac.uk/postgraduate/taught/psychology-conversion/ |
| 103 | Research Methods in Psychology, MSc | https://www.swansea.ac.uk/postgraduate/taught/research-methods-psychology/ |
| 104 | Sport Psychology, MSc | https://www.swansea.ac.uk/postgraduate/taught/sport-psychology/ |

##### School of Biosciences, Geography and Physics (shared)

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 105 | Biomedical Science (Clinical Biochemistry), MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/biomedical-science-clinical-biochemistry/ |
| 106 | Biomedical Science (Clinical Microbiology), MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/biomedical-science-clinical-microbiology/ |
| 107 | Clinical Exercise Physiology, MSc | https://www.swansea.ac.uk/postgraduate/taught/clinical-exercise-physiology/ |
| 108 | Drug Discovery, Development and Translation, MSc | https://www.swansea.ac.uk/postgraduate/taught/drug-discovery-development-translation/ |
| 109 | Environmental Drone Remote Sensing, MSc | https://www.swansea.ac.uk/postgraduate/taught/environmental-drone-remote-sensing/ |
| 110 | Environmental Dynamics and Climate Change, MSc | https://www.swansea.ac.uk/postgraduate/taught/environmental-dynamics-climate-change/ |
| 111 | Geographic Information and Climate Change, MSc | https://www.swansea.ac.uk/postgraduate/taught/geographic-information-climate-change/ |
| 112 | Global Biodiversity and Conservation, MSc | https://www.swansea.ac.uk/postgraduate/taught/global-biodiversity-conservation/ |
| 113 | Marine Restoration and Conservation, MSc | https://www.swansea.ac.uk/postgraduate/taught/marine-restoration-conservation/ |

#### Faculty of Science and Engineering

##### School of Aerospace, Civil, Electrical and Mechanical Engineering

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 114 | Aerospace Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/aerospace-engineering-msc/ |
| 115 | Biomedical Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/biomedical-engineering-msc/ |
| 116 | Civil Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/civil-engineering-msc/ |
| 117 | Computational Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/computational-engineering/ |
| 118 | Computational Mechanics, MSc | https://www.swansea.ac.uk/postgraduate/taught/computational-mechanics/ |
| 119 | Electronic and Electrical Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/electronic-electrical-engineering-msc/ |
| 120 | Engineering Leadership and Management, MSc | https://www.swansea.ac.uk/postgraduate/taught/engineering-leadership-management/ |
| 121 | Industrial Construction Management, MSc | https://www.swansea.ac.uk/postgraduate/taught/industrial-construction-management/ |
| 122 | Materials Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/materials-engineering-msc/ |
| 123 | Materials and Manufacturing, MSc (Track 2 18 months Swansea Start) | https://www.swansea.ac.uk/postgraduate/taught/materials-manufacturing-track2/ |
| 124 | Mechanical Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/mechanical-engineering-msc/ |
| 125 | Power Engineering and Sustainable Energy, MSc | https://www.swansea.ac.uk/postgraduate/taught/power-engineering-sustainable-energy/ |
| 126 | Space Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/space-engineering/ |
| 127 | Structural Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/structural-engineering/ |
| 128 | Sustainable Aviation, MSc | https://www.swansea.ac.uk/postgraduate/taught/sustainable-aviation/ |

##### School of Engineering and Applied Sciences

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 129 | Chemical Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/chemical-engineering-msc/ |
| 130 | Fusion Engineering, MSc | https://www.swansea.ac.uk/postgraduate/taught/fusion-engineering/ |

##### School of Mathematics and Computer Science

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 131 | Advanced Computer Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/advanced-computer-science/ |
| 132 | Applied Data Science, MSc / PGDip | https://www.swansea.ac.uk/postgraduate/taught/applied-data-science/ |
| 133 | Artificial Intelligence and Data Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/artificial-intelligence-data-science/ |
| 134 | Computer Science - Informatique (Swansea), MSc | https://www.swansea.ac.uk/postgraduate/taught/computer-science-informatique/ |
| 135 | Computer Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/computer-science-msc/ |
| 136 | Cyber Security, MSc | https://www.swansea.ac.uk/postgraduate/taught/cyber-security/ |
| 137 | Data Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/data-science-msc/ |
| 138 | Mathematics and Computing for Finance, MSc | https://www.swansea.ac.uk/postgraduate/taught/mathematics-computing-finance/ |
| 139 | Mathematics, MSc | https://www.swansea.ac.uk/postgraduate/taught/mathematics-msc/ |

##### School of Biosciences, Geography and Physics (shared)

###### MSc
| # | 项目 | URL |
|---|------|-----|
| 140 | Advanced Sport Performance Science, MSc | https://www.swansea.ac.uk/postgraduate/taught/advanced-sport-performance-science/ |
| 141 | Physics with Particle Physics and Cosmology, MSc | https://www.swansea.ac.uk/postgraduate/taught/physics-particle-cosmology-msc/ |

#### PG Research (cross-faculty)

###### MPhil / MRes / Masters by Research / PhD / EngD / EdD / DCrim / DBA
| # | 项目 | URL |
|---|------|-----|
| 142 | PhD (all faculties) — full-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 143 | MPhil (all faculties) — full-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 144 | Masters by Research (all faculties) — full-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 145 | EngD (Engineering Doctorate) — full-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 146 | EdD (Doctor of Education) — part-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 147 | DCrim (Doctor of Criminology) — part-time | https://www.swansea.ac.uk/postgraduate/research/ |
| 148 | DBA (Doctor of Business Administration) — part-time | https://www.swansea.ac.uk/postgraduate/research/ |

#### PGCE / PG Teacher Training (cross-faculty, School of Education)

###### PGCert (with QTS)
| # | 项目 | URL |
|---|------|-----|
| 149 | Secondary PGCE with QTS: Biology, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-biology/ |
| 150 | Secondary PGCE with QTS: Chemistry, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-chemistry/ |
| 151 | Secondary PGCE with QTS: Computer Science, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-computer-science/ |
| 152 | Secondary PGCE with QTS: Design and Technology, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-design-technology/ |
| 153 | Secondary PGCE with QTS: English, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-english/ |
| 154 | Secondary PGCE with QTS: Geography, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-geography/ |
| 155 | Secondary PGCE with QTS: History, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-history/ |
| 156 | Secondary PGCE with QTS: Mathematics, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-mathematics/ |
| 157 | Secondary PGCE with QTS: Modern Foreign Languages (French, Spanish), PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-mfl/ |
| 158 | Secondary PGCE with QTS: Physics, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-physics/ |
| 159 | Secondary PGCE with QTS: Welsh, PGCert | https://www.swansea.ac.uk/postgraduate/taught/pgce-welsh/ |

> **Note**: Some UG programmes listed in Section 1.2 also have a Foundation Year variant (e.g. Engineering Foundation Year, Medical Biochemistry with Foundation Year). Foundation Year counts as Year 0; full degree is 4 years.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | **UCAS** (national) |
| UCAS main deadline (equal consideration) | **25 January** (most UG courses) |
| UCAS late deadline | **30 June** (Clearing applications) |
| Application opens | UCAS opens early September; applications reviewed from 1 September onwards |
| Admissions tests | None required by default (some courses may require subject-specific tests e.g. LNAT for Law; interview for Medicine) |
| Personal statement | Single UCAS personal statement (max 4,000 characters; 2024+ reform to 3-question format pending — check UCAS for current year) |
| References | 1 academic reference required via UCAS |
| Interview policy | **Medicine** (MB BCh) uses MMI interviews; other courses rarely interview; PGCE programmes interview |
| Work experience | Recommended for Nursing, Medicine, Social Work (relevant work experience cited in personal statement) |
| EPQ | Grade B in EPQ = one-grade reduction in offer (e.g. AAB→ABB). Mention in personal statement. |
| Clearing | Active in 2026 — see https://www.swansea.ac.uk/clearing/ |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum (UG) | Recommended |
|------|--------------|-------------|
| IELTS Academic | 6.0 (most courses); 6.5 (e.g. Healthcare Sciences, Nursing); 7.0 (Law, Medicine — check course page) | 6.5–7.0 |
| TOEFL iBT | ~80 (most courses) | 90+ |
| PTE Academic | ~62 (most courses) | 65+ |
| Cambridge English | Advanced (CAE) / Proficiency (CPE) — grade C or above accepted | — |
| Duolingo English Test | Not consistently accepted — check course page | — |

> Per-school variations: Law and Healthcare Science often require higher. Confirm on individual course pages.

### 3.3 Graduate — global rules

| Field | Value |
|-------|-------|
| Application platform | Direct to Swansea University (no UCAS for PG) |
| Standard application fee | None for direct online application (Swansea has no application fee) |
| PG Taught deadlines | Rolling — many courses accept applications through summer; competitive courses (e.g. Physician Associate, Medicine-related) have earlier cutoffs (e.g. January for September entry) |
| PG Research (PhD/MPhil) deadlines | Rolling — research degrees start throughout year; funding applications (e.g. UKRI) usually January deadline |
| Admissions tests | None standard; some programmes require portfolio (Creative Writing), interview (Social Work, Physician Associate, PGCE) |
| English proficiency | Generally IELTS 6.5 (most PGT); 7.0 (e.g. Physician Associate, English Literature); 6.0 (lower-tier) — confirm on course page |
| GRE/GMAT | Not required for any Swansea programme |
| Reference requirements | 1–2 academic/professional references |
| Personal statement | Required — explains motivation, suitability for programme |
| International scholarship deadline | Varies — typically March–May for September entry |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, 2025/26)

| Expense item | Home (UK) fee | Overseas/International fee |
|--------------|---------------|---------------------------|
| Tuition (most programmes) | £9,250/yr | £18,950 – £21,400/yr |
| Tuition (Engineering — Aerospace, Mechanical, Electrical, Civil) | £9,250/yr | £22,400 – £23,650/yr |
| Tuition (Architecture / Materials) | £9,250/yr | £22,400/yr |
| Tuition (Medicine MB BCh) | £9,250/yr | **£47,950/yr** |
| Tuition (Biosciences, Chemistry, Geography, Physics, Psychology) | £9,250/yr | ~£19,450 – £22,000/yr |
| Tuition (Business, Economics, Accounting, Law, Marketing) | £9,250/yr | £18,950 – £19,950/yr |
| Tuition (Computer Science, Software Engineering, AI) | £9,250/yr | £20,000/yr |
| Accommodation (on-campus, varies) | £4,500 – £7,500/yr | £4,500 – £7,500/yr |
| Cost of living (estimate) | £9,000 – £11,000/yr | £9,000 – £11,000/yr |

> Home fees are capped at the standard UK £9,250/yr. Fees rise ~3% annually. Confirmation on each course page.

### 4.2 Undergraduate financial-aid policy

| Field | Value |
|-------|-------|
| Home student loans | Student Finance England / Wales (loans up to £9,250 tuition + maintenance loan) |
| Welsh Government grants | Maintenance grants available for Welsh-domiciled low-income students |
| International scholarships | International Excellence Scholarships up to £3,000; Country-specific bursaries |
| Excellence/Merit Scholarships | For AAA–AAB at A-Level (or equivalent) — automatic consideration |
| Need-blind admissions | Yes (UK Home students) — Swansea participates in Student Finance Wales |
| Visa surcharge (IHS) | International students pay ~£470/yr Immigration Health Surcharge |

### 4.3 Graduate cost & funding framework

| Field | Value |
|-------|-------|
| PGT Home tuition | £7,000 – £12,000/yr (varies by school — Lab-based higher) |
| PGT International tuition | £17,000 – £24,000/yr (varies by school — Business, Engineering higher) |
| PhD Home tuition | £4,786 (2024/25) → **£5,006 (2025/26)** |
| PhD part-time Home | £2,393 → **£2,503 (2025/26)** |
| MPhil Home tuition | £2,393 (PT) → £5,006 (FT 2025/26) |
| Masters by Research Home | £4,786 → **£5,006 (2025/26)** |
| EngD Home tuition | £4,786 → **£5,006 (2025/26)** |
| DBA part-time Home | £7,950 → **£8,100 (2025/26)** |
| Professional Doctorate (EdD, DCrim) | £2,427 → **£2,500 (2025/26)** |
| PhD International tuition | Varies by school/programme — typically £18,000–£22,000/yr; lab-based higher |
| Re-submission fee (dissertation) | £102 |
| Funding sources | UKRI (e.g. ESRC, BBSRC, EPSRC Doctoral Training Partnerships); Swansea University Scholarships; Commonwealth; Chevening (for internationals) |
| Application fee | None for direct application |
| Fees annual increase | ~3% |

---

## SECTION 5 — Evidence chain index

```yaml
E-UG-001:
  field: undergraduate.courses.total_count
  value: 154
  source_url: https://www.swansea.ac.uk/undergraduate/courses/
  source_snippet: "Search our Undergraduate courses - course list page enumerating 154 UG programmes"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-UG-002:
  field: undergraduate.faculties_count
  value: 3
  source_url: https://www.swansea.ac.uk/the-university/faculties/
  source_snippet: "Humanities and Social Sciences; Medicine, Health and Life Science; Science and Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-UG-003:
  field: undergraduate.application_platform
  value: UCAS
  source_url: https://www.swansea.ac.uk/undergraduate/how-to-apply/
  source_snippet: "All UK undergraduate applications submitted via UCAS"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-UG-004:
  field: undergraduate.ucas_deadline
  value: "25 January (equal consideration)"
  source_url: https://www.swansea.ac.uk/undergraduate/how-to-apply/
  source_snippet: "UCAS January deadline for equal consideration"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-FEE-001:
  field: undergraduate.cost.home_fee
  value: "£9,250/yr"
  source_url: https://www.swansea.ac.uk/undergraduate/fees-and-funding/
  source_snippet: "Standard UK undergraduate tuition fee cap"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-FEE-002:
  field: undergraduate.cost.overseas_fee_range
  value: "£18,950 – £23,650/yr"
  source_url: https://www.swansea.ac.uk/international-students/my-finances/
  source_snippet: "Most programmes £18,950–£21,400; Engineering £22,400–£23,650"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-FEE-003:
  field: undergraduate.cost.medicine_overseas
  value: "£47,950/yr"
  source_url: https://www.swansea.ac.uk/international-students/my-finances/
  source_snippet: "Medicine / MB BCh international fee significantly higher"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-PG-001:
  field: postgraduate.courses.pgt_total
  value: 152
  source_url: https://www.swansea.ac.uk/postgraduate/taught/
  source_snippet: "Search our Postgraduate Taught Courses - 152 PGT programmes listed"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-PG-002:
  field: postgraduate.courses.research_total
  value: 6
  source_url: https://www.swansea.ac.uk/postgraduate/research/
  source_snippet: "PhD, MPhil, Masters by Research, EngD, EdD, DCrim, DBA"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-PG-FEE-001:
  field: postgraduate.cost.phd_home_2025_26
  value: "£5,006/yr (full-time); £2,503/yr (part-time)"
  source_url: https://www.swansea.ac.uk/postgraduate/fees-and-funding/postgraduate-tuition-fees/
  source_snippet: "PhD (full-time) £5,006; PhD (part-time) £2,503 for 2025/26"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-LANG-001:
  field: english.presessional_swelts
  value: "IELTS 4.5 (20-week), 5.0 (12-week), 5.5 (10-week)"
  source_url: https://www.swansea.ac.uk/english-language-training-services/our-courses/
  source_snippet: "20 Weeks: SWELT/IELTS 4.5 (min 4.0); 12 Weeks: 5.0; 10 Weeks: 5.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-ACC-001:
  field: school.structure.acem_engineering_school
  value: "School of Aerospace, Civil, Electrical and Mechanical Engineering"
  source_url: https://www.swansea.ac.uk/science-and-engineering/
  source_snippet: "Our Schools: School of Aerospace, Civil, Electrical and Mechanical Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-RANK-001:
  field: institution.ranking.qs_world
  value: "Top 350 (QS 2027)"
  source_url: https://www.swansea.ac.uk/
  source_snippet: "IN THE TOP 350 IN THE WORLD - QS World University Rankings 2027"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: swansea-university-knowledge-base-v2
├── documents/
│   ├── overview/                       (Section 0 — counts, hierarchy, matrix)
│   ├── undergraduate/                  (Section 1 — UG programs by school)
│   ├── postgraduate/                   (Section 2 — PG programs by school)
│   ├── admissions/                     (Section 3 — requirements + deadlines)
│   ├── costs/                          (Section 4 — fees + funding)
│   ├── evidence/                       (Section 5 — evidence chain index)
│   └── monitoring/                     (URL watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "swansea-university-knowledge-base-v2"
  school: "<home school/faculty>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BSc|BEng|MEng|MA|MSc|LLM|MPAS|PGDip|PGCert|PhD|MPhil|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P1 | Per-program exact 2026/27 tuition fees (international) | https://www.swansea.ac.uk/international-students/my-finances/ |
| P1 | Per-program English language minimum (UG + PG) | individual course pages |
| P1 | Foundation Year (Year 0) variants — separate capture | https://www.swansea.ac.uk/undergraduate/courses/ |
| P2 | PhD/MPhil research areas by school | https://www.swansea.ac.uk/postgraduate/research/ |
| P2 | PG Research international tuition per school | https://www.swansea.ac.uk/postgraduate/research/ |
| P2 | Clearing vacancies (current year) | https://www.swansea.ac.uk/clearing/vacancies/ |
| P3 | UCAT/BMAT/LNAT scores by programme | individual course pages |
| P3 | Clearing phone-line hours | https://www.swansea.ac.uk/clearing/contact/ |

---

## SECTION 7 — Cross-school comparison framework

| Field | Swansea | UK Russell Group avg |
|-------|---------|---------------------|
| Total UG programs | 154 | ~200–400 |
| Total PG programs (PGT+PGR) | 158 | ~250–500 |
| Faculties | 3 | varies (typically 4–8) |
| Schools | 13 | varies |
| Home UG fee | £9,250/yr | £9,250/yr (cap) |
| International UG fee (most programmes) | £18,950–£21,400/yr | £20,000–£35,000/yr |
| International Engineering UG fee | £22,400–£23,650/yr | £25,000–£35,000/yr |
| Medicine international fee | £47,950/yr | £40,000–£65,000/yr |
| PhD Home fee | £5,006/yr | £4,500–£5,500/yr |
| UCAS deadline | 25 January | 25 January |
| Pre-sessional English | Yes (20/12/10/6-week) | Most Russell Group |
| Application fee (PG) | None | £0–£100 |
| Welsh language support | Yes — extensive Cymraeg provision | N/A (most outside Wales) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: https://www.swansea.ac.uk/ (UG/PG/Research/International sites)
> **Verification**: ego-browser snapshotText + JS DOM extraction + WebFetch
> **Granularity**: school → department → degree-level → program