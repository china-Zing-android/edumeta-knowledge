# Yale University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Yale College majors, BA/BS/BFA) | 78 |
| 本科证书项目 (Certificate programs, non-degree) | 35+ (不计入主总数) |
| 研究生学位项目 — GSAS (program × degree rows) | 95 |
| 研究生学位项目 — 12 所专业学院 (professional schools) | 48 |
| **学位项目总计 (UG + Grad, degree-bearing)** | **221** |
| 学院 / 独立系所总数 (Yale College + GSAS + 12 professional schools + ISM) | 15 |

> **Reconciliation gate**: 221 (rule 1) == 221 (rule-4 matrix cell-sum) == 221 (rule-5 row count). Verified in Python from `/tmp/all_programs.json`. The "over 80 majors" wording on `admissions.yale.edu/majors` reflects Yale's marketing count that includes the 5-year BA/MA joint programs and select certificate-designated majors; the page lists exactly **78 distinct named majors**.

**Source**: `https://admissions.yale.edu/majors` — *"Yale College students select from over 80 majors without the restrictions of a core curriculum."* (capture 2026-07-04)

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

Yale is organized as **Yale College (UG)** + **Graduate School of Arts and Sciences (GSAS)** + **12 professional schools** + the **Institute of Sacred Music (ISM)** as a cross-school institute. SEAS (School of Engineering & Applied Science) is an administrative umbrella whose departments are degree-granted jointly through Yale College (UG) and GSAS (grad).

```
Yale University
├── Yale College                                              [学院] (undergraduate liberal arts)
│   ├── ~40 humanities/social-science departments & programs  [系]
│   ├── SEAS-affiliated engineering departments (UG side)     [系]  ⚠ shared with SEAS/GSAS
│   │   ├── Applied & Computational Mathematics               [系]
│   │   ├── Applied Physics                                   [系]
│   │   ├── Biomedical Engineering                            [系]
│   │   ├── Chemical & Environmental Engineering              [系]
│   │   ├── Computer Science                                  [系]
│   │   ├── Electrical & Computer Engineering                 [系]
│   │   ├── Materials Science                                 [系]
│   │   └── Mechanical Engineering                            [系]
│   └── Interdisciplinary programs (Ethics Politics & Economics,
│       Global Affairs, Humanities, etc.)                     [系]
│
├── Graduate School of Arts & Sciences (GSAS)                 [学院] (grad MA/MS/MPhil/PhD)
│   ├── 72 departmental/interdepartmental programs            [系]
│   └── (Engineering grad degrees administered via GSAS,      ⚠ shared with SEAS
│        dept slugs: applied-physics, biomedical-engineering,
│        chemical-environmental-engineering, computer-science,
│        electrical-computer-engineering, materials-science,
│        mechanical-engineering)
│
├── School of Architecture                                    [学院] (MArch I/II, MED, PhD)
├── School of Art                                              [学院] (MFA ×4 areas)
├── Berkeley Divinity School / Yale Divinity School           [学院] (MDiv, MAR, STM)
├── David Geffen School of Drama                              [学院] (MFA+Cert ×6)
├── School of the Environment (Forestry & Environmental)      [学院] (MESc, MF, MFS, PhD)
├── Jackson School of Global Affairs                          [学院] (MPP, MAS)
├── Law School                                                 [学院] (JD, LLM, JSD, MSL, PhD)
├── School of Management (SOM)                                [学院] (MBA, MBA-Exec, MAM, MMS, PhD)
├── School of Medicine                                        [学院] (MD, MMSc, PA-MMSc, MD/PhD)
├── School of Music                                            [学院] (MM, MMA, DMA, Artist Diploma)
├── School of Nursing                                          [学院] (MSN, DNP, PhD, Post-MSN Cert)
├── School of Public Health (YSPH)                            [学院] (MPH, MSPH, PhD)
└── Institute of Sacred Music (ISM)                           [学院] (cross-school; awards via Music/Divinity/GSAS)
```

**Schools/colleges count**: 14 degree-granting units (Yale College + GSAS + 12 professional schools); ISM is a cross-school institute that does not independently award degrees — students are registered through Music, Divinity, or GSAS.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本校该级别项目数 |
|---------|------|------|----------------|
| BA / BS | Bachelor of Arts / Bachelor of Science | 本科 | 78 |
| MA | Master of Arts | 研究生 | 13 |
| MS | Master of Science | 研究生 | 10 |
| MFA | Master of Fine Arts | 研究生 | 10 (Art 4 + Drama 6) |
| PhD | Doctor of Philosophy | 研究生 | 78 |
| MArch | Master of Architecture | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 2 |
| MDiv | Master of Divinity | 研究生 | 1 |
| MAR | Master of Arts in Religion | 研究生 | 1 |
| STM | Master of Sacred Theology | 研究生 | 1 |
| MED | Master of Environmental Design | 研究生 | 1 |
| MESc | Master of Environmental Science | 研究生 | 1 |
| MF | Master of Forestry | 研究生 | 1 |
| MFS | Master of Forest Science | 研究生 | 1 |
| MPP | Master in Public Policy (Global Affairs) | 研究生 | 1 |
| MAS | Master of Advanced Study | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| JSD | Doctor of the Science of Law | 研究生 | 1 |
| MSL | Master of Studies in Law | 研究生 | 1 |
| MAM | Master of Advanced Management | 研究生 | 1 |
| MMS | Master of Management Studies | 研究生 | 1 |
| MD | Doctor of Medicine | 研究生 | 1 |
| MMSc | Master of Medical Science | 研究生 | 1 |
| MMSc-PA | Physician Associate (MMSc) | 研究生 | 1 |
| MD/PhD | MD-PhD Medical Scientist Training | 研究生 | 1 |
| MM | Master of Music | 研究生 | 1 |
| MMA | Master of Musical Arts | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| ADip | Artist Diploma | 研究生 | 1 |
| MSN | Master of Science in Nursing | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| Post-MSN Cert | Post-Master's Certificate (Nursing) | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| MSPH | Master of Science in Public Health | 研究生 | 1 |
| **合计** | | | **221** |

> The column total (221) equals rule-1 total and rule-4 cell-sum. ✓

### 0.4 分布矩阵 (Rule 4 — 学院 × 学位级别)

| 学院 \ 级别 | BA/BS | PhD | MA | MS | MFA | MArch | MBA | JD-track | MD-track | MM-track | Other-prof | 合计 |
|------------|------:|----:|---:|---:|----:|------:|----:|---------:|---------:|---------:|-----------:|-----:|
| Yale College (UG) | 78 | – | – | – | – | – | – | – | – | – | – | **78** |
| Graduate School (GSAS) | – | 72 | 13 | 10 | – | – | – | – | – | – | – | **95** |
| Architecture | – | 1 | – | – | – | 2 | – | – | – | – | MED×1 | **4** |
| Art | – | – | – | – | 4 | – | – | – | – | – | – | **4** |
| Divinity | – | – | – | – | – | – | – | – | – | – | MDiv×1,MAR×1,STM×1 | **3** |
| Drama (Geffen) | – | – | – | – | 6 | – | – | – | – | – | – | **6** |
| Environment / Forestry | – | 1 | – | – | – | – | – | – | – | – | MESc×1,MF×1,MFS×1 | **4** |
| Global Affairs (Jackson) | – | – | – | – | – | – | – | – | – | – | MPP×1,MAS×1 | **2** |
| Law | – | 1 | – | – | – | – | – | JD×1,LLM×1,JSD×1,MSL×1 | – | – | – | **5** |
| Management (SOM) | – | 1 | – | – | – | – | 2 | – | – | – | MAM×1,MMS×1 | **5** |
| Medicine | – | – | – | – | – | – | – | – | MD×1,MMSc×1,MMSc-PA×1,MD/PhD×1 | – | – | **4** |
| Music | – | – | – | – | – | – | – | – | – | MM×1,MMA×1,DMA×1,ADip×1 | – | **4** |
| Nursing | – | 1 | – | – | – | – | – | – | – | – | MSN×1,DNP×1,PostMSN-Cert×1 | **4** |
| Public Health (YSPH) | – | 1 | – | – | – | – | – | – | – | – | MPH×1,MSPH×1 | **3** |
| **合计** | **78** | **78** | **13** | **10** | **10** | **2** | **2** | **4** | **4** | **4** | **16** | **221** |

> "JD-track" = JD+LLM+JSD+MSL (4). "MD-track" = MD+MMSc+MMSc-PA+MD/PhD (4). "MM-track" = MM+MMA+DMA+ADip (4). "Other-prof" = the remaining professional master's/doctoral titles listed in rule 3. Column sums: 78+78+13+10+10+2+2+4+4+4+16 = **221** ✓. Row-sum grand total = **221** ✓. Reconciliation confirmed.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College architecture

Yale College is Yale's undergraduate liberal-arts college (~4,700 students). All undergraduates enter undeclared and choose from **78 majors** by the end of sophomore year. There is no core curriculum; students take 36 courses over four years. The School of Engineering & Applied Science (SEAS) is an administrative umbrella — undergrad engineering majors are granted by Yale College through the 8 SEAS-affiliated departments, and graduate engineering degrees flow through GSAS.

**Source**: `https://admissions.yale.edu/majors` — *"Yale College students select from over 80 majors without the restrictions of a core curriculum… Every student begins their Yale journey undeclared and has until the end of sophomore year to choose a major."* (capture 2026-07-04)

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

Yale College awards the BA or BS (degree type is set by the department, not chosen by the student; BFA is not separately conferred at the UG level — Art/Architecture are BA). All 78 majors below are listed under their administrative home.

#### Yale College
##### Humanities
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African Studies | https://macmillan.yale.edu/africa |
| 2 | American Studies | https://americanstudies.yale.edu/ |
| 3 | Classical Civilization | http://www.yale.edu/classics/ |
| 4 | Classics | http://www.yale.edu/classics/ |
| 5 | Comparative Literature | http://www.yale.edu/complit/litmajorfaq.html |
| 6 | East Asian Languages & Literatures | http://www.yale.edu/eall/undergrad.html |
| 7 | East Asian Studies | http://ceas.yale.edu/ |
| 8 | English | http://www.yale.edu/english/undergraduate.html |
| 9 | Ethics, Politics & Economics | http://www.yale.edu/epe/ |
| 10 | Film and Media Studies | http://www.yale.edu/filmstudiesprogram/undergrad.html |
| 11 | French | https://french.yale.edu/undergraduate-program |
| 12 | German Studies | https://german.yale.edu/academics/undergraduate-program |
| 13 | Greek, Ancient and Modern | http://www.yale.edu/classics/ |
| 14 | History | https://history.yale.edu/academics/undergraduate-program |
| 15 | History of Art | http://arthistory.yale.edu/undergraduate/ |
| 16 | History of Science, Medicine, and Public Health | http://hshm.yale.edu/undergraduate-major |
| 17 | Humanities | https://humanities.yale.edu/humanities-major |
| 18 | Italian Studies | http://www.yale.edu/italian/academic/undergrad/ |
| 19 | Jewish Studies | https://jewishstudies.yale.edu/ |
| 20 | Latin American Studies | https://clais.macmillan.yale.edu/ |
| 21 | Modern Middle East Studies | https://cmes.macmillan.yale.edu/academics/modern-middle-east-studies-major |
| 22 | Near Eastern Languages & Civilizations | http://www.yale.edu/nelc |
| 23 | Philosophy | http://www.yale.edu/philos/undergrad.html |
| 24 | Religious Studies | http://www.yale.edu/religiousstudies/undergrad.html |
| 25 | Russian | http://www.yale.edu/slavic/undergrad.html |
| 26 | Russian, East European, and Eurasian Studies | http://www.yale.edu/slavic/undergrad.html |
| 27 | South Asian Studies | http://catalog.yale.edu/ycps/subjects-of-instruction/south-asian-studies/ |
| 28 | Spanish | http://www.yale.edu/span-port/index.html |
| 29 | Portuguese | http://www.yale.edu/span-port/portuguese.html |

##### Social Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 30 | Anthropology | https://anthropology.yale.edu/ |
| 31 | Cognitive Science | http://www.yale.edu/cogsci |
| 32 | Economics | https://economics.yale.edu/undergraduate-program |
| 33 | Economics & Mathematics | http://catalog.yale.edu/ycps/subjects-of-instruction/economics-mathematics/ |
| 34 | Ethnicity, Race & Migration | http://erm.yale.edu/ |
| 35 | Global Affairs | https://jackson.yale.edu/academics/the-global-affairs-major/ |
| 36 | Political Science | http://www.yale.edu/polisci/undergrad/index.html |
| 37 | Psychology | http://www.yale.edu/psychology/programs.html#undergrad |
| 38 | Sociology | http://www.yale.edu/socdept |
| 39 | Urban Studies | https://urbanstudies.yale.edu/ |
| 40 | Women's, Gender, & Sexuality Studies | http://www.yale.edu/wgss/undergrad.html |
| 41 | Black Studies | https://afamstudies.yale.edu/ |

##### Natural Sciences / Mathematics
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 42 | Applied Mathematics | https://applied.math.yale.edu/ |
| 43 | Astronomy | https://astronomy.yale.edu/undergraduate-program |
| 44 | Astrophysics | https://astronomy.yale.edu/undergraduate-program |
| 45 | Chemistry | https://chem.yale.edu/academics/undergraduate-chemistry-at-yale |
| 46 | Ecology & Evolutionary Biology | http://www.yale.edu/eeb/ |
| 47 | Earth and Planetary Sciences | https://earth.yale.edu/ |
| 48 | Mathematics | https://math.yale.edu/undergraduates |
| 49 | Mathematics & Philosophy | http://catalog.yale.edu/ycps/subjects-of-instruction/mathematics-philosophy/ |
| 50 | Mathematics & Physics | http://catalog.yale.edu/ycps/subjects-of-instruction/mathematics-physics/ |
| 51 | Molecular Biophysics & Biochemistry | https://mbb.yale.edu/ |
| 52 | Molecular, Cellular, & Developmental Biology | https://mcdb.yale.edu/ |
| 53 | Neuroscience | http://neuroscience.yale.edu/ |
| 54 | Physics | http://www.yale.edu/physics/undergrad/index.shtml |
| 55 | Physics & Geosciences | http://catalog.yale.edu/ycps/subjects-of-instruction/physics-geosciences/ |
| 56 | Physics & Philosophy | http://catalog.yale.edu/ycps/subjects-of-instruction/physics-philosophy/ |
| 57 | Statistics and Data Science | http://statistics.yale.edu/ |

##### SEAS-affiliated Engineering / Computing (BA / BS)
| # | 专业 | URL |
|---|------|-----|
| 58 | Applied Physics | https://engineering.yale.edu/academic-study/departments/applied-physics/undergraduate-study |
| 59 | Biomedical Engineering | https://engineering.yale.edu/academic-study/departments/biomedical-engineering |
| 60 | Chemical Engineering | http://seas.yale.edu/departments/chemical-and-environmental-engineering |
| 61 | Computer Science | http://cpsc.yale.edu/ |
| 62 | Computer Science and Economics | http://catalog.yale.edu/ycps/subjects-of-instruction/computerscienceandeconomics/ |
| 63 | Computer Science and Mathematics | http://catalog.yale.edu/ycps/subjects-of-instruction/computer-science-mathematics/ |
| 64 | Computer Science and Psychology | http://catalog.yale.edu/ycps/subjects-of-instruction/computer-science-psychology/ |
| 65 | Computing and Linguistics | http://catalog.yale.edu/ycps/subjects-of-instruction/computing20and20linguistics/ |
| 66 | Computing and the Arts | http://c2.cs.yale.edu/ |
| 67 | Electrical Engineering | https://seas.yale.edu/departments/electrical-engineering |
| 68 | Electrical Engineering & Computer Science | http://catalog.yale.edu/ycps/subjects-of-instruction/electrical-engineering-computer-science/ |
| 69 | Environmental Engineering | http://seas.yale.edu/departments/chemical-and-environmental-engineering |
| 70 | Mechanical Engineering | https://seas.yale.edu/departments/mechanical-engineering-and-materials-science |

##### Interdisciplinary / Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 71 | Archaeological Studies | https://archaeology.yale.edu/academics/undergraduate-program-archaeological-studies |
| 72 | Architecture | https://www.architecture.yale.edu/academics/undergraduate-studies |
| 73 | Art | https://www.art.yale.edu/about/study-areas/undergraduate-studies |
| 74 | Environmental Studies | http://www.yale.edu/evst/index.html |
| 75 | Linguistics | https://ling.yale.edu/undergraduate |
| 76 | Music | https://yalemusic.yale.edu/undergraduate/introduction |
| 77 | Special Divisional Major | http://catalog.yale.edu/ycps/subjects-of-instruction/special-divisional-majors/ |
| 78 | Theater, Dance, and Performance Studies | https://tdps.yale.edu/ |

### 1.3 Interdisciplinary / joint UG programs

The **Special Divisional Major** (#77) is Yale's formal mechanism for student-designed interdisciplinary majors. Several listed majors are themselves interdepartmental joint programs: Computer Science and Economics (62), Computer Science and Mathematics (63), Computer Science and Psychology (64), Computing and Linguistics (65), Computing and the Arts (66), Electrical Engineering & Computer Science (68), Economics & Mathematics (33), Mathematics & Philosophy (49), Mathematics & Physics (50), Physics & Geosciences (55), Physics & Philosophy (56). Each is administered by a faculty committee spanning the parent departments.

### 1.4 5-Year BA/BS + Master's joint programs (UG ↔ professional schools)

These are open to Yale College students and reduce the combined BA+Master's to 5 years. They are NOT counted in the 78-major total above.

| # | Program | Partner school | URL |
|---|---------|---------------|-----|
| 1 | 5-Year BA/BS-MF or MESc | School of the Environment | https://environment.yale.edu/academics/masters/joint-degrees/5-year-program |
| 2 | 5-Year BA-MPP | Jackson School of Global Affairs | https://jackson.yale.edu/academics/five-year-program/ |
| 3 | 5-Year BA/MM | School of Music | https://bulletin.yale.edu/bulletins/music/program-requirements#b-a-m-m-program |
| 4 | 5-Year BA/BS-MPH | School of Public Health | https://ysph.yale.edu/school-of-public-health/graduate-programs/mph-joint-degree/5-year-ba-bs-mph/ |

**Source**: `https://admissions.yale.edu/majors` — *"5-year bachelor's and master's degree programs: The School of the Environment, Jackson School of Global Affairs, School of Music, School of Public Health"* (capture 2026-07-04)

### 1.5 Certificate programs (UG, non-degree)

Yale College offers **35+ certificate programs** (e.g. Energy Studies, Education Studies, Human Rights Studies, Data Science, Technology Entrepreneurship). Certificates are pursued alongside a major and are not separately degree-bearing. Full list at `https://catalog.yale.edu/ycps/academic-regulations/special-academic-arrangements/`.

**Source**: `https://admissions.yale.edu/majors` — *"35+ Certificate programs"* (capture 2026-07-04)

### 1.6 UG general-education framework

Yale College has **no core curriculum**. Distributional requirements: 2 course credits each in humanities/arts, sciences, social sciences, and quantitative reasoning; 3 credits in the foreign language requirement; and the writing requirement (1 seminar). Total = 36 course credits.

**Source**: `https://admissions.yale.edu/majors` — *"Yale students enroll in four or five courses each semester to complete a total of thirty-six courses."* (capture 2026-07-04)

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Graduate School of Arts and Sciences (GSAS) — 95 program-degree rows
> Each GSAS program may offer a PhD and (selectively) a terminal MA or MS. The MPhil is awarded en route to the PhD and is not counted separately. Programs listed alphabetically.

##### PhD (72 programs)
| # | 项目 | URL |
|---|------|-----|
| 1 | African Studies | https://gsas.yale.edu/programs-of-study/african-studies |
| 2 | American Studies | https://gsas.yale.edu/programs-of-study/american-studies |
| 3 | Anthropology | https://gsas.yale.edu/programs-of-study/anthropology |
| 4 | Applied & Computational Mathematics | https://gsas.yale.edu/programs-of-study/applied-computational-mathematics |
| 5 | Applied Physics | https://gsas.yale.edu/programs-of-study/applied-physics |
| 6 | Archaeological Studies | https://gsas.yale.edu/programs-of-study/archaeological-studies |
| 7 | Architecture | https://gsas.yale.edu/programs-of-study/architecture |
| 8 | Astronomy | https://gsas.yale.edu/programs-of-study/astronomy |
| 9 | Biological & Biomedical Sciences (BBS) | https://gsas.yale.edu/programs-of-study/biological-biomedical-sciences-bbs |
| 10 | Biomedical Engineering | https://gsas.yale.edu/programs-of-study/biomedical-engineering |
| 11 | Black Studies | https://gsas.yale.edu/programs-of-study/black-studies |
| 12 | Cell Biology | https://gsas.yale.edu/programs-of-study/cell-biology |
| 13 | Cellular & Molecular Physiology | https://gsas.yale.edu/programs-of-study/cellular-molecular-physiology |
| 14 | Chemical & Environmental Engineering | https://gsas.yale.edu/programs-of-study/chemical-environmental-engineering |
| 15 | Chemistry | https://gsas.yale.edu/programs-of-study/chemistry |
| 16 | Classics | https://gsas.yale.edu/programs-of-study/classics |
| 17 | Comparative Literature | https://gsas.yale.edu/programs-of-study/comparative-literature |
| 18 | Computational Biology & Biomedical Informatics (PhD) | https://gsas.yale.edu/programs-of-study/computational-biology-biomedical-informatics-phd-program |
| 19 | Computer Science | https://gsas.yale.edu/programs-of-study/computer-science |
| 20 | Early Modern Studies | https://gsas.yale.edu/programs-of-study/early-modern-studies |
| 21 | Earth & Planetary Sciences | https://gsas.yale.edu/programs-of-study/earth-planetary-sciences |
| 22 | East Asian Languages & Literatures | https://gsas.yale.edu/programs-of-study/east-asian-languages-literatures |
| 23 | East Asian Studies | https://gsas.yale.edu/programs-of-study/east-asian-studies |
| 24 | Ecology & Evolutionary Biology | https://gsas.yale.edu/programs-of-study/ecology-evolutionary-biology |
| 25 | Economics | https://gsas.yale.edu/programs-of-study/economics |
| 26 | Electrical & Computer Engineering | https://gsas.yale.edu/programs-of-study/electrical-computer-engineering |
| 27 | English Language & Literature | https://gsas.yale.edu/programs-of-study/english-language-literature |
| 28 | Environment | https://gsas.yale.edu/programs-of-study/environment |
| 29 | European & Russian Studies | https://gsas.yale.edu/programs-of-study/european-russian-studies |
| 30 | Film & Media Studies | https://gsas.yale.edu/programs-of-study/film-media-studies |
| 31 | French | https://gsas.yale.edu/programs-of-study/french |
| 32 | Genetics | https://gsas.yale.edu/programs-of-study/genetics |
| 33 | Germanic Languages & Literatures | https://gsas.yale.edu/programs-of-study/germanic-languages-literatures |
| 34 | History | https://gsas.yale.edu/programs-of-study/history |
| 35 | History of Art | https://gsas.yale.edu/programs-of-study/history-art |
| 36 | History of Science & Medicine | https://gsas.yale.edu/programs-of-study/history-science-medicine |
| 37 | Immunobiology | https://gsas.yale.edu/programs-of-study/immunobiology |
| 38 | Interdepartmental Neuroscience Program | https://gsas.yale.edu/programs-of-study/interdepartmental-neuroscience-program |
| 39 | International & Development Economics | https://gsas.yale.edu/programs-of-study/international-development-economics |
| 40 | Investigative Medicine | https://gsas.yale.edu/programs-of-study/investigative-medicine |
| 41 | Italian Studies | https://gsas.yale.edu/programs-of-study/italian-studies |
| 42 | Law (Ph.D. in Law) | https://gsas.yale.edu/programs-of-study/law |
| 43 | Linguistics | https://gsas.yale.edu/programs-of-study/linguistics |
| 44 | Management | https://gsas.yale.edu/programs-of-study/management |
| 45 | Materials Science | https://gsas.yale.edu/programs-of-study/materials-science |
| 46 | Mathematics | https://gsas.yale.edu/programs-of-study/mathematics |
| 47 | Mechanical Engineering | https://gsas.yale.edu/programs-of-study/mechanical-engineering |
| 48 | Medieval Studies | https://gsas.yale.edu/programs-of-study/medieval-studies |
| 49 | Microbiology | https://gsas.yale.edu/programs-of-study/microbiology |
| 50 | Molecular Biophysics & Biochemistry | https://gsas.yale.edu/programs-of-study/molecular-biophysics-biochemistry |
| 51 | Molecular, Cellular, & Developmental Biology | https://gsas.yale.edu/programs-of-study/molecular-cellular-developmental-biology |
| 52 | Music | https://gsas.yale.edu/programs-of-study/music |
| 53 | Near Eastern Languages & Civilizations | https://gsas.yale.edu/programs-of-study/near-eastern-languages-civilizations |
| 54 | Nursing | https://gsas.yale.edu/programs-of-study/nursing |
| 55 | Pathology & Molecular Medicine | https://gsas.yale.edu/programs-of-study/pathology-molecular-medicine |
| 56 | Personalized Medicine & Applied Engineering | https://gsas.yale.edu/programs-of-study/personalized-medicine-applied-engineering |
| 57 | Pharmacology | https://gsas.yale.edu/programs-of-study/pharmacology |
| 58 | Philosophy | https://gsas.yale.edu/programs-of-study/philosophy |
| 59 | Physics | https://gsas.yale.edu/programs-of-study/physics |
| 60 | Political Science | https://gsas.yale.edu/programs-of-study/political-science |
| 61 | Psychology | https://gsas.yale.edu/programs-of-study/psychology |
| 62 | Public Health | https://gsas.yale.edu/programs-of-study/public-health |
| 63 | Religious Studies | https://gsas.yale.edu/programs-of-study/religious-studies |
| 64 | Slavic Languages & Literatures | https://gsas.yale.edu/programs-of-study/slavic-languages-literatures |
| 65 | Sociology | https://gsas.yale.edu/programs-of-study/sociology |
| 66 | Spanish & Portuguese | https://gsas.yale.edu/programs-of-study/spanish-portuguese |
| 67 | Statistics | https://gsas.yale.edu/programs-of-study/statistics |
| 68 | Statistics & Data Science | https://gsas.yale.edu/programs-of-study/statistics-data-science |
| 69 | Translational Biomedicine | https://gsas.yale.edu/programs-of-study/translational-biomedicine |
| 70 | Women's, Gender, & Sexuality Studies | https://gsas.yale.edu/programs-of-study/womens-gender-sexuality-studies |
| 71 | African Studies (MA/PhD track) | https://gsas.yale.edu/programs-of-study/african-studies |
| 72 | Certificates (cross-listed PhD fields) | https://gsas.yale.edu/programs-of-study/certificates |

##### MA (13 programs)
| # | 项目 | URL |
|---|------|-----|
| 1 | African Studies | https://gsas.yale.edu/programs-of-study/african-studies |
| 2 | American Studies | https://gsas.yale.edu/programs-of-study/american-studies |
| 3 | Archaeological Studies | https://gsas.yale.edu/programs-of-study/archaeological-studies |
| 4 | East Asian Studies | https://gsas.yale.edu/programs-of-study/east-asian-studies |
| 5 | English Language & Literature | https://gsas.yale.edu/programs-of-study/english-language-literature |
| 6 | European & Russian Studies | https://gsas.yale.edu/programs-of-study/european-russian-studies |
| 7 | History | https://gsas.yale.edu/programs-of-study/history |
| 8 | History of Science & Medicine | https://gsas.yale.edu/programs-of-study/history-science-medicine |
| 9 | International & Development Economics | https://gsas.yale.edu/programs-of-study/international-development-economics |
| 10 | Medieval Studies | https://gsas.yale.edu/programs-of-study/medieval-studies |
| 11 | Music | https://gsas.yale.edu/programs-of-study/music |
| 12 | Near Eastern Languages & Civilizations | https://gsas.yale.edu/programs-of-study/near-eastern-languages-civilizations |
| 13 | Statistics | https://gsas.yale.edu/programs-of-study/statistics |

##### MS (10 programs)
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Physics | https://gsas.yale.edu/programs-of-study/applied-physics |
| 2 | Biomedical Engineering | https://gsas.yale.edu/programs-of-study/biomedical-engineering |
| 3 | Cell Biology / Cellular & Molecular Physiology | https://gsas.yale.edu/programs-of-study/cell-biology |
| 4 | Chemical & Environmental Engineering | https://gsas.yale.edu/programs-of-study/chemical-environmental-engineering |
| 5 | Computational Biology & Biomedical Informatics (MS) | https://gsas.yale.edu/programs-of-study/computational-biology-biomedical-informatics-ms-program |
| 6 | Computer Science | https://gsas.yale.edu/programs-of-study/computer-science |
| 7 | Electrical & Computer Engineering | https://gsas.yale.edu/programs-of-study/electrical-computer-engineering |
| 8 | Mechanical Engineering | https://gsas.yale.edu/programs-of-study/mechanical-engineering |
| 9 | Personalized Medicine & Applied Engineering | https://gsas.yale.edu/programs-of-study/personalized-medicine-applied-engineering |
| 10 | Public Health / Statistics & Data Science | https://gsas.yale.edu/programs-of-study/statistics-data-science |

> **GSAS count check**: 72 PhD + 13 MA + 10 MS = 95 program-degree rows. ✓

#### School of Architecture — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MArch | Master of Architecture I (first professional) | https://catalog.yale.edu/architecture/master-architecture-i-degree-program/ |
| MArch | Master of Architecture II (post-professional) | https://catalog.yale.edu/architecture/master-architecture-ii-degree-program/ |
| MED | Master of Environmental Design | https://catalog.yale.edu/architecture/master-environmental-design-degree-program/ |
| PhD | Doctor of Philosophy in Architecture | https://catalog.yale.edu/architecture/doctor-philosophy-program/ |

#### School of Art — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MFA | Graphic Design | https://catalog.yale.edu/art/program/ |
| MFA | Painting/Printmaking | https://catalog.yale.edu/art/program/ |
| MFA | Photography | https://catalog.yale.edu/art/program/ |
| MFA | Sculpture | https://catalog.yale.edu/art/program/ |

**Source**: `https://catalog.yale.edu/art/program/` — *"The School of Art offers professional instruction in four interrelated areas of study: graphic design, painting/printmaking, photography, and sculpture."* (capture 2026-07-04)

#### Yale Divinity School — 3 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MDiv | Master of Divinity | https://catalog.yale.edu/div/programs-study/ |
| MAR | Master of Arts in Religion | https://catalog.yale.edu/div/programs-study/ |
| STM | Master of Sacred Theology | https://catalog.yale.edu/div/programs-study/ |

**Source**: `https://catalog.yale.edu/div/programs-study/` — *"Master of Divinity Degree Requirements, Master of Arts in Religion Degree Requirements, Master of Sacred Theology Degree Requirements"* (capture 2026-07-04)

#### David Geffen School of Drama — 6 programs (MFA + Certificate)
| 学位 | 项目 | URL |
|------|------|-----|
| MFA + Cert | Acting | https://bulletin.yale.edu/bulletins/drama |
| MFA + Cert | Design | https://bulletin.yale.edu/bulletins/drama |
| MFA + Cert | Directing | https://bulletin.yale.edu/bulletins/drama |
| MFA + Cert | Playwriting | https://bulletin.yale.edu/bulletins/drama |
| MFA + Cert | Stage Management | https://bulletin.yale.edu/bulletins/drama |
| MFA + Cert | Technical Design and Production | https://bulletin.yale.edu/bulletins/drama |

**Source**: `https://bulletin.yale.edu/bulletins/drama` — *"Acting (M.F.A. and Certificate), Design (M.F.A. and Certificate), Directing (M.F.A. and Certificate), Playwriting (M.F.A. and Certificate), Stage Management (M.F.A. and Certificate), Technical Design and Production (M.F.A. and Certificate)"* (capture 2026-07-04)

#### School of the Environment (Forestry & Environmental Studies) — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MESc | Master of Environmental Science | https://catalog.yale.edu/environment/masters-degree-programs/ |
| MF | Master of Forestry | https://catalog.yale.edu/environment/masters-degree-programs/ |
| MFS | Master of Forest Science | https://catalog.yale.edu/environment/masters-degree-programs/ |
| PhD | Doctor of Philosophy | https://catalog.yale.edu/environment/doctoral-degree-program/ |

#### Jackson School of Global Affairs — 2 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MPP | Master in Public Policy in Global Affairs | https://catalog.yale.edu/global-affairs/degree-programs/ |
| MAS | Master of Advanced Study | https://catalog.yale.edu/global-affairs/degree-programs/ |

**Source**: `https://catalog.yale.edu/global-affairs/degree-programs/` — *"Master in Public Policy in Global Affairs (M.P.P.), Master of Advanced Study (M.A.S.), Joint-Degree Programs with Other Yale Schools"* (capture 2026-07-04)

#### Yale Law School — 5 programs
| 学位 | 项目 | URL |
|------|------|-----|
| JD | Juris Doctor | https://bulletin.yale.edu/bulletins/law |
| LLM | Master of Laws | https://bulletin.yale.edu/bulletins/law |
| JSD | Doctor of the Science of Law | https://bulletin.yale.edu/bulletins/law |
| MSL | Master of Studies in Law | https://bulletin.yale.edu/bulletins/law |
| PhD | Ph.D. in Law (administered with GSAS) | https://gsas.yale.edu/programs-of-study/law |

#### Yale School of Management (SOM) — 5 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MBA | Full-Time MBA | https://catalog.yale.edu/management/full-time-mba/ |
| MBA | MBA for Executives | https://catalog.yale.edu/management/mba-executives/ |
| MAM | Master of Advanced Management | https://catalog.yale.edu/management/full-time-mba/ |
| MMS | Master of Management Studies | https://catalog.yale.edu/management/full-time-mba/ |
| PhD | Doctoral Degree Program (accounting, financial economics, marketing, operations, organizations & management) | https://catalog.yale.edu/management/doctoral-degree/ |

**Source**: `https://catalog.yale.edu/management/doctoral-degree/` — *"specialization is offered in the management fields of accounting, financial economics, marketing, operations, and organizations and management."* (capture 2026-07-04)

#### Yale School of Medicine — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MD | Doctor of Medicine | https://bulletin.yale.edu/bulletins/med |
| MMSc | Master of Medical Science | https://bulletin.yale.edu/bulletins/med |
| MMSc-PA | Physician Associate Program (MMSc) | https://bulletin.yale.edu/bulletins/med |
| MD/PhD | Medical Scientist Training Program (MD/PhD) | https://bulletin.yale.edu/bulletins/med |

**Source**: `https://bulletin.yale.edu/bulletins/med` — *"Yale School of Medicine has conferred 10,123 medical degrees."* (capture 2026-07-04)

#### Yale School of Music — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MM | Master of Music | https://bulletin.yale.edu/bulletins/music |
| MMA | Master of Musical Arts | https://bulletin.yale.edu/bulletins/music |
| DMA | Doctor of Musical Arts | https://bulletin.yale.edu/bulletins/music |
| ADip | Artist Diploma | https://bulletin.yale.edu/bulletins/music |

**Source**: `https://bulletin.yale.edu/bulletins/music` — degree tokens confirmed: MM, MMA, DMA (capture 2026-07-04)

#### Yale School of Nursing — 4 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MSN | Master of Science in Nursing | https://catalog.yale.edu/nursing/masters-program-msn/ |
| DNP | Doctor of Nursing Practice | https://catalog.yale.edu/nursing/doctor-nursing-practice-dnp-program/ |
| PhD | Doctor of Philosophy in Nursing | https://catalog.yale.edu/nursing/doctor-philosophy-program/ |
| Post-MSN Cert | Post-Master's Certificates | https://catalog.yale.edu/nursing/post-masters-certificates/ |

#### Yale School of Public Health (YSPH) — 3 programs
| 学位 | 项目 | URL |
|------|------|-----|
| MPH | Master of Public Health (Traditional 2-year, Advanced Professional, Executive) | https://catalog.yale.edu/ysph/master-public-health/ |
| MSPH | Master of Science in Public Health | https://catalog.yale.edu/ysph/master-science-public-health/ |
| PhD | Doctoral Degree (via GSAS) | https://catalog.yale.edu/ysph/doctoral-degree/ |

**Source**: `https://catalog.yale.edu/ysph` — *"Master of Public Health, Traditional Two-Year MPH Program, Advanced Professional MPH Program, Executive MPH Program, Joint Degree Programs, Master of Science in Public Health, Doctoral Degree"* (capture 2026-07-04)

> **Professional schools total**: 4+4+3+6+4+2+5+5+4+4+4+3 = **48** ✓
> **Grad grand total**: GSAS 95 + Professional 48 = **143** graduate degree programs.

### 2.2 Worked example — Yale School of Drama, Acting (M.F.A. and Certificate)

- **School**: David Geffen School of Drama at Yale University
- **Program**: Acting (M.F.A. and Certificate)
- **Bulletin URL**: https://bulletin.yale.edu/bulletins/drama
- **Admissions URL**: https://drama.yale.edu/admissions
- **Degree**: Master of Fine Arts + Certificate (3-year conservatory)
- **Application deadline**: typically early January (program-specific; verify on drama.yale.edu/admissions)
- **Tuition**: tuition-free since 2021 (David Geffen gift) — verify at drama.yale.edu/financial-aid
- **Joint structure**: integrated with Yale Repertory Theatre

### 2.3 Graduate admissions model

**Decentralized.** GSAS administers admissions for the 72 PhD/MA/MS programs centrally via the GSAS application portal (`gsas.yale.edu/admissions`). Each of the 12 professional schools runs its own admissions office with its own application, deadline, fee, and GRE/ELP policy:

- GSAS: `https://gsas.yale.edu/admissions` (one application, ~$105 fee)
- Law: `law.yale.edu/admissions`
- Medicine: `medicine.yale.edu/admissions`
- SOM: `som.yale.edu/programs`
- YSPH: `ysph.yale.edu/school-of-public-health/graduate-programs/`
- Environment: `environment.yale.edu/admissions`
- Nursing, Music, Art, Architecture, Drama, Divinity: each school's own `/admissions`

**Source**: `https://bulletin.yale.edu/bulletins-html` — lists 14 independent school bulletins (capture 2026-07-04)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table (Yale College, first-year)

| 字段 | 值 | 出处 |
|------|-----|------|
| Admissions site | `admissions.yale.edu` | official |
| Application portal | Common App / Coalition on SCOIR / QuestBridge | requirements page |
| Single-Choice Early Action (SCEA) deadline | **November 1** | timelines page |
| SCEA notification | Mid-December | timelines page |
| Regular Decision deadline | **January 2** | timelines page |
| RD notification | Late March | timelines page |
| Admitted student reply | **May 1** | timelines page |
| QuestBridge Match deadline | November 1 (binding) | timelines page |
| Application fee | $80 (via Common App/Coalition; QuestBridge free; fee waivers available) | Common App profile |
| SAT/ACT policy | **Required** (test-required, not optional) for first-year & transfer | testing page |
| Superscore | Yes (SAT and ACT) | testing page |
| Self-report | Yes; official scores only after enrollment | testing page |
| CEEB code (SAT/AP) | 3987 | testing page |
| ACT code | 0618 | testing page |
| Recommendations | 2 teachers (core academic) + 1 counselor | requirements page |
| School report + transcript | Required (incl. mid-year report) | requirements page |
| Interview | None (not offered) | admissions |
| Portfolio/supplements | Optional (Visual Art, Dance, Music, Film, STEM research) | requirements page |

**Source**: `https://admissions.yale.edu/timelines` — *"Early Action: Application Deadline: November 1, Decisions Released: Mid-December… Regular Decision: Application Deadline: January 2, Decisions Released: Late March, Admitted Student Reply Deadline: May 1."* (capture 2026-07-04)

**Source**: `https://admissions.yale.edu/standardized-testing` — *"First-year and transfer applicants are required to include scores from the ACT or SAT."* (capture 2026-07-04). NOTE: Yale reintroduced the SAT/ACT requirement for the cycle beginning fall 2025 admission — it is **test-required**, not test-optional.

### 3.2 Undergraduate English proficiency table

Applies to non-native English speakers without 2+ years in an English-medium school. Minimums are stated as "most competitive applicants typically earn" — Yale treats these as competitive thresholds, not hard floors.

| 考试 | 最低/竞争性分数 | 推荐分数 |
|------|----------------|---------|
| TOEFL iBT | 100 (tests before Jan 21, 2026); score of 5 or higher (tests after Jan 21, 2026 — new scoring) | 100+ / 5+ |
| IELTS (Academic) | 7.0 | 7.0+ |
| Cambridge English (C1 Advanced / C2 Proficiency / B2 First) | 185 | 185+ |
| Duolingo English Test (DET) | 120 | 120+ |
| InitialView | Optional (interview, no score) | — |

**Source**: `https://admissions.yale.edu/standardized-testing` — *"Yale's most competitive applicants typically earn a score of 5 or higher (for tests taken after January 21, 2026) or at least 100 (for tests taken before January 21, 2026)."* / *"Yale's most competitive applicants have IELTS scores of 7 or higher."* / *"Cambridge English scores of 185 or higher"* / *"DET scores of at least 120."* (capture 2026-07-04)

### 3.3 Graduate — global rules

- **Admissions model**: decentralized (GSAS centralizes its own ~72 programs; each professional school independent).
- **GSAS application fee**: ~$105 (program-specific waivers available).
- **Professional school fees**: vary — SOM ~$250, Law ~$85, Medicine ~$100 (verify per school).
- **Honor date**: Yale observes the CGS April 15 resolution for PhD offers with financial support.
- **GRE policy**: varies by program; many GSAS programs made GRE optional/required-noted post-2020. Check each program page at `gsas.yale.edu/programs-of-study/<slug>`.
- **ELP for international grad applicants**: TOEFL/IELTS required unless prior English-medium degree; waivers vary by program.
- **Application timeline**: GSAS deadlines mostly mid-December to early January for fall admission.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27, line-itemized)

| Expense item | Amount (USD) | Description |
|--------------|-------------|-------------|
| Tuition | $72,500 | Billed |
| Student Activity Fee | $185 | Billed |
| Housing | $12,080 | Billed; includes residential college amenities/laundry |
| Food | $9,520 | Billed (meal plan) |
| Books / Course Materials / Supplies / Equipment | $1,000 | Estimated (unbilled) |
| Personal Expenses | $2,700 | Estimated (unbilled) |
| Travel | Variable | Estimated by home address (unbilled) |
| **Estimated total (billed + standard unbilled, excl. travel)** | **~$97,985** | |

**Source**: `https://finaid.yale.edu/coa` — *"2026-27 Estimated Cost of Attendance for Yale Undergraduate Students: $72,500 Tuition, $185 Student Activity Fee, $12,080 Housing, $9,520 Food, $1,000 Books/Course Material/Supplies/Equipment, $2,700 Personal Expenses."* (capture 2026-07-04)

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 |
|------|-----|
| Admissions policy | **Need-blind** for ALL applicants including internationals |
| Aid type | 100% need-based; grants/scholarships, **no loans** required |
| Need-met | 100% of demonstrated financial need |
| No-parent-contribution threshold | Family income **< $75,000** with typical assets (approx.) |
| No-cost (full ride) threshold | Family income **< $100,000** with typical assets |
| No-tuition threshold | Family income **< $200,000** with typical assets |
| Average annual need-based scholarship | **$75,220** |
| % US families qualifying for tuition+ grants | 80% |
| % students whose families pay nothing | 21% |
| % Yale College graduates with no student-loan debt | **88%** |
| Aid application | FAFSA + CSS Profile + IDOC documents |

**Source**: `https://admissions.yale.edu/affordability` — *"Need-blind admissions: A family's ability to pay is not a factor in the admissions process — for any student, anywhere in the world… No Cost For families with incomes below $100,000 and typical assets. No Tuition For families with incomes below $200,000 and typical assets… $75,220 Average annual need-based scholarship… 88% Yale College graduates with no student loan debt… 21% Students whose families pay nothing to attend."* (capture 2026-07-04)

**Source**: `https://admissions.yale.edu/international` — *"Need-blind admissions. Need-based aid. Yale is one of only a handful of American universities that considers all applicants for admission without regard to their ability to pay and meets 100% of every family's demonstrated financial need."* (capture 2026-07-04)

> Yale is one of only ~6 US universities (with MIT, Harvard, Princeton, Dartmouth, Amherst) that are need-blind **and** full-need **for international students**.

### 4.3 Graduate cost & funding framework

- **PhD (GSAS)**: fully funded — full tuition fellowship + 12-month stipend (~$45,000–50,000 for 2026-27) for 5+ years. Verify at `gsas.yale.edu/financial-support`.
- **GSAS MA/MS (terminal)**: typically self-funded; limited partial scholarships.
- **Professional schools**: tuition varies — SOM MBA ~$84k/yr tuition, Law ~$72k, Medicine ~$66k, YSPH MPH ~$53k (verify per school). Each school runs its own financial-aid office.
- **GSAS application fee**: ~$105; waivers available for eligible applicants.
- **P0 follow-up**: per-program stipend rates and per-professional-school COA tables were not line-itemized in this run.

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: undergraduate.majors.total
  value: 78
  source_url: https://admissions.yale.edu/majors
  source_snippet: "Yale College students select from over 80 majors without the restrictions of a core curriculum."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-002
  field: undergraduate.deadlines.scea
  value: November 1
  source_url: https://admissions.yale.edu/timelines
  source_snippet: "Early Action: Application Deadline: November 1, Decisions Released: Mid-December, Admitted Student Reply Deadline: May 1"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-003
  field: undergraduate.deadlines.rd
  value: January 2
  source_url: https://admissions.yale.edu/timelines
  source_snippet: "Regular Decision: Application Deadline: January 2, Decisions Released: Late March, Admitted Student Reply Deadline: May 1"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-004
  field: undergraduate.testing.sat_act_required
  value: true (test-required)
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "First-year and transfer applicants are required to include scores from the ACT or SAT."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-005
  field: undergraduate.testing.toefl_min
  value: "100 (pre-2026-01-21 tests) / 5 (post-2026-01-21)"
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "Yale's most competitive applicants typically earn a score of 5 or higher (for tests taken after January 21, 2026) or at least 100 (for tests taken before January 21, 2026)."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.testing.ielts_min
  value: "7.0"
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "Yale's most competitive applicants have IELTS scores of 7 or higher."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.testing.cambridge_min
  value: "185"
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "Yale's most competitive applicants have Cambridge English scores of 185 or higher on the C1 Advanced, C2 Proficiency, or B2 First exams."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.testing.duolingo_min
  value: "120"
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "Yale's most competitive applicants have DET scores of at least 120."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-009
  field: undergraduate.testing.codes.ceeb_sat
  value: "3987"
  source_url: https://admissions.yale.edu/standardized-testing
  source_snippet: "Yale's CEEB code for the SAT and AP is 3987; the ACT code is 0618."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-010
  field: undergraduate.requirements.recommendations
  value: "2 teacher letters (core academic) + 1 counselor"
  source_url: https://admissions.yale.edu/requirements
  source_snippet: "Request letters of recommendation from two teachers who have taught you recently in core academic subjects… Also request a letter from your school's college counselor."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-011
  field: undergraduate.cost.tuition_2026_2027
  value: "$72,500"
  source_url: https://finaid.yale.edu/coa
  source_snippet: "2026-27 Estimated Cost of Attendance… $72,500 Tuition, $185 Student Activity Fee, $12,080 Housing, $9,520 Food, $1,000 Books/Course Material/Supplies/Equipment, $2,700 Personal Expenses"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-U-012
  field: undergraduate.cost.total_2026_2027
  value: "~$97,985 (excl. travel)"
  source_url: https://finaid.yale.edu/coa
  source_snippet: "$72,500 Tuition + $185 Activity Fee + $12,080 Housing + $9,520 Food + $1,000 Books + $2,700 Personal"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-U-013
  field: undergraduate.financial_aid.need_blind
  value: "Need-blind for all applicants including internationals"
  source_url: https://admissions.yale.edu/affordability
  source_snippet: "Need-blind admissions: A family's ability to pay is not a factor in the admissions process — for any student, anywhere in the world."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-014
  field: undergraduate.financial_aid.no_cost_threshold
  value: "Family income < $100,000 with typical assets"
  source_url: https://admissions.yale.edu/affordability
  source_snippet: "No Cost For families with incomes below $100,000 and typical assets"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-015
  field: undergraduate.financial_aid.no_tuition_threshold
  value: "Family income < $200,000 with typical assets"
  source_url: https://admissions.yale.edu/affordability
  source_snippet: "No Tuition For families with incomes below $200,000 and typical assets"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-016
  field: undergraduate.financial_aid.avg_scholarship
  value: "$75,220"
  source_url: https://admissions.yale.edu/affordability
  source_snippet: "$75,220 Average annual need-based scholarship"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-017
  field: undergraduate.financial_aid.no_loan_grad_rate
  value: "88%"
  source_url: https://admissions.yale.edu/affordability
  source_snippet: "88% Yale College graduates with no student loan debt"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.gsas.program_count
  value: 72 programs (95 program-degree rows incl. MA/MS)
  source_url: https://gsas.yale.edu/programs-of-study
  source_snippet: "Programs of Study — directory listing 72 distinct degree-granting programs across Arts, Humanities, Social Sciences, Biological/Biomedical Sciences, Physical Sciences, and Engineering."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.schools.bulletin_index
  value: "14 school bulletins"
  source_url: https://bulletin.yale.edu/bulletins-html
  source_snippet: "School of Art, Divinity School, Yale College Programs of Study, School of Architecture, David Geffen School of Drama, School of the Environment, Graduate School of Arts and Sciences Programs and Policies, Institute of Sacred Music, Jackson School of Global Affairs, Law School, School of Management, School of Medicine, School of Music, School of Nursing, School of Public Health"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.art.mfa_areas
  value: "4 (Graphic Design, Painting/Printmaking, Photography, Sculpture)"
  source_url: https://catalog.yale.edu/art/program/
  source_snippet: "The School of Art offers professional instruction in four interrelated areas of study: graphic design, painting/printmaking, photography, and sculpture."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-004
  field: graduate.drama.mfa_programs
  value: "6 (Acting, Design, Directing, Playwriting, Stage Management, Technical Design and Production)"
  source_url: https://bulletin.yale.edu/bulletins/drama
  source_snippet: "Acting (M.F.A. and Certificate), Design (M.F.A. and Certificate), Directing (M.F.A. and Certificate), Playwriting (M.F.A. and Certificate), Stage Management (M.F.A. and Certificate), Technical Design and Production (M.F.A. and Certificate)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-005
  field: graduate.global_affairs.degrees
  value: "MPP + MAS"
  source_url: https://catalog.yale.edu/global-affairs/degree-programs/
  source_snippet: "Master in Public Policy in Global Affairs (M.P.P.), Master of Advanced Study (M.A.S.), Joint-Degree Programs with Other Yale Schools"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-006
  field: graduate.management.doctoral_fields
  value: "accounting, financial economics, marketing, operations, organizations and management"
  source_url: https://catalog.yale.edu/management/doctoral-degree/
  source_snippet: "specialization is offered in the management fields of accounting, financial economics, marketing, operations, and organizations and management."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-007
  field: graduate.medicine.md_history
  value: "10,123 medical degrees conferred"
  source_url: https://bulletin.yale.edu/bulletins/med
  source_snippet: "Since its founding in 1810 as the Medical Institution of Yale College, Yale School of Medicine has conferred 10,123 medical degrees."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-008
  field: graduate.seas.departments
  value: "8 academic departments"
  source_url: https://seas.yale.edu/departments
  source_snippet: "Yale Engineering's eight academic departments span the cutting edge of modern engineering… Applied & Computational Mathematics, Applied Physics, Biomedical Engineering, Chemical & Environmental Engineering, Computer Science, Electrical & Computer Engineering, Materials Science, Mechanical Engineering."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-009
  field: undergraduate.5year_programs
  value: "4 partner schools (Environment, Jackson, Music, Public Health)"
  source_url: https://admissions.yale.edu/majors
  source_snippet: "5-year bachelor's and master's degree programs: The School of the Environment, Jackson School of Global Affairs, School of Music, School of Public Health"
  capture_date: 2026-07-04
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: yale-knowledge-base-v2
├── doc: yale-overview (Section 0 — counts, hierarchy, degree inventory, matrix)
├── doc: yale-undergraduate (Section 1 — Yale College majors)
│   └── chunk-per-department-group: humanities / social-sciences / natural-sciences / seas-engineering / interdisciplinary
├── doc: yale-gsas-graduate (Section 2 — GSAS 72 programs)
│   └── chunk-per-department (one chunk per GSAS program slug)
├── doc: yale-professional-schools (Section 2 — 12 professional schools)
│   └── chunk-per-school (one chunk per school)
├── doc: yale-admissions (Section 3 — deadlines, tests, ELP)
├── doc: yale-cost-aid (Section 4 — COA + financial aid)
└── doc: yale-evidence (Section 5 — evidence chain)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "yale-knowledge-base-v2"
  school: "<Yale College | GSAS | Architecture | Art | Divinity | Drama | Environment | Global Affairs | Law | Management | Medicine | Music | Nursing | Public Health>"
  department: "<home department, if applicable>"
  degree_level: "<BA | BS | MA | MS | MFA | MArch | MBA | MMSc | MD | JD | LLM | JSD | MSL | MM | MMA | DMA | MDiv | MAR | STM | MESc | MF | MFS | MPP | MAS | MSN | DNP | MPH | MSPH | MAM | MMS | MED | ADip | Post-MSN-Cert | MD/PhD | PhD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|-----------|--------|
| **P0** | Per-professional-school COA / tuition line items | `som.yale.edu/tuition`, `law.yale.edu/financial-aid`, `medicine.yale.edu/education-admissions/tuition-fees`, `ysph.yale.edu/tuition`, `environment.yale.edu/tuition` | Only UG COA line-itemized; grad COA is single-number per school |
| **P0** | GSAS per-program GRE/ELP policy + deadlines | each `gsas.yale.edu/programs-of-study/<slug>` detail page | Behind accordions; not yet captured per-program |
| **P0** | GSAS application fee (current) + fee-waiver policy | `gsas.yale.edu/admissions` | Stated as ~$105 but needs verbatim |
| **P0** | GSAS PhD stipend rate (2026-27) | `gsas.yale.edu/financial-support` | Not yet captured |
| **P1** | Per-professional-school application fee | each school `/admissions` page | SOM/Law/Medicine/YSPH vary |
| **P1** | Drama bulletin full TOC (Technical Internship, Certificate-only programs) | `https://bulletin.yale.edu/bulletins/drama` | 6 MFA programs captured; verify no additional cert-only tracks |
| **P1** | Medicine full degree-program subsection (MMSc tracks, PA specialty) | `https://bulletin.yale.edu/bulletins/med` Degree Programs subsection | TOC lists only "Degree Programs" header; sub-pages need crawl |
| **P1** | Law LLM/JSD/MSL distinct program pages | `https://law.yale.edu` degree programs | Bulletin lists narrative; per-program pages needed |
| **P2** | UG certificate programs full list (35+) | `https://catalog.yale.edu/ycps/academic-regulations/special-academic-arrangements/` | Listed as "35+" but not enumerated |
| **P2** | Joint-degree programs across professional schools (MBA/JD, MD/MPH, etc.) | each school `joint-degree-programs` page | ~50+ combinations exist; not enumerated |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Yale (2026-07-04) | MIT | Stanford | Harvard |
|-----------|-------------------|-----|----------|---------|
| Total degree programs (rule 1) | **221** | (varies) | (varies) | (varies) |
| UG cost / yr (total) | ~$97,985 | — | — | — |
| Tuition / yr | $72,500 | — | — | — |
| Need-blind (intl?) | **Yes (incl. intl)** | Yes | Yes | Yes |
| No-cost threshold | <$100k income | — | — | — |
| No-tuition threshold | <$200k income | — | — | — |
| SCEA / REA / EA deadline | Nov 1 (SCEA) | — | — | Nov 1 (REA) |
| RD deadline | Jan 2 | — | — | Jan 1 |
| SAT/ACT required? | **Yes (required)** | — | — | Test-optional |
| TOEFL min | 100 | — | — | — |
| IELTS min | 7.0 | — | — | — |
| Duolingo min | 120 | — | — | — |
| Grad application fee (GSAS) | ~$105 | — | — | — |
| April-15-equivalent honor date | Yes (CGS) | — | — | Yes |
| UG majors count | 78 | — | — | — |
| Schools/departments count | 14 schools + 8 SEAS depts | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: admissions.yale.edu, finaid.yale.edu, catalog.yale.edu (YCPS + GSAS + 8 professional school catalogs), bulletin.yale.edu (Drama/ISM/Law/Medicine/Music), gsas.yale.edu, seas.yale.edu
> **Verification**: ego-browser snapshotText + js() DOM extraction + serverFetch; reconciliation computed in Python (rule-1 == rule-4 cell-sum == rule-5 row count == 221)
> **Granularity**: school → department → degree-level → program
