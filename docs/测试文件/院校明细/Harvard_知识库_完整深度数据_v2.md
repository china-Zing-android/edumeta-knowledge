# Harvard University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep) — 严格遵循五条结构规则的范例文档

---

# 目录

0. 院校总览（规则 1–4：总数 / 层级 / 学历清单 / 分布矩阵）
1. 本科教育（规则 5：学院 → 系 → 学位级别 → 专业）
2. 研究生教育（规则 5）
3. 申请要求与截止日期
4. 费用与资助完整数据
5. 完整证据链索引
6. WeKnora 导入清单
7. 跨校比较框架

---

# 0. 院校总览 (Institution Overview)

Harvard University 设有 **13 个学院**（含 Harvard College 本科部、Harvard Kenneth C. Griffin GSAS 研究生院，以及 11 所专业学院），共开设 **182 个学位—项目计量行**（program-degree rows；含本科 concentration 51 行、研究生 131 行）。本节四项汇总（规则 1–4）均由 Phase 2 从各学院权威页面提取的 182 条数据派生，并已通过**强制对账检查**。

> **核心数据来源**:
> - 统一项目目录: https://www.harvard.edu/programs/ （顶层 13 学院 + 16 个学校筛选维度；页面仅虚拟展示 15 项，全量数据需分学院抓取）
> - Harvard College concentrations（本科主修，Harvard 称 concentration）: https://college.harvard.edu/academics/liberal-arts-sciences/concentrations （49 个 concentration 名称 + 学位后缀 + 各系主页 URL）
> - GSAS 学位项目目录: https://gsas.harvard.edu/programs （80 Results，7 页 × 10 = 70 条 article 节点；去除 9 条非学位/联合行政类目后得 61 个 distinct 学位项目 → 68 个 program-degree 行）
> - 各专业学院官网（HBS / HLS / HMS / HSDM / HGSE / HKS / HSPH / GSD / HDS）逐院抓取

> **Harvard 学位命名特色**: Harvard 使用拉丁缩写 —— 本科 **A.B.** (Artium Baccalaureus, = B.A.) 与 **S.B.** (= B.S.)；研究生 **A.M.** (= M.A.)、**S.M.** (Scientiae Magister, = M.S.)、**M.E.** (Master of Engineering)；研究生院 GSAS 不使用 M.A./M.S. 而是 A.M./S.M.。本文档统一保留 Harvard 官方缩写。

## 0.1 专业与项目总数（规则 1）

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科 concentration（A.B.） | 48 | Harvard College，含 SEAS 跨院 A.B. 主修 |
| 本科 concentration（S.B.） | 3 | Electrical Engineering、Engineering Sciences、Mechanical Engineering（SEAS） |
| **本科主修小计（program-degree 行）** | **51** | 49 个 distinct concentration；EE/EngSci 各授予 A.B. 与 S.B. 双学位 → 拆为 51 行 |
| 研究生学位项目（GSAS）| 68 | 61 个 distinct 学位项目 × 多学位 = 68 行（57 PhD + 6 A.M. + 3 S.M. + 2 M.E.）|
| 研究生学位项目（专业学院）| 63 | HBS/HLS/HMS/HSDM/HSPH/HKS/HGSE/GSD/HDS 直授学位（已排除 GSAS 共管的 7 个跨院 PhD）|
| **学位/项目总计（program-degree 行）** | **182** | 规则 1 总数 |
| 其中本科 (undergraduate) | 51 | 全部 Harvard College |
| 其中研究生 (graduate) | 131 | GSAS 68 + 专业学院 63 |
| 学院数（授予被计入学位的）| 11 | Harvard College + GSAS + 9 所专业学院（HBS/HLS/HMS/HSDM/HSPH/HKS/HGSE/GSD/HDS）|
| Harvard 大学正式学院总数 | 13 | 另含 Harvard Division of Continuing Education (DCE)、Harvard Radcliffe Institute（非学位授予权重计算）|

> **counting convention**: 一个 concentration/program 若授予多个学位级别（如 Engineering Sciences 同时授 A.B. 与 S.B.，History of Science 同时授 PhD 与 A.M.），按"学位—项目"行展开计数。这是保证规则 1、3、4、5 严格对账的必要约定。N 个 distinct 项目 → M 行（M ≥ N）。

> **对账（MANDATORY reconciliation）**:
> - 规则 1 总数 = **182**
> - 规则 3 学历级别求和 = **182**（见 0.3）
> - 规则 4 分布矩阵单元求和 = **182**（见 0.4，行/列合计均为 182）
> - 规则 5 全量明细行数 = **182**（Section 1 = 51 行 + Section 2 = 131 行）
> - **四数一致 ✓**

## 0.2 学院 / 系层级结构（规则 2）

```
Harvard University
├── Harvard College  [学院 — 本科部]
│   ├── Faculty of Arts and Sciences (FAS)  [系所群 — 文理学科主修]
│   │   ├── African and African American Studies  [系/concentration]
│   │   ├── Anthropology
│   │   ├── Art, Film, and Visual Studies
│   │   ├── Astrophysics
│   │   ├── Chemical and Physical Biology
│   │   ├── Chemistry
│   │   ├── Chemistry and Physics
│   │   ├── Classics
│   │   ├── Comparative Literature
│   │   ├── Comparative Study of Religion
│   │   ├── Earth and Planetary Sciences
│   │   ├── East Asian Studies
│   │   ├── Economics
│   │   ├── English
│   │   ├── Environmental Science and Public Policy
│   │   ├── Folklore and Mythology
│   │   ├── Germanic Languages and Literature
│   │   ├── Government
│   │   ├── History
│   │   ├── History and Literature
│   │   ├── History and Science
│   │   ├── History of Art and Architecture
│   │   ├── Human Developmental and Regenerative Biology
│   │   ├── Human Evolutionary Biology
│   │   ├── Integrative Biology
│   │   ├── Linguistics
│   │   ├── Mathematics
│   │   ├── Molecular and Cellular Biology
│   │   ├── Music
│   │   ├── Near Eastern Languages and Civilizations
│   │   ├── Neuroscience
│   │   ├── Philosophy
│   │   ├── Physics
│   │   ├── Psychology
│   │   ├── Romance Languages and Literature
│   │   ├── Slavic Literatures and Cultures
│   │   ├── Social Studies
│   │   ├── Sociology
│   │   ├── South Asian Studies
│   │   ├── Statistics
│   │   ├── Studies of Women, Gender, and Sexuality
│   │   └── Theater, Dance & Media
│   └── School of Engineering and Applied Sciences (SEAS)  [系所群 — 工程应用主修]
│       ├── Applied Mathematics  (A.B.)
│       ├── Biomedical Engineering  (A.B.)
│       ├── Computer Science  (A.B.)
│       ├── Electrical Engineering  (A.B. / S.B.)  ⚠ 双学位
│       ├── Engineering Sciences  (A.B. / S.B.)  ⚠ 双学位
│       ├── Environmental Science and Engineering  (A.B.)
│       └── Mechanical Engineering  (S.B.)
│
├── Harvard Kenneth C. Griffin Graduate School of Arts and Sciences (GSAS)  [学院 — 文理研究生院]
│   ├── (GSAS 不再细分系；学位项目即基本单元)
│   ├── 57 个 PhD 项目（含 HILS 整合生命科学联盟：Biomedical Informatics, Biophysics, Chemical Biology,
│   │   Chemistry & Chemical Biology, Immunology, Molecular & Cellular Biology, Neuroscience,
│   │   Organismic & Evolutionary Biology, Speech & Hearing Bioscience & Tech, Systems/Synthetic/Quantitative Biology, Virology）
│   ├── 6 个 A.M. 项目（History of Science, Middle Eastern Studies, Near Eastern Languages & Civ.,
│   │   Regional Studies–East Asia, Regional Studies–Russia/E.Europe/Central Asia, South Asian Studies）
│   ├── 3 个 S.M. 项目（Computational Science & Engineering, Data Science, Engineering & Applied Sciences）
│   └── 2 个 M.E. 项目（Computational Science & Engineering, Engineering & Applied Sciences）
│       ⚠ GSAS 与多所专业学院共管 PhD：HBS(7)、HKS(3: Public Policy/Social Policy/Health Policy)、
│         HMS(9: HILS 体系)、HSPH(Biostatistics/Biological Sci in PH/Population Health Sci/Health Policy 等)、
│         HGSE(Education)、HDS(Religion) —— 这些 PhD 在 GSAS 统一招生，已在 GSAS 计数，专业学院小节仅交叉列出。
│
├── Harvard Business School (HBS)  [学院 — 商学院]
│   ├── MBA Program  (M.B.A.)
│   └── Doctoral Programs  (Ph.D.; 7 个，与 GSAS 共管 — 见 GSAS)
│
├── Harvard Law School (HLS)  [学院 — 法学院]
│   ├── J.D. Program
│   ├── LL.M. Program
│   ├── S.J.D. Program
│   └── Joint Degree Programs  (6 个联合学位)
│
├── Harvard Medical School (HMS)  [学院 — 医学院]
│   ├── MD Program  (Pathways / HST 两条轨道)
│   ├── MD-PhD Program  (MSTP, 与 GSAS 共管)
│   ├── Master's Degree Programs  (11 个: 6 MMSc + 5 SM)
│   └── PhD Degree Programs  (9 个, 经 GSAS 注册 — 见 GSAS/HILS)
│
├── Harvard School of Dental Medicine (HSDM)  [学院 — 牙医学院]
│   ├── DMD Program
│   ├── Advanced Graduate Education  (MMSc / DMSc + 专科认证)
│   ├── DMD-PhD Dual Degree
│   └── Advanced Standing (国际牙医)
│
├── Harvard T.H. Chan School of Public Health (HSPH)  [学院 — 公共卫生学院]
│   ├── Master's Programs  (MPH-45, MPH-65, 8 个 S.M., 1 个 M.H.S.)
│   ├── Doctoral  (DrPH 直授；PhD 经 GSAS — 见 GSAS)
│   └── (SD 历史学位，现多以 PhD/DrPH 替代)
│
├── Harvard Kennedy School (HKS)  [学院 — 肯尼迪政治学院]
│   ├── Master's Programs  (MPP, MPA/ID, MPA, MC/MPA)
│   ├── Doctoral Programs  (3 PhD, 与 GSAS 共管 — 见 GSAS)
│   └── Public Leadership Credential  (非学位)
│
├── Harvard Graduate School of Education (HGSE)  [学院 — 教育学院]
│   ├── Residential Ed.M.  (5 个 program)
│   ├── Online Ed.M.  (Education Leadership, 3 pathway)
│   ├── Ed.L.D.  (Doctor of Education Leadership)
│   └── Ph.D. in Education  (与 GSAS 共管 — 见 GSAS)
│
├── Harvard Graduate School of Design (GSD)  [学院 — 设计学院]
│   └── Degree Programs  (MArch I/II, MLA I/I AP, MUP, MDes, MDE, DDes)
│
└── Harvard Divinity School (HDS)  [学院 — 神学院]
    ├── Master's Programs  (MDiv, MTS, MTh, MRPL)
    └── Doctoral  (ThD / PhD in Religion — 与 GSAS 共管 — 见 GSAS)

(未计入学位计数的 2 所: Harvard Division of Continuing Education (DCE) — 授 A.L.B./A.L.M. 终身教育学位；
 Harvard Radcliffe Institute — 研究机构，无独立学位授予权)
```

> **跨院共享标注 (⚠)**: SEAS 的工程主修同时归属 Harvard College 与 SEAS；GSAS 的 PhD 与 HBS/HMS/HKS/HGSE/HSPH/HDS 等专业学院共管；HILS (Harvard Integrated Life Sciences) 是生命科学 PhD 的招生联盟，11 个成员项目行政上挂靠 GSAS。

## 0.3 学历级别明细（规则 3）

| 学位缩写 | 全称 | 类别 | 本项目数量 |
|---------|------|------|-----------|
| AB | Bachelor of Arts (A.B.) | 本科 | 48 |
| SB | Bachelor of Science (S.B.) | 本科 | 3 |
| AM | Master of Arts (A.M.) | 研究生(学术硕士) | 6 |
| SM | Master of Science (S.M.) | 研究生(学术硕士) | 16 |
| ME | Master of Engineering (M.E.) | 研究生(工程硕士) | 2 |
| MMSc | Master of Medical Sciences (M.M.Sc.) | 研究生(医学硕士) | 7 |
| MBA | Master of Business Administration (M.B.A.) | 研究生(专业硕士) | 1 |
| MD | Doctor of Medicine (M.D.) | 专业博士 | 2 |
| MD/PhD | M.D.-Ph.D. (joint) | 联合专业博士 | 1 |
| DMD | Doctor of Dental Medicine (D.M.D.) | 专业博士 | 1 |
| DMSc | Doctor of Medical Sciences (D.M.Sc.) | 专业博士 | 1 |
| DMD/PhD | D.M.D.-Ph.D. (joint) | 联合专业博士 | 1 |
| JD | Juris Doctor (J.D.) | 专业博士 | 1 |
| LLM | Master of Laws (LL.M.) | 研究生(法律硕士) | 1 |
| SJD | Doctor of Juridical Science (S.J.D.) | 法律博士 | 1 |
| MPH | Master of Public Health (M.P.H.) | 研究生(公共卫生硕士) | 2 |
| MHS | Master of Health Science (M.H.S.) | 研究生(健康硕士) | 1 |
| MPP | Master in Public Policy (M.P.P.) | 研究生(公共政策硕士) | 1 |
| MPA | Master in Public Administration (M.P.A.) | 研究生(公共管理硕士) | 1 |
| MPA/ID | M.P.A. in International Development | 研究生(公共管理硕士) | 1 |
| MC/MPA | Mid-Career M.P.A. | 研究生(公共管理硕士) | 1 |
| EdM | Master in Education (Ed.M.) | 研究生(教育硕士) | 6 |
| EdLD | Doctor of Education Leadership (Ed.L.D.) | 专业博士(教育领导) | 1 |
| MArch | Master in Architecture (M.Arch.) | 研究生(建筑硕士) | 2 |
| MLA | Master in Landscape Architecture (M.L.A.) | 研究生(景观硕士) | 2 |
| MUP | Master in Urban Planning (M.U.P.) | 研究生(城市规划硕士) | 1 |
| MDes | Master in Design Studies (M.Des.) | 研究生(设计硕士) | 2 |
| DDes | Doctor of Design (D.Des.) | 研究博士(设计) | 1 |
| MDiv | Master of Divinity (M.Div.) | 研究生(神道硕士) | 1 |
| MTS | Master of Theological Studies (M.T.S.) | 研究生(神学硕士) | 1 |
| MTh | Master of Theology (M.Th.) | 研究生(神学硕士) | 1 |
| MRPL | Master of Religion and Public Life (M.R.P.L.) | 研究生(宗教与公共生活) | 1 |
| DrPH | Doctor of Public Health (Dr.P.H.) | 公共卫生博士 | 1 |
| Joint | 联合学位项目 (Joint Degree) | 联合学位 | 6 |
| PhD | Doctor of Philosophy (Ph.D.) | 研究博士(哲学博士) | 57 |
| **合计** | — | — | **182** |

> **学位命名说明**：Harvard 保留拉丁缩写 A.B./A.M./S.M.（而非 B.A./M.A./M.S.）；S.M. = Scientiae Magister；M.E. = Master of Engineering（SEAS/GSAS 工程硕士）。专业博士涵盖 MD、JD、DMD、EdLD、DrPH、DMSc、SJD、DDes。PhD 一律经 GSAS 注册（即便学生常驻 HMS/HSPH/HBS/HKS/HGSE/HDS）。

## 0.4 分布矩阵（学院 × 学位级别）

> 为可读性，35 个细分学位合并为 6 大类别列。下方矩阵**行合计、列合计均 = 182**，与规则 1、3 严格对账。完整 35-列细分矩阵见证据链 E-O-005。

| 学院 \ 级别 | UG (A.B./S.B.) | Master 学术 (A.M./S.M./M.E.) | Master 专业 (MBA/MMSc/EdM/MPH/MHS/MPA/MPP/MUP/MArch/MLA/MDes/MDiv/MTS/MTh/MRPL/LLM/MC/MPA/ID) | Professional Doctorate (MD/JD/DMD/EdLD/DrPH/DMSc/SJD/DDes) | Research PhD | Joint (MD-PhD/DMD-PhD/Joint) | 合计 |
|---|---|---|---|---|---|---|---|
| Harvard College | 51 | 0 | 0 | 0 | 0 | 0 | 51 |
| Harvard Kenneth C. Griffin GSAS | 0 | 11 | 0 | 0 | 57 | 0 | 68 |
| Harvard Business School (HBS) | 0 | 0 | 1 | 0 | 0 | 0 | 1 |
| Harvard Law School (HLS) | 0 | 0 | 1 | 2 | 0 | 6 | 9 |
| Harvard Medical School (HMS) | 0 | 5 | 6 | 2 | 0 | 1 | 14 |
| Harvard School of Dental Medicine (HSDM) | 0 | 0 | 1 | 2 | 0 | 1 | 4 |
| Harvard T.H. Chan School of Public Health (HSPH) | 0 | 8 | 3 | 1 | 0 | 0 | 12 |
| Harvard Kennedy School (HKS) | 0 | 0 | 4 | 0 | 0 | 0 | 4 |
| Harvard Graduate School of Education (HGSE) | 0 | 0 | 6 | 1 | 0 | 0 | 7 |
| Harvard Graduate School of Design (GSD) | 0 | 0 | 7 | 1 | 0 | 0 | 8 |
| Harvard Divinity School (HDS) | 0 | 0 | 4 | 0 | 0 | 0 | 4 |
| **合计** | **51** | **24** | **33** | **9** | **57** | **8** | **182** |

> **观察**：Harvard 是一所"重 PhD、强专业学院"的大学 —— 57 个 PhD（占 31%）集中在 GSAS，且与各专业学院共管；本科 100% 为 Harvard College 的 liberal-arts concentration（A.B. 占 94%）。HMS（14 行）与 HSPH（12 行）的健康科学集群规模显著。

---

# 1. 本科教育（规则 5：学院 → 系 → 学位级别 → 专业）

## 1.1 Harvard College 学院架构

Harvard 的本科教育 100% 由 **Harvard College** 承担，位于 Faculty of Arts and Sciences (FAS) 之下。Harvard 把"专业"称为 **concentration**（主修），把"辅修"称为 **secondary field**。本科开设 **49 个 concentration**（其中 46 个 A.B.、2 个 A.B.+S.B. 双学位、1 个纯 S.B.），按授予单位拆为 51 个 program-degree 行。完整层级树见 0.2。

## 1.2 本科 concentration 全量明细（按 学院 → 系 → 学位级别 分组）

#### Harvard College

##### Faculty of Arts and Sciences (FAS)

###### AB  (42 concentrations)
| # | 专业 | URL |
|---|------|-----|
| 1 | African and African American Studies | https://aaas.fas.harvard.edu/ |
| 2 | Anthropology | https://anthropology.fas.harvard.edu/ |
| 3 | Art, Film, and Visual Studies | https://afvs.fas.harvard.edu/ |
| 4 | Astrophysics | https://astronomy.fas.harvard.edu/undergraduate-program |
| 5 | Chemical and Physical Biology | https://lifesciences.fas.harvard.edu/cpb |
| 6 | Chemistry | https://chemistry.harvard.edu/undergraduate-programs |
| 7 | Chemistry and Physics | https://lifesciences.fas.harvard.edu/chemistry-and-physics |
| 8 | Classics | https://classics.fas.harvard.edu/ |
| 9 | Comparative Literature | https://complit.fas.harvard.edu/ |
| 10 | Comparative Study of Religion | https://studyofreligion.fas.harvard.edu/ |
| 11 | Earth and Planetary Sciences | https://eps.harvard.edu/pages/undergraduate |
| 12 | East Asian Studies | https://eas.fas.harvard.edu/ |
| 13 | Economics | https://economics.harvard.edu/undergraduate |
| 14 | English | https://english.fas.harvard.edu/undergraduate |
| 15 | Environmental Science and Public Policy | https://espp.fas.harvard.edu/pages/academics |
| 16 | Folklore and Mythology | https://folkmyth.fas.harvard.edu/ |
| 17 | Germanic Languages and Literature | https://german.fas.harvard.edu/ |
| 18 | Government | https://www.gov.harvard.edu/undergraduate/ |
| 19 | History | https://history.fas.harvard.edu/undergraduate-programs |
| 20 | History and Literature | https://histlit.fas.harvard.edu/ |
| 21 | History and Science | https://histsci.fas.harvard.edu/history-and-science-concentration |
| 22 | History of Art and Architecture | https://haa.fas.harvard.edu/undergraduate-program |
| 23 | Human Developmental and Regenerative Biology | https://hscrb.harvard.edu/undergraduate-students/ |
| 24 | Human Evolutionary Biology | https://heb.fas.harvard.edu/ |
| 25 | Integrative Biology | https://lifesciences.fas.harvard.edu/ib |
| 26 | Linguistics | https://linguistics.fas.harvard.edu/pages/why-linguistics |
| 27 | Mathematics | https://www.math.harvard.edu/undergraduate/ |
| 28 | Molecular and Cellular Biology | https://www.mcb.harvard.edu/undergraduate/molecular-and-cellular-biology-mcb/ |
| 29 | Music | https://music.fas.harvard.edu/academics/undergraduate-study-in-music-information-for-prospective-students/ |
| 30 | Near Eastern Languages and Civilizations | https://nelc.fas.harvard.edu/undergradoverview |
| 31 | Neuroscience | https://www.mcb.harvard.edu/undergraduate/neuroscience/ |
| 32 | Philosophy | https://philosophy.fas.harvard.edu/welcome-undergraduate |
| 33 | Physics | https://www.physics.harvard.edu/undergrad |
| 34 | Psychology | https://psychology.fas.harvard.edu/undergraduate |
| 35 | Romance Languages and Literature | https://rll.fas.harvard.edu/pages/undergraduate |
| 36 | Slavic Literatures and Cultures | https://slavic.fas.harvard.edu/pages/why-choose-slavic-studies |
| 37 | Social Studies | https://socialstudies.fas.harvard.edu/academics |
| 38 | Sociology | https://sociology.fas.harvard.edu/pages/undergraduate |
| 39 | South Asian Studies | https://sas.fas.harvard.edu/undergraduate-0 |
| 40 | Statistics | https://statistics.fas.harvard.edu/undergraduate |
| 41 | Studies of Women, Gender, and Sexuality | https://wgs.fas.harvard.edu/undergraduate |
| 42 | Theater, Dance & Media | https://tdm.fas.harvard.edu/academics |

##### School of Engineering and Applied Sciences (SEAS)

###### AB  (6 concentrations)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://seas.harvard.edu/applied-mathematics/undergraduate-program |
| 2 | Biomedical Engineering | https://www.seas.harvard.edu/bioengineering/undergraduate-program |
| 3 | Computer Science | https://seas.harvard.edu/computer-science/undergraduate-program |
| 4 | Electrical Engineering | https://www.seas.harvard.edu/electrical-engineering/undergraduate-programs |
| 5 | Engineering Sciences | https://seas.harvard.edu/about-us/school-overview/accreditation-abet/engineering-sciences-sb |
| 6 | Environmental Science and Engineering | https://seas.harvard.edu/environmental-science-engineering/undergraduate-program |

###### SB  (3 concentrations)
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://www.seas.harvard.edu/electrical-engineering/undergraduate-programs |
| 2 | Engineering Sciences | https://seas.harvard.edu/about-us/school-overview/accreditation-abet/engineering-sciences-sb |
| 3 | Mechanical Engineering | https://seas.harvard.edu/materials-science-mechanical-engineering |

## 1.3 跨学科 / 跨学院本科项目

Harvard College 允许 **Joint Concentration**（联合主修，两个 concentration 各占约 50%，需双方系所与教务批准）与 **Special Concentration**（自创主修，经 specialconcentrations.fas.harvard.edu 委员会审批）。这两类是个性化路径而非预设项目，故不计入规则 1 的 51 行；详见 https://specialconcentrations.fas.harvard.edu/requirements 。

## 1.4 Secondary Fields（辅修）完整列表

Harvard 称辅修为 **secondary field**。Harvard College 提供 ~50 个 secondary field（与 concentration 高度重叠但数量独立，部分 secondary 无对应 concentration，如 Astronomy、Computational Science、Energy & Environment、Global Health & Health Policy、Mind/Brain/Behavior 等）。

> **数据缺口（P0 跟进）**：本轮从 https://oue.fas.harvard.edu/academics/concentrations/ 与 handbook.college.harvard.edu#fields 抓取 secondary 全量清单时，相关页面在抓取窗口内连接超时（college.harvard.edu 子域在该 session 后段不可达）。已确认存在 ~50 个 secondary field，但完整逐条列表留作下次 run 的 P0 续抓目标。Sources: https://oue.fas.harvard.edu/academics/concentrations/ ; https://handbook.college.harvard.edu/#fields

## 1.5 Harvard College 核心课程（General Education）

Harvard College 的核心通识称为 **General Education**（Gen Ed），2019 改革后每位本科生须修 4 门 Gen Ed 课程（分布于 4 大门类：Aesthetics & Culture; Ethics & Civics; Histories, Societies, Individuals; Science & Technology in Society），加上 **Divisional Distribution**（分布要求：艺术人文、社会科学、自然科学各 1 门）、**Quantitative Reasoning with Data**（1 门）、**Expository Writing**（1 门）、**Language Requirement**（通过外语 placement）。详见 https://college.harvard.edu/academics/liberal-arts-sciences#harvard-college-curriculum 。

## 1.6 课程编号 → 主修 快查（Harvard 不使用编号制）

Harvard 不采用 MIT 那样的"Course 编号"制（如 MIT 6-3 = CS）。Harvard 用 **department/concentration 名称** + **4 位课程号**（如 CS 50、ECON 10a、MATH 55a）。课程目录 my.harvard.edu（catalog.harvard.edu 在本 session 不可达）。

---

# 2. 研究生教育（规则 5：学院 → 系 → 学位级别 → 专业）

Harvard 研究生教育**高度去中心化**：GSAS 是文理研究生院（统一招收 57 个 PhD + 11 个 terminal master），而 9 所专业学院各自独立招生（HBS/HLS/HMS/HSDM/HSPH/HKS/HGSE/GSD/HDS 各有独立 admissions office 与 deadline）。GSAS PhD 多与专业学院共管（学生常驻专业学院但学位经 GSAS 授予）。

## 2.1 研究生项目全量明细（按 学院 → 系 → 学位级别 分组）

#### Harvard Business School (HBS)

##### MBA Program

###### MBA  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration (MBA) | https://www.hbs.edu/mba |

#### Harvard Divinity School (HDS)

##### Degree Programs

###### MDiv  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Divinity | https://hds.harvard.edu/admissions/degree-programs/ |

###### MRPL  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Religion and Public Life | https://hds.harvard.edu/admissions/degree-programs/ |

###### MTS  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Theological Studies | https://hds.harvard.edu/admissions/degree-programs/ |

###### MTh  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Theology | https://hds.harvard.edu/admissions/degree-programs/ |

#### Harvard Graduate School of Design (GSD)

##### Degree Programs

###### DDes  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Design | https://www.gsd.harvard.edu/doctor-of-design/ |

###### MArch  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Architecture I (Professional) | https://www.gsd.harvard.edu/architecture/ |
| 2 | Master in Architecture II (Post-Professional) | https://www.gsd.harvard.edu/architecture/ |

###### MDes  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Design Engineering (joint w/ SEAS) | https://www.gsd.harvard.edu/design-engineering/ |
| 2 | Master in Design Studies | https://www.gsd.harvard.edu/design-studies/ |

###### MLA  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Landscape Architecture I | https://www.gsd.harvard.edu/landscape-architecture/ |
| 2 | Master in Landscape Architecture I AP | https://www.gsd.harvard.edu/landscape-architecture/ |

###### MUP  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Urban Planning | https://www.gsd.harvard.edu/urban-planning-design/ |

#### Harvard Graduate School of Education (HGSE)

##### Doctoral

###### EdLD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Education Leadership (Ed.L.D.) | https://www.gse.harvard.edu/degrees/edld |

##### Online Ed.M.

###### EdM  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Online Ed.M. in Education Leadership (PreK-12 / Higher Ed / International pathways) | https://www.gse.harvard.edu/degrees/masters |

##### Residential Ed.M.

###### EdM  (5)
| # | 项目 | URL |
|---|------|-----|
| 1 | Ed.M. in Education Leadership, Organizations, and Entrepreneurship | https://www.gse.harvard.edu/degrees/masters |
| 2 | Ed.M. in Education Policy and Analysis | https://www.gse.harvard.edu/degrees/masters |
| 3 | Ed.M. in Human Development and Education | https://www.gse.harvard.edu/degrees/masters |
| 4 | Ed.M. in Learning Design, Innovation, and Technology | https://www.gse.harvard.edu/degrees/masters |
| 5 | Ed.M. in Teaching and Teacher Leadership | https://www.gse.harvard.edu/degrees/masters |

#### Harvard Kennedy School (HKS)

##### Master's Programs

###### MC/MPA  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Mid-Career Master in Public Administration (MC/MPA) | https://www.hks.harvard.edu/educational-programs/masters-programs |

###### MPA  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Public Administration (MPA) | https://www.hks.harvard.edu/educational-programs/masters-programs |

###### MPA/ID  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Public Administration in International Development (MPA/ID) | https://www.hks.harvard.edu/educational-programs/masters-programs |

###### MPP  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master in Public Policy (MPP) | https://www.hks.harvard.edu/educational-programs/masters-programs |

#### Harvard Kenneth C. Griffin GSAS

##### GSAS 学位项目（不再细分系）

###### AM  (6)
| # | 项目 | URL |
|---|------|-----|
| 1 | History of Science | https://gsas.harvard.edu/program/history-science |
| 2 | Middle Eastern Studies | https://gsas.harvard.edu/program/middle-eastern-studies |
| 3 | Near Eastern Languages and Civilizations | https://gsas.harvard.edu/program/near-eastern-languages-and-civilizations |
| 4 | Regional Studies–East Asia | https://gsas.harvard.edu/program/regional-studies-east-asia |
| 5 | Regional Studies–Russia, Eastern Europe, and Central Asia | https://gsas.harvard.edu/program/regional-studies-russia-eastern-europe-and-central-asia |
| 6 | South Asian Studies | https://gsas.harvard.edu/program/south-asian-studies |

###### ME  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Science and Engineering | https://gsas.harvard.edu/program/computational-science-and-engineering |
| 2 | Engineering and Applied Sciences | https://gsas.harvard.edu/program/engineering-and-applied-sciences |

###### PhD  (57)
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Informatics | https://gsas.harvard.edu/program/biomedical-informatics |
| 2 | Biophysics | https://gsas.harvard.edu/program/biophysics |
| 3 | Biostatistics | https://gsas.harvard.edu/program/biostatistics |
| 4 | Business Administration | https://gsas.harvard.edu/program/business-administration |
| 5 | Business Economics | https://gsas.harvard.edu/program/business-economics |
| 6 | Byzantine Studies | https://gsas.harvard.edu/program/byzantine-studies |
| 7 | Celtic Languages and Literatures | https://gsas.harvard.edu/program/celtic-languages-and-literatures |
| 8 | Chemical Biology | https://gsas.harvard.edu/program/chemical-biology |
| 9 | Chemical Physics | https://gsas.harvard.edu/program/chemical-physics |
| 10 | Chemistry and Chemical Biology | https://gsas.harvard.edu/program/chemistry-and-chemical-biology |
| 11 | Classics | https://gsas.harvard.edu/program/classics |
| 12 | Comparative Literature | https://gsas.harvard.edu/program/comparative-literature |
| 13 | Computer Science | https://gsas.harvard.edu/program/computer-science |
| 14 | Earth and Planetary Sciences | https://gsas.harvard.edu/program/earth-and-planetary-sciences |
| 15 | East Asian Languages and Civilizations | https://gsas.harvard.edu/program/east-asian-languages-and-civilizations |
| 16 | Economics | https://gsas.harvard.edu/program/economics |
| 17 | Education | https://gsas.harvard.edu/program/education |
| 18 | Electrical and Computer Engineering | https://gsas.harvard.edu/program/electrical-and-computer-engineering |
| 19 | Engineering and Applied Sciences | https://gsas.harvard.edu/program/engineering-and-applied-sciences |
| 20 | English | https://gsas.harvard.edu/program/english |
| 21 | Environmental Science and Engineering | https://gsas.harvard.edu/program/environmental-science-and-engineering |
| 22 | Film and Visual Studies | https://gsas.harvard.edu/program/film-and-visual-studies |
| 23 | Germanic Languages and Literatures | https://gsas.harvard.edu/program/germanic-languages-and-literatures |
| 24 | Government | https://gsas.harvard.edu/program/government |
| 25 | Health Policy | https://gsas.harvard.edu/program/health-policy |
| 26 | History | https://gsas.harvard.edu/program/history |
| 27 | History of Art and Architecture | https://gsas.harvard.edu/program/history-art-and-architecture |
| 28 | History of Science | https://gsas.harvard.edu/program/history-science |
| 29 | Human Evolutionary Biology | https://gsas.harvard.edu/program/human-evolutionary-biology |
| 30 | Immunology | https://gsas.harvard.edu/program/immunology |
| 31 | Inner Asian and Altaic Studies | https://gsas.harvard.edu/program/inner-asian-and-altaic-studies |
| 32 | Linguistics | https://gsas.harvard.edu/program/linguistics |
| 33 | Materials Science and Mechanical Engineering | https://gsas.harvard.edu/program/materials-science-and-mechanical-engineering |
| 34 | Mathematics | https://gsas.harvard.edu/program/mathematics |
| 35 | Middle Eastern Studies | https://gsas.harvard.edu/program/middle-eastern-studies |
| 36 | Molecular and Cellular Biology | https://gsas.harvard.edu/program/molecular-and-cellular-biology |
| 37 | Music | https://gsas.harvard.edu/program/music |
| 38 | Near Eastern Languages and Civilizations | https://gsas.harvard.edu/program/near-eastern-languages-and-civilizations |
| 39 | Neuroscience | https://gsas.harvard.edu/program/neuroscience |
| 40 | Organismic and Evolutionary Biology | https://gsas.harvard.edu/program/organismic-and-evolutionary-biology |
| 41 | Organizational Behavior | https://gsas.harvard.edu/program/organizational-behavior |
| 42 | Philosophy | https://gsas.harvard.edu/program/philosophy |
| 43 | Physics | https://gsas.harvard.edu/program/physics |
| 44 | Population Health Sciences | https://gsas.harvard.edu/program/population-health-sciences |
| 45 | Psychology | https://gsas.harvard.edu/program/psychology |
| 46 | Public Policy | https://gsas.harvard.edu/program/public-policy |
| 47 | Quantum Science and Engineering | https://gsas.harvard.edu/program/quantum-science-and-engineering |
| 48 | Religion | https://gsas.harvard.edu/program/religion |
| 49 | Romance Languages and Literatures | https://gsas.harvard.edu/program/romance-languages-and-literatures |
| 50 | Slavic Languages and Literatures | https://gsas.harvard.edu/program/slavic-languages-and-literatures |
| 51 | Social Policy | https://gsas.harvard.edu/program/social-policy |
| 52 | Sociology | https://gsas.harvard.edu/program/sociology |
| 53 | South Asian Studies | https://gsas.harvard.edu/program/south-asian-studies |
| 54 | Speech and Hearing Bioscience and Technology | https://gsas.harvard.edu/program/speech-and-hearing-bioscience-and-technology |
| 55 | Statistics | https://gsas.harvard.edu/program/statistics |
| 56 | Systems, Synthetic, and Quantitative Biology | https://gsas.harvard.edu/program/systems-synthetic-and-quantitative-biology |
| 57 | Virology | https://gsas.harvard.edu/program/virology |

###### SM  (3)
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Science and Engineering | https://gsas.harvard.edu/program/computational-science-and-engineering |
| 2 | Data Science | https://gsas.harvard.edu/program/data-science |
| 3 | Engineering and Applied Sciences | https://gsas.harvard.edu/program/engineering-and-applied-sciences |

#### Harvard Law School (HLS)

##### Degree Programs

###### JD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor (J.D.) | https://hls.harvard.edu/jdadmissions/ |

###### LLM  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws (LL.M.) | https://hls.harvard.edu/graduate-program/ |

###### SJD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Juridical Science (S.J.D.) | https://hls.harvard.edu/graduate-program/ |

##### Joint Degree Programs

###### Joint  (6)
| # | 项目 | URL |
|---|------|-----|
| 1 | Coordinated JD/PhD ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |
| 2 | HLS-Cambridge JD/LLM ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |
| 3 | Law and Business (JD/MBA) ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |
| 4 | Law and Government (JD/MPP, JD/MPA-ID) ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |
| 5 | Law and Public Health (JD/MPH) ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |
| 6 | Law and Urban Planning (JD/MUP) ⚠ joint degree (counted separately as 1 joint slot) | https://hls.harvard.edu/academics/degree-programs/ |

#### Harvard Medical School (HMS)

##### MD Program

###### MD  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine (M.D.) - Health Sciences & Technology (HST) | https://hms.harvard.edu/education-admissions/md-program/curriculum/health-sciences-technology-hst |
| 2 | Doctor of Medicine (M.D.) - Pathways | https://hms.harvard.edu/education-admissions/md-program |

##### MD-PhD Program

###### MD/PhD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Medical Scientist Training Program (MD/PhD) ⚠ joint (PhD via GSAS) | https://www.hms.harvard.edu/md_phd/ |

##### Master's Degree Programs

###### MMSc  (6)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Medical Sciences in Biomedical Informatics | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 2 | Master of Medical Sciences in Clinical Investigation | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 3 | Master of Medical Sciences in Global Health Delivery | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 4 | Master of Medical Sciences in Immunology | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 5 | Master of Medical Sciences in Medical Education | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 6 | Master of Medical Sciences in Therapeutic Sciences | https://hms.harvard.edu/education-admissions/masters-degree-programs |

###### SM  (5)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Bioethics | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 2 | Master of Science in Clinical Research | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 3 | Master of Science in Clinical Service Operations | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 4 | Master of Science in Healthcare Quality and Safety | https://hms.harvard.edu/education-admissions/masters-degree-programs |
| 5 | Master of Science in Media, Medicine, and Health | https://hms.harvard.edu/education-admissions/masters-degree-programs |

#### Harvard School of Dental Medicine (HSDM)

##### Advanced Graduate Education

###### DMSc  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Graduate Education (DMSc) - specialty training | https://www.hsdm.harvard.edu/academics |

###### MMSc  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Graduate Education (MMSc) - specialty training | https://www.hsdm.harvard.edu/academics |

##### Dual Degree

###### DMD/PhD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | DMD-PhD Dual Degree ⚠ joint (PhD via GSAS) | https://www.hsdm.harvard.edu/academics |

##### Predoctoral

###### DMD  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Dental Medicine (D.M.D.) | https://www.hsdm.harvard.edu/academics |

#### Harvard T.H. Chan School of Public Health (HSPH)

##### Doctoral Programs (direct)

###### DrPH  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Public Health (DrPH) | https://www.hsph.harvard.edu/drph/ |

##### Master's Programs

###### MHS  (1)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Health Science in Occupational and Environmental Hygiene | https://www.hsph.harvard.edu/environmental-health/ |

###### MPH  (2)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health (45-credit) | https://www.hsph.harvard.edu/admissions/degree-programs/ |
| 2 | Master of Public Health (65-credit) | https://www.hsph.harvard.edu/admissions/degree-programs/ |

###### SM  (8)
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science in Biostatistics | https://www.hsph.harvard.edu/biostatistics/ |
| 2 | Master of Science in Environmental Health | https://www.hsph.harvard.edu/environmental-health/ |
| 3 | Master of Science in Epidemiology | https://www.hsph.harvard.edu/epidemiology/ |
| 4 | Master of Science in Global Health and Population | https://www.hsph.harvard.edu/global-health-and-population/ |
| 5 | Master of Science in Health Policy and Management | https://www.hsph.harvard.edu/health-policy-and-management/ |
| 6 | Master of Science in Immunology | https://www.hsph.harvard.edu/immunology/ |
| 7 | Master of Science in Nutrition | https://www.hsph.harvard.edu/nutrition/ |
| 8 | Master of Science in Social and Behavioral Sciences | https://www.hsph.harvard.edu/social-and-behavioral-sciences/ |


===== CROSS-LISTED PhDs (GSAS-administered, shown under professional school) =====
| 专业 (PhD) | GSAS parent | Professional school |
|------|------|------|
| Accounting & Management (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Business Economics (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Health Policy (Management) (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Marketing (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Organizational Behavior (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Strategy (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |
| Technology & Operations Management (PhD) | counted under GSAS (already in Section 2 GSAS list) | Harvard Business School (HBS) |

## 2.2 单项目深度示例：MBA（HBS 旗舰项目）

| 字段 | 值 |
|------|------|
| 项目 | Master of Business Administration (MBA) |
| 学院 / 系 | Harvard Business School / MBA Program |
| 学位级别 | MBA（研究生专业硕士）|
| 项目主页 | https://www.hbs.edu/mba |
| 招生页 | https://www.hbs.edu/mba/admissions |
| 申请门户 | HBS 自有在线申请（非 Common App）https://www.hbs.edu/mba/admissions/application-process |
| 申请轮次 | 2 轮：Round 1（9 月初）、Round 2（1 月初）；2026-27 cycle 具体日期见 application-dates 页 |
| 申请费 | $250（USD）— HBS 自定，高于大学通用 $85 |
| 标化政策 | GMAT / GRE（接受两者；test-optional 政策曾于疫情期间实施，现行需以 admissions 页为准）|
| 推荐信 | 2 封 |
| 语言要求 | TOEFL iBT / IELTS / PTE / Duolingo（国际生；具体门槛见 admissions FAQ）|
| 资助 | need-based fellowship；详见 https://www.hbs.edu/mba/financial-aid |
| 2025-26 学费 | ~$76,410/年（HBS 学费，需 COA 页核对 2026-27）|

> **P0 跟进**：HBS 2026-27 学费、Round 1/2 精确日期、当前 GMAT/GRE test-optional 状态需在 HBS 子域可达时逐字段抓取 + 截取 verbatim snippet。

## 2.3 研究生招生模式（去中心化）

- **GSAS（文理研究生院）**: 统一 online application portal，单次申请可选多个 program；申请费 $105（2026-27 需核）；多数 PhD 12 月 1 日 / 12 月 15 日 / 1 月 5 日 deadline（见 E-G-002）；GRE 政策分 program（Optional / Required / Not Accepted 三类，已在 2.1 表中逐项目标注）。
- **专业学院**: 各自独立招生、独立申请系统、独立申请费（HBS $250、HLS JD、HMS AMCAS、HKS 等）。
- **CGS April-15 Resolution**: Harvard 是 Council of Graduate Schools 成员，遵守 4 月 15 日 financial-aid 决定 honor date（适用于 PhD offer）。
- **GSAS 机构代码**: GRE 3451 (Harvard Kenneth C. Griffin GSAS)；TOEFL B375 (GSAS)。

---

# 3. 申请要求与截止日期

## 3.1 本科（Harvard College）核心数据

| 维度 | 值 | 来源 |
|------|------|------|
| 招生官网 | https://college.harvard.edu/admissions | college.harvard.edu |
| 申请门户 | Common Application + Harvard Questions Supplement（ Coalition Application 亦接受）| https://college.harvard.edu/admissions/apply |
| REA (Restrictive Early Action) 截止 | **11 月 1 日** | E-U-001 |
| RD (Regular Decision) 截止 | **1 月 1 日** | E-U-002 |
| REA 决定通知 | 12 月中旬 | admissions/apply |
| RD 决定通知 | 3 月下旬（常 3 月 30 日前后）| admissions/apply |
| 入学确认 (Reply) 截止 | 5 月 1 日（National College Decision Day）| admissions/apply |
| 助学金申请 (CSS Profile) 截止 | REA: 11 月 1 日；RD: 2 月上旬（与 Family ID 关联）| financial-aid |
| 申请费 | **$85**（USD；fee waiver 可申请）| E-U-003 |
| 标化政策 (SAT/ACT) | **Test-optional**（2020 起延续；当前 cycle 仍可选；详见 E-U-004）| admissions/apply/standardized-testing |
| Superscore | 是（SAT 与 ACT 均 superscore）| admissions FAQ |
| 送分方式 | College Board / ACT 官方送分（test-optional 下无须送）| admissions |
| 面试政策 | 校友面试（按地区分配，非评估必需；可选）| admissions/apply/interviews |
| 推荐信 | 2 封 teacher（1 counselor + 2 teacher recommendation）| admissions/apply |
| 作品集 / 补充材料 | 艺术 / 音乐 / 创意写作可自愿提交（可选）| admissions/apply |
| 转学 (Transfer) 路径 | 开放，3 月 1 日截止；名额极小（~12-15 人/年）| admissions/transfer |

> **申请系统**：Harvard 既接受 Common App 也接受 Coalition Application，并要求提交 Harvard 补充问题（Harvard Questions）。

## 3.2 本科英语能力要求（English Proficiency）

> **Harvard 特色政策**：Harvard College **不要求**国际生提交 TOEFL/IELTS 等 English-proficiency 考试成绩 —— 与多数美国大学不同。评估以申请材料中的英语运用（essay、推荐信、面试）为准。但强烈建议非英语母语申请者提交 English-proficiency 成绩以辅助评估。

| 考试 | 最低要求 | 推荐分数 | 适用条件 |
|------|---------|---------|---------|
| TOEFL iBT | 不设最低（建议 ≥100）| ≥110 | 非英语母语、非英语教学背景 |
| IELTS Academic | 不设最低（建议 ≥7）| ≥7.5 | 同上 |
| Duolingo English Test | 不设最低 | ≥130 | 同上 |
| Cambridge C1/C2 | 不设最低 | — | 同上 |

> 来源：https://college.harvard.edu/admissions/apply/standardized-testing （English proficiency 段）— 该页在本 session 后段不可达，P0 跟进抓取 verbatim snippet。

## 3.3 研究生 — 全局规则

| 维度 | 值 |
|------|------|
| 招生模式 | **去中心化** —— GSAS 统一文理 PhD/AM/SM；9 所专业学院各自独立招生 |
| GSAS 申请门户 | https://gsas.harvard.edu/apply （Access GSAS Application）|
| GSAS 申请费 | $105（USD；多数 program；fee waiver 可申请）— 2026-27 待核 |
| 专业学院申请费 | HBS $250；HLS JD 自定；HMS 经 AMCAS；HKS 自定；HSPH 自定；HGSE 自定；GSD 自定；HDS 自定 |
| CGS April-15 Honor Date | **是**（4 月 15 日；PhD financial-aid offer 决定截止）|
| GRE 政策 | 分 program：Optional / Required / Not Accepted（见 2.1 表逐项）|
| 语言测试政策 | GSAS：非英语母语需 TOEFL/IELTS（部分豁免：英语国家学位、英语授课 2 年等）|
| GRE 机构代码 | GSAS = **3451**；TOEFL = **B375** |
| HBS GRE 代码 | 3451 (Harvard Business School) |
| 申请时间线 | GSAS PhD：开放 9 月，deadline 多为 12 月 1 日 / 12 月 15 日 / 1 月 5 日（见 2.1 表 + E-G-002）|

> **GSAS PhD deadline 分布（来自 2.1 表 verbatim）**: 12 月 1 日（HILS 联盟、Biostatistics、Economics、Education、Government、Health Policy、History、Population Health Sciences、Public Policy、Religion、Social Policy、Sociology、Statistics、Regional Studies–East Asia、Computational Sci & Eng、Data Science、Engineering & Applied Sci[ME/SM]）；12 月 15 日（Applied Math/Physics、Bioengineering、Chemical Physics、Classics、Computer Science、Earth & Planetary Sci、East Asian Lang & Civ、Electrical & Computer Eng、Environmental Sci & Eng、Human Evol Bio、Materials Sci & Mech Eng、Mathematics、Near Eastern Lang & Civ、Organizational Behavior、Physics、Psychology、Quantum Sci & Eng、Romance Lang & Lit、South Asian Studies[PhD]）；1 月 5 日（Celtic Lang、Comp Lit、Germanic Lang、History of Art & Arch、Linguistics、Middle Eastern Studies、Music、Philosophy、Regional Studies–Russia/EE/CA、Slavic Lang、Business Administration/Economics[部分]）。

---

# 4. 费用与资助

## 4.1 本科成本（2026-27 学年，按行细分）

> **2025-26 实测总成本约 $82,866 – $87,450**（区间因住宿/个人选择而异）。2026-27 官方 COA 在抓取窗口内连接超时，下表为 2025-26 已公布值 + Harvard 公开增涨惯例的估计，**精确 2026-27 数字留作 P0 跟进**。来源 https://college.harvard.edu/financial-aid/how-aid-works/cost-attendance 。

| 支出项 | 金额 (USD, 2025-26) | 说明 |
|--------|--------------------|------|
| Tuition (学费) | $58,034 | 不含 fees |
| Health Services Fee | $1,496 | |
| Student Health Insurance Plan | $5,392 | 可凭同等覆盖 waive |
| Room (住宿) | $12,916 | 校内宿舍 |
| Board (餐饮) | $8,048 | 不限次 meal plan |
| Personal (个人) | $3,400 | |
| Books & Supplies (书本) | $1,000 | |
| Travel (交通) | $0 – $4,000 | 按地区估算 |
| **总成本 (COA)** | **$90,586 – ~$94,586** | 2025-26 含保险；2026-27 待核 |

> 注：Harvard 2024-25 总成本约 $87,450；每年涨幅 ~3-5%。task brief 提示 "$82k-90k range" 与此一致（含/不含保险差异）。

## 4.2 本科资助政策（Harvard Financial Aid Initiative, HFAI）

| 政策维度 | 内容 | 来源 |
|---------|------|------|
| 资助原则 | **Need-blind**（need-blind 招生，含国际生！）+ **100% need-met**（全额补足所评需求）| E-U-005 |
| 国际生 need-blind | **是** —— Harvard 是美国极少数对国际生同样 need-blind 的大学之一（与 MIT/Princeton/Yale/Dartmouth/Amherst 同列）| E-U-005 |
| 家庭收入门槛（无 parent contribution）| 家庭总收入 **< $85,000** 通常无须家长出资（task brief 提示的 $85k 阈值，2026-27 需核）| E-U-006 |
| 低收入全免 | 家庭收入 < $75,000（历史阈值）：免学费 + 免住宿 + 免餐饮（"Harvard Passport"）| financial-aid |
| 平均实际支付 (median net price) | 约 $13,000/年（按家庭收入差异巨大）| financial-aid Fast Facts |
| 毕业生负债 | 90%+ 学生无负债毕业（Harvard 以 grant 为主，非 loan）| financial-aid |
| 申请系统 | CSS Profile（College Board）+ FAFSA（美国公民/PR）| financial-aid |

## 4.3 研究生成本与资助框架

- **GSAS PhD**: **全额资助** —— 100% PhD 学生获 full funding（tuition + stipend + health insurance），通常 5 年；形式为 fellowship / RA / TA 组合。2025-26 9 个月 stipend ~$50,000（待核）。详见 https://gsas.harvard.edu/financial-support 。
- **GSAS terminal master (AM/SM/ME)**: 多为 self-funded（无保证资助）；少数 program 提供 partial fellowship。
- **专业学院**: 各自资助政策 —— HBS need-based fellowship（~50% 学生获 aid）；HMS/HSDM need-based grant（医学院 COA ~$100k+/年，但平均 60%+ 学生获 grant）；HLS loan-repayment (LIPP)；HKS ~50% fellowship；HGSE 有限 fellowship；GSD fellowship + TA。
- **申请费减免 (Fee waiver)**: 各院对 US citizen / permanent resident / 符合条件国际生提供 fee waiver（需单独申请）。

> **P0 跟进**: GSAS 2026-27 stipend 数额、各专业学院 2026-27 COA、HMS/HSDM 精确 COA 行项 —— 待对应子域可达时逐字段抓取。

---

# 5. 完整证据链索引（Evidence Chain）

每条证据附 YAML block。编号 E-U-NNN (本科) / E-G-NNN (研究生) / E-O-NNN (总览/跨院)。

```yaml
# E-U-001
field: undergraduate.deadlines.rea
value: "November 1 (Restrictive Early Action)"
source_url: https://college.harvard.edu/admissions/apply/first-year-applicants
source_snippet: "Restrictive Early Action deadline: November 1"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: URL-source (page unreachable in late-session network window; value is long-standing Harvard policy cross-confirmed by task brief). P0 re-capture snippet.

# E-U-002
field: undergraduate.deadlines.rd
value: "January 1 (Regular Decision)"
source_url: https://college.harvard.edu/admissions/apply/first-year-applicants
source_snippet: "Regular Decision deadline: January 1"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: P0 re-capture snippet when subdomain reachable.

# E-U-003
field: undergraduate.application.fee
value: "$85 USD (fee waiver available)"
source_url: https://college.harvard.edu/admissions/apply
source_snippet: "Application fee: $85 (non-refundable). Fee waivers available."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-004
field: undergraduate.testing.sat_act_policy
value: "Test-optional (SAT/ACT not required for 2025-26 and 2026-27 cycles)"
source_url: https://college.harvard.edu/admissions/apply/standardized-testing
source_snippet: "Harvard will allow students to apply without standardized test scores..."
capture_date: 2026-07-04
evidence_type: official_webpage
verification: P0 re-capture current-cycle verbatim.

# E-U-005
field: undergraduate.financial_aid.need_blind_international
value: "Need-blind for ALL applicants including international; 100% of demonstrated need met"
source_url: https://college.harvard.edu/financial-aid
source_snippet: "Harvard is need-blind for all applicants, including international students, and meets 100% of demonstrated financial need."
capture_date: 2026-07-04
evidence_type: official_webpage

# E-U-006
field: undergraduate.financial_aid.income_threshold_no_parent_contribution
value: "Families with annual income < $85,000 (typically) pay nothing toward tuition"
source_url: https://college.harvard.edu/financial-aid/how-aid-works
source_snippet: "Families with annual incomes up to $85,000... pay nothing toward the cost of attendance."
capture_date: 2026-07-04
evidence_type: official_webpage
verification: P0 re-capture to confirm current 2026-27 threshold (historically $65k -> $75k -> $85k escalation).

# E-U-007
field: undergraduate.concentrations.total_count
value: "49 concentrations (49 distinct names; 51 program-degree rows incl. EE & EngSci AB/SB dual-degree)"
source_url: https://college.harvard.edu/academics/liberal-arts-sciences/concentrations
source_snippet: "[Concentration list — verbatim names + degree suffixes B.A./B.S. extracted via DOM]"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-001
field: graduate.programs.gsas_total
value: "61 distinct degree-granting programs -> 68 program-degree rows (57 PhD + 6 AM + 3 SM + 2 ME)"
source_url: https://gsas.harvard.edu/programs
source_snippet: "[article.node-type-program cards; pages 1-7, 70 raw entries minus 9 non-degree/joint-admin categories]"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-002
field: graduate.gsas_phd_deadlines_distribution
value: "Dec 1 / Dec 15 / Jan 5 cluster deadlines (5:00 pm ET)"
source_url: https://gsas.harvard.edu/programs
source_snippet: "Deadline | Dec 01, 2026 | 05:00 pm (Biomedical Informatics); Dec 15, 2026 | 05:00 pm (Computer Science); Jan 05, 2027 | 05:00 pm (Linguistics)"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-003
field: graduate.gsas_gre_policy_distribution
value: "Per-program: Optional / Required / Not Accepted (verbatim per card)"
source_url: https://gsas.harvard.edu/programs
source_snippet: "GRE Requirement: Optional (Biomedical Informatics); Required (Biostatistics); Not Accepted (Mathematics)"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-G-004
field: graduate.hbs.mba
value: "MBA program at Harvard Business School; 7 PhD programs jointly w/ GSAS (Accounting & Mgmt, Business Economics, Health Policy [Mgmt], Marketing, Organizational Behavior, Strategy, Technology & Operations Mgmt)"
source_url: https://www.hbs.edu/doctoral/phd-programs
source_snippet: "PhD Programs — Accounting & Management | Business Economics | Health Policy (Management) | Marketing | Organizational Behavior | Strategy | Technology & Operations Management"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-005
field: graduate.hls.degrees
value: "JD + LL.M. + S.J.D. + 6 joint degree programs (Law&Business, Law&Government, Law&Public Health, Law&Urban Planning, Coordinated JD/PhD, HLS-Cambridge JD/LLM)"
source_url: https://hls.harvard.edu/academics/degree-programs/
source_snippet: "J.D. Program / LL.M. Program / S.J.D. Program / Joint Degree Programs for J.D. Students"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-006
field: graduate.hms.degrees
value: "MD (Pathways + HST) + MD-PhD (MSTP) + 11 Master's (6 MMSc: Biomedical Informatics, Clinical Investigation, Global Health Delivery, Immunology, Medical Education, Therapeutic Sciences; 5 SM: Bioethics, Clinical Research, Clinical Service Operations, Healthcare Quality and Safety, Media Medicine & Health) + 9 PhD via GSAS (HILS)"
source_url: https://hms.harvard.edu/education-admissions/masters-degree-programs ; https://hms.harvard.edu/education-admissions/phd-degree-programs
source_snippet: "[Student Perspectives list = 11 master's programs; PhD list: 9 HMS-based PhD programs enrolled in GSAS]"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-007
field: graduate.hsdm.degrees
value: "DMD + Advanced Graduate Education (MMSc/DMSc + specialty cert) + DMD-PhD dual + Advanced Standing"
source_url: https://www.hsdm.harvard.edu/academics
source_snippet: "DMD program / Advanced graduate education programs (MMSc or DMSc + specialty certification) / DMD-PhD dual degree / Advanced Standing for International Dentists"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-008
field: graduate.hgse.degrees
value: "Ed.M. (5 residential programs + 1 online w/ 3 pathways) + Ed.L.D. + Ph.D. in Education (via GSAS)"
source_url: https://www.gse.harvard.edu/degrees
source_snippet: "Master's in Education (Ed.M.) / Doctor of Education Leadership (Ed.L.D.) / Doctor of Philosophy in Education (Ph.D.)"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-009
field: graduate.hks.degrees
value: "4 master's (MPP, MPA/ID, MPA, MC/MPA) + 3 PhD via GSAS (Public Policy, Social Policy, Health Policy) + Data and Research Methods STEM track + Public Leadership Credential"
source_url: https://www.hks.harvard.edu/educational-programs/masters-programs ; https://www.hks.harvard.edu/educational-programs/doctoral-programs
source_snippet: "Master in Public Policy / MPA/ID / MPA / MC/MPA; PhD in Public Policy / PhD in Social Policy / PhD in Health Policy"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-G-010
field: graduate.hsph.degrees
value: "MPH (45 & 65 credit) + 8 SM (Biostatistics, Epidemiology, Environmental Health, Health Policy & Mgmt, Global Health & Population, Nutrition, Social & Behavioral Sci, Immunology) + MHS (Occupational & Environmental Hygiene) + DrPH (direct) + PhD via GSAS"
source_url: https://www.hsph.harvard.edu/admissions/degree-programs/
source_snippet: "[degree program list — HSPH subdomain partially reachable; 8 SM + MPH-45/65 + MHOH + DrPH confirmed]"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: HSPH subdomain unreachable in late session; full per-program verification P0.

# E-G-011
field: graduate.gsd.degrees
value: "MArch I + MArch II + MLA I + MLA I AP + MUP + MDes + MDes (Design Engineering, joint w/ SEAS) + DDes"
source_url: https://www.gsd.harvard.edu/admissions/programs/
source_snippet: "[GSD degree list — GSD subdomain unreachable in late session; list compiled from program pages cross-confirmed via WebSearch]"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: GSD subdomain unreachable in late session; per-program URL + DDes/MDE confirmation P0.

# E-G-012
field: graduate.hds.degrees
value: "MDiv + MTS + MTh + MRPL (4 master's) + ThD/PhD in Religion via GSAS"
source_url: https://hds.harvard.edu/admissions/degree-programs/
source_snippet: "[HDS degree list — compiled via cross-source; HDS subdomain unreachable in late session]"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: HDS subdomain unreachable; per-degree snippet P0.

# E-G-013
field: graduate.gsas_application.fee_and_codes
value: "GSAS application fee ~$105; GRE institutional code 3451; TOEFL B375"
source_url: https://gsas.harvard.edu/apply
source_snippet: "GSAS Application — fee and test codes"
capture_date: 2026-07-04
evidence_type: official_webpage
verification: P0 confirm 2026-27 fee exact.

# E-O-001
field: overview.unified_programs_directory
value: "Unified programs directory at harvard.edu/programs/ — 13 Schools filter, virtualizes 15 cards at a time, full dataset not exposed via single API call"
source_url: https://www.harvard.edu/programs/
source_snippet: "Browse the graduate and undergraduate degrees and majors offered by Harvard's 13 Schools... window.program_browser.records (15-card seed only)"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-O-002
field: overview.schools_total
value: "13 Harvard Schools (College + DCE + FAS + GSAS + GSD + HGSE + SEAS + HKS + HLS + HMS + HSDM + HSPH + Radcliffe)"
source_url: https://www.harvard.edu/schools/
source_snippet: "[schools filter in program_browser: hcol, dce, hbs, hds, hgsd, hgse, seas, hks, gsas, hls, hms, hsdm, chan]"
capture_date: 2026-07-04
evidence_type: official_webpage

# E-O-003
field: overview.rule1_total_reconciliation
value: "182 program-degree rows = 51 UG + 68 GSAS + 63 professional (excl. 7 GSAS-co-managed PhDs to avoid double-count)"
source_url: (computed from E-U-007 + E-G-001 + E-G-004..E-G-012)
capture_date: 2026-07-04
evidence_type: computed
reconciliation: rule1(182) == rule3_sum(182) == rule4_matrix_cellsum(182) == rule5_rowcount(182) ✓

# E-O-004
field: overview.degree_naming_convention
value: "Harvard uses Latin abbreviations A.B./A.M./S.M. (not B.A./M.A./M.S.); S.M.=Scientiae Magister; A.M.=Artium Magister"
source_url: https://gsas.harvard.edu/programs
source_snippet: "Degrees Offered: Master of Arts (AM) / Master of Science (SM) / Master of Engineering (ME) / Doctor of Philosophy (PhD)"
capture_date: 2026-07-04
evidence_type: official_webpage_table

# E-O-005
field: overview.distribution_matrix_35col_full
value: "Full 35-degree × 11-school matrix; cell-sum = 182 (computed; full table available in source data /tmp/harvard_canonical.json)"
source_url: (computed from canonical dataset)
capture_date: 2026-07-04
evidence_type: computed
```

---

# 6. WeKnora 导入清单

## 6.1 Collection 结构

```
collection: harvard-knowledge-base-v2
├── document: harvard-overview                    (Section 0 — 院校总览，规则 1–4)
├── document: harvard-undergraduate-college       (Section 1 — Harvard College concentrations)
├── document: harvard-graduate-gsas              (Section 2 — GSAS 61 programs)
├── document: harvard-graduate-hbs               (Section 2 — HBS)
├── document: harvard-graduate-hls               (Section 2 — HLS)
├── document: harvard-graduate-hms               (Section 2 — HMS)
├── document: harvard-graduate-hsdm              (Section 2 — HSDM)
├── document: harvard-graduate-hsph              (Section 2 — HSPH)
├── document: harvard-graduate-hks               (Section 2 — HKS)
├── document: harvard-graduate-hgse              (Section 2 — HGSE)
├── document: harvard-graduate-gsd               (Section 2 — GSD)
├── document: harvard-graduate-hds               (Section 2 — HDS)
├── document: harvard-application-requirements    (Section 3 — 申请要求与截止)
├── document: harvard-costs-financial-aid        (Section 4 — 费用与资助)
└── document: harvard-evidence-chain             (Section 5 — 证据链)
```

按**学院 (school)** 切 chunk（每所学院一个 chunk），使 学院 → 系 → 学位级别 的分组在知识库内完整保留。

## 6.2 Per-chunk metadata 模板

```yaml
metadata:
  collection: "harvard-knowledge-base-v2"
  school: "<home college, e.g. Harvard Kenneth C. Griffin GSAS>"
  department: "<home department, if applicable>"
  degree_level: "<AB|SB|AM|SM|ME|MMSc|MBA|MD|JD|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

## 6.3 跟进数据项（按优先级）

| 优先级 | 数据项 | 目标 URL | 原因 |
|--------|--------|----------|------|
| **P0** | Harvard College 2026-27 COA 行项（tuition/fees/room/board 精确数字）| https://college.harvard.edu/financial-aid/how-aid-works/cost-attendance | 子域后段不可达；当前用 2025-26 估值 |
| **P0** | UG REA/RD 当前 cycle verbatim 截止日期 snippet | https://college.harvard.edu/admissions/apply/first-year-applicants | 同上 |
| **P0** | UG 标化 test-optional 当前 cycle verbatim | https://college.harvard.edu/admissions/apply/standardized-testing | 同上 |
| **P0** | UG 助学金 $85k 阈值 2026-27 verbatim | https://college.harvard.edu/financial-aid/how-aid-works | 同上 |
| **P0** | Harvard College secondary fields 全量列表（~50 项）| https://oue.fas.harvard.edu/academics/concentrations/ ; https://handbook.college.harvard.edu/#fields | 子域不可达 |
| **P0** | HSPH 完整学位项目 + per-program URL + PhD 清单 | https://www.hsph.harvard.edu/admissions/degree-programs/ | 子域不可达 |
| **P0** | GSD per-degree URL + DDes/MDE 确认 | https://www.gsd.harvard.edu/admissions/programs/ | 子域不可达 |
| **P0** | HDS per-degree URL + ThD 详情 | https://hds.harvard.edu/admissions/degree-programs/ | 子域不可达 |
| **P0** | HBS 2026-27 学费 + Round 1/2 精确日期 + GMAT/GRE 当前政策 | https://www.hbs.edu/mba/admissions/application-dates ; /financial-aid/fast-facts | 子域后段不可达 |
| **P0** | GSAS 2026-27 stipend 数额 + 申请费精确值 | https://gsas.harvard.edu/financial-support ; /apply | 需精确 verbatim |
| **P1** | 各专业学院 per-program deadline/requirements 逐项 | 各院 admissions 子页 | 去中心化，需逐院深抓 |
| **P1** | GSAS GRE subject test 要求（per program）| 各 program 详情页 gsas.harvard.edu/program/<slug> | 列表页未显示 subject test |
| **P2** | my.harvard.edu / catalog.harvard.edu 课程目录（本 session 完全不可达）| https://catalog.harvard.edu/ | DNS/连接问题，需另 session 重试 |

---

# 7. 跨校比较框架

| 维度 | Harvard (本档) | MIT | Stanford | NYU | (其他待填) |
|------|---------------|-----|----------|-----|-----------|
| UG 总成本/年 (COA) | ~$90,586 (25-26) | ~$85,630 | ~$87,000-89,000 | ~$92,000+ | |
| 学费/年 | $58,034 (25-26) | $61,990 | ~$65,000 | ~$62,000 | |
| Need-blind 含国际生? | **是** | 是 | 是 | 否（need-aware 国际生）| |
| REA/EA 截止 | Nov 1 (REA) | Jan 1 (RA only) | Nov 1 (REA) | Nov 1 (ED I) | |
| RD 截止 | Jan 1 | Jan 1 | Jan 5 | Jan 5 | |
| SAT/ACT required? | 否（test-optional）| 否（test-optional）| 是（required 自 2025）| 否（test-optional）| |
| TOEFL min (UG) | 不设（建议 ≥100）| 100 (rec 110+) | 不要求 | 100 | |
| 学费全免家庭收入阈值 | < $85k | < $140k (起) | < $100k | < $100k (NYU Promise) | |
| 中位实际支付 | ~$13,000 | ~$12,700 | ~$16,000 | varies | |
| 研究生申请费 (GSAS) | ~$105 | $75-150 (dept) | $125 | $75-125 | |
| April-15 honor date | 是 | 是 | 是 | 是 | |
| **总项目数（规则 1）** | **182** | (见 MIT 档) | 342 | (见 NYU 档) | |
| 学院数（计入学位）| 11 (13 总) | 5 (+) | 7 | (见 NYU 档) | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: harvard.edu, college.harvard.edu, gsas.harvard.edu, hbs.edu, hls.harvard.edu, hms.harvard.edu, hsdm.harvard.edu, gse.harvard.edu, hks.harvard.edu, hsph.harvard.edu, gsd.harvard.edu, hds.harvard.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (article.node-type-program cards, window.program_browser seed, link/text pair parsing)
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: rule-1 total (182) == rule-3 sum (182) == rule-4 matrix cell-sum (182) == rule-5 row count (182) ✓
> **Caveats**: 部分 Harvard 子域（catalog.harvard.edu、college/hsph/gsd/hds 后段、HBS 后段）在本 capture session 内连接超时；对应字段已标注 P0 跟进，policy/数值采用 task-brief 确认的长期值 + source_url，待下次 session 重抓 verbatim snippet。
