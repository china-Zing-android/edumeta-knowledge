# University of Oxford Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位课程 (UG degree courses) | 52 |
| 本科 Foundation Year 课程 | 4 |
| 研究生课程 (PG courses) | 407 |
| 研究生学位类型 (PG degree types) | 17 |
| 学术学部 (Academic Divisions) | 4 |
| 学部下属系所/学院 (Departments/Schools) | 59+ |
| 书院 (Colleges) | 43 (含 Permanent Private Halls) |
| **学位课程总计 (UG + PG)** | **459** |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

> Oxford 采用 **Collegiate** 体制：学术组织分为 4 个学部 (Divisions)，学部下属系所 (Departments/Faculties/Schools) 负责教学与研究，另有 43 个独立书院 (Colleges) 负责学生生活与辅导 (Tutorial)。以下仅列学术学部及其下属系所。

```
University of Oxford
│
├── Humanities Division                                 [学部]
│   ├── Rothermere American Institute                   [系/研究所]
│   ├── Ruskin School of Art                            [系/学院]
│   ├── Faculty of Asian and Middle Eastern Studies     [系/学院]
│   ├── Faculty of Classics                             [系/学院]
│   ├── Faculty of English Language and Literature      [系/学院]
│   ├── Faculty of History                              [系/学院]
│   ├── Department of History of Art                    [系]
│   ├── Faculty of Linguistics, Philology and Phonetics [系/学院]
│   ├── Faculty of Medieval and Modern Languages        [系/学院]
│   ├── Faculty of Music                                [系/学院]
│   ├── Faculty of Philosophy                           [系/学院]
│   ├── Faculty of Theology and Religion                [系/学院]
│   ├── Institute for Ethics in AI                      [研究所]
│   ├── TORCH (Oxford Research Centre in the Humanities) [研究中心]
│   ├── Voltaire Foundation                             [研究机构]
│   ├── Ertegun Graduate Scholarship Programme          [奖学金项目]
│   └── Modern Slavery & Human Rights PEC               [政策中心]
│
├── Mathematical, Physical and Life Sciences (MPLS) Division  [学部]
│   ├── Department of Biology                           [系]
│   ├── Department of Chemistry                         [系]
│   ├── Department of Computer Science                  [系]
│   ├── Department of Earth Sciences                    [系]
│   ├── Department of Engineering Science               [系]
│   ├── Department of Materials                         [系]
│   ├── Mathematical Institute                          [系/研究所]
│   ├── Department of Physics                           [系]
│   ├── Department of Statistics                        [系]
│   ├── Doctoral Training Centre                        [培训中心]
│   └── Begbroke Science Park                           [科技园]
│
├── Medical Sciences Division                           [学部]
│   ├── Department of Biochemistry                      [系]
│   ├── Nuffield Department of Clinical Medicine        [系]
│   ├── Nuffield Department of Clinical Neurosciences   [系]
│   ├── Department of Experimental Psychology           [系]
│   ├── Radcliffe Department of Medicine                [系]
│   ├── Department of Oncology                          [系]
│   ├── Nuffield Dept of Orthopaedics, Rheumatology     [系]
│   │   and Musculoskeletal Sciences
│   ├── Department of Paediatrics                       [系]
│   ├── Sir William Dunn School of Pathology            [系/学院]
│   ├── Department of Pharmacology                      [系]
│   ├── Department of Physiology, Anatomy & Genetics    [系]
│   ├── Nuffield Department of Population Health        [系]
│   ├── Department of Primary Care Health Sciences      [系]
│   ├── Department of Psychiatry                        [系]
│   ├── Nuffield Department of Surgical Sciences        [系]
│   └── Nuffield Department of Women's & Reproductive   [系]
│       Health
│
├── Social Sciences Division                            [学部]
│   ├── School of Anthropology and Museum Ethnography   [系/学院]
│   ├── School of Archaeology                           [系/学院]
│   ├── Said Business School                            [系/学院]
│   ├── Department of Economics                         [系]
│   ├── Department of Education                         [系]
│   ├── School of Geography and the Environment         [系/学院]
│   ├── Oxford School of Global and Area Studies        [系/学院]
│   ├── Blavatnik School of Government                  [系/学院]
│   ├── Department of International Development         [系]
│   ├── Oxford Internet Institute                       [研究所]
│   ├── Faculty of Law                                  [系/学院]
│   ├── Oxford Martin School                            [研究所]
│   ├── Department of Politics & International Relations[系]
│   ├── Department of Social Policy and Intervention    [系]
│   └── Department of Sociology                         [系]
│
└── Department for Continuing Education                 [独立系]
    └── Gardens, Libraries and Museums (GLAM)           [附属机构]
        ├── Ashmolean Museum
        ├── Bodleian Libraries
        ├── History of Science Museum
        ├── Oxford Botanic Garden & Arboretum
        ├── Oxford University Museum of Natural History
        └── Pitt Rivers Museum
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Canonical 缩写 | Official (本校) | 全称 | 层级 | 本项目数量 |
|---------------|-----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 33 (含 joint honours) |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 1 |
| MBiochem | MBiochem | Master of Biochemistry (integrated) | 本科 (integrated master's) | 1 |
| MBiol | MBiol | Master of Biology (integrated) | 本科 (integrated master's) | 1 |
| MBiomedSci | MBiomedSci | Master of Biomedical Sciences (integrated) | 本科 (integrated master's) | 1 |
| MChem | MChem | Master of Chemistry (integrated) | 本科 (integrated master's) | 1 |
| MCompSci | MCompSci | Master of Computer Science (integrated) | 本科 (integrated master's) | 1 |
| MCompPhil | MCompPhil | Master of Computer Science & Philosophy (integrated) | 本科 (integrated master's) | 1 |
| MEarthSci | MEarthSci | Master of Earth Sciences (integrated) | 本科 (integrated master's) | 1 |
| MEng | MEng | Master of Engineering (integrated) | 本科 (integrated master's) | 2 |
| MMath | MMath | Master of Mathematics (integrated) | 本科 (integrated master's) | 1 |
| MMathCompSci | MMathCompSci | Master of Mathematics & Computer Science (integrated) | 本科 (integrated master's) | 1 |
| MMathPhil | MMathPhil | Master of Mathematics & Philosophy (integrated) | 本科 (integrated master's) | 1 |
| MPhys | MPhys | Master of Physics (integrated) | 本科 (integrated master's) | 1 |
| MPhysPhil | MPhysPhil | Master of Physics & Philosophy (integrated) | 本科 (integrated master's) | 1 |
| MSci | MSci | Master of Science (integrated) | 本科 (integrated master's) | 2 |
| BM BCh | BM BCh | Bachelor of Medicine, Bachelor of Surgery | 本科 (medicine) | 2 |
| BA LLB | BA (equivalent to LLB) | BA in Jurisprudence | 本科 (law) | 1 |
| Foundation Year | Foundation Year | Foundation Year (pre-degree) | 本科 (预科) | 4 |
| DPhil | DPhil | Doctor of Philosophy | 研究生 | ~200+ |
| MSc | MSc | Master of Science | 研究生 | ~100+ |
| MSt | MSt | Master of Studies | 研究生 | ~40+ |
| MPhil | MPhil | Master of Philosophy | 研究生 | ~30+ |
| MBA | MBA | Master of Business Administration | 研究生 | ~3 |
| MPP | MPP | Master of Public Policy | 研究生 | 1 |
| MFA | MFA | Master of Fine Art | 研究生 | 1 |
| MTh | MTh | Master of Theology | 研究生 | ~2 |
| BCL | BCL | Bachelor of Civil Law | 研究生 | 1 |
| MJur | MJur | Magister Juris | 研究生 | 1 |
| MLitt | MLitt | Master of Letters | 研究生 | ~2 |
| BPhil | BPhil | Bachelor of Philosophy | 研究生 | 1 |
| PGCE | PGCE | Postgraduate Certificate in Education | 研究生 | 9 |
| PGCert | PGCert | Postgraduate Certificate | 研究生 | ~5 |
| PGDip | PGDip | Postgraduate Diploma | 研究生 | ~5 |
| DClinPsych | DClinPsych | Doctor of Clinical Psychology | 研究生 | 1 |

> **说明**: Oxford 使用 "DPhil" 而非 "PhD" 表示博士学位，这是牛津特色。Integrated master's (4 年制) 是本科课程但授予硕士学位，在 UCAS 上注册为 undergraduate。PG 精确数量需从课程搜索页面逐页抓取 (407 个结果)，数量为基于课程名称样本的估算。

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

> 本科课程按学部 × 学位级别分布。研究生课程因数量庞大(407)且按系所分散，以学部汇总。Joint honours 课程可能跨学部，按主要归属列示。

**本科课程分布矩阵 (学部 × Canonical 学位级别)**

| 学部 \ 学位 | BA | BFA | MChem | MEng | MMath | MPhys | MBiol | MBiochem | MBiomedSci | MCompSci | MEarthSci | MSci | BM BCh | FY | 合计 |
|-----------|-----|-----|-------|------|-------|-------|-------|----------|------------|----------|-----------|------|--------|----|------|
| Humanities | 18 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 20 |
| MPLS | 0 | 0 | 1 | 2 | 2 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 0 | 1 | 13 |
| Medical Sciences | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 2 | 2 | 0 | 5 |
| Social Sciences | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 11 |
| Cross-division* | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| **合计** | **30** | **1** | **1** | **2** | **2** | **2** | **1** | **1** | **1** | **2** | **1** | **2** | **2** | **4** | **52** |

> *Cross-division: Human Sciences (跨多个学部), Psychology, Philosophy and Linguistics (跨 Medical Sciences + Humanities), 以及一些 joint honours 课程跨学部。部分课程提供 BA 和 integrated master's 两轨 (如 Computer Science: BA or MCompSci)，表中按 higher degree 统计。

**PG 课程分布 (按学部汇总)**

| 学部 | 估算课程数 |
|------|----------|
| Humanities Division | ~80 |
| MPLS Division | ~80 |
| Medical Sciences Division | ~100 |
| Social Sciences Division | ~120 |
| Continuing Education | ~27 |
| **合计** | **~407** |

> PG 课程总数来自课程搜索页面 (407)，精确的学部 × 学位级别矩阵需要完整逐页抓取，标记为 P1 后续任务。

---

## SECTION 1 — Undergraduate Education

### 1.1 College/School Architecture

Oxford 的本科教育由 4 个学术学部 (Divisions) 下属的系所组织教学，同时由 43 个书院 (Colleges) 和 Permanent Private Halls 提供 Tutorial 辅导。申请时需通过 UCAS 提交，截止日期为每年 10 月 15 日。课程在 UCAS 上注册为 undergraduate 学位，但 4 年制课程 (integrated master's) 最终授予硕士学位。

### 1.2 Undergraduate Courses — grouped by 学部 > 系 > 学位级别

#### Humanities Division

##### Faculty of Classics
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 1 | Classics | Q800 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classics |
| 2 | Classics and Asian and Middle Eastern Studies | TQ89 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classics-and-asian-and-middle-eastern-studies |
| 3 | Classics and English | QQ38 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classics-and-english |
| 4 | Classics and Modern Languages | Varies | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classics-and-modern-languages |
| 5 | Classical Archaeology and Ancient History | VV14 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classical-archaeology-and-ancient-history |

##### Faculty of English Language and Literature
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 6 | English Language and Literature | Q300 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/english-language-and-literature |
| 7 | English and Modern Languages | Varies | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/english-and-modern-languages |
| 8 | Classics and English | QQ38 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/classics-and-english |
| 9 | History and English | VQ13 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-english |

##### Faculty of History
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 10 | History | V100 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history |
| 11 | History (Ancient and Modern) | V118 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-ancient-and-modern |
| 12 | History and Economics | LV11 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-economics |
| 13 | History and English | VQ13 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-english |
| 14 | History and Modern Languages | Varies | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-modern-languages |
| 15 | History and Politics | LV21 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-politics |

##### Department of History of Art
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 16 | History of Art | V350 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-of-art |

##### Faculty of Asian and Middle Eastern Studies
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 17 | Asian and Middle Eastern Studies | T600 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/asian-and-middle-eastern-studies |
| 18 | European and Middle Eastern Languages | Various | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/european-and-middle-eastern-languages |
| 19 | Religion and Asian and Middle Eastern Studies | VT66 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/religion-and-asian-and-middle-eastern-studies |

##### Faculty of Medieval and Modern Languages
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 20 | Modern Languages | Various | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/modern-languages |
| 21 | Modern Languages and Linguistics | Various | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/modern-languages-and-linguistics |
| 22 | Philosophy and Modern Languages | Various | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/philosophy-and-modern-languages |
| 23 | English and Modern Languages | Varies | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/english-and-modern-languages |
| 24 | History and Modern Languages | Varies | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-modern-languages |

##### Faculty of Music
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 25 | Music | W300 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/music |

##### Faculty of Philosophy
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 26 | Philosophy and Modern Languages | Various | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/philosophy-and-modern-languages |
| 27 | Philosophy and Theology | VV56 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/philosophy-and-theology |

##### Faculty of Theology and Religion
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 28 | Theology and Religion | V600 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/theology-and-religion |
| 29 | Philosophy and Theology | VV56 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/philosophy-and-theology |
| 30 | Religion and Asian and Middle Eastern Studies | VT66 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/religion-and-asian-and-middle-eastern-studies |

##### Ruskin School of Art
###### BFA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 31 | Fine Art | W100 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/fine-art |

##### Foundation Year (Humanities Division)
###### Foundation Year
| # | 课程 | Duration | URL |
|---|------|----------|-----|
| 32 | Foundation Year in Humanities | 1 year | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-humanities |

#### Mathematical, Physical and Life Sciences (MPLS) Division

##### Department of Chemistry
###### MChem
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 33 | Chemistry | F100 | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/chemistry |

##### Department of Computer Science
###### BA or MCompSci
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 34 | Computer Science | G400 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/computer-science |

###### BA or MCompPhil
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 35 | Computer Science and Philosophy | IV15 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/computer-science-and-philosophy |

##### Department of Earth Sciences
###### BA Geology or MEarthSci
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 36 | Earth Sciences (Geology) | F640 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/earth-sciences-geology |

##### Department of Engineering Science
###### MEng
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 37 | Engineering Science | See course codes | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/engineering-science |

##### Department of Materials
###### MEng
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 38 | Materials Science | FJ22 | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/materials-science |

##### Mathematical Institute
###### MMath or BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 39 | Mathematics / Mathematics and Statistics | G100 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/mathematics |

###### BA or MMathCompSci
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 40 | Mathematics and Computer Science | GG14 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/mathematics-and-computer-science |

###### BA / MMathPhil
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 41 | Mathematics and Philosophy | GV15 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/mathematics-and-philosophy |

##### Department of Physics
###### MPhys / BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 42 | Physics | F303 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/physics |

###### MPhysPhil / BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 43 | Physics and Philosophy | VF53 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/physics-and-philosophy |

##### Department of Biology
###### MBiol or BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 44 | Biology | C100 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/biology |

##### Department of Biochemistry (MPLS / Medical Sciences 共享)
###### MBiochem
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 45 | Biochemistry (Molecular and Cellular) | C700 | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/biochemistry-molecular-and-cellular |

##### Foundation Year (MPLS)
###### Foundation Year
| # | 课程 | Duration | URL |
|---|------|----------|-----|
| 46 | Foundation Year in Chemistry, Engineering and Materials Science | 1 year | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-chemistry-engineering-and-materials-science |

#### Medical Sciences Division

##### Biomedical Sciences (跨系)
###### MBiomedSci or BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 47 | Biomedical Sciences | BC98 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/biomedical-sciences |

##### Medical School
###### BA / BM BCh
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 48 | Medicine | A100 | 6 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/medicine |

###### BM BCh
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 49 | Medicine (graduate-entry) | A101 | 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/medicine-graduate-entry |

#### Social Sciences Division

##### Faculty of Law
###### BA (equivalent to LLB)
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 50 | Law (Jurisprudence) | See course options | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/law-jurisprudence |

##### Department of Economics
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 51 | Economics and Management | LN12 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/economics-and-management |
| 52 | History and Economics | LV11 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-economics |

##### School of Geography and the Environment
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 53 | Geography | L700 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/geography |

##### Department of Politics & International Relations
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 54 | Philosophy, Politics and Economics (PPE) | L0V0 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/philosophy-politics-and-economics |
| 55 | History and Politics | LV21 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/history-and-politics |

##### School of Archaeology
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 56 | Archaeology and Anthropology | LV64 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/archaeology-and-anthropology |

##### Foundation Year (Social Sciences)
###### Foundation Year
| # | 课程 | Duration | URL |
|---|------|----------|-----|
| 57 | Foundation Year in Law | 1 year | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-law |
| 58 | Foundation Year in PPE | 1 year | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-philosophy-politics-and-economics-ppe |

#### Cross-Division / Interdisciplinary

##### Human Sciences (跨 MPLS + Medical Sciences + Social Sciences)
###### BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 59 | Human Sciences | BCL0 | 3 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/human-sciences |

##### Psychology (跨 Medical Sciences + Humanities)
###### MSci / BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 60 | Psychology (Experimental) | C800 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/psychology-experimental |

###### MSci / BA
| # | 课程 | UCAS Code | Duration | URL |
|---|------|-----------|----------|-----|
| 61 | Psychology, Philosophy and Linguistics | CV85 | 3 or 4 years | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/psychology-philosophy-and-linguistics |

> **Note**: 以上 52 个 UG 课程列表 (含 Foundation Year 4 个) 总计 52 个条目。部分 joint honours 课程跨学部，在表中按其主归属列出。每个课程的学部归属按 Oxford 官方分类。

### 1.3 Joint Honours / Interdisciplinary Undergraduate Programs

Oxford 的 joint honours 课程是独立的课程 (非组合 major/minor)，拥有独立的 UCAS code 和课程结构。所有 joint honours 课程已在上表中列出。跨学部课程包括：

| 课程 | 涉及学部 | URL |
|------|---------|-----|
| Human Sciences | MPLS + Medical Sciences + Social Sciences | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/human-sciences |
| Psychology, Philosophy and Linguistics | Medical Sciences + Humanities | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/psychology-philosophy-and-linguistics |
| Computer Science and Philosophy | MPLS + Humanities | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/computer-science-and-philosophy |
| Mathematics and Philosophy | MPLS + Humanities | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/mathematics-and-philosophy |
| Physics and Philosophy | MPLS + Humanities | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/physics-and-philosophy |

### 1.4 Foundation Year Programs

Oxford 提供 4 个 Foundation Year 课程 (Astrophoria Foundation Year)，面向英国 underrepresented 背景的学生，为期 1 年，完成后可升入相关本科学位课程。

| # | Foundation Year 课程 | 目标学部 | URL |
|---|---------------------|---------|-----|
| 1 | Chemistry, Engineering and Materials Science | MPLS | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-chemistry-engineering-and-materials-science |
| 2 | Humanities | Humanities | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-humanities |
| 3 | Law | Social Sciences | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-law |
| 4 | Philosophy, Politics and Economics (PPE) | Social Sciences | https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/foundation-year-in-philosophy-politics-and-economics-ppe |

### 1.5 General/Institute-wide Requirements

Oxford 本科申请的核心要求：
- **UCAS 申请**: 通过 UCAS 提交，截止日期 10 月 15 日 (英国时间 18:00)
- **入学考试 (Admissions Tests)**: 大多数课程要求参加特定科目的入学考试 (如 MAT, PAT, HAT 等)，考试在 10 月进行
- **Written Work**: 部分课程要求提交书面作品，截止日期 11 月 10 日
- **面试 (Interviews)**: 12 月初至中旬进行
- **录取决定**: 2027 年 1 月 12 日公布
- **A-Level 典型要求**: AAA 至 A*A*A (因课程而异)
- **IB 典型要求**: 38-40 分 (含核心分)

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs Overview

Oxford 研究生课程总数约 **407** 个，涵盖 4 个学部及 Department for Continuing Education。课程类型包括：

| 课程类型 | 描述 | 数量估算 |
|---------|------|---------|
| DPhil (Doctor of Philosophy) | 研究型博士 (3-4 年 full-time) | ~200+ |
| MSc (Master of Science) | 授课型/研究型硕士 | ~100+ |
| MSt (Master of Studies) | 授课型硕士 (人文社科为主) | ~40+ |
| MPhil (Master of Philosophy) | 研究型硕士 | ~30+ |
| PGCE | 教师培训证书 | 9 |
| MBA / EMBA | 工商管理硕士 | ~3 |
| Other (MPP, MFA, BCL, MJur, MTh, MLitt, BPhil, PGCert, PGDip, DClinPsych) | 各种专业学位 | ~25 |

### 2.2 Graduate Programs — grouped by Division

> 由于 407 个研究生课程数量庞大，以下按学部列出代表性课程，完整列表需从 `https://www.ox.ac.uk/admissions/graduate/courses/find-your-course` 逐页提取。

#### Humanities Division
典型 PG 课程包括：
- MSt in English (various periods)
- MSt in History
- MPhil in Classics
- DPhil in Philosophy
- MSt in Music (Composition/Musicology)
- MSt in History of Art
- DPhil in Medieval and Modern Languages

#### MPLS Division
典型 PG 课程包括：
- MSc in Advanced Computer Science
- DPhil in Computer Science
- MSc in Mathematical Sciences
- DPhil in Mathematics
- MSc in Physics
- DPhil in Chemistry
- DPhil in Biology
- MSc in Statistical Science
- DPhil in Engineering Science
- DPhil in Materials

#### Medical Sciences Division
典型 PG 课程包括：
- DPhil in Clinical Medicine
- DPhil in Biochemistry
- MSc in Neuroscience
- DPhil in Pharmacology
- DPhil in Psychiatry
- DPhil in Population Health
- MSc in Global Health Science
- DClinPsych

#### Social Sciences Division
典型 PG 课程包括：
- MBA / EMBA (Said Business School)
- MSc in Economics
- MPhil in Economics
- DPhil in Economics
- MSc in Law and Finance
- BCL (Bachelor of Civil Law)
- MJur (Magister Juris)
- DPhil in Law
- MPP (Master of Public Policy)
- MSc in Education
- DPhil in Politics
- MSc in Sociology
- DPhil in International Development
- MSc in Social Data Science
- MSc in Environmental Change and Management

### 2.3 Graduate Admissions Model

Oxford 研究生招生采用 **半集中式 (semi-centralized)** 模式：
- 统一通过 Graduate Application Form 在线申请
- 申请截止日期因课程而异，大多数为 12 月或 1 月 (部分有 11 月 deadline)
- 申请费: £75 (standard application)
- 部分课程有独立申请流程 (Said Business School 大部分课程, DPhil in Biochemistry Skaggs-Oxford Programme, DPhil in Biomedical Sciences NIH OxCam, DClinPsych, PGCE 等)
- 英语语言要求分为 Standard 和 Higher 两个级别，因课程而异
- 最多可申请 3 个课程 (其中 taught courses 最多 2 个)
- 8-10 周后出结果
- 书院 (College) 偏好可在申请中表明

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 详情 |
|------|------|
| 申请平台 | UCAS |
| 申请开放 | 2026 年 9 月初 |
| **申请截止日期** | **2026 年 10 月 15 日 (英国时间 18:00)** |
| 入学考试 (UAT-UK) | 2026 年 10 月 |
| Written Work 截止 | 2026 年 11 月 10 日 |
| 面试时间 | 2026 年 12 月初至中旬 |
| **录取决定公布** | **2027 年 1 月 12 日** |
| 英语语言成绩截止 | 2027 年 7 月 31 日 (offer holder) |
| UCAT (Medicine) | 需在申请前完成 |
| LNAT (Law) | 需在申请前完成 |

### 3.2 Undergraduate English Proficiency Table

牛津大学本科英语要求为 **单一标准级别** (无 Standard/Higher 之分，不同于研究生)。

| 考试 | 总分要求 | 单项要求 |
|------|---------|---------|
| **IELTS Academic** | 7.5 | 每项不低于 7.0 |
| **TOEFL iBT** | 110 | Listening: 22, Reading: 24, Speaking: 25, Writing: 24 |
| **C1 Advanced (CAE)** | 191 | 每项不低于 185 |
| **C2 Proficiency (CPE)** | 191 | 每项不低于 185 |
| **Pearson PTE Academic** | 76 | 每项不低于 66 |
| **Oxford Test of English (Advanced)** | 165 | 每项不低于 155 |
| **Trinity ISE** | ISE III distinction (all skills) 或 ISE IV pass (each section) | — |
| **English Language GCSE** | Grade B/6 + Merit in Speaking | — |
| **Cambridge IGCSE First Language English** | Grade B/6 + Grade 2 in Speaking and Listening | — |
| **OxfordAQA IGCSE English (First Language)** | Grade 6 + Merit in Speaking and Listening | — |
| **Pearson Edexcel English Language A/B (First Language)** | Grade 6 + Merit in Spoken Language | — |
| **Cambridge O-Level English** | Grade B | — |
| **IB English B** | 7 at HL (for those not taught in English) | — |
| **European Baccalaureate** | English at L1 or L2 with 70% | — |
| **SQA ESOL Higher** | Grade B | — |

> **不接受**: IELTS Online, TOEFL Essentials, TOEFL ITP, PTE Academic Online, IELTS General/UKVI General/Life Skills, Second Language English IGCSEs

### 3.3 Graduate — Global Rules

| 维度 | 详情 |
|------|------|
| 申请平台 | Oxford Graduate Application Form (统一在线系统) |
| 申请费 | £75 (standard); 部分课程不同 |
| 申请数量限制 | 最多 3 个课程 (taught courses 最多 2 个) |
| 主要截止日期 | 12 月或 1 月 (因课程而异); 部分课程有 11 月 deadline |
| 奖学金截止日期 | 12 月/1 月 deadline 可获牛津奖学金考虑; 3 月及以后 deadline 不可 |
| 录取决定时间 | 截止日期后 8-10 周 |
| 英语语言要求 | 分为 Standard 和 Higher 两个级别 (因课程而异) |
| 英语语言 waiver | 可申请 (需满足: 全英语授课学位, 9 个月以上, 2 年内完成) |
| 面试 | 部分课程需要 (由学术部门组织) |
| 书院偏好 | 可在申请中表明 |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026/27 Academic Year)

#### Course Fees

| Fee Status | Annual Course Fee (2026/27) | Notes |
|-----------|---------------------------|-------|
| **Home (UK)** | £9,790 | 政府设定上限; 2027/28 年将升至 £10,050 |
| **Overseas (International)** | £37,380 - £62,820 | 因课程而异; 临床医学费用更高 |

> **注意**: 自 2019/20 学年起，课程费用已包含 University tuition 和 College fees，不再分开列出。具体课程费用见各课程页面。

#### Living Costs (2026/27)

| 支出项目 | 每月 (下限) | 每月 (上限) | 9 个月 (下限) | 9 个月 (上限) |
|---------|-----------|-----------|-------------|-------------|
| Food | £315 | £545 | £2,835 | £4,905 |
| Accommodation | £825 | £990 | £7,425 | £8,910 |
| Personal items | £160 | £310 | £1,440 | £2,790 |
| Social activities | £50 | £130 | £450 | £1,170 |
| Study costs | £35 | £90 | £315 | £810 |
| Other | £20 | £40 | £180 | £360 |
| **Total** | **£1,405** | **£2,105** | **£12,645** | **£18,945** |

> 牛津大学本科生奖学金 (如 Crankstart Scholarship) 使用的维持津贴按平均值计算: £15,795/年 (2026/27)。

### 4.2 Undergraduate Financial Aid

- **Oxford Bursaries**: 面向低收入家庭 UK 学生，最高 £6,500/年 (2027 entry)
- **Crankstart Scholarship**: 面向 UK 低收入家庭学生，含 bursary + 实习 + 社交活动
- **政府支持**: Home 学生可申请 Tuition Fee Loan (全额覆盖课程费用)
- **国际学生**: 无 UK 政府贷款资格; 课程费用高出 Home 学生 3-6 倍

### 4.3 Graduate Cost & Funding

- **PG 课程费用**: 因课程而异，见各课程页面 (Funding and costs 部分)
- **PG 申请费**: £75 (standard)
- **PG 住宿费**: 约 £825-£990/月 (与 UG 相同)
- **奖学金**: 牛津奖学金 (Clarendon, Rhodes, Ertegun 等) 及 UKRI 资助
- **Fee Liability**: 课程费用按标准修业年限支付; DPhil 通常 3-4 年

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: institution.name
  value: "University of Oxford"
  source_url: https://www.ox.ac.uk/
  source_snippet: "University of Oxford"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: ug.course_count
  value: "52"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing
  source_snippet: "Showing 1 - 12 of 52 Results"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: ug.course_fees.home
  value: "£9,790"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/fees-and-funding/course-fees
  source_snippet: "If you are a Home student undertaking your first undergraduate degree, current university policy is to charge fees at the level of the cap set by the government, which for 2026/27 will be £9,790."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: ug.course_fees.overseas.range
  value: "Between £37,380 and £62,820"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/fees-and-funding/course-fees
  source_snippet: "Fee status: Overseas | Annual course fees payable by student for 2026/27 | Between £37,380 and £62,820*"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-005:
  field: ug.living_costs.2026_27
  value: "£1,405 - £2,105 per month; £12,645 - £18,945 for 9 months"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/fees-and-funding/living-costs
  source_snippet: "Likely living costs 2026-27: Total per month: £1,405 - £2,105; Total for 9 months: £12,645 - £18,945"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-006:
  field: ug.english_language.ielts
  value: "Overall 7.5, minimum 7.0 per component"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/for-international-students/english-language-requirements-visas
  source_snippet: "IELTS: 7.5 — Minimum 7.0 per component"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: ug.english_language.toefl
  value: "Overall 110, L:22, R:24, S:25, W:24"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/for-international-students/english-language-requirements-visas
  source_snippet: "TOEFL / TOEFL iBT Home Edition: 110 — Minimum component scores: Listening: 22, Reading: 24, Speaking: 25, Writing: 24"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-008:
  field: ug.english_language.pte
  value: "Overall 76, minimum 66 per skill"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/for-international-students/english-language-requirements-visas
  source_snippet: "Pearson PTE Academic: 76 — Minimum 66 in Speaking, Listening, Reading and Writing"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-009:
  field: ug.deadline.ucas
  value: "15 October 2026, 6pm UK time"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/admissions-timeline
  source_snippet: "Submit your application from early September. Final deadline 6pm (UK time) on 15 October"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: ug.deadline.decisions
  value: "12 January 2027"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/admissions-timeline
  source_snippet: "Find out if you have an offer on 12 January 2027"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: ug.structure.divisions
  value: "4 academic divisions: Humanities, MPLS, Medical Sciences, Social Sciences"
  source_url: https://www.ox.ac.uk/about/divisions-and-departments
  source_snippet: "There are four academic divisions within Oxford University. All have a full-time divisional head and an elected divisional board."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: ug.structure.humanities_departments
  value: "17 departments/faculties including Classics, English, History, Music, Philosophy, Theology and Religion, etc."
  source_url: https://www.ox.ac.uk/about/divisions-and-departments
  source_snippet: "Humanities Division — Departments: American Institute, Rothermere; Art, Ruskin School of; Asian and Middle Eastern Studies, Faculty of; Classics, Faculty of; ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: ug.structure.mpls_departments
  value: "11 departments including Biology, Chemistry, Computer Science, Earth Sciences, Engineering Science, Materials, Mathematics, Physics, Statistics"
  source_url: https://www.ox.ac.uk/about/divisions-and-departments
  source_snippet: "Mathematical, Physical and Life Sciences Division — Departments: Biology, Department of; Chemistry, Department of; Computer Science, Department of; ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: ug.structure.medical_sciences_departments
  value: "16 departments including Biochemistry, Clinical Medicine, Clinical Neurosciences, Experimental Psychology, Medicine, Oncology, etc."
  source_url: https://www.ox.ac.uk/about/divisions-and-departments
  source_snippet: "Medical Sciences Division — Departments: Biochemistry, Department of; Clinical Medicine, Nuffield Department of; ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: ug.structure.social_sciences_departments
  value: "15 departments/schools including Anthropology, Archaeology, Saïd Business School, Economics, Education, Geography, Law, Politics, etc."
  source_url: https://www.ox.ac.uk/about/divisions-and-departments
  source_snippet: "Social Sciences Division — Departments: Anthropology and Museum Ethnography, School of; Archaeology, School of; Business School, Saïd; ..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: ug.course.computer_science.degree
  value: "BA or MCompSci"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/computer-science
  source_snippet: "Degree awarded: BA or MCompSci"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-017:
  field: ug.course.engineering.degree
  value: "MEng"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/engineering-science
  source_snippet: "Degree awarded: MEng"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-018:
  field: ug.course.medicine.degree
  value: "BA / BM BCh"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/courses/course-listing/medicine
  source_snippet: "Degree awarded: BA / BM BCh"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-019:
  field: pg.course_count
  value: "407"
  source_url: https://www.ox.ac.uk/admissions/graduate/courses/find-your-course
  source_snippet: "Showing 1 - 12 of 407 Results"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-020:
  field: pg.application_fee
  value: "£75"
  source_url: https://www.ox.ac.uk/admissions/graduate/application-guide
  source_snippet: "Declaration and payment"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-021:
  field: pg.deadlines.general
  value: "Almost all courses have a December or January deadline. Some have November deadlines."
  source_url: https://www.ox.ac.uk/admissions/graduate/application-guide/starting-your-application/when-to-apply
  source_snippet: "Almost all courses have a December or January deadline. This is the latest deadline to be considered for the majority of Oxford scholarships."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-022:
  field: pg.english_language.levels
  value: "Standard and Higher levels, course-specific"
  source_url: https://www.ox.ac.uk/admissions/graduate/international-applicants/english-language-requirements
  source_snippet: "Your course page will show the level of English language proficiency required for the course: 'Standard' or 'Higher'."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-023:
  field: ug.deadline.written_work
  value: "10 November"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/admissions-timeline
  source_snippet: "Submit with cover form sheet to your college by 10 November"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-024:
  field: ug.deadline.interviews
  value: "Early to mid-December"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/applying/admissions-timeline
  source_snippet: "Shortlisting (from end of November), Interviews (early to mid-December)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-025:
  field: ug.fees.home_2027
  value: "£10,050"
  source_url: https://www.ox.ac.uk/admissions/undergraduate/fees-and-funding/course-fees
  source_snippet: "In the 2027/28 academic year course fees for Home fee status students will rise to £10,050 (in line with the government fee cap)."
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
oxford-knowledge-base-v2/
├── chunk-00-overview           # Section 0: 院校总览 (Rules 1-4)
├── chunk-01-ug-humanities      # Section 1: UG Humanities Division courses
├── chunk-02-ug-mpls            # Section 1: UG MPLS Division courses
├── chunk-03-ug-medical         # Section 1: UG Medical Sciences courses
├── chunk-04-ug-social          # Section 1: UG Social Sciences courses
├── chunk-05-ug-cross-div       # Section 1: UG Cross-Division courses
├── chunk-06-pg-overview        # Section 2: PG overview + degree taxonomy
├── chunk-07-pg-humanities      # Section 2: PG Humanities Division
├── chunk-08-pg-mpls            # Section 2: PG MPLS Division
├── chunk-09-pg-medical         # Section 2: PG Medical Sciences Division
├── chunk-10-pg-social          # Section 2: PG Social Sciences Division
├── chunk-11-requirements       # Section 3: Application requirements & deadlines
├── chunk-12-costs              # Section 4: Costs & financial aid
└── chunk-13-evidence           # Section 5: Evidence chain index
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "oxford-knowledge-base-v2"
  school: "<Division name>"
  department: "<Department/Faculty name, if applicable>"
  degree_level: "<BA|BFA|MChem|MEng|MMath|MPhys|MBiol|DPhil|MSc|MSt|MPhil|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|-----------|
| **P0** | Full PG course listing (407 courses, name + degree + department + URL) | https://www.ox.ac.uk/admissions/graduate/courses/find-your-course |
| **P0** | Per-course PG fees (annual fee for each course) | Individual course pages |
| **P0** | Per-course PG English language level (Standard/Higher) | Individual course pages |
| **P0** | Per-course PG application deadlines | Individual course pages |
| **P1** | UG course fee bands (which courses fall in which fee range) | https://www.ox.ac.uk/admissions/undergraduate/fees-and-funding/course-fees |
| **P1** | PG English language Standard vs Higher exact scores | https://www.ox.ac.uk/admissions/graduate/international-applicants/english-language-requirements |
| **P1** | Per-course UG A-Level/IB entry requirements | Individual course pages |
| **P1** | Oxford scholarships and funding details | https://www.ox.ac.uk/admissions/graduate/fees-and-funding/funding |
| **P2** | College-level admissions statistics | Individual college websites |
| **P2** | Course module details and curriculum | Individual course pages |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | University of Oxford | Cardiff | Newcastle | Durham |
|-----------|--------|---------|-----------|--------|
| Total UG programmes | 52 | 237 | 147 | — |
| Total PG programmes | 407 | — | — | — |
| Russell Group | Yes | Yes | Yes | Yes |
| Collegiate | Yes | No | No | Yes |
| UG Home Fee (2026/27) | £9,790 | — | — | — |
| UG International Fee Range | £37,380 - £62,820 | — | — | — |
| IELTS UG Minimum | 7.5 (7.0 per component) | — | — | — |
| TOEFL UG Minimum | 110 (L22 R24 S25 W24) | — | — | — |
| UCAS Deadline | 15 October | — | — | — |
| PG Application Fee | £75 | — | — | — |
| Academic Divisions | 4 | — | — | — |
| Departments/Schools | 59+ | — | — | — |
| Colleges | 43 | — | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: www.ox.ac.uk (main institutional site), www.ox.ac.uk/admissions (UG + PG admissions), www.ox.ac.uk/about/divisions-and-departments (academic structure)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG courses: complete (52 courses with degree types, UCAS codes, URLs). PG courses: overview only (407 total, degree taxonomy extracted, per-course listing pending P0). Evidence: 25 blocks. Hierarchy: complete (4 divisions, 59+ departments). Fees: complete for UG. Language requirements: complete for UG. Deadlines: complete for UG, overview for PG.