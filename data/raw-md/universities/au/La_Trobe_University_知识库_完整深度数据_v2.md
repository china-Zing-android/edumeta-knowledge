# La Trobe University 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Victoria)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~150+ (含 majors, minors) |
| 研究生授课型项目 (PGT: MSc/MA/MBA/Grad Cert/Grad Dip) | ~120+ |
| 研究生研究型项目 (MPhil/PhD/Professional Doctorate) | ~80+ |
| **学位项目总计** | **~350+ 官方声明 500+ (含所有级别)** |
| 学院/学系 (Schools) | 11 |
| 院系 (Departments) | 15+ |

> 来源: La Trobe University 官网声明 "500+ undergraduate, postgraduate and research degrees"
> 官网: https://www.latrobe.edu.au/about

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
La Trobe University
│
├── School of Agriculture, Biomedicine and Environment
│   ├── Department of Biochemistry and Chemistry
│   ├── Department of Ecological, Plant and Animal Sciences
│   ├── Department of Microbiology, Anatomy, Physiology and Pharmacology
│   └── Baker Department of Cardiovascular Research, Translation and Implementation
│
├── School of Allied Health, Human Services and Sport
│   ├── Department of Community and Clinical Health
│   ├── Department of Physiotherapy, Podiatry, Prosthetics and Orthotics
│   └── Department of Sport, Exercise and Nutrition Sciences
│
├── La Trobe Business School
│   ├── Department of Accounting, Data Analytics, Economics and Finance
│   └── Department of Management and Marketing
│
├── School of Computing, Engineering and Mathematical Sciences
│   ├── Department of Computer Science and Information Technology
│   ├── Department of Engineering
│   └── Department of Mathematical and Physical Sciences
│
├── School of Education
│
├── School of Humanities and Social Sciences
│   ├── Department of Archaeology and History
│   ├── Department of Languages and Cultures
│   ├── Department of Politics, Media and Philosophy
│   └── Department of Social Inquiry
│
├── La Trobe Law School
│
├── School of Nursing and Midwifery
│
├── School of Psychology and Public Health
│   ├── Department of Psychology, Counselling and Therapy
│   └── Department of Public Health
│
├── La Trobe Rural Health School
│   ├── Department of Rural Allied Health
│   ├── Department of Rural Clinical Sciences
│   └── Department of Rural Health Sciences
│
└── School of Cancer Medicine
```

> 来源: https://www.latrobe.edu.au/schools-departments (2026-07-10)

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位级别 | 数量(约) | 说明 |
|---------|------|------|
| Bachelor (BA/BSc/BCom/Bus/LLB) | ~80+ | 3-4年制标准本科 |
| Bachelor (Honours) | ~20+ | 1年额外荣誉学士 |
| Associate Degree | ~5+ | 副学士 (如Associate Degree in Engineering Technology) |
| Diploma | ~10+ | 文凭课程 (含Diploma of Rural Health等) |
| Graduate Certificate | ~15+ | 研究生证书 |
| Graduate Diploma | ~10+ | 研究生文凭 |
| Master (Coursework) | ~60+ | 授课型硕士 (含MBA, MEng, MTeach, MPH等) |
| Master (Research) | ~15+ | 研究型硕士 (MPhil, MSc by Research) |
| Doctor of Philosophy (PhD) | ~50+ | 各学科博士 |
| Professional Doctorate | ~5+ | 专业博士 (如Doctor of Medicine) |

### 0.4 分布矩阵 — 学院 × 学位级别 (Rule 4 — distribution matrix)

| School | UG Bachelor | Honours | Diploma/Assoc. | PG Cert/Dip | Master | PhD/Research |
|--------|------------|---------|---------------|-------------|--------|-------------|
| School of Agriculture, Biomedicine and Environment | ● | ● | | ● | ● | ● |
| School of Allied Health, Human Services and Sport | ● | ● | ● | ● | ● | ● |
| La Trobe Business School | ● | | | ● | ● | ● |
| School of Computing, Engineering and Mathematical Sciences | ● | ● | ● | ● | ● | ● |
| School of Education | ● | | | ● | ● | ● |
| School of Humanities and Social Sciences | ● | ● | | ● | ● | ● |
| La Trobe Law School | ● | | | ● | ● | ● |
| School of Nursing and Midwifery | ● | | ● | ● | ● | ● |
| School of Psychology and Public Health | ● | ● | | ● | ● | ● |
| La Trobe Rural Health School | ● | ● | ● | ● | ● | ● |
| School of Cancer Medicine | | | | | | ● |

> ● = 提供此级别项目
> 来源: https://www.latrobe.edu.au/schools-departments + 各学科课程页面 (2026-07-10)

---

## Section 1 — 本科教育 (Undergraduate Education)

### 1.1 School of Agriculture, Biomedicine and Environment

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Biomedical Science | BBiomedSc | 3年 | Melbourne | Pathway to Doctor of Medicine |
| Bachelor of Biomedical Science (Medical) | BBiomedSc(Med) | 3年 | Melbourne | Pre-medicine pathway |
| Bachelor of Biomedicine | BBiomed | 3年 | Melbourne | Pathway to research/medicine |
| Bachelor of Food and Nutrition | BFoodNutr | 3年 | Melbourne | Nutrition Society of Australia |
| Bachelor of Science | BSc | 3年 | Melbourne, Bendigo | Multiple majors |

> 来源: https://www.latrobe.edu.au/courses/study-health + https://www.latrobe.edu.au/courses/study-science

### 1.2 School of Allied Health, Human Services and Sport

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Health Sciences | BHealthSc | 3年 | Multiple | With professional placement |
| Bachelor of Sport and Exercise Science | BSportExSc | 3年 | Melbourne, Bendigo | |
| Bachelor of Sport and Recreation Management | BSpRecMgmt | 3年 | Melbourne | |
| Bachelor of Physiotherapy (Honours) | BPhysio(Hons) | 4年 | Melbourne | Fully-qualified physio |
| Bachelor of Social Work (Honours) | BSW(Hons) | 4年 | Multiple | |
| Bachelor of Paramedic Practice with Honours | BParamedic(Hons) | 3年 | Bendigo | |
| Bachelor of Oral Health Science | BOralHealth | 3年 | Bendigo | |
| Bachelor of Dental Science (Honours) | BDentSc(Hons) | 5年 | Bendigo | New course |

> 来源: https://www.latrobe.edu.au/courses/study-health

### 1.3 La Trobe Business School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Accounting | BAcc | 3年 | Melbourne, Bendigo, Online | CPA/CAANZ accredited |
| Bachelor of Business | BBus | 3年 | Multiple | AI-integrated curriculum |
| Bachelor of Business Analytics | BBusAnalytics | 3年 | Multiple | New course |
| Bachelor of Commerce | BCom | 3年 | Multiple | |
| Bachelor of Economics | BEc | 3年 | Melbourne | |
| Bachelor of Finance | BFin | 3年 | Melbourne | |
| Bachelor of International Business | BIntBus | 3年 | Melbourne | |
| Bachelor of Marketing | BMark | 3年 | Melbourne, Online | |

> 来源: https://www.latrobe.edu.au/courses/study-business-and-commerce

### 1.4 School of Computing, Engineering and Mathematical Sciences

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Associate Degree in Engineering Technology | ADipET | 2年 | Melbourne | Pathway to BEng |
| Bachelor of Civil Engineering (Honours) | BEng(Civil)(Hons) | 4年 | Melbourne | |
| Bachelor of Electrical and Electronic Engineering (Honours) | BEng(Elec)(Hons) | 4年 | Melbourne | 30+年教学历史 |
| Bachelor of Computer Science | BCompSc | 3年 | Melbourne | |
| Bachelor of Information Technology | BIT | 3年 | Melbourne, Bendigo | |
| Bachelor of Cybersecurity | BCyberSec | 3年 | Melbourne | |
| Bachelor of Mathematical Sciences | BMathSc | 3年 | Melbourne | |
| Bachelor of Statistics | BStat | 3年 | Melbourne | |
| Bachelor of Science (Physics) | BSc(Phys) | 3年 | Melbourne | |

> 来源: https://www.latrobe.edu.au/courses/study-engineering + https://www.latrobe.edu.au/courses/study-information-technology + https://www.latrobe.edu.au/courses/study-science

### 1.5 School of Education

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Education (Secondary) | BEd(Secondary) | 4年 | Melbourne, Bendigo | Teaching qualification |
| Bachelor of Education (Early Childhood) | BEd(EC) | 4年 | Melbourne | |
| Bachelor of Education (Primary) | BEd(Primary) | 4年 | Melbourne, Bendigo | |
| Bachelor of Teaching (Secondary) | BTeach(Secondary) | 2年 | Melbourne | Graduate entry |
| Bachelor of Physical and Outdoor Education | BPOE | 4年 | Bendigo | |

> 来源: https://www.latrobe.edu.au/courses/study-education-teaching

### 1.6 School of Humanities and Social Sciences

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Arts | BA | 3年 | Melbourne, Bendigo | Wide range of majors |
| Bachelor of Criminal Justice | BCJ | 3年 | Melbourne | |
| Bachelor of Criminology | BCrim | 3年 | Melbourne | |
| Bachelor of International Relations | BIntRel | 3年 | Melbourne | |
| Bachelor of Media and Communication | BMediaComm | 3年 | Melbourne | |
| Bachelor of Politics, Philosophy and Economics | BPPE | 3年 | Melbourne | |
| Bachelor of Social Science | BSocSc | 3年 | Melbourne | |
| Bachelor of Psychological Science (Humanities) | BPsySc | 3年 | Melbourne | |

> 来源: https://www.latrobe.edu.au/courses/study-arts-social-sciences-and-communications + https://www.latrobe.edu.au/courses/study-criminology

### 1.7 La Trobe Law School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Laws (Honours) | LLB(Hons) | 4年 | Melbourne, Bendigo | |
| Bachelor of Laws (Honours)/Bachelor of Arts | LLB(Hons)/BA | 5年 | Melbourne | Double degree |
| Bachelor of Laws (Honours)/Bachelor of Commerce | LLB(Hons)/BCom | 5年 | Melbourne | Double degree |
| Bachelor of Laws (Honours)/Bachelor of Science | LLB(Hons)/BSc | 5年 | Melbourne | Double degree |
| Bachelor of Laws (Honours)/Bachelor of Criminology | LLB(Hons)/BCrim | 5年 | Melbourne | Double degree |
| Bachelor of Laws (Honours)/Bachelor of International Relations | LLB(Hons)/BIntRel | 5年 | Melbourne | Double degree |

> 来源: https://www.latrobe.edu.au/courses/study-law

### 1.8 School of Nursing and Midwifery

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Nursing | BNurs | 3年 | Multiple campuses | World top 50 nursing (QS) |
| Bachelor of Nursing/Bachelor of Midwifery | BNurs/BMid | 4年 | Melbourne, Bendigo | Dual registration |
| Bachelor of Nursing/Bachelor of Psychological Science | BNurs/BPsySc | 4年 | Melbourne | Dual degree |
| Diploma of Health Sciences | DipHealthSc | 1年 | Multiple | Pathway to BNurs |

> 来源: https://www.latrobe.edu.au/courses/study-health

### 1.9 School of Psychology and Public Health

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Psychological Science | BPsySc | 3年 | Multiple | APAC accredited |
| Bachelor of Health Sciences | BHealthSc | 3年 | Multiple | |
| Bachelor of Public Health | BPH | 3年 | Melbourne, Online | |
| Diploma in Health Sciences | DipHealthSc | 1年 | Multiple | Pathway program |

> 来源: https://www.latrobe.edu.au/courses/study-health

### 1.10 La Trobe Rural Health School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Bachelor of Nursing | BNurs | 3年 | Albury-Wodonga, Bendigo, Mildura, Shepparton | Regional campuses |
| Bachelor of Health Sciences | BHealthSc | 3年 | Regional campuses | |
| Bachelor of Social Work (Honours) | BSW(Hons) | 4年 | Regional campuses | |
| Diploma of Rural Health | DipRuralHealth | 1年 | Regional campuses | Pathway program |
| Diploma in Health Sciences | DipHealthSc | 1年 | Regional campuses | |

> 来源: https://www.latrobe.edu.au/study/health + https://www.latrobe.edu.au/la-trobe-rural-health-school

---

## Section 2 — 研究生教育 (Graduate Education)

### 2.1 School of Agriculture, Biomedicine and Environment

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Biotechnology | MBiotech | 2年 | Melbourne | |
| Master of Science | MSc | 2年 | Melbourne | By research |
| Master of Philosophy | MPhil | 2年 | Melbourne | Research degree |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | Various disciplines |
| Graduate Diploma in Science | GradDipSc | 1年 | Melbourne | |

### 2.2 School of Allied Health, Human Services and Sport

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Exercise Science (Clinical) | MExSc(Clin) | 2年 | Melbourne | |
| Master of Physiotherapy Practice | MPhysioPrac | 2年 | Melbourne | Graduate entry |
| Master of Speech Pathology | MSpeechPath | 2年 | Melbourne | |
| Master of Occupational Therapy | MOccTher | 2年 | Melbourne | |
| Master of Orthoptics | MOrthoptics | 2年 | Melbourne | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | Allied Health |

### 2.3 La Trobe Business School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Business Administration | MBA | 1.5-2年 | Melbourne, Online | |
| Master of Professional Accounting | MPA | 2年 | Melbourne | CPA/CAANZ accredited |
| Master of Finance | MFin | 1.5-2年 | Melbourne | |
| Master of Marketing | MMark | 1.5-2年 | Melbourne | |
| Master of Management | MMgmt | 1.5-2年 | Melbourne | |
| Master of Human Resource Management | MHRM | 1.5-2年 | Melbourne | |
| Master of Business Analytics | MBusAnalytics | 1.5-2年 | Melbourne | |
| Graduate Diploma in Business | GradDipBus | 1年 | Melbourne | |
| Graduate Certificate in Business | GradCertBus | 0.5年 | Melbourne | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | |

### 2.4 School of Computing, Engineering and Mathematical Sciences

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Engineering | MEng | 2年 | Melbourne | |
| Master of Engineering Management | MEngMgmt | 1.5-2年 | Melbourne | |
| Master of Civil Engineering | MCivilEng | 2年 | Melbourne | |
| Master of Manufacturing Engineering | MManufEng | 1.5年 | Melbourne | |
| Master of Construction Engineering and Management | MConsEngMgmt | 1.5年 | Melbourne | |
| Master of Engineering (Research) | MEng(Res) | 2年 | Melbourne | Research degree |
| Master of Information Technology | MIT | 2年 | Melbourne | |
| Master of Cybersecurity | MCyberSec | 2年 | Melbourne | |
| Master of Data Science | MDataSc | 2年 | Online | |
| Master of Digital Health | MDigitalHealth | 2年 | Online | |
| Graduate Diploma in Engineering Management | GradDipEngMgmt | 1年 | Melbourne | |
| Graduate Certificate in Engineering | GradCertEng | 0.5年 | Melbourne | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | |

> 来源: https://www.latrobe.edu.au/courses/study-engineering

### 2.5 School of Education

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Teaching (Secondary) | MTeach(Secondary) | 2年 | Multiple | Graduate entry |
| Master of Teaching (Primary) | MTeach(Primary) | 2年 | Multiple | Graduate entry |
| Master of Education | MEd | 1.5-2年 | Multiple | |
| Master of TESOL | MTESOL | 1.5年 | Online | |
| Master of Inclusive Education | MInclEd | 1.5年 | Online | |
| Graduate Diploma in Education | GradDipEd | 1年 | Multiple | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Multiple | Education |

### 2.6 School of Humanities and Social Sciences

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Arts | MA | 1.5-2年 | Melbourne | Coursework by major |
| Master of International Relations | MIntRel | 1.5-2年 | Melbourne | |
| Master of Communication and Media Studies | MCommMedia | 1.5-2年 | Melbourne | |
| Master of Strategic Communication | MStratComm | 1.5-2年 | Melbourne | |
| Master of Social Work (Qualifying) | MSW(Qual) | 2年 | Melbourne, Bendigo | |
| Master of Philosophy | MPhil | 2年 | Melbourne | Research degree |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | |

### 2.7 La Trobe Law School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Juris Doctor | JD | 3年 | Melbourne | Graduate entry |
| Master of Laws | LLM | 1年 | Melbourne | |
| Graduate Diploma in Legal Practice | GradDipLP | 0.5年 | Melbourne | Practical legal training |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | |

### 2.8 School of Nursing and Midwifery

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Nursing | MNurs | 1.5-2年 | Melbourne | |
| Master of Mental Health Nursing | MMHN | 1.5年 | Online | |
| Graduate Certificate in Nursing | GradCertNurs | 0.5年 | Multiple | |
| Graduate Certificate in Midwifery | GradCertMid | 0.5年 | Multiple | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | Nursing |

### 2.9 School of Psychology and Public Health

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Psychology (Clinical) | MPsych(Clin) | 2年 | Melbourne | APAC accredited |
| Master of Public Health | MPH | 1.5-2年 | Melbourne, Online | |
| Master of Health Administration | MHA | 1.5-2年 | Online | |
| Master of Health Information Management | MHIM | 1.5-2年 | Melbourne | |
| Graduate Diploma in Psychology | GradDipPsych | 1年 | Melbourne | |
| Doctor of Clinical Psychology | DClinPsych | 3-4年 | Melbourne | Professional doctorate |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Melbourne | |

### 2.10 La Trobe Rural Health School

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Master of Nursing | MNurs | 1.5-2年 | Regional campuses | |
| Master of Social Work (Qualifying) | MSW(Qual) | 2年 | Regional campuses | |
| Graduate Certificate in Rural Health | GradCertRH | 0.5年 | Regional campuses | |
| Doctor of Philosophy (PhD) | PhD | 3-4年 | Regional campuses | Rural health |

### 2.11 Research Degrees (All Schools)

| 专业名称 | 学位 | 学制 | 校区 | 备注 |
|---------|------|------|------|------|
| Doctor of Philosophy (PhD) | PhD | 3-4年 | All campuses | All disciplines |
| Master of Philosophy | MPhil | 2年 | All campuses | Research preparation |
| Professional Doctorate | DProf | 3-4年 | Melbourne | Various fields |

> 来源: https://www.latrobe.edu.au/research/graduate-research

---

## Section 3 — 申请要求与截止日期 (Application Requirements & Deadlines)

### 3.1 本科入学要求 (UG Entry Requirements)

#### 国内学生 (Domestic)

| 要求 | 详情 |
|------|------|
| 最低年龄 | 17岁 (入学时) |
| 学术要求 | ATAR成绩 (澳大利亚高等教育入学排名)，各专业要求不同 |
| 先修课程 | 部分专业要求特定VCE科目 (如英语、数学、科学) |
| 语言要求 | 英语作为先修科目 (VCE English) |
| 特殊项目 | Aspire Early Offer Program (非ATAR途径) |
| 衔接课程 | Foundation programs, Diploma pathways |
| VTAC代码 | 通过VTAC申请 (维多利亚州招生中心) |
| 直申 | 可直接向大学申请 (非VTAC途径) |

> 来源: https://www.latrobe.edu.au/study/undergrad + https://www.latrobe.edu.au/study/apply

#### 国际学生 (International)

| 要求 | 详情 |
|------|------|
| 学术要求 | 相当于澳大利亚12年级学历；各国学历具体评估 |
| 最低年龄 | 17岁 |
| ATAR替代 | 接受高考成绩、A-Levels、IB、SAT等国际学历 |
| 衔接课程 | La Trobe College Australia提供Diploma和Foundation pathways |

**英语语言要求 (English Language Requirements):**

| IELTS | PTE Academic | TOEFL iBT | CAE/CPE |
|------|-------------|-----------|---------|
| 6.0 (单项≥6.0) | 50 (单项≥50) | 64 (R13,L12,S18,W21) | 169 (各项≥169) |
| **6.5 (单项≥6.0)** | **58 (单项≥50)** | **79 (R13,L12,S18,W21)** | **176 (各项≥169)** |
| 7.0 (单项≥6.5) | 65 (单项≥58) | 94 (R19,L20,S20,W24) | 185 (各项≥176) |
| 7.0 (单项≥7.0) | 65 (单项≥65) | 98 (R24,L24,S23,W27) | NA |
| 7.5 (单项≥7.0) | 73 (单项≥65) | 102 (R24,L24,S23,W27) | 191 (各项≥185) |

> **注**: 各专业要求不同，部分专业要求更高水平。雅思6.5 (单项≥6.0) 为大多数专业的最低标准。
> 来源: https://www.latrobe.edu.au/international/applying/entry-requirements

### 3.2 研究生入学要求 (PG Entry Requirements)

| 项目类型 | 学术要求 | 语言要求 (典型) |
|---------|---------|----------------|
| 授课型硕士 | 相关学科本科学位，均分60-70%+ | 雅思6.5 (单项≥6.0) |
| 研究型硕士 (MPhil) | 相关学科本科学位 (荣誉学士优先) | 雅思6.5 (单项≥6.0) |
| PhD | 相关学科荣誉学士/硕士学位 | 雅思6.5-7.0 (单项≥6.0) |
| MBA | 本科学位+3年工作经验 | 雅思6.5 (单项≥6.0) |
| 研究生证书/文凭 | 本科学位或相关工作经验 | 雅思6.5 (单项≥6.0) |

### 3.3 关键日期 (Key Dates)

| 学期 | 开学时间 | 申请截止 | 备注 |
|------|---------|---------|------|
| Semester 1 | 3月 (March) | 前一年12月-当年1月 | 主要入学季 |
| Semester 2 | 7月 (July) | 5月-6月 | 部分专业开设 |
| Summer | 11月 (November) | 10月 | 部分专业开设 |

### 3.4 申请方式

| 学生类型 | 申请通道 | 说明 |
|---------|---------|------|
| 国内本科 (VCE) | VTAC (维多利亚招生中心) | 12年级学生通过VTAC申请 |
| 国内本科 (非VCE) | 直接向大学申请 | 非12年级学生 |
| 国内研究生 | 直接向大学申请 | |
| 国际学生 | 直接向大学申请 (LTU Application Portal) | 有代理网络 |
| 研究型学位 | 直接向大学申请，需联系导师 | |

> 来源: https://www.latrobe.edu.au/study/apply + https://www.latrobe.edu.au/international/applying/how-to-apply

---

## Section 4 — 费用与奖学金 (Costs & Financial Aid)

### 4.1 学费样本 (Sample Tuition Fees)

#### 国内学生 (Domestic) — Commonwealth Supported Place (CSP)

| 专业示例 | 年学费 (CSP) | 学制 | 备注 |
|---------|-------------|------|------|
| Bachelor of Accounting | ~A$14,827/年 | 3年 | 120 credit points/年 |
| Bachelor of Nursing | ~A$14,827/年 (CSP) | 3年 | 政府补贴 |
| Bachelor of Engineering (Hons) | ~A$14,827/年 (CSP) | 4年 | 政府补贴 |

> CSP费用因学科组别不同有差异 (Band 1-3)

#### 国际学生 (International)

| 专业示例 | 年学费 (国际) | 学制 | 备注 |
|---------|-------------|------|------|
| Bachelor of Nursing | ~A$44,600/年 | 3年 | CRICOS: 113570D |
| Bachelor of Accounting | ~A$38,000-42,000/年 | 3年 | 预估范围 |
| Bachelor of Business | ~A$38,000-42,000/年 | 3年 | |
| Bachelor of Engineering (Hons) | ~A$42,000-45,000/年 | 4年 | |
| Master of Engineering | ~A$40,000-44,000/年 | 2年 | |
| MBA | ~A$45,000-50,000/年 | 1.5-2年 | |
| Master of IT | ~A$38,000-42,000/年 | 2年 | |

> **注**: 国际学费每年可能有最高7%的增长。具体费用以课程页面为准。
> 来源: https://www.latrobe.edu.au/international/applying/fees + 课程页面采样

### 4.2 其他费用 (Other Fees)

| 费用类型 | 金额 | 说明 |
|---------|------|------|
| Student Services and Amenities Fee (SSAF) | ~A$347/年 (2026) | 学生服务设施费 |
| Overseas Student Health Cover (OSHC) | ~A$600-800/年 | 国际学生健康保险 |
| 生活费 (Cost of living) | ~A$25,000-35,000/年 | 预估 (含住宿、餐饮、交通) |

### 4.3 奖学金 (Scholarships)

| 奖学金名称 | 金额 | 适用对象 | 说明 |
|---------|------|---------|------|
| La Trobe International Scholarship | 最高25%学费减免 | 国际学生 | 学术成绩 |
| La Trobe Academic Excellence Scholarship | 最高A$10,000 | 国内新生 | ATAR高分 |
| Destination Australia Program | 最高A$15,000/年 | 地区校区学生 | Regional campus |
| La Trobe Rural Health Scholarship | 多种金额 | 健康类专业 | Rural health |
| Postgraduate Fee Support | 最高25%学费减免 | 研究生 | 指定课程 |

> 来源: https://www.latrobe.edu.au/study/scholarships + https://www.latrobe.edu.au/international/applying/fees

### 4.4 支付方式

| 支付方式 | 说明 |
|---------|------|
| 全额支付 | 学费全款在到期日前支付 |
| 政府资助 (国内) | HECS-HELP (CSP), FEE-HELP (全费), SA-HELP (SSAF) |
| 分期支付 | 不提供分期付款选项 |
| 第三方赞助 | 政府/雇主赞助 |
| 支付截止日期 | 每个课程Census日期前21天 |

> 来源: https://www.latrobe.edu.au/international/applying/fees

---

## Section 5 — 证据链索引 (Evidence Chain Index)

| 证据ID | 字段 | 值 | 来源URL | 捕获日期 |
|-------|------|-----|---------|---------|
| E-U-001 | institution.name | La Trobe University | https://www.latrobe.edu.au/ | 2026-07-10 |
| E-U-002 | institution.schools | 11个School列表 | https://www.latrobe.edu.au/schools-departments | 2026-07-10 |
| E-U-003 | institution.departments | 18个Department列表 | https://www.latrobe.edu.au/schools-departments | 2026-07-10 |
| E-U-004 | fees.domestic.csp | ~A$14,827/年 (Bachelor of Accounting) | https://www.latrobe.edu.au/courses/bachelor-of-accounting | 2026-07-10 |
| E-U-005 | fees.international.annual | A$44,600/年 (Bachelor of Nursing) | https://www.latrobe.edu.au/courses/bachelor-of-nursing | 2026-07-10 |
| E-U-006 | english.ielts.minimum | 6.0-7.5 取决于课程 | https://www.latrobe.edu.au/international/applying/entry-requirements | 2026-07-10 |
| E-U-007 | english.pte.equivalent | 50-73 对应IELTS | https://www.latrobe.edu.au/international/applying/entry-requirements | 2026-07-10 |
| E-U-008 | english.toefl.equivalent | 64-102 对应IELTS | https://www.latrobe.edu.au/international/applying/entry-requirements | 2026-07-10 |
| E-U-009 | application.ug.method | VTAC + Direct | https://www.latrobe.edu.au/study/apply | 2026-07-10 |
| E-U-010 | application.international.method | Direct + Agent | https://www.latrobe.edu.au/international/applying/how-to-apply | 2026-07-10 |
| E-U-011 | rankings.top1percent | QS排名前1% | https://www.latrobe.edu.au/ | 2026-07-10 |
| E-U-012 | rankings.employer.satisfaction | 维州第2 (88.2%) | https://www.latrobe.edu.au/ | 2026-07-10 |
| E-U-013 | nursing.top50 | QS 2026护理学全球前50 | https://www.latrobe.edu.au/courses/study-health | 2026-07-10 |
| E-U-014 | engineering.top200 | 计算机科学/工程全球前200 | https://www.latrobe.edu.au/courses/study-engineering | 2026-07-10 |
| E-U-015 | business.aacsb | 商学院AACSB认证 | https://www.latrobe.edu.au/courses/study-business-and-commerce | 2026-07-10 |
| E-U-016 | fees.international.increase | 每年最高7%增长 | https://www.latrobe.edu.au/international/applying/fees | 2026-07-10 |
| E-U-017 | institution.teqsa | TEQSA PRV12132 | https://www.latrobe.edu.au/courses/bachelor-of-accounting | 2026-07-10 |
| E-U-018 | institution.cricos | CRICOS Provider 00115M | https://www.latrobe.edu.au/ | 2026-07-10 |

---

## Section 6 — WeKnora 导入清单与后续事项

### 6.1 导入清单

| 模块 | 状态 | 优先级 | 备注 |
|------|------|--------|------|
| 院校基本信息 (Section 0.1-0.3) | ✅ 已完成 | P0 | |
| 学院层级结构 (Section 0.2) | ✅ 已完成 | P0 | |
| 分布矩阵 (Section 0.4) | ✅ 已完成 | P0 | |
| 本科课程列表 (Section 1) | ⚠️ 抽样+推测 | P1 | 需要全量API提取 |
| 研究生课程列表 (Section 2) | ⚠️ 抽样+推测 | P1 | 需要全量API提取 |
| 申请要求 (Section 3) | ✅ 已完成 | P0 | |
| 费用信息 (Section 4) | ✅ 已完成 (抽样) | P0 | |
| 证据链 (Section 5) | ✅ 已完成 | P0 | |

### 6.2 P0 — 必须立即完成

- ~350+课程的全量列表 (目前为抽样)
- 各课程具体ATAR/入学分数
- 各课程的国际学费精确值
- IELTS/PTE/TOEFL各课程具体要求

### 6.3 P1 — 尽快完成

- 各专业详细课程设置 (curriculum structure)
- 各专业毕业生就业数据
- 奖学金详细申请条件
- 各专业学分的具体major/minor选项

### 6.4 P2 — 待补充

- 教授/研究团队信息
- 学生生活详细数据
- 校园设施细节
- 实习/placement合作企业列表

---

## Section 7 — 跨校对比框架 (Cross-School Comparison Framework)

### 7.1 澳大利亚院校对比维度

| 对比维度 | La Trobe University | 备注 |
|---------|-------------------|------|
| 建校年份 | 1964 | Go8以外的创新型大学 |
| 校区数量 | 7+ (Melbourne, Bendigo, Albury-Wodonga, Mildura, Shepparton, Sydney, City) | 多校区战略 |
| QS排名 | 世界前250 | 全球前1% |
| 学校结构 | 11个School + 15+ Department | 扁平结构 |
| 重点领域 | 健康科学、护理、工程、商科 | |
| 国际学生比例 | ~30% | 多元化校园 |
| 特色项目 | 地区校区健康专业、Aspire早申项目、StudyFlex灵活学习 | |
| CRICOS | 00115M | |
| TEQSA | PRV12132 | |

### 7.2 特色优势

| 优势领域 | 详情 |
|---------|------|
| 护理学 | QS全球前50，澳大利亚最大的农村健康学院 |
| 雇主满意度 | 维州第2 (88.2%) |
| 商学院 | AACSB认证 (全球前6%) |
| 工程学 | 30+年教学历史，全球前200 |
| StudyFlex | 混合教学模式 (线上线下结合) |
| 就业率 | 87.9%工程本科毕业生4个月内就业 (维州第2) |
| 地区校区 | 澳大利亚最大的农村健康学院 (La Trobe Rural Health School) |

---

> **Document generated**: 2026-07-10
> **Sources**: La Trobe University official website (https://www.latrobe.edu.au/)
> **Next review recommended**: 2026-10-10 (3 months)
