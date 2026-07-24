# University of Tasmania (UTAS) — 知识库完整深度数据 (v2)

> **Data capture date**: 2026-07-10
> **Capture tool**: Browser-based extraction (Hermes browser tools)
> **Target knowledge base**: WeKnora
> **Granularity**: college → school → study area → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU, Tasmania)
> **Official website**: https://www.utas.edu.au/
> **Courses & Units catalog**: https://www.utas.edu.au/courses/
> **CRICOS Provider Code**: 00586B

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| Dimension | Count |
|-----------|-------|
| 本科学位专业 (UG Bachelor programmes, incl. Honours) | ~60+ study areas |
| 本科辅修 (Majors within degrees) | Extensive (not individually counted) |
| 研究生授课型项目 (PGT: Master/Graduate Cert/Graduate Dip) | ~50+ study areas |
| 研究生博士项目 (PhD/Doctoral) | Available across all colleges |
| 学位项目总计 (Total identified) | 110+ study areas (see below for full listing) |
| 学院 (Colleges/Schools) | 4 Academic Colleges + 1 Pathway College |
| 学术院系 (Academic Schools/Departments) | ~25+ schools and institutes |

**Note**: UTAS organizes its courses by 6 broad study areas, not by colleges directly. Full course listings need to be checked per-course at https://www.utas.edu.au/courses/. The data below represents a comprehensive listing of all study areas extracted from the 6 study area pages.

**Source**: https://www.utas.edu.au/study/ (course areas navigation)

---

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Tasmania
│
├── College of Arts, Society and Education
│   ├── School of Creative and Performing Arts
│   │   └── Conservatorium of Music
│   ├── School of Education
│   ├── School of Humanities and Social Sciences
│   └── School of Law
│
├── College of Health
│   ├── Menzies Institute for Medical Research
│   ├── Wicking Dementia Research and Education Centre
│   ├── Tasmanian School of Medicine
│   ├── School of Nursing
│   ├── School of Health Sciences
│   ├── School of Paramedicine and Public Safety
│   ├── School of Pharmacy and Pharmacology
│   ├── School of Psychological Sciences
│   ├── Centre for Rural Health
│   └── Social Work
│
├── College of Sciences and Engineering
│   ├── Tasmanian Institute of Agriculture
│   ├── School of Architecture and Design
│   ├── School of Engineering
│   ├── School of Geography, Planning, and Spatial Sciences
│   ├── School of Information and Communication Technology
│   ├── Institute for Marine and Antarctic Studies (IMAS)
│   ├── Australian Maritime College (AMC)
│   ├── School of Natural Sciences
│   └── Australian Forest and Wood Innovations
│
├── College of Business and Economics
│   └── Tasmanian School of Business and Economics (TSBE)
│
└── University College (Pathways)
    └── Foundation programs, diplomas, pathway programs

Research Institutes & Centres:
├── Institute for Marine and Antarctic Studies (IMAS)
├── Menzies Institute for Medical Research
├── Tasmanian Institute of Agriculture (TIA)
├── Australian Maritime College (AMC)
├── Wicking Dementia Research and Education Centre
└── Australian Forest and Wood Innovations
```

**Source**: https://www.utas.edu.au/about/academic-structure

---

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| Degree Level | Count (study areas) | Complete? |
|--------------|-------------------|-----------|
| Bachelor (UG) | ~40+ | Comprehensive |
| Honours (UG, standalone) | Available per degree | Partial |
| Graduate Certificate | ~15+ | Partial |
| Graduate Diploma | ~5+ | Partial |
| Master (Coursework) | ~40+ | Comprehensive |
| MPhil (Research) | Available | Partial |
| PhD / Doctoral | Available across all colleges | Partial |
| Undergraduate Certificate / Diploma | ~3+ | Partial |
| Double Degrees (UG) | 20+ combinations | Partial |
| **Total** | **~110+ study areas** | **Comprehensive** |

---

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| Study Area | UG Bachelor | Honours | Master/Coursework | Grad Cert/Dip | PhD | Total |
|-----------|-----------|---------|-----------------|--------------|-----|-------|
| Business and Law | 7 | ✓ | 10 | 0 | ✓ | 17+ |
| Creative Arts and Design | 7 | ✓ | 1 | 0 | ✓ | 8+ |
| Earth, Sea, Antarctic and Environment | 12 | ✓ | 8 | 0 | ✓ | 20+ |
| Education, Humanities and Social Sciences | 9 | ✓ | 6 | 0 | ✓ | 15+ |
| Health and Medicine | 12 | ✓ | 16 | 0 | ✓ | 28+ |
| Science, Technology and Engineering | 13 | ✓ | 10 | 0 | ✓ | 23+ |
| **Total** | **60+** | **—** | **51+** | **—** | **—** | **111+** |

**Note**: Honours and PhD are available in virtually all study areas. Honours typically adds 1 year to UG. PhD by research is available across all colleges.

---

## Section 1 — Undergraduate education

### 1.1 Business and Law (Tasmanian School of Business and Economics + School of Law)

| Study Area / Course Name | Degree Type | College/School | Course Code | Key Details | Program URL |
|------------------------|-------------|---------------|------------|-------------|-------------|
| Agribusiness | Bachelor | TSBE | — | Hobart, Launceston, Online | /study/undergraduate/agribusiness |
| Business | Bachelor (B3A) | TSBE | B3A | 3 yrs, AQF 7, CSP avail. ATAR 50.95 (2025). IELTS 6.0/5.5. Int'l fee $37,950/yr. | /study/undergraduate/business |
| Business (Honours) | Bachelor (Hons) | TSBE | G4F | 1 yr, AQF 8 | /courses/tsbe/courses/g4f-bachelor-of-business-with-honours |
| Economics | Bachelor | TSBE | — | Hobart, Online | /study/undergraduate/economics |
| Global Logistics and Maritime Management | Bachelor | TSBE/AMC | — | Launceston, Online. Maritime focus | /study/undergraduate/global-logistics-and-maritime-management |
| Information and Communication Technology (ICT) | Bachelor | TSBE/ICT | — | Hobart, Launceston, Online | /study/undergraduate/information-and-communication-technology |
| Law | Bachelor (LLB) | School of Law | — | Hobart | /study/undergraduate/law |
| Media and Communication | Bachelor | TSBE | — | Hobart, Online | /study/undergraduate/media |
| Behavioural Insights | Postgraduate | TSBE | — | Online | /study/postgraduate/behavioural-insights |
| Business Administration (MBA) | Master | TSBE | — | 1.5-2 yrs, Online/Hobart | /study/postgraduate/business-administration |
| Digital Health | Master | TSBE/Health | — | Online | /study/postgraduate/digital-health |
| Leadership and Organisational Capability | Master | TSBE | — | Online | /study/postgraduate/leadership-and-organisational-capability |
| Leadership in Health and Human Services | Master | TSBE/Health | — | Online. Not avail. for int'l students | /study/postgraduate/leadership-in-health-and-human-services |
| Global Logistics and Supply Chain Management | Master | TSBE/AMC | — | Launceston, Online | /study/postgraduate/global-logistics-and-supply-chain-management |
| Maritime Management | Master | AMC | — | Launceston | /study/postgraduate/maritime-management |
| Organisational Resilience | Master | TSBE | — | Online | /study/postgraduate/organisational-resilience |
| Professional Accounting | Master (MPA) | TSBE | — | 1.5-2 yrs | /study/postgraduate/professional-accounting |
| Protected Area Conservation | Master | TSBE/SciEng | — | Online | /study/postgraduate/protected-area-conservation |
| Sustainable Business | Master | TSBE | — | Online | /study/postgraduate/sustainable-business |

### 1.2 Creative Arts and Design (School of Creative and Performing Arts)

| Study Area / Course Name | Degree Type | College | Key Details | Program URL |
|------------------------|-------------|---------|-------------|-------------|
| Architecture and Built Environments | Bachelor | Sciences & Engineering | Hobart, Launceston. 3-4 yrs | /study/undergraduate/architecture-and-built-environments |
| Creative Arts and Health | Bachelor | Health/Arts Society | Hobart | /study/undergraduate/creative-arts-and-health |
| Design | Bachelor | Sciences & Engineering | Hobart, Launceston | /study/undergraduate/design |
| Fine Arts | Bachelor | Arts Society | Hobart | /study/undergraduate/fine-arts |
| Media and Communication | Bachelor | TSBE | Hobart, Online | /study/undergraduate/media |
| Music | Bachelor | Arts Society | Hobart (Conservatorium) | /study/undergraduate/music |
| Theatre and Performance | Bachelor | Arts Society | Hobart | /study/undergraduate/theatre-and-performance |
| Architecture | Master | Sciences & Engineering | Hobart, Launceston | /study/postgraduate/architecture |

### 1.3 Earth, Sea, Antarctic and Environment (IMAS, TIA, AMC, Natural Sciences)

| Study Area / Course Name | Degree Type | College | Key Details | Program URL |
|------------------------|-------------|---------|-------------|-------------|
| Agribusiness | Bachelor | TSBE | Hobart, Launceston, Online | /study/undergraduate/agribusiness |
| Agricultural Science | Bachelor | Sciences & Engineering | Hobart, Launceston. TIA affiliated | /study/undergraduate/agricultural-science |
| Engineering | Bachelor (BE) | Sciences & Engineering | Hobart, Launceston. 4 yrs | /study/undergraduate/engineering |
| Geospatial Science | Bachelor | Sciences & Engineering | Hobart, Online | /study/undergraduate/geospatial-science |
| Global Logistics and Maritime Management | Bachelor | TSBE/AMC | Launceston, Online | /study/undergraduate/global-logistics-and-maritime-management |
| Marine and Antarctic Science | Bachelor | Sciences & Engineering | Hobart. IMAS affiliated | /study/undergraduate/marine-and-antarctic-science |
| Maritime Engineering | Bachelor | AMC | Launceston | /study/undergraduate/maritime-engineering |
| Natural Environments and Conservation | Bachelor | Sciences & Engineering | Hobart, Launceston | /study/undergraduate/natural-environments-and-conservation |
| Ocean Seafaring | Bachelor | AMC | Launceston | /study/undergraduate/ocean-seafaring |
| Outdoor and Environmental Education | Bachelor | Arts Society/Education | Launceston | /study/undergraduate/outdoor-and-environmental-education |
| Science | Bachelor (BSc) | Sciences & Engineering | Hobart, Launceston | /study/undergraduate/science |
| Sustainability | Bachelor | Sciences & Engineering | Online | /study/undergraduate/sustainability |
| Sustainable Living | Bachelor | Sciences & Engineering | Online | /study/undergraduate/sustainable-living |

### 1.4 Education, Humanities and Social Sciences (School of Humanities, Education, Law)

| Study Area / Course Name | Degree Type | College | Key Details | Program URL |
|------------------------|-------------|---------|-------------|-------------|
| Education | Bachelor | Arts Society | Hobart, Launceston, Cradle Coast, Online | /study/undergraduate/education |
| Family History | Bachelor | Arts Society | Online | /study/undergraduate/family-history |
| Humanities and Social Sciences | Bachelor | Arts Society | Hobart, Launceston, Online | /study/undergraduate/humanities-and-social-sciences |
| Languages | Bachelor | Arts Society | Hobart, Online | /study/undergraduate/languages |
| Media and Communication | Bachelor | TSBE | Hobart, Online | /study/undergraduate/media |
| Mental Health | Bachelor | Health | Online | /study/undergraduate/mental-health |
| Outdoor and Environmental Education | Bachelor | Arts Society/Education | Launceston | /study/undergraduate/outdoor-and-environmental-education |
| Psychology | Bachelor (BPsych) | Health | Hobart, Launceston, Online | /study/undergraduate/psychology |
| Social Work | Bachelor (BSW) | Health | Hobart, Cradle Coast | /study/undergraduate/social-work |

### 1.5 Health and Medicine (College of Health)

| Study Area / Course Name | Degree Type | College | Key Details | Program URL |
|------------------------|-------------|---------|-------------|-------------|
| Applied Health and Community Support | Bachelor | Health | — | /study/undergraduate/applied-health |
| Biomedicine | Bachelor | Health | Hobart | /study/undergraduate/biomedicine |
| Creative Arts and Health | Bachelor | Health/Arts Society | Hobart | /study/undergraduate/creative-arts-and-health |
| Dementia Care | Bachelor | Health | Online. Wicking Centre | /study/undergraduate/dementia-care |
| Emergency Management | Bachelor | Health/Paramedicine | — | /study/undergraduate/emergency-management |
| Exercise and Sport Science | Bachelor | Health | Hobart, Launceston | /study/undergraduate/exercise-and-sport-science |
| Medicine | Bachelor (MBBS) | Tasmanian School of Medicine | Hobart, Launceston. 5 yrs. CSP avail. | /study/undergraduate/medicine |
| Nursing | Bachelor (BN) | School of Nursing | Hobart, Launceston, Cradle Coast. 3 yrs (can accelerate to 2) | /study/undergraduate/nursing |
| Paramedicine | Bachelor | Paramedicine | Hobart, Launceston | /study/undergraduate/paramedicine |
| Pharmacy | Bachelor | Pharmacy & Pharmacology | Hobart. 4 yrs | /study/undergraduate/pharmacy |
| Psychology | Bachelor (BPsych) | Psychological Sciences | Hobart, Launceston, Online | /study/undergraduate/psychology |

### 1.6 Science, Technology and Engineering (College of Sciences and Engineering)

| Study Area / Course Name | Degree Type | College | Key Details | Program URL |
|------------------------|-------------|---------|-------------|-------------|
| Agricultural Science | Bachelor | Sciences & Engineering | TIA affiliated | /study/undergraduate/agricultural-science |
| Applied Technologies | Bachelor | Sciences & Engineering | — | /study/undergraduate/applied-technologies |
| Architecture and Built Environments | Bachelor | Sciences & Engineering | Hobart, Launceston | /study/undergraduate/architecture-and-built-environments |
| Design | Bachelor | Sciences & Engineering | Hobart, Launceston | /study/undergraduate/design |
| Engineering | Bachelor (BE) | School of Engineering | Hobart, Launceston. 4 yrs | /study/undergraduate/engineering |
| Geospatial Science | Bachelor | Sciences & Engineering | Hobart, Online | /study/undergraduate/geospatial-science |
| Global Logistics and Maritime Management | Bachelor | TSBE/AMC | Launceston | /study/undergraduate/global-logistics-and-maritime-management |
| Information and Communication Technology (ICT) | Bachelor | ICT | Hobart, Launceston, Online | /study/undergraduate/information-and-communication-technology |
| Marine and Antarctic Science | Bachelor | IMAS | Hobart | /study/undergraduate/marine-and-antarctic-science |
| Maritime Engineering | Bachelor | AMC | Launceston | /study/undergraduate/maritime-engineering |
| Ocean Seafaring | Bachelor | AMC | Launceston | /study/undergraduate/ocean-seafaring |
| Science | Bachelor (BSc) | Natural Sciences | Hobart, Launceston | /study/undergraduate/science |
| Sustainable Living | Bachelor | Sciences & Engineering | Online | /study/undergraduate/sustainable-living |

---

## Section 2 — Graduate education

### 2.1 Taught Postgraduate (PGT)

#### 2.1.1 Business and Law

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Behavioural Insights | Master | TSBE | Online | /study/postgraduate/behavioural-insights |
| Business Administration (MBA) | Master | TSBE | Hobart, Online. 1.5-2 yrs | /study/postgraduate/business-administration |
| Digital Health | Master | TSBE/Health | Online | /study/postgraduate/digital-health |
| Global Logistics and Supply Chain Management | Master | TSBE/AMC | Launceston, Online | /study/postgraduate/global-logistics-and-supply-chain-management |
| Leadership and Organisational Capability | Master | TSBE | Online | /study/postgraduate/leadership-and-organisational-capability |
| Leadership in Health and Human Services | Master | TSBE/Health | Online. Not avail. int'l | /study/postgraduate/leadership-in-health-and-human-services |
| Maritime Management | Master | AMC | Launceston | /study/postgraduate/maritime-management |
| Organisational Resilience | Master | TSBE | Online | /study/postgraduate/organisational-resilience |
| Professional Accounting | Master (MPA) | TSBE | 1.5-2 yrs | /study/postgraduate/professional-accounting |
| Protected Area Conservation | Master | TSBE/SciEng | Online | /study/postgraduate/protected-area-conservation |
| Sustainable Business | Master | TSBE | Online | /study/postgraduate/sustainable-business |

#### 2.1.2 Creative Arts and Design

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Architecture | Master | Architecture & Design | Hobart, Launceston | /study/postgraduate/architecture |

#### 2.1.3 Earth, Sea, Antarctic and Environment

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Agriculture | Master | TIA | Hobart | /study/postgraduate/agriculture |
| Economic Geology | Master | Natural Sciences | Hobart | /study/postgraduate/economic-geology |
| Environmental Geospatial Sciences | Master | Geography/Planning | Hobart, Online | /study/postgraduate/environmental-geospatial-sciences |
| Global Logistics and Supply Chain Management | Master | TSBE/AMC | Launceston, Online | /study/postgraduate/global-logistics-and-supply-chain-management |
| Healthcare in Remote and Extreme Environments | Master | Health/IMAS | Hobart | /study/postgraduate/healthcare-in-remote-and-extreme-environments |
| Marine and Antarctic Science | Master | IMAS | Hobart | /study/postgraduate/marine-and-antarctic-science |
| Maritime Management | Master | AMC | Launceston | /study/postgraduate/maritime-management |
| Planning | Master | Geography/Planning | Hobart, Online | /study/postgraduate/planning |
| Protected Area Conservation | Master | SciEng | Online | /study/postgraduate/protected-area-conservation |
| Sustainability | Master | SciEng | Online | /study/postgraduate/sustainability |

#### 2.1.4 Education, Humanities and Social Sciences

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Education | Master | School of Education | Hobart, Launceston, Online | /study/postgraduate/education |
| Mental Health | Master | Health | Online | /study/postgraduate/mental-health |
| Organisational Resilience | Master | TSBE | Online | /study/postgraduate/organisational-resilience |
| Psychology | Master | Psychological Sciences | Hobart | /study/postgraduate/psychology |
| Social Work | Master (MSW) | Social Work | Hobart, Cradle Coast | /study/postgraduate/social-work |
| Teaching | Master (MTeach) | School of Education | Hobart, Launceston | /study/postgraduate/teaching |

#### 2.1.5 Health and Medicine

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Health Professional Development | Various | Health | Online | /study/postgraduate/health-professional-development |
| Advanced Nursing | Master | Nursing | Online | /study/postgraduate/advanced-nursing |
| Advanced Practice | Master | Health | Online | /study/postgraduate/advanced-practice |
| Allied Health | Master | Health Sciences | Online | /study/postgraduate/allied-health |
| Clinical Pharmacy | Master | Pharmacy | Hobart, Online | /study/postgraduate/clinical-pharmacy |
| Dementia | Master | Wicking Centre | Online | /study/postgraduate/dementia |
| Digital Health | Master | TSBE/Health | Online | /study/postgraduate/digital-health |
| Healthcare in Remote and Extreme Environments | Master | Health/IMAS | Hobart | /study/postgraduate/healthcare-in-remote-and-extreme-environments |
| Healthcare Redesign | Master | Health | Online | /study/postgraduate/healthcare-redesign |
| Laboratory Medicine | Master | Health Sciences | Hobart | /study/postgraduate/laboratory-medicine |
| Leadership in Health and Human Services | Master | Health | Online. Not int'l | /study/postgraduate/leadership-in-health-and-human-services |
| Midwifery | Master | Nursing | Online | /study/postgraduate/midwifery |
| Occupational Therapy | Master | Health Sciences | Hobart, Launceston | /study/postgraduate/occupational-therapy |
| Pharmaceutical Science | Master | Pharmacy | Hobart | /study/postgraduate/pharmaceutical-science |
| Physiotherapy | Master | Health Sciences | Hobart, Launceston | /study/postgraduate/physiotherapy |
| Psychology | Master (MClinPsych) | Psychological Sciences | Hobart | /study/postgraduate/psychology |
| Public Health | Master (MPH) | Health | Online | /study/postgraduate/public-health |
| Speech Pathology | Master | Health Sciences | Hobart, Launceston | /study/postgraduate/speech-pathology |

#### 2.1.6 Science, Technology and Engineering

| Program Name | Degree Type | School | Key Details | Program URL |
|-------------|-------------|--------|-------------|-------------|
| Architecture | Master | Architecture & Design | Hobart, Launceston | /study/postgraduate/architecture |
| Chemistry | Master | Natural Sciences | Hobart | /study/postgraduate/chemistry |
| Economic Geology | Master | Natural Sciences | Hobart | /study/postgraduate/economic-geology |
| Global Logistics and Supply Chain Management | Master | TSBE/AMC | Launceston, Online | /study/postgraduate/global-logistics-and-supply-chain-management |
| Information Technology and Systems | Master | ICT | Hobart, Online | /study/postgraduate/information-technology-and-systems |
| Marine and Antarctic Science | Master | IMAS | Hobart | /study/postgraduate/marine-and-antarctic-science |
| Maritime Engineering | Master | AMC | Launceston | /study/postgraduate/maritime-engineering |
| Organisational Resilience | Master | TSBE | Online | /study/postgraduate/organisational-resilience |
| Protected Area Conservation | Master | SciEng | Online | /study/postgraduate/protected-area-conservation |

### 2.2 Research Postgraduate (PhD/MPhil)

Research degrees are available across all 4 colleges and research institutes:

| Program Name | Degree Type | College/Institute | Key Details | Program URL |
|-------------|-------------|------------------|-------------|-------------|
| Doctor of Philosophy (PhD) | PhD | All colleges | 3-4 yrs F/T. Apply any time | /research/degrees |
| Master of Philosophy (MPhil) | MPhil | All colleges | 1-2 yrs F/T | /research/degrees |
| PhD - IMAS | PhD | IMAS | Marine & Antarctic research | /research/degrees/available-projects |
| PhD - Menzies | PhD | Menzies Institute | Medical research | /research/degrees/available-projects |
| PhD - TIA | PhD | Tasmanian Institute of Agriculture | Agricultural research | /research/degrees/available-projects |
| PhD - AMC | PhD | Australian Maritime College | Maritime research | /research/degrees/available-projects |

**Source**: https://www.utas.edu.au/research/degrees

---

## Section 3 — Application requirements & deadlines

### 3.1 Undergraduate Admissions

**Source**: https://www.utas.edu.au/study/apply/admission-requirements

#### Domestic students

- **Application system**: Direct to UTAS (free online form) or via Schools Recommendation Program (SRP)
- **Selection basis**: ATAR or equivalent. Year 12 students can also apply via SRP (teacher recommendation, not ATAR)
- **Guaranteed ATAR entry**: Varies by course. Example: Bachelor of Business (B3A) lowest ATAR in 2025 was **50.95**
- **Special Consideration**: Available for applicants whose education was affected by circumstances beyond their control (economic hardship, medical condition, disability)
- **Pathway programs**: University Preparation Program (E0D), Diploma of University Studies, Foundation programs
- **Prerequisites**: Vary by program. Most courses have no specific prerequisites beyond general entry requirements

#### International students

- **English Language Requirements**: IELTS (Academic) 6.0 overall, no band < 5.5 (for most UG courses); some professional programs require higher (e.g., Nursing, Medicine)
- **PTE Academic**: 50 overall, no score < 42 (for most UG courses)
- **General Entry**: Completion of qualifications equivalent to Australian Year 12
- **Application**: Direct to UTAS or via authorized education agents
- **Pathway**: International Pathway College - Foundation Studies Program and International First Year Diploma (Business - X1B)

### 3.2 Postgraduate Admissions

- **General entry**: Bachelor's degree in relevant discipline. GPA requirements vary by program
- **Honours entry**: Bachelor degree with Distinction average or higher in final year units (varies by program)
- **Research degrees**: Apply any day of the year. Supervisor availability required
- **English Language**: IELTS 6.0-7.0 depending on program (Medicine/Health typically require 7.0)

### 3.3 Application Dates

**Source**: https://www.utas.edu.au/study/apply/application-dates

| Date | Event |
|------|-------|
| Jan | First-round offers made progressively to Year 12 & IB interstate applicants |
| 3 Jan | Application for Special Consideration closes (11:59 pm AEDST) |
| 20 Feb | Last applications close for Semester 1 UG & PG (non-quota) courses |
| 23 Feb | Semester 1 commences (Orientation week before) |
| 25 Feb | Last offers for Semester 1 UG & PG (non-quota) courses |
| 3 Jul | Last applications close for Semester 2 UG & PG (non-quota) courses |
| 6 Jul | Semester 2 commences |
| 8 Jul | Last offers for Semester 2 UG & PG (non-quota) courses |

**International students**: Apply at least 3 months before semester start (offshore) or 1 month before (onshore).

**Research degrees**: Can apply any day of the year.

---

## Section 4 — Fees, scholarships & costs

**Source**: https://www.utas.edu.au/study/scholarships-fees-and-costs

### 4.1 Domestic Student Contributions (Commonwealth Supported Place - CSP)

| Band | Field of Education | 2026 Rate ($/EFTSL) |
|------|-------------------|---------------------|
| 1 | Agriculture, English, maths, education, clinical psych, Indigenous/foreign languages, nursing, statistics | $4,738 |
| 2 | Allied health, built environment, computing, engineering, science, environmental studies, performing arts | $9,537 |
| 3 | Medicine, dental, veterinary science | $13,558 |
| 4 | Law, accounting, admin, economics, commerce, communications, society & culture | $17,399 |

**Example**: Bachelor of Business (B3A) CSP indicative annual fee: **$15,028.17** (Band 4)

### 4.2 International Tuition Fees

- **Bachelor of Business (B3A)**: $37,950 AUD/year (2026). Indicative total: $119,637 AUD
- Fees are CPI-indexed annually. Quoted in AUD. Do not include textbooks, health insurance (OSHC), or living expenses
- Research degrees: flat annual fee for international candidates

### 4.3 Scholarships

- **Domestic**: Hundreds of scholarships available. S1 2026 applications closed. S2 2026 opens May 2026
- **International**: Merit-based scholarships available across all study areas
- **External scholarships**: Also available
- **Prizes**: 300+ prizes, $160,000+ awarded annually
- **Fee scholarships**: Discounts applied to student account. Available via DHHS, DoE, staff/alumni scholarships

### 4.4 Other Costs

- **SSAF (Student Services and Amenities Fee)**: Compulsory. Can be deferred via SA-HELP loan for domestic students. Built into international fees
- **OS-HELP**: Loan for CSP students studying abroad
- **HELP loans**: HECS-HELP (CSP students), FEE-HELP (full-fee students). Repay via tax system once earning above threshold
- **Living costs**: Use Study Australia Cost of Living Calculator

---

## Section 5 — International student information

**Source**: https://www.utas.edu.au/study/international

### 5.1 Key Facts

| Metric | Value |
|--------|-------|
| CRICOS Provider Code | 00586B |
| #1 in climate action globally | THE Impact Ratings 2022-2026 |
| #1 in Australia for PG International Student Satisfaction | ISB 2024 |
| Post-study work rights | Up to 4 years on Temporary Graduate visa (subclass 485) |
| Study locations | Hobart, Launceston, Cradle Coast, Sydney (Melbourne for int'l only) |

### 5.2 International Entry Requirements (Standard)

- **IELTS Academic**: 6.0 overall, no band < 5.5 (most programs)
- **Higher IELTS required for**: Nursing, Medicine, Pharmacy, Teaching, Social Work (6.5-7.0 typically)
- **PTE Academic**: 50 overall, no score < 42
- **Academic**: Equivalent to Australian Year 12 for UG; Bachelor degree for PG
- **Pathway**: International Pathway College - Foundation Studies + International First Year Diploma

### 5.3 Application Process

- **Apply**: Direct online form or via authorized agent
- **Timing**: Offshore: at least 3 months before semester. Onshore: at least 1 month before
- **Required documents**: Academic transcripts, English language test results, passport copy
- **Agent network**: Global network of authorized agents

---

## Section 6 — Course detail URLs (Evidence chain)

All course detail pages follow the pattern: `https://www.utas.edu.au/courses/{school}/courses/{code}-{course-name}`

### Key course detail pages verified:

| Course | Course Code | URL |
|--------|------------|-----|
| Bachelor of Business | B3A | https://www.utas.edu.au/courses/tsbe/courses/b3a-bachelor-of-business |
| Bachelor of Business with Honours | G4F | https://www.utas.edu.au/courses/tsbe/courses/g4f-bachelor-of-business-with-honours |
| Undergraduate Cert in Climate Accounting | 30C | https://www.utas.edu.au/courses/tsbe/courses/30c-undergraduate-certificate-in-climate-accounting |

### Key source pages used:

| Page | URL |
|------|-----|
| Homepage | https://www.utas.edu.au/ |
| Academic Structure | https://www.utas.edu.au/about/academic-structure |
| Study with us | https://www.utas.edu.au/study |
| Undergraduate courses | https://www.utas.edu.au/study/undergraduate |
| Postgraduate courses | https://www.utas.edu.au/study/postgraduate |
| Admission requirements | https://www.utas.edu.au/study/apply/admission-requirements |
| Application dates | https://www.utas.edu.au/study/apply/application-dates |
| Scholarships, fees & costs | https://www.utas.edu.au/study/scholarships-fees-and-costs |
| International students | https://www.utas.edu.au/study/international |
| Business and Law area | https://www.utas.edu.au/study/areas/business-and-law |
| Creative Arts and Design area | https://www.utas.edu.au/study/areas/creative-arts-and-design |
| Earth, Sea, Antarctic and Environment area | https://www.utas.edu.au/study/areas/earth-sea-antarctic-and-environment |
| Education, Humanities and Social Sciences area | https://www.utas.edu.au/study/areas/education-humanities-and-social-sciences |
| Health and Medicine area | https://www.utas.edu.au/study/areas/health-and-medicine |
| Science, Technology and Engineering area | https://www.utas.edu.au/study/areas/science-technology-and-engineering |
| Research degrees | https://www.utas.edu.au/research/degrees |
| Nursing course page | https://www.utas.edu.au/study/undergraduate/nursing |
| Business course detail | https://www.utas.edu.au/courses/tsbe/courses/b3a-bachelor-of-business |

---

## Section 7 — Monitoring & notes

### 7.1 Site Architecture

- **CMS**: Custom web framework with Funnelback search
- **URL pattern**: `/study/` for marketing pages, `/courses/{school}/courses/{code}-{name}` for course detail pages
- **Mobile navigation**: JS-based hamburger menu (`button#e7`)
- **Search**: Funnelback-powered search at `search.utas.edu.au`
- **Student portal**: SharePoint-based (`universitytasmania.sharepoint.com/sites/StudentPortal`)
- **LMS**: MyLO (`mylo.utas.edu.au`)

### 7.2 Data Quality Notes

- **Completeness**: Study area listings are comprehensive but individual course detail pages (fees, IELTS, ATAR) were sampled from the Business program as representative
- **Not extracted**: Individual unit/module listings within each course (available per course detail page under "Course structure")
- **Not extracted**: Full double degree combinations (20+ available)
- **Not extracted**: Short courses and micro-credentials
- **Not extracted**: Individual scholarship listings (hundreds available via separate portal)
- **Curriculum data**: Course structure with core units and majors is available per-course at `/courses/{school}/courses/{code}-{name}`

### 7.3 Recommended Updates

| Data Point | Update Frequency | Source |
|-----------|-----------------|--------|
| Course fees (int'l) | Annual (indexation) | Individual course pages |
| CSP student contributions | Annual (indexation) | Fees page |
| ATAR thresholds | Annual | Entry requirements section per course |
| Application dates | Semesterly | Application dates page |
| Scholarship deadlines | Semesterly | Scholarships portal |
| IELTS requirements | As updated | Course detail pages |
| New courses | As added | Study area pages |

### 7.4 Key Contacts

| Contact | Details |
|---------|---------|
| Domestic enquiries | 13 8827 (13 UTAS) |
| International enquiries | +61 3 6226 6200 |
| Email | Course.Info@utas.edu.au |
| Operating hours | Mon-Fri 9:00am-4:00pm (5:00pm for course enquiries) |
| Address | University of Tasmania, Private Bag 51, Hobart TAS 7001, Australia |

---

*End of document — University of Tasmania (UTAS) knowledge base v2*
*Generated: 2026-07-10*
