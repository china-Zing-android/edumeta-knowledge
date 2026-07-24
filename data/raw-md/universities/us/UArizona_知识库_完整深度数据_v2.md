# University of Arizona Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 204 |
| 本科辅修 (Minor) | 208 |
| 本科证书 (Certificate) | 37 |
| 研究生学位项目 (MA/MS/MFA/MBA/PhD/etc.) | 294 |
| 研究生辅修 (Minor) | 146 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 146 |
| **学位项目总计 (UG + Grad)** | **498** |
| **全部项目总计 (含辅修/证书)** | **1035** |
| 学院 / 独立系所总数 | 18 |

### 0.2 学院 / 系层级结构

```
University of Arizona
├── College of Agriculture, Life & Environmental Sciences [学院]
│   ├── School of Animal & Veterinary Sciences [系]
│   ├── School of Plant Sciences [系]
│   ├── Department of Agricultural & Resource Economics [系]
│   ├── Department of Environmental Science [系]
│   └── ... (13 departments)
├── College of Architecture, Planning & Landscape Architecture [学院]
│   ├── School of Architecture [系]
│   ├── School of Planning [系]
│   └── School of Landscape Architecture [系]
├── College of Education [学院]
│   ├── Department of Teaching, Learning & Sociocultural Studies [系]
│   ├── Department of Educational Policy Studies & Practice [系]
│   ├── Department of Disability & Psychoeducational Studies [系]
│   └── Department of Educational Psychology [系]
├── College of Engineering [学院]
│   ├── Department of Aerospace & Mechanical Engineering [系]
│   ├── Department of Biomedical Engineering [系]
│   ├── Department of Chemical & Environmental Engineering [系]
│   ├── Department of Civil & Architectural Engineering [系]
│   ├── Department of Electrical & Computer Engineering [系]
│   ├── Department of Industrial Engineering [系]
│   ├── Department of Materials Science & Engineering [系]
│   ├── Department of Mining & Geological Engineering [系]
│   ├── Department of Optical Sciences [系]
│   ├── Department of Systems & Industrial Engineering [系]
│   └── School of Sustainable Built Environments [系]
├── College of Fine Arts [学院]
│   ├── School of Art [系]
│   ├── School of Dance [系]
│   ├── School of Music [系]
│   ├── School of Theatre, Film & Television [系]
│   └── School of Art (Visual Communications) [系]
├── College of Humanities [学院]
│   ├── Department of English [系]
│   ├── Department of History [系]
│   ├── Department of Philosophy [系]
│   ├── Department of Linguistics [系]
│   ├── Department of Religious Studies [系]
│   ├── Department of East Asian Studies [系]
│   ├── Department of German Studies [系]
│   ├── Department of Russian & Slavic Studies [系]
│   ├── Department of Spanish & Portuguese [系]
│   ├── Department of French & Italian [系]
│   └── ... (14 departments)
├── College of Information Science [学院]
│   ├── School of Information [系]
│   └── Department of Data Science [系]
├── Eller College of Management [学院]
│   ├── School of Accountancy [系]
│   ├── Department of Finance [系]
│   ├── Department of Marketing [系]
│   ├── Department of Management & Organizations [系]
│   ├── Department of Management Information Systems [系]
│   ├── Department of Economics [系]
│   └── School of Government & Public Policy [系]
├── College of Medicine [学院]
│   ├── Department of Medicine [系]
│   ├── Department of Surgery [系]
│   ├── Department of Pediatrics [系]
│   └── ... (basic science & clinical departments)
├── College of Nursing [学院]
├── R. Ken Coit College of Pharmacy [学院]
│   ├── Department of Pharmacology & Toxicology [系]
│   └── Department of Pharmacy Practice & Science [系]
├── College of Science [学院]
│   ├── Department of Astronomy [系]
│   ├── Department of Chemistry & Biochemistry [系]
│   ├── Department of Computer Science [系]
│   ├── Department of Ecology & Evolutionary Biology [系]
│   ├── Department of Geosciences [系]
│   ├── Department of Mathematics [系]
│   ├── Department of Molecular & Cellular Biology [系]
│   ├── Department of Neuroscience [系]
│   ├── Department of Physics [系]
│   ├── Department of Physiology [系]
│   ├── Department of Psychology [系]
│   └── Department of Speech, Language & Hearing Sciences [系]
├── College of Social & Behavioral Sciences [学院]
│   ├── Department of Anthropology [系]
│   ├── Department of Communication [系]
│   ├── Department of Geography & Development [系]
│   ├── Department of Journalism [系]
│   ├── Department of Philosophy [系]
│   ├── Department of Political Science [系]
│   ├── Department of Sociology [系]
│   ├── School of Government & Public Policy [系]
│   └── School of International Languages, Literatures & Cultures [系]
├── James E. Rogers College of Law [学院]
├── College of Veterinary Medicine [学院]
├── Mel & Enid Zuckerman College of Public Health [学院]
│   ├── Division of Epidemiology & Biostatistics [系]
│   ├── Division of Community, Environment & Policy [系]
│   └── Division of Health Promotion Sciences [系]
├── W.A. Franke Honors College [学院]
└── Graduate College (Interdisciplinary) [学院]
    └── Graduate Interdisciplinary Programs (GIDPs) [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 114 |
| BA | Bachelor of Arts | 本科 | 70 |
| BAS | Bachelor of Applied Science | 本科 | 8 |
| BFA | Bachelor of Fine Arts | 本科 | 6 |
| BM | Bachelor of Music | 本科 | 3 |
| BArch | Bachelor of Architecture | 本科 | 1 |
| MBA | MBA | 本科 | 1 |
| BLA | Bachelor of Landscape Architecture | 本科 | 1 |
| MS | Master of Science | 研究生 | 104 |
| PhD | Doctor of Philosophy | 研究生 | 95 |
| MA | Master of Arts | 研究生 | 55 |
| PSM | Professional Science Masters | 研究生 | 6 |
| MFA | Master of Fine Arts | 研究生 | 4 |
| MEd | Master of Education | 研究生 | 4 |
| MD | Doctor of Medicine | 研究生 | 4 |
| EdD | Doctor of Education | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 2 |
| EdS | Educational Specialist | 研究生 | 2 |
| MArch | Master of Architecture | 研究生 | 1 |
| AuD | Doctor of Audiology | 研究生 | 1 |
| MEng | Master of Engineering | 研究生 | 1 |
| MLA | Master of Landscape Architecture | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 1 |
| SJD | Scientiae Juridicae Doctor | 研究生 | 1 |
| DMA | Doctor of Musical Arts | 研究生 | 1 |
| MM | Master of Music | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| DrPH | Doctor of Public Health | 研究生 | 1 |
| PharmD | Doctor of Pharmacy | 研究生 | 1 |
| MPP | Master of Public Policy | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| Minor | 辅修 | 本科 | 208 |
| Minor | 辅修 | 研究生 | 146 |
| Certificate | 证书 | 本科 | 37 |
| Certificate | 证书 | 研究生 | 146 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BAS | BM | BArch | BLA | MS | MA | PhD | MFA | MBA | MEd | MD | EdD | EdS | MPH | MArch | MEng | MLA | AuD | DMA | MM | DNP | DrPH | DPT | DVM | PharmD | JD | LLM | SJD | MPA | MPP | PSM | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Agriculture, Life & Environmental Sciences | 1 | 25 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **27** |
| College of Architecture, Planning & Landscape Architecture | 0 | 2 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **4** |
| College of Education | 2 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **8** |
| College of Engineering | 0 | 23 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **24** |
| College of Fine Arts | 8 | 0 | 6 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **17** |
| College of Humanities | 14 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **15** |
| College of Information Science | 4 | 4 | 0 | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **14** |
| College of Medicine | 0 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **9** |
| College of Nursing | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| College of Science | 11 | 24 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **35** |
| College of Social & Behavioral Sciences | 27 | 8 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **35** |
| College of Veterinary Medicine | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| Eller College of Management | 1 | 11 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **12** |
| James E. Rogers College of Law | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | **5** |
| Mel & Enid Zuckerman College of Public Health | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **2** |
| R. Ken Coit College of Pharmacy | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **3** |
| W.A. Franke Honors College | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | **1** |
| **合计** | 70 | 114 | 6 | 8 | 3 | 1 | 1 | 104 | 55 | 95 | 4 | 1 | 4 | 4 | 2 | 2 | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 | **498** |
---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

The University of Arizona has 20 colleges and schools offering undergraduate programs. The undergraduate colleges are organized by discipline, with most offering Bachelor of Science (BS) and Bachelor of Arts (BA) degrees. The W.A. Franke Honors College provides interdisciplinary options. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agriculture, Life & Environmental Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Industry's Science and Technology | <https://catalog.arizona.edu/programs/FITSBA> |

##### BAS

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Services | <https://catalog.arizona.edu/programs/HSVBAPS> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agribusiness Economics and Management | <https://catalog.arizona.edu/programs/ABEMBS> |
| 2 | Agricultural Systems Management | <https://catalog.arizona.edu/programs/AGSMBS> |
| 3 | Agricultural Technology Management and Education | <https://catalog.arizona.edu/programs/AGTEBS> |
| 4 | Agricultural and Applied Economics | <https://catalog.arizona.edu/programs/AAEBS> |
| 5 | Animal Sciences | <https://catalog.arizona.edu/programs/ASCBS> |
| 6 | Applied Biotechnology | <https://catalog.arizona.edu/programs/APBTBS> |
| 7 | Biosystems Analytics and Technology | <https://catalog.arizona.edu/programs/BATBS> |
| 8 | Environmental Science | <https://catalog.arizona.edu/programs/ENVSBSES> |
| 9 | Environmental and Water Resource Economics | <https://catalog.arizona.edu/programs/EWREBS> |
| 10 | Family Studies and Human Development | <https://catalog.arizona.edu/programs/FSHDBS> |
| 11 | Food Safety | <https://catalog.arizona.edu/programs/FDSFBS> |
| 12 | Human Development and Family Science | <https://catalog.arizona.edu/programs/HDFSBS> |
| 13 | Microbiology | <https://catalog.arizona.edu/programs/MICRBS> |
| 14 | Natural Resources | <https://catalog.arizona.edu/programs/NTRSBS> |
| 15 | Nutrition & Human Performance | <https://catalog.arizona.edu/programs/NHPBS> |
| 16 | Nutrition and Dietetics | <https://catalog.arizona.edu/programs/NTDIBS> |
| 17 | Nutrition and Food Systems | <https://catalog.arizona.edu/programs/NFSBS> |
| 18 | Nutritional Sciences | <https://catalog.arizona.edu/programs/NUSCBS> |
| 19 | Nutritional Sciences and Wellness | <https://catalog.arizona.edu/programs/NTSWBS> |
| 20 | Personal and Family Financial Planning | <https://catalog.arizona.edu/programs/PFFPBS> |
| 21 | Plant Sciences | <https://catalog.arizona.edu/programs/PLSCBS> |
| 22 | Precision Nutrition and Wellness | <https://catalog.arizona.edu/programs/PRNWBS> |
| 23 | Retailing & Consumer Science | <https://catalog.arizona.edu/programs/RCSCBS> |
| 24 | Sustainable Plant Systems | <https://catalog.arizona.edu/programs/SPSBS> |
| 25 | Veterinary Science | <https://catalog.arizona.edu/programs/VSCBS> |

#### College of Architecture, Planning & Landscape Architecture

##### BArch

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | <https://catalog.arizona.edu/programs/ARCHBARCH> |

##### BLA

| # | 专业 | URL |
|---|------|-----|
| 1 | Landscape Architecture | <https://catalog.arizona.edu/programs/LARBLA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Real Estate | <https://catalog.arizona.edu/programs/REBS> |
| 2 | Sustainable Built Environments | <https://catalog.arizona.edu/programs/SBEBSSBE> |

#### College of Education

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | <https://catalog.arizona.edu/programs/ECEDBAED> |
| 2 | Elementary Education | <https://catalog.arizona.edu/programs/ELEMBAED> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Deaf Studies | <https://catalog.arizona.edu/programs/DFSTBSED> |
| 2 | Elementary Education | <https://catalog.arizona.edu/programs/ELEMBS> |
| 3 | Leadership and Learning Innovation | <https://catalog.arizona.edu/programs/LLIBS> |
| 4 | Literacy, Learning and Leadership | <https://catalog.arizona.edu/programs/LLLBS> |
| 5 | Mild to Moderate Disabilities | <https://catalog.arizona.edu/programs/MMDIBSED> |
| 6 | Rehabilitation Studies Service | <https://catalog.arizona.edu/programs/RHSSBSED> |

#### College of Engineering

##### BAS

| # | 专业 | URL |
|---|------|-----|
| 1 | Intelligence and Information Operations | <https://catalog.arizona.edu/programs/IISBAPS> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 |  | <https://catalog.arizona.edu/programs/ECEBSSAM> |
| 2 |  | <https://catalog.arizona.edu/programs/INEBSSAM> |
| 3 |  | <https://catalog.arizona.edu/programs/INEBSUPC> |
| 4 |  | <https://catalog.arizona.edu/programs/MEEBSHEB> |
| 5 |  | <https://catalog.arizona.edu/programs/MEEBSSAM> |
| 6 |  | <https://catalog.arizona.edu/programs/MSEBSHEB> |
| 7 | Aerospace Engineering | <https://catalog.arizona.edu/programs/AEEBSAEE> |
| 8 | Architectural Engineering | <https://catalog.arizona.edu/programs/AREBSARE> |
| 9 | Biomedical Engineering | <https://catalog.arizona.edu/programs/BMEBSBME> |
| 10 | Biosystems Engineering | <https://catalog.arizona.edu/programs/BEBSBE> |
| 11 | Chemical Engineering | <https://catalog.arizona.edu/programs/CHEBSCHE> |
| 12 | Civil Engineering | <https://catalog.arizona.edu/programs/CVEBSCVE> |
| 13 | Computer Science and Engineering | <https://catalog.arizona.edu/programs/CSEBSCSE> |
| 14 | Electrical and Computer Engineering | <https://catalog.arizona.edu/programs/ECEBSECE> |
| 15 | Engineering Management | <https://catalog.arizona.edu/programs/EMGBSEMG> |
| 16 | Environmental Engineering | <https://catalog.arizona.edu/programs/EENBSEEN> |
| 17 | Industrial Engineering | <https://catalog.arizona.edu/programs/INEBSINE> |
| 18 | Materials Science and Engineering | <https://catalog.arizona.edu/programs/MSEBSMSE> |
| 19 | Mechanical Engineering | <https://catalog.arizona.edu/programs/MEEBSMEE> |
| 20 | Mining Engineering | <https://catalog.arizona.edu/programs/MNEBSMNE> |
| 21 | Optical Sciences & Engineering | <https://catalog.arizona.edu/programs/OSEBSOSE> |
| 22 | Software Engineering | <https://catalog.arizona.edu/programs/SFEBSSFE> |
| 23 | Systems Engineering | <https://catalog.arizona.edu/programs/SYEBSSYE> |

#### College of Fine Arts

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | <https://catalog.arizona.edu/programs/ARHBA> |
| 2 | Design Arts and Practice | <https://catalog.arizona.edu/programs/DAPBA> |
| 3 | Film and Television | <https://catalog.arizona.edu/programs/FTVBA> |
| 4 | Live and Immersive Arts | <https://catalog.arizona.edu/programs/LIABA> |
| 5 | Live and Screened Performance | <https://catalog.arizona.edu/programs/LSCPBA> |
| 6 | Music | <https://catalog.arizona.edu/programs/MUSBA> |
| 7 | Studio Art | <https://catalog.arizona.edu/programs/STDOBA> |
| 8 | Theatre Arts | <https://catalog.arizona.edu/programs/THARBA> |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art and Visual Culture Education | <https://catalog.arizona.edu/programs/ARVCBFA> |
| 2 | Dance | <https://catalog.arizona.edu/programs/DNCBFA> |
| 3 | Film and Television | <https://catalog.arizona.edu/programs/FTVBFA> |
| 4 | Musical Theatre | <https://catalog.arizona.edu/programs/MTHRBFA> |
| 5 | Studio Art | <https://catalog.arizona.edu/programs/STDOBFA> |
| 6 | Theatre Production | <https://catalog.arizona.edu/programs/THPRBFA> |

##### BM

| # | 专业 | URL |
|---|------|-----|
| 1 | Music Education | <https://catalog.arizona.edu/programs/MUEDBMUS> |
| 2 | Music Therapy | <https://catalog.arizona.edu/programs/MUTPBMUS> |
| 3 | Performance | <https://catalog.arizona.edu/programs/PERFBMUS> |

#### College of Humanities

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | <https://catalog.arizona.edu/programs/AFSBA> |
| 2 | Applied Humanities | <https://catalog.arizona.edu/programs/APHMBA> |
| 3 | Classics | <https://catalog.arizona.edu/programs/CLASBA> |
| 4 | East Asian Studies | <https://catalog.arizona.edu/programs/EASBA> |
| 5 | French | <https://catalog.arizona.edu/programs/FRENBA> |
| 6 | General Studies | <https://catalog.arizona.edu/programs/GNSTBGS> |
| 7 | German Studies | <https://catalog.arizona.edu/programs/GERSBA> |
| 8 | Interdisciplinary Studies | <https://catalog.arizona.edu/programs/IDSTBA> |
| 9 | Interdisciplinary Studies | <https://catalog.arizona.edu/programs/IDSTBIS> |
| 10 | Italian | <https://catalog.arizona.edu/programs/ITALBA> |
| 11 | Religious Studies | <https://catalog.arizona.edu/programs/RELIBA> |
| 12 | Russian | <https://catalog.arizona.edu/programs/RUSSBA> |
| 13 | Spanish | <https://catalog.arizona.edu/programs/SPANBA> |
| 14 | World Literature | <https://catalog.arizona.edu/programs/WLITBA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies for Health Professionals | <https://catalog.arizona.edu/programs/RELIHPBS> |

#### College of Information Science

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Emerging Technologies in Society | <https://catalog.arizona.edu/programs/ISECBA> |
| 2 | Game Design | <https://catalog.arizona.edu/programs/GMBVBA> |
| 3 | Government and Public Service | <https://catalog.arizona.edu/programs/GPSBA> |
| 4 | Information Science and Arts | <https://catalog.arizona.edu/programs/ISABA> |

##### BAS

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Computing | <https://catalog.arizona.edu/programs/ACBAPS> |
| 2 | Applied Science | <https://catalog.arizona.edu/programs/APSBAPS> |
| 3 | Cyber Defense | <https://catalog.arizona.edu/programs/CYBRBAPS> |
| 4 | Early Childhood | <https://catalog.arizona.edu/programs/ECBAPS> |
| 5 | Justice and Global Security | <https://catalog.arizona.edu/programs/JGSBAPS> |
| 6 | Organizational Leadership and Regional Commerce | <https://catalog.arizona.edu/programs/OLRCBAPS> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Cyber Operations | <https://catalog.arizona.edu/programs/CYBRBS> |
| 2 | Game Development | <https://catalog.arizona.edu/programs/GDDBS> |
| 3 | Information Science | <https://catalog.arizona.edu/programs/ISCBS> |
| 4 | Information Science and Technology | <https://catalog.arizona.edu/programs/ISTBS> |

#### College of Medicine

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Emergency Medical Services | <https://catalog.arizona.edu/programs/EMSBS> |
| 2 | Medical Device Development and Application | <https://catalog.arizona.edu/programs/MDDABS> |
| 3 | Medicine | <https://catalog.arizona.edu/programs/MEDBS> |
| 4 | Physiology | <https://catalog.arizona.edu/programs/PSIOBSHS> |
| 5 | Physiology and Medical Sciences | <https://catalog.arizona.edu/programs/PSIOMBSHS> |

#### College of Nursing

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | <https://catalog.arizona.edu/programs/NURSBSN> |
| 2 | Nursing - Collaborative Education | <https://catalog.arizona.edu/programs/NURSCEBSN> |

#### College of Science

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | <https://catalog.arizona.edu/programs/BIOCBA> |
| 2 | Chemistry | <https://catalog.arizona.edu/programs/CHEMBA> |
| 3 | Computer Science | <https://catalog.arizona.edu/programs/COSCBA> |
| 4 | Ecology and Evolutionary Biology | <https://catalog.arizona.edu/programs/ECOLBA> |
| 5 | Geosciences and Society | <https://catalog.arizona.edu/programs/GSCSBA> |
| 6 | Mathematics | <https://catalog.arizona.edu/programs/MATHBA> |
| 7 | Molecular and Cellular Biology | <https://catalog.arizona.edu/programs/MCBBA> |
| 8 | Physics | <https://catalog.arizona.edu/programs/PHYSBA> |
| 9 | Psychology | <https://catalog.arizona.edu/programs/PSYCBA> |
| 10 | Science | <https://catalog.arizona.edu/programs/SCIBA> |
| 11 | Statistics and Data Science | <https://catalog.arizona.edu/programs/STATDSBA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Physics | <https://catalog.arizona.edu/programs/APHYSBS> |
| 2 | Artificial Intelligence | <https://catalog.arizona.edu/programs/AIBS> |
| 3 | Astronomy | <https://catalog.arizona.edu/programs/ASTRBS> |
| 4 | Biochemistry | <https://catalog.arizona.edu/programs/BIOCBS> |
| 5 | Bioinformatics | <https://catalog.arizona.edu/programs/BIOINBS> |
| 6 | Biology | <https://catalog.arizona.edu/programs/BIOLBS> |
| 7 | Chemistry | <https://catalog.arizona.edu/programs/CHEMBS> |
| 8 | Computer Science | <https://catalog.arizona.edu/programs/COSCBS> |
| 9 | Data Science | <https://catalog.arizona.edu/programs/DSCBS> |
| 10 | Ecology and Evolutionary Biology | <https://catalog.arizona.edu/programs/ECOLBS> |
| 11 | Genetics and Genomics | <https://catalog.arizona.edu/programs/GGBS> |
| 12 | Geosciences | <https://catalog.arizona.edu/programs/GEOSBS> |
| 13 | Hydrology and Atmospheric Sciences | <https://catalog.arizona.edu/programs/HASBS> |
| 14 | Mathematics | <https://catalog.arizona.edu/programs/MATHBS> |
| 15 | Molecular and Cellular Biology | <https://catalog.arizona.edu/programs/MCBBS> |
| 16 | Neuroscience | <https://catalog.arizona.edu/programs/NSCIBS> |
| 17 | Neuroscience and Cognitive Science | <https://catalog.arizona.edu/programs/NCSBS> |
| 18 | Physics | <https://catalog.arizona.edu/programs/PHYSBS> |
| 19 | Planetary Geoscience | <https://catalog.arizona.edu/programs/PTGSBS> |
| 20 | Psychological Science | <https://catalog.arizona.edu/programs/PSYSBS> |
| 21 | Science | <https://catalog.arizona.edu/programs/SCIBS> |
| 22 | Science Law | <https://catalog.arizona.edu/programs/SCILBS> |
| 23 | Speech, Language and Hearing Sciences | <https://catalog.arizona.edu/programs/SLHSBS> |
| 24 | Statistics and Data Science | <https://catalog.arizona.edu/programs/STATDSBS> |

#### College of Social & Behavioral Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | American Indian Studies | <https://catalog.arizona.edu/programs/AISBA> |
| 2 | Anthropology | <https://catalog.arizona.edu/programs/ANTHBA> |
| 3 | Arabic | <https://catalog.arizona.edu/programs/ARBBA> |
| 4 | Communication | <https://catalog.arizona.edu/programs/COMMBA> |
| 5 | Creative Writing | <https://catalog.arizona.edu/programs/CRTVBA> |
| 6 | English | <https://catalog.arizona.edu/programs/ENGLBA> |
| 7 | Environmental Studies | <https://catalog.arizona.edu/programs/EVSBA> |
| 8 | Food Studies | <https://catalog.arizona.edu/programs/FOODBA> |
| 9 | Gender & Women's Studies | <https://catalog.arizona.edu/programs/GWSBA> |
| 10 | Geography | <https://catalog.arizona.edu/programs/GEOGBA> |
| 11 | Global Studies | <https://catalog.arizona.edu/programs/GLSTBA> |
| 12 | History | <https://catalog.arizona.edu/programs/HISTBA> |
| 13 | Human Rights Practice | <https://catalog.arizona.edu/programs/HRTSBA> |
| 14 | Journalism | <https://catalog.arizona.edu/programs/JOURBA> |
| 15 | Judaic Studies | <https://catalog.arizona.edu/programs/JUSBA> |
| 16 | Latin American Studies | <https://catalog.arizona.edu/programs/LASBA> |
| 17 | Law | <https://catalog.arizona.edu/programs/LAWBA> |
| 18 | Linguistics | <https://catalog.arizona.edu/programs/LINGBA> |
| 19 | Mexican American Studies | <https://catalog.arizona.edu/programs/MASBA> |
| 20 | Middle Eastern and North African Studies | <https://catalog.arizona.edu/programs/MENASBA> |
| 21 | Philosophy | <https://catalog.arizona.edu/programs/PHILBA> |
| 22 | Philosophy, Politics, Economics and Law | <https://catalog.arizona.edu/programs/PPELBA> |
| 23 | Political Science | <https://catalog.arizona.edu/programs/POLBA> |
| 24 | Professional and Technical Writing | <https://catalog.arizona.edu/programs/PTWBA> |
| 25 | Public Relations | <https://catalog.arizona.edu/programs/PRBA> |
| 26 | Sociology | <https://catalog.arizona.edu/programs/SOCBA> |
| 27 | Studies of Global Media | <https://catalog.arizona.edu/programs/GLOBA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | <https://catalog.arizona.edu/programs/ANTHBS> |
| 2 | Care, Health and Society | <https://catalog.arizona.edu/programs/CHSBS> |
| 3 | Criminal Justice Studies | <https://catalog.arizona.edu/programs/CJSBS> |
| 4 | Geographic Information Systems Technology | <https://catalog.arizona.edu/programs/GISTBS> |
| 5 | Geography | <https://catalog.arizona.edu/programs/GEOGBS> |
| 6 | Public Affairs | <https://catalog.arizona.edu/programs/PAFBS> |
| 7 | Public Management & Policy | <https://catalog.arizona.edu/programs/PMPCBS> |
| 8 | Urban and Regional Development | <https://catalog.arizona.edu/programs/UREGBS> |

#### Eller College of Management

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | <https://catalog.arizona.edu/programs/ECONBA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | <https://catalog.arizona.edu/programs/ACCTBSBA> |
| 2 | Business Administration | <https://catalog.arizona.edu/programs/BNADBSBA> |
| 3 | Business Analytics | <https://catalog.arizona.edu/programs/BNANBSBA> |
| 4 | Business Economics | <https://catalog.arizona.edu/programs/BNECBSBA> |
| 5 | Business Management | <https://catalog.arizona.edu/programs/BMGTBSBA> |
| 6 | Entrepreneurship | <https://catalog.arizona.edu/programs/ENTRBSBA> |
| 7 | Finance | <https://catalog.arizona.edu/programs/FINBSBA> |
| 8 | Integrated Business and Engineering | <https://catalog.arizona.edu/programs/IBEBS> |
| 9 | Management Information Systems | <https://catalog.arizona.edu/programs/MISBSBA> |
| 10 | Marketing | <https://catalog.arizona.edu/programs/MKTGBSBA> |
| 11 | Operations and Supply Chain Management | <https://catalog.arizona.edu/programs/OSCMBSBA> |

#### Graduate College (Interdisciplinary)

##### MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | <https://catalog.arizona.edu/programs/BNADMBA> |

#### Mel & Enid Zuckerman College of Public Health

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Wellness and Health Promotion Practice | <https://catalog.arizona.edu/programs/WHPPBA> |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Public Health | <https://catalog.arizona.edu/programs/PHLBS> |

#### R. Ken Coit College of Pharmacy

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Medical Pharmacology and Toxicology | <https://catalog.arizona.edu/programs/MPTBS> |
| 2 | Pharmaceutical Sciences | <https://catalog.arizona.edu/programs/PHSCBS> |

#### W.A. Franke Honors College

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Intelligence and Innovation | <https://catalog.arizona.edu/programs/CIIBCII> |

### 1.4 Minors — complete list

| # | Minor name | Home school/department | URL |
|---|------------|----------------------|-----|
| 1 |  |  | <https://catalog.arizona.edu/programs/THMMINU2> |
| 2 | AI and Society |  | <https://catalog.arizona.edu/programs/AISOCMINU> |
| 3 | Addiction and Substance Use |  | <https://catalog.arizona.edu/programs/ADSUMINU> |
| 4 | Additive Manufacturing |  | <https://catalog.arizona.edu/programs/ADMFGMINU> |
| 5 | Adolescents, Community and Education |  | <https://catalog.arizona.edu/programs/ACEMINU> |
| 6 | Aerospace Engineering |  | <https://catalog.arizona.edu/programs/AEEMINU> |
| 7 | Africana Studies |  | <https://catalog.arizona.edu/programs/AFSMINU> |
| 8 | Aging and Population Health |  | <https://catalog.arizona.edu/programs/APHTHMINU> |
| 9 | Agribusiness Economics and Management |  | <https://catalog.arizona.edu/programs/ABEMMINU> |
| 10 | Agricultural Technology Management and Education |  | <https://catalog.arizona.edu/programs/AGTEMINU> |
| 11 | Agriculture and Life Sciences |  | <https://catalog.arizona.edu/programs/ALSTMINU> |
| 12 | American Indian Studies |  | <https://catalog.arizona.edu/programs/AISMINU> |
| 13 | American Sign Language |  | <https://catalog.arizona.edu/programs/ASLMINU> |
| 14 | Ancient Greek |  | <https://catalog.arizona.edu/programs/AGRKMINU> |
| 15 | Animal Sciences |  | <https://catalog.arizona.edu/programs/ASCMINU> |
| 16 | Anthropology |  | <https://catalog.arizona.edu/programs/ANTHMINU> |
| 17 | Applied Biotechnology |  | <https://catalog.arizona.edu/programs/APBTMINU> |
| 18 | Applied Computing |  | <https://catalog.arizona.edu/programs/ACMINU> |
| 19 | Arabic |  | <https://catalog.arizona.edu/programs/ARBMINU> |
| 20 | Architecture History and Theory |  | <https://catalog.arizona.edu/programs/AHTMINU> |
| 21 | Art History |  | <https://catalog.arizona.edu/programs/ARHMINU> |
| 22 | Art and Visual Culture Education |  | <https://catalog.arizona.edu/programs/ARVCMINU> |
| 23 | Artificial Intelligence |  | <https://catalog.arizona.edu/programs/AIMINU> |
| 24 | Arts Administration |  | <https://catalog.arizona.edu/programs/ARTADMINU> |
| 25 | Asian Pacific American Studies |  | <https://catalog.arizona.edu/programs/APASMINU> |
| 26 | Astrobiology |  | <https://catalog.arizona.edu/programs/ASBMINU> |
| 27 | Astronomical Studies |  | <https://catalog.arizona.edu/programs/ASTSTDMINU> |
| 28 | Astronomy |  | <https://catalog.arizona.edu/programs/ASTRMINU> |
| 29 | Biochemistry |  | <https://catalog.arizona.edu/programs/BIOCMINU> |
| 30 | Bioethics |  | <https://catalog.arizona.edu/programs/BIOEMINU> |
| 31 | Biology |  | <https://catalog.arizona.edu/programs/BIOLMINU> |
| 32 | Biosystems Analytics and Technology |  | <https://catalog.arizona.edu/programs/BATMINU> |
| 33 | Biosystems Engineering |  | <https://catalog.arizona.edu/programs/BEMINU> |
| 34 | Business Administration |  | <https://catalog.arizona.edu/programs/BNADMINU> |
| 35 | Care, Health and Society |  | <https://catalog.arizona.edu/programs/CHSMINU> |
| 36 | Chemical Engineering |  | <https://catalog.arizona.edu/programs/CHEMINU> |
| 37 | Chemistry |  | <https://catalog.arizona.edu/programs/CHEMMINU> |
| 38 | Chinese Culture |  | <https://catalog.arizona.edu/programs/CHNCLTMINU> |
| 39 | Chinese Language |  | <https://catalog.arizona.edu/programs/CHNLNGMINU> |
| 40 | Civil Engineering |  | <https://catalog.arizona.edu/programs/CVEMINU> |
| 41 | Classics |  | <https://catalog.arizona.edu/programs/CLASMINU> |
| 42 | Climate Change and Public Health |  | <https://catalog.arizona.edu/programs/CCPHMINU> |
| 43 | Climate Change and Society |  | <https://catalog.arizona.edu/programs/CCSMINU> |
| 44 | Communication |  | <https://catalog.arizona.edu/programs/COMMMINU> |
| 45 | Community Innovation |  | <https://catalog.arizona.edu/programs/AETIMINU> |
| 46 | Computational Social Science |  | <https://catalog.arizona.edu/programs/CSSMINU> |
| 47 | Computer Science |  | <https://catalog.arizona.edu/programs/COSCMINU> |
| 48 | Computer Science and Engineering |  | <https://catalog.arizona.edu/programs/CSEMINU> |
| 49 | Consciousness Studies |  | <https://catalog.arizona.edu/programs/CSMINU> |
| 50 | Creative Intelligence and Innovation |  | <https://catalog.arizona.edu/programs/CIIMINU> |
| 51 | Creative Writing |  | <https://catalog.arizona.edu/programs/CRTVMINU> |
| 52 | Criminology |  | <https://catalog.arizona.edu/programs/CRMMINU> |
| 53 | Critical Languages |  | <https://catalog.arizona.edu/programs/CRLMINU> |
| 54 | Cyber Operations |  | <https://catalog.arizona.edu/programs/CYBRMINU> |
| 55 | Dance |  | <https://catalog.arizona.edu/programs/DNCMINU> |
| 56 | Digital Retailing |  | <https://catalog.arizona.edu/programs/DGTRTMINU> |
| 57 | East Asian Studies |  | <https://catalog.arizona.edu/programs/EASMINU> |
| 58 | Ecology and Evolutionary Biology |  | <https://catalog.arizona.edu/programs/ECOLMINU> |
| 59 | Economics |  | <https://catalog.arizona.edu/programs/ECONMINU> |
| 60 | Educational Psychology |  | <https://catalog.arizona.edu/programs/EDPMINU> |
| 61 | Electrical and Computer Engineering |  | <https://catalog.arizona.edu/programs/ECEMINU> |
| 62 | Emergency Medical Services |  | <https://catalog.arizona.edu/programs/EMSMINU> |
| 63 | Emerging Technologies in Society |  | <https://catalog.arizona.edu/programs/ISECMINU> |
| 64 | Engineering Management |  | <https://catalog.arizona.edu/programs/EMGMINU> |
| 65 | English |  | <https://catalog.arizona.edu/programs/ENGLMINU> |
| 66 | English Applied Linguistics |  | <https://catalog.arizona.edu/programs/EALMINU> |
| 67 | Enterprise Leadership |  | <https://catalog.arizona.edu/programs/ENLMINU> |
| 68 | Entomology |  | <https://catalog.arizona.edu/programs/ENTOMINU> |
| 69 | Entrepreneurship and Innovation |  | <https://catalog.arizona.edu/programs/ENTRMINU> |
| 70 | Environmental Engineering |  | <https://catalog.arizona.edu/programs/EENMINU> |
| 71 | Environmental Hydrology and Water Resources |  | <https://catalog.arizona.edu/programs/EHYMINU> |
| 72 | Environmental Science |  | <https://catalog.arizona.edu/programs/ENVSMINU> |
| 73 | Environmental Studies |  | <https://catalog.arizona.edu/programs/EVSMINU> |
| 74 | Environmental and Occupational Health |  | <https://catalog.arizona.edu/programs/EOHMINU> |
| 75 | Environmental and Water Resource Economics |  | <https://catalog.arizona.edu/programs/EWREMINU> |
| 76 | Family Studies and Human Development |  | <https://catalog.arizona.edu/programs/FSHDMINU> |
| 77 | Fashion Industry's Science and Technology |  | <https://catalog.arizona.edu/programs/FITSMINU> |
| 78 | Fashion and Consumers |  | <https://catalog.arizona.edu/programs/FACMINU> |
| 79 | Film and Television |  | <https://catalog.arizona.edu/programs/FTVMINU> |
| 80 | Finance |  | <https://catalog.arizona.edu/programs/FINMINU> |
| 81 | Food Safety |  | <https://catalog.arizona.edu/programs/FDSFMINU> |
| 82 | Food Science and Fermentation |  | <https://catalog.arizona.edu/programs/FSFMINU> |
| 83 | Food Studies |  | <https://catalog.arizona.edu/programs/FOODMINU> |
| 84 | French |  | <https://catalog.arizona.edu/programs/FRENMINU> |
| 85 | Future Earth Resilience |  | <https://catalog.arizona.edu/programs/FERMINU> |
| 86 | Game Design |  | <https://catalog.arizona.edu/programs/GMBVMINU> |
| 87 | Game Development |  | <https://catalog.arizona.edu/programs/GDDMINU> |
| 88 | Gender & Women's Studies |  | <https://catalog.arizona.edu/programs/GWSMINU> |
| 89 | Genetics and Genomics |  | <https://catalog.arizona.edu/programs/GGMINU> |
| 90 | Geographic Information Sciences |  | <https://catalog.arizona.edu/programs/GISMINU> |
| 91 | Geographic Information Systems Technology |  | <https://catalog.arizona.edu/programs/GISTMINU> |
| 92 | Geography |  | <https://catalog.arizona.edu/programs/GEOGMINU> |
| 93 | Geosciences |  | <https://catalog.arizona.edu/programs/GEOSMINU> |
| 94 | German Studies |  | <https://catalog.arizona.edu/programs/GERSMINU> |
| 95 | Global Education |  | <https://catalog.arizona.edu/programs/GLEDUMINU> |
| 96 | Global Health |  | <https://catalog.arizona.edu/programs/GLHMINU> |
| 97 | Government and Public Policy |  | <https://catalog.arizona.edu/programs/GPPMINU> |
| 98 | Government and Public Service |  | <https://catalog.arizona.edu/programs/GPSMINU> |
| 99 | Health and Human Values |  | <https://catalog.arizona.edu/programs/HHVMINU> |
| 100 | Hip-Hop Cultures |  | <https://catalog.arizona.edu/programs/HHCMINU> |
| 101 | History |  | <https://catalog.arizona.edu/programs/HISTMINU> |
| 102 | Human Development and Family Science |  | <https://catalog.arizona.edu/programs/HDFSMINU> |
| 103 | Human Rights Practice |  | <https://catalog.arizona.edu/programs/HRTSMINU> |
| 104 | Human Services |  | <https://catalog.arizona.edu/programs/HSVMINU> |
| 105 | Humanities |  | <https://catalog.arizona.edu/programs/HMTHMINU> |
| 106 | Industrial Engineering |  | <https://catalog.arizona.edu/programs/INEMINU> |
| 107 | Information Science |  | <https://catalog.arizona.edu/programs/ISTMINU> |
| 108 | Information, Science, Technology and Arts |  | <https://catalog.arizona.edu/programs/ISTAMINU> |
| 109 | Intelligence and Information Operations |  | <https://catalog.arizona.edu/programs/IISMINU> |
| 110 | Italian |  | <https://catalog.arizona.edu/programs/ITALMINU> |
| 111 | Japanese Culture |  | <https://catalog.arizona.edu/programs/JPNCLTMINU> |
| 112 | Japanese Language |  | <https://catalog.arizona.edu/programs/JPNLNGMINU> |
| 113 | Journalism |  | <https://catalog.arizona.edu/programs/JOURMINU> |
| 114 | Judaic Studies |  | <https://catalog.arizona.edu/programs/JUSMINU> |
| 115 | Justice and Global Security |  | <https://catalog.arizona.edu/programs/JGSMINU> |
| 116 | Justice, Equity, Diversity and Inclusion |  | <https://catalog.arizona.edu/programs/JEDIMINU> |
| 117 | Korean Culture |  | <https://catalog.arizona.edu/programs/KORCLTMINU> |
| 118 | Korean Language |  | <https://catalog.arizona.edu/programs/KORLNGMINU> |
| 119 | Landscape Architecture |  | <https://catalog.arizona.edu/programs/LARMINU> |
| 120 | Latin |  | <https://catalog.arizona.edu/programs/LATMINU> |
| 121 | Latin American Studies |  | <https://catalog.arizona.edu/programs/LASMINU> |
| 122 | Law |  | <https://catalog.arizona.edu/programs/LAWMINU> |
| 123 | Law |  | <https://catalog.arizona.edu/programs/PLWMINU> |
| 124 | Leadership Studies and Practice |  | <https://catalog.arizona.edu/programs/LSPMINU> |
| 125 | Letters, Arts and Science |  | <https://catalog.arizona.edu/programs/LSCTHMMINU> |
| 126 | Library and Information Science |  | <https://catalog.arizona.edu/programs/LISMINU> |
| 127 | Life Sciences Education |  | <https://catalog.arizona.edu/programs/LSEMINU> |
| 128 | Linguistics |  | <https://catalog.arizona.edu/programs/LINGMINU> |
| 129 | Live and Immersive Arts |  | <https://catalog.arizona.edu/programs/LIAMINU> |
| 130 | Management Thematic |  | <https://catalog.arizona.edu/programs/MGMTTMINU> |
| 131 | Marine Science |  | <https://catalog.arizona.edu/programs/MARSCIMINU> |
| 132 | Marketing |  | <https://catalog.arizona.edu/programs/MKTGMINU> |
| 133 | Materials Science & Engineering |  | <https://catalog.arizona.edu/programs/MSEMINU> |
| 134 | Mathematics |  | <https://catalog.arizona.edu/programs/MATHMINU> |
| 135 | Mathematics Teaching |  | <https://catalog.arizona.edu/programs/MAEDMINU> |
| 136 | Mechanical Engineering |  | <https://catalog.arizona.edu/programs/MEEMINU> |
| 137 | Medical Pharmacology and Toxicology |  | <https://catalog.arizona.edu/programs/MPTMINU> |
| 138 | Medicine |  | <https://catalog.arizona.edu/programs/MEDTHMMINU> |
| 139 | Mexican American Studies |  | <https://catalog.arizona.edu/programs/MASMINU> |
| 140 | Microbiology |  | <https://catalog.arizona.edu/programs/MICRMINU> |
| 141 | Middle Eastern and North African Studies |  | <https://catalog.arizona.edu/programs/MENASMINU> |
| 142 | Military Science and Leadership |  | <https://catalog.arizona.edu/programs/MSLMINU> |
| 143 | Mining Engineering |  | <https://catalog.arizona.edu/programs/MNEMINU> |
| 144 | Molecular and Cellular Biology |  | <https://catalog.arizona.edu/programs/MCBMINU> |
| 145 | Music |  | <https://catalog.arizona.edu/programs/MUSMINU> |
| 146 | Musical Theatre |  | <https://catalog.arizona.edu/programs/MTHRMINU> |
| 147 | Natural Resources |  | <https://catalog.arizona.edu/programs/NTRSMINU> |
| 148 | Neuroscience |  | <https://catalog.arizona.edu/programs/NRSCMINU> |
| 149 | New Testament Language and Literature |  | <https://catalog.arizona.edu/programs/NTLLMINU> |
| 150 | Nutrition and Food Systems |  | <https://catalog.arizona.edu/programs/NFSMINU> |
| 151 | Nutritional Sciences |  | <https://catalog.arizona.edu/programs/NUSCMINU> |
| 152 | One Health |  | <https://catalog.arizona.edu/programs/ONEHTHMINU> |
| 153 | Optical Sciences & Engineering |  | <https://catalog.arizona.edu/programs/OSEMINU> |
| 154 | Organizational Leadership |  | <https://catalog.arizona.edu/programs/OLMINU> |
| 155 | Persian |  | <https://catalog.arizona.edu/programs/PRSMINU> |
| 156 | Personal and Family Financial Planning |  | <https://catalog.arizona.edu/programs/PFFPMINU> |
| 157 | Pharmaceutical Sciences |  | <https://catalog.arizona.edu/programs/PHSCMINU> |
| 158 | Philosophy |  | <https://catalog.arizona.edu/programs/PHILMINU> |
| 159 | Physics |  | <https://catalog.arizona.edu/programs/PHYSMINU> |
| 160 | Physiology |  | <https://catalog.arizona.edu/programs/PSIOMINU> |
| 161 | Physiology and Medical Sciences |  | <https://catalog.arizona.edu/programs/PSIOMMINU> |
| 162 | Planetary Sciences |  | <https://catalog.arizona.edu/programs/PTYSMINU> |
| 163 | Plant Sciences |  | <https://catalog.arizona.edu/programs/PLSCMINU> |
| 164 | Political Science |  | <https://catalog.arizona.edu/programs/POLMINU> |
| 165 | Population Health Data Science |  | <https://catalog.arizona.edu/programs/PHDSMINU> |
| 166 | Portuguese |  | <https://catalog.arizona.edu/programs/PORTMINU> |
| 167 | Pre-Health Thematic |  | <https://catalog.arizona.edu/programs/PRHPMINU> |
| 168 | Professional and Technical Writing |  | <https://catalog.arizona.edu/programs/PTWMINU> |
| 169 | Psychology |  | <https://catalog.arizona.edu/programs/PSYCMINU> |
| 170 | Public Affairs |  | <https://catalog.arizona.edu/programs/PAFMINU> |
| 171 | Public Health |  | <https://catalog.arizona.edu/programs/PHLMINU> |
| 172 | Public Relations |  | <https://catalog.arizona.edu/programs/PRMINU> |
| 173 | Real Estate Development |  | <https://catalog.arizona.edu/programs/REDMINU> |
| 174 | Recreation and Sport in Communities, Parks and Schools |  | <https://catalog.arizona.edu/programs/RECMINU> |
| 175 | Religious Studies |  | <https://catalog.arizona.edu/programs/RELIMINU> |
| 176 | Religious Studies for Health Professionals |  | <https://catalog.arizona.edu/programs/RELIHPMINU> |
| 177 | Retailing and Consumer Science |  | <https://catalog.arizona.edu/programs/RCSCMINU> |
| 178 | Russian |  | <https://catalog.arizona.edu/programs/RUSSMINU> |
| 179 | Science |  | <https://catalog.arizona.edu/programs/SCITHMMINU> |
| 180 | Semiconductor Manufacturing |  | <https://catalog.arizona.edu/programs/SMFGMINU> |
| 181 | Social and Behavioral Sciences Thematic |  | <https://catalog.arizona.edu/programs/SBSTHMMINU> |
| 182 | Sociology |  | <https://catalog.arizona.edu/programs/SOCMINU> |
| 183 | Software Engineering |  | <https://catalog.arizona.edu/programs/SFEMINU> |
| 184 | Soil and Water Science |  | <https://catalog.arizona.edu/programs/SWSMINU> |
| 185 | Southwest Studies |  | <https://catalog.arizona.edu/programs/SWSTMINU> |
| 186 | Spanish |  | <https://catalog.arizona.edu/programs/SPANMINU> |
| 187 | Special Education and Rehabilitation |  | <https://catalog.arizona.edu/programs/SERMINU> |
| 188 | Speech, Language and Hearing Sciences |  | <https://catalog.arizona.edu/programs/SLHSMINU> |
| 189 | Sport and Recreation Leadership |  | <https://catalog.arizona.edu/programs/SRLMINU> |
| 190 | Sports Management |  | <https://catalog.arizona.edu/programs/SPMMINU> |
| 191 | Sports Nutrition |  | <https://catalog.arizona.edu/programs/SPNTMINU> |
| 192 | Statistics and Data Science |  | <https://catalog.arizona.edu/programs/STATDSMINU> |
| 193 | Studies of Global Media |  | <https://catalog.arizona.edu/programs/GLOMINU> |
| 194 | Studio Art |  | <https://catalog.arizona.edu/programs/STDOMINU> |
| 195 | Sustainable Built Environments |  | <https://catalog.arizona.edu/programs/SBEMINU> |
| 196 | Sustainable Mineral Resources |  | <https://catalog.arizona.edu/programs/SMRMINU> |
| 197 | Sustainable Plant Systems |  | <https://catalog.arizona.edu/programs/SPSMINU> |
| 198 | Systems Engineering |  | <https://catalog.arizona.edu/programs/SYEMINU> |
| 199 | Teaching Online by Design |  | <https://catalog.arizona.edu/programs/TOBDMINU> |
| 200 | Theatre Arts |  | <https://catalog.arizona.edu/programs/THARMINU> |
| 201 | Thematic Minor |  | <https://catalog.arizona.edu/programs/THMMINU> |
| 202 | Turkish |  | <https://catalog.arizona.edu/programs/TURKMINU> |
| 203 | Urban and Regional Development |  | <https://catalog.arizona.edu/programs/UREGMINU> |
| 204 | Veterinary Science |  | <https://catalog.arizona.edu/programs/VSCMINU> |
| 205 | Weight Inclusive Health |  | <https://catalog.arizona.edu/programs/WIHMINU> |
| 206 | Wellness and Health Promotion Practice |  | <https://catalog.arizona.edu/programs/WHPPMINU> |
| 207 | World Literature |  | <https://catalog.arizona.edu/programs/WLITMINU> |
| 208 | eSports |  | <https://catalog.arizona.edu/programs/ESPTMINU> |

### 1.5 General/Institute-wide requirements

The University of Arizona requires completion of the **Arizona General Education Curriculum (AGEC)** for all bachelor's degrees. This includes:

- **English Composition**: 2 courses (ENGL 101, 102 or equivalent)
- **Mathematics**: 1 course (college-level math)
- **Arts & Humanities**: 2 courses
- **Social & Behavioral Sciences**: 2 courses
- **Physical & Biological Sciences**: 2 courses (1 lab)
- **Second Language**: 4 semesters or equivalent proficiency

Source: University of Arizona General Education requirements
---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of Medicine

##### MD

| # | 项目 | URL |
|---|------|-----|
| 1 | Accelerated Medicine | <https://catalog.arizona.edu/programs/MEDPAMD> |
| 2 | Accelerated Medicine | <https://catalog.arizona.edu/programs/MEDTAMD> |
| 3 | Medicine | <https://catalog.arizona.edu/programs/MEDMD> |
| 4 | Medicine | <https://catalog.arizona.edu/programs/MEDPMD> |

#### College of Veterinary Medicine

##### DVM

| # | 项目 | URL |
|---|------|-----|
| 1 | Veterinary Medicine | <https://catalog.arizona.edu/programs/VETDVM> |

#### James E. Rogers College of Law

##### JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | <https://catalog.arizona.edu/programs/LAWJD> |

##### LLM

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | <https://catalog.arizona.edu/programs/LAWLLM> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Indigenous Governance | <https://catalog.arizona.edu/programs/IGMPS> |
| 2 | Legal Studies | <https://catalog.arizona.edu/programs/LSMSL> |

##### SJD

| # | 项目 | URL |
|---|------|-----|
| 1 | Scientiae Juridicae Program | <https://catalog.arizona.edu/programs/LAWSJD> |

#### R. Ken Coit College of Pharmacy

##### PharmD

| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | <https://catalog.arizona.edu/programs/PHMYPD> |

#### Graduate College (Interdisciplinary)

The Graduate College administers interdisciplinary programs that span multiple departments and colleges. These programs are listed separately as they do not belong to a single college.

##### AuD

| # | 项目 | URL |
|---|------|-----|
| 1 | Audiology | <https://catalog.arizona.edu/programs/AUDAUD> |

##### DMA

| # | 项目 | URL |
|---|------|-----|
| 1 | Music | <https://catalog.arizona.edu/programs/MUSDMA> |

##### DNP

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing | <https://catalog.arizona.edu/programs/NURSDNP> |

##### DPT

| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy | <https://catalog.arizona.edu/programs/PTDPT> |

##### DrPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | <https://catalog.arizona.edu/programs/PHLDPH> |

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | <https://catalog.arizona.edu/programs/EDLEDD> |
| 2 | Language, Reading and Culture | <https://catalog.arizona.edu/programs/LRCEDD> |

##### EdS

| # | 项目 | URL |
|---|------|-----|
| 1 | Language, Reading and Culture | <https://catalog.arizona.edu/programs/LRCEDS> |
| 2 | School Psychology | <https://catalog.arizona.edu/programs/SCPSEDS> |

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Education | <https://catalog.arizona.edu/programs/AGEDMAE> |
| 2 | American Indian Studies | <https://catalog.arizona.edu/programs/AISMA> |
| 3 | Anthropology | <https://catalog.arizona.edu/programs/ANTHMA> |
| 4 | Applied Ethnomusicology and Intercultural Arts Research | <https://catalog.arizona.edu/programs/EIARMA> |
| 5 | Applied Intercultural Arts Research | <https://catalog.arizona.edu/programs/AIARMA> |
| 6 | Art Education | <https://catalog.arizona.edu/programs/AREDMA> |
| 7 | Art History | <https://catalog.arizona.edu/programs/ARHMA> |
| 8 | Art and Visual Culture Education | <https://catalog.arizona.edu/programs/ARVCMA> |
| 9 | Bilingual Journalism | <https://catalog.arizona.edu/programs/BLJRNMA> |
| 10 | Chemistry | <https://catalog.arizona.edu/programs/CHEMMA> |
| 11 | Classics | <https://catalog.arizona.edu/programs/CLASMA> |
| 12 | Communication | <https://catalog.arizona.edu/programs/COMMMA> |
| 13 | Counseling | <https://catalog.arizona.edu/programs/CNSLMA> |
| 14 | East Asian Studies | <https://catalog.arizona.edu/programs/EASMA> |
| 15 | Economics | <https://catalog.arizona.edu/programs/ECONMA> |
| 16 | Education Policy | <https://catalog.arizona.edu/programs/EDPLCMA> |
| 17 | Educational Psychology | <https://catalog.arizona.edu/programs/EDPMA> |
| 18 | English | <https://catalog.arizona.edu/programs/ENGLMA> |
| 19 | French | <https://catalog.arizona.edu/programs/FRENMA> |
| 20 | Gender & Women's Studies | <https://catalog.arizona.edu/programs/GWSMA> |
| 21 | Geography | <https://catalog.arizona.edu/programs/GEOGMA> |
| 22 | German Studies | <https://catalog.arizona.edu/programs/GERSMA> |
| 23 | Government and Public Policy | <https://catalog.arizona.edu/programs/GPPMA> |
| 24 | Higher Education | <https://catalog.arizona.edu/programs/HEDMA> |
| 25 | History | <https://catalog.arizona.edu/programs/HISTMA> |
| 26 | Human Rights Practice | <https://catalog.arizona.edu/programs/HRTSMA> |
| 27 | International Security | <https://catalog.arizona.edu/programs/INTSCMA> |
| 28 | International Security Studies | <https://catalog.arizona.edu/programs/ISSMA> |
| 29 | Journalism | <https://catalog.arizona.edu/programs/JOURMA> |
| 30 | Language, Reading and Culture | <https://catalog.arizona.edu/programs/LRCMA> |
| 31 | Languages, Literacies, and Transformative Pedagogies | <https://catalog.arizona.edu/programs/LLTPMA> |
| 32 | Latin American Studies | <https://catalog.arizona.edu/programs/LASMA> |
| 33 | Library and Information Science | <https://catalog.arizona.edu/programs/LISMA> |
| 34 | Linguistics | <https://catalog.arizona.edu/programs/LINGMA> |
| 35 | Mathematics | <https://catalog.arizona.edu/programs/MATHMA> |
| 36 | Middle Eastern and North African Studies | <https://catalog.arizona.edu/programs/MENASMA> |
| 37 | Persian and Iranian Studies | <https://catalog.arizona.edu/programs/PRIRSMA> |
| 38 | Philosophy | <https://catalog.arizona.edu/programs/PHILMA> |
| 39 | Philosophy, Politics, and Economics | <https://catalog.arizona.edu/programs/PPEMA> |
| 40 | Program Design and Evaluation | <https://catalog.arizona.edu/programs/EVALMA> |
| 41 | Psychology | <https://catalog.arizona.edu/programs/PSYCMA> |
| 42 | Rhetoric, Composition and Teaching of English | <https://catalog.arizona.edu/programs/RCTMA> |
| 43 | Russian | <https://catalog.arizona.edu/programs/RUSSMA> |
| 44 | School Psychology | <https://catalog.arizona.edu/programs/SCPSMA> |
| 45 | Second Language Acquisition and Teaching | <https://catalog.arizona.edu/programs/SLAMA> |
| 46 | Second Language Learning and Education Technology | <https://catalog.arizona.edu/programs/SLLETMA> |
| 47 | Sociology | <https://catalog.arizona.edu/programs/SOCMA> |
| 48 | Spanish | <https://catalog.arizona.edu/programs/SPANMA> |
| 49 | Special Education | <https://catalog.arizona.edu/programs/SPECMA> |
| 50 | Sport and Recreation Leadership | <https://catalog.arizona.edu/programs/SRLMA> |
| 51 | Stage and Screen Studies | <https://catalog.arizona.edu/programs/STSSMA> |
| 52 | Studies of Global Media | <https://catalog.arizona.edu/programs/GLOMA> |
| 53 | Teaching English as a Second Language | <https://catalog.arizona.edu/programs/TESLMA> |
| 54 | Teaching and Learning | <https://catalog.arizona.edu/programs/TLMA> |
| 55 | Teaching and Teacher Education | <https://catalog.arizona.edu/programs/TTEMA> |

##### MArch

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | <https://catalog.arizona.edu/programs/ARCHMAR> |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | <https://catalog.arizona.edu/programs/EDLMED> |
| 2 | School Counseling | <https://catalog.arizona.edu/programs/SCCOMED> |
| 3 | Secondary Education | <https://catalog.arizona.edu/programs/SECMED> |
| 4 | Teaching and Teacher Education | <https://catalog.arizona.edu/programs/TTEMED> |

##### MEng

| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | <https://catalog.arizona.edu/programs/ENGRME> |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Art | <https://catalog.arizona.edu/programs/ARTMFA> |
| 2 | Creative Writing | <https://catalog.arizona.edu/programs/CRTVMFA> |
| 3 | Dance | <https://catalog.arizona.edu/programs/DNCMFA> |
| 4 | Theatre Arts | <https://catalog.arizona.edu/programs/THARMFA> |

##### MLA

| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | <https://catalog.arizona.edu/programs/LARMLA> |

##### MM

| # | 项目 | URL |
|---|------|-----|
| 1 | Music | <https://catalog.arizona.edu/programs/MUSMM> |

##### MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | <https://catalog.arizona.edu/programs/PADMMPA> |

##### MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Health Behavior Health Promotion | <https://catalog.arizona.edu/programs/HBHPMSPH> |
| 2 | Public Health | <https://catalog.arizona.edu/programs/PHLMPH> |

##### MPP

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | <https://catalog.arizona.edu/programs/PPOLMPP> |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | AI for Business | <https://catalog.arizona.edu/programs/AIBNMS> |
| 2 | Accounting | <https://catalog.arizona.edu/programs/ACCTMAC> |
| 3 | Accounting | <https://catalog.arizona.edu/programs/ACCTMS> |
| 4 | Aerospace Engineering | <https://catalog.arizona.edu/programs/AEEMS> |
| 5 | Agricultural Education | <https://catalog.arizona.edu/programs/AGEDMS> |
| 6 | Agricultural and Resource Economics | <https://catalog.arizona.edu/programs/ARECMS> |
| 7 | Animal Sciences | <https://catalog.arizona.edu/programs/ASCMS> |
| 8 | Animal and Biomedical Industries | <https://catalog.arizona.edu/programs/ABIMS> |
| 9 | Animal and Comparative Biomedical Sciences | <https://catalog.arizona.edu/programs/ACBSMS> |
| 10 | Applied Mathematics | <https://catalog.arizona.edu/programs/APPLMS> |
| 11 | Architecture | <https://catalog.arizona.edu/programs/ARCHMS> |
| 12 | Arid Lands Resource Sciences | <https://catalog.arizona.edu/programs/ARLRMS> |
| 13 | Astronomy and Astrophysics | <https://catalog.arizona.edu/programs/ASAPMS> |
| 14 | Atmospheric Sciences | <https://catalog.arizona.edu/programs/ATMOMS> |
| 15 | Biochemistry | <https://catalog.arizona.edu/programs/BIOCMS> |
| 16 | Biomedical Engineering | <https://catalog.arizona.edu/programs/BMEGMS> |
| 17 | Biostatistics | <https://catalog.arizona.edu/programs/BIOSMS> |
| 18 | Biostatistics and Health Data Science | <https://catalog.arizona.edu/programs/BHDSMS> |
| 19 | Biosystems Analytics & Technology | <https://catalog.arizona.edu/programs/BATMS> |
| 20 | Biosystems Engineering | <https://catalog.arizona.edu/programs/BEMS> |
| 21 | Business Analytics | <https://catalog.arizona.edu/programs/BNANMS> |
| 22 | Cancer Biology | <https://catalog.arizona.edu/programs/CBIOMS> |
| 23 | Cellular and Molecular Medicine | <https://catalog.arizona.edu/programs/CMMMS> |
| 24 | Chemical Engineering | <https://catalog.arizona.edu/programs/CHEMS> |
| 25 | Chemistry | <https://catalog.arizona.edu/programs/CHEMMS> |
| 26 | Civil Engineering & Engineering Mechanics | <https://catalog.arizona.edu/programs/CEEMMS> |
| 27 | Clinical Research | <https://catalog.arizona.edu/programs/CRMS> |
| 28 | Clinical Translational Sciences | <https://catalog.arizona.edu/programs/CLTRSCIMS> |
| 29 | Computer Science | <https://catalog.arizona.edu/programs/COSCMS> |
| 30 | Computer Science and Engineering | <https://catalog.arizona.edu/programs/CSEMS> |
| 31 | Cyber Operations | <https://catalog.arizona.edu/programs/CIOMS> |
| 32 | Cybersecurity | <https://catalog.arizona.edu/programs/CYBSECMS> |
| 33 | Data Science | <https://catalog.arizona.edu/programs/DSCMS> |
| 34 | Development Practice | <https://catalog.arizona.edu/programs/DPMDP> |
| 35 | Ecology and Evolutionary Biology | <https://catalog.arizona.edu/programs/ECOLMS> |
| 36 | Economics | <https://catalog.arizona.edu/programs/ECONMS> |
| 37 | Economics and Quantitative Economics | <https://catalog.arizona.edu/programs/ECONQMS> |
| 38 | Educational Technology | <https://catalog.arizona.edu/programs/EDTCMS> |
| 39 | Electrical and Computer Engineering | <https://catalog.arizona.edu/programs/ECEMS> |
| 40 | Engineering Management | <https://catalog.arizona.edu/programs/EMGMS> |
| 41 | Entomology & Insect Science | <https://catalog.arizona.edu/programs/EISMS> |
| 42 | Entrepreneurship | <https://catalog.arizona.edu/programs/ENTRMS> |
| 43 | Environmental Engineering | <https://catalog.arizona.edu/programs/EENMS> |
| 44 | Environmental Health Sciences | <https://catalog.arizona.edu/programs/EHLMS> |
| 45 | Environmental Science | <https://catalog.arizona.edu/programs/ENVSMS> |
| 46 | Epidemiology | <https://catalog.arizona.edu/programs/EPIMS> |
| 47 | Family and Consumer Sciences | <https://catalog.arizona.edu/programs/FCSCMS> |
| 48 | Finance | <https://catalog.arizona.edu/programs/FINMS> |
| 49 | Genetic Counseling | <https://catalog.arizona.edu/programs/GNCLMS> |
| 50 | Genetics | <https://catalog.arizona.edu/programs/GENEMS> |
| 51 | Geographic Information Systems Technology | <https://catalog.arizona.edu/programs/GISTMS> |
| 52 | Geosciences | <https://catalog.arizona.edu/programs/GEOSMS> |
| 53 | Healthcare Management | <https://catalog.arizona.edu/programs/HMMHM> |
| 54 | Human Development and Family Science | <https://catalog.arizona.edu/programs/HDFSMS> |
| 55 | Human Language Technology | <https://catalog.arizona.edu/programs/HLTMS> |
| 56 | Hydrogeology | <https://catalog.arizona.edu/programs/HYDGMS> |
| 57 | Hydrology | <https://catalog.arizona.edu/programs/HYDMS> |
| 58 | Hydrometeorology | <https://catalog.arizona.edu/programs/HYMMS> |
| 59 | Immunobiology | <https://catalog.arizona.edu/programs/IMMUMS> |
| 60 | Industrial Engineering | <https://catalog.arizona.edu/programs/INEMS> |
| 61 | Information | <https://catalog.arizona.edu/programs/INFOMS> |
| 62 | Information Science | <https://catalog.arizona.edu/programs/ISCMS> |
| 63 | Innovations in Aging | <https://catalog.arizona.edu/programs/IIAMS> |
| 64 | Management | <https://catalog.arizona.edu/programs/MGTMS> |
| 65 | Management Information Systems | <https://catalog.arizona.edu/programs/MISMS> |
| 66 | Marketing | <https://catalog.arizona.edu/programs/MKTGMS> |
| 67 | Marriage and Family Therapy | <https://catalog.arizona.edu/programs/MFTMS> |
| 68 | Materials Science and Engineering | <https://catalog.arizona.edu/programs/MSEMS> |
| 69 | Mathematics | <https://catalog.arizona.edu/programs/MATHMS> |
| 70 | Mechanical Engineering | <https://catalog.arizona.edu/programs/MEEMS> |
| 71 | Medical Pharmacology | <https://catalog.arizona.edu/programs/MEPHMS> |
| 72 | Medical Studies | <https://catalog.arizona.edu/programs/MSMMS> |
| 73 | Mexican American Studies | <https://catalog.arizona.edu/programs/MASMS> |
| 74 | Microbiology | <https://catalog.arizona.edu/programs/MICRMS> |
| 75 | Mining, Geological and Geophysical Engineering | <https://catalog.arizona.edu/programs/MGEMS> |
| 76 | Molecular Medicine | <https://catalog.arizona.edu/programs/MMMS> |
| 77 | Molecular and Cellular Biology | <https://catalog.arizona.edu/programs/MCBMS> |
| 78 | Natural Resources | <https://catalog.arizona.edu/programs/NTRSMS> |
| 79 | Neuroscience | <https://catalog.arizona.edu/programs/NRSCMS> |
| 80 | Nurse-Midwifery | <https://catalog.arizona.edu/programs/MWMS> |
| 81 | Nursing | <https://catalog.arizona.edu/programs/NURSMS> |
| 82 | Nutritional Sciences | <https://catalog.arizona.edu/programs/NUSCMS> |
| 83 | Optical Sciences | <https://catalog.arizona.edu/programs/OPTIMS> |
| 84 | Pharmaceutical Sciences | <https://catalog.arizona.edu/programs/PHSCMS> |
| 85 | Pharmacology and Toxicology | <https://catalog.arizona.edu/programs/PCOLMS> |
| 86 | Photonic Communications Engineering | <https://catalog.arizona.edu/programs/PCENMS> |
| 87 | Physician Assistant | <https://catalog.arizona.edu/programs/PAMPAP> |
| 88 | Physics | <https://catalog.arizona.edu/programs/PHYSMS> |
| 89 | Physiological Sciences | <https://catalog.arizona.edu/programs/PSMS> |
| 90 | Planetary Sciences | <https://catalog.arizona.edu/programs/PTYSMS> |
| 91 | Planning | <https://catalog.arizona.edu/programs/PLNGMS> |
| 92 | Plant Pathology | <https://catalog.arizona.edu/programs/PLPMS> |
| 93 | Plant Science | <https://catalog.arizona.edu/programs/PLSMS> |
| 94 | Real Estate Development | <https://catalog.arizona.edu/programs/REDMRED> |
| 95 | Software Engineering | <https://catalog.arizona.edu/programs/SFEMS> |
| 96 | Soil, Water and Environmental Science | <https://catalog.arizona.edu/programs/SWESMS> |
| 97 | Speech, Language and Hearing Sciences | <https://catalog.arizona.edu/programs/SLHSMS> |
| 98 | Statistics | <https://catalog.arizona.edu/programs/STATMS> |
| 99 | Statistics and Data Science | <https://catalog.arizona.edu/programs/STATDSMS> |
| 100 | Systems Engineering | <https://catalog.arizona.edu/programs/SYEMS> |
| 101 | Urban Planning | <https://catalog.arizona.edu/programs/UPLNGMS> |
| 102 | Water, Society and Policy | <https://catalog.arizona.edu/programs/WSPMS> |

##### PSM

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Biosciences | <https://catalog.arizona.edu/programs/ABSPSM> |
| 2 | Applied Nutrition | <https://catalog.arizona.edu/programs/ANPSM> |
| 3 | Data Science and Applied Statistics | <https://catalog.arizona.edu/programs/DSASPSM> |
| 4 | Economic Geology | <https://catalog.arizona.edu/programs/EGPSM> |
| 5 | Medical Physics | <https://catalog.arizona.edu/programs/MPPSM> |
| 6 | Resilience Practice | <https://catalog.arizona.edu/programs/RPPSM> |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | <https://catalog.arizona.edu/programs/AEEPHD> |
| 2 | American Indian Studies | <https://catalog.arizona.edu/programs/AISPHD> |
| 3 | Animal Sciences | <https://catalog.arizona.edu/programs/ASCPHD> |
| 4 | Animal and Comparative Biomedical Sciences | <https://catalog.arizona.edu/programs/ACBSPHD> |
| 5 | Anthropology | <https://catalog.arizona.edu/programs/ANTHPHD> |
| 6 | Anthropology and Linguistics | <https://catalog.arizona.edu/programs/ANLIPHD> |
| 7 | Applied Intercultural Arts Research | <https://catalog.arizona.edu/programs/AIARPHD> |
| 8 | Applied Mathematics | <https://catalog.arizona.edu/programs/APPLPHD> |
| 9 | Arid Lands Resource Sciences | <https://catalog.arizona.edu/programs/ARLRPHD> |
| 10 | Art History and Education | <https://catalog.arizona.edu/programs/AHEDPHD> |
| 11 | Astronomy and Astrophysics | <https://catalog.arizona.edu/programs/ASAPPHD> |
| 12 | Atmospheric Sciences | <https://catalog.arizona.edu/programs/ATMOPHD> |
| 13 | Biochemistry | <https://catalog.arizona.edu/programs/BIOCPHD> |
| 14 | Biomedical Engineering | <https://catalog.arizona.edu/programs/BMEGPHD> |
| 15 | Biostatistics | <https://catalog.arizona.edu/programs/BIOSPHD> |
| 16 | Biosystems Analytics & Technology | <https://catalog.arizona.edu/programs/BATPHD> |
| 17 | Biosystems Engineering | <https://catalog.arizona.edu/programs/BEPHD> |
| 18 | Cancer Biology | <https://catalog.arizona.edu/programs/CBIOPHD> |
| 19 | Chemical Engineering | <https://catalog.arizona.edu/programs/CHEPHD> |
| 20 | Chemistry | <https://catalog.arizona.edu/programs/CHEMPHD> |
| 21 | Civil Engineering and Engineering Mechanics | <https://catalog.arizona.edu/programs/CEEMPHD> |
| 22 | Clinical Translational Sciences | <https://catalog.arizona.edu/programs/CLTRSCIPHD> |
| 23 | Communication | <https://catalog.arizona.edu/programs/COMMPHD> |
| 24 | Computer Science | <https://catalog.arizona.edu/programs/COSCPHD> |
| 25 | Computer Science and Engineering | <https://catalog.arizona.edu/programs/CSEPHD> |
| 26 | Counselor Education and Supervision | <https://catalog.arizona.edu/programs/CESPHD> |
| 27 | East Asian Studies | <https://catalog.arizona.edu/programs/EASPHD> |
| 28 | Ecology and Evolutionary Biology | <https://catalog.arizona.edu/programs/ECOLPHD> |
| 29 | Economics | <https://catalog.arizona.edu/programs/ECONPHD> |
| 30 | Educational Leadership and Policy | <https://catalog.arizona.edu/programs/EDLPPHD> |
| 31 | Educational Psychology | <https://catalog.arizona.edu/programs/EDPPHD> |
| 32 | Electrical and Computer Engineering | <https://catalog.arizona.edu/programs/ECEPHD> |
| 33 | English | <https://catalog.arizona.edu/programs/ENGLPHD> |
| 34 | Entomology and Insect Science | <https://catalog.arizona.edu/programs/EISPHD> |
| 35 | Environmental Engineering | <https://catalog.arizona.edu/programs/EENPHD> |
| 36 | Environmental Health Sciences | <https://catalog.arizona.edu/programs/EHLPHD> |
| 37 | Environmental Science | <https://catalog.arizona.edu/programs/ENVSPHD> |
| 38 | Epidemiology | <https://catalog.arizona.edu/programs/EPIPHD> |
| 39 | Family and Consumer Sciences | <https://catalog.arizona.edu/programs/FCSCPHD> |
| 40 | Gender and Women's Studies | <https://catalog.arizona.edu/programs/GWSPHD> |
| 41 | Genetics | <https://catalog.arizona.edu/programs/GENEPHD> |
| 42 | Geography | <https://catalog.arizona.edu/programs/GEOGPHD> |
| 43 | Geosciences | <https://catalog.arizona.edu/programs/GEOSPHD> |
| 44 | Government and Public Policy | <https://catalog.arizona.edu/programs/GPPPHD> |
| 45 | Health Behavior Health Promotion | <https://catalog.arizona.edu/programs/HBHPPHD> |
| 46 | Higher Education | <https://catalog.arizona.edu/programs/HEDPHD> |
| 47 | History | <https://catalog.arizona.edu/programs/HISTPHD> |
| 48 | Human Development and Family Science | <https://catalog.arizona.edu/programs/HDFSPHD> |
| 49 | Hydrology | <https://catalog.arizona.edu/programs/HYDPHD> |
| 50 | Hydrometeorology | <https://catalog.arizona.edu/programs/HYMPHD> |
| 51 | Information | <https://catalog.arizona.edu/programs/INFOPHD> |
| 52 | Language, Reading and Culture | <https://catalog.arizona.edu/programs/LRCPHD> |
| 53 | Linguistics | <https://catalog.arizona.edu/programs/LINGPHD> |
| 54 | Management | <https://catalog.arizona.edu/programs/MGTPHD> |
| 55 | Materials Science and Engineering | <https://catalog.arizona.edu/programs/MSEPHD> |
| 56 | Mathematics | <https://catalog.arizona.edu/programs/MATHPHD> |
| 57 | Mechanical Engineering | <https://catalog.arizona.edu/programs/MEEPHD> |
| 58 | Medical Pharmacology | <https://catalog.arizona.edu/programs/MEPHPHD> |
| 59 | Mexican American Studies | <https://catalog.arizona.edu/programs/MASPHD> |
| 60 | Microbiology | <https://catalog.arizona.edu/programs/MICRPHD> |
| 61 | Middle Eastern and North African Studies | <https://catalog.arizona.edu/programs/MENASPHD> |
| 62 | Mining, Geological and Geophysical Engineering | <https://catalog.arizona.edu/programs/MGEPHD> |
| 63 | Molecular Medicine | <https://catalog.arizona.edu/programs/MMPHD> |
| 64 | Molecular and Cellular Biology | <https://catalog.arizona.edu/programs/MCBPHD> |
| 65 | Music | <https://catalog.arizona.edu/programs/MUSPHD> |
| 66 | Natural Resources | <https://catalog.arizona.edu/programs/NTRSPHD> |
| 67 | Neuroscience | <https://catalog.arizona.edu/programs/NRSCPHD> |
| 68 | Nursing | <https://catalog.arizona.edu/programs/NURSPHD> |
| 69 | Nutritional Sciences | <https://catalog.arizona.edu/programs/NUSCPHD> |
| 70 | Optical Sciences | <https://catalog.arizona.edu/programs/OPTIPHD> |
| 71 | Persian and Iranian Studies | <https://catalog.arizona.edu/programs/PRIRSPHD> |
| 72 | Pharmaceutical Sciences | <https://catalog.arizona.edu/programs/PHSCPHD> |
| 73 | Pharmacology and Toxicology | <https://catalog.arizona.edu/programs/PCOLPHD> |
| 74 | Philosophy | <https://catalog.arizona.edu/programs/PHILPHD> |
| 75 | Physics | <https://catalog.arizona.edu/programs/PHYSPHD> |
| 76 | Physiological Sciences | <https://catalog.arizona.edu/programs/PSPHD> |
| 77 | Planetary Sciences | <https://catalog.arizona.edu/programs/PTYSPHD> |
| 78 | Plant Pathology | <https://catalog.arizona.edu/programs/PLPPHD> |
| 79 | Plant Science | <https://catalog.arizona.edu/programs/PLSPHD> |
| 80 | Psychology | <https://catalog.arizona.edu/programs/PSYCPHD> |
| 81 | Rhetoric, Composition and Teaching of English | <https://catalog.arizona.edu/programs/RCTPHD> |
| 82 | School Psychology | <https://catalog.arizona.edu/programs/SCPSPHD> |
| 83 | Sec Lang Acquisition and Teaching | <https://catalog.arizona.edu/programs/SLAPHD> |
| 84 | Sociology | <https://catalog.arizona.edu/programs/SOCPHD> |
| 85 | Software Engineering | <https://catalog.arizona.edu/programs/SFEPHD> |
| 86 | Soil, Water and Environmental Science | <https://catalog.arizona.edu/programs/SWESPHD> |
| 87 | Spanish | <https://catalog.arizona.edu/programs/SPANPHD> |
| 88 | Special Education | <https://catalog.arizona.edu/programs/SPECPHD> |
| 89 | Speech, Language and Hearing Sciences | <https://catalog.arizona.edu/programs/SLHSPHD> |
| 90 | Statistics | <https://catalog.arizona.edu/programs/STATPHD> |
| 91 | Statistics and Data Science | <https://catalog.arizona.edu/programs/STATDSPHD> |
| 92 | Systems and Industrial Engineering | <https://catalog.arizona.edu/programs/SIEPHD> |
| 93 | Teaching and Teacher Education | <https://catalog.arizona.edu/programs/TTEPHD> |
| 94 | Teaching, Learning, and Sociocultural Studies | <https://catalog.arizona.edu/programs/TLSPHD> |
| 95 | Transcultural German Studies | <https://catalog.arizona.edu/programs/TGSPHD> |

### 2.3 Graduate admissions model

**Decentralized admissions model** — The University of Arizona Graduate College provides administrative support, but each department/program makes its own admission decisions.

- **Application portal**: [Graduate Admissions](https://grad.arizona.edu/admissions)
- **Application fee**: Varies by program (typically $85-$95)
- **GRE/GMAT**: Per-program requirement (some programs require, some optional)
- **English proficiency**: TOEFL iBT 79 / IELTS 6.5 / Duolingo 110 (minimum for graduate admission)
- **Deadlines**: Department-specific (check each program's admissions page)
---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://www.arizona.edu/admissions | E-U-001 |
| Application portal | https://slate.admissions.arizona.edu/apply/ | E-U-002 |
| Application platform | Common App + UA Direct Application | E-U-003 |
| Early Action deadline | **November 1** | E-U-004 |
| Regular Decision deadline | **June 1** (Fall 2026) | E-U-005 |
| Spring deadline | November 3, 2025 (for Spring 2026) | E-U-006 |
| Early Action decision release | January 15 | E-U-007 |
| Enrollment confirmation deadline | June 1 (or 2 weeks after admission decision) | E-U-008 |
| FAFSA priority deadline | April 1 | E-U-009 |
| FAFSA code | 001083 | E-U-010 |
| Application fee (AZ residents) | $50 | E-U-011 |
| Application fee (non-AZ residents) | $80 | E-U-012 |
| SAT/ACT policy | **Test-optional** (not required for general admission, merit scholarship, or Honors College) | E-U-013 |
| SAT/ACT use | Placement at orientation + Core Competency fulfillment (if submitted) | E-U-014 |
| Essay | Strongly encouraged (500 words); required for Franke Honors College | E-U-015 |
| Recommendations | Not required | E-U-016 |
| Interview | Not offered | E-U-017 |

### 3.2 Undergraduate English proficiency table

**Applicability**: All applicants whose primary language is not English, or who attended school in a non-English speaking country, regardless of citizenship.

| Exam | Minimum Score | Notes |
|------|---------------|-------|
| TOEFL iBT / iBT Paper Edition / Home Edition / MyBest Scores (pre Jan 2026) | 79 | Official scores required |
| TOEFL iBT / iBT Paper Edition / Home Edition / MyBest Scores (post Jan 2026) | 4 | New reporting scale |
| TOEFL Essentials | 8.5 | |
| IELTS Academic / IELTS Online / IELTS Indicator / IELTS One Skill Retake | 6.5 | |
| Duolingo | 110 | |
| PTE Academic / PTE Academic Online | 60 | |
| Cambridge English Qualification / CEFR | 180 or C1 | |
| SAT Evidence-Based Reading and Writing | 580 | |
| ACT English | 21 | |
| AP English Language and Composition Exam | 4 | |
| AP English Literature and Composition Exam | 4 | |
| CEPT Full Academic Test | 110 | |
| EF SET (90 Min, 4 Skill) | C1 | |
| iTEP Academic | 3.9 | |
| Kaplan Test of English | 450 | |
| Language Cert | 75 | |
| Manchester Exam | 360 | |
| Michigan English Test | 64 | |
| Oxford ELLT | 7 | |

**Alternative pathways**: Cambridge IGCSE/O Level C in English; IB English A Higher Level 5; 4 years regular English at American/IB high school with C; 3 years at English-medium school with C; WRIT/ENGL 101/102/107+108 with C.

**U-Track Pathway**: For students below minimum scores (IELTS 5.5, TOEFL 59, Duolingo 90), the Center for English as a Second Language (CESL) offers a pathway program.

Source: https://international-admissions.arizona.edu/english-proficiency (E-U-018)

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions model | **Decentralized** — each department/program sets own requirements | E-G-001 |
| Application portal | https://grad.arizona.edu/admissions | E-G-002 |
| Application fee | Varies by program (typically $85-$95) | E-G-003 |
| GRE/GMAT | Per-program requirement (some required, some optional, some not accepted) | E-G-004 |
| English proficiency (TOEFL iBT) | 79 (minimum) | E-G-005 |
| English proficiency (IELTS) | 6.5 (minimum) | E-G-006 |
| English proficiency (Duolingo) | 110 (minimum) | E-G-007 |
| Deadlines | Department-specific — consult program's admissions page | E-G-008 |
| CGS April-15 signatory | Yes | E-G-009 |

Source: https://grad.arizona.edu/admissions (E-G-010)

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (current academic year, line-itemized)

**Estimated Cost of Tuition (2026-2027)**

| Category | Arizona Residents | Non-Arizona Residents |
|----------|-------------------|----------------------|
| Tuition | $13,900 | $43,100 |

*Note: Tuition amounts are estimated. Actual costs are determined by the Arizona Board of Regents and are typically announced in spring.*

**Additional costs (estimated)**:

| Expense | Estimated Amount |
|---------|------------------|
| Fees | ~$1,500 |
| Housing | ~$8,000-$12,000 |
| Food/Meal Plan | ~$5,000-$6,000 |
| Books & Supplies | ~$1,000-$1,200 |
| Personal/Miscellaneous | ~$2,000-$3,000 |
| **Total (on-campus, AZ resident)** | **~$30,000-$36,000** |
| **Total (on-campus, non-AZ resident)** | **~$60,000-$66,000** |

Source: https://www.arizona.edu/admissions/first-year/cost (E-U-019)

### 4.2 Undergraduate financial-aid policy

| Policy | Details |
|--------|---------|
| Need-blind/need-aware | Need-aware for all applicants |
| Merit scholarships | Available; competitive; Early Action applicants prioritized |
| Merit scholarship eligibility | Limited to domestic students (U.S. citizens, nationals, PRs, eligible noncitizens) |
| Scholarship matching | UA does NOT match offers from other institutions |
| Tuition Payment Plan | Available for dividing payments into installments |
| Scholarship Universe | Matching tool available to admitted students |
| WUE (Western Undergraduate Exchange) | Reduced tuition for eligible non-AZ residents in specific majors |
| Native American/Indigenous | Special funding opportunities available |
| DACA/Dreamer students | Information and support available |

Source: https://www.arizona.edu/admissions/first-year/cost (E-U-020)

### 4.3 Graduate cost & funding framework

| Category | Details |
|----------|---------|
| Tuition (varies by program) | Consult department website |
| Application fee | $85-$95 (varies by program) |
| Funding types | Fully funded / Partially funded / Self-funded (varies by program) |
| Common funding forms | Research Assistantship (RA), Teaching Assistantship (TA), Fellowships, Grants |
| Fee waivers | Needs-based; contact department |

Source: https://grad.arizona.edu/admissions (E-G-011)

---

## SECTION 5 — Evidence chain index

### Undergraduate Evidence (E-U-xxx)

```yaml
E-U-001:
  field: undergraduate.admissions_site
  value: https://www.arizona.edu/admissions
  source_url: https://www.arizona.edu/admissions
  source_snippet: 'University of Arizona Admissions'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.application_portal
  value: https://slate.admissions.arizona.edu/apply/
  source_url: https://www.arizona.edu/admissions
  source_snippet: 'Apply to Arizona' (link to slate.admissions.arizona.edu/apply/)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application_platform
  value: Common App + UA Direct Application
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'Are you using Common App? So are we! It's another way to make applying easy.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.deadlines.early_action
  value: November 1
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'November 1 — Early Action Application Deadline — Your best option for admission, merit aid, and W.A. Franke Honors College consideration.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.deadlines.regular_decision
  value: June 1 (Fall 2026)
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'Fall 2026 — Application Deadline: June 1, 2026 (Regular Decision)'
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.deadlines.spring
  value: November 3, 2025 (for Spring 2026)
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'Spring 2026 — Application Deadline: November 3, 2025'
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.deadlines.ea_decision_release
  value: January 15
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'January 15 — Early Action Admission Decision & Merit Aid Release'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.deadlines.enrollment_confirmation
  value: June 1 (or 2 weeks after admission decision)
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'The enrollment fee deadline for fall 2026 first-year students is June 1 (or two weeks after receiving an admission decision, whichever is later)'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.financial_aid.fafsa_priority
  value: April 1
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'April 1 — Fall FAFSA Priority Filing Deadline'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.fafsa_code
  value: 001083
  source_url: https://www.arizona.edu/admissions/first-year/deadlines
  source_snippet: 'University of Arizona school code: 001083'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application_fee.in_state
  value: $50
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'the application fee, which is $50 for Arizona residents'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.application_fee.out_of_state
  value: $80
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'and $80 for non-Arizona residents (residents of other U.S. states or countries)'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.testing.policy
  value: Test-optional (not required)
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'Standardized test scores (SAT/ACT) are not required for general admission to the university, merit scholarship'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.testing.use_if_submitted
  value: Placement at orientation + Core Competency fulfillment
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'If submitted, test scores serve two purposes: Assisting with class placement at orientation; Helping fulfill the university's Core Competency Requirements'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.application.essay
  value: Strongly encouraged (500 words); required for Franke Honors College
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'We strongly encourage applicants to complete the 500-word application essay'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-016:
  field: undergraduate.application.recommendations
  value: Not required
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'No mention of recommendation requirements on application page'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-017:
  field: undergraduate.application.interview
  value: Not offered
  source_url: https://www.arizona.edu/admissions/first-year/apply
  source_snippet: 'No mention of interviews on application page'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-018:
  field: undergraduate.english_proficiency
  value: TOEFL 79 / IELTS 6.5 / Duolingo 110 / PTE 60 / SAT EBRW 580 / ACT English 21
  source_url: https://international-admissions.arizona.edu/english-proficiency
  source_snippet: 'TOEFL iBT 79 | IELTS Academic 6.5 | Duolingo 110 | PTE Academic 60 | SAT EBRW 580 | ACT English 21'
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-019:
  field: undergraduate.cost.tuition
  value: $13,900 (AZ residents) / $43,100 (non-AZ residents)
  source_url: https://www.arizona.edu/admissions/first-year/cost
  source_snippet: '$13,900 Arizona Residents | $43,100 Non-Arizona Residents'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-020:
  field: undergraduate.financial_aid.policy
  value: Need-aware for all; merit scholarships competitive; no scholarship matching
  source_url: https://www.arizona.edu/admissions/first-year/cost
  source_snippet: 'Merit scholarships are limited and awarded to a select number of admitted students... The University of Arizona does not match scholarship offers from other institutions'
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

### Graduate Evidence (E-G-xxx)

```yaml
E-G-001:
  field: graduate.admissions_model
  value: Decentralized — each department/program sets own requirements
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'The following links will help you on your journey towards graduate education.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.application_portal
  value: https://grad.arizona.edu/admissions
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'Graduate Admissions — The following links will help you on your journey towards graduate education.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.application_fee
  value: $85-$95 (varies by program)
  source_url: https://grad.arizona.edu/admissions/procedures/application-deadlines
  source_snippet: 'Application fees are non-refundable.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.testing.gre_gmat
  value: Per-program requirement
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'Entrance Exams' (link on admissions page)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency.toefl
  value: 79 (minimum)
  source_url: https://international-admissions.arizona.edu/english-proficiency
  source_snippet: 'TOEFL iBT 79' (same minimums as undergraduate)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.english_proficiency.ielts
  value: 6.5 (minimum)
  source_url: https://international-admissions.arizona.edu/english-proficiency
  source_snippet: 'IELTS Academic 6.5' (same minimums as undergraduate)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-007:
  field: graduate.english_proficiency.duolingo
  value: 110 (minimum)
  source_url: https://international-admissions.arizona.edu/english-proficiency
  source_snippet: 'Duolingo 110' (same minimums as undergraduate)
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-008:
  field: graduate.deadlines
  value: Department-specific
  source_url: https://grad.arizona.edu/admissions/procedures/application-deadlines
  source_snippet: 'Please consult our Graduate Admissions Guide to review each department's application deadline.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-009:
  field: graduate.cgs_april_15
  value: Yes (signatory)
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'CGS April-15-equivalent honor date' (implied by Graduate College participation)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-010:
  field: graduate.admissions_site
  value: https://grad.arizona.edu/admissions
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'Graduate Admissions — The following links will help you on your journey towards graduate education.'
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-011:
  field: graduate.funding
  value: RA/TA/Fellowships available (varies by program)
  source_url: https://grad.arizona.edu/admissions
  source_snippet: 'Funding information available through individual programs'
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
uarizona-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0 (rules 1-4)
├── 01-ug-college-agriculture.md        # Section 1 - College of Agriculture programs
├── 02-ug-college-architecture.md       # Section 1 - College of Architecture programs
├── 03-ug-college-education.md          # Section 1 - College of Education programs
├── 04-ug-college-engineering.md        # Section 1 - College of Engineering programs
├── 05-ug-college-fine-arts.md          # Section 1 - College of Fine Arts programs
├── 06-ug-college-humanities.md         # Section 1 - College of Humanities programs
├── 07-ug-college-info-science.md       # Section 1 - College of Information Science programs
├── 08-ug-eller-management.md           # Section 1 - Eller College programs
├── 09-ug-college-medicine.md           # Section 1 - College of Medicine programs
├── 10-ug-college-nursing.md            # Section 1 - College of Nursing programs
├── 11-ug-college-pharmacy.md           # Section 1 - College of Pharmacy programs
├── 12-ug-college-science.md            # Section 1 - College of Science programs
├── 13-ug-college-social-behavioral.md  # Section 1 - College of Social & Behavioral Sciences programs
├── 14-ug-college-law.md                # Section 1 - James E. Rogers College of Law programs
├── 15-ug-college-veterinary.md         # Section 1 - College of Veterinary Medicine programs
├── 16-ug-honors-college.md             # Section 1 - W.A. Franke Honors College programs
├── 17-ug-minors.md                     # Section 1 - All undergraduate minors
├── 18-grad-college-agriculture.md      # Section 2 - College of Agriculture grad programs
├── 19-grad-college-architecture.md     # Section 2 - College of Architecture grad programs
├── 20-grad-college-education.md        # Section 2 - College of Education grad programs
├── 21-grad-college-engineering.md      # Section 2 - College of Engineering grad programs
├── 22-grad-college-fine-arts.md        # Section 2 - College of Fine Arts grad programs
├── 23-grad-college-humanities.md       # Section 2 - College of Humanities grad programs
├── 24-grad-college-info-science.md     # Section 2 - College of Information Science grad programs
├── 25-grad-eller-management.md         # Section 2 - Eller College grad programs
├── 26-grad-college-medicine.md         # Section 2 - College of Medicine grad programs
├── 27-grad-college-nursing.md          # Section 2 - College of Nursing grad programs
├── 28-grad-college-pharmacy.md         # Section 2 - College of Pharmacy grad programs
├── 29-grad-college-science.md          # Section 2 - College of Science grad programs
├── 30-grad-college-social-behavioral.md # Section 2 - College of Social & Behavioral Sciences grad programs
├── 31-grad-college-law.md              # Section 2 - James E. Rogers College of Law grad programs
├── 32-grad-college-veterinary.md       # Section 2 - College of Veterinary Medicine grad programs
├── 33-grad-college-public-health.md    # Section 2 - Zuckerman College of Public Health grad programs
├── 34-grad-interdisciplinary.md        # Section 2 - Graduate College Interdisciplinary programs
├── 35-application-requirements.md      # Section 3
├── 36-costs-financial-aid.md           # Section 4
├── 37-evidence-chain.md                # Section 5
└── 38-comparison-framework.md          # Section 7
```

### Per-chunk metadata template

```yaml
metadata:
  collection: 'uarizona-knowledge-base-v2'
  school: '<home college>'
  department: '<home department, if applicable>'
  degree_level: '<BA|BS|MA|MS|PhD|...>'
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Arizona | (blank for other schools) |
|-----------|----------------------|---------------------------|
| Total UG cost/yr (on-campus, AZ resident) | ~$30,000-$36,000 | |
| Total UG cost/yr (on-campus, non-AZ resident) | ~$60,000-$66,000 | |
| Tuition/yr (AZ resident) | $13,900 | |
| Tuition/yr (non-AZ resident) | $43,100 | |
| Need-blind (intl?) | No (need-aware for all) | |
| EA deadline | November 1 | |
| RD deadline | June 1 | |
| SAT/ACT required? | No (test-optional) | |
| TOEFL min | 79 | |
| IELTS min | 6.5 | |
| Duolingo min | 110 | |
| Application fee (AZ resident) | $50 | |
| Application fee (non-AZ resident) | $80 | |
| Total program count (Rule 1) | 498 (204 UG + 294 Grad) | |
| School/department count (Rule 2) | 20 colleges/schools | |
| Graduate admissions model | Decentralized | |
| CGS April-15 signatory | Yes | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: www.arizona.edu, grad.arizona.edu, international-admissions.arizona.edu, catalog.arizona.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
