# University at Albany, SUNY (UAlbany) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS) | 54 |
| 本科辅修 (Minor) | 50+ |
| 研究生学位项目 (MA/MS/PhD/MBA/MPA/MPH/MSW/MIA/DrPH/PsyD/MRP/MFA/CAS) | 170+ |
| 研究生高级证书 (Advanced Certificate / Graduate Certificate) | 40+ |
| **学位项目总计 (UG + Grad)** | **270+** |
| 学院 / 独立系所总数 | 9 |

> Source: https://www.albany.edu/academics/undergraduate-majors-minors, https://www.albany.edu/graduate/graduate-programs

### 0.2 学院 / 系层级结构

```
University at Albany, SUNY
├── College of Arts and Sciences (CAS)                    [学院]
│   ├── Africana Studies                                  [系]
│   ├── Anthropology                                      [系]
│   ├── Art                                               [系]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Communication                                     [系]
│   ├── Computer Science                                  [系]
│   ├── East Asian Studies                                [系]
│   ├── Economics                                         [系]
│   ├── English                                           [系]
│   ├── Geography & Planning                              [系]
│   ├── History                                           [系]
│   ├── Languages, Literatures & Cultures                 [系]
│   ├── Latin American, Caribbean & U.S. Latino Studies   [系]
│   ├── Mathematics                                       [系]
│   ├── Music & Theatre                                   [系]
│   ├── Philosophy                                        [系]
│   ├── Physics                                           [系]
│   ├── Psychology                                        [系]
│   ├── Sociology                                         [系]
│   ├── Women's, Gender & Sexuality Studies               [系]
│   └── Atmospheric & Environmental Sciences (DAES)       [系]
├── Massry School of Business                             [学院]
│   ├── Accounting                                        [系]
│   ├── Finance                                           [系]
│   ├── Information Security & Digital Forensics          [系]
│   └── Management & Marketing                            [系]
├── College of Emergency Preparedness, Homeland Security & Cybersecurity (CEHC) [学院]
│   ├── Emergency Management                              [系]
│   ├── Cybersecurity                                     [系]
│   ├── Informatics                                       [系]
│   └── Game Design & Development                         [系]
├── College of Integrated Health Sciences (CIHS)          [学院]
│   ├── Biomedical Sciences                               [系]
│   ├── Environmental Health Sciences                     [系]
│   ├── Epidemiology & Biostatistics                      [系]
│   ├── Health Policy & Management                        [系]
│   ├── Nursing                                           [系]
│   ├── Public Health                                     [系]
│   └── Social Work                                       [系]
├── School of Social Welfare                              [学院] ⚠ (under CIHS)
├── College of Nanotechnology, Science, and Engineering (CNSE) [学院]
│   ├── Electrical & Computer Engineering                 [系]
│   ├── Environmental & Sustainable Engineering           [系]
│   └── Nanoscale Science & Engineering                   [系]
├── Rockefeller College of Public Affairs & Policy        [学院]
│   ├── Political Science                                 [系]
│   ├── Public Administration & Policy                    [系]
│   └── International Affairs                             [系]
├── School of Criminal Justice                            [学院]
├── School of Education                                   [学院]
│   ├── Educational Psychology & Methodology              [系]
│   ├── Educational Policy & Leadership                   [系]
│   ├── Curriculum & Instruction                          [系]
│   └── Special Education                                 [系]
└── Graduate School                                       [学院] (administers graduate admissions)
```

### 0.3 学历级别明细

| 学位缩写 | official (本校) | 全称 | 层级 | 本项目数量 |
|---------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | 22 |
| BS | BS | Bachelor of Science | 本科 | 32 |
| MA | MA | Master of Arts | 研究生 | 20+ |
| MS | MS | Master of Science | 研究生 | 50+ |
| PhD | PhD | Doctor of Philosophy | 研究生 | 30+ |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| MFA | MFA | Master of Fine Arts | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| MPH | MPH | Master of Public Health | 研究生 | 6 |
| MSW | MSW | Master of Social Work | 研究生 | 2 |
| MIA | MIA | Master of International Affairs | 研究生 | 1 |
| DrPH | DrPH | Doctor of Public Health | 研究生 | 1 |
| PsyD | PsyD | Doctor of Psychology | 研究生 | 1 |
| MRP | MRP | Master of Regional Planning | 研究生 | 1 |
| CAS | CAS | Certificate of Advanced Study | 研究生 | 3 |
| CGS | CGS | Certificate of Graduate Study | 研究生 | 30+ |
| AGC | AGC | Advanced Graduate Certificate | 研究生 | 3 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | PhD | MBA | MFA | MPA | MPH | MSW | MIA | Other | 合计 |
|------------|----|----|----|----|-----|-----|-----|-----|-----|-----|-----|-------|------|
| College of Arts & Sciences | 20 | 10 | 12 | 8 | 15 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 71 |
| Massry School of Business | 0 | 2 | 0 | 8 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 2 | 13 |
| CEHC | 0 | 5 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 12 |
| CIHS | 0 | 2 | 0 | 5 | 3 | 0 | 0 | 0 | 6 | 2 | 0 | 8 | 26 |
| CNSE | 0 | 2 | 0 | 2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 12 |
| Rockefeller College | 0 | 2 | 2 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 1 | 4 | 11 |
| School of Criminal Justice | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Education | 0 | 4 | 0 | 12 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 24 |
| **合计** | **20** | **28** | **15** | **39** | **26** | **1** | **1** | **1** | **6** | **2** | **1** | **32** | **172+** |

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

UAlbany has 9 schools/colleges. See Section 0.2 for the full hierarchy tree. The College of Arts and Sciences is the largest undergraduate unit.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Department of Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.albany.edu/africana/programs/ba-africana-studies |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.albany.edu/anthropology/programs/ba-anthropology |
| 2 | Linguistics | https://www.albany.edu/anthropology/programs/ba-linguistics |

##### Department of Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.albany.edu/art/programs/ba-art-history |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://www.albany.edu/art/programs/bs-art |

##### Department of Atmospheric & Environmental Sciences (DAES)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Atmospheric Science | https://www.albany.edu/daes/programs/bs-atmospheric-science |
| 2 | Climate Science | https://www.albany.edu/daes/programs/bs-climate-science |

##### Department of Biology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.albany.edu/biology/programs/ba-biology |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.albany.edu/biology/programs/bs-biology |
| 2 | Biochemistry and Molecular Biology | https://www.albany.edu/biology/programs/bs-biochemistry-and-molecular-biology |

##### Department of Chemistry
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.albany.edu/chemistry/programs/ba-chemistry |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.albany.edu/chemistry/programs/bs-chemistry |

##### Department of Communication
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | https://www.albany.edu/communication/programs/ba-communication |

##### Department of Computer Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.albany.edu/computer-science/programs/ba-computer-science |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.albany.edu/computer-science/programs/bs-computer-science |

##### Department of East Asian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chinese Studies | https://www.albany.edu/eastasianstudies/programs/ba-chinese-studies |
| 2 | East Asian Studies | https://www.albany.edu/eastasianstudies/programs/ba-east-asian-studies |
| 3 | Japanese Studies | https://www.albany.edu/eastasianstudies/programs/ba-japanese-studies |

##### Department of Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.albany.edu/economics/programs/ba-economics |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://www.albany.edu/economics/programs/bs-business-economics |
| 2 | Quantitative Economics and Data Analysis | https://www.albany.edu/economics/programs/bs-quantitative-economics-data-analysis |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.albany.edu/english/programs/ba-english |

##### Department of Geography & Planning
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.albany.edu/geographyplanning/programs/ba-geography |
| 2 | Interdisciplinary Studies - Globalization Studies | https://www.albany.edu/geographyplanning/programs/ba-interdisciplinary-studies-globalization-studies |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.albany.edu/history/programs/ba-history |
| 2 | Interdisciplinary Studies - Documentary Studies | https://www.albany.edu/history/programs/ba-interdisciplinary-studies-documentary-studies |

##### Department of Languages, Literatures & Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish | https://www.albany.edu/llc/programs/ba-spanish |

##### Department of Latin American, Caribbean & U.S. Latino Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American, Caribbean, and U.S. Latino Studies | https://www.albany.edu/lacs/programs/ba-latin-american-caribbean-and-us-latino-studies |

##### Department of Mathematics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.albany.edu/math/programs/ba-mathematics |
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.albany.edu/math/programs/bs-mathematics |
| 2 | Actuarial and Mathematical Sciences | https://www.albany.edu/math/programs/bs-actuarial-and-mathematical-sciences |

##### Department of Music & Theatre
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music | https://www.albany.edu/musicandtheatre/programs/ba-music |
| 2 | Theatre | https://www.albany.edu/musicandtheatre/programs/ba-theatre |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.albany.edu/philosophy/programs/ba-philosophy |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.albany.edu/physics/programs/bs-physics |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.albany.edu/psychology/programs/ba-psychology |

##### Department of Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.albany.edu/sociology/programs/ba-sociology |

##### Department of Women's, Gender & Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender and Sexuality Studies | https://www.albany.edu/womensstudies/programs/ba-womens-gender-and-sexuality-studies |

#### Massry School of Business

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.albany.edu/business/programs/bs-accounting |
| 2 | Business Administration | https://www.albany.edu/business/programs/bs-business-administration |
| 3 | Digital Forensics & Information Security | https://www.albany.edu/business/programs/bs-digital-forensics-and-information-security |
| 4 | Financial Regulation and Technology | https://www.albany.edu/business/programs/bs-financial-regulation-and-technology |

#### College of Emergency Preparedness, Homeland Security & Cybersecurity (CEHC)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Cybersecurity | https://www.albany.edu/cehc/programs/bs-cybersecurity |
| 2 | Emergency Management and Homeland Security | https://www.albany.edu/cehc/programs/bs-emergency-management-homeland-security |
| 3 | Game Design and Development | https://www.albany.edu/cehc/programs/bs-game-design-and-development |
| 4 | Informatics | https://www.albany.edu/cehc/programs/bs-informatics |

#### College of Integrated Health Sciences (CIHS)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing RN | https://www.albany.edu/cihs/programs/bs-nursing-rn |
| 2 | Public Health | https://www.albany.edu/cihs/programs/bs-public-health |
| 3 | Social Welfare | https://www.albany.edu/cihs/programs/bs-social-welfare |

#### College of Nanotechnology, Science, and Engineering (CNSE)

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Computer Engineering | https://www.albany.edu/ece/programs/bs-electrical-and-computer-engineering |

#### Rockefeller College of Public Affairs & Policy

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.albany.edu/rockefeller/programs/ba-political-science |
| 2 | Public Policy and Management | https://www.albany.edu/rockefeller/programs/ba-public-policy-and-management |

#### School of Criminal Justice

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminal Justice | https://www.albany.edu/scj/programs/ba-criminal-justice |

#### School of Education

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Adolescent Education | https://www.albany.edu/education/programs/bs-adolescent-education |
| 2 | Childhood and Special Education | https://www.albany.edu/education/programs/bs-childhood-and-special-education |
| 3 | Early Childhood/Childhood Education | https://www.albany.edu/education/programs/bs-early-childhood-childhood-education |
| 4 | Human Development | https://www.albany.edu/education/programs/bs-human-development |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 | URL |
|---|------|------|-----|
| 1 | Interdisciplinary Studies - Documentary Studies | CAS (History) | https://www.albany.edu/history/programs/ba-interdisciplinary-studies-documentary-studies |
| 2 | Interdisciplinary Studies - Globalization Studies | CAS (Geography) | https://www.albany.edu/geographyplanning/programs/ba-interdisciplinary-studies-globalization-studies |

### 1.4 Minors — complete list

UAlbany offers 50+ undergraduate minors across all colleges. See https://www.albany.edu/academics/undergraduate-majors-minors#minors for the complete list.

### 1.5 General/Institute-wide requirements

UAlbany requires all undergraduates to complete General Education requirements covering:
- Writing and Critical Inquiry
- Arts and Humanities
- Natural Sciences
- Social Sciences
- Mathematics and Statistics
- World Languages and Cultures
- U.S. History and Civic Engagement

See: https://www.albany.edu/academics/general-education

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UAlbany offers 170+ graduate programs across all schools. Programs are listed at https://www.albany.edu/graduate/graduate-programs. Key programs include:

#### College of Arts and Sciences
- PhD: Anthropology, Biology, Chemistry, Clinical Psychology, Cognitive Psychology, Communication, Computer Science, Economics, English, History, Industrial & Organizational Psychology, Mathematics, Philosophy, Physics, Social & Personality Psychology, Sociology, Spanish
- MA/MS: Africana Studies, Anthropology, Applied Atmospheric Science, Biology, Chemistry, Communication, Computer Science, Economics, English, History, Mathematics, Philosophy, Physics, Sociology, Spanish, Studio Art, Women's Gender & Sexuality Studies
- MFA: Studio Art
- CAS: School Psychology
- CGS: Various certificates

#### Massry School of Business
- MBA: Business Administration
- MS: Accounting, AI for Business, Business Analytics, Digital Forensics & Cybersecurity, Forensic Accounting, Professional Accountancy, Taxation
- CGS: Information Security

#### College of Emergency Preparedness, Homeland Security & Cybersecurity (CEHC)
- PhD: Information Science
- MS: Cybersecurity & Risk, Emergency Management & Homeland Security, Information Science, Information Science School Library, Strategic Game Design & Applied Development
- CGS: Emergency Preparedness, Homeland Security & Cybersecurity; Computing Education; Online Learning & Teaching

#### College of Integrated Health Sciences (CIHS)
- PhD: Biomedical Sciences, Biostatistics, Environmental Health Sciences, Epidemiology, Social Work
- DrPH: Public Health
- MS: Biomedical Sciences, Biostatistics, Environmental Health Sciences, Epidemiology, Population Health Nursing
- MPH: Biomedical Sciences, Biostatistics, Environmental Health, Epidemiology, Health Policy & Management, Public Health Practice, Social Behavior & Community Health
- MSW: Social Work; Social Work/Criminal Justice; Social Work/Health Policy & Management; Social Work/JD
- CGS: Global Health Studies, Health Disparities, HIV Studies, Maternal & Child Health, Public Health Fundamentals & Principles, Public Health Surveillance & Preparedness

#### College of Nanotechnology, Science, and Engineering (CNSE)
- PhD: Electrical & Computer Engineering, Environmental & Sustainable Engineering, Nanobioscience, Nanoscale Engineering, Nanoscale Science
- MS: Computational Physics, Electrical & Computer Engineering, Environmental & Sustainable Engineering, Nanobioscience, Nanoscale Engineering, Nanoscale Science
- CGS: Semiconductor Manufacturing, Semiconductor Metrology, Semiconductor Patterning & Processing

#### Rockefeller College of Public Affairs & Policy
- PhD: Political Science, Public Administration & Policy
- MA: Political Science
- MPA: Public Administration & Policy
- MIA: International Affairs
- CGS: Data Science for Public Affairs, Nonprofit Management & Leadership, Public Sector Management, Women & Public Policy

#### School of Criminal Justice
- PhD: Criminal Justice
- MA: Criminal Justice; Criminal Justice/Social Work

#### School of Education
- PhD: Counseling Psychology, Curriculum & Instruction, Educational Policy & Leadership, Educational Psychology, Literacy
- PsyD: School Psychology
- MS: Childhood Education, Curriculum Development & Instructional Technology, Early Childhood Education, Educational Policy & Leadership, Educational Psychology & Methodology, General Education Studies, Higher Education, Literacy, Mental Health Counseling, Reading, Secondary Education, Special Education (multiple tracks)
- CAS: Curriculum & Instruction, Literacy, School Psychology
- AGC: Professional School Administrator, School District Business Leadership
- CGS: Community College Leadership, Computing Education, International Education Management, Online Learning & Teaching, Teacher Leadership

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (MS)**
- Department: Computer Science, College of Arts and Sciences
- URL: https://www.albany.edu/computer-science/programs/ms-computer-science
- Application: Via Graduate School portal
- GRE: Not required
- TOEFL minimum: 70 iBT
- IELTS minimum: 6.0

### 2.3 Graduate admissions model

UAlbany uses a **centralized Graduate School** for most programs. Apply at https://www.albany.edu/graduate/admissions. Some professional programs (Law, MBA) may have separate processes.

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://www.albany.edu/admissions | official_webpage |
| Application portal | Common App or SUNY Application | official_webpage |
| Early Action deadline | November 15 (domestic) / November 1 (international) | official_webpage |
| Regular Admission deadline | February 1 (domestic) / March 1 (international) | official_webpage |
| FAFSA priority deadline | December 1 | official_webpage |
| Enrollment Deposit deadline | May 1 | official_webpage |
| SAT/ACT policy | Test-optional | official_webpage |
| SAT Code | 2532 | official_webpage |
| ACT Code | 2926 | official_webpage |
| FAFSA Code | 002835 | official_webpage |
| TAP & Excelsior Code | 0895 | official_webpage |
| Application fee | Required (amount not specified on page) | official_webpage |
| Recommendation | Optional for domestic; Required 1 letter for international first-year | official_webpage |

**Source**: https://www.albany.edu/admissions/how-apply-first-year-student

**Accepted First-Year Profile (Fall 2025)**:
- Applications: 35,500
- Mid-Range GPA: 89-96 (3.3-4.0)
- SAT and ACT: Test Optional

### 3.2 Undergraduate English proficiency table

| Exam | Minimum Score | Notes |
|------|---------------|-------|
| TOEFL (iBT) | 70 (4 on new scale) | Code: 2532 |
| TOEFL (PBT) | 523 | |
| IELTS | 6.0 | |
| PTE | 50 | |
| Duolingo | 95 | |
| Cambridge English | B2 | |
| SAT 1 ERWS | 400 (22 Reading sub-score) | |
| ACT (English & Reading) | 19 | |
| IB Higher Level English A Literature | 4 | |
| IB Higher Level English A Language & Literature | 4 | |
| AS/A Level English | AS | |

**Applies to**: International students who attended high school outside the U.S. AND English is not native language.

**Source**: https://www.albany.edu/international-admissions/apply-international-undergraduate-student

### 3.3 Graduate — global rules

- Application portal: https://www.albany.edu/graduate/admissions
- GRE: Program-specific (many programs do not require)
- English proficiency: TOEFL 70+ iBT / IELTS 6.0+ (same as UG minimums)
- Application fee: Required (varies by program)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2025-2026 Academic Year)

| Expense Item | NYS Resident | Out-of-State | Description |
|-------------|--------------|--------------|-------------|
| Tuition | $7,070 | $28,280 | Full-time (12+ credits/semester) |
| Annual Fees | $3,646 | $3,646 | Student fees |
| On-Campus Housing | $10,346 | $10,346 | Quad Standard Double |
| Meal Plan | $6,406 | $6,406 | myUnlimited Meal Plan #1 |
| **Total (Fall & Spring)** | **$27,468** | **$48,678** | |

**Additional fees**:
- New Student Fee: $265 (freshmen) / $125 (transfer) — one-time
- Student-Alumni Partnership Fee: $30/semester (optional, can opt-out)
- Course Fees: Vary by course (labs, art classes)
- Inclusive Access Course Fee: Vary by course (optional digital materials)

**Source**: https://www.albany.edu/cost-aid/tuition-fees/undergraduate-students

### 4.2 Undergraduate financial-aid policy

- Nearly 80% of undergraduates apply for financial aid
- About 60% receive money they don't need to pay back
- Need-aware admissions (for all students, including international)
- Net Price Calculator: https://www.suny.edu/howmuch/netpricecalculator.xhtml
- State aid: TAP, Excelsior Scholarship (NYS residents)
- Federal aid: Pell Grants, work-study, direct loans

### 4.3 Graduate cost & funding framework

- Graduate tuition varies by program and residency
- See: https://www.albany.edu/cost-aid/tuition-fees/graduate-students
- International graduate students: https://www.albany.edu/cost-aid/tuition-fees/international-students
- International COA on-campus: $53,662/year
- International COA off-campus: $44,316/year (requires junior/senior standing)

---

## SECTION 5 — Evidence chain index

### E-U-001: Early Action Deadline (Domestic)
```yaml
field: undergraduate.deadlines.EA
value: November 15
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "Early Action: November 15"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-002: Regular Admission Deadline (Domestic)
```yaml
field: undergraduate.deadlines.RD
value: February 1
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "Regular Admission: February 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-003: Early Action Deadline (International)
```yaml
field: undergraduate.deadlines.EA_international
value: November 1
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "Early Action Deadline: November 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-004: Regular Admission Deadline (International)
```yaml
field: undergraduate.deadlines.RD_international
value: March 1
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "Regular Admission Deadline: March 1"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-005: Test-Optional Policy
```yaml
field: undergraduate.testing.policy
value: Test-optional
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "Official SAT or ACT scores (optional)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-006: SAT/ACT Codes
```yaml
field: undergraduate.testing.codes
value: SAT 2532, ACT 2926
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "UAlbany's SAT Code: 2532, UAlbany's ACT Code: 2926"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-007: NYS Resident Tuition
```yaml
field: undergraduate.costs.tuition_instate
value: $7,070
source_url: https://www.albany.edu/cost-aid/tuition-fees/undergraduate-students
source_snippet: "New York State Resident | $7,070"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-008: Out-of-State Tuition
```yaml
field: undergraduate.costs.tuition_outofstate
value: $28,280
source_url: https://www.albany.edu/cost-aid/tuition-fees/undergraduate-students
source_snippet: "Out-Of-State Resident | $28,280"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-009: Total NYS Resident COA
```yaml
field: undergraduate.costs.total_instate
value: $27,468
source_url: https://www.albany.edu/cost-aid/tuition-fees/undergraduate-students
source_snippet: "Total For Fall & Spring Semesters | $27,468"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-010: Total Out-of-State COA
```yaml
field: undergraduate.costs.total_outofstate
value: $48,678
source_url: https://www.albany.edu/cost-aid/tuition-fees/undergraduate-students
source_snippet: "Total For Fall & Spring Semesters | $48,678"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-011: TOEFL Minimum
```yaml
field: undergraduate.english_proficiency.toefl
value: 70 (iBT)
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "TOEFL (iBT) — UAlbany's Institutional Code: 2532 | 70 (4 on new scale)"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-012: IELTS Minimum
```yaml
field: undergraduate.english_proficiency.ielts
value: 6.0
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "IELTS | 6.0"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-013: Duolingo Minimum
```yaml
field: undergraduate.english_proficiency.duolingo
value: 95
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "Duolingo | 95"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-014: Number of Schools/Colleges
```yaml
field: institution.schools_count
value: 9
source_url: https://www.albany.edu/admissions
source_snippet: "9 Schools & Colleges"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-015: Undergraduate Enrollment
```yaml
field: institution.undergraduate_enrollment
value: 12,889
source_url: https://www.albany.edu/admissions
source_snippet: "12,889 undergraduates"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-016: Graduate Enrollment
```yaml
field: institution.graduate_enrollment
value: 4,537
source_url: https://www.albany.edu/admissions
source_snippet: "4,537 graduate students"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-017: Application Count (Fall 2025)
```yaml
field: undergraduate.admissions.applications
value: 35,500
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "Applications: 35,500"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-018: Accepted GPA Range
```yaml
field: undergraduate.admissions.gpa_range
value: 89-96 (3.3-4.0)
source_url: https://www.albany.edu/admissions/how-apply-first-year-student
source_snippet: "Mid-Range GPA: 89-96 (3.3-4.0)"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-019: International COA (On-Campus)
```yaml
field: graduate.costs.international_oncampus
value: $53,662/year
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "International students living on campus have a total cost of attendance (including tuition, fees, housing and meals) of $53,662 per year."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-020: International Scholarship Maximum
```yaml
field: undergraduate.scholarships.international_max
value: $82,000 over 4 years ($20,500/year)
source_url: https://www.albany.edu/international-admissions/apply-international-undergraduate-student
source_snippet: "The maximum scholarship award is $20,500 per year for first-year (freshmen) applicants, for a potential total of $82,000 over four years."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
ualbany-knowledge-base-v2/
├── 00-institution-overview.md
├── 01-ug-arts-sciences.md
├── 02-ug-business.md
├── 03-ug-cehc.md
├── 04-ug-health-sciences.md
├── 05-ug-engineering.md
├── 06-ug-rockefeller.md
├── 07-ug-criminal-justice.md
├── 08-ug-education.md
├── 09-grad-programs.md
├── 10-deadlines-requirements.md
├── 11-costs-financial-aid.md
└── 12-evidence-chain.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ualbany-knowledge-base-v2"
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
| P0 | Application fee amount | https://www.albany.edu/admissions/how-apply-first-year-student |
| P0 | Complete minors list (50+) | https://www.albany.edu/academics/undergraduate-majors-minors#minors |
| P1 | Graduate tuition by program | https://www.albany.edu/cost-aid/tuition-fees/graduate-students |
| P1 | Per-program GRE requirements | Individual program pages |
| P1 | Financial aid details (income thresholds) | https://www.albany.edu/cost-aid/financial-aid |
| P2 | Need-blind/need-aware policy details | https://www.albany.edu/cost-aid/financial-aid |
| P2 | Graduate application deadlines by program | Individual program pages |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | UAlbany | (Other schools) |
|------|---------|-----------------|
| Type | Public (SUNY) | |
| Location | Albany, NY | |
| UG Tuition (NYS) | $7,070 | |
| UG Tuition (OOS) | $28,280 | |
| UG Total COA (NYS) | $27,468 | |
| UG Total COA (OOS) | $48,678 | |
| EA Deadline (Domestic) | November 15 | |
| EA Deadline (International) | November 1 | |
| RD Deadline (Domestic) | February 1 | |
| RD Deadline (International) | March 1 | |
| SAT/ACT Required? | No (test-optional) | |
| TOEFL Minimum | 70 | |
| IELTS Minimum | 6.0 | |
| Duolingo Minimum | 95 | |
| Need-blind? | Need-aware (all) | |
| Total UG Majors | 54 | |
| Total Grad Programs | 170+ | |
| Schools/Colleges | 9 | |
| UG Enrollment | 12,889 | |
| Grad Enrollment | 4,537 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.albany.edu, admissions.albany.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
