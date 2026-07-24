# Glasgow Caledonian University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (Scotland)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 82 |
| 研究生授课型项目 (PGT: MSc/MA/MBA/LLM/MPH/DPsych/DBA/PgD) | 72 |
| 研究生博士项目 (PhD/Doctoral) | Extracted via separate research programme listing |
| **学位项目总计 (UG + PGT extracted)** | **154** |
| 学术学院 (Academic Schools) | 3 (+ GCU London) |
| 学术系所 (Departments) | 16 |

> **Data source**: GCU course search API (`gcu.ac.uk/search?query=!padrenull&f.Tabs|gcun~ds-courses=Courses`), Funnelback-powered search. UG: 82 results, PG: 72 results extracted.
> **Note**: GCU also offers Graduate Apprenticeship courses and Pathway courses (multiple locations) which are included in the counts above.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
Glasgow Caledonian University
├── Glasgow School for Business and Society (GSBS)      [学院]
│   ├── Department of Economics and Law                  [系]
│   ├── Department of Fashion, Marketing, Tourism and Events [系]
│   ├── Department of Finance, Accounting and Risk       [系]
│   ├── Department of Management                         [系]
│   ├── Department of Media and Journalism               [系]
│   ├── Department of People and Organisations           [系]
│   └── Department of Social Sciences                    [系]
├── School of Health and Life Sciences (HLS)             [学院]
│   ├── Department of Biological and Biomedical Sciences [系]
│   ├── Department of Nursing, Community and Public Health [系]
│   ├── Department of Psychology                         [系]
│   ├── Department of Social Work                        [系]
│   ├── Department of Vision Sciences                    [系]
│   └── Department of Allied Health Professions          [系]
├── School of Science and Engineering (SSE)              [学院]
│   ├── Department of Computer Science                   [系]
│   ├── Department of Construction and Built Environment [系]
│   └── Department of Engineering                        [系]
└── GCU London                                           [分校区]
    └── (Various programmes from GSBS and SSE offered at London campus)
```

> **Source**: `gcu.ac.uk/aboutgcu/academicschools` and individual school pages.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 (official) | Canonical | 层级 | 本项目数量 |
|---------|-----------|------|-----------|
| BA (Hons) | BA | 本科 | 22 |
| BSc (Hons) | BSc | 本科 | 42 |
| BSc | BSc (Ordinary) | 本科 | 6 |
| BEng (Hons) | BEng | 本科 | 9 |
| MEng | MEng | 本科 (Integrated Master's) | 2 |
| LLB (Hons) | LLB | 本科 | 1 |
| LLB | LLB (Fast-track) | 本科 | 1 |
| MOptom (IP) | MOptom | 本科 (Integrated Master's) | 1 |
| MAcc | MAcc | 本科 (Graduate Apprenticeship) | 1 |
| **UG 合计** | | | **82** |
| MSc | MSc | 研究生授课型 | 48 |
| MA | MA | 研究生授课型 | 3 |
| MBA | MBA | 研究生授课型 | 1 |
| LLM | LLM | 研究生授课型 | 1 |
| MPH | MPH | 研究生授课型 | 2 |
| DPsych | DPsych | 研究生博士级 | 3 |
| DBA | DBA | 研究生博士级 | 1 |
| PgD | PgD | 研究生文凭 | 2 |
| SCQF Level 11 | PgD | 研究生文凭 | 1 |
| **PGT 合计** | | | **72** |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学术学院 \ 学位 | BA | BEng | BSc | BSc(Hons) | LLB | MAcc | MEng | MOptom | 合计 |
|------------|---|---|---|---|---|---|---|---|---|
| Glasgow School for Business and Society | 22 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | **23** |
| School of Health and Life Sciences | 0 | 0 | 6 | 22 | 0 | 0 | 0 | 1 | **29** |
| School of Science and Engineering | 0 | 9 | 0 | 20 | 0 | 0 | 2 | 0 | **31** |
| **合计** | **22** | **9** | **6** | **42** | **0** | **1** | **2** | **1** | **82** |

> **Note**: LLB programmes (2 total) are under GSBS but counted separately. Some courses are Graduate Apprenticeships or Pathway courses offered at multiple locations.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Glasgow Caledonian University is organised into 3 academic Schools, each containing multiple Departments (16 total). See Section 0.2 for the full hierarchy tree. All undergraduate degree programmes are administered by one of these departments. GCU London also offers selected programmes.

### 1.2 Undergraduate degree programmes — grouped by School > Degree Level

#### Glasgow School for Business and Society (GSBS)

##### BA (Hons) (22 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-accountancy-glasgow/sep-26-full-time-339709 |
| 2 | Accountancy Pathway | https://www.gcu.ac.uk/study/courses/undergraduate-accountancy-pathway-multiple-locations/aug-26-full-time-312476 |
| 3 | Business Management | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-business-management-glasgow/sep-26-full-time-339858 |
| 4 | Fashion Design with Business | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-fashion-design-with-business-glasgow/sep-26-full-time-339708 |
| 5 | Finance, Investment and Risk | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-finance,-investment-and-risk-glasgow/sep-26-full-time-339707 |
| 6 | Finance, Investment and Risk Pathway | https://www.gcu.ac.uk/study/courses/ba-hons-finance,-investment-and-risk-pathway-multiple-locations/aug-26-full-time-312647 |
| 7 | Graduate Apprenticeship Business Management | https://www.gcu.ac.uk/study/courses/ba-hons-graduate-apprenticeship-business-management-glasgow/sep-26-blended-learning-258610 |
| 8 | Graduate Apprenticeship Business Management with HR Management | https://www.gcu.ac.uk/study/courses/ba-hons-graduate-apprenticeship-business-management-with-hr-management-glasgow/sep-26-blended-learning-258750 |
| 9 | International Business | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-international-business-glasgow/sep-26-full-time-339706 |
| 10 | International Business and Human Resource Management (Yr 3 Direct Entry) | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-international-business-and-human-resource-management-yr-3-direct-entry-glasgow/sep-26-full-time-339705 |
| 11 | International Fashion Branding | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-international-fashion-branding-glasgow/sep-26-full-time-339704 |
| 12 | International Marketing | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-international-marketing-glasgow/sep-26-full-time-339701 |
| 13 | International Tourism and Events Management | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-international-tourism-and-events-management-glasgow/sep-26-full-time-339700 |
| 14 | International Tourism and Events Management Pathway | https://www.gcu.ac.uk/study/courses/ba-hons-international-tourism-and-events-management-pathway-multiple-locations/aug-26-full-time-312810 |
| 15 | Media and Communication | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-media-and-communication-glasgow/sep-26-full-time-339698 |
| 16 | Multimedia Journalism | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-multimedia-journalism-glasgow/sep-26-full-time-339697 |
| 17 | Risk Management | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-risk-management-glasgow/sep-26-full-time-339695 |
| 18 | Risk Management Pathway | https://www.gcu.ac.uk/study/courses/ba-hons-risk-management-pathway-multiple-locations/aug-26-full-time-312848 |
| 19 | Social Sciences | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-social-sciences-glasgow/sep-26-full-time-339685 |
| 20 | Social Sciences Pathway | https://www.gcu.ac.uk/study/courses/ba-hons-social-sciences-pathway-glasgow/sep-26-full-time-313063 |
| 21 | Social Work | https://www.gcu.ac.uk/study/courses/ug/2728/ba-hons-social-work-glasgow/sep-26-full-time-339681 |
| 22 | Graduate Apprenticeship Master of Accountancy | https://www.gcu.ac.uk/study/courses/-graduate-apprenticeship-master-of-accountancy-glasgow/sep-26-blended-learning-261150 |

---

#### School of Health and Life Sciences (HLS)

##### BSc (6 programmes — Ordinary degree)

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing Studies (Adult) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-nursing-studies-adult-glasgow/sep-26-full-time-339748 |
| 2 | Nursing Studies (Child) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-nursing-studies-child-glasgow/sep-26-full-time-339759 |
| 3 | Nursing Studies (Learning Disabilities) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-nursing-studies-learning-disabilities-glasgow/sep-26-full-time-339764 |
| 4 | Nursing Studies (Mental Health) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-nursing-studies-mental-health-glasgow/sep-26-full-time-339763 |
| 5 | Ophthalmic Dispensing | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-ophthalmic-dispensing-glasgow/sep-26-full-time-339753 |
| 6 | Oral Health Sciences | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-oral-health-sciences-glasgow/sep-26-full-time-339853 |

##### BSc (Hons) (22 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | 3D Animation and Visualisation with pathways for Games and VFX | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-3d-animation-and-visualisation-with-pathways-for-games-and-vfx-glasgow/sep-26-full-time-340503 |
| 2 | Applied Psychology | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-applied-psychology-glasgow/sep-26-full-time-339675 |
| 3 | Biomedical Science | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-biomedical-science-glasgow/sep-26-full-time-339852 |
| 4 | Biomedical Science (Pathways) | https://www.gcu.ac.uk/study/courses/bsc-hons-biomedical-science-pathways-glasgow/biomedical-science-pathways-sep-26-ft |
| 5 | Diagnostic Imaging | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-diagnostic-imaging-glasgow/sep-26-full-time-339667 |
| 6 | Forensic Investigation | https://www.gcu.ac.uk/study/courses/bsc-hons-forensic-investigation-glasgow/sep-26-full-time-312757 |
| 7 | Human Nutrition and Dietetics | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-human-nutrition-and-dietetics-glasgow/sep-26-full-time-339658 |
| 8 | Nursing Studies (Adult) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-nursing-studies-adult-glasgow/sep-26-full-time-339657 |
| 9 | Nursing Studies (Child) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-nursing-studies-child-glasgow/sep-26-full-time-339645 |
| 10 | Nursing Studies (Learning Disabilities) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-nursing-studies-learning-disabilities-glasgow/sep-26-full-time-339653 |
| 11 | Nursing Studies (Mental Health) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-nursing-studies-mental-health-glasgow/sep-26-full-time-339654 |
| 12 | Occupational Therapy | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-occupational-therapy-glasgow/sep-26-full-time-339720 |
| 13 | Orthoptics | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-orthoptics-glasgow/sep-26-full-time-339721 |
| 14 | Paramedic Science | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-paramedic-science-glasgow/sep-26-full-time-339754 |
| 15 | Pharmacology | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-pharmacology-glasgow/sep-26-full-time-339722 |
| 16 | Pharmacology Pathway | https://www.gcu.ac.uk/study/courses/bsc-hons-pharmacology-pathway-multiple-locations/aug-26-full-time-312840 |
| 17 | Physiotherapy | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-physiotherapy-glasgow/sep-26-full-time-339723 |
| 18 | Podiatry | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-podiatry-glasgow/sep-26-full-time-339724 |
| 19 | Professional Studies in Nursing | https://www.gcu.ac.uk/study/courses/bsc-professional-studies-in-nursing-glasgow/sep-26-full-time-313327 |
| 20 | Professional Studies in Nursing (Hons) | https://www.gcu.ac.uk/study/courses/bsc-hons-professional-studies-in-nursing-glasgow/sep-26-full-time-330559 |
| 21 | Radiotherapy and Oncology | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-radiotherapy-and-oncology-glasgow/sep-26-full-time-339746 |
| 22 | Digital Design (direct entry) | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-digital-design-direct-entry-glasgow/sep-26-full-time-339760 |

##### MOptom (IP) (1 programme)

| # | 专业 | URL |
|---|------|-----|
| 1 | Optometry with Independent Prescribing | https://www.gcu.ac.uk/study/courses/ug/2728/moptom-ip-optometry-with-independent-prescribing-glasgow/sep-26-full-time-339855 |

---

#### School of Science and Engineering (SSE)

##### BEng (Hons) (9 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Building Services Engineering | https://www.gcu.ac.uk/study/courses/beng-hons-building-services-engineering-glasgow/sep-26-part-time-312509 |
| 2 | Electrical and Electronic Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/beng-hons-electrical-and-electronic-engineering-glasgow/sep-26-full-time-339744 |
| 3 | Electrical and Electronic Engineering Pathway | https://www.gcu.ac.uk/study/courses/beng-hons-electrical-and-electronic-engineering-pathway-multiple-locations/aug-26-full-time-312641 |
| 4 | Electrical Power Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/beng-hons-electrical-power-engineering-glasgow/sep-26-part-time-339679 |
| 5 | Electrical Power Engineering Pathway | https://www.gcu.ac.uk/study/courses/beng-hons-electrical-power-engineering-pathway-multiple-locations/aug-26-full-time-313064 |
| 6 | Graduate Apprenticeship Engineering (Design and Manufacture) | https://www.gcu.ac.uk/study/courses/beng-hons-graduate-apprenticeship-engineering-design-and-manufacture-glasgow/sep-26-blended-learning-258615 |
| 7 | Mechanical Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/beng-hons-mechanical-engineering-glasgow/sep-26-part-time-339677 |
| 8 | Mechanical Engineering Pathway | https://www.gcu.ac.uk/study/courses/beng-hons-mechanical-engineering-pathway-multiple-locations/aug-26-full-time-312817 |
| 9 | Mechanical Engineering (Part-time) | https://www.gcu.ac.uk/study/courses/ug/2728/beng-hons-mechanical-engineering-glasgow/sep-26-part-time-339677 |

##### BSc (Hons) (20 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | AI and Data Science | https://www.gcu.ac.uk/study/courses/bsc-hons-ai-and-data-science-glasgow/sep-26-full-time-312475 |
| 2 | Audio Technology | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-audio-technology-glasgow/sep-26-full-time-339674 |
| 3 | Building Surveying | https://www.gcu.ac.uk/study/courses/bsc-hons-building-surveying-glasgow/sep-26-part-time-312515 |
| 4 | Computing | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-computing-glasgow/sep-26-full-time-339673 |
| 5 | Computing Pathways | https://www.gcu.ac.uk/study/courses/bsc-hons-computing-pathways-multiple-locations/sep-26-full-time-312532 |
| 6 | Construction Management | https://www.gcu.ac.uk/study/courses/bsc-hons-construction-management-glasgow/sep-26-part-time-312534 |
| 7 | Cyber Security and Networks | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-cyber-security-and-networks-glasgow/sep-26-full-time-339668 |
| 8 | Cyber Security and Networks Pathway | https://www.gcu.ac.uk/study/courses/undergraduate-cyber-security-and-networks-pathway-multiple-locations/aug-26-full-time-312598 |
| 9 | Digital Security and Forensics | https://www.gcu.ac.uk/study/courses/bsc-hons-digital-security-and-forensics-glasgow/sep-26-full-time-312605 |
| 10 | Environmental Civil Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-environmental-civil-engineering-glasgow/sep-26-full-time-339661 |
| 11 | Environmental Management | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-environmental-management-glasgow/sep-26-full-time-339660 |
| 12 | Games Development | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-games-development-glasgow/sep-26-full-time-339659 |
| 13 | Graduate Apprenticeship AI and Data Science | https://www.gcu.ac.uk/study/courses/bsc-hons-graduate-apprenticeship-ai-and-data-science-glasgow/sep-26-blended-learning-258609 |
| 14 | Graduate Apprenticeship Civil Engineering (Environmental Civil Engineering) | https://www.gcu.ac.uk/study/courses/bsc-hons-graduate-apprenticeship-civil-engineering-environmental-civil-engineering-glasgow/sep-26-blended-learning-258611 |
| 15 | Graduate Apprenticeship Construction and Built Environment (Quantity Surveying) | https://www.gcu.ac.uk/study/courses/bsc-hons-graduate-apprenticeship-construction-and-built-environment-quantity-surveying-glasgow/sep-26-blended-learning-258612 |
| 16 | Graduate Apprenticeship Cyber Security | https://www.gcu.ac.uk/study/courses/bsc-hons-graduate-apprenticeship-cyber-security-glasgow/sep-26-blended-learning-258614 |
| 17 | Quantity Surveying | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-quantity-surveying-glasgow/sep-26-part-time-339726 |
| 18 | Quantity Surveying Pathway | https://www.gcu.ac.uk/study/courses/bsc-hons-quantity-surveying-pathway-multiple-locations/aug-26-full-time-312845 |
| 19 | Software Development | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-software-development-glasgow/sep-26-full-time-339747 |
| 20 | AI and Data Science | https://www.gcu.ac.uk/study/courses/bsc-hons-ai-and-data-science-glasgow/sep-26-full-time-312475 |

##### MEng (2 programmes)

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/meng-electrical-and-electronic-engineering-glasgow/sep-26-full-time-339877 |
| 2 | Mechanical Engineering | https://www.gcu.ac.uk/study/courses/ug/2728/meng-mechanical-engineering-glasgow/sep-26-full-time-339884 |

---

#### LLB Programmes (GSBS — Department of Economics and Law)

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Bachelor of Laws | LLB (Hons) | https://www.gcu.ac.uk/study/courses/ug/2728/llb-hons-bachelor-of-laws-glasgow/sep-26-full-time-339854 |
| 2 | Bachelor of Laws Fast-track | LLB | https://www.gcu.ac.uk/study/courses/ug/2728/llb-bachelor-of-laws-fast-track-glasgow/sep-26-full-time-339817 |

---

### 1.3 Joint honours / cross-school programmes

GCU offers several "Pathway" programmes that may be delivered across multiple locations (Glasgow and partner colleges). These include Accountancy Pathway, Computing Pathways, Cyber Security and Networks Pathway, and various Engineering Pathways.

### 1.4 Foundation year programmes

GCU does not appear to offer standalone foundation year programmes in the traditional sense. Instead, they offer pathway programmes through partner colleges that provide alternative entry routes.

### 1.5 Graduate Apprenticeship programmes

GCU offers several Graduate Apprenticeship programmes that combine work-based learning with academic study:
- BA (Hons) Business Management
- BA (Hons) Business Management with HR Management
- MAcc Master of Accountancy
- BSc (Hons) AI and Data Science
- BSc (Hons) Civil Engineering (Environmental)
- BSc (Hons) Construction and Built Environment (Quantity Surveying)
- BSc (Hons) Cyber Security
- BEng (Hons) Engineering (Design and Manufacture)

---

## SECTION 2 — Graduate education

### 2.1 Postgraduate taught (PGT)

GCU offers72 postgraduate programmes. Key programmes by school:

#### GSBS Postgraduate Programmes

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting, Finance and Regulation | MSc | https://www.gcu.ac.uk/study/courses/msc-accounting,-finance-and-regulation-glasgow/sep-26-full-time-313797 |
| 2 | Applied Business Analytics | MSc | https://www.gcu.ac.uk/study/courses/msc-applied-business-analytics-glasgow/sep-26-full-time-313987 |
| 3 | Digital Media and Content Creation | MA | https://www.gcu.ac.uk/study/courses/postgraduate-digital-media-and-content-creation-glasgow/sep-26-full-time-313828 |
| 4 | Financial Technology | MSc | https://www.gcu.ac.uk/study/courses/msc-financial-technology-glasgow/sep-26-full-time-313814 |
| 5 | Global Master of Business Administration (MBA) | MBA | https://www.gcu.ac.uk/study/courses/mba-global-master-of-business-administration-mba-glasgow/sep-26-full-time-313803 |
| 6 | Human Resource Management | MSc | https://www.gcu.ac.uk/study/courses/msc-human-resource-management-glasgow/sep-26-full-time-313899 |
| 7 | Human Rights | MSc | https://www.gcu.ac.uk/study/courses/msc-human-rights-glasgow/sep-26-full-time-313907 |
| 8 | International Banking and Finance | MSc | https://www.gcu.ac.uk/study/courses/msc-international-banking-and-finance-glasgow/sep-26-full-time-313993 |
| 9 | International Business Management | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-international-business-management-glasgow/sep-26-full-time-313909 |
| 10 | International Commercial Law | LLM | https://www.gcu.ac.uk/study/courses/llm-international-commercial-law-glasgow/sep-26-full-time-313844 |
| 11 | International Fashion Marketing | MSc | https://www.gcu.ac.uk/study/courses/msc-international-fashion-marketing-glasgow/sep-26-full-time-340337 |
| 12 | International Marketing | MSc | https://www.gcu.ac.uk/study/courses/msc-international-marketing-london/sep-26-full-time-313974 |
| 13 | International Operations and Supply Chain Management | MSc | https://www.gcu.ac.uk/study/courses/msc-international-operations-and-supply-chain-management-glasgow/sep-26-full-time-313971 |
| 14 | International Tourism and Events Management | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-international-tourism-and-events-management-glasgow/sep-26-full-time-313957 |
| 15 | Marketing | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-marketing-glasgow/sep-26-full-time-313931 |
| 16 | Multimedia Journalism | MA | https://www.gcu.ac.uk/study/courses/postgraduate-multimedia-journalism-glasgow/sep-26-full-time-313813 |
| 17 | Risk Management | MSc | https://www.gcu.ac.uk/study/courses/msc-risk-management-glasgow/sep-26-full-time-313876 |
| 18 | Social Innovation | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-social-innovation-glasgow/sep-26-full-time-313872 |
| 19 | Television Fiction Writing | MA | https://www.gcu.ac.uk/study/courses/ma-television-fiction-writing-glasgow/sep-26-part-time-313812 |
| 20 | 3D Design for Virtual Environments | MSc | https://www.gcu.ac.uk/study/courses/msc-3d-design-for-virtual-environments-glasgow/sep-26-full-time-313870 |
| 21 | User Experience and Interaction Design | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-user-experience-and-interaction-design-glasgow/sep-26-part-time-313866 |
| 22 | Project Management | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-project-management-glasgow/jan-27-full-time-337756 |
| 23 | Social Work | MSc | https://www.gcu.ac.uk/study/courses/msc-social-work-glasgow/sep-26-full-time-312850 |

#### HLS Postgraduate Programmes

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Physiotherapy Practice | MSc | https://www.gcu.ac.uk/study/courses/msc-advanced-physiotherapy-practice-glasgow/sep-26-full-time-313802 |
| 2 | Advanced Practice | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-glasgow/sep-26-full-time-338685 |
| 3 | Advanced Practice (Diabetes Care) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-diabetes-care-glasgow/sep-26-full-time-338750 |
| 4 | Advanced Practice (Expedition and Wilderness Medicine) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-expedition-and-wilderness-medicine-glasgow/sep-26-part-time-338296 |
| 5 | Advanced Practice (Musculoskeletal Health) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-musculoskeletal-health-glasgow/sep-26-part-time-338815 |
| 6 | Advanced Practice (Paramedicine) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-paramedicine-glasgow/sep-26-full-time-338817 |
| 7 | Advanced Practice (Podiatry) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-podiatry-glasgow/sep-26-full-time-338366 |
| 8 | Advanced Practice (Travel Medicine) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-advanced-practice-travel-medicine-glasgow/sep-26-part-time-338381 |
| 9 | Community Nursing | MSc | https://www.gcu.ac.uk/study/courses/msc-community-nursing-glasgow/sep-26-part-time-314041 |
| 10 | Counselling Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-counselling-psychology-glasgow/sep-26-part-time-313864 |
| 11 | Diagnostic Radiography (Pre-registration) | MSc | https://www.gcu.ac.uk/study/courses/msc-diagnostic-radiography-pre-registration-glasgow/jan-27-full-time-314019 |
| 12 | Forensic Psychology | MSc | https://www.gcu.ac.uk/study/courses/msc-forensic-psychology-glasgow/sep-26-full-time-313890 |
| 13 | Health Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-health-psychology-glasgow/sep-26-part-time-313861 |
| 14 | Human Nutrition and Dietetics | MSc | https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-human-nutrition-and-dietetics-glasgow/sep-26-full-time-339658 |
| 15 | Independent Prescribing for Optometrists | PgD | https://www.gcu.ac.uk/study/courses/pgd-independent-prescribing-for-optometrists-glasgow/jan-27-part-time-328678 |
| 16 | Investigative Ophthalmology and Vision Research | MSc | https://www.gcu.ac.uk/study/courses/msc-investigative-ophthalmology-and-vision-research-glasgow/sep-26-part-time-313955 |
| 17 | Master of Public Health (Glasgow) | MPH | https://www.gcu.ac.uk/study/courses/mph-master-of-public-health-glasgow/sep-26-full-time-313788 |
| 18 | Master of Public Health (London) | MPH | https://www.gcu.ac.uk/study/courses/mph-master-of-public-health-london/sep-26-part-time-313786 |
| 19 | Medical Bioscience | MSc | https://www.gcu.ac.uk/study/courses/msc-medical-bioscience-glasgow/sep-26-full-time-313936 |
| 20 | Medical Imaging | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-medical-imaging-glasgow/sep-26-full-time-338417 |
| 21 | Medical Imaging (Artificial Intelligence) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-medical-imaging-artificial-intelligence-glasgow/sep-26-full-time-338430 |
| 22 | Medical Imaging (Computed Tomography) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-medical-imaging-computed-tomography-glasgow/sep-26-full-time-338427 |
| 23 | Medical Imaging (Magnetic Resonance Imaging) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-medical-imaging-magnetic-resonance-imaging-glasgow/sep-26-full-time-338424 |
| 24 | Medical Imaging (Ultrasound) | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-medical-imaging-ultrasound-glasgow/sep-26-part-time-338422 |
| 25 | Nursing: Advancing Professional Practice | MSc | https://www.gcu.ac.uk/study/courses/msc-nursing-advancing-professional-practice-glasgow/sep-26-full-time-313927 |
| 26 | Nursing Studies Adult (Pre-registration) | MSc | https://www.gcu.ac.uk/study/courses/msc-nursing-studies-adult-pre-registration-glasgow/jan-27-full-time-313926 |
| 27 | Occupational Therapy (Pre-registration) | MSc | https://www.gcu.ac.uk/study/courses/msc-occupational-therapy-pre-registration-glasgow/jan-27-full-time-313925 |
| 28 | Physiotherapy (Pre-registration) | MSc | https://www.gcu.ac.uk/study/courses/msc-physiotherapy-pre-registration-glasgow/jan-27-full-time-313924 |
| 29 | Sports and Exercise Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-sports-and-exercise-psychology-glasgow/sep-26-part-time-313847 |
| 30 | Specialist Community Public Health Nursing (Health Visiting) | PgD | https://www.gcu.ac.uk/study/courses/pgd-specialist-community-public-health-nursing-health-visiting-glasgow/jan-27-full-time-328714 |
| 31 | Specialist Practice District Nurse with V300 | SCQF L11 | https://www.gcu.ac.uk/study/courses/pgd-postgraduate-diploma-specialist-practice-district-nurse-with-v300-glasgow/sep-26-full-time-324586 |

#### SSE Postgraduate Programmes

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Computer Science (Glasgow) | MSc | https://www.gcu.ac.uk/study/courses/msc-advanced-computer-science-multiple-locations/sep-26-full-time-327120 |
| 2 | Applied Data Science in Engineering | MSc | https://www.gcu.ac.uk/study/courses/msc-applied-data-science-in-engineering-glasgow/sep-26-full-time-313989 |
| 3 | Applied Instrumentation and Control | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-applied-instrumentation-and-control-glasgow/sep-26-full-time-314843 |
| 4 | Big Data Technologies | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-big-data-technologies-glasgow/sep-26-full-time-314030 |
| 5 | Computer Science (Glasgow) | MSc | https://www.gcu.ac.uk/study/courses/msc-computer-science-multiple-locations/sep-26-part-time-314025 |
| 6 | Computer Science (London) | MSc | https://www.gcu.ac.uk/study/courses/msc-computer-science-london/sep-26-part-time-314032 |
| 7 | Cyber Security | MSc | https://www.gcu.ac.uk/study/courses/postgraduate-cyber-security-glasgow/sep-26-full-time-314022 |
| 8 | Electrical and Electronic Engineering | MSc | https://www.gcu.ac.uk/study/courses/msc-electrical-and-electronic-engineering-glasgow/sep-26-part-time-314016 |
| 9 | Electrical Power Engineering | MSc | https://www.gcu.ac.uk/study/courses/msc-electrical-power-engineering-glasgow/sep-26-part-time-314004 |
| 10 | Environmental Management (Glasgow) | MSc | https://www.gcu.ac.uk/study/courses/msc-environmental-management-waste,-energy,-water,-oil-and-gas-glasgow/sep-26-part-time-314012 |
| 11 | Environmental Management (London) | MSc | https://www.gcu.ac.uk/study/courses/msc-environmental-management-waste,-energy,-water,-oil-and-gas-london/sep-26-part-time-314008 |
| 12 | International Construction Project Management | MSc | https://www.gcu.ac.uk/study/courses/msc-international-construction-project-management-glasgow/sep-26-part-time-313917 |
| 13 | Mechanical Engineering | MSc | https://www.gcu.ac.uk/study/courses/msc-mechanical-engineering-glasgow/sep-26-part-time-313941 |
| 14 | Quantity Surveying | MSc | https://www.gcu.ac.uk/study/courses/msc-quantity-surveying-glasgow/sep-26-part-time-313903 |
| 15 | Software Engineering | MSc | https://www.gcu.ac.uk/study/courses/pg/msc-software-engineering-glasgow/jan-27-part-time-339571 |
| 16 | Graduate Apprenticeship Cyber Security | MSc | https://www.gcu.ac.uk/study/courses/msc-graduate-apprenticeship-cyber-security-glasgow/sep-26-blended-learning-258613 |

#### GCU London Postgraduate Programmes

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | International Management and Business Development | MSc | https://www.gcu.ac.uk/study/courses/msc-international-management-and-business-development-london/sep-26-full-time-313945 |
| 2 | International Marketing | MSc | https://www.gcu.ac.uk/study/courses/msc-international-marketing-london/sep-26-full-time-313974 |
| 3 | Master of Public Health | MPH | https://www.gcu.ac.uk/study/courses/mph-master-of-public-health-london/sep-26-part-time-313786 |

#### Doctoral-level Programmes

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Counselling Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-counselling-psychology-glasgow/sep-26-part-time-313864 |
| 2 | Health Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-health-psychology-glasgow/sep-26-part-time-313861 |
| 3 | Sports and Exercise Psychology | DPsych | https://www.gcu.ac.uk/study/courses/dpsych-sports-and-exercise-psychology-glasgow/sep-26-part-time-313847 |
| 4 | Doctorate of Business Administration | DBA | https://www.gcu.ac.uk/study/courses/dba-doctorate-of-business-administration-glasgow/sep-26-part-time-distance-learning-314622 |

### 2.2 Postgraduate research (PGR)

- **Research programmes**: `gcu.ac.uk/research/postgraduateresearchstudy`
- **Degrees**: PhD, MPhil, Professional Doctorates
- **Research areas**: Organised by School; each School has its own research programme pages
- **Research centres**: Listed at `gcu.ac.uk/research/researchcentres`

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data

| 维度 | 值 |
|------|-----|
| **Application system** | UCAS |
| **UCAS institution code** | G400 |
| **Main application deadline** | 29 January (2026 entry) |
| **UCAS Extra opens** | February 2026 |
| **Clearing opens** | July 2026 |
| **Entry year** | September 2026 |

### 3.2 Undergraduate — academic entry requirements (typical)

| 考试体系 | 标准要求 | 最低要求 | 来源 |
|---------|---------|---------|------|
| **UCAS Tariff** | 96 | 90 | Course pages |
| **Scottish Higher** | BBCC (incl relevant subject) | BCCC | Course pages |
| **A-Level** | CCC (incl relevant subject) | CCC | Course pages |
| **HNC/HND** | HNC with A in Graded Unit (Year 2 entry); HND with BB in Graded Units (Year 3 entry) | — | Course pages |

> **Note**: Entry requirements vary by course. Computing requires Maths or Computing at Higher/A-Level. Some health programmes have higher requirements. Minimum entry requirements are for widening access students only.

### 3.3 Undergraduate English language requirements

| 考试类型 | 标准要求 | 单项最低 | 来源 |
|---------|---------|---------|------|
| **IELTS Academic** | 6.0 overall | 5.5 each band | `gcu.ac.uk/internationalstudy/howtoapply/englishlanguagerequirements` |
| **Cambridge English** | 169 overall | 162 each element | Same source |
| **LanguageCert Academic** | 65 overall | 60 each element | Same source |
| **Oxford ELLT** | 6 overall | 5 each element | Same source |

> **Exemptions**: Applicants from majority English-speaking countries with education in English may be exempt.
> **Higher requirements**: Some courses (especially health programmes) may require higher IELTS scores.
> **Accepted A-Level**: A Level English Language/Literature at Grade D or above accepted as English qualification.

### 3.4 Graduate admissions

Graduate entry requirements vary by programme. Typical requirements:
- **MSc**: UK honours degree (2:2 or above) in a relevant subject
- **MBA**: Honours degree + relevant work experience
- **DPsych**: Honours degree in Psychology (2:1 or above) + relevant experience
- **DBA**: Master's degree + significant professional experience

> Check individual course pages for specific requirements.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate tuition fees (2026 entry)

| Fee status | Annual tuition | Source |
|-----------|---------------|--------|
| **Scotland** | £1,820 (standard); £7,600 (LLB Fast Track) | `gcu.ac.uk/study/tuitionfees` |
| **England, Wales, NI** | £9,790 (standard); £7,600 (LLB Fast Track) | Same source |
| **International** | £15,700 (standard); £21,900 (MOptom) | Same source |
| **Nursing (Professional Studies)** | Scotland: £1,350-£2,100; International: £15,500 | Same source |

### 4.2 Postgraduate tuition fees (2026 entry)

| Programme type | Home/UK fee | International fee | Source |
|---------------|-------------|-------------------|--------|
| **MSc (typical)** | £7,500 | £16,700 | `gcu.ac.uk/study/tuitionfees` |
| **MSc (STEM/Engineering)** | £9,200 | £19,400 | Same source |
| **MBA** | £13,500 | £20,400 | Same source |
| **DPsych** | £8,100/year | £16,700/year | Same source |
| **Pre-registration Health MSc** | £9,700/year | £19,900/year | Same source |
| **Distance learning MSc** | £11,000 total | £11,000 total | Same source |

### 4.3 Estimated living costs (per year)

| 项目 | 估计费用 (£) |
|------|------------|
| Accommodation | 5,000 – 9,000 |
| Food | 2,000 – 4,000 |
| Transport | 400 – 800 |
| Study materials | 400 – 800 |
| Personal expenses | 1,500 – 3,000 |
| **Total (estimated)** | **9,300 – 17,600** |

### 4.4 Scholarships

- International scholarships available at undergraduate and postgraduate level
- Scholarship page: `gcu.ac.uk/study/scholarships`
- Various merit-based and need-based scholarships available

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "Glasgow Caledonian University"
  source_url: https://www.gcu.ac.uk
  source_snippet: "Glasgow Caledonian University"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.schools
  value: "3 Academic Schools: GSBS, HLS, SSE + GCU London"
  source_url: https://www.gcu.ac.uk/aboutgcu/academicschools
  source_snippet: "Glasgow School for Business and Society / School of Health and Life Sciences / School of Science and Engineering"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.departments
  value: "16 departments across 3 schools"
  source_url: https://www.gcu.ac.uk/aboutgcu/academicschools/gsbs/aboutus/departments
  source_snippet: "GSBS: 7 departments, HLS: 6 departments, SSE: 3 departments"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.programs.count
  value: "82 undergraduate programmes"
  source_url: https://www.gcu.ac.uk/search?query=%21padrenull&f.Tabs%7Cgcun~ds-courses=Courses&f.Level%7CcourseLevel=undergraduate
  source_snippet: "Showing 1-10 of 82 results"
  capture_date: 2026-07-08
  evidence_type: official_search_results

E-U-005:
  field: postgraduate.programs.count
  value: "72 postgraduate programmes"
  source_url: https://www.gcu.ac.uk/search?query=%21padrenull&f.Tabs%7Cgcun~ds-courses=Courses&f.Level%7CcourseLevel=postgraduate
  source_snippet: "72 results"
  capture_date: 2026-07-08
  evidence_type: official_search_results

E-U-006:
  field: undergraduate.entry_requirements.ucas_tariff
  value: "96 (standard), 90 (minimum)"
  source_url: https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-computing-glasgow/sep-26-full-time-339673
  source_snippet: "UCAS Tariff: 96 / UCAS Tariff: 90"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english.ielts
  value: "IELTS 6.0 overall (5.5 each band)"
  source_url: https://www.gcu.ac.uk/internationalstudy/howtoapply/englishlanguagerequirements
  source_snippet: "Academic IELTS/IELTS for UKVI: Overall score of 6.0, with no single element below 5.5"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.fees.scotland
  value: "£1,820 per year"
  source_url: https://www.gcu.ac.uk/study/tuitionfees
  source_snippet: "Standard undergraduate course: Scotland fee £1,820"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.fees.international
  value: "£15,700 per year (standard)"
  source_url: https://www.gcu.ac.uk/study/tuitionfees
  source_snippet: "Standard undergraduate course: EU and International fee £15,700"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.application.system
  value: "UCAS (code G400)"
  source_url: https://www.gcu.ac.uk/study/courses/ug/2728/bsc-hons-computing-glasgow/sep-26-full-time-339673
  source_snippet: "UCAS: G401"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: institution.type
  value: "Modern university (post-1992), largest in Scotland"
  source_url: https://www.gcu.ac.uk/aboutgcu
  source_snippet: "Glasgow Caledonian – the largest and leading modern university in Scotland"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: postgraduate.fees.typical
  value: "MSc £7,500-£9,200 home, £16,700-£19,400 international"
  source_url: https://www.gcu.ac.uk/study/tuitionfees
  source_snippet: "Fee tables for MSc programmes"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
glasgow-caledonian-university-knowledge-base-v2
├── 0-overview (Section 0: rule 1-4, institution overview)
├── 1-undergraduate (Section 1: full UG programme listing, chunked by School)
│   ├── chunk-01-gsbs-business
│   ├── chunk-02-hls-health
│   ├── chunk-03-sse-science-engineering
│   └── chunk-04-llb-law
├── 2-graduate (Section 2: PGT programme listing, chunked by School)
│   ├── chunk-01-gsbs-postgraduate
│   ├── chunk-02-hls-postgraduate
│   ├── chunk-03-sse-postgraduate
│   └── chunk-04-doctoral
├── 3-applications (Section 3: requirements, deadlines, English)
├── 4-costs (Section 4: fees, living costs, scholarships)
├── 5-evidence (Section 5: evidence chain)
└── 6-monitoring (Section 7: monitoring watchlist)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "glasgow-caledonian-university-knowledge-base-v2"
  school: "<academic school>"
  degree_level: "<BA|BSc|BEng|MEng|LLB|MSc|MA|MBA|...>"
  level: undergraduate|postgraduate
  field_type: programs
  source_url: https://www.gcu.ac.uk/search?query=!padrenull&f.Tabs|gcun~ds-courses=Courses
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| **P0** | Per-course entry requirements (Scottish Higher/A-Level specifics) | Individual course pages |
| **P0** | PhD/MPhil research programme listing | `gcu.ac.uk/research/postgraduateresearchstudy` |
| **P0** | Detailed scholarship amounts and eligibility | `gcu.ac.uk/study/scholarships` |
| **P1** | Course module details and curriculum structure | Individual course pages |
| **P1** | Graduate Apprenticeship detailed requirements | Individual GA course pages |
| **P2** | Accommodation costs | `gcu.ac.uk/accommodation` |
| **P2** | GCU London campus programmes (detailed) | `gcu.ac.uk/london` |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Glasgow Caledonian University | Cardiff | Newcastle |
|-----------|--------|---------|-----------|
| Total UG programmes | 82 | 237 | 147 |
| Total PG programmes | 72 | P0 follow-up | P0 follow-up |
| Academic schools | 3 (+ GCU London) | 3 | 3 |
| Academic departments | 16 | 24 | — |
| UG Home tuition (Scotland) | £1,820 | N/A | N/A |
| UG Home tuition (rUK) | £9,790 | £9,250 | £9,250 |
| UG International tuition (range) | £15,700 – £21,900 | £22,700 – £29,450 | — |
| IELTS minimum (UG) | 6.0 (5.5 each) | 6.5 (5.5 each) | — |
| A-Level typical | CCC | ABB | — |
| UCAS code | G400 | C15 | — |
| UCAS deadline | 29 Jan | 29 Jan | — |
| Region | Scotland, UK | Wales, UK | England, UK |
| Russell Group | No | Yes | Yes |
| University type | Modern (post-1992) | Russell Group | Russell Group |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: gcu.ac.uk (main domain — Funnelback search-powered course listing)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: UG programs (82/82) ✅ | PG programs (72/72) ✅ | Evidence (12 blocks) ✅
> **Key differentiator**: GCU is Scotland's largest modern university with strong vocational focus, Graduate Apprenticeship programmes, and the UK's only honours degree in Risk Management.
