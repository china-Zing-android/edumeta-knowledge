# Missouri University of Science and Technology Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

## 0. 院校总览 (Institution Overview)

Missouri University of Science and Technology (Missouri S&T) is a public STEM-focused research university in Rolla, Missouri, founded in 1870 as the Missouri School of Mines. It is one of four campuses of the University of Missouri System. Missouri S&T is classified as R2: Doctoral Universities — High Research Activity, and is accredited by the Higher Learning Commission (HLC).

**Source URL**: https://www.mst.edu/
**Source snippet**: "Missouri S&T — Missouri University of Science and Technology" (main gateway header); located in Rolla, MO 65409.

The university is organized around three primary academic colleges:
- **College of Arts, Sciences, and Education (CASE)** — arts, humanities, sciences, education, ROTC
- **College of Engineering and Computing (CEC)** — engineering (largest college), computer science, information technology
- **Kummer College** — business and management (formerly College of Business and Management Systems; renamed in 2021 after a $300M gift from the Kummer Family Foundation)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS / BA / BS-BA combined / Bachelor's Degree) | 38 |
| 本科辅修 (Minor) | 74 |
| 本科高级证书 (Certificate) | 20 |
| 研究生学位项目 (MS / MEng / MBA / MST / PhD / DEng / DSc / combined) | 85 |
| 研究生高级证书 (Certificate) | 143 |
| **学位项目总计 (UG + Grad)** | **360** |
| 学院 (Colleges) | 3 |
| 系/项目组 (Departments) | 27 (UG) + 25 (Grad) |

> **Source URLs**:
> - https://futurestudents.mst.edu/academic-programs/undergraduate-programs/ — UG list filter UI shows "132 Results"; 132 unique li.mst-program-entry items extracted.
> - https://futurestudents.mst.edu/academic-programs/graduate-programs/ — Grad list filter UI shows "228 Results"; 228 unique li.mst-program-entry items extracted.
> - Reconciliation: 132 + 228 = 360. UG: 38+74+20=132 ✓. Grad: 85+143=228 ✓.

### 0.2 学院 / 系层级结构

```
Missouri University of Science and Technology (Missouri S&T) [大学]
├── College of Arts, Sciences, and Education (CASE)           [学院]
│   ├── Arts, Languages, and Philosophy                       [系] (18 UG programs)
│   ├── Biological Sciences                                   [系] (4 UG + 2 Grad)
│   ├── Chemistry                                             [系] (4 UG + 2 Grad)
│   ├── Earth Sciences and Engineering                        [系] (7 UG + 28 Grad) — shared with Mining & Explosives Eng.
│   ├── Economics                                             [系] (7 UG; under Kummer at Grad level)
│   ├── Education                                             [系] (3 UG + 1 Grad)
│   ├── English and Technical Communication                   [系] (13 UG + 1 Grad)
│   ├── History and Political Science                         [系] (8 UG)
│   ├── Mathematics and Statistics                            [系] (4 UG + 8 Grad)
│   ├── Physics                                               [系] (2 UG + 2 Grad)
│   ├── Psychological Science                                 [系] (7 UG + 7 Grad)
│   ├── Army ROTC                                             [系] (1 UG minor: Adaptive Leadership)
│   └── Air Force ROTC                                        [系] (1 UG minor: Military Aerospace Studies)
├── College of Engineering and Computing (CEC)                [学院]
│   ├── Chemical and Biochemical Engineering                  [系] (2 UG + 6 Grad)
│   ├── Civil, Architectural and Environmental Engineering    [系] (6 UG + 20 Grad)
│   ├── Computer Science                                      [系] (3 UG + 12 Grad)
│   ├── Electrical and Computer Engineering                   [系] (7 UG + 14 Grad)
│   ├── Engineering Management and Systems Engineering        [系] (2 UG + 28 Grad) — ⚠ hosted in Kummer at grad level
│   ├── Materials Science and Engineering                     [系] (4 UG + 6 Grad)
│   ├── Mechanical and Aerospace Engineering                  [系] (4 UG + 26 Grad)
│   ├── Mining and Explosives Engineering                     [系] (6 UG + 18 Grad)
│   └── Nuclear Engineering and Radiation Science             [系] (2 UG + 4 Grad)
└── Kummer College (renamed 2021; formerly College of Business and Management Systems) [学院]
    ├── Jaggi School of Business                              [系] (13 UG + 27 Grad)
    ├── Economics                                             [系] (UG in CASE; Grad here: 5)
    └── Business and Information Technology (BIT)             [系] (2 Grad certificates)

Multi-college minors (4 UG): Global Studies, Latin American Studies for Technical Applications, Multiculturalism and Diversity, Pre-medicine.
```

> **Source URLs**: https://futurestudents.mst.edu/academic-programs/, https://case.mst.edu/, https://cec.mst.edu/, https://kummercollege.mst.edu/, https://jaggi.mst.edu/

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | official (本校) | 本项目数量 |
|---------|------|------|----------------|-----------|
| BS | Bachelor of Science | 本科 | Bachelor of Science | 29 |
| BS/BA | Bachelor of Science + Bachelor of Arts combined track | 本科 | Bachelor of Science, Bachelor of Arts | 6 |
| BA | Bachelor of Arts | 本科 | Bachelor of Arts | 1 |
| BS* | Bachelor (generic degree) | 本科 | Bachelor's Degree | 2 |
| Minor | Minor (辅修) | 本科 | Minor | 74 |
| Cert | Certificate (本科高级证书) | 本科 | Certificate | 20 |
| MS | Master of Science | 研究生 | Master of Science | 45 |
| MS+MST | MS + Master of Science in Teaching combined | 研究生 | Master of Science, Master of Science in Teaching | 1 |
| MEng | Master of Engineering | 研究生 | Master of Engineering | 3 |
| MBA | Master of Business Administration | 研究生 | MBA | 2 |
| MST | Master of Science in Teaching | 研究生 | Master of Science in Teaching | 2 |
| PhD | Doctor of Philosophy | 研究生 | Doctor of Philosophy | 24 |
| PhD/DEng | PhD + Doctor of Engineering combined | 研究生 | Doctor of Philosophy, Doctor of Engineering | 5 |
| DEng | Doctor of Engineering | 研究生 | Doctor of Engineering | 2 |
| DSc | Doctor of Science | 研究生 | Doctor of Science | 1 |
| Cert | Certificate (研究生高级证书) | 研究生 | Certificate | 143 |
| **Total** | | | | **360** |

> Canonical mapping (degree-taxonomy.md): BS → Bachelor of Science; BA → Bachelor of Arts; MS → Master of Science; MEng → Master of Engineering; MBA → Master of Business Administration; PhD → Doctor of Philosophy; DEng → Doctor of Engineering; DSc → Doctor of Science. "BS/BA" combined tracks mean the department offers both BS and BA variants of the same program name.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS | BA | BS/BA | MS | MEng | MBA | MST/MS+MST | PhD | DEng | DSc | PhD/DEng | Minor | Cert | 合计 |
|------------|----|----|------|----|------|-----|-----------|-----|------|-----|---------|-------|------|------|
| College of Arts, Sciences, and Education | 6 | 1 | 6 | 6 | 0 | 0 | 3 | 4 | 0 | 1 | 0 | 38 | 25 | **90** |
| College of Engineering and Computing | 21 | 0 | 0 | 31 | 3 | 0 | 0 | 16 | 2 | 0 | 5 | 17 | 89 | **184** |
| Kummer College | 4 | 0 | 0 | 8 | 0 | 2 | 0 | 4 | 0 | 0 | 0 | 15 | 49 | **82** |
| Multi-College (Cross-listed) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | **4** |
| **合计** | 31 | 1 | 6 | 45 | 3 | 2 | 3 | 24 | 2 | 1 | 5 | 74 | 163 | **360** |

> Reconciliation: row totals = 360 ✓; column totals = 360 ✓; equals rule-1 total (132 UG + 228 Grad = 360).

---

## 1. Undergraduate Education

### 1.1 College/school architecture

Missouri S&T's undergraduate programs are housed in three colleges: CASE (arts, sciences, education, ROTC), CEC (engineering and computing — the largest by enrollment), and Kummer College (business and economics). Several minors are cross-listed across multiple colleges. See section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts, Sciences, and Education

##### Department: Army ROTC

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Adaptive Leadership | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/militaryscience/#minortext |

##### Department: English and Technical Communication

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | English and Technical Communication | https://english.mst.edu/academicprograms/bachelorsdegreeinetc/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |
| 2 | Communication Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/speechandmediastudies/#minorstext |
| 3 | Creative Writing | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |
| 4 | Game Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/ |
| 5 | Leadership Communication | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/speechandmediastudies/#minorstext |
| 6 | Linguistics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/ |
| 7 | Literature | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |
| 8 | Literature and Film | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |
| 9 | Social Media in Industry | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/ |
| 10 | Technical Communication | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |
| 11 | Writing | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Technical Writing | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/englishandtechnicalcommunication/#certificatestext |

##### Department: Mathematics and Statistics

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://math.mst.edu/academic-programs/undergraduateprograms/appliedmath/ |
| 2 | Data Science | https://datascience.mst.edu/bachelorsdegree/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/mathematics/#minortext |
| 2 | Mathematics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/mathematics/#minortext |

##### Department: Arts, Languages, and Philosophy

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://alp.mst.edu/philosophy/ |

###### BA — Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | Multidisciplinary Studies | https://alp.mst.edu/multidisciplinarystudies/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Art | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/art/#minortext |
| 2 | Ethics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#minorstext |
| 3 | Film and Literature | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/art/#minortext |
| 4 | French | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/foreignlanguages/#minorstext |
| 5 | German | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/foreignlanguages/#minorstext |
| 6 | Music | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/music/#minorstext |
| 7 | Philosophy | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#minorstext |
| 8 | Philosophy of Technology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#minorstext |
| 9 | Russian | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/foreignlanguages/#minorstext |
| 10 | Spanish | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/foreignlanguages/#minorstext |
| 11 | Studio Art | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/art/#minortext |
| 12 | Theatre | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/theatre/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Intercultural Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/multidisciplinarystudies/#certificatestext |
| 2 | Logic and the Philosophical Foundations of Stem | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#certificatestext |
| 3 | Professional Ethics and Moral Reasoning | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#certificatestext |
| 4 | Technology, Philosophy, and Ethical Futures | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/philosophy/#certificatestext |

##### Department: Chemistry

###### BS/BA — Bachelor of Science, Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://chem.mst.edu/academic-programs/undergraduate-programs/bsbiochemistry/ |
| 2 | Chemistry | https://chem.mst.edu/academic-programs/undergraduate-programs/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/chemistry/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Medicinal Chemistry | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/chemistry/#certificatestext |

##### Department: Biological Sciences

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/environmentalsciences/ |

###### BS/BA — Bachelor of Science, Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://biosci.mst.edu/academicprograms/undergraduate-degrees/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/biologicalsciences/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Bioinnovation | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/biologicalsciences/#certificatestext |

##### Department: Psychological Science

###### BS/BA — Bachelor of Science, Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://psych.mst.edu/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Cognitive Neuroscience | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |
| 2 | Human Factors | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |
| 3 | Industrial/Organizational | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |
| 4 | Psychology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |
| 5 | Psychology for Health Care | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |
| 6 | Psychology of Leadership | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/psychology/#minorstext |

##### Department: Education

###### BS/BA — Bachelor of Science, Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://teachereducation.mst.edu/ |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Education of Young Children | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/education/#certificatestext |
| 2 | Teaching and Learning | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/education/#certificatestext |

##### Department: History and Political Science

###### BS/BA — Bachelor of Science, Bachelor of Arts

| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://history.mst.edu/undergraduateprograms/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/history/#minorstext |
| 2 | Political Science | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/politicalscience/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Medieval and Renaissance Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/history/#certificatestext |
| 2 | Military and Security Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/history/#certificatestext |
| 3 | Pre-law | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/prelaw/#minortext |
| 4 | Science, Technology, and Society | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/history/#certificatestext |
| 5 | War and Society | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/history/#certificatestext |

##### Department: Air Force ROTC

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Military Aerospace Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/aerospace-studies/#minortext |

##### Department: Physics

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://physics.mst.edu/academicprograms/undergraduateprograms/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/physics/#minorstext |

#### College of Engineering and Computing

##### Department: Mechanical and Aerospace Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://mae.mst.edu/academic-programs/bachelors-degree-in-aerospace-engineering/ |
| 2 | Mechanical Engineering | https://mae.mst.edu/academic-programs/bachelors-degree-in-mechanical-engineering/ |
| 3 | Mechanical Engineering | https://www.missouristate.edu/EGR/Mechanical/default.htm |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/aerospaceengineering/#minorstext |

##### Department: Civil, Architectural and Environmental Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Engineering | https://care.mst.edu/academic-programs/architecturalengineering/undergraduate-degree/ |
| 2 | Civil Engineering | https://care.mst.edu/academic-programs/civil-engineering/undergraduate-degree/ |
| 3 | Civil Engineering | https://www.missouristate.edu/EGR/Civil/default.htm |
| 4 | Environmental Engineering | https://care.mst.edu/academic-programs/environmentalengineering/bachelorsdegreeinenvironmentalengineering/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Engineering and Management | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/civilengineering/ |
| 2 | Sustainability | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/sustainability/#text |

##### Department: Electrical and Computer Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://ece.mst.edu/academic-programs/computer-engineering/undergraduate-degree/ |
| 2 | Electrical Engineering | https://www.missouristate.edu/EGR/Electrical/default.htm |
| 3 | Electrical Engineering | https://ece.mst.edu/academic-programs/electrical-engineering/undergraduate-degree/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Automation Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/electricalengineering/#minorstext |
| 2 | Computer Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/computerengineering/#minorstext |
| 3 | Electrical Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/electricalengineering/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Automation Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/electricalengineering/#certificatestext |

##### Department: Computer Science

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://cs.mst.edu/undergraduate-degree/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Bioinformatics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/bioinformaticsminor/#text |
| 2 | Computer Science | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/computerscience/#minorstext |

##### Department: Chemical and Biochemical Engineering

###### BS — Bachelor's Degree

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://chbe.mst.edu/academicprograms/bme/ |

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://chbe.mst.edu/academicprograms/bachelorsdegreeinchemicalengineering/ |

##### Department: Materials Science and Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Ceramic Engineering | https://mse.mst.edu/academic-programs/bachelorsdegreeinceramicengineering/ |
| 2 | Metallurgical Engineering | https://mse.mst.edu/academic-programs/bachelorsdegreeinmetallurgicalengineering/ |

###### BS — Bachelor's Degree

| # | 专业 | URL |
|---|------|-----|
| 1 | Semiconductor Engineering | https://mse.mst.edu/academic-programs/bachelorsdegreeinsemiconductorengineering/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/materialsscienceandengineering/#minortext |

##### Department: Earth Sciences and Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Geological Engineering | https://ge.mst.edu/gee/undergraduate/ |
| 2 | Geology and Geophysics | https://gs.mst.edu/ggprogram/undergraduate/ |
| 3 | Petroleum Engineering | https://petroleum.mst.edu/academic-programs/undergraduate-degree/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Computational Earth Sciences | https://ese.mst.edu/academic-programs/geology-and-geophysics/ |
| 2 | Geological Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/geologicalengineering/#minortext |
| 3 | Geology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/geologyandgeophysics/#minorstext |
| 4 | Petroleum Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/petroleumengineering/#minorstext |

##### Department: Mining and Explosives Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Mining Engineering | https://mining.mst.edu/academicprograms/ugraddegree/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Explosives Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/explosivesengineering/#minorstext |
| 2 | Mineral Process Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/miningengineering/#minorstext |
| 3 | Mining Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/miningengineering/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Explosives Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/explosivesengineering/#certificatestext |
| 2 | Explosives Technology Certificate | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/explosivesengineering/#certificatestext |

##### Department: Nuclear Engineering and Radiation Science

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://nuclear.mst.edu/academic-programs/bachelors-degree-in-nuclear-engineering/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/nuclearengineering/#minorstext |

#### Kummer College

##### Department: Jaggi School of Business

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Management Systems | https://bit.mst.edu/business-management/undergraduate/ |
| 2 | Information Science and Technology | https://bit.mst.edu/information-science-technology/undergraduate/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Artificial Intelligence and Machine Learning in Business | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/ |
| 2 | Business | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/businessandmanagementsystems/#testtext |
| 3 | Business Analytics and Data Science | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/#minortext |
| 4 | Cybersecurity Management and Information Assurance | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/ |
| 5 | Digital Supply Chain Management | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/#minortext |
| 6 | Enterprise Resource Planning | https://catalog.mst.edu/undergraduate/courselist/erp/#text |
| 7 | Entrepreneurship | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/businessandmanagementsystems/#testtext |
| 8 | Financial Technology, Analytics and Transformation | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/ |
| 9 | Information Science and Technology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/informationscienceandtechnology/#minortext |
| 10 | Management | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/businessandmanagementsystems/#testtext |
| 11 | Marketing | https://catalog.mst.edu/undergraduate/courselist/mkt/ |

##### Department: Economics

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://econ.mst.edu/academic-programs/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Energy Technology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/economics/ |
| 2 | Finance | https://catalog.mst.edu/undergraduate/courselist/finance/ |
| 3 | Global Sustainable Economics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/economics/#minorstext |

###### Cert — Certificate

| # | 专业 | URL |
|---|------|-----|
| 1 | Decision Data Analytics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/economics/#certificatestext |
| 2 | Energy Economics | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/economics/#certificatestext |
| 3 | Financial Economics and Technology | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/economics/#certificatestext |

##### Department: Engineering Management and Systems Engineering

###### BS — Bachelor of Science

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Management | https://emse.mst.edu/academicprograms/engineeringmanagement/undergraduate/ |

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Management | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/engineeringmanagement/#minorstext |

#### College of Arts, Sciences, and Education | College of Engineering and Computing | Kummer College

##### Department: Arts, Languages, and Philosophy | Engineering Management and Systems Engineering | Chemical and Biochemical Engineering | Nuclear Engineering and Radiation Science | Civil, Architectural and Environmental Engineering | Biological Sciences | Chemistry

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Global Studies | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/globalstudies/#text |

#### College of Arts, Sciences, and Education | College of Engineering and Computing

##### Department: Arts, Languages, and Philosophy | Chemical and Biochemical Engineering | History and Political Science | English and Technical Communication | Earth Sciences and Engineering

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Latin American Studies for Technical Applications | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/latinamericanstudiesminor/#text |

##### Department: Arts, Languages, and Philosophy | History and Political Science | English and Technical Communication | Psychological Science

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Multiculturalism and Diversity | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/multiculturalismanddiversity/#text |

##### Department: Biological Sciences | Chemistry | Physics | Mathematics and Statistics

###### Minor — Minor

| # | 专业 | URL |
|---|------|-----|
| 1 | Pre-medicine | https://catalog.mst.edu/undergraduate/degreeprogramsandcourses/prehealthprofessions/#minortext |

> UG program total: 132 (must equal 132).

### 1.3 Interdisciplinary / cross-college undergraduate programs

The following 4 minors are cross-listed across multiple colleges and therefore not assignable to a single home school:

| # | Minor | Listing |
|---|-------|---------|
| 1 | Global Studies | CASE + CEC + Kummer |
| 2 | Latin American Studies for Technical Applications | CASE + CEC |
| 3 | Multiculturalism and Diversity | CASE + CEC |
| 4 | Pre-medicine | CASE (Bio Sci, Chem, Physics, Math) |

### 1.4 General / Institute-wide requirements

Missouri S&T requires the following for admission as a freshman (minimum 17 units of college-prep high school coursework):

- English: 4 units (composition emphasis)
- Mathematics: 4 units (Algebra I and higher)
- Social Studies: 3 units
- Science: 3 units (one with lab)
- Fine Arts: 1 unit
- Foreign Language: 2 units (same language)

**Source URL**: https://futurestudents.mst.edu/admissions/first-timefreshmen/
**Snippet**: "Students planning to attend Missouri S&T should follow a college preparatory curriculum completing at least 17 units of credit."

### 1.5 Course-ID → Major quick-lookup

Missouri S&T does NOT use a numbered course-ID system (unlike MIT or Stanford). Each program is identified by its full name (e.g., "Aerospace Engineering (BS)").

---

## 2. Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

Missouri S&T graduate programs span 3 colleges and 25 department/program-area combinations, comprising 85 degree programs (MS, MEng, MBA, MST, PhD, DEng, DSc, and combined) and 143 graduate certificates.

#### College of Arts, Sciences, and Education

##### Department / Program Area: Mathematics and Statistics

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://math.mst.edu/academic-programs/graduateprogram/ |
| 2 | Data Science | https://datascience.mst.edu/mastersdegree/ |

###### MS+MST — Master of Science in Teaching

| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://math.mst.edu/academic-programs/graduateprogram/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Mathematics | https://math.mst.edu/academic-programs/graduateprogram/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Actuarial Science | https://catalog.mst.edu/graduate/graduatedegreeprograms/mathematicsandstatistics/#certificatestext |
| 2 | Financial Mathematics | https://catalog.mst.edu/graduate/graduatedegreeprograms/mathematicsandstatistics/#certificatestext |
| 3 | Statistics | https://online.mst.edu/onlineprograms/online-graduate-certificates/statistics/ |
| 4 | Statistics | https://catalog.mst.edu/graduate/graduatedegreeprograms/mathematicsandstatistics/#certificatestext |

##### Department / Program Area: Psychological Science

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Industrial-Organizational Psychology | https://online.mst.edu/onlineprograms/online-graduate-degrees/industrial-organizational-psychology/ |
| 2 | Industrial-Organizational Psychology | https://psych.mst.edu/academic-programs/graduate/ |

###### DSc — Doctor of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Psychology | https://psych.mst.edu/academic-programs/phdinappliedpsychology/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Workplace Psychology | https://online.mst.edu/onlineprograms/online-graduate-certificates/applied-workplace-psychology/ |
| 2 | Applied Workplace Psychology | https://catalog.mst.edu/graduate/graduatedegreeprograms/psychology#certificatestext |
| 3 | Human Factors Psychology | https://catalog.mst.edu/graduate/graduatedegreeprograms/psychology/#certificatestext |
| 4 | Human Factors Psychology | https://catalog.mst.edu/graduate/graduatedegreeprograms/psychology/#certificatestext |

##### Department / Program Area: Biological Sciences

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://biosci.mst.edu/academicprograms/mastersdegreeinbiologicalsciences/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://biosci.mst.edu/academicprograms/phdinbiologicalsciences/ |

##### Department / Program Area: Chemistry

###### MS+MST — Master of Science, Master of Science in Teaching

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://chem.mst.edu/academic-programs/graduate-programs/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://chem.mst.edu/academic-programs/graduate-programs/ |

##### Department / Program Area: Physics

###### MS+MST — Master of Science in Teaching

| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://physics.mst.edu/academicprograms/graduatedegreeprograms/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Physics | https://physics.mst.edu/academicprograms/graduatedegreeprograms/ |

##### Department / Program Area: Business and Information Technology

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Communication | https://online.mst.edu/onlineprograms/online-graduate-certificates/professional-communication/ |
| 2 | Professional Communication | https://catalog.mst.edu/graduate/graduatedegreeprograms/technicalcommunication/#certificatestext |

##### Department / Program Area: Education

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Teacher Leadership | https://online.mst.edu/onlineprograms/online-graduate-certificates/teacher-leadership/ |

##### Department / Program Area: English and Technical Communication

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Technical Communication | https://online.mst.edu/onlineprograms/online-graduate-degrees/technical-communication/ |

#### College of Engineering and Computing

##### Department / Program Area: Materials Science and Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Ceramic Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |
| 2 | Materials Science and Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Ceramic Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |
| 2 | Materials Science and Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Engineering Materials | https://online.mst.edu/onlineprograms/online-graduate-certificates/advanced-engineering-materials/ |
| 2 | Materials for Extreme Environments | https://online.mst.edu/onlineprograms/online-graduate-certificates/materials-extreme-environments/ |

##### Department / Program Area: Civil, Architectural and Environmental Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/civil-engineering/ |
| 2 | Civil Engineering | https://care.mst.edu/academic-programs/civil-engineering/graduatedegreesincivilengineering/ |
| 3 | Environmental Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/environmental-engineering/ |
| 4 | Environmental Engineering | https://care.mst.edu/academic-programs/environmentalengineering/masters-degree-in-environmental-engineering/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://care.mst.edu/academic-programs/civil-engineering/graduatedegreesincivilengineering/ |

###### DEng — Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/civil-engineering/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Materials for Sustainable Infrastructure | https://online.mst.edu/onlineprograms/online-graduate-certificates/advanced-materials-for-sustainable-infrastructure/ |
| 2 | Advanced Materials for Sustainable Infrastructure | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 3 | Building Systems Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/building-systems-engineering/ |
| 4 | Building Systems Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 5 | Contemporary Structural Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/contemporary-structural-engineering/ |
| 6 | Contemporary Structural Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 7 | Geoenvironmental Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/geoenvironmental-engineering/ |
| 8 | Geoenvironmental Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 9 | Geotechnical Earthquake Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/geotechnical-earthquake-engineering/ |
| 10 | Geotechnical Earthquake Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 11 | Infrastructure Renewal | https://online.mst.edu/onlineprograms/online-graduate-certificates/infrastructure-renewal/ |
| 12 | Infrastructure Renewal | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |
| 13 | Surface Water Resources | https://online.mst.edu/onlineprograms/online-graduate-certificates/surface-water-resources/ |
| 14 | Surface Water Resources | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |

##### Department / Program Area: Mechanical and Aerospace Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/aerospace-engineering/ |
| 2 | Aerospace Engineering | https://mae.mst.edu/academic-programs/#graduate-programs |
| 3 | Manufacturing Engineering | https://mae.mst.edu/academic-programs/#graduate-programs |
| 4 | Mechanical Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/mechanical-engineering/ |
| 5 | Mechanical Engineering | https://mae.mst.edu/academic-programs/#graduate-programs |
| 6 | Metallurgical Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |

###### MEng — Master of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Manufacturing Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/manufacturing-engineering/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/aerospace-engineering/ |
| 2 | Aerospace Engineering | https://mae.mst.edu/academic-programs/#graduate-programs |
| 3 | Mechanical Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/mechanical-engineering/ |
| 4 | Mechanical Engineering | https://mae.mst.edu/academic-programs/#graduate-programs |
| 5 | Metallurgical Engineering | https://mse.mst.edu/academic-programs/#graduate-programs |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | CAD/CAM and Rapid Product Realization | https://online.mst.edu/onlineprograms/online-graduate-certificates/cad-cam-rapid-product-realization/ |
| 2 | CAD/CAM and Rapid Product Realization | https://catalog.mst.edu/graduate/graduatedegreeprograms/manufacturingengineering/#certificatestext |
| 3 | Composite Materials and Structures | https://online.mst.edu/onlineprograms/online-graduate-certificates/composite-materials-structures/ |
| 4 | Composite Materials and Structures | https://catalog.mst.edu/graduate/graduatedegreeprograms/aerospaceengineering/#certificatestext |
| 5 | Control Systems | https://online.mst.edu/onlineprograms/online-graduate-certificates/control-systems/ |
| 6 | Control Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/mechanicalengineering/#certificatestext |
| 7 | Energy Conversion and Transport | https://online.mst.edu/onlineprograms/online-graduate-certificates/energy-conversion-transport/ |
| 8 | Energy Conversion and Transport | https://catalog.mst.edu/graduate/graduatedegreeprograms/aerospaceengineering/#certificatestext |
| 9 | Engineering Mechanics | https://online.mst.edu/onlineprograms/online-graduate-certificates/engineering-mechanics/ |
| 10 | Engineering Mechanics | https://catalog.mst.edu/graduate/graduatedegreeprograms/mechanicalengineering/#certificatestext |
| 11 | Manufacturing Automation | https://online.mst.edu/onlineprograms/online-graduate-certificates/manufacturing-automation/ |
| 12 | Manufacturing Automation | https://catalog.mst.edu/graduate/graduatedegreeprograms/mechanicalengineering/#certificatestext |
| 13 | Manufacturing Systems | https://online.mst.edu/onlineprograms/online-graduate-certificates/manufacturing-systems/ |
| 14 | Manufacturing Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/manufacturingengineering/#certificatestext |

##### Department / Program Area: Computer Science

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Artificial Intelligence | https://cs.mst.edu/graduate-degrees/masterofscienceinappliedai/ |
| 2 | Computer Science | https://cs.mst.edu/graduate-degrees/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://cs.mst.edu/graduate-degrees/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Big Data Management and Analytics | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 2 | Big Data Management and Security | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 3 | Cyber Security | https://online.mst.edu/onlineprograms/online-graduate-certificates/cyber-security/ |
| 4 | Cyber Security | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 5 | Information Systems and Cloud Computing | https://online.mst.edu/onlineprograms/online-graduate-certificates/information-systems-and-cloud-computing/ |
| 6 | Information Systems and Cloud Computing | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 7 | Software Design and Development | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 8 | Systems and Software Architecture | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |
| 9 | Wireless Networks and Mobile Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |

##### Department / Program Area: Electrical and Computer Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/computer-engineering/ |
| 2 | Computer Engineering | https://ece.mst.edu/academic-programs/computer-engineering/graduate-degrees-certificates/ |
| 3 | Electrical Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/electrical-engineering/ |
| 4 | Electrical Engineering | https://ece.mst.edu/academic-programs/electrical-engineering/graduate-degrees-certificates/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/computer-engineering/ |
| 2 | Computer Engineering | https://ece.mst.edu/academic-programs/computer-engineering/graduate-degrees-certificates/ |
| 3 | Electrical Engineering | https://ece.mst.edu/academic-programs/electrical-engineering/graduate-degrees-certificates/ |

###### DEng — Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Electrical Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/electrical-engineering/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Automation Engineering and PLC | https://online.mst.edu/onlineprograms/online-graduate-certificates/automation-engineering-plc/ |
| 2 | Automation Engineering and PLC | https://catalog.mst.edu/graduate/graduatedegreeprograms/electricalengineering/#certificatestext |
| 3 | Electric Machine and Drives | https://online.mst.edu/onlineprograms/online-graduate-certificates/electric-machines-drives/ |
| 4 | Electric Machine and Drives | https://catalog.mst.edu/graduate/graduatedegreeprograms/electricalengineering/#certificatestext |
| 5 | Electrical Power Systems Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/electric-power-systems-engineering/ |
| 6 | Electrical Power Systems Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/electricalengineering/#certificatestext |

##### Department / Program Area: Chemical and Biochemical Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://chbe.mst.edu/academicprograms/mastersdegreeinchemicalengineering/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Bioengineering | https://chbe.mst.edu/academicprograms/phd-bioeng/ |

###### PhD/DEng — Doctor of Philosophy, Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering | https://chbe.mst.edu/academicprograms/phdinchemicalengineering/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Carbon Management Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/chemicalandbiochemicalengineering/#certificatestext |
| 2 | Chemical Process Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/chemical-process-engineering/ |
| 3 | Chemical Process Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/chemicalandbiochemicalengineering/#certificatestext |

##### Department / Program Area: Engineering Management and Systems Engineering | Computer Science

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Intelligence | https://online.mst.edu/onlineprograms/online-graduate-certificates/computational-intelligence/ |
| 2 | Computational Intelligence | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerscience/#certificatestext |

##### Department / Program Area: Engineering Management and Systems Engineering | Electrical and Computer Engineering

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Cyber Physical Systems | https://online.mst.edu/onlineprograms/online-graduate-certificates/network-centric-systems/ |
| 2 | Cyber Physical Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/computerengineering/#certificatestext |

##### Department / Program Area: Mining and Explosives Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Explosives Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/explosives-engineering/ |
| 2 | Explosives Engineering | https://mee.mst.edu/degrees/ |
| 3 | Explosives Technology | https://online.mst.edu/onlineprograms/online-graduate-degrees/explosives-technology/ |
| 4 | Mining Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/mining-engineering/ |
| 5 | Mining Engineering | https://mee.mst.edu/degrees/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Explosives Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/explosives-engineering/ |
| 2 | Explosives Engineering | https://mee.mst.edu/degrees/ |

###### PhD/DEng — Doctor of Philosophy, Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Mining Engineering | https://mee.mst.edu/degrees/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Explosives Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/explosives-engineering-certificate/ |
| 2 | Explosives Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/explosivesengineering#certificatestext |
| 3 | Explosives Technology | https://online.mst.edu/onlineprograms/online-graduate-certificates/explosives-technology_certificate/ |
| 4 | Explosives Technology | https://catalog.mst.edu/graduate/graduatedegreeprograms/explosivesengineering#certificatestext |
| 5 | Mining Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/mining-engineering/ |
| 6 | Mining Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/miningengineering/#certificatestext |
| 7 | Mining Project Evaluation | https://online.mst.edu/onlineprograms/online-graduate-certificates/mining-project-evaluation/ |
| 8 | Mining Project Evaluation | https://catalog.mst.edu/graduate/graduatedegreeprograms/miningengineering/#certificatestext |
| 9 | Sustainability in Mining | https://catalog.mst.edu/graduate/graduatedegreeprograms/miningengineering/#certificatestext |
| 10 | Sustainability in Mining | https://online.mst.edu/onlineprograms/online-graduate-certificates/sustainability-in-mining/ |

##### Department / Program Area: Earth Sciences and Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Geological Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/geologicalengineering/ |
| 2 | Geological Engineering | http://ge.mst.edu/gee/graduate/ |
| 3 | Geology and Geophysics | http://gs.mst.edu/ggprogram/graduate/ |
| 4 | Geospatial Engineering | https://ese.mst.edu/academic-programs/geospatial-engineering/ |
| 5 | Geospatial Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/geospatial-engineering/ |
| 6 | Petroleum Engineering | https://petroleum.mst.edu/peprogram/graduate/ |

###### MEng — Master of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Geotechnics | https://online.mst.edu/onlineprograms/online-graduate-degrees/geotechnics/ |
| 2 | Geotechnics | http://gtech.mst.edu/certificate/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Geology and Geophysics | http://gs.mst.edu/ggprogram/graduate/ |

###### PhD/DEng — Doctor of Philosophy, Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Geological Engineering | http://ge.mst.edu/gee/graduate/ |
| 2 | Petroleum Engineering | https://petroleum.mst.edu/peprogram/graduate/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Geoanalytics and Geointelligence | https://online.mst.edu/onlineprograms/online-graduate-certificates/geoanalytics-and-geointelligence/ |
| 2 | Geoanalytics and Geointelligence | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |
| 3 | Geoenvironmental Science and Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/geoenvironmental-engineering/ |
| 4 | Geoenvironmental Science and Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |
| 5 | Geologic Hazards | https://online.mst.edu/onlineprograms/online-graduate-certificates/geologic-hazards/ |
| 6 | Geologic Hazards | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |
| 7 | Geophysics | https://online.mst.edu/onlineprograms/online-graduate-certificates/geophysics/ |
| 8 | Geophysics | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologyandgeophysics/#certificatestext |
| 9 | Geotechnics | https://online.mst.edu/onlineprograms/online-graduate-certificates/geotechnics/ |
| 10 | Geotechnics | https://catalog.mst.edu/graduate/graduatedegreeprograms/geotechnics/#certificatestext |
| 11 | Military Geological Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |
| 12 | Petroleum Systems | https://online.mst.edu/onlineprograms/online-graduate-certificates/petroleum-systems/ |
| 13 | Petroleum Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologyandgeophysics/#certificatestext |
| 14 | Space Resources | https://online.mst.edu/onlineprograms/online-graduate-certificates/space-resources/ |
| 15 | Space Resources | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |
| 16 | Subsurface Water Resources | https://online.mst.edu/onlineprograms/online-graduate-certificates/subsurface-water-resources/ |
| 17 | Subsurface Water Resources | https://catalog.mst.edu/graduate/graduatedegreeprograms/geologicalengineering/#certificatestext |

##### Department / Program Area: Mining and Explosives Engineering | Engineering Management and Systems Engineering

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Mine Reclamation | https://online.mst.edu/onlineprograms/online-graduate-certificates/mine-reclamation/ |
| 2 | Mine Reclamation | https://catalog.mst.edu/graduate/graduatedegreeprograms/miningengineering/#certificatestext |

##### Department / Program Area: Nuclear Engineering and Radiation Science

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://nuclear.mst.edu/academic-programs/masters-degree-in-nuclear-engineering/ |

###### PhD/DEng — Doctor of Philosophy, Doctor of Engineering

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Engineering | https://nuclear.mst.edu/academic-programs/masters-degree-in-nuclear-engineering/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Nuclear Nonproliferation | https://online.mst.edu/onlineprograms/online-graduate-certificates/nuclear-nonproliferation/ |
| 2 | Nuclear Nonproliferation | https://catalog.mst.edu/graduate/graduatedegreeprograms/nuclearengineering/#certificatestext |

##### Department / Program Area: Engineering Management and Systems Engineering | Civil, Architectural and Environmental Engineering

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Project Engineering and Construction Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/civilarchitecturalandenvironmentalengineering/#certificatestext |

##### Department / Program Area: Engineering Management and Systems Engineering | Chemical and Biochemical Engineering

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Safety Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/safety-engineering/ |
| 2 | Safety Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/chemicalandbiochemicalengineering/#certificatestext |

#### Kummer College

##### Department / Program Area: Jaggi School of Business

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Information Science and Technology | https://online.mst.edu/onlineprograms/online-graduate-degrees/information-science-technology/ |
| 2 | Information Science and Technology | http://bit.mst.edu/information-science-technology/graduate/ |

###### MBA — MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | https://online.mst.edu/onlineprograms/online-graduate-degrees/business_administration/ |
| 2 | Business Administration | http://bit.mst.edu/business-management/mba-program/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | AI, Machine Learning and Automation in Business | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 2 | AI, Machine Learning and Automation in Business | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 3 | Business Analytics and Data Science | https://online.mst.edu/onlineprograms/online-graduate-certificates/business-analytics-data-science/ |
| 4 | Business Analytics and Data Science | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 5 | Business Intelligence | https://online.mst.edu/onlineprograms/online-graduate-certificates/business-intelligence/ |
| 6 | Business Intelligence | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 7 | Business Project Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/business-project-management/ |
| 8 | Business Project Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/businessadministration/#certificatestext |
| 9 | Cybersecurity and Information Assurance Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 10 | Digital Supply Chain Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/digital-supply-chain-management/ |
| 11 | Digital Supply Chain Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 12 | Enterprise Resource Planning | https://online.mst.edu/onlineprograms/online-graduate-certificates/enterprise-resource-planning/ |
| 13 | Enterprise Resource Planning | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 14 | Entrepreneurship and Technological Innovation | https://online.mst.edu/onlineprograms/online-graduate-certificates/entrepreneurship-and-technological-innovation/ |
| 15 | Entrepreneurship and Technological Innovation | https://catalog.mst.edu/graduate/graduatedegreeprograms/businessadministration/#certificatestext |
| 16 | Finance | https://online.mst.edu/onlineprograms/online-graduate-certificates/finance/ |
| 17 | Finance | https://catalog.mst.edu/graduate/graduatedegreeprograms/businessadministration/#certificatestext |
| 18 | Financial Technology | https://online.mst.edu/onlineprograms/online-graduate-certificates/financial-technology/ |
| 19 | Financial Technology | https://catalog.mst.edu/graduate/graduatedegreeprograms/businessadministration/#certificatestext |
| 20 | Information System Project Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/information-systems-project-management/ |
| 21 | Information System Project Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/informationscienceandtechnology/#certificatestext |
| 22 | Management and Leadership | https://online.mst.edu/onlineprograms/online-graduate-certificates/management-and-leadership/ |
| 23 | Management and Leadership | https://catalog.mst.edu/graduate/graduatedegreeprograms/businessadministration/#certificatestext |

##### Department / Program Area: Economics

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Economics and Innovation | https://econ.mst.edu/mei/ |
| 2 | Economics and Innovation | https://econ.mst.edu/mei/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Energy Economics and Global Sustainability | https://online.mst.edu/onlineprograms/online-graduate-certificates/energyeconomicsandglobalsustainability/ |
| 2 | Management for Sustainable Business | https://catalog.mst.edu/graduate/graduatedegreeprograms/economics/#certificatestext |
| 3 | Value-driven Innovation | https://online.mst.edu/onlineprograms/online-graduate-certificates/value-driveninnovation/ |

##### Department / Program Area: Engineering Management and Systems Engineering

###### MS — Master of Science

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://online.mst.edu/onlineprograms/online-graduate-degrees/engineering-management/ |
| 2 | Engineering Management | https://emse.mst.edu/academicprograms/index.html |
| 3 | Systems Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/systems-engineering/ |
| 4 | Systems Engineering | https://emse.mst.edu/academicprograms/systemsengineering/graduate/ |

###### PhD — Doctor of Philosophy

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://online.mst.edu/onlineprograms/online-graduate-degrees/engineering-management/ |
| 2 | Engineering Management | https://emse.mst.edu/academicprograms/index.html |
| 3 | Systems Engineering | https://online.mst.edu/onlineprograms/online-graduate-degrees/systems-engineering/ |
| 4 | Systems Engineering | https://emse.mst.edu/academicprograms/systemsengineering/graduate/ |

###### Cert — Certificate

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/engineering-management/ |
| 2 | Engineering Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 3 | Financial Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/financial-engineering/ |
| 4 | Financial Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 5 | Foundations of Supply Chain Integration Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 6 | Foundations of Supply Chain Integration Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 7 | Human Systems Integration | https://online.mst.edu/onlineprograms/online-graduate-certificates/human-systems-integration/ |
| 8 | Human Systems Integration | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 9 | Lean Six Sigma | https://online.mst.edu/onlineprograms/online-graduate-certificates/lean-six-sigma/ |
| 10 | Lean Six Sigma | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 11 | Military Construction Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 12 | Model Based Systems Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/systemsengineering/#certificatestext |
| 13 | Modeling and Simulation for Decision Systems | https://online.mst.edu/onlineprograms/online-graduate-certificates/modeling-simulation-decision-systems/ |
| 14 | Modeling and Simulation for Decision Systems | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 15 | Project Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/project-management/ |
| 16 | Project Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 17 | Systems Engineering | https://online.mst.edu/onlineprograms/online-graduate-certificates/systems-engineering/ |
| 18 | Systems Engineering | https://catalog.mst.edu/graduate/graduatedegreeprograms/systemsengineering/#certificatestext |
| 19 | Systems of Human Capital Management | https://catalog.mst.edu/graduate/graduatedegreeprograms/engineeringmanagement/#certificatestext |
| 20 | Systems of Human Capital Management | https://online.mst.edu/onlineprograms/online-graduate-certificates/systems-human-capital-management/ |

> Graduate program total: 228 (must equal 228).

### 2.2 Worked example: Aerospace Engineering (PhD, Online) — CEC, Mechanical and Aerospace Engineering

**Home department**: Mechanical and Aerospace Engineering
**Department URL**: https://mae.mst.edu/
**Program URL (online)**: https://online.mst.edu/onlineprograms/online-graduate-degrees/aerospace-engineering/
**Catalog URL**: https://catalog.mst.edu/graduate/graduatedegreeprograms/aerospaceengineering/
**College**: College of Engineering and Computing — https://cec.mst.edu/
**Mode**: Online (also offered in-person at Rolla campus)
**Term**: 4 years
**Thesis options**: Thesis, Non-thesis
**Description**: "Embark on a journey into the future with our aerospace engineering doctoral degree. This comprehensive online program equips you with cutting-edge knowledge in aerodynamics, system design, propulsion and more."
**Career outcomes**: Aerospace Research Scientist, Advanced Flight Systems Designer, University Professor, Space Propulsion Expert, Aerodynamics Consultant.
**Graduate and International Admissions contact**: stgrad@mst.edu (domestic) / intadm@mst.edu (international) — 573-341-6903

**Per-program application requirements** (live in accordions on the Graduate Admissions page — referenced, not exhaustively listed):
- Application form via Connect portal
- Personal statement ≤1,000 words
- Transcripts (unofficial for review; official after admission)
- 3 letters of recommendation (typical; dept-specific)
- GRE recommended for PhD (test code 6876)
- English proficiency (international applicants)
- Application fee: $55 domestic / $75 international

### 2.3 Graduate admissions model

- **Centralized portal**: https://connect.mst.edu/apply/ (Connect/Slate-based)
- **Graduate office**: https://grad.mst.edu/ (Office of Graduate Education, formerly Office of Graduate Studies)
- **Application fee**: $55 (domestic graduate), $75 (international graduate), $0 (online/distance programs)
- **Test codes**: GRE 6876 / GMAT RWQ-TL-82
- **English proficiency (full admission)**: TOEFL iBT 80 (pre-Jan-2026) / 4.5 (post-Jan-2026); IELTS 6.5; PTE 58; Duolingo 115; Cambridge B2/C1/C2 = 176. Pathway: TOEFL 60/3.5, IELTS 5.5, PTE 50, Duolingo 105, Cambridge 162.
- **Decision timeline**: 2-4 weeks after all materials received.
- **Honor pledge**: Not signed to CGS April 15 resolution; no fixed honor date listed on official pages (N/A).
- **Contact**: stgrad@mst.edu (domestic) — 573-341-6903; intadm@mst.edu (international) — 573-341-7661.

---

## 3. Application Requirements & Deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 |
|------|---|
| Admissions site | https://futurestudents.mst.edu/ |
| Application portal | https://connect.mst.edu/apply/ (Connect/Slate) |
| Common App | Accepted (Missouri S&T profile on commonapp.org) |
| **Fall priority scholarship deadline** | December 1 |
| **Fall final scholarship deadline** | February 1 |
| **Spring priority deadline (UG)** | December 1 |
| **Summer deadline (UG)** | May 1 |
| **Spring transfer deadline** | December 1 |
| **Fall transfer deadline** | July 1 |
| Test-optional policy | Yes — for fall 2025, 2026, 2027 (freshman applicants) |
| SAT/ACT superscore | Yes — accepted |
| SAT score-report code | 6876 |
| ACT score-report code | 2398 |
| Application fee | $0 (no fee for UG applicants) |
| Recommendation letters | Not required for UG; required for select scholarships |
| Interview policy | Not required |
| Min high school units (UG) | 17 units: English 4, Math 4 (Algebra I+), Social Studies 3, Science 3 (1 lab), Fine Arts 1, Foreign Language 2 (same language) |
| Decision notification | Rolling (no firm deadline; applications remain open after priority) |
| Transfer min GPA | 2.5 on 4.0 scale |

### 3.2 Undergraduate English proficiency (international freshmen)

| Exam | Minimum | Recommended |
|------|---------|-------------|
| TOEFL iBT (test taken prior to Jan 1, 2026) | 80 | N/A |
| TOEFL iBT (test taken on/after Jan 1, 2026) | 4.5 | N/A |
| IELTS | 6.5 | N/A |
| PTE Academic | 58 | N/A |
| Duolingo English Test | 115 | N/A |
| Cambridge English B2 First / C1 Advanced / C2 Proficiency | 176 | N/A |

Pathway Program (conditional admission with English support): TOEFL iBT 60/3.5; IELTS 5.5; PTE 50; Duolingo 105; Cambridge 162.

Exempt: applicants who have received a degree from a US, UK, Australia, New Zealand, or Canada (excl. Quebec) institution, or from a country on Missouri S&T's English Proficiency Exempt Countries list.

### 3.3 Graduate — global rules

| 维度 | 值 |
|------|---|
| Application portal | https://connect.mst.edu/apply/ |
| Application fee (domestic) | $55 |
| Application fee (international) | $75 |
| Application fee (online/distance) | $0 |
| GRE | Recommended (test code 6876) — department-specific; some MS/PhD programs waive it |
| GMAT | Required for MBA (code RWQ-TL-82) |
| Master's Fall deadline (recommended) | April 30 |
| Master's Spring deadline (recommended) | November 15 |
| Master's Summer deadline (recommended) | March 15 |
| Doctoral Fall deadline (recommended) | February 15 |
| Doctoral Spring deadline (recommended) | September 15 |
| Doctoral Summer deadline (recommended) | November 15 |
| Decision time | 2-4 weeks after all materials received |
| Three-year bachelor's degrees | Not accepted unless Bologna Process country |
| Personal statement | Required, ≤1,000 words |
| Unofficial transcripts | Accepted for review; official required after admission |
| International enrollment deposit | Required for I-20 processing (non-refundable; credited to student account) |

Graduate English proficiency:

| Exam | Minimum (full admission) | Minimum (Pathway Program) |
|------|--------------------------|---------------------------|
| TOEFL iBT (pre-Jan 1, 2026) | 80 | 60 |
| TOEFL iBT (post-Jan 1, 2026) | 4.5 | 3.5 |
| IELTS | 6.5 | 5.5 |
| PTE Academic | 58 | 50 |
| Duolingo | 115 | 105 |
| Cambridge B2/C1/C2 | 176 | 162 |

---

## 4. Costs & Financial Aid

> All costs below are line-itemized for the current academic year (2026-2027) per the official Cost Estimates page (https://sfs.mst.edu/tuitioncosts/cost-estimates/). Tuition is a flat-rate plateau for 12-18 credit hours per semester.

### 4.1 Undergraduate cost — Missouri resident, Aerospace Engineering BS (representative)

| Expense item | Amount (USD) | Description |
|--------------|-------------|-------------|
| Tuition | $19,494 | Flat-rate plateau for 12-18 credit hours per semester |
| Student Fees | $1,678 | Includes activity, facility, health service, and loan fees |
| Books & Supplies | $720 | Standard estimate |
| Personal Expenses | $1,206 | Based on survey of current S&T students |
| Transportation | $1,826 ($2,954 if living with parent) | Survey-based estimate |
| Living Expenses (9 mo) — Residence Hall | $14,066 | Standard residence hall |
| Living Expenses (9 mo) — Greek/Cooperative | $10,412 | |
| Living Expenses (9 mo) — Off-campus | $9,350 | |
| Living Expenses (9 mo) — With parent | $4,870 | |
| **Total (Residence Hall)** | **$38,990** | Per academic year |
| Total (Greek/CCH) | $35,336 | |
| Total (Off-campus) | $34,274 | |
| Total (With parent) | $30,922 | |

### 4.1b Undergraduate cost — Out-of-State resident, Aerospace Engineering BS

| Expense item | Amount (USD) | Description |
|--------------|-------------|-------------|
| Tuition | $39,436 | Flat-rate plateau for 12-18 credit hours per semester |
| Student Fees | $1,678 | |
| Books & Supplies | $720 | |
| Personal Expenses | $1,206 | |
| Transportation | $2,028 ($2,954 if living with parent) | |
| Living Expenses (9 mo) — Residence Hall | $14,066 | |
| **Total (Residence Hall)** | **$59,134** | |
| Total (Off-campus) | $54,418 | |
| Total (With parent) | $50,864 | |

> Programs are grouped into 3 Missouri-undergrad cost tiers: $26,330-$34,398 (humanities/social sciences); $28,626-$36,694 (sciences/computing/nursing); $30,922-$38,990 (engineering). Out-of-state tiers run ~$19,942 higher across the board. See https://sfs.mst.edu/tuitioncosts/cost-estimates/ for full per-program breakdown.

### 4.2 Graduate cost — Missouri resident (representative; varies by program)

| Expense item | Amount (USD, /year) | Description |
|--------------|---------------------|-------------|
| Tuition (highest grad tier) | $14,760 | Based on 18 hours enrollment per academic year |
| Tuition (mid tier) | $14,256 | |
| Tuition (lower tier) | $12,294 | |
| Tuition (lowest tier) | $10,836 | |
| Student Fees | $1,416 | Activity, facility, health service, loan fees |
| Books & Supplies | $432 | |
| Personal Expenses | $3,570 | Survey-based |
| Transportation | $2,092 ($2,954 with parent) | Survey-based |
| Living Expenses (9 mo) — Residence Hall | $14,066 | |
| Living Expenses (9 mo) — Off-campus | $10,412 | |
| Living Expenses (9 mo) — With parent | $4,870 | |
| **Total (Residence Hall, highest tier)** | **$36,336** | |
| Total (Off-campus, highest tier) | $32,682 | |

Graduate Out-of-State total range (e.g., Aerospace Engineering MS/PhD): $35,978-$45,174/year.

### 4.3 Undergraduate financial-aid policy

| 维度 | 值 |
|------|---|
| % of new undergrads receiving aid | 97% |
| Avg grant & scholarship aid (freshmen) | $13,900/year |
| Need-blind admissions (US) | Yes (institutional policy) |
| Need-blind for international | N/A — institutional aid not generally offered to international freshmen |
| FAFSA priority deadline | February 1 |
| FAFSA code | 002511 (University of Missouri System) |
| Top public university for ROI in Missouri | #1 (Georgetown CEW) |
| Public university career placement | #3 (Princeton Review 2025) |
| Average starting salary (recent grads) | N/A — not published on official pages; see https://career.mst.edu/ |
| Tuition-free income threshold | N/A — Missouri S&T does not publish a tuition-free threshold; evaluated via FAFSA |

### 4.4 Graduate cost & funding framework

| 维度 | 值 |
|------|---|
| Application fee (domestic) | $55 |
| Application fee (international) | $75 |
| Application fee (online/distance) | $0 |
| Funding types | Graduate Research Assistantship (GRA), Graduate Teaching Assistantship (GTA), Graduate Assistantship (GA), Fellowships, Scholarships |
| Fee-waiver policy | Fee waivers available via graduate events (in-person/virtual) |
| Domestic scholarships | https://sfs.mst.edu/financialaid/typesofaid/scholarships/graduate/ |
| International scholarships | https://sfs.mst.edu/financialaid/typesofaid/scholarships/international/ |
| Scholarship Universe portal | https://sfs.mst.edu/financialaid/typesofaid/scholarships/graduate/scholarshipuniverse/ |
| External funding directory | https://grad.mst.edu/funding/opportunities/ |
| GTA English requirement | TOEFL/IELTS minimums higher; see https://gta-workshop.mst.edu/internationalgtas/englishproficiencyrequirementforgtas/ |
| Stipend rates | N/A — varies by department and funding source; contact individual program coordinator |

---

## 5. Evidence Chain Index

Every cited fact in this document binds to the source URL + a verbatim snippet + capture date. Below are evidence blocks covering the highest-value fields.

```yaml
evidence_id: E-U-001
field: institution.identity
value: Missouri University of Science and Technology (Missouri S&T)
source_url: https://www.mst.edu/
source_snippet: "Main gateway: "Missouri University of Science and Technology" — Rolla, MO 65409."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-002
field: undergraduate.totals.count
value: 132
source_url: https://futurestudents.mst.edu/academic-programs/undergraduate-programs/
source_snippet: "UG programs page filter UI shows "132 Results"; 132 unique li.mst-program-entry items extracted."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-U-003
field: undergraduate.degrees.count
value: 38
source_url: https://futurestudents.mst.edu/academic-programs/undergraduate-programs/
source_snippet: "38 items with data-sub-type='Bachelor's Degree'; breakdown: 29 BS + 6 BS/BA combined + 1 BA + 2 generic Bachelor's Degree."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-U-004
field: undergraduate.minors.count
value: 74
source_url: https://futurestudents.mst.edu/academic-programs/undergraduate-programs/
source_snippet: "74 items with data-sub-type='Minor'."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-U-005
field: undergraduate.certificates.count
value: 20
source_url: https://futurestudents.mst.edu/academic-programs/undergraduate-programs/
source_snippet: "20 items with data-sub-type='Certificate'."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-U-006
field: undergraduate.deadlines.priority_scholarship_fall
value: December 1
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""The priority scholarship deadline for the fall semester is December 1, and the final scholarship deadline is February 1.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-007
field: undergraduate.deadlines.final_scholarship_fall
value: February 1
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""...the final scholarship deadline is February 1.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-008
field: undergraduate.deadlines.spring
value: December 1
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Spring Semester (January-May) - apply before December 1""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-009
field: undergraduate.deadlines.summer
value: May 1
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Summer Semester (May-July) - apply before May 1""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-010
field: undergraduate.application_fee
value: $0
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Missouri S&T does not charge an application fee!""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-011
field: undergraduate.test_policy
value: Test-optional through fall 2027 (freshman applicants)
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Freshman applicants for fall 2027 have the option of being reviewed with or without test scores.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-012
field: undergraduate.test_codes
value: ACT: 2398 | SAT: 6876
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Use these codes to send test scores to S&T: ACT: 2398 || SAT: 6876""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-013
field: undergraduate.minimum_units
value: 17 (English 4 / Math 4 / Social Studies 3 / Science 3 [1 lab] / Fine Arts 1 / Foreign Language 2)
source_url: https://futurestudents.mst.edu/admissions/first-timefreshmen/
source_snippet: ""Students planning to attend Missouri S&T should follow a college preparatory curriculum completing at least 17 units of credit.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-014
field: international.undergrad.english_full_admission
value: TOEFL 80 (pre-2026) / 4.5 (post-2026); IELTS 6.5; PTE 58; Duolingo 115; Cambridge 176
source_url: https://futurestudents.mst.edu/admissions/international/freshmen/
source_snippet: ""Full academic admission requires one of the following: TOEFL: 4.5 (Test taken prior to January 1, 2026: 80), IELTS: 6.5, PTE: 58, Duolingo: 115, Cambridge English B2 First, C1 Advanced, or C2 Proficiency: 176""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-015
field: international.undergrad.english_pathway
value: TOEFL 60/3.5; IELTS 5.5; PTE 50; Duolingo 105; Cambridge 162
source_url: https://futurestudents.mst.edu/admissions/international/freshmen/
source_snippet: ""Pathway Program...unofficial scores are accepted): TOEFL: 3.5 (Test taken prior to January 1, 2026: 60), IELTS: 5.5, PTE: 50, Duolingo: 105, Cambridge English B2 First, C1 Advanced, or C2 Proficiency: 162""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-016
field: international.undergrad.freshmen_fall_deadline
value: April 1
source_url: https://futurestudents.mst.edu/admissions/international/freshmen/
source_snippet: ""First-time Freshmen Application Deadlines... Fall Semester (Aug. - Dec.) - April 1""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-017
field: transfer.min_gpa
value: 2.5 on a 4.0 scale
source_url: https://futurestudents.mst.edu/admissions/transfer/
source_snippet: ""Possess a cumulative grade point average of 2.5 or higher on a 4.0 scale.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-U-018
field: transfer.fall_deadline
value: July 1
source_url: https://futurestudents.mst.edu/admissions/transfer/
source_snippet: ""Fall Semester (August-December) - apply before July 1""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-001
field: graduate.totals.count
value: 228
source_url: https://futurestudents.mst.edu/academic-programs/graduate-programs/
source_snippet: "Grad programs page filter UI shows "228 Results"; 228 unique li.mst-program-entry items extracted."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-G-002
field: graduate.degrees.count
value: 85
source_url: https://futurestudents.mst.edu/academic-programs/graduate-programs/
source_snippet: "85 items with data-sub-type='Master's Degree' or 'Doctoral Degree'; breakdown by specificType: 45 MS, 5 MS+MST combined, 3 MEng, 2 MBA, 2 MST, 24 PhD, 5 PhD/DEng combined, 2 DEng, 1 DSc."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-G-003
field: graduate.certificates.count
value: 143
source_url: https://futurestudents.mst.edu/academic-programs/graduate-programs/
source_snippet: "143 items with data-sub-type='Certificate'."
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-G-004
field: graduate.deadlines.masters_fall
value: April 30
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""Master's Recommended Application Deadlines... Fall Semester (Aug. - Dec.) - April 30""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-005
field: graduate.deadlines.doctoral_fall
value: February 15
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""Doctoral Recommended Application Deadlines... Fall Semester (Aug. - Dec.) - Feb. 15""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-006
field: graduate.application_fee_domestic
value: $55
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""$55 application fee for domestic graduate students""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-007
field: graduate.application_fee_international
value: $75
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""$75 application fee for international graduate students.""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-008
field: international.graduate.english_full_admission
value: TOEFL 80/4.5; IELTS 6.5; PTE 58; Duolingo 115; Cambridge 176
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""TOEFL: 4.5 (Test taken prior to January 1, 2026: 80) IELTS: 6.5 PTE: 58 Duolingo: 115 Cambridge English B2 First, C1 Advanced, or C2 Proficiency: 176""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-G-009
field: graduate.test_codes
value: GRE: 6876 / GMAT: RWQ-TL-82
source_url: https://futurestudents.mst.edu/admissions/graduate/
source_snippet: ""S&T's GRE Test Center Code is 6876 / GMAT test code is RWQ-TL-82""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-C-001
field: cost.ug.tuition_missouri_aerospace
value: $19,494/year (plateau 12-18 cr)
source_url: https://sfs.mst.edu/tuitioncosts/cost-estimates/
source_snippet: "Cost breakdown table for "Missouri Undergraduates Aerospace Engineering (BS)": "Tuition Based on plateau rate for 12-18 credit hours per semester | $19,494""
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-C-002
field: cost.ug.total_missouri_aerospace_residence_hall
value: $38,990/year
source_url: https://sfs.mst.edu/tuitioncosts/cost-estimates/
source_snippet: ""Total | $38,990" (Residence Hall column)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-C-003
field: cost.ug.tuition_outofstate_aerospace
value: $39,436/year
source_url: https://sfs.mst.edu/tuitioncosts/cost-estimates/
source_snippet: "Out-of-State Missouri Undergraduates Aerospace Engineering (BS): "Tuition Based on plateau rate... $39,436""
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-C-004
field: cost.ug.total_outofstate_aerospace_residence_hall
value: $59,134/year
source_url: https://sfs.mst.edu/tuitioncosts/cost-estimates/
source_snippet: ""Total | $59,134" (Out-of-State Residence Hall column)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-C-005
field: cost.grad.tuition_outofstate_aerospace
value: Total range $35,978-$45,174/year
source_url: https://sfs.mst.edu/tuitioncosts/cost-estimates/
source_snippet: "Out-of-State Graduate Students Aerospace Engineering (MS PhD): "$35,978 - $45,174 / year""
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

```yaml
evidence_id: E-F-001
field: aid.receipt_rate
value: 97%
source_url: https://sfs.mst.edu/financialaid/
source_snippet: ""97 % New Undergrads Receiving Aid Nearly all new undergrads receive some type of grant and/or scholarship aid""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-F-002
field: aid.avg_grant_scholarship_freshmen
value: $13,900/year
source_url: https://sfs.mst.edu/financialaid/
source_snippet: ""13.9k $ Average Grant & Scholarship Aid Per year for freshmen students""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-F-003
field: aid.fafsa_priority_deadline
value: February 1
source_url: https://sfs.mst.edu/financialaid/
source_snippet: "Callout image alt text: "Submit the FAFSA by Feb 1"; also surfaced via /financialaid/fafsa/."
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-S-001
field: structure.colleges
value: 3 colleges (CASE, CEC, Kummer)
source_url: https://futurestudents.mst.edu/academic-programs/
source_snippet: "Filter sidebar shows "College of Arts, Sciences, and Education, College of Engineering and Computing, Kummer College""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-S-002
field: structure.system
value: University of Missouri System
source_url: https://www.mst.edu/
source_snippet: "Footer: "© 2026 The Curators of the University of Missouri" + UM System link"
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-S-003
field: structure.location
value: Rolla, Missouri, USA 65409
source_url: https://futurestudents.mst.edu/
source_snippet: "Contact block: "Welcome Center, 500 Tim Bradley Way, Rolla, MO 65409""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-S-004
field: rankings.roi
value: #1 Public University in Missouri for Return on Investment
source_url: https://futurestudents.mst.edu/
source_snippet: "Hero stats: "# Best Value Public University in Missouri""
capture_date: 2026-07-07
evidence_type: official_webpage
```

```yaml
evidence_id: E-S-005
field: rankings.career_placement
value: #3 Public University for Career Placement
source_url: https://futurestudents.mst.edu/
source_snippet: "Hero stats: "#3 Public University for Career Placement""
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## 6. WeKnora Import Manifest

### Collection structure

```
collection: missouri-s-t-knowledge-base-v2
  └── document: missouri-s-t-institution-overview           (Section 0)
  ├── document: missouri-s-t-undergraduate-catalog           (Section 1)
  │     ├── chunk: ug-case-arts-languages                    (1 per dept in CASE)
  │     ├── chunk: ug-case-biological-sciences
  │     ├── ... (12 CASE depts)
  │     ├── chunk: ug-cec-chemical-biochemical
  │     ├── ... (10 CEC depts)
  │     ├── chunk: ug-kummer-jaggi-business
  │     ├── chunk: ug-kummer-economics
  │     └── chunk: ug-multi-college-cross-listed-minors
  ├── document: missouri-s-t-graduate-catalog                (Section 2)
  │     ├── chunk: grad-case-math-stat
  │     ├── ... (8 CASE dept/program areas at grad level)
  │     ├── chunk: grad-cec-mechanical-aerospace
  │     ├── ... (13 CEC dept/program areas)
  │     └── chunk: grad-kummer-emse-jaggi-economics
  ├── document: missouri-s-t-application-requirements         (Section 3)
  ├── document: missouri-s-t-costs-and-financial-aid          (Section 4)
  └── document: missouri-s-t-evidence-chain                  (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "missouri-s-t-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BS|BA|MS|MEng|MBA|PhD|DEng|DSc|Minor|Cert>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P1 | Per-department graduate application requirements (specifics, not just the global rules) | https://futurestudents.mst.edu/academic-programs/graduate-programs/ + each program page |
| P1 | Median starting salary by program / department | https://career.mst.edu/ |
| P1 | Tuition-free income threshold / zero-parent-contribution threshold (institutional aid policy) | https://sfs.mst.edu/financialaid/ |
| P2 | April 15-equivalent honor pledge for grad admits | https://grad.mst.edu/ |
| P2 | GTA stipend rates by department | https://gta-workshop.mst.edu/ + dept pages |
| P2 | Departmental test-score minimums (GRE/GMAT) for specific grad programs | Each program's catalog page on https://catalog.mst.edu/ |
| P3 | Engineering Management dept official attribution (hosted in Kummer for grad, CASE+CEC for UG) | https://emse.mst.edu/ |
| P3 | International student population size / % international enrollment | https://ira.mst.edu/ |
| P3 | Acceptance rate / admit rate by college / program | https://ira.mst.edu/ |

---

## 7. Cross-school comparison framework

Comparison matrix with Missouri S&T values + blank columns for other schools in the comparison set.

| Dimension | Missouri S&T | School 2 | School 3 |
|-----------|--------------|----------|----------|
| Region | US (Missouri) | | |
| Total UG cost/yr (Missouri, ResHall) | $38,990 | | |
| Total UG cost/yr (Out-of-State, ResHall) | $59,134 | | |
| Tuition/yr (UG Missouri plateau) | $19,494 | | |
| Tuition/yr (UG Out-of-State plateau) | $39,436 | | |
| Need-blind for international? | N/A (no institutional aid for intl) | | |
| EA deadline | N/A (rolling, priority Dec 1) | | |
| RA deadline | Rolling | | |
| SAT/ACT required? | Optional through Fall 2027 | | |
| TOEFL min (UG, full admit) | 80 / 4.5 | | |
| IELTS min (UG, full admit) | 6.5 | | |
| Tuition-free threshold | N/A (FAFSA-based) | | |
| Median price paid | N/A — published via Net Price Calculator | | |
| Grad application fee | $55 (dom) / $75 (intl) / $0 (online) | | |
| April-15-equivalent honor date | N/A | | |
| Total program count (rule 1) | 360 | | |
| UG degrees | 38 | | |
| UG minors | 74 | | |
| UG certificates | 20 | | |
| Grad degrees | 85 | | |
| Grad certificates | 143 | | |
| Schools/colleges (rule 2) | 3 | | |
| Department count | 27 (UG) + 25 (Grad) | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: futurestudents.mst.edu, grad.mst.edu, sfs.mst.edu, international.mst.edu, case.mst.edu, cec.mst.edu, kummercollege.mst.edu, jaggi.mst.edu, catalog.mst.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction (li.mst-program-entry data attributes, accordion expansion)
> **Granularity**: school → department → degree-level → program
> **Reconciliation**: 132 UG + 228 Grad = 360 ✓; rule-1 total = matrix cell sum = rule-5 row count.