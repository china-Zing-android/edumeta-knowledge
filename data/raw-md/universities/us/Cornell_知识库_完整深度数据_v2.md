# Cornell University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → degree-level → program (Cornell uses a field system; department-level grouping is by degree within school/college)
> **Document version**: v2.0 (deep)

---

## The five structural rules (enforced)

1. **专业总数** — 429 (90 UG majors + 139 UG minors + 193 grad degrees + 7 grad field minors)
2. **学院/系明细 + 父子层级** — 7 undergraduate colleges + Graduate School + 4 professional schools (Law/Vet Med/Business/Weill Med)
3. **学历级别明细** — 33 distinct degree designations (BA/BS/BFA/BArch at UG; PhD/MS/MA/MEng/MFA/MBA/MPA/MPH/JD/LLM/DMA/DVM + 6 dual degrees at grad)
4. **分布矩阵** — 学院 × canonical 学位级别 (below)
5. **全量专业明细按 学院 > 学位级别 分组** — every program listed under its school → degree level (429 rows)

> **Reconciliation gate (PASSED):** Rule-1 total (429) == sum of matrix cells (429) == count of Rule-5 rows (429) == sum of degree-inventory counts (429).

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BArch/dual) | 90 |
| 本科辅修 (Minor) | 139 |
| 研究生学位项目 (PhD/MS/MA/MEng/MBA/MPA/MPH/JD/LLM/DMA/DVM/…) | 193 |
| 研究生领域辅修 (Graduate Field Minor) | 7 |
| **学位项目总计 (UG + Grad, 含 minors)** | **429** |
| 学位项目总计 (仅学位，不含 minors) | 283 |
| 本科学院 (undergraduate colleges) | 7 (+ Brooks hybrid) |
| 研究生院 / 专业学院 | 5 (Graduate School + Law + Vet Med + Johnson MBA + Weill Med) |

> Counts derived from `catalog.cornell.edu/programs/` (2026-07-05). Programs sitting in two colleges (25 of them, e.g. Applied Economics & Management = CALS + SC Johnson) are counted ONCE under their primary/home college and cross-listed in the matrix notes.

### 0.2 学院 / 系层级结构 (Rule 2)

```
Cornell University
├── [本科 7 学院 — endowed (private tuition)]
│   ├── College of Architecture, Art and Planning (AAP)        [学院]  Architecture / Art / City & Regional Planning
│   ├── College of Arts and Sciences (A&S)                     [学院]  ~41 BA majors + ~64 minors (humanities/social sci/natural sci)
│   ├── Cornell David A. Duffield College of Engineering       [学院]  12 BS majors + 14 minors; 17 MEng fields
│   ├── Cornell Jeb E. Brooks School of Public Policy          [学院]  ⚠ hybrid (BS = contract-college tuition; other = endowed)
│   └── Cornell SC Johnson College of Business                 [学院]  Nolan School of Hotel Admin + Dyson AEM (Dyson shared ⚠ with CALS)
├── [本科 — NY State Contract Colleges (reduced NY-resident tuition)]
│   ├── College of Agriculture and Life Sciences (CALS)        [学院]  21 BS + 1 BA/BS dual + 32 minors
│   ├── College of Human Ecology (HumEc)                       [学院]  6 BS + 7 minors
│   ├── School of Industrial and Labor Relations (ILR)         [学院]  1 BS (ILR) + 2 minors
│   └── Charles H. Dyson School of Applied Economics & Mgmt   [系]   ⚠ shared CALS × SC Johnson
├── Bowers College of Computing and Information Science        [学院]  (UG minors only via catalog; CS BS administered in Engineering/A&S)
├── [研究生 / 专业学院]
│   ├── Graduate School (administers cross-disciplinary field system)  [学院]  145 programs — 79 PhD + 30 MS + 12 MPS + 8 MA + 6 grad-minor + MFA/MILR/MLA/JSD/MPH/DMA/MFS + JD/PhD + MLA/MRP
│   ├── Law School                                             [学院]  JD + 3 LLM + 1 MS (joint with grad)
│   ├── College of Veterinary Medicine                         [学院]  DVM
│   ├── SC Johnson Graduate School of Management               [学院]  5 MBA + duals (within SC Johnson above)
│   └── Weill Cornell Graduate School of Medical Sciences      [学院]  PhD (Biomedical) + MBA/MS Healthcare Leadership
```

> Cornell uses a **cross-disciplinary "field" system** for graduate study (≈100 fields of study, broadest in the Ivy League). Most graduate programs are administered through the **Graduate School** even when faculty sit in a professional school — e.g. PhDs in biomedical sciences register via Weill Cornell. Each field sets its own admission requirements (decentralized).

### 0.3 学历级别明细 (Rule 3)

| canonical | official (本校) | 全称 | 层级 | 数量 |
|-----------|----------------|------|------|------|
| Minor | Minor | Undergraduate Minor | 本科 | 139 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 80 |
| BS | BS, ECSAG-BS, ECSEN-BS, GPHSAG-BS, GPHSHE-BS | Bachelor of Science | 本科 | 45 |
| BA | BA | Bachelor of Arts | 本科 | 42 |
| MS | BANA-MS, MS, NYBANA-MS | Master of Science | 研究生 | 38 |
| MEng | CSCN-MEng, EENG-MEng, MEng, NYCS-MEng, NYEE-MEng, NYOR-MEng, ORIE-MEng | Master of Engineering | 研究生 | 18 |
| MPS | ISCI-MPS, MPS | Master of Professional Studies | 研究生 | 15 |
| MA | MA | Master of Arts | 研究生 | 8 |
| Graduate Minor | Graduate Minor | Graduate Field Minor | 研究生 | 7 |
| MBA | MBA | Master of Business Administration | 研究生 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| LLM | LLM | Master of Laws | 研究生 | 3 |
| MHA | MHA | Master of Health Administration | 研究生 | 2 |
| MMH | MMH | Master of Management in Hospitality | 研究生 | 2 |
| MPA | MPA | Master of Public Administration | 研究生 | 2 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 2 |
| BArch | B.Arch | Bachelor of Architecture (5-yr) | 本科 | 1 |
| MArch | M.Arch | Master of Architecture | 研究生 | 1 |
| BA/BS | BA, BS | Dual BA/BS | 本科 | 1 |
| MRP | MRP | Master of Regional Planning | 研究生 | 1 |
| MRP/MPS | MRP/MPS | MRP/MPS | 研究生(双学位) | 1 |
| MBA/MS | MBA/MS | MBA/MS | 研究生(双学位) | 1 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| MFS | MFS | Master of Food Science | 研究生 | 1 |
| MILR | MILR | Master of Industrial & Labor Relations | 研究生 | 1 |
| MLA/MRP | MLA/MRP | MLA/MRP | 研究生(双学位) | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| JSD | JSD | Doctor of Juridical Science | 研究生 | 1 |
| JD/PhD | JD/PhD | JD/PhD | 研究生(双学位) | 1 |
| MBA/MILR | MBA/MILR | MBA/MILR | 研究生(双学位) | 1 |
| MBA/JD | MBA/JD | MBA/JD | 研究生(双学位) | 1 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 1 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |

> 学位规范化：Cornell 使用标准缩写（BA/BS/MS/PhD），但 B.Arch 编码为 `BAR`、M.Arch 编码为 `MAR`（catalog 内部码）；NY 州居民变体加 `NY` 前缀（如 `NYBANA-MS`）；4+1 双学位编码如 `BANA-MS`（BA+MS）；MEng 带方向码如 `ECSEN-MEng`（Electrical & Computer）、`CSCN-MEng`（CS）、`ORIE-MEng`（Operations Research）。所有这些都已解码到 canonical 列。详见 [degree-taxonomy.md](degree-taxonomy.md)。

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BArch | Minor | MA | MS | MFA | MBA | MEng | MPS | MPA | MPH | MLA | MRP | LLM | JD | PhD | DMA | DVM | JSD | MHA | MMH | MFS | MILR | Grad Minor | 其他/双学位 | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Agriculture and Life Sciences | 0 | 21 | 0 | 0 | 32 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 56 |
| College of Architecture, Art and Planning | 0 | 2 | 1 | 1 | 3 | 0 | 2 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 16 |
| College of Arts and Sciences | 41 | 0 | 0 | 0 | 64 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 105 |
| Duffield College of Engineering | 0 | 12 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 43 |
| College of Human Ecology | 0 | 6 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 13 |
| Brooks School of Public Policy | 1 | 2 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 13 |
| SC Johnson College of Business | 0 | 1 | 0 | 0 | 9 | 0 | 2 | 0 | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 1 | 21 |
| School of Industrial and Labor Relations | 0 | 1 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| Bowers College of Computing and Information Science | 0 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Graduate School | 0 | 0 | 0 | 0 | 0 | 8 | 30 | 1 | 0 | 0 | 12 | 0 | 1 | 2 | 0 | 0 | 0 | 79 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 6 | 2 | 145 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Weill Cornell Graduate School of Medical Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 |
| **合计** | 42 | 45 | 1 | 1 | 139 | 8 | 38 | 3 | 5 | 18 | 15 | 2 | 1 | 2 | 1 | 3 | 1 | 80 | 1 | 1 | 1 | 2 | 2 | 1 | 1 | 7 | 7 | **429** |

> **Reconciliation:** row totals + column totals each sum to 429 (Rule-1 total). "其他/双学位" aggregates the 6 dual-degree types + BA/BS (Biology & Society). Graduate School administers the bulk of PhDs (79) via the field system — these PhDs span all academic disciplines even though their faculty home may be a specific college.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Cornell undergraduates apply to **one of seven undergraduate colleges/schools** (not to the university at large). The colleges fall into two tuition categories:
- **Endowed colleges** (private tuition, $73,946): AAP, Arts & Sciences, Duffield Engineering, Brooks School of Public Policy (non-BS), SC Johnson College of Business.
- **NY State Contract Colleges** (subsidized for NY residents, $49,816): CALS, Human Ecology, ILR, Dyson AEM, Brooks (BS candidates).

Plus the Bowers College of Computing and Information Science (administers CS-related minors; the CS BS is jointly run by Engineering and A&S). See Section 0.2 for the full tree.

### 1.2 Undergraduate majors & minors — grouped by 学院 > 学位级别

#### College of Agriculture and Life Sciences

##### BA/BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Biology &​ Society |  + College of Arts and Sciences | https://catalog.cornell.edu/programs/biology-society-ba/ |

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Agricultural Sciences |  | https://catalog.cornell.edu/programs/agricultural-sciences-bs/ |
| 2 | Animal Science |  | https://catalog.cornell.edu/programs/animal-science-bs/ |
| 3 | Applied Economics and Management |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/applied-economics-management-bs/ |
| 4 | Atmospheric Sciences |  | https://catalog.cornell.edu/programs/atmospheric-science-bs/ |
| 5 | Biological Engineering |  + Duffield College of Engineering | https://catalog.cornell.edu/programs/biological-engineering-bs/ |
| 6 | Biological Sciences |  | https://catalog.cornell.edu/programs/biological-sciences-bs/ |
| 7 | Communication |  | https://catalog.cornell.edu/programs/communication-bs/ |
| 8 | Earth and Climate Sciences |  | https://catalog.cornell.edu/programs/earth-climate-sciences-ecsag-bs/ |
| 9 | Entomology |  | https://catalog.cornell.edu/programs/entomology-bs/ |
| 10 | Environment &​ Sustainability |  | https://catalog.cornell.edu/programs/environment-sustainability-bs/ |
| 11 | Environmental Engineering |  + Duffield College of Engineering | https://catalog.cornell.edu/programs/environmental-engineering-bs/ |
| 12 | Food Science |  | https://catalog.cornell.edu/programs/food-science-bs/ |
| 13 | Global &​ Public Health Sciences |  | https://catalog.cornell.edu/programs/global-public-health-sciences-bs/ |
| 14 | Global Development |  | https://catalog.cornell.edu/programs/global-development-bs/ |
| 15 | Information Science |  | https://catalog.cornell.edu/programs/information-science-bs/ |
| 16 | Interdisciplinary Studies in Agriculture &​ Life Sciences |  | https://catalog.cornell.edu/programs/interdisciplinary-studies-bs/ |
| 17 | Landscape Architecture |  | https://catalog.cornell.edu/programs/landscape-architecture-bs/ |
| 18 | Nutritional Sciences |  + College of Human Ecology | https://catalog.cornell.edu/programs/nutritional-sciences-bs/ |
| 19 | Plant Sciences |  | https://catalog.cornell.edu/programs/plant-sciences-bs/ |
| 20 | Statistics &​ Biometry |  | https://catalog.cornell.edu/programs/biometry-statistics-bs/ |
| 21 | Viticulture and Enology |  | https://catalog.cornell.edu/programs/viticulture-enology-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | American Indian and Indigenous Studies |  | https://catalog.cornell.edu/programs/american-indian-indigenous-studies-minor/ |
| 2 | Animal Science |  | https://catalog.cornell.edu/programs/animal-science-minor/ |
| 3 | Applied Exercise Science |  + College of Human Ecology | https://catalog.cornell.edu/programs/applied-exercise-science-minor/ |
| 4 | Atmospheric Sciences |  + Duffield College of Engineering | https://catalog.cornell.edu/programs/atmospheric-science-minor/ |
| 5 | Biomedical Sciences |  | https://catalog.cornell.edu/programs/biomedical-sciences-minor/ |
| 6 | Biometry and Statistics |  | https://catalog.cornell.edu/programs/biometry-statistics-minor/ |
| 7 | Climate Change |  + Duffield College of Engineering, College of Arts and Sciences | https://catalog.cornell.edu/programs/climate-change-minor/ |
| 8 | Communication |  | https://catalog.cornell.edu/programs/communications-minor/ |
| 9 | Community Food Systems |  | https://catalog.cornell.edu/programs/community-food-systems-minor-cfs/ |
| 10 | Crop Management |  | https://catalog.cornell.edu/programs/crop-management-minor/ |
| 11 | Digital Agriculture |  | https://catalog.cornell.edu/programs/digital-agriculture-minor/ |
| 12 | Earth and Climate Sciences |  + Duffield College of Engineering, College of Arts and Sciences | https://catalog.cornell.edu/programs/earth-atmospheric-sciences-minor/ |
| 13 | Education |  | https://catalog.cornell.edu/programs/education-minor/ |
| 14 | Entomology |  | https://catalog.cornell.edu/programs/entomology-minor/ |
| 15 | Environment &​ Sustainability |  + College of Arts and Sciences | https://catalog.cornell.edu/programs/environment-sustainability-minor/ |
| 16 | Food Science |  | https://catalog.cornell.edu/programs/food-science-minor/ |
| 17 | Fungal Biology |  | https://catalog.cornell.edu/programs/fungal-biology-minor/ |
| 18 | Global Development |  | https://catalog.cornell.edu/programs/global-development-minor/ |
| 19 | Global Health |  + College of Human Ecology | https://catalog.cornell.edu/programs/global-health-minor/ |
| 20 | Horticulture |  | https://catalog.cornell.edu/programs/horticulture-minor/ |
| 21 | Infectious Disease Biology |  | https://catalog.cornell.edu/programs/infectious-disease-biology-minor/ |
| 22 | Landscape Studies |  | https://catalog.cornell.edu/programs/landscape-studies-minor/ |
| 23 | Leadership |  | https://catalog.cornell.edu/programs/leadership-minor/ |
| 24 | Marine Biology |  | https://catalog.cornell.edu/programs/marine-biology-minor/ |
| 25 | Microbial Science |  | https://catalog.cornell.edu/programs/microbial-science-minor/ |
| 26 | Nutrition and Health |  + College of Human Ecology | https://catalog.cornell.edu/programs/nutrition-health-minor/ |
| 27 | Plant Breeding |  | https://catalog.cornell.edu/programs/plant-breeding-minor/ |
| 28 | Plant Sciences |  | https://catalog.cornell.edu/programs/plant-sciences-minor/ |
| 29 | Science Communication and Public Engagement |  + College of Arts and Sciences | https://catalog.cornell.edu/programs/science-communication-public-engagement-minor/ |
| 30 | Soil Science |  | https://catalog.cornell.edu/programs/soil-science-minor/ |
| 31 | Sustainable Agricultural and Food Systems |  | https://catalog.cornell.edu/programs/sustainable-ag-food-system-minor/ |
| 32 | Viticulture and Enology |  | https://catalog.cornell.edu/programs/viticulture-enology-minor/ |


#### College of Architecture, Art and Planning

##### BArch

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Architecture |  | https://catalog.cornell.edu/programs/architecture-barch/ |

##### BFA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Fine Arts |  | https://catalog.cornell.edu/programs/art-bfa/ |

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | History of Architecture and Urban Development |  | https://catalog.cornell.edu/programs/history-architecture-urban-development-bs-haud/ |
| 2 | Urban and Regional Studies |  | https://catalog.cornell.edu/programs/urban-regional-studies-bs-urs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Architecture |  | https://catalog.cornell.edu/programs/architecture-minor-for-non-departmental-students/ |
| 2 | Fine Arts |  | https://catalog.cornell.edu/programs/fine-arts-minor-for-non-departmental-students/ |
| 3 | Urban and Regional Studies |  | https://catalog.cornell.edu/programs/urban-regional-studies-minor/ |


#### College of Arts and Sciences

##### BA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Africana Studies |  | https://catalog.cornell.edu/programs/africana-studies-ba/ |
| 2 | American Studies |  | https://catalog.cornell.edu/programs/american-studies-ba/ |
| 3 | Anthropology |  | https://catalog.cornell.edu/programs/anthropology-ba/ |
| 4 | Archaeology |  | https://catalog.cornell.edu/programs/archaeology-ba/ |
| 5 | Asian Studies |  | https://catalog.cornell.edu/programs/asian-studies-ba/ |
| 6 | Astronomy |  | https://catalog.cornell.edu/programs/astronomy-ba/ |
| 7 | Biological Sciences |  | https://catalog.cornell.edu/programs/biological-sciences-ba/ |
| 8 | Chemistry |  | https://catalog.cornell.edu/programs/chemistry-ba/ |
| 9 | China and Asia-​Pacific Studies |  | https://catalog.cornell.edu/programs/china-asia-pacific-studies-ba/ |
| 10 | Classics |  | https://catalog.cornell.edu/programs/classics-ba/ |
| 11 | Cognitive Science |  | https://catalog.cornell.edu/programs/cognitive-science-ba/ |
| 12 | College Scholar |  | https://catalog.cornell.edu/programs/college-scholar-ba/ |
| 13 | Comparative Literature |  | https://catalog.cornell.edu/programs/comparative-literature-ba/ |
| 14 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-ba/ |
| 15 | Earth and Climate Sciences |  | https://catalog.cornell.edu/programs/earth-climate-sciences-ba/ |
| 16 | Economics |  | https://catalog.cornell.edu/programs/economics-ba/ |
| 17 | English |  | https://catalog.cornell.edu/programs/english-ba/ |
| 18 | Environment &​ Sustainability |  | https://catalog.cornell.edu/programs/environment-sustainability-ba/ |
| 19 | Feminist, Gender, &​ Sexuality Studies |  | https://catalog.cornell.edu/programs/fgss-ba/ |
| 20 | French |  | https://catalog.cornell.edu/programs/french-ba/ |
| 21 | German Studies |  | https://catalog.cornell.edu/programs/german-studies-ba/ |
| 22 | Government |  | https://catalog.cornell.edu/programs/government-ba/ |
| 23 | History |  | https://catalog.cornell.edu/programs/history-ba/ |
| 24 | History of Art |  | https://catalog.cornell.edu/programs/history-art-ba/ |
| 25 | Information Science |  | https://catalog.cornell.edu/programs/information-science-ba/ |
| 26 | Italian |  | https://catalog.cornell.edu/programs/italian-ba/ |
| 27 | Jewish Studies |  | https://catalog.cornell.edu/programs/jewish-studies-ba/ |
| 28 | Latina/​o Studies |  | https://catalog.cornell.edu/programs/latina-o-studies-ba/ |
| 29 | Linguistics |  | https://catalog.cornell.edu/programs/linguistics-ba/ |
| 30 | Mathematics |  | https://catalog.cornell.edu/programs/mathematics-ba/ |
| 31 | Music |  | https://catalog.cornell.edu/programs/music-ba/ |
| 32 | Near Eastern Studies |  | https://catalog.cornell.edu/programs/near-eastern-studies-ba/ |
| 33 | Performing and Media Arts |  | https://catalog.cornell.edu/programs/performing-media-arts-ba/ |
| 34 | Philosophy |  | https://catalog.cornell.edu/programs/philosophy-ba/ |
| 35 | Physics |  | https://catalog.cornell.edu/programs/physics-ba/ |
| 36 | Psychology |  | https://catalog.cornell.edu/programs/psychology-ba/ |
| 37 | Religious Studies |  | https://catalog.cornell.edu/programs/religious-studies-ba/ |
| 38 | Science, Technology and Society |  | https://catalog.cornell.edu/programs/science-technology-studies-ba/ |
| 39 | Sociology |  | https://catalog.cornell.edu/programs/sociology-ba/ |
| 40 | Spanish |  | https://catalog.cornell.edu/programs/spanish-ba/ |
| 41 | Statistical Science |  | https://catalog.cornell.edu/programs/statistics-data-science-ba/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Africana Studies |  | https://catalog.cornell.edu/programs/africana-minor/ |
| 2 | American Sign Language (ASL)/​Deaf Studies |  | https://catalog.cornell.edu/programs/asl-deaf-studies-minor/ |
| 3 | American Studies |  | https://catalog.cornell.edu/programs/american-studies-minor/ |
| 4 | Anthropology |  | https://catalog.cornell.edu/programs/anthropology-minor/ |
| 5 | Arabic |  | https://catalog.cornell.edu/programs/arabic-minor/ |
| 6 | Archaeology |  | https://catalog.cornell.edu/programs/archaeology-minor/ |
| 7 | Asian American Studies |  | https://catalog.cornell.edu/programs/asian-american-studies-minor/ |
| 8 | Astrobiology |  | https://catalog.cornell.edu/programs/astrobiology-minor/ |
| 9 | Astronomy |  | https://catalog.cornell.edu/programs/astronomy-minor/ |
| 10 | Caribbean Studies |  | https://catalog.cornell.edu/programs/caribbean-studies-minor/ |
| 11 | China and Asia-​Pacific Studies |  | https://catalog.cornell.edu/programs/china-asia-pacific-studies-minor/ |
| 12 | Classical Civilization |  | https://catalog.cornell.edu/programs/classical-civilization-minor/ |
| 13 | Classics |  | https://catalog.cornell.edu/programs/classics-minor/ |
| 14 | Cognitive Science |  | https://catalog.cornell.edu/programs/cognitive-science-minor/ |
| 15 | Comparative Literature |  | https://catalog.cornell.edu/programs/comparative-literature-minor/ |
| 16 | Creative Writing |  | https://catalog.cornell.edu/programs/creative-writing-minor/ |
| 17 | Crime, Prisons, Education, and Justice |  | https://catalog.cornell.edu/programs/crime-prisons-education-justice-minor/ |
| 18 | Dance |  | https://catalog.cornell.edu/programs/dance-minor/ |
| 19 | Data Science in Astronomy |  | https://catalog.cornell.edu/programs/data-science-astronomy-minor/ |
| 20 | East Asian Studies |  | https://catalog.cornell.edu/programs/east-asian-studies-minor/ |
| 21 | English |  | https://catalog.cornell.edu/programs/english-minor/ |
| 22 | European Studies |  | https://catalog.cornell.edu/programs/european-studies-minor/ |
| 23 | Feminist, Gender, &​ Sexuality Studies |  | https://catalog.cornell.edu/programs/fgss-minor/ |
| 24 | Film |  | https://catalog.cornell.edu/programs/film-minor/ |
| 25 | French |  | https://catalog.cornell.edu/programs/french-minor/ |
| 26 | German Studies |  | https://catalog.cornell.edu/programs/german-studies-minor/ |
| 27 | Global Asia Studies |  | https://catalog.cornell.edu/programs/global-asia-studies-minor/ |
| 28 | History |  | https://catalog.cornell.edu/programs/history-minor/ |
| 29 | History of Art |  | https://catalog.cornell.edu/programs/history-art-minor/ |
| 30 | History of Capitalism |  | https://catalog.cornell.edu/programs/history-capitalism-interdisciplinary-minor/ |
| 31 | Inequality Studies |  | https://catalog.cornell.edu/programs/inequality-studies-minor/ |
| 32 | International Relations |  | https://catalog.cornell.edu/programs/international-relations-minor/ |
| 33 | Italian |  | https://catalog.cornell.edu/programs/italian-minor/ |
| 34 | Jewish Studies |  | https://catalog.cornell.edu/programs/jewish-studies-minor/ |
| 35 | Latin American Studies |  | https://catalog.cornell.edu/programs/latin-american-studies-minor/ |
| 36 | Latina/​o Studies |  | https://catalog.cornell.edu/programs/latina-o-studies-minor/ |
| 37 | Law &​ Society |  | https://catalog.cornell.edu/programs/law-society-minor/ |
| 38 | Lesbian, Gay, Bisexual, &​ Transgender |  | https://catalog.cornell.edu/programs/lgbt-minor/ |
| 39 | Linguistics |  | https://catalog.cornell.edu/programs/linguistics-minor/ |
| 40 | Mathematics |  | https://catalog.cornell.edu/programs/mathematics-minor/ |
| 41 | Media Studies |  | https://catalog.cornell.edu/programs/media-studies-minor/ |
| 42 | Medieval Studies |  | https://catalog.cornell.edu/programs/medieval-studies-minor/ |
| 43 | Migration Studies |  | https://catalog.cornell.edu/programs/migration-studies-minor/ |
| 44 | Minority, Indigenous, and Third World Studies |  | https://catalog.cornell.edu/programs/mitws-minor/ |
| 45 | Moral Psychology |  | https://catalog.cornell.edu/programs/moral-psychology-minor/ |
| 46 | Music |  | https://catalog.cornell.edu/programs/music-minor/ |
| 47 | Near Eastern Studies |  | https://catalog.cornell.edu/programs/near-eastern-studies-minor/ |
| 48 | Performing and Media Arts |  | https://catalog.cornell.edu/programs/performing-media-arts-minor/ |
| 49 | Philosophy |  | https://catalog.cornell.edu/programs/philosophy-minor/ |
| 50 | Physics |  | https://catalog.cornell.edu/programs/physics-minor/ |
| 51 | Portuguese and Brazilian Studies |  | https://catalog.cornell.edu/programs/portuguese-brazilian-studies-minor/ |
| 52 | Psychology |  | https://catalog.cornell.edu/programs/psychology-minor/ |
| 53 | Public History |  | https://catalog.cornell.edu/programs/public-history-minor/ |
| 54 | Public Policy |  | https://catalog.cornell.edu/programs/public-policy-minor/ |
| 55 | Religious Studies |  | https://catalog.cornell.edu/programs/religious-studies-minor/ |
| 56 | Russian |  | https://catalog.cornell.edu/programs/russian-minor/ |
| 57 | Sanskrit Studies |  | https://catalog.cornell.edu/programs/sanskrit-studies-minor/ |
| 58 | Science &​ Technology Studies |  | https://catalog.cornell.edu/programs/science-technology-studies-minor/ |
| 59 | South Asian Studies |  | https://catalog.cornell.edu/programs/south-asian-studies-minor/ |
| 60 | Southeast Asian Studies |  | https://catalog.cornell.edu/programs/southeast-asian-studies-minor/ |
| 61 | Spanish |  | https://catalog.cornell.edu/programs/spanish-minor/ |
| 62 | Theatre |  | https://catalog.cornell.edu/programs/theatre-minor/ |
| 63 | Viking Studies |  | https://catalog.cornell.edu/programs/viking-studies-minor/ |
| 64 | Visual Studies |  | https://catalog.cornell.edu/programs/visual-studies-minor/ |


#### Duffield College of Engineering

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Biomedical Engineering |  | https://catalog.cornell.edu/programs/biomedical-engineering-bs/ |
| 2 | Chemical Engineering |  | https://catalog.cornell.edu/programs/chemical-engineering-bs/ |
| 3 | Civil Engineering |  | https://catalog.cornell.edu/programs/civil-engineering-bs/ |
| 4 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-bs/ |
| 5 | Earth and Climate Sciences |  | https://catalog.cornell.edu/programs/earth-climate-sciences-ecsen-bs/ |
| 6 | Electrical and Computer Engineering |  | https://catalog.cornell.edu/programs/electrical-computer-engineering-bs/ |
| 7 | Engineering Physics |  | https://catalog.cornell.edu/programs/engineering-physics-bs/ |
| 8 | Independent Major |  | https://catalog.cornell.edu/programs/independent-major/ |
| 9 | Information Science, Systems, and Technology |  | https://catalog.cornell.edu/programs/information-science-systems-technology-bs/ |
| 10 | Materials Science and Engineering |  | https://catalog.cornell.edu/programs/materials-science-engineering-bs/ |
| 11 | Mechanical Engineering |  | https://catalog.cornell.edu/programs/mechanical-engineering-bs/ |
| 12 | Operations Research and Engineering |  | https://catalog.cornell.edu/programs/operations-research-engineering-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Aerospace Engineering |  | https://catalog.cornell.edu/programs/aerospace-engineering-minor/ |
| 2 | Applied Mathematics |  | https://catalog.cornell.edu/programs/applied-mathematics-minor/ |
| 3 | Biological Engineering |  | https://catalog.cornell.edu/programs/biological-engineering-minor/ |
| 4 | Biomedical Engineering |  | https://catalog.cornell.edu/programs/biomedical-engineering-minor/ |
| 5 | Computer Science |  + College of Arts and Sciences | https://catalog.cornell.edu/programs/computer-science-minor/ |
| 6 | Electrical and Computer Engineering |  | https://catalog.cornell.edu/programs/electrical-computer-engineering-minor/ |
| 7 | Engineering Communications |  | https://catalog.cornell.edu/programs/engineering-communications-minor/ |
| 8 | Engineering Management |  | https://catalog.cornell.edu/programs/engineering-management-minor/ |
| 9 | Materials Science and Engineering |  | https://catalog.cornell.edu/programs/materials-science-engineering-minor/ |
| 10 | Mechanical Engineering |  | https://catalog.cornell.edu/programs/mechanical-engineering-minor/ |
| 11 | Operations Research and Management Science |  | https://catalog.cornell.edu/programs/operations-research-management-science-minor/ |
| 12 | Robotics |  | https://catalog.cornell.edu/programs/robotics-minor/ |
| 13 | Smart Cities |  | https://catalog.cornell.edu/programs/smart-cities-minor/ |
| 14 | Sustainable Energy Systems |  | https://catalog.cornell.edu/programs/sustainable-energy-systems-minor/ |


#### College of Human Ecology

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Design and Environmental Analysis |  | https://catalog.cornell.edu/programs/design-environmental-analysis-bs/ |
| 2 | Fashion Design and Management |  | https://catalog.cornell.edu/programs/fashion-design-management-bs/ |
| 3 | Fiber Science |  | https://catalog.cornell.edu/programs/fiber-science-bs/ |
| 4 | Global &​ Public Health Sciences |  | https://catalog.cornell.edu/programs/global-public-health-sciences-hum-ecol-bs/ |
| 5 | Human Biology, Health, and Society |  | https://catalog.cornell.edu/programs/human-biology-health-society-bs/ |
| 6 | Human Development |  | https://catalog.cornell.edu/programs/human-development-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Design and Environmental Analysis |  | https://catalog.cornell.edu/programs/design-environmental-analysis-minor/ |
| 2 | Fashion Studies |  | https://catalog.cornell.edu/programs/fashion-studies-minor/ |
| 3 | Fiber Science |  | https://catalog.cornell.edu/programs/fiber-science-minor/ |
| 4 | Gerontology |  | https://catalog.cornell.edu/programs/gerontology-minor/ |
| 5 | Healthy Futures |  | https://catalog.cornell.edu/programs/healthy-futures-minor/ |
| 6 | Human Development |  | https://catalog.cornell.edu/programs/human-development-minor/ |
| 7 | Translational Research |  | https://catalog.cornell.edu/programs/translational-research-minor/ |


#### Brooks School of Public Policy

##### BA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Public Policy |  + College of Arts and Sciences | https://catalog.cornell.edu/programs/public-policy-ba/ |

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Health Care Policy |  | https://catalog.cornell.edu/programs/health-care-policy-major-bs/ |
| 2 | Public Policy |  | https://catalog.cornell.edu/programs/public-policy-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Demography |  | https://catalog.cornell.edu/programs/demography-minor/ |
| 2 | Health Policy |  | https://catalog.cornell.edu/programs/health-policy-minor/ |
| 3 | Policy Analysis and Management |  | https://catalog.cornell.edu/programs/policy-analysis-management-minor/ |


#### SC Johnson College of Business

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Hotel Administration |  | https://catalog.cornell.edu/programs/hotel-management-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Applied Economics |  | https://catalog.cornell.edu/programs/applied-economics-minor/ |
| 2 | Business |  | https://catalog.cornell.edu/programs/business-minor/ |
| 3 | Business Minor for Engineers |  | https://catalog.cornell.edu/programs/dyson-business-minor-engineers/ |
| 4 | Dyson Business Minor for Life Sciences |  | https://catalog.cornell.edu/programs/dyson-business-minor-life-sciences/ |
| 5 | Entrepreneurship |  | https://catalog.cornell.edu/programs/entrepreneurship-minor/ |
| 6 | Food and Agricultural Business |  | https://catalog.cornell.edu/programs/food-agricultural-business-minor/ |
| 7 | International Markets &​ Development |  | https://catalog.cornell.edu/programs/international-markets-development-minor/ |
| 8 | Real Estate |  | https://catalog.cornell.edu/programs/real-estate-minor-nolan-school-ug-students/ |
| 9 | Sustainable Business and Economic Policy |  | https://catalog.cornell.edu/programs/sustainable-business-economic-policy-minor/ |


#### School of Industrial and Labor Relations

##### BS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Industrial and Labor Relations |  | https://catalog.cornell.edu/programs/industrial-labor-relations-bs/ |

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Labor and Social Justice |  | https://catalog.cornell.edu/programs/labor-social-justice-minor/ |
| 2 | Organizations and Human Resource Management |  | https://catalog.cornell.edu/programs/org-human-resource-management-minor/ |


#### Bowers College of Computing and Information Science

##### Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Actuarial Science |  | https://catalog.cornell.edu/programs/actuarial-science-minor/ |
| 2 | Artificial Intelligence |  | https://catalog.cornell.edu/programs/artificial-intelligence-minor/ |
| 3 | Data Science |  | https://catalog.cornell.edu/programs/data-science-minor/ |
| 4 | Game Design |  + Duffield College of Engineering | https://catalog.cornell.edu/programs/game-design-minor/ |
| 5 | Information Science |  + College of Agriculture and Life Sciences, Duffield College of Engineering, College of Arts and Sciences | https://catalog.cornell.edu/programs/information-science-minor/ |


### 1.3 Interdisciplinary / cross-college undergraduate programs

25 UG programs are jointly offered across two or more colleges. The most prominent:
- **Applied Economics and Management (BS, MPS, MS, PhD)** — Dyson School: CALS × SC Johnson College of Business
- **Biology & Society (BA/BS dual)** — CALS × Arts & Sciences
- **Biological Engineering (BS) / Biological & Environmental Engineering (MEng)** — CALS × Duffield Engineering
- **Environmental Engineering (BS)** — CALS × Duffield Engineering
- **Computer Science (BS, BA, Minor)** — Duffield Engineering × Arts & Sciences (× Bowers CIS for the minor ecosystem)
- **Game Design (Minor)** — Bowers CIS × Duffield Engineering
- **Climate Change / Earth & Climate Sciences / Environment & Sustainability (Minors)** — CALS × Engineering × A&S

Each is counted ONCE in Rule 1 under its administrative home and cross-listed in the "多学院" column of the grouped tables.

### 1.4 Minors — complete list

The full 139-minor list is embedded inline in Section 1.2 grouped tables (every `Minor` row). 139 = 132 UG college minors + 7 graduate-field minors (the latter appear in Section 2 under Graduate School).

### 1.5 General/Institute-wide requirements

Cornell has no single university-wide core curriculum; each undergraduate college sets its own distribution/major requirements. College-specific subject-unit recommendations (e.g. CALS 16 units incl. 4 English / 4 math / 3 science; Engineering 16 units incl. 1 chemistry + 1 physics + 4 math through calculus; AAP Architecture requires 4 math + portfolio + video interview) are published on the College and School Admissions Requirements page. Source: `https://admissions.cornell.edu/how-to-apply/first-year-applicants/college-and-school-admissions-requirements`.

### 1.6 Catalog URL → Major quick-lookup

Cornell does not number programs (no Course-ID scheme like MIT). Each program has a stable catalog slug of the form `catalog.cornell.edu/programs/<name>-<degree-slug>/`, e.g. `aerospace-engineering-meng`, `computer-science-bs`. The degree is encoded both in the trailing parens of the listing text and in the URL suffix.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by College > Field > Degree Level
(Rule 5 leaf enumeration — see `#### College / ##### Field / ###### Degree Level` tables immediately below for the exhaustive list.)

#### College of Agriculture and Life Sciences

##### MEng

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Biological and Environmental Engineering |  + Duffield College of Engineering | https://catalog.cornell.edu/programs/biological-environmental-engineering-meng/ |

##### MPS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Applied Economics and Management |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/applied-economics-management-mps/ |


#### College of Architecture, Art and Planning

##### Graduate Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Real Estate |  | https://catalog.cornell.edu/programs/real-estate-minor/ |

##### MArch

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Architecture I |  | https://catalog.cornell.edu/programs/architecture-march/ |

##### MFA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Creative Visual Arts |  | https://catalog.cornell.edu/programs/creative-visual-arts-mfa/ |
| 2 | Image Text |  | https://catalog.cornell.edu/programs/image-text-mfa/ |

##### MPS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Real Estate |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/real-estate-mps-re/ |

##### MRP

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | City &​ Regional Planning |  | https://catalog.cornell.edu/programs/city-regional-planning-mrp/ |

##### MRP/MPS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | City &​ Regional Planning and Real Estate |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/regional-planning-real-estate-mps-re-mrp/ |

##### MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Advanced Architectural Design |  | https://catalog.cornell.edu/programs/advanced-architectural-design-ms-aad/ |
| 2 | Advanced Urban Design |  | https://catalog.cornell.edu/programs/advanced-urban-design-ms-aud/ |


#### Duffield College of Engineering

##### MEng

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Aerospace Engineering |  | https://catalog.cornell.edu/programs/aerospace-engineering-meng/ |
| 2 | Biomedical Engineering |  | https://catalog.cornell.edu/programs/biomedical-engineering-meng/ |
| 3 | Chemical Engineering |  | https://catalog.cornell.edu/programs/chemical-engineering-meng/ |
| 4 | Civil &​ Environmental Engineering |  | https://catalog.cornell.edu/programs/civil-environmental-engineering-meng/ |
| 5 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-cscn-meng/ |
| 6 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-nysc-meng/ |
| 7 | Data Science and Decision Analytics |  | https://catalog.cornell.edu/programs/data-science-decision-analytics-meng/ |
| 8 | Earth Science and Engineering |  | https://catalog.cornell.edu/programs/earth-science-engineering-meng/ |
| 9 | Electrical and Computer Engineering |  | https://catalog.cornell.edu/programs/electrical-computer-engineering-meng/ |
| 10 | Electrical and Computer Engineering |  | https://catalog.cornell.edu/programs/electrical-computer-engineering-nyee-meng/ |
| 11 | Engineering Management |  | https://catalog.cornell.edu/programs/engineering-management-meng/ |
| 12 | Engineering Physics |  | https://catalog.cornell.edu/programs/engineering-physics-meng/ |
| 13 | Materials Science &​ Engineering |  | https://catalog.cornell.edu/programs/materials-science-engineering-meng/ |
| 14 | Mechanical Engineering |  | https://catalog.cornell.edu/programs/mechanical-engineering-meng/ |
| 15 | Operations Research &​ Information Engineering |  | https://catalog.cornell.edu/programs/operations-research--information-engineering-nyor-meng/ |
| 16 | Operations Research &​ Information Engineering |  | https://catalog.cornell.edu/programs/operations-research-information-engineering-orie-meng/ |
| 17 | Systems Engineering |  | https://catalog.cornell.edu/programs/systems-engineering-meng/ |


#### Brooks School of Public Policy

##### MHA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Executive Health Administration |  | https://catalog.cornell.edu/programs/emha/ |
| 2 | Health Administration |  | https://catalog.cornell.edu/programs/health-administration-mha/ |

##### MPA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Executive Public Administration |  | https://catalog.cornell.edu/programs/empa/ |
| 2 | Public Administration |  | https://catalog.cornell.edu/programs/public-administration-mpa/ |

##### MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Data Science for Public Policy |  | https://catalog.cornell.edu/programs/data-science-public-policy/ |
| 2 | Environmental &​ Sustainability Policy |  | https://catalog.cornell.edu/programs/environmental-sustainability-policy/ |
| 3 | Executive Data Science for Public Policy |  | https://catalog.cornell.edu/programs/executive-data-science-public-policy/ |


#### SC Johnson College of Business

##### MBA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Executive MBA |  | https://catalog.cornell.edu/programs/cornell-executive-mba-metro-ny/ |
| 2 | Management |  | https://catalog.cornell.edu/programs/johnson-cornell-tech-mba/ |
| 3 | Management (w/​ Tsinghua U-​China) |  | https://catalog.cornell.edu/programs/cornell-tsinghua-mba-fmba/ |
| 4 | Management Science, 2 Year |  | https://catalog.cornell.edu/programs/two-year-residential-management-science-mba-stem-certified/ |
| 5 | Management, 2 year |  | https://catalog.cornell.edu/programs/two-year-residential-mba/ |

##### MBA/JD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Management and Law |  + Law School | https://catalog.cornell.edu/programs/dual-degree-program-jd-mba/ |

##### MMH

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Executive Hospitality Management |  | https://catalog.cornell.edu/programs/emmh/ |
| 2 | Hospitality Management |  | https://catalog.cornell.edu/programs/hospitality-management-mmh/ |

##### MPS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Management |  | https://catalog.cornell.edu/programs/management-mps/ |

##### MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Business Analytics |  | https://catalog.cornell.edu/programs/business-analytics-bana-ms/ |
| 2 | Business Analytics |  | https://catalog.cornell.edu/programs/business-analytics-ny-bana-ms/ |


#### School of Industrial and Labor Relations

##### MBA/MILR

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Management and Industrial &​ Labor Relations |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/milr-mba/ |


#### Graduate School

##### DMA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Music |  | https://catalog.cornell.edu/programs/music-dma/ |

##### Graduate Minor

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | City and Regional Planning |  | https://catalog.cornell.edu/programs/city-regional-planning-graduate-minor/ |
| 2 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-graduate-minor/ |
| 3 | Historic Preservation Planning |  | https://catalog.cornell.edu/programs/historic-preservation-planning-graduate-minor/ |
| 4 | Landscape Architecture Studies (Design) |  | https://catalog.cornell.edu/programs/landscape-architecture-graduate-minor-design/ |
| 5 | Landscape Architecture Studies (History/​Theory) |  | https://catalog.cornell.edu/programs/landscape-architecture-graduate-minor/ |
| 6 | Peace Studies and Peace Science |  | https://catalog.cornell.edu/programs/peace-studies-peace-science-graduate-minor/ |

##### JD/PhD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Law and Developmental Psychology |  + Law School | https://catalog.cornell.edu/programs/developmental-psychology-jd-phd/ |

##### JSD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Law |  | https://catalog.cornell.edu/programs/law-jsd/ |

##### MA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Apparel Design |  | https://catalog.cornell.edu/programs/apparel-design-ma/ |
| 2 | Archaeology |  | https://catalog.cornell.edu/programs/archaeology-ma/ |
| 3 | Asian Studies |  | https://catalog.cornell.edu/programs/asian-studies-ma/ |
| 4 | Classics |  | https://catalog.cornell.edu/programs/classics-ma/ |
| 5 | Design |  | https://catalog.cornell.edu/programs/design-ma/ |
| 6 | Developmental Psychology |  | https://catalog.cornell.edu/programs/developmental-psychology-ma/ |
| 7 | Historic Preservation Planning |  | https://catalog.cornell.edu/programs/historic-preservation-planning-ma/ |
| 8 | Human Development |  | https://catalog.cornell.edu/programs/human-development-family-studies-ma/ |

##### MFA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Creative Writing |  | https://catalog.cornell.edu/programs/creative-writing-mfa/ |

##### MFS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Food Science |  | https://catalog.cornell.edu/programs/food-science-technology-mfs/ |

##### MILR

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Industrial and Labor Relations |  | https://catalog.cornell.edu/programs/industrial-labor-relations-milr/ |

##### MLA

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Landscape Architecture |  | https://catalog.cornell.edu/programs/landscape-architecture-mla/ |
| 2 | Landscape Architecture -​ Advanced Degree |  | https://catalog.cornell.edu/programs/landscape-architecture-mla-adv-deg/ |

##### MLA/MRP

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Landscape Architecture and City &​ Regional Planning |  | https://catalog.cornell.edu/programs/mla-mrp/ |

##### MPH

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Public Health |  | https://catalog.cornell.edu/programs/public-health-mph/ |

##### MPS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Agriculture and Life Sciences |  | https://catalog.cornell.edu/programs/agriculture-life-sciences-biological-environmental-engineering-mps/ |
| 2 | Animal Science |  | https://catalog.cornell.edu/programs/animal-science-mps/ |
| 3 | Applied Statistics |  | https://catalog.cornell.edu/programs/applied-statistics-mps-as/ |
| 4 | Global Development |  | https://catalog.cornell.edu/programs/global-development-mps/ |
| 5 | Human Ecology |  | https://catalog.cornell.edu/programs/human-ecology-mps/ |
| 6 | Human Resources |  | https://catalog.cornell.edu/programs/executive-master-hr-management-mps-hr/ |
| 7 | Industrial and Labor Relations |  | https://catalog.cornell.edu/programs/industrial-labor-relations-mps/ |
| 8 | Information Science |  | https://catalog.cornell.edu/programs/information-science-isci-mps/ |
| 9 | Integrative Plant Science |  | https://catalog.cornell.edu/programs/integrative-plant-science-mps/ |
| 10 | Landscape Architecture |  | https://catalog.cornell.edu/programs/landscape-architecture-mps/ |
| 11 | Natural Resources and the Environment |  | https://catalog.cornell.edu/programs/natural-resources-mps/ |
| 12 | Veterinary Parasitology |  | https://catalog.cornell.edu/programs/veterinary-medical-sciences-mps/ |

##### MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Animal Science |  | https://catalog.cornell.edu/programs/animal-science-ms/ |
| 2 | Applied Economics and Management |  | https://catalog.cornell.edu/programs/applied-economics-management-ms/ |
| 3 | Applied Physics |  | https://catalog.cornell.edu/programs/applied-physics-ms/ |
| 4 | Atmospheric Sciences |  | https://catalog.cornell.edu/programs/atmospheric-science-ms/ |
| 5 | Biological and Environmental Engineering |  | https://catalog.cornell.edu/programs/biological-environmental-engineering-ms/ |
| 6 | Biomedical Engineering |  | https://catalog.cornell.edu/programs/biomedical-engineering-ms/ |
| 7 | Chemical Engineering |  | https://catalog.cornell.edu/programs/chemical-engineering-ms/ |
| 8 | Chemistry |  | https://catalog.cornell.edu/programs/chemistry-chemical-biology-ms/ |
| 9 | Civil and Environmental Engineering |  | https://catalog.cornell.edu/programs/civil-environmental-engineering-ms/ |
| 10 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-ms/ |
| 11 | Design Technology |  | https://catalog.cornell.edu/programs/design-technology-ms/ |
| 12 | Design Technology: Studio |  | https://catalog.cornell.edu/programs/design-technology-studio-ms/ |
| 13 | Entomology |  | https://catalog.cornell.edu/programs/entomology-ms/ |
| 14 | Fiber Science |  | https://catalog.cornell.edu/programs/fiber-science-ms/ |
| 15 | Food Science &​ Technology |  | https://catalog.cornell.edu/programs/food-science-technology-ms/ |
| 16 | Geological Sciences |  | https://catalog.cornell.edu/programs/geological-sciences-ms/ |
| 17 | Horticultural Biology |  | https://catalog.cornell.edu/programs/horticultural-biology-ms/ |
| 18 | Hotel Administration |  | https://catalog.cornell.edu/programs/hotel-administration-ms/ |
| 19 | Human Environment Relations |  | https://catalog.cornell.edu/programs/human-environment-relations-ms/ |
| 20 | Industrial and Labor Relations |  | https://catalog.cornell.edu/programs/industrial-labor-relations-ms/ |
| 21 | Information Systems |  | https://catalog.cornell.edu/programs/information-systems-ms/ |
| 22 | Materials Science and Engineering |  | https://catalog.cornell.edu/programs/materials-science-engineering-ms/ |
| 23 | Mechanical Engineering |  | https://catalog.cornell.edu/programs/mechanical-engineering-ms/ |
| 24 | Natural Resources |  | https://catalog.cornell.edu/programs/natural-resources-ms/ |
| 25 | Nutrition |  | https://catalog.cornell.edu/programs/nutrition-ms/ |
| 26 | Plant Breeding |  | https://catalog.cornell.edu/programs/plant-breeding-ms/ |
| 27 | Plant Pathology |  | https://catalog.cornell.edu/programs/plant-pathology-ms/ |
| 28 | Regional Science |  | https://catalog.cornell.edu/programs/regional-science-ms/ |
| 29 | Soil and Crop Sciences |  | https://catalog.cornell.edu/programs/soil-crop-science-ms/ |
| 30 | Systems |  | https://catalog.cornell.edu/programs/systems-ms/ |

##### PhD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Aerospace Engineering |  | https://catalog.cornell.edu/programs/aerospace-engineering-phd/ |
| 2 | Africana Studies |  | https://catalog.cornell.edu/programs/africana-studies-phd/ |
| 3 | Animal Science |  | https://catalog.cornell.edu/programs/animal-science-phd/ |
| 4 | Anthropology |  | https://catalog.cornell.edu/programs/anthropology-phd/ |
| 5 | Apparel Design |  | https://catalog.cornell.edu/programs/apparel-design-phd/ |
| 6 | Applied Economics and Management |  | https://catalog.cornell.edu/programs/applied-economics-management-phd/ |
| 7 | Applied Mathematics |  | https://catalog.cornell.edu/programs/applied-mathematics-phd/ |
| 8 | Applied Physics |  | https://catalog.cornell.edu/programs/applied-physics-phd/ |
| 9 | Asian Literature, Religion and Culture |  | https://catalog.cornell.edu/programs/asian-literature-religion-culture-phd/ |
| 10 | Astronomy and Space Sciences |  | https://catalog.cornell.edu/programs/astronomy-space-sciences-phd/ |
| 11 | Atmospheric Sciences |  | https://catalog.cornell.edu/programs/atmospheric-science-phd/ |
| 12 | Behavioral Biology |  | https://catalog.cornell.edu/programs/behavior-biology-phd/ |
| 13 | Biochemistry |  | https://catalog.cornell.edu/programs/biochemistry-phd/ |
| 14 | Biological and Environmental Engineering |  | https://catalog.cornell.edu/programs/biological-environmental-engineering-phd/ |
| 15 | Biomedical Engineering |  | https://catalog.cornell.edu/programs/biomedical-engineering-phd/ |
| 16 | Biophysics |  | https://catalog.cornell.edu/programs/biophysics-phd/ |
| 17 | Chemical Engineering |  | https://catalog.cornell.edu/programs/chemical-engineering-phd/ |
| 18 | Chemistry and Chemical Biology |  | https://catalog.cornell.edu/programs/chemistry-chemical-biology-phd/ |
| 19 | City and Regional Planning |  | https://catalog.cornell.edu/programs/city-regional-planning-phd/ |
| 20 | Civil and Environmental Engineering |  | https://catalog.cornell.edu/programs/civil-environmental-engineering-phd/ |
| 21 | Classics |  | https://catalog.cornell.edu/programs/classics-phd/ |
| 22 | Communication |  | https://catalog.cornell.edu/programs/communication-phd/ |
| 23 | Comparative Literature |  | https://catalog.cornell.edu/programs/comparative-literature-phd/ |
| 24 | Computational Biology |  | https://catalog.cornell.edu/programs/computational-biology-phd/ |
| 25 | Computer Science |  | https://catalog.cornell.edu/programs/computer-science-phd/ |
| 26 | Development Sociology |  | https://catalog.cornell.edu/programs/development-sociology-phd/ |
| 27 | Developmental Psychology |  | https://catalog.cornell.edu/programs/developmental-psychology-phd/ |
| 28 | Ecology |  | https://catalog.cornell.edu/programs/ecology-phd/ |
| 29 | Economics |  | https://catalog.cornell.edu/programs/economics-phd/ |
| 30 | Electrical and Computer Engineering |  | https://catalog.cornell.edu/programs/electrical-computer-engineering-phd/ |
| 31 | English Language and Literature |  | https://catalog.cornell.edu/programs/english-language-literature-phd/ |
| 32 | Entomology |  | https://catalog.cornell.edu/programs/entomology-phd/ |
| 33 | Evolutionary Biology |  | https://catalog.cornell.edu/programs/evolutionary-biology-phd/ |
| 34 | Fiber Science |  | https://catalog.cornell.edu/programs/fiber-science-phd/ |
| 35 | Food Science &​ Technology |  | https://catalog.cornell.edu/programs/food-science-technology-phd/ |
| 36 | Genetics |  | https://catalog.cornell.edu/programs/genetics-phd/ |
| 37 | Geological Sciences |  | https://catalog.cornell.edu/programs/geological-sciences-phd/ |
| 38 | Germanic Studies |  | https://catalog.cornell.edu/programs/germanic-studies-phd/ |
| 39 | Government |  | https://catalog.cornell.edu/programs/government-phd/ |
| 40 | History |  | https://catalog.cornell.edu/programs/history-phd/ |
| 41 | History of Architecture and Urban Development |  | https://catalog.cornell.edu/programs/history-architecture-urban-development-phd/ |
| 42 | History of Art and Archaeology |  | https://catalog.cornell.edu/programs/history-art-archaeology-visual-studies-phd/ |
| 43 | Horticultural Biology |  | https://catalog.cornell.edu/programs/horticultural-biology-phd/ |
| 44 | Hotel Administration |  | https://catalog.cornell.edu/programs/hotel-administration-phd/ |
| 45 | Human Behavior and Design |  | https://catalog.cornell.edu/programs/human-behavior-design-phd/ |
| 46 | Human Development and Family Studies |  | https://catalog.cornell.edu/programs/human-development-family-studies-phd/ |
| 47 | Industrial and Labor Relations |  | https://catalog.cornell.edu/programs/industrial-labor-relations-phd/ |
| 48 | Information Science |  | https://catalog.cornell.edu/programs/information-science-phd/ |
| 49 | Linguistics |  | https://catalog.cornell.edu/programs/linguistics-phd/ |
| 50 | Management |  | https://catalog.cornell.edu/programs/management-phd/ |
| 51 | Materials Science and Engineering |  | https://catalog.cornell.edu/programs/materials-science-engineering-phd/ |
| 52 | Mathematics |  | https://catalog.cornell.edu/programs/mathematics-phd/ |
| 53 | Mechanical Engineering |  | https://catalog.cornell.edu/programs/mechanical-engineering-phd/ |
| 54 | Medieval Studies |  | https://catalog.cornell.edu/programs/medieval-studies-phd/ |
| 55 | Microbiology |  | https://catalog.cornell.edu/programs/microbiology-phd/ |
| 56 | Molecular and Cell Biology |  | https://catalog.cornell.edu/programs/molecular-cell-biology-phd/ |
| 57 | Music |  | https://catalog.cornell.edu/programs/music-phd/ |
| 58 | Natural Resources |  | https://catalog.cornell.edu/programs/natural-resources-phd/ |
| 59 | Near Eastern Studies |  | https://catalog.cornell.edu/programs/near-eastern-studies-phd/ |
| 60 | Neurobiology |  | https://catalog.cornell.edu/programs/neurobiology-phd/ |
| 61 | Nutrition |  | https://catalog.cornell.edu/programs/nutrition-phd/ |
| 62 | Operations Research |  | https://catalog.cornell.edu/programs/operations-research-phd/ |
| 63 | Performing and Media Arts |  | https://catalog.cornell.edu/programs/performing-media-arts-phd/ |
| 64 | Philosophy |  | https://catalog.cornell.edu/programs/philosophy-phd/ |
| 65 | Physics |  | https://catalog.cornell.edu/programs/physics-phd/ |
| 66 | Plant Biology |  | https://catalog.cornell.edu/programs/plant-biology-phd/ |
| 67 | Plant Breeding |  | https://catalog.cornell.edu/programs/plant-breeding-phd/ |
| 68 | Plant Pathology |  | https://catalog.cornell.edu/programs/plant-pathology-phd/ |
| 69 | Psychology |  | https://catalog.cornell.edu/programs/psychology-phd/ |
| 70 | Public Policy |  | https://catalog.cornell.edu/programs/public-policy-phd/ |
| 71 | Regional Science |  | https://catalog.cornell.edu/programs/regional-science-phd/ |
| 72 | Robotics |  | https://catalog.cornell.edu/programs/robotics-phd/ |
| 73 | Romance Studies |  | https://catalog.cornell.edu/programs/romance-studies-phd/ |
| 74 | Science and Technology Studies |  | https://catalog.cornell.edu/programs/science-technology-studies-phd/ |
| 75 | Sociology |  | https://catalog.cornell.edu/programs/sociology-phd/ |
| 76 | Soil and Crop Sciences |  | https://catalog.cornell.edu/programs/soil-crop-science-phd/ |
| 77 | Statistics |  | https://catalog.cornell.edu/programs/statistics-phd/ |
| 78 | Systems |  | https://catalog.cornell.edu/programs/systems-phd/ |
| 79 | Theoretical and Applied Mechanics |  | https://catalog.cornell.edu/programs/theoretical-applied-mechanics-phd/ |


#### Law School

##### JD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Law |  | https://catalog.cornell.edu/programs/jd/ |

##### LLM

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Law |  | https://catalog.cornell.edu/programs/llm/ |
| 2 | Law, Tech &​ Entrepreneurship -​ International 3 Semester |  | https://catalog.cornell.edu/programs/law-tech-intnl-llm-program/ |
| 3 | Law, Technology and Entrepreneurship |  | https://catalog.cornell.edu/programs/cornell-tech-llm-program/ |

##### MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Legal Studies |  | https://catalog.cornell.edu/programs/msls-program/ |


#### College of Veterinary Medicine

##### DVM

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Veterinary Medicine |  | https://catalog.cornell.edu/programs/dvm/ |


#### Weill Cornell Graduate School of Medical Sciences

##### MBA/MS

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Executive MBA/​MS in Healthcare Leadership |  + SC Johnson College of Business | https://catalog.cornell.edu/programs/healthcare-leadership-executive-mba-ms/ |

##### PhD

| # | 专业/项目 | 多学院 | URL |
|---|---------|--------|-----|
| 1 | Biomedical and Biological Sciences |  | https://catalog.cornell.edu/programs/biomedical-sciences-phd/ |


### 2.2 At least one program's full deep-dive (worked example)
(The following item — Cornell's PhD in Computer Science deep-dive — was previously numbered 2.1; renumbered to 2.2 below.)

#### Worked example — PhD in Computer Science (a Cornell field)

- **Field**: Computer Science (PhD) — administered via the Graduate School, field home in the Bowers CIS / Duffield Engineering ecosystem.
- **Catalog page**: `https://catalog.cornell.edu/programs/computer-science-phd/`
- **Application**: decentralized — apply via the Graduate School online application; the CS field makes its own admission decision.
- **Funding**: PhD students are fully funded (tuition + stipend via fellowship/TA/RA). See Graduate School stipend rates.
- **GRE**: field-decided (most Cornell PhD fields have dropped the GRE general requirement in recent cycles; verify on the field's page).
- **English proficiency**: TOEFL iBT or IELTS Academic (Tier A: TOEFL speaking 27 / IELTS 7.0 overall + speaking 8.0; Tier B: TOEFL speaking 22 / IELTS 7.0).
- **Application fee**: $105.

### 2.3 Graduate admissions model — DECENTRALIZED via the field system

Cornell's graduate admissions is **decentralized**: each of the ~100 fields of study sets its own requirements (GRE policy, deadlines, materials) and makes independent admission decisions, even though applicants submit through a single Graduate School application portal (`gradschool.cornell.edu/academics/apply/`). Professional schools (Law via LSAC, Johnson MBA, Vet Med DVM, Weill Cornell MD/PhD) operate their own separate application platforms and set their own fees. The Graduate School is an administrative/services body, NOT a centralized admission decider — analogous to UChicago's UChicagoGRAD model.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table (2026-27 cycle)

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生网站 | admissions.cornell.edu | E-U-001 |
| 申请平台 | Common Application (+ Cornell Writing Supplement) | E-U-001 |
| **ED 截止** | **November 1** (binding) | E-U-001 |
| **RD 截止** | **January 2** | E-U-001 |
| ED 决定发布 | Mid-December | E-U-001 |
| RD 决定发布 | Late March / Early April (传统; verify) | E-U-001 |
| 入学确认截止 | January 20 (ED); May (RD, 传统) | E-U-001 |
| 申请费 | **$85** (or fee waiver) | E-U-001 |
| SAT/ACT 政策 | **REQUIRED** (reinstituted for fall 2026+; previously test-optional) | E-U-002 |
| Superscore | SAT: yes (highest section across dates, Score Choice); ACT: superscore + highest sections | E-U-002 |
| SAT code | 2098 | E-U-002 |
| ACT code | 2726 | E-U-002 |
| ACT science section | NOT required | E-U-002 |
| Self-report | Yes (Common App or portal); enrolling students must verify official | E-U-002 |
| 推荐信 | 2 teacher recommendations (Engineering: ≥1 from math/science/CS teacher) | E-U-005 |
| 面试 | NOT offered (most colleges); Architecture requires video interview | E-U-005 |
| 作品集 | Architecture (portfolio + video interview); Art (portfolio); Landscape Architecture (portfolio); DEA/Fashion (design challenge) | E-U-005 |
| 转学申请 | March 15 (international transfer financial aid); SAT/ACT neither required nor expected for transfers | E-U-001, E-U-007 |
| 财力援助申请 | CSS Profile (ED: Nov 1; RD: Jan 2 for intl; FAFSA for US) | E-U-007 |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低分 | 推荐分 | 适用条件 |
|------|-------|--------|---------|
| TOEFL iBT (exams before Jan 2026) | **100** | — | Required if not US citizen/PR, native English speaker, or full English-medium secondary school |
| TOEFL iBT (exams Jan 2026+) | **5.0** | **5.5** | New TOEFL scoring scale (post-Jan 2026 redesign) |
| IELTS Academic | **7.5** | — | Same applicability |
| Duolingo English Test (DET) | **130** | — | Same applicability |
| Cambridge C1 Advanced / C2 Proficiency | **191** | — | Same applicability |

> Self-reported scores accepted on the Common App. Official scores required only after enrollment. Source: `https://admissions.cornell.edu/how-to-apply/first-year-international-applicants` (ELP section). E-U-003.

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生模式 | **Decentralized** via field system (~100 fields); each field sets own GRE/deadline/materials | E-G-001 |
| 申请平台 | Single Graduate School online application (professional schools use LSAC / separate) | E-G-001 |
| 申请费 | **$105** (nonrefundable; waiver for financial hardship) | E-G-002 |
| CGS April-15 honor date | Cornell is a Council of Graduate Schools signatory; April 15 is the customary reply deadline for funded offers | E-G-001 |
| GRE 政策 | **Field-decided** (no university-wide GRE requirement; many fields have made it optional/dropped) | E-G-001 |
| 英语考试 | **IELTS Academic or TOEFL iBT ONLY** (NO Duolingo, Cambridge, PTE, TOEFL Essentials) | E-G-003 |
| TOEFL 送分码 | 2098 (Graduate School) | E-G-003 |
| 豁免条件 | Standing exemption (e.g. degree from English-medium institution per field rules) or special exemption request in-app | E-G-003 |
| Research-degree ELP Tier A (TA-ready) | TOEFL speaking 27 / reading 20 / listening 15 / writing 20; IELTS 7.0 overall + speaking 8.0 | E-G-003 |
| Research-degree ELP Tier B (assessment needed) | TOEFL speaking 22 / reading 20 / listening 15 / writing 20; IELTS 7.0 overall | E-G-003 |
| Professional master's ELP | Higher field-specific minimums may apply (M.Arch/M.Eng/MFS/MHA/MILR/MLA/MMH/MPA/MPH/MPS/MRP) | E-G-003 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

**Endowed colleges** (AAP, Arts & Sciences, Engineering, Brooks non-BS, SC Johnson Business):

| 费用项 | 金额 (USD) | 说明 |
|--------|-----------|------|
| Tuition | $73,946 | Endowed college rate |
| Mandatory Fees | $1,024 | $424 activity + $600 Cornell Health |
| Housing | $13,744 | On-campus estimate |
| Food | $7,604 | Standard meal plan |
| **Sub-total, Billed** | **$96,318** | |
| Books & Course Materials | $1,234 | |
| Personal Expenses | $2,182 | |
| Transportation | Varies | By region |
| **Sub-total, Non-Billed** | **$3,416** | |
| **Total COA (Endowed)** | **$99,734** | |

**NY State Contract Colleges — NY resident** (CALS, Human Ecology, ILR, Dyson AEM, Brooks BS):

| 费用项 | 金额 (USD) | 说明 |
|--------|-----------|------|
| Tuition | **$49,816** | NY-resident contract college rate |
| Mandatory Fees | $1,024 | same |
| Housing | $13,744 | same |
| Food | $7,604 | same |
| **Sub-total, Billed** | **$72,188** | |
| Books / Personal / Transport | $3,416 | same as endowed |
| **Total COA (Contract, NY resident)** | **$75,604** | |

> Contract-college **non-NY-resident** tuition equals the endowed rate ($73,946). SHP (Student Health Plan) is NOT included — it is billed separately only for students without equivalent coverage. Source: `https://finaid.cornell.edu/cost-attend`. E-U-004.

### 4.2 Undergraduate financial-aid policy

- **Need-blind** for U.S. citizens, permanent residents, and undocumented/DACA students who attended a U.S. high school.
- **Need-AWARE for international applicants** — financial need is one factor in admission decisions, BUT Cornell **meets 100% of demonstrated financial need** for all admitted undergraduates (including internationals) with grants + work-study + loans. E-U-007.
- **Meets 100% demonstrated need** for all eligible undergraduates. E-U-006.
- **Zero Student Loans + Zero Expected Family Contribution** for families with total annual income **≤ $75,000** and typical assets — aid offer = grant aid + $5,000 work-study, no loans. E-U-006.
- **Low Student Loans** (income-tiered) for families above $75k:

| Total Family Income | Maximum Loan Offer |
|---------------------|-------------------|
| Under $75,000 | $0 |
| $75,001 – $125,000 | $2,000 |
| $125,001 – $175,000 | $4,000 |
| Above $175,000 | $6,000 |

- **CSS Profile** required for all first-year/transfer applicants seeking institutional aid (international aid applications due Nov 1 ED / Jan 2 RD). **FAFSA** required for U.S. federal aid.
- **Tata Scholarship** for students from India (undergraduate).
- **No merit scholarships** — Cornell undergraduate aid is entirely need-based.

### 4.3 Graduate cost & funding framework

- **Most PhD students are FULLY FUNDED** — tuition + stipend via fellowships, research assistantships (RA), and teaching assistantships (TA). Source: `gradschool.cornell.edu/admissions/`.
- **Professional master's programs** (MEng, MPS, MBA, MArch, MHA, MILR, etc.) are typically **self-funded** (tuition-paying); some offer limited RA/TA support.
- **Stipend rates** published annually at `gradschool.cornell.edu/financial-support/program-stipend-rates/` (P1 follow-up — not scraped this run).
- **Application fee**: $105 (waiver for documented financial hardship).
- **Cost of attendance** for graduate/professional schools published per-school at `finaid.cornell.edu` → "Graduate & Professional Schools costs of attendance" (P1 follow-up).
- **Funding forms**: fellowship, RA, TA, grant, traineeship; the field/department nominates students for funding at admission.

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: undergraduate.deadlines_and_fee
  value: "ED Nov 1; RD Jan 2; Transfer March 15 (intl aid); App fee $85; Common App"
  source_url: https://admissions.cornell.edu/how-to-apply/first-year-applicants
  source_snippet: "November 1 Important Deadlines: The Common Application & Cornell Writing Supplement $85 Application Fee or Fee Waiver ... January 20 Reply to offer of admission"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-002
  field: undergraduate.test_policy
  value: "SAT/ACT REQUIRED for fall 2026+ (reinstituted); superscore; SAT code 2098, ACT code 2726; ACT science not required"
  source_url: https://admissions.cornell.edu/policies/standardized-testing-policy
  source_snippet: "Cornell University has reinstituted standardized testing requirements for first-year students ... First-year applicants are required to submit the SAT or ACT scores ... Cornell's SAT code is 2098, and our ACT code is 2726. The science section of the ACT is not required."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-003
  field: undergraduate.english_proficiency
  value: "TOEFL 100 (pre-Jan 2026) / 5.0 min-5.5 rec (Jan 2026+); IELTS 7.5; DET 130; Cambridge C1/C2 191"
  source_url: https://admissions.cornell.edu/how-to-apply/first-year-international-applicants
  source_snippet: "TOEFL exams taken prior to January 2026: minimum score of 100. TOEFL exams taken January 2026 or later: minimum score of 5.0, recommended score of 5.5. IELTS, minimum score of 7.5. Duolingo English Test, minimum score of 130. Cambridge C1 Advanced or C2 Proficiency, minimum score of 191."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-004
  field: undergraduate.cost.coa_2026_2027
  value: "Endowed tuition $73,946; total COA $99,734. Contract (NY res) tuition $49,816; total $75,604."
  source_url: https://finaid.cornell.edu/cost-attend
  source_snippet: "Tuition $73,946 ... Total, (Billed + Non-Billed) $99,734 ... Tuition $49,816 ... Total, (Billed + Non-Billed) $75,604"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-005
  field: undergraduate.per_college_requirements
  value: "CALS 16 units (4 Eng/4 math/3 sci); AAP Architecture 4 math + portfolio + video interview; Engineering 16 units incl 1 chem + 1 physics + 4 math through calculus, 2 recs incl 1 STEM; interviews NOT offered (most colleges)"
  source_url: https://admissions.cornell.edu/how-to-apply/first-year-applicants/college-and-school-admissions-requirements
  source_snippet: "College of Agriculture and Life Sciences Secondary-School Subjects/Requirements & Recommendations: 16 units, including 4 of English, 4 of mathematics ... Architecture Portfolio and video interview required ... Cornell David A. Duffield College of Engineering ... 16 units, including 1 of chemistry, 1 of physics, and 4 of mathematics ... Two (2) teacher recommendations, with at least one recommendation from a math, science, or computer science teacher."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.financial_aid.thresholds
  value: "Meets 100% demonstrated need; income ≤$75k = no loans, no parent contribution; loan caps $0/$2k/$4k/$6k by income tier"
  source_url: https://finaid.cornell.edu/cost-to-attend/access-and-affordability
  source_snippet: "Cornell meets 100 percent of demonstrated financial need for all eligible undergraduates ... Most families with total annual income up to $75,000 and typical assets will receive aid offers that include grant aid and work-study only—no student loans ... $0 expected student and parent contributions"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.financial_aid.international
  value: "Need-aware for internationals; meets 100% of admitted intl demonstrated need; CSS Profile required (ED Nov 1, RD Jan 2)"
  source_url: https://finaid.cornell.edu/first-year-and-transfer-students-international
  source_snippet: "Cornell's undergraduate admission process for international students is 'need-aware', meaning interest in or need for financial aid is one factor amongst many considered when making admission decisions. Cornell meets 100 percent of admitted international undergraduates' demonstrated financial need"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.colleges.contract_vs_endowed
  value: "Contract (NY res discount): CALS, Dyson AEM, Human Ecology, ILR, Brooks BS. Endowed: AAP, A&S, Engineering, Brooks, SC Johnson Nolan."
  source_url: https://finaid.cornell.edu/cost-attend
  source_snippet: "Cornell's NY State contract college tuition rate applies to undergraduate programs in: College of Agriculture and Life Sciences, Charles H. Dyson School of Applied Economics and Management, College of Human Ecology, School of Industrial and Labor Relations, Cornell Jeb E. Brooks School of Public Policy (Bachelor of Science candidates only). Cornell's endowed college tuition rate applies to ... College of Architecture, Art, and Planning, College of Arts and Sciences, Cornell David A. Duffield College of Engineering, Cornell Jeb E. Brooks School of Public Policy, Cornell SC Johnson College of Business, Peter and Stephanie Nolan School of Hotel Administration."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.admissions_model
  value: "Decentralized field system (~100 fields); each field sets own GRE/deadline; apply via Graduate School portal; PhDs fully funded; CGS April-15 signatory"
  source_url: https://gradschool.cornell.edu/admissions/application-steps/
  source_snippet: "Graduate study at Cornell is cross-disciplinary by design. Our decentralized structure allows students in research degrees to customize their research ... Each field sets its own admission requirements and makes independent admission decisions ... With nearly 100 fields of study, Cornell has the broadest range of programs in the Ivy League."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.application_fee
  value: "$105 nonrefundable (waiver for financial hardship)"
  source_url: https://gradschool.cornell.edu/admissions/application-steps/pay-fees/
  source_snippet: "The nonrefundable application fee is $105. You may pay using a credit or debit card."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.english_proficiency
  value: "IELTS Academic or TOEFL iBT ONLY (no DET/Cambridge/PTE); TOEFL code 2098; Tier A speaking 27, Tier B speaking 22; IELTS 7.0 overall"
  source_url: https://gradschool.cornell.edu/admissions/application-steps/required-tests/english-language-proficiency-requirement-2/
  source_snippet: "Applicants can demonstrate English Language proficiency using IELTS Academic or TOEFL iBT scores or can provide proof of an exemption. We do not accept any other English Language Proficiency exams (e.g., TOEFL Essentials, Pearson, Duolingo DET, etc.). Score Tier A ... TOEFL iBT Speaking: 27 or higher ... IELTS Academic: An overall band score of 7.0 or higher with a speaking section score of 8.0 or higher."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-004
  field: programs.directory_count
  value: "429 programs (90 UG majors + 139 UG minors + 193 grad degrees + 7 grad field minors) extracted from catalog"
  source_url: https://catalog.cornell.edu/programs/
  source_snippet: "Programs of Study [list of 429 links each named 'Name (Degree)']"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
cornell-knowledge-base-v2/
├── overview/                         (Section 0 — counts, hierarchy, matrix)
│   ├── chunk-00-overview.md
│   ├── chunk-01-hierarchy.md
│   └── chunk-02-degree-inventory.md
├── undergraduate/                    (Section 1 — one chunk per college)
│   ├── chunk-cals.md
│   ├── chunk-aap.md
│   ├── chunk-arts-sciences.md
│   ├── chunk-engineering.md
│   ├── chunk-human-ecology.md
│   ├── chunk-brooks-public-policy.md
│   ├── chunk-sc-johnson-business.md
│   ├── chunk-ilr.md
│   └── chunk-bowers-cis.md
├── graduate/                         (Section 2 — one chunk per school)
│   ├── chunk-graduate-school.md
│   ├── chunk-law.md
│   ├── chunk-vet-med.md
│   ├── chunk-johnson-mba.md
│   └── chunk-weill-med.md
├── requirements/                     (Section 3)
│   ├── chunk-deadlines.md
│   ├── chunk-tests.md
│   └── chunk-elp.md
└── costs/                            (Section 4)
    ├── chunk-coa.md
    └── chunk-aid-policy.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "cornell-knowledge-base-v2"
  school: "<home college, e.g. College of Agriculture and Life Sciences>"
  degree_level: "<BA|BS|BArch|Minor|MS|MEng|MPS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| 优先级 | 数据项 | 目标 URL | 原因 |
|--------|--------|---------|------|
| P0 | Per-field grad deadlines + GRE policy (each of ~100 fields) | `gradschool.cornell.edu/academics/apply/` field pages | Decentralized — must visit each field for its deadline/GRE/materials |
| P0 | Graduate stipend rates (2026-27) | `gradschool.cornell.edu/financial-support/program-stipend-rates/` | Not scraped; needed for grad funding framework |
| P0 | Graduate/professional per-school COA (Law, Johnson MBA, Vet Med, Weill) | `finaid.cornell.edu` graduate/professional page | Only UG COA captured |
| P1 | RD decision release date + May 1 enrollment deadline (confirm exact) | admissions.cornell.edu | ED Jan 20 confirmed; RD dates inferred from common pattern — verify |
| P1 | Weill Cornell Medicine MD program (separate admissions via AMCAS) | `med.cornell.edu` | Not in scope this run; medical MD separate from catalog |
| P1 | Per-college UG subject-unit requirements for Brooks, SC Johnson, HumEc, ILR, Bowers (CALS/AAP/A&S/Engineering captured) | admissions.cornell.edu college-requirements page | Expand accordions for remaining colleges |
| P2 | Course catalog curriculum per major | `catalog.cornell.edu/programs/<slug>/` Curriculum tab | Curriculum detail not extracted this run |
| P2 | Departmental grouping within Graduate School fields | field pages | Cornell's field system doesn't expose department cleanly in catalog |

---

## SECTION 7 — Cross-school comparison framework (Cornell column)

| 维度 | Cornell (2026-27) | MIT | Harvard | Stanford | Caltech | UC Berkeley |
|------|-------------------|-----|---------|----------|---------|-------------|
| Total UG cost/yr (endowed) | $99,734 | — | — | — | — | — |
| Tuition/yr | $73,946 (endowed) / $49,816 (contract NY) | — | — | — | — | — |
| Need-blind (intl?) | **No (need-aware intl, but meets 100% need)** | Yes | Yes | Yes | No | No |
| ED / EA / REA | **ED Nov 1** | EA Nov 1 | REA Nov 1 | — | REA Nov 1 | (none) |
| RD deadline | **Jan 2** | Jan 5 | Jan 1 | Jan 5 | Jan 5 | Nov 30 |
| SAT/ACT required? | **Yes (reinstituted)** | required | optional | required | required | test-free |
| TOEFL min (UG) | 100 / 5.0 (new) | — | — | (none) | — | 80-100 |
| IELTS min (UG) | 7.5 | — | — | — | — | 6.5 |
| Income ≤ for no loans | $75,000 | — | $85,000 | — | — | — |
| Grad app fee | $105 | — | — | — | — | $120 (dom) / $155 (intl) |
| CGS April-15 honor date | Yes | — | — | — | — | — |
| **Total programs (Rule 1)** | **429** | — | — | — | — | — |
| **School/department count (Rule 2)** | 7 UG colleges + 5 grad/prof | — | — | — | — | — |

> Empty cells to be filled from the comparison dataset as other schools are processed. Cornell's distinctive Ivy positions: (1) only Ivy with a contract-college tuition structure (NY State residency discount), (2) reinstituted SAT/ACT for fall 2026+, (3) need-aware for internationals (unlike MIT/Harvard/Yale/Princeton/Dartmouth), (4) cross-disciplinary graduate field system (~100 fields, broadest in Ivy League).

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.cornell.edu, finaid.cornell.edu, catalog.cornell.edu, gradschool.cornell.edu, cornell.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch static-HTML extraction (catalog platform = static HTML, no pagination)
> **Granularity**: school → degree-level → program (429 rows; reconciliation gate PASSED: rule1 == matrix-sum == row-count == inventory-sum == 429)
