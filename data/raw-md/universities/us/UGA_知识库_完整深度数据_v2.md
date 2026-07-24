# University of Georgia (UGA) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (AB/BS/BBA/BFA/etc.) | 162 |
| 本科辅修 (Minor) | 130 |
| 本科证书 (Undergraduate Certificate) | 67 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 405 |
| 研究生高级证书 (Graduate Certificate) | 95 |
| **学位项目总计 (UG + Grad)** | **859** |
| 学院 / 独立系所总数 | 20 |

### 0.2 学院 / 系层级结构

University of Georgia
├── Biomedical and Translational Sciences Institute [学院]
├── College of Agricultural and Environmental Sciences [学院]
├── College of Engineering [学院]
├── College of Environment and Design [学院]
├── College of Family and Consumer Sciences [学院]
├── College of Pharmacy [学院]
├── College of Public Health [学院]
├── College of Veterinary Medicine [学院]
├── Franklin College of Arts and Sciences [学院]
├── Grady College of Journalism and Mass Communication [学院]
├── Institute of Bioinformatics [学院]
├── Institute of Higher Education [学院]
├── Mary Frances Early College of Education [学院]
├── Odum School of Ecology [学院]
├── School of Law [学院]
├── School of Public and International Affairs [学院]
├── School of Social Work [学院]
├── Terry College of Business [学院]
├── Vice President for Instruction [学院]
├── Warnell School of Forestry and Natural Resources [学院]

### 0.3 学历级别明细

| 学位缩写 (official) | canonical | 全称 | 层级 | 数量 |
|---------------------|-----------|------|------|------|
| Certificate | Certificate | Certificate | 研究生 | 162 |
| Minor | Minor | Minor | 研究生 | 130 |
| PhD | PhD | PhD | 研究生 | 128 |
| MS | MS | Master of Science | 研究生 | 113 |
| BS | BS | Bachelor of Science | 本科 | 85 |
| BA | BA | BA | 研究生 | 40 |
| MA | MA | Master of Arts | 研究生 | 37 |
| MEd | MEd | MEd | 研究生 | 33 |
| EdS | EdS | EdS | 研究生 | 28 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 18 |
| BBA | BBA | Bachelor of Business Administration | 本科 | 17 |
| BFA | BFA | Bachelor of Fine Arts | 本科 | 13 |
| MSW | MSW | Master of Social Work | 研究生 | 10 |
| MPH | MPH | Master of Public Health | 研究生 | 9 |
| EdD | EdD | EdD | 研究生 | 8 |
| MM | MM | Master of Music | 研究生 | 6 |
| BMUS | BMUS | Bachelor of Music | 本科 | 5 |
| MFA | MFA | Master of Fine Arts | 研究生 | 4 |
| DMA | DMA | Doctor of Musical Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 1 |
| BLA | BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| MLA | MLA | Master of Landscape Architecture | 研究生 | 1 |
| JD | JD | Juris Doctor | 研究生 | 1 |
| LLM | LLM | Master of Laws | 研究生 | 1 |
| PharmD | PharmD | PharmD | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 1 |
| DrPH | DrPH | DrPH | 研究生 | 1 |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| DVM | DVM | Doctor of Veterinary Medicine | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BBA | BFA | BLA | BMUS | BS | BSW | Certificate | DMA | DVM | DrPH | EdD | EdS | JD | LLM | MA | MAT | MBA | MEd | MFA | MLA | MM | MPA | MPH | MS | MSW | Minor | PhD | PharmD | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Biomedical and Translational Sciences Institute | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 |
| College of Agricultural and Environmental Sciences | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | 0 | 19 | 13 | 0 | 78 |
| College of Engineering | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 13 | 0 | 35 |
| College of Environment and Design | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 2 | 0 | 4 | 1 | 0 | 14 |
| College of Family and Consumer Sciences | 0 | 0 | 0 | 0 | 0 | 11 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 6 | 4 | 0 | 40 |
| College of Pharmacy | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 2 | 4 | 1 | 22 |
| College of Public Health | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 8 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 6 | 0 | 6 | 7 | 0 | 39 |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 22 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 2 | 5 | 0 | 38 |
| Franklin College of Arts and Sciences | 32 | 0 | 13 | 0 | 5 | 22 | 0 | 43 | 3 | 0 | 0 | 1 | 1 | 0 | 0 | 19 | 0 | 0 | 0 | 2 | 0 | 6 | 0 | 0 | 19 | 0 | 69 | 32 | 0 | 267 |
| Grady College of Journalism and Mass Communication | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 16 |
| Institute of Bioinformatics | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 3 |
| Institute of Higher Education | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| Mary Frances Early College of Education | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 26 | 0 | 0 | 0 | 6 | 27 | 0 | 0 | 13 | 18 | 0 | 32 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 9 | 30 | 0 | 179 |
| Odum School of Ecology | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 1 | 3 | 0 | 12 |
| School of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 6 |
| School of Public and International Affairs | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 4 | 2 | 0 | 15 |
| School of Social Work | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 | 1 | 1 | 0 | 17 |
| Terry College of Business | 1 | 17 | 0 | 0 | 0 | 0 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 | 1 | 2 | 0 | 36 |
| Vice President for Instruction | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Warnell School of Forestry and Natural Resources | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 18 | 0 | 5 | 7 | 0 | 37 |
| **合计** | 40 | 17 | 13 | 1 | 5 | 85 | 1 | 162 | 3 | 1 | 1 | 8 | 28 | 1 | 1 | 37 | 18 | 1 | 33 | 4 | 1 | 6 | 1 | 9 | 113 | 10 | 130 | 128 | 1 | **859** |

---

## 1. 本科教育 (Undergraduate Education)

### 1.1 学院架构

UGA has 20 schools/colleges offering undergraduate programs. The largest is Franklin College of Arts and Sciences. See Section 0.2 for the full hierarchy tree.

### 1.2 本科专业 -- 按 学院 > 学位级别 分组

#### College of Agricultural and Environmental Sciences
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness | <https://bulletin.uga.edu/Program/Details/86648?IDc=CAES> |
| 2 | Agricultural Education | <https://bulletin.uga.edu/Program/Details/28608?IDc=CAES> |
| 3 | Agricultural and Applied Economics | <https://bulletin.uga.edu/Program/Details/33812?IDc=CAES> |
| 4 | Agricultural and Environmental Science Communication | <https://bulletin.uga.edu/Program/Details/45731?IDc=CAES> |
| 5 | Agriscience and Environmental Systems | <https://bulletin.uga.edu/Program/Details/47617?IDc=CAES> |
| 6 | Animal Biosciences | <https://bulletin.uga.edu/Program/Details/27361?IDc=CAES> |
| 7 | Animal Health | <https://bulletin.uga.edu/Program/Details/18956?IDc=CAES> |
| 8 | Animal and Dairy Science | <https://bulletin.uga.edu/Program/Details/75032?IDc=CAES> |
| 9 | Applied Biotechnology | <https://bulletin.uga.edu/Program/Details/47637?IDc=CAES> |
| 10 | Avian Biology | <https://bulletin.uga.edu/Program/Details/20412?IDc=CAES> |
| 11 | Biological Science | <https://bulletin.uga.edu/Program/Details/99573?IDc=CAES> |
| 12 | Entomology | <https://bulletin.uga.edu/Program/Details/69190?IDc=CAES> |
| 13 | Environmental Economics and Management | <https://bulletin.uga.edu/Program/Details/66704?IDc=CAES> |
| 14 | Environmental Resource Science | <https://bulletin.uga.edu/Program/Details/27349?IDc=CAES> |
| 15 | Food Science | <https://bulletin.uga.edu/Program/Details/35947?IDc=CAES> |
| 16 | Honors Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/92067?IDc=CAES> |
| 17 | Horticulture | <https://bulletin.uga.edu/Program/Details/33716?IDc=CAES> |
| 18 | Hospitality and Food Industry Management | <https://bulletin.uga.edu/Program/Details/86144?IDc=CAES> |
| 19 | Poultry Science | <https://bulletin.uga.edu/Program/Details/62966?IDc=CAES> |
| 20 | Regenerative Bioscience | <https://bulletin.uga.edu/Program/Details/77774?IDc=CAES> |
| 21 | Turfgrass Management | <https://bulletin.uga.edu/Program/Details/95527?IDc=CAES> |
| 22 | Water and Soil Resources | <https://bulletin.uga.edu/Program/Details/51070?IDc=CAES> |

#### College of Engineering
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Engineering | <https://bulletin.uga.edu/Program/Details/29981?IDc=FENGR> |
| 2 | Biochemical Engineering | <https://bulletin.uga.edu/Program/Details/82357?IDc=FENGR> |
| 3 | Biological Engineering | <https://bulletin.uga.edu/Program/Details/89691?IDc=FENGR> |
| 4 | Civil Engineering | <https://bulletin.uga.edu/Program/Details/79689?IDc=FENGR> |
| 5 | Computer Systems Engineering | <https://bulletin.uga.edu/Program/Details/45516?IDc=FENGR> |
| 6 | Electrical and Electronics Engineering | <https://bulletin.uga.edu/Program/Details/81996?IDc=FENGR> |
| 7 | Environmental Engineering | <https://bulletin.uga.edu/Program/Details/73693?IDc=FENGR> |
| 8 | Mechanical Engineering | <https://bulletin.uga.edu/Program/Details/20122?IDc=FENGR> |

#### College of Environment and Design
##### BLA
| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | <https://bulletin.uga.edu/Program/Details/29349?IDc=ENV> |

#### College of Family and Consumer Sciences
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Consumer Economics | <https://bulletin.uga.edu/Program/Details/44649?IDc=FCS> |
| 2 | Culinary Science and Nutrition | <https://bulletin.uga.edu/Program/Details/12516?IDc=FCS> |
| 3 | Dietetics | <https://bulletin.uga.edu/Program/Details/31975?IDc=FCS> |
| 4 | Family and Consumer Sciences Education | <https://bulletin.uga.edu/Program/Details/22708?IDc=FCS> |
| 5 | Fashion Merchandising | <https://bulletin.uga.edu/Program/Details/48680?IDc=FCS> |
| 6 | Financial Planning | <https://bulletin.uga.edu/Program/Details/89431?IDc=FCS> |
| 7 | Furnishings and Interiors | <https://bulletin.uga.edu/Program/Details/85319?IDc=FCS> |
| 8 | Housing Management and Policy | <https://bulletin.uga.edu/Program/Details/28344?IDc=FCS> |
| 9 | Human Development and Family Science | <https://bulletin.uga.edu/Program/Details/67554?IDc=FCS> |
| 10 | Nutritional Sciences | <https://bulletin.uga.edu/Program/Details/31338?IDc=FCS> |
| 11 | Social Entrepreneurship for Consumer Well-Being | <https://bulletin.uga.edu/Program/Details/77137?IDc=FCS> |

#### College of Pharmacy
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmaceutical and Biomedical Sciences | <https://bulletin.uga.edu/Program/Details/28389?IDc=PHAR> |

#### College of Public Health
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Health | <https://bulletin.uga.edu/Program/Details/47320?IDc=PBHL> |
| 2 | Health Promotion | <https://bulletin.uga.edu/Program/Details/33197?IDc=PBHL> |

#### College of Veterinary Medicine
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Physiology | <https://bulletin.uga.edu/Program/Details/18982?IDc=VET> |

#### Franklin College of Arts and Sciences
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | African American Studies | <https://bulletin.uga.edu/Program/Details/99424?IDc=ARTS> |
| 2 | Anthropology | <https://bulletin.uga.edu/Program/Details/51649?IDc=ARTS> |
| 3 | Arabic | <https://bulletin.uga.edu/Program/Details/98747?IDc=ARTS> |
| 4 | Art History | <https://bulletin.uga.edu/Program/Details/66399?IDc=ARTS> |
| 5 | Art: Interdisciplinary Art | <https://bulletin.uga.edu/Program/Details/86044?IDc=ARTS> |
| 6 | Asian Languages and Literature | <https://bulletin.uga.edu/Program/Details/88637?IDc=ARTS> |
| 7 | Classics | <https://bulletin.uga.edu/Program/Details/82769?IDc=ARTS> |
| 8 | Cognitive Science | <https://bulletin.uga.edu/Program/Details/96447?IDc=ARTS> |
| 9 | Communication Studies | <https://bulletin.uga.edu/Program/Details/52209?IDc=ARTS> |
| 10 | Comparative Literature and Intercultural Studies | <https://bulletin.uga.edu/Program/Details/47290?IDc=ARTS> |
| 11 | Criminal Justice | <https://bulletin.uga.edu/Program/Details/64585?IDc=ARTS> |
| 12 | Dance | <https://bulletin.uga.edu/Program/Details/71373?IDc=ARTS> |
| 13 | English | <https://bulletin.uga.edu/Program/Details/86328?IDc=ARTS> |
| 14 | Film AB | <https://bulletin.uga.edu/Program/Details/29901?IDc=ARTS> |
| 15 | French | <https://bulletin.uga.edu/Program/Details/56782?IDc=ARTS> |
| 16 | Geography | <https://bulletin.uga.edu/Program/Details/68705?IDc=ARTS> |
| 17 | Geology | <https://bulletin.uga.edu/Program/Details/70540?IDc=ARTS> |
| 18 | German | <https://bulletin.uga.edu/Program/Details/86205?IDc=ARTS> |
| 19 | History | <https://bulletin.uga.edu/Program/Details/35426?IDc=ARTS> |
| 20 | Honors Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/71506?IDc=ARTS> |
| 21 | Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/76673?IDc=ARTS> |
| 22 | Latin American and Caribbean Studies | <https://bulletin.uga.edu/Program/Details/20701?IDc=ARTS> |
| 23 | Linguistics | <https://bulletin.uga.edu/Program/Details/84398?IDc=ARTS> |
| 24 | Music | <https://bulletin.uga.edu/Program/Details/55653?IDc=ARTS> |
| 25 | Philosophy | <https://bulletin.uga.edu/Program/Details/99676?IDc=ARTS> |
| 26 | Religion | <https://bulletin.uga.edu/Program/Details/13716?IDc=ARTS> |
| 27 | Romance Languages | <https://bulletin.uga.edu/Program/Details/58425?IDc=ARTS> |
| 28 | Russian | <https://bulletin.uga.edu/Program/Details/76210?IDc=ARTS> |
| 29 | Sociology | <https://bulletin.uga.edu/Program/Details/77932?IDc=ARTS> |
| 30 | Spanish | <https://bulletin.uga.edu/Program/Details/21871?IDc=ARTS> |
| 31 | Theatre | <https://bulletin.uga.edu/Program/Details/93915?IDc=ARTS> |
| 32 | Women&#39;s and Gender Studies | <https://bulletin.uga.edu/Program/Details/57374?IDc=ARTS> |

##### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art BFA - Animation | <https://bulletin.uga.edu/Program/Details/71747?IDc=ARTS> |
| 2 | Art BFA - Ceramics | <https://bulletin.uga.edu/Program/Details/14150?IDc=ARTS> |
| 3 | Art BFA - Drawing and Painting | <https://bulletin.uga.edu/Program/Details/30672?IDc=ARTS> |
| 4 | Art BFA - Fabric Design | <https://bulletin.uga.edu/Program/Details/47137?IDc=ARTS> |
| 5 | Art BFA - Graphic Design | <https://bulletin.uga.edu/Program/Details/79344?IDc=ARTS> |
| 6 | Art BFA - Interior Design | <https://bulletin.uga.edu/Program/Details/40512?IDc=ARTS> |
| 7 | Art BFA - Jewelry and Metalwork | <https://bulletin.uga.edu/Program/Details/70174?IDc=ARTS> |
| 8 | Art BFA - Photography and Expanded Media | <https://bulletin.uga.edu/Program/Details/74546?IDc=ARTS> |
| 9 | Art BFA - Printmaking | <https://bulletin.uga.edu/Program/Details/45379?IDc=ARTS> |
| 10 | Art BFA - Scientific Illustration | <https://bulletin.uga.edu/Program/Details/65044?IDc=ARTS> |
| 11 | Art BFA - Sculpture | <https://bulletin.uga.edu/Program/Details/54287?IDc=ARTS> |
| 12 | Art Education | <https://bulletin.uga.edu/Program/Details/68952?IDc=ARTS> |
| 13 | Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/73709?IDc=ARTS> |

##### BMUS
| # | 专业 | URL |
|---|------|-----|
| 1 | Music BMus - Music Composition | <https://bulletin.uga.edu/Program/Details/93244?IDc=ARTS> |
| 2 | Music BMus - Music Education | <https://bulletin.uga.edu/Program/Details/22148?IDc=ARTS> |
| 3 | Music BMus - Music Performance | <https://bulletin.uga.edu/Program/Details/16876?IDc=ARTS> |
| 4 | Music BMus - Music Theory | <https://bulletin.uga.edu/Program/Details/56733?IDc=ARTS> |
| 5 | Music BMus - Music Therapy | <https://bulletin.uga.edu/Program/Details/11719?IDc=ARTS> |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Astrophysics | <https://bulletin.uga.edu/Program/Details/45275?IDc=ARTS> |
| 2 | Atmospheric Sciences | <https://bulletin.uga.edu/Program/Details/29248?IDc=ARTS> |
| 3 | Biochemistry and Molecular Biology | <https://bulletin.uga.edu/Program/Details/95737?IDc=ARTS> |
| 4 | Biology | <https://bulletin.uga.edu/Program/Details/45780?IDc=ARTS> |
| 5 | Cellular Biology | <https://bulletin.uga.edu/Program/Details/70249?IDc=ARTS> |
| 6 | Chemistry | <https://bulletin.uga.edu/Program/Details/77246?IDc=ARTS> |
| 7 | Chemistry | <https://bulletin.uga.edu/Program/Details/97290?IDc=ARTS> |
| 8 | Computer Science | <https://bulletin.uga.edu/Program/Details/73962?IDc=ARTS> |
| 9 | Data Science | <https://bulletin.uga.edu/Program/Details/35773?IDc=ARTS> |
| 10 | Genetics | <https://bulletin.uga.edu/Program/Details/83049?IDc=ARTS> |
| 11 | Geography | <https://bulletin.uga.edu/Program/Details/22757?IDc=ARTS> |
| 12 | Geology | <https://bulletin.uga.edu/Program/Details/90385?IDc=ARTS> |
| 13 | Honors Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/70139?IDc=ARTS> |
| 14 | Interdisciplinary Studies | <https://bulletin.uga.edu/Program/Details/21398?IDc=ARTS> |
| 15 | Mathematics | <https://bulletin.uga.edu/Program/Details/69357?IDc=ARTS> |
| 16 | Microbiology | <https://bulletin.uga.edu/Program/Details/57726?IDc=ARTS> |
| 17 | Neuroscience BS | <https://bulletin.uga.edu/Program/Details/30336?IDc=ARTS> |
| 18 | Ocean Science | <https://bulletin.uga.edu/Program/Details/39199?IDc=ARTS> |
| 19 | Physics | <https://bulletin.uga.edu/Program/Details/17511?IDc=ARTS> |
| 20 | Plant Biology | <https://bulletin.uga.edu/Program/Details/62409?IDc=ARTS> |
| 21 | Psychology | <https://bulletin.uga.edu/Program/Details/69115?IDc=ARTS> |
| 22 | Statistics | <https://bulletin.uga.edu/Program/Details/85325?IDc=ARTS> |

#### Grady College of Journalism and Mass Communication
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | <https://bulletin.uga.edu/Program/Details/98779?IDc=JOUR> |
| 2 | Entertainment and Media Studies | <https://bulletin.uga.edu/Program/Details/60174?IDc=JOUR> |
| 3 | Journalism | <https://bulletin.uga.edu/Program/Details/84144?IDc=JOUR> |
| 4 | Public Relations | <https://bulletin.uga.edu/Program/Details/63054?IDc=JOUR> |

#### Mary Frances Early College of Education
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | <https://bulletin.uga.edu/Program/Details/95317?IDc=EDCN> |
| 2 | Elementary Education | <https://bulletin.uga.edu/Program/Details/90610?IDc=EDCN> |
| 3 | English Education | <https://bulletin.uga.edu/Program/Details/20130?IDc=EDCN> |
| 4 | Exercise and Sport Science | <https://bulletin.uga.edu/Program/Details/65938?IDc=EDCN> |
| 5 | Health and Physical Education | <https://bulletin.uga.edu/Program/Details/28666?IDc=EDCN> |
| 6 | Mathematics Education | <https://bulletin.uga.edu/Program/Details/79641?IDc=EDCN> |
| 7 | Science Education | <https://bulletin.uga.edu/Program/Details/79643?IDc=EDCN> |
| 8 | Social Studies Education | <https://bulletin.uga.edu/Program/Details/79831?IDc=EDCN> |
| 9 | Special Education | <https://bulletin.uga.edu/Program/Details/90477?IDc=EDCN> |
| 10 | Sport Management | <https://bulletin.uga.edu/Program/Details/42162?IDc=EDCN> |
| 11 | TESOL and World Language Education | <https://bulletin.uga.edu/Program/Details/42194?IDc=EDCN> |
| 12 | Workforce Education | <https://bulletin.uga.edu/Program/Details/93788?IDc=EDCN> |

#### Odum School of Ecology
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology | <https://bulletin.uga.edu/Program/Details/38829?IDc=ECOL> |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Ecology | <https://bulletin.uga.edu/Program/Details/86043?IDc=ECOL> |

#### School of Public and International Affairs
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Affairs | <https://bulletin.uga.edu/Program/Details/24662?IDc=SPIA> |
| 2 | Political Science | <https://bulletin.uga.edu/Program/Details/46524?IDc=SPIA> |

##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | <https://bulletin.uga.edu/Program/Details/12235?IDc=SPIA> |

#### School of Social Work
##### BSW
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | <https://bulletin.uga.edu/Program/Details/51439?IDc=SSW> |

#### Terry College of Business
##### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | <https://bulletin.uga.edu/Program/Details/77024?IDc=BUS> |

##### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | <https://bulletin.uga.edu/Program/Details/31532?IDc=BUS> |
| 2 | Accounting and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/35784?IDc=BUS> |
| 3 | Economics | <https://bulletin.uga.edu/Program/Details/62927?IDc=BUS> |
| 4 | Economics and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/75605?IDc=BUS> |
| 5 | Finance | <https://bulletin.uga.edu/Program/Details/28543?IDc=BUS> |
| 6 | Finance and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/83627?IDc=BUS> |
| 7 | General Business | <https://bulletin.uga.edu/Program/Details/51100?IDc=BUS> |
| 8 | Management | <https://bulletin.uga.edu/Program/Details/91641?IDc=BUS> |
| 9 | Management Information Systems | <https://bulletin.uga.edu/Program/Details/23268?IDc=BUS> |
| 10 | Management Information Systems and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/19506?IDc=BUS> |
| 11 | Management and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/11214?IDc=BUS> |
| 12 | Marketing | <https://bulletin.uga.edu/Program/Details/59600?IDc=BUS> |
| 13 | Marketing and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/17378?IDc=BUS> |
| 14 | Real Estate | <https://bulletin.uga.edu/Program/Details/46304?IDc=BUS> |
| 15 | Real Estate and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/36008?IDc=BUS> |
| 16 | Risk Management and Insurance | <https://bulletin.uga.edu/Program/Details/93328?IDc=BUS> |
| 17 | Risk Management and Insurance and International Business Co-Major | <https://bulletin.uga.edu/Program/Details/81139?IDc=BUS> |

#### Warnell School of Forestry and Natural Resources
##### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fisheries and Wildlife | <https://bulletin.uga.edu/Program/Details/70392?IDc=FRS> |
| 2 | Forestry | <https://bulletin.uga.edu/Program/Details/61717?IDc=FRS> |
| 3 | Natural Resource Management and Sustainability | <https://bulletin.uga.edu/Program/Details/51733?IDc=FRS> |
| 4 | Parks, Recreation, and Tourism Management | <https://bulletin.uga.edu/Program/Details/99141?IDc=FRS> |

### 1.3 本科辅修 (Minors) -- 完整列表

| # | 辅修名称 | 学院 | URL |
|---|----------|------|-----|
| 1 | African American Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/99707?IDc=ARTS> |
| 2 | Minor in African Languages and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/35595?IDc=ARTS> |
| 3 | Minor in African Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/13458?IDc=ARTS> |
| 4 | Minor in Agribusiness and Management | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/57930?IDc=CAES> |
| 5 | Minor in Agricultural and Applied Economics | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/14098?IDc=CAES> |
| 6 | Minor in American Sign Language | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/34720?IDc=EDCN> |
| 7 | Minor in Animal Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/71291?IDc=CAES> |
| 8 | Minor in Anthropology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/75540?IDc=ARTS> |
| 9 | Minor in Applied Biotechnology | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/73088?IDc=CAES> |
| 10 | Minor in Arabic | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/40013?IDc=ARTS> |
| 11 | Minor in Art History | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/24881?IDc=ARTS> |
| 12 | Minor in Asian Languages and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/26570?IDc=ARTS> |
| 13 | Minor in Astrophysics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/16224?IDc=ARTS> |
| 14 | Minor in Avian Biology | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/56158?IDc=CAES> |
| 15 | Minor in Biochemistry and Molecular Biology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/58449?IDc=ARTS> |
| 16 | Minor in Bioethics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/93650?IDc=ARTS> |
| 17 | Minor in Biological and Medical Anthropology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/42766?IDc=ARTS> |
| 18 | Minor in Biology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/30305?IDc=ARTS> |
| 19 | Minor in Biomedical Physiology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/17518?IDc=VET> |
| 20 | Minor in Birth through Kindergarten Education | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/38707?IDc=EDCN> |
| 21 | Minor in Cancer Therapeutics | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/96209?IDc=PHAR> |
| 22 | Minor in Cellular Biology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/46608?IDc=ARTS> |
| 23 | Minor in Chemistry | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/26185?IDc=ARTS> |
| 24 | Minor in Chinese Language and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/65711?IDc=ARTS> |
| 25 | Minor in Classical Culture | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/36775?IDc=ARTS> |
| 26 | Minor in Classics and Comparative Cultures | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/98428?IDc=ARTS> |
| 27 | Minor in Cognitive Science | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/85904?IDc=ARTS> |
| 28 | Minor in Communication Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/18349?IDc=ARTS> |
| 29 | Minor in Community Forestry and Arboriculture | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/58385?IDc=FRS> |
| 30 | Minor in Comparative Literature and Intercultural Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/48594?IDc=ARTS> |
| 31 | Minor in Computer Science | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/67412?IDc=ARTS> |
| 32 | Minor in Conservation Paleobiology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/86025?IDc=ARTS> |
| 33 | Minor in Consumer Economics | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/28999?IDc=FCS> |
| 34 | Minor in Criminal Justice Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/41261?IDc=ARTS> |
| 35 | Minor in Crop Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/18311?IDc=CAES> |
| 36 | Minor in Culinary Science &amp; Nutrition | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/19955?IDc=FCS> |
| 37 | Minor in Dairy Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/39665?IDc=CAES> |
| 38 | Minor in Dance | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/95376?IDc=ARTS> |
| 39 | Minor in Design and Media | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/39532?IDc=ARTS> |
| 40 | Minor in Disaster Management | College of Public Health | <https://bulletin.uga.edu/Program/Details/67736?IDc=PBHL> |
| 41 | Minor in Ecology | Odum School of Ecology | <https://bulletin.uga.edu/Program/Details/74073?IDc=ECOL> |
| 42 | Minor in Educational Psychology | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/11688?IDc=EDCN> |
| 43 | Minor in Elementary Agricultural Education | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/14383?IDc=CAES> |
| 44 | Minor in English | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/18267?IDc=ARTS> |
| 45 | Minor in Entomology | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/21125?IDc=CAES> |
| 46 | Minor in Environmental Design | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/58420?IDc=ENV> |
| 47 | Minor in Environmental Economics and Management | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/58473?IDc=CAES> |
| 48 | Minor in Environmental Geology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/51967?IDc=ARTS> |
| 49 | Minor in Environmental Health Science | College of Public Health | <https://bulletin.uga.edu/Program/Details/28020?IDc=PBHL> |
| 50 | Minor in Environmental Law | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/95465?IDc=CAES> |
| 51 | Minor in Environmental Soil Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/51188?IDc=CAES> |
| 52 | Minor in Exercise and Sport Science | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/35593?IDc=EDCN> |
| 53 | Minor in Fashion Merchandising | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/30634?IDc=FCS> |
| 54 | Minor in Film Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/85137?IDc=ARTS> |
| 55 | Minor in Fisheries and Aquatic Sciences | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/76253?IDc=FRS> |
| 56 | Minor in Food Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/31067?IDc=CAES> |
| 57 | Minor in Food and Fiber Marketing | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/63203?IDc=CAES> |
| 58 | Minor in Forestry | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/29182?IDc=FRS> |
| 59 | Minor in French | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/37834?IDc=ARTS> |
| 60 | Minor in French Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/79054?IDc=ARTS> |
| 61 | Minor in General Business | Terry College of Business | <https://bulletin.uga.edu/Program/Details/74739?IDc=BUS> |
| 62 | Minor in Genetics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/40556?IDc=ARTS> |
| 63 | Minor in Geoenergy and Mineral Resources | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/55352?IDc=ARTS> |
| 64 | Minor in Geography | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/67990?IDc=ARTS> |
| 65 | Minor in Geology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/95018?IDc=ARTS> |
| 66 | Minor in German | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/29719?IDc=ARTS> |
| 67 | Minor in Gerontology | College of Public Health | <https://bulletin.uga.edu/Program/Details/31612?IDc=PBHL> |
| 68 | Minor in Global Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/12588?IDc=PBHL> |
| 69 | Minor in Greek | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/29789?IDc=ARTS> |
| 70 | Minor in Health Policy and Management | College of Public Health | <https://bulletin.uga.edu/Program/Details/23501?IDc=PBHL> |
| 71 | Minor in Hebrew Language and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/19260?IDc=ARTS> |
| 72 | Minor in Historic Preservation | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/27660?IDc=ENV> |
| 73 | Minor in History | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/71628?IDc=ARTS> |
| 74 | Minor in History of Science, Medicine, and Engineering | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/98359?IDc=ARTS> |
| 75 | Minor in Horticulture | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/72613?IDc=CAES> |
| 76 | Minor in Housing Management &amp; Policy | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/51984?IDc=FCS> |
| 77 | Minor in Human Development and Family Science | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/15758?IDc=FCS> |
| 78 | Minor in Human Services | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/58181?IDc=EDCN> |
| 79 | Minor in Infectious Diseases | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/86503?IDc=VET> |
| 80 | Minor in International Affairs | School of Public and International Affairs | <https://bulletin.uga.edu/Program/Details/25359?IDc=SPIA> |
| 81 | Minor in International Human Rights and Security | School of Public and International Affairs | <https://bulletin.uga.edu/Program/Details/37022?IDc=SPIA> |
| 82 | Minor in Italian | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/64109?IDc=ARTS> |
| 83 | Minor in Japanese Language and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/56218?IDc=ARTS> |
| 84 | Minor in Jazz Music | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/80855?IDc=ARTS> |
| 85 | Minor in Jewish Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/94416?IDc=ARTS> |
| 86 | Minor in Korean Language and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/49831?IDc=ARTS> |
| 87 | Minor in Landscape Studies | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/89393?IDc=ENV> |
| 88 | Minor in Latin | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/57394?IDc=ARTS> |
| 89 | Minor in Latin American and Caribbean Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/99967?IDc=ARTS> |
| 90 | Minor in Latinx Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/97463?IDc=ARTS> |
| 91 | Minor in Law Ethics and Philosophy | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/10930?IDc=ARTS> |
| 92 | Minor in Law Jurisprudence and State | School of Law | <https://bulletin.uga.edu/Program/Details/13226?IDc=LAW> |
| 93 | Minor in Linguistics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/62097?IDc=ARTS> |
| 94 | Minor in Mathematics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/65181?IDc=ARTS> |
| 95 | Minor in Microbiology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/10943?IDc=ARTS> |
| 96 | Minor in Music | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/96971?IDc=ARTS> |
| 97 | Minor in Nutritional Sciences | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/48846?IDc=FCS> |
| 98 | Minor in Parks, Recreation, and Tourism Management | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/92354?IDc=FRS> |
| 99 | Minor in Personal Health &amp; Well-Being | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/32224?IDc=EDCN> |
| 100 | Minor in Pharmaceutical and Biomedical Sciences | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/81028?IDc=PHAR> |
| 101 | Minor in Philosophy | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/57294?IDc=ARTS> |
| 102 | Minor in Physics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/42728?IDc=ARTS> |
| 103 | Minor in Plant Biology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/62384?IDc=ARTS> |
| 104 | Minor in Plant Pathology | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/67940?IDc=CAES> |
| 105 | Minor in Political Science | School of Public and International Affairs | <https://bulletin.uga.edu/Program/Details/33004?IDc=SPIA> |
| 106 | Minor in Portuguese | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/57536?IDc=ARTS> |
| 107 | Minor in Poultry Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/12898?IDc=CAES> |
| 108 | Minor in Public Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/61840?IDc=PBHL> |
| 109 | Minor in Public Policy &amp; Management | School of Public and International Affairs | <https://bulletin.uga.edu/Program/Details/40349?IDc=SPIA> |
| 110 | Minor in Quechua | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/36366?IDc=ARTS> |
| 111 | Minor in Religion | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/89575?IDc=ARTS> |
| 112 | Minor in Resource Economics | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/70093?IDc=CAES> |
| 113 | Minor in Russian | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/78727?IDc=ARTS> |
| 114 | Minor in Social Work | School of Social Work | <https://bulletin.uga.edu/Program/Details/93119?IDc=SSW> |
| 115 | Minor in Sociology | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/96612?IDc=ARTS> |
| 116 | Minor in Solid Earth Dynamics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/77068?IDc=ARTS> |
| 117 | Minor in Spanish | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/94514?IDc=ARTS> |
| 118 | Minor in Sport Coaching | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/73395?IDc=EDCN> |
| 119 | Minor in Sport Management | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/78939?IDc=EDCN> |
| 120 | Minor in Statistics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/55337?IDc=ARTS> |
| 121 | Minor in Studio Art | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/92609?IDc=ARTS> |
| 122 | Minor in Swahili Language, Literature, and Culture | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/71151?IDc=ARTS> |
| 123 | Minor in Teaching English to Speakers of Other Languages | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/11400?IDc=EDCN> |
| 124 | Minor in Theatre | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/46041?IDc=ARTS> |
| 125 | Minor in Transnational European Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/36400?IDc=ARTS> |
| 126 | Minor in Turfgrass Management | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/57480?IDc=CAES> |
| 127 | Minor in Urban Planning | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/67090?IDc=ENV> |
| 128 | Minor in Vietnamese Language and Literature | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/22134?IDc=ARTS> |
| 129 | Minor in Wildlife Sciences | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/13503?IDc=FRS> |
| 130 | Minor in Women&#39;s and Gender Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/10594?IDc=ARTS> |

---

## 2. 研究生教育 (Graduate Education)

### 2.1 研究生项目 -- 按 学院 > 学位级别 分组

#### Biomedical and Translational Sciences Institute
##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | <https://bulletin.uga.edu/Program/Details/35284?IDc=BIHSI> |

#### College of Agricultural and Environmental Sciences
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agribusiness | <https://bulletin.uga.edu/Program/Details/70105?IDc=CAES> |
| 2 | Agricultural Leadership, Education, and Communication | <https://bulletin.uga.edu/Program/Details/14040?IDc=CAES> |
| 3 | Agricultural and Applied Economics | <https://bulletin.uga.edu/Program/Details/62017?IDc=CAES> |
| 4 | Animal and Dairy Science | <https://bulletin.uga.edu/Program/Details/90100?IDc=CAES> |
| 5 | Crop and Soil Sciences MS - Soil Science | <https://bulletin.uga.edu/Program/Details/69327?IDc=CAES> |
| 6 | Crop and Soil Sciences MS - Sustainable Agriculture | <https://bulletin.uga.edu/Program/Details/63197?IDc=CAES> |
| 7 | Crop and Soil Sciences MS - Weed Science | <https://bulletin.uga.edu/Program/Details/18894?IDc=CAES> |
| 8 | Entomology | <https://bulletin.uga.edu/Program/Details/37266?IDc=CAES> |
| 9 | Environmental Economics | <https://bulletin.uga.edu/Program/Details/80554?IDc=CAES> |
| 10 | Food Science | <https://bulletin.uga.edu/Program/Details/70642?IDc=CAES> |
| 11 | Food Technology | <https://bulletin.uga.edu/Program/Details/72751?IDc=CAES> |
| 12 | Horticulture | <https://bulletin.uga.edu/Program/Details/52077?IDc=CAES> |
| 13 | Plant Breeding, Genetics and Genomics | <https://bulletin.uga.edu/Program/Details/91354?IDc=CAES> |
| 14 | Plant Pathology | <https://bulletin.uga.edu/Program/Details/51011?IDc=CAES> |
| 15 | Plant Protection and Pest Management | <https://bulletin.uga.edu/Program/Details/82467?IDc=CAES> |
| 16 | Poultry Science | <https://bulletin.uga.edu/Program/Details/98600?IDc=CAES> |
| 17 | Toxicology MS - Ag | <https://bulletin.uga.edu/Program/Details/41815?IDc=CAES> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Leadership, Education, and Communication | <https://bulletin.uga.edu/Program/Details/98256?IDc=CAES> |
| 2 | Agricultural and Applied Economics | <https://bulletin.uga.edu/Program/Details/67871?IDc=CAES> |
| 3 | Animal and Dairy Science | <https://bulletin.uga.edu/Program/Details/47518?IDc=CAES> |
| 4 | Crop and Soil Sciences PHD - Soil Science | <https://bulletin.uga.edu/Program/Details/10959?IDc=CAES> |
| 5 | Crop and Soil Sciences PHD - Weed Science | <https://bulletin.uga.edu/Program/Details/95335?IDc=CAES> |
| 6 | Entomology | <https://bulletin.uga.edu/Program/Details/60664?IDc=CAES> |
| 7 | Food Science | <https://bulletin.uga.edu/Program/Details/43923?IDc=CAES> |
| 8 | Horticulture | <https://bulletin.uga.edu/Program/Details/32165?IDc=CAES> |
| 9 | Plant Breeding, Genetics and Genomics | <https://bulletin.uga.edu/Program/Details/27736?IDc=CAES> |
| 10 | Plant Pathology | <https://bulletin.uga.edu/Program/Details/79790?IDc=CAES> |
| 11 | Poultry Science | <https://bulletin.uga.edu/Program/Details/75922?IDc=CAES> |
| 12 | Regenerative Bioscience | <https://bulletin.uga.edu/Program/Details/68737?IDc=CAES> |
| 13 | Toxicology PHD - Ag | <https://bulletin.uga.edu/Program/Details/94682?IDc=CAES> |

#### College of Engineering
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Engineering | <https://bulletin.uga.edu/Program/Details/58517?IDc=FENGR> |
| 2 | Biochemical Engineering | <https://bulletin.uga.edu/Program/Details/42717?IDc=FENGR> |
| 3 | Biological Engineering | <https://bulletin.uga.edu/Program/Details/38427?IDc=FENGR> |
| 4 | Biomanufacturing and Bioprocessing | <https://bulletin.uga.edu/Program/Details/39792?IDc=FENGR> |
| 5 | Civil and Environmental Engineering MS - Civil Engineering | <https://bulletin.uga.edu/Program/Details/26542?IDc=FENGR> |
| 6 | Civil and Environmental Engineering MS - Environmental Engineering | <https://bulletin.uga.edu/Program/Details/82643?IDc=FENGR> |
| 7 | Engineering MS - Electrical and Computer Engineering | <https://bulletin.uga.edu/Program/Details/67141?IDc=FENGR> |
| 8 | Engineering MS - Mechanical Engineering | <https://bulletin.uga.edu/Program/Details/64142?IDc=FENGR> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemical Engineering | <https://bulletin.uga.edu/Program/Details/32590?IDc=FENGR> |
| 2 | Biological and Agricultural Engineering | <https://bulletin.uga.edu/Program/Details/40447?IDc=FENGR> |
| 3 | Biomedical Engineering | <https://bulletin.uga.edu/Program/Details/44059?IDc=FENGR> |
| 4 | Civil and Environmental Engineering | <https://bulletin.uga.edu/Program/Details/76366?IDc=FENGR> |
| 5 | Engineering PHD - Dynamical Systems and Control | <https://bulletin.uga.edu/Program/Details/59566?IDc=FENGR> |
| 6 | Engineering PHD - Electrical and Computer Engineering | <https://bulletin.uga.edu/Program/Details/15059?IDc=FENGR> |
| 7 | Engineering PHD - Energy Systems | <https://bulletin.uga.edu/Program/Details/61440?IDc=FENGR> |
| 8 | Engineering PHD - Engineering Education and Transformative Practice | <https://bulletin.uga.edu/Program/Details/38639?IDc=FENGR> |
| 9 | Engineering PHD - Environment and Water | <https://bulletin.uga.edu/Program/Details/68586?IDc=FENGR> |
| 10 | Engineering PHD - Fluid and Thermal Systems | <https://bulletin.uga.edu/Program/Details/96011?IDc=FENGR> |
| 11 | Engineering PHD - Mechanics and Materials | <https://bulletin.uga.edu/Program/Details/38952?IDc=FENGR> |
| 12 | Engineering PHD - Resilient Infrastructure Systems | <https://bulletin.uga.edu/Program/Details/62779?IDc=FENGR> |
| 13 | Mechanical Engineering | <https://bulletin.uga.edu/Program/Details/49528?IDc=FENGR> |

#### College of Environment and Design
##### MLA
| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | <https://bulletin.uga.edu/Program/Details/14296?IDc=ENV> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Historic Preservation | <https://bulletin.uga.edu/Program/Details/91949?IDc=ENV> |
| 2 | Urban Planning and Design | <https://bulletin.uga.edu/Program/Details/11818?IDc=ENV> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Design and Planning | <https://bulletin.uga.edu/Program/Details/74516?IDc=ENV> |

#### College of Family and Consumer Sciences
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Child Life | <https://bulletin.uga.edu/Program/Details/95232?IDc=FCS> |
| 2 | Couple and Family Therapy MS | <https://bulletin.uga.edu/Program/Details/61008?IDc=FCS> |
| 3 | Financial Planning, Housing, and Consumer Economics | <https://bulletin.uga.edu/Program/Details/79988?IDc=FCS> |
| 4 | Financial Planning, Housing, and Consumer Economics MS - Applied Consumer Analytics | <https://bulletin.uga.edu/Program/Details/35928?IDc=FCS> |
| 5 | Financial Planning, Housing, and Consumer Economics MS - Community Development | <https://bulletin.uga.edu/Program/Details/62485?IDc=FCS> |
| 6 | Financial Planning, Housing, and Consumer Economics MS - Consumer Economics | <https://bulletin.uga.edu/Program/Details/74550?IDc=FCS> |
| 7 | Financial Planning, Housing, and Consumer Economics MS - Financial Planning | <https://bulletin.uga.edu/Program/Details/54943?IDc=FCS> |
| 8 | Financial Planning, Housing, and Consumer Economics MS - Housing Management and Policy | <https://bulletin.uga.edu/Program/Details/15754?IDc=FCS> |
| 9 | Human Development and Family Science | <https://bulletin.uga.edu/Program/Details/79659?IDc=FCS> |
| 10 | Nutritional Sciences | <https://bulletin.uga.edu/Program/Details/36178?IDc=FCS> |
| 11 | Nutritional Sciences MS - Community Nutrition | <https://bulletin.uga.edu/Program/Details/15979?IDc=FCS> |
| 12 | Textiles, Merchandising and Interiors | <https://bulletin.uga.edu/Program/Details/81451?IDc=FCS> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Financial Planning, Housing and Consumer Economics | <https://bulletin.uga.edu/Program/Details/93056?IDc=FCS> |
| 2 | Human Development and Family Science | <https://bulletin.uga.edu/Program/Details/51246?IDc=FCS> |
| 3 | Nutritional Sciences | <https://bulletin.uga.edu/Program/Details/79252?IDc=FCS> |
| 4 | Polymer, Fiber, and Textile Sciences | <https://bulletin.uga.edu/Program/Details/73043?IDc=FCS> |

#### College of Pharmacy
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | <https://bulletin.uga.edu/Program/Details/32476?IDc=PHAR> |
| 2 | Pharmacy MS - Clinical Trials Management | <https://bulletin.uga.edu/Program/Details/73058?IDc=PHAR> |
| 3 | Pharmacy MS - Clinical and Experimental Therapeutics | <https://bulletin.uga.edu/Program/Details/88261?IDc=PHAR> |
| 4 | Pharmacy MS - International Biomedical Regulatory Sciences | <https://bulletin.uga.edu/Program/Details/34033?IDc=PHAR> |
| 5 | Pharmacy MS - Pharmaceutical Health Services, Outcomes, and Policy | <https://bulletin.uga.edu/Program/Details/54977?IDc=PHAR> |
| 6 | Pharmacy MS - Pharmaceutical and Biomedical Sciences | <https://bulletin.uga.edu/Program/Details/68366?IDc=PHAR> |
| 7 | Toxicology MS - Pharmacy | <https://bulletin.uga.edu/Program/Details/37530?IDc=PHAR> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy PHD - Clinical and Experimental Therapeutics | <https://bulletin.uga.edu/Program/Details/34868?IDc=PHAR> |
| 2 | Pharmacy PHD - Pharmaceutical Health Services, Outcomes, and Policy | <https://bulletin.uga.edu/Program/Details/76133?IDc=PHAR> |
| 3 | Pharmacy PHD - Pharmaceutical and Biomedical Sciences | <https://bulletin.uga.edu/Program/Details/84651?IDc=PHAR> |
| 4 | Toxicology PHD - Pharmacy | <https://bulletin.uga.edu/Program/Details/70719?IDc=PHAR> |

##### PharmD
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | <https://bulletin.uga.edu/Program/Details/49185?IDc=PHAR> |

#### College of Public Health
##### DrPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | <https://bulletin.uga.edu/Program/Details/24828?IDc=PBHL> |

##### MPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | <https://bulletin.uga.edu/Program/Details/84650?IDc=PBHL> |
| 2 | Public Health MPH - Biostatistics | <https://bulletin.uga.edu/Program/Details/72802?IDc=PBHL> |
| 3 | Public Health MPH - Disaster Management | <https://bulletin.uga.edu/Program/Details/60787?IDc=PBHL> |
| 4 | Public Health MPH - Environmental Health | <https://bulletin.uga.edu/Program/Details/96199?IDc=PBHL> |
| 5 | Public Health MPH - Epidemiology | <https://bulletin.uga.edu/Program/Details/94564?IDc=PBHL> |
| 6 | Public Health MPH - Gerontology | <https://bulletin.uga.edu/Program/Details/91623?IDc=PBHL> |
| 7 | Public Health MPH - Global Health | <https://bulletin.uga.edu/Program/Details/96784?IDc=PBHL> |
| 8 | Public Health MPH - Health Policy and Management | <https://bulletin.uga.edu/Program/Details/86133?IDc=PBHL> |
| 9 | Public Health MPH - Health Promotion and Behavior | <https://bulletin.uga.edu/Program/Details/49885?IDc=PBHL> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health | <https://bulletin.uga.edu/Program/Details/17291?IDc=PBHL> |
| 2 | Epidemiology and Biostatistics MS - Biostatistics | <https://bulletin.uga.edu/Program/Details/43863?IDc=PBHL> |
| 3 | Epidemiology and Biostatistics MS - Data Analysis and Modeling | <https://bulletin.uga.edu/Program/Details/22091?IDc=PBHL> |
| 4 | Epidemiology and Biostatistics MS - Epidemiology | <https://bulletin.uga.edu/Program/Details/56239?IDc=PBHL> |
| 5 | Health Administration | <https://bulletin.uga.edu/Program/Details/60440?IDc=PBHL> |
| 6 | Toxicology MS - Public Health | <https://bulletin.uga.edu/Program/Details/81773?IDc=PBHL> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Environmental Health Science | <https://bulletin.uga.edu/Program/Details/86113?IDc=PBHL> |
| 2 | Epidemiology and Biostatistics PHD - Biostatistics | <https://bulletin.uga.edu/Program/Details/29967?IDc=PBHL> |
| 3 | Epidemiology and Biostatistics PHD - Data Analysis and Modeling | <https://bulletin.uga.edu/Program/Details/22137?IDc=PBHL> |
| 4 | Epidemiology and Biostatistics PHD - Epidemiology | <https://bulletin.uga.edu/Program/Details/93776?IDc=PBHL> |
| 5 | Health Promotion and Behavior | <https://bulletin.uga.edu/Program/Details/80244?IDc=PBHL> |
| 6 | Health Services Research and Policy | <https://bulletin.uga.edu/Program/Details/55701?IDc=PBHL> |
| 7 | Toxicology PHD - Public Health | <https://bulletin.uga.edu/Program/Details/14602?IDc=PBHL> |

#### College of Veterinary Medicine
##### DVM
| # | 项目 | URL |
|---|------|-----|
| 1 | Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/39063?IDc=VET> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Avian Health and Medicine | <https://bulletin.uga.edu/Program/Details/21872?IDc=VET> |
| 2 | Avian Medicine | <https://bulletin.uga.edu/Program/Details/86122?IDc=VET> |
| 3 | Comparative Biomedical Sciences | <https://bulletin.uga.edu/Program/Details/27520?IDc=VET> |
| 4 | Comparative Biomedical Sciences MS - Infectious Diseases | <https://bulletin.uga.edu/Program/Details/99914?IDc=VET> |
| 5 | Comparative Biomedical Sciences MS - Integrative Biomedical Physiology | <https://bulletin.uga.edu/Program/Details/78169?IDc=VET> |
| 6 | Food Animal Medicine | <https://bulletin.uga.edu/Program/Details/31138?IDc=VET> |
| 7 | Toxicology MS - Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/73376?IDc=VET> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Biomedical Sciences | <https://bulletin.uga.edu/Program/Details/63481?IDc=VET> |
| 2 | Comparative Biomedical Sciences - Pathology | <https://bulletin.uga.edu/Program/Details/58479?IDc=VET> |
| 3 | Infectious Diseases | <https://bulletin.uga.edu/Program/Details/94254?IDc=VET> |
| 4 | Integrative Physiology and Pharmacology | <https://bulletin.uga.edu/Program/Details/37002?IDc=VET> |
| 5 | Toxicology PHD - Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/91024?IDc=VET> |

#### Franklin College of Arts and Sciences
##### DMA
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Musical Arts DMA - Composition | <https://bulletin.uga.edu/Program/Details/70117?IDc=ARTS> |
| 2 | Doctor of Musical Arts DMA - Conducting | <https://bulletin.uga.edu/Program/Details/67799?IDc=ARTS> |
| 3 | Doctor of Musical Arts DMA - Performance | <https://bulletin.uga.edu/Program/Details/71755?IDc=ARTS> |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | <https://bulletin.uga.edu/Program/Details/61317?IDc=ARTS> |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | <https://bulletin.uga.edu/Program/Details/70442?IDc=ARTS> |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | <https://bulletin.uga.edu/Program/Details/12032?IDc=ARTS> |
| 2 | Art Education | <https://bulletin.uga.edu/Program/Details/37673?IDc=ARTS> |
| 3 | Art History | <https://bulletin.uga.edu/Program/Details/38996?IDc=ARTS> |
| 4 | Classics | <https://bulletin.uga.edu/Program/Details/97406?IDc=ARTS> |
| 5 | Communication Studies | <https://bulletin.uga.edu/Program/Details/62722?IDc=ARTS> |
| 6 | Comparative Literature and Intercultural Studies | <https://bulletin.uga.edu/Program/Details/53004?IDc=ARTS> |
| 7 | English | <https://bulletin.uga.edu/Program/Details/48442?IDc=ARTS> |
| 8 | Geography | <https://bulletin.uga.edu/Program/Details/81904?IDc=ARTS> |
| 9 | German | <https://bulletin.uga.edu/Program/Details/87099?IDc=ARTS> |
| 10 | History | <https://bulletin.uga.edu/Program/Details/77118?IDc=ARTS> |
| 11 | Industrial and Organizational Psychology | <https://bulletin.uga.edu/Program/Details/29052?IDc=ARTS> |
| 12 | Linguistics | <https://bulletin.uga.edu/Program/Details/84181?IDc=ARTS> |
| 13 | Mathematics | <https://bulletin.uga.edu/Program/Details/96577?IDc=ARTS> |
| 14 | Music | <https://bulletin.uga.edu/Program/Details/55880?IDc=ARTS> |
| 15 | Philosophy | <https://bulletin.uga.edu/Program/Details/92460?IDc=ARTS> |
| 16 | Religion | <https://bulletin.uga.edu/Program/Details/87230?IDc=ARTS> |
| 17 | Romance Languages | <https://bulletin.uga.edu/Program/Details/20475?IDc=ARTS> |
| 18 | Sociology | <https://bulletin.uga.edu/Program/Details/84327?IDc=ARTS> |
| 19 | Spanish | <https://bulletin.uga.edu/Program/Details/81923?IDc=ARTS> |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | <https://bulletin.uga.edu/Program/Details/53370?IDc=ARTS> |
| 2 | Theatre | <https://bulletin.uga.edu/Program/Details/58175?IDc=ARTS> |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Music Education | <https://bulletin.uga.edu/Program/Details/89292?IDc=ARTS> |
| 2 | Music MM - Composition | <https://bulletin.uga.edu/Program/Details/87772?IDc=ARTS> |
| 3 | Music MM - Conducting | <https://bulletin.uga.edu/Program/Details/52970?IDc=ARTS> |
| 4 | Music MM - Music Therapy | <https://bulletin.uga.edu/Program/Details/92620?IDc=ARTS> |
| 5 | Music MM - Performance | <https://bulletin.uga.edu/Program/Details/81452?IDc=ARTS> |
| 6 | Music MM - Performance and Pedagogy | <https://bulletin.uga.edu/Program/Details/47280?IDc=ARTS> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematical Science | <https://bulletin.uga.edu/Program/Details/11743?IDc=ARTS> |
| 2 | Archaeological Resource Management | <https://bulletin.uga.edu/Program/Details/66328?IDc=ARTS> |
| 3 | Artificial Intelligence | <https://bulletin.uga.edu/Program/Details/19170?IDc=ARTS> |
| 4 | Cellular Biology | <https://bulletin.uga.edu/Program/Details/34995?IDc=ARTS> |
| 5 | Chemistry | <https://bulletin.uga.edu/Program/Details/89991?IDc=ARTS> |
| 6 | Computer Science | <https://bulletin.uga.edu/Program/Details/84091?IDc=ARTS> |
| 7 | Cybersecurity and Privacy | <https://bulletin.uga.edu/Program/Details/94067?IDc=ARTS> |
| 8 | Data Science | <https://bulletin.uga.edu/Program/Details/85228?IDc=ARTS> |
| 9 | Data Science MS - Applied Data Science | <https://bulletin.uga.edu/Program/Details/72922?IDc=ARTS> |
| 10 | Genetics | <https://bulletin.uga.edu/Program/Details/77772?IDc=ARTS> |
| 11 | Geography | <https://bulletin.uga.edu/Program/Details/70429?IDc=ARTS> |
| 12 | Geology | <https://bulletin.uga.edu/Program/Details/68161?IDc=ARTS> |
| 13 | Geology MS - Environmental Geology | <https://bulletin.uga.edu/Program/Details/50546?IDc=ARTS> |
| 14 | Marine Sciences | <https://bulletin.uga.edu/Program/Details/30241?IDc=ARTS> |
| 15 | Microbiology | <https://bulletin.uga.edu/Program/Details/51505?IDc=ARTS> |
| 16 | Physics | <https://bulletin.uga.edu/Program/Details/38214?IDc=ARTS> |
| 17 | Plant Biology | <https://bulletin.uga.edu/Program/Details/86001?IDc=ARTS> |
| 18 | Psychology | <https://bulletin.uga.edu/Program/Details/90212?IDc=ARTS> |
| 19 | Statistics | <https://bulletin.uga.edu/Program/Details/57980?IDc=ARTS> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | <https://bulletin.uga.edu/Program/Details/83143?IDc=ARTS> |
| 2 | Art | <https://bulletin.uga.edu/Program/Details/14714?IDc=ARTS> |
| 3 | Artificial Intelligence | <https://bulletin.uga.edu/Program/Details/56418?IDc=ARTS> |
| 4 | Biochemistry and Molecular Biology | <https://bulletin.uga.edu/Program/Details/81262?IDc=ARTS> |
| 5 | Cellular Biology | <https://bulletin.uga.edu/Program/Details/95330?IDc=ARTS> |
| 6 | Chemistry | <https://bulletin.uga.edu/Program/Details/84053?IDc=ARTS> |
| 7 | Communication Studies | <https://bulletin.uga.edu/Program/Details/54193?IDc=ARTS> |
| 8 | Comparative Literature and Intercultural Studies | <https://bulletin.uga.edu/Program/Details/97202?IDc=ARTS> |
| 9 | Computer Science | <https://bulletin.uga.edu/Program/Details/31898?IDc=ARTS> |
| 10 | English | <https://bulletin.uga.edu/Program/Details/43854?IDc=ARTS> |
| 11 | Genetics | <https://bulletin.uga.edu/Program/Details/42448?IDc=ARTS> |
| 12 | Geography | <https://bulletin.uga.edu/Program/Details/27579?IDc=ARTS> |
| 13 | Geology | <https://bulletin.uga.edu/Program/Details/30995?IDc=ARTS> |
| 14 | History | <https://bulletin.uga.edu/Program/Details/11856?IDc=ARTS> |
| 15 | Integrative Conservation PHD - Anthropology | <https://bulletin.uga.edu/Program/Details/17253?IDc=ARTS> |
| 16 | Integrative Conservation PHD - Geography | <https://bulletin.uga.edu/Program/Details/77274?IDc=ARTS> |
| 17 | Integrative Conservation PHD - Marine Science | <https://bulletin.uga.edu/Program/Details/95478?IDc=ARTS> |
| 18 | Linguistics | <https://bulletin.uga.edu/Program/Details/63836?IDc=ARTS> |
| 19 | Marine Sciences | <https://bulletin.uga.edu/Program/Details/40406?IDc=ARTS> |
| 20 | Mathematics | <https://bulletin.uga.edu/Program/Details/84380?IDc=ARTS> |
| 21 | Microbiology | <https://bulletin.uga.edu/Program/Details/61758?IDc=ARTS> |
| 22 | Music PHD - Music Education | <https://bulletin.uga.edu/Program/Details/30539?IDc=ARTS> |
| 23 | Music PHD - Musicology and Ethnomusicology | <https://bulletin.uga.edu/Program/Details/66431?IDc=ARTS> |
| 24 | Philosophy | <https://bulletin.uga.edu/Program/Details/58841?IDc=ARTS> |
| 25 | Physics | <https://bulletin.uga.edu/Program/Details/60390?IDc=ARTS> |
| 26 | Plant Biology | <https://bulletin.uga.edu/Program/Details/15671?IDc=ARTS> |
| 27 | Psychology | <https://bulletin.uga.edu/Program/Details/25082?IDc=ARTS> |
| 28 | Religion | <https://bulletin.uga.edu/Program/Details/54453?IDc=ARTS> |
| 29 | Romance Languages | <https://bulletin.uga.edu/Program/Details/31956?IDc=ARTS> |
| 30 | Sociology | <https://bulletin.uga.edu/Program/Details/33188?IDc=ARTS> |
| 31 | Statistics | <https://bulletin.uga.edu/Program/Details/99834?IDc=ARTS> |
| 32 | Theatre | <https://bulletin.uga.edu/Program/Details/11923?IDc=ARTS> |

#### Grady College of Journalism and Mass Communication
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism and Mass Communication | <https://bulletin.uga.edu/Program/Details/11702?IDc=JOUR> |
| 2 | Journalism and Mass Communication MA - Emerging Media | <https://bulletin.uga.edu/Program/Details/39766?IDc=JOUR> |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Film, Television, and Digital Media | <https://bulletin.uga.edu/Program/Details/91122?IDc=JOUR> |
| 2 | Narrative Media Writing | <https://bulletin.uga.edu/Program/Details/70157?IDc=JOUR> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Mass Communication | <https://bulletin.uga.edu/Program/Details/46467?IDc=JOUR> |

#### Institute of Bioinformatics
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | <https://bulletin.uga.edu/Program/Details/60995?IDc=BINF> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioinformatics | <https://bulletin.uga.edu/Program/Details/84240?IDc=BINF> |

#### Institute of Higher Education
##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education | <https://bulletin.uga.edu/Program/Details/72124?IDc=EDHI> |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education | <https://bulletin.uga.edu/Program/Details/50515?IDc=EDHI> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Higher Education | <https://bulletin.uga.edu/Program/Details/24514?IDc=EDHI> |

#### Mary Frances Early College of Education
##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | <https://bulletin.uga.edu/Program/Details/36187?IDc=EDCN> |
| 2 | Learning, Design, and Technology EDD | <https://bulletin.uga.edu/Program/Details/41869?IDc=EDCN> |
| 3 | Learning, Leadership and Organization Development | <https://bulletin.uga.edu/Program/Details/51167?IDc=EDCN> |
| 4 | Science Education | <https://bulletin.uga.edu/Program/Details/19944?IDc=EDCN> |
| 5 | Student Affairs Leadership | <https://bulletin.uga.edu/Program/Details/91179?IDc=EDCN> |
| 6 | Workforce Education | <https://bulletin.uga.edu/Program/Details/90826?IDc=EDCN> |

##### EdS
| # | 项目 | URL |
|---|------|-----|
| 1 | Education EDS - Art Education | <https://bulletin.uga.edu/Program/Details/34652?IDc=EDCN> |
| 2 | Education EDS - Communication Sciences and Disorders | <https://bulletin.uga.edu/Program/Details/50869?IDc=EDCN> |
| 3 | Education EDS - Elementary Education | <https://bulletin.uga.edu/Program/Details/32951?IDc=EDCN> |
| 4 | Education EDS - English Education | <https://bulletin.uga.edu/Program/Details/72981?IDc=EDCN> |
| 5 | Education EDS - Learning, Leadership and Organization Development | <https://bulletin.uga.edu/Program/Details/43353?IDc=EDCN> |
| 6 | Education EDS - Literacy Specialist | <https://bulletin.uga.edu/Program/Details/67391?IDc=EDCN> |
| 7 | Education EDS - Middle Grades Education | <https://bulletin.uga.edu/Program/Details/38152?IDc=EDCN> |
| 8 | Education EDS - Reading Education, Children&#39;s Literature and Language Arts P-5 | <https://bulletin.uga.edu/Program/Details/90872?IDc=EDCN> |
| 9 | Education EDS - Reading Education, Literature and Language Arts 6-12 | <https://bulletin.uga.edu/Program/Details/13044?IDc=EDCN> |
| 10 | Education EDS - Social Studies Education | <https://bulletin.uga.edu/Program/Details/87898?IDc=EDCN> |
| 11 | Education EDS - Special Education | <https://bulletin.uga.edu/Program/Details/11343?IDc=EDCN> |
| 12 | Education EDS - Speech-Language Pathology | <https://bulletin.uga.edu/Program/Details/66190?IDc=EDCN> |
| 13 | Education EDS - Workforce Education | <https://bulletin.uga.edu/Program/Details/94718?IDc=EDCN> |
| 14 | Education EDS - Workforce Education Advanced Preparation | <https://bulletin.uga.edu/Program/Details/88800?IDc=EDCN> |
| 15 | Education EDS - Workforce Education Teacher Preparation | <https://bulletin.uga.edu/Program/Details/20914?IDc=EDCN> |
| 16 | Education EDS - World Language Education | <https://bulletin.uga.edu/Program/Details/17672?IDc=EDCN> |
| 17 | Education EDS -Teaching English to Speakers of Other Languages | <https://bulletin.uga.edu/Program/Details/25741?IDc=EDCN> |
| 18 | Educational Administration and Policy | <https://bulletin.uga.edu/Program/Details/12649?IDc=EDCN> |
| 19 | Educational Psychology EDS - Applied Cognition and Development | <https://bulletin.uga.edu/Program/Details/19835?IDc=EDCN> |
| 20 | Educational Psychology EDS - Gifted and Creative Education | <https://bulletin.uga.edu/Program/Details/53218?IDc=EDCN> |
| 21 | Educational Psychology EDS - Quantitative Methodology | <https://bulletin.uga.edu/Program/Details/25790?IDc=EDCN> |
| 22 | Educational Psychology EDS - School Psychology | <https://bulletin.uga.edu/Program/Details/67640?IDc=EDCN> |
| 23 | Learning, Design and Technology | <https://bulletin.uga.edu/Program/Details/41089?IDc=EDCN> |
| 24 | Mathematics Education EDS - Grades 6-12 | <https://bulletin.uga.edu/Program/Details/73816?IDc=EDCN> |
| 25 | Mathematics Education EDS - PreK - 8 | <https://bulletin.uga.edu/Program/Details/41036?IDc=EDCN> |
| 26 | Professional School Counseling | <https://bulletin.uga.edu/Program/Details/13680?IDc=EDCN> |
| 27 | Science Education | <https://bulletin.uga.edu/Program/Details/65078?IDc=EDCN> |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | <https://bulletin.uga.edu/Program/Details/13568?IDc=EDCN> |
| 2 | Education MA - Elementary Education | <https://bulletin.uga.edu/Program/Details/82816?IDc=EDCN> |
| 3 | Education MA - Literacies and Children&#39;s Literature | <https://bulletin.uga.edu/Program/Details/21409?IDc=EDCN> |
| 4 | Education MA - Mathematics Education | <https://bulletin.uga.edu/Program/Details/27852?IDc=EDCN> |
| 5 | Education MA - Middle Grades Education | <https://bulletin.uga.edu/Program/Details/72320?IDc=EDCN> |
| 6 | Education MA - Science Education | <https://bulletin.uga.edu/Program/Details/15918?IDc=EDCN> |
| 7 | Education MA - Social Studies Education | <https://bulletin.uga.edu/Program/Details/23624?IDc=EDCN> |
| 8 | Education MA - Special Education General Curriculum | <https://bulletin.uga.edu/Program/Details/33747?IDc=EDCN> |
| 9 | Education MA - Special Education/Adapted Curriculum | <https://bulletin.uga.edu/Program/Details/32837?IDc=EDCN> |
| 10 | Education MA - Special Education/Birth Through Kindergarten | <https://bulletin.uga.edu/Program/Details/74290?IDc=EDCN> |
| 11 | Educational Psychology MA - Applied Cognition and Development | <https://bulletin.uga.edu/Program/Details/26929?IDc=EDCN> |
| 12 | Educational Psychology MA - Gifted and Creative Education | <https://bulletin.uga.edu/Program/Details/34420?IDc=EDCN> |
| 13 | Educational Psychology MA - Quantitative Methodology | <https://bulletin.uga.edu/Program/Details/14408?IDc=EDCN> |

##### MAT
| # | 项目 | URL |
|---|------|-----|
| 1 | Elementary Education | <https://bulletin.uga.edu/Program/Details/65697?IDc=EDCN> |
| 2 | English Education | <https://bulletin.uga.edu/Program/Details/47220?IDc=EDCN> |
| 3 | Mathematics Education | <https://bulletin.uga.edu/Program/Details/53966?IDc=EDCN> |
| 4 | Middle Grades Education MAT | <https://bulletin.uga.edu/Program/Details/50912?IDc=EDCN> |
| 5 | Science Education | <https://bulletin.uga.edu/Program/Details/95847?IDc=EDCN> |
| 6 | Social Studies Education | <https://bulletin.uga.edu/Program/Details/55160?IDc=EDCN> |
| 7 | Special Education MAT - Adapted Curriculum and Autism | <https://bulletin.uga.edu/Program/Details/44447?IDc=EDCN> |
| 8 | Special Education MAT - Birth Through Five/Preschool Special Education | <https://bulletin.uga.edu/Program/Details/66621?IDc=EDCN> |
| 9 | Special Education MAT - Early Childhood Education/Special Education General Curriculum P-5 | <https://bulletin.uga.edu/Program/Details/21046?IDc=EDCN> |
| 10 | Special Education MAT - Special Education General Curriculum | <https://bulletin.uga.edu/Program/Details/99135?IDc=EDCN> |
| 11 | TESOL and World Language Education MAT - TESOL | <https://bulletin.uga.edu/Program/Details/16811?IDc=EDCN> |
| 12 | TESOL and World Language Education MAT - World Language Education | <https://bulletin.uga.edu/Program/Details/74443?IDc=EDCN> |
| 13 | Workforce Education MAT - Business Education | <https://bulletin.uga.edu/Program/Details/87211?IDc=EDCN> |
| 14 | Workforce Education MAT - Engineering and Technology Education | <https://bulletin.uga.edu/Program/Details/97417?IDc=EDCN> |
| 15 | Workforce Education MAT - Family and Consumer Sciences Education | <https://bulletin.uga.edu/Program/Details/26200?IDc=EDCN> |
| 16 | Workforce Education MAT - Healthcare Science and Technology Education | <https://bulletin.uga.edu/Program/Details/99207?IDc=EDCN> |
| 17 | Workforce Education MAT - Marketing Education | <https://bulletin.uga.edu/Program/Details/16215?IDc=EDCN> |
| 18 | Workforce Education MAT - Trade and Industrial Education | <https://bulletin.uga.edu/Program/Details/94891?IDc=EDCN> |

##### MEd
| # | 项目 | URL |
|---|------|-----|
| 1 | College Student Affairs Administration | <https://bulletin.uga.edu/Program/Details/57149?IDc=EDCN> |
| 2 | Communication Sciences and Disorders | <https://bulletin.uga.edu/Program/Details/97519?IDc=EDCN> |
| 3 | Educational Administration and Policy | <https://bulletin.uga.edu/Program/Details/70700?IDc=EDCN> |
| 4 | Educational Administration and Policy MED - Research | <https://bulletin.uga.edu/Program/Details/32193?IDc=EDCN> |
| 5 | Educational Administration and Policy MED - Tier I Leadership Certification | <https://bulletin.uga.edu/Program/Details/81241?IDc=EDCN> |
| 6 | Educational Psychology MED - Applied Cognition and Development | <https://bulletin.uga.edu/Program/Details/60057?IDc=EDCN> |
| 7 | Educational Psychology MED - Gifted and Creative Education | <https://bulletin.uga.edu/Program/Details/25881?IDc=EDCN> |
| 8 | Educational Psychology MED - Quantitative Methodology | <https://bulletin.uga.edu/Program/Details/25674?IDc=EDCN> |
| 9 | Elementary Education | <https://bulletin.uga.edu/Program/Details/58828?IDc=EDCN> |
| 10 | English Education | <https://bulletin.uga.edu/Program/Details/89919?IDc=EDCN> |
| 11 | Learning, Design, and Technology MED - Instructional Design and Development | <https://bulletin.uga.edu/Program/Details/93275?IDc=EDCN> |
| 12 | Learning, Design, and Technology MED - Instructional Technology | <https://bulletin.uga.edu/Program/Details/70363?IDc=EDCN> |
| 13 | Learning, Design, and Technology MED - Research-Oriented Learning Design | <https://bulletin.uga.edu/Program/Details/94478?IDc=EDCN> |
| 14 | Learning, Leadership and Organization Development | <https://bulletin.uga.edu/Program/Details/42656?IDc=EDCN> |
| 15 | Mathematics Education MED - Grades 6-12 | <https://bulletin.uga.edu/Program/Details/36177?IDc=EDCN> |
| 16 | Mathematics Education MED - PreK - 8 | <https://bulletin.uga.edu/Program/Details/54458?IDc=EDCN> |
| 17 | Middle Grades Education MED | <https://bulletin.uga.edu/Program/Details/69518?IDc=EDCN> |
| 18 | Professional Counseling MED - Mental Health Counseling | <https://bulletin.uga.edu/Program/Details/93929?IDc=EDCN> |
| 19 | Professional Counseling MED - School Counseling | <https://bulletin.uga.edu/Program/Details/76896?IDc=EDCN> |
| 20 | Reading Education MED - 6-12 Secondary Teaching | <https://bulletin.uga.edu/Program/Details/59255?IDc=EDCN> |
| 21 | Reading Education MED - Children&#39;s Literature and Language Arts | <https://bulletin.uga.edu/Program/Details/15872?IDc=EDCN> |
| 22 | Reading Education MED - New and Digital Literacy 6-12 | <https://bulletin.uga.edu/Program/Details/53162?IDc=EDCN> |
| 23 | Reading Education MED - New and Digital Literacy P-5 | <https://bulletin.uga.edu/Program/Details/66853?IDc=EDCN> |
| 24 | Reading Education MED - P-5 Elementary Teaching | <https://bulletin.uga.edu/Program/Details/95868?IDc=EDCN> |
| 25 | Science Education | <https://bulletin.uga.edu/Program/Details/47099?IDc=EDCN> |
| 26 | Social Studies Education | <https://bulletin.uga.edu/Program/Details/74478?IDc=EDCN> |
| 27 | Special Education MED - Adapted Curriculum and Autism | <https://bulletin.uga.edu/Program/Details/31317?IDc=EDCN> |
| 28 | Special Education MED - Birth Through Five/Preschool Special Education | <https://bulletin.uga.edu/Program/Details/89830?IDc=EDCN> |
| 29 | Special Education MED - Early Childhood Education/Special Education General Curriculum P-5 | <https://bulletin.uga.edu/Program/Details/52729?IDc=EDCN> |
| 30 | Special Education MED - Special Education General Curriculum | <https://bulletin.uga.edu/Program/Details/67651?IDc=EDCN> |
| 31 | TESOL and World Language Education | <https://bulletin.uga.edu/Program/Details/75760?IDc=EDCN> |
| 32 | Workforce Education | <https://bulletin.uga.edu/Program/Details/72333?IDc=EDCN> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | <https://bulletin.uga.edu/Program/Details/59790?IDc=EDCN> |
| 2 | Athletic Training | <https://bulletin.uga.edu/Program/Details/57549?IDc=EDCN> |
| 3 | Kinesiology MS - Adapted Physical Education | <https://bulletin.uga.edu/Program/Details/22562?IDc=EDCN> |
| 4 | Kinesiology MS - Exercise Science | <https://bulletin.uga.edu/Program/Details/85629?IDc=EDCN> |
| 5 | Kinesiology MS - Physical Education | <https://bulletin.uga.edu/Program/Details/94658?IDc=EDCN> |
| 6 | Kinesiology MS - Sport Management and Policy | <https://bulletin.uga.edu/Program/Details/90674?IDc=EDCN> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Sciences and Disorders | <https://bulletin.uga.edu/Program/Details/52767?IDc=EDCN> |
| 2 | Counseling Psychology | <https://bulletin.uga.edu/Program/Details/94620?IDc=EDCN> |
| 3 | Education PHD - College Student Affairs Administration | <https://bulletin.uga.edu/Program/Details/86247?IDc=EDCN> |
| 4 | Education PHD - Counselor Education and Supervision | <https://bulletin.uga.edu/Program/Details/57875?IDc=EDCN> |
| 5 | Education PHD - Social Studies Education | <https://bulletin.uga.edu/Program/Details/33242?IDc=EDCN> |
| 6 | Educational Administration and Policy | <https://bulletin.uga.edu/Program/Details/56041?IDc=EDCN> |
| 7 | Educational Psychology PHD - Applied Cognition and Development | <https://bulletin.uga.edu/Program/Details/33860?IDc=EDCN> |
| 8 | Educational Psychology PHD - Gifted and Creative Education | <https://bulletin.uga.edu/Program/Details/67429?IDc=EDCN> |
| 9 | Educational Psychology PHD - Quantitative Methodology | <https://bulletin.uga.edu/Program/Details/11446?IDc=EDCN> |
| 10 | Educational Psychology PHD - School Psychology | <https://bulletin.uga.edu/Program/Details/52074?IDc=EDCN> |
| 11 | Educational Theory and Practice PHD - Critical Studies in Educational Theory and Practice | <https://bulletin.uga.edu/Program/Details/85542?IDc=EDCN> |
| 12 | Educational Theory and Practice PHD - Early Childhood Education | <https://bulletin.uga.edu/Program/Details/98311?IDc=EDCN> |
| 13 | Educational Theory and Practice PHD - Elementary Education | <https://bulletin.uga.edu/Program/Details/64251?IDc=EDCN> |
| 14 | Educational Theory and Practice PHD - Middle Grades Education | <https://bulletin.uga.edu/Program/Details/57719?IDc=EDCN> |
| 15 | Educational Theory and Practice PHD - Teacher Education | <https://bulletin.uga.edu/Program/Details/76263?IDc=EDCN> |
| 16 | Kinesiology PHD - Exercise Science | <https://bulletin.uga.edu/Program/Details/62901?IDc=EDCN> |
| 17 | Kinesiology PHD - Physical Education | <https://bulletin.uga.edu/Program/Details/54425?IDc=EDCN> |
| 18 | Kinesiology PHD - Sport Management and Policy | <https://bulletin.uga.edu/Program/Details/68019?IDc=EDCN> |
| 19 | Language and Literacy Education PHD - Reading Education, Children&#39;s Literature and Language Arts 6-12 | <https://bulletin.uga.edu/Program/Details/21335?IDc=EDCN> |
| 20 | Language and Literacy Education PHD - Reading Education, Children&#39;s Literature and Language Arts P-5 | <https://bulletin.uga.edu/Program/Details/53767?IDc=EDCN> |
| 21 | Language and Literacy Education PHD - Teaching English to Speakers of Other Languages | <https://bulletin.uga.edu/Program/Details/40257?IDc=EDCN> |
| 22 | Language and Literacy Education PHD - World Language Education | <https://bulletin.uga.edu/Program/Details/74322?IDc=EDCN> |
| 23 | Language and Literacy Education PHD -English Education | <https://bulletin.uga.edu/Program/Details/62947?IDc=EDCN> |
| 24 | Learning, Design and Technology | <https://bulletin.uga.edu/Program/Details/91997?IDc=EDCN> |
| 25 | Learning, Leadership and Organization Development | <https://bulletin.uga.edu/Program/Details/46386?IDc=EDCN> |
| 26 | Mathematics Education | <https://bulletin.uga.edu/Program/Details/36223?IDc=EDCN> |
| 27 | Qualitative Research and Evaluation Methodologies | <https://bulletin.uga.edu/Program/Details/44296?IDc=EDCN> |
| 28 | Science Education | <https://bulletin.uga.edu/Program/Details/16152?IDc=EDCN> |
| 29 | Special Education | <https://bulletin.uga.edu/Program/Details/65350?IDc=EDCN> |
| 30 | Workforce Education | <https://bulletin.uga.edu/Program/Details/52946?IDc=EDCN> |

#### Odum School of Ecology
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology | <https://bulletin.uga.edu/Program/Details/74212?IDc=ECOL> |
| 2 | Ecology MS - Integrative Conservation and Sustainability | <https://bulletin.uga.edu/Program/Details/28459?IDc=ECOL> |
| 3 | Toxicology - Ecology | <https://bulletin.uga.edu/Program/Details/37657?IDc=ECOL> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Ecology | <https://bulletin.uga.edu/Program/Details/42196?IDc=ECOL> |
| 2 | Integrative Conservation PHD - Ecology | <https://bulletin.uga.edu/Program/Details/67502?IDc=ECOL> |
| 3 | Toxicology - Ecology | <https://bulletin.uga.edu/Program/Details/21595?IDc=ECOL> |

#### School of Law
##### JD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | <https://bulletin.uga.edu/Program/Details/42178?IDc=LAW> |

##### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Laws | <https://bulletin.uga.edu/Program/Details/92303?IDc=LAW> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | <https://bulletin.uga.edu/Program/Details/78108?IDc=LAW> |

#### School of Public and International Affairs
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science and International Affairs | <https://bulletin.uga.edu/Program/Details/53924?IDc=SPIA> |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | <https://bulletin.uga.edu/Program/Details/76704?IDc=SPIA> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | International Policy | <https://bulletin.uga.edu/Program/Details/95832?IDc=SPIA> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science and International Affairs | <https://bulletin.uga.edu/Program/Details/19295?IDc=SPIA> |
| 2 | Public Administration | <https://bulletin.uga.edu/Program/Details/11488?IDc=SPIA> |

#### School of Social Work
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Management and Leadership | <https://bulletin.uga.edu/Program/Details/21338?IDc=SSW> |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | <https://bulletin.uga.edu/Program/Details/56199?IDc=SSW> |
| 2 | Social Work MSW - Athens Advanced Combined | <https://bulletin.uga.edu/Program/Details/80350?IDc=SSW> |
| 3 | Social Work MSW - Athens Advanced Macro | <https://bulletin.uga.edu/Program/Details/24376?IDc=SSW> |
| 4 | Social Work MSW - Athens Advanced Micro | <https://bulletin.uga.edu/Program/Details/20723?IDc=SSW> |
| 5 | Social Work MSW - Athens Combined | <https://bulletin.uga.edu/Program/Details/75586?IDc=SSW> |
| 6 | Social Work MSW - Athens Macro | <https://bulletin.uga.edu/Program/Details/66777?IDc=SSW> |
| 7 | Social Work MSW - Athens Micro | <https://bulletin.uga.edu/Program/Details/35730?IDc=SSW> |
| 8 | Social Work MSW - Gwinnett Advanced | <https://bulletin.uga.edu/Program/Details/45939?IDc=SSW> |
| 9 | Social Work MSW - Gwinnett Micro | <https://bulletin.uga.edu/Program/Details/17184?IDc=SSW> |
| 10 | Social Work MSW - Online Micro | <https://bulletin.uga.edu/Program/Details/81628?IDc=SSW> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | <https://bulletin.uga.edu/Program/Details/42188?IDc=SSW> |

#### Terry College of Business
##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Economics | <https://bulletin.uga.edu/Program/Details/81555?IDc=BUS> |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | <https://bulletin.uga.edu/Program/Details/92389?IDc=BUS> |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | <https://bulletin.uga.edu/Program/Details/35960?IDc=BUS> |
| 2 | Accounting | <https://bulletin.uga.edu/Program/Details/19997?IDc=BUS> |
| 3 | Business Analytics | <https://bulletin.uga.edu/Program/Details/34156?IDc=BUS> |
| 4 | Business and Technology | <https://bulletin.uga.edu/Program/Details/19049?IDc=BUS> |
| 5 | Marketing Research | <https://bulletin.uga.edu/Program/Details/85706?IDc=BUS> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | <https://bulletin.uga.edu/Program/Details/61245?IDc=BUS> |
| 2 | Economics | <https://bulletin.uga.edu/Program/Details/34752?IDc=BUS> |

#### Warnell School of Forestry and Natural Resources
##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Forest Resources MFR - Forest Business | <https://bulletin.uga.edu/Program/Details/37144?IDc=FRS> |
| 2 | Forest Resources MFR - Forestry | <https://bulletin.uga.edu/Program/Details/26395?IDc=FRS> |
| 3 | Forestry and Natural Resources MS | <https://bulletin.uga.edu/Program/Details/16035?IDc=FRS> |
| 4 | Forestry and Natural Resources MS - Community Forestry and Arboriculture | <https://bulletin.uga.edu/Program/Details/20415?IDc=FRS> |
| 5 | Forestry and Natural Resources MS - Forest Biology | <https://bulletin.uga.edu/Program/Details/21452?IDc=FRS> |
| 6 | Forestry and Natural Resources MS - Geospatial Information Science | <https://bulletin.uga.edu/Program/Details/13388?IDc=FRS> |
| 7 | Forestry and Natural Resources MS - Policy and Sustainability | <https://bulletin.uga.edu/Program/Details/63188?IDc=FRS> |
| 8 | Forestry and Natural Resources MS - Wildlife Science | <https://bulletin.uga.edu/Program/Details/51075?IDc=FRS> |
| 9 | Natural Resources MNR | <https://bulletin.uga.edu/Program/Details/27885?IDc=FRS> |
| 10 | Natural Resources MNR - Community Forestry and Arboriculture | <https://bulletin.uga.edu/Program/Details/75180?IDc=FRS> |
| 11 | Natural Resources MNR - Environmental Education | <https://bulletin.uga.edu/Program/Details/71602?IDc=FRS> |
| 12 | Natural Resources MNR - Fisheries Science | <https://bulletin.uga.edu/Program/Details/28157?IDc=FRS> |
| 13 | Natural Resources MNR - Forest Biology | <https://bulletin.uga.edu/Program/Details/52603?IDc=FRS> |
| 14 | Natural Resources MNR - Geospatial Information Science | <https://bulletin.uga.edu/Program/Details/85733?IDc=FRS> |
| 15 | Natural Resources MNR - Parks, Recreation, and Tourism Management | <https://bulletin.uga.edu/Program/Details/47408?IDc=FRS> |
| 16 | Natural Resources MNR - Water and Soil Science | <https://bulletin.uga.edu/Program/Details/18221?IDc=FRS> |
| 17 | Natural Resources MNR - Wildlife Science | <https://bulletin.uga.edu/Program/Details/30742?IDc=FRS> |
| 18 | Toxicology MS - Forestry | <https://bulletin.uga.edu/Program/Details/81403?IDc=FRS> |

##### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Forestry and Natural Resources PHD | <https://bulletin.uga.edu/Program/Details/38805?IDc=FRS> |
| 2 | Forestry and Natural Resources PHD - Community Forestry and Arboriculture | <https://bulletin.uga.edu/Program/Details/18425?IDc=FRS> |
| 3 | Forestry and Natural Resources PHD - Forest Biology | <https://bulletin.uga.edu/Program/Details/29804?IDc=FRS> |
| 4 | Forestry and Natural Resources PHD - Geospatial Information Science | <https://bulletin.uga.edu/Program/Details/94262?IDc=FRS> |
| 5 | Forestry and Natural Resources PHD - Wildlife Science | <https://bulletin.uga.edu/Program/Details/71824?IDc=FRS> |
| 6 | Integrative Conservation PHD - Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/56533?IDc=FRS> |
| 7 | Toxicology PHD - Forestry | <https://bulletin.uga.edu/Program/Details/60069?IDc=FRS> |

### 2.2 研究生证书 (Graduate Certificates)

| # | 证书名称 | 学院 | URL |
|---|----------|------|-----|
| 1 | African American Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/27654?IDc=ARTS> |
| 2 | Graduate Certificate in African Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/62814?IDc=ARTS> |
| 3 | Graduate Certificate in Agricultural Data Science | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/97530?IDc=CAES> |
| 4 | Graduate Certificate in Alternative Dispute Resolution | School of Law | <https://bulletin.uga.edu/Program/Details/80853?IDc=LAW> |
| 5 | Graduate Certificate in Atmospheric Sciences | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/63588?IDc=ARTS> |
| 6 | Graduate Certificate in Avian Health | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/15236?IDc=VET> |
| 7 | Graduate Certificate in Behavioral Financial Planning and Financial Therapy | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/73422?IDc=FCS> |
| 8 | Graduate Certificate in Bioinformatics | Institute of Bioinformatics | <https://bulletin.uga.edu/Program/Details/11115?IDc=BINF> |
| 9 | Graduate Certificate in Chemistry, Manufacturing, and Controls | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/44974?IDc=PHAR> |
| 10 | Graduate Certificate in Classical Music Recording | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/35476?IDc=ARTS> |
| 11 | Graduate Certificate in Clinical Internship - Diagnostic Medicine | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/30625?IDc=VET> |
| 12 | Graduate Certificate in Clinical Internship - Large Animal Hospital Rotating Intern | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/12114?IDc=VET> |
| 13 | Graduate Certificate in Clinical Internship - Small Animal Internal Medicine | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/21990?IDc=VET> |
| 14 | Graduate Certificate in Clinical Residency - Cardiology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/11194?IDc=VET> |
| 15 | Graduate Certificate in Clinical Residency - Clinical Microbiology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/80652?IDc=VET> |
| 16 | Graduate Certificate in Clinical Residency - Dermatology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/59085?IDc=VET> |
| 17 | Graduate Certificate in Clinical Residency - Laboratory Animal Medicine | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/18316?IDc=VET> |
| 18 | Graduate Certificate in Clinical Residency - Large Animal Surgery and Emergency Critical Care | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/31088?IDc=VET> |
| 19 | Graduate Certificate in Clinical Residency - Oncology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/47223?IDc=VET> |
| 20 | Graduate Certificate in Clinical Residency - Ophthalmology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/78993?IDc=VET> |
| 21 | Graduate Certificate in Clinical Residency - Small Animal Internal Medicine | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/11468?IDc=VET> |
| 22 | Graduate Certificate in Clinical Residency - Small Animal Surgery | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/50933?IDc=VET> |
| 23 | Graduate Certificate in Clinical Residency - Small Animal Veterinary Radiology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/56062?IDc=VET> |
| 24 | Graduate Certificate in Clinical Residency - Veterinary Neurology and Neurosurgery | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/36546?IDc=VET> |
| 25 | Graduate Certificate in Clinical Residency - Zoological Medicine | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/54845?IDc=VET> |
| 26 | Graduate Certificate in Clinical Residency in Pharmacy: PGY-1 | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/20627?IDc=PHAR> |
| 27 | Graduate Certificate in Clinical Residency in Pharmacy: PGY-2 | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/47611?IDc=PHAR> |
| 28 | Graduate Certificate in Clinical Trials Design and Management | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/29279?IDc=PHAR> |
| 29 | Graduate Certificate in Coaching Mathematics | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/23902?IDc=EDCN> |
| 30 | Graduate Certificate in Coastal and Oceanographic Engineering | College of Engineering | <https://bulletin.uga.edu/Program/Details/58470?IDc=FENGR> |
| 31 | Graduate Certificate in Comparative Medical Illustration and Interactive Educational Media | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/82640?IDc=VET> |
| 32 | Graduate Certificate in Complexity Leadership | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/21841?IDc=EDCN> |
| 33 | Graduate Certificate in Conservation Ecology and Sustainable Development | Odum School of Ecology | <https://bulletin.uga.edu/Program/Details/24177?IDc=ECOL> |
| 34 | Graduate Certificate in Crisis, Risk, and Disaster Communication | College of Public Health | <https://bulletin.uga.edu/Program/Details/22380?IDc=PBHL> |
| 35 | Graduate Certificate in Cultural Landscape Conservation | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/17417?IDc=ENV> |
| 36 | Graduate Certificate in Cybersecurity | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/33385?IDc=ARTS> |
| 37 | Graduate Certificate in Disability Studies | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/64411?IDc=FCS> |
| 38 | Graduate Certificate in Disaster Management | College of Public Health | <https://bulletin.uga.edu/Program/Details/89077?IDc=PBHL> |
| 39 | Graduate Certificate in Diversity, Equity, and Inclusion | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/50921?IDc=EDCN> |
| 40 | Graduate Certificate in Drug Safety and Pharmacovigilance | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/79796?IDc=PHAR> |
| 41 | Graduate Certificate in Dyslexia | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/83200?IDc=EDCN> |
| 42 | Graduate Certificate in Educational Law and Policy | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/73672?IDc=EDCN> |
| 43 | Graduate Certificate in Educational Leadership Tier I | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/22793?IDc=EDCN> |
| 44 | Graduate Certificate in English to Speakers of Other Languages | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/23101?IDc=EDCN> |
| 45 | Graduate Certificate in Entrepreneurship | Terry College of Business | <https://bulletin.uga.edu/Program/Details/81276?IDc=BUS> |
| 46 | Graduate Certificate in Environmental Ethics | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/97062?IDc=ARTS> |
| 47 | Graduate Certificate in Film and Media Scoring | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/71936?IDc=ARTS> |
| 48 | Graduate Certificate in Financial Literacy | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/83860?IDc=FCS> |
| 49 | Graduate Certificate in Geographic Information Science | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/61659?IDc=ARTS> |
| 50 | Graduate Certificate in Gerontology | College of Public Health | <https://bulletin.uga.edu/Program/Details/19261?IDc=PBHL> |
| 51 | Graduate Certificate in Gifted In-Field | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/81056?IDc=EDCN> |
| 52 | Graduate Certificate in Global Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/25004?IDc=PBHL> |
| 53 | Graduate Certificate in Historic Preservation Studies | College of Environment and Design | <https://bulletin.uga.edu/Program/Details/40551?IDc=ENV> |
| 54 | Graduate Certificate in Instructional Technology for Teaching | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/70304?IDc=EDCN> |
| 55 | Graduate Certificate in International Agriculture | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/26370?IDc=CAES> |
| 56 | Graduate Certificate in International Biomedical Regulatory Sciences | College of Pharmacy | <https://bulletin.uga.edu/Program/Details/26324?IDc=PHAR> |
| 57 | Graduate Certificate in International Law | School of Law | <https://bulletin.uga.edu/Program/Details/62799?IDc=LAW> |
| 58 | Graduate Certificate in K-5 Mathematics | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/75515?IDc=EDCN> |
| 59 | Graduate Certificate in Latin American and Caribbean Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/12470?IDc=ARTS> |
| 60 | Graduate Certificate in Mathematics Education | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/30862?IDc=EDCN> |
| 61 | Graduate Certificate in Media Analytics | Grady College of Journalism and Mass Communication | <https://bulletin.uga.edu/Program/Details/60181?IDc=JOUR> |
| 62 | Graduate Certificate in Museum Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/22295?IDc=ARTS> |
| 63 | Graduate Certificate in Music Performance | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/29863?IDc=ARTS> |
| 64 | Graduate Certificate in Native American Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/28474?IDc=ARTS> |
| 65 | Graduate Certificate in Natural Infrastructure | College of Engineering | <https://bulletin.uga.edu/Program/Details/74081?IDc=FENGR> |
| 66 | Graduate Certificate in New Media | Grady College of Journalism and Mass Communication | <https://bulletin.uga.edu/Program/Details/84273?IDc=JOUR> |
| 67 | Graduate Certificate in Nonprofit Management and Leadership | School of Social Work | <https://bulletin.uga.edu/Program/Details/83528?IDc=SSW> |
| 68 | Graduate Certificate in Obesity and Weight Management - Counseling and Human Development | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/72191?IDc=EDCN> |
| 69 | Graduate Certificate in Obesity and Weight Management - Kinesiology | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/31829?IDc=EDCN> |
| 70 | Graduate Certificate in Obesity and Weight Management - Nutritional Sciences | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/22229?IDc=FCS> |
| 71 | Graduate Certificate in Obesity and Weight Management - Public Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/96623?IDc=PBHL> |
| 72 | Graduate Certificate in Online Teaching and Learning | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/90443?IDc=EDCN> |
| 73 | Graduate Certificate in Organization Coaching | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/49198?IDc=EDCN> |
| 74 | Graduate Certificate in Pre-Professional Speech Language Pathology | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/27813?IDc=EDCN> |
| 75 | Graduate Certificate in Preschool Special Education | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/60339?IDc=EDCN> |
| 76 | Graduate Certificate in Public Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/85806?IDc=PBHL> |
| 77 | Graduate Certificate in Qualitative Studies | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/97375?IDc=EDCN> |
| 78 | Graduate Certificate in Quantitative Methods in Family and Social Sciences | College of Family and Consumer Sciences | <https://bulletin.uga.edu/Program/Details/48236?IDc=FCS> |
| 79 | Graduate Certificate in Reading Education | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/35917?IDc=EDCN> |
| 80 | Graduate Certificate in Residency in Pathology - Veterinary Anatomic Pathology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/76137?IDc=VET> |
| 81 | Graduate Certificate in Residency in Pathology - Veterinary Clinical Pathology | College of Veterinary Medicine | <https://bulletin.uga.edu/Program/Details/59714?IDc=VET> |
| 82 | Graduate Certificate in STEM Education | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/82698?IDc=EDCN> |
| 83 | Graduate Certificate in Science and Health Communication | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/29500?IDc=ARTS> |
| 84 | Graduate Certificate in Social Determinants of Health | College of Public Health | <https://bulletin.uga.edu/Program/Details/12131?IDc=PBHL> |
| 85 | Graduate Certificate in Substance Use Counseling | School of Social Work | <https://bulletin.uga.edu/Program/Details/49089?IDc=SSW> |
| 86 | Graduate Certificate in Sustainability | Odum School of Ecology | <https://bulletin.uga.edu/Program/Details/65459?IDc=ECOL> |
| 87 | Graduate Certificate in Sustainable Food Systems | College of Agricultural and Environmental Sciences | <https://bulletin.uga.edu/Program/Details/29986?IDc=CAES> |
| 88 | Graduate Certificate in Suzuki Violin Pedagogy | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/78284?IDc=ARTS> |
| 89 | Graduate Certificate in Teaching English to Speakers of Other Languages | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/56812?IDc=EDCN> |
| 90 | Graduate Certificate in University Teaching | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/59843?IDc=EDCN> |
| 91 | Graduate Certificate in Urban and Metropolitan Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/88973?IDc=ARTS> |
| 92 | Graduate Certificate in Water Resources | Warnell School of Forestry and Natural Resources | <https://bulletin.uga.edu/Program/Details/29502?IDc=FRS> |
| 93 | Graduate Certificate in Women&#39;s and Gender Studies | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/88907?IDc=ARTS> |
| 94 | Graduate Certificate in eLearning Design | Mary Frances Early College of Education | <https://bulletin.uga.edu/Program/Details/90208?IDc=EDCN> |
| 95 | Post-Baccalaureate Certificate in Studio Furniture Design and Fabrication | Franklin College of Arts and Sciences | <https://bulletin.uga.edu/Program/Details/28713?IDc=ARTS> |

---

## 3. 申请要求与截止日期 (Application Requirements & Deadlines)

### 3.1 本科 -- 核心数据表

| 维度 | 详情 |
|------|------|
| 申请系统 | Common App (秋季); UGA Application (春季/转学) |
| EA 截止日期 | October 15 |
| EA 材料截止日期 | October 29 |
| RD 截止日期 | January 1 |
| RD 材料截止日期 | January 15 |
| EA 决定发布 | In-state: Mid-Late November; OOS: Mid December |
| RD 决定发布 | Mid March |
| 押金截止日期 | May 1 |
| 申请费 (US Citizens) | $70 |
| 申请费 (International) | $85 |
| SAT/ACT 要求 | **REQUIRED** -- 不是 test-optional |
| Superscore | Yes |
| 推荐信 | Optional |
| 面试 | None |

> **重要发现**: UGA **不是** test-optional。官方明确声明: 'All first-year and dual enrollment applicants are required to submit official test scores from either ACT or SAT. There is no test optional pathway to UGA.'

### 3.2 本科英语能力要求 (International English Proficiency)

| 考试 | 最低要求 | 推荐分数 |
|------|----------|----------|
| TOEFL iBT | TBD (behind accordion - P0 follow-up) | - |
| IELTS | TBD (behind accordion - P0 follow-up) | - |
| Duolingo | TBD (behind accordion - P0 follow-up) | - |

> **Note**: English proficiency requirements are behind expandable FAQ accordions on the international students page that could not be expanded during this capture. Marked as P0 follow-up.

### 3.3 研究生 -- 全局规则

UGA graduate admissions is **decentralized** -- each school/college manages its own admissions process. The Graduate School provides coordination but each program sets its own requirements.

---

## 4. 费用与经济援助 (Costs & Financial Aid)

### 4.1 本科费用 (2026-27 学年, 线性明细)

#### Georgia Resident (On Campus)
| 费用项目 | 金额 | 说明 |
|----------|------|------|
| Tuition | $10,134 | 学费 |
| Fees | $1,494 | 杂费 |
| Housing | $7,722 | 住宿 |
| Food | $4,718 | 餐饮 |
| Books & Supplies | $978 | 书本材料 |
| Transportation | $1,584 | 交通 |
| Miscellaneous | $3,290 | 其他 |
| **Total COA** | **$29,920** | On Campus |

#### Non-Resident (On Campus)
| 费用项目 | 金额 | 说明 |
|----------|------|------|
| Tuition | $31,804 | 学费 |
| Fees | $1,494 | 杂费 |
| Housing | $7,722 | 住宿 |
| Food | $4,718 | 餐饮 |
| Books & Supplies | $978 | 书本材料 |
| Transportation | $2,150 | 交通 |
| Miscellaneous | $3,290 | 其他 |
| **Total COA** | **$52,156** | On Campus |

### 4.2 本科经济援助政策

- Need-aware for all applicants (domestic and international)
- 80/20 in-state/OOS enrollment split (strategic enrollment management)
- Georgia residents eligible for HOPE Scholarship and Zell Miller Scholarship
- Fee waivers available for US citizens/permanent residents (Common App, College Board, ACT, NACAC)
- International students are NOT eligible for fee waivers

### 4.3 研究生费用 (2026-27 学年)

#### Georgia Resident Graduate (On Campus)
| 费用项目 | 金额 |
|----------|------|
| Tuition | $10,124 |
| Fees | $980 |
| **Total COA** | **$29,184** |

#### Non-Resident Graduate (On Campus)
| 费用项目 | 金额 |
|----------|------|
| Tuition | $31,148 |
| Fees | $980 |
| **Total COA** | **$36,594** |

---

## 5. 证据链索引 (Evidence Chain Index)

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: October 15
  source_url: https://admissions.uga.edu/apply/deadlines/
  source_snippet: "Application Deadline | Early Action: October 15"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-002:
  field: undergraduate.deadlines.RD
  value: January 1
  source_url: https://admissions.uga.edu/apply/deadlines/
  source_snippet: "Application Deadline | Regular Decision: January 1"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-003:
  field: undergraduate.test_policy
  value: SAT/ACT REQUIRED (NOT test-optional)
  source_url: https://admissions.uga.edu/apply/first-year-applicants/first-year-criteria/
  source_snippet: "All first-year and dual enrollment applicants are required to submit official test scores from either ACT or SAT. There is no test optional pathway to UGA."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.tuition_in_state
  value: $10,134
  source_url: https://osfa.uga.edu/costs/
  source_snippet: "Tuition | $10,134" (Georgia Resident: Undergraduate)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.tuition_oos
  value: $31,804
  source_url: https://osfa.uga.edu/costs/
  source_snippet: "Tuition | $31,804" (Non-resident: Undergraduate)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.total_coa_in_state
  value: $29,920
  source_url: https://osfa.uga.edu/costs/
  source_snippet: "COST OF ATTENDANCE | $29,920" (Georgia Resident On Campus)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_coa_oos
  value: $52,156
  source_url: https://osfa.uga.edu/costs/
  source_snippet: "COST OF ATTENDANCE | $52,156" (Non-resident On Campus)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.application.fee
  value: $70 (US), $85 (International)
  source_url: https://admissions.uga.edu/apply/start-application/application-fee-fee-waivers/
  source_snippet: "The First-Year application fee is $70 for US Citizens and $85 for International Students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.application.portal
  value: Common App (fall first-year); UGA Application (spring/transfers)
  source_url: https://admissions.uga.edu/apply/start-application/
  source_snippet: "Fall first-year applicants must apply exclusively through the Common Application"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.need_policy
  value: Need-aware for all applicants
  source_url: https://admissions.uga.edu/apply/first-year-applicants/
  source_snippet: "Our first-year enrollment goal is designed to maintain an 80/20 split, prioritizing talented students from across the state of Georgia, supplemented by a select group of high-achieving non-resident students."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: programs.total
  value: 859
  source_url: https://bulletin.uga.edu/Program/Index
  source_snippet: "863 results found"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## 6. WeKnora 导入清单

### Collection structure

```
uga-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: rules 1-4
├── 01-ug-education.md                  # Section 1: UG majors + minors
├── 02-grad-education.md                # Section 2: grad programs + certs
├── 03-requirements-deadlines.md        # Section 3
├── 04-costs-financial-aid.md           # Section 4
├── 05-evidence-chain.md                # Section 5
├── 06-import-manifest.md               # This section
└── 07-comparison-framework.md          # Section 7
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | English proficiency minimums (TOEFL/IELTS/DET) | https://admissions.uga.edu/apply/other-applicants/international-students/ |
| P0 | Graduate admissions details per school | Various school websites |
| P1 | SAT/ACT minimum score requirements | https://admissions.uga.edu/apply/first-year-applicants/first-year-criteria/ |
| P1 | Superscoring policy details | https://admissions.uga.edu/apply/first-year-applicants/first-year-criteria/ |
| P1 | Admissions statistics (middle 50% ranges) | https://admissions.uga.edu/apply/first-year-applicants/admissions-stats/ |
| P2 | Graduate cost per program | https://osfa.uga.edu/costs/ |

---

## 7. 跨校比较框架 (Cross-School Comparison Framework)

| 维度 | UGA |
|------|-----|
| 类型 | Public (SEC) |
| 地点 | Athens, GA |
| 本科学费 (In-state) | $10,134 |
| 本科学费 (OOS) | $31,804 |
| 总COA (In-state) | $29,920 |
| 总COA (OOS) | $52,156 |
| Need-blind? | Need-aware for ALL |
| Test policy | REQUIRED (SAT/ACT) |
| EA deadline | October 15 |
| RD deadline | January 1 |
| TOEFL minimum | TBD (P0) |
| IELTS minimum | TBD (P0) |
| App fee (US) | $70 |
| App fee (Intl) | $85 |
| Total programs (Rule 1) | 859 |
| Schools/colleges (Rule 2) | 20 |
| Conference | SEC |
| Strong areas | Public Health, Ecology, Agriculture, Veterinary Medicine |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.uga.edu, osfa.uga.edu, bulletin.uga.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program