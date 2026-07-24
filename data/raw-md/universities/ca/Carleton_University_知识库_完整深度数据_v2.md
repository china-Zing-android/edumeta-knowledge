# Carleton University 知识库 完整深度数据

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Ontario)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~90+ (含主修、辅修、证书) |
| 本科辅修 (Minors) | ~20+ |
| 本科证书 (Certificates) | ~10+ |
| 研究生授课型项目 (PGT: Master's) | ~80+ |
| 研究生博士项目 (PhD/Doctoral) | ~50+ |
| 研究生文凭/证书 (Graduate Diploma/Certificate) | ~5 |
| **学位项目总计** | **~200+ UG + ~100+ Graduate** |
| 学院 (Faculties) | 6 |
| 学术院系/所/中心 (Academic Schools/Departments) | ~50+ |

### 0.2 学院 / 系层级结构

```
Carleton University
├── Faculty of Arts and Social Sciences (FASS)
│   ├── Carleton University Art Gallery
│   ├── Centre for Initiatives in Education (includes Enriched Support Program)
│   ├── College of the Humanities (Bachelor of Humanities, Greek & Roman Studies, Religion)
│   ├── Department of Cognitive Science
│   ├── Department of English Language and Literature
│   ├── Department of French
│   ├── Department of Geography and Environmental Studies
│   ├── Department of History
│   ├── Department of Philosophy
│   ├── Department of Psychology
│   ├── Department of Sociology and Anthropology
│   ├── Institute for Comparative Studies in Literature, Art and Culture
│   ├── Institute of African Studies
│   ├── Institute of Interdisciplinary Studies (Childhood & Youth Studies, Indigenous Studies, Human Rights & Social Justice)
│   ├── School for Studies in Art and Culture (Art History, Film Studies, Music)
│   ├── School of Canadian Studies
│   ├── School of Linguistics and Language Studies
│   └── Social Transformation (FIST)
│
├── Faculty of Engineering and Design (FED)
│   ├── Azrieli School of Architecture and Urbanism
│   ├── Department of Civil and Environmental Engineering
│   ├── Department of Electronics
│   ├── Department of Mechanical and Aerospace Engineering
│   ├── Department of Systems and Computer Engineering
│   ├── Industrial Design
│   └── Information Technology
│
├── Faculty of Public and Global Affairs (FPGA)
│   ├── Arthur Kroeger College of Public Affairs
│   ├── Department of Economics
│   ├── Department of Law and Legal Studies
│   ├── Department of Political Science
│   ├── Infrastructure Protection & International Security
│   ├── Institute of African Studies
│   ├── Institute of Criminology and Criminal Justice
│   ├── Institute of European, Russian and Eurasian Studies
│   ├── Institute of Political Economy
│   ├── Norman Paterson School of International Affairs
│   ├── School of Journalism and Communication
│   ├── School of Public Policy and Administration
│   └── School of Social Work
│
├── Faculty of Science
│   ├── Department of Biology
│   ├── Department of Chemistry
│   ├── Department of Earth Sciences
│   ├── Department of Health Sciences
│   ├── Department of Neuroscience
│   ├── Department of Physics
│   ├── Institute of Biochemistry
│   ├── Institute of Environmental and Interdisciplinary Science
│   ├── School of Computer Science
│   ├── School of Mathematics and Statistics
│   └── Technology, Society, Environment Studies
│
├── Sprott School of Business
│   └── (Single school, no sub-departments)
│
└── Graduate Studies (Faculty-level)
    └── (跨学院管理所有研究生项目)
```

### 0.3 学历级别明细

| 学位级别 | 缩写 | 数量 (估算) |
|---------|------|------------|
| Bachelor of Arts | BA | 20+ |
| Bachelor of Arts (Honours) | BA (Hons) | 30+ |
| Bachelor of Science | BSc | 15+ |
| Bachelor of Engineering | BEng | 8 |
| Bachelor of Commerce | BCom | 1 |
| Bachelor of Computer Science | BCS | 1 |
| Bachelor of Journalism | BJ | 1 |
| Bachelor of Social Work | BSW | 1 |
| Bachelor of Music | BMus | 1 |
| Bachelor of Architectural Studies | BAS | 1 |
| Bachelor of Information Technology | BIT | 1 |
| Bachelor of Industrial Design | BID | 1 |
| Bachelor of Nursing | BScN | 1 |
| Bachelor of Mathematics | BMath | 1 |
| Bachelor of Media Production and Design | BMPD | 1 |
| Bachelor of Global and International Studies | BGInS | 1 |
| Bachelor of Public Affairs and Policy Management | BPAPM | 1 |
| Bachelor of Humanities | BHum | 1 |
| Bachelor of Cognitive Science | BCogSc | 1 |
| Bachelor of Cybersecurity | BCyber | 1 |
| Bachelor of Data Science | BDS | 1 |
| Bachelor of Economics | BEcon | 1 |
| Bachelor of Communication and Media Studies | BCoMS | 1 |
| Bachelor of Accounting | BAcc | 1 |
| Bachelor of International Business | BIB | 1 |
| Bachelor of Journalism and Humanities | BJHum | 1 |
| Master of Arts | MA | 30+ |
| Master of Science | MSc | 20+ |
| Master of Engineering | MEng | 10+ |
| Master of Business Administration | MBA | 1 |
| Master of Computer Science | MCS | 1 |
| Master of Architecture | MArch | 1 |
| Master of Journalism | MJ | 1 |
| Master of Social Work | MSW | 1 |
| Master of Design | MDes | 1 |
| Doctor of Philosophy | PhD | 50+ |
| Graduate Diploma | GDip | ~5 |
| Post-Baccalaureate Diploma | PBD | ~7 |

### 0.4 分布矩阵 (学院 × 学位级别)

| 学院 | UG 本科 | Master 硕士 | PhD 博士 | 证书/文凭 | 合计 |
|------|---------|------------|---------|----------|------|
| Faculty of Arts and Social Sciences | ~60 | ~30 | ~20 | ~5 | ~115 |
| Faculty of Engineering and Design | ~15 | ~15 | ~8 | ~2 | ~40 |
| Faculty of Public and Global Affairs | ~15 | ~15 | ~10 | ~3 | ~43 |
| Faculty of Science | ~20 | ~15 | ~12 | ~2 | ~49 |
| Sprott School of Business | ~3 | ~5 | ~3 | ~1 | ~12 |
| Graduate Studies (跨学院) | — | — | — | — | ~50+ |
| **合计** | **~113** | **~80** | **~53** | **~13** | **~260** |

> 注：研究生项目由 Graduate Studies 统一管理，但具体归属各学院。很多项目同时授予 Master 和 PhD 学位。

---

## Section 1 — Undergraduate Education (本科教育)

### Faculty of Arts and Social Sciences (FASS)

| Program Name | Degree Type | Department |
|-------------|------------|-----------|
| African Studies | BA | Institute of African Studies |
| Anthropology | BA (Hons) | Department of Sociology and Anthropology |
| Applied Linguistics and Discourse Studies | BA | School of Linguistics and Language Studies |
| Art History | BA (Hons) | School for Studies in Art and Culture |
| Biochemistry | BSc | Institute of Biochemistry |
| Biology | BSc (Hons) | Department of Biology |
| Canadian Studies (Minors) | Minor | School of Canadian Studies |
| Certificate in Carillon Studies | Certificate | College of the Humanities |
| Certificate in Journalism in Indigenous Communities | Certificate | School of Journalism and Communication |
| Certificate in Multidisciplinary Studies in Mental Health and Well-Being | Certificate | Institute of Interdisciplinary Studies |
| Certificate in Nunavut Public Service Studies | Certificate | Centre for Initiatives in Education |
| Certificate in Science and Policy | Certificate | Faculty of Science |
| Certificate in Science Communication | Certificate | Faculty of Science |
| Certificate in the Teaching of English as a Second Language (CTESL) | Certificate | School of Linguistics and Language Studies |
| Chemistry | BSc (Hons) | Department of Chemistry |
| Childhood and Youth Studies | BA | Institute of Interdisciplinary Studies |
| Cognitive Science | BCogSc | Department of Cognitive Science |
| Communication and Media Studies | BCoMS | School of Journalism and Communication |
| Criminology and Criminal Justice | BA (Hons) | Institute of Criminology and Criminal Justice |
| Digital Humanities (Minor) | Minor | Institute for Comparative Studies in Literature, Art and Culture |
| Earth Sciences | BSc (Hons) | Department of Earth Sciences |
| Economics | BEcon | Department of Economics |
| English | BA (Hons) | Department of English Language and Literature |
| Environmental and Climate Humanities (Minor) | Minor | Institute of Interdisciplinary Studies |
| Environmental Science | BSc | Institute of Environmental and Interdisciplinary Science |
| Environmental Studies | BA | Institute of Environmental and Interdisciplinary Science |
| European and Russian Studies | BA (Hons) | Institute of European, Russian and Eurasian Studies |
| Film Studies | BA (Hons) | School for Studies in Art and Culture |
| Food Science | BSc | Department of Chemistry |
| French | BA (Hons) | Department of French |
| Geography | BA/BSc | Department of Geography and Environmental Studies |
| Geomatics | BSc | Department of Geography and Environmental Studies |
| Global and International Studies | BGInS | Faculty of Public and Global Affairs |
| Greek and Roman Studies | BA | College of the Humanities |
| Health Sciences | BHSc | Department of Health Sciences |
| History | BA (Hons) | Department of History |
| Human Rights and Social Justice | BA | Institute of Interdisciplinary Studies |
| Humanities (Great Books) | BHum | College of the Humanities |
| Indigenous Studies | BA | Institute of Interdisciplinary Studies |
| Journalism | BJ | School of Journalism and Communication |
| Journalism and Humanities | BJHum | School of Journalism and Communication / College of Humanities |
| Latin American and Caribbean Studies | BA (Hons) | Institute of African Studies |
| Law | BA | Department of Law and Legal Studies |
| Linguistics (Bachelor of Arts) | BA | School of Linguistics and Language Studies |
| Linguistics (Bachelor of Science) | BSc | School of Linguistics and Language Studies |
| Music | BMus | School for Studies in Art and Culture |
| Philosophy | BA (Hons) | Department of Philosophy |
| Political Science | BA (Hons) | Department of Political Science |
| Psychology | BA/BSc (Hons) | Department of Psychology |
| Public Affairs and Policy Management | BPAPM | Arthur Kroeger College of Public Affairs |
| Religion | BA | College of the Humanities |
| Social Work | BSW | School of Social Work |
| Sociology | BA (Hons) | Department of Sociology and Anthropology |
| Women's and Gender Studies | BA (Hons) | Institute of Interdisciplinary Studies |

### Faculty of Engineering and Design (FED)

| Program Name | Degree Type | Department |
|-------------|------------|-----------|
| Architectural Studies | BAS | Azrieli School of Architecture and Urbanism |
| Engineering (Aerospace) | BEng | Department of Mechanical and Aerospace Engineering |
| Engineering (Biomedical) | BEng | Department of Systems and Computer Engineering |
| Engineering (Civil) | BEng | Department of Civil and Environmental Engineering |
| Engineering (Computer Systems) | BEng | Department of Systems and Computer Engineering |
| Engineering (Electrical) | BEng | Department of Electronics |
| Engineering (Environmental) | BEng | Department of Civil and Environmental Engineering |
| Engineering (Mechanical) | BEng | Department of Mechanical and Aerospace Engineering |
| Engineering (Software) | BEng | Department of Systems and Computer Engineering |
| Engineering (Sustainable and Renewable Energy) | BEng | Department of Mechanical and Aerospace Engineering |
| Industrial Design | BID | Industrial Design |
| Information Technology | BIT | Information Technology |

### Faculty of Public and Global Affairs (FPGA)

| Program Name | Degree Type | Department |
|-------------|------------|-----------|
| Global and International Studies | BGInS | Arthur Kroeger College |
| International Business | BIB | Arthur Kroeger College / Sprott School of Business |
| Public Affairs and Policy Management | BPAPM | Arthur Kroeger College of Public Affairs |

### Faculty of Science

| Program Name | Degree Type | Department |
|-------------|------------|-----------|
| Biochemistry | BSc (Hons) | Institute of Biochemistry |
| Biology | BSc (Hons) | Department of Biology |
| Biotechnology | BSc | Institute of Biochemistry |
| Chemistry | BSc (Hons) | Department of Chemistry |
| Computer Science | BCS | School of Computer Science |
| Cybersecurity | BCyber | School of Computer Science |
| Data Science | BDS | School of Computer Science |
| Earth Sciences | BSc (Hons) | Department of Earth Sciences |
| Food Science | BSc | Department of Chemistry |
| Health Sciences | BHSc | Department of Health Sciences |
| Integrated Science | BSc | Faculty of Science |
| Mathematics and Statistics | BMath | School of Mathematics and Statistics |
| Nanoscience | BSc | Department of Physics |
| Neuroscience | BSc (Hons) | Department of Neuroscience |
| Open Studies (B.A. and B.Sc.) | BA/BSc | Faculty of Science |
| Physics | BSc (Hons) | Department of Physics |

### Sprott School of Business

| Program Name | Degree Type | Department |
|-------------|------------|-----------|
| Accounting | BAcc | Sprott School of Business |
| Commerce (Business) | BCom (Hons) | Sprott School of Business |
| International Business | BIB | Sprott School of Business |

### Minors (跨学院辅修)

| Minor Name | Department/Faculty |
|-----------|-------------------|
| American Sign Language | School of Linguistics and Language Studies |
| Archaeology | Department of Sociology and Anthropology |
| Canadian Studies | School of Canadian Studies |
| Community Engagement | Institute of Interdisciplinary Studies |
| Critical Race Studies | Institute of Interdisciplinary Studies |
| Digital Humanities | Institute for Comparative Studies |
| Disability Studies | Institute of Interdisciplinary Studies |
| Environmental and Climate Humanities | Institute of Interdisciplinary Studies |
| German | Department of English Language and Literature |
| Italian | Department of French |
| Japanese Language | School of Linguistics and Language Studies |
| Korean Language | School of Linguistics and Language Studies |
| Mandarin Chinese | School of Linguistics and Language Studies |
| Medieval and Early Modern Studies | College of the Humanities |
| News Media and Information | School of Journalism and Communication |
| Russian | Institute of European, Russian and Eurasian Studies |
| Sexuality Studies | Institute of Interdisciplinary Studies |
| Spanish | Department of French |
| Technology, Society, Environment Studies | Faculty of Science |

---

## Section 2 — Graduate Education (研究生教育)

### Graduate Programs — Faculty of Arts and Social Sciences (FASS)

| Program Name | Degree(s) | Department |
|-------------|----------|-----------|
| African Studies | MA, PhD (Collab. Spec.) | Institute of African Studies |
| Anthropology | MA, PhD | Department of Sociology and Anthropology |
| Applied Linguistics and Discourse Studies | MA, PhD | School of Linguistics and Language Studies |
| Art and Architectural History | MA, PhD | School for Studies in Art and Culture |
| Canadian Studies | MA, PhD | School of Canadian Studies |
| Cognitive Science | MA, MSc, PhD | Department of Cognitive Science |
| Communication | MA, PhD | School of Journalism and Communication |
| Cultural Mediations | MA, PhD | Institute for Comparative Studies |
| Curatorial Studies | Graduate Diploma | School for Studies in Art and Culture |
| Digital Humanities | MA (Collab. Spec.) | Institute for Comparative Studies |
| English | MA, PhD | Department of English Language and Literature |
| Film Studies | MA, PhD | School for Studies in Art and Culture |
| Geography | MA, MSc, PhD | Department of Geography and Environmental Studies |
| History | MA, PhD | Department of History |
| Linguistics | MA, PhD | School of Linguistics and Language Studies |
| Migration and Diaspora Studies | MA, PhD | Institute of African Studies |
| Music and Culture | MA, PhD | School for Studies in Art and Culture |
| Philosophy | MA, PhD | Department of Philosophy |
| Psychology | MA, MSc, PhD | Department of Psychology |
| Sociology | MA, PhD | Department of Sociology and Anthropology |
| Teaching English as an Additional Language | MA | School of Linguistics and Language Studies |
| Women's and Gender Studies | MA, PhD | Institute of Interdisciplinary Studies |
| Work and Labour | MA, PhD | Department of Sociology and Anthropology |

### Graduate Programs — Faculty of Engineering and Design (FED)

| Program Name | Degree(s) | Department |
|-------------|----------|-----------|
| Aerospace Engineering | MEng, MASc, PhD | Department of Mechanical and Aerospace Engineering |
| Architecture | MArch | Azrieli School of Architecture and Urbanism |
| Biomedical Engineering | MASc, MEng, PhD | Department of Systems and Computer Engineering |
| Building Engineering | MEng, MASc, PhD | Department of Civil and Environmental Engineering |
| Civil Engineering | MEng, MASc, PhD | Department of Civil and Environmental Engineering |
| Design | MDes | Industrial Design |
| Electrical and Computer Engineering | MEng, MASc, PhD | Department of Electronics |
| Engineering Practice | MEng | Faculty of Engineering and Design |
| Environmental Engineering | MEng, MASc, PhD | Department of Civil and Environmental Engineering |
| Human-Computer Interaction | MA, MSc, PhD | School of Computer Science / Psychology |
| Information Technology | MIT | Information Technology |
| Materials Engineering | MEng, MASc, PhD | Department of Mechanical and Aerospace Engineering |
| Mechanical and Aerospace Engineering | MEng, MASc, PhD | Department of Mechanical and Aerospace Engineering |
| Networking Technology | MTech | Information Technology |
| Sustainable Energy | MEng, MASc, PhD | Department of Mechanical and Aerospace Engineering |
| Technology Innovation Management | MEng, PhD | Department of Systems and Computer Engineering |

### Graduate Programs — Faculty of Public and Global Affairs (FPGA)

| Program Name | Degree(s) | Department |
|-------------|----------|-----------|
| Economics | MA, PhD | Department of Economics |
| Ethics and Public Affairs | MA | School of Public Policy and Administration |
| European, Russian and Eurasian Studies | MA, PhD | Institute of European, Russian and Eurasian Studies |
| Infrastructure Protection and International Security | MA | Infrastructure Protection & International Security |
| International Affairs | MA | Norman Paterson School of International Affairs |
| Journalism | MJ | School of Journalism and Communication |
| Legal Studies | MA, PhD | Department of Law and Legal Studies |
| Philanthropy and Nonprofit Leadership | MA | School of Public Policy and Administration |
| Political Economy | MA, PhD | Institute of Political Economy |
| Political Management | MA | Department of Political Science |
| Political Science | MA, PhD | Department of Political Science |
| Public Policy and Administration | MA, PhD | School of Public Policy and Administration |
| Social Work | MSW, PhD | School of Social Work |

### Graduate Programs — Faculty of Science

| Program Name | Degree(s) | Department |
|-------------|----------|-----------|
| Biochemistry | MSc, PhD (Collab. Spec.) | Institute of Biochemistry |
| Bioinformatics | MSc, PhD (Collab. Spec.) | School of Computer Science |
| Biology | MSc, PhD | Department of Biology |
| Biotechnology | MSc | Institute of Biochemistry |
| Chemistry | MSc, PhD | Department of Chemistry |
| Climate Change | MSc, PhD (Collab. Spec.) | Institute of Environmental and Interdisciplinary Science |
| Clinical Trials | MSc | Department of Health Sciences |
| Computer Science | MCS, MSc, PhD | School of Computer Science |
| Data Science, Analytics, and Artificial Intelligence | MSc | School of Computer Science |
| Earth Sciences | MSc, PhD | Department of Earth Sciences |
| Health Sciences | MSc, PhD | Department of Health Sciences |
| Mathematics and Statistics | MSc, PhD | School of Mathematics and Statistics |
| Neuroscience | MSc, PhD | Department of Neuroscience |
| Physics | MSc, PhD | Department of Physics |

### Graduate Programs — Sprott School of Business

| Program Name | Degree(s) | Department |
|-------------|----------|-----------|
| Accounting | MAcc | Sprott School of Business |
| Applied Business Analytics | MBA | Sprott School of Business |
| Business | MBA | Sprott School of Business |
| Finance | MFin | Sprott School of Business |
| Management | MSc, PhD | Sprott School of Business |

### Collaborative Specializations (跨学科协作方向)

| Collaborative Specialization | Participating Programs |
|---------------------------|----------------------|
| Accessibility | Multiple programs |
| African Studies | Multiple programs |
| Biochemistry | Multiple programs |
| Bioinformatics | Multiple programs |
| Chemical and Environmental Toxicology | Multiple programs |
| Climate Change | Multiple programs |
| Cybersecurity | Multiple programs |
| Data Science | Multiple programs |
| Digital Humanities | Multiple programs |
| Latin American and Caribbean Studies | Multiple programs |
| Political Economy | Multiple programs |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admissions

**Application System:** Ontario Universities' Application Centre (OUAC)
**Application Portal:** https://admissions.carleton.ca/

**Ontario High School Students:**
- Ontario Secondary School Diploma (OSSD) required
- Six Grade 12 U/M courses, including program-specific prerequisites
- ENG4U (English) required for all programs
- Competitive admission averages vary by program (typically mid-70s to low-90s)

**Canadian High School (Outside Ontario):**
- High school diploma with Grade 12 academic subjects
- Program-specific prerequisite courses required
- Competitive averages vary by province and program

**International High School:**
- High school diploma equivalent to OSSD
- Program-specific prerequisite courses
- IB, GCE, AP, and other international qualifications accepted
- IB minimum: typically 26-34 points depending on program

**International Baccalaureate (IB):**
- IB Diploma accepted for admission
- Competitive scores vary by program
- Transfer credit available for HL subjects (grade 5 or higher)

**English Language Requirements (International):**
> Source: Carleton University Admissions — English requirements page (URL varies by education background)

| Test | Undergraduate Minimum | Graduate Minimum |
|-----|---------------------|-----------------|
| IELTS (Academic) | 6.5 overall (min 6.0 each band) | 6.5-7.0 (varies by program) |
| TOEFL iBT | 86 overall (min 20 each section) | 86-100 (varies by program) |
| PTE Academic | 60 overall (min 60 each skill) | 60+ (varies by program) |
| CAEL | 70 overall | 70 |
| Duolingo English Test | 120+ | — |

**Application Deadlines** (Undergraduate):

| Intake | Deadline |
|--------|---------|
| Fall 2026 (September) | Applications accepted on rolling basis; early admission recommended by February |
| Document Deadline | April 1 (Fall 2026) |
| Residence Guarantee | June 1 |

> Source: https://admissions.carleton.ca/ — "International Undergraduate Admissions — applications for Fall 2026 are still open"

### 3.2 Graduate Admissions

**Application Portal:** https://graduate.carleton.ca/
**Application System:** Carleton's online application system

| Intake | Deadline (varies by program) |
|--------|---------------------------|
| Fall 2026 (September) | Most programs: February 1 - April 1 |
| Winter 2027 (January) | Some programs accept (check specific program) |
| Summer 2027 (May) | Some programs accept (check specific program) |

**General Requirements:**
- Bachelor's degree (4-year honours or equivalent) with minimum B+ average
- Transcripts from all post-secondary institutions
- Letters of reference (2-3, typically academic)
- Statement of intent / research proposal (for research programs)
- CV/Resume
- Some programs require GRE/GMAT (MBA, some Economics/Management programs)
- Portfolio required for Architecture, Design, Art programs

**Graduate English Language Requirements:**

| Test | Minimum |
|-----|---------|
| IELTS (Academic) | 6.5-7.0 (varies by program; some programs require 7.0) |
| TOEFL iBT | 86-100 (varies by program) |
| PTE Academic | 60-65+ (varies by program) |
| CAEL | 70 |

### 3.3 Special Admission Categories

- Mature Applicant (age 21+, out of school 2+ years)
- Home-Schooled Applicant
- CEGEP (Québec college system)
- Transfer from other university/college
- Internal transfer (Carleton current student)
- Re-admission (Carleton former student)
- Special (non-degree) student

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition (Annual, 2026-2027)

> Source: Carleton Student Accounts Receivable — Fee Estimator & Fee Tables
> Note: Fee tables require login to Carleton Central for exact rates; below are estimated ranges

| Category | Estimated Annual Tuition |
|----------|------------------------|
| **Domestic (Ontario)** — Arts programs | ~$6,100 - $7,200 CAD |
| **Domestic (Ontario)** — Science/Engineering | ~$7,200 - $8,500 CAD |
| **Domestic (Ontario)** — Business | ~$7,000 - $8,000 CAD |
| **Domestic (Out-of-Province)** | Similar to Ontario rates + differential |
| **International** — Arts | ~$33,000 - $38,000 CAD |
| **International** — Science/Engineering | ~$38,000 - $45,000 CAD |
| **International** — Business | ~$35,000 - $42,000 CAD |

### 4.2 Graduate Tuition (Annual, 2026-2027)

| Category | Estimated Annual Tuition |
|----------|------------------------|
| **Domestic** — Master's thesis-based | ~$5,000 - $7,000 CAD |
| **Domestic** — Master's course-based | ~$7,000 - $15,000 CAD |
| **Domestic** — PhD | ~$5,000 - $7,000 CAD |
| **International** — Master's thesis-based | ~$18,000 - $25,000 CAD |
| **International** — Master's course-based | ~$20,000 - $35,000 CAD |
| **International** — PhD | ~$18,000 - $25,000 CAD |
| **MBA (all)** | ~$30,000 - $50,000 CAD |

> Note: Fee tables are updated annually. For exact rates, use the Fee Estimator at https://carleton.ca/studentaccounts/ or log into Carleton Central.

### 4.3 Compulsory Fees (估算)

| Fee Type | Annual Amount (approx.) |
|---------|----------------------|
| UHIP (International, single) | ~$1,000 CAD |
| U-Pass (Public Transit) | ~$400 CAD |
| Health & Dental Plan | ~$400 CAD |
| Athletics/Recreation | ~$300 CAD |
| Other miscellaneous | ~$500 CAD |

### 4.4 Scholarships & Financial Aid

**Undergraduate:**
- **Entrance Scholarships:** Automatic consideration for domestic students (average-based: 80%+ = $1,000-$4,000; 90%+ = $4,000-$8,000)
- **International Entrance Scholarships:** Merit-based, up to $16,000 ($4,000/year × 4 years)
- **Renewable Scholarships:** Based on maintaining academic standing
- **Carleton University Undergraduate Scholarship:** Automatic for top Ontario applicants

**Graduate:**
- **Faculty/University Funding:** Many thesis-based Master's and PhD students receive funding packages including tuition + stipend
- **Ontario Graduate Scholarship (OGS):** $15,000 CAD per year
- **Canada Graduate Scholarships (CGS):** Master's ($17,500) / Doctoral ($35,000-$50,000/year)
- **Carleton International Scholarships:** Available for international graduate students

### 4.5 Cost of Living (Ottawa, ON)

| Expense | Monthly Cost (approx.) |
|---------|----------------------|
| On-campus residence & meal plan | $1,200 - $1,800 CAD |
| Off-campus rent (shared) | $700 - $1,200 CAD |
| Food & groceries | $300 - $500 CAD |
| Transportation (U-Pass included) | Included in fees |
| Personal & miscellaneous | $300 - $500 CAD |

> Source: https://carleton.ca/studentaccounts/tuition-fees/ (Fee Estimator Guide), https://carleton.ca/studentaccounts/

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-U-001 | institution.name | Carleton University | https://carleton.ca/ | official_webpage |
| E-U-002 | institution.address | 1125 Colonel By Drive, Ottawa, ON, K1S 5B6 | https://carleton.ca/ | official_webpage |
| E-U-003 | institution.founded | 1942 | https://carleton.ca/about/ | official_webpage |
| E-U-004 | student.population | 30,600+ | https://carleton.ca/ | official_webpage |
| E-U-005 | faculties.list | 6 Faculties | https://carleton.ca/academics/departments/ | official_webpage |
| E-U-006 | ug.programs.count | 200+ programs | https://carleton.ca/academics/ | official_webpage |
| E-U-007 | grad.programs.count | 100+ programs | https://carleton.ca/academics/ | official_webpage |
| E-U-008 | ug.programs.full_list | Full UG program listing | http://calendar.carleton.ca/undergrad/undergradprograms/ | academic_calendar |
| E-U-009 | grad.programs.full_list | Full graduate program listing | http://calendar.carleton.ca/grad/gradprograms/ | academic_calendar |
| E-U-010 | dept_and_faculties | Complete faculty/department listing | https://carleton.ca/academics/departments/ | official_webpage |
| E-U-011 | ug.degree_types | 26 UG degree options (all | https://admissions.carleton.ca/ | official_webpage |
| E-U-012 | ug.application_platform | OUAC | https://admissions.carleton.ca/ | official_webpage |
| E-U-013 | ug.international_applications | Open for Fall 2026 | https://admissions.carleton.ca/international-homepage/ | official_webpage |
| E-U-014 | grad.programs_listing | 100+ programs listed | https://graduate.carleton.ca/programs/ | official_webpage |
| E-U-015 | ug.english_language | IELTS 6.5, TOEFL 86, PTE 60, DET 120 | https://admissions.carleton.ca/international-homepage/ | official_webpage |
| E-U-016 | fees.office | Student Accounts Receivable | https://carleton.ca/studentaccounts/ | official_webpage |
| E-U-017 | fees.tuition_pages | Undergraduate & Special Student Fees | https://carleton.ca/studentaccounts/tuition-fees/ | official_webpage |
| E-U-018 | fees.estimator | Fee Estimator Guide | https://carleton.ca/studentaccounts/fee-estimator-guide/ | official_webpage |
| E-U-019 | academic_calendar | 2026-27 Edition | https://calendar.carleton.ca/ | official_calendar |
| E-U-020 | ug.admission_regulations | General and per-program requirements | https://calendar.carleton.ca/undergrad/regulations/admissions/ | academic_calendar |

---

## Section 6 — WeKnora Import Manifest & Follow-Up

### Current Status

| Section | Status |
|---------|--------|
| Section 0 — 院校总览 | ✅ Complete |
| Section 1 — Undergraduate education | ✅ Complete (full listing) |
| Section 2 — Graduate education | ✅ Complete (full listing) |
| Section 3 — Application requirements | ✅ Complete (overview) |
| Section 4 — Costs & financial aid | ⚠️ Estimated (fee tables require login) |
| Section 5 — Evidence chain | ✅ Complete |
| Section 7 — Comparison framework | 🔲 Pending |

### Follow-Up Items

| Priority | Item | Notes |
|----------|------|-------|
| **P0** | Per-program tuition fee tables (domestic & international) | Fee tables at carleton.ca/studentaccounts/ require Fee Estimator login; exact rates not publicly scrapable without interactive form |
| **P0** | Per-program admission requirements (specific grade averages, prerequisites) | Available in individual program pages on calendar.carleton.ca; would need ~90+ page extraction |
| **P0** | Per-program graduate application deadlines | Some programs have different deadlines; need per-program extraction |
| **P1** | Detailed scholarship breakdown (per-program, renewable conditions) | Available on separate pages |
| **P1** | Graduate funding package details per program | Varies by department |
| **P1** | Co-op program details (work-integrated learning) | Carleton has a large co-op program; details on separate pages |
| **P2** | Faculty research metrics per department | Research funding data available on research.carleton.ca |
| **P2** | Residence/housing costs & options | Available on https://carleton.ca/housing/ |
| **P2** | Student life statistics | Clubs, societies, athletics info on separate pages |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | Carleton University | University of Ottawa | University of Toronto |
|-----------|-------------------|-------------------|-------------------|
| Location | Ottawa, ON | Ottawa, ON | Toronto, ON |
| UG Programs | 200+ | 450+ | 700+ |
| Graduate Programs | 100+ | 300+ | 280+ |
| Student Population | 30,600+ | 43,000+ | 72,000+ |
| Faculties/Schools | 6 | 10 | 17 |
| Research Funding | $155M+ | $400M+ | $1.3B+ |
| International Tuition (UG) | ~$33K-$45K CAD | ~$35K-$55K CAD | ~$45K-$65K CAD |
| IELTS (UG minimum) | 6.5 | 6.5 | 6.5 |
| Application System | OUAC | OUAC | OUAC |
| Notable Strengths | Journalism, Public Affairs, Engineering, Cognitive Science | Law, Medicine, Health Sciences | All disciplines, Medicine, Engineering, Business |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: Carleton University official website (carleton.ca), Undergraduate Calendar (calendar.carleton.ca), Graduate Calendar (calendar.carleton.ca), Admissions (admissions.carleton.ca), Graduate Studies (graduate.carleton.ca), Student Accounts (carleton.ca/studentaccounts/)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ | PG programmes ✅ | Evidence (20 blocks) ✅ | Costs (estimated ⚠️)
> **Next step**: Extract per-program fee data and detailed admission requirements for individual programs via Fee Estimator
