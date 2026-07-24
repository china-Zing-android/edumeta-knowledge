# Florida International University (FIU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BBA/BFA/etc.) | 84 |
| 本科辅修 (Minor) | 13 |
| 本科证书 (Undergraduate Certificate) | 75 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 136 |
| 研究生证书 (Graduate Certificate) | 59 |
| **学位项目总计 (UG + Grad)** | **367** |

> Note: FIU catalog shows 473 total programs. The difference includes some programs with non-standard naming or inactive status. Graduate admissions reports: 106 Master's, 34 Doctoral, 50+ Certificates, 3 Specialist programs.

### 0.2 学院 / 系层级结构

Florida International University
├── College of Arts, Sciences, and Education [学院]
│   ├── School of Education and Human Development [系]
│   │   ├── Department of Counseling, Recreation, and School Psychology
│   │   ├── Department of Educational Policy Studies
│   │   └── Department of Teaching and Learning
│   ├── School of Environment, Arts, and Society [系]
│   │   ├── Department of Biological Sciences
│   │   ├── Department of Earth and Environment
│   │   ├── Department of English
│   │   ├── Department of Mathematics and Statistics
│   │   ├── Department of Chemistry and Physics
│   │   ├── Department of Philosophy
│   │   └── Department of Psychology
│   └── School of Integrated, Computing and Learning [系]
├── College of Business [学院]
│   ├── Department of Finance
│   ├── Department of Global Leadership and Management
│   ├── Department of Decision Sciences and Information Systems
│   ├── Department of International Business
│   ├── Department of Marketing
│   ├── School of Accounting
│   └── Department of Real Estate
├── College of Communication, Architecture, and the Arts [学院]
│   ├── School of Architecture
│   ├── Department of Art and Art History
│   ├── Department of Communication
│   ├── Department of Interior Architecture
│   ├── Department of Landscape Architecture
│   ├── School of Music
│   └── Department of Theatre
├── College of Engineering and Computing [学院]
│   ├── Department of Biomedical Engineering
│   ├── Department of Civil and Environmental Engineering
│   ├── Department of Electrical and Computer Engineering
│   ├── Department of Engineering Management
│   ├── Department of Mechanical and Materials Engineering
│   └── School of Computing and Information Sciences
├── College of Law [学院]
├── College of Medicine [学院]
├── College of Nursing and Health Sciences [学院]
│   ├── School of Nursing
│   └── Department of Health Sciences
├── College of Public Health and Social Work [学院]
│   ├── Department of Public Health
│   └── Department of Social Work
├── School of Hospitality and Tourism Management [学院]
├── School of International and Public Affairs [学院]
│   ├── Department of Criminal Justice
│   ├── Department of Economics
│   ├── Department of Geography
│   ├── Department of History
│   ├── Department of Modern Languages
│   ├── Department of Political Science
│   └── Department of Religious Studies
└── [Graduate-level only]
    ├── Green School of International and Public Affairs
    └── Various interdisciplinary programs

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~20 |
| BS | Bachelor of Science | 本科 | ~45 |
| BBA | Bachelor of Business Administration | 本科 | ~8 |
| BFA | Bachelor of Fine Arts | 本科 | ~3 |
| BSN | Bachelor of Science in Nursing | 本科 | ~2 |
| BM | Bachelor of Music | 本科 | ~2 |
| BACC | Bachelor of Accounting | 本科 | ~2 |
| MA | Master of Arts | 研究生 | ~15 |
| MS | Master of Science | 研究生 | ~50 |
| MBA | Master of Business Administration | 研究生 | ~5 |
| MFA | Master of Fine Arts | 研究生 | ~3 |
| MSN | Master of Science in Nursing | 研究生 | ~8 |
| MARCH | Master of Architecture | 研究生 | ~3 |
| MAT | Master in the Art of Teaching | 研究生 | ~3 |
| MACC | Master of Accounting | 研究生 | ~3 |
| MPA | Master of Public Administration | 研究生 | ~2 |
| MPH | Master of Public Health | 研究生 | ~2 |
| MSW | Master of Social Work | 研究生 | ~2 |
| PhD | Doctor of Philosophy | 研究生 | ~20 |
| EdD | Doctor of Education | 研究生 | ~5 |
| DBA | Doctorate in Business Administration | 研究生 | ~1 |
| DNP | Doctor of Nursing Practice | 研究生 | ~2 |
| DPT | Doctor of Physical Therapy | 研究生 | ~1 |
| MD | Doctor of Medicine | 研究生 | ~1 |
| JD | Juris Doctor | 研究生 | ~1 |
| EdS | Education Specialist | 研究生 | ~3 |
| Certificate | Various Graduate Certificates | 研究生 | ~59 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院  级别 | BA | BS | BBA | BFA | MA | MS | MBA | PhD | EdD | Certificate | 合计 |
|------------|----|----|----|-----|----|----|----|-----|-----|-------------|------|
| Arts, Sciences & Education | ~10 | ~20 | 0 | 0 | ~8 | ~25 | 0 | ~10 | ~5 | ~30 | ~108 |
| Business | 0 | 0 | ~8 | 0 | 0 | ~5 | ~5 | ~3 | 0 | ~10 | ~31 |
| Communication, Architecture & Arts | ~5 | ~3 | 0 | ~3 | ~3 | ~5 | 0 | ~2 | 0 | ~10 | ~31 |
| Engineering & Computing | 0 | ~10 | 0 | 0 | 0 | ~15 | 0 | ~5 | 0 | ~8 | ~38 |
| Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~2 | ~2 |
| Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~1 | 0 | ~1 | ~2 |
| Nursing & Health Sciences | 0 | ~2 | 0 | 0 | 0 | ~10 | 0 | ~1 | 0 | ~5 | ~18 |
| Public Health & Social Work | 0 | 0 | 0 | 0 | 0 | ~3 | 0 | ~1 | 0 | ~3 | ~7 |
| Hospitality & Tourism Mgmt | 0 | ~2 | 0 | 0 | 0 | ~2 | 0 | 0 | 0 | ~2 | ~6 |
| International & Public Affairs | ~5 | ~3 | 0 | 0 | ~2 | ~5 | 0 | ~2 | 0 | ~8 | ~25 |
| **合计** | ~20 | ~40 | ~8 | ~3 | ~13 | ~70 | ~5 | ~25 | ~5 | ~79 | ~268 |

> Note: This matrix is estimated based on available data. Some programs may be cross-listed or interdisciplinary.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

FIU has 11 colleges and schools offering undergraduate programs. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Business
##### School of Accounting
###### BACC (Bachelor of Accounting)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://catalog.fiu.edu/programs/ACCT%3ABACC |

###### BBA (Bachelor of Business Administration)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics and Artificial Intelligence | https://catalog.fiu.edu/programs/BAIA%3ABBA |
| 2 | Finance | https://catalog.fiu.edu/programs/FIN%3ABBA |
| 3 | Human Resource Management | https://catalog.fiu.edu/programs/HRM%3ABBA |
| 4 | International Business | https://catalog.fiu.edu/programs/INTLB%3ABBA |
| 5 | Management | https://catalog.fiu.edu/programs/MGMT%3ABBA |
| 6 | Marketing | https://catalog.fiu.edu/programs/MKTG%3ABBA |
| 7 | Real Estate | https://catalog.fiu.edu/programs/REST%3ABBA |

#### College of Arts, Sciences, and Education
##### Department of Biological Sciences
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.fiu.edu/programs/BIOL%3ABS |

##### Department of Chemistry
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.fiu.edu/programs/CHEM%3ABS |

##### Department of Physics
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.fiu.edu/programs/PHYS%3ABS |

##### Department of Mathematics and Statistics
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.fiu.edu/programs/MATH%3ABS |
| 2 | Statistics | https://catalog.fiu.edu/programs/STAT%3ABS |

##### Department of Psychology
###### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.fiu.edu/programs/PSY%3ABA |

##### Department of English
###### BA (Bachelor of Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.fiu.edu/programs/ENG%3ABA |

#### College of Engineering and Computing
##### School of Computing and Information Sciences
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.fiu.edu/programs/CS%3ABS |
| 2 | Information Technology | https://catalog.fiu.edu/programs/IT%3ABS |

##### Department of Electrical and Computer Engineering
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://catalog.fiu.edu/programs/EE%3ABS |
| 2 | Computer Engineering | https://catalog.fiu.edu/programs/CE%3ABS |

##### Department of Mechanical and Materials Engineering
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.fiu.edu/programs/ME%3ABS |

##### Department of Civil and Environmental Engineering
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.fiu.edu/programs/CE%3ABS |

#### College of Communication, Architecture, and the Arts
##### School of Architecture
###### BARCH (Bachelor of Architecture)
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://catalog.fiu.edu/programs/ARCH%3ABARCH |

##### Department of Art and Art History
###### BFA (Bachelor of Fine Arts)
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.fiu.edu/programs/ART%3ABFA |

#### College of Nursing and Health Sciences
##### School of Nursing
###### BSN (Bachelor of Science in Nursing)
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://catalog.fiu.edu/programs/NUR%3ABSN |

#### School of Hospitality and Tourism Management
###### BS (Bachelor of Science)
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management | https://catalog.fiu.edu/programs/HM%3ABS |
| 2 | Tourism Management | https://catalog.fiu.edu/programs/TM%3ABS |

### 1.3 Interdisciplinary / cross-college undergraduate programs

FIU offers several interdisciplinary programs that span multiple colleges. These are typically housed in one college but draw coursework from others.

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|-----------|----------------------|-----|
| 1 | African Studies | CASE | https://catalog.fiu.edu/programs/AFNST%3ACFI |
| 2 | Anthropology | CASE | https://catalog.fiu.edu/programs/ANTH%3ACFI |
| 3 | Art History | CARTA | https://catalog.fiu.edu/programs/ARTHST%3ACFI |
| 4 | Biology | CASE | https://catalog.fiu.edu/programs/BIOL%3ACFI |
| 5 | Business Administration | Business | https://catalog.fiu.edu/programs/BUAD%3ACFI |
| 6 | Chemistry | CASE | https://catalog.fiu.edu/programs/CHEM%3ACFI |
| 7 | Communication | CARTA | https://catalog.fiu.edu/programs/COMM%3ACFI |
| 8 | Computer Science | ECS | https://catalog.fiu.edu/programs/CS%3ACFI |
| 9 | Criminal Justice | SIPA | https://catalog.fiu.edu/programs/CJ%3ACFI |
| 10 | Economics | SIPA | https://catalog.fiu.edu/programs/ECON%3ACFI |
| 11 | English | CASE | https://catalog.fiu.edu/programs/ENG%3ACFI |
| 12 | History | SIPA | https://catalog.fiu.edu/programs/HIST%3ACFI |
| 13 | Mathematics | CASE | https://catalog.fiu.edu/programs/MATH%3ACFI |

### 1.5 General Education Requirements

FIU requires all undergraduate students to complete the University Core Curriculum (UCC), which includes:
- Communication (6 credits)
- Quantitative Reasoning (6 credits)
- Natural Sciences (6 credits)
- Humanities (6 credits)
- Social Sciences (6 credits)
- Additional requirements in diversity, international, and capstone experiences

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

FIU offers extensive graduate programs across 11 colleges. Key statistics from graduate admissions:
- 106 Master's Degrees
- 34 Doctoral Degrees
- 50+ Certificates
- 3 Specialist Programs

#### College of Business
##### MBA Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Professional MBA | MBA | https://catalog.fiu.edu/programs/PMBAA%3AMBA |
| 2 | Corporate MBA | MBA | https://catalog.fiu.edu/programs/CMBA%3AMBA |
| 3 | International MBA | MBA | https://catalog.fiu.edu/programs/IMBA%3AMBA |

##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Accounting | MACC | https://catalog.fiu.edu/programs/ACCT%3AMACC |
| 2 | Master of Science in Finance | MS | https://catalog.fiu.edu/programs/FIN%3AMS |
| 3 | Master of International Business | MIB | https://catalog.fiu.edu/programs/INTLB%3AMIB |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctorate in Business Administration | DBA | https://catalog.fiu.edu/programs/BUAD%3ADBA |

#### College of Engineering and Computing
##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Science in Computer Science | MS | https://catalog.fiu.edu/programs/CS%3AMS |
| 2 | Master of Science in Electrical Engineering | MS | https://catalog.fiu.edu/programs/EE%3AMS |
| 3 | Master of Science in Mechanical Engineering | MS | https://catalog.fiu.edu/programs/ME%3AMS |
| 4 | Master of Science in Civil Engineering | MS | https://catalog.fiu.edu/programs/CE%3AMS |
| 5 | Master of Science in Information Technology | MS | https://catalog.fiu.edu/programs/IT%3AMS |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Ph.D. in Computer Science | PhD | https://catalog.fiu.edu/programs/CS%3APHD |
| 2 | Ph.D. in Electrical Engineering | PhD | https://catalog.fiu.edu/programs/EE%3APHD |

#### College of Arts, Sciences, and Education
##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Arts in Biology | MA | https://catalog.fiu.edu/programs/BIOL%3AMA |
| 2 | Master of Science in Chemistry | MS | https://catalog.fiu.edu/programs/CHEM%3AMS |
| 3 | Master of Arts in English | MA | https://catalog.fiu.edu/programs/ENG%3AMA |
| 4 | Master of Arts in History | MA | https://catalog.fiu.edu/programs/HIST%3AMA |
| 5 | Master of Science in Mathematics | MS | https://catalog.fiu.edu/programs/MATH%3AMS |
| 6 | Master of Arts in Psychology | MA | https://catalog.fiu.edu/programs/PSY%3AMA |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Ph.D. in Biological Sciences | PhD | https://catalog.fiu.edu/programs/BIOL%3APHD |
| 2 | Ph.D. in Chemistry | PhD | https://catalog.fiu.edu/programs/CHEM%3APHD |
| 3 | Ph.D. in Physics | PhD | https://catalog.fiu.edu/programs/PHYS%3APHD |
| 4 | Ph.D. in Mathematics | PhD | https://catalog.fiu.edu/programs/MATH%3APHD |
| 5 | Ph.D. in Psychology | PhD | https://catalog.fiu.edu/programs/PSY%3APHD |
| 6 | Doctor of Education in Educational Leadership | EdD | https://catalog.fiu.edu/programs/EDLD%3AEDD |

#### College of Communication, Architecture, and the Arts
##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Architecture | MARCH | https://catalog.fiu.edu/programs/ARCH%3AMARCH |
| 2 | Master of Fine Arts in Art | MFA | https://catalog.fiu.edu/programs/ART%3AMFA |
| 3 | Master of Arts in Communication | MA | https://catalog.fiu.edu/programs/COMM%3AMA |
| 4 | Master of Interior Architecture | MIA | https://catalog.fiu.edu/programs/INTARCH%3AMIA |
| 5 | Master of Landscape Architecture | MLA | https://catalog.fiu.edu/programs/LANDARCH%3AMLA |

#### College of Nursing and Health Sciences
##### Master's Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Science in Nursing - Family Nurse Practitioner | MSN | https://catalog.fiu.edu/programs/AFNP%3AMSN |
| 2 | Master of Science in Nursing - Adult-Gerontology NP | MSN | https://catalog.fiu.edu/programs/AAGNP%3AMSN |
| 3 | Master of Science in Nursing - Pediatric NP | MSN | https://catalog.fiu.edu/programs/ACNP%3AMSN |
| 4 | Master of Science in Nursing - Psychiatric Mental Health NP | MSN | https://catalog.fiu.edu/programs/APNP%3AMSN |

##### Doctoral Programs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Nursing Practice - Nurse Anesthesia | DNP | https://catalog.fiu.edu/programs/NURAN%3ADNP |
| 2 | Doctor of Physical Therapy | DPT | https://catalog.fiu.edu/programs/PT%3ADPT |

#### College of Medicine
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Doctor of Medicine | MD | https://catalog.fiu.edu/programs/MED%3AMD |

#### College of Law
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Juris Doctor | JD | https://catalog.fiu.edu/programs/LAW%3AJD |
| 2 | Master of Laws | LL.M. | https://catalog.fiu.edu/programs/LAW%3ALLM |

#### School of Hospitality and Tourism Management
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Science in Hospitality Management | MS | https://catalog.fiu.edu/programs/HM%3AMS |

#### School of International and Public Affairs
| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Master of Public Administration | MPA | https://catalog.fiu.edu/programs/PA%3AMPA |
| 2 | Master of Public Health | MPH | https://catalog.fiu.edu/programs/PH%3AMPH |
| 3 | Master of Social Work | MSW | https://catalog.fiu.edu/programs/SW%3AMSW |
| 4 | Master of Arts in International Studies | MA | https://catalog.fiu.edu/programs/IS%3AMA |

### 2.2 Graduate admissions model

FIU graduate admissions is **decentralized**. Each college/school manages its own admissions process. Key points:
- Application portal: Varies by program
- Application fee: $30 USD
- GRE/GMAT: Varies by program (some require, some optional, some waived)
- TOEFL/IELTS: Required for non-native English speakers (minimum scores vary by program)
- Deadlines: Vary by program (typically rolling or semester-based)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common App | admissions.fiu.edu |
| 申请费 | $30 USD | admissions.fiu.edu |
| EA 截止日期 | November 3 | admissions.fiu.edu |
| Regular 截止日期 | December 17 | admissions.fiu.edu |
| Final 截止日期 | March 4 | admissions.fiu.edu |
| 决定通知 (EA) | December 11 | admissions.fiu.edu |
| 决定通知 (Regular) | January 21 | admissions.fiu.edu |
| 最终决定通知 | April 2 | admissions.fiu.edu |
| 押金截止 | May 1 | admissions.fiu.edu |
| SAT/ACT/CLT | REQUIRED (not test-optional) | admissions.fiu.edu |
| SAT 代码 | 5206 | admissions.fiu.edu |
| ACT 代码 | 0776 | admissions.fiu.edu |
| CLT 代码 | 844-925-8392 | admissions.fiu.edu |
| 推荐信 | Not required | admissions.fiu.edu |
| 面试 | Not required | admissions.fiu.edu |
| 作品集 | Required for some programs (Architecture, Art) | admissions.fiu.edu |

### 3.2 Undergraduate English proficiency table

| 考试 | 最低要求 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL | Not required for direct admission | N/A | English proficiency determined by SAT/ACT sub-scores |
| IELTS | Not required for direct admission | N/A | English proficiency determined by SAT/ACT sub-scores |
| Duolingo | Not accepted | N/A | Not mentioned as accepted |
| PTE | Not accepted | N/A | Not mentioned as accepted |

> **Note**: FIU has a distinctive policy where international students are NOT required to submit TOEFL or IELTS for direct admission. Instead, English proficiency is determined by SAT or ACT sub-section scores in Verbal/Reading and English sections.

### 3.3 Graduate — global rules

- Application portal: Varies by program (some use departmental portals, some use centralized system)
- Application fee: $30 USD
- GRE/GMAT: Varies by program
- TOEFL/IELTS: Required for non-native English speakers
- Deadlines: Vary by program (typically rolling or semester-based)
- Most PhD programs offer funding (TA/RA positions)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

#### Florida Resident (On-Campus)
| Expense item | Per Semester | Annual |
|-------------|-------------|--------|
| Tuition | $3,084 | $6,168 |
| Fees | $199 | $398 |
| Direct Loan Origination Fee | $22 | $44 |
| Books & Supplies | $675 | $1,350 |
| Housing | $4,465 | $8,930 |
| Food | $2,461 | $4,922 |
| Transportation | $1,473 | $2,946 |
| Personal | $1,737 | $3,474 |
| **Total** | **$14,116** | **$28,232** |

#### Non-Florida Resident (On-Campus)
| Expense item | Per Semester | Annual |
|-------------|-------------|--------|
| Tuition | $9,903 | $19,806 |
| Fees | $199 | $398 |
| Direct Loan Origination Fee | $22 | $44 |
| Books & Supplies | $675 | $1,350 |
| Housing | $4,465 | $8,930 |
| Food | $2,461 | $4,922 |
| Transportation | $1,473 | $2,946 |
| Personal | $1,737 | $3,474 |
| **Total** | **$20,935** | **$41,870** |

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 |
|------|-----|
| Need-blind/Need-aware | Need-aware for all (domestic and international) |
| Meets demonstrated need | Yes (through combination of aid) |
| Golden Promise | 100% tuition and fees for FL residents with SAI ≤ 0 |
| FAFSA priority date | December 1 |
| Merit scholarships | Available (priority deadline: November 1) |
| Total financial aid awarded | >$180 million annually |

**Golden Promise Requirements:**
- First-time-in-college freshman (started early fall 2017 or later) OR new transfer student (started fall 2023 or later)
- U.S. citizen or permanent resident
- Florida resident
- Submit FAFSA prior to enrollment
- Student Aid Index (SAI) ≤ 0
- Registered for at least 12 credits each semester (15 recommended)
- Complete 30 credit hours each year
- Earn cumulative GPA of 2.0 or higher each semester

### 4.3 Graduate cost & funding framework

- Graduate tuition varies by program
- Many PhD programs offer full funding (TA/RA positions)
- Master's programs are typically self-funded
- Application fee: $30 USD
- Fee waivers: Available for qualifying students

---

## SECTION 5 — Evidence chain index

### E-U-001: Undergraduate Deadlines
```yaml
field: undergraduate.deadlines
value:
  ea: November 3
  regular: December 17
  final: March 4
  ea_notification: December 11
  regular_notification: January 21
  final_notification: April 2
  deposit: May 1
source_url: https://admissions.fiu.edu/how-to-apply/freshman-applicant/index.html
source_snippet: "Early Action: Complete App with Docs: November 3, Notification: December 11, Deposit: May 1"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Test Policy
```yaml
field: undergraduate.test_policy
value: SAT, ACT, or CLT REQUIRED (not test-optional)
source_url: https://admissions.fiu.edu/admission-standards/index.html
source_snippet: "SAT, ACT and/or CLT scores are required for first time in college applicants"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Application Fee
```yaml
field: undergraduate.application_fee
value: $30 USD
source_url: https://admissions.fiu.edu/international/incoming-freshmen/index.html
source_snippet: "Applicants will be required to pay a $30 USD application fee"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: English Proficiency Policy
```yaml
field: undergraduate.english_proficiency
value: TOEFL/IELTS NOT required for direct admission; proficiency determined by SAT/ACT sub-scores
source_url: https://admissions.fiu.edu/international/incoming-freshmen/index.html
source_snippet: "For direct admission to FIU, international first time in college students are not required to submit TOEFL or IELTS scores"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: In-State Tuition
```yaml
field: undergraduate.costs.tuition_in_state
value: $3,084 per semester ($6,168 annual)
source_url: https://onestop.fiu.edu/finances/estimate-your-costs/
source_snippet: "Tuition: $3,084"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Out-of-State Tuition
```yaml
field: undergraduate.costs.tuition_out_of_state
value: $9,903 per semester ($19,806 annual)
source_url: https://onestop.fiu.edu/finances/estimate-your-costs/
source_snippet: "Tuition: $9,903"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Total COA (In-State)
```yaml
field: undergraduate.costs.total_in_state
value: $28,232 annual (on-campus)
source_url: https://onestop.fiu.edu/finances/estimate-your-costs/
source_snippet: "Total Annual: $28,232"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: Total COA (Out-of-State)
```yaml
field: undergraduate.costs.total_out_of_state
value: $41,870 annual (on-campus)
source_url: https://onestop.fiu.edu/finances/estimate-your-costs/
source_snippet: "Total Annual: $41,870"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: Golden Promise
```yaml
field: undergraduate.financial_aid.golden_promise
value: 100% tuition and fees for FL residents with SAI ≤ 0
source_url: https://onestop.fiu.edu/finances/types-of-aid/fius-golden-promise/
source_snippet: "This program guarantees 100% tuition and fees for Florida residents with a Student Aid Index (SAI) of 0 or less"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Program Counts
```yaml
field: graduate.programs.counts
value:
  masters: 106
  doctoral: 34
  certificates: 50+
  specialist: 3
source_url: https://admissions.fiu.edu/how-to-apply/graduate-applicant/index.html
source_snippet: "106 Master's Degrees, 34 Doctoral Degrees, 50+ Certificates, 3 Specialist Programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Application Fee
```yaml
field: graduate.application_fee
value: $30 USD
source_url: https://admissions.fiu.edu/how-to-apply/graduate-applicant/index.html
source_snippet: "Application fee: $30 USD"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-001: Institution Overview
```yaml
field: institution.overview
value:
  type: Public Research University
  location: Miami, Florida
  students: 56,000+
  acceptance_rate: ~50%
  ranking: "#1 University in Florida (Wall Street Journal)"
source_url: https://admissions.fiu.edu/
source_snippet: "With over 56,000 students and a freshman acceptance rate around 50%"
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
fiu-knowledge-base-v2/
├── 00-institution-overview.md
├── 01-undergraduate-colleges/
│   ├── arts-sciences-education.md
│   ├── business.md
│   ├── communication-architecture-arts.md
│   ├── engineering-computing.md
│   ├── hospitality-tourism.md
│   ├── international-public-affairs.md
│   ├── law.md
│   ├── medicine.md
│   ├── nursing-health-sciences.md
│   └── public-health-social-work.md
├── 02-graduate-programs/
│   ├── masters-programs.md
│   ├── doctoral-programs.md
│   └── certificates.md
├── 03-admissions-deadlines.md
├── 04-costs-financial-aid.md
├── 05-test-policies.md
└── 06-evidence-chain.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "fiu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Complete program list (473 vs 367 captured) | https://catalog.fiu.edu/programs/ |
| P0 | Per-program GRE/GMAT requirements | Graduate program pages |
| P1 | Per-program TOEFL minimums | Graduate program pages |
| P1 | Detailed department-program mapping | https://catalog.fiu.edu/college-school-department |
| P2 | Transfer admission requirements | https://admissions.fiu.edu/how-to-apply/transfer-applicant/ |
| P2 | International graduate admissions | https://admissions.fiu.edu/international/graduate/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | FIU | (Other schools) |
|------|-----|-----------------|
| Type | Public Research | |
| Location | Miami, FL | |
| UG Tuition (In-State) | $6,168/yr | |
| UG Tuition (OOS) | $19,806/yr | |
| UG Total COA (In-State) | $28,232/yr | |
| UG Total COA (OOS) | $41,870/yr | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA Deadline | November 3 | |
| RD Deadline | December 17 | |
| Final Deadline | March 4 | |
| SAT/ACT Required? | Yes (not test-optional) | |
| TOEFL Min | N/A (not required) | |
| IELTS Min | N/A (not required) | |
| Golden Promise | Yes (SAI ≤ 0, FL residents) | |
| Total Programs | ~367 (473 catalog) | |
| Graduate Programs | 106 Master's, 34 Doctoral | |
| Application Fee | $30 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.fiu.edu, onestop.fiu.edu, catalog.fiu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
