# Singapore Management University (SMU) — 知识库完整深度数据

> **Data capture date**: 2026-07-09
> **Capture tool**: ego-browser (browser_navigate + JS extraction)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Singapore (SG)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 11 |
| 研究生授课型项目 (Masters taught) | 18 |
| 研究型硕士项目 (Master by Research) | 4 |
| 博士项目 (PhD / Academic Research) | 12 |
| 专业博士项目 (Professional Doctorate) | 8 |
| 学位项目总计 | 53 |
| 学院 (Schools/Colleges) | 8 |
| 学术院系 (Academic Schools/Colleges) | 8 |

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Singapore Management University (SMU)
├── College of Integrative Studies (CIS)
├── College of Graduate Research Studies (CGRS)      [oversees research programmes]
├── Lee Kong Chian School of Business (LKCSB)
├── School of Accountancy (SOA)
├── School of Computing and Information Systems (SCIS)
├── School of Economics (SOE)
├── School of Social Sciences (SOSS)
└── Yong Pung How School of Law (YPHSL)
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学历级别 | 数量 |
|----------|------|
| Bachelor (BAcc, BBM, BSc, LLB, BSocSc) | 11 |
| Master (Taught: MPA, MSc, MBA, EMBA, JD, LLM, MST, MITB, etc.) | 18 |
| Master by Research (MPhil, MSc) | 4 |
| Doctor of Philosophy (PhD) | 12 |
| Professional Doctorate (DBA, EngD, DLCG) | 8 |
| **总计** | **53** |

### 0.4 分布矩阵 (Rule 4 — Distribution Cross-Tab)

| 学院 | Bachelor | Master (Taught) | Master by Research | PhD | Professional Doctorate | **Total** |
|------|----------|-----------------|--------------------|-----|-----------------------|-----------|
| College of Integrative Studies | 1 | — | 1 | 1 | — | **3** |
| College of Graduate Research Studies | — | — | — | — | — | **0** |
| Lee Kong Chian School of Business | 1 | 9 | — | 5 | 4 | **19** |
| School of Accountancy | 1 | 2 | — | 1 | 1 | **5** |
| School of Computing & Information Systems | 4 | 1 | 1 | 2 | 1 | **9** |
| School of Economics | 1 | 3 | 1 | 1 | 1 | **7** |
| School of Social Sciences | 1 | — | 1 | 1 | — | **3** |
| Yong Pung How School of Law | 1 | 2 | — | 1 | 1 | **5** |
| Partnership (SMU × Duke-NUS) | 1 | — | — | — | — | **1** |
| Cross-school (CIS & SOSS) | — | 1 | — | — | — | **1** |
| **Total** | **11** | **18** | **4** | **12** | **8** | **53** |

---

## Section 1 — Undergraduate Education

### 1.1 College of Integrative Studies

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Integrative Studies | BIS | College of Integrative Studies | https://admissions.smu.edu.sg/programmes/college-integrative-studies |

### 1.2 School of Accountancy

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Accountancy | BAcc | School of Accountancy | https://admissions.smu.edu.sg/programmes/school-accountancy |

### 1.3 Lee Kong Chian School of Business

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Business Management | BBM | Lee Kong Chian School of Business | https://admissions.smu.edu.sg/programmes/lee-kong-chian-school-business |

### 1.4 School of Economics

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Science (Economics) | BSc | School of Economics | https://admissions.smu.edu.sg/programmes/school-economics |

### 1.5 School of Computing and Information Systems

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Science (Information Systems) | BSc | School of Computing and Information Systems | https://admissions.smu.edu.sg/programmes/school-computing-and-information-systems/bsc-information-systems-curriculum |
| Bachelor of Science (Computer Science) | BSc | School of Computing and Information Systems | https://admissions.smu.edu.sg/programmes/school-computing-and-information-systems/bsc-it-solution-development-major-curriculum |
| Bachelor of Science (Computing & Law) | BSc | School of Computing and Information Systems | https://admissions.smu.edu.sg/programmes/school-computing-and-information-systems/bsc-computing-law-curriculum |
| Bachelor of Science (Software Engineering) | BSc | School of Computing and Information Systems | https://admissions.smu.edu.sg/programmes/school-computing-and-information-systems/bsc-software-engineering-wsdeg |

### 1.6 Yong Pung How School of Law

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Laws | LLB | Yong Pung How School of Law | https://admissions.smu.edu.sg/programmes/yong-pung-how-school-law |

### 1.7 School of Social Sciences

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| Bachelor of Social Science | BSocSc | School of Social Sciences | https://admissions.smu.edu.sg/programmes/school-social-sciences |

### 1.8 Partnership

| Program Name | Degree Type | School | URL |
|-------------|-------------|--------|-----|
| SMU–Duke-NUS Medicine Pathway | Special | SMU × Duke-NUS | https://admissions.smu.edu.sg/programmes/smu-duke-nus-medicine-pathway |

---

## Section 2 — Graduate Education

### 2.1 Taught Master's Programmes

#### School of Accountancy

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| Master of Professional Accounting | MPA | 18 mo (FT, flex 12 mo), 24 mo (PT) | FT/PT | https://masters.smu.edu.sg/programmes |
| MSc in Accounting (Data & Analytics) | MSA | 18 mo (FT, flex 12 mo), 24 mo (PT) | FT/PT | https://masters.smu.edu.sg/programmes |

#### Lee Kong Chian School of Business

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| Chinese Executive MBA | CEMBA | 24 mo (Modular) | Modular | https://masters.smu.edu.sg/programmes |
| Executive MBA | EMBA | 15 mo (FT, flex 12 mo) | Modular | https://masters.smu.edu.sg/programmes |
| Master of Business Administration | MBA | 15 mo (FT, flex 10 mo), 20 mo (PT, flex 15 mo) | FT/PT | https://masters.smu.edu.sg/programmes |
| MSc in Management | MiM | 18 mo (FT) | FT | https://masters.smu.edu.sg/programmes |
| MSc in Applied Finance | MAF | 18 mo (FT), 24 mo (PT) | FT/PT | https://masters.smu.edu.sg/programmes |
| MSc in Quantitative Finance | MQF | 18 mo (FT), 24 mo (PT) | FT/PT | https://masters.smu.edu.sg/programmes |
| MSc in Wealth Management | MWM | 12 mo (Modular) | Modular | https://masters.smu.edu.sg/programmes |
| MSc in Entrepreneurship & Innovation | MEI | 12 mo (FT) | FT | https://masters.smu.edu.sg/programmes |
| Master of Science in Business AI | MBAI | 12 mo (FT) | FT | https://masters.smu.edu.sg/programmes |

#### School of Economics

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| MSc in Economics | MSE | 1.5 yr (FT, flex 1 yr), 2.5 yr (PT, flex 2 yr) | FT/PT | https://masters.smu.edu.sg/programmes |
| Master of Data Science in Economics | MDSE | 1.5 yr (FT, flex 1 yr), 2.5 yr (PT, flex 2 yr) | FT/PT | https://masters.smu.edu.sg/programmes |
| MSc in Financial Economics | MSFE | 1.5 yr (FT, flex 1 yr), 2.5 yr (PT, flex 2 yr) | FT/PT | https://masters.smu.edu.sg/programmes |

#### School of Computing & Information Systems

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| Master of IT in Business | MITB | 1.5 yr (FT, flex 1 yr), 2.5 yr (PT, flex 2 yr) | FT/PT | Tracks: Cybersecurity, Data Science & Analytics, AI, Digital Transformation, FinTech & Analytics |

#### Yong Pung How School of Law

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| Juris Doctor | JD | 3 yr (FT) | FT | https://masters.smu.edu.sg/programmes |
| Master of Laws | LLM | 1 yr (FT), 2 yr (PT) | FT/PT | https://masters.smu.edu.sg/programmes |

#### College of Integrative Studies & School of Social Sciences

| Program Name | Degree | Duration | Mode | URL/Notes |
|-------------|--------|----------|------|-----------|
| Master of Sustainability | MST | 18 mo (FT, flex 11 mo), 30 mo (PT, flex 23 mo) | FT/PT | https://masters.smu.edu.sg/programmes |

### 2.2 Master by Research Programmes

| Program Name | Degree | School | URL/Notes |
|-------------|--------|--------|-----------|
| Master of Philosophy in Economics | MPhil | School of Economics | https://graduatestudies.smu.edu.sg/ |
| Master of Philosophy in Psychology | MPhil | School of Social Sciences | https://graduatestudies.smu.edu.sg/ |
| Master of Science in Computing | MSc | School of Computing & Information Systems | https://graduatestudies.smu.edu.sg/ |
| Master of Philosophy in Asian Urbanisms | MPhil | College of Integrative Studies | https://graduatestudies.smu.edu.sg/ |

### 2.3 PhD (Academic Research) Programmes

| Program Name | School | URL/Notes |
|-------------|--------|-----------|
| PhD in Accounting | School of Accountancy | https://graduatestudies.smu.edu.sg/ |
| PhD in Business (Finance) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| PhD in Business (Marketing) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| PhD in Business (Operations Management) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| PhD in Business (Organisational Behaviour & HR) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| PhD in Business (Strategy & Entrepreneurship) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| PhD in Economics | School of Economics | https://graduatestudies.smu.edu.sg/ |
| PhD in Computer Science | School of Computing & Information Systems | https://graduatestudies.smu.edu.sg/ |
| PhD in Information Systems | School of Computing & Information Systems | https://graduatestudies.smu.edu.sg/ |
| PhD in Psychology | School of Social Sciences | https://graduatestudies.smu.edu.sg/ |
| PhD in Law, Commerce and Technology | Yong Pung How School of Law | https://graduatestudies.smu.edu.sg/ |
| PhD in Asian Urbanisms | College of Integrative Studies | https://graduatestudies.smu.edu.sg/ |

### 2.4 Professional Doctorate Programmes

| Program Name | Degree | School | URL/Notes |
|-------------|--------|--------|-----------|
| PhD in Business (General Management) | PhD (Professional) | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| Doctor of Business Administration | DBA | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| CKGSB–SMU Doctor of Business Administration | DBA | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| SJTU–SMU Doctor of Business Administration | DBA | Lee Kong Chian School of Business | https://graduatestudies.smu.edu.sg/ |
| SMU–PHBS Doctor of Business Administration | DBA | School of Economics | https://graduatestudies.smu.edu.sg/ |
| SMU–ZJU DBA (Accounting & Finance) | DBA | School of Accountancy | https://graduatestudies.smu.edu.sg/ |
| Doctor of Engineering | EngD | School of Computing & Information Systems | https://graduatestudies.smu.edu.sg/ |
| Doctor of Law and Commercial Governance | DLCG | Yong Pung How School of Law | https://graduatestudies.smu.edu.sg/ |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admissions

#### Application Timeline (AY2026/27)

| Event | Date |
|-------|------|
| Application Opening | 17 November 2025, 12:00pm SGT |
| Application Closing | 19 March 2026, 11:59pm SGT |
| Standardised Test Score Submission Deadline | 31 March 2026 |
| Interview Notification (shortlisted) | January – July 2026 |
| Law Writing Test (shortlisted, applied by 10 Mar) | 14 March 2026 (in-person) |
| Law Writing Test (shortlisted, after 10 Mar) | 27 or 29 March 2026 |
| Law Interview (further shortlisted) | 28 Mar, 4 Apr, 11 Apr, 13–18 Apr 2026 |
| Notification of Application Outcome | February – July 2026 |
| 1st Window Acceptance | 2 January – 25 May 2026 |
| 2nd Window Acceptance | 1 June – 16 June 2026 |
| Matriculation | June – July 2026 |
| Orientation | July – August 2026 |
| Classes Start | 17 August 2026 |

#### Entry Requirements by Qualification

**Singapore-Cambridge GCE A-Levels:**
- Holistic admissions based on grades + aptitude + attitude
- Indicative Grade Profile (2025 intake, 10th–90th percentile):
  - Accountancy: BBB/C – AAA/A
  - Business Management: ABB/C – AAA/A
  - Laws: AAA/A – AAA/A
  - Economics: BBB/C – AAA/A
  - Information Systems: BBC/C – AAA/B
  - Computer Science: AAB/B – AAA/A
  - Computing & Law: ABB/A – AAA/A
  - Software Engineering: BBC/B – AAA/C
  - Social Sciences: BBB/C – AAA/A
  - Integrative Studies: ABB/A – AAA/A

**Polytechnic Diploma (from Singapore polytechnics):**
- Indicative GPA range (10th–90th percentile, 2025 intake):
  - Accountancy: 3.71 – 3.94
  - Business Management: 3.78 – 3.95
  - Laws: 3.73 – 3.97
  - Economics: 3.65 – 3.91
  - Information Systems: 3.61 – 3.89
  - Computer Science: 3.80 – 3.98
  - Software Engineering: 3.67 – 3.93
  - Social Sciences: 3.65 – 3.89
  - Integrative Studies: 3.73 – 3.95

**International & Other Qualifications:**
- Minimum 12 years of formal education with good passes in a recognised national/international examination
- Accepted qualifications include: Australian High School, Bangladeshi HSC, Brunei A-Levels, Canadian Diploma, European Baccalaureate, French Baccalaureate, Gao Kao (NCEE), German Abitur, HKDSE, India Standard 12, Indonesian SMA, Italian Diploma, Malaysia STPM/UEC, Mauritius HSC, Myanmar High School, NCEA Level 3 (NZ), Philippines High School, South Korea CSAT, Sri Lanka A-Levels, Swiss Matura, Taiwan Senior High, Thailand Mathayom 6, Turkish High School, UK A-Levels, US High School Diploma, Vietnam Graduation Exam

#### English Language / Standardised Test Requirements

**For non-Law programmes:**

| Test | Minimum Score |
|------|---------------|
| SAT | 1350 total (≥650 Evidence-Based Reading & Writing) |
| ACT | 29 composite (≥57 English + Reading) |
| IELTS (Academic) | 7.0 overall (≥7.0 Reading, ≥6.5 Writing) |
| TOEFL iBT | 93 (≥22 Reading, ≥22 Writing) |
| C1 Advanced | 185 overall (≥185 Reading, ≥176 Writing) |
| PTE Academic | 66 overall (≥66 Reading, ≥56 Writing) |
| AST (English) | 225 |
| Duolingo English Test | Not listed |

**For Law programme:**

| Test | Minimum Score |
|------|---------------|
| SAT | 1350 total (≥700 Evidence-Based Reading & Writing) |
| ACT | 29 composite (≥64 English + Reading) |
| IELTS (Academic) | 7.5 overall (≥7.0 Reading, ≥7.0 Writing) |
| TOEFL iBT | 100 (≥24 Reading, ≥24 Writing) |
| C1 Advanced | 191 overall (≥185 Reading, ≥185 Writing) |
| PTE Academic | 76 overall (≥76 Reading, ≥66 Writing) |
| AST (English) | 240 |

Note: SAT/ACT/IELTS/TOEFL/C1 Advanced/PTE/AST not required for IB Diploma, LASALLE, NAFA, and NIE diploma holders.

### 3.2 Postgraduate Admissions

#### Taught Master's Key Deadlines

| Programme | Intake | Application Deadline |
|-----------|--------|---------------------|
| MPA, MSA | Aug | May |
| CEMBA | Jan | 1 Nov (prior year) |
| EMBA | Aug | May |
| MBA | Jan/Aug | Nov/May |
| MiM | Jan/Aug | Nov/May |
| MAF, MQF, MWM, MEI, MBAI | Aug | May |
| MSE, MDSE, MSFE | Aug/Jan | June/Nov |
| MITB | Aug/Jan | May/Oct |
| JD | Aug | May |
| LLM | Aug | May |
| MST | Aug | May |

#### PhD / Research Programme Entry
- Requires strong academic background in relevant discipline
- Scholarships, fellowships and assistantships available
- Specific requirements vary by programme — refer to individual programme page

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition Fees (AY2026/27 Entering Freshmen)

**Annual Tuition Fees (Regular Term 1 & 2):**

| Degree | Singapore Citizen (Subsidised) | Singapore PR (Subsidised) | ASEAN International (Subsidised, incl. GST) | Other International (Subsidised, incl. GST) | Non-Subsidised (incl. GST) |
|--------|------|------|-------|-------|------|
| Most UG programmes* | S$11,550 | S$16,100 | S$25,150 | S$26,200 | S$47,700 |
| Bachelor of Laws | S$12,750 | S$17,800 | S$27,750 | S$30,450 | S$56,150 |

*Bachelor of Accountancy, Business Management, Integrative Studies, BSc (Economics), BSc (Computing & Law), BSc (Computer Science), BSc (Software Engineering), BSc (Information Systems), Bachelor of Social Sciences

**Special Term (Term 3) per course:**

| Degree | Singapore Citizen | Singapore PR | ASEAN International | Other International | Non-Subsidised |
|--------|------|------|-------|-------|------|
| Most UG programmes | S$1,155 | S$1,610 | S$2,515 | S$2,620 | S$4,770 |
| Bachelor of Laws | S$1,275 | S$1,780 | S$2,775 | S$3,045 | S$5,615 |

**Annual Miscellaneous Student Fees (2025):**

| Item | SC/SPR | International |
|------|--------|---------------|
| Student Activities | S$80 | S$80 |
| Insurance | S$129 | S$193 |
| IT Facilities | S$18 | S$18 |
| **Total** | **S$227** | **S$291** |

**Tuition Grant:**
- Singapore Citizens: automatically awarded Tier A (highest subsidy), no bond
- Singapore PRs: may apply for Tier B, 3-year work bond in Singapore entity upon graduation
- International students: may apply for Tier C (limited, merit-based), 3-year work bond in Singapore entity upon graduation
- Fixed fee model: fees remain unchanged throughout normal 4-year duration

### 4.2 Postgraduate Tuition (Masters Programmes)
- Up to 40% tuition fee discount for selected 2025 intakes (SMU 25th anniversary)
- SkillsFuture Level-Up Programme: S$4,000 top-up for Singaporeans aged 40+
- Education loans from partner banks available

### 4.3 Financial Aid
- SMU ACCESS PLUS: Most generous financial aid scheme — covers 100% of tuition fees for eligible Singapore Citizens
- Close to 40% of all students receive a scholarship or financial award
- 100% need-blind admissions
- Hundreds of scholarships and financial awards available

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Capture Date |
|----|-------|-------|------------|--------------|
| E-U-001 | institution.name | Singapore Management University | https://www.smu.edu.sg/ | 2026-07-09 |
| E-U-002 | school.hierarchy | 8 schools listed in footer | https://www.smu.edu.sg/ | 2026-07-09 |
| E-U-003 | ug.programmes.list | 11 UG programmes | https://www.smu.edu.sg/education/undergraduates | 2026-07-09 |
| E-U-004 | ug.programme.details | Bachelor of Accountancy, BBM, etc. | https://admissions.smu.edu.sg/programmes/ | 2026-07-09 |
| E-U-005 | pg.taught.list | 18 Masters programmes | https://www.smu.edu.sg/education/postgraduates | 2026-07-09 |
| E-U-006 | phd.list | 12 PhD programmes | https://www.smu.edu.sg/education/postgraduates | 2026-07-09 |
| E-U-007 | prof.doctorate.list | 8 Professional Doctorates | https://www.smu.edu.sg/education/postgraduates | 2026-07-09 |
| E-U-008 | masters.by.research.list | 4 MPhil/MSc programmes | https://www.smu.edu.sg/education/postgraduates | 2026-07-09 |
| E-U-009 | masters.details | Masters programme durations & deadlines | https://masters.smu.edu.sg/programmes | 2026-07-09 |
| E-U-010 | ug.application.dates | AY2026/27 timeline | https://admissions.smu.edu.sg/admissions-requirements/important-dates | 2026-07-09 |
| E-U-011 | ug.entry.requirements | Qualification types + requirements | https://admissions.smu.edu.sg/admissions-requirements/international-and-other-qualifications | 2026-07-09 |
| E-U-012 | min.test.scores.nonlaw | SAT 1350, IELTS 7.0, TOEFL 93 etc. | https://admissions.smu.edu.sg/admissions-requirements/international-and-other-qualifications | 2026-07-09 |
| E-U-013 | min.test.scores.law | SAT 1350 (700 EBW), IELTS 7.5, TOEFL 100 etc. | https://admissions.smu.edu.sg/admissions-requirements/international-and-other-qualifications | 2026-07-09 |
| E-U-014 | igp.a-level | Indicative grade profile by programme | https://admissions.smu.edu.sg/admissions-requirements/indicative-grade-profile | 2026-07-09 |
| E-U-015 | igp.poly | Polytechnic GPA ranges | https://admissions.smu.edu.sg/admissions-requirements/indicative-grade-profile | 2026-07-09 |
| E-U-016 | course.places.2025 | Programme places taken up 2025 | https://admissions.smu.edu.sg/admissions-requirements/indicative-grade-profile | 2026-07-09 |
| E-U-017 | tuition.fees.ug | AY2026/27 fee table | https://admissions.smu.edu.sg/financial-matters/tuition-fees-grant | 2026-07-09 |
| E-U-018 | tuition.grant | MOE Tuition Grant details | https://admissions.smu.edu.sg/financial-matters/tuition-fees-grant | 2026-07-09 |
| E-U-019 | misc.fees | Annual miscellaneous fees | https://admissions.smu.edu.sg/financial-matters/tuition-fees-grant | 2026-07-09 |
| E-U-020 | financial.aid | SMU ACCESS PLUS, need-blind admissions | https://admissions.smu.edu.sg/financial-matters/financial-aid | 2026-07-09 |
| E-U-021 | majors.and.tracks | Full list of 1st/2nd majors per school | https://admissions.smu.edu.sg/programmes/majors-and-tracks-offered-smu | 2026-07-09 |
| E-U-022 | graduate.research.studies | CGRS overview + programme list | https://graduatestudies.smu.edu.sg/ | 2026-07-09 |

---

## Section 6 — WeKnora Import Manifest

### 6.1 Follow-up Data Items

| Priority | Data Item | Notes |
|----------|-----------|-------|
| **P0** | Full tuition fees for Masters programmes | Available on per-programme pages; not centrally listed |
| **P0** | PhD/Professional Doctorate tuition & funding details | Per-programme pages needed |
| **P0** | Scholarships listing (by name, value, eligibility) | Brochure available at admissions.smu.edu.sg |
| **P1** | Detailed programme curriculum/study plan for each major | Available on individual programme pages |
| **P1** | Campus housing costs and options | References found at /about/facilities/campus-housing |
| **P2** | Student visa process for international students | Referenced at admissions.smu.edu.sg/international-students |
| **P2** | Career outcomes / Graduate Employment Survey data | GES Flyer PDF available |
| **P2** | QS/FT rankings data | Mentioned on site (QS 5th in Asia MBA 2025) |

### 6.2 Data Quality Assessment

| Dimension | Status |
|-----------|--------|
| Programme count — UG | ✅ Complete (11 programmes) |
| Programme count — PG Taught | ✅ Complete (18 programmes) |
| Programme count — PG Research | ✅ Complete (4 MPhil + 12 PhD) |
| Programme count — Prof Doctorate | ✅ Complete (8 programmes) |
| Distribution matrix reconciled | ✅ Verified (53 total) |
| Tuition fees — UG | ✅ Complete (AY2026/27) |
| Tuition fees — PG | ⚠️ Partial (per-programme scholarships noted, exact fees on programme pages) |
| Application deadlines — UG | ✅ Complete |
| Application deadlines — PG | ⚠️ Partial (some deadlines from masters page) |
| Language requirements | ✅ Complete |
| Admission requirements | ✅ Complete (all qualification types) |
| Evidence chain | ✅ Complete (22 evidence blocks) |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | SMU (Singapore) | NUS (Singapore) | NTU (Singapore) |
|-----------|----------------|-----------------|-----------------|
| City | Singapore | Singapore | Singapore |
| Total UG programmes | 11 | — | — |
| Total PG programmes | 42 | — | — |
| Schools/Colleges | 8 | — | — |
| Tuition (SC, UG/yr) | S$11,550–12,750 | — | — |
| Tuition (Intl, UG/yr) | S$26,200–30,450 | — | — |
| Special Features | Holistic admissions, guaranteed 2nd major, 100% global exposure, city campus | — | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: SMU official website (smu.edu.sg, admissions.smu.edu.sg, masters.smu.edu.sg, graduatestudies.smu.edu.sg)
> **Granularity**: school → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (11/11) | PG programmes ✅ (42/42) | Evidence (22 blocks) ✅
> **Next step**: Verify Masters tuition fees on individual programme pages; extract scholarship brochure data
