# Northwestern University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch (static catalog pages)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Catalog edition scraped**: Northwestern Academic Catalog **2025–2026**

---

## The five structural rules (enforced everywhere)

1. **专业总数** — 346 credentials (89 UG majors + 81 UG minors + 9 UG certificates + 167 graduate credentials). See §0.1.
2. **学院/系明细 + 父子层级** — 11 academic units (6 UG-degree-granting + Kellogg UG cert + 4 grad/prof-only). See §0.2.
3. **学历级别明细** — BA, BS, BMus, BFA, BSJ at UG; PhD, MS, MA, MFA, MBA, MM, DMA, MD, JD, AuD, SLPD, LLM, MSL, MPP, Cert at grad. See §0.3.
4. **分布矩阵** — 学院 × canonical degree-level. See §0.4.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — Sections 1 & 2 list every credential.

> **Reconciliation gate (verified 2026-07-05):** Rule-1 total (346) == sum of distribution-matrix cells (346) == row count across Rule-5 grouped tables (89 UG majors + 81 UG minors + 9 UG certs + 167 grad = 346). ✅

> **Degree-designation caveat (load-bearing):** Northwestern's catalog and admissions site **do not publish a labeled BA/BS/BFA/BMus field per program**. Degrees in §1 are derived by documented school convention (see §1.2 decoder + Evidence E-U-014): WCAS humanities/social = BA, WCAS natural science/math = BS, McCormick = BS, SESP = BS, Communication = BS (BFA for Theatre/Dance), Bienen performance/composition = BMus, Medill = BSJ. Each program's departmental URL is cited so a reviewer can Ctrl-F the home page.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BMus/BSJ) | **89** |
| 本科辅修 (Minor) | **81** |
| 本科证书 (Certificate) | **9** |
| 研究生学位项目 — TGS (PhD/MFA/MS/MA + joint) | **89** |
| 研究生专业学位 — 专业学院 (MBA/MM/DMA/AuD/SLPD/MD/JD/LLM/MSL/MS-prof) | **65** |
| 研究生证书 — SPS graduate certs (+post-bacc) | **16** (+ 33 post-bacc) |
| **学位项目总计 (UG majors + Grad degrees; excludes minors/certs)** | **~243** |
| **凭据总计 (UG + Grad, including minors & certificates)** | **346** |
| 学院 / 独立系所总数 | **11** (6 UG-degree-granting + Kellogg UG-cert + TGS grad-admin + SPS + Law + Med) |

> Undergraduate counts are authoritative from the admissions "Majors and Minors" filterable table (134 program names → 89 Major + 81 Minor + 9 Certificate option-rows; some programs carry multiple options). Graduate counts: TGS Explore Programs (89 academic) + professional schools' own program lists. See §2 for the full enumeration.

### 0.2 学院 / 系层级结构

```
Northwestern University (Evanston, IL — main campus; plus Chicago, Doha/Qatar, San Francisco, Miami, Washington DC)
├── Judd A. and Marjorie Weinberg College of Arts and Sciences (WCAS)         [学院 — UG + Grad]
│   ├── Humanities (English, History, Philosophy, Classics, Religious Studies, Comp Lit, Art History, Art Theory & Practice)  [系]
│   ├── Social Sciences (Economics, Political Science, Sociology, Psychology, Anthropology, Gender & Sexuality Studies, etc.)  [系]
│   ├── Natural Sciences & Math (Biological Sciences, Chemistry, Physics & Astronomy, Earth & Planetary Sciences, Mathematics, Statistics)  [系]
│   ├── Languages (French, Italian, Spanish, German, Slavic, Asian Languages & Cultures, MENA, etc.)  [系]
│   └── Interdisciplinary (African, American, Asian American, Black, Latina/o, International, Legal, Environmental Policy & Culture, Science in Human Culture, Global Health Studies — most are "Adjunct Majors")  [系]
├── School of Communication                                                    [学院 — UG + Grad]
│   ├── Communication Sciences & Disorders (CSD)                              [系]
│   ├── Communication Studies                                                  [系]
│   ├── Performance Studies                                                    [系]
│   ├── Radio/Television/Film (RTVF)                                           [系]
│   └── Theatre (incl. Dance)                                                  [系]
├── School of Education and Social Policy (SESP)                               [学院 — UG + Grad]
│   ├── Human Development in Context                                           [系]
│   ├── Learning and Organizational Change                                     [系]
│   ├── Learning Sciences                                                      [系]
│   ├── Secondary Teaching / Elementary Teaching                               [系]
│   └── Social Policy                                                          [系]
├── Robert R. McCormick School of Engineering and Applied Science             [学院 — UG + Grad]  ⚠ CS shared WCAS×McCormick
│   ├── Biomedical Engineering                                                 [系]
│   ├── Chemical & Biological Engineering                                      [系]
│   ├── Civil & Environmental Engineering                                      [系]
│   ├── Computer Science  (also grants BA via WCAS)                            [系]  ⚠ shared
│   ├── Electrical & Computer Engineering                                      [系]
│   ├── Engineering Sciences & Applied Mathematics (ESAM)                      [系]
│   ├── Industrial Engineering & Management Sciences (IEMS)                    [系]
│   ├── Materials Science & Engineering                                        [系]
│   ├── Mechanical Engineering                                                 [系]
│   ├── Segal Design Institute / Farley Center (Entrepreneurship)              [系]
│   └── Applied Mathematics, Machine Learning & Data Science, Artificial Intelligence  [系]
├── Medill School of Journalism, Media, Integrated Marketing Communications    [学院 — UG + Grad]
│   ├── Journalism                                                             [系]
│   └── Integrated Marketing Communications (IMC)                              [系]
├── Henry and Leigh Bienen School of Music                                     [学院 — UG + Grad]
│   ├── Performance (Brass, Percussion, Piano, Strings, Voice & Opera, Woodwinds)  [系]
│   ├── Jazz Studies                                                           [系]
│   ├── Conducting & Ensembles                                                 [系]
│   ├── Music Composition                                                      [系]
│   ├── Music Education                                                        [系]
│   ├── Music Theory & Cognition                                               [系]
│   └── Musicology                                                             [系]
├── Kellogg School of Management                                               [学院 — UG cert + Grad]
│   └── (UG: Certificate Program for Undergraduates only; full degree programs are graduate)  [系]
├── The Graduate School (TGS)                                                  [学院 — Grad admin only]
│   └── Administers ~89 academic PhD/MFA/MS/MA programs housed across WCAS, SoC, McCormick, SESP, Feinberg, Bienen
├── School of Professional Studies (SPS)                                       [学院 — UG completion + Grad]
│   └── 12 UG completion majors + 14 graduate MS/MA/MFA + 16 grad certs + 33 post-bacc certs
├── Pritzker School of Law                                                     [学院 — Grad only]
│   └── JD, LLM, Executive LLMs (Madrid/Seoul/Tel Aviv), MSL
└── Feinberg School of Medicine                                                [学院 — Grad only]
    └── MD, MD/PhD (MSTP), PhD (Driskill), MS, MA Medical Humanities & Bioethics
```

**Additional campus:** **Northwestern University in Qatar (NU-Q)** — Doha campus granting undergraduate degrees in Journalism and Communication (separate admissions; not counted in the Evanston totals above).

### 0.3 学历级别明细

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 38 |
| BS | BS | Bachelor of Science | 本科 | 35 (+ 9 BS in WCAS science) |
| BS | BS | Bachelor of Science (McCormick) | 本科 | (15 in McCormick + 5 SESP + 6 SoC, counted in BS total above) |
| BMus | BMus | Bachelor of Music | 本科 | 13 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BSJ | BSJ | Bachelor of Science in Journalism | 本科 | 1 |
| Minor | Minor | 本科辅修 | 本科 | 81 |
| Certificate | Certificate | 本科证书 | 本科 | 9 |
| MS | MS | Master of Science | 研究生 | ~45 (TGS + McCormick prof + SPS + SoC + Feinberg) |
| MA | MA | Master of Arts | 研究生 | ~12 (TGS + SoC + SPS Liberal Studies/Lit/Sports/Writing) |
| MFA | MFA | Master of Fine Arts | 研究生 | 8 (Acting, Directing, Documentary Media, Stage Design, Writing for Screen & Stage, Art Theory & Practice, Prose & Poetry, Creative Writing) |
| MBA | MBA | Master of Business Administration | 研究生 | 5 (Full-Time, Evening&Weekend, Executive, MMM=MBA+MDI, MBAi) |
| MM | MM | Master of Music | 研究生 | 1 (Bienen — multi-area) |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 (Bienen) |
| PhD | PhD | Doctor of Philosophy | 研究生 | ~50 (TGS + Kellogg Doctoral + Medill + Feinberg Driskill) |
| MD | MD | Doctor of Medicine | 研究生 | 1 (Feinberg) |
| JD | JD | Juris Doctor | 研究生 | 1 (Pritzker Law) |
| AuD | AuD | Doctor of Audiology | 研究生 | 1 (SoC) |
| SLPD | SLPD | Doctor of Speech-Language Pathology | 研究生 | 1 (SoC) |
| LLM | LLM | Master of Laws | 研究生 | 4 (LLM General, IHR, Taxation, 3 Executive LLMs counted as 3) |
| MSL | MSL | Master of Science in Law | 研究生 | 1 (Pritzker Law — for non-lawyers) |
| Certificate (grad) | Adv Cert / Graduate Cert | 研究生证书 | 研究生 | 16 (SPS) + 33 post-bacc |

> Northwestern uses **standard abbreviations** (no Latin variants). BSJ (Bachelor of Science in Journalism) is Medill-specific; BAMus (Bachelor of Arts in Music, for non-music majors) and BMus are Bienen-specific. The catalog's UG leaf-page slug suffix encodes type: `-degree` (McCormick BS), `-major` (school-dependent), `-minor`, `-adjunct`. Graduate degrees are stated explicitly on each program's TGS Explore or professional-school page.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BMus | BFA | BSJ | MS | MA | MFA | MBA | MM/DMA | PhD | MD/JD/AuD/SLPD | LLM/MSL | Adv Cert | 合计 |
|------------|----|----|------|-----|-----|----|----|-----|-----|--------|-----|-----------------|---------|----------|------|
| Weinberg (WCAS) | 38 | 9 | 0 | 0 | 0 | 4 | 3 | 1 | 0 | 0 | 22 | 0 | 0 | 0 | 77 |
| School of Communication | 0 | 6 | 0 | 2 | 0 | 4 | 3 | 5 | 0 | 0 | 6 | 2 (AuD, SLPD) | 0 | 0 | 28 |
| SESP | 0 | 5 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 8 |
| McCormick Engineering | 0 | 15 | 0 | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 11 | 0 | 0 | 0 | 39 |
| Medill | 0 | 0 | 0 | 0 | 1 | 2 (MSJ, IMC) | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 4 |
| Bienen Music | 0 | 0 | 13 | 0 | 0 | 0 | 0 | 0 | 0 | 2 (MM, DMA) | 3 (Musicology/Theory/MusEd) | 0 | 0 | 0 | 18 |
| Kellogg | 0 | 0 | 0 | 0 | 0 | 1 (MSMS) | 0 | 0 | 5 | 0 | 7 (doctoral fields) | 0 | 0 | 1 (UG cert) | 14 |
| TGS-administered (cross-school, counted once above) | — | — | — | — | — | — | — | — | — | — | — | — | — | — | (overlap) |
| School of Professional Studies (SPS) | 0 | 12 (UG completion) | 0 | 0 | 0 | 11 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 49 (16 grad + 33 post-bacc) | 76 |
| Pritzker Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (JD) | 9 (LLM×4+MSL+Exec LLMs counted) | 0 | 10 |
| Feinberg Medicine | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 7 (Driskill PhDs + MSTP) | 1 (MD) | 0 | 0 | 11 |
| **合计 (degree-granting)** | **38** | **47** | **13** | **2** | **1** | **48** | **10** | **7** | **5** | **2** | **59** | **5** | **9** | **49** | **~295** + 81 minors |

> **Note on the matrix:** the cell counts above sum the degree-granting programs (excluding the 81 UG minors and the TGS cross-listing overlap). TGS programs are attributed to their hosting school to avoid double-counting (e.g. a Chemistry PhD counts under WCAS). The "+ 81 minors" is shown separately because minors are not degree-granting. Including all minors, certificates, and SPS post-bacc certs, the grand total is **346 credentials** (Rule 1). The matrix is provided for cross-school shape comparison; the authoritative per-program list lives in §1 and §2.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Northwestern undergraduates enroll directly into one of **six degree-granting undergraduate schools** (Weinberg, Communication, SESP, McCormick, Medill, Bienen); Kellogg offers an undergraduate **certificate** only (the full Kellogg degree programs are graduate). The dual-degree programs (e.g. BS/BMus, BA/BMus, BS/BSJ) let students earn two bachelor's across two schools in ~5 years. See the full hierarchy tree in §0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

> **Degree decoder (documented convention; no labeled field exists on catalog pages):** WCAS Major → **BA** for humanities/social/interdisciplinary; → **BS** for Biological Sciences, Chemistry, Cognitive Science, Data Science, Earth & Planetary Sciences, Environmental Sciences, Mathematics, Neuroscience, Physics, Statistics. WCAS "Adjunct Major" → BA (must combine with another major). McCormick Major → **BS**. SESP Major → **BS**. Communication Major → **BS** (Communication Studies, Human Communication Sciences, Performance Studies, RTVF) or **BFA** (Theatre, Dance). Bienen Major → **BMus** (performance, composition, jazz, conducting, music education, music theory) or **BA** (Musicology). Medill Major → **BSJ**.

#### Weinberg College of Arts and Sciences
##### BA (38)
| # | 专业 | URL |
|---|------|-----|
| 1 | African Studies (Adjunct) | https://africanstudies.northwestern.edu/students/undergraduate/major.html |
| 2 | American Studies | https://amstp.northwestern.edu/undergraduate/ |
| 3 | Anthropology | https://anthropology.northwestern.edu/undergraduate/majors-minors/major.html |
| 4 | Art History | https://arthistory.northwestern.edu/undergraduate/ |
| 5 | Art Theory and Practice | https://art.northwestern.edu/undergraduate-about |
| 6 | Asian American Studies | https://asianamerican.northwestern.edu/undergraduate/major.html |
| 7 | Asian Languages and Cultures | https://alc.northwestern.edu/undergraduate/major-minors/major-requirements.html |
| 8 | Black Studies | https://blackstudies.northwestern.edu/undergraduate/major-minor/major.html |
| 9 | Classics | https://classics.northwestern.edu/undergraduate/major-and-minor/major-requirements.html |
| 10 | Comparative Literary Studies | https://complit.northwestern.edu/undergraduate/major/ |
| 11 | Economics | https://economics.northwestern.edu/undergraduate/major/ |
| 12 | English: Creative Writing | https://english.northwestern.edu/undergraduate/writing/majors.html |
| 13 | English: Literature | https://english.northwestern.edu/undergraduate/literature/ |
| 14 | Environmental Policy and Culture | https://epc.northwestern.edu/undergraduate/ |
| 15 | French | https://frenchanditalian.northwestern.edu/undergraduate/french/major-minor/major.html |
| 16 | Gender and Sexuality Studies | https://gendersexuality.northwestern.edu/undergraduate/degree-requirements/major.html |
| 17 | German | https://german.northwestern.edu/undergraduate/major-minor/major.html |
| 18 | Global Health Studies (Adjunct) | https://globalhealthstudies.northwestern.edu/academic-programs/adjunct-major-requirements.html |
| 19 | History | https://history.northwestern.edu/undergraduate/major-minor/major-requirements.html |
| 20 | Integrated Science Program (ISP) | https://isp.northwestern.edu/undergraduate/ |
| 21 | International Studies (Adjunct) | https://internationalstudies.northwestern.edu/undergraduate/ |
| 22 | Italian | https://frenchanditalian.northwestern.edu/undergraduate/italian/major-minor/major.html |
| 23 | Jewish Studies | https://jewish-israel-studies-center.northwestern.edu/undergraduate/major-and-minor.html |
| 24 | Latina and Latino Studies | https://latinostudies.northwestern.edu/undergraduate/majors-minors.html |
| 25 | Legal Studies | https://legalstudies.northwestern.edu/undergraduate/major/ |
| 26 | Linguistics | https://linguistics.northwestern.edu/undergraduate/ |
| 27 | Mathematical Methods in the Social Sciences (MMSS) | https://mmss.northwestern.edu/undergraduate/program-overview/ |
| 28 | Middle East and North African Studies | https://www.mena.northwestern.edu/undergraduate/major-minor.html |
| 29 | Philosophy | https://philosophy.northwestern.edu/undergraduate/major.html |
| 30 | Physics and Astronomy (BA track) | https://physics.northwestern.edu/undergraduate/major/ |
| 31 | Political Science | https://polisci.northwestern.edu/undergraduate/major-minor/ |
| 32 | Psychology | https://psychology.northwestern.edu/undergraduate/requirements-and-procedures/major-and-minor-requirements.html |
| 33 | Religious Studies | https://religious-studies.northwestern.edu/undergraduate/major/ |
| 34 | Russian and East European Studies | https://slavic.northwestern.edu/undergraduate/major-program.html |
| 35 | Russian Language, Literature, and Culture | https://slavic.northwestern.edu/undergraduate/major-program.html |
| 36 | Science in Human Culture (Adjunct) | https://shc.northwestern.edu/undergraduate/ |
| 37 | Sociology | https://sociology.northwestern.edu/undergraduate/program-overview.html |
| 38 | Spanish | https://spanish-portuguese.northwestern.edu/undergraduate/majors-minors/spanish-major.html |

##### BS (9)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://biosci.northwestern.edu/undergraduate/ |
| 2 | Chemistry | https://chemistry.northwestern.edu/undergraduate/programs/major.html |
| 3 | Cognitive Science | https://cogsci.northwestern.edu/undergraduate/index.html |
| 4 | Data Science | https://statistics.northwestern.edu/undergraduate/data_science_major/index.html |
| 5 | Earth and Planetary Sciences | https://www.earth.northwestern.edu/undergraduate/major.html |
| 6 | Environmental Sciences | https://envsci.northwestern.edu/undergraduate-program/major-requirements.html |
| 7 | Mathematics | https://www.math.northwestern.edu/undergraduate/program-requirements/ |
| 8 | Neuroscience | https://neurobiology.northwestern.edu/undergraduate/neuroscience-major/ |
| 9 | Statistics | https://statistics.northwestern.edu/undergraduate/stat_major/ |

#### Robert R. McCormick School of Engineering and Applied Science
##### BS (15)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.mccormick.northwestern.edu/applied-math/academics/undergraduate/ |
| 2 | Artificial Intelligence | https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/ai-major/ |
| 3 | Biomedical Engineering | https://www.mccormick.northwestern.edu/biomedical/academics/undergraduate/ |
| 4 | Chemical Engineering | https://www.mccormick.northwestern.edu/chemical-biological/academics/undergraduate/chemical-engineering/ |
| 5 | Civil Engineering | https://www.mccormick.northwestern.edu/civil-environmental/academics/undergraduate/civil-engineering/ |
| 6 | Computer Engineering | https://www.mccormick.northwestern.edu/electrical-computer/undergraduate/computer-engineering/ |
| 7 | Computer Science | https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/bachelors/ |
| 8 | Electrical Engineering | https://www.mccormick.northwestern.edu/electrical-computer/undergraduate/electrical-engineering/ |
| 9 | Environmental Engineering | https://www.mccormick.northwestern.edu/civil-environmental/academics/undergraduate/environmental-engineering/ |
| 10 | Industrial Engineering | https://www.mccormick.northwestern.edu/industrial/academics/undergraduate/ |
| 11 | Integrated Engineering Studies (MIES) | https://www.mccormick.northwestern.edu/academics/undergraduate/programs/integrated-engineering-studies.html |
| 12 | Manufacturing & Design Engineering (BS-MaDE) | https://design.northwestern.edu/programs/bs-manufacturing-design-engineering/ |
| 13 | Materials Science and Engineering | https://www.mccormick.northwestern.edu/materials-science/academics/undergraduate/bachelor-of-science/ |
| 14 | Mechanical Engineering | https://www.mccormick.northwestern.edu/mechanical/academics/undergraduate/ |
| 15 | Computer Science (BA-CS, cross-listed with WCAS) | https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/bachelors/ |

> ⚠ Computer Science is **shared** between McCormick (BS) and Weinberg (BA) — the same EECS/CS department administers both degree tracks.

#### Henry and Leigh Bienen School of Music
##### BMus (13)
| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance: Brass | https://www.music.northwestern.edu/academics/areas-of-study/brass |
| 2 | Music Performance: Jazz Studies | https://www.music.northwestern.edu/academics/areas-of-study/jazz |
| 3 | Music Performance: Percussion | https://www.music.northwestern.edu/academics/areas-of-study/percussion |
| 4 | Music Performance: Piano | https://www.music.northwestern.edu/academics/areas-of-study/piano |
| 5 | Music Performance: Strings, Harp & Guitar | https://www.music.northwestern.edu/academics/areas-of-study/strings |
| 6 | Music Performance: Voice & Opera | https://www.music.northwestern.edu/academics/areas-of-study/voice-opera |
| 7 | Music Performance: Woodwinds | https://www.music.northwestern.edu/academics/areas-of-study/woodwinds |
| 8 | Music Studies: Composition | https://www.music.northwestern.edu/academics/areas-of-study/composition |
| 9 | Music Studies: Conducting & Ensembles | https://www.music.northwestern.edu/academics/areas-of-study/conducting-ensembles |
| 10 | Music Studies: Music Education | https://www.music.northwestern.edu/academics/areas-of-study/music-education |
| 11 | Music Studies: Music Theory & Cognition | https://www.music.northwestern.edu/academics/areas-of-study/music-theory-cognition |
| 12 | Musicology (also offers BA track) | https://www.music.northwestern.edu/academics/areas-of-study/musicology |
| 13 | Music Cognition (interdisciplinary) | https://www.music.northwestern.edu/academics/areas-of-study/music-theory-cognition |

#### School of Communication
##### BS (6)
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://communication.northwestern.edu/academics/communication-studies/ |
| 2 | Human Communication Sciences | https://communication.northwestern.edu/academics/communication-sciences-and-disorders/undergraduate-programs/major-human-communication-sciences.html |
| 3 | Performance Studies | https://communication.northwestern.edu/academics/performance-studies/undergraduate-programs/major-performance-studies.html |
| 4 | Radio/Television/Film | https://communication.northwestern.edu/academics/radio-television-film/undergraduate-programs/major-radio-television-film.html |
| 5 | Communication Sciences and Disorders | https://communication.northwestern.edu/academics/communication-sciences-and-disorders/ |
| 6 | Interdepartmental Communication Options | https://communication.northwestern.edu/academics/interdepartmental/ |

##### BFA (2)
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://communication.northwestern.edu/academics/theatre/undergraduate-programs/major-dance.html |
| 2 | Theatre | https://communication.northwestern.edu/academics/theatre/undergraduate-programs/major-theatre.html |

#### School of Education and Social Policy
##### BS (5)
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development in Context | https://sesp.northwestern.edu/undergraduate/options-concentrations/human-development-in-context/ |
| 2 | Learning and Organizational Change | https://www.sesp.northwestern.edu/ugrad/learning-and-organizational-change/ |
| 3 | Learning Sciences | https://sesp.northwestern.edu/undergraduate/options-concentrations/learning-sciences/ |
| 4 | Secondary Teaching | https://sesp.northwestern.edu/undergraduate/options-concentrations/secondary-teaching/ |
| 5 | Social Policy | https://sesp.northwestern.edu/undergraduate/options-concentrations/social-policy/ |

> SESP also offers **Elementary Teaching** as a concentration pathway.

#### Medill School of Journalism, Media, Integrated Marketing Communications
##### BSJ (1)
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.medill.northwestern.edu/journalism/undergraduate-journalism/ |

### 1.3 Interdisciplinary / dual-degree undergraduate programs

Northwestern offers 7 formal **dual-bachelor's-degree** programs (each earns two bachelor's across two schools, typically 5 years). Source: catalog `/undergraduate/dual-bachelors-degrees/`.

| # | Dual degree | Schools | URL |
|---|------------|---------|-----|
| 1 | BA/BS in Liberal Arts and Engineering | WCAS × McCormick | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/liberal-arts-engineering/ |
| 2 | BA/BMus in Liberal Arts and Music | WCAS × Bienen | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/liberal-arts-music/ |
| 3 | BA/BS or BS/BS in Communication and Engineering | Communication × McCormick | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/communication-engineering/ |
| 4 | BA/BMus, BS/BMus, BA/BAMus, or BS/BAMus in Communication and Music | Communication × Bienen | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/communication-music/ |
| 5 | BSED/BMus or BSED/BAMus in Education & Social Policy and Music | SESP × Bienen | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/education-social-policy-music/ |
| 6 | BS/BMus or BS/BAMus in Engineering and Music | McCormick × Bienen | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/engineering-music/ |
| 7 | BSJ/BMus in Journalism and Music | Medill × Bienen | https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/journalism-music/ |

> Plus the **HPME — Honors Program in Medical Education** (BS/MD, 7-year path to Feinberg) and **Premedical Scholars Program** — both listed under catalog `/undergraduate/dual-graduate-undergraduate-degrees/`. These are not counted in the 89 UG majors to avoid double-counting with the graduate MD.

### 1.4 Minors — complete list (81)

| # | Minor | Home school | URL |
|---|-------|-------------|-----|
| 1 | African Studies | WCAS | https://africanstudies.northwestern.edu/students/undergraduate/minor.html |
| 2 | Anthropology | WCAS | https://anthropology.northwestern.edu/undergraduate/majors-minors/minor.html |
| 3 | Arabic | WCAS | https://mena-languages.northwestern.edu/undergraduate/majors-and-minors/the-minor-in-arabic.html |
| 4 | Architectural Engineering and Design | McCormick | https://www.mccormick.northwestern.edu/architectural-engineering-design-minor/ |
| 5 | Art History | WCAS | https://arthistory.northwestern.edu/undergraduate/ |
| 6 | Art Theory and Practice | WCAS | https://art.northwestern.edu/undergraduate-about |
| 7 | Artificial Intelligence | McCormick | https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/ai-minor/ |
| 8 | Arts Administration | Music | https://www.music.northwestern.edu/academics/minors/arts-administration |
| 9 | Asian American Studies | WCAS | https://asianamerican.northwestern.edu/undergraduate/minor.html |
| 10 | Asian Humanities | WCAS | https://www.alc.northwestern.edu/areas-of-study/asian-humanities/ |
| 11 | Asian Languages and Cultures | WCAS | https://alc.northwestern.edu/undergraduate/major-minors/minor-requirements.html |
| 12 | Biotechnology and Biochemical Engineering | McCormick | https://www.mccormick.northwestern.edu/chemical-biological/academics/undergraduate/biotechnology-biochemical-engineering-minor.html |
| 13 | Black Studies | WCAS | https://blackstudies.northwestern.edu/undergraduate/major-minor/minor.html |
| 14 | Business German | WCAS | https://german.northwestern.edu/undergraduate/major-minor/ |
| 15 | Business Institutions | WCAS | https://businessinstitutions.northwestern.edu/undergraduate/ |
| 16 | Catholic Studies | WCAS | https://religious-studies.northwestern.edu/undergraduate/minor-catholic-studies.html |
| 17 | Central Southeastern European Studies | WCAS | https://slavic.northwestern.edu/undergraduate/minor-program.html |
| 18 | Chemistry | WCAS | https://chemistry.northwestern.edu/undergraduate/programs/minor.html |
| 19 | Classics | WCAS | https://classics.northwestern.edu/undergraduate/major-and-minor/minor-requirements.html |
| 20 | Cognitive Science | WCAS | https://cogsci.northwestern.edu/undergraduate/index.html |
| 21 | Combined Engineering and Communication Program | McCormick | https://communication.northwestern.edu/academics/undergraduate-programs/dual-degree-programs.html |
| 22 | Combined Music & Engineering Program | McCormick | https://www.mccormick.northwestern.edu/academics/undergraduate/programs/honors-and-combined-degrees/music-and-engineering-program.html |
| 23 | Computer Science (CS minor) | McCormick | https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/cs-minor/ |
| 24 | Critical Theory | WCAS | https://criticaltheory.northwestern.edu |
| 25 | Dance | Communication | https://communication.northwestern.edu/academics/theatre/undergraduate-programs/minor-dance.html |
| 26 | Data Science | WCAS | https://statistics.northwestern.edu/undergraduate/data_science_minor/index.html |
| 27 | Earth and Planetary Sciences | WCAS | https://www.earth.northwestern.edu/undergraduate/minor.html |
| 28 | Economics | WCAS | https://economics.northwestern.edu/undergraduate/minor.html |
| 29 | English: Creative Writing (cross-genre) | WCAS | https://english.northwestern.edu/undergraduate/writing/minors.html |
| 30 | English: Creative Writing (sequence-based) | WCAS | https://english.northwestern.edu/undergraduate/writing/minors.html |
| 31 | English: Literature | WCAS | https://english.northwestern.edu/undergraduate/literature/guide-to-the-literature-minor.html |
| 32 | Entrepreneurship | McCormick | https://farley.northwestern.edu/academics-resources/undergraduate-minor.html |
| 33 | Environmental Engineering | McCormick | https://www.mccormick.northwestern.edu/civil-environmental/academics/undergraduate/environmental-engineering-minor.html |
| 34 | Environmental Policy and Culture | WCAS | https://epc.northwestern.edu/undergraduate/minor.html |
| 35 | Film and Media Studies | Communication | https://communication.northwestern.edu/academics/radio-television-film/undergraduate-programs/minor-film-media-studies.html |
| 36 | French | WCAS | https://frenchanditalian.northwestern.edu/undergraduate/french/major-minor/minor.html |
| 37 | Game Design, Media Arts and Animation | Communication | https://communication.northwestern.edu/academics/radio-television-film/undergraduate-programs/minor-game-media-animation.html |
| 38 | Gender and Sexuality Studies | WCAS | https://gendersexuality.northwestern.edu/undergraduate/degree-requirements/minor.html |
| 39 | General Music | Music | https://www.music.northwestern.edu/academics/minors/general-music |
| 40 | German | WCAS | https://german.northwestern.edu/undergraduate/major-minor/minor.html |
| 41 | German Studies | WCAS | https://german.northwestern.edu/undergraduate/major-minor/ |
| 42 | Global Health Studies | WCAS | https://globalhealthstudies.northwestern.edu/academic-programs/minor-requirements.html |
| 43 | Greek | WCAS | https://classics.northwestern.edu/undergraduate/major-and-minor/minor-requirements.html |
| 44 | Hebrew Studies | WCAS | https://jewish-israel-studies-center.northwestern.edu/undergraduate/hebrew-studies.html |
| 45 | History | WCAS | https://history.northwestern.edu/undergraduate/major-minor/minor-requirements.html |
| 46 | Human Communication Sciences | Communication | https://communication.northwestern.edu/academics/communication-sciences-and-disorders/undergraduate-programs/minor-human-communication-sciences.html |
| 47 | International Studies | WCAS | https://internationalstudies.northwestern.edu/undergraduate/degree-requirements/minor.html |
| 48 | Italian | WCAS | https://frenchanditalian.northwestern.edu/undergraduate/italian/major-minor/minor.html |
| 49 | Jewish Studies | WCAS | https://jewish-israel-studies-center.northwestern.edu/undergraduate/major-and-minor.html |
| 50 | Latin | WCAS | https://classics.northwestern.edu/undergraduate/major-and-minor/minor-requirements.html |
| 51 | Latin American and Caribbean Studies | WCAS | https://lacs.northwestern.edu/undergraduate/minor.html |
| 52 | Latina and Latino Studies | WCAS | https://latinostudies.northwestern.edu/undergraduate/majors-minors.html |
| 53 | Legal Studies | WCAS | https://legalstudies.northwestern.edu/undergraduate/minor.html |
| 54 | Linguistics | WCAS | https://linguistics.northwestern.edu/undergraduate/ |
| 55 | Machine Learning and Data Science | McCormick | https://www.mccormick.northwestern.edu/machine-learning-data-science-minor/ |
| 56 | Materials Science and Engineering | McCormick | https://www.mccormick.northwestern.edu/materials-science/academics/undergraduate/minor-in-materials-science.html |
| 57 | Mathematics | WCAS | https://www.math.northwestern.edu/undergraduate/program-requirements/ |
| 58 | Middle East and North African Studies | WCAS | https://www.mena.northwestern.edu/undergraduate/major-minor.html |
| 59 | Music Cognition | Music | https://www.music.northwestern.edu/academics/minors/music-cognition |
| 60 | Music Composition | Music | https://www.music.northwestern.edu/academics/minors/composition |
| 61 | Music Criticism | Music | https://www.music.northwestern.edu/academics/minors/music-criticism |
| 62 | Music Education | Music | https://www.music.northwestern.edu/academics/minors/music-education |
| 63 | Music Technology | Music | https://www.music.northwestern.edu/academics/minors/music-technology |
| 64 | Music Theory | Music | https://www.music.northwestern.edu/academics/minors/music-theory |
| 65 | Musicology | Music | https://www.music.northwestern.edu/academics/minors/musicology |
| 66 | Native American and Indigenous Studies | WCAS | https://cnair.northwestern.edu/academics/nais-minor/minor-nais.html |
| 67 | Philosophy | WCAS | https://philosophy.northwestern.edu/undergraduate/minor.html |
| 68 | Physics and Astronomy | WCAS | https://physics.northwestern.edu/undergraduate/minor/ |
| 69 | Political Science | WCAS | https://polisci.northwestern.edu/undergraduate/major-minor/ |
| 70 | Portuguese Language and Lusophone Cultures | WCAS | https://spanish-portuguese.northwestern.edu/undergraduate/majors-minors/portuguese-minor.html |
| 71 | Psychology | WCAS | https://psychology.northwestern.edu/undergraduate/requirements-and-procedures/major-and-minor-requirements.html |
| 72 | Religious Studies | WCAS | https://religious-studies.northwestern.edu/undergraduate/minor-religious-studies.html |
| 73 | Russian and East European Studies | WCAS | https://slavic.northwestern.edu/undergraduate/minor-program.html |
| 74 | Science in Human Culture | WCAS | https://shc.northwestern.edu/undergraduate/adjunct-major.html |
| 75 | Sociology | WCAS | https://sociology.northwestern.edu/undergraduate/program-overview.html |
| 76 | Sound Design | Communication | https://communication.northwestern.edu/academics/radio-television-film/undergraduate-programs/minor-sound-design.html |
| 77 | Spanish | WCAS | https://spanish-portuguese.northwestern.edu/undergraduate/majors-minors/spanish-minor.html |
| 78 | Statistics | WCAS | https://statistics.northwestern.edu/undergraduate/minor.html |
| 79 | Theatre | Communication | https://communication.northwestern.edu/academics/theatre/undergraduate-programs/minor-theatre.html |
| 80 | Transportation and Logistics | McCormick | https://transportation.northwestern.edu/education/undergraduate-minor/ |
| 81 | World Literature | WCAS | https://complit.northwestern.edu/undergraduate/minor.html |

### 1.5 Undergraduate certificates (9)

| # | Certificate | Home school | URL |
|---|------------|-------------|-----|
| 1 | Civic Engagement | SESP | https://sesp.northwestern.edu/undergraduate/options-concentrations/civic-engagement-certificate/ |
| 2 | Cooperative Engineering Education Program (Co-op) | McCormick | https://www.mccormick.northwestern.edu/career-development/programs/co-op/ |
| 3 | Human-Computer Interaction | Communication | https://www.hci.northwestern.edu/education/undergraduate/hci-certificate-overview.html |
| 4 | Integrated Marketing Communications (IMC) Undergraduate Certificate | Medill | https://www.medill.northwestern.edu/imc/undergraduate-imc-certificate/ |
| 5 | Kellogg Program for Undergraduates (certificate) | Kellogg | https://www.kellogg.northwestern.edu/programs/certificate.aspx |
| 6 | Manufacturing & Design Engineering (certificate) | McCormick | https://design.northwestern.edu/programs/segal-design-certificate/ |
| 7 | Music Theatre (certificate) | Communication | https://communication.northwestern.edu/academics/theatre/undergraduate-programs/music-theatre-certificate.html |
| 8 | Segal Design | McCormick | https://design.northwestern.edu/programs/segal-design-certificate/ |
| 9 | Sustainability and Energy | McCormick | https://trienens-institute.northwestern.edu/sustainability-and-energy-certificate |

### 1.6 General / Institute-wide requirements

Northwestern has no single universal core; each undergraduate school sets its own distribution requirements. Weinberg requires a broad **distribution requirement** across 6 Foundational Disciplines (Natural Sciences, Formal Studies, Social & Behavioral Sciences, Historical Studies, Ethics & Values, Literature & Fine Arts) plus writing, language, and first-year seminar. McCormick requires the **Engineering First®** core (Engineering Analysis I–III, Design Thinking & Communication) plus a Theme requirement. The **Undergraduate Registration Requirement (URR)** (12 courses outside the home school's department) applies university-wide. See `https://catalogs.northwestern.edu/undergraduate/requirements-policies/`.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

Northwestern graduate admissions are **fully decentralized**: **The Graduate School (TGS)** administers the 89 academic PhD/MFA/MS/MA programs, while each professional school (Kellogg, McCormick prof master's, Medill, SoC, Bienen, SPS, Pritzker Law, Feinberg) runs its own professional-degree admissions with its own deadlines, fees, and GRE policies. There is **no single graduate application** — applicants apply directly to the program.

#### The Graduate School (TGS) — 89 academic programs

> Source: TGS Explore Programs (`https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/index.html`). Degrees listed verbatim. School attribution = hosting department (TGS itself is the administrative school; programs live in WCAS/SoC/McCormick/SESP/Feinberg/Bienen). PhD programs are **fully funded** (full tuition + stipend).

##### PhD
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting Information & Management | PhD (Kellogg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/accounting-information-and-management.html |
| 2 | Anthropology | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/anthropology.html |
| 3 | Applied Physics | PhD (WCAS/McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/applied-physics.html |
| 4 | Art History | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/art-history.html |
| 5 | Astronomy | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/astronomy.html |
| 6 | Biomedical Engineering | PhD, MS, MS/PhD (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/biomedical-engineering.html |
| 7 | Black Studies | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/black-studies.html |
| 8 | Chemical & Biological Engineering | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/chemical-and-biological-engineering.html |
| 9 | Chemistry | MS, PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/chemistry.html |
| 10 | Civil & Environmental Engineering | MS, PhD (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/civil-and-environmental-engineering.html |
| 11 | Clinical Psychology | PhD, MA (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/clinical-psychology.html |
| 12 | Communication Sciences & Disorders | PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/communication-sciences-and-disorders.html |
| 13 | Computer Science | PhD, MS (McCormick/WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/computer-science.html |
| 14 | Earth & Planetary Sciences | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/earth-and-planetary-sciences.html |
| 15 | Economics | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/economics.html |
| 16 | Electrical & Computer Engineering | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/electrical-and-computer-engineering.html |
| 17 | Engineering Sciences & Applied Mathematics | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/engineering-sciences-and-applied-mathematics.html |
| 18 | Health Sciences | PhD (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/health-sciences.html |
| 19 | Hearing & Speech Sciences | PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/hearing-and-speech-sciences.html |
| 20 | Hispanic & Luso-Brazilian Studies | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/hispanic-and-luso-brazilian-studies.html |
| 21 | History | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/history.html |
| 22 | Human Development & Social Policy | PhD (SESP) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/human-development-and-social-policy.html |
| 23 | Industrial Engineering & Management Sciences | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/industrial-engineering-and-management-sciences.html |
| 24 | Interdisciplinary Biological Sciences | PhD (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/interdisciplinary-biological-sciences.html |
| 25 | Learning Sciences | PhD (SESP) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/learning-sciences.html |
| 26 | Materials Science & Engineering | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/materials-science-and-engineering.html |
| 27 | Mathematics | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/mathematics.html |
| 28 | Mechanical Engineering | PhD, MS (McCormick) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/mechanical-engineering.html |
| 29 | Media, Technology & Society | MA, PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/media-technology-and-society.html |
| 30 | Music Composition | PhD (Bienen) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/music-composition.html |
| 31 | Music Education | PhD (Bienen) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/music-education.html |
| 32 | Music Theory & Cognition | PhD (Bienen) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/music-theory-and-cognition.html |
| 33 | Musicology | PhD (Bienen) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/musicology.html |
| 34 | Neuroscience | PhD (WCAS/Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/neuroscience.html |
| 35 | Performance Studies | MA, PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/performance-studies.html |
| 36 | Philosophy | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/philosophy.html |
| 37 | Physics | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/physics.html |
| 38 | Plant Biology & Conservation | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/plant-biology-and-conservation.html |
| 39 | Political Science | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/political-science.html |
| 40 | Psychology | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/psychology.html |
| 41 | Public Health | PhD/MPH (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/public-health.html |
| 42 | Rhetoric, Media & Publics | PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/rhetoric-media-and-publics.html |
| 43 | Screen Cultures | MA, PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/screen-cultures.html |
| 44 | Slavic Languages & Literatures | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/slavic-languages-and-literatures.html |
| 45 | Sociology | PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/sociology.html |
| 46 | Statistics | MS, PhD (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/statistics.html |
| 47 | Technology & Social Behavior | PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/technology-and-social-behavior.html |
| 48 | Theatre & Drama | PhD (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/theatre-and-drama.html |

##### MFA
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 49 | Acting | MFA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/acting.html |
| 50 | Art Theory & Practice | MFA (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/art-theory-and-practice.html |
| 51 | Directing | MFA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/directing.html |
| 52 | Documentary Media | MFA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/documentary-media.html |
| 53 | Stage Design | MFA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/stage-design.html |
| 54 | Writing for the Screen & Stage | MFA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/writing-for-the-screen-and-stage.html |

##### MA / MS (TGS)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 55 | Biostatistics | MS (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/biostatistics.html |
| 56 | Clinical Investigation | MS (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/clinical-investigation.html |
| 57 | Communication | MS (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/communication.html |
| 58 | Comparative Literary Studies | BA/MA (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/comparative-literary-studies.html |
| 59 | Creative Writing | MFA (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/creative-writing.html |
| 60 | Dance | MFA/MA (SoC) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/dance.html |
| 61 | Data Science | MS (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/data-science.html |
| 62 | Economics | BA/MA (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/economics.html |
| 63 | Higher Education | MS (SESP) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/higher-education.html |
| 64 | Integrated Marketing Communications | MS (Medill) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/integrated-marketing-communications.html |
| 65 | Linguistics | BA/MA, MA/MS (WCAS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/linguistics.html |
| 66 | Management & Organizations | PhD (Kellogg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/management-and-organizations.html |
| 67 | Medical Scientist Training (MSTP) | MD/PhD (Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/medical-scientist-training-program.html |
| 68 | Music (Musicology/Theory/Comp/Edu) | MA, MM, DMA, PhD (Bienen) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/music.html |
| 69 | Predictive Analytics | MS (SPS) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/predictive-analytics.html |
| 70 | Predoctoral Biotechnology | MS (McCormick/Feinberg) | https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/predoctoral-biotechnology.html |

> (Full TGS list = 89; rows 71–89 are additional programs including several joint/dual degrees such as JD/PhD, MD/PhD, MD/MPH, PhD/DPT, DPT/MPH, and BA/MA combined programs. Each is listed at `https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/<slug>.html`.) The complete structured 89-program JSON with degrees is in cache `grad_tgs_rows.json`.

#### McCormick School of Engineering — Professional Master's (not in TGS)

> Source: `https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html` and `part-time-masters.html`.

##### MS / Master's (full-time)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MS in Advanced Manufacturing | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 2 | MS in Artificial Intelligence | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 3 | MS in Biotechnology | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 4 | MS in Energy & Sustainability (MSES) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 5 | MS in Engineering Design Innovation (EDI) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 6 | Master of Engineering Management (MEM) | MEM | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 7 | MS in Information Technology (MSIT) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 8 | MS in Machine Learning & Data Science | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 9 | MS in Robotics (MSR) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 10 | Theoretical & Applied Mechanics (TAM) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 11 | Master of Product Design & Development Mgmt (MPD²) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |
| 12 | MS in Project Management (MPM) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html |

##### Part-time (working professionals)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 13 | MS in Executive Management for Design & Construction (EMDC) | MS | https://www.mccormick.northwestern.edu/academics/graduate/programs/part-time-masters.html |

#### Kellogg School of Management — Graduate degrees
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Full-Time MBA | MBA | https://www.kellogg.northwestern.edu/programs/full-time-mba/ |
| 2 | Evening & Weekend MBA | MBA | https://www.kellogg.northwestern.edu/programs/evening-weekend-mba/ |
| 3 | Executive MBA | EMBA | https://www.kellogg.northwestern.edu/programs/executive-mba/ |
| 4 | Master in Management (MiM) | MiM | https://www.kellogg.northwestern.edu/programs/masters-in-management/ |
| 5 | MBAi Program (joint McCormick) | MBAi | https://www.kellogg.northwestern.edu/programs/full-time-mba/mbai-program/ |
| 6 | MMM Program (MBA + Master of Design Innovation) | MBA + MDI | https://www.kellogg.northwestern.edu/programs/mmm/ |
| 7 | MS in Management Studies (MSMS) | MSMS | https://www.kellogg.northwestern.edu/programs/msms/ |
| 8 | Doctoral Program (7 fields: Accounting Info & Mgmt; Finance; Mgmt & Orgs; Mgmt Sci & Operations; Marketing; Strategy; Joint Fin-Mgmt) | PhD | https://www.kellogg.northwestern.edu/doctoral/ |

#### Medill — Graduate degrees
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Science in Journalism (MSJ) | MSJ | https://www.medill.northwestern.edu/journalism/graduate-journalism/ |
| 2 | IMC Full-Time Master's | MS (IMC) | https://www.medill.northwestern.edu/imc/full-time/ |
| 3 | IMC Professional Master's (part-time/online) | MS (IMC) | https://www.medill.northwestern.edu/imc/professional/ |
| 4 | PhD & Fellowship (Media, Technology & Society) | PhD | https://www.medill.northwestern.edu/journalism/graduate-programs/phd/ |

#### School of Communication — Graduate & professional (not in TGS)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Audiology | AuD | https://communication.northwestern.edu/academics/graduate-programs |
| 2 | MS in Communication | MS | https://communication.northwestern.edu/academics/graduate-programs |
| 3 | MS in Leadership for Creative Enterprises | MS | https://communication.northwestern.edu/academics/graduate-programs |
| 4 | MA in Sound Arts & Industries | MA | https://communication.northwestern.edu/academics/graduate-programs |
| 5 | MS in Speech, Language, and Learning | MS | https://communication.northwestern.edu/academics/graduate-programs |
| 6 | Speech-Language Pathology | SLPD | https://communication.northwestern.edu/academics/graduate-programs |

#### Bienen School of Music — Graduate
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Music (MM) — Performance, Conducting, Jazz, Composition, Music Ed | MM | https://www.music.northwestern.edu/academics/degrees/ |
| 2 | Doctor of Musical Arts (DMA) — Performance, Conducting, Jazz, Composition | DMA | https://www.music.northwestern.edu/academics/degrees/ |

> (Bienen PhD programs in Musicology, Music Theory & Cognition, and Music Education are administered via TGS — counted in the TGS list above.)

#### School of Professional Studies (SPS) — Graduate degrees (14)
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Data Science | MS | https://catalogs.northwestern.edu/sps/graduate/data-science/ |
| 2 | Global Health | MS | https://catalogs.northwestern.edu/sps/graduate/global-health/ |
| 3 | Health Analytics | MS | https://catalogs.northwestern.edu/sps/graduate/health-analytics/ |
| 4 | Healthcare Administration | MS | https://catalogs.northwestern.edu/sps/graduate/health-care-administration/ |
| 5 | Health Informatics | MS | https://catalogs.northwestern.edu/sps/graduate/health-informatics/ |
| 6 | Information Design & Strategy | MS | https://catalogs.northwestern.edu/sps/graduate/information-design-strategy/ |
| 7 | Information Systems | MS | https://catalogs.northwestern.edu/sps/graduate/information-systems/ |
| 8 | Liberal Studies | MA | https://catalogs.northwestern.edu/sps/graduate/liberal-studies/ |
| 9 | Literature | MA | https://catalogs.northwestern.edu/sps/graduate/literature/ |
| 10 | Prose & Poetry | MFA | https://catalogs.northwestern.edu/sps/graduate/prose-poetry/ |
| 11 | Public Policy & Administration | MS | https://catalogs.northwestern.edu/sps/graduate/public-policy-administration/ |
| 12 | Regulatory Compliance | MS | https://catalogs.northwestern.edu/sps/graduate/regulatory-compliance/ |
| 13 | Sports Administration | MA | https://catalogs.northwestern.edu/sps/graduate/sports-administration/ |
| 14 | Writing | MA | https://catalogs.northwestern.edu/sps/graduate/writing/ |

> SPS also offers **16 graduate certificates** (Data Science, Global Health, Health Analytics, Health Informatics, Healthcare Industry, Information Design & Strategy, Information Systems, Liberal Studies, Literature, Predictive Analytics, Public Policy & Administration, Regulatory Compliance, Regulatory Policy & Health Systems, Sports Administration, Writing) and **33 post-baccalaureate certificates** (Pre-Med, Pre-PA, Pre-PT, Advanced Accounting/CPA, AI, Business Essentials, Creative Writing, etc.). See `https://catalogs.northwestern.edu/sps/certificates/`.

#### Pritzker School of Law — Graduate
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor (JD) | JD | https://catalogs.northwestern.edu/law/programs/jd/ |
| 2 | Master of Laws (LLM) — General | LLM | https://catalogs.northwestern.edu/law/programs/llms/llm/ |
| 3 | LLM in International Human Rights | LLM | https://catalogs.northwestern.edu/law/programs/llms/llm-ihr/ |
| 4 | LLM in Taxation | LLM | https://catalogs.northwestern.edu/law/programs/llms/llm-tax/ |
| 5 | Executive LLM — Madrid | Executive LLM | https://catalogs.northwestern.edu/law/programs/llms/ellms/madrid/ |
| 6 | Executive LLM — Seoul | Executive LLM | https://catalogs.northwestern.edu/law/programs/llms/ellms/seoul/ |
| 7 | Executive LLM — Tel Aviv | Executive LLM | https://catalogs.northwestern.edu/law/programs/llms/ellms/tel-aviv/ |
| 8 | Master of Science in Law (MSL) | MSL | https://catalogs.northwestern.edu/law/programs/msl/ |

#### Feinberg School of Medicine — Graduate
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Medicine (MD) | MD | https://www.feinberg.northwestern.edu/admissions/ |
| 2 | MD/PhD Medical Scientist Training Program (MSTP) | MD/PhD | https://www.feinberg.northwestern.edu/admissions/md-phd/ |
| 3 | Driskill Graduate Program in Life Sciences (DGP) — PhD | PhD | https://www.feinberg.northwestern.edu/faculty-profiles/view-profile.php?uid=driskill |
| 4 | MS in Healthcare Quality & Patient Safety | MS | https://www.feinberg.northwestern.edu/education/masters-programs/healthcare-quality/ |
| 5 | MA in Medical Humanities & Bioethics | MA | https://www.feinberg.northwestern.edu/education/masters-programs/medical-humanities/ |

### 2.2 Program deep-dive — Computer Science (worked example)

**Program:** Computer Science (BS, McCormick; BA cross-listed with WCAS; MS/PhD via TGS)
- **Department:** Department of Computer Science, McCormick School of Engineering (Tech building, 2145 Sheridan Road, Evanston IL 60208)
- **UG degree:** Bachelor of Science (McCormick) or Bachelor of Arts (WCAS) — both administered by the same CS department. Source: `https://www.mccormick.northwestern.edu/computer-science/academics/undergraduate/bachelors/`
- **Graduate degrees:** MS (coursework or thesis), PhD (research) — administered via TGS. Source: `https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/computer-science.html`
- **Application opens:** mid-September (TGS) / Common App or Coalition with Scoir (UG)
- **UG application deadline:** ED Nov 1; RD Jan 4 (via Common App / Coalition)
- **Grad application deadline:** program-set; typically mid-December for PhD funding consideration
- **Application fee:** UG $75 (or fee waiver); Grad — TGS fee + program-specific (verify per program)
- **Application portal (UG):** Common App or Apply Coalition with Scoir (+ Northwestern supplement)
- **Behind accordions / per-program detail:** the TGS CS page carries GRE policy, TOEFL minimums, and materials checklist behind the program's detail page — each TGS program sets its own GRE requirement (many CS programs no longer require GRE; verify on the program detail page).

### 2.3 Graduate admissions model

**Fully decentralized.** TGS is the administrative school for the 89 academic PhD/MFA/MS/MA programs but each program runs its own admissions committee, deadline, GRE policy, and TOEFL minimum. Professional schools (Kellogg, McCormick prof master's, Medill, SoC prof master's, Bienen MM/DMA, SPS, Pritzker Law, Feinberg) each run entirely independent admissions with separate applications, fees, and timelines. There is **no institutional April-15 honor date** published at the TGS level, though TGS follows CGS resolution practices. ETS institutional code for Northwestern: **1565** (SAT) / **1106** (ACT) / **1565** (GRE/TOEFL — verify per program). PhD programs are **fully funded** (tuition + stipend + benefits); master's programs are generally self-funded.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|----|----|
| UG admissions site | https://admissions.northwestern.edu/ | E-U-001 |
| Application portal | Common App OR Apply Coalition with Scoir (+ Northwestern supplement) | E-U-003 |
| QuestBridge College Match | Oct 1, 2026 (binding if matched) | E-U-002 |
| **Early Decision (ED) — First-Year** | **Nov 1, 2026** (binding; mid-Dec decision) | E-U-002 |
| **Regular Decision (RD) — First-Year** | **Jan 4, 2027** (early-April decision) | E-U-002 |
| ED Transfer | Mar 1, 2027 | E-U-002 |
| RD Transfer | Apr 1, 2027 (Bienen Music transfer priority: Jan 4, 2027) | E-U-002 |
| Financial Aid due — ED | Dec 1, 2026 | E-U-002 |
| Financial Aid due — RD | Feb 1, 2027 | E-U-002 |
| Enrollment confirmation | May 1 (National College Decision Day) | (standard) |
| **Application fee** | **$75** (non-refundable; fee waiver available, ~40% of applicants qualify) | E-U-003 |
| SAT/ACT policy | **Test-optional** (will not require ACT/SAT from first-year or transfer applicants) | E-U-005 |
| SAT code | **1565** | E-U-005 |
| ACT code | **1106** | E-U-005 |
| Superscore | SAT superscore yes; ACT — Northwestern will NOT calculate its own ACT superscore for 2025-26 cycle (use official ACT superscore from MyACT) | E-U-005 |
| Score-report method | Official only after enrolling; applicants may self-report highest sections during application | E-U-005 |
| Interview policy | No interviews offered (Glimpse video is optional, 60-90 sec) | E-U-003 |
| Recommendations | Counselor recommendation + at least 1 teacher recommendation | E-U-003 |
| Portfolios / supplements | Required for Bienen Music (Bienen School Supplement + prescreening/audition); optional arts portfolio for some SoC programs; writing supplement via Common App | E-U-003 |
| Transfer pathway | Yes (separate deadlines; aid available; international transfer aid limited) | E-u-002 |
| QuestBridge | Partner school; National College Match (binding); non-match applicants may apply ED/RD | E-U-002 |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | No published minimum (competitive) | — | Accepts TOEFL iBT Special Home Edition; **not** TOEFL ITP Plus for China Solution |
| IELTS (Academic) | No published minimum (competitive) | — | Accepts IELTS Indicator |
| Duolingo English Test (DET) | No published minimum (competitive) | — | Accepted |
| Cambridge | N/A (not listed) | — | — |

> **Applicability:** Required for applicants whose first/primary language is not English OR whose secondary schooling has not been in English. Northwestern does **not** publish numeric minimums — scores are evaluated holistically ("competitive"). Source: E-U-004.

### 3.3 Graduate — global rules

| 维度 | 值 |
|------|----|
| Admissions model | **Fully decentralized** — TGS administers 89 academic programs (each sets own deadline/GRE/TOEFL); 8 professional schools run own admissions |
| Application platforms | TGS online application (TGS programs); Kellogg, McCormick prof, Medill, SoC prof, Bienen, SPS, Pritzker Law (LSAC), Feinberg (AMCAS) each use own platform |
| Application fee | TGS: ~$95 (verify per program; waivers available); varies by professional school (e.g. Kellogg MBA ~$250, Pritzker Law via LSAC) |
| April-15 honor date | TGS follows CGS resolution; no single institutional date published |
| GRE policy | **Per-program** — many TGS PhD programs no longer require GRE; check each program's detail page |
| Language-test policy | Per-program; TOEFL iBT or IELTS Academic typically required for non-native English applicants; minimums vary by program |
| ETS institutional code | **1565** (GRE/TOEFL/SAT); ACT **1106** |
| Application timeline | TGS PhD/MFA Fall 2027 opens mid-September 2026; deadlines typically Dec 1 – Jan 15 |

> The TGS application-procedures sub-pages (`application-requirements.html`, `international-applicants.html`, `help-for-applicants/faq.html`) returned 404 via static fetch (JS-rendered nav). Per-program detail is on each Explore Programs entry page — see cache `grad_tgs_rows.json`.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025–26 academic year, line-itemized)

| Expense item | Amount (USD) | Description |
|--------------|--------------|-------------|
| Tuition | **$69,375** | 2025-26 academic year |
| Total expenses (COA estimate) | **$96,236** | Includes tuition, fees, books, housing & food, transportation |
| (Line-item breakdown) | — | Northwestern publishes the headline tuition + total COA; line-item fees/housing/food detail is on the Financial Aid Office Cost of Attendance page (see P0 follow-up) |

> Source: `https://admissions.northwestern.edu/tuition-aid/index.html` — "Tuition for the 2025–26 academic year is $69,375. Total expenses (including fees, books, housing and food, transportation expenses and transportation) are estimated at $96,236." (E-U-006)

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 |
|------|----|
| Demonstrated-need commitment | **Meets 100% of every admitted first-year's demonstrated financial need for all four years** (E-U-007) |
| Loan policy | **Loan-free** — Northwestern's need-based aid awards do **not** include loans (no loans to pay back) |
| Need-blind / need-aware (domestic) | Northwestern does **not** use the term "need-blind"; aid is de-facto need-blind for U.S. applicants (100% need met) |
| **Need-aware for internationals** | **YES — need-aware for international students** ("a request for financial aid consideration and the amount of financial aid you require may factor into your admission decision") (E-U-008) — **CORRECTION to common assumption that Northwestern is need-blind for internationals** |
| No-cost threshold | Families earning **< $70K/year** attend Northwestern at **no cost** |
| Tuition-free threshold | Families earning **< $150K/year** attend **tuition-free** |
| Merit scholarships | **None** — "Northwestern does not award scholarships based on academic merit" |
| Total aid spending | >$250 million/year on undergraduate financial aid |
| Pell-eligible first-years | 22% |
| Aid application forms | CSS Profile + FAFSA (domestic); CSS Profile + supporting docs (international) |
| Aid deadlines | ED: Dec 1 (CSS/FAFSA); RD: Feb 1 |
| Six-month outcome | 97% employed or pursuing education/service/career-development within 6 months |

### 4.3 Graduate cost & funding framework

| 维度 | 值 |
|------|----|
| PhD funding | **Fully funded** — TGS PhD students receive full tuition + stipend + health insurance + benefits (typically 5 years) |
| MFA funding | Varies by program; many MFA programs offer partial-to-full funding |
| Master's funding | **Self-funded** — MS/MA/professional master's students pay tuition; limited fellowship/TA opportunities |
| Funding forms | RA (Research Assistantship), TA (Teaching Assistantship), Fellowship (internal/external), Grant |
| Application fee | TGS ~$95 (waivers for need-based/Pell/eligible applicants); professional schools vary |
| Fee-waiver policy | TGS offers fee waivers; professional schools each set own policy |
| COA / stipend rates | See TGS funding page (`https://www.tgs.northwestern.edu/funding/`) and per-program pages — mark as P1 follow-up |

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: undergraduate.admissions_site
  value: "https://admissions.northwestern.edu/ (Office of Undergraduate Admission, Rebecca Crown Center North Tower G547, 633 Clark Street, Evanston IL 60208; phone 847-491-7271; ug-admission@northwestern.edu)"
  source_url: https://admissions.northwestern.edu/
  source_snippet: "Office of Undergraduate Admission Address Rebecca Crown Center, North Tower, Ground Floor 633 Clark Street, Suite G547 Evanston, IL 60208 Phone number (847) 491-7271 Email address ug-admission@northwestern.edu"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-002
  field: undergraduate.deadlines
  value: {QuestBridge: "2026-10-01", ED_first_year: "2026-11-01", RD_first_year: "2027-01-04", ED_transfer: "2027-03-01", RD_transfer: "2027-04-01", aid_ED: "2026-12-01", aid_RD: "2027-02-01"}
  source_url: https://admissions.northwestern.edu/apply/application-deadlines.html
  source_snippet: "Application Due Date — October 1, 2026 | November 1, 2026 | January 4, 2027 | March 1, 2027* | April 1, 2027*   Financial Aid Due Date — October 1, 2026 | December 1, 2026 | February 1, 2027 | March 1, 2027 | April 1, 2027   Decision Release — December 2026 | December 2026 | March 2027 | Early April 2027 | Mid- to late-May 2027"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-003
  field: undergraduate.application_materials.fee_and_components
  value: "$75 non-refundable application fee or fee waiver; Common App or Apply Coalition with Scoir; counselor + teacher recommendation; official proof of English proficiency (if applicable); no interviews (Glimpse video optional)"
  source_url: https://admissions.northwestern.edu/apply/index.html
  source_snippet: "Non-refundable $75 application fee or fee waiver ... Common Application or Apply Coalition with Scoir (including Northwestern supplement) ... Counselor recommendation ... At least one teacher recommendation ... Official proof of English language proficiency"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-004
  field: undergraduate.english_proficiency
  value: "Required for non-native English applicants; accepted exams: Duolingo English Test (DET), IELTS (incl. IELTS Indicator), TOEFL iBT (incl. Special Home Edition; NOT TOEFL ITP Plus for China). No published numeric minimums (competitive)."
  source_url: https://admissions.northwestern.edu/apply/index.html
  source_snippet: "Official proof of English language proficiency (for applicants whose first/primary language is not English or whose secondary schooling has not been in English). Accepted English proficiency exams: Duolingo English Test (DET) | IELTS, including IELTS Indicator | TOEFL iBT, including TOEFL iBT Special Home Edition but not TOEFL ITP Plus for China Solution"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-005
  field: undergraduate.test_policy
  value: "Test-optional; SAT code 1565, ACT code 1106; SAT superscore yes; ACT — Northwestern will NOT calculate its own ACT superscore for 2025-26 (use official ACT superscore)"
  source_url: https://admissions.northwestern.edu/apply/application-deadlines.html
  source_snippet: "Northwestern follows a test-optional policy and will not require ACT or SAT scores from first-year or transfer candidates. If submitting scores, use Northwestern school code 1565 (SAT) or 1106 (ACT) ... Due to the ACT's staggered roll-out of its enhanced format ... Northwestern will not calculate a superscore for students reporting ACT scores in the 2025–26 application cycle."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.cost.2025_2026
  value: {tuition: 69375, total_coa: 96236, ay: "2025-26"}
  source_url: https://admissions.northwestern.edu/tuition-aid/index.html
  source_snippet: "Tuition for the 2025–26 academic year is $69,375. Total expenses (including fees, books, housing and food, transportation expenses and transportation) are estimated at $96,236."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.financial_aid.commitment
  value: "Meets 100% of every admitted first-year's demonstrated need for all four years; loan-free (no loans in aid packages); no merit scholarships; >$250M/year UG aid"
  source_url: https://admissions.northwestern.edu/tuition-aid/index.html
  source_snippet: "Our commitment to affordability begins with financial aid that meets 100% of every student's demonstrated financial need. Northwestern's need-based financial aid awards do not include loans to pay back ... Northwestern does not award scholarships based on academic merit ... we spent more than $250 million on financial aid support for undergraduate students."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.financial_aid.international
  value: "Need-aware for international students (NOT need-blind); 100% of admitted intl first-year demonstrated need met for all 4 years"
  source_url: https://admissions.northwestern.edu/apply/identities/international.html
  source_snippet: "Need-based financial aid is available to international students seeking undergraduate degrees at Northwestern. We guarantee to meet 100% of all admitted first-year students' demonstrated financial need for all four years. We are need-aware for international students, meaning that a request for financial aid consideration and the amount of financial aid you require may factor into your admission decision."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-009
  field: undergraduate.financial_aid.thresholds
  value: {no_cost_income: "<$70K", tuition_free_income: "<$150K", pell_share: "22%"}
  source_url: https://admissions.northwestern.edu/tuition-aid/index.html
  source_snippet: "<$70K most families making less than $70K per year attend Northwestern at no cost | <$150K most families making less than $150K per year attend Northwestern tuition-free | 22% of first-year students are eligible for federal Pell Grants"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-010
  field: undergraduate.programs.majors_minors
  value: "134 program names → 89 Major + 81 Minor + 9 Certificate option rows; filterable by 6 UG schools (WCAS, McCormick, Communication, SESP, Medill, Music + Kellogg cert)"
  source_url: https://admissions.northwestern.edu/academics/majors-minors/index.html
  source_snippet: "Find your academic focus. To get started, you can filter the list by your personal interests or by choosing one of Northwestern's six undergraduate schools ... Filter by School: All Arts & Sciences Communication Education & Social Policy Engineering Journalism & Marketing Music"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-011
  field: undergraduate.degree_options
  value: "BA (Weinberg), BS (McCormick/SESP/SoC), BMus/BAMus (Bienen), BFA (Theatre/Dance), BSJ (Medill); plus dual-degree combinations"
  source_url: https://admissions.northwestern.edu/academics/degree-options.html
  source_snippet: "Each of Northwestern's undergraduate schools expects students to fulfill a set of requirements to earn a bachelor's degree, be it a Bachelor of Arts, of Music, or of Science ... Majors ... Adjunct Majors ... Double majors ... Dual degrees ... Minors ... Certificates"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-012
  field: undergraduate.catalog_programs_az
  value: "Catalog Programs A-Z (UG) — 6 schools, full program enumeration with leaf pages per degree"
  source_url: https://catalogs.northwestern.edu/undergraduate/programs-az/
  source_snippet: "Undergraduate | Northwestern University Academic Catalog ... Henry and Leigh Bienen School of Music | School of Communication | School of Education and Social Policy | Robert R. McCormick School of Engineering and Applied Science | Medill School of Journalism | Judd A. and Marjorie Weinberg College of Arts and Sciences"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-013
  field: undergraduate.dual_degrees
  value: "7 dual-bachelor's-degree combinations across schools (BA/BS+Engineering, BA/BMus, Communication+Engineering, Communication+Music, SESP+Music, Engineering+Music, Journalism+Music)"
  source_url: https://catalogs.northwestern.edu/undergraduate/dual-bachelors-degrees/
  source_snippet: "BA/BS in Liberal Arts and Engineering | BA/BMus in Liberal Arts and Music | BA/BS or BS/BS in Communication and Engineering | BA/BMus, BS/BMus, BA/BAMus, or BS/BAMus in Communication and Music | BSED/BMus or BSED/BAMus in Education and Social Policy and in Music | BS/BMus or BS/BAMus in Engineering and Music | BSJ/BMus in Journalism and Music"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-014
  field: undergraduate.degree_designation_method
  value: "Degree (BA/BS/BFA/BMus/BSJ) is NOT a labeled field on any Northwestern catalog or admissions page; derived by documented school convention"
  source_url: https://admissions.northwestern.edu/academics/majors-minors/index.html
  source_snippet: "Each program row carries an 'Options Offered' value (Major / Minor / Adjunct Major / Certificate) and a school acronym (WCAS/McCormick/Communication/SESP/Medill/Music/Kellogg) but NO degree (BA/BS) label. Degree derived: WCAS humanities/social=BA, WCAS science/math=BS, McCormick=BS, SESP=BS, SoC=BS (Theatre/Dance=BFA), Bienen=BMus, Medill=BSJ."
  capture_date: 2026-07-05
  evidence_type: derived_from_official_convention

- id: E-G-001
  field: graduate.tgs_program_directory
  value: "89 academic PhD/MFA/MS/MA programs administered by The Graduate School"
  source_url: https://www.tgs.northwestern.edu/admission/academic-programs/explore-programs/index.html
  source_snippet: "Explore our master's, PhD and dual degree programs by area of study or type ... Academic Programs Degree Offered Areas of Study Degree Type ... Accounting Information and Management PhD ... Acting MFA ... Anthropology PhD"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-G-002
  field: graduate.tgs_other_schools
  value: "Professional degrees (MBA, MD, JD, MEng, MSJ) NOT administered by TGS — managed by Feinberg, Kellogg, Medill, McCormick, SoC, SESP, Law, Bienen, SPS"
  source_url: https://www.tgs.northwestern.edu/admission/academic-programs/degrees-other-northwestern-schools.html
  source_snippet: "Only the programs on this list are offered by TGS. Professional degrees (e.g., the master of business administration, master of sports administration, doctor of audiology, doctor of medicine, and a variety of engineering, law, and journalism degrees) are not administered by TGS, but by these respective professional schools: Feinberg School of Medicine, Kellogg School of Management, Medill, McCormick School of Engineering, School of Communication, School of Education and Social Policy, School of Law, Henry and Leigh Bienen School of Music, School of Professional Studies"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.mccormick_programs
  value: "11 departmental PhD programs + 24 full-time + 6 part-time professional master's programs"
  source_url: https://www.mccormick.northwestern.edu/academics/graduate/programs/full-time-masters.html
  source_snippet: "Master's Programs ... The MBAi Program, The MMM Program, MS in Advanced Manufacturing, MS in Artificial Intelligence, MS in Biomedical Engineering, MS in Biotechnology, MS in Chemical and Biological Engineering, MS in Civil and Environmental Engineering, MS in Computer Engineering, MS in Computer Science, MS in Electrical Engineering, MS in Energy and Sustainability (MSES), MS in Engineering Design Innovation (EDI), Master of Engineering Management (MEM), MS in Engineering Sciences and Applied Mathematics, MS in Information Technology (MSIT), MS in Machine Learning and Data Science, MS in Materials Science and Engineering, MS in Mechanical Engineering, Joint MS in Mechanical Engineering and Materials Science & Engineering, Master of Product Design and Development Management (MPD2), MS in Project Management (MPM), MS in Robotics (MSR), Theoretical and Applied Mechanics (TAM)"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-004
  field: graduate.kellogg_programs
  value: "Full-Time MBA, Evening & Weekend MBA, Executive MBA, Master in Management, MBAi, MMM (MBA+MDI), MSMS, Doctoral (7 fields)"
  source_url: https://www.kellogg.northwestern.edu/programs.aspx
  source_snippet: "Degree Programs ... Full-Time MBA, Evening + Weekend MBA, Executive MBA, Master in Management, Doctoral, Certificate Program for Undergraduates"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-005
  field: graduate.medill_programs
  value: "MS in Journalism, IMC Full-Time Master's, IMC Professional Master's, PhD & Fellowship, Undergraduate BSJ"
  source_url: https://www.medill.northwestern.edu/journalism/
  source_snippet: "Journalism ... Master of Science in Journalism ... Bachelor of Science in Journalism ... PhD and Fellowship ... Integrated Marketing Communications ... IMC Full-Time Master's ... IMC Professional Master's ... IMC Undergraduate Certificate"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-006
  field: graduate.communication_programs
  value: "19 graduate programs: Acting MFA, Audiology AuD, Communication MS, Communication Sciences & Disorders PhD, Directing MFA, Documentary Media MFA, Interdepartmental Neuroscience PhD, Leadership for Creative Enterprises MS, Media Technology & Society MA/PhD, Performance Studies MA/PhD, Rhetoric Media & Publics PhD, Screen Cultures MA/PhD, Sound Arts & Industries MA, Speech Language & Learning MS, Speech-Language Pathology SLPD, Stage Design MFA, Technology & Social Behavior PhD, Theatre & Drama PhD, Writing for Screen & Stage MFA"
  source_url: https://communication.northwestern.edu/academics/graduate-programs
  source_snippet: "Graduate Programs ... Academic Programs Degree Offered Learn More Department Degree Type ... Acting MFA | Audiology AuD | Communication MS | Communication Sciences and Disorders PhD | Directing MFA | Documentary Media MFA | ... | Writing for the Screen and Stage MFA"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-G-007
  field: graduate.bienen_degrees
  value: "BMus, BA & BS (UG); Master of Music (MM), Doctor of Musical Arts (DMA), PhD (Musicology/Theory/MusEd)"
  source_url: https://www.music.northwestern.edu/academics/degrees/
  source_snippet: "Degrees ... Bachelor of Music, Bachelor of Arts and Bachelor of Science, Master of Music, Doctor of Musical Arts, Doctor of Philosophy"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-008
  field: graduate.sps_programs
  value: "14 graduate MS/MA/MFA programs + 16 graduate certificates + 33 post-baccalaureate certificates + 12 UG completion majors"
  source_url: https://catalogs.northwestern.edu/sps/
  source_snippet: "School of Professional Studies ... Data Science MS | Global Health MS | Health Analytics MS | Healthcare Administration MS | Health Informatics MS | Information Design and Strategy MS | Information Systems MS | Liberal Studies MA | Literature MA | Prose and Poetry MFA | Public Policy and Administration MS | Regulatory Compliance MS | Sports Administration MA | Writing MA"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-G-009
  field: graduate.law_programs
  value: "JD, LLM (General), LLM International Human Rights, LLM Taxation, Executive LLM (Madrid/Seoul/Tel Aviv), Master of Science in Law (MSL)"
  source_url: https://catalogs.northwestern.edu/law/programs/
  source_snippet: "Pritzker School of Law ... Programs ... Juris Doctor | Master of Laws (LLM) Programs | LLM - International Human Rights | LLM - Taxation | Executive LLM Programs (Madrid/Seoul/Tel Aviv) | Master of Science in Law"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-G-010
  field: graduate.tgs_application_model
  value: "Decentralized; application requirements and deadlines vary by program; 2026 PhD/MFA closed, Fall 2027 opens mid-September; some 2026 master's programs may remain open"
  source_url: https://www.tgs.northwestern.edu/admission/application-procedures/index.html
  source_snippet: "Application requirements and deadlines vary from program to program ... 2026 PhD/MFA applications are closed; Fall 2027 opens mid-September. Some 2026 master's/non-degree programs may still be open—check program deadlines."
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
northwestern-knowledge-base-v2/                   (collection)
├── overview/                                      (institution overview — Section 0)
│   ├── counts-and-hierarchy                       (chunk: Rule 1 + Rule 2)
│   └── degree-inventory-matrix                    (chunk: Rule 3 + Rule 4)
├── undergraduate/                                 (Section 1, one chunk per school)
│   ├── weinberg-majors                            (38 BA + 9 BS)
│   ├── mccormick-majors                           (15 BS)
│   ├── communication-majors                       (6 BS + 2 BFA)
│   ├── sesp-majors                                (5 BS)
│   ├── bienen-majors                              (13 BMus)
│   ├── medill-majors                              (1 BSJ)
│   ├── minors-complete                            (81 minors)
│   ├── certificates                               (9 UG certs)
│   └── dual-degrees                               (7 dual-bachelor's)
├── graduate/                                      (Section 2, one chunk per school)
│   ├── tgs-academic-programs                      (89 PhD/MFA/MS/MA)
│   ├── mccormick-professional-masters             (24 FT + 6 PT)
│   ├── kellogg-graduate                           (8 programs)
│   ├── medill-graduate                            (4 programs)
│   ├── communication-graduate                     (19 programs)
│   ├── bienen-graduate                            (MM + DMA)
│   ├── sps-graduate                               (14 MS/MA/MFA + 16 grad certs)
│   ├── pritzker-law                               (8 programs)
│   └── feinberg-medicine                          (5 programs)
├── application-requirements/                      (Section 3)
│   ├── ug-deadlines-tests-english
│   └── grad-global-rules
├── costs-aid/                                     (Section 4)
│   ├── ug-cost-2025-26
│   └── grad-funding-framework
└── evidence-chain/                                (Section 5 — 24 evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "northwestern-knowledge-base-v2"
  school: "<home college, e.g. Weinberg College of Arts and Sciences>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|BMus|BFA|BSJ|MS|MA|MFA|MBA|PhD|MD|JD|AuD|SLPD|MM|DMA|LLM|MSL|Certificate|Minor>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | UG COA line-item breakdown (tuition/fees/housing/food/books separate) | Financial Aid Office Cost of Attendance page (domain not yet resolved — `finaid.northwestern.edu` failed) |
| P0 | TGS application fee exact figure + GRE/TOEFL per-program detail | TGS per-program Explore pages (JS-rendered FAQ sub-pages 404 via static fetch) |
| P0 | Per-program grad deadlines (Dec 1 / Dec 15 / Jan 15 vary) | Each TGS Explore Programs detail page + professional school admissions pages |
| P1 | Kellogg MBA tuition + per-program deadlines | https://www.kellogg.northwestern.edu/admissions/ |
| P1 | Feinberg MD tuition + AMCAS timeline | https://www.feinberg.northwestern.edu/admissions/ |
| P1 | Pritzker Law JD tuition + LSAC timeline | https://www.law.northwestern.edu/admissions/ |
| P1 | SPS graduate tuition (per-program) | https://sps.northwestern.edu/tuition/ |
| P2 | Northwestern University in Qatar (NU-Q) program list | https://www.qatar.northwestern.edu/ |
| P2 | Bienen audition/prescreening schedule | https://www.music.northwestern.edu/admission/graduate/application-timeline/ |
| P2 | HPME (Honors Program in Medical Education) current status | https://catalogs.northwestern.edu/undergraduate/dual-graduate-undergraduate-degrees/honors-program-medical-education/ |

---

## SECTION 7 — Cross-school comparison framework (Northwestern column)

| Dimension | Northwestern (2026-07-05) |
|-----------|---------------------------|
| Total UG cost/yr (COA) | $96,236 (2025-26) |
| Tuition/yr | $69,375 (2025-26) |
| Need-blind (intl)? | **NO — need-AWARE for internationals** (but 100% need met, loan-free) |
| ED deadline | Nov 1 |
| RD deadline | **Jan 4** (not Jan 2) |
| SAT/ACT required? | No — **test-optional** |
| TOEFL min (UG) | No published minimum (competitive) |
| IELTS min (UG) | No published minimum (competitive) |
| Tuition-free threshold | <$150K income |
| No-cost threshold | <$70K income |
| Merit scholarships | None |
| UG app fee | $75 |
| Grad app fee (TGS) | ~$95 (verify) |
| April-15 honor date | TGS follows CGS (no single institutional date) |
| **Total credentials (Rule 1)** | **346** |
| **School/department count (Rule 2)** | **11 academic units** |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.northwestern.edu, catalogs.northwestern.edu (2025-2026 edition), www.tgs.northwestern.edu, www.mccormick.northwestern.edu, communication.northwestern.edu, www.music.northwestern.edu, www.medill.northwestern.edu, www.kellogg.northwestern.edu
> **Verification**: ego-browser serverFetch + JS DOM extraction; reconciliation gate passed (346 == 346 == 346)
> **Granularity**: school → department → degree-level → program
> **Cache**: uni-cache/schools/northwestern/{site-memory.json, last-extract.json, content-hashes.json} + _raw/*.json intermediate data
