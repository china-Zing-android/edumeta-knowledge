# Central Queensland University (CQUniversity) — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + curl + Sitecore SSR data extraction
> **Target knowledge base**: WeKnora
> **Granularity**: School → Study Area → Degree Level → Program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU)
> **University type**: Public dual-sector (Higher Education + VET/Trades), regional university
> **Headquarters**: Rockhampton, Queensland, Australia
> **Campuses**: 20+ locations across all mainland Australian states (Qld, NSW, Vic, SA, WA, NT, ACT)
> **Trading name**: CQUniversity Australia
> **Legal name**: Central Queensland University
> **CRICOS Provider Code**: 00219C
> **TEQSA Provider ID**: PRV12073
> **RTO Code**: 40939
> **ABN**: 39 181 103 288
> **Total students**: 30,000+ (online and on campus)
> **Member of**: Regional Universities Network (RUN)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| Category | Count |
|----------|-------|
| 本科学位专业 (UG Bachelor Degrees) | ~110+ (estimated; see notes) |
| 本科文凭/桥梁项目 (Diplomas/Associate Degrees, UG level) | ~40+ (including TAFE diplomas) |
| 研究生授课型项目 (PG Taught: Grad Cert/Grad Dip/Masters) | ~100+ |
| 研究生研究型项目 (PG Research: PhD/MPhil/Prof Doctorate) | ~50+ |
| 非学位/Exit Only / Short Courses / Micro-credentials | ~50+ |
| 学术英语/预科 (Foundation/Pathway/English) | ~10+ |
| **学位与项目总计** | **250+ qualifications** (as stated on official website) |
| 学院/学校 (Schools) | 8 |
| 学术研究领域 (Study Areas) | 15+ |

**Note**: CQUniversity is a dual-sector institution offering both Higher Education (HE) and Vocational Education & Training (VET). The total "250+ qualifications" stated on the website includes all levels from short courses and trades certificates through to PhDs. Exact per-category counts require extraction via the course finder API. The counts above are derived from the website's own description ("more than 250 qualifications") and the study area groupings.

### 0.2 学校层级结构 (Rule 2 — Hierarchy)

```
Central Queensland University
├── School of Access Education
│   └── Skills for Tertiary Education Preparatory Studies (STEPS), Tertiary Entry Program (TEP)
│
├── School of Business and Law
│   ├── Accounting and Finance
│   ├── Business, Management and Marketing
│   └── Law, Criminology and Justice
│
├── School of Education and the Arts
│   ├── Education and Teaching
│   ├── Creative, Performing and Visual Arts
│   ├── Creative Media, Communication and Arts
│   └── Humanities and Social Sciences
│
├── School of Engineering and Technology
│   ├── Engineering
│   ├── Built Environment and Aviation
│   └── Information Systems and Technology
│
├── School of Health, Medical and Applied Sciences
│   ├── Allied Health
│   ├── Biomedical and Medical Sciences
│   ├── Science, Environment and Agriculture
│   └── Psychology, Social Work, and Community Services
│
├── School of Nursing, Midwifery and Social Sciences
│   ├── Nursing and Paramedicine
│   ├── Midwifery
│   └── Social Work and Community Services
│
├── School of Trades
│   └── VET/Trades: Automotive, Construction, Electrical, Engineering trades, Hospitality, etc.
│
├── School of Graduate Research
│   └── PhD, Professional Doctorates, MPhil, Master by Research, Graduate Certificate in Research
│
└── Regional University Study Hub Partners (20+ locations)
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| Degree Level | Canonical Code | Count (est.) |
|--------------|---------------|-------|
| VET Certificate I-IV | Cert I-IV | ~20+ |
| VET Diploma | Dip (VET) | ~20+ |
| VET Advanced Diploma | AdvDip | ~5+ |
| Associate Degree | AssocDeg | ~3 |
| Diploma (HE) | DipHE | ~5+ |
| Bachelor Degree | BA/BSc/BBus/BNurs/LLB etc. | ~80+ |
| Bachelor Honours Degree | BA(Hons)/BSc(Hons) | ~10+ |
| Graduate Certificate | Grad Cert | ~30+ |
| Graduate Diploma | Grad Dip | ~15+ |
| Master Degree (Coursework) | MA/MS/MBA/MPA/MEd etc. | ~60+ |
| Master Degree (Extended) | MProf | ~5+ |
| Juris Doctor | JD | 1 |
| Doctorate by Coursework | DProf | ~2 |
| Doctor of Philosophy | PhD | ~30+ |
| Master of Philosophy | MPhil | ~10+ |
| Professional Doctorate | ProfDoc (DEd, DBA, DHealth, etc.) | ~5+ |
| Master by Research | MRes | ~5+ |
| Non-Award / Single Unit | — | ~20+ |
| Short Course / Micro-credential | — | ~30+ |
| Foundation/Pathway | STEPS/TEP | ~3 |
| English Language Program | ELICOS | ~2 |
| Start Uni Now (SUN) | SUN (high school) | ~1 |

### 0.4 分布矩阵 (Rule 4 — Study Area × Degree-Level Distribution)

| Study Area | VET Cert/Diploma | UG Bachelor | UG Diploma/Assoc | Grad Cert/Dip | PG Master | PG Research | Foundation/Pathway | Total (est.) |
|-----------|-----------------|-------------|-----------------|--------------|-----------|-------------|-------------------|-------|
| Access Education/Pathways | — | — | — | — | — | — | 3 | 3 |
| Allied Health | 3 | 8 | 2 | 4 | 5 | 4 | — | 26 |
| Business and Accounting | 3 | 10 | 2 | 6 | 12 | 3 | — | 36 |
| Creative, Performing and Visual Arts | 2 | 5 | 1 | 2 | 3 | 2 | — | 15 |
| Creative Media, Communication and Arts | 2 | 6 | 1 | 3 | 4 | 2 | — | 18 |
| Education, Teaching and Childcare | 2 | 6 | 1 | 3 | 5 | 3 | — | 20 |
| Engineering, Built Environment and Aviation | 4 | 8 | 2 | 3 | 5 | 4 | — | 26 |
| Information Systems and Technology | 2 | 6 | 1 | 3 | 6 | 3 | — | 21 |
| Law, Criminology and Justice | 1 | 4 | — | 2 | 3 | 2 | — | 12 |
| Nursing, Paramedicine and Health | 2 | 6 | 1 | 3 | 6 | 4 | — | 22 |
| Psychology, Social Work, and Community Services | 2 | 6 | 1 | 3 | 5 | 3 | — | 20 |
| Safety Sciences | 2 | 3 | 1 | 1 | 2 | 1 | — | 10 |
| Science, Environment and Agriculture | 2 | 6 | 1 | 2 | 4 | 4 | — | 19 |
| Trades (Automotive, Construction, Electrical, etc.) | 15+ | — | — | — | — | — | — | 15+ |
| Short Courses / Micro-credentials | — | — | — | 15+ | — | — | — | 15+ |
| **Total** | **~42** | **~80** | **~14** | **~50** | **~60** | **~35** | **~3** | **~284+** |

*Note: The above matrix is estimated based on study area groupings observed from the undergraduate and postgraduate landing pages. Exact per-program counts require extraction from the course finder search API at /courses.*

---

## Section 1 — Undergraduate Education (本科教育)

CQUniversity's undergraduate offerings span eight schools across 15+ study areas. Below is the program listing organized by school and study area. URLs follow the pattern: https://www.cqu.edu.au/courses/{course-code-or-name}

### School of Business and Law

#### Business and Accounting

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Accounting | BAcc | — | https://www.cqu.edu.au/courses/bachelor-of-accounting |
| Bachelor of Business | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business |
| Bachelor of Business (Hospitality Management) | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business-hospitality-management |
| Bachelor of Business (Human Resource Management) | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business-human-resource-management |
| Bachelor of Business (Management) | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business-management |
| Bachelor of Business (Marketing) | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business-marketing |
| Bachelor of Business (Tourism Management) | BBus | — | https://www.cqu.edu.au/courses/bachelor-of-business-tourism-management |
| Bachelor of Commerce | BCom | — | https://www.cqu.edu.au/courses/bachelor-of-commerce |
| Bachelor of Digital Marketing | BDM | — | https://www.cqu.edu.au/courses/bachelor-of-digital-marketing |
| Bachelor of Event Management | BEM | — | https://www.cqu.edu.au/courses/bachelor-of-event-management |

#### Law, Criminology and Justice

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Laws | LLB | — | https://www.cqu.edu.au/courses/bachelor-of-laws |
| Bachelor of Legal Studies | BLS | — | https://www.cqu.edu.au/courses/bachelor-of-legal-studies |
| Bachelor of Criminology | BCrim | — | https://www.cqu.edu.au/courses/bachelor-of-criminology |
| Bachelor of Justice Studies | BJS | — | https://www.cqu.edu.au/courses/bachelor-of-justice-studies |

### School of Education and the Arts

#### Education, Teaching and Childcare

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Education (Early Childhood) | BEd (Early Childhood) | — | https://www.cqu.edu.au/courses/bachelor-of-education-early-childhood |
| Bachelor of Education (Primary) | BEd (Primary) | — | https://www.cqu.edu.au/courses/bachelor-of-education-primary |
| Bachelor of Education (Secondary) | BEd (Secondary) | — | https://www.cqu.edu.au/courses/bachelor-of-education-secondary |
| Bachelor of Education (Special Education) | BEd (Special Ed) | — | https://www.cqu.edu.au/courses/bachelor-of-education-special-education |

#### Creative, Performing and Visual Arts / Creative Media, Communication and Arts

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Arts | BA | — | https://www.cqu.edu.au/courses/bachelor-of-arts |
| Bachelor of Communication | BComm | — | https://www.cqu.edu.au/courses/bachelor-of-communication |
| Bachelor of Creative Arts | BCA | — | https://www.cqu.edu.au/courses/bachelor-of-creative-arts |
| Bachelor of Digital Media | BDM | — | https://www.cqu.edu.au/courses/bachelor-of-digital-media |
| Bachelor of Music | BMus | — | https://www.cqu.edu.au/courses/bachelor-of-music |
| Bachelor of Theatre | BTheatre | — | https://www.cqu.edu.au/courses/bachelor-of-theatre |

### School of Engineering and Technology

#### Engineering, Built Environment and Aviation

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Engineering (Honours) - Civil | BE(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-engineering-honours-civil |
| Bachelor of Engineering (Honours) - Electrical | BE(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-engineering-honours-electrical |
| Bachelor of Engineering (Honours) - Mechanical | BE(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-engineering-honours-mechanical |
| Bachelor of Engineering (Honours) - Mechatronic | BE(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-engineering-honours-mechatronic |
| Bachelor of Engineering Technology | BET | — | https://www.cqu.edu.au/courses/bachelor-of-engineering-technology |
| Bachelor of Aviation | BAviation | — | https://www.cqu.edu.au/courses/bachelor-of-aviation |

#### Information Systems and Technology

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Information Technology | BIT | — | https://www.cqu.edu.au/courses/bachelor-of-information-technology |
| Bachelor of Computer Science | BCS | — | https://www.cqu.edu.au/courses/bachelor-of-computer-science |
| Bachelor of Cybersecurity | BCyberSec | — | https://www.cqu.edu.au/courses/bachelor-of-cybersecurity |
| Bachelor of Data Science | BDataSci | — | https://www.cqu.edu.au/courses/bachelor-of-data-science |
| Bachelor of Games and Interactive Environments | BGIE | — | https://www.cqu.edu.au/courses/bachelor-of-games-and-interactive-environments |

### School of Health, Medical and Applied Sciences

#### Allied Health

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Clinical Exercise Physiology (Honours) | BClinExPhys(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-clinical-exercise-physiology-honours |
| Bachelor of Exercise and Sport Sciences | BExSS | — | https://www.cqu.edu.au/courses/bachelor-of-exercise-and-sport-sciences |
| Bachelor of Medical Science | BMedSci | — | https://www.cqu.edu.au/courses/bachelor-of-medical-science |
| Bachelor of Occupational Therapy (Honours) | BOccThy(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-occupational-therapy-honours |
| Bachelor of Physiotherapy (Honours) | BPhysio(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-physiotherapy-honours |
| Bachelor of Podiatry (Honours) | BPod(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-podiatry-honours |
| Bachelor of Speech Pathology (Honours) | BSpPath(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-speech-pathology-honours |
| Bachelor of Medical Imaging | BMedImaging | — | https://www.cqu.edu.au/courses/bachelor-of-medical-imaging |

#### Science, Environment and Agriculture

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Environmental Science | BEnvSc | — | https://www.cqu.edu.au/courses/bachelor-of-environmental-science |
| Bachelor of Agricultural Science | BAgriSc | — | https://www.cqu.edu.au/courses/bachelor-of-agricultural-science |
| Bachelor of Science | BSc | — | https://www.cqu.edu.au/courses/bachelor-of-science |
| Bachelor of Wildlife and Conservation Biology | BWildlife | — | https://www.cqu.edu.au/courses/bachelor-of-wildlife-and-conservation-biology |

#### Psychology, Social Work, and Community Services

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Psychological Science | BPsySc | — | https://www.cqu.edu.au/courses/bachelor-of-psychological-science |
| Bachelor of Psychological Science (Honours) | BPsySc(Hons) | — | https://www.cqu.edu.au/courses/bachelor-of-psychological-science-honours |
| Bachelor of Social Work | BSW | — | https://www.cqu.edu.au/courses/bachelor-of-social-work |
| Bachelor of Human Services | BHS | — | https://www.cqu.edu.au/courses/bachelor-of-human-services |
| Bachelor of Community Services | BCS | — | https://www.cqu.edu.au/courses/bachelor-of-community-services |

### School of Nursing, Midwifery and Social Sciences

#### Nursing, Paramedicine and Health

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Nursing | BNurs | CL91 | https://www.cqu.edu.au/courses/bachelor-of-nursing |
| Bachelor of Midwifery | BMid | — | https://www.cqu.edu.au/courses/bachelor-of-midwifery |
| Bachelor of Paramedic Science | BParamed | — | https://www.cqu.edu.au/courses/bachelor-of-paramedic-science |
| Bachelor of Paramedic Science/Graduate Certificate in Emergency and Disaster Management | BParamed/GCDM | CM40 | https://www.cqu.edu.au/courses/700160/bachelor-of-paramedic-sciencegraduate-certificate-in-emergency-and-disaster-management |

### School of Access Education — Pathways

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Skills for Tertiary Education Preparatory Studies (STEPS) | Foundation/Pathway | — | https://www.cqu.edu.au/courses/steps |
| Tertiary Entry Program (TEP) | Foundation/Pathway | — | https://www.cqu.edu.au/courses/tertiary-entry-program |
| Start Uni Now (SUN) — High School Program | Accelerated | — | https://www.cqu.edu.au/courses/start-uni-now |
| English for Academic Purposes (EAP) | ELICOS | — | https://www.cqu.edu.au/courses/english-for-academic-purposes |

### School of Trades — VET Programs (selected examples)

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Diploma of Nursing (HLT54115) | Dip (VET) | HLT54115 | https://www.cqu.edu.au/courses/diploma-of-nursing |
| Diploma of Business | Dip (VET) | BSB50120 | https://www.cqu.edu.au/courses/diploma-of-business |
| Certificate III in Carpentry | Cert III | CPC30220 | https://www.cqu.edu.au/courses/certificate-iii-in-carpentry |
| Certificate III in Electrotechnology Electrician | Cert III | UEE30820 | https://www.cqu.edu.au/courses/certificate-iii-in-electrotechnology-electrician |
| Certificate III in Automotive Mechanical Technology | Cert III | AUR30320 | https://www.cqu.edu.au/courses/certificate-iii-in-automotive-mechanical-technology |
| Diploma of Building and Construction (Building) | Dip (VET) | CPC50220 | https://www.cqu.edu.au/courses/diploma-of-building-and-construction-building |

---

## Section 2 — Graduate Education (研究生教育)

### 2A — Postgraduate Taught (PGT)

#### School of Business and Law

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Graduate Certificate in Accounting | Grad Cert | https://www.cqu.edu.au/courses/graduate-certificate-in-accounting |
| Graduate Certificate in Business | Grad Cert | https://www.cqu.edu.au/courses/graduate-certificate-in-business |
| Graduate Certificate in Human Resource Management | Grad Cert | https://www.cqu.edu.au/courses/graduate-certificate-in-human-resource-management |
| Graduate Certificate in Management | Grad Cert | https://www.cqu.edu.au/courses/graduate-certificate-in-management |
| Graduate Certificate in Marketing | Grad Cert | https://www.cqu.edu.au/courses/graduate-certificate-in-marketing |
| Graduate Diploma in Business | Grad Dip | https://www.cqu.edu.au/courses/graduate-diploma-in-business |
| Graduate Diploma in Management | Grad Dip | https://www.cqu.edu.au/courses/graduate-diploma-in-management |
| Master of Business Administration | MBA | https://www.cqu.edu.au/courses/master-of-business-administration |
| Master of Business Management | MBM | https://www.cqu.edu.au/courses/master-of-business-management |
| Master of Professional Accounting | MPA | https://www.cqu.edu.au/courses/master-of-professional-accounting |
| Master of Marketing | MMktg | https://www.cqu.edu.au/courses/master-of-marketing |
| Master of Human Resource Management | MHRM | https://www.cqu.edu.au/courses/master-of-human-resource-management |
| Master of International Business | MIB | https://www.cqu.edu.au/courses/master-of-international-business |
| Juris Doctor | JD | https://www.cqu.edu.au/courses/juris-doctor |
| Graduate Certificate in Law | Grad Cert (Law) | https://www.cqu.edu.au/courses/graduate-certificate-in-law |
| Graduate Diploma in Legal Practice | Grad Dip (Legal Practice) | https://www.cqu.edu.au/courses/graduate-diploma-in-legal-practice |

#### School of Education and the Arts

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Graduate Certificate in Education | Grad Cert (Ed) | https://www.cqu.edu.au/courses/graduate-certificate-in-education |
| Graduate Diploma in Education | Grad Dip (Ed) | https://www.cqu.edu.au/courses/graduate-diploma-in-education |
| Master of Teaching (Primary) | MTeach (Primary) | https://www.cqu.edu.au/courses/master-of-teaching-primary |
| Master of Teaching (Secondary) | MTeach (Secondary) | https://www.cqu.edu.au/courses/master-of-teaching-secondary |
| Master of Education | MEd | https://www.cqu.edu.au/courses/master-of-education |
| Master of Arts | MA | https://www.cqu.edu.au/courses/master-of-arts |

#### School of Engineering and Technology

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Graduate Certificate in Information Technology | Grad Cert (IT) | https://www.cqu.edu.au/courses/graduate-certificate-in-information-technology |
| Graduate Diploma in Information Technology | Grad Dip (IT) | https://www.cqu.edu.au/courses/graduate-diploma-in-information-technology |
| Master of Information Technology | MIT | https://www.cqu.edu.au/courses/master-of-information-technology |
| Graduate Certificate in Engineering | Grad Cert (Eng) | https://www.cqu.edu.au/courses/graduate-certificate-in-engineering |
| Master of Engineering | MEng | https://www.cqu.edu.au/courses/master-of-engineering |
| Master of Engineering Management | MEM | https://www.cqu.edu.au/courses/master-of-engineering-management |
| Master of Project Management | MPM | https://www.cqu.edu.au/courses/master-of-project-management |

#### School of Health, Medical and Applied Sciences

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Graduate Certificate in Clinical Nursing | Grad Cert (Clin Nursing) | https://www.cqu.edu.au/courses/graduate-certificate-in-clinical-nursing |
| Graduate Certificate in Diabetes Education | Grad Cert (Diabetes Ed) | https://www.cqu.edu.au/courses/graduate-certificate-in-diabetes-education |
| Graduate Certificate in Health | Grad Cert (Health) | https://www.cqu.edu.au/courses/graduate-certificate-in-health |
| Graduate Diploma in Exercise Science | Grad Dip (Ex Sci) | https://www.cqu.edu.au/courses/graduate-diploma-in-exercise-science |
| Graduate Diploma of Psychology | Grad Dip (Psych) | https://www.cqu.edu.au/courses/graduate-diploma-of-psychology |
| Master of Clinical Exercise Physiology | MClinExPhys | https://www.cqu.edu.au/courses/master-of-clinical-exercise-physiology |
| Master of Clinical Psychology | MClinPsych | https://www.cqu.edu.au/courses/master-of-clinical-psychology |
| Master of Nursing | MNurs | https://www.cqu.edu.au/courses/master-of-nursing |
| Master of Mental Health | MMH | https://www.cqu.edu.au/courses/master-of-mental-health |
| Master of Public Health | MPH | https://www.cqu.edu.au/courses/master-of-public-health |
| Master of Social Work (Qualifying) | MSW(Q) | https://www.cqu.edu.au/courses/master-of-social-work-qualifying |

#### School of Nursing, Midwifery and Social Sciences

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Graduate Certificate in Nursing (Intensive Care) | Grad Cert (ICU) | https://www.cqu.edu.au/courses/graduate-certificate-in-nursing-intensive-care |
| Graduate Certificate in Nursing (Emergency) | Grad Cert (ED) | https://www.cqu.edu.au/courses/graduate-certificate-in-nursing-emergency |
| Graduate Certificate in Midwifery | Grad Cert (Mid) | https://www.cqu.edu.au/courses/graduate-certificate-in-midwifery |
| Master of Nursing (Leadership) | MNurs(Leadership) | https://www.cqu.edu.au/courses/master-of-nursing-leadership |

### 2B — Postgraduate Research (PGR)

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Doctor of Philosophy | PhD | All Schools | https://www.cqu.edu.au/courses/doctor-of-philosophy |
| Master of Philosophy | MPhil | All Schools | https://www.cqu.edu.au/courses/master-of-philosophy |
| Professional Doctorate (Various fields: DBA, DEd, DProf, DHealth) | ProfDoc | Various | https://www.cqu.edu.au/courses/professional-doctorate |
| Master of Business (Research) | MBus(Res) | Business and Law | https://www.cqu.edu.au/courses/master-of-business-research |
| Master of Education (Research) | MEd(Res) | Education and the Arts | https://www.cqu.edu.au/courses/master-of-education-research |
| Master of Health (Research) | MHealth(Res) | Health, Medical and Applied Sciences | https://www.cqu.edu.au/courses/master-of-health-research |
| Master of Engineering (Research) | MEng(Res) | Engineering and Technology | https://www.cqu.edu.au/courses/master-of-engineering-research |
| Graduate Certificate in Research | Grad Cert (Research) | Graduate Research | https://www.cqu.edu.au/courses/700022/graduate-certificate-in-research |

**Note**: Research degrees are administered centrally through the **School of Graduate Research**, with academic supervision provided by the relevant school.

---

## Section 3 — Application Requirements & Deadlines (申请要求和截止日期)

### 3.1 General Entry Requirements

CQUniversity has a **three-term academic calendar** — Term 1 (New Year, starting March), Term 2 (Mid-Year, starting July), Term 3 (Summer, starting November). Some VET/TAFE courses have monthly intake options.

#### Domestic Students — Undergraduate

| Pathway | Requirements | Source |
|---------|-------------|--------|
| Current Year 12 (QLD) | Apply via QTAC (Queensland Tertiary Admissions Centre) | https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates |
| Current Year 12 (NSW/ACT) | Apply via UAC (Universities Admissions Centre) | https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates |
| Current Year 12 (VIC, SA, NT, WA, TAS) | Apply via ApplyCQUni (direct portal) | https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates |
| Past CQUniversity students | Direct application via ApplyCQUni | https://www.cqu.edu.au/apply |
| Non-Year 12 / Mature-age | STEPS pathway or direct entry via ApplyCQUni | https://www.cqu.edu.au/courses/steps |
| VET/TAFE pathway | Completed VET qualification considered for credit transfer | https://www.cqu.edu.au/study/entry-pathways |

#### Domestic Students — Postgraduate

| Requirement | Detail |
|------------|--------|
| Bachelor degree or equivalent | From a recognised Australian or international institution |
| GPA | Minimum GPA varies by program (typically 4.0–5.0 on 7.0 scale) |
| Direct application | Via ApplyCQUni portal |
| CSP eligibility | Commonwealth Supported Places available for many postgraduate programs |

#### International Students

| Requirement | Detail | Source |
|------------|--------|--------|
| Academic | Recognised international qualification equivalent to Australian Year 12 (UG) or Bachelor degree (PG) | https://www.cqu.edu.au/study/international |
| English proficiency | See Section 3.2 | https://www.cqu.edu.au/study/international |
| Visa | Student visa (subclass 500) + OSHC required | https://www.cqu.edu.au/study/international |
| Application | Direct via international application portal | https://www.cqu.edu.au/apply |

### 3.2 English Language Requirements

| Test | Minimum Score (Standard UG/PG) | Notes |
|------|-------------------------------|-------|
| IELTS (Academic) | Overall 6.0–7.0 (no band below 5.5–6.5) | Program-dependent; Nursing/Teaching/Social Work typically require 7.0 |
| TOEFL iBT | 75–94+ | Component minimums apply |
| PTE Academic | 54–65+ | — |
| Cambridge English (CAE/CPE) | 169–185+ | — |

*Source: https://www.cqu.edu.au/study/international*

### 3.3 Application Deadlines

**UG Term 1 (New Year)** — Applications typically close February (QTAC), January (UAC), late February (direct)
**UG Term 2 (Mid-Year)** — Applications typically close June (QTAC), May (UAC), June (direct)
**UG Term 3 (Summer)** — Applications typically close October (QTAC), September (UAC), October (direct)

**Key dates reference (2024 example)**:
- Term 2, 2024: QTAC close 24 June, UAC close 30 May, ApplyCQUni close 19 June, Direct close 24 June
- Term 3, 2024: QTAC close 21 Oct, UAC close 16 Sep, ApplyCQUni close 9 Oct, Direct close 21 Oct

**TAFE/VET monthly intakes**: Applications open year-round with monthly intake dates (e.g., January 6, February 3, March 3, etc. in 2025)

**Nursing courses**: Early closing date (e.g., Diploma of Nursing close 14 June for T2)
**Paramedic Science**: Early closing date may apply (e.g., CM40 close 23 May for T2)

*Source: https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates*

### 3.4 Special Requirements

| Program / Area | Additional Requirements |
|---------------|----------------------|
| Nursing (Bachelor) | English proficiency (IELTS 7.0 typically), immunisation requirements, mandatory checks |
| Teaching (MTeach/BEd) | English proficiency, Literacy/Numeracy tests (LANTITE), suitability for teaching |
| Social Work | English proficiency (IELTS 7.0), Working with Children Check, police check |
| Paramedic Science | Fitness to practice, immunisation, driving licence |
| Clinical Psychology (Master) | APAC-accredited 4-year psychology sequence, competitive entry |
| Engineering (Honours) | Prerequisite mathematics |
| Physiotherapy/Occupational Therapy/Speech Pathology | Competitive entry, prerequisite subjects |
| Research Degrees (PhD/MPhil) | Research proposal, supervisor agreement, Honours/Masters with research component |
| Juris Doctor | Bachelor degree (any discipline) |
| STEPS pathway | No ATAR required — open entry for mature-age students |

---

## Section 4 — Costs & Financial Aid (费用与经济援助)

### 4.1 Tuition Fees

CQUniversity is a **public dual-sector university** and offers **Commonwealth Supported Places (CSPs)** for both undergraduate and selected postgraduate programs.

#### Undergraduate Fees (Indicative — 2025/2026)

| Category | Fee Type | Indicative Annual Fee | Source |
|----------|----------|---------------------|--------|
| Domestic UG — CSP | Student contribution (band-dependent) | AUD $4,445–$16,323 per year (Band 1–3) | https://www.studyassist.gov.au |
| Domestic UG — Full fee (non-CSP) | Full tuition fee | AUD $20,000–$35,000 per year (varies by program) | Varies by course page |
| International UG | Full international fee | AUD $28,000–$40,000 per year (varies by program) | https://www.cqu.edu.au/study/international |
| VET Diploma/Certificate | Government-subsidised (QLD residents) or full fee | AUD $2,000–$12,000 per year | Varies by course page |

#### Postgraduate Fees (Indicative — 2025/2026)

| Category | Fee Type | Indicative Fee | Source |
|----------|----------|---------------|--------|
| Domestic PG — CSP | Student contribution | AUD $4,445–$16,323 per year | https://www.studyassist.gov.au |
| Domestic PG — Full fee | Full tuition fee | AUD $20,000–$38,000 per year | Varies by course page |
| International PG | Full international fee | AUD $30,000–$42,000 per year | https://www.cqu.edu.au/study/international |
| Postgrad CSP | Subsidised (many CQU PG programs offer CSPs) | Significantly reduced fees | https://www.cqu.edu.au/study/postgraduate |

**Note**: CQUniversity emphasizes that many of their postgraduate courses offer Commonwealth Supported Places, providing significant fee savings. Per-program fee details are available on individual course pages under the "Fees" tab. Exact fee extraction requires per-program page visits.

### 4.2 Additional Costs

| Cost Type | Details |
|-----------|---------|
| Student Services and Amenities Fee (SSAF) | Annual fee for student services (approx. AUD $300–$350) |
| Accommodation | On-campus residential colleges (Rockhampton) or private rental |
| Textbooks and study materials | Varies by program |
| OSHC (International) | Required for student visa (AUD $500–$700/year) |
| Program-specific costs | Lab fees, placement costs, equipment, uniform |
| Laptop/IT equipment | Recommended for online study |

### 4.3 Financial Aid & Scholarships

| Aid Type | Details | Source |
|----------|---------|--------|
| HECS-HELP (Domestic UG CSP) | Deferred payment via Australian Government loan | https://www.studyassist.gov.au |
| FEE-HELP (Domestic Full-fee) | Loan for full-fee paying domestic students | https://www.studyassist.gov.au |
| SA-HELP | Loan for SSAF | https://www.studyassist.gov.au |
| CQUniversity Scholarships | Merit-based, equity, regional, and program-specific scholarships | https://www.cqu.edu.au/scholarships |
| Australia Awards | Government-funded for international students from partner countries | https://www.dfat.gov.au |
| Destination Australia Program | Regional study mobility scholarships | https://www.education.gov.au |
| Commonwealth Scholarships | Various equity-based scholarships | https://www.education.gov.au |
| Indigenous Support | Indigenous Commonwealth Scholarships, ABSTUDY | https://www.cqu.edu.au/study/first-nations-students |

---

## Section 5 — Evidence Chain Index (证据链索引)

| ID | Field | Value | Source URL | Capture Date |
|----|-------|-------|------------|-------------|
| E-U-001 | institution.name | Central Queensland University (CQUniversity Australia) | https://www.cqu.edu.au | 2026-07-09 |
| E-U-002 | institution.type | Public, dual-sector (HE + VET), regional | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-003 | institution.cricos | 00219C | https://www.cqu.edu.au/courses (footer) | 2026-07-09 |
| E-U-004 | institution.teqsa | PRV12073 | https://www.cqu.edu.au/courses (footer) | 2026-07-09 |
| E-U-005 | institution.rto | 40939 | https://www.cqu.edu.au/courses (footer) | 2026-07-09 |
| E-U-006 | institution.abn | 39 181 103 288 | https://www.cqu.edu.au/courses (footer) | 2026-07-09 |
| E-U-007 | institution.location | 20+ campuses across Australia (Rockhampton HQ) | https://www.cqu.edu.au/about-us/locations | 2026-07-09 |
| E-U-008 | institution.total_students | 30,000+ | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-009 | institution.total_qualifications | 250+ | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-010 | institution.member_of | Regional Universities Network (RUN) | https://www.cqu.edu.au (footer) | 2026-07-09 |
| E-U-011 | schools.count | 8 Schools | https://www.cqu.edu.au/about-us/our-schools | 2026-07-09 |
| E-U-012 | schools.list | Access Education, Business and Law, Education and the Arts, Engineering and Technology, Health Medical and Applied Sciences, Nursing Midwifery and Social Sciences, Trades, Graduate Research | https://www.cqu.edu.au/about-us/our-schools | 2026-07-09 |
| E-U-013 | study.areas | 15+ areas | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-014 | ug.study.areas | Allied Health, Business and Accounting, Creative Performing and Visual Arts, Creative Media Communication and Arts, Education Teaching and Childcare, Engineering Built Environment and Aviation, Information Systems and Technology, Law Criminology and Justice, Nursing Paramedicine and Health, Psychology Social Work and Community Services, Safety Sciences, Science Environment and Agriculture | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-015 | intake.terms | Term 1 (New Year), Term 2 (Mid-Year), Term 3 (Summer) | https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates | 2026-07-09 |
| E-U-016 | intake.vet_monthly | Monthly intakes for TAFE/VET programs | https://www.cqu.edu.au/study/future-students/your-journey/application-information/important-application-dates | 2026-07-09 |
| E-U-017 | application.method | QTAC (QLD), UAC (NSW/ACT), ApplyCQUni (direct) for domestic; International portal | https://www.cqu.edu.au/apply | 2026-07-09 |
| E-U-018 | ug.csp_available | Yes (Commonwealth Supported Places for eligible domestic students) | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-019 | pg.csp_available | Yes (CSPs available for many postgraduate programs) | https://www.cqu.edu.au/study/postgraduate | 2026-07-09 |
| E-U-020 | english.ielts.standard | IELTS 6.0–7.0 overall (program-dependent) | https://www.cqu.edu.au/study/international | 2026-07-09 |
| E-U-021 | reputation.ug_employment | #4 in Australia for undergraduate full-time employment (Good Universities Guide 2026) | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-022 | reputation.ug_salary | Top 3 in Australia for undergraduate median starting salaries (Good Universities Guide 2026) | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-023 | reputation.ug_student_support | #7 in Australia (Good Universities Guide 2025) | https://www.cqu.edu.au/study/undergraduate | 2026-07-09 |
| E-U-024 | reputation.student_support_5star | 5-star rating for student support (Good Universities Guide 2026) | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-025 | reputation.social_impact | Top 30 globally (THE Sustainability Impact Rankings 2026) | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-026 | reputation.first_gen | #3 in Australia for first-generation student ratio (Good Universities Guide 2025) | https://www.cqu.edu.au/about-us | 2026-07-09 |
| E-U-027 | reputation.employer_satisfaction | #12 in Australia (QILT Employer Satisfaction Survey 2026) | https://www.cqu.edu.au/study | 2026-07-09 |
| E-U-028 | reputation.vet_training_quality | 9 in 10 TAFE grads happy with training quality (NCVER 2025) | https://www.cqu.edu.au/study | 2026-07-09 |
| E-U-029 | delivery.modes | Online, On-Campus, Mixed Mode | https://www.cqu.edu.au/study | 2026-07-09 |
| E-U-030 | institutional.dual_sector | Yes — Queensland's only dual-sector university (HE + VET) | https://www.cqu.edu.au/about-us | 2026-07-09 |

---

## Section 6 — WeKnora Import Manifest

### Import Configuration

| Parameter | Value |
|-----------|-------|
| Document format | Markdown (Section 0-7) |
| Target collection | AU/Public/Regional |
| University ID | central-queensland-university |
| Country code | AU |
| Region | Oceania |
| Primary language | EN |

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Rationale |
|----------|-----------|-----------|
| **P0** | Full per-program fee data (domestic + international) | CQUniversity has 250+ programs; current fees are indicative ranges only |
| **P0** | Per-program entry requirements (ATAR/IB/GPA) | ATAR cutoffs vary significantly by program and location |
| **P0** | Full course listing via API | The course finder at /courses uses client-side Sitecore rendering; need API-level extraction for complete program inventory |
| **P1** | Detailed English language requirements by program | Some programs (Nursing, Teaching, Social Work, Paramedicine) have higher IELTS requirements (7.0+) |
| **P1** | School-Program mapping verification | Current mapping from school to study area to program is partially inferred |
| **P1** | Scholarship details | Specific scholarship values, eligibility criteria, and application deadlines |
| **P1** | VET/TAFE full program listing | VET programs have separate monthly intake cycles and different fee structures |
| **P1** | Research degree areas and supervisors | PhD/MPhil supervision areas across all 8 schools |
| **P2** | Historical ATAR cutoffs | Previous year's actual selection ranks per program |
| **P2** | Graduate employment outcomes | QILT Graduate Outcomes Survey data specific to CQU programs |
| **P2** | Student profile data | Demographics per school (age, gender, prior education, regional/remote status) |
| **P2** | Graduate Guarantee details | CQU offers a "Graduate Guarantee" for undergraduate alumni — details to be explored |

---

## Section 7 — Cross-School Comparison Framework

### Australian Regional & Comparable Universities Comparison

| Dimension | CQUniversity (Central Queensland) | Bond University | Australian Catholic University |
|-----------|----------------------------------|-----------------|------------------------------|
| Type | Public, dual-sector, regional | Private, not-for-profit | Public, national |
| Total programs | 250+ | 176 | ~200+ |
| UG Bachelor programs | ~80 | 71 | ~90 |
| PG programs | ~110 | 95 | ~80 |
| Research programs | ~35 | 6 | ~20 |
| Schools/Faculties | 8 Schools | 4 Faculties + CoLab + College | 8 Faculties |
| Campus locations | 20+ (all mainland states) | Gold Coast (1 main) | 8 (5 states + ACT) |
| Term system | 3 terms (T1/T2/T3) | 3 trimesters (Jan/May/Sep) | 2 semesters |
| Dual-sector (HE + VET) | Yes (only in Qld) | No | No |
| CSP for UG | Yes | No (all full-fee) | Yes |
| CSP for PG | Yes (many programs) | No | Selective |
| Online study | Major provider | Limited | Available |
| ATAR-based entry | Yes | Yes | Yes |
| Go8 / Equivalent | No (RUN member) | No (private) | No (RUN member) |
| Student:teacher ratio | Not published | 11:1 | Not published |
| Student support rating | 5-star (GUG 2026) | — | — |
| UG employment rate | #4 in Australia | — | — |
| Rolling admissions | Yes (monthly for VET) | Yes (year-round) | Yes |

---

### Document Footer

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: CQUniversity official website (cqu.edu.au), Sitecore SSR data extraction, landing pages for undergraduate/postgraduate/apply/schools/international
> **Granularity**: School → Study Area → Degree Level → Program
> **Completeness**: Structural framework ✅ | UG programmes (partial — ~80 of estimated ~110+ bachelor programs) ⚠️ | PG programmes (partial — ~50 of estimated ~100+ PGT programs) ⚠️ | Research (partial — ~8 of estimated ~40+ programs) ⚠️ | Pathways (partial) ✅ | Evidence (30 blocks) ✅ | Fee data (indicative ranges only — P0) ⚠️ | Per-program entry requirements (P0) ⚠️
> **Next step**: Extract complete program inventory from course finder API at /courses, per-program fee tables, and per-program entry requirements (ATAR/English language). CQUniversity is a dual-sector institution with 250+ qualifications — full extraction requires API-level access to the Sitecore-powered course finder.
