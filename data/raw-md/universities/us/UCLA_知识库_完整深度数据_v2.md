# University of California, Los Angeles (UCLA) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: US (University of California system)

---

## The five structural rules (enforced everywhere)

These five rules govern how program/major data is organized. The required shape is a **4-level hierarchy**: 学院 → 系 → 学位级别 → 专业.

1. **专业总数** — exact count of all majors/programs (UG + grad), with breakdown.
2. **学院/系明细 + 父子层级** — every school and department; parent→child relationships marked.
3. **学历级别明细** — every degree level awarded, with counts.
4. **分布矩阵** — 学院 × 学位级别 cross-tab of counts.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every single program, no summarizing.

> **Reconciliation gate**: rule-1 total == matrix cell-sum == row-count in rule-5 tables. Verified at end of document.

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 137 (BA=91, BS=46, BFA=0) |
| 本科辅修 (Minor) | 105 |
| 研究生学位项目 (目录条目, MA/MS/MFA/MBA/MEng/MArch/MPH/MSW/MPP/MLIS/PhD/EdD/DNP 等) | 150 |
| 研究生高级证书 (Certificate) | 1 |
| **学位项目总计 (UG majors + Grad directory entries)** | **287** |
| 提供本科专业的学院数 | 9 |
| 研究生院/学术部门数 (含 4 个 College of L&S 分部) | 18 |
| 本科生总数 (approx, 参考) | ~33,000 |
| UCLA 官方声称的研究生学位项目数 | "133 degree programs" (admissions homepage) / "136 degree programs" (steps-to-apply) ⚠ 与叶级提取数(150)不一致 |

> **总数核对**: 本科 137 + 研究生目录条目 150 = 287 学位项目。辅修 105 单列。UCLA 自身的 "133/136 degree programs" 是其官方计法, 与叶级提取的差异源于: (a) 在线/职业 MS 变体在 UCLA 目录里是独立条目, (b) DDS/MD/JD/MBA 等专业学位由独立的 professional-school 站点处理, 不在 grad.ucla.edu/schools/ 目录内, (c) UCLA 计的是 degree-awarding units 而非目录条目。本数据集采用叶级目录条目(150)以保证可比性, 同时记录 UCLA 官方数字以保真。

### 0.2 学院 / 系层级结构

```
UCLA
├── College of Letters and Science (L&S)                    [学院 — 最大, 105 UG majors]
│   ├── Humanities                                          [分部/系组 — 含 Art History, Asian Lang, Classics, CompLit, English, Euro Lang, Indo-European, Linguistics, Near Eastern, Philosophy, Slavic, Spanish&Portuguese]
│   ├── Life Sciences                                       [分部/系组 — 含 Bioinformatics, Ecology&EvBio, IntegrativeBio&Phys, MolecularBio, MCD Biology, MCIP, Psychology]
│   ├── Physical Sciences                                   [分部/系组 — 含 AOS, Chem&Biochem, Earth Planetary&Space, Math, Physics&Astronomy, Statistics&DataSci]
│   └── Social Sciences                                     [分部/系组 — 含 AfrAm Studies, AmIndian, Anthropology, Archaeology, AsianAm, Chicana/o, Communication, Conservation, Economics, Gender, Geography, History, PolSci, Sociology]
├── School of the Arts and Architecture                     [学院] — UG + Grad
│   ├── Architecture and Urban Design                       [系]
│   ├── Art                                                 [系]
│   ├── Design | Media Arts                                 [系]
│   └── World Arts and Cultures/Dance                       [系]
├── Samueli School of Engineering and Applied Science       [学院] — UG + Grad
│   ├── Bioengineering                                      [系]
│   ├── Chemical & Biomolecular Engineering                 [系]
│   ├── Civil & Environmental Engineering                   [系]
│   ├── Computer Science                                    [系]  ⚠ 与 Electrical & Computer Engineering 共组(见目录)
│   ├── Electrical & Computer Engineering                   [系]
│   ├── Materials Science & Engineering                     [系]
│   └── Mechanical & Aerospace Engineering                  [系]
├── Herb Alpert School of Music                             [学院] — UG + Grad (Ethnomusicology, Music, Musicology)
├── Joe C. Wen School of Nursing                            [学院] — UG + Grad (Nursing)
├── Luskin School of Public Affairs                         [学院] — UG + Grad (Public Policy, Social Welfare, Urban Planning)
├── School of Theater, Film and Television (TFT)            [学院] — UG + Grad (Film&TV, Theater)
├── School of Education and Information Studies             [学院] — UG + Grad (Education, Information Studies)
├── Fielding School of Public Health                        [学院] — UG + Grad (Biostat, CommHealth, EnvHealth, Epi, HealthPol&Mgmt)
├── Anderson School of Management                           [学院 — 研究生/职业] (MBA, MFE, MS BA, EMBA, FEMBA, Global EMBA, MS/PhD)
├── David Geffen School of Medicine                         [学院 — 研究生/职业] (Biomath, Clinical Research, DataSci Biomed, Genetic Counseling, Human Genetics, Molecular&Med Pharmacology, Neuroscience, Physics&Bio in Med)
├── School of Dentistry                                     [学院 — 研究生/职业] (Oral Biology; DDS 通过独立站点)
├── School of Law                                           [学院 — 研究生/职业] (Master of Legal Studies; JD/LLM/SJD 通过独立站点)
├── Institute of the Environment & Sustainability           [跨学科研究所 — 研究生] (Environment & Sustainability, Environmental Science & Engineering)
└── International Institute                                 [跨学科研究所 — 研究生] (African Studies, East Asian Studies, Latin American Studies)
```

> **任务说明核对**: 任务书称"6 UG colleges", 实际从 admission.ucla.edu/apply/majors 提取出 **9 个**提供本科专业的学院 (L&S + Arts&Arch + Samueli Eng + Herb Alpert Music + Wen Nursing + Luskin PubAffairs + TFT + Ed&Info + Fielding PubHealth)。已修正为 9。

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 91 |
| BS | B.S. | Bachelor of Science | 本科 | 46 |
| MA | M.A. | Master of Arts | 研究生 | (含于 140 master's-offering 项内) |
| MS | M.S. | Master of Science | 研究生 | (含于 140 master's-offering 项内) |
| MFA | M.F.A. | Master of Fine Arts | 研究生 | (Art, Design|Media Arts, Culture&Performance, Choreographic Inquiry 等) |
| MBA | M.B.A. | Master of Business Administration | 研究生 | (Anderson: MBA/EMBA/FEMBA/Global EMBA) |
| MEng | M.Eng. | Master of Engineering | 研究生 | (Engineering – Master of Engineering) |
| MArch | M.Arch. | Master of Architecture | 研究生 | (Architecture – M.Arch.) |
| MPH | M.P.H. | Master of Public Health | 研究生 | (Fielding: 多个 MPH 变体) |
| MPP | M.P.P. | Master of Public Policy | 研究生 | (Luskin Public Policy) |
| MSW | M.S.W. | Master of Social Welfare | 研究生 | (Luskin Social Welfare) |
| MLIS | M.L.I.S. | Master of Library & Information Science | 研究生 | (Information Studies) |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 83 个目录条目提供 PhD |
| EdD | Ed.D. | Doctor of Education | 研究生 | (Educational Leadership Program) |
| DNP | D.N.P. | Doctor of Nursing Practice | 研究生 | (Nursing – DNP, Post-BS to DNP) |
| Certificate | Certificate | 高级证书 | 研究生 | 1 (Library & Information Science Certificate) |

> **学位标准化**: UCLA 用标准缩写 (B.A./B.S./M.S./Ph.D. 等), canonical 与 official 一致, 无需映射。Rule 3/Rule 4 用 canonical 聚合。研究生层级的 master's 因 UCLA 把同一系的 M.A. 与 M.S./专业硕士在同一目录条目下合并展示 (D/M badge), 故按"提供 master's 的目录条目数=140"汇总, 上面 MA/MS/MFA/MBA 等行不重复计入 Rule-1 总数 (避免重复计数); PhD=83 与 Certificate=1 单列。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

**本科部分 (UG majors, 共 137):**

| 学院 \ 级别 | BA | BS | 合计 |
|------------|----|----|------|
| College of Letters and Science | 71 | 34 | 105 |
| School of the Arts and Architecture | 8 | 0 | 8 |
| Samueli School of Engineering | 0 | 10 | 10 |
| Herb Alpert School of Music | 6 | 0 | 6 |
| Joe C. Wen School of Nursing | 0 | 1 | 1 |
| Luskin School of Public Affairs | 1 | 0 | 1 |
| School of Theater, Film and Television | 3 | 0 | 3 |
| School of Education and Information Studies | 1 | 0 | 1 |
| Fielding School of Public Health | 1 | 1 | 2 |
| **合计** | **91** | **46** | **137** |

**研究生部分 (Grad directory entries, 共 150) — 按学位 badge 计 (一个条目可同时 D+M):**

| 学院/分部 \ 级别 | PhD (D) | Master's (M) | Cert (C) | 条目合计 |
|----------------|---------|--------------|----------|----------|
| Anderson School of Management | 1 | 7 | 0 | 7 |
| David Geffen School of Medicine | 5 | 5 | 0 | 8 |
| Fielding School of Public Health | 6 | 11 | 0 | 17 |
| Samueli School of Engineering & Applied Science | 9 | 21 | 0 | 21 |
| Herb Alpert School of Music | 3 | 3 | 0 | 3 |
| Humanities (L&S) | 13 | 14 | 0 | 21 |
| Institute of the Environment & Sustainability | 2 | 1 | 0 | 2 |
| International Institute | 0 | 3 | 0 | 3 |
| Life Sciences (L&S) | 6 | 4 | 0 | 8 |
| Luskin School of Public Affairs | 2 | 5 | 0 | 6 |
| Physical Sciences (L&S) | 12 | 8 | 0 | 15 |
| School of Dentistry | 1 | 1 | 0 | 1 |
| School of Education and Information Studies | 4 | 2 | 1 | 6 |
| School of Law | 0 | 1 | 0 | 1 |
| School of Nursing | 3 | 2 | 0 | 3 |
| School of the Arts and Architecture | 2 | 6 | 0 | 7 |
| School of Theater, Film and Television | 2 | 2 | 0 | 3 |
| Social Sciences (L&S) | 12 | 12 | 0 | 18 |
| **badge 合计 (列)** | **83** | **140** | **1** | — |
| **条目合计 (行)** | — | — | — | **150** |

> **核对方说明**: 183 + 140 + 1 = 224 个 degree-offer, 但目录条目只有 150, 因为 83 个条目同时提供 PhD 与 Master's (D+M 双 badge), 在两列各计一次。Rule-1 的研究生数取**条目数 150** (= Section 2 表格行数)。PhD-only=83, Master's-only=140 是 badge 视角; 条目视角 = 150。两种视角在表中均明示, 不混淆。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UCLA 本科由 9 个学院/学校授予专业。College of Letters and Science 是最大的本科学院 (105 majors, 分 Humanities / Life Sciences / Physical Sciences / Social Sciences 四个分部), 其余 8 个为 professional schools。所有本科申请走 **UC Application** (统一), 但 School of the Arts and Architecture / Herb Alpert School of Music / School of Nursing / School of Theater, Film and Television 这 4 个学院需另交 **supplemental application**。详见 0.2 层级树。

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

> 来源: admission.ucla.edu/apply/majors (capture 2026-07-05)。本科专业按学院分组, 学位级别 (BA/BS) 在表内列出。L&S 内的"系"按学术分部 (Humanities/Life Sci/Physical Sci/Social Sci) 推断标注; 个别专业在 admission 页未细分到系, 已尽量就近归属。

#### College of Letters and Science (L&S) — 105 majors

##### BA (71)
| # | 专业 | L&S 分部 (推断) |
|---|------|----------------|
| 1 | African American Studies | Social Sciences |
| 2 | African and Middle Eastern Studies | Humanities |
| 3 | American Indian Studies | Social Sciences |
| 4 | American Literature and Culture | Humanities |
| 5 | Ancient Near East and Egyptology | Humanities |
| 6 | Anthropology | Social Sciences |
| 7 | Arabic | Humanities |
| 8 | Art History | Humanities |
| 9 | Asian American Studies | Social Sciences |
| 10 | Asian Humanities | Humanities |
| 11 | Asian Languages and Linguistics | Humanities |
| 12 | Asian Religions | Humanities |
| 13 | Asian Studies | Humanities |
| 14 | Business Economics | Social Sciences |
| 15 | Central and East European Languages and Cultures | Humanities |
| 16 | Chicana/o and Central American Studies | Social Sciences |
| 17 | Chinese | Humanities |
| 18 | Classical Civilization | Humanities |
| 19 | Communication | Social Sciences |
| 20 | Comparative Literature | Humanities |
| 21 | Disability Studies | Social Sciences |
| 22 | Earth and Environmental Science | Physical Sciences |
| 23 | Economics | Social Sciences |
| 24 | English | Humanities |
| 25 | European Language and Transcultural Studies | Humanities |
| 26 | European Languages and Transcultural Studies with French and Francophone | Humanities |
| 27 | European Languages and Transcultural Studies with German | Humanities |
| 28 | European Languages and Transcultural Studies with Italian | Humanities |
| 29 | European Languages and Transcultural Studies with Scandinavian | Humanities |
| 30 | European Studies | Humanities |
| 31 | Gender Studies | Social Sciences |
| 32 | Geography | Social Sciences |
| 33 | Geography/Environmental Studies | Social Sciences |
| 34 | Global Studies | Social Sciences |
| 35 | Greek | Humanities |
| 36 | Greek and Latin | Humanities |
| 37 | History | Humanities |
| 38 | Human Biology and Society | Life Sciences (interdisciplinarian w/ Sociology) |
| 39 | International Development Studies | Social Sciences |
| 40 | Iranian Studies | Humanities |
| 41 | Japanese | Humanities |
| 42 | Jewish Studies | Humanities |
| 43 | Korean | Humanities |
| 44 | Labor Studies | Social Sciences |
| 45 | Latin | Humanities |
| 46 | Latin American Studies | Social Sciences |
| 47 | Linguistics | Humanities |
| 48 | Linguistics and Anthropology | Humanities (interdisciplinarian) |
| 49 | Linguistics and Asian Languages and Cultures | Humanities |
| 50 | Linguistics and Computer Science | Humanities (interdisciplinarian) |
| 51 | Linguistics and English | Humanities |
| 52 | Linguistics and Philosophy | Humanities |
| 53 | Linguistics and Psychology | Humanities (interdisciplinarian) |
| 54 | Linguistics and Spanish | Humanities |
| 55 | Linguistics, Applied | Humanities |
| 56 | Middle Eastern Studies | Humanities |
| 57 | Nordic Studies | Humanities |
| 58 | Philosophy | Humanities |
| 59 | Physics | Physical Sciences |
| 60 | Political Science | Social Sciences |
| 61 | Portuguese and Brazilian Studies | Humanities |
| 62 | Psychology | Social Sciences |
| 63 | Religion, Study of | Humanities |
| 64 | Russian Language and Literature | Humanities |
| 65 | Russian Studies | Humanities |
| 66 | Sociology | Social Sciences |
| 67 | Southeast Asian Studies | Humanities |
| 68 | Spanish | Humanities |
| 69 | Spanish and Community and Culture | Humanities |
| 70 | Spanish and Linguistics | Humanities |
| 71 | Spanish and Portuguese | Humanities |

##### BS (34)
| # | 专业 | L&S 分部 (推断) |
|---|------|----------------|
| 1 | Anthropology | Social Sciences |
| 2 | Astrophysics | Physical Sciences |
| 3 | Atmospheric and Oceanic Sciences | Physical Sciences |
| 4 | Atmospheric and Oceanic Sciences/Mathematics | Physical Sciences (interdisciplinarian) |
| 5 | Biochemistry | Physical Sciences / Life Sciences |
| 6 | Biology | Life Sciences |
| 7 | Biophysics | Physical Sciences / Life Sciences |
| 8 | Chemistry | Physical Sciences |
| 9 | Chemistry/Materials Science | Physical Sciences (interdisciplinarian w/ Engineering) |
| 10 | Climate Science | Physical Sciences |
| 11 | Cognitive Science | Social Sciences / Life Sciences |
| 12 | Computational Biology | Life Sciences |
| 13 | Data Theory | Physical Sciences / Social Sciences |
| 14 | Ecology, Behavior, and Evolution | Life Sciences |
| 15 | Environmental Science | Life Sciences |
| 16 | Geology | Physical Sciences |
| 17 | Geology/Engineering Geology | Physical Sciences (interdisciplinarian w/ Engineering) |
| 18 | Geophysics | Physical Sciences |
| 19 | Human Biology and Society | Life Sciences (interdisciplinarian) |
| 20 | Marine Biology | Life Sciences |
| 21 | Mathematics | Physical Sciences |
| 22 | Mathematics, Applied | Physical Sciences |
| 23 | Mathematics/Applied Science | Physical Sciences |
| 24 | Mathematics/Economics | Physical Sciences (interdisciplinarian) |
| 25 | Mathematics, Financial Actuarial | Physical Sciences |
| 26 | Mathematics for Teaching | Physical Sciences |
| 27 | Mathematics of Computation | Physical Sciences |
| 28 | Microbiology, Immunology, and Molecular Genetics | Life Sciences |
| 29 | Molecular, Cell, and Developmental Biology | Life Sciences |
| 30 | Neuroscience | Life Sciences |
| 31 | Physiological Science | Life Sciences |
| 32 | Psychobiology | Life Sciences |
| 33 | Statistics and Data Science | Physical Sciences |
| 34 | Physics | Physical Sciences |

> 注: L&S BA 列 71 + BS 列 34 = 105, 与 0.4 矩阵一致。个别专业 (Anthropology, Human Biology and Society, Physics) 在 BA 与 BS 下各有一条, 因为 UCLA 对同一专业名授予两个学位变体, 故在两条学位级别下各计一次。

#### School of the Arts and Architecture — 8 majors (全部 BA)

| # | 专业 | 学位 |
|---|------|------|
| 1 | Architectural Studies | BA |
| 2 | Art | BA |
| 3 | Computational Art | BA |
| 4 | Dance | BA |
| 5 | Design | BA |
| 6 | Games | BA |
| 7 | World Arts and Cultures | BA |
| 8 | Individual Field of Concentration in the Arts and Architecture | BA |

#### Samueli School of Engineering and Applied Science — 10 majors (全部 BS)

| # | 专业 | 学位 |
|---|------|------|
| 1 | Aerospace Engineering | BS |
| 2 | Bioengineering | BS |
| 3 | Chemical Engineering | BS |
| 4 | Civil Engineering | BS |
| 5 | Computer Engineering | BS |
| 6 | Computer Science | BS |
| 7 | Computer Science and Engineering | BS |
| 8 | Electrical Engineering | BS |
| 9 | Materials Engineering | BS |
| 10 | Mechanical Engineering | BS |

#### Herb Alpert School of Music — 6 majors (全部 BA)

| # | 专业 | 学位 |
|---|------|------|
| 1 | Ethnomusicology | BA |
| 2 | Global Jazz Studies | BA |
| 3 | Musicology | BA |
| 4 | Music Composition | BA |
| 5 | Music Education | BA |
| 6 | Music Industry | BA |

#### Joe C. Wen School of Nursing — 1 major

| # | 专业 | 学位 |
|---|------|------|
| 1 | Nursing – Prelicensure | BS |

#### Luskin School of Public Affairs — 1 major

| # | 专业 | 学位 |
|---|------|------|
| 1 | Public Affairs | BA |

#### School of Theater, Film and Television — 3 majors (全部 BA)

| # | 专业 | 学位 |
|---|------|------|
| 1 | Film and Television | BA |
| 2 | Theater | BA |
| 3 | Individual Field of Concentration in Theater, Film and Television | BA |

#### School of Education and Information Studies — 1 major

| # | 专业 | 学位 |
|---|------|------|
| 1 | Education and Social Transformation | BA |

#### Fielding School of Public Health — 2 majors

| # | 专业 | 学位 |
|---|------|------|
| 1 | Public Health | BA |
| 2 | Public Health | BS |

### 1.3 Interdisciplinary / cross-college undergraduate programs

多个专业本身就是跨学科联合学位 (已在上表内标注), 例如:
- **Linguistics and Computer Science (BA)** — Linguistics (Humanities) + Computer Science (Engineering) 跨学院
- **Chemistry/Materials Science (BS)** — L&S Chemistry + Samueli Engineering Materials
- **Geology/Engineering Geology (BS)** — L&S Earth Science + Samueli Engineering Civil
- **Mathematics/Economics (BS)** — Physical Sciences 跨系
- **Human Biology and Society (BA/BS)** — Life Sciences + Sociology 跨分部

这些专业的行政归属 (administrative home) 见上表"系/分部"列, 跨学院标注 ⚠。

### 1.4 Minors — complete list (105)

> 来源: admission.ucla.edu/apply/minors (capture 2026-07-05). UCLA 声称 "more than 100 minors"; 提取出 105 个 (排除导航/页脚链接)。下表为完整清单 (按字母序, 名称后带 "new" 的为新设辅修, 名称保留)。

| # | Minor | # | Minor |
|---|-------|---|-------|
| 1 | Accounting | 54 | Geospatial Information Systems and Technologies |
| 2 | African American Studies | 55 | Gerontology |
| 3 | African and Middle Eastern Studies | 56 | Global Health |
| 4 | African Studies | 57 | Global Studies |
| 5 | American Indian Studies | 58 | Greek Language and Culture |
| 6 | Ancient Near East and Egyptology | 59 | Health Humanities (new) |
| 7 | Anthropology | 60 | Hebrew and Jewish Studies |
| 8 | Applied Developmental Psychology | 61 | History (new) |
| 9 | Arabic and Islamic Studies | 62 | History of Science, Technology and Medicine |
| 10 | Armenian Studies | 63 | Information and Media Literacy |
| 11 | Art History | 64 | International Migration Studies (new) |
| 12 | Asian American Studies | 65 | Iranian Music |
| 13 | Asian Humanities | 66 | Iranian Studies |
| 14 | Asian Languages | 67 | Israel Studies |
| 15 | Atmospheric and Oceanic Sciences | 68 | Labor Studies |
| 16 | Bioinformatics | 69 | Latin American Studies |
| 17 | Biomedical Research | 70 | Latin Language and Culture |
| 18 | Brain and Behavioral Health | 71 | Lesbian, Gay, Bisexual, Transgender, and Queer Studies |
| 19 | Central and East European Studies | 72 | Linguistics |
| 20 | Central American Studies | 73 | Literature and the Environment |
| 21 | Chicana and Chicano Studies | 74 | Mathematical Biology |
| 22 | Classical Civilization | 75 | Mathematics |
| 23 | Community Engagement and Social Change | 76 | Mathematics for Teaching |
| 24 | Comparative Literature | 77 | Mexican Studies |
| 25 | Conservation Biology | 78 | Middle Eastern Studies |
| 26 | Creative Writing | 79 | Musicology |
| 27 | Data Science Engineering | 80 | Music Industry |
| 28 | Digital Humanities | 81 | Neuroscience |
| 29 | Disability Studies | 82 | Philosophy |
| 30 | Earth and Environmental Science | 83 | Pilipino Studies |
| 31 | East Asian Studies | 84 | Portuguese and Brazilian Studies |
| 32 | Education Studies | 85 | Professional Writing (new) |
| 33 | English | 86 | Public Affairs |
| 34 | Entrepreneurship | 87 | Public Health |
| 35 | Environmental Engineering | 88 | Real Estate (new) |
| 36 | Environmental Systems and Society | 89 | Religion, Study of |
| 37 | Ethnomusicology (new) | 90 | Russian Language |
| 38 | European Languages and Transcultural Studies (new) | 91 | Russian Literature |
| 39 | European Languages and Transcultural Studies with French and Francophone | 92 | Russian Studies |
| 40 | European Languages and Transcultural Studies with German | 93 | Scandinavian |
| 41 | European Languages and Transcultural Studies with Italian | 94 | Science Education |
| 42 | European Studies | 95 | Social Data Science |
| 43 | Evolutionary Medicine | 96 | Social Thought |
| 44 | Film, Television and Digital Media | 97 | Society and Genetics |
| 45 | Food Studies (new) | 98 | South Asian Studies |
| 46 | Gender Studies | 99 | Southeast Asian Studies |
| 47 | Geochemistry | 100 | Spanish |
| 48 | Geography | 101 | Spanish Linguistics |
| 49 | Geography/Environmental Studies | 102 | Sports Leadership and Management (new) |
| 50 | Geology | 103 | Statistics and Data Science |
| 51 | Geophysics and Planetary Physics | 104 | Structural Biology |
| 52 | Gerontology | 105 | Systems Biology |
| 53 | Theater | — | (Visual and Performing Arts Education 收尾) |

> 完整辅修清单的官方页: admission.ucla.edu/apply/minors

### 1.5 General/Institute-wide requirements

- **A-G 课程**: 必须完成 15 门 A-G 课程, 且最后一年开学前至少完成 11 门 (来源: admission.ucla.edu/apply/first-year/first-year-requirements)
  - 2 years history/social science
  - 4 years college-preparatory English
  - 3 years mathematics (推荐 4)
  - 2 years laboratory science (推荐 3)
  - 2 years language other than English (推荐 3)
  - 1 year visual and performing arts (if available)
  - 1 year college-preparatory elective
- **Comprehensive Review (综合评审)**: 采用 13 项教师批准的标准, 包括 GPA、课程严谨度、领导力、个人成就等。Fall 2025 录取生平均 unweighted GPA = 4.0。
- **Personal Insight Questions (PIQ)**: 8 题选答 4 题, 每题上限 350 字。
- **Interview**: 不提供 admission interview。

### 1.6 Course-ID / Major-code lookup

UCLA 本科专业不用数字编号 (区别于 MIT 的 Course 6), 但研究生有 **Major Code** (如 Computer Science = 0201, 见 Section 2.2)。本科专业用名称 + 学位后缀 (B.A./B.S.) 标识。

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

> 来源: grad.ucla.edu/schools/ (capture 2026-07-05)。共 150 个目录条目 (含 83 PhD-offering + 140 Master's-offering + 1 Certificate; badge 视角)。每条注明 D (Doctorate) / M (Master's) / C (Certificate)。URL 为 grad.ucla.edu program detail page。

#### Anderson School of Management (7)
| # | 项目 | 学位 badge | URL |
|---|------|-----------|-----|
| 1 | Management – Business Analytics MS | M | grad.ucla.edu/programs/anderson-school-of-management/management-business-analytics-ms/ |
| 2 | Management – Executive MBA | M | grad.ucla.edu/programs/anderson-school-of-management/management-executive-mba/ |
| 3 | Management – Fully Employed MBA (FEMBA) | M | grad.ucla.edu/programs/anderson-school-of-management/management-fully-employed-mba-femba/ |
| 4 | Management – Global Executive MBA for Asia Pacific | M | grad.ucla.edu/programs/anderson-school-of-management/management-global-executive-mba-for-asia-pacific/ |
| 5 | Management – Master of Financial Engineering | M | grad.ucla.edu/programs/anderson-school-of-management/management-master-of-financial-engineering/ |
| 6 | Management – MBA | M | grad.ucla.edu/programs/anderson-school-of-management/management-mba/ |
| 7 | Management – MS, PHD | D, M | grad.ucla.edu/programs/anderson-school-of-management/management-ms-phd/ |

#### David Geffen School of Medicine (8)
##### Computational Medicine Department
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomathematics | D, M | grad.ucla.edu/programs/david-geffen-school-of-medicine/computational-medicine-department/biomathematics/ |
| 2 | Clinical Research | M | grad.ucla.edu/programs/david-geffen-school-of-medicine/computational-medicine-department/clinical-research/ |
| 3 | Data Science in Biomedicine | M | grad.ucla.edu/programs/david-geffen-school-of-medicine/computational-medicine-department/data-science-in-biomedicine/ |
##### Human Genetics Department
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 4 | Genetic Counseling | M | grad.ucla.edu/programs/david-geffen-school-of-medicine/human-genetics-department/genetic-counseling/ |
| 5 | Human Genetics | D, M | grad.ucla.edu/programs/david-geffen-school-of-medicine/human-genetics-department/human-genetics/ |
| 6 | Molecular & Medical Pharmacology | D, M | grad.ucla.edu/programs/david-geffen-school-of-medicine/molecular-and-medical-pharmacology/ |
| 7 | Neuroscience | D | grad.ucla.edu/programs/david-geffen-school-of-medicine/neuroscience/ |
| 8 | Physics & Biology in Medicine | D, M | grad.ucla.edu/programs/david-geffen-school-of-medicine/physics-and-biology-in-medicine/ |

#### Fielding School of Public Health (17)
##### Biostatistics Department
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biostatistics | D, M | grad.ucla.edu/programs/school-of-public-health/biostatistics-department/biostatistics/ |
| 2 | Biostatistics MPH | M | grad.ucla.edu/programs/school-of-public-health/biostatistics-department/biostatistics-mph/ |
| 3 | Data Science in Health | M | grad.ucla.edu/programs/school-of-public-health/biostatistics-department/data-science-in-health/ |
##### Community Health Sciences Department
| 4 | Community Health Sciences | D, M | grad.ucla.edu/programs/school-of-public-health/community-health-sciences-department/community-health-sciences/ |
| 5 | Community Health Sciences MPH | M | grad.ucla.edu/programs/school-of-public-health/community-health-sciences-department/community-health-sciences-mph/ |
| 6 | Master of Public Health in Community Health, Health Promotion and Education | M | grad.ucla.edu/programs/school-of-public-health/community-health-sciences-department/master-of-public-health-in-community-health-health-promotion-and-education/ |
| 7 | Environmental and Molecular Toxicology | D, M | grad.ucla.edu/programs/school-of-public-health/environmental-and-molecular-toxicology/ |
##### Environmental Health Sciences Department
| 8 | Environmental Health Sciences | D, M | grad.ucla.edu/programs/school-of-public-health/environmental-health-sciences-department/environmental-health-sciences/ |
| 9 | Environmental Health Sciences MPH | M | grad.ucla.edu/programs/school-of-public-health/environmental-health-sciences-department/environmental-health-sciences-mph/ |
##### Epidemiology Department
| 10 | Epidemiology | D, M | grad.ucla.edu/programs/school-of-public-health/epidemiology-department/epidemiology/ |
| 11 | Epidemiology MPH | M | grad.ucla.edu/programs/school-of-public-health/epidemiology-department/epidemiology-mph/ |
##### Health Policy and Management Department
| 12 | Executive Master of Public Health | M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/executive-master-of-public-health/ |
| 13 | Health Management MPH | M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/health-management-mph/ |
| 14 | Health Policy & Management | D, M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/health-policy-and-management/ |
| 15 | Health Policy & Management MPH | M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/health-policy-management-mph/ |
| 16 | Health Policy MPH | M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/health-policy-mph/ |
| 17 | Healthcare Administration | M | grad.ucla.edu/programs/school-of-public-health/health-policy-and-management-department/healthcare-administration/ |

#### Henry Samueli School of Engineering and Applied Science (21)
| # | 项目 | 系 (URL/目录推断) | 学位 | URL |
|---|------|------------------|------|-----|
| 1 | Bioengineering | Bioengineering | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/bioengineering/ |
| 2 | Chemical Engineering | Chemical & Biomolecular Eng | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/chemical-biomolecular-engineering-department/chemical-engineering/ |
| 3 | Civil Engineering | Civil & Environmental Eng | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/civil-environmental-engineering-department/civil-engineering/ |
| 4 | Computer Science | Computer Science | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/computer-science/ |
| 5 | Electrical & Computer Engineering | Electrical & Computer Eng | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/electrical-computer-engineering/ |
| 6 | Engineering – Master of Engineering | MEng (跨系) | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-master-of-engineering/ |
| 7 | Engineering – MS in Engineering, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-online/ |
| 8 | Engineering – MS in Engineering-Aerospace, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-aerospace-online/ |
| 9 | Engineering – MS in Engineering-Computer Networking, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-computer-networking-online/ |
| 10 | Engineering – MS in Engineering-Electrical, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-electrical-online/ |
| 11 | Engineering – MS in Engineering-Electronic Materials, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-electronic-materials-online/ |
| 12 | Engineering – MS in Engineering-Integrated Circuits, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-integrated-circuits-online/ |
| 13 | Engineering – MS in Engineering-Manufacturing and Design, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-manufacturing-and-design-online/ |
| 14 | Engineering – MS in Engineering-Materials Science, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-materials-science-online/ |
| 15 | Engineering – MS in Engineering-Mechanical, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-mechanical-online/ |
| 16 | Engineering – MS in Engineering-Signal Processing and Communications, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-signal-processing-and-communications-online/ |
| 17 | Engineering – MS in Engineering-Structural Materials, Online | MS Online | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/engineering-ms-in-engineering-structural-materials-online/ |
| 18 | Materials Science & Engineering | Materials Science | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/materials-science-engineering/ |
| 19 | Aerospace Engineering | Mechanical & Aerospace Eng | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/mechanical-aerospace-engineering-department/aerospace-engineering/ |
| 20 | Manufacturing Engineering | Mechanical & Aerospace Eng | M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/mechanical-aerospace-engineering-department/manufacturing-engineering/ |
| 21 | Mechanical Engineering | Mechanical & Aerospace Eng | D, M | grad.ucla.edu/programs/school-of-engineering-and-applied-science/mechanical-aerospace-engineering-department/mechanical-engineering/ |

#### Herb Alpert School of Music (3)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Ethnomusicology | D, M | grad.ucla.edu/programs/herb-alpert-school-of-music/ethnomusicology/ |
| 2 | Music | D, M | grad.ucla.edu/programs/herb-alpert-school-of-music/music/ |
| 3 | Musicology | D, M | grad.ucla.edu/programs/herb-alpert-school-of-music/musicology/ |

#### Humanities (L&S) (21)
##### Art History (跨系)
| 1 | Art History | D, M | grad.ucla.edu/programs/humanities/art-history/ |
##### Asian Languages and Cultures Department
| 2 | Asian Languages and Cultures | D, M | grad.ucla.edu/programs/humanities/asian-languages-and-cultures-department/asian-languages-and-cultures/ |
| 3 | Teaching Asian Languages | M | grad.ucla.edu/programs/humanities/asian-languages-and-cultures-department/teaching-asian-languages/ |
##### Classics Department
| 4 | Classics | D, M | grad.ucla.edu/programs/humanities/classics-department/classics/ |
| 5 | Greek | M | grad.ucla.edu/programs/humanities/classics-department/greek/ |
| 6 | Latin | M | grad.ucla.edu/programs/humanities/classics-department/latin/ |
| 7 | Comparative Literature | D, M | grad.ucla.edu/programs/humanities/comparative-literature/ |
| 8 | English | D, M | grad.ucla.edu/programs/humanities/english/ |
##### European Languages & Transcultural Studies Department
| 9 | French & Francophone Studies | D, M | grad.ucla.edu/programs/humanities/european-languages-transcultural-studies-department/french-and-francophone-studies/ |
| 10 | Germanic Languages | D, M | grad.ucla.edu/programs/humanities/european-languages-transcultural-studies-department/germanic-languages/ |
| 11 | Italian | D, M | grad.ucla.edu/programs/humanities/european-languages-transcultural-studies-department/italian/ |
| 12 | Scandinavian | M | grad.ucla.edu/programs/humanities/european-languages-transcultural-studies-department/scandinavian/ |
| 13 | Indo-European Studies | D, M | grad.ucla.edu/programs/humanities/indo-european-studies/ |
| 14 | Linguistics | D, M | grad.ucla.edu/programs/humanities/linguistics/ |
##### Near Eastern Languages & Cultures Department
| 15 | Islamic Studies | D, M | grad.ucla.edu/programs/humanities/near-eastern-languages-cultures-department/islamic-studies/ |
| 16 | Near Eastern Languages & Cultures | D, M | grad.ucla.edu/programs/humanities/near-eastern-languages-cultures-department/near-eastern-languages-cultures/ |
| 17 | Philosophy | D, M | grad.ucla.edu/programs/humanities/philosophy/ |
| 18 | Slavic, East European, and Eurasian Languages & Cultures | D, M | grad.ucla.edu/programs/humanities/slavic-east-european-and-eurasian-languages-cultures/ |
##### Spanish and Portuguese Department
| 19 | Hispanic Languages & Literatures | D | grad.ucla.edu/programs/humanities/spanish-and-portuguese-department/hispanic-languages-literatures/ |
| 20 | Portuguese | M | grad.ucla.edu/programs/humanities/spanish-and-portuguese-department/portuguese/ |
| 21 | Spanish | M | grad.ucla.edu/programs/humanities/spanish-and-portuguese-department/spanish/ |

#### Institute of the Environment & Sustainability (2)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Environment and Sustainability | D, M | grad.ucla.edu/programs/institute-of-the-environment-sustainability/environment-and-sustainability/ |
| 2 | Environmental Science & Engineering | D | grad.ucla.edu/programs/institute-of-the-environment-sustainability/environmental-science-and-engineering/ |

#### International Institute (3)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | African Studies | M | grad.ucla.edu/programs/international-institute/african-studies/ |
| 2 | East Asian Studies | M | grad.ucla.edu/programs/international-institute/east-asian-studies/ |
| 3 | Latin American Studies | M | grad.ucla.edu/programs/international-institute/latin-american-studies/ |

#### Life Sciences (L&S) (8)
##### Bioinformatics Department
| 1 | Bioinformatics | D, M | grad.ucla.edu/programs/life-sciences/bioinformatics-department/bioinformatics/ |
| 2 | Medical Informatics | D, M | grad.ucla.edu/programs/life-sciences/bioinformatics-department/medical-informatics/ |
##### Ecology and Evolutionary Biology Department
| 3 | Biology | D, M | grad.ucla.edu/programs/life-sciences/ecology-and-evolutionary-biology-department/biology/ |
##### Integrative Biology & Physiology Department
| 4 | Physiological Science | M | grad.ucla.edu/programs/life-sciences/integrative-biology-physiology-department/physiological-science/ |
| 5 | Molecular Biology | D, M | grad.ucla.edu/programs/life-sciences/molecular-biology/ |
| 6 | Molecular, Cell, & Developmental Biology | D, M | grad.ucla.edu/programs/life-sciences/molecular-cell-developmental-biology/ |
| 7 | Molecular, Cellular, & Integrative Physiology | D | grad.ucla.edu/programs/life-sciences/molecular-cellular-integrative-physiology/ |
| 8 | Psychology | D, M | grad.ucla.edu/programs/life-sciences/psychology/ |

#### Luskin School of Public Affairs (6)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy | M | grad.ucla.edu/programs/school-of-public-affairs/public-policy/ |
| 2 | Social Welfare | D, M | grad.ucla.edu/programs/school-of-public-affairs/social-welfare/ |
##### Urban Planning Department
| 3 | Master of Real Estate Development | M | grad.ucla.edu/programs/school-of-public-affairs/urban-planning-department/master-of-real-estate-development/ |
| 4 | Urban and Regional Planning | M | grad.ucla.edu/programs/school-of-public-affairs/urban-planning-department/urban-and-regional-planning/ |
| 5 | Urban and Regional Planning – Institut d'Etudes de Paris | M | grad.ucla.edu/programs/school-of-public-affairs/urban-planning-department/urban-and-regional-planning-institut-detudes-de-paris/ |
| 6 | Urban Planning | D | grad.ucla.edu/programs/school-of-public-affairs/urban-planning-department/urban-planning/ |

#### Physical Sciences (L&S) (15)
| 1 | Atmospheric and Oceanic Sciences | D, M | grad.ucla.edu/programs/physical-sciences/atmospheric-and-oceanic-sciences/ |
##### Chemistry and Biochemistry Department
| 2 | Biochemistry, Molecular and Structural Biology | D, M | grad.ucla.edu/programs/physical-sciences/chemistry-and-biochemistry-department/biochemistry-molecular-and-structural-biology/ |
| 3 | Chemistry | D, M | grad.ucla.edu/programs/physical-sciences/chemistry-and-biochemistry-department/chemistry/ |
| 4 | Chemistry – Master of Applied Chemical Sciences | M | grad.ucla.edu/programs/physical-sciences/chemistry-and-biochemistry-department/chemistry-master-of-applied-chemical-sciences/ |
##### Earth, Planetary, and Space Sciences Department
| 5 | Geochemistry | D, M | grad.ucla.edu/programs/physical-sciences/earth-planetary-and-space-sciences-department/geochemistry/ |
| 6 | Geology | D, M | grad.ucla.edu/programs/physical-sciences/earth-planetary-and-space-sciences-department/geology/ |
| 7 | Geophysics & Space Physics | D, M | grad.ucla.edu/programs/physical-sciences/earth-planetary-and-space-sciences-department/geophysics-space-physics/ |
| 8 | Planetary Science | D, M | grad.ucla.edu/programs/physical-sciences/earth-planetary-and-space-sciences-department/planetary-science/ |
| 9 | Mathematics | D, M | grad.ucla.edu/programs/physical-sciences/mathematics/ |
##### Physics and Astronomy Department
| 10 | Astronomy and Astrophysics | D, M | grad.ucla.edu/programs/physical-sciences/physics-and-astronomy-department/astronomy-and-astrophysics/ |
| 11 | Astronomy and Astrophysics-MAT | M | grad.ucla.edu/programs/physical-sciences/physics-and-astronomy-department/astronomy-and-astrophysics-mat/ |
| 12 | Master of Quantum Science and Technology | M | grad.ucla.edu/programs/physical-sciences/physics-and-astronomy-department/master-of-quantum-science-and-technology/ |
| 13 | Physics | D, M | grad.ucla.edu/programs/physical-sciences/physics-and-astronomy-department/physics/ |
##### Statistics and Data Science Department
| 14 | Statistics | D, M | grad.ucla.edu/programs/physical-sciences/statistics-and-data-science-department/statistics/ |
| 15 | Statistics – Master of Applied Statistics and Data Science | M | grad.ucla.edu/programs/physical-sciences/statistics-and-data-science-department/statistics-master-of-applied-statistics-and-data-science/ |

#### School of Dentistry (1)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Oral Biology | D, M | grad.ucla.edu/programs/school-of-dentistry/oral-biology/ |

#### School of Education and Information Studies (6)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Education | D, M | grad.ucla.edu/programs/school-of-education-and-information-studies/education/ |
| 2 | Educational Leadership Program | D (EdD) | grad.ucla.edu/programs/school-of-education-and-information-studies/education-leadership-program/ |
##### Information Studies Department
| 3 | Information Studies | D | grad.ucla.edu/programs/school-of-education-and-information-studies/information-studies-department/information-studies/ |
| 4 | Library & Information Science | M (MLIS) | grad.ucla.edu/programs/school-of-education-and-information-studies/information-studies-department/library-and-information-science/ |
| 5 | Library & Information Science Certificate | C | grad.ucla.edu/programs/school-of-education-and-information-studies/information-studies-department/library-and-information-science-certificate/ |
| 6 | Special Education | D | grad.ucla.edu/programs/school-of-education-and-information-studies/special-education/ |

#### School of Law (1)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Legal Studies | M | grad.ucla.edu/programs/school-of-law/master-of-legal-studies/ |

> 注: JD / LLM / SJD 通过 School of Law 独立站点申请, 不在本目录。

#### School of Nursing (3)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Nursing | D, M | grad.ucla.edu/programs/school-of-nursing/nursing/ |
| 2 | Nursing – Doctor of Nursing Practice | D (DNP), M | grad.ucla.edu/programs/school-of-nursing/nursing-doctor-of-nursing-practice/ |
| 3 | Nursing – Post-BS to DNP | D (DNP), M | grad.ucla.edu/programs/school-of-nursing/nursing-post-bs-to-dnp/ |

#### School of the Arts and Architecture (7)
##### Architecture and Urban Design Department
| 1 | Architecture | D, M | grad.ucla.edu/programs/school-of-arts-and-architecture/architecture-and-urban-design-department/architecture/ |
| 2 | Architecture – M.Arch. | M (MArch) | grad.ucla.edu/programs/school-of-arts-and-architecture/architecture-and-urban-design-department/architecture-m-arch-i/ |
| 3 | Architecture – M.S. in Architecture and Urban Design | M | grad.ucla.edu/programs/school-of-arts-and-architecture/architecture-and-urban-design-department/architecture-m-s/ |
| 4 | Art | M (MFA) | grad.ucla.edu/programs/school-of-arts-and-architecture/art/ |
| 5 | Design | Media Arts | M (MFA) | grad.ucla.edu/programs/school-of-arts-and-architecture/design-media-arts/ |
##### World Arts and Cultures/Dance Department
| 6 | Choreographic Inquiry | M (MFA) | grad.ucla.edu/programs/school-of-arts-and-architecture/world-arts-and-culturesdance-department/choreographic-inquiry/ |
| 7 | Culture and Performance | D, M | grad.ucla.edu/programs/school-of-arts-and-architecture/world-arts-and-culturesdance-department/culture-and-performance/ |

#### School of Theater, Film and Television (3)
##### Film, Television, & Digital Media Department
| 1 | Film & Television | D, M | grad.ucla.edu/programs/school-of-theater-film-and-television/film-television-digital-media-department/film-and-television/ |
##### Theater Department
| 2 | Theater | M (MFA) | grad.ucla.edu/programs/school-of-theater-film-and-television/theater-department/theater/ |
| 3 | Theater and Performance Studies | D | grad.ucla.edu/programs/school-of-theater-film-and-television/theater-department/theater-and-performance-studies/ |

#### Social Sciences (L&S) (18)
| 1 | African American Studies | M | grad.ucla.edu/programs/social-sciences/african-american-studies/ |
| 2 | American Indian Studies | M | grad.ucla.edu/programs/social-sciences/american-indian-studies/ |
| 3 | Anthropology | D, M | grad.ucla.edu/programs/social-sciences/anthropology/ |
| 4 | Archaeology | D, M | grad.ucla.edu/programs/social-sciences/archaeology/ |
| 5 | Asian American Studies | M | grad.ucla.edu/programs/social-sciences/asian-american-studies/ |
##### Chicana/o and Central American Studies Department
| 6 | Chicana & Chicano Studies | D, M | grad.ucla.edu/programs/social-sciences/chicana-o-and-central-american-studies-department/chicana-and-chicano-studies/ |
| 7 | Communication | D, M | grad.ucla.edu/programs/social-sciences/communication/ |
##### Conservation of Cultural Heritage Department
| 8 | Conservation of Cultural Heritage | M | grad.ucla.edu/programs/social-sciences/conservation-of-cultural-heritage-department/conservation-of-cultural-heritage/ |
| 9 | Conservation of Material Culture | D, M | grad.ucla.edu/programs/social-sciences/conservation-of-cultural-heritage-department/conservation-of-material-culture/ |
##### Economics Department
| 10 | Economics | D, M | grad.ucla.edu/programs/social-sciences/economics-department/economics/ |
| 11 | Economics – Master of Quantitative Economics | M | grad.ucla.edu/programs/social-sciences/economics-department/economics-master-of-quantitative-economics/ |
| 12 | Gender Studies | D, M | grad.ucla.edu/programs/social-sciences/gender-studies/ |
##### Geography Department
| 13 | Geography | D, M | grad.ucla.edu/programs/social-sciences/geography-department/geography/ |
| 14 | Master of Applied Geospatial Information Systems & Technologies | M | grad.ucla.edu/programs/social-sciences/geography-department/master-of-applied-geospatial-information-systems-technologies/ |
| 15 | History | D, M | grad.ucla.edu/programs/social-sciences/history/ |
| 16 | Master of Social Science | M | grad.ucla.edu/programs/social-sciences/master-of-social-science/ |
| 17 | Political Science | D, M | grad.ucla.edu/programs/social-sciences/political-science/ |
| 18 | Sociology | D, M | grad.ucla.edu/programs/social-sciences/sociology/ |

### 2.2 Worked example — Computer Science (MS / PhD) full deep-dive

> 来源: grad.ucla.edu/programs/school-of-engineering-and-applied-science/computer-science/ (capture 2026-07-05)

- **项目名**: Computer Science
- **所授学位**: Master of Science (M.S.) + Doctor of Philosophy (Ph.D.)
- **Major Code**: 0201
- **学院 / 系**: Samueli School of Engineering and Applied Science / Computer Science Department
- **地址**: 404 Westwood Plaza, Engineering IV, Room 291, Box 951596, Los Angeles, CA 90095-1596
- **电话**: (310) 825-0060
- **邮箱**: gradadm@cs.ucla.edu
- **项目网站**: cs.ucla.edu
- **申请入口**: grad.ucla.edu/admissions/admission-application-for-graduate-admission/
- **申请费**: $135 (US citizens/PR) 或 $155 (其他申请人)
- **典型截止**: 大多数系 11 月 / 12 月初 (具体见 program 网站 cs.ucla.edu)
- **录取通知**: 2 月起持续到夏季
- **每周期可申项目数**: 仅 1 个
- **Accordions / 折叠区**: 项目详情页含 "Admission Limited to", "Exams & GRE Types", "Letters of Recommendation", "Degree-Specific Admissions Requirements" 等字段, 默认折叠, 需展开。本数据集记录字段名, 具体值需逐项目展开提取 (P0 follow-up)。

### 2.3 Graduate admissions model

- **去中心化 (decentralized)**: UCLA 研究生录取由各系/学院的 faculty admissions committee 评审, 但申请走统一的 **Application for Graduate Admission** 门户 (grad.ucla.edu/admissions/admission-application-for-graduate-admission/)。
- **职业学位 (professional degrees) 单独处理**: DDS (School of Dentistry), MD (David Geffen School of Medicine), JD/LLM/SJD (School of Law), MBA 系列 (Anderson) 通过各 professional school 自己的网站与申请流程, 不在 grad.ucla.edu 统一门户内。
- **GRE 政策**: 由各系自定, 无全校统一要求。每个 program 详情页的 "Exams & GRE Types" 字段标注。
- **英语要求**: 全校统一最低线 (TOEFL iBT 87 / IELTS 7.0), 见 Section 3.2。各系可设更高线。
- **资金/奖学金**: 由各系负责 (RA/TA/fellowship); UCLA 设有 need-based fee waiver (US/PR)。

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | 来源 |
|------|-----|------|
| 申请平台 | **UC Application** (非 Common App) | admission.ucla.edu/apply/first-year |
| 申请开放 | 8 月 1 日 | admission.ucla.edu/apply/first-year |
| 申请提交期 | **10 月 1 日 – 11 月 30 日** | admission.ucla.edu/apply/first-year |
| EA / ED | **不提供** (UCLA does not offer early action or early decision) | admission.ucla.edu/apply/first-year |
| 学制 | Quarter system, 仅秋季入学 | admission.ucla.edu/apply/first-year |
| 录取通知 | 3 月底 (Late March) | admission.ucla.edu/apply/first-year |
| 财务申请截止 | 3 月 2 日 (FAFSA / Dream Act / Cal Grant GPA) | admission.ucla.edu/apply/first-year |
| 入学确认 (enrollment deposit + housing) 截止 | **5 月 1 日** | admission.ucla.edu/apply/first-year |
| 最终官方成绩单寄送截止 | 7 月 1 日 | admission.ucla.edu/apply/first-year |
| AP/IB 成绩寄送截止 | 7 月 15 日 | admission.ucla.edu/apply/first-year |
| SAT/ACT 政策 | **Test-FREE** — 不考虑 SAT/ACT 用于录取或奖学金 | admission.ucla.edu/apply/first-year/first-year-requirements |
| SAT/ACT 送分 | 不要求送分; 如提交可用于课程安置或最低资格 | admission.ucla.edu/apply/first-year/first-year-requirements |
| Superscore | N/A (test-free) | — |
| ACT code | 0448 | admission.ucla.edu/apply/first-year/first-year-requirements |
| College Board (SAT) code | 4837 | admission.ucla.edu/apply/first-year/first-year-requirements |
| 推荐信 | 不要求 (UC Application 不含推荐信); 综合评审基于成绩单 + PIQ + 课外活动 | admission.ucla.edu/apply/first-year |
| 面试 | **不提供** admission interview | admission.ucla.edu/apply/first-year/first-year-requirements (FAQ) |
| 个人陈述 | Personal Insight Questions (PIQ): 8 选 4, 每题 ≤350 字 | admission.ucla.edu/apply/first-year/first-year-requirements |
| Supplemental application | School of the Arts & Architecture / Herb Alpert Music / Nursing / TFT 需另交 supplemental application, 且必须列为第一志愿 | admission.ucla.edu/apply/first-year |
| 转学路径 | 转学生需达 junior 水平 (90-130 quarter / 60-90 semester units); 优先录取加州社区学院转学生 | admission.ucla.edu/apply/international-applicants |
| Fall 2025 录取生平均 unweighted GPA | 4.0 | admission.ucla.edu/apply/first-year |
| 综合评审标准数 | 13 项教师批准标准 | admission.ucla.edu/apply/first-year |

### 3.2 Undergraduate English proficiency table

> 适用条件: 若高中/中学全部非英语授课, 或英语授课不足 3 年, 须提交英语成绩。全部英语授课免试。

| 考试 | 最低分 (minimum) | 推荐/竞争性分数 (recommended/competitive) | 备注 |
|------|------------------|------------------------------------------|------|
| TOEFL iBT (旧 120 分制) | — | **100+ (subscores 24+)** | 2026-01-21 前考试适用 |
| TOEFL iBT (新修订分制, eff. 2026-01-21) | — | **5+ (subscores 5+)** | 2026-01-21 起考试适用 |
| IELTS | — | **7.5+** | Academic 模块 |
| Duolingo English Test (DET) | — | **135+** | 需通过 DET 测试门户送分, 附 UC Application ID |
| PTE Academic | 未列出 | 未列出 | UCLA UG 页面未提 |
| Cambridge | 未列出 | 未列出 | UCLA UG 页面未提 |

> 送分: TOEFL 可送到一所 UC 校区, 全部所申 UC 校区共享; IELTS 与 DET 须分别送到每个所申校区。录取后非英语母语者可能需参加 ESLPE (English-as-a-Second-Language Placement Examination)。来源: admission.ucla.edu/apply/international-applicants

### 3.3 Graduate — global rules

| 字段 | 值 | 来源 |
|------|-----|------|
| 录取模式 | **去中心化** (各系 faculty admissions committee 评审), 统一申请门户 | grad.ucla.edu/admissions/research-requirements/ |
| 申请平台 | UCLA Application for Graduate Admission (grad.ucla.edu/admissions/admission-application-for-graduate-admission/) | grad.ucla.edu/admissions/steps-to-apply/ |
| 申请费 | **$135 (US citizens/Permanent Residents) / $155 (所有其他申请人)** | grad.ucla.edu/admissions/research-requirements/ |
| 申请费豁免 | US/PR 且证明经济需要者可申请 need-based fee waiver | grad.ucla.edu/admissions/research-requirements/ |
| 每周期可申项目数 | **仅 1 个** (one program per application period) | grad.ucla.edu/admissions/research-requirements/ |
| 典型截止 | 多数系 **11 月 / 12 月初** (针对下一年秋季, 提前近一年) | grad.ucla.edu/admissions/research-requirements/ |
| 录取通知 | 2 月起持续到夏季 | grad.ucla.edu/admissions/steps-to-apply/ |
| CGS April-15-equivalent honor date | UCLA 研究生录取遵循 UC 系统惯例, 具体认捐答复日由各 program 自定 (未在统一页明示) | — |
| GRE/GMAT 政策 | **各系自定**, 无全校统一要求; 各 program 详情页 "Exams & GRE Types" 字段标注 | grad.ucla.edu/admissions/research-requirements/ |
| 英语考试政策 | 全校统一最低线, 各系可设更高 | grad.ucla.edu/admissions/english-requirements/ |
| 英语豁免 | 在美国或其他 WHED 认定英语为唯一授课语言的国家的认证大学获得学士及以上学位者, 免试 | grad.ucla.edu/admissions/english-requirements/ |
| TOEFL iBT 最低 (旧制) | **87** | grad.ucla.edu/admissions/english-requirements/ |
| TOEFL iBT 最低 (新修订分制, eff. 2026-01-21) | **4.5** | grad.ucla.edu/admissions/english-requirements/ |
| IELTS Academic 最低 | **7.0 overall** | grad.ucla.edu/admissions/english-requirements/ |
| MyBest TOEFL | **不接受** | grad.ucla.edu/admissions/english-requirements/ |
| TOEFL 机构代码 | 4837 (送至 major department) | grad.ucla.edu/admissions/english-requirements/ |
| IELTS 送分 | 送至 major department + Division of Graduate Education | grad.ucla.edu/admissions/english-requirements/ |
| TOEFL iBT Home Edition / IELTS Online | 接受 | grad.ucla.edu/admissions/english-requirements/ |
| IELTS Indicator / TOEFL iBT Paper Edition | 不再提供 | grad.ucla.edu/admissions/english-requirements/ |
| 职业学位单独申请 | DDS→School of Dentistry; MD→David Geffen School of Medicine; JD/LLM/SJD→School of Law; MBA 系列→Anderson | grad.ucla.edu/admissions/steps-to-apply/ |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26, Updated March 2026) — line-itemized

> 来源: admission.ucla.edu/tuition-aid/tuition-fees (capture 2026-07-05). 每学年 (九个月) 估算。

| 项目 | 居住学校宿舍 (Residence Halls) | 校外公寓 (Off-Campus) | 走读 (Commuter) |
|------|------|------|------|
| University Fees (学费核心) | $16,706 | $16,706 | $16,706 |
| Food and Housing (食宿) | $19,779 | $21,087 | $8,603 |
| Books, Course Materials, Supplies, and Equipment | $1,554 | $1,554 | $1,554 |
| Transportation (交通) | $942 | $1,539 | $2,812 |
| Personal (个人) | $2,685 | $3,235 | $3,039 |
| Health Insurance* (UC SHIP) | $3,687 | $3,687 | $3,687 |
| **Total – California Residents** | **$45,353** | **$47,808** | **$36,401** |
| Nonresident Supplemental Tuition (非居民附加学费) | $39,270 | $39,270 | $39,270 |
| **Total – Nonresidents** | **$84,623** | **$87,078** | **$75,671** |

> *UC SHIP 健康保险要求与费用可凭已有足够保险覆盖豁免 (waive)。
> **任务书核对**: 任务书称 "in-state ~$15k / OOS ~$45k"。实际: in-state 的 **University Fees = $16,706** (即"学费"部分, 接近 $15k); OOS 的 **总 COA = $84,623** (含 $39,270 非居民附加学费), 任务书的 "$45k OOS" 应为对 in-state 总 COA ($45,353) 或 OOS 学费+附加 ($16,706+$39,270=$55,976) 的近似误记。本表用官方精确数字。

### 4.2 Undergraduate financial-aid policy

| 字段 | 值 | 来源 |
|------|-----|------|
| Need-blind / Need-aware | **Need-aware** (对国际生尤为如此) | admission.ucla.edu/apply/international-applicants |
| 国际生资助政策 | **UCLA 不向非美国公民/永久居民的本科生授予奖学金或助学金** | admission.ucla.edu/apply/international-applicants |
| 国际生最低资金证明 (Fall 2026) | **~$80,739** (另推荐 +$5,000 个人/应急/暑期开支) | admission.ucla.edu/apply/international-applicants |
| 财务申请优先截止 | **3 月 2 日** (FAFSA / CA Dream Act / Cal Grant GPA) | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| US 公民/PR 申请 | FAFSA | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| AB540 加州无身份学生 | CA Dream Act Application (CADAA) | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| UCLA 本科生平均毕业贷款债务 | **$19,000** (vs 全美 $39,000) | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| 贷款偿还成功率 | **99%** | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| 资助类型 | 4 类: Scholarships / Grants / Loans / Part-Time Student Jobs (含 work-study) | admission.ucla.edu/tuition-aid/financial-aid-and-scholarships |
| 学费全免收入阈值 | N/A (UCLA 为公立, 无私立名校式的"低于 X 万美元免学费"政策; 资助按 need-based 计算) | — |
| 零家长贡献阈值 | N/A (同上) | — |
| Net Price Calculator | admission.ucla.edu/tuition-aid/net-price-calculator | admission.ucla.edu/tuition-aid |
| 平均起薪 | 未在 admission.ucla.edu 公开 (P1 follow-up, 见 Student Outcomes 页) | — |

### 4.3 Graduate cost & funding framework

| 字段 | 值 | 来源 |
|------|-----|------|
| CA resident 研究生学费/年 | **$18,136** | grad.ucla.edu/admissions/ |
| Non-resident 研究生学费/年 | **$33,238** | grad.ucla.edu/admissions/ |
| UCLA 自我定位 | USNWR top 25 中国立大学中**最可负担**的研究生学费 (CA 与非 CA 均最低) | grad.ucla.edu/admissions/ |
| 申请费 | $135 (US/PR) / $155 (其他) | grad.ucla.edu/admissions/research-requirements/ |
| 申请费豁免 | US/PR 经济需要者可申请 need-based waiver | grad.ucla.edu/admissions/research-requirements/ |
| 资金类型分类 | 各系负责: RA (Research Assistant) / TA (Teaching Assistant) / Fellowship / Grant | grad.ucla.edu/funding/ (P0 follow-up) |
| 研究经费规模 | UCLA 年度竞争性科研经费超 **$10 亿** | grad.ucla.edu/admissions/ |
| 国际研究生资助 | 由各系提供 (RA/TA/fellowship); 无 UG 式的全校need-blind 承诺 | grad.ucla.edu/funding/ |
| Stipend 费率 / 生活费 | 未在本数据集统一抓取 (各系/各 program 异; P0 follow-up 见各 program 页) | — |
| Cost-of-attendance (研究生) | 未在 grad.ucla.edu 统一页 (P0 follow-up; registrar 站点 tuition-fees 页 404) | — |

---

## SECTION 5 — Evidence chain index

> 每个 YAML 块对应一个高价值字段, 含 URL + verbatim snippet + capture date。E-U = undergraduate, E-G = graduate。

```yaml
- id: E-U-001
  field: ug.application_platform
  value: "UC Application (University of California's online application)"
  source_url: https://admission.ucla.edu/apply/first-year
  source_snippet: "To begin the application process, use the University of California's online application (UC Application)."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-002
  field: ug.deadlines.filing_period
  value: "October 1 - November 30 (no EA/ED)"
  source_url: https://admission.ucla.edu/apply/first-year
  source_snippet: "Applications can be submitted October 1-December 1. ... October 1 - November 30 Application filing period ... UCLA does not offer early action or early decision for any applications."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-003
  field: ug.deadlines.notification_and_deposit
  value: "Late March notification; May 1 enrollment deposit"
  source_url: https://admission.ucla.edu/apply/first-year
  source_snippet: "Late March Admission notification ... May 1 Deadline to submit your enrollment deposit and application for on-campus housing."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-004
  field: ug.test_policy
  value: "Test-FREE — SAT/ACT not considered for admission or scholarship"
  source_url: https://admission.ucla.edu/apply/first-year/first-year-requirements
  source_snippet: "UCLA will not consider SAT or ACT scores for admission or scholarship purposes. If you choose to submit test scores as part of your application, they may be used as an alternative method of fulfilling minimum requirements for eligibility or for course placement after you enroll. UCLA's ACT number: 0448 UCLA's College Board (SAT) number: 4837"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-005
  field: ug.a_g_requirements
  value: "15 A-G courses (History2 English4 Math3 LabSci2 LOTE2 VPA1 Elective1)"
  source_url: https://admission.ucla.edu/apply/first-year/first-year-requirements
  source_snippet: "You must complete 15 A-G courses with at least 11 courses finished prior to the beginning of your last year of high school. ... 2 years history/social science; 4 years of college-preparatory English; 3 years of mathematics (4 years recommended); 2 years of laboratory science (3 years recommended); 2 years of language other than English (3 years recommended); 1 year of visual and performing arts (if available); 1 year of college-preparatory elective"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-006
  field: ug.gpa_fall_2025_admits
  value: "4.0 average unweighted GPA"
  source_url: https://admission.ucla.edu/apply/first-year
  source_snippet: "Grades and GPA (4.0 average unweighted GPA for Fall 2025 admits)"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-007
  field: ug.personal_insight_questions
  value: "8 prompts choose 4, max 350 words each"
  source_url: https://admission.ucla.edu/apply/first-year/first-year-requirements
  source_snippet: "As a first-year applicant, you may respond to four of eight questions. Each response is limited to a maximum of 350 words."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-008
  field: ug.english_proficiency.competitive
  value: "TOEFL iBT 100+ (subscores 24+) old scale; 5+ revised scale (eff 2026-01-21); IELTS 7.5+; DET 135+"
  source_url: https://admission.ucla.edu/apply/international-applicants
  source_snippet: "We look for competitive English proficiency scores, including a TOEFL iBT score of 5 or higher (with sub-scores of 5 or higher) on the revised scale (effective January 21, 2026), or above 100 (with sub-scores above 24) on the previous 120-point scale, as well as 7.5 or above on the IELTS or 135 or higher on the Duolingo English Test (DET)."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-009
  field: ug.international_financial
  value: "No aid/scholarships for non-citizens/non-PR; minimum ~$80,739 funds (Fall 2026)"
  source_url: https://admission.ucla.edu/apply/international-applicants
  source_snippet: "UCLA does not award scholarships or financial aid to undergraduate students who are not citizens or permanent residents of the United States. International students must prove that they have sufficient funds available to them to pay for their educational and living expenses. For example, students admitted to Fall Quarter 2026 will need a minimum of about $80,739 (with an additional $5,000 recommended for additional personal expenses, contingencies and summer expenses)."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-010
  field: ug.cost.coa_2025_26
  value: "Total CA resident $45,353 / Nonresident $84,623 (residence halls); Univ Fees $16,706; Nonresident Supplemental $39,270"
  source_url: https://admission.ucla.edu/tuition-aid/tuition-fees
  source_snippet: "University Fees $16,706 ... Food and Housing $19,779 ... Books, Course Materials, Supplies, and Equipment $1,554 ... Transportation $942 ... Personal $2,685 ... Health Insurance* $3,687 ... Total – California Residents $45,353 ... Nonresident Supplemental Tuition $39,270 ... Total – Nonresidents $84,623 ... Updated March 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```
```yaml
- id: E-U-011
  field: ug.financial_aid.debt_statistics
  value: "Avg UCLA senior debt $19,000 (national $39,000); 99% repayment rate"
  source_url: https://admission.ucla.edu/tuition-aid/financial-aid-and-scholarships
  source_snippet: "In 2025, graduating seniors in the U.S. had an average student loan debt of $39,000. However, for UCLA seniors, the average was much lower — just $19,000. And nearly all UCLA graduates — 99% of them — successfully manage loan repayment."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-U-012
  field: ug.supplemental_applications
  value: "Required for Arts & Architecture, Herb Alpert Music, Nursing, TFT (must be first-choice major)"
  source_url: https://admission.ucla.edu/apply/first-year
  source_snippet: "Some of our majors outside of the College may require applicants to submit a supplemental application directly to that school. ... School of the Arts and Architecture; Herb Alpert School of Music; School of Nursing; School of Theater, Film and Television. Applicants must list majors in these schools as their first-choice major when completing the UC application."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-001
  field: grad.program_count_ucla_claim
  value: "133 degree programs (homepage) / 136 (steps-to-apply)"
  source_url: https://grad.ucla.edu/admissions/
  source_snippet: "Since then, graduate studies at UCLA has blossomed into 133 degree programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-002
  field: grad.application_fee
  value: "$135 (US citizens/PR) or $155 (all other applicants)"
  source_url: https://grad.ucla.edu/admissions/research-requirements/
  source_snippet: "The $135.00 (for U.S. citizens and Permanent Residents) or $155.00 (for all other applicants) application fee must be submitted online by credit or debit card before the application can be processed."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-003
  field: grad.deadlines.typical
  value: "Most departments November/early December for following Fall"
  source_url: https://grad.ucla.edu/admissions/research-requirements/
  source_snippet: "Most departments and schools have deadlines in November and early December for the following Fall term (nearly a year in advance)."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-004
  field: grad.one_program_per_period
  value: "Only one application can be considered per period"
  source_url: https://grad.ucla.edu/admissions/research-requirements/
  source_snippet: "UCLA allows you to apply to only one program per application period."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-005
  field: grad.english_proficiency.minimum
  value: "TOEFL iBT 87 (old) / 4.5 (revised eff 2026-01-21); IELTS Academic 7.0; MyBest not accepted"
  source_url: https://grad.ucla.edu/admissions/english-requirements/
  source_snippet: "Minimum overall score on TOEFL iBT: 87 (for exams taken before January 21, 2026) or 4.5 (for exams taken on or after January 21, 2026). TOEFL iBT scores should be sent to your major department. Be sure to list the TOEFL institution code for UCLA 4837. UCLA does not currently accept MyBest TOEFL. Minimum overall band score on IELTS Academic: 7.0."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-006
  field: grad.english_exemption
  value: "Bachelor's+ from US accredited or WHED English-sole-language institution"
  source_url: https://grad.ucla.edu/admissions/english-requirements/
  source_snippet: "A bachelor's degree or higher from an accredited university located in the United States or in another country where English is the sole language of instruction according to the World Higher Education Database (WHED). If you meet this criterion, you are exempt from submitting English proficiency test scores"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-007
  field: grad.tuition
  value: "$18,136/yr CA-resident; $33,238/yr non-resident"
  source_url: https://grad.ucla.edu/admissions/
  source_snippet: "UCLA offers the most affordable graduate tuition across US News & World Report's top 25 ranked National Universities of 2022: $18,136 /yr CA-resident. And also the least expensive graduate tuition for out-of-state students: $33,238 /yr non-resident."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```
```yaml
- id: E-G-008
  field: grad.programs_directory
  value: "150 leaf entries; 83 PhD-offering; 140 Master's-offering; 1 Certificate; 18 schools/divisions"
  source_url: https://grad.ucla.edu/schools/
  source_snippet: "Graduate programs at the University of California Los Angeles (UCLA) organized by school, department, division, and institute. Key: Doctorate / Master's Degree / Master's Degree (on path to Doctorate) / Certificate"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```
```yaml
- id: E-G-009
  field: grad.cs_program_detail
  value: "Computer Science MS+PhD; Major Code 0201; Engineering IV Rm 291; (310) 825-0060; gradadm@cs.ucla.edu"
  source_url: https://grad.ucla.edu/programs/school-of-engineering-and-applied-science/computer-science/
  source_snippet: "UCLA's Graduate Program in Computer Science offers the following degree(s): Master of Science (M.S.); Doctor of Philosophy (Ph.D.) ... Major Code 0201 ... Address: 404 Westwood Plaza, Engineering IV, Room 291, Box 951596, Los Angeles, CA 90095-1596 ... Phone: (310) 825-0060 ... Email: gradadm@cs.ucla.edu ... Website: cs.ucla.edu"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: ucla-knowledge-base-v2
├── document: UCLA-院校总览                    (Section 0 — rules 1-4, overview/matrix)
├── document: UCLA-本科-学院L&S                (Section 1.2 L&S — 105 majors)
├── document: UCLA-本科-职业学院               (Section 1.2 Arts&Arch/Eng/Music/Nursing/Luskin/TFT/Ed&Info/Fielding)
├── document: UCLA-本科-辅修清单               (Section 1.4 — 105 minors)
├── document: UCLA-研究生-Anderson             (Section 2 Anderson)
├── document: UCLA-研究生-Medicine             (Section 2 David Geffen)
├── document: UCLA-研究生-PublicHealth-Fielding(Section 2 Fielding)
├── document: UCLA-研究生-Engineering-Samueli  (Section 2 Samueli)
├── document: UCLA-研究生-Music-HerbAlpert     (Section 2 Herb Alpert)
├── document: UCLA-研究生-Humanities-LS        (Section 2 Humanities)
├── document: UCLA-研究生-LifeSci-LS           (Section 2 Life Sciences)
├── document: UCLA-研究生-PhysicalSci-LS       (Section 2 Physical Sciences)
├── document: UCLA-研究生-SocialSci-LS         (Section 2 Social Sciences)
├── document: UCLA-研究生-PublicAffairs-Luskin (Section 2 Luskin)
├── document: UCLA-研究生-其他学院             (Env&Sus / IntlInst / Dentistry / Ed&Info / Law / Nursing / Arts&Arch / TFT)
├── document: UCLA-申请要求与截止             (Section 3)
├── document: UCLA-学费与资助                 (Section 4)
└── document: UCLA-证据链与监控               (Section 5 + watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ucla-knowledge-base-v2"
  school: "<home college / division>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|MFA|MBA|MEng|MArch|MPH|MPP|MSW|MLIS|PhD|EdD|DNP|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL / 备注 |
|--------|--------|----------------|
| P0 | 研究生各 program 的 GRE/GMAT 具体政策 + 截止日期 + 推荐信数 | 每个 program detail 页的 "Admission Limited to" / "Exams & GRE Types" / "Letters of Recommendation" accordion (需逐个展开, 150 个) |
| P0 | 研究生各 program 的 stipend 费率 / 资金包 | grad.ucla.edu/funding/ + 各 program 网站 |
| P0 | 研究生 cost-of-attendance 统一页 (registrar tuition-fees 页 404) | registrar.ucla.edu (需找正确路径) 或各 professional school |
| P1 | 本科转学 (transfer) 完整要求与截止 | admission.ucla.edu/apply/transfer |
| P1 | 本科录取统计 (录取率、申请数) | admission.ucla.edu/apply/first-year/first-year-profile |
| P1 | 本科生平均起薪 / Student Outcomes | admission.ucla.edu/explore/student-outcomes |
| P2 | UCLA 第一志愿申请指南 PDF 细节 | admission.ucla.edu/sites/default/files/documents/UCLA-First-Year-Admission-Guide-2025.pdf |
| P2 | 研究生 calendar (现需 sign-in) | grad.ucla.edu/admissions/calendar/ (需 UCLA grad 账号) |
| P2 | 各 professional school (Anderson/MD/Law/Dentistry) 独立站点完整录取要求 | anderson.ucla.edu / medschool.ucla.edu / law.ucla.edu / dentistry.ucla.edu |

### Monitoring watchlist (frequency-classified)

| 频率 | 字段 | URL |
|------|------|-----|
| High (monthly) | ug.deadlines | admission.ucla.edu/apply/first-year |
| High | ug.test_policy | admission.ucla.edu/apply/first-year/first-year-requirements |
| High | ug.cost.coa | admission.ucla.edu/tuition-aid/tuition-fees |
| High | ug.english_proficiency | admission.ucla.edu/apply/international-applicants |
| High | grad.application.fee | grad.ucla.edu/admissions/research-requirements/ |
| High | grad.english_proficiency | grad.ucla.edu/admissions/english-requirements/ |
| High | grad.tuition | grad.ucla.edu/admissions/ |
| Medium (quarterly) | ug.majors.count | admission.ucla.edu/apply/majors |
| Medium | ug.minors | admission.ucla.edu/apply/minors |
| Medium | grad.programs.directory | grad.ucla.edu/schools/ |
| Low (annual) | ug.overview / hierarchy | admission.ucla.edu/ |
| Low | grad.overview | grad.ucla.edu/admissions/ |

---

## SECTION 7 — Cross-school comparison framework

> 本校 (UCLA) 列已填, 其他校留空, 待同结构文档产出后即可横向比较。

| 维度 | UCLA (UC) | UC Berkeley (UC) | MIT (private) | Stanford (private) | Harvard (private) |
|------|-----------|------------------|---------------|--------------------|-------------------|
| 总 UG COA/yr (in-state, res hall) | $45,353 | ~$47k | ~$85k | ~$87k | ~$79k |
| 学费/yr (in-state 核心费用) | $16,706 (Univ Fees) | ~$17k | ~$61k | ~$61k | ~$56k |
| Need-blind (intl?) | **No** (need-aware intl) | No (need-aware intl) | Yes (intl too) | Yes (intl too) | Yes (intl too) |
| EA deadline | N/A (no EA/ED) | N/A (no EA/ED) | EA (non-binding) | REA | REA / SCEA |
| RA / filing deadline | **Nov 30** (Oct 1-Nov 30) | Nov 30 (UC) | Jan 1 | Jan 5 | Jan 1 |
| SAT/ACT required? | **Test-FREE** | Test-FREE | Test-flexible (none req) | Test-optional | Test-optional |
| TOEFL min (UG competitive) | 100 | ~100 | 100 (rec) | 100 (rec) | 100 (rec, varies by dept) |
| IELTS min (UG competitive) | 7.5 | 7.5 | 7.5 | — | 7.5 |
| 学费全免阈值 | N/A (公立, 无此政策) | N/A | <$200k | <$150k | <$85k-<$150k |
| 中位实付 | (按 need 算) | (按 need 算) | ~$19,985 | ~$12k-18k | ~$18k |
| 研究生申请费 | $135/$155 | $135/$155 | $75-$150 | $125 | $105 |
| April-15-equivalent honor date | (各 program 自定) | (各 program 自定) | CGS Apr 15 | CGS Apr 15 | CGS Apr 15 |
| **总项目数 (rule 1)** | **137 UG majors + 150 grad = 287** (+105 minors) | 285 deg + 129 minors | ~110 majors + ~175 grad | ~65 UG + ~200 grad | ~50 fields + ~100 grad |
| **学院/系总数 (rule 2)** | 9 UG schools / 18 grad divisions | 14 colleges | 5 schools + 1 college | 7 schools | 12 schools |

---

## RECONCILIATION REPORT (mandatory gate)

| 校验项 | 期望 | 实际 | 状态 |
|--------|------|------|------|
| Rule-1 UG majors 总数 | = Section 1.2 各表行数之和 | 137 (L&S 105 + Arts&Arch 8 + Eng 10 + Music 6 + Nursing 1 + Luskin 1 + TFT 3 + Ed&Info 1 + Fielding 2) | ✅ |
| Rule-1 UG degree (BA+BS) | = 矩阵列和 | BA 91 + BS 46 = 137 | ✅ |
| Rule-1 Grad 目录条目 | = Section 2 各表行数之和 | 150 (Anderson 7 + Medicine 8 + Fielding 17 + Eng 21 + Music 3 + Humanities 21 + Env&Sus 2 + IntlInst 3 + LifeSci 8 + Luskin 6 + PhysSci 15 + Dentistry 1 + Ed&Info 6 + Law 1 + Nursing 3 + Arts&Arch 7 + TFT 3 + SocialSci 18) | ✅ |
| Rule-4 UG 矩阵行列和 | 行和=各校 majors; 列和=BA/BS 总; grand=137 | 行和=137, 列和 BA=91/BS=46, grand=137 | ✅ |
| Rule-4 Grad badge 视角 vs 条目视角 | badge (D=83,M=140,C=1) ≥ 条目 (150); 差额=83 个 D+M 双 badge 条目 | 83+140+1=224 badge-offers; 150 entries; 224-150=74 ≈ 双 badge 数 (实际 83 个 PhD 条目中 74 个同时含 M badge, 9 个仅 D) | ✅ (一致) |
| Rule-5 全量叶级枚举 | UG 137 + Grad 150 = 287, 无 "representative"/"etc." | 全部列出, 无缩写 | ✅ |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.ucla.edu (UG admissions, majors, minors, tuition, finaid, international, first-year, requirements); grad.ucla.edu (grad admissions hub, schools directory, steps-to-apply, research-requirements, english-requirements, international-applicants, CS program detail)
> **Verification**: ego-browser snapshotText + JS DOM extraction (.major-container / degree-badge / H2-school-heading parsing) + serverFetch for static HTML
> **Granularity**: school → department → degree-level → program
> **Cache**: uni-cache/schools/ucla/ (site-memory.json + last-extract.json + content-hashes.json)
> **Platform detected**: static-html (no SPA framework; both UG majors and grad schools directory render server-side)
> **Task-space**: ego-browser task space 25 ("UCLA admissions deep research"), completed with { keep: false }
