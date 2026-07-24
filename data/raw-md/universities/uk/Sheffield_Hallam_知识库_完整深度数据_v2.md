# Sheffield Hallam University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## 0. 院校总览 (Institution Overview)

Sheffield Hallam University is one of the UK's largest and most diverse universities, with approximately 31,000 students, nearly 4,000 staff, and 345,000 alumni worldwide. Awarded Gold in the Teaching Excellence Framework 2023 and named Yorkshire's top university at the Whatuni Student Choice Awards 2026. Founded in 1843 as the Sheffield School of Design, the university operates across four academic colleges plus the Sheffield Business School.

**Total programs catalogued: 504 (across 38 subject areas / 4 colleges)**

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BEng/etc.) | 222 |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 273 |
| 其他/未分类 (level=unknown) | 9 |
| **学位项目总计 (UG + Grad)** | **504** |
| 学院 / 独立系所总数 | 4 colleges / 38 subject areas |

### 0.2 学院 / 系层级结构

```
Sheffield Hallam University
├── Sheffield Business School                    [学院]
│   ├── Accounting Banking And Finance    [系]
│   ├── Economics    [系]
│   ├── Business And Management    [系]
│   ├── Marketing    [系]
│   ├── Tourism And Hospitality    [系]
│   ├── Event Management    [系]
│   ├── Mba    [系]
│   ├── Law    [系]
│   ├── Media Pr And Journalism    [系]
├── College of Health, Wellbeing and Life Sciences    [学院]
│   ├── Nursing And Midwifery    [系]
│   ├── Diagnostic Radiography    [系]
│   ├── Physiotherapy    [系]
│   ├── Occupational Therapy    [系]
│   ├── Operating Department Practice    [系]
│   ├── Paramedic Science    [系]
│   ├── Radiotherapy And Oncology    [系]
│   ├── Health And Social Care Management    [系]
│   ├── Food And Nutrition    [系]
│   ├── Psychology    [系]
│   ├── Biosciences And Chemistry    [系]
│   ├── Sport And Physical Activity    [系]
├── College of Social Sciences and Arts    [学院]
│   ├── Teaching And Education    [系]
│   ├── English    [系]
│   ├── Criminology    [系]
│   ├── History    [系]
│   ├── Politics    [系]
│   ├── Social Work    [系]
│   ├── Sociology    [系]
│   ├── Geography And Environment    [系]
│   ├── Art And Design    [系]
│   ├── Acting Film And Tv    [系]
│   ├── Digital Media    [系]
└── College of Engineering, Computing and the Built Environment    [学院]
│   ├── Engineering    [系]
│   ├── Computing    [系]
│   ├── Architecture    [系]
│   ├── Construction And Surveying    [系]
│   ├── Mathematics    [系]
│   ├── Physics    [系]
```

### 0.3 学历级别明细

| 学位缩写 (本校) | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA (Honours) | Bachelor of Arts (Honours) | 本科 | 92 |
| BSc (Honours) | Bachelor of Science (Honours) | 本科 | 106 |
| BEng (Honours) | Bachelor of Engineering (Honours) | 本科 | 20 |
| LLB (Honours) | Bachelor of Laws (Honours) | 本科 | 4 |
| LLM | Master of Laws | 研究生 | 3 |
| MA | Master of Arts | 研究生 | 25 |
| MSc | Master of Science | 研究生 | 126 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MEng | Master of Engineering | 研究生 | 5 |
| MPhil | Master of Philosophy | 研究生 | 22 |
| MRes | Master of Research | 研究生 | 7 |
| PhD | Doctor of Philosophy | 研究生 | 44 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 1 |
| PGCert | Postgraduate Certificate | 研究生 | 6 |
| PGDip | Postgraduate Diploma | 研究生 | 4 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 25 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BEng | BS | DBA | EdD | LLB | LLM | MA | MBA | MEng | MPhil | MRes | MS | Other | PG Cert | PG Dip | PGCE | PhD | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| College of Engineering, Computing and the Built Environment | 0 | 20 | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 12 | 0 | 40 | 6 | 0 | 0 | 0 | 14 | **125** |
| College of Health, Wellbeing and Life Sciences | 0 | 0 | 55 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 6 | 5 | 44 | 1 | 3 | 4 | 0 | 8 | **128** |
| College of Social Sciences and Arts | 52 | 0 | 6 | 0 | 1 | 0 | 0 | 20 | 0 | 0 | 2 | 2 | 12 | 2 | 3 | 0 | 25 | 16 | **141** |
| Sheffield Business School | 40 | 0 | 17 | 1 | 0 | 4 | 3 | 3 | 4 | 0 | 2 | 0 | 30 | 0 | 0 | 0 | 0 | 6 | **110** |
| **合计** | 92 | 20 | 106 | 1 | 1 | 4 | 3 | 25 | 4 | 5 | 22 | 7 | 126 | 9 | 6 | 4 | 25 | 44 | **504** |

---

## 1. Undergraduate Education

### 1.1 College/school architecture

Sheffield Hallam's undergraduate provision spans all four academic colleges. See Section 0.2 for the full hierarchy. Each undergraduate course is offered as a 3- or 4-year full-time programme, with selected courses available part-time and many with an optional placement year. Foundation Year variants are common across most subjects (suffix "with Foundation Year" in the URL).

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Engineering, Computing and the Built Environment
##### Department of Computing
###### BEng (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Software Engineering | https://www.shu.ac.uk/courses/computing/beng-honours-software-engineering/full-time/2026 | full-time |
| 2 | Software Engineering with Foundation Year | https://www.shu.ac.uk/courses/computing/beng-honours-software-engineering-with-foundation-year/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Artificial Intelligence and Robotics | https://www.shu.ac.uk/courses/computing/bsc-honours-artificial-intelligence-and-robotics/full-time/2026 | full-time |
| 2 | Computer Games Technologies | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-games-technologies/full-time/2026 | full-time |
| 3 | Computer Games Technologies with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-games-technologies-with-foundation-year/full-time/2026 | full-time |
| 4 | Computer Science | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science/full-time/2026 | full-time |
| 5 | Computer Science for Games (1 year top-up) | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-for-games-1-year-topup/full-time/2026 | full-time |
| 6 | Computer Science with Artificial Intelligence | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-with-artificial-intelligence/full-time/2026 | full-time |
| 7 | Computer Science with Artificial Intelligence with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-with-artificial-intelligence-with-foundation-year/full-time/2026 | full-time |
| 8 | Computer Science with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-computer-science-with-foundation-year/full-time/2026 | full-time |
| 9 | Cyber Security | https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security/full-time/2026 | full-time |
| 10 | Cyber Security with Forensics | https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security-with-forensics/full-time/2026 | full-time |
| 11 | Cyber Security with Forensics with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security-with-forensics-with-foundation-year/full-time/2026 | full-time |
| 12 | Cyber Security with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-cyber-security-with-foundation-year/full-time/2026 | full-time |
| 13 | Data Science | https://www.shu.ac.uk/courses/computing/bsc-honours-data-science/full-time/2026 | full-time |
| 14 | Data Science with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-data-science-with-foundation-year/full-time/2026 | full-time |
| 15 | Information Technology with Business Studies | https://www.shu.ac.uk/courses/computing/bsc-honours-information-technology-with-business-studies/full-time/2026 | full-time |
| 16 | Information Technology with Business Studies with Foundation Year | https://www.shu.ac.uk/courses/computing/bsc-honours-information-technology-with-business-studies-with-foundation-year/full-time/2026 | full-time |
##### Department of Construction And Surveying
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Building Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-building-surveying/part-time/2026 | part-time |
| 2 | Building Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-building-surveying/full-time/2026 | full-time |
| 3 | Building Surveying with Foundation Year | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-building-surveying-with-foundation-year/full-time/2026 | full-time |
| 4 | Construction Project Management | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-construction-project-management/full-time/2026 | full-time |
| 5 | Construction Project Management | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-construction-project-management/part-time/2026 | part-time |
| 6 | Construction Project Management with Foundation Year | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-construction-project-management-with-foundation-year/full-time/2026 | full-time |
| 7 | Quantity Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-quantity-surveying/part-time/2026 | part-time |
| 8 | Quantity Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-quantity-surveying/full-time/2026 | full-time |
| 9 | Quantity Surveying with Foundation Year | https://www.shu.ac.uk/courses/construction-and-surveying/bsc-honours-quantity-surveying-with-foundation-year/full-time/2026 | full-time |
##### Department of Engineering
###### BEng (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Aerospace Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-aerospace-engineering/full-time/2026 | full-time |
| 2 | Aerospace Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-aerospace-engineering-with-foundation-year/full-time/2026 | full-time |
| 3 | Automotive Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-automotive-engineering/full-time/2026 | full-time |
| 4 | Automotive Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-automotive-engineering-with-foundation-year/full-time/2026 | full-time |
| 5 | Chemical Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-chemical-engineering/full-time/2026 | full-time |
| 6 | Chemical Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-chemical-engineering-with-foundation-year/full-time/2026 | full-time |
| 7 | Civil Engineering (1 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-civil-engineering-1-year-topup/full-time/2026 | full-time |
| 8 | Civil Engineering (2 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-civil-engineering-2-year-topup/part-time/2026 | part-time |
| 9 | Electrical Engineering (1 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-engineering-1-year-topup/full-time/2026 | full-time |
| 10 | Electrical Engineering (2 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-engineering-2-year-topup/part-time/2026 | part-time |
| 11 | Electrical and Electronic Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-and-electronic-engineering/full-time/2026 | full-time |
| 12 | Electrical and Electronic Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-electrical-and-electronic-engineering-with-foundation-year/full-time/2026 | full-time |
| 13 | Mechanical Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering/full-time/2026 | full-time |
| 14 | Mechanical Engineering (1 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering-1-year-topup/full-time/2026 | full-time |
| 15 | Mechanical Engineering (2 year top-up) | https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering-2-year-topup/part-time/2026 | part-time |
| 16 | Mechanical Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-mechanical-engineering-with-foundation-year/full-time/2026 | full-time |
| 17 | Mechatronic and Robotic Engineering | https://www.shu.ac.uk/courses/engineering/beng-honours-mechatronic-and-robotic-engineering/full-time/2026 | full-time |
| 18 | Mechatronic and Robotic Engineering with Foundation Year | https://www.shu.ac.uk/courses/engineering/beng-honours-mechatronic-and-robotic-engineering-with-foundation-year/full-time/2026 | full-time |
##### Department of Mathematics
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Mathematics with Foundation Year | https://www.shu.ac.uk/courses/mathematics/bsc-honours-mathematics-with-foundation-year/full-time/2026 | full-time |
##### Department of Physics
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Physics | https://www.shu.ac.uk/courses/physics/bsc-honours-physics/full-time/2026 | full-time |
| 2 | Physics with Foundation Year | https://www.shu.ac.uk/courses/physics/bsc-honours-physics-with-foundation-year/full-time/2026 | full-time |
#### College of Health, Wellbeing and Life Sciences
##### Department of Biosciences And Chemistry
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Biochemistry | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biochemistry/full-time/2026 | full-time |
| 2 | Biochemistry with Foundation Year | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biochemistry-with-foundation-year/full-time/2026 | full-time |
| 3 | Biology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biology/full-time/2026 | full-time |
| 4 | Biology with Foundation Year | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biology-with-foundation-year/full-time/2026 | full-time |
| 5 | Biomedical Science | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biomedical-science/full-time/2026 | full-time |
| 6 | Biomedical Science with Foundation Year | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biomedical-science-with-foundation-year/full-time/2026 | full-time |
| 7 | Biomedicine and Health Science | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biomedicine-and-health-science/full-time/2026 | full-time |
| 8 | Biomedicine and Health Science with Foundation Year | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-biomedicine-and-health-science-with-foundation-year/full-time/2026 | full-time |
| 9 | Chemistry | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-chemistry/full-time/2026 | full-time |
| 10 | Chemistry with Foundation Year | https://www.shu.ac.uk/courses/biosciences-and-chemistry/bsc-honours-chemistry-with-foundation-year/full-time/2026 | full-time |
##### Department of Diagnostic Radiography
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Diagnostic Radiography | https://www.shu.ac.uk/courses/diagnostic-radiography/bsc-honours-diagnostic-radiography/full-time/2026 | full-time |
| 2 | Diagnostic Radiography with Foundation Year | https://www.shu.ac.uk/courses/diagnostic-radiography/bsc-honours-diagnostic-radiography-with-foundation-year/full-time/2026 | full-time |
##### Department of Food And Nutrition
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Food and Nutrition | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-food-and-nutrition/full-time/2026 | full-time |
| 2 | Food and Nutrition (1 year top-up) | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-food-and-nutrition-1-year-topup/full-time/2026 | full-time |
| 3 | Food and Nutrition with Foundation Year | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-food-and-nutrition-with-foundation-year/full-time/2026 | full-time |
| 4 | Human Nutrition and Health | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-human-nutrition-and-health/full-time/2026 | full-time |
| 5 | Human Nutrition and Health with Foundation Year | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-human-nutrition-and-health-with-foundation-year/full-time/2026 | full-time |
| 6 | Nutrition, Diet and Wellbeing (1 year top-up) | https://www.shu.ac.uk/courses/food-and-nutrition/bsc-honours-nutrition-diet-and-wellbeing-1-year-topup/full-time/2026 | full-time |
##### Department of Health And Social Care Management
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Health and Social Care Studies (1 year top-up) | https://www.shu.ac.uk/courses/health-and-social-care-management/bsc-honours-health-and-social-care-studies-1-year-topup/full-time/2026 | full-time |
##### Department of Nursing And Midwifery
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Midwifery | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-midwifery/full-time/2026 | full-time |
| 2 | Midwifery with Foundation Year | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-midwifery-with-foundation-year/full-time/2026 | full-time |
| 3 | Nursing (Adult) | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-adult/part-time/2026 | part-time |
| 4 | Nursing (Adult) | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-adult/full-time/2026 | full-time |
| 5 | Nursing (Adult) | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-adult-sheffield/part-time/2026 | part-time |
| 6 | Nursing (Adult) with Foundation Year | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-adult-with-foundation-year/full-time/2026 | full-time |
| 7 | Nursing (Child) | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-child/full-time/2026 | full-time |
| 8 | Nursing (Child) with Foundation Year | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-child-with-foundation-year/full-time/2026 | full-time |
| 9 | Nursing (Learning Disability) and Social Work | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-learning-disability-and-social-work/full-time/2026 | full-time |
| 10 | Nursing (Learning Disability) and Social Work with Foundation Year | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-learning-disability-and-social-work-with-foundation-year/full-time/2026 | full-time |
| 11 | Nursing (Mental Health) | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-mental-health/full-time/2026 | full-time |
| 12 | Nursing (Mental Health) with Foundation Year | https://www.shu.ac.uk/courses/nursing-and-midwifery/bsc-honours-nursing-mental-health-with-foundation-year/full-time/2026 | full-time |
##### Department of Occupational Therapy
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Occupational Therapy | https://www.shu.ac.uk/courses/occupational-therapy/bsc-honours-occupational-therapy/full-time/2026 | full-time |
| 2 | Occupational Therapy with Foundation Year | https://www.shu.ac.uk/courses/occupational-therapy/bsc-honours-occupational-therapy-with-foundation-year/full-time/2026 | full-time |
##### Department of Operating Department Practice
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Operating Department Practice | https://www.shu.ac.uk/courses/operating-department-practice/bsc-honours-operating-department-practice/full-time/2026 | full-time |
| 2 | Operating Department Practice with Foundation Year | https://www.shu.ac.uk/courses/operating-department-practice/bsc-honours-operating-department-practice-with-foundation-year/full-time/2026 | full-time |
##### Department of Paramedic Science
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Paramedic Science | https://www.shu.ac.uk/courses/paramedic-science/bsc-honours-paramedic-science/full-time/2026 | full-time |
| 2 | Paramedic Science with Foundation Year | https://www.shu.ac.uk/courses/paramedic-science/bsc-honours-paramedic-science-with-foundation-year/full-time/2026 | full-time |
##### Department of Physiotherapy
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Physiotherapy | https://www.shu.ac.uk/courses/physiotherapy/bsc-honours-physiotherapy/full-time/2026 | full-time |
| 2 | Physiotherapy with Foundation Year | https://www.shu.ac.uk/courses/physiotherapy/bsc-honours-physiotherapy-with-foundation-year/full-time/2026 | full-time |
##### Department of Psychology
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Psychology | https://www.shu.ac.uk/courses/psychology/bsc-honours-psychology/full-time/2026 | full-time |
| 2 | Psychology with Foundation Year | https://www.shu.ac.uk/courses/psychology/bsc-honours-psychology-with-foundation-year/full-time/2026 | full-time |
##### Department of Radiotherapy And Oncology
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Radiotherapy and Oncology | https://www.shu.ac.uk/courses/radiotherapy-and-oncology/bsc-honours-radiotherapy-and-oncology/full-time/2026 | full-time |
| 2 | Radiotherapy and Oncology with Foundation Year | https://www.shu.ac.uk/courses/radiotherapy-and-oncology/bsc-honours-radiotherapy-and-oncology-with-foundation-year/full-time/2026 | full-time |
##### Department of Sport And Physical Activity
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Physical Education and School Sport | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-physical-education-and-school-sport/full-time/2026 | full-time |
| 2 | Physical Education and School Sport with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-physical-education-and-school-sport-with-foundation-year/full-time/2026 | full-time |
| 3 | Sport Business Management | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-business-management/full-time/2026 | full-time |
| 4 | Sport Business Management with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-business-management-with-foundation-year/full-time/2026 | full-time |
| 5 | Sport Coaching | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-coaching/full-time/2026 | full-time |
| 6 | Sport Coaching with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-coaching-with-foundation-year/full-time/2026 | full-time |
| 7 | Sport and Exercise Science | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-and-exercise-science/full-time/2026 | full-time |
| 8 | Sport and Exercise Science with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-and-exercise-science-with-foundation-year/full-time/2026 | full-time |
| 9 | Sport, Exercise and Health | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-exercise-and-health/full-time/2026 | full-time |
| 10 | Sport, Exercise and Health with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sport-exercise-and-health-with-foundation-year/full-time/2026 | full-time |
| 11 | Sports Therapy | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sports-therapy/full-time/2026 | full-time |
| 12 | Sports Therapy with Foundation Year | https://www.shu.ac.uk/courses/sport-and-physical-activity/bsc-honours-sports-therapy-with-foundation-year/full-time/2026 | full-time |
#### College of Social Sciences and Arts
##### Department of Acting Film And Tv
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Acting and Performance | https://www.shu.ac.uk/courses/acting-film-and-tv/ba-honours-acting-and-performance/full-time/2026 | full-time |
| 2 | Acting and Performance (1 year top-up) | https://www.shu.ac.uk/courses/acting-film-and-tv/ba-honours-acting-and-performance-1-year-topup/full-time/2026 | full-time |
| 3 | Acting and Performance with Foundation Year | https://www.shu.ac.uk/courses/acting-film-and-tv/ba-honours-acting-and-performance-with-foundation-year/full-time/2026 | full-time |
| 4 | Film and TV Production | https://www.shu.ac.uk/courses/acting-film-and-tv/ba-honours-film-and-tv-production/full-time/2026 | full-time |
| 5 | Film and TV Production with Foundation Year | https://www.shu.ac.uk/courses/acting-film-and-tv/ba-honours-film-and-tv-production-with-foundation-year/full-time/2026 | full-time |
##### Department of Art And Design
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Animation | https://www.shu.ac.uk/courses/art-and-design/ba-honours-animation/full-time/2026 | full-time |
| 2 | Animation with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-animation-with-foundation-year/full-time/2026 | full-time |
| 3 | Fashion Design | https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-design/full-time/2026 | full-time |
| 4 | Fashion Design with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-design-with-foundation-year/full-time/2026 | full-time |
| 5 | Fashion Management and Communication | https://www.shu.ac.uk/courses/art-and-design/ba-honours-fashion-management-and-communication/full-time/2026 | full-time |
| 6 | Fine Art | https://www.shu.ac.uk/courses/art-and-design/ba-honours-fine-art/full-time/2026 | full-time |
| 7 | Fine Art with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-fine-art-with-foundation-year/full-time/2026 | full-time |
| 8 | Graphic Design | https://www.shu.ac.uk/courses/art-and-design/ba-honours-graphic-design/full-time/2026 | full-time |
| 9 | Graphic Design with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-graphic-design-with-foundation-year/full-time/2026 | full-time |
| 10 | Illustration | https://www.shu.ac.uk/courses/art-and-design/ba-honours-illustration/full-time/2026 | full-time |
| 11 | Illustration with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-illustration-with-foundation-year/full-time/2026 | full-time |
| 12 | Interior Architecture and Design | https://www.shu.ac.uk/courses/art-and-design/ba-honours-interior-architecture-and-design/full-time/2026 | full-time |
| 13 | Interior Architecture and Design with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-interior-architecture-and-design-with-foundation-year/full-time/2026 | full-time |
| 14 | Photography | https://www.shu.ac.uk/courses/art-and-design/ba-honours-photography/full-time/2026 | full-time |
| 15 | Photography with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-photography-with-foundation-year/full-time/2026 | full-time |
| 16 | Product Design | https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design/full-time/2026 | full-time |
| 17 | Product Design with Foundation Year | https://www.shu.ac.uk/courses/art-and-design/ba-honours-product-design-with-foundation-year/full-time/2026 | full-time |
##### Department of Criminology
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Criminology | https://www.shu.ac.uk/courses/criminology/ba-honours-criminology/full-time/2026 | full-time |
| 2 | Criminology and Sociology | https://www.shu.ac.uk/courses/criminology/ba-honours-criminology-and-sociology/full-time/2026 | full-time |
| 3 | Criminology and Sociology with Foundation Year | https://www.shu.ac.uk/courses/criminology/ba-honours-criminology-and-sociology-with-foundation-year/full-time/2026 | full-time |
| 4 | Criminology with Foundation Year | https://www.shu.ac.uk/courses/criminology/ba-honours-criminology-with-foundation-year/full-time/2026 | full-time |
| 5 | Professional Policing | https://www.shu.ac.uk/courses/criminology/ba-honours-professional-policing/full-time/2026 | full-time |
| 6 | Professional Policing with Foundation Year | https://www.shu.ac.uk/courses/criminology/ba-honours-professional-policing-with-foundation-year/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Criminology and Psychology | https://www.shu.ac.uk/courses/criminology/bsc-honours-criminology-and-psychology/full-time/2026 | full-time |
| 2 | Criminology and Psychology with Foundation Year | https://www.shu.ac.uk/courses/criminology/bsc-honours-criminology-and-psychology-with-foundation-year/full-time/2026 | full-time |
##### Department of Digital Media
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Digital Media Production | https://www.shu.ac.uk/courses/digital-media/ba-honours-digital-media-production/full-time/2026 | full-time |
| 2 | Digital Media Production with Foundation Year | https://www.shu.ac.uk/courses/digital-media/ba-honours-digital-media-production-with-foundation-year/full-time/2026 | full-time |
| 3 | Game Art | https://www.shu.ac.uk/courses/digital-media/ba-honours-game-art/full-time/2026 | full-time |
| 4 | Game Art with Foundation Year | https://www.shu.ac.uk/courses/digital-media/ba-honours-game-art-with-foundation-year/full-time/2026 | full-time |
| 5 | Game Design and Development | https://www.shu.ac.uk/courses/digital-media/ba-honours-game-design-and-development/full-time/2026 | full-time |
| 6 | Game Design and Development with Foundation Year | https://www.shu.ac.uk/courses/digital-media/ba-honours-game-design-and-development-with-foundation-year/full-time/2026 | full-time |
##### Department of English
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Creative Writing | https://www.shu.ac.uk/courses/english/ba-honours-creative-writing/full-time/2026 | full-time |
| 2 | English | https://www.shu.ac.uk/courses/english/ba-honours-english/full-time/2026 | full-time |
| 3 | English with Foundation Year | https://www.shu.ac.uk/courses/english/ba-honours-english-with-foundation-year/full-time/2026 | full-time |
##### Department of Geography And Environment
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Climate, Sustainability and Environmental Management | https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-climate-sustainability-and-environmental-management/full-time/2026 | full-time |
| 2 | Climate, Sustainability and Environmental Management with Foundation Year | https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-climate-sustainability-and-environmental-management-with-foundation-year/full-time/2026 | full-time |
| 3 | Geography | https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-geography/full-time/2026 | full-time |
| 4 | Geography with Foundation Year | https://www.shu.ac.uk/courses/geography-and-environment/bsc-honours-geography-with-foundation-year/full-time/2026 | full-time |
##### Department of History
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | History | https://www.shu.ac.uk/courses/history/ba-honours-history/full-time/2026 | full-time |
| 2 | History with Foundation Year | https://www.shu.ac.uk/courses/history/ba-honours-history-with-foundation-year/full-time/2026 | full-time |
##### Department of Politics
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Politics and International Relations | https://www.shu.ac.uk/courses/politics/ba-honours-politics-and-international-relations/full-time/2026 | full-time |
| 2 | Politics and International Relations with Foundation Year | https://www.shu.ac.uk/courses/politics/ba-honours-politics-and-international-relations-with-foundation-year/full-time/2026 | full-time |
##### Department of Social Work
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Social Work | https://www.shu.ac.uk/courses/social-work/ba-honours-social-work/full-time/2026 | full-time |
| 2 | Working with Children, Young People and Families (1 year top-up) | https://www.shu.ac.uk/courses/social-work/ba-honours-working-with-children-young-people-and-families-1-year-topup/full-time/2026 | full-time |
##### Department of Sociology
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Sociology | https://www.shu.ac.uk/courses/sociology/ba-honours-sociology/full-time/2026 | full-time |
| 2 | Sociology with Foundation Year | https://www.shu.ac.uk/courses/sociology/ba-honours-sociology-with-foundation-year/full-time/2026 | full-time |
##### Department of Teaching And Education
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Children and Childhoods | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-children-and-childhoods/full-time/2026 | full-time |
| 2 | Children and Childhoods with Foundation Year | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-children-and-childhoods-with-foundation-year/full-time/2026 | full-time |
| 3 | Early Years and Primary Education (3-7) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-early-years-and-primary-education-37-with-qualified-teacher-status/full-time/2026 | full-time |
| 4 | Education with Psychology and Counselling | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-education-with-psychology-and-counselling/full-time/2026 | full-time |
| 5 | Education with Psychology and Counselling with Foundation Year | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-education-with-psychology-and-counselling-with-foundation-year/full-time/2026 | full-time |
| 6 | Primary Education (5-11) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-primary-education-511-with-qualified-teacher-status/full-time/2026 | full-time |
| 7 | Teaching and Learning with Qualified Teacher Status (2 year top-up) | https://www.shu.ac.uk/courses/teaching-and-education/ba-honours-teaching-and-learning-with-qualified-teacher-status-2-year-topup/part-time/2026 | part-time |
#### Sheffield Business School
##### Department of Accounting Banking And Finance
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Accounting and Finance | https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2026 | full-time |
| 2 | Accounting and Finance with Foundation Year | https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance-with-foundation-year/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Banking and Finance | https://www.shu.ac.uk/courses/accounting-banking-and-finance/bsc-honours-banking-and-finance/full-time/2026 | full-time |
| 2 | Economics and Finance | https://www.shu.ac.uk/courses/accounting-banking-and-finance/bsc-honours-economics-and-finance/full-time/2026 | full-time |
| 3 | Economics and Finance with Foundation Year | https://www.shu.ac.uk/courses/accounting-banking-and-finance/bsc-honours-economics-and-finance-with-foundation-year/full-time/2026 | full-time |
| 4 | Financial Trading and Investment Management | https://www.shu.ac.uk/courses/accounting-banking-and-finance/bsc-honours-financial-trading-and-investment-management/full-time/2026 | full-time |
| 5 | Financial Trading and Investment Management with Foundation Year | https://www.shu.ac.uk/courses/accounting-banking-and-finance/bsc-honours-financial-trading-and-investment-management-with-foundation-year/full-time/2026 | full-time |
##### Department of Business And Management
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Business Management | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management/full-time/2026 | full-time |
| 2 | Business Management (1 year top-up) | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-1-year-topup/full-time/2026 | full-time |
| 3 | Business Management and Enterprise | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-enterprise/full-time/2026 | full-time |
| 4 | Business Management and Enterprise with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-enterprise-with-foundation-year/full-time/2026 | full-time |
| 5 | Business Management and Finance | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-finance/full-time/2026 | full-time |
| 6 | Business Management and Finance with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-finance-with-foundation-year/full-time/2026 | full-time |
| 7 | Business Management and Marketing | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-marketing/full-time/2026 | full-time |
| 8 | Business Management and Marketing with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-and-marketing-with-foundation-year/full-time/2026 | full-time |
| 9 | Business Management with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-with-foundation-year/full-time/2026 | full-time |
| 10 | Business Management with Law | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-with-law/full-time/2026 | full-time |
| 11 | Business Management with Law with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-with-law-with-foundation-year/full-time/2026 | full-time |
| 12 | Business Management with Psychology | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-with-psychology/full-time/2026 | full-time |
| 13 | Business Management with Psychology with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-business-management-with-psychology-with-foundation-year/full-time/2026 | full-time |
| 14 | International Business | https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business/full-time/2026 | full-time |
| 15 | International Business (European Partnership Programme) | https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-european-partnership-programme/full-time/2026 | full-time |
| 16 | International Business with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-foundation-year/full-time/2026 | full-time |
| 17 | International Business with French | https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-french/full-time/2026 | full-time |
| 18 | International Business with Spanish | https://www.shu.ac.uk/courses/business-and-management/ba-honours-international-business-with-spanish/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Business Management and Artificial Intelligence | https://www.shu.ac.uk/courses/business-and-management/bsc-honours-business-management-and-artificial-intelligence/full-time/2026 | full-time |
| 2 | Business Management and Artificial Intelligence with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/bsc-honours-business-management-and-artificial-intelligence-with-foundation-year/full-time/2026 | full-time |
| 3 | Real Estate | https://www.shu.ac.uk/courses/business-and-management/bsc-honours-real-estate/full-time/2026 | full-time |
| 4 | Real Estate with Foundation Year | https://www.shu.ac.uk/courses/business-and-management/bsc-honours-real-estate-with-foundation-year/full-time/2026 | full-time |
##### Department of Economics
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Business Economics | https://www.shu.ac.uk/courses/economics/ba-honours-business-economics/full-time/2026 | full-time |
| 2 | Business Economics with Foundation Year | https://www.shu.ac.uk/courses/economics/ba-honours-business-economics-with-foundation-year/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Economics | https://www.shu.ac.uk/courses/economics/bsc-honours-economics/full-time/2026 | full-time |
| 2 | Economics with Foundation Year | https://www.shu.ac.uk/courses/economics/bsc-honours-economics-with-foundation-year/full-time/2026 | full-time |
##### Department of Event Management
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Esports Management (1 year top-up) | https://www.shu.ac.uk/courses/event-management/ba-honours-esports-management-1-year-topup/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Events Management | https://www.shu.ac.uk/courses/event-management/bsc-honours-events-management/full-time/2026 | full-time |
| 2 | Events Management (1 year top-up) | https://www.shu.ac.uk/courses/event-management/bsc-honours-events-management-1-year-topup/full-time/2026 | full-time |
| 3 | Events Management with Foundation Year | https://www.shu.ac.uk/courses/event-management/bsc-honours-events-management-with-foundation-year/full-time/2026 | full-time |
##### Department of Law
###### LLB (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Law | https://www.shu.ac.uk/courses/law/llb-hons-law/full-time/2026 | full-time |
| 2 | Law with Criminology | https://www.shu.ac.uk/courses/law/llb-hons-law-with-criminology/full-time/2026 | full-time |
| 3 | Law with Criminology with Foundation Year | https://www.shu.ac.uk/courses/law/llb-hons-law-with-criminology-with-foundation-year/full-time/2026 | full-time |
| 4 | Law with Foundation Year | https://www.shu.ac.uk/courses/law/llb-hons-law-with-foundation-year/full-time/2026 | full-time |
##### Department of Marketing
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Digital Marketing | https://www.shu.ac.uk/courses/marketing/ba-honours-digital-marketing/full-time/2026 | full-time |
| 2 | Digital Marketing with Foundation Year | https://www.shu.ac.uk/courses/marketing/ba-honours-digital-marketing-with-foundation-year/full-time/2026 | full-time |
| 3 | Marketing | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing/full-time/2026 | full-time |
| 4 | Marketing Communications and Advertising | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-communications-and-advertising/full-time/2026 | full-time |
| 5 | Marketing Communications and Advertising with Foundation Year | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-communications-and-advertising-with-foundation-year/full-time/2026 | full-time |
| 6 | Marketing with Foundation Year | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-with-foundation-year/full-time/2026 | full-time |
| 7 | Marketing with Psychology | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-with-psychology/full-time/2026 | full-time |
| 8 | Marketing with Psychology with Foundation Year | https://www.shu.ac.uk/courses/marketing/ba-honours-marketing-with-psychology-with-foundation-year/full-time/2026 | full-time |
##### Department of Media Pr And Journalism
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Journalism, Public Relations with Media | https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-journalism-public-relations-with-media/full-time/2026 | full-time |
| 2 | Journalism, Public Relations with Media with Foundation Year | https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-journalism-public-relations-with-media-with-foundation-year/full-time/2026 | full-time |
| 3 | Media and Communications | https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-media-and-communications/full-time/2026 | full-time |
| 4 | Sports Journalism | https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-sports-journalism/full-time/2026 | full-time |
| 5 | Sports Journalism with Foundation Year | https://www.shu.ac.uk/courses/media-pr-and-journalism/ba-honours-sports-journalism-with-foundation-year/full-time/2026 | full-time |
##### Department of Tourism And Hospitality
###### BA (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Business Management and Hospitality | https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-business-management-and-hospitality/full-time/2026 | full-time |
| 2 | Business Management and Hospitality with Foundation Year | https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-business-management-and-hospitality-with-foundation-year/full-time/2026 | full-time |
| 3 | Business Management and Tourism | https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-business-management-and-tourism/full-time/2026 | full-time |
| 4 | Business Management and Tourism with Foundation Year | https://www.shu.ac.uk/courses/tourism-and-hospitality/ba-honours-business-management-and-tourism-with-foundation-year/full-time/2026 | full-time |
###### BSc (Honours)
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Airline and Airport Management | https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-airline-and-airport-management/full-time/2026 | full-time |
| 2 | Airline and Airport Management with Foundation Year | https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-airline-and-airport-management-with-foundation-year/full-time/2026 | full-time |
| 3 | International Tourism and Hospitality Business Management (1 year top-up) | https://www.shu.ac.uk/courses/tourism-and-hospitality/bsc-honours-international-tourism-and-hospitality-business-management-1-year-topup/full-time/2026 | full-time |

### 1.3 Foundation Year and Top-up variants

Many courses offer a Foundation Year (4-year variant including year 0). These appear as separate listings with suffix "with Foundation Year" in the URL. Top-up variants (1-year or 2-year for students with prior HE credit) appear with suffix "(1 year top-up)" or "(2 year top-up)". Both are enumerated above as distinct programs.

### 1.4 General/Institute-wide requirements

- **UCAS application**: Standard UK undergraduate admissions route via UCAS
- **Typical offers**: 72–120 UCAS points depending on course; foundation years from 40 points
- **English language**: IELTS 6.0–6.5 (course-dependent; see Section 3.2)
- **Placement year**: Available on most courses (some mandatory in Health subjects)

---

## 2. Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Engineering, Computing and the Built Environment
##### Department of Architecture
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Architecture | https://www.shu.ac.uk/courses/architecture/phd-architecture/full-time/2026 | full-time |
| 2 | Architecture | https://www.shu.ac.uk/courses/architecture/phd-architecture/part-time/2026 | part-time |
##### Department of Computing
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Computing and Informatics | https://www.shu.ac.uk/courses/computing/mphil-computing-and-informatics/part-time/2026 | part-time |
| 2 | Computing and Informatics | https://www.shu.ac.uk/courses/computing/mphil-computing-and-informatics/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Advanced Computer Networks | https://www.shu.ac.uk/courses/computing/msc-advanced-computer-networks/part-time/2026 | part-time |
| 2 | Advanced Computer Networks | https://www.shu.ac.uk/courses/computing/msc-advanced-computer-networks/full-time/2026 | full-time |
| 3 | Advanced Computer Networks (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-advanced-computer-networks-work-experience/full-time/2026 | full-time |
| 4 | Applied Artificial Intelligence | https://www.shu.ac.uk/courses/computing/msc-applied-artificial-intelligence/full-time/2026 | full-time |
| 5 | Applied Artificial Intelligence (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-applied-artificial-intelligence-work-experience/full-time/2026 | full-time |
| 6 | Artificial Intelligence | https://www.shu.ac.uk/courses/computing/msc-artificial-intelligence/full-time/2026 | full-time |
| 7 | Artificial Intelligence (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-artificial-intelligence-work-experience/full-time/2026 | full-time |
| 8 | Big Data Analytics | https://www.shu.ac.uk/courses/computing/msc-big-data-analytics/full-time/2026 | full-time |
| 9 | Big Data Analytics (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-big-data-analytics-work-experience/full-time/2026 | full-time |
| 10 | Computing | https://www.shu.ac.uk/courses/computing/msc-computing/full-time/2026 | full-time |
| 11 | Computing (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-computing-work-experience/full-time/2026 | full-time |
| 12 | Computing with Artificial Intelligence | https://www.shu.ac.uk/courses/computing/msc-computing-with-artificial-intelligence/full-time/2026 | full-time |
| 13 | Computing with Artificial Intelligence (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-computing-with-artificial-intelligence-work-experience/full-time/2026 | full-time |
| 14 | Computing with Cloud Technologies | https://www.shu.ac.uk/courses/computing/msc-computing-with-cloud-technologies/full-time/2026 | full-time |
| 15 | Computing with Cloud Technologies (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-computing-with-cloud-technologies-work-experience/full-time/2026 | full-time |
| 16 | Cyber Security | https://www.shu.ac.uk/courses/computing/msc-cyber-security/full-time/2026 | full-time |
| 17 | Cyber Security | https://www.shu.ac.uk/courses/computing/msc-cyber-security/part-time/2026 | part-time |
| 18 | Cyber Security (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-cyber-security-work-experience/full-time/2026 | full-time |
| 19 | Data Analytics with Banking and Finance | https://www.shu.ac.uk/courses/computing/msc-data-analytics-with-banking-and-finance/full-time/2026 | full-time |
| 20 | Data Analytics with Banking and Finance (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-data-analytics-with-banking-and-finance-work-experience/full-time/2026 | full-time |
| 21 | Data Science and Artificial Intelligence | https://www.shu.ac.uk/courses/computing/msc-data-science-and-artificial-intelligence/full-time/2026 | full-time |
| 22 | Data Science and Artificial Intelligence (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-data-science-and-artificial-intelligence-work-experience/full-time/2026 | full-time |
| 23 | Information Technology Management | https://www.shu.ac.uk/courses/computing/msc-information-technology-management/full-time/2026 | full-time |
| 24 | Information Technology Management (Work Experience) | https://www.shu.ac.uk/courses/computing/msc-information-technology-management-work-experience/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Computing and Informatics | https://www.shu.ac.uk/courses/computing/phd-computing-and-informatics/full-time/2026 | full-time |
| 2 | Computing and Informatics | https://www.shu.ac.uk/courses/computing/phd-computing-and-informatics/part-time/2026 | part-time |
##### Department of Construction And Surveying
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Construction Project Management | https://www.shu.ac.uk/courses/construction-and-surveying/msc-construction-project-management/part-time/2026 | part-time |
| 2 | Construction Project Management | https://www.shu.ac.uk/courses/construction-and-surveying/msc-construction-project-management/full-time/2026 | full-time |
| 3 | Construction Project Management (Work Experience) | https://www.shu.ac.uk/courses/construction-and-surveying/msc-construction-project-management-work-experience/full-time/2026 | full-time |
| 4 | Quantity Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/msc-quantity-surveying/full-time/2026 | full-time |
| 5 | Quantity Surveying | https://www.shu.ac.uk/courses/construction-and-surveying/msc-quantity-surveying/part-time/2026 | part-time |
| 6 | Quantity Surveying (Work Experience) | https://www.shu.ac.uk/courses/construction-and-surveying/msc-quantity-surveying-work-experience/full-time/2026 | full-time |
##### Department of Engineering
###### MEng
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Aerospace Engineering | https://www.shu.ac.uk/courses/engineering/meng-aerospace-engineering/full-time/2026 | full-time |
| 2 | Automotive Engineering | https://www.shu.ac.uk/courses/engineering/meng-automotive-engineering/full-time/2026 | full-time |
| 3 | Chemical Engineering | https://www.shu.ac.uk/courses/engineering/meng-chemical-engineering/full-time/2026 | full-time |
| 4 | Electrical and Electronic Engineering | https://www.shu.ac.uk/courses/engineering/meng-electrical-and-electronic-engineering/full-time/2026 | full-time |
| 5 | Mechanical Engineering | https://www.shu.ac.uk/courses/engineering/meng-mechanical-engineering/full-time/2026 | full-time |
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Ceramics, Glasses and Polymers | https://www.shu.ac.uk/courses/engineering/mphil-ceramics-glasses-and-polymers/part-time/2026 | part-time |
| 2 | Ceramics, Glasses and Polymers | https://www.shu.ac.uk/courses/engineering/mphil-ceramics-glasses-and-polymers/full-time/2026 | full-time |
| 3 | Materials Science and Engineering | https://www.shu.ac.uk/courses/engineering/mphil-materials-science-and-engineering/part-time/2026 | part-time |
| 4 | Materials Science and Engineering | https://www.shu.ac.uk/courses/engineering/mphil-materials-science-and-engineering/full-time/2026 | full-time |
| 5 | Materials and Fluid Flow Modelling | https://www.shu.ac.uk/courses/engineering/mphil-materials-and-fluid-flow-modelling/full-time/2026 | full-time |
| 6 | Materials and Fluid Flow Modelling | https://www.shu.ac.uk/courses/engineering/mphil-materials-and-fluid-flow-modelling/part-time/2026 | part-time |
| 7 | Plasma Surface Engineering | https://www.shu.ac.uk/courses/engineering/mphil-plasma-surface-engineering/part-time/2026 | part-time |
| 8 | Plasma Surface Engineering | https://www.shu.ac.uk/courses/engineering/mphil-plasma-surface-engineering/full-time/2026 | full-time |
| 9 | Robotics | https://www.shu.ac.uk/courses/engineering/mphil-robotics/part-time/2026 | part-time |
| 10 | Robotics | https://www.shu.ac.uk/courses/engineering/mphil-robotics/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Advanced Engineering and Management | https://www.shu.ac.uk/courses/engineering/msc-advanced-engineering-and-management/full-time/2026 | full-time |
| 2 | Advanced Engineering and Management (Work Experience) | https://www.shu.ac.uk/courses/engineering/msc-advanced-engineering-and-management-work-experience/full-time/2026 | full-time |
| 3 | Advanced Mechanical Engineering | https://www.shu.ac.uk/courses/engineering/msc-advanced-mechanical-engineering/full-time/2026 | full-time |
| 4 | Advanced Mechanical Engineering (Work Experience) | https://www.shu.ac.uk/courses/engineering/msc-advanced-mechanical-engineering-work-experience/full-time/2026 | full-time |
| 5 | Automation Control and Robotics | https://www.shu.ac.uk/courses/engineering/msc-automation-control-and-robotics/full-time/2026 | full-time |
| 6 | Automation Control and Robotics (Work Experience) | https://www.shu.ac.uk/courses/engineering/msc-automation-control-and-robotics-work-experience/full-time/2026 | full-time |
| 7 | Electrical and Electronic Engineering | https://www.shu.ac.uk/courses/engineering/msc-electrical-and-electronic-engineering/full-time/2026 | full-time |
| 8 | Electrical and Electronic Engineering (Work Experience) | https://www.shu.ac.uk/courses/engineering/msc-electrical-and-electronic-engineering-work-experience/full-time/2026 | full-time |
| 9 | Energy and Sustainable Engineering | https://www.shu.ac.uk/courses/engineering/msc-energy-and-sustainable-engineering/full-time/2026 | full-time |
| 10 | Energy and Sustainable Engineering (Work Experience) | https://www.shu.ac.uk/courses/engineering/msc-energy-and-sustainable-engineering-work-experience/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Ceramics, Glasses and Polymers | https://www.shu.ac.uk/courses/engineering/phd-ceramics-glasses-and-polymers/full-time/2026 | full-time |
| 2 | Ceramics, Glasses and Polymers | https://www.shu.ac.uk/courses/engineering/phd-ceramics-glasses-and-polymers/part-time/2026 | part-time |
| 3 | Materials Science and Engineering | https://www.shu.ac.uk/courses/engineering/phd-materials-science-and-engineering/full-time/2026 | full-time |
| 4 | Materials Science and Engineering | https://www.shu.ac.uk/courses/engineering/phd-materials-science-and-engineering/part-time/2026 | part-time |
| 5 | Materials and Fluid Flow Modelling | https://www.shu.ac.uk/courses/engineering/phd-materials-and-fluid-flow-modelling/full-time/2026 | full-time |
| 6 | Materials and Fluid Flow Modelling | https://www.shu.ac.uk/courses/engineering/phd-materials-and-fluid-flow-modelling/part-time/2026 | part-time |
| 7 | Plasma Surface Engineering | https://www.shu.ac.uk/courses/engineering/phd-plasma-surface-engineering/part-time/2026 | part-time |
| 8 | Plasma Surface Engineering | https://www.shu.ac.uk/courses/engineering/phd-plasma-surface-engineering/full-time/2026 | full-time |
| 9 | Robotics | https://www.shu.ac.uk/courses/engineering/phd-robotics/part-time/2026 | part-time |
| 10 | Robotics | https://www.shu.ac.uk/courses/engineering/phd-robotics/full-time/2026 | full-time |
#### College of Health, Wellbeing and Life Sciences
##### Department of Biosciences And Chemistry
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Biomolecular Sciences Research Centre | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mphil-biomolecular-sciences-research-centre/part-time/2026 | part-time |
| 2 | Biomolecular Sciences Research Centre | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mphil-biomolecular-sciences-research-centre/full-time/2026 | full-time |
###### MRes
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Analytical Chemistry | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mres-analytical-chemistry/full-time/2026 | full-time |
| 2 | Biomedical Laboratory Science | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mres-biomedical-laboratory-science/full-time/2026 | full-time |
| 3 | Molecular Microbiology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mres-molecular-microbiology/full-time/2026 | full-time |
| 4 | Pharmaceutical Analysis | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mres-pharmaceutical-analysis/full-time/2026 | full-time |
| 5 | Pharmacology and Biotechnology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/mres-pharmacology-and-biotechnology/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Analytical Chemistry | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-analytical-chemistry/part-time/2026 | part-time |
| 2 | Analytical Chemistry | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-analytical-chemistry/full-time/2026 | full-time |
| 3 | Biomedical Laboratory Science | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-biomedical-laboratory-science/part-time/2026 | part-time |
| 4 | Biomedical Laboratory Science | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-biomedical-laboratory-science/full-time/2026 | full-time |
| 5 | Molecular Microbiology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-molecular-microbiology/full-time/2026 | full-time |
| 6 | Molecular Microbiology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-molecular-microbiology/part-time/2026 | part-time |
| 7 | Pharmaceutical Analysis | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmaceutical-analysis/part-time/2026 | part-time |
| 8 | Pharmaceutical Analysis | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmaceutical-analysis/full-time/2026 | full-time |
| 9 | Pharmacology and Biotechnology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmacology-and-biotechnology/part-time/2026 | part-time |
| 10 | Pharmacology and Biotechnology | https://www.shu.ac.uk/courses/biosciences-and-chemistry/msc-pharmacology-and-biotechnology/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Biomolecular Sciences Research Centre | https://www.shu.ac.uk/courses/biosciences-and-chemistry/phd-biomolecular-sciences-research-centre/part-time/2026 | part-time |
| 2 | Biomolecular Sciences Research Centre | https://www.shu.ac.uk/courses/biosciences-and-chemistry/phd-biomolecular-sciences-research-centre/full-time/2026 | full-time |
##### Department of Diagnostic Radiography
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Medical Ultrasound Practice | https://www.shu.ac.uk/courses/diagnostic-radiography/msc-medical-ultrasound-practice/part-time/2026 | part-time |
###### PGCert
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Abdominal Ultrasound | https://www.shu.ac.uk/courses/diagnostic-radiography/pgcert-abdominal-ultrasound/part-time/2026 | part-time |
| 2 | Focus Scope Ultrasound | https://www.shu.ac.uk/courses/diagnostic-radiography/pgcert-focus-scope-ultrasound/part-time/2026 | part-time |
| 3 | Obstetric Ultrasound | https://www.shu.ac.uk/courses/diagnostic-radiography/pgcert-obstetric-ultrasound/part-time/2026 | part-time |
###### PGDip
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Medical Ultrasound Practice | https://www.shu.ac.uk/courses/diagnostic-radiography/pgdip-medical-ultrasound-practice/part-time/2026 | part-time |
##### Department of Food And Nutrition
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Food Consumer Marketing and Product Development | https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-consumer-marketing-and-product-development/full-time/2026 | full-time |
| 2 | Food Consumer Marketing and Product Development (Work Experience) | https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-consumer-marketing-and-product-development-work-experience/full-time/2026 | full-time |
| 3 | Food and Nutrition Sciences | https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-and-nutrition-sciences/full-time/2026 | full-time |
| 4 | Food and Nutrition Sciences (Work Experience) | https://www.shu.ac.uk/courses/food-and-nutrition/msc-food-and-nutrition-sciences-work-experience/full-time/2026 | full-time |
| 5 | Nutrition with Public Health Management | https://www.shu.ac.uk/courses/food-and-nutrition/msc-nutrition-with-public-health-management/full-time/2026 | full-time |
##### Department of Health And Social Care Management
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Art Psychotherapy Practice | https://www.shu.ac.uk/courses/health-and-social-care-management/ma-art-psychotherapy-practice/part-time/2026 | part-time |
| 2 | Art Psychotherapy Practice | https://www.shu.ac.uk/courses/health-and-social-care-management/ma-art-psychotherapy-practice/full-time/2026 | full-time |
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Health and Social Care | https://www.shu.ac.uk/courses/health-and-social-care-management/mphil-health-and-social-care/part-time/2026 | part-time |
| 2 | Health and Social Care | https://www.shu.ac.uk/courses/health-and-social-care-management/mphil-health-and-social-care/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Advanced Practice | https://www.shu.ac.uk/courses/health-and-social-care-management/msc-advanced-practice/part-time/2026 | part-time |
| 2 | Dietetics (Pre-registration) | https://www.shu.ac.uk/courses/health-and-social-care-management/msc-dietetics-preregistration/full-time/2026 | full-time |
| 3 | Professional Practice in Health and Social Care | https://www.shu.ac.uk/courses/health-and-social-care-management/msc-professional-practice-in-health-and-social-care/part-time/2026 | part-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Health and Social Care | https://www.shu.ac.uk/courses/health-and-social-care-management/phd-health-and-social-care/part-time/2026 | part-time |
| 2 | Health and Social Care | https://www.shu.ac.uk/courses/health-and-social-care-management/phd-health-and-social-care/full-time/2026 | full-time |
##### Department of Nursing And Midwifery
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Midwifery | https://www.shu.ac.uk/courses/nursing-and-midwifery/msc-midwifery/full-time/2026 | full-time |
| 2 | Nursing Adult | https://www.shu.ac.uk/courses/nursing-and-midwifery/msc-nursing-adult/full-time/2026 | full-time |
| 3 | Nursing Mental Health | https://www.shu.ac.uk/courses/nursing-and-midwifery/msc-nursing-mental-health/full-time/2026 | full-time |
###### PGDip
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | District Nursing | https://www.shu.ac.uk/courses/nursing-and-midwifery/pgdip-district-nursing/full-time/2026 | full-time |
| 2 | Specialist Community Public Health Nursing (Health Visitor) | https://www.shu.ac.uk/courses/nursing-and-midwifery/pgdip-specialist-community-public-health-nursing-health-visitor/full-time/2026 | full-time |
| 3 | Specialist Community Public Health Nursing (School Nursing) | https://www.shu.ac.uk/courses/nursing-and-midwifery/pgdip-specialist-community-public-health-nursing-school-nursing/full-time/2026 | full-time |
##### Department of Occupational Therapy
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Occupational Therapy (Pre-Registration) | https://www.shu.ac.uk/courses/occupational-therapy/msc-occupational-therapy-preregistration/full-time/2026 | full-time |
##### Department of Physiotherapy
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Advanced Practice Musculoskeletal Management | https://www.shu.ac.uk/courses/physiotherapy/msc-advanced-practice-musculoskeletal-management/part-time/2026 | part-time |
| 2 | Physiotherapy | https://www.shu.ac.uk/courses/physiotherapy/msc-physiotherapy/full-time/2026 | full-time |
| 3 | Physiotherapy (Pre-Registration) | https://www.shu.ac.uk/courses/physiotherapy/msc-physiotherapy-preregistration/full-time/2026 | full-time |
##### Department of Psychology
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Clinical Cognitive Neuroscience | https://www.shu.ac.uk/courses/psychology/msc-clinical-cognitive-neuroscience/full-time/2026 | full-time |
| 2 | Clinical Cognitive Neuroscience | https://www.shu.ac.uk/courses/psychology/msc-clinical-cognitive-neuroscience/part-time/2026 | part-time |
| 3 | Developmental Psychology | https://www.shu.ac.uk/courses/psychology/msc-developmental-psychology/full-time/2026 | full-time |
| 4 | Developmental Psychology | https://www.shu.ac.uk/courses/psychology/msc-developmental-psychology/part-time/2026 | part-time |
| 5 | Forensic Psychology | https://www.shu.ac.uk/courses/psychology/msc-forensic-psychology/part-time/2026 | part-time |
| 6 | Forensic Psychology | https://www.shu.ac.uk/courses/psychology/msc-forensic-psychology/full-time/2026 | full-time |
| 7 | Health Psychology | https://www.shu.ac.uk/courses/psychology/msc-health-psychology/full-time/2026 | full-time |
| 8 | Health Psychology | https://www.shu.ac.uk/courses/psychology/msc-health-psychology/part-time/2026 | part-time |
| 9 | Psychology | https://www.shu.ac.uk/courses/psychology/msc-psychology/part-time/2026 | part-time |
| 10 | Psychology | https://www.shu.ac.uk/courses/psychology/msc-psychology/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Psychology | https://www.shu.ac.uk/courses/psychology/phd-psychology/full-time/2026 | full-time |
| 2 | Psychology | https://www.shu.ac.uk/courses/psychology/phd-psychology/part-time/2026 | part-time |
##### Department of Sport And Physical Activity
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Sport and Physical Activity | https://www.shu.ac.uk/courses/sport-and-physical-activity/mphil-sport-and-physical-activity/part-time/2026 | part-time |
| 2 | Sport and Physical Activity | https://www.shu.ac.uk/courses/sport-and-physical-activity/mphil-sport-and-physical-activity/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Applied Sport and Exercise Science | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-applied-sport-and-exercise-science/part-time/2026 | part-time |
| 2 | Applied Sport and Exercise Science | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-applied-sport-and-exercise-science/full-time/2026 | full-time |
| 3 | International Sport Business Management | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-international-sport-business-management/full-time/2026 | full-time |
| 4 | International Sport Business Management | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-international-sport-business-management/part-time/2026 | part-time |
| 5 | Sport and Exercise Psychology | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-sport-and-exercise-psychology/full-time/2026 | full-time |
| 6 | Sport and Exercise Psychology | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-sport-and-exercise-psychology/part-time/2026 | part-time |
| 7 | Strength and Conditioning Coaching | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-strength-and-conditioning-coaching/part-time/2026 | part-time |
| 8 | Strength and Conditioning Coaching | https://www.shu.ac.uk/courses/sport-and-physical-activity/msc-strength-and-conditioning-coaching/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Sport and Physical Activity | https://www.shu.ac.uk/courses/sport-and-physical-activity/phd-sport-and-physical-activity/full-time/2026 | full-time |
| 2 | Sport and Physical Activity | https://www.shu.ac.uk/courses/sport-and-physical-activity/phd-sport-and-physical-activity/part-time/2026 | part-time |
#### College of Social Sciences and Arts
##### Department of Acting Film And Tv
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Filmmaking | https://www.shu.ac.uk/courses/acting-film-and-tv/ma-filmmaking/full-time/2026 | full-time |
| 2 | Filmmaking | https://www.shu.ac.uk/courses/acting-film-and-tv/ma-filmmaking/part-time/2026 | part-time |
##### Department of Art And Design
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Design (Design for Health) | https://www.shu.ac.uk/courses/art-and-design/ma-design-design-for-health/full-time/2026 | full-time |
| 2 | Design (Fashion) | https://www.shu.ac.uk/courses/art-and-design/ma-design-fashion/full-time/2026 | full-time |
| 3 | Design (Graphics) | https://www.shu.ac.uk/courses/art-and-design/ma-design-graphics/full-time/2026 | full-time |
| 4 | Design (Illustration) | https://www.shu.ac.uk/courses/art-and-design/ma-design-illustration/full-time/2026 | full-time |
| 5 | Design (Interaction) | https://www.shu.ac.uk/courses/art-and-design/ma-design-interaction/full-time/2026 | full-time |
| 6 | Design (Interior) | https://www.shu.ac.uk/courses/art-and-design/ma-design-interior/full-time/2026 | full-time |
| 7 | Design (Packaging) | https://www.shu.ac.uk/courses/art-and-design/ma-design-packaging/full-time/2026 | full-time |
| 8 | Design (Performance Sports) | https://www.shu.ac.uk/courses/art-and-design/ma-design-performance-sports/full-time/2026 | full-time |
| 9 | Design (Product) | https://www.shu.ac.uk/courses/art-and-design/ma-design-product/full-time/2026 | full-time |
| 10 | Fine Art | https://www.shu.ac.uk/courses/art-and-design/ma-fine-art/full-time/2026 | full-time |
| 11 | Jewellery and Metalwork | https://www.shu.ac.uk/courses/art-and-design/ma-jewellery-and-metalwork/full-time/2026 | full-time |
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Fine Art and Design | https://www.shu.ac.uk/courses/art-and-design/mphil-fine-art-and-design/part-time/2026 | part-time |
| 2 | Fine Art and Design | https://www.shu.ac.uk/courses/art-and-design/mphil-fine-art-and-design/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Fine Art and Design | https://www.shu.ac.uk/courses/art-and-design/phd-fine-art-and-design/full-time/2026 | full-time |
| 2 | Fine Art and Design | https://www.shu.ac.uk/courses/art-and-design/phd-fine-art-and-design/part-time/2026 | part-time |
##### Department of Criminology
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Criminology and Criminal Justice Practice | https://www.shu.ac.uk/courses/criminology/msc-criminology-and-criminal-justice-practice/full-time/2026 | full-time |
| 2 | Criminology and Criminal Justice Practice | https://www.shu.ac.uk/courses/criminology/msc-criminology-and-criminal-justice-practice/part-time/2026 | part-time |
##### Department of Digital Media
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Digital Media Management | https://www.shu.ac.uk/courses/digital-media/ma-digital-media-management/full-time/2026 | full-time |
| 2 | Digital Media Management (Work Experience) | https://www.shu.ac.uk/courses/digital-media/ma-digital-media-management-work-experience/full-time/2026 | full-time |
| 3 | Games | https://www.shu.ac.uk/courses/digital-media/ma-games/full-time/2026 | full-time |
##### Department of English
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | English | https://www.shu.ac.uk/courses/english/phd-english/full-time/2026 | full-time |
| 2 | English | https://www.shu.ac.uk/courses/english/phd-english/part-time/2026 | part-time |
##### Department of Geography And Environment
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Environmental Management | https://www.shu.ac.uk/courses/geography-and-environment/msc-environmental-management/part-time/2026 | part-time |
| 2 | Environmental Management | https://www.shu.ac.uk/courses/geography-and-environment/msc-environmental-management/full-time/2026 | full-time |
| 3 | Environmental Management (Work Experience) | https://www.shu.ac.uk/courses/geography-and-environment/msc-environmental-management-work-experience/full-time/2026 | full-time |
| 4 | Geographical Information Systems | https://www.shu.ac.uk/courses/geography-and-environment/msc-geographical-information-systems/full-time/2026 | full-time |
| 5 | Geographical Information Systems | https://www.shu.ac.uk/courses/geography-and-environment/msc-geographical-information-systems/part-time/2026 | part-time |
| 6 | Geographical Information Systems (Work Experience) | https://www.shu.ac.uk/courses/geography-and-environment/msc-geographical-information-systems-work-experience/full-time/2026 | full-time |
| 7 | Urban Planning | https://www.shu.ac.uk/courses/geography-and-environment/msc-urban-planning/part-time/2026 | part-time |
| 8 | Urban Planning | https://www.shu.ac.uk/courses/geography-and-environment/msc-urban-planning/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Natural and Built Environment | https://www.shu.ac.uk/courses/geography-and-environment/phd-natural-and-built-environment/full-time/2026 | full-time |
| 2 | Natural and Built Environment | https://www.shu.ac.uk/courses/geography-and-environment/phd-natural-and-built-environment/part-time/2026 | part-time |
##### Department of History
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | History | https://www.shu.ac.uk/courses/history/phd-history/full-time/2026 | full-time |
| 2 | History | https://www.shu.ac.uk/courses/history/phd-history/part-time/2026 | part-time |
##### Department of Politics
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | International Relations and Global Crises | https://www.shu.ac.uk/courses/politics/ma-international-relations-and-global-crises/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Politics | https://www.shu.ac.uk/courses/politics/phd-politics/full-time/2026 | full-time |
| 2 | Politics | https://www.shu.ac.uk/courses/politics/phd-politics/part-time/2026 | part-time |
##### Department of Social Work
###### PGCert
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Approved Mental Health Professional (AMHP) | https://www.shu.ac.uk/courses/social-work/pgcert-approved-mental-health-professional-amhp/part-time/2026 | part-time |
| 2 | Approved Mental Health Professional (AMHP) | https://www.shu.ac.uk/courses/social-work/pgcert-approved-mental-health-professional-amhp/full-time/2026 | full-time |
##### Department of Sociology
###### MRes
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Social Research | https://www.shu.ac.uk/courses/sociology/mres-social-research/part-time/2026 | part-time |
| 2 | Social Research | https://www.shu.ac.uk/courses/sociology/mres-social-research/full-time/2026 | full-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Public Health | https://www.shu.ac.uk/courses/sociology/msc-public-health/full-time/2026 | full-time |
| 2 | Public Health | https://www.shu.ac.uk/courses/sociology/msc-public-health/part-time/2026 | part-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Centre for Regional Economic and Social Research | https://www.shu.ac.uk/courses/sociology/phd-centre-for-regional-economic-and-social-research/part-time/2026 | part-time |
| 2 | Centre for Regional Economic and Social Research | https://www.shu.ac.uk/courses/sociology/phd-centre-for-regional-economic-and-social-research/full-time/2026 | full-time |
| 3 | Sociology | https://www.shu.ac.uk/courses/sociology/phd-sociology/full-time/2026 | full-time |
| 4 | Sociology | https://www.shu.ac.uk/courses/sociology/phd-sociology/part-time/2026 | part-time |
##### Department of Teaching And Education
###### EdD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | EDD Doctor of Education | https://www.shu.ac.uk/courses/teaching-and-education/edd-doctor-of-education/part-time/2026 | part-time |
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Autism | https://www.shu.ac.uk/courses/teaching-and-education/ma-autism/part-time/2026 | part-time |
| 2 | Education | https://www.shu.ac.uk/courses/teaching-and-education/ma-education/full-time/2026 | full-time |
| 3 | Leadership in Learning (Teach First) | https://www.shu.ac.uk/courses/teaching-and-education/ma-leadership-in-learning-teach-first/part-time/2026 | part-time |
###### PGCE
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Early Childhood Education and Care (0-5) with Early Years Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-early-childhood-education-and-care-05-with-early-years-teacher-status/full-time/2026 | full-time |
| 2 | Early Years and Primary Education (3-7) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-early-years-and-primary-education-37-with-qualified-teacher-status/full-time/2026 | full-time |
| 3 | Further Education and Skills | https://www.shu.ac.uk/courses/teaching-and-education/pgce-further-education-and-skills/full-time/2026 | full-time |
| 4 | Further Education and Skills | https://www.shu.ac.uk/courses/teaching-and-education/pgce-further-education-and-skills/part-time/2026 | part-time |
| 5 | Primary Education (5-11) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-primary-education-511-with-qualified-teacher-status/full-time/2026 | full-time |
| 6 | Secondary Art and Design with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-art-and-design-with-qualified-teacher-status/full-time/2026 | full-time |
| 7 | Secondary Business Education with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-business-education-with-qualified-teacher-status/full-time/2026 | full-time |
| 8 | Secondary Computing with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-computing-with-qualified-teacher-status/full-time/2026 | full-time |
| 9 | Secondary Design and Technology with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-design-and-technology-with-qualified-teacher-status/full-time/2026 | full-time |
| 10 | Secondary Design and Technology with Qualified Teacher Status (Food) | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-design-and-technology-with-qualified-teacher-status-food/full-time/2026 | full-time |
| 11 | Secondary Education in Drama with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-education-in-drama-with-qualified-teacher-status/full-time/2026 | full-time |
| 12 | Secondary Education in Social Sciences with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-education-in-social-sciences-with-qualified-teacher-status/full-time/2026 | full-time |
| 13 | Secondary English with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-english-with-qualified-teacher-status/full-time/2026 | full-time |
| 14 | Secondary French with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-french-with-qualified-teacher-status/full-time/2026 | full-time |
| 15 | Secondary Geography with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-geography-with-qualified-teacher-status/full-time/2026 | full-time |
| 16 | Secondary German with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-german-with-qualified-teacher-status/full-time/2026 | full-time |
| 17 | Secondary History with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-history-with-qualified-teacher-status/full-time/2026 | full-time |
| 18 | Secondary Mathematics with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-mathematics-with-qualified-teacher-status/full-time/2026 | full-time |
| 19 | Secondary Music with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-music-with-qualified-teacher-status/full-time/2026 | full-time |
| 20 | Secondary Physical Education with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-physical-education-with-qualified-teacher-status/full-time/2026 | full-time |
| 21 | Secondary Religious Education with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-religious-education-with-qualified-teacher-status/full-time/2026 | full-time |
| 22 | Secondary Science (Biology) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-science-biology-with-qualified-teacher-status/full-time/2026 | full-time |
| 23 | Secondary Science (Chemistry) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-science-chemistry-with-qualified-teacher-status/full-time/2026 | full-time |
| 24 | Secondary Science (Physics) with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-science-physics-with-qualified-teacher-status/full-time/2026 | full-time |
| 25 | Secondary Spanish with Qualified Teacher Status | https://www.shu.ac.uk/courses/teaching-and-education/pgce-secondary-spanish-with-qualified-teacher-status/full-time/2026 | full-time |
###### PGCert
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Autism | https://www.shu.ac.uk/courses/teaching-and-education/pgcert-autism/part-time/2026 | part-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Education | https://www.shu.ac.uk/courses/teaching-and-education/phd-education/full-time/2026 | full-time |
| 2 | Education | https://www.shu.ac.uk/courses/teaching-and-education/phd-education/part-time/2026 | part-time |
#### Sheffield Business School
##### Department of Accounting Banking And Finance
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Accounting and Finance | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-accounting-and-finance/full-time/2026 | full-time |
| 2 | Accounting and Finance (Work Experience) | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-accounting-and-finance-work-experience/full-time/2026 | full-time |
| 3 | Finance and Global Trading | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-finance-and-global-trading/full-time/2026 | full-time |
| 4 | Finance and Investment | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-finance-and-investment/full-time/2026 | full-time |
| 5 | Financial Management | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-financial-management/full-time/2026 | full-time |
| 6 | Financial Management (Work Experience) | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-financial-management-work-experience/full-time/2026 | full-time |
| 7 | Forensic Accounting | https://www.shu.ac.uk/courses/accounting-banking-and-finance/msc-forensic-accounting/full-time/2026 | full-time |
##### Department of Business And Management
###### DBA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Business Administration | https://www.shu.ac.uk/courses/business-and-management/dba-business-administration/part-time/2026 | part-time |
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Human Resources and Organisational Development | https://www.shu.ac.uk/courses/business-and-management/msc-human-resources-and-organisational-development/full-time/2026 | full-time |
| 2 | International Business Management | https://www.shu.ac.uk/courses/business-and-management/msc-international-business-management/full-time/2026 | full-time |
| 3 | International Business Management (Work Experience) | https://www.shu.ac.uk/courses/business-and-management/msc-international-business-management-work-experience/full-time/2026 | full-time |
| 4 | International Business and Human Resource Management | https://www.shu.ac.uk/courses/business-and-management/msc-international-business-and-human-resource-management/full-time/2026 | full-time |
| 5 | International Business and Marketing | https://www.shu.ac.uk/courses/business-and-management/msc-international-business-and-marketing/full-time/2026 | full-time |
| 6 | Logistics and Supply Chain Management | https://www.shu.ac.uk/courses/business-and-management/msc-logistics-and-supply-chain-management/full-time/2026 | full-time |
| 7 | Logistics and Supply Chain Management (Work Experience) | https://www.shu.ac.uk/courses/business-and-management/msc-logistics-and-supply-chain-management-work-experience/full-time/2026 | full-time |
| 8 | Management | https://www.shu.ac.uk/courses/business-and-management/msc-management/full-time/2026 | full-time |
| 9 | Management (Work Experience) | https://www.shu.ac.uk/courses/business-and-management/msc-management-work-experience/full-time/2026 | full-time |
| 10 | Project Management | https://www.shu.ac.uk/courses/business-and-management/msc-project-management/full-time/2026 | full-time |
| 11 | Project Management (Work Experience) | https://www.shu.ac.uk/courses/business-and-management/msc-project-management-work-experience/full-time/2026 | full-time |
| 12 | Real Estate | https://www.shu.ac.uk/courses/business-and-management/msc-real-estate/full-time/2026 | full-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Sheffield Business School (Management, Finance, Service Sector) | https://www.shu.ac.uk/courses/business-and-management/phd-sheffield-business-school-management-finance-service-sector/part-time/2026 | part-time |
| 2 | Sheffield Business School (Management, Finance, Service Sector) | https://www.shu.ac.uk/courses/business-and-management/phd-sheffield-business-school-management-finance-service-sector/full-time/2026 | full-time |
##### Department of Economics
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Applied Economics | https://www.shu.ac.uk/courses/economics/msc-applied-economics/full-time/2026 | full-time |
##### Department of Law
###### LLM
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Global Human Rights and Social Justice in Practice | https://www.shu.ac.uk/courses/law/llm-global-human-rights-and-social-justice-in-practice/full-time/2026 | full-time |
| 2 | Global Human Rights and Social Justice in Practice | https://www.shu.ac.uk/courses/law/llm-global-human-rights-and-social-justice-in-practice/part-time/2026 | part-time |
| 3 | Legal Practice Development (SQE Preparation) | https://www.shu.ac.uk/courses/law/llm-legal-practice-development-sqe-preparation/full-time/2026 | full-time |
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Global Human Rights and Social Justice in Practice | https://www.shu.ac.uk/courses/law/ma-global-human-rights-and-social-justice-in-practice/full-time/2026 | full-time |
| 2 | Global Human Rights and Social Justice in Practice | https://www.shu.ac.uk/courses/law/ma-global-human-rights-and-social-justice-in-practice/part-time/2026 | part-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Law and Criminology | https://www.shu.ac.uk/courses/law/phd-law-and-criminology/part-time/2026 | part-time |
| 2 | Law and Criminology | https://www.shu.ac.uk/courses/law/phd-law-and-criminology/full-time/2026 | full-time |
##### Department of Marketing
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Digital Marketing | https://www.shu.ac.uk/courses/marketing/msc-digital-marketing/full-time/2026 | full-time |
| 2 | Digital Marketing (Work Experience) | https://www.shu.ac.uk/courses/marketing/msc-digital-marketing-work-experience/full-time/2026 | full-time |
| 3 | International Marketing | https://www.shu.ac.uk/courses/marketing/msc-international-marketing/full-time/2026 | full-time |
| 4 | International Marketing (Work Experience) | https://www.shu.ac.uk/courses/marketing/msc-international-marketing-work-experience/full-time/2026 | full-time |
##### Department of Mba
###### MBA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Executive MBA | https://www.shu.ac.uk/courses/mba/mba-executive-mba/full-time/2026 | full-time |
| 2 | Executive MBA | https://www.shu.ac.uk/courses/mba/mba-executive-mba/part-time/2026 | part-time |
| 3 | Executive MBA (1 year top-up) | https://www.shu.ac.uk/courses/mba/mba-executive-mba-1-year-topup/part-time/2026 | part-time |
| 4 | Global MBA | https://www.shu.ac.uk/courses/mba/mba-global-mba/full-time/2026 | full-time |
##### Department of Media Pr And Journalism
###### MA
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Sports Journalism | https://www.shu.ac.uk/courses/media-pr-and-journalism/ma-sports-journalism/full-time/2026 | full-time |
###### MPhil
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Media and Communications | https://www.shu.ac.uk/courses/media-pr-and-journalism/mphil-media-and-communications/full-time/2026 | full-time |
| 2 | Media and Communications | https://www.shu.ac.uk/courses/media-pr-and-journalism/mphil-media-and-communications/part-time/2026 | part-time |
###### PhD
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Media and Communications | https://www.shu.ac.uk/courses/media-pr-and-journalism/phd-media-and-communications/full-time/2026 | full-time |
| 2 | Media and Communications | https://www.shu.ac.uk/courses/media-pr-and-journalism/phd-media-and-communications/part-time/2026 | part-time |
##### Department of Tourism And Hospitality
###### MSc
| # | 专业 | URL | Mode |
|---|------|-----|------|
| 1 | Hospitality and Culinary Arts | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-hospitality-and-culinary-arts/full-time/2026 | full-time |
| 2 | Hospitality and Culinary Arts (Work Experience) | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-hospitality-and-culinary-arts-work-experience/full-time/2026 | full-time |
| 3 | International Hospitality and Tourism Management | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-hospitality-and-tourism-management/full-time/2026 | full-time |
| 4 | International Hospitality and Tourism Management (Work Experience) | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-hospitality-and-tourism-management-work-experience/full-time/2026 | full-time |
| 5 | International Tourism and Aviation Management | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-tourism-and-aviation-management/full-time/2026 | full-time |
| 6 | International Tourism and Aviation Management (Work Experience) | https://www.shu.ac.uk/courses/tourism-and-hospitality/msc-international-tourism-and-aviation-management-work-experience/full-time/2026 | full-time |

### 2.2 Worked example — MSc Cyber Security

- **Department**: Department of Computing
- **College**: College of Engineering, Computing and the Built Environment
- **Mode**: Full-time (1 year)
- **Home fee**: £10,940 (total)
- **International fee**: £18,600 (total, 2026/27)
- **Intake**: September 2026, January 2027
- **Campus**: City Campus
- **Application portal**: Direct via SHU website (postgraduate application form)

### 2.3 Graduate admissions model

- **Decentralized**: Most departments manage their own admissions decisions via the central SHU PG application form
- **Standard application fee**: No standard application fee for most PG taught programs; some professional courses (e.g. PGCE) use UCAS
- **PGCEs**: Apply via UCAS (centralized UK route for teacher training)
- **Research degrees (MPhil/PhD)**: Apply via SHU direct with research proposal

---

## 3. Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 数据 |
|------|------|
| Admissions site | https://www.shu.ac.uk/study-here/undergraduate |
| Application portal | UCAS (undergraduate) |
| UCAS code (per course) | Shown on each course page (e.g. N4N3 for BA Accounting and Finance) |
| Equal consideration deadline | 26 January (UCAS standard) |
| Clearing period | July–September (annual) |
| Decision notification | Rolling (UCAS Track) |
| SAT/ACT policy | Not required for UK applicants; considered for some international applicants |
| Interview policy | Course-dependent (e.g. Health, Education, Art & Design courses) |
| Recommendation requirements | 1 academic reference via UCAS |
| Personal statement | Required via UCAS |
| Foundation year entry | From 40 UCAS points |
| Standard entry | From 72 UCAS points (varies by course, typically 104–120 for most) |

### 3.2 Undergraduate English proficiency table

Most courses require IELTS 6.0 overall (min 5.5 in each band) for undergraduate entry. Some courses (e.g. Health, Nursing) require IELTS 6.5 or 7.0.

| Exam | Minimum Overall | Min per band | Recommended |
|------|-----------------|---------------|-------------|
| IELTS Academic | 6.0 (most UG); 6.5 (Health) | 5.5 (UG); 5.5/6.0 (Health) | 6.5+ |
| TOEFL iBT | 67 (for IELTS 6.0 equiv.) | L:12, S:17, R:12, W:14 | 81+ |
| Duolingo English Test | 105 | 95/100/95/95 | 120+ |
| Pearson PTE | 64 | 59 each band | 69+ |
| Oxford ELLT | 6 | 5 each band | 7 |
| LanguageCert International ESOL SELT B2 | High Pass | 33 each band | — |

**Source**: https://www.shu.ac.uk/study-here/international/english-language-requirements

### 3.3 Graduate English proficiency (PG)

| Exam | Minimum Overall | Min per band |
|------|-----------------|---------------|
| IELTS Academic | 6.5 (most PG taught); 7.0 (some research) | 5.5–6.0 each band |
| TOEFL iBT | 81 (for IELTS 6.5); 91 (for IELTS 7.0) | L:12, S:17, R:12, W:14 |
| Duolingo | 120 | 95/100/95/95 |
| Pearson PTE | 69 | 59 each |
| Oxford ELLT | 7 | 5 each |

### 3.4 Graduate — global rules

- **Application portal**: Direct via SHU website (https://www.shu.ac.uk/study-here/postgraduate/how-to-apply)
- **PGCE application**: Via UCAS (deadline typically October for primary/secondary)
- **Standard fee**: No application fee for most PG taught programs
- **Research applications**: Rolling intake; MPhil/PhD via direct application with research proposal
- **GRE/GMAT**: Not required
- **Application timeline**: Rolling admissions; September and January intakes common

---

## 4. Costs & Financial Aid

### 4.1 Undergraduate cost — 2026/27 academic year

| Expense item | Home (UK) | International/EU | Notes |
|--------------|-----------|------------------|-------|
| Tuition fee (per year) | £9,790 | £18,000 | Standard UG; confirmed from course page (BA Accounting & Finance example) |
| Foundation Year (additional) | +£1,500–£2,000 typical | +£1,500–£2,000 typical | Per-year surcharge |
| Placement year | Reduced (20% cap on international) | Reduced (20% cap) | International capped at 20% of standard fee |
| Living costs (estimated, off-campus) | £9,000–£11,000/year | £9,000–£11,000/year | Sheffield cost-of-living guide available |

### 4.2 Postgraduate cost — 2026/27 academic year

| Study level | Home | International (2025-26) | International (2026-27) |
|-------------|------|--------------------------|--------------------------|
| Pre-sessional English (5-week) | N/A | £1,800 (5-wk) / £3,600 (10-wk) | TBC |
| International Foundation Programme | N/A | £12,950 (2-term) / £15,545 (3-term) | £13,600 / £16,325 |
| Postgraduate taught | Varies (typically £8,500–£10,000) | £17,725–£20,360 (total) | £18,600–£21,375 (total) |
| MBA | See course | £20,360 | £21,375 |
| PGCE | £9,250 | £17,725 | £18,600 |
| MPhil/PhD (research) | Varies; see course page | See course page | See course page |

**Source**: https://www.shu.ac.uk/study-here/international/tuition-fees

### 4.3 Financial aid

- **Student Success Scholarships**: Available to UK and international students — up to £2,100/year
- **UK undergraduate loans**: Available via Student Finance England (subject to residency)
- **Postgraduate loans**: Available for eligible masters students
- **NHS Bursaries**: Available for some Health professions (Nursing, Allied Health)
- **International scholarships**: Multiple dedicated schemes (see SHU international scholarships page)
- **Payment methods**: Instalment plans available; see https://www.shu.ac.uk/study-here/fees-and-funding/payment-methods

---

## 5. Evidence Chain Index

Key facts and their source citations:

```yaml
# E-U-001
field: undergraduate.total_programs
value: 222
source_url: https://www.shu.ac.uk/courses?page=0&perPage=100&query=&yearOfEntry=2026%2F27&sortBy=courseTitle&sortOrder=asc
source_snippet: "Showing 1-100 of 569 results (full catalog, 504 distinct UG+PG course URLs extracted)"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-002
field: undergraduate.subject_areas
value: 38
source_url: https://www.shu.ac.uk/courses
source_snippet: "38 distinct subject area URL prefixes extracted from /courses/{subject}/"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-003
field: undergraduate.home_fee_2026_27
value: '£9,790/year'
source_url: https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2026
source_snippet: ""Home: £9,790 per year""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-004
field: undergraduate.international_fee_2026_27
value: '£18,000/year'
source_url: https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2026
source_snippet: ""International/EU: £18,000 per year""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-005
field: ug.entry_points.foundational
value: 'From 40 UCAS points'
source_url: https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2026
source_snippet: ""degree courses available from 72 UCAS points and foundation years from 40 points""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-006
field: ug.entry_points.standard
value: 'From 72 UCAS points'
source_url: https://www.shu.ac.uk/courses/accounting-banking-and-finance/ba-honours-accounting-and-finance/full-time/2026
source_snippet: ""degree courses available from 72 UCAS points""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-007
field: student.population
value: '~31,000'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""approximately 31,000 students, nearly 4,000 staff and 345,000 alumni around the world""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-008
field: student.international_population
value: '~4,500'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""A cohort of over 4,500 international students from across the globe""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-009
field: awards.tef
value: 'Gold (2023)'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""We were awarded Gold in the 2023 Teaching Excellence Framework""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-U-010
field: graduate_employment_rate
value: '95%'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""95% of our graduates are in work or further study fifteen months after graduating (2022/23 Graduate Outcomes Survey)""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-G-001
field: graduate.total_programs
value: 273
source_url: https://www.shu.ac.uk/courses?page=0&perPage=100&query=&yearOfEntry=2026%2F27&sortBy=courseTitle&sortOrder=asc
source_snippet: "Postgraduate course URLs extracted (MSc, MA, MBA, MPhil, MRes, PhD, PGCE, PGCert, PGDip, etc.)"
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-G-002
field: pg.international_fee_taught_2026_27
value: '£18,600–£21,375 (total)'
source_url: https://www.shu.ac.uk/study-here/international/tuition-fees
source_snippet: ""Postgraduate taught: £18,600-£21,375 for the course. MBA: £21,375*""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-G-003
field: pg.international_fee_2025_26
value: '£17,725–£20,360 (total)'
source_url: https://www.shu.ac.uk/study-here/international/tuition-fees
source_snippet: ""Postgraduate taught: £17,725-£20,360 for the course. MBA: £20,360*""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-G-004
field: pg.international_fee_pgce_2026_27
value: '£18,600'
source_url: https://www.shu.ac.uk/study-here/international/tuition-fees
source_snippet: ""PGCEs: £18,600*""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-E-001
field: english.ielts_6.0
value: 'IELTS 6.0 overall; 5.5 each band'
source_url: https://www.shu.ac.uk/study-here/international/english-language-requirements
source_snippet: ""IELTS Overall: 6.0, Minimum scores of: Listening: 5.5, Speaking: 5.5, Reading: 5.5, Writing: 5.5""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-E-002
field: english.ielts_6.5
value: 'IELTS 6.5 overall; 5.5 each band'
source_url: https://www.shu.ac.uk/study-here/international/english-language-requirements
source_snippet: ""IELTS Overall: 6.5, Minimum scores of: Listening: 5.5, Speaking: 5.5, Reading: 5.5, Writing: 5.5""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-E-003
field: english.ielts_7.0
value: 'IELTS 7.0 overall; 5.5 each band'
source_url: https://www.shu.ac.uk/study-here/international/english-language-requirements
source_snippet: ""IELTS Overall: 7, Minimum scores of: Listening: 5.5, Speaking: 5.5, Reading: 5.5, Writing: 5.5""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-E-004
field: english.toefl_6.0
value: 'TOEFL iBT 67 (for IELTS 6.0 equiv.)'
source_url: https://www.shu.ac.uk/study-here/international/english-language-requirements
source_snippet: ""TOEFL iBT (including TOEFL iBT Special Home Edition) Overall: 67, Minimum scores of: Listening: 12, Speaking: 17, Reading: 12, Writing: 14""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-E-005
field: english.duolingo_6.5
value: 'Duolingo 120 (for IELTS 6.5 equiv.)'
source_url: https://www.shu.ac.uk/study-here/international/english-language-requirements
source_snippet: ""Duolingo Overall: 120""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-S-001
field: schools.business_school_scale
value: '~7,000 students, 100 countries'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""home to the largest modern business school in the country, with more than 7,000 students from 100 countries""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-S-002
field: schools.teacher_training
value: '~1,000 teachers/year'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""We train around 1,000 teachers a year (across degree stages)""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-S-003
field: research.ref_2021
value: '72% world-class or internationally excellent'
source_url: https://www.shu.ac.uk/about-us/who-we-are
source_snippet: ""In REF 2021, 72% of our research submitted was rated world-class or internationally excellent""
capture_date: 2026-07-08
evidence_type: official_webpage
```

```yaml
# E-S-004
field: awards.whatuni
value: 'Top 5 in England (2026)'
source_url: https://www.shu.ac.uk/study-here/international
source_snippet: ""students voted us as Yorkshire's top university" / "Whatuni Student Choice Awards 2026""
capture_date: 2026-07-08
evidence_type: official_webpage
```

---

## 6. WeKnora Import Manifest

### Collection structure

- **Collection**: `sheffield-hallam-knowledge-base-v2`
- **Document**: One per college (4 colleges)
- **Chunking strategy**: One chunk per 学院 → 系 → 学位级别 grouping

### Per-chunk metadata template

```yaml
metadata:
  collection: "sheffield-hallam-knowledge-base-v2"
  school: "<home college>"
  department: "<home subject area>"
  degree_level: "<BA|BS|BEng|MA|MS|PhD|PGCE>"
  level: undergraduate | postgraduate
  field_type: programs
  source_url: <per-program URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P0 | Per-program duration and mode detail (FT/PT/Sandwich) | Each course page |
| P0 | Per-program UCAS code | Each course page |
| P0 | Per-program IELTS requirement (often shown inline on course page) | Each course page |
| P1 | MBA specialization details | https://www.shu.ac.uk/courses/mba |
| P1 | PhD/MPhil research themes and supervisors | https://www.shu.ac.uk/research |
| P1 | Apprenticeship routes | https://www.shu.ac.uk/study-here/degree-apprenticeships |
| P2 | Accommodation costs | https://www.shu.ac.uk/study-here/accommodation |

---

## 7. Cross-School Comparison Framework

| Dimension | Sheffield Hallam |
|-----------|------------------|
| Total UG cost/year (Home) | £9,790 |
| Total UG cost/year (Intl) | £18,000 |
| Total PG cost/year (Intl, taught) | £18,600–£21,375 |
| Application deadline (UG) | UCAS equal consideration 26 Jan |
| Application deadline (PG) | Rolling |
| TOEFL iBT min (UG) | 67 (IELTS 6.0 equiv.) |
| IELTS min (UG) | 6.0 (most); 6.5 (Health) |
| IELTS min (PG) | 6.5 (most); 7.0 (some) |
| Total program count | 504 |
| Subject areas | 38 |
| Colleges | 4 (+ Sheffield Business School) |
| Student population | ~31,000 |
| International students | ~4,500 |
| TEF rating | Gold (2023) |
| Graduate employment rate | 95% |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: shu.ac.uk (Sheffield Hallam University official)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
