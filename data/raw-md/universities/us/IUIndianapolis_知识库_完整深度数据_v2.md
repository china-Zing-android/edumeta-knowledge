# Indiana University Indianapolis Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 134 |
| 本科证书 (Certificate) | 61 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 228 |
| 研究生证书/专家 (Graduate Certificate/PMC/Spec) | 81 |
| **学位项目总计 (UG + Grad)** | **504** |
| 学院 / 独立系所总数 | 16 |

### 0.2 学院 / 系层级结构

Indiana University Indianapolis
├── Herron School of Art and Design [学院]
├── Kelley School of Business [学院]
├── Lilly Family School of Philanthropy [学院]
├── Luddy School of Informatics, Computing, and Engineering [学院]
├── Paul O'Neill School of Public and Environmental Affairs [学院]
├── Richard M. Fairbanks School of Public Health [学院]
├── Robert H. McKinney School of Law [学院]
├── School of Dentistry [学院]
├── School of Education [学院]
├── School of Health & Human Sciences [学院]
├── School of Liberal Arts [学院]
├── School of Medicine [学院]
├── School of Nursing [学院]
├── School of Science [学院]
├── School of Social Work [学院]
└── University College [学院] (exploratory/advising)

> Note: Graduate School Indianapolis is an administrative unit that co-lists graduate programs across all schools. It is not a separate degree-granting college. The Honors College is an academic enrichment unit, not a separate school.

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 91 |
| MS | Master of Science | 研究生 | 69 |
| GCert | Graduate Certificate | 研究生 | 68 |
| UGCert | Undergraduate Certificate | 本科 | 61 |
| PhD | Doctor of Philosophy | 研究生 | 36 |
| BA | Bachelor of Arts | 本科 | 35 |
| Accel | Accelerated Program (UG+Grad) | 研究生 | 33 |
| MA | Master of Arts | 研究生 | 15 |
| MPH | Master of Public Health | 研究生 | 11 |
| MBA | Master of Business Administration | 研究生 | 10 |
| PMC | Post-Master's Graduate Certificate | 研究生 | 9 |
| JD | Juris Doctor | 研究生 | 8 |
| MSW | Master of Social Work | 研究生 | 6 |
| MAT | Master of Arts for Teachers | 研究生 | 5 |
| MD | Doctor of Medicine | 研究生 | 5 |
| DDS | Doctor of Dental Surgery | 研究生 | 4 |
| MLS | Master of Legal Studies | 研究生 | 4 |
| MLIS | Master of Library and Information Science | 研究生 | 4 |
| MPA | Master of Public Affairs | 研究生 | 4 |
| AS | Associate of Science | 本科 | 3 |
| BGS | Bachelor of General Studies | 本科 | 2 |
| MHA | Master of Health Administration | 研究生 | 2 |
| PBC | Post-Baccalaureate Certificate | 研究生 | 2 |
| DND | Doctor of Nutrition & Dietetics | 研究生 | 2 |
| OTD | Doctor of Occupational Therapy | 研究生 | 2 |
| BSW | Bachelor of Social Work | 本科 | 2 |
| BAE | Bachelor of Art Education | 本科 | 1 |
| MDes | Master of Design | 研究生 | 1 |
| DIC | Dietetic Internship Certificate | 研究生 | 1 |
| Spec | Specialist | 研究生 | 1 |
| DrPH | Doctor of Public Health | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPL | Doctor of Philanthropic Leadership | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| MPAS | Master of Physician Assistant Studies | 研究生 | 1 |
| MFA | Master of Fine Arts | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | AS | BS | BA | BAE | BGS | BSW | UGCert | MS | MA | MAT | MBA | MFA | MPH | MSW | MHA | MPA | LLM | MLS | MLIS | MDes | MPAS | PhD | DDS | MD | JD | DNP | DrPH | DND | OTD | DPL | DPT | GCert | PMC | PBC | DIC | Spec | Accel | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Herron School of Art and Design | | 2 | 9 | 1 | | | 2 | 2 | 1 | | | 1 | | | | | | | | 1 | | 3 | | | | | | | | | | 1 | | | | | 1 | **24** |
| Kelley School of Business | | 12 | | | | | 3 | 3 | | | 10 | | | | | | | | | | | | | | | | | | | | | 4 | | | | | | **32** |
| Lilly Family School of Philanthropy | | | 1 | | | | 1 | | 6 | | | | | | | | | | | | | 1 | | | | | | | | 1 | | 3 | | | | | 1 | **14** |
| Luddy School of Informatics, Computing, and Engineering | | 12 | 4 | | | | 16 | 9 | | 1 | | | | | | | | | 4 | | | 3 | | | | | | | | | | 6 | | 2 | | | 20 | **77** |
| Paul O'Neill School of Public and Environmental Affairs | | 7 | | | | | 4 | 3 | | | | | | | | 4 | | | | | | | | | | | | | | | | 17 | | | | | 4 | **39** |
| Richard M. Fairbanks School of Public Health | | 2 | | | | | 2 | 2 | | | | | 11 | | 2 | | | | | | | 2 | | | | | 1 | | | | | 2 | | | | | 2 | **26** |
| Robert H. McKinney School of Law | | | | | | | | | | | | | | | | | 1 | 4 | | | | | | | 8 | | | | | | | 8 | | | | | 3 | **24** |
| School of Dentistry | | 1 | | | | | 1 | 7 | | | | | | | | | | | | | | 1 | 4 | | | | | | | | | 2 | | | | | | **16** |
| School of Education | | 6 | | | | | | 10 | | | | | | | | | | | | | | 2 | | | | | | | | | | 3 | 2 | | | 1 | | **24** |
| School of Health & Human Sciences | | 10 | | | | | 11 | 3 | | | | | | | | | | | | | 1 | 1 | | | | | | 2 | 2 | | 1 | | | | 1 | | | **32** |
| School of Liberal Arts | | 4 | 14 | | 2 | | 12 | | 7 | 3 | | | | | | | | | | | | 2 | | | | | | | | | | 17 | | | | | | **61** |
| School of Medicine | 3 | 9 | | | | | 1 | 6 | | | | | | | | | | | | | | 10 | | 5 | | | | | | | | 2 | | | | | | **36** |
| School of Nursing | | 3 | | | | | | 9 | | | | | | | | | | | | | | 2 | | | | 1 | | | | | | 1 | 7 | | | | | **23** |
| School of Science | | 23 | 6 | | | | 4 | 15 | | 1 | | | | | | | | | | | | 7 | | | | | | | | | | 1 | | | | | 2 | **59** |
| School of Social Work | | | | | | 2 | 4 | | | | | | | 6 | | | | | | | | 1 | | | | | | | | | | 1 | | | | | | **14** |
| University College | | | 1 | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | **1** |
| **合计** | **3** | **91** | **35** | **1** | **2** | **2** | **61** | **69** | **14** | **5** | **10** | **1** | **11** | **6** | **2** | **4** | **1** | **4** | **4** | **1** | **1** | **35** | **4** | **5** | **8** | **1** | **1** | **2** | **2** | **1** | **1** | **68** | **9** | **2** | **1** | **1** | **33** | **502** |

---

## Section 1 — Undergraduate Education

### 1.1 College/School Architecture

IU Indianapolis has 16 degree-granting schools/colleges. See Section 0.2 for the full hierarchy tree. Programs are grouped below by 学院 → 学位级别 → 专业.

### 1.2 Undergraduate Majors — Grouped by 学院 > 学位级别

#### Herron School of Art and Design
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Ceramics | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/ceramics.html |
| 2 | Drawing & Illustration | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/drawing-and-illustration.html |
| 3 | Furniture Design | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/furniture-design.html |
| 4 | Integrative Studio Practice | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/integrative-studio-practice.html |
| 5 | Painting | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/painting.html |
| 6 | Photography | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/photography.html |
| 7 | Printmaking | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/printmaking.html |
| 8 | Sculpture | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/sculpture.html |
| 9 | Visual Communication Design | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/visual-communication-design.html |

##### BAE
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Art Education | Bachelor of Art Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-art-education.html |

##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Music Technology | Bachelor of Science in Music Technology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-music-technology.html |
| 2 | Music Therapy | Bachelor of Science in Music Therapy | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-music-therapy.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Architectural & Interior Design Graphics | Certificate in Architectural and Interior Design Graphics | https://academics.iu.edu/degrees/indianapolis/certificate-in-architectural-and-interior-design-graphics.html |
| 2 | Pre-Art Therapy | Certificate in Pre-Art Therapy | https://academics.iu.edu/degrees/indianapolis/certificate-in-pre-art-therapy.html |

#### Kelley School of Business
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Accounting | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/accounting.html |
| 2 | Business | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business.html |
| 3 | Business of Sports Co-Major | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/business-of-sports-co-major.html |
| 4 | Finance | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/finance.html |
| 5 | Human Resource Management | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/human-resource-management.html |
| 6 | Human Resource Management (TSAP) | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/human-resource-management-tsap.html |
| 7 | International Studies Co-Major | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/international-studies-co-major.html |
| 8 | Management | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/management.html |
| 9 | Management (TSAP) | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/management-tsap.html |
| 10 | Marketing | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/marketing.html |
| 11 | Real Estate Co-Major | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/real-estate-co-major.html |
| 12 | Supply Chain Management | Bachelor of Science in Business | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-business/supply-chain-management.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Business Foundations (100% online) | Certificate in Business Foundations | https://academics.iu.edu/degrees/indianapolis/certificate-in-business-foundations-online.html |
| 2 | Entrepreneurship CRT | Certificate in Entrepreneurship | https://academics.iu.edu/degrees/indianapolis/certificate-in-entrepreneurship/entrepreneurship-crt.html |
| 3 | Real Estate | Certificate in Real Estate | https://academics.iu.edu/degrees/indianapolis/certificate-in-real-estate.html |

#### Lilly Family School of Philanthropy
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Leadership | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/philanthropic-leadership.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Fundraising | Area Certificate in Philanthropic Fundraising | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-philanthropic-fundraising.html |

#### Luddy School of Informatics, Computing, and Engineering
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Artificial Intelligence | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/artificial-intelligence.html |
| 2 | Artificial Intelligence (100% online) | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/artificial-intelligence-online.html |
| 3 | Computer Science | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/computer-science.html |
| 4 | Computer Science (100% online) | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/computer-science-online.html |

##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Artificial Intelligence | Bachelor of Science in Artificial Intelligence | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-artificial-intelligence.html |
| 2 | Artificial Intelligence (100% online) | Bachelor of Science in Artificial Intelligence | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-artificial-intelligence-online.html |
| 3 | Biomedical Informatics | Bachelor of Science in Biomedical Informatics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biomedical-informatics.html |
| 4 | Computer Science | Bachelor of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-computer-science.html |
| 5 | Computer Science (100% online) | Bachelor of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-computer-science-online.html |
| 6 | Computer Science (TSAP) | Bachelor of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-computer-science-tsap.html |
| 7 | Data Science (100% online) | Bachelor of Science in Data Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-data-science-online.html |
| 8 | Health Information Management | Bachelor of Science in Biomedical Informatics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biomedical-informatics/health-information-management.html |
| 9 | Informatics | Bachelor of Science in Informatics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-informatics.html |
| 10 | Informatics (100% online) | Bachelor of Science in Informatics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-informatics-online.html |
| 11 | Informatics (TSAP) | Bachelor of Science in Informatics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-informatics-tsap.html |
| 12 | Media Arts & Science | Bachelor of Science in Media Arts and Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-media-arts-and-science.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Applied Computer Science | Certificate in Applied Computer Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-computer-science.html |
| 2 | Applied Computer Science (100% online) | Certificate in Applied Computer Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-computer-science-online.html |
| 3 | Applied Data Science | Certificate in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-data-science.html |
| 4 | Applied Information Science (100% online) | Certificate in Applied Information Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-information-science-online.html |
| 5 | Artificial Intelligence | Certificate in Artificial Intelligence | https://academics.iu.edu/degrees/indianapolis/certificate-in-artificial-intelligence.html |
| 6 | Artificial Intelligence (100% online) | Certificate in Artificial Intelligence | https://academics.iu.edu/degrees/indianapolis/certificate-in-artificial-intelligence-online.html |
| 7 | Full-Stack Development | Certificate in Full-Stack Development | https://academics.iu.edu/degrees/indianapolis/certificate-in-full-stack-development.html |
| 8 | Full-Stack Development (100% online) | Certificate in Full-Stack Development | https://academics.iu.edu/degrees/indianapolis/certificate-in-full-stack-development-online.html |
| 9 | Human Computer Interaction | Certificate in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-computer-interaction.html |
| 10 | Human Computer Interaction (100% online) | Certificate in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-computer-interaction-online.html |
| 11 | Legal Informatics (100% online) | Certificate in Legal Informatics | https://academics.iu.edu/degrees/indianapolis/certificate-in-legal-informatics-online.html |
| 12 | Medical Coding | Certificate in Medical Coding | https://academics.iu.edu/degrees/indianapolis/certificate-in-medical-coding.html |
| 13 | Medical Coding (100% online) | Certificate in Medical Coding | https://academics.iu.edu/degrees/indianapolis/certificate-in-medical-coding-online.html |
| 14 | Network Security | Certificate in Network Security | https://academics.iu.edu/degrees/indianapolis/certificate-in-network-security.html |
| 15 | Software Bots for Cognitive Automation (100% online) | Certificate in Software Bots for Cognitive Automation | https://academics.iu.edu/degrees/indianapolis/certificate-in-software-bots-for-cognitive-automation-online.html |
| 16 | Virtual Production | Certificate in Virtual Production | https://academics.iu.edu/degrees/indianapolis/certificate-in-virtual-production.html |

#### Paul O'Neill School of Public and Environmental Affairs
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Community & Organizational Leadership Studies | Bachelor of Science in Community and Organizational Leadership Studies | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-community-and-organizational-leadership-studies.html |
| 2 | Community Resilience & Risk Management | Bachelor of Science in Public Affairs | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-public-affairs/community-resilience-and-risk-management.html |
| 3 | Criminal Justice | Bachelor of Science in Criminal Justice | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-criminal-justice.html |
| 4 | Criminal Justice (TSAP) | Bachelor of Science in Criminal Justice | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-criminal-justice-tsap.html |
| 5 | Management & Civic Leadership | Bachelor of Science in Public Affairs | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-public-affairs/management-and-civic-leadership.html |
| 6 | Public Policy | Bachelor of Science in Public Affairs | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-public-affairs/public-policy.html |
| 7 | Sustainability Practice and Policy | Bachelor of Science in Public Affairs | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-public-affairs/sustainability-practice-and-policy.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Intergroup Dialogue | Certificate in Intergroup Dialogue | https://academics.iu.edu/degrees/indianapolis/certificate-in-intergroup-dialogue.html |
| 2 | Nonprofit Management | Certificate in Nonprofit Management | https://academics.iu.edu/degrees/indianapolis/certificate-in-nonprofit-management.html |
| 3 | Public Affairs | Certificate in Public Affairs | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-affairs.html |
| 4 | Public Management | Certificate in Public Management | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-management.html |

#### Richard M. Fairbanks School of Public Health
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Health Administration | Bachelor of Science in Health Administration | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-health-administration.html |
| 2 | Public Health | Bachelor of Science in Public Health | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-public-health.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Community Health | Certificate in Community Health | https://academics.iu.edu/degrees/indianapolis/certificate-in-community-health.html |
| 2 | Health Administration | Certificate in Health Administration | https://academics.iu.edu/degrees/indianapolis/certificate-in-health-administration.html |

#### School of Dentistry
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dental Hygiene | Bachelor of Science in Dental Hygiene | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-dental-hygiene.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dental Assisting | Certificate in Dental Assisting | https://academics.iu.edu/degrees/indianapolis/certificate-in-dental-assisting.html |

#### School of Education
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Early Childhood Education | Bachelor of Science in Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-education/early-childhood-education.html |
| 2 | Early Childhood Education (TSAP) | Bachelor of Science in Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-education/early-childhood-education-tsap.html |
| 3 | Early Childhood Education ADAPT Program (80-99% online) | Bachelor of Science in Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-education/early-childhood-education-adapt-program-hybrid.html |
| 4 | Elementary Education | Bachelor of Science in Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-education/elementary-education.html |
| 5 | Elementary Education (TSAP) | Bachelor of Science in Education | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-education/elementary-education-tsap.html |
| 6 | Elementary Education ADAPT Program (80-99% online) | Bachelor of Science in Psychology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-psychology/elementary-education-adapt-program-hybrid.html |

#### School of Health & Human Sciences
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Applied Fitness and Sports Performance | Bachelor of Science in Kinesiology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-kinesiology/applied-fitness-and-sports-performance.html |
| 2 | Event Management | Bachelor of Science in Tourism, Event and Sport Management | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-tourism-event-and-sport-management/event-management.html |
| 3 | Exercise Science | Bachelor of Science in Kinesiology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-kinesiology/exercise-science.html |
| 4 | Health Sciences | Bachelor of Science in Health Sciences | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-health-sciences.html |
| 5 | Health Sciences (80-99% online) | Bachelor of Science in Health Sciences | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-health-sciences-hybrid.html |
| 6 | Hospitality | Bachelor of Science in Tourism, Event and Sport Management | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-tourism-event-and-sport-management/hospitality.html |
| 7 | Nutrition and Wellness | Bachelor of Science in Kinesiology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-kinesiology/nutrition-and-wellness.html |
| 8 | Physical Education & Health Education Teaching | Bachelor of Science in Kinesiology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-kinesiology/physical-education-and-health-education-teaching.html |
| 9 | Sport Management | Bachelor of Science in Tourism, Event and Sport Management | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-tourism-event-and-sport-management/sport-management.html |
| 10 | Tourism | Bachelor of Science in Tourism, Event and Sport Management | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-tourism-event-and-sport-management/tourism.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Cultural Tourism | Certificate in Cultural Tourism | https://academics.iu.edu/degrees/indianapolis/certificate-in-cultural-tourism.html |
| 2 | Destination Management | Certificate in Destination Management | https://academics.iu.edu/degrees/indianapolis/certificate-in-destination-management.html |
| 3 | Event Management | Certificate in Event Management | https://academics.iu.edu/degrees/indianapolis/certificate-in-event-management.html |
| 4 | Food & Beverage Operations | Certificate in Food and Beverage Operations | https://academics.iu.edu/degrees/indianapolis/certificate-in-food-and-beverage-operations.html |
| 5 | Gerontology Studies (100% online) | Certificate in Gerontology Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-gerontology-studies-online.html |
| 6 | Global Health Rehabilitation Sciences (100% online) | Certificate in Global Health Rehabilitation Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-global-health-rehabilitation-sciences-online.html |
| 7 | Nutrition (100% online) | Certificate in Nutrition | https://academics.iu.edu/degrees/indianapolis/certificate-in-nutrition-online.html |
| 8 | Personal Training | Certificate in Personal Training | https://academics.iu.edu/degrees/indianapolis/certificate-in-personal-training.html |
| 9 | Rehabilitation & Disability Studies (100% online) | Certificate in Rehabilitation and Disability Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-rehabilitation-and-disability-studies.html |
| 10 | Sport Destination Development | Certificate in Sport Destination Development | https://academics.iu.edu/degrees/indianapolis/certificate-in-sport-destination-development.html |
| 11 | Youth Physical Wellness Programs | Certificate in Youth Physical Wellness Programming | https://academics.iu.edu/degrees/indianapolis/certificate-in-youth-physical-wellness-programming/youth-physical-wellness-programs.html |

#### School of Liberal Arts
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Anthropology | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/anthropology.html |
| 2 | Applied Theatre, Film & Television-Communication BA | Bachelor of Arts in Communication | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts-in-communication/applied-theatre-film-and-television-communication-ba.html |
| 3 | Communication Studies-Communication BA | Bachelor of Arts in Communication | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts-in-communication/communication-studies-communication-ba.html |
| 4 | Economics | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/economics.html |
| 5 | English | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/english.html |
| 6 | History | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/history.html |
| 7 | History (100% online) | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/history-online.html |
| 8 | Journalism and Public Relations-Communication BA | Bachelor of Arts in Communication | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts-in-communication/journalism-and-public-relations-communication-ba.html |
| 9 | Law in Liberal Arts | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/law-in-liberal-arts.html |
| 10 | Medical Humanities & Health Studies | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/medical-humanities-and-health-studies.html |
| 11 | Political Science | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/political-science.html |
| 12 | Sociology | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/sociology.html |
| 13 | Sociology (TSAP) | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/sociology-tsap.html |
| 14 | Spanish | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/spanish.html |

##### BGS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | General Studies | Bachelor of General Studies | https://academics.iu.edu/degrees/indianapolis/bachelor-of-general-studies.html |
| 2 | General Studies (100% online) | Bachelor of General Studies | https://academics.iu.edu/degrees/indianapolis/bachelor-of-general-studies-online.html |

##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Digital Media and Storytelling (100% online) | Bachelor of Science in Digital Media and Storytelling | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-digital-media-and-storytelling-online.html |
| 2 | Medical Humanities & Health Studies | Bachelor of Science in Medical Humanities and Health Studies | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-medical-humanities-and-health-studies.html |
| 3 | Quantitative Economics | Bachelor of Science in Quantitative Economics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-quantitative-economics.html |
| 4 | Spanish (100% online) | Bachelor of Science in Spanish | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-spanish-online.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | African Studies | Certificate in African Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-african-studies.html |
| 2 | American Sign Language-English Interpretation | Certificate in American Sign Language/English Interpretation | https://academics.iu.edu/degrees/indianapolis/certificate-in-american-sign-language+english-interpretation/american-sign-language-english-interpretation.html |
| 3 | Chinese Studies | Certificate in Chinese Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-chinese-studies.html |
| 4 | Geographic Information Science | Certificate in Geographic Information Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-geographic-information-science.html |
| 5 | Human Communication in a Mediated World (100% online) | Certificate in Human Communication in a Mediated World | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-communication-in-a-mediated-world-online.html |
| 6 | Intercultural Health | Area Certificate in Intercultural Health | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-intercultural-health.html |
| 7 | Journalism | Certificate in Journalism | https://academics.iu.edu/degrees/indianapolis/certificate-in-journalism.html |
| 8 | Latino Studies | Certificate in Latino Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-latino-studies.html |
| 9 | Museum Studies | Certificate in Museum Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-museum-studies.html |
| 10 | Paralegal Studies | Certificate in Paralegal Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-paralegal-studies.html |
| 11 | Public Relations | Certificate in Public Relations | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-relations.html |
| 12 | Theatre | Certificate in Theatre | https://academics.iu.edu/degrees/indianapolis/certificate-in-theatre.html |

#### School of Medicine
##### AS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Histotechnology (100% online) | Associate of Science in Histotechnology | https://academics.iu.edu/degrees/indianapolis/associate-of-science-in-histotechnology-online.html |
| 2 | Paramedic Science | Associate of Science in Paramedic Science | https://academics.iu.edu/degrees/indianapolis/associate-of-science-in-paramedic-science.html |
| 3 | Radiography | Associate of Science in Radiography | https://academics.iu.edu/degrees/indianapolis/associate-of-science-in-radiography.html |

##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Cytotechnology | Bachelor of Science in Cytotechnology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-cytotechnology.html |
| 2 | Diagnostic Sonography | Bachelor of Science in Diagnostic Sonography | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-diagnostic-sonography.html |
| 3 | Medical Imaging Technology | Bachelor of Science in Medical Imaging Technology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-medical-imaging-technology.html |
| 4 | Medical Imaging Technology (100% online) | Bachelor of Science in Medical Imaging Technology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-medical-imaging-technology-online.html |
| 5 | Medical Laboratory Science | Bachelor of Science in Medical Laboratory Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-medical-laboratory-science.html |
| 6 | Nuclear Medicine Technology | Bachelor of Science in Nuclear Medicine Technology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-nuclear-medicine-technology.html |
| 7 | Nuclear Medicine Technology (80-99% online) | Bachelor of Science in Nuclear Medicine Technology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-nuclear-medicine-technology-hybrid.html |
| 8 | Radiation Therapy | Bachelor of Science in Radiation Therapy | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-radiation-therapy.html |
| 9 | Respiratory Therapy | Bachelor of Science in Respiratory Therapy | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-respiratory-therapy.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Histotechnology (100% online) | Certificate in Histotechnology | https://academics.iu.edu/degrees/indianapolis/certificate-in-histotechnology-online.html |

#### School of Nursing
##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Nursing (RN to BSN) (100% online) | Bachelor of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-nursing/nursing-(rn-to-bsn)-online.html |
| 2 | Nursing (Second Degree Accelerated) | Bachelor of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-nursing/nursing-(second-degree-accelerated).html |
| 3 | Nursing (Traditional BSN) | Bachelor of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-nursing/nursing-(traditional-bsn).html |

#### School of Science
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Biology | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/biology.html |
| 2 | Biology Teaching | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/biology-teaching.html |
| 3 | Chemistry | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/chemistry.html |
| 4 | Chemistry Teaching | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/chemistry-teaching.html |
| 5 | Psychology | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/psychology.html |
| 6 | Psychology (TSAP) | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/psychology-tsap.html |

##### BS
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Actuarial Science | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/actuarial-science.html |
| 2 | Actuarial Science (100% online) | Bachelor of Science in Actuarial Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-actuarial-science-online.html |
| 3 | Applied Mathematics | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/applied-mathematics.html |
| 4 | Applied Statistics | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/applied-statistics.html |
| 5 | Applied Statistics (100% online) | Bachelor of Science in Applied Statistics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-applied-statistics-online.html |
| 6 | Biochemistry | Bachelor of Science in Biochemistry | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biochemistry.html |
| 7 | Biology | Bachelor of Science in Biology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biology.html |
| 8 | Biology (TSAP) | Bachelor of Science in Biology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biology-tsap.html |
| 9 | Biomedical Sciences | Bachelor of Science in Biomedical Sciences | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-biomedical-sciences.html |
| 10 | Chemistry | Bachelor of Science in Chemistry | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-chemistry.html |
| 11 | Chemistry (A.C.S. Certified) | Bachelor of Science in Chemistry | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-chemistry/chemistry-(a.c.s.-certified).html |
| 12 | Chemistry (TSAP) | Bachelor of Science in Chemistry | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-chemistry-tsap.html |
| 13 | Digital Forensics | Bachelor of Science in Digital Forensics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-digital-forensics.html |
| 14 | Environmental Science | Bachelor of Science in Environmental Science | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-environmental-science.html |
| 15 | Forensic & Investigative Sciences | Bachelor of Science in Forensic and Investigative Sciences | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-forensic-and-investigative-sciences.html |
| 16 | Mathematics | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics.html |
| 17 | Mathematics Teaching | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/mathematics-teaching.html |
| 18 | Mathematics Teaching (TSAP) | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/mathematics-teaching-tsap.html |
| 19 | Neuroscience | Bachelor of Science in Neuroscience | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-neuroscience.html |
| 20 | Physics | Bachelor of Science in Physics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-physics.html |
| 21 | Physics Teaching | Bachelor of Science in Physics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-physics/physics-teaching.html |
| 22 | Psychology | Bachelor of Science in Psychology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-psychology.html |
| 23 | Pure Mathematics | Bachelor of Science in Mathematics | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-mathematics/pure-mathematics.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Computational Science-Biology | Certificate in Computational Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-biology.html |
| 2 | Computational Science-Chemistry | Certificate in Computational Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-chemistry.html |
| 3 | Computational Science-Earth & Environmental Science | Certificate in Computational Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-earth-and-environmental-science.html |
| 4 | Computational Science-Physics | Certificate in Computational Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-physics.html |

#### School of Social Work
##### BSW
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Social Work | Bachelor of Social Work | https://academics.iu.edu/degrees/indianapolis/bachelor-of-social-work.html |
| 2 | Social Work (TSAP) | Bachelor of Social Work | https://academics.iu.edu/degrees/indianapolis/bachelor-of-social-work-tsap.html |

##### UGCert
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Child Abuse & Neglect | Certificate in Child Abuse and Neglect | https://academics.iu.edu/degrees/indianapolis/certificate-in-child-abuse-and-neglect.html |
| 2 | Intergroup Dialogue | Certificate in Intergroup Dialogue | https://academics.iu.edu/degrees/indianapolis/certificate-in-intergroup-dialogue.html |
| 3 | Labor Studies (100% online) | Certificate in Labor Studies | https://academics.iu.edu/degrees/indianapolis/certificate-in-labor-studies-online.html |
| 4 | Substance Use Disorders (80-99% online) | Area Certificate in Substance Use Disorders | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-substance-use-disorders-hybrid.html |

#### University College
##### BA
| # | 专业 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Exploratory | Bachelor of Arts | https://academics.iu.edu/degrees/indianapolis/bachelor-of-arts/exploratory.html |

### 1.3 Undergraduate Certificates

| # | Certificate Name | School | URL |
|---|-----------------|--------|-----|
| 1 | Architectural & Interior Design Graphics | Herron School of Art and Design | https://academics.iu.edu/degrees/indianapolis/certificate-in-architectural-and-interior-design-graphics.html |
| 2 | Pre-Art Therapy | Herron School of Art and Design | https://academics.iu.edu/degrees/indianapolis/certificate-in-pre-art-therapy.html |
| 3 | Business Foundations (100% online) | Kelley School of Business | https://academics.iu.edu/degrees/indianapolis/certificate-in-business-foundations-online.html |
| 4 | Entrepreneurship CRT | Kelley School of Business | https://academics.iu.edu/degrees/indianapolis/certificate-in-entrepreneurship/entrepreneurship-crt.html |
| 5 | Real Estate | Kelley School of Business | https://academics.iu.edu/degrees/indianapolis/certificate-in-real-estate.html |
| 6 | Philanthropic Fundraising | Lilly Family School of Philanthropy | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-philanthropic-fundraising.html |
| 7 | Applied Computer Science | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-computer-science.html |
| 8 | Applied Computer Science (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-computer-science-online.html |
| 9 | Applied Data Science | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-data-science.html |
| 10 | Applied Information Science (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-applied-information-science-online.html |
| 11 | Artificial Intelligence | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-artificial-intelligence.html |
| 12 | Artificial Intelligence (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-artificial-intelligence-online.html |
| 13 | Full-Stack Development | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-full-stack-development.html |
| 14 | Full-Stack Development (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-full-stack-development-online.html |
| 15 | Human Computer Interaction | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-computer-interaction.html |
| 16 | Human Computer Interaction (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-computer-interaction-online.html |
| 17 | Legal Informatics (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-legal-informatics-online.html |
| 18 | Medical Coding | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-medical-coding.html |
| 19 | Medical Coding (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-medical-coding-online.html |
| 20 | Network Security | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-network-security.html |
| 21 | Software Bots for Cognitive Automation (100% online) | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-software-bots-for-cognitive-automation-online.html |
| 22 | Virtual Production | Luddy School of Informatics, Computing, and Engineering | https://academics.iu.edu/degrees/indianapolis/certificate-in-virtual-production.html |
| 23 | Intergroup Dialogue | Paul O'Neill School of Public and Environmental Affairs | https://academics.iu.edu/degrees/indianapolis/certificate-in-intergroup-dialogue.html |
| 24 | Nonprofit Management | Paul O'Neill School of Public and Environmental Affairs | https://academics.iu.edu/degrees/indianapolis/certificate-in-nonprofit-management.html |
| 25 | Public Affairs | Paul O'Neill School of Public and Environmental Affairs | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-affairs.html |
| 26 | Public Management | Paul O'Neill School of Public and Environmental Affairs | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-management.html |
| 27 | Community Health | Richard M. Fairbanks School of Public Health | https://academics.iu.edu/degrees/indianapolis/certificate-in-community-health.html |
| 28 | Health Administration | Richard M. Fairbanks School of Public Health | https://academics.iu.edu/degrees/indianapolis/certificate-in-health-administration.html |
| 29 | Dental Assisting | School of Dentistry | https://academics.iu.edu/degrees/indianapolis/certificate-in-dental-assisting.html |
| 30 | Cultural Tourism | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-cultural-tourism.html |
| 31 | Destination Management | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-destination-management.html |
| 32 | Event Management | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-event-management.html |
| 33 | Food & Beverage Operations | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-food-and-beverage-operations.html |
| 34 | Gerontology Studies (100% online) | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-gerontology-studies-online.html |
| 35 | Global Health Rehabilitation Sciences (100% online) | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-global-health-rehabilitation-sciences-online.html |
| 36 | Nutrition (100% online) | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-nutrition-online.html |
| 37 | Personal Training | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-personal-training.html |
| 38 | Rehabilitation & Disability Studies (100% online) | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-rehabilitation-and-disability-studies.html |
| 39 | Sport Destination Development | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-sport-destination-development.html |
| 40 | Youth Physical Wellness Programs | School of Health & Human Sciences | https://academics.iu.edu/degrees/indianapolis/certificate-in-youth-physical-wellness-programming/youth-physical-wellness-programs.html |
| 41 | African Studies | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-african-studies.html |
| 42 | American Sign Language-English Interpretation | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-american-sign-language+english-interpretation/american-sign-language-english-interpretation.html |
| 43 | Chinese Studies | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-chinese-studies.html |
| 44 | Geographic Information Science | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-geographic-information-science.html |
| 45 | Human Communication in a Mediated World (100% online) | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-human-communication-in-a-mediated-world-online.html |
| 46 | Intercultural Health | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-intercultural-health.html |
| 47 | Journalism | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-journalism.html |
| 48 | Latino Studies | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-latino-studies.html |
| 49 | Museum Studies | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-museum-studies.html |
| 50 | Paralegal Studies | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-paralegal-studies.html |
| 51 | Public Relations | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-public-relations.html |
| 52 | Theatre | School of Liberal Arts | https://academics.iu.edu/degrees/indianapolis/certificate-in-theatre.html |
| 53 | Histotechnology (100% online) | School of Medicine | https://academics.iu.edu/degrees/indianapolis/certificate-in-histotechnology-online.html |
| 54 | Computational Science-Biology | School of Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-biology.html |
| 55 | Computational Science-Chemistry | School of Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-chemistry.html |
| 56 | Computational Science-Earth & Environmental Science | School of Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-earth-and-environmental-science.html |
| 57 | Computational Science-Physics | School of Science | https://academics.iu.edu/degrees/indianapolis/certificate-in-computational-science/computational-science-physics.html |
| 58 | Child Abuse & Neglect | School of Social Work | https://academics.iu.edu/degrees/indianapolis/certificate-in-child-abuse-and-neglect.html |
| 59 | Intergroup Dialogue | School of Social Work | https://academics.iu.edu/degrees/indianapolis/certificate-in-intergroup-dialogue.html |
| 60 | Labor Studies (100% online) | School of Social Work | https://academics.iu.edu/degrees/indianapolis/certificate-in-labor-studies-online.html |
| 61 | Substance Use Disorders (80-99% online) | School of Social Work | https://academics.iu.edu/degrees/indianapolis/area-certificate-in-substance-use-disorders-hybrid.html |

---

## Section 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### Herron School of Art and Design
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Music Technology | Master of Science in Music Technology | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-music-technology-accelerated.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Design Thinking (100% online) | Graduate Certificate in Design Thinking | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-design-thinking-online.html |

##### MA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Art Therapy | Master of Arts in Art Therapy | https://academics.iu.edu/degrees/indianapolis/master-of-arts-in-art-therapy.html |

##### MDes
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Design | Master of Design | https://academics.iu.edu/degrees/indianapolis/master-of-design.html |

##### MFA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Visual Art | Master of Fine Arts | https://academics.iu.edu/degrees/indianapolis/master-of-fine-arts/visual-art.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Music Technology | Master of Science in Music Technology | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-music-technology.html |
| 2 | Music Technology (100% online) | Master of Science in Music Technology | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-music-technology-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Music Technology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/music-technology.html |
| 2 | Music Therapy | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/music-therapy.html |
| 3 | Music Therapy (100% online) | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/music-therapy-online.html |

#### Kelley School of Business
##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Accounting | Graduate Certificate in Accounting | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-accounting.html |
| 2 | Internal Auditing | Graduate Certificate in Internal Auditing | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-internal-auditing.html |
| 3 | Medical Management Grad Cert-Occupational Therapy OTD Dual Degree (100% online) | Graduate Certificate in Medical Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-medical-management/medical-management-grad-cert-occupational-therapy-otd-dual-degree-online.html |
| 4 | Tax | Graduate Certificate in Tax | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-tax.html |

##### MBA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Business | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration.html |
| 2 | Entrepreneurship | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/entrepreneurship.html |
| 3 | Finance | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/finance.html |
| 4 | MBA-Accounting MSA Dual Degree | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/mba-accounting-msa-dual-degree.html |
| 5 | MBA-Dental Surgery DDS Dual Degree | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/mba-dental-surgery-dds-dual-degree.html |
| 6 | MBA-Law JD Dual Degree | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/mba-law-jd-dual-degree.html |
| 7 | MBA-Medicine MD Dual Degree | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/mba-medicine-md-dual-degree.html |
| 8 | Marketing | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/marketing.html |
| 9 | Physican MBA | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/physican-mba.html |
| 10 | Supply Chain Management | Master of Business Administration | https://academics.iu.edu/degrees/indianapolis/master-of-business-administration/supply-chain-management.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Accounting | Master of Science in Accounting | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-accounting.html |
| 2 | Accounting MSA-MBA Dual Degree | Master of Science in Accounting | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-accounting/accounting-msa-mba-dual-degree.html |
| 3 | Business of Biotechnology | Master of Science in the Business of Biotechnology | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-the-business-of-biotechnology.html |

#### Lilly Family School of Philanthropy
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Studies BA/MA | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts-accelerated/philanthropic-studies-ba+ma.html |

##### DPL
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Leadership (PhilD) (100% online) | Doctor of Philanthropic Leadership | https://academics.iu.edu/degrees/indianapolis/doctor-of-philanthropic-leadership/philanthropic-leadership-(phild)-online.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Fundraising (100% online) | Graduate Certificate in Philanthropic Fundraising | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-philanthropic-fundraising-online.html |
| 2 | Philanthropic Studies | Graduate Certificate in Philanthropic Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-philanthropic-studies.html |
| 3 | Philanthropic Studies (100% online) | Graduate Certificate in Philanthropic Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-philanthropic-studies-online.html |

##### MA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Studies | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies.html |
| 2 | Philanthropic Studies (100% online) | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies-online.html |
| 3 | Philanthropic Studies MA-Law JD Dual Degree | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies-ma-law-jd-dual-degree.html |
| 4 | Philanthropic Studies MA-Legal Studies MLS Dual Degree | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies-ma-legal-studies-mls-dual-degree.html |
| 5 | Philanthropic Studies MA-Library & Information Science MLIS Dual Degree | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies-ma-library-and-information-science-mlis-dual-degree.html |
| 6 | Philanthropic Studies MA-Master of Public Affairs MPA Dual Degree | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/philanthropic-studies-ma-master-of-public-affairs-mpa-dual-degree.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Philanthropic Studies | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/philanthropic-studies.html |

#### Luddy School of Informatics, Computing, and Engineering
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Artificial Intelligence BA/Applied Data Science MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/artificial-intelligence-ba+applied-data-science-ms.html |
| 2 | Artificial Intelligence BS/Computer Science MS | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science-accelerated/artificial-intelligence-bs+computer-science-ms.html |
| 3 | Artificial Intelligence BS/Computer Science MS (100% online) | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science-accelerated/artificial-intelligence-bs+computer-science-ms-online.html |
| 4 | Biology BS/Bioinformatics MS | Master of Science in Bioinformatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-bioinformatics-accelerated/biology-bs+bioinformatics-ms.html |
| 5 | Biomedical Informatics BS/Bioinformatics MS | Master of Science in Bioinformatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-bioinformatics-accelerated/biomedical-informatics-bs+bioinformatics-ms.html |
| 6 | Biomedical Informatics BS/Health Informatics MS | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics-accelerated/biomedical-informatics-bs+health-informatics-ms.html |
| 7 | Computer Science BS/MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/computer-science-bs+ms.html |
| 8 | Computer Science BS/MS | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science-accelerated/computer-science-bs+ms.html |
| 9 | Computer Science BS/MS (100% online) | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science-accelerated/computer-science-bs+ms-online.html |
| 10 | Data Science BS/Applied Data Science MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/data-science-bs+applied-data-science-ms.html |
| 11 | Health Sciences BS/Health Informatics MS (100% online) | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics-accelerated/health-sciences-bs+health-informatics-ms-online.html |
| 12 | Informatics BS/Applied Data Science MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/informatics-bs+applied-data-science-ms.html |
| 13 | Informatics BS/Bioinformatics MS | Master of Science in Bioinformatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-bioinformatics-accelerated/informatics-bs+bioinformatics-ms.html |
| 14 | Informatics BS/Health Informatics MS | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics-accelerated/informatics-bs+health-informatics-ms.html |
| 15 | Informatics BS/Human Computer Interaction MS | Master of Science in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-human-computer-interaction-accelerated/informatics-bs+human-computer-interaction-ms.html |
| 16 | Mathematics BS/Applied Data Science MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/mathematics-bs+applied-data-science-ms.html |
| 17 | Media Arts & Science BS/Human Computer Interaction MS | Master of Science in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-human-computer-interaction-accelerated/media-arts-and-science-bs+human-computer-interaction-ms.html |
| 18 | Media Arts & Science BS/Library & Information Science MLIS (100% online) | Master of Library and Information Science | https://academics.iu.edu/degrees/indianapolis/master-of-library-and-information-science-accelerated/media-arts-and-science-bs+library-and-information-science-mlis-online.html |
| 19 | Nursing BSN/Health Informatics MS | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics-accelerated/nursing-bsn+health-informatics-ms.html |
| 20 | Sport Management BS/Applied Data Science MS | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science-accelerated/sport-management-bs+applied-data-science-ms.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Archives Management (100% online) | Graduate Certificate in Archives Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-archives-management-online.html |
| 2 | Clinical Informatics (100% online) | Graduate Certificate in Clinical Informatics | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-clinical-informatics-online.html |
| 3 | Computer Science (100% online) | Graduate Certificate in Computer Science | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-computer-science-online.html |
| 4 | Human Computer Interaction | Graduate Certificate in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-human-computer-interaction.html |
| 5 | Human Computer Interaction (100% online) | Graduate Certificate in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-human-computer-interaction-online.html |
| 6 | School Librarianship (100% online) | Graduate Certificate in School Librarianship | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-school-librarianship-online.html |

##### MAT
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Computer Science (100% online) | Master of Arts for Teachers | https://academics.iu.edu/degrees/indianapolis/master-of-arts-for-teachers/computer-science-online.html |

##### MLIS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Library & Info Science (100% online) | Master of Library and Information Science | https://academics.iu.edu/degrees/indianapolis/master-of-library-and-information-science/library-and-info-science-online.html |
| 2 | MLIS-History MA Dual Degree | Master of Library and Information Science | https://academics.iu.edu/degrees/indianapolis/master-of-library-and-information-science/mlis-history-ma-dual-degree.html |
| 3 | MLIS-Law JD Dual Degree | Master of Library and Information Science | https://academics.iu.edu/degrees/indianapolis/master-of-library-and-information-science/mlis-law-jd-dual-degree.html |
| 4 | MLIS-Philanthropic Studies MA Dual Degree | Master of Library and Information Science | https://academics.iu.edu/degrees/indianapolis/master-of-library-and-information-science/mlis-philanthropic-studies-ma-dual-degree.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Applied Data Science | Master of Science in Applied Data Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-applied-data-science.html |
| 2 | Bioinformatics | Master of Science in Bioinformatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-bioinformatics.html |
| 3 | Biomedical Engineering | Master of Science in Biomedical Engineering | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-biomedical-engineering.html |
| 4 | Computer Science | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science.html |
| 5 | Computer Science (100% online) | Master of Science in Computer Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-computer-science-online.html |
| 6 | Health Informatics | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics.html |
| 7 | Health Informatics (100% online) | Master of Science in Health Informatics | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-health-informatics-online.html |
| 8 | Human Computer Interaction | Master of Science in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-human-computer-interaction.html |
| 9 | Human Computer Interaction (100% online) | Master of Science in Human Computer Interaction | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-human-computer-interaction-online.html |

##### PBC
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Health Information Management | Post-Baccalaureate Certificate in Health Information Management | https://academics.iu.edu/degrees/indianapolis/post-baccalaureate-certificate-in-health-information-management.html |
| 2 | Health Information Management (100% online) | Post-Baccalaureate Certificate in Health Information Management | https://academics.iu.edu/degrees/indianapolis/post-baccalaureate-certificate-in-health-information-management-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Computer Science | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/computer-science.html |
| 2 | Data Science | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/data-science.html |
| 3 | Informatics | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/informatics.html |

#### Paul O'Neill School of Public and Environmental Affairs
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Criminal Justice BSCJ/Criminal Justice & Public Safety MS | Master of Science in Criminal Justice and Public Safety | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-criminal-justice-and-public-safety-accelerated/criminal-justice-bscj+criminal-justice-and-public-safety-ms.html |
| 2 | Criminal Justice BSCJ/Public Affairs MPA | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs-accelerated/criminal-justice-bscj+public-affairs-mpa.html |
| 3 | Political Science BA/Public Affairs MPA | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs-accelerated/political-science-ba+public-affairs-mpa.html |
| 4 | Public Affairs BSPA/Public Affairs MPA | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs-accelerated/public-affairs-bspa+public-affairs-mpa.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Analytics in Public Affairs | Graduate Certificate in Analytics in Public Affairs | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-analytics-in-public-affairs.html |
| 2 | Criminal Justice Leadership and Management (100% online) | Graduate Certificate in Criminal Justice Leadership and Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-criminal-justice-leadership-and-management-online.html |
| 3 | Disaster Health Management | Graduate Certificate in Disaster Health Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-disaster-health-management.html |
| 4 | Environmental Policy and Sustainability | Graduate Certificate in Environmental Policy and Sustainability | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-environmental-policy-and-sustainability.html |
| 5 | Homeland Security & Emergency Management | Graduate Certificate in Homeland Security and Emergency Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-homeland-security-and-emergency-management.html |
| 6 | Homeland Security & Emergency Management (100% online) | Graduate Certificate in Homeland Security and Emergency Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-homeland-security-and-emergency-management.html |
| 7 | Innovation & Social Change | Graduate Certificate in Innovation and Social Change | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-innovation-and-social-change.html |
| 8 | Nonprofit Management | Graduate Certificate in Nonprofit Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-nonprofit-management.html |
| 9 | Nonprofit Management (100% online) | Graduate Certificate in Nonprofit Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-nonprofit-management-online.html |
| 10 | Policy Analysis | Graduate Certificate in Policy Analysis | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-policy-analysis.html |
| 11 | Professional Project Management and Leadership | Graduate Certificate in Professional Project Management and Leadership | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-professional-project-management-and-leadership.html |
| 12 | Public Finance | Graduate Certificate in Public Finance | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-public-finance.html |
| 13 | Public Management | Graduate Certificate in Public Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-public-management.html |
| 14 | Public Management (100% online) | Graduate Certificate in Public Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-public-management-online.html |
| 15 | Public Management (Exec Ed) | Graduate Certificate in Public Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-public-management/public-management-(exec-ed).html |
| 16 | Strategic Human Resource Management | Graduate Certificate in Strategic Human Resource Management | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-strategic-human-resource-management.html |
| 17 | Urban & Regional Governance | Graduate Certificate in Urban and Regional Governance | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-urban-and-regional-governance.html |

##### MPA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | MPA-Law JD Dual Degree | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs/mpa-law-jd-dual-degree.html |
| 2 | MPA-Master of Library & Information Science MLIS Dual Degree | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs/mpa-master-of-library-and-information-science-mlis-dual-degree.html |
| 3 | MPA-Philanthropic Studies MA Dual Degree | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs/mpa-philanthropic-studies-ma-dual-degree.html |
| 4 | Public Affairs | Master of Public Affairs | https://academics.iu.edu/degrees/indianapolis/master-of-public-affairs.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Criminal Justice & Public Safety | Master of Science in Criminal Justice and Public Safety | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-criminal-justice-and-public-safety.html |
| 2 | Criminal Justice & Public Safety (100% online) | Master of Science in Criminal Justice and Public Safety | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-criminal-justice-and-public-safety.html |
| 3 | Leadership & Organizational Systems | Master of Science in Leadership and Organizational Systems | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-leadership-and-organizational-systems.html |

#### Richard M. Fairbanks School of Public Health
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Health Administration BS/Health Administration MHA | Master of Health Administration | https://academics.iu.edu/degrees/indianapolis/master-of-health-administration-accelerated/health-administration-bs+health-administration-mha.html |
| 2 | Public Health BSPH/Interdisciplinary Health Studies MPH | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health-accelerated/public-health-bsph+interdisciplinary-health-studies-mph.html |

##### DrPH
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Global Health Leadership (80-99% online) | Doctor of Public Health | https://academics.iu.edu/degrees/indianapolis/doctor-of-public-health/global-health-leadership-hybrid.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Infection Control and Prevention Epidemiology (100% online) | Graduate Certificate in Infection Control and Prevention Epidemiology | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-infection-control-and-prevention-epidemiology-online.html |
| 2 | Public Health (100% online) | Graduate Certificate in Public Health | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-public-health-online.html |

##### MHA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Health Administration | Master of Health Administration | https://academics.iu.edu/degrees/indianapolis/master-of-health-administration.html |
| 2 | MHA-Law JD Dual Degree | Master of Health Administration | https://academics.iu.edu/degrees/indianapolis/master-of-health-administration/mha-law-jd-dual-degree.html |

##### MPH
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Epidemiology | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/epidemiology.html |
| 2 | Health Policy & Management | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/health-policy-and-management.html |
| 3 | Interdisciplinary Public Health Studies | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/interdisciplinary-public-health-studies.html |
| 4 | Interdisciplinary Public Health Studies (100% online) | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/interdisciplinary-public-health-studies-online.html |
| 5 | MPH-Dental Surgery DDS Dual Degree | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/mph-dental-surgery-dds-dual-degree.html |
| 6 | MPH-Law JD Dual Degree | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/mph-law-jd-dual-degree.html |
| 7 | MPH-Medicine MD Dual Degree | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/mph-medicine-md-dual-degree.html |
| 8 | MPH-Social Work MSW Dual Degree | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/mph-social-work-msw-dual-degree.html |
| 9 | Public Health Informatics | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/public-health-informatics.html |
| 10 | Public Health Informatics (100% online) | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/public-health-informatics-online.html |
| 11 | Social & Behavioral Science | Master of Public Health | https://academics.iu.edu/degrees/indianapolis/master-of-public-health/social-and-behavioral-science.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Biostatistics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/biostatistics.html |
| 2 | Global Health and Sustainable Development (100% online) | Master of Science in Global Health and Sustainable Development | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-global-health-and-sustainable-development-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Biostatistics | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/biostatistics.html |
| 2 | Population Health Science | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/population-health-science.html |

#### Robert H. McKinney School of Law
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Informatics BS/Legal Studies MLS | Bachelor of Science in Psychology | https://academics.iu.edu/degrees/indianapolis/bachelor-of-science-in-psychology-accelerated/informatics-bs+legal-studies-mls.html |
| 2 | Law in Liberal Arts BA/Law MJ | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence-accelerated/law-in-liberal-arts-ba+law-mj.html |
| 3 | Sport Management BSTESM/Legal Studies MLS | Master of Legal Studies | https://academics.iu.edu/degrees/indianapolis/master-of-legal-studies-accelerated/sport-management-bstesm+legal-studies-mls.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Advocacy Skills | Graduate Certificate in Advocacy Skills | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-advocacy-skills.html |
| 2 | Civil & Human Rights | Graduate Certificate in Civil and Human Rights | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-civil-and-human-rights.html |
| 3 | Corporate & Commercial Law | Graduate Certificate in Corporate and Commercial Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-corporate-and-commercial-law.html |
| 4 | Criminal Law | Graduate Certificate in Criminal Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-criminal-law.html |
| 5 | Environmental & Natural Resources Law | Graduate Certificate in Environmental and Natural Resources Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-environmental-and-natural-resources-law.html |
| 6 | Health Law | Graduate Certificate in Health Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-health-law.html |
| 7 | Intellectual Property Law | Graduate Certificate in Intellectual Property Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-intellectual-property-law.html |
| 8 | International & Comparative Law | Graduate Certificate in International and Comparative Law | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-international-and-comparative-law.html |

##### JD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | JD-Business MBA Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-business-mba-dual-degree.html |
| 2 | JD-Library & Information Science MLIS Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-library-and-information-science-mlis-dual-degree.html |
| 3 | JD-Master of Health Administration MHA Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-master-of-health-administration-mha-dual-degree.html |
| 4 | JD-Master of Public Affairs MPA Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-master-of-public-affairs-mpa-dual-degree.html |
| 5 | JD-Master of Public Health MPH Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-master-of-public-health-mph-dual-degree.html |
| 6 | JD-Master of Social Work MSW Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-master-of-social-work-msw-dual-degree.html |
| 7 | JD-Medicine MD Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-medicine-md-dual-degree.html |
| 8 | JD-Philanthropic Studies MA Dual Degree | Doctor of Jurisprudence | https://academics.iu.edu/degrees/indianapolis/doctor-of-jurisprudence/jd-philanthropic-studies-ma-dual-degree.html |

##### LLM
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Law (LLM) | Master of Laws | https://academics.iu.edu/degrees/indianapolis/master-of-laws/law-(llm).html |

##### MLS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Legal Studies MLS | Master of Legal Studies | https://academics.iu.edu/degrees/indianapolis/master-of-legal-studies/legal-studies-mls.html |
| 2 | Legal Studies MLS (100% online) | Master of Legal Studies | https://academics.iu.edu/degrees/indianapolis/master-of-legal-studies/legal-studies-mls-online.html |
| 3 | Legal Studies MLS-Philanthropic Studies MA Dual Degree | Master of Legal Studies | https://academics.iu.edu/degrees/indianapolis/master-of-legal-studies/legal-studies-mls-philanthropic-studies-ma-dual-degree.html |
| 4 | Legal Studies MLS-Urban Ed Studies PhD Dual Degree | Master of Legal Studies | https://academics.iu.edu/degrees/indianapolis/master-of-legal-studies/legal-studies-mls-urban-ed-studies-phd-dual-degree.html |

#### School of Dentistry
##### DDS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | DDS-Business MBA Dual Degree | Doctor of Dental Surgery | https://academics.iu.edu/degrees/indianapolis/doctor-of-dental-surgery/dds-business-mba-dual-degree.html |
| 2 | DDS-Master of Public Health MPH Dual Degree | Doctor of Dental Surgery | https://academics.iu.edu/degrees/indianapolis/doctor-of-dental-surgery/dds-master-of-public-health-mph-dual-degree.html |
| 3 | Dental Surgery (DDS) | Doctor of Dental Surgery | https://academics.iu.edu/degrees/indianapolis/doctor-of-dental-surgery/dental-surgery-(dds).html |
| 4 | International Dentist Program (IU-IDP) | Doctor of Dental Surgery | https://academics.iu.edu/degrees/indianapolis/doctor-of-dental-surgery/international-dentist-program-(iu-idp).html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dental Informatics (80-99% online) | Graduate Certificate in Dental Informatics | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-dental-informatics-hybrid.html |
| 2 | Oral & Maxillofacial Surgery (Residency) | Graduate Certificate in Oral and Maxillofacial Surgery | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-oral-and-maxillofacial-surgery/oral-and-maxillofacial-surgery-(residency).html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dental Materials | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/dental-materials.html |
| 2 | Dental Materials | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/dental-materials.html |
| 3 | Endodontics | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/endodontics.html |
| 4 | Orthodontics | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/orthodontics.html |
| 5 | Pediatric Dentistry | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/pediatric-dentistry.html |
| 6 | Periodontology | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/periodontology.html |
| 7 | Prosthodontics | Master of Science in Dentistry | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-dentistry/prosthodontics.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dental Sciences | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/dental-sciences.html |

#### School of Education
##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Academic Advising (100% online) | Graduate Certificate in Academic Advising | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-academic-advising-online.html |
| 2 | Literacy & Learning | Graduate Certificate in Literacy and Learning | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-literacy-and-learning.html |
| 3 | Teaching English Learners (100% online) | Graduate Certificate in Teaching English Learners | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-teaching-english-learners-online.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Elementary Education | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/elementary-education.html |
| 2 | Language Education | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/language-education.html |
| 3 | Language Education (100% online) | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/language-education-online.html |
| 4 | School Counseling | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/school-counseling.html |
| 5 | School Counseling (100% online) | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/school-counseling-online.html |
| 6 | Science of Reading (100% online) | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/science-of-reading-online.html |
| 7 | Secondary Education | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/secondary-education.html |
| 8 | Teaching, Learning, and Curriculum (100% online) | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/teaching-learning-and-curriculum-online.html |
| 9 | Urban Education Leadership | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/urban-education-leadership.html |
| 10 | Urban Education Leadership (100% online) | Master of Science in Education | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-education/urban-education-leadership-online.html |

##### PMC
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Urban School Leadership | Post-Masters Graduate Certificate in Urban School Leadership | https://academics.iu.edu/degrees/indianapolis/post-masters-graduate-certificate-in-urban-school-leadership.html |
| 2 | Urban School Leadership (100% online) | Post-Masters Graduate Certificate in Urban School Leadership | https://academics.iu.edu/degrees/indianapolis/post-masters-graduate-certificate-in-urban-school-leadership-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Urban Ed Studies PhD-Legal Studies MLS Dual Degree | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/urban-ed-studies-phd-legal-studies-mls-dual-degree.html |
| 2 | Urban Education Studies | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/urban-education-studies.html |

##### Spec
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Educational Leadership (100% online) | Specialist in Education | https://academics.iu.edu/degrees/indianapolis/specialist-in-education/educational-leadership-online.html |

#### School of Health & Human Sciences
##### DIC
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Dietetic Internship | Dietetic Internship Professional Certificate | https://academics.iu.edu/degrees/indianapolis/dietetic-internship-professional-certificate.html |

##### DND
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Nutrition & Dietetics | Doctor of Nutrition & Dietetics | https://academics.iu.edu/degrees/indianapolis/doctor-of-nutrition-and-dietetics.html |
| 2 | Nutrition & Dietetics (Post-Professional) | Doctor of Nutrition & Dietetics | https://academics.iu.edu/degrees/indianapolis/doctor-of-nutrition-and-dietetics/nutrition-and-dietetics-(post-professional).html |

##### DPT
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Physical Therapy | Doctor of Physical Therapy | https://academics.iu.edu/degrees/indianapolis/doctor-of-physical-therapy.html |

##### MPAS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Physician Assistant Studies | Master of Physician Assistant Studies | https://academics.iu.edu/degrees/indianapolis/master-of-physician-assistant-studies.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Human Performance & Rehabilitation Sciences | Master of Science in Human Performance and Rehabilitation Sciences | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-human-performance-and-rehabilitation-sciences.html |
| 2 | Nutrition & Dietetics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/nutrition-and-dietetics.html |
| 3 | Nutrition & Dietetics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/nutrition-and-dietetics.html |

##### OTD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Occupational Therapy | Doctor of Occupational Therapy | https://academics.iu.edu/degrees/indianapolis/doctor-of-occupational-therapy.html |
| 2 | Occupational Therapy (Post-Professional) (100% online) | Doctor of Occupational Therapy | https://academics.iu.edu/degrees/indianapolis/doctor-of-occupational-therapy/occupational-therapy-(post-professional)-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Human Performance & Rehabilitation Sciences | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/human-performance-and-rehabilitation-sciences.html |

#### School of Liberal Arts
##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | American Philosophy | Graduate Certificate in American Philosophy | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-american-philosophy.html |
| 2 | Bioethics | Graduate Certificate in Bioethics | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-bioethics.html |
| 3 | Communication Studies (100% online) | Graduate Certificate in Communication Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-communication-studies-online.html |
| 4 | Composition Studies (100% online) | Graduate Certificate in Composition Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-composition-studies-online.html |
| 5 | Geographic Information Science | Graduate Certificate in Geographic Information Science | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-geographic-information-science.html |
| 6 | German (100% online) | Graduate Certificate in German | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-german-online.html |
| 7 | History (100% online) | Graduate Certificate in History | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-history-online.html |
| 8 | Language and Literature (100% online) | Graduate Certificate in Language and Literature | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-language-and-literature-online.html |
| 9 | Literature (100% online) | Graduate Certificate in Literature | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-literature-online.html |
| 10 | Medical Humanities | Graduate Certificate in Medical Humanities | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-medical-humanities.html |
| 11 | Museum Studies | Graduate Certificate in Museum Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-museum-studies.html |
| 12 | Professional Editing | Graduate Certificate in Professional Editing | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-professional-editing.html |
| 13 | Spanish (100% online) | Graduate Certificate in Spanish | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-spanish-online.html |
| 14 | Teaching English to Speakers of Other Languages | Graduate Certificate in Teaching English to Speakers of Other Languages (TESOL) | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-teaching-english-to-speakers-of-other-languages-(tesol).html |
| 15 | Teaching Literature | Graduate Certificate in Teaching Literature | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-teaching-literature.html |
| 16 | Teaching Writing | Graduate Certificate in Teaching Writing | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-teaching-writing.html |
| 17 | Translation Studies | Graduate Certificate in Translation Studies | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-translation-studies.html |

##### MA
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Applied Anthropology | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/applied-anthropology.html |
| 2 | Applied Communication | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/applied-communication.html |
| 3 | English | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/english.html |
| 4 | English (100% online) | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/english-online.html |
| 5 | History | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/history.html |
| 6 | History (100% online) | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/history-online.html |
| 7 | History MA-Library & Information Science MLIS Dual Degree | Master of Arts | https://academics.iu.edu/degrees/indianapolis/master-of-arts/history-ma-library-and-information-science-mlis-dual-degree.html |

##### MAT
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | French (100% online) | Master of Arts for Teachers | https://academics.iu.edu/degrees/indianapolis/master-of-arts-for-teachers/french-online.html |
| 2 | German (100% online) | Master of Arts for Teachers | https://academics.iu.edu/degrees/indianapolis/master-of-arts-for-teachers/german-online.html |
| 3 | History (100% online) | Master of Arts for Teachers | https://academics.iu.edu/degrees/indianapolis/master-of-arts-for-teachers/history-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | American Studies | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/american-studies.html |
| 2 | Health Communication | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/health-communication.html |

#### School of Medicine
##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Clinical Research | Graduate Certificate in Clinical Research | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-clinical-research.html |
| 2 | Innovation & Implementation Science | Graduate Certificate in Innovation and Implementation Science | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-innovation-and-implementation-science.html |

##### MD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | MD-Business MBA Dual Degree | Doctor of Medicine | https://academics.iu.edu/degrees/indianapolis/doctor-of-medicine/md-business-mba-dual-degree.html |
| 2 | MD-Law JD Dual Degree | Doctor of Medicine | https://academics.iu.edu/degrees/indianapolis/doctor-of-medicine/md-law-jd-dual-degree.html |
| 3 | MD-Master of Public Health MPH Dual Degree | Doctor of Medicine | https://academics.iu.edu/degrees/indianapolis/doctor-of-medicine/md-master-of-public-health-mph-dual-degree.html |
| 4 | Medicine | Doctor of Medicine | https://academics.iu.edu/degrees/indianapolis/doctor-of-medicine.html |
| 5 | Medicine (MD) | Doctor of Medicine | https://academics.iu.edu/degrees/indianapolis/doctor-of-medicine/medicine-(md).html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Anatomy, Cell Biology & Physiology | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/anatomy-cell-biology-and-physiology.html |
| 2 | Anesthesiologist Assistant (MSA) | Master of Science in Anesthesia | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-anesthesia/anesthesiologist-assistant (msa).html |
| 3 | Clinical Research | Master of Science in Clinical Research | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-clinical-research.html |
| 4 | Foundational Biomedical Research | Master of Science in Foundational Biomedical Research | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-foundational-biomedical-research.html |
| 5 | Medical & Molecular Genetics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/medical-and-molecular-genetics.html |
| 6 | Medical Science | Master of Science in Medical Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-medical-science.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Anatomy, Cell Biology & Physiology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/anatomy-cell-biology-and-physiology.html |
| 2 | Biochemistry & Molecular Biology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/biochemistry-and-molecular-biology.html |
| 3 | IU BioMedical Gateway Program | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/iu-biomedical-gateway-program.html |
| 4 | MD/PhD Dual Degree | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/md+phd-dual-degree.html |
| 5 | Medical & Molecular Genetics | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/medical-and-molecular-genetics.html |
| 6 | Medical Neuroscience | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/medical-neuroscience.html |
| 7 | Microbiology & Immunology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/microbiology-and-immunology.html |
| 8 | Musculoskeletal Health | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/musculoskeletal-health.html |
| 9 | Pharmacology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/pharmacology.html |
| 10 | Translational Cancer Biology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/translational-cancer-biology.html |

#### School of Nursing
##### DNP
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Nursing Practice (DNP) (80-99% online) | Doctor of Nursing Practice | https://academics.iu.edu/degrees/indianapolis/doctor-of-nursing-practice/nursing-practice-(dnp)-hybrid.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Teaching in Nursing (100% online) | Graduate Certificate in Teaching in Nursing | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-teaching-in-nursing-online.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/adult-gerontology-acute-care-nurse-practitioner.html |
| 2 | Adult-Gerontology Clinical Nurse Specialist | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/adult-gerontology-clinical-nurse-specialist.html |
| 3 | Adult-Gerontology Primary Care Nurse Practitioner | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/adult-gerontology-primary-care-nurse-practitioner.html |
| 4 | Family Nurse Practitioner | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/family-nurse-practitioner.html |
| 5 | Leadership in Health Systems | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/leadership-in-health-systems.html |
| 6 | Nursing Education (80-99% online) | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/nursing-education-hybrid.html |
| 7 | Pediatric Clinic Nurse Specialist | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/pediatric-clinic-nurse-specialist.html |
| 8 | Pediatric Nurse Practitioner - Primary Care | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/pediatric-nurse-practitioner---primary-care.html |
| 9 | Psychiatric Mental Health Nurse Practitioner Lifespan | Master of Science in Nursing | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-nursing/psychiatric-mental-health-nurse-practitioner-lifespan.html |

##### PMC
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner | Post-Master's Graduate Certificate in Adult Gerontology Acute Care Nurse Practitioner | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-adult-gerontology-acute-care-nurse-practitioner/adult-gerontology-acute-care-nurse-practitioner.html |
| 2 | Adult-Gerontology Clinical Nurse Specialist | Post-Master's Graduate Certificate in Adult Gerontology Clinical Nurse Specialist | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-adult-gerontology-clinical-nurse-specialist/adult-gerontology-clinical-nurse-specialist.html |
| 3 | Adult-Gerontology Primary Care Nurse Practitioner | Post-Master's Graduate Certificate in Adult Gerontology Primary Care Nurse Practitioner | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-adult-gerontology-primary-care-nurse-practitioner/adult-gerontology-primary-care-nurse-practitioner.html |
| 4 | Family Nurse Practitioner | Post-Master's Graduate Certificate in Family Nurse Practitioner | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-family-nurse-practitioner.html |
| 5 | Pediatric Clinical Nurse Specialist | Post-Master's Graduate Certificate in Pediatric Clinical Nurse Specialist | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-pediatric-clinical-nurse-specialist.html |
| 6 | Primary Care Pediatric Nurse Practitioner | Post-Master's Graduate Certificate in Primary Care Pediatric Nurse Practitioner | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-primary-care-pediatric-nurse-practitioner.html |
| 7 | Psychiatric-Mental Health Nurse Practitioner | Post-Master's Graduate Certificate in Psychiatric Mental Health Nurse Practitioner | https://academics.iu.edu/degrees/indianapolis/post-master's-graduate-certificate-in-psychiatric-mental-health-nurse-practitioner/psychiatric-mental-health-nurse-practitioner.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Nursing Science | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/nursing-science.html |
| 2 | Nursing Science (80-99% online) | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/nursing-science-hybrid.html |

#### School of Science
##### Accel
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Actuarial Science BS/MS (100% online) | Master of Science in Actuarial Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-actuarial-science-accelerated/actuarial-science-bs+ms-online.html |
| 2 | Geology BS/MS | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-accelerated/geology-bs+ms.html |

##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Biology (100% online) | Graduate Certificate in Biology | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-biology-online.html |

##### MAT
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Biology (100% online) | Master of Arts for Teachers | https://academics.iu.edu/degrees/indianapolis/master-of-arts-for-teachers/biology-online.html |

##### MS
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Actuarial Science (100% online) | Master of Science in Actuarial Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-actuarial-science-online.html |
| 2 | Addiction Neuroscience Psychology | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/addiction-neuroscience-psychology.html |
| 3 | Applied Mathematics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/applied-mathematics.html |
| 4 | Applied Statistics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/applied-statistics.html |
| 5 | Biology | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/biology.html |
| 6 | Biology (Pre-Professional) | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/biology-(pre-professional).html |
| 7 | Chemistry | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/chemistry.html |
| 8 | Computational Data Science | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/computational-data-science.html |
| 9 | Forensic Science | Master of Science in Forensic Science | https://academics.iu.edu/degrees/indianapolis/master-of-science-in-forensic-science.html |
| 10 | Geology | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/geology.html |
| 11 | Industrial Organization Psychology | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/industrial-organization-psychology.html |
| 12 | Math Education | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/math-education.html |
| 13 | Mathematical Sciences | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/mathematical-sciences.html |
| 14 | Physics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/physics.html |
| 15 | Pure Mathematics | Master of Science | https://academics.iu.edu/degrees/indianapolis/master-of-science/pure-mathematics.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Addiction Neuroscience | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/addiction-neuroscience.html |
| 2 | Applied Earth Sciences | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/applied-earth-sciences.html |
| 3 | Biology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/biology.html |
| 4 | Chemistry & Chemical Biology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/chemistry-and-chemical-biology.html |
| 5 | Clinical Psychology | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/clinical-psychology.html |
| 6 | Mathematical Sciences | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/mathematical-sciences.html |
| 7 | Physics | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/physics.html |

#### School of Social Work
##### GCert
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | e-Social Work (100% online) | Graduate Certificate in e-Social Work Practice | https://academics.iu.edu/degrees/indianapolis/graduate-certificate-in-e-social-work-online-practice.html |

##### MSW
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | MSW-Law JD Dual Degree | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/msw-law-jd-dual-degree.html |
| 2 | MSW-Master of Public Health MPH Dual Degree | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/msw-master-of-public-health-mph-dual-degree.html |
| 3 | Social Work-Advanced Standing | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/social-work-advanced-standing.html |
| 4 | Social Work-Advanced Standing (100% online) | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/social-work-advanced-standing-online.html |
| 5 | Social Work-Regular Standing | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/social-work-regular-standing.html |
| 6 | Social Work-Regular Standing (100% online) | Master of Social Work | https://academics.iu.edu/degrees/indianapolis/master-of-social-work/social-work-regular-standing-online.html |

##### PhD
| # | 项目 | 学位全称 | URL |
|---|------|----------|-----|
| 1 | Social Work | Doctor of Philosophy | https://academics.iu.edu/degrees/indianapolis/doctor-of-philosophy/social-work.html |

### 2.2 Graduate Admissions Model

Graduate admissions at IU Indianapolis is **decentralized**. Each school/department manages its own admissions process, deadlines, and requirements. The IU Graduate School Indianapolis serves as the administrative home for graduate students but does not make admissions decisions. Students apply through the IU Graduate CAS (Centralized Application Service) or school-specific portals.

Application deadlines and dates are determined and managed by the department offering the degree. International students are encouraged to apply early to allow time for visa documents.

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Dimension | Value |
|-----------|-------|
| Application portal | Apply IU (apply.iu.edu) or Common Application |
| Application fee | $65 (domestic); $70 (international) |
| Admission type | Rolling admission |
| Fall priority deadline | July 1 (application closes) |
| Spring priority deadline | December 1 |
| Summer 1 priority deadline | March 15 |
| Summer 2 priority deadline | May 1 |
| Scholarship priority (fall) | February 1 (competitive scholarships) |
| Honors College scholarship priority | November 15 |
| FAFSA priority deadline | April 15 (Indiana state) |
| SAT/ACT policy | **Test-optional** (not required) |
| GPA requirement | Minimum 2.0 (only transcript needed if GPA > 3.0) |
| Superscore policy | N/A (test-optional) |
| Recommendation requirements | Not required for general admission |

### 3.2 Undergraduate English Proficiency Table

IU Indianapolis requires English proficiency for international applicants whose native language is not English.

| Exam | Minimum Score | Recommended |
|------|--------------|-------------|
| TOEFL iBT | 79 (overall) | 85+ |
| IELTS | 6.5 (overall) | 7.0+ |
| Duolingo English Test | 105 | 115+ |
| PTE Academic | 53 | 60+ |
| Cambridge C1/C2 | 176 | 185+ |

> Note: English proficiency requirements may vary by program. Some programs may have higher minimums. Check with individual departments for specific requirements.

### 3.3 Graduate — Global Rules

- **Decentralized admissions**: each school/department manages its own process
- **Application platform**: IU Graduate CAS or school-specific portals
- **Application fee**: $70 (international); varies by program (domestic)
- **GRE/GMAT policy**: varies by program (some required, some optional, some not accepted)
- **English proficiency**: TOEFL 79+ / IELTS 6.5+ / Duolingo 105+ (minimums vary by program)
- **CGS April-15 signatory**: Yes (for funded offers)

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-27 Academic Year)

#### In-State (Living on Campus)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and mandatory fees | $10,760 | Full-time (12-18 credit hours) |
| Housing and Food | $14,006 | On-campus room and board |
| **Total direct costs** | **$24,766** | Billed by university |
| Books and supplies | $1,320 | Estimated |
| Transportation | $378 | Estimated |
| Personal expenses | $2,430 | Estimated |
| **Total estimated COA** | **$28,894** | |

#### Out-of-State (Indiana Partner Tuition States — Living on Campus)

Students from IL, KS, KY, MI, MN, MO, NE, ND, OH, PR, WI qualify for reduced tuition via the Indiana Partners Tuition program.

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and mandatory fees | $15,520 | After MSEP discount |
| Housing and Food | $14,006 | On-campus room and board |
| **Total direct costs** | **$29,526** | Billed by university |
| Books and supplies | $1,320 | Estimated |
| Transportation | $378 | Estimated |
| Personal expenses | $2,430 | Estimated |
| **Total estimated COA** | **$33,654** | |

#### Out-of-State (Non-Indiana Partners — Living on Campus)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition and mandatory fees | $35,566 | Full out-of-state rate |
| Housing and Food | $14,006 | On-campus room and board |
| **Total direct costs** | **$49,572** | Billed by university |
| Books and supplies | $1,320 | Estimated |
| Transportation | $378 | Estimated |
| Personal expenses | $2,430 | Estimated |
| **Total estimated COA** | **$53,700** | |

### 4.2 Undergraduate Financial Aid Policy

- **FAFSA school code**: 001813
- **Scholarship funding available**: $84M+ annually
- **Students receiving financial aid**: 76%
- **Students graduating debt-free**: 48% (undergraduate)
- **56% of students graduate debt-free**
- **Need-aware**: Yes (for all students, including international)
- **Merit scholarships**: Available based on admissions, interests, academic achievements, and financial need
- **Honors College scholarships**: Available for first-year students admitted to the Honors College
- **Indiana Partners Tuition**: Reduced tuition for students from 12 partner states

### 4.3 Graduate Cost & Funding Framework

- **Tuition**: Per credit hour (varies by school and program); some programs have flat-rate tuition
- **Funding types**: Fellowships, Student Academic Appointments (SAAs — teaching/research/graduate assistantships), tuition remission
- **SAAs typically provide**: stipend, health and dental insurance, tuition waivers
- **Additional funding sources**: GradGrants, Handshake, student affairs positions
- **Application fee**: $70 (international); varies by program
- **Fee waivers**: Available for veterans and military-connected students

---

## Section 5 — Evidence Chain Index

#### E-U-001
- **field**: undergraduate.admissions.test_policy
- **value**: Test-optional (SAT/ACT not required)
- **source_url**: https://www.iu.edu/admissions/index.html
- **source_snippet**: "IU is test-optional. SAT/ACT test scores aren't required to apply to IU."
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-002
- **field**: undergraduate.admissions.application_fee
- **value**: $65 domestic / $70 international
- **source_url**: https://indianapolis.iu.edu/admissions/apply/steps-to-apply.html
- **source_snippet**: "There is a $65 nonrefundable application fee... $70 application fee (international)"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-003
- **field**: undergraduate.deadlines.fall_priority
- **value**: July 1 (application closes for fall)
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "July 1: Application closes for fall admission"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-004
- **field**: undergraduate.deadlines.spring_priority
- **value**: December 1
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "December 1: Priority deadline for spring admission"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-005
- **field**: undergraduate.deadlines.scholarship_priority
- **value**: February 1 (competitive scholarships)
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "February 1: Deadline for competitive scholarships"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-006
- **field**: undergraduate.deadlines.honors_scholarship
- **value**: November 15
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "November 15: Priority deadline for separate Honors College Bepko, Presidential, and Plater scholarship application"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-007
- **field**: undergraduate.costs.tuition_instate
- **value**: $10,760
- **source_url**: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/
- **source_snippet**: "Tuition and mandatory fees $10,760"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-008
- **field**: undergraduate.costs.tuition_oos
- **value**: $35,566
- **source_url**: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/
- **source_snippet**: "Tuition and mandatory fees $35,566"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-009
- **field**: undergraduate.costs.tuition_partner
- **value**: $15,520
- **source_url**: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/
- **source_snippet**: "Tuition and mandatory fees (after MSEP is applied) $15,520"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-010
- **field**: undergraduate.costs.total_instate_oncampus
- **value**: $28,894
- **source_url**: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/
- **source_snippet**: "Total $28,894"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-011
- **field**: undergraduate.costs.total_oos_oncampus
- **value**: $53,700
- **source_url**: https://indianapolis.iu.edu/cost-aid/cost-of-attendance/
- **source_snippet**: "Total $53,700"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-012
- **field**: undergraduate.fafsa_code
- **value**: 001813
- **source_url**: https://indianapolis.iu.edu/cost-aid/financial-aid/
- **source_snippet**: "Use school code 001813"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-013
- **field**: undergraduate.scholarships.total_funding
- **value**: $84M+ annually
- **source_url**: https://indianapolis.iu.edu/cost-aid/
- **source_snippet**: "$84M+ Scholarship funding available"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-014
- **field**: undergraduate.aid.recipients
- **value**: 76% of students receive financial aid
- **source_url**: https://indianapolis.iu.edu/cost-aid/
- **source_snippet**: "76% IU Indianapolis students receive financial aid"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-U-015
- **field**: programs.total
- **value**: 504 total programs (195 UG + 309 Grad)
- **source_url**: https://indianapolis.iu.edu/academics/degrees-majors/
- **source_snippet**: "375+ Degrees and certificates (API returns 504 program entries)"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-001
- **field**: graduate.admissions.model
- **value**: Decentralized (per-department)
- **source_url**: https://graduate.indianapolis.iu.edu/admissions/
- **source_snippet**: "admissions are handled by individual departments"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-002
- **field**: graduate.admissions.international_deadline
- **value**: Apply early for visa processing
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "international students coming from outside the US are highly encouraged to apply and submit all required materials as early as possible"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-003
- **field**: graduate.funding.saas
- **value**: Stipend + health/dental insurance + tuition waivers
- **source_url**: https://graduate.indianapolis.iu.edu/admissions/financial-support/
- **source_snippet**: "SAAs... typically provide a stipend, health and dental insurance, and tuition waivers"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-004
- **field**: institutions.type
- **value**: Public (IU system)
- **source_url**: https://indianapolis.iu.edu/
- **source_snippet**: "Indiana University Indianapolis — public research university"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-005
- **field**: institutions.location
- **value**: Indianapolis, Indiana
- **source_url**: https://indianapolis.iu.edu/
- **source_snippet**: "420 University Blvd, Indianapolis, IN 46202"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-006
- **field**: institutions.r1_status
- **value**: R1 research university
- **source_url**: https://indianapolis.iu.edu/
- **source_snippet**: "Indy's premier R1 university"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-007
- **field**: institutions.student_body
- **value**: 135 countries, 49 states
- **source_url**: https://indianapolis.iu.edu/admissions/
- **source_snippet**: "135 Countries and 49 states represented in the student body"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

#### E-G-008
- **field**: undergraduate.admissions.rolling
- **value**: Rolling admission
- **source_url**: https://indianapolis.iu.edu/admissions/apply/dates/
- **source_snippet**: "Rolling admission with priority deadlines"
- **capture_date**: 2026-07-06
- **evidence_type**: official_webpage

---

## Section 6 — WeKnora Import Manifest

### Collection Structure

```
iu-indianapolis-knowledge-base-v2/
├── 00-overview.md (Section 0: counts, hierarchy, degree inventory, distribution matrix)
├── 01-undergraduate-education.md (Section 1: all UG programs by school)
├── 02-graduate-education.md (Section 2: all grad programs by school)
├── 03-admissions-deadlines.md (Section 3: requirements, deadlines, test policy)
├── 04-costs-financial-aid.md (Section 4: COA, aid policy, grad funding)
├── 05-evidence-chain.md (Section 5: all evidence blocks)
└── 06-comparison-framework.md (Section 7: cross-school comparison)
```

### Per-chunk Metadata Template

```yaml
metadata:
  collection: "iu-indianapolis-knowledge-base-v2"
  school: "<home college>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program English proficiency minimums | individual program pages |
| P0 | Graduate program-specific deadlines | individual department pages |
| P1 | GRE/GMAT requirements by program | individual department pages |
| P1 | International student cost of attendance | international.indianapolis.iu.edu |
| P1 | Honors College admission requirements | honors.indianapolis.iu.edu |
| P2 | Net price calculator results | indianapolis.iu.edu/cost-aid/cost-of-attendance/net-price-calculator.html |
| P2 | Transfer credit policy details | indianapolis.iu.edu/admissions/apply/transfer.html |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | IU Indianapolis |
|-----------|-----------------|
| Total programs (Rule 1) | 504 |
| UG degree programs | 134 |
| UG certificates | 61 |
| Grad degree programs | 228 |
| Grad certificates/specialist | 81 |
| Schools/colleges (Rule 2) | 16 |
| In-state tuition/yr | $10,760 |
| OOS tuition/yr | $35,566 |
| In-state total COA (on-campus) | $28,894 |
| OOS total COA (on-campus) | $53,700 |
| Admission type | Rolling |
| Fall application deadline | July 1 (priority) |
| Test policy | Test-optional |
| Need-blind? | Need-aware (all) |
| Application fee (UG domestic) | $65 |
| Application fee (international) | $70 |
| TOEFL minimum | 79 |
| IELTS minimum | 6.5 |
| FAFSA code | 001813 |
| R1 status | Yes |
| Public/Private | Public (IU system) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: indianapolis.iu.edu, www.iu.edu, graduate.indianapolis.iu.edu, international.indianapolis.iu.edu, exdd-academics.webapps.iu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch + API extraction
> **Granularity**: school → degree-level → program