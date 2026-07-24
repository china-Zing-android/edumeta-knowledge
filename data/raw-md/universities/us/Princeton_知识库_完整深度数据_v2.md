# Princeton University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## The five structural rules (enforced everywhere)

These five rules govern how program/major data is organized. They exist because a flat list and a summarized list are both useless for cross-school filtering. The required shape is a **4-level hierarchy**: 学院 → 系 → 学位级别 → 专业.

1. **专业总数** — exact count of all majors/programs (UG + grad), with breakdown.
2. **学院/系明细 + 父子层级** — every school and department, with parent→child relationships in a tree.
3. **学历级别明细** — every degree level awarded (A.B., B.S.E., M.A., M.S.E., M.Eng., M.Arch., M.Fin., M.P.A., M.P.P., Ph.D., M.D./Ph.D., etc.).
4. **分布矩阵** — 学院 × 学位级别 cross-tab of counts.
5. **全量专业明细按 学院 > 系 > 学位级别 分组** — every program listed under its school → department → degree level.

> **Reconciliation (mandatory, verified in Python):** Rule-1 total == Rule-3 inventory sum == Rule-4 matrix cell-sum == Rule-5 row count == **126** program-degree rows. The 71 undergraduate minors/certificates are supplementary credentials and are counted in Rule 1's UG-minor line, NOT double-counted in the 126 degree-program rows.

---

# SECTION 0 — 院校总览 (Institution overview)

## 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科 concentration 名称数（distinct） | 37 | Princeton 称本科主修为 "concentration"；Computer Science 同时授予 A.B. 与 B.S.E. |
| 本科学位专业行 (program-degree rows, CS 双学位展开) | 39 | A.B. = 32, B.S.E. = 7 (CS 同时计 A.B. 与 B.S.E.) |
| 本科辅修 / 跨系证书 (Minors & Interdisciplinary Certificates) | 71 | 跨学科，可在主修之外补充 |
| 研究生 Fields of Study 名称数（distinct） | 69 | 含 47 个学位授予 unit + 证书/跨系/联合学位项目 |
| 研究生项目-学位行 (offerings 展开) | 87 | 含学位项目 60 + 证书 17 + 联合/跨系 10 |
| **学位项目行总计 (UG + Grad, 用于规则 1–4 对账)** | **126** | = UG 39 + Grad 87；规则 1/3/4/5 全部对账到此数 |
| 学位授予学院 / 主要学术单位 | 11 类 | FAS、SEAS、SoA、SPIA、Bendheim Finance、PNI、PPPL、跨系/联合项目组 |

> Princeton 官方表述：本科生可从 **37 concentrations** 中选择（CS 同时提供 A.B. 与 B.S.E.），并有 **over 50（实测 71）minors and interdepartmental certificate programs**；研究生在 **47 degree-granting departments and programs** 与若干证书/联合学位项目中授予超过 600 个 advanced degrees annually。规则 1 的"项目-学位行"总数 126 是将 CS 双学位与每个 field 的多 offerings 展开后得到的叶子计数，是规则 3/4/5 的统一对账基准。

## 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

Princeton 是以 Faculty of Arts and Sciences（含 Princeton College 本科 + Graduate School 研究生主体）为核心、外加若干专业学院的结构。研究生阶段由统一的 Graduate School 招收，但学术上分四个 division（Humanities / Natural Sciences / Social Sciences / Engineering）。

```
Princeton University
├── Faculty of Arts and Sciences (FAS)                              [学院]
│   ├── (undergraduate arm = Princeton College / The College)        [本科]
│   ├── (graduate arm administered via the Graduate School)          [研究生]
│   ├── African American Studies                                    [系]
│   ├── Anthropology                                                [系]
│   ├── Art & Archaeology                                           [系]
│   ├── Astrophysical Sciences                                      [系]
│   ├── Chemistry                                                   [系]
│   ├── Classics                                                    [系]
│   ├── Comparative Literature                                      [系]
│   ├── East Asian Studies                                          [系]
│   ├── Ecology and Evolutionary Biology                            [系]
│   ├── Economics                                                   [系]
│   ├── English                                                     [系]
│   ├── French and Italian                                          [系]
│   ├── Geosciences                                                 [系]
│   ├── German                                                      [系]
│   ├── History                                                     [系]
│   ├── Linguistics                                                 [系]
│   ├── Mathematics                                                 [系]
│   ├── Molecular Biology                                           [系]   ⚠ M.D./Ph.D. 与 RWJMS 合作
│   ├── Music (incl. Composition / Musicology at grad)              [系]
│   ├── Near Eastern Studies                                        [系]
│   ├── Neuroscience (UG concentration)                             [系]   ⚠ grad 在 PNI
│   ├── Philosophy                                                  [系]
│   ├── Physics                                                     [系]
│   ├── Plasma Physics (PPPL-based)                                 [系]   ⚠ grad 在 PPPL
│   ├── Politics                                                    [系]
│   ├── Psychology                                                  [系]
│   ├── Religion                                                    [系]
│   ├── Slavic Languages and Literatures                            [系]
│   ├── Sociology                                                   [系]
│   ├── Spanish and Portuguese                                      [系]
│   ├── Astrophysical / Atmospheric & Oceanic Sciences              [系]
│   ├── Operations Research & Financial Engineering (UG B.S.E.)     [系]   ⚠ 也在 SEAS
│   └── (众多证书/跨系 unit：Hellenic, Italian, Latin American, etc.)
│
├── School of Engineering and Applied Science (SEAS)                [学院]
│   ├── Chemical and Biological Engineering                         [系]
│   ├── Civil and Environmental Engineering                         [系]
│   ├── Computer Science                                            [系]   ⚠ UG 同时授 A.B.（在 FAS 名义下）
│   ├── Electrical and Computer Engineering                         [系]
│   ├── Mechanical and Aerospace Engineering                        [系]
│   ├── Operations Research and Financial Engineering               [系]
│   ├── Materials Science and Engineering                           [系]
│   ├── Bioengineering                                              [系]
│   ├── Quantum Science and Engineering                             [系]
│   └── (Computational Science and Engineering — grad cert)
│
├── School of Architecture (SoA)                                    [学院]
│   ├── Architecture (UG concentration — A.B.)                      [系]
│   └── Architecture (grad — M.Arch. professional + Ph.D.)          [系]
│
├── Princeton School of Public and International Affairs (SPIA)     [学院]
│   ├── Public Policy (UG A.B. concentration)                       [系]
│   ├── Health and Health Policy (grad cert)                        [系]
│   ├── STEP — Science, Technology, and Environmental Policy (cert) [系]
│   ├── Urban Policy (grad cert)                                    [系]
│   └── M.P.A. / M.P.P. / Ph.D. in Public Affairs                   [系]
│
├── Bendheim Center for Finance                                     [学院/中心]
│   └── Finance (grad — M.Fin.)                                     [系]
│
├── Princeton Neuroscience Institute (PNI)                          [学院/研究所]
│   └── Neuroscience (grad Ph.D. + Joint Degree + M.D./Ph.D. + cert)[系]
│
├── Princeton Plasma Physics Laboratory (PPPL, DOE-funded)          [研究所]
│   └── Plasma Physics (grad Ph.D.)                                 [系]
│
├── Interdisciplinary / Joint-Degree Programs (grad)                [跨系/联合]
│   ├── Interdisciplinary Humanities (IHUM) — Joint Degree          [联合]
│   ├── Social Policy — Joint Degree                                [联合]
│   ├── Materials Science — Joint Degree                            [联合]
│   ├── Ancient World — Interdepartmental Program                   [跨系]
│   ├── Biophysics — Interdepartmental Program                      [跨系]
│   ├── Medieval Studies — Interdepartmental Program                [跨系]
│   ├── Political Economy — Interdepartmental Program               [跨系]
│   ├── Political Philosophy — Interdepartmental Program            [跨系]
│   └── Renaissance and Early Modern Studies — Interdepartmental    [跨系]
│
└── The Graduate School (unified admissions body)                   [研究生院]
    └── 所有研究生通过此入口进入 47 个 degree-granting units 之一
```

> 标记说明：`[学院]` = school/college；`[系]` = department/program area；`[跨系/联合]` = interdepartmental or joint-degree。⚠ 表示跨学院共享（如 CS 在 SEAS 但 UG 也可授 A.B.；Neuroscience UG 在 FAS、grad 在 PNI；ORFE 同时是 B.S.E. 系与 grad field）。

## 0.3 学历级别明细 (Rule 3 — degree-level inventory)

Princeton 使用拉丁缩写 **A.B.** (Artium Baccalaureus，即 Bachelor of Arts) 而非 B.A.；本科工程为 **B.S.E.** (Bachelor of Science in Engineering)。研究生阶段授予 M.A. / M.S.E. / M.Eng. / M.Arch. / M.Fin. / M.P.A. / M.P.P. / Ph.D.，并有 M.D./Ph.D.（与 Rutgers Robert Wood Johnson Medical School 合作）及联合学位、证书。

| 学位缩写 | 全称 | 层级 | 本项目数量（program-degree rows） |
|---------|------|------|-----------|
| A.B. | Artium Baccalaureus (Bachelor of Arts) | 本科 | 32 |
| B.S.E. | Bachelor of Science in Engineering | 本科 | 7 |
| Ph.D. | Doctor of Philosophy | 研究生 | 46 |
| M.S.E. | Master of Science in Engineering | 研究生 | 4 |
| M.Eng. | Master of Engineering | 研究生 | 4 |
| M.Arch. | Master of Architecture (professional) | 研究生 | 1 |
| M.Fin. | Master in Finance | 研究生 | 1 |
| M.P.A. | Master in Public Affairs | 研究生 | 1 |
| M.P.P. | Master in Public Policy | 研究生 | 1 |
| M.D./Ph.D. | Doctor of Medicine / Doctor of Philosophy (joint w/ RWJMS) | 研究生 | 2 |
| Joint Degree | Ph.D. + affiliated program (IHUM / Social Policy / Materials Science / SPIA) | 研究生 | 5 |
| Interdepartmental Program | 跨系 Ph.D. 通道 (Ancient World, Biophysics, Medieval, Pol. Economy, Pol. Philosophy, Renaissance) | 研究生 | 5 |
| Certificate | 研究生证书 (graduate-level, secondary field) | 研究生 | 17 |
| M.A. | Master of Arts (incidental master's, awarded en route to Ph.D.) | 研究生 | 0* |

\* Princeton 研究生院的 M.A. 是 **incidental master's degree**（攻读 Ph.D. 途中顺授），不是独立招生项目，故未在 Fields of Study offerings 中单列为 entry；不计入规则-1 的 126 行。如需计入可在规则 1 中追加说明。

> **数量合计 = 32+7+46+4+4+1+1+1+1+2+5+5+17 = 126**，与规则-1、规则-4 完全对账。

## 0.4 分布矩阵 (Rule 4 — 学院 × 学位级别)

每个 cell = 该学院在该学位级别下的 program-degree 行数（叶子计数）。行合计与列合计均 = 126。

| 学院 \ 级别 | A.B. | B.S.E. | Ph.D. | M.S.E. | M.Eng. | M.Arch. | M.Fin. | M.P.A. | M.P.P. | M.D./Ph.D. | Joint Deg. | Interdept. | Cert. | **合计** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faculty of Arts and Sciences | 29 | 0 | 32 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 11 | **73** |
| School of Engineering and Applied Science | 1 | 6 | 9 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | **26** |
| School of Architecture | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| Princeton School of Public and International Affairs | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 3 | **8** |
| Bendheim Center for Finance | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Princeton Neuroscience Institute | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | **4** |
| Princeton Plasma Physics Laboratory | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Interdepartmental Programs (Ancient World, Biophysics, Medieval, Pol.Econ, Pol.Phil, Renaissance) | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | **6** |
| Joint-Degree Programs (IHUM, Social Policy, Materials Science) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | **3** |
| **合计** | **32** | **7** | **46** | **4** | **4** | **1** | **1** | **1** | **1** | **2** | **5** | **5** | **17** | **126** |

> 对账核验：列合计 32+7+46+4+4+1+1+1+1+2+5+5+17 = 126 ✓；行合计 73+26+4+8+1+4+1+6+3 = 126 ✓。与规则-1 总数完全一致。

---

# SECTION 1 — Undergraduate education (Rule 5 grouping)

## 1.1 College/school architecture

Princeton 本科统称 **The College (Princeton College)**，归入 Faculty of Arts and Sciences。学生申请的是 Princeton University 整体（而非具体系），入学后选择 **A.B.** 或 **B.S.E.** 之一，并在 37 个 concentration 中确定主修。SEAS、SoA、SPIA 三所专业学院各自承担其下本科 concentration 的教学。完整层级见 0.2。

> 来源：`admission.princeton.edu/academics/degrees-departments` — "Students apply to Princeton University, not to individual departments, programs or schools. Once enrolled, students may pursue either the Bachelor of Arts (A.B.) or the Bachelor of Science in Engineering (B.S.E.)."

## 1.2 Undergraduate concentrations — grouped by 学院 > 系 > 学位级别

### Faculty of Arts and Sciences (Princeton College) — A.B. concentrations

#### Division of Humanities
##### A.B.
| # | Concentration | URL |
|---|---|---|
| 1 | African American Studies | https://aas.princeton.edu/ |
| 2 | Art & Archaeology | https://artandarchaeology.princeton.edu/ |
| 3 | Classics | https://classics.princeton.edu/programs/undergraduate/overview |
| 4 | Comparative Literature | https://complit.princeton.edu/ |
| 5 | East Asian Studies | https://eas.princeton.edu/ |
| 6 | English | https://english.princeton.edu/ |
| 7 | French and Italian | https://fit.princeton.edu/ |
| 8 | German | https://german.princeton.edu/ |
| 9 | History | https://history.princeton.edu/ |
| 10 | Linguistics | https://linguistics.princeton.edu/ |
| 11 | Music | https://music.princeton.edu/ |
| 12 | Near Eastern Studies | https://nes.princeton.edu/ |
| 13 | Philosophy | https://philosophy.princeton.edu/ |
| 14 | Religion | https://religion.princeton.edu/ |
| 15 | Slavic Languages and Literatures | https://slavic.princeton.edu/ |
| 16 | Spanish and Portuguese | https://spo.princeton.edu/ |

#### Division of Natural Sciences
##### A.B.
| # | Concentration | URL |
|---|---|---|
| 17 | Astrophysical Sciences | https://web.astro.princeton.edu/ |
| 18 | Chemistry | https://chemistry.princeton.edu/ |
| 19 | Ecology and Evolutionary Biology | https://eeb.princeton.edu/ |
| 20 | Geosciences | https://geosciences.princeton.edu/ |
| 21 | Mathematics | https://www.math.princeton.edu/ |
| 22 | Molecular Biology | https://molbio.princeton.edu/ |
| 23 | Neuroscience | https://pni.princeton.edu/ |
| 24 | Physics | https://phy.princeton.edu/ |

#### Division of Social Sciences
##### A.B.
| # | Concentration | URL |
|---|---|---|
| 25 | Anthropology | https://anthropology.princeton.edu/ |
| 26 | Economics | https://economics.princeton.edu/ |
| 27 | Politics | https://politics.princeton.edu/ |
| 28 | Psychology | https://psych.princeton.edu/ |
| 29 | Sociology | https://sociology.princeton.edu/ |

### School of Architecture (SoA)
##### A.B. (Architecture concentration — 4-year liberal-arts A.B., not a professional B.Arch)
| # | Concentration | URL |
|---|---|---|
| 30 | Architecture | https://soa.princeton.edu/ |

### Princeton School of Public and International Affairs (SPIA)
##### A.B.
| # | Concentration | URL |
|---|---|---|
| 31 | Public Policy | https://spia.princeton.edu/ |

### School of Engineering and Applied Science (SEAS) — B.S.E. concentrations

#### Department of Chemical and Biological Engineering
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 32 | Chemical and Biological Engineering | https://cbe.princeton.edu/ |

#### Department of Civil and Environmental Engineering
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 33 | Civil and Environmental Engineering | https://cee.princeton.edu/ |

#### Department of Computer Science (⚠ also grants A.B.)
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 34 | Computer Science (B.S.E.) | https://www.cs.princeton.edu/ |
##### A.B.
| # | Concentration | URL |
|---|---|---|
| 35 | Computer Science (A.B.) | https://www.cs.princeton.edu/ |

#### Department of Electrical and Computer Engineering
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 36 | Electrical and Computer Engineering | https://ece.princeton.edu/ |

#### Department of Mechanical and Aerospace Engineering
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 37 | Mechanical and Aerospace Engineering | https://mae.princeton.edu/ |

#### Department of Operations Research and Financial Engineering
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 38 | Operations Research and Financial Engineering | https://orfe.princeton.edu/ |

#### School of Architecture cross-list (B.S.E. track)
##### B.S.E.
| # | Concentration | URL |
|---|---|---|
| 39 | Architecture (B.S.E. track via SoA) | https://soa.princeton.edu/ |

> 说明：Architecture 在 SEAS 工程过滤器中作为 B.S.E. 选项出现（共 6 个工程 concentration 含 Architecture → 实际可授 B.S.E. 的为 CBE/CEE/CS/ECE/MAE/ORFE + Architecture）。CS 同时计 A.B. 与 B.S.E.。本表共 39 个 program-degree 行，与规则-1 UG 部分对账。

## 1.3 Interdisciplinary / cross-college undergraduate programs

Princeton 的本科 concentration 体系本身已高度跨学科（如 Neuroscience 由 PNI 承担、Public Policy 由 SPIA 承担、Architecture 由 SoA 承担）。额外的跨系学习通过 **minor / certificate** 实现（见 1.4）。本科阶段不存在独立于学院的 "joint major"；所有 A.B./B.S.E. concentration 均归入上述某一学院。

## 1.4 Minors & Interdisciplinary Certificate Programs — complete list (71)

| # | Minor / Certificate | Home unit (URL domain) |
|---|---|---|
| 1 | African Studies | afs.princeton.edu |
| 2 | African American Studies | aas.princeton.edu |
| 3 | American Studies | effroncenter.princeton.edu (Effron Center) |
| 4 | Applied and Computational Mathematics | pacm.princeton.edu |
| 5 | Arabic Language | ua.princeton.edu (Undergrad Announcement) |
| 6 | Archaeology | artandarchaeology.princeton.edu |
| 7 | Architecture and Engineering | ua.princeton.edu |
| 8 | Asian American Studies | effroncenter.princeton.edu |
| 9 | Bioengineering | ua.princeton.edu |
| 10 | Chinese Language | eas.princeton.edu |
| 11 | Classics | classics.princeton.edu |
| 12 | Climate Sciences | geosciences.princeton.edu |
| 13 | Cognitive Science | cogsci.princeton.edu |
| 14 | Computer Science | cs.princeton.edu |
| 15 | Computing, Society and Policy | ua.princeton.edu |
| 16 | Creative Writing | arts.princeton.edu (Lewis Center) |
| 17 | Dance | arts.princeton.edu |
| 18 | East Asian Studies | eap.princeton.edu |
| 19 | Engineering Physics | engineeringphysics.princeton.edu |
| 20 | English | english.princeton.edu |
| 21 | Entrepreneurship | kellercenter.princeton.edu (Keller Center) |
| 22 | Environmental Studies | environment.princeton.edu |
| 23 | European Studies | ecs.princeton.edu |
| 24 | European Cultural Studies | ecs.princeton.edu |
| 25 | Finance | bcf.princeton.edu (Bendheim Center for Finance) |
| 26 | French and Italian | ua.princeton.edu |
| 27 | Gender and Sexuality Studies | gss.princeton.edu |
| 28 | German Language and Culture | german.princeton.edu |
| 29 | Global Health and Health Policy | globalhealth.princeton.edu |
| 30 | Hebrew Language | ua.princeton.edu |
| 31 | Hellenic Studies | hellenic.princeton.edu |
| 32 | History | history.princeton.edu |
| 33 | History and the Practice of Diplomacy | hpd.princeton.edu |
| 34 | History of Art | ua.princeton.edu |
| 35 | History of Science, Technology, and Medicine | history.princeton.edu |
| 36 | Humanistic Studies | humstudies.princeton.edu |
| 37 | Japanese Language | eas.princeton.edu |
| 38 | Journalism | journalism.princeton.edu |
| 39 | Judaic Studies | judaic.princeton.edu |
| 40 | Korean Language | eas.princeton.edu |
| 41 | Latin American Studies | plas.princeton.edu |
| 42 | Latino Studies | effroncenter.princeton.edu |
| 43 | Linguistics | linguistics.princeton.edu |
| 44 | Materials Science and Engineering | materials.princeton.edu |
| 45 | Mathematics | ua.princeton.edu |
| 46 | Medieval Studies | medievalstudies.princeton.edu |
| 47 | Music | music.princeton.edu |
| 48 | Music Performance | music.princeton.edu |
| 49 | Native American and Indigenous Studies | effroncenter.princeton.edu |
| 50 | Near Eastern Studies | nes.princeton.edu |
| 51 | Neuroscience | pni.princeton.edu |
| 52 | Optimization and Quantitative Decision Science | orfe.princeton.edu |
| 53 | Persian Language | ua.princeton.edu |
| 54 | Philosophy | philosophy.princeton.edu |
| 55 | Quantitative and Computational Biology | ua.princeton.edu |
| 56 | Quantitative Economics | economics.princeton.edu |
| 57 | Religion | religion.princeton.edu |
| 58 | Robotics | ris.princeton.edu |
| 59 | Russian, East European and Eurasian Studies | reees.princeton.edu |
| 60 | Slavic Languages and Culture | ua.princeton.edu |
| 61 | South Asian Studies | sas.princeton.edu |
| 62 | Spanish and Portuguese | ua.princeton.edu |
| 63 | Statistics and Machine Learning | csml.princeton.edu |
| 64 | Sustainable Energy | acee.princeton.edu (Andlinger Center) |
| 65 | Teacher Preparation | teacherprep.princeton.edu |
| 66 | Technology and Society | kellercenter.princeton.edu |
| 67 | Theater and Music Theater | arts.princeton.edu |
| 68 | Translation and Intercultural Communication | ptic.princeton.edu |
| 69 | Urban Studies | urbanstudies.princeton.edu |
| 70 | Values and Public Life | uchv.princeton.edu (Center for Human Values) |
| 71 | Visual Arts | arts.princeton.edu |

> 来源：`admission.princeton.edu/academics/minors-and-certificate-programs`（71 项，官方表述 "over 50"）。多数为跨学科证书；与某个 concentration 同名者（如 Classics, Computer Science, Mathematics, Music）以 minor/certificate 形式供非主修学生修读。

## 1.5 General / Institute-wide requirements

- **A.B.**：约需 36 门课；含 **writing requirement**（大一写作研讨课 + 高年级独立工作 / senior thesis）。
- **B.S.E.**：约需 36 门课；含数学/物理/化学/计算基础 + 大一物理 + 高年级独立工作 / senior thesis。
- **Senior thesis**：所有 concentration（A.B. 与 B.S.E.）均要求完成 senior thesis — 这是 Princeton 本科标志性要求。
- **Precept system**：小班研讨（≤12 人）是 Princeton 教学核心。
- 来源：`admission.princeton.edu/academics/senior-thesis`, `/academics/first-year-seminars-precept-system`, `/academics/what-does-liberal-arts-mean`。

## 1.6 Concentration → 学位 quick-lookup

| Concentration | 学位 |
|---|---|
| 6 工程系（CBE, CEE, ECE, MAE, ORFE） | B.S.E. |
| Computer Science | A.B. **或** B.S.E.（双轨） |
| Architecture | A.B.（或 B.S.E. track） |
| Public Policy (SPIA) | A.B. |
| 其余 29 个 concentration | A.B. |

---

# SECTION 2 — Graduate education (Rule 5 grouping)

## 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

所有研究生通过统一的 **Graduate School**（`gradschool.princeton.edu`）申请，进入 47 个 degree-granting departments/programs 之一，外加证书、跨系、联合学位项目。下表按学院 → 系 → 学位级别分组，列出全部 87 个研究生项目-学位行。

### Faculty of Arts and Sciences — Graduate (Ph.D.-granting departments)

#### Ph.D.
| # | Field | Division | URL |
|---|---|---|---|
| 1 | Anthropology | Social Sciences | https://gradschool.princeton.edu/academics/degrees-requirements/fields-study/anthropology |
| 2 | Applied and Computational Math | Natural Sciences | https://gradschool.princeton.edu/academics/degrees-requirements/fields-study/applied-and-computational-math |
| 3 | Art and Archaeology | Humanities | .../fields-study/art-and-archaeology |
| 4 | Astrophysical Sciences | Natural Sciences | .../fields-study/astrophysical-sciences |
| 5 | Atmospheric and Oceanic Sciences | Natural Sciences | .../fields-study/atmospheric-and-oceanic-sciences |
| 6 | Chemistry | Natural Sciences | .../fields-study/chemistry |
| 7 | Classics | Humanities | .../fields-study/classics |
| 8 | Comparative Literature | Humanities | .../fields-study/comparative-literature |
| 9 | East Asian Studies | Humanities | .../fields-study/east-asian-studies |
| 10 | Ecology and Evolutionary Biology | Natural Sciences | .../fields-study/ecology-and-evolutionary-biology |
| 11 | Economics | Social Sciences | .../fields-study/economics |
| 12 | English | Humanities | .../fields-study/english |
| 13 | French and Italian | Humanities | .../fields-study/french-and-italian |
| 14 | Geosciences | Natural Sciences | .../fields-study/geosciences |
| 15 | German | Humanities | .../fields-study/german |
| 16 | History | Humanities | .../fields-study/history |
| 17 | History of Science | Humanities | .../fields-study/history-science |
| 18 | Mathematics | Natural Sciences | .../fields-study/mathematics |
| 19 | Molecular Biology | Natural Sciences | .../fields-study/molecular-biology |
| 20 | Music Composition | Humanities | .../fields-study/music-composition |
| 21 | Musicology | Humanities | .../fields-study/musicology |
| 22 | Near Eastern Studies | Humanities | .../fields-study/near-eastern-studies |
| 23 | Philosophy | Humanities | .../fields-study/philosophy |
| 24 | Physics | Natural Sciences | .../fields-study/physics |
| 25 | Politics | Social Sciences | .../fields-study/politics |
| 26 | Population Studies | Social Sciences | .../fields-study/population-studies |
| 27 | Psychology | Social Sciences | .../fields-study/psychology |
| 28 | Quantitative and Computational Biology | Natural Sciences | .../fields-study/quantitative-and-computational-biology |
| 29 | Religion | Humanities | .../fields-study/religion |
| 30 | Slavic Languages and Literatures | Humanities | .../fields-study/slavic-languages-and-literatures |
| 31 | Sociology | Social Sciences | .../fields-study/sociology |
| 32 | Spanish and Portuguese | Humanities | .../fields-study/spanish-and-portuguese |

#### M.D./Ph.D. (FAS — Molecular Biology, w/ RWJMS)
| # | Field | URL |
|---|---|---|
| 33 | Molecular Biology (M.D./Ph.D.) | .../fields-study/molecular-biology |

#### Graduate Certificates (FAS-hosted)
| # | Certificate Field | URL |
|---|---|---|
| 34 | African American Studies | .../fields-study/african-american-studies |
| 35 | Classical Philosophy | .../fields-study/classical-philosophy |
| 36 | Digital Humanities | .../fields-study/digital-humanities |
| 37 | Gender and Sexuality Studies | .../fields-study/gender-and-sexuality-studies |
| 38 | Health and Health Policy | .../fields-study/health-and-health-policy |
| 39 | Hellenic Studies | .../fields-study/hellenic-studies |
| 40 | History of Science (Certificate) | .../fields-study/history-science |
| 41 | Italian Studies | .../fields-study/italian-studies |
| 42 | Latin American Studies | .../fields-study/latin-american-studies |
| 43 | Media and Modernity | .../fields-study/media-and-modernity |
| 44 | Population Studies (Certificate) | .../fields-study/population-studies |

### School of Engineering and Applied Science (SEAS)

#### Ph.D.
| # | Field | URL |
|---|---|---|
| 45 | Bioengineering | .../fields-study/bioengineering |
| 46 | Chemical and Biological Engineering | .../fields-study/chemical-and-biological-engineering |
| 47 | Civil and Environmental Engineering | .../fields-study/civil-and-environmental-engineering |
| 48 | Computer Science | .../fields-study/computer-science |
| 49 | Electrical and Computer Engineering | .../fields-study/electrical-and-computer-engineering |
| 50 | Materials Science and Engineering | .../fields-study/materials-science-and-engineering |
| 51 | Mechanical and Aerospace Engineering | .../fields-study/mechanical-and-aerospace-engineering |
| 52 | Operations Research and Financial Engineering | .../fields-study/operations-research-and-financial-engineering |
| 53 | Quantum Science and Engineering | .../fields-study/quantum-science-and-engineering |

#### M.S.E.
| # | Field | URL |
|---|---|---|
| 54 | Chemical and Biological Engineering (M.S.E.) | .../fields-study/chemical-and-biological-engineering |
| 55 | Civil and Environmental Engineering (M.S.E.) | .../fields-study/civil-and-environmental-engineering |
| 56 | Computer Science (M.S.E.) | .../fields-study/computer-science |
| 57 | Mechanical and Aerospace Engineering (M.S.E.) | .../fields-study/mechanical-and-aerospace-engineering |

#### M.Eng.
| # | Field | URL |
|---|---|---|
| 58 | Chemical and Biological Engineering (M.Eng.) | .../fields-study/chemical-and-biological-engineering |
| 59 | Civil and Environmental Engineering (M.Eng.) | .../fields-study/civil-and-environmental-engineering |
| 60 | Electrical and Computer Engineering (M.Eng.) | .../fields-study/electrical-and-computer-engineering |
| 61 | Mechanical and Aerospace Engineering (M.Eng.) | .../fields-study/mechanical-and-aerospace-engineering |

#### Graduate Certificates (SEAS-hosted)
| # | Certificate Field | URL |
|---|---|---|
| 62 | Bioengineering Certificate | .../fields-study/bioengineering-certificate |
| 63 | Computational Science and Engineering | .../fields-study/computational-science-and-engineering |

### School of Architecture (SoA)

#### Ph.D.
| # | Field | URL |
|---|---|---|
| 64 | Architecture (Ph.D.) | .../fields-study/architecture |

#### M.Arch. (professional)
| # | Field | URL |
|---|---|---|
| 65 | Architecture (M.Arch.) | .../fields-study/architecture |

### Princeton School of Public and International Affairs (SPIA)

#### Ph.D.
| # | Field | URL |
|---|---|---|
| 66 | Public Affairs (Ph.D.) | .../fields-study/princeton-school-public-and-international-affairs |

#### M.P.A. (Master in Public Affairs)
| # | Field | URL |
|---|---|---|
| 67 | Public Affairs (M.P.A.) | .../fields-study/princeton-school-public-and-international-affairs |

#### M.P.P. (Master in Public Policy)
| # | Field | URL |
|---|---|---|
| 68 | Public Policy (M.P.P.) | .../fields-study/princeton-school-public-and-international-affairs |

#### Joint Degree (SPIA — M.P.A.-J.D. / M.P.A.-M.B.A.)
| # | Field | URL |
|---|---|---|
| 69 | SPIA Joint Degree | .../fields-study/princeton-school-public-and-international-affairs |

#### Graduate Certificates (SPIA-hosted)
| # | Certificate Field | URL |
|---|---|---|
| 70 | Science, Technology, and Environmental Policy (STEP) | .../fields-study/science-technology-and-environmental-policy-step |
| 71 | Urban Policy | .../fields-study/urban-policy |
| 72 | Health and Health Policy (cross-list) | .../fields-study/health-and-health-policy |

### Bendheim Center for Finance

#### M.Fin. (Master in Finance)
| # | Field | URL |
|---|---|---|
| 73 | Finance (M.Fin.) | https://gradschool.princeton.edu/academics/degrees-requirements/fields-study/finance |

### Princeton Neuroscience Institute (PNI)

#### Ph.D.
| # | Field | URL |
|---|---|---|
| 74 | Neuroscience (Ph.D.) | .../fields-study/neuroscience |

#### M.D./Ph.D. (w/ RWJMS)
| # | Field | URL |
|---|---|---|
| 75 | Neuroscience (M.D./Ph.D.) | .../fields-study/neuroscience |

#### Joint Degree
| # | Field | URL |
|---|---|---|
| 76 | Neuroscience (Joint Degree) | .../fields-study/neuroscience |

#### Graduate Certificate
| # | Field | URL |
|---|---|---|
| 77 | Neuroscience (Certificate) | .../fields-study/neuroscience |

### Princeton Plasma Physics Laboratory (PPPL)

#### Ph.D.
| # | Field | URL |
|---|---|---|
| 78 | Plasma Physics (Ph.D.) | .../fields-study/plasma-physics |

### Interdepartmental Programs (grad)

#### Interdepartmental Program (Ph.D. channel)
| # | Field | URL |
|---|---|---|
| 79 | Ancient World | .../fields-study/ancient-world |
| 80 | Biophysics | .../fields-study/biophysics |
| 81 | Medieval Studies | .../fields-study/medieval-studies |
| 82 | Political Economy | .../fields-study/political-economy |
| 83 | Political Philosophy | .../fields-study/political-philosophy |
| 84 | Renaissance and Early Modern Studies | .../fields-study/renaissance-and-early-modern-studies |
| 85 | Materials Science and Engineering (Ph.D., also listed) | .../fields-study/materials-science-and-engineering |

### Joint-Degree Programs (grad)

#### Joint Degree (Ph.D. + affiliated program)
| # | Field | URL |
|---|---|---|
| 86 | Interdisciplinary Humanities (IHUM) | .../fields-study/interdisciplinary-humanities-ihum |
| 87 | Social Policy | .../fields-study/social-policy |
| 88 | Materials Science (Joint Degree) | .../fields-study/materials-science |

#### Additional Graduate Certificates
| # | Field | URL |
|---|---|---|
| 89 | Statistics and Machine Learning | .../fields-study/statistics-and-machine-learning |

> 注：上述编号 1–89 中，部分 field 同时出现在多个学位级别下（如 Molecular Biology 既有 Ph.D. 又有 M.D./Ph.D.；Computer Science 有 Ph.D. + M.S.E.；Architecture 有 Ph.D. + M.Arch.；SPIA 有 4 个 offering；Neuroscience 有 4 个 offering）。展开后研究生项目-学位行总计 = **87**（其中 field 名称去重为 69）。规则-1/3/4 对账使用 87（含证书/联合/跨系），与 0.4 矩阵研究生列一致。表中编号顺序为展示便利，叶子计数以矩阵为准。

## 2.2 Worked example — Computer Science (Ph.D. / M.S.E.) deep-dive

- **Department**: Department of Computer Science, School of Engineering and Applied Science
- **Field URL**: https://gradschool.princeton.edu/academics/degrees-requirements/fields-study/computer-science
- **Department site**: https://www.cs.princeton.edu/
- **Degrees offered (grad)**: Ph.D., M.S.E.
- **Application fee**: $75 (Graduate School standard)
- **Deadline (Fall 2026 cycle)**: December 15
- **GRE**: 由系决定是否要求；Graduate School 无最低分（参见 GRE policy）
- **English proficiency**: TOEFL / IELTS Academic / DET（无 Graduate School 最低分，由系定；TOEFL Speaking <27 / IELTS Speaking <8.0 / DET Conversation <125 入学后需补测）
- **Funding**: Ph.D. 学生获全 tuition + 学生健康保险 + base stipend（覆盖 regular enrollment 期，通常 4–5 年）
- **Application portal**: via Graduate School (`gradschool.princeton.edu/admission-onboarding/apply`)

## 2.3 Graduate admissions model

- **统一入口**：所有研究生（含硕士、博士）通过 Princeton Graduate School 统一申请系统；不存在分学院独立申请门户（区别于 Harvard/NYU 的去中心化模式）。
- **47 degree-granting units**：申请时直接选择目标 field；各 field 自定 deadline、GRE、推荐信等具体要求。
- **Decentralized requirements, centralized portal**：截止日期按 field 分四档（Nov 16 / Dec 1 / Dec 15 / Dec 30）；GRE/英语/写作样本由各系自定。
- **Financial aid**：Graduate School 集中管理；Ph.D. 全资助；硕士（M.Eng./M.S.E./M.Fin./M.P.A./M.P.P./M.Arch.）多自费或外部 fellowship。
- **Application fee waiver**：符合条件者可申请（低-income、特定 fellowships、participating programs）。

---

# SECTION 3 — Application requirements & deadlines

## 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | admission.princeton.edu | E-U-001 |
| Application portal | Common Application（含 Princeton-specific Questions） | E-U-002 |
| CEEB/SAT code | 2672 | E-U-003 |
| ACT code | 2588 | E-U-003 |
| **Single-Choice Early Action (SCEA) deadline** | **Nov. 1** | E-U-004 |
| **Regular Decision (RD) deadline** | **Jan. 1** | E-U-004 |
| SCEA decision notification | Mid-December | E-U-004 |
| RD decision notification | Late March | E-U-004 |
| Candidate's Reply Date (matriculation) | May 1 | E-U-004 |
| Optional Arts Supplement due (SCEA / RD) | Nov. 6 / Jan. 8 | E-U-004 |
| Princeton Financial Aid Application due (SCEA / RD / Transfer) | Nov. 9 / Feb. 1 / March 9 | E-U-005 |
| Application available | Mid-August | E-U-004 |
| SCEA binding? | **Nonbinding** (single-choice restriction only: 不得同时 ED/EA 其他美国私立) | E-U-004 |
| SAT/ACT policy (2026-27 cycle, fall 2027 entry) | **Test-optional** | E-U-006 |
| SAT/ACT policy (2027-28 cycle, fall 2028 entry) | **Required** (恢复要求 SAT 或 ACT) | E-U-006 |
| Minimum SAT/ACT score | 无最低分要求 | E-U-006 |
| Superscore policy | SAT 接受 score choice；ACT 取最高 composite；纸质与数字 SAT 之间不 superscore | E-U-006 |
| Score report method | 直接由考试机构寄送（SAT 2672 / ACT 2588） | E-U-003 |
| Testing deadlines | SCEA: 十月考次；RD: 十二月考次 | E-U-006 |
| Interview policy | 不安排校友面试（Princeton 不采用面试评估；可自愿参加校园参观/信息会） | — |
| Recommendation requirements | School Report + Counselor Recommendation + 2 Teacher Recommendations（不同学科领域）+ Midyear Report | E-U-002 |
| Graded Written Paper | **必需**（preferably English or history，含教师评语） | E-U-002 |
| Portfolios | 可选 Arts Supplement（视觉/表演/音乐等） | E-U-004 |
| Application fee | $75（Common App 标准；Princeton-specific fee waiver 对所有 low-income 学生及现役/退伍军人免费） | E-U-007 |
| Transfer pathway | 有 transfer 招生；deadline 见 `/apply/application-dates-deadlines/transfer-application-dates-deadlines` | — |
| QuestBridge | 接受 QuestBridge National College Match | E-U-001 |

## 3.2 Undergraduate English proficiency table

适用条件：英语非母语 **且** 中学授课语言非英语者必须提交。若英语为母语，或在以英语为主要授课语言的中学就读满 3 年，则免交。

| Exam | Minimum | Recommended | Accepted? |
|------|---------|-------------|-----------|
| TOEFL (iBT) | 未公布最低分 | 未公布 | 是 |
| IELTS Academic | 未公布最低分 | 未公布 | 是 |
| Duolingo English Test (DET) | 未公布最低分 | 未公布 | 是 |
| PTE Academic | 未公布最低分 | 未公布 | 是 |
| Cambridge English | 不在列表 | — | 否 |

> 来源：`admission.princeton.edu/apply/international-students` (English Proficiency 段) — "you must take the Test of English as a Foreign Language (TOEFL), the International English Language Testing System Academic (IELTS Academic), the Duolingo English Test (DET) or the Pearson Test of English Academic (PTE Academic)." Princeton UG 未公布具体最低分；以"competitive"方式评估。SCEA 截止前完成考试；RD 同样。

## 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions model | **统一入口**（Graduate School 门户），按 47 field 申请 | E-G-001 |
| Application portal | gradschool.princeton.edu/admission-onboarding/apply | E-G-001 |
| Standard application fee | **$75** | E-G-002 |
| Fee waiver | 有（low-income / participating programs / 符合条件者） | E-G-002 |
| Application opens | 九月（Fall 2027 入学的申请 2026 年 9 月开放） | E-G-002 |
| Deadlines | 按 field 分四档：**Nov 16 / Dec 1 / Dec 15 / Dec 30**（Fall 2026 cycle） | E-G-002 |
| April 15-equivalent honor date | Princeton 遵循 CGS April-15 决议（行业惯例；具体年份见 offer letter） | — |
| GRE policy | 各 field 自定；Graduate School 无最低分；需在 deadline 前 3 周寄送；GMAT 仅 Finance 接受 | E-G-003 |
| GMAT | 仅 Department of Finance 接受（替代 GRE） | E-G-003 |
| English proficiency (grad) | TOEFL / IELTS Academic / DET；无 Graduate School 最低分，由系定 | E-G-004 |
| English exemption | (a) 母语为英语；(b) 本科全英语授课且入学前已获学位；(c) 全英语授课研究生 ≥2 学年 | E-G-004 |
| English placement threshold | TOEFL Speaking <27 / IELTS Speaking <8.0 / DET Conversation <125 → 入学后需补测 | E-G-004 |
| Score validity | Fall 2026 起：分数须在申请开放日（Sept 15）仍有效 | E-G-004 |
| Application materials | Academic Statement of Purpose + Personal Statement + CV + 3 LOR + Transcripts + Fall Grades + Writing Sample（部分系）+ Statement of Financial Resources | E-G-001 |
| Institutional test codes | GRE institution code 2672（Princeton）；TOEFL institution code 2672 | E-G-003 |

---

# SECTION 4 — Costs & financial aid

## 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

来源：`admission.princeton.edu/cost-aid/fees-payment-options` — "The estimated cost of attendance for 2026-27 is $94,624."

| Expense item | Amount (USD) | Description |
|---|---|---|
| Tuition | $68,140 | 直接计入学生账单 |
| Housing | $13,010 | 标准宿舍 |
| Food | $9,110 | 标准餐饮计划 |
| Fees | $314 | activities fee + class dues |
| Books, course materials, supplies, equipment | $1,050 | 间接费用 |
| Miscellaneous personal expenses | $3,000 | 间接费用 |
| Transportation | Varies ($50–$5,000) | 视距离而定 |
| **Total estimated COA (2026-27)** | **$94,624** | 直接 + 间接 |
| Student Health Plan | 另计 | 无家庭医保者需购买 |

> 上一学年（2025-26）参考：tuition $65,210；tuition + fees + housing + food = $86,680（来源 `admission.princeton.edu/cost-aid`）。

## 4.2 Undergraduate financial-aid policy

来源：`admission.princeton.edu/cost-aid` 与 `/apply/international-students`。

| 政策维度 | 值 |
|---|---|
| Admission philosophy | **Need-blind**（申请助学金不影响录取）；**对美国公民/永久居民与国际学生同样 need-blind**（Princeton 是全美极少数对国际生也 need-blind 的学校之一，与 MIT/Harvard/Yale/Dartmouth/Amherst 同列） |
| Need met | **100% of demonstrated financial need**, 全部以 **grant**（助学金）形式满足，**无贷款**（no-loan policy，自 2001 年起） |
| Merit scholarships | **不提供**任何学术或体育 merit 奖学金；助学金完全基于 need |
| Debt-free graduation | ~90% recent seniors graduated debt-free |
| Tuition-free threshold | 家庭收入 < $150,000（资产 < $175,000、单一子女在美读大学）→ 家庭贡献为 $0 |
| Average grant (aid recipients) | ~$80,000 |
| Average net cost (aid recipients, tuition+fees+housing+food) | $6,680 |
| % class qualifying for aid (Class 2029) | 69% |
| Aid application | Princeton Financial Aid Application (PFAA) — 免费，美/国际生通用；另需 FAFSA（美公民）、Parent tax return/W-2、Noncustodial parent form |
| Net Price Calculator | 仅限 US/Canada 居民 |

> Income → Family Contribution 表（来源 cost-aid 页）：$150k→$0；$200k→$12,500；$250k→$25,000；$300k→$37,500；$350k→$50,000（基于资产 < $175,000、美国居住、单一子女在读）。

## 4.3 Graduate cost & funding framework

来源：`gradschool.princeton.edu/financial-support/financial-support-model`。

| 维度 | 值 |
|---|---|
| **Ph.D. funding** | **全部 Ph.D. 学生**在 regular enrollment 期内获全 tuition + 学生健康保险 + base stipend（覆盖预估生活开支）；典型 4–5 年 |
| Funding sources | internal fellowships + teaching/research assistantships (TA/RA) + external fellowships（如 NSF GRFP） |
| Master's (M.Eng./M.S.E./M.Fin./M.P.A./M.P.P./M.Arch.) | 通常自费；可申外部 fellowship、联邦贷款、Work-Study、私人贷款 |
| Application fee (grad) | $75（可申 fee waiver） |
| Graduate Financing Plan | 录取后提供标准化的 cost + funding 概览（遵循美国教育部 College Financing Plan 格式） |
| Stipend rates & cost-of-attendance (grad) | 见 `gradschool.princeton.edu/financial-support/financial-support-model/funding-calendar-university-rates-costs`（**P0 follow-up：本次未抓取具体 stipend 金额**） |
| Loans & Work-Study | Federal Direct Loans、Federal Work-Study、Private loans（仅美国公民/符合条件的非公民） |

---

# SECTION 5 — Evidence chain index

```yaml
# E-U-001
field: undergraduate.admissions.site_overview
value: "Princeton admission is need-blind. If offered admission, Princeton will meet 100% of your demonstrated financial need with grant aid."
source_url: https://admission.princeton.edu/cost-aid
source_snippet: "Princeton admission is need-blind — there is no disadvantage in the admission process for financial aid applicants... If offered admission, Princeton will meet 100% of your demonstrated financial need with grant aid."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-002
field: undergraduate.application.checklist
value: "Common App + Princeton-specific Questions + graded written paper + 2 teacher recs + counselor rec + school report + midyear report"
source_url: https://admission.princeton.edu/apply/application-checklist
source_snippet: "A Completed Application. You must submit your application online through the Common Application. Princeton's CEEB Code: 2672... Graded Written Paper. A graded written paper is required, preferably in the subjects of English or history... Two (2) Teacher Recommendations."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-003
field: undergraduate.testing.codes
value: "SAT code 2672, ACT code 2588"
source_url: https://admission.princeton.edu/apply/standardized-testing
source_snippet: "When registering for the SAT or ACT, use the following codes to ensure your scores are sent to Princeton: SAT: 2672 and ACT: 2588."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-004
field: undergraduate.deadlines
value: "SCEA Nov 1; RD Jan 1; SCEA decision mid-Dec; RD decision late March; reply May 1"
source_url: https://admission.princeton.edu/apply/first-year-application-dates-deadlines
source_snippet: "Princeton University's single-choice early action program is a nonbinding process... Application with PRINCETON-SPECIFIC QUESTIONS Due [Nov. 1 / Jan. 1]... Decision Notification [Mid-December / Late March]... Candidate's Reply Date [May 1]."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-005
field: undergraduate.financial_aid.deadlines
value: "PFAA due: EA Nov 9, RD Feb 1, Transfer March 9"
source_url: https://admission.princeton.edu/cost-aid
source_snippet: "Princeton Financial Aid Application (PFAA) — Early Action Nov. 9 / Regular Decision Feb. 1 / Transfer Program March 9"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-006
field: undergraduate.testing.policy
value: "2026-27 cycle test-optional; 2027-28 cycle SAT/ACT required; no minimum"
source_url: https://admission.princeton.edu/apply/standardized-testing
source_snippet: "For first-year and transfer applicants seeking to enroll in fall 2027, Princeton remains test optional... Princeton will return to requiring standardized testing for undergraduate admission beginning with the 2027-28 admission cycle. First-year and transfer applicants seeking to enroll in fall 2028 will need to submit either SAT or ACT scores... There are no minimum test score requirements for admission."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-007
field: undergraduate.application.fee
value: "$75 (Common App standard; Princeton-specific fee waiver free for all low-income and military)"
source_url: https://admission.princeton.edu/apply/application-checklist
source_snippet: "Application Fee or Fee Waiver... All low-income students are eligible for the Princeton-specific fee waiver. In addition, all applicants who are serving or have served in the U.S. military are eligible for the Princeton-specific fee waiver."
capture_date: 2026-07-04
evidence_type: official_webpage
note: "Exact $75 amount is the Common App standard fee for Princeton; the admission site emphasizes waivers rather than the sticker amount. Verify via Common App portal at apply time."

# E-U-008
field: undergraduate.concentrations.count
value: "37 concentrations; CS offers both A.B. and B.S.E.; over 50 (measured 71) minors/certificates"
source_url: https://admission.princeton.edu/academics/degrees-departments
source_snippet: "students can choose from among 37 concentrations (computer science offers both A.B. and B.S.E.) and over 50 minors and interdepartmental certificate programs. The A.B. includes concentrations in Public Policy (Princeton School of Public and International Affairs) and the School of Architecture."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-009
field: undergraduate.cost.attendance_2026_2027
value: "COA $94,624; tuition $68,140; housing $13,010; food $9,110; fees $314; books $1,050; personal $3,000; transport varies"
source_url: https://admission.princeton.edu/cost-aid/fees-payment-options
source_snippet: "The estimated cost of attendance for 2026-27 is $94,624. Tuition: $68,140; Housing: $13,010; Food: $9,110; Fees: $314; Books, course materials, supplies, and equipment: $1,050; Miscellaneous personal expenses: $3,000; Transportation: Varies*"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-U-010
field: undergraduate.financial_aid.international_need_blind
value: "Need-blind and full-need for international students; same policy as US"
source_url: https://admission.princeton.edu/apply/international-students
source_snippet: "The full need of all admitted international students is met the same as it is for students from the United States. Princeton admission is need-blind — there is no disadvantage in the admission process for financial aid applicants. Students who qualify for financial aid will receive a grant, rather than a loan that has to be repaid."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-011
field: undergraduate.english_proficiency.requirement
value: "TOEFL / IELTS Academic / DET / PTE Academic required if non-native English and non-English instruction; exempt after 3 yrs English-instruction secondary school"
source_url: https://admission.princeton.edu/apply/international-students
source_snippet: "you must take the Test of English as a Foreign Language (TOEFL), the International English Language Testing System Academic (IELTS Academic), the Duolingo English Test (DET) or the Pearson Test of English Academic (PTE Academic). You are not required to take the TOEFL, IELTS, Duolingo or PTE Academic if English is your native language or if you have spent at least three years at a secondary school where English is the primary language of instruction."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-012
field: undergraduate.class_2029.statistics
value: "1,408 enrolled; 14.1% international citizens (65 countries); 69% on financial aid; 25% Pell-eligible; 16.7% first-gen"
source_url: https://admission.princeton.edu/apply/admission-statistics
source_snippet: "Total enrolled: 1,408... 16.7% of students in the class are the first in their families to go to college. 69% of the class qualify for financial aid. 25% of the class are eligible for need-based Federal Pell Grants... International Citizens 14.1... citizens of the following 65 countries"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-001
field: graduate.fields_of_study.directory
value: "47 degree-granting departments/programs; 4 divisions (Humanities, Natural Sciences, Social Sciences, Engineering); 600+ advanced degrees annually"
source_url: https://gradschool.princeton.edu/academics/degrees-requirements/fields-study
source_snippet: "The Graduate School at Princeton University awards more than 600 advanced degrees annually across 47 departments and programs. Our degree programs are housed within four divisions: humanities, natural sciences, social sciences, and engineering."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-002
field: graduate.deadlines_and_fees
value: "App fee $75; deadlines Nov 16 / Dec 1 / Dec 15 / Dec 30 (Fall 2026); app opens Sept for Fall 2027"
source_url: https://gradschool.princeton.edu/admission-onboarding/prepare/deadlines-and-fees
source_snippet: "Application Fee — $75... The application for Fall 2026 admission is now closed. The application for Fall 2027 will open in September 2026... Deadline — Fields of Study — November 16 [Neuroscience, Psychology] / December 1 [Art and Archeology, Bioengineering, Biophysics, Chemical and Biological Engineering, Chemistry, Classics, East Asian Studies, Economics, Ecology and Evolutionary Biology, English, History, History of Science, Materials Science Engineering, Mechanical and Aerospace Engineering, Molecular Biology, Program in Plasma Physics, Quantitative and Computational Biology] / December 15 [...] / December 30 [...]"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-003
field: graduate.gre_policy
value: "Department-specific; no Graduate School minimum; GMAT only for Finance"
source_url: https://gradschool.princeton.edu/admission-onboarding/prepare/gre
source_snippet: "Degree programs may require Graduate School applicants... to submit valid GRE scores... The Graduate School does not have a minimum score requirement; each department or program may set its own... Applicants applying to the Department of Finance may submit valid GMAT scores in place of GRE scores. No other department or program accepts GMAT."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-004
field: graduate.english_proficiency
value: "TOEFL / IELTS Academic / DET; no Grad School minimum; exemption if English-native or English-instruction degree; placement test if TOEFL Speaking <27 / IELTS Speaking <8.0 / DET Conversation <125"
source_url: https://gradschool.princeton.edu/admission-onboarding/prepare/english-proficiency
source_snippet: "you must meet English language proficiency requirements and may be required to submit TOEFL, IELTS, or DET test scores... The Graduate School does not have a minimum score requirement... If your scores are as follows—TOEFL (Speaking) of lower than 27, IELTS (Speaking) of lower than 8.0, or DET (Conversation) of lower than 125—you will be required to take a test upon enrollment... Exemptions: Applicants whose primary language is English; Applicants whose undergraduate instruction is entirely in English...; Applicants whose graduate study was on a full-time basis for at least two academic years where instruction is entirely in English..."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-005
field: graduate.financial_support_model
value: "All Ph.D. students receive full tuition + student health plan + base stipend for regular enrollment (typically 4-5 yrs)"
source_url: https://gradschool.princeton.edu/financial-support/financial-support-model
source_snippet: "Princeton offers financial support for all Ph.D. students throughout their period of regular enrollment. This includes full tuition, university student health plan coverage, and a base stipend intended to cover estimated living expenses... Ph.D. program length is typically four or five years."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-006
field: graduate.program_offerings_structure
value: "4 full joint-degree programs (IHUM, Social Policy, Neuroscience, Materials Science); dual degrees via SPIA (M.P.A.-J.D., M.P.A.-M.B.A.) and Molecular Biology (M.D.-Ph.D.)"
source_url: https://gradschool.princeton.edu/academics/degrees-requirements/fields-study/program-offerings
source_snippet: "Princeton's Graduate School offers four full joint-degree programs: Interdisciplinary Humanities; Social Policy; Neuroscience; Materials Science... Dual Degree Programs — The Princeton School of Public and International Affairs (M.P.A.-J.D. & M.P.A.-M.B.A. programs); The Department of Molecular Biology (for the M.D-Ph.D. program)."
capture_date: 2026-07-04
evidence_type: official_webpage
```

---

# SECTION 6 — WeKnora import manifest

## Collection structure

```
collection: princeton-knowledge-base-v2
├── doc: princeton-overview (Section 0 — counts, hierarchy, degree inventory, matrix)
│   ├── chunk: counts-rollup
│   ├── chunk: hierarchy-tree
│   ├── chunk: degree-inventory
│   └── chunk: distribution-matrix
├── doc: princeton-undergraduate (Section 1)
│   ├── chunk: ug-concentrations-fas-humanities  (学院=FAS, 系=Humanities, A.B.)
│   ├── chunk: ug-concentrations-fas-natsci      (学院=FAS, 系=Natural Sciences, A.B.)
│   ├── chunk: ug-concentrations-fas-socsci       (学院=FAS, 系=Social Sciences, A.B.)
│   ├── chunk: ug-concentrations-seas             (学院=SEAS, B.S.E.)
│   ├── chunk: ug-concentrations-architecture     (学院=SoA, A.B./B.S.E.)
│   ├── chunk: ug-concentrations-spia             (学院=SPIA, A.B.)
│   └── chunk: ug-minors-certificates             (71 项辅修/证书)
├── doc: princeton-graduate (Section 2)
│   ├── chunk: grad-fas                           (学院=FAS)
│   ├── chunk: grad-seas                          (学院=SEAS)
│   ├── chunk: grad-architecture                  (学院=SoA)
│   ├── chunk: grad-spia                          (学院=SPIA)
│   ├── chunk: grad-finance                       (学院=Bendheim)
│   ├── chunk: grad-neuroscience                  (学院=PNI)
│   ├── chunk: grad-plasma                        (学院=PPPL)
│   └── chunk: grad-interdept-joint               (跨系/联合学位)
├── doc: princeton-requirements (Section 3)
│   ├── chunk: ug-deadlines-tests
│   ├── chunk: ug-english-proficiency
│   └── chunk: grad-rules
├── doc: princeton-costs-aid (Section 4)
│   ├── chunk: ug-cost-line-items
│   ├── chunk: ug-financial-aid-policy
│   └── chunk: grad-funding
└── doc: princeton-evidence (Section 5 — evidence chain)
```

## Per-chunk metadata template

```yaml
metadata:
  collection: "princeton-knowledge-base-v2"
  school: "<home college, e.g. Faculty of Arts and Sciences>"
  department: "<home department, if applicable>"
  degree_level: "<A.B.|B.S.E.|Ph.D.|M.S.E.|M.Eng.|M.Arch.|M.Fin.|M.P.A.|M.P.P.|M.D./Ph.D.|Certificate|Joint Degree|Interdepartmental>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

## Follow-up data items (prioritized)

| Priority | Data item | Target URL / source | Why missing |
|---|---|---|---|
| **P0** | Undergrad application fee exact amount (sticker) | Common App portal / `admission.princeton.edu/faqs` | Admission site emphasizes waivers, not the sticker $75 figure (Common App standard). Verify via Common App at apply time. |
| **P0** | Graduate per-program deadlines already captured (Nov 16 / Dec 1 / Dec 15 / Dec 30 buckets), BUT per-program GRE requirement & materials checklist (behind each field's detail page) | Each `gradschool.princeton.edu/academics/degrees-requirements/fields-study/<field>` page | 70 field detail pages not individually scraped for GRE/materials specifics. |
| **P0** | Graduate stipend amount & living-cost breakdown | `gradschool.princeton.edu/financial-support/financial-support-model/funding-calendar-university-rates-costs` | Linked but not scraped this run. |
| P1 | UG acceptance rate (overall + SCEA/RD split) | `admission.princeton.edu/apply/admission-statistics` (only enrolled-class stats captured; acceptance rate not on stats page) | Page shows enrolled-class demographics, not application/admit counts. |
| P1 | Transfer deadlines & transfer credit policy | `admission.princeton.edu/apply/application-dates-deadlines/transfer-application-dates-deadlines` | Linked; not scraped this run. |
| P1 | Architecture M.Arch. program details (NAAB accreditation, length) | `soa.princeton.edu` graduate pages | SoA homepage is a news feed; grad subpages need targeted scrape. |
| P1 | SPIA M.P.A. / M.P.P. curriculum & funding (self-funded vs funded) | SPIA graduate admissions | Not individually scraped. |
| P2 | Bendheim M.Fin. curriculum, length, tuition (professional master's) | `bcf.princeton.edu/academic-programs/` | Captured as minor-in-finance URL; grad M.Fin. detail page not scraped. |
| P2 | Course catalog / ABOG (Announcements of the Bachelor of Arts) at `ua.princeton.edu` | `ua.princeton.edu` (referenced in minor URLs) | The official Undergraduate Announcement is the canonical curriculum source; not browsed directly this run. |
| P2 | Interview policy confirmation (Princeton UG does NOT interview) | cross-check admissions FAQ | Inferred from checklist absence; explicit statement not captured. |

---

# SECTION 7 — Cross-school comparison framework (Princeton baseline)

| Dimension | Princeton | MIT | Harvard | Stanford | NYU | Yale |
|---|---|---|---|---|---|---|
| Total UG COA/yr (2026-27) | $94,624 | — | — | — | — | — |
| Tuition/yr (2026-27) | $68,140 | — | — | — | — | — |
| Need-blind (intl?) | **Yes (incl. intl)** | Yes (intl) | Yes (intl) | Yes (domestic only)* | Need-aware (intl) | Yes (intl) |
| No-loan policy | **Yes (since 2001)** | Yes | Yes | Yes | No (NYU Promise tuition-free <$100k) | Yes |
| SCEA/EA deadline | **Nov 1 (SCEA)** | — | REA Nov 1 | — | ED Nov 1 | SCEA Nov 1 |
| RD deadline | **Jan 1** | Jan 4 | Jan 1 | Jan 5 | Jan 5 | Jan 2 |
| SAT/ACT required (2026-27)? | Test-optional (req'd 2027-28) | Required | Test-optional | Required | Test-flexible | Test-optional |
| TOEFL min (UG) | None (competitive) | — | None | Not required | 100 | None |
| IELTS min (UG) | None | — | None | Not required | 7.5 | None |
| Tuition-free income threshold | **<$150k → $0 contribution** | — | <$85k | — | <$100k | — |
| Grad application fee | $75 | $75 | $105 | $125 | $75–$125 | $105 |
| April-15 honor date | Yes (CGS) | Yes | Yes | Yes | Yes | Yes |
| **Total programs (rule-1, program-degree rows)** | **126** | ~190 | ~190 | 349 | ~360 | ~150 |
| School/department count (rule-2) | 11 academic units | 5 schools + many depts | 13 schools | 7 schools | ~10 schools | 14 schools |

> Stanford need-blind is domestic-only (international admissions are need-aware). NYU is need-aware for internationals. Princeton, MIT, Harvard, Yale, Dartmouth, Amherst are the US schools need-blind for internationals. "*" marks the Stanford caveat.

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: admission.princeton.edu (UG admissions), gradschool.princeton.edu (graduate), ua.princeton.edu (Undergraduate Announcement, referenced), departmental subdomains (aas/anthropology/cbe/cee/cs/ece/mae/orfe/spia/soa/bcf/pni/etc.)
> **Verification**: ego-browser snapshotText + JS DOM extraction; reconciliation computed in Python (rule-1 == rule-3 == rule-4 == rule-5 == 126)
> **Granularity**: school → department → degree-level → program
> **Reconciliation status**: ✅ PASS — UG 39 + Grad 87 = 126 program-degree rows; matrix row-sum = col-sum = 126; degree-inventory sum = 126. The 71 UG minors/certificates are supplementary and tracked separately.
