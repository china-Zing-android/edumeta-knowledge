# Central Michigan University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

Central Michigan University (CMU) is a public R2 Carnegie research university located in Mount Pleasant, Michigan, founded in 1892. The university serves ~14,426 total students across 7 academic colleges with 1,726 international students from 71 countries. CMU offers 306 academic programs spanning undergraduate, graduate, doctorate, and certificate levels, with strong online options through CMU Online.

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSBA) | 159 |
| 本科辅修 (Minor) | (included in 159) |
| 本科证书 (Undergraduate Certificate) | 39 |
| 研究生学位项目 (MA/MS/MBA/MSAT) | 56 |
| 研究生高级证书 (Graduate Certificate) | 24 |
| 专业博士项目 (PhD/EdD/DPT/AuD/DHA) | 15 |
| **学位项目总计 (UG + Grad, all levels)** | **289 (unique by URL+level)** |
| CMU 全部 program-finder 计数 | 306 |
| 学院 / 独立系所总数 | 7 colleges |
| 国际学生数 | 1,726 |
| 校友总数 | 245,000+ |

> **Reconciliation note**: The CMU program-finder returns 306 total entries. We captured 289 unique programs by (URL + level) because 5 programs are cross-listed in 2 colleges each, and a handful appear with the same URL under different levels (e.g., "Biology" appears for both BS Biology and MS Biology). The remaining 12 entries from program-finder are variations (e.g., Athletic Training appears for both UG and Grad) that we represent with multi-level entries.

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy Tree)

Central Michigan University
├── College of Business Administration [学院]
│   ├── Accounting & Finance
│   ├── Economics (Business & Non-Business)
│   ├── Entrepreneurship
│   ├── Management & Business Information Systems
│   ├── Marketing
│   └── Hospitality & Casino Gaming
├── College of Education and Human Services [学院]
│   ├── Counseling & Special Education
│   ├── Educational Leadership
│   ├── Fashion, Interior Design & Merchandising
│   ├── Health & Physical Education (shared with Health Professions)
│   ├── Recreation & Event Management
│   ├── Teacher Education & Professional Development
│   └── Music Education (shared with Arts and Media)
├── The Herbert H. and Grace A. Dow College of Health Professions [学院]
│   ├── Communication Sciences & Disorders
│   ├── Health Administration & Public Health
│   ├── Nursing
│   ├── Physical Therapy
│   ├── Physician Assistant
│   ├── Athletic Training
│   ├── Audiology
│   └── Social Work
├── College of Liberal Arts and Social Sciences [学院]
│   ├── English Language and Literature
│   ├── History, World Languages, and Cultures
│   ├── Military Science and Leadership
│   ├── Museum Studies
│   ├── Philosophy, Anthropology and Religion
│   ├── Politics, Society, Justice and Public Service
│   ├── Psychology
│   └── Women and Gender Studies
├── Covenant HealthCare College of Medicine at Central Michigan University [学院]
│   └── Medicine (MD)
├── College of Science and Engineering [学院]
│   ├── Biology & Biomedical Sciences
│   ├── Chemistry & Biochemistry
│   ├── Computer Science & Cybersecurity
│   ├── Engineering (Computer, Electrical, Environmental, Mechanical)
│   ├── Engineering Technology (Industrial, Mechanical, Product Design)
│   ├── Geography, Geology & Environmental Studies
│   ├── Mathematics & Statistics
│   └── Physics & Astronomy
└── College of the Arts and Media [学院]
    ├── Art & Design (Animation, Graphic Design, Studio Art)
    ├── Communication
    ├── Journalism & Photojournalism
    ├── Music (Commercial, Music Education, Performance)
    └── Theatre & Dance

> ⚠ Cross-listed programs: Music Education (Education + Arts), Health & Physical Education (Education + Health), Teaching English Learners (Education + Liberal Arts), Environmental Health & Safety (Science + Health), Marketing Environmental Sustainability (Business + Science).

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|-----------------|------|------|-----------|
| BA | B.A. / BSBA / B.S. | Bachelor of Arts / Science | 本科 | 159 |
| UG Cert | Undergraduate Certificate | Undergraduate Certificate | 本科 | 39 |
| MA | M.A. | Master of Arts | 研究生 | ~25 |
| MS | M.S. | Master of Science | 研究生 | ~35 |
| MBA | M.B.A. | Master of Business Administration | 研究生 | 1 |
| MSAT | M.S.A.T. | Master of Science in Athletic Training | 研究生 | 1 |
| EdS | Ed.S. | Educational Specialist | 研究生 | 1 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 11 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 2 |
| DPT | D.P.T. | Doctor of Physical Therapy | 专业博士 | 1 |
| AuD | Au.D. | Doctor of Audiology | 专业博士 | 1 |
| DHA | D.H.A. | Doctor of Health Administration | 专业博士 | 1 |
| Grad Cert | Graduate Certificate | Graduate Certificate | 研究生 | 24 |

> **Note**: CMU commonly awards BS (Bachelor of Science), with the College of Business awarding BSBA (Bachelor of Science in Business Administration). The College of Medicine confers the MD (Doctor of Medicine) for its medical degree.

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix)

| 学院 \ canonical 学位 | BS | BA | MS | MA | MBA | MSAT | EdS | PhD | EdD | DPT | AuD | DHA | UG Cert | Grad Cert | 合计 |
|----------------------|----|----|----|----|-----|------|-----|-----|-----|-----|-----|-----|---------|-----------|------|
| College of Business Administration | 19 | 0 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 3 | 33 |
| College of Education and Human Services | 25 | 1 | 6 | 9 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 15 | 60 |
| College of Liberal Arts and Social Sciences | 32 | 4 | 4 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 16 | 1 | 59 |
| Covenant HealthCare College of Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| College of Science and Engineering | 35 | 0 | 8 | 6 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 8 | 1 | 65 |
| College of the Arts and Media | 22 | 1 | 5 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 36 |
| The Herbert H. and Grace A. Dow College of Health Professions | 17 | 0 | 6 | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 4 | 34 |
| **合计** | **150** | **6** | **31** | **26** | **0** | **1** | **0** | **10** | **2** | **1** | **1** | **1** | **37** | **24** | **288** |

> MBA count includes only non-cross-listed entries; CMU awards the MBA through the College of Business Administration. The EdS (Educational Specialist) appears under Education and Human Services.

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/school architecture

CMU's 7 colleges each house multiple academic departments. The "Bachelor of Science" (BS) is the dominant undergraduate credential, with "Bachelor of Science in Business Administration" (BSBA) awarded in the College of Business Administration. The College of Liberal Arts and Social Sciences awards the majority of BA degrees. See Section 0.2 for the full hierarchy tree.

Undergraduate program counts per college:
- College of Business Administration: 19 majors + 4 certificates = 23
- College of Education and Human Services: 26 majors + 2 certificates = 28
- College of Liberal Arts and Social Sciences: 36 majors + 16 certificates = 52
- College of Science and Engineering: 35 majors + 8 certificates = 43
- College of the Arts and Media: 23 majors + 6 certificates = 29
- The Herbert H. and Grace A. Dow College of Health Professions: 17 majors + 1 certificate = 18

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Business Administration

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | <https://www.cmich.edu/program/accounting> |
| 2 | Applied Business Communication minor | <https://www.cmich.edu/program/applied-business-communication> |
| 3 | Business Administration minor | <https://www.cmich.edu/program/business-administration> |
| 4 | Economics (Business) | <https://www.cmich.edu/program/economics-business> |
| 5 | Economics (Non-Business) | <https://www.cmich.edu/program/economics-non-business> |
| 6 | Entrepreneurship | <https://www.cmich.edu/program/Entrepreneurship-(Major-Minor)> |
| 7 | Finance | <https://www.cmich.edu/program/finance> |
| 8 | General Business Administration: Applied Business Communication | <https://www.cmich.edu/program/general-business-administration-applied-communication> |
| 9 | Hospitality Services Administration | <https://www.cmich.edu/program/hospitality-services-administration> |
| 10 | Information Systems | <https://www.cmich.edu/program/information-systems> |
| 11 | International Business | <https://www.cmich.edu/program/international-business> |
| 12 | Law and Economics | <https://www.cmich.edu/program/law-economics> |
| 13 | Law and Economics (Business) | <https://www.cmich.edu/program/law-economics-business> |
| 14 | Legal Studies | <https://www.cmich.edu/program/legal-studies> |
| 15 | Marketing | <https://www.cmich.edu/program/marketing> |
| 16 | Marketing: Professional Sales | <https://www.cmich.edu/program/marketing-professional-sales> |
| 17 | Personal Financial Planning | <https://www.cmich.edu/program/personal-financial-planning> |
| 18 | Real Estate: Development & Finance | <https://www.cmich.edu/program/real-estate> |
| 19 | Actuarial and Risk Analytics | <https://www.cmich.edu/program/Actuarial-and-Risk-Analytics-(Minor)> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | Casino Gaming Operations | <https://www.cmich.edu/program/Casino-Gaming-Operations-(Undergraduate-Certificate)> |
| 2 | Cybersecurity | <https://www.cmich.edu/program/cybersecurity> |
| 3 | Entrepreneurial Studies | <https://www.cmich.edu/program/Entrepreneurial-Studies-(Undergraduate-Certificate)> |
| 4 | Marketing Environmental Sustainability | <https://www.cmich.edu/program/Marketing-Environmental-Sustainability-(Undergraduate-Certificate)> |

#### College of Education and Human Services

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development | <https://www.cmich.edu/program/Child-Development-(Major-Minor)> |
| 2 | Community Development: Community Services | <https://www.cmich.edu/program/Community-Development-Option-Concentration-in-Community-Services> |
| 3 | Community Development: Health Sciences | <https://www.cmich.edu/program/Community-Development-Option-Concentration-in-Health-Sciences> |
| 4 | Community Development: Public Administration | <https://www.cmich.edu/program/Community-Development-Option-Concentration-in-Public-Administration> |
| 5 | Disability Studies & Community Inclusion | <https://www.cmich.edu/program/disability-studies-community-inclusion-minor> |
| 6 | Early Childhood Development and Learning | <https://www.cmich.edu/program/early-childhood-development-learning> |
| 7 | Ergonomics Administration | <https://www.cmich.edu/program/Adm-Ergonomics-Administration-Conc> |
| 8 | Family Studies | <https://www.cmich.edu/program/Family-Studies-(Major-Minor)> |
| 9 | Fashion Merchandising and Design | <https://www.cmich.edu/program/Fashion-Merchandising-and-Design-(Major-Minor)> |
| 10 | Health and Physical Education | <https://www.cmich.edu/program/health-physical-education> |
| 11 | Interior Design | <https://www.cmich.edu/program/Interior-Design-(Major-Minor)> |
| 12 | Leadership | <https://www.cmich.edu/program/leadership-minor> |
| 13 | Music Education | <https://www.cmich.edu/program/music-education> |
| 14 | Organizational Leadership | <https://www.cmich.edu/program/Organizational-Leadership-(Major)> |
| 15 | Outdoor and Environmental Education | <https://www.cmich.edu/program/outdoor-and-environmental-education-minor> |
| 16 | Outdoor and Environmental Recreation | <https://www.cmich.edu/program/Outdoor-Environmental-Recreation> |
| 17 | Personnel Administration | <https://www.cmich.edu/program/Adm-Personnel-Administration-Concentration> |
| 18 | Recreational Therapy and Rehabilitation | <https://www.cmich.edu/program/Recreational-Therapy-and-Rehab> |
| 19 | Specialist in General Educational Administration | <https://www.cmich.edu/program/specialist-in-educational-administration> |
| 20 | Teaching Early Childhood B-K & Early Childhood Special Education | <https://www.cmich.edu/program/Teaching-Early-Childhd-B-K-Spec-Ed-MJ> |
| 21 | Teaching English Learners | <https://www.cmich.edu/program/Teaching-English-Learners-(Minor)> |
| 22 | Teaching Grades 3-6 | <https://www.cmich.edu/program/Teaching-Grades-3-6-(Major)> |
| 23 | Teaching Grades 3-6 & Special Education | <https://www.cmich.edu/program/Teaching-Grades-3-6-with-Spec-Ed-(Major)> |
| 24 | Teaching Grades PK-3 | <https://www.cmich.edu/program/Teaching-Grades-PK-3-(Major)> |
| 25 | Teaching Grades PK-6 Major | <https://www.cmich.edu/program/Teaching-Grades-PK-6-(Major)> |
| 26 | Teaching PK-3 with Special Education | <https://www.cmich.edu/program/Teaching-Grades-PK-3-w-Special-Ed-(Major)> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | Deafblind Intervener | <https://www.cmich.edu/program/deafblind-intervener> |
| 2 | Game Design and Social Studies | <https://www.cmich.edu/program/GAME-DESIGN-AND-SOCIAL-STUDIES-(Undergraduate-Certificate)> |

#### College of Liberal Arts and Social Sciences

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | <https://www.cmich.edu/program/anthropology> |
| 2 | Applied Forensic Studies | <https://www.cmich.edu/program/Applied-Forensics-Studies-(Minor)> |
| 3 | Creative Writing Minor | <https://www.cmich.edu/program/Creative-Writing-(Minor)> |
| 4 | English | <https://www.cmich.edu/program/English-(Major)> |
| 5 | French | <https://www.cmich.edu/program/french> |
| 6 | Game Design Thinking | <https://www.cmich.edu/program/Game-Design-Thinking-(Minor)> |
| 7 | German | <https://www.cmich.edu/program/german> |
| 8 | History | <https://www.cmich.edu/program/history> |
| 9 | Intergroup Relations and Justice | <https://www.cmich.edu/program/Intergroup-Relations-and-Justice-(Minor)> |
| 10 | International Relations | <https://www.cmich.edu/program/international-relations> |
| 11 | Military Science | <https://www.cmich.edu/program/military-science> |
| 12 | Museum Studies | <https://www.cmich.edu/program/museum-studies> |
| 13 | Nonprofit Leadership and Service Minor | <https://www.cmich.edu/program/Nonprofit-Leadership--Service-(Minor)> |
| 14 | Philosophy | <https://www.cmich.edu/program/philosophy> |
| 15 | Political Science | <https://www.cmich.edu/program/political-science> |
| 16 | Pre-Law program | <https://www.cmich.edu/program/Pre-Law> |
| 17 | Psychology | <https://www.cmich.edu/program/psychology> |
| 18 | Public History | <https://www.cmich.edu/program/public-history> |
| 19 | Public Law Minor | <https://www.cmich.edu/program/Public-Law-(Minor)> |
| 20 | Public and Applied Liberal Arts | <https://www.cmich.edu/program/applied-liberal-arts> |
| 21 | Public and Nonprofit Administration | <https://www.cmich.edu/program/public-nonprofit-administration> |
| 22 | Religion | <https://www.cmich.edu/program/religion> |
| 23 | Social Science | <https://www.cmich.edu/program/social-science> |
| 24 | Social Work | <https://www.cmich.edu/program/social-work> |
| 25 | Social and Criminal Justice | <https://www.cmich.edu/program/Social-and-Criminal-Justice-(Major)> |
| 26 | Sociology | <https://www.cmich.edu/program/sociology> |
| 27 | Sociology: Youth Studies | <https://www.cmich.edu/program/sociology-youth-studies> |
| 28 | Spanish | <https://www.cmich.edu/program/spanish> |
| 29 | Teaching English Language Arts Grades 5-12 Major | <https://www.cmich.edu/program/Teaching-English-Grades-5-12-(Major)> |
| 30 | Teaching English Language Arts Grades 5-9 (Minor) | <https://www.cmich.edu/program/Teach-ENG-Lang-Arts-Grades-5-9-(Minor)> |
| 31 | Teaching English Language Arts Grades 7-12 (Minor) | <https://www.cmich.edu/program/Teaching-ENG-Language-Arts-Grades-7-12> |
| 32 | Teaching Social Studies Grades 5-12 Major | <https://www.cmich.edu/program/Teaching-Social-Studies-Grades-5-12-Mjr> |
| 33 | Teaching Social Studies Grades 5-9 Minor | <https://www.cmich.edu/program/Teaching-Social-Studies-Grades-5-9-(Minor)> |
| 34 | Teaching Social Studies Grades 7-12 Minor | <https://www.cmich.edu/program/Teaching-Soc-Studies-Grades-7-12-(Minor)> |
| 35 | Women and Gender Studies | <https://www.cmich.edu/program/women-gender-studies> |
| 36 | Applied World Languages and Cultures | <https://www.cmich.edu/program/Applied-World-Languages-and-Cultures> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | African and African Diaspora Studies | <https://www.cmich.edu/program/african-diaspora-studies> |
| 2 | Applied Ethics | <https://www.cmich.edu/program/applied-ethics-undergrad-cert> |
| 3 | Applied Forensic Studies | <https://www.cmich.edu/program/Applied-Forensic-Studies-(Undergraduate-Certificate)> |
| 4 | Creative writing | <https://www.cmich.edu/program/creative-writing> |
| 5 | Critical Reasoning | <https://www.cmich.edu/program/critical-reasoning> |
| 6 | Cultural Competency | <https://www.cmich.edu/program/cultural-competency> |
| 7 | East Asian Studies | <https://www.cmich.edu/program/east-asian-studies> |
| 8 | International Non-Governmental Organization (NGO) Administration | <https://www.cmich.edu/program/international-ngo-administration> |
| 9 | International Security Studies | <https://www.cmich.edu/program/international-security-studies> |
| 10 | LGBTQ+ Studies | <https://www.cmich.edu/program/LGBTQ-Studies-Undergraduate-Certificate> |
| 11 | Latin American and Latino Studies | <https://www.cmich.edu/program/latin-american-latino-studies> |
| 12 | Lawmaking and Legal Processes | <https://www.cmich.edu/program/lawmaking-legal-processes> |
| 13 | Native American and Indigenous Studies | <https://www.cmich.edu/program/Native-American-and-Indigenous-Studies-(Undergraduate-Certificate)> |
| 14 | Political Advocacy and Elections | <https://www.cmich.edu/program/political-advocacy-elections> |
| 15 | Translation (English and Spanish) | <https://www.cmich.edu/program/translation-english-spanish> |
| 16 | Indigenous Studies for Social Studies Educators | <https://www.cmich.edu/program/Indig-Studies-for-Soc-Studies-Educators-(Undergraduate-Certificate)> |

#### College of Science and Engineering

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Actuarial Science | <https://www.cmich.edu/program/actuarial-science> |
| 2 | Astronomy and Astrophysics | <https://www.cmich.edu/program/Astronomy-and-Astrophysics> |
| 3 | Biochemistry | <https://www.cmich.edu/program/biochemistry> |
| 4 | Biological Analytics | <https://www.cmich.edu/program/Biological-Analytics-(Minor)> |
| 5 | Biology: Biomedical, Cellular, & Molecular | <https://www.cmich.edu/program/biology-biomedical-cellular-molecular> |
| 6 | Biology: Ecology, Evolution, and Conservation | <https://www.cmich.edu/program/biology-ecology-evolution-conservation> |
| 7 | Biology: Microscopy | <https://www.cmich.edu/program/biology-microscopy> |
| 8 | Biotechnology: Microscopy | <https://www.cmich.edu/program/Biotechnology-Major-Microscopy-Conc> |
| 9 | Biotechnology: Molecular Biology | <https://www.cmich.edu/program/Biotechnology-Major-Molecular-Bio-Conc> |
| 10 | Chemistry | <https://www.cmich.edu/program/chemistry> |
| 11 | Chemistry: Chemical Technology | <https://www.cmich.edu/program/chemistry-chemical-technology> |
| 12 | Chemistry: Environmental Chemistry | <https://www.cmich.edu/program/environmental-chemistry> |
| 13 | Chemistry: Materials Chemistry | <https://www.cmich.edu/program/materials-chemistry> |
| 14 | Computational Mathematics and Analytics Minor | <https://www.cmich.edu/program/Computational-Math--Analytics-(Minor)> |
| 15 | Computer Engineering | <https://www.cmich.edu/program/computer-engineering> |
| 16 | Computer Science | <https://www.cmich.edu/program/computer-science> |
| 17 | Data Science | <https://www.cmich.edu/program/Data-Science-(Major)> |
| 18 | Electrical Engineering | <https://www.cmich.edu/program/electrical-engineering> |
| 19 | Environmental Analytics | <https://www.cmich.edu/program/Environmental-Analytics-(Minor)> |
| 20 | Environmental Engineering | <https://www.cmich.edu/program/environmental-engineering> |
| 21 | Environmental Health and Safety | <https://www.cmich.edu/program/environmental-health-safety> |
| 22 | Environmental Science | <https://www.cmich.edu/program/environmental-science> |
| 23 | Geography | <https://www.cmich.edu/program/geography> |
| 24 | Geography: Geographic Information Sciences | <https://www.cmich.edu/program/geographic-information-sciences> |
| 25 | Geography: Urban and Community Planning | <https://www.cmich.edu/program/Geo-MJ-Urban--Community-Planning-Conc> |
| 26 | Geology | <https://www.cmich.edu/program/geology> |
| 27 | Industrial Engineering Technology | <https://www.cmich.edu/program/industrial-engineering-technology> |
| 28 | Industrial Technology | <https://www.cmich.edu/program/industrial-technology> |
| 29 | Information Technology | <https://www.cmich.edu/program/information-technology> |
| 30 | Mathematics | <https://www.cmich.edu/program/mathematics> |
| 31 | Mechanical Engineering | <https://www.cmich.edu/program/mechanical-engineering> |
| 32 | Mechanical Engineering Technology | <https://www.cmich.edu/program/mechanical-engineering-technology> |
| 33 | Meteorology | <https://www.cmich.edu/program/meteorology> |
| 34 | Neuroscience: Cell and Molecular | <https://www.cmich.edu/program/Neuroscience-Cell-Molecular> |
| 35 | Biology | <https://www.cmich.edu/program/biology-minor> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | Cartographic Design | <https://www.cmich.edu/program/cartographic-design> |
| 2 | Cloud computing | <https://www.cmich.edu/program/Cloud-Computing-(Undergraduate-Certificate)> |
| 3 | Database Development | <https://www.cmich.edu/program/Database-Development-(Undergraduate-Certificate)> |
| 4 | Environmental Justice | <https://www.cmich.edu/program/Environmental-Justice-(Undergraduate-Certificate)> |
| 5 | Integration of Science, Technology and Engineering | <https://www.cmich.edu/program/Integration-of-Sci-Tech--EGR-(InSciTE)-(Undergraduate-Certificate)> |
| 6 | Mobile Computing | <https://www.cmich.edu/program/Mobile-Computing-(Undergraduate-Certificate)> |
| 7 | Network Administration | <https://www.cmich.edu/program/Network-Administration-(Undergraduate-Certificate)> |
| 8 | Web development | <https://www.cmich.edu/program/Web-Development-(Undergraduate-Certificate)> |

#### College of the Arts and Media

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | <https://www.cmich.edu/program/advertising> |
| 2 | Art: Animation | <https://www.cmich.edu/program/art-animation> |
| 3 | Art: Art History | <https://www.cmich.edu/program/art-history> |
| 4 | Art: Graphic Design | <https://www.cmich.edu/program/graphic-design> |
| 5 | Art: Studio Art | <https://www.cmich.edu/program/studio-art> |
| 6 | Cinema Arts | <https://www.cmich.edu/program/cinema-arts> |
| 7 | Commercial Music | <https://www.cmich.edu/program/Commercial-Music> |
| 8 | Communication | <https://www.cmich.edu/program/communication> |
| 9 | Dance | <https://www.cmich.edu/program/Dance-Minor-Non-Teaching> |
| 10 | Dance Studies | <https://www.cmich.edu/program/Dance-Studies> |
| 11 | Digital Strategy | <https://www.cmich.edu/program/Digital-Strategy-Undergraduate-(Minor)> |
| 12 | Integrative Public Relations | <https://www.cmich.edu/program/integrative-public-relations> |
| 13 | Journalism | <https://www.cmich.edu/program/journalism> |
| 14 | Multimedia Design | <https://www.cmich.edu/program/multimedia-design> |
| 15 | Music | <https://www.cmich.edu/program/music> |
| 16 | Music (B.Mus.) | <https://www.cmich.edu/program/music-bm> |
| 17 | Music Theatre | <https://www.cmich.edu/program/music-theatre> |
| 18 | Photojournalism | <https://www.cmich.edu/program/photojournalism> |
| 19 | Songwriting | <https://www.cmich.edu/program/Songwriting> |
| 20 | Sports Communication | <https://www.cmich.edu/program/Sports-Communication-Minor> |
| 21 | Theatre & Interpretation | <https://www.cmich.edu/program/theatre-interpretation> |
| 22 | Theatre & Interpretation: Acting & Directing | <https://www.cmich.edu/program/theatre-interpretation-acting-directing> |
| 23 | Theatre & Interpretation: Design & Technical Theatre | <https://www.cmich.edu/program/theatre-interpretation-design-technical> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | Corporate Video | <https://www.cmich.edu/program/corporate-video> |
| 2 | Drone Regulations, Operations, and Applications | <https://www.cmich.edu/program/Drone-Operations-Undergraduate-Certificate> |
| 3 | Health communication | <https://www.cmich.edu/program/Health-Communication-(Undergraduate-Certificate)> |
| 4 | Professional Communication and Presentation Skills | <https://www.cmich.edu/program/Prof-Comm-Presentation-Skills> |
| 5 | Professional Video | <https://www.cmich.edu/program/Professional-Video-Certificate> |
| 6 | Social Media | <https://www.cmich.edu/program/Social-Media-Undergraduate-Certificate> |

#### The Herbert H. and Grace A. Dow College of Health Professions

##### Undergraduate (BS / B.S. / BSBA)
| # | 专业 | URL |
|---|------|-----|
| 1 | American Sign Language | <https://www.cmich.edu/program/american-sign-language> |
| 2 | Athletic Coaching | <https://www.cmich.edu/program/athletic-coaching> |
| 3 | Communication Sciences and Disorders | <https://www.cmich.edu/program/communication-sciences-disorders> |
| 4 | Dietetics | <https://www.cmich.edu/program/dietetics> |
| 5 | Health Administration | <https://www.cmich.edu/program/health-administration> |
| 6 | Health Fitness and Performance | <https://www.cmich.edu/program/health-fitness-performance-minor> |
| 7 | Nursing BSN | <https://www.cmich.edu/program/nursing-bsn> |
| 8 | Nutrition | <https://www.cmich.edu/program/nutrition> |
| 9 | Pre-Occupational Therapy | <https://www.cmich.edu/program/Pre-Occupational-Therapy> |
| 10 | Pre-Physical Therapy Pathway | <https://www.cmich.edu/program/Pre-Physical-Therapy> |
| 11 | Pre-physician assistant program | <https://www.cmich.edu/program/Pre-Physician-Assistant> |
| 12 | Public Health | <https://www.cmich.edu/program/public-health> |
| 13 | Public Health Minor | <https://www.cmich.edu/program/Public-Health-(Minor)> |
| 14 | RN to BSN Program | <https://www.cmich.edu/program/Nursing-(Major)> |
| 15 | Speech-Language Pathology | <https://www.cmich.edu/program/speech-language-pathology> |
| 16 | Sports Administration | <https://www.cmich.edu/program/sports-administration> |
| 17 | Substance Use Disorders | <https://www.cmich.edu/program/substance-use-disorders> |

##### Undergraduate Certificates
| # | Certificate | URL |
|---|------|-----|
| 1 | Deaf and Hard of Hearing Studies | <https://www.cmich.edu/program/Deaf-and-Hard-of-Hearing-Studies-(Undergraduate-Certificate)> |

##### Combined Undergraduate & Graduate
| # | Program | URL |
|---|------|-----|
| 1 | Athletic Training | <https://www.cmich.edu/program/Athletic-Training> |


### 1.3 Interdisciplinary / cross-college undergraduate programs

The following programs are administratively housed in multiple CMU colleges:

| # | Program | Primary College(s) | URL |
|---|---------|-------------------|-----|
| 1 | Music Education | College of Education and Human Services; College of the Arts and Media | <https://www.cmich.edu/program/music-education> |
| 2 | Health and Physical Education | College of Education and Human Services; The Herbert H. and Grace A. Dow College of Health Professions | <https://www.cmich.edu/program/health-physical-education> |
| 3 | Teaching English Learners | College of Education and Human Services; College of Liberal Arts and Social Sciences | <https://www.cmich.edu/program/Teaching-English-Learners-(Minor)> |
| 4 | Environmental Health and Safety | College of Science and Engineering; The Herbert H. and Grace A. Dow College of Health Professions | <https://www.cmich.edu/program/environmental-health-safety> |
| 5 | Marketing Environmental Sustainability | College of Business Administration; College of Science and Engineering | <https://www.cmich.edu/program/Marketing-Environmental-Sustainability-(Undergraduate-Certificate)> |

### 1.4 Minors — complete list

CMU offers approximately 60+ undergraduate minors, including (non-exhaustive list):

| # | Minor | URL |
|---|-------|-----|
| 1 | Actuarial and Risk Analytics | <https://www.cmich.edu/program/Actuarial-and-Risk-Analytics-(Minor)> |
| 2 | Applied Artificial Intelligence | <https://www.cmich.edu/program/Applied-Artificial-Intelligence-(Minor)> |
| 3 | Applied Business Communication | <https://www.cmich.edu/program/applied-business-communication> |
| 4 | Applied Forensic Studies | <https://www.cmich.edu/program/Applied-Forensics-Studies-(Minor)> |
| 5 | Biological Analytics | <https://www.cmich.edu/program/Biological-Analytics-(Minor)> |
| 6 | Business Administration | <https://www.cmich.edu/program/business-administration> |
| 7 | Computational Mathematics and Analytics | <https://www.cmich.edu/program/Computational-Math--Analytics-(Minor)> |
| 8 | Creative Writing | <https://www.cmich.edu/program/Creative-Writing-(Minor)> |
| 9 | Digital Strategy | <https://www.cmich.edu/program/Digital-Strategy-Undergraduate-(Minor)> |
| 10 | Disability Studies & Community Inclusion | <https://www.cmich.edu/program/disability-studies-community-inclusion-minor> |
| 11 | Entrepreneurship | <https://www.cmich.edu/program/Entrepreneurship-(Major-Minor)> |
| 12 | Environmental Analytics | <https://www.cmich.edu/program/Environmental-Analytics-(Minor)> |
| 13 | Family Studies | <https://www.cmich.edu/program/Family-Studies-(Major-Minor)> |
| 14 | Fashion Merchandising and Design | <https://www.cmich.edu/program/Fashion-Merchandising-and-Design-(Major-Minor)> |
| 15 | Teaching English Learners | <https://www.cmich.edu/program/Teaching-English-Learners-(Minor)> |
| 16 | Child Development | <https://www.cmich.edu/program/Child-Development-(Major-Minor)> |

> Note: Many CMU programs offer both Major and Minor in the same URL/curriculum path; consult each program page for specifics.

### 1.5 General / Institute-wide requirements

CMU requires all undergraduates to complete the **General Education Program** which provides a broad-based liberal arts foundation. Honors Program participants complete an enhanced curriculum.

- General Education Program: <https://www.cmich.edu/academics/general-education>
- Honors Program: <https://www.cmich.edu/academics/honors-program>

### 1.6 Course-ID → Major quick-lookup

CMU does not use a numbered course-id system for majors (unlike MIT's "Course 6" or Caltech's options). Programs are referenced by name. However, each academic department has a 2-4 letter subject code (e.g., "ACC" for Accounting, "BIO" for Biology, "CSC" for Computer Science).

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

CMU offers approximately 95 graduate programs (Master's, Specialist, Doctoral, and Graduate Certificate levels). Master's tuition is $862/credit hour for U.S. residents ($1,062 international). Doctoral tuition is $962/credit hour for U.S. residents ($1,162 international).

#### College of Business Administration

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | <https://www.cmich.edu/program/economics-ma> |
| 2 | General Management | <https://www.cmich.edu/program/general-management> |
| 3 | Human Resource Management | <https://www.cmich.edu/program/human-resource-management> |
| 4 | Logistics Management | <https://www.cmich.edu/program/logistics-management> |
| 5 | Master of Business Administration | <https://www.cmich.edu/program/master-of-business-administration> |
| 6 | Purchasing and Supply Management | <https://www.cmich.edu/program/purchasing-supply-management> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Systems | <https://www.cmich.edu/program/information-systems-ms> |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | <https://www.cmich.edu/program/cybersecurity-grad> |
| 2 | Finance | <https://www.cmich.edu/program/finance-graduate-certificate> |
| 3 | Logistics Management | <https://www.cmich.edu/program/Logistics-Management-(Graduate-Certificate)> |

#### College of Education and Human Services

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling | <https://www.cmich.edu/program/Counseling-MA> |
| 2 | Early Childhood Leadership | <https://www.cmich.edu/program/MA--Early-Childhood-Leadership> |
| 3 | Education (Training and Development) | <https://www.cmich.edu/program/education-training-development-ma> |
| 4 | Event Management | <https://www.cmich.edu/program/event-management> |
| 5 | Event and Recreation Management | <https://www.cmich.edu/program/Event-Recreation-Management> |
| 6 | Fashion Merchandising & Design | <https://www.cmich.edu/program/Master-of-Science-in-Fashion-Merchandising-and-Design> |
| 7 | Master of Science in Administration | <https://www.cmich.edu/program/master-of-science-administration> |
| 8 | Masters in curriculum and instruction | <https://www.cmich.edu/program/education-curriculum-and-instruction-ma> |
| 9 | Reading and Literacy (K-12) | <https://www.cmich.edu/program/reading-literacy-k12-ma> |
| 10 | Special Education | <https://www.cmich.edu/program/Special-Education-Major> |
| 11 | Special Education: The Master Teacher | <https://www.cmich.edu/program/special-education-master-teacher> |
| 12 | Teaching Early Childhood B-3 & Early Childhood Special Education | <https://www.cmich.edu/program/Teaching-Early-Childhd-B-3--Spec-Ed-Maj> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership (MA) | <https://www.cmich.edu/program/educational-leadership> |
| 2 | Higher Education Administration and Social Justice | <https://www.cmich.edu/program/MA-Higher-Education-Social-Justice> |
| 3 | Learning, Design and Technology | <https://www.cmich.edu/program/learning-design-technology> |

##### Doctoral Programs (Ph.D. / Ed.D. / DPT / Au.D. / DHA)
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | <https://www.cmich.edu/program/educational-leadership-edd> |
| 2 | Educational Technology | <https://www.cmich.edu/program/educational-technology-det> |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | AI for learning, design and technology | <https://www.cmich.edu/program/AI-for-Learning-Design-and-Technology-(Graduate-Certificate)> |
| 2 | Digital Management | <https://www.cmich.edu/program/Digital-Management-(Graduate-Certificate)> |
| 3 | Disability Studies & Community Inclusion | <https://www.cmich.edu/program/Disability-Studies--Community-Inclusion-(Graduate-Certificate)> |
| 4 | Engineering Management | <https://www.cmich.edu/program/engineering-management> |
| 5 | Equity-Centered Teaching and Learning | <https://www.cmich.edu/program/Equity-Centered-Teaching-and-Learning> |
| 6 | Executive Management | <https://www.cmich.edu/program/Executive-Management-Certificate-(Graduate-Certificate)> |
| 7 | General Administration | <https://www.cmich.edu/program/general-administration> |
| 8 | Health Services Administration | <https://www.cmich.edu/program/health-services-administration> |
| 9 | Human Resources Administration | <https://www.cmich.edu/program/human-resources-administration> |
| 10 | Leadership | <https://www.cmich.edu/program/leadership> |
| 11 | Philanthropy and Nonprofit Organizations | <https://www.cmich.edu/program/philanthropy-nonprofit-organizations> |
| 12 | Project Management | <https://www.cmich.edu/program/project-management> |
| 13 | Public Administration | <https://www.cmich.edu/program/public-administration-grad> |
| 14 | Talent Development | <https://www.cmich.edu/program/Talent-Development> |
| 15 | Postgraduate School Counseling Certificate | <https://www.cmich.edu/program/Postgraduate-School-Counseling-(Graduate-Certificate)> |

#### College of Liberal Arts and Social Sciences

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Creative Writing | <https://www.cmich.edu/program/Creative-Writing-MA> |
| 2 | History | <https://www.cmich.edu/program/history-ma> |
| 3 | Master of Public Administration | <https://www.cmich.edu/program/Master-of-Public-Administration> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Experimental Psychology | <https://www.cmich.edu/program/experimental-psychology> |
| 2 | Industrial / Organizational Psychology | <https://www.cmich.edu/program/industrial-organizational-psychology> |
| 3 | School Psychology Specialist | <https://www.cmich.edu/program/school-psychology-specialist> |

##### Doctoral Programs (Ph.D. / Ed.D. / DPT / Au.D. / DHA)
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Experimental Psychology | <https://www.cmich.edu/program/applied-experimental-psychology-phd> |
| 2 | Industrial / Organizational Psychology | <https://www.cmich.edu/program/industrial-organizational-psychology-phd> |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Leadership | <https://www.cmich.edu/program/nonprofit-leadership> |

#### College of Medicine

##### Doctoral Programs (Ph.D. / Ed.D. / DPT / Au.D. / DHA)
| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | <https://www.cmich.edu/program/medicine-md> |

#### College of Science and Engineering

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Cybersecurity | <https://www.cmich.edu/program/Cybersecurity-Major> |
| 2 | Geology: Green energy | <https://www.cmich.edu/program/Geology-Major-BS-Green-Energy-Concent> |
| 3 | Integrated Science for Secondary Education | <https://www.cmich.edu/program/Integrated-Science-Major> |
| 4 | Mathematics | <https://www.cmich.edu/program/mathematics-ma> |
| 5 | Mathematics: Applied Mathematics | <https://www.cmich.edu/program/applied-mathematics> |
| 6 | Mathematics: Pure Mathematics | <https://www.cmich.edu/program/pure-mathematics> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics and Analytics | <https://www.cmich.edu/program/applied-statistics-analytics> |
| 2 | Biochemistry, Cell and Molecular Biology | <https://www.cmich.edu/program/biochemistry-cell-molecular-biology> |
| 3 | Biology | <https://www.cmich.edu/program/biology-ms> |
| 4 | Chemistry | <https://www.cmich.edu/program/chemistry-ms> |
| 5 | Computer Science | <https://www.cmich.edu/program/computer-science-ms> |
| 6 | Engineering | <https://www.cmich.edu/program/engineering-ms> |
| 7 | Neuroscience | <https://www.cmich.edu/program/neuroscience-ms> |
| 8 | Physics | <https://www.cmich.edu/program/physics-ms> |

##### Doctoral Programs (Ph.D. / Ed.D. / DPT / Au.D. / DHA)
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry, Cell and Molecular Biology | <https://www.cmich.edu/program/biochemistry-cell-molecular-biology-phd> |
| 2 | Earth and Ecosystem Science | <https://www.cmich.edu/program/earth-ecosystem-science-phd> |
| 3 | Mathematical Sciences | <https://www.cmich.edu/program/mathematical-sciences-phd> |
| 4 | Neuroscience | <https://www.cmich.edu/program/neuroscience-phd> |
| 5 | Physics | <https://www.cmich.edu/program/physics-phd> |
| 6 | Science of Advanced Materials | <https://www.cmich.edu/program/science-of-advanced-materials-phd> |
| 7 | Statistics and Analytics | <https://www.cmich.edu/program/statistics-analytics-phd> |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Mining | <https://www.cmich.edu/program/data-mining> |

#### College of the Arts and Media

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | <https://www.cmich.edu/program/communication-ma> |
| 2 | Media Arts | <https://www.cmich.edu/program/media-arts-major> |
| 3 | Music Composition | <https://www.cmich.edu/program/master-of-music-composition> |
| 4 | Music: Conducting | <https://www.cmich.edu/program/master-of-music-in-conducting> |
| 5 | Music: Education | <https://www.cmich.edu/program/master-of-music-in-education> |
| 6 | Music: Performance | <https://www.cmich.edu/program/master-of-music-in-performance> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Media Arts | <https://www.cmich.edu/program/MA-in-Media-Arts> |

#### The Herbert H. and Grace A. Dow College of Health Professions

##### Master of Arts (M.A.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training | <https://www.cmich.edu/program/master-science-athletic-training> |
| 2 | Exercise Science | <https://www.cmich.edu/program/exercise-science-major> |
| 3 | Master of Health Administration | <https://www.cmich.edu/program/master-of-health-administration> |
| 4 | Master of Public Health | <https://www.cmich.edu/program/master-of-public-health> |
| 5 | Sport Management | <https://www.cmich.edu/program/sport-management> |

##### Master of Science (M.S.)
| # | 项目 | URL |
|---|------|-----|
| 1 | Exercise Physiology | <https://www.cmich.edu/program/exercise-physiology> |
| 2 | Physician Assistant | <https://www.cmich.edu/program/physician-assistant> |

##### Doctoral Programs (Ph.D. / Ed.D. / DPT / Au.D. / DHA)
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Audiology | <https://www.cmich.edu/program/doctor-of-audiology> |
| 2 | Doctor of Health Administration | <https://www.cmich.edu/program/doctor-of-health-administration> |
| 3 | Doctor of Physical Therapy | <https://www.cmich.edu/program/doctor-of-physical-therapy-dpt> |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 1 | Health Systems Leadership | <https://www.cmich.edu/program/health-systems-leadership> |
| 2 | Health and Physical Education (Graduate Certificate) | <https://www.cmich.edu/program/Health-and-Physical-Education-(Graduate-Certificate)> |
| 3 | International Health | <https://www.cmich.edu/program/international-health> |
| 4 | Structured Language and Literacy Intervention | <https://www.cmich.edu/program/Structured-Language-and-Literacy-Intervention-(Graduate-Certificate)> |

### 2.2 At least one program's full deep-dive (worked example)

**Master of Business Administration (MBA)** — one of CMU's largest graduate programs:

- **Department address**: College of Business Administration, Grawn Hall 250, 150 E. Bellows, Mount Pleasant, MI 48859
- **Phone**: 989-774-3337
- **Email**: cba@cmich.edu
- **Application portal**: <https://fireup.cmich.edu/portal/apply/>
- **Application fee**: $50 (domestic)
- **English proficiency required** for international applicants
- **Tuition**: International MBA total ~$33,220 (9 months, 18 credits/year load); domestic rates lower
- **Funding**: Graduate assistantships, scholarships via Scholarship Universe
- **Career outcomes**: 95% employed within 6 months, $62,000 average starting salary for CBA graduates

**Worked example accordion-style content (per-program FAQ live on site)**:
- Application materials: 2-3 letters of recommendation, personal statement, resume, GMAT/GRE (recommended not required)
- GMAT minimum: Not required; class profile typically 500-650
- Class size: ~25-40 students
- AACSB-accredited (top 3% globally)

### 2.3 Graduate admissions model

CMU Graduate Admissions is **decentralized at the program level** but coordinated by the Office of Graduate Studies:
- All applicants apply through the FireUp portal: <https://fireup.cmich.edu/portal/apply/>
- Application fee: $50 domestic, varies for international
- **Special application portals** required for College of Health Professions programs (Athletic Training MSAT, Audiology AuD, Physician Assistant MS, Physical Therapy DPT, Speech-Language Pathology MA) — call 989-774-1730 or email chpgradadm@cmich.edu
- College of Medicine (MD) uses separate admissions: <https://www.cmich.edu/academics/colleges/college-of-medicine/education/md/admissions>
- Graduate Admissions contact: grad@cmich.edu, 989-774-4723, Ronan 330
- International graduate admissions: isr@cmich.edu, +1-989-774-1619

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| Field | Value | Notes |
|-------|-------|-------|
| Admissions site | <https://www.cmich.edu/undergraduate> | Main undergraduate admissions hub |
| Application portal | <https://fireup.cmich.edu/portal/apply/> | FireUp portal |
| Common App accepted | Yes | "You can also apply using the Common Application" |
| Application opens | Aug. 1 of senior year | "Our application opens on Aug. 1 of your senior year" |
| Application fee | $40 | "submit a $40 application fee. You may be eligible to have your fee waived" |
| Fee waiver eligibility | Financial hardship, military, CMU-sponsored charter school students | |
| EA deadline | N/A | CMU does not offer Early Action |
| RD / Regular deadline | Rolling until classes begin | "Applications are accepted until classes begin" |
| Priority scholarship deadline (Freshmen) | Oct. 15 | "recommend applying by Oct. 15 to be considered for all competitive scholarship programs" |
| First-come-first-served merit scholarship priority | Dec. 1 | "Priority consideration for first-come, first-served merit scholarship funds is given to applications completed by Dec. 1" |
| Spring semester priority | Dec. 1 | "Students applying to start in the spring semester are also encouraged to apply by Dec. 1" |
| Transfer priority (summer/fall) | March 1 | "Submit all your application materials by March 1 for the summer/fall semesters" |
| Transfer priority (spring) | Dec. 1 | "and Dec. 1 for the spring semester, to get priority consideration for our merit scholarships" |
| Decision notification | Rolling | Based on completed application |
| Enrollment confirmation / deposit | See Admitted Students page | <https://www.cmich.edu/undergraduate/admitted> |
| Financial aid deadline | FAFSA priority March 1 (Michigan residents) | CMU school code: 002243 |
| SAT/ACT policy | **Test-optional** for freshmen | "submitting your test scores may enhance your likelihood of being admitted or earning a higher merit scholarship (this applies to freshmen only)" |
| SAT/ACT requirement exception | Required for homeschooled students or those attending high school without grades | "If you are homeschooled or attend a high school that does not provide grades, an ACT/SAT test score is required" |
| SAT code | 1106 | |
| ACT code | 1972 | |
| Superscore policy | Yes — "best scores" accepted | "When tests provide 'best scores' in specific areas, CMU will use the composite score generated by using the highest from each section" |
| Test validity | 2 years from test date | "Test scores are valid for two (2) years from the test date" |
| Essay required | **No** | "An admissions essay is not required but you may submit additional information" |
| Recommendation letters | Not required for UG admission | May submit additional info |
| Interview policy | Not required | |
| Portfolios | Required for select Art/Design programs | Per program |
| Transfer pathway | <https://www.cmich.edu/undergraduate/transfer-students> | |
| Dual enrollment | <https://www.cmich.edu/undergraduate/apply/dual-enrollment> | |
| AP/IB/CLEP testing | <https://www.cmich.edu/undergraduate/apply/testing-for-credit> | |
| Michigan Assured Admission Pact | <https://www.cmich.edu/undergraduate/apply/michigan-assured-admission-pact> | Guaranteed admission for qualifying MI students |
| Honors Program | <https://www.cmich.edu/academics/honors-program> | Separate application |
| Required HS coursework | 4 years English, Math, Bio/Physical Science, History/Social Science; 2 years foreign language + fine arts; 1 year computer experience (recommended) | Not strict requirement but recommended for success |

### 3.2 Undergraduate English proficiency table (international applicants)

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL (IBT) | 79 | 100 |
| TOEFL (PBT) | 550 | — |
| IELTS | 6.5 | 7.0 |
| Pearson PTE | 53 | — |
| Duolingo | 100 | — |
| Michigan English Test (MET) | 52 | — |
| IB English HL | 5 | — |
| AP English Language/Literature | 4 | — |
| GCSE/GCE English | A or B | — |
| SAT EBRW | 520 | — |
| ACT English | 21 | — |
| ELS Language Center | Completion of Level 112 | — |

**Exemptions:**
- Graduate of a U.S. high school with at least three years of attendance
- Completion of courses meeting CMU's requirements for Oral English (COM 101) and Writing Competency (ENG 101/103 and ENG 201)
- Successful completion of a course of study (high school diploma, associate degree, baccalaureate) at an institution where the language of instruction is English
- Successful completion of 24+ graded, academic, postsecondary credits with GPA 2.50 at an institution where the language of instruction is English

> **Source**: <https://www.cmich.edu/international-admissions/contact/english-proficiency>

### 3.3 Graduate — global rules

CMU Graduate Admissions is **decentralized** — each program sets its own requirements, deadlines, and materials. The Office of Graduate Studies (Ronan 330, 989-774-4723, grad@cmich.edu) provides overall coordination.

| Field | Value |
|-------|-------|
| Application portal | <https://fireup.cmich.edu/portal/apply/> (main) |
| Special portals | College of Health Professions (chpgradadm@cmich.edu, 989-774-1730): MSAT, AuD, MS-PA, DPT, MA-SLP |
| College of Medicine (MD) | <https://www.cmich.edu/academics/colleges/college-of-medicine/education/md/admissions> |
| Application fee (domestic) | $50 |
| Application fee (international) | Varies by program |
| Fee waiver | Available for service members |
| Admission types | Regular, Concurrent (while in UG), Accelerated (UG-to-Grad), Non-degree |
| GRE/GMAT | **Program-dependent**. Most programs do not require GRE; some have recommended minimums (e.g., MBA: GMAT ~500-650). For international grad scholarship: GRE Verbal ≥ 157 and Quantitative ≥ 152, OR GMAT ≥ 600 |
| English proficiency (intl) | TOEFL ≥ 100 IBT or IELTS ≥ 7.0 for international scholarship (Out-of-State Tuition Merit Award) |
| School Code (TOEFL) | 1106 |
| FAFSA code | 002243 |
| CGS April-15-equivalent honor date | CMU is not a CGS April-15 signatory; CMU uses graduate assistantship contracts individually |
| Funding forms | Graduate assistantships (RA/TA/admin) with stipend + tuition waiver; departmental scholarships; Scholarship Universe; on-campus employment |
| International grad assistantship | Available; F-1 students may work on-campus up to 20 hrs/week |

---

## SECTION 4 — Costs & Financial Aid

CMU uses a "Cost of Attendance" (COA) model with direct costs (billed by CMU: tuition, fees, food/housing if on-campus) and indirect costs (estimated expenses not billed: books, transportation, personal). AY 2025-2026 is the current published year. In-state and out-of-state U.S. students pay the same tuition; only international students pay a different rate.

### 4.1 Undergraduate cost (academic year 2025-2026, line-itemized)

#### Mount Pleasant Campus — Undergraduate lower division living on campus

| Expense Item | Amount | Description |
|--------------|--------|-------------|
| **Direct Costs** | | |
| Tuition | $14,970 | Lower division (estimated 30 credit hours/AY) |
| Food and Housing | $12,902 | On-campus |
| Student Services Fee | $450 | |
| **Sub-Total Direct** | **$28,322** | |
| **Indirect Costs** | | |
| Books, Course Materials, Supplies & Equipment | $1,290 | |
| Loan Fees | $100 | |
| Transportation | $1,340 | |
| Misc. Personal Expenses | $1,537 | |
| **Sub-Total Indirect** | **$4,267** | |
| **Total Estimated COA** | **$32,589** | |

#### Mount Pleasant Campus — Undergraduate upper division living on campus

| Expense Item | Amount |
|--------------|--------|
| Tuition | $16,560 |
| Food and Housing | $12,902 |
| Student Services Fee | $450 |
| **Sub-Total Direct** | **$29,912** |
| Books, Course Materials, Supplies & Equipment | $1,250 |
| Loan Fees | $100 |
| Transportation | $1,290 |
| Misc. Personal Expenses | $1,460 |
| **Sub-Total Indirect** | **$4,267** |
| **Total Estimated COA** | **$34,179** |

#### Mount Pleasant Campus — Undergraduate lower division living OFF campus

| Expense Item | Amount |
|--------------|--------|
| Tuition | $14,970 |
| Student Services Fee | $450 |
| **Sub-Total Direct** | **$15,420** |
| Food and Housing | $8,874 |
| Books, Course Materials, Supplies & Equipment | $1,290 |
| Loan Fees | $100 |
| Transportation | $2,010 |
| Misc. Personal Expenses | $1,537 |
| **Sub-Total Indirect** | **$13,811** |
| **Total Estimated COA** | **$29,231** |

#### International Undergraduate (9-month academic year 2025-2026)

| Expense Item | Amount |
|--------------|--------|
| Tuition & fees (24-credit-hour load) | $21,450 |
| Housing & food | $12,902 |
| Miscellaneous expenses (books, incidentals, personal) | $3,500 |
| Health insurance | $1,550 |
| **Total Estimated COA** | **$39,402** |

> **Required**: Incoming freshmen must live on campus for first two years. Transfer students entering with college credits are exempt.

### 4.2 Undergraduate financial-aid policy

| Item | Value | Notes |
|------|-------|-------|
| Tuition-free income threshold | **None** (CMU does not offer a tuition-free threshold) | Standard merit + need-based aid |
| Need-blind (domestic) | **Yes** | U.S. applicants not screened on ability to pay for admission |
| Need-blind (international) | **No** | International applicants must show proof of financial support for I-20 issuance |
| Median actual price paid (after aid) | N/A — not published | <https://www.cmich.edu/undergraduate/cost-aid-scholarships/college-affordability> |
| Merit scholarship (max) | Up to $8,250/yr | "Earn up to $8,250 per year with merit scholarships" |
| International President's Award | Domestic tuition rate (saves $8,952-$9,024/yr) | Requires 3.3+ GPA |
| International Scholar Award | $4,000/yr for 4 yrs | Requires 3.0-3.29 GPA |
| International Opportunity Award | $1,000/yr for 4 yrs | Requires 2.8-2.9 GPA |
| Centralis Scholarship (Honors) | Up to full tuition/fees/room/board for 4 yrs | Competitive; Honors College membership |
| Average starting salary (CBA) | $62,000 | "95% employed within 6 months" |
| 94.9% career outcome rate | Yes | "employed, volunteering or in grad school within 6 months" |

### 4.3 Graduate cost & funding framework

#### Main campus graduate tuition (per credit hour, AY 2025-2026)

| Student Type | Master's / Specialist | Doctoral |
|--------------|----------------------|----------|
| U.S. resident | $862 | $962 |
| International | $1,062 | $1,162 |

> U.S. residents pay in-state tuition regardless of state of residence. Specialty programs (MBA, MSIS) have unique rates.

#### International graduate cost (9-month academic year 2025-2026)

| Expense Item | Master's | MBA | MSIS | Doctoral |
|--------------|----------|-----|------|----------|
| Tuition & Fees (18 credit hours) | $18,972 | $16,686 | $16,686 | $20,772 |
| Housing & Food | $11,484 | $11,484 | $11,484 | $11,484 |
| Misc. Expenses (books, incidentals, personal) | $3,500 | $3,500 | $3,500 | $3,500 |
| Health Insurance | $1,550 | $1,550 | $1,550 | $1,550 |
| **Total** | **$35,506** | **$33,220** | **$33,220** | **$37,306** |

> F-1 students are required to take a full-time load (12 credits UG, 9 credits master's/MBA/doctorate). Dependents: $5,000 for spouse, $2,500 per minor child.

#### Funding forms

| Form | Description | Eligibility |
|------|-------------|-------------|
| Graduate Assistantships (RA/TA/admin) | Stipend + tuition waiver | Domestic & international; applied to academic department |
| Scholarship Universe | University-wide matching | All admitted students |
| Departmental scholarships | Discretionary | By department |
| Federal Loans (FAFSA) | File FAFSA, code 002243 | Domestic graduate students in degree programs |
| On-campus employment | Up to 20 hrs/week (F-1) | International |
| Out-of-State Tuition Merit Award | Domestic tuition rate | International grad: 3.0+ GPA + GRE (157V/152Q) or GMAT 600+ + English prof. |
| Neighboring Regions Merit Award | Domestic tuition rate | International grad from Ontario, Canada; 3.0+ GPA |
| Legacy Tuition Award | Resident tuition | International grad with CMU-alum parent/grandparent |

---

## SECTION 5 — Evidence Chain Index

Each high-value field is cited to a source URL with a verbatim snippet captured on 2026-07-07.

### 5.1 Undergraduate admissions facts

```yaml
field: undergraduate.application_opens
value: "Aug. 1 of senior year"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "Our application opens on Aug. 1 of your senior year."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.application_fee_usd
value: 40
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "submit a $40 application fee. You may be eligible to have your fee waived"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.freshman_priority_scholarship_deadline
value: "Oct. 15"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "we recommend applying by Oct. 15 to be considered for all competitive scholarship programs"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.freshman_first_come_first_served_deadline
value: "Dec. 1"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "Priority consideration for first-come, first-served merit scholarship funds is given to applications completed by Dec. 1"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.transfer_summer_fall_priority_deadline
value: "March 1"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "Submit all your application materials by March 1 for the summer/fall semesters"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.test_policy
value: "Test-optional (recommended but not required for freshmen)"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "submitting your test scores may enhance your likelihood of being admitted or earning a higher merit scholarship (this applies to freshmen only)"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.test_required_for_homeschooled
value: "Required if no HS grades"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "If you are homeschooled or attend a high school that does not provide grades, an ACT/SAT test score is required."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.sat_code
value: "1106"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "SAT code: 1106"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.act_code
value: "1972"
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "ACT code: 1972"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: undergraduate.essay_required
value: false
source_url: https://www.cmich.edu/undergraduate/apply
source_snippet: "An admissions essay is not required but you may submit additional information"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### 5.2 English proficiency facts

```yaml
field: international_undergraduate.toefl_ibt_min
value: 79
source_url: https://www.cmich.edu/international-admissions/contact/english-proficiency
source_snippet: "TOEFL: 550 PBT/79 IBT for regular admission. School Code 1106"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: international_undergraduate.ielts_min
value: 6.5
source_url: https://www.cmich.edu/international-admissions/contact/english-proficiency
source_snippet: "IELTS: 6.5 for regular admission."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: international_undergraduate.duolingo_min
value: 100
source_url: https://www.cmich.edu/international-admissions/contact/english-proficiency
source_snippet: "Duolingo: 100 for regular admissions."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: international_undergraduate.pearson_pte_min
value: 53
source_url: https://www.cmich.edu/international-admissions/contact/english-proficiency
source_snippet: "Pearson Test of English (PTE): 53 for regular admission."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: international_undergraduate.test_validity_years
value: 2
source_url: https://www.cmich.edu/international-admissions/contact/english-proficiency
source_snippet: "Test scores are valid for two (2) years from the test date."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### 5.3 Graduate admissions facts

```yaml
field: graduate.application_fee_usd
value: 50
source_url: https://www.cmich.edu/graduate/how-to-apply
source_snippet: "Domestic applicants will need to submit a $50 non-refundable application fee along with the application."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: graduate.school_code_fafsa
value: "002243"
source_url: https://www.cmich.edu/graduate/cost-financial-aid
source_snippet: "CMU's school code is 002243."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: graduate.us_resident_per_credit_ms
value: 862
source_url: https://www.cmich.edu/graduate/cost-financial-aid
source_snippet: "U.S. resident tuition*: $862 (MASTER'S/SPECIALIST per credit hour)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: graduate.us_resident_per_credit_doctoral
value: 962
source_url: https://www.cmich.edu/graduate/cost-financial-aid
source_snippet: "U.S. resident tuition*: $962 (DOCTORAL per credit hour)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: graduate.international_per_credit_ms
value: 1062
source_url: https://www.cmich.edu/graduate/cost-financial-aid
source_snippet: "International tuition: $1,062 (Master's)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: graduate.international_per_credit_doctoral
value: 1162
source_url: https://www.cmich.edu/graduate/cost-financial-aid
source_snippet: "International tuition: $1,162 (Doctoral)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### 5.4 Cost of attendance facts

```yaml
field: ug_lower_div_on_campus_coa_usd
value: 32589
source_url: https://www.cmich.edu/offices-departments/office-scholarships-financial-aid/cost-of-attendance
source_snippet: "Total Estimated Cost of Attendance: $32,589"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: ug_upper_div_on_campus_coa_usd
value: 34179
source_url: https://www.cmich.edu/offices-departments/office-scholarships-financial-aid/cost-of-attendance
source_snippet: "Total Estimated Cost of Attendance: $34,179"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: ug_lower_div_off_campus_coa_usd
value: 29231
source_url: https://www.cmich.edu/offices-departments/office-scholarships-financial-aid/cost-of-attendance
source_snippet: "Total Estimated Cost of Attendance: $29,231"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: intl_ug_total_usd
value: 39402
source_url: https://www.cmich.edu/international-admissions/undergraduate/cost-scholarships
source_snippet: "Total: $39,402"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: intl_grad_total_ms_usd
value: 35506
source_url: https://www.cmich.edu/international-admissions/graduate/cost-scholarships
source_snippet: "Total: $35,506 (MASTER'S)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: intl_grad_total_mba_usd
value: 33220
source_url: https://www.cmich.edu/international-admissions/graduate/cost-scholarships
source_snippet: "Total: $33,220 (MBA)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
field: intl_grad_total_doctoral_usd
value: 37306
source_url: https://www.cmich.edu/international-admissions/graduate/cost-scholarships
source_snippet: "Total: $37,306 (DOCTORAL)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### 5.5 Program directory facts

```yaml
field: program_directory.total_count
value: 306
source_url: https://www.cmich.edu/program-finder
source_snippet: "306 search results for ALL PROGRAMS"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: institution.college_count
value: 7
source_url: https://www.cmich.edu/academics/colleges
source_snippet: "Each of our seven academic colleges offer a transformative culture"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: institution.international_students
value: 1726
source_url: https://www.cmich.edu/international-admissions
source_snippet: "1726 International Students at Central Michigan University"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: institution.total_students
value: 14426
source_url: https://www.cmich.edu/international-admissions
source_snippet: "14426 Total number of CMU students"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
field: institution.carnegie_classification
value: "R2 research university"
source_url: https://www.cmich.edu/graduate
source_snippet: "R2 Carnegie research university - We're thrilled to be an R2 Carnegie research university"
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### 6.1 Collection structure

```
collection: central-michigan-university-knowledge-base-v2
├── document: institution-overview
│   └── chunk 1: overview-rules-1-4 (Section 0)
├── document: ug-college-business-administration
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: ug-college-education-and-human-services
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: ug-college-liberal-arts-and-social-sciences
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: ug-college-science-and-engineering
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: ug-college-arts-and-media
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: ug-college-health-professions
│   └── chunk: ug-programs (Section 1, 1.2)
├── document: grad-college-business-administration
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-education-and-human-services
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-liberal-arts-and-social-sciences
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-medicine
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-science-and-engineering
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-arts-and-media
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: grad-college-health-professions
│   └── chunk: grad-programs (Section 2, 2.1)
├── document: ug-application-requirements-deadlines
│   └── chunk: application-info (Section 3)
├── document: graduate-application-requirements-deadlines
│   └── chunk: application-info (Section 3)
├── document: ug-cost-of-attendance
│   └── chunk: cost-info (Section 4.1, 4.2)
├── document: grad-cost-of-attendance
│   └── chunk: cost-info (Section 4.3)
├── document: international-admissions
│   └── chunk: english-proficiency-costs (Section 3.2, 4)
└── document: evidence-chain
    └── chunk: evidence-index (Section 5)
```

### 6.2 Per-chunk metadata template

```yaml
metadata:
  collection: "central-michigan-university-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|MBA|PhD|EdD|DPT|AuD|DHA|MSAT|Cert-UG|Cert-GR>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### 6.3 Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|------------|--------|
| P0 | Per-program requirements (GRE, letters, materials) | Each /program/{slug} page | Programs have specific accordion content; sample 3-5 priority programs only |
| P0 | Tuition rates by program specialty (MBA, MSAT, etc.) | <https://www.cmich.edu/graduate/cost-financial-aid> | Some specialty programs have unique tuition |
| P0 | Per-college department list (full) | <https://www.cmich.edu/academics/colleges/{college}/departments> | Department subdivision was incomplete on some college pages |
| P1 | Graduate assistantship stipend amounts | <https://www.cmich.edu/graduate/cost-financial-aid/graduate-assistant-opportunities> | Stipend amounts vary |
| P1 | Honors Program admission requirements | <https://www.cmich.edu/academics/honors-program> | Separate application track |
| P1 | College of Medicine MD admission details | <https://www.cmich.edu/academics/colleges/college-of-medicine/education/md/admissions> | Distinct from general grad admission |
| P2 | Michigan Achievement Scholarship details | <https://www.cmich.edu/undergraduate/cost-aid-scholarships/scholarships> | State-funded scholarship for MI students |
| P2 | CMU Online specific costs | <https://www.cmich.edu/academics/innovation-online/cmu-online> | Online-only tuition rates may differ |
| P2 | Cross-listed program complete details | Program detail pages | 5 programs cross-listed in 2 colleges each |
| P2 | Academic calendar / term start dates | <https://www.cmich.edu/academics/academic-calendar> | Spring 2027 start, Summer 2027 start |

### 6.4 Total program count reconciliation

| Source | Count |
|--------|-------|
| CMU program-finder ("306 search results") | 306 |
| Unique programs captured (URL × level) | 289 |
| Cross-listed programs (counted in 2 colleges) | 5 |
| Approximate additional from cross-listing | +5 |
| **Reconciled total** | **294** |
| **Remaining gap (likely additional cross-listings or specialty variants)** | **~12** |

The gap of ~12 programs represents minor variations (e.g., a single URL with 2+ level configurations that the program-finder treats as separate entries).

---

## SECTION 7 — Cross-school Comparison Framework (Template)

This section is designed to grow as more universities are added. The following table provides CMU's values plus placeholder columns for future cross-school comparison:

| Dimension | CMU (this run) |
|-----------|----------------|
| Institution type | Public R2 research |
| Location | Mount Pleasant, MI |
| Founded | 1892 |
| Carnegie classification | R2 |
| Total students | 14,426 |
| International students | 1,726 |
| Total UG majors (Rule 1) | 159 |
| Total UG certificates | 39 |
| Total graduate programs | 56 |
| Total doctoral programs | 15 |
| Total graduate certificates | 24 |
| Total program count (Rule 1) | 289 (unique) / 306 (program-finder total) |
| Number of colleges (Rule 2) | 7 |
| UG application fee | $40 |
| UG EA deadline | N/A (rolling) |
| UG priority scholarship deadline | Oct. 15 / Dec. 1 |
| Transfer priority deadline | March 1 (summer/fall), Dec. 1 (spring) |
| SAT/ACT policy | Test-optional |
| SAT code | 1106 |
| ACT code | 1972 |
| TOEFL min (intl UG) | 79 IBT |
| IELTS min (intl UG) | 6.5 |
| Duolingo min (intl UG) | 100 |
| UG COA (in-state, on campus) | $32,589 (lower div) / $34,179 (upper div) |
| UG COA (international) | $39,402 |
| Graduate application fee | $50 |
| Graduate tuition (US, MS) | $862/credit |
| Graduate tuition (Intl, MS) | $1,062/credit |
| Graduate tuition (US, PhD) | $962/credit |
| Graduate tuition (Intl, PhD) | $1,162/credit |
| Need-blind (international) | No |
| Federal FAFSA code | 002243 |
| Average starting salary (CBA) | $62,000 |
| 6-month career outcome rate | 94.9% |

---

## Closing Block

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: cmich.edu (primary), fireup.cmich.edu (application portal)
> **Verification**: ego-browser snapshotText + JS DOM extraction (Vue.js data accessed via `window.programFinderApp`)
> **Granularity**: school → department → degree-level → program
> **Capture tool**: ego-browser (Chromium headless)
> **Knowledge base target**: WeKnora
> **Notes**: CMU's program-finder returns 306 results; this document captures 289 unique programs by (URL × level) with 5 cross-listed programs duplicated. Reconciliation shows ~12-entry gap likely from specialty-level variants.
