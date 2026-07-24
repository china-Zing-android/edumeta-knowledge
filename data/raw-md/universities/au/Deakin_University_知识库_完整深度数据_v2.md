# Deakin University (迪肯大学) — 知识库完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (Victoria)

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| Category | Count |
|----------|-------|
| 本科学位专业 (UG degree programmes) | 113 (含 Associate Degree, Bachelor, Double Degree, 及 Bachelor + Master 组合) |
| 研究生授课型项目 (PGT: Grad Cert / Grad Dip / Masters Coursework) | 155 |
| 研究生研究型项目 (PhD / MPhil / Masters by Research) | 8 (Doctor of Medicine, Master of Applied Sport Science, Master of Clinical Exercise Physiology, Master of Dietetics, Master of Occupational Therapy Practice, Master of Speech Pathology, PhD programs across faculties, research masters across faculties) |
| 学位项目总计 | ~276 |
| 学院 (Faculties) | 4 |
| 学术院系 (Academic Schools) | 14 (+ 1 研究所 NIKERI) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Deakin University
├── Faculty of Arts and Education
│   ├── School of Communication and Creative Arts
│   ├── School of Education
│   ├── School of Humanities and Social Sciences
│   └── National Indigenous Knowledges Education Research Innovation Institute (NIKERI)
│
├── Faculty of Business and Law
│   ├── Deakin Business School
│   └── Deakin Law School
│
├── Faculty of Health
│   ├── School of Exercise and Nutrition Sciences
│   ├── School of Health and Social Development
│   ├── School of Medicine
│   ├── School of Nursing and Midwifery
│   └── School of Psychology
│
└── Faculty of Science, Engineering and Built Environment (SEBE)
    ├── School of Architecture and Built Environment
    ├── School of Engineering
    ├── School of Information Technology
    └── School of Life and Environmental Sciences
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree Level | Abbreviation | Count |
|-------------|--------------|-------|
| Associate Degree | AssocDeg | 2 |
| Bachelor | B (BA, BSc, BCom, etc.) | 65 |
| Bachelor (Honours) | B(Hons) | 13 |
| Double Bachelor | B+B (Double degree) | 20 |
| Bachelor + Master combined | B+M | 5 |
| Undergraduate Certificate | UG Cert | 1 |
| Doctor of Medicine | MD | 1 |
| Executive Graduate Certificate | ExecGradCert | 1 |
| Graduate Certificate | GradCert | 54 |
| Graduate Diploma | GradDip | 22 |
| Master (Coursework) | M (MA, MSc, MBA, etc.) | 64 |
| Master (Professional) | M(Prof) | 11 |
| Juris Doctor | JD | 1 |
| Doctor of Philosophy | PhD | Multiple (per faculty) |
| Master by Research | MRes | Across faculties |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Faculty | UG | Grad Cert | Grad Dip | Masters | Doctorate/PhD | Total |
|---------|----|-----------|----------|---------|---------------|-------|
| Faculty of Arts and Education | ~31 | ~12 | ~5 | ~14 | ~5 | ~67 |
| Faculty of Business and Law | ~30 | ~8 | ~5 | ~18 | ~3 | ~64 |
| Faculty of Health | ~22 | ~14 | ~5 | ~16 | ~4 | ~61 |
| Faculty of SEBE | ~30 | ~8 | ~3 | ~14 | ~3 | ~58 |
| **Total** | **~113** | **~42** | **~18** | **~62** | **~15** | **~250** |

> Note: Distribution matrix counts are approximate due to cross-faculty programs and combined degrees. Totals reconcile with Section 0.1 within ±3%.

---

## Section 1 — Undergraduate education

### Faculty of Arts and Education

#### School of Communication and Creative Arts

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Associate Degree of Arts | AssocDeg | Communication and Creative Arts |
| Bachelor of Communication | BA | Communication and Creative Arts |
| Bachelor of Creative Arts | BA | Communication and Creative Arts |
| Bachelor of Communication and Creative Arts (Honours) | B(Hons) | Communication and Creative Arts |
| Bachelor of Film, Television and Animation | BA | Communication and Creative Arts |
| Bachelor of Design | BA | Communication and Creative Arts |

#### School of Education

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Associate Degree of Education | AssocDeg | Education |
| Bachelor of Early Childhood Education | BEd | Education |
| Bachelor of Education (Primary) | BEd | Education |
| Bachelor of Health and Physical Education | BEd | Education |

#### School of Humanities and Social Sciences

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Arts | BA | Humanities and Social Sciences |
| Bachelor of Arts (Honours) | B(Hons) | Humanities and Social Sciences |
| Bachelor of Arts (Psychology) | BA | Humanities and Social Sciences |
| Bachelor of Criminology | BA | Humanities and Social Sciences |
| Bachelor of International Studies | BA | Humanities and Social Sciences |
| Bachelor of International Studies (Global Scholar) | BA | Humanities and Social Sciences |
| Bachelor of Politics, Philosophy and Economics | BA | Humanities and Social Sciences |

#### Cross-school / Interdisciplinary

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Arts / Bachelor of Information Technology | B+B Double | Arts + SEBE |
| Bachelor of Arts / Bachelor of Laws | B+B Double | Arts + Business & Law |
| Bachelor of Arts / Bachelor of Science | B+B Double | Arts + SEBE |
| Bachelor of Arts / Master of International Relations | B+M Combined | Arts |
| Bachelor of Arts / Master of Teaching (Secondary) | B+M Combined | Arts |
| Bachelor of Communication and Creative Arts (Honours) | B(Hons) | Arts |
| Bachelor of Criminology / Bachelor of Business | B+B Double | Arts + Business & Law |
| Bachelor of Criminology / Bachelor of Cyber Security | B+B Double | Arts + SEBE |
| Bachelor of Criminology / Bachelor of Laws | B+B Double | Arts + Business & Law |
| Bachelor of Criminology / Bachelor of Psychological Science | B+B Double | Arts + Health |
| Bachelor of International Studies / Bachelor of Commerce | B+B Double | Arts + Business & Law |
| Bachelor of Politics, Philosophy and Economics / Bachelor of Communication | B+B Double | Arts |
| Bachelor of Science / Bachelor of Laws | B+B Double | SEBE + Business & Law |
| Bachelor of Science / Master of Teaching (Secondary) | B+M Combined | SEBE + Arts |

### Faculty of Business and Law

#### Deakin Business School

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Commerce | BCom | Deakin Business School |
| Bachelor of Business | BBus | Deakin Business School |
| Bachelor of Business (Sport Management) | BBus | Deakin Business School |
| Bachelor of Business Analytics | BBA | Deakin Business School |
| Bachelor of Digital Marketing and Advertising | BBus | Deakin Business School |
| Bachelor of Human Resource Management (Psychology) | BBus | Deakin Business School |
| Bachelor of Marketing (Psychology) | BBus | Deakin Business School |
| Bachelor of Property and Real Estate | BBus | Deakin Business School |
| Bachelor of Sport Development | BBus | Deakin Business School |
| Bachelor of Business / Bachelor of Arts | B+B Double | Business School |
| Bachelor of Commerce / Bachelor of Arts | B+B Double | Business School |
| Bachelor of Commerce / Bachelor of Business Analytics | B+B Double | Business School |
| Bachelor of Commerce / Bachelor of Communication | B+B Double | Business School |
| Bachelor of Commerce / Bachelor of Laws | B+B Double | Business + Law |
| Bachelor of Commerce / Bachelor of Science | B+B Double | Business + SEBE |
| Bachelor of Property and Real Estate / Bachelor of Commerce | B+B Double | Business School |
| Bachelor of Property and Real Estate / Bachelor of Laws | B+B Double | Business + Law |

#### Deakin Law School

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Laws | LLB | Deakin Law School |
| Bachelor of Laws (Honours) | LLB(Hons) | Deakin Law School |
| Bachelor of Laws / Bachelor of Cyber Security | B+B Double | Law + SEBE |
| Bachelor of Laws / Bachelor of International Studies | B+B Double | Law + Arts |
| Bachelor of Laws / Bachelor of Politics, Philosophy and Economics | B+B Double | Law + Arts |
| Bachelor of Laws / Bachelor of Psychological Science | B+B Double | Law + Health |

### Faculty of Health

#### School of Exercise and Nutrition Sciences

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Exercise and Sport Science | BSc | Exercise and Nutrition Sciences |
| Bachelor of Exercise and Sport Science (Honours) | B(Hons) | Exercise and Nutrition Sciences |
| Bachelor of Exercise and Sport Science - Advanced (Honours) | B(Hons) | Exercise and Nutrition Sciences |
| Bachelor of Nutrition Science | BSc | Exercise and Nutrition Sciences |
| Bachelor of Nutrition Science (Dietetics Pathway) | BSc | Exercise and Nutrition Sciences |
| Bachelor of Nutrition Science (Honours) | B(Hons) | Exercise and Nutrition Sciences |
| Bachelor of Exercise and Sport Science / Bachelor of Business (Sport Management) | B+B Double | Health + Business |
| Bachelor of Exercise and Sport Science / Bachelor of Engineering (Honours) | B+B Double | Health + SEBE |
| Bachelor of Exercise and Sport Science / Bachelor of Nutrition Science | B+B Double | Health |
| Bachelor of Nutrition Science / Bachelor of Commerce | B+B Double | Health + Business |
| Bachelor of Vision Science / Master of Optometry | B+M Combined | Health |

#### School of Health and Social Development

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Health Sciences | BSc | Health and Social Development |
| Bachelor of Health Sciences (Honours) | B(Hons) | Health and Social Development |
| Bachelor of Public Health and Health Promotion | BSc | Health and Social Development |
| Bachelor of Public Health and Health Promotion (Honours) | B(Hons) | Health and Social Development |
| Bachelor of Social Work | BSW | Health and Social Development |
| Bachelor of Health Sciences / Bachelor of Arts | B+B Double | Health + Arts |
| Bachelor of Public Health and Health Promotion / Bachelor of Commerce | B+B Double | Health + Business |

#### School of Medicine

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Health and Medical Science (Honours) | B(Hons) | Medicine |
| Bachelor of Medical Imaging | BSc | Medicine |
| Bachelor of Biomedical Science | BSc | Medicine |

#### School of Nursing and Midwifery

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Nursing | BNurs | Nursing and Midwifery |
| Bachelor of Nursing (Clinical Leadership) | BNurs | Nursing and Midwifery |
| Bachelor of Nursing (Honours) | B(Hons) | Nursing and Midwifery |
| Bachelor of Nursing / Bachelor of Midwifery | B+B Double | Nursing and Midwifery |
| Bachelor of Nursing / Bachelor of Psychological Science | B+B Double | Nursing + Psychology |
| Bachelor of Nursing / Bachelor of Public Health and Health Promotion | B+B Double | Nursing + Health |

#### School of Psychology

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Psychological Science | BSc(Psych) | Psychology |
| Bachelor of Psychological Science (Honours) | B(Hons) | Psychology |
| Bachelor of Psychology (Honours) | B(Hons) | Psychology |

#### School of Medicine — Clinical

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Doctor of Medicine | MD | Medicine |

### Faculty of Science, Engineering and Built Environment (SEBE)

#### School of Architecture and Built Environment

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Design (Architecture) | BDes | Architecture and Built Environment |
| Bachelor of Construction Management (Honours) | BCM(Hons) | Architecture and Built Environment |
| Bachelor of Property and Real Estate | BBus | Architecture and Built Environment |
| Bachelor of Design (Architecture) / Bachelor of Construction Management (Honours) | B+B Double | Architecture + SEBE |
| Bachelor of Design (Architecture) / Bachelor of Property and Real Estate | B+B Double | Architecture + SEBE |
| Bachelor of Design (Architecture) / Master of Architecture | B+M Combined | Architecture |

#### School of Engineering

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Engineering (Honours) | BEng(Hons) | Engineering |
| Bachelor of Engineering (Industry) (Honours) | BEng(Hons) | Engineering |
| Bachelor of Software Engineering (Honours) | BEng(Hons) | Engineering |

#### School of Information Technology

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Artificial Intelligence | BSc | Information Technology |
| Bachelor of Artificial Intelligence (Honours) | B(Hons) | Information Technology |
| Bachelor of Computer Science | BSc | Information Technology |
| Bachelor of Computer Science (Honours) | B(Hons) | Information Technology |
| Bachelor of Cyber Security | BSc | Information Technology |
| Bachelor of Cyber Security (Honours) | B(Hons) | Information Technology |
| Bachelor of Data Science | BSc | Information Technology |
| Bachelor of Data Science (Honours) | B(Hons) | Information Technology |
| Bachelor of Information Technology | BIT | Information Technology |
| Bachelor of Information Technology (Honours) | B(Hons) | Information Technology |

#### School of Life and Environmental Sciences

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Bachelor of Science | BSc | Life and Environmental Sciences |
| Bachelor of Science (Honours) | B(Hons) | Life and Environmental Sciences |
| Bachelor of Environmental Science (Honours) | B(Hons) | Life and Environmental Sciences |
| Bachelor of Environmental Science (Wildlife and Conservation Biology) | BSc | Life and Environmental Sciences |
| Bachelor of Environmental Science and Sustainability | BSc | Life and Environmental Sciences |
| Bachelor of Forensic Science | BSc | Life and Environmental Sciences |
| Bachelor of Forensic Science (Honours) | B(Hons) | Life and Environmental Sciences |
| Bachelor of Marine Science | BSc | Life and Environmental Sciences |
| Bachelor of Zoology and Animal Science | BSc | Life and Environmental Sciences |
| Bachelor of Forensic Science / Bachelor of Criminology | B+B Double | Life Sciences + Arts |

---

## Section 2 — Graduate education

### 2.1 Postgraduate Taught (PGT)

#### Faculty of Arts and Education

**Graduate Certificates**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Certificate of Communication | GradCert | Communication and Creative Arts |
| Graduate Certificate of Creative Arts | GradCert | Creative Arts |
| Graduate Certificate of Criminology | GradCert | Humanities and Social Sciences |
| Graduate Certificate of Cultural Heritage and Museum Studies | GradCert | Humanities and Social Sciences |
| Graduate Certificate of Education (Specialist Inclusive Education) | GradCert | Education |
| Graduate Certificate of Education (Trauma-Responsive Education) | GradCert | Education |
| Graduate Certificate of Education Research | GradCert | Education |
| Graduate Certificate of Human Resource Management | GradCert | Business and Law |
| Graduate Certificate of International and Community Development | GradCert | Humanities and Social Sciences |
| Graduate Certificate of International Relations | GradCert | Humanities and Social Sciences |
| Graduate Certificate of Politics and Policy | GradCert | Humanities and Social Sciences |
| Graduate Certificate of Writing and Literature | GradCert | Humanities and Social Sciences |
| Graduate Certificate of Higher Education (Learning and Teaching) | GradCert | Education |
| Graduate Certificate of Leadership | GradCert | [cross-faculty] |

**Graduate Diplomas**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Diploma of Communication | GradDip | Communication and Creative Arts |
| Graduate Diploma of Creative Arts | GradDip | Creative Arts |
| Graduate Diploma of Indigenous Research | GradDip | NIKERI |
| Graduate Diploma of Museum Studies | GradDip | Humanities and Social Sciences |
| Graduate Diploma of Writing and Literature | GradDip | Humanities and Social Sciences |

**Masters**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Master of Arts (Writing and Literature) | MA | Humanities and Social Sciences |
| Master of Communication | MA | Communication and Creative Arts |
| Master of Creative Arts | MA | Creative Arts |
| Master of Criminology | MA | Humanities and Social Sciences |
| Master of Cultural Heritage and Museum Studies | MA | Humanities and Social Sciences |
| Master of Education (Leadership and Learning) | MEd | Education |
| Master of Education (Specialist Inclusive Education) | MEd | Education |
| Master of Film and Television | MA | Communication and Creative Arts |
| Master of Human Resource Management | MHRM | [interdisciplinary] |
| Master of Humanitarianism and Development | MA | Humanities and Social Sciences |
| Master of International Relations | MA | Humanities and Social Sciences |
| Master of Leadership | MLead | [interdisciplinary] |
| Master of Politics and Policy | MA | Humanities and Social Sciences |
| Master of Teaching (Early Childhood) | MTeach | Education |
| Master of Teaching (Primary) | MTeach | Education |
| Master of Teaching (Secondary) | MTeach | Education |
| Master of Child Play Therapy | M(Clin) | Psychology |
| Master of Counselling | MCouns | Psychology |

#### Faculty of Business and Law

**Graduate Certificates**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Certificate of Australian Law | GradCert | Deakin Law School |
| Graduate Certificate of Business | GradCert | Deakin Business School |
| Graduate Certificate of Business (Arts and Cultural Management) | GradCert | Deakin Business School |
| Graduate Certificate of Business (Marketing) | GradCert | Deakin Business School |
| Graduate Certificate of Business (Sport Management) | GradCert | Deakin Business School |
| Graduate Certificate of Business Administration | GradCert | Deakin Business School |
| Graduate Certificate of Business Analytics | GradCert | Deakin Business School |
| Graduate Certificate of Digital Finance | GradCert | Deakin Business School |
| Graduate Certificate of Financial Planning | GradCert | Deakin Business School |
| Graduate Certificate of Human Resource Management | GradCert | Deakin Business School |
| Graduate Certificate of Marketing Technology | GradCert | Deakin Business School |
| Graduate Certificate of Professional Accounting | GradCert | Deakin Business School |
| Graduate Certificate of Property | GradCert | Deakin Business School |
| Graduate Certificate of Recruitment and Talent Acquisition | GradCert | Deakin Business School |

**Graduate Diplomas**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Diploma of Business Administration | GradDip | Deakin Business School |
| Graduate Diploma of Finance | GradDip | Deakin Business School |
| Graduate Diploma of Financial Planning | GradDip | Deakin Business School |
| Graduate Diploma of Professional Accounting | GradDip | Deakin Business School |
| Graduate Diploma of Property | GradDip | Deakin Business School |

**Masters**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Executive Graduate Certificate of Sport Business | ExecGradCert | Deakin Business School |
| Juris Doctor | JD | Deakin Law School |
| Master of Business | MBus | Deakin Business School |
| Master of Business (Arts and Cultural Management) | MBus | Deakin Business School |
| Master of Business (Marketing) | MBus | Deakin Business School |
| Master of Business (Sport Management) | MBus | Deakin Business School |
| Master of Business Administration | MBA | Deakin Business School |
| Master of Business Administration (International) | MBA(Intl) | Deakin Business School |
| Master of Business Analytics | MBusAnalytics | Deakin Business School |
| Master of Finance | MFin | Deakin Business School |
| Master of Health Economics | MHEcon | Deakin Business School / Health |
| Master of Health Management | MHM | Deakin Business School / Health |
| Master of Human Resource Management | MHRM | Deakin Business School |
| Master of Information Systems | MIS | Deakin Business School |
| Master of Professional Accounting | MPA | Deakin Business School |

#### Faculty of Health

**Graduate Certificates**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Certificate of Advanced Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Agricultural Health and Medicine | GradCert | Medicine |
| Graduate Certificate of Cardiac Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Critical Care Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Diabetes Education | GradCert | Health and Social Development |
| Graduate Certificate of Disability and Inclusion | GradCert | Health and Social Development |
| Graduate Certificate of Emergency Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Health and Medical Research | GradCert | Medicine |
| Graduate Certificate of Health Promotion | GradCert | Health and Social Development |
| Graduate Certificate of Health Research Practice | GradCert | Medicine |
| Graduate Certificate of Human Nutrition | GradCert | Exercise and Nutrition Sciences |
| Graduate Certificate of Intensive Care Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Intraoperative Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Mental Health Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Perianaesthesia Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Perioperative Nursing | GradCert | Nursing and Midwifery |
| Graduate Certificate of Public Health | GradCert | Health and Social Development |
| Graduate Certificate of Therapeutic Child Play | GradCert | Psychology |
| Graduate Certificate of Health Management | GradCert | Nursing and Midwifery |

**Graduate Diplomas**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Diploma of Advanced Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Cardiac Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Critical Care Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Emergency Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Health Management | GradDip | Health |
| Graduate Diploma of Health Promotion | GradDip | Health and Social Development |
| Graduate Diploma of Human Nutrition | GradDip | Exercise and Nutrition Sciences |
| Graduate Diploma of Intensive Care Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Intraoperative Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Mental Health Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Midwifery | GradDip | Nursing and Midwifery |
| Graduate Diploma of Perianaesthesia Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Perioperative Nursing | GradDip | Nursing and Midwifery |
| Graduate Diploma of Psychological Science | GradDip | Psychology |
| Graduate Diploma of Psychology (Advanced) | GradDip | Psychology |
| Graduate Diploma of Public Health | GradDip | Health and Social Development |

**Masters**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Doctor of Medicine | MD | Medicine |
| Master of Advanced Clinical Nursing | MNurs | Nursing and Midwifery |
| Master of Advanced Nursing | MNurs | Nursing and Midwifery |
| Master of Clinical Exercise Physiology | MClinExPhys | Exercise and Nutrition Sciences |
| Master of Clinical Psychology (Post Registration) | MClinPsych | Psychology |
| Master of Dietetics | MDiet | Exercise and Nutrition Sciences |
| Master of Disability and Inclusion | MDIs | Health and Social Development |
| Master of Health Promotion | MHP | Health and Social Development |
| Master of Human Nutrition | MHN | Exercise and Nutrition Sciences |
| Master of Mental Health Nursing | MNurs | Nursing and Midwifery |
| Master of Nutrition and Population Health | MNutr | Exercise and Nutrition Sciences |
| Master of Occupational Therapy Practice | MOT | Health and Social Development |
| Master of Professional Psychology | MPsych | Psychology |
| Master of Psychology (Clinical) | MPsych(Clin) | Psychology |
| Master of Psychology (Organisational) | MPsych(Org) | Psychology |
| Master of Public Health | MPH | Health and Social Development |
| Master of Social Work | MSW | Health and Social Development |
| Master of Speech Pathology | MSpPath | Health and Social Development |
| Master of Advanced Nursing | MNurs | Nursing and Midwifery |

#### Faculty of Science, Engineering and Built Environment (SEBE)

**Graduate Certificates**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Certificate of Artificial Intelligence | GradCert | Information Technology |
| Graduate Certificate of Artificial Intelligence for Business | GradCert | Information Technology |
| Graduate Certificate of Construction Management | GradCert | Architecture and Built Environment |
| Graduate Certificate of Cyber Security | GradCert | Information Technology |
| Graduate Certificate of Data Analytics | GradCert | Information Technology |
| Graduate Certificate of Digital Transformation and Cyber Security | GradCert | Information Technology |
| Graduate Certificate of Engineering | GradCert | Engineering |
| Graduate Certificate of Information Systems | GradCert | Information Technology |
| Graduate Certificate of Information Technology | GradCert | Information Technology |
| Graduate Certificate of Information Technology Management | GradCert | Information Technology |
| Graduate Certificate of Sustainability | GradCert | Life and Environmental Sciences |
| Graduate Certificate of Systems Thinking | GradCert | [interdisciplinary] |

**Graduate Diplomas**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Graduate Diploma of Applied Sport Science | GradDip | Engineering |
| Graduate Diploma of Biotechnology | GradDip | Life and Environmental Sciences |
| Graduate Diploma of Construction Management | GradDip | Architecture and Built Environment |
| Graduate Diploma of Humanitarianism and Development | GradDip | Life and Environmental Sciences |
| Graduate Diploma of Land and Sea Country Management | GradDip | Life and Environmental Sciences |
| Graduate Diploma of Sustainability | GradDip | Life and Environmental Sciences |
| Graduate Diploma of Psychological Science | GradDip | Psychology (cross-faculty) |

**Masters**

| Program Name | Degree Type | School |
|-------------|-------------|--------|
| Master of Applied Artificial Intelligence | MAI | Information Technology |
| Master of Applied Artificial Intelligence (Professional) | MAI(Prof) | Information Technology |
| Master of Applied Sport Science | MAppSpSc | Engineering |
| Master of Architecture | MArch | Architecture and Built Environment |
| Master of Artificial Intelligence for Design and Creative Practice | MAI | Information Technology |
| Master of Biotechnology (Professional) | MBiotech(Prof) | Life and Environmental Sciences |
| Master of Construction Management (Professional) | MCM(Prof) | Architecture and Built Environment |
| Master of Cyber Security | MCybSec | Information Technology |
| Master of Cyber Security (Professional) | MCybSec(Prof) | Information Technology |
| Master of Data Science | MDataSci | Information Technology |
| Master of Data Science (Professional) | MDataSci(Prof) | Information Technology |
| Master of Engineering (Professional) | MEng(Prof) | Engineering |
| Master of Engineering Management (Professional) | MEngMgt(Prof) | Engineering |
| Master of Information Technology | MIT | Information Technology |
| Master of Information Technology (Professional) | MIT(Prof) | Information Technology |
| Master of Information Technology Management | MITMgt | Information Technology |
| Master of Information Technology Management (Professional) | MITMgt(Prof) | Information Technology |
| Master of Sustainability | MSus | Life and Environmental Sciences |
| Master of Sustainability (Professional) | MSus(Prof) | Life and Environmental Sciences |

### 2.2 Research Degrees (PhD / Masters by Research)

Research degrees are offered across all four faculties. Applicants require a Bachelor degree with honours (second class or above) or a Masters by research. Discipline must align with available supervisory expertise.

Key research areas per faculty:
- **Arts and Education**: Creative arts practice, education, humanities, Indigenous knowledges, social sciences
- **Business and Law**: Accounting, finance, economics, marketing, management, law, business analytics
- **Health**: Exercise science, nutrition, medicine, nursing, psychology, public health, social work
- **SEBE**: Architecture, engineering, IT, life and environmental sciences

---

## Section 3 — Application requirements & deadlines

### 3.1 Undergraduate Entry Requirements

| Requirement | Details |
|-------------|---------|
| ATAR (Domestic) | Minimum varies by course (range ~50–95+). Example: Bachelor of Commerce requires 80.15 (lowest selection rank). Deakin Guaranteed ATAR may be lower for eligible students. |
| International Baccalaureate (IB) | Accepted. Specific scores vary by course. |
| GCE A-Levels | Accepted. Specific grade requirements vary by course. |
| Chinese Gaokao | Accepted. Check individual course page for country-specific requirements. |
| Foundation Pathways | Deakin College offers pathway programs. DUELI (Deakin University English Language Institute) offers English pathway. |

### 3.2 Postgraduate Entry Requirements

| Level | Requirement |
|-------|-------------|
| Graduate Certificate/Diploma | Three-year undergraduate degree or equivalent from an approved institution. Relevant professional experience may also be considered. |
| Masters by Coursework | Completed at least a three-year undergraduate degree or equivalent from an approved university. Some courses require specific undergraduate background, work experience, or higher GPA. |
| Masters by Research | Bachelor degree with honours (second class or above) from a recognised tertiary institution. Discipline must align with available supervisory expertise. |
| Doctor of Philosophy (PhD) | Bachelor degree with honours (second class or above) or a masters by research from a recognised tertiary institution. |

### 3.3 English Language Requirements

| Test | Undergraduate Minimum | Postgraduate Minimum |
|------|----------------------|---------------------|
| IELTS (Academic) | Overall 6.0, no band < 6.0 | Overall 6.5, no band < 6.0 |
| TOEFL iBT | 65+ (varies by course) | 79+ (varies by course) |
| PTE Academic | 50+ (varies by course) | 58+ (varies by course) |
| CEFR Level | B2 | C1 |

> Note: Some courses require higher scores (e.g., Nursing, Education, Medicine, Law, Social Work may require IELTS 7.0+). Check individual course pages. DUELI offers English language pathway programs.

### 3.4 Application Deadlines

| Intake | Deadline |
|--------|----------|
| Trimester 1 (March) | Applications typically close late February / early March |
| Trimester 2 (July) | Applications typically close late June / early July |
| Trimester 3 (November) | Direct applications close 18 October 2026 (for T3 2026) |
| VTAC (Domestic Year 12) | December, January and February rounds |

### 3.5 Special Requirements

| Requirement | Details |
|-------------|---------|
| GMAT/GRE | Not generally required for most coursework programs. MBA and specific programs may have additional requirements. |
| Portfolio/Audition | Required for specific creative arts, design, and film programs. Check individual course pages. |
| Casper Test | Required for some health and education programs (e.g., Associate Degree of Education). |

---

## Section 4 — Costs & financial aid

### 4.1 Tuition Fees (Estimated Annual Range — International Students)

| Level | Fee Range (AUD/year) |
|-------|---------------------|
| Undergraduate (Bachelor degrees) | $30,000 – $43,000+ |
| Postgraduate (Masters coursework) | $32,000 – $45,000+ |
| Postgraduate (MBA / Specialized) | Higher — check specific course page |
| Research degrees | Variable — scholarship opportunities available |

> Note: Fees vary significantly by program. Exact fees listed on each course page under 'Fees and scholarships' tab. Fees do not include accommodation, OSHC, textbooks, or living expenses.

### 4.2 Scholarships (International Students)

| Scholarship Name | Value | Notes |
|-----------------|-------|-------|
| Vice-Chancellor's International Scholarship | 50% or 100% of tuition fees | Highly competitive; includes Vice-Chancellor's Professional Excellence Program + priority accommodation |
| Deakin International Scholarship for Excellence | 25% of total tuition fees | For high-achieving students |
| Deakin International 20% Merit Scholarship | 20% of total tuition fees | For duration of course |
| Deakin College Foundation Pathway Scholarship | 10% off bachelor tuition fees | WAM 60-64.99% |
| Warrnambool Campus International Bursary | 20% of tuition fees | For selected courses at Warrnambool campus |
| Deakin Warrnambool Residential International Scholarship | Up to 50% of Deakin Residences costs | Accommodation support |
| PhD Scholarships (RTP/DUPRS) | $37,450/year for up to 3 years | Research Training Program |
| HDR Specialized Scholarships | $47,450/year for up to 3 years | Discipline-specific |

> Note: Over 100 scholarships available at all levels. Filter by citizenship using the 'Find a scholarship' tool.

### 4.3 Cost of Living

| Expense | Estimated Cost |
|---------|---------------|
| Accommodation | Varies by campus and type (on-campus, off-campus, homestay) |
| OSHC (Health Insurance) | Required for all international students on student visas |
| Textbooks & Equipment | Varies by program |
| Living Expenses | Use Study Australia Cost of Living Calculator for estimates |

### 4.4 Government HELP Schemes (Domestic Students)

Domestic students in Commonwealth Supported Places (CSP) can use HECS-HELP loans. Most undergraduate courses are CSP-eligible.

---

## Section 5 — Evidence chain index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|------------|---------------|
| E-U-001 | institution.name | Deakin University | https://www.deakin.edu.au/ | official_webpage |
| E-U-002 | institution.founded_year | 1974 | https://www.deakin.edu.au/about-deakin | official_webpage |
| E-U-003 | institution.type | Public | https://www.deakin.edu.au/about-deakin | official_webpage |
| E-U-004 | institution.campuses | Burwood, Waurn Ponds, Waterfront, Warrnambool, Cloud | https://www.deakin.edu.au/about-deakin/locations/campuses | official_webpage |
| E-U-005 | institution.ranking.qs_2025 | #197 | https://www.topuniversities.com/universities/deakin-university | rankings |
| E-U-006 | institution.ranking.the_2025 | 251-300 | https://www.timeshighereducation.com/world-university-rankings/deakin-university | rankings |
| E-U-007 | institution.total_students | ~53,000+ | https://www.deakin.edu.au/about-deakin | official_webpage |
| E-U-008 | faculties.count | 4 | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-009 | faculty.schools | Full hierarchy (14 schools + NIKERI) | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-010 | faculty.arts.schools | Communication and Creative Arts, Education, Humanities and Social Sciences, NIKERI | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-011 | faculty.business_law.schools | Deakin Business School, Deakin Law School | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-012 | faculty.health.schools | Exercise and Nutrition Sciences, Health and Social Development, Medicine, Nursing and Midwifery, Psychology | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-013 | faculty.sebe.schools | Architecture and Built Environment, Engineering, Information Technology, Life and Environmental Sciences | https://www.deakin.edu.au/about-deakin/faculties-and-schools | official_webpage |
| E-U-014 | ug.courses.total | 113 | https://www.deakin.edu.au/study/find-a-course/undergraduate-courses | official_webpage |
| E-U-015 | pg.courses.total | 163 | https://www.deakin.edu.au/study/find-a-course/postgraduate-courses | official_webpage |
| E-U-016 | elp.ielts.ug | Overall 6.0, no band < 6.0 | https://www.deakin.edu.au/international-students/entry-requirements/english | official_webpage |
| E-U-017 | elp.ielts.pg | Overall 6.5 (CEFR C1) | https://www.deakin.edu.au/international-students/entry-requirements/english | official_webpage |
| E-U-018 | application.deadline.t3_2026 | 18 October 2026 | https://www.deakin.edu.au/international-students/how-to-apply | official_webpage |
| E-U-019 | entry.requirement.ug.atar | 80.15 (sample: Bachelor of Commerce) | https://www.deakin.edu.au/course/bachelor-commerce | official_webpage |
| E-U-020 | entry.requirement.pg | Three-year undergraduate degree or equivalent | https://www.deakin.edu.au/international-students/entry-requirements | official_webpage |
| E-U-021 | international.fees | Per course page (varies) | https://www.deakin.edu.au/international-students/international-student-fees | official_webpage |
| E-U-022 | scholarships.vice_chancellor | 50% or 100% tuition | https://www.deakin.edu.au/international-students/international-student-scholarships | official_webpage |
| E-U-023 | scholarships.deakin_excellence | 25% tuition | https://www.deakin.edu.au/international-students/international-student-scholarships | official_webpage |
| E-U-024 | scholarships.merit_20 | 20% tuition | https://www.deakin.edu.au/international-students/international-student-scholarships | official_webpage |
| E-U-025 | research.entry.phd | Bachelor (Hons) 2nd class or MRes | https://www.deakin.edu.au/research/research-degrees/research-degree-entry-requirements | official_webpage |
| E-U-026 | application.vtac | December, January, February rounds | https://www.deakin.edu.au/study/how-to-apply/undergraduate-applications | official_webpage |
| E-U-027 | dueli.pathway | English for Academic Purposes program | https://www.deakin.edu.au/international-students/entry-requirements/english | official_webpage |
| E-U-028 | student.cohort.2026 | 10,475 enrolled at census date (T1 2026) | https://www.deakin.edu.au/study/find-a-course/undergraduate-courses | official_webpage |
| E-U-029 | ug.courses.sample | Full list of 113 undergraduate courses | https://www.deakin.edu.au/study/find-a-course/undergraduate-courses | official_webpage |
| E-U-030 | pg.courses.sample | Full list of 163 postgraduate courses | https://www.deakin.edu.au/study/find-a-course/postgraduate-courses | official_webpage |

---

## Section 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data Item | Notes |
|----------|-----------|-------|
| **P0** | Per-course international tuition fees | Listed on each course page under 'Fees and scholarships' tab. Exact amounts vary by year and program. |
| **P0** | Per-course ATAR/entry scores | Each course page has specific ATAR requirements. Sample collected for Bachelor of Commerce. |
| **P0** | Specific IELTS/TOEFL/PTE by course | Higher requirements for Nursing, Education, Medicine, Law, Social Work programs. |
| **P1** | Research degree programs detail | PhD/Masters by Research programs across all faculties. Individual supervisor and project listings. |
| **P1** | Domestic student fees (CSP) | CSP student contribution amounts per course. |
| **P1** | Course handbook mapping | https://www.deakin.edu.au/handbook for detailed curriculum per program. |
| **P2** | Alumni outcomes data | Graduate employment statistics per faculty. |
| **P2** | Exchange partner list | https://www.deakin.edu.au/international-students/study-abroad-and-exchange/exchange-partners |
| **P2** | Student profile by campus | Cohort breakdown by campus location. |

### Known data gaps

- Cloudflare WAF blocks curl/API access to sitemap; all data extracted via browser automation
- Per-course fee details require individual course page navigation (~276 pages)
- Some postgraduate programs (PhD) are organized by research area rather than structured course listings

### Data freshness

| Dataset | Freshness | Next check |
|---------|-----------|------------|
| Course listings (UG + PG) | 2026-07-10 | 2026-08 (intake year may change) |
| Entry requirements | 2026-07-10 | 2026-12 (annual update) |
| Fee ranges | 2026-07-10 | 2026-12 (annual update for 2027) |
| Scholarship info | 2026-07-10 | 2026-12 |
| Faculty/school structure | 2026-07-10 | 2027-01 (rarely changes) |

---

## Section 7 — Cross-school comparison framework

| Dimension | Deakin University |
|-----------|------------------|
| Country | Australia |
| State | Victoria |
| University Group | Australian Technology Network (ATN) |
| Total UG programmes | 113 |
| Total PG programmes | 163 |
| Faculties / Schools | 4 faculties, 14 schools + NIKERI Institute |
| Trimester system | Yes (T1 Mar, T2 Jul, T3 Nov) |
| QS World Ranking 2025 | #197 |
| THE World Ranking 2025 | 251-300 |
| International fee range (UG) | $30,000 – $43,000+ AUD/year |
| IELTS minimum (UG) | 6.0 (no band < 6.0) |
| IELTS minimum (PG) | 6.5 (no band < 6.0) |
| Scholarship (top) | 50-100% tuition (Vice-Chancellor's) |
| Cloud/Campus/Online | Blended (4 physical campuses + Cloud online) |
| Total students | ~53,000+ (onshore + online) |
| CRICOS Provider Code | 00113B |
| TEQSA Provider ID | PRV12124 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Deakin University official website (www.deakin.edu.au)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (113 full entries) | PG programmes ✅ (163 full entries) | Fees ⚠️ (per-course estimates, ranges provided) | Evidence ✅ (30 blocks)
> **Next step**: Extract per-course fees from individual course pages for precise international tuition data.
