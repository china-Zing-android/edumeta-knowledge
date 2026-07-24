# Nanyang Technological University (NTU) — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + urllib
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Singapore (SG)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| Dimension | Count |
|-----------|-------|
| 本科学位专业 (UG single-degree programmes) | 41 |
| 本科双主修 (Double Major programmes) | 22 |
| 双学位 (Double Degree programmes) | 6 |
| 本科学位+教育 (NIE Teacher Education programmes) | 16 |
| 本科学位+硕士 (REP — Renaissance Engineering Programme) | 1 |
| **本科项目总计 (UG programmes total)** | **86** |
| 本科辅修 (Minors) | 53 |
| 本科第二主修 (Second Majors) | 30 |
| 研究生授课型项目 (PGT — MSc/MA/MBA etc.) | ~110+ (待确认详细列表) |
| 研究生研究型项目 (PhD/Doctoral) | ~50+ (按学院分组) |
| **学位项目总计 (All degree programmes)** | **~246+** |
| 学院 (Colleges) | 6 |
| 学术院系 (Academic Schools/Departments) | 13 |
| 自主学院 (Autonomous Institutes) | 3 (NTU Honours College, NIE, RSIS) |

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Nanyang Technological University (NTU)
│
├── College of Business (Nanyang Business School — NBS)
│
├── College of Computing and Data Science (CCDS)
│
├── College of Engineering
│   ├── School of Chemistry, Chemical Engineering and Biotechnology (CCEB)
│   ├── School of Civil and Environmental Engineering (CEE)
│   ├── School of Electrical and Electronic Engineering (EEE)
│   ├── School of Mechanical and Aerospace Engineering (MAE)
│   └── School of Materials Science and Engineering (MSE)
│
├── College of Humanities, Arts and Social Sciences (HASS)
│   ├── School of Art, Design and Media (ADM)
│   ├── School of Humanities (SOH)
│   ├── School of Social Sciences (SSS)
│   └── Wee Kim Wee School of Communication and Information (WKWSCI)
│
├── College of Science
│   ├── School of Chemistry, Chemical Engineering and Biotechnology (CCEB) [跨学院]
│   ├── School of Biological Sciences (SBS)
│   ├── School of Physical and Mathematical Sciences (SPMS)
│   └── The Asian School of the Environment (ASE)
│
├── Lee Kong Chian School of Medicine (LKCMedicine)
│
├── National Institute of Education (NIE) — 自主学院
│
├── S. Rajaratnam School of International Studies (RSIS) — 自主学院
│
├── NTU Honours College
│
└── Interdisciplinary & Cross-College Programmes
    ├── Renaissance Engineering Programme (REP)
    ├── NTU Entrepreneurship Academy (NTUpreneur)
    └── NTU Institute for Digital Medicine
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学历级别 (Canonical) | 全称 | 数量 (approx.) |
|----------------------|------|----------------|
| **Undergraduate** | | |
| BAcc | Bachelor of Accountancy | 2 |
| BAcc(SMA) | Bachelor of Accountancy (Sustainability Mgmt & Analytics) | 1 |
| BA | Bachelor of Arts | 7+ |
| BAppCompFin | Bachelor of Applied Computing in Finance | 1 |
| BBus | Bachelor of Business | 1 |
| BCom | Bachelor of Communication Studies | 1 |
| BComp | Bachelor of Computing | 4 |
| BCM | Bachelor of Chinese Medicine | 1 |
| BEng | Bachelor of Engineering | 12 |
| BFA | Bachelor of Fine Arts | 1 |
| BSc | Bachelor of Science | 7 |
| BSocSci | Bachelor of Social Sciences | 5 |
| BAcc+BBus | Bachelor of Accountancy + Business (Double Degree) | 1 |
| BTech | Bachelor of Technology | 1 |
| MBBS | Bachelor of Medicine and Bachelor of Surgery | 1 |
| BEngSc | Bachelor of Engineering Science | 1 |
| **Graduate (Coursework — PGT)** | | |
| MA | Master of Arts | ~10 |
| MSc | Master of Science | ~60+ |
| MBA | Master of Business Administration | ~3 |
| MEng | Master of Engineering | ~10 |
| MEd | Master of Education | ~5 |
| MM | Master of Medicine | ~2 |
| LLM | Master of Laws | ~2 |
| MPA | Master of Public Administration | ~2 |
| MSSc | Master of Social Science | ~3 |
| PG Dip | Postgraduate Diploma | ~5 |
| PG Cert | Postgraduate Certificate | ~3 |
| **Graduate (Research — PhD)** | | |
| PhD | Doctor of Philosophy | ~50+ (所有学院) |
| EdD | Doctor of Education | ~2 |
| MPhil | Master of Philosophy | ~10 |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

**UG Programmes (Single Degree + Double Major + Double Degree + Education + REP) by College:**

| College | BAcc | BA | BAppCompFin | BBus | BCom | BComp | BCM | BEng | BEngSc | BFA | BSc | BSocSci | BTech | MBBS | Total |
|---------|------|-----|------------|------|------|-------|-----|------|--------|-----|-----|---------|-------|------|-------|
| College of Business (NBS) | 2 | - | - | 1 | - | - | - | - | - | - | - | - | - | - | **3** |
| College of Computing & Data Science | - | - | 1 | - | - | 4 | - | - | - | - | - | - | 1 | - | **6** |
| College of Engineering | - | - | - | - | - | - | - | 11 | 1 | - | - | - | - | - | **12** |
| College of HASS | - | 7 | - | - | 1 | - | - | 1 | - | 1 | 1 | 5 | - | - | **16** |
| College of Science | - | - | - | - | - | - | - | - | - | - | 6 | - | - | - | **6** |
| LKC Medicine | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | **1** |
| NIE (Teacher Ed) | - | 8 | - | - | - | - | - | - | - | - | 7 | - | - | - | **15** |
| Cross-College/DD | - | - | - | - | - | - | - | - | - | - | - | - | - | - | **6** |
| REP | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | **1** |
| **Total UG** | **2** | **15** | **1** | **1** | **1** | **4** | **1** | **12** | **1** | **1** | **14** | **5** | **1** | **1** | **66** |

> Note: The 20 Double Major programmes within HASS / Science that already include 2 subject names are counted as single degree programmes above. Total UG = 41 single + 22 double major + 6 double degree + 16 education + 1 REP = 86.

---

## Section 1 — Undergraduate Education (Full Program List)

### 1.1 College of Business (Nanyang Business School)

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Accountancy | BAcc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-accountancy |
| Accountancy (Sustainability Management and Analytics) | BAcc(SMA) | https://www.ntu.edu.sg/education/undergraduate-programme/accountancy-for-future-leaders-bachelor-of-accountancy-in-sustainability-management-and-analytics |
| Business | BBus | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-business |

### 1.2 College of Computing and Data Science

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Applied Computing in Finance | BAppCompFin | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-applied-computing-in-finance |
| Artificial Intelligence and Society | BComp | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-hons-in-artificial-intelligence-and-society |
| Computer Science | BComp | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-computing-in-computer-science |
| Data Science and Artificial Intelligence | BComp | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-data-science-artificial-intelligence |
| Computing (Part-time) | BTech | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-technology-in-computing-skillsfuture-work-study-degree |

### 1.3 College of Engineering

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Aerospace Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-aerospace-engineering |
| Bioengineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-bioengineering |
| Chemical and Biomolecular Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-chemical-and-biomolecular-engineering |
| Civil Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-civil-engineering |
| Computer Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-computer-engineering |
| Electrical and Electronic Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-electrical-and-electronic-engineering-(eee) |
| Environmental Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-environmental-engineering |
| Information Engineering and Media | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-information-engineering-and-media-iem |
| Materials Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-materials-engineering |
| Mechanical Engineering | BEng | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-engineering-in-mechanical-engineering |
| Robotics | BEng | https://www.ntu.edu.sg/mae/admissions/undergraduate-programmes/detail/bachelor-of-engineering-in-robotics |

### 1.4 College of Humanities, Arts and Social Sciences

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Art, Design and Media | BFA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-art-design-media |
| Chinese | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-in-chinese |
| Chinese Medicine | BCM | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-chinese-medicine |
| Communication Studies | BCom | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-communication-studies |
| Economics | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-in-economics-(honours) |
| Economics and Data Science | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-economics-and-data-science |
| English | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-in-english |
| History | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-in-history |
| Linguistics and Multilingual Studies | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-linguistics-and-multilingual-studies |
| Philosophy | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-philosophy |
| Philosophy, Politics, and Economics | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-science-in-philosophy-politics-and-economics |
| Psychology | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-in-psychology-(honours) |
| Public Policy and Global Affairs | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-in-public-policy-and-global-affairs-(honours) |
| Sociology | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-in-sociology-(honours) |

### 1.5 College of Science

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Biological Sciences | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-biological-sciences |
| Chemistry and Biological Chemistry | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-chemistry-and-biological-chemistry |
| Environmental Earth Systems Science | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-(bsc)-in-environmental-earth-systems-science |
| Maritime Studies | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-maritime-studies |
| Mathematical Sciences | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-mathematical-sciences |
| Physics and Applied Physics | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-physics-applied-physics |

### 1.6 Lee Kong Chian School of Medicine

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Medicine | MBBS | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-medicine-and-bachelor-of-surgery-(mbbs) |

### 1.7 Double Major Programmes (学院交叉)

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Biological Sciences and Psychology | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-biological-sciences-and-psychology |
| Biomedical Sciences and BioBusiness | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-biomedical-sciences-and-biobusiness |
| Chinese and English | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---chinese-and-english |
| Chinese and Linguistics and Multilingual Studies | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---chinese-and-linguistics-and-multilingual-studies |
| Economics and Media Analytics | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-(hons)-in-double-major---economics-and-media-analytics |
| Economics and Psychology | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-(hons)-in-double-major---economics-and-psychology |
| Economics and Public Policy and Global Affairs | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-(hons)-in-double-major---economics-and-public-policy-global-affairs |
| English and History | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---english-and-history |
| English and Philosophy | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---english-and-philosophy |
| English Literature and Art History | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---english-literature-and-art-history |
| Environmental Earth Systems Science and Public Policy & Global Affairs | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-environmental-earth-systems-science-and-public-policy-and-global-affairs |
| History and Chinese | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---history-and-chinese |
| History and Linguistics and Multilingual Studies | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---history-and-linguistics-and-multilingual-studies |
| Linguistics and Multilingual Studies and English | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---linguistics-and-multilingual-studies-and-english |
| Linguistics and Multilingual Studies and Philosophy | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---linguistics-and-multilingual-studies-and-philosophy |
| Mathematical and Computer Sciences | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-mathematical-and-computer-sciences |
| Mathematical Sciences and Economics | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-mathematical-sciences-and-economics |
| Philosophy and Chinese | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---philosophy-and-chinese |
| Philosophy and History | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---philosophy-and-history |
| Physics and Mathematical Sciences | BSc | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-science-in-physics-and-mathematical-sciences |
| Process Engineering and Synthetic Chemistry | BEngSc | https://www.ntu.edu.sg/cceb/admissions/detail/bachelor-of-engineering-science-with-double-majors-in-process-engineering-and-synthetic-chemistry |
| Psychology and Media Analytics | BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-social-sciences-(hons)-in-double-major---psychology-and-media-analytics |
| Psychology and Linguistics and Multilingual Studies | BA | https://www.ntu.edu.sg/education/undergraduate-programme/bachelor-of-arts-(hons)-in-double-major---psychology-and-linguistics-multilingual-studies |

### 1.8 Double Degree Programmes

| Programme | Degree Types | URL |
|-----------|-------------|------|
| Accountancy and Business | BAcc + BBus | https://www.ntu.edu.sg/education/undergraduate-programme/double-degree-in-accountancy-business |
| Accountancy and Data Science & AI | BAcc + BComp | https://www.ntu.edu.sg/education/undergraduate-programme/double-degree-in-accountancy-and-science |
| Business and Computing | BBus + BComp | https://www.ntu.edu.sg/education/undergraduate-programme/double-degree-in-business-and-computer-engineering-or-computer-science |
| Business and Computer Engineering | BBus + BEng | https://www.ntu.edu.sg/education/undergraduate-programme/double-degree-in-computer-engineering-and-business-(specialisation-in-business-analytics) |
| Computer Science and Economics | BComp + BSocSci | https://www.ntu.edu.sg/education/undergraduate-programme/double-degree-in-computer-science-and-economics |
| Engineering+ and Economics | BEng+ + BSocSci | https://www.ntu.edu.sg/admissions/undergraduate-programmes |

### 1.9 Renaissance Engineering Programme

| Programme | Degree Types | URL |
|-----------|-------------|------|
| Renaissance Engineering Programme | BEngSc + MSc (Tech Mgmt) | https://www.ntu.edu.sg/education/undergraduate-programme/renaissance-engineering-programme-(rep) |

### 1.10 National Institute of Education — Teacher Education Programmes

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Art and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Chinese Studies and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Drama and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| English Language & Linguistics and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| English Literature and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Geography and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| History and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Malay Studies and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Music and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Tamil Studies and Education | BA | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Biology and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Chemistry and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Food & Consumer Sciences and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Mathematics & Computational Thinking and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Sport Science and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |
| Physics & Energy Studies and Education | BSc | https://nie.edu.sg/te-undergraduate/undergraduate-programmes |

### 1.11 Sport Science and Management

| Programme | Degree Type | URL |
|-----------|-------------|-----|
| Sport Science and Management | BSc | https://nie.edu.sg/our-people/academic-groups/physical-education-and-sports-science/programmes/sport-science-management-ssm |

---

## Section 2 — Graduate Education

### 2.1 Graduate Programmes by Coursework (选修型) — 主要学院汇总

NTU offers a wide range of Graduate Programmes by Coursework (PGT). The full list is maintained on the Graduate Programmes (Coursework) page:
https://www.ntu.edu.sg/admissions/graduate/coursework

Key programmes include (not exhaustive — full PG list needed as P0 follow-up):

**College of Business (Nanyang Business School):**
| Programme | Degree | URL |
|-----------|--------|-----|
| Nanyang MBA | MBA | https://www.ntu.edu.sg/business/programmes/graduate/nanyang-mba |
| Nanyang Professional MBA (Part-time) | MBA | https://www.ntu.edu.sg/business/programmes/graduate/nanyang-professional-mba |
| MSc Accountancy | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-accountancy |
| MSc Financial Engineering | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-financial-engineering |
| MSc Business Analytics | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-business-analytics |
| MSc Marketing Science | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-marketing-science |
| MSc Finance | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-finance |
| MSc Asset & Wealth Management | MSc | https://www.ntu.edu.sg/business/programmes/graduate/msc-asset-and-wealth-management |

**College of Engineering:**
| Programme | Degree | URL |
|-----------|--------|-----|
| MSc in Sustainability and Environmental Engineering | MSc | https://www.ntu.edu.sg/education/graduate-programme/master-of-science-in-sustainability-and-environmental-engineering |
| MSc in Engineering Management | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |
| MSc in Nanotechnology and Nanoscience | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |
| MSc in Applied Materials Analytics | MSc | https://www.ntu.edu.sg/education/graduate-programme/master-of-science-in-applied-materials-analytics |
| MSc (Robotics and Intelligent Systems) | MSc | https://www.ntu.edu.sg/education/graduate-programme/master-of-science-(robotics-and-intelligent-systems) |
| MSc (AI in Medicine) | MSc | https://www.ntu.edu.sg/education/graduate-programme/master-of-science-(ai-in-medicine) |

**College of Humanities, Arts and Social Sciences:**
| Programme | Degree | URL |
|-----------|--------|-----|
| MA in Museum Studies and Curatorial Practices | MA | https://www.ntu.edu.sg/education/graduate-programme/master-in-museums-studies-and-curatorial-practices |
| MA in Digital Humanities | MA | https://www.ntu.edu.sg/education/graduate-programme/... |
| MA (Applied Psychology) | MA | https://www.ntu.edu.sg/education/graduate-programme/master-of-arts-(applied-psychology) |
| Master of Media and Communication | MMComm | https://www.ntu.edu.sg/education/graduate-programme/master-of-media-and-communication |
| MSc in BioBusiness and BioEntrepreneurship | MSc | https://www.ntu.edu.sg/education/graduate-programme/master-of-science-in-biobusiness-and-bioentrepreneurship-msbbb |

**College of Computing and Data Science:**
| Programme | Degree | URL |
|-----------|--------|-----|
| MSc in Artificial Intelligence | MSc | https://www.ntu.edu.sg/computing/programmes/graduate/msc-in-artificial-intelligence |
| MSc in Data Science | MSc | https://www.ntu.edu.sg/computing/programmes/graduate/msc-in-data-science |
| MSc in Cyber Security | MSc | https://www.ntu.edu.sg/computing/programmes/graduate/msc-in-cyber-security |
| MSc in Enterprise Artificial Intelligence | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |

**College of Science:**
| Programme | Degree | URL |
|-----------|--------|-----|
| MSc in Chemical Sciences and Instrumentation | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |
| MSc in Environmental Sustainability Science | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |
| MSc in Biomedical Data Science | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |
| Master in Management | MMgt | https://www.ntu.edu.sg/education/graduate-programme/... |

**Lee Kong Chian School of Medicine:**
| Programme | Degree | URL |
|-----------|--------|-----|
| MSc in Translational Medicine | MSc | https://www.ntu.edu.sg/education/graduate-programme/... |

### 2.2 Graduate Programmes by Research

Research degrees (PhD and MPhil) are offered across all Colleges and Schools. Key research programmes include:

**Doctoral Programmes by College:**
- College of Business (NBS): PhD in Business
- College of Computing and Data Science: PhD in Computer Science, PhD in Data Science
- College of Engineering: PhD in Engineering (various specialisations)
- College of HASS: PhD in Humanities, PhD in Social Sciences, PhD in Communication Studies
- College of Science: PhD in Biological Sciences, PhD in Chemistry, PhD in Physics, PhD in Mathematics, PhD in Environmental Science
- LKCMedicine: PhD in Medicine
- NIE: PhD in Education
- RSIS: PhD in International Studies

> **Note:** Full PG programme list extraction is a P0 follow-up item. NTU offers ~110+ PGT programmes and ~50+ PhD programmes across all schools.

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admissions

**Application Period (Typical):**
- Opening: ~mid-November of preceding year
- Closing: ~mid-March of intake year
- Outcome notification: February–July (batched)
- Matriculation: July–August
- Classes start: ~mid-August

**Accepted Qualifications:**
1. **Singapore-Cambridge GCE A-Levels** — 3 H2 + 1 H1 content-based subjects
2. **Polytechnic Diploma** — GPA-based admission from Singapore polytechnics
3. **IB Diploma** — Group 1 (local IB schools) and Group 2 (international)
4. **NUS High School Diploma**
5. **International Qualifications** — 25+ international systems

**English Language Requirements (for international applicants):**
- IELTS: Minimum 6.0 overall (some programmes require 6.5+)
- TOEFL (iBT): Minimum 90
- PTE Academic: Minimum 55
- SAT: Evidence-Based Reading & Writing and Math (score depends on programme)
- C1 Advanced: Pass

**Standardised Test Scores (for international qualifications):**
- SAT / ACT for US-system applicants
- Specific subject prerequisites for each programme

**Aptitude-Based Admissions (ABA):**
- Holistic assessment including academic results + co-curricular activities
- Leadership, community service, awards, internships considered
- Interview for shortlisted applicants (mandatory for some programmes)

### 3.2 Graduate Admissions (Coursework)

**Application Period:**
- Varies by programme (typically November–March for August intake)
- Some programmes have January intake (July–September application)

**General Requirements:**
- Bachelor's degree from a recognised university
- Minimum GPA / honours classification (typically Second Class Honours or equivalent)
- English proficiency (if prior degree not in English):
  - IELTS: 6.0–7.0 (varies by programme)
  - TOEFL: 85–100 (varies by programme)
- Work experience required for MBA programmes
- GMAT/GRE for some programmes (e.g., MBA, Financial Engineering)

**Specific Requirements:**
- Portfolio for Art, Design and Media programmes
- Interview for selected programmes
- Research proposal for research programmes

### 3.3 Graduate Admissions (Research)

**Application Period:**
- Open throughout the year (2 intakes: August and January)
- Scholarship deadlines: typically October (for August intake) and April (for January intake)

**General Requirements:**
- Bachelor's degree with Honours (at least Second Class Upper or equivalent)
- Master's degree for PhD (for some programmes)
- Research proposal outlining intended research area
- Academic transcripts and referee reports
- English proficiency as above

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition Fees (AY2026 — Accepted Offer in 2026)

Annual tuition fees in Singapore dollars (S$), for full-time programmes:

| Programme Category | SC Subsidised | SPR Subsidised | ASEAN Intl (Subsidised) | Other Intl (Subsidised) | Non-Subsidised |
|-------------------|--------------|----------------|------------------------|------------------------|----------------|
| All programmes (except listed below) — Lab Based | $8,300 | $11,600 | $18,050 | $21,400 | $40,600 |
| All programmes — Non-Lab Based | — | — | — | — | $36,350 |
| Accountancy / Business / Accounting & Business / Business & Computing / Business & Computer Engineering | $9,500 | $13,300 | $20,700 | $21,800 | $45,600 |
| Medicine (MBBS) | $36,100 | $51,850 | $80,850 | $91,250 | N/A |
| Renaissance Engineering Programme | $13,500 | $20,100 | $31,000 | $32,000 | N/A |

> Notes:
> - SC = Singapore Citizens; SPR = Singapore Permanent Residents; IS = International Students
> - ASEAN includes: Brunei, Cambodia, Indonesia, Lao PDR, Malaysia, Myanmar, Philippines, Singapore, Thailand, Timor-Leste, Vietnam
> - Fees shown for subsidised students exclude GST (borne by MOE)
> - Non-subsidised fees include GST
> - Annual tuition fee is fixed at the 2026 rate for the duration of the degree programme

### 4.2 Miscellaneous Fees (UG)

- Miscellaneous Student Fees (annual): ~S$227 (SC/SPR), ~S$291 (International)
- Term-specific fees for Special Term (vacation courses)

### 4.3 MOE Tuition Grant

| Residency | Grant Tier | Bond Requirement |
|-----------|-----------|------------------|
| Singapore Citizen | Automatic (highest subsidy) | None |
| Singapore PR | Must apply | 3-year work bond for Singapore entity |
| International Student | Limited, merit-based | 3-year work bond for Singapore entity |
| Non-subsidised | No grant | No bond, but pay 2-4× subsidised fees |

### 4.4 Scholarships (UG)

NTU offers scholarships including:
- **NTU Scholarships** — Full tuition + living allowance (merit-based)
- **NTU-University Scholars Programme (NTU-USP)** — Enhanced curriculum + scholarship
- **College-specific scholarships** — Per college/school
- **ASEAN Undergraduate Scholarships** — For ASEAN international students
- **Sports & Arts Scholarships** — For students with exceptional talent

### 4.5 Graduate Tuition Fees (PGT)

> **P0 follow-up**: PG tuition fee data is in PDF format on the page https://www.ntu.edu.sg/admissions/graduate/financialmatters/pgtuitionfees. Links to "Tuition and Other Fees AY2025-2026" (subsidised and non-subsidised) contain the detailed fee tables. Typical PG tuition ranges from S$20,000–S$80,000 depending on programme. MBA fees are typically higher (~S$60,000–S$80,000).

### 4.6 Graduate Scholarships

- **NTU Research Scholarship** — Covers tuition + monthly stipend for PhD students
- **NTU President's Graduate Scholarship** — Enhanced stipend for outstanding PhD students
- **Singapore International Graduate Award (SINGA)** — For international PhD students
- **NTU Postgraduate Incentives** — Various tuition fee rebates

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|------------|---------------|
| E-U-001 | institution.name | "Nanyang Technological University (NTU)" | https://www.ntu.edu.sg/ | official_webpage |
| E-U-002 | counts.ug_single_degree | 41 | https://www.ntu.edu.sg/education/degree-programmes | official_webpage_table |
| E-U-003 | counts.ug_double_major | 22 | https://www.ntu.edu.sg/education/degree-programmes | official_webpage_table |
| E-U-004 | counts.ug_double_degree | 6 | https://www.ntu.edu.sg/education/degree-programmes | official_webpage_table |
| E-U-005 | counts.teacher_education | 16 | https://www.ntu.edu.sg/education/degree-programmes | official_webpage_table |
| E-U-006 | counts.ug_total | 86 | https://www.ntu.edu.sg/education/degree-programmes | derived_count |
| E-U-007 | hierarchy.colleges | 6 Colleges | https://www.ntu.edu.sg/education/colleges-schools | official_webpage |
| E-U-008 | hierarchy.schools | 13+ Schools | https://www.ntu.edu.sg/education/colleges-schools | official_webpage |
| E-U-009 | tuition.ug.base_sc_2026 | "$8,300" | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 | official_webpage_table |
| E-U-010 | tuition.ug.business_sc_2026 | "$9,500" | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 | official_webpage_table |
| E-U-011 | tuition.ug.medicine_sc_2026 | "$36,100" | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 | official_webpage_table |
| E-U-012 | tuition.ug.rep_sc_2026 | "$13,500" | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 | official_webpage_table |
| E-U-013 | tuition.ug.non_subsidised_base | "$36,350 – $40,600" | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-fees/accepted-programme-offer-in-2026 | official_webpage_table |
| E-U-014 | application.ug.accepted_quals | GCE A-Level, Poly Diploma, IB, NUS High, Intl | https://www.ntu.edu.sg/admissions/undergraduate/admission-guide | official_webpage |
| E-U-015 | application.ug.english_requirements | IELTS 6.0+, TOEFL 90+, PTE 55+ | https://www.ntu.edu.sg/admissions/undergraduate/admission-guide/international-qualifications | official_webpage |
| E-U-016 | application.ug.aba | Aptitude-Based Admissions | https://www.ntu.edu.sg/admissions/undergraduate/admission-guide/Aptitude-based-Admissions | official_webpage |
| E-U-017 | igp.link | NTU IGP PDF | https://www.ntu.edu.sg/docs/default-source/undergraduate-admissions/igp/ntu_igp.pdf | official_pdf |
| E-U-018 | hierarchy.college_of_business | Nanyang Business School | https://www.ntu.edu.sg/education/colleges-schools/college-of-business-(nanyang-business-school) | official_webpage |
| E-U-019 | hierarchy.college_of_computing | College of Computing and Data Science | https://www.ntu.edu.sg/education/colleges-schools/college-of-computing-and-data-science | official_webpage |
| E-U-020 | hierarchy.college_of_engineering | College of Engineering | https://www.ntu.edu.sg/education/colleges-schools/college-of-engineering | official_webpage |
| E-U-021 | hierarchy.hass | College of Humanities, Arts and Social Sciences | https://www.ntu.edu.sg/education/colleges-schools/college-of-humanities--arts-and-social-sciences | official_webpage |
| E-U-022 | hierarchy.college_of_science | College of Science | https://www.ntu.edu.sg/education/colleges-schools/college-of-science | official_webpage |
| E-U-023 | hierarchy.lkcmedicine | Lee Kong Chian School of Medicine | https://www.ntu.edu.sg/education/colleges-schools/lee-kong-chian-school-of-medicine | official_webpage |
| E-U-024 | hierarchy.nie | National Institute of Education | https://www.ntu.edu.sg/education/colleges-schools/national-institute-of-education | official_webpage |
| E-U-025 | hierarchy.rsis | S. Rajaratnam School of International Studies | https://www.ntu.edu.sg/education/colleges-schools/s.rajaratnam-school-of-international-studies | official_webpage |
| E-U-026 | tuition.ug.moe_grant | MOE Tuition Grant system | https://www.ntu.edu.sg/admissions/undergraduate/financial-matters/tuition-grants | official_webpage |

---

## Section 6 — WeKnora Import Manifest

### 6.1 Chunk Configuration

| Chunk | Content | Token Estimate |
|-------|---------|---------------|
| chunk-00 | Section 0 (Overview + Counts + Hierarchy + Matrix) | ~2,000 |
| chunk-01 | Section 1.1–1.6 (UG Programmes by College) | ~3,000 |
| chunk-02 | Section 1.7–1.11 (Double Major, Double Degree, REP, NIE) | ~2,500 |
| chunk-03 | Section 2 (Graduate Programmes) | ~2,500 |
| chunk-04 | Section 3 (Application Requirements) | ~2,000 |
| chunk-05 | Section 4 (Costs & Financial Aid) | ~2,000 |
| chunk-06 | Section 5–7 (Evidence, Monitoring, Comparison) | ~1,500 |

### 6.2 Follow-up Data Items (Prioritized)

| Priority | Data Item | Rationale |
|----------|-----------|-----------|
| **P0** | Full PGT programme list (~110+) | Extracted only sample; need complete per-school list |
| **P0** | Full PhD programme list (~50+) | Research areas per school |
| **P0** | PG tuition fees AY2026-27 (subsidised and non-subsidised) | Data in PDF; needs extraction |
| **P0** | IGP data extraction (PDF → structured) | Grade profiles in PDF at ntu_igp.pdf |
| **P1** | Indicative Grade Profile (IGP) tables for A-Level and Poly | Cross-reference academic competitiveness |
| **P1** | English language requirement details per programme | Some programmes have higher requirements |
| **P1** | Application deadlines by intake | Varies by programme |
| **P2** | Cost of living estimates | Not on NTU website (Singapore-wide data) |
| **P2** | Alumni outcomes / employment data | Available in Graduate Employment Survey |
| **P2** | Detailed scholarship terms | Available on scholarship pages |

---

## Section 7 — Cross-School Comparison Framework

> NTU is the first Singapore university being researched in this batch. Comparison with NUS, SMU, SUTD will be added as they are completed.

| Dimension | NTU |
|-----------|-----|
| Total UG Programmes | 86 |
| Total PGT Programmes | ~110+ (P0) |
| Total PhD Programmes | ~50+ (P0) |
| Number of Colleges | 6 |
| Number of Academic Schools | 13+ |
| Autonomous Institutes | 3 (NIE, RSIS, Honours College) |
| QS World Ranking 2027 | #12 |
| QS World Ranking 2026 | #15 |
| MOE Tuition Grant | Yes (SC/SPR/ASEAN IS/Other IS tiers) |
| Holistic Admissions | Yes (ABA for UG) |
| Common Acceptance Platform | Yes (with NUS, SMU, SUTD, SIT, SUSS) |
| Fixed Fee Model | Yes (rate locked for cohort duration) |
| Medicine | MBBS (joint with Imperial College London) |
| Teacher Education | Yes (via NIE) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: NTU Singapore official website (https://www.ntu.edu.sg/)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (86 listed) | PG programmes ⚠️ (sample only, P0 follow-up) | Evidence (26 blocks) ✅
> **Next step**: Extract full PGT programme list per school from NTU graduate programme pages; extract PhD programme list; extract PG tuition fees from PDFs; extract IGP tables from PDF.
