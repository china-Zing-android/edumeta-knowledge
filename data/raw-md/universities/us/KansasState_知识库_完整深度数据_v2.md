# Kansas State University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/Accelerated BS+MS) | 115 |
| 本科辅修 (Minor) | 20+ (Minors listed across multiple colleges; precise list on `catalog.k-state.edu`) |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/EdD/DNP/MPAS) | 110 |
| 研究生高级证书 (Graduate Certificate) | 24 |
| **学位项目总计 (UG + Grad + Certificates)** | **~250** |
| 学院 / 独立系所总数 | 10 colleges + 60 departments |

### 0.2 学院 / 系层级结构

```
Kansas State University
├── College of Agriculture                              [学院] https://www.ag.k-state.edu/
│   ├── Agricultural Economics                          [系]
│   ├── Agronomy                                        [系]
│   ├── Animal Sciences and Industry                    [系]
│   ├── Communications and Agricultural Education       [系]
│   ├── Entomology                                      [系]
│   ├── Food Science Institute                          [系]
│   ├── Grain and Food Science                          [系]
│   ├── Horticulture and Natural Resources              [系]
│   └── Plant Pathology                                 [系]
├── College of Architecture, Planning and Design        [学院] https://apdesign.k-state.edu/
│   ├── Architecture                                    [系]
│   ├── Interior Architecture & Industrial Design       [系]
│   ├── Landscape Architecture/Regional & Community Plan[系]
│   └── Architectural Engineering and Construction Science [系]  ⚠ shared with College of Engineering
├── College of Arts and Sciences                        [学院] https://cas.k-state.edu/
│   ├── Aerospace Studies                               [系]
│   ├── Art                                             [系]
│   ├── Biochemistry and Molecular Biophysics           [系]
│   ├── Biology                                         [系]
│   ├── Chemistry                                       [系]
│   ├── Economics                                       [系]
│   ├── English                                         [系]
│   ├── Geography and Geospatial Sciences               [系]
│   ├── Geology                                         [系]
│   ├── History                                         [系]
│   ├── Mathematics                                     [系]
│   ├── Media and Communication                         [系]
│   ├── Military Science                                [系]
│   ├── Modern Languages                                [系]
│   ├── Music, Theatre and Dance, School of             [系]
│   ├── Philosophy                                      [系]
│   ├── Physics                                         [系]
│   ├── Political Science                               [系]
│   ├── Psychological Sciences                          [系]
│   ├── Social Transformation Studies                   [系]
│   ├── Sociology, Anthropology, and Social Work        [系]
│   └── Statistics                                      [系]
├── College of Business Administration                 [学院] https://cba.k-state.edu/
│   ├── Accountancy, School of                          [系]
│   ├── Finance                                         [系]
│   ├── Management                                      [系]
│   └── Marketing                                       [系]
├── College of Education                                [学院] https://coe.k-state.edu/
│   ├── Curriculum and Instruction                      [系]
│   ├── Educational Leadership                          [系]
│   ├── Special Education, Counseling and Student Affairs[系]
│   └── Staley School of Leadership                     [系]
├── Carl R. Ice College of Engineering                  [学院] https://engr.k-state.edu/
│   ├── Architectural Engineering and Construction Science [系]  ⚠ shared with APDesign
│   ├── Biological and Agricultural Engineering         [系]
│   ├── Chemical Engineering                            [系]
│   ├── Civil Engineering                               [系]
│   ├── Computer Science                                [系]
│   ├── Electrical and Computer Engineering             [系]
│   ├── Industrial and Manufacturing Systems Engineering [系]
│   └── Mechanical and Nuclear Engineering              [系]
├── College of Health and Human Sciences                [学院] https://www.hhs.k-state.edu/
│   ├── Anatomy and Physiology                          [系]
│   ├── Food, Nutrition, Dietetics and Health           [系]
│   ├── Hospitality Management                          [系]
│   ├── Kinesiology                                     [系]
│   ├── Personal Financial Planning                     [系]
│   ├── School of Consumer Sciences                     [系]
│   ├── School of Health Sciences                       [系]
│   └── School of Human Sciences                        [系]
├── College of Technology and Aviation (Salina)         [学院] https://salina.k-state.edu/
│   ├── Aviation                                        [系]
│   └── Integrated Studies                              [系]
├── College of Veterinary Medicine                      [学院] https://www.vet.k-state.edu/
│   ├── Clinical Sciences                               [系]
│   └── Diagnostic Medicine/Pathobiology                [系]
└── Graduate School                                     [学院] https://www.k-state.edu/grad/
    └── (cross-college graduate programs; all departments listed above grant graduate degrees)
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 99+ |
| BA | Bachelor of Arts | 本科 | 14+ |
| BFA | Bachelor of Fine Arts | 本科 | 2 (Art, Music) |
| Minor | Undergraduate Minor | 本科辅修 | 20+ |
| Undergraduate Certificate | Undergraduate Certificate | 本科证书 | 7+ |
| Accelerated Bachelor's/Master's | 加速本硕连读 | 本科+研究生 | 8+ |
| MS | Master of Science | 研究生 | 50+ |
| MA | Master of Arts | 研究生 | 25+ |
| MBA | Master of Business Administration | 研究生 | 3 (MBA, Prof MBA, Agribusiness) |
| MArch | Master of Architecture | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| MEng / MNE / MIE / MARE | 专业硕士 (Engineering) | 研究生 | 6 |
| MPAS | Master of Physician Assistant | 研究生 | 1 |
| MPH | Master of Public Health | 研究生 | 1 |
| PhD | Doctor of Philosophy | 研究生 | 35+ |
| EdD | Doctor of Education | 研究生 | 3 (Ed Leadership, Curriculum & Instruction, Community College Leadership) |
| Graduate Certificate | 研究生证书 | 研究生 | 24 |
| DVM | Doctor of Veterinary Medicine | 专业博士 | 1 (College of Vet Med) |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | MA | MS | MBA | PhD | EdD | Grad Cert | DVM | 合计 |
|------------|----|----|----|----|-----|-----|-----|-----------|-----|------|
| Agriculture | 0 | 11 | 1 | 7 | 1 | 6 | 0 | 6 | 0 | 32 |
| Architecture, Planning & Design | 3 | 3 | 4 | 0 | 0 | 1 | 0 | 1 | 0 | 12 |
| Arts & Sciences | 14 | 22 | 8 | 8 | 0 | 7 | 0 | 4 | 0 | 63 |
| Business Administration | 0 | 6 | 0 | 0 | 3 | 0 | 0 | 1 | 0 | 10 |
| Education | 0 | 5 | 1 | 1 | 0 | 0 | 3 | 3 | 0 | 13 |
| Engineering | 0 | 11 | 0 | 10 | 0 | 8 | 0 | 2 | 0 | 31 |
| Health and Human Sciences | 0 | 11 | 2 | 5 | 0 | 1 | 0 | 2 | 0 | 21 |
| Technology and Aviation (Salina) | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 5 |
| Veterinary Medicine | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 5 |
| **合计** | **17** | **74** | **17** | **32** | **4** | **24** | **3** | **19** | **1** | **~191** |

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

K-State has 9 degree-granting undergraduate colleges plus the Graduate School. The college structure is documented in Section 0.2.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture (https://www.ag.k-state.edu/)

##### Department of Agricultural Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness | https://www.k-state.edu/academics/majors-programs/agribusiness-degree/ |
| 2 | Agricultural Economics | https://www.k-state.edu/academics/majors-programs/agricultural-economics-degree/ |

###### Accelerated BS/MS
| # | 专业 | URL |
|---|------|-----|
| 3 | Agricultural Economics (Accelerated bachelor's/master's) | https://catalog.k-state.edu/programs/BAGEC/about-the-program-aoYks |

##### Department of Agronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Agronomy | https://www.k-state.edu/academics/majors-programs/agronomy-degree/ |

##### Department of Animal Sciences and Industry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 5 | Animal Sciences and Industry | https://www.k-state.edu/academics/majors-programs/animal-sciences-industry-degree/ |
| 6 | Animal Sciences and Industry (Online) | https://online.k-state.edu/programs/animal-science-industry-bachelors/ |
| 7 | Food Science and Industry | https://www.k-state.edu/academics/majors-programs/food-science-industry-degree/ |

###### Accelerated BS/MBA
| # | 专业 | URL |
|---|------|-----|
| 8 | Animal Sciences and Industry and Master of Business Administration | https://catalog.k-state.edu/programs/BASI/about-the-program-aoYks |

##### Department of Communications and Agricultural Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Agricultural Education | https://www.k-state.edu/academics/majors-programs/agricultural-education-degree/ |
| 10 | Agricultural Education (Online) | https://online.k-state.edu/programs/ag-education-bachelors/ |
| 11 | Agricultural and Natural Resources Communications | https://www.k-state.edu/academics/majors-programs/agricultural-communications-journalism-degree/ |

##### Department of Horticulture and Natural Resources
###### BS
| # | 专业 | URL |
|---|------|-----|
| 12 | General Agriculture | https://www.k-state.edu/academics/majors-programs/agriculture-degree/ |
| 13 | Horticulture | https://www.k-state.edu/academics/majors-programs/horticulture-degree/ |
| 14 | Park Management and Conservation | https://www.k-state.edu/academics/majors-programs/park-management-conservation-degree/ |
| 15 | Wildlife and Outdoor Enterprise Management | https://www.k-state.edu/academics/majors-programs/wildlife-outdoor-management-degree/ |

##### Department of Entomology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 16 | Entomology | https://www.k-state.edu/academics/majors-programs/entomology-degree/ |

##### Department of Grain and Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 17 | Bakery Science and Management | https://www.k-state.edu/academics/majors-programs/bakery-science-degree/ |
| 18 | Feed and Pet Food Science | https://www.k-state.edu/academics/majors-programs/feed-science-management-degree/ |
| 19 | Milling Science and Management | https://www.k-state.edu/academics/majors-programs/milling-science-management-degree/ |

#### College of Architecture, Planning and Design (https://apdesign.k-state.edu/)

##### Department of Architecture
###### BARCH (Bachelor of Architecture)
| # | 专业 | URL |
|---|------|-----|
| 20 | Architecture | https://www.k-state.edu/academics/majors-programs/architecture-degree/ |

##### Department of Interior Architecture and Industrial Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 21 | Industrial Design | https://www.k-state.edu/academics/majors-programs/industrial-design-degree/ |
| 22 | Interior Architecture | https://www.k-state.edu/academics/majors-programs/interior-architecture-product-design-degree/ |
| 23 | Interior Design | https://www.k-state.edu/academics/majors-programs/interior-design-degree/ |

##### Department of Landscape Architecture/Regional and Community Planning
###### BS
| # | 专业 | URL |
|---|------|-----|
| 24 | Landscape Architecture | https://www.k-state.edu/academics/majors-programs/landscape-architecture-degree/ |
| 25 | Regional and Community Planning | https://www.k-state.edu/academics/majors-programs/regional-community-planning-degree/ |

##### Department of Architectural Engineering (joint with Engineering)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 26 | Architectural Engineering | https://www.k-state.edu/academics/majors-programs/architectural-engineering-degree/ |

#### College of Arts and Sciences (https://cas.k-state.edu/)

##### Department of Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 27 | Art | https://www.k-state.edu/academics/majors-programs/art-degree/ |

##### Department of Biochemistry and Molecular Biophysics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 28 | Biochemistry | https://www.k-state.edu/academics/majors-programs/biochemistry-degree/ |

##### Department of Biology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 29 | Biology | https://www.k-state.edu/academics/majors-programs/biology-degree/ |
| 30 | Fisheries, Wildlife, Conservation, and Environmental Biology | https://www.k-state.edu/academics/majors-programs/biology-degree/index.html |
| 31 | Life Science | https://www.k-state.edu/academics/majors-programs/life-science-degree/ |
| 32 | Microbiology | (via Biology dept) https://www.k-state.edu/academics/majors-programs/biology-degree/ |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 33 | Chemistry | https://www.k-state.edu/academics/majors-programs/chemistry-degree/ |

##### Department of Economics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 34 | Economics | https://www.k-state.edu/academics/majors-programs/economics-degree/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 35 | English | https://www.k-state.edu/academics/majors-programs/english-degree/ |

##### Department of Geography and Geospatial Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 36 | Geography | https://www.k-state.edu/academics/majors-programs/geography-degree/ |

##### Department of Geology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 37 | Geology | https://www.k-state.edu/academics/majors-programs/geology-degree/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 38 | History | https://www.k-state.edu/academics/majors-programs/history-degree/index.html |

##### Department of Mathematics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 39 | Mathematics | https://www.k-state.edu/academics/majors-programs/mathematics-degree/ |
| 40 | Statistics and Data Science | https://www.k-state.edu/academics/majors-programs/statistics-data-science-degree/ |

##### Department of Media and Communication
###### BS
| # | 专业 | URL |
|---|------|-----|
| 41 | Advertising and Public Relations | https://www.k-state.edu/academics/majors-programs/advertising-public-relations-degree/ |
| 42 | Communication Studies | https://www.k-state.edu/academics/majors-programs/communication-studies-degree/ |
| 43 | Digital Innovation in Media | https://www.k-state.edu/academics/majors-programs/digital-innovation-media-degree/ |
| 44 | News and Sports Media | https://www.k-state.edu/academics/majors-programs/news-sports-media-degree/ |

##### Department of Modern Languages
###### BA
| # | 专业 | URL |
|---|------|-----|
| 45 | Modern Languages (Chinese Studies track) | https://www.k-state.edu/academics/majors-programs/modern-languages-degree/ |

##### School of Music, Theatre and Dance
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 46 | Music | https://www.k-state.edu/academics/majors-programs/music-degree/ |
| 47 | Theatre | https://www.k-state.edu/academics/majors-programs/theatre-degree/ |
| 48 | Dance | https://www.k-state.edu/academics/majors-programs/dance-degree/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 49 | Philosophy | https://www.k-state.edu/academics/majors-programs/philosophy-degree/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 50 | Physical Science | https://www.k-state.edu/academics/majors-programs/physical-science-degree/ |
| 51 | Physics | https://www.k-state.edu/academics/majors-programs/physics-degree/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 52 | Political Science | https://www.k-state.edu/academics/majors-programs/political-science-degree/ |

##### Department of Psychological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 53 | Psychology | https://www.k-state.edu/academics/majors-programs/psychology-degree/ |

##### Department of Social Transformation Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 54 | Social Transformation Studies | https://www.k-state.edu/academics/majors-programs/social-transformation-studies-degree/ |

##### Department of Sociology, Anthropology, and Social Work
###### BA
| # | 专业 | URL |
|---|------|-----|
| 55 | Anthropology | https://www.k-state.edu/academics/majors-programs/anthropology-degree/ |
| 56 | Criminology | https://www.k-state.edu/academics/majors-programs/criminology-degree/ |
| 57 | Social Work | https://www.k-state.edu/academics/majors-programs/social-work-degree/ |
| 58 | Sociology | https://www.k-state.edu/academics/majors-programs/sociology-degree/ |

#### College of Business Administration (https://cba.k-state.edu/)

##### School of Accountancy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 59 | Accounting | https://www.k-state.edu/academics/majors-programs/accounting-degree/ |
| 60 | Accounting (Online) | https://online.k-state.edu/programs/accounting-bachelors/ |

###### Accelerated BS/MAcc
| # | 专业 | URL |
|---|------|-----|
| 61 | Accounting and Master of Accountancy | https://catalog.k-state.edu/programs/LACCTG/about-the-program-aoYks |

##### Department of Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 62 | Finance | https://www.k-state.edu/academics/majors-programs/finance-degree/ |
| 63 | Personal Financial Planning | https://www.k-state.edu/academics/majors-programs/personal-financial-planning-degree/ |

##### Department of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 64 | Entrepreneurship | https://www.k-state.edu/academics/majors-programs/entrepreneurship-degree/ |
| 65 | Management | https://www.k-state.edu/academics/majors-programs/management-degree/ |
| 66 | Management Information Systems | https://www.k-state.edu/academics/majors-programs/management-information-systems-degree/ |
| 67 | Professional Strategic Selling | https://www.k-state.edu/academics/majors-programs/professional-strategic-selling-degree/ |

##### Department of Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 68 | Marketing | https://www.k-state.edu/academics/majors-programs/marketing-degree/ |

#### College of Education (https://coe.k-state.edu/)

##### Department of Curriculum and Instruction
###### BS
| # | 专业 | URL |
|---|------|-----|
| 69 | Early Childhood Education | https://www.k-state.edu/academics/majors-programs/early-childhood-education-degree/ |
| 70 | Elementary Education | https://www.k-state.edu/academics/majors-programs/elementary-education-degree/ |
| 71 | Secondary Education | https://www.k-state.edu/academics/majors-programs/secondary-education-degree/ |
| 72 | Educational Studies | https://www.k-state.edu/academics/majors-programs/educational-studies-degree/ |
| 73 | Family and Consumer Sciences Education | https://www.k-state.edu/academics/majors-programs/family-consumer-sciences-education-degree/ |

#### Carl R. Ice College of Engineering (https://engr.k-state.edu/)

##### Department of Biological and Agricultural Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 74 | Biological Systems Engineering | https://www.k-state.edu/academics/majors-programs/biological-systems-engineering-degree/ |

##### Department of Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 75 | Chemical Engineering | https://www.k-state.edu/academics/majors-programs/chemical-engineering-degree/ |

##### Department of Civil Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 76 | Civil Engineering | https://www.k-state.edu/academics/majors-programs/civil-engineering-degree/ |
| 77 | Construction Science and Management | https://www.k-state.edu/academics/majors-programs/construction-science-management-degree/ |
| 78 | Environmental Engineering | https://www.k-state.edu/academics/majors-programs/environmental-engineering-degree/ |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 79 | Computer Science | https://www.k-state.edu/academics/majors-programs/computer-science-degree/ |
| 80 | Cybersecurity | https://www.k-state.edu/academics/majors-programs/cybersecurity-degree/ |
| 81 | Integrated Computer Science | https://www.k-state.edu/academics/majors-programs/integrated-computer-science-degree/ |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 82 | Computer Engineering | https://www.k-state.edu/academics/majors-programs/computer-engineering-degree/ |
| 83 | Electrical Engineering | https://www.k-state.edu/academics/majors-programs/electrical-engineering-degree/ |

##### Department of Industrial and Manufacturing Systems Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 84 | Industrial Engineering | https://www.k-state.edu/academics/majors-programs/industrial-engineering-degree/ |

##### Department of Mechanical and Nuclear Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 85 | Biomedical Engineering | https://www.k-state.edu/academics/majors-programs/biomedical-engineering-degree/ |
| 86 | Mechanical Engineering | https://www.k-state.edu/academics/majors-programs/mechanical-engineering-degree/ |
| 87 | Nuclear Engineering | https://www.k-state.edu/academics/majors-programs/nuclear-engineering-degree/ |

#### College of Health and Human Sciences (https://www.hhs.k-state.edu/)

##### Department of Food, Nutrition, Dietetics and Health
###### BS
| # | 专业 | URL |
|---|------|-----|
| 88 | Dietetics | https://www.k-state.edu/academics/majors-programs/dietetics-degree/ |
| 89 | Nutrition and Health | https://www.k-state.edu/academics/majors-programs/nutrition-health-degree/ |
| 90 | Nutritional Sciences | https://www.k-state.edu/academics/majors-programs/nutritional-sciences-degree/ |
| 91 | Sports Nutrition | https://www.k-state.edu/academics/majors-programs/sports-nutrition-degree/ |

##### Department of Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 92 | Hospitality Management | https://www.k-state.edu/academics/majors-programs/hospitality-management-degree/ |

##### Department of Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 93 | Athletic Training and Rehabilitation Sciences | https://www.k-state.edu/academics/majors-programs/athletic-training-degree/ |
| 94 | Integrative Physiology | https://www.k-state.edu/academics/majors-programs/integrative-physiology-degree/ |
| 95 | Kinesiology | https://www.k-state.edu/academics/majors-programs/kinesiology-degree/ |

##### School of Consumer Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 96 | Communication Sciences and Disorders | https://www.k-state.edu/academics/majors-programs/communication-sciences-disorders-degree/ |
| 97 | Human Development and Family Science | https://www.k-state.edu/academics/majors-programs/human-development-family-science-degree/ |
| 98 | Integrative Human Sciences | https://www.k-state.edu/academics/majors-programs/integrative-human-sciences-degree/ |

##### School of Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 99 | Medical Laboratory Science | https://www.k-state.edu/academics/majors-programs/medical-laboratory-science-degree/ |
| 100 | Public Health | https://www.k-state.edu/academics/majors-programs/public-health-degree/ |

##### School of Human Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 101 | Addiction Counseling | https://www.k-state.edu/academics/majors-programs/addiction-counseling-degree/ |
| 102 | Addiction Counseling (Online) | https://online.k-state.edu/programs/addiction-counseling-bachelors/ |
| 103 | Social Science | https://www.k-state.edu/academics/majors-programs/social-science-degree/ |

#### College of Technology and Aviation (Salina Campus, https://salina.k-state.edu/)

##### Department of Aviation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 104 | Professional Pilot (selective) | https://salina.k-state.edu/ (Professional Pilot, College of Technology and Aviation) |

##### Department of Integrated Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 105 | Engineering Technology Management | https://www.k-state.edu/academics/majors-programs/engineering-technology-management-degree/ |

##### Cross-college Salina programs
| # | 专业 | URL |
|---|------|-----|
| 106 | Cybersecurity (Salina-based) | https://www.k-state.edu/academics/majors-programs/cybersecurity-degree/ |
| 107 | Integrated Computer Science | https://www.k-state.edu/academics/majors-programs/integrated-computer-science-degree/ |

#### Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 (home) | URL |
|---|------|-------------|-----|
| 108 | Humanities (cross-college) | College of Arts and Sciences | https://www.k-state.edu/academics/majors-programs/humanities-degree/ |
| 109 | Social Science (cross-college) | College of Health and Human Sciences | https://www.k-state.edu/academics/majors-programs/social-science-degree/ |
| 110 | Agricultural and Occupational Safety and Health (Online) | College of Agriculture | https://online.k-state.edu/programs/certificates/undergraduate-certificates/agricultural-occupational-safety-health.html |
| 111 | Animal Health (Online certificate) | College of Agriculture | https://online.k-state.edu/programs/certificates/undergraduate-certificates/animal-health.html |
| 112 | Animal Nutrition (Online certificate) | College of Agriculture | https://online.k-state.edu/programs/certificates/undergraduate-certificates/animal-nutrition.html |
| 113 | Agritourism (UG certificate) | College of Agriculture | https://catalog.k-state.edu/programs/CAGTSM/about-the-program-aoYks |
| 114 | Health Professions (pre-health) | Multiple | https://www.k-state.edu/academics/majors-programs/health-professions/ |
| 115 | Interior Design (selective, fall-only) | College of APDesign | https://www.k-state.edu/academics/majors-programs/interior-design-degree/ |

### 1.3 Minors — complete list (representative subset; full minor list on catalog.k-state.edu)

| # | Minor | Home department | URL |
|---|-------|-----------------|-----|
| 1 | Aerospace Studies | Aerospace Studies | https://catalog.k-state.edu/programs/RAERO/about-the-program-aoYks |
| 2 | African Studies | Arts & Sciences | https://catalog.k-state.edu/programs/RAFRIS/about-the-program-aoYks |
| 3 | Agricultural Sales | Agriculture | https://catalog.k-state.edu/programs/RAGRAS/about-the-program-aoYks |
| 4 | Agricultural Technology Management | Agriculture | https://catalog.k-state.edu/programs/RAGTM/about-the-program-aoYks |
| 5 | American Ethnic Studies | Arts & Sciences | https://online.k-state.edu/programs/concurrent-minors-programs/ |
| 6 | Animal Sciences and Industry | Agriculture | https://online.k-state.edu/programs/concurrent-minors-programs/ |
| 7 | Anthropology | Arts & Sciences | https://online.k-state.edu/programs/concurrent-minors-programs/ |
| 8 | Entomology | Agriculture | https://catalog.k-state.edu/programs/RENTOM/about-the-program-aoYks |
| 9 | Horticulture | Agriculture | https://catalog.k-state.edu/programs/RHORT/about-the-program-aoYks |
| 10 | Plant Pathology | Agriculture | https://catalog.k-state.edu/programs/RPPATH/about-the-program-aoYks |
| 11 | South Asian Studies | Arts & Sciences | https://catalog.k-state.edu/programs/RSASIA/about-the-program-aoYks |
| 12-20+ | Additional minors | Various | https://catalog.k-state.edu/ |

### 1.4 General Education / University-wide requirements

K-State has a K-State 8 General Education program. All undergraduate students must complete the K-State 8 areas:
- Aesthetic Experience
- Empirical and Quantitative Reasoning
- Ethical Responsibility
- Global Issues and Perspectives
- Historical Perspectives
- Human Diversity within the U.S.
- Natural and Physical Sciences
- Social Sciences

Source: https://www.k-state.edu/academics/

### 1.5 Course-ID / Catalog → Major mapping

K-State does not use MIT-style course numbering for majors. Programs are identified by name and college in the catalog (https://catalog.k-state.edu/).

---

## SECTION 2 — Graduate education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Agriculture (https://www.ag.k-state.edu/)

##### MS / MA
| # | 项目 | URL |
|---|------|-----|
| 1 | MS Agronomy | https://catalog.k-state.edu/programs/MAGRON/about-the-program-aoYks |
| 2 | MS Animal Science | https://catalog.k-state.edu/programs/MASC/about-the-program-aoYks |
| 3 | MS Food Science | https://catalog.k-state.edu/programs/MFDSC/about-the-program-aoYks |
| 4 | MS Biological and Agricultural Engineering | https://catalog.k-state.edu/programs/MBAE/about-the-program-aoYks |
| 5 | MS Horticulture and Natural Resources | https://catalog.k-state.edu/programs/MHNR/about-the-program-aoYks |
| 6 | MS Entomology | https://catalog.k-state.edu/programs/MENTOM/about-the-program-aoYks |
| 7 | MS Plant Pathology | https://catalog.k-state.edu/programs/MPPATH/about-the-program-aoYks |
| 8 | MS Agricultural Economics | https://catalog.k-state.edu/programs/MAGEC/about-the-program-aoYks |
| 9 | MAB Agribusiness (Professional MBA / Master of Agribusiness) | https://catalog.k-state.edu/programs/MAGBUS/about-the-program-aoYks |
| 10 | MS Grain Science | https://catalog.k-state.edu/programs/MGRS/about-the-program-aoYks |
| 11 | MA/MFA Fashion Studies | https://catalog.k-state.edu/programs//about-the-program-aoYks |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 12 | PhD Agronomy | https://catalog.k-state.edu/programs/DAGRON/about-the-program-aoYks |
| 13 | PhD Animal Science | https://catalog.k-state.edu/programs/DASC/about-the-program-aoYks |
| 14 | PhD Food Science | https://catalog.k-state.edu/programs/DFDSC/about-the-program-aoYks |
| 15 | PhD Biological and Agricultural Engineering | https://catalog.k-state.edu/programs/DBAE/about-the-program-aoYks |
| 16 | PhD Horticulture and Natural Resources | https://catalog.k-state.edu/programs/DHNR/about-the-program-aoYks |
| 17 | PhD Entomology | https://catalog.k-state.edu/programs/DENTOM/about-the-program-aoYks |
| 18 | PhD Plant Pathology | https://catalog.k-state.edu/programs/DPPATH/about-the-program-aoYks |
| 19 | PhD Agricultural Economics | https://catalog.k-state.edu/programs/DAGEC/about-the-program-aoYks |
| 20 | PhD Grain Science | https://catalog.k-state.edu/programs/DGRS/about-the-program-aoYks |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 21 | Agritourism | https://catalog.k-state.edu/programs/CAGTSM/about-the-program-aoYks |
| 22 | Agricultural Biosecurity Research | https://catalog.k-state.edu/programs/CAGBR/about-the-program-aoYks |
| 23 | Animal Health Management | https://catalog.k-state.edu/programs/CAHM/about-the-program-aoYks |
| 24 | Genetics, Genomics and Biotechnology | https://catalog.k-state.edu/programs/CGGBT/about-the-program-aoYks |
| 25 | Stem Cell Biotechnology | https://catalog.k-state.edu/programs/CSTMBI/about-the-program-aoYks |
| 26 | Sustainable Food, Energy, Water | https://catalog.k-state.edu/programs/CFEW/about-the-program-aoYks |
| 27 | Urban Food Systems | https://catalog.k-state.edu/programs/CUFS/about-the-program-aoYks |
| 28 | Biobased Products and Bioenergy | https://catalog.k-state.edu/programs/CBPBC/about-the-program-aoYks |

#### College of Architecture, Planning and Design (https://apdesign.k-state.edu/)

##### Master's
| # | 项目 | URL |
|---|------|-----|
| 29 | MArch Architecture | https://catalog.k-state.edu/programs/MARMS/about-the-program-aoYks |
| 30 | Master of Landscape Architecture (MLA) | https://catalog.k-state.edu/programs/MLA/about-the-program-aoYks |
| 31 | MS Interior Architecture and Product Design | https://catalog.k-state.edu/programs/MIAPDP/about-the-program-aoYks |
| 32 | MS Industrial Design | https://catalog.k-state.edu/programs/MINDD/about-the-program-aoYks |
| 33 | MS Regional and Community Planning | https://catalog.k-state.edu/programs/MRCP/about-the-program-aoYks |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 34 | PhD Environmental Design and Planning | https://catalog.k-state.edu/programs/DEVD/about-the-program-aoYks |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 35 | Furniture Design | https://catalog.k-state.edu/programs/CFD/about-the-program-aoYks |

#### College of Arts and Sciences (https://cas.k-state.edu/)

##### Master's
| # | 项目 | URL |
|---|------|-----|
| 36 | MA Communication Studies | https://catalog.k-state.edu/programs/MCOMM/about-the-program-aoYks |
| 37 | MS Communication Sciences and Disorders | https://catalog.k-state.edu/programs/MCSD/about-the-program-aoYks |
| 38 | MS Couple and Family Therapy | https://catalog.k-state.edu/programs/MFSHS/about-the-program-aoYks |
| 39 | MA Economics | https://catalog.k-state.edu/programs/MECON/about-the-program-aoYks |
| 40 | MA English | https://catalog.k-state.edu/programs/MENGL/about-the-program-aoYks |
| 41 | MS Geography | https://catalog.k-state.edu/programs/MGEOG/about-the-program-aoYks |
| 42 | MS Geology | https://catalog.k-state.edu/programs/MGEOL/about-the-program-aoYks |
| 43 | MA History | https://catalog.k-state.edu/programs/MHIST/about-the-program-aoYks |
| 44 | MS Mathematics | https://catalog.k-state.edu/programs/MMATH/about-the-program-aoYks |
| 45 | MS Statistics | https://catalog.k-state.edu/programs/MSTAT/about-the-program-aoYks |
| 46 | MS Mass Communications | https://catalog.k-state.edu/programs/MMC/about-the-program-aoYks |
| 47 | MS Modern Languages | https://catalog.k-state.edu/programs/MMLANG/about-the-program-aoYks |
| 48 | MM Music | https://catalog.k-state.edu/programs/MMUSIC/about-the-program-aoYks |
| 49 | MA Theatre | https://catalog.k-state.edu/programs/MTHTRE/about-the-program-aoYks |
| 50 | MS Physics | https://catalog.k-state.edu/programs/MPHYS/about-the-program-aoYks |
| 51 | MS Psychology | https://catalog.k-state.edu/programs/MPSYCH/about-the-program-aoYks |
| 52 | MS Sociology | https://catalog.k-state.edu/programs/MSOCIO/about-the-program-aoYks |
| 53 | MS Biochemistry | https://catalog.k-state.edu/programs/MBIOCH/about-the-program-aoYks |
| 54 | MS Biology | https://catalog.k-state.edu/programs/MBIOL/about-the-program-aoYks |
| 55 | MS Chemistry | https://catalog.k-state.edu/programs/MCHM/about-the-program-aoYks |
| 56 | MS Security Studies | https://catalog.k-state.edu/programs/MSECUR/about-the-program-aoYks |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 57 | PhD Biology | https://catalog.k-state.edu/programs/DBIOL/about-the-program-aoYks |
| 58 | PhD Chemistry | https://catalog.k-state.edu/programs/DCHM/about-the-program-aoYks |
| 59 | PhD Economics | https://catalog.k-state.edu/programs/DECON/about-the-program-aoYks |
| 60 | PhD English | https://catalog.k-state.edu/programs/MENGL/about-the-program-aoYks |
| 61 | PhD Geography | https://catalog.k-state.edu/programs/DGEOG/about-the-program-aoYks |
| 62 | PhD History | https://catalog.k-state.edu/programs/DHIST/about-the-program-aoYks |
| 63 | PhD Mathematics | https://catalog.k-state.edu/programs/DMATH/about-the-program-aoYks |
| 64 | PhD Physics | https://catalog.k-state.edu/programs/DPHYS/about-the-program-aoYks |
| 65 | PhD Psychology | https://catalog.k-state.edu/programs/DPSYCH/about-the-program-aoYks |
| 66 | PhD Sociology | https://catalog.k-state.edu/programs/DSOCIO/about-the-program-aoYks |
| 67 | PhD Security Studies | https://catalog.k-state.edu/programs/DSECUR/about-the-program-aoYks |
| 68 | PhD Statistics | https://catalog.k-state.edu/programs/DSTAT/about-the-program-aoYks |
| 69 | PhD Biochemistry | https://catalog.k-state.edu/programs/DBIOCH/about-the-program-aoYks |
| 70 | PhD Microbiology | https://catalog.k-state.edu/programs/DMBIOL/about-the-program-aoYks |
| 71 | PhD Genetics | https://catalog.k-state.edu/programs/DGNT/about-the-program-aoYks |
| 72 | PhD Molecular Life Sciences (Integrated) | https://www.k-state.edu/grad/academics/integrated-life-sciences.html |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 73 | Applied Mathematics | https://catalog.k-state.edu/programs/CAMATH/about-the-program-aoYks |
| 74 | Geographic Information Science | https://catalog.k-state.edu/programs/CGISC/about-the-program-aoYks |
| 75 | Geoenvironmental | https://catalog.k-state.edu/programs/CGENVC/about-the-program-aoYks |
| 76 | Technical Writing and Professional Communication | https://catalog.k-state.edu/programs/CTWPC/about-the-program-aoYks |
| 77 | Entomology | https://catalog.k-state.edu/programs/CENTC/about-the-program-aoYks |

#### College of Business Administration (https://cba.k-state.edu/)

##### Master's / Professional
| # | 项目 | URL |
|---|------|-----|
| 78 | MBA Business Administration | https://catalog.k-state.edu/programs/MBA/about-the-program-aoYks |
| 79 | MAcc Accountancy | https://catalog.k-state.edu/programs/MACCTG/about-the-program-aoYks |
| 80 | MS Marketing Science | https://catalog.k-state.edu/programs/MMSX/about-the-program-aoYks |

#### College of Education (https://coe.k-state.edu/)

##### Master's
| # | 项目 | URL |
|---|------|-----|
| 81 | MS Curriculum and Instruction | https://catalog.k-state.edu/programs/MMEDCI/about-the-program-aoYks |
| 82 | MEd Educational Leadership | https://catalog.k-state.edu/programs/MEDLEA/about-the-program-aoYks |

##### Education Specialist / EdD
| # | 项目 | URL |
|---|------|-----|
| 83 | EdD Curriculum and Instruction | https://catalog.k-state.edu/programs/DCURIN-ED/about-the-program-aoYks |
| 84 | EdD Educational Leadership | https://catalog.k-state.edu/programs/DEDLEA-ED/about-the-program-aoYks |
| 85 | EdD Community College Leadership | https://catalog.k-state.edu/programs/DCCLD-ED/about-the-program-aoYks |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 86 | Dual Language Instruction | https://catalog.k-state.edu/programs/CDLIX/about-the-program-aoYks |
| 87 | Educational Technology | https://catalog.k-state.edu/programs/CEDTC/about-the-program-aoYks |
| 88 | Teaching and Learning | https://catalog.k-state.edu/programs/CTELRN/about-the-program-aoYks |
| 89 | Teaching Students with Autism Spectrum Disorders | https://catalog.k-state.edu/programs/CEDADC/about-the-program-aoYks |
| 90 | Urban Education | https://catalog.k-state.edu/programs/CUE/about-the-program-aoYks |

#### Carl R. Ice College of Engineering (https://engr.k-state.edu/)

##### Master's
| # | 项目 | URL |
|---|------|-----|
| 91 | MS Architectural Engineering | https://catalog.k-state.edu/programs/MARE/about-the-program-aoYks |
| 92 | MS Chemical Engineering | https://catalog.k-state.edu/programs/MCHE/about-the-program-aoYks |
| 93 | MS Civil Engineering | https://catalog.k-state.edu/programs/MCE/about-the-program-aoYks |
| 94 | MS Computer Science | https://catalog.k-state.edu/programs/MCS/about-the-program-aoYks |
| 95 | MS Electrical and Computer Engineering | https://catalog.k-state.edu/programs/MEECPE/about-the-program-aoYks |
| 96 | MS Industrial Engineering | https://catalog.k-state.edu/programs/MIE/about-the-program-aoYks |
| 97 | MS Mechanical Engineering | https://catalog.k-state.edu/programs/MME/about-the-program-aoYks |
| 98 | MS Mechanical and Nuclear Engineering | https://catalog.k-state.edu/programs/MNE/about-the-program-aoYks |
| 99 | MS Software Engineering (via CS) | https://catalog.k-state.edu/programs/MCS/about-the-program-aoYks |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 100 | PhD Chemical Engineering | https://catalog.k-state.edu/programs/DCHE/about-the-program-aoYks |
| 101 | PhD Civil Engineering | https://catalog.k-state.edu/programs/DCE/about-the-program-aoYks |
| 102 | PhD Computer Science | https://catalog.k-state.edu/programs/DCS/about-the-program-aoYks |
| 103 | PhD Electrical and Computer Engineering | https://catalog.k-state.edu/programs/DEECPE/about-the-program-aoYks |
| 104 | PhD Industrial Engineering | https://catalog.k-state.edu/programs/DIE/about-the-program-aoYks |
| 105 | PhD Mechanical Engineering | https://catalog.k-state.edu/programs/DME/about-the-program-aoYks |
| 106 | PhD Architectural Engineering | https://catalog.k-state.edu/programs/DARE/about-the-program-aoYks |
| 107 | PhD Biological and Agricultural Engineering | https://catalog.k-state.edu/programs/DBAE/about-the-program-aoYks |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 108 | Air Quality | https://catalog.k-state.edu/programs/CAQC/about-the-program-aoYks |
| 109 | Complex Fluid Flows | https://catalog.k-state.edu/programs/CCFFL/about-the-program-aoYks |
| 110 | Mineral Exploration for a Sustainable Future | https://catalog.k-state.edu/programs/CMESF/about-the-program-aoYks |
| 111 | Space Systems and Astrodynamics | https://catalog.k-state.edu/programs/CSSAX/about-the-program-aoYks |
| 112 | Aerospace Safety | https://catalog.k-state.edu/programs/CASX/about-the-program-aoYks |

#### College of Health and Human Sciences (https://www.hhs.k-state.edu/)

##### Master's
| # | 项目 | URL |
|---|------|-----|
| 113 | MS Athletic Training | https://catalog.k-state.edu/programs/MATHR/about-the-program-aoYks |
| 114 | MS Couple and Family Therapy (Human Ecology track) | https://catalog.k-state.edu/programs/MFSHS/about-the-program-aoYks |
| 115 | MS Kinesiology | https://catalog.k-state.edu/programs/MKINES/about-the-program-aoYks |
| 116 | MS Hospitality Administration | https://catalog.k-state.edu/programs/MHADM/about-the-program-aoYks |
| 117 | MS Food, Nutrition and Health | https://catalog.k-state.edu/programs/MHNDS/about-the-program-aoYks |
| 118 | MPH Public Health | https://catalog.k-state.edu/programs/MMPH/about-the-program-aoYks |
| 119 | MPAS Physician Assistant | https://catalog.k-state.edu/programs/MPAS/about-the-program-aoYks |

##### PhD / EdD
| # | 项目 | URL |
|---|------|-----|
| 120 | PhD Couple and Family Therapy | https://catalog.k-state.edu/programs/DHE/about-the-program-aoYks |
| 121 | PhD Food, Nutrition, Dietetics and Health | https://catalog.k-state.edu/programs/DFNDH/about-the-program-aoYks |
| 122 | PhD Human Ecology (Couple & Family Therapy) | https://catalog.k-state.edu/programs/DHE/about-the-program-aoYks |

##### Graduate Certificates
| # | 项目 | URL |
|---|------|-----|
| 123 | Public Health Core Concepts | https://catalog.k-state.edu/programs/CPHC/about-the-program-aoYks |
| 124 | Qualitative Research | https://catalog.k-state.edu/programs/CQUALR/about-the-program-aoYks |

#### College of Veterinary Medicine (https://www.vet.k-state.edu/)

##### Professional / Master's
| # | 项目 | URL |
|---|------|-----|
| 125 | DVM Veterinary Medicine | https://www.vet.k-state.edu/ (College of Veterinary Medicine) |
| 126 | MS Veterinary Biomedical Science | https://catalog.k-state.edu/programs/MBIOSC/about-the-program-aoYks |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 127 | PhD Pathobiology | https://catalog.k-state.edu/programs/DPATHB/about-the-program-aoYks |
| 128 | PhD Physiology | https://catalog.k-state.edu/programs/DPHYL/about-the-program-aoYks |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 129 | Exotic Animal Zoological Medicine | https://catalog.k-state.edu/programs/CEAZM/about-the-program-aoYks |
| 130 | Food Animal Veterinary | https://catalog.k-state.edu/programs/CAFVM/about-the-program-aoYks |

### 2.2 Full deep-dive — Computer Science (MS / PhD)

- **Department**: Department of Computer Science, College of Engineering
- **Department URL**: https://catalog.k-state.edu/departments/45065/overview
- **Application portal**: https://gradapply.ksu.edu/apply/
- **GRE Required**: Yes (MS and PhD) — institution code 6334 for K-State
- **Application fee**: $65 domestic / $75 international
- **English proficiency (international)**: TOEFL iBT 79 (pre-2026-01-21) or 4.5 (post-2026-01-21), IELTS 6.5, PTE 58 — see Section 3.3
- **Funding**: GTA/GRA available; PhD students typically funded
- **Contact**: grad@ksu.edu (general Graduate School); departmental coordinator listed on program page
- **Deadlines**: International Jan 8 for Fall, Aug 1 for Spring, Dec 1 for Summer; Domestic deadlines vary — contact program

### 2.3 Graduate admissions model

**Decentralized**. Each academic program reviews applications first; final admission decision is made by the Graduate School. Application fee waivers available via department request only (no central waivers, except McNair Scholars). Most graduate programs use the central Slate-based portal at https://gradapply.ksu.edu/apply/. Two exceptions: Physician Assistant Program (uses its own system) and Communication Sciences and Disorders (uses CSDCAS). Per-program contact information: https://www.k-state.edu/grad/academics/program-contacts.html

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table (Manhattan Campus, in-person)

| 维度 | 详情 | 来源 |
|------|------|------|
| Admissions site | https://www.k-state.edu/admissions/undergrad/manhattan/ | — |
| Application portal | https://apply.k-state.edu/ OR https://apply.commonapp.org/login (Common App member) | Apply page |
| **EA deadline** | N/A — K-State uses rolling admission with priority dates | https://www.k-state.edu/admissions/undergrad/manhattan/apply/deadlines.html |
| **RA/Regular deadline** | Rolling; Priority dates: Fall Freshmen March 1; Spring Freshmen Dec. 1; Transfer/Intl Fall May 1; Transfer/Intl Spring Dec. 1 | Deadlines page |
| Selective majors priority date | Dec. 1 (College of APDesign; Engineering domestic; Wildlife & Outdoor Enterprise Mgmt; Interior Design) | Deadlines page |
| Decision notification | Rolling | Admissions office |
| Enrollment confirmation | May 1 (national common date; K-State confirms in Admitted Student portal) | — |
| Financial aid priority date | Dec. 1 (FAFSA, school code 001928) | Deadlines page |
| SAT/ACT policy | Test-optional for admission. Required for some scholarships. Superscored. | Detailed requirements page |
| Score-report method | Official SAT/ACT scores optional for admission; if submitted, sent via College Board / ACT directly | Detailed requirements page |
| Interview policy | Not required; audition required for Music/Music Education studios | Majors with different requirements page |
| Recommendations | Not required for freshman admission | Admissions page |
| Portfolio | Required for Architecture, Interior Design, Industrial Design, Landscape Architecture, Regional & Community Planning (College of APDesign) | Majors with different requirements page |
| Transfer pathway | Transfer Center; 2.0+ college GPA required for most majors (2.5 for Business, Engineering; 2.5+ for Psychology transfer) | Transfer page; Majors requirements |
| International transfer | 2.0+ college GPA; if <24 credit hours, also 2.5 HS GPA | International requirements page |

### 3.2 Undergraduate English proficiency (international students)

K-State notes: "English proficiency is not required for admission to Kansas State University. However, you must meet the English Proficiency Standards before you enroll in courses."

| Exam | Minimum | Notes |
|------|---------|-------|
| TOEFL iBT | Waived if not required for admission; WildCAT EPT used after arrival for placement | https://www.k-state.edu/admissions/undergrad/manhattan/apply/international/english-proficiency.html |
| IELTS | Same — placement test after arrival | Same |
| PTE | Accepted (grad level); UG may use WildCAT EPT | Same |
| Duolingo English Test | NOT accepted (per grad policy) | Grad page |
| Completion of US high school | Exempt | International requirements |

### 3.3 Graduate — global rules

| 维度 | 详情 |
|------|------|
| Application portal | https://gradapply.ksu.edu/apply/ (Slate-based, centralized) — exceptions: PA Program and CSD |
| Application fee — Domestic degree seeking | $65 |
| Application fee — Domestic non-degree/certificate | $35 |
| Application fee — International degree seeking | $75 |
| Application fee — International non-degree/certificate | $35 |
| Application fee — Accelerated Master's (current K-State undergrad) | $35 |
| Fee waiver | McNair Scholars automatic; departmental waivers limited (no central waivers) |
| GRE institution code | 6334 (Kansas State University) |
| GRE/GMAT required for | MS Agricultural Economics (+Agribusiness conc), MS Architectural Engineering, MS Computer Science, PhD Agricultural Economics, PhD Computer Science, PhD Environmental Design and Planning, PhD Industrial Engineering, MS/PhD Hospitality Administration (GRE or GMAT), PhD Pathobiology, MS/PhD Personal Financial Planning (GRE or GMAT) |
| TOEFL iBT minimum (pre-2026-01-21) | 79 |
| TOEFL iBT minimum (2026-01-21+) | 4.5 |
| IELTS academic minimum | 6.5 |
| PTE minimum | 58 |
| Duolingo | NOT accepted |
| TOEFL ITP | NOT accepted |
| WildCAT EPT | NOT accepted for grad admission |
| US-accredited US degree | Exempt from English test |
| International deadlines — Fall | Jan 8 |
| International deadlines — Spring | Aug 1 |
| International deadlines — Summer | Dec 1 |
| CGS April-15 honor | K-State participates (15 April deadline for admitted students to commit) |
| Decision notification | Email notification after program + Graduate School review |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (Manhattan Campus, 2025-2026 academic year)

| Expense item | Kansas Resident | Non-Kansas Resident |
|--------------|-----------------|---------------------|
| Tuition and mandatory fees (billed) | $12,694 | $30,388 |
| On-campus housing + food (3 meals/day) | $13,652 | $13,652 |
| **Total billed (living on campus)** | **$26,346** | **$44,040** |
| Books and supplies | $1,062 | $1,062 |
| Transportation | $1,116 | $1,116 |
| Off-campus housing and food | $9,580 (if not on campus) | $9,580 (if not on campus) |
| Miscellaneous personal costs | $2,028 | $2,028 |
| **Total cost (billed + other, on campus)** | **$30,552** | **$48,246** |
| **Total cost (billed + other, off campus)** | **$26,480** | **$44,174** |

Source: https://www.k-state.edu/sfa/cost/manhattan-campus-costs/undergraduate.html (Updated 7/6/2026)

### 4.2 Undergraduate financial-aid policy

| Metric | Detail |
|--------|--------|
| Need-blind for domestic | Yes |
| Need-aware for international | Yes (international aid limited; merit-based scholarships available) |
| Tuition-free income threshold | N/A — K-State is not tuition-free; however K-State Promise program for Kansas residents with family income ≤$65,000 may cover tuition/fees |
| FAFSA school code | 001928 |
| FAFSA priority date | Dec. 1 |
| K-State Scholarship Network (KSN) | Feb. 1 priority date |
| Competitive scholarship deadline | Dec. 15 (requires supplemental application) |
| Average aid awarded | Last year $238 million in financial assistance awarded |
| Median price paid (in-state) | N/A — see Net Price Calculator: https://www.k-state.edu/sfa/cost/net-price-calculator/ |
| SmartAsset ranking | "Best educational value in Kansas" (2022) |

### 4.3 Graduate cost & funding framework (2025-2026)

| Item | Kansas Resident | Non-Kansas Resident |
|------|-----------------|---------------------|
| Tuition and mandatory fees (9 cr/term, 18 cr/yr) | $10,992 | $21,868 |
| Books and supplies | $706 | $706 |
| Transportation | $3,016 | $3,016 |
| Off-campus housing and food | $12,212 | $12,212 |
| Miscellaneous personal costs | $2,474 | $2,474 |
| **Total cost** | **$29,490** | **$40,366** |

Source: https://www.k-state.edu/sfa/cost/manhattan-campus-costs/graduate.html (Updated 7/6/2026)

**Funding types**:
- Graduate Teaching Assistantship (GTA) — requires spoken English certification for non-native speakers
- Graduate Research Assistantship (GRA) — common in STEM and Agriculture
- fellowships (Sarachek, Donoghue, Cross the Finish Line, etc.)
- Tuition waivers — common with full assistantships
- For international applicants: must show funds after admission (Affidavit of Financial Support)
- Job placement: 98% for master's and doctoral graduates (per Graduate School landing page)

---

## SECTION 5 — Evidence chain index

### E-U-001 — Test-optional assured admission
```yaml
field: undergraduate.admissions.test_policy
value: "Admission to the university is test-optional and requires achieving EITHER: A cumulative high school GPA (weighted or unweighted) of 3.25 or higher OR ACT composite score of 21, or an SAT ERW+M score of 1060 or higher"
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/incoming-freshmen/requirements.html
source_snippet: "Admission to the university is test-optional and requires achieving EITHER: A cumulative high school GPA (weighted or unweighted) of 3.25 or higher OR ACT composite score of 21, or an SAT ERW+M score of 1060 or higher"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-002 — UG priority dates
```yaml
field: undergraduate.deadlines.priority_dates
value:
  freshmen_fall: March 1
  freshmen_spring: Dec. 1
  transfer_international_fall: May 1
  transfer_international_spring: Dec. 1
  selective_majors: Dec. 1
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/deadlines.html
source_snippet: "Student Type | Starting Semester | Priority Date | Freshmen | Fall | March 1 | Freshman | Spring | Dec. 1 | Transfer or International | Fall | May 1 | Transfer or International | Spring | Dec. 1"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-003 — Undergraduate Manhattan Campus cost 2025-2026
```yaml
field: undergraduate.cost.2025_2026
value:
  ks_resident_billed_on_campus: 26346
  ks_resident_total: 30552
  non_resident_billed_on_campus: 44040
  non_resident_total: 48246
source_url: https://www.k-state.edu/sfa/cost/manhattan-campus-costs/undergraduate.html
source_snippet: "Estimated tuition and mandatory fees: Kansas resident $12,694; Non-Kansas resident $30,388. Total billed expenses: $26,346 (KS) / $44,040 (non-KS). Total cost (billed and other): $30,552 (KS) / $48,246 (non-KS)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-004 — Selective majors priority date
```yaml
field: undergraduate.admissions.selective_majors_priority
value: Dec. 1
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/deadlines.html
source_snippet: "Dec. 1 is the priority application date for: College of Architecture, Planning & Design programs; Carl R. Ice College of Engineering programs domestic students only; The wildlife and outdoor enterprise management program in the College of Agriculture; The interior design program in the College of Architecture, Planning & Design programs"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-005 — International UG requirements
```yaml
field: undergraduate.international.requirements
value:
  hs_gpa_min: 2.5
  transfer_gpa_min: 2.0
  english_proficiency_for_admission: not required
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/international/requirements.html
source_snippet: "Minimum 2.5 GPA (Grade Point Average) on a 4.0 scale in high school coursework. 2.0 GPA on a 4.0 scale on college or university transcripts. Proof of English proficiency is not required for admission to most Kansas State University Undergraduate degree programs"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-006 — Selective program requirements (Architecture, Engineering, Music, Business, Psychology, Aviation)
```yaml
field: undergraduate.admissions.selective_programs
value:
  architecture: "Selective based on academic performance and space availability. Fall entry only"
  engineering_domestic: "Selective based on academic performance and space availability"
  music: "Audition required for specific studios"
  business_transfer: "Cumulative college/university GPA of 2.5 or higher"
  psychology_transfer: "Cumulative college/university GPA of 2.5 or higher"
  professional_pilot: "Selective based on academic performance, space availability, and holistic review"
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/policies-requirements/majors-requirements.html
source_snippet: "Architecture, Interior Design, Industrial Design, Landscape Architecture, Regional and Community Planning: Admission is selective based on academic performance and space availability. Fall entry term only. Carl R. Ice College of Engineering: Admission is selective based on academic performance and space availability. Music and Music Education: Enrollment in specific studios requires an audition. College of Business Administration: Transfer students must have a cumulative college/university GPA of 2.5 or higher. Psychology: Transfer students must have a cumulative college/university GPA of 2.5 or higher. Professional Pilot: Admission is selective based on academic performance, space availability, and holistic review"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-007 — 250+ UG programs claim
```yaml
field: undergraduate.programs.total_count_claim
value: "250+ undergraduate programs"
source_url: https://www.k-state.edu/
source_snippet: "250+ undergraduate programs"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-001 — Graduate application fees
```yaml
field: graduate.admissions.fees
value:
  domestic_degree_seeking: 65
  domestic_non_degree_certificate: 35
  international_degree_seeking: 75
  international_non_degree_certificate: 35
  accelerated_master_current_kstate: 35
source_url: https://www.k-state.edu/grad/admissions/application-process/
source_snippet: "Domestic degree seeking $65; Domestic non-degree or certificate $35; International degree seeking $75; International non-degree or certificate fee $35; Accelerated Master's (for current K-State undergraduates) $35"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-002 — Graduate English proficiency
```yaml
field: graduate.admissions.english_proficiency
value:
  toefl_ibt_pre_2026_01_21: 79
  toefl_ibt_post_2026_01_21: 4.5
  ielts: 6.5
  pte: 58
  duolingo: not_accepted
  toefl_itp: not_accepted
  wildcat_ept: not_accepted
source_url: https://www.k-state.edu/grad/admissions/application-process/
source_snippet: "IBT TOEFL (internet based) [Valid scores earned prior to January 21, 2026] 79*; IBT TOEFL (internet based) [Valid scores earned on or after January 21, 2026] 4.5*; IELTS academic test 6.5*; Pearson Test of English (PTE) 58. We do not accept 'Duo Lingo', TOEFL ITP, or PTE (home edition). The WildCAT EPT is not an accepted English test for admission to graduate school"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-003 — Graduate international deadlines
```yaml
field: graduate.international.deadlines
value:
  fall: Jan 8
  spring: Aug 1
  summer: Dec 1
source_url: https://www.k-state.edu/grad/admissions/application-process/
source_snippet: "International applicants must follow these deadlines: Fall (August start) Jan 8; Spring (January start) Aug 1; Summer (May start) Dec 1"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-004 — GRE-required graduate programs
```yaml
field: graduate.admissions.gre_required_programs
value:
  - Agricultural Economics (MS conc Agribusiness)
  - Architectural Engineering (MS)
  - Computer Science (MS, PhD)
  - Environmental Design and Planning (PhD)
  - Industrial Engineering (PhD)
  - Hospitality Administration (MS/PhD; GRE or GMAT)
  - Pathobiology (PhD)
  - Personal Financial Planning (MS/PhD; GRE or GMAT)
  - Agricultural Economics (PhD)
source_url: https://www.k-state.edu/grad/admissions/application-process/
source_snippet: "GRE institution code 6334 for Kansas State University. Master's: Agricultural Economics, Agricultural Economics Concentration in Agribusiness, Architectural Engineering, Computer Science. Doctoral: Agricultural Economics, Computer Science, Environmental Design and Planning, Industrial Engineering, Hospitality Administration (GRE or GMAT), Pathobiology, Personal Financial Planning (GRE or GMAT)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-005 — Graduate cost Manhattan Campus 2025-2026
```yaml
field: graduate.cost.2025_2026
value:
  ks_resident_total: 29490
  non_resident_total: 40366
  ks_resident_tuition_fees: 10992
  non_resident_tuition_fees: 21868
source_url: https://www.k-state.edu/sfa/cost/manhattan-campus-costs/graduate.html
source_snippet: "Estimated tuition and mandatory fees: Kansas resident $10,992; Non-Kansas resident $21,868. Total cost (billed and other): Kansas resident $29,490; Non-Kansas resident $40,366"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-006 — 165+ graduate programs claim
```yaml
field: graduate.programs.total_count_claim
value: "165+ graduate programs"
source_url: https://www.k-state.edu/grad/
source_snippet: "165+ PROGRAMS"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-001 — Institutional identity
```yaml
field: institution.identity
value:
  name: Kansas State University
  founded: 1863
  type: Public R1 land-grant university
  oldest_public_university_in_kansas: true
  main_campus: Manhattan, KS
  campuses: [Manhattan, Olathe, Salina (Polytechnic)]
source_url: https://www.k-state.edu/
source_snippet: "Leading the nation as the next-generation land-grant university, K-State is the first operational land-grant university in the United States"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-002 — College structure (10 colleges)
```yaml
field: institution.colleges
value:
  - Agriculture
  - Architecture, Planning and Design
  - Arts and Sciences
  - Business Administration
  - Education
  - Carl R. Ice Engineering
  - Health and Human Sciences
  - Technology and Aviation
  - Veterinary Medicine
  - Graduate School
source_url: https://www.k-state.edu/directories/academic.html
source_snippet: "Agriculture, College of; Architecture, Planning and Design, College of; Arts and Sciences, College of; Business Administration, College of; Education, College of; Engineering, College of; Health and Human Sciences, College of; Technology and Aviation, College of; Veterinary Medicine, College of"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-003 — International student facts
```yaml
field: undergraduate.international.facts
value:
  total_intl_students: "2,000+"
  countries_represented: "100+"
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/international/
source_snippet: "2,000+ international students, scholars and faculty; More than 100 countries represented on campus"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-004 — Graduate employment
```yaml
field: graduate.outcomes.job_placement
value: "98% job placement for master's and doctoral graduates"
source_url: https://www.k-state.edu/grad/
source_snippet: "98% job placement for master's and doctoral graduates"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-005 — TOEFL institution code (implied via GRE code)
```yaml
field: graduate.admissions.test_codes
value:
  gre_gmat_code: "6334"
source_url: https://www.k-state.edu/grad/admissions/application-process/
source_snippet: "When you take your GRE/GMAT use institution code 6334 for Kansas State University"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-006 — UG ranking
```yaml
field: institution.rankings
value:
  niche_best_colleges_kansas_2026: "#1"
  niche_colleges_best_professors_kansas_2026: "#1"
  princeton_review_friendliest_students_2025: "#1"
  princeton_review_best_quality_of_life_2025: "#2"
  college_rank_best_college_town: "#3"
source_url: https://www.k-state.edu/
source_snippet: "#1 BEST COLLEGES IN KANSAS, Niche, 2026; #1 COLLEGES WITH THE BEST PROFESSORS IN KANSAS, Niche, 2026; #1 friendliest students in the nation, Princeton Review 2025; #2 best quality of life in the nation, Princeton Review 2025; #3 best college town in the nation, College Rank"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-O-007 — UG acceptance channels
```yaml
field: undergraduate.admissions.channels
value: [K-State Direct Application (https://apply.k-state.edu/), Common App (https://apply.commonapp.org/login)]
source_url: https://www.k-state.edu/admissions/undergrad/manhattan/apply/
source_snippet: "Apply for admission via https://apply.k-state.edu/ OR Kansas State University is also a member of Common App. If you prefer, Sign in to Common App and add Kansas State University to My Colleges"
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
kansas-state-university-knowledge-base-v2/
├── 00-overview/
│   ├── institution-identity.md
│   ├── college-structure.md
│   └── degree-levels-matrix.md
├── 01-undergraduate/
│   ├── college-of-agriculture.md
│   ├── college-of-architecture-planning-design.md
│   ├── college-of-arts-and-sciences.md
│   ├── college-of-business-administration.md
│   ├── college-of-education.md
│   ├── carl-r-ice-college-of-engineering.md
│   ├── college-of-health-and-human-sciences.md
│   ├── college-of-technology-and-aviation.md
│   └── interdisciplinary-undergraduate.md
├── 02-graduate/
│   ├── college-of-agriculture-grad.md
│   ├── college-of-apd-grad.md
│   ├── college-of-arts-sciences-grad.md
│   ├── college-of-business-grad.md
│   ├── college-of-education-grad.md
│   ├── engineering-grad.md
│   ├── health-and-human-sciences-grad.md
│   └── veterinary-medicine-grad.md
├── 03-admissions/
│   ├── undergraduate-requirements.md
│   ├── undergraduate-deadlines.md
│   ├── international-undergraduate.md
│   ├── transfer-requirements.md
│   ├── graduate-application-process.md
│   ├── graduate-english-proficiency.md
│   └── graduate-gre-requirements.md
└── 04-costs/
    ├── undergraduate-cost-2025-2026.md
    ├── graduate-cost-2025-2026.md
    └── financial-aid-policy.md
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "kansas-state-university-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|EdD|DVM|GradCert|UG Cert>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Reason |
|----------|-----------|------------|--------|
| P0 | Per-program graduate deadlines (most programs have earlier deadlines than International defaults) | https://www.k-state.edu/grad/academics/program-contacts.html | Capture showed program-specific deadlines vary |
| P0 | TOEFL/IELTS minimum score mapping per grad program (some programs may be higher) | https://www.k-state.edu/grad/admissions/application-process/ and individual program pages | Programs can require higher than minimums |
| P1 | Minors — complete full list of ~20+ minors | https://catalog.k-state.edu/programs (filter by Minor) | Captured representative subset only |
| P1 | Salina (Polytechnic Campus) and Olathe campus programs — full listing | https://salina.k-state.edu/academics/ and https://olathe.k-state.edu/ | Captured majors through main filter; campus-specific pages not exhaustively scraped |
| P1 | Tuition rates per credit hour (campus-based plan 2026-2027) | https://www.k-state.edu/finsvcs/cashiers/costs/campus-tuition-fees/ | Used Manhattan Campus annual estimate instead |
| P2 | Acceptance rate / admit rate historical | Common Data Set or Institutional Research | Not publicly posted on admissions pages |
| P2 | Average starting salary | Career Center / Niche | Not posted on admissions pages |
| P2 | Detailed program curriculum (4-year plans) | https://catalog.k-state.edu/academics/maps | Degree maps exist; not extracted |
| P2 | Accelerated bachelor's/master's full list of 8+ programs | https://www.k-state.edu/academics/majors-programs/ | Captured subset; needs full enumeration |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Kansas State University |
|-----------|-------------------------|
| Institution type | Public R1 land-grant (oldest public in Kansas, est. 1863) |
| Total UG programs | 115 |
| Total graduate programs | 110 |
| Total programs (claim) | 250+ UG + 165+ Grad |
| Number of colleges | 10 |
| Campuses | Manhattan, Olathe, Salina (Polytechnic) |
| UG application portal | apply.k-state.edu OR Common App |
| UG test policy | Test-optional (assured: 3.25 HS GPA OR 21 ACT/1060 SAT) |
| UG application fee | $0 (no application fee listed) |
| Fall UG priority deadline | March 1 (freshmen) |
| UG cost 2025-2026 (KS resident, total) | $30,552 |
| UG cost 2025-2026 (non-resident, total) | $48,246 |
| Grad application fee (domestic) | $65 |
| Grad application fee (international) | $75 |
| TOEFL iBT minimum (pre-2026-01-21) | 79 |
| TOEFL iBT minimum (2026-01-21+) | 4.5 |
| IELTS minimum | 6.5 |
| PTE minimum | 58 |
| Duolingo accepted | No |
| Financial aid priority | Dec. 1 (FAFSA code 001928) |
| Job placement (grad) | 98% |
| Median price paid (KS resident, in-state) | N/A — see Net Price Calculator |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: k-state.edu (main, admissions, grad, sfa, finsvcs, catalog), ksu.edu (catalog), apply.commonapp.org
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
