# University of Derby Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: college → school → subject-area → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科专业 (UG) | 297 |
| 研究生授课型 (PGT: MA/MSc/MBA/LLM/PGCert/PGDip) | 104 |
| 在线课程 (Online) | 108 |
| **学位项目总计 (UG + PGT + Online)** | **509** |
| 学院 (Colleges) | 3 + 1 Institute |
| 学术学院 (Academic Schools) | 7 |
| 本科科目领域 (UG Subject Areas) | 40 |

> **Data source**: University of Derby A-Z course page (`derby.ac.uk/courses/a-z/`), accessed 2026-07-08.
> **Note**: Foundation year and placement year variants are listed as separate course entries. Joint honours courses are listed under the joint-honours subject area. Online courses are counted separately.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

```
University of Derby
├── College of Health and Humanities                        [学院]
│   ├── School of Health and Social Care                    [系]
│   ├── School of Health, Sport and Rehabilitation          [系]
│   └── School of Humanities, Law and Creative Arts         [系]
├── College of Science and Engineering                      [学院]
│   ├── School of Science                                   [系]
│   ├── School of Engineering and Built Environment          [系]
│   └── School of Computing                                 [系]
├── Derby International Business School                     [学院]
│   └── (School-level structure not subdivided)              [系]
└── Institute of Education and Skills                       [学院]
    └── (School-level structure not subdivided)              [系]
```

> **Note**: Derby uses a College > School hierarchy. The Institute of Education operates at the same level as the three colleges. University of Derby Online Learning (UDOL) offers 100+ part-time online courses across all colleges.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts (Hons) | 本科 | 167 |
| BSc | Bachelor of Science (Hons) | 本科 | 98 |
| BEng | Bachelor of Engineering (Hons) | 本科 | 10 |
| LLB | Bachelor of Laws (Hons) | 本科 | 3 |
| FdA | Foundation Degree (Arts) | 本科 (Foundation) | 3 |
| MSci | Master in Science (integrated) | 本科 (4-year) | ~3 |
| MEdu | Master of Education (integrated) | 本科 (4-year) | 1 |
| MArts | Master of Arts (integrated) | 本科 (4-year) | 1 |
| BEd | Bachelor of Education (Hons) | 本科 | 1 |
| MSc | Master of Science | 研究生授课型 | 56 |
| MA | Master of Arts | 研究生授课型 | 18 |
| MBA | Master of Business Administration | 研究生授课型 | 3 |
| LLM | Master of Laws | 研究生授课型 | 2 |
| MRes | Master of Research | 研究生研究型 | ~3 |
| PG Cert | Postgraduate Certificate | 研究生证书 | ~10 |
| PG Dip | Postgraduate Diploma | 研究生文凭 | ~5 |
| EdD | Doctor of Education | 博士 (Online) | 1 |
| DBA | Doctor of Business Administration | 博士 | 1 |

> **UK degree naming note**: MSci, MArts, and MEdu are 4-year **integrated master's** degrees classified as undergraduate in the UK system.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 | UG | PGT | 合计 |
|------|------|------|------|
| College of Health and Humanities | 105 | 49 | **154** |
| College of Science and Engineering | 64 | 23 | **87** |
| Derby International Business School | 60 | 23 | **83** |
| Institute of Education | 19 | 9 | **28** |
| Various (Joint Honours) | 49 | 0 | **49** |
| **合计** | **297** | **104** | **401** |

> **Reconciliation**: Campus-based UG (297) + PG (104) = 401. Online (108) counted separately. Total A-Z listing: 509 entries.

---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

University of Derby has 3 colleges plus the Institute of Education, each containing academic schools. UCAS institution code: **D39**.

### 1.2 Undergraduate programmes — grouped by 学院 > 科目领域 > 学位级别

#### College of Health and Humanities

##### Art and Design

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Animation BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/animation-ba-hons/) |
| 2 | Animation with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/animation-ba-hons-foundation/) |
| 3 | Fine Art BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/fine-art-ba-hons/) |
| 4 | Fine Art with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/fine-art-ba-hons-foundation/) |
| 5 | Graphic Design BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/graphic-design-ba-hons/) |
| 6 | Graphic Design with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/graphic-design-ba-hons-foundation/) |
| 7 | Illustration BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/illustration-ba-hons/) |
| 8 | Illustration with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/illustration-ba-hons-foundation/) |
| 9 | Interior Design BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/interior-design-ba-hons/) |
| 10 | Interior Design with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/art-design-courses/interior-design-ba-hons-foundation/) |

##### Counselling and Psychotherapy

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Counselling and Psychotherapy (Humanistic Approaches) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/counselling-psychotherapy-courses/counselling-psychotherapy-bsc-hons/) |
| 2 | Counselling and Psychotherapy (Humanistic Approaches) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/counselling-psychotherapy-courses/counselling-psychotherapy-bsc-hons-foundation/) |

##### English, Creative Writing and Publishing

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing and Publishing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/creative-writing-publishing-ba-hons/) |
| 2 | Creative Writing and Publishing with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/creative-writing-publishing-ba-hons-foundation/) |
| 3 | English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-ba-hons/) |
| 4 | English with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/english-creative-writing-publishing-courses/english-ba-hons-foundation/) |

##### Fashion

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/fashion-courses/fashion-design-ba-hons/) |
| 2 | Fashion with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/fashion-courses/fashion-design-ba-hons-foundation/) |
| 3 | Fashion, Marketing and Communication BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/fashion-courses/fashion-marketing-communications-ba-hons/) |
| 4 | Fashion, Marketing and Communication with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/fashion-courses/fashion-marketing-communication-ba-hons-foundation/) |

##### Film

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Film and High-End Television Production BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/film-courses/film-high-end-television-production-ba-hons/) |
| 2 | Film and High-End Television Production with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/film-courses/film-high-end-television-production-ba-hons-foundation/) |

##### History, International Relations and Politics

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | History BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/history-international-relations-politics-courses/history-ba-hons/) |
| 2 | History with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/history-international-relations-politics-courses/history-ba-hons-foundation/) |
| 3 | International Relations and Politics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/history-international-relations-politics-courses/international-relations-politics-ba-hons/) |
| 4 | International Relations and Politics with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/history-international-relations-politics-courses/international-relations-politics-ba-hons-foundation/) |

##### Journalism and Media

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Football Journalism BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/football-journalism-ba-hons/) |
| 2 | Football Journalism with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/football-journalism-ba-hons-foundation/) |
| 3 | Media and Communication BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/media-and-communication-ba-hons/) |
| 4 | Media and Communication with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/media-communications-ba-hons-foundation/) |
| 5 | Media Content Creation BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/media-content-creation-ba-hons/) |
| 6 | Media Content Creation with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/media-content-creation-ba-hons-foundation/) |
| 7 | Sports Journalism and Communications BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/sports-journalism-and-communications-ba-hons/) |
| 8 | Sports Journalism and Communications with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/journalism-media-courses/sports-journalism-and-communications-ba-hons-foundation/) |

##### Law

###### LLB

| # | 专业 | URL |
|---|------|-----|
| 1 | Law LLB (Hons) | [Link](https://www.derby.ac.uk/undergraduate/law-courses/llb/) |
| 2 | LLB (Hons) with Criminology | [Link](https://www.derby.ac.uk/undergraduate/law-courses/llb-criminology/) |
| 3 | LLB (Hons) with Foundation Year | [Link](https://www.derby.ac.uk/undergraduate/law-courses/llb-foundation/) |

##### Midwifery

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Midwifery BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/midwifery-courses/midwifery-bsc-hons/) |

##### Music and Music Production

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Music Performance BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/music-music-production-courses/music-performance-ba-hons/) |
| 2 | Music Performance with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/music-music-production-courses/music-performance-ba-hons-foundation/) |
| 3 | Music Production BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/music-music-production-courses/music-production-ba-hons/) |
| 4 | Music Production with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/music-music-production-courses/music-production-bsc-hons-foundation/) |

##### Nursing

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-adult-bsc-hons/) |
| 2 | Nursing (Adult) Direct Entry BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-adult-direct-entry-bsc-hons/) |
| 3 | Nursing (Adult) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-adult-bsc-hons-foundation/) |
| 4 | Nursing (Children's) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-childrens-bsc-hons/) |
| 5 | Nursing (Children's) Direct Entry BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-children-direct-entry-bsc-hons/) |
| 6 | Nursing (Children's) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-childrens-bsc-hons-foundation/) |
| 7 | Nursing (Learning Disabilities) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-learning-disabilities-bsc-hons-foundation/) |
| 8 | Nursing (Mental Health) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-bsc-hons/) |
| 9 | Nursing (Mental Health) Direct Entry BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-direct-entry-bsc-hons/) |
| 10 | Nursing (Mental Health) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-bsc-hons-foundation/) |

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Adult) and Leadership MSci | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-adult-and-leadership-msci/) |
| 2 | Nursing (Child) and Leadership MSci | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-child-and-leadership-msci/) |
| 3 | Nursing (Mental Health) and Leadership MSci | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-mental-health-and-leadership-msci/) |
| 4 | Nursing Dual Award (Adult and Child) MSci | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-dual-award-adult-and-child-msci/) |
| 5 | Nursing Dual Award (Adult and Mental Health) MSci | [Link](https://www.derby.ac.uk/undergraduate/nursing-courses/nursing-dual-award-adult-and-mental-health-msci/) |

##### Occupational Therapy

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Occupational Therapy BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/occupational-therapy-courses/occupational-therapy-bsc-hons/) |
| 2 | Occupational Therapy with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/occupational-therapy-courses/occupational-therapy-bsc-hons-foundation/) |

##### Photography

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Commercial Photography BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/photography-courses/commercial-photography-ba-hons/) |
| 2 | Commercial Photography with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/photography-courses/photography-commercial-ba-hons-foundation/) |
| 3 | Photography BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/photography-courses/photography-ba-hons/) |
| 4 | Photography with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/photography-courses/photography-ba-hons-foundation/) |

##### Physiotherapy

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Physiotherapy BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/physiotherapy-courses/physiotherapy-bsc-hons/) |
| 2 | Physiotherapy with Foundation Year BSc (Hons) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/physiotherapy-courses/physiotherapy-foundation-bsc-hons/) |

##### Policing

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Policing and Investigations BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/policing-courses/policing-and-investigations-ba-hons/) |
| 2 | Professional Policing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/policing-courses/professional-policing-ba-hons/) |
| 3 | Professional Policing with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/policing-courses/professional-policing-with-foundation-year-ba-hons/) |

##### Psychology

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Psychology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/psychology-courses/forensic-psychology-bsc-hons/) |
| 2 | Forensic Psychology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/psychology-courses/forensic-psychology-bsc-hons-foundation/) |
| 3 | Psychology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/psychology-courses/psychology-bsc-hons/) |
| 4 | Psychology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/psychology-courses/psychology-bsc-hons-foundation/) |

##### Public Health and Social Care

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Social Work BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/public-health-social-care-courses/applied-social-work-ba-hons/) |
| 2 | Applied Social Work with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/public-health-social-care-courses/social-work-applied-ba-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Health and Social Care Practice (with pathways) BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/public-health-social-care-courses/health-and-social-care-practice-bsc-hons/) |
| 2 | Health and Social Care Practice (with pathways) with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/public-health-social-care-courses/health-and-social-care-practice-bsc-hons-foundation/) |

##### Radiography

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Diagnostic Radiography BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/radiography-courses/diagnostic-radiography-bsc-hons/) |
| 2 | Diagnostic Radiography with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/radiography-courses/diagnostic-radiography-bsc-hons-foundation/) |

##### Social Sciences

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/criminology-sociology-ba-hons/) |
| 2 | Criminology and Sociology with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/criminology-sociology-ba-hons-foundation/) |
| 3 | Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/sociology-ba-hons/) |
| 4 | Sociology with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/sociology-ba-hons-foundation/) |
| 5 | Sociology with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/sociology-ba-hons-with-placement-year/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/criminology-bsc-hons/) |
| 2 | Criminology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/social-sciences-courses/criminology-bsc-hons-foundation/) |

##### Sport and Exercise Science

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Physical Education, Physical Activity and Sport BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/physical-education-physical-activity-and-sport-ba-hons/) |
| 2 | Physical Education, Physical Activity and Sport with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/physical-education-physical-activity-and-sport-ba-hons-foundation/) |
| 3 | Sport Coaching and Coach Development BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-coaching-and-coach-development-ba-hons/) |
| 4 | Sport Coaching and Coach Development with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-coaching-and-coach-development-with-foundation-year-ba-hons/) |
| 5 | Sport Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-management-ba-hons/) |
| 6 | Sport Management with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-management-ba-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Performance Analysis and Coaching Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/performance-analysis-coaching-science-bsc-hons/) |
| 2 | Performance Analysis and Coaching Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/performance-analysis-coaching-science-bsc-hons-foundation/) |
| 3 | Sport and Exercise Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-exercise-science-bsc-hons/) |
| 4 | Sport and Exercise Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-and-exercise-science-bsc-hons-foundation/) |
| 5 | Sport Therapy and Rehabilitation BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-therapy-and-rehabilitation-bsc-hons/) |
| 6 | Sport Therapy and Rehabilitation with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sport-therapy-and-rehabilitation-bsc-hons-foundation/) |
| 7 | Sports Nutrition and Health BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sports-nutrition-health-bsc-hons/) |
| 8 | Sports Nutrition and Health with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/sports-nutrition-health-bsc-hons-foundation/) |

###### FdA

| # | 专业 | URL |
|---|------|-----|
| 1 | Athlete Professional Development FdA | [Link](https://www.derby.ac.uk/undergraduate/sport-exercise-science-courses/athlete-professional-development-fda/) |

##### Theatre

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/theatre-courses/theatre-arts-ba-hons/) |
| 2 | Theatre Arts with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/theatre-courses/theatre-arts-ba-hons-foundation/) |

##### Therapeutic Arts

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Expressive Arts, Health, and Wellbeing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/therapeutic-arts-courses/creative-expressive-arts-health-wellbeing-ba-hons/) |
| 2 | Creative Expressive Arts, Health, and Wellbeing with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/therapeutic-arts-courses/creative-expressive-arts-health-wellbeing-ba-hons-foundation-year/) |

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Expressive Arts and Health Practice MArts (Hons) | [Link](https://www.derby.ac.uk/undergraduate/therapeutic-arts-courses/creative-expressive-arts-health-practice-marts-hons/) |


#### College of Science and Engineering

##### Architectural Technologies and Interior Architecture

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architecture-ba-hons/) |
| 2 | Architecture with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architecture-ba-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Technology and Practice BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architectural-technology-and-practice-bsc-hons/) |
| 2 | Architectural Technology and Practice with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/architecture-architectural-technology-courses/architectural-technology-and-practice-bsc-hons-foundation/) |

##### Artificial Intelligence

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Data Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-and-data-science-bsc-hons/) |
| 2 | Artificial Intelligence and Data Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-data-science-bsc-hons-foundation/) |
| 3 | Artificial Intelligence in Criminology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-criminology-bsc-hons/) |
| 4 | Artificial Intelligence in Digital Marketing BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-digital-marketing-bsc-hons/) |
| 5 | Artificial Intelligence in Healthcare BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-healthcare-bsc-hons/) |
| 6 | Artificial Intelligence in Human Resources BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-human-resources-bsc-hons/) |
| 7 | Artificial Intelligence in Psychology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/artificial-intelligence-courses/artificial-intelligence-psychology-bsc-hons/) |

##### Biology and Zoology

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Biology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biology-zoology-courses/biology-bsc-hons/) |
| 2 | Biology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biology-zoology-courses/biology-bsc-hons-foundation/) |
| 3 | Zoology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biology-zoology-courses/zoology-bsc-hons/) |
| 4 | Zoology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biology-zoology-courses/zoology-bsc-hons-foundation/) |

##### Biomedical Science

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/biomedical-science-bsc-hons/) |
| 2 | Biomedical Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/biomedical-science-bsc-hons-foundation/) |
| 3 | Human Biology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/human-biology-bsc-hons/) |
| 4 | Human Biology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/human-biology-bsc-hons-foundation/) |
| 5 | Pharmacology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/pharmacology-bsc-hons/) |
| 6 | Pharmacology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/biomedical-science-courses/pharmacology-bsc-hons-foundation/) |

##### Civil Engineering and Construction

###### BEng

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-beng-hons/) |
| 2 | Civil Engineering with Foundation Year BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-beng-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-bsc-hons/) |
| 2 | Civil Engineering with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/civil-engineering-bsc-hons-foundation/) |
| 3 | Construction Management BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/construction-management-bsc-hons/) |
| 4 | Construction Management with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/construction-management-bsc-hons-foundation/) |
| 5 | Quantity Surveying and Commercial Management BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/quantity-surveying-commercial-mgmt-bsc-hons/) |
| 6 | Quantity Surveying and Commercial Management with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/civil-engineering-construction-courses/quantity-surveying-and-commercial-management-bsc-hons-foundation/) |

##### Computer Games

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Game Art BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-art-ba-hons/) |
| 2 | Game Art with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-art-ba-hons-foundation/) |
| 3 | Game Design BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-design-ba-hons/) |
| 4 | Game Design with Foundation Year (Art) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-design-ba-hons-foundation-art/) |
| 5 | Game Design with Foundation Year (Computing) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-design-ba-hons-foundation-computing/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Game Programming BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-programming-bsc-hons/) |
| 2 | Game Programming with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computer-games-courses/game-programming-bsc-hons-foundation/) |

##### Computing

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Games Modelling and Animation with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-modelling-animation-ba-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Games Programming with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/computer-games-programming-bsc-hons-foundation/) |
| 2 | Computer Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/computer-science-bsc-hons/) |
| 3 | Computer Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/computer-science-bsc-hons-foundation/) |
| 4 | Cyber Security BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/cyber-security-bsc-hons/) |
| 5 | Cyber Security with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/cyber-security-bsc-hons-foundation/) |
| 6 | Information Technology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/information-technology-bsc-hons/) |
| 7 | Information Technology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/information-technology-bsc-hons-foundation/) |
| 8 | Internet of Things BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/internet-of-things-bsc-hons/) |
| 9 | Internet of Things with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/computing-courses/internet-of-things-bsc-hons-foundation/) |

##### Engineering

###### BEng

| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical and Electronic Engineering BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/electrical-and-electronic-engineering-beng-hons/) |
| 2 | Electrical and Electronic Engineering with Foundation Year BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/electrical-and-electronic-engineering-beng-hons-foundation/) |
| 3 | Engineering Management (Top-Up) BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/engineering-management-beng-hons-top-up/) |
| 4 | Mechanical and Manufacturing Engineering (Top-Up) BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/mechanical-manufacturing-engineering-beng-hons-top-up/) |
| 5 | Mechanical Engineering BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/mechanical-engineering-beng-hons/) |
| 6 | Mechanical Engineering with Foundation Year BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/mechanical-engineering-beng-hons-foundation/) |
| 7 | Motorsport Engineering BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/motorsport-engineering-beng-hons/) |
| 8 | Motorsport Engineering with Foundation Year BEng (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/motorsport-engineering-beng-hons-foundation/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Sound, Light and Live Event Engineering BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/sound-light-and-live-event-engineering-bsc-hons/) |
| 2 | Sound, Light and Live Event Engineering with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/engineering-courses/sound-light-and-live-event-engineering-bsc-hons-foundation/) |

##### Environmental Sciences

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Sciences BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/environmental-science-courses/earth-sciences-bsc-hons/) |
| 2 | Earth Sciences with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/environmental-science-courses/earth-sciences-bsc-hons-foundation/) |
| 3 | Environmental Science and Sustainability BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/environmental-science-courses/environmental-science-sustainability-bsc-hons/) |
| 4 | Environmental Science and Sustainability with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/environmental-science-courses/environmental-science-sustainability-bsc-hons-foundation/) |

##### Forensic Science

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Science BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-bsc-hons/) |
| 2 | Forensic Science with Criminology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-criminology-bsc-hons/) |
| 3 | Forensic Science with Criminology with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-with-criminology-bsc-hons-foundation/) |
| 4 | Forensic Science with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/forensic-science-courses/forensic-science-bsc-hons-foundation/) |


#### Derby International Business School

##### Accounting, Economics and Finance

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Accounting and Finance BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/business-accounting-and-finance-ba-hons/) |
| 2 | Business Accounting and Finance with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/business-accounting-and-finance-ba-hons-foundation/) |
| 3 | Business Accounting and Finance with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/business-accounting-and-finance-ba-hons-with-placement-year/) |
| 4 | Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-ba-hons/) |
| 5 | Economics with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-ba-hons-foundation/) |
| 6 | Economics with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-ba-hons-with-placement-year/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/accounting-and-finance-bsc-hons/) |
| 2 | Accounting and Finance with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/accounting-and-finance-bsc-hons-foundation/) |
| 3 | Accounting and Finance with Placement Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/accounting-and-finance-bsc-hons-with-placement-year/) |
| 4 | Economics and Finance BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-and-finance-bsc-hons/) |
| 5 | Economics and Finance with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-and-finance-bsc-hons-foundation/) |
| 6 | Economics and Finance with Placement Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/accounting-economics-finance-courses/economics-finance-bsc-hons-with-placement-year/) |

##### Business Management

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management (Top-Up) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-ba-hons-top-up/) |
| 2 | Business Management and Entrepreneurship BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-entrepreneurship-ba-hons/) |
| 3 | Business Management and Entrepreneurship with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-entrepreneurship-ba-hons-with-placement-year/) |
| 4 | Business Management and Finance BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-finance-ba-hons/) |
| 5 | Business Management and Finance with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-finance-ba-hons-with-placement-year/) |
| 6 | Business Management and Human Resource Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-human-resource-management-ba-hons/) |
| 7 | Business Management and Human Resource Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-human-resource-management-ba-hons-with-placement-year/) |
| 8 | Business Management and Marketing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-marketing-ba-hons/) |
| 9 | Business Management and Marketing with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-marketing-ba-hons-with-placement-year/) |
| 10 | Business Management and Sustainable Practice BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-sustainable-practice-ba-hons/) |
| 11 | Business Management and Sustainable Practice with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-sustainable-practice-ba-hons-with-placement-year/) |
| 12 | Business Management and Tourism BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-tourism-ba-hons/) |
| 13 | Business Management and Tourism with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-tourism-placement-year-ba-hons/) |
| 14 | Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-ba-hons/) |
| 15 | Business Management with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-ba-hons-foundation/) |
| 16 | Business Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-ba-hons-with-placement-year/) |
| 17 | Business Management, Analytics and Technology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-analytics-technology-ba-hons/) |
| 18 | Business Management, Analytics and Technology with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-analytics-technology-ba-hons-with-placement-year/) |
| 19 | Business Management, Supply Chain and Logistics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-supply-chain-logistics-ba-hons/) |
| 20 | Business Management, Supply Chain and Logistics with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/business-management-supply-chain-logistics-ba-hons-with-placement-year/) |
| 21 | International Business and Finance top-up BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/international-business-and-finance-ba-hons-top-up/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | International Business and AI BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/international-business-ai-bsc-hons/) |
| 2 | International Business Management BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/international-business-management-bsc-hons/) |
| 3 | International Business Management with Foundation Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/international-business-management-bsc-hons-foundation/) |
| 4 | International Business Management with Placement Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/business-management-courses/international-business-management-bsc-hons-with-placement-year/) |

##### Events, Tourism and Hospitality Management

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Event Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/events-management-ba-hons/) |
| 2 | Event Management with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/event-management-ba-hons-foundation/) |
| 3 | Event Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/event-management-ba-hons-with-placement-year/) |
| 4 | International Hospitality Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/international-hospitality-management-ba-hons/) |
| 5 | International Hospitality Management with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/international-hospitality-management-ba-hons-foundation/) |
| 6 | International Hospitality Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/international-hospitality-management-ba-hons-with-placement-year/) |
| 7 | International Tourism Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/tourism-management-ba-hons/) |
| 8 | International Tourism Management with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/international-tourism-management-ba-hons-foundation/) |
| 9 | International Tourism Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/events-hospitality-tourism-management-courses/tourism-management-ba-hons-with-placement-year/) |

##### Marketing

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | International Marketing (Top-Up) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/international-marketing-ba-hons-top-up/) |
| 2 | Marketing and Consumer Psychology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-consumer-psychology-ba-hons/) |
| 3 | Marketing and Consumer Psychology with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-consumer-psychology-ba-hons-with-placement-year/) |
| 4 | Marketing and Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-management-ba-hons/) |
| 5 | Marketing and Management with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-management-ba-hons-with-placement-year/) |
| 6 | Marketing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-ba-hons/) |
| 7 | Marketing with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-ba-hons-foundation/) |
| 8 | Marketing with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-ba-hons-with-placement-year/) |
| 9 | Marketing, PR and Advertising BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-pr-advertising-ba-hons/) |
| 10 | Marketing, PR and Advertising with Placement Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-pr-advertising-ba-hons-with-placement-year/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Digital Marketing BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/digital-marketing-bsc-hons/) |
| 2 | Digital Marketing with Placement Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/digital-marketing-bsc-hons-with-placement-year/) |
| 3 | Marketing and Data Insights BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-data-insights-bsc-hons/) |
| 4 | Marketing and Data Insights with Placement Year BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/marketing-courses/marketing-and-data-insights-bsc-hons-with-placement-year/) |


#### Institute of Education

##### Access to Higher Education

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Access to Higher Education Diploma (Business and Law) | [Link](https://www.derby.ac.uk/undergraduate/access-courses/access-to-higher-education-diploma-business-and-law/) |
| 2 | Access to Higher Education Diploma (Medical Science with Health Psychology) | [Link](https://www.derby.ac.uk/undergraduate/access-courses/access-to-higher-education-diploma-medical-science-health-psychology/) |
| 3 | Access to Higher Education Diploma (Medical Science) with Chemistry or Physics | [Link](https://www.derby.ac.uk/undergraduate/access-courses/access-to-higher-education-diploma-medical-science-chemistry-physics/) |
| 4 | Access to Higher Education Diploma (Social Science) | [Link](https://www.derby.ac.uk/undergraduate/access-courses/access-to-higher-education-diploma-social-science/) |
| 5 | Access to Higher Education Diploma: Law and Criminology | [Link](https://www.derby.ac.uk/undergraduate/access-courses/access-to-higher-education-diploma-law-criminology/) |
| 6 | Foundation Pathways Programme | [Link](https://www.derby.ac.uk/undergraduate/access-courses/foundation-pathways/) |
| 7 | International Foundation Programme | [Link](https://www.derby.ac.uk/undergraduate/access-courses/international-foundation-programme/) |
| 8 | Level 2 English and Maths | [Link](https://www.derby.ac.uk/undergraduate/access-courses/pre-access-level-2/) |

##### Education, Childhood and SEND

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Studies (Top-Up) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/early-childhood-studies-top-up-ba-hons/) |
| 2 | Education Studies (Top-Up) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/education-studies-top-up-ba-hons/) |
| 3 | Education Studies with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/education-studies-ba-hons-foundation/) |
| 4 | Education Studies with optional pathway in SEND or TESOL BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/education-studies-ba-hons/) |
| 5 | Special Educational Needs and Disability (Top-Up) BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/special-education-needs-disabilities-top-up-ba-hons/) |
| 6 | Special Educational Needs and Disability BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/special-educational-needs-disability-ba-hons/) |
| 7 | Special Educational Needs and Disability with Foundation Year BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/special-educational-needs-disability-ba-hons-foundation/) |

###### FdA

| # | 专业 | URL |
|---|------|-----|
| 1 | Children and Young People FdA | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/children-and-young-people-fda/) |
| 2 | Special Educational Needs and Disabilities FdA | [Link](https://www.derby.ac.uk/undergraduate/education-childhood-inclusion-courses/special-educational-needs-disabilities-fda/) |

##### Teacher Training

###### Other

| # | 专业 | URL |
|---|------|-----|
| 1 | Education with Qualified Teacher Status Integrated Masters MEdu | [Link](https://www.derby.ac.uk/undergraduate/teacher-training-courses/education-integrated-masters/) |
| 2 | Primary Education with Qualified Teacher Status (5-11) BEd (Hons) | [Link](https://www.derby.ac.uk/undergraduate/teacher-training-courses/primary-education-qts-bed-hons/) |


#### Various (Joint Honours)

##### Joint Honours Programmes

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management and Accounting BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/business-management-and-accounting-ba-hons/) |
| 2 | Business Management and Criminology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/business-management-criminology-ba-hons/) |
| 3 | Business Management and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/business-management-and-economics-ba-hons/) |
| 4 | Business Management and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/business-management-and-english-ba-hons/) |
| 5 | Education Studies and Criminology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/criminology-and-education-studies-ba-bsc-hons/) |
| 6 | Education Studies and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/education-studies-economics-ba-hons/) |
| 7 | Education Studies and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-education-studies-ba-hons/) |
| 8 | English and Creative and Professional Writing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-creative-and-professional-writing-ba-hons/) |
| 9 | English and Law BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-law-ba-hons/) |
| 10 | Entrepreneurship and Creative and Professional Writing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-creative-professional-writing-ba-hons/) |
| 11 | Entrepreneurship and Human Resource Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-human-resource-management-ba-hons/) |
| 12 | Entrepreneurship and Law BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-law-ba-hons/) |
| 13 | Entrepreneurship and Marketing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-marketing-ba-hons/) |
| 14 | Entrepreneurship and Music Performance BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-and-music-performance-ba-hons/) |
| 15 | Entrepreneurship and Publishing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-and-publishing-ba-hons/) |
| 16 | Entrepreneurship and Theatre BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/entrepreneurship-theatre-ba-hons/) |
| 17 | History and Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-business-management-ba-hons/) |
| 18 | History and Criminology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-criminology-ba-bsc-hons/) |
| 19 | History and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-economics-ba-hons/) |
| 20 | History and Education Studies BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-education-ba-hons/) |
| 21 | History and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-history-ba-hons/) |
| 22 | History and Law BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-law-ba-hons/) |
| 23 | History and Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/history-and-sociology-ba-hons/) |
| 24 | International Relations and Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/international-relations-business-management-ba-hons/) |
| 25 | International Relations and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/international-relations-economics-ba-hons/) |
| 26 | International Relations and Law BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/international-relations-law-ba-hons/) |
| 27 | International Relations and Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/international-relations-sociology-ba-hons/) |
| 28 | Law and Accounting BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/law-and-accounting-ba-hons/) |
| 29 | Law and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/law-and-economics-ba-hons/) |
| 30 | Media and Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/media-and-business-management-ba-hons/) |
| 31 | Media and Criminology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/criminology-and-media-ba-bsc-hons/) |
| 32 | Media and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/media-and-english-ba-hons/) |
| 33 | Media and Marketing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/media-and-marketing-ba-hons/) |
| 34 | Media and Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/sociology-and-media-ba-hons/) |
| 35 | Music Performance and Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/music-performance-and-business-management-ba-hons/) |
| 36 | Psychology and Business Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-business-management-ba-hons/) |
| 37 | Psychology and Education Studies BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-education-studies-ba-bsc-hons/) |
| 38 | Psychology and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-psychology-ba-hons/) |
| 39 | Psychology and Law BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-law-ba-bsc-hons/) |
| 40 | Psychology and Publishing BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/publishing-and-psychology-ba-bsc-hons/) |
| 41 | Psychology and Sociology BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-sociology-ba-bsc-hons/) |
| 42 | Psychology and Theatre BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-theatre-arts-ba-hons/) |
| 43 | Publishing and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/english-and-publishing-ba-hons/) |
| 44 | Sociology and Economics BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/sociology-and-economics-ba-hons/) |
| 45 | Sociology and English BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/sociology-and-english-ba-hons/) |
| 46 | Sociology and Human Resource Management BA (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/sociology-and-human-resource-management-ba-hons/) |

###### BSc

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology and Criminology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-criminology-bsc-hons/) |
| 2 | Psychology and Sport Studies BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/psychology-and-sport-studies-bsc-hons/) |
| 3 | Sport Studies and Criminology BSc (Hons) | [Link](https://www.derby.ac.uk/undergraduate/joint-honours-courses/criminology-and-sport-studies-ba-bsc-hons/) |


---

## SECTION 2 — Graduate Education

### 2.1 Postgraduate programmes — grouped by 学院 > 科目领域 > 学位级别

#### College of Health and Humanities

##### Art and Design

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Arts (pathways in Fine Art or Photography) MA | MA | [Link](https://www.derby.ac.uk/postgraduate/art-design-courses/arts-ma/) |
| 2 | Creative and Cultural Industries MA | MA | [Link](https://www.derby.ac.uk/postgraduate/art-design-courses/creative-and-cultural-industries-ma/) |
| 3 | Design MA/MDes | MA | [Link](https://www.derby.ac.uk/postgraduate/art-design-courses/design-ma-mdes/) |

##### Counselling and Psychotherapy

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Cognitive Behavioural Psychotherapy (Adult or Children and Young People) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/counselling-psychotherapy-courses/cognitive-behavioural-psychotherapy-msc/) |
| 2 | Integrative Counselling and Psychotherapy (incorporating PG Cert/PG Dip) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/counselling-psychotherapy-courses/integrative-counselling-psychotherapy-msc/) |

##### Criminology and Policing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Criminal Investigation MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/criminology-policing-courses/criminal-investigation-msc/) |
| 2 | Criminal Justice and Criminology MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/criminology-policing-courses/criminal-justice-and-criminology-msc/) |
| 3 | Intelligence, Security and Disaster Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/criminology-policing-courses/intelligence-security-and-disaster-management-msc/) |
| 4 | Police Leadership, Strategy and Organisation MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/criminology-policing-courses/police-leadership-strategy-organisation-msc/) |

##### English, Creative Writing and Publishing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Creative Writing MA | MA | [Link](https://www.derby.ac.uk/postgraduate/english-creative-writing-publishing-courses/creative-writing-ma/) |
| 2 | Publishing MA | MA | [Link](https://www.derby.ac.uk/postgraduate/english-creative-writing-publishing-courses/publishing-ma/) |

##### Film

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Film and Screen Production MA | MA | [Link](https://www.derby.ac.uk/postgraduate/film-courses/film-and-screen-production-ma/) |

##### Global Affairs and Politics

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Global Affairs and Politics MA | MA | [Link](https://www.derby.ac.uk/postgraduate/global-affairs-and-politics-courses/global-affairs-politics-ma/) |

##### History

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | History and Heritage MA | MA | [Link](https://www.derby.ac.uk/postgraduate/history-courses/history-heritage-ma/) |

##### Journalism

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Journalism MA | MA | [Link](https://www.derby.ac.uk/postgraduate/journalism-courses/journalism-ma/) |

##### Law

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Legal Practice (SQE) LLM | LLM | [Link](https://www.derby.ac.uk/postgraduate/law-courses/llm-legal-practice-sqe/) |
| 2 | LLM (including specialist pathways) | LLM | [Link](https://www.derby.ac.uk/postgraduate/law-courses/llm/) |

##### Midwifery

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Midwifery (Pre-registration) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/midwifery-courses/midwifery-pre-registration-msc/) |

##### Music Production

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Music Production MA | MA | [Link](https://www.derby.ac.uk/postgraduate/music-music-production-courses/music-production-ma/) |

##### Nursing and Health Care Practice

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Clinical Practice MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/advanced-practice-msc/) |
| 2 | Nursing (Adult) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/nursing-adult-msc/) |
| 3 | Nursing (Mental Health) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/nursing-mental-health-msc/) |
| 4 | Specialist Community Public Health Nursing (Health Visiting or Occupational Health Nursing or School Nursing) PG Dip | — | [Link](https://www.derby.ac.uk/postgraduate/nursing-health-care-practice-courses/specialist-community-public-health-nursing-pg-dip/) |

##### Occupational Therapy

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Occupational Therapy (Pre-registration) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/occupational-therapy-courses/occupational-therapy-pre-registration-msc/) |

##### Performing Arts and Theatre

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Theatre and Education MA | MA | [Link](https://www.derby.ac.uk/postgraduate/performing-arts-theatre-courses/applied-theatre-and-education-ma/) |

##### Psychology

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Behaviour Change (incorporating PG Dip/PG Cert) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/psychology-courses/behaviour-change-msc/) |
| 2 | Forensic Psychology MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/psychology-courses/forensic-psychology-msc/) |
| 3 | Health Psychology MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/psychology-courses/health-psychology-msc/) |
| 4 | Psychology MRes | — | [Link](https://www.derby.ac.uk/postgraduate/psychology-courses/psychology-mres/) |

##### Public Health and Social Care

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Communicable Diseases Continuing Professional Development (Postgraduate) | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/communicable-diseases-continuing-professional-development-postgraduate/) |
| 2 | Community Health Promotion Continuing Professional Development (Postgraduate) | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/community-health-promotion-continuing-professional-development-postgraduate/) |
| 3 | Health and Care (Allied Health Professions) MRes | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/health-care-allied-health-professions-mres/) |
| 4 | Health and Care (Nursing and Midwifery) MRes | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/health-care-nursing-midwifery-mres/) |
| 5 | Health and Care (Public Health) MRes | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/health-care-public-health-mres/) |
| 6 | Leadership in Health and Social Care MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/leadership-in-health-and-social-care-msc/) |
| 7 | Master of Public Health | — | [Link](https://www.derby.ac.uk/postgraduate/public-health-social-care-courses/public-health-masters/) |

##### Radiography

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Bone Densitometry Reporting PG Cert | — | [Link](https://www.derby.ac.uk/postgraduate/radiography-courses/bone-densitometry-reporting-pg-cert/) |
| 2 | Diagnostic Radiography (Pre-Registration) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/radiography-courses/diagnostic-radiography-msc/) |
| 3 | Medical Ultrasound MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/radiography-courses/medical-ultrasound-msc/) |
| 4 | Osteoporosis and Falls Management PG Cert | — | [Link](https://www.derby.ac.uk/postgraduate/radiography-courses/osteoporosis-falls-management-pg-cert/) |

##### Sport and Exercise

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Practitioner Development PG Cert | — | [Link](https://www.derby.ac.uk/postgraduate/sport-exercise-courses/applied-practitioner-development-pgcert/) |
| 2 | Applied Sport and Exercise Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/sport-exercise-courses/applied-sport-exercise-science-msc/) |
| 3 | Clinical Exercise Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/sport-exercise-courses/clinical-exercise-science-msc/) |
| 4 | Sport and Exercise Medicine MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/sport-exercise-courses/sport-exercise-medicine-msc/) |
| 5 | Strength and Conditioning MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/sport-exercise-courses/strength-conditioning-msc/) |

##### Therapeutic Practice

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Art Therapy MA | MA | [Link](https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/art-therapy-ma/) |
| 2 | Dance Movement Psychotherapy MA | MA | [Link](https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/dance-movement-psychotherapy-ma/) |
| 3 | Dramatherapy MA | MA | [Link](https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/dramatherapy-ma/) |
| 4 | Music Therapy MA | MA | [Link](https://www.derby.ac.uk/postgraduate/therapeutic-practice-courses/music-therapy-ma/) |


#### College of Science and Engineering

##### Acoustics

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Applied Acoustics MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/acoustics-courses/applied-acoustics-msc/) |

##### Architecture and Architectural Technology

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Building Information Modelling (BIM) and Project Collaboration MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/building-info-modelling-project-collab-msc/) |
| 2 | CAD Presentation, Integration and Visualisation Certificate of Credit | — | [Link](https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/cad-presentation-integration-visualisation-certificate-of-credit/) |
| 3 | Computational Design Certificate of Credit | — | [Link](https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/certificate-of-credit-in-computational-design/) |
| 4 | Computer Aided Design PG Cert | — | [Link](https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/postgraduate-certificate-computer-aided-design/) |
| 5 | Sustainable Architecture and Healthy Buildings MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/architecture-architectural-technology-courses/sustainable-architecture-healthy-buildings-msc/) |

##### Biology and Zoology

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Conservation Biology MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/biology-zoology-courses/conservation-biology-msc/) |
| 2 | Environmental Assessment and Control MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/biology-zoology-courses/environmental-assessment-control-msc/) |

##### Biomedical Science

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/biomedical-science-courses/biomedical-science-msc/) |
| 2 | Molecular Medicine MRes | — | [Link](https://www.derby.ac.uk/postgraduate/biomedical-science-courses/molecular-medicine-mres/) |

##### Civil Engineering and Construction

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Civil Engineering and Construction Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/civil-engineering-construction-courses/civil-engineering-msc/) |

##### Computing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Cyber Security MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/computing-courses/cyber-security-msc/) |
| 2 | Advanced Data Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/computing-courses/advanced-data-science-msc/) |
| 3 | Applied Data Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/computing-courses/applied-data-science-msc/) |
| 4 | Information Technology MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/computing-courses/information-technology-msc/) |

##### Electrical and Electronic Engineering

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Control and Instrumentation MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/electrical-electronic-engineering-courses/control-instrumentation-msc/) |
| 2 | Mechatronics MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/electrical-electronic-engineering-courses/mechatronics-msc/) |

##### Entertainment Engineering

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Audio Engineering MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/entertainment-engineering-courses/audio-engineering-msc/) |

##### Forensic Science

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Forensic Science MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/forensic-science-courses/forensic-science-msc/) |

##### Mechanical and Manufacturing Engineering

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Advanced Engineering Materials MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/advanced-engineering-materials-msc/) |
| 2 | Mechanical and Manufacturing Engineering MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/mechanical-manufacturing-engineering-msc/) |
| 3 | Nuclear Product Engineering for Power Generation (Level 7) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/nuclear-product-engineering-for-power-generation-level7-msc/) |
| 4 | Strategic Engineering Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/mechanical-manufacturing-engineering-courses/strategic-engineering-management-msc/) |


#### Derby International Business School

##### Accounting

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Accounting and Finance MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/accounting-courses/accounting-finance-msc/) |

##### Business

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Analytics MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/business-analytics-msc/) |
| 2 | Doctorate in Business Administration DBA | — | [Link](https://www.derby.ac.uk/postgraduate/business-courses/business-administration-doctorate/) |
| 3 | Economics and Finance MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/economics-and-finance-msc/) |
| 4 | Economics and International Business MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/economics-international-business-msc/) |
| 5 | International Business and Finance MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/international-business-finance-msc/) |
| 6 | International Business and HRM MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/international-business-hrm-msc/) |
| 7 | International Business and Marketing MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/international-business-marketing-msc/) |
| 8 | International Business MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/international-business-msc/) |
| 9 | Leadership and Management (Block Delivery) MRes | — | [Link](https://www.derby.ac.uk/postgraduate/business-courses/leadership-and-management-mres-block-delivery/) |
| 10 | Leadership and Management MRes | — | [Link](https://www.derby.ac.uk/postgraduate/business-courses/leadership-management-mres/) |
| 11 | Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/management-msc/) |
| 12 | Master of Business Administration (MBA Global Block Delivery) MBA | MBA | [Link](https://www.derby.ac.uk/postgraduate/business-courses/mba-block-delivery/) |
| 13 | Master of Business Administration - MBA Global MBA | MBA | [Link](https://www.derby.ac.uk/postgraduate/business-courses/mba/) |
| 14 | MBA Professional | MBA | [Link](https://www.derby.ac.uk/postgraduate/business-courses/mba-professional/) |
| 15 | Sustainable and Ethical Business Management (Block Delivery) MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/msc-sustainable-and-ethical-business-management-block-delivery/) |
| 16 | Sustainable and Ethical Business Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/business-courses/sustainable-and-ethical-business-management-msc/) |

##### Human Resource Management

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Human Resource Management (CIPD accredited) PG Dip | — | [Link](https://www.derby.ac.uk/postgraduate/human-resource-management-courses/cipd-approved-human-resource-management-pg-dip/) |
| 2 | Human Resource Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/human-resource-management-courses/human-resource-management-msc/) |

##### International Hospitality and Tourism Management

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | International Hospitality and Tourism Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/international-hospitality-and-tourism-management-courses/international-hospitality-and-tourism-management-msc/) |

##### Logistics and Supply Chain Management

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Global Operations and Supply Chain Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/logistics-supply-chain-management-courses/global-operations-supply-chain-management-msc/) |

##### Marketing

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Digital Marketing MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/marketing-courses/digital-marketing-msc/) |
| 2 | Marketing Management MSc | MSc | [Link](https://www.derby.ac.uk/postgraduate/marketing-courses/marketing-management-msc/) |


#### Institute of Education

##### Education

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Education (with optional pathways) MA | MA | [Link](https://www.derby.ac.uk/postgraduate/education-courses/education-ma/) |
| 2 | Education (Workplace Contract) MA | MA | [Link](https://www.derby.ac.uk/postgraduate/education-courses/education-ma-workplace-contract/) |
| 3 | Teaching English to Speakers of Other Languages (TESOL) MA | MA | [Link](https://www.derby.ac.uk/postgraduate/education-courses/teaching-english-speakers-other-languages-tesol-ma/) |

##### Teacher Training

| # | 专业 | 学位 | URL |
|---|------|------|-----|
| 1 | Assessment Only Route to Qualified Teacher Status (QTS) | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/qualified-teacher-status-assessment-only-route/) |
| 2 | PGCE (Non-QTS) PGCE | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/education-non-qts-pg-cert/) |
| 3 | Post-14 Further Education and Skills PGCE | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/pgce-post-14/) |
| 4 | Primary (Provider-Led, School-based) with Qualified Teacher Status PGCE | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/pgce-primary-school-based/) |
| 5 | Primary (Provider-led, University based) with Qualified Teacher Status PGCE | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/pgce-primary/) |
| 6 | Secondary (Provider-Led, School-based) with Qualified Teacher Status PGCE | — | [Link](https://www.derby.ac.uk/postgraduate/teacher-training-courses/pgce-secondary-school-based/) |


---

## SECTION 3 — Application requirements & deadlines

### 3.1 英语语言要求 (English language requirements)

For most bachelors degree programmes and above, the standard requirement is **IELTS 6.0 to 7.0** with minimum component scores.

| IELTS Level | Overall | Minimum Component | Typical Use |
|-------------|---------|-------------------|-------------|
| Level 1 | 6.0 | 5.5 in all components | Most UG programmes |
| Level 2 | 6.5 | 5.5 in all components | Some UG/PG programmes |
| Level 3 | 6.5 | 6.0 in all components | Some PG programmes |
| Level 4 | 7.0 | 6.5 in all components | Health/teaching programmes |

#### Accepted English Language Tests

| 测试 | Level 1 (6.0/5.5) | Level 2 (6.5/5.5) | Level 3 (6.5/6.0) | Level 4 (7.0/6.5) | SELT |
|------|-------------------|-------------------|-------------------|-------------------|------|
| IELTS for UKVI | 6.0 with 5.5 | 6.5 with 5.5 | 6.5 with 6.0 | 7.0 with 6.5 | Yes |
| IELTS Academic | 6.0 with 5.5 | 6.5 with 5.5 | 6.5 with 6.0 | 7.0 with 6.5 | No |
| Pearson PTE Academic UKVI | 59 (min 59 each) | 65 (min 59 each) | 71 (min 65 each) | 76 (min 65 each) | Yes |
| Pearson PTE Academic | 59 (min 59 each) | 65 (min 59 each) | 71 (min 65 each) | 76 (min 65 each) | No |
| TOEFL iBT | 79 | 81 | 87 | 100 | No |
| Oxford ELLT | 6 (min 5 each) | 7 (min 5 each) | 7 (min 6 each) | 8 (min 7 each) | No |
| Pearson IGCSE English | Grade C/4 | Grade C/4 | Grade C/4 | Grade B/3 | No |

> **Source**: https://www.derby.ac.uk/life/international-students/applicants/english-language-tests/

### 3.2 国际入学要求 (International entry requirements)

Derby provides country-specific entry requirements. Multiple entry pathways available:

- **International Foundation Programme (IFP)**: Additional preparation before UG study
- **Foundation Pathway Programme (FPP)**: Alternative foundation route
- **Undergraduate with Foundation Year**: Integrated 4-year programme
- **Undergraduate (1st year entry)**: Direct entry with recognised qualifications
- **Undergraduate (3rd year/top-up entry)**: Direct entry to final year
- **Postgraduate**: Entry with bachelor's degree (typically 2:2 or 2:1 equivalent)

> **Source**: https://www.derby.ac.uk/undergraduate/apply/entry-requirements/international/

### 3.3 申请流程 (Application process)

- **Undergraduate**: Apply via UCAS (institution code D39)
- **Postgraduate**: Apply directly via the university website
- **Clearing**: Available for 2026 entry (open as of July 2026)

---

## SECTION 4 — Costs & financial aid

### 4.1 学费 (Tuition fees)

| 费用类别 | 2025/26 | 2026/27 |
|---------|---------|--------|
| **UK (Home) UG** | £9,535/year | £9,790/year |
| **International UG (on-campus)** | £16,900/year | £17,500/year |
| **PG (varies by course)** | Varies | Varies |
| **Online courses** | Typically lower | Varies |

> **Note**: UK fees are regulated by the government. International fees may vary by course. Check individual course pages for exact PG fees.

### 4.2 奖学金与资助 (Scholarships and financial aid)

- **Vice-Chancellor's Scholarship**: £2,000 fee reduction for eligible international students
- **Alumni Discount**: 25% discount for Derby graduates pursuing PG study
- **Postgraduate Masters Loan**: Up to £13,206 for eligible students
- Scholarships not available for online studies, foundation, and pre-sessional programmes

> **Source**: https://www.derby.ac.uk/study/fees-finance/scholarships/

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Derby"
  source_url: https://www.derby.ac.uk
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: course.total_count
  value: 509 (297 UG + 104 PG + 108 Online)
  source_url: https://www.derby.ac.uk/courses/a-z/
  capture_date: 2026-07-08

E-U-003:
  field: fees.ug_international
  value: "£16,900 (2025/26), £17,500 (2026/27)"
  source_url: https://www.derby.ac.uk/undergraduate/fees-and-finance/
  capture_date: 2026-07-08

E-U-004:
  field: english_language.ielts
  value: "IELTS 6.0-7.0 depending on programme"
  source_url: https://www.derby.ac.uk/life/international-students/applicants/english-language-tests/
  capture_date: 2026-07-08
```

---

## SECTION 6 — WeKnora import manifest

```yaml
document_id: derby-uk-v2.0
university: University of Derby
country: UK
region: East Midlands, England
ucas_code: D39
total_programmes: 509
ug_programmes: 297
pg_programmes: 104
online_programmes: 108
colleges: 4
academic_schools: 7
ug_subject_areas: 40
capture_date: 2026-07-08
document_version: v2.0
schema_version: weknora-2.0
```

---

## SECTION 7 — Notes and limitations

1. **Online courses**: 108 online courses listed separately, may overlap with campus-based offerings.
2. **Foundation year variants**: 90 UG programmes offer foundation year variants as separate entries.
3. **Placement year variants**: 24 UG programmes offer placement year variants.
4. **Top-up degrees**: 20 programmes for students with prior qualifications.
5. **Joint honours**: 49 combinations available across subject areas.
6. **PG fees**: Vary by course; individual course pages should be consulted.
7. **Integrated master's**: MSci, MArts, MEdu are 4-year undergraduate degrees.
8. **Clearing 2026**: Open as of capture date.
9. **Professional accreditation**: Many programmes hold professional body accreditations (BCS, RIBA, HCPC, etc.) - verify on individual course pages.
