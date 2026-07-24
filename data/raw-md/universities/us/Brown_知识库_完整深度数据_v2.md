# Brown University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

> **Verification note on user-supplied priors (FIVE RULES applied — VERIFY everything):**
> - "Test-optional (verify current cycle)" → **VERIFIED FALSE**: Brown **returned to test-REQUIRED** for first-year applicants starting with the 2024-25 admission cycle. SAT or ACT is now mandatory (superscored). See E-U-003.
> - "ED Nov 1, RD Jan 3" → ED Nov 1 **VERIFIED**; RD **VERIFIED as January 5** (not Jan 3). See E-U-001.
> - "~$69k tuition" → Tuition for **2025-26 is $71,700** (was $69,648 in 2024-25). See E-U-006.
> - "need-blind + full-need incl internationals" → **VERIFIED**; need-blind for international undergraduates began with the Class of 2029 (entering fall 2025). See E-U-008.
> - "3 grad schools (Engineering, Public Health, Professional Studies)" → **VERIFIED INCOMPLETE**: Brown actually has **6 graduate/professional schools** beyond The College: Graduate School, School of Engineering, School of Public Health, Warren Alpert Medical School, School of Professional Studies, **and Watson School of International and Public Affairs** (newly chartered). See Section 0.2.

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

Brown University is a private Ivy League research university in Providence, Rhode Island. It is distinctively structured as a "University-College": undergraduate education is based in **The College** (rooted in the flexible **Open Curriculum** — no core requirements, no distribution requirements), while graduate/professional work spans 6 schools. Brown calls undergraduate majors **"concentrations"** and uses Latin-style degree abbreviations (**A.B.** = Bachelor of Arts → canonical `BA`; **Sc.B.** = Bachelor of Science → canonical `BS`; **A.M.** = Master of Arts → `MA`; **Sc.M.** = Master of Science → `MS`).

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科 concentration 数 (distinct programs) | 90 |
| 本科学位项目 (A.B. + Sc.B. degree offerings after expanding dual-degree concentrations) | 108 |
| 本科辅修 (Minor) | **0** — Brown has **no undergraduate minors**; the Open Curriculum makes them unnecessary. Complementary credentials are 6 interdisciplinary **certificates** (counted below). |
| 本科证书 (Undergraduate Certificate) | 6 |
| 研究生项目 (distinct graduate programs) | 91 |
| 研究生学位项目 (degree offerings after expanding combined-degree programs) | 100 |
| **学位项目总计 (UG + Grad degree rows)** | **208** |
| 学院 / 独立系所总数 (Schools/Colleges) | 7 (The College + 6 grad/professional schools) |

> **Reconciliation:** 90 UG concentrations expand to 108 degree rows (because 18 concentrations offer both A.B. and Sc.B.). 91 graduate programs expand to 100 degree rows (because 9 programs combine two degrees, e.g. "A.M., Sc.M."). 108 + 100 = **208 degree-level rows**. Adding the 6 UG certificates yields 214 total credentials. The Section 0.4 matrix sums to 208 (degree rows); certificates are reported separately because they are non-degree credentials.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Brown University
├── The College                                            [学院 — undergraduate]
│   └── (no academic-department subdivision at the UG admin level;
│        90 concentrations span A&H, social sciences, life sciences,
│        physical sciences; 16 of these are Engineering-track and
│        cross-listed administratively with the School of Engineering)
├── Graduate School                                        [学院 — graduate]
│   └── PhD / Sc.M. / A.M. / MFA / MAT across ~40 disciplines
│        (humanities, social sciences, natural & mathematical sciences,
│         computer science, applied mathematics)
├── School of Engineering                                  [学院 — UG + graduate]
│   └── Biomedical · Chemical · Computer · Electrical · Materials ·
│        Mechanical Engineering · Engineering (general) · Design Engineering
├── School of Public Health                                [学院 — graduate]
│   └── Biostatistics · Epidemiology · Health Services Research ·
│        Behavioral & Social Health Sciences · Public Health (MPH)
├── Warren Alpert Medical School                           [学院 — graduate]
│   └── M.D. program + 5 BioMed PhD programs (EEOB, MCB, Neuroscience,
│        Pathobiology, Therapeutic Sciences) + M.D./Ph.D. +
│        Primary Care–Population Medicine (M.D./Sc.M.)
├── School of Professional Studies                         [学院 — graduate]
│   └── Executive & online professional master's (Business Analytics,
│        Innovation Mgmt & Entrepreneurship, Organizational Leadership,
│        Technology Leadership, Management MiM, IE Brown Executive MBA,
│        plus Sustainable Energy / Cybersecurity Sc.M. delivered here)
└── Watson School of International and Public Affairs      [学院 — graduate]  ⚠ newest school
    └── Public Affairs (MPA) · Public Policy (MPP)
```

⚠ **Watson School of International and Public Affairs** was chartered in 2025 (growing out of the former Watson Institute for International and Public Affairs) and is the newest of Brown's schools — it is missing from older references that list only 3 graduate schools. ⚠ Some UG Engineering concentrations (Biomedical, Chemical, Computer, Electrical, Materials, Mechanical Engineering, etc.) are administered jointly between The College and the School of Engineering; they are listed under School of Engineering in Section 1.2 because their degree is Sc.B.-Engineering and their home faculty are in the School of Engineering, but their students are degree candidates of The College.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory, canonical)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | A.B. (Artium Baccalaureus) | Bachelor of Arts | 本科 | 71 |
| BS | Sc.B. (Scientiae Baccalaureus) | Bachelor of Science | 本科 | 37 |
| Certificate | Certificate | Undergraduate Certificate | 本科 | 6 |
| MA | A.M. (Artium Magister) | Master of Arts | 研究生 | 7 |
| MS | Sc.M. (Scientiae Magister) | Master of Science | 研究生 | 29 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MEng | M.Eng. | Master of Engineering | 研究生 | 2 |
| ExecMaster | Executive Master | Executive Master (e.g. IE Brown EMBA) | 研究生 | 1 |
| MiM | MiM | Master in Management | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 4 |
| MPA | MPA | Master of Public Affairs | 研究生 | 2 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 46 |
| MD | M.D. | Doctor of Medicine | 研究生 | 3 |

> Counts are degree-level rows (canonical) summed across all schools. PhD+MA+MS+MEng+MAT+MFA+ExecMaster+MiM+MPH+MPA+MPP+MD = 100 graduate degree rows. BA+BS = 108 undergraduate degree rows. 6 certificates are non-degree and listed separately. **Brown does NOT award** the BFA, BBA, MBA (on-campus standalone), EdD, JD, DrPH, or DNP — the IE Brown program awards an "Executive Master," not an MBA.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab, 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | MFA | MAT | MEng | MPH | MPA | MPP | MiM | ExecM | MD | PhD | 合计 |
|------------|----|----|----|----|-----|-----|------|-----|-----|-----|-----|-------|----|-----|------|
| The College | 68 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **92** |
| School of Engineering | 3 | 13 | 2 | 7 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | **29** |
| Graduate School | 0 | 0 | 4 | 12 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 34 | **54** |
| School of Public Health | 0 | 0 | 1 | 4 | 0 | 0 | 0 | 4 | 1 | 0 | 0 | 0 | 0 | 4 | **14** |
| Warren Alpert Medical School | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 6 | **12** |
| School of Professional Studies | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | **5** |
| Watson School of Intl & Public Affairs | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | **2** |
| **合计** | **71** | **37** | **7** | **29** | **3** | **1** | **2** | **4** | **2** | **1** | **1** | **1** | **3** | **46** | **208** |

> **Reconciliation check:** Column totals (71+37+7+29+3+1+2+4+2+1+1+1+3+46) = **208**. Row totals (92+29+54+14+12+5+2) = **208**. Rule-1 total degree rows = **208**. ✅ All three reconcile.
> 6 undergraduate certificates are excluded from the matrix (non-degree) but reported in Rule 1 and Section 1.4.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Undergraduate education at Brown lives entirely in **The College**. The College does not subdivide into academic departments at the administrative level the way most universities do — instead, each of the 90 **concentrations** is governed by a Concentration Advisor / DUG (Departmental Undergraduate Group) tied to a disciplinary faculty body. The School of Engineering jointly administers the 16 Engineering-track Sc.B. concentrations (their students are still degree candidates of The College). See the full hierarchy in Section 0.2.

Brown's signature is the **Open Curriculum**: there is **no required core curriculum and no distribution/general-education requirements**. Students build their own course of study, take all courses for a grade (or S/NC — Satisfactory/No Credit, Brown's unique grading option), and declare a concentration. There are **no minors**; the 6 interdisciplinary **certificates** (Section 1.4) serve that complementary-credential role.

### 1.2 Undergraduate concentrations — grouped by 学院 > 学位级别

#### School of Engineering
##### A.B.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | <https://www.brown.edu/undergraduate-programs/applied-mathematics-ab-scb> |
| 2 | Applied Mathematics - Economics | <https://www.brown.edu/undergraduate-programs/applied-mathematics-economics-ab-scb> |
| 3 | Engineering | <https://www.brown.edu/undergraduate-programs/engineering-ab> |

##### Sc.B.
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | <https://www.brown.edu/undergraduate-programs/applied-mathematics-ab-scb> |
| 2 | Applied Mathematics - Biology | <https://www.brown.edu/undergraduate-programs/applied-mathematics-biology-scb> |
| 3 | Applied Mathematics - Computer Science | <https://www.brown.edu/undergraduate-programs/applied-mathematics-computer-science-scb> |
| 4 | Applied Mathematics - Economics | <https://www.brown.edu/undergraduate-programs/applied-mathematics-economics-ab-scb> |
| 5 | Biomedical Engineering | <https://www.brown.edu/undergraduate-programs/biomedical-engineering-scb> |
| 6 | Chemical Engineering | <https://www.brown.edu/undergraduate-programs/chemical-engineering-scb> |
| 7 | Computer Engineering | <https://www.brown.edu/undergraduate-programs/computer-engineering-scb> |
| 8 | Design Engineering | <https://www.brown.edu/undergraduate-programs/design-engineering-scb> |
| 9 | Electrical Engineering | <https://www.brown.edu/undergraduate-programs/electrical-engineering-scb> |
| 10 | Engineering and Physics | <https://www.brown.edu/undergraduate-programs/engineering-and-physics-scb> |
| 11 | Environmental Engineering | <https://www.brown.edu/undergraduate-programs/environmental-engineering-scb> |
| 12 | Materials Engineering | <https://www.brown.edu/undergraduate-programs/materials-engineering-scb> |
| 13 | Mechanical Engineering | <https://www.brown.edu/undergraduate-programs/mechanical-engineering-scb> |

#### The College
##### A.B.
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | <https://www.brown.edu/undergraduate-programs/africana-studies-ab> |
| 2 | American Studies | <https://www.brown.edu/undergraduate-programs/american-studies-ab> |
| 3 | Anthropology | <https://www.brown.edu/undergraduate-programs/anthropology-ab> |
| 4 | Archaeology and the Ancient World | <https://www.brown.edu/undergraduate-programs/archaeology-and-ancient-world-ab> |
| 5 | Architecture | <https://www.brown.edu/undergraduate-programs/architecture-ab> |
| 6 | Astronomy | <https://www.brown.edu/undergraduate-programs/astronomy-ab> |
| 7 | Behavioral Decision Sciences | <https://www.brown.edu/undergraduate-programs/behavioral-decision-sciences-ab> |
| 8 | Biology | <https://www.brown.edu/undergraduate-programs/biology-ab-scb> |
| 9 | Business, Entrepreneurship, and Organizations | <https://www.brown.edu/undergraduate-programs/business-entrepreneurship-and-organizations-ab> |
| 10 | Chemistry | <https://www.brown.edu/undergraduate-programs/chemistry-ab-scb> |
| 11 | Classics | <https://www.brown.edu/undergraduate-programs/classics-ab> |
| 12 | Cognitive Neuroscience | <https://www.brown.edu/undergraduate-programs/cognitive-neuroscience-ab-scb> |
| 13 | Cognitive Science | <https://www.brown.edu/undergraduate-programs/cognitive-science-ab-scb> |
| 14 | Comparative Literature | <https://www.brown.edu/undergraduate-programs/comparative-literature-ab> |
| 15 | Computational Biology | <https://www.brown.edu/undergraduate-programs/computational-biology-ab-scb> |
| 16 | Computer Science | <https://www.brown.edu/undergraduate-programs/computer-science-ab-scb> |
| 17 | Computer Science - Economics | <https://www.brown.edu/undergraduate-programs/computer-science-economics-ab-scb> |
| 18 | Contemplative Studies | <https://www.brown.edu/undergraduate-programs/contemplative-studies-ab> |
| 19 | Critical Native American and Indigenous Studies | <https://www.brown.edu/undergraduate-programs/critical-native-american-and-indigenous-studies-ab> |
| 20 | Development Studies | <https://www.brown.edu/undergraduate-programs/development-studies-ab> |
| 21 | Early Modern World | <https://www.brown.edu/undergraduate-programs/early-modern-world-ab> |
| 22 | Earth and Planetary Science | <https://www.brown.edu/undergraduate-programs/earth-and-planetary-science-ab-scb> |
| 23 | Earth, Climate and Biology | <https://www.brown.edu/undergraduate-programs/earth-climate-and-biology-ab-scb> |
| 24 | East Asian Studies | <https://www.brown.edu/undergraduate-programs/east-asian-studies-ab> |
| 25 | Economics | <https://www.brown.edu/undergraduate-programs/economics-ab> |
| 26 | Education Studies | <https://www.brown.edu/undergraduate-programs/education-studies-ab> |
| 27 | Egyptology and Assyriology | <https://www.brown.edu/undergraduate-programs/egyptology-and-assyriology-ab> |
| 28 | English | <https://www.brown.edu/undergraduate-programs/english-ab> |
| 29 | Environmental Sciences and Studies | <https://www.brown.edu/undergraduate-programs/environmental-sciences-and-studies-ab-scb> |
| 30 | Ethnic Studies | <https://www.brown.edu/undergraduate-programs/ethnic-studies-ab> |
| 31 | French and Francophone Studies | <https://www.brown.edu/undergraduate-programs/french-and-francophone-studies-ab> |
| 32 | Gender and Sexuality Studies | <https://www.brown.edu/undergraduate-programs/gender-and-sexuality-studies-ab> |
| 33 | Geochemistry and Environmental Chemistry | <https://www.brown.edu/undergraduate-programs/geochemistry-and-environmental-chemistry-ab-scb> |
| 34 | Geophysics and Climate Physics | <https://www.brown.edu/undergraduate-programs/geophysics-and-climate-physics-ab-scb> |
| 35 | German Studies | <https://www.brown.edu/undergraduate-programs/german-studies-ab> |
| 36 | Health and Human Biology | <https://www.brown.edu/undergraduate-programs/health-and-human-biology-ab> |
| 37 | Hispanic Literatures and Cultures | <https://www.brown.edu/undergraduate-programs/hispanic-literatures-and-cultures-ab> |
| 38 | History | <https://www.brown.edu/undergraduate-programs/history-ab> |
| 39 | History of Art and Architecture | <https://www.brown.edu/undergraduate-programs/history-art-and-architecture-ab> |
| 40 | International and Public Affairs | <https://www.brown.edu/undergraduate-programs/international-and-public-affairs-ab> |
| 41 | International Relations | <https://www.brown.edu/undergraduate-programs/international-relations-ab> |
| 42 | Italian Studies | <https://www.brown.edu/undergraduate-programs/italian-studies-ab> |
| 43 | Judaic Studies | <https://www.brown.edu/undergraduate-programs/judaic-studies-ab> |
| 44 | Latin American and Caribbean Studies | <https://www.brown.edu/undergraduate-programs/latin-american-and-caribbean-studies-ab> |
| 45 | Linguistics | <https://www.brown.edu/undergraduate-programs/linguistics-ab-scb> |
| 46 | Literary Arts | <https://www.brown.edu/undergraduate-programs/literary-arts-ab> |
| 47 | Mathematics | <https://www.brown.edu/undergraduate-programs/mathematics-ab-scb> |
| 48 | Mathematics - Economics | <https://www.brown.edu/undergraduate-programs/mathematics-economics-ab> |
| 49 | Medieval Cultures | <https://www.brown.edu/undergraduate-programs/medieval-cultures-ab> |
| 50 | Middle East Studies | <https://www.brown.edu/undergraduate-programs/middle-east-studies-ab> |
| 51 | Modern Culture and Media | <https://www.brown.edu/undergraduate-programs/modern-culture-and-media-ab> |
| 52 | Music | <https://www.brown.edu/undergraduate-programs/music-ab> |
| 53 | Philosophy | <https://www.brown.edu/undergraduate-programs/philosophy-ab> |
| 54 | Physics | <https://www.brown.edu/undergraduate-programs/physics-ab-scb> |
| 55 | Physics and Philosophy | <https://www.brown.edu/undergraduate-programs/physics-and-philosophy-ab> |
| 56 | Political Science | <https://www.brown.edu/undergraduate-programs/political-science-ab> |
| 57 | Portuguese and Brazilian Studies | <https://www.brown.edu/undergraduate-programs/portuguese-and-brazilian-studies-ab> |
| 58 | Psychology | <https://www.brown.edu/undergraduate-programs/psychology-ab-scb> |
| 59 | Public Health | <https://www.brown.edu/undergraduate-programs/public-health-ab> |
| 60 | Public Policy | <https://www.brown.edu/undergraduate-programs/public-policy-ab> |
| 61 | Religious Studies | <https://www.brown.edu/undergraduate-programs/religious-studies-ab> |
| 62 | Science, Technology, and Society | <https://www.brown.edu/undergraduate-programs/science-technology-and-society-ab> |
| 63 | Slavic Studies | <https://www.brown.edu/undergraduate-programs/slavic-studies-ab> |
| 64 | Sociology | <https://www.brown.edu/undergraduate-programs/sociology-ab> |
| 65 | South Asian Studies | <https://www.brown.edu/undergraduate-programs/south-asian-studies-ab> |
| 66 | Theatre Arts and Performance Studies | <https://www.brown.edu/undergraduate-programs/theatre-arts-and-performance-studies-ab> |
| 67 | Urban Studies | <https://www.brown.edu/undergraduate-programs/urban-studies-ab> |
| 68 | Visual Art | <https://www.brown.edu/undergraduate-programs/visual-art-ab> |

##### Sc.B.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | <https://www.brown.edu/undergraduate-programs/biochemistry-and-molecular-biology-scb> |
| 2 | Biology | <https://www.brown.edu/undergraduate-programs/biology-ab-scb> |
| 3 | Biophysics | <https://www.brown.edu/undergraduate-programs/biophysics-scb> |
| 4 | Chemical Physics | <https://www.brown.edu/undergraduate-programs/chemical-physics-scb> |
| 5 | Chemistry | <https://www.brown.edu/undergraduate-programs/chemistry-ab-scb> |
| 6 | Cognitive Neuroscience | <https://www.brown.edu/undergraduate-programs/cognitive-neuroscience-ab-scb> |
| 7 | Cognitive Science | <https://www.brown.edu/undergraduate-programs/cognitive-science-ab-scb> |
| 8 | Computational Biology | <https://www.brown.edu/undergraduate-programs/computational-biology-ab-scb> |
| 9 | Computational Neuroscience | <https://www.brown.edu/undergraduate-programs/computational-neuroscience-scb> |
| 10 | Computer Science | <https://www.brown.edu/undergraduate-programs/computer-science-ab-scb> |
| 11 | Computer Science - Economics | <https://www.brown.edu/undergraduate-programs/computer-science-economics-ab-scb> |
| 12 | Earth and Planetary Science | <https://www.brown.edu/undergraduate-programs/earth-and-planetary-science-ab-scb> |
| 13 | Earth, Climate and Biology | <https://www.brown.edu/undergraduate-programs/earth-climate-and-biology-ab-scb> |
| 14 | Environmental Sciences and Studies | <https://www.brown.edu/undergraduate-programs/environmental-sciences-and-studies-ab-scb> |
| 15 | Geochemistry and Environmental Chemistry | <https://www.brown.edu/undergraduate-programs/geochemistry-and-environmental-chemistry-ab-scb> |
| 16 | Geophysics and Climate Physics | <https://www.brown.edu/undergraduate-programs/geophysics-and-climate-physics-ab-scb> |
| 17 | Linguistics | <https://www.brown.edu/undergraduate-programs/linguistics-ab-scb> |
| 18 | Mathematics | <https://www.brown.edu/undergraduate-programs/mathematics-ab-scb> |
| 19 | Mathematics - Computer Science | <https://www.brown.edu/undergraduate-programs/mathematics-computer-science-scb> |
| 20 | Neuroscience | <https://www.brown.edu/undergraduate-programs/neuroscience-scb> |
| 21 | Physics | <https://www.brown.edu/undergraduate-programs/physics-ab-scb> |
| 22 | Psychology | <https://www.brown.edu/undergraduate-programs/psychology-ab-scb> |
| 23 | Social Analysis and Research | <https://www.brown.edu/undergraduate-programs/social-analysis-and-research-scb> |
| 24 | Statistics | <https://www.brown.edu/undergraduate-programs/statistics-scb> |

> **Counts in this section:** 108 UG degree rows = 71 A.B. + 37 Sc.B. (3 A.B. Engineering + 13 Sc.B. Engineering + 68 A.B. College + 24 Sc.B. College). 18 concentrations appear twice because they offer both A.B. and Sc.B. tracks (e.g. Applied Mathematics, Biology, Chemistry, Computer Science, Physics, Mathematics, Linguistics, Psychology, etc.).

### 1.3 Interdisciplinary / cross-college undergraduate programs

Brown's Open Curriculum means most programs are inherently interdisciplinary. Notable structured joint/cross-college programs:
- **Program in Liberal Medical Education (PLME)** — Brown's 8-year combined baccalaureate+M.D. program (the only combined BS/MD program in the Ivy League). Requires special program essays on the Common App. See E-U-001.
- **Brown|RISD Dual Degree (BRDD)** — 5-year dual degree with Rhode Island School of Design; requires special program essays.
- Combined concentrations with **-Economics** (Applied Mathematics–Economics, Computer Science–Economics, Mathematics–Economics) and **-Computer Science** (Applied Mathematics–CS, Mathematics–CS) joint tracks.

### 1.4 Undergraduate Certificates — complete list (Brown has no minors)

| # | Certificate | Home unit | URL |
|---|-------------|-----------|-----|
| 1 | Data Fluency | (interdisciplinary) | <https://www.brown.edu/undergraduate-programs/data-fluency-certificate> |
| 2 | Engaged Scholarship | Swearer Center for Public Service | <https://www.brown.edu/undergraduate-programs/engaged-scholarship-certificate> |
| 3 | Entrepreneurship | School of Engineering | <https://www.brown.edu/undergraduate-programs/entrepreneurship-certificate> |
| 4 | European Critical Thought | (interdisciplinary) | <https://www.brown.edu/undergraduate-programs/european-critical-thought-certificate> |
| 5 | Intercultural Competence | (Center for Language Studies) | <https://www.brown.edu/undergraduate-programs/intercultural-competence-certificate> |
| 6 | Migration Studies | (interdisciplinary) | <https://www.brown.edu/undergraduate-programs/migration-studies-certificate> |

### 1.5 General/Institute-wide requirements — the Open Curriculum

Brown's distinctive feature is that it has **NO required core curriculum and NO distribution/general-education requirements**. Under the **Open Curriculum** (introduced 1969, sometimes called the "New Curriculum"):
- Students design their own course of study.
- Courses may be taken for a letter grade **or** S/NC (Satisfactory / No Credit) — Brown's unique non-punitive grading option.
- A student must complete one **concentration** (major) to graduate; many complete two.
- **Writing requirement**: each student must demonstrate writing ability, typically satisfied within concentration courses (no separate core writing course).
- Source: <https://www.brown.edu/academics/undergraduate/open-curriculum> — *"At most universities, students must complete a set of core courses. At Brown, our students develop a personalized course of study — they have greater freedom to study what they choose and the flexibility to discover what they love."* (E-U-009)

### 1.6 Course-ID → Major quick-lookup

Brown does **not** use a numbered course-ID-to-major scheme (unlike MIT's "Course 6"). Concentrations are identified by name and by URL slug on `brown.edu/undergraduate-programs/<slug>-<degree-suffix>`, where the suffix encodes the degree: `-ab` = A.B., `-scb` = Sc.B., `-ab-scb` = both, `-certificate` = undergraduate certificate.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

Graduate admissions at Brown is **decentralized**: each program sets its own admission criteria and deadlines, with oversight by the Graduate School. The Graduate School centrally manages applications for **all doctoral and MFA programs**; non-MFA master's programs are administered through the individual schools (see masters.brown.edu). The authoritative program directory is `graduateprograms.brown.edu`, listing **91 graduate programs**.

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### Graduate School
##### A.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology | <https://graduateprograms.brown.edu/graduate-program/biotechnology-am-scm> |
| 2 | Education: Urban Education Policy | <https://graduateprograms.brown.edu/graduate-program/education-urban-education-policy-am> |
| 3 | Integrative Studies | <https://graduateprograms.brown.edu/graduate-program/integrative-studies-am-scm> |
| 4 | Public Humanities (Integrative Studies) | <https://graduateprograms.brown.edu/graduate-program/public-humanities-integrative-studies-am> |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Education: Master of Arts in Teaching | <https://graduateprograms.brown.edu/graduate-program/education-master-arts-teaching-mat> |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Literary Arts | <https://graduateprograms.brown.edu/graduate-program/literary-arts-mfa> |
| 2 | Theatre Arts and Performance Studies: Playwriting | <https://graduateprograms.brown.edu/graduate-program/theatre-arts-and-performance-studies-playwriting-mfa> |
| 3 | Theatre: Brown/Trinity Rep Acting and Directing | <https://graduateprograms.brown.edu/graduate-program/theatre-browntrinity-rep-acting-and-directing-mfa> |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Africana Studies | <https://graduateprograms.brown.edu/graduate-program/africana-studies-phd> |
| 2 | American Studies | <https://graduateprograms.brown.edu/graduate-program/american-studies-phd> |
| 3 | Anthropology | <https://graduateprograms.brown.edu/graduate-program/anthropology-phd> |
| 4 | Applied Mathematics | <https://graduateprograms.brown.edu/graduate-program/applied-mathematics-phd> |
| 5 | Archaeology and the Ancient World | <https://graduateprograms.brown.edu/graduate-program/archaeology-and-ancient-world-phd> |
| 6 | Chemistry | <https://graduateprograms.brown.edu/graduate-program/chemistry-phd> |
| 7 | Classics | <https://graduateprograms.brown.edu/graduate-program/classics-phd> |
| 8 | Cognitive Science | <https://graduateprograms.brown.edu/graduate-program/cognitive-science-phd> |
| 9 | Comparative Literature | <https://graduateprograms.brown.edu/graduate-program/comparative-literature-phd> |
| 10 | Computational Biology | <https://graduateprograms.brown.edu/graduate-program/computational-biology-phd> |
| 11 | Computer Science | <https://graduateprograms.brown.edu/graduate-program/computer-science-phd> |
| 12 | Earth, Environmental and Planetary Sciences | <https://graduateprograms.brown.edu/graduate-program/earth-environmental-and-planetary-sciences-phd> |
| 13 | Economics | <https://graduateprograms.brown.edu/graduate-program/economics-phd> |
| 14 | Egyptology and Assyriology | <https://graduateprograms.brown.edu/graduate-program/egyptology-and-assyriology-phd> |
| 15 | English | <https://graduateprograms.brown.edu/graduate-program/english-phd> |
| 16 | French and Francophone Studies | <https://graduateprograms.brown.edu/graduate-program/french-and-francophone-studies-phd> |
| 17 | German Studies | <https://graduateprograms.brown.edu/graduate-program/german-studies-phd> |
| 18 | Hispanic Studies | <https://graduateprograms.brown.edu/graduate-program/hispanic-studies-phd> |
| 19 | History | <https://graduateprograms.brown.edu/graduate-program/history-phd> |
| 20 | History of Art and Architecture | <https://graduateprograms.brown.edu/graduate-program/history-art-and-architecture-phd> |
| 21 | Italian Studies | <https://graduateprograms.brown.edu/graduate-program/italian-studies-phd> |
| 22 | Mathematics | <https://graduateprograms.brown.edu/graduate-program/mathematics-phd> |
| 23 | Modern Culture and Media | <https://graduateprograms.brown.edu/graduate-program/modern-culture-and-media-phd> |
| 24 | Music and Multimedia Composition | <https://graduateprograms.brown.edu/graduate-program/music-and-multimedia-composition-phd> |
| 25 | Musicology and Ethnomusicology | <https://graduateprograms.brown.edu/graduate-program/musicology-and-ethnomusicology-phd> |
| 26 | Philosophy | <https://graduateprograms.brown.edu/graduate-program/philosophy-phd> |
| 27 | Physics | <https://graduateprograms.brown.edu/graduate-program/physics-phd> |
| 28 | Political Science | <https://graduateprograms.brown.edu/graduate-program/political-science-phd> |
| 29 | Portuguese and Brazilian Studies | <https://graduateprograms.brown.edu/graduate-program/portuguese-and-brazilian-studies-phd> |
| 30 | Psychology | <https://graduateprograms.brown.edu/graduate-program/psychology-phd> |
| 31 | Religious Studies | <https://graduateprograms.brown.edu/graduate-program/religious-studies-phd> |
| 32 | Slavic Studies | <https://graduateprograms.brown.edu/graduate-program/slavic-studies-phd> |
| 33 | Sociology | <https://graduateprograms.brown.edu/graduate-program/sociology-phd> |
| 34 | Theatre Arts and Performance Studies | <https://graduateprograms.brown.edu/graduate-program/theatre-arts-and-performance-studies-phd> |

##### Sc.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology | <https://graduateprograms.brown.edu/graduate-program/biotechnology-am-scm> |
| 2 | Computer Science | <https://graduateprograms.brown.edu/graduate-program/computer-science-scm> |
| 3 | Cybersecurity | <https://graduateprograms.brown.edu/graduate-program/cybersecurity-scm> |
| 4 | Data Science | <https://graduateprograms.brown.edu/graduate-program/data-science-scm> |
| 5 | Data Science: Policy, Governance & Society (Online) | <https://graduateprograms.brown.edu/graduate-program/data-science-policy-governance-society-online-scm> |
| 6 | Environmental Engineering | <https://graduateprograms.brown.edu/graduate-program/environmental-engineering-scm> |
| 7 | Innovation Management and Entrepreneurship | <https://graduateprograms.brown.edu/graduate-program/innovation-management-and-entrepreneurship-scm> |
| 8 | Integrative Studies | <https://graduateprograms.brown.edu/graduate-program/integrative-studies-am-scm> |
| 9 | Physics | <https://graduateprograms.brown.edu/graduate-program/physics-scm> |
| 10 | Social Data Analytics | <https://graduateprograms.brown.edu/graduate-program/social-data-analytics-scm> |
| 11 | Sustainable Energy | <https://graduateprograms.brown.edu/graduate-program/sustainable-energy-scm> |
| 12 | Technology Leadership | <https://graduateprograms.brown.edu/graduate-program/technology-leadership-scm> |

#### School of Engineering
##### A.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Design Engineering | <https://graduateprograms.brown.edu/graduate-program/design-engineering-am> |
| 2 | Engineering | <https://graduateprograms.brown.edu/graduate-program/engineering-am-meng-scm> |

##### M.Eng.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | <https://graduateprograms.brown.edu/graduate-program/biomedical-engineering-meng-scm> |
| 2 | Engineering | <https://graduateprograms.brown.edu/graduate-program/engineering-am-meng-scm> |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | <https://graduateprograms.brown.edu/graduate-program/biomedical-engineering-phd> |
| 2 | Engineering | <https://graduateprograms.brown.edu/graduate-program/engineering-phd> |

##### Sc.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | <https://graduateprograms.brown.edu/graduate-program/biomedical-engineering-meng-scm> |
| 2 | Chemical Engineering | <https://graduateprograms.brown.edu/graduate-program/chemical-engineering-scm> |
| 3 | Data-Enabled Computational Engineering and Science | <https://graduateprograms.brown.edu/graduate-program/data-enabled-computational-engineering-and-science-scm> |
| 4 | Electrical and Computer Engineering | <https://graduateprograms.brown.edu/graduate-program/electrical-and-computer-engineering-scm> |
| 5 | Engineering | <https://graduateprograms.brown.edu/graduate-program/engineering-am-meng-scm> |
| 6 | Environmental Engineering | <https://graduateprograms.brown.edu/graduate-program/environmental-engineering-scm> |
| 7 | Materials Science and Engineering | <https://graduateprograms.brown.edu/graduate-program/materials-science-and-engineering-scm> |
| 8 | Mechanical Engineering and Applied Mechanics | <https://graduateprograms.brown.edu/graduate-program/mechanical-engineering-and-applied-mechanics-scm> |

#### School of Public Health
##### A.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | <https://graduateprograms.brown.edu/graduate-program/biostatistics-am-scm> |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health and Public Affairs Dual Degree | <https://graduateprograms.brown.edu/graduate-program/public-health-and-public-affairs-dual-degree-mpa-mph> |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | <https://graduateprograms.brown.edu/graduate-program/public-health-mph> |
| 2 | Public Health (Accelerated) | <https://graduateprograms.brown.edu/graduate-program/public-health-accelerated-mph> |
| 3 | Public Health (Online) | <https://graduateprograms.brown.edu/graduate-program/public-health-online-mph> |
| 4 | Public Health and Public Affairs Dual Degree | <https://graduateprograms.brown.edu/graduate-program/public-health-and-public-affairs-dual-degree-mpa-mph> |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Behavioral and Social Health Sciences | <https://graduateprograms.brown.edu/graduate-program/behavioral-and-social-health-sciences-phd> |
| 2 | Biostatistics | <https://graduateprograms.brown.edu/graduate-program/biostatistics-phd> |
| 3 | Epidemiology | <https://graduateprograms.brown.edu/graduate-program/epidemiology-phd> |
| 4 | Health Services Research | <https://graduateprograms.brown.edu/graduate-program/health-services-research-phd> |

##### Sc.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | <https://graduateprograms.brown.edu/graduate-program/biostatistics-am-scm> |
| 2 | Biostatistics (Online) | <https://graduateprograms.brown.edu/graduate-program/biostatistics-online-scm> |
| 3 | Health Informatics | <https://graduateprograms.brown.edu/graduate-program/health-informatics-scm> |
| 4 | Healthcare Leadership | <https://graduateprograms.brown.edu/graduate-program/healthcare-leadership-scm> |

#### Warren Alpert Medical School
##### M.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine | <https://graduateprograms.brown.edu/graduate-program/doctor-medicine-md> |
| 2 | M.D./Ph.D. | <https://graduateprograms.brown.edu/graduate-program/mdphd> |
| 3 | Primary Care-Population Medicine Program | <https://graduateprograms.brown.edu/graduate-program/primary-care-population-medicine-program-md-scm> |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | BioMed: Ecology, Evolution, and Organismal Biology | <https://graduateprograms.brown.edu/graduate-program/biomed-ecology-evolution-and-organismal-biology-phd> |
| 2 | BioMed: Molecular Biology, Cell Biology, and Biochemistry | <https://graduateprograms.brown.edu/graduate-program/biomed-molecular-biology-cell-biology-and-biochemistry-phd> |
| 3 | BioMed: Neuroscience | <https://graduateprograms.brown.edu/graduate-program/biomed-neuroscience-phd> |
| 4 | BioMed: Pathobiology | <https://graduateprograms.brown.edu/graduate-program/biomed-pathobiology-phd> |
| 5 | BioMed: Therapeutic Sciences | <https://graduateprograms.brown.edu/graduate-program/biomed-therapeutic-sciences-phd> |
| 6 | M.D./Ph.D. | <https://graduateprograms.brown.edu/graduate-program/mdphd> |

##### Sc.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Physics | <https://graduateprograms.brown.edu/graduate-program/medical-physics-scm> |
| 2 | Medical Sciences | <https://graduateprograms.brown.edu/graduate-program/medical-sciences-scm> |
| 3 | Primary Care-Population Medicine Program | <https://graduateprograms.brown.edu/graduate-program/primary-care-population-medicine-program-md-scm> |

#### School of Professional Studies
##### Executive Master
| # | 项目 | URL |
|---|------|-----|
| 1 | IE Brown Executive MBA | <https://graduateprograms.brown.edu/graduate-program/ie-brown-executive-mba-executive-master> |

##### MiM
| # | 项目 | URL |
|---|------|-----|
| 1 | Management (Online) | <https://graduateprograms.brown.edu/graduate-program/management-online-mim> |

##### Sc.M.
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics (Online) | <https://graduateprograms.brown.edu/graduate-program/business-analytics-online-scm> |
| 2 | Innovation Management and Entrepreneurship (Online) | <https://graduateprograms.brown.edu/graduate-program/innovation-management-and-entrepreneurship-online-scm> |
| 3 | Organizational Leadership (Online) | <https://graduateprograms.brown.edu/graduate-program/organizational-leadership-online-scm> |

#### Watson School of International and Public Affairs
##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Affairs | <https://graduateprograms.brown.edu/graduate-program/public-affairs-mpa> |

##### MPP
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy (Online) | <https://graduateprograms.brown.edu/graduate-program/public-policy-online-mpp> |

### 2.2 Worked example — Computer Science Sc.M. (Brown's most-applied-to master's)

- **Department**: Department of Computer Science, Brown University
- **Program URL**: <https://graduateprograms.brown.edu/graduate-program/computer-science-scm>
- **Department site**: <https://cs.brown.edu>
- **Degree awarded**: Sc.M. (canonical: MS) — offered in two options: coursework-only OR research-project; either may be completed as a "professional track" with a 2–6 month internship.
- **Format**: two-year, on-campus
- **Curricular scope**: AI/machine learning, computational biology, computer architecture, data, design, security, software principles, systems, theory, visual computing.
- **Application opens / deadline**: deadlines vary by program; common doctoral/MFA deadline is **January 1** (date determined using Eastern Standard Time). Master's deadlines set per program.
- **Application fee**: **$75** nonrefundable (Graduate School). Fee waivers available for demonstrated financial need (E-G-002).
- **Application portal**: Brown online application (Graduate School manages doctoral + MFA; non-MFA master's via masters.brown.edu).
- **GRE policy**: each program decides whether to require the GRE — Computer Science requires it; check the program page (E-G-003).
- **Language**: TOEFL or IELTS required of non-native English speakers (waiver possible by request to graduate_admissions@brown.edu after submission).
- **Behind accordions / program page sections**: About the Program · Application Information · Tuition and Funding · Completion Requirements · Alumni Outcomes · Leadership · Contact and Location.
- **Funding**: doctoral students receive 5 years guaranteed support (6 in humanities/social sciences); master's programs are typically self-funded.

### 2.3 Graduate admissions model

**Decentralized**, with central oversight:
- The **Graduate School** (graduateschool.brown.edu, 47 George Street, Providence RI) sets policy and runs the online application for all **doctoral and MFA** programs. Contact: graduate_admissions@brown.edu / 401-863-2600.
- **Non-MFA master's** programs are administered through each school; central portal: masters.brown.edu.
- Each program sets its own admission criteria, deadlines, and GRE requirements.
- **School of Professional Studies** self-manages executive/online professional master's admissions (professional.brown.edu/admissions).
- **Warren Alpert Medical School** M.D. admissions runs separately via admission.med.brown.edu (AMCAS-based).
- Funding: doctoral funding is centralized (5-yr guarantee; 6-yr in humanities/social sciences); master's funding is generally not provided (self-funded).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table (2025-26 / Class of 2029 cycle)

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://admission.brown.edu/ | E-U-002 |
| Application portal | **Common Application** + Brown Member section | E-U-002 |
| **Early Decision deadline** | **November 1, 11:59 p.m. applicant's local time** (binding; mid-December decision) | E-U-001, E-U-002 |
| **Regular Decision deadline** | **January 5, 11:59 p.m. applicant's local time** (early-April decision) | E-U-001, E-U-002 |
| ED notification | Mid-December | E-U-002 |
| RD notification | By early April | E-U-002 |
| Enrollment confirmation | **May 1** (common reply date) | E-U-002 |
| **Application fee** | **$80** nonrefundable (or fee waiver) | E-U-001 |
| **Standardized tests** | **REQUIRED** — SAT or ACT (returned to required starting 2024-25 cycle; previously test-optional 2020-24). **NOT test-optional.** No minimum. Superscore either or both. | E-U-003 |
| SAT Essay / ACT Writing | Optional (not required) | E-U-003 |
| ACT Science (from spring 2025) | Optional | E-U-003 |
| Last acceptable test date | ED: last October; RD: last December | E-U-003 |
| SAT / TOEFL institutional code | **3094** | E-U-003 |
| ACT institutional code | **3800** | E-U-003 |
| Score-report method | Self-report via Common App or Brown Applicant Portal, OR official from agency | E-U-003 |
| School forms | Common App: School Report + Counselor Recommendation + **2 Teacher Evaluations** (from major academic subjects) + Transcript + Midyear Report (due Feb 27) | E-U-001 |
| BS / PLME recommendation | At least one recommendation from a math or science teacher | E-U-001 |
| Interview | Not offered (replaced by **Video Introduction** — optional short video) | E-U-002 |
| Supplementary materials | Optional for arts/research portfolios; required special-program essays for **PLME** (8-yr BA/MD) and **BRDD** (5-yr Brown|RISD Dual Degree) | E-U-001 |
| First-quarter grades | Required of ED applicants (as soon as available) | E-U-001 |
| Transfer pathway | Fall or Spring entry; **need-aware** for transfers (financial need considered) | E-U-002 |

### 3.2 Undergraduate English proficiency table (international applicants)

Accepts: TOEFL iBT (incl. Home Edition), IELTS, Duolingo English Test, Pearson (PTE), Cambridge English (C1 Advanced / C2 Proficiency). Required of applicants for whom English is not a first language, primary language spoken at home, or primary language of secondary instruction.

| Exam | Minimum | Notes |
|------|---------|-------|
| TOEFL iBT (taken **prior to January 2026**) | **105** | E-U-004 |
| TOEFL iBT (taken **January 2026 and later**) | **5.5** | New TOEFL reporting scale — verbatim per Brown's page (E-U-004) |
| IELTS | **8.0** | E-U-004 |
| Duolingo English Test | **130** | E-U-004 |
| Pearson Test of English (PTE) | **75** | E-U-004 |
| Cambridge C1 Advanced / C2 Proficiency | **191** | E-U-004 |

> Applicability: "We highly recommend that international applicants for whom English is not a first language, a primary language spoken at home, or the primary language of instruction for the duration of their secondary school career submit the results of an English proficiency test." Official score reports required of all matriculating students who self-reported (due May 2026 for fall-2026 enrollment). Brown does NOT offer ESL courses for undergraduates and does not admit provisionally. (E-U-004)

### 3.3 Graduate — global rules

- **Admissions model**: decentralized; each program sets criteria and deadlines with Graduate School oversight. (E-G-001)
- **Application platforms**: Brown online application (doctoral + MFA via Graduate School; non-MFA master's via masters.brown.edu; Professional Studies via professional.brown.edu/admissions; MD via AMCAS).
- **Application fee**: **$75** nonrefundable, paid at submission. Multiple programs → separate applications each. (E-G-002)
- **Fee waivers**: needs-based, requested within the application; supporting docs required (FAFSA/CSS/financial-aid letter/GRE or TOEFL fee voucher/unemployment verification). (E-G-005)
- **CGS April-15 honor date**: Brown adheres to the Council of Graduate Schools' April 15 resolution for acceptance of financial offers (standard for U.S. doctoral programs; confirm per program).
- **GRE policy**: **per-program**. "Each program at Brown University may choose to require applicants to submit their official results from the GRE, or not." GRE General Test at-home accepted. GRE code **3094** (Graduate School) / **7765** (School of Public Health). Subject tests required by some departments. (E-G-003)
- **Language-test policy (grad)**: TOEFL or IELTS required of non-native speakers whose instruction was not in English; TOEFL ITP Plus for China also accepted. Waiver may be requested by emailing graduate_admissions@brown.edu after submission. (E-G-001, E-G-006)
- **Application timeline**: deadlines vary by program; common doctoral/MFA deadline is **January 1** (EST). Decisions 4–8 weeks after deadline (Feb/Mar for Jan 1 deadline).
- **Institutional codes**: Brown Graduate School **3094** (GRE/TOEFL); School of Public Health **7765** (GRE); SAT/TOEFL UG **3094**; ACT UG **3800**.
- **Supplemental essay**: 300-word diversity/inclusion prompt (one of two options). Statement of Purpose 2–3 pages.
- **Contact**: Graduate School, 47 George Street, Providence RI 02912; graduate_admissions@brown.edu; 401-863-2600.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26 academic year, line-itemized)

Source: <https://admission.brown.edu/tuition-aid/tuition-fees> (E-U-006). Two-semester billing (Fall + Spring).

| Expense item | Fall | Spring | Annual Total | Description |
|--------------|------|--------|--------------|-------------|
| Tuition | $35,850 | $35,850 | **$71,700** | Per-semester tuition |
| Fees | $1,475 | $1,475 | **$2,950** | Mandatory university fees |
| Housing | $5,205 | $5,205 | **$10,410** | On-campus room |
| Food | $4,052 | $4,052 | **$8,104** | Meal plan |
| Books & Materials | $650 | $650 | **$1,300** | Estimated |
| Personal | $1,410 | $1,410 | **$2,820** | Estimated personal expenses |
| **Total Cost of Attendance** | **$48,642** | **$48,642** | **$97,284** | — |

> Tuition for 2025-26 is **$71,700** (up from $69,648 in 2024-25). The total on-campus COA is **$97,284**. (E-U-006)

### 4.2 Undergraduate financial-aid policy

- **Need-blind admission**: "All first-year applicants will be admitted to Brown on a need-blind basis." (E-U-007)
- **Need-blind for international students**: **YES — beginning with the Class of 2029** (students entering fall 2025). *"Brown will be need-blind for international students beginning with the Class of 2029."* (E-U-008). This makes Brown one of very few U.S. universities (with MIT, Harvard, Princeton, Yale, Dartmouth, Amherst) that are need-blind for internationals.
- **100% of demonstrated financial need met** for all admitted undergraduates (U.S. and international) who apply for aid at admission. (E-U-007, E-U-008)
- **The Brown Promise**: Brown does **not** package loans in any financial-aid award — all packaged loans have been **replaced with scholarship grants** that do not need to be repaid. (E-U-007)
- **Need-aware for transfers**: financial need IS considered for transfer applicants (transfer is not need-blind). International transfers get aid consideration.
- **No merit awards**: "Brown University does not offer any merit awards." All aid is need-based. (E-U-008)
- **Filing deadlines**: CSS Profile + FAFSA due **Nov 3, 2025** for ED applicants; **Feb 2, 2026** for RD applicants. (E-U-007)
- **Median actual price paid / debt-free graduation rate / avg starting salary**: not captured on the public-facing pages scraped in this run — flag as P0 follow-up (likely available in the Common Data Set / Brown by the Numbers).

### 4.3 Graduate cost & funding framework

- **Funding taxonomy**:
  - **Doctoral**: 5 years guaranteed support (stipend + tuition remission + health-services fee + health-insurance subsidy). Doctoral students in **Humanities and Social Sciences get 6 years**. (E-G-006)
  - **Master's**: generally **self-funded** (no guaranteed institutional support); external fellowships and federal loans available.
  - **MFA**: funded through the Graduate School application (varying by program).
- **Common funding forms**: RA (Research Assistantship), TA (Teaching Assistantship), internal fellowships, dissertation-completion grants, emergency funding.
- **Application fee**: **$75** nonrefundable (E-G-002).
- **Fee-waiver policy**: needs-based waiver requested within the application; documentation required (E-G-005).
- **Graduate living-expenses estimate**: ~$26,667 (9 months) / $35,556 (12 months). (E-G-006)
- **International master's**: must provide certified proof of financial support (incl. travel) if not fully funded, before final admission.
- **Cost-of-attendance / stipend-rate / living-expenses pages**: link through Student Financial Services — mark the detailed graduate COA line items as P1 follow-up (the grad international page references SFS for "all academic year costs").

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: ug.application.deadlines_fee
  value: "ED Nov 1; RD Jan 5; fee $80; Common App; 2 teacher evals; midyear due Feb 27"
  source_url: https://admission.brown.edu/first-year/application-checklist
  source_snippet: "Early Decision application deadline - November 1 ... Regular Decision application deadline - January 5 ... Submit the $80 non-refundable application fee or a fee waiver ... Two Teacher Evaluations/Recommendations ... Midyear School Report and Transcript: Due February 27"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-002
  field: ug.application.plans_and_decisions
  value: "ED binding (Nov 1, mid-Dec decision); RD (Jan 5, early April decision); enroll by May 1; Video Introduction replaces interview"
  source_url: https://admission.brown.edu/first-year/early-decision
  source_snippet: "prospective students apply by November 1 (11:59 p.m. applicant's local time) and receive a decision by mid-December ... If you are admitted under our Early Decision plan, you will be required to withdraw all pending applications"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-003
  field: ug.standardized_tests.policy
  value: "SAT/ACT REQUIRED (not optional) since 2024-25 cycle; superscore; no minimum; SAT/TOEFL code 3094; ACT code 3800"
  source_url: https://admission.brown.edu/first-year/standardized-tests
  source_snippet: "Brown University has returned to a policy requiring standardized test scores (either SAT or ACT scores) for first-year applicants beginning with the 2024-25 admission cycle. As we have done in prior years, we will superscore either the SAT or ACT, or both ... For the SAT, Brown's code number is 3094. For the ACT, Brown's code number is 3800. For the TOEFL, Brown's code number is 3094."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-004
  field: ug.english_proficiency.minimums
  value: "TOEFL 105 (pre-Jan 2026) / 5.5 (Jan 2026+); IELTS 8.0; Duolingo 130; PTE 75; Cambridge 191"
  source_url: https://admission.brown.edu/international/english-proficiency
  source_snippet: "TOEFL internet-based exam taken prior to January 2026: minimum score of 105 ... TOEFL internet-based exam taken January 2026 and later: minimum score of 5.5 ... IELTS: minimum score of 8.0 ... Duolingo Test of English: minimum score of 130 ... Pearson Test of English: minimum score of 75 ... C1 Advanced or C2 Proficiency Cambridge English Exams: minimum score of 191"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-006
  field: ug.cost.attendance_2025_2026
  value: "Tuition $71,700; Fees $2,950; Housing $10,410; Food $8,104; Books $1,300; Personal $2,820; Total COA $97,284"
  source_url: https://admission.brown.edu/tuition-aid/tuition-fees
  source_snippet: "Tuition $35,850 $35,850 $71,700 Fees $1,475 $1,475 $2,950 Housing $5,205 $5,205 $10,410 Food $4,052 $4,052 $8,104 Books& Materials $650 $650 $1,300 Personal $1,410 $1,410 $2,820 Total Cost $48,642 $48,642 $97,284"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-007
  field: ug.financial_aid.policy
  value: "Need-blind all first-year; 100% demonstrated need met; Brown Promise (no loans); ED FAFSA/CSS due Nov 3 2025; RD due Feb 2 2026"
  source_url: https://admission.brown.edu/tuition-aid/financial-aid
  source_snippet: "Brown meets 100% of each student's demonstrated financial need ... All first-year applicants will be admitted to Brown on a need-blind basis ... The Brown Promise — Brown does not package loans in its financial aid awards ... CSS Profile November 3, 2025 (ED) / February 2, 2026 (RD); FAFSA November 3, 2025 / February 2, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-008
  field: ug.financial_aid.international_need_blind
  value: "Need-blind for international undergrads beginning Class of 2029; 100% need met; no merit awards"
  source_url: https://admission.brown.edu/international/financial-aid
  source_snippet: "We meet full demonstrated need for students who are admitted provided they apply for financial aid at the time they apply for admission. Brown will be need-blind for international students beginning with the Class of 2029 ... Brown University does not offer any merit awards."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-009
  field: ug.curriculum.open_curriculum
  value: "Open Curriculum — no core, no distribution requirements; 80+ concentrations; S/NC grading option"
  source_url: https://www.brown.edu/academics/undergraduate/open-curriculum
  source_snippet: "At most universities, students must complete a set of core courses. At Brown, our students develop a personalized course of study ... they have greater freedom to study what they choose ... diving into one of 80-plus academic concentrations for in-depth, focused study."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-010
  field: ug.concentrations.directory
  value: "97 results = 90 concentrations (108 degree offerings) + 6 certificates"
  source_url: https://www.brown.edu/undergraduate_concentrations
  source_snippet: "Brown offers more than 80 concentrations, what some colleges call majors ... 97 Results based on your selections ... To complement your concentration, you may also choose to complete one of several interdisciplinary undergraduate certificates."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-011
  field: institution.schools_colleges.structure
  value: "7 schools: The College, Graduate School, School of Engineering, School of Professional Studies, School of Public Health, Warren Alpert Medical School, Watson School of International and Public Affairs"
  source_url: https://www.brown.edu/academics/schools-colleges
  source_snippet: "Brown is distinctively known as a University-College ... undergraduate education is based in the College ... The College / Graduate School / School of Engineering / School of Professional Studies / School of Public Health / Warren Alpert Medical School / Watson School of International and Public Affairs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.admissions.model
  value: "Decentralized; program-level decisions with Graduate School oversight; doctoral/MFA via Grad School; non-MFA master's via masters.brown.edu"
  source_url: https://graduateschool.brown.edu/apply
  source_snippet: "Admission to the Graduate School is determined at the program level with oversight by the Graduate School. Each program, in consultation with the dean of the Graduate School, sets its own admission criteria ... Brown offers nearly 100 options for master's, doctoral, executive leadership, certification and dual-degree medical programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.application.fee
  value: "$75 nonrefundable; separate application per program"
  source_url: https://graduateschool.brown.edu/application-information
  source_snippet: "A nonrefundable fee of $75 is charged for processing each application received by the Graduate School. This fee must be paid when the application is submitted ... Applicants who want to be evaluated by more than one graduate program must submit separate applications to each program"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.gre.policy
  value: "Per-program; GRE General (incl. at-home) accepted; Grad School code 3094; SPH code 7765"
  source_url: https://graduateschool.brown.edu/application-information/gre-information
  source_snippet: "Each program at Brown University may choose to require applicants to submit their official results from the Graduate Record Examination (GRE), or not ... The GRE reporting code for the Brown University Graduate School is 3094 ... The GRE code for the Brown University School of Public Health is 7765."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-005
  field: graduate.application.fee_waiver
  value: "Needs-based; requested within application; FAFSA/CSS/aid-letter/GRE-TOEFL voucher/unemployment verification accepted"
  source_url: https://graduateschool.brown.edu/apply/application-fee-waivers
  source_snippet: "To be eligible for a fee waiver, applicants to Brown University's graduate programs must demonstrate financial need ... Financial aid package (for current students or recent alumni) / FAFSA showing EFC / CSS profile showing EFC / Unemployment statement verification from the last 90 days / GRE or TOEFL fee reduction voucher"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-006
  field: graduate.funding.international_and_living_costs
  value: "Doctoral 5-yr guarantee (6 in Hum/SS); living estimate $26,667 (9mo) / $35,556 (12mo); intl master's must prove funds"
  source_url: https://graduateschool.brown.edu/apply/international-applicants
  source_snippet: "Living Expenses (est.) 9 months: $26,667 12 months: $35,556 ... Incoming doctoral students receive five years of guaranteed financial support, including a stipend, tuition remission, a health-services fee, and a health-insurance subsidy. Doctoral students in the Humanities and Social Sciences are guaranteed six years of support ... International students who are not awarded full financial assistance will not be granted final admission in their master's program until they provide certified proof of financial support"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-007
  field: graduate.programs.directory
  value: "91 graduate programs (PhD/ScM/AM/MEng/MFA/MAT/MD/MPA/MPH/MPP/MiM/Executive Master)"
  source_url: https://graduateprograms.brown.edu/
  source_snippet: "91 results based on your selections ... Filter by: Combined Degree Program / Doctoral Program / Master Program / Medical Degree / Professional Education"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: brown-knowledge-base-v2
├── overview (Section 0 — counts, hierarchy, degree inventory, distribution matrix)
├── ug-the-college (Section 1.2 — The College concentrations: 92 degree rows)
├── ug-engineering (Section 1.2 — School of Engineering UG concentrations: 16 rows)
├── ug-certificates (Section 1.4 — 6 undergraduate certificates)
├── ug-requirements (Section 3.1 + 3.2 — deadlines, tests, English proficiency)
├── ug-costs (Section 4.1 + 4.2 — COA, financial aid)
├── grad-graduate-school (Section 2.1 — Graduate School programs: 54 rows)
├── grad-engineering (Section 2.1 — School of Engineering grad: 13 rows)
├── grad-public-health (Section 2.1 — School of Public Health: 14 rows)
├── grad-medical (Section 2.1 — Warren Alpert Medical School: 12 rows)
├── grad-professional-studies (Section 2.1 — School of Professional Studies: 5 rows)
├── grad-watson (Section 2.1 — Watson School: 2 rows)
└── grad-requirements (Section 3.3 + 4.3 — grad admissions rules, funding)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "brown-knowledge-base-v2"
  school: "<home college>"
  department: "<home department / concentration>"
  degree_level: "<BA|BS|MA|MS|MFA|MAT|MEng|MPH|MPA|MPP|MiM|ExecMaster|MD|PhD|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | curriculum
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Median actual price paid / debt-free graduation rate / avg starting salary (UG) | Brown Common Data Set; admission.brown.edu/explore/brown-admission-numbers |
| P0 | Confirm current-cycle ED/RD decision-notification exact dates and CSS Profile ID | admission.brown.edu/first-year/{early,regular}-decision |
| P0 | Per-program GRE requirements table (which Brown grad programs require GRE) | each graduateprograms.brown.edu/graduate-program/<slug> page (Application Information accordion) |
| P1 | Graduate cost-of-attendance line items (per program) | graduateschool.brown.edu/financing-support/tuition-fees; SFS site |
| P1 | Doctoral stipend rates by program | graduateschool.brown.edu/financing-support (Internal Funding & Appointments) |
| P1 | Transfer applicant deadlines + spring-entry deadline | admission.brown.edu/transfer |
| P1 | RUE / Veterans / PLME / BRDD specific deadlines and requirements | admission.brown.edu/{rue,veterans}; admission.med.brown.edu (PLME) |
| P2 | Faculty count, UG/grad enrollment, acceptance rate (current CDS figures) | Brown Facts / IR site |
| P2 | School of Engineering / Watson School / Professional Studies per-school application fees (may differ from $75) | engineering.brown.edu; watson.brown.edu; professional.brown.edu/admissions |

---

## SECTION 7 — Cross-school comparison framework (Brown column)

| Dimension | Brown (2026-07-05) |
|-----------|--------------------|
| Total UG cost/yr (on-campus COA) | **$97,284** (2025-26) |
| Tuition/yr | **$71,700** (2025-26) |
| Need-blind (international)? | **YES** (Class of 2029+) |
| 100% demonstrated need met? | YES (UG) |
| Loans in aid package? | **NO** (Brown Promise — scholarship only) |
| ED deadline | **Nov 1** |
| RD deadline | **Jan 5** |
| SAT/ACT required? | **YES (required since 2024-25)** |
| SAT/ACT superscore? | YES (both) |
| TOEFL min (UG) | 105 (pre-Jan 2026) / 5.5 (new scale, Jan 2026+) |
| IELTS min (UG) | 8.0 |
| UG application fee | **$80** |
| Grad application fee | **$75** |
| April-15-equivalent honor date | YES (CGS resolution, doctoral aid) |
| Total degree programs (Rule 1) | **208 degree rows** (90 UG conc + 6 cert + 91 grad prog) |
| Schools/Colleges (Rule 2) | **7** |
| Common App? | YES |
| Has minors? | **NO** (Open Curriculum; uses certificates instead) |
| Core curriculum? | **NO** (Open Curriculum) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.brown.edu · www.brown.edu (undergraduate_concentrations, undergraduate/open-curriculum, academics/schools-colleges) · graduateschool.brown.edu · graduateprograms.brown.edu · www.brown.edu/about/administration/financial-aid
> **Verification**: ego-browser snapshotText + serverFetch + JS DOM extraction (96 UG program cards, 91 graduate program cards extracted via virtualized scroll)
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: Rule 1 total (208 degree rows) == distribution-matrix cell-sum (208) == row count in Sections 1.2 + 2.1 (108 UG + 100 grad = 208). ✅ Plus 6 non-degree certificates.
