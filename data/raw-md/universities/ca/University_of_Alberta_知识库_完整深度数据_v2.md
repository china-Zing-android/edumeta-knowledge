# University of Alberta 知识库_完整深度数据_v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: college → faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (CA) — Alberta, Edmonton

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科项目 (UG programmes) | ~200+ (400+ 涵盖所有类别) |
| 研究生授课型项目 (PGT: MSc/MA/MEng/MBA/etc.) | ~200+ |
| 研究生研究型项目 (PhD/MSc-thesis) | ~150+ |
| 学位项目总计 | ~500+ |
| 学院/学系 (Colleges) | 3 |
| 学院 (Faculties/Schools) | 18 |
| 学术院系 (Academic Departments) | ~100+ |

### 0.2 院校层级结构

```
University of Alberta (U of A)
├── College of Health Sciences
│   ├── Faculty of Kinesiology, Sport, and Recreation
│   ├── Faculty of Medicine and Dentistry
│   ├── Faculty of Nursing
│   ├── Faculty of Pharmacy and Pharmaceutical Sciences
│   ├── School of Public Health
│   └── Faculty of Rehabilitation Medicine
├── College of Natural and Applied Sciences
│   ├── Faculty of Agricultural, Life and Environmental Sciences (ALES)
│   ├── Faculty of Engineering
│   └── Faculty of Science
├── College of Social Sciences and Humanities
│   ├── Faculty of Arts
│   ├── Faculty of Business (Alberta School of Business)
│   ├── Faculty of Education
│   └── Faculty of Law
├── Standalone Faculties
│   ├── Augustana Faculty
│   ├── Faculty of Native Studies
│   ├── Faculté Saint-Jean (French-language campus)
│   └── Faculty of Graduate & Postdoctoral Studies (oversight body)
└── Campuses
    ├── North Campus (Main — Edmonton)
    ├── Campus Saint-Jean (Edmonton)
    ├── Augustana Campus (Camrose)
    ├── Enterprise Square (Edmonton Downtown)
    └── South Campus (Edmonton)
```

### 0.3 学历级别明细

| 学历级别 | 说明 |
|---------|------|
| Bachelor's (BA, BSc, BEd, BComm, BCom, BMus, BFA, BSN, BScEng, BScN, LLB/JD) | 本科学位 |
| Master's (MA, MSc, MBA, MEd, MEng, MFA, MMus, MPH, MScN, MScPT, MScOT, MScSLP, LLM) | 硕士学位 |
| Doctorate (PhD, EdD, DM, DNursing) | 博士学位 |
| Graduate Certificate | 研究生证书 |
| Graduate Diploma | 研究生文凭 |
| Undergraduate Certificate | 本科证书 |
| Undergraduate Diploma | 本科文凭 |

### 0.4 分布矩阵 (College × 学历级别)

| College / Faculty | Bachelor's | Master's | PhD | Certificate/Diploma |
|-----|-----------|---------|-----|-------------------|
| **College of Health Sciences** | | | | |
| Kinesiology, Sport, and Recreation | ✓ | ✓ | ✓ | ✓ |
| Medicine and Dentistry | ✓ (MD/DDS) | ✓ | ✓ | ✓ |
| Nursing | ✓ | ✓ | ✓ | ✓ |
| Pharmacy and Pharmaceutical Sciences | ✓ | ✓ | ✓ | ✓ |
| Public Health | — | ✓ | ✓ | ✓ |
| Rehabilitation Medicine | ✓ | ✓ | ✓ | ✓ |
| **College of Natural and Applied Sciences** | | | | |
| ALES | ✓ | ✓ | ✓ | ✓ |
| Engineering | ✓ | ✓ | ✓ | ✓ |
| Science | ✓ | ✓ | ✓ | ✓ |
| **College of Social Sciences and Humanities** | | | | |
| Arts | ✓ | ✓ | ✓ | ✓ |
| Business | ✓ | ✓ | ✓ | ✓ |
| Education | ✓ | ✓ | ✓ | ✓ |
| Law | ✓ (JD) | ✓ (LLM) | — | — |
| **Standalone** | | | | |
| Augustana Faculty | ✓ | — | — | — |
| Native Studies | ✓ | ✓ | — | ✓ |
| Faculté Saint-Jean | ✓ | — | — | — |

---

## Section 1 — Undergraduate Education

### 1.1 本科项目类别分布

通过 U of A 项目搜索工具分类：

| 主题类别 | 包含项目数 |
|---------|----------|
| People, Culture, and Society | ~112 |
| Math, Chemistry, and Physics | ~87 |
| Health and Life Sciences | ~83 |
| Education | ~78 |
| Engineering and Technology | ~54 |
| Business and Economics | ~53 |
| Earth, Environment, and Sustainability | ~42 |
| Media and Fine Arts | ~41 |
| History, Law, and Politics | ~36 |
| Languages and Linguistics | ~30 |

*注：以上类别有重叠（跨学科项目被归入多个类别），实际独立本科项目约200+*

### 1.2 College of Health Sciences — 本科项目

**Faculty of Kinesiology, Sport, and Recreation**
| Program | Degree | Department |
|---------|--------|-----------|
| Kinesiology | BKin | Kinesiology |
| Physical Activity and Health | BKin | Kinesiology |
| Sports Performance | BKin | Kinesiology |

**Faculty of Medicine and Dentistry**
| Program | Degree |
|---------|--------|
| Doctor of Dental Surgery | DDS |
| Dental Hygiene | Diploma/BSc |
| Medical Doctor | MD |

**Faculty of Nursing**
| Program | Degree |
|---------|--------|
| Nursing | BScN |

**Faculty of Pharmacy and Pharmaceutical Sciences**
| Program | Degree |
|---------|--------|
| Pharmacy | BSc Pharmacy |

**Faculty of Rehabilitation Medicine**
| Program | Degree | Department |
|---------|--------|-----------|
| Occupational Therapy | BScOT | Occupational Therapy |
| Physical Therapy | BScPT | Physical Therapy |
| Speech-Language Pathology | BScSLP | Speech Pathology |

### 1.3 College of Natural and Applied Sciences — 本科项目

**Faculty of Agricultural, Life and Environmental Sciences (ALES)**
| Program | Degree | Department |
|---------|--------|-----------|
| Agricultural and Resource Economics | BSc | Resource Economics |
| Agricultural Biotechnology | BSc | Various |
| Agriculture (General) | BSc | Various |
| Animal Health | BSc | Various |
| Animal Science | BSc | Various |
| Conservation Biology | BSc | Various |
| Crop Science | BSc | Various |
| Environmental and Conservation Sciences | BSc | Various |
| Food Business Management | BSc | Various |
| Food Science and Technology | BSc | Various |
| Forestry | BSc | Various |
| Human Ecology | BSc/BSc(HEcol) | Various |
| Nutrition and Food Sciences | BSc | Various |
| Plant Biology | BSc | Various |
| Renewable Resources | BSc | Various |
| Soil Science | BSc | Various |
| Sustainable Agriculture | BSc | Various |
| Wildlife Biology | BSc | Various |

**Faculty of Engineering**
| Program | Degree |
|---------|--------|
| Chemical Engineering | BSc in Engineering |
| Civil Engineering | BSc in Engineering |
| Computer Engineering | BSc in Engineering |
| Electrical Engineering | BSc in Engineering |
| Engineering Physics | BSc in Engineering |
| Materials Engineering | BSc in Engineering |
| Mechanical Engineering | BSc in Engineering |
| Mining Engineering | BSc in Engineering |
| Petroleum Engineering | BSc in Engineering |
| Engineering (General — first year) | BSc in Engineering |

**Faculty of Science**
| Program | Degree | Department |
|---------|--------|-----------|
| Applied Mathematics | BSc | Mathematics |
| Astrophysics | BSc | Physics |
| Biochemistry | BSc | Biochemistry |
| Biological Sciences | BSc | Biological Sciences |
| Cell Biology | BSc | Biological Sciences |
| Chemistry | BSc | Chemistry |
| Computing Science | BSc/BSc(Hons) | Computing Science |
| Data Science | BSc | Computing Science |
| Earth and Atmospheric Sciences | BSc | Earth Sciences |
| Ecology | BSc | Biological Sciences |
| Environmental Earth Sciences | BSc | Earth Sciences |
| Environmental Physical Sciences | BSc | Various |
| Genetics | BSc | Biological Sciences |
| Geology | BSc | Earth Sciences |
| Geophysics | BSc | Earth Sciences |
| Immunology and Infection | BSc | Biological Sciences |
| Marine Biology | BSc | Biological Sciences |
| Mathematical Physics | BSc | Mathematics/Physics |
| Mathematics | BSc | Mathematics |
| Mathematics and Finance | BSc | Mathematics |
| Microbiology | BSc | Biological Sciences |
| Molecular Genetics | BSc | Biological Sciences |
| Neuroscience | BSc | Various |
| Paleontology | BSc | Earth Sciences |
| Pharmacology | BSc | Pharmacology |
| Physics | BSc | Physics |
| Physiology | BSc | Physiology |
| Plant Biology | BSc | Biological Sciences |
| Psychology | BSc | Psychology |
| Statistics | BSc | Mathematics |
| Zoology | BSc | Biological Sciences |

### 1.4 College of Social Sciences and Humanities — 本科项目

**Faculty of Arts**
| Program | Degree | Department |
|---------|--------|-----------|
| Anthropology | BA | Anthropology |
| Arabic and Islamic Studies | BA | Religious Studies |
| Art and Design | BA/BFA | Art and Design |
| Biological Anthropology | BA/BSc | Anthropology |
| Chinese Studies | BA | East Asian Studies |
| Classics | BA | History/Classics |
| Comparative Literature | BA | Modern Languages |
| Creative Writing | BA | English |
| Criminology | BA | Sociology |
| Digital Humanities | BA | Various |
| Drama | BA | Drama |
| East Asian Studies | BA | East Asian Studies |
| Economics | BA | Economics |
| English | BA | English |
| Film Studies | BA | Modern Languages |
| French Language and Literature | BA | Modern Languages |
| German Language and Literature | BA | Modern Languages |
| Greek and Roman Studies | BA | History/Classics |
| History | BA | History |
| Humanities | BA | Various |
| Indigenous Studies | BA | Native Studies |
| Italian Language and Literature | BA | Modern Languages |
| Japanese Studies | BA | East Asian Studies |
| Linguistics | BA | Linguistics |
| Mathematics | BA | Mathematics |
| Media Studies | BA | Various |
| Modern Languages | BA | Modern Languages |
| Music | BA/BMus | Music |
| Native Studies | BA | Native Studies |
| Philosophy | BA | Philosophy |
| Political Science | BA | Political Science |
| Psychology | BA | Psychology |
| Religious Studies | BA | Religious Studies |
| Russian Language and Literature | BA | Modern Languages |
| Science, Technology and Society | BA | Various |
| Slavic Languages and Literature | BA | Modern Languages |
| Sociology | BA | Sociology |
| Spanish Language and Literature | BA | Modern Languages |
| Statistics | BA | Mathematics/Business |
| Women's and Gender Studies | BA | Various |

**Alberta School of Business**
| Program | Degree |
|---------|--------|
| Accounting | BCom |
| Business Economics and Law | BCom |
| Business Studies | BCom |
| Entrepreneurship | BCom |
| Finance | BCom |
| Human Resources Management | BCom |
| International Business | BCom |
| Management Information Systems | BCom |
| Marketing | BCom |
| Operations Management | BCom |
| Strategic Management and Organization | BCom |
| Supply Chain Management | BCom |

**Faculty of Education**
| Program | Degree |
|---------|--------|
| Elementary Education | BEd |
| Secondary Education | BEd |
| Combined Degrees (BEd/BSc, BEd/BA, etc.) | BEd/BA, BEd/BSc |
| Physical Education | BEd |

**Faculty of Law**
| Program | Degree |
|---------|--------|
| Juris Doctor | JD |

### 1.5 Standalone Faculties — 本科项目

**Augustana Faculty (Camrose Campus)**
| Program | Degree |
|---------|--------|
| Liberal Arts and Sciences — BA/BSc (various majors) | BA/BSc |
| Environmental Studies | BA/BSc |
| Psychology | BA/BSc |

**Faculté Saint-Jean (French-language campus)**
| Program | Degree |
|---------|--------|
| Arts (en français) | BA |
| Science (en français) | BSc |
| Education (en français) | BEd |

---

## Section 2 — Graduate Education

### 2.1 Graduate Programs by College

**Faculty of Graduate & Postdoctoral Studies** oversees all graduate programs across:

**College of Health Sciences Graduate Programs:**
- Kinesiology, Sport, and Recreation — MSc, PhD
- Medicine and Dentistry — MSc, PhD (various specialties)
- Nursing — MN, MScN, PhD
- Pharmacy and Pharmaceutical Sciences — MSc, PhD
- Rehabilitation Medicine — MSc (OT, PT, SLP), PhD
- Public Health — MPH, MSc, PhD

**College of Natural and Applied Sciences Graduate Programs:**
- ALES — MSc, PhD (Agricultural Economics, Animal Science, Food Science, Forestry, etc.)
- Engineering — MEng, MASc, MSc, PhD (all engineering disciplines)
- Science — MSc, PhD (Biological Sciences, Chemistry, Computing Science, Earth Sciences, Mathematics, Physics, Psychology, Statistics, etc.)

**College of Social Sciences and Humanities Graduate Programs:**
- Arts — MA, PhD (Anthropology, Economics, English, History, Philosophy, Political Science, Sociology, etc.)
- Business — MBA, MSc, PhD
- Education — MEd, MA, MSc, PhD
- Law — LLM

**Standalone Graduate Programs:**
- Native Studies — MA
- Interdisciplinary programs — MA, MSc, PhD

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admission Requirements

**General Requirements:**
- All undergraduate programs require completion of five specific Grade 12 subjects
- English 30-1 (or provincial equivalent) is always required
- Admission is competitive and subject to space availability

**Competitive Averages:**
- Competitive averages vary by faculty/program and change throughout the year
- Highly competitive programs require higher averages
- Meeting the minimum does not guarantee admission

**International Students:**
- Country-specific requirements apply
- International high school pathway or bridging program available
- See: International Undergraduate Admissions page

**Transfer Students:**
- Post-secondary transfer from Canadian, US, or international institutions accepted
- Transfer credit assessment on application

**Application Fee:**
- CAD $150 (new applicants)
- CAD $100 (current or previous U of A students)
- Non-refundable

**Additional Requirements (program-specific):**
- Portfolio (Art and Design, Drama)
- Audition (Music, Drama)
- Interview (some programs)
- References or written statement

### 3.2 English Language Proficiency (Undergraduate)

**General ELP (English Language Proficiency) — all applicants:**

| Method | Requirement |
|--------|-----------|
| TOEFL iBT (before Jan 21, 2026) | Total score 90, no section less than 21 |
| TOEFL iBT (on/after Jan 21, 2026) | Overall score 4.5 (1-6 scale), no band below 4.5 |
| IELTS Academic | 6.5 overall, no band less than 6.0 |
| Duolingo English Test | Overall 120, no integrated subscore below 100 (valid through 2028-29) |
| CAEL (paper or online) | Score 70, no band less than 60 |
| Cambridge English: Advanced (CAE) | 180 overall, no less than 170 in each skill |
| Cambridge English: Proficiency (CPE) | 180 overall, no less than 170 in each skill |
| PTE Academic | 61 overall, no less than 60 in each skill |

**High School Exam ELP alternatives:**
- Alberta/NWT ELA 30-1: 75% or higher final blended grade (mandatory diploma exam)
- IB English A: Literature/Language & Literature: 5 or better
- IB English B: 6 or better
- AP English: 4 or better
- GCE A-level/AS/GCSE/IGCSE/O-level English Language or Literature: B/6 or better

**Previous Education in English:**
- 3+ years of full-time education in English in Canada or ELP-exempt country
- Graduation from degree program at accredited English-language university

**Spoken English Proficiency (SEP) — required for Education & Health Sciences (e.g., Nursing):**

| Method | Requirement |
|--------|-----------|
| TOEFL iBT Speaking (before Jan 21, 2026) | Minimum 26 in Speaking section |
| TOEFL iBT Speaking (on/after Jan 21, 2026) | Minimum 5.0 (1-6 scale) |
| IELTS Speaking | Minimum 7.5 in Speaking section |
| Duolingo English Test | Overall 140, no integrated subscore below 120 |
| 6 years of full-time education in English | Successful completion |

### 3.3 Graduate Admission Requirements

**Master's programs minimum:**
- 4-year Bachelor's degree from recognized institution
- GPA minimum (typically 3.0/4.0 or B+ in last 60 credits)
- Two letters of reference
- Statement of purpose
- English Language Proficiency

**Doctoral programs minimum:**
- Master's degree from recognized institution (or exceptional Bachelor's)
- GPA minimum (typically 3.3/4.0)
- Research proposal
- Reference letters
- English Language Proficiency

**Graduate English Language Proficiency:**

| Test | Minimum Score (Graduate) |
|------|------------------------|
| TOEFL iBT | 90 overall (no section <21) / 4.5 (no band <4.5 after Jan 2026) |
| IELTS Academic | 6.5 overall (no band <6.0) |
| Duolingo | 120+ (varies by program) |
| CAEL | 70 (no band <60) |
| PTE Academic | 61 (no band <60) |

### 3.4 Application Deadlines

**Undergraduate — Fall 2026 Timeline:**

| Date | Deadline |
|------|---------|
| October 1, 2025 | Applications open for admission, awards, and residence |
| October 18, 2025 | Open House |
| January 10, 2026 | Entrance Award Application Deadline |
| February 15, 2026 | Deadline to submit Program Change Request form |
| March 1, 2026 | **Application deadline for most programs** |
| March 31, 2026 | Deadline to accept admission offer (Law JD) |
| April 30, 2026 | Deadline to self-report final high school marks |
| April 30, 2026 | Residence application deadline (guaranteed spot) |
| May 1, 2026 | Deadline to accept admission offers made before April 1 |
| June 15, 2026 | Post-secondary final transcripts deadline |
| August 1, 2026 | Outstanding documents deadline (high school) |
| September 2026 | Classes begin |

*Note: Different deadlines apply for Dental Hygiene, Dentistry, Medicine, and Law programs*

**Graduate:**
- Deadlines are program-specific
- Most programs admit for Fall term
- Check individual program pages for specific deadlines

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition & Fees

**Canadian Students — First-Year Estimate (2025-26, general Arts program):**

| Cost Item | Amount |
|-----------|--------|
| Tuition | $7,150 |
| Books, Supplies and Fees | $3,700 |
| **Year 1 Total (tuition + fees)** | **$10,850** |
| Residence and Meal Plan* | $14,200+ |
| **Year 1 Total (incl. residence)** | **$25,050** |

*\*Based on single room with private washroom in Schäffer Hall, eight months, 7-day meal plan*

**International Students — Key Costs:**
- Tuition deposit: $5,000 (students outside Canada) / $1,000 (students already in Canada)
- Use Cost Calculator for personalized estimate
- International tuition guarantee applies to admitted cohorts
- See International Tuition + Fees page for program-specific rates

### 4.2 Graduate Tuition & Fees

- Graduate instructional fees vary by: Canadian/international status, admission date, and program type (course-based vs thesis-based)
- Non-standard fees apply for some programs
- Actual fee assessments available on Bear Tracks
- Fee payment deadlines: typically late September (Fall) and late January (Winter)

**Graduate Funding:**
- Teaching assistantships and research assistantships available
- Tuition offset funding: $8.5M/year domestic, 8.55% of international tuition revenue set aside for student support
- Payroll deduction available for TA/RA appointments

### 4.3 Scholarships & Financial Aid

**Entrance Scholarships:**
- Entrance Award Application Deadline: January 10, 2026
- Automatic consideration for most high school applicants
- International Entrance Scholarships available

**Additional Support:**
- Scholarships, Awards, Bursaries
- Financial Support and Advising services
- Work-Study Program
- Government Student Loans
- US Government Student Loans

**$52 Million+ in funding** for scholarships, awards, and financial support annually.

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-UA-001 | institution.name | "University of Alberta" | https://www.ualberta.ca/en/index.html | official_webpage |
| E-UA-002 | institution.location | Edmonton, Alberta, Canada | https://www.ualberta.ca/en/index.html | official_webpage |
| E-UA-003 | total.programs | 400+ diverse programs | https://www.ualberta.ca/en/admissions-programs/index.html | official_webpage |
| E-UA-004 | ranking.canada | #4 research-based university in Canada | https://www.ualberta.ca/en/admissions-programs/index.html | official_webpage |
| E-UA-005 | ranking.world | Top 100 universities in the world | https://www.ualberta.ca/en/admissions-programs/index.html | official_webpage |
| E-UA-006 | student.population | ~46,000 students | https://www.ualberta.ca/en/index.html | official_webpage |
| E-UA-007 | colleges.count | 3 | https://calendar.ualberta.ca/content.php?catoid=69&navoid=20882 | academic_calendar |
| E-UA-008 | faculties.count | 18 (including schools + Augustana + Saint-Jean) | https://calendar.ualberta.ca/content.php?catoid=69&navoid=20882 | academic_calendar |
| E-UA-009 | campuses.count | 5 | https://www.ualberta.ca/en/index.html | official_webpage |
| E-UA-010 | ug.admission.requirements | 5 Grade 12 subjects incl. English 30-1, competitive averages | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/index.html | official_webpage |
| E-UA-011 | ug.application.fee | $150 ($100 for current/former students) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/index.html | official_webpage |
| E-UA-012 | ug.elp.toefl | 90 (before Jan 2026) / 4.5 (after Jan 2026) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-013 | ug.elp.ielts | 6.5 overall (no band <6.0) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-014 | ug.elp.duolingo | 120 overall (subscores 100+) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-015 | ug.elp.cael | 70 (no band <60) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-016 | ug.elp.pte | 61 (no band <60) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-017 | ug.sep.toefl | Speaking 26 (before Jan 2026) / 5.0 (after Jan 2026) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-018 | ug.sep.ielts | Speaking 7.5 | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-019 | ug.tuition.canadian | $7,150/year (Arts, first-year) | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/tuition-and-fees.html | official_webpage |
| E-UA-020 | ug.tuition.books.fees | $3,700 | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/tuition-and-fees.html | official_webpage |
| E-UA-021 | ug.tuition.total.firstyear | $10,850 (tuition + fees, excl. residence) | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/tuition-and-fees.html | official_webpage |
| E-UA-022 | ug.residence.cost | $14,200+ (room + meal plan) | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/tuition-and-fees.html | official_webpage |
| E-UA-023 | ug.total.with.residence | $25,050 (year 1) | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/tuition-and-fees.html | official_webpage |
| E-UA-024 | ug.deadlines.fall2026 | Applications open Oct 1, 2025; deadline Mar 1, 2026 | https://www.ualberta.ca/en/admissions/how-to-apply/dates-deadlines/index.html | official_webpage |
| E-UA-025 | ug.deadline.awards | January 10, 2026 | https://www.ualberta.ca/en/admissions/how-to-apply/dates-deadlines/index.html | official_webpage |
| E-UA-026 | ug.intl.tuition.deposit | $5,000 (outside Canada) / $1,000 (in Canada) | https://www.ualberta.ca/en/admissions/tuition-and-scholarships/international-tuition-and-fees.html | official_webpage |
| E-UA-027 | grad.faculty | Faculty of Graduate & Postdoctoral Studies (GPS) | https://www.ualberta.ca/en/graduate-studies/index.html | official_webpage |
| E-UA-028 | grad.tuition.framework | Varies by status, admission date, program type | https://www.ualberta.ca/en/graduate-studies/fees-funding/tuition-fees/index.html | official_webpage |
| E-UA-029 | academic.calendar | 2026-2027 | https://calendar.ualberta.ca/ | academic_calendar |
| E-UA-030 | ug.program.categories | 10 themes, ~200+ unique programs | https://www.ualberta.ca/en/undergraduate-programs/index.html | official_webpage |
| E-UA-031 | institution.founded | 1908 | https://www.ualberta.ca/en/about/index.html | official_webpage |
| E-UA-032 | ug.elp.cambridge | CAE/CPE: 180 overall (no <170) | https://www.ualberta.ca/en/admissions/how-to-apply/admission-requirements/language-requirements/index.html | official_webpage |
| E-UA-033 | scholarships.funding | $52M+ annually | https://www.ualberta.ca/en/admissions-programs/index.html | official_webpage |
| E-UA-034 | grad.employment.rank | Top 5 in Canada | https://www.ualberta.ca/en/admissions-programs/index.html | official_webpage |

---

## Section 6 — WeKnora Import Manifest & Follow-Up Items

### P0 — Must Extract

| Item | Notes |
|------|-------|
| Individual program-specific tuition fees | UofA uses cost calculator, needs interactive access |
| Graduate tuition fees by program | Tables behind navigation, requires program-specific search |
| Competitive admission averages by program | Historical ranges from competitive averages page |
| Program-specific admission requirements | Portfolio/audition/interview details for Arts, Music, Drama |
| International tuition fee schedule | Exact international per-program rates not fully extracted |

### P1 — Should Extract

| Item | Notes |
|------|-------|
| Graduate program-specific ELP requirements | Some programs have higher minimums than general requirements |
| Course catalog / listings | Available in University Calendar Course Listings section |
| Co-op and internship program details | UofA has strong experiential learning programs |
| Faculty-specific research areas | Each graduate program has specialized research fields |
| Residence options and costs | Detailed residence information on residence website |

### P2 — Nice-to-Have

| Item | Notes |
|------|-------|
| Full faculty research profiles | Individual professor research areas |
| Student demographics | Enrollment numbers, international student ratios |
| Graduate employment outcomes | Post-graduation data |
| Campus-specific program offerings | Augustana and Saint-Jean campus programs |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | University of Alberta | University of British Columbia |
|-----------|----------------------|-------------------------------|
| Location | Edmonton, AB | Vancouver/Kelowna, BC |
| Founded | 1908 | 1908 |
| Type | Public research (Top 100 world) | Public research (Top 50 world) |
| Student population | ~46,000 | ~66,000 |
| Campuses | 5 | 2 |
| Colleges | 3 | 15+ |
| Faculties/Schools | 18 | ~20+ |
| UG Programs | ~200+ | ~300+ |
| Graduate Programs | ~350+ (combined) | ~200+ |
| UG Tuition (Canadian) | ~$7,150/year | ~$6,000/year |
| UG Tuition (International) | Varies by program | ~$45,000/year |
| ELP IELTS | 6.5 (UG) / 6.5 (Grad) | 6.5 (UG) / 6.5 (Grad) |
| ELP TOEFL | 90 (UG) / 90 (Grad) | 90 (UG) / 90 (Grad) |
| French campus | Yes (Campus Saint-Jean) | No |
| Notable strengths | Paleontology, AI/Robotics, Oil & Gas Eng. | Forestry, Oceanography, Pharmacy |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: University of Alberta official website (ualberta.ca), University Calendar (calendar.ualberta.ca)
> **Granularity**: college → faculty → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (partial list) | PG programmes ✅ (partial) | Evidence (34 blocks) ✅
> **Next step**: P0 items — program-specific tuition, competitive averages, international tuition schedule
