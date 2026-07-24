# Aberystwyth University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless) + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Wales)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 311 |
| 本科辅修 (Minors) | N/A (UK universities do not typically offer standalone minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/LLM/MRes) | 67 |
| 研究生博士项目 (PhD/MPhil/DProf) | 65 |
| **学位项目总计 (UG extracted)** | **311** |
| 学术科目领域 (Subject areas) | 32 |
| 学术院系 (Academic Departments) | 22 |
| 学院 (Faculties) | 2 |

> **Data source**: Aberystwyth University course search portal (`courses.aber.ac.uk/atoz/`), 311 UG courses and 132 PG courses extracted.
> **Faculties**: Faculty of Humanities (11 departments) and Faculty of Sciences (8 departments).

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Aberystwyth University (Prifysgol Aberystwyth)
├── Faculty of Humanities                               [学院]
│   ├── School of Art                                   [系]
│   ├── Aberystwyth Business School                     [系]
│   ├── School of Education                             [系]
│   ├── Dept of English & Creative Writing              [系]
│   ├── Dept of History & Welsh History                 [系]
│   ├── Dept of Information Studies                     [系]
│   ├── Dept of International Politics                  [系]
│   ├── Dept of Law & Criminology                       [系]
│   ├── Dept of Modern Languages                        [系]
│   ├── Dept of Theatre, Film & Television Studies      [系]
│   └── Dept of Welsh & Celtic Studies                  [系]
└── Faculty of Sciences                                 [学院]
    ├── Dept of Computer Science                        [系]
    ├── Dept of Geography & Earth Sciences              [系]
    ├── Healthcare Education Centre                     [系]
    ├── Dept of Life Sciences / IBERS                   [系]
    ├── Dept of Mathematics                             [系]
    ├── Dept of Physics                                 [系]
    ├── Dept of Psychology                              [系]
    └── Aberystwyth School of Veterinary Science        [系]
```

> **Source**: `aber.ac.uk/en/about-us/departments-faculties/`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 层级 | 本项目数量 |
|---------|-----------|------|-----------|
| BSc | BSc | 本科 | 173 |
| BA | BA | 本科 | 91 |
| LLB | LLB | 本科 | 11 |
| MBiol | MBiol | 本科 (Integrated Master's) | 10 |
| BEng | BEng | 本科 | 8 |
| MPhys | MPhys | 本科 (Integrated Master's) | 4 |
| MEng | MEng | 本科 (Integrated Master's) | 4 |
| MAg | MAg | 本科 (Integrated Master's) | 2 |
| FDSc | FDSc | 本科 (Foundation Degree) | 2 |
| MComp | MComp | 本科 (Integrated Master's) | 2 |
| MMath | MMath | 本科 (Integrated Master's) | 2 |
| CertHE | CertHE | 本科 | 1 |
| NQUG | NQUG | 本科 (Professional) | 1 |
| **合计** | | | **311** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学科领域 \ 学位 | BSc | BA | LLB | MBiol | BEng | MPhys | MEng | MAg | FDSc | MComp | MMath | CertHE | NQUG | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Accounting & Finance | 10 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **11** |
| Agriculture | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | **14** |
| Animal & Aquatic Sciences | 24 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **28** |
| Art | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **7** |
| Biochemistry & Genetics | 9 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Biosciences | 7 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **12** |
| Business & Management | 15 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **17** |
| Computer Science | 19 | 0 | 0 | 0 | 3 | 0 | 3 | 0 | 0 | 2 | 0 | 0 | 0 | **27** |
| Criminology | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **7** |
| Drama & Theatre | 0 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **11** |
| Ecological Sciences | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| Economics | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| Education & Childhood Studies | 3 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | **12** |
| Engineering | 0 | 0 | 0 | 0 | 5 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| English & Creative Writing | 0 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Film, Television & Media | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| Geography, Earth & Environmental Sciences | 17 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **21** |
| History | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **14** |
| Human Biology & Health | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| Information Studies | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| Law | 0 | 1 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| Marketing | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **6** |
| Mathematics | 10 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | **13** |
| Modern Languages | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| Nursing | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | **5** |
| Physics | 6 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **10** |
| Politics & International Relations | 1 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **12** |
| Psychology | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **9** |
| Sociology | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Sport & Exercise Science | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| Veterinary Studies | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Welsh & Celtic Studies | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **9** |
| **合计** | 173 | 91 | 11 | 10 | 8 | 4 | 4 | 2 | 2 | 2 | 2 | 1 | 1 | **311** |

> **Reconciliation check**: Rule-1 total (311) == matrix-sum (311) == Rule-5 rows (311). ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 Subject area architecture

Aberystwyth University organises its undergraduate programmes across 32 subject areas, administered by 22 academic departments within 2 faculties. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate degree programmes — grouped by Subject Area > Degree Level


#### Accounting & Finance
*Department: Aberystwyth Business School*


##### BSc (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/accounting-and-finance-degree |
| 2 | Accounting and Finance (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/accounting-and-finance-foundation |
| 3 | Accounting and Finance / Business and Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/accounting-management |
| 4 | Accounting and Finance / Economics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/accounting-economics |
| 5 | Accounting and Finance and Computing (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/accounting-computing |
| 6 | Accounting and International Finance (Top-up) (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/accounting-international-finance |
| 7 | Business Finance (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-finance-degree |
| 8 | Business Finance (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-finance-foundation |
| 9 | International Business Finance (Top-Up) (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/international-business-finance |
| 10 | Mathematics / Accounting and Finance (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-accounting |

##### LLB (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law and Accounting & Finance (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/llb-law-accounting-finance |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Agriculture
*Department: Institute of Biological, Environmental & Rural Sciences (IBERS)*


##### BSc (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/agriculture-top-up |
| 2 | Agriculture (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/bsc-agriculture-degree |
| 3 | Agriculture (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/agriculture-degree |
| 4 | Agriculture (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/agriculture-study-abroad |
| 5 | Agriculture with Animal Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/agriculture-animal-science |
| 6 | Agriculture with Animal Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/agriculture-with-animal-science-degree |
| 7 | Agriculture with Business Management (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/agriculture-business |
| 8 | Plant Biology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/plant-biology-degree |
| 9 | Plant Biology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/plant-biology-integrated-foundation |
| 10 | Plant Biology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/plant-biology-industry |
| 11 | Plant Biology (with integrated year in industry) (BSc, 5 years) | https://courses.aber.ac.uk/undergraduate/plant-biology-industry-foundation |

##### MAg (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture (MAg, 4 years) | https://courses.aber.ac.uk/undergraduate/mag=agriculture |
| 2 | Agriculture with Animal Science (MAg, 4 years) | https://courses.aber.ac.uk/undergraduate/agrictulture-animalscience |

##### FDSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture (with integrated year in industry) (FDSc, 3 years) | https://courses.aber.ac.uk/undergraduate/agriculture-foundation-degree-work-experience |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Animal & Aquatic Sciences
*Department: Department of Life Sciences*


##### BSc (24 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Behaviour (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/animal-behaviour-degree |
| 2 | Animal Behaviour (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/animal-behaviour-foundation |
| 3 | Animal Behaviour (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/animal-behaviour-industry |
| 4 | Animal Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/animal-science-degree |
| 5 | Animal Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/animal-science-integrated-foundation |
| 6 | Animal Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/animal-science-industry |
| 7 | Equine and Veterinary Bioscience (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/equine-science-and-veterinary-bioscience |
| 8 | Equine and Veterinary Bioscience (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/equine-veterinary-bioscience-integrated-foundation-Cym |
| 9 | Equine and Veterinary Bioscience (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/equine-veterinary-biosciences-industry |
| 10 | Equine and Veterinary Bioscience (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/equine-veterinary-bioscience-study-abroad |
| 11 | Equine and Veterinary Bioscience (with integrated year studying abroad) (BSc, 5 years) | https://courses.aber.ac.uk/undergraduate/D3YF-equine-veterinary-bioscience |
| 12 | Marine and Freshwater Biology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/marine-freshwater-biology-foundation |
| 13 | Marine and Freshwater Biology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/marine-freshwater-biology-industry |
| 14 | Veterinary Biosciences (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/veterinary-biosciences |
| 15 | Veterinary Biosciences (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/veterinary-biosciences-integrated-foundation |
| 16 | Veterinary Biosciences (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/veterinary-biosciences-industry |
| 17 | Wildlife Conservation (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/wildlife-conservation |
| 18 | Wildlife Conservation (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/wildlife-conservation-integrated-foundation |
| 19 | Wildlife Conservation (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/wildlife-conservation-industry |
| 20 | Zoology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/zoology-degree |
| 21 | Zoology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/zoology-foundation |
| 22 | Zoology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/zoology-industry |
| 23 | Zoology (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/zoology-study-abroad |
| 24 | Zoology (with integrated year studying abroad) (BSc, 5 years) | https://courses.aber.ac.uk/undergraduate/C3Y1-zoology |

##### MBiol (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Marine and Freshwater Biology (MBiol, 4 years) | https://courses.aber.ac.uk/undergraduate/mbiol-marine-freshwater-biology |
| 2 | Marine and Freshwater Biology (MBiol, 5 years) | https://courses.aber.ac.uk/undergraduate/mbiol-marine-freshwater-biology-foundation |
| 3 | Zoology (MBiol, 4 years) | https://courses.aber.ac.uk/undergraduate/mbiol-zoology |
| 4 | Zoology (MBiol, 5 years) | https://courses.aber.ac.uk/undergraduate/mbiol-zoology-integrated-foundation |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Art
*Department: School of Art*


##### BA (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Art History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/V350-art-history |
| 2 | Creative Writing and Fine Art (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/WW18-creative-writing-and-fine-art |
| 3 | Film and Television / Fine Art (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/WW16-film-and-television-fine-art |
| 4 | Fine Art (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/W100-fine-art |
| 5 | Fine Art / Art History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/WV13-fine-art-art-history |
| 6 | Fine Art / English Literature (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/WQ13-fine-art-english-literature |
| 7 | Fine Art with Art History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/W1V3-fine-art-art-history |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Biochemistry & Genetics
*Department: Department of Life Sciences*


##### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/biochemistry-degree |
| 2 | Biochemistry (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biochemistry-integrated-foundation |
| 3 | Biochemistry (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biochemistry-industry |
| 4 | Biomedical Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/Biomedical-Science |
| 5 | Biomedical Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biomedical-science-foundation |
| 6 | Biomedical Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biomedical-sciences-integrated-industry |
| 7 | Genetics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/genetics-degree |
| 8 | Genetics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/genetics-degree-integrated-foundation |
| 9 | Genetics (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/genetics-integrated-year-in-industry |

##### MBiol (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry (MBiol, 5 years) | https://courses.aber.ac.uk/undergraduate/mbiolbiochem-integrated-foundation |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Biosciences
*Department: Department of Life Sciences*


##### BSc (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/biology-degree |
| 2 | Biology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biology-foundation-year |
| 3 | Biology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/biology-degree-industry |
| 4 | Marine and Freshwater Biology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/marine-and-freshwater-biology |
| 5 | Microbiology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/microbiology-degree |
| 6 | Microbiology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/microbiology-degree-integrated-foundation |
| 7 | Microbiology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/microbiology-industry |

##### MBiol (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry (MBiol, 4 years) | https://courses.aber.ac.uk/undergraduate/mbiolbiology-degree |
| 2 | Biology (MBiol, 4 years) | https://courses.aber.ac.uk/undergraduate/mbiol-biology |
| 3 | Biology (MBiol, 5 years) | https://courses.aber.ac.uk/undergraduate/mbiol-biology-integrated-foundation |
| 4 | Microbiology (MBiol, 4 years) | https://courses.aber.ac.uk/undergraduate/mbiolmicrobiology-degree |
| 5 | Microbiology (MBiol, 5 years) | https://courses.aber.ac.uk/undergraduate/mbiolmicrobiology-degree-intergrated-foundation |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Business & Management
*Department: Aberystwyth Business School*


##### BSc (15 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Agriculture with Business Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/agri-business |
| 2 | Business Economics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-economics-degree |
| 3 | Business Economics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-economics-foundation |
| 4 | Business Information Technology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-information-technology-degree |
| 5 | Business Information Technology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-information-technology-with-foundation-year |
| 6 | Business Information Technology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-information-technology |
| 7 | Business and Climate Change (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-and-climate-change |
| 8 | Business and Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-management-degree |
| 9 | Business and Management (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-and-management-foundation |
| 10 | Business and Management (Top-up) (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/N12T-business-topup |
| 11 | Business and Management / Modern Languages (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/business-modern-languages |
| 12 | Business and Management and Computing (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/business-computing |
| 13 | Economics / Business and Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/economics-business |
| 14 | Marketing / Business and Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/marketing-businessmanagement |
| 15 | Mathematics / Business and Management (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-businessmanagement |

##### LLB (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Law (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/M140-business-law |
| 2 | Law and Business & Management (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/law-business |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Computer Science
*Department: Department of Computer Science*


##### BSc (19 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Robotics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/artificial-intelligence-roboticsdegree |
| 2 | Artificial Intelligence and Robotics (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/artificial-intelligence-robotics-degree-work-exp |
| 3 | Computer Graphics, Vision and Games (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/computer-graphics-vision-games-degree |
| 4 | Computer Graphics, Vision and Games (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/computer-graphics-vision-games-degree-work-exp |
| 5 | Computer Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/computer-science-degree |
| 6 | Computer Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/computer-science-degree-foundation-year |
| 7 | Computer Science (Top-up) (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/comp-sci-top-up |
| 8 | Computer Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/computer-science-degree-with-industrial-year |
| 9 | Computer Science (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/computer-science-year-study-abroad |
| 10 | Computer Science / Mathematics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/computer-science-and-mathematics-degree |
| 11 | Computer Science / Physical Geography (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/computer-science-and-physical-geography-degree |
| 12 | Computer Science and Artificial Intelligence (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/computer-science-and-artificial-intelligence-deg |
| 13 | Computer Science and Artificial Intelligence (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/computer-science-and-artificial-intelligence |
| 14 | Data Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/data-science |
| 15 | Data Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/data-science-iy |
| 16 | Space Science and Robotics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/space-science-robotics-degree |
| 17 | Web Development and Security (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/web-development-and-security |
| 18 | Web Development and Security (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/web-development-security-foundation |
| 19 | Web Development and Security (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/web-development-and-security-integrated-industry |

##### BEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics and Embedded Systems Engineering (BEng, 3 years) | https://courses.aber.ac.uk/undergraduate/robotics-systems-engineering-computer-science |
| 2 | Robotics and Embedded Systems Engineering (with integrated year in industry) (BEng, 4 years) | https://courses.aber.ac.uk/undergraduate/systems-engineering-industry-computer-science |
| 3 | Software Engineering (with integrated year in industry) (BEng, 4 years) | https://courses.aber.ac.uk/undergraduate/software-engineering |

##### MEng (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics and Embedded Systems Engineering (MEng, 4 years) | https://courses.aber.ac.uk/undergraduate/masters-robotics-systems-computer-science |
| 2 | Robotics and Embedded Systems Engineering (with integrated year in industry) (MEng, 5 years) | https://courses.aber.ac.uk/undergraduate/systems-robotics-engineering-computer-science |
| 3 | Software Engineering (with integrated year in industry) (MEng, 5 years) | https://courses.aber.ac.uk/undergraduate/meng-software-engineering-degree |

##### MComp (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science (MComp, 4 years) | https://courses.aber.ac.uk/undergraduate/mcomp-computerscience |
| 2 | Computer Science (with integrated year in industry) (MComp, 5 years) | https://courses.aber.ac.uk/undergraduate/computer-science-industry |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Criminology
*Department: Department of Law & Criminology*


##### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/M900-criminology |
| 2 | Criminology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/M90F-criminology-foundation |
| 3 | Criminology and Criminal Psychology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/M9C6-criminology-and-criminal-psychology |
| 4 | Criminology and Sociology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/ML93-criminology-and-sociology |
| 5 | Psychology and Criminology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/psychology-and-criminology |
| 6 | Psychology and Criminology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/psychology-criminology-year-in-industry |

##### LLB (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law and Criminology (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/MM91-law-and-criminology |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Drama & Theatre
*Department: Department of Theatre, Film & Television Studies*


##### BA (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing and Drama and Theatre (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/creative-writing-drama-theatre-studies-degree |
| 2 | Drama and English (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/WQ44-drama-and-english |
| 3 | Drama and Theatre (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/W400-drama-and-theatre |
| 4 | Drama and Theatre (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/W40F-drama-and-theatre-foundation |
| 5 | Drama and Theatre (with integrated year in professional practice) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/W402-drama-and-theatre-professional-practice |
| 6 | Drama and Theatre / History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/drama-and-theatre-studies-and-history-degree |
| 7 | Drama and Theatre / International Relations (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/drama-relations |
| 8 | Education / Drama and Theatre (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/W4X3-educationdramaandtheatre |
| 9 | Film and Television / Drama and Theatre (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/film-drama |
| 10 | Mathematics / Drama and Theatre (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-and-drama-and-theatre-studies-degree |
| 11 | Modern Languages / Drama and Theatre (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/modern-languages-drama-theatre |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Ecological Sciences
*Department: Department of Life Sciences*


##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/ecology-degree |
| 2 | Ecology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/ecology-degree-integrated-foundation |
| 3 | Ecology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/ecology-industry |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Economics
*Department: Aberystwyth Business School*


##### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/economics-degree |
| 2 | Economics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/economics-foundation |
| 3 | Economics and Climate Change (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/economics-and-climate-change |
| 4 | Economics and International Relations (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/relations-economics |
| 5 | Economics and Politics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/economics-politics |
| 6 | Mathematics / Economics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-economics |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Education & Childhood Studies
*Department: School of Education*


##### BA (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Childhood Studies (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/childhood-studies-degree |
| 2 | Early Childhood Studies with Early Years Practitioner Status (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/early-childhood-studies |
| 3 | Education (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/BA-education |
| 4 | Education (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/BA-education-foundation |
| 5 | Education / History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/BA-education-and-history |
| 6 | Education with Spanish (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/BA-education-spanish |
| 7 | English Literature / Education (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/english-literature-and-education |
| 8 | Welsh / Education (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/welsh-education |

##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics / Education (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-and-education |
| 2 | Mathematics with Education (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-with-education |
| 3 | Psychology and Education (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/psychology-education-degree |

##### CertHE (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Healthcare Education (CertHE, 2 years) | https://courses.aber.ac.uk/undergraduate/healthcare-education |

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Engineering
*Department: Department of Computer Science*


##### BEng (5 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering (BEng, 3 years) | https://courses.aber.ac.uk/undergraduate/electrical-engineering |
| 2 | Electrical and Electronic Engineering (BEng, 4 years) | https://courses.aber.ac.uk/undergraduate/electrical-engineering-foundation |
| 3 | Electrical and Electronic Engineering (with integrated year in industry) (BEng, 4 years) | https://courses.aber.ac.uk/undergraduate/electrical-engineering-industry |
| 4 | Engineering Physics (BEng, 3 years) | https://courses.aber.ac.uk/undergraduate/engineering-physics-aber |
| 5 | Engineering Physics (with integrated year in industry) (BEng, 4 years) | https://courses.aber.ac.uk/undergraduate/engineering-physics-industry |

##### MEng (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Physics (with integrated year in industry) (MEng, 5 years) | https://courses.aber.ac.uk/undergraduate/engineering-physics |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### English & Creative Writing
*Department: Department of English & Creative Writing*


##### BA (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/creative-writing-degree |
| 2 | Creative Writing and Film and Television (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/creative-writing-film-television-degree |
| 3 | Creative Writing and Modern Languages (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/creative-writing-modern-language |
| 4 | English Literature (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/english-literature-degree |
| 5 | English Literature and Creative Writing (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/english-creative-writing-degree |
| 6 | English Literature and Creative Writing (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/english-creative-writing-foundation |
| 7 | English Studies and Climate Change (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/english-climatechange |
| 8 | Film and Television / English Literature (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/film-television-and-english-literature |
| 9 | History / English Literature (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/history-and-english-literature-degree |
| 10 | Modern Languages / English Literature (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/modern-languages-english-literature |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Film, Television & Media
*Department: Department of Theatre, Film & Television Studies*


##### BA (8 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Television (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/W620-film-and-television |
| 2 | Film and Television (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/W62F-film-and-television-foundation |
| 3 | Film and Television / Mathematics (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/film-and-television-and-mathematics-degree |
| 4 | Filmmaking (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/P301-film-making |
| 5 | Media and Communication Studies (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/P300-media-and-communication-studies |
| 6 | Media and Creative Writing (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/media-creative |
| 7 | Media and English Literature (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/media-englishliterature |
| 8 | Writing for Broadcasting, Media and Performance (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/P302-writing-for-broadcasting-mediaperformance |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Geography, Earth & Environmental Sciences
*Department: Department of Geography & Earth Sciences*


##### BSc (17 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Earth Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/environmental-earth-science-degree |
| 2 | Environmental Earth Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-earth-science-foundation |
| 3 | Environmental Earth Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-earth-science-industry |
| 4 | Environmental Earth Science (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-earth-science-studyabroad |
| 5 | Environmental Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/environmental-science-degree |
| 6 | Environmental Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-science-foundation |
| 7 | Environmental Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-science-industry |
| 8 | Environmental Science (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/environmental-science-studyabroad |
| 9 | Geography (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/geography-degree |
| 10 | Geography (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/geography-foundation |
| 11 | Geography (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/geography-with-year-in-industry |
| 12 | Geography (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/geography-with-year-abroad |
| 13 | Physical Geography (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/physical-geography |
| 14 | Physical Geography (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/physical-geography-foundation |
| 15 | Physical Geography (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/physical-geography-year-in-industry |
| 16 | Physical Geography (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/physical-geography-year-abroad |
| 17 | Physical Geography / Mathematics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/physical-geography-and-mathematics-degree |

##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Geography (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/human-geography-degree |
| 2 | Human Geography (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/human-geography-foundation |
| 3 | Human Geography (with integrated year in industry) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/human-geography-year-in-industry |
| 4 | Human Geography (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/human-geography-year-abroad |

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### History
*Department: Department of History & Welsh History*


##### BA (14 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing and History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/creativewriting-history |
| 2 | History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/history-degree |
| 3 | History (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/history-foundation |
| 4 | History (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/history-study-abroad |
| 5 | History / Mathematics (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/history-and-mathematics-degree |
| 6 | History / Welsh History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/hanes-a-hanes-cymru |
| 7 | History and Welsh History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/history-and-welsh-history-degree |
| 8 | International Relations / History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/relations-history |
| 9 | International Relations and Military History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/H2VL-international-relations-and-military-history |
| 10 | International Relations and Military History (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/H2VY-international-relations-military-history-study-abroad |
| 11 | Medieval and Early Modern History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/medieval-early-modern-history-degree |
| 12 | Modern Languages / History (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/modern-languages-history |
| 13 | Modern and Contemporary History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/modern-and-contemporary-history-degree |
| 14 | Politics and Modern History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/V135-politics-and-modern-history |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Human Biology & Health
*Department: Healthcare Education Centre*


##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Health Science (Nutrition and Exercise) (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/health-science |
| 2 | Health Science (Nutrition and Exercise) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/health-science-foundation |
| 3 | Health Science (Nutrition and Exercise) (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/health-science-industrial-year |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Information Studies
*Department: Department of Information Studies*


##### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Cultural Heritage Studies: Libraries, Archives and Museums (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/cultural-heritage-studies |

##### BSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Information and Library Studies (BSc, 5 years) | https://courses.aber.ac.uk/undergraduate/information-library-studies-distance-learning |

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Law
*Department: Department of Law & Criminology*


##### LLB (7 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Law (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/M131-criminal-law |
| 2 | Human Rights (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/M990-human-rights |
| 3 | Law (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/M100-law |
| 4 | Law (LLB, 4 years) | https://courses.aber.ac.uk/undergraduate/M10F-law-foundation |
| 5 | Law and International Relations (LLB, 3 years) | https://courses.aber.ac.uk/undergraduate/law-relations |
| 6 | Law and Modern Languages (LLB, 4 years) | https://courses.aber.ac.uk/undergraduate/law-modern-languages |
| 7 | Senior Status Law (LLB, 2 years) | https://courses.aber.ac.uk/undergraduate/M104-senior-status-law |

##### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Law (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/M103-law |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Marketing
*Department: Aberystwyth Business School*


##### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Marketing (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/digital-marketing |
| 2 | International Marketing (Top-up) (BSc, 1 year) | https://courses.aber.ac.uk/undergraduate/international-marketing-topup |
| 3 | Marketing (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/marketing-degree |
| 4 | Marketing (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/marketing-foundation |
| 5 | Marketing / Modern Languages (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/marketing-modern-languages |
| 6 | Psychology and Marketing (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/marketing-psychology |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Mathematics
*Department: Department of Mathematics*


##### BSc (10 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics / Pure Mathematics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/applied-mathematics-and-pure-mathematics-degree |
| 2 | Financial Mathematics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/financial-mathematics-degree |
| 3 | Financial Mathematics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/financial-mathematics-integrated-foundation-year |
| 4 | Mathematical Modelling (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematical-modelling |
| 5 | Mathematical and Theoretical Physics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematical-theoretical-physics-degree |
| 6 | Mathematics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-degree |
| 7 | Mathematics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/mathematics-degree-with-foundation-year |
| 8 | Mathematics (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/mathematics-integrated-year-industry |
| 9 | Mathematics / Physics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mathematics-and-physics-degree |
| 10 | Pure Mathematics / Statistics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/pure-mathematics-and-statistics-degree |

##### MMath (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematical and Theoretical Physics (MMath, 4 years) | https://courses.aber.ac.uk/undergraduate/mmath-mathematical-theoretical-physics-degree |
| 2 | Mathematics (MMath, 4 years) | https://courses.aber.ac.uk/undergraduate/mmath-mathematics-degree |

##### BA (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Modern Languages / Mathematics (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/modern-languages-mathematics |

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Modern Languages
*Department: Department of Modern Languages*


##### BA (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Modern Languages (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/R991-modern-languages |
| 2 | Modern Languages / International Relations (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/modern-languages-international-relations |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Nursing
*Department: Healthcare Education Centre*


##### BSc (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/nursing-adult |
| 2 | Nursing (Adult) (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/adult-part |
| 3 | Nursing (Mental Health) (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mental-health |
| 4 | Nursing (Mental Health) (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/mentalhealth-parttime |

##### FDSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Nursing (FDSc, 3 years) | https://courses.aber.ac.uk/undergraduate/veterinary-nursing |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Physics
*Department: Department of Physics*


##### BSc (6 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/astrophysics-degree |
| 2 | Astrophysics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/astrophysics-with-foundation-year |
| 3 | Physics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/bsc-physics-degree |
| 4 | Physics (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/physics-degree-with-foundation-year |
| 5 | Physics (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/physics-with-year-in-industry |
| 6 | Physics with Planetary and Space Physics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/physics-with-planetary-space-physics-degree |

##### MPhys (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics (MPhys, 4 years) | https://courses.aber.ac.uk/undergraduate/astrophysics-masters-degree |
| 2 | Physics (MPhys, 4 years) | https://courses.aber.ac.uk/undergraduate/mphys-physics-degree |
| 3 | Physics (with integrated year in industry) (MPhys, 5 years) | https://courses.aber.ac.uk/undergraduate/mphys-physics-with-year-in-industry |
| 4 | Physics with Planetary and Space Physics (MPhys, 4 years) | https://courses.aber.ac.uk/undergraduate/mphys-physics-planetary-space-physics-degree |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Politics & International Relations
*Department: Department of International Politics*


##### BA (11 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Intelligence and International Security (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/intelligence-security |
| 2 | Intelligence and International Security (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/intelligence-security-study-abroad |
| 3 | International Relations (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/142L-international-relations |
| 4 | International Relations (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/F42L-international-relations-foundation |
| 5 | International Relations (with integrated year in Industry) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/642L-international-relations-industry |
| 6 | International Relations (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/242L-international-relations-abroad |
| 7 | International Relations and Military History (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/F2VL-international-relations-and-military-hist-F |
| 8 | Politics (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/L203-politics |
| 9 | Politics (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/politics-study-abroad |
| 10 | Politics and International Relations (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/L248-politics-and-international-relations |
| 11 | Politics and International Relations (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/politics-international-relations-study-abroad |

##### BSc (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology and Politics (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/LL32-sociology-and-politics |

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Psychology
*Department: Department of Psychology*


##### BSc (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/psychology |
| 2 | Psychology (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/psychology-foundation |
| 3 | Psychology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/psychology-year-in-industry |
| 4 | Psychology (with integrated year studying abroad) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/psychology-year-abroad |
| 5 | Psychology and Sociology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/psychology-sociology |
| 6 | Psychology with Counselling (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/psychology-counselling |
| 7 | Psychology with Counselling (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/C844-psychology-counselling-industry |
| 8 | Psychology with Forensic Psychology (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/forensic-psychology |
| 9 | Psychology with Forensic Psychology (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/psychology-forensic-industry |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Sociology
*Department: Department of International Politics*


##### BA (4 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/ba-sociology |
| 2 | Sociology (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/ba-sociology-foundation |
| 3 | Sociology (with integrated year in Industry) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/sociology-industry |
| 4 | Sociology (with integrated year studying abroad) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/sociology-abroad |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Sport & Exercise Science
*Department: Department of Life Sciences*


##### BSc (3 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Exercise Science (BSc, 3 years) | https://courses.aber.ac.uk/undergraduate/sport-exercise-science-degree |
| 2 | Sport and Exercise Science (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/sport-and-exercise-science-foundation |
| 3 | Sport and Exercise Science (with integrated year in industry) (BSc, 4 years) | https://courses.aber.ac.uk/undergraduate/sports-science-industry |

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Veterinary Studies
*Department: Aberystwyth School of Veterinary Science*


##### NQUG (1 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Veterinary Science (BVSc) (NQUG, 5 years) | https://courses.aber.ac.uk/undergraduate/vet-sci |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BA (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

#### Welsh & Celtic Studies
*Department: Department of Welsh & Celtic Studies*


##### BA (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Celtic Studies (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/celtic-studies-degree |
| 2 | Professional Welsh (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/gradd-cymraeg-proffesiynol |
| 3 | Welsh (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/gradd-cymraeg |
| 4 | Welsh (for Beginners) (BA, 4 years) | https://courses.aber.ac.uk/undergraduate/welsh-beginners-degree |
| 5 | Welsh / Geography (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/cymraeg-a-daearyddiaeth |
| 6 | Welsh / History (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/cymraeg-hanes |
| 7 | Welsh / International Relations (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/cymraeg-cysylltiadau |
| 8 | Welsh / Mathematics (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/cymraeg-a-mathemateg |
| 9 | Welsh and the Celtic Languages (BA, 3 years) | https://courses.aber.ac.uk/undergraduate/gradd-cymraeg-ar-ieithoedd-celtaidd |

##### BSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### LLB (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MBiol (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### BEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MPhys (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MEng (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MAg (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### FDSc (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MComp (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### MMath (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### CertHE (0 programmes)

| # | 专业 | URL |
|---|------|-----|

##### NQUG (0 programmes)

| # | 专业 | URL |
|---|------|-----|

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate taught (PGT)

Aberystwyth offers **67 postgraduate taught programmes** across the following subject areas:


#### Accounting & Finance
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Finance (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/finance-msc |
| 2 | International Finance and Banking (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/international-banking |
| 3 | Management and Finance (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/management-finance-msc |

#### Agriculture
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Agriculture (DAg, 5 years) | DAg | https://courses.aber.ac.uk/postgraduate/professional-doctorate-agriculture |
| 2 | Agriculture (MRes, 5 years) | MRes | https://courses.aber.ac.uk/postgraduate/agriculture-research-masters |
| 3 | Agrifood Innovation (MRes, 3 years) | MRes | https://courses.aber.ac.uk/postgraduate/J792D3-sustainable-agriculture |
| 4 | Agrifood Innovation (MRes, 5 years) | MRes | https://courses.aber.ac.uk/postgraduate/J792D-agrifood-innovation |
| 5 | Agrifood Innovation (MSc, 5 years) | MSc | https://courses.aber.ac.uk/postgraduate/agrifood-innovation |
| 6 | Livestock Science (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/livestock-science-masters |
| 7 | Livestock Science (UCert, 2 years) | UCert | https://courses.aber.ac.uk/postgraduate/livestock-science-pgcert |
| 8 | Nuffield Scholarship (UCert, 2 years) | UCert | https://courses.aber.ac.uk/postgraduate/D406D-nuffield |
| 9 | Sustainable Agriculture (MSc, 3 years) | MSc | https://courses.aber.ac.uk/postgraduate/sustainable-agriculture-3 |
| 10 | Sustainable Agriculture (MSc, 5 years) | MSc | https://courses.aber.ac.uk/postgraduate/sustainable-agriculture |

#### Animal & Aquatic Sciences
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Animal Science (MRes, 1 year) | MRes | https://courses.aber.ac.uk/postgraduate/animal-science |
| 2 | Animal Science (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/animal-science-masters |
| 3 | Equine Science (MRes, 1 year) | MRes | https://courses.aber.ac.uk/postgraduate/equine-science |
| 4 | Parasite Control (MRes, 1 year) | MRes | https://courses.aber.ac.uk/postgraduate/parasite-control |

#### Art
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Fine Art (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/fine-art-masters |

#### Biosciences
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Biosciences (MRes, 1 year) | MRes | https://courses.aber.ac.uk/postgraduate/biosciences-masters-research |

#### Business & Management
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Archives and Records Management (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/archives-records-management |
| 2 | Archives and Records Management (MA, 2 years) | MA | https://courses.aber.ac.uk/postgraduate/archives-records-management-dl2 |
| 3 | Archives and Records Management (MA, 5 years) | MA | https://courses.aber.ac.uk/postgraduate/archives-records-management-dl |
| 4 | Behaviour Change (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/C801-behaviour-change |
| 5 | Biodiversity and Conservation Management (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/biodiversity-conservation-management |
| 6 | Business Administration (MBA, 1 year) | MBA | https://courses.aber.ac.uk/postgraduate/business-administration |
| 7 | Engineering Management (MBA, 1 year) | MBA | https://courses.aber.ac.uk/postgraduate/engineering-management |
| 8 | Engineering Management (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/N23F-engineering-management |
| 9 | Global Supply Chain Management (MBA, 1 year) | MBA | https://courses.aber.ac.uk/postgraduate/global-management |
| 10 | International Business Management (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/international-business-management-msc |
| 11 | International Business and Marketing (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/international-business-marketing-msc |
| 12 | Management (ExecMBA, 3 years) | ExecMBA | https://courses.aber.ac.uk/postgraduate/management-dl |
| 13 | Management (ExecMMgt, 3 years) | ExecMMgt | https://courses.aber.ac.uk/postgraduate/emmgt-mangement |
| 14 | Project Management (MBA, 1 year) | MBA | https://courses.aber.ac.uk/postgraduate/project-management |

#### Computer Science
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Advanced Computer Science (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/computer-science-software-engineering-masters |
| 2 | Advanced Computer Science (with integrated year in industry) (MSc, 2 years) | MSc | https://courses.aber.ac.uk/postgraduate/software-engineering-integrated-industrial-year |
| 3 | Artificial Intelligence (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/artificial-intelligence-msc |
| 4 | Computer Science (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/computer-science-msc |
| 5 | Data Science (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/masters-data-science |
| 6 | Intelligent Wireless Communications and Networks (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/intelligent-wireless-communications-networks |

#### Criminology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Criminology and Criminal Justice (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/M984-criminology-criminal-justice |
| 2 | Criminology and Criminal Justice (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/M983-criminology-criminal-justice |

#### Education & Childhood Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Education (Wales) (MA, 3 years) | MA | https://courses.aber.ac.uk/postgraduate/education-wales |
| 2 | Education (Wales): Additional Learning Needs (MA, 3 years) | MA | https://courses.aber.ac.uk/postgraduate/education-wales-additional-needs |
| 3 | Education (Wales): Curriculum (MA, 3 years) | MA | https://courses.aber.ac.uk/postgraduate/education-wales-curriculum |
| 4 | Education (Wales): Equity in Education (MA, 3 years) | MA | https://courses.aber.ac.uk/postgraduate/education-wales-equity |
| 5 | Education (Wales): Leadership (MA, 3 years) | MA | https://courses.aber.ac.uk/postgraduate/education-wales-leadership |

#### Engineering
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Space Engineering (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/space-engineering |

#### English & Creative Writing
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Creative Writing (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/creative-writing-masters |
| 2 | Literary Studies (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/literary-studies-masters |

#### Film, Television & Media
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Documentary Filmmaking: Landscape and Ecology (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/documentary-film |

#### Geography, Earth & Environmental Sciences
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Remote Sensing and GIS (MSc, 1 year) | MSc | https://courses.aber.ac.uk/postgraduate/gis-remote-sensing-masters |
| 2 | Society and Space (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/198L-society-space |

#### History
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | History of Wales (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/history-of-wales-masters |
| 2 | Medieval Britain & Europe (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/medieval-british-and-european-history-masters |
| 3 | Modern History (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/modern-history-masters |

#### Information Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Information and Library Studies (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/information-and-library-studies-masters |
| 2 | Information and Library Studies (MA, 2 years) | MA | https://courses.aber.ac.uk/postgraduate/information-library |
| 3 | Information and Library Studies (MA, 5 years) | MA | https://courses.aber.ac.uk/postgraduate/information-and-library-studies-distance-learning-masters |

#### Law
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | By Research (LLM, 1 year) | LLM | https://courses.aber.ac.uk/postgraduate/M1866-llm-research |
| 2 | Human Rights and Humanitarian Law (LLM, 1 year) | LLM | https://courses.aber.ac.uk/postgraduate/M198-human-rights-humanitarian-law |
| 3 | International Commercial Law (LLM, 1 year) | LLM | https://courses.aber.ac.uk/postgraduate/M190-international-commercial-law |
| 4 | Law (LLM, 1 year) | LLM | https://courses.aber.ac.uk/postgraduate/M172-law |

#### Marketing
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | International Marketing (MBA, 1 year) | MBA | https://courses.aber.ac.uk/postgraduate/international-marketing |

#### Politics & International Relations
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | International Politics (Dual Degree) (MA, 2 years) | MA | https://courses.aber.ac.uk/postgraduate/politics-dual |
| 2 | International Relations (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/international-relations-L288 |
| 3 | War, Strategy and Intelligence (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/war-strategy-L254 |

#### Welsh & Celtic Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Professional Translation Studies (MA, 1 year) | MA | https://courses.aber.ac.uk/postgraduate/astudiaethau-cyfieithu |

### 2.2 Postgraduate research (PGR)

Aberystwyth offers **65 postgraduate research programmes**:


#### Accounting & Finance
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Accounting (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-accounting |
| 2 | Accounting (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/phd-accounting |

#### Agriculture
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Agriculture (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-agriculture |
| 2 | Agriculture (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/phd-agriculture |
| 3 | BioInnovation (DProf, 5 years) | DProf | https://courses.aber.ac.uk/postgraduate/bioinnovation-professional-doctorate |
| 4 | Biological Sciences (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-biological-sciences |
| 5 | Biological Sciences (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-ibers |
| 6 | Biological Sciences (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-ibers |

#### Art
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Art (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-Art |
| 2 | Art (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-art |
| 3 | Art (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-art |

#### Business & Management
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Management and Business (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-management-business |
| 2 | Management and Business (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-management-business |
| 3 | Management and Business (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-management-business |

#### Computer Science
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Computer Science (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-computer-science |
| 2 | Computer Science (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-computer-science |
| 3 | Computer Science (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/computer-science-research |

#### Criminology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Criminology (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/criminology-mphil |
| 2 | Criminology (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/criminology-phd |
| 3 | Law (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/M1450-law-criminology-phd |
| 4 | Law and Criminology (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-law-criminology |

#### Drama & Theatre
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Theatre, Film and Television Studies (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/W4740-TFTS-MPhil |
| 2 | Theatre, Film and Television Studies (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-tfts |

#### Economics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Economics (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-economics |
| 2 | Economics (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/phd-economics |

#### Education & Childhood Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Education (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-education |
| 2 | Education (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-education |
| 3 | Education (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-education |

#### English & Creative Writing
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Creative Writing (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/creative-writing-mphil |
| 2 | Creative Writing (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-creative-writing |
| 3 | English (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/literature-mphil |
| 4 | English (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-literature |
| 5 | English and Creative Writing (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-english-creative-writing |

#### Film, Television & Media
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Theatre, Film and Television Studies (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/dprof-theatre-film-television |

#### Geography, Earth & Environmental Sciences
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Geography (Arts) (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-geography |
| 2 | Geography (Arts) (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/phd-arts-dges |
| 3 | Geography and Earth Sciences (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-geography-earth-sciences |
| 4 | Geography and Earth Sciences (Science) (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-geography-science |
| 5 | Geography and Earth Sciences (Science) (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-iges |

#### History
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | History (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-history |
| 2 | History (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-history |
| 3 | History (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-history |

#### Information Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Librarianship (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/librarianship |
| 2 | Librarianship (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-librarianship |
| 3 | Librarianship (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-information-studies |

#### Law
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Law (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/M1450-law-mphil |

#### Mathematics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Mathematics (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/dprof-mathematics |
| 2 | Mathematics (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-mathematics |
| 3 | Mathematics (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-mathematics |

#### Modern Languages
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | European Languages (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/modernlangs/mphil |
| 2 | European Languages (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-european-languages |
| 3 | Modern Languages (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-modern-languages |

#### Physics
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Physics (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-physics |
| 2 | Physics (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-physics |
| 3 | Physics (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-physics |

#### Politics & International Relations
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | International Politics (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-international-politics |
| 2 | International Politics (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/international-politics-mphil |
| 3 | International Politics (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-international-politics |

#### Psychology
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Psychology (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/DProf-psychology |
| 2 | Psychology (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-psychology |
| 3 | Psychology (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-psychology |

#### Sport & Exercise Science
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Sport and Exercise Science (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/mphil-sports-exercise |
| 2 | Sport and Exercise Science (PhD, 3 years) | PhD | https://courses.aber.ac.uk/postgraduate/research-sport-exercise |

#### Welsh & Celtic Studies
| # | 专业 | Degree | URL |
|---|------|--------|-----|
| 1 | Welsh (DProf, 3 years) | DProf | https://courses.aber.ac.uk/postgraduate/dprof-Welsh |
| 2 | Welsh (MPhil, 1 year) | MPhil | https://courses.aber.ac.uk/postgraduate/welsh-mphil |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | A40 |
| **Main application deadline** | 29 January (2026 entry) |
| **UCAS Extra opens** | February 2026 |
| **Clearing opens** | July 2026 |
| **Entry year** | September 2026 |

### 3.2 Undergraduate — academic entry requirements (typical)

| 考试体系 | 标准要求 | 来源 |
|---------|---------|------|
| **A-Level** | BBB–CCC (varies by course) | Course pages |
| **UCAS Tariff** | 96–120 points (varies by course) | Course pages |
| **IB Diploma** | 26–30 points (varies by course) | Course pages |
| **BTEC** | DDM–MMM (varies by course) | Course pages |
| **Welsh Baccalaureate** | Accepted as part of offers | Course pages |

> **Note**: Entry requirements vary by course. Aberystwyth generally has lower entry requirements than Russell Group universities, making it accessible to a wider range of applicants. Specific requirements should be checked on individual course pages.

### 3.3 Undergraduate English language requirements

| 考试类型 | Computer Science & Business | All Other Courses | 来源 |
|---------|---------------------------|-------------------|------|
| **IELTS Academic** | 6.0 overall (min 5.5 each) | 6.5 overall (min 5.5 each) | `aber.ac.uk/en/study-with-us/international/english-requirements/ug-english-requirements/` |
| **IELTS Nursing** | — | 7.0 overall (6.5 writing, 7.0 others) | Same source |
| **TOEFL iBT (pre-2026)** | 88 (R18, L17, S20, W17) | 93 (R18, L17, S20, W17) | Same source |
| **TOEFL iBT (post-2026)** | 4.0 overall (min 4 each) | 4.5 overall (min 4.5 each) | Same source |
| **PTE Academic** | 59 overall (min 59 each) | — | Same source |
| **Oxford ELLT** | Score 6 (min 5 each) | Score 7 (min 5 each) | Same source |
| **Cambridge C1 Advanced** | Grade C (min 162 each) | Grade C (min 162 each) | Same source |
| **Cambridge C2 Proficiency** | Grade C (min 162 each) | Grade C (min 162 each) | Same source |

> **Exemptions**: Applicants with a degree from a majority English-speaking country are exempt. English language test results are valid for a maximum of 2 years.
> **Country-specific qualifications**: German Abitur Grade 10+, French Baccalaureat 12+, Dutch VWO 7.5+, Hong Kong HKDSE Level 4, Indian Standard XII at 70%, South Africa NSC C/5.

### 3.4 Graduate admissions

Postgraduate entry requirements vary by programme. Generally:

- **Taught Masters (MSc/MA/MBA)**: A good honours degree (2:1 or 2:2 depending on programme)
- **Research (PhD/MPhil)**: A good Masters degree in a relevant subject
- **English language**: Separate PG requirements apply (see `aber.ac.uk/en/study-with-us/international/english-requirements/pg-english-requirements/`)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition fees (2026 entry)

| Fee status | Annual tuition | Source |
|-----------|---------------|--------|
| **Home (UK)** | £9,790 | `aber.ac.uk/en/study-with-us/fees/undergrad/tuition-fees/` |
| **International — Arts/Social Sciences** | £19,190 | Same source |
| **International — Sciences** | £21,875 | Same source |
| **Year in Industry** | £1,958 | Same source |
| **Year Abroad** | £1,465 | Same source |
| **Foundation Year (classroom-based)** | £5,760 | Same source |

> **Note**: International fees are frozen at the level of entry for subsequent study years.

### 4.2 Postgraduate tuition fees (2026/27)

| Programme | Arts & Social Sciences | Sciences | MBA |
|-----------|----------------------|----------|-----|
| **Masters (MA/MSc/MRes)** | £20,805 | £22,410 | £21,930 |
| **Research (PhD/MPhil)** | £19,070 | £21,515 | — |
| **Professional Doctorate (DProf)** | £17,000 | £17,000 | — |

### 4.3 Estimated living costs (per year)

| 项目 | University Residences (£/month) | Private Sector (£/month) |
|------|-------------------------------|-------------------------|
| Accommodation | From £640 | £442 |
| Food, Laundry & Toiletries | £222 | £222 |
| Bills (Energy, Internet) | Included | £95 |
| Social | £80 | £80 |
| Travel Home | £35 | £35 |
| **Total (estimated, ~39 weeks)** | **~£8,500–£10,000** | **~£8,000–£9,500** |

> **Note**: Aberystwyth is consistently one of the most affordable university towns in the UK. Residential costs include energy, internet, insurance, and sports package.

### 4.4 Scholarships

- International scholarships available at undergraduate and postgraduate level
- Scholarship page: `aber.ac.uk/en/study-with-us/international/scholarships/`
- International Accommodation Award available for eligible students
- U.S. Federal Loans accepted (FAFSA): `aber.ac.uk/en/study-with-us/international/usloans/`

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Aberystwyth University"
  source_url: https://www.aber.ac.uk
  source_snippet: "Aberystwyth University"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-002:
  field: institution.faculties
  value: "2 Faculties: Humanities (11 depts), Sciences (8 depts)"
  source_url: https://www.aber.ac.uk/en/about-us/departments-faculties/faculties/
  source_snippet: "Faculty of Humanities / Faculty of Sciences"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-003:
  field: institution.departments
  value: "22 Academic Departments"
  source_url: https://www.aber.ac.uk/en/about-us/departments-faculties/
  source_snippet: "22 academic departments listed"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-004:
  field: undergraduate.programs.count
  value: "311 undergraduate degree programmes"
  source_url: https://courses.aber.ac.uk/atoz/
  source_snippet: "A-Z listing, 311 UG courses extracted"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-005:
  field: postgraduate.programs.count
  value: "132 postgraduate programmes"
  source_url: https://courses.aber.ac.uk/atoz/
  source_snippet: "A-Z listing, 132 PG courses extracted"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-006:
  field: undergraduate.fees.home
  value: "£9,790 per year (2026 entry)"
  source_url: https://www.aber.ac.uk/en/study-with-us/fees/undergrad/tuition-fees/
  source_snippet: "Home undergraduate fees 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-007:
  field: undergraduate.fees.international.arts
  value: "£19,190 per year (2026 entry)"
  source_url: https://www.aber.ac.uk/en/study-with-us/fees/undergrad/tuition-fees/
  source_snippet: "International Arts/Social Sciences fees"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-008:
  field: undergraduate.fees.international.science
  value: "£21,875 per year (2026 entry)"
  source_url: https://www.aber.ac.uk/en/study-with-us/fees/undergrad/tuition-fees/
  source_snippet: "International Science fees"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-009:
  field: undergraduate.english.ielts
  value: "IELTS 6.0 (CS/Business) or 6.5 (others), min 5.5 each"
  source_url: https://www.aber.ac.uk/en/study-with-us/international/english-requirements/ug-english-requirements/
  source_snippet: "UG English language requirements"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-010:
  field: undergraduate.english.toefl
  value: "TOEFL iBT 88 (CS/Business) or 93 (others)"
  source_url: https://www.aber.ac.uk/en/study-with-us/international/english-requirements/ug-english-requirements/
  source_snippet: "UG English language requirements"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-011:
  field: undergraduate.application.system
  value: "UCAS"
  source_url: https://courses.aber.ac.uk/
  source_snippet: "Course search portal"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-012:
  field: institution.founded
  value: "1872 (first university in Wales)"
  source_url: https://www.aber.ac.uk/en/about-us/about/
  source_snippet: "About page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-013:
  field: institution.students
  value: "~6,000 students"
  source_url: https://www.aber.ac.uk/en/about-us/about/
  source_snippet: "About page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-014:
  field: institution.ref
  value: "98% of research internationally recognised (REF 2021)"
  source_url: https://www.aber.ac.uk/en/about-us/about/
  source_snippet: "About page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-015:
  field: institution.award
  value: "University of the Year for Sustainability (Good University Guide 2026)"
  source_url: https://www.aber.ac.uk/en/about-us/about/
  source_snippet: "About page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-016:
  field: postgraduate.fees.masters.arts
  value: "£20,805 per year"
  source_url: https://www.aber.ac.uk/en/study-with-us/international/fees-scholarships/
  source_snippet: "International fees page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-017:
  field: postgraduate.fees.masters.sciences
  value: "£22,410 per year"
  source_url: https://www.aber.ac.uk/en/study-with-us/international/fees-scholarships/
  source_snippet: "International fees page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-018:
  field: postgraduate.fees.research
  value: "£19,070 (Arts) / £21,515 (Sciences)"
  source_url: https://www.aber.ac.uk/en/study-with-us/international/fees-scholarships/
  source_snippet: "International fees page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-019:
  field: undergraduate.entry.alevel
  value: "BBB–CCC typical (varies by course)"
  source_url: https://courses.aber.ac.uk/
  source_snippet: "Course pages"
  capture_date: 2026-07-08
  evidence_type: official_webpage
E-U-020:
  field: undergraduate.fees.frozen
  value: "International fees frozen at entry level"
  source_url: https://www.aber.ac.uk/en/study-with-us/fees/undergrad/tuition-fees/
  source_snippet: "Fee page"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
aberystwyth-university-knowledge-base-v2
├── 0-overview (Section 0: rule 1-4, institution overview)
├── 1-undergraduate (Section 1: full UG programme listing, chunked by Subject Area)
│   ├── chunk-accounting-finance
│   ├── chunk-agriculture
│   ├── chunk-animal-aquatic-sciences
│   ├── chunk-art
│   ├── chunk-biochemistry-genetics
│   ├── chunk-biosciences
│   ├── chunk-business-management
│   ├── chunk-computer-science
│   ├── chunk-criminology
│   ├── chunk-drama-theatre
│   ├── chunk-ecological-sciences
│   ├── chunk-economics
│   ├── chunk-education-childhood-studies
│   ├── chunk-engineering
│   ├── chunk-english-creative-writing
│   ├── chunk-film-television-media
│   ├── chunk-geography-earth-environmental-sciences
│   ├── chunk-history
│   ├── chunk-human-biology-health
│   ├── chunk-information-studies
│   ├── chunk-law
│   ├── chunk-marketing
│   ├── chunk-mathematics
│   ├── chunk-modern-languages
│   ├── chunk-nursing
│   ├── chunk-physics
│   ├── chunk-politics-international-relations
│   ├── chunk-psychology
│   ├── chunk-sociology
│   ├── chunk-sport-exercise-science
│   ├── chunk-veterinary-studies
│   ├── chunk-welsh-celtic-studies
├── 2-graduate (Section 2: PGT + PGR programmes)
├── 3-applications (Section 3: requirements, deadlines, English)
├── 4-costs (Section 4: fees, living costs, scholarships)
├── 5-evidence (Section 5: evidence chain)
└── 6-comparison (Section 7: cross-school comparison)
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P1** | Per-course A-Level/IB entry requirements | Individual course pages |
| **P1** | Per-course detailed module lists | Individual course pages |
| **P1** | Scholarship amounts and eligibility criteria | `aber.ac.uk/en/study-with-us/international/scholarships/` |
| **P2** | Accommodation options and costs (detailed) | `aber.ac.uk/en/study-with-us/accommodation/` |
| **P2** | Student satisfaction / NSS scores | External sources |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Aberystwyth University | Cardiff | Newcastle |
|-----------|----------------------|---------|-----------|
| Total UG programmes | 311 | 237 | 147 |
| Academic departments | 22 | 24 | — |
| Faculties | 2 | 3 | — |
| UG Home tuition (2026) | £9,790 | £9,250 | — |
| UG International (Arts) | £19,190 | £22,700–£29,450 | — |
| UG International (Science) | £21,875 | (within range) | — |
| IELTS minimum (UG) | 6.0 (CS/Business), 6.5 (others) | 6.5 (5.5 each) | — |
| A-Level typical | BBB–CCC | ABB | — |
| Russell Group | No | Yes | Yes |
| UCAS deadline | 29 Jan | 29 Jan | — |
| Region | Wales, UK | Wales, UK | England, UK |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: courses.aber.ac.uk (course portal), aber.ac.uk (main domain)
> **Verification**: ego-browser snapshotText + JS DOM extraction + WebFetch
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programs (311/311) ✅ | PG programs (132/132) ✅ | Evidence (20 blocks) ✅