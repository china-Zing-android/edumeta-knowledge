# Massachusetts Institute of Technology (MIT) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless) — snapshotText + JS DOM extraction
> **Target knowledge base**: WeKnora
> **Granularity**: 学院 (school) → 系 (department) → 学位级别 (degree level) → 专业/项目 (program)
> **Document version**: v2.0 (deep)
> **Source domains**: mitadmissions.org (UG) · oge.mit.edu (graduate) · sfs.mit.edu (finances) · catalog.mit.edu (programs/majors)

---

## The five structural rules (enforced)

1. **专业总数** — exact count of every UG major, minor, and grad degree-offering.
2. **学院/系明细 + 父子层级** — every school and department with parent→child tree.
3. **学历级别明细** — every degree level MIT awards (SB, SM, MEng, MArch, MBA, MBAn, MFin, MSMS, MCP, MASc, PhD, ScD, Minor).
4. **分布矩阵** — 学院 × 学位级别 cross-tab.
5. **全量专业按 学院 → 系 → 学位级别 分组** — every program, no summarizing.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

Counting unit = **degree-granting offering** (each degree a department confers is one row; a department offering SM + PhD + ScD contributes 3 rows). This is the most granular, comparable unit.

| 维度 | 数量 |
|------|------|
| 本科学位专业 (SB) | 55 |
| 本科辅修 (Minor) | 17 |
| 研究生学位项目 (OGE 独立招生项目) | 47 |
| 研究生学位授予细项 (degree offerings, 含同一项目的多学位) | 85 |
| **学位细项总计 (UG majors + minors + grad degree offerings)** | **157** |
| 学院 (School/College) 总数 | 6 |
| 系 / 独立项目组 总数 | ~33 |

> Reconciliation gate (offering basis): rule-1 total = **157** = rule-3 degree-level sum = rule-4 matrix cell-sum = rule-5 grouped-table row count. Verified by Python computation (see Section 5, evidence E-U-001). On the coarser "program-listing" basis (treating each OGE entry as one program regardless of how many degrees it confers): 55 + 17 + 47 = **119**.

### 0.2 学院 / 系层级结构 (Rule 2)

```
MIT
├── School of Engineering                                              [学院]
│   ├── Aeronautics and Astronautics (Course 16)                       [系]
│   ├── Biological Engineering (Course 20)                             [系]
│   ├── Chemical Engineering (Course 10)                               [系]
│   ├── Civil and Environmental Engineering (Course 1)                 [系]
│   ├── Electrical Eng. and Computer Science (Course 6)                [系]  ⚠ shared with Schwarzman College of Computing
│   ├── Health Sciences and Technology (Harvard-MIT, HST)              [系]
│   ├── Materials Science and Engineering (Course 3)                   [系]
│   ├── Mechanical Engineering (Course 2)                              [系]
│   ├── Nuclear Science and Engineering (Course 22)                    [系]
│   └── Institute for Data, Systems, and Society (IDSS)                [系]  ⚠ shared with Schwarzman
├── School of Science                                                  [学院]
│   ├── Biology (Course 7)                                             [系]
│   ├── Brain and Cognitive Sciences (Course 9)                        [系]
│   ├── Chemistry (Course 5)                                           [系]
│   ├── Earth, Atmospheric and Planetary Sciences (Course 12)          [系]
│   ├── Mathematics (Course 18)                                        [系]
│   └── Physics (Course 8)                                             [系]
├── School of Architecture and Planning                                [学院]
│   ├── Architecture (Course 4)                                        [系]
│   ├── Media Arts and Sciences (Media Lab)                            [系]
│   ├── Center for Real Estate                                         [系]
│   └── Urban Studies and Planning (Course 11)                         [系]
├── School of Humanities, Arts, and Social Sciences (SHASS)            [学院]
│   ├── Anthropology (Course 21A)                                      [系]
│   ├── Comparative Media Studies / Writing (Course CMS, 21W)          [系]
│   ├── Economics (Course 14)                                          [系]
│   ├── Global Studies and Languages (Course 21G)                      [系]
│   ├── History (Course 21H)                                           [系]
│   ├── History, Anthropology, and STS (HASTS)                         [系]
│   ├── Humanities (Dean's Office; Course 21, 21E, 21S)                [系]
│   ├── Linguistics and Philosophy (Course 24)                         [系]
│   ├── Literature (Course 21L)                                        [系]
│   ├── Music and Theater Arts (Course 21M, 21T)                       [系]
│   ├── Political Science (Course 17)                                  [系]
│   └── Science, Technology, and Society (STS)                         [系]
├── MIT Sloan School of Management                                     [学院]
│   └── MIT Sloan (UG Course 15; MBA / MBAn / MFin / MSMS / PhD / EMBA / Fellows MBA)  [系]
└── Schwarzman College of Computing                                    [学院]  (founded 2019; cross-cutting)
    ├── Electrical Eng. and Computer Science (Course 6)                [系]  ⚠ shared with Engineering
    ├── Institute for Data, Systems, and Society (IDSS)                [系]  ⚠ shared with Engineering
    ├── Operations Research Center                                     [系]
    ├── Center for Transportation & Logistics (SCM, Transportation)    [系]
    ├── System Design and Management (SDM)                             [系]
    └── Technology and Policy Program (TPP)                            [系]
```

**Shared / interdisciplinary departments**: EECS (Course 6) and IDSS sit administratively in both the School of Engineering and Schwarzman College of Computing. Several UG majors are joint across two schools (Course 6-9, 6-7, 6-14, 11-6, 1-12, 21E, 21S) — listed under administrative home, cross-listing noted.

### 0.3 学历级别明细 (Rule 3)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| SB | Bachelor of Science | 本科 | 55 |
| Minor | 辅修 (本科学位补充) | 本科 | 17 |
| SM | Master of Science | 研究生 | 27 |
| MEng | Master of Engineering | 研究生 | 4 |
| MArch | Master of Architecture | 研究生 | 1 |
| MCP | Master in City Planning | 研究生 | 1 |
| MASc | Master of Applied Science | 研究生 | 4 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MBAn | Master of Business Analytics | 研究生 | 1 |
| MFin | Master of Finance | 研究生 | 1 |
| MSMS | Master of Science in Management Studies | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 32 |
| ScD | Doctor of Science | 研究生 | 9 |
| **合计** | | | **157** |

> Note: MIT does not award BA, BFA, MA, MFA, EdD, DNP, or "Advanced Certificate" degrees. MIT's graduate certificates (e.g. MicroMasters credentials) are non-degree and excluded from rule-1. ScD and PhD are equivalent doctorates at MIT; several departments (AeroAstro, ChemE, CEE, DMSE, Math, NSE, EAPS, EECS, ME, MIT-WHOI) offer both.

### 0.4 分布矩阵 (学院 × 学位级别) (Rule 4)

| 学院 \ 级别 | SB | Minor | SM | MEng | MArch | MCP | MASc | MBA | MBAn | MFin | MSMS | PhD | ScD | **合计** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| School of Engineering | 23 | 3 | 9 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | 7 | **55** |
| School of Science | 8 | 1 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 2 | **24** |
| School of Architecture and Planning | 4 | 0 | 6 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | **14** |
| School of Humanities, Arts, and Social Sciences | 17 | 10 | 3 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 5 | 0 | **37** |
| MIT Sloan School of Management | 3 | 1 | 1 | 0 | 0 | 0 | 0 | 4 | 1 | 1 | 1 | 1 | 0 | **13** |
| Schwarzman College of Computing | 0 | 1 | 4 | 2 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 4 | 0 | **13** |
| Institute-wide (Energy Initiative) | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| **合计** | **55** | **17** | **27** | **4** | **1** | **1** | **4** | **4** | **1** | **1** | **1** | **32** | **9** | **157** |

**Reconciliation**: row totals = column totals = grand total = **157** = rule-1 count. PASS (computed, not hand-counted).

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

MIT undergraduates earn the **Bachelor of Science (SB)** in every field (MIT does not offer BA/BFA). Students enter undeclared and choose a major (often called a "Course", identified by number — e.g. Course 6 = EECS) by end of sophomore year. The 6 schools + Schwarzman College of Computing house the departments; see the full hierarchy tree in Section 0.2. All UG majors below are SB.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别


#### School of Engineering

##### Aeronautics and Astronautics

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 1 | 16 | Aerospace Engineering | https://catalog.mit.edu/degree-charts/aerospace-engineering-course-16/ |
| 2 | 16-ENG | Engineering (Aero/Astro) | https://catalog.mit.edu/degree-charts/engineering-aeronautics-astronautics-course-16-eng/ |

##### Biological Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 3 | 20 | Biological Engineering | https://catalog.mit.edu/degree-charts/biological-engineering-course-20/ |

##### Chemical Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 4 | 10 | Chemical Engineering | https://catalog.mit.edu/degree-charts/chemical-engineering-course-10/ |
| 5 | 10-B | Chemical-Biological Engineering | https://catalog.mit.edu/degree-charts/chemical-biological-engineering-course-10-b/ |
| 6 | 10-C | Chemical Engineering | https://catalog.mit.edu/degree-charts/chemical-engineering-course-10-c/ |
| 7 | 10-ENG | Engineering (ChemE) | https://catalog.mit.edu/degree-charts/engineering-chemical-engineering-course-10-eng/ |

##### Civil and Environmental Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 8 | 1-ENG | Engineering (CEE) | https://catalog.mit.edu/degree-charts/engineering-civil-environmental-engineering-course-1-eng/ |
| 9 | 1-12 | Climate System Science and Engineering ⚠ 跨学院: School of Engineering / School of Science | https://catalog.mit.edu/degree-charts/climate-system-science-engineering-course-1-12/ |

##### Electrical Eng. and Computer Science

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 10 | 6-3 | Computer Science and Engineering | https://catalog.mit.edu/degree-charts/computer-science-engineering-course-6-3/ |
| 11 | 6-4 | Artificial Intelligence and Decision Making | https://catalog.mit.edu/degree-charts/artifical-intelligence-decision-making-course-6-4/ |
| 12 | 6-5 | Electrical Engineering with Computing | https://catalog.mit.edu/degree-charts/electrical-engineering-computing-course-6-5/ |
| 13 | 6-9 | Computation and Cognition ⚠ 跨学院: School of Engineering / School of Science | https://catalog.mit.edu/degree-charts/computation-cognition-6-9/ |
| 14 | 6-7 | Computer Science and Molecular Biology ⚠ 跨学院: School of Engineering / School of Science | https://catalog.mit.edu/degree-charts/computer-science-molecular-biology-course-6-7/ |
| 15 | 6-14 | Computer Science, Economics, and Data Science ⚠ 跨学院: School of Engineering / School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/degree-charts/computer-science-economics-data-science-course-6-14/ |

##### Materials Science and Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 16 | 3 | Materials Science and Engineering | https://catalog.mit.edu/degree-charts/materials-science-engineering-course-3/ |
| 17 | 3-A | Materials Science and Engineering | https://catalog.mit.edu/degree-charts/materials-science-engineering-course-3-a/ |
| 18 | 3-C | Archaeology and Materials | https://catalog.mit.edu/degree-charts/archaeology-materials-course-3-c/ |

##### Mechanical Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 19 | 2 | Mechanical Engineering | https://catalog.mit.edu/degree-charts/mechanical-engineering-course-2/ |
| 20 | 2-A | Engineering (MechE) | https://catalog.mit.edu/degree-charts/mechanical-engineering-course-2-a/ |
| 21 | 2-OE | Mechanical and Ocean Engineering | https://catalog.mit.edu/degree-charts/mechanical-ocean-engineering-course-2-oe/ |

##### Nuclear Science and Engineering

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 22 | 22 | Nuclear Science and Engineering | https://catalog.mit.edu/degree-charts/nuclear-science-engineering-course-22/ |
| 23 | 22-ENG | Engineering (NSE) | https://catalog.mit.edu/degree-charts/engineering-nuclear-science-engineering-course-22-eng/ |


#### School of Science

##### Biology

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 24 | 7 | Biology | https://catalog.mit.edu/degree-charts/biology-course-7/ |

##### Chemistry

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 25 | 5 | Chemistry | https://catalog.mit.edu/degree-charts/chemistry-course-5/ |
| 26 | 5-7 | Chemistry and Biology | https://catalog.mit.edu/degree-charts/chemistry-biology-course-5-7/ |

##### Brain and Cognitive Sciences

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 27 | 9 | Brain and Cognitive Sciences | https://catalog.mit.edu/degree-charts/brain-cognitive-sciences-course-9/ |

##### Earth, Atmospheric and Planetary Sciences

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 28 | 12 | Earth, Atmospheric and Planetary Sciences | https://catalog.mit.edu/degree-charts/earth-atmospheric-planetary-sciences-course-12/ |

##### Mathematics

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 29 | 18 | Mathematics | https://catalog.mit.edu/degree-charts/mathematics-course-18/ |
| 30 | 18-C | Mathematics with Computer Science | https://catalog.mit.edu/degree-charts/mathematics-computer-science-course-18-c/ |

##### Physics

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 31 | 8 | Physics | https://catalog.mit.edu/degree-charts/physics-course-8/ |


#### School of Architecture and Planning

##### Architecture

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 32 | 4 | Architecture | https://catalog.mit.edu/degree-charts/architecture-course-4/ |
| 33 | 4-B | Art and Design | https://catalog.mit.edu/degree-charts/architecture-course-4-b/ |

##### Urban Studies and Planning

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 34 | 11 | Planning | https://catalog.mit.edu/degree-charts/planning-course-11/ |
| 35 | 11-6 | Urban Science and Planning with Computer Science ⚠ 跨学院: School of Architecture and Planning / Schwarzman College of Computing | https://catalog.mit.edu/degree-charts/urban-science-planning-computer-science-11-6/ |


#### School of Humanities, Arts, and Social Sciences

##### Anthropology

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 36 | 21A | Anthropology | https://catalog.mit.edu/degree-charts/anthropology-course-21a/ |

##### Comparative Media Studies/Writing

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 37 | CMS | Comparative Media Studies | https://catalog.mit.edu/degree-charts/comparative-media-studies-cms/ |
| 38 | 21W | Writing | https://catalog.mit.edu/degree-charts/writing-course-21w/ |

##### Global Studies and Languages

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 39 | 21G | Global Studies and Languages | https://catalog.mit.edu/degree-charts/global-studies-languages-course-21g/ |

##### History

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 40 | 21H | History | https://catalog.mit.edu/degree-charts/history-course-21h/ |

##### Humanities (Dean's Office)

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 41 | 21 | Humanities | https://catalog.mit.edu/degree-charts/humanities-course-21/ |
| 42 | 21E | Humanities and Engineering ⚠ 跨学院: School of Humanities, Arts, and Social Sciences / School of Engineering | https://catalog.mit.edu/degree-charts/humanities-engineering-course-21e/ |
| 43 | 21S | Humanities and Science ⚠ 跨学院: School of Humanities, Arts, and Social Sciences / School of Science | https://catalog.mit.edu/degree-charts/humanities-science-course-21s/ |

##### Literature

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 44 | 21L | Literature | https://catalog.mit.edu/degree-charts/literature-course-21l/ |

##### Music and Theater Arts

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 45 | 21M | Music | https://catalog.mit.edu/degree-charts/music-course-21m/ |
| 46 | 21T | Theater Arts | https://catalog.mit.edu/degree-charts/theater-arts-course-21t/ |

##### Linguistics and Philosophy

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 47 | 24-1 | Philosophy | https://catalog.mit.edu/degree-charts/philosophy-course-24-1/ |
| 48 | 24-2 | Linguistics and Philosophy | https://catalog.mit.edu/degree-charts/linguistics-philosophy-course-24-2/ |

##### Political Science

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 49 | 17 | Political Science | https://catalog.mit.edu/degree-charts/political-science-course-17/ |

##### Science, Technology, and Society

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 50 | STS | Science, Technology, and Society/Second Major | https://catalog.mit.edu/degree-charts/science-technology-society-sts/ |

##### Economics

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 51 | 14-1 | Economics | https://catalog.mit.edu/degree-charts/economics-course-14/ |
| 52 | 14-2 | Mathematical Economics | https://catalog.mit.edu/degree-charts/mathematical-economics-course-14-2/ |


#### MIT Sloan School of Management

##### MIT Sloan (UG)

###### SB

| # | 课程号 | 专业 | URL |
|---|--------|------|-----|
| 53 | 15-1 | Management | https://catalog.mit.edu/degree-charts/management-course-15-1/ |
| 54 | 15-2 | Business Analytics | https://catalog.mit.edu/degree-charts/business-analytics-course-15-2/ |
| 55 | 15-3 | Finance | https://catalog.mit.edu/degree-charts/finance-course-15-3/ |


### 1.3 Interdisciplinary / cross-college undergraduate programs

The following SB majors are joint across two schools (listed under administrative home in 1.2, cross-listed here):

| 课程号 | 专业 | 父学院 |
|--------|------|--------|
| 6-9 | Computation and Cognition | School of Engineering (EECS) × School of Science (BCS) |
| 6-7 | Computer Science and Molecular Biology | School of Engineering (EECS) × School of Science (Biology) |
| 6-14 | Computer Science, Economics, and Data Science | School of Engineering (EECS) × SHASS (Economics) |
| 11-6 | Urban Science and Planning with Computer Science | School of Architecture and Planning (DUSP) × Schwarzman (EECS) |
| 1-12 | Climate System Science and Engineering | School of Engineering (CEE) × School of Science (EAPS) |
| 21E | Humanities and Engineering | SHASS × School of Engineering |
| 21S | Humanities and Science | SHASS × School of Science |

### 1.4 Minors — complete list (17)

| # | Minor | 所属学院 | URL |
|---|-------|---------|-----|
| 1 | African and African Diaspora Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 2 | American Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 3 | Ancient and Medieval Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 4 | Applied International Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 5 | Asian and Asian Diaspora Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 6 | Astronomy | School of Science | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 7 | Biomedical Engineering | School of Engineering | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 8 | Energy Studies | Institute-wide (Energy Initiative) | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 9 | Entrepreneurship and Innovation | MIT Sloan School of Management | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 10 | Environment and Sustainability | School of Engineering | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 11 | Latin American and Latino/a Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 12 | Middle Eastern Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 13 | Polymers and Soft Matter | School of Engineering | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 14 | Public Policy | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 15 | Russian and Eurasian Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 16 | Statistics and Data Science | Schwarzman College of Computing | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |
| 17 | Women's and Gender Studies | School of Humanities, Arts, and Social Sciences | https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/ |

### 1.5 General Institute Requirements (GIRs)

All SB candidates must complete the **General Institute Requirements**: the **Science Core** (calculus, physics, chemistry, biology), the **Communication Requirement** (writing/integrated across all four years), the **Laboratory Requirement**, and the **Restricted Electives in Science and Technology (REST)**. Plus a **HASS (Humanities, Arts, and Social Sciences) Requirement** (8 subjects across distribution) and a **Physical Education requirement** (swim test + 4 PE units). Source: https://catalog.mit.edu/mit/undergraduate-education/

### 1.6 Course-ID → Major quick-lookup

| 课程号 | 专业 | 所属学院 |
|--------|------|---------|
| 4 | Architecture | School of Architecture and Planning
| 4-B | Art and Design | School of Architecture and Planning
| 11 | Planning | School of Architecture and Planning
| 11-6 | Urban Science and Planning with Computer Science | School of Architecture and Planning
| 16 | Aerospace Engineering | School of Engineering
| 16-ENG | Engineering (Aero/Astro) | School of Engineering
| 20 | Biological Engineering | School of Engineering
| 10 | Chemical Engineering | School of Engineering
| 10-B | Chemical-Biological Engineering | School of Engineering
| 10-C | Chemical Engineering | School of Engineering
| 10-ENG | Engineering (ChemE) | School of Engineering
| 1-ENG | Engineering (CEE) | School of Engineering
| 1-12 | Climate System Science and Engineering | School of Engineering
| 6-3 | Computer Science and Engineering | School of Engineering
| 6-4 | Artificial Intelligence and Decision Making | School of Engineering
| 6-5 | Electrical Engineering with Computing | School of Engineering
| 6-9 | Computation and Cognition | School of Engineering
| 6-7 | Computer Science and Molecular Biology | School of Engineering
| 6-14 | Computer Science, Economics, and Data Science | School of Engineering
| 3 | Materials Science and Engineering | School of Engineering
| 3-A | Materials Science and Engineering | School of Engineering
| 3-C | Archaeology and Materials | School of Engineering
| 2 | Mechanical Engineering | School of Engineering
| 2-A | Engineering (MechE) | School of Engineering
| 2-OE | Mechanical and Ocean Engineering | School of Engineering
| 22 | Nuclear Science and Engineering | School of Engineering
| 22-ENG | Engineering (NSE) | School of Engineering
| 21A | Anthropology | School of Humanities, Arts, and Social Sciences
| CMS | Comparative Media Studies | School of Humanities, Arts, and Social Sciences
| 21W | Writing | School of Humanities, Arts, and Social Sciences
| 21G | Global Studies and Languages | School of Humanities, Arts, and Social Sciences
| 21H | History | School of Humanities, Arts, and Social Sciences
| 21 | Humanities | School of Humanities, Arts, and Social Sciences
| 21E | Humanities and Engineering | School of Humanities, Arts, and Social Sciences
| 21S | Humanities and Science | School of Humanities, Arts, and Social Sciences
| 21L | Literature | School of Humanities, Arts, and Social Sciences
| 21M | Music | School of Humanities, Arts, and Social Sciences
| 21T | Theater Arts | School of Humanities, Arts, and Social Sciences
| 24-1 | Philosophy | School of Humanities, Arts, and Social Sciences
| 24-2 | Linguistics and Philosophy | School of Humanities, Arts, and Social Sciences
| 17 | Political Science | School of Humanities, Arts, and Social Sciences
| STS | Science, Technology, and Society/Second Major | School of Humanities, Arts, and Social Sciences
| 15-1 | Management | MIT Sloan School of Management
| 15-2 | Business Analytics | MIT Sloan School of Management
| 15-3 | Finance | MIT Sloan School of Management
| 7 | Biology | School of Science
| 5 | Chemistry | School of Science
| 5-7 | Chemistry and Biology | School of Science
| 9 | Brain and Cognitive Sciences | School of Science
| 12 | Earth, Atmospheric and Planetary Sciences | School of Science
| 18 | Mathematics | School of Science
| 18-C | Mathematics with Computer Science | School of Science
| 8 | Physics | School of Science
| 14-1 | Economics | School of Humanities, Arts, and Social Sciences
| 14-2 | Mathematical Economics | School of Humanities, Arts, and Social Sciences

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Each row below is one degree-offering. A department offering multiple degrees (e.g. AeroAstro: SM, PhD, ScD) appears once per degree. All URLs are on oge.mit.edu.


#### School of Engineering

##### Aeronautics and Astronautics

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 1 | Aeronautics and Astronautics | Master of Science in Aeronautics and Astronautics (SM) | https://oge.mit.edu/programs/aeronautics-and-astronautics/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 2 | Aeronautics and Astronautics | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/aeronautics-and-astronautics/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 3 | Aeronautics and Astronautics | Doctor of Science (ScD) | https://oge.mit.edu/programs/aeronautics-and-astronautics/ |

##### Biological Engineering

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 4 | Biological Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/biological-engineering-2/ |

##### Chemical Engineering

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 5 | Chemical Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/chemical-engineering/ |
| 6 | Chemical Engineering | Doctor of Philosophy in Chemical Engineering Practice (PhDCEP) | https://oge.mit.edu/programs/chemical-engineering/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 7 | Chemical Engineering | Doctor of Science (ScD) | https://oge.mit.edu/programs/chemical-engineering/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 8 | Chemical Engineering | Master of Science in Chemical Engineering Practice (MSCEP) | https://oge.mit.edu/programs/chemical-engineering/ |

##### Civil and Environmental Engineering

###### MEng

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 9 | Civil and Environmental Engineering | Master of Engineering (MEng) | https://oge.mit.edu/programs/civil-and-environmental-engineering/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 10 | Civil and Environmental Engineering | Master of Science (SM) | https://oge.mit.edu/programs/civil-and-environmental-engineering/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 11 | Civil and Environmental Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/civil-and-environmental-engineering/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 12 | Civil and Environmental Engineering | Doctor of Science (ScD) | https://oge.mit.edu/programs/civil-and-environmental-engineering/ |

##### Electrical Eng. and Computer Science

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 13 | Electrical Engineering and Computer Science | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/electrical-engineering-and-computer-science/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 14 | Electrical Engineering and Computer Science | Doctor of Science (ScD) | https://oge.mit.edu/programs/electrical-engineering-and-computer-science/ |

##### Health Sciences and Technology

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 15 | Health Sciences and Technology (Harvard-MIT) | Medical Engineering and Medical Physics PhD (MEMP) | https://oge.mit.edu/programs/harvard-mit-health-sciences-and-technology/ |

##### Materials Science and Engineering

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 16 | Materials Science and Engineering | Master of Science in Materials Science and Engineering (SM) | https://oge.mit.edu/programs/materials-science-and-engineering/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 17 | Materials Science and Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/materials-science-and-engineering/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 18 | Materials Science and Engineering | Doctor of Science (ScD) | https://oge.mit.edu/programs/materials-science-and-engineering/ |

##### Mechanical Engineering

###### MEng

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 19 | Mechanical Engineering | Master of Engineering in Manufacturing (MEng) | https://oge.mit.edu/programs/mechanical-engineering/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 20 | Mechanical Engineering | Master of Science in Mechanical Engineering (SM) | https://oge.mit.edu/programs/mechanical-engineering/ |
| 21 | Mechanical Engineering | Master of Science in Ocean Engineering (SM) | https://oge.mit.edu/programs/mechanical-engineering/ |
| 22 | Mechanical Engineering | Master of Science in Oceanographic Engineering (SM) | https://oge.mit.edu/programs/mechanical-engineering/ |
| 23 | Mechanical Engineering | Master of Science in Naval Architecture and Marine Engineering (SM) | https://oge.mit.edu/programs/mechanical-engineering/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 24 | Mechanical Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/mechanical-engineering/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 25 | Mechanical Engineering | Doctor of Science (ScD) | https://oge.mit.edu/programs/mechanical-engineering/ |

##### Nuclear Science and Engineering

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 26 | Nuclear Science and Engineering | Master of Science in Nuclear Science and Engineering (SM) | https://oge.mit.edu/programs/nuclear-science-and-engineering/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 27 | Nuclear Science and Engineering | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/nuclear-science-and-engineering/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 28 | Nuclear Science and Engineering | Doctor of Science (ScD) | https://oge.mit.edu/programs/nuclear-science-and-engineering/ |

##### Program in Polymers and Soft Matter (interdepartmental)

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 29 | Program in Polymers and Soft Matter | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/program-in-polymers-and-soft-matter/ |


#### School of Science

##### Biology

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 30 | Biology | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/biology/ |
| 31 | Microbiology | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/microbiology/ |

##### Brain and Cognitive Sciences

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 32 | Brain and Cognitive Sciences | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/brain-and-cognitive-sciences/ |

##### Chemistry

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 33 | Chemistry | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/chemistry/ |

##### Computational and Systems Biology

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 34 | Computational and Systems Biology | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/computational-and-systems-biology/ |

##### Earth, Atmospheric and Planetary Sciences

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 35 | Earth, Atmospheric, and Planetary Sciences | Master of Science in Earth and Planetary Sciences (SM) | https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/ |
| 36 | Earth, Atmospheric, and Planetary Sciences | Master of Science in Atmospheric Science (SM) | https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/ |
| 37 | Earth, Atmospheric, and Planetary Sciences | Master of Science in Climate Physics and Chemistry (SM) | https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 38 | Earth, Atmospheric, and Planetary Sciences | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 39 | Earth, Atmospheric, and Planetary Sciences | Doctor of Science (ScD) | https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/ |

##### Mathematics

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 40 | Mathematics | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/mathematics/ |

###### ScD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 41 | Mathematics | Doctor of Science (ScD) | https://oge.mit.edu/programs/mathematics/ |

##### Earth, Atmospheric and Planetary Sciences (joint with WHOI)

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 42 | MIT-WHOI Joint Program (Oceanography/Applied Ocean Science & Engineering) | Master of Science (SM) for U.S. Naval Officers | https://oge.mit.edu/programs/mit-whoi-joint-program-in-oceanography-applied-ocean-science-and-engineering/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 43 | MIT-WHOI Joint Program (Oceanography/Applied Ocean Science & Engineering) | Doctor of Philosophy (PhD)/Doctor of Science (ScD) | https://oge.mit.edu/programs/mit-whoi-joint-program-in-oceanography-applied-ocean-science-and-engineering/ |

##### Physics

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 44 | Physics | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/physics/ |


#### School of Architecture and Planning

##### Architecture

###### MArch

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 45 | Architecture | Master of Architecture (MArch) | https://oge.mit.edu/programs/architecture/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 46 | Architecture | Master of Science in Architecture Studies (SMArchS) | https://oge.mit.edu/programs/architecture/ |
| 47 | Architecture | Master of Science in Building Technology (SMBT) | https://oge.mit.edu/programs/architecture/ |
| 48 | Architecture | Master of Science in Art, Culture and Technology (SMACT) | https://oge.mit.edu/programs/architecture/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 49 | Architecture | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/architecture/ |

##### Center for Real Estate

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 50 | Center for Real Estate | Master of Science in Real Estate Development (SM) | https://oge.mit.edu/programs/center-for-real-estate/ |

##### Media Arts and Sciences (Media Lab)

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 51 | Media Arts and Sciences | Master of Science in Media Arts and Sciences (SM) | https://oge.mit.edu/programs/media-arts-and-sciences/ |

##### Urban Studies and Planning

###### MCP

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 52 | Urban Studies and Planning | Master in City Planning (MCP) | https://oge.mit.edu/programs/urban-studies-and-planning/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 53 | Urban Studies and Planning | Master of Science in Urban Studies and Planning (SM) | https://oge.mit.edu/programs/urban-studies-and-planning/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 54 | Urban Studies and Planning | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/urban-studies-and-planning/ |


#### School of Humanities, Arts, and Social Sciences

##### Economics (J-PAL)

###### MASc

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 55 | Data, Economics, and Design of Policy | Master of Applied Science in Data, Economics, and Design of Policy | https://oge.mit.edu/programs/data-economics-and-development-policy/ |

##### Economics

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 56 | Economics | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/economics/ |

##### History, Anthropology, and STS (HASTS)

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 57 | History, Anthropology, and STS | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/history-anthropology-and-science-technology-and-society/ |

##### Linguistics and Philosophy

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 58 | Linguistics | Doctor of Philosophy in Linguistics (PhD) | https://oge.mit.edu/programs/linguistics/ |
| 59 | Philosophy | Doctor of Philosophy in Philosophy (PhD) | https://oge.mit.edu/programs/philosophy/ |

##### Music and Theater Arts

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 60 | Music Technology and Computation | Master of Science (SM) | https://oge.mit.edu/programs/music-technology-and-computation/ |

###### MASc

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 61 | Music Technology and Computation | Master of Applied Science (MASc) | https://oge.mit.edu/programs/music-technology-and-computation/ |

##### Political Science

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 62 | Political Science | Master of Science in Political Science (SM) | https://oge.mit.edu/programs/political-science/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 63 | Political Science | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/political-science/ |

##### Comparative Media Studies/Writing

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 64 | Science Writing | Master of Science in Science Writing (SM) | https://oge.mit.edu/programs/science-writing/ |


#### MIT Sloan School of Management

##### Leaders for Global Operations (with Engineering)

###### MBA

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 65 | Leaders for Global Operations | Master of Business Administration (MBA) | https://oge.mit.edu/programs/leaders-for-global-operations/ |

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 66 | Leaders for Global Operations | Master of Science (SM) | https://oge.mit.edu/programs/leaders-for-global-operations/ |

##### MIT Sloan (Executive)

###### MBA

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 67 | MIT Sloan Executive MBA | Master of Business Administration (MBA) | https://oge.mit.edu/programs/mit-sloan-executive-mba-program/ |

##### MIT Sloan (Fellows)

###### MBA

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 68 | MIT Sloan Fellows MBA | Master of Business Administration (MBA) | https://oge.mit.edu/programs/mit-sloan-fellows-mba-program/ |

##### MIT Sloan (MBAn)

###### MBAn

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 69 | MIT Sloan Master of Business Analytics | Master of Business Analytics (MBAn) | https://oge.mit.edu/programs/mit-sloan-master-of-business-analytics/ |

##### MIT Sloan (MFin)

###### MFin

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 70 | MIT Sloan Master of Finance | Master of Finance (MFin) | https://oge.mit.edu/programs/mit-sloan-master-of-finance/ |

##### MIT Sloan (MSMS)

###### MSMS

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 71 | MIT Sloan Master of Science in Management Studies | Master of Science in Management Studies (MSMS) | https://oge.mit.edu/programs/mit-sloan-master-of-science-in-management-studies/ |

##### MIT Sloan (MBA)

###### MBA

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 72 | MIT Sloan MBA | Master of Business Administration (MBA) | https://oge.mit.edu/programs/mit-sloan-mba-program/ |

##### MIT Sloan (PhD)

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 73 | MIT Sloan PhD | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/mit-sloan-phd-program/ |


#### Schwarzman College of Computing

##### Institute for Data, Systems, and Society (CSE)

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 74 | Computational Science and Engineering PhD | Doctor of Philosophy (PhD) in Computational Science and Engineering | https://oge.mit.edu/programs/computational-science-and-engineering-phd/ |

##### Institute for Data, Systems, and Society

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 75 | Institute for Data, Systems, and Society | Doctor of Philosophy in Social and Engineering Systems (PhD) | https://oge.mit.edu/programs/institute-for-data-systems-and-society/ |

##### Operations Research Center

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 76 | Operations Research Center | Master of Science in Operations Research (SM) | https://oge.mit.edu/programs/operations-research-center/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 77 | Operations Research Center | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/operations-research-center/ |

##### Center for Transportation & Logistics

###### MASc

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 78 | Supply Chain Management (Blended) | Master of Applied Science in Supply Chain Management | https://oge.mit.edu/programs/supply-chain-management-blended/ |
| 79 | Supply Chain Management (Residential) | Master of Applied Science in Supply Chain Management | https://oge.mit.edu/programs/supply-chain-management-residential/ |

###### MEng

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 80 | Supply Chain Management (Blended) | Master of Engineering in Supply Chain Management | https://oge.mit.edu/programs/supply-chain-management-blended/ |
| 81 | Supply Chain Management (Residential) | Master of Engineering in Supply Chain Management | https://oge.mit.edu/programs/supply-chain-management-residential/ |

##### System Design and Management (with Engineering)

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 82 | System Design and Management | Master of Science in Engineering and Management (SM) | https://oge.mit.edu/programs/system-design-and-management/ |

##### Technology and Policy Program (with Engineering)

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 83 | Technology and Policy Program | Master of Science in Technology and Policy (SM) | https://oge.mit.edu/programs/technology-and-policy-program/ |

##### Center for Transportation & Logistics (with CEE)

###### SM

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 84 | Transportation | Master of Science in Transportation (MST) | https://oge.mit.edu/programs/transportation/ |

###### PhD

| # | 项目 | 学位全称 | URL |
|---|------|---------|-----|
| 85 | Transportation | Doctor of Philosophy (PhD) | https://oge.mit.edu/programs/transportation/ |


### 2.2 Worked deep-dive — Electrical Engineering and Computer Science (Course 6, the largest program)

| 字段 | 值 | 来源 |
|------|-----|------|
| Department | Electrical Engineering and Computer Science | oge.mit.edu/programs/electrical-engineering-and-computer-science/ |
| Address | 77 Massachusetts Avenue, Building 38-444, Cambridge MA 02139 | OGE EECS page |
| Phone / Email | 617-253-4603 / grad-ap@eecs.mit.edu | OGE EECS page |
| Degrees offered | Doctor of Philosophy (PhD); Doctor of Science (ScD) | OGE EECS Degrees accordion (field-item) |
| Application platform | MIT online application (decentralized — each dept) | OGE |
| Standardized tests | GRE — required for some tracks; **IELTS preferred** for English proficiency; Institution code **3514** (MIT), dept code per program | OGE EECS/CSE Standardized Tests sections |
| Funding | PhD students fully funded (RA/TA/fellowship); SM admission limited/self-funded paths exist | OGE EECS Financial Support section |

> ✅ **已完成 (2026-07-04):** 47 个 OGE 研究生项目的逐项录取数据 (截止日/申请费/GRE 政策/英语最低分/资助模型) 已全部抓取,见下方 **Section 2.4 各研究生项目录取明细表**,原始证据见 E-G-008。

### 2.3 Graduate admissions model

MIT graduate admissions is **decentralized**: each of the 47 programs runs its own admissions committee, sets its own deadlines, GRE policy, and English-proficiency minimums, and uses the central MIT online application. The **Office of Graduate Education (OGE, oge.mit.edu)** publishes the program directory and institute-wide policies; the program pages carry the binding per-program detail. Standard application materials across programs: online application, statement of objectives, 2–3 letters of recommendation, transcripts, CV, standardized-test scores, English-proficiency scores (international). Most PhD programs are fully funded (RA/TA + fellowship); most master's programs are self-funded.

### 2.4 各研究生项目录取明细 — 47 个 OGE 项目逐项数据

> 数据源: 每个 OGE 项目详情页的展开面板 (Application Requirements / Standardized Tests / Financial Support / Department Policies),统一抓取并结构化。完整原始文本见 `uni-cache/schools/mit/grad-program-details.json`。证据汇总见 [E-G-008](#e-g-008)。
>
> 费用栏上标 ¹ = 该项目明确提供申请费豁免 (fee waiver)。

| # | 项目 (Program) | 申请截止 (美东时间) | 申请费 | GRE/GMAT 政策 | 英语能力 (最低分) | 资助模型 | 来源 |
|---|----------------|---------------------|--------|---------------|-------------------|----------|------|
| 1 | Aeronautics and Astronautics | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/aeronautics-and-astronautics/) |
| 2 | Architecture | January 7 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/architecture/) |
| 3 | Biological Engineering | December 1 at 11:59 PM Eastern Time | $90.00 | Not required (no standardized test) | IELTS 7 / TOEFL 100 / DET 135 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/biological-engineering-2/) |
| 4 | Biology | December 1 at 11:59 PM Eastern Time | $90.00 | Not required (no standardized test) | IELTS 6.5 / TOEFL 100 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/biology/) |
| 5 | Brain and Cognitive Sciences | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 90 / DET 135 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/brain-and-cognitive-sciences/) |
| 6 | Center for Real Estate | January 7 at 11:59 PM Eastern Time | $90.00 | Optional (GRE or GMAT) | IELTS 7.5 / TOEFL 100 | 资助 (详见项目页) | [项目页](https://oge.mit.edu/programs/center-for-real-estate/) |
| 7 | Chemical Engineering | December 1 at 11:59 PM Eastern Time | $90.00 | Not required (no standardized test) | IELTS 7 / TOEFL 100 / DET 135 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/chemical-engineering/) |
| 8 | Chemistry | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/chemistry/) |
| 9 | Civil and Environmental Engineering | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7.5 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/civil-and-environmental-engineering/) |
| 10 | Computational and Systems Biology | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/computational-and-systems-biology/) |
| 11 | Computational Science and Engineering PhD | December 1 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7 / TOEFL 100 | 详见项目页 | [项目页](https://oge.mit.edu/programs/computational-science-and-engineering-phd/) |
| 12 | Data, Economics, and Design of Policy | January 15 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 自费为主 | [项目页](https://oge.mit.edu/programs/data-economics-and-development-policy/) |
| 13 | Earth, Atmospheric, and Planetary Sciences | December 15 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7 / DET 135 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/earth-atmospheric-and-planetary-sciences/) |
| 14 | Economics | December 15 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7 / TOEFL 100 / DET 135 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/economics/) |
| 15 | Electrical Engineering and Computer Science | December 1 at 11:59 PM Eastern Time | $90.00 ¹ | Not required | IELTS 7 / TOEFL 100 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/electrical-engineering-and-computer-science/) |
| 16 | Health Sciences and Technology (Joint Harvard-MIT Program) | December 1 at 11:59 PM Eastern Time | $90.00 ¹ | Not required (no standardized test) | IELTS 7 / TOEFL 100 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/harvard-mit-health-sciences-and-technology/) |
| 17 | History, Anthropology, and Science, Technology, and Society | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/history-anthropology-and-science-technology-and-society/) |
| 18 | Institute for Data, Systems, and Society | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7.5 / TOEFL 110 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/institute-for-data-systems-and-society/) |
| 19 | Leaders for Global Operations | November 8 at 11:59 PM Eastern Time | $250.00 | Required (GRE or GMAT) | Conditional (R2 via Aero/Astro only) | 自费为主 | [项目页](https://oge.mit.edu/programs/leaders-for-global-operations/) |
| 20 | Linguistics | December 15 at 11:59 PM Eastern Time | $90.00 | Not required (no standardized test) | IELTS 6.5 / TOEFL 90 / DET 135 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/linguistics/) |
| 21 | Materials Science and Engineering | December 1 at 11:59 PM Eastern Time | $90.00 | Not required (no standardized test) | IELTS 7 / TOEFL 100 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/materials-science-and-engineering/) |
| 22 | Mathematics | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 6 / TOEFL 100 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/mathematics/) |
| 23 | Mechanical Engineering | December 15 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7 / TOEFL 100 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/mechanical-engineering/) |
| 24 | Media Arts and Sciences | Master of Science (SM): December 15 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/media-arts-and-sciences/) |
| 25 | Microbiology | December 1 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/microbiology/) |
| 26 | MIT Sloan Executive MBA Program | Early Admissions: December 5, 2024 | $250.00 | Not required | Not required (English via interview) | 自费 (职业硕士) | [项目页](https://oge.mit.edu/programs/mit-sloan-executive-mba-program/) |
| 27 | MIT Sloan Fellows MBA Program | 多轮次 (见项目页) | $250.00 | Optional | Not required (English via interview) | 自费 (职业硕士) | [项目页](https://oge.mit.edu/programs/mit-sloan-fellows-mba-program/) |
| 28 | MIT Sloan Master of Business Analytics | January 5, 2026 | $150.00 | Optional (GRE or GMAT) | Not required (English via interview) | 自费 (职业硕士) | [项目页](https://oge.mit.edu/programs/mit-sloan-master-of-business-analytics/) |
| 29 | MIT Sloan Master of Finance | January 5, 2026 | $150.00 | Optional (GRE or GMAT) | Not required (English via interview) | 自费 (职业硕士) | [项目页](https://oge.mit.edu/programs/mit-sloan-master-of-finance/) |
| 30 | MIT Sloan Master of Science in Management Studies | February 20, 2026 | — | Required (GRE or GMAT) | Not required (English via interview) | 硕士:自费为主 (部分 RA/TA) | [项目页](https://oge.mit.edu/programs/mit-sloan-master-of-science-in-management-studies/) |
| 31 | MIT Sloan MBA Program | 多轮次 (见项目页) | $250.00 | Required (GRE or GMAT) | Not required (English via interview) | 自费 (职业硕士) | [项目页](https://oge.mit.edu/programs/mit-sloan-mba-program/) |
| 32 | MIT Sloan PhD Program | December 1 at 11:59 PM Eastern Time | $95.00 | Required (GRE or GMAT) | IELTS 7 / TOEFL 90 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/mit-sloan-phd-program/) |
| 33 | MIT-WHOI Joint Program in Oceanography / Applied Ocean Science and Engineering | October 1 at 11:59 PM Eastern Time (SM Program for U.S. Naval Officers) | $90.00 | Optional | IELTS 7 / TOEFL 100 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/mit-whoi-joint-program-in-oceanography-applied-ocean-science-and-engineering/) |
| 34 | Music Technology and Computation | December 22 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7 / TOEFL 100 | 资助 (详见项目页) | [项目页](https://oge.mit.edu/programs/music-technology-and-computation/) |
| 35 | Nuclear Science and Engineering | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/nuclear-science-and-engineering/) |
| 36 | Operations Research Center | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7 / TOEFL 100 / DET 135 | 自费为主 | [项目页](https://oge.mit.edu/programs/operations-research-center/) |
| 37 | Philosophy | January 2 at 11:59 PM Eastern Time | $90.00 ¹ | Optional | IELTS 6.5 / TOEFL 90 / DET 135 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/philosophy/) |
| 38 | Physics | December 15 at 11:59 PM Eastern Time | $90.00 | Recommended (optional) | IELTS 7 / TOEFL 100 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/physics/) |
| 39 | Political Science | December 15 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/political-science/) |
| 40 | Program in Polymers and Soft Matter | December 1 or December 15, depending on home department | $90.00 | Set by home department | Set by home department | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/program-in-polymers-and-soft-matter/) |
| 41 | Science Writing | January 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7 / TOEFL 100 / DET 135 | 硕士:自费为主 (部分 RA/TA) | [项目页](https://oge.mit.edu/programs/science-writing/) |
| 42 | Supply Chain Management Blended | R1: January 10, 2026 at 11:59 PM Eastern Time | $90.00 | Not accepted | IELTS 7 / TOEFL 100 / DET 135 | 硕士:自费为主 (部分 RA/TA) | [项目页](https://oge.mit.edu/programs/supply-chain-management-blended/) |
| 43 | Supply Chain Management Residential | R1: November 1, 2025 at 11:59 PM Eastern Time | $90.00 | Required — MicroMasters SC0x OR GRE OR GMAT (any one) | IELTS 7 / TOEFL 100 / DET 135 | 硕士:自费为主 (部分 RA/TA) | [项目页](https://oge.mit.edu/programs/supply-chain-management-residential/) |
| 44 | System Design and Management | December 13, 2024 at 11:59 PM Eastern Time | $90.00 | Recommended (GRE or GMAT) | IELTS 7.5 / TOEFL 90 | 硕士:自费为主 (部分 RA/TA) | [项目页](https://oge.mit.edu/programs/system-design-and-management/) |
| 45 | Technology and Policy Program | December 15 at 11:59 PM Eastern Time | $90.00 | Optional | IELTS 7.5 | 全额资助 (fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/technology-and-policy-program/) |
| 46 | Transportation | December 15 at 11:59 PM Eastern Time | $90.00 | Required | IELTS 7.5 / TOEFL 100 | 全额资助 (博士,fellowship/RA/TA) | [项目页](https://oge.mit.edu/programs/transportation/) |
| 47 | Urban Studies and Planning | December 15 at 11:59 PM Eastern Time | $90.00 ¹ | Optional | IELTS 7 / TOEFL 100 / DET 135 | 博士全额资助 / 硕士自费为主 | [项目页](https://oge.mit.edu/programs/urban-studies-and-planning/) |

> **截止日期备注:** Sloan MBA / Fellows MBA 采用多轮次招生 (无单一截止日,见项目页);Supply Chain 与部分 Sloan 项目采用 Round 制;System Design and Management、Sloan EMBA 页面显示的日期为 2024 年 (MIT 页面按招生周期标注,对应下一入学季);Media Arts and Sciences、Program in Polymers 等跨系项目的截止日随归属系变化。

> **英语能力备注:** 标 "Not required (English via interview)" 的 Sloan 职业硕士项目不设 TOEFL/IELTS 线,通过面试评估英语;标 "Set by home department" 的 Program in Polymers and Soft Matter 沿用归属系 (BE/ChemE/MSE/MechE) 标准;Leaders for Global Operations 仅在 Round 2 经 Aero/Astro 系申请时需要 TOEFL/IELTS。所有 MIT 研究生送分机构代码为 **3514** (Sloan MBA 等少数用 3791)。

> **GRE/GMAT 政策图例:** "Not accepted" = 明确不接受也不考虑;"Not required" = 不要求 (可提交);"Optional" = 可选提交;"Required" = 必须;"Required/Optional (GRE or GMAT)" = Sloan 类项目 GRE 与 GMAT 二选一;"Not required (no standardized test)" = 该项目完全不需要标准化考试。

> **申请材料共性:** 在线申请 + 目的陈述/研究兴趣 (1–2 篇) + 2–3 封推荐信 + 成绩单 + CV + 英语成绩;博士项目通常附加写作样本/研究经历。详见各项目页 Application Requirements 面板。

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 证据 |
|------|-----|------|
| 招生网站 | mitadmissions.org | E-U-002 |
| 申请平台 | MIT application portal (NOT Common App; MIT uses its own) | E-U-002 |
| **EA 截止** | **November 1** (all components + 2 recs + SSR/transcript) | E-U-003 |
| **RA 截止** | **January 5** (all components + 2 recs + SSR/transcript) | E-U-003 |
| EA 测试截止 | November SAT/ACT test date | E-U-003 |
| RA 测试截止 | December SAT/ACT test date (English-proficiency through January dates) | E-U-003, E-U-004 |
| February Updates | Mid-February (midyear grades) | E-U-003 |
| EA 放榜 | Mid-December | E-U-003 |
| RA 放榜 | Mid-March | E-U-003 |
| 入学确认截止 | **May 1** (Reply date) | E-U-003 |
| 财务资助截止 | **February 15** | E-U-003 |
| SAT/ACT 政策 | **Required** (SAT or ACT; writing/essay sections NOT required; paper and digital SAT both accepted) | E-U-004 |
| Superscore | Yes — highest section scores across sittings considered | E-U-004 |
| 送分方式 | Self-report on application; verified upon enrollment (no official report needed at apply time) | E-U-004 |
| 面试 | Offered (Educational Counselors interview, when available) | mitadmissions.org/apply/firstyear/interview/ |
| 推荐信 | 2 — one math/science teacher + one humanities/social science/language teacher | E-U-003 |
| 作品集 | Supplemental via SlideRoom (researchers, performing/visual artists, makers) | E-U-003 |
| 转学途径 | Separate transfer application (≥1 year college) | mitadmissions.org/apply/transfer/ |
| 二学士学位 | NOT offered (MIT does not award second bachelor's degrees) | E-U-002 |

### 3.2 Undergraduate English proficiency table

Source: mitadmissions.org/apply/firstyear/tests-scores/ (E-U-004). Applicability: "strongly recommended" for non-native English speakers who have used English fewer than 5 years or do not speak English at home/school.

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL | 90 | 100 |
| IELTS | 7 | 7.5 |
| Pearson Test of English (PTE) Academic | 65 | 70 |
| Cambridge English Qualifications (C1 Advanced / C2 Proficiency) | 185 | 190 |
| Duolingo English Test (DET) | 120 | 125 |

> MIT does not publish SAT/ACT minimum or recommended scores — "scores are evaluated within an applicant's context." Accepted English exams: Cambridge, Duolingo, IELTS, PTE Academic, TOEFL.

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 招生模式 | **Decentralized** — 47 programs, each with own committee/deadlines/policies | oge.mit.edu/graduate-admissions/programs/ |
| 申请平台 | Central MIT online application (per-program entry) | OGE program pages |
| 申请费 | Varies by program (~$75–$150); fee waivers available per program | OGE program pages (Application Requirements sections) |
| GRE 政策 | Per-program; many STEM programs require GRE, some (e.g. MIT-WHOI) make it optional | OGE per-program Standardized Tests sections (E-G-001, E-G-002) |
| 英语能力 | Per-program; **IELTS preferred** at several programs (e.g. EECS, CSE); Institution code **3514** | OGE EECS/CSE Standardized Tests (E-G-001, E-G-002) |
| 英语免试 | Typically exempt if instruction language was English (per-program rules) | OGE program pages |
| 录取荣誉日 | MIT adheres to the **Council of Graduate Schools April 15 Resolution** for acceptance of financial offers | MIT graduate policy (P1 verify exact URL) |
| 测试代码 | MIT Institution code **3514** (GRE, TOEFL, IELTS) | E-G-002 (CSE page) |

> ✅ **已完成 (2026-07-04):** 47 个项目的逐项截止日 / GRE / IELTS / TOEFL 最低分 / 申请费 已全部抓取并结构化,见 **Section 2.4**;证据见 E-G-008。Section 6 中对应 3 项 P0 已标记完成。

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost — 2026–2027 academic year (line-itemized)

Source: sfs.mit.edu/undergraduate-students/the-cost-of-attendance/coa/ (E-U-005).

| 支出项 | 金额 (USD) | 说明 |
|--------|-----------|------|
| Tuition (学费) | $66,720 | Covers faculty, advising, study spaces, MIT Health (specific non-waivable services + urgent care/mental health/specialist) |
| Student life fee | $420 | Funds student clubs/orgs and their spaces |
| Housing (住宿) | $14,090 | Based on most expensive double room ($13,614); first-years required on-campus |
| Food (餐饮) | $8,104 | Most expensive meal plan (21 meals/week) as baseline |
| Books, course materials, supplies & equipment | $930 | Estimate |
| Personal expenses | $2,496 | Clothes, laundry, other bills |
| **Total COA** | **$92,760** | Before any financial aid; excludes travel allowance (address-specific) |

> Median net price actually paid by an MIT Scholarship recipient (2024–2025): **$10,268**.

### 4.2 Undergraduate financial-aid policy

Source: sfs.mit.edu/.../making-mit-affordable/ (E-U-006).

- **Need-blind + full-need** — for ALL undergraduates, domestic AND international. ("need blind" = ability to pay not considered in admissions; "full need" = 100% of demonstrated need met.)
- **Tuition-free** — beginning 2025–2026, families with annual income **under $200,000** (~80th US percentile) typically attend MIT tuition-free.
- **$0 parent contribution** — for families with income **below $100,000**, parents pay nothing toward the full cost of attendance (tuition + housing + dining + fees + books/personal allowance).
- **Median net price** by family income (2025–2026, MIT Scholarship recipients):

| Income range | Median MIT Scholarship | % of tuition covered | Median net price |
|--------------|------------------------|----------------------|------------------|
| $0–$100,000 | $85,236 | 100% | $0 |
| $100,000–$200,000 | $67,848 | 100% | $19,734 |
| Over $200,000 | $37,750 | 59% | $49,083 |

- **Debt-free**: 88% of MIT students graduate debt-free; for families ≤$140,000 (2024–25) median loan among borrowers was $5,442.
- **Aid budget**: $176M planned in MIT need-based scholarships for 2025–2026 (vs $162M in 2024–2025); 57% of full-time undergraduates received an MIT Scholarship in 2024–2025.

### 4.3 Graduate cost & funding framework

- Most **PhD programs are fully funded** (research assistantship / teaching assistantship + fellowship — covers tuition + stipend).
- Most **master's programs are self-funded** (notably Sloan MBA, MFin, MBAn, MSMS, EMBA, Fellows MBA; Architecture SMArchS/SMBT/SMACT; CEE MEng; ME MEng; SCM; etc.). LGO (Leaders for Global Operations) and a few SM programs offer partial funding.
- Common funding forms: RA (research assistantship), TA (teaching assistantship), fellowship, grant.
- **Application fee**: varies by program (~$75–$150); fee waivers available per program.
- **Cost-of-attendance / stipend-rate / living-expenses pages** for graduate students: sfs.mit.edu/graduate-students/cost-of-attendance/ (P1 follow-up — scrape line items).

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001
field: overview.reconciliation.total_programs_offering_basis
value: 157
source_url: (computed) catalog.mit.edu degree-charts + oge.mit.edu/programs/
source_snippet: "UG majors 55 + minors 17 + graduate degree offerings 85 = 157; matrix cell-sum = 157; rule-5 grouped-table rows = 157"
capture_date: 2026-07-04
evidence_type: computed_reconciliation

# E-U-002
field: undergraduate.application.first_year_overview
value: MIT uses its own application portal; does not award second bachelor's degrees
source_url: https://mitadmissions.org/apply/firstyear/
source_snippet: "MIT does not award second bachelor's degrees—even if you are interested in pursuing a different field of study from the bachelor's degree you hold."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-003
field: undergraduate.deadlines.ea_ra
value: EA Nov 1; RA Jan 5; aid Feb 15; decision May 1
source_url: https://mitadmissions.org/apply/firstyear/deadlines-requirements/
source_snippet: "Early Action (EA) November 1 — All individual application components... Regular Action (RA) January 5 — All individual application components... Admitted students must inform MIT of their enrollment decision by May 1... financial aid should submit materials by February 15"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-004
field: undergraduate.tests.sat_act_and_english
value: SAT/ACT required (no min); TOEFL min 90/rec 100; IELTS min 7/rec 7.5; superscore; self-report
source_url: https://mitadmissions.org/apply/firstyear/tests-scores/
source_snippet: "We require the SAT or the ACT... TOEFL Minimum: 90 Recommended: 100 | IELTS Minimum: 7 Recommended: 7.5... we will consider the highest score achieved in each section [superscore]"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-005
field: undergraduate.cost.coa_2026_2027
value: Tuition $66,720; Student life fee $420; Housing $14,090; Food $8,104; Books/supplies $930; Personal $2,496; Total $92,760
source_url: https://sfs.mit.edu/undergraduate-students/the-cost-of-attendance/coa/
source_snippet: "Cost of attendance for the 2026–2027 academic year ... Tuition $66,720 ... Total $92,760"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-006
field: undergraduate.financial_aid.policy
value: need-blind + full-need (incl. intl); tuition-free <$200k; $0 parent contribution <$100k; 88% debt-free; median net price $10,268
source_url: https://sfs.mit.edu/undergraduate-students/cost-and-affordability/making-mit-affordable/
source_snippet: "need blind and full need for all of our undergraduate students, domestic and international... students from families with an annual income under $200,000... typically attend MIT tuition-free... 88% of MIT students graduate debt-free"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-007
field: undergraduate.programs.majors_count
value: 55 SB majors (catalog degree-charts)
source_url: https://catalog.mit.edu/mit/undergraduate-education/academic-programs/majors/
source_snippet: "Architecture (SB, Course 4)... Physics (SB, Course 8)..." [full 55-row list in Section 1.2]
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-008
field: undergraduate.programs.minors_count
value: 17 minors
source_url: https://catalog.mit.edu/mit/undergraduate-education/academic-programs/minors/
source_snippet: "African and African Diaspora Studies... Women's and Gender Studies" [17 minors]
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-009
field: overview.schools_structure
value: 6 schools + departments (EECS and IDSS shared between Engineering and Schwarzman)
source_url: https://catalog.mit.edu/schools/
source_snippet: "School of Architecture and Planning / School of Engineering / School of Humanities, Arts, and Social Sciences / MIT Sloan School of Management / School of Science" + Schwarzman College of Computing
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-001
field: graduate.programs.directory_total
value: 47 OGE graduate programs; 85 degree-granting offerings
source_url: https://oge.mit.edu/graduate-admissions/programs/
source_snippet: "Aeronautics and Astronautics... Urban Studies and Planning" [47 program links; 29 Master's-listed + 32 Doctoral-listed = 47 distinct]
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-002
field: graduate.tests.institution_code_and_ielts
value: MIT Institution code 3514; IELTS preferred for English proficiency
source_url: https://oge.mit.edu/programs/computational-science-and-engineering-phd/
source_snippet: "GRE scores Institution code: 3514... English proficiency exam scores* IELTS preferred, see website for more information"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-003
field: graduate.programs.aeroastro_degrees
value: SM, PhD, ScD
source_url: https://oge.mit.edu/programs/aeronautics-and-astronautics/
source_snippet: "Master of Science in Aeronautics and Astronautics (SM) | Doctor of Philosophy (PhD) | Doctor of Science (ScD)"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-004
field: graduate.programs.meche_degrees
value: MEng (Manufacturing), SM (MechE/Ocean/Oceanographic/Naval Arch), PhD, ScD (7 offerings)
source_url: https://oge.mit.edu/programs/mechanical-engineering/
source_snippet: "Master of Engineering in Manufacturing (MEng) | Master of Science in Mechanical Engineering (SM) | Master of Science in Ocean Engineering (SM) | ... | Doctor of Philosophy (PhD) | Doctor of Science (ScD)"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-005
field: graduate.programs.sloan_degrees
value: MBA (4 programs: MBA, EMBA, Fellows MBA, LGO), MBAn, MFin, MSMS, PhD
source_url: https://oge.mit.edu/programs/mit-sloan-mba-program/
source_snippet: "MIT Sloan MBA Program... Degrees: Master of Business Administration (MBA)"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-006
field: graduate.programs.cse_phd
value: CSE PhD — 1 standalone + 9 joint specializations under one program entry
source_url: https://oge.mit.edu/programs/computational-science-and-engineering-phd/
source_snippet: "Standalone Program: Doctor of Philosophy (PhD) in Computational Science and Engineering | Joint Program: PhD in Civil Engineering and Computation... [10 total]"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-007
field: graduate.programs.music_tech_degrees
value: SM + MASc (internal applicants only for Fall 2025)
source_url: https://oge.mit.edu/programs/music-technology-and-computation/
source_snippet: "Master's of Science (SM)... Master's of Applied Science (MASc)... *Applications for Fall 2025 are for current MIT undergraduates only."
capture_date: 2026-07-04
evidence_type: official_webpage
# E-G-008
field: graduate.programs.per_program_admissions_sweep
value: 47 OGE program detail pages — per-program deadline, application fee, fee-waiver availability, GRE/GMAT policy, English-proficiency minimums (IELTS/TOEFL/DET), funding model
source_url: https://oge.mit.edu/graduate-admissions/programs/ (hub) + 47 program detail pages oge.mit.edu/programs/<each>/
source_snippet: "[EECS] Deadline: December 1 at 11:59 PM Eastern Time | Fee: $90.00 | Application Requirements: Online application, Essay 1, Essay 2, Three letters of recommendation, Transcripts, English proficiency exam scores | Standardized Tests: GRE Not required | IELTS Minimum score required: 7 | TOEFL Minimum score required: 100 (iBT) | Institute code: 3514 | IELTS exam is preferred over the TOEFL"  [representative snippet; full 47-program dataset in Section 2.4 + uni-cache/schools/mit/grad-program-details.json]
capture_date: 2026-07-04
evidence_type: official_webpage_table

```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: mit-knowledge-base-v2
├── doc: mit-overview                 → chunk: overview (counts, hierarchy, matrix, degree inventory)
├── doc: mit-ug-engineering           → chunk: School of Engineering (majors + minors)
├── doc: mit-ug-science               → chunk: School of Science
├── doc: mit-ug-sap                   → chunk: School of Architecture and Planning
├── doc: mit-ug-shass                 → chunk: SHASS
├── doc: mit-ug-sloan                 → chunk: MIT Sloan UG
├── doc: mit-grad-engineering         → chunk: School of Engineering grad
├── doc: mit-grad-science             → chunk: School of Science grad
├── doc: mit-grad-sap                 → chunk: SAP grad
├── doc: mit-grad-shass               → chunk: SHASS grad
├── doc: mit-grad-sloan               → chunk: MIT Sloan grad
├── doc: mit-grad-schwarzman          → chunk: Schwarzman College of Computing grad
├── doc: mit-ug-deadlines-tests       → chunk: UG application requirements
├── doc: mit-costs-aid                → chunk: costs + financial aid
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "mit-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<SB|Minor|SM|MEng|MArch|MCP|MASc|MBA|MBAn|MFin|MSMS|PhD|ScD>"
  level: undergraduate | graduate
  field_type: overview|counts|hierarchy|programs|deadlines|tests|costs|funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| ✅ ~~P0~~ DONE | Per-program graduate deadlines (47 programs) — 见 Section 2.4 (2026-07-04) | oge.mit.edu/programs/<each>/ |
| ✅ ~~P0~~ DONE | Per-program graduate GRE/IELTS minimums — 见 Section 2.4 (2026-07-04) | oge.mit.edu/programs/<each>/ |
| ✅ ~~P0~~ DONE | Per-program application fee + fee-waiver policy — 见 Section 2.4 (2026-07-04) | oge.mit.edu/programs/<each>/ |
| P1 | Graduate cost-of-attendance line items (stipend rates, living expenses) | sfs.mit.edu/graduate-students/cost-of-attendance/ |
| P1 | OGE institute-wide applying-to-graduate-school global rules page (fee, April-15 resolution) | oge.mit.edu/graduate-admissions/applying-to-graduate-school/ (page returned 404 at capture; locate canonical URL) |
| P1 | UG admissions statistics (acceptance rate, SAT middle 50%) | mitadmissions.org/apply/statistics/ |
| P2 | Per-program "Areas of Research" + faculty (curriculum depth) | oge.mit.edu/programs/<each>/ |
| P2 | Department addresses/phones/email for all 47 grad programs (captured for ~12; sweep the rest) | oge.mit.edu/programs/<each>/ |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | MIT | Stanford | Harvard | NYU |
|-----------|-----|----------|---------|-----|
| Total UG COA (2026–27) | $92,760 | | | |
| Tuition (2026–27) | $66,720 | | | |
| Need-blind (intl?) | Yes (incl. intl) | | | |
| EA deadline | Nov 1 | | | |
| RA/ED deadline | Jan 5 (RA) | | | |
| SAT/ACT required? | Yes | | | |
| TOEFL min / rec | 90 / 100 | | | |
| IELTS min / rec | 7 / 7.5 | | | |
| Tuition-free threshold | <$200k | | | |
| $0 parent contribution threshold | <$100k | | | |
| Median net price paid | $10,268 (2024–25) | | | |
| Grad application fee | ~$75–150 (per program) | | | |
| April-15-equivalent honor date | Yes (CGS Resolution) | | | |
| **Total program count (rule 1, offering basis)** | **157** | | | |
| **School/college count (rule 2)** | **6** | | | |
| **Grad program directory (OGE)** | **47** | | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: mitadmissions.org · oge.mit.edu · sfs.mit.edu · catalog.mit.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (`.accordion-body .field-item` for degree offerings; catalog degree-charts for UG majors/minors)
> **Granularity**: 学院 (school) → 系 (department) → 学位级别 (degree level) → 专业/项目 (program)
> **Reconciliation**: rule-1 total (157) == rule-3 degree-level sum (157) == rule-4 matrix cell-sum (157) == rule-5 grouped-table row count (157). PASS.
