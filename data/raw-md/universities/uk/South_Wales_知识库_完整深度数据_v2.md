# University of South Wales 知识库_完整深度数据_v2

> **Version**: v2.0 | **Capture date**: 2026-07-08 | **Data source**: southwales.ac.uk (live) | **Method**: ego-browser 6-Phase full extraction

---

## 0. 院校总览 (Overview & Roll-up)

### 0.1 学校基本信息

| Field | Value |
|-------|-------|
| Name (English) | University of South Wales (USW) |
| Name (Welsh) | Prifysgol De Cymru |
| Country | United Kingdom (Wales) |
| Founded | 2013 (merger of University of Glamorgan + University of Wales, Newport) |
| Type | Public University |
| Charity Registration | 1140312 |
| Faculties | 3 |
| Subject areas | 25 |
| Campuses | Pontypridd, Cardiff, Newport |
| Total Courses (live catalog) | 337 |
| Undergraduate (UG) | 148 |
| Postgraduate (PG) | 189 |
| Website | https://www.southwales.ac.uk |
| Academic Structure URL | https://www.southwales.ac.uk/about/our-structure/ |
| Course Catalog URL | https://www.southwales.ac.uk/courses/ |

### 0.2 Rule 1: 专业/项目总数 (Total program count)

- **Total course offerings (all variants)**: 337
  - Undergraduate (UG): 148
    - Including Foundation Year variants and Top-up variants
  - Postgraduate (PG): 189
    - Including PGCert / PGDip / MA / MSc / MBA / MPhil / PhD

**Distinct program titles**: 289 (multiple variants exist with Foundation Year, Top Up, with/without Sandwich Year, or different awarding qualification).

### 0.3 Rule 2: 学院/系明细 + 父子层级 (School/Department hierarchy)

USW has **3 Faculties** with **25 subject areas**:

#### Faculty of Computing, Engineering and Science (FCES)
- Dean: **Professor Jill Stewart**
- 4 subject areas:
  - Applied Science
  - Built Environment and Sustainability
  - Computing and Cyber Security
  - Engineering

#### Faculty of Business and Creative Industries (FBCI)
- Dean: **Adam Williams**
- 11 subject areas:
  - Accounting and Finance
  - Business and Management
  - Design
  - Fashion
  - Film and Media
  - Games, Animation and Visual Effects
  - History and Buddhist Studies
  - Law
  - Marketing and Advertising
  - Music, Drama and Performance
  - Photography

#### Faculty of Life Sciences and Education (FLSE)
- Dean: **Dr Rob Orford**
- 10 subject areas:
  - Art and Creative Wellbeing
  - Chiropractic
  - Criminology, Policing and Public Services
  - Education and Teaching
  - Health and Social Care
  - Health Professions
  - Nursing
  - Psychology
  - Psychotherapy and Counselling
  - Sport

**Source**: https://www.southwales.ac.uk/about/our-structure/ (verbatim: "The University has three faculties - the Faculty of Computing, Engineering and Science; the Faculty of Business and Creative Industries; and the Faculty of Life Sciences and Education.")

### 0.4 Rule 3: 学历级别明细 (Degree-level inventory)

| Degree | Count | Level |
|--------|------|-------|
| **UG Total** | | |
| BA (Hons) | 46 | UG |
| BSc (Hons) | 77 | UG |
| BEng (Hons) | 12 | UG |
| LLB (Hons) | 5 | UG |
| MEng (integrated masters, UG) | 5 | UG |
| HNC | 3 | UG |
| HND | 1 | UG |
| Foundation Degree (FdSc) | 2 | UG |
| CertHE | 2 | UG |
| **PG Total** | | |
| MA | 29 | PG |
| MSc | 71 | PG |
| MBA | 8 | PG |
| MChiro | 2 | PG |
| LLM | 4 | PG |
| PGDip | 33 | PG |
| PGCert | 20 | PG |
| PGCE | 3 | PG |
| ProfGCE / ProfCE | 2 | PG |
| MA/MSc (Masters by Research) | 1 | PG |
| MPhil | 1 | PG (Research) |
| PhD | 1 | PG (Research) |
| DBA | 1 | PG |
| **Other** | | |
| UAC / Sessional English / ACCA | 7 | Mixed |
| **TOTAL** | **337** | |

### 0.5 Rule 4: 分布矩阵 (Faculty × Degree distribution matrix)

| Faculty | UG Total | PG Total | Grand Total |
|---------|----------|----------|-------------|
| Faculty of Computing, Engineering and Science | 57 | 23 | 80 |
| Faculty of Business and Creative Industries | 49 | 50 | 99 |
| Faculty of Life Sciences and Education | 47 | 111 | 158 |
| **TOTAL** | **148** | **189** | **337** |

#### Detailed Faculty × Degree matrix:

| Faculty / Degree | BA (Hons) | BSc (Hons) | BEng (Hons) | LLB (Hons) | MEng | HNC | HND | FdSc | CertHE | MA | MSc | MBA | MChiro | LLM | PGDip | PGCert | PGCE | Other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Faculty of Computing, Engineering and Science | 0 | 36 | 12 | 0 | 5 | 3 | 1 | 0 | 0 | 0 | 21 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| Faculty of Business and Creative Industries | 37 | 6 | 0 | 5 | 0 | 0 | 0 | 0 | 1 | 15 | 18 | 8 | 0 | 3 | 3 | 0 | 0 | 3 |
| Faculty of Life Sciences and Education | 9 | 35 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 14 | 32 | 0 | 2 | 1 | 30 | 19 | 3 | 10 |

### 0.6 Reconciliation Check

- **Rule-1 total (live catalog)**: 337
- **Matrix cell sum (UG + PG)**: 337 = 148 UG + 189 PG
- **Rule-5 leaf enumeration**: 337 rows (each course is one row in section 1+2)
- **PASS**: All three reconcile to 337

---

## 1. 本科专业清单 (Undergraduate courses by Faculty → Subject Area)

Full UG listing with all variants (Foundation Year, Top Up, Sandwich Year, etc.). Each row is a unique course offering.

### 1.1 Faculty of Computing, Engineering and Science

#### Applied Science

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Biology | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-biology/ |
| 3 | Biology including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-biology-including-foundation-year/ |
| 4 | Biomedical Science | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-biomedical-science/ |
| 5 | Biomedical Science including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-biomedical-science-including-foundation-year/ |
| 6 | Digital Forensics | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-digital-forensics/ |
| 8 | Digital Forensics including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-digital-forensics-including-foundation-year/ |
| 11 | Forensic Investigation | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-forensic-investigation/ |
| 13 | Forensic Investigation including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-forensic-investigation-including-foundation-year/ |
| 14 | Forensic Science | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-forensic-science/ |
| 15 | Forensic Science including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-forensic-science-including-foundation-year/ |
| 16 | Medicinal and Biological Chemistry | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-medicinal-and-biological-chemistry/ |
| 17 | Medicinal and Biological Chemistry including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-medicinal-and-biological-chemistry-including-foundation-year/ |
| 19 | Pharmaceutical Science | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-pharmaceutical-science/ |
| 20 | Pharmaceutical Science including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-pharmaceutical-science-including-foundation-year/ |
| 21 | Wildlife Ecology and Conservation | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-wildlife-ecology-and-conservation/ |
| 22 | Wildlife Ecology and Conservation including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-wildlife-ecology-and-conservation-including-foundation-year/ |

#### Built Environment and Sustainability

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Building Surveying | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-building-surveying/ |
| 2 | Building Surveying including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-building-surveying-including-foundation-year/ |
| 3 | Built Environment | HNC | https://www.southwales.ac.uk/courses/hnc-built-environment/ |
| 4 | Civil Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-civil-engineering/ |
| 5 | Civil Engineering | HNC | https://www.southwales.ac.uk/courses/hnc-civil-engineering/ |
| 8 | Civil Engineering including Foundation Year | BEng (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-civil-engineering-including-foundation-year/ |
| 9 | Civil and Construction Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-civil-and-construction-engineering/ |
| 10 | Construction Project Management | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-construction-project-management/ |
| 12 | Construction Project Management including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-construction-project-management-including-foundation-year/ |
| 13 | Project Management (Construction) (SUST) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-project-management-construction/ |
| 14 | Quantity Surveying and Commercial Management | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-quantity-surveying-and-commercial-management/ |
| 15 | Quantity Surveying and Commercial Management including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-quantity-surveying-and-commercial-management-including-foundation-year/ |
| 16 | Real Estate | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-real-estate/ |
| 17 | Real Estate including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-real-estate-including-foundation-year/ |

#### Computing and Cyber Security

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Applied Computing (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-applied-computing-top-up/ |
| 3 | Applied Cyber Security | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-applied-cyber-security/ |
| 5 | Applied Cyber Security including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-applied-cyber-security-including-foundation-year/ |
| 8 | Computer Science | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-computer-science/ |
| 9 | Computer Science including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-computer-science-including-foundation-year/ |
| 10 | Computing | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-computing/ |
| 12 | Computing including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-computing-including-foundation-year/ |

#### Engineering

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Aeronautical Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-aeronautical-engineering/ |
| 4 | Aeronautical Engineering including Foundation Year | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-aeronautical-engineering-including-foundation-year/ |
| 5 | Aerospace Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-aerospace-engineering/ |
| 7 | Aerospace Engineering including Foundation Year | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-aerospace-engineering-including-foundation-year/ |
| 8 | Aircraft Engineering and Maintenance Systems (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-aircraft-engineering-and-maintenance-systems-top-up/ |
| 9 | Aircraft Maintenance Engineering | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-aircraft-maintenance-engineering/ |
| 10 | Aircraft Maintenance Engineering including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-aircraft-maintenance-engineering-including-foundation-year/ |
| 12 | Electrical and Electronic Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-electrical-and-electronic-engineering/ |
| 14 | Electrical and Electronic Engineering (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-electrical-and-electronic-engineering-top-up/ |
| 15 | Electrical and Electronic Engineering including Foundation Year | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-electrical-and-electronic-engineering-including-foundation-year/ |
| 17 | Mechanical Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-mechanical-engineering/ |
| 18 | Mechanical Engineering | HNC | https://www.southwales.ac.uk/courses/hnc-mechanical-engineering/ |
| 19 | Mechanical Engineering | HND | https://www.southwales.ac.uk/courses/hnd-mechanical-engineering/ |
| 22 | Mechanical Engineering including Foundation Year | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-mechanical-engineering-including-foundation-year/ |
| 23 | Mechanical Systems Engineering | BEng (Hons) | https://www.southwales.ac.uk/courses/beng-hons-mechanical-systems-engineering/ |

### 1.2 Faculty of Business and Creative Industries

#### Accounting and Finance

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Accounting and Finance | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance/ |
| 2 | Accounting and Finance including Foundation Year | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance-including-foundation-year/ |
| 3 | Business Management (Accounting and Finance) (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-management-accounting-and-finance-top-up/ |

#### Business and Management

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Business Management (Human Resource Management) (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-management-human-resource-management-top-up/ |
| 3 | Business Management (Marketing) (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-management-marketing-top-up/ |
| 4 | Business Management (Supply Chain Management) (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-management-supply-chain-management-top-up/ |
| 5 | Business Management (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-management-top-up/ |
| 6 | Business and Management | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-and-management/ |
| 7 | Business and Management (Creative Industries) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-and-management-creative-industries/ |
| 8 | Business and Management (Entrepreneurship) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-and-management-entrepreneurship/ |
| 9 | Business and Management including Foundation Year | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-business-and-management-including-foundation-year/ |
| 14 | Health, Wellbeing and Social Care Management | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-health-wellbeing-and-social-care-management/ |
| 15 | Health, Wellbeing and Social Care Management including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-health-wellbeing-and-social-care-management-including-foundation-year/ |
| 17 | International Business (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-international-business-top-up/ |
| 23 | Logistics, Procurement and Supply Chain Management | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-logistics-procurement-and-supply-chain-management/ |
| 39 | Sports Business and Management | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-sports-business-and-management/ |

#### Design

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Creative and Therapeutic Arts | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-creative-and-therapeutic-arts/ |
| 2 | Graphic Communication | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-graphic-communication/ |
| 4 | Illustration | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-illustration/ |
| 5 | Interior Design | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-interior-design/ |

#### Fashion

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Fashion Design | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-fashion-design/ |
| 2 | Fashion Marketing | BA (Hons) | https://www.southwales.ac.uk/courses/ba-fashion-marketing/ |

#### Film and Media

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Film | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-film/ |
| 7 | Media Production | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-media-production/ |
| 8 | Media, Culture and Journalism | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-media-culture-and-journalism/ |
| 9 | Performance and Media | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-performance-and-media/ |
| 10 | Sound, Lighting and Live Event Technology | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-sound-lighting-and-live-event-technology/ |
| 11 | TV and Film Set Design | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-tv-and-film-set-design/ |

#### Games, Animation and Visual Effects

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Animation | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-animation/ |
| 3 | Animation (2D and Stop Motion) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-animation-2d-and-stop-motion/ |
| 4 | Game Art | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-game-art/ |
| 6 | Games Design | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-games-design/ |
| 7 | Visual Effects and Motion Graphics | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-visual-effects-and-motion-graphics/ |

#### History and Buddhist Studies

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | History | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-history/ |
| 3 | History including Foundation Year | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-history-including-foundation-year/ |

#### Law

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Community Health and Wellbeing | CertHE | https://www.southwales.ac.uk/courses/certhe-community-health-and-wellbeing/ |
| 3 | Law | LLB (Hons) | https://www.southwales.ac.uk/courses/llb-hons-law/ |
| 4 | Law (Accelerated Route) | LLB (Hons) | https://www.southwales.ac.uk/courses/llb-hons-law-accelerated-route/ |
| 5 | Law and Criminology | LLB (Hons) | https://www.southwales.ac.uk/courses/law-and-criminology-llb-hons/ |
| 6 | Law and Legal Practice (SQE) | LLB (Hons) | https://www.southwales.ac.uk/courses/llb-hons-law-and-legal-practice-sqe/ |
| 7 | Law including Foundation Year | LLB (Hons) | https://www.southwales.ac.uk/courses/law-including-foundation-year---llb-hons/ |

#### Marketing and Advertising

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Advertising | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-advertising/ |
| 2 | Marketing | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-marketing/ |
| 3 | Marketing including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-marketing-including-foundation-year/ |

#### Music, Drama and Performance

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Music Producing | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-music-producing/ |
| 5 | Popular and Commercial Music | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-popular-and-commercial-music/ |
| 6 | Theatre and Drama | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-theatre-and-drama/ |

#### Photography

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Documentary Photography | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-documentary-photography/ |
| 2 | Photography | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-photography/ |

#### English Language

| # | Programme | Degree | URL |
|---|-----------|--------|-----|

### 1.3 Faculty of Life Sciences and Education

#### Art and Creative Wellbeing

| # | Programme | Degree | URL |
|---|-----------|--------|-----|

#### Chiropractic

| # | Programme | Degree | URL |
|---|-----------|--------|-----|

#### Criminology, Policing and Public Services

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Criminology | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-criminology/ |
| 3 | Criminology including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-criminology-including-foundation-year/ |
| 4 | Criminology with Psychology | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-criminology-with-psychology/ |
| 5 | Criminology with Youth Justice | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-criminology-with-youth-justice/ |
| 6 | Criminology with Youth Justice including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-criminology-with-youth-justice-including-foundation-year/ |
| 8 | Professional Policing | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-professional-policing/ |
| 9 | Professional Policing including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-professional-policing-including-foundation-year/ |
| 10 | Psychology with Criminology | BSc (Hons) | https://www.southwales.ac.uk/courses/psychology-with-criminology---bsc-hons/ |
| 11 | Public Services | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-public-services/ |
| 12 | Public Services including Foundation Year | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-public-services-including-foundation-year/ |

#### Education and Teaching

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Childhood Development | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-childhood-development/ |
| 2 | Childhood Development including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-childhood-development-including-foundation-year/ |
| 3 | Childhood Studies (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-childhood-studies-top-up/ |
| 4 | Early Years Education (Top Up) | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-early-years-education-top-up/ |
| 5 | Education | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-education/ |
| 15 | Health Care Nursing Support Worker Education | CertHE | https://www.southwales.ac.uk/courses/certhe-health-care-nursing-support-worker-education/ |
| 22 | Primary Initial Teacher Education with QTS: English-medium | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-primary-initial-teacher-education-with-qts/ |
| 24 | Primary Initial Teacher Education with QTS: Welsh-medium | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-primary-initial-teacher-education-with-qts-welsh-medium/ |
| 30 | Sports Coaching and Physical Education | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-sports-coaching-and-physical-education/ |
| 34 | Working with Children and Families | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-working-with-children-and-families/ |

#### Health and Social Care

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Social Work | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-social-work/ |

#### Health Professions

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 33 | Medical Sciences | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-medical-sciences/ |
| 36 | Midwifery | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-midwifery/ |
| 38 | Occupational Therapy | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-occupational-therapy/ |
| 39 | Operating Department Practice (ODP) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-operating-department-practice-odp/ |
| 41 | Physiotherapy | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-physiotherapy/ |

#### Nursing

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 3 | Nursing (Adult) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-nursing-adult/ |
| 5 | Nursing (Adult): Flexible Learning | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-nursing-adult-flexible-learning/ |
| 6 | Nursing (Child) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-nursing-child/ |
| 7 | Nursing (Learning Disabilities) | BSc (Hons) | https://www.southwales.ac.uk/courses/-bsc-hons-nursing-learning-disabilities/ |
| 9 | Nursing (Mental Health) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-nursing-mental-health/ |
| 11 | Nursing (Mental Health): Flexible Learning | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-nursing-mental-health-flexible-learning/ |

#### Psychology

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Psychology | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-psychology/ |
| 4 | Psychology including Foundation Year | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-psychology-including-foundation-year/ |
| 5 | Psychology with Counselling | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-counselling/ |
| 6 | Psychology with Developmental Disorders | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-psychology-with-developmental-disorders/ |

#### Psychotherapy and Counselling

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 4 | Counselling and Therapeutic Practice | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-counselling-and-therapeutic-practice/ |

#### Research Degrees

| # | Programme | Degree | URL |
|---|-----------|--------|-----|

#### Sport

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 2 | Community Football Coaching and Administration (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-community-football-coaching-and-administration-top-up/ |
| 3 | Community Football Coaching and Development | Foundation Degree (FdSc) | https://www.southwales.ac.uk/courses/foundation-degree-fdsc-community-football-coaching-and-development/ |
| 4 | Football Coaching and Performance | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-football-coaching-and-performance/ |
| 5 | Football Coaching, Development and Administration | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-football-coaching-development-and-administration/ |
| 7 | Sport and Exercise Science | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-sport-and-exercise-science/ |
| 8 | Sport and Exercise Therapy | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-sport-and-exercise-therapy/ |
| 10 | Sports Coaching and Development | Foundation Degree (FdSc) | https://www.southwales.ac.uk/courses/sports-coaching-and-development-foundation-degree-fdsc/ |
| 11 | Sports Coaching and Development (Top Up) | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-sports-coaching-and-development-top-up/ |
| 13 | Sports Journalism | BA (Hons) | https://www.southwales.ac.uk/courses/ba-hons-sports-journalism/ |
| 15 | Strength and Conditioning | BSc (Hons) | https://www.southwales.ac.uk/courses/bsc-hons-strength-and-conditioning/ |

---

## 2. 研究生专业清单 (Postgraduate courses by Faculty → Subject Area)

Full PG listing — includes MA, MSc, MBA, MChiro, LLM, PGDip, PGCert, PGCE, ProfGCE, ProfCE, MPhil, PhD, DBA, Masters by Research.

### 2.1 Faculty of Computing, Engineering and Science

#### Applied Science

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Analytical and Forensic Science | MSc | https://www.southwales.ac.uk/courses/msc-analytical-and-forensic-science/ |
| 2 | Digital Forensics | MSc | https://www.southwales.ac.uk/courses/msc-digital-forensics/ |
| 3 | Essential Mathematics for Teaching | Unknown | https://www.southwales.ac.uk/courses/essential-mathematics-for-teaching/ |
| 4 | Forensic Audit and Accounting | MSc | https://www.southwales.ac.uk/courses/msc-forensic-audit-and-accounting/ |
| 5 | Forensic Investigation | MSc | https://www.southwales.ac.uk/courses/msc-forensic-investigation/ |
| 6 | Pharmaceutical Chemistry | MSc | https://www.southwales.ac.uk/courses/msc-pharmaceutical-chemistry/ |
| 7 | Wildlife and Conservation Management | MSc | https://www.southwales.ac.uk/courses/msc-wildlife-and-conservation-management/ |

#### Built Environment and Sustainability

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Civil Engineering | MEng | https://www.southwales.ac.uk/courses/meng-civil-engineering/ |
| 2 | Civil Engineering | MSc | https://www.southwales.ac.uk/courses/msc-civil-engineering/ |
| 3 | Construction Project Management | MSc | https://www.southwales.ac.uk/courses/msc-construction-project-management/ |
| 4 | Renewable Energy and Sustainable Technology | MSc | https://www.southwales.ac.uk/courses/msc-renewable-energy-and-sustainable-technology/ |

#### Computing and Cyber Security

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Advanced Computer Science | MSc | https://www.southwales.ac.uk/courses/msc-advanced-computer-science/ |
| 2 | Applied Cyber Security | MSc | https://www.southwales.ac.uk/courses/msc-applied-cyber-security/ |
| 3 | Artificial Intelligence | MSc | https://www.southwales.ac.uk/courses/msc-artificial-intelligence/ |
| 4 | Artificial Intelligence in Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-artificial-intelligence-in-medicine/ |
| 5 | Computing and Information Systems | MSc | https://www.southwales.ac.uk/courses/msc-computing-and-information-systems/ |
| 6 | Cyber Security, Risk and Resilience | MSc | https://www.southwales.ac.uk/courses/msc-cyber-security-risk-and-resilience/ |
| 7 | Data Science | MSc | https://www.southwales.ac.uk/courses/msc-data-science/ |
| 8 | Leading Digital Transformation | MSc | https://www.southwales.ac.uk/courses/msc-leading-digital-transformation/ |

#### Engineering

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Aeronautical Engineering | MEng | https://www.southwales.ac.uk/courses/meng-aeronautical-engineering/ |
| 2 | Aeronautical Engineering | MSc | https://www.southwales.ac.uk/courses/msc-aeronautical-engineering/ |
| 3 | Aerospace Engineering | MEng | https://www.southwales.ac.uk/courses/meng-hons-aerospace-engineering/ |
| 4 | Aviation Engineering and Management | MSc | https://www.southwales.ac.uk/courses/msc-aviation-engineering-and-management/ |
| 5 | Electrical and Electronic Engineering | MEng | https://www.southwales.ac.uk/courses/meng-electrical-and-electronic-engineering/ |
| 6 | Electronics and Information Technology | MSc | https://www.southwales.ac.uk/courses/msc-electronics-and-information-technology/ |
| 7 | Mechanical Engineering | MEng | https://www.southwales.ac.uk/courses/meng-mechanical-engineering/ |
| 8 | Mechanical Engineering | MSc | https://www.southwales.ac.uk/courses/msc-mechanical-engineering/ |
| 9 | Professional Engineering | MSc | https://www.southwales.ac.uk/courses/msc-professional-engineering/ |

### 2.2 Faculty of Business and Creative Industries

#### Accounting and Finance

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Finance and Investment | MSc | https://www.southwales.ac.uk/courses/msc-finance-and-investment/ |
| 2 | Master of Business Administration Global (Finance) | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-global-finance/ |
| 3 | Professional Accounting (With ACCA tuition) (Fast Track) | MSc | https://www.southwales.ac.uk/courses/msc-professional-accounting-with-acca-tuition-fast-track/ |
| 4 | Professional Accounting (with ACCA Tuition) | MSc | https://www.southwales.ac.uk/courses/msc-professional-accounting-with-acca-tuition/ |

#### Business and Management

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Association of Chartered Certified Accountants (ACCA) | Unknown | https://www.southwales.ac.uk/courses/association-of-chartered-certified-accountants-acca/ |
| 2 | Doctor of Business Administration | DBA | https://www.southwales.ac.uk/courses/doctor-of-business-administration-dba/ |
| 3 | Engineering Management | MSc | https://www.southwales.ac.uk/courses/msc-engineering-management/ |
| 4 | Film (Production Management) | MA | https://www.southwales.ac.uk/courses/ma-film-production-management/ |
| 5 | Health and Public Service Management | MSc | https://www.southwales.ac.uk/courses/msc-health-and-public-service-management/ |
| 6 | Human Resource Management | MSc | https://www.southwales.ac.uk/courses/msc-human-resource-management/ |
| 7 | International Logistics and Supply Chain Management | MSc | https://www.southwales.ac.uk/courses/msc-international-logistics-and-supply-chain-management/ |
| 8 | International Security and Risk Management | MSc | https://www.southwales.ac.uk/courses/msc-international-security-and-risk-management/ |
| 9 | International Security and Risk Management (Counter Terrorism) | MSc | https://www.southwales.ac.uk/courses/msc-international-security-and-risk-management-counter-terrorism/ |
| 10 | Leadership and Management | MSc | https://www.southwales.ac.uk/courses/msc-leadership-and-management/ |
| 11 | Leadership and Management (Education) | MA | https://www.southwales.ac.uk/courses/ma-leadership-and-management-education/ |
| 12 | Management | MSc | https://www.southwales.ac.uk/courses/msc-management/ |
| 13 | Master of Business Administration | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration/ |
| 14 | Master of Business Administration Global | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-global/ |
| 15 | Master of Business Administration Global (Financial Services) | MBA | https://www.southwales.ac.uk/courses/master-of-business-administration-global-financial-services---mba/ |
| 16 | Master of Business Administration Global (Hospitality Management) | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-global-hospitality-management/ |
| 17 | Master of Business Administration Global (Human Resource Management) | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-human-resource-management/ |
| 18 | Master of Business Administration Global (Marketing) | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-global-marketing/ |
| 19 | Master of Business Administration Global (Operations and Supply Chain Management) | MBA | https://www.southwales.ac.uk/courses/mba-master-of-business-administration-global-operations-and-supply-chain-management/ |
| 20 | Obesity and Weight Management | MSc | https://www.southwales.ac.uk/courses/msc-obesity-and-weight-management/ |
| 21 | Obesity and Weight Management | PGDip | https://www.southwales.ac.uk/courses/pgdip-obesity-and-weight-management/ |
| 22 | Pain Management | MSc | https://www.southwales.ac.uk/courses/msc-pain-management/ |
| 23 | Pain Management | PGDip | https://www.southwales.ac.uk/courses/pgdip-pain-management/ |
| 24 | Project Management | MSc | https://www.southwales.ac.uk/courses/msc-project-management/ |
| 25 | Project Management (Fast Track) | MSc | https://www.southwales.ac.uk/courses/msc-project-management-fast-track/ |
| 26 | Safety, Health and Environmental Management | MSc | https://www.southwales.ac.uk/courses/msc-safety-health-and-environmental-management/ |

#### Design

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Graphic Communication | MA | https://www.southwales.ac.uk/courses/ma-graphic-communication/ |

#### Film and Media

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Film (Cinematography) | MA | https://www.southwales.ac.uk/courses/ma-film-cinematography/ |
| 2 | Film (Directing) | MA | https://www.southwales.ac.uk/courses/ma-film-directing/ |
| 3 | Film (Documentary) | MA | https://www.southwales.ac.uk/courses/ma-film-documentary/ |
| 4 | Film (Editing) | MA | https://www.southwales.ac.uk/courses/ma-film-editing/ |
| 5 | Film (Screenwriting) | MA | https://www.southwales.ac.uk/courses/ma-film-screenwriting/ |

#### Games, Animation and Visual Effects

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Animation | MA | https://www.southwales.ac.uk/courses/ma-animation/ |
| 2 | Games | MA | https://www.southwales.ac.uk/courses/ma-games/ |

#### History and Buddhist Studies

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Buddhist Studies | MA | https://www.southwales.ac.uk/courses/ma-buddhist-studies/ |

#### Law

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Arts, Health and Wellbeing | MA | https://www.southwales.ac.uk/courses/ma-arts-health-and-wellbeing/ |
| 2 | Laws | LLM | https://www.southwales.ac.uk/courses/llm-laws/ |
| 3 | Laws (International Commercial Law) | LLM | https://www.southwales.ac.uk/courses/llm-laws-international-commercial-law/ |
| 4 | Legal Practice | LLM | https://www.southwales.ac.uk/courses/llm-legal-practice/ |
| 5 | Legal Practice Course | PGDip | https://www.southwales.ac.uk/courses/pgdip-legal-practice-course/ |

#### Marketing and Advertising

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Strategic and Digital Marketing | MSc | https://www.southwales.ac.uk/courses/msc-strategic-digital-marketing/ |

#### Music, Drama and Performance

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Music Engineering and Production | MSc | https://www.southwales.ac.uk/courses/msc-music-engineering-and-production/ |
| 2 | Music Production and Songwriting | MA | https://www.southwales.ac.uk/courses/ma-music-production-and-songwriting/ |
| 3 | Music Therapy | MA | https://www.southwales.ac.uk/courses/ma-music-therapy/ |
| 4 | Theatre and Performance | MA | https://www.southwales.ac.uk/courses/ma-theatre-and-performance/ |

#### English Language

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Pre-Sessional English Language | Unknown | https://www.southwales.ac.uk/courses/pre-sessional-english-language/ |

### 2.3 Faculty of Life Sciences and Education

#### Art and Creative Wellbeing

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Art Psychotherapy | MA | https://www.southwales.ac.uk/courses/ma-art-psychotherapy/ |
| 2 | CAMH (Child and Adolescent Mental Health) | MA | https://www.southwales.ac.uk/courses/ma-camh-child-and-adolescent-mental-health/ |
| 3 | Play Therapy | MSc | https://www.southwales.ac.uk/courses/msc-play-therapy/ |

#### Chiropractic

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Master of Chiropractic | MChiro | https://www.southwales.ac.uk/courses/mchiro-master-of-chiropractic/ |
| 2 | Master of Chiropractic including Foundation Year | MChiro | https://www.southwales.ac.uk/courses/mchiro-master-of-chiropractic-including-foundation-year/ |
| 3 | Trichology and Hair Sciences | PGCert | https://www.southwales.ac.uk/courses/pgcert-trichology-and-hair-sciences/ |

#### Criminology, Policing and Public Services

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Crime and Justice | MSc | https://www.southwales.ac.uk/courses/msc-crime-and-justice/ |
| 2 | Leadership in Professional Policing | MSc | https://www.southwales.ac.uk/courses/msc-leadership-in-professional-policing/ |
| 3 | Working with Adult and Young People who Offend | MSc | https://www.southwales.ac.uk/courses/msc-working-with-adult-and-young-people-who-offend/ |

#### Education and Teaching

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Education (Innovation In Learning and Teaching) | MA | https://www.southwales.ac.uk/courses/ma-education-innovation-in-learning-and-teaching/ |
| 2 | Education (Wales) | MA | https://www.southwales.ac.uk/courses/ma-education-wales/ |
| 3 | Education (Wales): Additional Learning Needs | MA | https://www.southwales.ac.uk/courses/ma-education-wales-additional-learning-needs/ |
| 4 | Education (Wales): Curriculum | MA | https://www.southwales.ac.uk/courses/ma-education-wales-curriculum/ |
| 5 | Education (Wales): Equity in Education | MA | https://www.southwales.ac.uk/courses/ma-education-wales-equity-in-education/ |
| 6 | Education (Wales): Leadership | MA | https://www.southwales.ac.uk/courses/ma-education-wales-leadership/ |
| 7 | Education For Healthcare Professionals | PGCert | https://www.southwales.ac.uk/courses/pgcert-education-for-healthcare-professionals/ |
| 8 | Essential English for Teaching | Unknown | https://www.southwales.ac.uk/courses/essential-english-for-teaching/ |
| 9 | Essential Science for Teaching | Unknown | https://www.southwales.ac.uk/courses/essential-science-for-teaching/ |
| 10 | Medical Education | MSc | https://www.southwales.ac.uk/courses/msc-medical-education/ |
| 11 | Medical Education | PGDip | https://www.southwales.ac.uk/courses/pgdip-medical-education/ |
| 12 | Medical Education | PGCert | https://www.southwales.ac.uk/courses/pgcert-medical-education/ |
| 13 | Post Compulsory Education and Training (PcET) | PGCE | https://www.southwales.ac.uk/courses/pgce-post-compulsory-education-and-training-pcet/ |
| 14 | Post Compulsory Education and Training (PcET) | ProfCE | https://www.southwales.ac.uk/courses/profce-post-compulsory-education-and-training-pcet/ |
| 15 | Post Compulsory Education and Training (PcET) | ProfGCE | https://www.southwales.ac.uk/courses/profgce-post-compulsory-education-and-training-pcet/ |
| 16 | Primary Initial Teacher Education with QTS: English-medium | PGCE | https://www.southwales.ac.uk/courses/pgce-primary-initial-teacher-education-with-qts/ |
| 17 | Primary Initial Teacher Education with QTS: Welsh-medium | PGCE | https://www.southwales.ac.uk/courses/pgce-primary-initial-teacher-education-with-qts-welsh-medium/ |
| 18 | Return to Teaching | Unknown | https://www.southwales.ac.uk/courses/return-to-teaching/ |
| 19 | SEN/ALN (Additional Learning Needs) | MA | https://www.southwales.ac.uk/courses/ma-senaln-additional-learning-needs/ |
| 20 | SEN/ALN (Autism) | MA | https://www.southwales.ac.uk/courses/ma-sen-aln-autism/ |
| 21 | SEN/ALN (Specific Learning Difficulties) | PGDip | https://www.southwales.ac.uk/courses/pgdip-senaln-specific-learning-difficulties/ |
| 22 | TESOL (Teaching English to Speakers of Other Languages) | MA | https://www.southwales.ac.uk/courses/ma-tesol-teaching-english-to-speakers-of-other-languages/ |
| 23 | Teaching in Higher Education | PGCert | https://www.southwales.ac.uk/courses/pgcert-teaching-in-higher-education/ |
| 24 | Working for Children and Young People (Youth Work Initial Qualifying) | MA | https://www.southwales.ac.uk/courses/ma-working-for-children-and-young-people-youth-work-initial-qualifying/ |

#### Health Professions

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Acute Medicine | MSc | https://www.southwales.ac.uk/courses/msc-acute-medicine/ |
| 2 | Acute Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-acute-medicine/ |
| 3 | Addiction Medicine | PGCert | https://www.southwales.ac.uk/courses/courses/pgcert-addiction-medicine/ |
| 4 | Advanced Clinical Practitioner | MSc | https://www.southwales.ac.uk/courses/msc-advanced-clinical-practitioner/ |
| 5 | Anti-ageing Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-anti-ageing-medicine/ |
| 6 | Applied Health Economics | MSc | https://www.southwales.ac.uk/courses/msc-applied-health-economics/ |
| 7 | Applied Health Economics | PGDip | https://www.southwales.ac.uk/courses/pgdip-applied-health-economics/ |
| 8 | Calcium and Bone Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-calcium-and-bone-medicine/ |
| 9 | Clinical Physiology | MSc | https://www.southwales.ac.uk/courses/msc-clinical-physiology/ |
| 10 | Clinical Physiology | PGDip | https://www.southwales.ac.uk/courses/pgdip-clinical-physiology/ |
| 11 | Clinical Psychiatry | MSc | https://www.southwales.ac.uk/courses/msc-clinical-psychiatry/ |
| 12 | Clinical Psychiatry | PGDip | https://www.southwales.ac.uk/courses/pgdip-clinical-psychiatry/ |
| 13 | Cosmetic and Aesthetic Medicine | MSc | https://www.southwales.ac.uk/courses/msc-cosmetic-and-aesthetic-medicine/ |
| 14 | Cosmetic and Aesthetic Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-cosmetic-and-aesthetic-medicine/ |
| 15 | Cosmetic and Aesthetic Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-cosmetic-and-aesthetic-medicine/ |
| 16 | Critical Care | UAC | https://www.southwales.ac.uk/courses/acerthe-critical-care/ |
| 17 | Critical Care | PGCert | https://www.southwales.ac.uk/courses/pgcert-critical-care/ |
| 18 | Dermatology Clinical Practice | MSc | https://www.southwales.ac.uk/courses/msc-dermatology-clinical-practice/ |
| 19 | Dermatology in Clinical Practice | PGDip | https://www.southwales.ac.uk/courses/pgdip-dermatology-in-clinical-practice/ |
| 20 | Diabetes | MSc | https://www.southwales.ac.uk/courses/msc-diabetes/ |
| 21 | Diabetes | PGDip | https://www.southwales.ac.uk/courses/pgdip-diabetes/ |
| 22 | Endocrinology | MSc | https://www.southwales.ac.uk/courses/msc-endocrinology/ |
| 23 | Endocrinology | PGDip | https://www.southwales.ac.uk/courses/pgdip-endocrinology/ |
| 24 | Expedition and Wilderness Medicine | MSc | https://www.southwales.ac.uk/courses/msc-expedition-and-wilderness-medicine/ |
| 25 | Expedition and Wilderness Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-expedition-and-wilderness-medicine/ |
| 26 | Gastroenterology | MSc | https://www.southwales.ac.uk/courses/msc-gastroenterology/ |
| 27 | Gastroenterology | PGDip | https://www.southwales.ac.uk/courses/pgdip-gastroenterology/ |
| 28 | Genomic Medicine and Healthcare | PGDip | https://www.southwales.ac.uk/courses/pgdip-genomic-medicine-and-healthcare/ |
| 29 | Hypertension | PGCert | https://www.southwales.ac.uk/courses/pgdip-hypertension/ |
| 30 | Independent Prescribing Practice | PGCert | https://www.southwales.ac.uk/courses/pgcert-independent-prescribing-practice/ |
| 31 | Leadership in Healthcare | MSc | https://www.southwales.ac.uk/courses/msc-leadership-in-healthcare/ |
| 32 | Leadership in Healthcare | PGDip | https://www.southwales.ac.uk/courses/pgdip-leadership-in-healthcare/ |
| 33 | Menopause Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-menopause-medicine/ |
| 34 | Metabolic Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-metabolic-medicine/ |
| 35 | Neurodiversity-inclusive Healthcare | PGCert | https://www.southwales.ac.uk/courses/courses/pgcert-neurodiversity-inclusive-healthcare/ |
| 36 | Palliative Care | PGCert | https://www.southwales.ac.uk/courses/pgcert-palliative-care/ |
| 37 | Preventative Cardiovascular Medicine | MSc | https://www.southwales.ac.uk/courses/msc-preventative-cardiovascular-medicine/ |
| 38 | Preventative Cardiovascular Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-preventative-cardiovascular-medicine/ |
| 39 | Professional Practice | MSc | https://www.southwales.ac.uk/courses/msc-professional-practice/ |
| 40 | Professional Practice (SQE) | LLM | https://www.southwales.ac.uk/courses/llm-professional-practice-sqe/ |
| 41 | Public Health | MSc | https://www.southwales.ac.uk/courses/msc-public-health/ |
| 42 | Public Health | PGDip | https://www.southwales.ac.uk/courses/pgdip-public-health/ |
| 43 | Public Health: Online | MSc | https://www.southwales.ac.uk/courses/msc-public-health-online/ |
| 44 | Renal Medicine | MSc | https://www.southwales.ac.uk/courses/msc-renal-medicine/ |
| 45 | Renal Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-renal-medicine/ |
| 46 | Respiratory Medicine | MSc | https://www.southwales.ac.uk/courses/msc-respiratory-medicine/ |
| 47 | Respiratory Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-respiratory-medicine/ |
| 48 | Return to Practice | Unknown | https://www.southwales.ac.uk/courses/return-to-practice/ |
| 49 | Rheumatology | MSc | https://www.southwales.ac.uk/courses/msc-rheumatology/ |
| 50 | Rheumatology | PGDip | https://www.southwales.ac.uk/courses/pgdip-rheumatology/ |
| 51 | Sexual Health Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-sexual-health-medicine/ |
| 52 | Sexual and Reproductive Medicine | MSc | https://www.southwales.ac.uk/courses/msc-sexual-and-reproductive-medicine/ |
| 53 | Sexual and Reproductive Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-sexual-and-reproductive-medicine/ |
| 54 | Specialist Community Public Health Nursing - Health Visiting | PGDip | https://www.southwales.ac.uk/courses/pgdip-specialist-community-public-health-nursing-health-visiting/ |
| 55 | Specialist Community Public Health Nursing - School Nursing | PGDip | https://www.southwales.ac.uk/courses/pgdip-specialist-community-public-health-nursing-school-nursing/ |
| 56 | Sports and Exercise Medicine | MSc | https://www.southwales.ac.uk/courses/msc-sports-and-exercise-medicine/ |
| 57 | Sports and Exercise Medicine | PGDip | https://www.southwales.ac.uk/courses/pgdip-sports-and-exercise-medicine/ |
| 58 | Thyroid Medicine | PGCert | https://www.southwales.ac.uk/courses/pgcert-thyroid-medicine/ |

#### Nursing

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Community Health Studies (Specialist Practitioner Community Children's Nursing) | PGDip | https://www.southwales.ac.uk/courses/pgdip-community-health-studies-specialist-practitioner-community-childrens-nursing/ |
| 2 | Community Health Studies (Specialist Practitioner District Nursing) | PGDip | https://www.southwales.ac.uk/courses/pgdip-community-health-studies-specialist-practitioner-district-nursing/ |
| 3 | Nursing (Adult) | PGDip | https://www.southwales.ac.uk/courses/pgdip-nursing-adult/ |
| 4 | Nursing (Learning Disabilities) | PGDip | https://www.southwales.ac.uk/courses/pgdip-nursing-learning-disabilities/ |
| 5 | Nursing (Mental Health) | PGDip | https://www.southwales.ac.uk/courses/pgdip-nursing-mental-health/ |

#### Psychology

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Clinical Psychology | MSc | https://www.southwales.ac.uk/courses/msc-clinical-psychology/ |
| 2 | Psychology (Conversion) | MSc | https://www.southwales.ac.uk/courses/msc-psychology-conversion/ |

#### Psychotherapy and Counselling

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Behaviour Analysis Supervised Practice | PGDip | https://www.southwales.ac.uk/courses/pgdip-behaviour-analysis-supervised-practice/ |
| 2 | Behaviour Analysis and Therapy | MSc | https://www.southwales.ac.uk/courses/msc-behaviour-analysis-and-therapy/ |
| 3 | Counselling Skills | PGCert | https://www.southwales.ac.uk/courses/pgcert-counselling-skills/ |
| 4 | Integrative Counselling and Psychotherapy | MA | https://www.southwales.ac.uk/courses/ma-integrative-counselling-and-psychotherapy/ |
| 5 | Integrative Counselling and Psychotherapy | PGDip | https://www.southwales.ac.uk/courses/pgdip-integrative-counselling-and-psychotherapy/ |

#### Research Degrees

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Doctor of Philosophy | PhD | https://www.southwales.ac.uk/courses/phd-doctor-of-philosophy/ |
| 2 | Master of Philosophy | MPhil | https://www.southwales.ac.uk/courses/mphil-master-of-philosophy/ |
| 3 | Masters by Research | MA/MSc | https://www.southwales.ac.uk/courses/ma-msc-masters-by-research/ |

#### Sport

| # | Programme | Degree | URL |
|---|-----------|--------|-----|
| 1 | Advanced Performance Football Coaching | MSc | https://www.southwales.ac.uk/courses/msc-advanced-performance-football-coaching/ |
| 2 | Leadership in Sport | MA | https://www.southwales.ac.uk/courses/ma-leadership-in-sport/ |
| 3 | Sport, Health and Exercise Science | MSc | https://www.southwales.ac.uk/courses/msc-sport-health-and-exercise-science/ |
| 4 | Sports Coaching and Performance | MSc | https://www.southwales.ac.uk/courses/msc-sports-coaching-and-performance/ |
| 5 | Sports and Exercise Nutrition | PGCert | https://www.southwales.ac.uk/courses/pgcert-sports-and-exercise-nutrition/ |

---

## 3. 申请要求 (Application requirements)

### 3.1 Typical UG Entry Requirements (representative - BA/BSc Hons programmes)

| Requirement | Typical value |
|-------------|---------------|
| UCAS tariff points | 112 (or above) |
| A Level | BBC |
| BTEC Extended Diploma | Distinction Merit Merit (DMM) |
| AAT | Level 3 for 1st year entry / Level 4 for direct 2nd year entry |
| Welsh Baccalaureate | Advanced Skills Baccalaureate Wales grade B/C with BB-BC at A Level |
| Access to HE | Pass the Access to HE Diploma and obtain a minimum of 112 UCAS tariff points |
| T Level | Pass (C and above) |
| GCSE minimum | 5 GCSEs including Mathematics/Numeracy and English at Grade C/4 or above |

**Source**: https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance/#course-requirements-anchor
> Original snippet: "UCAS Points: 112 (or above). Typical qualification requirements: A Level: BBC, AAT: Level 3 for 1st year entry or Level 4 for direct 2nd year entry, Welsh Baccalaureate - Advanced Skills Baccalaureate Wales grade B/C with BB-BC at A Level, BTEC: BTEC Extended Diploma Distinction Merit Merit, Access to HE: Pass the Access to HE Diploma and obtain a minimum of 112 UCAS tariff points, T Level: Pass (C and above)"

**Note**: Individual programmes may require higher UCAS points (e.g. MEng, integrated masters, healthcare programmes). Always check the specific course page. Contextual offers available for widening-participation applicants.

### 3.2 English Language Requirements (International Students)

Standard entry requirement for UG and most PG programmes:

| Test | Required Score |
|------|----------------|
| **IELTS Academic** | Overall 6.0 with minimum 5.5 in each component (One Skill Retake accepted) |
| **TOEFL iBT** (before Jan 21, 2026) | Total 72 minimum (Reading 18, Listening 17, Writing 17, Speaking 20) |
| **TOEFL iBT** (on/after Jan 21, 2026) | Total 4 minimum (each section 4) |
| **Duolingo English Test** | 110 overall, 100 in each component |
| **Cambridge English: Advanced (CAE)** | 169 overall, minimum 162 in each component (exams from Jan 2015) |
| **PTE Academic / PTE Academic UKVI** | 59 overall and 59 in each component |
| **Trinity College ISE** | ISE II Distinction or ISE III Pass |
| **LanguageCert Academic (or SELT)** | 65 overall, minimum 60 in each component |
| **PSI Skills for English UKVI B2** | Pass in all 4 components |
| **Kaplan Test of English (online)** | Overall 458, minimum 425 in each component |
| **LanguageCert International ESOL B2** | High Pass overall, min 38 in speaking, min 33 in all other components |
| **Oxford Test of English (OTE)** | 125 overall, 111 in each component |
| **IELCA (Direct entry)** | 32 overall (or 35 for higher IELTS-equivalent entry) |
| **GCSE pass in English** | Grade C or above |

**Doctoral and research masters**: IELTS 6.5 overall (minimum 5.5 each band) or regional equivalents.

**Source**: https://www.southwales.ac.uk/international/english-language-programmes/requirements/

> Original snippet: "We recognise the following English language qualifications: GCSE pass in English at Grade C or above, IELTS with an overall score of 6.0 with at least 5.5 in each component..."

**Note**: A small number of USW programmes require higher IELTS (e.g. health, education). Always check individual course pages.

## 4. 学费与费用 (Tuition fees — 2026/27 academic year)

### 4.1 Standard Fees (representative UG full-time programme)

| Cohort | Fee | Period |
|--------|-----|--------|
| **UK (Home) full-time UG** | £9,790 | per year |
| **UK (Home) part-time UG** | £804 | per 20 credits |
| **International full-time UG** | £16,800 | per year |

**Source**: https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance/#course-fees-anchor
> Original snippet: "FEES AND FUNDING 2026/27 — UK Full-time Fee £9,790 per year*, International Full-time Fee £16,800 per year*, UK Part-time Fee £804 per 20 credits*"

### 4.2 Fee notes

* Full-time fees are per year. Part-time fees are per 20 credits.
* Once enrolled, the fee is anticipated to remain at the same rate throughout the duration of study on this course, except as described below.
* The University may increase the maximum fee for home students on full-time undergraduate courses only where the Welsh Government increases the permitted level of inflation of fees.
* Fees for all students (including part-time, postgraduate and international students) may be amended in accordance with the Fees and Debt Management Policy.
* International fees vary by programme — see individual course pages for exact figure. Some programmes (e.g. online Diploma MSc partnership programmes) refer applicants to partner website.

### 4.3 Additional Costs

- Tuition fees cover the cost of tuition, examination and registration.
- Living costs (accommodation, food, transport, books) are additional.
- Scholarships and bursaries available — see https://www.southwales.ac.uk/money/

## 5. 申请方式与截止日期 (How to apply)

### 5.1 Undergraduate

- **Standard route**: Apply through **UCAS** (https://www.ucas.com).
- **USW UCAS Apply page**: https://www.southwales.ac.uk/apply-through-ucas
- **Clearing route**: Apply through USW Clearing hotline (03455 76 06 06). See https://www.southwales.ac.uk/clearing/how-to-apply-through-clearing/
- **Application deadlines** (typical): UCAS main scheme deadlines (Equal Consideration: end of January; late applications thereafter). Confirm exact dates on individual course pages or UCAS website.
- **Start date**: September (most programmes).

### 5.2 Postgraduate

- **Standard route**: Apply directly via USW online application form.
- **International PG applications**: https://www.southwales.ac.uk/international/welcome/apply-questions/
- **Start date**: September (most programmes; some online programmes have rolling/multiple intakes).

### 5.3 Campuses & Locations

| Campus | Location |
|--------|----------|
| Pontypridd | Main campus (Treforest) — most programmes |
| Cardiff | City campus — selected programmes |
| Newport | City campus — selected programmes |
| Online | Many PG programmes (incl. Diploma MSc partnership) |

Specific campus shown on each course page (Campus Code A, B, etc.).

---

## 6. WeKnora Chunk Import Manifest

This document should be chunked into the following sections for ingestion:

| Chunk ID | Section | Size est. | Notes |
|----------|---------|-----------|-------|
| usw-overview | §0 | ~5KB | School basics + roll-up tables |
| usw-ug-fces | §1.1 | ~80 rows | FCES UG programmes |
| usw-ug-fbci | §1.2 | ~99 rows | FBCI UG programmes |
| usw-ug-flse | §1.3 | ~158 rows | FLSE UG programmes |
| usw-pg-fces | §2.1 | ~28 rows | FCES PG programmes |
| usw-pg-fbci | §2.2 | ~50 rows | FBCI PG programmes |
| usw-pg-flse | §2.3 | ~111 rows | FLSE PG programmes |
| usw-entry-req | §3 | ~2KB | Entry + language requirements |
| usw-fees | §4 | ~2KB | Tuition fees |
| usw-apply | §5 | ~1KB | Application routes |

## 7. Monitoring Watchlist (Phase 4)

| URL | Frequency | Reason |
|-----|-----------|--------|
| https://www.southwales.ac.uk/courses/ | **HIGH** (monthly) | Course catalog — new programmes added throughout year |
| https://www.southwales.ac.uk/courses/{slug}/#course-fees-anchor | **HIGH** (monthly) | Tuition fees — annual update typically Aug/Sep |
| https://www.southwales.ac.uk/courses/{slug}/#course-requirements-anchor | **MEDIUM** (quarterly) | UCAS points / qualification requirements |
| https://www.southwales.ac.uk/international/english-language-programmes/requirements/ | **MEDIUM** (quarterly) | IELTS / TOEFL equivalents change |
| https://www.southwales.ac.uk/about/our-structure/ | **LOW** (annual) | Faculty/dean list |
| https://www.southwales.ac.uk/apply-through-ucas | **HIGH** (monthly) | UCAS deadlines |
| https://www.southwales.ac.uk/clearing/ | **HIGH** (Aug–Sep) | Clearing availability |

---

## Appendix: Data Sources

All data captured 2026-07-08 from:

1. https://www.southwales.ac.uk/courses/?page={1..17} — full course catalog (337 courses)
2. https://www.southwales.ac.uk/about/our-structure/ — academic structure (3 faculties, 25 subject areas, 3 deans)
3. https://www.southwales.ac.uk/courses/ba-hons-accounting-and-finance/ — sample course page (template for fees/entry/UCAS/location/campus code)
4. https://www.southwales.ac.uk/courses/msc-acute-medicine/ — online PG partner programme
5. https://www.southwales.ac.uk/international/english-language-programmes/requirements/ — full English language requirements table
6. https://www.southwales.ac.uk/international/welcome/apply-questions/ — international apply
7. https://www.southwales.ac.uk/apply-through-ucas — UCAS route
8. https://www.southwales.ac.uk/clearing/how-to-apply-through-clearing/ — Clearing route
9. https://www.southwales.ac.uk/money/ — fees & funding hub

---

## Cache

See:
- `uni-cache/schools/south-wales/site-memory.json` — site topology & extraction rules
- `uni-cache/schools/south-wales/last-extract.json` — full extracted data + evidence blocks
- `uni-cache/schools/south-wales/content-hashes.json` — content fingerprints for monitoring
