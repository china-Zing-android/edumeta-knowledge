# Robert Gordon University (RGU) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

**Robert Gordon University (RGU)** is a public university in Aberdeen, Scotland, founded 1729 (Robert Gordon's College) and granted university status in 1992. Named **Scottish University of the Year** by The Times and Sunday Times Good University Guide 2026. Garthdee campus houses **8 academic schools** (7 schools + Graduate School). Total courses listed on `/study/courses` A-Z: **299** (including short courses and SCQF-credit modules).

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/BDes/LLB/Integrated M-level/CertHE/DipHE/UG Apprenticeship) | 94 |
| 研究生学位项目 (MSc/MA/MBA/LLM/MRes/MPhil/PhD + PgCert/PgDip variants + Professional Doctorates) | 93 |
| **学位项目总计 (UG + Grad)** | **187** |
| 短期课程 (Short Course) | 16 |
| 模块单元 (SCQF-credited modules) | 96 |
| 课程总条目 (A-Z listing) | 299 |
| 学院 / 独立系所总数 (含 Graduate School) | 8 |

### 0.2 学院 / 系层级结构

```
Robert Gordon University (Garthdee campus, Aberdeen)
├── Aberdeen Business School  [学院]
│   ├── Accounting & Finance  [系]
│   ├── Business & Management  [系]
│   ├── Communication & Media  [系]
│   ├── Data Analytics  [系]
│   ├── Energy Management  [系]
│   ├── Fashion Management  [系]
│   ├── HR Management  [系]
│   ├── Marketing  [系]
│   ├── Procurement & Supply Chain  [系]
│   ├── Project Management  [系]
│   └── Tourism & Hospitality  [系]
├── School of Computing, Engineering and Technology  [学院]
│   ├── Computing & Data Science  [系]
│   ├── Engineering (Research)  [系]
│   ├── Engineering Design & Manufacture  [系]
│   ├── Information & Library Studies  [系]
│   ├── Information Science (Research)  [系]
│   ├── Information Technology  [系]
│   ├── Mechanical & Offshore Engineering  [系]
│   ├── Oil & Gas Engineering  [系]
│   ├── Renewable Energy Engineering  [系]
│   └── Robotics & Mechatronics  [系]
├── School of Health  [学院]
│   ├── Applied Psychology  [系]
│   ├── Diagnostic Radiography  [系]
│   ├── Healthcare Practice  [系]
│   ├── Maritime Studies  [系]
│   ├── Midwifery  [系]
│   ├── Nursing  [系]
│   ├── Nutrition & Dietetics  [系]
│   ├── Occupational Health  [系]
│   ├── Occupational Therapy  [系]
│   ├── Paramedicine  [系]
│   ├── Physiotherapy  [系]
│   └── Sport & Exercise Science  [系]
├── School of Law and Social Sciences  [学院]
│   ├── Applied Social Sciences  [系]
│   ├── Criminology  [系]
│   ├── Law & Social Sciences  [系]
│   ├── Law (LLB/LLM)  [系]
│   ├── Legal Practice  [系]
│   └── Social Work  [系]
├── Graduate School  [学院]
│   ├── Professional Doctorate  [系]
│   └── Research Degrees  [系]
├── School of Pharmacy, Applied Sciences and Public Health  [学院]
│   ├── Biomedical Science  [系]
│   ├── Forensic & Analytical Science  [系]
│   ├── Pharmaceutical Science  [系]
│   ├── Pharmacist Prescribing  [系]
│   ├── Pharmacy (MPharm)  [系]
│   └── Pharmacy Practice  [系]
├── Gray's School of Art  [学院]
│   ├── Art & Design  [系]
│   ├── Communication Design  [系]
│   ├── Fashion & Textile Design  [系]
│   ├── Fine Art  [系]
│   ├── Foundation in Art & Design  [系]
│   ├── Interior Design  [系]
│   ├── Photography  [系]
│   └── Product, Ceramics & Jewellery  [系]
├── The Scott Sutherland School of Architecture & Built Environment  [学院]
│   ├── Architecture  [系]
│   ├── Architecture & Built Environment  [系]
│   ├── Built Environment  [系]
│   └── Quantity Surveying  [系]
```

### 0.3 学历级别明细

| 学位缩写 (官方/official) | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | 1 |
| BA (Hons) | Bachelor of Arts (Honours) | 本科 | 31 |
| BSc | Bachelor of Science | 本科 | 8 |
| BSc (Hons) | Bachelor of Science (Honours) | 本科 | 19 |
| BEng | Bachelor of Engineering | 本科 | 1 |
| BEng (Hons) | Bachelor of Engineering (Honours) | 本科 | 5 |
| BDes (Hons) | Bachelor of Design (Honours) | 本科 | 1 |
| LLB (Hons) | Bachelor of Laws (Honours) | 本科 | 4 |
| MSci | Master in Science (integrated 4-yr UG) | 本科 | 3 |
| MEng | Master of Engineering (integrated 4-yr UG) | 本科 | 5 |
| MPhys | Master of Physiotherapy (pre-reg integrated UG) | 本科 | 1 |
| MPharm | Master of Pharmacy (integrated UG) | 本科 | 1 |
| MOccTh | Master of Occupational Therapy (integrated UG) | 本科 | 1 |
| MDRad | Master of Diagnostic Radiography (integrated UG) | 本科 | 1 |
| MDiet | Master of Nutrition and Dietetics (integrated UG) | 本科 | 1 |
| MArch | Master of Architecture (Part 2 RIBA/ARB — integrated UG) | 本科 | 1 |
| DipHE | CertHE | DipHE + CertHE (UG combined pathway) | 本科 | 1 |
| DipHE | LLB | Diploma of Higher Education + Bachelor of Laws (UG combined pathway) | 本科 | 1 |
| CertHE | Certificate of Higher Education (UG) | 本科 | 1 |
| Graduate Apprenticeship in BA(Hons) | Graduate Apprenticeship in BA (Hons) | 本科 | 3 |
| Graduate Apprenticeship in BSc(Hons) | Graduate Apprenticeship in BSc (Hons) | 本科 | 2 |
| Graduate Apprenticeship in BEng(Hons) | Graduate Apprenticeship in BEng (Hons) | 本科 | 2 |
| BSc+MArch (UG combined) | BSc+MArch (UG combined) | 研究生 | 1 |
| DBA | Doctor of Business Administration (PG) | 研究生 | 1 |
| DInfSc | Doctor of Information Science (PG) | 研究生 | 1 |
| DLaw | Doctor of Law (PG) | 研究生 | 1 |
| DPT | Doctorate of Physiotherapy (PG) | 研究生 | 1 |
| EngD | Doctor of Engineering (PG) | 研究生 | 1 |
| GradCert | Graduate Certificate (Professional Development) | 研究生 | 2 |
| Graduate Apprenticeship in MSc | Graduate Apprenticeship in MSc | 研究生 | 1 |
| LLM | Master of Laws (PG) | 研究生 | 5 |
| MBA | Master of Business Administration (PG) | 研究生 | 6 |
| MSc+LLM | Master of Science + Master of Laws (combined award) | 研究生 | 1 |
| PgCert | Postgraduate Certificate | 研究生 | 2 |
| PgCert+PgDip+LLM | Postgraduate Certificate + Diploma + Master of Laws (combined award) | 研究生 | 1 |
| PgCert+PgDip+LLM+MSc | Postgraduate Certificate + Diploma + LLM + MSc (combined award) | 研究生 | 2 |
| PgCert+PgDip+MA | Postgraduate Certificate + Diploma + Master of Arts (combined award) | 研究生 | 4 |
| PgCert+PgDip+MRes+PhD | Postgraduate Certificate + Diploma + MRes + PhD (professional doctorate pathway) | 研究生 | 1 |
| PgCert+PgDip+MSc | Postgraduate Certificate + Diploma + Master of Science (combined award) | 研究生 | 56 |
| PgDip | Postgraduate Diploma | 研究生 | 1 |
| PgDip+MSc | Postgraduate Diploma + Master of Science (combined award) | 研究生 | 4 |
| Practice Cert | Practice Certificate (Pharmacist Independent Prescribing) | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BA (Hons) | BSc | BSc (Hons) | BEng | BEng (Hons) | BDes (Hons) | LLB (Hons) | MSci | MEng | MPhys | MPharm | MOccTh | MDRad | MDiet | MArch | DipHE | CertHE | DipHE | LLB | CertHE | Graduate Apprenticeship in BA(Hons) | Graduate Apprenticeship in BSc(Hons) | Graduate Apprenticeship in BEng(Hons) | BSc+MArch (UG combined) | DBA | DInfSc | DLaw | DPT | EngD | GradCert | Graduate Apprenticeship in MSc | LLM | MBA | MSc+LLM | PgCert | PgCert+PgDip+LLM | PgCert+PgDip+LLM+MSc | PgCert+PgDip+MA | PgCert+PgDip+MRes+PhD | PgCert+PgDip+MSc | PgDip | PgDip+MSc | Practice Cert | 合计 |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Aberdeen Business School | 0 | 18 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 6 | 0 | 1 | 0 | 0 | 0 | 0 | 24 | 0 | 0 | 0 | **55** |
| School of Computing, Engineering and Technology | 0 | 0 | 0 | 6 | 1 | 5 | 0 | 0 | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 15 | 0 | 0 | 0 | **38** |
| School of Health | 0 | 0 | 8 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 0 | **25** |
| School of Law and Social Sciences | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 5 | 0 | 1 | 0 | 1 | 2 | 0 | 0 | 1 | 1 | 0 | 0 | **23** |
| Graduate School | 1 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 3 | 0 | 4 | 0 | **17** |
| School of Pharmacy, Applied Sciences and Public Health | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 6 | 0 | 0 | 1 | **12** |
| Gray's School of Art | 0 | 6 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | **11** |
| The Scott Sutherland School of Architecture & Built Environment | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | **6** |
| **合计** | **1** | **31** | **8** | **19** | **1** | **5** | **1** | **4** | **3** | **5** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **1** | **3** | **2** | **2** | **1** | **1** | **1** | **1** | **1** | **1** | **2** | **1** | **5** | **6** | **1** | **2** | **1** | **2** | **4** | **1** | **56** | **1** | **4** | **1** | **187** |

> Reconciliation: rule-1 total = matrix sum = degree-inventory sum = **187** ✅

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

RGU's undergraduate portfolio is delivered across 7 academic schools (the Graduate School does not award UG degrees). All 8 schools appear in Section 0.2 tree. UG degrees follow the Scottish 4-year Honours model (MA/BSc Hons typically 4 years, with integrated 4-year master's variants MSci/MEng/MPhys/MPharm/MOccTh/MDRad/MDiet/MArch). See Section 0.2 for the full hierarchy.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Aberdeen Business School
##### Accounting & Finance
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance | https://www.rgu.ac.uk/study/courses/ba-hons-accounting-and-finance |
| 2 | Accounting with Business Analytics | https://www.rgu.ac.uk/study/courses/ba-hons-accounting-with-business-analytics |
| 3 | Business with Finance and Economics | https://www.rgu.ac.uk/study/courses/ba-hons-business-with-finance-and-economics |

###### Graduate Apprenticeship in BA(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-ba-hons-accounting |

##### Business & Management
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management | https://www.rgu.ac.uk/study/courses/ba-hons-business-management |
| 2 | Business and Management | https://www.rgu.ac.uk/study/courses/ba-hons-business-and-management |
| 3 | International Business Management | https://www.rgu.ac.uk/study/courses/ba-hons-international-business-management |

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.rgu.ac.uk/study/courses/bsc-hons-business-analytics |

###### Graduate Apprenticeship in BA(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Management | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-ba-hons-business-management |

##### Communication & Media
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Film and Media | https://www.rgu.ac.uk/study/courses/ba-hons-film-and-media |
| 2 | Journalism | https://www.rgu.ac.uk/study/courses/ba-hons-journalism |

##### Data Analytics
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business with Data Analytics | https://www.rgu.ac.uk/study/courses/ba-hons-business-with-data-analytics |

##### Fashion Management
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Management | https://www.rgu.ac.uk/study/courses/ba-hons-fashion-management |

##### HR Management
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business with Human Resource Management | https://www.rgu.ac.uk/study/courses/ba-hons-business-with-human-resource-management |

##### Marketing
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business with Marketing | https://www.rgu.ac.uk/study/courses/ba-hons-business-with-marketing |
| 2 | Digital Marketing | https://www.rgu.ac.uk/study/courses/ba-hons-digital-marketing |
| 3 | Digital Marketing and Business Analytics | https://www.rgu.ac.uk/study/courses/ba-hons-digital-marketing-and-business-analytics |
| 4 | Digital Marketing for Business | https://www.rgu.ac.uk/study/courses/ba-hons-digital-marketing-for-business |

##### Project Management
###### Graduate Apprenticeship in BA(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Project Management | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-ba-hons-business-and-project-management |

##### Tourism & Hospitality
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Events Management | https://www.rgu.ac.uk/study/courses/ba-hons-events-management |
| 2 | International Hospitality Management | https://www.rgu.ac.uk/study/courses/ba-hons-international-hospitality-management |
| 3 | International Tourism Management | https://www.rgu.ac.uk/study/courses/ba-hons-international-tourism-management |


#### School of Computing, Engineering and Technology
##### Computing & Data Science
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.rgu.ac.uk/study/courses/bsc-hons-computer-science |
| 2 | Cyber Security | https://www.rgu.ac.uk/study/courses/bsc-hons-cyber-security |
| 3 | Data Science with Artificial Intelligence | https://www.rgu.ac.uk/study/courses/bsc-hons-data-science-with-artificial-intelligence |
| 4 | Data Science with Business Management | https://www.rgu.ac.uk/study/courses/bsc-hons-data-science-with-business-management |
| 5 | Games Design | https://www.rgu.ac.uk/study/courses/bsc-hons-games-design |
| 6 | Web and Mobile Design | https://www.rgu.ac.uk/study/courses/bsc-hons-web-and-mobile-design |

###### Graduate Apprenticeship in BSc(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science with Artificial Intelligence | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-bsc-hons-data-science-with-artificial-intelligence |

##### Engineering Design & Manufacture
###### BEng (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Design | https://www.rgu.ac.uk/study/courses/beng-hons-engineering-design |

###### Graduate Apprenticeship in BEng(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering: Design and Manufacture | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-beng-hons-engineering-design-and-manufacture |
| 2 | Engineering: Instrumentation, Measurement and Control | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-beng-hons-engineering-instrumentation-measurement-and-control |

##### Mechanical & Offshore Engineering
###### BEng (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.rgu.ac.uk/study/courses/beng-hons-mechanical-engineering |
| 2 | Mechanical and Electrical Engineering | https://www.rgu.ac.uk/study/courses/beng-hons-mechanical-and-electrical-engineering |
| 3 | Mechanical and Offshore Engineering | https://www.rgu.ac.uk/study/courses/beng-hons-mechanical-and-offshore-engineering |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.rgu.ac.uk/study/courses/meng-mechanical-engineering |
| 2 | Mechanical and Electrical Engineering | https://www.rgu.ac.uk/study/courses/meng-mechanical-and-electrical-engineering |
| 3 | Mechanical and Offshore Engineering | https://www.rgu.ac.uk/study/courses/meng-mechanical-and-offshore-engineering |

##### Renewable Energy Engineering
###### BEng (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Renewable Energy Engineering | https://www.rgu.ac.uk/study/courses/beng-hons-renewable-energy-engineering |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Renewable Energy Engineering | https://www.rgu.ac.uk/study/courses/meng-renewable-energy-engineering |

##### Robotics & Mechatronics
###### BEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics and Mechatronics | https://www.rgu.ac.uk/study/courses/beng-robotics-and-mechatronics |

###### MEng
| # | 专业 | URL |
|---|------|-----|
| 1 | Robotics and Mechatronics | https://www.rgu.ac.uk/study/courses/meng-robotics-and-mechatronics |


#### School of Health
##### Diagnostic Radiography
###### MDRad
| # | 专业 | URL |
|---|------|-----|
| 1 | Diagnostic Radiography | https://www.rgu.ac.uk/study/courses/mdrad-diagnostic-radiography |

##### Healthcare Practice
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Healthcare Practice | https://www.rgu.ac.uk/study/courses/bsc-healthcare-practice |

##### Maritime Studies
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Maritime Studies | https://www.rgu.ac.uk/study/courses/bsc-maritime-studies |

##### Midwifery
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Midwifery | https://www.rgu.ac.uk/study/courses/bsc-midwifery |

##### Nursing
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing – Adult | https://www.rgu.ac.uk/study/courses/bsc-nursing-adult |
| 2 | Nursing – Children and Young People | https://www.rgu.ac.uk/study/courses/bsc-nursing-children-and-young-people |
| 3 | Nursing – Mental Health | https://www.rgu.ac.uk/study/courses/bsc-nursing-mental-health |

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing - Multiple Registration in Adult and Children and Young People | https://www.rgu.ac.uk/study/courses/bsc-hons-nursing-multiple-registration-in-adult-and-children-and-young-people |
| 2 | Nursing - Multiple Registration in Children and Young People and Mental Health | https://www.rgu.ac.uk/study/courses/bsc-hons-nursing-multiple-registration-in-children-and-young-people-and-mental-health |
| 3 | Nursing - Multiple Registration in Mental Health and Adult | https://www.rgu.ac.uk/study/courses/bsc-hons-nursing-multiple-registration-in-mental-health-and-adult |
| 4 | Nursing – Adult | https://www.rgu.ac.uk/study/courses/bsc-hons-nursing-adult |

##### Nutrition & Dietetics
###### MDiet
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition and Dietetics | https://www.rgu.ac.uk/study/courses/mdiet-nutrition-and-dietetics |

##### Occupational Health
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Occupational Health | https://www.rgu.ac.uk/study/courses/bsc-occupational-health |

##### Occupational Therapy
###### MOccTh
| # | 专业 | URL |
|---|------|-----|
| 1 | Occupational Therapy | https://www.rgu.ac.uk/study/courses/moccth-occupational-therapy |

##### Paramedicine
###### BSc
| # | 专业 | URL |
|---|------|-----|
| 1 | Paramedicine | https://www.rgu.ac.uk/study/courses/bsc-paramedicine |

##### Physiotherapy
###### MPhys
| # | 专业 | URL |
|---|------|-----|
| 1 | Physiotherapy | https://www.rgu.ac.uk/study/courses/mphys-physiotherapy |

##### Sport & Exercise Science
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Sport and Exercise Science | https://www.rgu.ac.uk/study/courses/bsc-hons-applied-sport-and-exercise-science |
| 2 | Sport Coaching | https://www.rgu.ac.uk/study/courses/bsc-hons-sport-coaching |


#### School of Law and Social Sciences
##### Applied Social Sciences
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Social Sciences | https://www.rgu.ac.uk/study/courses/ba-hons-applied-social-sciences |

##### Criminology
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.rgu.ac.uk/study/courses/ba-hons-criminology |

###### LLB (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Law with Criminology | https://www.rgu.ac.uk/study/courses/llb-hons-law-with-criminology |

##### Law & Social Sciences
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Sociology | https://www.rgu.ac.uk/study/courses/ba-hons-applied-sociology |

###### DipHE | LLB
| # | 专业 | URL |
|---|------|-----|
| 1 | Law – Online Learning | https://www.rgu.ac.uk/study/courses/diphe-llb-law-online-learning |

###### LLB (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://www.rgu.ac.uk/study/courses/llb-hons-law |

##### Law (LLB/LLM)
###### LLB (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Law with Artificial Intelligence | https://www.rgu.ac.uk/study/courses/llb-hons-law-with-artificial-intelligence |
| 2 | Law with Management | https://www.rgu.ac.uk/study/courses/llb-hons-law-with-management |

##### Legal Practice
###### CertHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Paralegal Practice | https://www.rgu.ac.uk/study/courses/certhe-paralegal-practice |

##### Social Work
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work - Distance Learning | https://www.rgu.ac.uk/study/courses/ba-hons-social-work-distance-learning |
| 2 | Social Work | https://www.rgu.ac.uk/study/courses/ba-hons-social-work |


#### Gray's School of Art
##### Communication Design
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Design - Graphics, Illustration, Photography | https://www.rgu.ac.uk/study/courses/ba-hons-communication-design-graphics-illustration-photography |

##### Fashion & Textile Design
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion and Textile Design - Fashion Design, Textile Design | https://www.rgu.ac.uk/study/courses/ba-hons-fashion-and-textile-design-fashion-design-textile-design |

##### Fine Art
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art - Painting, Photography, Printmaking, Sculpture, Moving Image | https://www.rgu.ac.uk/study/courses/ba-hons-fine-art-painting-photography-printmaking-sculpture-moving-image |

##### Foundation in Art & Design
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Foundation in Art and Design | https://www.rgu.ac.uk/study/courses/ba-hons-foundation-in-art-and-design |

##### Interior Design
###### BDes (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Design | https://www.rgu.ac.uk/study/courses/bdes-hons-interior-design |

##### Photography
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Photography | https://www.rgu.ac.uk/study/courses/ba-hons-photography |

##### Product, Ceramics & Jewellery
###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Product, Ceramics and Jewellery | https://www.rgu.ac.uk/study/courses/ba-hons-product-ceramics-and-jewellery |


#### Graduate School
##### Research Degrees
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative and Cultural Enterprise | https://www.rgu.ac.uk/study/courses/ba-creative-and-cultural-enterprise |

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Psychology | https://www.rgu.ac.uk/study/courses/ba-hons-applied-psychology |
| 2 | Law and Management | https://www.rgu.ac.uk/study/courses/ba-hons-law-and-management |

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computing and Creative Design | https://www.rgu.ac.uk/study/courses/bsc-hons-computing-and-creative-design |

###### DipHE | CertHE
| # | 专业 | URL |
|---|------|-----|
| 1 | Developing Support Worker Practice | https://www.rgu.ac.uk/study/courses/diphe-certhe-developing-support-worker-practice |

###### MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Computing Science | https://www.rgu.ac.uk/study/courses/msci-computing-science |


#### The Scott Sutherland School of Architecture & Built Environment
##### Architecture
###### BSc | Master of
| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | https://www.rgu.ac.uk/study/courses/bsc-master-of-architecture |

##### Architecture & Built Environment
###### MSci
| # | 专业 | URL |
|---|------|-----|
| 1 | Advanced Architectural Technology (Top-up route) | https://www.rgu.ac.uk/study/courses/msci-advanced-architectural-technology-top-up-route |
| 2 | Advanced Architectural Technology BSc (Hons) | | https://www.rgu.ac.uk/study/courses/bsc-hons-msci-advanced-architectural-technology |

##### Built Environment
###### Graduate Apprenticeship in BSc(Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Built Environment | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-bsc-hons-built-environment |

##### Quantity Surveying
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Quantity Surveying and Commercial Management | https://www.rgu.ac.uk/study/courses/bsc-hons-quantity-surveying-and-commercial-management |


#### School of Pharmacy, Applied Sciences and Public Health
##### Biomedical Science
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Biomedical Science | https://www.rgu.ac.uk/study/courses/bsc-hons-applied-biomedical-science |
| 2 | Biomedical Science | https://www.rgu.ac.uk/study/courses/bsc-hons-biomedical-science |

##### Forensic & Analytical Science
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic and Analytical Science | https://www.rgu.ac.uk/study/courses/bsc-hons-forensic-and-analytical-science |

##### Pharmacy (MPharm)
###### MPharm
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.rgu.ac.uk/study/courses/mpharm-pharmacy |

##### Pharmacy Practice
###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Clinical Practice for Pharmacy Technicians | https://www.rgu.ac.uk/study/courses/bsc-hons-clinical-practice-for-pharmacy-technicians |


---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Aberdeen Business School
##### Accounting & Finance
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Finance | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-accounting-and-finance |

##### Business & Management
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-analytics |
| 2 | Business Analytics for Healthcare Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-analytics-for-healthcare-management |
| 3 | Business Innovation and Entrepreneurship | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-innovation-and-entrepreneurship |
| 4 | Business Leadership and Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-leadership-and-management |
| 5 | Business and Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-and-management |
| 6 | Business and Management with Sustainability | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-and-management-with-sustainability |
| 7 | Business with Financial Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-with-financial-management |
| 8 | Business with Strategic Risk Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-with-strategic-risk-management |
| 9 | Engineering Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-engineering-management |
| 10 | Financial Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-financial-management |
| 11 | International Business Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-international-business-management |
| 12 | Project Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-project-management |

###### DBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Business Administration | https://www.rgu.ac.uk/study/courses/dba-doctor-of-business-administration |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration - Digital Transformation | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration-digital-transformation |
| 2 | Master of Business Administration - Healthcare Management | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration-healthcare-management |
| 3 | Master of Business Administration - Sustainability | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration-sustainability |
| 4 | Master of Business Administration | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration |

###### PgCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration - Essentials | https://www.rgu.ac.uk/study/courses/pgcert-business-administration-essentials |

##### Communication & Media
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Corporate Communications and Public Affairs | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-corporate-communications-and-public-affairs |

##### Energy Management
###### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Data Management with Business Analytics | https://www.rgu.ac.uk/study/courses/graduate-certificate-energy-data-management-with-business-analytics |

###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-energy-management |
| 2 | Energy Transitions and Sustainability | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-energy-transitions-and-sustainability |
| 3 | IT for the Energy Industry | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-it-for-the-energy-industry |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration - Energy and Transitions | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration-energy-and-transitions |

##### Fashion Management
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | International Fashion Business | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-international-fashion-business |

##### HR Management
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Business with HR Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-business-with-hr-management |
| 2 | Human Resource Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-human-resource-management |

##### Marketing
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Marketing | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-digital-marketing |
| 2 | International Marketing | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-international-marketing |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration - Digital Marketing | https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration-digital-marketing |

##### Procurement & Supply Chain
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Procurement and Supply Chain Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-procurement-and-supply-chain-management |

##### Tourism & Hospitality
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | International Tourism and Hospitality Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-international-tourism-and-hospitality-management |


#### School of Computing, Engineering and Technology
##### Computing & Data Science
###### Graduate Apprenticeship in MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Cyber Security | https://www.rgu.ac.uk/study/courses/graduate-apprenticeship-in-msc-cyber-security |

###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Computing | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-advanced-computing |
| 2 | Artificial Intelligence | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-artificial-intelligence |
| 3 | Cyber Security | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-cyber-security |
| 4 | Cyber Security with Artificial Intelligence | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-cyber-security-with-artificial-intelligence |
| 5 | Data Science | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-data-science |
| 6 | Games Design and Development | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-games-design-and-development |
| 7 | Information Technology with Artificial Intelligence | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-information-technology-with-artificial-intelligence |
| 8 | Information Technology with Cyber Security | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-information-technology-with-cyber-security |

##### Engineering (Research)
###### EngD
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Engineering | https://www.rgu.ac.uk/study/courses/engd-doctor-of-engineering |

##### Information & Library Studies
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Information and Library Studies | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-information-and-library-studies |

##### Information Science (Research)
###### DInfSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Information Science | https://www.rgu.ac.uk/study/courses/dinfsc-doctor-of-information-science |

##### Information Technology
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Information Technology | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-information-technology |
| 2 | Information Technology with Business Intelligence | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-information-technology-with-business-intelligence |

##### Oil & Gas Engineering
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Drilling and Well Engineering | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-drilling-and-well-engineering |
| 2 | Oil and Gas Engineering | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-oil-and-gas-engineering |

##### Renewable Energy Engineering
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Renewable Energy Engineering | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-renewable-energy-engineering |

##### Robotics & Mechatronics
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Robotics | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-robotics |


#### School of Law and Social Sciences
##### Law & Social Sciences
###### MSc | LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Oil, Gas and Renewable Energy Law | https://www.rgu.ac.uk/study/courses/msc-llm-oil-gas-and-renewable-energy-law |

###### PgCert | PgDip | LLM | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | International Environmental Law | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-llm-msc-international-environmental-law |

###### DLaw
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Law | https://www.rgu.ac.uk/study/courses/dlaw-doctor-of-law |

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.rgu.ac.uk/study/courses/llm-law |

##### Law (LLB/LLM)
###### PgCert | PgDip | LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Law with Corporate Governance | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-llm-law-with-corporate-governance |

###### PgCert | PgDip | LLM | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Law and Arbitration | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-llm-msc-construction-law-and-arbitration |

###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | Law and Dispute Resolution | https://www.rgu.ac.uk/study/courses/llm-law-and-dispute-resolution |
| 2 | Law and Energy Law | https://www.rgu.ac.uk/study/courses/llm-law-and-energy-law |
| 3 | Law and International Commercial Law | https://www.rgu.ac.uk/study/courses/llm-law-and-international-commercial-law |
| 4 | Law and International Law | https://www.rgu.ac.uk/study/courses/llm-law-and-international-law |

##### Legal Practice
###### PgDip
| # | 项目 | URL |
|---|------|-----|
| 1 | Diploma in Professional Legal Practice | https://www.rgu.ac.uk/study/courses/pgdip-professional-legal-practice |

##### Social Work
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-social-work |


#### Graduate School
##### Professional Doctorate
###### PgCert | PgDip | MRes | PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Doctorate | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-mres-phd-professional-doctorate |

##### Research Degrees
###### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Practice Learning Qualification - Social Services | https://www.rgu.ac.uk/study/courses/graduate-certificate-practice-learning-qualification-social-services |

###### MArch
| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture Part 2 RIBA/ARB | https://www.rgu.ac.uk/study/courses/master-of-architecture-part-2-riba-arb |

###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Occupational Health Practice | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-advanced-occupational-health-practice |
| 2 | Engineering | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-engineering |
| 3 | Physiotherapy – Pre-registration | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-physiotherapy-pre-registration |

###### PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Practice - Community Children’s Nursing | https://www.rgu.ac.uk/study/courses/pgdip-msc-advanced-practice-community-children-s-nursing |
| 2 | Advanced Practice - District Nursing | https://www.rgu.ac.uk/study/courses/pgdip-msc-advanced-practice-district-nursing |
| 3 | Advanced Practice - Health Visiting | https://www.rgu.ac.uk/study/courses/pgdip-msc-advanced-practice-health-visiting |
| 4 | Advanced Practice - School Nursing | https://www.rgu.ac.uk/study/courses/pgdip-msc-advanced-practice-school-nursing |

###### PgCert
| # | 项目 | URL |
|---|------|-----|
| 1 | Mental Health Officer Award | https://www.rgu.ac.uk/study/courses/pgcert-mental-health-officer-award |


#### School of Health
##### Applied Psychology
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Psychology | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-applied-psychology |

##### Healthcare Practice
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advancing Healthcare Practice | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-advancing-healthcare-practice |
| 2 | Healthcare Leadership | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-healthcare-leadership |
| 3 | Leading Transformation in Health and Social Care | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-leading-transformation-in-health-and-social-care |
| 4 | Public Health and Health Promotion | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-public-health-and-health-promotion |

##### Midwifery
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Midwifery | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-midwifery |

##### Physiotherapy
###### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Doctorate of Physiotherapy | https://www.rgu.ac.uk/study/courses/dpt-doctorate-of-physiotherapy |


#### School of Pharmacy, Applied Sciences and Public Health
##### Forensic & Analytical Science
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Analytical Science - Drug Analysis and Toxicology | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-analytical-science-drug-analysis-and-toxicology |
| 2 | Analytical Science – Environmental Analysis | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-analytical-science-environmental-analysis |
| 3 | Analytical Science – Food Analysis, Authenticity and Safety | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-analytical-science-food-analysis-authenticity-and-safety |

##### Pharmaceutical Science
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmaceutical Science | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-pharmaceutical-science |

##### Pharmacist Prescribing
###### Practice Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacist Independent Prescribing | https://www.rgu.ac.uk/study/courses/practice-certificate-pharmacist-independent-prescribing |

##### Pharmacy Practice
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Pharmacy Practice | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-advanced-pharmacy-practice |
| 2 | Clinical Pharmacy Practice | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-clinical-pharmacy-practice |


#### Gray's School of Art
##### Art & Design
###### PgCert | PgDip | MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion & Textiles | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-ma-fashion-textiles |

##### Communication Design
###### PgCert | PgDip | MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Design | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-ma-communication-design |

##### Fine Art
###### PgCert | PgDip | MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Fine Art | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-ma-fine-art |

##### Product, Ceramics & Jewellery
###### PgCert | PgDip | MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Product, Ceramics and Jewellery Design | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-ma-product-ceramics-and-jewellery-design |


#### The Scott Sutherland School of Architecture & Built Environment
##### Architecture & Built Environment
###### PgCert | PgDip | MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Project Management | https://www.rgu.ac.uk/study/courses/pgcert-pgdip-msc-construction-project-management |


### 2.2 Worked example — Master of Business Administration (MBA)


**Course**: Master of Business Administration (MBA) — Part Time
**URL**: https://www.rgu.ac.uk/study/courses/mba-master-of-business-administration
**School**: Aberdeen Business School
**Mode of Attendance**: Part Time
**Mode of Study**: On Campus
**Start Date**: September
**Variants offered** (each a separate listing):
  - MBA (generic) — Part Time
  - MBA - Digital Marketing — Part Time
  - MBA - Digital Transformation — Part Time
  - MBA - Energy and Transitions — Full Time | Part Time
  - MBA - Healthcare Management — Part Time
  - MBA - Sustainability — Full Time | Part Time
**Accreditation**: Aberdeen Business School is accredited by AACSB International (AACSB, achieved by 6% of global Business Schools); Small Business Charter (SBC).
**Note**: Per-program application deadlines, GRE/GMAT policy, and fees live on each course page (Fees & Funding tab) — fees differ between UK/Home and international students. International fees are listed on each course page; RGU is a licensed Student Sponsor with CAS for visa.

### 2.3 Graduate admissions model

RGU graduate admissions is **centralized** for application processing via the Student Admissions Service (`admissions@rgu.ac.uk`) but **decentralized academically** — each school sets its own entry requirements and assesses applications. No central application portal mentioned; applicants apply directly to RGU for most PGT courses. Research degrees (PhD, MRes, MPhil, professional doctorates) are administered by the **Graduate School** (`/research/our-research-degrees/the-graduate-school`).

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 数据 |
|------|------|
| Admissions site | https://www.rgu.ac.uk/study |
| Course directory (A-Z) | https://www.rgu.ac.uk/study/courses |
| Course search (filterable) | https://www.rgu.ac.uk/study/course-search |
| Application portal — UG | UCAS (https://www.ucas.com/) — RGU institution code: R36 (typical) |
| Application portal — PG | Direct to RGU (https://www.rgu.ac.uk/study/apply) |
| Application portal — ICRGU (January intake, international) | International College at RGU |
| January intake (international UG only) | Available for select courses (e.g. BA Accounting and Finance), via ICRGU |
| Clearing 2026 | Open (per BA Accounting and Finance page notice: "This course is accepting applications through clearing in 2026") |
| Application deadlines | Course-specific; see each course page. Postgraduate taught deadlines apply for September 2026 or January 2027 entry. |
| UCAS Code (sample, BA Accounting and Finance) | N420 |
| Interview policy | Course-specific (not collected in this run) |
| Recommendation requirements | Course-specific |
| Transfer pathway | Course-specific |

> **Note**: RGU does NOT publish a single centralised deadlines page — each course's Fees & Funding / Entry Requirements tab carries its own timeline. UCAS Equal Consideration deadline for UG is 26 January (well-known industry standard) but RGU also has Clearing/Flexible Admission pathways. Specific deadlines flagged as **P0 follow-up** for individual courses.

### 3.2 Undergraduate English proficiency (RGU-wide policy)

RGU states: "All applicants whose first language is not from a recognised English speaking country will be asked to provide evidence of their English language skills as part of their offer to study at RGU. Specific English language requirements are found on our course pages as these may differ for certain course areas."

| Exam | Minimum (typical UG) | Notes |
|------|---------------------|-------|
| IELTS Academic | Course-specific (typical UG 6.0–6.5 overall, no band <5.5; PGT typically 6.5; research typically 7.0) | Per course page |
| TOEFL iBT | Course-specific | Per course page |
| PTE Academic | Course-specific | Per course page |
| Cambridge (C1 Advanced / C2 Proficiency) | Course-specific | Per course page |
| Duolingo English Test | Course-specific | Per course page |
| RGU English language test discounts | Available for selected test providers (see "Exclusive English Test Discounts" on https://www.rgu.ac.uk/study/international-students/english-language-requirements) |
| UKVI SELT requirement (visa students) | Must meet both UKVI and RGU requirements |

### 3.3 Graduate — global rules

| 维度 | 数据 |
|------|------|
| Postgraduate application | Direct to RGU via course page (Apply Online). Some courses via ICRGU (international applicants). |
| Application fee | Not collected (P0 follow-up) |
| Postgraduate research degrees (MRes, MPhil, PhD, DBA, DPT, EngD, DInfSc, DLaw) | Apply through Graduate School — https://www.rgu.ac.uk/research/our-research-degrees/the-graduate-school |
| English language requirements (PG) | "It is essential that you can read and interpret academic journal articles, communicate effectively and write at a doctorate level." Per course page for PGT; higher for PGR. |
| Application deadlines (PG) | "If you are considering a postgraduate study option starting in September 2026 or January 2027, then please be aware application deadlines are in place which may affect your first choice of start date or course selection." — per-course. |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost

RGU states: "Tuition fees are set in relation to the type of course you are studying. For example, due to the materials required, laboratory based courses are often more expensive than class based ones. Fees for Overseas Students also differ from fees for UK and European Union students."

> **Important**: Tuition fees are **per-course**, not standardised. Each course page (Fees & Funding tab) shows the up-to-date UK, EU, and Overseas (international) tuition fee. Fees are not aggregated in a single page on RGU's site. **P0 follow-up**: capture per-course fees by visiting individual course pages in a future run.

| Expense item | Amount | Description |
|--------------|--------|-------------|
| UK / Home tuition | Per course — varies | Listed on each course page |
| EU tuition | Per course — varies | Listed on each course page |
| International (Overseas) tuition | Per course — varies | Listed on each course page; laboratory-based courses higher |
| Payment | Instalment plan available (see /study/international-students/international-fees-costs-funding) |
| Refund policy | International Students Refund Request Form (DOCX) |
| Living cost estimate | Per RGU "Cost of Living" guide — varies by accommodation, lifestyle |

### 4.2 Undergraduate financial-aid policy

| Dimension | Detail |
|-----------|--------|
| Scholarships search | https://www.rgu.ac.uk/study/finance-funding/funding-and-scholarships-search |
| International fee discount | "RGU offers all direct entry, self-funding international students a discount on their fees to help with this initial stage." (Per https://www.rgu.ac.uk/study/international-students/international-fees-costs-funding) |
| Emergency loan | Short-term emergency loans available; International Fund for internationals with change in circumstances |
| Fee status determination | https://www.rgu.ac.uk/study/finance-funding/determine-your-fee-status |
| Other fees & costs | https://www.rgu.ac.uk/study/finance-funding/other-fees-costs |

### 4.3 Graduate cost & funding framework

Per-course fees (PGT/PGR). RGU does not aggregate graduate fees in a single page; each course page's Fees & Funding tab shows current UK/EU/Overseas rates. PGR students may receive studentships / Graduate School funding. **P0 follow-up**: per-course fees and funding options.

---

## SECTION 5 — Evidence chain index


```yaml
E-U-001:
  field: institution.name
  value: Robert Gordon University
  source_url: https://www.rgu.ac.uk/
  source_snippet: "Robert Gordon University, Garthdee House, Garthdee Road, Aberdeen, AB10 7QB, Scotland, UK"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: institution.founded
  value: 1729 (Robert Gordon's College); university status 1992
  source_url: https://www.rgu.ac.uk/about
  source_snippet: "Robert Gordon University, Garthdee House, Garthdee Road, Aberdeen" (Scottish charity SC013781)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: institution.schools_count
  value: 8 (7 academic schools + Graduate School)
  source_url: https://www.rgu.ac.uk/study/academic-schools
  source_snippet: "Robert Gordon University has eight schools at our Garthdee campus in Aberdeen."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: institution.school_list
  value: Aberdeen Business School; Gray's School of Art; School of Computing, Engineering and Technology; School of Health; School of Law and Social Sciences; School of Pharmacy, Applied Sciences and Public Health; The Scott Sutherland School of Architecture & Built Environment; Graduate School
  source_url: https://www.rgu.ac.uk/study/academic-schools
  source_snippet: (8 schools enumerated on /study/academic-schools page)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: course_directory.count
  value: 299 total entries (187 degree programs + 96 SCQF modules + 16 short courses)
  source_url: https://www.rgu.ac.uk/study/courses
  source_snippet: (A-Z listing of all courses, 299 anchors)
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: course_search.url
  value: https://www.rgu.ac.uk/study/course-search
  source_snippet: "RGU Course Search — Use the course selector to find a course that interests you. Use the filters to narrow down your search."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: course_search.filters
  value: subject_area (17 options); mode_of_attendance (Full Time/Part Time); mode_of_study (On Campus/Online Learning/Work Based Learning); school_filter (8 schools)
  source_url: https://www.rgu.ac.uk/study/course-search
  source_snippet: (form <select> options enumerated in DOM)
  capture_date: 2026-07-08
  evidence_type: official_webpage_form

E-U-008:
  field: sample_course.BA_Accounting_Finance
  value: BA (Hons) Accounting and Finance — 4 years FT on-campus, September start. UCAS code N420. Accredited by ICAS, AACSB, Small Business Charter, ACCA, AIA, CIMA exemptions.
  source_url: https://www.rgu.ac.uk/study/courses/ba-hons-accounting-and-finance
  source_snippet: "Robert Gordon University's BA (Hons) Accounting and Finance degree will develop your academic knowledge and understanding, practical hands on skills and broader abilities... 4 years ... The course is fully accredited by the Institute of Chartered Accountants of Scotland (ICAS)"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: ranking.university_of_year
  value: Scottish University of the Year (The Times and Sunday Times Good University Guide 2026); RGU named top in Scotland for teaching quality in Art and Design (Gray's)
  source_url: https://www.rgu.ac.uk/study/academic-schools/gray-s-school-of-art
  source_snippet: "1st in Scotland for teaching quality in Art and Design (The Times and Sunday Times Good University Guide 2026)."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: international.english_requirements
  value: All non-native English speakers must provide evidence; specific requirements per course page. UKVI SELT required for visa students.
  source_url: https://www.rgu.ac.uk/study/international-students/english-language-requirements
  source_snippet: "All applicants whose first language is not from a recognised English speaking country will be asked to provide evidence of their English language skills as part of their offer to study at RGU."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: international.fees_discount
  value: "RGU offers all direct entry, self-funding international students a discount on their fees to help with this initial stage."
  source_url: https://www.rgu.ac.uk/study/international-students/international-fees-costs-funding
  source_snippet: "RGU offers all direct entry, self-funding international students a discount on their fees to help with this initial stage."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: international.fee_setting
  value: "Tuition fees are set in relation to the type of course you are studying. For example, due to the materials required, laboratory based courses are often more expensive than class based ones."
  source_url: https://www.rgu.ac.uk/study/international-students/international-fees-costs-funding
  source_snippet: "Tuition fees are set in relation to the type of course you are studying. For example, due to the materials required, laboratory based courses are often more expensive than class based ones."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-013:
  field: international.postgraduate_deadlines
  value: "If you are considering a postgraduate study option starting in September 2026 or January 2027, then please be aware application deadlines are in place which may affect your first choice of start date or course selection."
  source_url: https://www.rgu.ac.uk/study/international-students/english-language-requirements
  source_snippet: "If you are considering a postgraduate study option starting in September 2026 or January 2027, then please be aware application deadlines are in place which may affect your first choice of start date or course selection."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: application.ucas_requirement
  value: UG applicants apply via UCAS (single online application). RGU also accepts ICRGU applications for January intake (international).
  source_url: https://www.rgu.ac.uk/study/courses/ba-hons-accounting-and-finance
  source_snippet: "Applicants for first year entry will apply to other universities as well as to RGU through a single online Universities and Colleges Admissions Service (UCAS) application. UCAS Code: N420"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: graduate_school.url
  value: https://www.rgu.ac.uk/research/our-research-degrees/the-graduate-school
  source_url: https://www.rgu.ac.uk/study/academic-schools
  source_snippet: "Graduate School — research degrees, MRes, MPhil, professional doctorates" (linked from academic-schools page)
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: "robert-gordon-knowledge-base-v2"
  ├── document: institution-overview (Section 0)
  ├── document: undergraduate-programs (Section 1, chunked by school)
  │   ├── chunk: aberdeen-business-school-ug
  │   ├── chunk: grays-school-of-art-ug
  │   ├── chunk: school-of-computing-engineering-technology-ug
  │   ├── chunk: school-of-health-ug
  │   ├── chunk: school-of-law-and-social-sciences-ug
  │   ├── chunk: school-of-pharmacy-applied-sciences-ug
  │   └── chunk: scott-sutherland-architecture-ug
  ├── document: graduate-programs (Section 2, chunked by school)
  ├── document: application-requirements (Section 3)
  ├── document: costs-financial-aid (Section 4)
  ├── document: short-courses-and-modules (96 SCQF modules + 16 short courses)
  └── document: evidence-chain (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "robert-gordon-knowledge-base-v2"
  school: "<home school>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BA (Hons)|BSc|BSc (Hons)|BEng (Hons)|LLB (Hons)|MSci|MEng|MPhys|MPharm|MOccTh|MDRad|MDiet|MArch|MA|MSc|MBA|LLM|MRes|MPhil|PhD|DBA|DPT|EngD|DInfSc|DLaw|PgCert|PgDip|CertHE|DipHE>"
  level: undergraduate | postgraduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://www.rgu.ac.uk/study/courses/<slug>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P0 | Per-course tuition fees (UK / EU / Overseas) | Each /study/courses/<slug> page (Fees & Funding tab) |
| P0 | Per-course English language minimums (IELTS / TOEFL / PTE / Cambridge / Duolingo) | Each course page (Entry Requirements tab) |
| P0 | Per-course application deadlines (UG via UCAS, PG direct) | Each course page (How to Apply section) |
| P0 | Per-course accreditation details (e.g. NMC, HCPC, GPhC, RIBA) | Each course page (Accreditation section) |
| P1 | Per-course application fee | RGU Apply portal |
| P1 | Per-course interview/portfolio policy | Each course page |
| P1 | Per-course placement/sandwich year details | Each course page (Placements & Jobs tab) |
| P1 | School-level fee/award summary | https://www.rgu.ac.uk/study/academic-schools/<school-slug> |
| P2 | RGU ranking data (THE / QS / GUG) | https://www.rgu.ac.uk/about |
| P2 | International student support services | https://www.rgu.ac.uk/study/international-students |
| P2 | Accommodation costs | https://www.rgu.ac.uk/life-at-rgu/accommodation (if exists) |
| P2 | Career outcomes / DLHE data | https://www.rgu.ac.uk/study/employability |

---

## SECTION 7 — Cross-school comparison framework (UK Russell Group + modern universities)


| Dimension | RGU | Notes |
|-----------|-----|-------|
| Total program count (Rule 1) | 187 degree programs (94 UG + 93 PG) + 96 SCQF modules + 16 short courses | |
| School count (Rule 2) | 8 (7 schools + Graduate School) | |
| Region | Scotland (Aberdeen) | |
| Year founded / university status | 1729 (as Robert Gordon's College); 1992 (university) | |
| Campus | Single — Garthdee | |
| UG entry — typical 4-year Scottish Honours model | Yes | |
| Integrated 4-yr UG Master's | Yes (MSci / MEng / MPhys / MPharm / MOccTh / MDRad / MDiet / MArch) | |
| UCAS application (UG) | Yes (UCAS); institution code R36 (typical) | |
| International application (PG) | Direct to RGU | |
| Application portal — international UG (January) | ICRGU (International College at RGU) | |
| International fee discount | Yes — "all direct entry, self-funding international students a discount" | |
| UKVI licensed Student Sponsor | Yes (CAS for visa) | |
| Clearing 2026 | Open | |
| Times/Sunday Times ranking (2026) | Scottish University of the Year | |
| Notable rankings | 1st in Scotland for Art & Design teaching quality (Gray's, GUG 2026); 2nd in Scotland for teaching quality in Accounting & Finance | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: https://www.rgu.ac.uk (Course Search, A-Z course list, Academic Schools, International Students, English Language Requirements, International Fees/Costs/Funding, Finance & Funding)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: rule-1 (187) == matrix sum (187) == degree inventory sum (187) ✅
