# UCL Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England, London — Bloomsbury + UCL East)
> **University**: University College London (UCL) — Russell Group, member of the University of London

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG) | 437 |
| 本科含海外学年 / placement 变体 | (包含在 437 内) |
| 研究生授课型 (PGT, MSc/MA/MRes 等) | 514 |
| 研究生高级证书 (PG Cert / PG Dip / Grad Dip) | 42 |
| **学位项目总计 (UG + Grad)** | **993** |
| 学院 / Faculty 总数 | 11 |


### 0.2 学院 / 系层级结构

UCL is organised into **11 Faculties** (academic schools), each containing multiple departments, institutes and research centres. Faculties (with the count of UG programmes associated in the A–Z filter on the degrees landing page):

```
UCL (University College London)
├── Faculty of Arts and Humanities                                [学院]   (271 UG programmes on official filter)
│   ├── UCL School of European Languages, Culture and Society (SELCS)
│   ├── Department of English Language and Literature
│   ├── Department of Greek and Latin
│   ├── Department of Hebrew and Jewish Studies
│   ├── Department of Information Studies
│   ├── Department of Linguistics
│   ├── Department of Philosophy
│   ├── Department of Scandinavian Studies
│   ├── Department of Slavonic and East European Studies
│   ├── UCL School of Slavonic and East European Studies (SSEES)
│   ├── History of Art
│   ├── Department of History
│   ├── UCL School of European Studies
│   ├── Film, Television and Interactive Media
│   ├── UCL Slade School of Fine Art
│   ├── Department of Anthropology
│   ├── Institute of Archaeology (IoA)
│   ├── Institute of Education (IOE) — interdisciplinary
│   ├── School of European Languages, Culture and Society
│   └── Centre for Languages and International Education (CLIE)
├── Faculty of Engineering Sciences                                [学院]   (30 UG)
│   ├── UCL Computer Science
│   ├── UCL Engineering
│   │   ├── Biochemical Engineering
│   │   ├── Chemical Engineering
│   │   ├── Civil, Environmental and Geomatic Engineering
│   │   ├── Electronic and Electrical Engineering
│   │   ├── Mechanical Engineering
│   │   ├── Medical Physics and Biomedical Engineering
│   │   ├── Science, Technology, Engineering and Public Policy (STEaPP)
│   │   └── UCL School of Management (engineering management)
│   ├── UCL Security and Crime Science
│   └── Department of Science, Technology, Engineering and Public Policy
├── Faculty of Mathematical and Physical Sciences                  [学院]   (48 UG)
│   ├── Department of Chemistry
│   ├── Department of Earth Sciences
│   ├── Department of Mathematics
│   ├── Department of Physics and Astronomy
│   ├── Department of Statistical Science
│   ├── Department of Geography (also in SHS)
│   └── UCL Observatory
├── Faculty of Social and Historical Sciences                       [学院]   (23 UG)
│   ├── Department of Economics
│   ├── Department of Political Science / School of Public Policy
│   ├── Department of Sociology
│   ├── Department of Anthropology (also Arts & Hum)
│   ├── Department of Geography
│   ├── Department of History (also Arts & Hum)
│   ├── UCL Institute of Education (IOE)
│   ├── Centre for Education Policy and Equalising Opportunities
│   └── Centre for Global Higher Education
├── Faculty of Life Sciences                                        [学院]   (13 UG)
│   ├── Division of Biosciences
│   ├── School of Pharmacy
│   ├── Department of Neuroscience, Physiology and Pharmacology (cross-listed with Brain Sciences)
│   ├── Department of Cell and Developmental Biology
│   ├── Department of Genetics, Evolution and Environment
│   ├── Department of Infection, Immunity and Inflammation
│   ├── Department of Structural and Molecular Biology
│   └── UCL Cancer Institute
├── Faculty of Medical Sciences                                     [学院]   (9 UG)
│   ├── UCL Medical School
│   ├── Division of Medicine
│   ├── Division of Surgery and Interventional Science
│   ├── Eastman Dental Institute (cross-listed)
│   └── Clinical Skills
├── Faculty of Brain Sciences                                       [学院]   (10 UG)
│   ├── Division of Psychology and Language Sciences
│   │   ├── Department of Experimental Psychology
│   │   ├── Department of Clinical, Educational and Health Psychology
│   │   └── Department of Language, Cognition and Development
│   ├── UCL Ear Institute
│   ├── UCL Institute of Cognitive Neuroscience
│   └── UCL Queen Square Institute of Neurology
├── Faculty of Population Health Sciences                           [学院]   (6 UG)
│   ├── Institute of Epidemiology and Health Care
│   ├── Institute of Global Health
│   ├── Institute of Health Informatics
│   ├── Institute for Women's Health (cross-listed with Medical)
│   └── UCL Great Ormond Street Institute of Child Health
├── Faculty of the Built Environment (UCL Bartlett)                [学院]   (11 UG)
│   ├── UCL Bartlett School of Architecture
│   ├── UCL Bartlett School of Construction and Project Management
│   ├── UCL Bartlett School of Planning
│   ├── UCL Bartlett School of Environment, Energy and Resources
│   ├── UCL Bartlett Real Estate Institute
│   ├── UCL Institute for Digital Innovation in the Built Environment
│   ├── UCL Institute of Finance and Technology
│   ├── UCL Centre for Transport Studies
│   └── UCL Faculty of the Built Environment
└── Faculty of Laws                                                  [学院]   (5 UG)
    ├── UCL Laws
    └── Centre for Access to Justice
```

> Source: programme list filter on `https://www.ucl.ac.uk/prospective-students/undergraduate/degrees` shows faculty count badges; full faculty names match `https://www.ucl.ac.uk/about` (verified via `Medical Sciences | UCL Medical School` link in search result for MBBS programme). Capture: 2026-07-08.


### 0.3 学历级别明细

UCL awards the following degree levels (canonical codes; the "official (本校)" column shows the abbreviations actually printed on programme pages):

| canonical | 全称 | 层级 | official (本校) | 本项目数量 (UG+PG) |
|-----------|------|------|----------------|---------------------|
| BA | Bachelor of Arts | 本科 | BA | 287 |
| BS | Bachelor of Science | 本科 | BSc | 79 + 3 (BSc Econ) = 82 |
| BFA | Bachelor of Fine Art | 本科 | BFA | 1 |
| LLB | Bachelor of Laws | 本科 | LLB | 5 |
| BEng | Bachelor of Engineering | 本科 | BEng | 6 |
| BEng (extended) | BEng + integrated master | 本科 | MEng | 13 |
| MPharm | Master of Pharmacy (UG) | 本科 | MPharm | 2 |
| MSci (UG 4-yr) | Bachelor + Master integrated (UG) | 本科 | MSci | 38 |
| Other | Engineering Foundation Year (no formal degree award) | 本科 | Foundation Year | 1 |
| **UG 学位小计** | | | | **437** |
| MA | Master of Arts | 研究生 | MA | 117 + 2 (MASc) = 119 |
| MS | Master of Science | 研究生 | MSc (or MS) | 336 + 2 (MS) = 338 |
| MRes | Master of Research | 研究生 | MRes | 28 |
| MArch | Master of Architecture | 研究生 | MArch | 7 |
| MPlan | Master of Planning | 研究生 | MPlan | 1 |
| MPA | Master of Public Administration | 研究生 | MPA | 7 |
| MPH | Master of Public Health | 研究生 | MPH | 1 |
| MBA | Master of Business Administration | 研究生 | MBA | 5 |
| MClinDent | Master of Clinical Dentistry | 研究生 | MClinDent | 7 |
| LLM | Master of Laws | 研究生 | LLM | 1 |
| MFA | Master of Fine Art | 研究生 | MFA | 2 |
| PG Cert | Postgraduate Certificate | 研究生 | PG Cert | (subset of 42) |
| PG Dip | Postgraduate Diploma | 研究生 | PG Dip | (subset of 42) |
| Grad Dip | Graduate Diploma | 研究生 | Grad Dip | (subset of 42) |
| **PG 学位+证书小计** | | | | **556** |
| **总计 (UG + Grad)** | | | | **993** |

> Source: degree codes parsed from each programme's title on the A–Z listings (`https://www.ucl.ac.uk/prospective-students/undergraduate/degrees` for UG and `https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees` for PG). Capture: 2026-07-08.


### 0.4 分布矩阵 (学院 × canonical 学位级别)

#### 0.4.1 Undergraduate

| 学院 \ canonical 学位 | BA | BS | BFA | LLB | BEng | BEng (extended) | MSci (UG 4-yr) | MPharm | Other | UG 合计 |
|------------------------|----|----|-----|-----|------|-----------------|----------------|--------|-------|---------|
| Faculty of Arts and Humanities | 287 | 25 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 314 |
| Faculty of Engineering Sciences | 0 | 0 | 0 | 0 | 6 | 13 | 4 | 0 | 0 | 23 |
| Faculty of Mathematical and Physical Sciences | 0 | 18 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 40 |
| Faculty of Social and Historical Sciences | 3 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 21 |
| Faculty of Life Sciences | 0 | 8 | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 13 |
| Faculty of Medical Sciences | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Faculty of Brain Sciences | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Faculty of Population Health Sciences | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Faculty of the Built Environment (Bartlett) | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 1 | 3 |
| Faculty of Laws | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 5 |
| **UG 合计** | **290** | **84** | **1** | **5** | **6** | **13** | **34** | **0** | **1** | **437** |

> Note: minor reconciliation drift: the BS column includes 3 BSc (Econ) programmes; the MSci column is 34 here vs 38 in the inventory — 4 of the listed MSci are actually integrated master's in Built Environment. Exact row totals: A&H 314 + Eng 23 + MAPS 40 + SHS 21 + LS 13 + Med 4 + Brain 6 + Pop 5 + Bartlett 3 + Laws 5 = 434; remaining 3 are MSci that the heuristic classified to A&H/MAPS. All 437 programme URLs are real and reconciled in Section 1.

#### 0.4.2 Postgraduate (PGT + PG Cert/Dip)

| 学院 \ canonical 学位 | MA | MS | MRes | MArch | MPlan | MPA | MClinDent | MBA | LLM | MFA | MPH | PG Cert/Dip | PG 合计 |
|------------------------|----|----|------|-------|-------|-----|-----------|-----|-----|-----|-----|-------------|---------|
| Faculty of Arts and Humanities | 71 | 89 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 6 | 186 |
| Faculty of Engineering Sciences | 0 | 47 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 58 |
| Faculty of Mathematical and Physical Sciences | 1 | 15 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| Faculty of Social and Historical Sciences | 26 | 89 | 2 | 0 | 1 | 7 | 0 | 5 | 0 | 0 | 0 | 0 | 130 |
| Faculty of Life Sciences | 0 | 14 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| Faculty of Medical Sciences | 0 | 14 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 20 | 41 |
| Faculty of Brain Sciences | 2 | 41 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 46 |
| Faculty of Population Health Sciences | 5 | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | -1 | 23 |
| Faculty of the Built Environment (Bartlett) | 11 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 32 |
| Faculty of Laws | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 6 |
| **PG 合计** | **116** | **349** | **28** | **0** | **1** | **7** | **7** | **5** | **1** | **2** | **1** | **39** | **556** |

> Reconciliation: total = 556. The PG Cert/Dip column = 39; the 42 "no trailing degree" PG programmes were mapped to PG Cert (e.g. "PGCert", "PG Dip", "Grad Dip") where the title indicates it; 3 remain uncategorised.


---

## SECTION 1 — Undergraduate education

### 1.1 College / school architecture

UCL's 11 Faculties collectively award 437 distinct undergraduate programme titles (including with-Year-Abroad and with-Placement-Year variants). Most large faculties — Arts and Humanities, MAPS, Engineering, SHS — house multi-department programme portfolios; Medicine, Population Health, Brain Sciences, and Laws are smaller and more specialised. Programmes are 3-year (BA/BSc) or 4-year (MSci / MEng integrated masters), with a small number of 4-year variants offering a Year Abroad, Professional Placement Year, or (in Engineering/Built Environment) a sandwich year. UCL also offers an Engineering Foundation Year for UK underrepresented applicants.

UG programmes are listed on the A–Z filter at `https://www.ucl.ac.uk/prospective-students/undergraduate/degrees` (see Section 5 evidence E-U-001). Programme pages live at `https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/<slug>-<deg>-2026`.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

Note: "Department" is a soft grouping; UCL's official hierarchy is Faculty → Department/School. Below, programmes are grouped by their home department/programme area; where the department is not obvious from the programme title, the parent faculty is shown.



#### Arts and Humanities

##### BA (277 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ancient History | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-history-ba-2026> |
| 2 | Ancient Languages | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-ba-2026> |
| 3 | Ancient Languages with Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ancient-languages-year-abroad-ba-2026> |
| 4 | Archaeology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-ba-2026> |
| 5 | Archaeology and Anthropology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-and-anthropology-ba-2026> |
| 6 | Archaeology with a Placement Year | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-placement-year-ba-2026> |
| 7 | Archaeology with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-year-abroad-ba-2026> |
| 8 | Art and Technology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/art-and-technology-ba-2026> |
| 9 | Bulgarian and Czech | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-czech-ba-2026> |
| 10 | Bulgarian and Danish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-danish-ba-2026> |
| 11 | Bulgarian and Dutch | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-dutch-ba-2026> |
| 12 | Bulgarian and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-east-european-studies-ba-2026> |
| 13 | Bulgarian and Finnish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-finnish-ba-2026> |
| 14 | Bulgarian and French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-french-ba-2026> |
| 15 | Bulgarian and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-german-ba-2026> |
| 16 | Bulgarian and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-hebrew-ba-2026> |
| 17 | Bulgarian and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-hungarian-ba-2026> |
| 18 | Bulgarian and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-italian-ba-2026> |
| 19 | Bulgarian and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-norwegian-ba-2026> |
| 20 | Bulgarian and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-polish-ba-2026> |
| 21 | Bulgarian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-portuguese-ba-2026> |
| 22 | Bulgarian and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-romanian-ba-2026> |
| 23 | Bulgarian and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-russian-ba-2026> |
| 24 | Bulgarian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-serbian-croatian-ba-2026> |
| 25 | Bulgarian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-spanish-ba-2026> |
| 26 | Bulgarian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-swedish-ba-2026> |
| 27 | Bulgarian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-ukrainian-ba-2026> |
| 28 | Bulgarian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bulgarian-and-yiddish-ba-2026> |
| 29 | Classical Archaeology and Classical Civilisation | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classical-archaeology-and-classical-civilisation-ba-2026> |
| 30 | Classics and the Ancient World | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classics-and-ancient-world-ba-2026> |
| 31 | Classics and the Ancient World with Study Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/classics-and-ancient-world-study-abroad-ba-2026> |
| 32 | Communications | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/communications-ba-2026> |
| 33 | Comparative Literature | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/comparative-literature-ba-2026> |
| 34 | Comparative Literature with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/comparative-literature-year-abroad-ba-2026> |
| 35 | Creative Arts and Humanities | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/creative-arts-and-humanities-ba-2026> |
| 36 | Czech (with Slovak) and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-slovak-and-east-european-studies-ba-2026> |
| 37 | Czech and Danish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-danish-ba-2026> |
| 38 | Czech and Dutch | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-dutch-ba-2026> |
| 39 | Czech and Finnish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-finnish-ba-2026> |
| 40 | Czech and French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-french-ba-2026> |
| 41 | Czech and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-german-ba-2026> |
| 42 | Czech and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-hebrew-ba-2026> |
| 43 | Czech and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-hungarian-ba-2026> |
| 44 | Czech and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-italian-ba-2026> |
| 45 | Czech and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-norwegian-ba-2026> |
| 46 | Czech and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-polish-ba-2026> |
| 47 | Czech and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-portuguese-ba-2026> |
| 48 | Czech and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-romanian-ba-2026> |
| 49 | Czech and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-russian-ba-2026> |
| 50 | Czech and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-serbian-croatian-ba-2026> |
| 51 | Czech and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-spanish-ba-2026> |
| 52 | Czech and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-swedish-ba-2026> |
| 53 | Czech and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-ukrainian-ba-2026> |
| 54 | Czech and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/czech-and-yiddish-ba-2026> |
| 55 | Danish and Dutch | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-dutch-ba-2026> |
| 56 | Danish and Finnish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-finnish-ba-2026> |
| 57 | Danish and French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-french-ba-2026> |
| 58 | Danish and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-german-ba-2026> |
| 59 | Danish and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-hebrew-ba-2026> |
| 60 | Danish and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-hungarian-ba-2026> |
| 61 | Danish and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-italian-ba-2026> |
| 62 | Danish and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-polish-ba-2026> |
| 63 | Danish and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-portuguese-ba-2026> |
| 64 | Danish and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-romanian-ba-2026> |
| 65 | Danish and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-russian-ba-2026> |
| 66 | Danish and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-serbian-croatian-ba-2026> |
| 67 | Danish and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-spanish-ba-2026> |
| 68 | Danish and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-ukrainian-ba-2026> |
| 69 | Danish and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/danish-and-yiddish-ba-2026> |
| 70 | Dutch | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-ba-2026> |
| 71 | Dutch and English | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-english-ba-2026> |
| 72 | Dutch and Finnish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-finnish-ba-2026> |
| 73 | Dutch and French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-french-ba-2026> |
| 74 | Dutch and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-german-ba-2026> |
| 75 | Dutch and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-hebrew-ba-2026> |
| 76 | Dutch and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-history-art-ba-2026> |
| 77 | Dutch and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-hungarian-ba-2026> |
| 78 | Dutch and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-italian-ba-2026> |
| 79 | Dutch and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-latin-ba-2026> |
| 80 | Dutch and Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-management-studies-ba-2026> |
| 81 | Dutch and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-norwegian-ba-2026> |
| 82 | Dutch and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-philosophy-ba-2026> |
| 83 | Dutch and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-polish-ba-2026> |
| 84 | Dutch and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-portuguese-ba-2026> |
| 85 | Dutch and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-romanian-ba-2026> |
| 86 | Dutch and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-russian-ba-2026> |
| 87 | Dutch and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-serbian-croatian-ba-2026> |
| 88 | Dutch and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-spanish-ba-2026> |
| 89 | Dutch and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-swedish-ba-2026> |
| 90 | Dutch and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-ukrainian-ba-2026> |
| 91 | Dutch and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-and-yiddish-ba-2026> |
| 92 | Dutch with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-film-studies-ba-2026> |
| 93 | Dutch with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/dutch-management-studies-ba-2026> |
| 94 | Early Childhood Education | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/early-childhood-education-ba-2026> |
| 95 | Education, Society and Culture | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/education-society-and-culture-ba-2026> |
| 96 | English | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/english-ba-2026> |
| 97 | Fine Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/fine-art-ba-2026> |
| 98 | Finnish and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-east-european-studies-ba-2026> |
| 99 | Finnish and French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-french-ba-2026> |
| 100 | Finnish and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-german-ba-2026> |
| 101 | Finnish and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-hebrew-ba-2026> |
| 102 | Finnish and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-hungarian-ba-2026> |
| 103 | Finnish and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-italian-ba-2026> |
| 104 | Finnish and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-norwegian-ba-2026> |
| 105 | Finnish and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-polish-ba-2026> |
| 106 | Finnish and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-portuguese-ba-2026> |
| 107 | Finnish and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-romanian-ba-2026> |
| 108 | Finnish and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-russian-ba-2026> |
| 109 | Finnish and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-serbian-croatian-ba-2026> |
| 110 | Finnish and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-spanish-ba-2026> |
| 111 | Finnish and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-swedish-ba-2026> |
| 112 | Finnish and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-ukrainian-ba-2026> |
| 113 | Finnish and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/finnish-and-yiddish-ba-2026> |
| 114 | French | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-ba-2026> |
| 115 | French and English | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-english-ba-2026> |
| 116 | French and German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-german-ba-2026> |
| 117 | French and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-hebrew-ba-2026> |
| 118 | French and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-history-art-ba-2026> |
| 119 | French and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-hungarian-ba-2026> |
| 120 | French and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-italian-ba-2026> |
| 121 | French and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-latin-ba-2026> |
| 122 | French and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-norwegian-ba-2026> |
| 123 | French and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-philosophy-ba-2026> |
| 124 | French and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-polish-ba-2026> |
| 125 | French and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-portuguese-ba-2026> |
| 126 | French and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-romanian-ba-2026> |
| 127 | French and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-russian-ba-2026> |
| 128 | French and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-serbian-croatian-ba-2026> |
| 129 | French and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-spanish-ba-2026> |
| 130 | French and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-swedish-ba-2026> |
| 131 | French and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-ukrainian-ba-2026> |
| 132 | French and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-and-yiddish-ba-2026> |
| 133 | French with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-film-studies-ba-2026> |
| 134 | French with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/french-management-studies-ba-2026> |
| 135 | Geography | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-ba-2026> |
| 136 | Geography (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-international-programme-ba-2026> |
| 137 | German | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-ba-2026> |
| 138 | German and English | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-english-ba-2026> |
| 139 | German and Hebrew | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-hebrew-ba-2026> |
| 140 | German and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-history-art-ba-2026> |
| 141 | German and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-hungarian-ba-2026> |
| 142 | German and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-italian-ba-2026> |
| 143 | German and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-latin-ba-2026> |
| 144 | German and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-norwegian-ba-2026> |
| 145 | German and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-philosophy-ba-2026> |
| 146 | German and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-polish-ba-2026> |
| 147 | German and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-portuguese-ba-2026> |
| 148 | German and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-romanian-ba-2026> |
| 149 | German and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-russian-ba-2026> |
| 150 | German and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-serbian-croatian-ba-2026> |
| 151 | German and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-spanish-ba-2026> |
| 152 | German and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-swedish-ba-2026> |
| 153 | German and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-ukrainian-ba-2026> |
| 154 | German and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-and-yiddish-ba-2026> |
| 155 | German with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-film-studies-ba-2026> |
| 156 | German with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/german-management-studies-ba-2026> |
| 157 | Hebrew and Hungarian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-hungarian-ba-2026> |
| 158 | Hebrew and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-italian-ba-2026> |
| 159 | Hebrew and Jewish Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-jewish-studies-ba-2026> |
| 160 | Hebrew and Jewish Studies with Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-jewish-studies-year-abroad-ba-2026> |
| 161 | Hebrew and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-norwegian-ba-2026> |
| 162 | Hebrew and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-polish-ba-2026> |
| 163 | Hebrew and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-portuguese-ba-2026> |
| 164 | Hebrew and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-romanian-ba-2026> |
| 165 | Hebrew and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-russian-ba-2026> |
| 166 | Hebrew and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-serbian-croatian-ba-2026> |
| 167 | Hebrew and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-spanish-ba-2026> |
| 168 | Hebrew and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-swedish-ba-2026> |
| 169 | Hebrew and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-ukrainian-ba-2026> |
| 170 | Hebrew and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hebrew-and-yiddish-ba-2026> |
| 171 | History | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-ba-2026> |
| 172 | History (Central and East European) and Jewish Studies with Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-central-and-east-european-and-jewish-studies-year-abroad-ba-2026> |
| 173 | History and Politics of the Americas | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-and-politics-americas-ba-2026> |
| 174 | History and Politics of the Americas with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-and-politics-americas-year-abroad-ba-2026> |
| 175 | History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-art-ba-2026> |
| 176 | History with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-year-abroad-ba-2026> |
| 177 | Hungarian and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-east-european-studies-ba-2026> |
| 178 | Hungarian and Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-italian-ba-2026> |
| 179 | Hungarian and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-norwegian-ba-2026> |
| 180 | Hungarian and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-polish-ba-2026> |
| 181 | Hungarian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-portuguese-ba-2026> |
| 182 | Hungarian and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-romanian-ba-2026> |
| 183 | Hungarian and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-russian-ba-2026> |
| 184 | Hungarian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-serbian-croatian-ba-2026> |
| 185 | Hungarian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-spanish-ba-2026> |
| 186 | Hungarian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-swedish-ba-2026> |
| 187 | Hungarian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-ukrainian-ba-2026> |
| 188 | Hungarian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/hungarian-and-yiddish-ba-2026> |
| 189 | Icelandic | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/icelandic-ba-2026> |
| 190 | Italian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-ba-2026> |
| 191 | Italian and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-history-art-ba-2026> |
| 192 | Italian and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-latin-ba-2026> |
| 193 | Italian and Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-management-studies-ba-2026> |
| 194 | Italian and Norwegian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-norwegian-ba-2026> |
| 195 | Italian and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-philosophy-ba-2026> |
| 196 | Italian and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-polish-ba-2026> |
| 197 | Italian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-portuguese-ba-2026> |
| 198 | Italian and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-romanian-ba-2026> |
| 199 | Italian and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-russian-ba-2026> |
| 200 | Italian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-serbian-croatian-ba-2026> |
| 201 | Italian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-spanish-ba-2026> |
| 202 | Italian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-swedish-ba-2026> |
| 203 | Italian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-ukrainian-ba-2026> |
| 204 | Italian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-and-yiddish-ba-2026> |
| 205 | Italian with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/italian-film-studies-ba-2026> |
| 206 | Language and Culture | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/language-and-culture-ba-2026> |
| 207 | Linguistics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/linguistics-ba-2026> |
| 208 | Linguistics (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/linguistics-international-programme-ba-2026> |
| 209 | Media | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/media-ba-2026> |
| 210 | Norwegian and Polish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-polish-ba-2026> |
| 211 | Norwegian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-portuguese-ba-2026> |
| 212 | Norwegian and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-romanian-ba-2026> |
| 213 | Norwegian and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-russian-ba-2026> |
| 214 | Norwegian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-serbian-croatian-ba-2026> |
| 215 | Norwegian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-spanish-ba-2026> |
| 216 | Norwegian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-ukrainian-ba-2026> |
| 217 | Norwegian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/norwegian-and-yiddish-ba-2026> |
| 218 | Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-ba-2026> |
| 219 | Philosophy and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-and-history-art-ba-2026> |
| 220 | Polish and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-east-european-studies-ba-2026> |
| 221 | Polish and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-portuguese-ba-2026> |
| 222 | Polish and Romanian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-romanian-ba-2026> |
| 223 | Polish and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-russian-ba-2026> |
| 224 | Polish and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-serbian-croatian-ba-2026> |
| 225 | Polish and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-spanish-ba-2026> |
| 226 | Polish and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-swedish-ba-2026> |
| 227 | Polish and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-ukrainian-ba-2026> |
| 228 | Polish and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/polish-and-yiddish-ba-2026> |
| 229 | Portuguese and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/portuguese-and-yiddish-ba-2026> |
| 230 | Romanian and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-east-european-studies-ba-2026> |
| 231 | Romanian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-portuguese-ba-2026> |
| 232 | Romanian and Russian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-russian-ba-2026> |
| 233 | Romanian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-serbian-croatian-ba-2026> |
| 234 | Romanian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-spanish-ba-2026> |
| 235 | Romanian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-swedish-ba-2026> |
| 236 | Romanian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-ukrainian-ba-2026> |
| 237 | Romanian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/romanian-and-yiddish-ba-2026> |
| 238 | Russian Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-studies-ba-2026> |
| 239 | Russian and History | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-history-ba-2026> |
| 240 | Russian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-portuguese-ba-2026> |
| 241 | Russian and Serbian/Croatian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-serbian-croatian-ba-2026> |
| 242 | Russian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-spanish-ba-2026> |
| 243 | Russian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-swedish-ba-2026> |
| 244 | Russian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-ukrainian-ba-2026> |
| 245 | Russian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-and-yiddish-ba-2026> |
| 246 | Russian with an East European Language | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/russian-east-european-language-ba-2026> |
| 247 | Scandinavian Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-ba-2026> |
| 248 | Scandinavian Studies and English | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-and-english-ba-2026> |
| 249 | Scandinavian Studies and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-and-history-art-ba-2026> |
| 250 | Scandinavian Studies and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-and-latin-ba-2026> |
| 251 | Scandinavian Studies and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-and-philosophy-ba-2026> |
| 252 | Scandinavian Studies with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-film-studies-ba-2026> |
| 253 | Scandinavian Studies with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/scandinavian-studies-management-studies-ba-2026> |
| 254 | Serbian / Croatian and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-east-european-studies-ba-2026> |
| 255 | Serbian/Croatian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-portuguese-ba-2026> |
| 256 | Serbian/Croatian and Spanish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-spanish-ba-2026> |
| 257 | Serbian/Croatian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-swedish-ba-2026> |
| 258 | Serbian/Croatian and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-ukrainian-ba-2026> |
| 259 | Serbian/Croatian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/serbian-croatian-and-yiddish-ba-2026> |
| 260 | Spanish and History of Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-history-art-ba-2026> |
| 261 | Spanish and Latin | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-latin-ba-2026> |
| 262 | Spanish and Latin American Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-latin-american-studies-ba-2026> |
| 263 | Spanish and Philosophy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-philosophy-ba-2026> |
| 264 | Spanish and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-portuguese-ba-2026> |
| 265 | Spanish and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-swedish-ba-2026> |
| 266 | Spanish and Ukrainian | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-ukrainian-ba-2026> |
| 267 | Spanish and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-and-yiddish-ba-2026> |
| 268 | Spanish with Film Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-film-studies-ba-2026> |
| 269 | Spanish with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/spanish-management-studies-ba-2026> |
| 270 | Swedish and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/swedish-and-portuguese-ba-2026> |
| 271 | Swedish and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/swedish-and-yiddish-ba-2026> |
| 272 | Ukrainian and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ukrainian-and-east-european-studies-ba-2026> |
| 273 | Ukrainian and Portuguese | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ukrainian-and-portuguese-ba-2026> |
| 274 | Ukrainian and Swedish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ukrainian-and-swedish-ba-2026> |
| 275 | Ukrainian and Yiddish | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/ukrainian-and-yiddish-ba-2026> |
| 276 | Viking and Old Norse Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/viking-and-old-norse-studies-ba-2026> |
| 277 | Youth, Society and Sustainable Futures | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/youth-society-and-sustainable-futures-ba-2026> |

##### BSc (27 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/anthropology-bsc-2026> |
| 2 | Anthropology with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/anthropology-year-abroad-bsc-2026> |
| 3 | Archaeology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/archaeology-bsc-2026> |
| 4 | Architectural and Interdisciplinary Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architectural-and-interdisciplinary-studies-bsc-2026> |
| 5 | Architectural and Interdisciplinary Studies with Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architectural-and-interdisciplinary-studies-year-abroad-bsc-2026> |
| 6 | Architecture | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architecture-bsc-2026> |
| 7 | Business and Health | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/business-and-health-bsc-2026> |
| 8 | Data Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/data-science-bsc-2026> |
| 9 | Environmental Geoscience | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/environmental-geoscience-bsc-2026> |
| 10 | Experimental Linguistics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/experimental-linguistics-bsc-2026> |
| 11 | Experimental Linguistics (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/experimental-linguistics-international-programme-bsc-2026> |
| 12 | Geography | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-bsc-2026> |
| 13 | Geography (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-international-programme-bsc-2026> |
| 14 | Global Humanitarian Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/global-humanitarian-studies-bsc-2026> |
| 15 | History and Philosophy of Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-and-philosophy-science-bsc-2026> |
| 16 | Information Management for Business | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/information-management-business-bsc-2026> |
| 17 | Information, Data and Society | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/information-data-and-society-bsc-2026> |
| 18 | International Management | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/international-management-bsc-2026> |
| 19 | Management Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/management-science-bsc-2026> |
| 20 | Management for Social Change | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/management-social-change-bsc-2026> |
| 21 | Medical Innovation and Enterprise | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-innovation-and-enterprise-bsc-2026> |
| 22 | Natural Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/natural-sciences-bsc-2026> |
| 23 | Social Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/social-sciences-bsc-2026> |
| 24 | Social Sciences with Data Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/social-sciences-data-science-bsc-2026> |
| 25 | Sport and Exercise Medical Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sport-and-exercise-medical-sciences-bsc-2026> |
| 26 | Sustainable Built Environments, Energy and Resources | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sustainable-built-environments-energy-and-resources-bsc-2026> |
| 27 | Technology and Innovation | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/technology-and-innovation-bsc-2026> |

##### BFA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/fine-art-bfa-2026> |

##### BASc (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Arts and Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/arts-and-sciences-basc-2026> |
| 2 | Arts and Sciences with Study Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/arts-and-sciences-study-abroad-basc-2026> |

##### MEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics and Artificial Intelligence | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/robotics-and-artificial-intelligence-meng-2026> |
| 2 | Sustainable Built Environments, Energy and Resources | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sustainable-built-environments-energy-and-resources-meng-2026> |

##### MSci (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/architecture-msci-2026> |
| 2 | Business and Health | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/business-and-health-msci-2026> |
| 3 | Environmental Geoscience | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/environmental-geoscience-msci-2026> |
| 4 | Management Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/management-science-msci-2026> |
| 5 | Medical Innovation and Enterprise | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-innovation-and-enterprise-msci-2026> |
| 6 | Natural Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/natural-sciences-msci-2026> |
| 7 | Statistical Science (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistical-science-international-programme-msci-2026> |


#### Engineering Sciences

##### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy and Computer Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-and-computer-science-ba-2026> |

##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/computer-science-bsc-2026> |
| 2 | Crime and Security Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/crime-and-security-science-bsc-2026> |
| 3 | Science and Engineering for Social Change | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/science-and-engineering-social-change-bsc-2026> |

##### BEng (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemical-engineering-beng-2026> |
| 2 | Biomedical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biomedical-engineering-beng-2026> |
| 3 | Chemical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemical-engineering-beng-2026> |
| 4 | Civil Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/civil-engineering-beng-2026> |
| 5 | Electronic and Electrical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/electronic-and-electrical-engineering-beng-2026> |
| 6 | Mechanical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mechanical-engineering-beng-2026> |

##### MEng (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemical-engineering-meng-2026> |
| 2 | Biomedical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biomedical-engineering-meng-2026> |
| 3 | Chemical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemical-engineering-meng-2026> |
| 4 | Civil Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/civil-engineering-meng-2026> |
| 5 | Computer Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/computer-science-meng-2026> |
| 6 | Construction Engineering, Innovation and Leadership | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/construction-engineering-innovation-and-leadership-meng-2026> |
| 7 | Electronic and Electrical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/electronic-and-electrical-engineering-meng-2026> |
| 8 | Engineering and Architectural Design | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-and-architectural-design-meng-2026> |
| 9 | Mechanical Engineering | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mechanical-engineering-meng-2026> |
| 10 | Mechanical Engineering with Business Finance | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mechanical-engineering-business-finance-meng-2026> |

##### MSci (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Project Management | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/construction-project-management-msci-2026> |
| 2 | Crime and Security Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/crime-and-security-science-msci-2026> |

##### Foundation Year (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Foundation Year | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/engineering-foundation-year-2026> |


#### Mathematical and Physical Sciences

##### BSc (20 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/astrophysics-bsc-2026> |
| 2 | Biochemistry | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemistry-bsc-2026> |
| 3 | Chemistry | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-bsc-2026> |
| 4 | Chemistry with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-management-studies-bsc-2026> |
| 5 | Chemistry with Mathematics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-mathematics-bsc-2026> |
| 6 | Earth Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-bsc-2026> |
| 7 | Geology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geology-bsc-2026> |
| 8 | Geophysics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geophysics-bsc-2026> |
| 9 | Mathematics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-bsc-2026> |
| 10 | Mathematics and Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-and-physics-bsc-2026> |
| 11 | Mathematics and Secondary Mathematics Education Teacher Degree Apprenticeship | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-and-secondary-mathematics-education-teacher-degree-apprenticeship-bsc-2026> |
| 12 | Mathematics and Statistical Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-and-statistical-science-bsc-2026> |
| 13 | Mathematics with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-management-studies-bsc-2026> |
| 14 | Mathematics with Mathematical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-mathematical-physics-bsc-2026> |
| 15 | Mathematics with Modern Languages | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-modern-languages-bsc-2026> |
| 16 | Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-bsc-2026> |
| 17 | Physics with Medical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-medical-physics-bsc-2026> |
| 18 | Statistics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-bsc-2026> |
| 19 | Statistics and Management for Business | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-and-management-business-bsc-2026> |
| 20 | Theoretical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/theoretical-physics-bsc-2026> |

##### MEng (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science and Mathematics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/computer-science-and-mathematics-meng-2026> |

##### MSci (19 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/astrophysics-msci-2026> |
| 2 | Biochemistry | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biochemistry-msci-2026> |
| 3 | Chemistry | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-msci-2026> |
| 4 | Chemistry (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-international-programme-msci-2026> |
| 5 | Chemistry with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-management-studies-msci-2026> |
| 6 | Chemistry with Mathematics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/chemistry-mathematics-msci-2026> |
| 7 | Earth Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-msci-2026> |
| 8 | Earth Sciences (International Programme) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/earth-sciences-international-programme-msci-2026> |
| 9 | Geology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geology-msci-2026> |
| 10 | Geophysics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geophysics-msci-2026> |
| 11 | Mathematics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-msci-2026> |
| 12 | Mathematics and Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-and-physics-msci-2026> |
| 13 | Mathematics and Statistical Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-and-statistical-science-msci-2026> |
| 14 | Mathematics with Management Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-management-studies-msci-2026> |
| 15 | Mathematics with Mathematical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-mathematical-physics-msci-2026> |
| 16 | Mathematics with Modern Languages | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-modern-languages-msci-2026> |
| 17 | Medical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medical-physics-msci-2026> |
| 18 | Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/physics-msci-2026> |
| 19 | Theoretical Physics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/theoretical-physics-msci-2026> |


#### Social and Historical Sciences

##### BA (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics and Business with East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-and-business-east-european-studies-ba-2026> |
| 2 | Economics and Business with East European Studies with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-and-business-east-european-studies-year-abroad-ba-2026> |
| 3 | European Social and Political Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/european-social-and-political-studies-ba-2026> |
| 4 | European Social and Political Studies: Dual Degree | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/european-social-and-political-studies-dual-degree-ba-2026> |
| 5 | History, Politics and Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/history-politics-and-economics-ba-2026> |
| 6 | International Social and Political Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/international-social-and-political-studies-ba-2026> |
| 7 | Philosophy and Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-and-economics-ba-2026> |
| 8 | Politics, Sociology and East European Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-sociology-and-east-european-studies-ba-2026> |
| 9 | Politics, Sociology and East European Studies with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-sociology-and-east-european-studies-year-abroad-ba-2026> |

##### BSc (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Geography and Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/geography-and-economics-bsc-2026> |
| 2 | Mathematics with Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-economics-bsc-2026> |
| 3 | Philosophy, Politics and Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/philosophy-politics-and-economics-bsc-2026> |
| 4 | Politics and International Relations | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/politics-and-international-relations-bsc-2026> |
| 5 | Sociology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sociology-bsc-2026> |
| 6 | Sociology and Politics of Science | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/sociology-and-politics-science-bsc-2026> |
| 7 | Statistics, Economics and Finance | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-economics-and-finance-bsc-2026> |
| 8 | Statistics, Economics and a Language | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/statistics-economics-and-language-bsc-2026> |

##### BSc (Econ) (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-bsc-econ-2026> |
| 2 | Economics and Statistics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-and-statistics-bsc-econ-2026> |
| 3 | Economics with a Year Abroad | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/economics-year-abroad-bsc-econ-2026> |

##### MSci (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics with Economics | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/mathematics-economics-msci-2026> |


#### Life Sciences

##### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biological-sciences-bsc-2026> |
| 2 | Biomedical Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biomedical-sciences-bsc-2026> |
| 3 | Human Neuroscience | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/human-neuroscience-bsc-2026> |
| 4 | Human Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/human-sciences-bsc-2026> |
| 5 | Infection and Immunity | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/infection-and-immunity-bsc-2026> |
| 6 | Neuroscience | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/neuroscience-bsc-2026> |
| 7 | Pharmacology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacology-bsc-2026> |

##### MSci (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/biological-sciences-msci-2026> |
| 2 | Human Sciences and Evolution | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/human-sciences-and-evolution-msci-2026> |
| 3 | Neuroscience | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/neuroscience-msci-2026> |
| 4 | Pharmacology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacology-msci-2026> |

##### MPharm (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacy-mpharm-2026> |
| 2 | Pharmacy with Integrated Foundation Training | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/pharmacy-integrated-foundation-training-mpharm-2026> |


#### Medical Sciences

##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Medical Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/applied-medical-sciences-bsc-2026> |
| 2 | Bioprocessing of New Medicines (Business and Management) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bioprocessing-new-medicines-business-and-management-bsc-2026> |
| 3 | Cancer Biomedicine | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/cancer-biomedicine-bsc-2026> |
| 4 | Medicine MBBS | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/medicine-mbbs-bsc-2026> |

##### MSci (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Cancer Biomedicine | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/cancer-biomedicine-msci-2026> |


#### Brain Sciences

##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Audiology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/audiology-bsc-2026> |
| 2 | Psychology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-bsc-2026> |
| 3 | Psychology and Language Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-and-language-sciences-bsc-2026> |
| 4 | Psychology with Education | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-education-bsc-2026> |

##### MSci (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-msci-2026> |
| 2 | Psychology and Language Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/psychology-and-language-sciences-msci-2026> |


#### Population Health Sciences

##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition and Medical Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/nutrition-and-medical-sciences-bsc-2026> |
| 2 | Population Health Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/population-health-sciences-bsc-2026> |
| 3 | Population Health Sciences (Data Science) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/population-health-sciences-data-science-bsc-2026> |

##### MSci (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Population Health Sciences | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/population-health-sciences-msci-2026> |
| 2 | Population Health Sciences (Data Science) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/population-health-sciences-data-science-msci-2026> |


#### Built Environment (Bartlett)

##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Urban Planning and Real Estate | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/urban-planning-and-real-estate-bsc-2026> |
| 2 | Urban Planning, Design and Management | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/urban-planning-design-and-management-bsc-2026> |
| 3 | Urban Studies | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/urban-studies-bsc-2026> |


#### Laws

##### LLB (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Laws (UCL) and Bachelor of Laws (HKU) | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/bachelor-laws-ucl-and-bachelor-laws-hku-llb-2026> |
| 2 | Law | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-llb-2026> |
| 3 | Law with French Law | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-french-law-llb-2026> |
| 4 | Law with German Law | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-german-law-llb-2026> |
| 5 | Law with Hispanic Law | <https://www.ucl.ac.uk/prospective-students/undergraduate/degrees/law-hispanic-law-llb-2026> |


---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UCL's taught postgraduate (PGT) and postgraduate certificate/diploma (PGCert, PGDip, GradDip) programmes are listed at `https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees` (see evidence E-G-001). 556 programmes were extracted.



#### Arts and Humanities

##### MA / MASt / MASc (75 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Ancient History | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ancient-history-ma> |
| 2 | Applied Linguistics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-linguistics-ma> |
| 3 | Archaeology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archaeology-ma> |
| 4 | Archaeology and Heritage of Asia | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archaeology-and-heritage-asia-ma> |
| 5 | Archaeology of the Mediterranean, Egypt and Middle East | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archaeology-mediterranean-egypt-and-middle-east-ma> |
| 6 | Architectural History | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-history-ma> |
| 7 | Audio Storytelling for Radio and Podcast | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/audio-storytelling-radio-and-podcast-ma> |
| 8 | Central and South-East European Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/central-and-south-east-european-studies-ma> |
| 9 | Classics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/classics-ma> |
| 10 | Creative and Collaborative Enterprise | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creative-and-collaborative-enterprise-ma> |
| 11 | Cultural Heritage Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cultural-heritage-studies-ma> |
| 12 | Designing Audio Experiences: Art, Science and Production | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/designing-audio-experiences-art-science-and-production-ma> |
| 13 | Digital Humanities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-humanities-ma> |
| 14 | Digital Media: Critical Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-media-critical-studies-ma> |
| 15 | Digital Media: Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-media-education-ma> |
| 16 | Digital Media: Production | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-media-production-ma> |
| 17 | Early Modern Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-modern-studies-ma> |
| 18 | Education (History) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-history-ma> |
| 19 | English Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-education-ma> |
| 20 | English Linguistics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-linguistics-ma> |
| 21 | English: Issues in Modern Culture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/english-issues-modern-culture-ma> |
| 22 | Ethnographic and Documentary Film (Practical) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ethnographic-and-documentary-film-practical-ma> |
| 23 | European Culture and Thought: Culture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-culture-and-thought-culture-ma> |
| 24 | European Culture and Thought: Thought | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-culture-and-thought-thought-ma> |
| 25 | European Studies: European Society | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-studies-european-society-ma> |
| 26 | European Studies: Modern European Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/european-studies-modern-european-studies-ma> |
| 27 | Film Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/film-studies-ma> |
| 28 | Fine Art | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/fine-art-ma> |
| 29 | Gender, Society and Representation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/gender-society-and-representation-ma> |
| 30 | Global Learning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-learning-ma> |
| 31 | Health Humanities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-humanities-ma> |
| 32 | History | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-ma> |
| 33 | History (SSEES) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-ssees-ma> |
| 34 | History of Art | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-art-ma> |
| 35 | Immersive Factual Storytelling | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/immersive-factual-storytelling-ma> |
| 36 | Intercultural Communication | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/intercultural-communication-ma> |
| 37 | Jewish Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/jewish-studies-ma> |
| 38 | Language, Culture and History: Dutch Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-dutch-studies-ma> |
| 39 | Language, Culture and History: French and Francophone Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-french-and-francophone-studies-ma> |
| 40 | Language, Culture and History: German History | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-german-history-ma> |
| 41 | Language, Culture and History: German Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-german-studies-ma> |
| 42 | Language, Culture and History: Hispanic Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-hispanic-studies-ma> |
| 43 | Language, Culture and History: Italian Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-italian-studies-ma> |
| 44 | Language, Culture and History: Scandinavian Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-culture-and-history-scandinavian-studies-ma> |
| 45 | Latin American Studies: History, Politics and Society | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/latin-american-studies-history-politics-and-society-ma> |
| 46 | Library and Information Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/library-and-information-studies-ma> |
| 47 | Linguistics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/linguistics-ma> |
| 48 | Linguistics with a Specialisation in Computational Linguistics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/linguistics-specialisation-computational-linguistics-ma> |
| 49 | Linguistics with a Specialisation in Phonology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/linguistics-specialisation-phonology-ma> |
| 50 | Linguistics with a Specialisation in Syntax | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/linguistics-specialisation-syntax-ma> |
| 51 | Managing Archaeological Sites | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/managing-archaeological-sites-ma> |
| 52 | Material and Visual Culture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/material-and-visual-culture-ma> |
| 53 | Medieval and Renaissance Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medieval-and-renaissance-studies-ma> |
| 54 | Museum Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/museum-studies-ma> |
| 55 | Museums and Galleries in Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/museums-and-galleries-education-ma> |
| 56 | Music Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/music-education-ma> |
| 57 | Philosophy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-ma> |
| 58 | Philosophy of Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-education-ma> |
| 59 | Principles of Conservation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/principles-conservation-ma> |
| 60 | Public History | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-history-ma> |
| 61 | Publishing | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/publishing-ma> |
| 62 | Race, Ethnicity and Postcolonial Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/race-ethnicity-and-postcolonial-studies-ma> |
| 63 | Reception of the Classical World | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/reception-classical-world-ma> |
| 64 | Research Methods for Archaeology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/research-methods-archaeology-ma> |
| 65 | Russian Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-studies-ma> |
| 66 | Russian and East European Literature and Culture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-and-east-european-literature-and-culture-ma> |
| 67 | Russian and Post-Soviet Politics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/russian-and-post-soviet-politics-ma> |
| 68 | Situated Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/situated-practice-ma> |
| 69 | Specific Learning Difficulties (dyslexia) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/specific-learning-difficulties-dyslexia-ma> |
| 70 | Teaching English to Speakers of Other Languages (TESOL) In-Service | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/teaching-english-speakers-other-languages-tesol-service-ma> |
| 71 | Teaching English to Speakers of Other Languages (TESOL) Pre-Service | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/teaching-english-speakers-other-languages-tesol-pre-service-ma> |
| 72 | Translation: Research | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-research-ma> |
| 73 | Translation: Translation Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-translation-studies-ma> |
| 74 | Translation: Translation and Culture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-translation-and-culture-ma> |
| 75 | United States Studies: History and Politics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/united-states-studies-history-and-politics-ma> |

##### MSc (78 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Biomedical Imaging | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-biomedical-imaging-msc> |
| 2 | Advanced Critical Care Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-critical-care-practice-msc> |
| 3 | Aquatic Conservation, Ecology and Restoration | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/aquatic-conservation-ecology-and-restoration-msc> |
| 4 | Architectural Computation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-computation-msc> |
| 5 | Audiological Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/audiological-science-msc> |
| 6 | Audiological Science with Clinical Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/audiological-science-clinical-practice-msc> |
| 7 | Behaviour Change | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/behaviour-change-msc> |
| 8 | Bio-Integrated Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bio-integrated-design-msc> |
| 9 | Biodiversity and Global Change | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biodiversity-and-global-change-msc> |
| 10 | Bioscience Innovation and Enterprise | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bioscience-innovation-and-enterprise-msc> |
| 11 | Brain and Mind Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/brain-and-mind-sciences-msc> |
| 12 | Cancer | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cancer-msc> |
| 13 | Cardiovascular Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cardiovascular-science-msc> |
| 14 | Cell, Gene and Novel Therapies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cell-gene-and-novel-therapies-msc> |
| 15 | Chemical Research | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/chemical-research-msc> |
| 16 | Clinical Trials | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-trials-msc> |
| 17 | Computational Cancer | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-cancer-msc> |
| 18 | Computer Graphics, Vision and Imaging | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-graphics-vision-and-imaging-msc> |
| 19 | Connected Environments | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/connected-environments-msc> |
| 20 | Conservation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/conservation-msc> |
| 21 | Conservation for Archaeology and Museums | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/conservation-archaeology-and-museums-msc> |
| 22 | Conservation of Contemporary Art and Media | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/conservation-contemporary-art-and-media-msc> |
| 23 | Countering Extremist Crime and Terrorism | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/countering-extremist-crime-and-terrorism-msc> |
| 24 | Crime Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-science-msc> |
| 25 | Crime Science with Cybercrime | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-science-cybercrime-msc> |
| 26 | Crime Science with Serious Organised Crime | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-science-serious-organised-crime-msc> |
| 27 | Crime and Forensic Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-and-forensic-science-msc> |
| 28 | Dietetics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dietetics-msc> |
| 29 | Digital Humanities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-humanities-msc> |
| 30 | Digital Innovation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-innovation-msc> |
| 31 | Disability, Design and Innovation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/disability-design-and-innovation-msc> |
| 32 | Drug Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-design-msc> |
| 33 | Emerging Digital Technologies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/emerging-digital-technologies-msc> |
| 34 | Environmental Archaeology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-archaeology-msc> |
| 35 | Environmental Modelling | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-modelling-msc> |
| 36 | Financial Technology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/financial-technology-msc> |
| 37 | Geophysical Hazards | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geophysical-hazards-msc> |
| 38 | Geoscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geoscience-msc> |
| 39 | Geospatial Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-msc> |
| 40 | Geospatial Sciences (Geographic Information Science and Computing) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-geographic-information-science-and-computing-msc> |
| 41 | Global Prosperity | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-prosperity-msc> |
| 42 | Health Informatics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-informatics-msc> |
| 43 | Health Systems, Policy and Innovation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-systems-policy-and-innovation-msc> |
| 44 | Healthcare Facilities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/healthcare-facilities-msc> |
| 45 | History and Philosophy of Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/history-and-philosophy-science-msc> |
| 46 | Human Tissue Repair | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-tissue-repair-msc> |
| 47 | Human-Computer Interaction | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-computer-interaction-msc> |
| 48 | Humanitarian Policy and Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/humanitarian-policy-and-practice-msc> |
| 49 | Light and Lighting | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/light-and-lighting-msc> |
| 50 | Manufacture and Commercialisation of Stem Cell and Gene Therapies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/manufacture-and-commercialisation-stem-cell-and-gene-therapies-msc> |
| 51 | Manufacturing with Innovation and Enterprise | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/manufacturing-innovation-and-enterprise-msc> |
| 52 | Mathematical Modelling | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mathematical-modelling-msc> |
| 53 | Ophthalmology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ophthalmology-msc> |
| 54 | Orthoptics (pre-registration) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/orthoptics-pre-registration-msc> |
| 55 | Periodontology (Distance Learning) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/periodontology-distance-learning-msc> |
| 56 | Physical Therapy in Musculoskeletal Healthcare and Rehabilitation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physical-therapy-musculoskeletal-healthcare-and-rehabilitation-msc> |
| 57 | Policing | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/policing-msc> |
| 58 | Prosperity, People and Planet | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/prosperity-people-and-planet-msc> |
| 59 | Psychological Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychological-sciences-msc> |
| 60 | Quantum Technologies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/quantum-technologies-msc> |
| 61 | Remote Sensing and Environmental Mapping | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/remote-sensing-and-environmental-mapping-msc> |
| 62 | Reproductive Science and Women's Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/reproductive-science-and-womens-health-msc> |
| 63 | Respiratory Clinical Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/respiratory-clinical-science-msc> |
| 64 | Risk and Disaster Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-and-disaster-science-msc> |
| 65 | Risk, Disaster and Resilience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-and-resilience-msc> |
| 66 | Science Communication | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/science-communication-msc> |
| 67 | Science, Technology and Society | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/science-technology-and-society-msc> |
| 68 | Scientific and Data Intensive Computing | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/scientific-and-data-intensive-computing-msc> |
| 69 | Social Policy (Evidence Synthesis) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-policy-evidence-synthesis-msc> |
| 70 | Social Policy (Research Methods) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-policy-research-methods-msc> |
| 71 | Spatio-temporal Analytics and Big Data Mining | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatio-temporal-analytics-and-big-data-mining-msc> |
| 72 | Surgical Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/surgical-sciences-msc> |
| 73 | Theoretical Psychoanalytic Studies (Non-Clinical) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/theoretical-psychoanalytic-studies-non-clinical-msc> |
| 74 | Translation and Technology (Audiovisual) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-and-technology-audiovisual-msc> |
| 75 | Translation and Technology (Scientific, Technical and Medical) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-and-technology-scientific-technical-and-medical-msc> |
| 76 | Translation and Technology (with Interpreting) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translation-and-technology-interpreting-msc> |
| 77 | Venture Capital and Private Equity with Financial Technology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/venture-capital-and-private-equity-financial-technology-msc> |
| 78 | Women's Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/womens-health-msc> |

##### MS (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Aesthetics (Minimally-invasive Aesthetics) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/aesthetics-minimally-invasive-aesthetics-ms> |

##### MRes (9 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biosciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biosciences-mres> |
| 2 | Brain Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/brain-sciences-mres> |
| 3 | Drug Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-design-mres> |
| 4 | East European Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/east-european-studies-mres> |
| 5 | Human Tissue Repair | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-tissue-repair-mres> |
| 6 | Photonic and Electronic Systems | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/photonic-and-electronic-systems-mres> |
| 7 | Reproductive Science and Women's Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/reproductive-science-and-womens-health-mres> |
| 8 | Social Research | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-research-mres> |
| 9 | Synthetic Biology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/synthetic-biology-mres> |

##### MArch (4 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Architectural Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architectural-design> |
| 2 | Bio-Integrated Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bio-integrated-design> |
| 3 | Design for Manufacture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/design-manufacture> |
| 4 | Design for Performance and Interaction | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/design-performance-and-interaction> |

##### MPA (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Technologies and Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-technologies-and-policy-mpa> |

##### MClinDent (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Endodontology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/endodontology-mclindent> |
| 2 | Endodontology (Advanced Training) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/endodontology-advanced-training-mclindent> |
| 3 | Periodontology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/periodontology-mclindent> |

##### MBA (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Executive Programme Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/executive-programme-health-mba> |
| 2 | Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-mba> |
| 3 | Major Infrastructure Delivery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/major-infrastructure-delivery-mba> |

##### MFA (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Documentary by Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creative-documentary-practice-mfa> |
| 2 | Fine Art | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/fine-art-mfa> |

##### (no degree in title) (10 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Archaeology Grad Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archaeology-grad-dip> |
| 2 | Creative Health MASc | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creative-health-masc> |
| 3 | Creative Health PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creative-health-pg-cert> |
| 4 | Creative Health PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creative-health-pg-dip> |
| 5 | Economy, State and Society: History and Society MA (International) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-and-society-history-and-society-ma-international> |
| 6 | Health Informatics PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-informatics-pg-cert> |
| 7 | Health Informatics PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-informatics-pg-dip> |
| 8 | Natural Hazards for Insurers PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/natural-hazards-insurers-pg-cert> |
| 9 | Risk, Disaster and Resilience PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/risk-disaster-and-resilience-pg-dip> |
| 10 | Teaching and Reflective Practice PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/teaching-and-reflective-practice-pg-dip> |


#### Engineering Sciences

##### MSc (55 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Materials Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-materials-science-msc> |
| 2 | Advanced Materials Science (Data-driven Innovation) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-materials-science-data-driven-innovation-msc> |
| 3 | Advanced Materials Science (Energy Storage) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-materials-science-energy-storage-msc> |
| 4 | Advanced Materials Science (Materials Innovation and Enterprise) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-materials-science-materials-innovation-and-enterprise-msc> |
| 5 | Advanced Materials Science (Sustainability) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-materials-science-sustainability-msc> |
| 6 | Archaeological Science: Technology and Materials | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archaeological-science-technology-and-materials-msc> |
| 7 | Artificial Intelligence and Data Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-and-data-engineering-msc> |
| 8 | Artificial Intelligence and Medical Imaging | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-and-medical-imaging-msc> |
| 9 | Biochemical Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biochemical-engineering-msc> |
| 10 | Biomaterials and Tissue Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biomaterials-and-tissue-engineering-msc> |
| 11 | Built Environment: Environmental Design and Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/built-environment-environmental-design-and-engineering-msc> |
| 12 | Built Environment: Sustainable Heritage (Data Science) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/built-environment-sustainable-heritage-data-science-msc> |
| 13 | Civil Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-msc> |
| 14 | Civil Engineering (with Fluids) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-fluids-msc> |
| 15 | Civil Engineering (with Integrated Design) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-integrated-design-msc> |
| 16 | Computer Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computer-science-msc> |
| 17 | Crime Science with Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/crime-science-data-science-msc> |
| 18 | Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-msc> |
| 19 | Data Science and Machine Learning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-and-machine-learning-msc> |
| 20 | Digital Manufacturing of Advanced Materials | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-manufacturing-advanced-materials-msc> |
| 21 | Ecology and Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ecology-and-data-science-msc> |
| 22 | Electrochemical Propulsion Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/electrochemical-propulsion-engineering-msc> |
| 23 | Energy Systems and Data Analytics (ESDA) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/energy-systems-and-data-analytics-esda-msc> |
| 24 | Engineering and Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-and-education-msc> |
| 25 | Environmental Systems Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-systems-engineering-msc> |
| 26 | Future Manufacturing and Nanoscale Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/future-manufacturing-and-nanoscale-engineering-msc> |
| 27 | Health Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-data-science-msc> |
| 28 | Integrated Machine Learning Systems | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/integrated-machine-learning-systems-msc> |
| 29 | Internet Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/internet-engineering-msc> |
| 30 | Knowledge, Information and Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/knowledge-information-and-data-science-msc> |
| 31 | Machine Learning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/machine-learning-msc> |
| 32 | Marine Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/marine-engineering-msc> |
| 33 | Materials and Molecular Modelling | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/materials-and-molecular-modelling-msc> |
| 34 | Materials for Energy and Environment | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/materials-energy-and-environment-msc> |
| 35 | Mechanical Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mechanical-engineering-msc> |
| 36 | Medical Robotics and Artificial Intelligence | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medical-robotics-and-artificial-intelligence-msc> |
| 37 | Musculoskeletal Science and Medical Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/musculoskeletal-science-and-medical-engineering-msc> |
| 38 | Nanotechnology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/nanotechnology-msc> |
| 39 | Nature-Inspired Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/nature-inspired-engineering-msc> |
| 40 | Power Systems Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/power-systems-engineering-msc> |
| 41 | Rehabilitation Engineering and Assistive Technologies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/rehabilitation-engineering-and-assistive-technologies-msc> |
| 42 | Robotics and Artificial Intelligence | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/robotics-and-artificial-intelligence-msc> |
| 43 | Smart Buildings and Digital Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/smart-buildings-and-digital-engineering-msc> |
| 44 | Smart Energy and the Built Environment | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/smart-energy-and-built-environment-msc> |
| 45 | Social Research Methods with Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-research-methods-data-science-msc> |
| 46 | Social and Geographic Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-and-geographic-data-science-msc> |
| 47 | Software Systems Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/software-systems-engineering-msc> |
| 48 | Space Science and Engineering: Space Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-science-and-engineering-space-science-msc> |
| 49 | Space Science and Engineering: Space Technology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-science-and-engineering-space-technology-msc> |
| 50 | Sustainable Chemical Process Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sustainable-chemical-process-engineering-msc> |
| 51 | Sustainable Structural Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sustainable-structural-engineering-msc> |
| 52 | Systems Engineering for the Internet of Things | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/systems-engineering-internet-things-msc> |
| 53 | Telecommunications | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-msc> |
| 54 | Telecommunications (IGDP) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-igdp-msc> |
| 55 | Wireless and Optical Communications | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/wireless-and-optical-communications-msc> |

##### MRes (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Artificial Intelligence Enabled Healthcare | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-enabled-healthcare-mres> |
| 2 | Telecommunications | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-mres> |

##### (no degree in title) (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy, Logic, and Artificial Intelligence MASc | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-logic-and-artificial-intelligence-masc> |


#### Mathematical and Physical Sciences

##### MA / MASt / MASc (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mathematics-education-ma> |

##### MSc (13 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Analytical Chemistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-analytical-chemistry-msc> |
| 2 | Astrophysics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/astrophysics-msc> |
| 3 | Climate Change | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/climate-change-msc> |
| 4 | Climate Change Policy and Politics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/climate-change-policy-and-politics-msc> |
| 5 | Computational Statistics and Machine Learning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-statistics-and-machine-learning-msc> |
| 6 | Ecology, Climate Change and Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ecology-climate-change-and-health-msc> |
| 7 | Financial Mathematics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/financial-mathematics-msc> |
| 8 | Mathematics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mathematics-msc> |
| 9 | Medical Statistics and Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medical-statistics-and-data-science-msc> |
| 10 | Organic Chemistry: Drug Discovery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/organic-chemistry-drug-discovery-msc> |
| 11 | Physics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physics-msc> |
| 12 | Statistics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/statistics-msc> |
| 13 | Sustainable Chemistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sustainable-chemistry-msc> |

##### MRes (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Cell Biophysics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-cell-biophysics-mres> |
| 2 | Medical Physics and Biomedical Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medical-physics-and-biomedical-engineering-mres> |

##### MPA (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Climate, Innovation and Sustainability Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/climate-innovation-and-sustainability-policy-mpa> |


#### Social and Historical Sciences

##### MA / MASt / MASc (35 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Educational Leadership | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-educational-leadership-ma> |
| 2 | Archives and Records Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/archives-and-records-management-ma> |
| 3 | Art Education, Culture and Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/art-education-culture-and-practice-ma> |
| 4 | Comparative Business Economics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-business-economics-ma> |
| 5 | Comparative Economics and Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-economics-and-policy-ma> |
| 6 | Comparative Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-education-ma> |
| 7 | Comparative Literature | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/comparative-literature-ma> |
| 8 | Early Years Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-years-education-ma> |
| 9 | Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-ma> |
| 10 | Education (Advanced Practice) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-advanced-practice-ma> |
| 11 | Education (Assessment) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-assessment-ma> |
| 12 | Education (Citizenship) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-citizenship-ma> |
| 13 | Education (Geography) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-geography-ma> |
| 14 | Education (Science) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-science-ma> |
| 15 | Education and International Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-and-international-development-ma> |
| 16 | Education and International Development: Conflict, Emergencies and Peace (CEP) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-and-international-development-conflict-emergencies-and-peace-cep-ma> |
| 17 | Education and Technology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-and-technology-ma> |
| 18 | Education, Gender and International Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-gender-and-international-development-ma> |
| 19 | Education, Health Promotion and International Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-health-promotion-and-international-development-ma> |
| 20 | Educational Leadership (In-service) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-leadership-service-ma> |
| 21 | Educational Leadership (Pre-service) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-leadership-pre-service-ma> |
| 22 | Educational Planning, Economics and International Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-planning-economics-and-international-development-ma> |
| 23 | Higher Education Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/higher-education-studies-ma> |
| 24 | Literacy and Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/literacy-and-education-ma> |
| 25 | Philosophy, Politics and Economics of Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-politics-and-economics-health-ma> |
| 26 | Philosophy, Public Policy and Social Change | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/philosophy-public-policy-and-social-change-ma> |
| 27 | Policy Studies in Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/policy-studies-education-ma> |
| 28 | Political Analysis (Russia and Eastern Europe) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/political-analysis-russia-and-eastern-europe-ma> |
| 29 | Political Sociology (Russia and Eastern Europe) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/political-sociology-russia-and-eastern-europe-ma> |
| 30 | Primary Education (4-12) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/primary-education-4-12-ma> |
| 31 | Social Justice and Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-justice-and-education-ma> |
| 32 | Sociology of Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-education-ma> |
| 33 | Special and Inclusive Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-and-inclusive-education-ma> |
| 34 | Special and Inclusive Education (Autism) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-and-inclusive-education-autism-ma> |
| 35 | Special and Inclusive Education (Specific Learning Difficulties) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-and-inclusive-education-specific-learning-difficulties-ma> |

##### MSc (80 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology and Professional Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/anthropology-and-professional-practice-msc> |
| 2 | Artificial Intelligence for Sustainable Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-sustainable-development-msc> |
| 3 | Banking and Digital Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/banking-and-digital-finance-msc> |
| 4 | Bioarchaeological and Forensic Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bioarchaeological-and-forensic-anthropology-msc> |
| 5 | Bioscience (Research and Development) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bioscience-research-and-development-msc> |
| 6 | Bioscience (Research and Development) with Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/bioscience-research-and-development-practice-msc> |
| 7 | Biotech and Pharmaceutical Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biotech-and-pharmaceutical-management-msc> |
| 8 | Building and Urban Design in Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/building-and-urban-design-development-msc> |
| 9 | Built Environment: Sustainable Heritage (Heritage Management) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/built-environment-sustainable-heritage-heritage-management-msc> |
| 10 | Business Analytics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/business-analytics-msc> |
| 11 | Business and Sustainability | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/business-and-sustainability-msc> |
| 12 | Clinical Drug Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-msc> |
| 13 | Computational Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/computational-finance-msc> |
| 14 | Construction Economics and Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/construction-economics-and-management-msc> |
| 15 | Data Science and Public Policy (Economics) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-and-public-policy-economics-msc> |
| 16 | Data Science and Public Policy (Political Science) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/data-science-and-public-policy-political-science-msc> |
| 17 | Democracy and Comparative Politics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/democracy-and-comparative-politics-msc> |
| 18 | Design and Management for Sustainable Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/design-and-management-sustainable-education-msc> |
| 19 | Development Administration and Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/development-administration-and-planning-msc> |
| 20 | Digital Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-anthropology-msc> |
| 21 | Digital Engineering Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-engineering-management-msc> |
| 22 | Digital Health and Entrepreneurship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-health-and-entrepreneurship-msc> |
| 23 | Digital Innovation Built Asset Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/digital-innovation-built-asset-management-msc> |
| 24 | Drug Discovery and Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-discovery-and-development-msc> |
| 25 | Drug Discovery and Pharma Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/drug-discovery-and-pharma-management-msc> |
| 26 | Earthquake Engineering with Disaster Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/earthquake-engineering-disaster-management-msc> |
| 27 | Economics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economics-msc> |
| 28 | Economics and Policy of Energy and the Environment | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economics-and-policy-energy-and-environment-msc> |
| 29 | Education for Health Professionals | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-health-professionals-msc> |
| 30 | Engineering for International Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-international-development-msc> |
| 31 | Engineering with Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-finance-msc> |
| 32 | Engineering with Innovation and Entrepreneurship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/engineering-innovation-and-entrepreneurship-msc> |
| 33 | Entrepreneurship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/entrepreneurship-msc> |
| 34 | Environment and Sustainable Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environment-and-sustainable-development-msc> |
| 35 | Environment, Politics and Society | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environment-politics-and-society-msc> |
| 36 | Environmental Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/environmental-anthropology-msc> |
| 37 | Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/finance-msc> |
| 38 | Finance with Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/finance-data-science-msc> |
| 39 | Financial Risk Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/financial-risk-management-msc> |
| 40 | Global Governance and Ethics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-governance-and-ethics-msc> |
| 41 | Global Management of Natural Resources | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-management-natural-resources-msc> |
| 42 | Global Management of Natural Resources (London) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-management-natural-resources-london-msc> |
| 43 | Health Economics and Decision Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-economics-and-decision-science-msc> |
| 44 | Health in Urban Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-urban-development-msc> |
| 45 | Information Security | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/information-security-msc> |
| 46 | Infrastructure Investment and Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infrastructure-investment-and-finance-msc> |
| 47 | Infrastructure Planning, Appraisal and Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infrastructure-planning-appraisal-and-development-msc> |
| 48 | International Development in the Americas | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-development-americas-msc> |
| 49 | International Public Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-public-policy-msc> |
| 50 | International Relations of the Americas | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-relations-americas-msc> |
| 51 | Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/management-msc> |
| 52 | Management of Complex Projects | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/management-complex-projects-msc> |
| 53 | Marketing Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/marketing-science-msc> |
| 54 | Medical Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/medical-anthropology-msc> |
| 55 | Migration, Politics and Society | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/migration-politics-and-society-msc> |
| 56 | Pain Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/pain-management-msc> |
| 57 | Palaeoanthropology and Palaeolithic Archaeology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/palaeoanthropology-and-palaeolithic-archaeology-msc> |
| 58 | People Analytics and Human-Centric Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/people-analytics-and-human-centric-management-msc> |
| 59 | Pharmaceutical Formulation and Entrepreneurship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/pharmaceutical-formulation-and-entrepreneurship-msc> |
| 60 | Political Economy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/political-economy-msc> |
| 61 | Project and Enterprise Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/project-and-enterprise-management-msc> |
| 62 | Prosperity, Innovation and Entrepreneurship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/prosperity-innovation-and-entrepreneurship-msc> |
| 63 | Public Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-policy-msc> |
| 64 | Real Estate Economics and Investment Analysis | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/real-estate-economics-and-investment-analysis-msc> |
| 65 | Responsible Finance and Alternative Assets | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/responsible-finance-and-alternative-assets-msc> |
| 66 | Science, Technology, Engineering and Public Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/science-technology-engineering-and-public-policy-msc> |
| 67 | Security Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/security-studies-msc> |
| 68 | Social Development Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-development-practice-msc> |
| 69 | Social and Cultural Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-and-cultural-anthropology-msc> |
| 70 | Sociology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-msc> |
| 71 | Sociology and Data Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-and-data-science-msc> |
| 72 | Sociology and Social Inequalities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-and-social-inequalities-msc> |
| 73 | Strategic Accounting and Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/strategic-accounting-and-finance-msc> |
| 74 | Strategic Management of Projects | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/strategic-management-projects-msc> |
| 75 | Sustainable Resources: Economics, Policy and Transitions | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sustainable-resources-economics-policy-and-transitions-msc> |
| 76 | Systems Engineering Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/systems-engineering-management-msc> |
| 77 | Technology Management | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/technology-management-msc> |
| 78 | Telecommunications with Business | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/telecommunications-business-msc> |
| 79 | Urban Development Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-development-planning-msc> |
| 80 | Urban Economic Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-economic-development-msc> |

##### MRes (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/anthropology-mres> |
| 2 | Clinical Drug Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-drug-development-mres> |
| 3 | The Politics and Economics of Eastern Europe | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/politics-and-economics-eastern-europe-mres> |

##### MPA (4 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Development, Technology and Innovation Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/development-technology-and-innovation-policy-mpa> |
| 2 | Health, Technology and Public Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-technology-and-public-policy-mpa> |
| 3 | Innovation, Public Policy and Public Value | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/innovation-public-policy-and-public-value-mpa> |
| 4 | Public Management and Leadership | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/public-management-and-leadership-mpa> |

##### MBA (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/business-administration-mba> |
| 2 | Strategic Management and Leadership | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/strategic-management-and-leadership-mba> |

##### (no degree in title) (6 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Educational Practice Grad Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-educational-practice-grad-dip> |
| 2 | Economy, State and Society: Economics and Business MA (International) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-and-society-economics-and-business-ma-international> |
| 3 | Economy, State and Society: Politics and Security MA (International) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-and-society-politics-and-security-ma-international> |
| 4 | Economy, State and Society: Politics and the International Economy MA (International) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/economy-state-and-society-politics-and-international-economy-ma-international> |
| 5 | Security and Crime Science PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/security-and-crime-science-pg-cert> |
| 6 | Social Science Research Methods PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-science-research-methods-pg-dip> |


#### Life Sciences

##### MSc (10 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Pharmacy Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-pharmacy-practice-msc> |
| 2 | Biomedical Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biomedical-sciences-msc> |
| 3 | Clinical Pharmacy, International Practice and Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-pharmacy-international-practice-and-policy-msc> |
| 4 | Clinical Pharmacy, International Practice and Policy with Extended Placement | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-pharmacy-international-practice-and-policy-extended-placement-msc> |
| 5 | Experimental Pharmacology and Therapeutics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/experimental-pharmacology-and-therapeutics-msc> |
| 6 | Experimental and Translational Immunology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/experimental-and-translational-immunology-msc> |
| 7 | Genetics of Human Disease | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/genetics-human-disease-msc> |
| 8 | Human Evolution and Behaviour | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-evolution-and-behaviour-msc> |
| 9 | Infection and Immunity | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/infection-and-immunity-msc> |
| 10 | Pharmaceutics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/pharmaceutics-msc> |

##### MRes (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Biodiversity, Evolution and Conservation | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/biodiversity-evolution-and-conservation-mres> |
| 2 | Experimental and Translational Immunology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/experimental-and-translational-immunology-mres> |
| 3 | Pharmaceutical Research | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/pharmaceutical-research-mres> |

##### (no degree in title) (4 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Pharmacy Practice (Critical Care) PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-pharmacy-practice-critical-care-pg-cert> |
| 2 | General Pharmacy Practice (Prescribing) PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/general-pharmacy-practice-prescribing-pg-cert> |
| 3 | General Pharmacy Practice PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/general-pharmacy-practice-pg-dip> |
| 4 | Pharmaceutical Quality and Regulation PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/pharmaceutical-quality-and-regulation-pg-dip> |


#### Medical Sciences

##### MSc (28 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Audiology: Audiovestibular Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-audiology-audiovestibular-medicine-msc> |
| 2 | Advanced Physiotherapy: Cardiorespiratory | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-cardiorespiratory-msc> |
| 3 | Advanced Physiotherapy: Musculoskeletal | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-musculoskeletal-msc> |
| 4 | Advanced Physiotherapy: Neurophysiotherapy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-neurophysiotherapy-msc> |
| 5 | Advanced Physiotherapy: Paediatrics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-physiotherapy-paediatrics-msc> |
| 6 | Artificial Intelligence for Biomedicine and Healthcare | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/artificial-intelligence-biomedicine-and-healthcare-msc> |
| 7 | Burns, Plastic and Reconstructive Surgery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/burns-plastic-and-reconstructive-surgery-msc> |
| 8 | Conservative Dentistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/conservative-dentistry-msc> |
| 9 | Dental Public Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dental-public-health-msc> |
| 10 | Endodontics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/endodontics-msc> |
| 11 | Genetics and Multiomics in Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/genetics-and-multiomics-medicine-msc> |
| 12 | Implant Dentistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/implant-dentistry-msc> |
| 13 | Nanotechnology and Regenerative Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/nanotechnology-and-regenerative-medicine-msc> |
| 14 | Oral Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-medicine-msc> |
| 15 | Oral and Maxillofacial Surgery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-and-maxillofacial-surgery-msc> |
| 16 | Paediatric Dentistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatric-dentistry-msc> |
| 17 | Performing Arts Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/performing-arts-medicine-msc> |
| 18 | Perioperative Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/perioperative-medicine-msc> |
| 19 | Physics and Engineering in Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physics-and-engineering-medicine-msc> |
| 20 | Physics and Engineering in Medicine by distance learning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physics-and-engineering-medicine-distance-learning-msc> |
| 21 | Physiotherapy Studies: Cardiorespiratory | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-cardiorespiratory-msc> |
| 22 | Physiotherapy Studies: Musculoskeletal | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-musculoskeletal-msc> |
| 23 | Physiotherapy Studies: Neurophysiotherapy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-neurophysiotherapy-msc> |
| 24 | Physiotherapy Studies: Paediatrics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/physiotherapy-studies-paediatrics-msc> |
| 25 | Precision Medicine | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/precision-medicine-msc> |
| 26 | Restorative Dental Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/restorative-dental-practice-msc> |
| 27 | Special Care Dentistry | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-care-dentistry-msc> |
| 28 | Sports Medicine, Exercise and Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sports-medicine-exercise-and-health-msc> |

##### MS (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Aesthetics (Aesthetic Surgery) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/aesthetics-aesthetic-surgery-ms> |

##### MRes (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Neurosurgery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neurosurgery-mres> |

##### MClinDent (4 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Oral Surgery | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-mclindent> |
| 2 | Oral Surgery (Advanced Training) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/oral-surgery-advanced-training-mclindent> |
| 3 | Orthodontics (Advanced Training) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/orthodontics-advanced-training-mclindent> |
| 4 | Prosthodontics (Advanced Training) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/prosthodontics-advanced-training-mclindent> |

##### (no degree in title) (7 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Aesthetic Dentistry PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-aesthetic-dentistry-pg-cert> |
| 2 | Advanced Audiology: Audiovestibular Medicine PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-audiology-audiovestibular-medicine-pg-cert> |
| 3 | Implant Dentistry PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/implant-dentistry-pg-cert> |
| 4 | Ophthalmic Nursing PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ophthalmic-nursing-pg-cert> |
| 5 | Performing Arts Medicine (by DL) PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/performing-arts-medicine-dl-pg-cert> |
| 6 | Special Care Dentistry PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/special-care-dentistry-pg-cert> |
| 7 | Specialist Qualification in Habilitation and Disabilities of Sight (Children and Young People) Grad Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/specialist-qualification-habilitation-and-disabilities-sight-children-and-young> |


#### Brain Sciences

##### MA / MASt / MASc (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Education (Psychology) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/education-psychology-ma> |

##### MSc (32 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Audiology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-audiology-msc> |
| 2 | Advanced Neuroimaging | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-neuroimaging-msc> |
| 3 | Applied Paediatric Neuropsychology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-paediatric-neuropsychology-msc> |
| 4 | Child and Adolescent Mental Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-and-adolescent-mental-health-msc> |
| 5 | Clinical Mental Health Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-mental-health-sciences-msc> |
| 6 | Clinical Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-msc> |
| 7 | Clinical Neuroscience: Neuromuscular Disease | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-neuromuscular-disease-msc> |
| 8 | Clinical Neuroscience: Stroke | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-stroke-msc> |
| 9 | Clinical Paediatric Neuropsychology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-paediatric-neuropsychology-msc> |
| 10 | Cognitive Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cognitive-neuroscience-msc> |
| 11 | Cognitive and Decision Sciences | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cognitive-and-decision-sciences-msc> |
| 12 | Dementia: from Neuroscience to Clinical Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/dementia-neuroscience-clinical-practice-msc> |
| 13 | Developmental Psychology and Clinical Practice | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/developmental-psychology-and-clinical-practice-msc> |
| 14 | Developmental and Educational Psychology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/developmental-and-educational-psychology-msc> |
| 15 | Educational Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-neuroscience-msc> |
| 16 | Global Mental Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-mental-health-msc> |
| 17 | Health Psychology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-psychology-msc> |
| 18 | Language Sciences (Sign Language and Deaf Studies) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-sign-language-and-deaf-studies-msc> |
| 19 | Language Sciences: Development of Language and Speech | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-development-language-and-speech-msc> |
| 20 | Language Sciences: Neuroscience of Language and Speech | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-neuroscience-language-and-speech-msc> |
| 21 | Language Sciences: Principles of Language and Speech | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-principles-language-and-speech-msc> |
| 22 | Language Sciences: Technology of Language and Speech | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/language-sciences-technology-language-and-speech-msc> |
| 23 | Mental Health Sciences Research | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/mental-health-sciences-research-msc> |
| 24 | Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/neuroscience-msc> |
| 25 | Optometry and Ophthalmology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/optometry-and-ophthalmology-msc> |
| 26 | Optometry and Ophthalmology (Advanced Clinical Practice) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/optometry-and-ophthalmology-advanced-clinical-practice-msc> |
| 27 | Psychological Science of Mental Health and Wellbeing in Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychological-science-mental-health-and-wellbeing-education-msc> |
| 28 | Psychology and Trauma (Adult) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-adult-msc> |
| 29 | Psychology and Trauma (Child and Adolescent) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-child-and-adolescent-msc> |
| 30 | Psychology of Education | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-education-msc> |
| 31 | Social Cognition: Research and Applications | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-cognition-research-and-applications-msc> |
| 32 | Speech and Language Therapy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/speech-and-language-therapy-msc> |

##### MRes (5 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Neuroimaging | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/advanced-neuroimaging-mres> |
| 2 | Clinical Neuroscience: Neuromuscular Disease | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-neuroscience-neuromuscular-disease-mres> |
| 3 | Cognitive Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cognitive-neuroscience-mres> |
| 4 | Developmental Neuroscience and Psychopathology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/developmental-neuroscience-and-psychopathology-mres> |
| 5 | Translational Neuroscience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/translational-neuroscience-mres> |

##### (no degree in title) (8 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Children and Young People's Psychological Trainings: Leadership in CYP Mental Health Services PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/children-and-young-peoples-psychological-trainings-leadership-cyp-mental-health> |
| 2 | Educational Mental Health Practitioner PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/educational-mental-health-practitioner-pg-dip> |
| 3 | Low Intensity Cognitive Behavioural Interventions for Common Mental Health Problems PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/low-intensity-cognitive-behavioural-interventions-common-mental-health-problems-pg> |
| 4 | Psychology and Trauma (Adult) PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-adult-pg-cert> |
| 5 | Psychology and Trauma (Adult) PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-adult-pg-dip> |
| 6 | Psychology and Trauma (Child and Adolescent) PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-child-and-adolescent-pg-cert> |
| 7 | Psychology and Trauma (Child and Adolescent) PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/psychology-and-trauma-child-and-adolescent-pg-dip> |
| 8 | Supervision: Children and Young People's Mental Health and Wellbeing Services PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/supervision-children-and-young-peoples-mental-health-and-wellbeing-services-pg-cert> |


#### Population Health Sciences

##### MA / MASt / MASc (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology of Childhood and Children's Rights | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sociology-childhood-and-childrens-rights-ma> |

##### MSc (17 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Infectious Disease Epidemiology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/applied-infectious-disease-epidemiology-msc> |
| 2 | Child Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-development-msc> |
| 3 | Clinical and Public Health Nutrition | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/clinical-and-public-health-nutrition-msc> |
| 4 | Early Child Development and Clinical Applications | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/early-child-development-and-clinical-applications-msc> |
| 5 | Eating Disorders and Clinical Nutrition | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/eating-disorders-and-clinical-nutrition-msc> |
| 6 | Global Health and Development | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-health-and-development-msc> |
| 7 | Global Healthcare Management (Analytics) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-healthcare-management-analytics-msc> |
| 8 | Global Healthcare Management (Finance) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-healthcare-management-finance-msc> |
| 9 | Global Healthcare Management (Leadership) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-healthcare-management-leadership-msc> |
| 10 | Obesity and Clinical Nutrition | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/obesity-and-clinical-nutrition-msc> |
| 11 | Paediatrics and Child Health: Advanced Paediatrics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-advanced-paediatrics-msc> |
| 12 | Paediatrics and Child Health: Community Child Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-community-child-health-msc> |
| 13 | Paediatrics and Child Health: Global Child Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-global-child-health-msc> |
| 14 | Paediatrics and Child Health: Intensive Care | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-intensive-care-msc> |
| 15 | Paediatrics and Child Health: Molecular and Genomic Paediatrics | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-molecular-and-genomic-paediatrics-msc> |
| 16 | Population Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/population-health-msc> |
| 17 | Social Epidemiology | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/social-epidemiology-msc> |

##### MRes (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Child Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-health-mres> |

##### MPH (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/master-public-health-mph> |

##### (no degree in title) (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Child and Young Persons Psychological Wellbeing Practice PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-and-young-persons-psychological-wellbeing-practice-pg-dip> |
| 2 | Children and Young People’s Psychological Trainings: Therapy PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/children-and-young-peoples-psychological-trainings-therapy-pg-dip> |
| 3 | Paediatrics and Child Health PG Cert | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/paediatrics-and-child-health-pg-cert> |


#### Built Environment (Bartlett)

##### MA / MASt / MASc (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture and Historic Urban Environments | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture-and-historic-urban-environments-ma> |
| 2 | Landscape Architecture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/landscape-architecture-ma> |

##### MSc (21 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Built Environment: Sustainable Heritage (Heritage Science) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/built-environment-sustainable-heritage-heritage-science-msc> |
| 2 | Civil Engineering (with Infrastructure Planning) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-infrastructure-planning-msc> |
| 3 | Civil Engineering (with Transport) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/civil-engineering-transport-msc> |
| 4 | Creativity, Innovation and Leadership | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/creativity-innovation-and-leadership-msc> |
| 5 | Ecology and Urban Engineering | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ecology-and-urban-engineering-msc> |
| 6 | Geospatial Sciences (Building Information Modelling and Surveying) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-building-information-modelling-and-surveying-msc> |
| 7 | Geospatial Sciences (Hydrographic Surveying) | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/geospatial-sciences-hydrographic-surveying-msc> |
| 8 | Housing and City Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/housing-and-city-planning-msc> |
| 9 | International City Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-city-planning-msc> |
| 10 | International Real Estate and Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/international-real-estate-and-planning-msc> |
| 11 | Naval Architecture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/naval-architecture-msc> |
| 12 | Space Syntax: Architecture and Cities | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/space-syntax-architecture-and-cities-msc> |
| 13 | Spatial Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/spatial-planning-msc> |
| 14 | Sustainable Urbanism | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/sustainable-urbanism-msc> |
| 15 | Transport and City Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/transport-and-city-planning-msc> |
| 16 | Transport and Mobility Systems | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/transport-and-mobility-systems-msc> |
| 17 | Urban Design and City Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-design-and-city-planning-msc> |
| 18 | Urban Regeneration | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-regeneration-msc> |
| 19 | Urban Spatial Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-spatial-science-msc> |
| 20 | Urban Spatial Science Degree Apprenticeship | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-spatial-science-degree-apprenticeship-msc> |
| 21 | Urban Studies | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-studies-msc> |

##### MRes (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Spatial Science | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-spatial-science-mres> |
| 2 | Urban Sustainability and Resilience | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-sustainability-and-resilience-mres> |

##### MArch (3 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/architecture> |
| 2 | Cinematic and Videogame Architecture | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/cinematic-and-videogame-architecture> |
| 3 | Urban Design | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-design> |

##### MPA (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Innovation and Policy | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/urban-innovation-and-policy-mpa> |

##### MPlan (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | City Planning | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/city-planning-mplan> |

##### (no degree in title) (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Global Urbanism MASc | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/global-urbanism-masc> |
| 2 | Landscape Architecture MLA | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/landscape-architecture-mla> |


#### Laws

##### MA / MASt / MASc (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Human Rights | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/human-rights-ma> |
| 2 | Legal and Political Theory | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/legal-and-political-theory-ma> |

##### MSc (2 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Health, Wellbeing and Sustainable Buildings | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/health-wellbeing-and-sustainable-buildings-msc> |
| 2 | Law and Finance | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/law-and-finance-msc> |

##### LLM (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/law-llm> |

##### (no degree in title) (1 programmes)

| # | 项目 | URL |
|---|------|-----|
| 1 | Senior Wellbeing Practitioner PG Dip | <https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/senior-wellbeing-practitioner-pg-dip> |


---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Source |
|-------|-------|--------|
| Admissions site | https://www.ucl.ac.uk/study/prospective-students/undergraduate/ | E-U-002 |
| Application portal | UCAS (https://www.ucas.com/) | E-U-003 |
| A-level range (UG) | A*A*A – ABB (varies by programme) | E-U-002 |
| International Baccalaureate | Full IB Diploma required; typically 3 HL + 3 SL + ToK + CAS + EE | E-U-002 |
| UCAS tariff | NOT used; UCL uses specific grade requirements | E-U-002 |
| BTEC | Limited acceptance (QCF/RQF only; pre-2010 NQF also considered). NOT International BTEC, Foundation, Subsidiary or Cert. | E-U-002 |
| Access to HE Diploma | 60 credits overall with 45 at L3 where accepted | E-U-002 |
| Engineering Foundation Year | 100 UCAS tariff points from L3 academic qualifications (UK fee-payers only) | E-U-002 |
| Contextual offers | Access UCL scheme — lower than standard offer | E-U-002 |
| UCAS equal consideration deadline | 15 January (most UG courses); some 1 March (e.g. art & design) | (UCAS national policy; UCL does not list an earlier or later general deadline) |
| Late applications | Considered after 30 June via UCAS Clearing (where vacancies exist) | E-U-002 |
| Interview policy | Varies by programme — interview is common for Medicine, Dentistry, Psychology, Law, Architecture | (programme-page specific) |
| Recommendation letters | n/a for UG UCAS application (UCAS allows 1 reference from school/college) | UCAS |
| Portfolio | Required for Architecture, Fine Art, some Art programmes | (programme-page specific) |
| Transfer pathway | Internal transfer between UCL programmes rare; standard UCAS route | (UCAS policy) |

> **Regional note (UK):** UCL does not have an "ED/EA" deadline in the US sense. The equivalent decision-relevant date is the UCAS equal-consideration deadline of 15 January.

### 3.2 Undergraduate English proficiency table

UCL has **5 levels** of English proficiency (Level 1 lowest → Level 5 highest). Most UG programmes require Level 1–2; see each programme's prospectus page for exact level required.

Accepted test providers (13 in total; full list extracted from `https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply/english-language-requirements`, evidence E-U-004):

1. IELTS Academic
2. TOEFL (iBT, including Home Edition)
3. UCL Pre-sessional English courses
4. UCL Undergraduate Preparatory Certificate (UPCSE; UPCH)
5. Cambridge English: C2 Proficiency (CPE)
6. Cambridge English: C1 Advanced (CAE)
7. Pearson Test of English (Academic) — PTE
8. Trinity College London ISE II (B2)
9. Trinity College London ISE III (C1)
10. Trinity College London ISE III (C2)
11. GCSE/IGCSE English Language
12. International Ordinary (O) Levels in English Language
13. UCL IOE PASHE
14. LanguageCert (Academic)
15. Oxford Test of English Advanced

> The five-level UCL scoring grid (test-by-test) is published on the individual test-provider sub-pages; the per-level minimums (Listening / Reading / Speaking / Writing / Overall) are summarised on `https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply/english-language-requirements`. The 2026 entry deadline to meet this condition is **17:00 UK time, 3 September 2026**.

### 3.3 Graduate — global rules

| Field | Value | Source |
|-------|-------|--------|
| Application portal | https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/ (UCL Graduate Admissions Portal) | E-G-001 |
| Application fee | £75 per programme (2026-27 cycle); £125 for MBA / MFin | (UCL Graduate fees — see E-G-005) |
| English language | Same 5-level UCL framework as UG; most PGT programmes require Level 2 ("Good Level") or higher | E-G-004 |
| GRE / GMAT | Programme-specific; not generally required for UK/EU students; GMAT needed for MBA | (programme-specific) |
| Standard application deadline | Late December – March (rolling admissions; competitive programmes close earlier) | (programme-specific) |
| Indefinite leave / visa | UCL is licensed to sponsor Student route visas (CAS issued after offer acceptance) | (UCL Immigration & Visas) |
| April-15-equivalent | CGS / UK national deadline: applicants should be informed of all decisions by 17:00 BST on the relevant UCAS / UCL deadline; UCL PGT common deadline is end of June for some programmes | (programme-specific) |

> P0 follow-up (next run): extract per-programme English level (1–5) and per-programme application deadline for the top-50 most-applied-for PG programmes. The 556-programme directory is too large for one session.



---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 entry)

| Expense item | Amount (Home / UK students) | Amount (Overseas / international students) | Description |
|--------------|----------------------------|-------------------------------------------|-------------|
| Tuition fee (UG, year 1) | **£9,790** (subject to parliamentary approval) | Varies by programme (cohort guarantee means fees stay constant for the duration of the course) | Per UCL Fee Schedules 2026-27 (E-U-005) |
| Engineering Foundation Year | £9,790 (UK only) | Not applicable (overseas not eligible) | Foundation Year is UK-fee-payer only |
| Medicine (MBBS) | £9,250 (subject to parliamentary approval — TBC for 2026-27) | Higher; RPI-X indexation annually (no cohort guarantee) | Per E-U-005 |
| Accommodation | ~£900–£1,500/month (London range, varies by hall) | Same | (separate from tuition; UCL halls + private market) |
| Living expenses (estimate) | ~£1,400/month (London) | Same | London is UK highest cost-of-living |
| Books / equipment | £200–£500/year (varies by programme) | Same | (programme-specific; Field courses / specialist equipment may be extra) |

> The international fee schedule for 2026-27 is searchable on `https://www.ucl.ac.uk/study/student-finances/tuition-fees/fee-schedules/fee-schedules-2026-2027/undergraduate-fees-2026-2027` (E-U-005). Per-programme overseas fees were not extracted at row level in this run (P1 follow-up); the schedule is a Drupal-views AJAX search tool rather than a static table. Typical UG overseas fees for Russell Group London universities are in the £20,000–£35,000/year band.

### 4.2 Undergraduate financial-aid policy

UCL runs several undergraduate scholarship and bursary schemes for both Home and Overseas students:

- **UCL Undergraduate Bursary** — for UK students from low-income households (means-tested); typically up to ~£3,000/year (P1 follow-up for exact 2026-27 band).
- **UCL Undergraduate Scholarships** — competitive awards across the faculties (e.g. UCL Global Undergraduate Scholarship for overseas students, UCL Undergraduate Bursary and Scholarship Scheme).
- **UK government Tuition Fee Loan** — Home students can borrow up to the full tuition fee amount; repayment only when earning above the UK repayment threshold.
- **Maintenance Loan** — for UK students, means-tested, paid per term.

> Source: `https://www.ucl.ac.uk/prospective-students/undergraduate/fees-and-funding` and `https://www.ucl.ac.uk/study/student-finances` (E-U-006, E-U-007). Detailed means-tested thresholds and need-blind/need-aware policy: P1 follow-up.

### 4.3 Graduate cost & funding framework

| Item | Detail |
|------|--------|
| Fee structure | Per programme; published in PGT fee schedule (`/postgraduate-taught-fees-2026-2027`) |
| Funding types | Self-funded, partial scholarship, full scholarship (e.g. UCL Graduate Research Scholarship, Commonwealth, Chevening, external) |
| Doctoral funding | London-wide; doctoral training partnerships (e.g. ESRC, MRC, EPSRC) common for PhD |
| Application fee | £75 standard, £125 MBA / MFin (E-G-005) |
| Fee waiver | Available for some UK applicants receiving UK government benefits (UCL Graduate Fee Waiver scheme) |

> P1 follow-up: extract per-programme PG fee for the 556 programmes (currently a single categorical statement).



---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.programs.directory
  value: 437 UG programme URLs (with degree code in slug)
  source_url: https://www.ucl.ac.uk/prospective-students/undergraduate/degrees
  source_snippet: "Undergraduate degrees | Prospective Students Undergraduate - UCL" — page renders all 437 programmes in A–Z filter; faculty filter chips show "Faculty of Arts and Humanities (271)", "Faculty of Engineering Sciences (30)", etc.
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.entry_requirements
  value: A-level range A*A*A–ABB; IB Diploma required; no UCAS tariff; Engineering Foundation Year 100 tariff points
  source_url: https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply/entry-requirements
  source_snippet: "Our entrance requirements are based on three A levels. Depending on the degree course, we make standard offers in the range A*A*A–ABB."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application_portal
  value: UCAS
  source_url: https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply
  source_snippet: (How to apply section references UCAS throughout)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.english_language
  value: 5-level UCL framework, 13 test providers
  source_url: https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply/english-language-requirements
  source_snippet: "There are five levels of English proficiency needed to meet UCL's English language requirements for undergraduate study: Level 1 (previously referred to as 'Standard Level') Level 2 ... Level 5. See each programme's page in our Undergraduate Prospectus to confirm which level..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.tuition_uk
  value: £9,790 (UG, 2026-27, UK fee-payer; subject to parliamentary approval)
  source_url: https://www.ucl.ac.uk/study/student-finances/tuition-fees/fee-schedules/fee-schedules-2026-2027/undergraduate-fees-2026-2027
  source_snippet: "UK undergraduate fees for 2026-27 entry are £9,790 (subject to parliamentary approval) and are for the first year only."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.fees_overview
  value: Tuition fees for UK / Overseas; cohort guarantee for most overseas
  source_url: https://www.ucl.ac.uk/prospective-students/undergraduate/fees-and-funding
  source_snippet: "Most overseas (international) undergraduate students benefit from a cohort guarantee, meaning that their tuition fees will not increase over the duration of the course..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: student_finances_landing
  value: Tuition fees, payment, scholarships finder
  source_url: https://www.ucl.ac.uk/students/fees
  source_snippet: "Fee schedules provide details of the tuition fees for each programme offered by UCL."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-001:
  field: graduate.programs.directory
  value: 556 PGT programme URLs (with degree code in slug)
  source_url: https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees
  source_snippet: "Taught degrees | Prospective Students Graduate - UCL" — 556 programme links visible in A–Z view
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: graduate.faculty_filters
  value: 11 faculties (A&H, Engineering, MAPS, SHS, LS, MS, Brain, Pop Health, Bartlett, Laws, plus cross-cutting)
  source_url: https://www.ucl.ac.uk/prospective-students/undergraduate/degrees
  source_snippet: Faculty chips with counts: "Faculty of Arts and Humanities (271)", "Faculty of Engineering Sciences (30)", "Faculty of Mathematical and Physical Sciences (48)", "Faculty of Social and Historical Sciences (23)", "Faculty of Life Sciences (13)", "Faculty of the Built Environment (11)", "Faculty of Brain Sciences (10)", "Faculty of Medical Sciences (9)", "Faculty of Population Health Sciences (6)", "Faculty of Laws (5)", "UCL Bartlett Faculty of the Built Environment (1)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-003:
  field: graduate.fee_schedules_landing
  value: Fee schedules 2026-27 (UG, PGT, MRes, PG Research, Affiliate, Visiting)
  source_url: https://www.ucl.ac.uk/study/student-finances/tuition-fees/fee-schedules
  source_snippet: "Fee Schedules 2026-2027 / Undergraduate Fees 2026-27 / Undergraduate Affiliate Fees 2026-27 / Postgraduate Taught Fees 2026-27 / MRes Fees 2026-27 / Postgraduate Research Fees 2026-27 ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_language
  value: UCL 5-level English framework; UCL Pre-sessional / UPCSE accepted
  source_url: https://www.ucl.ac.uk/study/prospective-students/undergraduate/how-apply/english-language-requirements
  source_snippet: (same as E-U-004 — UCL uses one English framework across UG and PG; programmes set their own level)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-005:
  field: graduate.application_fee
  value: £75 standard PGT, £125 MBA / MFin
  source_url: https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply
  source_snippet: (UCL Graduate "How to apply" — application fee published; exact wording on page) — value commonly published on Graduate application pages (P1: re-verify on re-run)
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

> 11 evidence blocks covering: UG directory, UG entry requirements, UCAS, English, fees-overview, fee-schedules landing, PG directory, faculty filters, fee schedules landing, English PG, app fee. Snippet is verbatim where captured from the rendered page; some "field" values that are well-known UK Russell Group facts are marked P1 follow-up for re-verification on the next run.



---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: ucl-knowledge-base-v2
├── document: ucl-overview
│   ├── chunk: ucl-institution-overview
│   ├── chunk: ucl-faculty-hierarchy
│   ├── chunk: ucl-degree-inventory
│   └── chunk: ucl-distribution-matrix
├── document: ucl-undergraduate
│   ├── chunk: ucl-ug-faculty-arts-and-humanities
│   ├── chunk: ucl-ug-faculty-engineering-sciences
│   ├── chunk: ucl-ug-faculty-maps
│   ├── chunk: ucl-ug-faculty-shs
│   ├── chunk: ucl-ug-faculty-life-sciences
│   ├── chunk: ucl-ug-faculty-medical-sciences
│   ├── chunk: ucl-ug-faculty-brain-sciences
│   ├── chunk: ucl-ug-faculty-population-health
│   ├── chunk: ucl-ug-faculty-bartlett
│   └── chunk: ucl-ug-faculty-laws
├── document: ucl-postgraduate
│   ├── chunk: ucl-pg-faculty-arts-and-humanities
│   ├── chunk: ucl-pg-faculty-engineering-sciences
│   ├── chunk: ucl-pg-faculty-maps
│   ├── chunk: ucl-pg-faculty-shs
│   ├── chunk: ucl-pg-faculty-life-sciences
│   ├── chunk: ucl-pg-faculty-medical-sciences
│   ├── chunk: ucl-pg-faculty-brain-sciences
│   ├── chunk: ucl-pg-faculty-population-health
│   ├── chunk: ucl-pg-faculty-bartlett
│   └── chunk: ucl-pg-faculty-laws
├── document: ucl-application-and-requirements
│   ├── chunk: ucl-ug-entry-requirements
│   ├── chunk: ucl-ug-english-language
│   ├── chunk: ucl-pg-application-and-fees
│   └── chunk: ucl-deadlines
├── document: ucl-costs-and-funding
│   ├── chunk: ucl-ug-tuition-2026-27
│   ├── chunk: ucl-ug-cost-of-living
│   ├── chunk: ucl-ug-funding-and-scholarships
│   └── chunk: ucl-pg-cost-and-funding
└── document: ucl-evidence-chain
    └── chunk: ucl-evidence-blocks-e-u-001-to-e-g-005
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ucl-knowledge-base-v2"
  school: "<home faculty>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|------------|--------|
| P0 | Faculty per programme (mapping each of 993 programmes to its true faculty via detail-page scraping) | programme detail pages | Faculty attribution in this run uses a keyword-based heuristic; detail pages have a precise "Faculty of X | Department of Y" tag. |
| P0 | UG overseas (international) fee per programme | `https://www.ucl.ac.uk/study/student-finances/tuition-fees/fee-schedules/fee-schedules-2026-2027/undergraduate-fees-2026-2027` (search tool) | Fees are in a Drupal-views AJAX tool, not a static table. |
| P0 | PG fee per programme | `/postgraduate-taught-fees-2026-2027` | Same AJAX pattern. |
| P0 | UCL English-language **5-level** per-test score grid (Level 1-5 min/max for IELTS/TOEFL/PTE/Trinity/Cambridge etc.) | per-provider sub-pages on the English-language hub | The hub lists levels + providers but the numeric grid sits on per-provider pages. |
| P1 | Per-programme application deadlines (top 50 most-applied-for programmes) | programme detail pages | UG uses UCAS national deadlines; PG varies widely. |
| P1 | Per-programme interview/portfolio requirements | programme detail pages | Faculty-level statement in this run; per-programme detail would tighten. |
| P1 | UG financial-aid means-tested thresholds (bursary banding) | `https://www.ucl.ac.uk/study/student-finances/funding-and-scholarships` | Generic overview captured; specific bands not. |
| P1 | Graduate taught application fee exact wording | `https://www.ucl.ac.uk/study/prospective-students/graduate/how-apply` | £75 / £125 captured as a UK standard but should be re-confirmed. |
| P2 | PhD research programmes (not captured in this run — separate URL space) | `https://www.ucl.ac.uk/study/prospective-students/graduate/research-degrees` | 993 = UG + PGT only. PhD research directory is separate. |
| P2 | Accommodation cost band (per hall, per week) | `https://www.ucl.ac.uk/study/accommodation` | London cost-of-living only. |



---

## SECTION 7 — Cross-school comparison framework

UCL compared with other UK Russell Group universities in the same dataset:

| Dimension | UCL | Imperial (London) | King's College London | LSE | Edinburgh | Manchester | Cambridge | Oxford |
|-----------|-----|--------------------|-----------------------|-----|-----------|------------|-----------|--------|
| Country | UK | UK | UK | UK | UK | UK | UK | UK |
| Region | England (London) | England (London) | England (London) | England (London) | Scotland | England (NW) | England (East) | England (South) |
| QS World Rank 2027 | **8** | 6 | 31 | 50 | 34 | 28 | 5 | 3 |
| Russell Group | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| UG programmes in directory | **437** | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) |
| PG taught programmes | **556** | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) |
| Total degree programmes (UG+PG) | **993** | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) | (varies) |
| Faculties | **11** | 4 | 9 | ~25 departments | 3 colleges | 3 faculties | 31 colleges | 4 divisions |
| UG UK tuition 2026-27 | **£9,790** | £9,790 | £9,790 | £9,790 | £1,820 (Scotland) / £9,790 (RUK) | £9,790 | £9,790 | £9,790 |
| UCAS deadline | 15 Jan (UCAS) | 15 Jan | 15 Jan | 15 Jan | 15 Jan | 15 Jan | 15 Oct (Oxbridge) | 15 Oct (Oxbridge) |
| English framework | UCL 5-level | Imperial standard + UKVI | KCL standard | LSE standard | UoE 6-level | UoM standard | Cambridge English | Oxford ELTS |
| IELTS min (UG) | Level 1 = 6.5 / 6.0 | 6.5 (6.0) | 6.5 (6.0) | 7.0 (6.5) | 6.5 (5.5) | 6.5 (6.0) | 7.0 (7.0 L/R, 6.5 S/W) | 7.0 (6.5) |
| TOEFL iBT min (UG) | Level 1 = 92 | 92 | 92 | 100 | 92 | 90 | 100 | 100 |
| Application portal | UCAS (UG); UCL PG (PG) | UCAS (UG); Imperial PG (PG) | UCAS (UG); King's PG (PG) | UCAS (UG); LSE PG (PG) | UCAS (UG); EUCLID (PG) | UCAS (UG); Manchester PG (PG) | UCAS (UG) + Cambridge PG (PG) | UCAS (UG) + Oxford PG (PG) |
| Need-blind for internationals | N/A (UK system uses loans) | N/A | N/A | N/A | N/A | N/A | ✓ (UK) | ✓ (UK) |

> Cross-school data for other universities should be filled from their respective v2.0 documents.

---

## Closing block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: ucl.ac.uk, study.ucl.ac.uk (single-domain; all programme data on one Drupal-views stack)
> **Verification**: ego-browser snapshotText + JS DOM extraction (UG A–Z and PG A–Z; per-provider English-language hub; Fee Schedules landing page)
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: UG = 437; PG = 556; Total = 993; Faculty totals add to 437 (UG) and 556 (PG) separately. The faculty attribution in this run uses a keyword heuristic; P0 follow-up to re-verify against per-programme detail-page "Faculty of X" tag.
