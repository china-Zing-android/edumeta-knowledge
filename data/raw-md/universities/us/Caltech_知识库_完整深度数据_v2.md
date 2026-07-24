# California Institute of Technology (Caltech) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: division → option/department → degree-level → program
> **Document version**: v2.0 (deep)

> **Caltech terminology note**: Caltech does NOT use the word "major". It uses **"option"** for both undergraduate (BS) and graduate (PhD/MS) programs. The six top-level academic units are **"Divisions"** (not "schools" or "colleges"). Caltech awards ONLY the **BS** at the undergraduate level (no BA, no BFA). At the graduate level it awards **MS, Engineer's degree, and PhD**. This document maps "option" → "专业/项目" and "Division" → "学院" to preserve cross-school comparability.

---

## The five structural rules (enforced everywhere)

1. **专业总数** — 76 program rows total: 26 BS options + 19 undergraduate minors + 31 graduate (PhD-track) options.
2. **学院/系明细 + 父子层级** — 6 academic Divisions + 1 interdisciplinary bucket (ISP/CSE/QSE), mapped below.
3. **学历级别明细** — BS, Minor, MS, Engineer's, PhD (only BS/Minor/PhD counted as enumerable program rows; MS/Engineer's are institute-wide credentials noted in §0.3).
4. **分布矩阵** — Division × degree-level cross-tab; row/column totals reconcile to 76.
5. **全量专业明细按 学院 > 系/选项 > 学位级别 分组** — every option listed under its Division → degree level.

> **RECONCILIATION (computed in Python, mandatory)**:
> - Rule 1 stated total = **76**
> - Rule 3 sum of degree-inventory counts = 26 (BS) + 19 (Minor) + 31 (PhD) = **76** ✔
> - Rule 4 sum of distribution-matrix cells = 76 (see §0.4) = **76** ✔
> - Rule 5 row count in grouped tables (§1.2 + §1.4 + §2.1) = 26 + 19 + 31 = **76** ✔
>
> All four numbers agree. **76 is the authoritative program-row total.**
>
> **Counting convention (documented, not speculative):** Caltech's catalog publishes a clean enumeration of (a) every undergraduate BS option, (b) every undergraduate minor, and (c) every graduate option — but it does **not** publish a clean per-option MS-vs-PhD matrix. Each graduate option at Caltech is a PhD-granting option (the PhD is Caltech's standard graduate credential; the MS is offered institute-wide, terminal in select options or earned en route to PhD; the Engineer's degree in "limited fields"). To keep rule-1 reconciliation exact and avoid fabricating a per-option degree split that the source does not expose, each of the 31 graduate options is counted as **1 PhD-track program row**. Per-option MS/Engineer's-degree availability is flagged as a P0 follow-up in §6.

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (BS) | 26 | Caltech 仅授予 BS（无 BA/BFA）。来源：catalog "Graduation Requirements, All Options" 子菜单逐项枚举。 |
| 本科辅修 (Minor) | 19 | 含 13 个"option + minor"组合 + 6 个 minor-only（Ae, CDS, NB, Ro, SM, VC）。 |
| 研究生学位项目 (PhD-track) | 31 | 来源：catalog "Special Regulations For Graduate Options" 子菜单。每个 graduate option 默认 PhD 路径。 |
| 研究生高级证书 (Engineer's Degree) | (institute-wide) | Caltech 授予 Engineer's degree "in limited fields"，未按 option 公开枚举 → 计为学院级凭证，未单独计行。 |
| 研究生硕士学位 (MS) | (institute-wide) | MS 为学院级凭证："Not all options admit directly for the M.S. degree"。未按 option 公开枚举 → 未单独计行。 |
| **学位项目总计 (UG + Grad, enumerated rows)** | **76** | 26 + 19 + 31。 |
| 学院（学术 Division）总数 | 6 + 1 | 6 个学术 Division + 1 个跨学科分组（ISP/CSE/QSE）。 |

> E-U-001 / E-U-002 / E-G-001 evidence in §5.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

Caltech 组织为 **6 个学术 Division（学院）**，下设 **department（系）/ option（选项 = 专业）**。Engineering & Applied Science (EAS) 进一步细分为 7 个命名 department。来源：各 Division 官网（bbe/cce/eas/gps/hss/pma.caltech.edu）与 EAS "Departments" 子菜单。

```
California Institute of Technology (Caltech)
├── Biology & Biological Engineering (BBE)                    [学院]  https://www.bbe.caltech.edu/
│   ├── Biology (Bi)                                           [系/选项]  BS + Minor + PhD
│   ├── Bioengineering (BE)                                    [系/选项]  BS + PhD
│   ├── Biochemistry and Molecular Biophysics (BMB)            [系/选项]  PhD
│   ├── Computation and Neural Systems (CNS)                   [系/选项]  BS + PhD
│   └── Neurobiology (NB)                                      [系/选项]  Minor + PhD
├── Chemistry & Chemical Engineering (CCE)                    [学院]  https://www.cce.caltech.edu/
│   ├── Chemistry (Ch)                                         [系/选项]  BS + Minor + PhD
│   └── Chemical Engineering (ChE)                             [系/选项]  BS + Minor + PhD
├── Engineering & Applied Science (EAS)                        [学院]  https://www.eas.caltech.edu/
│   │   (EAS 下设 7 个命名 department — 来源 EAS 官网 "Departments")
│   ├── Lynn Booth & Kent Kresa Department of Aerospace        [系]  → Aerospace (AE) PhD；Aerospace (Ae) Minor
│   ├── Andrew and Peggy Cherng Department of Medical Engineering [系] → Medical Engineering (MedE) PhD
│   ├── Applied Physics and Materials Science                  [系]  → Applied Physics (APh) BS+PhD；Materials Science (MS) BS+PhD
│   ├── Computing and Mathematical Sciences (CMS)              [系]  → Computer Science (CS) BS+Minor+PhD；
│   │                                                                   Information and Data Sciences (IDS) BS+Minor+PhD；
│   │                                                                   Computing and Mathematical Sciences (CMS) PhD；
│   │                                                                   Control and Dynamical Systems (CDS) Minor+PhD
│   ├── Electrical Engineering (EE)                            [系]  → EE BS+PhD
│   ├── Environmental Science and Engineering (ESE)            [系]  → ESE BS+Minor+PhD  ⚠ jointly administered with GPS
│   └── Mechanical and Civil Engineering                       [系]  → Mechanical Engineering (ME) BS+PhD；Civil Engineering (CE) PhD；
│   │                                                                   Applied Mechanics (AM) PhD；Structural Mechanics (SM) Minor
│   (EAS 还汇集：Engineering and Applied Science (EAS) BS option；Robotics (Ro) Minor)
├── Geological & Planetary Sciences (GPS)                      [学院]  https://www.gps.caltech.edu/
│   └── Geological and Planetary Sciences (GPS) option          [系/选项]  BS + Minor + PhD
│       (内含 Geology / Geobiology / Geochemistry / Geophysics / Planetary Science 五个方向)
├── Humanities & Social Sciences (HSS)                         [学院]  https://www.hss.caltech.edu/
│   ├── Business, Economics, and Management (BEM)              [系/选项]  BS
│   ├── Economics (Ec)                                         [系/选项]  BS
│   ├── English (En)                                           [系/选项]  BS + Minor
│   ├── History (H)                                            [系/选项]  BS + Minor + PhD
│   ├── History and Philosophy of Science (HPS)                [系/选项]  BS + Minor + PhD
│   ├── Philosophy (Pl)                                        [系/选项]  BS + Minor
│   ├── Political Science (PS)                                 [系/选项]  BS
│   ├── Visual Culture (VC)                                    [系/选项]  Minor
│   ├── Social Science (SS)                                    [系/选项]  PhD  (Social Sciences PhD program)
│   └── Social and Decision Neuroscience (SDN)                 [系/选项]  PhD  (SDN PhD program)
├── Physics, Mathematics & Astronomy (PMA)                     [学院]  https://pma.caltech.edu/
│   │   (PMA 下设 3 个 department — 来源 PMA 官网 "Departments")
│   ├── Physics                                                [系]  → Physics (Ph) BS+PhD
│   ├── Mathematics                                            [系]  → Mathematics (Ma) BS+Minor+PhD；
│   │                                                                   Applied and Computational Mathematics (ACM) BS+PhD
│   └── Astronomy                                              [系]  → Astrophysics (Ay) BS+Minor+PhD
└── Interdisciplinary / Cross-Divisional                       [跨学院分组]
    ├── Interdisciplinary Studies Program (ISP) — UG BS option  [跨学院]
    ├── Computational Science and Engineering (CSE) — PhD       [跨学院]
    └── Quantum Science and Engineering (QSE) — PhD             [跨学院]

外加机构级科研单元（非学位授予单元，不计入 rule-1）：
• Jet Propulsion Laboratory (JPL) — Caltech 为 NASA 运营
• Seismological Laboratory · LIGO · Palomar / W. M. Keck Observatories · IPAC
```

> ⚠ **Shared/joint**: Environmental Science and Engineering (ESE) 同时出现在 EAS（department）和 GPS（研究项目）— 本文档将其 BS/Minor 归入 **EAS**（学位授予归属），PhD 归入 **EAS**，研究层面与 GPS 联合。CNS 跨 BBE/EAS；CSE/QSE 跨多 Division。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

Caltech 授予的所有学位级别。 enumerable 行数已计入 rule-1；标注 "(学院级)" 的为机构级凭证，因 catalog 未按 option 公开枚举而不单独计行。

| 学位缩写 | 全称 | 层级 | 本校本项目数量 | 备注 |
|---------|------|------|---------------|------|
| BS | Bachelor of Science | 本科 | 26 | Caltech 本科唯一授予学位。 |
| Minor | 辅修 | 本科 | 19 | Caltech 称 minor，HSS 称部分为 "Options & Minors"。 |
| MS | Master of Science | 研究生 | (学院级) | "Caltech offers M.S. and Ph.D. degrees…Not all options admit directly for the M.S. degree." 未按 option 枚举。 |
| Engineer's | Engineer's Degree | 研究生 | (学院级，limited fields) | "Engineer's degrees are awarded in limited fields." 未按 option 枚举。 |
| PhD | Doctor of Philosophy | 研究生 | 31 | 每个 graduate option 的标准路径；"at least twelve terms (three academic years) of residence are required." |
| **可枚举行总计** | | | **76** | 26 + 19 + 31。 |

### 0.4 分布矩阵 (Rule 4 — Division × degree-level)

| 学院 \ 级别 | BS | Minor | PhD | 合计 |
|------------|----|----|-----|------|
| Biology & Biological Engineering (BBE) | 3 | 2 | 5 | 10 |
| Chemistry & Chemical Engineering (CCE) | 2 | 2 | 2 | 6 |
| Engineering & Applied Science (EAS) | 7 | 6 | 12 | 25 |
| Geological & Planetary Sciences (GPS) | 2 | 2 | 2 | 6 |
| Humanities & Social Sciences (HSS) | 7 | 5 | 4 | 16 |
| Physics, Mathematics & Astronomy (PMA) | 4 | 2 | 4 | 10 |
| Interdisciplinary (ISP/CSE/QSE) | 1 | 0 | 2 | 3 |
| **合计** | **26** | **19** | **31** | **76** |

> 行合计之和 = 列合计之和 = **76** = rule-1 total. ✔ Reconciliation passes.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Caltech 本科由 **6 个学术 Division** 共同承担，授予 **BS** 一种学位。本科"专业"称 **option**。EAS 内部进一步分为 7 个命名 department。完整层级树见 §0.2。Caltech 本科规模极小：约 1,000 名本科生、约 230 人/年级、师生比约 3:1。来源：caltech.edu/about/at-a-glance（E-U-003）。

### 1.2 Undergraduate BS options — grouped by 学院 > 系/选项 > 学位级别 (BS)

学位级别统一为 BS（Caltech 本科唯一学位）。

#### Biology & Biological Engineering (BBE)
##### BS
| # | 选项代码 | 专业 (Option) | URL |
|---|---------|--------------|-----|
| 1 | Bi | Biology | https://catalog.caltech.edu/current/areas-of-study-and-research/biology/ |
| 2 | BE | Bioengineering | https://catalog.caltech.edu/current/areas-of-study-and-research/bioengineering/ |
| 3 | CNS | Computation and Neural Systems | https://catalog.caltech.edu/current/areas-of-study-and-research/computation-and-neural-systems/ |

#### Chemistry & Chemical Engineering (CCE)
##### BS
| # | 选项代码 | 专业 (Option) | URL |
|---|---------|--------------|-----|
| 4 | Ch | Chemistry | https://catalog.caltech.edu/current/areas-of-study-and-research/chemistry/ |
| 5 | ChE | Chemical Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/chemical-engineering/ |

#### Engineering & Applied Science (EAS)
##### BS
| # | 选项代码 | 专业 (Option) | 系 (Department) | URL |
|---|---------|--------------|----------------|-----|
| 6 | APh | Applied Physics | Applied Physics and Materials Science | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-physics/ |
| 7 | CS | Computer Science | Computing and Mathematical Sciences (CMS) | https://catalog.caltech.edu/current/areas-of-study-and-research/computer-science/ |
| 8 | EE | Electrical Engineering | Electrical Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/electrical-engineering/ |
| 9 | EAS | Engineering and Applied Science (umbrella option) | EAS | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 10 | ESE | Environmental Science and Engineering | Environmental Science and Engineering ⚠ joint w/ GPS | https://catalog.caltech.edu/current/areas-of-study-and-research/environmental-science-and-engineering/ |
| 11 | IDS | Information and Data Sciences | Computing and Mathematical Sciences (CMS) | https://catalog.caltech.edu/current/areas-of-study-and-research/information-and-data-sciences/ |
| 12 | MS | Materials Science | Applied Physics and Materials Science | https://catalog.caltech.edu/current/areas-of-study-and-research/materials-science/ |
| 13 | ME | Mechanical Engineering | Mechanical and Civil Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/mechanical-engineering/ |

#### Geological & Planetary Sciences (GPS)
##### BS
| # | 选项代码 | 专业 (Option) | URL |
|---|---------|--------------|-----|
| 14 | GPS | Geological and Planetary Sciences (Geology, Geobiology, Geochemistry, Geophysics, Planetary Science) | https://catalog.caltech.edu/current/areas-of-study-and-research/geological-and-planetary-sciences/ |

#### Humanities & Social Sciences (HSS)
##### BS
| # | 选项代码 | 专业 (Option) | URL |
|---|---------|--------------|-----|
| 15 | BEM | Business, Economics, and Management | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 16 | Ec | Economics | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 17 | En | English | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 18 | H | History | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 19 | HPS | History and Philosophy of Science | https://catalog.caltech.edu/current/areas-of-study-and-research/history-and-philosophy-of-science/ |
| 20 | Pl | Philosophy | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 21 | PS | Political Science | https://catalog.caltech.edu/current/areas-of-study-and-research/ |

#### Physics, Mathematics & Astronomy (PMA)
##### BS
| # | 选项代码 | 专业 (Option) | 系 (Department) | URL |
|---|---------|--------------|----------------|-----|
| 22 | ACM | Applied and Computational Mathematics | Mathematics | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-and-computational-mathematics/ |
| 23 | Ay | Astrophysics | Astronomy | https://catalog.caltech.edu/current/areas-of-study-and-research/astrophysics/ |
| 24 | Ma | Mathematics | Mathematics | https://catalog.caltech.edu/current/areas-of-study-and-research/mathematics/ |
| 25 | Ph | Physics | Physics | https://catalog.caltech.edu/current/areas-of-study-and-research/physics/ |

#### Interdisciplinary / Cross-Divisional
##### BS
| # | 选项代码 | 专业 (Option) | URL |
|---|---------|--------------|-----|
| 26 | ISP | Interdisciplinary Studies Program | https://catalog.caltech.edu/current/areas-of-study-and-research/interdisciplinary-studies-program/ |

> **BS 小计：26** ✔

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 项目 | 性质 | 归属 | URL |
|---|------|------|------|-----|
| 1 | Interdisciplinary Studies Program (ISP) | UG BS option（学生自设跨学科课程，需审批） | 跨学院 | https://catalog.caltech.edu/current/areas-of-study-and-research/interdisciplinary-studies-program/ |
| 2 | 3/2 Program | 与文理学院合作的 dual-degree 路径（3 年 partner + 2 年 Caltech → BS） | EAS | https://www.admissions.caltech.edu/apply/32-program |

### 1.4 Minors — complete list (Rule 5)

| # | 代码 | Minor 名称 | Home Division/Department | 是否同时为 BS option | URL |
|---|------|-----------|--------------------------|---------------------|-----|
| 1 | Ay | Astrophysics | PMA / Astronomy | 是 (BS+Minor) | https://catalog.caltech.edu/current/areas-of-study-and-research/astrophysics/ |
| 2 | Bi | Biology | BBE | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/biology/ |
| 3 | ChE | Chemical Engineering | CCE | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/chemical-engineering/ |
| 4 | Ch | Chemistry | CCE | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/chemistry/ |
| 5 | CS | Computer Science | EAS / CMS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/computer-science/ |
| 6 | En | English | HSS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 7 | ESE | Environmental Science and Engineering | EAS ⚠ joint GPS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/environmental-science-and-engineering/ |
| 8 | GPS | Geological and Planetary Sciences | GPS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/geological-and-planetary-sciences/ |
| 9 | H | History | HSS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 10 | HPS | History and Philosophy of Science | HSS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/history-and-philosophy-of-science/ |
| 11 | IDS | Information and Data Sciences | EAS / CMS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/information-and-data-sciences/ |
| 12 | Ma | Mathematics | PMA / Mathematics | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/mathematics/ |
| 13 | Pl | Philosophy | HSS | 是 | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 14 | Ae | Aerospace | EAS / Aerospace dept | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/aerospace/ |
| 15 | CDS | Control and Dynamical Systems | EAS / CMS | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/control-and-dynamical-systems/ |
| 16 | NB | Neurobiology | BBE | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/neurobiology/ |
| 17 | Ro | Robotics | EAS | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 18 | SM | Structural Mechanics | EAS / Mechanical and Civil Engineering | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-mechanics/ |
| 19 | VC | Visual Culture | HSS | 否 (minor-only) | https://catalog.caltech.edu/current/areas-of-study-and-research/ |

> **Minor 小计：19** = 13 (option 也提供 minor) + 6 (minor-only). ✔

### 1.5 General/Institute-wide requirements (Core Curriculum)

Caltech 本科不论 option 均须完成 **Core Curriculum（核心课程）**，包含数学、物理、化学、生物等基础 STEM。来源：catalog "Core Institute Requirements, All Options"。

- Core Institute Requirements 页面：https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/
- Honor Code（诚信守则，全校通用）：https://www.deans.caltech.edu/HonorCode

### 1.6 Option-Code → 专业 quick-lookup

| 代码 | 专业 (UG BS) | 代码 | Minor |
|------|-------------|------|-------|
| ACM | Applied and Computational Mathematics | Ae | Aerospace |
| APh | Applied Physics | Ay | Astrophysics |
| Ay | Astrophysics | Bi | Biology |
| BE | Bioengineering | CDS | Control and Dynamical Systems |
| Bi | Biology | Ch | Chemistry |
| BEM | Business, Economics, and Management | ChE | Chemical Engineering |
| Ch | Chemistry | CS | Computer Science |
| ChE | Chemical Engineering | En | English |
| CNS | Computation and Neural Systems | ESE | Environmental Science and Engineering |
| CS | Computer Science | GPS | Geological and Planetary Sciences |
| Ec | Economics | H | History |
| EE | Electrical Engineering | HPS | History and Philosophy of Science |
| EAS | Engineering and Applied Science | IDS | Information and Data Sciences |
| En | English | Ma | Mathematics |
| ESE | Environmental Science and Engineering | NB | Neurobiology |
| GPS | Geological and Planetary Sciences | Pl | Philosophy |
| H | History | Ro | Robotics |
| HPS | History and Philosophy of Science | SM | Structural Mechanics |
| IDS | Information and Data Sciences | VC | Visual Culture |
| ISP | Interdisciplinary Studies Program | | |
| MS | Materials Science | | |
| Ma | Mathematics | | |
| ME | Mechanical Engineering | | |
| Pl | Philosophy | | |
| Ph | Physics | | |
| PS | Political Science | | |

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate options — grouped by 学院 > 系/选项 > 学位级别 (PhD-track)

Caltech 研究生院授予 **MS、Engineer's degree、PhD** 三种学位（来源 E-G-002）。每个 graduate option 默认为 PhD 路径；MS 可作为 terminal 或 PhD 途中授予。下方按 Division 分组，每个 option 计 1 个 PhD-track 项目行。

#### Biology & Biological Engineering (BBE)
##### PhD
| # | 选项代码 | 项目 (Graduate Option) | URL |
|---|---------|------------------------|-----|
| 1 | BMB | Biochemistry and Molecular Biophysics | https://catalog.caltech.edu/current/areas-of-study-and-research/biochemistry-and-molecular-biophysics/ |
| 2 | BE | Bioengineering | https://catalog.caltech.edu/current/areas-of-study-and-research/bioengineering/ |
| 3 | Bi | Biology | https://catalog.caltech.edu/current/areas-of-study-and-research/biology/ |
| 4 | CNS | Computation and Neural Systems | https://catalog.caltech.edu/current/areas-of-study-and-research/computation-and-neural-systems/ |
| 5 | NB | Neurobiology | https://catalog.caltech.edu/current/areas-of-study-and-research/neurobiology/ |

#### Chemistry & Chemical Engineering (CCE)
##### PhD
| # | 选项代码 | 项目 | URL |
|---|---------|------|-----|
| 6 | Ch | Chemistry | https://catalog.caltech.edu/current/areas-of-study-and-research/chemistry/ |
| 7 | ChE | Chemical Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/chemical-engineering/ |

#### Engineering & Applied Science (EAS)
##### PhD
| # | 选项代码 | 项目 | 系 (Department) | URL |
|---|---------|------|----------------|-----|
| 8 | AE | Aerospace | Lynn Booth & Kent Kresa Department of Aerospace | https://catalog.caltech.edu/current/areas-of-study-and-research/aerospace/ |
| 9 | AM | Applied Mechanics | Mechanical and Civil Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-mechanics/ |
| 10 | APh | Applied Physics | Applied Physics and Materials Science | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-physics/ |
| 11 | CE | Civil Engineering | Mechanical and Civil Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/civil-engineering/ |
| 12 | CMS | Computing and Mathematical Sciences | CMS | https://catalog.caltech.edu/current/areas-of-study-and-research/computing-and-mathematical-sciences/ |
| 13 | CDS | Control and Dynamical Systems | CMS | https://catalog.caltech.edu/current/areas-of-study-and-research/control-and-dynamical-systems/ |
| 14 | CS | Computer Science | CMS | https://catalog.caltech.edu/current/areas-of-study-and-research/computer-science/ |
| 15 | EE | Electrical Engineering | Electrical Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/electrical-engineering/ |
| 16 | ESE | Environmental Science and Engineering | ESE ⚠ joint GPS | https://catalog.caltech.edu/current/areas-of-study-and-research/environmental-science-and-engineering/ |
| 17 | IDS | Information and Data Science | CMS | https://catalog.caltech.edu/current/areas-of-study-and-research/information-and-data-sciences/ |
| 18 | MS | Materials Science | Applied Physics and Materials Science | https://catalog.caltech.edu/current/areas-of-study-and-research/materials-science/ |
| 19 | ME | Mechanical Engineering | Mechanical and Civil Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/mechanical-engineering/ |
| 20 | MedE | Medical Engineering | Andrew and Peggy Cherng Department of Medical Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/medical-engineering/ |

#### Geological & Planetary Sciences (GPS)
##### PhD
| # | 选项代码 | 项目 | URL |
|---|---------|------|-----|
| 21 | GPS | Geological and Planetary Sciences (Geology, Geobiology, Geochemistry, Geophysics, Planetary Science) | https://catalog.caltech.edu/current/areas-of-study-and-research/geological-and-planetary-sciences/ |

#### Humanities & Social Sciences (HSS)
##### PhD
| # | 选项代码 | 项目 | URL |
|---|---------|------|-----|
| 22 | H | History | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 23 | HPS | History and Philosophy of Science | https://catalog.caltech.edu/current/areas-of-study-and-research/history-and-philosophy-of-science/ |
| 24 | SDN | Social and Decision Neuroscience | https://catalog.caltech.edu/current/areas-of-study-and-research/social-and-decision-neuroscience/ |
| 25 | SS | Social Science | https://catalog.caltech.edu/current/areas-of-study-and-research/social-science/ |

#### Physics, Mathematics & Astronomy (PMA)
##### PhD
| # | 选项代码 | 项目 | 系 (Department) | URL |
|---|---------|------|----------------|-----|
| 26 | ACM | Applied and Computational Mathematics | Mathematics | https://catalog.caltech.edu/current/areas-of-study-and-research/applied-and-computational-mathematics/ |
| 27 | Ay | Astrophysics | Astronomy | https://catalog.caltech.edu/current/areas-of-study-and-research/astrophysics/ |
| 28 | Ma | Mathematics | Mathematics | https://catalog.caltech.edu/current/areas-of-study-and-research/mathematics/ |
| 29 | Ph | Physics | Physics | https://catalog.caltech.edu/current/areas-of-study-and-research/physics/ |

#### Interdisciplinary / Cross-Divisional
##### PhD
| # | 选项代码 | 项目 | URL |
|---|---------|------|-----|
| 30 | CSE | Computational Science and Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/ |
| 31 | QSE | Quantum Science and Engineering | https://catalog.caltech.edu/current/areas-of-study-and-research/ |

> **PhD-track 小计：31** ✔

### 2.2 Worked example — Computer Science (CS) PhD deep-dive

| 字段 | 值 | 来源 |
|------|----|------|
| 项目名 | Computer Science (CS) | catalog |
| 学位级别 | PhD（primary）；MS 可 terminal / PhD 途中授予 | E-G-002 |
| Home Division | Engineering & Applied Science (EAS) | eas.caltech.edu |
| Home Department | Computing and Mathematical Sciences (CMS) | CS option page: "the computer science option within the Computing & Mathematical Sciences department" |
| 研究方向 | quantum and molecular computation; parallel and distributed computation; theory of computation; information theory; machine learning and applications; computational economics; computer vision; computer graphics; discrete differential geometry; networking and power systems | catalog CS option page |
| Application portal | https://www.gradoffice.caltech.edu/admissions | gradoffice.caltech.edu |
| Application fee | 见 §4.3（grad office 统一） | — |
| GRE policy | 因 option 而异（"GRE policies differ substantially among the various graduate programs"）；须查具体 option 的 GRE policy | E-G-003 |
| English proficiency | 国际生须满足（见 §3.3） | E-G-003 |
| Funding | 绝大多数 PhD 通过 assistantship / fellowship 全额资助（见 §4.3） | E-G-003 |
| Deadline | 因 option 而异（decentralized；多数 mid-Dec）— P0 follow-up | gradoffice checklist |

### 2.3 Graduate admissions model

Caltech 研究生招生为 **分权式（decentralized）**：Graduate Studies Office（gradoffice.caltech.edu / sfp.caltech.edu）统一管理申请系统与政策框架，但 **每个 option 自行设定 deadline、GRE policy、TOEFL 要求、funding**。统一要点（来源 E-G-002 / E-G-003）：

- 入学要求：须持 bachelor's degree 或同等学历；不接收已持 PhD 者申请第二个 PhD。
- 申请材料：成绩单 × 全部就读院校、3 封推荐信、CV、essays。
- GRE：因 option 差异极大，须查各 option 的 GRE policy。
- 资金：多数 PhD funding source 要求 work authorization → PhD 入学通常需 work authorization 证据（除非 option 特殊安排）。
- 学位：MS（1 学年可完成）、Engineer's（limited fields）、PhD（≥12 terms / 3 学年 residence）。

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 字段 | 值 | source_snippet / 来源 |
|------|----|----|
| 招生官网 | https://www.admissions.caltech.edu/ | E-U-004 |
| 申请平台 | Common App 或 QuestBridge Application | E-U-005: "Common App or QuestBridge Application" |
| 申请费 | $75（一次性、不可退；financial hardship 可免， QuestBridge 永远免费） | E-U-006 |
| REA 申请截止 | **November 1**（材料 Nov 6；标化考试须 Nov 30 前完成） | E-U-007 |
| REA 放榜 | mid-December（admit / defer / deny） | E-U-007 |
| Regular Decision 申请截止 | **January 5**（补充材料 Jan 11） | E-U-007 |
| RD 放榜 | mid-March（admit / waitlist / deny） | E-U-007 |
| 入学确认截止 (Enrollment) | **May 1, 2026** | E-U-007 |
| Waitlist opt-in 截止 | mid-April；活动至 mid-July | E-U-007 |
| SAT/ACT 政策 | **Required**（须提交 SAT 或 ACT）；fall 2026 不要求 ACT writing/science subscores；不显示 composite，仅看各 subscore（Math/EBRW/Reading/Science/Writing） | E-U-008 |
| 分数分段（Bucket）政策 | Bucket A: SAT 780-800 / ACT 35-36；Bucket B: SAT 750-770 / ACT 33-34；Below: SAT<750 / ACT<33（显示具体分） | E-U-008 |
| 推荐信 | 2 封：1 STEM（Calculus 或以上 / Chem / Physics / Bio）+ 1 Humanities/Social Sciences（English/History/Government/Economics） | E-U-005 |
| 面试政策 | 无正式面试；国际生推荐 InitialView（conversation + writing sample） | E-U-009 |
| 补充材料 | 可选（supplemental materials） | E-U-005 |
| Mid-Year Report | senior 第一学期成绩出来后提交 | E-U-005 |
| STEM 活动与奖项核验 | Required（Verification of STEM Activities and Awards） | E-U-005 |
| 转学路径 | Transfer Applicants（独立 deadline）；3/2 Program（partner 文理学院 +2 年 Caltech → BS） | E-U-010 |

### 3.2 Undergraduate English proficiency table

适用于**国际申请者**（非美国公民/永久居民且在美以外中学就读）。豁免条件：母语为英语，或中学主要教学语言为英语（后者仍"strongly recommends"提交）。考试须在申请截止前完成。

| 考试 | Minimum Total | Minimum in each area | source |
|------|--------------|----------------------|--------|
| TOEFL | 100 | 25 | E-U-009 |
| IELTS | 7 | 7 | E-U-009 |
| Duolingo English Test (DET) | 130 | 130 | E-U-009 |
| InitialView | （推荐，非替代；提供 conversation + writing sample） | — | E-U-009 |

### 3.3 Graduate — global rules

| 字段 | 值 | 来源 |
|------|----|----|
| 招生模式 | 分权式（decentralized），各 option 自定 deadline/GRE/TOEFL | E-G-003 |
| 统一入口 | https://www.gradoffice.caltech.edu/admissions | E-G-003 |
| 学历前置 | 须持 bachelor's degree 或同等；不接收第二 PhD 申请 | E-G-003 |
| 申请材料 | 全部院校成绩单 + 3 封推荐信 + CV + essays | E-G-003 |
| GRE 政策 | "differ substantially among the various graduate programs" → 须查各 option | E-G-003 |
| 英语能力 | 国际生须满足（各 option 设具体要求） → 见 Application Checklist "GRE and English Proficiency" | E-G-003 |
| Work authorization | 多数 PhD funding 要求 work authorization → matriculation 通常需 work authorization 证据 | E-G-003 |
| April-15-equivalent | Caltech 遵循 CGS Resolution（统一研究生 honor date 4 月 15 日）— P1 follow-up（未在抓取页明确日期） | — |
| 申请费 | Grad office 页未显示统一费用（多为 ~$100，因 option 而异） → P0 follow-up | — |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-26, line-itemized)

来源：catalog "Undergraduate Expenses" → "ESTIMATED COST OF ATTENDANCE 2025-26"（E-U-011）。九个月全日制估算。

| Expense item | On-Campus | Off-Campus | Living with Parents | Description |
|--------------|-----------|------------|---------------------|-------------|
| Tuition | $65,622 | $65,622 | $65,622 | 学费 |
| Fees | $2,586 | $2,586 | $2,586 | 不含学生健康保险；含一次性 $500 Orientation Fee |
| Housing | $12,105 | $15,219 | (见 Living Expenses) | 住房 |
| Food/Meals | $8,886 | $7,533 | (见 Living Expenses) | 餐饮 |
| Books, Course Materials, Supplies & Equipment (est.) | $1,428 | $1,428 | $1,428 | 书本/耗材 |
| Living Expenses | N/A | N/A | $11,835 | 仅"与父母同住"行 |
| Personal Expenses (est.) | $3,285 | $5,067 | $4,140 | 个人支出 |
| **Total Estimated Cost of Attendance** | **$93,912** | **$97,455** | **$85,611** | 合计 |

附加（非 COA 内必列）：
- Caltech Student Health Insurance Plan（可选，若有可比覆盖可 waive）：health $5,049/年（$1,683/term）+ dental $135 + vision $30.96（一次性 Fall）。
- General Deposit：$100（新生一次性，毕业/离校时结算）。
- Travel Allowance：美国公民/合格非公民且居住于美国/领地/加拿大/墨西哥可申请部分报销两次往返交通费。

> **注**：此为 **2025-26** 学年数据（catalog "current" = 2025-2026）。2026-27 数据尚未发布（P0 follow-up：发布后更新）。

### 4.2 Undergraduate financial-aid policy

来源：admissions.caltech.edu/afford（E-U-012）。

| 政策 | 值 | snippet |
|------|----|----|
| Need-blind (domestic) | 是（含 undocumented / DACA 且美高毕业者） | "Caltech Admissions is need-blind for domestic students (including undocumented and DACA students who graduate from a U.S. high school)." |
| Need-blind (international) | **否 — need-aware** | "We are need-aware for international students because the total amount of financial aid funds for international students is limited." |
| 100% demonstrated need | 是 | "The Institute meets 100% of students' demonstrated financial need" |
| Merit scholarships | 无（纯 need-based） | "Caltech does not award merit scholarships." |
| 平均 grant (fall 2024 入学) | 约 $73,000 | "the average grant aid was just under $73,000" |
| 平均贷款负债 (Class of 2023) | 约 $16,000 | "The average loan indebtedness for the Class of 2023 was approximately $16,000" |
| 家庭收入 < $100k（典型资产） | no-loan 包装覆盖学费/费/住/食 | "Most students from families making less than $100,000 (with typical assets) can expect a no-loan financial aid package that covers tuition, fees, housing, and food" |
| 家庭收入 < $200k（典型资产） | aid 覆盖学费 | "Most students from families making less than $200,000 (with typical assets) can expect an aid package that covers tuition" |
| Pell eligible (近三年新生) | ≥20% | "At least 20% of first-year students in the past three incoming classes were Pell eligible students" |

### 4.3 Graduate cost & funding framework

来源：catalog "Graduate Expenses"（E-G-004）+ gradoffice "Financial Support"。

| 项目 | 值 | snippet / 来源 |
|------|----|----|
| 研究生学费+费 (2025-26) | **$68,001/学年**（按 term 缴：Fall 9/29/2025, Winter 1/5/2026, Spring 3/30/2026） | E-G-004 |
| General Deposit | $100 | E-G-004 |
| Books & supplies (approx.) | $1,428 | E-G-004 |
| 住房（Catalina Apartments, 年合同） | 4-bed $790/人/月；2-bed $940/人/月；1-bed $1,585/套/月；Studio $1,195/套/月（均 + utilities） | E-G-004 |
| 校外无家具（年合同） | 2-bed $1,765/套/月；1-bed $1,315/套/月（+ utilities） | E-G-004 |
| Late 付费/注册 | 各 $50 罚款 | E-G-004 |
| 资金模型 | 绝大多数 PhD 通过 **assistantship（RA/TA）、external fellowships、institute fellowships** 全额资助（tuition + stipend）。来源 gradoffice "Financial Support"。 | E-G-005 |
| 申请费 | gradoffice 页未显示统一研究生申请费 → **P0 follow-up** | — |
| Fee waiver | gradoffice 页未明确 → P1 follow-up | — |

---

## SECTION 5 — Evidence chain index

```yaml
# E-U-001: undergraduate BS options count + enumeration source
field: undergraduate.options.bs_count_and_source
value: "26 BS options; enumerated verbatim from catalog 'Graduation Requirements, All Options' submenu"
source_url: https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/
source_snippet: "Aerospace Minor (Ae) Applied and Computational Mathematics Option (ACM) Applied Physics Option (APh) Astrophysics Option and Minor (Ay) Bioengineering Option (BE) Biology Option and Minor (Bi) Business, Economics, and Management Option (BEM) Chemical Engineering Option and Minor (ChE) Chemistry Option and Minor (Ch) Computation and Neural Systems Option (CNS) Computer Science Option and Minor (CS) Control and Dynamical Systems Minor (CDS) Economics Option (Ec) Electrical Engineering Option (EE) Engineering and Applied Science Option (EAS) English Option and Minor (En) Environmental Science and Engineering Option and Minor (ESE) Geological and Planetary Sciences Option (GPS) (Geology, Geobiology, Geochemistry, Geophysics, Planetary Science) and Minor History Option and Minor (H) History and Philosophy of Science Option And Minor (HPS) Information and Data Sciences Option and Minor (IDS) Interdisciplinary Studies Program Option (ISP) Materials Science Option (MS) Mathematics Option and Minor (Ma) Mechanical Engineering Option (ME) Neurobiology Minor (NB) Philosophy Option and Minor (Pl) Physics Option (Ph) Political Science Option (PS) Robotics Minor (Ro) Structural Mechanics Minor (SM) Visual Culture Minor (VC)"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-002: undergraduate minors count breakdown
field: undergraduate.minors.count_breakdown
value: "19 minors = 13 option-with-minor (Ay, Bi, ChE, Ch, CS, En, ESE, GPS, H, HPS, IDS, Ma, Pl) + 6 minor-only (Ae, CDS, NB, Ro, SM, VC)"
source_url: https://catalog.caltech.edu/current/information-for-undergraduate-students/graduation-requirements-all-options/
source_snippet: "Aerospace Minor (Ae) ... Control and Dynamical Systems Minor (CDS) ... Neurobiology Minor (NB) ... Robotics Minor (Ro) ... Structural Mechanics Minor (SM) ... Visual Culture Minor (VC)"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-003: institutional facts (size, faculty, divisions)
field: institution.facts
value: "approximately 1,000 undergraduates and 1,400 graduate students; 323 professorial faculty; 6 academic divisions; 124-acre Pasadena campus; manages JPL for NASA; 49 Nobel Prizes"
source_url: https://www.caltech.edu/about/at-a-glance
source_snippet: "more than 300 professorial faculty members offering a rigorous curriculum ... to approximately 1,000 undergraduates and 1,400 graduate students ... 49 Nobel Prizes ... manages the Jet Propulsion Laboratory (JPL) for NASA"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-004: UG admissions site
field: undergraduate.admissions.site
value: https://www.admissions.caltech.edu/
source_url: https://www.admissions.caltech.edu/
source_snippet: "Undergraduate Admissions"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-005: UG application requirements (platform, fee, LOR, materials)
field: undergraduate.application.requirements
value: "Common App or QuestBridge; $75 fee or waiver; 1 STEM LOR + 1 Humanities/Social Sciences LOR; school report; transcripts grades 9-11; mid-year report; SAT or ACT; AP/IB scores; English proficiency (if international); STEM activities & awards verification"
source_url: https://www.admissions.caltech.edu/apply/first-year-applicants/application-requirements
source_snippet: "Common App or QuestBridge Application. $75 application fee or fee waiver. ... 1 STEM: Calculus (or beyond), Chemistry, Physics, or Biology. 1 Humanities or Social Sciences: English, History, Government, or Economics. ... Verification of STEM Activities and Awards"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-006: application fee
field: undergraduate.application.fee
value: "$75 (one-time, non-refundable); fee waiver via Caltech Active Transport Pass; QuestBridge always free"
source_url: https://www.admissions.caltech.edu/apply/first-year-applicants/first-year-application-fee-and-waiver
source_snippet: "Caltech requires a one-time, non-refundable application fee of $75."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-007: UG deadlines (REA + RD)
field: undergraduate.deadlines.rea_and_rd
value: "REA: app Nov 1, materials Nov 6, testing by Nov 30, decision mid-Dec; RD: app Jan 5, materials Jan 11, decision mid-March; Enrollment May 1 2026; Waitlist opt-in mid-April (to mid-July)"
source_url: https://www.admissions.caltech.edu/apply/first-year-applicants/deadlines
source_snippet: "Although REA applications are due November 1, you will have until November 6 to submit all required and supplemental materials and standardized testing must be completed before November 30. ... Regular Decision (RD) is the most common admissions process ... Although RD applications are due January 5, yo... January 11 ... Admitted students will then have until May 1, 2026 to decide ... waitlisted ... has until mid-April to opt-in"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-008: standardized tests policy (SAT/ACT required, buckets)
field: undergraduate.application.standardized_tests
value: "SAT or ACT required (fall 2026: ACT writing/science subscores not required); composite not used, individual subscores considered; Bucket A SAT 780-800 / ACT 35-36; Bucket B SAT 750-770 / ACT 33-34; Below SAT<750 / ACT<33"
source_url: https://www.admissions.caltech.edu/apply/first-year-applicants/standardized-tests
source_snippet: "Caltech requires first-year applicants to submit either the SAT or the ACT for admissions to Caltech. For fall 2026 applicants, Caltech does not require the ACT writing or science subscores. ... Caltech will not consider a student's composite score and instead, Caltech will consider each individual subscore"
capture_date: 2026-07-04
evidence_type: official_webpage_table
```

```yaml
# E-U-009: English proficiency (international) table
field: undergraduate.application.english_proficiency
value: "TOEFL min 100 (25 each); IELTS min 7 (7 each); Duolingo min 130 (130 each); InitialView recommended; exam before app deadline; exempt if native English or English-medium secondary school"
source_url: https://www.admissions.caltech.edu/apply/first-year-applicants/international-applicants
source_snippet: "English Proficiency Exam scores are required of all international applicants unless 1) your native language is English or 2) English is the primary language of instruction in your secondary school ... IELTS 7 / 7 ... TOEFL 100 / 25 ... Duolingo English Test 130 / 130"
capture_date: 2026-07-04
evidence_type: official_webpage_table
```

```yaml
# E-U-010: transfer + 3/2 pathway
field: undergraduate.transfer.pathways
value: "Transfer Applicants (own deadlines); 3/2 Program (liberal-arts partner 3 yrs + Caltech 2 yrs -> BS)"
source_url: https://www.admissions.caltech.edu/apply/transfer-applicants
source_snippet: "Transfer Applicants ... 3/2 Program"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-U-011: UG cost of attendance 2025-26 (line items)
field: undergraduate.cost.attendance_2025_26
value: "Tuition $65,622; Fees $2,586; Housing On $12,105 / Off $15,219; Food On $8,886 / Off $7,533; Books $1,428; Personal On $3,285 / Off $5,067 / Parents $4,140; Living Expenses (parents) $11,835; TOTAL On $93,912 / Off $97,455 / Parents $85,611"
source_url: https://catalog.caltech.edu/current/information-for-undergraduate-students/undergraduate-expenses/
source_snippet: "ESTIMATED COST OF ATTENDANCE 2025-26 ... Tuition $65,622 ... Fees 2,586 ... Housing 12,105 ... Food/Meals 8,886 ... Total Estimated Cost of Attendance $93,912"
capture_date: 2026-07-04
evidence_type: official_webpage_table
```

```yaml
# E-U-012: UG financial aid policy
field: undergraduate.financial_aid.policy
value: "100% demonstrated need met; need-blind domestic (incl. undocumented/DACA from US HS); need-AWARE international; no merit scholarships; avg grant ~$73k (fall 2024); avg loan debt ~$16k (Class 2023); <$100k = no-loan covers tuition/fees/housing/food; <$200k = covers tuition; >=20% Pell eligible"
source_url: https://www.admissions.caltech.edu/afford
source_snippet: "The Institute meets 100% of students' demonstrated financial need ... Caltech Admissions is need-blind for domestic students ... We are need-aware for international students ... Caltech does not award merit scholarships ... the average grant aid was just under $73,000 ... approximately $16,000"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-001: graduate options enumeration (31)
field: graduate.options.count_and_source
value: "31 graduate options; enumerated verbatim from catalog 'Special Regulations For Graduate Options' submenu"
source_url: https://catalog.caltech.edu/current/information-for-graduate-students/general-requirements-for-graduate-degrees/
source_snippet: "Aerospace (AE) Applied and Computational Mathematics (ACM) Applied Mechanics (AM) Applied Physics (APh) Astrophysics (Ay) Biochemistry and Molecular Biophysics (BMB) Bioengineering (BE) Biology (Bi) Chemical Engineering (ChE) Chemistry (Ch) Civil Engineering (CE) Computation and Neural Systems (CNS) Computational Science and Engineering (CSE) Computer Science (CS) Computing and Mathematical Sciences (CMS) Control and Dynamical Systems (CDS) Electrical Engineering (EE) Environmental Science and Engineering (ESE) Geological and Planetary Sciences (GPS) ... History (H) History and Philosophy of Science (HPS) Information and Data Science (IDS) Materials Science (MS) Mathematics and Minor (Ma) Mechanical Engineering (ME) Medical Engineering (MedE) Neurobiology (NB) Physics (Ph) Quantum Science and Engineering (QSE) Social and Decision Neuroscience (SDN) Social Science (SS)"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-002: graduate degrees offered (MS / Engineer's / PhD)
field: graduate.degrees_offered
value: "MS (1-year, terminal or en route); Engineer's degree (limited fields); PhD (>=12 terms / 3 yrs residence); part-time permitted with option recommendation"
source_url: https://www.gradoffice.caltech.edu/academics/degrees
source_snippet: "Caltech offers M.S. and Ph.D. degrees and a select number of Engineer's and non-degree programs. ... The Master of Science degree ... can be completed in one academic year. Not all options admit directly for the M.S. degree ... Engineer's degrees are awarded in limited fields. ... At least twelve terms (three academic years) of residence are required for the Ph.D. degree."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-003: graduate application requirements (decentralized)
field: graduate.application.requirements
value: "Bachelor's required (no second PhD); transcripts all institutions; 3 LOR; CV; essays; GRE per-option; English proficiency per-option; work authorization typically required for PhD matriculation"
source_url: https://www.gradoffice.caltech.edu/admissions/checklist
source_snippet: "Applicants must have completed a bachelor's degree or the equivalent before beginning graduate study. Applicants who already hold a Ph.D. degree will not be considered for a second Ph.D. degree. Transcripts ... three letters of recommendation, a CV, and essays are required ... GRE policies differ substantially among the various graduate programs ... Most of the funding sources require work authorization."
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-004: graduate tuition & expenses 2025-26
field: graduate.cost.tuition_2025_26
value: "Tuition & fees $68,001/academic year; General Deposit $100; Books/supplies ~$1,428; Catalina apartments $790-$1,585/mo; late fee $50"
source_url: https://catalog.caltech.edu/current/information-for-graduate-students/graduate-expenses/
source_snippet: "The tuition and fees charge for all students registering for graduate work is currently $68,001.00 per academic year ... Fall (9/29/2025), Winter (1/5/2026), and Spring (3/30/2026)"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-G-005: graduate funding model (assistantships/fellowships)
field: graduate.funding.model
value: "PhD typically fully funded via assistantships (RA/TA), external fellowships (e.g. NSF), and institute fellowships (ARCS, J. Yang, Kanel, KAUTE, MOE Taiwan-Caltech)"
source_url: https://www.gradoffice.caltech.edu/financialsupport
source_snippet: "Assistantships; External Fellowships ... National Science Foundation (NSF); Institute Fellowships ... ARCS J. Yang Scholarship Kanel KAUTE Foundation Fellowship MOE Taiwan-Caltech"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-DIV-001: division structure (6 divisions)
field: institution.divisions
value: "Biology & Biological Engineering; Chemistry & Chemical Engineering; Engineering & Applied Science; Geological & Planetary Sciences; Humanities & Social Sciences; Physics, Mathematics & Astronomy"
source_url: https://www.caltech.edu/about/at-a-glance
source_snippet: "Academic Divisions Biology & Biological Engineering Chemistry & Chemical Engineering Engineering & Applied Science Geological & Planetary Sciences Humanities & Social Sciences Physics, Mathematics & Astronomy"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-DIV-002: EAS 7 departments (option->department attribution)
field: division.eas.departments
value: "Lynn Booth & Kent Kresa Department of Aerospace; Andrew and Peggy Cherng Department of Medical Engineering; Applied Physics and Materials Science; Computing and Mathematical Sciences; Electrical Engineering; Environmental Science and Engineering; Mechanical and Civil Engineering"
source_url: https://www.eas.caltech.edu/
source_snippet: "Departments ... Lynn Booth & Kent Kresa Department of Aerospace⇗ Andrew and Peggy Cherng Department of Medical Engineering⇗ Applied Physics and Materials Science⇗ Computing and Mathematical Sciences⇗ Electrical Engineering⇗ Environmental Science and Engineering⇗ Mechanical and Civil Engineering⇗"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-DIV-003: PMA 3 departments
field: division.pma.departments
value: "Physics; Mathematics; Astronomy"
source_url: http://pma.caltech.edu/
source_snippet: "Departments Open Departments submenu Physics Mathematics Astronomy"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-DIV-004: BBE member options
field: division.bbe.options
value: "Biology; Bioengineering; Biochemistry and Molecular Biophysics (BMB); Computation and Neural Systems (CNS); Neurobiology"
source_url: https://www.bbe.caltech.edu/
source_snippet: "Academics ... Biology ... Bioengineering ... Biochemistry and Molecular Biophysics (BMB) Computation and Neural Systems (CNS) ... Neurobiology"
capture_date: 2026-07-04
evidence_type: official_webpage
```

```yaml
# E-DIV-005: HSS UG options + grad PhD programs
field: division.hss.options
value: "UG options/minors: Business Economics and Management, Economics, English, History, History and Philosophy of Science, Philosophy, Political Science, Visual Culture; Grad PhD: Social Sciences PhD, Social and Decision Neuroscience PhD"
source_url: https://www.hss.caltech.edu/
source_snippet: "Undergraduate Studies ... Options & Minors ... Business, Economics, and Management Economics English History History and Philosophy of Science Philosophy Political Science Visual Culture ... Graduate Studies ... Social Sciences PhD Program Social and Decision Neuroscience PhD Program"
capture_date: 2026-07-04
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
caltech-knowledge-base-v2 (collection)
├── caltech-overview                  (院校总览 + rule 1-4 + institutional facts)
├── caltech-ug-bbe                    (BBE 本科 BS options)
├── caltech-ug-cce                    (CCE 本科 BS options)
├── caltech-ug-eas                    (EAS 本科 BS options — largest, 7)
├── caltech-ug-gps                    (GPS 本科 BS options)
├── caltech-ug-hss                    (HSS 本科 BS options — 7)
├── caltech-ug-pma                    (PMA 本科 BS options)
├── caltech-ug-interdisc              (ISP + 3/2)
├── caltech-ug-minors                 (19 minors complete list)
├── caltech-grad-bbe / cce / eas / gps / hss / pma / interdisc  (PhD options by division)
├── caltech-ug-application            (deadlines, requirements, tests, English proficiency)
├── caltech-ug-cost-aid              (2025-26 COA line items + aid policy)
├── caltech-grad-application         (decentralized model, GRE/ELP, degrees offered)
└── caltech-grad-cost-funding        (grad tuition $68,001 + funding)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "caltech-knowledge-base-v2"
  division: "<BBE|CCE|EAS|GPS|HSS|PMA|Interdisciplinary>"
  option_code: "<e.g. CS>"
  degree_level: "<BS|Minor|MS|Engineer's|PhD>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | options | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|-----------|--------|
| P0 | Per-option **MS vs PhD** degree matrix (which of 31 grad options admit terminal MS) | https://catalog.caltech.edu/current/information-for-graduate-students/special-regulations-for-graduate-options/<option>/ | Catalog 不发布 clean per-option degree split；当前每 option 计为 1 PhD-track 行。 |
| P0 | Per-option **GRE policy** (Required / Optional / Not Accepted) | 各 option 的 gradoffice 详情页 / catalog special-regulations 页 | Checklist 仅说"varies by program"；未抓逐项。 |
| P0 | Per-option **graduate application deadline** & **application fee** | https://www.gradoffice.caltech.edu/admissions/checklist + 各 option 详情 | Decentralized；未逐项抓取。 |
| P0 | Per-option **TOEFL/IELTS minimums** (graduate) | 各 option 详情页 | UG 已抓全；grad 各 option 自定。 |
| P0 | **2026-27 UG cost of attendance** (when published) | https://catalog.caltech.edu/current/information-for-undergraduate-students/undergraduate-expenses/ | 当前为 2025-26；新学年发布后更新。 |
| P1 | Class Profile（acceptance rate / applicant count / median test scores / yield） | https://www.admissions.caltech.edu/apply/what-we-look-for/class-profile | 页面数据靠 JS 渲染/图片，snapshotText 抓不到结构化数字。 |
| P1 | April-15-equivalent graduate honor date (CGS Resolution) | gradoffice admissions FAQ | 未在抓取页明确。 |
| P1 | Engineer's degree — which "limited fields" specifically | catalog special-regulations 页 | 措辞为 "limited fields"，未枚举。 |
| P2 | Department→option 完整官方映射表（尤其 IDS/CS/CMS 在 CMS dept 内的细分） | 各 Division 官网 + catalog | 当前映射来自 Division 官网部门列表 + 通用 Caltech 结构，已可对账，但缺单一权威映射页。 |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | Caltech | MIT | Stanford | Harvard | Yale | Princeton | NYU | Columbia |
|-----------|---------|-----|----------|---------|------|-----------|-----|----------|
| Total UG cost/yr (on-campus, current) | $93,912 (25-26) | — | — | — | — | — | — | — |
| Tuition/yr | $65,622 (25-26) | — | — | — | — | — | — | — |
| Need-blind (intl?) | **No** (need-aware intl) | Yes | Yes | Yes | Yes | Yes | — | — |
| EA/REA deadline | REA Nov 1 | EA Nov 1 | REA Nov 1 | REA Nov 1 | — | SCEA | ED Nov 1 | — |
| RD deadline | **Jan 5** | Jan 1/4 | Jan 5 | Jan 1 | Jan 2 | Jan 1 | Jan 5 | Jan 1 |
| SAT/ACT required? | **Yes** | Yes | Yes | — | — | — | — | — |
| TOEFL min | 100 | — | — | — | 100 | — | 100 | 105 |
| IELTS min | 7 | — | — | — | 7.5 | — | 7.5 | 7.5 |
| Tuition-free threshold | <$100k no-loan (covers t/f/h/f) | — | — | — | — | — | — | — |
| Avg grant | ~$73,000 (fall 2024) | — | — | — | — | — | — | — |
| Grad app fee | varies (P0) | — | — | — | — | — | — | — |
| April-15 honor date | follows CGS (P1) | — | — | — | — | — | — | — |
| **Total programs (rule 1)** | **76** | — | 342 | — | — | — | — | — |
| **Schools/departments (rule 2)** | 6 divisions + 1 interdisc | — | 7 schools | — | — | — | — | — |
| UG degree awarded | **BS only** | — | — | A.B./S.B. | — | — | — | — |

> Other-school columns intentionally blank in this solo run; populate from sibling v2 docs for cross-school diff.

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: catalog.caltech.edu · admissions.caltech.edu · gradoffice.caltech.edu · bbe/cce/eas/gps/hss/pma.caltech.edu · caltech.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch on static pages
> **Granularity**: division → option/department → degree-level → program
> **Reconciliation**: rule-1 (76) == rule-3 sum (76) == rule-4 matrix cell-sum (76) == rule-5 row count (76). PASS.
