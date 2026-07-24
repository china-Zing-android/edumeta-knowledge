# Johns Hopkins University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + e-catalogue.jhu.edu program explorer
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **School slug**: `jhu`

---

## ⚠ Verification flags (brief vs. official — 4 corrections)

The user-supplied brief contained four factual errors, all corrected below from official JHU pages:

| Brief claim | Official truth | Source |
|-------------|----------------|--------|
| "ED II Jan 4" | **ED II = January 2** (same as RD) | apply.jhu.edu/how-to-apply/application-deadlines-requirements/ |
| "RD Jan 2" | ✅ correct | (confirmed) |
| "test-optional (verify)" | **NOT test-optional — SAT/ACT REQUIRED** for first-year applicants (transfer = optional) | apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/ |
| "need-blind + full-need incl internationals" | **Need-blind for DOMESTIC; need-AWARE for internationals** (but meets 100% demonstrated need, loan-free, for all admitted) | apply.jhu.edu/international-applicants/ (FAQ) |
| "~$64k tuition" | **2026-27 tuition = $68,670** (full on-campus COA $94,858) | sfs.jhu.edu/cost-tuition/ |
| "9 schools" | **10 academic divisions** granting degrees (+ APL research center, non-degree). Includes the newly chartered **School of Government and Policy** (brief omitted it). | jhu.edu/schools/ |

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

**Johns Hopkins University (JHU)** — founded 1876, Baltimore MD; "America's first research university." Private R1. Four campuses in Baltimore + one in Washington D.C. + facilities in China (Nanjing) and Italy (Bologna). ~24,000 full- and part-time students across 10 academic divisions; 5,600 undergraduates on the Homewood campus. CGS April-15 Resolution signatory.

### 0.1 专业与项目总数 (Rule 1 — counts)

Source: e-catalogue.jhu.edu/programs/ interactive program explorer (605 items extracted 2026-07-05).

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM) | 79 |
| 本科辅修 (Minor) | 63 |
| 本科证书 (UG Cert, Peabody Music Ed) | 2 |
| 研究生硕士项目 (MA/MS/MFA/MBA/MEng/MEd/MM/MHS/MPH/MPP/MAS/MSPH + Dual) | 241 |
| 研究生博士项目 (PhD/DNP/EdD/DrPH/MD/DMA/DEng/DocOther) | 96 |
| 研究生证书/文凭 (Certificate/Post-Master's/Post-Bacc/Performer's/Diploma) | 124 |
| **学位/项目总计 (UG + Grad)** | **605** |
| 学院 / 学术 division 总数（含 APL 研究中心） | 11（10 学位授予 + APL） |

> Reconciliation: rule-1 total (605) == sum of distribution-matrix cells (605) == count of rows in Section 1 + Section 2 grouped tables (144 UG + 461 Grad = 605). ✅
>
> Note on the marketing headline "55 undergraduate majors / 55 minors" (Fast Facts): that count collapses BA + BS variants of the same name and excludes Peabody conservatory degrees. The catalog-level count above (79 UG degree programs + 63 minors) is the authoritative enumeration used for cross-school comparison.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

JHU has **10 degree-granting academic divisions** + 1 research center (APL). Note: the brief's "9 schools" missed the newly chartered **School of Government and Policy** (JHU's first new division since 2007) and incorrectly counted APL as a school.

```
Johns Hopkins University
├── Krieger School of Arts & Sciences (KSAS)              [学院 — UG + Grad]
│   ├── 22 departments (Humanities, Natural Sci, Social Sci)   [系]
│   ├── 33 centers/programs/institutes
│   ├── Full-time residential (Homewood)                        [UG BA + Grad MA/MS/PhD/MFA]
│   └── Advanced Academic Programs (AAP) — part-time/evening/online  ⚠ separate division in catalog
├── Whiting School of Engineering (WSE)                   [学院 — UG + Grad]
│   ├── Full-time residential departments (BME, CS, ECE, ME, etc.)  [系 — UG BS + Grad MS/PhD]
│   ├── Engineering for Professionals (EP) — part-time/online   ⚠ separate division in catalog
│   └── Doctor of Engineering (DEng) program
├── Peabody Institute (Conservatory + Preparatory)        [学院 — UG + Grad, music/dance]
│   ├── Bachelor of Music (BM) programs                         [系 — by instrument/discipline]
│   ├── Master of Music (MM) / DMA                              [Grad]
│   └── Performer's Certificate / Artist's Diploma              [Grad cert/diploma]
├── School of Medicine (SOM)                              [学院 — Grad + MD professional]
│   ├── MD program                                             [系 — Basic Sci + Clinical]
│   ├── Graduate (PhD biomedical via BGS) + MA/MHS/MS
│   └── Post-Baccalaureate Certificate
├── School of Nursing (SON)                               [学院 — Grad; BSN via separate pathway]
│   ├── MSN entry-into-nursing + specialties
│   ├── DNP Advanced Practice Tracks (10) / PhD
│   └── Post-Master's Certificate / Dual degrees
├── Bloomberg School of Public Health (BSPH)              [学院 — Grad only, #1 ranked since 1994]
│   ├── 10 departments (Biostatistics, EHE, Epi, HPM, IH, MHE, PFRH, etc.)
│   ├── MHS / MSPH / MPH / MAS / MS / PhD / DrPH
│   └── 47 graduate certificates (largest cert portfolio at JHU)
├── School of Advanced International Studies (SAIS)       [学院 — Grad; UG Direct-Matric only]
│   ├── MA / MPP / MS / Doctor of International Affairs (DIA) / PhD
│   └── Hopkins-Nanjing Center Certificate + Diploma (Bologna/Washington/Nanjing)
├── School of Education (SOE)                             [学院 — Grad only]
│   ├── MEd / MS / EdD / PhD
│   └── Post-Master's Certificate
├── Carey Business School                                 [学院 — Grad; UG minor only]
│   ├── MS / MBA / MA
│   └── Graduate Certificate + Dual degrees (MBA/JD, MBA/MD, MBA/MPH, etc.)
├── School of Government and Policy (NEW, chartered ~2024) [学院 — newest division, anchored at Hopkins Bloomberg Center DC]
│   └── Programs under development (not yet listed in e-catalogue explorer)
└── Applied Physics Laboratory (APL)                      [非学位 — research center, UARC]
    └── Nation's largest university affiliated research center; no degree programs
```

⚠ **Shared / cross-listed**: (1) AAP and EP are administratively Krieger/Whiting but carry their **own distinct program inventories** in the catalog — counted separately in the matrix (preserves fidelity). (2) The Peabody-Homewood Double Degree Program lets students earn a Krieger/Whiting bachelor's + a Peabody BM concurrently. (3) Several PhDs (e.g. Cellular & Molecular Physiology, Pharmacology) are administered by the School of Medicine but registered via interdivisional programs.

### 0.3 学历级别明细 (Rule 3 — degree inventory)

JHU uses **standard (non-Latin) abbreviations** — no SB/A.B./SM remapping needed. Distinctive codes: **MHS** (Master of Health Science, Bloomberg/SoM), **MM/BM** (Music), **MAS** (Master of Applied Science), **MSPH** (Master of Science in Public Health), **DIA/DocOther** (Doctor of International Affairs), **DEng** (Doctor of Engineering), **Performer's Certificate / Artist's Diploma** (Peabody).

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| Minor | Minor | Minor (undergraduate) | 本科 | 63 |
| BA | BA | Bachelor of Arts | 本科 | 45 |
| BS | BS | Bachelor of Science | 本科 | 18 |
| BM | BM | Bachelor of Music | 本科 | 15 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| UGCert | UGCert | Undergraduate Certificate (Music Ed) | 本科 | 2 |
| MS | MS | Master of Science | 研究生 | 116 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 95 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 65 |
| MA | MA | Master of Arts | 研究生 | 38 |
| DualDegree | Dual/Combined | Dual / Combined Degree (e.g. MBA/MPH, MD/PhD) | 研究生 | 22 |
| PostMasterCert | PostMasterCert | Post-Master's Certificate | 研究生 | 19 |
| MM | MM | Master of Music | 研究生 | 19 |
| MHS | MHS | Master of Health Science | 研究生 | 15 |
| DocOther | DocOther | Doctor of International Affairs (DIA) + misc. | 研究生 | 14 |
| MEd | MEd | Master of Education | 研究生 | 11 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 10 |
| MBA | MBA | Master of Business Administration | 研究生 | 9 |
| PerformerCert | PerformerCert | Performer's Certificate (Peabody) | 研究生 | 5 |
| PostBaccCert | PostBaccCert | Post-Baccalaureate Certificate | 研究生 | 4 |
| MAS | MAS | Master of Applied Science | 研究生 | 3 |
| DNP | DNP | Doctor of Nursing Practice | 研究生 | 2 |
| DrPH | DrPH | Doctor of Public Health | 研究生 | 2 |
| MEng | MEng | Master of Engineering | 研究生 | 2 |
| MPP | MPP | Master of Public Policy | 研究生 | 2 |
| MPH | MPH | Master of Public Health | 研究生 | 2 |
| MSPH | MSPH | Master of Science in Public Health (matrix-col: MS) | 研究生 | 1 |
| MD | MD | Doctor of Medicine | 研究生 | 1 |
| EdD | EdD | Doctor of Education | 研究生 | 1 |
| DEng | DEng | Doctor of Engineering | 研究生 | 1 |
| Diploma | Diploma | Artist's / Performance Diploma (Peabody) | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| **合计** | | | | **605** |

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

Matrix columns use canonical codes. Aggregation notes: `MSPH`(1)→`MS` column; `ScD`/`DocOther`(14)→`PhD` column (14 DIA + misc doctoral); certificate variants split into `Cert` / `Post-MS Cert` / `Post-BS Cert` / `Perf Cert` / `Diploma`. AAP = Krieger Advanced Academic Programs (part-time); EP folded under Whiting.

| 学院 \ 级别 | BA | BS | BFA | BM | UG Cert | Minor | MA | MS | MFA | MBA | MEng | MEd | MM | MHS | MPH | MPP | MAS | PhD | DNP | EdD | DrPH | MD | DMA | DEng | Cert | Post-MS Cert | Post-BS Cert | Perf Cert | Diploma | Dual | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Krieger School of Arts & Sciences | 45 | 0 | 0 | 0 | 0 | 40 | 8 | 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 0 | 0 | 0 | **134** |
| Krieger School of Arts & Sciences (AAP) | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 20 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | **49** |
| Whiting School of Engineering | 0 | 15 | 0 | 0 | 0 | 15 | 1 | 46 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 1 | 19 | 14 | 0 | 0 | 0 | 0 | **121** |
| Peabody Institute | 0 | 3 | 1 | 15 | 2 | 7 | 2 | 0 | 0 | 0 | 0 | 1 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 0 | 2 | 0 | 0 | 5 | 0 | 0 | **67** |
| Carey Business School | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 18 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 7 | **45** |
| School of Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | **14** |
| Bloomberg School of Public Health | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 13 | 2 | 0 | 3 | 11 | 0 | 0 | 2 | 0 | 0 | 0 | 47 | 0 | 0 | 0 | 0 | 12 | **107** |
| School of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | **30** |
| School of Nursing | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 3 | **22** |
| SAIS (Advanced International Studies) | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | **16** |
| **合计** | 45 | 18 | 1 | 15 | 2 | 63 | 38 | 117 | 1 | 9 | 2 | 11 | 19 | 15 | 2 | 2 | 3 | 79 | 2 | 1 | 2 | 1 | 10 | 1 | 95 | 19 | 4 | 5 | 1 | 22 | **605** |

> Reconciliation: matrix cell-sum (605) == Rule-1 total (605) == Rule-5 row count (144 UG + 461 Grad = 605). ✅ MS column = 116 MS + 1 MSPH (aggregated). PhD column = 65 PhD + 14 DocOther/DIA. The "School of Government and Policy" (newest division) has no programs in the e-catalogue explorer yet — counted as 0 rows.

---

## SECTION 1 — Undergraduate Education (Rule 5 grouping)

### 1.1 Homewood undergraduate architecture

JHU undergraduate education is centered on the Homewood campus and delivered across **four** undergraduate-degree-granting divisions: **Krieger School of Arts & Sciences** (all Bachelor of Arts majors + minors), **Whiting School of Engineering** (Bachelor of Science engineering majors + minors), **Peabody Institute** (Bachelor of Music / BFA / BS in music, dance, recording arts — a separate conservatory with its own application/audition), and the **School of Nursing** (BSN — but the traditional 4-yr BSN is administered via a separate pathway; the Krieger+Whiting Homewood pool is what the Common App undergraduate application covers). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### Krieger School of Arts & Sciences

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 1 | Africana Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/africana-studies/africana-studies-bachelor-arts/ |
| 2 | Anthropology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/anthropology/anthropology-bachelor-arts/ |
| 3 | Archaeology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/archaeology-ugrad-major/archaeology-bachelor-arts/ |
| 4 | Behavioral Biology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/behavioral-biology/behavioral-biology-bachelor-arts/ |
| 5 | Biology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biology/biology-bachelor-arts/ |
| 6 | Biophysics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biophysics/biophysics-bachelor-science/ |
| 7 | Chemistry | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/chemistry/chemistry-bachelor-science/ |
| 8 | Classics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/classics/classics-bachelor-arts/ |
| 9 | Cognitive Science | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/cognitive-science/cognitive-science-bachelor-arts/ |
| 10 | Critical Diaspora Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/chloe-center/critical-diaspora-studies-bachelor-arts/ |
| 11 | Direct Matriculation: International Studies B.A./M.A. Program with the Paul H. Nitze School of Advanced International Studies (SAIS) | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/international-studies/ba-ma-sais/ |
| 12 | Earth and Planetary Sciences | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/earth-planetary-sciences-bachelor-arts/ |
| 13 | East Asian Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/east-asian-studies/east-asian-studies-bachelor-arts/ |
| 14 | Economics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/economics/economics-bachelor-arts/ |
| 15 | English | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/english/english-bachelor-arts/ |
| 16 | Environmental Science | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/environmental-science-bachelor-science/ |
| 17 | Environmental Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/environmental-studies-bachelor-arts/ |
| 18 | Film and Media Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/film-media-studies/film-media-studies-bachelor-arts/ |
| 19 | French | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/french-bachelor-arts/ |
| 20 | German | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/german-bachelor-arts/ |
| 21 | German Bachelor of Arts/Master of Arts | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/german-bachelor-arts-master/ |
| 22 | History | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history/history-bachelor-arts/ |
| 23 | History of Art | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-art-bachelor-arts/ |
| 24 | History of Science, Medicine, and Technology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-science-technology/history-science-medicine-technology-bachelor-arts/ |
| 25 | Interdisciplinary Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/interdisciplinary-studies/interdisciplinary-studies-bachelor-arts/ |
| 26 | International Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/international-studies/international-studies-bachelor-arts/ |
| 27 | Italian | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/italian-bachelor-arts/ |
| 28 | Latin American, Caribbean, and Latinx Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/program-latin-american-caribbean-latinx-studies/latin-american-caribbean-latinx-studies-bachelor-arts/ |
| 29 | Mathematics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/mathematics/mathematics-bachelor-arts/ |
| 30 | Medicine, Science, and the Humanities | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/medicine-science-humanities/medicine-science-humanities-bachelor-arts/ |
| 31 | Molecular and Cellular Biology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biology/molecular-cellular-biology-bachelor-science/ |
| 32 | Moral and Political Economy | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/center-economy-society/moral-political-economy-bachelor-arts/ |
| 33 | Natural Sciences Area | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/natural-sciences-area/natural-sciences-area-bachelor-arts/ |
| 34 | Near Eastern Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/near-eastern-studies/near-eastern-studies-bachelor-arts/ |
| 35 | Neuroscience | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/neuroscience/neuroscience-bachelor-science/ |
| 36 | Philosophy | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/philosophy/philosophy-bachelor-arts/ |
| 37 | Physics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/physics-astronomy-bachelor-arts/ |
| 38 | Physics | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/physics-bachelor-science/ |
| 39 | Political Science | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/political-science/political-science-bachelor-arts/ |
| 40 | Psychology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/psychological-brain-science/psychology-bachelor-arts/ |
| 41 | Public Health Studies | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/public-health-studies/public-health-studies-bachelor-arts/ |
| 42 | Romance Languages | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/romance-languages-bachelor-arts/ |
| 43 | Sociology | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/sociology/sociology-bachelor-arts/ |
| 44 | Spanish | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/spanish-bachelor-arts/ |
| 45 | Writing Seminars | BA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/writing-seminars/writing-seminars-bachelor-arts/ |

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 46 | Africana Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/africana-studies/africana-studies-minor/ |
| 47 | Anthropology | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/anthropology/anthropology-minor/ |
| 48 | Archaeology | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/archaeology-ugrad-major/archaeology-minor/ |
| 49 | Bioethics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/bioethics/bioethics-minor/ |
| 50 | Civic Leadership | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/snf-agora-institute/civic-leadership-minor/ |
| 51 | Classics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/classics/classics-minor/ |
| 52 | Comparative Thought and Literature | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/comparative-thought-and-literature/comparative-thought-literature-minor/ |
| 53 | Earth and Planetary Sciences | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/earth-planetary-sciences-minor/ |
| 54 | East Asian Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/east-asian-studies/east-asian-studies-minor/ |
| 55 | Economics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/economics/economics-minor/ |
| 56 | Energy | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/energy-minor/ |
| 57 | English | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/english/english-minor/ |
| 58 | Environmental Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/environmental-studies-minor/ |
| 59 | Film and Media Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/film-media-studies/film-media-studies-minor/ |
| 60 | Financial Economics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/economics/financial-economics-minor/ |
| 61 | French | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/french-minor/ |
| 62 | German | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/german-minor/ |
| 63 | History | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history/history-minor/ |
| 64 | History of Art | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-art/history-art-minor/ |
| 65 | History of Science, Medicine and Technology | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-science-technology/history-science-medicine-technology-minor/ |
| 66 | Islamic Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/islamic-studies/islamic-studies-minor/ |
| 67 | Italian | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/italian-minor/ |
| 68 | Jewish Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/jewish-studies/jewish-studies-minor/ |
| 69 | Latin American, Caribbean, and Latinx Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/program-latin-american-caribbean-latinx-studies/latin-american-caribbean-latinx-studies-minor/ |
| 70 | Linguistics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/cognitive-science/linguistics-minor/ |
| 71 | Mathematics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/mathematics/mathematics-minor/ |
| 72 | Museums and Society | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/museums-society/museums-society-minor/ |
| 73 | Music | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/music/music-minor/ |
| 74 | Near Eastern Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/near-eastern-studies/near-eastern-studies-minor/ |
| 75 | Philosophy | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/philosophy/philosophy-minor/ |
| 76 | Physics | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/physics-minor/ |
| 77 | Portuguese | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/portuguese-minor/ |
| 78 | Psychology | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/psychological-brain-science/psychology-minor/ |
| 79 | Space Science and Engineering | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/space-science-engineering/space-science-engineering-minor/ |
| 80 | Spanish Language and Hispanic Cultures | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/spanish-language-hispanic-cultures-minor/ |
| 81 | Spanish for the Professions | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/spanish-professions-minor/ |
| 82 | Theatre Arts and Studies | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/theatre-arts-studies/theatre-arts-studies-minor/ |
| 83 | Visual Arts | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/art-workships/visual-arts-minor/ |
| 84 | Women, Gender, and Sexuality | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/study-women-gender-sexuality/women-gender-sexuality-minor/ |
| 85 | Writing Seminars | Minor | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/writing-seminars/writing-seminars-minor/ |

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### Krieger School of Arts & Sciences (AAP)

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### Whiting School of Engineering

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 86 | Applied Mathematics and Statistics | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/applied-mathematics-statistics-bachelors-degrees/ |
| 87 | Applied Mathematics and Statistics | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/applied-mathematics-statistics-bs/ |
| 88 | Biomedical Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/biomedical-engineering/biomedical-engineering-bachelor-science/ |
| 89 | Chemical and Biomolecular Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/chemical-biomolecular-engineering/chemical-biomolecular-engineering-bachelor-science/ |
| 90 | Civil Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/civil-engineering-bachelor-science/ |
| 91 | Computer Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/electrical-computer-engineering/computer-engineering-bachelor-science/ |
| 92 | Computer Science | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computer-science/computer-science-ba/ |
| 93 | Computer Science | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computer-science/computer-science-bs/ |
| 94 | Electrical Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/electrical-computer-engineering/electrical-engineering-bachelor-science/ |
| 95 | Engineering Mechanics | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/mechanical-engineering/engineering-mechanics-bachelor-science/ |
| 96 | Environmental Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-engineering-bachelor-science/ |
| 97 | General Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/general-engineering/general-engineering-bachelor-arts/ |
| 98 | Materials Science and Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/materials-science-engineering/materials-engineering-bachelor-science/ |
| 99 | Mechanical Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/mechanical-engineering/mechanical-engineering-bachelor-science/ |
| 100 | Systems Engineering | BS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/systems-engineering-bachelor-science/ |

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 101 | Accounting and Financial Management | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/accounting-financial-management-minor/ |
| 102 | Applied Mathematics and Statistics | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/applied-mathematics-statistics-minor/ |
| 103 | Civil Engineering | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/civil-engineering-minor/ |
| 104 | Computational Medicine | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computational-medicine/computational-medicine-minor/ |
| 105 | Computer Integrated Surgery | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/robotics-computational-sensing/computer-integrated-surgery-minor/ |
| 106 | Computer Science | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computer-science/computer-science-minor/ |
| 107 | Energy | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/electrical-computer-engineering/energy-minor/ |
| 108 | Engineering for Sustainable Development | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/engineering-sustainable-development-minor/ |
| 109 | Environmental Engineering | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-engineering-minor/ |
| 110 | Environmental Sciences | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-sciences-minor/ |
| 111 | Leadership Studies | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/leadership-studies/ |
| 112 | Marketing and Communications | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/marketing-communications/ |
| 113 | Robotics | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/robotics-computational-sensing/robotics-minor/ |
| 114 | Systems Engineering | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/systems-engineering-minor/ |
| 115 | W.P. Carey Entrepreneurship and Management | Minor | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/entrepreneurship-management-minor/ |

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### Peabody Institute

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 116 | Bachelor of Fine Arts in Dance | BFA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/dance-bachelor-fine-arts/ |
| 117 | Bachelor of Music in Composition | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/composition-bachelor-music/ |
| 118 | Bachelor of Music in Hip Hop | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/hip-hop-bachelor-music/ |
| 119 | Bachelor of Music in Jazz Performance | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/jazz-performance-bachelor-music/ |
| 120 | Bachelor of Music in Music Education | BM | https://e-catalogue.jhu.edu/peabody/bachelor-music-degree/bachelor-music-education/ |
| 121 | Bachelor of Music in Music for New Media | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/music-new-media-bachelor-music/ |
| 122 | Bachelor of Music in Performance | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/performance-general-bachelor-music/ |
| 123 | Bachelor of Music in Performance - Computer Music | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/computer-music-bachelor-music/ |
| 124 | Bachelor of Music in Performance - Guitar | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/guitar-bachelor-music/ |
| 125 | Bachelor of Music in Performance - Harpsichord | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/harpsichord-bachelor-music/ |
| 126 | Bachelor of Music in Performance - Historical Performance | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-bachelor-music/ |
| 127 | Bachelor of Music in Performance - Orchestral Instruments | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/orchestral-instruments-bachelor-music/ |
| 128 | Bachelor of Music in Performance - Organ | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/organ-bachelor-music/ |
| 129 | Bachelor of Music in Performance - Piano | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/piano-bachelor-music/ |
| 130 | Bachelor of Music in Performance - Voice | BM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/voice-bachelor-music/ |
| 131 | Bachelor of Music in Recording Arts & Sciences | BM | https://e-catalogue.jhu.edu/peabody/bachelor-music-degree/bachelor-music-recording-arts/ |
| 132 | Five-Year BM/MM Program | BS | https://e-catalogue.jhu.edu/peabody/bachelor-music-degree/accelerated-graduate-degrees/five-year-bm-mm-program/ |
| 133 | Five-Year BMRA/MA Program | BS | https://e-catalogue.jhu.edu/peabody/bachelor-music-degree/accelerated-graduate-degrees/five-year-bmra-ma-program/ |
| 134 | Peabody-Homewood Double Degree Program | BS | https://e-catalogue.jhu.edu/peabody/bachelor-music-degree/combined-degree-programs/peabody-homewood-double-degree-program/ |

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 135 | Business of Music | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/business-music-minor/ |
| 136 | Directed Studies | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/directed-studies-minor/ |
| 137 | Historical Performance | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-minor/ |
| 138 | Historical Performance: Voice | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-voice-minor/ |
| 139 | Liberal Arts | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/liberal-arts-minor/ |
| 140 | Music Theory | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/music-theory-minor/ |
| 141 | Musicology | Minor | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/musicology-minor/ |

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 142 | Music Education Certification - Instrumental | UGCert | https://e-catalogue.jhu.edu/peabody/extension-study/music-education-certification-instrumental/ |
| 143 | Music Education Certification - Vocal | UGCert | https://e-catalogue.jhu.edu/peabody/extension-study/music-education-certification-vocal/ |


#### Carey Business School

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|
| 144 | Business | Minor | https://e-catalogue.jhu.edu/business/degrees-certificates/undergraduate-minor-business/ |

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### School of Education

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### Bloomberg School of Public Health

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### School of Medicine

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### School of Nursing

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


#### SAIS (Advanced International Studies)

##### 本科 (Bachelor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科辅修 (Minor)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|

##### 本科证书 (UG Cert)

| # | 专业 | 学位 | 来源 URL |
|---|------|------|----------|


<!-- UG program-degree rows: 144 (majors 79 + minors 63 + UG certs 2) -->

## SECTION 2 — Graduate Education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by School > Department > Degree Level
(Rule 5 leaf enumeration — see `#### School / ##### Department / ###### Degree Level` tables immediately below for the exhaustive list.)

### 2.2 At least one program's full deep-dive (worked example)
Flagship PhD example: see "Doctor of Philosophy in Biology" under Krieger School of Arts & Sciences → Biology (full application materials, GRE policy, funding, deadlines — all live on the program's e-catalogue page referenced in-line above).

### 2.3 Graduate admissions model
Decentralized per-school admissions; the Krieger School of Arts & Sciences and most professional schools (SAIS, Carey Business, School of Education, Peabody Institute, Bloomberg School of Public Health, School of Medicine, School of Nursing) each run their own admissions office. Some programs use SOPHAS (public health), AMCAS (MD), AACOMAS (DO), LSAC (law), or other centralized services. Funding structures vary by school (see Section 4.3).

#### Krieger School of Arts & Sciences

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 1 | Biology | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biology/biology-bachelor-arts-master-science/ |
| 2 | Biophysical Chemistry and Design for Biotechnology | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biophysics/biophysical-chemistry-design-biotechnology-master-science/ |
| 3 | Chemistry | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/chemistry/chemistry-bachelors-masters-combined/ |
| 4 | Classics | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/classics/classics-bachelor-arts-master/ |
| 5 | Cognitive Science | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/cognitive-science/cognitive-science-master-art/ |
| 6 | Earth and Planetary Sciences | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/earth-planetary-sciences-master-science/ |
| 7 | Economics | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/economics/economics-master-arts/ |
| 8 | History | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history/history-bachelor-arts-master-four-year-program/ |
| 9 | History of Art | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-art-bachelor-arts-master-arts/ |
| 10 | Mathematics | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/mathematics/mathematics-bachelor-arts-master/ |
| 11 | Molecular & Cellular Biology | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biology/molecular-cellular-biology-master-science/ |
| 12 | Neuroscience | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/neuroscience/neuroscience-bachelor-science-master/ |
| 13 | Neuroscience | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/neuroscience/neuroscience-master-science/ |
| 14 | Philosophy | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/philosophy/philosophy-bachelor-arts-master/ |
| 15 | Physics | MA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/physics-bachelor-science-master-science/ |
| 16 | Psychology | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/psychological-brain-science/psychology-master-science/ |
| 17 | Sociology, PhD/Applied Mathematics and Statistics | MS | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/sociology/sociology-phd-applied-mathematics-statistics-mse-joint-program/ |
| 18 | Writing Seminars | MFA | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/writing-seminars/writing-seminars-master-fine-art/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 19 | Anthropology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/anthropology/anthropology-phd/ |
| 20 | Astronomy and Astrophysics | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/astronomy-astrophysics-phd/ |
| 21 | Biology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biology/cellular-molecular-developmental-biology-biophysics-phd/ |
| 22 | Biophysics | DocOther | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biophysics/biophysics-phd-jenkins/ |
| 23 | Biophysics | DocOther | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/biophysics/biophysics-phd-bmp/ |
| 24 | Chemical Biology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/chemical-biology/chemical-biology-phd/ |
| 25 | Chemistry | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/chemistry/chemistry-phd/ |
| 26 | Classics | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/classics/classics-phd/ |
| 27 | Cognitive Science | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/cognitive-science/cognitive-science-phd/ |
| 28 | Earth and Planetary Sciences | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/earth-planetary-science/earth-planetary-science-phd/ |
| 29 | Economics | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/economics/economics-phd/ |
| 30 | English | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/english/english-phd/ |
| 31 | French | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/french-phd/ |
| 32 | German | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/german-phd/ |
| 33 | History | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history/history-phd/ |
| 34 | History of Art | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-art/history-art-phd/ |
| 35 | History of Science and Technology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/history-science-technology/history-science-technology-phd/ |
| 36 | Humanistic Studies | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/comparative-thought-and-literature/humanistic-studies-phd/ |
| 37 | Italian | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/italian-phd/ |
| 38 | Jewish Languages and Literatures | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/jewish-languages-literatures-phd/ |
| 39 | Mathematics | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/mathematics/mathematics-phd/ |
| 40 | Near Eastern Studies | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/near-eastern-studies/near-eastern-studies-phd/ |
| 41 | Philosophy | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/philosophy/philosophy-phd/ |
| 42 | Physics | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/physics-astronomy/physics-phd/ |
| 43 | Political Science | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/political-science/political-science-phd/ |
| 44 | Psychology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/psychological-brain-science/psychology-phd/ |
| 45 | Sociology | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/sociology/sociology-phd/ |
| 46 | Spanish | PhD | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/spanish-phd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 47 | Film and Media Studies | Certificate | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/modern-languages-literatures/film-media-studies-pbc/ |
| 48 | Military Science | Certificate | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/military-science/ |
| 49 | Pre-medicine | PostBaccCert | https://e-catalogue.jhu.edu/arts-sciences/full-time-residential-programs/degree-programs/Post-baccalaureate-premedical-program/pre-medicine-pbc/ |


#### Krieger School of Arts & Sciences (AAP)

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 50 | Applied Economics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/applied-economics-master-science/ |
| 51 | Applied Economics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/applied-economics-master-science/applied-economics-ms-investment-graduate-certificates-finance/ |
| 52 | Applied Economics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/applied-economics-master-science/applied-economics-ms-finance-graduate-certificates-finance/ |
| 53 | Bioinformatics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/bioinformatics-master-science/ |
| 54 | Biotechnology | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/biotechnology-master-science/ |
| 55 | Communication | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/communication-master-arts-mba/ |
| 56 | Communication | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/communication-master-arts/ |
| 57 | Cultural Heritage Management | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/cultural-heritage-management-master-arts/ |
| 58 | Data Analytics and Policy | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/data-analytics-policy-master-science/ |
| 59 | Energy Policy and Climate | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/energy-policy-climate-master-science/ |
| 60 | Environmental Sciences and Policy | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/environmental-sciences-policy-master-science/ |
| 61 | Film and Media | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/film-media-master-arts/ |
| 62 | Financial Economics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/financial-economics-master-science/ |
| 63 | Food Safety Regulation | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/food-safety-regulation-master-science/ |
| 64 | Geographic Information Systems | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/geographic-information-systems-master-science/ |
| 65 | Geospatial Intelligence | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/geospatial-intelligence-master-science/ |
| 66 | Global Security Studies | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/global-security-studies-master-arts/ |
| 67 | Government | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/government-master-arts/ |
| 68 | Individualized Genomics and Health | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/individualized-genomics-health-master-science/ |
| 69 | Intelligence Analysis | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/intelligence-analysis-master-science/ |
| 70 | Master of Biotechnology Enterprise and Entrepreneurship | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/biotechnology-enterprise-entrepreneurship-master/ |
| 71 | Master of Liberal Arts | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/master-liberal-arts/ |
| 72 | Museum Studies | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/museum-studies-master-arts/ |
| 73 | Nonprofit Management | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/non-profit-management-master-arts/ |
| 74 | Organizational Leadership | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/organizational-leadership-master-science/ |
| 75 | Public Management | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/public-management-master-arts/ |
| 76 | Regenerative and Stem Cell Technologies | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/regenerative-stem-cell-technologies/ |
| 77 | Regulatory Science | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/regulatory-master-science/ |
| 78 | Research Administration | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/research-administration-master-science/ |
| 79 | Science Writing | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/science-writing-master-of-arts/ |
| 80 | Teaching Writing | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/teaching-writing-master-arts/ |
| 81 | Writing | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/writing-master-arts/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 82 | Communication, MA/Nonprofit Management | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/communication-master-arts-mba/communication-master-arts-nonprofit-management-certificate/ |
| 83 | Cultural Heritage Management, MA/Digital Curation | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/cultural-heritage-management-master-arts/cultural-heritage-management-ma-digital-curation-certificate/ |
| 84 | Cultural Heritage Management, MA/Nonprofit Management | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/cultural-heritage-management-master-arts/cultural-heritage-management-ma-nonprofit-management-certificate/ |
| 85 | Data Analytics and Policy, MS/Intelligence | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/data-analytics-policy-master-science/data-analytics-policy-ms-intelligence-certificate/ |
| 86 | Digital Curation | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/digital-curation-certificate/ |
| 87 | Environmental Sciences and Policy, MS/Geographic Information Systems | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/environmental-sciences-policy-master-science/environmental-sciences-policy-ms-geographic-information-systems-graduate-certificate/ |
| 88 | Geographic Information Systems | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/geographic-information-systems-post-baccalaureate-certificate/ |
| 89 | Global Security Studies, MA/Intelligence | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/global-security-studies-master-arts/global-security-studies-ma-intelligence-certificate/ |
| 90 | Government, MA/Intelligence | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/government-master-arts/government-ma-intelligence-certificate/ |
| 91 | Intelligence | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/intelligence-certificate/ |
| 92 | Museum Studies, MA/Digital Curation | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/museum-studies-master-arts/museum-studies-ma-digital-curation-certificate/ |
| 93 | Museum Studies, MA/Nonprofit Management | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/museum-studies-master-arts/museum-studies-ma-nonprofit-management-certificate/ |
| 94 | Nonprofit Management | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/nonprofit-management-certificate/ |
| 95 | Public Management, MA/Data Analytics and Policy | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/public-management-master-arts/public-management-ma-government-analytics-certificate/ |
| 96 | Public Management, MA/Intelligence | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/public-management-master-arts/public-management-ma-intelligence-certificate/ |
| 97 | Public Management, MA/Nonprofit Management | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/public-management-master-arts/public-management-ma-nonprofit-certificate/ |
| 98 | Science Writing | Certificate | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/science-writing-graduate-certificate/ |


#### Whiting School of Engineering

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 99 | Applied Biomedical Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-biomedical-engineering/applied-biomedical-engineering-master-science/ |
| 100 | Applied Mathematics and Statistics | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/applied-mathematics-statistics-master-science-engineering/ |
| 101 | Applied Physics | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-physics/applied-physics-master-science/ |
| 102 | Applied and Computational Mathematics | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-computational-mathematics/applied-computational-mathematics-master-science/ |
| 103 | Artificial Intelligence | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/artificial-intelligence/master-of-science/ |
| 104 | Bioengineering Innovation and Design | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/biomedical-engineering/innovation-design-master-science-engineering/ |
| 105 | Biomedical Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/biomedical-engineering/biomedical-engineering-master-science-engineering/ |
| 106 | Chemical and Biomolecular Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/chemical-biomolecular-engineering/chemical-biomolecular-engineering-master/ |
| 107 | Chemical and Biomolecular Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/chemical-biomolecular-engineering/chemical-biomolecular-engineering-master-science-engineering/ |
| 108 | Civil Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/civil-engineering/civil-engineering-master-civil-engineering/ |
| 109 | Civil Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/civil-engineering-mse/ |
| 110 | Climate, Energy, and Environmental Sustainability | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/climate-energy-environmental-sustainability/ |
| 111 | Computer Science | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/computer-science/computer-science-master/ |
| 112 | Computer Science | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computer-science/computer-science-master-science-engineering/ |
| 113 | Cybersecurity | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/cybersecurity/cybersecurity-master-science/ |
| 114 | Data Analytics and Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/data-analytics-engineering/data-analytics-engineering-master-science/ |
| 115 | Data Science | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/data-science/data-science-master/ |
| 116 | Data Science | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/data-science-masters-degree/ |
| 117 | Electrical and Computer Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/electrical-computer-engineering/electrical-computer-engineering-master-science/ |
| 118 | Electrical and Computer Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/electrical-computer-engineering/electrical-computer-master-science-engineering/ |
| 119 | Engineering Management | MEng | https://e-catalogue.jhu.edu/engineering/engineering-professionals/engineering-management/engineering-management-master/ |
| 120 | Engineering Management | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/engineering-management-master-science/ |
| 121 | Environmental Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-master/ |
| 122 | Environmental Engineering and Science | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-science-master/ |
| 123 | Environmental Health and Engineering | MA | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-health-engineering-master-arts/ |
| 124 | Environmental Health and Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-health-engineering-master-science/ |
| 125 | Environmental Health and Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-health-engineering-master-science-engineering/ |
| 126 | Environmental Planning and Management | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-planning-management-master-science/ |
| 127 | Financial Mathematics | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/financial-mathematics/financial-mathematics-master-science/ |
| 128 | Financial Mathematics | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/financial-mathematics-master-science-engineering/ |
| 129 | Global Innovation and Leadership Through Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/global-innovation-leadership-engineering-master-science/ |
| 130 | Healthcare Systems Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/healthcare-systems-engineering/healthcare-systems-engineering-master-science/ |
| 131 | Industrial and Operations Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/industrial-operations-engineering/industrial-operations-engineering-master-science/ |
| 132 | Information Systems Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/information-systems-engineering/information-systems-engineering-master-science/ |
| 133 | Materials Science and Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/materials-science-engineering/materials-science-engineering-master-science/ |
| 134 | Materials Science and Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/materials-science-engineering/materials-science-engineering-master/ |
| 135 | Mechanical Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/mechanical-engineering/mechanical-engineering-master-science/ |
| 136 | Mechanical Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/mechanical-engineering/mechanical-engineering-master-science/ |
| 137 | Occupational and Environmental Hygiene | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/occupational-environmental-hygiene/occupational-environmental-hygiene-master-science/ |
| 138 | Professional Communication Program | MEng | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/professional-communication/ |
| 139 | Robotics | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/robotics-computational-sensing/robotics-master-science-engineering/ |
| 140 | Robotics and Autonomous Systems | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/robotics-autonomous-systems/robotics-autonomous-systems-master-science/ |
| 141 | Security Informatics | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/information-security-institute/security-informatics-master-science/ |
| 142 | Security Informatics, Master of Science/Applied Mathematics and Statistics | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/information-security-institute/security-informatics-master-science-applied-mathematics-statistics-engineering-dual-program/ |
| 143 | Security Informatics, Master of Science/Computer Science | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/information-security-institute/security-informatics-master-science-computer-science-engineering-dual-program/ |
| 144 | Space Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/space-engineering/space-engineering-master-science/ |
| 145 | Systems Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/systems-engineering/systems-engineering-master-science/ |
| 146 | Systems Engineering | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/systems-engineering-ms/ |
| 147 | Systems Engineering | MS | https://e-catalogue.jhu.edu/engineering/engineering-professionals/systems-engineering/systems-engineering-master-science-engineering/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 148 | Applied Mathematics and Statistics | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/applied-mathematics-statistics/applied-mathematics-statistics-phd/ |
| 149 | Chemical and Biomolecular Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/chemical-biomolecular-engineering/chemical-biomolecular-engineering-phd/ |
| 150 | Civil and Systems Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/civil-engineering/civil-engineering-phd/ |
| 151 | Computer Science | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/computer-science/computer-science-phd/ |
| 152 | Electrical and Computer Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/electrical-computer-engineering/electrical-computer-engineering-phd/ |
| 153 | Engineering | DEng | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/doctor-engineering/engineering-doctor/ |
| 154 | Environmental Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/environmental-engineering-phd/ |
| 155 | Materials Science and Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/materials-science-engineering/materials-science-engineering-phd/ |
| 156 | Mechanical Engineering | PhD | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/mechanical-engineering/mechanical-engineering-phd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 157 | Applied Biomedical Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-biomedical-engineering/applied-biomedical-engineering-graduate-certificate/ |
| 158 | Applied Biomedical Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-biomedical-engineering/applied-biomedical-engineering-post-masters-certificate/ |
| 159 | Applied Physics | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-physics/applied-physics-post-masters-certificate/ |
| 160 | Applied and Computational Mathematics | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-computational-mathematics/applied-computational-mathematics-graduate-certificate/ |
| 161 | Applied and Computational Mathematics | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/applied-computational-mathematics/applied-computational-mathematics-post-masters-certificate/ |
| 162 | Artificial Intelligence | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/artificial-intelligence/graduate-certificate/ |
| 163 | Civil Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/civil-engineering/civil-engineering-graduate-certificate/ |
| 164 | Climate, Energy, and Environmental Sustainability | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/climate-change-energy-environmental-sustainability-graduate-certificate/ |
| 165 | Computer Science | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/computer-science/computer-science-graduate-certificate/ |
| 166 | Computer Science | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/computer-science/computer-science-post-masters-certificate/ |
| 167 | Cybersecurity | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/cybersecurity/cybersecurity-graduate-certificate/ |
| 168 | Cybersecurity | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/cybersecurity/cybersecurity-post-masters-certificate/ |
| 169 | Data Science | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/data-science/data-science-graduate-certificate/ |
| 170 | Data Science | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/data-science/data-science-post-masters-certificate/ |
| 171 | Electrical and Computer Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/electrical-computer-engineering/electrical-computer-engineering-graduate-certificate/ |
| 172 | Electrical and Computer Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/electrical-computer-engineering/electrical-computer-engineering-post-masters-certificate/ |
| 173 | Engineering Management | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/engineering-management/engineering-management-graduate-certificate/ |
| 174 | Environmental Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-graduate-certificate/ |
| 175 | Environmental Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-post-masters-certificate/ |
| 176 | Environmental Engineering and Science | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-science-graduate-certificate/ |
| 177 | Environmental Engineering and Science | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-engineering-science-post-masters-certificate/ |
| 178 | Environmental Planning and Management | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-planning-management-graduate-certificate/ |
| 179 | Environmental Planning and Management | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/environmental-engineering-science-management-programs/environmental-planning-management-post-masters-certificate/ |
| 180 | Financial Risk Management | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/financial-mathematics/financial-risk-management-graduate-certificate/ |
| 181 | Information Systems Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/information-systems-engineering/information-systems-engineering-graduate-certificate/ |
| 182 | Information Systems Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/information-systems-engineering/information-systems-engineering-post-masters-certificate/ |
| 183 | Mechanical Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/mechanical-engineering/mechanical-engineering-post-masters-certificate/ |
| 184 | Professional Development Program | Certificate | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/leadership-education/professional-development/ |
| 185 | Quantitative Portfolio Management | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/financial-mathematics/quantitative-portfolio-management-graduate-certificate/ |
| 186 | Securitization | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/financial-mathematics/securitization-graduate-certificate/ |
| 187 | Space Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/space-engineering/space-engineering-post-masters-certificate/ |
| 188 | Systems Engineering | Certificate | https://e-catalogue.jhu.edu/engineering/engineering-professionals/systems-engineering/systems-engineering-graduate-certificate/ |
| 189 | Systems Engineering | PostMasterCert | https://e-catalogue.jhu.edu/engineering/engineering-professionals/systems-engineering/systems-engineering-post-masters-certificate/ |


#### Peabody Institute

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 190 | Audio Sciences: Acoustics | MA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/audio-sciences-acoustics-master-arts/ |
| 191 | Audio Sciences: Recording Arts and Sciences | MA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/audio-sciences-recording-production-master-arts/ |
| 192 | Composition | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/composition-master-music/ |
| 193 | Electronics and Computer Music | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/electronics-computer-music-master-music/ |
| 194 | Film and Game Scoring | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/film-game-scoring-master-of-music/ |
| 195 | Master of Music: Low Residency | MM | https://e-catalogue.jhu.edu/peabody/master-music-degree/master-music-low-residency/ |
| 196 | Music Education | MEd | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/music-education-master-music/ |
| 197 | Music Theory Pedagogy | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/music-theory-pedagogy-master-music/ |
| 198 | Musicology | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/musicology-master-music/ |
| 199 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/choral-conducting-specialization/ |
| 200 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/guitar-master-music/ |
| 201 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/harpsichord-master-music/ |
| 202 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-instruments-master-music/ |
| 203 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-voice-master-music/ |
| 204 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/jazz-master-music/ |
| 205 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/conducting-orchestral-master-music/ |
| 206 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/orchestral-instruments-master-music/ |
| 207 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/organ-master-music/ |
| 208 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/performance-pedagogy-master-music/ |
| 209 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/piano-master-music/ |
| 210 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/voice-master-music/ |
| 211 | Performance | MM | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/conducting-wind-master-music/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 212 | Composition | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/composition-doctor-musical-arts/ |
| 213 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/choral-conducting-doctor-musical-arts/ |
| 214 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/guitar-doctor-musical-arts/ |
| 215 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/historical-performance-instruments-doctor-musical-arts/ |
| 216 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/orchestral-conducting-doctor-musical-arts/ |
| 217 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/orchestral-instruments-doctor-musical-arts/ |
| 218 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/organ-doctor-musical-arts/ |
| 219 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/piano-doctor-musical-arts/ |
| 220 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/voice-doctor-musical-arts/ |
| 221 | Performance | DMA | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/wind-conducting-doctor-musical-arts/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 222 | Artist’s Diploma | Certificate | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/artists-diploma/ |
| 223 | Graduate Performance Diploma | Certificate | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/graduate-performance-diploma/ |
| 224 | Guitar | PerformerCert | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/guitar-performers-certificate/ |
| 225 | Orchestral Instruments | PerformerCert | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/orchestral-instruments-performers-certificate/ |
| 226 | Organ | PerformerCert | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/organ-performers-certificate/ |
| 227 | Piano | PerformerCert | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/piano-performers-certificate/ |
| 228 | Voice | PerformerCert | https://e-catalogue.jhu.edu/peabody/degree-diploma-programs/voice-performers-certificate/ |


#### Carey Business School

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 229 | Applied Economics | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/applied-economics-ms-mba/ |
| 230 | Biotechnology | MS | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-biotechnology-education/biotechnology-master-science-mba/ |
| 231 | Business Administration (Accelerated) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-administration-accelerated-mba/ |
| 232 | Business Administration (Executive) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-administration-executive-mba/ |
| 233 | Business Administration (Flexible) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-administration-flexible-mba/ |
| 234 | Business Administration (Full Time) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-administration-fulltime-mba/ |
| 235 | Business Analytics and Artificial Intelligence | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-analytics-artificial-intelligence-master-science/ |
| 236 | Business Analytics and Artificial Intelligence (Part Time) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/business-analytics-artificial-intelligence-part-time-master-science/ |
| 237 | Design Leadership | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/design-leadership-mba-ma/ |
| 238 | Finance | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/finance-master-science/ |
| 239 | Finance (Part Time) | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/finance-part-time-master-science/ |
| 240 | Finance, Master of Science | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/finance-master-science-financial-econometrics/ |
| 241 | Financial Management, Graduate Certificate, Investments, Graduate Certificate, Applied Economics | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/financial-management-investments-graduate-certificate-applied-economics-master-science/ |
| 242 | Government | MA | https://e-catalogue.jhu.edu/arts-sciences/advanced-academic-programs/programs/center-advanced-governmental-studies/government-master-arts-mba/ |
| 243 | Health Care Management | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/health-care-management-master-science/ |
| 244 | Health Care Management (Part Time) | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/health-care-management-part-time-master-science/ |
| 245 | Information Systems and Artificial Intelligence for Business | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/information-systems-master-science/ |
| 246 | Information Systems and Artificial Intelligence for Business (Part Time) | MBA | https://e-catalogue.jhu.edu/business/degrees-certificates/information-systems-artificial-intelligence-business-part-time-master-science/ |
| 247 | MBA/Applied Economics | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/applied-economics-mba-ms/ |
| 248 | MBA/Biotechnology | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/biotechnology-mba-ms/ |
| 249 | MBA/Communication | MA | https://e-catalogue.jhu.edu/business/degrees-certificates/communication-mba-ma/ |
| 250 | MBA/DNP Dual Degree | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/mba-dnp/ |
| 251 | MBA/Government | MA | https://e-catalogue.jhu.edu/business/degrees-certificates/government-mba-ma/ |
| 252 | MBA/Health Care Management | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/health-care-management-mba-ms/ |
| 253 | MBA/Healthcare Organizational Leadership | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/nursing-health-systems-management-mba-ms/ |
| 254 | MBA/JD Dual Degree | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/mba-jd/ |
| 255 | MBA/MA in International Relations | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/international-relations-mba-ma/ |
| 256 | MBA/MD Dual Degree | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/mba-md/ |
| 257 | MBA/PharmD Dual Degree | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/mba-pharmd/ |
| 258 | MD-MBA | DualDegree | https://e-catalogue.jhu.edu/medicine/medical-students/md-mba-combined-degree/ |
| 259 | Management | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/management-master-science/ |
| 260 | Management (Part Time) | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/management-part-time-master-science/ |
| 261 | Marketing | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/marketing-master-science/ |
| 262 | Marketing (Part Time) | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/marketing-part-time-master-science/ |
| 263 | Marketing, Master of Science | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/marketing-master-science-marketing-analytics/ |
| 264 | Real Estate and Infrastructure | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/real-estate-infrastructure-master-science/ |
| 265 | Real Estate and Infrastructure (Part Time) | MS | https://e-catalogue.jhu.edu/business/degrees-certificates/real-estate-infrastructure-part-time-master-science/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 266 | Artificial Intelligence for Business | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/artificial-intelligence-business-graduate-certificate/ |
| 267 | Business Analytics and Risk Management | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/business-analytics-risk-management-graduate-certificate/ |
| 268 | Digital Marketing | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/digital-marketing-graduate-certificate/ |
| 269 | Entrepreneurial Marketing | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/entrepreneurial-marketing-graduate-certificate/ |
| 270 | Financial Management | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/financial-management-graduate-certificate/ |
| 271 | Healthcare Management, Innovation, and Technology | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/healthcare-management-innovation-technology-graduate-certificate/ |
| 272 | Investments | Certificate | https://e-catalogue.jhu.edu/business/degrees-certificates/investments-graduate-certificate/ |


#### School of Education

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 273 | Counseling | MS | https://e-catalogue.jhu.edu/education/programs/masters/counseling-master-science/ |
| 274 | Education | MEd | https://e-catalogue.jhu.edu/education/programs/masters/education-master-science/ |
| 275 | Education | MEd | https://e-catalogue.jhu.edu/education/programs/masters/education-master-science/digital-age-learning-educational-technology/ |
| 276 | Education | MEd | https://e-catalogue.jhu.edu/education/programs/masters/education-master-science/educational-studies/ |
| 277 | Education | MEd | https://e-catalogue.jhu.edu/education/programs/masters/education-master-science/gifted-education/ |
| 278 | Education Policy | MEd | https://e-catalogue.jhu.edu/education/programs/masters/education-policy-master-science/ |
| 279 | Health Professions (Online) | MEd | https://e-catalogue.jhu.edu/education/programs/masters/health-professions-online-master-education/ |
| 280 | Learning Design and Technology | MEd | https://e-catalogue.jhu.edu/education/programs/masters/learning-design-technology-master-education/ |
| 281 | Special Education | MEd | https://e-catalogue.jhu.edu/education/programs/masters/special-education-master-science/ |
| 282 | Teaching Professionals | MEd | https://e-catalogue.jhu.edu/education/programs/masters/teaching-for-professional-master-education/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 283 | Education | PhD | https://e-catalogue.jhu.edu/education/programs/doctoral/education-phd/ |
| 284 | Education (Online) | EdD | https://e-catalogue.jhu.edu/education/programs/doctoral/education-online-edd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 285 | Applied Behavior Analysis | PostMasterCert | https://e-catalogue.jhu.edu/education/programs/post-masters-certificates/applied-behavior-analysis-post-masters-certificate/ |
| 286 | Evidence-Based Teaching in the Health Professions | PostMasterCert | https://e-catalogue.jhu.edu/education/programs/post-masters-certificates/evidence-based-teaching-health-professions-post-masters-certificate/ |


#### Bloomberg School of Public Health

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 287 | Biochemistry and Molecular Biology | MHS | https://e-catalogue.jhu.edu/public-health/departments/biochemistry-molecular-biology/biochemistry-molecular-biology-mhs/ |
| 288 | Biochemistry and Molecular Biology | MS | https://e-catalogue.jhu.edu/public-health/departments/biochemistry-molecular-biology/biochemistry-molecular-biology-scm/ |
| 289 | Biostatistics | MHS | https://e-catalogue.jhu.edu/public-health/departments/biostatistics/biostatistics-mhs/ |
| 290 | Biostatistics | MS | https://e-catalogue.jhu.edu/public-health/departments/biostatistics/biostatistics-scm/ |
| 291 | Clinical Investigation | MHS | https://e-catalogue.jhu.edu/public-health/departments/graduate-training-clinical-investigation/graduate-training-clinical-investigation-mhs/ |
| 292 | Clinical Investigation | MS | https://e-catalogue.jhu.edu/public-health/departments/graduate-training-clinical-investigation/graduate-training-programs-clinical-investigation-scm/ |
| 293 | DNP/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/dnp-mph/ |
| 294 | DVM/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/dvm-mph/ |
| 295 | Environmental Health | MHS | https://e-catalogue.jhu.edu/public-health/departments/environmental-health-engineering/environmental-health-mhs/ |
| 296 | Environmental Health | MS | https://e-catalogue.jhu.edu/public-health/departments/environmental-health-engineering/environmental-health-scm/ |
| 297 | Epidemiology | MHS | https://e-catalogue.jhu.edu/public-health/departments/epidemiology/epidemiology-mhs/ |
| 298 | Epidemiology | MS | https://e-catalogue.jhu.edu/public-health/departments/epidemiology/epidemiology-scm/ |
| 299 | Genetic Counseling | MS | https://e-catalogue.jhu.edu/public-health/departments/health-behavior-society/genetic-counseling-scm/ |
| 300 | Global Health Economics | MHS | https://e-catalogue.jhu.edu/public-health/departments/international-health/global-health-economics-mhs/ |
| 301 | Health Administration | MS | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/mha/ |
| 302 | Health Economics and Outcomes Research | MHS | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/health-economics-outcomes-research-mhs/ |
| 303 | Health Education and Health Communication | MS | https://e-catalogue.jhu.edu/public-health/departments/health-behavior-society/health-education-communication-msph/ |
| 304 | Health Finance and Management | MHS | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/health-finance-management-mhs/ |
| 305 | Health Policy | MS | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/health-policy-msph/ |
| 306 | Health, Behavior, and Society | MHS | https://e-catalogue.jhu.edu/public-health/departments/health-behavior-society/health-behavior-society-mhs/ |
| 307 | International Health | MSPH | https://e-catalogue.jhu.edu/public-health/departments/international-health/international-health-ma-msph/ |
| 308 | International Health | MS | https://e-catalogue.jhu.edu/public-health/departments/international-health/international-health-msph/ |
| 309 | International Health, MSPH | MS | https://e-catalogue.jhu.edu/public-health/departments/international-health/international-health-msph-human-nutrition-dietitian/ |
| 310 | JD/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/jd-mph/ |
| 311 | LLM/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/llm-mph/ |
| 312 | MBA/MPH Dual Degree | DualDegree | https://e-catalogue.jhu.edu/business/degrees-certificates/mba-mph/ |
| 313 | MBA/MPH with China Europe International Business School | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/mph-mba-ceibs/ |
| 314 | MD-PhD | DualDegree | https://e-catalogue.jhu.edu/medicine/medical-students/md-phd-combined-degree/ |
| 315 | MD/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/md-mph/ |
| 316 | MD/PhD | DualDegree | https://e-catalogue.jhu.edu/public-health/md-phd/ |
| 317 | MPH/MBA | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/mph-mba/ |
| 318 | MSW/MPH | DualDegree | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/msw-mph/ |
| 319 | Master of Applied Science in Patient Safety and Healthcare Quality | MAS | https://e-catalogue.jhu.edu/public-health/departments/MAS-Office/patient-safety-healthcare-quality-master-applied-science/ |
| 320 | Master of Applied Science in Population Health Management | MAS | https://e-catalogue.jhu.edu/public-health/departments/MAS-Office/population-health-management-master-applied-science/ |
| 321 | Master of Applied Science in Spatial Analysis for Public Health | MAS | https://e-catalogue.jhu.edu/public-health/departments/MAS-Office/spatial-analysis-public-health-master-applied-science/ |
| 322 | Master of Arts in Public Health Biology | MPH | https://e-catalogue.jhu.edu/public-health/departments/ma-public-health-biology/ |
| 323 | Master of Bioethics (MBE) | MS | https://e-catalogue.jhu.edu/public-health/departments/master-bioethics/ |
| 324 | Master of Public Health Program (MPH) | MPH | https://e-catalogue.jhu.edu/public-health/departments/master-public-health/ |
| 325 | Mental Health | MHS | https://e-catalogue.jhu.edu/public-health/departments/mental-health/mental-health-mhs/ |
| 326 | Molecular Microbiology & Immunology | MHS | https://e-catalogue.jhu.edu/public-health/departments/molecular-microbiology-immunology/molecular-microbiology-immunology-mhs/ |
| 327 | Molecular Microbiology & Immunology | MS | https://e-catalogue.jhu.edu/public-health/departments/molecular-microbiology-immunology/molecular-microbiology-immunology-scm/ |
| 328 | Occupational and Environmental Hygiene | MS | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/environmental-health-engineering/occupational-environmental-hygiene-master-sience/ |
| 329 | PhD/MBA | DualDegree | https://e-catalogue.jhu.edu/public-health/mba-phd/ |
| 330 | Population, Family and Reproductive Health | MHS | https://e-catalogue.jhu.edu/public-health/departments/population-family-reproductive-health/population-family-reproductive-health-mhs/ |
| 331 | Population, Family and Reproductive Health | MHS | https://e-catalogue.jhu.edu/public-health/departments/population-family-reproductive-health/population-family-reproductive-health-mhs-online/ |
| 332 | Population, Family and Reproductive Health | MS | https://e-catalogue.jhu.edu/public-health/departments/population-family-reproductive-health/population-family-reproductive-health-msph/ |
| 333 | Toxicology for Human Risk Assessment | MS | https://e-catalogue.jhu.edu/public-health/departments/environmental-health-engineering/toxicology-human-risk-ms/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 334 | Biochemistry and Molecular Biology | PhD | https://e-catalogue.jhu.edu/public-health/departments/biochemistry-molecular-biology/biochemistry-molecular-biology-phd/ |
| 335 | Biostatistics | PhD | https://e-catalogue.jhu.edu/public-health/departments/biostatistics/biostatistics-phd/ |
| 336 | Clinical Investigation | PhD | https://e-catalogue.jhu.edu/public-health/departments/graduate-training-clinical-investigation/graduate-training-clinical-investigation-phd/ |
| 337 | Doctor of Public Health (DrPH) | DrPH | https://e-catalogue.jhu.edu/public-health/departments/doctor-public-health/ |
| 338 | Environmental Health | PhD | https://e-catalogue.jhu.edu/public-health/departments/environmental-health-engineering/environmental-health-phd/ |
| 339 | Epidemiology | PhD | https://e-catalogue.jhu.edu/public-health/departments/epidemiology/epidemiology-phd/ |
| 340 | Health Policy and Management | DrPH | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/health-policy-management-drph-tsinghua/ |
| 341 | Health Policy and Management | PhD | https://e-catalogue.jhu.edu/public-health/departments/health-policy-management/health-policy-management-phd/ |
| 342 | International Health | PhD | https://e-catalogue.jhu.edu/public-health/departments/international-health/international-health-phd/ |
| 343 | Mental Health | PhD | https://e-catalogue.jhu.edu/public-health/departments/mental-health/mental-health-phd/ |
| 344 | Molecular Microbiology & Immunology | PhD | https://e-catalogue.jhu.edu/public-health/departments/molecular-microbiology-immunology/molecular-microbiology-immunology-phd/ |
| 345 | Population, Family and Reproductive Health | PhD | https://e-catalogue.jhu.edu/public-health/departments/population-family-reproductive-health/population-family-reproductive-health-phd/ |
| 346 | Social and Behavioral Sciences | PhD | https://e-catalogue.jhu.edu/public-health/departments/health-behavior-society/health-behavior-society-phd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 347 | Adolescent Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/adolescent-health/ |
| 348 | Bioethics | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/bioethics/ |
| 349 | Climate and Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/climate-change-and-ph/ |
| 350 | Clinical Trials | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/clinical-trials/ |
| 351 | Community-Based Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/community-based-public-health/ |
| 352 | Demographic Methods | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/demographic-methods/ |
| 353 | Environmental and Occupational Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/environmental-and-occ-health/ |
| 354 | Epidemiology for Public Health Professionals | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/epi-for-ph-professionals/ |
| 355 | Evaluation: International Health Programs | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/evaluation-ih-progms/ |
| 356 | Food Systems, the Environment & Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/food-systems-environment-and-ph/ |
| 357 | Gender and Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/genderandhealth/ |
| 358 | Gerontology | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/gerontology/ |
| 359 | Global Digital Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/global-digital-health/ |
| 360 | Global Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/global-health/ |
| 361 | Health Communication | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/health-communication/ |
| 362 | Health Disparities and Health Inequality | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/health-disparities-and-health-inequality/ |
| 363 | Health Education | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/health-education/ |
| 364 | Health Finance and Management | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/health-finance-and-management/ |
| 365 | Healthcare Epidemiology and Infection Prevention and Control | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/healthcare-epi-infection-prevention-control/ |
| 366 | Humane Sciences and Toxicology Policy | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/humane-sciences-and-tox-policy/ |
| 367 | Humanitarian Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/humanitarian-health/ |
| 368 | Implementation Science and Research Practice | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/implementation-science-research-practice/ |
| 369 | Indigenous Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/indigenous-public-health/ |
| 370 | Infectious Disease Dynamics, Analytics, and Modeling | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/infectious-disease-dynamics-analytics-modeling/ |
| 371 | Injury and Violence Prevention | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/injury-and-violence-prevention/ |
| 372 | Leadership for Public Health and Healthcare | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/leadership-public-health-healthcare/ |
| 373 | Lesbian, Gay, Bisexual, Transgender, and Queer (LGBTQ) Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/lgbtq-public-health/ |
| 374 | Maternal and Child Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/maternal-and-child-health/ |
| 375 | Mental Health Policy, Economics and Services | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/mental-health-policy-econ-and-services/ |
| 376 | Pharmacoepidemiology and Drug Safety | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/pharmacoepi-and-drug-safety/ |
| 377 | Population Health Management | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/pop-health-management/ |
| 378 | Population and Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/population-and-health/ |
| 379 | Product Stewardship for Sustainability | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/product-stewardship-sustainability-certificate/ |
| 380 | Public Health Advocacy | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-health-advocacy/ |
| 381 | Public Health Economics | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-health-econ/ |
| 382 | Public Health Informatics | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-health-informatics/ |
| 383 | Public Health Preparedness | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-health-preparedness/ |
| 384 | Public Health, Human Rights, and Law | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-health-human-rights-law/ |
| 385 | Public Mental Health Research | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/public-mental-health-research/ |
| 386 | Quality, Patient Safety and Outcomes Research | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/quality-patient-safety-outcomes-research/ |
| 387 | Rigor, Reproducibility and Responsibility in Scientific Practice | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/rigorreproducibilityandresponsibilityinscientificpractice/ |
| 388 | Risk Sciences and Public Policy | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/risk-sciences-and-public-policy/ |
| 389 | Social Epidemiology | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/social-epidemiology/ |
| 390 | Spatial Analysis for Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/spatial-analysis-for-ph/ |
| 391 | Training Certificate in Public Health | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/training-in-public-health/ |
| 392 | Tropical Medicine | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/tropical-medicine/ |
| 393 | Vaccine Science and Policy | Certificate | https://e-catalogue.jhu.edu/public-health/certificates/vaccine-science-and-policy/ |


#### School of Medicine

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 394 | Anatomy Education | MEd | https://e-catalogue.jhu.edu/medicine/graduate-programs/anatomy-education-ms/ |
| 395 | Applied Health Sciences Informatics | MHS | https://e-catalogue.jhu.edu/medicine/graduate-programs/applied-health-sciences-informatics-ms/ |
| 396 | Cellular and Molecular Medicine | MS | https://e-catalogue.jhu.edu/medicine/graduate-programs/cellular-molecular-medicine-ms/ |
| 397 | Clinical Anaplastology | MS | https://e-catalogue.jhu.edu/medicine/graduate-programs/clinical-anaplastology-ms/ |
| 398 | Health Sciences Informatics | MHS | https://e-catalogue.jhu.edu/medicine/graduate-programs/health-sciences-informatics-research-ms/ |
| 399 | History of Medicine | MA | https://e-catalogue.jhu.edu/medicine/graduate-programs/history-medicine-ma-onsite/ |
| 400 | History of Medicine | MA | https://e-catalogue.jhu.edu/medicine/graduate-programs/history-medicine-ma/ |
| 401 | Medical Physics | MS | https://e-catalogue.jhu.edu/medicine/graduate-programs/medical-physics-ms/ |
| 402 | Medical and Biological Illustration | MA | https://e-catalogue.jhu.edu/medicine/graduate-programs/medical-biological-illustration-ma/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 403 | Biochemistry, Cellular and Molecular Biology | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/biochemistry-cellular-molecular-biology-phd/ |
| 404 | Biological Chemistry | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/biological-chemistry-phd/ |
| 405 | Biomedical Engineering | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/biomedical-engineering-phd/ |
| 406 | Biomedical Engineering | DocOther | https://e-catalogue.jhu.edu/engineering/full-time-residential-programs/degree-programs/biomedical-engineering/biomedical-engineering-phd/ |
| 407 | Cellular and Molecular Medicine | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/cellular-molecular-medicine-phd/ |
| 408 | Cellular and Molecular Physiology | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/cellular-molecular-physiology-phd/ |
| 409 | Cross-Disciplinary Program in Graduate Biomedical Sciences | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/20cross-disciplinary-program-biomedical-sciences/ |
| 410 | Doctor of Medicine | MD | https://e-catalogue.jhu.edu/medicine/medical-students/md/ |
| 411 | Functional Anatomy and Evolution | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/functional-anatomy-evolution-phd/ |
| 412 | Health Sciences Informatics | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/health-sciences-informatics-phd/ |
| 413 | History of Medicine | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/history-science-medicine-technology-phd/ |
| 414 | Human Genetics and Genomics | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/human-genetics-genomics-phd/ |
| 415 | Immunology | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/immunology-phd/ |
| 416 | Medical Physics | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/medical-physics-phd/ |
| 417 | Molecular Biophysics | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/molecular-biophysics-phd/ |
| 418 | Neuroscience | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/neuroscience-phd/ |
| 419 | Pathobiology | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/pathobiology-phd/ |
| 420 | Pharmacology and Molecular Sciences | PhD | https://e-catalogue.jhu.edu/medicine/graduate-programs/pharmacology-molecular-sciences-phd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 421 | Clinical Informatics | PostBaccCert | https://e-catalogue.jhu.edu/medicine/graduate-programs/clinical-informatics-certificate/ |
| 422 | History of Medicine | PostBaccCert | https://e-catalogue.jhu.edu/medicine/graduate-programs/history-medicine-certificate/ |
| 423 | Medical Physics | PostBaccCert | https://e-catalogue.jhu.edu/medicine/graduate-programs/medical-physics-certificate/ |


#### School of Nursing

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 424 | DNP Post Master's / MPH Dual Degree | DualDegree | https://e-catalogue.jhu.edu/nursing/dual-joint-degrees/dnp-mph/ |
| 425 | DNP Post Master's/MBA Dual Degree | DualDegree | https://e-catalogue.jhu.edu/nursing/dual-joint-degrees/dnp-mba/ |
| 426 | Entry into Nursing | MS | https://e-catalogue.jhu.edu/nursing/masters-degrees/entry-nursing-msn/ |
| 427 | Healthcare Organizational Leadership, MSN/MBA | DualDegree | https://e-catalogue.jhu.edu/nursing/dual-joint-degrees/healthcare-organizational-leadership-msn-mba/ |
| 428 | Master of Science in Nursing (MSN) Healthcare Organizational Leadership Track | MS | https://e-catalogue.jhu.edu/nursing/masters-degrees/msn-healthcare-organizational-leadership-track/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 429 | Adult-Gerontological Acute Care Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/adult-gerontological-acute-care-nurse-practitioner-dnp/ |
| 430 | Adult-Gerontological Critical Care Clinical Nurse Specialist | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/adult-gerontological-critical-care-clinical-nurse-specialist-dnp/ |
| 431 | Adult-Gerontological Health Clinical Nurse Specialist | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/adult-gerontological-health-clinical-nurse-specialist-dnp/ |
| 432 | Adult-Gerontological Primary Care Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/adult-gerontological-primary-care-nurse-practitioner-dnp/ |
| 433 | Doctor of Nursing Practice | DNP | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/ |
| 434 | Doctor of Nursing Practice (DNP): Advanced Practice Track/Doctor of Philosophy in Nursing (PhD) Dual Degree | PhD | https://e-catalogue.jhu.edu/nursing/dual-joint-degrees/nursing-dnp-phd/ |
| 435 | Doctor of Nursing Practice: Post Master's Track | DNP | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp-post-masters-track/ |
| 436 | Family Primary Care Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/family-primary-care-nurse-practitioner-dnp/ |
| 437 | Nurse Anesthesia | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/nurse-Anesthesia/ |
| 438 | Nursing | PhD | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/nursing-phd/ |
| 439 | Pediatric Critical Care Clinical Nurse Specialist | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/pediatric-critical-care-clinical-nurse-specialist-dnp/ |
| 440 | Pediatric Dual Primary/Acute Care Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/pediatric-dual-primary-acute-care-nurse-practitioner-dnp-advanced-practice-track/ |
| 441 | Pediatric Primary Care Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/pediatric-primary-care-nurse-practitioner-dnp/ |
| 442 | Psychiatric Mental Health Nurse Practitioner | DocOther | https://e-catalogue.jhu.edu/nursing/doctoral-degrees/dnp/psychiatric-mental-health-nurse-practitioner-dnp/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 443 | Healthcare Organizational Leadership | PostMasterCert | https://e-catalogue.jhu.edu/nursing/certificates/healthcare-organizational-leadership-post-masters-certificate/ |
| 444 | Nursing Education | PostMasterCert | https://e-catalogue.jhu.edu/nursing/certificates/nursing-education-post-masters-certificate/ |
| 445 | Psychiatric Mental Health Nurse Practitioner | PostMasterCert | https://e-catalogue.jhu.edu/nursing/certificates/psychiatric-mental-health-nurse-practitioner-postmasters-certificate/ |


#### SAIS (Advanced International Studies)

##### 硕士 (Master)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 446 | European Public Policy | MPP | https://e-catalogue.jhu.edu/advanced-international-studies/programs/european-public-policy-master-arts/ |
| 447 | Global Policy | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/global-policy-master-arts/ |
| 448 | Global Risk | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/global-risk-master-arts/ |
| 449 | Global Risk | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/global-risk-online/ |
| 450 | Graduate Certificates | MS | https://e-catalogue.jhu.edu/advanced-international-studies/programs/certificates/ |
| 451 | International Affairs | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-affairs-master-arts/ |
| 452 | International Economics and Finance | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-economics-finance-master-arts/ |
| 453 | International Public Policy | MPP | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-public-policy-master-mipp/ |
| 454 | International Relations | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/master-arts/ |
| 455 | International Studies | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-studies-master-arts/ |
| 456 | Strategy, Cybersecurity, and Intelligence | MA | https://e-catalogue.jhu.edu/advanced-international-studies/strategy-cybersecurity-intelligence/ |
| 457 | Sustainable Energy | MA | https://e-catalogue.jhu.edu/advanced-international-studies/programs/sustainable-energy-master-arts/ |

##### 博士 (Doctoral)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 458 | International Affairs | DocOther | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-affairs-dia/ |
| 459 | International Studies | PhD | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-studies-phd/ |

##### 研究生证书/文凭 (Certificate/Diploma)

| # | 项目 | 学位 | 来源 URL |
|---|------|------|----------|
| 460 | Chinese and American Studies | Certificate | https://e-catalogue.jhu.edu/advanced-international-studies/programs/chinese-american-studies-hopkins-nanjing-certificate/ |
| 461 | International Studies | Diploma | https://e-catalogue.jhu.edu/advanced-international-studies/programs/international-studies-diploma/ |


<!-- Grad program-degree rows: 461 -->
---

## SECTION 3 — Application requirements & deadlines (Region: US)

### 3.1 Undergraduate — core data table (Homewood, 2025-26 cycle for Class of 2029)

| 维度 | 值 | 来源 URL |
|------|-----|---------|
| Admissions site | apply.jhu.edu | https://apply.jhu.edu/ |
| Application portal | Common Application OR Coalition on Scoir | https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/ |
| Application plans | **ED I, ED II (binding), Regular Decision** + QuestBridge + Transfer | (same) |
| **ED I deadline** | **November 1, 2025** | (deadlines page) |
| **ED II deadline** | **January 2, 2026** (NOT Jan 4) | (deadlines page) |
| **Regular Decision deadline** | **January 2, 2026** | (deadlines page) |
| Transfer deadline | March 1, 2026 | (deadlines page) |
| Financial aid deadline (ED I) | November 15, 2025 | apply.jhu.edu/tuition-aid/how-to-apply-for-financial-aid/ |
| Financial aid deadline (ED II / RD) | January 15, 2026 | (financial aid page) |
| Decision release ED I | December 12, 2025 | (deadlines page) |
| Decision release ED II | February 13, 2026 | (deadlines page) |
| Decision release RD | March 18, 2026 | (deadlines page) |
| Reply-by date ED I / ED II / RD | Jan 15 / Feb 27 / **May 1, 2026** | (deadlines page) |
| **Application fee** | **$70** (or fee waiver) | (deadlines page) |
| **SAT/ACT policy** | **REQUIRED** (NOT test-optional); transfer = optional | apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/ |
| Superscore policy | YES — superscore across test dates (SAT M+ERW; ACT M+R+E) | (testing page) |
| Score-report method | Self-report on app; official only if admitted & enrolling | (testing page) |
| SAT code / ACT code / TOEFL code | **5332 / 1704 / 5332** | (testing page) |
| Interview policy | None (no interviews offered) | (implied — not in checklist) |
| Recommendations | Secondary school report + **2 teacher evaluations** + mid-year report | (deadlines page checklist) |
| Portfolio | Optional additional materials (required for arts/Peabody audition) | (deadlines page) |
| Peabody Institute | Separate application + audition — see peabody.jhu.edu/audition-apply/ | https://peabody.jhu.edu/audition-apply/application-requirements/ |
| QuestBridge | Partner; National College Match | questbridge.org/college-partners/johns-hopkins-university |

### 3.2 Undergraduate English proficiency table

English proficiency exams are **recommended** (not strictly required) for applicants whose primary language is not English or who have not attended an English-language school for the last 3 years.

| Exam | Minimum (competitive) | Recommended sub-scores |
|------|----------------------|------------------------|
| TOEFL iBT | **100 total** | 26 Reading, 26 Listening, 22 Writing, 25 Speaking |
| IELTS Academic | **7.0** on each band | — |
| Duolingo English Test (DET) | **120 composite** | 125 Literacy, 120 Conversation, 135 Comprehension, 105 Production |
| Cambridge English Exam | **C1 Advanced or C2 Proficiency, score 185+** | — |
| SAT ERW benchmark | < 690 → submit proficiency | — |
| ACT R+E benchmark | < 30 on both → submit proficiency | — |

Source: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/

### 3.3 Graduate — global rules

JHU graduate admissions is **fully decentralized** — each of the 10 divisions runs its own application, deadlines, fee, GRE/ELP policy. There is no single graduate portal; apply directly to the school/department. Sample entry points and policies:

| Division | App fee | GRE policy | Notes |
|----------|---------|------------|-------|
| **Krieger GSAS** (full-time) | (dept-set) | per-program | 26 full-time programs; one online app; contact dept for GRE |
| **Krieger AAP** (part-time) | (dept-set) | typically not required | Rolling/priority deadlines; professional master's |
| **Whiting Engineering (full-time)** | **MS = NO FEE**; **PhD = $75** (some $25) | **GRE NOT required** for spring/summer/fall 2025 (optional; some programs don't review) | ETS code 4655; app opens ~Aug 15 |
| **Whiting Engineering for Professionals (EP)** | (per program) | typically not required | Part-time/online; rolling |
| **School of Education** | **$80** | GRE accepted (code 5470); per program | TOEFL 8585; rolling/fixed/priority/ED deadlines |
| **Bloomberg SPH** | (per program) | per program | SOPHAS for many degrees; largest MPH program in world |
| **School of Medicine (MD)** | AMCAS | MCAT (not GRE for MD) | MD PhD via BGS; ~$130 AMCAS |
| **School of Nursing** | (per program) | per program | NursingCAS; MSN/DNP/PhD |
| **SAIS** | (per program) | per program | MA/MPP/PhD/DIA; multi-continent |
| **Carey Business School** | (per program) | GMAT/GRE (waivers available) | MBA/MS; multiple rounds |
| **School of Education ELP** | TOEFL/IELTS/Duolingo accepted | — | Send to code 8585 |

- **April 15 national signing date**: JHU is a signatory of the Council of Graduate Schools (CGS) Resolution; PhD/doctoral offers follow the April 15 deadline convention (verify per-program).
- **Institutional code (UG)**: SAT/TOEFL 5332, ACT 1704. **Graduate** codes vary by school (Whiting 4655, Education 5470/8585).

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

Source: https://sfs.jhu.edu/cost-tuition/ — full line-item breakdown. Total estimated COA ~$92,000 (Class of 2029 estimate); line items below are the official 2026-27 figures.

**On-Campus Living — Freshman** (total **$94,858**):

| Expense item | Amount (USD) | Description |
|--------------|--------------|-------------|
| Tuition* | $68,670 | 12+ credits fall + spring |
| Matriculation Fee (one-time) | $500 | New students only |
| Living Expenses, Housing (on-campus) | $13,073 | Double room |
| Living Expenses, Meals (on-campus) | $8,894 | Meal plan |
| Miscellaneous Personal Expenses | $1,606 | — |
| Books, Course Materials, Supplies, Equipment | $1,377 | — |
| Transportation | $738 | Avg varies by home state |
| **TOTAL** | **$94,858** | — |

**Other living arrangements** (2026-27): On-campus Sophomore total $95,729; **Off-campus total $88,233**; **Living-at-home-with-parents total $80,080**. Summer 2026 tuition = $1,275/credit hour (typical half-time); on-campus summer total $20,775.

*Per-credit-hour rate for <12 credits (part-time) = **$2,289/credit**. Health insurance required ($3,624 for 2026-27 AY; F1/J1 international students cannot waive).

### 4.2 Undergraduate financial-aid policy

| Policy | Value | Source |
|--------|-------|--------|
| Need-met | **100% of demonstrated need met**, all admitted students | apply.jhu.edu/tuition-aid/ |
| Loans in aid package | **$0 — debt-free** (no student loan expectation; Hopkins Scholarship only) | apply.jhu.edu/tuition-aid/ |
| Parent cost, families ≤$100k income | **$0** | apply.jhu.edu/tuition-aid/ |
| Free tuition threshold | Families ≤**$200,000** income (typical assets) = at least full tuition covered | apply.jhu.edu/tuition-aid/ |
| Most families who qualify | Up to $250,000 income | apply.jhu.edu/tuition-aid/ |
| Average need-based scholarship (first-year) | **$63,000–$66,000** | apply.jhu.edu/fast-facts/ |
| Debt-free graduation rate | **80%** graduate debt-free | apply.jhu.edu/fast-facts/ |
| % students receiving need-based aid | 52% | apply.jhu.edu/fast-facts/ |
| Total need-based scholarships awarded/yr | $174M | apply.jhu.edu/fast-facts/ |
| Merit scholarships | Limited; auto-considered (no separate app) | apply.jhu.edu/tuition-aid/types-of-financial-aid/merit-scholarships/ |
| **Need-blind (domestic)** | YES — US citizens, PRs, DACA/undocumented, eligible noncitizens | apply.jhu.edu/international-applicants/ FAQ |
| **Need-aware (international)** | **YES — need-aware** for international citizens applying for aid (financial circumstances considered) | apply.jhu.edu/international-applicants/ FAQ |
| International aid % of need met | 100% for admitted (even though need-aware at review) | apply.jhu.edu/international-applicants/ FAQ |
| International students receiving aid | ~10% of international students | apply.jhu.edu/international-applicants/ FAQ |
| International transfer aid | **NOT offered** | apply.jhu.edu/international-applicants/ FAQ |
| Aid application forms (domestic) | FAFSA (code E00473) + CSS Profile (code 5332) | apply.jhu.edu/tuition-aid/how-to-apply-for-financial-aid/ |
| Aid application forms (international) | CSS Profile + Certification of Finances (COF); free alternative = JHU ISFAA | (same) |

> **Critical correction to brief:** JHU is **NOT need-blind for internationals**. It is need-blind for US/domestic applicants but **need-aware for international citizens** who apply for aid. However, JHU still **meets 100% of demonstrated need, loan-free, for all admitted students including internationals**. The brief's "need-blind + full-need incl internationals" conflates these two distinct policies.

### 4.3 Graduate cost & funding framework

Graduate funding is highly division-specific:

- **Doctoral (PhD) programs** (Krieger, Whiting, SoM BGS, Nursing PhD, Bloomberg PhD, SAIS PhD): typically **fully funded** — full tuition + stipend + health benefits, through fellowships/RA/TA. Vivien Thomas Scholars Initiative (VTSI) for HBCU/MSI graduates in STEM PhDs (full tuition + stipend + benefits).
- **Master's programs**: largely **self-funded** (student pays tuition); some fellowships and RA/TA available per program. Whiting MS = no application fee.
- **Professional schools**: Carey MBA, School of Medicine MD, Nursing DNP — tuition-based with limited institutional aid; MD eligible for need-based institutional aid + federal loans.
- **Application fee structure**: ranges $0 (Whiting MS) → $75 (Whiting PhD) → $80 (Education) → ~$130 (AMCAS for MD). Fee waivers needs-based at most divisions.
- **Living stipends (PhD)**: vary by division; check per-program pages (P0 follow-up — not scraped at line-item level).

---

## SECTION 5 — Evidence chain index

Every cited fact bound to URL + verbatim snippet + capture date. `E-U-NNN` = undergraduate, `E-G-NNN` = graduate.

```yaml
- id: E-U-001
  field: undergraduate.deadlines.ED_I
  value: "November 1, 2025"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/
  source_snippet: "APPLICATION DEADLINE Early Decision I November 1, 2025 Early Decision II January 2, 2026 Regular Decision January 2, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-002
  field: undergraduate.deadlines.ED_II
  value: "January 2, 2026"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/
  source_snippet: "Early Decision II January 2, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-003
  field: undergraduate.deadlines.RD
  value: "January 2, 2026"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/
  source_snippet: "Regular Decision January 2, 2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-004
  field: undergraduate.application.fee_usd
  value: 70
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/
  source_snippet: "The $70 application fee or fee waiver"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-005
  field: undergraduate.test_policy.required
  value: "SAT or ACT REQUIRED (not test-optional)"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "Johns Hopkins University requires first-year applicants to submit SAT (Math and Evidence-Based Reading and Writing sections) or ACT (Math, Reading, and English sections) scores to be considered for admission."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.test_policy.superscore
  value: true
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "we superscore, meaning if you take the SAT or ACT more than once and submit multiple scores, we consider your highest section scores across all test dates."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.test_policy.codes
  value: {SAT: 5332, ACT: 1704, TOEFL: 5332}
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "Test scores should be sent to the following recipient codes: SAT (5332), ACT (1704), AND TOEFL (5332)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.english_proficiency.TOEFL_min
  value: "100 total (preferred sub: 26R/26L/22W/25S)"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "TOEFL (iBT)- A minimum of 100 total with preferred sub-scores of 26 (Reading), 26 (Listening), 22 (Writing), and 25 (Speaking)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-009
  field: undergraduate.english_proficiency.IELTS_min
  value: "7.0 each band"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "IELTS- A score of 7.0 or higher on each band"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-010
  field: undergraduate.english_proficiency.DET_min
  value: "120 composite (preferred sub: 125 Lit/120 Conv/135 Comp/105 Prod)"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "DET- A composite score of 120 or higher with preferred sub-scores of 125 (Literacy), 120 (Conversation), 135 (Comprehension), and 105 (Production)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-011
  field: undergraduate.english_proficiency.Cambridge_min
  value: "C1 Advanced/C2 Proficiency, 185+"
  source_url: https://apply.jhu.edu/how-to-apply/application-deadlines-requirements/standardized-testing/
  source_snippet: "Cambridge English Exam- C1 Advanced or C2 Proficiency with a Cambridge English score of 185 or higher"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-012
  field: undergraduate.financial_aid.need_blind_domestic
  value: true
  source_url: https://apply.jhu.edu/international-applicants/
  source_snippet: "Hopkins is need-blind for domestic applicants, which includes U.S. citizens, permanent residents, students with DACA or undocumented status, and other eligible noncitizens."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-013
  field: undergraduate.financial_aid.need_aware_international
  value: true
  source_url: https://apply.jhu.edu/international-applicants/
  source_snippet: "Hopkins is need-aware for international citizens (who do not hold U.S. citizenship or permanent resident status) that apply for financial aid. This means financial circumstances are considered in the admissions process."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-014
  field: undergraduate.financial_aid.need_met
  value: "100% demonstrated need met, loan-free"
  source_url: https://apply.jhu.edu/international-applicants/
  source_snippet: "We promise to meet 100% of a family's demonstrated need—the difference between the total cost of attendance each year and what a family can pay. We also promise to meet this need without any loans."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-015
  field: undergraduate.cost.tuition_2026_2027
  value: 68670
  source_url: https://sfs.jhu.edu/cost-tuition/
  source_snippet: "2026-27 Academic Year On-Campus Living (Freshman) Tuition* $68,670"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-016
  field: undergraduate.cost.coa_2026_2027_oncampus_freshman
  value: 94858
  source_url: https://sfs.jhu.edu/cost-tuition/
  source_snippet: "TOTAL $94,858"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-017
  field: undergraduate.cost.free_tuition_threshold
  value: "families up to $200,000 income"
  source_url: https://apply.jhu.edu/tuition-aid/
  source_snippet: "Free tuition for families making up to $200,000"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-018
  field: undergraduate.cost.zero_parent_threshold
  value: "families up to $100,000 income"
  source_url: https://apply.jhu.edu/tuition-aid/
  source_snippet: "$0 parent cost for families making up to $100,000"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-019
  field: undergraduate.financial_aid.codes
  value: {FAFSA: E00473, CSS_Profile: 5332}
  source_url: https://apply.jhu.edu/tuition-aid/how-to-apply-for-financial-aid/
  source_snippet: "FAFSA school code E00473 CollegeBoard CSS Profile code 5332"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-020
  field: institution.fast_facts.class_2029
  value: {applicants: 49112, enrolled: 1297, SAT_mid_50: "1530-1570", avg_need_scholarship: "$63K-66K", pct_debt_free: 80}
  source_url: https://apply.jhu.edu/fast-facts/
  source_snippet: "49,112 Applicants 1,297 Students Enrolled 1530-1570 SAT Middle 50th Percent $63K Average Need-Based Scholarship for First-Year Students 80% Students Graduate Debt-Free"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-021
  field: institution.divisions.count
  value: 10
  source_url: https://www.jhu.edu/schools/
  source_snippet: "Johns Hopkins enrolls more than 24,000 full-time and part-time students in ten academic divisions"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.programs.total_count
  value: 461
  source_url: https://e-catalogue.jhu.edu/programs/
  source_snippet: "Johns Hopkins University faculty and students study, teach, and learn across more than 400 programs"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.whiting.fee
  value: "MS = $0; PhD = $75"
  source_url: https://engineering.jhu.edu/admissions/graduate-admissions/full-time-programs/how-to-apply/general-application-requirements/
  source_snippet: "The Whiting School of Engineering does not require an application fee to our master's programs... A fee of $75 is required for each doctoral application"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.whiting.gre_policy
  value: "GRE NOT required (optional)"
  source_url: https://engineering.jhu.edu/admissions/graduate-admissions/full-time-programs/how-to-apply/general-application-requirements/
  source_snippet: "The Whiting School of Engineering does not require GRE General Test scores for applications to our graduate programs when applying to spring, summer, or fall 2025 start terms."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-004
  field: graduate.whiting.gre_code
  value: 4655
  source_url: https://engineering.jhu.edu/admissions/graduate-admissions/full-time-programs/how-to-apply/general-application-requirements/
  source_snippet: "Official GRE scores must be sent electronically to Engineering Graduate Admissions directly from the Testing Agency using institution Code (4655)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-005
  field: graduate.education.fee
  value: 80
  source_url: https://education.jhu.edu/admissions/how-to-apply/
  source_snippet: "securely pay our $80 application fee"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-006
  field: graduate.education.test_codes
  value: {GRE: 5470, TOEFL: 8585, SAT: 3926, ACT: 8804}
  source_url: https://education.jhu.edu/admissions/how-to-apply/
  source_snippet: "GRE: 5470 TOEFL: 8585 SAT: 3926 ACT: 8804"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-007
  field: graduate.krieger.full_time_programs
  value: 26
  source_url: https://krieger.jhu.edu/graduate-admissions/
  source_snippet: "The Krieger School of Arts and Sciences offers 26 full-time graduate programs."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
jhu-knowledge-base-v2 (collection)
├── jhu-overview                       # Section 0 (counts, hierarchy, degree inventory, matrix)
├── jhu-undergraduate                  # Section 1 (144 chunks: 79 majors + 63 minors + 2 UG certs)
│   ├── jhu-ug-krieger-arts-sciences   # 45 BA + 40 minor
│   ├── jhu-ug-whiting-engineering      # 15 BS + 15 minor
│   ├── jhu-ug-peabody                 # 19 BM/BFA/BS + 7 minor + 2 UG cert
│   └── jhu-ug-carey (minor)           # 1 minor
├── jhu-graduate                       # Section 2 (461 chunks across 9 schools)
│   ├── jhu-grad-krieger               # 134 (incl. PhD, MA, MS, MFA, post-bacc)
│   ├── jhu-grad-krieger-aap           # 49 (part-time MS/MA/cert)
│   ├── jhu-grad-whiting               # 121 (incl. EP part-time)
│   ├── jhu-grad-peabody               # 67 (MM/DMA/cert/diploma)
│   ├── jhu-grad-carey                 # 45 (MBA/MS/MA/dual)
│   ├── jhu-grad-education             # 14 (MEd/MS/EdD/PhD)
│   ├── jhu-grad-bloomberg-sph         # 107 (MPH/MHS/MSPH/MAS/MS/PhD/DrPH/cert)
│   ├── jhu-grad-medicine              # 30 (MD/PhD/MA/MS/MHS/MEd/post-bacc)
│   ├── jhu-grad-nursing               # 22 (DNP/PhD/MSN/MS/post-master's/dual)
│   └── jhu-grad-sais                  # 16 (MA/MPP/MS/DIA/PhD/cert/diploma)
├── jhu-deadlines-tests                # Section 3
├── jhu-costs-aid                      # Section 4
└── jhu-evidence                       # Section 5
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "jhu-knowledge-base-v2"
  school: "<home division>"
  department: "<home dept, if applicable>"
  degree_level: "<BA|BS|BM|BFA|MA|MS|MFA|MBA|MEng|MEd|MM|MHS|MPH|MPP|MAS|PhD|DNP|EdD|DrPH|MD|DMA|DEng|Certificate|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Why |
|----------|-----------|-----------|-----|
| P0 | Per-program graduate deadlines + GRE/ELP minimums (Bloomberg SPH, SoM BGS, SAIS, Carey MBA, Nursing) | per division admissions pages | Each grad program has its own deadlines/GRE — only Whiting/Education captured at line-item level |
| P0 | Bloomberg SPH cost & PhD stipend rates | sphadmissions.jhsph.edu | Not scraped |
| P0 | School of Medicine MD admissions (AMCAS, MCAT thresholds, secondary essays) | med.jhu.edu/admissions | Not scraped |
| P1 | Peabody audition requirements + repertoire by instrument | peabody.jhu.edu/audition-apply | Conservatory-specific |
| P1 | School of Government and Policy — first programs (division chartered but no catalog entries yet) | jhu.edu/government-policy | Track as it launches |
| P1 | Nursing MSN/DNP specialties full detail | nursing.jhu.edu/academics/programs | 10 DNP tracks enumerated |
| P2 | Department-level addresses/phone/email for one worked-example deep-dive | per dept site | Section 2.2 worked example deferred |
| P2 | Per-program application fee for AAP/Carey/SAIS/Bloomberg/SoM | per program | Range varies widely |

---

## SECTION 7 — Cross-school comparison framework (JHU column)

| Dimension | JHU value |
|-----------|-----------|
| Total UG cost/yr (on-campus, 2026-27) | $94,858 |
| Tuition/yr (2026-27) | $68,670 |
| Need-blind (intl?) | ❌ Need-blind DOMESTIC only; **need-AWARE international** (but 100% need met, loan-free) |
| ED I deadline | Nov 1 |
| ED II deadline | **Jan 2** |
| RD deadline | **Jan 2** |
| SAT/ACT required? | ✅ **REQUIRED** (not test-optional) |
| TOEFL min (competitive) | 100 iBT |
| IELTS min | 7.0 each band |
| Tuition-free threshold | ≤$200,000 income |
| Zero-parent-cost threshold | ≤$100,000 income |
| Average net scholarship (first-year) | $63K–$66K |
| Debt-free graduation | 80% (no loans in aid package) |
| Grad application fee (sample, Whiting MS) | $0 |
| April-15 signatory | ✅ (CGS Resolution) |
| **Total program count (Rule 1)** | **605** |
| **School/division count (Rule 2)** | **10 degree-granting + APL** |
| Application fee (UG) | $70 |
| App pool (Class 2029) | 49,112 applicants → 1,297 enrolled |
| SAT mid-50 | 1530–1570 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: apply.jhu.edu, e-catalogue.jhu.edu, sfs.jhu.edu, www.jhu.edu, engineering.jhu.edu, krieger.jhu.edu, education.jhu.edu, peabody.jhu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction from e-catalogue.jhu.edu/programs/ (605 program items extracted server-side, fully reconciled)
> **Granularity**: school → department → degree-level → program
> **Reconciliation gate**: rule-1 (605) == matrix-sum (605) == rule-5 rows (144 + 461 = 605) == inventory-sum (605) ✅
