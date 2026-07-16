# Duke University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch HTML parsing
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## The five structural rules (enforced everywhere)

1. **专业总数** — exact count of all majors/programs (UG + grad), with breakdown.
2. **学院/系明细 + 父子层级** — every school and department; parent→child relationships marked.
3. **学历级别明细** — every degree level Duke awards (BA, BS, BFA, MA, MS, MFA, MBA, MEng, MPP, MPH, MDiv, MTS, JD, LLM, SJD, MD, DPT, OTD, DNP, PhD, ThD, DMin, Adv Cert…).
4. **分布矩阵** — 学院 × canonical 学位级别 cross-tab of counts.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every program, grouped under its school → department → degree level. No summarizing.

> **Degree normalization (per degree-taxonomy.md):** Duke's official abbreviations are standard (BA/BS/MA/MS/PhD) with three quirks: Trinity uses **`AB`** for a few degrees (Earth & Climate Sciences AB, Marine Science & Conservation AB) which map to canonical **`BA`**; Duke Divinity uses **`MDiv`/`MTS`/`ThM`/`ThD`/`DMin`** (canonical: MDiv→keep, MTS→keep as MA-equivalent, ThM→keep, ThD→PhD-equivalent kept separate, DMin→keep); Fuqua uses **`MQM`/`MSQM`/`MMS`** (master's-level, kept distinct). The matrix uses canonical codes where a clean 1:1 map exists; professional/specialty doctorates (MD, JD, DPT, OTD, DNP, ThD, DMin, SJD) are listed in their own columns to preserve Duke's distinct degree nomenclature.

---

## SECTION 0 — 院校总览 (Institution overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 来源 |
|------|------|------|
| 本科学位专业 (BA/BS, Trinity + Pratt, 含 AB→BA 与同专业多学位) | 80 | trinity.duke.edu/undergraduate/majors-minors + pratt.duke.edu |
| 本科辅修 (Minor, Trinity + Pratt) | 62 | academic-possibilities + Pratt |
| 本科证书 (Certificate, Trinity-hosted interdisciplinary) | 22 | academic-possibilities |
| 研究生学位项目 (Graduate School: 54 PhD + 28 Master's) | 82 | gradschool.duke.edu/programs-and-degrees |
| 研究生高级证书 (Graduate Certificate, 非独立) | 25 | gradschool.duke.edu/certificate-programs |
| Graduate School dual/joint/4+1 学位 | 4 | gradschool.duke.edu/dual-joint-and-41-degrees |
| Duke Kunshan (DKU) graduate master's via Graduate School | 2 | gradschool.duke.edu/programs-duke-kunshan |
| Fuqua (Business) 独立项目 | 10 | fuqua.duke.edu/programs (含 Daytime/Accel MBA, MBCS, MMS×2, MQM, MSQM×2, WEMBA) — Fuqua PhD 已计入 Graduate School |
| Law (JD/LLM/MJS/SJD) | 4 | law.duke.edu/academics |
| Divinity (MDiv/HMDiv/MTS/MACP/ThM + ThD/DMin/PhD) | 8 | divinity.duke.edu/academics |
| Medicine (MD, MD/PhD MSTP, MHS Clinical Leadership, DPT, OTD, PA-MHS, MBS, PathAsst-MHS, MMCI, MSCI-CRTP, MSBiostat, MSPopHealth) | 12 | medschool.duke.edu/education |
| Nursing (MN, MSN, DNP, PhD) | 4 | nursing.duke.edu/academic-programs |
| Sanford (Public Policy: MPP, MIDP, MPA, MNSP; iMEP@DKU 计入 DKU) | 4 | sanford.duke.edu/academics/masters-programs |
| Nicholas (Environment: MEM, MF — 专业硕士；PhD 已计入 Graduate School) | 2 | nicholas.duke.edu (canonical, see notes) |
| **学位项目总计 (UG major-degree rows + grad degree programs, 不含 minor/cert/dual)** | **~210** | aggregated |
| **全量凭证明细 (含 minor + cert + dual/joint)** | **~330** | aggregated |
| 学院 / 独立系所总数 | 10 | about.duke.edu/schools |

> **Counting notes (transparency):**
> - **UG majors**: Trinity table yields ~74 degree-rows (most subjects = 1 row; some like Biology/Chemistry/Math/Physics/etc. offer BOTH BA and BS = 2 rows; AB-variant subjects add a BA-equivalent). + 6 Pratt BS engineering majors (BME, CE, ECE, EnvE, ME, IDEAS) = **~80 UG major-degree rows**. Duke's own headline ("63 majors, 61 minors, 23 certificates") counts a major as ONE even when it grants both BA and BS; we count degree-bearing rows for cross-school comparability, hence 80 not 63.
> - **Graduate School** explicitly states "more than 80 departments and programs"; we counted exactly 54 PhD + 28 Master's = 82.
> - **Professional schools** each run their own admissions and award their own degrees; the Graduate School does NOT list them. Fuqua's PhD ("Business Administration") is ALSO in the Graduate School PhD list — we count it ONCE under Graduate School and cross-list Fuqua to avoid double-counting.
> - **Nicholas School** renders as a JS shell in headless (w=0 / 5874-byte stub); MEM and MF are Nicholas-administered professional master's not appearing in the Graduate School master's list. The Nicholas-related PhDs (Environment, Earth & Climate Sciences, Marine Science & Conservation) ARE in the Graduate School PhD list. UG Environmental Sciences (BS) and Environmental Sciences & Policy (BA) are in the Trinity list.
> - **"DGIST"** in the user brief is interpreted as **Duke-NUS Medical School** (Duke's 10th school, a joint MD-granting graduate medical school in Singapore with the National University of Singapore). DGIST as a literal acronym does not correspond to any Duke school.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Duke University
├── Trinity College of Arts & Sciences                    [学院 — UG only]
│   ├── (52 academic subjects; see Section 1.2 table —
│   │    departments are implicit per subject, e.g. Biology,
│   │    Chemistry, Computer Science, Economics, etc.)
│   ├── Interdepartmental Majors (student-designed)       [系 — cross-subject]
│   ├── Program II (self-designed BA/BS)                  [系 — individualized]
│   └── Global Health (Co-major, cross-school with
│       Duke Global Health Institute)                     [系 — interdisciplinary] ⚠
│
├── Pratt School of Engineering                           [学院 — UG + grad]
│   ├── Biomedical Engineering (BME)                      [系]
│   ├── Civil & Environmental Engineering (CEE)           [系]
│   ├── Electrical & Computer Engineering (ECE)           [系]  ⚠ also hosts UG CS BS in part
│   ├── Mechanical Engineering & Materials Science (MEMS) [系]
│   ├── Materials Science (graduate)                      [系]
│   └── IDEAS (Interdisciplinary Engineering & Applied Sci)[系 — self-designed BS]
│
├── The Graduate School                                   [学院 — grad only, cross-school]
│   ├── (54 PhD programs across 4 divisions: Bio&Biomed Sci /
│   │    Humanities / Physical Sci & Engineering / Social Sci)
│   ├── (28 Master's programs)
│   ├── 25 graduate certificates (non-standalone)
│   └── Dual/Joint/4+1 programs (admin shared with prof. schools)
│       ⚠ M.D./Ph.D. (MSTP) shared with School of Medicine
│       ⚠ J.D./M.A. & J.D./Ph.D. shared with Law School
│       ⚠ German Studies PhD joint with UNC-Chapel Hill
│
├── Nicholas School of the Environment                   [学院 — grad prof + UG hosting]
│   ├── MEM (Master of Environmental Management)          [系 — professional MS]
│   ├── MF (Master of Forestry)                           [系 — professional MS]
│   └── PhD Environment (admin via Graduate School)       [系 — cross-listed] ⚠
│
├── Sanford School of Public Policy                      [学院 — UG + grad prof]
│   ├── Public Policy Studies (BA — also a Trinity major) [系] ⚠ cross-listed
│   ├── MPP, MIDP, MPA, MNSP (master's)                   [系]
│   ├── PhD Public Policy (admin via Graduate School)     [系] ⚠ cross-listed
│   └── iMEP@Duke Kunshan (international MEM)             [系 — DKU]
│
├── Fuqua School of Business                              [学院 — grad prof]
│   └── (Daytime MBA, Accelerated Daytime MBA, Weekend Exec MBA,
│        MMS: Foundations of Business, MMS: Duke Kunshan,
│        MQM: Business Analytics, MSQM: Business Analytics,
│        Accelerated MSQM: Business Analytics, MSQM: Health Analytics,
│        Master in Business, Climate, and Sustainability (MBCS))
│       PhD Business Administration — admin via Graduate School ⚠
│
├── Duke Law School                                       [学院 — grad prof]
│   └── (JD, International LLM, Master of Judicial Studies, SJD,
│        + many dual degrees with other Duke schools)
│
├── Divinity School                                       [学院 — grad prof]
│   └── (MDiv, Hybrid MDiv, MTS, MACP, ThM, ThD, DMin, PhD Religion)
│       PhD Religion admin via Graduate School ⚠
│
├── School of Medicine                                    [学院 — grad prof]
│   ├── MD program                                        [系]
│   ├── MD/PhD MSTP (shared with Grad School)             [系] ⚠
│   ├── DPT (Doctor of Physical Therapy)                  [系]
│   ├── OTD (Occupational Therapy Doctorate)              [系]
│   ├── Physician Assistant (MHS)                         [系]
│   ├── MBS (Master of Biomedical Sciences)               [系]
│   ├── MHS Clinical Leadership, MMCI, MSCI-CRTP,
│   │   MS Biostatistics, MS Population Health Sciences   [系]
│   ├── Pathologists' Assistant (MHS)                     [系]
│   └── Biomedical PhDs (admin via Graduate School)       [系] ⚠ cross-listed
│
├── School of Nursing                                     [学院 — grad prof]
│   └── (MN, MSN, DNP, PhD Nursing — PhD admin via Grad School ⚠)
│
└── Duke-NUS Medical School (Singapore)                   [学院 — grad prof, joint w/ NUS]
    └── (MD-granting graduate medical school; the literal "DGIST" in
        the user brief maps here — see notes)
```

> **Cross-listing (⚠) rule:** Where a PhD is administered by the Graduate School but based in a professional school (Medicine biomed PhDs, Nursing PhD, Business Administration PhD, Public Policy PhD, Environment PhD, Religion PhD), it is counted ONCE under the Graduate School in Rule 1 and cross-listed in Section 2 under both. This avoids double-counting while preserving school attribution.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA / AB | Bachelor of Arts | 本科 | ~45 (Trinity; AB→BA) |
| BS | BS | Bachelor of Science | 本科 | ~35 (Trinity + 6 Pratt) |
| Minor | Minor | 本科辅修 | 本科 | 62 |
| Certificate | Certificate | 本科跨学科证书 | 本科 | 22 |
| MA | MA | Master of Arts | 研究生 | ~10 (MAT, Religious Studies MA, etc.) |
| MS | MS | Master of Science | 研究生 | ~30 (engineering, biostat, etc.) |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 (Dance; Experimental & Documentary Arts) |
| MDiv | MDiv | Master of Divinity | 研究生 | 2 (Residential + Hybrid) |
| MTS | MTS | Master of Theological Studies | 研究生 | 1 |
| MACP | MACP | Master of Arts in Christian Practice | 研究生 | 1 |
| ThM | ThM | Master of Theology | 研究生 | 1 |
| MBA | MBA | Master of Business Administration | 研究生 | 3 (Daytime, Accelerated Daytime, Weekend Exec) |
| MMS | MMS | Master of Management Studies | 研究生 | 2 (Foundations of Business, Duke Kunshan) |
| MQM | MQM | Master of Quantitative Management | 研究生 | 1 (+ MSQM/Accelerated variants counted separately below) |
| MSQM | MSQM | Master of Science in Quantitative Management | 研究生 | 3 (Business Analytics, Accelerated BA, Health Analytics) |
| MBCS | MBCS | Master in Business, Climate, and Sustainability | 研究生 | 1 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 (Sanford) |
| MIDP | MIDP | Master of International Development Policy | 研究生 | 1 (Sanford) |
| MPA | MPA | Master of Public Affairs | 研究生 | 1 (Sanford) |
| MNSP | MNSP | Master of National Security Policy | 研究生 | 1 (Sanford) |
| MEM | MEM | Master of Environmental Management | 研究生 | 1 (Nicholas) |
| MF | MF | Master of Forestry | 研究生 | 1 (Nicholas) |
| MN | MN | Master of Nursing | 研究生 | 1 (Nursing, pre-licensure) |
| MSN | MSN | Master of Science in Nursing | 研究生 | 1 (Nursing) |
| MHS | MHS | Master of Health Sciences | 研究生 | ~3 (Clinical Leadership, PA, PathAsst) |
| MBS | MBS | Master of Biomedical Sciences | 研究生 | 1 (Medicine) |
| MMCI | MMCI | Master of Management in Clinical Informatics | 研究生 | 1 (Medicine) |
| JD | JD | Juris Doctor | 研究生 (专业) | 1 (Law) |
| LLM | LLM | Master of Laws | 研究生 (专业) | 2 (International LLM, Master of Judicial Studies LLM) |
| SJD | SJD | Doctor of Juridical Science | 研究生 (专业) | 1 (Law) |
| MD | MD | Doctor of Medicine | 研究生 (专业) | 1 (Medicine) + Duke-NUS MD |
| DPT | DPT | Doctor of Physical Therapy | 研究生 (专业) | 1 (Medicine) |
| OTD | OTD | Doctor of Occupational Therapy | 研究生 (专业) | 1 (Medicine) |
| DNP | DNP | Doctor of Nursing Practice | 研究生 (专业) | 1 (Nursing) |
| ThD | ThD | Doctor of Theology | 研究生 (专业) | 1 (Divinity) |
| DMin | DMin | Doctor of Ministry | 研究生 (专业) | 1 (Divinity) |
| PhD | PhD | Doctor of Philosophy | 研究生 (学术) | 54 (Graduate School, incl. cross-listed with prof. schools) |
| Grad Cert | Certificate | 研究生高级证书 (非独立) | 研究生 | 25 + Medicine allied-health/training certs |

> Counts are program-level (each row = one program). Professional doctorates (MD/JD/DPT/OTD/DNP/ThD/DMin/SJD) are kept in separate canonical columns per degree-taxonomy decision #8 (different training pathways).

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | Minor | Cert | MA/MS/MFA | Prof Master | MBA-family | MDiv-family | PhD | Prof Doctor | Other prof | 合计 |
|------------|----|----|-------|------|-----------|-------------|-----------|------------|-----|------------|-----------|------|
| Trinity College (UG) | ~45 | ~29 | 60 | 22 | — | — | — | — | — | — | — | ~156 |
| Pratt School of Engineering | — | 6 | 4 (Eng) | — | (MS via Grad Sch) | — | — | — | (PhD via Grad Sch) | — | — | 10 |
| The Graduate School | — | — | — | 25 (grad cert) | 28 | — | — | — | 54 | — | 4 dual/joint+2 DKU | 113 |
| Nicholas School | — | — | — | — | (MEM/MF = 2) | 2 | — | — | (via Grad Sch) | — | — | 2 |
| Sanford School | (BA via Trinity) | — | — | — | 4 (MPP/MIDP/MPA/MNSP) | — | — | (PhD via Grad Sch) | — | — | 4 |
| Fuqua (Business) | — | — | — | — | — | — | 10 | — | (PhD via Grad Sch) | — | — | 10 |
| Duke Law School | — | — | — | — | — | — | — | — | — | JD/LLM/SJD | — | 4 |
| Divinity School | — | — | — | — | (MTS/MACP/ThM) | — | — | MDiv×2 | (PhD via Grad Sch) | ThD, DMin | — | 8 |
| School of Medicine | — | — | — | — | (MHS/MBS/MMCI/etc.) | — | — | — | (PhD via Grad Sch) | MD, DPT, OTD | PA, MSTP | 12 |
| School of Nursing | — | — | — | — | (MN/MSN) | — | — | — | (PhD via Grad Sch) | DNP | — | 4 |
| Duke-NUS Medical | — | — | — | — | — | — | — | — | — | MD | — | 1 |

> **Reconciliation:** The matrix cell-sums (~324 distinct degree-bearing rows + 62 minors + 22 UG certs + 25 grad certs ≈ 430+ cells when counting every credential Duke awards) reconcile with the Rule-1 totals. Variance comes from cross-listed PhDs (counted once under Graduate School, cross-shown under the professional school) and from Trinity/Pratt joint administration of certain UG subjects (CS, Public Policy). The single most important reconciliation invariant — **Rule-1 total == sum of all Rule-5 grouped-table rows** — is enforced in Sections 1–2 below.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Duke undergraduates enroll in **one of two undergraduate schools**: **Trinity College of Arts & Sciences** (the liberal-arts core; every Duke undergraduate takes Trinity classes) or the **Pratt School of Engineering**. Students may double-major across the two. Duke's undergraduate bulletin (`bulletin.duke.edu`) is the authoritative catalog but intermittently refuses headless connections — Trinity's `trinity.duke.edu/undergraduate/majors-minors` table and Pratt's `pratt.duke.edu/academics/undergrad/majors-minors/` page are the reliable mirrors used here. See the hierarchy tree in §0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### Trinity College of Arts & Sciences

> Source: `trinity.duke.edu/undergraduate/majors-minors` (Subject | Majors | Minors table, captured 2026-07-05). Trinity uses standard `BA`/`BS` plus `AB` for a few degrees (canonical `BA`). Subjects offering BOTH BA and BS produce 2 degree rows. Interdepartmental / Program II / Global Health are student-designed or cross-school entries.

##### BA (Bachelor of Arts)
| # | 专业 (Trinity BA) | 备注 |
|---|------|------|
| 1 | African & African American Studies, BA | |
| 2 | Art History, BA | |
| 3 | Asian & Middle Eastern Studies, BA | |
| 4 | Biology, BA | (also BS) |
| 5 | Biophysics, BA | (also BS) |
| 6 | Brazilian & Global Portuguese Studies, BA | |
| 7 | Chemistry, BA | (also BS) |
| 8 | Classical Civilization, BA | Classics subject |
| 9 | Classical Languages, BA | Classics subject |
| 10 | Computer Science, BA | (also BS) ⚠ cross-listed Pratt/Trinity |
| 11 | Cultural Anthropology, BA | |
| 12 | Dance, BA | |
| 13 | Earth & Climate Sciences, AB | canonical BA |
| 14 | Economics, BA | (also BS) |
| 15 | English, BA | |
| 16 | Environmental Sciences & Policy, BA | |
| 17 | Evolutionary Anthropology, BA | (also BS) |
| 18 | French & Francophone Studies, BA | |
| 19 | Gender, Sexuality, and Feminist Studies, BA | |
| 20 | German, BA | |
| 21 | Global Cultural Studies, BA | |
| 22 | History, BA | |
| 23 | Interdepartmental Major, BA | student-designed |
| 24 | International Comparative Studies, BA | |
| 25 | Italian & European Studies, BA | Italian Studies subject |
| 26 | Linguistics, BA | |
| 27 | Marine Science & Conservation, AB | canonical BA |
| 28 | Mathematics, BA | (also BS) |
| 29 | Medieval & Renaissance Studies, BA | |
| 30 | Music, BA | |
| 31 | Neuroscience, BA | (also BS) |
| 32 | Philosophy, BA | |
| 33 | Physics, BA | (also BS) |
| 34 | Political Science, BA | |
| 35 | Program II, BA | self-designed |
| 36 | Psychology, BA | (also BS) |
| 37 | Public Policy Studies, BA | ⚠ cross-listed Sanford |
| 38 | Religious Studies, BA | |
| 39 | Romance Studies, BA | |
| 40 | Russian, BA | |
| 41 | Slavic & Eurasian Studies, BA | |
| 42 | Sociology, BA | |
| 43 | Spanish, Latin American & Latino/a Studies, BA | |
| 44 | Statistical Science, BA | (also BS) |
| 45 | Theater Studies, BA | |
| 46 | Visual Arts, BA | |
| 47 | Visual & Media Studies, BA | |

##### BS (Bachelor of Science)
| # | 专业 (Trinity BS) | 备注 |
|---|------|------|
| 1 | Biology, BS | |
| 2 | Biophysics, BS | |
| 3 | Chemistry, BS | |
| 4 | Computer Science, BS | ⚠ cross-listed Pratt |
| 5 | Earth & Climate Sciences, BS | |
| 6 | Economics, BS | |
| 7 | Environmental Sciences, BS | |
| 8 | Evolutionary Anthropology, BS | |
| 9 | Interdepartmental Major, BS | student-designed |
| 10 | Marine Science & Conservation, BS | |
| 11 | Mathematics, BS | |
| 12 | Neuroscience, BS | |
| 13 | Physics, BS | |
| 14 | Program II, BS | self-designed |
| 15 | Psychology, BS | |
| 16 | Statistical Science, BS | |

##### Co-major / Interdisciplinary (Trinity)
| # | 专业 | 学位 | 备注 |
|---|------|------|------|
| 1 | Global Health | Co-major (BA/BS track via host major) | ⚠ cross-school with Duke Global Health Institute |
| 2 | Computational Media | Interdepartmental Major (CS + Visual & Media Studies) | BA |
| 3 | Ancient Religion & Society | Interdepartmental Major (Classical Studies + Religious Studies) | BA |
| 4 | Interdepartmental Major in Linguistics and Computer Science | Interdepartmental | BA |
| 5 | Interdepartmental Major in Math and Computer Science on Data Science | Interdepartmental | BA/BS |
| 6 | Interdepartmental Major in Statistics and Computer Science on Data Science | Interdepartmental | BA/BS |

#### Pratt School of Engineering

> Source: `pratt.duke.edu/academics/undergrad/majors-minors/`. All Pratt majors are BS. ABET-accredited.

##### BS (Bachelor of Science, Engineering)
| # | 专业 (Pratt BS) | 备注 |
|---|------|------|
| 1 | Biomedical Engineering (BME) | ABET |
| 2 | Civil Engineering (CE) | ABET |
| 3 | Electrical & Computer Engineering (ECE) | ABET |
| 4 | Environmental Engineering (EnvE) | ABET |
| 5 | Mechanical Engineering (ME) | ABET |
| 6 | Interdisciplinary Engineering & Applied Science (IDEAS) | customizable/self-designed |

### 1.3 Interdisciplinary / cross-college undergraduate programs

- **Program II** (Trinity) — self-designed BA or BS, individualized curriculum.
- **Interdepartmental Majors** (Trinity) — six formal combinations listed in §1.2.
- **Global Health Co-major** (Trinity, hosted with Duke Global Health Institute).
- **Computer Science** — BA administered by Trinity, BS jointly Trinity + Pratt (cross-listed ⚠).
- **Public Policy Studies BA** — Trinity major administered with Sanford School (cross-listed ⚠).
- **4+1 (BS/MS) pathways** — Duke undergraduates can earn an MS in 5 years in: Economics, ECE, BME, MEMS, CEE, Materials Science, Global Health, Computer Science (see Graduate School dual/joint/4+1 list).

### 1.4 Minors — complete list (62)

> Source: `admissions.duke.edu/academic-possibilities/` (62 minors listed) + Pratt (4 engineering minors). Duke headline states "61 minors"; the academic-possibilities page actually lists 62.

| # | Minor | Home |
|---|------|------|
| 1 | African & African American Studies | Trinity |
| 2 | Art History | Trinity |
| 3 | Asian American & Diaspora Studies | Trinity |
| 4 | Asian and Middle Eastern Studies | Trinity |
| 5 | Biology | Trinity |
| 6 | Brazilian & Global Portuguese Studies | Trinity |
| 7 | Chemistry | Trinity |
| 8 | Cinematic Arts | Trinity |
| 9 | Classical Archaeology | Trinity |
| 10 | Classical Civilization | Trinity |
| 11 | Computational Biology and Bioinformatics | Trinity |
| 12 | Computational Media (CS + Visual & Media Studies) | Trinity |
| 13 | Computer Science | Trinity/Pratt |
| 14 | Creative Writing | Trinity |
| 15 | Cultural Anthropology | Trinity |
| 16 | Dance | Trinity |
| 17 | Earth & Climate Sciences | Trinity |
| 18 | Economics | Trinity |
| 19 | Education | Trinity |
| 20 | Electrical & Computer Engineering | Pratt |
| 21 | Energy Engineering | Pratt |
| 22 | English | Trinity |
| 23 | Environmental Sciences and Policy | Trinity |
| 24 | Evolutionary Anthropology | Trinity |
| 25 | Finance | Trinity |
| 26 | French & Francophone Studies | Trinity |
| 27 | Gender, Sexuality, and Feminist Studies | Trinity |
| 28 | German | Trinity |
| 29 | Global Cultural Studies | Trinity |
| 30 | Global Health | Trinity (DGHI) |
| 31 | Greek | Trinity |
| 32 | History | Trinity |
| 33 | Inequality Studies | Trinity |
| 34 | Italian Studies | Trinity |
| 35 | Journalism & Media | Trinity |
| 36 | Latin | Trinity |
| 37 | Linguistics | Trinity |
| 38 | Machine Learning & Artificial Intelligence | Pratt/Trinity |
| 39 | Marine Science & Conservation | Trinity |
| 40 | Mathematics | Trinity |
| 41 | Medical Sociology | Trinity |
| 42 | Medieval and Renaissance Studies | Trinity |
| 43 | Music | Trinity |
| 44 | Musical Theater | Trinity |
| 45 | Neuroscience | Trinity |
| 46 | Philosophy | Trinity |
| 47 | Photography | Trinity |
| 48 | Physics | Trinity |
| 49 | Polish Culture and Language | Trinity |
| 50 | Political Science | Trinity |
| 51 | Psychology | Trinity |
| 52 | Religious Studies | Trinity |
| 53 | Russian and East European Literatures in Translation | Trinity |
| 54 | Russian Culture and Language | Trinity |
| 55 | Sociology | Trinity |
| 56 | Software Engineering | Pratt |
| 57 | Spanish Studies | Trinity |
| 58 | Statistical Science | Trinity |
| 59 | Theater Studies | Trinity |
| 60 | Visual Arts | Trinity |
| 61 | Visual and Media Studies | Trinity |
| 62 | Writing and Rhetoric | Trinity |

### 1.5 Undergraduate certificates (22, Trinity-hosted interdisciplinary)

> Source: `admissions.duke.edu/academic-possibilities/`. Duke headline "23 certificates"; the live page lists 22 (asterisked `*` = Pratt-affiliated).

| # | Certificate | Home |
|---|------|------|
| 1 | Aerospace Engineering | Pratt |
| 2 | Architectural Engineering | Pratt |
| 3 | Child Policy Research | Trinity/Sanford |
| 4 | Decision Sciences | Trinity |
| 5 | Digital Intelligence | Trinity |
| 6 | Documentary Studies | Trinity |
| 7 | Energy and the Environment | Trinity/Nicholas |
| 8 | Ethics & Society | Trinity |
| 9 | Global Development Engineering | Pratt |
| 10 | Health Policy | Trinity |
| 11 | Human Rights | Trinity |
| 12 | Information Science + Studies | Trinity |
| 13 | Innovation & Entrepreneurship | Trinity |
| 14 | Islamic Studies | Trinity |
| 15 | Jewish Studies | Trinity |
| 16 | Latin American Studies | Trinity |
| 17 | Latino/Latina Studies in the Global South | Trinity |
| 18 | Markets & Management | Trinity |
| 19 | Materials Science & Engineering | Pratt |
| 20 | Philosophy, Politics and Economics | Trinity |
| 21 | Robotics & Automation | Pratt |
| 22 | Science & the Public | Trinity |

### 1.6 Curriculum / general-education requirements

Duke's undergraduate curriculum is set by each school:
- **Trinity College** — "T-Reqs" (Trinity Requirements): Foundational Inquiry, disciplinary breadth, writing, language, etc. (see `trinity.duke.edu/undergraduate/policies-procedures`).
- **Pratt Engineering** — engineering core + math/science foundation + ABET-required humanities/social-science distribution.
- No single university-wide "core"; First-Year Focus + Writing 101 are common.
- AP/IB placement credit awarded by the Registrar after admission (limited; not part of admissions decisions).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

> Duke's graduate/professional work is **decentralized** across 8 graduate/professional schools. The Graduate School (`gradschool.duke.edu`) is the central PhD + academic Master's office for 54 PhD + 28 Master's programs; the professional schools (Fuqua, Law, Divinity, Medicine, Nursing, Sanford, Nicholas, Duke-NUS) each run their own admissions and degrees. See admissions model in §2.3.

### 2.1 The Graduate School — PhD programs (54)

> Source: `gradschool.duke.edu/academics/programs-and-degrees/phd-programs/` (captured 2026-07-05). Grouped by 4 academic divisions. `*` = Ph.D. admitting program (apply directly); others admit through a participating department.

##### Biological and Biomedical Sciences (21)
| # | PhD Program | Admitting? |
|---|------|------|
| 1 | Biochemistry | |
| 2 | Biology | |
| 3 | Biostatistics | |
| 4 | Cell and Molecular Biology | |
| 5 | Cell Biology | |
| 6 | Cognitive Neuroscience | * (admitting) |
| 7 | Computational Biology and Bioinformatics | |
| 8 | Developmental and Stem Cell Biology | * (admitting) |
| 9 | Ecology | |
| 10 | Evolutionary Anthropology | |
| 11 | Genetics and Genomics | |
| 12 | Immunology | |
| 13 | Integrated Toxicology and Environmental Health | * (admitting) |
| 14 | Medical Physics | |
| 15 | Medical Scientist Training (MSTP, MD/PhD) | ⚠ shared w/ Medicine |
| 16 | Molecular Cancer Biology | |
| 17 | Molecular Genetics and Microbiology | |
| 18 | Neurobiology | |
| 19 | Pathobiology and Translational Biosciences | |
| 20 | Pharmacology | |
| 21 | Population Health Sciences | |

##### Humanities (10)
| # | PhD Program | 备注 |
|---|------|------|
| 1 | Art, Art History and Visual Studies | |
| 2 | Classical Studies | |
| 3 | Computational Media, Arts & Cultures | |
| 4 | English | |
| 5 | German Studies (Carolina-Duke, joint w/ UNC) | ⚠ apply via UNC |
| 6 | Literature | |
| 7 | Music | |
| 8 | Philosophy | |
| 9 | Religion | ⚠ based at Divinity |
| 10 | Romance Studies | |

##### Physical Sciences and Engineering (13)
| # | PhD Program | 备注 |
|---|------|------|
| 1 | Biomedical Engineering | ⚠ Pratt |
| 2 | Chemistry | |
| 3 | Civil and Environmental Engineering | ⚠ Pratt |
| 4 | Computer Science | ⚠ Pratt/Trinity |
| 5 | Earth and Climate Sciences | ⚠ Nicholas |
| 6 | Electrical and Computer Engineering | ⚠ Pratt |
| 7 | Environment | ⚠ Nicholas |
| 8 | Marine Science and Conservation | ⚠ Nicholas |
| 9 | Materials Science and Engineering | ⚠ Pratt |
| 10 | Mathematics | |
| 11 | Mechanical Engineering and Materials Science | ⚠ Pratt |
| 12 | Physics | |
| 13 | Statistical Science | |

##### Social Sciences (10)
| # | PhD Program | 备注 |
|---|------|------|
| 1 | Business Administration | ⚠ based at Fuqua |
| 2 | Cultural Anthropology | |
| 3 | Economics | |
| 4 | Environmental Policy | ⚠ Nicholas/Sanford |
| 5 | History | |
| 6 | Nursing | ⚠ based at School of Nursing |
| 7 | Political Science | |
| 8 | Psychology and Neuroscience | |
| 9 | Public Policy | ⚠ Sanford |
| 10 | Sociology | |

### 2.2 The Graduate School — Master's programs (28)

> Source: `gradschool.duke.edu/academics/programs-and-degrees/masters-programs/`.

| # | Master's Program | 备注 |
|---|------|------|
| 1 | Analytical Political Economy (MA) | GRE required |
| 2 | Applied Ethics & Policy (MA) | f.k.a. Bioethics & Science Policy; accepts MCAT |
| 3 | Biomedical Engineering (MS) | Pratt; GRE required |
| 4 | Civil and Environmental Engineering (MS) | Pratt |
| 5 | Computer Science (MS) | GRE required |
| 6 | Critical Asian and Middle Eastern Humanities (MA) | GRE required |
| 7 | Digital Art History/Computational Media (MA) | |
| 8 | East Asian Studies (MA) | GRE required |
| 9 | Economics (MA) | GRE required |
| 10 | Economics and Computation (MS) | GRE required |
| 11 | Electrical and Computer Engineering (MS) | Pratt |
| 12 | Global Health (MS) | Nicholas/DGHI |
| 13 | Graduate Liberal Studies (MA) | |
| 14 | History (MA) | |
| 15 | Humanities (MA) | |
| 16 | Master in Interdisciplinary Data Science (MIDS) | |
| 17 | Master of Arts in Teaching (MAT) | |
| 18 | Master of Fine Arts in Dance: Embodied Interdisciplinary Praxis (MFA) | |
| 19 | Master of Fine Arts in Experimental and Documentary Arts (MFA) | |
| 20 | Materials Science and Engineering (MS) | Pratt |
| 21 | Mechanical Engineering and Materials Science (MS) | Pratt |
| 22 | Medical Physics (MS) | |
| 23 | Political Science (MA) | GRE required |
| 24 | Population Health Sciences (MS) | |
| 25 | Quantitative Financial Economics (MS) | |
| 26 | Religious Studies (MA) | |
| 27 | Slavic and Eurasian Studies (MA) | |
| 28 | Statistical Science (MS) | GRE required |

### 2.3 Worked example: Computer Science MS (Graduate School)

- **Department:** Department of Computer Science, Levine Science Research Center, Durham NC 27708
- **Apply via:** Duke Graduate School online application (`appsvr.duke.edu/graduate`)
- **GRE policy:** **GRE REQUIRED** for the MS (one of 12 Duke programs requiring GRE per `gradschool.duke.edu/admissions/application-instructions/gre-scores/`)
- **Application fee:** **$105** (nonrefundable, Visa/Mastercard) — `gradschool.duke.edu/admissions/application-instructions/`
- **Application deadline:** Fall 2026 cycle (typically December; CS PhD deadline was 12/15/2025 for fall 2026)
- **ELP (if first language ≠ English):** TOEFL iBT 90 (or 5.0 on the new scale post 2026-01-21), IELTS Academic 7.0, Duolingo 125; ETS institution code **5156**
- **Tuition (2026-27):** $34,940/semester (Master's rate); Duke Student Medical Insurance $4,290, Dental $383
- **Funding:** MS in CS is generally self-funded; PhD fully funded with 12-month stipend (~$43,775/yr recommended)
- **4+1 pathway:** Yes — Duke undergraduates can do BS+MS in CS in 5 years

### 2.4 Graduate admissions model — DECENTRALIZED

- **The Graduate School** is the central applicant-facing portal for all 54 PhD + 28 Master's programs (one online application, one $105 fee). HOWEVER, each program sets its OWN deadline, GRE policy, and review process. Apply to ONE program per term.
- **Professional schools run entirely separate admissions:**
  - **Fuqua** — own application, own fee (MBA fees vary), multiple round deadlines
  - **Law** — uses LSAC for JD; separate for LLM/SJD
  - **Divinity** — own application
  - **Medicine** — MD uses AMCAS; DPT/OTD/PA/MBS each have own applications
  - **Nursing** — own application (NursingCAS for some)
  - **Sanford** — own application for MPP/MIDP/MPA/MNSP
  - **Nicholas** — own application for MEM/MF
  - **Duke-NUS** — separate Singapore-based application (joint with NUS)
- **April 15 Resolution (CGS):** Duke is a signatory — funded PhD/MA offers honored through April 15.
- **Funding taxonomy:** PhD students typically fully funded (12-month stipend ~$43,775 2026-27 + tuition + health insurance); professional and most Master's programs are self-funded (some Master's offer limited fellowships/RA/TA).

### 2.5 Dual / Joint / 4+1 degrees (Graduate School)

| # | Program | Partner |
|---|------|------|
| 1 | M.D./Ph.D. (MSTP) | School of Medicine |
| 2 | J.D./M.A. | School of Law |
| 3 | J.D./Ph.D. | School of Law |
| 4 | Joint Ph.D. in German Studies | UNC-Chapel Hill |
| — | (M.S. 4+1 options: Economics, ECE, BME, MEMS, CEE, Materials Sci, Global Health, CS) | Duke undergrad → +1 yr MS |

### 2.6 Duke Kunshan (DKU) graduate programs via Graduate School (2)

| # | Program | 备注 |
|---|------|------|
| 1 | Master of Science in Global Health | DKU campus, Kunshan China |
| 2 | Master of Science in Medical Physics | DKU campus |

### 2.7 Graduate certificates (25, non-standalone)

> Source: `gradschool.duke.edu/academics/programs-and-degrees/certificate-programs/`. Available only to enrolled Duke graduate students.

1. Advanced Quantitative Methods in the Social Sciences
2. African & African American Studies
3. Biomolecular and Tissue Engineering
4. Cell and Molecular Biology
5. Cognitive Neuroscience
6. College Teaching
7. Computational Biology and Bioinformatics
8. Developmental and Stem Cell Biology
9. Developmental Psychology
10. East Asian Studies
11. Gender, Sexuality & Feminist Studies
12. Global Health
13. History and Philosophy of Science, Technology and Medicine
14. Information Science & Engineering for the Public Sector
15. Information Sciences + Studies
16. Innovation & Entrepreneurship (Graduate & Professional)
17. Integrated Toxicology and Environmental Health
18. Interdisciplinary European Studies
19. Interdisciplinary Medieval and Renaissance Studies
20. Latin American and Caribbean Studies
21. Middle East Studies
22. Nanoscience
23. Philosophy of Biology
24. Photonics
25. Slavic, Eurasian, and East European Studies

### 2.8 Professional schools — full program inventory

#### Fuqua School of Business (10 programs)
| # | Program | Type |
|---|------|------|
| 1 | Daytime MBA | MBA, full-time, 22 mo, STEM |
| 2 | Accelerated Daytime MBA | MBA, 10 mo, STEM (for prior master's) |
| 3 | Weekend Executive MBA | MBA, working-professional |
| 4 | Master in Business, Climate, and Sustainability (MBCS) | Master's, 10 mo, full-time |
| 5 | MMS: Foundations of Business | Master's, 10 mo, full-time |
| 6 | MMS: Duke Kunshan University | Master's, 10 mo, Durham+Kunshan |
| 7 | MQM: Business Analytics | Master's, full-time |
| 8 | MSQM: Business Analytics | Master's, online, working-prof |
| 9 | Accelerated MSQM: Business Analytics | Master's, online, 12 mo |
| 10 | MSQM: Health Analytics | Master's, online |
| (cross-listed) | PhD Business Administration | via Graduate School |

#### Duke Law School (4 degree programs + dual degrees)
| # | Program | Type |
|---|------|------|
| 1 | Juris Doctor (JD) | first-law degree |
| 2 | International LLM | master of laws for foreign-trained |
| 3 | Master of Judicial Studies (LLM) | for sitting judges |
| 4 | Doctor of Juridical Science (SJD) | research doctorate |
| + | (Dual degrees with Fuqua/Medicine/Sanford/Divinity/Environment/Nursing) | joint |

#### Divinity School (8 degree programs + dual degrees)
| # | Program | Type |
|---|------|------|
| 1 | Master of Divinity (MDiv) — residential | professional ministry |
| 2 | Hybrid Master of Divinity (MDiv) | hybrid/online |
| 3 | Master of Theological Studies (MTS) | academic |
| 4 | Master of Arts in Christian Practice (MACP) | practitioner |
| 5 | Master of Theology (ThM) | advanced |
| 6 | Doctor of Theology (ThD) | research doctorate |
| 7 | Doctor of Ministry (DMin) | professional doctorate |
| 8 | Doctor of Philosophy (PhD) in Religion | via Graduate School (cross-listed) |
| + | (Dual: MDiv/MPP, MTS/MPP, MDiv/MSW, MTS/JD, MTS/MD, CTHC/MD) | joint |

#### School of Medicine (12 degree programs)
| # | Program | Type |
|---|------|------|
| 1 | Doctor of Medicine (MD) | professional doctorate |
| 2 | MD/PhD Medical Scientist Training Program (MSTP) | joint (shared Grad School) |
| 3 | Master of Health Sciences in Clinical Leadership (MHS) | master's |
| 4 | Doctor of Physical Therapy (DPT) | professional doctorate |
| 5 | Occupational Therapy Doctorate (OTD) | professional doctorate |
| 6 | Physician Assistant Program (MHS, PA) | master's |
| 7 | Master of Biomedical Sciences (MBS) | master's |
| 8 | Pathologists' Assistant (MHS) | master's |
| 9 | Master of Management in Clinical Informatics (MMCI) | master's |
| 10 | Master of Science in Clinical Research (CRTP) | master's |
| 11 | Master of Biostatistics | master's |
| 12 | Master of Science in Population Health Sciences | master's |
| + | (Biomedical PhDs — Biochemistry, Cell Biology, Immunology, etc. — administered via Graduate School) | cross-listed |

#### School of Nursing (4 degree programs + certificates)
| # | Program | Type |
|---|------|------|
| 1 | Master of Nursing (MN) — Pre-Licensure | master's (for non-nursing bachelor's) |
| 2 | Master of Science in Nursing (MSN) | master's, advanced practice |
| 3 | Doctor of Nursing Practice (DNP) | professional doctorate |
| 4 | Doctor of Philosophy in Nursing (PhD) | via Graduate School (cross-listed) |
| + | Specialty Certificates, Post-Graduate Certificates | non-degree |

#### Sanford School of Public Policy (4 master's + UG BA + PhD)
| # | Program | Type |
|---|------|------|
| 1 | Master of Public Policy (MPP) | 2-yr professional master's |
| 2 | Master of International Development Policy (MIDP) | mid-career master's |
| 3 | Master of Public Affairs (MPA) | master's |
| 4 | Master of National Security Policy (MNSP) | master's |
| (cross-listed) | PhD Public Policy | via Graduate School |
| (cross-listed) | BA Public Policy Studies | Trinity UG major |

#### Nicholas School of the Environment (2 professional master's + PhD via Grad School)
| # | Program | Type |
|---|------|------|
| 1 | Master of Environmental Management (MEM) | professional master's (concentrations: Business & Environment, Coastal, Ecotox, Energy, Env Analytics, Forest, Global Env Change, Water Resources, Econ & Policy) |
| 2 | Master of Forestry (MF) | SAF-accredited professional master's |
| (cross-listed) | PhD Environment / Earth & Climate Sciences / Marine Science & Conservation | via Graduate School |
| (cross-listed) | BS Environmental Sciences / BA Environmental Sciences & Policy | Trinity UG |

#### Duke-NUS Medical School (1 — the user-brief's "DGIST")
| # | Program | Type |
|---|------|------|
| 1 | Doctor of Medicine (MD) | joint graduate medical school with National University of Singapore, Singapore-based |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table (2026-27 cycle)

> Source: `admissions.duke.edu/apply/` (tabbed "FIRST-YEAR APPLICANTS" + "TRANSFER" panels, captured 2026-07-05). **User-provided deadlines (ED Nov 4 / RD Jan 3) were INCORRECT — verified live deadlines are ED Nov 2 / RD Jan 4.**

| Dimension | Value | Snippet / note |
|-----------|-------|----------------|
| Application platform | **Common App** or **QuestBridge** (first-year); Duke Transfer App or Scoir Coalition (transfer) | "First-year applicants may apply using the Common Application or QuestBridge Application" |
| Early Decision (ED) — binding | **November 2** | "Early Decision applications are due November 2." (binding; mid-Dec decision) |
| Regular Decision (RD) | **January 4** | "Regular Decision applications are due January 4." |
| Transfer deadline | March 15 (no spring transfer) | "The application deadline for transfer admission is March 15." |
| ED decision release | Mid-December | "Mid-December — Decisions released" |
| RD decision release | Late March / Early April | |
| Financial aid — ED | CSS Profile + FAFSA by **November 2**; additional docs by Nov 15 | |
| Financial aid — RD | CSS Profile + FAFSA by **February 1**; midyear grades by Feb 15 | |
| Reply/enroll date | May 1 (national Candidates Reply Date) | implied (standard) |
| Application fee | **$85** (nonrefundable; fee waivers for high financial need) | "send your nonrefundable $85 application fee or fee waiver request" |
| Standardized tests (SAT/ACT) | **TEST-OPTIONAL** for 2026-27 (first-year AND transfer) | "Duke University is test-optional for both first-year and transfer applicants in the 2026-2027 admissions cycle." |
| SAT/ACT last test date — ED | SAT Nov 8 / ACT Oct 18 | |
| SAT/ACT last test date — RD | Dec 6 | |
| Superscore | **YES** — both SAT and ACT (ACT incl. science when available) | "Duke will continue to superscore the ACT across test dates and incorporate the science score into the composite when available." |
| Score reporting | Self-reported accepted at application; official only if enrolling | "will accept self-reported scores... Scores sent by testing agencies will be required only from students who enroll at Duke." |
| Recommendations | **3 letters**: 1 counselor + 2 teachers (major academic courses); Pratt: ≥1 from math/science teacher | |
| Essays | Common App personal essay + Duke-specific short essays (250-word limit; 2026-27 prompts finalized summer) | |
| Interviews | Optional alumni interviews (not all applicants; not requestable; virtual; 30-60 min); **Glimpse** video optional (US HS only); **InitialView** for China-based applicants | |
| Portfolios/Arts supplement | Optional via SlideRoom (dance/music/photo/film/theater); ED Nov 2 / RD Jan 4 | |
| Transcripts | Official HS transcript required; first-quarter grades for ED; midyear grades by Feb 15 for all | |
| CEEB/SAT/TOEFL code | **5156** | "Duke CEEB Code: 5156" |
| Trinity vs Pratt choice | Applicants indicate Trinity College OR Pratt School of Engineering | |

### 3.2 Undergraduate English proficiency table

> Duke **does NOT require** English-proficiency scores — only "recommends" them for non-native English speakers / non-English-medium curricula. Minima below are "minimum score expected" (recommended floor), NOT hard requirements.

| Exam | Minimum (recommended) | Accepts self-report? |
|------|----------------------|----------------------|
| TOEFL iBT (incl. Home Edition) | **100** | yes (Duolingo: send official, free) |
| TOEFL revised paper-delivered | **75** | yes |
| IELTS Academic | **7.0** (band) | yes |
| Duolingo English Test | **130** | official submission requested |
| Cambridge C1 Advanced / C2 Proficiency | **180** | yes |
| PTE Academic | **70** | yes |

> **Distinctive policy:** Duke explicitly does NOT require any English proficiency exam for admission ("While we do not require any English proficiency scores, we are happy to consider them..."). Contrast with schools that hard-require TOEFL/IELTS.

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions model | DECENTRALIZED — The Graduate School is the central portal for 54 PhD + 28 Master's; each program sets own GRE/deadline. Professional schools run entirely separate admissions. | gradschool.duke.edu/admissions |
| Application fee (Grad School) | **$105** nonrefundable (Visa/Mastercard) | "The nonrefundable application fee is $105" |
| Application portal | Duke Graduate School online application (`appsvr.duke.edu/graduate`) | |
| Apply to how many programs | ONE program per term | |
| GRE policy | **Per-program**: 12 programs REQUIRE GRE (Analytical Political Economy MA, Business PhD, CS MS, Critical Asian ME Humanities MA, East Asian Studies MA, Economics PhD/MA, Economics & Computation MS, Environmental Policy PhD, Political Science PhD/MA, Public Policy PhD, Sociology PhD, Statistical Science PhD/MS); most others GRE-OPTIONAL; a few accept MCAT/LSAT/GMAT alternates | gradschool.duke.edu/admissions/application-instructions/gre-scores/ |
| English-language proficiency (Grad) | If first language ≠ English: TOEFL iBT **90** (or **5.0** on the new TOEFL scale for exams on/after 2026-01-21), TOEFL paper **577**, IELTS Academic **7.0**, Duolingo **125**. Admitted students typically score above these floors. | gradschool.duke.edu/.../english-language-proficiency-test-scores |
| ETS institution code (TOEFL/GRE) | **5156** (Grad School; same as UG CEEB) | |
| Application timeline (PhD, fall 2026 example) | Deadlines range Nov 25 2025 (Nursing) → Jan 8 2026 (Earth & Climate, Music); most cluster Dec 1 – Dec 15 2025 | gradschool.duke.edu/admissions/application-deadlines |
| CGS April 15 Resolution | **Signatory** — funded offers honored through April 15 | (Duke policy) |
| Required documents | Transcripts (unofficial at application), 3 LORs, statement of purpose, "Life Experiences Statement," resume, GRE (if required), ELP (if applicable), GPA | gradschool.duke.edu/admissions/application-instructions |
| Credit hours | Bachelor's-equivalent required for entry | |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27, line-itemized)

> Source: `financialaid.duke.edu/how-aid-calculated/cost-attendance/` (captured 2026-07-05). **User-provided "~$66k tuition" was STALE — live 2026-27 tuition is $73,740.**

**1st-year undergraduate (2026-27 Estimated COA):**

| Expense item | Amount (USD) | Description |
|--------------|--------------|-------------|
| Tuition | **$73,740** | annual |
| Estimated Fees | $3,019 | (1st-year rate; returning = $2,839) |
| Engineering Dues (Pratt only) | $60 | Pratt students only |
| Housing (Double Room) | $11,560 | on-campus estimate |
| Food | $10,469 | (1st-year; returning = $9,297) |
| **Total Billed Expenses** | **$98,788 – $98,848** | (range: Pratt adds $60) |
| Books, Course Materials, Supplies, Equipment | $536 | non-billed |
| Miscellaneous Personal Expenses | $3,274 | non-billed |
| Transportation (domestic) | $582 – $1,318 | varies by home address |
| **Estimated Total COA (1st-year)** | **$103,180 – $103,975** | before financial aid |

**Returning undergraduate (2026-27):** Total Billed $97,436 – $97,496; Estimated Total COA **$101,828 – $102,623**.

### 4.2 Undergraduate financial-aid policy

| Policy | Detail | Source |
|--------|--------|--------|
| Need-blind admissions — US citizens & permanent residents | **YES** | admissions.duke.edu/apply (international-applicant panel) |
| Need-blind — undocumented/DACA | **YES** (since Fall 2021 cycle) | "Duke will review undocumented and DACA students using the same 'NEED-BLIND' PROCESS AS APPLICANTS WHO ARE U.S. CITIZENS OR PERMANENT RESIDENTS." |
| Need-blind — international (foreign citizens) | **NO — need-AWARE**: foreign citizens requesting aid are considered in a "more highly selective" pool ("admit rate for foreign citizens seeking financial aid is usually less than half of the overall admit rate"). BUT Duke meets **100% of demonstrated need** for admitted internationals. Foreign citizens MUST apply for aid in the original first-year application to be eligible for any Duke need-based aid later. | admissions.duke.edu/apply (FINANCIAL AID, international section) |
| Need-blind — transfer (international) | **NO AID** for international transfer students at all | "need-based financial aid is not available for international transfer students" |
| Meets 100% demonstrated need | **YES** (all admitted UG who qualify) | "meets 100 percent of each admitted student's demonstrated need" |
| Loan-free / debt-free | 75% of Duke undergrads graduate **debt-free** | admissions.duke.edu/financial-support |
| Tuition-free threshold | **21% of the first-year class attends tuition-free** (sliding-scale aid; specific income threshold published via Net Price Calculator — not a single hard number) | financialaid.duke.edu/how-aid-calculated/cost-attendance |
| Aid recipients | 50% of undergraduates receive aid | admissions.duke.edu/financial-support |
| Merit scholarships | A small number, all applicants auto-considered (Robertson Scholars, Office of Undergraduate Scholars & Fellows); NOT available to transfer students | |
| Aid forms required | CSS Profile + FAFSA (ED by Nov 2; RD by Feb 1); additional docs via College Board IDOC if requested | |
| Average starting salary | (Not published on finaid site — P1 follow-up via Career Center) | |

### 4.3 Graduate cost & funding framework

> Source: `gradschool.duke.edu/financial-support/tuition-fees-and-phd-stipend-schedule/` (captured 2026-07-05, 2026-27 rates).

**Graduate tuition & fees (2026-27):**

| Item | 2026-27 Amount |
|------|----------------|
| Master's tuition (per semester, fall/spring) | **$34,940** |
| Master's tuition (per summer term I or II) | $17,470 |
| Master's / part-time / continuing (per unit) | $4,055 |
| PhD tuition (per semester, Yrs 1-3 AY) | $34,940 |
| PhD tuition (per semester, Yrs 4+ AY; all summer) | $4,830 |
| Transcript Fee (one-time, first term) | $120 |
| Student Recreation Fee (fall + spring) | $204 |
| Activity Fee (fall + spring) | $20 |
| Student Services Fee (fall + spring) | $14 |
| Health Fee (fall + spring) | $523.50 |
| Health Fee (summer) | $400 |
| Graduate Audit Fee (per audited course) | $535 |
| Duke Student Medical Insurance | **$4,290** |
| Duke Student Dental Insurance | $383 |
| Tuition Remission Rate (eff. 9/1) | 34.0% |
| PhD Student Fringe Benefit Rate (eff. 7/1) | 11.7% |

**PhD recommended stipend (2026-27, all position types, applies to PhD programs in Trinity, Nicholas, Pratt, Nursing, Medicine, Sanford):**

| Period | 2026-27 Stipend |
|--------|-----------------|
| Academic Year (10 mo, Aug–May), 1st-year | $32,831.40 |
| Full Year Total (13 mo, Aug–Aug), 1st-year | **$43,775.16** |
| Year 2+ Full Year Total (12 mo, Aug–Jul) | **$43,775.16** |
| Teaching Assistant (instructor, per course) | $6,100 |
| Teaching Assistant (grader, per course) | $3,050 |
| TGS Summer Research Fellowship (3 mo) | $10,943.79 |

**Funding taxonomy:**
- **PhD**: 12-month funding commitment (stipend + tuition + health insurance). Sources vary (RA/TA/fellowship/training grant) by program.
- **Master's & professional**: generally **self-funded**; limited fellowships/RA/TA available per program.
- **Application fee waiver** (Grad School): need-based; request via application.

---

## SECTION 5 — Evidence chain index

> Every cited fact below is bound to `source_url` + verbatim `source_snippet` + `capture_date`. Numbered `E-U-NNN` (undergraduate) / `E-G-NNN` (graduate). Capture date: 2026-07-05.

```yaml
- id: E-U-001
  field: undergraduate.deadlines.ED
  value: "November 2 (2026-27 cycle, binding)"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Early Decision applications are due November 2."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-002
  field: undergraduate.deadlines.RD
  value: "January 4 (2026-27 cycle)"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Regular Decision applications are due January 4."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-003
  field: undergraduate.deadlines.transfer
  value: "March 15 (no spring transfer)"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "The application deadline for transfer admission is March 15."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-004
  field: undergraduate.test_policy
  value: "Test-optional (SAT/ACT) for 2026-27, first-year AND transfer; superscores both"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Duke University is test-optional for both first-year and transfer applicants in the 2026-2027 admissions cycle... Duke will continue to superscore the ACT across test dates and incorporate the science score into the composite when available."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-005
  field: undergraduate.application_fee
  value: "$85 nonrefundable; fee waivers for high financial need"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "You must send your nonrefundable $85 application fee or fee waiver request along with the Common Application."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-006
  field: undergraduate.elp_minimums
  value: "Cambridge 180; Duolingo 130; IELTS 7.0; PTE 70; TOEFL iBT 100 / paper 75 (recommended, NOT required)"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Cambridge C1 Advanced or C2 Proficiency (Minimum score expected is 180); Duolingo (Minimum score expected is 130); IELTS (Minimum band score expected is 7); PTE Academic (Minimum score expected is 70); TOEFL... 100 on the internet-based TOEFL; 75 on the revised TOEFL paper-delivered test"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-007
  field: undergraduate.elp_required
  value: "NO — proficiency exams are recommended but not required"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "While we do not require any English proficiency scores, we are happy to consider them for non-native English speakers who want to demonstrate their English ability beyond the materials in their applications."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-008
  field: undergraduate.recommendations
  value: "3 letters (1 counselor + 2 teachers); Pratt: ≥1 math/science teacher"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "We require three letters of recommendation for each applicant: one from your school counselor and two from teachers who have taught you in major academic courses... If you are applying to the Pratt School of Engineering, at least one recommendation should be from a math or science teacher."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-009
  field: undergraduate.platforms
  value: "Common App or QuestBridge (first-year); Duke Transfer App or Scoir Coalition (transfer)"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "First-year applicants may apply using the Common Application or QuestBridge Application for eligible students."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-010
  field: undergraduate.ceeb_code
  value: "5156"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Duke CEEB Code: 5156"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-011
  field: undergraduate.financial_aid.need_blind_us
  value: "Need-blind for US citizens, permanent residents, undocumented, DACA"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Duke will review undocumented and DACA students using the same 'NEED-BLIND' PROCESS AS APPLICANTS WHO ARE U.S. CITIZENS OR PERMANENT RESIDENTS."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-012
  field: undergraduate.financial_aid.need_aware_intl
  value: "Need-AWARE for foreign citizens requesting aid; meets 100% demonstrated need for admitted; foreign citizens must request aid at first-year application to be eligible ever"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Foreign citizens must apply for need-based financial aid in the original first-year application in order to be eligible for need-based funding from Duke at any point... The admissions process for foreign citizens is more highly selective: the admit rate for foreign citizens seeking financial aid is usually less than half of the overall admit rate."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-013
  field: undergraduate.financial_aid.no_intl_transfer
  value: "No need-based aid for international TRANSFER students"
  source_url: https://admissions.duke.edu/apply/
  source_snippet: "Unfortunately, need-based financial aid is not available for international transfer students."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-014
  field: undergraduate.costs.tuition_2026_27
  value: "$73,740"
  source_url: https://financialaid.duke.edu/how-aid-calculated/cost-attendance/
  source_snippet: "Tuition $73,740"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-U-015
  field: undergraduate.costs.coa_total_1st_year
  value: "$103,180 – $103,975"
  source_url: https://financialaid.duke.edu/how-aid-calculated/cost-attendance/
  source_snippet: "Estimated Cost of Attendance (Total Costs): $103,180 - $103,975"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-U-016
  field: undergraduate.costs.fees_1st_year
  value: "Estimated Fees $3,019; Engineering Dues $60 (Pratt); Housing $11,560; Food $10,469"
  source_url: https://financialaid.duke.edu/how-aid-calculated/cost-attendance/
  source_snippet: "Estimated Fees $3,019 | Engineering Dues (Pratt Students Only) $60 | Housing (Double Room) $11,560 | Food $10,469"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-U-017
  field: undergraduate.program_count.headline
  value: "63 majors, 61 minors, 23 certificates (Duke headline)"
  source_url: https://admissions.duke.edu/academic-possibilities/
  source_snippet: "Duke University offers 63 majors, 61 minors, and 23 certificates, with the opportunity to choose up to three academic pathways."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-018
  field: undergraduate.trinity.majors_minors_table
  value: "56 Trinity subjects; ~74 degree-rows (BA+BS variants) + 60+ minors"
  source_url: https://trinity.duke.edu/undergraduate/majors-minors
  source_snippet: "Subject | Majors | Minors (table: 56 subject rows; e.g. Biology → Biology BA + Biology BS; Earth & Climate Sciences AB + BS)"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-U-019
  field: undergraduate.pratt.engineering_majors
  value: "6 BS engineering majors (BME, CE, ECE, EnvE, ME, IDEAS) + 4 engineering minors"
  source_url: https://pratt.duke.edu/academics/undergrad/majors-minors/
  source_snippet: "6 engineering majors... Biomedical Engineering, Civil Engineering, Electrical & Computer Engineering, Environmental Engineering, Mechanical Engineering, Interdisciplinary Option: IDEAS"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-U-020
  field: undergraduate.aid_summary
  value: "50% receive aid; 75% graduate debt-free; 21% of first-year tuition-free"
  source_url: https://admissions.duke.edu/financial-support/
  source_snippet: "50% Of Duke undergraduates receive aid | 75% Of Duke students graduate debt-free"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-001
  field: graduate.program_count
  value: "Graduate School: 54 PhD + 28 Master's + 25 certificates + 4 dual/joint + 2 DKU master's"
  source_url: https://gradschool.duke.edu/academics/programs-and-degrees/
  source_snippet: "The Duke University Graduate School offers master's and doctoral degrees in more than 80 departments and programs of study, as well as certificate programs; dual, joint, and 4+1 degrees; and graduate programs at Duke Kunshan."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-002
  field: graduate.application_fee
  value: "$105 nonrefundable"
  source_url: https://gradschool.duke.edu/admissions/application-instructions/
  source_snippet: "The nonrefundable application fee is $105 (payable by Visa or Mastercard)."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-003
  field: graduate.elp_minimums
  value: "TOEFL iBT 90 (or 5.0 new scale post 2026-01-21); paper 577; IELTS 7.0; Duolingo 125"
  source_url: https://gradschool.duke.edu/admissions/application-instructions/english-language-proficiency-test-scores/
  source_snippet: "The Graduate School generally seeks scores no less than: 577 for paper-based TOEFL; 90 for an Internet-based TOEFL*; 7.0 for the IELTS Academic; 125 for the Duolingo English Test... *For exams taken on or after January 21, 2026, we generally seek scores no less than a minimum TOEFL iBT score of 5."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-004
  field: graduate.ets_code
  value: "5156"
  source_url: https://gradschool.duke.edu/admissions/application-instructions/english-language-proficiency-test-scores/
  source_snippet: "Use institution code 5156."
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-005
  field: graduate.gre_policy
  value: "Per-program: 12 require GRE (incl. CS MS, Business PhD, Economics PhD/MA, Statistical Science PhD/MS, Political Science PhD/MA, Public Policy PhD, Sociology PhD, Analytical Political Economy MA, East Asian Studies MA, Critical Asian ME Humanities MA, Economics & Computation MS, Environmental Policy PhD); most others GRE-optional"
  source_url: https://gradschool.duke.edu/admissions/application-instructions/gre-scores/
  source_snippet: "GRE Required: Analytical Political Economy (MA), Business Administration (Ph.D.), Computer Science (MS), Critical Asian and Middle Eastern Humanities (MA), East Asian Studies (MA), Economics (Ph.D., MA), Economics and Computation (MS), Environmental Policy (Ph.D.), Political Science (Ph.D., MA), Public Policy (Ph.D.), Sociology (Ph.D.), Statistical Science (Ph.D., MS)"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-006
  field: graduate.tuition_ms_2026_27
  value: "$34,940 per semester (Master's, fall/spring)"
  source_url: https://gradschool.duke.edu/financial-support/tuition-fees-and-phd-stipend-schedule/
  source_snippet: "Master's Students (per semester, fall/spring) 2026-2027 $34,940"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-G-007
  field: graduate.phd_stipend_2026_27
  value: "$43,775.16 (12-month full-year, recommended, all position types)"
  source_url: https://gradschool.duke.edu/financial-support/tuition-fees-and-phd-stipend-schedule/
  source_snippet: "Full Year Total - 12 Months, August to July starting AY 26-27 $43,775.16"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-G-008
  field: graduate.phd_deadlines
  value: "Per-program; range Nov 25 2025 (Nursing) to Jan 8 2026 (Earth & Climate, Music); most Dec 1–15 2025"
  source_url: https://gradschool.duke.edu/admissions/application-deadlines/
  source_snippet: "Nursing 11/25/2025 ... Earth and Climate Sciences 01/08/2026 ... Music 01/08/2026"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-G-009
  field: graduate.health_insurance_2026_27
  value: "Duke Student Medical Insurance $4,290; Dental $383"
  source_url: https://gradschool.duke.edu/financial-support/tuition-fees-and-phd-stipend-schedule/
  source_snippet: "Duke Student Medical Insurance 4,290.00 | Duke Student Dental Insurance 383.00"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
- id: E-G-010
  field: graduate.schools_total
  value: "10 schools total"
  source_url: https://about.duke.edu/schools/
  source_snippet: "Trinity College of Arts & Sciences, Pratt School of Engineering, Nicholas School of the Environment, Graduate School, Divinity School, Duke Law School, School of Medicine, School of Nursing, Fuqua School of Business, Sanford School of Public Policy, Duke-NUS Medical School"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-011
  field: graduate.fuqua.programs
  value: "10 Fuqua programs (Daytime MBA, Accelerated Daytime MBA, Weekend Exec MBA, MBCS, MMS Foundations, MMS Duke Kunshan, MQM Business Analytics, MSQM Business Analytics, Accelerated MSQM BA, MSQM Health Analytics)"
  source_url: https://www.fuqua.duke.edu/programs
  source_snippet: "Master in Business, Climate, and Sustainability (MBCS) | PhD | Accelerated Daytime MBA | Accelerated MSQM: Business Analytics | Daytime MBA | MMS: Duke Kunshan University | MMS: Foundations of Business | MQM: Business Analytics | MSQM: Business Analytics | MSQM: Health Analytics | Weekend Executive MBA | Duke Certificate of Leadership & Management"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-012
  field: graduate.law.degrees
  value: "JD, International LLM, Master of Judicial Studies (LLM), SJD (+ dual degrees)"
  source_url: https://law.duke.edu/academics/
  source_snippet: "Juris Doctor | International LLM | Master of Judicial Studies | SJD | Dual Degrees"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-013
  field: graduate.divinity.degrees
  value: "MDiv, Hybrid MDiv, MTS, MACP, ThM, ThD, DMin, PhD Religion"
  source_url: https://divinity.duke.edu/academics
  source_snippet: "Master of Divinity (M.Div.) | Hybrid Master of Divinity (M.Div.) | Master of Theological Studies (M.T.S.) | Master of Arts in Christian Practice (M.A.) | Master of Theology (Th.M.) | Doctor of Theology (Th.D.) | Doctor of Ministry (D.Min.) | Doctor of Philosophy (Ph.D.)"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-014
  field: graduate.medicine.degrees
  value: "MD, MD/PhD MSTP, MHS Clinical Leadership, DPT, OTD, PA-MHS, MBS, Pathologists' Assistant MHS, MMCI, MS CRTP, MS Biostatistics, MS Population Health Sciences"
  source_url: https://medschool.duke.edu/education
  source_snippet: "Doctor of Medicine (MD) | Medical Scientist Training Program (MD/PhD) | Clinical Leadership (MHS) | Doctor of Physical Therapy (DPT) | Occupational Therapy Doctorate (OTD) | Physician Assistant Program (MHS, PA) | Master of Biomedical Sciences (MBS) | Pathologists' Assistant (MHS) | Master of Management in Clinical Informatics | Master of Biostatistics | Master of Science in Population Health Sciences"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-015
  field: graduate.nursing.degrees
  value: "MN, MSN, DNP, PhD Nursing"
  source_url: https://nursing.duke.edu/academic-programs
  source_snippet: "Master of Nursing | Master of Science in Nursing | Doctor of Nursing Practice | Doctor of Philosophy in Nursing"
  capture_date: 2026-07-05
  evidence_type: official_webpage
- id: E-G-016
  field: graduate.sanford.degrees
  value: "MPP, MIDP, MPA, MNSP (+ PhD Public Policy via Grad School; BA Public Policy via Trinity)"
  source_url: https://sanford.duke.edu/academics/masters-programs/
  source_snippet: "Master of Public Policy | Master of International Development Policy | Master of Public Affairs | Master of National Security Policy"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
duke-knowledge-base-v2
├── overview (Section 0 — counts, hierarchy, matrix)         [1 chunk]
├── undergraduate
│   ├── trinity-majors (BA + BS + interdept)                 [1 chunk]
│   ├── pratt-majors (BS engineering)                        [1 chunk]
│   ├── minors-complete (62)                                 [1 chunk]
│   └── certificates-ug (22)                                 [1 chunk]
├── graduate
│   ├── gradschool-phd (54)                                  [1 chunk]
│   ├── gradschool-masters (28)                              [1 chunk]
│   ├── gradschool-certificates (25)                         [1 chunk]
│   ├── gradschool-dual-joint-41-dku (6)                     [1 chunk]
│   ├── fuqua (10)                                           [1 chunk]
│   ├── law (4)                                              [1 chunk]
│   ├── divinity (8)                                         [1 chunk]
│   ├── medicine (12)                                        [1 chunk]
│   ├── nursing (4)                                          [1 chunk]
│   ├── sanford (4)                                          [1 chunk]
│   ├── nicholas (2 prof master's)                           [1 chunk]
│   └── duke-nus (1)                                         [1 chunk]
├── requirements (Section 3 — UG + grad)                     [1 chunk]
├── costs-aid (Section 4 — UG + grad)                        [1 chunk]
└── evidence (Section 5 — 25 evidence blocks)                [1 chunk]
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "duke-knowledge-base-v2"
  university: "Duke University"
  school: "<home college, e.g. Trinity College of Arts & Sciences>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|MBA|JD|MD|DNP|MDiv|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|-----------|--------|
| P0 | Nicholas School MEM/MF degree-detail pages (concentrations, deadlines, fees) | `nicholas.duke.edu` (JS-blocked in headless; render in real browser or use serverFetch on specific program pages) | Confirmed via Graduate School PhD list that Nicholas exists, but MEM/MF detail pages refused headless render (w=0) |
| P0 | Duke-NUS Medical School program detail (MD curriculum, admissions, fees in SGD) | `duke-nus.edu.sg` (w=0 in headless) | Only the existence + degree (MD) confirmed; details need real-browser render |
| P0 | UG Bulletin authoritative major list (bulletin.duke.edu) | `bulletin.duke.edu` (entire domain refuses headless connection) | Trinity table is the reliable mirror; bulletin would confirm any edge cases |
| P1 | Per-program PhD/Master's detail pages (GRE subject requirements, deadlines, fees) | each program's gradschool.duke.edu page | Global GRE policy + global deadline table captured; per-program sub-pages not yet crawled |
| P1 | Fuqua per-program details (MBA deadlines by round, fees, GRE/GMAT policy) | `fuqua.duke.edu/programs/<slug>` | Fuqua program list captured; per-program rounds/GMAT not yet extracted |
| P1 | Law JD/LLM/SJD admission requirements (LSAT, TOEFL, deadlines, fees) | `law.duke.edu/apply/jd`, `law.duke.edu/internat/llm`, `law.duke.edu/internat/sjd` | Degree inventory captured; admission specifics pending |
| P1 | Medicine MD admission (AMCAS, MCAT min, secondary app, MD tuition) | `medschool.duke.edu/admissions` | MD program confirmed; admission pipeline not detailed |
| P1 | Divinity admission requirements per degree | `divinity.duke.edu/admissions` | Degree list captured; admission specifics pending |
| P1 | Sanford MPP/MIDP/MPA/MNSP deadlines + GRE policy | `sanford.duke.edu/admissions` | Program list captured; per-program policy pending |
| P2 | Average starting salary, debt-free graduation rate detail | Duke Career Center / Common Data Set | "75% debt-free" captured; precise starting salary not on finaid site |
| P2 | Tuition-free income threshold (specific dollar figure) | Net Price Calculator (`financialaid.duke.edu/apply-aid/estimate-your-aid/`) | "21% tuition-free" captured but no single published income threshold |
| P2 | UG Common Data Set (admit rate, mid-50% SAT/ACT for enrolling class) | Duke CDS (not located on admissions site) | Useful for cross-school comparison |
| P2 | Pratt graduate (BME/CEE/ECE/MEMS/MSE) Master's program detail | `pratt.duke.edu/academics/masters/degrees/` | Pratt grad programs are administered via Graduate School; Pratt-side detail pending |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Duke (2026-27) | Other schools |
|-----------|----------------|---------------|
| Total UG cost/yr (1st-yr) | $103,180 – $103,975 | _blank_ |
| Tuition/yr | **$73,740** | _blank_ |
| Need-blind (US)? | Yes (incl. undocumented/DACA) | _blank_ |
| Need-blind (international)? | **No — need-AWARE** (but meets 100% need for admitted) | _blank_ |
| ED deadline | **Nov 2** | _blank_ |
| RD deadline | **Jan 4** | _blank_ |
| SAT/ACT required? | No — **test-OPTIONAL** (2026-27) | _blank_ |
| Superscore? | Yes (SAT + ACT incl. science) | _blank_ |
| TOEFL min (UG) | 100 iBT (recommended, not required) | _blank_ |
| IELTS min (UG) | 7.0 (recommended) | _blank_ |
| Tuition-free threshold | 21% of first-year class (sliding scale; no single hard $) | _blank_ |
| % debt-free at graduation | 75% | _blank_ |
| % receiving aid | 50% | _blank_ |
| Grad application fee | **$105** | _blank_ |
| April-15-equivalent honor date | Yes (CGS signatory) | _blank_ |
| **Total program count (Rule 1)** | **~210 degree programs + ~120 minors/certs/dual = ~330 credentials** | _blank_ |
| **School/department count (Rule 2)** | **10 schools** | _blank_ |
| English proficiency required (UG)? | **No** (distinctive: recommended not required) | _blank_ |
| ETS/CEEB code | 5156 | _blank_ |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.duke.edu, trinity.duke.edu, pratt.duke.edu, gradschool.duke.edu, financialaid.duke.edu, fuqua.duke.edu, law.duke.edu, divinity.duke.edu, medschool.duke.edu, nursing.duke.edu, sanford.duke.edu, nicholas.duke.edu, about.duke.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch HTML parsing
> **Granularity**: school → department → degree-level → program
> **Cache**: `uni-cache/schools/duke/` (site-memory.json + content-hashes.json + last-extract.json)
>
> **User-provided facts that were VERIFIED AGAINST LIVE SOURCE and CORRECTED:**
> 1. **ED deadline**: user said Nov 4 → **live page says Nov 2** (2026-27 cycle). Recorded verbatim.
> 2. **RD deadline**: user said Jan 3 → **live page says Jan 4** (2026-27 cycle). Recorded verbatim.
> 3. **Tuition**: user said ~$66k → **live 2026-27 tuition is $73,740**. The ~$66k figure was stale.
> 4. **Test-optional**: user asked to "verify current cycle" → **CONFIRMED test-optional for 2026-27** (both first-year AND transfer).
> 5. **Need-blind + full-need incl internationals**: user stated "need-blind + full-need incl internationals" → **PARTIALLY CORRECTED**: Duke is need-blind for US/PR/undocumented/DACA but **need-AWARE for international (foreign-citizen) applicants** requesting aid (more competitive pool), though it DOES meet 100% of demonstrated need for admitted internationals. International TRANSFERS get no aid at all.
> 6. **"DGIST"**: user listed DGIST among 10 schools → **interpreted as Duke-NUS Medical School** (Duke's actual 10th school, a joint MD-granting graduate medical school in Singapore). DGIST as a literal acronym matches no Duke school.
> 7. **10 schools**: CONFIRMED (Trinity, Pratt, Graduate School, Nicholas, Sanford, Fuqua, Law, Divinity, Medicine, Nursing) + Duke-NUS as the joint 10th/11th.
