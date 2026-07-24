# University of Roehampton, London — Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/LLB/FdA) | 103 |
| 本科 Top-up / 衔接课程 | 0 |
| 研究生学位项目 (MA/MSc/MBA/MRes/LLM/DTh/PGCE) | 72 |
| **学位项目总计 (UG + Grad)** | **175** |
| 学院 / 独立系所总数 | 6 学院 / 13 系 |

> **Recon**: total (175) == sum of distribution matrix cells == rows in Section 1 + Section 2.

### 0.2 学院 / 系层级结构

```
University of Roehampton, London
├── School of Arts, Humanities and Social Sciences   [学院]
│   ├── Media, Communications and Creative Arts        [系]
│   └── Humanities and Social Sciences                 [系]
├── Faculty of Business and Law                       [学院]
│   ├── Business School                                 [系]
│   └── Law School                                      [系]
├── School of Computing, Engineering and the Built Environment  [学院]
│   ├── Computing                                       [系]
│   └── Sustainable Engineering and Technology          [系]
├── School of Education                                [学院]
│   ├── Education and Early Years                       [系]
│   └── Teacher Training                                [系]
├── School of Life and Health Sciences                 [学院]
│   ├── Health Sciences                                 [系]
│   ├── Sport and Exercise Sciences                     [系]
│   └── Ecology and Biological Sciences                 [系]
└── School of Psychology                               [学院]
    ├── Psychology                                       [系]
    └── Therapy and Counselling                          [系]

Plus:
├── Graduate School                                    [研究学院] — PhD/MPhil by research
└── School of Continuing Education                     [继续教育] — Foundation/Apprenticeship/Pathways
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 34 |
| BSc | Bachelor of Science | 本科 | 78 |
| LLB | Bachelor of Laws | 本科 | 3 |
| FdA | Foundation Degree in Arts | 本科 | 1 |
| MA | Master of Arts | 研究生 | 3 |
| MSc | Master of Science | 研究生 | 43 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MRes | Master of Research | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 2 |
| DTh | Doctor of Practical Theology | 研究生 | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 3 |
| iPGCE | International PGCE | 研究生 | 1 |
| Top-up | Top-up Degree (year-1 entry) | 本科 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \\ 级别 | BA | BSc | LLB | FdA | MA | MSc | MBA | MRes | LLM | PhD | DTh | PGCE | iPGCE | Top-up | 合计 |
|------------|----|-----|-----|-----|-----|-----|-----|------|-----|-----|-----|------|-------|--------|------|
| School of Arts, Humanities and Social Sciences | 23 | 0 | 0 | 0 | 3 | 10 | 0 | 1 | 0 | 0 | 1 | 0 | 0 | 0 | **38** |
| Faculty of Business and Law | 6 | 28 | 3 | 0 | 0 | 5 | 4 | 0 | 2 | 0 | 0 | 0 | 0 | 1 | **49** |
| School of Computing, Engineering and the Built Environment | 0 | 18 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **26** |
| School of Education | 5 | 2 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 3 | 1 | 0 | **14** |
| School of Life and Health Sciences | 0 | 16 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **20** |
| School of Psychology | 0 | 14 | 0 | 0 | 0 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **28** |
| **合计** | **34** | **78** | **3** | **1** | **3** | **43** | **4** | **1** | **2** | **0** | **1** | **3** | **1** | **1** | **175** |

---

## 1. Undergraduate Education

### 1.1 College/School architecture

Roehampton's undergraduate portfolio spans **6 academic schools/faculties**, each offering BA/BSc/LLB/FdA degrees. Top-up programmes are listed alongside their base programme. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### School of Arts, Humanities and Social Sciences
##### Media, Communications and Creative Arts
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance (BA) | https://www.roehampton.ac.uk/study/undergraduate-courses/dance/ |
| 2 | Dance (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/dance-top-up/ |
| 3 | Dance and Fitness (BA) | https://www.roehampton.ac.uk/study/undergraduate-courses/dance-and-fitness/ |
| 4 | Digital Design | https://www.roehampton.ac.uk/study/undergraduate-courses/digital-design/ |
| 5 | English and Journalism | https://www.roehampton.ac.uk/study/undergraduate-courses/english-and-journalism/ |
| 6 | Film Production | https://www.roehampton.ac.uk/study/undergraduate-courses/film-production/ |
| 7 | Games Art | https://www.roehampton.ac.uk/study/undergraduate-courses/games-art/ |
| 8 | Graphic Design | https://www.roehampton.ac.uk/study/undergraduate-courses/graphic-design/ |
| 9 | Journalism | https://www.roehampton.ac.uk/study/undergraduate-courses/journalism/ |
| 10 | Media and Communications | https://www.roehampton.ac.uk/study/undergraduate-courses/media-communications/ |

##### Humanities and Social Sciences
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Biblical Studies and Theology | https://www.roehampton.ac.uk/study/undergraduate-courses/biblical-studies-and-theology/ |
| 2 | Criminology | https://www.roehampton.ac.uk/study/undergraduate-courses/criminology/ |
| 3 | Criminology and Criminal Psychology | https://www.roehampton.ac.uk/study/undergraduate-courses/criminology-and-criminal-psychology/ |
| 4 | Criminology and Policing | https://www.roehampton.ac.uk/study/undergraduate-courses/criminology-and-policing/ |
| 5 | Criminology and Sociology | https://www.roehampton.ac.uk/study/undergraduate-courses/criminology-and-sociology/ |
| 6 | Criminology with Digital Forensics | https://www.roehampton.ac.uk/study/undergraduate-courses/criminology-with-digital-forensics/ |
| 7 | English Literature | https://www.roehampton.ac.uk/study/undergraduate-courses/english-literature/ |
| 8 | History | https://www.roehampton.ac.uk/study/undergraduate-courses/history/ |
| 9 | History and English | https://www.roehampton.ac.uk/study/undergraduate-courses/history-and-english/ |
| 10 | Politics and International Relations | https://www.roehampton.ac.uk/study/undergraduate-courses/politics-and-international-relations/ |
| 11 | Politics, International Relations, and History | https://www.roehampton.ac.uk/study/undergraduate-courses/politics-international-relations-and-history/ |
| 12 | Theology, Mission and Practice | https://www.roehampton.ac.uk/study/undergraduate-courses/theology-mission-and-practice/ |

#### Faculty of Business and Law
##### Business School
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.roehampton.ac.uk/study/undergraduate-courses/accounting/ |
| 2 | Accounting Studies (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/accounting-studies/ |
| 3 | Business Analytics | https://www.roehampton.ac.uk/study/undergraduate-courses/business-analytics/ |
| 4 | Business Management | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/ |
| 5 | Business Management (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-top-up/ |
| 6 | Business Management and Economics | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-economics/ |
| 7 | Business Management and Economics (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-economics-top-up/ |
| 8 | Business Management and Entrepreneurship | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-entrepreneurship/ |
| 9 | Business Management and Entrepreneurship (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-entrepreneurship-top-up/ |
| 10 | Business Management and Finance | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-finance/ |
| 11 | Business Management and Finance (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-finance-top-up/ |
| 12 | Business Management and Marketing | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-marketing/ |
| 13 | Business Management and Marketing (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/business-management-and-marketing-top-up/ |
| 14 | Business and Computing | https://www.roehampton.ac.uk/study/undergraduate-courses/business-and-computing/ |
| 15 | Digital Business Management | https://www.roehampton.ac.uk/study/undergraduate-courses/digital-business-management/ |
| 16 | Digital Marketing | https://www.roehampton.ac.uk/study/undergraduate-courses/digital-marketing/ |
| 17 | Economics | https://www.roehampton.ac.uk/study/undergraduate-courses/economics/ |
| 18 | Finance and Accounting | https://www.roehampton.ac.uk/study/undergraduate-courses/finance-and-accounting/ |
| 19 | Human Resource Management | https://www.roehampton.ac.uk/study/undergraduate-courses/human-resource-management/ |
| 20 | Human Resource Management (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/human-resource-management-top-up/ |
| 21 | International Business | https://www.roehampton.ac.uk/study/undergraduate-courses/international-business/ |
| 22 | International Business (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/international-business-top-up/ |
| 23 | International Business and Finance (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/international-business-and-finance-top-up/ |
| 24 | Marketing (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/marketing-top-up/ |
| 25 | Marketing with Business Analytics | https://www.roehampton.ac.uk/study/undergraduate-courses/marketing-with-business-analytics/ |

##### Law School
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Law | https://www.roehampton.ac.uk/study/undergraduate-courses/business-and-law/ |

###### LLB

| # | 专业 | URL |
|---|------|-----|
| 1 | LLB (Hons) Law | https://www.roehampton.ac.uk/study/undergraduate-courses/law/ |
| 2 | LLB (Hons) Law with Criminal Justice | https://www.roehampton.ac.uk/study/undergraduate-courses/law-with-criminal-justice/ |
| 3 | LLB (Hons) Law with Politics | https://www.roehampton.ac.uk/study/undergraduate-courses/llb-law-with-politics/ |

#### School of Computing, Engineering and the Built Environment
##### Computing
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence & Machine Learning | https://www.roehampton.ac.uk/study/undergraduate-courses/ai-and-machine-learning/ |
| 2 | Computer Science | https://www.roehampton.ac.uk/study/undergraduate-courses/computer-science/ |
| 3 | Computer Science (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/computer-science-top-up/ |
| 4 | Computing and Digital Technologies | https://www.roehampton.ac.uk/study/undergraduate-courses/computing-and-digital-technologies/ |
| 5 | Cyber Security | https://www.roehampton.ac.uk/study/undergraduate-courses/cybersecurity/ |
| 6 | Cyber Security (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/cyber-security-top-up/ |
| 7 | Software Engineering | https://www.roehampton.ac.uk/study/undergraduate-courses/software-engineering/ |
| 8 | Software Engineering (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/software-engineering-top-up/ |

##### Sustainable Engineering and Technology
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://www.roehampton.ac.uk/study/undergraduate-courses/architectural-engineering/ |
| 2 | Architectural Technology | https://www.roehampton.ac.uk/study/undergraduate-courses/architectural-technology/ |
| 3 | Architecture | https://www.roehampton.ac.uk/study/undergraduate-courses/architecture/ |
| 4 | Building Surveying | https://www.roehampton.ac.uk/study/undergraduate-courses/building-surveying/ |
| 5 | Civil Engineering | https://www.roehampton.ac.uk/study/undergraduate-courses/civil-engineering/ |
| 6 | Civil and Environmental Engineering | https://www.roehampton.ac.uk/study/undergraduate-courses/civil-and-environmental-engineering/ |
| 7 | Construction Management | https://www.roehampton.ac.uk/study/undergraduate-courses/construction-management/ |
| 8 | Engineering Management | https://www.roehampton.ac.uk/study/undergraduate-courses/engineering-management/ |
| 9 | Quantity Surveying | https://www.roehampton.ac.uk/study/undergraduate-courses/quantity-surveying/ |

#### School of Education
##### Education and Early Years
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Studies (BA) | https://www.roehampton.ac.uk/study/undergraduate-courses/early-childhood-studies/ |
| 2 | Early Childhood Studies (Top-up) | https://www.roehampton.ac.uk/study/undergraduate-courses/early-childhood-studies-top-up/ |
| 3 | Education | https://www.roehampton.ac.uk/study/undergraduate-courses/education/ |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Speech and Language Therapy | https://www.roehampton.ac.uk/study/undergraduate-courses/speech-and-language-therapy/ |
| 2 | Sport Management | https://www.roehampton.ac.uk/study/undergraduate-courses/sport-management/ |

###### FdA

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Studies (FdA) | https://www.roehampton.ac.uk/study/undergraduate-courses/fda-early-childhood-studies/ |

##### Teacher Training
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Primary Education (QTS) | https://www.roehampton.ac.uk/study/undergraduate-courses/primary-education-qts/ |

#### School of Life and Health Sciences
##### Health Sciences
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Adult Nursing | https://www.roehampton.ac.uk/study/undergraduate-courses/adult-nursing/ |
| 2 | Adult and Mental Health Nursing | https://www.roehampton.ac.uk/study/undergraduate-courses/adult-and-mental-health-nursing/ |
| 3 | Children's Nursing | https://www.roehampton.ac.uk/study/undergraduate-courses/childrens-nursing/ |
| 4 | Health Sciences | https://www.roehampton.ac.uk/study/undergraduate-courses/health-sciences/ |
| 5 | Mental Health Nursing | https://www.roehampton.ac.uk/study/undergraduate-courses/mental-health-nursing/ |
| 6 | Nursing Associate | https://www.roehampton.ac.uk/study/undergraduate-courses/nursing-associate/ |
| 7 | Nutrition and Health | https://www.roehampton.ac.uk/study/undergraduate-courses/nutrition-and-health/ |
| 8 | Occupational Therapy (pre-registration) | https://www.roehampton.ac.uk/study/undergraduate-courses/occupational-therapy/ |
| 9 | Physiotherapy (pre-registration) | https://www.roehampton.ac.uk/study/undergraduate-courses/physiotherapy/ |

##### Sport and Exercise Sciences
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Exercise Sciences | https://www.roehampton.ac.uk/study/undergraduate-courses/sport-and-exercise-sciences/ |
| 2 | Sports Therapy | https://www.roehampton.ac.uk/study/undergraduate-courses/sports-therapy/ |

##### Ecology and Biological Sciences
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.roehampton.ac.uk/study/undergraduate-courses/biological-sciences/ |
| 2 | Biomedical Science | https://www.roehampton.ac.uk/study/undergraduate-courses/biomedical-science/ |
| 3 | Zoology | https://www.roehampton.ac.uk/study/undergraduate-courses/zoology/ |

#### School of Psychology
##### Psychology
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.roehampton.ac.uk/study/undergraduate-courses/neuroscience/ |
| 2 | Psychology | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology/ |
| 3 | Psychology (Clinical and Mental Health) | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-clinical-and-mental-health/ |
| 4 | Psychology (Forensic and Criminal) | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-forensic-and-criminal/ |
| 5 | Psychology (Sport and Health) | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-sport-and-health/ |
| 6 | Psychology and Artificial Intelligence | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-artificial-intelligence/ |
| 7 | Psychology and Business | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-business/ |
| 8 | Psychology and Coaching | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-coaching/ |
| 9 | Psychology and Cognitive Neuroscience | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-cognitive-neuroscience/ |
| 10 | Psychology and Digital Marketing | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-digital-marketing/ |
| 11 | Psychology and Education | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-education/ |
| 12 | Psychology and Human Resource Management | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-human-resource-management/ |
| 13 | Psychology and Sociology | https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-sociology/ |

##### Therapy and Counselling
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Therapeutic Psychology and Counselling | https://www.roehampton.ac.uk/study/undergraduate-courses/therapeutic-psychology-and-counselling/ |


### 1.3 Interdisciplinary / cross-college undergraduate programs

Several Roehampton UG degrees are joint honours / cross-listed between two schools. Examples:

- **Business and Computing** — Business School + Computing (CEBE). URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/business-and-computing/>
- **Business and Law** — Business School + Law School. URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/business-and-law/>
- **English and Journalism** — AHSS. URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/english-and-journalism/>
- **History and English** — AHSS. URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/history-and-english/>
- **Politics, International Relations, and History** — AHSS. URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/politics-international-relations-and-history/>
- **Psychology and Business / Education / Sociology / HRM / Digital Marketing / AI / Coaching / Cognitive Neuroscience** — Psychology + partner school. URLs: <https://www.roehampton.ac.uk/study/undergraduate-courses/psychology-and-business/> etc.
- **Criminology and Sociology / Criminal Psychology / Policing / Digital Forensics** — AHSS + partner. URLs: <https://www.roehampton.ac.uk/study/undergraduate-courses/criminology-and-sociology/> etc.
- **Therapeutic Psychology and Counselling** — Psychology (Therapy & Counselling). URL: <https://www.roehampton.ac.uk/study/undergraduate-courses/therapeutic-psychology-and-counselling/>

### 1.4 Top-up / Foundation / Pathway routes

- **Top-up degrees** (1-year full-time) — listed alongside base programmes in §1.2. Designed for HND/Year-2 holders.
- **Foundation Year option** — most 3-year BSc/BA programmes offer a 4-year 'with Foundation Year' variant. Source: <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/>
- **International Foundation Pathway** — separate International Year 1 / Foundation entry. Source: <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/>
- **Higher Technical Qualifications (HTQs)** — School of Continuing Education. URL: <https://www.roehampton.ac.uk/study/higher-technicals/>
- **Apprenticeships** — School of Continuing Education. URL: <https://www.roehampton.ac.uk/study/apprenticeships/>
- **Foundation Programmes** — URL: <https://www.roehampton.ac.uk/study/academic-areas/continuing-education/foundation-programmes/>
- **International Pathways** — URL: <https://www.roehampton.ac.uk/study/academic-areas/continuing-education/international-pathways/>

### 1.5 General/Institute-wide requirements

- UCAS application via <https://www.ucas.com/> (Roehampton UCAS institution code 'N' — e.g. N190 for BSc Business Management, N121 with Foundation Year).
- Entry tariff varies by programme; sample BSc Business Management: '2026/27 entry: Call 0300 303 8320 to find out if you are eligible for this programme in Clearing'. International Foundation Pathway: 64 UCAS (or equivalent) + IELTS 5.5.
- For full per-programme entry requirements see each course page (linked in §1.2).

### 1.6 UCAS-code quick-lookup (selected)

| Course | UCAS code |
|--------|-----------|
| BSc Business Management | N190 (N121 with Foundation Year) |

> Most Roehampton UG courses use the **N** UCAS institution code. Per-programme codes are listed on each course page (linked in §1.2).

---

## 2. Graduate Education

### 2.1 Graduate (taught) programs — grouped by 学院 > 系 > 学位级别

#### School of Arts, Humanities and Social Sciences
##### Media, Communications and Creative Arts
###### MA

| # | 专业 | URL |
|---|------|-----|
| 1 | AI and Digital Media | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/ai-and-digital-media/ |
| 2 | Creative Writing (MA) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/creative-writing/ |
| 3 | Media and Communications (MA) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/media-and-communications/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Choreography | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/choreography/ |
| 2 | Dance Education | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/dance-education/ |
| 3 | Dance Practice and Performance | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/dance-practice-and-performance/ |
| 4 | Dance and Embodied Practice | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/dance-and-embodied-practice/ |
| 5 | Filmmaking | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/filmmaking/ |
| 6 | International Master in Dance and Movement as Practical Knowledge and Heritage | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/international-master-in-dance-and-movement-as-practical-knowledge-and-heritage/ |

###### MRes

| # | 专业 | URL |
|---|------|-----|
| 1 | Choreography and Performance (MRes) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/choreography-and-performance-mres/ |

##### Humanities and Social Sciences
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/criminology/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Children's Literature (Distance Learning) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/childrens-literature-distance-learning/ |
| 2 | Erasmus Mundus Human Rights Policy and Practice | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/erasmus-mundus-human-rights-policy-and-practice/ |
| 3 | Human Rights | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/human-rights/ |
| 4 | International Relations | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/international-relations/ |

###### DTh

| # | 专业 | URL |
|---|------|-----|
| 1 | Practical Theology (DTh) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/practical-theology-dth/ |

#### Faculty of Business and Law
##### Business School
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Banking and Finance | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/banking-and-finance/ |
| 2 | Global Business ManagementJuly 2026, | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-business-management/ |
| 3 | Global Financial Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-financial-management/ |
| 4 | Global Human Resource Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-human-resources-management/ |
| 5 | Global Logistics and Supply Chain Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-logistics-and-supply-chain-management/ |
| 6 | Global Marketing | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-marketing/ |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/business-analytics/ |
| 2 | Digital Marketing | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/digital-marketing/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | AI for Business | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/ai-for-business/ |
| 2 | Digital Business | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/digital-business/ |
| 3 | International Hospitality Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/international-hospitality-management/ |
| 4 | Occupational and Business Psychology | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/occupational-and-business-psychology/ |
| 5 | Project Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/project-management/ |

###### MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | MBA Healthcare Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba-healthcare-management/ |
| 2 | MBA with Finance | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba-with-finance/ |
| 3 | MBA with Marketing | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba-with-marketing/ |
| 4 | MBAJuly 2026, | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/ |

###### Top-up

| # | 专业 | URL |
|---|------|-----|
| 1 | Global Human Resource Management (Top-up) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/global-human-resources-management-top-up/ |

##### Law School
###### LLM

| # | 专业 | URL |
|---|------|-----|
| 1 | LLM Human Rights and International Law | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/llm-human-rights-and-international-law/ |
| 2 | LLM International Commercial Law | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/llm-international-commercial-law/ |

#### School of Computing, Engineering and the Built Environment
##### Computing
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Cyber Security | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/cyber-security/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/artificial-intelligence/ |
| 2 | Computing | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/computing/ |
| 3 | Cyber Security Technology (Conversion) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/cyber-security-technology-conversion/ |
| 4 | Data Science | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/data-science/ |
| 5 | Data Science Applications (Conversion) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/data-science-applications-conversion/ |

##### Sustainable Engineering and Technology
###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management and Digital Innovation | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/construction-management-and-digital-innovation/ |
| 2 | Construction Project Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/construction-project-management/ |
| 3 | Engineering Project Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/engineering-project-management/ |

#### School of Education
##### Education and Early Years
###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/education/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Education Leadership and Management | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/education-leadership-and-management/ |
| 2 | Music for Children with Special Abilities and Needs: Sounds of Intent | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/music-and-children-with-special-abilities-and-needs-sounds-of-intent/ |

##### Teacher Training
###### PGCE

| # | 专业 | URL |
|---|------|-----|
| 1 | PGCE Lead Partner Route - Primary and Secondary | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/lead-partner/ |
| 2 | PGCE Primary | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/pgce-primary/ |
| 3 | PGCE Secondary | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/pgce-secondary/ |

###### iPGCE

| # | 专业 | URL |
|---|------|-----|
| 1 | iPGCE | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/international-postgraduate-certificate-in-education/ |

#### School of Life and Health Sciences
##### Health Sciences
###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Occupational Therapy (Pre-Registration) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/occupational-therapy/ |
| 2 | Physiotherapy (Pre-Registration) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/physiotherapy/ |

###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Nutrition | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/clinical-nutrition/ |

##### Ecology and Biological Sciences
###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Advanced Biomedical Science | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/advanced-biomedical-science/ |
| 2 | Applied Sciences | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/applied-sciences/ |
| 3 | Clinical Neuroscience | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/clinical-neuroscience/ |

#### School of Psychology
##### Psychology
###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Developmental Psychology | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/developmental-psychology/ |
| 2 | Digital Health | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/digital-health/ |
| 3 | Forensic Psychology | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/forensic-psychology/ |
| 4 | Neuroscience and Mental Health | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/neuroscience-and-mental-health/ |
| 5 | Psychology (Conversion) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/psychology-conversion/ |
| 6 | Psychology (Conversion) Distance Learning | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/psychology-conversion-distance-learning/ |
| 7 | Psychology of Forensic and Criminal Behaviour | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/psychology-of-forensic-and-criminal-behaviour/ |

##### Therapy and Counselling
###### MSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Art Psychotherapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/art-psychotherapy/ |
| 2 | Cognitive Behavioural Therapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/cognitive-behavioural-therapy/ |
| 3 | Counselling Psychology (HCPC approved) | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/counselling-psychology/ |
| 4 | Dance Movement Psychotherapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/dance-movement-psychotherapy/ |
| 5 | Integrative Counselling and Psychotherapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/integrative-counselling-and-psychotherapy/ |
| 6 | Music Therapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/music-therapy/ |
| 7 | Play Therapy | https://www.roehampton.ac.uk/study/postgraduate-taught-courses/play-therapy/ |


### 2.2 Worked example — MBA (Business School)

- **Programme**: MBA — <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/>
- **Duration**: 1 year (full-time); +1 year Professional Experience Year option (integrated 2-year masters, not available for November entry).
- **Credits**: 180 credits at level 7.
- **Start dates (2026/27)**: July 2026, September 2026, November 2026, January 2027.
- **UK tuition fees**:
  | Entry date | MBA |
  |---|---|
  | July 2026 | £16,000 |
  | September 2026 | £16,640 |
  | November 2026 | £16,640 |
  | January 2027 | £16,640 |
- **International tuition fees**:
  | Entry date | MBA | Extended Masters (1 Sem) | Extended Masters (2 Sem) |
  |---|---|---|---|
  | July 2026 | £19,250 | £23,250 | £26,250 |
  | September 2026 | £20,020 | £24,180 | £27,300 |
  | November 2026 | £20,020 | – | – |
  | January 2027 | £20,020 | £24,180 | £27,300 |
- **Modules (Level 7)**: Global Strategic Management; Global Talent Management; Financial Performance Management for Decision Making; Marketing Communication and Strategy Development; Capstone Live Project (60 credits).
- **Assessment**: case-based assignments; financial/data analysis tasks; consultancy reports; marketing strategy portfolios; presentations and reflective reports; AI-enhanced business analytics exercises; capstone project.
- **Application portal**: Direct via Roehampton (or via the Roehampton online portal for international).

### 2.3 Graduate admissions model

- **Centralized admissions office** with per-school academic decision-making (e.g. Business School admissions panel, School of Psychology panel for Counselling Psychology PsychD).
- **Application portal**: Most taught postgraduates apply directly via <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/> (course-specific 'Apply' button). Research degrees apply via Graduate School. PGCE Primary/Secondary apply via UCAS or Roehampton.
- **PGCE routes**: 1-year PGCE Primary, 1-year PGCE Secondary, plus a Lead Partner Route (school-direct), and iPGCE for international teachers. <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/pgce-primary/>

---

## 3. Application Requirements & Deadlines (UK region)

### 3.1 Undergraduate — application data

| Item | Value | Source URL |
|---|---|---|
| UCAS application | Via UCAS; Roehampton UCAS institution code **N** | <https://www.ucas.com/> |
| Direct application | Available for international/PG/foundation applicants | <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> |
| Clearing hotline | 0300 303 8320 (Clearing 2026) | Sample: <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> |
| Multiple start dates | September 2026, January 2027, April 2027 (most UG) | <https://www.roehampton.ac.uk/study/undergraduate-courses/> |
| Personal statement | Required | <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/> |
| Two references | Required | <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/> |
| Interview | Programme-dependent (e.g. Nursing, Education, Counselling Psychology) | Sample: <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/counselling-psychology/> |
| Foundation Year | Most 3-year UG programmes offer 4-year 'with Foundation Year' variant | <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> |

### 3.2 English Language Requirements (UG + PG)

Source: <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/>. The page lists accepted tests but per-test minimum scores are programme-specific and shown on each course page. Sample from BSc Business Management:

| Exam | Notes |
|---|---|
| IELTS Academic | Accepted (sample: 5.5 for International Foundation Pathway). UG/PG minimums vary by programme; typically 6.0–6.5 for UG, 6.5–7.0 for PG. |
| TOEFL iBT (Home Edition NOT Accepted) | Accepted. Test must be ≤2 years old. |
| PTE Academic | Accepted. |
| Trinity Integrated Skills in English | Accepted. |
| Cambridge Proficiency / Advanced Certificate | Accepted. |
| GCSE / IGCSE English | Accepted (typically grade C/4 or above). |
| International Baccalaureate English | Accepted. |
| European Baccalaureate English | Accepted. |
| LanguageCert International ESOL | Accepted. |
| QA English Test | Accepted. |
| Roehampton University English Language Test | Internal online test. Cost £120 (10% discount code RU10). <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/roehampton-university-english-language-test/> |
| Kaplan Test of English (KTE) | Accepted. |
| UKVI list of majority English speaking countries | National exemption (Antigua & Barbuda, Australia, Bahamas, Barbados, Belize, Canada, Dominica, Grenada, Guyana, Jamaica, New Zealand, St Kitts & Nevis, St Lucia, St Vincent & Grenadines, Trinidad & Tobago, USA). |
| Pre-sessional English | Roehampton runs pre-sessional English courses in lieu of re-taking English tests. <https://www.roehampton.ac.uk/student-support/international-students/english-language-courses/> |

> Test validity: results typically only accepted if achieved in the last 2 years. For Student Route visa applicants, validity ≤ 2 years from date of issue (mandatory for CAS issuance).

### 3.3 Graduate — global rules

- **Application portal**: Direct to Roehampton (course page Apply button). PGCE via UCAS.
- **Application fee**: Standard UK PG application fee not stated; international students pay an **initial refundable deposit (IDP)** before full deposit payment (FDP). Excludes US, Norway, EU applicants.
- **Deposit payment**: Accepted via Easytransfer, Flywire, Convera (initial deposits via these methods only are refundable).
- **Early-bird discount**: £500 discount if initial or full deposit paid by the date specified in offer letter.
- **Funding deadline**: Scholarship schemes should be applied for well in advance of arrival in the UK. <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/postgraduate-scholarships/>
- **PGCE April-15-equivalent honor date**: N/A (UK PGCE generally begins in September, applications via UCAS by late summer prior year).
- **GRE/GMAT**: Not required for Roehampton PGT programmes (per the MBA sample page — no GRE/GMAT policy).
- **Language test policy**: See §3.2 above.
- **Institutional code**: Not applicable (Roehampton direct application, not test-report based).

### 3.4 Application checklist (per Roehampton guidance)

- Academic qualifications (certificate + transcript).
- Valid English language qualification.
- Personal statement.
- Two references.
- (For some programmes) Portfolio, audition, or interview.

Source: <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/>

---

## 4. Costs & Financial Aid

### 4.1 Undergraduate cost — sample (BSc Business Management, 2026/27)

Source: <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/>

**UK / Home students:**

| Entry date | Year 1 | Foundation Year |
|---|---|---|
| September 2026 | £9,790 | £5,760 |
| January 2027 | £9,790 | – |
| April 2027 | £9,790 | – |

**International students:**

| Entry date | Year 1 | Foundation Year | International Foundation Pathway | International Year 1 |
|---|---|---|---|---|
| April 2026 | £16,950 | – | – | – |
| September 2026 | £17,628 | £17,628 | £17,628 | £17,628 |
| January 2027 | £17,628 | – | £17,628 | £17,628 |
| April 2027 | £17,628 | – | – | – |

> Tuition fees are confirmed on each course page and in the offer letter. Multi-year courses should budget for **3–5% annual increase**. Source: <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/> and <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/>

### 4.2 Postgraduate cost — sample (MBA, 2026/27)

Source: <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/>

**UK / Home students:**

| Entry date | MBA |
|---|---|
| July 2026 | £16,000 |
| September 2026 | £16,640 |
| November 2026 | £16,640 |
| January 2027 | £16,640 |

**International students:**

| Entry date | MBA | Extended Masters (1 Sem) | Extended Masters (2 Sem) |
|---|---|---|---|
| July 2026 | £19,250 | £23,250 | £26,250 |
| September 2026 | £20,020 | £24,180 | £27,300 |
| November 2026 | £20,020 | – | – |
| January 2027 | £20,020 | £24,180 | £27,300 |

### 4.3 Part-time postgraduate policy

> Part-time master's students will be offered different payment schedules across their 2-year programme. Paying year's fees upfront each year earns a **2% discount**. Otherwise payment can be made in up to **7 instalments** depending on credits. Students in receipt of a SLC postgraduate loan pay in 3 instalments (33%/33%/34%). Source: <https://www.roehampton.ac.uk/study/fees-and-funding/home-postgraduate/>

### 4.4 Other costs

> 'Students undertaking certain programmes and courses may be required to pay an additional fee to cover part or all the cost of special equipment, consumables or facilities over and above the tuition fee. Where applicable these mandatory course costs include field trips, travel costs and attendance at performances.' — <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/>

### 4.5 Financial aid — undergraduate (international)

Source: <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/undergraduate-scholarships/>

- **International Excellence Scholarship** (Academic Excellence)
- **Global Excellence** (Country Scholarships)
- **EU Scholarship**
- **ASEAN Excellence Awards 2026**
- **Engineering and Technology Scholarship** (CEBE)
- **Talented Futures**: Esports Scholarships; Roehampton Women in Esports scholarship; Scholarship for Sporting Excellence
- **Roehampton Higher Technical Qualification (HNC/HND) Scholarship**
- **Arts, Humanities and Social Sciences Scholarship** (<https://www.roehampton.ac.uk/student-support/international-students/arts-humanities-and-social-sciences-scholarship/>)

### 4.6 Financial aid — postgraduate (international)

Source: <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/postgraduate-scholarships/>

- **International Excellence Scholarship** (Academic Excellence)
- **The Fulbright-University of Roehampton Award in Dance**
- **The Fulbright-University of Roehampton Scholar Award**
- **Country Scholarships** (Global Excellence)
- **EU Scholarship**
- **ASEAN Excellence Awards 2026**
- **Alumni discount** — **20% tuition fee discount** for Roehampton alumni
- **Talented Futures**: Esports, Women in Esports, Sport scholarships

### 4.7 Financial aid — UK/Home

- **Undergraduate Academic Excellence Scholarships** — <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/undergraduate-academic-excellence-scholarships/>
- **Postgraduate Graduate Gateway Scholarship** — <https://www.roehampton.ac.uk/study/fees-and-funding/home-postgraduate/graduate-gateway-scholarship/>
- **Student Loans** (UK UG + PG via Student Loans Company) — standard UK system.
- **Cost-of-living support** — <https://www.roehampton.ac.uk/student-support/non-academic-and-academic-support/financial-support-and-guidance/cost-of-living-support/>
- **Sport Roehampton scholarships** — <https://www.roehampton.ac.uk/student-life/sports-and-activities/sport-roehampton/sport-scholarship/>

### 4.8 Other payment notes

- 95% of tuition fees are spent directly on education (Roehampton self-report).
- Payment methods: credit/debit card online, bank transfer (Flywire/Easytransfer/Convera for international deposits).
- US Student Loans: <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/us-student-loans/>

---

## 5. Evidence Chain Index

| ID | Claim | Source URL | Snippet |
|---|---|---|---|
| E1 | 103 UG programmes offered (Sept 2026 intake + Jan/April 2027 where indicated) | <https://www.roehampton.ac.uk/study/undergraduate-courses/> | 'Showing N of 103 results' counter (final unique URL count after pagination = 103) |
| E2 | 72 taught PG programmes offered | <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/> | Header counter; 78 raw entries, 6 are pagination placeholders → 72 real programmes |
| E3 | 6 academic schools/faculties listed | <https://www.roehampton.ac.uk/study/academic-areas/> | School of Arts, Humanities and Social Sciences; Faculty of Business and Law; School of Computing, Engineering and the Built Environment; School of Education; School of Life and Health Sciences; School of Psychology |
| E4 | BSc Business Management UG tuition (UK): £9,790 (Sept 2026) | <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> | Fees table: 'September 2026 | £9,790 | £5,760' |
| E5 | BSc Business Management UG tuition (Intl): £17,628 (Sept 2026) | <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> | Fees table: 'September 2026 | £17,628 | £17,628 | £17,628 | £17,628' |
| E6 | MBA UK tuition £16,640 (Sept 2026) | <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/> | Fees table: 'September 2026 | £16,640' |
| E7 | MBA International tuition £20,020 (Sept 2026) | <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/> | Fees table: 'September 2026 | £20,020 | £24,180 | £27,300' |
| E8 | English language tests accepted list | <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/> | 'IELTS Academic, Roehampton English Language Test, Kaplan Test of English (KTE), TOEFL IBT (Home Edition not Accepted), PTE Academic, Trinity Integrated Skills in English, Cambridge Proficiency Certificate, Cambridge Advanced Certificate, GCSE, IGCSE, International Baccalaureate, European Baccalaureate English, Language Cert International ESOL, QA English Test' |
| E9 | International Foundation Pathway: 64 UCAS + IELTS 5.5 | <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> | 'International Foundation Pathway: 64 UCAS (or equivalent) IELTS: 5.5' |
| E10 | Alumni 20% PG tuition discount | <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/postgraduate-scholarships/> | 'Alumni discount — 20% tuition fee discount' |
| E11 | Initial deposit (IDP) + Full deposit (FDP) — refundable via Easytransfer/Flywire/Convera only | <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/> | 'initial deposit payment (IDP) before you make your full deposit payment (FDP)' |
| E12 | Early-bird £500 discount on timely deposit payment | <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/> | 'You may be eligible for a £500 discount if you pay your initial deposit or full deposit by a specific date' |
| E13 | 2% discount for paying part-time PG fees upfront each year | <https://www.roehampton.ac.uk/study/fees-and-funding/home-postgraduate/> | 'a 2% discount will be applied' (part-time PG) |
| E14 | 95% of tuition fee spent directly on education | <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/> | 'At Roehampton 95% of the tuition fee you pay will be spent directly on your education – one of the highest proportions in the country' |
| E15 | Roehampton English Language Test cost £120 (code RU10 = 10% off) | <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/roehampton-university-english-language-test/> | 'The test costs £120 - use the discount code RU10 to claim a 10% discount' |
| E16 | TOEFL iBT Home Edition NOT accepted | <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/> | 'TOEFL IBT (Home Edition not Accepted)' |
| E17 | Multiple start dates: September 2026, January 2027, April 2027 (most UG) | <https://www.roehampton.ac.uk/study/undergraduate-courses/> | 'September 2026, January 2027 • 3 years (full-time)' (course card) |
| E18 | Graduate School manages MPhil/PhD research admissions | <https://www.roehampton.ac.uk/study/academic-areas/graduate-school/> | 'Administers applications for research degrees. Oversees the Research Student Development Programme' |
| E19 | International fees indexed on each course page + offer letter | <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/> | 'You will find the tuition fee for your course, listed on the relevant undergraduate or postgraduate course pages' |
| E20 | Annual fee rise 3–5% for multi-year UG/PG courses | <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/> | 'budget for a likely increase of between three and five percent for each year of study with us on the same degree' |

---

## 6. WeKnora Import Manifest

Suggested chunking strategy for the WeKnora RAG ingest:

- **Section 0 (overview)** → single overview chunk for the institution summary.
- **Section 1 (UG)** → one chunk per (school, department, degree) group; each row in §1.2 = a sub-chunk.
- **Section 2 (PG)** → one chunk per (school, department, degree) group; one chunk for the MBA worked example (§2.2).
- **Section 3 (requirements)** → one chunk per sub-section (UG app data; English lang; PG rules; checklist).
- **Section 4 (costs)** → one chunk per cost sub-section (UG UK/Intl; PG UK/Intl; scholarships).
- **Section 5 (evidence)** → one chunk per evidence ID row (E1–E20).

---

## 7. Cross-School Comparison Framework

Roehampton sits in the UK **modern/post-1992 university** group, alongside other UK modern institutions in this knowledge base (e.g. Anglia Ruskin, Bath, Brighton, Canterbury Christ Church, Coventry, De Montfort, Derby, East London, Edinburgh Napier, Essex, Glasgow Caledonian, Goldsmiths, Greenwich, Harper Adams, Hertfordshire, Huddersfield, Hull, Keele, Kingston, Leeds Beckett, Leicester, Lincoln, LJMU, London Met, London South Bank, Manchester Met, Middlesex, Northampton, NTU, Northumbria, Oxford Brookes, Plymouth, Portsmouth, Queen Margaret, Reading, Robert Gordon, Salford, Sheffield Hallam, Staffordshire, Sunderland, Teesside, West London, Westminster, Wolverhampton, Worcester, York St John).

Key cross-school compare axes:

1. **UG/PG programme count** — Roehampton: 103 UG + 72 PG = 175 total.
2. **International tuition range** — Roehampton UG £17,628 / MBA £20,020 (typical UK modern range £14k–£22k).
3. **English language tests accepted** — Roehampton accepts 14 different English tests including internal Roehampton ELT.
4. **Schools structure** — 6 academic schools (vs 4–10 in most modern UK universities).
5. **Start-date flexibility** — multiple start dates (Sept + Jan + Apr for most UG; July + Sept + Nov + Jan for MBA — unusually flexible).
6. **Apprenticeships / HTQs / Foundation** — Roehampton offers all three pathways via School of Continuing Education.
7. **Teacher training routes** — 4 distinct routes (PGCE Primary, PGCE Secondary, Lead Partner Route, iPGCE).
8. **Alumni discount** — 20% PG tuition for Roehampton alumni (above-typical modern-uni alumni benefit).

---

## Appendix A — Source URLs

Primary source pages used in this document (all captured 2026-07-08):

- <https://www.roehampton.ac.uk/study/>
- <https://www.roehampton.ac.uk/study/undergraduate-courses/>
- <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/>
- <https://www.roehampton.ac.uk/study/postgraduate-research-courses/>
- <https://www.roehampton.ac.uk/study/academic-areas/>
- <https://www.roehampton.ac.uk/study/academic-areas/arts-humanities-and-social-sciences/>
- <https://www.roehampton.ac.uk/study/academic-areas/business-and-law/>
- <https://www.roehampton.ac.uk/study/academic-areas/computing-engineering-and-the-built-environment/>
- <https://www.roehampton.ac.uk/study/academic-areas/education/>
- <https://www.roehampton.ac.uk/study/academic-areas/life-and-health-sciences/>
- <https://www.roehampton.ac.uk/study/academic-areas/psychology/>
- <https://www.roehampton.ac.uk/study/academic-areas/graduate-school/>
- <https://www.roehampton.ac.uk/study/academic-areas/continuing-education/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/home-undergraduate/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/home-postgraduate/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/undergraduate-scholarships/>
- <https://www.roehampton.ac.uk/study/fees-and-funding/international-fees-and-financial-support/postgraduate-scholarships/>
- <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/>
- <https://www.roehampton.ac.uk/student-support/international-students/entry-requirements/roehampton-university-english-language-test/>
- <https://www.roehampton.ac.uk/study/undergraduate-courses/business-management/> (worked example)
- <https://www.roehampton.ac.uk/study/postgraduate-taught-courses/mba/> (worked example)

## Appendix B — Document coverage

- UG programmes captured: **103** (per school landing-page crawl, deduplicated).
- PG programmes captured: **72** (per school landing-page crawl, deduplicated).
- Reconciliation: **175 rows = sum of distribution matrix cells = Section 1 row count + Section 2 row count**.
- All cited URLs accessed 2026-07-08.
