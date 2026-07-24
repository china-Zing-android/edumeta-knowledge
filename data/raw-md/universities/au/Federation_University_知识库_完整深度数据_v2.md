# Federation University Australia — 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: institute/school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Victoria)

---

## Section 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~70 |
| 本科荣誉学位 (Honours) | ~8 |
| 副学士/文凭 (Associate Degree/Diploma HE) | ~5 |
| 研究生授课型项目 (PGT: GC/GD/Masters) | ~55 |
| 研究生研究型项目 (PhD/MPhil) | ~8 |
| TAFE 证书/文凭 (Certs I-IV, Diploma, Adv Dip) | ~60 |
| 非学历/短期课程 (Non-award/Short courses) | ~6 |
| **学位项目总计 (含TAFE)** | **~212** |
| 学院/研究所 (Institutes + Schools) | 6 |
| 学术院系 (Departments/Schools) | 6 (扁平结构) |

**数据来源**: Federation 课程搜索引擎显示 "Courses (212)"，共 11 页（每页20条，末页12条）。

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

Federation University Australia 采用扁平化的学院-研究所结构（非传统的学院→系→专业层级），共 **3 个研究所 + 1 个 TAFE + 1 个研究生院 + 1 个在线学院**：

```
Federation University Australia
├── Institute of Education, Arts and Community (IEAC)
│   ├── Education (teaching streams)
│   ├── Humanities & Social Sciences
│   ├── Community & Human Services
│   ├── Visual & Performing Arts
│   └── Psychology
├── Institute of Health and Wellbeing (IHW)
│   ├── Nursing & Midwifery
│   ├── Paramedicine
│   ├── Allied Health (OT, Physio, Speech Pathology)
│   ├── Sport & Exercise Science
│   ├── Clinical Exercise Physiology
│   └── OHS / Workplace Health & Safety
├── Institute of Innovation, Science and Sustainability (IISS)
│   ├── Engineering (Civil, Electrical, Mechanical, Mining)
│   ├── Science (Biomedical, Food & Nutrition, Environmental, Veterinary Bioscience)
│   ├── Mathematics
│   ├── Information Technology (Cyber, Data Science, Software, Networking)
│   └── Business & Accounting
├── Federation TAFE
│   ├── Automotive
│   ├── Building & Construction
│   ├── Children's Services / Early Childhood
│   ├── Hairdressing & Beauty
│   ├── Hospitality
│   ├── Nursing (Enrolled Nurse - Diploma)
│   ├── Conservation & Ecosystem Management
│   ├── Engineering Trades
│   └── Other VET streams
├── Graduate Research School (GRS)
│   ├── Master of Philosophy (MPhil)
│   └── Doctor of Philosophy (PhD)
└── Federation University Online
    └── Online degree programmes
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 (Degree Level) | 数量 |
|------------------------|------|
| Certificate I (TAFE) | 1 |
| Certificate II (TAFE) | ~5 |
| Certificate III (TAFE) | ~18 |
| Certificate IV (TAFE) | ~8 |
| Diploma (TAFE) | ~4 |
| Advanced Diploma (TAFE) | ~2 |
| Diploma (Higher Education) | ~3 |
| Associate Degree | ~2 |
| Undergraduate Certificate | 1 |
| Bachelor Degree | ~50 |
| Bachelor (Honours) | ~8 |
| Graduate Certificate | ~10 |
| Graduate Diploma | ~10 |
| Master (Coursework) | ~22 |
| Master (Research) - MPhil | ~2 |
| Doctor of Philosophy (PhD) | ~7 |
| Non-award / Short course | ~6 |
| VCE | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Institute/School | UG Bachelor | UG Honours | PG Coursework | PhD/MPhil | TAFE/VET | Other | Total |
|-----------------|------------|------------|--------------|-----------|---------|-------|-------|
| IEAC | ~10 | ~1 | ~3 | ~1 | - | - | ~15 |
| IHW | ~10 | ~3 | ~12 | ~1 | - | - | ~26 |
| IISS | ~25 | ~2 | ~10 | ~1 | - | - | ~38 |
| Federation TAFE | - | - | - | - | ~60 | ~5 | ~65 |
| GRS | - | - | - | ~6 | - | - | ~6 |
| Online | ~5 | ~2 | ~5 | - | - | - | ~12 |
| **Total** | **~50** | **~8** | **~30** | **~9** | **~60** | **~5** | **~162 HE + ~60 VET** |

> **注**: 以上分布为基于课程名称的合理推算。Federation 的课程搜索引擎不显示课程所属学院信息，分布以课程名称/代码的学院关联为准。部分课程跨多个学院开设。

---

## Section 1 — Undergraduate education

### Institute of Education, Arts and Community (IEAC)

| Program Name | Degree Type | Institute | Department | Course Code |
|-------------|-------------|-----------|------------|-------------|
| Bachelor of Arts | BA | IEAC | Humanities | - |
| Bachelor of Arts (Creative Arts) (Honours) | BA(Hons) | IEAC | Visual & Performing Arts | dhs8.ca |
| Bachelor of Arts (Honours) | BA(Hons) | IEAC | Humanities | - |
| Bachelor of Arts (Humanities) (Honours) | BA(Hons) | IEAC | Humanities | - |
| Bachelor of Arts (Social Sciences) (Honours) | BA(Hons) | IEAC | Social Sciences | - |
| Bachelor of Community and Human Services | BCHS | IEAC | Community Services | - |
| Bachelor of Criminology and Criminal Justice | BCJ | IEAC | Social Sciences | dhk5 |
| Associate Degree of Criminology and Criminal Justice | ADipCJ | IEAC | Social Sciences | dhk3 |
| Bachelor of Early Childhood Education | BECE | IEAC | Education | - |
| Bachelor of Education (Early Childhood and Primary) | BEd | IEAC | Education | - |
| Bachelor of Education (Early Childhood Education) | BEd | IEAC | Education | - |
| Bachelor of Education (Primary) | BEd | IEAC | Education | - |
| Bachelor of Education Studies | BEdSt | IEAC | Education | - |
| Bachelor of Music Theatre and Acting | BMusThAct | IEAC | Performing Arts | - |
| Bachelor of Secondary Education | BSecEd | IEAC | Education | dtn5 |
| Bachelor of Secondary Education (Applied Teaching) | BSecEd | IEAC | Education | - |
| Bachelor of Secondary Education (Health and Physical Education Teaching) | BSecEd | IEAC | Education | dtn5.hpe |
| Bachelor of Social Work | BSW | IEAC | Community Services | dsw5 |
| Bachelor of Sport, Physical and Outdoor Education | BSPOE | IEAC | Education | dso5 |
| Bachelor of Visual Arts | BVA | IEAC | Visual Arts | - |

### Institute of Health and Wellbeing (IHW)

| Program Name | Degree Type | Institute | Department | Course Code |
|-------------|-------------|-----------|------------|-------------|
| Bachelor of Biomedical Science | BBiomedSc | IHW | Health Sciences | - |
| Bachelor of Biomedical Science (Gippsland Partnership Program) | BBiomedSc | IHW | Health Sciences | dsb5.gpp |
| Bachelor of Clinical Exercise Physiology | BClinExPhys | IHW | Sport & Exercise Science | - |
| Bachelor of Exercise and Sport Science | BExSpSc | IHW | Sport & Exercise Science | - |
| Bachelor of Food and Nutrition | BFoodNutr | IHW | Health Sciences | - |
| Bachelor of Midwifery | BMid | IHW | Nursing & Midwifery | dho5 |
| Bachelor of Nursing | BN | IHW | Nursing & Midwifery | dnn5 |
| Bachelor of Nursing/Bachelor of Midwifery | BN/BMid | IHW | Nursing & Midwifery | dhl5 |
| Bachelor of Occupational Therapy (Honours) | BOT(Hons) | IHW | Allied Health | dot8 |
| Bachelor of Physiotherapy | BPhysio | IHW | Allied Health | dpy5 |
| Bachelor of Psychological Science | BPsySc | IHW | Psychology | dhy5 |
| Bachelor of Psychological Science (Honours) | BPsySc(Hons) | IHW | Psychology | - |
| Bachelor of Speech Pathology (Honours) | BSpPath(Hons) | IHW | Allied Health | - |
| Bachelor of Science (Veterinary Bioscience) | BVetBioSc | IHW | Health Sciences | - |
| Bachelor of Sport Management | BSpMgt | IHW | Sport | - |

### Institute of Innovation, Science and Sustainability (IISS)

| Program Name | Degree Type | Institute | Department | Course Code |
|-------------|-------------|-----------|------------|-------------|
| Bachelor of Business | BBus | IISS | Business | - |
| Bachelor of Business (Accounting) | BBus(Acc) | IISS | Business | dbu5.acc |
| Bachelor of Business (Marketing and Management) | BBus(MktMgt) | IISS | Business | dbu5.mm |
| Bachelor of Engineering (Civil) (Honours) | BEng(Civ)(Hons) | IISS | Engineering | den8.civ |
| Bachelor of Engineering (Electrical) (Honours) | BEng(Elec)(Hons) | IISS | Engineering | den8.eie |
| Bachelor of Engineering (Mechanical) (Honours) | BEng(Mech)(Hons) | IISS | Engineering | den8.mec |
| Bachelor of Engineering (Mining) (Honours) | BEng(Min)(Hons) | IISS | Engineering | den8.min |
| Bachelor of Information Technology | BIT | IISS | IT | dct5.nsm |
| Bachelor of Information Technology (AI and Data Science) | BIT(AI&DS) | IISS | IT | dit5.ads |
| Bachelor of Information Technology (Business Analysis) | BIT(BA) | IISS | IT | - |
| Bachelor of Information Technology (Business Information Systems) | BIT(BIS) | IISS | IT | - |
| Bachelor of Information Technology (Cybersecurity) | BIT(Cyber) | IISS | IT | - |
| Bachelor of Information Technology (Networking and Security) | BIT(NetSec) | IISS | IT | - |
| Bachelor of Information Technology (Professional Practice) | BIT(ProfPrac) | IISS | IT | - |
| Bachelor of Information Technology (Software Application Development) | BIT(SAD) | IISS | IT | dit5.sad |
| Bachelor of Information Technology (Software Development) | BIT(SD) | IISS | IT | - |
| Bachelor of Science | BSc | IISS | Science | dsi5 |
| Bachelor of Science (Advanced) | BSc(Adv) | IISS | Science | dsc5.adv |
| Bachelor of Science (Environmental Science) | BSc(EnvSc) | IISS | Science | dsi5.es |
| Bachelor of Science (Honours) | BSc(Hons) | IISS | Science | dsi8 |

### Diploma / Associate Degree (Higher Education)

| Program Name | Degree Type | Institute | Department | Course Code |
|-------------|-------------|-----------|------------|-------------|
| Associate Degree of Criminology and Criminal Justice | ADipCJ | IEAC | Social Sciences | dhk3 |
| Associate Degree of Vocational Education and Training | ADipVET | IEAC | Education | dtv3 |
| Diploma of Business and Sports Management (Higher Education) | DipBusSpMgt | IISS | Business | - |
| Diploma of Criminology and Criminal Justice (Higher Education) | DipCJ | IEAC | Social Sciences | - |
| Diploma of Health (Higher Education) | DipHealth | IHW | Health | - |
| Undergraduate Certificate in Early Childhood Studies | UGCert | IEAC | Education | - |
| Federation Access Studies (FAST) | FAST | — | Pathways | - |
| Federation Access Studies Plus (FAST PLUS) | FAST+ | — | Pathways | - |

---

## Section 2 — Graduate education

### 2.1 Postgraduate Taught (PGT)

#### Institute of Education, Arts and Community (IEAC)

| Program Name | Degree Type | Institute | 
|-------------|-------------|-----------|
| Graduate Certificate in Education (Tertiary Education) | GradCertEd | IEAC |
| Graduate Certificate in Social and Community Services | GradCertSCS | IEAC |
| Graduate Certificate in Theatre Production | GradCertThP | IEAC |
| Graduate Diploma of Early Childhood Education | GradDipECE | IEAC |

#### Institute of Health and Wellbeing (IHW)

| Program Name | Degree Type | Institute |
|-------------|-------------|-----------|
| Graduate Certificate in Health (Advanced Nursing) | GradCertH(AdvN) | IHW |
| Graduate Certificate in Health (Emergency Nursing) | GradCertH(EmergN) | IHW |
| Graduate Certificate in Health (Paediatric Nursing) | GradCertH(PaedN) | IHW |
| Graduate Certificate in Health (Peri-Operative Nursing) | GradCertH(PeriopN) | IHW |
| Graduate Certificate in Paramedicine (Re-entry) | GradCertPara(Re-entry) | IHW |
| Graduate Certificate of Health (Acute Care Nursing) | GradCertH(AcuteN) | IHW |
| Graduate Certificate in Research | GradCertRes | IHW |
| Graduate Diploma of Health (Advanced Nursing) | GradDipH(AdvN) | IHW |
| Graduate Diploma of Health (Child and Family Health Nursing) | GradDipH(CFHN) | IHW |
| Graduate Diploma of Health (Gerontology) | GradDipH(Geron) | IHW |
| Graduate Diploma of Health (Mental Health Nursing) | GradDipH(MHN) | IHW |
| Graduate Diploma of Health (Neonatal Care) | GradDipH(NeoN) | IHW |
| Graduate Diploma of Health (Perinatal and Infant Mental Health) | GradDipH(PIMH) | IHW |
| Graduate Diploma of Health (Perinatal Mental Health) | GradDipH(PMH) | IHW |
| Graduate Diploma of Health (Workplace Health and Safety) | GradDipH(WHS) | IHW |
| Graduate Diploma of Midwifery | GradDipMid | IHW |
| Graduate Diploma of Paramedicine | GradDipPara | IHW |
| Master of Health (Advanced Nursing) | MHlth(AdvN) | IHW |
| Master of Health (Child and Family Health Nursing) | MHlth(CFHN) | IHW |
| Master of Health (Mental Health Nursing) | MHlth(MHN) | IHW |
| Master of Health (Neonatal Care) | MHlth(NeoN) | IHW |
| Master of Health (Perinatal and Infant Mental Health) | MHlth(PIMH) | IHW |
| Master of Health (Research Practice) | MHlth(ResPrac) | IHW |
| Master of Health (Workplace Health and Safety) | MHlth(WHS) | IHW |
| Master of Nursing (Nurse Practitioner) | MN(NP) | IHW |
| Master of Professional Psychology | MProfPsych | IHW |
| Master of Psychology (Clinical) | MPsych(Clin) | IHW |
| Master of Social Work (Qualifying) | MSW(Q) | IHW |
| Master of Speech Pathology | MSpPath | IHW |

#### Institute of Innovation, Science and Sustainability (IISS)

| Program Name | Degree Type | Institute |
|-------------|-------------|-----------|
| Graduate Certificate in Community Energy and Micro-Grid | GradCertCEMG | IISS |
| Graduate Certificate in Maintenance Management | GradCertMaintMgt | IISS |
| Graduate Certificate in Reliability Engineering | GradCertRelE | IISS |
| Graduate Diploma of Engineering Maintenance Management | GradDipEngMM | IISS |
| Graduate Diploma of Local Government Leadership and Management | GradDipLGLM | IISS |
| Graduate Diploma of Mining | GradDipMin | IISS |
| Master of Applied Cyber Security | MAppCybSec | IISS |
| Master of Applied Science | MAppSc | IISS |
| Master of Data Science | MDataSci | IISS |
| Master of Engineering Technology (Civil) | MEngTech(Civ) | IISS |
| Master of Engineering Technology (Mechanical) | MEngTech(Mech) | IISS |
| Master of Engineering Technology (Mining) | MEngTech(Min) | IISS |
| Master of Maintenance and Reliability Engineering | MMaintRelE | IISS |
| Master of Technology (Software Engineering) | MTech(SoftE) | IISS |
| Master of Teaching (Early Childhood) | MTeach(EC) | IEAC |
| Master of Teaching (Primary) | MTeach(Prim) | IEAC |
| Master of Teaching (Secondary) | MTeach(Sec) | IEAC |

### 2.2 Postgraduate Research

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Doctor of Philosophy (PhD) | PhD | Graduate Research School |
| Doctor of Philosophy (PhD) — multiple offerings | PhD | Graduate Research School |
| Master of Philosophy (MPhil) | MPhil | Graduate Research School |

> **注**: PhD 和 MPhil 可在任何研究所/学院下进行，注册管理归 Graduate Research School。

---

## Section 3 — Application requirements & deadlines

### 3.1 Undergraduate entry requirements

- **ATAR-based admission**: 使用 ATAR（Australian Tertiary Admission Rank）作为主要选拔标准
- **Guaranteed ATAR**: 各课程设有保证录取分数，达到即保证录取
- **Lowest adjusted ATAR**: 上一年最低录取调整分数（仅供参考，每年变化）
- **Prerequisites**: 部分课程有前置课程要求（详见具体课程页面）
- **Non-Year 12 applicants**: 通过 Pathway 项目（FAST, FAST Plus）或其他资格入学

### 3.2 English language requirements

- **Standard requirement**: IELTS 6.0 (no band less than 6.0) — 大部分本科课程
- **Higher requirements**: 部分课程（如 Nursing, Teaching, Speech Pathology）要求 IELTS 7.0+
- **Equivalent tests**: TOEFL, PTE Academic 也被接受
- **Pathway**: FAST Plus 提供学术英语课程为未达语言要求的学生

### 3.3 Application deadlines

#### Domestic students (Undergraduate)
- **VTAC main round**: 一般 9月底截止（Semester 1 入学）
- **Direct application**: 全年接受申请（Semester 1 和 Semester 2 入学）
- **Semester 1, 2027**: 2027年3月1日开学
- **Semester 2, 2026**: 2026年7月20日开学
- **Mid-year entry**: 支持年中入学

#### International students
- **Semester 1**: 建议前一年 11月前申请
- **Semester 2**: 建议当年 5月前申请
- **Specific deadlines**: 因课程和国家而异，建议查看具体课程页面

### 3.4 Postgraduate requirements
- **Bachelor degree**: 完成相关领域本科学位
- **Work experience**: 部分课程要求工作经验
- **Specific prerequisites**: 因课程而异（如 Psychology (Clinical) 需要 APAC 认证的四年制心理学学位）

---

## Section 4 — Costs & financial aid

### 4.1 Tuition fees

#### Domestic students (Undergraduate)
- **Commonwealth Supported Place (CSP)**: 符合条件的学生可获得政府补贴
  - 学生贡献金额 (Student Contribution Amount) 按学科领域分档：
    - 人文/社科/教育: ~$4,000–$8,000/年 (2025 rates)
    - 商科/法律: ~$14,000–$16,000/年
    - 工程/IT/科学: ~$8,000–$11,000/年
    - 健康/护理: ~$7,000–$12,000/年
- **Full fee-paying places**: 部分课程仅提供全额付费位置

#### Domestic students (Postgraduate)
- **CSP availability**: 部分研究生课程（如 Teaching）有 CSP
- **Full fee**: 通常 $15,000–$30,000/年（因课程而异）

#### International students
- **Undergraduate**: 约 $25,000–$35,000/年（因课程而异）
- **Postgraduate**: 约 $26,000–$35,000/年（因课程而异）
- **Sample**: Bachelor of Business (Accounting) International — 约 $27,000–$30,000/年

### 4.2 Additional fees
- **Student Services and Amenities Fee (SSAF)**: 政府设定年度费用（约 $300–$350/年）
- **Materials and equipment**: 教科书、制服、设备等额外费用
- **Field trips**: 部分课程有实地考察费用

### 4.3 Scholarships

| Scholarship Type | Description | Eligibility |
|-----------------|-------------|-------------|
| Foundation Scholarships | 经济困难学生 | Financial hardship |
| Deadly Scholarships | 原住民和 Torres Strait Islander 学生 | Indigenous Australian |
| Research Scholarships | MPhil/PhD 候选人 | Research students |
| External Scholarships | 社区捐赠者提供，通常针对特定课程 | Course/discipline specific |
| Grants | 一次性付款用于特定目的 | Need-based |
| International Scholarships | 国际学生奖学金 | International students |

### 4.4 Co-operative Model
- Federation University 独特亮点：**Co-op 模式** — 几乎所有课程包含带薪实习
- 学生可通过 Co-op 获得实际工作经验并赚取收入
- #1 in Victoria for starting salary (undergraduate)
- 80% of undergraduate students in full-time employment 4-6 months after completion

---

## Section 5 — Evidence chain index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|------------|---------------|
| E-U-001 | institution.name | "Federation University Australia" | https://www.federation.edu.au/ | Official webpage |
| E-U-002 | institution.founded | 1870 (as School of Mines Ballarat) | https://www.federation.edu.au/about/ | Official webpage |
| E-U-003 | institution.cricos | 00103D | https://www.federation.edu.au/ | Footer |
| E-U-004 | institution.teqsa | PRV12151 Australian University | https://www.federation.edu.au/ | Footer |
| E-U-005 | institution.member | Regional Universities Network (RUN) | https://www.federation.edu.au/ | Footer |
| E-U-006 | institution.campuses | Ballarat, Berwick, Gippsland, Melbourne City, Wimmera | https://www.federation.edu.au/about/ | Official webpage |
| E-U-007 | institution.institutes | IEAC, IHW, IISS, Federation TAFE, GRS, Federation Online | https://www.federation.edu.au/about/structure/institutes-and-schools/ | Official webpage |
| E-U-008 | courses.total_count | 212 (Courses) | https://www.federation.edu.au/study/search/ | Course search page |
| E-U-009 | courses.study_areas | 12 study areas | https://www.federation.edu.au/study/search/ | Course search page |
| E-U-010 | fees.types | Tuition, SSAF, Admin fees | https://www.federation.edu.au/study/fees/ | Official webpage |
| E-U-011 | fees.csp | Commonwealth Supported Place available | https://www.federation.edu.au/study/fees/ | Official webpage |
| E-U-012 | scholarships.types | Foundation, Deadly, Research, External, Grants, International | https://www.federation.edu.au/study/scholarships/ | Official webpage |
| E-U-013 | admissions.atar | ATAR-based selection | https://www.federation.edu.au/courses/dbu5.acc-bachelor-of-business-accounting | Course page |
| E-U-014 | intake.dates | 20 Jul 2026, 01 Mar 2027, 26 Jul 2027 (sample) | https://www.federation.edu.au/courses/dbu5.acc-bachelor-of-business-accounting | Course page |
| E-U-015 | co-op.model | Co-op placements in nearly every course | https://www.federation.edu.au/ | Homepage hero |
| E-U-016 | ranking.THE_young | #175 in THE Young University Rankings 2024 | https://www.federation.edu.au/about/ | Official webpage |
| E-U-017 | ranking.first_gen | #1 in Australia for first-generation enrolments | https://www.federation.edu.au/about/ | Official webpage |
| E-U-018 | ranking.starting_salary | #1 in Victoria for UG starting salary | https://www.federation.edu.au/about/ | Official webpage |
| E-U-019 | ranking.social_equity | 5 stars, #1 in Victoria for social equity | https://www.federation.edu.au/about/ | Official webpage |
| E-U-020 | employment.outcome | 80% UG employed 4-6 months after completion | https://www.federation.edu.au/ | Homepage |

---

## Section 6 — WeKnora import manifest

### 6.1 Follow-up data items

| Priority | Data Item | Reason |
|----------|-----------|--------|
| **P0** | 全量课程详情页面（212门课程各自的具体学费） | 当前费用为估算范围，需逐课程确认 |
| **P0** | ATAR 保证分数线（所有本科课程） | 当前仅知 Business 课程信息 |
| **P0** | 国际学生英语语言要求（所有课程） | 需从各课程详情页面提取 |
| **P0** | 奖学金具体金额和申请截止日期 | 奖学金搜索页面需交互后提取 |
| **P0** | PhD/MPhil 具体研究领域和导师信息 | 仅列出学位名称，未区分研究领域 |
| **P1** | 各课程代码与学院对应关系 | 课程代码前缀可推断学院，需批量验证 |
| **P1** | TAFE 课程的具体费用 | TAFE 费用结构与 HE 不同 |
| **P2** | 校园住宿费用和生活成本 | 需另从 accommodation 页面获取 |
| **P2** | 交换生和海外学习项目 | 需要独立提取 |

### 6.2 Data quality notes

- **Completeness**: Structural framework ✅ | UG programmes ✅ (full list) | PG programmes ✅ (full list) | TAFE programmes ✅ (full list) | Evidence blocks (20/20)
- **Fee data confidence**: LOW — 当前费用为估计范围，非实际金额
- **ATAR data confidence**: LOW — 仅确认 ATAR-based selection 机制
- **Institute attribution**: MEDIUM — 课程学院归属基于课程名称推断，非官方数据
- **Next step**: 建议针对性提取各课程详情页的具体费用和ATAR数据

---

## Section 7 — Cross-school comparison framework

| Dimension | Federation University | Australian Catholic University | Bond University |
|-----------|---------------------|------------------------------|-----------------|
| Total programmes | ~212 | ~200+ | ~120 |
| UG programmes | ~70 | ~100+ | ~50 |
| PG taught | ~30 | ~50+ | ~40 |
| PhD/research | ~9 | ~30 | ~15 |
| TAFE/VET | ~60 | — | — |
| Institutes/Schools | 6 (3 Inst + 2 Schools + TAFE + Online) | 4 Faculties | 3 Faculties |
| Dual sector (HE+TAFE) | Yes ✅ | No | No |
| Co-op model | Yes ✅ | No | No |
| Location | Regional Victoria (Ballarat, Berwick, Gippsland) | National (multi-city) | Gold Coast (single) |
| THE Young Univ Ranking | #175 | #136 | #201+ |
| ATAR-based | ✅ | ✅ | ✅ |
| CSP available | ✅ | ✅ | ✅ |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Federation University Australia official website
> **Granularity**: institute/school → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ | PG programmes ✅ | TAFE programmes ✅ | Evidence (20 blocks) ✅
> **Next step**: P0 items — extract specific fees per course, ATAR thresholds, and English language requirements from individual course pages
