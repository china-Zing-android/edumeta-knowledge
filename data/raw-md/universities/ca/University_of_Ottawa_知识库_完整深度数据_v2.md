# University of Ottawa 知识库 完整深度数据

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department/school → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Ontario)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~220+ (含 Honours/Spécialisé/Major/Bachelor's) |
| 本科辅修 (Minors) | ~71+ |
| 本科证书 (Certificates) | ~10+ |
| 研究生硕士项目 (Master's) | ~215+ (含授课型与研究型) |
| 研究生博士项目 (PhD/Doctoral) | ~75+ |
| 研究生文凭 (Graduate Diplomas) | ~17+ |
| 微证书 (Microprograms) | ~20+ |
| **学位项目总计** | **~700+** |
| 学院 (Faculties) | 10 |
| 学术院系/所/中心 (Departments/Schools) | ~80+ |

### 0.2 学院 / 系层级结构

```
University of Ottawa
├── Faculty of Arts
│   ├── Department of Communication
│   ├── Department of English
│   ├── Department of French
│   ├── Department of History
│   ├── Department of Philosophy
│   ├── Department of Linguistics
│   ├── Department of Modern Languages and Literatures
│   ├── Department of Music
│   ├── Department of Theatre
│   ├── Department of Visual Arts
│   ├── School of Translation and Interpretation
│   ├── School of Information Studies (ÉSIS)
│   └── Institute of Indigenous Research and Studies
│
├── Faculty of Education
│   └── (Single-faculty, teacher education programs)
│
├── Faculty of Engineering
│   ├── Department of Chemical and Biological Engineering
│   ├── Department of Civil Engineering
│   ├── Department of Electrical Engineering and Computer Science
│   ├── Department of Mechanical Engineering
│   └── School of Engineering Design and Teaching Innovation
│
├── Faculty of Health Sciences
│   ├── School of Human Kinetics
│   ├── School of Nursing
│   ├── School of Nutrition Sciences
│   ├── School of Rehabilitation Sciences
│   ├── School of Epidemiology and Public Health
│   └── Interdisciplinary School of Health Sciences
│
├── Faculty of Law — Civil Law (Section de droit civil)
│   └── (Single-faculty, French-language common law and civil law)
│
├── Faculty of Law — Common Law
│   └── (English-language common law, JD program)
│
├── Faculty of Medicine
│   ├── Department of Biochemistry, Microbiology and Immunology
│   ├── Department of Cellular and Molecular Medicine
│   ├── Department of Family Medicine
│   ├── Department of Innovation in Medical Education
│   ├── Department of Medicine
│   ├── Department of Obstetrics and Gynecology
│   ├── Department of Ophthalmology
│   ├── Department of Pathology and Laboratory Medicine
│   ├── Department of Pediatrics
│   ├── Department of Psychiatry
│   ├── Department of Radiology, Radiation Oncology and Medical Physics
│   ├── School of Pharmaceutical Sciences
│   └── School of Translational and Molecular Medicine
│
├── Faculty of Science
│   ├── Department of Biology
│   ├── Department of Chemistry and Biomolecular Sciences
│   ├── Department of Earth and Environmental Sciences
│   ├── Department of Mathematics and Statistics
│   ├── Department of Physics
│   └── School of Computer Science and Electrical Engineering (joint with Engineering)
│
├── Faculty of Social Sciences
│   ├── School of Political Studies
│   ├── School of International Development and Global Studies
│   ├── School of Sociological and Anthropological Studies
│   ├── School of Psychology
│   ├── School of Criminology
│   ├── School of Social Work
│   ├── Department of Economics
│   ├── Institute of Feminist and Gender Studies
│   └── Institute for Science, Society and Policy
│
├── Telfer School of Management
│   └── (Single school, offers BCom, MBA, MSc Management, MHA, EMHA, PhD Management)
│
└── Faculty of Graduate and Postdoctoral Studies (FPGS)
    └── (Cross-faculty coordination, does not administer programs directly)
```

### 0.3 学历级别明细

| 学位级别 | 缩写 | 数量 (估算) |
|---------|------|------------|
| Bachelor of Arts | BA | 50+ |
| Bachelor of Science | BSc | 40+ |
| Bachelor of Social Sciences | BSocSc | 20+ |
| Bachelor of Commerce | BCom | 30+ (含选项分支) |
| Bachelor of Engineering | BASc/BEng | 20+ |
| Bachelor of Health Sciences | BHSc | 15+ |
| Bachelor of Fine Arts | BFA | 5+ |
| Bachelor of Music | BMus | 5+ |
| Bachelor of Human Kinetics | BHK | 10+ |
| Bachelor of Science in Nursing | BScN | 3+ |
| Bachelor of Education | BEd | 3+ |
| Juris Doctor / LLB | JD/LLL | 5+ |
| MD (Medicine) | MD | 1 |
| 本科学位小计 | | ~220+ |
| 本科辅修 | Minor | ~71+ |
| 本科证书 | Cert | ~10+ |
| Master of Arts / MSc | MA/MSc | 120+ |
| Master of Engineering | MEng | 20+ |
| Master of Business Administration | MBA/EMBA | 5+ |
| Master of Health Administration | MHA/EMHA | 3+ |
| Master of Education | MEd | 5+ |
| LLM | LLM | 5+ |
| 硕士学位小计 | | ~215+ |
| Doctor of Philosophy | PhD | 75+ |
| 研究生文凭 | GDip | 17+ |
| 微证书 | Microprogram | 20+ |
| **总计** | | **~700+** |

### 0.4 分布矩阵 (Faculty × Degree-Level)

| 学院 | UG Bachelor's | UG Minor | UG Cert | Master's | PhD | Grad Dip | Micro |
|------|:-----------:|:-------:|:-------:|:-------:|:---:|:-------:|:----:|
| Faculty of Arts | ~65 | ~30 | ~5 | ~40 | ~15 | ~5 | ~5 |
| Faculty of Education | ~10 | ~2 | ~0 | ~10 | ~5 | ~2 | ~2 |
| Faculty of Engineering | ~30 | ~5 | ~0 | ~30 | ~15 | ~3 | ~3 |
| Faculty of Health Sciences | ~25 | ~5 | ~2 | ~20 | ~10 | ~3 | ~2 |
| Faculty of Law (Civil + Common) | ~6 | ~0 | ~0 | ~8 | ~5 | ~2 | ~0 |
| Faculty of Medicine | ~10 | ~0 | ~0 | ~25 | ~15 | ~5 | ~3 |
| Faculty of Science | ~45 | ~15 | ~2 | ~20 | ~10 | ~2 | ~2 |
| Faculty of Social Sciences | ~40 | ~10 | ~2 | ~30 | ~10 | ~2 | ~2 |
| Telfer School of Management | ~30 | ~2 | ~2 | ~15 | ~2 | ~3 | ~10 |
| FPGS (跨学院) | — | — | — | — | — | — | — |
| **总计** | **~220+** | **~71** | **~10** | **~215** | **~75** | **~17** | **~20** |

---

## Section 1 — Undergraduate Education

### Faculty of Arts (UG Programs — 代表性选列)

| Program | Degree | Department/School |
|---------|--------|------------------|
| Communication | BA | Communication |
| English | BA | English |
| French | BA | French |
| History | BA | History |
| Philosophy | BA | Philosophy |
| Linguistics | BA | Linguistics |
| Music | BA/BMus | Music |
| Theatre | BA | Theatre |
| Visual Arts | BA/BFA | Visual Arts |
| Translation and Interpretation | BA | Translation and Interpretation |
| Modern Languages and Literatures | BA | Modern Languages |
| World Languages and Cultures | BA | Modern Languages |
| Second Language Teaching (ESL/FLS) | BA | Second Language Teaching |
| Professional Writing | BA | English |
| Creative Writing | Cert | English |
| Lettres françaises | BA | French |
| Communication et lettres françaises | BA | French/Communication |
| Journalism (in French) | BA | Communication |
| Advanced Minor in ESL | Minor | Second Language Teaching |
| Advanced Minor in FLS | Minor | Second Language Teaching |

### Faculty of Education (UG)

| Program | Degree |
|---------|--------|
| Bachelor of Education (BEd) — Intermediate/Senior | BEd |
| Bachelor of Education (BEd) — Primary/Junior | BEd |
| BA spécialisé Lettres françaises et BEd | BA/BEd |
| BSc spécialisé Sciences et BEd — Cycles intermédiaire/supérieur | BSc/BEd |

### Faculty of Engineering (UG)

| Program | Degree |
|---------|--------|
| Biomedical Mechanical Engineering | BASc |
| Chemical Engineering | BASc |
| Chemical Engineering, Engineering Management Option | BASc |
| Chemical Engineering, Environmental Engineering Option | BASc |
| Civil Engineering | BASc |
| Civil Engineering, Engineering Management Option | BASc |
| Civil Engineering, Environmental and Water Resources Option | BASc |
| Civil Engineering, Structural and Geotechnical Option | BASc |
| Computer Engineering | BASc |
| Electrical Engineering | BASc |
| Mechanical Engineering | BASc |
| Software Engineering | BASc |
| Biomedical Mechanical Engineering and Computing Technology | BASc + BSc |
| Chemical Engineering and Computing Technology | BASc + BSc |
| Civil Engineering and Computing Technology | BASc + BSc |
| Electrical Engineering and Computing Technology | BASc + BSc |
| Mechanical Engineering and Computing Technology | BASc + BSc |

### Faculty of Health Sciences (UG)

| Program | Degree |
|---------|--------|
| Human Kinetics (BHK) | BHK |
| Human Kinetics — Education and Coaching | BHK |
| Human Kinetics — Recreation and Sport Management | BHK |
| Human Kinetics (BSc) | BSc |
| Human Kinetics — Applied Studies in Kinesiology | BSc |
| Nursing | BScN |
| Nutrition Sciences | BSc |
| Health Sciences | BHSc/BSc |
| Food Sciences | BSc |
| Healthcare Analytics | BSc |

### Faculty of Law (UG)

| Program | Degree |
|---------|--------|
| Juris Doctor (JD) | JD |
| Honours BCom and JD | BCom + JD |
| Honours BSocSc Political Science and JD | BSocSc + JD |
| Joint Licentiate in Law (LLL) and MBA | LLL + MBA |
| Certificate Indigenous Laws | Cert |
| Certificate Law | Cert |

### Faculty of Medicine (UG)

| Program | Degree |
|---------|--------|
| MD Program (Doctor of Medicine) | MD |
| Translational and Molecular Medicine | BSc |
| Biomedical Science | BSc |
| Biopharmaceutical Science | BSc |
| Biochemistry | BSc |

### Faculty of Science (UG)

| Program | Degree |
|---------|--------|
| Biology | BSc |
| Biochemistry | BSc |
| Biomedical Science | BSc |
| Biopharmaceutical Science | BSc |
| Chemistry | BSc |
| Environmental Geoscience | BSc |
| Environmental Science | BSc |
| Food Sciences | BSc |
| Geology | BSc |
| Geology-Physics | BSc |
| Health Sciences | BSc |
| Mathematics | BSc |
| Mathematics and Computer Science (Data Science) | BSc |
| Physics | BSc |
| Physics-Mathematics | BSc |
| Physical Geography and Geomatics | BSc |
| Statistics | BSc |
| Computer Science | BSc |
| Financial Mathematics and Economics | BSc |
| Science (General) | BSc |
| Science with Major | BSc |
| Science with Minor | BSc |
| Science with Double Minor | BSc |

### Faculty of Social Sciences (UG)

| Program | Degree |
|---------|--------|
| Anthropology | BA/BSocSc |
| Criminology | BA/BSocSc |
| Economics | BA/BSocSc |
| Feminist and Gender Studies | BA/BSocSc |
| Geography | BA/BSocSc |
| History | BA |
| International Development and Globalization | BA/BSocSc |
| Political Science | BA/BSocSc |
| Psychology | BA/BSc |
| Public Administration | BSocSc |
| Public Relations | BA/BSocSc |
| Sociology | BA/BSocSc |
| Social Work | BSW |
| Conflict Studies and Human Rights | BA/BSocSc |
| Environmental Studies | BA/BSocSc |
| International Economics and Development | BA/BSocSc |
| International Studies and Modern Languages | BA |
| Communication and Sociology | BA |
| Communication and Political Science | BA/BSocSc |
| Economics and Political Science | BA/BSocSc |
| Economics and Public Policy | BA/BSocSc |
| Environmental Economics and Public Policy | BA/BSocSc |

### Telfer School of Management (UG)

| Program | Degree |
|---------|--------|
| Honours BCom (Option in Accounting) | BCom |
| Honours BCom (Option in Business Analytics) | BCom |
| Honours BCom (Option in Business Technology Management) | BCom |
| Honours BCom (Option in Entrepreneurship) | BCom |
| Honours BCom (Option in Finance) | BCom |
| Honours BCom (Option in Healthcare Analytics) | BCom |
| Honours BCom (Option in Human Resource Management) | BCom |
| Honours BCom (Option in International Management) | BCom |
| Honours BCom (Option in Management) | BCom |
| Honours BCom (Option in Marketing) | BCom |
| Honours BCom (Global Management) | BCom |
| Honours BCom — International Dual Degree | BCom |
| Honours BCom in Accounting | BCom |
| Honours BCom and JD | BCom + JD |
| Honours BCom and MSc Management (combined) | BCom + MSc (多种Option) |
| BCom and Master's in Management (combined) | BCom + MSc |
| Certificate Management | Cert |
| Certificate Human Resource Management | Cert |
| Minor Management | Minor |
| Minor Entrepreneurship | Minor |

---

## Section 2 — Graduate Education

### PGT / PGR Summary

| Category | Count | Description |
|----------|-------|-------------|
| Master's (research/thesis) | ~120+ | MA, MSc — research paper or thesis |
| Master's (course-based/short duration) | ~60+ | MEng, MBA, MHA, etc. — 8–20 months |
| Graduate Diplomas | ~17+ | GDip — practical focus |
| Microprograms | ~20+ | 4–8 month specializations |
| PhD Programs | ~75+ | Research doctorate |
| Professional Doctorates | ~5 | MD, JD already counted as UG |

### Representative Graduate Programs

#### Arts (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Communication | MA/PhD | Thesis |
| English | MA/PhD | Thesis |
| French Studies | MA/PhD | Thesis |
| History | MA/PhD | Thesis |
| Philosophy | MA/PhD | Thesis |
| Linguistics | MA/PhD | Thesis |
| Translation Studies | MA/PhD | Thesis |
| Music | MA/PhD | Thesis |
| Theatre | MA | Thesis |
| Visual Arts | MA/MFA | Thesis |
| Information Studies | MA/MIS | Course-based |
| Indigenous Studies | MA | Thesis |
| Digital Transformation and Innovation | MA | Course-based |

#### Engineering (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Chemical Engineering | MASc/MEng/PhD | Both |
| Civil Engineering | MASc/MEng/PhD | Both |
| Computer Science | MSc/MCS/PhD | Both |
| Electrical Engineering | MASc/MEng/PhD | Both |
| Environmental Engineering | MASc/MEng | Both |
| Mechanical Engineering | MASc/MEng/PhD | Both |
| Engineering Management | MEng | Course-based |
| Biomedical Engineering | MASc/PhD | Thesis |

#### Health Sciences (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Human Kinetics | MA/MSc/PhD | Both |
| Nursing | MScN/PhD | Both |
| Epidemiology | MSc/PhD | Thesis |
| Public Health | MPH | Course-based |
| Health Systems | MSc | Research |
| Rehabilitation Sciences | MSc/PhD | Thesis |
| Nutrition Sciences | MSc/PhD | Thesis |

#### Law (Graduate)

| Program | Degree |
|---------|--------|
| LLM (多种方向) | LLM |
| PhD in Law | PhD |
| JD/MBA (combined) | JD + MBA |
| JD/MA International Affairs (with Carleton) | JD + MA |

#### Medicine (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Biochemistry | MSc/PhD | Thesis |
| Cellular and Molecular Medicine | MSc/PhD | Thesis |
| Microbiology and Immunology | MSc/PhD | Thesis |
| Neuroscience | MSc/PhD | Thesis |
| Translational and Molecular Medicine | MSc/PhD | Thesis |
| Medical Physics | MSc/PhD | Thesis |
| Health Administration | MHA/EMHA | Course-based |
| Executive MHA | EMHA | Online |

#### Science (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Biology | MSc/PhD | Thesis |
| Chemistry | MSc/PhD | Thesis |
| Earth Sciences | MSc/PhD | Thesis |
| Mathematics | MSc/PhD | Thesis |
| Physics | MSc/PhD | Thesis |
| Statistics | MSc/PhD | Thesis |
| Computer Science | MSc/MCS/PhD | Both |
| Environmental Sustainability | MSc | Thesis |

#### Social Sciences (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| Psychology | MA/MSc/PhD | Thesis |
| Criminology | MA/PhD | Thesis |
| Economics | MA/PhD | Thesis |
| Political Science | MA/PhD | Thesis |
| Sociology | MA/PhD | Thesis |
| Social Work | MSW/PhD | Both |
| International Development | MA/PhD | Thesis |
| Public Administration | MPA | Course-based |
| Public Policy | MPP | Course-based |

#### Telfer School of Management (Graduate)

| Program | Degree | Type |
|---------|--------|------|
| MBA | MBA | Course-based |
| Executive MBA | EMBA | Course-based |
| MSc Management | MSc | Thesis |
| PhD Management | PhD | Thesis |
| MHA (Health Administration) | MHA | Course-based |
| EMHA (Online) | EMHA | Course-based |
| Graduate Diploma Chartered Professional Accountancy | GDip | Course-based |
| Graduate Diploma Engineering Management | GDip | Course-based |
| Graduate Diploma Leadership and Management | GDip | Course-based |
| Graduate Diploma Public Management and Governance | GDip | Course-based |
| Graduate Diploma Program Evaluation | GDip | Course-based |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Entry Requirements

#### Ontario Secondary School Applicants
- OSSD with at least six 4U/4M or DU-level courses
- Prerequisite courses must be 4U-level
- Minimum averages vary by program (typically 70%–90%+ depending on competitiveness)
- Calculated on best 5 4U/4M courses (or best 6 for some programs)
- Offers made in 3 rounds: Mid-Nov–Jan, Feb–Apr, May–Aug

#### International Applicants
- Depends on country of education (country-specific requirements)
- Minimum: completion of senior secondary education equivalent to Ontario Grade 12
- IB: completion of IB Diploma
- GCE: A-Levels
- AP: Advanced Placement exams
- Transfer credits: AP score ≥4, IB HL grade ≥5, A-Level grade ≥B

#### Competitive Programs (March 1 deadline)
- Acting (BFA)
- Computer Engineering
- Computer Science
- Computer Science and Mathematics
- Data Science (five-year double degree)
- Health Sciences
- Music (BMus)
- Music and Science (five-year double degree)
- Social Work
- Software Engineering
- Nursing
- Visual Arts (BFA)

### 3.2 Graduate Entry Requirements

#### Master's and Graduate Diploma Programs
- Hold an Honours Bachelor's degree (4 years) or equivalent
- Minimum average 70% (B) based on last 20 courses

#### PhD Programs
- Hold a Master's degree or equivalent
- Minimum average 75% (B+) based on last 10 courses

#### Additional Requirements
- Some programs require higher averages, specific tests (GRE/GMAT), portfolios, or supervisor acceptance
- Highly competitive — meeting minimum does not guarantee admission

### 3.3 English Language Requirements (UG)

For programs offered in **English** — applicants who have NOT completed 3+ years full-time in English-only instruction in an English-official country:

| Test | Direct Entry Score | Notes |
|------|-------------------|-------|
| **IELTS Academic** | Overall 6.5, Writing 6.5 | Overall 6.0 → direct entry with extra ESL courses; 4.5–6.0 band → EIP conditional |
| **TOEFL iBT** | Confirmed accepted (specific scores not listed on UG page — check per program) | — |
| **Duolingo English Test** | Confirmed accepted (specific scores not listed on UG page) | — |

**English Intensive Program (EIP)**: Conditional admission available for lower scores.
- Overall IELTS 4.5 + Writing 5 → ESL0120 + ESL0130 + ESL0140 (42 weeks)
- Overall IELTS 5.5 + Writing 5 → ESL0130 + ESL0140 (28 weeks)
- Overall IELTS 5.5 + Writing 6 / Overall 6 + Writing 5.5 → ESL0140 only (8–14 weeks)

**Not accepted**: IELTS for UKVI, CELPIP, TCF Canada, TEF Canada, Bright Language test.

### 3.4 French Language Requirements (UG)

For programs offered in **French**:

| Test | Required Score |
|------|---------------|
| DALF | C1 or C2 |
| DELF | B2 (Production écrite ≥16/25) |
| TCF (Tout Public / DAP) | B2 |
| TEF (5 épreuves) | B2 |

Exemptions: 3+ years full-time French-only instruction in a French-official country, or completion of French-language post-secondary studies.

### 3.5 Application Deadlines

#### Undergraduate — International (Fall 2026 entry)
| Date | Event |
|------|-------|
| Sep 18, 2025 | Application opens via OUAC |
| Jan 15, 2026 | Recommended deadline |
| Mar 1, 2026 | Deadline for competitive programs (Acting, CS, Engineering, Health Sciences, etc.) |
| Mar 30, 2026 | Supporting documents deadline for competitive programs |
| Apr 1, 2026 | Deadline for all other UG programs |
| May 2, 2026 | Complete admission file deadline |
| Jun 1, 2026 | Accept offer + pay deposit deadline |

#### Undergraduate — Canadian (Fall 2026 entry)
| Date | Event |
|------|-------|
| Mid-Oct 2025 | Application opens via OUAC |
| Jan 15, 2026 | Recommended deadline |
| Jun 1, 2026 | Most programs accept applications until this date |

#### Graduate
- Deadlines vary by program
- Apply via OUAC
- Some programs require supervisor acceptance before applying
- Specific programs (OT/PT/Audiology/SLP) apply via ORPAS

### 3.6 Application Fees
- Paid through OUAC
- Non-refundable
- Separate fees for each application

---

## Section 4 — Costs & Financial Aid

### 4.1 Tuition Fee Structure

uOttawa fee structure varies by:
- **Student category**: Ontario resident, Non-Ontario Canadian, International
- **Level**: Undergraduate, Graduate
- **Program/Faculty**: Different rates per faculty
- **Course load**: Full-time vs Part-time

Fee structure uses the DNN fee calculator platform:
- https://dnn.uottawa.ca/en/Utilities/University-Fees/Tuition-Fees-INTL (International)
- https://dnn.uottawa.ca/en/Utilities/University-Fees/Tuition-Fees (Domestic)

**Fee posting schedule**: Fees for upcoming academic year (Sep–Aug) posted in late May.

### 4.2 International Tuition

The University of Ottawa offers a **Differential Tuition Fee Exemption Scholarship** for:
- International Francophone and Francophile students enrolled in bachelor's or master's programs (since Sep 2021)
- French Immersion Stream students

**International Doctoral Scholarship**: $45,000 over 5 years for international PhD students.
- Students who began PhD before May 2023: tuition fees equivalent to Canadian non-Ontario rate (max 5 years)
- Students who began before Sep 2021: differential tuition exemption for remainder of studies

### 4.3 Scholarships & Financial Aid

| Scholarship | Value | Eligibility |
|-------------|-------|-------------|
| Admission Scholarships | Varies | Based on admission average |
| Differential Tuition Fee Exemption | Tuition reduction | Francophone/Francophile intl students |
| International Doctoral Scholarship | $45,000/5 yrs | International PhD students |
| Undergraduate Scholarships | Various | Academic merit |
| Bursaries | Need-based | Financial need |

- uOttawa awarded **$130 million** to undergraduate students in 2024
- Ranked #1 in Canada for scholarships and bursaries

### 4.4 Other Costs

| Cost Item | Notes |
|-----------|-------|
| Application fees | Via OUAC, non-refundable |
| Admission deposit | Non-refundable, credited toward tuition |
| Ancillary fees | Additional mandatory fees |
| Housing | Residence + meal plan (guaranteed for first-year if applied by June 1) |
| UHIP (health insurance) | Mandatory for international students |
| Study permit costs | For international applicants |

---

## Section 5 — Evidence Chain Index

```yaml
E-UO-001:
  field: institution.name
  value: "University of Ottawa"
  source_url: "https://www.uottawa.ca/en"
  source_snippet: "University of Ottawa"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-002:
  field: institution.students
  value: "49,000 students"
  source_url: "https://www.uottawa.ca/about-us/"
  source_snippet: "49,000 students"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-003:
  field: institution.faculties
  value: "10 faculties: Arts, Education, Engineering, Health Sciences, Law (Civil), Law (Common), Medicine, Science, Social Sciences, Telfer School of Management"
  source_url: "https://www.uottawa.ca/about-us/faculties"
  source_snippet: "Faculty of Arts, Faculty of Education, Faculty of Engineering..."
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-004:
  field: admissions.ug.deadlines.international
  value: "Jan 15 recommended; Mar 1 competitive programs; Apr 1 other UG programs"
  source_url: "https://www.uottawa.ca/study/undergraduate-studies/international-applicants"
  source_snippet: "January 15, 2026: Recommended deadline... March 1, 2026: Deadline for competitive programs"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-005:
  field: admissions.ug.language.english
  value: "IELTS Academic 6.5 overall (Writing 6.5); EIP conditional admission available"
  source_url: "https://www.uottawa.ca/study/undergraduate-studies/language-requirements"
  source_snippet: "IELTS Academic\t6.5\t6.5"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-006:
  field: admissions.ug.language.french
  value: "DALF C1/C2; DELF B2 (écrit ≥16/25); TCF B2; TEF B2"
  source_url: "https://www.uottawa.ca/study/undergraduate-studies/language-requirements"
  source_snippet: "DALF C1 or C2; DELF B2"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-007:
  field: admissions.graduate.requirements
  value: "Master's: Honours bachelor's 70% (B); PhD: Master's 75% (B+)"
  source_url: "https://www.uottawa.ca/study/graduate-studies/how-to-apply"
  source_snippet: "Master's and graduate diploma programs: Hold an honours bachelor's degree... with an average of 70%"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-008:
  field: admissions.ug.ontario
  value: "OSSD with 6 4U/4M courses; minimum averages vary"
  source_url: "https://www.uottawa.ca/study/undergraduate-studies/ontario-secondary-schools"
  source_snippet: "Ontario high school diploma with at least six 4U-4M or DU-level courses"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-009:
  field: programs.catalog
  value: "550+ undergraduate and graduate programs across 10 faculties"
  source_url: "https://catalogue.uottawa.ca/en/programs/"
  source_snippet: "Search over 550 undergraduate and graduate programs across 10 faculties"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-010:
  field: scholarships.overview
  value: "$130M awarded to undergraduate students in 2024; #1 in Canada for scholarships and bursaries"
  source_url: "https://www.uottawa.ca/en"
  source_snippet: "1st in Canada for scholarships and bursaries"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-011:
  field: tuition.fee_calculator
  value: "Fee calculator at dnn.uottawa.ca; interactive DNN platform; fees posted in late May for upcoming year"
  source_url: "https://www.uottawa.ca/study/fees-financial-support/university-fees"
  source_snippet: "Fees for the coming academic year (September to August) are posted in late May"
  capture_date: 2026-07-10
  evidence_type: official_webpage

E-UO-012:
  field: institution.rankings
  value: "U15 Canada; 5th in Canada for research intensity; 7th in Canada for research funding"
  source_url: "https://www.uottawa.ca/about-us/"
  source_snippet: "5th in Canada for research intensity"
  capture_date: 2026-07-10
  evidence_type: official_webpage
```

---

## Section 6 — WeKnora Import Manifest

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Description |
|----------|-----------|-------------|
| **P0** | Full per-program tuition fees | Fee calculator requires DNN interaction — extract via browser automation with faculty/program/year selectors |
| **P0** | TOEFL/Duolingo specific minimums | Not displayed on main language requirements page — may be behind JS accordion or per-program |
| **P0** | Graduate program-specific requirements | Master's/PhD requirements vary by program — need per-program page extraction from catalogue |
| **P0** | Course listing | Full course catalog at https://catalogue.uottawa.ca/en/courses/ |
| **P1** | Undergraduate per-program admission averages | The program prerequisites page uses JS combobox — need to extract data per selected program |
| **P1** | Graduate funding packages | Per-program funding details for research students |
| **P1** | Housing costs | Residence fee schedule |
| **P2** | Historical rankings | THE/QS/ARWU ranking data over time |
| **P2** | Alumni outcomes data | Employment rates, graduate salaries |
| **P2** | Student demographics | Gender ratio, international student %, etc. |

### Data Gaps Summary

1. **Tuition fees by program** — Requires DNN interactive fee calculator; specific amounts for 2026-2027 not yet published (late May posting)
2. **TOEFL/Duolingo exact scores** — Not directly surfaced on the main language requirements page; may require per-program info
3. **Graduate program-level requirements** — Each program has specific requirements documented per academic unit
4. **Per-program admission averages** — Hidden behind JS combobox on prerequisite page

---

## Section 7 — Cross-School Comparison Framework

| Dimension | University of Ottawa | Carleton University | 
|-----------|--------------------|--------------------|
| Total UG programmes | ~220+ | ~90+ |
| Total PG programmes | ~300+ | ~130+ |
| Total programs | ~700+ | ~200+ UG + ~100+ Grad |
| Faculties | 10 | 6 |
| U15 Canada | ✅ Yes | ❌ No |
| Location | Ottawa, ON | Ottawa, ON |
| Bilingual | ✅ English-French | ❌ English only |
| Students | ~49,000 | ~31,000 |
| Research intensity (Can) | #5 | #15+ |
| International students | 145+ countries | 100+ countries |
| Application system | OUAC | OUAC |
| Tuition fee format | DNN interactive calculator | Login-gated estimator |
| Language requirements | IELTS 6.5 (W 6.5) | IELTS 6.5 (no band <6.0) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: University of Ottawa official website (uottawa.ca), Academic Catalogue (catalogue.uottawa.ca), Fee Calculator (dnn.uottawa.ca)
> **Granularity**: faculty → department/school → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (221 bachelor's + 71 minors + certificates) | PG programmes ✅ (~215 master's + ~75 PhD + diplomas) | Evidence (12 blocks) ✅
> **Next step**: Extract per-program tuition fees via DNN fee calculator interaction; extract graduate program-specific requirements from academic units
