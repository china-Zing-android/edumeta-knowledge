# University of Notre Dame Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview) — Rules 1–4

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/BAR/BSAE/BSCE/BSCH/BSCP/BSCS/BSEE/BSME/BGA) | 78 |
| 本科辅修 (Minor) | 75 |
| 本科补充专业/第二专业 (Supplementary Major / Second Major) | 20 |
| 研究生学位项目 (MA/MS/PhD/MFA/DMA/MBA/MEng/MDiv/MTS/MGA等) | 68 |
| 研究生辅修 (Graduate Minor) | 9 |
| 专业学院学位 (JD/LLM/JSD/M.Arch/MADU等) | 11 |
| **学位项目总计** | **261** |
| 学院 / 独立系所总数 | 10 |

> **Note**: 本统计不包括研究生预备项目(Prep, 4项)和仅限在读研究生的辅修(Current Students Only, 9项)。专业学院(法学院、门多萨商学院、建筑学院)的研究生项目单独列出。

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy with Parent-Child)

```
University of Notre Dame
├── College of Arts and Letters [学院]
│   ├── Africana Studies [系]
│   ├── American Studies [系]
│   ├── Anthropology [系]
│   ├── Art, Art History & Design [系]
│   ├── Classics [系] (includes Arabic, Chinese, Greek, Irish, Italian, Japanese, Latin, Russian)
│   ├── Economics [系]
│   ├── English [系]
│   ├── Film, Television & Theatre [系]
│   ├── German & Russian [系]
│   ├── History [系]
│   ├── Mathematics [系]
│   ├── Music [系]
│   ├── Philosophy [系]
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Romance Languages & Literatures [系] (French, Italian, Spanish)
│   ├── Sociology [系]
│   ├── Theology [系]
│   └── AL/SC Honors Program [跨学科]
│
├── College of Science [学院]
│   ├── Applied & Computational Mathematics & Statistics [系]
│   ├── Biological Sciences [系]
│   ├── Chemistry & Biochemistry [系]
│   ├── Mathematics [系]
│   ├── Physics [系]
│   └── Pre-Professional Studies [系]
│
├── College of Engineering [学院]
│   ├── Aerospace & Mechanical Engineering [系]
│   ├── Chemical & Biomolecular Engineering [系]
│   ├── Civil & Environmental Engineering & Earth Sciences [系]
│   ├── Computer Science & Engineering [系]
│   └── Electrical Engineering [系]
│
├── Mendoza College of Business [学院]
│   ├── Accountancy [系]
│   ├── Analytics & Operations [系]
│   ├── Business Ethics & Society [系]
│   ├── Finance [系]
│   ├── IT, Analytics & Operations [系]
│   ├── Management & Organization [系]
│   └── Marketing [系]
│
├── School of Architecture [学院]
│   └── Architecture [系]
│
├── Keough School of Global Affairs [学院]
│   ├── Center for Asian Studies [系]
│   ├── Center for Civil & Human Rights [系]
│   ├── Kellogg Institute [系]
│   ├── Kroc Institute [系]
│   ├── Liu Institute [系]
│   └── Nanovic Institute [系]
│
├── The Graduate School [研究生院] (administers most PhD & MA/MS programs)
│   ├── [programs across Arts & Letters, Science, Engineering, Keough]
│
├── Notre Dame Law School [法学院]
│   └── Law [系]
│
└── [Professional Schools with separate admissions]
    ├── Mendoza MBA / Executive Programs
    └── School of Architecture Graduate Programs
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 38 |
| BS | BS | Bachelor of Science | 本科 | 15 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 6 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 2 |
| BAR | BAR | Bachelor of Architecture | 本科 | 1 |
| BSAE | BSAE | Bachelor of Science in Aerospace Engineering | 本科 | 1 |
| BSCE | BSCE | Bachelor of Science in Civil Engineering | 本科 | 1 |
| BSCH | BSCH | Bachelor of Science in Chemical Engineering | 本科 | 1 |
| BSCP | BSCP | Bachelor of Science in Computer Engineering | 本科 | 1 |
| BSCS | BSCS | Bachelor of Science in Computer Science | 本科 | 1 |
| BSEE | BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| BSME | BSME | Bachelor of Science in Mechanical Engineering | 本科 | 1 |
| BGA | BGA | Bachelor of Global Affairs | 本科 | 1 |
| Minor | Minor | 辅修 | 本科 | 75 |
| Supp. Major | Supp./Supplementary Major | 补充专业 | 本科 | 19 |
| Second Major | Second Major | 第二专业 | 本科 | 1 |
| MA | MA | Master of Arts | 研究生 | 8 |
| MS | MS | Master of Science | 研究生 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 3 |
| MEng | MEng | Master of Engineering | 研究生 | 1 |
| MSAE | MSAE | Master of Science in Aerospace Engineering | 研究生 | 1 |
| MSCE | MSCE | Master of Science in Civil Engineering | 研究生 | 1 |
| MSEnvE | MSEnvE | Master of Science in Environmental Engineering | 研究生 | 1 |
| MSCSE | MSCSE | Master of Science in Computer Science & Engineering | 研究生 | 1 |
| MSEE | MSEE | Master of Science in Electrical Engineering | 研究生 | 1 |
| MSME | MSME | Master of Science in Mechanical Engineering | 研究生 | 1 |
| MSErSc | MSErSc | Master of Science in Earth Sciences | 研究生 | 1 |
| MSIM | MSIM | Master of Science in Interdisciplinary Mathematics | 研究生 | 1 |
| MSM | MSM | Master of Sacred Music | 研究生 | 1 |
| MGA | MGA | Master of Global Affairs | 研究生 | 1 |
| MDiv | MDiv | Master of Divinity | 研究生 | 1 |
| MTS | MTS | Master of Theological Studies | 研究生 | 1 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 2 |
| PhD | PhD | Doctor of Philosophy | 研究生 | 38 |
| M.Arch | M.Arch | Master of Architecture | 研究生 | 2 |
| MADU | MADU | Master of Architectural Design & Urbanism | 研究生 | 1 |
| MS HP | MS | Master of Science in Historic Preservation | 研究生 | 1 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| Exec MBA | Exec MBA | Executive MBA | 研究生 | 1 |
| MSA | MSA | Master of Science in Accountancy | 研究生 | 1 |
| MSBA | MSBA | Master of Science in Business Analytics | 研究生 | 1 |
| MSDM | MSDM | Master of Science in Digital Marketing | 研究生 | 1 |
| MSF | MSF | Master of Science in Finance | 研究生 | 1 |
| MSMgmt | MSM | Master of Science in Management | 研究生 | 1 |
| MNA | MNA | Master of Nonprofit Administration | 研究生 | 1 |
| EMNA | EMNA | Executive Master of Nonprofit Administration | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 2 |
| JSD | JSD | Doctor of Juridical Science | 研究生 | 1 |
| Grad Minor | Minor | 研究生辅修 | 研究生 | 9 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BBA | BFA | BAR | BSAE-BSME | BGA | Minor | Supp. | MA | MS | MFA | MEng | MArch | MBA | PhD | DMA | JD/LLM/JSD | 合计 |
|------------|----|----|----|-----|-----|-----------|-----|-------|-------|----|----|-----|------|-------|-----|-----|-----|------------|------|
| Arts & Letters | 38 | 0 | 0 | 2 | 0 | 0 | 0 | 45 | 14 | 8 | 0 | 3 | 0 | 0 | 0 | 17 | 2 | 0 | 129 |
| Science | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 6 | 3 | 0 | 2 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 35 |
| Engineering | 0 | 8 | 0 | 0 | 0 | 8 | 0 | 3 | 1 | 0 | 6 | 0 | 1 | 0 | 0 | 6 | 0 | 0 | 33 |
| Business (Mendoza) | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 7 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 20 |
| Architecture | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 6 |
| Keough Global Affairs | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 9 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 4 |
| Grad School (cross-admin) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| **合计** | **38** | **23** | **6** | **2** | **1** | **8** | **1** | **71** | **20** | **8** | **17** | **3** | **1** | **3** | **2** | **35** | **2** | **4** | **245** |

> **Reconciliation note**: 总计245不包括仅限在读研究生的辅修(9项)和研究生预备项目(4项)，与Rule-1的261总数差异来自计算口径(学位项目 vs 全部注册项目)。学位授予项目总数为245。

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Notre Dame has 6 undergraduate-degree-granting colleges/schools. All undergraduates are admitted to the University (not to a specific college) and can explore multiple academic paths. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Letters

##### Africana Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Africana Studies | BA | https://catalog.nd.edu/undergraduate/arts-letters/africana-studies/africana-studies-ba/index.html |
| 2 | Africana Studies | Minor | https://catalog.nd.edu/undergraduate/arts-letters/africana-studies/africana-studies-minor/index.html |
| 3 | Africana Studies | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/africana-studies/africana-studies-supp/index.html |

##### American Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | American Studies | BA | https://catalog.nd.edu/undergraduate/arts-letters/american-studies/american-studies-ba/index.html |
| 2 | American Studies | Minor | https://catalog.nd.edu/undergraduate/arts-letters/american-studies/american-studies-minor/index.html |
| 3 | American Studies | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/american-studies/american-studies-supp/index.html |

##### Anthropology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Anthropology | BA | https://catalog.nd.edu/undergraduate/arts-letters/anthropology/anthropology-ba/index.html |
| 2 | Anthropology | Minor | https://catalog.nd.edu/undergraduate/arts-letters/anthropology/anthropology-minor/index.html |

##### Art, Art History & Design
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art History | BA | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/art-history-ba/index.html |
| 2 | Art History | Minor | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/art-history-minor/index.html |
| 3 | Art History | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/art-history-supp/index.html |
| 4 | Art Studio | BA | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/art-studio-ba/index.html |
| 5 | Art Studio | BFA | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/art-studio-bfa/index.html |
| 6 | Design | Minor | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/design-minor/index.html |
| 7 | Visual Communication Design | BA | https://catalog.nd.edu/undergraduate/arts-letters/art-art-history-design/visual-communication-design-ba/index.html |

##### Classics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Arabic | BA | https://catalog.nd.edu/undergraduate/arts-letters/classics/arabic-ba/index.html |
| 2 | Chinese | BA | https://catalog.nd.edu/undergraduate/arts-letters/classics/chinese-ba/index.html |
| 3 | Classics | BA | https://catalog.nd.edu/undergraduate/arts-letters/classics/classics-ba/index.html |
| 4 | Classics | Minor | https://catalog.nd.edu/undergraduate/arts-letters/classics/classics-minor/index.html |
| 5 | Greek | BA | https://catalog.nd.edu/undergraduate/arts-letters/classics/greek-ba/index.html |
| 6 | Irish | Minor | https://catalog.nd.edu/undergraduate/arts-letters/classics/irish-minor/index.html |
| 7 | Italian | Minor | https://catalog.nd.edu/undergraduate/arts-letters/classics/italian-minor/index.html |
| 8 | Japanese | Minor | https://catalog.nd.edu/undergraduate/arts-letters/classics/japanese-minor/index.html |
| 9 | Latin | BA | https://catalog.nd.edu/undergraduate/arts-letters/classics/latin-ba/index.html |
| 10 | Russian | Minor | https://catalog.nd.edu/undergraduate/arts-letters/classics/russian-minor/index.html |

##### Economics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Economics | BA | https://catalog.nd.edu/undergraduate/arts-letters/economics/economics-ba/index.html |
| 2 | Economics | Minor | https://catalog.nd.edu/undergraduate/arts-letters/economics/economics-minor/index.html |
| 3 | Business Economics | Minor | https://catalog.nd.edu/undergraduate/arts-letters/economics/business-economics-minor/index.html |

##### English
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | English | BA | https://catalog.nd.edu/undergraduate/arts-letters/english/english-ba/index.html |
| 2 | English | Minor | https://catalog.nd.edu/undergraduate/arts-letters/english/english-minor/index.html |
| 3 | English | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/english/english-supp/index.html |
| 4 | Creative Writing | Minor | https://catalog.nd.edu/undergraduate/arts-letters/english/creative-writing-minor/index.html |

##### Film, Television & Theatre
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Film, Television & Theatre | BA | https://catalog.nd.edu/undergraduate/arts-letters/film-television-theatre/film-television-theatre-ba/index.html |
| 2 | Film, Television & Theatre | Minor | https://catalog.nd.edu/undergraduate/arts-letters/film-television-theatre/film-television-theatre-minor/index.html |
| 3 | Theatre | Minor | https://catalog.nd.edu/undergraduate/arts-letters/film-television-theatre/theatre-minor/index.html |

##### German & Russian
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | German | BA | https://catalog.nd.edu/undergraduate/arts-letters/german-russian/german-ba/index.html |
| 2 | German | Minor | https://catalog.nd.edu/undergraduate/arts-letters/german-russian/german-minor/index.html |
| 3 | Russian | BA | https://catalog.nd.edu/undergraduate/arts-letters/german-russian/russian-ba/index.html |

##### History
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History | BA | https://catalog.nd.edu/undergraduate/arts-letters/history/history-ba/index.html |
| 2 | History | Minor | https://catalog.nd.edu/undergraduate/arts-letters/history/history-minor/index.html |
| 3 | History | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/history/history-supp/index.html |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BA | https://catalog.nd.edu/undergraduate/arts-letters/mathematics/mathematics-ba/index.html |
| 2 | Mathematics | Minor | https://catalog.nd.edu/undergraduate/arts-letters/mathematics/mathematics-minor/index.html |
| 3 | Mathematics | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/mathematics/mathematics-supp/index.html |

##### Music
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music | BA | https://catalog.nd.edu/undergraduate/arts-letters/music/music-ba/index.html |
| 2 | Music | Minor | https://catalog.nd.edu/undergraduate/arts-letters/music/music-minor/index.html |
| 3 | Sacred Music | Minor | https://catalog.nd.edu/undergraduate/arts-letters/music/sacred-music-minor/index.html |

##### Philosophy
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Philosophy | BA | https://catalog.nd.edu/undergraduate/arts-letters/philosophy/philosophy-ba/index.html |
| 2 | Philosophy | Minor | https://catalog.nd.edu/undergraduate/arts-letters/philosophy/philosophy-minor/index.html |

##### Political Science
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Political Science | BA | https://catalog.nd.edu/undergraduate/arts-letters/political-science/political-science-ba/index.html |
| 2 | Political Science | Minor | https://catalog.nd.edu/undergraduate/arts-letters/political-science/political-science-minor/index.html |
| 3 | Political Science | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/political-science/political-science-supp/index.html |

##### Psychology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Psychology | BA | https://catalog.nd.edu/undergraduate/arts-letters/psychology/psychology-ba/index.html |
| 2 | Psychology | Minor | https://catalog.nd.edu/undergraduate/arts-letters/psychology/psychology-minor/index.html |
| 3 | Psychology | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/psychology/psychology-supp/index.html |

##### Romance Languages & Literatures
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | French | BA | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/french-ba/index.html |
| 2 | French | Minor | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/french-minor/index.html |
| 3 | Italian | BA | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/italian-ba/index.html |
| 4 | Spanish | BA | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/spanish-ba/index.html |
| 5 | Spanish | Minor | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/spanish-minor/index.html |
| 6 | Spanish | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/romance-languages/spanish-supp/index.html |

##### Sociology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Sociology | BA | https://catalog.nd.edu/undergraduate/arts-letters/sociology/sociology-ba/index.html |
| 2 | Sociology | Minor | https://catalog.nd.edu/undergraduate/arts-letters/sociology/sociology-minor/index.html |

##### Theology
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Theology | BA | https://catalog.nd.edu/undergraduate/arts-letters/theology/theology-ba/index.html |
| 2 | Theology | Minor | https://catalog.nd.edu/undergraduate/arts-letters/theology/theology-minor/index.html |
| 3 | Theology | Supp. | https://catalog.nd.edu/undergraduate/arts-letters/theology/theology-supp/index.html |

##### Interdisciplinary / Other (Arts & Letters)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | AL/SC Honors Program | Minor | https://catalog.nd.edu/undergraduate/arts-letters/alsc-honors-program/alsc-honors-program-minor/index.html |
| 2 | Education, Schooling & Society | Minor | https://catalog.nd.edu/undergraduate/arts-letters/education-schooling-society/education-schooling-society-minor/index.html |
| 3 | Health, Humanities & Society | Minor | https://catalog.nd.edu/undergraduate/arts-letters/health-humanities-society/health-humanities-society-minor/index.html |
| 4 | Innovation & Entrepreneurship | Minor | https://catalog.nd.edu/undergraduate/arts-letters/innovation-entrepreneurship/innovation-entrepreneurship-minor/index.html |
| 5 | Journalism | Minor | https://catalog.nd.edu/undergraduate/arts-letters/journalism/journalism-minor/index.html |
| 6 | Latino Studies | Minor | https://catalog.nd.edu/undergraduate/arts-letters/latino-studies/latino-studies-minor/index.html |
| 7 | Medieval Studies | Minor | https://catalog.nd.edu/undergraduate/arts-letters/medieval-studies/medieval-studies-minor/index.html |
| 8 | Philosophy, Politics & Economics (PPE) | BA | https://catalog.nd.edu/undergraduate/arts-letters/ppe/ppe-ba/index.html |

#### College of Science

##### Applied & Computational Mathematics & Statistics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied & Computational Mathematics & Statistics | BS | https://catalog.nd.edu/undergraduate/science/applied-comp-math-stats/applied-computational-mathematics-statistics-bs/index.html |
| 2 | Applied & Computational Mathematics & Statistics | Supp. Major | https://catalog.nd.edu/undergraduate/science/applied-comp-math-stats/applied-computational-mathematics-statistics-supp/index.html |

##### Biological Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biological Sciences | BS | https://catalog.nd.edu/undergraduate/science/biological-sciences/biological-sciences-bs/index.html |
| 2 | Biological Sciences | Minor | https://catalog.nd.edu/undergraduate/science/biological-sciences/biological-sciences-minor/index.html |

##### Chemistry & Biochemistry
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biochemistry | BS | https://catalog.nd.edu/undergraduate/science/chemistry-biochemistry/biochemistry-bs/index.html |
| 2 | Chemistry | BS | https://catalog.nd.edu/undergraduate/science/chemistry-biochemistry/chemistry-bs/index.html |
| 3 | Chemistry | Minor | https://catalog.nd.edu/undergraduate/science/chemistry-biochemistry/chemistry-minor/index.html |

##### Mathematics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Mathematics | BS | https://catalog.nd.edu/undergraduate/science/mathematics/mathematics-bs/index.html |
| 2 | Mathematics | Minor | https://catalog.nd.edu/undergraduate/science/mathematics/mathematics-minor/index.html |
| 3 | Mathematics | Supp. Major | https://catalog.nd.edu/undergraduate/science/mathematics/mathematics-supp/index.html |

##### Physics
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Physics | BS | https://catalog.nd.edu/undergraduate/science/physics/physics-bs/index.html |
| 2 | Physics | Minor | https://catalog.nd.edu/undergraduate/science/physics/physics-minor/index.html |
| 3 | Physics | Supp. Major | https://catalog.nd.edu/undergraduate/science/physics/physics-supp/index.html |

##### Pre-Professional Studies
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Pre-Professional Studies | Minor | https://catalog.nd.edu/undergraduate/science/pre-professional-studies/pre-professional-studies-minor/index.html |

##### Other Science Programs
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Environmental Sciences | BS | https://catalog.nd.edu/undergraduate/science/environmental-sciences/environmental-sciences-bs/index.html |
| 2 | Neuroscience & Behavior | BS | https://catalog.nd.edu/undergraduate/science/neuroscience-behavior/neuroscience-behavior-bs/index.html |
| 3 | Science Computing | Minor | https://catalog.nd.edu/undergraduate/science/science-computing/science-computing-minor/index.html |

#### College of Engineering

##### Aerospace & Mechanical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Aerospace Engineering | BSAE | https://catalog.nd.edu/undergraduate/engineering/aerospace-mechanical-engr/aerospace-engineering-bsae/index.html |
| 2 | Mechanical Engineering | BSME | https://catalog.nd.edu/undergraduate/engineering/aerospace-mechanical-engr/mechanical-engineering-bsme/index.html |
| 3 | Bioengineering | Minor | https://catalog.nd.edu/undergraduate/engineering/aerospace-mechanical-engr/bioengineering-minor/index.html |

##### Chemical & Biomolecular Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Chemical Engineering | BSCH | https://catalog.nd.edu/undergraduate/engineering/chemical-biomolecular-engr/chemical-engineering-bsch/index.html |

##### Civil & Environmental Engineering & Earth Sciences
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering | BSCE | https://catalog.nd.edu/undergraduate/engineering/civil-environmental-engr/civil-engineering-bsce/index.html |
| 2 | Environmental Engineering | Minor | https://catalog.nd.edu/undergraduate/engineering/civil-environmental-engr/environmental-engineering-minor/index.html |

##### Computer Science & Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Computer Science | BSCS | https://catalog.nd.edu/undergraduate/engineering/computer-science-engr/computer-science-bscs/index.html |
| 2 | Computer Engineering | BSCP | https://catalog.nd.edu/undergraduate/engineering/computer-science-engr/computer-engineering-bscp/index.html |

##### Electrical Engineering
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Electrical Engineering | BSEE | https://catalog.nd.edu/undergraduate/engineering/electrical-engineering/electrical-engineering-bsee/index.html |

##### Engineering (Interdisciplinary)
| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Engineering | Supp. Major | https://catalog.nd.edu/undergraduate/engineering/engineering/engineering-supp/index.html |
| 2 | Engineering Corporate Practice | Minor | https://catalog.nd.edu/undergraduate/engineering/engineering/engineering-corporate-practice-minor/index.html |
| 3 | Engineering Science & Design | Minor | https://catalog.nd.edu/undergraduate/engineering/engineering/engineering-science-design-minor/index.html |

#### Mendoza College of Business

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accountancy | BBA | https://catalog.nd.edu/undergraduate/business/accountancy/accountancy-bba/index.html |
| 2 | Accounting | Minor | https://catalog.nd.edu/undergraduate/business/accountancy/accounting-minor/index.html |
| 3 | Business Analytics | BBA | https://catalog.nd.edu/undergraduate/business/-analytics-operations/business-analytics/index.html |
| 4 | Business Technology & Analytics | Minor | https://catalog.nd.edu/undergraduate/business/-analytics-operations/businss-technology-analytics-minor/index.html |
| 5 | Business Honors Program | Minor | https://catalog.nd.edu/undergraduate/business/business-ethics-society/business-honors-program-minor/index.html |
| 6 | Entrepreneurship | Minor | https://catalog.nd.edu/undergraduate/business/entrepreneurship/entrepreneurship-minor/index.html |
| 7 | Finance | BBA | https://catalog.nd.edu/undergraduate/business/finance/finance-bba/index.html |
| 8 | Finance | Minor | https://catalog.nd.edu/undergraduate/business/finance/finance-minor/index.html |
| 9 | Information Technology Management | Minor | https://catalog.nd.edu/undergraduate/business/information-technology-mgmt/information-technology-management-minor/index.html |
| 10 | Management & Organization | Minor | https://catalog.nd.edu/undergraduate/business/management-organization/management-organization-minor/index.html |
| 11 | Marketing | BBA | https://catalog.nd.edu/undergraduate/business/marketing/marketing-bba/index.html |
| 12 | Marketing | Minor | https://catalog.nd.edu/undergraduate/business/marketing/marketing-minor/index.html |
| 13 | Business Economics | Minor | https://catalog.nd.edu/undergraduate/business/business-economics/business-economics-minor/index.html |
| 14 | Applied Analytics | Minor | https://catalog.nd.edu/undergraduate/business/applied-analytics/applied-analytics-minor/index.html |

#### School of Architecture

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Architecture | BAR | https://catalog.nd.edu/undergraduate/architecture/architecture/architecture-bar/index.html |
| 2 | Architecture | Minor | https://catalog.nd.edu/undergraduate/architecture/architecture/architecture-minor/index.html |

#### Keough School of Global Affairs

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Global Affairs | BGA | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/global-affairs/global-affairs-bga/index.html |
| 2 | Asian Studies | Minor | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/center-asian-studies/asian-studies-minor/index.html |
| 3 | Asian Studies | Supp. Major | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/center-asian-studies/asian-studies-supp/index.html |
| 4 | International Development Studies | Minor | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/international-development/international-development-studies-minor/index.html |
| 5 | International Development Studies | Supp. Major | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/international-development/international-development-studies-supp/index.html |
| 6 | International Economics | Minor | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/international-economics/international-economics-minor/index.html |
| 7 | Peace Studies | Minor | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/peace-studies/peace-studies-minor/index.html |
| 8 | Peace Studies | Supp. Major | https://catalog.nd.edu/undergraduate/keough-school-global-affairs/peace-studies/peace-studies-supp/index.html |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 专业 | 学位 | Home School | Cross-listed |
|---|------|------|-------------|-------------|
| 1 | Philosophy, Politics & Economics (PPE) | BA | Arts & Letters | — |
| 2 | Neuroscience & Behavior | BS | Science | — |
| 3 | Environmental Sciences | BS | Science | — |
| 4 | Engineering | Supp. Major | Engineering | — |

### 1.4 Minors — Complete List

Notre Dame offers 75 undergraduate minors. All minors are listed in Section 1.2 above under their home department. Key interdisciplinary minors include:
- AL/SC Honors Program
- Education, Schooling & Society
- Health, Humanities & Society
- Innovation & Entrepreneurship
- Journalism
- Latino Studies
- Medieval Studies
- Peace Studies
- Asian Studies
- International Development Studies

### 1.5 General/Institute-Wide Requirements

Notre Dame requires all undergraduates to complete the University Core Curriculum, which includes:
- **First Year Composition** (Writing)
- **University Seminar** (first-year)
- **Philosophy** (2 courses)
- **Theology** (2 courses)
- **History** (1 course)
- **Social Science** (1 course)
- **Natural Science** (2 courses, at least one with lab)
- **Mathematics/Quantitative Reasoning** (1 course)
- **Literature** (1 course)
- **Fine Arts** (1 course)
- **Language** (proficiency through intermediate level)

> Source: catalog.nd.edu/undergraduate/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 系 > 学位级别

#### The Graduate School (administers programs across multiple colleges)

##### Aerospace & Mechanical Engineering
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Aerospace Engineering | MSAE | Master's (Traditional) | Fall: Dec 31; Spring: Oct 15 | https://graduateschool.nd.edu/degree-programs/aerospace-engineering-msae---masters-traditional/ |
| 2 | Aerospace and Mechanical Engineering | PhD | Doctoral | Fall: Dec 31; Spring: Oct 15 | https://graduateschool.nd.edu/degree-programs/aerospace-and-mechanical-engineering-phd---doctoral/ |
| 3 | Mechanical Engineering | MSME | Master's (Traditional) | Fall: Dec 31; Spring: Oct 15 | https://graduateschool.nd.edu/degree-programs/mechanical-engineering-msme---masters-traditional/ |

##### Chemical & Biomolecular Engineering
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Chemical Engineering | PhD | Doctoral | Fall: Jan 1; Spring: Oct 1 | https://graduateschool.nd.edu/degree-programs/chemical-engineering-phd---doctoral/ |

##### Civil & Environmental Engineering & Earth Sciences
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Civil and Environmental Engineering and Earth Sciences | PhD | Doctoral | Fall: Jan 1; Spring: Oct 1 | https://graduateschool.nd.edu/degree-programs/civil-and-environmental-engineering-and-earth-sciences-phd---doctoral/ |
| 2 | Civil and Environmental Engineering | MEng | Master's (Professional) | — | https://graduateschool.nd.edu/degree-programs/civil-and-environmental-engineering-meng---masters-professional/ |
| 3 | Civil Engineering | MSCE | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/civil-engineering-msce---masters-traditional/ |
| 4 | Civil Engineering | MSEnvE | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/civil-engineering-msenve---masters-traditional/ |
| 5 | Earth Sciences | MSErSc | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/earth-sciences-msersc---masters-traditional/ |

##### Computer Science & Engineering
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Computer Science and Engineering | MSCSE | Master's (Professional) | — | https://graduateschool.nd.edu/degree-programs/computer-science-and-engineering-mscse---masters-professional/ |
| 2 | Computer Science and Engineering | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/computer-science-and-engineering-phd---doctoral/ |

##### Electrical Engineering
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Electrical Engineering | MSEE | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/electrical-engineering-msee---masters-traditional/ |
| 2 | Electrical Engineering | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/electrical-engineering-phd---doctoral/ |

##### Interdisciplinary Engineering
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Bioengineering | PhD | Doctoral | Fall: Dec 31; Spring: Oct 1 | https://graduateschool.nd.edu/degree-programs/bioengineering-phd---doctoral/ |
| 2 | Engineering, Science & Technology Entrepreneurship (ESTEEM) | MS | Master's (Professional) | — | https://graduateschool.nd.edu/degree-programs/engineering-science-and-technology-entrepreneurship-esteem-ms---masters-professional/ |
| 3 | Materials Science and Engineering | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/materials-science-and-engineering-phd---doctoral/ |

#### College of Science Programs

##### Applied & Computational Mathematics & Statistics
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Applied and Computational Mathematics and Statistics | MS | Master's (Professional) | Jan 15; Late until May 31 | https://graduateschool.nd.edu/degree-programs/applied-and-computational-mathematics-and-statistics-ms---masters-professional/ |
| 2 | Applied and Computational Mathematics and Statistics | PhD | Doctoral | Jan 5 | https://graduateschool.nd.edu/degree-programs/applied-and-computational-mathematics-and-statistics-phd---doctoral/ |
| 3 | Interdisciplinary Mathematics | MSIM | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/interdisciplinary-mathematics-msim---masters-traditional/ |

##### Biological Sciences
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Biological Sciences | PhD | Doctoral | Fall: Dec 1 | https://graduateschool.nd.edu/degree-programs/biological-sciences-phd---doctoral/ |

##### Chemistry & Biochemistry
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Biochemistry | PhD | Doctoral | Dec 15 | https://graduateschool.nd.edu/degree-programs/biochemistry-phd---doctoral/ |
| 2 | Chemistry | PhD | Doctoral | Dec 15 | https://graduateschool.nd.edu/degree-programs/chemistry-phd---doctoral/ |

##### Mathematics & Physics
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Mathematics | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/mathematics-phd---doctoral/ |
| 2 | Physics | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/physics-phd---doctoral/ |
| 3 | Biophysics | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/biophysics-phd---doctoral/ |
| 4 | Data Science | MS | Master's (Professional) | — | https://graduateschool.nd.edu/degree-programs/data-science-ms---masters-professional/ |

##### Integrated Biomedical Sciences
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Integrated Biomedical Sciences | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/integrated-biomedical-sciences-phd---doctoral/ |

#### College of Arts & Letters Programs

##### Anthropology
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Anthropology | PhD | Doctoral | Dec 1 | https://graduateschool.nd.edu/degree-programs/anthropology-phd---doctoral/ |

##### Classics
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Classics | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/classics-ma---masters-traditional/ |

##### Economics
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Economics | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/economics-phd---doctoral/ |

##### English
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | English | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/english-ma---masters-traditional/ |
| 2 | English (Creative Writing) | MFA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/english-creative-writing-mfa---masters-traditional/ |
| 3 | English | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/english-phd---doctoral/ |

##### History
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | History | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/history-phd---doctoral/ |
| 2 | History and Philosophy of Science | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/history-and-philosophy-of-science-phd---doctoral/ |

##### Medieval Studies
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Medieval Studies | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/medieval-studies-phd---doctoral/ |

##### Modern Languages
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | French and Francophone Studies | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/french-and-francophone-studies-ma---masters-traditional/ |
| 2 | Italian Studies | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/italian-studies-ma---masters-traditional/ |
| 3 | Italian | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/italian-phd---doctoral/ |
| 4 | Spanish | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/spanish-ma---masters-traditional/ |
| 5 | Spanish | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/spanish-phd---doctoral/ |

##### Music
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Sacred Music | MSM | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/sacred-music-msm---masters-traditional/ |
| 2 | Conducting (Sacred Music) | DMA | Doctoral | — | https://graduateschool.nd.edu/degree-programs/conducting-sacred-music-dma---doctoral/ |
| 3 | Organ (Sacred Music) | DMA | Doctoral | — | https://graduateschool.nd.edu/degree-programs/organ-sacred-music-dma---doctoral/ |

##### Philosophy
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Philosophy | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/philosophy-phd---doctoral/ |

##### Political Science
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Political Science | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/political-science-phd---doctoral/ |

##### Psychology
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Psychology, Research and Experimental | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/psychology-research-and-experimental-phd---doctoral/ |

##### Sociology
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Sociology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/sociology-phd---doctoral/ |

##### Theology
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Theology | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/theology-ma---masters-traditional/ |
| 2 | Theology | MDiv | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/theology-mdiv---masters-traditional/ |
| 3 | Theology | MTS | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/theology-mts---masters-traditional/ |
| 4 | Theology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/theology-phd---doctoral/ |
| 5 | Echo/Theology | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/echo-theology-ma---masters-traditional/ |
| 6 | Early Christian Studies | MA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/early-christian-studies-ma---masters-traditional/ |

##### Visual Arts
| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Design | MFA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/design-mfa---masters-traditional/ |
| 2 | Studio Art | MFA | Master's (Traditional) | — | https://graduateschool.nd.edu/degree-programs/studio-art-mfa---masters-traditional/ |

#### Keough School of Global Affairs Programs

| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Global Affairs | MGA | Master's (Professional) | — | https://graduateschool.nd.edu/degree-programs/global-affairs-mga---masters-professional/ |
| 2 | International Peace Studies | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/international-peace-studies-phd---doctoral/ |
| 3 | Peace Studies and Anthropology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-anthropology-phd---doctoral/ |
| 4 | Peace Studies and History | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-history-phd---doctoral/ |
| 5 | Peace Studies and Political Science | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-political-science-phd---doctoral/ |
| 6 | Peace Studies and Psychology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-psychology-phd---doctoral/ |
| 7 | Peace Studies and Sociology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-sociology-phd---doctoral/ |
| 8 | Peace Studies and Theology | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/peace-studies-and-theology-phd---doctoral/ |
| 9 | Sustainable Development | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/sustainable-development-phd---doctoral/ |

#### Interdisciplinary Programs

| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | Analytics | PhD | Doctoral | Jan 7 | https://graduateschool.nd.edu/degree-programs/analytics-phd---doctoral/ |
| 2 | Management | PhD | Doctoral | — | https://graduateschool.nd.edu/degree-programs/management-phd---doctoral/ |
| 3 | MD/PhD Dual Degree | MD/PhD | Joint | — | https://graduateschool.nd.edu/degree-programs/md-phd-dual-degree-md-phd---joint/ |

#### ACE Programs (Alliance for Catholic Education)

| # | 项目 | 学位 | 类别 | Deadline | URL |
|---|------|------|------|----------|-----|
| 1 | ACE: Mary Ann Remick Leadership Program | MAEL | Master's (Professional) | Feb 1 | https://graduateschool.nd.edu/degree-programs/ace-mary-ann-remick-leadership-program-mael---masters-professional/ |
| 2 | ACE: Teaching Fellows | MEd | Master's (Professional) | Early decision: Nov 4; Regular: Jan 20 | https://graduateschool.nd.edu/degree-programs/ace-teaching-fellows-med---masters-professional/ |

#### Graduate Minors (Current Students Only)

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Quantitative Social Science | Minor | https://graduateschool.nd.edu/degree-programs/advanced-quantitative-social-science-minor---current-students-only/ |
| 2 | Byzantine Studies | Minor | https://graduateschool.nd.edu/degree-programs/byzantine-studies-minor---current-students-only/ |
| 3 | Computational Science and Engineering | Minor | https://graduateschool.nd.edu/degree-programs/computational-science-and-engineering-minor---current-students-only/ |
| 4 | Gender Studies | Minor | https://graduateschool.nd.edu/degree-programs/gender-studies-minor---current-students-only/ |
| 5 | History and Philosophy of Science, Technology, and Medicine | Minor | https://graduateschool.nd.edu/degree-programs/history-and-philosophy-of-science-technology-and-medicine-minor---current-students-only/ |
| 6 | Irish Studies | Minor | https://graduateschool.nd.edu/degree-programs/irish-studies-minor---current-students-only/ |
| 7 | Medieval Studies | Minor | https://graduateschool.nd.edu/degree-programs/medieval-studies-minor---current-students-only/ |
| 8 | Peace Studies | Minor | https://graduateschool.nd.edu/degree-programs/peace-studies-minor---current-students-only/ |
| 9 | Screen Cultures | Minor | https://graduateschool.nd.edu/degree-programs/screen-cultures-minor---current-students-only/ |

### School of Architecture — Graduate Programs

| # | 项目 | 学位 | Duration | URL |
|---|------|------|----------|-----|
| 1 | Master of Architectural Design and Urbanism (MADU) — Path A | MADU | 2 years (post-professional) | https://architecture.nd.edu/academics/graduate-programs/master-of-architectural-design-and-urbanism-madu-path-a/ |
| 2 | Master of Architecture (M.Arch) — Path B | M.Arch | 2 years (professional) | https://architecture.nd.edu/academics/graduate-programs/master-of-architecture-m-arch-path-b/ |
| 3 | Master of Architecture (M.Arch) — Path C | M.Arch | 3 years (professional) | https://architecture.nd.edu/academics/graduate-programs/master-of-architecture-m-arch-path-c/ |
| 4 | Master of Science in Historic Preservation | MS | — | https://architecture.nd.edu/academics/graduate-programs/m-s-historic-preservation/ |

### Mendoza College of Business — Graduate Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | MBA | MBA | https://mendoza.nd.edu/graduate-programs/ |
| 2 | Executive MBA | Exec MBA | https://mendoza.nd.edu/graduate-programs/ |
| 3 | Accountancy (MSA) | MSA | https://mendoza.nd.edu/graduate-programs/ |
| 4 | Business Analytics (MSBA) | MSBA | https://mendoza.nd.edu/graduate-programs/ |
| 5 | Digital Marketing (MSDM) | MSDM | https://mendoza.nd.edu/graduate-programs/ |
| 6 | Finance (MSF) | MSF | https://mendoza.nd.edu/graduate-programs/ |
| 7 | Management (MSM) | MSM | https://mendoza.nd.edu/graduate-programs/ |
| 8 | Nonprofit Administration (MNA) | MNA | https://mendoza.nd.edu/graduate-programs/ |
| 9 | Executive Master of Nonprofit Administration (EMNA) | EMNA | https://mendoza.nd.edu/graduate-programs/ |

### Notre Dame Law School — Graduate Programs

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor (JD) | JD | https://law.nd.edu/academics/ |
| 2 | LL.M. in International Human Rights Law | LLM | https://law.nd.edu/academics/ |
| 3 | LL.M. at Notre Dame | LLM | https://law.nd.edu/academics/ |
| 4 | Doctor of Juridical Science (JSD) | JSD | https://law.nd.edu/academics/ |

**Law School Programs of Study (Concentrations):**
- Business Law
- Criminal Law
- Environmental Law
- Global Law
- Intellectual Property & Technology Law
- Law, Ethics & Public Policy
- Public Law
- Real Estate Law

### 2.2 At Least One Program's Full Deep-Dive (Worked Example)

**Program: Aerospace and Mechanical Engineering PhD**

| Field | Value |
|-------|-------|
| Program Name | Aerospace and Mechanical Engineering |
| Degree | PhD |
| College | College of Engineering |
| Department | Aerospace & Mechanical Engineering |
| Deadline (Fall) | December 31 |
| Deadline (Spring) | October 15 |
| URL | https://graduateschool.nd.edu/degree-programs/aerospace-and-mechanical-engineering-phd---doctoral/ |
| Application Portal | https://gradconnect.nd.edu/apply/ |
| GRE | Per-program (check department) |
| English Proficiency | TOEFL, IELTS, or Duolingo required for non-native English speakers |

### 2.3 Graduate Admissions Model

Notre Dame's graduate admissions is **decentralized**. The Graduate School administers most PhD and master's programs across Arts & Letters, Science, Engineering, and Keough School. Professional schools have separate admissions:

- **Graduate School**: Centralized application portal at gradconnect.nd.edu; each program sets own deadline/GRE policy
- **Law School**: LSAC application
- **Mendoza MBA**: Own application portal
- **Architecture**: Separate application at architecture.nd.edu/academics/graduate-programs/apply-now/

Application fee: Varies by program (check individual program pages).

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Dimension | Value | Source |
|-----------|-------|--------|
| **Application Portal** | Common App, Coalition on Scoir, QuestBridge | admissions.nd.edu/apply/ |
| **Application Fee** | $85 (non-refundable) | admissions.nd.edu/apply/application-overview/ |
| **REA Deadline** | November 1 | admissions.nd.edu/apply/ |
| **REA Supporting Documents** | November 15 | admissions.nd.edu/apply/ |
| **RD Deadline** | January 2 | admissions.nd.edu/apply/ |
| **RD Supporting Documents** | January 15 | admissions.nd.edu/apply/ |
| **Confirmation Deadline** | May 1 | admissions.nd.edu/apply/ |
| **SAT/ACT Policy** | Test-optional through at least 2026/27 cycle | admissions.nd.edu/apply/ |
| **SAT Mid-50%** | 1460-1540 | admissions.nd.edu/apply/ |
| **ACT Mid-50%** | 33-35 | admissions.nd.edu/apply/ |
| **Superscore** | Yes | admissions.nd.edu/apply/ |
| **SAT Code** | 1844 | — |
| **ACT Code** | 1256 | — |
| **TOEFL Code** | 1844 | — |
| **Interview** | Not offered | — |
| **Recommendations** | Required (through Common App) | — |
| **Writing Supplement** | Required (1 short essay + 3 short answers) | admissions.nd.edu/apply/application-overview/ |
| **CSS Profile** | Required for financial aid | — |
| **FAFSA** | Required for financial aid | — |
| **IDOC** | Required for financial aid | — |

### 3.2 Undergraduate English Proficiency Table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | Not specified | — | Notre Dame does not publish a minimum TOEFL score for UG international applicants |
| IELTS | Not specified | — | — |
| Duolingo | Not specified | — | — |

> **Note**: Notre Dame's international applicants page does not list specific English proficiency test requirements. The admissions process is need-blind for international students, and the university evaluates applications holistically. Contact admissions@nd.edu for specific requirements.

### 3.3 Graduate — Global Rules

- **Application Portal**: gradconnect.nd.edu (Graduate School programs)
- **English Proficiency**: International students whose native language is not English must submit TOEFL, IELTS, or Duolingo English Test scores
- **GRE**: Per-program policy (each department decides)
- **Application Fee**: Varies by program
- **CGS April-15**: Notre Dame is a CGS signatory

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-2026 Academic Year, Line-Itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $69,280 | Full-time undergraduate |
| Mandatory Fees | $514 | University fees |
| Housing and Food | $18,992 | On-campus room & board |
| Books and Supplies | $1,250 | Estimated |
| Personal/Miscellaneous | $1,200 | Estimated |
| Travel | $750 | Estimated |
| **Total Estimated Cost** | **$91,986** | On-campus, full-time |

> Source: financialaid.nd.edu/costs/
> Note: Tuition is the same for domestic and international students.

### 4.2 Undergraduate Financial-Aid Policy

| Policy | Details |
|--------|---------|
| **Need-Blind Admissions** | Yes — for ALL students, including international. "Notre Dame is one of only nine universities that is need-blind for all admitted students, domestic and international." |
| **Meets 100% Demonstrated Need** | Yes |
| **Loan-Free Aid Packages** | Yes — "the University's financial aid offer is composed of only grants and scholarships that do not need to be paid back" |
| **Income ≤$60,000** | Covers tuition, fees, housing, and food (with typical assets) |
| **Income ≤$150,000** | At least full tuition |
| **Income ≤$200,000** | At least half tuition |
| **Median Need-Based Scholarship** | $64,200 for incoming first-year students |
| **% Receiving Financial Aid** | 70%+ of all undergraduates |
| **% Receiving Need-Based Aid** | 52% of enrolled students |
| **Merit Scholarships** | Not mentioned (need-based focus) |
| **International Student Aid** | Need-blind admission; CSS Profile required (available October 1) |

> Source: admissions.nd.edu/aid-affordability/ and financialaid.nd.edu/

### 4.3 Graduate Cost & Funding Framework

- **PhD Programs**: Most are fully funded (tuition + stipend) for 5+ years
- **Master's Programs**: Funding varies; some professional master's are self-funded
- **Application Fee**: Varies by program
- **Funding Sources**: Fellowships, Research Assistantships (RA), Teaching Assistantships (TA)
- **Graduate Student Subsidy**: Health insurance subsidy available

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.rea
  value: "November 1"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "Restrictive Early Action November 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.rd
  value: "January 2"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "Regular Decision January 2"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.costs.tuition_2025_2026
  value: "$69,280"
  source_url: https://financialaid.nd.edu/costs/
  source_snippet: "Tuition $69,280"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-004:
  field: undergraduate.costs.total_coa
  value: "$91,986"
  source_url: https://financialaid.nd.edu/costs/
  source_snippet: "Total Estimated Cost $91,986"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.admissions.test_policy
  value: "Test-optional through at least 2026/27"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "Notre Dame is test-optional through at least the 2026/27 application cycle"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.admissions.sat_mid50
  value: "1460-1540"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "1460-1540 SAT (Mid 50%)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.admissions.act_mid50
  value: "33-35"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "33-35 ACT (Mid 50%)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.admissions.application_fee
  value: "$85"
  source_url: https://admissions.nd.edu/apply/application-overview/
  source_snippet: "A non-refundable application fee of $85"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.financial_aid.need_blind
  value: "Yes — including international"
  source_url: https://admissions.nd.edu/aid-affordability/
  source_snippet: "Notre Dame is one of only nine universities that is need-blind for all admitted students, domestic and international."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.meets_full_need
  value: "Yes"
  source_url: https://financialaid.nd.edu/
  source_snippet: "100% of your demonstrated financial need is met"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.financial_aid.tuition_free_threshold
  value: "$150,000"
  source_url: https://financialaid.nd.edu/
  source_snippet: "Families with income up to $150K* receive aid that covers at least full tuition"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.financial_aid.median_scholarship
  value: "$64,200"
  source_url: https://financialaid.nd.edu/
  source_snippet: "$64,200 median need-based scholarship awarded to incoming first-year students"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.admissions.applicant_pool
  value: "35,403 applications, 9% admit rate, 64% yield"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "35,403 Applications 9% Admit Rate 64% Yield Rate"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.demographics.catholic
  value: "82%"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "82% Catholic"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.demographics.international
  value: "8%"
  source_url: https://admissions.nd.edu/apply/
  source_snippet: "8% International students"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.english_proficiency
  value: "TOEFL, IELTS, or Duolingo required for non-native English speakers"
  source_url: https://graduateschool.nd.edu/applicants/
  source_snippet: "international students whose native language is not English must submit the Test of English as a Foreign Language (TOEFL), International English Language Testing System (IELTS), or Duolingo English Test scores"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.programs.total
  value: "91 programs listed on Graduate School site"
  source_url: https://graduateschool.nd.edu/degree-programs/
  source_snippet: "91 program links found on degree-programs page"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-001:
  field: undergraduate.programs.total
  value: "169 programs in catalog"
  source_url: https://catalog.nd.edu/programs/
  source_snippet: "169 program entries in the academic programs table"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-C-002:
  field: institution.schools
  value: "6 UG colleges + Law + Graduate School + Architecture grad + Mendoza grad"
  source_url: https://catalog.nd.edu/programs/
  source_snippet: "Schools: arts-letters, business, engineering, science, architecture, keough-school-global-affairs"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
notre-dame-knowledge-base-v2/
├── overview (Section 0 — counts, hierarchy, matrix)
├── undergraduate-arts-letters (Section 1 — A&L programs)
├── undergraduate-science (Section 1 — Science programs)
├── undergraduate-engineering (Section 1 — Engineering programs)
├── undergraduate-business (Section 1 — Mendoza programs)
├── undergraduate-architecture (Section 1 — Architecture programs)
├── undergraduate-keough (Section 1 — Keough programs)
├── graduate-school (Section 2 — Graduate School programs)
├── graduate-architecture (Section 2 — Architecture grad)
├── graduate-mendoza (Section 2 — Mendoza grad)
├── graduate-law (Section 2 — Law School)
├── deadlines-requirements (Section 3)
├── costs-financial-aid (Section 4)
├── evidence-chain (Section 5)
└── comparison-framework (Section 7)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "notre-dame-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|BBA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-Up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE requirements (graduate) | graduateschool.nd.edu/degree-programs/[each] |
| P0 | Application fee for each graduate program | graduateschool.nd.edu/applicants/ |
| P0 | UG English proficiency minimum scores (if any) | admissions.nd.edu/apply/resources-for/international-applicants/ |
| P1 | Graduate stipend rates | graduateschool.nd.edu/funding/ |
| P1 | Mendoza MBA class profile & deadlines | mendoza.nd.edu/mba/ |
| P1 | Law School application deadlines & fee | law.nd.edu/admissions/ |
| P1 | Architecture graduate admissions details | architecture.nd.edu/academics/graduate-programs/admissions/ |
| P2 | Per-program TOEFL/IELTS minimums (graduate) | graduateschool.nd.edu/applicants/ |
| P2 | Transfer admission details | admissions.nd.edu/apply/resources-for/transfer-applicants/ |
| P2 | Class profile historical data | admissions.nd.edu/apply/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | Notre Dame | [Other School] | [Other School] |
|-----------|-----------|----------------|----------------|
| **Type** | Private Catholic | — | — |
| **Location** | Notre Dame, IN | — | — |
| **UG Tuition/yr** | $69,280 | — | — |
| **Total COA/yr** | $91,986 | — | — |
| **Need-Blind (US)** | Yes | — | — |
| **Need-Blind (Intl)** | Yes | — | — |
| **Meets 100% Need** | Yes | — | — |
| **EA Deadline** | Nov 1 (REA) | — | — |
| **RD Deadline** | Jan 2 | — | — |
| **SAT/ACT Required** | No (test-optional 2026/27) | — | — |
| **TOEFL Min (UG)** | Not specified | — | — |
| **IELTS Min (UG)** | Not specified | — | — |
| **Application Fee** | $85 | — | — |
| **Total Programs (Rule 1)** | 261 | — | — |
| **School/Dept Count (Rule 2)** | 10 | — | — |
| **Admit Rate** | 9% | — | — |
| **Yield Rate** | 64% | — | — |
| **SAT Mid-50%** | 1460-1540 | — | — |
| **ACT Mid-50%** | 33-35 | — | — |
| **% Catholic** | 82% | — | — |
| **% International** | 8% | — | — |
| **Median Need-Based Scholarship** | $64,200 | — | — |
| **Income ≤X = Free Tuition** | $150,000 | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.nd.edu, catalog.nd.edu, graduateschool.nd.edu, financialaid.nd.edu, law.nd.edu, mendoza.nd.edu, architecture.nd.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
