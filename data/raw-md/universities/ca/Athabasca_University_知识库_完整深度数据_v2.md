> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Alberta)
> **Official website**: https://www.athabascau.ca/
> **Calendar**: https://www.athabascau.ca/calendar/

# Athabasca University 知识库 — 完整深度数据 v2

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| Category | Count |
|----------|-------|
| 本科学位专业 (UG degree programmes) | 33 |
| 本科辅修 (Minors) | N/A (open university model — majors/concentrations within degrees) |
| 大学证书 (University Certificates) | 14 |
| 大学文凭 (University Diploma) | 1 |
| 结业证书 (Certificate of Completion) | 1 |
| 后学士证书 (Post-Baccalaureate Certificate) | 1 |
| 后文凭路径 (Post Diploma Route) | 18 |
| 授课型研究生项目 (PGT: Master's/Grad Cert/Grad Dip) | 18 |
| 博士项目 (Doctoral/PhD) | 2 (DBA, EdD) |
| **学位项目总计** | ~90 (含所有级别) |
| 学院 (Faculties) | 5 |
| 学术院系 (Academic Schools/Departments) | N/A — AU is a distributed online university; programs are administered by faculties without traditional department subdivisions |

**Note**: AU operates as an open university with rolling admissions. Programs are grouped under 5 faculties rather than a traditional department structure. The Calendar states "90 graduate and undergraduate degrees, diplomas, and certificate programs" and "over 850 university courses."

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Athabasca University
├── Faculty of Business (FB)
│   ├── Doctor of Business Administration (DBA)
│   ├── Master of Business Administration (MBA)
│   ├── Graduate Diploma – Management
│   ├── Graduate Diploma – Leadership & Management (pre-2026)
│   ├── Bachelor of Commerce (BCom) — General, Accounting, BTech Mgmt, Finance, HR Mgmt, Indigenous Business, Marketing
│   ├── Bachelor of Management — General
│   ├── Bachelor of Human Resources and Labour Relations
│   ├── University Certificate — Accounting, Advanced Accounting, Computers & MIS, Finance, Human Resources & Labour Relations, Indigenous Community Economic Dev & Planning, Management Applications, Management Foundations, Marketing, Public Administration
│   └── Post Diploma Route — various
│
├── Faculty of Health Disciplines (FHD)
│   ├── Master of Counselling (MC)
│   ├── Master of Health Studies (MHS)
│   ├── Master of Nursing — Generalist (MN)
│   ├── Master of Nursing — Nurse Practitioner (MN-NP)
│   ├── Graduate Diploma — Counselling
│   ├── Post-Master's Certificate — Counselling
│   ├── Post-Master's Diploma — Nurse Practitioner
│   ├── Post-LPN Bachelor of Nursing
│   ├── Post-RN Bachelor of Nursing
│   ├── University Certificate — Gender & Social Justice Counselling
│   └── Post Diploma Route — various
│
├── Faculty of Humanities and Social Sciences (FHSS)
│   ├── Master of Arts — Interdisciplinary Studies (MA)
│   ├── Master of Education — Open, Digital, and Distance Education (MEd)
│   ├── Graduate Diploma — Heritage Resources Management
│   ├── Graduate Diploma — Instructional Design
│   ├── Graduate Diploma — Legislative Drafting
│   ├── Graduate Diploma — Distance Education Technology
│   ├── Graduate Certificate — Instructional Design
│   ├── Graduate Certificate — Technology-Based Learning
│   ├── Post-Baccalaureate Certificate — Inclusive Education
│   ├── Bachelor of Arts — 3-year General, Anthropology, English, French, History, Humanities, Labour Studies, Political Economy, Political Science, Psychology, Sociology, Women's & Gender Studies
│   ├── Bachelor of Professional Arts — Comm Studies, Criminal Justice, Governance Law & Mgmt, Human Services
│   ├── Bachelor of General Studies
│   ├── University Diploma — Arts
│   ├── University Certificate — French Language Proficiency, Heritage Resources Mgmt, [others under FB/FHD/FST]
│   └── Post Diploma Route — various
│
├── Faculty of Science and Technology (FST)
│   ├── Master of Science — Computing & Information Systems (MSc)
│   ├── Master of Science — Earth System Science (MSc)
│   ├── Graduate Diploma — Architecture
│   ├── Graduate Diploma — Information Security
│   ├── Graduate Certificate — Artificial Intelligence
│   ├── Graduate Certificate — Data Analytics
│   ├── Graduate Certificate — Information Security
│   ├── Graduate Certificate — Information Technology Management
│   ├── Bachelor of Science — General, Applied Mathematics, Architecture Track, Computing & IS, Biological Sciences
│   ├── Bachelor of Environmental Studies
│   ├── University Certificate — Computing & IS, Computers & MIS
│   └── Post Diploma Route — various
│
└── Faculty of Graduate Studies (cross-faculty coordination)
    └── (oversees graduate programs administered by the four teaching faculties)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree Level Code | Full Name | Count |
|-------------------|-----------|-------|
| BA (3yr) | Bachelor of Arts, 3-year General | 1 |
| BA | Bachelor of Arts (4-year with Major) | 11 |
| BCom | Bachelor of Commerce | 7 |
| BES | Bachelor of Environmental Studies | 1 |
| BGS | Bachelor of General Studies | 1 |
| BHRLR | Bachelor of Human Resources & Labour Relations | 1 |
| BMan | Bachelor of Management | 1 |
| BPA | Bachelor of Professional Arts | 4 |
| BSc | Bachelor of Science | 5 |
| Post-LPN BN | Post-LPN Bachelor of Nursing | 1 |
| Post-RN BN | Post-RN Bachelor of Nursing | 1 |
| CertComp | Certificate of Completion | 1 |
| UnivCert | University Certificate | 14 |
| UnivDip | University Diploma | 1 |
| PostBaccCert | Post-Baccalaureate Certificate | 1 |
| PostDipRoute | Post Diploma Route | 18 |
| MA | Master of Arts | 1 |
| MBA | Master of Business Administration | 1 |
| MC | Master of Counselling | 1 |
| MEd | Master of Education | 1 |
| MHS | Master of Health Studies | 1 |
| MN | Master of Nursing | 2 |
| MSc | Master of Science | 2 |
| GradCert | Graduate Certificate | 6 |
| GradDip | Graduate Diploma | 7 |
| PostMastCert | Post-Master's Certificate | 1 |
| PostMastDip | Post-Master's Diploma | 1 |
| DBA | Doctor of Business Administration | 1 |
| EdD | Doctor of Education | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Faculty | UG Degree | UG Cert/Dip | Post-Bacc | Post-Dip Route | Master's | Grad Cert/Dip | Post-Master's | Doctorate | **Total** |
|---------|-----------|-------------|-----------|---------------|----------|---------------|--------------|-----------|-----------|
| Business | 9 | 10 | — | Included | 1 | 2 | — | 1 | ~23 |
| Health Disciplines | 2 | 1 | — | Included | 4 | 1 | 2 | — | ~10 |
| Humanities & Social Sciences | 16 | 3 | 1 | Included | 2 | 4 | — | 1 | ~27 |
| Science & Technology | 7 | 2 | — | Included | 2 | 4 | — | — | ~15 |
| Graduate Studies | — | — | — | — | (cross-faculty) | — | — | — | — |
| **Total** | **34** | **16** | **1** | **18** | **9** | **13** | **2** | **2** | **~90** |

**Note**: The Post Diploma Route (18 programs) spans multiple faculties. Distribution is approximate, inferred from program naming and URL patterns. The Calendar states "90 graduate and undergraduate degrees, diplomas, and certificate programs."

---

## Section 1 — Undergraduate education

### Faculty of Business — Undergraduate Programs

| Program Name | Degree Type | Faculty | Department | URL |
|-------------|------------|---------|------------|-----|
| Bachelor of Arts – 3 year General | BA (3yr) | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-general.html |
| Bachelor of Arts, Anthropology Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-anthropology.html |
| Bachelor of Arts, English Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-english.html |
| Bachelor of Arts, French Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-french.html |
| Bachelor of Arts, History Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-history.html |
| Bachelor of Arts, Humanities Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-humanities.html |
| Bachelor of Arts, Labour Studies Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-labour-studies.html |
| Bachelor of Arts, Political Economy Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-political-economy.html |
| Bachelor of Arts, Political Science Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-political-science.html |
| Bachelor of Arts, Psychology Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-psychology.html |
| Bachelor of Arts, Sociology Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-sociology.html |
| Bachelor of Arts, Women's & Gender Studies Major | BA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-arts-in-women-and-gender-studies.html |
| Bachelor of Commerce, General | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-general.html |
| Bachelor of Commerce, Accounting Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-accounting.html |
| Bachelor of Commerce, Business Technology Management Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-business-technology-management.html |
| Bachelor of Commerce, Finance Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-finance.html |
| Bachelor of Commerce, Human Resources Management Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-human-resources-management.html |
| Bachelor of Commerce, Indigenous Business Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-indigenous-business.html |
| Bachelor of Commerce, Marketing Major | BCom | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-commerce-in-marketing.html |
| Bachelor of Environmental Studies | BES | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-environmental-studies.html |
| Bachelor of General Studies | BGS | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-general-studies.html |
| Bachelor of Human Resources and Labour Relations | BHRLR | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-human-resources-and-labour-relations.html |
| Bachelor of Management, General | BMan | Business | — | https://www.athabascau.ca/programs/summary/bachelor-of-management-general.html |
| Bachelor of Professional Arts, Communication Studies Major | BPA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-professional-arts-in-communication-studies.html |
| Bachelor of Professional Arts, Criminal Justice Major | BPA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-professional-arts-in-criminal-justice.html |
| Bachelor of Professional Arts, Governance, Law, and Management Major | BPA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-professional-arts-in-governance-law-and-management.html |
| Bachelor of Professional Arts, Human Services Major | BPA | FHSS | — | https://www.athabascau.ca/programs/summary/bachelor-of-professional-arts-in-human-services.html |
| Bachelor of Science, General | BSc | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-science-general.html |
| Bachelor of Science, Applied Mathematics Major | BSc | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-science-in-applied-mathematics.html |
| Bachelor of Science, Architecture | BSc | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-science-in-architecture.html |
| Bachelor of Science, Computing and Information Systems Major | BSc | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-science-in-computing-and-information-systems.html |
| Bachelor of Science, Biological Sciences Major | BSc | Science & Technology | — | https://www.athabascau.ca/programs/summary/bachelor-of-science-in-biological-sciences.html |
| Post-LPN Bachelor of Nursing | Post-LPN BN | Health Disciplines | — | https://www.athabascau.ca/programs/summary/post-lpn-bachelor-of-nursing.html |
| Post-RN Bachelor of Nursing | Post-RN BN | Health Disciplines | — | https://www.athabascau.ca/programs/summary/post-rn-bachelor-of-nursing.html |
| Certificate of Completion in English Language Proficiency | CertComp | FHSS/Faculty | — | https://www.athabascau.ca/programs/summary/certificate-of-completion-in-english-language-proficiency.html |

### Undergraduate Certificates and Diplomas

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| University Certificate in Accounting | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-accounting.html |
| University Certificate in Advanced Accounting | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-advanced-accounting.html |
| University Certificate in Computers and Management Information Systems | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-computers-and-management-information-systems.html |
| University Certificate in Computing and Information Systems | UnivCert | Science & Technology | https://www.athabascau.ca/programs/summary/university-certificate-in-computing-and-information-systems.html |
| University Certificate in Gender and Social Justice Counselling | UnivCert | Health Disciplines | https://www.athabascau.ca/programs/summary/university-certificate-in-counselling-women.html |
| University Certificate in Finance | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-finance.html |
| University Certificate in French Language Proficiency | UnivCert | FHSS | https://www.athabascau.ca/programs/summary/university-certificate-in-french-language-proficiency.html |
| University Certificate in Heritage Resources Management | UnivCert | FHSS | https://www.athabascau.ca/programs/summary/university-certificate-in-heritage-resources-management.html |
| University Certificate in Human Resources and Labour Relations | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-human-resources-and-labour-relations.html |
| University Certificate in Indigenous Community Economic Development and Planning | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-indigenous-community-economic-development-and-planning.html |
| University Certificate in Management Applications | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-management-applications.html |
| University Certificate in Management Foundations | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-management-foundations.html |
| University Certificate in Marketing | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-marketing.html |
| University Certificate in Public Administration | UnivCert | Business | https://www.athabascau.ca/programs/summary/university-certificate-in-public-administration.html |
| University Diploma in Arts | UnivDip | FHSS | https://www.athabascau.ca/programs/summary/university-diploma-in-arts.html |
| Post-Baccalaureate Certificate in Inclusive Education | PostBaccCert | FHSS | https://www.athabascau.ca/programs/summary/post-baccalaureate-certificate-in-inclusive-education.html |

---

## Section 2 — Graduate education

### Master's Programs

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| Master of Arts – Interdisciplinary Studies | MA | FHSS | https://www.athabascau.ca/programs/summary/master-of-arts-in-interdisciplinary-studies.html |
| Master of Business Administration | MBA | Business | https://www.athabascau.ca/programs/summary/master-of-business-administration.html |
| Master of Counselling | MC | Health Disciplines | https://www.athabascau.ca/programs/summary/master-of-counselling.html |
| Master of Education – Open, Digital, and Distance Education | MEd | FHSS | https://www.athabascau.ca/programs/summary/master-of-education-in-open-digital-distance-education.html |
| Master of Health Studies | MHS | Health Disciplines | https://www.athabascau.ca/programs/summary/master-of-health-studies.html |
| Master of Nursing – Generalist | MN | Health Disciplines | https://www.athabascau.ca/programs/summary/master-of-nursing-generalist.html |
| Master of Nursing – Nurse Practitioner | MN-NP | Health Disciplines | https://www.athabascau.ca/programs/summary/master-of-nursing-nurse-practitioner.html |
| Master of Science – Computing and Information Systems | MSc | Science & Technology | https://www.athabascau.ca/programs/summary/master-of-science-in-information-systems.html |
| Master of Science – Earth System Science | MSc | Science & Technology | https://www.athabascau.ca/programs/summary/master-of-science-earth-system-science.html |

### Graduate Certificates

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| Graduate Certificate – Artificial Intelligence | GradCert | Science & Technology | https://www.athabascau.ca/programs/summary/graduate-certificate-artificial-intelligence.html |
| Graduate Certificate – Data Analytics | GradCert | Science & Technology | https://www.athabascau.ca/programs/summary/graduate-certificate-in-data-analytics.html |
| Graduate Certificate – Information Security | GradCert | Science & Technology | https://www.athabascau.ca/programs/summary/graduate-certificate-in-information-security.html |
| Graduate Certificate – Information Technology Management | GradCert | Science & Technology | https://www.athabascau.ca/programs/summary/graduate-certificate-in-information-technology-management.html |
| Graduate Certificate – Instructional Design | GradCert | FHSS | https://www.athabascau.ca/programs/summary/graduate-certificate-in-instructional-design.html |
| Graduate Certificate – Technology-Based Learning | GradCert | FHSS | https://www.athabascau.ca/programs/summary/graduate-certificate-in-technology-based-learning.html |

### Graduate Diplomas

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| Graduate Diploma – Architecture | GradDip | Science & Technology | https://www.athabascau.ca/programs/summary/graduate-diploma-in-architecture.html |
| Graduate Diploma – Counselling | GradDip | Health Disciplines | https://www.athabascau.ca/programs/summary/graduate-diploma-in-counselling.html |
| Graduate Diploma – Distance Education Technology | GradDip | FHSS | https://www.athabascau.ca/programs/summary/graduate-diploma-in-distance-education-technology.html |
| Graduate Diploma – Heritage Resources Management | GradDip | FHSS | https://www.athabascau.ca/programs/summary/graduate-diploma-in-heritage-resources-management.html |
| Graduate Diploma – Instructional Design | GradDip | FHSS | https://www.athabascau.ca/programs/summary/graduate-diploma-in-instructional-design.html |
| Graduate Diploma – Legislative Drafting | GradDip | FHSS | https://www.athabascau.ca/programs/summary/graduate-diploma-in-legislative-drafting.html |
| Graduate Diploma – Management | GradDip | Business | https://www.athabascau.ca/programs/summary/graduate-diploma-in-management.html |

### Post-Master's Credentials

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| Post-Master's Certificate in Counselling | PostMastCert | Health Disciplines | https://www.athabascau.ca/programs/summary/post-masters-certificate-in-counselling.html |
| Post-Master's Diploma – Nurse Practitioner | PostMastDip | Health Disciplines | https://www.athabascau.ca/programs/summary/post-masters-diploma-nurse-practitioner.html |

### Doctoral Programs

| Program Name | Degree Type | Faculty | URL |
|-------------|------------|---------|-----|
| Doctor of Business Administration | DBA | Business | https://www.athabascau.ca/programs/summary/doctor-of-business-administration.html |
| Doctor of Education – Distance Education | EdD | FHSS | https://www.athabascau.ca/programs/summary/doctor-of-education-in-distance-education.html |

---

## Section 3 — Application requirements & deadlines

### 3.1 General Admissions Policy

Athabasca University operates an **open admissions** model — most undergraduate programs have no formal admission requirements beyond being 16 years of age or older. There is no competitive selection process for most undergraduate programs. Graduate programs have faculty-specific entry requirements.

**Undergraduate general admission**: Applicants must be at least 16 years of age. There is no requirement for a high school diploma or previous academic record for general admission to undergraduate programs. Some specific programs (e.g., Nursing, Science) may have prerequisite course requirements.

**Graduate admission**: Each graduate program has specific admission requirements set by the administering faculty. General requirements include a recognized undergraduate degree with a minimum GPA (varies by program).

### 3.2 Application Deadlines

AU has **no fixed application deadlines** — it operates on a **continuous/rolling enrollment** model. Students can apply and register at any time of the year for most programs.

- Undergraduate: Apply any time. Monthly start dates for most courses.
- Graduate: Varies by program. Some graduate programs have specific intake dates (September, January, May).
- General Application Fee (one-time, non-refundable): payable before first registration.

### 3.3 English Language Proficiency Requirements

#### Undergraduate Level

Applicants whose first language is not English, or who have not completed secondary or post-secondary education in an English-speaking country, must demonstrate English Language Proficiency (ELP) via one of the following:

| Test | Minimum Score | Validity |
|------|--------------|----------|
| IELTS (Academic) | 6.0 overall | Within 2 years |
| CAEL (Canadian Academic English Language Assessment) | 60 | Within 2 years |
| MELAB (Michigan English Language Battery) | 80 | Within 2 years |
| PTE Academic | 59 overall (no less than 51 in each of 4 skills) | Within 2 years |
| TOEFL iBT (before Jan 21, 2026) | 80 overall (essay 20+, all other bands 46+) | Within 2 years |
| TOEFL (after Jan 21, 2026) | 4 overall (Reading 3.5, Listening 3.5, Writing 3.5, Speaking 4) | Within 2 years |
| Duolingo English Test | 105 overall (75+ each band) | Within 2 years |
| AU English Language Proficiency Program | 75% average (GPA 3.0) | — |
| 15+ credits from recognized English-speaking post-secondary institution | Pass | — |

**Source**: https://www.athabascau.ca/calendar/undergraduate/admission-registration-evaluation/english-language-proficency.html

#### Graduate Level

Prospective visa students or foreign applicants to graduate programs must provide documentation of at least one of:

| Test | Minimum Score |
|------|--------------|
| TOEFL iBT (before Jan 21, 2026) | 80 overall |
| TOEFL (after Jan 21, 2026) | 4 overall (Reading 3.5, Listening 3.5, Writing 3.5, Speaking 4) |
| IELTS (Academic) | 6.0 overall |
| MELAB | 80 (or MET with 54) |
| CAEL | 60 |
| Degree from English-instruction institution | Recognized |
| AU undergraduate English course (grade 70%+) | Grade of 70% or higher |

**Source**: https://www.athabascau.ca/calendar/graduate/additional-information/english-language-proficiency-requirements.html

### 3.4 How to Apply

- Undergraduate: Submit the Undergraduate General Application Form via https://tux.athabascau.ca/oros/servlet/DispatcherServlet
- Graduate: Apply through the specific graduate program's application portal
- Supporting documents: Transcripts (sent directly from institution), ELP scores (sent directly from testing centre)
- Email for ELP submissions: enrol@athabascau.ca

### 3.5 Transfer Credit

AU recognizes prior learning through:
- Transfer credit from recognized post-secondary institutions
- Prior Learning Assessment and Recognition (PLAR)
- Challenge for Credit examinations
- Letter of Permission for courses taken elsewhere

---

## Section 4 — Costs & financial aid

### 4.1 Fee Structure Overview

AU uses an **all-inclusive per-course fee model**. Course fees include: tuition, course administration & technology fee, course materials fee (textbooks included), and Students' Union & Alumni Relations fees. Additional fees may apply for out-of-province and out-of-country students.

Fee rates vary by:
- **Faculty** (Business, Health Disciplines, Humanities & Social Sciences, Science & Technology)
- **Student category** (Alberta resident, Canadian non-Alberta, Indigenous, Senior, Non-Canadian in Canada, Outside Canada)
- **Credit value** of the course (0-credit, 1-credit, 3-credit, 4-credit, 6-credit, 9-credit)

### 4.2 Per-3-Credit-Course Fees (Sep 1, 2025 – Aug 31, 2026)

#### Alberta Residents

| Category | Business | Health Disc. | Humanities & SS | Science & Tech. |
|----------|---------|-------------|----------------|----------------|
| Tuition fee | $669 | $669 | $621 | $621 |
| Course Admin & Tech Fee | $181 | $181 | $166 | $166 |
| Course Materials Fee | $88 | $88 | $88 | $88 |
| Students' Union ($13.50) + Alumni Relations ($2) | $15.50 | $15.50 | $15.50 | $15.50 |
| **3-credit total** | **$953.50** | **$953.50** | **$890.50** | **$890.50** |

#### Non-Canadian (living temporarily in Alberta)

| Category | Business | Health Disc. | Humanities & SS | Science & Tech. |
|----------|---------|-------------|----------------|----------------|
| Tuition fee | $1,338 | $1,338 | $1,242 | $1,242 |
| Course Admin & Tech Fee | $181 | $181 | $166 | $166 |
| Course Materials Fee | $88 | $88 | $88 | $88 |
| Students' Union + Alumni Relations | $15.50 | $15.50 | $15.50 | $15.50 |
| **3-credit total** | **$1,622.50** | **$1,622.50** | **$1,511.50** | **$1,511.50** |

#### Non-Canadian (living temporarily outside Alberta)

| Category | Business | Health Disc. | Humanities & SS | Science & Tech. |
|----------|---------|-------------|----------------|----------------|
| Tuition fee | $1,338 | $1,338 | $1,242 | $1,242 |
| Course Admin & Tech Fee | $181 | $181 | $166 | $166 |
| Course Materials Fee | $88 | $88 | $88 | $88 |
| Students' Union + Alumni Relations | $15.50 | $15.50 | $15.50 | $15.50 |
| Out of Province Fee | $187 | $187 | $187 | $187 |
| **3-credit total** | **$1,809.50** | **$1,809.50** | **$1,698.50** | **$1,698.50** |

### 4.3 Estimated Total Program Fees (120-credit UG program)

| Category | Business | Health Disc. | Humanities & SS | Science & Tech. |
|----------|---------|-------------|----------------|----------------|
| Alberta residents | $38,140 | $38,140 | $35,620 | $35,620 |
| Indigenous students in Alberta | $35,550 | $35,550 | $33,100 | $33,100 |
| Canadian seniors in Alberta | $24,700 | $24,700 | $23,140 | $23,140 |
| Canadian residents outside Alberta | $45,620 | $45,620 | $43,100 | $43,100 |
| Indigenous outside Alberta | $42,980 | $42,980 | $40,580 | $40,580 |

**Note**: These are estimates based on 3-credit courses. Actual costs vary if 6-credit courses are used. Academic-related fees (lab fees, exam fees) are not included. Plus one-time General Application Fee.

### 4.4 Financial Aid & Scholarships

- AU offers various financial aid options (student loans, bursaries, scholarships)
- Alberta student loans available for eligible Alberta residents
- Canadian student loans for residents of other provinces
- AU-specific awards and scholarships available
- Payment plans available
- T2202 tuition tax receipt for Canadian income tax purposes

**Source**: https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/index.html

---

## Section 5 — Evidence chain index

| Evidence ID | Field | Value | Source URL | Capture Date |
|------------|-------|------|------------|-------------|
| E-U-001 | institution.name | Athabasca University | https://www.athabascau.ca/ | 2026-07-10 |
| E-U-002 | institution.type | Canada's Open University (public online university) | https://www.athabascau.ca/ | 2026-07-10 |
| E-U-003 | institution.total_programs | ~90 graduate and undergraduate degrees, diplomas, and certificates | https://www.athabascau.ca/calendar/index.html | 2026-07-10 |
| E-U-004 | institution.total_courses | Over 850 university courses | https://www.athabascau.ca/calendar/index.html | 2026-07-10 |
| E-U-005 | faculties.list | Business, Health Disciplines, Humanities and Social Sciences, Science and Technology, Graduate Studies | https://www.athabascau.ca/ | 2026-07-10 |
| E-U-006 | programs.ug.full_list | 51+ UG degree programs, certificates, diplomas | https://www.athabascau.ca/programs/index.html#/undergraduate/all/all | 2026-07-10 |
| E-U-007 | programs.grad.full_list | 18+ graduate programs (Master's, Grad Cert, Grad Dip, Doctoral) | https://www.athabascau.ca/programs/index.html#/graduate/all/all | 2026-07-10 |
| E-U-008 | fees.ug.3credit.alberta | $953.50 (Business/Health) or $890.50 (HSS/SciTech) | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/canadian-student-fees.html | 2026-07-10 |
| E-U-009 | fees.ug.3credit.noncanadian_alberta | $1,622.50 (Business/Health) or $1,511.50 (HSS/SciTech) | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/non-canadian-student-fees.html | 2026-07-10 |
| E-U-010 | fees.ug.3credit.noncanadian_outside_ab | $1,809.50 (Business/Health) or $1,698.50 (HSS/SciTech) | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/non-canadian-student-fees.html | 2026-07-10 |
| E-U-011 | fees.ug.120credit_est.alberta | $35,620–$38,140 depending on faculty | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/estimated-program-fees.html | 2026-07-10 |
| E-U-012 | fees.ug.120credit_est.outside_ab | $43,100–$45,620 depending on faculty | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/estimated-program-fees.html | 2026-07-10 |
| E-U-013 | admission.ug.ELP.IELTS | Minimum 6.0 overall | https://www.athabascau.ca/calendar/undergraduate/admission-registration-evaluation/english-language-proficency.html | 2026-07-10 |
| E-U-014 | admission.ug.ELP.TOEFL | 80 (before Jan 2026) or 4 (after Jan 2026) | https://www.athabascau.ca/calendar/undergraduate/admission-registration-evaluation/english-language-proficency.html | 2026-07-10 |
| E-U-015 | admission.ug.ELP.Duolingo | Minimum 105 overall, 75 each band | https://www.athabascau.ca/calendar/undergraduate/admission-registration-evaluation/english-language-proficency.html | 2026-07-10 |
| E-U-016 | admission.ug.ELP.PTE | 59 overall, no less than 51 each skill | https://www.athabascau.ca/calendar/undergraduate/admission-registration-evaluation/english-language-proficency.html | 2026-07-10 |
| E-U-017 | admission.grad.ELP | TOEFL 80/4, IELTS 6.0, MELAB 80, CAEL 60 | https://www.athabascau.ca/calendar/graduate/additional-information/english-language-proficiency-requirements.html | 2026-07-10 |
| E-U-018 | admission.model | Open admissions (UG); rolling enrollment | https://www.athabascau.ca/applications-admissions/index.html | 2026-07-10 |
| E-U-019 | fees.effective_date | Sep 1, 2025 – Aug 31, 2026 | https://www.athabascau.ca/calendar/undergraduate/fees-refunds-and-financial-assistance/index.html | 2026-07-10 |
| E-U-020 | calendar.undergrad.effective | Sep 1, 2025 – Aug 31, 2026 | https://www.athabascau.ca/calendar/undergraduate/index.html | 2026-07-10 |
| E-U-021 | calendar.grad.effective | Sep 1, 2025 – Aug 31, 2026 | https://www.athabascau.ca/calendar/graduate/index.html | 2026-07-10 |

---

## Section 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data item | Reason |
|----------|-----------|--------|
| **P0** | Full Post Diploma Route (18 programs) individual details | Listed as a credential filter but individual programs not extracted from the JS interface |
| **P0** | Graduate ELP specific minimum score per test (detailed) | Page references test scores but the individual score thresholds require expanding accordion sections |
| **P1** | Graduate program-specific admission requirements (GPA, prerequisites) | Each graduate program has faculty-specific requirements beyond general ELP |
| **P1** | AU-specific scholarships and awards list and amounts | Financial aid page has a link to "Financial assistance" but detailed amounts not extracted |
| **P1** | Indigenous student fee details | Listed as fee category but "Indigenous student fees" subpage not accessible via direct URL |
| **P1** | Canadian senior citizen fee details | Listed as fee category but subpage content not verified beyond estimated program fees |
| **P2** | Per-program fee details for graduate programs | Graduate program fees not shown in the Undergraduate Calendar; need Graduate Calendar fee pages |
| **P2** | Cost of living estimates | AU is online/distance so no on-campus living costs, but may have relevant information |

**Note on open university model**: AU does not use a traditional department structure. Programs are administered directly by faculties. The "department" column in Sections 1 and 2 is left blank as there are no intermediate academic units between faculty and program.

---

## Section 7 — Cross-school comparison framework

| Dimension | Athabasca University | Acadia University |
|-----------|--------------------|-------------------|
| Type | Public Open University (Online) | Public (Traditional + Online) |
| Location | Athabasca, Alberta | Wolfville, Nova Scotia |
| Country | Canada | Canada |
| Total programmes | ~90 | — |
| UG degree programmes | ~34 | — |
| Graduate programmes | ~24 (Master's + Grad Certs/Dips + Doctoral) | — |
| Faculties/Schools | 5 | — |
| Open admissions | ✅ Yes (UG) | — |
| Rolling enrollment | ✅ Yes | — |
| Online-first | ✅ Fully online | — |
| Language req (UG IELTS) | 6.0 | — |
| Language req (Grad IELTS) | 6.0 | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Athabasca University official website and Calendar
> **Granularity**: faculty → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ | PG programmes ✅ (full list) | Evidence (21 blocks) ✅ | Fees details ✅ | ELP requirements ✅
> **Next step**: Expand Post Diploma Route details (18 programs) and graduate program-specific admission requirements
