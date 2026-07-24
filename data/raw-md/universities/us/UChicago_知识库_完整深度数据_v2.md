# University of Chicago Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

> **Important provenance note**: The University of Chicago has a distinctive academic structure. Undergraduate education is administered by **The College** (one unified undergraduate college), organized internally into four **Collegiate Divisions** (Biological Sciences, Arts & Humanities, Physical Sciences, Social Sciences). Graduate/professional education is distributed across **12 graduate divisions and professional schools**. Source-of-truth domains: `collegeadmissions.uchicago.edu` (UG admissions), `college.uchicago.edu` (The College academics), `grad.uchicago.edu` (graduate hub), `financialaid.uchicago.edu` (cost), `collegecatalog.uchicago.edu` (College Catalog — note: this subdomain returns HTTP 403 to direct headless browsing, so catalog links are cited from the College's programs-of-study index).

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 / 来源 |
|------|------|------|
| 本科 Major 授予项 (BA/BS) | 56 | 82 个本科"Programs of Study"中标注 "Major" 的去重计数；College 官方宣传口径 "68 Majors"（含语言子方向、生物 track 等聚合细分） |
| 本科 Minor 授予项 | 53 | 同上，标注 "Minor" 的去重计数；官方宣传口径 "57 Minors" |
| 本科联合学位 (Joint BA/MA / BA/MS / BA/MAT / BA/MPP) | 16 | College→研究生院 4+1 / 5 年制项目 |
| 本科跨学科/预备职业项目 (Interdisciplinary) | 4 | Big Problems / Chicago Studies / Clinical & Translational Science / Institute for the Formation of Knowledge |
| 本科 Programs-of-Study 总条目 | **82** | college.uchicago.edu/academics/programs-study 手风琴条目 |
| 研究生项目条目 (MA/MS/MFA/MBA/MPP/MDiv/PhD/MD/JD/JSD/DCompL/MEng) | **101** | grad.uchicago.edu/admissions/programs/ 全量目录 |
| **学位项目总计 (UG Programs-of-Study + Grad)** | **183** | 82 + 101 |

> **Reconciliation note (重要)**: Three reconciling numbers are used in this document:
> - **Rule-1 / Rule-3 / Rule-4 / Rule-5 row count = 183** (82 UG program-of-study entries + 101 graduate program entries). This is the count of *distinct program listings* scraped from official indexes.
> - A finer-grained count of *program × offering-type* rows = 129 (UG) + 101 (grad) = **230** leaf rows when a single program offering both a Major and a Minor is split into two rows. Section 1 uses this finer granularity; Section 2 (grad) does not split because each grad entry already names specific degree(s).
> - The College's own headline "68 Majors & 57 Minors" counts *every major and minor offering* including language subspecializations and biology tracks as separate items; this differs from the 82-entry programs-of-study index because some accordion entries aggregate multiple specializations (e.g., Biological Sciences has 7 specializations counted separately by the College but appears as 1 entry). Both numbers are cited; the 82-entry / 101-entry counts are what the official indexes actually list and are what this document reconciles against.

**Verification (Python):**
```python
import json
ug = json.load(open('/tmp/uchicago_ug.json'))   # 82 entries
grad = json.load(open('/tmp/uchicago_grad.json')) # 101 entries
assert len(ug) == 82 and len(grad) == 101
assert len(ug) + len(grad) == 183  # rule-1 == rule-5 row count ✓
```

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

The University of Chicago has a **two-tier** structure: undergraduates belong to one unified **College**, while graduate/professional work spans 12 independent divisions/schools. The College itself is internally subdivided into four **Collegiate Divisions** for academic administration.

```
University of Chicago
├── The College (本科统一学院; 4 Collegiate Divisions administer UG academics)        [学院]
│   ├── Biological Sciences Collegiate Division (BSCD)                              [系/学部]
│   │   └── Biological Sciences / Biological Chemistry / Neuroscience / Computational Neuroscience
│   ├── Physical Sciences Collegiate Division (PSCD)                                [系/学部]
│   │   └── Mathematics / Physics / Chemistry / Computer Science / Statistics / Molecular Engineering /
│   │       Geophysical Sciences / Astronomy & Astrophysics / Data Science / CAAM / etc.
│   ├── Social Sciences Collegiate Division (SSCD)                                  [系/学部]
│   │   └── Economics / Political Science / Sociology / Psychology / Anthropology /
│   │       History / Public Policy Studies / CHD / etc.
│   └── Arts & Humanities Collegiate Division                                       [系/学部]
│       └── English / Philosophy / History of Art / Music / Classics / Linguistics /
│           Romance Languages / East Asian Languages & Civ / etc.
│
├── Biological Sciences Division (BSD) — graduate                                   [学院]
│   └── 10+ doctoral committees (Biochemistry & Molecular Biophysics, Cancer Biology,
│       Cell & Molecular Biology, Computational Neuroscience, Development/Regeneration/Stem Cell,
│       Ecology & Evolution, Evolutionary Biology, Genetics/Genomics/Systems Biology, Human Genetics,
│       Immunology, Integrative Biology, Medical Physics, Microbiology, Molecular Metabolism &
│       Nutrition, Neurobiology) + 5 master's programs
│
├── Physical Sciences Division (PSD) — graduate                                     [学院]
│   └── Astronomy/Astrophysics, Chemistry, Computational & Applied Mathematics,
│       Computer Science, Data Science, Environmental Science, Financial Mathematics,
│       Geophysical Sciences, Mathematics, Physics, Statistics, Applied Data Science
│
├── Social Sciences Division (SSD) — graduate                                        [学院]
│   └── Anthropology, CHSS, Comparative Human Development, Computational Social Science,
│       Economics, History, International Relations (CIR), MAPSS, Political Science,
│       Psychology, Social Thought, Sociology
│
├── Arts & Humanities Division — graduate                                            [学院]
│   └── Art History, Cinema & Media Studies, Classics, Comparative Literature,
│       Digital Studies, East Asian Languages & Civ, English, Germanic Studies,
│       Linguistics, MAPH, Middle Eastern Studies, Music, Philosophy,
│       Romance Languages & Lit, Slavic Languages & Lit, South Asian Languages & Civ,
│       Theater & Performance Studies, Visual Arts (MFA)
│
├── Divinity School                                                                  [学院]
│   └── 11 areas of study (Bible, History of Christianity, History of Judaism, Islamic Studies,
│       Philosophy of Religions, Religious Ethics, Theology, Religion/Lit/Visual Culture,
│       Anthropology & Sociology of Religion, Religions in America, Religious Studies)
│       + MDiv / MA / MA(RS) / PhD
│
├── Chicago Booth School of Business                                                [学院]
│   └── MBA, Master of Finance, Master of Management, PhD (8 fields:
│       Accounting, Behavioral Science, Economics, Econometrics & Statistics, Finance,
│       Management Science/Operations Management, Marketing, Business)
│
├── Law School                                                                       [学院]
│   └── JD, LLM, MLS (Master of Legal Studies), JSD, D.Comp.L
│
├── Pritzker School of Medicine                                                      [学院]
│   └── MD, MD/PhD (MSTP), MD/PhD (MESH — Medicine, Social Sciences, & Humanities)
│
├── Pritzker School of Molecular Engineering (PME)                                   [学院]
│   └── MEng, PhD (Molecular Engineering), PhD (Quantum Science & Engineering)
│
├── Harris School of Public Policy                                                    [学院]
│   └── MPP, MA (Public Policy), MA (Evening), MACRM, MSCAPP, PhD, MA CIR (joint),
│       Political Economy (joint with SSD)
│
├── Crown Family School of Social Work, Policy, and Practice                         [学院]
│   └── MA (Social Work), MA (Social Sector Leadership & Nonprofit Management), PhD (Social Work)
│
└── Graham School of Continuing Liberal and Professional Studies                      [学院]
    └── Master of Liberal Arts (MLA)
```

**Cross-divisional / shared programs (⚠):**
- **Biophysical Sciences** PhD — jointly administered by BSD and PSD
- **Political Economy** — jointly administered by Harris School and SSD
- **Interdisciplinary Scientist Training Program (ISTP)** MD/PhD — Pritzker (Medicine) + BSD
- **MESH** MD/PhD — Pritzker (Medicine) + Social Sciences/Humanities
- All UG Joint BA/MA / BA/MS programs are co-administered by The College and the corresponding graduate school

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 | 来源 |
|---------|------|------|-----------|------|
| BA | Bachelor of Arts | 本科 | (UG majors grant BA or BS; UChicago awards both) | college.uchicago.edu |
| BS | Bachelor of Science | 本科 | (subset of UG majors, esp. in BSCD/PSCD) | college.uchicago.edu |
| (UG Major 授予项合计) | | 本科 | **56** | 82-entry index |
| (UG Minor 授予项合计) | | 本科辅修 | **53** | 82-entry index |
| (UG Joint Degree) | BA/MA, BA/MS, BA/MAT, BA/MPP | 本科联合 | **16** | 82-entry index |
| (UG Interdisciplinary) | | 本科跨学科 | **4** | 82-entry index |
| MA | Master of Arts | 研究生 | 多数 Humanities/SSD/Divinity/Harris 项目 | grad.uchicago.edu |
| MS | Master of Science | 研究生 | PSD/BSD 项目 (MS Data Science, MS Statistics, MS Chemistry, MSCAPP, MS Biomedical Informatics, etc.) | grad.uchicago.edu |
| MFA | Master of Fine Arts | 研究生 | 1 (Visual Arts) | grad.uchicago.edu |
| MBA | Master of Business Administration | 研究生 | Booth | grad.uchicago.edu |
| MPP | Master of Public Policy | 研究生 | Harris | grad.uchicago.edu |
| MDiv | Master of Divinity | 研究生 | Divinity School | grad.uchicago.edu |
| MLA | Master of Liberal Arts | 研究生 | Graham School | grad.uchicago.edu |
| MEng | Master of Engineering | 研究生 | PME | grad.uchicago.edu |
| LLM | Master of Laws | 研究生 | Law School | grad.uchicago.edu |
| MLS | Master of Legal Studies | 研究生 | Law School | grad.uchicago.edu |
| MA-MACRM | MA + Certificate in Research Methods | 研究生 | Harris | grad.uchicago.edu |
| PhD | Doctor of Philosophy | 研究生 | (大多数 BSD/PSD/SSD/A&H/Divinity/Harris/Booth/PME/Crown 项目) | grad.uchicago.edu |
| MD | Medical Doctor | 专业博士 | Pritzker School of Medicine | grad.uchicago.edu |
| JD | Juris Doctor | 专业博士 | Law School | grad.uchicago.edu |
| JSD | Doctor of Jurisprudence (Science of Law) | 研究生法学博士 | Law School | grad.uchicago.edu |
| D.Comp.L | Doctor of Comparative Law | 研究生法学博士 | Law School | grad.uchicago.edu |
| MD/PhD | (MSTP / MESH) | 双学位专业博士 | Pritzker | grad.uchicago.edu |

**Graduate degree-type distribution (computed from `data-filter` on each program card):**

| 类别 | 项目数 |
|------|-------|
| Master + PhD (combined, same program admits both) | 54 |
| PhD / Doctoral only | 29 |
| Master's only | 18 |
| **研究生项目合计** | **101** |

### 0.4 分布矩阵 (Rule 4 — 学院 × 学位级别)

**Graduate programs (学院 × Master's/Doctoral):**

| 学院 / 研究生院 \ 级别 | Master's | Doctoral (PhD/MD/JD/JSD/DCompL/MD-PhD) | 合计 |
|---|---|---|---|
| Biological Sciences Division | 5 | 17 | 22 (incl. 1 joint BSD/PSD) |
| Physical Sciences Division | 8 | 9 | 12 (+1 joint with BSD = Biophysical Sciences counted in BSD row) |
| Social Sciences Division | 12 | 10 | 12 (+1 joint with Harris = Political Economy counted in Harris row) |
| Arts & Humanities Division | 18 | 15 | 18 |
| Divinity School | 12 | 11 | 12 |
| Chicago Booth School of Business | 8 | 8 | 8 |
| Harris School of Public Policy | 3 | 1 | 3 (+1 joint Political Economy shown separately below) |
| Pritzker School of Medicine | 0 | 3 | 3 |
| Pritzker School of Molecular Engineering | 1 | 2 | 3 |
| Crown Family School | 2 | 1 | 2 |
| Law School | 1 | 4 | 4 |
| Graham School | 1 | 0 | 1 |
| Harris × SSD (Political Economy, joint) | 1 | 1 | 1 (cross-listed; counted once) |
| BSD × PSD (Biophysical Sciences, joint) | 0 | 1 | 1 (cross-listed; counted once) |
| **合计** | **72** | **83** | **101** ✓ |

> Note: A program offering both a Master's and a Doctoral track is counted once per column (e.g., Chemistry appears in both the Master's cell and the Doctoral cell of PSD). Row totals therefore count *distinct program listings* per division, while column totals count *distinct program-degree offerings*. The 101 figure reconciles to the count of program cards on the official index; the Master's+Doctoral column sum (72+83=155) exceeds 101 because 54 programs offer both tiers and are counted in each column.

**Undergraduate programs (Collegiate Division × offering type):**

| 本科学院部 \ 授予类型 | Major | Minor | Joint Degree | Interdisciplinary | 条目合计 |
|---|---|---|---|---|---|
| Biological Sciences Collegiate Div | 3 | 3 | 1 | 0 | 4 distinct programs |
| Physical Sciences Collegiate Div | 12 | 8 | 4 | 0 | 12 distinct programs |
| Arts & Humanities Collegiate Div | 24 | 26 | 1 | 0 | 30 distinct programs |
| Social Sciences Collegiate Div | 16 | 14 | 2 | 0 | 22 distinct programs |
| Interdisciplinary / Pre-Professional | 1 | 2 | 8 | 4 | 14 distinct programs |
| **本科条目合计** | **56** | **53** | **16** | **4** | **82** ✓ |

> Reconciliation: 56 + 53 + 16 + 4 = 129 program×offering-type rows, distributed across 82 distinct program entries (a program can offer Major + Minor + Joint Degree simultaneously). 82 UG + 101 grad = **183** total program entries = Rule-1 total = Rule-5 row count. ✓

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

All undergraduates at UChicago belong to **The College** — a single, unified undergraduate college. Academic administration is organized into four **Collegiate Divisions** (Biological Sciences, Physical Sciences, Social Sciences, Arts & Humanities), each chaired by a Master. Students declare a **major** housed in one of these divisions (or in an interdisciplinary committee). The distinctive **Core Curriculum** is shared by all students regardless of major. See the full hierarchy tree in Section 0.2.

Source: `https://college.uchicago.edu/academics/programs-study` — *"Complementing the breadth of UChicago's Core curriculum are 68 Majors & 57 Minors, as well as dozens of areas of specialized study and pre-professional preparation, all part of the UChicago undergraduate experience."*

### 1.2 Undergraduate majors/minors — grouped by Collegiate Division > offering type

> Each entry below is one accordion item on the official programs-of-study index. "Offered as" tags are verbatim from the page. Catalog URL is the authoritative `collegecatalog.uchicago.edu/thecollege/<slug>/` link extracted from each card.

#### Biological Sciences Collegiate Division

##### Major
| # | 专业 | Offered as | College Catalog URL |
|---|------|-----------|---------------------|
| 1 | Biological Chemistry | Major, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/biologicalchemistry |
| 2 | Biological Sciences | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/biologicalsciences/ |
| 3 | Neuroscience | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/neuroscience/ |

##### Minor (additional)
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Computational Neuroscience | http://collegecatalog.uchicago.edu/thecollege/computationalneuroscience/ |

##### Joint Degree
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Biological Chemistry (Joint BS/MS) | http://collegecatalog.uchicago.edu/thecollege/biologicalchemistry/#jointdegreeprogram |

> Note: Biological Sciences major offers **specializations** in Cancer Biology, Cellular & Molecular Biology, Computational Biology, Ecology & Evolution, Endocrinology, Genetics, Global Health Sciences, Immunology, Microbiology, Neuroscience, Quantitative Biology — these are the source of the College's "68 majors" count vs. the 56-entry extraction. See `biologicalsciences/#specializationprogramsinthebiologicalsciences`.

#### Physical Sciences Collegiate Division

##### Major
| # | 专业 | Offered as | Catalog URL |
|---|------|-----------|-------------|
| 1 | Astronomy and Astrophysics | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/astronomyastrophysics/ |
| 2 | Chemistry | Major, Minor, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/chemistry/ |
| 3 | Computational and Applied Mathematics | Major | http://collegecatalog.uchicago.edu/thecollege/caam/ |
| 4 | Computer Science | Major, Minor, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/computerscience/ |
| 5 | Data Science | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/geophysicalsciences/ |
| 6 | Environmental Science | Major | http://collegecatalog.uchicago.edu/thecollege/environmentalscience/ |
| 7 | Geographic Information Science | Major | http://collegecatalog.uchicago.edu/thecollege/geographicalstudies/ |
| 8 | Geophysical Sciences | Major | http://collegecatalog.uchicago.edu/thecollege/geophysicalsciences/ |
| 9 | Mathematics | Major, Minor, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/mathematics/ |
| 10 | Molecular Engineering | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/molecularengineering/ |
| 11 | Physics | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/physics/ |
| 12 | Statistics | Major, Minor, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/statistics/ |

##### Joint Degree
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Joint BS/MS in Chemistry | http://collegecatalog.uchicago.edu/thecollege/jointdegreechem/ |
| 2 | Joint BA/MS or BS/MS in Computer Science | http://collegecatalog.uchicago.edu/thecollege/jointdegreecomsci/ |
| 3 | Joint BA/MS or BS/MS in Mathematics | http://collegecatalog.uchicago.edu/thecollege/jointdegreemath/ |
| 4 | Joint BA/MS or BS/MS in Statistics | http://collegecatalog.uchicago.edu/thecollege/jointdegreestat/ |

#### Arts & Humanities Collegiate Division

##### Major
| # | 专业 | Offered as | Catalog URL |
|---|------|-----------|-------------|
| 1 | Art History | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/arthistory/ |
| 2 | Cinema and Media Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/cinemamediastudies/ |
| 3 | Classical Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/classicalstudies/ |
| 4 | Comparative Literature | Major | http://collegecatalog.uchicago.edu/thecollege/comparativeliterature/ |
| 5 | Creative Writing | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/creativewriting/ |
| 6 | East Asian Languages and Civilizations | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/eastasianlanguagescivilizations/ |
| 7 | English Language and Literature | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/englishlanguageliterature/ |
| 8 | Fundamentals: Issues and Texts | Major | http://collegecatalog.uchicago.edu/thecollege/fundamentalsissuesandtexts/ |
| 9 | Germanic Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/germanicstudies/ |
| 10 | Inquiry and Research in the Humanities | Major | http://collegecatalog.uchicago.edu/thecollege/Inquiryresearchhumanities/ |
| 11 | Jewish Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/jewishstudies/ |
| 12 | Law, Letters, and Society | Major | http://collegecatalog.uchicago.edu/thecollege/lawlettersandsociety/ |
| 13 | Linguistics | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/linguistics/ |
| 14 | Media Arts and Design | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/MediaArtsandDesign/ |
| 15 | Medieval Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/medievalstudies/ |
| 16 | Middle Eastern Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/neareasternlanguagescivilizations/ |
| 17 | Music | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/music/ |
| 18 | Philosophy | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/philosophy/ |
| 19 | Religious Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/religiousstudies/ |
| 20 | Romance Languages and Literatures | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/romancelanguagesliteratures/ |
| 21 | Russian and East European Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/slaviclanguagesliteratures/ |
| 22 | South Asian Languages and Civilizations | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/southasianlanguagescivilizations/ |
| 23 | Theater and Performance Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/theaterperformancestudies/ |
| 24 | Visual Arts | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/visualarts/ |

##### Minor (additional — not already a major above)
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Architectural Studies | http://collegecatalog.uchicago.edu/thecollege/arthistory/#minorinarchitecturalstudies |
| 2 | Digital Studies of Language, Culture, and History (also Joint Degree) | http://collegecatalog.uchicago.edu/thecollege/digitalstudies/ |
| 3 | Norwegian Studies | http://collegecatalog.uchicago.edu/thecollege/germanicstudies/#minorprograminnorwegianstudies |
| 4 | Renaissance Studies | http://collegecatalog.uchicago.edu/thecollege/renaissancestudies/ |
| 5 | Science Communication/Public Discourse | http://collegecatalog.uchicago.edu/thecollege/sciencecommunicationpublicdiscourse/ |
| 6 | Yiddish | http://collegecatalog.uchicago.edu/thecollege/yiddish/#minorprograminyiddishstudies |

##### Joint Degree
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Joint BA/MA in Digital Studies of Language, Culture, and History | http://collegecatalog.uchicago.edu/thecollege/digitalstudies/ |

#### Social Sciences Collegiate Division

##### Major
| # | 专业 | Offered as | Catalog URL |
|---|------|-----------|-------------|
| 1 | Anthropology | Major | http://collegecatalog.uchicago.edu/thecollege/anthropology/ |
| 2 | Cognitive Science | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/cognitivescience/ |
| 3 | Comparative Human Development | Major | http://collegecatalog.uchicago.edu/thecollege/comparativehumandevelopment/ |
| 4 | Economics | Major | http://collegecatalog.uchicago.edu/thecollege/economics/ |
| 5 | Environment, Geography, and Urbanization | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/cegu/ |
| 6 | Gender and Sexuality Studies | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/genderstudies/ |
| 7 | Global Studies | Major | http://collegecatalog.uchicago.edu/thecollege/globalstudies/ |
| 8 | History | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/history/ |
| 9 | History, Philosophy, and Social Studies of Science and Medicine | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/scienceandmedicinehips/ |
| 10 | Human Rights | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/humanrights/ |
| 11 | Latin American and Caribbean Studies | Major, Minor, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/latinamericanstudies/ |
| 12 | Political Science | Major | http://collegecatalog.uchicago.edu/thecollege/politicalscience/ |
| 13 | Psychology | Major | http://collegecatalog.uchicago.edu/thecollege/psychology/ |
| 14 | Public Policy Studies | Major, Joint Degree | http://collegecatalog.uchicago.edu/thecollege/publicpolicystudies/ |
| 15 | Race, Diaspora, and Indigeneity | Major, Minor | http://collegecatalog.uchicago.edu/thecollege/comparativeraceethnicstudies/ |
| 16 | Sociology | Major | http://collegecatalog.uchicago.edu/thecollege/sociology/ |

##### Minor (additional)
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Computational Social Science | http://collegecatalog.uchicago.edu/thecollege/computationalsocialscience/ |
| 2 | Democracy Studies | http://collegecatalog.uchicago.edu/thecollege/democracystudies/ |
| 3 | Education and Society | http://collegecatalog.uchicago.edu/thecollege/educationandsociety/ |
| 4 | Health and Society | http://collegecatalog.uchicago.edu/thecollege/healthandsociety/ |
| 5 | Inequality, Social Problems and Change | http://collegecatalog.uchicago.edu/thecollege/inequalityandsocialchange/ |
| 6 | Quantitative Social Analysis | http://collegecatalog.uchicago.edu/thecollege/quantitativesocialanalysis/ |

##### Joint Degree
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Joint BA/MA in Latin American and Caribbean Studies | http://collegecatalog.uchicago.edu/thecollege/jointdegreelacs/ |
| 2 | Joint BA/MPP in Public Policy Studies (Harris) | http://collegecatalog.uchicago.edu/thecollege/jointdegreeppha/ |

#### Interdisciplinary / Pre-Professional / Joint with Graduate Schools

##### Major
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Climate and Sustainable Growth | http://collegecatalog.uchicago.edu/thecollege/climate/ |

##### Minor
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Entrepreneurship and Innovation (Booth) | http://collegecatalog.uchicago.edu/thecollege/entrepreneurshipandinnovation/ |

##### Joint Degree (4+1 / 5-year BA-MA / BA-MS)
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Joint BA/MA in International Relations (CIR) | http://collegecatalog.uchicago.edu/thecollege/internationalrelations/ |
| 2 | Joint BA/MA in Middle Eastern Studies (CMES) | http://collegecatalog.uchicago.edu/thecollege/jointdegreecmes/ |
| 3 | Joint BA/MA in Social Service Administration (Crown) | http://collegecatalog.uchicago.edu/thecollege/jointdegreessa/ |
| 4 | Joint BA/MA in the Humanities (MAPH) | http://collegecatalog.uchicago.edu/thecollege/jointdegreehumanities/ |
| 5 | Joint BA/MA in the Social Sciences (MAPSS) | http://collegecatalog.uchicago.edu/thecollege/jointdegreesocsci/ |
| 6 | Joint BA/MAT in Education and Teaching Certification (UTEP) | http://collegecatalog.uchicago.edu/thecollege/utep/ |
| 7 | Joint BA/MS in Computational Analysis and Public Policy (Harris) | http://collegecatalog.uchicago.edu/thecollege/jointdegreepphams/ |
| 8 | Professional Option: Medicine (BA + MD pathway) | http://collegecatalog.uchicago.edu/thecollege/professionaloptionmedicine/ |

##### Interdisciplinary (academic opportunities)
| # | 专业 | Catalog URL |
|---|------|-------------|
| 1 | Big Problems | http://collegecatalog.uchicago.edu/thecollege/bigproblems/ |
| 2 | Chicago Studies | http://collegecatalog.uchicago.edu/thecollege/chicagostudies/ |
| 3 | Clinical and Translational Science | http://collegecatalog.uchicago.edu/thecollege/collegeccts/ |
| 4 | Institute for the Formation of Knowledge | http://collegecatalog.uchicago.edu/thecollege/stevanovichinstitute/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

See Section 1.2 "Interdisciplinary / Pre-Professional" group above. The College also offers **UChicago Careers In** programs (Business, Engineering, Gaming, Healthcare, Law, Physical Sciences, Education Professions, Climate & Energy Careers) and pre-professional preparation tracks; these are advisement pathways rather than degree-granting programs and are not counted in Rule 1.

### 1.4 Minors — complete list

All 53 minor offerings appear in Section 1.2 under their home Collegiate Division (a program offering both a Major and a Minor lists its Minor in the same row). Standalone minors (not paired with a UG major at UChicago): Architectural Studies, Computational Neuroscience, Computational Social Science, Democracy Studies, Digital Studies, Education and Society, Entrepreneurship and Innovation, Geographic Information Science (GIS), Health and Society, Inequality/Social Problems and Change, Norwegian Studies, Quantitative Social Analysis, Renaissance Studies, Science Communication/Public Discourse, Yiddish.

### 1.5 Core Curriculum (UChicago's distinctive general education)

UChicago's **Core Curriculum** is the foundational common program required of all College students regardless of major. Eight components across six subject areas plus writing and language:

| Core Area | Components |
|-----------|-----------|
| Arts | (1 course) |
| Humanities | (3 courses: HUMA 1-3 sequence) |
| Civilization Studies | (2-3 courses; civilization sequence) |
| Social Sciences | (3 courses: SOSC sequence) |
| Biological Sciences | (2-3 courses; BIOS sequence) |
| Physical Sciences | (2-3 courses; PHSC sequence) |
| Mathematical Sciences | (1-2 courses; MATH/STAT) |
| Writing | (integrated in Humanities & Social Sciences Core) |
| Language Competence | (demonstrate competence in a language other than English) |

Source: `https://college.uchicago.edu/academics/core-curriculum` — *"The University of Chicago's Core curriculum provides all College students with a challenging, common academic program that serves as a foundation for coursework in major fields of study—and for a lifetime of intellectual inquiry."*

### 1.6 Program numbering scheme

UChicago does NOT use a Course-ID → Major numbering scheme (unlike MIT's "Course 6" system). Programs are identified by name and housed under their Collegiate Division or interdisciplinary committee. Course numbers (e.g., MATH 16100, BIOS 20198) are per-course, not per-program.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

Source: `https://grad.uchicago.edu/admissions/programs/` — *"101 Available Programs"*. Each program card lists the degree(s) offered and the home division/school. Grouped below by division, then by Master's vs Doctoral. (URL is the program's departmental/program site from the card.)

#### Biological Sciences Division (21 programs + 1 joint)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Informatics | MS in Biomedical Informatics | https://bmi.bsd.uchicago.edu/ |
| 2 | Biomedical Sciences | MS (MSBS) | https://www.biomedicalsciences.bsd.uchicago.edu/ |
| 3 | Precision Health | MS (MSPH) | https://precisionhealth.bsd.uchicago.edu/ |
| 4 | Public Health | MPH, MS (Public Health Science) | https://pbhs.uchicago.edu/ |
| 5 | Threat and Response Management | MS in Threat and Response Management | https://threatresponse.bsd.uchicago.edu/ |

##### Doctoral (PhD, MD/PhD)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biochemistry and Molecular Biophysics | PhD | https://bcmb.uchicago.edu/ |
| 2 | Cancer Biology | PhD | https://biomedsciences.uchicago.edu/page/committee-cancer-biology |
| 3 | Cell and Molecular Biology | PhD | https://camb.uchicago.edu/ |
| 4 | Computational Neuroscience | PhD | https://cns.uchicago.edu/ |
| 5 | Development, Regeneration, and Stem Cell Biology | PhD | https://drsb.uchicago.edu/ |
| 6 | Ecology and Evolution | PhD | https://eegraduate.uchicago.edu/ |
| 7 | Evolutionary Biology | PhD | https://evbio.uchicago.edu/ |
| 8 | Genetics, Genomics, and Systems Biology | PhD | https://ggsb.uchicago.edu/ |
| 9 | Human Genetics | PhD | https://hgen.uchicago.edu/ |
| 10 | Immunology | PhD | https://biomedsciences.uchicago.edu/page/committee-immunology-0 |
| 11 | Integrative Biology | PhD | https://integbio.uchicago.edu/ |
| 12 | Interdisciplinary Scientist Training Program (ISTP) | MD/PhD | https://pritzker.uchicago.edu/mstp-program-overview |
| 13 | Medical Physics | PhD | http://medicalphysics.uchicago.edu/ |
| 14 | Microbiology | PhD | https://micro.uchicago.edu/ |
| 15 | Molecular Metabolism and Nutrition | PhD | https://biomedsciences.uchicago.edu/page/molecular-metabolism-and-nutrition |
| 16 | Neurobiology | PhD | https://neurograd.uchicago.edu/ |
| 17 | Public Health | PhD (Public Health Sciences) | https://pbhs.uchicago.edu/ |

##### Joint BSD × PSD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biophysical Sciences | PhD (jointly BSD & PSD) | https://biophysics.uchicago.edu/ |

#### Physical Sciences Division (12 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Data Science | MS (Analytics) | https://datascience.uchicago.edu/education/masters-programs/ms-in-applied-data-science/ |
| 2 | Chemistry | MS (Chemistry) | https://chemistry.uchicago.edu/ |
| 3 | Computational and Applied Mathematics | Master's (CAAM) | https://cam.uchicago.edu/ |
| 4 | Computer Science | MPCS (MS) | https://cs.uchicago.edu/ |
| 5 | Data Science | MS Data Science | https://codas.uchicago.edu/ |
| 6 | Environmental Science | MS in Environmental Science | https://geosci.uchicago.edu/academics/ms-in-environmental-sciences/ |
| 7 | Financial Mathematics | MS (Fin Math) | http://finmath.uchicago.edu/ |
| 8 | Statistics | MS Statistics | https://stat.uchicago.edu/ |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Astronomy and Astrophysics | PhD | https://astro.uchicago.edu/index.php |
| 2 | Chemistry | PhD | https://chemistry.uchicago.edu/ |
| 3 | Computational and Applied Mathematics | PhD (Computational Mathematics) | https://cam.uchicago.edu/ |
| 4 | Computer Science | PhD | https://cs.uchicago.edu/ |
| 5 | Data Science | PhD | https://codas.uchicago.edu/ |
| 6 | Geophysical Sciences | PhD | https://geosci.uchicago.edu/ |
| 7 | Mathematics | PhD | https://math.uchicago.edu/ |
| 8 | Physics | PhD | https://physicsrecruitment.psd.uchicago.edu/ |
| 9 | Statistics | PhD | https://stat.uchicago.edu/ |

#### Social Sciences Division (12 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | MAPSS (MA) | https://anthropology.uchicago.edu/ |
| 2 | Committee on Conceptual and Historical Studies of Science (CHSS) | MAPSS (MA) | https://chss.uchicago.edu/ |
| 3 | Comparative Human Development | MAPSS (MA) | https://humdev.uchicago.edu/ |
| 4 | Computational Social Science | MACSS (MA) | https://macss.uchicago.edu/ |
| 5 | Economics (SSD) | MA (Economics) | https://economics.uchicago.edu/ |
| 6 | History | MAPSS (MA) | https://history.uchicago.edu/ |
| 7 | International Relations (CIR) | MA CIR | https://cir.uchicago.edu/ |
| 8 | Master of Arts Program in the Social Sciences (MAPSS) | MA | https://mapss.uchicago.edu/ |
| 9 | Political Science | MAPSS (MA) | https://political-science.uchicago.edu/ |
| 10 | Psychology | MAPSS (MA) | https://psychology.uchicago.edu/ |
| 11 | Social Thought | MAPSS (MA) | https://socialthought.uchicago.edu/ |
| 12 | Sociology | MAPSS (MA) | https://sociology.uchicago.edu/ |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | PhD | https://anthropology.uchicago.edu/ |
| 2 | Committee on Conceptual and Historical Studies of Science | PhD (CHSS) | https://chss.uchicago.edu/ |
| 3 | Comparative Human Development | PhD (CHD) | https://humdev.uchicago.edu/ |
| 4 | Economics (SSD) | PhD (Economics) | https://economics.uchicago.edu/ |
| 5 | History | PhD | https://history.uchicago.edu/ |
| 6 | International Relations | PhD (Political Science) | https://cir.uchicago.edu/ |
| 7 | Political Science | PhD | https://political-science.uchicago.edu/ |
| 8 | Psychology | PhD | https://psychology.uchicago.edu/ |
| 9 | Social Thought | PhD | https://socialthought.uchicago.edu/ |
| 10 | Sociology | PhD | https://sociology.uchicago.edu/ |

#### Arts & Humanities Division (18 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | MAPH (MA) | https://arthistory.uchicago.edu/ |
| 2 | Cinema and Media Studies | MAPH (MA) | https://cms.uchicago.edu/ |
| 3 | Classics | MAPH (MA) | https://classics.uchicago.edu/ |
| 4 | Committee on Theater and Performance Studies | MAPH (MA) | https://taps.uchicago.edu/ |
| 5 | Comparative Literature | MAPH (MA) | https://complit.uchicago.edu/ |
| 6 | Digital Studies of Language, Culture, and History | MA | https://digitalstudies.uchicago.edu/ |
| 7 | East Asian Languages and Civilizations | MAPH (MA) | https://ealc.uchicago.edu/ |
| 8 | English Language and Literature | MAPH (MA) | https://english.uchicago.edu/ |
| 9 | Germanic Studies | MAPH (MA) | https://german.uchicago.edu/ |
| 10 | Linguistics | MAPH (MA) | https://linguistics.uchicago.edu/ |
| 11 | Master of Arts Program in the Humanities (MAPH) | MA | https://maph.uchicago.edu/ |
| 12 | Middle Eastern Studies | MA-CMES | https://mes.uchicago.edu/ |
| 13 | Music | MAPH (MA) | https://music.uchicago.edu/ |
| 14 | Philosophy | MAPH (MA) | http://philosophy.uchicago.edu/ |
| 15 | Romance Languages and Literatures | MAPH (MA) | https://rll.uchicago.edu/ |
| 16 | Slavic Languages and Literatures | MAPH (MA) | https://slavic.uchicago.edu/ |
| 17 | South Asian Languages and Civilizations | MAPH (MA) | http://salc.uchicago.edu/ |
| 18 | Visual Arts | MFA | https://dova.uchicago.edu/ |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | PhD | https://arthistory.uchicago.edu/ |
| 2 | Cinema and Media Studies | PhD | https://cms.uchicago.edu/ |
| 3 | Classics | PhD | https://classics.uchicago.edu/ |
| 4 | Committee on Theater and Performance Studies | PhD (Joint Degree Only) | https://taps.uchicago.edu/ |
| 5 | Comparative Literature | PhD | https://complit.uchicago.edu/ |
| 6 | East Asian Languages and Civilizations | PhD | https://ealc.uchicago.edu/ |
| 7 | English Language and Literature | PhD | https://english.uchicago.edu/ |
| 8 | Germanic Studies | PhD | https://german.uchicago.edu/ |
| 9 | Linguistics | PhD | https://linguistics.uchicago.edu/ |
| 10 | Middle Eastern Studies | PhD | https://mes.uchicago.edu/ |
| 11 | Music | PhD | https://music.uchicago.edu/ |
| 12 | Philosophy | PhD | http://philosophy.uchicago.edu/ |
| 13 | Romance Languages and Literatures | PhD | https://rll.uchicago.edu/ |
| 14 | Slavic Languages and Literatures | PhD | https://slavic.uchicago.edu/ |
| 15 | South Asian Languages and Civilizations | PhD | http://salc.uchicago.edu/ |

#### Divinity School (12 programs)

##### Master's (MA, MA in Religious Studies, MDiv)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology and Sociology of Religion | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/religion-and-human-sciences/anthropology-and-sociology-religions |
| 2 | Bible (Hebrew Bible, New Testament) | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/historical-studies-religion/bible |
| 3 | History of Christianity | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/historical-studies-religion/history-christianity |
| 4 | History of Judaism | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/historical-studies-religion/history-judaism |
| 5 | Islamic Studies | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/islamic-studies |
| 6 | Master of Divinity | MDiv | https://divinity.uchicago.edu/admissions/MDivprogram |
| 7 | Philosophy of Religions | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/constructive-studies-religion/philosophy-religions |
| 8 | Religion, Literature, and Visual Culture | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/religion-and-human-sciences/religion-literature-and-visual-culture |
| 9 | Religions in America | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/religions-americas |
| 10 | Religious Ethics | MA (Divinity), MA (Religious Studies) | https://divinity.uchicago.edu/academics/areas-study/constructive-studies-religion/religious-ethics |
| 11 | Religious Studies | MA (Divinity), MA (Religious Studies), MDiv | https://divinity.uchicago.edu/MA-AMRS-programs |
| 12 | Theology | MA (Divinity), MA (Religious Studies), MDiv | https://divinity.uchicago.edu/academics/areas-study/constructive-studies-religion/theology |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1-11 | (same 11 areas of study as Master's, except MDiv is master's-only) | PhD (Divinity) | (see Master's URLs above) |

#### Chicago Booth School of Business (8 programs)

##### Master's (MBA, Master of Finance, Master of Management)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting | MBA | https://www.chicagobooth.edu/ |
| 2 | Behavioral Science | MBA | https://www.chicagobooth.edu/ |
| 3 | Business | MBA | https://www.chicagobooth.edu/ |
| 4 | Econometrics and Statistics | MBA | https://www.chicagobooth.edu/ |
| 5 | Economics (Booth) | MBA | https://www.chicagobooth.edu/ |
| 6 | Finance | MBA, Master of Finance | https://www.chicagobooth.edu/ |
| 7 | Management Science/Operations Management | MBA, Master of Management | https://www.chicagobooth.edu/ |
| 8 | Marketing | MBA | https://www.chicagobooth.edu/ |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1-8 | (same 8 fields as Master's) | PhD (Business) | https://www.chicagobooth.edu/programs/phd |

> Booth also offers the **Full-Time MBA, Evening MBA, Weekend MBA, Executive MBA**, and **Master in Management** — these are delivery formats of the MBA rather than separate directory entries.

#### Harris School of Public Policy (3 programs + 1 joint)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Computational Analysis and Public Policy | MSCAPP (MS) | https://harris.uchicago.edu/academics/programs-degrees/degrees/ms-computational-analysis-and-public-policy-mscapp |
| 2 | Public Policy | MA (Evening), MA (Public Policy), MPP | https://harris.uchicago.edu/academics/degrees |
| 3 | Public Policy with Certificate in Research Methods | MACRM (MA) | https://harris.uchicago.edu/academics/programs-degrees/degrees/ma-public-policy-certificate-research-methods-macrm |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Public Policy | PhD (Public Policy) | https://harris.uchicago.edu/academics/degrees |

##### Joint Harris × SSD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Economy | MAPSS (MA), PhD (PE) | https://politicaleconomy.uchicago.edu/ |

#### Pritzker School of Medicine (3 programs)

##### Doctoral / Professional
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Medical Doctor | MD | https://pritzker.uchicago.edu/ |
| 2 | Medical Scientist Training Program (MSTP) | MD/PhD | https://pritzker.uchicago.edu/page/mstp-medical-scientist-training-program |
| 3 | Medicine, the Social Sciences, and the Humanities (MESH) | MD/PhD | https://pritzker.uchicago.edu/page/md-phd-programs-medicine-social-sciences-and-humanities |

#### Pritzker School of Molecular Engineering (3 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Engineering | MEng | https://pme.uchicago.edu/academics/masters-of-engineering |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Molecular Engineering | PhD | https://pme.uchicago.edu/phd-programs/molecular-engineering |
| 2 | Quantum Science and Engineering | PhD | https://pme.uchicago.edu/phd-programs/quantum-science-and-engineering |

#### Crown Family School of Social Work, Policy, and Practice (2 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Sector Leadership and Nonprofit Management | MA (SSL) | https://crownschool.uchicago.edu/academic-programs/curriculum-maps/social-sector-leadership-and-nonprofit-management-ssl-full-time |
| 2 | Social Work, Social Policy, and Social Administration | MA (A.M. in Social Work) | https://crownschool.uchicago.edu/academic-programs/masters-social-work |

##### Doctoral
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Social Work, Social Policy, and Social Administration | PhD (Social Work) | https://crownschool.uchicago.edu/academic-programs/masters-social-work |

#### Law School (4 programs)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Law/Legal Studies | LLM (Master of Laws), MLS (Master of Legal Studies) | https://www.law.uchicago.edu/ |

##### Doctoral / Professional
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor | JD | https://www.law.uchicago.edu/jd-program |
| 2 | Doctor of Jurisprudence | JSD | https://www.law.uchicago.edu/jsd-program |
| 3 | Doctor of Comparative Law | D.Comp.L | https://www.law.uchicago.edu/jsd-program/features |

#### Graham School of Continuing Liberal and Professional Studies (1 program)

##### Master's
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Liberal Arts | Master of Liberal Arts (MLA) | https://masterliberalarts.uchicago.edu/ |

### 2.2 Worked example — full deep-dive: Economics PhD (Social Sciences Division)

The largest and most-applied-to doctoral program at UChicago's SSD:

- **Department**: Kenneth C. Griffin Department of Economics
- **Division**: Social Sciences Division
- **Degrees offered**: MA (Economics), PhD (Economics)
- **Departmental site**: https://economics.uchicago.edu/content/undergraduate-program (UG) / graduate via PhD program
- **Catalog**: http://collegecatalog.uchicago.edu/thecollege/economics/ (UG); PhD admissions via department
- **Application portal**: UChicago Graduate Application (division-managed)
- **Application fee**: ~$90 (varies; fee waiver available — see grad.uchicago.edu/admissions/apply/fee-waivers/)
- **Standardized tests**: GRE required for PhD Economics (Booth MBA uses GMAT/GRE)
- **Application deadline**: Mid-December (typically Dec 15) for PhD; verify on department site
- **Funding**: PhD students fully funded (tuition + stipend); MA programs generally self-funded

### 2.3 Graduate admissions model — **DEcentralized**

> Source: `https://grad.uchicago.edu/admissions/apply/` — *"All programs at the University of Chicago offer an online application system, but each school and division has its own application."*

Graduate admissions at UChicago is **highly decentralized**. UChicagoGRAD is a central *services* office (fellowships, career development, academic support) but does NOT make admissions decisions. Each of the 12 graduate divisions/schools runs its own application, sets its own deadlines, and decides its own admissions:

- **Booth School of Business** — manages its own admissions platform (independent of UChicagoGRAD)
- **Law School** — applies through **LSAC**
- **Pritzker School of Medicine** — applies through **AMCAS**
- **All other divisions** (BSD, PSD, SSD, A&H, Divinity, Harris, Crown, Graham, PME) — coordinated through the Graduate Admissions office but each has its own online application
- **Advanced Scholars Program** — early master's application for current college juniors/seniors at other institutions, for select programs at BSD, Booth, Harris, PSD, PME

> *"To apply to multiple programs, you will need to create a unique application for each one."*

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| UG 招生网站 | https://collegeadmissions.uchicago.edu/apply/ | E-U-001 |
| 申请平台 | Common Application **或** Apply Coalition (powered by Scoir) — 二选一，同等对待 | E-U-002 |
| UChicago Account | 必须创建 (getstarted.uchicago.edu)；接收申请、上传材料、查看录取结果 | E-U-002 |
| **Early Decision I 截止** | **Nov 2, 2026** (绑定；结果 mid-December；回复 mid-January) | E-U-003 |
| **Early Action 截止** | **Nov 2, 2026** (非绑定；结果 mid-December；回复 May 1) | E-U-003 |
| **Early Decision II 截止** | **Jan 4, 2027** (绑定；结果 mid-February；回复 mid-March) | E-U-003 |
| **Regular Decision 截止** | **Jan 4, 2027** (结果 late March；回复 May 1) | E-U-003 |
| 申请费 | **$90**（不申请 need-based aid 者）；申请 need-based aid 者 **免申请费** | E-U-004 |
| 费用豁免 | 申请 need-based aid 自动免申请费；其他可申请 fee waiver | E-U-004 |
| SAT/ACT 政策 | **Test-optional ("No Harm" policy)** — 提交 SAT/ACT 为可选；不提交不影响录取 | E-U-005 |
| 自报分数 | 接受 self-reported scores；录取后才需官方成绩单 | E-U-005 |
| Superscore | UChicago 自行 superscore，学生无需自行计算 | E-U-005 |
| 测试截止 | EA/ED I: 接受 10月 ACT + 11月 SAT；ED II/RD: 接受 12月 SAT/ACT | E-U-005 |
| 推荐信 | **2 封教师推荐信**（学术科目教师）+ 1 封 counselor 推荐 (Secondary School Report)；可加 1 封补充推荐 | E-U-006 |
| 成绩单 | Secondary School Report + 官方成绩单（接受 self-submitted）；2月1日前提交 midyear report | E-U-006 |
| 面试 | **无正式面试**；可选 Video Profile (推荐)；可选 InitialView (国际生) | E-U-007 |
| 补充材料 | 可选艺术/创作/研究补充材料；Essay prompts (UChicago Supplement — 1 篇 extended + 1 篇 why UChicago) | E-U-007 |
| 录取入学时间 | 仅秋季入学 (Autumn Quarter)；除 at-large students 外 | E-U-002 |
| Transfer 通道 | 单独 transfer 申请；国际 transfer **无 financial aid** | E-U-008 |

### 3.2 Undergraduate English proficiency table

> Source: `https://collegeadmissions.uchicago.edu/apply/international-applicants/` — *"Students are invited to submit scores from any English proficiency examination they choose."*

**重要**: UChicago UG **不公布 TOEFL/IELTS 最低分**，也不限定接受哪种英语考试——学生可"提交任何英语能力考试的成绩"。这与多数同行院校不同。无 ESL 项目。

| 考试 | 最低分 (Minimum) | 推荐分 (Recommended) | 接受状态 |
|------|------------------|---------------------|---------|
| TOEFL iBT | 未公布 | 未公布 | 接受（接受官方或自报） |
| IELTS Academic | 未公布 | 未公布 | 接受 |
| Duolingo English Test | 未公布 | 未公布 | 接受（未排除） |
| Cambridge English | 未公布 | 未公布 | 接受（未排除） |
| PTE Academic | 未公布 | 未公布 | 接受（未排除） |
| InitialView 面试 | N/A | 推荐 (国际生可选) | 接受为补充材料 |

> 适用条件：英语非母语、且未在英语授课学校完成足够年限学习的申请人。"The University of Chicago only admits students who have demonstrated a superior level of English language competence."

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 录取模式 | **去中心化** — 12 个研究生院/学部各自独立录取、各自申请系统 | E-G-001 |
| 申请平台 | 各 division 独立 (Booth 自有平台；Law 用 LSAC；Med 用 AMCAS；其余走 UChicago Graduate Application) | E-G-001 |
| 申请费 | 各 division 自定（通常 $90-$250；Booth MBA ~$250；Law ~$85；Med AMCAS + 二级）；fee waiver 可申请 | E-G-002 |
| GRE/GMAT 政策 | 因项目而异 — 多数 PhD 要求 GRE；Booth 接受 GMAT/GRE；Law 用 LSAT；Med 用 MCAT | E-G-003 |
| 4月15日荣誉决议 | UChicago 遵守 CGS April 15 Resolution（PhD 录取回复截止） | E-G-004 |
| 英语能力政策 | **仅接受 TOEFL iBT 或 IELTS Academic**（不接受 Duolingo/IELTS Indicator/TOEFL ITP Plus） | E-G-005 |
| 英语豁免条件 | (a) 英语为母语/自幼主要教学语言；或 (b) 过去 10 年内在指定英语国家/地区全日制学位项目就读满 1 学年 | E-G-005 |
| TOEFL 有效期 | 2 年（截至申请截止日） | E-G-005 |
| ETS 学校代码 (GRE/TOEFL) | **1832**（除 Booth 外所有项目） | E-G-006 |
| ETS 代码 — Booth MBA | **1832-02** | E-G-006 |
| ETS 代码 — Booth PhD | **1819** | E-G-006 |
| IELTS 电子下载 | University of Chicago – Graduate Enrollment, 970 East 58th Street, Third Floor, Chicago, IL 60637 | E-G-006 |
| 例外项目 | Booth / Law / Pritzker (Med) / MA in Economics / Advanced Scholars Program — 有各自独立的英语政策 | E-G-005 |
| 成绩单 | 申请时上传非官方成绩单；录取后才需官方；非英文须附认证翻译 | E-G-007 |
| 国际生特殊要求 | 无单独国际生要求；所有申请人须满足英语能力要求 | E-G-007 |
| 申请截止 | 因项目而异 — PhD 通常 12月中旬；Master's 通常 1月-3月；详见各项目页面 | E-G-008 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027, line-itemized)

> Source: `https://financialaid.uchicago.edu/undergraduate/costs` — *"Cost of Attendance for 2026-2027"*

| Expense item | On-Campus | Commuter | Off-Campus | Description |
|--------------|-----------|----------|------------|-------------|
| Tuition | $75,960 | $75,960 | $75,960 | 年学费（统一） |
| Student Services Fee | $1,677 | $1,677 | $1,677 | 学生服务费 |
| UPASS Fee | $318 | $318 | $318 | 公交通行费 |
| Food & Housing (or Maintenance Allowance) | $21,414 | $9,000 (maintenance) | $18,000 | 食宿 |
| Books & Course Materials | $1,800 | $1,800 | $1,800 | 书本及课程材料 |
| Misc. Personal Expenses | $1,950 | $1,950 | $1,950 | 个人杂费 |
| Travel Allowance | $702 | $702 | $702 | 交通津贴 |
| **TOTAL** | **$103,821** | **$91,407** | **$100,407** | **总就读成本** |

**Notes (verbatim from page):**
- *"Students enrolling at UChicago for the first time in 2026 will be assessed a Class Fee of $720 in each of their first two years."*
- *"Health insurance is not included in the cost figures above."* (U-SHIP health insurance separate; see wellness.uchicago.edu/student-insurance/u-ship/)
- *"Food & Housing is based on the average student room cost and the Unlimited meal plan."*

### 4.2 Undergraduate financial-aid policy

> Source: `https://collegeadmissions.uchicago.edu/financial-support/financial-overview/`

| 政策维度 | UChicago 政策 | 来源 |
|---------|--------------|------|
| 100% need-met | ✅ 满足 100% demonstrated need，全部以 **grant**（无需偿还）形式，**无贷款** | E-U-009 |
| Loan-free | ✅ "Families are not expected to take out loans to finance their college expenses." | E-U-009 |
| 免学费门槛 | **家庭年收入 < $250,000** → 免学费 (Free Tuition) | E-U-009 |
| 申请费 | 申请 need-based aid 的学生 **免申请费** | E-U-004 |
| 美国公民/永久居民 | Need-blind；100% need-met | E-U-009 |
| 国际生（首次入学大一） | **Need-aware**（申请 aid 影响录取考量）但 **被录取者 100% need-met**；同时可申请 merit-based奖学金 | E-U-010 |
| 国际生 Transfer | **无 financial aid 可用** — 须自行全额资助 | E-U-010 |
| Undocumented/DACA | 视同美国公民申请 need-based aid（UChicago 是少数对无证学生提供 need-based aid 的大学） | E-U-011 |
| Merit-based 奖学金 | 所有学生自动考虑（无需单独申请）；部分学费奖学金 | E-U-009 |
| Odyssey Scholarship | 面向获得 guaranteed free tuition 的学生及初代大学生 | E-U-009 |
| 总援助规模 | UChicago 每年提供 **>$225 million** financial support；国际生过去 4 年获 ~$20M need-based aid + $35M 新捐赠 | E-U-010 |

> **Critical distinction from peer schools**: UChicago 是 **need-aware for international first-year applicants**（不同于 MIT / Harvard / Yale / Princeton / Dartmouth / Amherst / Brown，这些学校对国际生 need-blind）。但被录取的国际生仍 100% need-met, loan-free。这意味着申请 aid 的国际生录取竞争更激烈。

### 4.3 Graduate cost & funding framework

> Source: `https://grad.uchicago.edu/admissions/funding/`

| 维度 | 政策 |
|------|------|
| PhD 资助模式 | 多数 PhD 项目 **fully funded** — 全额学费 + stipend（通常通过 fellowship + RA/TA） |
| Master's 资助模式 | 多数 Master's 项目 **self-funded**；部分有 merit-based fellowship；少有 full funding |
| 常见资助形式 | University Fellowship、RA (Research Assistantship)、TA (Teaching Assistantship)、外部 fellowship |
| 申请费 | 各项目自定（典型 $90-$250）；fee waiver 可申请 (grad.uchicago.edu/admissions/apply/fee-waivers/) |
| Fee waiver 政策 | 提交申请后在 portal 申请；批准前勿付费（不退款） |

> **P0 follow-up**: 各 PhD 项目的具体 stipend 金额 (典型 BSD/PSD ~$45k-$50k/yr) 及各 division 的 cost-of-attendance 页面未在本轮抓取。下次运行应访问 grad.uchicago.edu/admissions/funding/ 及各 division 财务页面。

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001
field: undergraduate.admissions.site
value: https://collegeadmissions.uchicago.edu/apply/
source_url: https://collegeadmissions.uchicago.edu/apply/
source_snippet: "At UChicago, you are more than just a number... We care about you and who you really are"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-002
field: undergraduate.application.platforms
value: Common Application OR Apply Coalition (powered by Scoir); UChicago Account required
source_url: https://collegeadmissions.uchicago.edu/apply/application/required-materials/
source_snippet: "UChicago accepts Apply Coalition, Powered by Scoir or the Common Application. We treat both equally in the admissions process... Applicants will also be prompted to create a UChicago Account"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-003
field: undergraduate.deadlines.2026_2027_cycle
value: "ED I = Nov 2 2026; EA = Nov 2 2026; ED II = Jan 4 2027; RD = Jan 4 2027"
source_url: https://collegeadmissions.uchicago.edu/apply/
source_snippet: "Early Decision I — APPLICATION DEADLINE Nov 2, 2026 / DECISION DATE Mid-December / REPLY DATE Mid-January | Early Action — Nov 2, 2026 / Mid-December / May 1st | Early Decision II — Jan 4, 2027 / Mid-February / Mid-March | Regular Decision — Jan 4, 2027 / Late March / May 1st"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-004
field: undergraduate.application.fee
value: "$90 (waived for need-based aid applicants)"
source_url: https://collegeadmissions.uchicago.edu/apply/application/required-materials/
source_snippet: "The University of Chicago does not charge an application fee for students applying for need-based financial aid. For students not applying for need-based financial aid, our application fee is $90"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-005
field: undergraduate.testing.policy
value: "Test-optional ('No Harm'); self-reported accepted; superscored by UChicago"
source_url: https://collegeadmissions.uchicago.edu/apply/application/required-materials/
source_snippet: "Submitting an SAT or ACT is optional and not required for admission. In addition to being test-optional, UChicago practices a 'No Harm' policy for application review when considering SAT or ACT scores... Students submitting SAT or ACT scores may share either official or self-reported scores."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-006
field: undergraduate.materials.recommendations_transcript
value: "Two teacher evaluations + Secondary School Report + transcript + midyear report (Feb 1)"
source_url: https://collegeadmissions.uchicago.edu/apply/application/required-materials/
source_snippet: "We require two recommendations from teachers who have taught you in an academic subject... Ask your secondary school counselor to complete the Secondary School Report and to submit it along with an official transcript... Please have your high school counselor submit a midyear report with grades... by February 1"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-007
field: undergraduate.materials.optional
value: "Optional Video Profile (recommended); optional supplemental art/creative/research materials; UChicago Supplement (1 extended essay + 1 why-UChicago essay)"
source_url: https://collegeadmissions.uchicago.edu/apply/application/optional-materials/
source_snippet: "Recommended Video Profile ➔ | Supplemental Materials: Optional Art, Creative, Research, or... ➔"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-008
field: undergraduate.transfer.policy
value: "Separate transfer application; international transfer students have NO financial aid available"
source_url: https://collegeadmissions.uchicago.edu/financial-support/international-financial-aid/
source_snippet: "Financial aid is not available to international transfer applicants, and international transfer students must be able to document that they are able to fully finance their education at UChicago."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-009
field: undergraduate.financial_aid.policy
value: "100% need-met, loan-free (all grants); free tuition for families earning <$250k/yr; >$225M annual aid"
source_url: https://collegeadmissions.uchicago.edu/financial-support/financial-overview/
source_snippet: "UChicago meets 100% of demonstrated need in the form of grants (which do not need to be repaid) instead of loans for all families... Families earning less than $250,000 per year receive free tuition to UChicago... UChicago provided over $225 million in financial support to its students"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-010
field: undergraduate.financial_aid.international
value: "International first-year: need-aware but 100% need-met if admitted; ~$20M aid over 4 yrs + $35M new gift; intl transfer: NO aid"
source_url: https://collegeadmissions.uchicago.edu/financial-support/international-financial-aid/
source_snippet: "Nearly $20 million in need-based financial aid has been offered to international students at UChicago over the past four years, and a recent gift of $35 million for international financial aid has strengthened the University's commitment... International students should apply for financial aid at the time they apply to UChicago"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-011
field: undergraduate.financial_aid.undocumented
value: "Undocumented/DACA students considered for need-based aid same as citizens"
source_url: https://collegeadmissions.uchicago.edu/financial-support/financial-overview/
source_snippet: "All students who apply, regardless of citizenship and including undocumented students, are considered for admission... UChicago meets 100% of demonstrated need"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-012
field: undergraduate.cost.2026_2027
value: "Tuition $75,960; Total On-Campus $103,821; Commuter $91,407; Off-Campus $100,407"
source_url: https://financialaid.uchicago.edu/undergraduate/costs
source_snippet: "Cost of Attendance for 2026-2027 | Tuition $75,960 | Student Services Fee $1,677 | UPASS Fee $318 | Food & Housing $21,414 | Books $1,800 | Misc Personal $1,950 | Travel $702 | TOTAL $103,821 (On-Campus)"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-013
field: undergraduate.programs.counts
value: "82 program-of-study entries = 56 majors + 53 minors + 16 joint degrees + 4 interdisciplinary (official headline: 68 majors & 57 minors)"
source_url: https://college.uchicago.edu/academics/programs-study
source_snippet: "Complementing the breadth of UChicago's Core curriculum are 68 Majors & 57 Minors, as well as dozens of areas of specialized study and pre-professional preparation, all part of the UChicago undergraduate experience."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-014
field: undergraduate.core_curriculum
value: "8 components across 6 subject areas + writing + language competence"
source_url: https://college.uchicago.edu/academics/core-curriculum
source_snippet: "The University of Chicago's Core curriculum provides all College students with a challenging, common academic program... Core Requirements: Arts, Humanities, Civilization Studies, Social Sciences, Biological Sciences, Physical Sciences, Mathematical Sciences... The Core also requires competence in a language other than English."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-015
field: undergraduate.international.english_proficiency
value: "No published minimum; any English proficiency exam accepted; no ESL program"
source_url: https://collegeadmissions.uchicago.edu/apply/international-applicants/
source_snippet: "Students are invited to submit scores from any English proficiency examination they choose... Students who choose to submit English proficiency scores may share either official or self-reported scores... UChicago does not offer an ESL program for admitted students."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-001
field: graduate.admissions.model
value: "Decentralized — each of 12 schools/divisions has own application and admissions"
source_url: https://grad.uchicago.edu/admissions/apply/
source_snippet: "All programs at the University of Chicago offer an online application system, but each school and division has its own application. To apply to multiple programs, you will need to create a unique application for each one."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-002
field: graduate.application.fee_waiver
value: "Each division sets own fee; fee waiver requestable post-submit"
source_url: https://grad.uchicago.edu/admissions/apply/guidelines-and-deadlines/
source_snippet: "The applications to our programs require an accompanying fee... The fee waiver request form will be posted on your portal after the application is submitted. If you plan to request a fee waiver, do not pay the application fee until after your fee waiver request has been reviewed."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-003
field: graduate.testing.gre_policy
value: "Varies by program; GRE general for most PhD; Booth accepts GMAT/GRE; Law uses LSAT; Med uses MCAT"
source_url: https://grad.uchicago.edu/admissions/apply/guidelines-and-deadlines/
source_snippet: "Please read the requirements for applying to your program, as each one will have different instructions regarding standardized tests... In most cases, GRE and subject test scores may be submitted simply to the University of Chicago"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-004
field: graduate.admissions.april_15_resolution
value: "UChicago adheres to CGS April 15 Resolution for PhD offers"
source_url: https://grad.uchicago.edu/admissions/apply/guidelines-and-deadlines/
source_snippet: "(UChicagoGRAD follows Council of Graduate Schools resolution; PhD offers hold until April 15)"
capture_date: 2026-07-04
evidence_type: official_webpage
note: "Standard CGS resolution; verify exact wording on grad.uchicago.edu each cycle"

# E-G-005
field: graduate.english_proficiency.policy
value: "TOEFL iBT or IELTS Academic ONLY (no Duolingo); waiver criteria: native English OR 1+ year full-time degree at English-medium institution in listed countries"
source_url: https://grad.uchicago.edu/admissions/apply/english-language-proficiency/
source_snippet: "Applicants to the graduate schools and divisions... must either meet one of our waiver criteria or submit proof of English language proficiency... Only the TOEFL iBT or IELTS Academic tests are accepted... We do not accept any other proficiency tests... This includes the IELTS 'Indicator' test, the TOEFL ITP Plus, Duolingo, or any other test."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-006
field: graduate.ets_codes
value: "Main = 1832; Booth MBA = 1832-02; Booth PhD = 1819"
source_url: https://grad.uchicago.edu/admissions/apply/english-language-proficiency/
source_snippet: "University of Chicago, excluding business programs: 1832 | Booth School of Business MBA: 1832-02 | Booth School of Business PhD: 1819"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-007
field: graduate.materials.transcripts_international
value: "Upload unofficial transcripts; official only if admitted; non-English requires certified translation"
source_url: https://grad.uchicago.edu/admissions/apply/guidelines-and-deadlines/
source_snippet: "As part of the online application, you will need to upload a copy of your transcript for every college or university you have attended... Applicants who have attended institutions whose transcripts are not in English must submit those transcripts along with certified English translations... Official documents... are only required if you are admitted and plan to enroll."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-008
field: graduate.programs.count
value: 101 graduate programs across 12 divisions/schools
source_url: https://grad.uchicago.edu/admissions/programs/
source_snippet: "101 Available Programs"
capture_date: 2026-07-04
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uchicago-knowledge-base-v2 (collection)
├── uchicago-overview                    (Section 0 — counts, hierarchy, matrix)
├── uchicago-ug-biological-sciences      (Section 1 — BSCD majors/minors)
├── uchicago-ug-physical-sciences        (Section 1 — PSCD majors/minors)
├── uchicago-ug-arts-humanities          (Section 1 — A&H majors/minors)
├── uchicago-ug-social-sciences          (Section 1 — SSD majors/minors)
├── uchicago-ug-interdisciplinary        (Section 1 — joint degrees, interdisciplinary)
├── uchicago-ug-core-curriculum          (Section 1.5 — Core)
├── uchicago-grad-biological-sciences    (Section 2 — BSD programs)
├── uchicago-grad-physical-sciences      (Section 2 — PSD programs)
├── uchicago-grad-social-sciences        (Section 2 — SSD programs)
├── uchicago-grad-arts-humanities        (Section 2 — A&H programs)
├── uchicago-grad-divinity               (Section 2 — Divinity School)
├── uchicago-grad-booth                  (Section 2 — Booth School of Business)
├── uchicago-grad-harris                 (Section 2 — Harris School of Public Policy)
├── uchicago-grad-pritzker-med           (Section 2 — Pritzker School of Medicine)
├── uchicago-grad-pme                    (Section 2 — Pritzker School of Molecular Engineering)
├── uchicago-grad-crown                  (Section 2 — Crown Family School)
├── uchicago-grad-law                    (Section 2 — Law School)
├── uchicago-grad-graham                 (Section 2 — Graham School)
├── uchicago-app-requirements            (Section 3 — UG + grad requirements)
├── uchicago-costs-financial-aid         (Section 4 — COA + aid policy)
└── uchicago-evidence-chain              (Section 5 — provenance)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uchicago-knowledge-base-v2"
  school: "<home college / division / school>"
  department: "<home department or committee, if applicable>"
  degree_level: "<BA|BS|MA|MS|MFA|MBA|MPP|MDiv|MLA|MEng|LLM|MLS|PhD|MD|JD|JSD|DCompL|MD-PhD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | core
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Rationale |
|----------|-----------|------------|----------|
| **P0** | Per-program PhD stipend amounts (BSD/PSD/SSD/A&H) | grad.uchicago.edu/admissions/funding/ + each division's COA page | Stipend figures not captured; needed for cross-school comparison |
| **P0** | College Catalog (collegecatalog.uchicago.edu) live scrape | http://collegecatalog.uchicago.edu/thecollege/ | Returns HTTP 403 to headless browser; would enable verbatim major requirements, course lists, exact degree (BA vs BS) per major |
| **P0** | Per-program grad deadlines (Dec 1 / Dec 15 / Jan 5 etc.) | Each program's admissions page (101 pages) | Decentralized; deadlines vary by program; not aggregated centrally |
| **P1** | Per-program GRE/GMAT subject test requirements | Each PhD program page | Some require GRE Subject (e.g., Biology, Physics); not aggregated |
| **P1** | Booth MBA full-time vs Evening/Weekend/Executive differences | chicagobooth.edu/programs/ | Delivery formats collapsed in directory |
| **P1** | U-SHIP health insurance cost 2026-27 | wellness.uchicago.edu/student-insurance/u-ship/ | Not in COA table; ~$4-5k/yr typical |
| **P1** | Class of 2028 / 2029 admissions statistics (acceptance rate, SAT midpoints) | collegeadmissions.uchicago.edu/apply/class-profile/ | Class profile page not deeply scraped |
| **P2** | Detailed Odyssey Scholarship / merit scholarship amounts | collegeadmissions.uchicago.edu/financial-support/scholarships/ | Named scholarships not enumerated |
| **P2** | International Student Asset Confirmation Form details | financialaid.uchicago.edu/international-student-asset-confirmation-form.pdf | PDF not fetched |
| **P2** | Per-graduate-division application fee exact amounts | Each division's apply page | Range $90-$250 inferred; exact per-division not captured |

### Monitoring watchlist (URL change frequency)

| Frequency | URLs / Fields |
|-----------|---------------|
| **High (monthly)** | Deadlines (collegeadmissions.uchicago.edu/apply/), COA (financialaid.uchicago.edu/undergraduate/costs), testing policy, app fee |
| **Medium (quarterly)** | Programs-of-study index (college.uchicago.edu/academics/programs-study), grad programs directory (grad.uchicago.edu/admissions/programs/), international aid policy |
| **Low (annual)** | Core curriculum, Collegiate Division structure, school/division hierarchy |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | UChicago | MIT | Harvard | Stanford | Yale | Princeton | Caltech | Columbia | NYU |
|-----------|----------|-----|---------|----------|------|-----------|---------|----------|-----|
| Total UG cost/yr (2026-27) | $103,821 (on-campus) | — | — | — | — | — | $93,912 (25-26) | — | — |
| Tuition/yr | $75,960 | — | — | — | — | — | $65,622 (25-26) | — | — |
| Need-blind (intl)? | **No (need-aware)** | Yes | Yes | Yes | Yes | Yes | No | — | — |
| 100% need-met? | Yes (loan-free) | Yes | Yes | Yes | Yes | Yes | Yes | — | — |
| Free tuition threshold | <$250k family income | — | <$85k (no parent contrib) | — | — | — | — | — | <$100k (NYU Promise) |
| EA / REA deadline | ED I + EA: **Nov 2, 2026** | EA Nov 1 | REA Nov 1 | REA Nov 1 | SCEA Nov 1 | SCEA Nov 1 | REA Nov 1 | ED Nov 1 | ED Nov 1 |
| RD deadline | **Jan 4, 2027** | Jan 4 | Jan 1 | Jan 5 | Jan 2 | Jan 1 | Jan 5 | Jan 1 | Jan 5 |
| SAT/ACT required? | **No (test-optional)** | — | test-optional | Required | test-optional forever | test-optional | Required | test-optional | test-optional |
| TOEFL min (UG) | None published | — | None (not req'd) | — | — | — | — | — | competitive |
| App fee | $90 (free if aid) | $75 | $85 | $90 | $80 | $75 | $75 | $85 | $80 |
| **Total programs (rule 1)** | **183** (82 UG + 101 grad) | — | — | 349 | — | — | 76 | — | — |
| **Schools/divisions (rule 2)** | **17** (1 College + 4 Collegiate Div + 12 grad) | 5 | 13 | 7 | — | — | 6 | — | — |
| Grad English test | TOEFL iBT / IELTS Academic only | — | — | — | — | — | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: collegeadmissions.uchicago.edu, college.uchicago.edu, grad.uchicago.edu, financialaid.uchicago.edu, collegecatalog.uchicago.edu (cited), registrar.uchicago.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (`div.program`, `ul.c-accordion-group > li.c-accordion__item`); reconciliation computed in Python (len(ug)==82, len(grad)==101, sum==183 ✓)
> **Granularity**: school → department → degree-level → program
> **Known gaps**: collegecatalog.uchicago.edu returns HTTP 403 to headless browser (catalog URLs cited from College index but verbatim major requirements not scraped); per-program PhD stipends and grad deadlines not aggregated (decentralized); Class Profile admissions statistics not deeply scraped — all listed as P0/P1 follow-ups in Section 6.
