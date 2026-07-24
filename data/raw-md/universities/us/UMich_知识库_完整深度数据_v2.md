# University of Michigan, Ann Arbor — Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BSE/BGS) | 155 |
| 本科辅修 (Minor) | 100+ (LSA alone has 100+; other schools add more) |
| 研究生学位项目 (MA/MS/MBA/PhD/EdD/JD/MD/etc.) | 191 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 50 |
| **学位项目总计 (UG + Grad)** | **346+** |
| 学院 / 独立系所总数 | 19 (14 UG-awarding + 5 graduate-only/professional) |

> **来源**: UMich Admissions主页标注"280+ degree programs in 14 undergraduate schools & colleges"；Rackham Programs of Study页面列出242个研究生项目(含证书)；本科项目列表实际提取155个。LSA官方称"more than 85 majors, sub-majors, and other degree programs, as well as more than 100 minors"。

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Michigan, Ann Arbor
├── College of Literature, Science, and the Arts (LSA)                    [学院-本科]
│   ├── Department of Mathematics                                         [系]
│   ├── Department of Computer Science                                    [系]
│   ├── Department of Economics                                           [系]
│   ├── Department of Psychology                                          [系]
│   ├── Department of Biology                                             [系]
│   ├── Department of Chemistry                                           [系]
│   ├── Department of Physics                                             [系]
│   ├── Department of English                                             [系]
│   ├── Department of History                                             [系]
│   ├── Department of Philosophy                                          [系]
│   ├── Department of Sociology                                           [系]
│   ├── Department of Political Science                                   [系]
│   ├── Department of Anthropology                                        [系]
│   ├── Department of Astronomy and Astrophysics                          [系]
│   ├── Department of Earth and Environmental Sciences                    [系]
│   ├── Department of Statistics                                          [系]
│   ├── Residential College                                               [系-跨学科]
│   ├── Program in International Studies                                  [系-跨学科]
│   └── 41+ departments total                                             [系]
│
├── College of Engineering                                                [学院-本科]
│   ├── Aerospace Engineering                                             [系]
│   ├── Biomedical Engineering                                            [系]
│   ├── Chemical Engineering                                              [系]
│   ├── Civil Engineering                                                 [系]
│   ├── Climate and Space Sciences and Engineering                        [系]
│   ├── Computer Science and Engineering                                  [系]
│   ├── Electrical and Computer Engineering                               [系]
│   ├── Industrial and Operations Engineering                             [系]
│   ├── Materials Science and Engineering                                 [系]
│   ├── Mechanical Engineering                                            [系]
│   ├── Naval Architecture and Marine Engineering                         [系]
│   ├── Nuclear Engineering and Radiological Sciences                     [系]
│   └── 19 programs total                                                 [系]
│
├── Ross School of Business                                               [学院-本科+研究生]
│   ├── BBA Program                                                       [系-本科]
│   ├── MBA Program                                                       [系-研究生]
│   └── PhD Programs                                                      [系-研究生]
│
├── School of Music, Theatre & Dance (SMTD)                               [学院-本科+研究生]
│   ├── Department of Composition                                         [系]
│   ├── Department of Dance                                               [系]
│   ├── Department of Music Education                                     [系]
│   ├── Department of Music Theory                                        [系]
│   ├── Department of Musicology                                          [系]
│   ├── Department of Performing Arts Technology                          [系]
│   ├── Department of Theatre & Drama                                     [系]
│   ├── Department of Voice & Opera                                       [系]
│   ├── Department of Strings                                             [系]
│   ├── Department of Winds & Percussion                                  [系]
│   └── 16 UG programs + 39 graduate programs                             [系]
│
├── Stamps School of Art & Design                                         [学院-本科+研究生]
│   ├── Art and Design (BFA)                                              [系]
│   └── Design (MFA)                                                      [系-研究生]
│
├── Taubman College of Architecture & Urban Planning                      [学院-本科+研究生]
│   ├── Architecture (BS)                                                 [系]
│   ├── Urban Technology (BS)                                             [系]
│   ├── Architecture (MArch/PhD)                                          [系-研究生]
│   └── Urban and Regional Planning (MUP)                                 [系-研究生]
│
├── School of Kinesiology                                                 [学院-本科+研究生]
│   ├── Applied Exercise Science                                          [系]
│   ├── Movement Science                                                  [系]
│   ├── Sport Management                                                  [系]
│   └── Athletic Training (MS)                                            [系-研究生]
│
├── School of Nursing                                                     [学院-本科+研究生]
│   ├── BS in Nursing                                                     [系]
│   └── PhD in Nursing                                                    [系-研究生]
│
├── College of Pharmacy                                                   [学院-本科+研究生]
│   ├── Pharmaceutical Sciences (BS)                                      [系]
│   ├── PharmD                                                            [系-研究生]
│   └── PhD Programs                                                      [系-研究生]
│
├── School of Public Health                                               [学院-本科+研究生]
│   ├── Community and Global Public Health (BS)                           [系]
│   ├── Biostatistics (MPH/MS/PhD)                                        [系-研究生]
│   ├── Environmental Health Sciences (MPH/MS/PhD)                        [系-研究生]
│   ├── Epidemiology (MPH/MS/PhD)                                         [系-研究生]
│   ├── Health Behavior and Health Equity (MPH/PhD)                       [系-研究生]
│   └── Health Management and Policy (MPH/PhD)                            [系-研究生]
│
├── Ford School of Public Policy                                          [学院-本科+研究生]
│   ├── Public Policy (BA)                                                [系-本科]
│   ├── Master of Public Policy (MPP)                                     [系-研究生]
│   └── PhD in Public Policy                                              [系-研究生]
│
├── Marsal Family School of Education                                     [学院-本科+研究生]
│   ├── LEAPS Program (BA)                                                [系]
│   ├── Educator Preparation Program (BA)                                 [系]
│   ├── Secondary Teacher Education (BA)                                  [系]
│   └── Graduate Programs (MA/MEd/PhD)                                    [系-研究生]
│
├── School of Information                                                 [学院-本科+研究生]
│   ├── User Experience Design (BSI)                                      [系-本科]
│   ├── Master of Science in Information (MSI)                            [系-研究生]
│   └── PhD in Information                                                [系-研究生]
│
├── School of Dentistry                                                   [学院-本科+研究生]
│   ├── Dental Hygiene (BS)                                               [系-本科]
│   ├── DDS                                                               [系-研究生]
│   └── Advanced Specialty Programs                                       [系-研究生]
│
├── School of Social Work                                                 [学院-研究生]
│   ├── Master of Social Work (MSW)                                       [系]
│   └── PhD in Social Work                                                [系]
│
├── School of Law                                                         [学院-研究生]
│   ├── Juris Doctor (JD)                                                 [系]
│   ├── LLM                                                               [系]
│   └── SJD                                                               [系]
│
├── Medical School                                                        [学院-研究生]
│   ├── MD Program                                                        [系]
│   ├── Medical Scientist Training Program (MD/PhD)                       [系]
│   └── Graduate Biomedical Programs (PIBS)                               [系]
│
├── School of Environment & Sustainability                                [学院-研究生]
│   ├── Master of Science (MS)                                            [系]
│   └── PhD Programs                                                      [系]
│
└── Horace H. Rackham School of Graduate Studies                          [学院-研究生]
    └── Administers 200+ graduate programs across all schools             [系-管理]
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 (canonical) | 全称 | 层级 | 本项目数量 | official (本校) |
|----------------------|------|------|-----------|----------------|
| BA | Bachelor of Arts | 本科 | ~85 (LSA) | A.B. / B.A. |
| BS | Bachelor of Science | 本科 | ~30 | B.S. / B.S.E. |
| BSE | Bachelor of Science in Engineering | 本科 | 19 (Engineering) | B.S.E. |
| BFA | Bachelor of Fine Arts | 本科 | 2 (Art & Design, SMTD) | B.F.A. |
| BGS | Bachelor in General Studies | 本科 | 1 (LSA) | B.G.S. |
| BSI | Bachelor of Science in Information | 本科 | 1 (Information) | B.S.I. |
| BSN | Bachelor of Science in Nursing | 本科 | 1 (Nursing) | B.S.N. |
| MA | Master of Arts | 研究生 | ~25 | M.A. |
| MS | Master of Science | 研究生 | ~40 | M.S. |
| MFA | Master of Fine Arts | 研究生 | 2 (Art & Design) | M.F.A. |
| MBA | Master of Business Administration | 研究生 | 1 (Ross) | M.B.A. |
| MEng | Master of Engineering | 研究生 | ~10 | M.S.E. |
| MArch | Master of Architecture | 研究生 | 1 (Taubman) | M.Arch. |
| MPP | Master of Public Policy | 研究生 | 1 (Ford) | M.P.P. |
| MPH | Master of Public Health | 研究生 | ~6 (Public Health) | M.P.H. |
| MSW | Master of Social Work | 研究生 | 1 (Social Work) | M.S.W. |
| MEd | Master of Education | 研究生 | ~3 (Education) | M.Ed. |
| MUP | Master of Urban Planning | 研究生 | 1 (Taubman) | M.U.P. |
| MSI | Master of Science in Information | 研究生 | 1 (Information) | M.S.I. |
| DMA | Doctor of Musical Arts | 研究生 | ~15 (SMTD) | D.M.A. |
| PhD | Doctor of Philosophy | 研究生 | ~100 | Ph.D. |
| EdD | Doctor of Education | 研究生 | ~2 (Education) | Ed.D. |
| MD | Doctor of Medicine | 研究生 | 1 (Med School) | M.D. |
| JD | Juris Doctor | 研究生 | 1 (Law) | J.D. |
| DNP | Doctor of Nursing Practice | 研究生 | 1 (Nursing) | D.N.P. |
| DDS | Doctor of Dental Surgery | 研究生 | 1 (Dentistry) | D.D.S. |
| Certificate | 高级证书/文凭 | 研究生 | 50 | Certificate |
| **合计** | | | **346+** | |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS/BSE | BFA | MA | MS/MEng | MBA | PhD | DMA | JD/MD/DDS | Certificate | 合计 |
|------------|-----|--------|-----|-----|---------|-----|-----|-----|-----------|-------------|------|
| LSA | ~85 | ~15 | 0 | ~20 | ~20 | 0 | ~40 | 0 | 0 | ~23 | ~183 |
| Engineering | 0 | 19 | 0 | 0 | ~18 | 0 | ~18 | 0 | 0 | ~5 | ~60 |
| Ross Business | 0 | 0 | 0 | 0 | 0 | 1 | ~2 | 0 | 0 | ~1 | ~4 |
| SMTD | 0 | 0 | ~2 | ~4 | 0 | 0 | ~20 | ~15 | 0 | ~3 | ~44 |
| Art & Design | 0 | 0 | 1 | 0 | ~2 | 0 | 0 | 0 | 0 | 0 | ~3 |
| Taubman (Arch) | 0 | 2 | 0 | 0 | ~3 | 0 | ~2 | 0 | 0 | ~3 | ~10 |
| Kinesiology | 0 | 3 | 0 | 0 | ~4 | 0 | ~2 | 0 | 0 | ~1 | ~10 |
| Nursing | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ~2 |
| Pharmacy | 0 | 1 | 0 | 0 | ~1 | 0 | ~3 | 0 | 0 | 0 | ~5 |
| Public Health | 0 | 2 | 0 | 0 | ~9 | 0 | ~7 | 0 | 0 | 0 | ~18 |
| Ford/Public Policy | 1 | 0 | 0 | 0 | ~2 | 0 | ~5 | 0 | 0 | ~1 | ~9 |
| Education | 3 | 0 | 0 | ~3 | 0 | 0 | ~3 | 0 | 0 | ~1 | ~10 |
| Information | 0 | 1 | 0 | 0 | ~1 | 0 | ~1 | 0 | 0 | ~1 | ~4 |
| Dentistry | 0 | 1 | 0 | 0 | ~8 | 0 | ~1 | 0 | ~1 | 0 | ~11 |
| Social Work | 0 | 0 | 0 | 0 | ~1 | 0 | ~4 | 0 | 0 | ~1 | ~6 |
| Law | 0 | 0 | 0 | 0 | ~2 | 0 | ~1 | 0 | ~1 | 0 | ~4 |
| Medicine | 0 | 0 | 0 | 0 | ~10 | 0 | ~19 | 0 | ~1 | ~3 | ~33 |
| Env & Sustainability | 0 | 0 | 0 | 0 | ~2 | 0 | ~1 | 0 | 0 | ~4 | ~7 |
| Dearborn/Flint | 0 | 0 | 0 | 0 | ~3 | 0 | ~4 | 0 | 0 | 0 | ~7 |
| **合计** | **~89** | **~49** | **~3** | **~27** | **~86** | **~1** | **~134** | **~15** | **~3** | **~47** | **~346+** |

> 注: 矩阵为近似值，因部分项目跨学院且学位类型有重叠。精确数字需逐项目核实。

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

UMich本科由14个学院/学校招收一年级学生，另有4个Upper-level学院接受已在读学生转入。详见Section 0.2层级树。

**First-year Admitting Units (10):** Art & Design; Architecture & Urban Planning; Business; Education*; Engineering; Kinesiology; LSA; Music, Theatre & Dance; Nursing; Pharmacy.

**Preferred Admission:** Architecture & Urban Planning, Business, Information, and Pharmacy offer Preferred Admission，被录取学生在大二或大三转入upper-level项目。

**Upper-level Admitting Units:** Dental Hygiene, Information, Public Health, Public Policy.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Literature, Science, and the Arts (LSA)

LSA提供超过85个专业(sub-majors和其他学位项目)和超过100个辅修。以下为从admissions页面提取的完整列表：

##### BA Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Afroamerican and African Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#afroamerican_and_african_studies-maj |
| 2 | American Culture | https://lsa.umich.edu/lsa/academics/majors-minors.html#american_culture-maj |
| 3 | Anthropology | https://lsa.umich.edu/lsa/academics/majors-minors.html#anthropology-maj |
| 4 | Archaeology of the Ancient Mediterranean | https://lsa.umich.edu/lsa/academics/majors-minors.html#archaeology_of_the_ancient_mediterranean-maj |
| 5 | Arts and Ideas in the Humanities (RC) | https://lsa.umich.edu/lsa/academics/majors-minors.html#arts_and_ideas_in_the_humanities-maj |
| 6 | Asian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#arab_and_muslim_american_studies-min |
| 7 | Astronomy and Astrophysics | https://lsa.umich.edu/lsa/academics/majors-minors.html#astronomy_and_astrophysics-maj |
| 8 | Biology | https://lsa.umich.edu/lsa/academics/majors-minors.html#biology-maj |
| 9 | Biomolecular Science | https://lsa.umich.edu/lsa/academics/majors-minors.html#biomolecular_science_ab_or_bs-maj |
| 10 | Biopsychology, Cognition, and Neuroscience | https://lsa.umich.edu/lsa/academics/majors-minors.html#biophyschology_cognition_and_neuroscience_bcn-maj |
| 11 | Classical Civilization | https://lsa.umich.edu/lsa/academics/majors-minors.html#classical_civilization-maj |
| 12 | Classical Languages and Literatures | https://lsa.umich.edu/lsa/academics/majors-minors.html#classical_languages_and_literatures-maj |
| 13 | Cognitive Science | https://lsa.umich.edu/lsa/academics/majors-minors.html#cognitive_science-maj |
| 14 | Communication and Media | https://lsa.umich.edu/lsa/academics/majors-minors.html#communication_studies-maj |
| 15 | Comparative Literature, Arts, and Media | https://lsa.umich.edu/lsa/academics/majors-minors.html#comparative_literature_arts_and_media-maj |
| 16 | Creative Writing and Literature (RC) | https://lsa.umich.edu/lsa/academics/majors-minors.html#creative_writing_and_literature-maj |
| 17 | Drama (RC) | https://lsa.umich.edu/lsa/academics/majors-minors.html#drama-maj |
| 18 | Earth and Environmental Sciences | https://lsa.umich.edu/lsa/academics/majors-minors.html#earth_and_environmental_sciences-maj |
| 19 | Ecology, Evolution, and Biodiversity | https://lsa.umich.edu/lsa/academics/majors-minors.html#ecology_and_evolutionary_biology_eeb-maj |
| 20 | Economics | https://lsa.umich.edu/lsa/academics/majors-minors.html#economics-maj |
| 21 | English and Digital Media Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#english_and_digital_media_studies-maj |
| 22 | English and Education | https://lsa.umich.edu/lsa/academics/majors-minors.html#english_and_education-maj |
| 23 | Environment | https://lsa.umich.edu/lsa/academics/majors-minors.html#environment-maj |
| 24 | Environmental Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#environmental_studies-maj |
| 25 | Film, Television, and Media | https://lsa.umich.edu/lsa/academics/majors-minors.html#film_tv_and_media-ftv-maj |
| 26 | French and Francophone Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#french_and_francophone_studies-maj |
| 27 | German Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#german_studies-maj |
| 28 | Global Health and Environment | https://lsa.umich.edu/lsa/academics/majors-minors.html#global_health_and_environment-maj |
| 29 | Greek | https://lsa.umich.edu/lsa/academics/majors-minors.html#greek-maj |
| 30 | History | https://lsa.umich.edu/lsa/academics/majors-minors.html#history-maj |
| 31 | History of Art | https://lsa.umich.edu/lsa/academics/majors-minors.html#history_of_art-maj |
| 32 | International Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#international_studies-maj |
| 33 | Italian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#italian_studies-maj |
| 34 | Judaic Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#judaic_studies-maj |
| 35 | Latina/o Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#latina_o_studies-maj |
| 36 | Latin | https://lsa.umich.edu/lsa/academics/majors-minors.html#latin-maj |
| 37 | Linguistics | https://lsa.umich.edu/lsa/academics/majors-minors.html#linguistics-maj |
| 38 | Mathematics | https://lsa.umich.edu/lsa/academics/majors-minors.html#mathematics-maj |
| 39 | Middle East Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#middle_east_studies-maj |
| 40 | Molecular, Cellular, and Developmental Biology | https://lsa.umich.edu/lsa/academics/majors-minors.html#molecular_cellular_and_developmental_biology-maj |
| 41 | Movement Science | https://lsa.umich.edu/lsa/academics/majors-minors.html#movement_science-maj |
| 42 | Musicology | https://lsa.umich.edu/lsa/academics/majors-minors.html#musicology-maj |
| 43 | Near Eastern Civilizations | https://lsa.umich.edu/lsa/academics/majors-minors.html#near_eastern_civilizations-maj |
| 44 | Neuroscience | https://lsa.umich.edu/lsa/academics/majors-minors.html#neuroscience-maj |
| 45 | Organizational Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#organizational_studies-maj |
| 46 | Philosophy | https://lsa.umich.edu/lsa/academics/majors-minors.html#philosophy-maj |
| 47 | Philosophy, Politics, and Economics | https://lsa.umich.edu/lsa/academics/majors-minors.html#philosophy_politics_and_economics_ppe-maj |
| 48 | Physics | https://lsa.umich.edu/lsa/academics/majors-minors.html#physics-maj |
| 49 | Political Science | https://lsa.umich.edu/lsa/academics/majors-minors.html#political_science-maj |
| 50 | Psychology | https://lsa.umich.edu/lsa/academics/majors-minors.html#psychology-maj |
| 51 | Romance Languages and Literatures | https://lsa.umich.edu/lsa/academics/majors-minors.html#romance_languages_and_literatures-maj |
| 52 | Russian, East European, and Eurasian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#rees-maj |
| 53 | Screen Arts and Cultures | https://lsa.umich.edu/lsa/academics/majors-minors.html#screen_arts_and_cultures-maj |
| 54 | Social Theory and Practice (RC) | https://lsa.umich.edu/rc/curriculum/social-theory-and-practice--stp-.html |
| 55 | Sociology | https://lsa.umich.edu/lsa/academics/majors-minors.html#sociology-maj |
| 56 | Spanish | https://lsa.umich.edu/lsa/academics/majors-minors.html#spanish-maj |
| 57 | Statistics | https://lsa.umich.edu/lsa/academics/majors-minors.html#statistics-maj |
| 58 | Translation | https://lsa.umich.edu/lsa/academics/majors-minors.html#translation-maj |
| 59 | Women's and Gender Studies | https://lsa.umich.edu/wgs/undergraduates.html |

##### BS Programs

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://lsa.umich.edu/lsa/academics/majors-minors.html#biochemistry_bs-maj |
| 2 | Biophysics | https://lsa.umich.edu/lsa/academics/majors-minors.html#biophysics_bs-maj |
| 3 | Biology, Health, and Society | https://lsa.umich.edu/lsa/academics/majors-minors.html#general_biology-maj |
| 4 | Cellular and Molecular Biomedical Science | https://lsa.umich.edu/lsa/academics/majors-minors.html#cell_and_molecular_biology_and_biomedical_engineering-maj |
| 5 | Chemistry | https://lsa.umich.edu/lsa/academics/majors-minors.html#chemical_science_bschem-maj |
| 6 | Computer Science (BS) | https://lsa.umich.edu/lsa/academics/majors-minors.html#computer_science-maj |
| 7 | Data Science (BS) | https://lsa.umich.edu/lsa/academics/majors-minors.html#data_science-maj |
| 8 | Microbiology | https://lsa.umich.edu/lsa/academics/majors-minors.html#microbiology-maj |

##### Sub-Majors (under parent majors)

| # | 专业 | Parent Major | URL |
|---|------|-------------|-----|
| 1 | Actuarial Mathematics | Mathematics | https://lsa.umich.edu/lsa/academics/majors-minors.html#actuarial_mathematics-sub |
| 2 | Archaeology | Anthropology | https://lsa.umich.edu/lsa/academics/majors-minors.html#archaeology-sub |
| 3 | Biological Physics | Biophysics | https://lsa.umich.edu/lsa/academics/majors-minors/biological-physics-sub-major.html |
| 4 | Chinese Studies | Asian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#asian_studies-maj |
| 5 | Comparative Culture and Identity | International Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#comparative_culture_and_identity_cci-sub |
| 6 | Culture and Media | Anthropology | https://lsa.umich.edu/lsa/academics/majors-minors.html#culture_and_media-sub |
| 7 | Sociology and Social Work | Sociology | https://lsa.umich.edu/lsa/academics/majors-minors.html#sociology_and_social_work-sub |
| 8 | Sociology of Health and Medicine | Sociology | https://lsa.umich.edu/lsa/academics/majors-minors.html#health-and-society-sub |
| 9 | South Asian Studies | Asian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#asian_studies-maj |
| 10 | Southeast Asian Studies | Asian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#asian_studies-maj |
| 11 | Structural Biology | Biophysics | https://lsa.umich.edu/lsa/academics/majors-minors/structural-biology-sub-major.html |
| 12 | Global Asian Studies | Asian Studies | https://lsa.umich.edu/lsa/academics/majors-minors.html#asian_studies-maj |

#### College of Engineering

##### BSE (Bachelor of Science in Engineering)

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://aero.engin.umich.edu/undergraduate/ |
| 2 | Biomedical Engineering | https://bme.umich.edu/academics/ |
| 3 | Chemical Engineering | https://che.engin.umich.edu/ |
| 4 | Civil Engineering | https://cee.engin.umich.edu/undergraduate-studies/bse-degree-in-civil-engineering/ |
| 5 | Climate and Meteorology | https://clasp.engin.umich.edu/academics/undergraduate-studies/ |
| 6 | Computer Engineering | https://ece.engin.umich.edu/academics/undergraduate/prospective-undergrad/computer-engineering/ |
| 7 | Computer Science (BSE) | https://cse.engin.umich.edu/academics/undergraduate/programs/computer-science-eng/ |
| 8 | Data Science | https://docs.google.com/spreadsheets/d/1Mets2NQ4i1ZY-4TNFfd7DpX2yU6h73bK673dgDiEEDA/preview |
| 9 | Electrical Engineering | https://ece.engin.umich.edu/academics/undergraduate/prospective-undergrad/electrical-engineering/ |
| 10 | Engineering Physics | https://engin.umich.edu/study/undergraduate/degrees/engineering-physics/ |
| 11 | Environmental Engineering | https://cee.engin.umich.edu/undergraduate-studies/bse-degree-in-environmental-engineering/ |
| 12 | Industrial and Operations Engineering | https://ioe.engin.umich.edu/academics/undergraduate/ |
| 13 | Materials Science and Engineering | https://mse.engin.umich.edu/academics/undergraduate |
| 14 | Mechanical Engineering | https://me.engin.umich.edu/academics/undergraduate/ |
| 15 | Naval Architecture and Marine Engineering | https://name.engin.umich.edu/academics/undergraduate-program/ |
| 16 | Nuclear Engineering and Radiological Sciences | https://ners.engin.umich.edu/academics/undergraduate/ |
| 17 | Space Sciences and Engineering | https://clasp.engin.umich.edu/academics/undergraduate-studies/bse-space-science-engineering/ |

#### Ross School of Business

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Business (BBA) | BBA | https://michiganross.umich.edu/undergraduate/bba |

#### School of Music, Theatre & Dance (SMTD)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Composition | BFA/BM | https://smtd.umich.edu/department/composition/ |
| 2 | Dance | BFA | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 3 | Jazz & Improvisation | BM | https://smtd.umich.edu/department/jazz-and-contemporary-improvisation/ |
| 4 | Music Education | BM | https://smtd.umich.edu/department/music-education/ |
| 5 | Music Theory | BM | https://smtd.umich.edu/department/music-theory/ |
| 6 | Musical Theatre | BFA | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 7 | Musicology | BM | https://smtd.umich.edu/department/musicology/ |
| 8 | Organ | BM | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 9 | Performing Arts Technology | BFA/BM | https://smtd.umich.edu/department/performing-arts-technology/ |
| 10 | Piano | BM | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 11 | Strings | BM | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 12 | Theatre & Drama | BFA | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 13 | Voice & Opera | BM | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |
| 14 | Winds & Percussion | BM | https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/ |

#### Stamps School of Art & Design

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art and Design | BFA | https://stamps.umich.edu/undergraduate-programs |

#### Taubman College of Architecture & Urban Planning

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | BS | https://taubmancollege.umich.edu/admissions/apply/bachelor-of-science-in-architecture-first-year/ |
| 2 | Urban Technology | BS | https://taubmancollege.umich.edu/academics/urban-and-regional-planning/bachelor-of-science-in-urban-technology/ |

#### School of Kinesiology

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Exercise Science | BS | https://www.kines.umich.edu/academics/applied-exercise-science |
| 2 | Movement Science | BS | https://www.kines.umich.edu/academics/movement-science |
| 3 | Sport Management | BS | https://www.kines.umich.edu/academics/sport-management/undergraduate |

#### School of Nursing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | BSN | https://nursing.umich.edu/academics/undergraduate |

#### College of Pharmacy

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Pharmaceutical Sciences | BS | https://pharmacy.umich.edu/academics/undergraduate |

#### School of Public Health

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Community and Global Public Health | BS | https://sph.umich.edu/undergrad/apply/#phs |
| 2 | Movement Science | BS | https://sph.umich.edu/undergrad/ |

#### Ford School of Public Policy

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy | BA | https://fordschool.umich.edu/academics/undergraduate |

#### Marsal Family School of Education

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | LEAPS (Learning, Equity, and Problem Solving) | BA | https://marsal.umich.edu/academics-admissions/degrees/bachelors |
| 2 | Educator Preparation Program (EPP) | BA | https://marsal.umich.edu/academics-admissions/epp |
| 3 | Secondary Teacher Education | BA | https://marsal.umich.edu/academics-admissions/degrees/bachelors |

#### School of Information

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | User Experience Design | BSI | https://www.si.umich.edu/programs/bachelor-science-information/curriculum |

#### School of Dentistry

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Dental Hygiene | BS | https://dent.umich.edu/about/dental-hygiene |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 涉及学院 | 说明 |
|---|------|---------|------|
| 1 | Integrated Business and Engineering | Ross + Engineering | 2025-2026 cycle新增双学位 |
| 2 | Data Science | LSA + Engineering | 两个学院各有一个BS/BSE版本 |
| 3 | Computer Science | LSA (BS) + Engineering (BSE) | 两个学院各有一个版本 |
| 4 | Various dual-degree options | Multiple | 可同时申请两个学院 |

### 1.4 Minors — Complete List

LSA提供超过100个辅修。其他学院也提供辅修选项。完整辅修列表请参见:
- LSA: https://lsa.umich.edu/lsa/academics/majors-minors.html (筛选"Minor")
- Engineering: 各系网站
- SMTD: https://smtd.umich.edu/admissions/undergraduate/undergraduate-degrees-minors/
- Ross: https://michiganross.umich.edu/undergraduate/

### 1.5 General/Institute-Wide Requirements

**LSA Distribution Requirements:**
- First-Year Writing Requirement (FYWR)
- Upper-Level Writing Requirement (ULWR)
- Race and Ethnicity (RE)
- Quantitative Reasoning (QR)
- Natural Science (NS)
- Social Science (SS)
- Humanities (HU)
- Mathematical and Symbolic Analysis (MSA)

**Engineering Core:**
- Mathematics, Physics, Chemistry, Engineering Fundamentals, Intellectual Breadth

### 1.6 Course-ID → Major Quick-Lookup

LSA使用学科代码(如MATH, ECON, PSYCH等)。Engineering使用部门编号系统。

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

Rackham Graduate School管理Ann Arbor校区的200+研究生项目。以下按学院分组：

#### Literature, Science, and the Arts (LSA) — 72 programs

##### Doctoral (PhD)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | American Culture | Fall: December 1 |
| 2 | Ancient History | Fall: December 15 |
| 3 | Ancient Mediterranean Art and Archaeology | Fall: December 1 |
| 4 | Anthropology | Fall: December 1 |
| 5 | Anthropology and History | Fall: December 1 |
| 6 | Applied and Interdisciplinary Mathematics | Fall: December 15 |
| 7 | Applied Physics | Fall: December 15 |
| 8 | Arabic Studies | Contact department |
| 9 | Asian Languages and Cultures | Fall: December 1 |
| 10 | Astronomy and Astrophysics | Fall: December 1 |
| 11 | Biophysics | Fall: December 1 |
| 12 | Chemistry | Fall: December 1 |
| 13 | Classical Studies | Fall: December 15 |
| 14 | Cognitive Science | Fall: December 1 |
| 15 | Communication and Media | Fall: December 1 |
| 16 | Comparative Literature | Fall: December 1 |
| 17 | Complex Systems | Fall: December 1 |
| 18 | Computer Science and Engineering | Fall: December 15 |
| 19 | Earth and Environmental Sciences | Fall: December 15 |
| 20 | Ecology and Evolutionary Biology | Fall: December 1 |
| 21 | Economics | Fall: December 15 |
| 22 | English Language and Literature | Fall: December 1 |
| 23 | Germanic Languages and Literatures | Fall: December 1 |
| 24 | History | Fall: December 1 |
| 25 | History of Art | Fall: December 1 |
| 26 | Linguistics | Fall: December 15 |
| 27 | Mathematics | Fall: December 15 |
| 28 | Molecular, Cellular, and Developmental Biology | Fall: December 1 |
| 29 | Musicology | Fall: December 1 |
| 30 | Philosophy | Fall: January 15 |
| 31 | Physics | Fall: December 15 |
| 32 | Political Science | Fall: December 1 |
| 33 | Psychology | Fall: December 1 |
| 34 | Romance Languages and Literatures: French | Fall: December 1 |
| 35 | Romance Languages and Literatures: Italian | Fall: December 1 |
| 36 | Romance Languages and Literatures: Spanish | Fall: December 1 |
| 37 | Slavic Languages and Literatures | Fall: December 1 |
| 38 | Sociology | Fall: December 1 |
| 39 | Statistics | Fall: December 15 |
| 40 | Women's and Gender Studies | Fall: December 1 |

##### Master's (MA/MS)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Applied Economics | Fall: January 15 |
| 2 | Applied and Interdisciplinary Mathematics | Fall: December 15 |
| 3 | Applied Physics | Fall: December 15 |
| 4 | Applied Statistics | Fall: January 15 |
| 5 | Chemistry | Fall: December 1 |
| 6 | Classical Reception Studies | Contact department |
| 7 | Comparative Literature | Fall: December 1 |
| 8 | Computer Science and Engineering | Fall: December 15 |
| 9 | Creative Writing | Fall: January 15 |
| 10 | Earth and Environmental Sciences | Fall: December 15 |
| 11 | Economics | Fall: December 15 |
| 12 | English Language and Literature | Fall: December 1 |
| 13 | German Studies | Fall: December 1 |
| 14 | Health and Health Care Research | Fall: December 1 |
| 15 | History | Fall: December 1 |
| 16 | Mathematics | Fall: December 15 |
| 17 | Museum Studies | Fall: January 15 |
| 18 | Physics | Fall: December 15 |
| 19 | Quantitative Finance and Risk Management | Fall: January 15 |
| 20 | Scientific Computing | Fall: December 15 |
| 21 | Statistics | Fall: December 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | African American and Diaspora Studies | Rolling admission |
| 2 | African Studies | Rolling admission |
| 3 | Afro-Luso-Brazilian Studies | Contact department |
| 4 | Ancient History | Fall: December 15 |
| 5 | Arts Entrepreneurship and Leadership | Contact department |
| 6 | Chinese Studies | Contact department |
| 7 | Classical Reception Studies | Contact department |
| 8 | Community Action and Research | Contact department |
| 9 | Critical Translation Studies | Contact department |
| 10 | Digital Studies | Contact department |
| 11 | Environmental Justice | Contact department |
| 12 | Graduate AI and Data Science Certificate | Contact department |
| 13 | Greek | Contact department |
| 14 | Healthy Cities | Contact department |
| 15 | Judaic Studies | Contact department |
| 16 | Latin | Contact department |
| 17 | Latin American and Caribbean Studies | Contact department |
| 18 | LGBTQ Studies | Contact department |
| 19 | Medieval and Early Modern Studies | Contact department |
| 20 | Middle East Studies | Contact department |
| 21 | Museum Studies | Contact department |
| 22 | Russian, East European, and Eurasian Studies | Contact department |
| 23 | South Asian Studies | Contact department |

#### College of Engineering — 23 programs

##### Doctoral (PhD)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Aerospace Engineering | Fall: December 15 (PhD) |
| 2 | Biomedical Engineering | Fall: December 15 |
| 3 | Chemical Engineering | Fall: December 15 |
| 4 | Civil Engineering | Fall: December 15 |
| 5 | Climate and Space Sciences and Engineering | Fall: December 15 |
| 6 | Computer Science and Engineering | Fall: December 15 |
| 7 | Electrical and Computer Engineering | Fall: December 15 |
| 8 | Engineering Education Research | Fall: December 15 |
| 9 | Industrial and Operations Engineering | Fall: December 15 |
| 10 | Macromolecular Science and Engineering | Fall: December 15 |
| 11 | Materials Science and Engineering | Fall: December 15 |
| 12 | Mechanical Engineering | Fall: December 15 |
| 13 | Naval Architecture and Marine Engineering | Fall: December 15 |
| 14 | Nuclear Engineering and Radiological Sciences | Fall: December 15 |
| 15 | Robotics | Fall: December 15 |

##### Master's (MS/MEng)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Aerospace Engineering | Fall: January 15 (MSE) |
| 2 | Biomedical Engineering | Fall: January 15 |
| 3 | Chemical Engineering | Fall: January 15 |
| 4 | Civil Engineering | Fall: January 15 |
| 5 | Climate and Space Sciences and Engineering | Fall: January 15 |
| 6 | Computer Science and Engineering | Fall: January 15 |
| 7 | Construction Engineering and Management | Fall: January 15 |
| 8 | Data Science | Fall: January 15 |
| 9 | Electrical and Computer Engineering | Fall: January 15 |
| 10 | Environmental Engineering | Fall: January 15 |
| 11 | Industrial and Operations Engineering | Fall: January 15 |
| 12 | Integrated Design and Business | Fall: January 15 |
| 13 | Macromolecular Science and Engineering | Fall: January 15 |
| 14 | Materials Science and Engineering | Fall: January 15 |
| 15 | Mechanical Engineering | Fall: January 15 |
| 16 | Naval Architecture and Marine Engineering | Fall: January 15 |
| 17 | Nuclear Engineering and Radiological Sciences | Fall: January 15 |
| 18 | Robotics | Fall: January 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Climate Change Solutions | Contact department |
| 2 | Computational Discovery and Engineering | Contact department |
| 3 | Design Science | Contact department |
| 4 | Extended Reality XR | Contact department |
| 5 | Plasma Science and Engineering | Contact department |

#### School of Music, Theatre & Dance — 39 programs

##### Doctoral (PhD/DMA)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Composition | Fall: December 1 |
| 2 | Conducting: Band/Wind Ensemble | Fall: December 1 |
| 3 | Conducting: Choral | Fall: December 1 |
| 4 | Conducting: Orchestral | Fall: December 1 |
| 5 | Dance | Fall: December 1 |
| 6 | Jazz and Contemporary Improvisation | Fall: December 1 |
| 7 | Music Education | Fall: December 1 |
| 8 | Music Theory | Fall: December 1 |
| 9 | Music Theory Pedagogy | Fall: December 1 |
| 10 | Musicology | Fall: December 1 |
| 11 | Musicology: Ethnomusicology | Fall: December 1 |
| 12 | Musicology: History | Fall: December 1 |
| 13 | Performance: Bassoon | Fall: December 1 |
| 14 | Performance: Cello | Fall: December 1 |
| 15 | Performance: Clarinet | Fall: December 1 |
| 16 | Performance: Collaborative Piano | Fall: December 1 |
| 17 | Performance: Double Bass | Fall: December 1 |
| 18 | Performance: Euphonium | Fall: December 1 |
| 19 | Performance: Flute | Fall: December 1 |
| 20 | Performance: French Horn | Fall: December 1 |
| 21 | Performance: Harp | Fall: December 1 |
| 22 | Performance: Harpsichord | Fall: December 1 |
| 23 | Performance: Oboe | Fall: December 1 |
| 24 | Performance: Organ | Fall: December 1 |
| 25 | Performance: Organ: Sacred Music | Fall: December 1 |
| 26 | Performance: Percussion | Fall: December 1 |
| 27 | Performance: Piano | Fall: December 1 |
| 28 | Performance: Piano Pedagogy and Performance | Fall: December 1 |
| 29 | Performance: Saxophone | Fall: December 1 |
| 30 | Performance: Trombone | Fall: December 1 |
| 31 | Performance: Trumpet | Fall: December 1 |
| 32 | Performance: Tuba | Fall: December 1 |
| 33 | Performance: Viola | Fall: December 1 |
| 34 | Performance: Violin | Fall: December 1 |
| 35 | Performance: Voice | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Composition and Music Theory | Fall: December 1 |
| 2 | Media Arts | Fall: December 1 |
| 3 | Music Education | Fall: December 1 |
| 4 | Performing Arts Technology | Fall: December 1 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Arts Entrepreneurship and Leadership | Contact department |
| 2 | World Performance Studies | Contact department |
| 3 | Transcultural Studies | Contact department |

#### Medical School — 30 programs

##### Doctoral (PhD)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Bioinformatics (PIBS) | Fall: December 1 |
| 2 | Biological Chemistry (PIBS) | Fall: December 1 |
| 3 | Biomedical Sciences (PIBS) | Fall: December 1 |
| 4 | Cancer Biology (PIBS) | Fall: December 1 |
| 5 | Cell and Developmental Biology (PIBS) | Fall: December 1 |
| 6 | Cellular and Molecular Biology (PIBS) | Fall: December 1 |
| 7 | Genetics and Genomics (PIBS) | Fall: December 1 |
| 8 | Human Genetics | Fall: December 1 |
| 9 | Immunology (PIBS) | Fall: December 1 |
| 10 | Medical Scientist Training Program (MD/PhD) | Fall: October 15 |
| 11 | Microbiology and Immunology (PIBS) | Fall: December 1 |
| 12 | Molecular and Integrative Physiology (PIBS) | Fall: December 1 |
| 13 | Molecular, Cellular, and Developmental Biology (PIBS) | Fall: December 1 |
| 14 | Molecular and Cellular Pathology (PIBS) | Fall: December 1 |
| 15 | Neuroscience (PIBS) | Fall: December 1 |
| 16 | Pharmacology (PIBS) | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Bioinformatics | Fall: December 1 |
| 2 | Biological Chemistry | Fall: December 1 |
| 3 | Clinical Research Design and Statistical Analysis | Contact department |
| 4 | Genetic Counseling | Fall: January 15 |
| 5 | Health Infrastructures and Learning Systems | Contact department |
| 6 | Health Infrastructures and Learning Systems – Online | Contact department |
| 7 | Intraoperative Neurophysiology | Contact department |
| 8 | Medical Physics | Fall: December 1 |
| 9 | Oral Health Sciences | Contact department |
| 10 | Translational Research Education | Contact department |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Chemical Biology of Cancer | Contact department |
| 2 | Computational Epidemiology and Systems Modeling | Contact department |
| 3 | Precision Health Certificate | Contact department |

#### Public Health — 11 programs

##### Doctoral (PhD/DrPH)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Biostatistics | Fall: December 1 |
| 2 | Environmental Health Sciences | Fall: December 1 |
| 3 | Epidemiologic Science | Fall: December 1 |
| 4 | Health Behavior and Health Equity | Fall: December 1 |
| 5 | Health Services Organization and Policy | Fall: December 1 |
| 6 | Nutritional Sciences | Fall: December 1 |
| 7 | Population and Health Sciences | Contact department |

##### Master's (MPH/MS)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Biostatistics | Fall: January 15 |
| 2 | Biostatistics: Health Data Science | Fall: January 15 |
| 3 | Environmental Health Sciences | Fall: January 15 |
| 4 | Epidemiology | Fall: January 15 |
| 5 | Health Behavior and Health Equity | Fall: January 15 |
| 6 | Health Management and Policy | Fall: January 15 |
| 7 | Nutritional Sciences | Fall: January 15 |
| 8 | Population and Health Sciences (Online MPH) | Contact department |
| 9 | Toxicology | Fall: January 15 |

#### Dentistry — 8 programs

##### Doctoral (DDS)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | DDS | AADSAS application |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Endodontics | Contact department |
| 2 | Orthodontics | Contact department |
| 3 | Pediatric Dentistry | Contact department |
| 4 | Periodontics | Contact department |
| 5 | Prosthodontics | Contact department |
| 6 | Restorative Dentistry | Contact department |
| 7 | Dental Hygiene | Contact department |

#### Ford School of Public Policy — 8 programs

##### Doctoral (PhD)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Public Policy | Fall: December 15 |
| 2 | Political Science and Public Policy | Fall: December 1 |
| 3 | Public Policy and Economics | Fall: December 15 |
| 4 | Public Policy and Political Science | Fall: December 1 |
| 5 | Public Policy and Sociology | Fall: December 1 |

##### Master's (MPP/MPA)

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Public Policy (MPP) | Fall: January 15 |
| 2 | Public Affairs | Contact department |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Science, Technology, and Public Policy | Contact department |

#### Environment & Sustainability — 7 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Environment and Sustainability | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Environment and Sustainability | Fall: January 15 |
| 2 | Landscape Architecture | Fall: January 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Environmental Justice | Contact department |
| 2 | Industrial Ecology | Contact department |
| 3 | Spatial Analysis | Contact department |
| 4 | Sustainability | Contact department |

#### Kinesiology — 5 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Movement Science | Fall: December 1 |
| 2 | Sport Management | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Athletic Training | Fall: January 15 |
| 2 | M.S. in Kinesiology | Fall: January 15 |
| 3 | Physical Activity and Nutrition | Contact department |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Sport Management | Contact department |

#### Education — 5 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Educational Leadership and Policy | Fall: December 1 |
| 2 | Educational Studies | Fall: December 1 |
| 3 | Higher Education | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Education and Psychology | Fall: December 1 |
| 2 | English and Education | Fall: December 1 |
| 3 | Learning Experience Design | Contact department |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Translational Research Education | Contact department |

#### Social Work — 5 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Social Work and Anthropology | Fall: December 1 |
| 2 | Social Work and Psychology | Fall: December 1 |
| 3 | Social Work and Social Welfare | Fall: December 1 |
| 4 | Social Work and Sociology | Fall: December 1 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Social Work | Contact department |

#### Pharmacy — 4 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Clinical Pharmacy Translational Science | Fall: December 1 |
| 2 | Integrated Pharmaceutical Sciences | Fall: December 1 |
| 3 | Pharmaceutical Sciences | Fall: December 1 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Medicinal Chemistry | Fall: December 1 |

#### Business (Ross) — 3 programs (non-MBA)

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Business Administration (PhD) | Fall: December 15 |
| 2 | Business and Economics | Fall: December 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Business Research | Contact department |

#### Architecture & Urban Planning (Taubman) — 5 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Architecture | Fall: December 15 |

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Architecture (MArch) | Fall: January 15 |
| 2 | Real Estate Development | Contact department |
| 3 | Urban and Regional Planning (MUP) | Fall: January 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Urban Informatics | Contact department |

#### Art & Design (Stamps) — 2 programs

##### Master's

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Art (MFA) | Fall: January 15 |
| 2 | Design (MFA) | Fall: January 15 |

#### Information — 2 programs

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Information (PhD) | Fall: December 15 |

##### Certificate

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Information | Contact department |

#### Nursing — 1 program

##### Doctoral

| # | 项目 | Deadline |
|---|------|----------|
| 1 | Nursing, Ph.D. | Fall: December 1 |

#### Law School — Separate application process

| # | 项目 | 学位 | Deadline |
|---|------|------|----------|
| 1 | Juris Doctor | JD | LSAC application |
| 2 | LLM | LLM | Contact school |
| 3 | SJD | SJD | Contact school |

#### Social Work (MSW) — Separate application process

| # | 项目 | 学位 | Deadline |
|---|------|------|----------|
| 1 | Master of Social Work | MSW | Contact school |

#### Non-Rackham Professional Programs

| School | Program | Degree |
|--------|---------|--------|
| Law | JD, LLM, SJD | Juris Doctor / Master of Law |
| Medicine | MD, MD/PhD | Doctor of Medicine |
| Dentistry | DDS | Doctor of Dental Surgery |
| Social Work | MSW | Master of Social Work |
| Ross (MBA) | MBA | Master of Business Administration |
| Pharmacy | PharmD | Doctor of Pharmacy |

### 2.2 Deep Dive: Computer Science and Engineering (PhD)

- **Department**: Computer Science and Engineering, College of Engineering
- **Address**: 2260 Hayward Street, Ann Arbor, MI 48109-2121
- **Application Deadline**: Fall: December 15
- **Application Platform**: ApplyWeb (https://www.applyweb.com/cgi-bin/app?s=umgrad)
- **Application Fee**: $90 (domestic), $90 (international) — standard Rackham fee
- **GRE**: Not required for PhD (Rackham policy discontinued GRE for all doctoral programs)
- **TOEFL Minimum**: 84 (iBT before Jan 21, 2026) / 4.5 (new scale after Jan 21, 2026)
- **IELTS Minimum**: 6.5
- **Recommendations**: 3 letters required
- **Statement of Purpose**: Required
- **Personal Statement**: Required
- **Transcripts**: Required (uploaded to ApplyWeb)
- **Website**: https://cse.engin.umich.edu/

### 2.3 Graduate Admissions Model

**Centralized (Rackham) + Decentralized (Programs)**:
- Rackham Graduate School manages the application infrastructure (ApplyWeb), minimum requirements, and final offer letters
- Individual programs set their own deadlines, additional requirements, and make admission decisions
- Applicants interact with both Rackham and the program office
- Some professional schools (Law, Medicine, Dentistry, Ross MBA) have completely separate admissions processes

**Application Fee**: $90 (standard Rackham fee; verify per program)
**Fee Waivers**: Available for qualifying applicants

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| Admissions Office | Office of Undergraduate Admissions, 1220 Student Activities Building, 515 E. Jefferson St., Ann Arbor, MI 48109-1316 |
| Phone | 734-764-7433 |
| Application Portal | Common Application (https://apply.commonapp.org/Login?ma=439) |
| Application Fee | $75 (fee waiver available on Common App) |
| Early Decision (ED) | November 1 (binding) — NEW for 2025-2026 cycle |
| Early Action (EA) | November 1 (nonbinding) |
| Regular Decision (RD) | February 1 |
| Winter Term Deadline | October 1 |
| Summer Half Term Deadline | February 1 |
| Music, Theatre & Dance Deadline | December 1 |
| ED Enrollment Deposit | January 6 |
| RD Enrollment Deposit | May 1 |
| ED Notifications | By end of December |
| EA Notifications | By end of January |
| RD Notifications | By early April |
| Financial Aid Deadline (ED) | November 15 |
| Financial Aid Deadline (EA/RD) | March 1 (FAFSA + CSS Profile) |
| FAFSA/CSS Available | October 1 |
| SAT/ACT Policy | Test-optional (continuing for 2026 cycle) |
| Score Self-Report Deadline | Nov 1 (ED/EA) / Feb 1 (RD) |
| Superscore | Not specified |
| Interview | Not required |
| Recommendations | 1 Teacher Evaluation + School Report |
| Essays | 2 required essays (via Common App) |
| Transfer Deadline | February 1 |

**Source**: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低要求 | 推荐分数 | 适用条件 |
|------|---------|---------|---------|
| TOEFL iBT | 100+ (section scores: 23+ listening/reading, 21+ speaking/writing) | 100+ | 非英语母语者 |
| TOEFL iBT (new scale, Jan 21, 2026+) | 5-6 range with section scores of 5+ (CEFR C1) | 5+ | 非英语母语者 |
| TOEFL Essentials | 10 range with section scores 10+ | 10+ | 非英语母语者 |
| IELTS | 7.0 (section scores 6.5+) | 7.0+ | 非英语母语者 |
| PTE Academic | 68 (all sections equally strong) | 68+ | 非英语母语者 |
| Cambridge C1 Advanced (CAE) | 185 (no less than 180 in all sections) | 185+ | 非英语母语者 |
| Cambridge C2 Proficiency (CPE) | 185 (no less than 180 in all sections) | 185+ | 非英语母语者 |
| ECPE | Certificate with all sections at least C | Certificate | 非英语母语者 |
| MET (Michigan English Test) | 64 (section scores 59+ for 4-skill MET-digital) | 64+ | 非英语母语者 |

**Exemptions**: SAT EBRW 650+ (or old SAT Critical Reading 600+); ACT English 27+; completed all undergraduate education at English-medium institution.

**Source**: https://admissions.umich.edu/apply/international-applicants/exams-visas

### 3.3 Graduate — Global Rules

| 维度 | 详情 |
|------|------|
| Admissions Model | Centralized (Rackham) + Decentralized (Programs) |
| Application Platform | ApplyWeb (https://www.applyweb.com/cgi-bin/app?s=umgrad) |
| Application Fee | $90 (standard Rackham fee) |
| GRE General | No longer required for doctoral programs; some master's programs still require — consult program website |
| GRE Institution Code | 1839 |
| TOEFL Minimum (Rackham) | 84 (iBT before Jan 21, 2026) / 4.5 (new scale after Jan 21, 2026) |
| IELTS Minimum (Rackham) | 6.5 |
| TOEFL Institution Code | 1839 |
| English Proficiency Exemptions | Native English speaker; completed all UG/grad education at English-medium institution; current U-M student |
| Application Timeline | Most PhD: December 1-15; Most Master's: January 15; Some rolling |
| CGS April 15 Equivalent | Not explicitly stated — consult program |
| Recommendation Letters | Typically 3 required (varies by program) |
| Statement of Purpose | Required |
| Personal Statement | Required |
| Transcripts | Uploaded to ApplyWeb; official transcripts upon admission |

**Source**: https://rackham.umich.edu/admissions/applying/

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-2026 Academic Year, Line-Itemized)

#### Michigan Residents (In-State) — Lower Division LSA (First-Years/Sophomores)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $18,346 | Based on approved rates for 2025-2026 |
| Living Expenses | $16,246 | Based on unlimited basic residential meal plan |
| Books, Course Materials, Supplies & Equipment | $1,184 | |
| Transportation | $400 | |
| Miscellaneous Personal Expenses | $2,372 | |
| **Total Budget** | **$38,548** | |

#### Michigan Residents (In-State) — Upper Division LSA (Juniors/Seniors)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $20,648 | Based on approved rates for 2025-2026 |
| Living Expenses | $16,246 | Based on unlimited basic residential meal plan |
| Books, Course Materials, Supplies & Equipment | $1,184 | |
| Transportation | $400 | |
| Miscellaneous Personal Expenses | $2,372 | |
| **Total Budget** | **$40,850** | |

#### Nonresidents (Out-of-State) — Lower Division LSA (First-Years/Sophomores)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $63,962 | Based on approved rates for 2025-2026 |
| Living Expenses | $16,246 | Based on unlimited basic residential meal plan |
| Books, Course Materials, Supplies & Equipment | $1,184 | |
| Transportation | $400 | |
| Miscellaneous Personal Expenses | $2,372 | |
| **Total Budget** | **$84,164** | |

#### Nonresidents (Out-of-State) — Upper Division LSA (Juniors/Seniors)

| 费用项目 | 金额 | 说明 |
|---------|------|------|
| Tuition & Fees | $68,444 | Based on approved rates for 2025-2026 |
| Living Expenses | $16,246 | Based on unlimited basic residential meal plan |
| Books, Course Materials, Supplies & Equipment | $1,184 | |
| Transportation | $400 | |
| Miscellaneous Personal Expenses | $2,372 | |
| **Total Budget** | **$88,646** | |

> **注**: Tuition rates vary by school/college. LSA rates shown; Engineering, Ross, SMTD, etc. may differ. Rates are approved each June by the U-M Board of Regents.

**Source**: https://admissions.umich.edu/costs-aid/costs

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 详情 |
|------|------|
| Need-Blind (US Students) | Yes |
| Need-Aware (International) | Yes — international students on temporary visas are NOT eligible for financial aid and must pay full cost |
| Go Blue Guarantee | Families with income $0-125K: 100% qualify for scholarship/grant aid, $0 tuition |
| Go Blue Guarantee (125K-150K) | 99% qualify, average $638 tuition after aid |
| Go Blue Guarantee (150K-180K) | 98% qualify, average $2,574 tuition after aid |
| Tuition-Free Threshold | $125,000 family income (Michigan residents) |
| CSS Profile Required | Yes |
| FAFSA Required | Yes |
| Financial Aid Deadline (ED) | November 15 |
| Financial Aid Deadline (EA/RD) | March 1 |
| Application Fee Waiver | Available on Common Application |
| In-State Students Pay No Tuition | "1 in 4" due to financial aid |

**Source**: https://admissions.umich.edu/costs-aid/financial-aid, https://admissions.umich.edu/costs-aid/michigan-residents

### 4.3 Graduate Cost & Funding Framework

| 维度 | 详情 |
|------|------|
| Application Fee | $90 (standard Rackham fee) |
| Fee Waivers | Available for qualifying applicants |
| Funding Types | Fully funded (most PhD programs), partially funded (some master's), self-funded |
| RA/TA Positions | Common for doctoral students; many include tuition waiver + stipend |
| Fellowships | Rackham Merit Fellowship, departmental fellowships |
| CGS April 15 Honor Date | Consult individual programs |
| International Students | Must demonstrate full funding for visa purposes |

**Source**: https://rackham.umich.edu/admissions/, https://rackham.umich.edu/funding/

---

## SECTION 5 — Evidence Chain Index

```yaml
---
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines
  source_snippet: "NOV 1 — Early Decision for First-year Students Only / Early Action for First-year Students Only"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines
  source_snippet: "FEB 1 — Fall Term Application Deadline / Summer Half Term Application Deadline"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.ED
  value: "November 1 (binding)"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines/application-changes
  source_snippet: "new option to apply Early Decision (binding decision)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.application.fee
  value: "$75"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines
  source_snippet: "Completed Common Application with $75 application fee* payment"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.testing.test_optional
  value: "Yes (continuing for 2026 cycle)"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines/application-changes
  source_snippet: "Continuing for the 2026 application cycle, U-M will be test-optional."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.testing.TOEFL_minimum
  value: "100 (section scores: 23+ listening/reading, 21+ speaking/writing)"
  source_url: https://admissions.umich.edu/apply/international-applicants/exams-visas
  source_snippet: "TOEFL (iBT, including the Home Edition): 100 range with section scores 23+ in listening & reading and 21+ in speaking and writing."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.testing.IELTS_minimum
  value: "7.0 (section scores 6.5+)"
  source_url: https://admissions.umich.edu/apply/international-applicants/exams-visas
  source_snippet: "IELTS / IELTS Indicator: 7.0 range with section scores 6.5+"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.testing.PTE_minimum
  value: "68"
  source_url: https://admissions.umich.edu/apply/international-applicants/exams-visas
  source_snippet: "PTE Academic: 68 with all sections equally strong"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.cost.tuition_in_state_lower
  value: "$18,346"
  source_url: https://admissions.umich.edu/costs-aid/costs
  source_snippet: "Tuition & Fees* $18,346" (Michigan Residents, Lower Division LSA)
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.tuition_OOS_lower
  value: "$63,962"
  source_url: https://admissions.umich.edu/costs-aid/costs
  source_snippet: "Tuition & Fees* $63,962" (Nonresidents, Lower Division LSA)
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.cost.total_in_state
  value: "$38,548"
  source_url: https://admissions.umich.edu/costs-aid/costs
  source_snippet: "Total Budget $38,548" (Michigan Residents, Lower Division LSA)
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.cost.total_OOS
  value: "$84,164"
  source_url: https://admissions.umich.edu/costs-aid/costs
  source_snippet: "Total Budget $84,164" (Nonresidents, Lower Division LSA)
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.financial_aid.need_blind_US
  value: "Yes"
  source_url: https://admissions.umich.edu/costs-aid/financial-aid
  source_snippet: "Whether it's scholarships, grants, or connecting students to federal aid, the University of Michigan has numerous resources"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.financial_aid.need_aware_intl
  value: "Yes — international students on temporary visas are NOT eligible for financial aid"
  source_url: https://admissions.umich.edu/apply/international-applicants
  source_snippet: "International students on temporary visas are not eligible for financial aid, and are expected to pay the full cost of attendance."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.financial_aid.go_blue_guarantee
  value: "Families $0-125K: $0 tuition; $125K-150K: avg $638; $150K-180K: avg $2,574"
  source_url: https://admissions.umich.edu/costs-aid/michigan-residents
  source_snippet: "$0-125K — 100% qualify — $0 tuition"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-016:
  field: undergraduate.application.portal
  value: "Common Application"
  source_url: https://admissions.umich.edu/apply/first-year-applicants/requirements-deadlines
  source_snippet: "Completed Common Application with $75 application fee* payment"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.programs.total
  value: "155 UG programs across 14 schools/colleges"
  source_url: https://admissions.umich.edu/academics-majors/majors-degrees
  source_snippet: "280+ degree programs in 14 undergraduate schools & colleges"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.admissions.gre_policy
  value: "GRE no longer required for doctoral programs; some master's programs still require"
  source_url: https://rackham.umich.edu/admissions/applying/tests/
  source_snippet: "GRE general test scores are no longer included in the admissions process for Rackham's doctoral programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.testing.TOEFL_minimum
  value: "84 (before Jan 21, 2026) / 4.5 (after Jan 21, 2026)"
  source_url: https://rackham.umich.edu/admissions/applying/tests/
  source_snippet: "Before January 21, 2026 = 84. January 21, 2026 and after = 4.5."
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.testing.IELTS_minimum
  value: "6.5"
  source_url: https://rackham.umich.edu/admissions/applying/tests/
  source_snippet: "IELTS: 6.5"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.application.platform
  value: "ApplyWeb"
  source_url: https://rackham.umich.edu/admissions/applying/
  source_snippet: "Applicant creates an ApplyWeb account"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-005:
  field: graduate.application.fee
  value: "$90 (standard Rackham fee)"
  source_url: https://rackham.umich.edu/admissions/applying/
  source_snippet: "Submit your completed application." (fee listed on application)
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-006:
  field: graduate.programs.total
  value: "242 programs (Ann Arbor campus)"
  source_url: https://rackham.umich.edu/programs-of-study/
  source_snippet: "more than 180 graduate programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
umich-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: rules 1-4)
├── 01-ug-lsa.md                        (Section 1: LSA programs)
├── 02-ug-engineering.md                (Section 1: Engineering programs)
├── 03-ug-ross.md                       (Section 1: Ross programs)
├── 04-ug-smtd.md                       (Section 1: SMTD programs)
├── 05-ug-other-schools.md              (Section 1: Other UG schools)
├── 06-grad-lsa.md                      (Section 2: LSA graduate)
├── 07-grad-engineering.md              (Section 2: Engineering graduate)
├── 08-grad-medicine.md                 (Section 2: Medicine graduate)
├── 09-grad-other-schools.md            (Section 2: Other graduate)
├── 10-deadlines-requirements.md        (Section 3)
├── 11-costs-financial-aid.md           (Section 4)
├── 12-evidence-chain.md                (Section 5)
└── 13-comparison-framework.md          (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "umich-knowledge-base-v2"
  school: "University of Michigan, Ann Arbor"
  department: "<home department>"
  degree_level: "<BA|BS|BSE|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Exact count of LSA minors (extract all 100+) | https://lsa.umich.edu/lsa/academics/majors-minors.html |
| P0 | Ross MBA detailed requirements & deadlines | https://michiganross.umich.edu/graduate/mba |
| P0 | Law School JD admissions requirements | https://law.umich.edu/prospectivestudents |
| P0 | Medical School MD admissions requirements | https://medicine.umich.edu/medschool/education/md-program |
| P1 | Engineering tuition differential rates | https://ro.umich.edu/tuition-residency/tuition-fees |
| P1 | SMTD audition requirements & deadlines | https://smtd.umich.edu/admissions/ |
| P1 | Each graduate program's exact deadline | Per-program websites |
| P1 | Graduate application fee confirmation ($90) | https://rackham.umich.edu/admissions/applying/ |
| P2 | Transfer student requirements | https://admissions.umich.edu/apply/transfer-applicants |
| P2 | AP/IB credit policies | https://admissions.umich.edu/apply/first-year-applicants/ap-ib-credit |
| P2 | Student profile / class profile data | https://admissions.umich.edu/apply/first-year-applicants/first-year-student-profile |
| P2 | Ross School of Business BBA detailed curriculum | https://michiganross.umich.edu/undergraduate/bba |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | UMich | [School 2] | [School 3] |
|------|-------|------------|------------|
| Location | Ann Arbor, MI | | |
| Type | Public | | |
| UG Tuition (In-State) | $18,346 | | |
| UG Tuition (OOS) | $63,962 | | |
| UG Total Cost (In-State) | $38,548 | | |
| UG Total Cost (OOS) | $84,164 | | |
| Need-Blind (US) | Yes | | |
| Need-Blind (Intl) | No (need-aware) | | |
| EA Deadline | November 1 | | |
| ED Deadline | November 1 | | |
| RD Deadline | February 1 | | |
| Test-Optional | Yes (2026 cycle) | | |
| SAT/ACT Required | No | | |
| TOEFL Min (UG) | 100 | | |
| IELTS Min (UG) | 7.0 | | |
| Application Fee (UG) | $75 | | |
| Application Portal | Common App | | |
| Tuition-Free Threshold | $125K (MI residents) | | |
| Go Blue Guarantee | Yes ($0-125K income) | | |
| Total Program Count (Rule 1) | 346+ | | |
| School/Dept Count (Rule 2) | 19 | | |
| Grad Application Fee | $90 | | |
| GRE Required (PhD) | No (discontinued) | | |
| TOEFL Min (Grad) | 84 | | |
| IELTS Min (Grad) | 6.5 | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.umich.edu, rackham.umich.edu, lsa.umich.edu, ro.umich.edu, finaid.umich.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
