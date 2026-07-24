# City St George's, University of London Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser + WebFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.0 院校基本信息

| 项目 | 内容 |
|------|------|
| 院校名 (English) | City St George's, University of London |
| 院校名 (Chinese) | 伦敦大学城市圣乔治学院 |
| 合并时间 | 2024 年 (City + St George's 合并) |
| 前身 | City, University of London (1894) + St George's, University of London (1733) |
| 校园 | Clerkenwell (主), Moorgate, Tooting (主医疗) |
| 学生总数 | ~27,000 |
| 在伦敦排名 | 第 4 (peopleandplanet.org) |
| UK 排名 | 第 13 |
| 课程总数 | **606** (UG + Foundation + PGT + PGR + Apprenticeships + Short Courses) |
| 学院数 | 6 schools + 1 institute |
| 性质 | 综合研究型大学 (University of London 联邦成员) |

> **证据**: `https://www.citystgeorges.ac.uk/about` — "Day in, day out, year in and year out, City St George's transforms the lives of around 27,000 students..." | 抓取日期: 2026-07-08

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位 (UG) | **96** |
| 研究生授课型 (PGT) | **157** |
| 研究生研究型 (PGR) | N/A — 见 research/degrees page |
| Foundation 预科 | 见 foundation page |
| Apprenticeships 学徒制 | 见 apprenticeships page |
| 短期 / 专业课程 | 见 short-courses page |
| **总计 (索引页)** | **606** |
| 学院 / 系所 | 6 schools + 1 institute, 共 23 departments |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
City St George's, University of London (2024 merger)
│
├── School of Policy & Global Affairs
│   ├── Department of Economics
│   ├── Department of International Politics
│   └── Department of Sociology and Criminology
│
├── School of Communication & Creativity
│   ├── Department of Journalism
│   ├── Department of Media, Culture and Creative Industries
│   ├── Department of Performing Arts
│   └── Centre for Language Studies
│
├── Bayes Business School (subdomain: bayes.citystgeorges.ac.uk)
│
├── School of Health & Medical Sciences
│   ├── Department of Population Health and Policy
│   ├── Department of Interprofessional Healthcare
│   ├── Department of Allied Health
│   ├── Department of Nursing and Midwifery
│   ├── Department of Optometry and Visual Science
│   ├── Department of Psychology and Neuroscience
│   ├── Department of Medicine
│   └── Department of Molecular and Biomedical Sciences
│
├── School of Science & Technology
│   ├── Department of Computer Science
│   ├── Department of Mathematics
│   └── Department of Engineering
│
├── The City Law School
│   ├── Academic Programmes (LLB, GDL, LLM)
│   └── Professional Programmes (Bar Training, SPP, SQE)
│
└── The Finsbury Institute
```

> **证据**: `https://www.citystgeorges.ac.uk/about/our-schools` — 完整列出 7 个学术单元 | 抓取日期: 2026-07-08

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

#### 本科 (UG) — 96 项

| 学位级别 | 数量 |
|---------|------|
| BA (Hons) | 27 |
| BSc (Hons) | 40 |
| LLB (Hons) | 3 |
| MBBS | 2 |
| BMid (Hons) | 1 |
| MOptom (Hons) | 1 |
| BEng (Hons) | 8 |
| MEng (Hons) | 8 |
| MSci (Hons) | 6 |
| **合计** | **96** |

#### 研究生授课型 (PGT) — 157 项

| 学位级别 | 数量 |
|---------|------|
| MA | ~30 |
| MSc | ~65 |
| MFA | 2 |
| MPH | 1 |
| MPAS | 1 |
| LLM | ~13 |
| MRes | ~6 |
| PGCert | ~12 |
| PGDip | ~3 |
| DPsych | 1 |
| 联合学位 (MA/MSc/LLM + PGDip/PGCert) | ~18 |
| 其他 (e.g. PGCert/GradCert, MRes/PGCert) | ~5 |
| **合计** | **157** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

#### UG (96 项)

| School | BA/BSc | LLB | MBBS/Mid/Optom | BEng/MEng/MSci | 合计 |
|--------|--------|-----|----------------|-----------------|------|
| Policy & Global Affairs | 18 | 0 | 0 | 0 | 18 |
| Communication & Creativity | 13 | 0 | 0 | 0 | 13 |
| Bayes Business School | 20 | 0 | 0 | 0 | 20 |
| Health & Medical Sciences | 18 | 0 | 6 | 0 | 24 |
| Science & Technology | 5 | 0 | 0 | 17 | 22 |
| The City Law School | 0 | 3 | 0 | 0 | 4* |
| **合计** | **75** | **3** | **6** | **17** | **96** |

\* The City Law School 在 UG 中也提供部分 combined 学位 (e.g. Law with Criminology)。某些专业跨学院归属（如 Mathematics & Finance）。

#### PGT (157 项)

| School | MA | MSc | LLM | MRes/MFA/MPH/MPAS | PGCert/PGDip | 联合 | 合计 |
|--------|-----|------|------|-------------------|--------------|------|------|
| Policy & Global Affairs | 4 | 6 | 0 | 0 | 0 | 2 | 12 |
| Communication & Creativity | 22 | 4 | 0 | 2 (MFA) | 0 | 0 | 28 |
| Bayes Business School | 0 | 26 | 0 | 0 | 0 | 4 | 30 |
| Health & Medical Sciences | 1 | 16 | 0 | 6 (MRes/MPH/MPAS) | 12 | 20 | 55 |
| Science & Technology | 0 | 11 | 1 | 0 | 0 | 2 | 14 |
| The City Law School | 2 | 0 | 12 | 0 | 0 | 4 | 18 |
| **合计** | **29** | **63** | **13** | **8** | **12** | **32** | **157** |

**Reconciliation**: 96 (UG) + 157 (PGT) = 253 在主站显式列出。剩余 353 项分布在 foundation, PGR, apprenticeships, short-courses 类别（合并索引页报告 606）。

---

## SECTION 1 — Undergraduate education

### 1.1 School of Policy & Global Affairs (UG 18 项)

| Program | Degree | URL |
|---------|--------|-----|
| Business Economics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/business-economics |
| Economics | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/economics-ba |
| Economics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/economics |
| Economics with Accounting | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/economics-with-accounting |
| Financial Economics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/financial-economics |
| International Political Economy | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/international-political-economy |
| Mathematics and Finance | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics-and-finance |
| Mathematics with Finance and Economics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics-with-finance-and-economics |
| Criminology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/criminology |
| Criminology and Law | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/criminology-and-law |
| Criminology and Sociology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/criminology-and-sociology |
| International Politics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/international-politics |
| International Politics and Sociology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/international-politics-and-sociology |
| Politics | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/politics |
| Social Sciences | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/social-sciences |
| Sociology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/sociology |
| Sociology with Psychology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/sociology-with-psychology |
| History | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/history |

> **证据**: 抓取自 https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate | 2026-07-08

### 1.2 School of Communication & Creativity (UG 13 项)

| Program | Degree | URL |
|---------|--------|-----|
| Commercial Dance | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/commercial-dance |
| Communication, PR and Advertising | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/communication-pr-advertising |
| Contemporary Vocal Performance | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/contemporary-vocal-performance |
| English with Creative Writing | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/english-with-creative-writing |
| English with Publishing | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/english-with-publishing |
| English | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/english |
| Journalism | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/journalism |
| Journalism, Politics and History | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/journalism-politics-and-history |
| Media and Communications | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/media-communications |
| Media Production | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/media-production |
| Music Performance with Production | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/music-performance-with-production |
| Music, Sound and Technology | BSc (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/music-sound-and-technology |
| Professional Dance and Musical Theatre | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/professional-dance-and-musical-theatre |

### 1.3 Bayes Business School (UG 20 项)

> **特殊**: Bayes Business School 使用独立子域 `bayes.citystgeorges.ac.uk`

| Program | Degree | URL |
|---------|--------|-----|
| Accounting and Finance | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/accounting-and-finance |
| Actuarial Science | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/actuarial-science |
| Banking and International Finance | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/banking-and-international-finance |
| Business Analytics | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-analytics |
| Business Analytics with Finance | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-analytics-with-finance |
| Business Management | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-management |
| Business Management with Social Purpose | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-management-with-social-purpose |
| Business Management, Digital Innovation and Entrepreneurship | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-management-digital-innovation-entrepreneurship |
| Business with Finance | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-with-finance |
| Business with Marketing | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/business-with-marketing |
| Data Analytics and Actuarial Science | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/data-analytics-and-actuarial-science |
| Finance | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/finance |
| Finance with Actuarial Science | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/finance-with-actuarial-science |
| International Business | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/international-business |
| Investment and Financial Risk Management | BSc (Hons) | https://www.bayes.citystgeorges.ac.uk/study/undergraduate/courses/investment-and-financial-risk-management |

### 1.4 School of Health & Medical Sciences (UG 24 项)

| Program | Degree | Campus | URL |
|---------|--------|--------|-----|
| Adult Nursing | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/adult-nursing |
| Biomedical Science | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-science |
| Biomedical Science | MSci (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-science-msci |
| Children's Nursing | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/childrens-nursing |
| Clinical Pharmacology | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/clinical-pharmacology |
| Diagnostic Radiography | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/radiography-diagnostic-imaging |
| Healthcare Science (Physiological Sciences) | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/healthcare-science |
| Linguistics | BSc (Hons) | Clerkenwell | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/linguistics |
| Medicine | MBBS | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine |
| Medicine (Graduate Entry) | MBBS | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/medicine-graduate-entry |
| Mental Health Nursing | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mental-health-nursing |
| Midwifery | BMid (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/midwifery |
| Occupational Therapy | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/occupational-therapy |
| Optometry | MOptom (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/optometry |
| Paramedic Science | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/paramedic-science |
| Physiotherapy | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/physiotherapy |
| Psychology | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/psychology |
| Psychology with Criminology | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/psychology-criminology |
| Speech and Language Therapy | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/speech-and-language-therapy |
| Therapeutic Radiography | BSc (Hons) | Tooting | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/therapeutic-radiography |

### 1.5 School of Science & Technology (UG 22 项)

| Program | Degree | Department | URL |
|---------|--------|------------|-----|
| Artificial Intelligence | BSc (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/artificial-intelligence |
| Artificial Intelligence | MSci (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/artificial-intelligence-msci |
| Computer Science | BSc (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/computer-science |
| Computer Science | MSci (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/computer-science-msci |
| Computer Science with Cyber Security | MSci (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/computer-science-with-cyber-security |
| Computer Science with Games Technology | BSc (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/computer-science-with-games-technology |
| Computer Science with Games Technology | MSci (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/computer-science-with-games-technology-msci |
| Data Science | MSci (Hons) | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/data-science |
| Mathematics with Data Science | BSc (Hons) | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics-with-data-science |
| Mathematics with Data Science | MSci (Hons) | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics-with-data-science-msci |
| Mathematics | BSc (Hons) | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics |
| Mathematics | MSci (Hons) | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mathematics-msci |
| Aerospace Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/aerospace-engineering |
| Aerospace Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/aerospace-engineering-meng |
| Biomedical and Healthcare Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-and-healthcare-engineering |
| Biomedical and Healthcare Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/biomedical-and-healthcare-engineering-meng |
| Civil and Infrastructure Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/civil-and-infrastructure-engineering |
| Civil and Infrastructure Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/civil-and-infrastructure-engineering-meng |
| Electrical and Electronic Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/electrical-and-electronic-engineering |
| Electrical and Electronic Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/electrical-and-electronic-engineering-meng |
| Energy and Sustainability Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/energy-and-sustainability-engineering |
| Energy and Sustainability Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/energy-and-sustainability-engineering-meng |
| Engineering with Business | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/engineering-with-business |
| Engineering with Business | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/engineering-with-business-meng |
| Mechanical and Design Engineering | BEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mechanical-and-design-engineering |
| Mechanical and Design Engineering | MEng (Hons) | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/mechanical-and-design-engineering-meng |

### 1.6 The City Law School (UG 4 项)

| Program | Degree | URL |
|---------|--------|-----|
| Law | LLB (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/law |
| Law and Criminology | LLB (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/law-and-criminology |
| History and Politics | BA (Hons) | https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate/history-and-politics |

---

## SECTION 2 — Graduate education

### 2.1 School of Communication & Creativity (PGT 28 项)

| Program | Degree | URL |
|---------|--------|-----|
| Broadcast Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/broadcast-journalism |
| Creative Writing | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/creative-writing |
| Creative Writing and Publishing | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/creative-writing-and-publishing |
| Creative Writing | MFA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/creative-writing-mfa |
| Culture, Policy and Management | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/culture-policy-and-management |
| Erasmus Mundus Masters: Journalism, Media and Globalisation | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/erasmus-mundus-masters-journalism-media-and-globalisation |
| Fashion Marketing and Strategic Communications | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/fashion-marketing-and-strategic-communications |
| Global Financial Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/global-financial-journalism |
| International Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-journalism |
| Investigative Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/investigative-journalism |
| Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/journalism |
| Magazine Journalism | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/magazine-journalism |
| Marketing Communications | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/marketing-communications |
| Media and Communications | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/media-and-communications |
| Media Management | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/media-management |
| Music by Research | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/music-by-research |
| Music Management | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/music-management |
| Performing Arts Management and Practice | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/performing-arts-management-and-practice |
| Podcasting | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/podcasting |
| Public Relations and Strategic Communications | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/public-relations-and-strategic-communications |
| Publishing | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/publishing |
| Screenwriting | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/screenwriting |
| Screenwriting | MFA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/screenwriting-mfa |
| Academic Practice | MA/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/academic-practice |

### 2.2 Bayes Business School (PGT ~30 项)

> **特殊**: Bayes Business School 使用独立子域 `bayes.citystgeorges.ac.uk/study/masters/courses/`

| Program | Degree | URL |
|---------|--------|-----|
| Actuarial Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/actuarial-management |
| Actuarial Science | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/actuarial-science |
| Actuarial Science with Business Analytics | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/actuarial-science-with-business-analytics |
| Banking and International Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/banking-and-international-finance |
| Business Analytics | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/business-analytics |
| Charity Accounting and Financial Management | MSc/PGDip | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/charity-accounting-and-financial-management |
| Charity Marketing and Fundraising | MSc/PGDip | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/charity-marketing-and-fundraising |
| Corporate Risk Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/corporate-risk-management |
| Digital Marketing with AI | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/digital-marketing-with-ai |
| Digital Supply Chain Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/digital-supply-chain-management |
| Energy, Trade and Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/energy-trade-and-finance |
| Entrepreneurship | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/entrepreneurship |
| Family Business | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/family-business |
| Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/finance |
| Financial Technology and Innovation | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/financial-technology-and-innovation |
| Global Finance (online) | MSc/PGDip/PGCert | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/global-finance |
| Insurance and Risk Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/insurance-and-risk-management |
| International Accounting and Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/international-accounting-and-finance |
| International Accounting and Finance with Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/international-accounting-and-finance-with-management |
| International Business | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/international-business |
| Management | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/management |
| Management, Finance and Tech | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/management-finance-tech |
| Marketing Strategy and Consumer Insights | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/marketing-strategy-and-consumer-insights |
| NGO Management | MSc/PGDip | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/ngo-management |
| Philanthropy, Grantmaking and Social Investment | MSc/PGDip/PGCert | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/philanthropy-grantmaking-and-social-investment |
| Quantitative Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/quantitative-finance |
| Shipping, Trade and Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/shipping-trade-and-finance |
| Sustainable Management and Finance | MSc | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/sustainable-management-and-finance |
| Voluntary Sector Leadership and Management | MSc/PGDip | https://www.bayes.citystgeorges.ac.uk/study/masters/courses/voluntary-sector-leadership-and-management |

### 2.3 School of Policy & Global Affairs (PGT 12 项)

| Program | Degree | URL |
|---------|--------|-----|
| Behavioural Economics | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/behavioural-economics |
| Economic Evaluation in Health Care | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economic-evaluation-in-health-care |
| Economics | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics |
| Economics and Data Analytics | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics-and-data-analytics |
| Economics and Public Policy | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics-and-public-policy |
| Financial Economics | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/financial-economics |
| Financial Technology and Systems | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/financial-technology-and-systems |
| Health Economics and Policy | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/health-economics-and-policy |
| International Business Economics and Strategy | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-business-economics-and-strategy |
| Policy and Global Affairs | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/policy-and-global-affairs |
| Project Management, Finance and Risk | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/project-management-finance-and-risk |
| Criminology and Criminal Justice | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/criminology-and-criminal-justice |
| Modern Public Service | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/modern-public-service |

### 2.4 School of Health & Medical Sciences (PGT 55 项)

| Program | Degree | URL |
|---------|--------|-----|
| Adult and Mental Health Nursing (Pre-reg) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/adult-and-mental-health-nursing-pre-registration |
| Adult Nursing (Pre-reg) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/adult-nursing-pre-registration |
| Advanced Breast Practice | MSc/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-breast-practice |
| Advanced Clinical Practice | MSc/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-clinical-practice |
| Advanced Clinical Practice (Tooting) | MSc/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-clinical-practice-tooting |
| Advanced Musculoskeletal Practice (Tooting) | MSc/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/msc-advanced-musculoskeletal-practice-tooting |
| Applied Nutrition | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/applied-nutrition |
| Biomedical Science – Antimicrobial Resistance | MRes | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-antimicrobial-resistance |
| Biomedical Science – Clinical Biomedical Research | MRes | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-clinical-biomedical-research |
| Biomedical Science – Infection and Immunity | MRes | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-infection-and-immunity |
| Biomedical Science – Molecular Mechanisms of Cancer | MRes | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-molecular-mechanisms-of-cancer |
| Biomedical Science – Reproduction and Development | MRes | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-science-reproduction-and-development |
| Children's Nursing (Pre-reg) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/childrens-nursing-pre-registration |
| Clinical Neuroscience Practice | MSc/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-neuroscience-practice |
| Clinical Optometry | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-optometry |
| Clinical Practice | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-practice |
| Clinical Research | MRes/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-research |
| Clinical, Social and Cognitive Neuroscience | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/clinical-social-and-cognitive-neuroscience |
| Critical Care | PGCert/GradCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/critical-care |
| Enhanced Midwifery Care | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/enhanced-midwifery-care |
| Food Policy | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/food-policy |
| Genomic Healthcare | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-healthcare |
| Genomic Medicine | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-medicine |
| Genomic Medicine (Online) | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/genomic-medicine-online |
| Global Health (online) | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/global-health-online |
| Global Maternal Health | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/global-maternal-health |
| Global Organisational and Business Psychology | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/global-organisational-and-business-psychology |
| Health Management | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/health-management |
| Health Policy (online) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/health-policy |
| Healthcare and Biomedical Education | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/healthcare-and-biomedical-education |
| Healthcare Research Skills and Methods | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/healthcare-research-skills-and-methods |
| Heart Failure | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/heart-failure |
| Interpretation and Clinical Application of Genomic Data | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/interpretation-and-clinical-application-of-genomic-data |
| Medical Ethics, Law and Humanities | MA/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/medical-ethics-law-and-humanities |
| Medical Ultrasound | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/medical-ultrasound |
| Mental Health Nursing (Pre-reg) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/mental-health-nursing-pre-registration |
| Occupational Therapy (Pre-Registration) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/occupational-therapy-pre-registration |
| Organisational Psychology | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/organisational-psychology |
| Physician Associate Studies | MPAS | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/physician-associate-studies |
| Physiotherapy (Pre-registration) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/physiotherapy |
| Postgraduate Certificate in Counselling Psychology | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/postgraduate-certificate-in-counselling-psychology |
| Primary Care (Practice Nursing) | MSc/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/primary-care-practice-nursing |
| Professional Doctorate in Counselling Psychology | DPsych | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/professional-doctorate-in-counselling-psychology |
| Professional Practice in Mammography | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/professional-practice-in-mammography |
| Professional Practice | PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/professional-practice |
| Psychological Therapies with Psychological Wellbeing Practitioner | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/psychological-therapies-with-psychological-wellbeing-practitioner |
| Psychology (Conversion) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/psychology-conversion |
| Psychology of Health and Wellbeing | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/psychology-of-health-and-wellbeing |
| Public Health and Specialist Community Nursing | MSc/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/public-health-and-specialist-community-nursing |
| Public Health | MPH | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/public-health |
| Radiography (Computed Tomography) | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/radiography-computed-tomography |
| Radiography (Magnetic Resonance Imaging) | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/radiography-magnetic-resonance-imaging |
| Speech and Language Therapy | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/speech-and-language-therapy |
| Speech, Language and Communication (Advanced Studies) | MSc | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/speech-language-and-communication-advanced-studies |
| Sports Cardiology | MSc/PGDip/PGCert | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/sports-cardiology |

### 2.5 School of Science & Technology (PGT 14 项)

| Program | Degree | Department | URL |
|---------|--------|------------|-----|
| Artificial Intelligence | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/artificial-intelligence |
| Computer Games Technology | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/computer-games-technology |
| Cyber Security | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/cyber-security |
| Data Science | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/data-science |
| Data, Policy and Society | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/data-policy-and-society |
| Human-Computer Interaction Design | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/human-computer-interaction-design |
| Mathematics with Data Science | MSc | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/mathematics-with-data-science |
| Software Engineering with Cloud Computing | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/software-engineering |
| User Experience Engineering | MSc | Computer Science | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/user-experience-engineering |
| Advanced Aerospace Engineering with Sustainable Technologies | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-aerospace-engineering-with-sustainable-technologies |
| Advanced Mechanical Engineering | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/advanced-mechanical-engineering |
| Biomedical Engineering with Data Analytics | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/biomedical-engineering-with-data-analytics |
| Civil Engineering Structures | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/civil-engineering-structures |
| Maritime Operations and Management | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/maritime-operations-and-management |
| Maritime Safety and Security Management | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/maritime-safety-and-security-management |
| Renewable Energy and Power Systems Management | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/renewable-energy-and-power-systems-management |
| Robotics, AI and Autonomous Systems | MSc | Engineering | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/robotics-ai-autonomous-systems |
| Mathematics | MSc | Mathematics | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/mathematics |
| Technology, AI and Legal Services | LLM | Computer Science / Law | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/technology-ai-and-legal-services |

### 2.6 The City Law School (PGT 18 项)

| Program | Degree | URL |
|---------|--------|-----|
| Bar Vocational Studies (BVS) | LLM/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/bar-training |
| Business and Social Responsibility | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/business-and-social-responsibility |
| Criminal Law and Social Justice | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/criminal-law-and-social-justice |
| Diplomacy and Foreign Policy | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/diplomacy-and-foreign-policy |
| Dispute Resolution | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/dispute-resolution |
| Global Political Economy | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/global-political-economy |
| Graduate Diploma in Law (GDL) | GDL | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/conversion-diploma |
| Graduate Entry Law | LLB | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/conversion-llb |
| Intellectual Property Law | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/llm-in-intellectual-property-law |
| International Banking and Corporate Law | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-banking-and-corporate-law |
| International Commercial Law | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-commercial-law-llm |
| International Politics and Human Rights | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-politics-and-human-rights |
| International Politics | MA | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/international-politics |
| Maritime Law | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/maritime-law-llm |
| Master of Laws | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/master-of-laws-llm |
| Public International Law and Human Rights | LLM | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/public-international-law-and-human-rights |
| Solicitors' Practice Programme (SPP) | LLM/PGDip | https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/solicitors-training |

---

## SECTION 3 — Application requirements & deadlines

### 3.1 本科入学要求 (UG entry requirements)

| 项目 | 要求 |
|------|------|
| 最低要求 | Passes in two subjects at GCE A-level or equivalent |
| A-Level 等价 | 接受一系列国际等价学历 (详细列表见 entry-requirements 页) |
| 课程具体要求 | 由课程招生导师决定，**可能高于最低要求** |
| 录取决定 | 实际 offer 可能与公布的最低要求不同 (竞争激烈时) |

> **证据**: `https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements` — "To enter an undergraduate degree course at City St George's, you must satisfy City St George's general minimum requirement of passes in two subjects at GCE A-level or equivalent." | 抓取日期: 2026-07-08

### 3.2 研究生入学要求 (PG entry requirements)

| 项目 | 要求 |
|------|------|
| 标准要求 | University honours degree or equivalent in appropriate subject |
| 特殊情况 | 没有荣誉学位但有相关经验/专业资格也可能被录取 (由部门决定) |
| 录取前 | 需提交原始证书或经核证副本 |

### 3.3 英语语言要求 (English language requirements)

**校区差异**: City St George's 在两个主要校区对英语要求采用不同体系。

#### Clerkenwell 校区 (主要)

| 项目 | 要求 |
|------|------|
| 免考条件 | 来自主要英语国家国民 / 在主要英语国家完成学位 |
| 最低 IELTS | 见具体课程页面 (Clerkenwell 最低通常 **6.5**，单科不低于 **6.0**) |
| 其他测试 | 见 entry-requirements 页"Accepted tests"和"Accepted qualifications"标签 |
| 关键提示 | City St George's 不接受列表外的其他测试 |

> **证据**: `https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements` — "City St George's accepts the following as minimum English requirements for entry... Some courses have higher English language requirements for entry than these minimums." | 抓取日期: 2026-07-08

#### Tooting 校区 (Health & Medical Sciences)

| 项目 | 要求 |
|------|------|
| 免考条件 | 同 Clerkenwell |
| 三组分类 | UG / PG 课程分成 3 个不同的英语要求组 |
| 测试时效 | 所有英语测试必须在所选项目开学日期前 2 年内有效 |
| 三种证明方式 | (1) 接受的英语测试 (2) 适当的专业注册 (3) 适当的学历 |

### 3.4 申请截止日期

申请截止日期因课程而异。City St George's 采用滚动招生 (rolling admissions)，多数课程接受全年申请。建议参考各课程页面：
- UG: `https://www.citystgeorges.ac.uk/prospective-students/apply/how-to-apply/undergraduate`
- PG taught: `https://www.citystgeorges.ac.uk/prospective-students/apply/how-to-apply/postgraduate`
- PG research: `https://www.citystgeorges.ac.uk/prospective-students/apply/how-to-apply/research`

---

## SECTION 4 — Costs & financial aid

### 4.1 学费 (Tuition fees)

| 课程级别 | Home/UK (£) | International (£) |
|---------|-------------|--------------------|
| UG (典型) | **9,250** | 视课程而定 |
| PGT MSc Economics (示例) | **9,535** | **25,190** |
| PGT MSc Economics Part-time (年) | 4,768 | 12,600 |
| Medicine MBBS (UK) | 9,250 | 见具体课程 |

> **证据**: `https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics` — "£9,535... International: £25,190... Part-time per year... Home/UK: £4,768... International: £12,600" | 抓取日期: 2026-07-08

### 4.2 奖学金 (Scholarships)

| 奖学金 | 适用人群 | 折扣 |
|--------|---------|------|
| **Global Excellence Scholarship (GES)** | Overseas fee paying PGT 学生 | 见网站最新公告 |
| **Graduate Loyalty Discount** | legacy City / legacy St George's 校友 (self-funded) | **20% 学费减免** |

> **证据**: `https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics` — "Overseas fee paying students applying for this course are eligible for the Global Excellence Scholarship (GES)... Graduate Loyalty Discount of 20% on tuition fees to all our alumni" | 抓取日期: 2026-07-08

### 4.3 通胀调整

> "Where applicable, tuition fees for City's programmes will be subject to inflationary increases in each year of study."

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "City St George's, University of London"
  source_url: https://www.citystgeorges.ac.uk/about
  source_snippet: "City St George's, University of London"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.student_count
  value: "~27,000"
  source_url: https://www.citystgeorges.ac.uk/about
  source_snippet: "City St George's transforms the lives of around 27,000 students"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.merger
  value: "2024 merger of City, University of London + St George's, University of London"
  source_url: https://www.citystgeorges.ac.uk/about/our-schools
  source_snippet: "Schools and departments: School of Policy & Global Affairs..."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: courses.total
  value: "606 courses (UG + Foundation + PGT + PGR + Apprenticeships + Short Courses)"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses
  source_snippet: "Showing 1–10 of 606 courses"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: courses.ug_count
  value: "96 undergraduate degrees"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate
  source_snippet: course listing pagination
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-006:
  field: courses.pgt_count
  value: "157 postgraduate taught degrees"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate
  source_snippet: course listing pagination
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: fees.pgt_economics_home
  value: "£9,535"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics
  source_snippet: "£9,535"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: fees.pgt_economics_international
  value: "£25,190"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics
  source_snippet: "International: £25,190"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: fees.pgt_economics_pt_home
  value: "£4,768"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics
  source_snippet: "Part-time per year... Home/UK: £4,768"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: fees.pgt_economics_pt_international
  value: "£12,600"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics
  source_snippet: "Part-time per year... International: £12,600"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: scholarships.graduate_loyalty
  value: "20% off tuition fees for legacy City / legacy SGUL alumni (self-funded)"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/economics
  source_snippet: "Graduate Loyalty Discount of 20% on tuition fees to all our alumni"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: requirements.ug_minimum
  value: "Passes in two subjects at GCE A-level or equivalent"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements
  source_snippet: "City St George's general minimum requirement of passes in two subjects at GCE A-level"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: requirements.pg_minimum
  value: "University honours degree or equivalent in appropriate subject"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements
  source_snippet: "Applicants for all postgraduate degree courses should normally hold a university honours degree or equivalent"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: english_requirements.clerkenwell
  value: "IELTS minimum 6.5 (subscore 6.0); some courses higher; only listed tests accepted"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements
  source_snippet: "City St George's accepts the following as minimum English requirements for entry... City St George's cannot accept any other tests or qualifications"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: english_requirements.tooting
  value: "Three-group classification (UG/PG); three proof routes (test, professional registration, academic qualification); tests must be < 2 years old"
  source_url: https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements
  source_snippet: "English language requirements are handled slightly differently from elsewhere at City St George's... Please note: all English Language Tests must be dated within two years of the start date"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-016:
  field: platform
  value: "Drupal CMS + bayes.citystgeorges.ac.uk subdomain for Bayes Business School"
  source_url: https://www.citystgeorges.ac.uk/
  source_snippet: site architecture
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### 6.1 Chunk segmentation plan

| Chunk | Section | Size estimate |
|-------|---------|---------------|
| C0 | Institution overview + campus/merger context | ~1500 tokens |
| C1 | Schools hierarchy (6 schools + 23 departments) | ~800 tokens |
| C2 | UG programs list (96 items) | ~3500 tokens |
| C3 | PGT programs list (157 items) | ~5500 tokens |
| C4 | Entry requirements (UG + PG + English) | ~1200 tokens |
| C5 | Tuition fees + scholarships | ~600 tokens |
| C6 | Evidence chain index | ~1500 tokens |
| C7 | Monitoring watchlist | ~300 tokens |

### 6.2 Cross-cutting fields for filtering

All chunks indexed by: `school`, `department`, `degree_level`, `program_name`, `home_or_international`, `campus`, `category` (UG/PGT/PGR/Foundation/Apprenticeship/ShortCourse).

---

## SECTION 7 — Cross-school comparison framework

### 7.1 同类 UK 高校对比字段

| 字段 | City St George's | (用于 cross-comparison) |
|------|------------------|------------------------|
| Institution type | University of London (post-2024 merger) | Russell Group / 1994 Group / Million+ / etc. |
| Student count | ~27,000 | total enrolled |
| Total courses | 606 | UG + PGT + ... |
| UG fee (Home) | £9,250 | standard UK fee cap |
| International UG fee | varies | by major |
| PGT fee range | £9,535 – £25,190+ | programme-dependent |
| IELTS minimum | 6.5 (Clerkenwell) / varies (Tooting) | by school |
| Three-campus | Yes (Clerkenwell + Moorgate + Tooting) | multi-campus |

### 7.2 WeKnora 查询示例

- "City St George's 所有跟 AI 相关的硕士课程"
- "Tooting 校区医学相关本科项目清单"
- "Bayes Business School 2026/27 学费信息"
- "可申请的奖学金 (GES + Loyalty Discount) 详情"

### 7.3 Monitoring watchlist

| URL | Frequency | Reason |
|-----|-----------|--------|
| https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate/* | **High** | PGT fees change annually |
| https://www.citystgeorges.ac.uk/prospective-students/courses/undergraduate | Medium | New courses added each intake |
| https://www.citystgeorges.ac.uk/prospective-students/courses/postgraduate | Medium | New programmes added each intake |
| https://www.citystgeorges.ac.uk/prospective-students/apply/entry-requirements | Medium | English test thresholds reviewed periodically |
| https://www.citystgeorges.ac.uk/about/our-schools | Low | School/department structure rarely changes |
| https://www.citystgeorges.ac.uk/about | Low | Institution overview |

---

## Document metadata

- **Author**: uni-admissions-research skill (v2.0)
- **Data captured**: 2026-07-08
- **Last verified**: 2026-07-08
- **Cache files**:
  - `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/city-st-georges/site-memory.json`
  - `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/city-st-georges/last-extract.json`
  - `/Users/erik/Desktop/知识库预处理测试/uni-cache/schools/city-st-georges/content-hashes.json`
- **Output file**: `/Users/erik/Desktop/知识库预处理测试/knowledge-base/City_St_George's,_London_知识库_完整深度数据_v2.md`

E-U-011