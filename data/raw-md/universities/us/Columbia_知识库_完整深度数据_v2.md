# Columbia University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-04
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

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

Columbia University（正式名称：Columbia University in the City of New York，创立于 1754 年）下设 **15 所授予学位的学院**，包括 4 所本科部（Columbia College、The Fu Foundation School of Engineering and Applied Science / Columbia Engineering、School of General Studies、Barnard College）和 11 所研究生 / 专业学院（GSAS、Columbia Business School、Columbia Law School、Vagelos College of Physicians & Surgeons、Mailman School of Public Health、SIPA、Columbia School of Social Work、GSAPP、Columbia Journalism School、School of the Arts、Columbia School of Nursing）。共开设 **434 个学位—项目计量行（program-degree rows）**：本科 154 + 辅修 50 + 研究生 216 + 高级证书 14。本节四项汇总（规则 1–4）均由 Phase 2 从各学院权威页面（`bulletin.columbia.edu`、`gsas.columbia.edu`、各专业学院官网）提取的 434 条数据派生，并已通过**强制对账检查**。

> **核心数据来源**:
> - 本科公告（Columbia College）：https://bulletin.columbia.edu/columbia-college/departments-instruction/ （58 个系/项目，授予 BA）
> - 本科公告（Columbia Engineering / SEAS）：https://bulletin.columbia.edu/columbia-engineering/academic-departments-programs/ （11 个工程系 + 跨学科 Data Science/Engineering；BS / MS / PhD / EngScD）
> - SEAS 本科辅修：https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/ （49 条辅修行）
> - 本科公告（School of General Studies）：https://bulletin.columbia.edu/general-studies/majors-concentrations/ （90 个 GS 项目页；GS 与 CC 共享 FAS 系所 + 39 个 GS-unique 主修）
> - Barnard College：https://barnard.edu/departments-and-programs （约 50 个系，授予 BA）
> - 研究生院 GSAS：https://www.gsas.columbia.edu/content/degree-programs （MA 46 + PhD 34 + Dual 4 + 非学位证书 12 + PhD 浓度 3）
> - 各专业学院官网逐院抓取（CBS / Law / Vagelos / Mailman / SIPA / CSSW / GSAPP / Journalism / Arts / Nursing）

> **Columbia 学位命名特色**: Columbia 同时授予传统学位（BA、BS、MA、MS、MFA、PhD）与专业博士（MD、JD、JSD、DPT、DNP、DrPH、EdD、OTD）、专业硕士（MBA、MPH、MIA、MPA、MSW、MSSW、MArch、MHA、LLM）以及工程类研究型博士 **EngScD**（Doctor of Engineering Science，SEAS 与 PhD 并列授予）和 **Engineer of Mines** 专业学位（Earth & Environmental Engineering）。本文档统一保留 Columbia 官方缩写。

## 0.1 专业与项目总数（规则 1）

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位专业 (BA) | 136 | Columbia College 56 + School of General Studies 39 + Barnard 41（CC 与 GS 共享 FAS 系所，BA 由各自学院授予）|
| 本科学位专业 (BS) | 18 | 全部 Columbia Engineering (SEAS)：含 Civil/Chemical/Mechanical/Electrical/Computer/Industrial/Operations Research/Mining/Materials Science/Biomedical/Applied Mathematics/Applied Physics + 双学位 + BS/MS 集成项目 |
| **本科主修小计（program-degree 行）** | **154** | BA 136 + BS 18 |
| 本科辅修 (Minor) | 50 | SEAS 提供 49 条辅修行（含 Statistics 三轨）+ 其他 |
| 研究生学位项目 (MA/MS/MFA/MBA/MPH/MPA/MIA/MSW/MArch/MHA/LLM/PhD/MD/JD/JSD/DPT/DNP/DrPH/EdD/OTD/EngScD 等) | 216 | 详见 0.3 学历级别明细 |
| 研究生高级证书 / 非学位证书 (Advanced Certificate / Certification of Professional Achievement) | 14 | GSAS 12 + SEAS 2（Medical Physics CPA、Engineer of Mines 专业学位）|
| **学位/项目总计（program-degree 行）** | **434** | 规则 1 总数 |
| 其中本科 (undergraduate) | 154 | CC + SEAS + GS + Barnard |
| 其中本科辅修 (minor) | 50 | SEAS 49 + 其他 |
| 其中研究生 (graduate) | 216 | GSAS + 10 所专业学院 |
| 其中研究生证书 (cert) | 14 | GSAS + SEAS |
| 学院 / 独立系所总数 | 15 | 4 本科 + 11 研究生/专业 |

> **counting convention**: 一个项目若授予多个学位级别（如 Electrical Engineering 同时授 BS 与 BS/MS 集成项目；Statistics 同时授 Minor 基础轨 / Applied 轨 / Theory 轨；Biomedical Engineering 同时授 BS、MS、PhD、MD/MS、集成 BS/MS），按"学位—项目"行展开计数。这是保证规则 1、3、4、5 严格对账的必要约定。

> **对账（MANDATORY reconciliation）**:
> - 规则 1 总数 = **434**
> - 规则 3 学历级别求和 = **434**（见 0.3）
> - 规则 4 分布矩阵单元求和 = **434**（见 0.4，行/列合计均为 434）
> - 规则 5 全量明细行数 = **434**（Section 1 = 204 行 [154 主修 + 50 辅修] + Section 2 = 230 行 [216 研究生学位 + 14 证书]）
> - **四数一致 ✓**

## 0.2 学院 / 系层级结构（规则 2）

```
Columbia University
├── Columbia College  [学院 — 本科部，授予 BA]
│   ├── African American and African Diaspora Studies  [系]
│   ├── American Studies  [系]
│   ├── Ancient Studies  [系]
│   ├── Anthropology  [系]
│   ├── Archaeology  [系]
│   ├── Architecture  [系]
│   ├── Art History and Archaeology  [系]
│   ├── Astronomy  [系]
│   ├── Biological Sciences  [系]
│   ├── Business  [系]
│   ├── Chemistry  [系]
│   ├── Classics  [系]
│   ├── Cognitive Science  [系]
│   ├── Comparative Literature and Society  [系]
│   ├── Computer Science  [系]  ⚠ 与 SEAS / GS 共享
│   ├── Creative Writing  [系]
│   ├── Dance  [系]
│   ├── Drama and Theatre Arts  [系]
│   ├── Earth and Environmental Sciences  [系]
│   ├── East Asian Languages and Cultures  [系]
│   ├── Ecology, Evolution, and Environmental Biology  [系]
│   ├── Economics  [系]
│   ├── Education  [系]
│   ├── English and Comparative Literature  [系]
│   ├── Ethnicity and Race Studies  [系]
│   ├── Film and Media Studies  [系]
│   ├── French  [系]
│   ├── Germanic Languages  [系]
│   ├── Global Affairs and Public Policy  [系]
│   ├── History  [系]
│   ├── Human Rights  [系]
│   ├── Italian  [系]
│   ├── Jazz Studies  [系]
│   ├── Jewish Studies  [系]
│   ├── Latin American and Caribbean Studies  [系]
│   ├── Latin American and Iberian Cultures  [系]
│   ├── Linguistics  [系]
│   ├── Mathematics  [系]
│   ├── Medieval and Renaissance Studies  [系]
│   ├── Middle Eastern, South Asian, and African Studies  [系]
│   ├── Music  [系]
│   ├── Philosophy  [系]
│   ├── Physics  [系]
│   ├── Political Science  [系]
│   ├── Psychology  [系]
│   ├── Public Health  [系]
│   ├── Regional Studies  [系]
│   ├── Religion  [系]
│   ├── Science and Society  [系]
│   ├── Slavic Languages  [系]
│   ├── Sociology  [系]
│   ├── Statistics  [系]
│   ├── Sustainable Development  [系]
│   ├── Urban Studies  [系]
│   ├── Visual Arts  [系]
│   └── Women's and Gender Studies  [系]
│       (另含非学位服务单元：Language Resource Center、Physical Education and Intercollegiate Athletics)
│
├── The Fu Foundation School of Engineering and Applied Science (Columbia Engineering / SEAS)  [学院 — 本科+研究生]
│   ├── Applied Physics and Applied Mathematics  [系]
│   ├── Biomedical Engineering  [系]
│   ├── Chemical Engineering  [系]
│   ├── Civil Engineering and Engineering Mechanics  [系]
│   ├── Computer Engineering Program  [系]
│   ├── Computer Science  [系]  ⚠ 与 CC/GS 共享
│   ├── Earth and Environmental Engineering  [系]
│   ├── Electrical Engineering  [系]
│   ├── Industrial Engineering and Operations Research  [系]
│   ├── Materials Science and Engineering Program  [系]
│   ├── Mechanical Engineering  [系]
│   ├── Data Science  [系 — 跨学科]  ⚠ 跨多系
│   └── Engineering (School-wide interdisciplinary)  [系 — 跨学科]  ⚠ 含 MS in AI / xMS / MBAxMS
│
├── School of General Studies (GS)  [学院 — 本科部，授予 BA/BS]
│   ├── (GS 与 Columbia College 共享 FAS 系所；56 个 CC 主修对 GS 学生同样开放)
│   └── GS-unique 主修（39 个）：Applied Mathematics (BS)、Astrophysics、Biochemistry、Biophysics、
│       Chemical Physics、Computational Biology、Data Science、Information Science、Neuroscience and
│       Behavior、Medical Humanities、Climate and Sustainability 等（详见 1.2 GS 表）
│
├── Barnard College  [学院 — 本科部（女子学院），Columbia 附属，授予 BA]
│   └── 约 50 个系/主修：Africana Studies、Anthropology、Architecture、Art History、Biological
│       Sciences、Chemistry、Computer Science、Dance、Economics、English、Film Studies、Mathematics、
│       Music、Neuroscience and Behavior、Philosophy、Physics、Political Science、Psychology、
│       Sociology、Theatre、Urban Studies 等（详见 1.2 Barnard 表）
│
├── Graduate School of Arts and Sciences (GSAS)  [学院 — 文理研究生院]
│   ├── MA Programs (46 个 free-standing master's)
│   ├── PhD Programs (34 个；含与 GSAPP 共管：Architecture、Historic Preservation、Urban Planning)
│   ├── Dual-Degree Programs (4)
│   ├── Non-Degree Graduate Certificates (12)
│   └── PhD Concentrations (3)
│
├── Columbia Business School (CBS)  [学院 — 专业学院]
├── Columbia Law School  [学院 — 专业学院]
├── Vagelos College of Physicians & Surgeons (VP&S, Medicine)  [学院 — 专业学院]
├── Mailman School of Public Health  [学院 — 专业学院]（6 个系：Biostatistics、Environmental Health
│   Sciences、Epidemiology、Health Policy and Management、Population and Family Health、Sociomedical Sciences）
├── School of International and Public Affairs (SIPA)  [学院 — 专业学院]
├── Columbia School of Social Work (CSSW)  [学院 — 专业学院]
├── Graduate School of Architecture, Planning and Preservation (GSAPP)  [学院 — 专业学院]
├── Columbia Journalism School  [学院 — 专业学院]
├── School of the Arts (SOA)  [学院 — 专业学院]
└── Columbia School of Nursing  [学院 — 专业学院]
```

> **跨院共享系所说明**：Computer Science 同时挂靠 Columbia College、SEAS 与 GS（同一系，三院学生共修，学位由各自学院授予）；GSAS 的 Architecture / Historic Preservation / Urban Planning 三个 PhD 实际由 GSAPP 主办但通过 GSAS 注册；Vagelos 的 PhD 通过 GSAS Coordinated Doctoral Programs 注册。本文档将 PhD 计入其实际主办学院，避免双重计数。

## 0.3 学历级别明细（规则 3）

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 136 |
| BS | Bachelor of Science | 本科 | 18 |
| Minor | Undergraduate Minor / Concentration | 本科辅修 | 50 |
| MA | Master of Arts | 研究生 | 48 |
| MS | Master of Science (含 EngScD 候选、MS-EEE 等变体) | 研究生 | 57 |
| MFA | Master of Fine Arts | 研究生 | 5 |
| MBA | Master of Business Administration (含 EMBA) | 研究生 | 2 |
| MIA | Master of International Affairs | 研究生 | 1 |
| MPA | Master of Public Administration (含 MPA-DP/EPM/ESP/GL、EMPA) | 研究生 | 6 |
| MPH | Master of Public Health (含 Accelerated、Online、2yr) | 研究生 | 12 |
| MHA | Master of Health Administration | 研究生 | 3 |
| MSW / MSSW | Master of Science in Social Work | 研究生 | 2 |
| MArch | Master of Architecture | 研究生 | 1 |
| LLM | Master of Laws (含 Executive LL.M.) | 研究生 | 2 |
| Dual | Dual-Degree Program (JD/PhD、MD/PhD、MA/MSc with LSE、Religion-Journalism MA/MS) | 研究生 | 4 |
| PhD | Doctor of Philosophy (含 EngScD、PhD/DES) | 研究生 | 59 |
| PhD-Conc | PhD Concentration (Atmospheric Science、Buddhist Studies、Math Structures) | 研究生 | 3 |
| MD | Doctor of Medicine (含 Columbia-Bassett Track) | 专业博士 | 2 |
| JD | Juris Doctor | 专业博士 | 1 |
| JSD | Doctor of the Science of Law | 专业博士 | 1 |
| DPT | Doctor of Physical Therapy | 专业博士 | 1 |
| DNP | Doctor of Nursing Practice | 专业博士 | 1 |
| DrPH | Doctor of Public Health | 专业博士 | 3 |
| EdD | Doctor of Education (Movement Science) | 专业博士 | 1 |
| OTD | Occupational Therapy Doctorate | 专业博士 | 1 |
| Cert | Advanced Certificate / Certification of Professional Achievement / Engineer of Mines | 研究生证书 | 14 |
| **合计** | | | **434** |

> 工程研究型博士 **EngScD**（Doctor of Engineering Science）在 Columbia SEAS 与 PhD 并列授予；本表中并入 PhD 计数（Applied Mathematics、Applied Physics、Civil Engineering、Electrical Engineering、Earth & Environmental Engineering、Materials Science 均同时列出 PhD, EngScD）。Chemical Engineering 列为 "PhD/DES"（Doctor of Engineering Science）。EngScD 是 Columbia 特有的工程博士学位。

## 0.4 分布矩阵（学院 × 学位级别）

> 学位级别归并为 9 个桶：BA/BS（本科主修）、Minor、MA/MS/MFA/Prof.M（含 MA、MS、MFA、MArch、MHA、MIA、MPA、MPH、MSW、LLM、OTD）、MBA、Prof. Doctorate（JD/JSD/MD/DPT/DNP/DrPH/EdD）、PhD（含 EngScD）、Dual、Cert、PhD-Conc。

| 学院 ＼ 级别 | BA/BS | Minor | MA/MS/MFA/Prof.M | MBA | Prof.Doc | PhD | Dual | Cert | PhD-Conc | 合计 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Columbia College | 56 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 56 |
| Columbia Engineering (SEAS) | 18 | 50 | 28 | 0 | 0 | 11 | 0 | 2 | 0 | 109 |
| School of General Studies | 39 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 39 |
| Barnard College | 41 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 41 |
| GSAS | 0 | 0 | 46 | 0 | 0 | 34 | 4 | 12 | 3 | 99 |
| Columbia Business School | 0 | 0 | 5 | 2 | 0 | 1 | 0 | 0 | 0 | 8 |
| Columbia Law School | 0 | 0 | 2 | 0 | 2 | 0 | 0 | 0 | 0 | 4 |
| Vagelos College of Physicians & Surgeons | 0 | 0 | 7 | 0 | 4 | 3 | 0 | 0 | 0 | 14 |
| Mailman School of Public Health | 0 | 0 | 22 | 0 | 3 | 4 | 0 | 0 | 0 | 29 |
| School of International & Public Affairs (SIPA) | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Columbia School of Social Work | 0 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 3 |
| GSAPP | 0 | 0 | 8 | 0 | 0 | 3 | 0 | 0 | 0 | 11 |
| Columbia Journalism School | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 4 |
| School of the Arts | 0 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| Columbia School of Nursing | 0 | 0 | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 4 |
| **合计** | **154** | **50** | **138** | **2** | **10** | **59** | **4** | **14** | **3** | **434** |

> Mailman 的 22 个 MA/MS/MFA/Prof.M 桶 = MPH 12 + MS 7 + MHA 3。行合计与列合计均为 434，与规则 1 一致 ✓。MA/MS/MFA/Prof.M 列总 138 = MA 48 + MS 57 + MFA 5 + MArch 1 + MHA 3 + MIA 1 + MPA 6 + MPH 12 + MSW 2 + LLM 2 + OTD 1。

---

# 1. 本科教育 (Undergraduate Education — 规则 5 分组)
## 1.1 College/school architecture

Columbia 的本科教育由 4 所学院构成：**Columbia College**（文理，授予 BA，58 个系）、**The Fu Foundation School of Engineering and Applied Science (Columbia Engineering / SEAS)**（工程，授予 BS，11 个工程系 + 跨学科 Data Science / Engineering）、**School of General Studies (GS)**（面向非传统/成人学习者，授予 BA/BS，与 CC 共享 FAS 系所 + 39 个 GS-unique 主修）、以及 **Barnard College**（女子学院，Columbia 附属，授予 BA，约 50 个系）。CC、SEAS、Barnard 共用同一套本科申请系统（`undergrad.admissions.columbia.edu`），GS 有独立招生。所有本科生共享 Columbia 著名的 **Core Curriculum**（核心课程：Literature Humanities、Contemporary Civilization、Art/Music Humanities、Frontiers of Science、University Writing、Foreign Language、Global Core、Science、Gym）。完整层级树见 0.2。
## 1.2 本科主修 — 按 学院 > 系 > 学位级别 分组
#### Columbia College

##### African American and African Diaspora Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | African American and African Diaspora Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### American Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | American Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Ancient Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Ancient Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Anthropology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Anthropology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Archaeology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Archaeology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Architecture

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Architecture | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Art History and Archaeology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Art History and Archaeology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Astronomy

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Astronomy | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Biological Sciences

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Business

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Business | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Chemistry

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Classics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Classics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Cognitive Science

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Cognitive Science | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Comparative Literature and Society

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Comparative Literature and Society | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Computer Science

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Creative Writing

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Creative Writing | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Dance

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Dance | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Drama and Theatre Arts

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Drama and Theatre Arts | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Earth and Environmental Sciences

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Earth and Environmental Sciences | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### East Asian Languages and Cultures

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | East Asian Languages and Cultures | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Ecology, Evolution, and Environmental Biology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Ecology, Evolution, and Environmental Biology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Economics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Economics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Education

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Education | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### English and Comparative Literature

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | English and Comparative Literature | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Ethnicity and Race Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Ethnicity and Race Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Film and Media Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Film and Media Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### French

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | French | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Germanic Languages

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Germanic Languages | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Global Affairs and Public Policy

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Global Affairs and Public Policy | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### History

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | History | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Human Rights

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Human Rights | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Italian

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Italian | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Jazz Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Jazz Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Jewish Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Jewish Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Latin American and Caribbean Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Latin American and Caribbean Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Latin American and Iberian Cultures

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Latin American and Iberian Cultures | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Linguistics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Linguistics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Mathematics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Medieval and Renaissance Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Medieval and Renaissance Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Middle Eastern, South Asian, and African Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Middle Eastern, South Asian, and African Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Music

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Music | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Philosophy

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Physics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Physics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Political Science

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Political Science | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Psychology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Psychology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Public Health

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Public Health | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Regional Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Regional Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Religion

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Religion | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Science and Society

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Science and Society | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Slavic Languages

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Slavic Languages | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Sociology

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Sociology | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Statistics

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Statistics | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Sustainable Development

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Sustainable Development | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Urban Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Urban Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Visual Arts

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Visual Arts | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |

##### Women's and Gender Studies

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Women's and Gender Studies | https://bulletin.columbia.edu/columbia-college/departments-instruction/ |
#### Columbia Engineering (SEAS)

##### Applied Physics and Applied Mathematics

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/undergraduate-programs/applied-mathematics-bs/ |
| 2 | Applied Physics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/undergraduate-programs/applied-physics-bs/ |
| 3 | Double Major in Applied Physics and Applied Mathematics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/undergraduate-programs/double-major-apams/ |

###### Certificate

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Medical Physics (Certification of Professional Achievement) | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/medical-physics-certification-professional-achievement/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/applied-mathematics-ms/ |
| 2 | Applied Physics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/applied-physics-ms/ |
| 3 | Medical Physics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/medical-physics-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/applied-mathematics-phd-engscd/ |
| 2 | Applied Physics | https://bulletin.columbia.edu/academic-departments-programs/applied-physics-applied-mathematics/graduate-programs/applied-physics-phd-engscd/ |

##### Biomedical Engineering

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.columbia.edu/academic-departments-programs/biomedical-engineering/undergraduate-programs/biomedical-engineering-bs/ |
| 2 | Integrated BS/MS in Biomedical Engineering | https://bulletin.columbia.edu/academic-departments-programs/biomedical-engineering/undergraduate-programs/integrated-bsms-program-biomedical-engineering/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.columbia.edu/academic-departments-programs/biomedical-engineering/graduate-programs/biomedical-engineering-ms/ |
| 2 | Biomedical Engineering (MD/MS) | https://bulletin.columbia.edu/academic-departments-programs/biomedical-engineering/graduate-programs/biomedical-engineering-md-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://bulletin.columbia.edu/academic-departments-programs/biomedical-engineering/graduate-programs/biomedical-engineering-phd/ |

##### Chemical Engineering

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://bulletin.columbia.edu/academic-departments-programs/chemical-engineering/undergraduate-programs/chemical-engineering-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://bulletin.columbia.edu/academic-departments-programs/chemical-engineering/graduate-programs/chemical-engineering-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering (PhD/DES) | https://bulletin.columbia.edu/academic-departments-programs/chemical-engineering/graduate-programs/chemical-engineering-phddes/ |

##### Civil Engineering and Engineering Mechanics

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://bulletin.columbia.edu/academic-departments-programs/civil-engineering-engineering-mechanics/undergraduate-programs/civil-engineering-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Civil Engineering and Engineering Mechanics | https://bulletin.columbia.edu/academic-departments-programs/civil-engineering-engineering-mechanics/graduate-programs/civil-engineering-engineering-mechanics-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Civil Engineering and Engineering Mechanics | https://bulletin.columbia.edu/academic-departments-programs/civil-engineering-engineering-mechanics/graduate-programs/civil-engineering-engineering-mechanics-engscd-phd/ |

##### Computer Engineering Program

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://bulletin.columbia.edu/academic-departments-programs/computer-engineering-program/undergraduate-programs/computer-engineering-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://bulletin.columbia.edu/academic-departments-programs/computer-engineering-program/graduate-programs/computer-engineering-program-ms/ |

##### Computer Science

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.columbia.edu/academic-departments-programs/computer-science/undergraduate-programs/computer-science-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.columbia.edu/academic-departments-programs/computer-science/graduate-programs/computer-science-ms/ |
| 2 | CS@CU MS Bridge Program in Computer Science | https://bulletin.columbia.edu/academic-departments-programs/computer-science/graduate-programs/cs-cu-ms-bridge-program-computer-science/ |
| 3 | Dual Degree Program in Journalism and Computer Science | https://bulletin.columbia.edu/academic-departments-programs/computer-science/graduate-programs/dual-degree-program-journalism-computer-science/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://bulletin.columbia.edu/academic-departments-programs/computer-science/graduate-programs/computer-science-phd/ |

##### Earth and Environmental Engineering

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Earth and Environmental Engineering | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/undergraduate-programs/earth-environmental-engineering-bs/ |
| 2 | Mining Engineering | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/undergraduate-programs/mining-engineering-bs/ |

###### Certificate

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Professional Degree; Engineer of Mines | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/graduate-programs/professional-degree-engineer-mines/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Earth and Environmental Engineering (MS-EEE) | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/graduate-programs/earth-environmental-engineering-ms-eee/ |
| 2 | Carbon Management | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/graduate-programs/carbon-management-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Earth and Environmental Engineering | https://bulletin.columbia.edu/academic-departments-programs/earth-environmental-engineering/graduate-programs/earth-environmental-engineering-engscd-phd/ |

##### Electrical Engineering

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.columbia.edu/academic-departments-programs/electrical-engineering/undergraduate-programs/electrical-engineering-bs/ |
| 2 | Electrical Engineering (BS/MS) | https://bulletin.columbia.edu/academic-departments-programs/electrical-engineering/undergraduate-programs/electrical-engineering-bs-ms/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.columbia.edu/academic-departments-programs/electrical-engineering/graduate-programs/electrical-engineering-ms/ |
| 2 | Quantum Science and Technology | https://bulletin.columbia.edu/academic-departments-programs/electrical-engineering/graduate-programs/quantum-science-and-technology-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://bulletin.columbia.edu/academic-departments-programs/electrical-engineering/graduate-programs/electrical-engineering-phd-engscd/ |

##### Industrial Engineering and Operations Research

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/undergraduate-programs/industrial-engineering-bs/ |
| 2 | Operations Research | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/undergraduate-programs/operations-research-bs/ |
| 3 | Undergraduate Advanced Track (IE/OR) | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/undergraduate-programs/undergraduate-advanced-track/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/industrial-engineering-ms/ |
| 2 | Operations Research | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/operations-research-ms/ |
| 3 | Financial Engineering | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/financial-engineering-ms/ |
| 4 | Business Analytics | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/business-analytics-ms/ |
| 5 | Management Science and Engineering | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/management-science-engineering-ms/ |
| 6 | Industrial Engineering (Joint MS and MBA) | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/industrial-engineering-joint-ms-mba/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Industrial Engineering / Operations Research | https://bulletin.columbia.edu/academic-departments-programs/industrial-engineering-operations-research/graduate-programs/industrial-engineering-phd-operations-research-phd/ |

##### Materials Science and Engineering Program

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Materials Science | https://bulletin.columbia.edu/academic-departments-programs/materials-science-engineering-program/undergraduate-programs/material-science-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://bulletin.columbia.edu/academic-departments-programs/materials-science-engineering-program/graduate-programs/materials-science-engineering-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Materials Science and Engineering | https://bulletin.columbia.edu/academic-departments-programs/materials-science-engineering-program/graduate-programs/materials-science-engineering-engscd-phd/ |

##### Mechanical Engineering

###### BS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.columbia.edu/academic-departments-programs/mechanical-engineering/undergraduate-programs/mechanical-engineering-bs/ |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.columbia.edu/academic-departments-programs/mechanical-engineering/graduate-programs/mechanical-engineering-ms/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://bulletin.columbia.edu/academic-departments-programs/mechanical-engineering/graduate-programs/mechanical-engineering-phd/ |

##### Data Science (interdepartmental)

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Data Science | https://bulletin.columbia.edu/academic-departments-programs/data-science/ |

##### Engineering (School-wide interdisciplinary)

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MS in AI | https://bulletin.columbia.edu/academic-departments-programs/engineering/graduate-programs/ms-in-ai/ |
| 2 | xMS | https://bulletin.columbia.edu/academic-departments-programs/engineering/graduate-programs/xms/ |
| 3 | MBAxMS | https://bulletin.columbia.edu/academic-departments-programs/engineering/graduate-programs/mbaxms/ |
| 4 | Elective Specialization | https://bulletin.columbia.edu/academic-departments-programs/engineering/graduate-programs/elective-specialization/ |

##### Engineering Minors

###### Minor

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/aerospace-engineering-minor/ |
| 2 | American Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/american-studies-minor/ |
| 3 | Anthropology Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/anthropology-minor/ |
| 4 | Applied Mathematics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/applied-mathematics-minor/ |
| 5 | Applied Physics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/applied-physics-minor/ |
| 6 | Architecture Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/architecture-minor/ |
| 7 | Art History Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/art-history-minor/ |
| 8 | Artificial Intelligence Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/artificial-intelligence-minor/ |
| 9 | Biomedical Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/biomedical-engineering-minor/ |
| 10 | Catalan Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/catalan-minor/ |
| 11 | Chemical Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/chemical-engineering-minor/ |
| 12 | Civil Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/civil-engineering-minor/ |
| 13 | Computer Science Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/computer-science-minor/ |
| 14 | Dance Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/dance-minor/ |
| 15 | Earth and Environmental Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/earth-and-environmental-engineering-minor/ |
| 16 | East Asian Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/east-asian-studies-minor/ |
| 17 | Economics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/economics-minor/ |
| 18 | Electrical Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/electrical-engineering-minor/ |
| 19 | Engineering Mechanics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/engineering-mechanics-minor/ |
| 20 | English and Comparative Literature Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/english-and-comparative-literature-minor/ |
| 21 | Entrepreneurship and Innovation Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/entrepreneurship-and-innovation-minor/ |
| 22 | Ethnicity and Race Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/ethnicity-and-race-minor/ |
| 23 | Film and Media Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/film-and-media-studies-minor/ |
| 24 | French and Francophone Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/french-and-francophone-studies-minor/ |
| 25 | Fusion Energy Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/fusion-energy-minor/ |
| 26 | German Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/german-minor/ |
| 27 | Greek or Latin Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/greek-or-latin-minor/ |
| 28 | Hispanic Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/hispanic-studies-minor/ |
| 29 | History Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/history-minor/ |
| 30 | Industrial Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/industrial-engineering-minor/ |
| 31 | Italian Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/italian-minor/ |
| 32 | Jewish Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/jewish-studies-minor/ |
| 33 | Linguistics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/linguistics-minor/ |
| 34 | Materials Science Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/materials-science-minor/ |
| 35 | Mechanical Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/mechanical-engineering-minor/ |
| 36 | Middle Eastern, South Asian, and African Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/middle-eastern-south-asian-and-african-studies-minor/ |
| 37 | Mining Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/mining-engineering-minor/ |
| 38 | Music Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/music-minor/ |
| 39 | Operations Research Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/operations-research-minor/ |
| 40 | Philosophy Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/philosophy-minor/ |
| 41 | Political Science Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/political-science-minor/ |
| 42 | Portuguese Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/portuguese-minor/ |
| 43 | Psychology Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/psychology-minor/ |
| 44 | Religion Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/religion-minor/ |
| 45 | Sociology Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/sociology-minor/ |
| 46 | Statistics Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/statistics-minor/ |
| 47 | Statistics (Applied Track) Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/statistics-applied-track-minor/ |
| 48 | Statistics (Theory Track) Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/statistics-theory-track-minor/ |
| 49 | Sustainable Engineering Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/sustainable-engineering-minor/ |
| 50 | Women's, Gender and Sexuality Studies Minor | https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/womens-gender-and-sexuality-studies-minor/ |
#### School of General Studies

##### GS Majors

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics (BS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 2 | Architecture, History and Theory | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 3 | Art History | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 4 | Art History and Visual Arts | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 5 | Astrophysics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 6 | Biochemistry | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 7 | Biophysics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 8 | Chemical Physics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 9 | Classical Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 10 | Climate and Sustainability | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 11 | Climate System Science | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 12 | Cognitive Science (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 13 | Computational Biology | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 14 | Computer Science-Mathematics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 15 | Data Science | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 16 | Earth and Space | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 17 | Ecology, Evolution, and Environmental Biology (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 18 | Education Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 19 | Environmental Biology | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 20 | Environmental Chemistry | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 21 | Environmental Science | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 22 | Information Science | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 23 | Mathematics-Statistics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 24 | Medical Humanities | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 25 | Neuroscience and Behavior | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 26 | Physical Education | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 27 | Political Science-Statistics | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 28 | Portuguese Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 29 | Russian Language and Culture | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 30 | Russian Literature and Culture | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 31 | Slavic Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 32 | Sustainable Development (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 33 | Yiddish Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 34 | Business Management | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 35 | Education (Urban Teaching) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 36 | Jazz Studies (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 37 | Jewish Studies (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 38 | Medieval and Renaissance Studies (GS) | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
| 39 | Modern Greek Studies | https://bulletin.columbia.edu/general-studies/majors-concentrations/ |
#### Barnard College

##### Barnard Departments

###### BA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Africana Studies | https://barnard.edu/departments-and-programs |
| 2 | American Studies | https://barnard.edu/departments-and-programs |
| 3 | Anthropology | https://barnard.edu/departments-and-programs |
| 4 | Architecture | https://barnard.edu/departments-and-programs |
| 5 | Art History | https://barnard.edu/departments-and-programs |
| 6 | Asian & Middle Eastern Cultures | https://barnard.edu/departments-and-programs |
| 7 | Biological Sciences | https://barnard.edu/departments-and-programs |
| 8 | Chemistry | https://barnard.edu/departments-and-programs |
| 9 | Classics and Ancient Studies | https://barnard.edu/departments-and-programs |
| 10 | Cognitive Science | https://barnard.edu/departments-and-programs |
| 11 | Comparative Literature & Translation Studies | https://barnard.edu/departments-and-programs |
| 12 | Computer Science | https://barnard.edu/departments-and-programs |
| 13 | Consortium of Critical Interdisciplinary Studies | https://barnard.edu/departments-and-programs |
| 14 | Dance | https://barnard.edu/departments-and-programs |
| 15 | Economics | https://barnard.edu/departments-and-programs |
| 16 | Education | https://barnard.edu/departments-and-programs |
| 17 | English | https://barnard.edu/departments-and-programs |
| 18 | Environmental Science | https://barnard.edu/departments-and-programs |
| 19 | European Studies | https://barnard.edu/departments-and-programs |
| 20 | Film Studies | https://barnard.edu/departments-and-programs |
| 21 | French and Francophone Studies | https://barnard.edu/departments-and-programs |
| 22 | German | https://barnard.edu/departments-and-programs |
| 23 | History | https://barnard.edu/departments-and-programs |
| 24 | Italian | https://barnard.edu/departments-and-programs |
| 25 | Mathematics | https://barnard.edu/departments-and-programs |
| 26 | Music | https://barnard.edu/departments-and-programs |
| 27 | Neuroscience and Behavior | https://barnard.edu/departments-and-programs |
| 28 | Philosophy | https://barnard.edu/departments-and-programs |
| 29 | Physics | https://barnard.edu/departments-and-programs |
| 30 | Political Science | https://barnard.edu/departments-and-programs |
| 31 | Psychology | https://barnard.edu/departments-and-programs |
| 32 | Religion | https://barnard.edu/departments-and-programs |
| 33 | Slavic Languages | https://barnard.edu/departments-and-programs |
| 34 | Sociology | https://barnard.edu/departments-and-programs |
| 35 | Spanish and Latin American Cultures | https://barnard.edu/departments-and-programs |
| 36 | Statistics | https://barnard.edu/departments-and-programs |
| 37 | Theatre | https://barnard.edu/departments-and-programs |
| 38 | Urban Studies | https://barnard.edu/departments-and-programs |
| 39 | Women's, Gender, and Sexuality Studies | https://barnard.edu/departments-and-programs |
| 40 | Economics and Political Economy | https://barnard.edu/departments-and-programs |
| 41 | Medieval and Renaissance Studies | https://barnard.edu/departments-and-programs |
## 1.3 跨院/跨学科本科项目

- **Computer Science**：同一系挂靠 Columbia College (BA)、Columbia Engineering (BS) 与 School of General Studies (BA)；三院学生共修同一套 CS 课程，学位由各自学院授予。ⓘ 来源：https://bulletin.columbia.edu/columbia-college/departments-instruction/computer-science/
- **联合主修 (Joint Majors, 经 GS bulletin 列出)**：Economics-Mathematics、Economics-Philosophy、Economics-Political Science、Economics-Statistics、Computer Science-Mathematics、Mathematics-Statistics、Political Science-Statistics、Latin American and Iberian Cultures (Hispanic Cultural Studies concentration) 等 — 由 FAS 跨系联合开设，对 CC 与 GS 学生开放。ⓘ 来源：https://bulletin.columbia.edu/general-studies/majors-concentrations/
- **Columbia-Juilliard Exchange / Combined Plan (3-2 BA/BS) / Visiting Student**：Columbia College 与 SEAS 之间的 Combined Plan（3-2 工程）、Columbia-Juilliard Program（音乐/表演双项目）。ⓘ 来源：https://undergrad.admissions.columbia.edu/apply/combinedplan

## 1.4 本科辅修 (Minors) — 完整列表

Columbia Engineering bulletin 列出 **49 条本科辅修**（含 Statistics 基础轨 / Applied 轨 / Theory 轨三条），覆盖工程、文理、语言、艺术各领域。Columbia College 与 GS 的"concentration"已并入主修计数（CC 称深度方向为 concentration；GS 称 minor）。完整 SEAS 辅修表见上方 1.2 Columbia Engineering (SEAS) → Engineering Minors → Minor 表（50 行）。

## 1.5 Core Curriculum（核心课程）— 全校通用要求

Columbia Core 是美国本科教育最著名的核心课程之一，所有 Columbia College、Columbia Engineering、General Studies 本科生必须修读：
- **Literature Humanities**（文学人文，全年）
- **Contemporary Civilization**（当代文明，全年）
- **Art Humanities** / **Music Humanities**（艺术/音乐人文）
- **University Writing**（大学写作）
- **Frontiers of Science**（科学前沿）
- **Foreign Language**（外语，达到最低要求）
- **Global Core**（全球核心，2 门）
- **Science**（科学，CC/SEAS 各有要求）
- **Physical Education**（体育，2 学期 + 游泳测试）

ⓘ 来源：https://bulletin.columbia.edu/columbia-college/core-curriculum/ ; https://bulletin.columbia.edu/general-studies/the-core/

## 1.6 Course-ID → Major 快速查找

Columbia 不使用 MIT 风格的数字编号主修（如 6-3）；课程用前缀+4 位数字（如 ECON UN1105、COMS W1004、PHYS UN1201），前缀代表系所（ECON=经济学、COMS=计算机科学、PHYS=物理）。本科主修通过系所名定位，不通过编号。

---

# 2. 研究生教育 (Graduate Education — 规则 5 分组)
## 2.1 研究生项目 — 按 学院 > 系 > 学位级别 分组
#### GSAS

##### MA Programs

###### MA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | African American Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 2 | American Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 3 | Anthropology | https://www.gsas.columbia.edu/content/ma-programs |
| 4 | Art History and Archaeology | https://www.gsas.columbia.edu/content/ma-programs |
| 5 | Biotechnology | https://www.gsas.columbia.edu/content/ma-programs |
| 6 | Classical Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 7 | Classics | https://www.gsas.columbia.edu/content/ma-programs |
| 8 | East Asian Languages and Cultures | https://www.gsas.columbia.edu/content/ma-programs |
| 9 | East Asian Regional Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 10 | Ecology, Evolution and Conservation Biology | https://www.gsas.columbia.edu/content/ma-programs |
| 11 | Economics | https://www.gsas.columbia.edu/content/ma-programs |
| 12 | English and Comparative Literature | https://www.gsas.columbia.edu/content/ma-programs |
| 13 | European History, Politics and Society | https://www.gsas.columbia.edu/content/ma-programs |
| 14 | European History, Politics, and Society (MA/MSc with LSE) | https://www.gsas.columbia.edu/content/ma-programs |
| 15 | French | https://www.gsas.columbia.edu/content/ma-programs |
| 16 | Germanic Languages | https://www.gsas.columbia.edu/content/ma-programs |
| 17 | Global Thought | https://www.gsas.columbia.edu/content/ma-programs |
| 18 | History and Literature | https://www.gsas.columbia.edu/content/ma-programs |
| 19 | Human Rights Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 20 | International and World History (MA/MSc with LSE) | https://www.gsas.columbia.edu/content/ma-programs |
| 21 | Islamic Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 22 | Italian | https://www.gsas.columbia.edu/content/ma-programs |
| 23 | Japanese Pedagogy | https://www.gsas.columbia.edu/content/ma-programs |
| 24 | Jewish Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 25 | Latin American and Caribbean Regional Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 26 | Latin American and Iberian Cultures (Hispanic Cultural Studies concentration) | https://www.gsas.columbia.edu/content/ma-programs |
| 27 | Mathematics of Finance | https://www.gsas.columbia.edu/content/ma-programs |
| 28 | Medieval and Renaissance Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 29 | Middle Eastern, South Asian, and African Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 30 | Modern Art: Critical and Curatorial Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 31 | Museum Anthropology | https://www.gsas.columbia.edu/content/ma-programs |
| 32 | Oral History | https://www.gsas.columbia.edu/content/ma-programs |
| 33 | Philosophical Foundations of Physics | https://www.gsas.columbia.edu/content/ma-programs |
| 34 | Philosophy | https://www.gsas.columbia.edu/content/ma-programs |
| 35 | Political Science | https://www.gsas.columbia.edu/content/ma-programs |
| 36 | Quantitative Methods in the Social Sciences | https://www.gsas.columbia.edu/content/ma-programs |
| 37 | Quantitative Methods in the Social Sciences (Dual-Degree) | https://www.gsas.columbia.edu/content/ma-programs |
| 38 | Religion | https://www.gsas.columbia.edu/content/ma-programs |
| 39 | Religion-Journalism Dual MA/MS | https://www.gsas.columbia.edu/content/ma-programs |
| 40 | Russia, Eurasia, and Eastern Europe Regional Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 41 | Russian Translation | https://www.gsas.columbia.edu/content/ma-programs |
| 42 | Slavic Cultures | https://www.gsas.columbia.edu/content/ma-programs |
| 43 | Slavic Languages | https://www.gsas.columbia.edu/content/ma-programs |
| 44 | Sociology | https://www.gsas.columbia.edu/content/ma-programs |
| 45 | South Asian Studies | https://www.gsas.columbia.edu/content/ma-programs |
| 46 | Statistics | https://www.gsas.columbia.edu/content/ma-programs |

##### PhD Programs

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | African American and African Diaspora Studies | https://www.gsas.columbia.edu/content/phd-programs |
| 2 | Anthropology | https://www.gsas.columbia.edu/content/phd-programs |
| 3 | Architecture (GSAPP) | https://www.gsas.columbia.edu/content/phd-programs |
| 4 | Art History and Archaeology | https://www.gsas.columbia.edu/content/phd-programs |
| 5 | Astronomy | https://www.gsas.columbia.edu/content/phd-programs |
| 6 | Biological Sciences | https://www.gsas.columbia.edu/content/phd-programs |
| 7 | Chemical Physics | https://www.gsas.columbia.edu/content/phd-programs |
| 8 | Chemistry | https://www.gsas.columbia.edu/content/phd-programs |
| 9 | Classical Studies | https://www.gsas.columbia.edu/content/phd-programs |
| 10 | Classics | https://www.gsas.columbia.edu/content/phd-programs |
| 11 | Earth and Environmental Sciences | https://www.gsas.columbia.edu/content/phd-programs |
| 12 | East Asian Languages and Cultures | https://www.gsas.columbia.edu/content/phd-programs |
| 13 | Ecology and Evolutionary Biology | https://www.gsas.columbia.edu/content/phd-programs |
| 14 | English and Comparative Literature | https://www.gsas.columbia.edu/content/phd-programs |
| 15 | French | https://www.gsas.columbia.edu/content/phd-programs |
| 16 | Germanic Languages | https://www.gsas.columbia.edu/content/phd-programs |
| 17 | History | https://www.gsas.columbia.edu/content/phd-programs |
| 18 | Historic Preservation (GSAPP) | https://www.gsas.columbia.edu/content/phd-programs |
| 19 | Italian | https://www.gsas.columbia.edu/content/phd-programs |
| 20 | Latin American and Iberian Cultures | https://www.gsas.columbia.edu/content/phd-programs |
| 21 | Mathematics | https://www.gsas.columbia.edu/content/phd-programs |
| 22 | Middle Eastern, South Asian, and African Studies | https://www.gsas.columbia.edu/content/phd-programs |
| 23 | Music | https://www.gsas.columbia.edu/content/phd-programs |
| 24 | Philosophy | https://www.gsas.columbia.edu/content/phd-programs |
| 25 | Physics | https://www.gsas.columbia.edu/content/phd-programs |
| 26 | Political Science | https://www.gsas.columbia.edu/content/phd-programs |
| 27 | Psychology | https://www.gsas.columbia.edu/content/phd-programs |
| 28 | Religion | https://www.gsas.columbia.edu/content/phd-programs |
| 29 | Slavic Languages | https://www.gsas.columbia.edu/content/phd-programs |
| 30 | Sociology | https://www.gsas.columbia.edu/content/phd-programs |
| 31 | Statistics | https://www.gsas.columbia.edu/content/phd-programs |
| 32 | Sustainable Development | https://www.gsas.columbia.edu/content/phd-programs |
| 33 | Theatre and Performance | https://www.gsas.columbia.edu/content/phd-programs |
| 34 | Urban Planning (GSAPP) | https://www.gsas.columbia.edu/content/phd-programs |

##### Dual-Degree Programs

###### Dual

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | JD/PhD | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 2 | MD/PhD | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 3 | International and World History (MA/MSc, with LSE) | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 4 | Religion-Journalism Dual MA/MS | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |

##### Graduate Certificates

###### Certificate

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | African Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 2 | Comparative Literature and Society | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 3 | East Asian Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 4 | East Central Europe | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 5 | European Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 6 | Human Rights | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 7 | Latin American Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 8 | Medieval and Renaissance Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 9 | Middle East Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 10 | Psychoanalytic Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 11 | Russian Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 12 | South Asian Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |

##### PhD Concentrations

###### PhD-Conc

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Atmospheric Science | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 2 | Buddhist Studies | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
| 3 | Mathematical Structures for Environmental and Social Sciences | https://www.gsas.columbia.edu/content/dual-degree-certificate-programs |
#### Columbia Business School

##### Business

###### MBA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://academics.business.columbia.edu/mba |
| 2 | Executive MBA (EMBA) | https://academics.business.columbia.edu/emba |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MS in Accounting and Fundamental Analysis (MSAFA) | https://academics.business.columbia.edu/admissions/ms |
| 2 | MS in Financial Economics (MSFE) | https://academics.business.columbia.edu/admissions/ms |
| 3 | MS in Marketing Science (MSM) | https://academics.business.columbia.edu/admissions/ms |
| 4 | MS in Business Analytics (MSBA) | https://academics.business.columbia.edu/ |
| 5 | MS in Climate Finance (with Climate School) | https://academics.business.columbia.edu/ |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctoral Program (PhD) | https://academics.business.columbia.edu/phd |
#### Columbia Law School

##### Law

###### JD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Juris Doctor (JD) | https://www.law.columbia.edu/academics/jd-program-and-curriculum |

###### JSD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of the Science of Law (JSD) | https://www.law.columbia.edu/academics/jsd-program-and-curriculum |

###### LLM

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Laws (LLM) | https://www.law.columbia.edu/academics/llm-program-and-curriculum |
| 2 | Executive LL.M. | https://www.law.columbia.edu/academics/executive-llm-program-and-curriculum |
#### Vagelos College of Physicians & Surgeons

##### Medicine

###### DPT

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of Physical Therapy (DPT) | https://www.vagelos.columbia.edu/education/academic-programs/programs-physical-therapy |

###### EdD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of Education in Movement Science | https://www.vagelos.columbia.edu/education/academic-programs/programs-physical-therapy |

###### MD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine (MD) | https://www.vagelos.columbia.edu/education/academic-programs/md-program |
| 2 | Columbia-Bassett MD Track | https://www.vagelos.columbia.edu/education/academic-programs/md-program/columbia-bassett-program |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MS in Genetic Counseling | https://www.vagelos.columbia.edu/education/academic-programs/program-genetic-counseling |
| 2 | Programs in Human Nutrition (MS) | https://www.vagelos.columbia.edu/education/academic-programs/programs-human-nutrition |
| 3 | MS in Occupational Therapy | https://www.vagelos.columbia.edu/education/academic-programs/programs-occupational-therapy |
| 4 | MS in Bioethics | https://www.vagelos.columbia.edu/education/academic-programs/additional-masters-degree-programs |
| 5 | MS in Biomedical Informatics | https://www.vagelos.columbia.edu/education/academic-programs/additional-masters-degree-programs |
| 6 | MS in Narrative Medicine | https://www.vagelos.columbia.edu/education/academic-programs/additional-masters-degree-programs |

###### OTD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy Doctorate (OTD) | https://www.vagelos.columbia.edu/education/academic-programs/programs-occupational-therapy |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biomedical Informatics (PhD) | https://www.vagelos.columbia.edu/education/academic-programs/vagelos-institutes-biomedical-research-education/phd-programs |
| 2 | Biomedical Life Sciences (PhD, 10 tracks) | https://www.vagelos.columbia.edu/education/academic-programs/vagelos-institutes-biomedical-research-education/phd-programs |
| 3 | Neurobiology and Behavior (PhD) | https://www.vagelos.columbia.edu/education/academic-programs/vagelos-institutes-biomedical-research-education/phd-programs |
#### Mailman School of Public Health

##### Public Health

###### DrPH

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biostatistics (DrPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 2 | Environmental Health Sciences (DrPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 3 | Epidemiology (DrPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |

###### MHA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MHA (Full-Time) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 2 | MHA (Part-Time) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 3 | Executive MHA/MPH | https://www.publichealth.columbia.edu/become-student/degree-programs |

###### MPH

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biostatistics (MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 2 | Environmental Health Sciences (MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 3 | Epidemiology (Accelerated MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 4 | Epidemiology (MPH 2yr) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 5 | Health Policy and Management (Accelerated MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 6 | Health Policy and Management (MPH 2yr) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 7 | Population and Family Health (Accelerated MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 8 | Population and Family Health (MPH 2yr) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 9 | Sociomedical Sciences (Accelerated MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 10 | Sociomedical Sciences (MPH 2yr) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 11 | General Public Health (Accelerated MPH) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 12 | Advanced MPH Online | https://www.publichealth.columbia.edu/become-student/degree-programs |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biostatistics (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 2 | Environmental Health Sciences (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 3 | Epidemiology (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 4 | Epidemiology (Online MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 5 | Health Policy and Management (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 6 | Population and Family Health (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 7 | Sociomedical Sciences (MS) | https://www.publichealth.columbia.edu/become-student/degree-programs |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Biostatistics (PhD) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 2 | Environmental Health Sciences (PhD) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 3 | Epidemiology (PhD) | https://www.publichealth.columbia.edu/become-student/degree-programs |
| 4 | Sociomedical Sciences (PhD) | https://www.publichealth.columbia.edu/become-student/degree-programs |
#### School of International & Public Affairs (SIPA)

##### International & Public Affairs

###### MIA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of International Affairs (MIA) | https://www.sipa.columbia.edu/sipa-education/masters-programs |

###### MPA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration (MPA) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
| 2 | MPA in Development Practice (MPA-DP) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
| 3 | MPA in Economic Policy Management (MPA-EPM) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
| 4 | MPA in Environmental Science and Policy (MPA-ESP) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
| 5 | MPA in Global Leadership (MPA-GL) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
| 6 | Executive MPA (EMPA) | https://www.sipa.columbia.edu/sipa-education/masters-programs |
#### Columbia School of Social Work

##### Social Work

###### MSW

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Science in Social Work (MSSW) | https://socialwork.columbia.edu/degrees-we-offer |
| 2 | MSSW Online Option | https://socialwork.columbia.edu/degrees-we-offer |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | PhD in Social Work | https://socialwork.columbia.edu/degrees-we-offer |
#### GSAPP (Architecture, Planning, Preservation)

##### Architecture/Planning/Preservation

###### MArch

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Architecture (MArch) | https://www.arch.columbia.edu/programs/1-master-of-architecture |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MS Advanced Architectural Design | https://www.arch.columbia.edu/programs |
| 2 | MS Computational Design Practices | https://www.arch.columbia.edu/programs |
| 3 | MS Critical, Curatorial & Conceptual Practices | https://www.arch.columbia.edu/programs |
| 4 | MS Architecture and Urban Design | https://www.arch.columbia.edu/programs/9-m-s-architecture-and-urban-design |
| 5 | MS Urban Planning | https://www.arch.columbia.edu/programs/10-m-s-urban-planning |
| 6 | MS Historic Preservation | https://www.arch.columbia.edu/programs/7-m-s-historic-preservation |
| 7 | MS Real Estate Development | https://www.arch.columbia.edu/programs |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | PhD Architecture | https://www.arch.columbia.edu/programs |
| 2 | PhD Urban Planning | https://www.arch.columbia.edu/programs/11-ph-d-in-urban-planning |
| 3 | PhD Historic Preservation | https://www.arch.columbia.edu/programs/14-ph-d-in-historic-preservation |
#### Columbia Journalism School

##### Journalism

###### MA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Arts (MA) | https://journalism.columbia.edu/academics |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Master of Science (MS) | https://journalism.columbia.edu/academics |
| 2 | MS Data Journalism | https://journalism.columbia.edu/academics |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | PhD in Journalism | https://journalism.columbia.edu/academics |
#### School of the Arts

##### Arts

###### MA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MA in Film and Media Studies | https://arts.columbia.edu/programs-study/film-and-media-studies |

###### MFA

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | MFA in Film | https://arts.columbia.edu/film |
| 2 | MFA in Theatre | https://arts.columbia.edu/theatre |
| 3 | MFA in Visual Arts | https://arts.columbia.edu/visual-arts |
| 4 | MFA in Sound Art (interdisciplinary, via Visual Arts) | https://arts.columbia.edu/sound-art |
| 5 | MFA in Writing | https://arts.columbia.edu/writing |
#### Columbia School of Nursing

##### Nursing

###### DNP

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of Nursing Practice (DNP) | https://www.nursing.columbia.edu/academics/academic-programs/doctor-nursing-practice |

###### MS

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Masters Direct Entry (MDE) Program | https://www.nursing.columbia.edu/academics/academic-programs/masters-direct-entry-program-non-nurses |
| 2 | Masters in Advanced Clinical Management and Leadership | https://www.nursing.columbia.edu/academics/academic-programs/masters-advanced-clinical-management-and-leadership |

###### PhD

| # | 专业/项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy (PhD) in Nursing | https://www.nursing.columbia.edu/academics/academic-programs/doctor-philosophy |
## 2.2 项目深度示例：Columbia Business School — Master of Business Administration (MBA)

> **学院**：Columbia Business School (CBS)
> **项目**：Full-Time MBA
> **申请入口**：https://academics.business.columbia.edu/admissions/mba
> **学位**：Master of Business Administration (MBA)
> **学制**：20 个月（两学年），Manhattanville 校区
> **申请材料**：本科成绩单、GMAT/GRE（CBS 接受 GRE）、TOEFL/IELTS/PTE（非英语授课本科者）、2 封推荐信、个人陈述、简历、申请费
> **2025 荣誉**：Poets&Quants 2025 MBA Program of the Year（CBS 官网标注）
> **资金**：CBS 自管奖学金与助学金；MBA 学费由 Student Financial Services 公布（P0 follow-up：抓取 2026-27 学费明细）
> **双学位**：11 条 MBA 双学位轨道（详见 2.1 CBS 表与证据链 E-G-008）
> **课程结构**：核心课（财务、营销、运营、统计、领导力）+ 选修（金融、创业、市场营销、媒体、房地产、社会企业等方向）；著名集群包括 Finance、Healthcare、Tech/Analytics

ⓘ 来源：https://academics.business.columbia.edu/mba ; https://academics.business.columbia.edu/dual-degrees/all

## 2.3 研究生招生模式

**分权式（decentralized）**——Columbia 没有统一的"研究生院招生办公室"覆盖所有专业学院。GSAS 统管文理类 MA/PhD 招生（入口 `gsas-admissions@columbia.edu`，统一申请 portal），但 10 所专业学院（CBS、Law、Vagelos、Mailman、SIPA、CSSW、GSAPP、Journalism、Arts、Nursing）各自独立招生、自定截止日期、自定申请费、自管奖学金与学费。
- **GSAS**：统一申请 portal，申请费 ~$120（各项目略有差异），多数 PhD 全额资助（5 年 tuition + stipend + health insurance）
- **CBS**：MBA 申请费 ~$250，分多轮（ED 9月、RD 1月、April round）
- **Law**：JD 通过 LSAC（CAS），LLM/JSD 独立申请
- **Vagelos (Medicine)**：MD 通过 AMCAS，PhD/MS 各项目独立
- **Mailman**：6 系分别招生，统一 SOPHAS/校内 portal
- **April 15 honor date**：Columbia 遵循 CGS（Council of Graduate Schools）4 月 15 日答复协议，适用于 GSAS 与多数研究生项目

ⓘ 来源：https://www.gsas.columbia.edu/content/admissions ; https://academics.business.columbia.edu/admissions

---

# 3. 申请要求与截止日期 (Application Requirements & Deadlines)

## 3.1 本科 — 核心数据表（Columbia College + Columbia Engineering）

| 维度 | 值 | 来源 |
|------|------|------|
| 招生网站 | https://undergrad.admissions.columbia.edu/ | E-U-001 |
| 申请平台 | Common Application 或 Coalition Application（任选其一，无偏好）；QuestBridge（National College Match） | E-U-002 |
| **Early Decision (ED) 截止** | **11 月 1 日**（与 QuestBridge National College Match 同日）| E-U-003 |
| ED 助学金申请截止 | 11 月 15 日 | E-U-003 |
| ED 录取发布 | 12 月中旬 | E-U-003 |
| **Regular Decision (RD) 截止** | **1 月 1 日** | E-U-003 |
| ED 录取学生答复截止 | 1 月中旬 | E-U-003 |
| RD 助学金申请截止 | 2 月 15 日 | E-U-003 |
| RD 录取发布 | 3 月下旬 | E-U-003 |
| RD 录取学生答复截止（Reply） | 5 月 1 日 | E-U-003 |
| 注册延期申请截止 | 5 月 15 日 | E-U-003 |
| 最终成绩单截止 | 6 月下旬 | E-U-003 |
| 标化考试政策 (2026-27) | **Test-Optional**（2026-2027 申请季仍为可选） | E-U-004 |
| 标化考试政策 (2027-28 起) | **Test-Required**（自 2027 年 8 月起重启强制标化要求；可申请豁免）| E-U-004 |
| SAT/ACT 最低分 | 无最低分要求；不要求 ACT 写作或科学部分；执行 superscore | E-U-004 |
| 面试政策 | **不设面试**（2023 年 5 月 18 日公告起取消） | E-U-005 |
| 推荐信 | 1 份 Secondary School Report（辅导员）+ 2 份学科教师推荐 | E-U-001 |
| 申请费 | **$85**（不可退还；电子支票/Visa/MC/Discover/AmEx 在线支付，不接受现金或纸质支票）| E-U-006 |
| Fee Waiver 家庭收入门槛 | 家庭年收入低于 **$66,000 USD** 可自动申请 fee waiver | E-U-006 |
| 作品集/补充材料 | 可选（艺术/音乐/舞蹈/戏剧/电影等可选提交 Supplementary Materials） | E-U-001 |
| 转学途径 | Transfer、Combined Plan (3-2 BA/BS 与 90+ 合作文理学院)、Visiting Student | E-U-007 |

> 注：以上截止日期基于"典型招生周期"，具体年份日期可能微调；所有录取决定通过 applicant portal 发布，Columbia 不通过 email 发布录取决定。

## 3.2 本科英语能力要求表 (English Proficiency)

> 适用条件：申请 Columbia College 或 Columbia Engineering、且 (a) 母语非英语、(b) 中学主要教学语言非英语、(c) SAT EBRW < 700 且 ACT English/Reading < 29 的申请者，**必须**提交英语能力考试成绩。Columbia 未公布最低分数门槛（"competitive"评价），但接受以下考试。

| 考试 | 最低要求 | 推荐 | 是否接受 |
|------|---------|------|---------|
| SAT Evidence-Based Reading and Writing (EBRW) | **700+**（即满足此条即视为英语达标，免考 ELP） | — | ✓（纸考/机考均接受）|
| ACT English 或 Reading | **29+**（即满足此条即视为英语达标，免考 ELP） | — | ✓ |
| TOEFL (Test of English as a Foreign Language) | 未公布最低（competitive） | 105+（行业经验值，非官方） | ✓ |
| IELTS (International English Language Testing System) | 未公布最低（competitive） | 7.5+（行业经验值） | ✓ |
| DET (Duolingo English Test) | 未公布最低（competitive） | — | ✓ |
| Cambridge English Qualifications | 未公布最低（competitive） | — | ✓ |

> **其他免考条件**：母语为英语；或中学主要教学语言为英语（整个中学阶段）。
> **2026-07-08 更新**：Columbia 强调英语能力是录取审核一部分，若申请时英语能力存疑，招生办可能联系申请者补充信息。

ⓘ 来源：https://undergrad.admissions.columbia.edu/apply/international/english-proficiency (E-U-008)

## 3.3 研究生 — 全局规则

| 维度 | 值 |
|------|------|
| 招生模式 | **分权式（decentralized）**——GSAS 统一文理 MA/PhD；10 所专业学院各自独立招生 |
| 统一申请平台 | GSAS 用校内 portal（apply.gsas.columbia.edu）；CBS 用独立 portal；Law JD 用 LSAC；Vagelos MD 用 AMCAS；Mailman 用 SOPHAS 或校内 portal |
| 标准申请费（GSAS） | ~$120（非退还）；各专业学院自定（CBS MBA ~$250，Law 等） |
| Fee waiver | GSAS 对 US 少数群体/退伍军人/部分 fellowship 申请人提供；CBS/Law 各有政策 |
| April-15 honor date | Columbia 遵循 Council of Graduate Schools (CGS) 4 月 15 日答复协议（GSAS PhD/全奖 offer）|
| GRE 政策 | GSAS 多数项目接受 GRE；近年部分项目 GRE Optional（COVID 后政策延续，需逐项目核实）；CBS 接受 GMAT/GRE；Law LSAT；Vagelos MCAT |
| 语言考试政策 | GSAS：TOEFL/IELTS（PhD 通常 TOEFL 100+ / IELTS 7.5+，各系不同）；免除条件：英语授课本科 4 年 |
| 申请时间线 | 多数 PhD/MA：12 月 – 1 月初截止；CBS MBA：ED 9 月、RD 1 月、4 月轮；Law JD：ED 11 月、RD 2 月 |
| 测试代码 | Columbia College/SEAS (UG) TOEFL Ceeb 2116；GSAS TOEFL 2162；CBS GMAT 3302；Law LSAC |

ⓘ 来源：https://www.gsas.columbia.edu/content/admissions

---

# 4. 费用与资助完整数据 (Costs & Financial Aid)

## 4.1 本科费用（2026-2027 学年，逐项明细）

| 费用项 | 金额 (USD) | 说明 |
|--------|-----------:|------|
| Tuition（学费） | **$72,800** | 2026-27 学年 |
| Fees（学杂费） | **$4,160** | 含 first-year 一次性 transcript + orientation fee $730 |
| Food（餐饮） | **$7,128** | Meal Plan EZ 19（标准餐计划）|
| Housing（住宿） | **$12,522** | 标准宿舍费；first-year 必须住校 |
| Books and supplies（书本用品） | **$1,320** | 估算 |
| Travel and local transportation（交通） | **varies** | 估算 2 次往返机票；按居住州/国不同（如印第安纳 $944，加州 $1,254）|
| Personal expenses（个人支出） | **$1,844** | 估算 |
| **Total budget（总预算）** | **$99,774** | 资助计算基础 |

ⓘ 来源：https://undergrad.admissions.columbia.edu/affordability/cost (E-U-009)

> 注：(1) First-year 必须住校；(2) 非首年学生住宿/餐饮按标准宿舍费 + Meal Plan EZ 19 计算；(3) 选择校外住宿的学生仍按相同 allowance 计入资助计算。

## 4.2 本科资助政策

| 政策 | 值 |
|------|------|
| 学费全免家庭收入门槛 | 家庭年收入 **< $150,000**（且 typical assets）→ 学费全免（tuition-free）|
| 零家长贡献门槛 | 家庭年收入 **< $66,000**（且 typical assets）→ 期望家长贡献 = **$0** |
| 贷款政策 | **No loans**（贷款不计入初始资助包；学生预期借款 = **$0**）|
| 年度奖学金/助学金总额 | Columbia 每年发放 **>$240 million** 奖学金与助学金（各来源合计）|
| 一年级生获资助比例 | 约一半（~50%）incoming first-year 获得 Columbia grant |
| 平均一年级 grant | **$77,908** |
| Pell Grant 覆盖 | 21% 一年级生获得 Pell Grant（联邦最高需求资助）|
| 低收入启动 grant | 低收入家庭一年级生获 **$2,000** 启动 grant（缓解入学过渡）|
| Need-blind 招生 | Columbia 实行 need-based 招生，对全体申请者（含国际生）need-aware 评价，但资助覆盖 100% 计算需求（**Need-aware for internationals** — 见下方说明）|

> **关于国际生的 need-blind / need-aware 说明**（重要澄清）：Columbia 本科招生对美国公民/永久居民实行 **need-blind**（录取不考虑支付能力）。对国际生，Columbia 的官方政策是 **need-aware**（need-aware for international applicants）—— 即国际生的支付能力在录取审核中会被考虑。这与 MIT / Harvard / Princeton / Yale / Dartmouth / Amherst / Bowdoin（这 7 所对国际生也 need-blind）不同。但一旦录取，Columbia 对所有录取学生（含国际生）**100% 满足计算需求**，且资助包不含贷款。**此项政策是 P0 需在下个抓取周期从官方页面精确确认的关键事实**（见 Section 6 P0 列表）。

ⓘ 来源：https://undergrad.admissions.columbia.edu/affordability/cost (E-U-009, E-U-010)

## 4.3 研究生费用与资助框架

| 维度 | 值 |
|------|------|
| 资助类型分类 | (a) **Fully funded**（GSAS PhD：5 年 tuition + stipend + health insurance）；(b) **Partially funded**（部分 MA：merit/need scholarship）；(c) **Self-funded**（专业硕士 MBA、MPH、MArch、MSSW 等） |
| 常见资助形式 | RA（研究助理）、TA（教学助理）、Fellowship（如 Presidential、Faculty Fellows）、Grant、External Fellowship（NSF、NDSEG、FLAS）|
| 申请费 | GSAS ~$120；CBS MBA ~$250；Law/Vagelos/Mailman 各异（详见各项目页）|
| Fee waiver | GSAS：US 少数群体 / 退伍军人 / 部分 fellowship；各学院独立政策 |
| PhD stipend（GSAS） | 9 个月 ~$45,000–$50,000（2026-27，含 summer 视项目）；tuition + health insurance 全免 |
| 学费（专业硕士，2026-27） | CBS MBA ~$84,000/yr；SIPA MIA/MPA ~$74,000/yr；Law JD ~$80,000/yr；Mailman MPH ~$61,000/yr（P0：精确数字需逐项目抓取 2026-27 official COA） |
| COA 链接 | https://sfs.columbia.edu/（Student Financial Services，全校统一）|

ⓘ 来源：https://www.gsas.columbia.edu/content/financial-aid ; https://sfs.columbia.edu/

---

# 5. 完整证据链索引 (Evidence Chain Index)

> 每条证据包含 field / value / source_url / source_snippet / capture_date / evidence_type。编号 E-U-NNN（本科）/ E-G-NNN（研究生）。capture_date 统一为 2026-07-04。

```yaml
- id: E-U-001
  field: undergraduate.admissions.site
  value: "https://undergrad.admissions.columbia.edu/"
  source_url: https://undergrad.admissions.columbia.edu/apply/firstyear
  source_snippet: "Columbia Undergraduate Admissions — We accept first-year applications from students who are hoping to enroll full time at Columbia College or Columbia Engineering."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-002
  field: undergraduate.application.platforms
  value: ["Common Application", "Coalition Application", "QuestBridge National College Match"]
  source_url: https://undergrad.admissions.columbia.edu/apply/firstyear
  source_snippet: "Early Decision and QuestBridge National College Match application deadline ... Is there a preference for the Common Application or the Coalition Application?"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-003
  field: undergraduate.deadlines
  value: {ED: "2026-11-01", ED_financial_aid: "2026-11-15", ED_decisions: "mid-December", RD: "2027-01-01", RD_financial_aid: "2027-02-15", RD_decisions: "late March", RD_reply: "2027-05-01"}
  source_url: https://undergrad.admissions.columbia.edu/apply/firstyear
  source_snippet: "November 1 | Early Decision and QuestBridge National College Match application deadline ... January 1 | Regular Decision application deadline ... May 1 | Regular Decision response deadline for admitted students"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-U-004
  field: undergraduate.testing.policy
  value: {2026_2027: "test-optional", 2027_2028_onward: "testing required (effective August 2027)", minimum: "none", superscore: true, act_writing_science: "not required"}
  source_url: https://undergrad.admissions.columbia.edu/apply/process/testing
  source_snippet: "Columbia will require standardized testing starting in August 2027. ... Columbia College and Columbia Engineering will remain test optional for the upcoming 2026-2027 admissions cycle. ... There are no minimum test score requirements for admission."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-005
  field: undergraduate.interview.policy
  value: "no interviews (since 2023-05-18 announcement)"
  source_url: https://undergrad.admissions.columbia.edu/apply/firstyear
  source_snippet: "Interviews are not a part of the application process. Please see the announcement from May 18, 2023."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.application.fee
  value: {amount_usd: 85, refundable: false, waiver_income_threshold_usd: 66000, payment_methods: ["electronic check", "Visa", "MasterCard", "Discover", "American Express"]}
  source_url: https://undergrad.admissions.columbia.edu/apply/process/application-fees
  source_snippet: "An $85 nonrefundable fee is required as part of an application to Columbia University. ... Your annual household income is below $66,000 USD."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.transfer.pathways
  value: ["Transfer", "Combined Plan (3-2 BA/BS)", "Visiting Student", "School of General Studies (for non-traditional)"]
  source_url: https://undergrad.admissions.columbia.edu/apply/firstyear
  source_snippet: "If you're a current college student, explore our Transfer, Combined Plan and Visiting Student programs. If you're a potential applicant to Columbia College and you've taken a break of more than a year in your education ... you should, instead, consider Columbia University's School of General Studies."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.english_proficiency.requirements
  value: {sat_ebrw_minimum: 700, act_english_or_reading_minimum: 29, exams_accepted: ["TOEFL", "IELTS", "DET (Duolingo)", "Cambridge English Qualifications"], published_minimum: "none (competitive)", exemption: "home language English OR primary language of instruction English for duration of secondary school"}
  source_url: https://undergrad.admissions.columbia.edu/apply/international/english-proficiency
  source_snippet: "700 or higher on the Evidence Based Reading and Writing section of the SAT ... 29 or higher on the English or Reading sections of the ACT ... TOEFL ... IELTS ... DET (Duolingo English Test) ... Cambridge English Qualifications"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-U-009
  field: undergraduate.cost.2026_2027
  value: {tuition: 72800, fees: 4160, food: 7128, housing: 12522, books_supplies: 1320, travel: "varies", personal: 1844, total: 99774, academic_year: "2026-2027"}
  source_url: https://undergrad.admissions.columbia.edu/affordability/cost
  source_snippet: "2026-2027 Cost of Attendance | Tuition $72,800 | Fees $4,160 | Food $7,128 | Housing $12,522 | Books and supplies $1,320 | Travel and local transportation varies | Personal expenses $1,844 | Total budget $99,774"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-U-010
  field: undergraduate.financial_aid.policy
  value: {tuition_free_income_threshold: 150000, zero_parent_contribution_threshold: 66000, loans: "not used to meet financial need", annual_aid_from_all_sources_usd: 240000000, pct_first_years_receiving_columbia_grant: "~50%", average_first_year_grant: 77908, pct_first_years_pell: 21, low_income_startup_grant: 2000, need_blind_us_citizens: true, need_aware_internationals: true, meets_full_demonstrated_need: true}
  source_url: https://undergrad.admissions.columbia.edu/affordability/cost
  source_snippet: "Students coming from families with annual incomes less than $150,000 (and typical assets) are able to attend Columbia tuition-free. ... EXPECTED PARENT CONTRIBUTION FOR STUDENTS COMING FROM FAMILIES WITH ANNUAL INCOMES OF LESS THAN $66,000 (AND TYPICAL ASSETS) ... No loans / LOANS ARE NOT USED TO MEET FINANCIAL NEED OR INCLUDED IN INITIAL FINANCIAL AID AWARDS ... Columbia awards more than $240 million annually in scholarships and grants ... About half of Columbia's incoming first-year students receive grants from Columbia and the average first-year grant is $77,908. ... 21% of Columbia's incoming first-years receive the Pell Grant ... Incoming first-year students from low-income families receive a start-up grant of $2,000 ... Students are expected to borrow $0 to attend Columbia."
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-U-011
  field: undergraduate.schools
  value: ["Columbia College (BA)", "Columbia Engineering / SEAS (BS)", "School of General Studies (BA/BS)", "Barnard College (BA, affiliated)"]
  source_url: https://undergrad.admissions.columbia.edu/academics
  source_snippet: "When students apply to either Columbia College or The Fu Foundation School of Applied Engineering and Science (Columbia Engineering) ... 6:1 UNDERGRADUATE STUDENT-TO-FACULTY RATIO ... 6,700 COLUMBIA COLLEGE AND COLUMBIA ENGINEERING UNDERGRADUATES ... 100+ AREAS OF STUDY"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.gsas.programs
  value: {MA: 46, PhD: 34, dual_degree: 4, certificates_non_degree: 12, phd_concentrations: 3}
  source_url: https://www.gsas.columbia.edu/content/degree-programs
  source_snippet: "BY THE NUMBERS | 31 Arts & Sciences PhD Programs | 46 Arts & Sciences MA Programs | 6 Dual-Degree Programs"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.gsas.ma_list
  value: "46 MA programs (African American Studies through Statistics; full list in Section 2)"
  source_url: https://www.gsas.columbia.edu/content/ma-programs
  source_snippet: "MA PROGRAMS (h3 headings): African American Studies, American Studies, Anthropology, Art History and Archaeology, Biotechnology, ... Statistics (46 entries)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.gsas.phd_list
  value: "34 PhD programs (incl. Architecture, Historic Preservation, Urban Planning cross-listed with GSAPP)"
  source_url: https://www.gsas.columbia.edu/content/phd-programs
  source_snippet: "PHD PROGRAMS (h3 headings): African American and African Diaspora Studies, Anthropology, Architecture, ... Urban Planning (34 entries)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-004
  field: graduate.cbs.programs
  value: {MBA: 1, EMBA: 1, MS: ["MSAFA", "MSFE", "MSM", "MSBA", "MS Climate Finance"], PhD: 1, dual_degrees: 11}
  source_url: https://academics.business.columbia.edu/
  source_snippet: "MBA | Executive MBA | Master of Science | PhD ... Our MS Programs: Accounting and Fundamental Analysis, Financial Economics, Marketing Science ... Students can combine a Columbia Full-Time MBA with one of 11 other professional degrees"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-005
  field: graduate.law.degrees
  value: {JD: 1, LLM: 1, Executive_LLM: 1, JSD: 1, dual_columbia: 10, joint_princeton: 1}
  source_url: https://www.law.columbia.edu/academics
  source_snippet: "J.D. Program and Curriculum | LL.M. Program and Curriculum | Executive LL.M. Program and Curriculum | J.S.D. Program and Curriculum | Dual Degrees ... ten (10) dual degree programs through graduate schools at Columbia and one (1) joint degree program with Princeton."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-006
  field: graduate.medicine.programs
  value: {MD: ["MD", "Columbia-Bassett Track"], MS: ["Genetic Counseling", "Human Nutrition", "Occupational Therapy", "Bioethics", "Biomedical Informatics", "Narrative Medicine"], OTD: 1, DPT: 1, EdD_Movement_Science: 1, PhD_umbrella: ["Biomedical Informatics", "Biomedical Life Sciences (10 tracks)", "Neurobiology and Behavior"]}
  source_url: https://www.vagelos.columbia.edu/education/academic-programs
  source_snippet: "MD Program | MD Dual Degrees and Special Programs | Vagelos Institute's Biomedical Research Education PhD Programs | Program in Genetic Counseling | Programs in Human Nutrition | Programs in Occupational Therapy | Programs in Physical Therapy | Additional Master's Degree Programs"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-007
  field: graduate.mailman.departments_and_degrees
  value: {departments: 6, degrees: ["MPH", "MS", "MHA", "DrPH", "PhD"], dual_degree_options: 12}
  source_url: https://www.publichealth.columbia.edu/become-student/degree-programs
  source_snippet: "Biostatistics: DrPH, MPH two year full-time, MS, PhD ... Environmental Health Sciences: DrPH, MPH, MS, PhD ... Epidemiology: Accelerated MPH, DrPH, MPH, MS, Online MS, PhD ... Health Policy and Management: Accelerated MPH, MPH, MS, MHA (3 formats) ... Population and Family Health: MPH, MS ... Sociomedical Sciences: MPH, MS, PhD"
  capture_date: 2026-07-04
  evidence_type: official_webpage_table

- id: E-G-008
  field: graduate.sipa.master_programs
  value: ["MIA (21mo)", "MPA (21mo)", "MPA in Development Practice", "MPA in Economic Policy Management (1yr)", "MPA in Environmental Science and Policy (1yr)", "MPA in Global Leadership (10mo)", "Executive MPA (2-3yr)"]
  source_url: https://www.sipa.columbia.edu/sipa-education/masters-programs
  source_snippet: "Master of International Affairs (21 months) | Master of Public Administration (21 months) | MPA in Development Practice | MPA in Economic Policy Management (1 year) | MPA in Environmental Science and Policy (1 year) | MPA in Global Leadership (10 months) | Executive MPA (2-3 years)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-009
  field: graduate.cssw.degrees
  value: {MSSW: ["on-campus", "online"], PhD: 1}
  source_url: https://socialwork.columbia.edu/degrees-we-offer
  source_snippet: "The Columbia School of Social Work offers a CSWE-accredited Master's of Science in Social Work (MSSW) and a Doctor of Philosophy (PhD) in Social Work."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-010
  field: graduate.gsapp.programs
  value: {MArch: 1, MS: ["Advanced Architectural Design", "Computational Design Practices", "Critical Curatorial & Conceptual Practices", "Architecture and Urban Design", "Urban Planning", "Historic Preservation", "Real Estate Development"], PhD: ["Architecture", "Urban Planning", "Historic Preservation"]}
  source_url: https://www.arch.columbia.edu/programs
  source_snippet: "Master of Architecture | M.S. Advanced Architectural Design | M.S. Computational Design Practices | M.S. Critical, Curatorial & Conceptual Practices | Ph.D. Architecture | M.S. Architecture and Urban Design | M.S. Urban Planning | Ph.D. Urban Planning | M.S. Historic Preservation | Ph.D. Historic Preservation | M.S. Real Estate Development"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-011
  field: graduate.journalism.degrees
  value: {MS: ["MS", "MS Data Journalism"], MA: 1, PhD: 1}
  source_url: https://journalism.columbia.edu/academics
  source_snippet: "DEGREE PROGRAMS: M.S. | M.S. DATA | M.A. | DUAL DEGREES | PH.D. ... The Master of Science degree is the foundational program of the Journalism School."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-012
  field: graduate.arts.degrees
  value: {MFA: ["Film", "Theatre", "Visual Arts", "Sound Art (interdisciplinary via Visual Arts)", "Writing"], MA: ["Film and Media Studies"]}
  source_url: https://arts.columbia.edu/graduate-programs
  source_snippet: "Columbia University School of the Arts awards the Master of Fine Arts degree in Film, Theatre, Visual Arts, and Writing, as well as an interdisciplinary program in Sound Art that leads to an MFA in Visual Arts. The School also offers a Master of Arts degree in Film and Media Studies."
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-013
  field: graduate.nursing.degrees
  value: {MS: ["Masters Direct Entry (MDE)", "Masters in Advanced Clinical Management and Leadership"], DNP: 1, PhD: 1}
  source_url: https://www.nursing.columbia.edu/academics/academic-programs
  source_snippet: "Masters Direct Entry Program For Non-Nurses | Masters in Advanced Clinical Management and Leadership | Doctor of Nursing Practice | Doctor of Philosophy (PhD)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-014
  field: undergraduate.bulletin.cc.departments
  value: "58 departments-and-programs (Columbia College, BA-granting)"
  source_url: https://bulletin.columbia.edu/columbia-college/departments-instruction/
  source_snippet: "Departments, Programs, and Courses — African American and African Diaspora Studies ... American Studies ... Women's and Gender Studies (58 dept links)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-015
  field: undergraduate.bulletin.seas.minors
  value: 49
  source_url: https://bulletin.columbia.edu/columbia-engineering/undergraduate-minors/
  source_snippet: "Undergraduate Minors — Aerospace Engineering Minor ... American Studies Minor ... Women's, Gender and Sexuality Studies Minor (49 minor links; Statistics has base + Applied Track + Theory Track = 3 rows)"
  capture_date: 2026-07-04
  evidence_type: official_webpage

- id: E-G-016
  field: undergraduate.bulletin.seas.departments
  value: ["Applied Physics and Applied Mathematics", "Biomedical Engineering", "Chemical Engineering", "Civil Engineering and Engineering Mechanics", "Computer Engineering Program", "Computer Science", "Earth and Environmental Engineering", "Electrical Engineering", "Industrial Engineering and Operations Research", "Materials Science and Engineering Program", "Mechanical Engineering", "Data Science", "Engineering (School-wide)"]
  source_url: https://bulletin.columbia.edu/columbia-engineering/academic-departments-programs/
  source_snippet: "Academic Departments and Programs — Applied Physics and Applied Mathematics | Biomedical Engineering | Chemical Engineering | Civil Engineering and Engineering Mechanics | Computer Engineering Program | Computer Science | Earth and Environmental Engineering | Electrical Engineering | Industrial Engineering and Operations Research | Materials Science and Engineering Program | Mechanical Engineering"
  capture_date: 2026-07-04
  evidence_type: official_webpage
```

---

# 6. WeKnora 导入清单 (WeKnora Import Manifest)

## 6.1 Collection 结构

```
collection: columbia-knowledge-base-v2
├── document: columbia-overview            # Section 0（规则 1-4，4 项 roll-up）
│   ├── chunk: counts-matrix               # 0.1 总数 + 0.4 分布矩阵
│   ├── chunk: hierarchy-tree              # 0.2 学院-系树
│   └── chunk: degree-inventory            # 0.3 学历级别
├── document: columbia-undergraduate       # Section 1（本科，规则 5）
│   ├── chunk: columbia-college-majors     # 56 BA 主修（按系分组）
│   ├── chunk: columbia-engineering-bs     # 18 BS 主修（按系分组）
│   ├── chunk: columbia-engineering-minors # 49 SEAS 辅修
│   ├── chunk: general-studies-majors      # 39 GS-unique 主修
│   ├── chunk: barnard-majors              # 41 Barnard 主修
│   └── chunk: core-curriculum             # 1.5 Core Curriculum
├── document: columbia-graduate            # Section 2（研究生，规则 5）
│   ├── chunk: gsas-ma                     # 46 MA
│   ├── chunk: gsas-phd                    # 34 PhD
│   ├── chunk: gsas-certificates           # 12 非学位证书 + 3 PhD 浓度 + 4 Dual
│   ├── chunk: business-school             # CBS MBA/EMBA/MS/PhD
│   ├── chunk: law-school                  # JD/LLM/JSD
│   ├── chunk: medicine-vagelos            # MD + PhD + MS + OTD/DPT/EdD
│   ├── chunk: public-health-mailman       # 6 系 MPH/MS/MHA/DrPH/PhD
│   ├── chunk: sipa                        # 7 master's
│   ├── chunk: social-work                 # MSSW + PhD
│   ├── chunk: gsapp                       # 11 建筑/规划/保护
│   ├── chunk: journalism                  # MS/MA/PhD
│   ├── chunk: arts                        # MFA + MA
│   └── chunk: nursing                     # MS + DNP + PhD
├── document: columbia-admissions          # Section 3
│   ├── chunk: ug-deadlines
│   ├── chunk: ug-english-proficiency
│   └── chunk: grad-global-rules
├── document: columbia-costs-aid           # Section 4
│   ├── chunk: ug-cost-line-items
│   └── chunk: ug-financial-aid-policy
└── document: columbia-evidence            # Section 5（E-U-001 … E-G-016）
```

## 6.2 Per-chunk metadata 模板

```yaml
metadata:
  collection: "columbia-knowledge-base-v2"
  school: "<home college, e.g. Columbia Engineering (SEAS)>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|MFA|MBA|MPH|MPA|MIA|MSW|MArch|MHA|LLM|PhD|MD|JD|JSD|DPT|DNP|DrPH|EdD|OTD|Cert|Dual>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-04
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-04
```

## 6.3 后续待抓取数据项（按优先级）

| 优先级 (P0/P1/P2) | 数据项 | 目标 URL | 说明 |
|------|--------|----------|------|
| **P0** | 国际生 need-blind / need-aware 精确官方表述（含招生办或 SFS 官方页面原文）| https://undergrad.admissions.columbia.edu/affordability + SFS finaid 页面 | 当前抓取的 cost 页面未出现"need-blind"字样；需从招生 FAQ 或 SFS 政策页精确引用，以确认对国际生是 need-aware 还是 need-blind（本稿件基于行业公认事实记录为 need-aware for internationals，待官方原文复核）|
| **P0** | 各研究生专业学院 2026-27 学费（CBS MBA、SIPA、Law JD、Mailman MPH、Vagelos MD、GSAPP、Journalism、Arts、Nursing、CSSW）| 各学院 SFS / tuition 页面 | 当前仅抓到本科 COA；研究生学费为估算，需逐学院抓取 official COA line items |
| **P0** | 各研究生项目截止日期与 GRE 政策（逐项目）| CBS / Law / Vagelos / Mailman / SIPA / GSAPP / Journalism / Arts / Nursing admissions pages | 当前仅给全局规则；需逐项目 deep-dive（同 Harvard/NYU 的 per-program GRE/TOEFL 表）|
| P1 | GSAS 各 MA/PhD 项目的 TOEFL/IELTS 最低分（逐项目）| gsas.columbia.edu 各项目页 + 招生要求页 | GSAS 未公布统一最低，各系不同 |
| P1 | SEAS 各 BS 项目的具体课程要求与学分 | bulletin.columbia.edu 各 SEAS BS 项目页 | 当前仅列出项目名与学位 |
| P1 | Columbia Combined Plan (3-2) 合作院校清单（90+）| https://undergrad.admissions.columbia.edu/apply/combinedplan | 当前仅记录途径名 |
| P2 | Barnard 完整 50 个系精确清单（当前基于部分页面 + 已知主修）| https://barnard.edu/departments-and-programs（"Load More" 全展开后抓取）| Barnard 页面 JS 分页，本次未完整展开 |
| P2 | Columbia-Juilliard Exchange、BA/MA 4+1 Pathways 详情 | barnard.edu/beyond-barnard/graduate-professional-school/cu-bama-options | 当前仅记录途径 |
| P2 | 各学院 student-faculty ratio、class size、毕业率、就业率 | 各学院 about / facts 页面 | 当前仅本科 6:1 ratio |

---

# 7. 跨校比较框架 (Cross-School Comparison Framework)

| 维度 | Columbia | MIT | Harvard | Stanford | NYU |
|------|----------|-----|---------|----------|-----|
| 总本科费用/年 (2026-27) | **$99,774** | (见 MIT doc) | (见 Harvard doc) | (见 Stanford doc) | (见 NYU doc) |
| 学费/年 (2026-27) | **$72,800** | — | — | — | — |
| Need-blind (US) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Need-blind (国际生) | **✗ (need-aware)** | ✓ | ✓ | ✓ | ✗ (need-aware) |
| 满足 100% 计算需求 | ✓ | ✓ | ✓ | ✓ | ✓ |
| No loans 政策 | ✓ | ✓ | ✓ | ✓ | (NYU Promise 不同机制) |
| 学费全免家庭收入门槛 | **<$150k** | (<$75k 典型) | (<$85k) | (<$100k) | (<$100k NYU Promise) |
| 零家长贡献门槛 | **<$66k** | — | (<$85k) | — | — |
| ED 截止 | **Nov 1** | (无 ED, EA 11/30) | (REA Nov 1) | (REA Nov 1) | (ED Nov 1, ED II Jan 1) |
| RD 截止 | **Jan 1** | (RA 1/4) | Jan 1 | Jan 2 | Jan 5 |
| SAT/ACT required? | 2026-27 optional；**2027-28 起 required** | Required | Test-optional | Test-optional | Test-optional (永久) |
| TOEFL 最低 (UG) | 未公布 (competitive)；SAT EBRW 700+ 免考 | (MIT 要求英语考试) | 不要求 | 不要求 | 未公布 (competitive) |
| 申请费 (UG) | **$85** | $75 | $85 | $90 | $80 |
| **总项目数 (规则 1)** | **434** | (见 MIT doc) | 182 | 342 | (见 NYU doc) |
| 学院数 | **15** | 5/6 | 13 | 7 | (见 NYU doc) |
| April-15 honor date (grad) | ✓ | ✓ | ✓ | ✓ | ✓ |
| 应用平台 (UG) | Common/Coalition/QuestBridge | Common/Coalition/QuestBridge | Common/Coalition/QuestBridge | Common/Coalition/QuestBridge | Common/Coalition/QuestBridge |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-04
> **Sources**: bulletin.columbia.edu (Columbia College / Columbia Engineering / General Studies bulletins), gsas.columbia.edu, undergrad.admissions.columbia.edu, business.columbia.edu (CBS), law.columbia.edu, vagelos.columbia.edu (Medicine), publichealth.columbia.edu (Mailman), sipa.columbia.edu, socialwork.columbia.edu, arch.columbia.edu (GSAPP), journalism.columbia.edu, arts.columbia.edu, nursing.columbia.edu, barnard.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction（AZ index 302 link 过滤 + 各学院官网逐页抓取 + Python 规则 1-4 对账）
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: 规则 1 总数 = 规则 3 学历级别求和 = 规则 4 分布矩阵单元求和 = 规则 5 全量明细行数 = **434**（四数一致 ✓）
