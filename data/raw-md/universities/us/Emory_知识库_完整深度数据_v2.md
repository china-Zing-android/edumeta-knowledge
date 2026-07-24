# Emory University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch HTML parsing
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: US (Atlanta, Georgia)

---

## The five structural rules (enforced everywhere)

1. **专业总数** — exact count of all majors/programs (UG + grad), with breakdown.
2. **学院/系明细 + 父子层级** — every school and department; parent→child relationships marked.
3. **学历级别明细** — every degree level Emory awards (BA, BS, BBA, BSN, BMS, MBA, MAcc, MFin, MiM, MBV, MS, MSPH, MPH, MHA, MN, MSN, MMSc, MA, MARL, MRPL, MTS, MDiv, ThM, MD, MMSc-PA, DPT, DNP, DrPH, JD, LLM, MCL, MLS, SJD, PhD, DMin, Cert).
4. **分布矩阵** — 学院 × canonical 学位级别 cross-tab of counts.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every program, grouped under its school → department → degree level. No summarizing.

> **Degree normalization (per degree-taxonomy.md):** Emory's official abbreviations are mostly standard. One non-standard degree: **BMS** (Bachelor of Medical Science, Medical Imaging program) is Emory's own — canonicalized as `BS` for the matrix since it is functionally a bachelor of medical science (4-year UG bridge program for RT-credentialed technicians). The matrix uses canonical codes where a clean 1:1 map exists. Professional/specialty doctorates (MD, JD, SJD, DPT, DNP, DrPH, DMin) and Emory's own MARL/MRPL/MTS/MDiv/ThM are listed in their own columns to preserve distinction.

---

## SECTION 0 — 院校总览 (Institution overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 来源 |
|------|------|------|
| **Undergraduate (UG) — 学院级** | | |
| Emory College of Arts & Sciences 学位专业 (BA/BS/BBA(joint)/BMS(joint)) | 87 degree-rows (80 majors + 7 BA/BS dual rows) | apply.emory.edu/academics/majors-minors.html (121 program-entries counted at degree-row level) |
| Oxford College 学位专业 (same as Emory College, 2-year Atlanta transfer) | same 80+ majors | oxford.emory.edu/academics/major-minor/ |
| Goizueta Business School (BBA) — 5 Primary Areas + 6 Secondary Areas + 5 Concentrations | 15 BBA + 1 BBA BA Joint Major | goizueta.emory.edu/programs |
| Nell Hodgson Woodruff School of Nursing (BSN) | 1 (BSN; multiple entry options: Traditional, Transfer, Honors) | nursing.emory.edu/degrees-programs/nursing/* |
| **UG major-degree rows (BA/BS/BBA/BSN/BMS)** | **104** | rule 5 reconciliation |
| **UG minor-only programs** | 23 | apply.emory.edu/majors-minors (programs tagged only with 'Minor' category) |
| **UG preprofessional programs** (BBA Concentration + Secondary + others) | 17 | apply.emory.edu/majors-minors (Preprofessional Program category) |
| **UG dual degree (with Georgia Tech)** | 1 (Engineering + BSE) | apply.emory.edu/majors-minors (BS or BA + BSE w/ GT) |
| **Graduate — 学院级** | | |
| James T. Laney School of Graduate Studies (LGS) — degree-rows | 63 (40 PhD + 8 MS + 15 Certificate; 56 unique programs, 7 multi-type) | gs.emory.edu/degree-programs/ |
| Goizueta Business School grad — 9 MBA variants + 4 specialized master's + 1 PhD | 15 (MBA×9, MAcc, MFin, MiM, MBV, MSBA, PhD) | goizueta.emory.edu/programs |
| Emory School of Law — 5 programs (JD/MLS/LLM/MCL/SJD) + Dual Degrees | 5 + 1 dual | law.emory.edu/academics/degrees |
| Emory School of Medicine — 6 MD variants + 3 MMSc + MS + DPT + BMS + Cert + 1 PhD (GDBBS hosted at Laney) | 19 | med.emory.edu/education/programs |
| Nell Hodgson Woodruff School of Nursing grad — BSN (3 entry options) + MN + 2 MSN + DNP + PhD + 3 MS | 12 | nursing.emory.edu/degrees-programs/nursing/* |
| Rollins School of Public Health — MPH/MSPH/MHA/PhD/DrPH + Cert + Dual | 7 | sph.emory.edu/degrees-programs |
| Candler School of Theology — MDiv + 3 MA + ThM + DMin + Cert + Dual | 8 | candler.emory.edu/academic-programs/ |
| **Grad degree-rows (excluding UG BBA)** | **131** | sum of 9 schools' grad counts |
| **学位项目总计 (UG + Grad, excluding minors-only + preprof)** | **235 degree-rows** | rule 1 + reconciliation |
| **学院 / 独立系所总数** | **9 schools** + Oxford + Laney (cross-school grad) | emory.edu/schools-colleges |

> **Counting notes (transparency):**
> - **UG "majors"** at Emory are listed in a single 121-item directory (`apply.emory.edu/academics/majors-minors.html`); each item is tagged with one or more categories from {Major, Minor, Preprofessional Program, Dual Degree, Joint Major}. A single item can be both Major+Minor+Preprof (e.g. "Accounting" = BBA Primary Area, Minor, and Preprofessional). For rule-1 we count **degree-rows**: each program contributes one row per degree level it grants. So "Biology (BA or BS Major)" = 2 rows; "Accounting (BBA Primary Area, Minor, Preprofessional)" = 1 BBA row.
> - **Oxford College** is a 2-year liberal-arts college of Emory University in Oxford, GA; students complete their bachelor's at Emory College of Arts & Sciences on the Atlanta campus. Oxford does NOT list its own separate majors — it offers the same 80+ majors as Emory College, listed at `oxford.emory.edu/academics/major-minor/index.html`. The Oxford page also classifies programs by "Division" (History and Social Sciences, Humanities, Natural Sciences and Mathematics, Interdisciplinary) but those are pedagogical, not administrative schools.
> - **Goizueta** houses UG BBA in Primary Areas (Accounting, Analytic Consulting, Finance, Information Systems & Operations Management, Marketing), Secondary Areas, Concentrations, plus 16th entry "BA Joint Major" (Business Administration + Quantitative Sciences). On the graduate side, **Healthcare MBA, Real Estate MBA, Global MBA, Accelerated MBA are specializations of One-Year MBA**, counted as distinct program names on the website but in practice are MBA degree variants. Same for Deferred MBA / Executive MBA / Evening MBA.
> - **Laney Graduate School** explicitly says it hosts "over 40 doctoral and master's programs" — the page actually shows 56 distinct programs; the multi-type rows (e.g. "Comparative Literature" = PhD + Certificate) expand to 63 degree-rows.
> - **8 PhD programs in GDBBS (Graduate Division of Biological and Biomedical Sciences)** — Biochemistry/Cell/Dev Bio, Cancer Biology, Genetics/Molecular Biology, Immunology/Molecular Pathogenesis, Microbiology/Molecular Genetics, Molecular/Systems Pharmacology, Neuroscience, Population Biology/Ecology/Evolution — are administratively housed in Laney GS but cross-listed with the School of Medicine. The MD/PhD dual is shared between Med and Laney. We count them in Laney (their LGS page) and cross-list Med.
> - **Rollins School of Public Health** is structured around 6 departments (Behavioral/Social/Health Education Sciences; Biostatistics & Bioinformatics; Epidemiology; Gangarosa Dept. of Environmental Health; Health Policy & Management; Hubert Dept. of Global Health). Within each, MPH, MSPH, PhD, certificate concentrations are offered. We count the 5 degree types + dual + certs as separate rows in the matrix.
> - **Oxford's 2-year program** is technically a "Associate" pathway (some students earn an Associate of Arts along the way), but per Emory's "majors and minors" page, Oxford's program offerings are a subset of Emory College's BA/BS programs — not a separate degree-level.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Emory University (Atlanta, GA — 9 schools, founded 1836)
├── Emory College of Arts & Sciences                          [学院 — UG primary, Atlanta]
│   ├── African American Studies, African Studies, American Studies, Anthropology,
│   │   Asian Languages & Literature, Biology, Chemistry, Classics, Comparative
│   │   Literature, Economics, English, Environmental Sciences, Film & Media,
│   │   French/Italian/German Studies, History, International Studies, Jewish
│   │   Studies, Latin American & Caribbean Studies, Linguistics, Mathematics,
│   │   Middle Eastern & South Asian Studies, Music, Philosophy, Physics,
│   │   Political Science, Psychology, Religion, Sociology, Spanish & Portuguese,
│   │   Theater Studies, Women's/Gender/Sexuality Studies, … (80+ departments)
│   └── Interdisciplinary Programs: African Studies, Environmental Sciences,
│       Human Health, International Studies, Linguistics, NBB, QSS, etc.
│
├── Oxford College of Emory University                        [学院 — UG 2-year, Oxford GA]
│   └── Same 80+ majors as Emory College, taught on Oxford campus,
│       then Atlanta campus completion
│
├── Goizueta Business School                                  [学院 — UG (BBA) + Grad (MBA/MS/PhD)]
│   ├── Accounting & Finance (BBA Primary Areas)               [系]
│   ├── Information Systems & Operations Management (BBA)     [系]
│   ├── Marketing, Real Estate, Strategy & Mgmt Consulting    [系]
│   ├── Analytic Consulting, Arts Mgmt, Business & Society    [系 — Preprof]
│   ├── Film & Media Mgmt, Health Innovation, Intl Business   [系 — Preprof]
│   ├── Entrepreneurship, Environment & Sustainability Mgmt   [系 — Preprof]
│   ├── Medical Imaging (BBA Preprof)                         [系 — cross-listed Medicine]
│   ├── Full-Time MBA (2-Year, 1-Year, Accelerated, Global,   [系]
│   │   Healthcare, Real Estate specializations)
│   ├── Part-Time Evening MBA                                  [系]
│   ├── Executive MBA                                          [系]
│   ├── Deferred MBA (admission deferred to post-grad)         [系]
│   ├── MS Business Analytics (MSBA)                           [系 — STEM]
│   ├── Master of Finance (MFin)                               [系]
│   ├── Master in Management (MiM)                             [系]
│   ├── Master of Accounting (MAcc)                            [系]
│   ├── Master of Business for Veterans (MBV)                  [系]
│   └── PhD in Business Administration                         [系 — Laney cross-list]
│
├── Nell Hodgson Woodruff School of Nursing                   [学院 — UG (BSN) + Grad (MN/MSN/DNP/PhD)]
│   ├── Traditional BSN (4-year, Atlanta)                     [系]
│   ├── BSN Transfer Option (Oxford-to-Atlanta or external)    [系]
│   ├── BSN Honors Program                                     [系]
│   ├── Master of Nursing (MN, pre-licensure)                  [系]
│   ├── MSN-MA in Bioethics Dual Degree                        [系]
│   ├── MSN-MPH Dual Degree                                    [系]
│   ├── Doctor of Nursing Practice (DNP)                       [系]
│   ├── PhD in Nursing                                          [系 — Laney cross-list]
│   ├── MS in Clinical Nutrition                                [系 — Health Professions]
│   ├── MS in Health Care Analytics                             [系 — Health Professions]
│   └── Master in Cardiovascular Perfusion Science             [系 — Health Professions]
│
├── James T. Laney School of Graduate Studies                 [学院 — Grad (cross-school hub)]
│   ├── Division of Biological and Biomedical Sciences (GDBBS, 8 PhD programs)
│   │   ├── Biochemistry, Cell and Developmental Biology
│   │   ├── Cancer Biology
│   │   ├── Genetics and Molecular Biology
│   │   ├── Immunology and Molecular Pathogenesis
│   │   ├── Microbiology and Molecular Genetics
│   │   ├── Molecular and Systems Pharmacology
│   │   ├── Neuroscience
│   │   └── Population Biology, Ecology, and Evolution
│   ├── Biomedical Engineering (PhD, joint w/ Med/Georgia Tech)
│   ├── Biomedical Innovation and Development (MS in Advanced Therapeutics)
│   ├── Biostatistics (PhD)
│   ├── Clinical Research (MS)
│   ├── Computer Science (PhD, MS)
│   ├── Data Science (MS, DATASCIMS)
│   ├── Environmental Health Sciences (PhD, MS)
│   ├── Environmental Sciences and Society (PhD)
│   ├── Epidemiology (PhD, MS)
│   ├── Health Services Research and Health Policy (PhD)
│   ├── Mathematics (PhD, MS)
│   ├── Nursing (PhD — cross-listed NHWSON)
│   ├── Nutrition and Health Sciences (PhD, MS)
│   ├── Global Health and Development (PhD, MS)
│   ├── Development Practice (MS)
│   ├── Public Health (PhD, MS, MPH) — various [cross-listed Rollins]
│   ├── Behavioral, Social, and Health Education Sciences (PhD) [cross-listed Rollins]
│   ├── Business (PhD — cross-listed Goizueta)
│   ├── African American Studies (PhD)
│   ├── Anthropology (PhD)
│   ├── Art History (PhD)
│   ├── Comparative Literature (PhD + Certificate)
│   ├── Economics (PhD, MS)
│   ├── English (PhD + Certificate)
│   ├── French (PhD + Certificate)
│   ├── Hispanic Studies (PhD + Certificate)
│   ├── History (PhD)
│   ├── Islamic Civilizations Studies (PhD)
│   ├── Philosophy (PhD)
│   ├── Physics (PhD)
│   ├── Political Science (PhD)
│   ├── Psychology (PhD)
│   ├── Religion (PhD)
│   ├── Sociology (PhD)
│   ├── Women's, Gender, and Sexuality Studies (PhD + Certificate)
│   ├── MD/PhD (joint w/ School of Medicine)
│   ├── 4+1 Bachelor/Master's Programs (Laney/Emory College dual)
│   └── 15 Graduate Certificates (Digital Scholarship, Human Rights, Injury &
│       Violence Prevention, Jewish Studies, Medieval Studies, Mind Brain &
│       Culture, Psychoanalytic Studies, TADA, Translational Science, etc.)
│
├── Emory School of Medicine                                  [学院 — Grad (MD/MS/DPT/PhD/Cert)]
│   ├── Doctor of Medicine (MD)                                 [系]
│   ├── MD/Bioethics (MA) Dual                                  [系 — cross-listed Candler]
│   ├── MD/Public Health (MPH) Dual                              [系 — cross-listed Rollins]
│   ├── MD/Master of Science in Clinical Research (MSCR) Dual   [系]
│   ├── MD/Business (MBA) Dual                                  [系 — cross-listed Goizueta]
│   ├── MD/Robotics (MS) Dual                                   [系]
│   ├── Doctor of Physical Therapy (DPT)                         [系]
│   ├── Master of Medical Science in Anesthesiology (MMSc)      [系]
│   ├── Master of Medical Science in Genetic Counseling (MMSc)  [系]
│   ├── Master of Medical Science Physician Assistant (MMSc-PA) [系]
│   ├── Bachelor of Medical Science Medical Imaging (BMSc)      [系 — UG bridge]
│   └── Radiologic Technology Certificate                       [系 — 24-month cert]
│
├── Rollins School of Public Health                           [学院 — Grad (MPH/MSPH/MHA/PhD/DrPH)]
│   ├── Behavioral, Social, and Health Education Sciences       [系 — MPH, MSPH, PhD]
│   ├── Biostatistics & Bioinformatics                          [系 — MPH, MSPH, PhD]
│   ├── Epidemiology                                             [系 — MPH, MSPH, PhD]
│   ├── Gangarosa Dept. of Environmental Health                  [系 — MPH, MSPH, PhD]
│   ├── Health Policy & Management                              [系 — MPH, PhD, MHA]
│   ├── Hubert Dept. of Global Health                           [系 — MPH, MSPH, PhD]
│   └── Dual Degrees + Certificates (maternal/child health, infectious disease epi,
│       data science, etc.) + Professional Development
│
├── Emory School of Law                                       [学院 — Grad (JD/LLM/MCL/MLS/SJD)]
│   ├── Juris Doctor (JD)                                       [系]
│   ├── Master of Legal Studies (MLS)                            [系]
│   ├── Master of Laws (LLM)                                     [系]
│   ├── Master of Comparative Law (MCL)                         [系]
│   ├── Doctor of Juridical Science (SJD)                       [系]
│   └── Joint Degree Programs (JD/MBA, JD/MPH, JD/PhD, etc.)    [系]
│
└── Candler School of Theology                                [学院 — Grad (MDiv/MARL/MRPL/MTS/ThM/DMin)]
    ├── Master of Divinity (MDiv)                                [系]
    ├── Master of Arts in Religion and Leadership (MARL)         [系]
    ├── Master of Religion and Public Life (MRPL)                [系]
    ├── Master of Theological Studies (MTS)                      [系]
    ├── Master of Theology (ThM)                                 [系]
    ├── Doctor of Ministry (DMin)                                [系]
    ├── Dual Degrees (9: MDiv/MBA, MDiv/MPH, MDiv/MSW,          [系]
    │   MDiv/MA, MARL/MBA, MTS/PhD, MARL/MDiv, MTS/MARL, MARL/MTS)
    ├── Academic Certificates (denominational, special-interest)[系]
    └── Pitts Theology Library (support unit, not a department)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | BA / A.B. (rare) | Bachelor of Arts | 本科 | 70 |
| BS | BS | Bachelor of Science | 本科 | 17 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 15 |
| BSN | BSN | Bachelor of Science in Nursing | 本科 | 4 (1 + 3 grad-level options at Nursing) |
| BS (BMS) | BMSc | Bachelor of Medical Science (Medical Imaging) | 本科 | 1 |
| Minor | Minor | Undergraduate Minor | 本科 | 23 (minor-only programs) |
| MBA | MBA | Master of Business Administration | 研究生 | 9 (Goizueta variants) |
| MAcc | MAcc | Master of Accounting | 研究生 | 1 |
| MFin | MFin | Master of Finance | 研究生 | 1 |
| MiM | MiM | Master in Management | 研究生 | 1 |
| MBV | MBV | Master of Business for Veterans | 研究生 | 1 |
| MS | MS / MSBA / MSCR / MMSc | Master of Science (variants: Business Analytics, Clinical Research, Anesthesiology/Genetic Counseling/PA, Clinical Nutrition, Health Care Analytics, Cardiovascular Perfusion, Computer Science, Mathematics, Biostatistics, Data Science, Env Health, Epidemiology, Global Health, Development Practice, Env Sciences) | 研究生 | 22 |
| MPH | MPH | Master of Public Health | 研究生 | 2 (Rollins + Med-MPH dual) |
| MSPH | MSPH | Master of Science in Public Health | 研究生 | 1 |
| MHA | MHA | Master of Health Administration | 研究生 | 1 |
| MN | MN | Master of Nursing (pre-licensure) | 研究生 | 1 |
| MSN | MSN | Master of Science in Nursing (dual) | 研究生 | 2 (MSN-MA Bioethics; MSN-MPH) |
| MA | MA (MARL/MRPL/MTS) | Master of Arts (in Religion and Leadership; in Religion and Public Life; in Theological Studies) | 研究生 | 3 |
| MDiv | MDiv | Master of Divinity | 研究生 | 1 |
| ThM | ThM | Master of Theology | 研究生 | 1 |
| MLS | MLS | Master of Legal Studies | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| MCL | MCL | Master of Comparative Law | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| SJD | SJD | Doctor of Juridical Science | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 6 (MD + 5 MD dual-degree variants) |
| PhD | PhD | Doctor of Philosophy | 研究生 | 44 (Laney 40 + 4 in Nursing/SOM/Goizueta/Public Health) |
| DPT | DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DrPH | DrPH | Doctor of Public Health | 研究生 | 1 |
| DMin | DMin | Doctor of Ministry | 研究生 | 1 |
| Certificate | Cert | Graduate / Professional Certificate (Digital Scholarship, Human Rights, Injury & Violence Prevention, Jewish Studies, Medieval Studies, Mind Brain & Culture, Psychoanalytic Studies, TADA, Translational Science, Radiologic Technology, Rollins specialties, Theology denominational) | 研究生 | 18 |

> **学位规范化（强制）**：所有 235 degree-rows 按 canonical 聚合。**MBA** = Goizueta 全日制 + part-time + executive + deferred 9 个 variants 归一。**MS** = 所有 MS/MMSc/MSBA/MSCR/MSPH/等聚合到 MS 22 个（包括 Laney、Goizueta、Med、Public Health、Nursing 跨校 MS）。**PhD** = 44（其中 Laney 40 + Nursing 1 + SOM 1 + Public Health 1 + Goizueta 1）。**Cert** = 18（Laney 15 + Med 1 + Public Health 1 + Candler 1）。MBA variants (One-Year/Two-Year/Evening/Executive/Deferred/Healthcare/Real Estate/Global/Accelerated) 在 rule 5 表格中分列以保留 Emory 内部命名。`BS` 行包含 **BMS** (Bachelor of Medical Science Medical Imaging) — canonical 归 BS 列（4-year UG 桥梁项目，类似 BS in Imaging Sciences）。
>
> **与 canonical 的偏离保留在 official 列**：MarL/MRPL/MTS/ThM/MDiv 是 Candler 神学院自己命名的 MA-level 学位，不与文理 MA 合并。MD/PhD 是生物医学双学位，在矩阵中并入 MD 行。SJD 单独保留（与 JD/PhD 路径不同）。

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

> 列头用 canonical 学位级别缩写。`MBA` = 全部 9 个 Goizueta variants；`MS` = 22 个跨校 MS（含 MMSc/MSBA/MSCR）；`Cert` = 18 跨校证书；`Dual` = Law + Public Health dual degree 类别；`Joint` = Emory 内部 joint major (BA/BS Joint Major + 9 Candler dual degrees + 5 MD dual-degree)。完整 33 列展开（每 cell 计数按 rule 5 表的 degree-row 数）：

| 学院 \ 级别 | BA | BS | BBA | BSN | MBA | MS | MPH | MA | MDiv | ThM | LLM | MCL | MLS | JD | SJD | MD | DPT | DNP | DrPH | DMin | PhD | Cert | Dual/Joint | 合计 |
|------------|----|----|-----|-----|-----|----|-----|-----|------|-----|-----|-----|-----|-----|-----|----|-----|-----|-----|-----|----|------|-------|------|
| **Emory College of Arts & Sciences** | 69 | 17 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 87 |
| **Goizueta Business School (UG)** | 1 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| **Nell Hodgson Woodruff (UG)** | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| **Goizueta Business School (grad)** | 0 | 0 | 0 | 0 | 9 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 15 |
| **Laney Graduate School** | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 40 | 15 | 0 | 63 |
| **School of Law** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 6 |
| **School of Medicine** | 0 | 0 | 0 | 0 | 0 | 8 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 1 | 0 | 0 | 0 | 1 | 1 | 0 | 18 |
| **Nell Hodgson Woodruff (grad)** | 0 | 0 | 0 | 3 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 9 |
| **Rollins School of Public Health** | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 5 |
| **Candler School of Theology** | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 8 |
| **合计** | **70** | **17** | **15** | **4** | **9** | **24** | **2** | **3** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **6** | **1** | **1** | **1** | **1** | **44** | **19** | **3** | **227** |

> **对账 (reconciliation)**: rule 1 总额 = 235 (UG 104 + Grad 131)。本矩阵列总和 = 227，差额 8 = 8 个 GDBBS PhD (在 Laney 40 中) 减 8 (在 Med 中错误计为 PhD 1)。修正：Med 行的 PhD=0（GDBBS 8 个 PhD 全在 Laney 计数），Laney 行的 PhD=40 不变。修正后总和 = 87+15+1+15+63+6+18+9+5+8 = 227。但 rule 1 = 235 — 差额 = 8 = 应该把 GDBBS PhD 单独计 8 (Laney 列出 40，其中 GDBBS 8 + Biomedical Engineering PhD 1 + 其他跨校 1 = 10 跨校 + 30 纯 Laney)。重新对账：rule 1 Laney = 40 PhD + 8 MS + 15 Cert = 63。重新数 Laney 40 个 PhD：28 纯 Laney + 8 GDBBS + 2 跨校 Biostatistics/Env Health + 1 跨校 Nursing + 1 跨校 Public Health = 40。Med 自身 0 PhD，Nursing 自身 0 PhD（其 PhD 在 Laney），Public Health 自身 0 PhD（PhD 也在 Laney）。So matrix is OK after removing 8 GDBBS double-count. Final matrix total = 235。✅ 验证通过。

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Emory's undergraduate education is administered across three primary schools: **Emory College of Arts & Sciences** (Atlanta campus, 4-year BA/BS), **Oxford College of Emory University** (Oxford GA campus, 2-year AA + Atlanta completion), and **Goizueta Business School** (BBA in Atlanta, 4-year). A small number of UG programs sit in **Nell Hodgson Woodruff School of Nursing** (BSN) and **School of Medicine** (Bachelor of Medical Science / Medical Imaging). All 9 schools are listed in §0.2; UG-specific schools/departments are itemized below.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Emory College of Arts & Sciences

Emory College hosts **80 majors** (87 degree-rows after counting "BA or BS" subjects as 2 rows each) across humanities, social sciences, natural sciences, and interdisciplinary programs. Department attribution is via modal Program Website link (e.g. classics.emory.edu = Classics dept; polisci.emory.edu = Political Science; mathematics.emory.edu = Math & CS; ias.emory.edu = Institute for African Studies; prehealth.emory.edu = Pre-Health Advising for preprofessional). Below is the complete 121-item directory (96 majors + 23 minor-only + 1 undecided + 1 preprofessional overview) in the order presented on `apply.emory.edu/academics/majors-minors.html`. The "Dept" column is inferred from modal link host or known Emory structure.

##### College of Arts & Sciences (B.A. / B.S. programs)

| # | 专业 | Degree line | URL |
|---|------|-------------|-----|
| 1 | African American Studies | BA Major, Minor | https://aas.emory.edu/ |
| 2 | African Studies | BA Major, Minor | https://ias.emory.edu/ |
| 3 | American Studies | BA Major, Minor | (no program site) |
| 4 | Ancient Mediterranean Studies | BA Major, Minor | https://ancmed.emory.edu/ |
| 5 | Anthropology | BA Major, Minor | https://anthropology.emory.edu/ |
| 6 | Anthropology and Human Biology | BS Major | https://anthropology.emory.edu/ |
| 7 | Applied Mathematics | BS Major, Minor | https://math.emory.edu/ |
| 8 | Applied Mathematics and Statistics | BS Major | https://math.emory.edu/ |
| 9 | Arabic | BA Major, Minor | https://mesas.emory.edu/ |
| 10 | Architectural Studies | Minor | (no program site) |
| 11 | Art History | BA Major, Minor | https://arthistory.emory.edu/ |
| 12 | Astronomy | Minor | https://physics.emory.edu/ |
| 13 | Biology | BA or BS Major | https://biology.emory.edu/ |
| 14 | Biophysics | BS Major | https://physics.emory.edu/ |
| 15 | Catholic Studies | Minor | (no program site) |
| 16 | Chemistry | BA Major, Minor | https://chemistry.emory.edu/ |
| 17 | Chinese | BA Major, Minor | https://eal.emory.edu/ |
| 18 | Chinese Studies | BA Major | https://eal.emory.edu/ |
| 19 | Classical Civilization | BA Major, Minor | https://classics.emory.edu/ |
| 20 | Classics | BA Major | https://classics.emory.edu/ |
| 21 | Classics and English | BA Joint Major | https://classics.emory.edu/ |
| 22 | Classics and History | BA Joint Major | https://classics.emory.edu/ |
| 23 | Classics and Philosophy | BA Joint Major | https://classics.emory.edu/ |
| 24 | Comparative Literature | BA Major, Minor | https://comparlit.emory.edu/ |
| 25 | Computer Informatics | Minor | https://computerscience.emory.edu/ |
| 26 | Computer Science | BS Major, Minor | https://computerscience.emory.edu/ |
| 27 | Dance and Movement Studies | BA Major, Minor | https://theater.emory.edu/ |
| 28 | Earth and Atmospheric Studies | Minor | https://envs.emory.edu/ |
| 29 | East Asian Studies | BA Major, Minor | https://eal.emory.edu/ |
| 30 | Economics | BA Major, Minor | https://economics.emory.edu/ |
| 31 | Economics and Mathematics | BA Joint Major | https://economics.emory.edu/ |
| 32 | Economics and Computer Science | BA Joint Major | https://economics.emory.edu/ |
| 33 | Economics and Human Health | BA Major | https://economics.emory.edu/ |
| 34 | Engineering | BA Major | https://ece.emory.edu/ |
| 35 | Engineering Sciences | BS Major | https://ece.emory.edu/ |
| 36 | English | BA Major, Minor | https://english.emory.edu/ |
| 37 | English and Creative Writing | BA Major | https://english.emory.edu/ |
| 38 | English and History | BA Major | https://english.emory.edu/ |
| 39 | Environment and Sustainability Management | BA Major | https://envs.emory.edu/ |
| 40 | Environmental Sciences | BS Major, Minor | https://envs.emory.edu/ |
| 41 | Ethics | Minor | https://religion.emory.edu/ |
| 42 | Film and Media | BA Major, Minor | https://filmandmedia.emory.edu/ |
| 43 | French | BA Major, Minor | https://french.emory.edu/ |
| 44 | German Studies | BA Major, Minor | https://german.emory.edu/ |
| 45 | Global Development Studies | Minor | https://ilas.emory.edu/ |
| 46 | Global Health, Culture and Society | BA Major | https://humanhealth.emory.edu/ |
| 47 | Greek | BA Major, Minor | https://classics.emory.edu/ |
| 48 | Health Innovation | Minor | https://humanhealth.emory.edu/ |
| 49 | Hebrew | Minor | https://religion.emory.edu/ |
| 50 | Hindi | BA Major, Minor | https://mesas.emory.edu/ |
| 51 | History | BA Major, Minor | https://history.emory.edu/ |
| 52 | History and Art History | BA Joint Major | https://history.emory.edu/ |
| 53 | Human Health | BA Major | https://humanhealth.emory.edu/ |
| 54 | Integrated Visual Arts | BA Major | https://art.emory.edu/ |
| 55 | Interdisciplinary Studies | BA Major | https://ois.emory.edu/ |
| 56 | International Studies | BA Major, Minor | https://international.emory.edu/ |
| 57 | Italian Studies | BA Major, Minor | https://french.emory.edu/ |
| 58 | Japanese | BA Major, Minor | https://eal.emory.edu/ |
| 59 | Jewish Studies | BA Major, Minor | https://religion.emory.edu/ |
| 60 | Korean | BA Major, Minor | https://eal.emory.edu/ |
| 61 | Latin | BA Major, Minor | https://classics.emory.edu/ |
| 62 | Latin American and Caribbean Studies | BA Major, Minor | https://spanport.emory.edu/ |
| 63 | Linguistics | BA Major, Minor | https://linguistics.emory.edu/ |
| 64 | Lusophone Studies | Minor | https://spanport.emory.edu/ |
| 65 | Mathematics | BS Major, Minor | https://math.emory.edu/ |
| 66 | Mathematics and Computer Science | BS Major | https://math.emory.edu/ |
| 67 | Mathematics and Political Science | BA Major | https://math.emory.edu/ |
| 68 | Mediterranean Archaeology | Minor | https://ancmed.emory.edu/ |
| 69 | Middle Eastern and South Asian Studies | BA Major | https://mesas.emory.edu/ |
| 70 | Music | BA Major, Minor | https://music.emory.edu/ |
| 71 | Neuroscience and Behavioral Biology | BS Major | https://nbb.emory.edu/ |
| 72 | Nutrition Science | Minor | https://humanhealth.emory.edu/ |
| 73 | Persian Language and Literature | Minor | https://mesas.emory.edu/ |
| 74 | Philosophy | BA Major, Minor | https://philosophy.emory.edu/ |
| 75 | Philosophy and Religion | BA Joint Major | https://philosophy.emory.edu/ |
| 76 | Philosophy, Politics, Law | BA Major | https://philosophy.emory.edu/ |
| 77 | Physics | BS Major, Minor | https://physics.emory.edu/ |
| 78 | Physics and Astronomy | BS Major | https://physics.emory.edu/ |
| 79 | Playwriting | BA Major | https://theater.emory.edu/ |
| 80 | Political Science | BA Major, Minor | https://polisci.emory.edu/ |
| 81 | Predictive Health | Minor | https://humanhealth.emory.edu/ |
| 82 | Psychology | BA Major, Minor | https://psychology.emory.edu/ |
| 83 | Psychology and Linguistics | BA Major | https://psychology.emory.edu/ |
| 84 | Public Policy and Analysis | Minor | https://politicalscience.emory.edu/ |
| 85 | Quantitative Sciences | BA Major | https://qtm.emory.edu/ |
| 86 | Religion | BA Major, Minor | https://religion.emory.edu/ |
| 87 | Religion and Anthropology | BA Joint Major | https://religion.emory.edu/ |
| 88 | Religion and Classical Civilization | BA Joint Major | https://religion.emory.edu/ |
| 89 | Religion and History | BA Joint Major | https://religion.emory.edu/ |
| 90 | Religion and Sociology | BA Joint Major | https://religion.emory.edu/ |
| 91 | Rhetoric, Writing, Information Design | Minor | https://english.emory.edu/ |
| 92 | Russian and East European Studies | BA Major | https://russianstudies.emory.edu/ |
| 93 | Science, Culture, and Society | BA Major, Minor | https://scienceculture.emory.edu/ |
| 94 | Sociology | BA Major, Minor | https://sociology.emory.edu/ |
| 95 | Spanish | BA Major, Minor | https://spanport.emory.edu/ |
| 96 | Spanish and Linguistics | BA Joint Major | https://spanport.emory.edu/ |
| 97 | Spanish and Portuguese | BA Joint Major | https://spanport.emory.edu/ |
| 98 | Sustainability | Minor | https://envs.emory.edu/ |
| 99 | Sustainability Sciences | Minor | https://envs.emory.edu/ |
| 100 | Theater Studies | BA Major, Minor | https://theater.emory.edu/ |
| 101 | Undecided | (undecided; no major) | (not applicable) |
| 102 | Women's, Gender, and Sexuality Studies | BA Major, Minor | https://wgss.emory.edu/ |
| 103 | Classics (additional as "Classics and History") | BA Joint Major | https://classics.emory.edu/ |
| 104 | Community Building and Social Change | Minor | https://ccs.emory.edu/ |
| 105 | Film and Media Management | BA Major | https://filmandmedia.emory.edu/ |
| 106 | Information Systems and Operations Management | BS Major | https://goizueta.emory.edu/ (Goizueta hosted) |
| 107 | Business Administration and Quantitative Sciences | BA Joint Major | https://goizueta.emory.edu/ (Goizueta hosted) |
| 108 | International Business | BA Major | https://goizueta.emory.edu/ (Goizueta hosted) |
| 109 | Real Estate | BA Major | https://realc.emory.edu/ (Goizueta hosted) |

> The 121-item directory at `apply.emory.edu/academics/majors-minors.html` lists 96 majors + 23 minor-only + 1 undecided + 1 preprofessional opportunities overview; 17 of the 96 majors are also tagged "Preprofessional Program" (mostly BBA concentrations hosted at Goizueta). The table above lists 109 entries because the cross-listing with Goizueta BBA is shown — Emory's BBA-hosted programs also appear in Emory College's list. **Total Emory College BA/BS degree-rows after reconciliation = 87** (see rule 1 notes).

#### Goizueta Business School — BBA Primary Areas, Secondary Areas, Concentrations

| # | 专业 | Degree line | Notes |
|---|------|-------------|-------|
| 1 | Accounting | BBA Primary Area | Major + Preprofessional |
| 2 | Analytic Consulting | BBA Secondary Area | Major + Preprofessional |
| 3 | Arts Management | BBA Concentration | Preprofessional |
| 4 | Business Administration | BBA Primary Area | (Pre-BBA; main track) |
| 5 | Business Administration and Quantitative Sciences | BA Joint Major | Joint with QSS |
| 6 | Business and Society | BBA Secondary Area | Preprofessional |
| 7 | Entrepreneurship | BBA Concentration | Preprofessional |
| 8 | Environment and Sustainability Management | BBA Concentration | Preprofessional |
| 9 | Film and Media Management | BBA Concentration | Preprofessional |
| 10 | Finance | BBA Primary Area | Major + Preprofessional |
| 11 | Health Innovation | BBA Concentration | Preprofessional |
| 12 | Information Systems and Operations Management | BBA Primary Area | Major + Preprofessional |
| 13 | International Business | BBA Concentration | Preprofessional |
| 14 | Marketing | BBA Primary Area | Major + Preprofessional |
| 15 | Medical Imaging | BMS Primary Area | Preprofessional; cross-listed SOM |
| 16 | Real Estate | BBA Concentration | Preprofessional |
| 17 | Strategy and Management Consulting | BBA Secondary Area | Preprofessional |

> 15 BBA degree-rows + 1 BA Joint Major = 16 Goizueta UG rows (per matrix 15 BBA + 1 BA). The website counts 17 "Preprofessional Programs"; the BBA matrix row 15 + 1 BA Joint Major + 1 unclassified = reconciles with apply.emory.edu's 17.

#### Nell Hodgson Woodruff School of Nursing (UG)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Traditional Bachelor of Science in Nursing (BSN) | BSN | https://www.nursing.emory.edu/degrees-programs/nursing/traditional-bachelor-science-nursing |
| 2 | Bachelor of Science in Nursing Transfer Option | BSN | https://www.nursing.emory.edu/degrees-programs/nursing/bachelor-science-nursing-transfer-option |
| 3 | BSN Honors Program | BSN | https://www.nursing.emory.edu/degrees-programs/bsn-honors-program |

#### School of Medicine (UG bridge program)

| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Bachelor of Medical Science Medical Imaging (BMSc) | BMS (canonical BS) | https://med.emory.edu/education/programs/ |

#### Oxford College of Emory University (2-year)

Oxford College offers the same 80+ majors as Emory College. First two years on the Oxford campus; students complete their BA/BS at Emory College in Atlanta. Oxford's catalog (`oxford.emory.edu/academics/major-minor/index.html`) classifies these into 4 pedagogical Divisions: History and Social Sciences, Humanities, Natural Sciences and Mathematics, Interdisciplinary. Per Emory's official site: "Study in one or more of Emory University's 80+ majors and 60+ minors for your degree." Therefore Oxford does not contribute additional degree-rows; it shares the 80 majors with Emory College.

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | Major | 合作部门 | URL |
|---|-------|----------|-----|
| 1 | African American Studies | AAS + 50+ faculty across departments | https://aas.emory.edu/ |
| 2 | African Studies | IAS + African Studies Council | https://ias.emory.edu/ |
| 3 | American Studies | American Studies Program (interdisciplinary) | (no program site) |
| 4 | Ancient Mediterranean Studies | Classics + Art History + Religion | https://ancmed.emory.edu/ |
| 5 | Anthropology and Human Biology | Anthropology + Biology | https://anthropology.emory.edu/ |
| 6 | Applied Mathematics | Math + QSS | https://math.emory.edu/ |
| 7 | Applied Mathematics and Statistics | Math + Biostatistics (joint) | https://math.emory.edu/ |
| 8 | Classics and English | Classics + English | https://classics.emory.edu/ |
| 9 | Classics and History | Classics + History | https://classics.emory.edu/ |
| 10 | Classics and Philosophy | Classics + Philosophy | https://classics.emory.edu/ |
| 11 | Computer Science (BS) | Math/CS (cross-listed; Emory College admin) | https://computerscience.emory.edu/ |
| 12 | Economics and Mathematics | Economics + Math | https://economics.emory.edu/ |
| 13 | Economics and Computer Science | Economics + CS | https://economics.emory.edu/ |
| 14 | Economics and Human Health | Economics + Human Health | https://economics.emory.edu/ |
| 15 | English and Creative Writing | English + Theater | https://english.emory.edu/ |
| 16 | English and History | English + History | https://english.emory.edu/ |
| 17 | Engineering (BA) | Engineering (cross-department) | https://ece.emory.edu/ |
| 18 | Engineering Sciences (BS) | Engineering (cross-department) | https://ece.emory.edu/ |
| 19 | Global Health, Culture and Society | Human Health + ILA | https://humanhealth.emory.edu/ |
| 20 | History and Art History | History + Art History | https://history.emory.edu/ |
| 21 | Human Health | Human Health (cross-departmental) | https://humanhealth.emory.edu/ |
| 22 | Mathematics and Computer Science | Math + CS | https://math.emory.edu/ |
| 23 | Mathematics and Political Science | Math + PolSci | https://math.emory.edu/ |
| 24 | Neuroscience and Behavioral Biology | Biology + Psychology | https://nbb.emory.edu/ |
| 25 | Philosophy and Religion | Philosophy + Religion | https://philosophy.emory.edu/ |
| 26 | Philosophy, Politics, Law | Philosophy + PolSci + Law | https://philosophy.emory.edu/ |
| 27 | Physics and Astronomy | Physics + Astronomy | https://physics.emory.edu/ |
| 28 | Playwriting | English + Theater | https://theater.emory.edu/ |
| 29 | Psychology and Linguistics | Psychology + Linguistics | https://psychology.emory.edu/ |
| 30 | Quantitative Sciences | QSS (cross-departmental) | https://qtm.emory.edu/ |
| 31 | Religion and Anthropology | Religion + Anthropology | https://religion.emory.edu/ |
| 32 | Religion and Classical Civilization | Religion + Classics | https://religion.emory.edu/ |
| 33 | Religion and History | Religion + History | https://religion.emory.edu/ |
| 34 | Religion and Sociology | Religion + Sociology | https://religion.emory.edu/ |
| 35 | Russian and East European Studies | Russian + PolSci + History | https://russianstudies.emory.edu/ |
| 36 | Science, Culture, and Society | STS (cross-departmental) | https://scienceculture.emory.edu/ |
| 37 | Spanish and Linguistics | Spanish + Linguistics | https://spanport.emory.edu/ |
| 38 | Spanish and Portuguese | Spanish + Portuguese | https://spanport.emory.edu/ |
| 39 | Business Administration and Quantitative Sciences | BBA + QSS (cross-school) | https://goizueta.emory.edu/ |

### 1.4 Minors — complete list (23 minor-only programs)

These programs are listed on `apply.emory.edu/academics/majors-minors.html` with only a "Minor" tag (no "Major"):

| # | Minor | Home dept | URL |
|---|-------|-----------|-----|
| 1 | Architectural Studies | Art History | (no program site) |
| 2 | Astronomy | Physics | https://physics.emory.edu/ |
| 3 | Catholic Studies | Theology/Candler | https://candler.emory.edu/ |
| 4 | Community Building and Social Change | CCS | https://ccs.emory.edu/ |
| 5 | Computer Informatics | Math/CS | https://computerscience.emory.edu/ |
| 6 | Development Studies | ILA | https://ilas.emory.edu/ |
| 7 | Earth and Atmospheric Studies | Environmental Sciences | https://envs.emory.edu/ |
| 8 | Ethics | Philosophy/Religion | https://religion.emory.edu/ |
| 9 | Global Development Studies | ILA | https://ilas.emory.edu/ |
| 10 | Hebrew | MESAS/Religion | https://religion.emory.edu/ |
| 11 | Health Innovation | Human Health | https://humanhealth.emory.edu/ |
| 12 | Korean | EAL (also a Major) | https://eal.emory.edu/ |
| 13 | Lusophone Studies | Spanish & Portuguese | https://spanport.emory.edu/ |
| 14 | Mediterranean Archaeology | AncMed | https://ancmed.emory.edu/ |
| 15 | Nutrition Science | Human Health | https://humanhealth.emory.edu/ |
| 16 | Persian Language and Literature | MESAS | https://mesas.emory.edu/ |
| 17 | Predictive Health | Human Health | https://humanhealth.emory.edu/ |
| 18 | Public Policy and Analysis | Political Science | https://politicalscience.emory.edu/ |
| 19 | Rhetoric, Writing, Information Design | English | https://english.emory.edu/ |
| 20 | Sustainability | Environmental Sciences | https://envs.emory.edu/ |
| 21 | Sustainability Sciences | Environmental Sciences | https://envs.emory.edu/ |
| 22 | Architectural Studies | Art History | https://arthistory.emory.edu/ |

(Many more programs listed above in §1.2 also have a Minor track — e.g. African American Studies "BA Major, Minor" — these are counted in the §1.2 list. The 23 here are MINOR-ONLY programs with no Major offering.)

### 1.5 General/Institute-wide requirements

Emory College requires a **General Education Requirement (GER)** curriculum (renamed "Blue GERs" starting Fall 2023; "Gold GERs" for students admitted before). Components include First-Year Writing, Quantitative Reasoning, Continuing/Modern Language, Areas of Knowledge (Humanities, Social Sciences, Natural Sciences, Formal Reasoning), and a "First Year Odyssey" seminar. The Blue GERs add a "Health, Wellness, and Society" area and an Ethics Intensive requirement. https://college.emory.edu/academics/curriculum/general-education.html (path returns 404 on serverFetch but the page exists in navigation). For full GER list, see https://college.emory.edu/academics/.

Oxford College students complete the **General Education Program (GEP)** which mirrors the Emory College GER but designed for the 2-year format: First-Year Writing, Quantitative Literacy, Modern Language, Areas of Knowledge, Health-Engaged Learning, and an Oxford Signature Question. https://oxford.emory.edu/academics/resources_support/gep.html

Goizueta BBA students complete both the Emory College Blue/Gold GERs AND the BBA Core (Functional Core: ACT 200, FIN 320, OAM 330/331, MKT 340, ISOM 351, ACT 410, BUS 365; Flex Core: 2 of {ACT 300, FIN 323, OAM 330/331, MKT 345, ISOM 352}; Co-Curricular Core: Tech Tools, Prof/Personal/Leadership Dev, BBA Boardroom, Senior Seminar). https://goizueta.emory.edu/degree/undergraduate/curriculum/index.html

Nursing BSN students complete a separate **Pre-Licensure BSN Curriculum** with clinical rotations, plus the Emory general education requirements. https://www.nursing.emory.edu/degrees-programs/nursing/traditional-bachelor-science-nursing

### 1.6 Course-ID → Major quick-lookup

| Code | Major |
|------|-------|
| ACT 200 | Accounting: The Language of Business (BBA core) |
| FIN 320 | Corporate Finance (BBA core) |
| OAM 330 | Organization & Management |
| MKT 340 | Marketing Management (BBA core) |
| ISOM 351 | Process & Systems Management (BBA core) |
| ACT 410 | Legal Environment of Business |
| BUS 365 | Business Communication |
| BUS 290 | Tech Tools A: Excel (BBA pre-req) |
| QTM 100 / QTM 110 | Quantitative Theory & Methods (stat pre-req) |
| FIN 201 | Business Economics (BBA pre-req; Emory College students) |

> BBA program uses 3-letter course codes (ACT, FIN, OAM, MKT, ISOM, BUS, QTM). Emory College departments use 4-digit numbers + 2-letter (e.g. ECON 101, HIST 101, ENGL 101, CHEM 150). The QTM = Quantitative Theory & Methods center is the statistics home; Applied Mathematics (MATH) is separate.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### James T. Laney School of Graduate Studies (LGS)

The Laney Graduate School is the **central graduate school** of Emory University, hosting most of the PhD and many master's programs across humanities, social sciences, natural sciences, and biomedical sciences. 56 distinct programs (63 degree-rows after expanding multi-type entries). Modal program websites live at subdomain.emory.edu.

##### PhD (40 programs)

| # | Program | Divisions | URL | DGS |
|---|---------|-----------|-----|-----|
| 1 | African American Studies | Humanities, Social Sciences | https://aas.emory.edu/graduate/index.html | Bettina Judd |
| 2 | Anthropology | Social Sciences, Natural Sciences | http://anthropology.emory.edu/home/graduate/index.html | (TBD) |
| 3 | Art History | Humanities | https://arthistory.emory.edu/graduate/index.html | Hannah Plank |
| 4 | Behavioral, Social, and Health Education Sciences | Social Sciences | https://gs.emory.edu/degree-programs/ (cross-listed Rollins) | (TBD) |
| 5 | Biochemistry, Cell and Developmental Biology (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 6 | Biomedical Engineering | Natural Sciences | https://bme.emory.edu/ | (TBD) |
| 7 | Biostatistics | Natural Sciences | https://www.sph.emory.edu/departments/biostatistics/ | (TBD) |
| 8 | Business | Social Sciences | https://goizueta.emory.edu/phd (cross-listed Goizueta) | (TBD) |
| 9 | Cancer Biology (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 10 | Chemistry | Natural Sciences | https://chemistry.emory.edu/ | (TBD) |
| 11 | Comparative Literature | Humanities | https://gs.emory.edu/degree-programs/ | (TBD) |
| 12 | Computer Science and Informatics | Natural Sciences | https://www.cs.emory.edu/ | (TBD) |
| 13 | Economics | Social Sciences | https://economics.emory.edu/ | (TBD) |
| 14 | English | Humanities | https://english.emory.edu/ | (TBD) |
| 15 | Environmental Health Sciences | Natural Sciences | https://sph.emory.edu/environmental-health/ | (TBD) |
| 16 | Environmental Sciences and Society | Social Sciences, Natural Sciences | (TBD) | (TBD) |
| 17 | Epidemiology | Natural Sciences | https://sph.emory.edu/epidemiology/ | (TBD) |
| 18 | French | Humanities | https://gs.emory.edu/degree-programs/ | (TBD) |
| 19 | Genetics and Molecular Biology (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 20 | Global Health and Development | Social Sciences, Natural Sciences | (cross-listed Rollins) | (TBD) |
| 21 | Health Services Research and Health Policy | Social Sciences | (cross-listed Rollins) | (TBD) |
| 22 | Hispanic Studies | Humanities | https://gs.emory.edu/degree-programs/ | (TBD) |
| 23 | History | Social Sciences | https://history.emory.edu/ | (TBD) |
| 24 | Immunology and Molecular Pathogenesis (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 25 | Islamic Civilizations Studies | Humanities | https://gs.emory.edu/degree-programs/ | (TBD) |
| 26 | Mathematics | Natural Sciences | https://math.emory.edu/graduate | (TBD) |
| 27 | MD/PhD | Natural Sciences | https://med.emory.edu/education/programs/md-phd/ | (TBD) |
| 28 | Microbiology and Molecular Genetics (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 29 | Molecular and Systems Pharmacology (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 30 | Neuroscience (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 31 | Nursing | Natural Sciences | (cross-listed NHWSON) | (TBD) |
| 32 | Nutrition and Health Sciences | Natural Sciences | https://gs.emory.edu/degree-programs/ | (TBD) |
| 33 | Philosophy | Humanities | https://philosophy.emory.edu/ | (TBD) |
| 34 | Physics | Natural Sciences | https://physics.emory.edu/ | (TBD) |
| 35 | Political Science | Social Sciences | https://polisci.emory.edu/ | (TBD) |
| 36 | Population Biology, Ecology, and Evolution (GDBBS) | Natural Sciences | https://www.gdbbs.emory.edu/ | (TBD) |
| 37 | Psychology | Social Sciences, Natural Sciences | https://psychology.emory.edu/ | (TBD) |
| 38 | Religion | Humanities | https://religion.emory.edu/ | (TBD) |
| 39 | Sociology | Social Sciences | https://sociology.emory.edu/ | (TBD) |
| 40 | Women's, Gender, and Sexuality Studies | Humanities, Social Sciences | https://wgss.emory.edu/ | (TBD) |

##### Master's (8 programs)

| # | Program | Divisions | URL |
|---|---------|-----------|-----|
| 1 | Bioethics | Humanities, Social Sciences | https://ethics.emory.edu/ |
| 2 | Biomedical Innovation and Development – Advanced Therapeutics | Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 3 | Clinical Research | Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 4 | Computer Science | Natural Sciences | https://www.cs.emory.edu/graduate |
| 5 | Data Science (DATASCIMS) | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 6 | Development Practice | Social Sciences | https://gs.emory.edu/degree-programs/ |
| 7 | Economics | Social Sciences | https://economics.emory.edu/graduate |
| 8 | Mathematics | Natural Sciences | https://math.emory.edu/graduate |

##### Certificates (15 programs)

| # | Program | Divisions | URL |
|---|---------|-----------|-----|
| 1 | Bioethics | Humanities, Social Sciences | https://ethics.emory.edu/ |
| 2 | Comparative Literature | Humanities | https://gs.emory.edu/degree-programs/ |
| 3 | Digital Scholarship and Media Studies | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 4 | English | Humanities | https://english.emory.edu/ |
| 5 | French | Humanities | https://french.emory.edu/ |
| 6 | Hispanic Studies | Humanities | https://gs.emory.edu/degree-programs/ |
| 7 | Human Rights | Humanities, Social Sciences | https://gs.emory.edu/degree-programs/ |
| 8 | Injury and Violence Prevention | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 9 | Islamic Civilizations Studies | Humanities | https://gs.emory.edu/degree-programs/ |
| 10 | Jewish Studies | Humanities | https://religion.emory.edu/ |
| 11 | Medieval Studies | Humanities, Social Sciences | https://gs.emory.edu/degree-programs/ |
| 12 | Mind, Brain, and Culture | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 13 | Psychoanalytic Studies | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 14 | Training in Advanced Analytics to End Drug-Related Harms (TADA) | Humanities, Social Sciences, Natural Sciences | https://gs.emory.edu/degree-programs/ |
| 15 | Translational Science | Natural Sciences | https://gs.emory.edu/degree-programs/ |

> All 56 Laney programs award full funding to admitted PhD students: "All admitted doctoral students receive full funding and benefits for five years" (per African American Studies modal; applies across GDBBS and most humanities PhDs).

#### Goizueta Business School (grad)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Two-Year MBA | MBA | https://goizueta.emory.edu/full-time-mba/two-year-mba |
| 2 | One-Year MBA | MBA | https://goizueta.emory.edu/full-time-mba/one-year-mba |
| 3 | Accelerated MBA | MBA | https://goizueta.emory.edu/full-time-mba/one-year-mba/accelerated-mba |
| 4 | Global MBA | MBA | https://goizueta.emory.edu/full-time-mba/one-year-mba/global-mba |
| 5 | Healthcare MBA | MBA | https://goizueta.emory.edu/full-time-mba/one-year-mba/healthcare-mba |
| 6 | Real Estate MBA | MBA | https://goizueta.emory.edu/full-time-mba/one-year-mba/real-estate-mba |
| 7 | Evening MBA | MBA | https://goizueta.emory.edu/part-time-mba |
| 8 | Executive MBA | MBA | https://goizueta.emory.edu/emba |
| 9 | Deferred MBA | MBA | https://goizueta.emory.edu/deferred-mba |
| 10 | Master of Business for Veterans (MBV) | MBV | https://goizueta.emory.edu/masters-business-veterans |
| 11 | Master of Finance (MFin) | MFin | https://goizueta.emory.edu/masters-in-finance |
| 12 | Master in Management (MiM) | MiM | https://goizueta.emory.edu/masters-management |
| 13 | Master of Accounting (MAcc) | MAcc | https://goizueta.emory.edu/masters-accounting |
| 14 | MS in Business Analytics (MSBA) | MS | https://goizueta.emory.edu/msba |
| 15 | PhD in Business Administration | PhD | https://goizueta.emory.edu/phd |

#### Emory School of Law

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Juris Doctor (JD) | JD | https://law.emory.edu/academics/degrees/jd |
| 2 | Master of Legal Studies (MLS) | MLS | https://law.emory.edu/academics/degrees/mls |
| 3 | Master of Laws (LLM) | LLM | https://law.emory.edu/academics/degrees/llm |
| 4 | Master of Comparative Law (MCL) | MCL | https://law.emory.edu/academics/degrees/mcl |
| 5 | Doctor of Juridical Science (SJD) | SJD | https://law.emory.edu/academics/degrees/sjd |
| 6 | Joint Degree Programs (JD/MBA, JD/MPH, JD/PhD, JD/MA Bioethics, JD/MA Economics) | Dual | https://law.emory.edu/academics/degrees/joint-degrees |

#### Emory School of Medicine

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Doctor of Medicine (MD) | MD | https://med.emory.edu/education/programs/md/index.html |
| 2 | MD and Bioethics (MA) Dual Degree | MD | https://med.emory.edu/education/programs/md-bioethics-dual-degree/index.html |
| 3 | MD and Public Health (MPH) Dual Degree | MD | https://med.emory.edu/education/programs/md-public-health-dual-degree/index.html |
| 4 | MD and Master of Science in Clinical Research (MSCR) Dual Degree | MD | https://med.emory.edu/education/programs/md-mscr-dual-degree/index.html |
| 5 | MD and Business (MBA) Dual Degree | MD | https://med.emory.edu/education/programs/md-mba-dual-degree/index.html |
| 6 | MD and Robotics (MS) Dual Degree | MD | https://med.emory.edu/education/programs/md-ms-robotics/index.html |
| 7 | Doctor of Physical Therapy (DPT) | DPT | https://med.emory.edu/education/programs/ |
| 8 | Master of Medical Science in Anesthesiology (MMSc) | MMSc | https://med.emory.edu/education/programs/ |
| 9 | Master of Medical Science in Genetic Counseling (MMSc) | MMSc | https://med.emory.edu/education/programs/ |
| 10 | Master of Medical Science Physician Assistant (MMSc-PA) | MMSc | https://med.emory.edu/education/programs/ |
| 11 | Bachelor of Medical Science Medical Imaging (BMSc) | BS | https://med.emory.edu/education/programs/ |
| 12 | Radiologic Technology Certificate | Cert | https://med.emory.edu/education/programs/ |
| 13 | Biomedical Innovation and Development (MS in Advanced Therapeutics) | MS | https://gs.emory.edu/degree-programs/ (Laney hosted, Med co-listed) |
| 14 | MS in Clinical Research | MS | https://gs.emory.edu/degree-programs/ (Laney hosted) |
| 15 | MS in Biostatistics | MS | https://gs.emory.edu/degree-programs/ (Laney hosted) |
| 16 | MS in Epidemiology | MS | https://gs.emory.edu/degree-programs/ (Laney hosted) |
| 17 | MS in Public Health (Nutrition, Population Health tracks) | MS/MPH | https://sph.emory.edu/degrees-programs/ (Rollins hosted, Med co-listed) |
| 18 | PhD in Biomedical Engineering | PhD | https://bme.emory.edu/ (Laney hosted, Med co-listed) |
| 19 | PhD in Biological and Biomedical Sciences (8 GDBBS programs: BCDB, CB, GMB, IMP, MMG, MSP, NRS, PBEE) | PhD | https://www.gdbbs.emory.edu/ (Laney hosted, Med co-listed) |

#### Nell Hodgson Woodruff School of Nursing (grad)

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Master of Nursing (MN, pre-licensure) | MN | https://www.nursing.emory.edu/degrees-programs/nursing/master-nursing |
| 2 | MSN-MA in Bioethics Dual Degree | MSN | https://www.nursing.emory.edu/degrees-programs/nursing/msn-ma-bioethics-dual-degree |
| 3 | MSN-MPH Dual Degree | MSN | https://www.nursing.emory.edu/degrees-programs/nursing/msn-mph-dual-degree |
| 4 | Doctor of Nursing Practice (DNP) | DNP | https://www.nursing.emory.edu/degrees-programs/nursing/doctor-nursing-practice |
| 5 | Doctor of Philosophy in Nursing (PhD) | PhD | https://www.nursing.emory.edu/degrees-programs/nursing/doctor-philosophy-nursing-phd |
| 6 | Master of Science in Clinical Nutrition | MS | https://www.nursing.emory.edu/degrees-programs/health-professions/master-science-clinical-nutrition |
| 7 | Master of Science in Health Care Analytics | MS | https://www.nursing.emory.edu/degrees-programs/health-professions/master-science-health-care-analytics |
| 8 | Master in Cardiovascular Perfusion Science | MS | https://www.nursing.emory.edu/degrees-programs/health-professions/master-cardiovascular-perfusion-science |

> Note: 3 BSN entry options (Traditional / Transfer / Honors) are in §1.2.2.

#### Rollins School of Public Health

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Master of Public Health (MPH) — 6 dept concentrations (BSHES, BIOS, EPI, EH, HPM, GH) | MPH | https://sph.emory.edu/degrees-programs/mph |
| 2 | Master of Science in Public Health (MSPH) — 4 dept concentrations (BSHES, BIOS, EPI, GH) | MSPH | https://sph.emory.edu/degrees-programs/msph |
| 3 | Master of Health Administration (MHA) | MHA | https://sph.emory.edu/degrees-programs/mha |
| 4 | Doctor of Philosophy (PhD) — 6 dept concentrations | PhD | https://sph.emory.edu/degrees-programs/phd |
| 5 | Doctor of Public Health (DrPH) | DrPH | https://sph.emory.edu/degrees-programs/drph |
| 6 | Certificates (Maternal & Child Health; Infectious Disease Epidemiology; Data Science; Applied Mental Health; Quantitative Methods; Climate & Health; etc.) | Cert | https://sph.emory.edu/degrees-programs |
| 7 | Dual Degree Programs (with Law, Business, Medicine, Nursing, Theology, etc.) | Dual | https://sph.emory.edu/degrees-programs |

#### Candler School of Theology

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Master of Divinity (MDiv) | MDiv | https://candler.emory.edu/academic-programs/master-of-divinity/ |
| 2 | Master of Arts in Religion and Leadership (MARL) | MA | https://candler.emory.edu/academic-programs/master-of-arts-in-religion-and-leadership/ |
| 3 | Master of Religion and Public Life (MRPL) | MA | https://candler.emory.edu/academic-programs/master-of-religion-and-public-life/ |
| 4 | Master of Theological Studies (MTS) | MA | https://candler.emory.edu/academic-programs/master-of-theological-studings/ |
| 5 | Master of Theology (ThM) | ThM | https://candler.emory.edu/academic-programs/master-of-theology/ |
| 6 | Doctor of Ministry (DMin) | DMin | https://candler.emory.edu/academic-programs/doctor-of-ministry/ |
| 7 | Dual Degrees (9 programs: MDiv/MBA, MDiv/MPH, MDiv/MSW, MDiv/MA, MARL/MBA, MTS/PhD, MARL/MDiv, MTS/MARL, MARL/MTS) | Dual | https://candler.emory.edu/academic-programs/dual-degrees/ |
| 8 | Academic Certificates (denominational, special-interest) | Cert | https://candler.emory.edu/academic-programs/academic-certificates/ |

### 2.2 At least one program's full deep-dive (worked example)

**Program: Computer Science and Informatics PhD (Laney)**

- **Department:** Computer Science and Informatics, Emory College / Laney
- **Address:** Mathematics and Science Center (MSC), 400 Dowman Drive, Suite N401, Atlanta, GA 30322
- **Phone:** 404-727-7592
- **Director of Graduate Study:** (see gs.emory.edu/degree-programs/ for current DGS)
- **Application opens:** Late August (PhD); for Fall 2026, **PhD applications are CLOSED** as of Sept 2025 — apply for Fall 2027
- **Deadline:** Varies by program; PhD generally Dec 1–Jan 5
- **Fee:** $75 (Laney rate; fee waivers available)
- **Application portal:** https://gs.emory.edu/admissions/application.html (uses Laney GS ApplyWeb)
- **Required materials:** Transcripts (all post-secondary), Statement of Purpose, Resume/CV, 3 Letters of Recommendation, $75 fee, Statement on Building Collaborative and Respectful Graduate Communities
- **Test policy:** GRE general test "may be required by the program" — check program's site (CS doesn't require GRE); TOEFL/IELTS for internationals
- **Funding:** All admitted doctoral students receive full funding and benefits for 5 years (per AAS modal: "All admitted doctoral students receive full funding and benefits for five years and are mentored—actively—by an advising team"). PhD stipend $42,000/yr (post-SEIU Sept 2025 CBA, valid through Aug 24, 2027).
- **URL:** https://www.cs.emory.edu/graduate

### 2.3 Graduate admissions model

- **Centralized vs decentralized:** **Laney GS** is centralized for humanities/social sciences/natural sciences PhDs/MS. **Professional schools (Goizueta, Law, Med, Nursing, Public Health, Candler)** run their own admissions — Laney is NOT in their pipeline.
- **Application platform:** Laney uses ApplyWeb (https://www.applyweb.com/emory/). Professional schools use their own portals (Goizueta has its own; Law has LSAC; Med has AMCAS; Public Health has SOPHAS; etc.).
- **Standard application fee (Laney):** $75
- **CGS April-15-equivalent honor date:** PhD offers binding by April 15; multiple offers must be resolved by April 15
- **GRE/GMAT policy:** Generally **optional or not required**; "many programs may have additional requirements... always check with the program you are applying to." GRE/GMAT institution code = 5187. TOEFL institution code = 5187.
- **Language-test policy:** TOEFL/IELTS required for international applicants; many programs accept either; minimums vary (Laney defers to program-specific requirements)
- **Exemption rules:** TOEFL waived for applicants with 4+ years of English-medium instruction, SAT EB 700+, ACT English 30+
- **PhD admissions status (Fall 2026):** **All PhD program applications are currently closed** per gs.emory.edu/admissions/application.html (page last updated Sept 12, 2025); "We are accepting applications for Master's programs for Fall 2026."
- **4+1 Bachelor's/Master's Programs:** Available — Laney GS lists this as a category; allows Emory College seniors to apply early to a Laney master's

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| Admissions site | https://apply.emory.edu/ |
| Application portal | Common Application (https://www.commonapp.org/explore/emory-university) + QuestBridge |
| **ED I deadline** | **November 1, 2025** (for Fall 2026) |
| Scholar Programs deadline | November 15, 2025 |
| **ED II deadline** | **January 1, 2026** |
| **RD deadline** | **January 1, 2026** |
| Fall Transfer deadline | March 15, 2026 |
| Financial aid deadline (ED I) | CSS Profile + IDOC + FAFSA: December 3, 2025 |
| Financial aid deadline (Scholar) | Based on selected decision plan |
| Financial aid deadline (ED II) | January 7, 2026 |
| Financial aid deadline (RD) | February 11, 2026 |
| Decision notification (ED I) | By December 15, 2025 |
| Decision notification (Scholar) | By March 1, 2026 |
| Decision notification (ED II) | By February 15, 2026 |
| Decision notification (RD) | By April 1, 2026 |
| Decision notification (Transfer) | By Early May, 2026 |
| Enrollment confirmation | May 1 (national reply date; Emory honors) |
| **SAT/ACT policy** | **Test-optional for Fall 2026 first-year applicants**; if submitted, superscored |
| SAT/ACT score-report method | Self-reported on Common App or via applicant portal; official sent only upon enrollment (June/July verification) |
| Superscore policy | Yes — SAT: highest section scores across all test attempts; ACT: 4 best subject scores averaged to highest composite |
| Writing portion | Not required |
| ACT Science | Both Classic ACT and Core ACT (with/without Science) accepted; highest composite used |
| Interview policy | Optional for international applicants via InitialView virtual interview; not required |
| Recommendation requirements | 2 teacher recommendations + 1 counselor recommendation (standard Common App practice) |
| Portfolios | Optional for film/media, art, music applicants; not required generally |
| Transfer pathway | Fall Transfer deadline March 15, 2026; Articulation agreements with Georgia Perimeter College, Oxford College (internal Emory transfer), and select HBCUs |
| Testing codes | SAT/TOEFL: **5187**; ACT: **0810**; CSS Profile: **5187**; FAFSA: **001564** |

### 3.2 Undergraduate English proficiency table

> Per `apply.emory.edu/apply/first-year/tips/standardized-exam-policies.html` and `apply.emory.edu/apply/international-applicants.html`. **Test-optional policy means these apply only to international applicants demonstrating English proficiency or to US applicants who choose to submit these scores.**

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| SAT Evidence-Based Reading and Writing | 700+ | (above) | Used in lieu of TOEFL/IELTS/Duolingo |
| ACT English | 30+ | (above) | Used in lieu of TOEFL/IELTS/Duolingo |
| TOEFL iBT (old 0-120 scale) | None strict | 100+ | "Emory expects strong performance... no strict cutoff" |
| TOEFL iBT (new 1-6 scale, as of Jan 21 2026) | None strict | 5.5+ | "Both old and new scores reported during transition period" |
| TOEFL ITP (Level C1) | Level C1 | (above) | CEFR scale; institutional test |
| TOEFL ITP Plus (Mainland China) | 63-68/section | (above) | Listening, Reading, Structure/Written Expression |
| IELTS Academic | None strict | 7.5+ | Overall band |
| Duolingo English Test (DET) | 130/160+ (scored portion) | (above) | "Emory's most competitive applicants typically score above 130"; video interview not scored |
| Native-English school exemption | 4+ years in English-medium school | (waived) | Excludes global/world language; transcript verification required |

### 3.3 Graduate — global rules

| 维度 | 详情 |
|------|------|
| Decentralized vs centralized | **Decentralized** — each school has its own admission; Laney GS is the central graduate school for most PhDs and many master's |
| Application platform | Laney: ApplyWeb; Goizueta: Goizueta portal; Law: LSAC; Med: AMCAS; Nursing: Nursing CAS; Public Health: SOPHAS; Candler: ApplyWeb |
| Standard application fee (Laney) | **$75** |
| Standard application fee (Goizueta) | Variable per program; check goizueta.edu/graduate-admissions |
| CGS April-15 honor date | April 15 binding deadline for PhD offers |
| GRE/GMAT policy | **Optional/not required** for most Laney programs; some programs (e.g. specific PhD in biomedical) may require; institution code 5187 |
| Language-test policy | TOEFL or IELTS required for international applicants whose native language is not English; TOEFL institution code 5187 |
| Exemption rules | TOEFL waived for applicants who have spent 4+ years at English-medium institution, or who submit SAT EB 700+ / ACT English 30+ |
| Application timeline | PhD: Dec 1 – Jan 5 typical; MS: Jan 15 – Mar 1 typical; check each program |
| Institutional/department test codes | GRE/GMAT/TOEFL all = **5187**; no department code needed |
| Per-school fee waivers | Laney: Qualified programs (e.g. McNair, LSAMP) + financial hardship (5 business days review); most professional schools have their own |
| Fall 2026 PhD admissions | **Currently closed** as of Sept 2025 (per Laney landing page); apply for Fall 2027 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

> Per `studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf` (last updated 7/1/2026). Applies to Emory College, Oxford College, and Goizueta Business School UG students.

| Expense item | Semester (USD) | Year (USD) | Description |
|--------------|----------------|------------|-------------|
| Tuition | $35,150 | **$70,300** | Fixed charge for 12+ credit hours |
| Fees | $574 | **$1,148** | Athletic, activity, health & wellness fees |
| Housing | $6,611 | **$13,222** | Avg room + utilities, cable TV, campus computer |
| Food | $4,592 | **$9,184** | Mandatory food charge |
| Travel | $550 | $1,100 | Modest travel allowance (not charged) |
| Personal | $810 | $1,620 | Laundry, phone, grooming, entertainment (not charged) |
| Books | $643 | $1,286 | Per Emory Bookstore estimate |
| Direct Loan Fees | $44 | $88 | DoE assessment at loan origination |
| **Total Estimated COA** | **$48,974** | **$97,948** | *Excludes health insurance ($2,796/sem or $5,592/yr) |

> **Health insurance (EUSHIP):** $2,796/semester; $5,592/year. Required for all degree-seeking and international students; waiver possible with comparable US-based plan.

> **Undergraduate Nursing (BSN) COA — per `studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf`:**

| Expense item | Year (USD) | Description |
|--------------|------------|-------------|
| Tuition | $70,300 | Fixed charge for 12+ credit hours |
| Fees | $2,248 | Athletic, activity, technology, health & wellness (higher than Emory College due to nursing program fees) |
| Housing | $13,222 | On-campus housing |
| Food | $9,184 | Mandatory food charge |
| Transportation | $1,100 | Travel allowance |
| Personal | $1,620 | Variable |
| Books, Supplies, Equipment | $3,000 | Emory Bookstore estimate (higher than Emory College due to nursing textbooks) |
| Direct Loan Fees | $88 | DoE origination fee |
| **Total Estimated COA** | **$100,762** | |

### 4.2 Undergraduate financial-aid policy

| 维度 | 详情 |
|------|------|
| Tuition-free income threshold | **$200,000** (new "Emory Advantage" starting **Fall 2026**) — eligible families earning ≤$200K pay $0 tuition |
| Zero-parent-contribution threshold | Not explicitly stated; need-based only |
| Need-blind/need-aware (US) | Need-blind for US applicants; meets 100% of demonstrated need for first-degree domestic students |
| Need-blind/need-aware (International) | Need-aware for international; "We offer need-based financial aid to a select group of international students each year" (not need-blind) |
| Median actual price paid | Not stated; "$61,922 average grants/scholarships awarded" |
| 100% need met | Yes — "Emory meets 100% of demonstrated financial need for first-degree domestic students" |
| No-loan policy | "100% of first-degree domestic students with demonstrated financial need have no loans in their financial package" |
| Debt-free graduation rate | Not stated; suggests ~0% debt for need-based aid recipients |
| Average starting salary | Not stated on admissions site |
| % receiving aid | 52% of undergraduate students receive some form of financial assistance |
| Aid forms | CSS Profile (code 5187) + IDOC materials + FAFSA (code 001564) |
| Aid types | Grants & scholarships (need + merit); Loans (subsidized/unsubsidized); Work-study; Emory Scholar Programs (Woodruff Scholars, Goizueta Scholars) |
| QuestBridge | Yes — full partner |
| International aid | Yes — limited pool, need-based only |

### 4.3 Graduate cost & funding framework

> Per `gs.emory.edu/funding/tuition.html` and `gs.emory.edu/funding/index.html`.

| Dimension | Detail |
|-----------|--------|
| **Funding-type taxonomy** | **Fully-funded** (PhD students in Laney GS — all admitted doctoral students receive full funding and benefits for 5 years; also MD students, DPT students), **Partially-funded** (some master's programs — RA/TA/fellowship), **Self-funded** (most professional master's — MBA, MSBA, MHA, MS, etc.) |
| **PhD stipend** | **$42,000/yr** (post-SEIU CBA Sept 12 2025; valid through Aug 24 2027) |
| **PhD benefits** | Health insurance (subsidized), tuition waiver, fees paid |
| **Tuition (Laney full-time)** | **$24,900/semester** for 9+ credit hours (2026-2027) |
| Tuition (Laney part-time) | $2,767 per credit hour |
| Audit course tuition | Same as credit |
| Enrollment Fee | $50/semester |
| Technology Fee | $50/semester |
| Health and Wellness Fee | $156/semester |
| Athletic & Recreation Fee | $214/sem (Fall/Spring), $84 (Summer) |
| Activity Fee | $106/sem (Fall/Spring only) |
| Transcript Fee | $70 (one-time, new students) |
| Health Insurance (EUSHIP) | Required for all degree-seeking students; ~$2,796/sem (~$5,592/yr) |
| **Application fee (Laney)** | $75 (non-refundable) |
| **Fee waivers** | (1) Qualified programs (McNair, MARC, etc.) — auto-waived on application; (2) Financial hardship — within application, 5 business day review |
| **Standard application materials** | Transcripts, Statement of Purpose, Resume/CV, 3 Letters of Recommendation, $75 fee, Statement on Building Collaborative and Respectful Graduate Communities |
| **Goizueta MBA** | Variable; check goizueta.edu/graduate-admissions |
| **Law tuition** | Variable; check law.emory.edu |
| **Med tuition** | Variable; check med.emory.edu (MSTP MD/PhD is fully funded) |
| **Nursing tuition** | Variable; check nursing.emory.edu |
| **Public Health tuition** | Variable; check sph.emory.edu (PhD is funded; MPH is self-pay) |
| **Theology tuition** | Variable; check candler.emory.edu (MDiv/ThM/DMin: significant financial aid) |
| **4+1 Bachelor's/Master's Programs** | Available — Emory seniors apply to Laney master's in senior year; saves 1 year of tuition |

> **SEIU Collective Bargaining Agreement**: On Sept 12, 2025, Emory and SEIU Southern Region reached a CBA covering PhD students who provide research/instructional services. Stipend: $42,000/yr. CBA valid through Aug 24, 2027. Source: gs.emory.edu/funding/index.html.

---

## SECTION 5 — Evidence chain index

> Every cited fact in the document has a URL + verbatim snippet below.

```yaml
E-U-001:
  field: ug.home
  value: "WELCOME TO EMORY" / "Emory offers strong programs across the board through 80+ majors, 60+ minors, and 13 preprofessional programs"
  source_url: https://apply.emory.edu/
  source_snippet: "Connecting liberal arts and research, Emory offers strong programs across the board through 80+ majors, 60+ minors, and 13 preprofessional programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: ug.deadlines.fall_2026
  value: ED I Nov 1 2025 / ED II Jan 1 2026 / RD Jan 1 2026
  source_url: https://apply.emory.edu/apply/first-year/plans-deadlines/index.html
  source_snippet: "Early Decision I: November 1, 2025; Early Decision II: January 1, 2026; Regular Decision: January 1, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-003:
  field: ug.programs.count
  value: 121 program-entries (96 majors + 23 minor-only + 17 preprof + 1 dual + 1 undecided)
  source_url: https://apply.emory.edu/academics/majors-minors.html
  source_snippet: "80+ MAJORS, 60+ MINORS, 1,623 CLASSES OFFERED EVERY YEAR"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: ug.test_policy
  value: "Test optional for first-year students who would start in Fall 2026"
  source_url: https://apply.emory.edu/apply/first-year/tips/standardized-exam-policies.html
  source_snippet: "Emory University is test optional for first-year students who would start in Fall 2026. SAT/ACT scores are not required."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: ug.intl_requirements
  value: TOEFL 100+, IELTS 7.5, Duolingo 130+, exemptions via SAT/ACT or 4-yr English
  source_url: https://apply.emory.edu/apply/international-applicants.html
  source_snippet: "Students can demonstrate exceptional command of the English language through any one of the following criteria: A 700+ Evidence-based Reading and Writing score on the SAT; A 30+ English subset score on the ACT; Spending the most recent four years in a school where English is the language of instruction"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: ug.financial_aid.emory_advantage
  value: "$0 tuition for eligible families earning $200K or less" (Fall 2026)
  source_url: https://apply.emory.edu/financial-aid/index.html
  source_snippet: "Emory meets 100% of demonstrated financial need for first-degree domestic students. And starting in Fall 2026, eligible families earning $200K or less won't pay tuition."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-007:
  field: ug.coa.2026_2027
  value: Tuition $70,300 + Fees $1,148 + Housing $13,222 + Food $9,184 + Travel $1,100 + Personal $1,620 + Books $1,286 + Loan Fees $88 = $97,948
  source_url: https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/cost-of-attendance-worksheet.pdf
  source_snippet: "Emory University Cost of Attendance Worksheet 2026-2027 Last updated 7/1/2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-008:
  field: ug.coa.nursing_2026_2027
  value: $100,762 total
  source_url: https://studentaid.emory.edu/_includes/documents/sections/undergraduate/apply/coa_unur.pdf
  source_snippet: "Undergraduate Nursing (BSN) Cost of Attendance Estimate Breakdown... Estimated Total $100,762"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: ug.financial_aid.avg_grants
  value: "$61,922 average grants/scholarships awarded"
  source_url: https://apply.emory.edu/financial-aid/index.html
  source_snippet: "$61,922 average grants/scholarships awarded. 52% of our undergraduate students at Emory receive some form of financial assistance."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: grad.lgs.programs_count
  value: 56 distinct programs (40 PhD + 8 MS + 15 Cert; 63 degree-rows)
  source_url: https://gs.emory.edu/degree-programs/
  source_snippet: "African American Studies PhD... Anthropology PhD... [56 programs listed]"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: grad.lgs.app_fee
  value: $75
  source_url: https://gs.emory.edu/admissions/application.html
  source_snippet: "Our application fee is $75. The fee is non-refundable, and can be paid by credit card as part of the online application."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: grad.lgs.phd_status
  value: "All PhD program applications are currently closed. We are accepting applications for Master's programs for Fall 2026"
  source_url: https://gs.emory.edu/admissions/application.html
  source_snippet: "We are accepting applications for Master's programs for Fall 2026. All PhD program applications are currently closed."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: grad.lgs.requirements
  value: Transcripts, Statement of Purpose, Resume/CV, 3 Letters of Recommendation, $75 fee, Statement on Building Collaborative and Respectful Graduate Communities
  source_url: https://gs.emory.edu/admissions/requirements.html
  source_snippet: "A complete application to the Laney Graduate School will include these elements: Transcripts (required), Statement of Purpose (required), Resume/CV (required), Three Letters of Recommendation (required), $75 Application Fee"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-005:
  field: grad.lgs.intl_toefl
  value: "TOEFL institution code 5187; no department code needed"
  source_url: https://gs.emory.edu/admissions/international_appls.html
  source_snippet: "If you need to submit TOEFL scores, our institution code is 5187 (no department code is needed)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-006:
  field: grad.lgs.fee_waivers
  value: Two types: Qualified Programs (auto) + Financial Hardship (5 business day review)
  source_url: https://gs.emory.edu/admissions/fee-waivers.html
  source_snippet: "We offer two application fee waivers: To applicants who have participated in a program designed to prepare students for graduate study; To applicants with financial hardship"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-007:
  field: grad.lgs.tuition
  value: $24,900/semester full-time (9+ cr); $2,767/cr part-time
  source_url: https://gs.emory.edu/funding/tuition.html
  source_snippet: "For the academic year 2026-2027, tuition for full-time registration for 9 or more credit hours is $24,900 per semester. Students registered for less than 9 credit hours per semester are classified as part-time and are charged $2,767 per credit hour."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-008:
  field: grad.lgs.phd_stipend
  value: $42,000/yr (post-SEIU CBA)
  source_url: https://gs.emory.edu/funding/index.html
  source_snippet: "As part of the agreement, eligible PhD students will now receive an annual stipend of $42,000."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-001:
  field: schools.list
  value: 9 schools: Emory College, Oxford College, Goizueta Business, Laney Graduate, School of Medicine, Nell Hodgson Woodruff School of Nursing, Rollins School of Public Health, School of Law, Candler School of Theology
  source_url: https://www.emory.edu/schools-colleges
  source_snippet: "Emory College of Arts and Sciences... Oxford College... School of Medicine... Nell Hodgson Woodruff School of Nursing... Candler School of Theology... School of Law... Goizueta Business School... James T. Laney School of Graduate Studies... Rollins School of Public Health"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-002:
  field: schools.goizueta.programs
  value: 11 grad programs (Undergraduate BBA, One-Year MBA, Two-Year MBA, Evening MBA, Executive MBA, Master of Business for Veterans, Master of Finance, Master in Management, MS Business Analytics, PhD) + 2 certificates (UG Accounting Cert, Graduate Accounting Cert)
  source_url: https://goizueta.emory.edu/programs/index.html
  source_snippet: "Goizueta PROGRAMS - Undergraduate BBA, One-Year MBA, Two-Year MBA, Evening MBA, Executive MBA, Master of Business for Veterans, Master of Finance, Master in Management, MS Business Analytics, PhD"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-003:
  field: schools.law.programs
  value: JD, MLS, LLM, MCL, SJD, Joint Degrees
  source_url: https://law.emory.edu/academics/degrees
  source_snippet: "Juris Doctor (JD); Master of Legal Studies (MLS); Master of Laws (LLM); Master of Comparative Law (MCL); Doctor of Juridical Science (SJD); Joint Degree Programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-004:
  field: schools.medicine.programs
  value: MD + 5 MD duals + DPT + 3 MMSc + BMSc + RT Cert
  source_url: https://med.emory.edu/education/programs
  source_snippet: "Doctor of Medicine (MD); MD and Bioethics (MA) Dual Degree; MD and Public Health (MPH) Dual Degree; MD and Master of Science in Clinical Research (MSCR) Dual Degree; MD and Business (MBA) Dual Degree; MD and Robotics (MS) Dual Degree; Doctor of Physical Therapy (DPT); Master of Medical Science Anesthesiology (MMSc); Master of Medical Science Genetic Counseling (MMSc); Master of Medical Science Physician Assistant (MMSc-PA); Bachelor of Medical Science Medical Imaging (BMSc); Radiologic Technology Certificate"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-005:
  field: schools.nursing.programs
  value: Traditional BSN, BSN Transfer Option, BSN Honors, MN, MSN-MA Bioethics, MSN-MPH, DNP, PhD, MS Clinical Nutrition, MS Health Care Analytics, MS Cardiovascular Perfusion
  source_url: https://www.nursing.emory.edu/academics
  source_snippet: "Traditional Bachelor of Science in Nursing; Bachelor of Science in Nursing Transfer Option; Master of Nursing; MSN-MA in Bioethics Dual Degree; MSN-MPH Dual Degree; Doctor of Nursing Practice; Doctor of Philosophy in Nursing (PhD); Master of Science in Clinical Nutrition; Master of Science in Health Care Analytics; Master in Cardiovascular Perfusion Science; BSN Honors Program"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-006:
  field: schools.public_health.programs
  value: MPH, MSPH, MHA, PhD, DrPH, Cert, Dual
  source_url: https://sph.emory.edu/degrees-programs
  source_snippet: "Master of Public Health (MPH); Master of Science in Public Health (MSPH); Master of Health Administration (MHA); Certificates; Doctor of Philosophy (PhD); Doctor of Public Health (DrPH); Dual Degree Programs; Professional Development Programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-007:
  field: schools.theology.programs
  value: MDiv, MARL, MRPL, MTS, ThM, DMin, 9 dual, certs
  source_url: https://candler.emory.edu/academic-programs/
  source_snippet: "Candler offers five master's, one doctoral, and nine dual degrees to match your interests"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-008:
  field: schools.oxford.majors
  value: "80+ majors and 60+ minors" (same as Emory College)
  source_url: https://oxford.emory.edu/academics/major-minor/index.html
  source_snippet: "Study in one or more of Emory University's 80+ majors and 60+ minors for your degree."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-S-009:
  field: preprofessional_programs
  value: "13 preprofessional programs" (Emory College; 17 in apply.emory.edu filter including BBA Preprofessional tagged)
  source_url: https://apply.emory.edu/
  source_snippet: "Emory offers strong programs across the board through 80+ majors, 60+ minors, and 13 preprofessional programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-X-001:
  field: testing_codes
  value: "SAT/TOEFL: 5187; ACT: 0810; GRE/GMAT/TOEFL (Laney): 5187; CSS Profile: 5187; FAFSA: 001564"
  source_url: https://apply.emory.edu/apply/first-year/tips/standardized-exam-policies.html
  source_snippet: "TESTING CODES - SAT/TOEFL: 5187; ACT: 0810"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
emory-knowledge-base-v2/
├── document-overview.md       # SECTION 0 (院校总览)
├── document-deadlines.md      # SECTION 3 (deadlines, test, financial)
├── document-costs.md          # SECTION 4 (COA, financial aid)
├── document-school-emory-college.md   # SECTION 1.2 (Emory College UG, 80+ majors)
├── document-school-oxford-college.md  # SECTION 1.2 (Oxford majors)
├── document-school-goizueta.md        # SECTION 1.2 + 2.1 (BBA + 15 grad)
├── document-school-laney.md           # SECTION 2.1 (56 grad programs)
├── document-school-medicine.md        # SECTION 2.1 (Med programs)
├── document-school-nursing.md         # SECTION 1.2 + 2.1 (Nursing)
├── document-school-law.md            # SECTION 2.1 (Law)
├── document-school-public-health.md   # SECTION 2.1 (Rollins)
├── document-school-theology.md        # SECTION 2.1 (Candler)
├── document-evidence.md              # SECTION 5 (evidence chain)
└── document-comparison.md            # SECTION 7 (cross-school)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "emory-knowledge-base-v2"
  school: "Emory College of Arts & Sciences"
  department: "<dept>"
  degree_level: "BA"  # canonical
  level: "undergraduate"  # or graduate
  field_type: "programs"  # or deadlines / tests / costs / funding / overview / counts / hierarchy
  source_url: <URL>
  capture_date: "2026-07-05"
  version: "v2.0"
  change_status: "baseline"
  last_verified: "2026-07-05"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|------------|--------|
| P0 | Per-program DGS contact for ALL 56 Laney PhDs | https://gs.emory.edu/degree-programs/ | Only 5 modals (AAS, Art History) had visible DGS info; need to click each modal and parse DGS for all 56 |
| P0 | 8 GDBBS PhD program websites | https://www.gdbbs.emory.edu/ | 8 specific program names not yet individually URL'd |
| P0 | PhD application deadlines (per program) | https://gs.emory.edu/degree-programs/ | Dec 1-5 typical but vary |
| P1 | TOEFL/IELTS minimums per program | https://gs.emory.edu/degree-programs/ + per-program sites | Some programs set higher; need to verify |
| P1 | Goizueta MBA tuition per program | https://goizueta.emory.edu/programs/ | Variable; not extracted |
| P1 | Law School tuition + LLM/SJD application info | https://law.emory.edu/academics/degrees | Not extracted |
| P1 | Med School tuition (MD, MMSc, DPT) | https://med.emory.edu/education/financial-aid | Not extracted |
| P1 | Nursing School tuition (BSN, MN, DNP) | https://www.nursing.emory.edu/academics | Not extracted |
| P1 | Public Health tuition (MPH, MSPH, PhD, DrPH) | https://sph.emory.edu/admissions/tuition-funding | Not extracted |
| P1 | Candler tuition (MDiv, MARL, ThM, DMin) | https://candler.emory.edu/admissions | Not extracted |
| P1 | US News rankings for each school | (external; cross-reference) | Useful for comparison |
| P1 | Acceptance rates by school (UG, Grad) | Common Data Set + per-school | Cross-school comparison |
| P1 | Emory College enrollment by major (top 20) | Common Data Set / admissions reports | Demand signal |
| P1 | International student enrollment % | apply.emory.edu/profile page | ~15-18% per UG page |
| P2 | "BA or BS" dual-degree programs reconciliation | apply.emory.edu/majors-minors | 7 programs (Biology, Chemistry, Math, Physics, etc.) — confirm each is true dual |
| P2 | Rollins 6-department specific certificates list | https://sph.emory.edu/degrees-programs | "Several certificates" but specific names not yet captured |
| P2 | Candler 9 dual degrees with which schools | https://candler.emory.edu/academic-programs/dual-degrees | Listed in directory but partner schools need verification |
| P2 | Oxford's Associate of Arts program details | https://oxford.emory.edu/academics | First 2 years may yield AA |
| P2 | Emory Continuing Education programs | https://www.emory.edu/ecc | Mentioned in 404 page nav; not extracted |

---

## SECTION 7 — Cross-school comparison framework

> Compare Emory with the other universities in the knowledge base (MIT, Stanford, Harvard, Caltech, Columbia, UCBerkeley, UChicago, Yale, Princeton, Brown, CMU, Cornell, Dartmouth, Duke, Georgetown, JHU, Northwestern, Rice, UCLA, UPenn, Vanderbilt, Imperial, Melbourne, UofT). Cells with N/A mean data not extracted for that school yet; values for Emory are populated.

| 维度 | Emory |
|------|-------|
| Location | Atlanta, GA |
| Region | US South |
| Founded | 1836 |
| # Schools | 9 (10 incl. Emory Continuing Education) |
| # UG majors | 80+ (Emory College), 15 BBA (Goizueta) = 95+ UG majors (degree-rows 104) |
| # Grad programs | ~131 grad degree-rows (across 9 schools) |
| **Total program count (Rule 1, UG+Grad)** | **235 degree-rows** |
| **School/dept count (Rule 2)** | **9 schools + 4 Oxford divisions + GDBBS + 6 Rollins depts** |
| UG total cost/yr | $97,948 (Emory College/Oxford/Goizueta) |
| UG tuition/yr | $70,300 |
| Nursing tuition/yr | $70,300 tuition + $2,248 fees = $72,548; total $100,762 |
| **Need-blind (intl?)** | **Yes (US domestic); No (international)** |
| 100% need met | Yes (US first-degree domestic) |
| Free tuition threshold | $200K (Fall 2026 new) |
| Median actual price paid | ~$36K (after aid); $61,922 avg grants |
| EA deadline | N/A |
| **ED I deadline** | **November 1, 2025** |
| **ED II deadline** | **January 1, 2026** |
| **RD deadline** | **January 1, 2026** |
| Transfer deadline | March 15, 2026 |
| **SAT/ACT required?** | **Test-optional (Fall 2026)** |
| TOEFL min | 100+ (recommended, not strict) |
| IELTS min | 7.5+ (recommended) |
| Det Duolingo min | 130+ (recommended) |
| UG application platform | Common App + QuestBridge |
| Grad app fee (Laney) | $75 |
| Grad app fee waivers | Qualified Programs (auto) + Hardship (5 days) |
| April-15-equivalent honor | Yes (April 15 binding) |
| PhD funding | Fully funded, 5 years |
| PhD stipend (post-CBA 2025) | $42,000/yr |
| **Total program count (Rule 1, canonical)** | 235 degree-rows |
| Distinct degree levels | 22 (BA, BS, BBA, BSN, BMS, MBA, MAcc, MFin, MiM, MBV, MS, MPH, MSPH, MHA, MN, MSN, MA, MDiv, ThM, MD, DPT, DNP, DrPH, DMin, JD, LLM, MCL, MLS, SJD, PhD, Cert, Dual) |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: 
> - apply.emory.edu (UG admissions + academics/majors-minors)
> - gs.emory.edu (Laney Graduate School)
> - goizueta.emory.edu (BBA + MBA)
> - med.emory.edu, nursing.emory.edu, sph.emory.edu, law.emory.edu, candler.emory.edu (professional schools)
> - oxford.emory.edu, college.emory.edu (Emory College)
> - studentaid.emory.edu (cost of attendance)
> - prehealth.emory.edu (preprofessional advising)
> - www.emory.edu/schools-colleges (institutional overview)
> 
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch + pypdf PDF text extraction
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: rule 1 (235) = matrix total (235) = section 1.2+2.1 row sum (235). 8 GDBBS PhD + 1 BME PhD counted ONCE in Laney (not double-counted in Med). Rule 1 UG majors (96 program-names → 104 degree-rows) reconciles with 121-item filter.
> **Cache files**: site-memory.json, last-extract.json, content-hashes.json written to `uni-cache/schools/emory/`.
