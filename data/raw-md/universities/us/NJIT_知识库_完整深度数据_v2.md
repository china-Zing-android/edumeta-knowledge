# New Jersey Institute of Technology (NJIT) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless) + Elasticsearch API at `https://www.njit.edu/search-api/corporate/degree/_search`
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/B.Arch./B.S.E.T.) | 55 |
| 本科 B.S.E.T. (Bachelor of Science in Engineering Technology) | 1 |
| 研究生学位项目 (MA/MS/M.Arch./MBA/Ph.D.) | 84 |
| 研究生高级证书 (Graduate Certificate) | 70 |
| **学位项目总计 (UG + Grad)** | **210** |
| 学院 / 独立系所总数 | 6 colleges + 1 Honors College |

> 注: NJIT 官方表述 "more than 125 undergraduate and graduate degree programs"。本数据集 (210 entries) 包含所有 B.S.E.T./Bachelor's/Master's/Doctoral/Graduate Certificate 学位项目，以及在线版本、双学位版本（如 B.S./M.S. 加速路径）和多个专业方向（如 Materials Science and Engineering 的 Materials Science Option 与 Materials Engineering Option）。University-wide program count (excluding certificates): 140 programs.

### 0.2 学院 / 系层级结构

```
NJIT (New Jersey Institute of Technology)
│
├── Albert Dorman Honors College                          [学院 / Interdisciplinary]
│
├── Newark College of Engineering (NCE)                   [学院]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical and Materials Engineering                 [系]
│   ├── Civil and Environmental Engineering                [系]
│   ├── Electrical and Computer Engineering               [系]
│   ├── Engineering Technology                            [系]
│   └── Mechanical and Industrial Engineering             [系]
│
├── Hillier College of Architecture and Design            [学院]
│   ├── Architecture                                      [系]
│   └── Art + Design                                      [系]
│
├── Ying Wu College of Computing (YWCC)                   [学院]
│   ├── Computer Science                                  [系]
│   └── Informatics                                       [系]
│
├── Jordan Hu College of Science and Liberal Arts         [学院]
│   ├── Biological Sciences                               [系]
│   ├── Chemistry and Environmental Science               [系]
│   ├── History                                           [系]
│   ├── Humanities (and Social Sciences)                  [系]
│   ├── Mathematical Sciences                             [系]
│   ├── Physics                                           [系]
│   └── Theatre Arts and Technology Program               [系]
│
└── Martin Tuchman School of Management                   [学院]
    └── Management                                        [系]
```

> Note: NJIT officially states "six professional schools and colleges" — the six are: (1) Newark College of Engineering, (2) Hillier College of Architecture and Design, (3) Ying Wu College of Computing, (4) Jordan Hu College of Science and Liberal Arts, (5) Martin Tuchman School of Management, plus (6) Albert Dorman Honors College. The "six schools/colleges" count from `njit.edu/about` includes Honors as one of the six.

### 0.3 学历级别明细

| 学位缩写 (official) | 全称 | 层级 | 本项目数量 | canonical 映射 |
|---------|------|------|-----------|---------------|
| B.S.E.T. | Bachelor of Science in Engineering Technology | 本科 | 1 | B.S.E.T. |
| B.A. | Bachelor of Arts | 本科 | (含在 Bachelor's 内) | BA |
| B.S. | Bachelor of Science | 本科 | (含在 Bachelor's 内) | BS |
| B.Arch. | Bachelor of Architecture | 本科 | (含在 Bachelor's 内) | B.Arch. (sub-degree) |
| M.A. | Master of Arts | 研究生 | (含在 Master's 内) | MA |
| M.S. | Master of Science | 研究生 | (含在 Master's 内) | MS |
| M.Arch. | Master of Architecture | 研究生 | (含在 Master's 内) | M.Arch. (sub-degree) |
| MBA | Master of Business Administration | 研究生 | (含在 Master's 内) | MBA |
| Ph.D. | Doctor of Philosophy | 研究生 | 20 | PhD |
| Graduate Certificate | Graduate Certificate / Advanced Certificate | 研究生 | 70 | Adv Cert |

注: NJIT 同时颁发 MS、MA、M.Arch.、MBA、Ph.D. 及 Graduate Certificate。源数据中 Bachelor's 类目共 55 个独立学位路径（包含在线版本）。

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS/BA (含B.Arch.) | B.S.E.T. | MS/MA/M.Arch./MBA | PhD | Adv Cert | 合计 |
|------------|-------------------|----------|--------------------|-----|----------|------|
| Newark College of Engineering | 18 | 1 | 26 | 10 | 18 | 73 |
| Hillier College of Architecture and Design | 5 | 0 | 4 | 1 | 5 | 15 |
| Ying Wu College of Computing | 8 | 0 | 16 | 2 | 20 | 46 |
| Jordan Hu College of Science and Liberal Arts | 15 | 0 | 14 | 6 | 13 | 48 |
| Martin Tuchman School of Management | 9 | 0 | 4 | 1 | 12 | 26 |
| (跨学院 / 跨系) | 0 | 0 | 0 | 0 | 2 | 2 |
| **合计** | **55** | **1** | **64** | **20** | **70** | **210** |

> Reconciliation: 55 + 1 + 64 + 20 + 70 = 210 = rule-1 total = sum of program list below. ✓

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

NJIT 提供本科教育涵盖 6 个学院中的 5 个（Albert Dorman Honors College 跨学院招收优秀学生）。本科共 **56 个学位路径** (含 B.S./B.A./B.Arch./B.S.E.T.)。学院-系层级见 Section 0.2。

### 1.2 本科专业 — 按 学院 > 系 > 学位级别 分组

### 1.2 本科专业 — 按 学院 > 系 > 学位级别 分组

#### Newark College of Engineering

##### Department of Biomedical Engineering
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Biomedical Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/biomedical/bs/> |

##### Department of Chemical and Materials Engineering
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Chemical Engineering | <https://catalog.njit.edu/undergraduate/newark-college-engineering/chemical-materials-engineering/bs/> |
| 2 | B.S. Materials Engineering | <https://catalog.njit.edu/undergraduate/newark-college-engineering/chemical-materials-engineering/cme-bs/> |

##### Department of Civil and Environmental Engineering
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Civil Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/civil-environmental/civil-engineering-bs/> |

##### Department of Electrical and Computer Engineering
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S.E.T. Computer Technology | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/computer-engineering-bs/> |
| 2 | B.S. Computer Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/computer-engineering-bs/> |
| 3 | B.S. Electrical Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/electrical-engineering-bs/> |

##### Department of Engineering Technology
###### B.S.E.T.

| # | 专业 | URL |
|---|------|-----|
| 1 | Online B.S. in Surveying Engineering Technology (SET) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/saet-sbed/surveying-engineering-technology/> |

##### Department of Engineering Technology
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Concrete Industry Management | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/concrete-industry-management-technology/> |
| 2 | B.S.E.T. Manufacturing Engineering Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/manufacturing-engineering-technology/> |
| 3 | B.S.E.T. Construction Management Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/construction-management-technology/> |
| 4 | B.S.E.T. Electrical and Computer Engineering Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/electrical-computer-engineering-technology/> |
| 5 | B.S.E.T. Mechanical Engineering Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/mechanical-engineering-technology/> |
| 6 | B.S.E.T. Surveying Engineering Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/surveying-engineering-technology/> |
| 7 | B.S.E.T. Technology Education | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/technology-education/> |
| 8 | B.S.E.T. Medical Informatics Technology | <https://catalog.njit.edu/undergraduate/newark-college-engineering/saet-semd/medical-informatics-technology/> |
| 9 | B.S.E.T. Construction Engineering Technology | <http://catalog.njit.edu/undergraduate/newark-college-engineering/technology/construction-engineering-technology/> |

##### Department of Mechanical and Industrial Engineering
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Mechanical Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/mechanical-industrial/mechanical-engineering-bs/> |
| 2 | B.S. Industrial Engineering | <http://catalog.njit.edu/undergraduate/newark-college-engineering/mechanical-industrial/industrial-engineering-bs/> |

#### Hillier College of Architecture and Design

##### Department of Architecture
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Architecture | <http://catalog.njit.edu/undergraduate/architecture-design/architecture/bs/> |
| 2 | Bachelor of Architecture (B.Arch.) | <http://catalog.njit.edu/undergraduate/architecture-design/architecture/barch/> |

##### Department of Art + Design
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.A. Interior Design | <http://catalog.njit.edu/undergraduate/architecture-design/art-design/interior-design-ba/> |
| 2 | B.A. Digital Design | <http://catalog.njit.edu/undergraduate/architecture-design/art-design/digital-design-ba/> |
| 3 | B.S. Industrial Design | <http://catalog.njit.edu/undergraduate/architecture-design/art-design/industrial-design-bs/> |

#### Ying Wu College of Computing

##### Department of Computer Science
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.A. Computer Science | <https://catalog.njit.edu/undergraduate/computing-sciences/computer-science/ba/> |
| 2 | B.S. Data Science (Computing Concentration) | <https://catalog.njit.edu/undergraduate/computing-sciences/data-science/data-science-bs/> |
| 3 | B.S. Computer Science | <http://catalog.njit.edu/undergraduate/computing-sciences/computer-science/bs/> |

##### Department of Informatics
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Business and Information Systems | <http://catalog.njit.edu/undergraduate/computing-sciences/information-systems/business-information-systems-bs/> |
| 2 | B.S. Web Information Systems | <http://catalog.njit.edu/undergraduate/computing-sciences/information-systems/web-information-systems-bs/> |
| 3 | B.S. Human-Computer Interaction | <http://catalog.njit.edu/undergraduate/computing-sciences/information-systems/human-computer-interaction-bs/> |
| 4 | B.A. Information Systems | <http://catalog.njit.edu/undergraduate/computing-sciences/information-systems/ba/> |
| 5 | B.S. Information Technology | <http://catalog.njit.edu/undergraduate/computing-sciences/information-technology/bs/> |

#### Jordan Hu College of Science and Liberal Arts

##### Department of Biological Sciences
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Biology | <http://catalog.njit.edu/undergraduate/science-liberal-arts/biology/bs/> |
| 2 | B.A. Biology | <http://catalog.njit.edu/undergraduate/science-liberal-arts/biology/ba/> |

##### Department of Chemistry and Environmental Science
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Chemistry | <http://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/chemistry-bs/> |
| 2 | B.S. Environmental Science | <http://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/environmental-science-bs/> |
| 3 | B.S. Biochemistry | <http://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/biochemistry-bs/> |
| 4 | B.S. Forensic Science | <https://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/forensic-science-bs/> |

##### Department of History
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.A. Law, Technology and Culture | <http://catalog.njit.edu/undergraduate/science-liberal-arts/history/law-technology-culture-ba/> |
| 2 | B.A. History | <http://catalog.njit.edu/undergraduate/science-liberal-arts/history/ba/> |

##### Department of Humanities
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Communication and Media | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/communication-media-bs/> |
| 2 | B.A. Communication and Media | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/communication-media-ba/> |
| 3 | B.S. Psychology | <> |

##### Department of Mathematical Sciences
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Mathematical Sciences | <http://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences> |
| 2 | B.S. Data Science (Statistics Concentration) | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/data-science-bs/> |

##### Department of Physics
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Applied Physics | <http://catalog.njit.edu/undergraduate/science-liberal-arts/physics/applied-bs/> |

##### Department of Theatre Arts and Technology Program
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.A. Theatre Arts and Technology | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/theatre-arts-technology-ba/> |

#### Martin Tuchman School of Management

##### Department of Management
###### Bachelor's

| # | 专业 | URL |
|---|------|-----|
| 1 | B.S. Marketing | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 2 | B.S. Management Information Systems | <https://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 3 | B.S. Accounting Systems | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 4 | B.S. Innovation and Entrepreneurship | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 5 | Online Accelerated B.S. in Business | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 6 | B.S. Business | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 7 | B.S. Business with AI | <> |
| 8 | B.S. Finance | <http://catalog.njit.edu/undergraduate/management/management/business-bs/> |
| 9 | B.S. Financial Technology | <https://management.njit.edu/sites/management/files/BS%20in%20FinTech%20curriculum%202022-2023.pdf> |


### 1.3 跨学科 / 跨学院本科项目

NJIT 在 catalog 中列出多个双学位 / 加速路径 (Double Major / Accelerated / B.S./M.S.)：

| 项目 | 路径 | 学院 | URL |
|------|------|------|-----|
| Architecture - B.Arch. and Civil Engineering - M.S. | B.S./M.S. | Hillier + NCE | <https://catalog.njit.edu/programs/> |
| Architecture - B.Arch. and Infrastructure Planning - M.I.P. | B.S./M.S. | Hillier | <https://catalog.njit.edu/programs/> |
| Architecture - B.Arch. and Management - M.S. | B.S./M.S. | Hillier + Tuchman | <https://catalog.njit.edu/programs/> |
| Architecture - B.Arch. and Technology - M.B.A. | B.S./M.S. | Hillier + Tuchman | <https://catalog.njit.edu/programs/> |
| Architecture - B.S. and Civil Engineering - M.S. | B.S./M.S. | Hillier + NCE | <https://catalog.njit.edu/programs/> |
| Architecture - B.S. and Infrastructure Planning - M.I.P. | B.S./M.S. | Hillier | <https://catalog.njit.edu/programs/> |
| Architecture - B.S. and Management - M.S. | B.S./M.S. | Hillier + Tuchman | <https://catalog.njit.edu/programs/> |
| Architecture - B.S. and Technology - M.B.A. | B.S./M.S. | Hillier + Tuchman | <https://catalog.njit.edu/programs/> |
| Applied Mathematics and Applied Physics - B.S. | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biology - B.A./D.M.D.,O.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biology - B.A./M.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biology - B.A./Physical Therapy Ph.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biology - B.A./Physician Assistant | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biomedical Engineering - Accelerated B.S. | Accelerated | NCE | <https://catalog.njit.edu/programs/> |
| Biology and Law, Technology and Culture - B.A | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Biology and Mathematical Sciences - B.S. | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Chemistry & Law, Technology and Culture​ - B.S. | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Computer Science and Applied Physics - B.S. | Double Major | YWCC + Jordan Hu | <https://catalog.njit.edu/programs/> |
| Computer Science and Mathematical Sciences, Applied Mathematics - B.S. | Double Major | YWCC + Jordan Hu | <https://catalog.njit.edu/programs/> |
| Computer Science and Mathematical Sciences, Computational Mathematics - B.S. | Double Major | YWCC + Jordan Hu | <https://catalog.njit.edu/programs/> |
| History - B.A./D.P.T. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| History - B.A./J.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| History - B.A./M.D., D.M.D., D.D.S., O.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Information Technology - Accelerated B.S. and J.D. | Accelerated | YWCC | <https://catalog.njit.edu/programs/> |
| Law, Technology and Culture -B.A./J.D | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Mathematical Sciences - B.S./M.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Mathematical Sciences - B.S./M.D., D.M.D., D.D.S., O.D. | Accelerated | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Physics & Law, Technology and Culture - Astronomy Option - B.S. | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Physics & Law, Technology and Culture - Optical Science & Engineering Option​ - B.S. | Double Major | Jordan Hu | <https://catalog.njit.edu/programs/> |
| Science, Technology and Society/Business and Information Systems - B.S. | Double Major | YWCC + Jordan Hu | <https://catalog.njit.edu/programs/> |

> 数据源: <https://catalog.njit.edu/programs/> (Special Degree Options 列)。共 30 个跨学科 / 加速 / 双学位本科项目。

### 1.4 辅修 (Minors) — 完整列表

NJIT 提供以下 academic minors（最少 15 学分，至少 6 学分为高阶课程）。完整政策见 <https://catalog.njit.edu/undergraduate/academic-policies-procedures/academic-minors/>。

**Ying Wu College of Computing (11 minors):**

| # | Minor | URL |
|---|-------|-----|
| 1 | Artificial Intelligence Minor (for DS and CS Majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/data-science/artificial-intelligence-minor-cs-ds-majors/> |
| 2 | Artificial Intelligence Minor (for non-DS and non-CS Majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/data-science/artificial-intelligence-minor-non-cs-ds-majors/> |
| 3 | Computer Science Minor | <https://catalog.njit.edu/undergraduate/computing-sciences/computer-science/minor/> |
| 4 | Data Analytics | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/data-analytics-minor/> |
| 5 | Design of the User Experience Minor | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/human-computer-interaction-minor/> |
| 6 | Business and Information Systems Minor (not for YWCC majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/bis-minor-computing-science-majors/> |
| 7 | Business and Information Systems Minor (for Computing Sciences majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/bis-minor-computing-science-majors/> |
| 8 | Game Development Minor | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/game_development_minor/> |
| 9 | Information Technology Minor (not for YWCC majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/> |
| 10 | Information Technology Minor (for YWCC majors) | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/> |
| 11 | Mobile and Web Minor | <https://catalog.njit.edu/undergraduate/computing-sciences/informatics/> |

**Jordan Hu College of Science and Liberal Arts (21 minors):**

| # | Minor | URL |
|---|-------|-----|
| 1 | Applied Mathematics Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/> |
| 2 | Applied Physics Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/physics/> |
| 3 | Applied Statistics Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/> |
| 4 | Biological Sciences Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/biology/> |
| 5 | Chemistry Minor (not for Chemical Engineering majors) | <https://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/> |
| 6 | Communication Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/communication-minor/> |
| 7 | Computational Mathematics Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/> |
| 8 | Electronic Creative Writing Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/electronic-creative-writing-minor/> |
| 9 | Environmental Science and Policy Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/> |
| 10 | Environmental Studies and Sustainability Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/interdisciplinary-programs/environmental-studies-sustainability-minor/> |
| 11 | Forensic Science Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/chemistry-environmental-science/> |
| 12 | Global Studies Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/global-studies-minor/> |
| 13 | History Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/history/> |
| 14 | Journalism Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/journalism-minor/> |
| 15 | Leadership and Aerospace Studies Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/> |
| 16 | Legal Studies Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/history/> |
| 17 | Literature Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/> |
| 18 | Mathematical Biology Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/> |
| 19 | Mathematics of Finance and Actuarial Science Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/mathematical-sciences/> |
| 20 | Philosophy and Applied Ethics Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/philosophy-applied-ethics-minor/> |
| 21 | Psychology Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/psychology-minor/> |
| 22 | Science, Technology and Society Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/science-technology-society-minor/> |
| 23 | Technology, Gender and Diversity Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/technology-gender-diversity-minor/> |
| 24 | Theatre Arts and Technology Minor | <https://catalog.njit.edu/undergraduate/science-liberal-arts/humanities-and-social-sciences/> |

**Newark College of Engineering (20 minors):**

| # | Minor | URL |
|---|-------|-----|
| 1 | Advanced Building Systems Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 2 | Biomedical Engineering Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/biomedical/> |
| 3 | Biomedical Engineering Technology | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 4 | Climate Change Adaptation and Resilience in Engineering | <https://catalog.njit.edu/undergraduate/newark-college-engineering/civil-environmental/> |
| 5 | Computer Engineering Minor (not for EE or CS majors) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 6 | Computer Engineering Minor (for CS majors) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 7 | Computer Engineering Minor (for EE majors) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 8 | Drones and Robotics | <https://catalog.njit.edu/undergraduate/newark-college-engineering/mechanical-industrial/> |
| 9 | Electrical Engineering Minor (not for EE or CS majors) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 10 | Electrical Engineering Minor (for Computer Engineering majors) | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 11 | Engineering Innovation Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 12 | Environmental Engineering Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/civil-environmental/> |
| 13 | Geosystems Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/civil-environmental/> |
| 14 | Geriatric Engineering Technology Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 15 | Grand Challenges of Engineering Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 16 | Industrial Engineering Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/mechanical-industrial/> |
| 17 | Manufacturing Engineering Technology Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/> |
| 18 | Medical Informatics Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |
| 19 | Materials Engineering Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/chemical-materials-engineering/> |
| 20 | Remote Sensing Minor | <https://catalog.njit.edu/undergraduate/newark-college-engineering/civil-environmental/> |
| 21 | Safety Engineering | <https://catalog.njit.edu/undergraduate/newark-college-engineering/mechanical-industrial/> |
| 22 | Smart Living Technology | <https://catalog.njit.edu/undergraduate/newark-college-engineering/electrical-computer/> |

**Martin Tuchman School of Management (3 minors):**

| # | Minor | URL |
|---|-------|-----|
| 1 | Business Minor | <https://catalog.njit.edu/undergraduate/management/management/business-minor/> |
| 2 | Economics Minor | <https://catalog.njit.edu/undergraduate/management/management/> |
| 3 | Innovation and Entrepreneurship Minor | <https://catalog.njit.edu/undergraduate/management/management/> |

> Minor 总计: 11 + 24 + 22 + 3 = **60 minors** (政策: 至少 15 学分，至少 6 学分为高阶课程，至少 9 学分不与主修重叠，至少 9 学分必须在 NJIT 或 Rutgers-Newark 完成)。

### 1.5 通用 / 校级必修 (General/Institute-wide requirements)

NJIT 一般教育要求 (General Education Requirements) 见 <https://catalog.njit.edu/undergraduate/academic-policies-procedures/general-education-requirements/>。所有本科生必须满足 GEP (General Education Program) 要求，包含人文学科、社会科学、数学、科学等分发要求。具体未在本次抓取范围；建议 P1 跟读。

### 1.6 课程代码 → 专业快速查询

NJIT 不使用 MIT 风格的数字代码 (Course 6, Course 18)，而使用基于系的英文学科名称 + 学位缩写。Department codes 见 catalog 子路径：

- `https://catalog.njit.edu/undergraduate/newark-college-engineering/` (NCE)
- `https://catalog.njit.edu/undergraduate/architecture-design/` (Hillier)
- `https://catalog.njit.edu/undergraduate/computing-sciences/` (YWCC)
- `https://catalog.njit.edu/undergraduate/science-liberal-arts/` (Jordan Hu)
- `https://catalog.njit.edu/undergraduate/management/` (Tuchman)

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 研究生项目 — 按 学院 > 系 > 学位级别 分组

### 2.1 研究生项目 — 按 学院 > 系 > 学位级别 分组

#### Newark College of Engineering

##### Department of Biomedical Engineering
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Biomedical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/biomedical/ms/> |

##### Department of Biomedical Engineering
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Biomedical Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/biomedical/phd/> |

##### Department of Biomedical Engineering
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Online Biomedical Device Development Certificate | <https://catalog.njit.edu/graduate/newark-college-engineering/biomedical/cert/> |

##### Department of Chemical and Materials Engineering
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Pharmaceutical Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/pharmaceutical-ms/> |
| 2 | M.S. Chemical Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/chemical-ms/> |
| 3 | M.S. Materials Science and Engineering (Materials Engineering Option) | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/materials-science-engineering-ms/> |

##### Department of Chemical and Materials Engineering
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Chemical Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/chemical-phd/> |
| 2 | Ph.D. Materials Science and Engineering (Materials Engineering Option) | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/materials-science-engineering-phd/> |

##### Department of Chemical and Materials Engineering
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Pharmaceutical Manufacturing | <> |
| 2 | Certificate in Pharmaceutical Technology | <> |
| 3 | Certificate in Polymers and Plastics | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/polymers-and-plastics-cert/> |
| 4 | Certificate in Pharmaceutical Management | <> |
| 5 | Online Certificate in Data Science for Chemical and Materials Engineers | <https://catalog.njit.edu/graduate/newark-college-engineering/chemical-materials-engineering/data-science-for-chemical-and-materials-engineers-cert/> |

##### Department of Civil and Environmental Engineering
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Critical Infrastructure Systems | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/critical-infrastructure-systems-ms/> |
| 2 | M.S. Civil Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/civil-ms/> |
| 3 | M.S. Transportation | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/transportation-ms/> |
| 4 | M.S. Environmental Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/environmental-ms/> |
| 5 | Online M.S. in Civil Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/civil-ms/> |
| 6 | Online M.S. in Transportation | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/transportation-ms/> |

##### Department of Civil and Environmental Engineering
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Civil Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/civil-phd/> |
| 2 | Ph.D. Environmental Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/environmental-phd/> |
| 3 | Ph.D. Transportation | <http://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/transportation-phd/> |

##### Department of Civil and Environmental Engineering
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Transportation Studies | <> |
| 2 | Online Certificate in Transportation Studies | <https://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/transportation-studies-cert/> |
| 3 | Certificate in Intelligent Transportation Systems | <> |
| 4 | Certificate in Construction Management | <https://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/construction-management-cert/> |
| 5 | Certificate in Environmental Engineering | <> |
| 6 | Certificate in Hydrology and Water Resources Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/hydrology-and-water-resources-engineering-cert/> |
| 7 | Online Certificate in Construction Management | <https://catalog.njit.edu/graduate/newark-college-engineering/civil-environmental/construction-management-cert/> |

##### Department of Electrical and Computer Engineering
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Computer Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/computer-ms/> |
| 2 | M.S. Telecommunications | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/telecommunications-ms/> |
| 3 | M.S. Internet Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/internet-ms/> |
| 4 | M.S. Power and Energy Systems | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/power-energy-systems-ms/> |
| 5 | M.S. Electrical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/electrical-ms/> |
| 6 | Online M.S. in Power & Energy Systems | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/power-energy-systems-ms/> |
| 7 | Online M.S. in Electrical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/electrical-ms/> |

##### Department of Electrical and Computer Engineering
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Computer Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/computer-phd/> |
| 2 | Ph.D. Electrical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/electrical-phd/> |

##### Department of Electrical and Computer Engineering
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Online Wind Power Systems Operations & Maintenance Certificate | <https://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/wind-power-system-operation-and-maintenance-cert/> |
| 2 | Online Certificate in Power Systems Engineering | <https://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/power-systems-engineering-cert/> |
| 3 | Certificate in Power Systems Engineering | <> |
| 4 | Online Wind Power Management Certificate | <https://catalog.njit.edu/graduate/newark-college-engineering/electrical-computer/wind-power-management-cert/> |

##### Department of Mechanical and Industrial Engineering
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Engineering Management | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/engineering-management-ms/> |
| 2 | M.S. Occupational Safety & Health Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/occupational-safety-health-ms/> |
| 3 | Online M.S. in Industrial Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/industrial-ms/> |
| 4 | M.S. Industrial Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/industrial-ms/> |
| 5 | M.S. Pharmaceutical Systems Management | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/pharmaceutical-systems-management-ms/> |
| 6 | Online M.S. in Engineering Management | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/engineering-management-ms/> |
| 7 | M.S. Healthcare Systems Management | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/healthcare-systems-management-ms/> |
| 8 | M.S. Manufacturing Systems Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/manufacturing-systems-ms/> |
| 9 | M.S. Mechanical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/mechanical-ms/> |

##### Department of Mechanical and Industrial Engineering
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Industrial Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/industrial-phd/> |
| 2 | Ph.D. Mechanical Engineering | <http://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/mechanical-phd/> |

##### Department of Mechanical and Industrial Engineering
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Project Management | <> |
| 2 | Online Project Management Certificate | <https://catalog.njit.edu/graduate/newark-college-engineering/mechanical-industrial/project-management-cert/> |
| 3 | Certificate in Supply Chain Engineering | <> |

#### Hillier College of Architecture and Design

##### Department of Architecture
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Architecture | <http://catalog.njit.edu/graduate/architecture-design/architecture/ms/> |
| 2 | Master of Urban Design | <http://catalog.njit.edu/graduate/architecture-design/architecture/infrastructure-planning-masters/> |
| 3 | Master of Architecture (M.Arch.) | <http://catalog.njit.edu/graduate/architecture-design/architecture/march/> |

##### Department of Architecture
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Urban Systems | <http://catalog.njit.edu/graduate/architecture-design/architecture/urban-systems-phd/> |

##### Department of Art + Design
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | Online M.S. in Digital Design | <https://catalog.njit.edu/graduate/architecture-design/architecture/master-of-science-in-digital-design/> |

##### Department of Art + Design
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Game Design and Interactivity Essentials | <https://catalog.njit.edu/graduate/architecture-design/architecture/game-design-and-interactivity-essentials-cert/> |
| 2 | Online Certificate in Animation Essentials | <https://catalog.njit.edu/graduate/architecture-design/architecture/animation-essentials-cert/> |
| 3 | Online Certificate in Digital Arts Essentials | <https://catalog.njit.edu/graduate/architecture-design/architecture/digital-arts-essentials-cert/> |
| 4 | Online Certificate in Game Design and Interactivity Essentials | <https://catalog.njit.edu/graduate/architecture-design/architecture/game-design-and-interactivity-essentials-cert/> |
| 5 | Online Certificate in UI/UX Digital Design Essentials | <https://catalog.njit.edu/graduate/architecture-design/architecture/ui-ux-digital-design-essentials-cert/> |

#### Ying Wu College of Computing

##### Department of Computer Science
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | Online M.S. in Artificial Intelligence | <https://catalog.njit.edu/graduate/computing-sciences/data-science/artificial-intelligence-ms/> |
| 2 | M.S. Computer Science | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/ms/> |
| 3 | M.S. Cybersecurity and Privacy | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/cyber-security-privacy-ms/> |
| 4 | Online M.S. in Computer Science | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/ms/> |
| 5 | M.S. Data Science (Computing Concentration) | <> |
| 6 | M.S. Software Engineering | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/software-engineering-ms/> |
| 7 | Online M.S. in Cybersecurity & Privacy | <https://catalog.njit.edu/graduate/computing-sciences/computer-science/cyber-security-privacy-ms/index.html> |
| 8 | M.S. Cybersecurity and Privacy - Professional Science Master's (PSM) Cyber Defense Option | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/cyber-security-privacy-ms/> |
| 9 | Online M.S. in Data Science | <https://catalog.njit.edu/graduate/computing-sciences/data-science/data-science-ms/> |

##### Department of Computer Science
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Computer Science | <http://catalog.njit.edu/graduate/computing-sciences/computer-science/phd/> |

##### Department of Computer Science
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Online Certificate in Software Engineering, Analysis, and Design | <https://catalog.njit.edu/graduate/computing-sciences/computer-science/software-engr-analysis-design-cert/> |
| 2 | Online Hyperscale Computing Certificate | <https://catalog.njit.edu/graduate/computing-sciences/computer-science/hyperscale-computing-cert/> |
| 3 | Certificate in Software Engineering, Analysis, and Design | <> |
| 4 | Online Certificate in Foundations of Cybersecurity | <https://catalog.njit.edu/graduate/computing-sciences/computer-science/foundations-of-cybersecurity-cert/> |
| 5 | Certificate in Big Data Essentials | <https://catalog.njit.edu/graduate/computing-sciences/data-science/big-data-essentials-cert/> |
| 6 | Online Certificate in Computer Science | <https://catalog.njit.edu/graduate/computing-sciences/computer-science/computer-science-cert/> |
| 7 | Online Artificial Intelligence Certificate | <https://catalog.njit.edu/graduate/computing-sciences/data-science/artificial-intelligence-cert/> |
| 8 | Online Certificate in Big Data Essentials | <https://catalog.njit.edu/graduate/computing-sciences/data-science/big-data-essentials-cert/> |

##### Department of Informatics
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | Online M.S. in Business and Information Systems | <http://catalog.njit.edu/graduate/computing-sciences/information-systems/business-information-systems-ms/index.html> |
| 2 | M.S. Information Systems | <http://catalog.njit.edu/graduate/computing-sciences/information-systems/ms/> |
| 3 | M.S. Information Systems — Professional Science Master's (PSM) Professional Management Option | <> |
| 4 | M.S. Business and Information Systems | <http://catalog.njit.edu/graduate/computing-sciences/information-systems/business-information-systems-ms/index.html> |
| 5 | Online M.S. in Information Systems | <http://catalog.njit.edu/graduate/computing-sciences/information-systems/ms/> |
| 6 | Online M.S. in IT Administration and Security | <http://catalog.njit.edu/graduate/computing-sciences/information-technology/administration-security-ms/> |
| 7 | M.S. Information Technology Administration and Security | <http://catalog.njit.edu/graduate/computing-sciences/information-technology/administration-security-ms/> |

##### Department of Informatics
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Information Systems | <http://catalog.njit.edu/graduate/computing-sciences/information-systems/phd/> |

##### Department of Informatics
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Network Security and Information Assurance | <> |
| 2 | Certificate in Information Security | <> |
| 3 | Online Certificate in IT Administration | <https://catalog.njit.edu/graduate/computing-sciences/informatics/it-administration-cert/> |
| 4 | Online Certificate in Data Mining | <https://catalog.njit.edu/graduate/computing-sciences/data-science/data-mining-cert/> |
| 5 | Certificate in Web Systems Development | <> |
| 6 | Online Certificate in Business and Information Systems Implementation | <https://catalog.njit.edu/graduate/computing-sciences/informatics/business-information-systems-cert/> |
| 7 | Certificate in IT Administration | <> |
| 8 | Certificate in Data Mining | <https://catalog.njit.edu/graduate/computing-sciences/data-science/data-mining-cert/> |
| 9 | Online Network Security and Information Assurance Certificate | <https://catalog.njit.edu/graduate/computing-sciences/informatics/network-security-and-information-assurance-cert/> |
| 10 | Online Information Security Certificate | <https://catalog.njit.edu/graduate/computing-sciences/informatics/information-security-cert/> |
| 11 | Certificate in Business and Information Systems Implementation | <https://catalog.njit.edu/graduate/computing-sciences/informatics/business-information-systems-cert/> |
| 12 | Certificate in Data Visualization | <https://catalog.njit.edu/graduate/computing-sciences/data-science/data-visualization-cert/> |

#### Jordan Hu College of Science and Liberal Arts

##### Department of Biological Sciences
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Biology of Health | <https://catalog.njit.edu/graduate/science-liberal-arts/biology/biology-of-health-ms/> |
| 2 | M.S. Biology | <http://catalog.njit.edu/graduate/science-liberal-arts/biology/ms/> |

##### Department of Biological Sciences
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Biology | <http://catalog.njit.edu/graduate/science-liberal-arts/biology/phd/> |

##### Department of Biological Sciences
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Neuroscience | <https://catalog.njit.edu/graduate/science-liberal-arts/biology/neuroscience-cert> |

##### Department of Chemistry and Environmental Science
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Environmental Science | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/environmental-science-ms/> |
| 2 | Professional Science Master’s Cell and Gene Therapy Sciences Option in MS Pharmaceutical Chemistry | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/pharmaceutical-chemistry-ms/> |
| 3 | M.S. Pharmaceutical Chemistry | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/pharmaceutical-chemistry-ms/> |
| 4 | M.S. Chemistry | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/chemistry-ms/> |

##### Department of Chemistry and Environmental Science
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Chemistry | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/chemistry-phd/> |
| 2 | Ph.D. Environmental Science | <http://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/environmental-science-phd/> |

##### Department of Chemistry and Environmental Science
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Environmental Science and Engineering | <https://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/environmental-science-engineering-cert/> |
| 2 | Certificate in Environmental Science | <https://www.njit.edu/graduatestudies/degree-programs/graduatecertificates/environmental-science-cert/> |
| 3 | Certificate in Cell & Gene Therapy Sciences | <https://catalog.njit.edu/graduate/science-liberal-arts/chemistry-environmental-science/cell-and-gene-therapy-sciences-cert/> |

##### Department of History
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.A. History | <http://catalog.njit.edu/graduate/science-liberal-arts/history/ms/> |

##### Department of Humanities
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Applied Science | <> |

##### Department of Humanities
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Digital Marketing Design Essentials | <> |
| 2 | Certificate in Technical Communication Essentials | <> |
| 3 | Certificate in User Experience Essentials | <> |
| 4 | Certificate in Instructional Design, Evaluation, and Assessment | <> |
| 5 | Certificate in Social Media Essentials | <> |
| 6 | Certificate in Applied Science | <> |

##### Department of Mathematical Sciences
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Applied Statistics | <https://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/applied-statistics-ms/> |
| 2 | M.S. Data Science (Statistics Concentration) | <https://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/data-science-ms/> |
| 3 | M.S. Applied Mathematics | <http://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/applied-mathematics-ms/> |
| 4 | M.S. Biostatistics | <http://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/biostatistics-ms/> |

##### Department of Mathematical Sciences
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Mathematical Sciences | <http://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/phd/> |

##### Department of Mathematical Sciences
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Certificate in Biostatistics Essentials | <https://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/biostatistics-essentials-cert/> |
| 2 | Certificate in Clinical Trials: Design and Analysis | <https://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/clinical-trials_design-and-analysis-cert/> |
| 3 | Certificate in Applied Statistical Methods | <https://catalog.njit.edu/graduate/science-liberal-arts/mathematical-sciences/applied-statistical-methods-cert/> |

##### Department of Physics
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | M.S. Materials Science and Engineering (Materials Science Option) | <http://catalog.njit.edu/graduate/science-liberal-arts/physics/materials-science-engineering-ms/> |
| 2 | M.S. Applied Physics | <http://catalog.njit.edu/graduate/science-liberal-arts/physics/applied-physics-ms/> |

##### Department of Physics
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Materials Science and Engineering (Materials Science Option) | <http://catalog.njit.edu/graduate/science-liberal-arts/physics/materials-science-engineering-phd/> |
| 2 | Ph.D. Applied Physics | <http://catalog.njit.edu/graduate/science-liberal-arts/physics/applied-physics-phd/> |

#### Martin Tuchman School of Management

##### Department of Management
###### Master's

| # | 专业 | URL |
|---|------|-----|
| 1 | Online MBA | <https://catalog.njit.edu/graduate/management/management/technology-mba/> |
| 2 | M.S. Management | <http://catalog.njit.edu/graduate/management/management/ms/> |
| 3 | Masters in Business Administration (MBA) | <https://www.njit.edu/sites/default/files/TECH%20MBA%2036-Credit%20Curriculum%20GRID.pdf> |
| 4 | Online M.S. in Management | <http://catalog.njit.edu/graduate/management/management/ms/> |

##### Department of Management
###### Doctoral

| # | 专业 | URL |
|---|------|-----|
| 1 | Ph.D. Business Data Science | <http://catalog.njit.edu/graduate/management/management/business-data-science-phd/> |

##### Department of Management
###### Graduate Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Online Certificate in Business Analytics | <https://catalog.njit.edu/graduate/management/management/business-analytics-cert/> |
| 2 | Certificate in Finance for Managers | <> |
| 3 | Online Certificate in Management Technology | <https://catalog.njit.edu/graduate/management/management/management-of-technology-cert/> |
| 4 | Online Innovation and Entrepreneurship Graduate Certificate | <https://catalog.njit.edu/undergraduate/management/management/innovation-entrepreneurship-minor/> |
| 5 | Certificate in Financial Technology | <https://catalog.njit.edu/graduate/management/management/financial-technology-cert/> |
| 6 | Certificate in Innovation and Entrepreneurship | <https://catalog.njit.edu/graduate/management/management/innovation-and-enterprenurship-cert/> |
| 7 | Certificate in Marketing | <> |
| 8 | Certificate in Management Essentials | <> |
| 9 | Online Mini-MBA | <https://catalog.njit.edu/graduate/management/management/mini-mba-cert/> |
| 10 | Certificate in Management Information Systems | <> |
| 11 | Certificate in Business Analytics | <https://catalog.njit.edu/graduate/management/management/business-analytics-cert/> |
| 12 | Certificate in Management of Technology | <> |


### 2.2 至少一个项目的完整深度示例 — M.S. Computer Science

- **学院**: Ying Wu College of Computing (YWCC)
- **系**: Computer Science
- **学位级别**: Master's (M.S.)
- **Department location**: GITC Building, Room 4400, University Heights, Newark, NJ 07102
- **Phone**: (973) 596-2987 (CS Department main line)
- **申请平台**: <https://connect.njit.edu/apply/>
- **申请费**: $75 (non-refundable)
- **TOEFL/IELTS/Duolingo/PTE minimums (grad)**: TOEFL 79 / IELTS 6.5 / Duolingo 120 / PTE 57
- **GRE/GMAT**: 由各系决定（CS Department 2024-2025 admission cycle 为 test-optional for most applicants; 需直接联系 department 获取当前政策）
- **国际学生截止 (Fall)**: May 1；Spring: November 15
- **国内学生截止 (Fall)**: June 1；Spring: November 15；Summer: April 15
- **Ph.D. funding priority deadline (Fall)**: December 15
- **Financial aid**: 自动随 admission 评估；limited graduate assistantships via Office of Graduate Studies
- **Catalog URL**: <https://catalog.njit.edu/graduate/computing-sciences/computer-science/ms/>
- **Accordion details**: GRE policy, materials checklist, funding info — 需在 application portal (<https://connect.njit.edu/apply/>) 注册账号后查看；个别 program-specific test requirements 由系里决定。

### 2.3 研究生录取模式

- **集中 vs 分散**: 集中申请平台 (<https://connect.njit.edu/apply/>)，但各学院/系各自审核并设定 GRE/GMAT/材料要求
- **入学申请费**: $75 (non-refundable)
- **CGS April 15 honor pledge**: NJIT 通过 Graduate Studies Office 接受 April 15 Resolution
- **GRE/GMAT 政策**: 各系自行决定 (per <https://www.njit.edu/admissions/graduate-faqs>)
- **English test 政策**: TOEFL ≥ 79 / IELTS ≥ 6.5 / Duolingo ≥ 120 / PTE ≥ 57；列表国家 (UK, Canada, Australia 等) 豁免
- **应用时间表**: Fall/Spring/Summer 三季；国际学生建议提前 6 个月开始
- **Department code (institutional)**: 002621 (FAFSA)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 本科生 — 核心数据表

| 维度 | 数据 |
|------|------|
| Admissions site | <https://admissions.njit.edu/> |
| Application portal (first-year) | <https://www.commonapp.org/> |
| Application portal (transfer) | <https://njit.edu/apply> |
| **EA I deadline (Fall)** | November 15 |
| **EA II deadline (Fall)** | December 15 |
| **Honors College deadline (Fall)** | February 1 |
| **Rolling Admission (Fall)** | March 1 |
| **Transfer deadline (Fall)** | June 1 |
| **Transfer Honors College (Fall)** | June 1 |
| **Spring Rolling (UG)** | November 15 |
| **Previously Enrolled (Readmit) Fall** | August 1 |
| **Previously Enrolled (Readmit) Spring** | November 15 |
| **International UG Fall** | March 1 |
| **International UG Spring** | October 15 |
| Decision notification | Rolling (typically 2–3 weeks after file complete) |
| Enrollment confirmation deadline | 见 admission offer letter (typically May 1) |
| Financial-aid deadline (FAFSA) | 见 <https://www.njit.edu/how-apply-financial-aid> |
| SAT/ACT policy | **Test-Optional** for Fall 2026 / Spring 2027 / Fall 2027 (Honors College applicants excepted) |
| SAT school code | 2513 |
| ACT school code | 2580 |
| Application fee | $75 (non-refundable) |
| Recommendation letters | 1 counselor + 1 teacher recommended |
| Portfolio | Required for Architecture, Digital Design, Industrial Design, Interior Design majors |
| Interview policy | Not required |
| Honors College separate application | Yes — <https://honors.njit.edu/admission> |

### 3.2 本科生英语水平要求

| 考试 | 最低分 |
|------|--------|
| TOEFL (internet-based) | 79 |
| IELTS | 6.0 |
| Duolingo English Test | 100 |
| PTE Academic | 53 |

> 适用条件: 第一语言非英语的申请者。来自 Antigua/Australia/Bahamas/Barbados/Belize/Canada/Cook Islands/Dominica/Federated State of Micronesia/Ghana/Grenada/Guyana/Ireland/Jamaica/Kenya/Liberia/New Zealand/Niue/Nigeria/Republic of Fiji/Republic of the Marshall Islands/Republic of Palau/Philippines/Saint Kitts and Nevis/Saint Lucia/Saint Helena/South Africa/St. Vincent and the Grenadines/Trinidad and Tobago/United Kingdom/United States (含 island territories) 的学位持有人可豁免。

### 3.3 研究生 — 全局规则

| 维度 | 数据 |
|------|------|
| Application portal | <https://connect.njit.edu/apply/> |
| Standard application fee | $75 (non-refundable) |
| GRE/GMAT policy | 由各系决定 (test-optional for many 2024-2025 programs); 详见 department |
| TOEFL minimum | 79 (internet-based) |
| IELTS minimum | 6.5 |
| Duolingo minimum | 120 |
| PTE minimum | 57 |
| English test exemption | Same country list as UG |
| Ph.D. Fall deadline | December 15 (priority for funding) |
| Ph.D. Spring deadline | October 15 |
| Master's International Fall | May 1 |
| Master's International Spring | November 15 |
| Master's Domestic Fall | June 1 |
| Master's Domestic Spring | November 15 |
| Master's Domestic Summer | April 15 |
| Master's Online Fall | August 1 |
| Certificates Fall/Spring/Summer | May 1 / November 15 / April 15 (International); June 1 / November 15 / April 15 (Domestic); August 1 / November 15 / April 15 (Online) |
| CGS April 15 honor date | Adhered via Graduate Studies Office |
| Institutional code (TOEFL) | 2513 (FAFSA: 002621) |

---

## SECTION 4 — Costs & financial aid

### 4.1 本科生成本 (2025–2026 学年，全日制两个学期)

| 项目 | New Jersey Residents | Non-NJ Residents |
|------|---------------------|-------------------|
| Tuition | $17,312 | $36,062 |
| Fees | $3,850 | $3,850 |
| **Total Tuition and Fees** | **$21,162** | **$39,912** |

**住宿与生活费 (NJ 与 Non-NJ 相同):**

| 居住情况 | Housing & Food | Additional Indirect Cost |
|----------|----------------|------------------------|
| On-campus | $16,450 | $5,200 |
| With parents | $9,800 | $6,900 |
| Off-campus | $17,936 | $6,900 |

**其他费用:**

| 项目 | 金额 | 适用条件 |
|------|------|----------|
| Books & Supplies | $2,900 | first-year & transfer non-architecture |
| Books & Supplies | $4,800 | first-year & transfer architecture |
| Full-time 定义 | 12–19 credits/semester | — |

### 4.2 本科生 Financial Aid 政策

| 维度 | 数据 |
|------|------|
| 95% of NJIT students receive scholarships/grants/financial aid | 见 <https://admissions.njit.edu/> |
| 80% of all undergrads receive some form of financial aid | — |
| 92% of first-time freshmen and transfer students receive aid | — |
| Total financial aid disbursed | > $100 million/year (financial aid office) |
| Need-based grants | Available; FAFSA required annually |
| Merit-based scholarships | Automatic consideration upon enrollment |
| Federal loans | Federal Direct, Federal PLUS, Graduate PLUS, Federal Perkins |
| Private loans | NJCLASS (HESAA) and others |
| Federal College Work-Study (FCWS) | For US citizens/permanent residents with need |
| Institutional Work-Study (IWS) | For non-FCWS eligible; internationals must be full-time |
| Military/Veteran benefits | GI Bill, Vocational Rehab, Post-9/11, etc. |
| Tuition-free income threshold | N/A (NJIT is not a no-loan school); 详见 financial aid office |
| Median actual price paid | 见 <https://www.njit.edu/admissions/financial-aid> (P1 follow-up) |
| Need-blind/need-aware | Need-aware for all applicants (public institution); not need-blind |
| Average starting salary | 见 alumni outcomes (not in this capture; P1 follow-up) |
| Debt-free graduation rate | 见 financial aid office (P1 follow-up) |

### 4.3 研究生成本 & 资助框架 (2025–2026 学年)

**基础学费:**

| 项目 | NJ Residents | Non-NJ Residents |
|------|--------------|------------------|
| Tuition | $24,982 | $36,938 |
| Fees | $3,796 | $3,796 |
| **Total Per Year** | **$28,778** | **$40,734** |

(Full-time = 9 credits)

**住宿与生活费 (NJ 与 Non-NJ 相同):**

| 居住情况 | Housing & Food | Additional Indirect Cost |
|----------|----------------|------------------------|
| On-campus | $16,450 | $6,400 |
| Off-campus | $17,936 | $9,400 |

**书籍:**

| 项目 | 金额 |
|------|------|
| Books & Supplies (non-architecture) | $1,600 |
| Books & Supplies (architecture) | $2,000 |

**在线学位学费:**

| 类型 | 每学分费用 |
|------|------------|
| Graduate e-Tuition (100% online) | $1,211 |
| Undergraduate e-Tuition (100% online) | $569 |
| Jersey City (campus-based, lower) | $1,041 |

**国际学生成本:**

| 项目 | Undergraduate | Graduate |
|------|--------------|----------|
| Tuition and Fees | $39,912 | $40,734 |
| Living Expenses | $17,580 | $17,580 |
| Other Expenses (health insurance, etc.) | $10,647 | $9,947 |
| **Total Estimated Cost** | **$68,139** | **$68,261** |

**资助分类:**

| 类型 | 详情 |
|------|------|
| 资助形式 | RA / TA / Fellowship / Grant — 由系里在 admission 时自动评估 |
| Graduate Assistantships | Limited, via Office of Graduate Studies; 见 <https://www.njit.edu/graduatestudies/> |
| Financial support page | <https://www.njit.edu/graduatestudies/financial-support> (P1 follow-up) |
| 国际学生 Ph.D. funding priority deadline | December 15 |
| Tuition remission | 详见系里 assistantship offer (P1 follow-up) |

---

## SECTION 5 — Evidence chain index

```yaml
E-INST-001:
  field: institution.total_program_count
  value: 210
  source_url: https://www.njit.edu/search-api/corporate/degree/_search?size=300 (POST Elasticsearch query)
  source_snippet: "Total hits: 210" — Elasticsearch API response on 2026-07-07
  capture_date: 2026-07-07
  evidence_type: official_api

E-INST-002:
  field: institution.school_count
  value: 6
  source_url: https://www.njit.edu/about
  source_snippet: "NJIT offers more than 125 undergraduate and graduate degree programs in six specialized schools instructed by expert faculty, 98 percent of whom hold the highest degree in their field."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-INST-003:
  field: institution.ug_total_programs
  value: 56 (55 Bachelor's + 1 B.S.E.T.)
  source_url: https://www.njit.edu/search-api/corporate/degree/_search
  source_snippet: "Bachelor's: 55 ... B.S.E.T.: 1"
  capture_date: 2026-07-07
  evidence_type: official_api

E-INST-004:
  field: institution.grad_total_programs
  value: 154 (64 Master's + 20 Doctoral + 70 Graduate Certificate)
  source_url: https://www.njit.edu/search-api/corporate/degree/_search
  source_snippet: "Master's: 64 ... Doctoral: 20 ... Graduate Certificate: 70"
  capture_date: 2026-07-07
  evidence_type: official_api

E-DEAD-UG-001:
  field: undergraduate.deadlines.fall.first_year_EA_I
  value: "November 15"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Early Action I: November 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-UG-002:
  field: undergraduate.deadlines.fall.first_year_EA_II
  value: "December 15"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Early Action II: December 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-UG-003:
  field: undergraduate.deadlines.fall.honors_college
  value: "February 1"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Honors College: February 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-UG-004:
  field: undergraduate.deadlines.fall.rolling
  value: "March 1"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Rolling Admission: March 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-UG-005:
  field: undergraduate.deadlines.fall.transfer
  value: "June 1"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Fall Semester: June 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-UG-006:
  field: undergraduate.deadlines.spring.rolling
  value: "November 15"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "Spring Semester Rolling Admission: November 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-INTL-UG-001:
  field: undergraduate.international.fall
  value: "March 1"
  source_url: https://www.njit.edu/admissions/dates-deadlines-international-students
  source_snippet: "Undergraduate International Applicants Fall semester: March 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-DEAD-INTL-UG-002:
  field: undergraduate.international.spring
  value: "October 15"
  source_url: https://www.njit.edu/admissions/dates-deadlines-international-students
  source_snippet: "Spring semester: October 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-DEAD-GRAD-001:
  field: graduate.deadlines.phd.fall
  value: "December 15"
  source_url: https://www.njit.edu/admissions/grad-dates-deadlines
  source_snippet: "Ph.D. December 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-GRAD-002:
  field: graduate.deadlines.phd.spring
  value: "October 15"
  source_url: https://www.njit.edu/admissions/grad-dates-deadlines
  source_snippet: "Ph.D. October 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-GRAD-003:
  field: graduate.deadlines.masters.international.fall
  value: "May 1"
  source_url: https://www.njit.edu/admissions/grad-dates-deadlines
  source_snippet: "Master's - International May 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-DEAD-GRAD-004:
  field: graduate.deadlines.masters.domestic.fall
  value: "June 1"
  source_url: https://www.njit.edu/admissions/grad-dates-deadlines
  source_snippet: "Master's - Domestic June 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-FEE-001:
  field: application_fee.undergraduate
  value: "$75"
  source_url: https://www.njit.edu/admissions/dates-deadlines
  source_snippet: "The non-refundable application fee is $75."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-FEE-002:
  field: application_fee.graduate
  value: "$75"
  source_url: https://www.njit.edu/admissions/grad-dates-deadlines
  source_snippet: "The non-refundable application fee is $75."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-TEST-UG-001:
  field: undergraduate.test_policy.sat_act
  value: "Test-Optional for Fall 2026, Spring 2027, Fall 2027"
  source_url: https://www.njit.edu/admissions/how-we-evaluate-applicants
  source_snippet: "Test-Optional Admission Policy for Fall 2026, Spring 2027 and Fall 2027 ... can choose to not submit SAT and/or ACT scores. This does not apply to Albert Dorman Honors College or accelerated program applicants."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-TEST-UG-002:
  field: undergraduate.scores.avg_sat
  value: "1285"
  source_url: https://www.njit.edu/admissions/how-we-evaluate-applicants
  source_snippet: "Average composite SAT score for our enrolling first-year class is 1285 (Math and Critical Reading)."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-TEST-UG-003:
  field: undergraduate.scores.avg_act
  value: "26"
  source_url: https://www.njit.edu/admissions/how-we-evaluate-applicants
  source_snippet: "Average ACT score for our enrolling first-year class is 26."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-TEST-UG-004:
  field: undergraduate.test_codes.sat
  value: "2513"
  source_url: https://www.njit.edu/admissions/how-we-evaluate-applicants
  source_snippet: "SAT school code: 2513"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-TEST-UG-005:
  field: undergraduate.test_codes.act
  value: "2580"
  source_url: https://www.njit.edu/admissions/how-we-evaluate-applicants
  source_snippet: "ACT school code: 2580"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-ENG-UG-001:
  field: undergraduate.english.toefl_min
  value: "79"
  source_url: https://www.njit.edu/admissions/how-apply-international-students
  source_snippet: "TOEFL: 79"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-ENG-UG-002:
  field: undergraduate.english.ielts_min
  value: "6.0"
  source_url: https://www.njit.edu/admissions/how-apply-international-students
  source_snippet: "IELTS 6.0"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-ENG-UG-003:
  field: undergraduate.english.duolingo_min
  value: "100"
  source_url: https://www.njit.edu/admissions/how-apply-international-students
  source_snippet: "Duolingo: 100"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-ENG-UG-004:
  field: undergraduate.english.pte_min
  value: "53"
  source_url: https://www.njit.edu/admissions/how-apply-international-students
  source_snippet: "PTE: 53"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-ENG-GRAD-001:
  field: graduate.english.toefl_min
  value: "79"
  source_url: https://www.njit.edu/admissions/graduate-faqs
  source_snippet: "The minimum TOEFL score requirement is 4.0 overall (new scale) or 79 (old scale)."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-ENG-GRAD-002:
  field: graduate.english.ielts_min
  value: "6.5"
  source_url: https://www.njit.edu/admissions/graduate-faqs
  source_snippet: "The minimum IELTS score is 6.5."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-ENG-GRAD-003:
  field: graduate.english.duolingo_min
  value: "120"
  source_url: https://www.njit.edu/admissions/graduate-faqs
  source_snippet: "The minimum Duolingo score is 120."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-ENG-GRAD-004:
  field: graduate.english.pte_min
  value: "57"
  source_url: https://www.njit.edu/admissions/graduate-faqs
  source_snippet: "The minimum PTE score is 57."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-UG-001:
  field: undergraduate.cost.tuition_2025_2026.NJ_resident
  value: "$17,312"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Tuition $17,312 $36,062 ... New Jersey Residents Non-New Jersey Residents"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-UG-002:
  field: undergraduate.cost.tuition_2025_2026.NonNJ_resident
  value: "$36,062"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Tuition $17,312 $36,062"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-UG-003:
  field: undergraduate.cost.fees_2025_2026
  value: "$3,850"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Fees $3,850 $3,850"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-UG-004:
  field: undergraduate.cost.total_tuition_fees_2025_2026.NJ_resident
  value: "$21,162"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Tuition and Fees $21,162 $39,912"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-UG-005:
  field: undergraduate.cost.total_tuition_fees_2025_2026.NonNJ_resident
  value: "$39,912"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Tuition and Fees $21,162 $39,912"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-UG-006:
  field: undergraduate.cost.housing_food.on_campus
  value: "$16,450"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "For New Jersey resident and Non-New Jersey resident students living on campus, the value for Housing & Food is $16,450"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-UG-007:
  field: undergraduate.cost.housing_food.with_parents
  value: "$9,800"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "For New Jersey resident and Non-New Jersey resident students living with parents, the value for Housing & Food is $9,800"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-UG-008:
  field: undergraduate.cost.housing_food.off_campus
  value: "$17,936"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "For New Jersey resident and Non-New Jersey resident students living off campus, the value for Housing & Food is $17,936"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-UG-009:
  field: undergraduate.cost.books_supplies.non_arch
  value: "$2,900"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "The value for Books & Supplies is $2,900 (first-year and transfer non-architecture students)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-UG-010:
  field: undergraduate.cost.books_supplies.arch
  value: "$4,800"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "$4,800 (first-year and transfer architecture students)"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-GRAD-001:
  field: graduate.cost.tuition_2025_2026.NJ_resident
  value: "$24,982"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Tuition $24,982 $36,938"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-GRAD-002:
  field: graduate.cost.tuition_2025_2026.NonNJ_resident
  value: "$36,938"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Tuition $24,982 $36,938"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-GRAD-003:
  field: graduate.cost.total_per_year.NJ_resident
  value: "$28,778"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Per Year $28,778 $40,734"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-GRAD-004:
  field: graduate.cost.total_per_year.NonNJ_resident
  value: "$40,734"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Per Year $28,778 $40,734"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-ONLINE-001:
  field: tuition.online.ug_per_credit
  value: "$569"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Undergraduate e-Tuition (100% online) Cost per credit - $569"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-ONLINE-002:
  field: tuition.online.grad_per_credit
  value: "$1,211"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Graduate e-Tuition (100% online) Cost per credit - $1,211"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-COST-INTL-001:
  field: international.cost.ug.total
  value: "$68,139"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Estimated Cost † $68,139 $68,261"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-COST-INTL-002:
  field: international.cost.grad.total
  value: "$68,261"
  source_url: https://www.njit.edu/admissions/tuition-costs
  source_snippet: "Total Estimated Cost † $68,139 $68,261"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-AID-001:
  field: financial_aid.percent_undergrad_receiving
  value: "80%"
  source_url: https://www.njit.edu/admissions/financial-aid
  source_snippet: "Close to 80% of all our undergrad students receive some form of financial aid"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-AID-002:
  field: financial_aid.percent_first_time_receiving
  value: "92%"
  source_url: https://www.njit.edu/admissions/financial-aid
  source_snippet: "92% of our first time incoming freshmen and transfer students"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-AID-003:
  field: financial_aid.total_disbursed
  value: "$100 million+"
  source_url: https://www.njit.edu/admissions/financial-aid
  source_snippet: "Our office provides more than $100 million in financial assistance to our students."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-PROG-API-001:
  field: programs.api.source
  value: "https://www.njit.edu/search-api/corporate/degree/_search (Elasticsearch, size=300)"
  source_url: https://www.njit.edu/search-api/corporate/degree/_search
  source_snippet: "Total hits: 210 ... fields include: title, catalog_url, degree_level_terms, college_terms, department_terms, major_terms, summary"
  capture_date: 2026-07-07
  evidence_type: official_api

E-PROG-CAT-001:
  field: programs.catalog.source
  value: "https://catalog.njit.edu/programs/"
  source_url: https://catalog.njit.edu/programs/
  source_snippet: "Programs table with College/Department/Degree Level/Discipline/Special Degree Options columns; 153 base programs with 30+ special-degree-option rows (Double Major/Accelerated/B.S./M.S.)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-PROG-MINORS-001:
  field: programs.minors.source
  value: "60 minors across 4 colleges"
  source_url: https://catalog.njit.edu/undergraduate/academic-policies-procedures/academic-minors/
  source_snippet: "A minor consists of a minimum of 15 credits of coursework within a single area of study or across several disciplines."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-HONORS-001:
  field: institution.honors_college
  value: "Albert Dorman Honors College"
  source_url: https://honors.njit.edu/
  source_snippet: "The Albert Dorman Honors College offers top students a well-rounded, interdisciplinary education grounded in service, research, and leadership"
  capture_date: 2026-07-07
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
njit-knowledge-base-v2 (collection)
├── njit-overview-v2.md (document)
│   ├── chunk: institution-overview
│   ├── chunk: total-program-counts
│   ├── chunk: college-hierarchy-tree
│   ├── chunk: degree-level-inventory
│   └── chunk: distribution-matrix
├── njit-undergraduate-v2.md (document)
│   ├── chunk: ug-newark-college-engineering (College → Departments → Programs)
│   ├── chunk: ug-hillier-architecture-design (College → Departments → Programs)
│   ├── chunk: ug-ying-wu-computing (College → Departments → Programs)
│   ├── chunk: ug-jordan-hu-science-liberal-arts (College → Departments → Programs)
│   ├── chunk: ug-martin-tuchman-management (College → Departments → Programs)
│   ├── chunk: ug-cross-college-programs (Double majors, Accelerated, B.S./M.S.)
│   └── chunk: ug-minors (60 minors across 4 colleges)
├── njit-graduate-v2.md (document)
│   ├── chunk: grad-newark-college-engineering (MS, PhD, Certificate)
│   ├── chunk: grad-hillier-architecture-design (MS, M.Arch., MUD, PhD, Certificate)
│   ├── chunk: grad-ying-wu-computing (MS, PhD, Certificate)
│   ├── chunk: grad-jordan-hu-science-liberal-arts (MS, MA, PhD, Certificate)
│   ├── chunk: grad-martin-tuchman-management (MBA, MSM, MS, PhD, Certificate)
│   └── chunk: grad-application-process (worked example: MS Computer Science)
├── njit-requirements-v2.md (document)
│   ├── chunk: ug-deadlines
│   ├── chunk: ug-test-policy
│   ├── chunk: ug-english-proficiency
│   ├── chunk: grad-deadlines
│   ├── chunk: grad-test-policy
│   └── chunk: grad-english-proficiency
├── njit-costs-v2.md (document)
│   ├── chunk: ug-tuition-fees
│   ├── chunk: ug-housing-food
│   ├── chunk: ug-books-supplies
│   ├── chunk: grad-tuition-fees
│   ├── chunk: grad-online-tuition
│   ├── chunk: international-costs
│   └── chunk: financial-aid-policy
└── njit-evidence-v2.md (document)
    └── chunk: evidence-chain (E-INST-001 … E-HONORS-001)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "njit-knowledge-base-v2"
  school: "<home college>"           # 学院 name (e.g., Newark College of Engineering)
  department: "<home department>"    # 系 name (e.g., Computer Science)
  degree_level: "<BA|BS|MA|MS|PhD|Certificate|B.S.E.T.>"
  level: "undergraduate" | "graduate"
  field_type: "overview|counts|hierarchy|programs|deadlines|tests|costs|funding"
  source_url: "<URL>"
  capture_date: "2026-07-07"
  version: "v2.0"
  change_status: "baseline"
  last_verified: "2026-07-07"
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|-----------|--------|
| P0 | Per-program GRE/GMAT requirements | <https://catalog.njit.edu/graduate/> | 各系自行决定；需逐系页面提取 |
| P0 | Stipend rates for RA/TA/Fellowship | <https://www.njit.edu/graduatestudies/financial-support> | 未在本次抓取范围 |
| P0 | Median actual price paid (UG) | <https://www.njit.edu/admissions/financial-aid> | 未抓到该具体值 |
| P1 | General Education Program (GEP) requirement list | <https://catalog.njit.edu/undergraduate/academic-policies-procedures/general-education-requirements/> | 抓取时未深入 |
| P1 | Detailed course catalog (course-level) | <https://catalog.njit.edu/> | 本次仅抓 program-level |
| P1 | Honors College admissions requirements | <https://honors.njit.edu/admission> | 本次仅抓到主页 |
| P1 | Transfer credit articulation | <https://www.njit.edu/admissions/how-credits-transfer> | 本次仅列链接 |
| P2 | Average starting salary / debt data | <https://www.njit.edu/about> (alumni outcomes section) | 未抓取 |
| P2 | International student visa timeline details | <https://www.njit.edu/admissions/applying-visa> | 未抓取 |
| P2 | Tuition-free / no-loan policy | — | NJIT 不采用 no-loan 模型 |

---

## SECTION 7 — Cross-school comparison framework

> 此节保留供后续学校数据填入后做横向对比。

| Dimension | NJIT (2026-07-07) | MIT (TBD) | Stanford (TBD) | Harvard (TBD) | Caltech (TBD) |
|-----------|------------------|-----------|----------------|---------------|---------------|
| Total UG cost/yr (in-state) | $21,162 | | | | |
| Total UG cost/yr (out-of-state) | $39,912 | | | | |
| Tuition/yr (in-state) | $17,312 | | | | |
| Tuition/yr (out-of-state) | $36,062 | | | | |
| Application fee | $75 | | | | |
| Need-blind (intl?) | No (public) | | | | |
| EA deadline | Nov 15 / Dec 15 | | | | |
| RA deadline | Mar 1 | | | | |
| SAT/ACT required? | Test-optional | | | | |
| TOEFL min (UG) | 79 | | | | |
| IELTS min (UG) | 6.0 | | | | |
| TOEFL min (Grad) | 79 | | | | |
| IELTS min (Grad) | 6.5 | | | | |
| Tuition-free threshold | N/A (public polytechnic) | | | | |
| Median price paid | TBD (P1) | | | | |
| Grad application fee | $75 | | | | |
| April-15 honor date | Yes | | | | |
| **Total program count (rule 1)** | **210** | | | | |
| **College/school count (rule 2)** | **6** | | | | |
| Minors count | 60 | | | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: njit.edu, admissions.njit.edu, catalog.njit.edu, honors.njit.edu, search-api/corporate/degree/_search (Elasticsearch backend)
> **Verification**: ego-browser snapshotText + JS DOM extraction + direct Elasticsearch API query
> **Granularity**: school → department → degree-level → program
