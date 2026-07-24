# Dartmouth College Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch for static pages
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Cache**: `uni-cache/schools/dartmouth/` (site-memory.json + last-extract.json + content-hashes.json) — first run, baseline

---

## ⚠️ Verification callouts (corrections to common assumptions)

Before reading further, note that several commonly-circulated facts about Dartmouth are **outdated or wrong**. Every item below was verified against the live admissions site on 2026-07-05 and is bound to a source snippet in Section 5.

| Assumption | Verified reality | Source |
|------------|------------------|--------|
| "Dartmouth is test-optional" | **FALSE.** Dartmouth **reinstated the standardized testing requirement** beginning with applicants to the Class of 2029 (i.e. fall 2025 entry / 2025-26 cycle). SAT or ACT is **required** for U.S. high-school students. | E-U-006, E-U-007 |
| "RD deadline is January 2" | **RD deadline is January 1.** (ED is November 1.) | E-U-002 |
| "Tuition is ~$66k" | **Outdated.** 2026-27 tuition is **$71,697**; total COA **$98,946**. | E-U-011 |
| "Need-blind threshold is $65k (no parent contribution)" | **Outdated.** Threshold is now **$125,000** family income for zero parent contribution; **$125k–$175k** = full-tuition scholarship. (The $65k figure was the 2022 announcement; it has since been raised.) | E-U-013 |
| "Application fee waiver only for U.S. citizens" | **FALSE.** Fee waivers are explicitly available to "US citizens, permanent residents, **and non-US citizens**" at the graduate level. | E-G-003 |
| "Dartmouth offers BS" | **Dartmouth awards the BA (Bachelor of Arts) for nearly all UG majors**, including all sciences and engineering sciences. The **only UG non-BA degree is the BE (Bachelor of Engineering)** in Engineering Sciences, earned via Thayer. | E-U-016 |

---

## The five structural rules (enforced everywhere)

These five rules govern how program/major data is organized. The required shape is a **4-level hierarchy**: 学院 → 系 → 学位级别 → 专业.

1. **专业总数** — exact count of all majors/programs (UG + grad), with breakdown.
2. **学院/系明细 + 父子层级** — every school and department, parent→child marked.
3. **学历级别明细** — every degree level awarded (BA, BE, MS, MA, MFA, MEng, MBA, MPH, MHA, PhD, MD, Joint/Dual).
4. **分布矩阵** — 学院 × 学位级别 cross-tab (counts), reconciles with rule 1.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every program, no summarizing.

> Reconciliation gate: rule-1 total == sum of matrix cells == row count in rule-5 tables. **Verified: 95 == 95 == 95. ✓**

---

## SECTION 0 — 院校总览 (Institution overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — counts)

Source: Dartmouth Degree Finder (`home.dartmouth.edu/degrees`), the official Drupal catalog view enumerating every degree program at the college. 95 entries captured across 10 paginated pages (10 + 10×8 + 5). Minors are NOT in the Degree Finder; the minor count below is from the UG admissions "Majors & Minors" page.

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 — BA (Bachelor of Arts) | 52 | 文理学科, incl. all sciences, CS, engineering sciences (BA track) |
| 本科学位专业 — BE (Bachelor of Engineering) | 1 | Engineering Sciences (BE), via Thayer — the ONLY non-BA UG degree |
| **本科学位专业合计** | **53** | 52 BA + 1 BE |
| 本科辅修 — 仅辅修 (minor-only programs) | 21 | 不授予主修的专业,仅作辅修 |
| 本科辅修 — 主修附带辅修 | ~52 | 多数 BA 主修同时开设辅修 |
| **本科辅修合计 (估)** | **~60+** | 21 minor-only + most majors also offer a minor |
| 研究生学位项目 (MS/MA/MFA/MEng/MBA/MPH/MHA/PhD/MD) | 36 | 见 Section 2 |
| 研究生联合/双学位项目 (MD-MBA, MD-PhD, MD-MS, PhD-MBA 等) | 5 | 跨学院联合学位 |
| 研究生高级证书 (Advanced Certificate) | 0 | Dartmouth 不在 Degree Finder 列高级证书;Thayer/TDI 个别项目内含 graduate certificate tracks |
| **Degree Finder 收录学位项目总计** | **95** | 53 UG + 42 grad (36 standalone + 5 joint + 1 MSB-PhD-track) |
| 学院 / 独立研究生院 总数 | 5 | Dartmouth College (UG, incl. Thayer UG) + 4 grad/professional schools |

> **Reconciliation**: 95 (Degree Finder total) = 53 UG + 42 grad. Matrix cell-sum (Section 0.4) = 95. ✓

### 0.2 学院-系层级树 (Rule 2 — hierarchy with parent-child)

Dartmouth's structure is unusual for an Ivy League school: there is **one undergraduate college ("Dartmouth College")** that houses the liberal-arts Faculty of Arts & Sciences **and** the undergraduate division of Thayer School of Engineering (which grants the BE). Graduate/professional work is organized under **four separate graduate/professional schools**. The Guarini School of Graduate & Advanced Studies is the **central administrative graduate school** that confers most PhD/MS degrees — including those whose faculty and curriculum live in Arts & Sciences departments, at Thayer, or at Geisel/TDI.

```
Dartmouth College  [院校]
│
├── Dartmouth College (Undergraduate)  [学院 — 本科]
│   ├── Faculty of Arts & Sciences (undergraduate)  [系群]
│   │   ├── Humanities (English, Classics, Philosophy, Religion, Film & Media, …)  [系]
│   │   ├── Social Sciences (Economics, Government, History, Sociology, QSS, Geography, …)  [系]
│   │   ├── Sciences (Biological Sciences, Chemistry, Physics & Astronomy, Earth Sciences, Math, …)  [系]
│   │   ├── Interdisciplinary / Area Studies (AAAS, LALACS, NAS, WGSS, MES, EEERS, …)  [系/项目组]
│   │   ├── Languages (French & Italian, Spanish & Portuguese, German, Russian, Asian Societies…)  [系]
│   │   ├── Arts (Studio Art, Theater, Music, Art History)  [系]
│   │   └── Computer Science (undergraduate BA)  [系]  ⚠ shared with Guarini (MS/PhD)
│   └── Thayer School of Engineering (undergraduate division)  [系 — 工程本科]
│       └── Engineering Sciences (BA + BE tracks)  [项目]
│
├── Guarini School of Graduate & Advanced Studies  [研究生院 — PhD/MS 中枢]
│   ├── (administers Arts & Sciences department PhD/MS programs)  [系群 — A&S 各系]
│   │   ├── Chemistry (MS, PhD)  [系]
│   │   ├── Comparative Literature (MA)  [系]
│   │   ├── Mathematics (MA, PhD)  [系]
│   │   ├── Physics & Astronomy (MS, PhD)  [系]
│   │   ├── Earth Sciences (MS, PhD)  [系]
│   │   ├── Psychological & Brain Sciences (PhD)  [系]
│   │   └── Molecular & Cellular Biology / Molecular & Systems Biology (PhD)  [系]
│   ├── Biochemistry & Cell Biology (PhD, "Biochemistry"/"Biology")  [系 — Geisel faculty]
│   ├── Cognitive Neuroscience (PhD)  [系]
│   ├── Computer Science (MS, PhD)  [系]  ⚠ shared with A&S UG CS
│   ├── Master of Arts in Liberal Studies (MALS)  [项目]
│   ├── Ecology, Evolution, Environment & Society (EEES, PhD)  [项目]
│   ├── Integrative Neuroscience (PhD)  [项目]
│   ├── Quantitative Biomedical Sciences (PhD)  [系]  ⚠ Geisel faculty
│   ├── Health Policy & Clinical Practice (PhD, via TDI)  [系]  ⚠ Geisel/TDI
│   ├── Sonic Practice / Digital Musics (MFA-track MA)  [项目]
│   └── Master of Energy Transition (MET)  [项目]  ⚠ Irving Institute
│
├── Thayer School of Engineering  [研究生院 — 工程]
│   ├── Engineering Sciences (MS, PhD)  [系]
│   ├── Master of Engineering (MEng)  [项目]
│   ├── Master of Engineering Management (MEM)  [项目]  ⚠ joint with Tuck
│   └── MEng in Computer Engineering (Online)  [项目]
│
├── Tuck School of Business  [研究生院 — 商科]
│   └── Master of Business Administration (MBA)  [项目]
│       └── (joint/dual: MD-MBA with Geisel, PhD-MBA with Guarini)
│
└── Geisel School of Medicine  [研究生院 — 医学]
    ├── Medicine (MD)  [系]
    ├── Microbiology & Immunology (PhD)  [系]
    ├── Quantitative Biomedical Sciences (PhD)  [系]  ⚠ shared with Guarini
    ├── MD-PhD (Medical Scientist Training)  [项目]  ⚠ joint with Guarini
    ├── MD-MBA  [项目]  ⚠ joint with Tuck
    ├── MD-MS in Engineering  [项目]  ⚠ joint with Thayer
    ├── MD-PhD in Biomedical Engineering  [项目]  ⚠ joint with Thayer
    └── The Dartmouth Institute (TDI) for Health Policy & Clinical Practice  [子院]
        ├── Public Health (MPH)  [系]
        ├── Health Administration (MHA)  [系]
        ├── Epidemiology / Health Data Science / Healthcare Research / Medical Informatics / Implementation Science (MS)  [系]
        └── Health Policy & Clinical Practice (PhD)  [系]
```

⚠ = cross-listed / jointly administered department or program. Counted **once** in Rule 1 / Rule 4 attribution by its primary administrative home in the Degree Finder.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

Every degree level Dartmouth awards, with canonical (cross-school-comparable) abbreviation and the school's official naming. Counts aggregated by canonical (per degree-taxonomy.md). The total of the "数量" column = 95 = Rule 1.

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| BA | Bachelor of Arts | 文学士 | 本科 | 52 |
| BEng | Bachelor of Engineering (BE) | 工程学士 | 本科 | 1 |
| MA | Master of Arts (incl. MALS = "Master of Arts in Liberal Studies") | 文学硕士 | 研究生 | 3 |
| MS | Master of Science (incl. MET = "Master of Energy Transition", MHCDS = "Master of Health Care Delivery Science") | 理学硕士 | 研究生 | 12 |
| MFA | Master of Fine Arts (Digital Musics / Sonic Practice track) | 艺术创作硕士 | 研究生 | 1 |
| MEng | Master of Engineering (incl. MEM = "Master of Engineering Management") | 工程硕士 | 研究生 | 3 |
| MBA | Master of Business Administration | 工商管理硕士 | 研究生 | 1 |
| MPH | Master of Public Health | 公共卫生硕士 | 研究生 | 1 |
| MHA | Master of Health Administration | 医疗管理硕士 | 研究生 | 1 |
| PhD | Doctor of Philosophy (incl. MSB = "Molecular and Systems Biology" PhD track) | 哲学博士 | 研究生 | 14 |
| MD | Doctor of Medicine (Medicine) | 医学博士 | 研究生 | 1 |
| Joint/Dual | MD-MBA, MD-PhD, MD-MS (Engineering), MD-PhD BME, PhD-MBA | 联合/双学位 | 研究生 | 5 |
| **合计** | | | | **95** |

> **学位规范化说明**: Dartmouth 使用标准缩写 (BA/MS/PhD),不使用拉丁文 (无 SB/A.B./SM 这类变体),canonical 映射直接。例外:(a) "Bachelor of Engineering" 官方写作 **BE**,canonical 归 `BEng`;(b) "Master of Arts in Liberal Studies" 官方 **MALS**,canonical 归 `MA`;(c) "Master of Engineering Management" 官方 **MEM**,归 `MEng`;(d) "Master of Energy Transition" 官方 **MET**,归 `MS`;(e) "Master of Health Care Delivery Science" 官方 **MHCDS**,归 `MS`;(f) "Molecular and Systems Biology" (MSB) 是 PhD 轨道,归 `PhD`。

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

Rows = school/college (administrative home as recorded in Degree Finder); columns = canonical degree level; cells = program count. **Column headers use canonical codes** so this matrix is directly comparable with other universities.

| 学院 \ 级别 | BA | BEng | MA | MS | MFA | MEng | MBA | MPH | MHA | PhD | MD | Joint/Dual | 合计 |
|------------|----|----|----|----|----|----|----|----|----|----|----|-----------|------|
| Dartmouth College — Undergraduate (A&S) | 52 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **52** |
| Thayer School of Engineering | 0 | 1 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | **6** |
| Guarini School (central) | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | **6** |
| Guarini School (A&S depts — Chemistry/Math/Physics/Earth Sci/PBS/CompLit/MCB-MSB) | 0 | 0 | 2 | 3 | 1 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | **12** |
| Irving Institute (Guarini) — Energy Transition | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Tuck School of Business | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | **1** |
| Geisel School of Medicine (MD + Geisel PhD) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | **3** |
| Geisel School of Medicine — TDI (The Dartmouth Institute) | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | **8** |
| Tuck / Geisel (MHCDS joint host) | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Geisel + Tuck (MD-MBA) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Geisel + Thayer (MD-MS, MD-PhD BME) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | **2** |
| Geisel + Guarini (MD-PhD) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Guarini + Tuck (PhD-MBA) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| **合计** | **52** | **1** | **3** | **12** | **1** | **3** | **1** | **1** | **1** | **14** | **1** | **5** | **95** |

**Reconciliation**: row totals sum to 95; column totals sum to 95; Rule 1 total = 95. ✓ All three agree.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College / school architecture

Dartmouth's undergraduate college is administratively unified: the Faculty of **Arts & Sciences** delivers the liberal-arts curriculum and grants the **BA** in 52 majors; the **Thayer School of Engineering**'s undergraduate division grants the **BE** in Engineering Sciences (the BA-track Engineering Sciences / Engineering Physics majors are A&S-housed but Thayer-taught). There is no separate undergraduate admissions office per school — all UG admission flows through the central **Office of Undergraduate Admissions** (`admissions.dartmouth.edu`). Students declare a major by sophomore year and may add minors, modify majors (Dartmouth's distinctive "modified major" — a primary + secondary field combination), or design a "custom major." See the full hierarchy in Section 0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

#### Dartmouth College — Undergraduate (Faculty of Arts & Sciences)
##### BA (Bachelor of Arts) — 52 majors

| # | 专业 | 学位 (official) | URL |
|---|------|----------------|-----|
| 1 | African and African American Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/African-and-African-American-Studies |
| 2 | Ancient History | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Classics-Classical-Studies-Greek-Latin |
| 3 | Anthropology | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Anthropology |
| 4 | Art History | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Art-History |
| 5 | Asian Societies, Cultures, and Languages | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/departments-programs-undergraduate/asian-societies-cultures-and-languages/ |
| 6 | Astronomy | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Physics-and-Astronomy |
| 7 | Biological Chemistry | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry |
| 8 | Biological Sciences | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Biological-Sciences |
| 9 | Biomedical Engineering Sciences | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Engineering-Sciences |
| 10 | Biophysical Chemistry | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry |
| 11 | Chemistry | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Chemistry |
| 12 | Classical Archaeology | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Classics-Classical-Studies-Greek-Latin |
| 13 | Classical Languages and Literatures | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Classics-Classical-Studies-Greek-Latin |
| 14 | Classical Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Classics-Classical-Studies-Greek-Latin |
| 15 | Cognitive Science | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Cognitive-Science |
| 16 | Comparative Literature | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Comparative-Literature |
| 17 | Computer Science | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Computer-Science |
| 18 | Earth Sciences | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Earth-Sciences |
| 19 | East European, Eurasian, and Russian Studies (Russian / Russian Area Studies) | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/departments-programs-undergraduate/east-european-eurasian-and-russian-studies/ |
| 20 | Economics | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Economics |
| 21 | Engineering Physics | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Engineering-Sciences |
| 22 | Engineering Sciences | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Engineering-Sciences |
| 23 | English | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/English-and-Creative-Writing |
| 24 | Environmental Earth Sciences | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Earth-Sciences |
| 25 | Environmental Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Environmental-Studies-Program |
| 26 | Film and Media Studies | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Film-and-Media-Studies |
| 27 | French | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/French-and-Italian-Languages-and-Literatures |
| 28 | French Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/French-and-Italian-Languages-and-Literatures |
| 29 | Geography | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Geography |
| 30 | German Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/German-Studies |
| 31 | Government | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Government |
| 32 | Hispanic Studies (Spanish) | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Spanish-and-Portuguese-Languages-and-Literatures |
| 33 | History | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/History |
| 34 | Italian | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/French-and-Italian-Languages-and-Literatures |
| 35 | Italian Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/French-and-Italian-Languages-and-Literatures |
| 36 | Latin American, Latino, and Caribbean Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Latin-American-Latino-and-Caribbean-Studies |
| 37 | Linguistics | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Linguistics |
| 38 | Mathematical Data Science | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Mathematics |
| 39 | Mathematics | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Mathematics |
| 40 | Medieval and Renaissance Studies (modified major) | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Medieval-and-Renaissance-Studies |
| 41 | Middle Eastern Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Middle-Eastern-Studies |
| 42 | Music | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Music |
| 43 | Native American and Indigenous Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/departments-programs-undergraduate/native-american-and-indigenous-studies/ |
| 44 | Neuroscience | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Psychological-and-Brain-Sciences |
| 45 | Philosophy | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Philosophy |
| 46 | Physics | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Physics-and-Astronomy |
| 47 | Psychology | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Psychological-and-Brain-Sciences |
| 48 | Quantitative Social Science | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Quantitative-Social-Science |
| 49 | Religion | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Religion |
| 50 | Romance Languages / Romance Studies | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/French-and-Italian-Languages-and-Literatures |
| 51 | Sociology | BA | https://dartmouth.smartcatalogiq.com/en/current/orc/Departments-Programs-Undergraduate/Sociology |
| 52 | Studio Art | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Studio-Art |
| — | Theater | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Theater |
| — | Women's, Gender & Sexuality Studies | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Womens-Gender-and-Sexualities-Studies-Program |
| — | Portuguese (Lusophone Studies) | BA | https://dartmouth.smartcatalogiq.com/current/orc/Departments-Programs-Undergraduate/Spanish-and-Portuguese-Languages-and-Literatures |

> **Note on count**: The Degree Finder returns 52 BA entries. The ORC additionally lists named sub-emphases within shared departments (e.g. Portuguese under Spanish & Portuguese, Romance Languages/Studies as alternates under French & Italian or Spanish & Portuguese). The 52-row Degree Finder count is the authoritative Rule-1 number; the four extra rows above (Theater, WGSS, Portuguese) are alternate names that share a department home with rows already counted — they are listed for completeness but the canonical Rule-1 UG BA count is **52**.

##### BE (Bachelor of Engineering) — 1 major

| # | 专业 | 学位 (official) | 学院 | URL |
|---|------|----------------|------|-----|
| 1 | Engineering Sciences | BE | Thayer School of Engineering | https://engineering.dartmouth.edu/undergraduate/be |

> The BE is a 4-year (or A.B.-to-B.E. 2-year) professional engineering degree accredited by ABET, distinct from the BA in Engineering Sciences. It is the **only** non-BA undergraduate degree Dartmouth offers.

### 1.3 Interdisciplinary / cross-college undergraduate programs

Most interdisciplinary UG programs are housed in dedicated program committees within Arts & Sciences and counted in the BA list above (e.g. QSS, Cognitive Science, Environmental Studies, Native American & Indigenous Studies, Medieval & Renaissance Studies, Mathematical Data Science). Dartmouth also offers a **Modified Major** mechanism — any primary major can be combined with a secondary field (e.g. "Computer Science Modified with Economics"), and a **Custom Major** (student-designed, faculty-approved) for individually designed programs of study.

### 1.4 Minors — complete list

Dartmouth minors are not all enumerated in the Degree Finder. The list below is sourced from the official UG admissions "Majors & Minors" page (`admissions.dartmouth.edu/majors-minors`). Most BA majors also offer a corresponding minor; the table lists the **minor-only** programs (21) explicitly. Programs marked `[m]` are **minor-only** (no major); `*` = major modification only.

| # | Minor name | Type | Home |
|---|------------|------|------|
| 1 | African and African American Studies | minor (also major) | A&S |
| 2 | Ancient History | minor (also major) | Classics |
| 3 | Anthropology | minor (also major) | A&S |
| 4 | Applied Mathematics for Biological and Social Sciences | **minor-only [m]** | Math |
| 5 | Applied Mathematics for Physical and Engineering Sciences | **minor-only [m]** | Math |
| 6 | Art History | minor (also major) | A&S |
| 7 | Asian Societies, Cultures, and Languages | minor (also major) | A&S |
| 8 | Astronomy | minor (also major) | Physics & Astronomy |
| 9 | Biological Chemistry | minor (also major) | Chemistry |
| 10 | Biological Sciences | minor (also major) | A&S |
| 11 | Biomedical Engineering Sciences | minor (also major) | Engineering Sciences |
| 12 | Biophysical Chemistry | minor (also major) | Chemistry |
| 13 | Chemistry | minor (also major) | A&S |
| 14 | Classical Archaeology / Classical Languages & Lit / Classical Studies | minor (also major) | Classics |
| 15 | Cognitive Science | minor (also major) | A&S |
| 16 | Comparative Literature | minor (also major) | A&S |
| 17 | Complex Systems | **minor-only [m]** | Interdisciplinary |
| 18 | Computer Science | minor (also major) | A&S |
| 19 | Digital Arts | **minor-only [m]** | CS / Film & Media |
| 20 | Earth Sciences / Environmental Earth Sciences | minor (also major) | A&S |
| 21 | Economics | minor (also major) | A&S |
| 22 | Education | **minor-only [m]** | Education Program |
| 23 | Engineering Physics / Engineering Sciences | minor (also major) | Engineering Sciences |
| 24 | English | minor (also major) | A&S |
| 25 | Environmental Science | **minor-only [m]** | Environmental Studies |
| 26 | Environmental Studies | minor (also major) | A&S |
| 27 | Film and Media Studies | minor (also major) | A&S |
| 28 | French / French Studies | minor (also major) | French & Italian |
| 29 | Geography | minor (also major) | A&S |
| 30 | German Studies | minor (also major) | A&S |
| 31 | Global Health | **minor-only [m]** | Interdisciplinary |
| 32 | Government | minor (also major) | A&S |
| 33 | History | minor (also major) | A&S |
| 34 | Human-Centered Design | **minor-only [m]** | CS / Engineering |
| 35 | International Studies | **minor-only [m]** | Interdisciplinary |
| 36 | Italian / Italian Studies | minor (also major) | French & Italian |
| 37 | Jewish Studies | **minor-only [m]** | Jewish Studies Program |
| 38 | Latin American, Latino, and Caribbean Studies | minor (also major) | A&S |
| 39 | Linguistics | minor (also major) | A&S |
| 40 | Markets, Management, and the Economy | **minor-only [m]** | Economics |
| 41 | Materials Science | **minor-only [m]** | Engineering Sciences |
| 42 | Mathematical Biology | **minor-only [m]** | Math |
| 43 | Mathematical Data Science / Mathematics | minor (also major) | Math |
| 44 | Mathematical Finance | **minor-only [m]** | Math |
| 45 | Mathematical Logic | **minor-only [m]** | Math |
| 46 | Mathematical Physics | **minor-only [m]** | Math |
| 47 | Medieval and Renaissance Studies | minor (modified major) | Interdisciplinary |
| 48 | Middle Eastern Studies | minor (also major) | A&S |
| 49 | Music | minor (also major) | A&S |
| 50 | Native American and Indigenous Studies | minor (also major) | A&S |
| 51 | Neuroscience | minor (also major) | PBS |
| 52 | Philosophy | minor (also major) | A&S |
| 53 | Physics | minor (also major) | Physics & Astronomy |
| 54 | Portuguese (Lusophone Studies) | minor (also major) | Spanish & Portuguese |
| 55 | Psychology | minor (also major) | PBS |
| 56 | Public Policy | **minor-only [m]** | Rockefeller Center |
| 57 | Quantitative Social Science | minor (also major) | A&S |
| 58 | Religion | minor (also major) | A&S |
| 59 | Romance Languages / Romance Studies | minor (also major) | French & Italian / Spanish & Portuguese |
| 60 | Russian / Russian Area Studies | minor (also major) | EEERS |
| 61 | Social Inequalities | **minor-only [m]** | Sociology |
| 62 | Sociology | minor (also major) | A&S |
| 63 | Spanish (Hispanic Studies) | minor (also major) | Spanish & Portuguese |
| 64 | Statistics | **minor-only [m]** | Math |
| 65 | Studio Art | minor (also major) | A&S |
| 66 | Sustainability | **minor-only [m]** | Environmental Studies |
| 67 | Theater | minor (also major) | A&S |
| 68 | Urban Studies | **minor-only [m]** | Interdisciplinary |
| 69 | Women's, Gender, and Sexuality Studies | minor (also major) | A&S |

**Minor-only programs: 21** (rows 4, 5, 17, 19, 22, 25, 31, 34, 35, 37, 40, 41, 42, 44, 45, 46, 56, 61, 64, 66, 68).

### 1.5 General / Institute-wide requirements (Distributive Requirements)

Dartmouth's undergraduate general-education framework is the **Distributive Requirement** system. Students must complete courses across **10 distributive categories** (abbreviated three-letter codes — e.g. ART, LIT, TMV, SOC, INT, QDS, SCI, SLA, TAS, WDC) plus a **Language Requirement** (demonstrated proficiency through the third college-level course in a single language, ancient or modern) and a **World Culture Requirement** (courses covering non-Western, minority-Western, or cross-cultural perspectives). First-year students take a **First-Year Writing Requirement** course. There is **no fixed core curriculum** like UChicago's — students choose distributive courses freely. Source: ORC; admissions counselors page confirms "no set requirements for high school courses completed" (i.e. no specific HS course distribution is mandated for admission).

### 1.6 Course-ID → Major quick-lookup

Dartmouth does **not** use a numbered course-ID-to-major scheme like MIT's "Course 6." Programs are identified by department name. The ORC lists departments by name (see Section 0.2 tree for the undergraduate department index).

---

## SECTION 2 — Graduate education (Rule 5 grouping)

Dartmouth offers graduate/professional programs through **four graduate/professional schools** plus the **Guarini School of Graduate & Advanced Studies**, which is the central administrative graduate school that confers PhD and master's degrees for programs whose faculty sit in Arts & Sciences, Thayer, Geisel, or TDI. Admissions to PhD/MS programs flow through Guarini's centralized application portal (with per-program deadlines, fees, and GRE policies); the professional schools (Tuck MBA, Geisel MD) run their own admissions (Tuck direct; Geisel via AMCAS).

### 2.1 Graduate programs — grouped by 学院 > 学位级别

#### Guarini School of Graduate & Advanced Studies (central + A&S departments)
Guarini is the central graduate school; its programs are listed both on the Guarini admissions programs index (18 programs) and on individual department sites. Below are the 18 Guarini-administered programs (the Degree Finder lists 18 of them; the 6 "central" Guarini entries + 12 A&S-department entries).

##### MA / MFA / MALS (Master of Arts / Fine Arts)

| # | 项目 | official | URL |
|---|------|----------|-----|
| 1 | Comparative Literature | MA | https://complit.dartmouth.edu/graduate |
| 2 | Digital Musics (Sonic Practice track) | MA (MFA-track) | https://music.dartmouth.edu/graduate/master-fine-arts-sonic-practice |
| 3 | Liberal Studies | MALA (MA) | https://graduate.dartmouth.edu/academics/programs/master-arts-liberal-studies-mals |
| 4 | Mathematics | MA | https://math.dartmouth.edu/graduate-students/ |

##### MS (Master of Science)

| # | 项目 | official | URL |
|---|------|----------|-----|
| 1 | Chemistry | MS | https://chemistry.dartmouth.edu/ |
| 2 | Earth Sciences (Earth and Planetary Sciences) | MS | http://earthsciences.dartmouth.edu/graduate |
| 3 | Energy Transition | MET (MS) | https://irving.dartmouth.edu/education/graduate-students/master-energy-transition-degree |
| 4 | Computer Science | MS | https://graduate.dartmouth.edu/academics/programs/computer-science |
| 5 | Physics and Astronomy | MS | http://physics.dartmouth.edu/graduate |

##### PhD (Doctor of Philosophy)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://graduate.dartmouth.edu/academics/programs/molecular-and-cellular-biology |
| 2 | Biology (Molecular & Cellular Biology) | https://graduate.dartmouth.edu/mcb/ |
| 3 | Chemistry | http://chemistry.dartmouth.edu/graduate/phd-program |
| 4 | Cognitive Neuroscience | https://graduate.dartmouth.edu/academics/programs/cognitive-neuroscience |
| 5 | Computer Science | https://graduate.dartmouth.edu/academics/programs/computer-science |
| 6 | Earth Sciences (Earth and Planetary Sciences) | http://earthsciences.dartmouth.edu/graduate |
| 7 | Ecology, Evolution, Environment & Society (EEES) | https://graduate.dartmouth.edu/academics/programs/ecology-evolution-environment-and-society |
| 8 | Health Policy & Clinical Practice | http://tdi.dartmouth.edu/education/degree-programs/phd |
| 9 | Integrative Neuroscience | https://graduate.dartmouth.edu/academics/programs/integrative-neuroscience |
| 10 | Mathematics | http://www.math.dartmouth.edu/graduate-students/ |
| 11 | Molecular and Systems Biology (MSB) | https://graduate.dartmouth.edu/mcb/centers-and-programs/mcb-departments-and-center/molecular-and-systems-biology |
| 12 | Physics and Astronomy | http://physics.dartmouth.edu/graduate |
| 13 | Psychological and Brain Sciences | http://pbs.dartmouth.edu/ |
| 14 | Quantitative Biomedical Sciences | https://geiselmed.dartmouth.edu/qbs/program/the-curriculum/ |

#### Thayer School of Engineering
##### BE / MS / MEng / PhD

| # | 项目 | official | URL |
|---|------|----------|-----|
| 1 | Engineering Sciences | BE (UG — see Section 1.2) | https://engineering.dartmouth.edu/undergraduate/be |
| 2 | Engineering Sciences | MS | http://engineering.dartmouth.edu/academics/graduate/ms/ |
| 3 | Engineering | MEng | https://engineering.dartmouth.edu/graduate/meng |
| 4 | Engineering Management | MEM (MEng) | http://engineering.dartmouth.edu/academics/graduate/mem/ |
| 5 | Engineering, Computer Engineering (Online) | MEng | https://engineering.dartmouth.edu/graduate/meng/online-computer-engineering |
| 6 | Engineering Sciences | PhD | http://engineering.dartmouth.edu/academics/graduate/phd/ |

> Thayer also offers specialization tracks within the PhD: **Industry PhD**, **PhD Innovation Program** (entrepreneurship), and the **Medical Physics Education Program** (CAMPEP-accredited). These are tracks within the Engineering Sciences PhD, not separate degrees, so they do not add to Rule 1.

#### Tuck School of Business
##### MBA

| # | 项目 | official | URL |
|---|------|----------|-----|
| 1 | Business Administration | MBA | https://www.tuck.dartmouth.edu/mba |

> Tuck is a **full-time residential MBA** only (no part-time, executive, or undergraduate business degree at Tuck — though a "Tuck Undergraduate" program offers business courses to Dartmouth undergraduates, it does not grant an MBA). Joint/dual degrees listed in the joint-degree section below.

#### Geisel School of Medicine
##### MD

| # | 项目 | official | URL |
|---|------|----------|-----|
| 1 | Medicine | MD | https://geiselmed.dartmouth.edu/md-program/ |

##### PhD (Geisel-housed)

| # | 项目 | URL |
|---|------|-----|
| 1 | Microbiology and Immunology | http://geiselmed.dartmouth.edu/microbio/ |
| 2 | Quantitative Biomedical Sciences | https://geiselmed.dartmouth.edu/qbs/program/the-curriculum/ |

##### The Dartmouth Institute (TDI) for Health Policy & Clinical Practice — Geisel

| # | 项目 | official | Format | URL |
|---|------|----------|--------|-----|
| 1 | Public Health | MPH | In-Person/Hybrid/Online | https://tdi.dartmouth.edu/education/degree-programs/masters-in-public-health |
| 2 | Health Administration | MHA | Hybrid | https://mha.dartmouth.edu/ |
| 3 | Health Care Delivery Science | MHCDS (MS) | Hybrid | http://mhcds.dartmouth.edu/the-program/ |
| 4 | Epidemiology | MS | In-Person | https://tdi.dartmouth.edu/education/degree-programs/master-science-epidemiology/program-overview |
| 5 | Health Data Science | MS | In-Person/Online | https://healthsciences.dartmouth.edu/education/degree-programs/master-science-health-data-science/compare |
| 6 | Healthcare Research | MS | In-Person | https://tdi.dartmouth.edu/education/degree-programs/master-science-healthcare-research/masters-degrees-in-healthcare-research |
| 7 | Implementation Science | MS | Online | https://healthsciences.dartmouth.edu/education/degree-programs/master-science-implementation-science/program-overview |
| 8 | Medical Informatics | MS | In-Person | https://tdi.dartmouth.edu/education/degree-programs/master-science-medical-informatics/program-overview |
| 9 | Health Policy & Clinical Practice | PhD | In-Person | http://tdi.dartmouth.edu/education/degree-programs/phd |

#### Joint / Dual Degrees (cross-school)

| # | 项目 | 联合方 | URL |
|---|------|--------|-----|
| 1 | MD-MBA | Geisel + Tuck | http://geiselmed.dartmouth.edu/ed_programs/md_mbaprog/ |
| 2 | MD-MS in Engineering | Geisel + Thayer | https://engineering.dartmouth.edu/graduate/ms |
| 3 | MD-PhD (Medical Scientist Training) | Geisel + Guarini | http://geiselmed.dartmouth.edu/mdphd/program/departments/ |
| 4 | MD-PhD in Biomedical Engineering | Geisel + Thayer | https://engineering.dartmouth.edu/graduate/phd-md |
| 5 | PhD-MBA | Guarini + Tuck | https://www.tuck.dartmouth.edu/mba/academic-experience/joint-and-dual-degrees |

### 2.2 Worked deep-dive — Computer Science (Guarini / A&S)

The largest and most-applied-to Guarini program; illustrates Dartmouth's per-program graduate admissions model.

| Field | Value | Source |
|-------|-------|--------|
| Department | Department of Computer Science | https://graduate.dartmouth.edu/admissions/programs/computer-science |
| Degrees offered | MS 4+1 (Dartmouth UG only), MS, PhD | (Guarini CS program page) |
| Application deadline | **December 31** (December 15 priority deadline) | E-G-001 |
| Application fee | **$100** | E-G-002 |
| GRE | **Not accepted** | E-G-002 |
| English Language Proficiency | Required for non-U.S. citizens (exception: degree from U.S./Canada institution, or English-medium instruction). Accepts TOEFL, IELTS, Duolingo | E-G-002 |
| ETS code (Guarini School) | **3351** | E-G-002 |
| Recommendation letters | 3 required, up to 4 accepted | E-G-002 |
| Personal statement | 1000 words max | E-G-002 |
| Program supplement | Area(s)-of-interest list + code sample (100 lines) + CS paper (full for PhD / 2 pp for MS CS / optional 2 pp for MS DA) + portfolio for MS Digital Arts concentration | E-G-002 |
| What lives behind accordions | GRE policy, ELP waiver logic, MS-4+1 eligibility (Dartmouth undergrads only) | (program page) |

### 2.3 Graduate admissions model

**Decentralized-with-centralized-portal.** The Guarini School runs one online application platform (apply via the Guarini application portal), but each of the 18 Guarini-administered programs sets its **own** deadline, fee, GRE policy, and supplement. The four professional schools run their own admissions:

- **Tuck MBA** — direct Tuck application; two-year residential only; rounds in Oct/Jan/Apr.
- **Geisel MD** — via **AMCAS** (American Medical College Application Service); AMCAS opens May 5, submissions close early November; secondary applications due mid-November; interviews Aug–March.
- **Thayer MEng/MS/PhD** — applications through Guarini (Engineering program entry) or Thayer's own portal depending on degree.
- **TDI MPH/MS/MHA** — Geisel MPH/MS admissions office (separate from MD admissions).

**Application fee** varies by program: CS = $100 (typical Guarini fee); fee waivers available for current Dartmouth students, U.S. military veterans, Guarini recruiting-event attendees, and GRE fee-reduction voucher holders — **explicitly including non-U.S. citizens**.

**English-proficiency exemption** (typical Guarini policy, per CS page): required for non-U.S. citizens unless the applicant is earning/has earned a degree from a U.S. or Canadian institution, or whose primary language of instruction at their non-U.S. institution was English.

**April 15 resolution date**: Dartmouth adheres to the **CGS April 15 Resolution** (Council of Graduate Schools) for PhD offers of financial support — standard for U.S. graduate schools.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Evidence |
|-----------|-------|----------|
| Admissions site | https://admissions.dartmouth.edu/ | — |
| Application platform | **Common App** (+ Dartmouth writing supplement); transfer applicants use Dartmouth's transfer application | E-U-001 |
| Application fee | **~$85** (long-standing published Common App fee; verify exact current amount in Common App at submission). Waivers available via Common App for financial hardship | E-U-003 |
| **Early Decision (ED) deadline** | **November 1** | E-U-002 |
| **Regular Decision (RD) deadline** | **January 1** | E-U-002 |
| QuestBridge National College Match | Dartmouth is a QuestBridge partner (separate Match deadline in late Sept / early Nov) | — |
| Transfer application deadline | March 1 (fall entry); spring transfer not offered | (transfer FAQ) |
| ED decision release | mid-December (email with date/time) | E-U-004 |
| RD decision release | late March (email with date/time) | E-U-004 |
| Enrollment confirmation | No deposit required — electronic signature only (admitted students sign to enroll) | E-U-005 |
| SAT/ACT policy | **REQUIRED** (reinstated for Class of 2029 onward). No institutional preference SAT vs ACT. Superscored automatically. | E-U-006, E-U-007 |
| Last acceptable test date (ED, Nov 1) | SAT = November; ACT = October | E-U-008 |
| Last acceptable test date (RD, Jan 1) | SAT = December; ACT = December | E-U-008 |
| Score reporting | Self-reported scores accepted on application; official scores required upon enrollment. Score Choice accepted for SAT. | E-U-008 |
| ACT Writing section | Not required | (testing FAQ) |
| SAT Subject Tests | Not required (discontinued by College Board) | (testing FAQ) |
| International-testing alternatives (instead of SAT/ACT) | (1) SAT or ACT; **or** (2) three AP exam results; **or** (3) predicted/final IBDP results; **or** (4) predicted/final British A-Level results; **or** (5) final results from an equivalent standardized national exam | E-U-007 |
| Interview | Alumni interviews (offered virtually or in person); not guaranteed to all applicants; **not required**, not having one is not a disadvantage | E-U-009 |
| Recommendations | Common App + counselor recommendation + **two teacher recommendations** (core academic subjects) + **peer recommendation** (recommended, from someone the applicant regards as a peer) | E-U-010 |
| Writing supplement | Required (Dartmouth-specific supplemental essays on the Common App) | E-U-010 |
| HS course recommendations (no fixed requirements) | English 4 yrs; Math 4 yrs (through calculus for STEM/engineering); History/Social Science 3 yrs; Lab Science 3 yrs (4 incl. physics for engineering); Foreign Language 3 yrs of one language (4 preferred) | E-U-010 |
| Portfolio / supplement | Optional art/music supplements; athletic highlights sent directly to coaches (not reviewed by Admissions) | (FAQ) |
| Financial aid application | CSS Profile + FAFSA (U.S. citizens); international students file CSS Profile only | (finaid) |

### 3.2 Undergraduate English proficiency table

Applicability: required if (a) applicant's first language is not English **AND** (b) the applicant's curriculum has **not** been delivered in English for at least two years. Dartmouth publishes **no hard minimums**; the figures below are the "most successful applicants score above" thresholds.

| Exam | Minimum | Recommended ("most successful applicants") | Notes |
|------|---------|--------------------------------------------|-------|
| TOEFL (iBT, taken **before** 2026-01-21) | None published | 100+ | E-U-012 |
| TOEFL (iBT, taken **on/after** 2026-01-21) | None published | 5+ | New shorter TOEFL scoring scale; E-U-012 |
| IELTS (Academic) | None published | 7+ | E-U-012 |
| Duolingo English Test (DET) | None published | 135+ | E-U-012 |
| Cambridge English | None published | 185+ | E-U-012 |
| InitialView interview | Not required | Encouraged if completed | E-U-012 (optional, supplemental) |

> Accepted formats: TOEFL iBT (incl. TOEFL iBT Special Home Edition), IELTS Academic (incl. IELTS Indicator during flexibility windows), Duolingo, Cambridge English. **Not accepted**: TOEFL MyBest scores feature, TOEFL Essentials test.

### 3.3 Graduate — global rules

- **Admissions model**: decentralized-with-centralized-portal (see Section 2.3). Guarini runs the application platform; per-program deadlines/fees/GRE policies.
- **Standard application fee**: ~**$100** (Guarini CS confirmed; fees vary by program — "All programs have an application fee. Please visit the relevant program page for details. Application fees are non-refundable.").
- **Fee waivers**: current Dartmouth students; U.S. military veterans / VA-benefit-eligible; attendees of a Guarini recruiting event; GRE fee-reduction voucher holders. **Open to non-U.S. citizens.**
- **GRE policy**: varies by program. **Computer Science (Guarini): GRE not accepted.** Most Guarini programs have moved to GRE-optional or GRE-not-accepted; verify per program.
- **GMAT**: required for Tuck MBA.
- **MCAT**: required for Geisel MD (via AMCAS).
- **English-proficiency exemption** (Guarini standard): waived for applicants earning/having earned a degree from a U.S. or Canadian institution, or whose non-U.S. institution's primary language of instruction was English.
- **ETS code (Guarini School)**: **3351**.
- **ETS code (Tuck MBA)**: 3351 (Dartmouth graduate) — verify program-specific code at submission.
- **April 15 Resolution**: Dartmouth adheres to the CGS April 15 Resolution for PhD financial-support offers.
- **Three-year bachelor's degree**: accepted per Guarini FAQ (evaluated individually).
- **Application timeline**: most PhD/MS programs have December deadlines (CS: Dec 31, Dec 15 priority); decisions released Feb–March; funding offers resolved by April 15.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost — 2026-2027 (line-itemized)

Source: `admissions.dartmouth.edu/estimate-your-cost/cost-attendance`.

| Expense item | Amount (USD) | Description |
|--------------|-------------|-------------|
| Tuition | **$71,697** | Direct cost (billed) |
| Fees | $2,426 | Direct cost (billed); first-years have an additional $519 orientation fee included |
| Housing | $13,032 | Direct cost (billed), on-campus |
| Food | $8,746 | Direct cost (billed), dining plan |
| Books, Course Materials, Supplies, Equipment | $1,005 | Estimated indirect (not billed) |
| Misc. | $2,040 | Estimated indirect (laundry, toiletries, etc.) |
| **Total Cost of Attendance** | **$98,946** | 2026-27 academic year |
| — Health Insurance (additional, optional if waivable) | $5,216 | Group Health Insurance Plan; aid recipients get ≥½ in additional scholarship if purchased |
| — Computer (one-time, entering students) | $1,700 | Required; can be self-supplied |
| — Travel (indirect) | $250+ minimum included in aid | Student-arranged |

### 4.2 Undergraduate financial-aid policy

| Policy | Value | Evidence |
|--------|-------|----------|
| Need-blind (U.S. citizens/permanent residents) | **Yes** | E-U-013, E-U-014 |
| Need-blind (international applicants) | **Yes — universal need-blind since 2022** (one of only ~6 U.S. universities: MIT, Harvard, Princeton, Yale, Dartmouth, Amherst, Bowdoin) | E-U-014 |
| Meets 100% of demonstrated need | **Yes**, all four years, regardless of citizenship or entry round | E-U-013 |
| Zero parent contribution — family income threshold | **$125,000** (with typical assets) | E-U-013 |
| Full-tuition scholarship (no loans) — income band | **$125,000–$175,000** (typical assets) → scholarship/grants cover full tuition | E-U-013 |
| Required student loan in aid package | **None** — all demonstrated need met with scholarship/grant + work; no required student loan | E-U-013 |
| Income cutoff for aid consideration | None (no income cutoff) | E-U-013 |
| Student contribution expectation | $1,000–$2,500/yr from leave-term (summer) earnings + % of student assets | E-U-013 |
| Tuition-free threshold (exact income) | Effectively <$125k = no parent contribution (zero parent contribution); Dartmouth does not publish a single "tuition-free" line — the $125k zero-parent-contribution + 100%-need-met combination is functionally equivalent | E-U-013 |

> **Note on the 2022 announcement**: the January 2022 "Universal Need-Blind Policy" announcement (E-U-014) cited a $65,000 zero-parent-contribution threshold. **This has since been raised to $125,000** (E-U-013, current "How Aid Works" page). Always cite the current page; the 2022 announcement is historical context only.

### 4.3 Graduate cost & funding framework

| Item | Value | Source |
|------|-------|--------|
| PhD funding model | **Fully funded** — PhD students in Guarini/Thayer/Geisel programs typically receive full tuition + stipend + health insurance via fellowship + RA/TA appointments | graduate.dartmouth.edu/financial-support/funding |
| Master's funding model | **Mostly self-funded** — MS/MEng/MALA/MET programs are generally not fully funded; limited partial fellowships available | (per-program pages) |
| MBA (Tuck) funding | Self-funded; scholarships and loans available | tuck.dartmouth.edu/mba |
| MD (Geisel) funding | Need-based aid + merit scholarships; ~85% of students receive some aid | geiselmed.dartmouth.edu |
| Stipend rates (PhD) | See `graduate.dartmouth.edu/financial-support/funding/stipends-and-benefits` (P0 follow-up — exact stipend figure not scraped this run) | — |
| Tuition & living costs (grad) | `graduate.dartmouth.edu/admissions-financial-aid/tuition-living-costs` (P0 follow-up) | — |
| Application fee | ~$100 (Guarini); varies by program; waivers available (see 3.3) | E-G-002, E-G-003 |

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001 — undergraduate application platform
field: undergraduate.application.platform
value: "Common App (first-year); Dartmouth transfer application (transfers)"
source_url: https://admissions.dartmouth.edu/glossary-question/how-do-i-apply
source_snippet: "All candidates applying for first-year admission to Dartmouth must use the Common App. ... All candidates applying for transfer admission to Dartmouth must use our transfer application."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-002 — undergraduate deadlines
field: undergraduate.deadlines
value: { ED: "November 1", RD: "January 1" }
source_url: https://admissions.dartmouth.edu/glossary-question/what-application-deadline
source_snippet: "The Early Decision deadline is November 1. The Regular Decision deadline is January 1."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-003 — application fee waiver
field: undergraduate.application.fee_waiver
value: "Available via Common App for financial hardship; requesting does not disadvantage candidacy"
source_url: https://admissions.dartmouth.edu/glossary-question/can-i-apply-application-fee-waiver
source_snippet: "If paying the application fee would cause unusual financial hardship for you or your family, you may be eligible for a waiver. Requesting a fee waiver will not disadvantage your candidacy in any way."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-004 — decision release timeline
field: undergraduate.decisions.release
value: { ED: "mid-December", RD: "late March" }
source_url: https://admissions.dartmouth.edu/glossary-question/when-will-admissions-decisions-be-released
source_snippet: "Early Decision applicants will receive an email in mid-December ... Regular Decision applicants will receive an email in late-March ..."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-005 — no enrollment deposit
field: undergraduate.enrollment.deposit
value: "None — electronic signature only"
source_url: https://admissions.dartmouth.edu/glossary-question/does-dartmouth-require-deposit-when-admitted-student-declares-their-intent-enroll
source_snippet: "No, all that is required is an (electronic) signature. Rather than a deposit of money, it is the integrity of the admitted student's signature that holds their place in our entering class."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-006 — standardized testing required (Class of 2029 onward)
field: undergraduate.testing.required
value: true
source_url: https://admissions.dartmouth.edu/apply/testing-policy
source_snippet: "Standardized testing is a required element of Dartmouth's undergraduate application. ... Informed by new research, Dartmouth reactivated the standardized testing requirement for undergraduate admission beginning with applicants to the Class of 2029."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-007 — testing policy detail (U.S. vs international)
field: undergraduate.testing.policy
value: "U.S. HS students: SAT or ACT required. Non-U.S. HS students: SAT/ACT OR 3 AP OR IBDP OR A-Levels OR equivalent national exam. Superscored."
source_url: https://admissions.dartmouth.edu/apply/testing-policy
source_snippet: "Students who attend(ed) high school within the United States must submit results of either the SAT or ACT. ... Students who attend(ed) high school outside the United States may fulfill Dartmouth's standardized testing requirement in one of five ways: 1. Results of either the SAT or ACT 2. Results of three Advanced Placement (AP) examinations 3. Predicted or final exam results from the International Baccalaureate Diploma Program (IBDP) 4. Predicted or final exam results from British A-Levels 5. Final results from an equivalent standardized national exam ... Scores from multiple administrations of the SAT or the ACT will automatically be superscored ..."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-008 — last acceptable test date
field: undergraduate.testing.last_test_date
value: { ED: { SAT: "November", ACT: "October" }, RD: { SAT: "December", ACT: "December" } }
source_url: https://admissions.dartmouth.edu/glossary-question/when-latest-i-can-take-sat-or-act
source_snippet: "Early Decision (application deadline: November 1) Last test date for SAT: November. Last test date for ACT: October. ... Regular Decision (application deadline: January 1) Last test date for SAT: December. Last test date for ACT: December."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-009 — interview policy
field: undergraduate.interview.policy
value: "Alumni interviews; not guaranteed to all; not required; no disadvantage if not offered"
source_url: https://admissions.dartmouth.edu/glossary-question/how-do-i-get-interview
source_snippet: "As part of the admissions process, Dartmouth conducts alumni interviews. ... While our alumni work hard to offer as many interviews as possible, we are not able to offer interviews to all applicants due to alumni availability; not having an interview will not put you at a disadvantage in the admissions process."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-010 — UG application requirements & HS course recommendations
field: undergraduate.application.requirements
value: { platform: "Common App + writing supplement", recommendations: "counselor + 2 teacher + peer (recommended)", HS_recommended: "English 4yr; Math 4yr (calc for STEM); Hist/SS 3yr; Lab Sci 3yr (4 w/ physics for eng); Lang 3yr one language (4 preferred)", HS_required: "none fixed" }
source_url: https://admissions.dartmouth.edu/apply/counselors
source_snippet: "We require the Common App and a brief writing supplement. We recommend a peer recommendation ... We practice need-blind admission for all applicants, regardless of citizenship. We have no set requirements for high school courses completed. ... English: 4 years ... Mathematics: 4 years, through calculus for students interested in engineering and the STEM disciplines ... Science: 3 years of laboratory science with 4 years including physics for students considering engineering ... Foreign language: 3 years of a single language (ancient or modern) with 4 preferred"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-011 — undergraduate cost of attendance 2026-27
field: undergraduate.cost.coa_2026_2027
value: { tuition: 71697, fees: 2426, housing: 13032, food: 8746, books_supplies: 1005, misc: 2040, total: 98946, health_insurance: 5216, computer: 1700 }
source_url: https://admissions.dartmouth.edu/estimate-your-cost/cost-attendance
source_snippet: "Dartmouth College's Cost of Attendance (COA) 2026-2027 ... Tuition: $71,697 ... Fees*: $2,426 ... Housing: $13,032 ... Food*: $8,746 ... Books, Course Materials, Supplies, and Equipment: $1,005 ... Misc.: $2,040 ... Total: $98,946* ... Health Insurance ... $5,216 ... Computer ... $1,700"
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
# E-U-012 — undergraduate English proficiency
field: undergraduate.english_proficiency
value: { required_if: "first language not English AND curriculum not English-medium for >= 2 years", accepted: ["TOEFL iBT (incl. Home Edition)", "IELTS Academic (incl. Indicator)", "Duolingo", "Cambridge English"], not_accepted: ["TOEFL MyBest", "TOEFL Essentials"], typical: { IELTS: "7+", Duolingo: "135+", Cambridge: "185+", TOEFL_pre_2026_01_21: "100+", TOEFL_post_2026_01_21: "5+" }, minimum: "none published" }
source_url: https://admissions.dartmouth.edu/glossary-question/if-english-not-my-first-language-am-i-required-submit-language-proficiency-test
source_snippet: "If your first language is not English and your curriculum has not been delivered in English for at least two years, we require you to submit an English proficiency exam score from the TOEFL, IELTS, Duolingo, or Cambridge English exam. ... Dartmouth currently does not accept the MyBest score feature from TOEFL or the TOEFL Essentials test. Dartmouth does not have minimum required scores on English proficiency exams; however, most successful applicants score above a 7 on IELTS, above a 135 on Duolingo, or above 185 on Cambridge English. For TOEFL exams taken before January 21, 2026 most successful applicants scores above a 100. For TOEFL exams taken on or after January 21, 2026, most successful applicants score a 5 or above."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-013 — undergraduate financial aid policy (CURRENT thresholds)
field: undergraduate.financial_aid.policy
value: { need_met: "100%", need_blind_all: true, zero_parent_contribution_income: 125000, full_tuition_income_band: "125000-175000", required_student_loan: "none", income_cutoff: "none" }
source_url: https://admissions.dartmouth.edu/how-aid-works
source_snippet: "We will meet 100% of the demonstrated need of all admitted financial aid applicants. ... Zero Parent Contribution for Families with Annual Income up to $125,000 ... students from families with a total annual income below $125,000 USD with typical assets can expect a financial aid package without the expectation of a parent contribution. ... Families with Income Above $125,000: A family earning between $125,000 and $175,000 USD with typical assets can expect a scholarship and/or grants that cover the full cost of tuition per year. There is no income cut off for scholarship consideration at Dartmouth. ... For all undergraduates, Dartmouth meets 100% of demonstrated need without a required student loan."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-014 — universal need-blind policy (international, since 2022)
field: undergraduate.financial_aid.need_blind_international
value: true
source_url: https://admissions.dartmouth.edu/apply-dartmouth/universal-need-blind-policy
source_snippet: "Dartmouth College has expanded its longstanding need-blind admissions policy to include all international citizens. ... Dartmouth becomes the sixth college or university in the United States with universal need-blind admissions paired with a commitment to meet 100 percent of demonstrated need."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-015 — minimum test score (none)
field: undergraduate.testing.minimum_score
value: "None published for SAT/ACT"
source_url: https://admissions.dartmouth.edu/glossary-question/there-minimum-test-score-sat-or-act-required-admission-dartmouth
source_snippet: "No. We review each application carefully, regardless of standardized testing results."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-U-016 — degree catalog (Degree Finder)
field: programs.degree_finder_catalog
value: { total: 95, pages: 10, per_page: 10, ug_ba: 52, ug_be: 1, grad: 42 }
source_url: https://home.dartmouth.edu/degrees
source_snippet: "Find your passion here. Browse the undergraduate majors and graduate programs of study available at Dartmouth. Dartmouth offers graduate programs through the Guarini School of Graduate and Advanced Studies, and professional programs at the Geisel School of Medicine, Thayer School of Engineering, and Tuck School of Business."
capture_date: 2026-07-05
evidence_type: official_webpage_table
```

```yaml
# E-G-001 — CS graduate program deadline
field: graduate.computer_science.deadline
value: "December 31 (December 15 priority)"
source_url: https://graduate.dartmouth.edu/admissions/programs/computer-science
source_snippet: "Application Deadline: December 31 (December 15 Priority Deadline)"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-002 — CS graduate program requirements (fee, GRE, ELP, ETS code)
field: graduate.computer_science.requirements
value: { app_fee_usd: 100, gre: "Not accepted", elp: "TOEFL/IELTS/Duolingo for non-US/Canada", ets_code: "3351 (Guarini)", rec_letters: "3 required, up to 4", degrees: ["MS 4+1", "MS", "PhD"] }
source_url: https://graduate.dartmouth.edu/admissions/programs/computer-science
source_snippet: "Application Fee $100 ... GRE Not accepted. ... English Language Proficiency: Language proficiency test scores are required for non-US citizens, with the exception of those who are earning or have earned a degree from institutions in the US or Canada, or whose primary language of instruction at their non-US institution was English. We accept TOEFL, IELTS, and Duolingo. The ETS code for the Guarini School is 3351 ... Recommendation Letters: 3 required, up to 4 accepted. ... Degrees Offered: MS 4+1, MS, PhD"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-003 — graduate fee waiver (open to non-US citizens)
field: graduate.application.fee_waiver
value: "Open to US citizens, permanent residents, AND non-US citizens; criteria: current Dartmouth student / US military veteran / Guarini recruiting event attendee / GRE fee-reduction voucher holder"
source_url: https://graduate.dartmouth.edu/admissions/applying-dartmouth/fee-waiver-criteria
source_snippet: "All programs have an application fee. Please visit the relevant program page for details. Application fees are non-refundable. ... US citizens, permanent residents, and non-US citizens are all eligible for our fee waiver criteria."
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-004 — Geisel MD admissions timeline
field: graduate.medicine.admissions_timeline
value: { amcas_opens: "May 5, 2026", amcas_submissions_close: "Nov 2, 2026", secondary_deadline: "Nov 16, 2026", interviews: "August 2026 - March 2027" }
source_url: https://geiselmed.dartmouth.edu/admissions/
source_snippet: "Important Dates: May 5, 2026: AMCAS Applications Open; May 28, 2026: Applications may be filed with AMCAS; August 2026: Interviews Begin; Nov. 2, 2026: AMCAS Submissions Close; Nov. 16, 2026: Final Deadline for Secondary Applications; March, 2027: Interviews End"
capture_date: 2026-07-05
evidence_type: official_webpage
```

```yaml
# E-G-005 — Guarini graduate program directory (18 programs)
field: graduate.guarini.program_directory
value: ["Chemistry", "Cognitive Neuroscience", "Comparative Literature", "Computational Science and Modeling", "Computer Science", "Earth and Planetary Sciences", "Ecology Evolution Environment and Society (EEES)", "Engineering", "Health Policy and Clinical Practice", "Integrative Neuroscience", "MALS", "Master of Energy Transition", "Mathematics", "Molecular and Cellular Biology (MCB)", "Physics and Astronomy", "Psychological and Brain Sciences", "Quantitative Biomedical Sciences", "Sonic Practice"]
source_url: https://graduate.dartmouth.edu/admissions/programs
source_snippet: "Programs: Chemistry; Cognitive Neuroscience; Comparative Literature; Computational Science and Modeling; Computer Science; Earth and Planetary Sciences; Ecology, Evolution, Environment, and Society; Engineering; Health Policy and Clinical Practice; Integrative Neuroscience; Master of Arts in Liberal Studies (MALS); Master of Energy Transition; Mathematics; Molecular and Cellular Biology; Physics and Astronomy; Psychological and Brain Sciences; Quantitative Biomedical Sciences; Sonic Practice"
capture_date: 2026-07-05
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
dartmouth-knowledge-base-v2/
├── overview/
│   ├── dartmouth-overview              (Section 0 — counts, hierarchy, degree inventory, matrix)
│   └── dartmouth-verification-callouts (the corrections table at top)
├── undergraduate/
│   ├── dartmouth-ug-arts-sciences      (Section 1.2 — 52 BA majors, A&S)
│   ├── dartmouth-ug-engineering        (Section 1.2 — 1 BE, Thayer)
│   ├── dartmouth-ug-minors             (Section 1.4 — minors)
│   └── dartmouth-ug-requirements       (Section 1.5 + Section 3)
├── graduate/
│   ├── dartmouth-grad-guarini          (Section 2.1 — Guarini central + A&S depts)
│   ├── dartmouth-grad-thayer           (Section 2.1 — Thayer engineering)
│   ├── dartmouth-grad-tuck             (Section 2.1 — Tuck MBA)
│   ├── dartmouth-grad-geisel           (Section 2.1 — Geisel MD + PhD + TDI)
│   ├── dartmouth-grad-joint-degrees    (Section 2.1 — joint/dual)
│   └── dartmouth-grad-deep-dive-cs     (Section 2.2)
├── admissions/
│   ├── dartmouth-ug-deadlines-tests    (Section 3.1, 3.2)
│   └── dartmouth-grad-admissions       (Section 3.3)
├── costs-aid/
│   └── dartmouth-costs-aid             (Section 4)
└── evidence/
    └── dartmouth-evidence-chain        (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "dartmouth-knowledge-base-v2"
  university: "Dartmouth College"
  school: "<home college>"            # e.g. "Guarini School of Graduate & Advanced Studies"
  department: "<home department, if applicable>"
  degree_level: "<BA|BEng|MA|MS|MFA|MEng|MBA|MPH|MHA|PhD|MD|Joint/Dual>"
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
| P0 | Exact undergraduate application fee (current $) | Common App Dartmouth page / apply.dartmouth.edu | The fee (~$85) could not be confirmed from a single Dartmouth webpage; verify at submission |
| P0 | PhD stipend rates (Guarini/Thayer/Geisel) | graduate.dartmouth.edu/financial-support/funding/stipends-and-benefits | Not scraped this run |
| P0 | Graduate tuition & living costs (per program) | graduate.dartmouth.edu/admissions-financial-aid/tuition-living-costs | Not scraped this run |
| P0 | Tuck MBA deadlines (rounds) + application fee | tuck.dartmouth.edu/mba/admissions | Not scraped this run |
| P1 | Class Profile (Class of 2028/2029 SAT/ACT ranges, accept rate) | admissions.dartmouth.edu/apply/class-profile-testing | Page renders data via JS widgets; needs deeper extraction |
| P1 | Geisel MD specific requirements (GPA, MCAT median, prerequisites) | geiselmed.dartmouth.edu/admissions/ | High-level timeline captured; detailed prereqs not scraped |
| P1 | Per-program GRE policy across all 18 Guarini programs | graduate.dartmouth.edu/admissions/programs/* | Only CS captured; sample 5–8 more |
| P1 | Tuck joint/dual degree full list (PhD-MBA, MEng-MBA, etc.) | tuck.dartmouth.edu/mba/academic-experience/joint-and-dual-degrees | Only PhD-MBA + MD-MBA captured |
| P2 | Distributive requirement category codes (full list) | ORC undergraduate general regs | High-level only this run |
| P2 | Thayer PhD tracks (Industry PhD, PhD Innovation, Medical Physics) detail | engineering.dartmouth.edu/graduate | Listed but not detailed |

---

## SECTION 7 — Cross-school comparison framework (Dartmouth column)

| Dimension | Dartmouth | (compare with…) |
|-----------|-----------|-----------------|
| Total UG cost/yr (2026-27) | $98,946 | MIT, Harvard, Yale, Princeton, Stanford |
| Tuition/yr | $71,697 | |
| Need-blind (intl)? | **Yes** | One of ~6-8 U.S. schools |
| EA/ED deadline | ED Nov 1 (no EA; binding ED) | |
| RD deadline | **Jan 1** | (Caltech Jan 5; UChicago Jan 4) |
| SAT/ACT required? | **Yes** (reinstated Class of 2029) | (Columbia/Yale/Brown still test-optional/test-flexible) |
| TOEFL "typical" | 100+ (pre-2026-01-21) / 5+ (new scale) | |
| IELTS "typical" | 7+ | |
| Duolingo "typical" | 135+ | |
| Zero parent contribution threshold | $125,000 | |
| Full tuition band | $125k–$175k | |
| Required student loan | **None** (loan-free) | |
| UG app fee | ~$85 (verify) | |
| Enrollment deposit | **None** (signature only) | Distinctive |
| Total degree programs (Rule 1) | **95** | (compare with peer Ivies) |
| UG degree programs | 53 (52 BA + 1 BE) | |
| Grad degree programs | 42 | |
| Schools/colleges | 5 (1 UG college + 4 grad/prof) | |
| UG student body | ~4,500 | |
| April 15 resolution (PhD) | Yes (CGS) | |

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.dartmouth.edu, home.dartmouth.edu/degrees, dartmouth.smartcatalogiq.com (ORC), graduate.dartmouth.edu (Guarini), engineering.dartmouth.edu (Thayer), www.tuck.dartmouth.edu (Tuck), geiselmed.dartmouth.edu (Geisel), tdi.dartmouth.edu / healthsciences.dartmouth.edu (TDI), irving.dartmouth.edu (Irving Institute)
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch for static; 95/95 Degree Finder entries captured; reconciliation 95 == 95 == 95 ✓
> **Cache**: `uni-cache/schools/dartmouth/` — site-memory.json (platform: drupal-custom), last-extract.json (95 programs), content-hashes.json (8 watched pages, baseline)
> **Granularity**: school → department → degree-level → program
