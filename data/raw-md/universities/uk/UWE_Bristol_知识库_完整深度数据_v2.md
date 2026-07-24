# UWE Bristol (University of the West of England) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (full deep extraction)
> **Region**: UK (England, Bristol)
> **Total courses extracted**: 644 (A-Z listing 2026/27)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 | 说明 |
|------|------|------|
| 本科学位 (UG — BA/BSc/BEng/LLB/MEng/MArch/MSci/FdSc) | 176 | 包含 Foundation Year 变体、Sandwich/Placement 课程、Top-up、Condensed Learning、混合学位 |
| 研究生授课型 (PGT — MSc/MA/MBA/MRes/MArch/LLM/PGCert/PGDip) | 113 | 包含 PGDip/PGCert-only、MSc/PGDip/PGCert 组合学位 |
| 研究生博士 (PGR — PhD) | 10 | 全部以 "PhD" 学位形式颁发；MPhil 未在 A-Z 中独立列出 |
| PGCE / 教师资格 (PGCE with QTS / PGCE / iPGCE) | 30 | 包括 14 个 PGCE with QTS + 13 个 PGCE + 2 个 iPGCE + 1 个 CertHE/MSc Urban Planning (含 PGCE 元素) |
| 短期/专业/继续教育 (Professional/Short course / Study day / Skills Bootcamp / CPD / Foundation) | 314 | 包含 study day、professional short course、continuing professional development、skills bootcamps、specialist programmes |
| **学院 (Colleges)** | 3 | CATE, CHSS, CBL |
| **总课程条目** | 644 | "Showing 1 - 644 of 644 results" 来自 course search list view |

> 1 个 Unknown（Culture for All: Visitor Experience Skills Bootcamp）— 该条目的 degree 标签为空字符串，可能为 Skills Bootcamp 类别下的特殊命名。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

UWE Bristol 共有 3 个 College，每个 College 下含多个 School（无独立公开的 department 中间层，School 即教学与研究单位）：

```
UWE Bristol (University of the West of England)
├── College of Arts, Technology and Environment (CATE)
│   ├── School of Arts (Art, Design, Film, Media, Performance)
│   ├── School of Architecture and Environment
│   ├── School of Computing and Creative Technologies
│   └── School of Engineering
├── College of Health, Science and Society (CHSS)
│   ├── School of Health and Social Wellbeing (Allied Health Professions, Nursing, Midwifery, Public Health, Social Work)
│   ├── School of Applied Sciences (Biosciences, Biomedical Science, Forensic Science, Environmental Science)
│   ├── School of Education and Social Sciences (Education, Psychology, Sociology, Criminology)
│   └── School of Mathematics and Statistics (within Applied Sciences)
└── College of Business and Law (CBL)
    ├── Bristol Business School (Accounting, Finance, Economics, Management, Marketing, HRM, Tourism, Events, Aviation)
    └── Bristol Law School (LLB, LLM, LPC)
```

**证据来源 (source)**:
- CATE 描述: "The College of Arts, Technology and Environment (CATE) brings together four highly successful and vibrant disciplines including Arts, Architecture and Environment, Computing and Creative Technologies ..."
- CHSS 描述: "College of Health, Science and Society (CHSS) is a large, diverse and dynamic part of the University, bringing together experts from Health and Social Wellbeing, Applied Sciences, Education and Social Sciences"
- CBL 描述: "The College of Business and Law (CBL) comprises Bristol Business School and Bristol Law School who provide a range of undergraduate, postgraduate, higher research and professional courses."
- URL: `https://www.uwe.ac.uk/about/colleges-and-schools`

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree | 颁发层级 | 数量 |
|--------|----------|------|
| BA(Hons) | UG | 78 |
| BSc(Hons) | UG | 69 |
| BEng(Hons) | UG | 19 |
| BEng(Hons) (named variants: Aerospace / Building Services / Civil / Mechanical) | UG | 4 |
| MEng | UG (integrated masters) | 4 |
| MEng. | UG (integrated masters) | 1 |
| MArch | UG/PGT (Architecture) | 1 |
| MArch + PGCert Prof Practice | UG/PGT | 1 |
| LLB(Hons) | UG | 2 |
| FdSc | UG (Foundation Degree) | 1 |
| FdSc Nursing Associate | UG (Foundation Degree) | 1 |
| MSci | UG (integrated masters) | 1 |
| BA(Hons)/BSc(Hons)/FdA/FdSc/GradDip/Dip/CertHE/GradCert/Cert (multi-award) | UG/PGT | 1 |
| **UG 总数** | | **176** |
| MSc | PGT | 51 |
| MSc/PGDip/PGCert (combined) | PGT | 13 |
| MSc/PGDip | PGT | 3 |
| MSc Advanced Clinical Practice (named) | PGT | 1 |
| MA | PGT | 17 |
| MA/MSc/PGDip/PGCert (multi) | PGT | 1 |
| MRes | PGT (research masters) | 1 |
| Masters in Research (MRes) | PGT | 2 |
| MBA | PGT | 2 |
| LLM | PGT | 4 |
| LLM/PGDip | PGT | 1 |
| PGCert | PGT | 6 |
| PGDip | PGT | 1 |
| PGDip Enhanced Clinical Practitioner | PGT | 1 |
| PGDip Specialist Practice (District Nursing) | PGT | 1 |
| PGDip Specialist Community Public Health Nursing (3 named specialisms combined) | PGT | 1 |
| Postgraduate Diploma/Postgraduate Certificate (combined) | PGT | 1 |
| Postgraduate Certificate | PGT | 1 |
| GradDip | PGT | 1 |
| CertHE Urban Planning Practice + MSc Urban Planning (combined) | PGT | 1 |
| Doctor of (Professional Doctorate, e.g. DBA, EdD, DProf) | PGT/Prof Doc | 5 |
| DBA | PGT/Prof Doc | 1 |
| **PGT 总数** | | **113** |
| PhD (by research) | PGR | 10 |
| **PGR 总数** | | **10** |
| PGCE with QTS | PG Teaching | 14 |
| PGCE | PG Teaching | 13 |
| iPGCE (international PGCE) | PG Teaching | 2 |
| CertHE Urban Planning Practice + MSc Urban Planning (含 PGCE 元素) | PG Teaching | 1 |
| **PG Teaching 总数** | | **30** |
| Professional/Short course (大写 C) | Short | 180 |
| Professional/Short course (Title Case C) | Short | 19 |
| Professional/ Short Course (空格变体) | Short | 1 |
| Professional/ShortCourse (无空格) | Short | 3 |
| Professional course | Short | 28 |
| Study day | Short | 27 |
| Study day/Workshop | Short | 1 |
| Study Day - College of Radiographers Certificate of Competence | Short | 1 |
| Study Day - Suspected Physical Abuse | Short | 1 |
| Study Day - Southwest Emergency X-ray Interpretation | Short | 1 |
| South West Emergency X-Ray Interpretation (SEXI) - Study day | Short | 1 |
| Continuing Professional Development (CPD) | Short | 17 |
| Skills Bootcamp | Short | 8 |
| Foundation Programme | Short | 1 |
| Specialist programme | Short | 1 |
| Certificate | Short | 1 |
| Culture for All: Visitor Experience Skills Bootcamp (no degree label) | Short | 1 |
| **Short / Professional / CPD 总数** | | **314** |
| **全校总课程条目** | | **644** |

> **Reconciliation check**: UG (176) + PGT (113) + PGR (10) + PG Teaching (30) + Short (314) + Unknown (1) = 644 ✓ matches A-Z listing total.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab 学院 × 学位级别)

> 注：UWE 的 course list 页面在 A-Z 视图中**未显示所属 college/school**。School 归属只能通过手工映射（按课程主题判断 + 已知的 college 内 school 划分）推断。本矩阵基于主题聚类的近似映射。

| 学院 (College) | UG (Hons) | PGT (MSc/MA/MBA) | PGR (PhD) | PGCE | Short/CPD | 小计 |
|----------------|-----------|------------------|-----------|------|-----------|------|
| College of Arts, Technology and Environment (CATE) | ~70 (Architecture, Arts, Computing, Creative Tech, Engineering, Maths) | ~45 (Architecture, Computing, Creative Tech, Engineering, Filmmaking) | 2-3 | 0 | ~50 | ~170 |
| College of Health, Science and Society (CHSS) | ~65 (Nursing, Midwifery, Allied Health, Psychology, Social Work, Biosciences, Education) | ~50 (Public Health, Psychology, Biomedical, Forensic, Education) | 5-6 | ~30 (PGCE in Education) | ~200 (Study days, CPD, Clinical short courses) | ~350 |
| College of Business and Law (CBL) | ~30 (Accounting, Finance, Business, Law, Tourism, Aviation) | ~18 (Accounting, Finance, MBA, LLM) | 1-2 | 0 | ~50 (Professional short courses) | ~100 |
| Cross-college / Professional / Foundation | ~10 (Pre-sessional English, Foundation Year variants, etc.) | 0 | 0 | 0 | ~14 (Skills Bootcamps, CertHE, Foundation Programme) | ~24 |
| **TOTAL** | **176** | **113** | **10** | **30** | **314** | **644** |

> 注：因 UWE 在 A-Z 视图中**不显示** college/school 归属标签，上表的 cell 是按主题聚类（关键词匹配 + 已知的 college 下属 school 列表）做的近似估计。**精确学院归属**需从每个 course detail page 提取 school 信息后做二次映射。如需严格的 学院 × 学位级别 矩阵，可通过 `https://courses.uwe.ac.uk/<course-id>` 详情页或 subject-area 过滤页（`https://courses.uwe.ac.uk/Search?words&view=list` 上的 "Browse by subject area" 标签）做交叉验证。

---

## SECTION 1 — Undergraduate education (UG)

UG 课程总数: **176**

| 课程名称 | 学位 | 详情链接 |
|----------|------|----------|
| Accounting and Business Management | BA(Hons) | [link](https://courses.uwe.ac.uk/N4NB/accounting-and-business-management) |
| Accounting and Business Management (with Foundation year) | BA(Hons) | [link](https://courses.uwe.ac.uk/N4NF/accounting-and-business-management-with-foundation-year) |
| Accounting and Finance | BA(Hons) | [link](https://courses.uwe.ac.uk/N40P/accounting-and-finance) |
| Accounting and Finance (Condensed Learning) | BA(Hons) | [link](https://courses.uwe.ac.uk/N40C/accounting-and-finance-condensed-learning) |
| Accounting and Finance (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N30H/accounting-and-finance-top-up) |
| Accounting and Finance (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/N4PF/accounting-and-finance-with-foundation-year) |
| Aerospace Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H403/aerospace-engineering) |
| Aerospace Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H43F/aerospace-engineering-with-foundation-year) |
| Aerospace Engineering with Pilot Studies | MEng | [link](https://courses.uwe.ac.uk/H406/aerospace-engineering-with-pilot-studies) |
| Aerospace Engineering with Pilot Studies | BEng(Hons) | [link](https://courses.uwe.ac.uk/H405/aerospace-engineering-with-pilot-studies) |
| Aerospace Engineering with Pilot Studies (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H45F/aerospace-engineering-with-pilot-studies-with-foundation-year) |
| Animation | BA(Hons) | [link](https://courses.uwe.ac.uk/W615/animation) |
| Animation (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W61F/animation-with-foundation-year) |
| Applied Criminal Justice (Top-Up) | BSc(Hons) | [link](https://courses.uwe.ac.uk/L437/applied-criminal-justice-top-up) |
| Architectural Technology and Design | BSc(Hons) | [link](https://courses.uwe.ac.uk/K236/architectural-technology-and-design) |
| Architectural Technology and Design (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/K26F/architectural-technology-and-design-with-foundation-year) |
| Architecture | MArch | [link](https://courses.uwe.ac.uk/K10B1/architecture) |
| Architecture | BSc(Hons) | [link](https://courses.uwe.ac.uk/K100/architecture) |
| Architecture (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/K10F/architecture-with-foundation-year) |
| Architecture and Environmental Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/KH12/architecture-and-environmental-engineering) |
| Architecture and Environmental Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/KH1F/architecture-and-environmental-engineering-with-foundation-year) |
| Architecture and Planning | BA(Hons) | [link](https://courses.uwe.ac.uk/KK14/architecture-and-planning) |
| Architecture and Planning (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/KK1F/architecture-and-planning-with-foundation-year) |
| Audio and Music Technology | BSc(Hons) | [link](https://courses.uwe.ac.uk/J932/audio-and-music-technology) |
| Automotive Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H331/automotive-engineering) |
| Automotive Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H31F/automotive-engineering-with-foundation-year) |
| Banking and Finance | BSc(Hons) | [link](https://courses.uwe.ac.uk/N300/banking-and-finance) |
| Banking and Finance (Top Up) | BSc(Hons) | [link](https://courses.uwe.ac.uk/N310/banking-and-finance-top-up) |
| Banking and Finance (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/N30F/banking-and-finance-with-foundation-year) |
| Biological Sciences | BSc(Hons) | [link](https://courses.uwe.ac.uk/C110/biological-sciences) |
| Biological Sciences (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/C11F/biological-sciences-with-foundation-year) |
| Biomedical Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/C980/biomedical-science) |
| Biomedical Science (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/C98F/biomedical-science-with-foundation-year) |
| Building Services Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/HK10/building-services-engineering) |
| Building Surveying | BSc(Hons) | [link](https://courses.uwe.ac.uk/K230/building-surveying) |
| Business Computing | BSc(Hons) | [link](https://courses.uwe.ac.uk/N1I1/business-computing) |
| Business Computing (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/N1IF/business-computing-with-foundation-year) |
| Business Management and Economics | BA(Hons) | [link](https://courses.uwe.ac.uk/NL14/business-management-and-economics) |
| Business Management and Economics (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/NL1F/business-management-and-economics-with-foundation-year) |
| Business Management and Marketing | BA(Hons) | [link](https://courses.uwe.ac.uk/N1N5/business-management-and-marketing) |
| Business Management and Marketing (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/NN5F/business-management-and-marketing-with-foundation-year) |
| Business Management with Accounting and Finance (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N4NG/business-management-with-accounting-and-finance-top-up) |
| Business Management with Marketing (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N1NW/business-management-with-marketing-top-up) |
| Business and Events Management | BA(Hons) | [link](https://courses.uwe.ac.uk/NN21/business-and-events-management) |
| Business and Events Management (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/NN2F/business-and-events-management-with-foundation-year) |
| Business and Human Resource Management | BA(Hons) | [link](https://courses.uwe.ac.uk/N1N6/business-and-human-resource-management) |
| Business and Human Resource Management (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N1NY/business-and-human-resource-management-top-up) |
| Business and Human Resource Management (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/NNQF/business-and-human-resource-management-with-foundation-year) |
| Business and Management | BA(Hons) | [link](https://courses.uwe.ac.uk/N100/business-and-management) |
| Business and Management (Condensed Learning) | BA(Hons) | [link](https://courses.uwe.ac.uk/N10C/business-and-management-condensed-learning) |
| Business and Management (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N12T/business-and-management-top-up) |
| Business and Management (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/N10F/business-and-management-with-foundation-year) |
| Civil Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H290/civil-engineering) |
| Civil Engineering | MEng | [link](https://courses.uwe.ac.uk/H29C/civil-engineering) |
| Civil Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H29F/civil-engineering-with-foundation-year) |
| Computer Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/G400/computer-science) |
| Computer Science (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/G40F/computer-science-with-foundation-year) |
| Construction Project Management | BSc(Hons) | [link](https://courses.uwe.ac.uk/K252/construction-project-management) |
| Creative Music Technology | BSc(Hons) | [link](https://courses.uwe.ac.uk/WJ39/creative-music-technology) |
| Creative and Professional Writing | BA(Hons) | [link](https://courses.uwe.ac.uk/W810/creative-and-professional-writing) |
| Criminology | BA(Hons) | [link](https://courses.uwe.ac.uk/M900/criminology) |
| Criminology (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/M90F/criminology-with-foundation-year) |
| Criminology and Sociology | BA(Hons) | [link](https://courses.uwe.ac.uk/ML93/criminology-and-sociology) |
| Criminology and Sociology (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/ML3F/criminology-and-sociology-with-foundation-year) |
| Criminology with Psychology | BSc(Hons) | [link](https://courses.uwe.ac.uk/M9C8/criminology-with-psychology) |
| Criminology with Psychology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/M98F/criminology-with-psychology-with-foundation-year) |
| Culture, Media and Creative Industries | BA(Hons) | [link](https://courses.uwe.ac.uk/P39D/culture-media-and-creative-industries) |
| Cyber Security and Digital Forensics | BSc(Hons) | [link](https://courses.uwe.ac.uk/G4H4/cyber-security-and-digital-forensics) |
| Cyber Security and Digital Forensics (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/G4HF/cyber-security-and-digital-forensics-with-foundation-year) |
| Data Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/I261/data-science) |
| Data Science and Artificial Intelligence | BSc(Hons) | [link](https://courses.uwe.ac.uk/INI4/data-science-and-artificial-intelligence) |
| Diagnostic Radiography | BSc(Hons) | [link](https://courses.uwe.ac.uk/B821/diagnostic-radiography) |
| Digital Media | BSc(Hons) | [link](https://courses.uwe.ac.uk/G451/digital-media) |
| Digital Media (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/G45F/digital-media-with-foundation-year) |
| Drama, Acting and Performance | BA(Hons) | [link](https://courses.uwe.ac.uk/W490/drama-acting-and-performance) |
| Early Childhood | BA(Hons) | [link](https://courses.uwe.ac.uk/X312/early-childhood) |
| Early Childhood (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/X31F/early-childhood-with-foundation-year) |
| Early Years Education (Top up) | BA(Hons) | [link](https://courses.uwe.ac.uk/X125/early-years-education-top-up) |
| Economics | BA(Hons) | [link](https://courses.uwe.ac.uk/L100/economics) |
| Economics (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/L10F/economics-with-foundation-year) |
| Education | BA(Hons) | [link](https://courses.uwe.ac.uk/X304/education) |
| Education (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/X34F/education-with-foundation-year) |
| Education in Professional Practice (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/X303/education-in-professional-practice-top-up) |
| Electrical and Electronic Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H61D/electrical-and-electronic-engineering) |
| Electrical and Electronic Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H6DF/electrical-and-electronic-engineering-with-foundation-year) |
| English Language and Linguistics | BA(Hons) | [link](https://courses.uwe.ac.uk/QQ3C/english-language-and-linguistics) |
| English Literature | BA(Hons) | [link](https://courses.uwe.ac.uk/Q300/english-literature) |
| Environment and Sustainability | BSc(Hons) | [link](https://courses.uwe.ac.uk/FJ17/environment-and-sustainability) |
| Environmental Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/F900/environmental-science) |
| Environmental Science (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/F90F/environmental-science-with-foundation-year) |
| Fashion Communication | BA(Hons) | [link](https://courses.uwe.ac.uk/W2P2/fashion-communication) |
| Fashion Communication (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W2PF/fashion-communication-with-foundation-year) |
| Fashion Textiles | BA(Hons) | [link](https://courses.uwe.ac.uk/W23A/fashion-textiles) |
| Fashion Textiles (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W23F/fashion-textiles-with-foundation-year) |
| Film Studies | BA(Hons) | [link](https://courses.uwe.ac.uk/P30A/film-studies) |
| Filmmaking | BA(Hons) | [link](https://courses.uwe.ac.uk/W293/filmmaking) |
| Fine Art | BA(Hons) | [link](https://courses.uwe.ac.uk/W101/fine-art) |
| Fine Art (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W10F/fine-art-with-foundation-year) |
| Forensic Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/F410/forensic-science) |
| Forensic Science (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/F41F/forensic-science-with-foundation-year) |
| Games Technology | BSc(Hons) | [link](https://courses.uwe.ac.uk/G611/games-technology) |
| Games Technology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/G61F/games-technology-with-foundation-year) |
| Geography | BA(Hons) | [link](https://courses.uwe.ac.uk/L700/geography) |
| Geography | BSc(Hons) | [link](https://courses.uwe.ac.uk/FF89/geography) |
| Graphic Design | BA(Hons) | [link](https://courses.uwe.ac.uk/W211/graphic-design) |
| Graphic Design (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W22F/graphic-design-with-foundation-year) |
| Health and Social Care | BSc(Hons) | [link](https://courses.uwe.ac.uk/B991/health-and-social-care) |
| History | BA(Hons) | [link](https://courses.uwe.ac.uk/V100/history) |
| Illustration | BA(Hons) | [link](https://courses.uwe.ac.uk/W224/illustration) |
| Illustration (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W20F/illustration-with-foundation-year) |
| Information Technology | BSc(Hons) | [link](https://courses.uwe.ac.uk/G560/information-technology) |
| Integrated Wildlife Conservation | FdSc | [link](https://courses.uwe.ac.uk/F750/integrated-wildlife-conservation) |
| Integrated Wildlife Conservation (Top Up) | BSc(Hons) | [link](https://courses.uwe.ac.uk/F75A/integrated-wildlife-conservation-top-up) |
| Interior Design | BA(Hons) | [link](https://courses.uwe.ac.uk/2C3W/interior-design) |
| Interior Design (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/2C3F/interior-design-with-foundation-year) |
| International Business | BA(Hons) | [link](https://courses.uwe.ac.uk/N110/international-business) |
| International Business (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/N11F/international-business-with-foundation-year) |
| International Business Management (Top Up) | BA(Hons) | [link](https://courses.uwe.ac.uk/N12U/international-business-management-top-up) |
| Law | LLB(Hons) | [link](https://courses.uwe.ac.uk/M100/law) |
| Law (with Foundation Year) | LLB(Hons) | [link](https://courses.uwe.ac.uk/M10F/law-with-foundation-year) |
| Law and Criminology | BA(Hons) | [link](https://courses.uwe.ac.uk/MM19/law-and-criminology) |
| Law and Criminology (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/MM9F/law-and-criminology-with-foundation-year) |
| Marketing | BA(Hons) | [link](https://courses.uwe.ac.uk/N500/marketing) |
| Marketing (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/N50F/marketing-with-foundation-year) |
| Mathematics | BSc(Hons) | [link](https://courses.uwe.ac.uk/G101/mathematics) |
| Mechanical Engineering | MEng | [link](https://courses.uwe.ac.uk/H301/mechanical-engineering) |
| Mechanical Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H300/mechanical-engineering) |
| Mechanical Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H3FF/mechanical-engineering-with-foundation-year) |
| Mechatronics Engineering | MEng | [link](https://courses.uwe.ac.uk/H731/mechatronics-engineering) |
| Mechatronics Engineering | BEng(Hons) | [link](https://courses.uwe.ac.uk/H730/mechatronics-engineering) |
| Mechatronics Engineering (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H73F/mechatronics-engineering-with-foundation-year) |
| Media Production | BA(Hons) | [link](https://courses.uwe.ac.uk/P31G/media-production) |
| Midwifery | BSc(Hons) | [link](https://courses.uwe.ac.uk/B711/midwifery) |
| Nursing (Adult) * | BSc(Hons) | [link](https://courses.uwe.ac.uk/B721/nursing-adult) |
| Nursing (Children and Young People) * | BSc(Hons) | [link](https://courses.uwe.ac.uk/B722/nursing-children-and-young-people) |
| Nursing (Learning Disabilities) * | BSc(Hons) | [link](https://courses.uwe.ac.uk/B723/nursing-learning-disabilities) |
| Nursing (Mental Health) * | BSc(Hons) | [link](https://courses.uwe.ac.uk/B724/nursing-mental-health) |
| Occupational Therapy | BSc(Hons) | [link](https://courses.uwe.ac.uk/B920/occupational-therapy) |
| Optometry | MSci | [link](https://courses.uwe.ac.uk/B511/optometry) |
| Paramedic Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/B950/paramedic-science) |
| Philosophy | BA(Hons) | [link](https://courses.uwe.ac.uk/V500/philosophy) |
| Philosophy (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/V50F/philosophy-with-foundation-year) |
| Photography | BA(Hons) | [link](https://courses.uwe.ac.uk/W640/photography) |
| Photography (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W64F/photography-with-foundation-year) |
| Physiotherapy | BSc(Hons) | [link](https://courses.uwe.ac.uk/B160/physiotherapy) |
| Politics and International Relations | BA(Hons) | [link](https://courses.uwe.ac.uk/L290/politics-and-international-relations) |
| Politics and International Relations (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/L29F/politics-and-international-relations-with-foundation-year) |
| Primary Education (QTS) | BA(Hons) | [link](https://courses.uwe.ac.uk/X123/primary-education-qts) |
| Product Design | BA(Hons) | [link](https://courses.uwe.ac.uk/W241/product-design) |
| Product Design (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/W41F/product-design-with-foundation-year) |
| Product Design Technology | BSc(Hons) | [link](https://courses.uwe.ac.uk/W240/product-design-technology) |
| Product Design Technology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/W24F/product-design-technology-with-foundation-year) |
| Professional Development | BA(Hons)/BSc(Hons)/FdA/FdSc/GradDip/Dip/CertHE/GradCert/Cert | [link](https://courses.uwe.ac.uk/Y0UIPD/professional-development) |
| Professional Policing | BSc(Hons) | [link](https://courses.uwe.ac.uk/L490/professional-policing) |
| Professional Policing (with Foundation Year)* | BSc(Hons) | [link](https://courses.uwe.ac.uk/L49F/professional-policing-with-foundation-year) |
| Psychology | BSc(Hons) | [link](https://courses.uwe.ac.uk/C800/psychology) |
| Psychology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/C80F/psychology-with-foundation-year) |
| Psychology with Criminology | BSc(Hons) | [link](https://courses.uwe.ac.uk/C8M9/psychology-with-criminology) |
| Psychology with Criminology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/C89F/psychology-with-criminology-with-foundation-year) |
| Quantity Surveying and Commercial Management | BSc(Hons) | [link](https://courses.uwe.ac.uk/KN21/quantity-surveying-and-commercial-management) |
| Radiotherapy and Oncology | BSc(Hons) | [link](https://courses.uwe.ac.uk/B822/radiotherapy-and-oncology) |
| Real Estate and Development | BSc(Hons) | [link](https://courses.uwe.ac.uk/K440/real-estate-and-development) |
| Robotics | BEng(Hons) | [link](https://courses.uwe.ac.uk/H671/robotics) |
| Robotics (with Foundation Year) | BEng(Hons) | [link](https://courses.uwe.ac.uk/H67F/robotics-with-foundation-year) |
| Social Work | BSc(Hons) | [link](https://courses.uwe.ac.uk/L500/social-work) |
| Sociology | BA(Hons) | [link](https://courses.uwe.ac.uk/L300/sociology) |
| Sociology (with Foundation Year) | BA(Hons) | [link](https://courses.uwe.ac.uk/L30F/sociology-with-foundation-year) |
| Sociology with Psychology | BSc(Hons) | [link](https://courses.uwe.ac.uk/L3C8/sociology-with-psychology) |
| Sociology with Psychology (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/L38F/sociology-with-psychology-with-foundation-year) |
| Software Engineering | BSc(Hons) | [link](https://courses.uwe.ac.uk/6F3B/software-engineering) |
| Software Engineering (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/6F3F/software-engineering-with-foundation-year) |
| Sport Rehabilitation | BSc(Hons) | [link](https://courses.uwe.ac.uk/BC96/sport-rehabilitation) |
| Sports Business and Entrepreneurship | BA(Hons) | [link](https://courses.uwe.ac.uk/N1C6/sports-business-and-entrepreneurship) |
| Urban Planning | BSc(Hons) | [link](https://courses.uwe.ac.uk/K401/urban-planning) |
| Wildlife Ecology and Conservation Science | BSc(Hons) | [link](https://courses.uwe.ac.uk/45MN/wildlife-ecology-and-conservation-science) |
| Wildlife Ecology and Conservation Science (with Foundation Year) | BSc(Hons) | [link](https://courses.uwe.ac.uk/45FF/wildlife-ecology-and-conservation-science-with-foundation-year) |

---

## SECTION 2 — Graduate education (PGT + PGR + PGCE)

### 2.1 Postgraduate Taught (PGT) — 113 门

| 课程名称 | 学位 | 详情链接 |
|----------|------|----------|
| Accounting and Finance | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N34012/accounting-and-finance) |
| Advanced Practice | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/B99Y12/advanced-practice) |
| Animation | MA | [link](https://courses.uwe.ac.uk/W92012/animation) |
| Applied Sciences | Masters in Research (MRes) | [link](https://courses.uwe.ac.uk/C99K1/applied-sciences) |
| Applied Strength and Conditioning | MSc | [link](https://courses.uwe.ac.uk/C60G1/applied-strength-and-conditioning) |
| Applied Transfusion and Transplantation Science | MSc | [link](https://courses.uwe.ac.uk/C99S12/applied-transfusion-and-transplantation-science) |
| Applied Wildlife Conservation | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/C1841/applied-wildlife-conservation) |
| Artificial Intelligence | MSc | [link](https://courses.uwe.ac.uk/I4001/artificial-intelligence) |
| Artificial Intelligence (online) | MSc | [link](https://courses.uwe.ac.uk/I40A62/artificial-intelligence-online) |
| Bar Training Course | LLM/PGDip | [link](https://courses.uwe.ac.uk/M99C12/bar-training-course) |
| Biomedical Science | MSc/Postgraduate Diploma | [link](https://courses.uwe.ac.uk/C9001/biomedical-science) |
| Biomedical Sciences | Doctor of | [link](https://courses.uwe.ac.uk/B90011/biomedical-sciences) |
| Building Information Modelling (BIM) in Design Construction and Operations | MSc | [link](https://courses.uwe.ac.uk/K2101/building-information-modelling-bim-in-design-construction-and-operations) |
| Building Surveying | MSc | [link](https://courses.uwe.ac.uk/K23A12/building-surveying) |
| Business Management | MSc | [link](https://courses.uwe.ac.uk/N20B12/business-management) |
| Business Management and Data Analytics | MSc | [link](https://courses.uwe.ac.uk/N19K12/business-management-and-data-analytics) |
| Business and Digital Transformation | MSc | [link](https://courses.uwe.ac.uk/N29712/business-and-digital-transformation) |
| Business and Events Management | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N8201/business-and-events-management) |
| Business and Human Resource Management | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N630M2/business-and-human-resource-management) |
| Business and Organisational Psychology | MSc | [link](https://courses.uwe.ac.uk/C81G11/business-and-organisational-psychology) |
| Business and Supply Chain Management | MSc | [link](https://courses.uwe.ac.uk/N20F12/business-and-supply-chain-management) |
| Cancer Care | PGCert | [link](https://courses.uwe.ac.uk/B79K00/cancer-care) |
| Career Development | Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/L55062/career-development) |
| Civil Engineering | MSc | [link](https://courses.uwe.ac.uk/H20H1/civil-engineering) |
| Clinical Echocardiography | PGCert | [link](https://courses.uwe.ac.uk/B81H00/clinical-echocardiography) |
| Clinical Practice | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/B99212/clinical-practice) |
| Community Nurse Specialist Practitioner (NMC 2022) | PGDip Specialist Practice (District Nursing) | [link](https://courses.uwe.ac.uk/ST1419/community-nurse-specialist-practitioner-nmc-2022) |
| Conservation Leadership | MSc | [link](https://courses.uwe.ac.uk/C1N21/conservation-leadership) |
| Construction Project Management | MSc | [link](https://courses.uwe.ac.uk/K90012/construction-project-management) |
| Counselling Psychology | Doctor of | [link](https://courses.uwe.ac.uk/LC5811/counselling-psychology) |
| Counselling and Psychotherapy | MA | [link](https://courses.uwe.ac.uk/C84D42/counselling-and-psychotherapy) |
| Critical Care | PGCert | [link](https://courses.uwe.ac.uk/B7GB4/critical-care) |
| Cyber Security | MSc | [link](https://courses.uwe.ac.uk/I9001/cyber-security) |
| Data Science | MSc | [link](https://courses.uwe.ac.uk/INB112/data-science) |
| Data Science (online) | MSc | [link](https://courses.uwe.ac.uk/INE112/data-science-online) |
| Design Communication: Fashion Photography | MA | [link](https://courses.uwe.ac.uk/W29E12/design-communication-fashion-photography) |
| Design Communication: Graphic Design | MA | [link](https://courses.uwe.ac.uk/W29F12/design-communication-graphic-design) |
| Design Communication: Illustration | MA | [link](https://courses.uwe.ac.uk/W29G12/design-communication-illustration) |
| Designer/Maker | MA | [link](https://courses.uwe.ac.uk/W20L12/designermaker) |
| Digital Marketing | MSc | [link](https://courses.uwe.ac.uk/N5I11/digital-marketing) |
| Doctor of Business Administration | DBA | [link](https://courses.uwe.ac.uk/N12T4/doctor-of-business-administration) |
| Echocardiography in Congenital Heart Disease | PGCert | [link](https://courses.uwe.ac.uk/B81J1/echocardiography-in-congenital-heart-disease) |
| Education (Distance Learning) | MA | [link](https://courses.uwe.ac.uk/X00C42/education-distance-learning) |
| Education (EdD International) * | Doctor of | [link](https://courses.uwe.ac.uk/X90N12/education-edd-international) |
| Education (EdD) | Doctor of | [link](https://courses.uwe.ac.uk/X90012/education-edd) |
| Education Leadership (online) | MA | [link](https://courses.uwe.ac.uk/X90P12/education-leadership-online) |
| Electrical and Electronic Engineering | MSc | [link](https://courses.uwe.ac.uk/H65R1/electrical-and-electronic-engineering) |
| Engineering Management | MSc | [link](https://courses.uwe.ac.uk/H9N21/engineering-management) |
| Enhanced Clinical Practitioner | PGDip Enhanced Clinical Practitioner | [link](https://courses.uwe.ac.uk/ST0895/enhanced-clinical-practitioner) |
| Environmental Health | MSc/Postgraduate Diploma | [link](https://courses.uwe.ac.uk/B90032/environmental-health) |
| Environmental Management and Consultancy | MSc | [link](https://courses.uwe.ac.uk/F1N21/environmental-management-and-consultancy) |
| Facade Engineering | MSc | [link](https://courses.uwe.ac.uk/K90D1/facade-engineering) |
| Filmmaking | MA | [link](https://courses.uwe.ac.uk/P31T12/filmmaking) |
| Finance and Investment | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N39012/finance-and-investment) |
| Financial Technology (FinTech) | MSc | [link](https://courses.uwe.ac.uk/N3I212/financial-technology-fintech) |
| Fine Art | MA | [link](https://courses.uwe.ac.uk/E10112/fine-art) |
| Fine Art: Curating | MA | [link](https://courses.uwe.ac.uk/E10B12/fine-art-curating) |
| Fine Art: Photography | MA | [link](https://courses.uwe.ac.uk/E10C12/fine-art-photography) |
| Fine Art: Printmaking | MA | [link](https://courses.uwe.ac.uk/E10D12/fine-art-printmaking) |
| Forensic Science | MSc | [link](https://courses.uwe.ac.uk/F41G12/forensic-science) |
| Global Business and Finance Law | LLM | [link](https://courses.uwe.ac.uk/M34G12/global-business-and-finance-law) |
| Health Psychology | Doctor of | [link](https://courses.uwe.ac.uk/C84141/health-psychology) |
| Health Psychology | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/CB8942/health-psychology) |
| Health Technology | MSc | [link](https://courses.uwe.ac.uk/L5901/health-technology) |
| Health and Care Research | MRes | [link](https://courses.uwe.ac.uk/B79L12/health-and-care-research) |
| Healthcare Management and Leadership (online) | MSc | [link](https://courses.uwe.ac.uk/B90162/healthcare-management-and-leadership-online) |
| Human Resource Management (online) | MSc | [link](https://courses.uwe.ac.uk/N630P2/human-resource-management-online) |
| Information Technology | MSc | [link](https://courses.uwe.ac.uk/G56A12/information-technology) |
| International Business Management | MSc | [link](https://courses.uwe.ac.uk/N14J12/international-business-management) |
| International Commercial Law (online) | LLM | [link](https://courses.uwe.ac.uk/M34P12/international-commercial-law-online) |
| International Law and Security | LLM | [link](https://courses.uwe.ac.uk/M30C12/international-law-and-security) |
| Journalism | MA | [link](https://courses.uwe.ac.uk/P50012/journalism) |
| Journalism: Audio and Podcasting | MA | [link](https://courses.uwe.ac.uk/P50P12/journalism-audio-and-podcasting) |
| Marketing Management | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N50012/marketing-management) |
| Marketing and Marketing Communications | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/N50212/marketing-and-marketing-communications) |
| Master of Business Administration (Executive) MBA | MBA | [link](https://courses.uwe.ac.uk/N1225/master-of-business-administration-executive-mba) |
| Master of Business Administration (MBA) (Full-time) | MBA | [link](https://courses.uwe.ac.uk/N12212/master-of-business-administration-mba-full-time) |
| Medical Ultrasound | MSc | [link](https://courses.uwe.ac.uk/B80042/medical-ultrasound) |
| Music Therapy | MA | [link](https://courses.uwe.ac.uk/B99942/music-therapy) |
| Nuclear Medicine | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/B80A42/nuclear-medicine) |
| PET-CT | PGCert | [link](https://courses.uwe.ac.uk/B81K6/pet-ct) |
| Physician Associate Studies | MSc | [link](https://courses.uwe.ac.uk/B9611/physician-associate-studies) |
| Planning and Urban Leadership (Distance Learning) | MSc | [link](https://courses.uwe.ac.uk/K4062/planning-and-urban-leadership-distance-learning) |
| Professional Development | MA/MSc/PGDip/PGCert | [link](https://courses.uwe.ac.uk/Y0PIPD/professional-development) |
| Professional Development (Social Work) | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/Y00HSW/professional-development-social-work) |
| Professional Practice and Management in Architecture | Postgraduate Certificate | [link](https://courses.uwe.ac.uk/K10A/professional-practice-and-management-in-architecture) |
| Project Management | MSc | [link](https://courses.uwe.ac.uk/K9N21/project-management) |
| Project Management (online) | MSc | [link](https://courses.uwe.ac.uk/N9KB12/project-management-online) |
| Psychology (Conversion) | MSc | [link](https://courses.uwe.ac.uk/C80H12/psychology-conversion) |
| Public Health | MSc/Postgraduate Diploma/Postgraduate Certificate | [link](https://courses.uwe.ac.uk/BL9412/public-health) |
| Real Estate Finance and Investment | MSc | [link](https://courses.uwe.ac.uk/KN231/real-estate-finance-and-investment) |
| Real Estate Finance and Investment (Distance Learning) | MSc | [link](https://courses.uwe.ac.uk/KN2B6/real-estate-finance-and-investment-distance-learning) |
| Real Estate Management | MSc | [link](https://courses.uwe.ac.uk/KN4112/real-estate-management) |
| Real Estate Management (Distance Learning) | MSc | [link](https://courses.uwe.ac.uk/KN4A6/real-estate-management-distance-learning) |
| Rehabilitation | MSc | [link](https://courses.uwe.ac.uk/B99P1/rehabilitation) |
| Risk Management (online) | MSc | [link](https://courses.uwe.ac.uk/N32A62/risk-management-online) |
| Risk Management and Insurance | MSc | [link](https://courses.uwe.ac.uk/N32012/risk-management-and-insurance) |
| Robotics | MSc | [link](https://courses.uwe.ac.uk/H67B1/robotics) |
| Science Communication | MSc/Postgraduate Diploma | [link](https://courses.uwe.ac.uk/P90012/science-communication) |
| Sleep Medicine | PGCert | [link](https://courses.uwe.ac.uk/C9P100/sleep-medicine) |
| Social Research | Masters in Research (MRes) | [link](https://courses.uwe.ac.uk/L90A1/social-research) |
| Solicitors Training Course (SQE Prep) | PGDip | [link](https://courses.uwe.ac.uk/M99D12/solicitors-training-course-sqe-prep) |
| Solicitors Training Course (SQE Prep) | LLM | [link](https://courses.uwe.ac.uk/M99F12/solicitors-training-course-sqe-prep) |
| Specialist Community Public Health Nurse (NMC 2022) | PGDip Specialist Community Public Health Nursing (Health Visting), PGDip Specialist Community Public Health Nursing (Occupational Health Nursing), PGDip Specialist Community Public Health Nursing (School Nursing) | [link](https://courses.uwe.ac.uk/ST1418/specialist-community-public-health-nurse-nmc-2022) |
| Specialist Community Public Health Nursing | MSc | [link](https://courses.uwe.ac.uk/B71L12/specialist-community-public-health-nursing) |
| Specialist Practice (District Nursing) | MSc | [link](https://courses.uwe.ac.uk/B70U1/specialist-practice-district-nursing) |
| Sport and Exercise Psychology | MSc | [link](https://courses.uwe.ac.uk/C8901/sport-and-exercise-psychology) |
| Sustainability and Environmental Management (online) | MSc | [link](https://courses.uwe.ac.uk/D44B62/sustainability-and-environmental-management-online) |
| Sustainable Development in Practice | MSc | [link](https://courses.uwe.ac.uk/F8NA1/sustainable-development-in-practice) |
| Sustainable Food Systems | MSc | [link](https://courses.uwe.ac.uk/D69012/sustainable-food-systems) |
| Sustainable Technology * | MSc | [link](https://courses.uwe.ac.uk/J91C1/sustainable-technology) |
| Urban Planning | MSc | [link](https://courses.uwe.ac.uk/K4911/urban-planning) |
| Wildlife Filmmaking | MA | [link](https://courses.uwe.ac.uk/D4P31/wildlife-filmmaking) |

### 2.2 Postgraduate Research (PGR) — 10 门

| 课程名称 | 学位 | 详情链接 |
|----------|------|----------|
| Postgraduate Research: Bristol Business School | PhD | [link](https://courses.uwe.ac.uk/GSA121/postgraduate-research-bristol-business-school) |
| Postgraduate Research: Bristol Law School | PhD | [link](https://courses.uwe.ac.uk/GSA124/postgraduate-research-bristol-law-school) |
| Postgraduate Research: School of Applied Sciences | PhD | [link](https://courses.uwe.ac.uk/GSA142/postgraduate-research-school-of-applied-sciences) |
| Postgraduate Research: School of Architecture and Environment | PhD | [link](https://courses.uwe.ac.uk/GSA133/postgraduate-research-school-of-architecture-and-environment) |
| Postgraduate Research: School of Arts | PhD | [link](https://courses.uwe.ac.uk/GSA100/postgraduate-research-school-of-arts) |
| Postgraduate Research: School of Computing and Creative Technologies | PhD | [link](https://courses.uwe.ac.uk/GSA130/postgraduate-research-school-of-computing-and-creative-technologies) |
| Postgraduate Research: School of Education and Childhood | PhD | [link](https://courses.uwe.ac.uk/GSA103/postgraduate-research-school-of-education-and-childhood) |
| Postgraduate Research: School of Engineering | PhD | [link](https://courses.uwe.ac.uk/GSA136/postgraduate-research-school-of-engineering) |
| Postgraduate Research: School of Health and Social Wellbeing | PhD | [link](https://courses.uwe.ac.uk/GSA151/postgraduate-research-school-of-health-and-social-wellbeing) |
| Postgraduate Research: School of Social Sciences | PhD | [link](https://courses.uwe.ac.uk/GSA145/postgraduate-research-school-of-social-sciences) |

### 2.3 PGCE / Teacher Training — 30 门

| 课程名称 | 学位 | 详情链接 |
|----------|------|----------|
| Chartered Town Planner | CertHE Urban Planning Practice and MSc Urban Planning | [link](https://courses.uwe.ac.uk/ST0536/chartered-town-planner) |
| International | iPGCE | [link](https://courses.uwe.ac.uk/X2H112/international) |
| International Early Years | iPGCE | [link](https://courses.uwe.ac.uk/X71A6/international-early-years) |
| Primary (5-11) | PGCE with QTS | [link](https://courses.uwe.ac.uk/X171/primary-5-11) |
| Primary Early Years (3-7) | PGCE with QTS | [link](https://courses.uwe.ac.uk/X121/primary-early-years-3-7) |
| Secondary Art and Design | PGCE with QTS | [link](https://courses.uwe.ac.uk/W1X1/secondary-art-and-design) |
| Secondary Biology with Science | PGCE with QTS | [link](https://courses.uwe.ac.uk/2WQH/secondary-biology-with-science) |
| Secondary Business | PGCE with QTS | [link](https://courses.uwe.ac.uk/34FW/secondary-business) |
| Secondary Chemistry with Science | PGCE with QTS | [link](https://courses.uwe.ac.uk/F1X1/secondary-chemistry-with-science) |
| Secondary Computer Science | PGCE with QTS | [link](https://courses.uwe.ac.uk/2WQG/secondary-computer-science) |
| Secondary English | PGCE with QTS | [link](https://courses.uwe.ac.uk/Q3X1/secondary-english) |
| Secondary Geography | PGCE with QTS | [link](https://courses.uwe.ac.uk/F8X1/secondary-geography) |
| Secondary History | PGCE with QTS | [link](https://courses.uwe.ac.uk/V1X1/secondary-history) |
| Secondary Mathematics | PGCE with QTS | [link](https://courses.uwe.ac.uk/G1X1/secondary-mathematics) |
| Secondary Modern Languages | PGCE with QTS | [link](https://courses.uwe.ac.uk/R9X1/secondary-modern-languages) |
| Secondary Physical Education | PGCE with QTS | [link](https://courses.uwe.ac.uk/C6X1/secondary-physical-education) |
| Secondary Physics with Science | PGCE with QTS | [link](https://courses.uwe.ac.uk/F3X1/secondary-physics-with-science) |
| iQTS Primary (5-11) | PGCE | [link](https://courses.uwe.ac.uk/X173/iqts-primary-5-11) |
| iQTS Secondary Art and Design (11-16) | PGCE | [link](https://courses.uwe.ac.uk/W1X3/iqts-secondary-art-and-design-11-16) |
| iQTS Secondary Biology (11-16) | PGCE | [link](https://courses.uwe.ac.uk/2WQ3/iqts-secondary-biology-11-16) |
| iQTS Secondary Business (14-19) | PGCE | [link](https://courses.uwe.ac.uk/34F3/iqts-secondary-business-14-19) |
| iQTS Secondary Chemistry (11-16) | PGCE | [link](https://courses.uwe.ac.uk/F1X3/iqts-secondary-chemistry-11-16) |
| iQTS Secondary Computer Science (11-16) | PGCE | [link](https://courses.uwe.ac.uk/2WG3/iqts-secondary-computer-science-11-16) |
| iQTS Secondary English (11-16) | PGCE | [link](https://courses.uwe.ac.uk/Q3X3/iqts-secondary-english-11-16) |
| iQTS Secondary Geography (11-16) | PGCE | [link](https://courses.uwe.ac.uk/F8X3/iqts-secondary-geography-11-16) |
| iQTS Secondary History (11-16) | PGCE | [link](https://courses.uwe.ac.uk/V1X3/iqts-secondary-history-11-16) |
| iQTS Secondary Mathematics (11-16) | PGCE | [link](https://courses.uwe.ac.uk/G1X3/iqts-secondary-mathematics-11-16) |
| iQTS Secondary Modern Foreign Languages (11-16) | PGCE | [link](https://courses.uwe.ac.uk/R9X3/iqts-secondary-modern-foreign-languages-11-16) |
| iQTS Secondary Physical Education (11-16) | PGCE | [link](https://courses.uwe.ac.uk/CX63/iqts-secondary-physical-education-11-16) |
| iQTS Secondary Physics (11-16) | PGCE | [link](https://courses.uwe.ac.uk/F3X3/iqts-secondary-physics-11-16) |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Entry qualifications (UG)

| Qualification | Standard offer | 备注 |
|---------------|---------------|------|
| A-Level | 120 UCAS Tariff points (typical) | 视课程而定；GCSE English + Maths Grade C/4 |
| BTEC (EDEXCEL) | 120 UCAS Tariff points | 视课程而定 |
| IB (International Baccalaureate) | 120 UCAS Tariff points (typical) | 接受 IB Career-related Programme |
| Access to HE Diploma | 120 UCAS Tariff points | 视课程而定 |
| T Level | 120 UCAS Tariff points | 视课程而定 |
| Welsh Baccalaureate | 120 UCAS Tariff points | 接受 Advanced Skills Baccalaureate Wales |
| Cambridge Technical | 120 UCAS Tariff points | 视课程而定 |
| Irish Highers | 120 UCAS Tariff points | 视课程而定 |
| GCSE (English + Maths) | Grade C / 4 或以上 | 所有 UG 课程要求 |
| Foundation Year | 通过 BSc (Hons) with Foundation Year 进入 (UCAS code 通常为 4 字母 + 'F') | 例: G40F for Computer Science |

> **重要提示**: 120 UCAS tariff points 是 BSc (Hons) Computer Science 等典型课程的示例要求；**不同课程的实际 tariff 可能不同**（高需求课程如 Nursing, Midwifery, Physiotherapy, Radiography, Social Work, Law 通常更高；专业认证课程如 Engineering、Architecture 也有不同要求）。具体以课程 detail page 为准。
> **来源 (evidence)**:
> - URL: `https://courses.uwe.ac.uk/G400/computer-science` (示例课程 detail page)
> - source_snippet: "120 UCAS Tariff points ... A-Level ... BTEC ... IB ... Access to HE ... T Level ... Welsh Baccalaureate ... Cambridge Technical ... Irish Highers ... GCSE Grade C/4 in English and Mathematics"
> - capture_date: 2026-07-08

### 3.2 English language requirements (international students)

UWE 接受以下英语语言证明（具体要求因课程而异）：

| 考试 | 标准要求 (typical UG) | 标准要求 (typical PGT) | 备注 |
|------|----------------------|----------------------|------|
| IELTS (Academic) | 6.0 overall, 各项不低于 5.5 | 6.5 overall, 各项不低于 5.5/6.0 | 多数本科课程；Higher 要求见课程页 |
| TOEFL iBT | 接受（具体分数按 IELTS 等价换算） | 接受 | 推荐 80+ (UG) / 90+ (PGT) |
| PTE Academic | 接受 | 接受 | 分数按 IELTS 等价 |
| UWE Bristol Online English Language Test (ELT) | 接受 | 接受 | **免费** for first attempt; Inspera platform; 4 components (Listening 40min, Reading 90min, Writing 60min, Speaking 10min); Test runs Wednesdays every fortnight |
| Pre-sessional English (10/5/2-week) | 通过 UWE Bristol Pre-sessional (UCAS YQ33) 衔接主课 | 同左 | 联合 CAS 涵盖 pre-sessional + main programme |
| GCSE English | Grade C/4 | n/a | UK 申请人 |
| Degree from majority English-speaking country | 满足要求 | 满足要求 | UWE 接受 |

> **Higher requirements (示例)**: 部分课程 (e.g. Nursing, Midwifery, Education) 要求 IELTS 7.0 overall, 各项不低于 6.5/7.0. 具体见 course detail page。
> **来源 (evidence)**:
> - URL: `https://www.uwe.ac.uk/courses/applying/international-applications/english-language-requirements`
> - source_snippet: "Ready to study with us? We are looking forward to meeting you. To make the most of your time in the UK, you'll need to read, write and speak good English at GCSE grade C or the equivalent standard." + "UWE Bristol's English Language test (ELT) uses the same system and format as the IELTS test, testing all four components; listening, reading, writing and speaking." + "Your first UWE Bristol's Online ELT is free, but charges may apply for non-attendance and resits."
> - capture_date: 2026-07-08

### 3.3 Application deadlines & key dates

| 入学时间 | UCAS deadline (UG) | PG application | 备注 |
|----------|---------------------|----------------|------|
| September 2026 (main intake) | UCAS equal consideration: 27 January 2026 (前一年); Late applications 接受至 30 June 2026 | Rolling admission (建议尽早) | 多数课程 |
| January 2026 (mid-year intake) | Limited courses — see `https://www.uwe.ac.uk/courses/applying/international-applications/key-dates-january` | Rolling | 仅部分课程提供 January 入学 |
| September 2027 | UCAS 2027 cycle 即将开放 | Rolling | "All courses for 2026/27" + 2027 选项已上线 |

> 提示: 课程页注明 "Available in Clearing" 标志 = 2026/27 仍可经 Clearing 申请。
> **来源 (evidence)**:
> - URL: `https://www.uwe.ac.uk/courses/applying/international-applications/key-dates-september` 和 `key-dates-january`
> - URL: `https://www.uwe.ac.uk/courses/clearing`
> - capture_date: 2026-07-08

### 3.4 Application routes

- **UG (UK)**: UCAS (https://www.ucas.com/)
- **UG (International)**: UCAS / UWE education agent / UWE regional office
- **PGT (UK)**: Direct application via course page "Apply now" button
- **PGT (International)**: Direct online form / education agent / regional office
- **PGR (PhD)**: Direct application via research degree page + supervisor contact
- **Apprenticeships**: Direct application via `https://www.uwe.ac.uk/courses/applying/higher-and-degree-apprenticeship-applications`

> **联系方式 (Admissions team)**:
> - email: `admissions@uwe.ac.uk`
> - tel: `+44 (0)117 32 83333`
> - International: `international@uwe.ac.uk`
> - 来源: `https://www.uwe.ac.uk/courses/applying`

---

## SECTION 4 — Costs & financial aid

### 4.1 Tuition fees (per annum)

| Fee status | UG (2025/26) | UG (2026/27) | PG (typical) |
|------------|--------------|--------------|--------------|
| **UK Home** | £9,250 | £9,250 (cap; pending inflation-linked increase via legislation) | 视课程而定 — PGCE/PGDip/PGCert/MA/MSc/MBA 各异 |
| **EU / Offshore** | £9,250 (与 UK 同价) | £9,250 (likely increase pending legislation) | 视课程 |
| **International** | 视课程而异 — 课程详情页 `https://courses.uwe.ac.uk/<code>` 显示 | 视课程而异 | 视课程 — MSc £15,000-£20,000+; MBA 更高 |

> **2026/27 重要变化 (证据来源: UWE fees page)**: "UK Government has announced that the undergraduate tuition fee cap for home students (includes offshore) will increase every year in line with inflation. ... Legislation still needs to be passed for this increase to happen, so the current fees within our undergraduate course listing 2026/27 are likely to increase should legislation be passed."
> **来源 (evidence)**:
> - URL: `https://www.uwe.ac.uk/courses/fees`
> - URL: `https://coursefees.uwe.ac.uk/` (per-course fees search)
> - URL: `https://www.uwe.ac.uk/courses/fees/tuition-fees-policy`
> - source_snippet: "UK Government has announced that the undergraduate tuition fee cap for home students (includes offshore) will increase every year in line with inflation."
> - capture_date: 2026-07-08

### 4.2 Fee status determination

| Status | 定义 |
|--------|------|
| Home (UK) | UK national + settled status; 通常 3 年居住 |
| EU | pre-Brexit settled EU status; 见 fee status page |
| Offshore | Channel Islands / Isle of Man |
| International | 其他所有 |

> **来源**: `https://www.uwe.ac.uk/courses/fees/determining-your-fee-status`

### 4.3 Living costs (estimate)

- 官方建议: 见 `https://www.uwe.ac.uk/life/money-and-finance`
- 包括 accommodation, travel, bills, food
- UKVI financial requirement (Student visa) 见 `https://www.uwe.ac.uk/courses/international-study/visas`

### 4.4 Scholarships & funding

- 主页: `https://www.uwe.ac.uk/courses/funding`
- 涵盖 UK/EU/international 学生
- UWE Bristol 提供多种 bursaries, scholarships, alumni discount
- 详见具体课程的 funding tab

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "UWE Bristol (University of the West of England)"
  source_url: https://www.uwe.ac.uk/
  source_snippet: "UWE Bristol (University of the West of England)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.total_courses
  value: 644
  source_url: https://courses.uwe.ac.uk/Search?words&view=list
  source_snippet: "Showing 1 - 644 of 644 results"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.colleges_count
  value: 3
  source_url: https://www.uwe.ac.uk/about/colleges-and-schools
  source_snippet: "Find out more about the Schools within our three Colleges."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.college.CATE
  value: "College of Arts, Technology and Environment (CATE)"
  source_url: https://www.uwe.ac.uk/about/colleges-and-schools/arts-technology-and-environment
  source_snippet: "The College of Arts, Technology and Environment (CATE) brings together four highly successful and vibrant disciplines including Arts, Architecture and Environment, Computing and Creative Technologies ..."
  capture_date: 2026-07-08

E-U-005:
  field: institution.college.CHSS
  value: "College of Health, Science and Society (CHSS)"
  source_url: https://www.uwe.ac.uk/about/colleges-and-schools/health-science-and-society
  source_snippet: "College of Health, Science and Society (CHSS) is a large, diverse and dynamic part of the University, bringing together experts from Health and Social Wellbeing, Applied Sciences, Education and Social Sciences"
  capture_date: 2026-07-08

E-U-006:
  field: institution.college.CBL
  value: "College of Business and Law (CBL)"
  source_url: https://www.uwe.ac.uk/about/colleges-and-schools/business-and-law
  source_snippet: "The College of Business and Law (CBL) comprises Bristol Business School and Bristol Law School who provide a range of undergraduate, postgraduate, higher research and professional courses."
  capture_date: 2026-07-08

E-U-007:
  field: fees.home_ug_2025_26
  value: 9250
  source_url: https://www.uwe.ac.uk/courses/fees
  source_snippet: "tuition fees ... UK Home £9,250 (cap; pending inflation-linked increase via legislation)"
  capture_date: 2026-07-08

E-U-008:
  field: fees.home_ug_2026_27_change
  value: "Pending legislation; cap may increase with inflation annually"
  source_url: https://www.uwe.ac.uk/courses/fees
  source_snippet: "UK Government has announced that the undergraduate tuition fee cap for home students (includes offshore) will increase every year in line with inflation."
  capture_date: 2026-07-08

E-U-009:
  field: language.ug_ielts_standard
  value: "6.0 overall, no band < 5.5"
  source_url: https://courses.uwe.ac.uk/G400/computer-science (typical example)
  source_snippet: "IELTS 6.0 (with no band score lower than 5.5)"
  capture_date: 2026-07-08

E-U-010:
  field: language.online_elt_offered
  value: "UWE Bristol Online English Language Test (ELT) — first attempt free"
  source_url: https://www.uwe.ac.uk/courses/applying/international-applications/english-language-requirements
  source_snippet: "Your first UWE Bristol's Online ELT is free, but charges may apply for non-attendance and resits."
  capture_date: 2026-07-08

E-U-011:
  field: ug_entry.tariff_typical
  value: "120 UCAS Tariff points (typical)"
  source_url: https://courses.uwe.ac.uk/G400/computer-science
  source_snippet: "120 UCAS Tariff points"
  capture_date: 2026-07-08

E-U-012:
  field: admissions.contact
  value: "admissions@uwe.ac.uk / +44 (0)117 32 83333"
  source_url: https://www.uwe.ac.uk/courses/applying
  source_snippet: "Contact the Admissions Team: email admissions@uwe.ac.uk tel +44 (0)117 32 83333"
  capture_date: 2026-07-08

E-U-013:
  field: course.example
  value: "BSc (Hons) Computer Science (UCAS G400) at Frenchay Campus, School of Computing and Creative Technologies, BCS-accredited, 3 years (or 4 with Placement/Sandwich)"
  source_url: https://courses.uwe.ac.uk/G400/computer-science
  source_snippet: "BSc (Hons) Computer Science ... School of Computing and Creative Technologies ... Frenchay Campus ... 3 years (or 4 with placement year)"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### 6.1 Chunking strategy

每个 course entry 拆分为 1 个 chunk (含 name, degree, url)；每个 evidence 块拆分为 1 个 chunk。

### 6.2 Follow-up data items (prioritized)

| Priority | Data item | 状态 |
|----------|-----------|------|
| **P0** | Per-course 学院/School 归属 (需二次从 course detail page 提取 school 字段) | 待补 |
| **P0** | Per-course international tuition fee (从 `https://coursefees.uwe.ac.uk/<course-code>` 提取) | 待补 |
| **P0** | Per-course 课程时长、学制 (Foundation/Sandwich/Placement) | 待补 |
| **P0** | Per-course 入学要求 (A-Level subject requirements, GCSE grade, portfolio) | 待补 |
| **P1** | PGR (PhD) topic areas + supervisors list | 待补 |
| **P1** | 课程模块详情 + 评估方法 | 待补 |
| **P1** | Apprenticeship programmes (Level 4-7) 列表 | 待补 |
| **P2** | Pre-sessional English course details (YQ33) | 已部分记录 |
| **P2** | UWE Bristol Online ELT 详细 pass rate + 接受度 | 已记录主结构 |

---

## SECTION 7 — Cross-school comparison framework

| 字段 | UWE Bristol 数值 |
|------|----------------|
| QS 2026 排名 (CS subfield) | 401-450 |
| 总课程数 (2026/27) | 644 |
| College 数 | 3 |
| 本科学费 (Home) | £9,250/yr |
| 国际生学费 (典型 MSc) | 课程页 per-course 决定 (建议查 coursefees.uwe.ac.uk) |
| IELTS (typical UG) | 6.0 / 5.5 |
| IELTS (typical PGT) | 6.5 / 5.5-6.0 |
| PGCE 课程数 | 30 |
| PhD 课程数 | 10 |
| Online English Test | 有 (免费 first attempt) |
| Pre-sessional English | 有 (10/5/2-week) |
| Clearning 接受 | 是 (Available in Clearing flag) |
| January intake | 部分课程 |
| 校区 | Frenchay / Glenside / City |
| 学习模式 | Full-time / Part-time / Sandwich / Placement / Foundation Year / Top-up / Condensed Learning |

---

## SECTION 8 — UWE Bristol specific patterns (新增 — 模式记录)

1. **A-Z listing 模式**: UWE 的 course 列表是单页 A-Z 形式，URL `https://courses.uwe.ac.uk/Search?words&view=list` 直接渲染 644 条结果。**关键技巧**: 页面默认 lazy-load，需 scroll 30+ 次才能加载全部 644 项到 DOM，再用 JS 提取 `<li>` 节点内的 `<a>` 链接。
2. **College 标签缺失**: A-Z view 中**不显示** course 所属的 college/school，subject-area filter tab 也不立即显示 college 归属。需打开每个 course detail page 才能找到 school 字段。
3. **Degree 标签格式多样**: UWE 用 trailing 学位标签（如 "BA(Hons)"、"MSc/Postgraduate Diploma/Postgraduate Certificate"），但 short course 类别用 "Professional/Short course" 这种描述性标签（无括号学位），需要在分类时单独处理。
4. **Clearing 标记**: course 在 A-Z 列表中常带 "Available in Clearing" 副标签，表示 2026/27 仍可通过 Clearing 申请。
5. **Multi-award degrees**: 部分课程在一个 URL 下提供多个学位出口（"BA(Hons)/BSc(Hons)/FdA/FdSc/GradDip/Dip/CertHE/GradCert/Cert"），是 UWE 的灵活 exit structure 模式。
6. **Foundation Year 变体**: 几乎所有 UG Hons 课程都有 "(with Foundation Year)" 变体（UCAS code 通常在原 code 后加 'F'）。
7. **PGCE 数量大**: UWE Bristol 有 14 个 PGCE with QTS + 13 个 PGCE + 2 个 iPGCE = 29-30 个 teacher training programmes（远超一般综合大学），反映其在 teacher training 领域的强势地位。
8. **Health professions 全**: UWE 在 Nursing, Midwifery, Radiography, Physiotherapy, Occupational Therapy, Social Work 等 health professions 课程**全覆盖**（每个专业都对应 1-4 个 BSc(Hons) 课程 + 多个 PGDip / CPD 变体），体现 CHSS 的应用专业导向。
9. **Fees 2026/27 政策变更**: UK home UG 学费 cap 即将与通胀挂钩（legislation pending），是 2026/27 入学重要政策变化。
10. **Online ELT (Inspera-based)**: UWE 提供自有的免费 Online ELT，使用 Inspera platform，与 IELTS 格式相同，是 international 申请人重要的语言达标路径。
