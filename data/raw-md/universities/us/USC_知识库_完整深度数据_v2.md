# University of Southern California (USC) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BArch/BM/BSW) | 229 |
| 本科辅修 (Minor) | 267 |
| 研究生学位项目 (MA/MS/MBA/PhD/EdD/JD/MD/PharmD/etc.) | 484 |
| 研究生高级证书 (Advanced Certificate / Diploma) | 169 |
| **学位项目总计 (UG + Grad)** | **713** |
| **全部项目总计 (含辅修和证书)** | **1149** |
| 学院 / 独立系所总数 | 23 |

### 0.2 学院 / 系层级结构

USC
├── USC Dana and David Dornsife College of Letters, Arts and Sciences [学院]
│   ├── Natural Sciences (Biology, Chemistry, Physics, Mathematics, etc.) [系]
│   ├── Social Sciences (Economics, Political Science, Psychology, Sociology, etc.) [系]
│   ├── Humanities (English, History, Philosophy, Comparative Literature, etc.) [系]
│   ├── Arts (Fine Arts, Art History, etc.) [系]
│   └── Interdisciplinary Programs (312 programs - largest school) [系]
├── USC Marshall School of Business [学院]
│   ├── Business Administration [系]
│   ├── Accounting (shared with Leventhal) [系]
│   ├── Finance and Business Economics [系]
│   ├── Management and Organization [系]
│   ├── Marketing [系]
│   ├── Data Sciences and Operations [系]
│   └── Lloyd Greif Center for Entrepreneurial Studies [系]
├── USC Viterbi School of Engineering [学院]
│   ├── Computer Science [系]
│   ├── Electrical and Computer Engineering [系]
│   ├── Aerospace and Mechanical Engineering [系]
│   ├── Biomedical Engineering [系]
│   ├── Civil and Environmental Engineering [系]
│   ├── Industrial and Systems Engineering [系]
│   ├── Chemical Engineering and Materials Science [系]
│   ├── Astronautical Engineering [系]
│   ├── Information Technology Program [系]
│   └── USC Stevens School of Computing and AI [系] ⚠ programs still under Viterbi in catalogue
├── USC Annenberg School for Communication and Journalism [学院]
│   ├── Communication [系]
│   ├── Journalism [系]
│   └── Public Relations and Advertising [系]
├── Keck School of Medicine of USC [学院]
│   ├── Biomedical Sciences [系]
│   ├── Clinical Sciences [系]
│   ├── Preventive Medicine [系]
│   ├── Pathology [系]
│   └── Population and Public Health Sciences [系]
├── USC Gould School of Law [学院]
│   ├── Law [系]
│   └── Alternative Dispute Resolution [系]
├── USC Thornton School of Music [学院]
│   ├── Classical Performance [系]
│   ├── Jazz Studies [系]
│   ├── Composition [系]
│   ├── Music Industry [系]
│   └── Music Education [系]
├── USC Alfred E. Mann School of Pharmacy and Pharmaceutical Sciences [学院]
│   ├── Pharmacy [系]
│   ├── Pharmaceutical Sciences [系]
│   └── Regulatory Science [系]
├── USC Sol Price School of Public Policy [学院]
│   ├── Public Policy [系]
│   ├── Public Administration [系]
│   ├── Urban Planning [系]
│   └── Health Administration [系]
├── USC School of Cinematic Arts [学院]
│   ├── Film and Television Production [系]
│   ├── Cinema and Media Studies [系]
│   ├── Interactive Media and Games [系]
│   ├── Animation and Digital Arts [系]
│   └── Writing for Screen and Television [系]
├── USC Rossier School of Education [学院]
│   ├── Education [系]
│   └── Educational Leadership [系]
├── USC Suzanne Dworak-Peck School of Social Work [学院]
│   ├── Social Work [系]
│   └── Military Social Work [系]
├── USC School of Architecture [学院]
│   ├── Architecture [系]
│   ├── Landscape Architecture [系]
│   └── Heritage Conservation [系]
├── USC Leonard Davis School of Gerontology [学院]
│   ├── Gerontology [系]
│   └── Lifespan Health [系]
├── Herman Ostrow School of Dentistry of USC [学院]
│   ├── Dentistry [系]
│   └── Dental Hygiene [系]
├── USC Independent Health Professions at Ostrow [学院]
│   ├── Biokinesiology [系]
│   ├── Occupational Therapy [系]
│   └── Physical Therapy [系]
├── USC Roski School of Art and Design [学院]
│   ├── Fine Arts [系]
│   ├── Design [系]
│   └── Art History [系]
├── USC School of Dramatic Arts [学院]
│   ├── Acting [系]
│   ├── Design [系]
│   └── Theatre [系]
├── USC Glorya Kaufman School of Dance [学院]
│   └── Dance [系]
├── USC Leventhal School of Accounting [学院]
│   └── Accounting [系]
├── USC Iovine and Young Academy [学院]
│   ├── Arts, Technology and Business of Innovation [系]
│   └── Design [系]
├── USC Bovard College [学院]
│   └── Professional Studies [系]
└── Office of the Provost [学院]
    └── Neuroscience [系] ⚠ shared across multiple schools

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本校数量 |
|---------|------|------|---------|
| BA | Bachelor of Arts | 本科 | 82 |
| BS | Bachelor of Science | 本科 | 95 |
| BFA | Bachelor of Fine Arts | 本科 | 15 |
| BArch | Bachelor of Architecture | 本科 | 1 |
| BM | Bachelor of Music | 本科 | 13 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| Minor | 辅修 | 本科 | 264 |
| MA | Master of Arts | 研究生 | 46 |
| MS | Master of Science | 研究生 | 169 |
| MFA | Master of Fine Arts | 研究生 | 10 |
| MBA | Master of Business Administration | 研究生 | 5 |
| MArch | Master of Architecture | 研究生 | 1 |
| MM | Master of Music | 研究生 | 18 |
| MSW | Master of Social Work | 研究生 | 2 |
| MEd | Master of Education | 研究生 | 6 |
| MPH | Master of Public Health | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 2 |
| MHA | Master of Health Administration | 研究生 | 1 |
| MUP | Master of Urban Planning | 研究生 | 1 |
| MBT | Master of Business Taxation | 研究生 | 2 |
| MAcc | Master of Accounting | 研究生 | 1 |
| LLM | Master of Laws | 研究生 | 8 |
| MAT | Master of Arts in Teaching | 研究生 | 3 |
| PhD | Doctor of Philosophy | 研究生 | 83 |
| EdD | Doctor of Education | 研究生 | 4 |
| DMA | Doctor of Musical Arts | 研究生 | 13 |
| JD | Juris Doctor | 专业 | 1 |
| MD | Doctor of Medicine | 专业 | 1 |
| PharmD | Doctor of Pharmacy | 专业 | 1 |
| DDS | Doctor of Dental Surgery | 专业 | 1 |
| DPT | Doctor of Physical Therapy | 专业 | 1 |
| OTD | Doctor of Occupational Therapy | 专业 | 2 |
| Certificate | 高级证书/文凭 | 研究生 | 166 |

### 0.4 分布矩阵 (学院 × 层级)

| 学院  级别 | UG | Grad | Doctoral | Professional | Certificate | 合计 |
|------------|-----|------|----------|--------------|-------------|------|
| Office of the Provost | 0 | 1 | 1 | 0 | 0 | 2 |
| USC Iovine and Young Academy | 8 | 2 | 0 | 0 | 0 | 10 |
| USC Leventhal School of Accounting | 2 | 3 | 0 | 1 | 1 | 7 |
| USC School of Architecture | 7 | 11 | 1 | 0 | 9 | 28 |
| USC Roski School of Art and Design | 15 | 4 | 0 | 0 | 1 | 20 |
| USC Marshall School of Business | 49 | 18 | 1 | 0 | 11 | 79 |
| USC School of Cinematic Arts | 25 | 10 | 3 | 0 | 5 | 43 |
| USC Bovard College | 0 | 7 | 0 | 0 | 0 | 7 |
| USC Dornsife College of Letters, Arts and Sciences | 199 | 55 | 39 | 0 | 19 | 312 |
| USC Annenberg School for Communication and Journal | 19 | 14 | 1 | 1 | 7 | 42 |
| USC Kaufman School of Dance | 5 | 0 | 0 | 0 | 0 | 5 |
| Herman Ostrow School of Dentistry of USC | 1 | 6 | 1 | 1 | 16 | 25 |
| USC School of Dramatic Arts | 21 | 2 | 0 | 0 | 0 | 23 |
| USC Rossier School of Education | 2 | 14 | 6 | 0 | 6 | 28 |
| USC Viterbi School of Engineering | 54 | 67 | 15 | 0 | 10 | 146 |
| USC Leonard Davis School of Gerontology | 8 | 15 | 3 | 0 | 3 | 29 |
| USC Independent Health Professions at the Herman O | 2 | 6 | 4 | 2 | 2 | 16 |
| USC Gould School of Law | 14 | 13 | 0 | 10 | 22 | 59 |
| Keck School of Medicine of USC | 16 | 28 | 11 | 4 | 16 | 75 |
| USC Thornton School of Music | 24 | 22 | 14 | 0 | 3 | 63 |
| USC Alfred E. Mann School of Pharmacy and Pharmace | 10 | 12 | 6 | 8 | 12 | 48 |
| USC Price School of Public Policy | 12 | 25 | 3 | 1 | 14 | 55 |
| USC Suzanne Dworak-Peck School of Social Work | 3 | 9 | 3 | 0 | 12 | 27 |
| **合计** | **496** | **344** | **112** | **28** | **169** | **1149** |

---

## SECTION 1 — Undergraduate Education

### 1.1 College/School Architecture

USC has 21 schools granting undergraduate degrees. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 学位级别

#### Keck School of Medicine of USC

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Global Health Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32210&returnto=9453) |
| 2 | Health Promotion and Disease Prevention Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32209&returnto=9453) |

##### MD/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Medicine/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32188&returnto=9453) |

#### USC Alfred E. Mann School of Pharmacy and Pharmaceutical Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Biopharmaceutical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32719&returnto=9453) |
| 2 | Pharmacology and Drug Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32707&returnto=9453) |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biopharmaceutical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32706&returnto=9453) |
| 2 | Pharmacology and Drug Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32517&returnto=9453) |

##### PHARMD/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32294&returnto=9453) |

#### USC Annenberg School for Communication and Journalism

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Communication | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31947&returnto=9453) |
| 2 | Journalism | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32448&returnto=9453) |
| 3 | Public Relations and Advertising | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32806&returnto=9453) |

#### USC Dornsife College of Letters, Arts and Sciences

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | American Popular Culture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32471&returnto=9453) |
| 2 | American Studies and Ethnicity (African American Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31692&returnto=9453) |
| 3 | American Studies and Ethnicity (Asian American Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31693&returnto=9453) |
| 4 | American Studies and Ethnicity | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31691&returnto=9453) |
| 5 | American Studies and Ethnicity (Chicano/Latino Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31694&returnto=9453) |
| 6 | Anthropology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31699&returnto=9453) |
| 7 | Anthropology (Visual Anthropology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31700&returnto=9453) |
| 8 | Applied and Computational Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31854&returnto=9453) |
| 9 | Archaeology and Heritage Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32908&returnto=9453) |
| 10 | Art History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31710&returnto=9453) |
| 11 | Astronomy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31889&returnto=9453) |
| 12 | Behavioral Economics and Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32779&returnto=9453) |
| 13 | Biological Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31717&returnto=9453) |
| 14 | Central European Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31924&returnto=9453) |
| 15 | Chemistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31738&returnto=9453) |
| 16 | Classics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31744&returnto=9453) |
| 17 | Cognitive Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31909&returnto=9453) |
| 18 | Comparative Literature | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31748&returnto=9453) |
| 19 | Contemporary Latino and Latin American Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32428&returnto=9453) |
| 20 | Earth Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31759&returnto=9453) |
| 21 | East Asian Area Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31765&returnto=9453) |
| 22 | East Asian Languages and Cultures | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31771&returnto=9453) |
| 23 | Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31776&returnto=9453) |
| 24 | English | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31788&returnto=9453) |
| 25 | Environmental Science and Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31805&returnto=9453) |
| 26 | Environmental Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31799&returnto=9453) |
| 27 | French | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31810&returnto=9453) |
| 28 | Gender and Sexuality Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32623&returnto=9453) |
| 29 | Global Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31701&returnto=9453) |
| 30 | Health and Human Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32477&returnto=9453) |
| 31 | History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31820&returnto=9453) |
| 32 | Human Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31720&returnto=9453) |
| 33 | Intelligence and Cyber Operations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32563&returnto=9453) |
| 34 | Interdisciplinary Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32737&returnto=9453) |
| 35 | International Relations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31830&returnto=9453) |
| 36 | International Relations (Global Business) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31831&returnto=9453) |
| 37 | International Relations and the Global Economy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31832&returnto=9453) |
| 38 | Italian | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31812&returnto=9453) |
| 39 | Jewish Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32429&returnto=9453) |
| 40 | Latin American and Iberian Cultures, Media and Politics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32519&returnto=9453) |
| 41 | Law, History, and Culture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31822&returnto=9453) |
| 42 | Linguistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31842&returnto=9453) |
| 43 | Linguistics and Cognitive Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32405&returnto=9453) |
| 44 | Linguistics and East Asian Languages and Cultures | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31844&returnto=9453) |
| 45 | Linguistics and Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31843&returnto=9453) |
| 46 | Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31852&returnto=9453) |
| 47 | Middle East Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31866&returnto=9453) |
| 48 | Narrative Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31790&returnto=9453) |
| 49 | Neuroscience | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31869&returnto=9453) |
| 50 | Non-Governmental Organizations and Social Change | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31929&returnto=9453) |
| 51 | Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31875&returnto=9453) |
| 52 | Philosophy, Politics and Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32604&returnto=9453) |
| 53 | Philosophy, Politics and Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31876&returnto=9453) |
| 54 | Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31888&returnto=9453) |
| 55 | Political Economy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31777&returnto=9453) |
| 56 | Political Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31897&returnto=9453) |
| 57 | Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31906&returnto=9453) |
| 58 | Religion | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31917&returnto=9453) |
| 59 | Russian | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31923&returnto=9453) |
| 60 | Social Sciences, with an Emphasis in Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31778&returnto=9453) |
| 61 | Social Sciences, with an Emphasis in Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31907&returnto=9453) |
| 62 | Sociology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31928&returnto=9453) |
| 63 | Spanish | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31936&returnto=9453) |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Applied and Computational Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31855&returnto=9453) |
| 2 | Astronomy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31886&returnto=9453) |
| 3 | Biochemistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31721&returnto=9453) |
| 4 | Biological Sciences (Biotechnology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32750&returnto=9453) |
| 5 | Biological Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31718&returnto=9453) |
| 6 | Biological Sciences (Ecology, Evolution and Environment) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32784&returnto=9453) |
| 7 | Biological Sciences (Marine Biology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32749&returnto=9453) |
| 8 | Biological Sciences (Molecular, Cellular and Developmental Biology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32751&returnto=9453) |
| 9 | Biophysics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31890&returnto=9453) |
| 10 | Chemistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31734&returnto=9453) |
| 11 | Chemistry (Chemical Biology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31737&returnto=9453) |
| 12 | Chemistry (Chemical Nanoscience) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31736&returnto=9453) |
| 13 | Chemistry (Research) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31735&returnto=9453) |
| 14 | Computational Linguistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32478&returnto=9453) |
| 15 | Computational Neuroscience | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31871&returnto=9453) |
| 16 | Economics and Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32704&returnto=9453) |
| 17 | Economics/Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31779&returnto=9453) |
| 18 | Environmental Science and Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31806&returnto=9453) |
| 19 | Environmental Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31804&returnto=9453) |
| 20 | Environmental Systems Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32958&returnto=9453) |
| 21 | Geodesign | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31939&returnto=9453) |
| 22 | Geological Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31758&returnto=9453) |
| 23 | Global Geodesign | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32569&returnto=9453) |
| 24 | Human Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31719&returnto=9453) |
| 25 | Human Security and Geospatial Intelligence | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32640&returnto=9453) |
| 26 | Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31853&returnto=9453) |
| 27 | Mathematics/Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31858&returnto=9453) |
| 28 | Neuroscience | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31870&returnto=9453) |
| 29 | Physical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31891&returnto=9453) |
| 30 | Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31885&returnto=9453) |
| 31 | Physics/Computer Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31887&returnto=9453) |
| 32 | Quantitative Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32504&returnto=9453) |

##### MA/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Arts, East Asian Area Studies/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31769&returnto=9453) |

#### USC Gould School of Law

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Law and Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32938&returnto=9453) |
| 2 | Legal Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32797&returnto=9453) |

##### JD/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32876&returnto=9453) |

#### USC Independent Health Professions at the Herman Ostrow School of Dentistry

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Occupational Therapy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32166&returnto=9453) |

#### USC Iovine and Young Academy

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Arts, Technology and the Business of Innovation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31586&returnto=9453) |
| 2 | Business of Innovation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32857&returnto=9453) |
| 3 | Human Technology Interaction | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32920&returnto=9453) |

#### USC Kaufman School of Dance

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31975&returnto=9453) |

#### USC Leonard Davis School of Gerontology

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development and Aging | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32142&returnto=9453) |
| 2 | Human Development and Aging, Health Science Track | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32143&returnto=9453) |
| 3 | Human Development and Aging, Honors Programs | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32144&returnto=9453) |
| 4 | Lifespan Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32145&returnto=9453) |

##### MS/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32156&returnto=9453) |

#### USC Leventhal School of Accounting

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31653&returnto=9453) |

#### USC Marshall School of Business

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting and Finance | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32801&returnto=9453) |
| 2 | Artificial Intelligence for Business | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32795&returnto=9453) |
| 3 | Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31591&returnto=9453) |
| 4 | Business Administration (Business Analytics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32693&returnto=9453) |
| 5 | Business Administration (Cinematic Arts) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31592&returnto=9453) |
| 6 | Business Administration (Communication) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32692&returnto=9453) |
| 7 | Business Administration (Entrepreneurship and Innovation) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32697&returnto=9453) |
| 8 | Business Administration (Finance) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32694&returnto=9453) |
| 9 | Business Administration (International Relations) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31593&returnto=9453) |
| 10 | Business Administration (Leadership and Innovation) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32696&returnto=9453) |
| 11 | Business Administration (Marketing) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32691&returnto=9453) |
| 12 | Business Administration (Real Estate Finance) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31594&returnto=9453) |
| 13 | Business Administration (Risk Management) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32695&returnto=9453) |
| 14 | Business Administration (World Program) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31595&returnto=9453) |
| 15 | Business of Cinematic Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32780&returnto=9453) |
| 16 | Real Estate Finance and Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32800&returnto=9453) |

##### MBA/JD

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31620&returnto=9453) |

##### MBA/MA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Master of Arts in East Asian Area Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31621&returnto=9453) |
| 2 | Master of Business Administration/Master of Arts in Jewish Nonprofit Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31629&returnto=9453) |

##### MBA/MD

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Doctor of Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31627&returnto=9453) |

##### MBA/MRED

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Master of Real Estate Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32376&returnto=9453) |

##### MBA/MS

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Master of Science in Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31624&returnto=9453) |
| 2 | Master of Business Administration/Master of Science in Industrial and Systems Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31625&returnto=9453) |
| 3 | Master of Business Administration/Master of Science, Systems Architecting and Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32546&returnto=9453) |

##### MBA/MSW

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31630&returnto=9453) |

##### MBA/MUP

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32595&returnto=9453) |

##### MBA/PHARMD

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Business Administration/Doctor of Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31628&returnto=9453) |

#### USC Price School of Public Policy

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Public Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32398&returnto=9453) |
| 2 | Real Estate Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32306&returnto=9453) |
| 3 | Urban Studies and Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32399&returnto=9453) |

##### MRED/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Real Estate Development/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31623&returnto=9453) |

#### USC Roski School of Art and Design

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31572&returnto=9453) |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Design | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32522&returnto=9453) |
| 2 | Fine Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31571&returnto=9453) |

#### USC School of Architecture

##### BArch

| # | 专业 | URL |
|---|------|-----|
| 1 | Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31587&returnto=9453) |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Architectural Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31557&returnto=9453) |
| 2 | Architecture and Inventive Technologies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32770&returnto=9453) |

##### MBS

| # | 专业 | URL |
|---|------|-----|
| 1 | Building Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31567&returnto=9453) |

##### MBS/MHC

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Building Science/Master of Heritage Conservation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32710&returnto=9453) |

#### USC School of Cinematic Arts

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Cinema and Media Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32404&returnto=9453) |
| 2 | Cinematic Arts, Film and Television Production | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31662&returnto=9453) |
| 3 | Media Arts and Practice | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31669&returnto=9453) |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Animation and Digital Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32669&returnto=9453) |
| 2 | Cinematic Arts, Film and Television Production | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31663&returnto=9453) |
| 3 | Game Art | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32728&returnto=9453) |
| 4 | Game Development and Interactive Design | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32782&returnto=9453) |
| 5 | Themed Entertainment | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32788&returnto=9453) |
| 6 | Writing for Screen and Television | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31674&returnto=9453) |

#### USC School of Dramatic Arts

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dramatic Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32838&returnto=9453) |
| 2 | Dramatic Arts, Acting Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32839&returnto=9453) |
| 3 | Dramatic Arts, Comedy Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32842&returnto=9453) |
| 4 | Dramatic Arts, Design Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32841&returnto=9453) |
| 5 | Dramatic Arts, Directing Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32918&returnto=9453) |
| 6 | Dramatic Arts, Musical Theatre Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32840&returnto=9453) |
| 7 | Visual and Performing Arts Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32006&returnto=9453) |

##### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Acting, Stage and Screen | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32769&returnto=9453) |
| 2 | Musical Theatre | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32621&returnto=9453) |
| 3 | Sound Design | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32832&returnto=9453) |
| 4 | Stage Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32833&returnto=9453) |
| 5 | Technical Direction | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32803&returnto=9453) |
| 6 | Theatrical Design | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32802&returnto=9453) |

#### USC Suzanne Dworak-Peck School of Social Work

##### BSW

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32862&returnto=9453) |

##### MSW/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32465&returnto=9453) |

#### USC Thornton School of Music

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Choral Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32243&returnto=9453) |
| 2 | Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32242&returnto=9453) |

##### BM

| # | 专业 | URL |
|---|------|-----|
| 1 | Choral Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32608&returnto=9453) |
| 2 | Composition | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32229&returnto=9453) |
| 3 | Jazz Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32230&returnto=9453) |
| 4 | Music Industry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32240&returnto=9453) |
| 5 | Music Production | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32231&returnto=9453) |
| 6 | Performance (Classical Guitar) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32233&returnto=9453) |
| 7 | Performance (Flute), (Oboe), (Clarinet), (Bassoon), (Saxophone), (French Horn), (Trumpet), (Trombone), (Tuba) or (Percussion) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32238&returnto=9453) |
| 8 | Performance (Organ) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32235&returnto=9453) |
| 9 | Performance (Piano) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32234&returnto=9453) |
| 10 | Performance (Popular Music) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32239&returnto=9453) |
| 11 | Performance (Studio Guitar) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32232&returnto=9453) |
| 12 | Performance (Violin), (Viola), (Violoncello), (Double Bass) or (Harp) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32236&returnto=9453) |
| 13 | Performance (Vocal Arts) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32237&returnto=9453) |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Music Industry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32241&returnto=9453) |

#### USC Viterbi School of Engineering

##### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32615&returnto=9453) |

##### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32035&returnto=9453) |
| 2 | Artificial Intelligence | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32917&returnto=9453) |
| 3 | Astronautical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32045&returnto=9453) |
| 4 | Biomedical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32049&returnto=9453) |
| 5 | Biomedical Engineering, Electrical Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32051&returnto=9453) |
| 6 | Biomedical Engineering, Mechanical Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32052&returnto=9453) |
| 7 | Biomedical Engineering, Molecular and Cellular Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32619&returnto=9453) |
| 8 | Chemical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32058&returnto=9453) |
| 9 | Chemical Engineering, Biological and Pharmaceutical Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32812&returnto=9453) |
| 10 | Chemical Engineering, Energy and Sustainability Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32814&returnto=9453) |
| 11 | Chemical Engineering, Materials Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32813&returnto=9453) |
| 12 | Chemical Engineering, Petroleum and Subsurface Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32811&returnto=9453) |
| 13 | Civil Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32433&returnto=9453) |
| 14 | Civil Engineering, Building Science Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32434&returnto=9453) |
| 15 | Civil Engineering, Construction Engineering and Management Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32626&returnto=9453) |
| 16 | Civil Engineering, Environmental Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32435&returnto=9453) |
| 17 | Civil Engineering, Structural Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32436&returnto=9453) |
| 18 | Civil Engineering, Water Resources Engineering Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32628&returnto=9453) |
| 19 | Computer Engineering and Computer Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32083&returnto=9453) |
| 20 | Computer Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32086&returnto=9453) |
| 21 | Computer Science Games | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32701&returnto=9453) |
| 22 | Computer Science/Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32088&returnto=9453) |
| 23 | Electrical and Computer Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32624&returnto=9453) |
| 24 | Environmental Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32437&returnto=9453) |
| 25 | Industrial and Systems Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32114&returnto=9453) |
| 26 | Mechanical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32039&returnto=9453) |

##### MS/MBA

| # | 专业 | URL |
|---|------|-----|
| 1 | Master of Science, Industrial and Systems Engineering/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32120&returnto=9453) |
| 2 | Master of Science, Systems Architecting and Engineering/Master of Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32548&returnto=9453) |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

Programs marked with asterisk (*) in the catalogue fall under the jurisdiction of Dornsife College but may be interdisciplinary in nature.

### 1.4 Minors — Complete List

Total minors: 267

#### Herman Ostrow School of Dentistry of USC

| # | Minor | URL |
|---|-------|-----|
| 1 | Craniofacial and Dental Technology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31979&returnto=9453) |

#### Keck School of Medicine of USC

| # | Minor | URL |
|---|-------|-----|
| 1 | Addiction Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32658&returnto=9453) |
| 2 | Cinema-Television for the Health Professions Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32211&returnto=9453) |
| 3 | Cultural Competence in Medicine Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32212&returnto=9453) |
| 4 | Environmental Health Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32213&returnto=9453) |
| 5 | Global Health Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32214&returnto=9453) |
| 6 | Health Care Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32201&returnto=9453) |
| 7 | Health Communication Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32215&returnto=9453) |
| 8 | Nutrition and Health Promotion Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32217&returnto=9453) |
| 9 | Psychiatry and Behavioral Sciences Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32881&returnto=9453) |
| 10 | Public Health Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32216&returnto=9453) |
| 11 | Speech-Language and Hearing Professions Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32645&returnto=9453) |
| 12 | Stem Cell Biology and Regenerative Medicine Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32799&returnto=9453) |
| 13 | Substance Abuse Prevention Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32218&returnto=9453) |

#### USC Alfred E. Mann School of Pharmacy and Pharmaceutical Sciences

| # | Minor | URL |
|---|-------|-----|
| 1 | Biopharmaceutical Business Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32708&returnto=9453) |
| 2 | Biopharmaceutical Management and Marketing Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32932&returnto=9453) |
| 3 | Foundation in Regulatory Sciences Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32642&returnto=9453) |
| 4 | Law and Biopharmaceutical Sciences Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32880&returnto=9453) |
| 5 | Science and Management of Biomedical Therapeutics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32427&returnto=9453) |

#### USC Annenberg School for Communication and Journalism

| # | Minor | URL |
|---|-------|-----|
| 1 | Advertising Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31968&returnto=9453) |
| 2 | Communication Policy and Law Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32416&returnto=9453) |
| 3 | Communication Technology Practices and Platforms Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31949&returnto=9453) |
| 4 | Cultural Diplomacy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32534&returnto=9453) |
| 5 | Culture, Media and Entertainment Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31948&returnto=9453) |
| 6 | Food Journalism and Public Relations Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32742&returnto=9453) |
| 7 | Justice, Voice, and Advocacy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32496&returnto=9453) |
| 8 | Latinx News Media Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32748&returnto=9453) |
| 9 | Media Economics and Entrepreneurship Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31616&returnto=9453) |
| 10 | News Media and Society Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31969&returnto=9453) |
| 11 | Nonprofits, Philanthropy and Volunteerism Interdisciplinary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32395&returnto=9453) |
| 12 | Podcasting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32718&returnto=9453) |
| 13 | Professional and Managerial Communication Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31950&returnto=9453) |
| 14 | Public Relations Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32417&returnto=9453) |
| 15 | Sports Media Industries Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32493&returnto=9453) |
| 16 | Sports Media Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31951&returnto=9453) |

#### USC Dornsife College of Letters, Arts and Sciences

| # | Minor | URL |
|---|-------|-----|
| 1 | American Popular Culture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31696&returnto=9453) |
| 2 | American Studies and Ethnicity Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31695&returnto=9453) |
| 3 | Arabic Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32413&returnto=9453) |
| 4 | Archaeology and Heritage Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32877&returnto=9453) |
| 5 | Archaeology of California Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32492&returnto=9453) |
| 6 | Art History Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31711&returnto=9453) |
| 7 | Astronomy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31893&returnto=9453) |
| 8 | Behavioral Economics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32415&returnto=9453) |
| 9 | Biology and Business Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32747&returnto=9453) |
| 10 | Biology of Human Movement Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32665&returnto=9453) |
| 11 | Chemistry Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31740&returnto=9453) |
| 12 | Chinese for the Professions Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32382&returnto=9453) |
| 13 | Classical Greek Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32474&returnto=9453) |
| 14 | Classical Perspectives Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32430&returnto=9453) |
| 15 | Classics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31745&returnto=9453) |
| 16 | Coaching, Health and Wellness Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32909&returnto=9453) |
| 17 | Comparative Literature Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31749&returnto=9453) |
| 18 | Computational Biology and Bioinformatics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31723&returnto=9453) |
| 19 | Consumer Behavior Interdisciplinary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31912&returnto=9453) |
| 20 | Contemplative Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32529&returnto=9453) |
| 21 | Cultural Anthropology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31702&returnto=9453) |
| 22 | Cultures and Politics of the Pacific Rim Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31773&returnto=9453) |
| 23 | Earth Sciences Minor: Climate Change, Stewardship and Resiliency | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32387&returnto=9453) |
| 24 | East Asian Area Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31766&returnto=9453) |
| 25 | East Asian Languages and Cultures Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31772&returnto=9453) |
| 26 | Economics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31780&returnto=9453) |
| 27 | English Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31789&returnto=9453) |
| 28 | Environmental Chemistry and Sustainability Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31741&returnto=9453) |
| 29 | Environmental Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31807&returnto=9453) |
| 30 | Evolutionary Health and Medicine Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32950&returnto=9453) |
| 31 | Folklore and Popular Culture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31703&returnto=9453) |
| 32 | Food and Society Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32609&returnto=9453) |
| 33 | Forensics and Criminality Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31931&returnto=9453) |
| 34 | French Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31811&returnto=9453) |
| 35 | Gender and Sexuality Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32602&returnto=9453) |
| 36 | Gender and Social Justice Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32423&returnto=9453) |
| 37 | Geobiology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31761&returnto=9453) |
| 38 | Geodesign Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32948&returnto=9453) |
| 39 | Geohazards Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31762&returnto=9453) |
| 40 | German Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31818&returnto=9453) |
| 41 | GIS and Sustainability Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32536&returnto=9453) |
| 42 | Global Communication Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31834&returnto=9453) |
| 43 | History and Culture of Business Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31825&returnto=9453) |
| 44 | History Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31824&returnto=9453) |
| 45 | Human Disease Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32666&returnto=9453) |
| 46 | Human Performance and AI in Sports Analytics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32949&returnto=9453) |
| 47 | Human Rights Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31899&returnto=9453) |
| 48 | Human Security and Geospatial Intelligence Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32459&returnto=9453) |
| 49 | International Health, Development, and Social Justice Interdisciplinary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31829&returnto=9453) |
| 50 | International Policy and Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31835&returnto=9453) |
| 51 | International Relations Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31833&returnto=9453) |
| 52 | Iranian Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31867&returnto=9453) |
| 53 | Italian Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31813&returnto=9453) |
| 54 | Jewish American Studies Minor (American Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31697&returnto=9453) |
| 55 | Jewish American Studies Minor (Jewish Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31840&returnto=9453) |
| 56 | Jewish Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32424&returnto=9453) |
| 57 | Judaic Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31839&returnto=9453) |
| 58 | Korean Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31767&returnto=9453) |
| 59 | Latin American Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31938&returnto=9453) |
| 60 | Latin Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32473&returnto=9453) |
| 61 | Law and Society Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31900&returnto=9453) |
| 62 | LGBTQ Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31816&returnto=9453) |
| 63 | Linguistics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31845&returnto=9453) |
| 64 | Logic Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32954&returnto=9453) |
| 65 | Luso-Brazilian Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32425&returnto=9453) |
| 66 | Managing Human Relations Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31932&returnto=9453) |
| 67 | Marine Biology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32470&returnto=9453) |
| 68 | Mathematical Data Analytics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32663&returnto=9453) |
| 69 | Mathematical Finance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31851&returnto=9453) |
| 70 | Mathematics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31857&returnto=9453) |
| 71 | Medical Anthropology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31704&returnto=9453) |
| 72 | Middle East Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31868&returnto=9453) |
| 73 | Mind Body Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32739&returnto=9453) |
| 74 | Modern Art Markets and Ethics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32553&returnto=9453) |
| 75 | Narrative Structure Interdisciplinary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31793&returnto=9453) |
| 76 | Native American Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32497&returnto=9453) |
| 77 | Natural Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31724&returnto=9453) |
| 78 | Neuroscience Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31872&returnto=9453) |
| 79 | Paleontology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32951&returnto=9453) |
| 80 | Philosophy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31878&returnto=9453) |
| 81 | Philosophy of Law, Politics and Economics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32667&returnto=9453) |
| 82 | Photography and Social Change Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31933&returnto=9453) |
| 83 | Physics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31892&returnto=9453) |
| 84 | Plastics Sustainability Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32819&returnto=9453) |
| 85 | Political Organizing in the Digital Age Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31902&returnto=9453) |
| 86 | Political Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31898&returnto=9453) |
| 87 | Practical Politics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32481&returnto=9453) |
| 88 | Psychology and Law Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31911&returnto=9453) |
| 89 | Psychology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31910&returnto=9453) |
| 90 | Race, Ethnicity and Politics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31901&returnto=9453) |
| 91 | Religion Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31921&returnto=9453) |
| 92 | Resistance to Genocide Interdisciplinary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31823&returnto=9453) |
| 93 | Russian Area Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31926&returnto=9453) |
| 94 | Russian Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31925&returnto=9453) |
| 95 | Sociology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31930&returnto=9453) |
| 96 | South Asian Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32824&returnto=9453) |
| 97 | Southeast Asia and its People Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31705&returnto=9453) |
| 98 | Spanish Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31937&returnto=9453) |
| 99 | Spatial Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31940&returnto=9453) |
| 100 | Statistics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31856&returnto=9453) |
| 101 | Thematic Approaches to Humanities and Society Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31946&returnto=9453) |
| 102 | User Experience Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32507&returnto=9453) |
| 103 | Visual Culture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31712&returnto=9453) |

#### USC Gould School of Law

| # | Minor | URL |
|---|-------|-----|
| 1 | Entertainment Law Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32879&returnto=9453) |
| 2 | Law and Government Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32943&returnto=9453) |
| 3 | Law and Innovation Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32944&returnto=9453) |
| 4 | Law and Migration Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32703&returnto=9453) |
| 5 | Law and Public Health Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32931&returnto=9453) |
| 6 | Law and Regulation of Artificial Intelligence Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32878&returnto=9453) |
| 7 | Law and Social Justice Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32702&returnto=9453) |
| 8 | Law and Technology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32793&returnto=9453) |
| 9 | Law, Advocacy and Persuasive Performance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32933&returnto=9453) |
| 10 | Legal Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32584&returnto=9453) |
| 11 | Sports Law Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32942&returnto=9453) |

#### USC Independent Health Professions at the Herman Ostrow School of Dentistry

| # | Minor | URL |
|---|-------|-----|
| 1 | Occupational Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32167&returnto=9453) |

#### USC Iovine and Young Academy

| # | Minor | URL |
|---|-------|-----|
| 1 | Designing for Digital Experiences Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32661&returnto=9453) |
| 2 | Designing Products Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32689&returnto=9453) |
| 3 | Disruptive Innovation Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32567&returnto=9453) |
| 4 | Extended Reality Design and Development Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32828&returnto=9453) |
| 5 | Health Innovation Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32617&returnto=9453) |

#### USC Kaufman School of Dance

| # | Minor | URL |
|---|-------|-----|
| 1 | Choreography for Stage and Screen Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32610&returnto=9453) |
| 2 | Dance in Entertainment Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32495&returnto=9453) |
| 3 | Dance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31977&returnto=9453) |
| 4 | Hip-Hop, Street and Social Dance Forms Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32488&returnto=9453) |

#### USC Leonard Davis School of Gerontology

| # | Minor | URL |
|---|-------|-----|
| 1 | Geroscience Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32738&returnto=9453) |
| 2 | Individuals, Societies and Aging Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32146&returnto=9453) |
| 3 | Science, Health and Aging Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32147&returnto=9453) |

#### USC Leventhal School of Accounting

| # | Minor | URL |
|---|-------|-----|
| 1 | Accounting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31654&returnto=9453) |

#### USC Marshall School of Business

| # | Minor | URL |
|---|-------|-----|
| 1 | Applied AI in Business Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32945&returnto=9453) |
| 2 | Business Economics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31598&returnto=9453) |
| 3 | Business Finance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31599&returnto=9453) |
| 4 | Business Law Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31600&returnto=9453) |
| 5 | Business Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31597&returnto=9453) |
| 6 | Business Technology Fusion Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31601&returnto=9453) |
| 7 | Consumer Behavior Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31602&returnto=9453) |
| 8 | Customer Analytics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32659&returnto=9453) |
| 9 | Dynamics in Workplace Communication Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32583&returnto=9453) |
| 10 | Entrepreneurship Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31603&returnto=9453) |
| 11 | Human Resource Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31604&returnto=9453) |
| 12 | Management Consulting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31606&returnto=9453) |
| 13 | Marketing Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31607&returnto=9453) |
| 14 | Operations and Supply Chain Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31608&returnto=9453) |
| 15 | Organizational Leadership and Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31609&returnto=9453) |
| 16 | Performance Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32426&returnto=9453) |
| 17 | Product Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32941&returnto=9453) |
| 18 | Real Estate Finance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32540&returnto=9453) |
| 19 | Risk Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32538&returnto=9453) |
| 20 | Social Entrepreneurship Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31611&returnto=9453) |
| 21 | Sports Business and Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32603&returnto=9453) |
| 22 | Technology Commercialization Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31612&returnto=9453) |

#### USC Price School of Public Policy

| # | Minor | URL |
|---|-------|-----|
| 1 | Construction Planning and Management Minor (Public Policy) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32374&returnto=9453) |
| 2 | Education Policy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32641&returnto=9453) |
| 3 | Health Administration Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32307&returnto=9453) |
| 4 | Health Policy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32308&returnto=9453) |
| 5 | Law and Public Policy Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32309&returnto=9453) |
| 6 | Nonprofits, Philanthropy and Volunteerism Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32310&returnto=9453) |
| 7 | Real Estate Development Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32311&returnto=9453) |
| 8 | Urban Sustainable Planning Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32419&returnto=9453) |

#### USC Roski School of Art and Design

| # | Minor | URL |
|---|-------|-----|
| 1 | 3-Dimensional Design Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31582&returnto=9453) |
| 2 | Ceramics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31573&returnto=9453) |
| 3 | Communication Design Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31574&returnto=9453) |
| 4 | Drawing Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31576&returnto=9453) |
| 5 | Fashion Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32829&returnto=9453) |
| 6 | Intermedia Arts Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32618&returnto=9453) |
| 7 | Painting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31577&returnto=9453) |
| 8 | Performance Art Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32700&returnto=9453) |
| 9 | Photography Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31578&returnto=9453) |
| 10 | Sculpture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31579&returnto=9453) |
| 11 | Two-Dimensional Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31580&returnto=9453) |
| 12 | Visual Narrative Art Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32668&returnto=9453) |

#### USC Rossier School of Education

| # | Minor | URL |
|---|-------|-----|
| 1 | Education and Society Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32014&returnto=9453) |
| 2 | Sustainability, Community and STEM Education Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32922&returnto=9453) |

#### USC School of Architecture

| # | Minor | URL |
|---|-------|-----|
| 1 | Architecture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31558&returnto=9453) |
| 2 | Landscape Architecture Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31559&returnto=9453) |

#### USC School of Cinematic Arts

| # | Minor | URL |
|---|-------|-----|
| 1 | 3-D Animation in Cinematic Arts Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32414&returnto=9453) |
| 2 | Cinematic Arts Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31678&returnto=9453) |
| 3 | Comedy Writing Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32953&returnto=9453) |
| 4 | Digital Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31680&returnto=9453) |
| 5 | Documentary Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32535&returnto=9453) |
| 6 | Entertainment Industry Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31681&returnto=9453) |
| 7 | Future Cinema Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32480&returnto=9453) |
| 8 | Game Audio Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31683&returnto=9453) |
| 9 | Game Design Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31684&returnto=9453) |
| 10 | Game Entrepreneurism Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31685&returnto=9453) |
| 11 | Game Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31686&returnto=9453) |
| 12 | Game User Research Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31687&returnto=9453) |
| 13 | Immersive Media Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32506&returnto=9453) |
| 14 | Media and Social Change Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31688&returnto=9453) |
| 15 | Screenwriting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31690&returnto=9453) |
| 16 | Themed Entertainment Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32431&returnto=9453) |

#### USC School of Dramatic Arts

| # | Minor | URL |
|---|-------|-----|
| 1 | Comedy (Performance) Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32008&returnto=9453) |
| 2 | Creating Dramatic Writing Content Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32858&returnto=9453) |
| 3 | Creative Leadership Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32859&returnto=9453) |
| 4 | Creator Arts Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32964&returnto=9453) |
| 5 | Directing Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32916&returnto=9453) |
| 6 | Performing Arts Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32009&returnto=9453) |
| 7 | Performing Social Change Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32614&returnto=9453) |
| 8 | Theatre Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32011&returnto=9453) |

#### USC Suzanne Dworak-Peck School of Social Work

| # | Minor | URL |
|---|-------|-----|
| 1 | Social Work and Juvenile Justice Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32664&returnto=9453) |

#### USC Thornton School of Music

| # | Minor | URL |
|---|-------|-----|
| 1 | Jazz Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32246&returnto=9453) |
| 2 | Music Industry Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32245&returnto=9453) |
| 3 | Music Production Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32384&returnto=9453) |
| 4 | Music Recording Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32244&returnto=9453) |
| 5 | Musical Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32248&returnto=9453) |
| 6 | Musical Theatre Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32247&returnto=9453) |
| 7 | Popular Music Studies Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32249&returnto=9453) |
| 8 | Songwriting Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32250&returnto=9453) |

#### USC Viterbi School of Engineering

| # | Minor | URL |
|---|-------|-----|
| 1 | Applied Analytics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32397&returnto=9453) |
| 2 | Artificial Intelligence Applications Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32792&returnto=9453) |
| 3 | Artificial Intelligence Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32947&returnto=9453) |
| 4 | Astronautical Engineering Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32046&returnto=9453) |
| 5 | Blockchain Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32585&returnto=9453) |
| 6 | Computer Programming Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32127&returnto=9453) |
| 7 | Computer Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32531&returnto=9453) |
| 8 | Connected Devices and Making Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32533&returnto=9453) |
| 9 | Construction Planning and Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32075&returnto=9453) |
| 10 | Cyber Governance Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32910&returnto=9453) |
| 11 | Cybersecurity Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32790&returnto=9453) |
| 12 | Digital Forensics Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32745&returnto=9453) |
| 13 | Engineering Innovation for Global Challenges Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32744&returnto=9453) |
| 14 | Engineering Management Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32115&returnto=9453) |
| 15 | Foundations of Data Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32613&returnto=9453) |
| 16 | Internet of Things Engineering Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32537&returnto=9453) |
| 17 | Materials Science Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32875&returnto=9453) |
| 18 | Mobile App Development Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32129&returnto=9453) |
| 19 | Nanotechnology Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32439&returnto=9453) |
| 20 | Petroleum Engineering Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32068&returnto=9453) |
| 21 | Technical Game Art Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32724&returnto=9453) |
| 22 | Technology Entrepreneurship Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32952&returnto=9453) |
| 23 | Video Game Production Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32794&returnto=9453) |
| 24 | Video Game Programming Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32131&returnto=9453) |
| 25 | Web Development Minor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32746&returnto=9453) |

### 1.5 General Education Requirements

USC requires all undergraduates to complete the General Education (GE) program, which includes courses in:
- Arts
- Humanities
- Social Sciences
- Natural Sciences and Engineering
- Quantitative Reasoning
- Writing
- Foreign Language (for some schools)

For details, see: [USC General Education](https://catalogue.usc.edu/content.php?catoid=22&navoid=9387)

---

## SECTION 2 — Graduate Education

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### Herman Ostrow School of Dentistry of USC

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Orofacial Pain and Oral Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31988&returnto=9453) |
| 2 | Biomaterials and Digital Dentistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32523&returnto=9453) |
| 3 | Biomedical Implants and Tissue Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32576&returnto=9453) |
| 4 | Community Oral Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32572&returnto=9453) |
| 5 | Craniofacial Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32370&returnto=9453) |
| 6 | Geriatric Dentistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31996&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Craniofacial Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31995&returnto=9453) |

##### DDS

| # | 项目 | URL |
|---|------|-----|
| 1 | Dental Surgery | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31980&returnto=9453) |

#### Keck School of Medicine of USC

##### MACM

| # | 项目 | URL |
|---|------|-----|
| 1 | Academic Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32194&returnto=9453) |

##### MPAP

| # | 项目 | URL |
|---|------|-----|
| 1 | Physician Assistant Practice | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32204&returnto=9453) |

##### MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32222&returnto=9453) |

##### MPH/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health/Master of Science, Social Entrepreneurship | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32461&returnto=9453) |

##### MPH/MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32224&returnto=9453) |

##### MPH/PHARMD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health/Doctor of Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32371&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Addiction Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32789&returnto=9453) |
| 2 | Applied Biostatistics and Epidemiology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32219&returnto=9453) |
| 3 | Biomedical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32654&returnto=9453) |
| 4 | Biostatistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32220&returnto=9453) |
| 5 | Cancer Biology and Molecular Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32921&returnto=9453) |
| 6 | Cancer Genomics and Bioinformatics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32928&returnto=9453) |
| 7 | Clinical Translational Research | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32850&returnto=9453) |
| 8 | Global Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32197&returnto=9453) |
| 9 | Health Behavior Research | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32927&returnto=9453) |
| 10 | Integrative Anatomical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32525&returnto=9453) |
| 11 | Molecular Microbiology and Immunology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32205&returnto=9453) |
| 12 | Molecular Pathology and Experimental Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32776&returnto=9453) |
| 13 | Narrative Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32651&returnto=9453) |
| 14 | Neuroimaging and Informatics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32206&returnto=9453) |
| 15 | Pain Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32741&returnto=9453) |
| 16 | Perfusion Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32837&returnto=9453) |
| 17 | Public Health Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32593&returnto=9453) |
| 18 | Speech-Language Pathology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32649&returnto=9453) |
| 19 | Stem Cell Biology and Regenerative Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32228&returnto=9453) |
| 20 | Stem Cell Biology and Regenerative Medicine with Research Year | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32709&returnto=9453) |
| 21 | Translational Biotechnology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32500&returnto=9453) |

##### Online

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health (MPH) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32549&returnto=9453) |

##### DNAP

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Nurse Anesthesia Practice | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32407&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biostatistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32225&returnto=9453) |
| 2 | Cancer Biology and Genomics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32190&returnto=9453) |
| 3 | Development, Stem Cells, and Regenerative Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32191&returnto=9453) |
| 4 | Epidemiology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32226&returnto=9453) |
| 5 | Health Behavior Research | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32852&returnto=9453) |
| 6 | Infectious Diseases, Immunology and Pathogenesis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32590&returnto=9453) |
| 7 | Integrative Anatomical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32773&returnto=9453) |
| 8 | Medical Biophysics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32521&returnto=9453) |
| 9 | Molecular Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32810&returnto=9453) |
| 10 | Neuromedicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32826&returnto=9453) |

##### MD

| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32186&returnto=9453) |

##### MD/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Medicine/Master of Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32189&returnto=9453) |

##### MD/PHD

| # | 项目 | URL |
|---|------|-----|
| 1 | Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32187&returnto=9453) |

##### PHARMD/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Global Medicine/Doctor of Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32199&returnto=9453) |

#### Office of the Provost

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31555&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31556&returnto=9453) |

#### USC Alfred E. Mann School of Pharmacy and Pharmaceutical Sciences

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biopharmaceutical Marketing | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32524&returnto=9453) |
| 2 | Clinical and Experimental Therapeutics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32527&returnto=9453) |
| 3 | Clinical Trial Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32851&returnto=9453) |
| 4 | Healthcare Decision Analysis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32283&returnto=9453) |
| 5 | Management of Drug Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32285&returnto=9453) |
| 6 | Medical Product Quality | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32286&returnto=9453) |
| 7 | Molecular Pharmacology and Toxicology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32281&returnto=9453) |
| 8 | Pharmaceutical Economics and Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32282&returnto=9453) |
| 9 | Pharmaceutical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32280&returnto=9453) |
| 10 | Pharmacoepidemiology and Drug Safety | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32902&returnto=9453) |
| 11 | Regulatory Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32547&returnto=9453) |
| 12 | Regulatory Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32284&returnto=9453) |

##### DRSc

| # | 项目 | URL |
|---|------|-----|
| 1 | Regulatory Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32287&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical and Experimental Therapeutics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32288&returnto=9453) |
| 2 | Health Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32289&returnto=9453) |
| 3 | Molecular Pharmacology and Toxicology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32292&returnto=9453) |
| 4 | Pharmaceutical Economics and Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31787&returnto=9453) |
| 5 | Pharmaceutical Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32291&returnto=9453) |

##### PharmD

| # | 项目 | URL |
|---|------|-----|
| 1 | Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32279&returnto=9453) |

##### PHARMD/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32293&returnto=9453) |

##### PHARMD/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy/Master of Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32298&returnto=9453) |

##### PHARMD/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy/Master of Science, Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32295&returnto=9453) |
| 2 | Doctor of Pharmacy/Master of Science, Global Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32296&returnto=9453) |
| 3 | Doctor of Pharmacy/Master of Science, Regulatory Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32299&returnto=9453) |
| 4 | Healthcare Decision Analysis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32297&returnto=9453) |

##### PHARMD/PHD

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Pharmacy/Doctor of Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32300&returnto=9453) |

#### USC Annenberg School for Communication and Journalism

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31961&returnto=9453) |
| 2 | Global Media and Communication | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32815&returnto=9453) |
| 3 | Public Relations and Advertising | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32648&returnto=9453) |
| 4 | Specialized Journalism (Arts and Culture) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32808&returnto=9453) |
| 5 | Specialized Journalism | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31972&returnto=9453) |

##### MCG

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31952&returnto=9453) |

##### MCG/MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Communication Management/Master of Arts, Jewish Nonprofit Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31966&returnto=9453) |

##### MPD

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Diplomacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31962&returnto=9453) |
| 2 | Public Diplomacy (Practitioner and Mid-Career Professional) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31963&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Communication Research | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32843&returnto=9453) |
| 2 | Digital Media Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32698&returnto=9453) |
| 3 | Digital Social Media | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31953&returnto=9453) |
| 4 | Journalism | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31970&returnto=9453) |
| 5 | Public Relations Innovation, Strategy and Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32807&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31964&returnto=9453) |

##### MCG/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Communication Management/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31965&returnto=9453) |

#### USC Bovard College

##### MMLIS

| # | 项目 | URL |
|---|------|-----|
| 1 | Library and Information Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32845&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Analytics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32905&returnto=9453) |
| 2 | Criminal Justice | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32577&returnto=9453) |
| 3 | Emergency Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32736&returnto=9453) |
| 4 | Hospitality and Tourism | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32647&returnto=9453) |
| 5 | Human Resource Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32472&returnto=9453) |
| 6 | Project Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32526&returnto=9453) |

#### USC Dornsife College of Letters, Arts and Sciences

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Anthropology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31706&returnto=9453) |
| 2 | Applied Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31863&returnto=9453) |
| 3 | Art History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31713&returnto=9453) |
| 4 | Classics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31746&returnto=9453) |
| 5 | Comparative Studies in Literature and Culture (Comparative Literature) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31752&returnto=9453) |
| 6 | Comparative Studies in Literature and Culture (Comparative Media and Culture) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31750&returnto=9453) |
| 7 | Comparative Studies in Literature and Culture (French and Francophone Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31754&returnto=9453) |
| 8 | Comparative Studies in Literature and Culture (Spanish and Latin American Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31756&returnto=9453) |
| 9 | East Asian Area Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31768&returnto=9453) |
| 10 | East Asian Languages and Cultures | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31774&returnto=9453) |
| 11 | English | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31794&returnto=9453) |
| 12 | Environmental Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31808&returnto=9453) |
| 13 | Global Security Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32672&returnto=9453) |
| 14 | History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31826&returnto=9453) |
| 15 | International Relations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31836&returnto=9453) |
| 16 | Language Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32768&returnto=9453) |
| 17 | Linguistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31847&returnto=9453) |
| 18 | Literary Editing and Publishing | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32456&returnto=9453) |
| 19 | Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31862&returnto=9453) |
| 20 | Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31881&returnto=9453) |
| 21 | Philosophy and Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31882&returnto=9453) |
| 22 | Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31895&returnto=9453) |
| 23 | Political Science and International Relations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31837&returnto=9453) |
| 24 | Religion | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32846&returnto=9453) |

##### MA/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Arts, Philosophy/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31883&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32455&returnto=9453) |
| 2 | Applied Economics and Econometrics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32591&returnto=9453) |
| 3 | Applied Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31859&returnto=9453) |
| 4 | Applied Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31914&returnto=9453) |
| 5 | Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31725&returnto=9453) |
| 6 | Computational Molecular Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31861&returnto=9453) |
| 7 | Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32885&returnto=9453) |
| 8 | Economics and Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32872&returnto=9453) |
| 9 | Environmental Risk Analysis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31809&returnto=9453) |
| 10 | Geodesign, Environment and Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32868&returnto=9453) |
| 11 | Geographic Information Science and Technology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31941&returnto=9453) |
| 12 | Geological Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31763&returnto=9453) |
| 13 | Human Security and Geospatial Intelligence | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32558&returnto=9453) |
| 14 | Innovation Economics, Law and Regulation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32817&returnto=9453) |
| 15 | Marine and Environmental Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31726&returnto=9453) |
| 16 | Mathematical Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32874&returnto=9453) |
| 17 | Mathematical Finance | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31783&returnto=9453) |
| 18 | Molecular and Computational Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31730&returnto=9453) |
| 19 | Molecular Genetics and Biochemistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31729&returnto=9453) |
| 20 | Ocean Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31873&returnto=9453) |
| 21 | Physical Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32674&returnto=9453) |
| 22 | Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31894&returnto=9453) |
| 23 | Population, Health and Place | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32676&returnto=9453) |
| 24 | Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32854&returnto=9453) |
| 25 | Quantitative and Computational Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32611&returnto=9453) |
| 26 | Spatial Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32545&returnto=9453) |
| 27 | Spatial Economics and Data Analysis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32559&returnto=9453) |
| 28 | Statistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31860&returnto=9453) |

##### MSM

| # | 项目 | URL |
|---|------|-----|
| 1 | Sustainability Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32809&returnto=9453) |

##### MVA

| # | 项目 | URL |
|---|------|-----|
| 1 | Visual Anthropology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31708&returnto=9453) |

##### DGL

| # | 项目 | URL |
|---|------|-----|
| 1 | Geospatial Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32961&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | American Studies and Ethnicity | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31698&returnto=9453) |
| 2 | Anthropology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31709&returnto=9453) |
| 3 | Applied Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31864&returnto=9453) |
| 4 | Art History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31716&returnto=9453) |
| 5 | Biology (Marine and Environmental Biology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32771&returnto=9453) |
| 6 | Chemistry (Chemical Physics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31743&returnto=9453) |
| 7 | Chemistry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31742&returnto=9453) |
| 8 | Classics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31747&returnto=9453) |
| 9 | Comparative Studies in Literature and Culture (Comparative Literature) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31753&returnto=9453) |
| 10 | Comparative Studies in Literature and Culture (Comparative Media and Culture) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31751&returnto=9453) |
| 11 | Comparative Studies in Literature and Culture (French and Francophone Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31755&returnto=9453) |
| 12 | Comparative Studies in Literature and Culture (Spanish and Latin American Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31757&returnto=9453) |
| 13 | Computational Biology and Bioinformatics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31732&returnto=9453) |
| 14 | East Asian Languages and Cultures | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31775&returnto=9453) |
| 15 | Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31786&returnto=9453) |
| 16 | English and American Literature | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31795&returnto=9453) |
| 17 | Geological Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31764&returnto=9453) |
| 18 | History | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31827&returnto=9453) |
| 19 | Integrative and Evolutionary Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31733&returnto=9453) |
| 20 | Linguistics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31848&returnto=9453) |
| 21 | Linguistics (Specialization in East Asian Linguistics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31849&returnto=9453) |
| 22 | Literature and Creative Writing | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31796&returnto=9453) |
| 23 | Marine Biology and Biological Oceanography | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31728&returnto=9453) |
| 24 | Mathematics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31865&returnto=9453) |
| 25 | Molecular Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31731&returnto=9453) |
| 26 | Neurobiology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32972&returnto=9453) |
| 27 | Ocean Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31874&returnto=9453) |
| 28 | Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31884&returnto=9453) |
| 29 | Physical Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32675&returnto=9453) |
| 30 | Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31896&returnto=9453) |
| 31 | Political Science and International Relations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31904&returnto=9453) |
| 32 | Population, Health and Place | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32381&returnto=9453) |
| 33 | Psychology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31915&returnto=9453) |
| 34 | Religion | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31922&returnto=9453) |
| 35 | Slavic Languages and Literatures | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31927&returnto=9453) |
| 36 | Sociology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31935&returnto=9453) |

##### PHD/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy in Political Science and International Relations/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31903&returnto=9453) |

##### PHD/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Philosophy in Psychology (Clinical) and Master of Public Health (Health Promotion) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31916&returnto=9453) |

#### USC Gould School of Law

##### LLM

| # | 项目 | URL |
|---|------|-----|
| 1 | Alternative Dispute Resolution | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32401&returnto=9453) |
| 2 | Artificial Intelligence and Technology Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32934&returnto=9453) |
| 3 | Business Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32848&returnto=9453) |
| 4 | International Business and Economic Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32579&returnto=9453) |
| 5 | Master of Laws | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32638&returnto=9453) |
| 6 | Media and Entertainment Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32849&returnto=9453) |
| 7 | Privacy Law and Cybersecurity | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32653&returnto=9453) |
| 8 | Sports Law and Negotiation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32935&returnto=9453) |

##### MCL

| # | 项目 | URL |
|---|------|-----|
| 1 | Comparative Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32639&returnto=9453) |

##### MDR

| # | 项目 | URL |
|---|------|-----|
| 1 | Dispute Resolution | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32458&returnto=9453) |

##### MITLE

| # | 项目 | URL |
|---|------|-----|
| 1 | International Trade Law and Economics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32705&returnto=9453) |

##### MSL

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Studies in Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32712&returnto=9453) |
| 2 | Sports Law and Negotiation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32939&returnto=9453) |

##### JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32171&returnto=9453) |

##### JD/MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Arts, Philosophy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32365&returnto=9453) |

##### JD/MCG

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Communication Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32178&returnto=9453) |

##### JD/MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Public Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32344&returnto=9453) |

##### JD/MPP

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Public Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32341&returnto=9453) |

##### JD/MRED

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Real Estate Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32377&returnto=9453) |

##### JD/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Science in Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32173&returnto=9453) |

##### JD/MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32176&returnto=9453) |

##### JD/PHARMD

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Doctor of Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32174&returnto=9453) |

##### JD/PHD

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Doctor of Philosophy in Political Science and International Relations | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32550&returnto=9453) |

#### USC Independent Health Professions at the Herman Ostrow School of Dentistry

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Occupational Therapy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32168&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Biokinesiology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32161&returnto=9453) |
| 2 | Biokinesiology (Sports Science) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32541&returnto=9453) |
| 3 | Lifespan, Nutrition and Dietetics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32729&returnto=9453) |
| 4 | Nutrition, Healthspan and Longevity | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32155&returnto=9453) |
| 5 | Nutritional Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32730&returnto=9453) |

##### OTD

| # | 项目 | URL |
|---|------|-----|
| 1 | Entry-Level Occupational Therapy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32726&returnto=9453) |
| 2 | Occupational Therapy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32169&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Biokinesiology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32163&returnto=9453) |
| 2 | Occupational Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32170&returnto=9453) |

##### DPT

| # | 项目 | URL |
|---|------|-----|
| 1 | Professional Entry-Level Doctor of Physical Therapy Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32393&returnto=9453) |

##### DPT/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Doctor of Physical Therapy/Master of Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32165&returnto=9453) |

#### USC Iovine and Young Academy

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Fashion Innovation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32835&returnto=9453) |
| 2 | Integrated Design, Business and Technology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32388&returnto=9453) |

#### USC Leonard Davis School of Gerontology

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Aging Services Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32581&returnto=9453) |
| 2 | Foodservice Management and Dietetics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32727&returnto=9453) |
| 3 | Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32151&returnto=9453) |
| 4 | Long Term Care Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32582&returnto=9453) |
| 5 | Medical Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32586&returnto=9453) |
| 6 | Senior Living Hospitality | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32622&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Placement Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32149&returnto=9453) |
| 2 | Applied Technology and Aging | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32733&returnto=9453) |
| 3 | Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32148&returnto=9453) |

##### MS/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32466&returnto=9453) |

##### MS/MHA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Master of Health Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32468&returnto=9453) |

##### MS/MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Master of Public Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32467&returnto=9453) |

##### MS/MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32386&returnto=9453) |

##### MS/PHARMD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Gerontology/Doctor of Pharmacy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32157&returnto=9453) |

##### MSAB

| # | 项目 | URL |
|---|------|-----|
| 1 | Aging Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32898&returnto=9453) |

##### DLAS

| # | 项目 | URL |
|---|------|-----|
| 1 | Longevity Arts and Sciences | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32731&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32159&returnto=9453) |
| 2 | Geroscience (Biology of Aging) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32869&returnto=9453) |

#### USC Leventhal School of Accounting

##### MAcc

| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31655&returnto=9453) |

##### MBT

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Taxation (Data and Analytics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32670&returnto=9453) |
| 2 | Business Taxation for Working Professionals | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31657&returnto=9453) |

##### JD/MBT

| # | 项目 | URL |
|---|------|-----|
| 1 | Juris Doctor/Master of Business Taxation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31658&returnto=9453) |

#### USC Marshall School of Business

##### MBA

| # | 项目 | URL |
|---|------|-----|
| 1 | Executive MBA Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31617&returnto=9453) |
| 2 | Full-time MBA Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31613&returnto=9453) |
| 3 | International MBA Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31618&returnto=9453) |
| 4 | MBA Program for Professionals and Managers | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31614&returnto=9453) |
| 5 | Online MBA Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31615&returnto=9453) |

##### MBV

| # | 项目 | URL |
|---|------|-----|
| 1 | Business for Veterans | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31641&returnto=9453) |

##### MMS

| # | 项目 | URL |
|---|------|-----|
| 1 | Management Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31631&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31632&returnto=9453) |
| 2 | Business Analytics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31634&returnto=9453) |
| 3 | Business Research | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31633&returnto=9453) |
| 4 | Entrepreneurship and Innovation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31636&returnto=9453) |
| 5 | Finance | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31637&returnto=9453) |
| 6 | Global Supply Chain Management (On‑Campus/Residential) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31638&returnto=9453) |
| 7 | Marketing (Marketing Analytics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32634&returnto=9453) |
| 8 | Marketing | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31639&returnto=9453) |
| 9 | Social Entrepreneurship | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31640&returnto=9453) |

##### MS/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Social Entrepreneurship/Master of Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32686&returnto=9453) |

##### Online

| # | 项目 | URL |
|---|------|-----|
| 1 | Global Supply Chain Management (MS) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32421&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31652&returnto=9453) |

#### USC Price School of Public Policy

##### Executive MHA

| # | 项目 | URL |
|---|------|-----|
| 1 | Health Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32313&returnto=9453) |

##### Executive MUP Online

| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32575&returnto=9453) |

##### IPPM

| # | 项目 | URL |
|---|------|-----|
| 1 | International Public Policy and Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32320&returnto=9453) |

##### MHA

| # | 项目 | URL |
|---|------|-----|
| 1 | Health Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32312&returnto=9453) |

##### MHA/MD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Health Administration/Doctor of Medicine | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32907&returnto=9453) |

##### MHA/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Health Administration/Master of Science in Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32343&returnto=9453) |

##### MHC/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Heritage Conservation/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32605&returnto=9453) |

##### MNLM

| # | 项目 | URL |
|---|------|-----|
| 1 | Nonprofit Leadership and Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32315&returnto=9453) |

##### MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration with Seoul National University | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32380&returnto=9453) |
| 2 | Public Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32318&returnto=9453) |

##### MPA/MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration/Master of Arts, Jewish Nonprofit Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32346&returnto=9453) |

##### MPA/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration/Master of Science in Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32342&returnto=9453) |

##### MPA/MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Administration/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32345&returnto=9453) |

##### MPDS

| # | 项目 | URL |
|---|------|-----|
| 1 | Planning and Development Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32317&returnto=9453) |

##### MPH/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Health/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32596&returnto=9453) |

##### MPP

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32319&returnto=9453) |

##### MPP/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Policy/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32175&returnto=9453) |

##### MPP/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Public Policy/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32598&returnto=9453) |

##### MRED

| # | 项目 | URL |
|---|------|-----|
| 1 | Dollinger Master of Real Estate Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32321&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32543&returnto=9453) |

##### MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32588&returnto=9453) |

##### MUP/MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban Planning/Master of Arts, Curatorial Practices and the Public Sphere | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32607&returnto=9453) |

##### MUP/MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban Planning/Master of Public Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32599&returnto=9453) |

##### MUP/MRED

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban Planning/Master of Real Estate Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32600&returnto=9453) |

##### MUP/MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Urban Planning/Master of Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32630&returnto=9453) |

##### DPPD

| # | 项目 | URL |
|---|------|-----|
| 1 | Policy, Planning, and Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32349&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Public Policy and Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32347&returnto=9453) |
| 2 | Urban Planning and Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32348&returnto=9453) |

##### MRED/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Real Estate Development/Juris Doctor | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32179&returnto=9453) |

#### USC Roski School of Art and Design

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Curatorial Practices and the Public Sphere | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31585&returnto=9453) |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Design | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32509&returnto=9453) |
| 2 | Fashion | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32834&returnto=9453) |
| 3 | Fine Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31584&returnto=9453) |

#### USC Rossier School of Education

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Education | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32946&returnto=9453) |
| 2 | Organizational Change and Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32887&returnto=9453) |
| 3 | Organizational Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32957&returnto=9453) |

##### MAT

| # | 项目 | URL |
|---|------|-----|
| 1 | Multiple Subject | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32501&returnto=9453) |
| 2 | Single Subject | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32502&returnto=9453) |
| 3 | Teaching, Teaching English to Speakers of Other Languages | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32018&returnto=9453) |

##### MEd

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Counseling | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32020&returnto=9453) |
| 2 | Enrollment Management and Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32532&returnto=9453) |
| 3 | Learning Design with AI and Emerging Technologies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32923&returnto=9453) |
| 4 | Postsecondary Administration and Student Affairs | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32022&returnto=9453) |
| 5 | School Counseling | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32023&returnto=9453) |
| 6 | Sports Administration and Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32924&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science for Learning Applications | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32900&returnto=9453) |
| 2 | Marriage and Family Therapy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32646&returnto=9453) |

##### EdD

| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32580&returnto=9453) |
| 2 | Global Executive | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32032&returnto=9453) |
| 3 | Mental Health Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32853&returnto=9453) |
| 4 | Organizational Change and Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32031&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Education | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32805&returnto=9453) |

##### PHD/MPP

| # | 项目 | URL |
|---|------|-----|
| 1 | Education/Public Policy | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32816&returnto=9453) |

#### USC School of Architecture

##### MAARS

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Architectural Research Studies (City Design and Housing) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32732&returnto=9453) |
| 2 | Advanced Architectural Research Studies (Performative Design and Technology) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32725&returnto=9453) |

##### MAAS

| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Architectural Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31589&returnto=9453) |

##### MAAS/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Advanced Architectural Studies/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32597&returnto=9453) |

##### MArch

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31588&returnto=9453) |

##### MBTech

| # | 项目 | URL |
|---|------|-----|
| 1 | Building Technology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32960&returnto=9453) |

##### MHC

| # | 项目 | URL |
|---|------|-----|
| 1 | Heritage Conservation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31566&returnto=9453) |

##### MHC/MARCH

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Heritage Conservation/Master of Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32915&returnto=9453) |

##### MHC/MLARCH

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Heritage Conservation/Master of Landscape Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32711&returnto=9453) |

##### MLArch

| # | 项目 | URL |
|---|------|-----|
| 1 | Landscape Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31565&returnto=9453) |

##### MLARCH/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Landscape Architecture/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32606&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Architecture | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31590&returnto=9453) |

#### USC School of Cinematic Arts

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Cinema and Media Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32450&returnto=9453) |
| 2 | Cinematic Arts (Media Arts, Games and Health) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31667&returnto=9453) |
| 3 | Media Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32970&returnto=9453) |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Animation and Digital Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31660&returnto=9453) |
| 2 | Cinematic Arts, Film and Television Production | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31664&returnto=9453) |
| 3 | Interactive Media (Games and Health) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31666&returnto=9453) |
| 4 | Interactive Media | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31668&returnto=9453) |
| 5 | Producing for Film, Television, and New Media | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31673&returnto=9453) |
| 6 | Writing for Screen and Television | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31675&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Game Design and Development | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32781&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Cinema and Media Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32451&returnto=9453) |
| 2 | Cinematic Arts (Critical Studies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31661&returnto=9453) |
| 3 | Cinematic Arts (Media Arts and Practice) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31671&returnto=9453) |

#### USC School of Dramatic Arts

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Theatre Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32013&returnto=9453) |

##### MFA

| # | 项目 | URL |
|---|------|-----|
| 1 | Theatre | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32012&returnto=9453) |

#### USC Suzanne Dworak-Peck School of Social Work

##### MSN-FNP

| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing, Family Nurse Practitioner | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32552&returnto=9453) |

##### MSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work (Integrative Social Work) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32798&returnto=9453) |
| 2 | Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32350&returnto=9453) |

##### MSW/JD

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Juris Doctor, Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32464&returnto=9453) |

##### MSW/MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Arts, Jewish Nonprofit Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32354&returnto=9453) |

##### MSW/MPA

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Public Administration | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32385&returnto=9453) |

##### MSW/MPH

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Public Health | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32353&returnto=9453) |

##### MSW/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Science, Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32158&returnto=9453) |

##### MSW/MUP

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Social Work/Master of Urban Planning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32734&returnto=9453) |

##### DSI

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Innovation | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32962&returnto=9453) |

##### DSW

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32454&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32355&returnto=9453) |

#### USC Thornton School of Music

##### MA

| # | 项目 | URL |
|---|------|-----|
| 1 | Early Music Performance Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32265&returnto=9453) |
| 2 | Music History and Literature Emphasis | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32264&returnto=9453) |

##### MM

| # | 项目 | URL |
|---|------|-----|
| 1 | Choral Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32251&returnto=9453) |
| 2 | Community Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32515&returnto=9453) |
| 3 | Composition | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32252&returnto=9453) |
| 4 | Conducting | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32253&returnto=9453) |
| 5 | Contemporary Teaching Practice | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32513&returnto=9453) |
| 6 | Jazz Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32254&returnto=9453) |
| 7 | Performance (Classical Guitar) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32256&returnto=9453) |
| 8 | Performance (Flute), (Oboe), (Clarinet), (Bassoon), (Saxophone), (French Horn), (Trumpet), (Trombone), (Tuba) or (Percussion) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32262&returnto=9453) |
| 9 | Performance (Keyboard Collaborative Arts) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32255&returnto=9453) |
| 10 | Performance (Organ) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32258&returnto=9453) |
| 11 | Performance (Piano) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32259&returnto=9453) |
| 12 | Performance (Studio Guitar) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32257&returnto=9453) |
| 13 | Performance (Violin), (Viola), (Violoncello), (Double Bass) or (Harp) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32260&returnto=9453) |
| 14 | Performance (Vocal Arts) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32438&returnto=9453) |
| 15 | Popular Music Teaching and Learning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32783&returnto=9453) |
| 16 | Sacred Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32263&returnto=9453) |
| 17 | Screen Scoring | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32441&returnto=9453) |
| 18 | Teaching and Learning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32446&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Arts Leadership | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32511&returnto=9453) |
| 2 | Music Industry | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32516&returnto=9453) |

##### DMA

| # | 项目 | URL |
|---|------|-----|
| 1 | Choral Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32268&returnto=9453) |
| 2 | Composition | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32269&returnto=9453) |
| 3 | Jazz Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32270&returnto=9453) |
| 4 | Performance - Organ, Percussion or Winds | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32271&returnto=9453) |
| 5 | Performance - Violin, Viola, Violoncello, Double Bass or Harp | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32655&returnto=9453) |
| 6 | Performance - Vocal Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32637&returnto=9453) |
| 7 | Performance — Classical Guitar | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32275&returnto=9453) |
| 8 | Performance — Early Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32274&returnto=9453) |
| 9 | Performance — Keyboard Collaborative Arts | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32273&returnto=9453) |
| 10 | Performance — Piano | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32272&returnto=9453) |
| 11 | Performance — Studio Guitar | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32276&returnto=9453) |
| 12 | Sacred Music | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32277&returnto=9453) |
| 13 | Teaching and Learning | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32445&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Music, Historical Musicology Emphasis, | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32278&returnto=9453) |

#### USC Viterbi School of Engineering

##### MCM

| # | 项目 | URL |
|---|------|-----|
| 1 | Construction Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32078&returnto=9453) |

##### MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace and Mechanical Engineering (Artificial Intelligence and Machine Learning) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32860&returnto=9453) |
| 2 | Aerospace and Mechanical Engineering (Computational Fluid and Solid Mechanics) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32037&returnto=9453) |
| 3 | Aerospace and Mechanical Engineering (Dynamics and Control) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32043&returnto=9453) |
| 4 | Aerospace Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32036&returnto=9453) |
| 5 | Aerospace Engineering/Engineering Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32038&returnto=9453) |
| 6 | Analytics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32116&returnto=9453) |
| 7 | Applied Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32528&returnto=9453) |
| 8 | Applied Physics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32714&returnto=9453) |
| 9 | Astronautical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32047&returnto=9453) |
| 10 | Biomedical Data Analytics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32679&returnto=9453) |
| 11 | Biomedical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32053&returnto=9453) |
| 12 | Chemical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32064&returnto=9453) |
| 13 | Civil Engineering (Emerging Technologies in Construction) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32864&returnto=9453) |
| 14 | Civil Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32135&returnto=9453) |
| 15 | Civil Engineering (Transportation Systems) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32076&returnto=9453) |
| 16 | Civil Engineering (Water and Waste Management) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32136&returnto=9453) |
| 17 | Communication Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32542&returnto=9453) |
| 18 | Communication Data Science Dual Degree with Tsinghua University School of Journalism and Communication | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32682&returnto=9453) |
| 19 | Computer Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32084&returnto=9453) |
| 20 | Computer Science (Artificial Intelligence) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32633&returnto=9453) |
| 21 | Computer Science (Data Science) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32091&returnto=9453) |
| 22 | Computer Science (Game Development) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32092&returnto=9453) |
| 23 | Computer Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32090&returnto=9453) |
| 24 | Computer Science (Scientists and Engineers) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32099&returnto=9453) |
| 25 | Computer Science Dual Degree with Tsinghua University School of Information Science and Technology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32100&returnto=9453) |
| 26 | Cyber Security Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32123&returnto=9453) |
| 27 | Data Science and Law | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32911&returnto=9453) |
| 28 | Electrical and Computer Engineering (Analog, Mixed-Signal and Radio-frequency Integrated Circuits) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32717&returnto=9453) |
| 29 | Electrical and Computer Engineering (Computer Architecture) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32906&returnto=9453) |
| 30 | Electrical and Computer Engineering (Computer Networks) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32892&returnto=9453) |
| 31 | Electrical and Computer Engineering (Electric Power) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32895&returnto=9453) |
| 32 | Electrical and Computer Engineering (Hardware Systems for Machine Learning) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32866&returnto=9453) |
| 33 | Electrical and Computer Engineering (Machine Learning and Data Science) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32616&returnto=9453) |
| 34 | Electrical and Computer Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32891&returnto=9453) |
| 35 | Electrical and Computer Engineering (VLSI Design) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32893&returnto=9453) |
| 36 | Electrical and Computer Engineering (Wireless Networks) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32894&returnto=9453) |
| 37 | Electrical and Computer Engineering/Engineering Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32897&returnto=9453) |
| 38 | Emerging Transportation Systems | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32867&returnto=9453) |
| 39 | Energy Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32873&returnto=9453) |
| 40 | Engineering Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32117&returnto=9453) |
| 41 | Environmental Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32632&returnto=9453) |
| 42 | Environmental Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32077&returnto=9453) |
| 43 | Financial Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32110&returnto=9453) |
| 44 | Health Systems Management Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32635&returnto=9453) |
| 45 | Healthcare Data Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32562&returnto=9453) |
| 46 | Industrial and Systems Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32118&returnto=9453) |
| 47 | Materials Engineering (Machine Learning) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32735&returnto=9453) |
| 48 | Materials Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32362&returnto=9453) |
| 49 | Materials Science and Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32886&returnto=9453) |
| 50 | Mechanical Engineering (Energy Conversion) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32138&returnto=9453) |
| 51 | Mechanical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32041&returnto=9453) |
| 52 | Mechanical Engineering (Nuclear Power) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32042&returnto=9453) |
| 53 | Mechanical Engineering (Quantitative Medical Engineering) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32861&returnto=9453) |
| 54 | Mechanical Engineering/Engineering Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32044&returnto=9453) |
| 55 | Medical Device and Diagnostic Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32055&returnto=9453) |
| 56 | Medical Imaging and Imaging Informatics | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32870&returnto=9453) |
| 57 | Operations Research Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32119&returnto=9453) |
| 58 | Petroleum Engineering (Digital Oilfield Technologies) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32673&returnto=9453) |
| 59 | Petroleum Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32069&returnto=9453) |
| 60 | Product Development Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32134&returnto=9453) |
| 61 | Quantum Information Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32677&returnto=9453) |
| 62 | Semiconductor Science and Technology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32959&returnto=9453) |
| 63 | Smart Manufacturing | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32889&returnto=9453) |
| 64 | Sustainable Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32871&returnto=9453) |
| 65 | Systems Architecting and Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32139&returnto=9453) |

##### MS/MS

| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Science, Petroleum Engineering/Master of Science, Engineering Management | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32625&returnto=9453) |

##### PhD

| # | 项目 | URL |
|---|------|-----|
| 1 | Aerospace Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32565&returnto=9453) |
| 2 | Aerospace Engineering and Computational Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32955&returnto=9453) |
| 3 | Astronautical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32373&returnto=9453) |
| 4 | Biomedical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32056&returnto=9453) |
| 5 | Chemical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32065&returnto=9453) |
| 6 | Civil Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32079&returnto=9453) |
| 7 | Computer Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32085&returnto=9453) |
| 8 | Computer Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32102&returnto=9453) |
| 9 | Electrical and Computer Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32896&returnto=9453) |
| 10 | Engineering (Environmental Engineering) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32080&returnto=9453) |
| 11 | Industrial and Systems Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32121&returnto=9453) |
| 12 | Materials Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32067&returnto=9453) |
| 13 | Mechanical Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32564&returnto=9453) |
| 14 | Mechanical Engineering and Computational Science | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32956&returnto=9453) |
| 15 | Petroleum Engineering | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32073&returnto=9453) |

### 2.2 Graduate Certificates — Complete List

Total graduate certificates: 169

#### Herman Ostrow School of Dentistry of USC

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Advanced Endodontics Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31981&returnto=9453) |
| 2 | Advanced Operative and Adhesive Dentistry Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31982&returnto=9453) |
| 3 | Advanced Operative and Adhesive Dentistry Certificate/MS, Craniofacial Biology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31983&returnto=9453) |
| 4 | Advanced Oral and Maxillofacial Surgery | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31984&returnto=9453) |
| 5 | Advanced Orofacial Pain Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31987&returnto=9453) |
| 6 | Advanced Orthodontics Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31989&returnto=9453) |
| 7 | Advanced Pediatric Dentistry Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31990&returnto=9453) |
| 8 | Advanced Periodontology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31991&returnto=9453) |
| 9 | Advanced Prosthodontics Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31992&returnto=9453) |
| 10 | Community Oral Health Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32573&returnto=9453) |
| 11 | Craniofacial Biology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31994&returnto=9453) |
| 12 | General Practice Residency | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31993&returnto=9453) |
| 13 | Geriatric Dentistry Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32539&returnto=9453) |
| 14 | Integrated MD Degree/Oral and Maxillofacial Surgery Certificate Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31985&returnto=9453) |
| 15 | Oral Pathology and Radiology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32485&returnto=9453) |
| 16 | Orofacial Pain Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32486&returnto=9453) |

#### Keck School of Medicine of USC

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Academic Medicine Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32406&returnto=9453) |
| 2 | Clinical Translational Research Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32844&returnto=9453) |
| 3 | Community Health Promotion Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32767&returnto=9453) |
| 4 | Epidemiology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32766&returnto=9453) |
| 5 | Global Health and Human Rights Leadership Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32762&returnto=9453) |
| 6 | Global Health Communications Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32764&returnto=9453) |
| 7 | Global Medicine Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32200&returnto=9453) |
| 8 | Narrative Medicine Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32883&returnto=9453) |
| 9 | Pain Medicine Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32487&returnto=9453) |
| 10 | Pain Science Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32723&returnto=9453) |
| 11 | Planning, Monitoring and Evaluation for Global Health and Development Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32765&returnto=9453) |
| 12 | Project Management in Global Health and Development Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32763&returnto=9453) |
| 13 | Spatial Sciences for Global Health Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32778&returnto=9453) |
| 14 | Stem Cell Biology and Regenerative Medicine Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32444&returnto=9453) |
| 15 | Translation and Entrepreneurship in Biomedical Sciences Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32594&returnto=9453) |
| 16 | Translational Biotechnology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32561&returnto=9453) |

#### USC Alfred E. Mann School of Pharmacy and Pharmaceutical Sciences

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Advanced Pharmacy Practice Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32687&returnto=9453) |
| 2 | Biopharmaceutical Marketing Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32743&returnto=9453) |
| 3 | Clinical Research Design and Management Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32301&returnto=9453) |
| 4 | Healthcare Analytics Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32884&returnto=9453) |
| 5 | Healthcare and Biopharmaceutical Business Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32825&returnto=9453) |
| 6 | Healthcare Decision Analysis Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32452&returnto=9453) |
| 7 | Medical Product Quality Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32411&returnto=9453) |
| 8 | Patient and Product Safety Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32303&returnto=9453) |
| 9 | Pharmacoepidemiology and Drug Safety Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32903&returnto=9453) |
| 10 | Preclinical Drug Development Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32304&returnto=9453) |
| 11 | Regulatory and Clinical Affairs Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32305&returnto=9453) |
| 12 | Sports Pharmacy Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32890&returnto=9453) |

#### USC Annenberg School for Communication and Journalism

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Health Communication Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31954&returnto=9453) |
| 2 | International and Intercultural Communication Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31955&returnto=9453) |
| 3 | Journalism Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31971&returnto=9453) |
| 4 | Marketing Communication Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31956&returnto=9453) |
| 5 | New Communication Technologies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31958&returnto=9453) |
| 6 | Public Policy Advocacy Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32390&returnto=9453) |
| 7 | Strategic Corporate and Organizational Communication Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31959&returnto=9453) |

#### USC Dornsife College of Letters, Arts and Sciences

| # | Certificate | URL |
|---|-------------|-----|
| 1 | AI for Molecular Biology Intensive | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32940&returnto=9453) |
| 2 | Cognitive Science Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32865&returnto=9453) |
| 3 | East Asian Area Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31770&returnto=9453) |
| 4 | Gender and Sexuality Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32740&returnto=9453) |
| 5 | Geographic Information Science and Technology Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31942&returnto=9453) |
| 6 | Geospatial Intelligence Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31943&returnto=9453) |
| 7 | Geospatial Leadership Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31944&returnto=9453) |
| 8 | History of Collecting and Display Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31714&returnto=9453) |
| 9 | Jewish Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32656&returnto=9453) |
| 10 | Latinx and Latin American Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32721&returnto=9453) |
| 11 | Religious Studies Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32505&returnto=9453) |
| 12 | Remote Sensing for Earth Observation Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32629&returnto=9453) |
| 13 | Science and Technology Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32657&returnto=9453) |
| 14 | Spatial Analytics Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31945&returnto=9453) |
| 15 | Survey Design and Data Analysis Intensive | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32930&returnto=9453) |
| 16 | Translation Studies Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32570&returnto=9453) |
| 17 | Visual Anthropology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31707&returnto=9453) |
| 18 | Visual Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31715&returnto=9453) |
| 19 | Writing and Responsible AI Intensive | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32963&returnto=9453) |

#### USC Gould School of Law

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Alternative Dispute Resolution Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32182&returnto=9453) |
| 2 | Business Law Certificate (On-Campus) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32183&returnto=9453) |
| 3 | Business Law Certificate (Online) | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32185&returnto=9453) |
| 4 | Certificate in U.S. Legal Studies | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32400&returnto=9453) |
| 5 | Compliance Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32483&returnto=9453) |
| 6 | Dispute Resolution Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32820&returnto=9453) |
| 7 | Entertainment Law and Industry Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32484&returnto=9453) |
| 8 | Financial Compliance Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32555&returnto=9453) |
| 9 | Health Care Compliance Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32556&returnto=9453) |
| 10 | Human Resources Law and Compliance Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32557&returnto=9453) |
| 11 | International Law and Human Rights Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32968&returnto=9453) |
| 12 | Law and Advocacy Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32914&returnto=9453) |
| 13 | Law and Artificial Intelligence Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32863&returnto=9453) |
| 14 | Law and Government Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32831&returnto=9453) |
| 15 | Media and Entertainment Law Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32722&returnto=9453) |
| 16 | Privacy Law and Cybersecurity Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32652&returnto=9453) |
| 17 | Public Interest Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32410&returnto=9453) |
| 18 | Real Estate Law Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32847&returnto=9453) |
| 19 | Social Work Administration Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32774&returnto=9453) |
| 20 | Sports Law and Negotiation Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32937&returnto=9453) |
| 21 | Technology and Entrepreneurship Law Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32403&returnto=9453) |
| 22 | Transnational Law and Business Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32520&returnto=9453) |

#### USC Independent Health Professions at the Herman Ostrow School of Dentistry

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Foundations of Lifestyle Redesign® Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32785&returnto=9453) |
| 2 | Sensory Processing and Sensory Integration Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32777&returnto=9453) |

#### USC Leonard Davis School of Gerontology

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Doctor of Pharmacy/Graduate Certificate in Gerontology | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32631&returnto=9453) |
| 2 | Gerontology Graduate Level Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32152&returnto=9453) |
| 3 | Gerontology Online Graduate Level Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32153&returnto=9453) |

#### USC Leventhal School of Accounting

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Business Taxation Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32804&returnto=9453) |

#### USC Marshall School of Business

| # | Certificate | URL |
|---|-------------|-----|
| 1 | AI in Business Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32926&returnto=9453) |
| 2 | Business Analytics Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31643&returnto=9453) |
| 3 | Financial Analysis and Valuation Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31645&returnto=9453) |
| 4 | Food Industry Management Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31596&returnto=9453) |
| 5 | Marketing Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31648&returnto=9453) |
| 6 | Optimization and Supply Chain Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31649&returnto=9453) |
| 7 | Product Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32901&returnto=9453) |
| 8 | Risk Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32899&returnto=9453) |
| 9 | Strategy and Management Consulting Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32412&returnto=9453) |
| 10 | Sustainability and Business Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31650&returnto=9453) |
| 11 | Technology Commercialization Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31651&returnto=9453) |

#### USC Price School of Public Policy

| # | Certificate | URL |
|---|-------------|-----|
| 1 | City/County Management Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32322&returnto=9453) |
| 2 | Health Management and Policy Programs Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32327&returnto=9453) |
| 3 | Homeland Security and Public Policy Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32330&returnto=9453) |
| 4 | International Policy and Planning Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32333&returnto=9453) |
| 5 | Nonprofit Management and Policy Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32324&returnto=9453) |
| 6 | Political Management Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32325&returnto=9453) |
| 7 | Public Financial Management Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32326&returnto=9453) |
| 8 | Public Management Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32328&returnto=9453) |
| 9 | Public Policy Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32329&returnto=9453) |
| 10 | Real Estate Development Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32332&returnto=9453) |
| 11 | Social Innovation Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32475&returnto=9453) |
| 12 | Social Justice Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32442&returnto=9453) |
| 13 | Sustainable Policy and Planning Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32331&returnto=9453) |
| 14 | Transportation Planning Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32713&returnto=9453) |

#### USC Roski School of Art and Design

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Performance Studies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32681&returnto=9453) |

#### USC Rossier School of Education

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Gifted Education Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32027&returnto=9453) |
| 2 | Learning Design with AI and Emerging Technologies Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32925&returnto=9453) |
| 3 | Postsecondary Administration and Student Affairs Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32936&returnto=9453) |
| 4 | Postsecondary Educational Counseling Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32965&returnto=9453) |
| 5 | School Counseling, Post-Master’s Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32818&returnto=9453) |
| 6 | Sports Administration and Leadership Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32966&returnto=9453) |

#### USC School of Architecture

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Architecture Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31563&returnto=9453) |
| 2 | Building Facade Art Science and Technology Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32772&returnto=9453) |
| 3 | Building Science Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31561&returnto=9453) |
| 4 | City Design and Housing Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32855&returnto=9453) |
| 5 | Heritage Conservation Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31562&returnto=9453) |
| 6 | Landscape Architecture Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31560&returnto=9453) |
| 7 | Lighting Design Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32969&returnto=9453) |
| 8 | Performative Design and Technology Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32856&returnto=9453) |
| 9 | Sustainable Design Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31564&returnto=9453) |

#### USC School of Cinematic Arts

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Business of Entertainment Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31676&returnto=9453) |
| 2 | Cinematic Arts Archiving and Preservation Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32482&returnto=9453) |
| 3 | Digital Media and Culture Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31672&returnto=9453) |
| 4 | Media and Entertainment Management Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=31957&returnto=9453) |
| 5 | Writing for Screen and Television Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32394&returnto=9453) |

#### USC Suzanne Dworak-Peck School of Social Work

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Advanced Clinical Social Work Practice Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32752&returnto=9453) |
| 2 | Advanced Integrative Social Work and Nursing Practice Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32753&returnto=9453) |
| 3 | Aging and Health Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32754&returnto=9453) |
| 4 | Child and Family Well-Being Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32756&returnto=9453) |
| 5 | Ending Homelessness Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32755&returnto=9453) |
| 6 | Evaluation and Research in Community and Environmental Contexts Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32912&returnto=9453) |
| 7 | Interprofessional Education Caregiving Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32821&returnto=9453) |
| 8 | Social Work Practice in Addiction Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32760&returnto=9453) |
| 9 | Telebehavioral Health Practice Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32822&returnto=9453) |
| 10 | Trauma Informed Practices in Educational Settings Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32786&returnto=9453) |
| 11 | Visual Social Work Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32787&returnto=9453) |
| 12 | Youth Advocacy Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32913&returnto=9453) |

#### USC Thornton School of Music

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Artist Diploma Program | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32363&returnto=9453) |
| 2 | Arts Leadership Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32266&returnto=9453) |
| 3 | Music Performance Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32267&returnto=9453) |

#### USC Viterbi School of Engineering

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Applied Data Science Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32715&returnto=9453) |
| 2 | Astronautical Engineering Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32048&returnto=9453) |
| 3 | Biomedical Data Analytics Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32967&returnto=9453) |
| 4 | Data Science Foundations Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32716&returnto=9453) |
| 5 | Health Systems Operations Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32369&returnto=9453) |
| 6 | Medical Imaging and Imaging Informatics Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32971&returnto=9453) |
| 7 | Operations Research and Artificial Intelligence Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32919&returnto=9453) |
| 8 | Systems Architecting and Engineering Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32140&returnto=9453) |
| 9 | Technology for National Security Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32823&returnto=9453) |
| 10 | Transportation Systems Graduate Certificate | [链接](https://catalogue.usc.edu/preview_program.php?catoid=22&poid=32081&returnto=9453) |

### 2.3 Graduate Admissions Model

USC graduate admissions is **decentralized**. Each school/program sets its own deadlines and requirements.

**Key facts:**
- Application portal: [USC Graduate Application](https://gradadm.usc.edu/)
- Application fee: $120 ($105 for programs beginning Fall 2026)
- Up to 3 programs per term may be applied to simultaneously
- PhD priority deadline: December 1 (varies by program)
- Master's/certificate deadlines: set by individual departments
- GRE/GMAT: required by most programs (scores valid 5 years)
- ETS school code: 4852
- Recommendation letters: number varies by program
- Statement of intent: required by most programs

**Programs with separate applications:**
- Chemistry, PhD
- Physics, PhD

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | Common Application | admission.usc.edu |
| Early Action (EA) 截止日期 | November 1 | admission.usc.edu/prospective-students/how-to-apply/first-year-students/ |
| Early Decision (ED) 截止日期 | November 1 | 同上 |
| Regular Decision (表演艺术专业) 截止日期 | December 1 | 同上 |
| Regular Decision (大多数专业) 截止日期 | January 10 | 同上 |
| 财务援助申请截止日期 (FAFSA/CSS Profile) | February 4, 2026 | financialaid.usc.edu |
| SAT/ACT 政策 | Test-Optional (2026-27学年) | admission.usc.edu/prospective-students/how-to-apply/international-students/ |
| Superscore 政策 | 未明确说明 | - |
| 面试政策 | 不进行录取面试 | admission.usc.edu |
| 推荐信要求 | 1封推荐信 | admission.usc.edu/prospective-students/how-to-apply/first-year-students/ |
| 作品集 | 部分专业要求 (如建筑、艺术、电影、音乐等) | 同上 |
| 申请费 | $85 (通过Common App) | commonapp.org |
| 录取通知 | 滚动录取，具体日期未公布 | - |
| 入学押金截止日期 | May 1 (National Decision Day) | 通用信息 |

### 3.2 Undergraduate English Proficiency Table

| 考试 | 最低分数 | 推荐分数 | 备注 |
|------|---------|---------|------|
| TOEFL iBT (2026年1月21日前考试) | 100 (各项≥20) | 111+ (各项≥25) | 不接受 TOEFL ITP Plus for China |
| TOEFL iBT (2026年1月21日后考试) | 5 (各项≥4) | - | ETS新评分体系 |
| IELTS | 7.0 | - | 接受 IELTS Indicator |
| Cambridge C1 Advanced | 185 (各项≥169) | - | - |
| PTE Academic | 68 | - | - |
| Duolingo English Test | 130 | - | 入学后需参加ISE考试 |

**适用条件**: 所有母语非英语的国际申请者必须提交英语水平考试成绩。不提供豁免。

**Source**: admission.usc.edu/prospective-students/how-to-apply/international-students/

### 3.3 Graduate — Global Rules

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请系统 | USC Graduate Application | gradadm.usc.edu |
| 申请费 | $120 ($105 for Fall 2026 programs) | gradadm.usc.edu/prospective-students/how-to-apply/ |
| Marshall商学院申请费 | 因项目而异 | 同上 |
| PhD优先截止日期 | December 1 | 同上 |
| 硕士/证书截止日期 | 因项目而异 | 同上 |
| GRE/GMAT | 大多数项目要求 (5年内有效) | 同上 |
| ETS学校代码 | 4852 | 同上 |
| 推荐信 | 因项目而异 | 同上 |
| 个人陈述 | 大多数项目要求 | 同上 |
| 最多申请项目数 | 每学期3个 | 同上 |
| 英语水平要求 (TOEFL) | PhD: 100+ (各项≥20); Master's: 90+ (各项≥20) | gradadm.usc.edu/prospective-international-students/english-proficiency/ |
| 英语水平要求 (IELTS) | Master's: 6.5+ (各项≥6.0) | 同上 |
| 英语水平考试有效期 | 2年内 | 同上 |
| 英语豁免条件 | 美国学位完成者或英语国家学位持有者 | 同上 |
| CGS April 15等效日期 | 未明确说明 | - |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

| 费用项目 | 金额 (美元) | 说明 |
|---------|-----------|------|
| 学费 (Tuition, 12-18 units/semester) | $75,384 | 两学期 |
| 费用 (Fees) | $1,952 | 两学期 |
| 住宿 (Housing, on-campus) | $13,510 | 校内住宿 |
| 餐饮 (Food) | $8,442 | 校内餐饮 |
| 书本/用品 (Books/Supplies) | $670 | - |
| 交通 (Transportation) | $1,188 | - |
| 个人/杂项 (Personal/Misc) | $2,016 | - |
| **总计 (Total, on-campus)** | **$103,162** | - |
| 新生费用 (New Student Fee) | +$450 | 第一学期 |

**其他住宿选项:**
- 校外住宿: $13,140 (住宿) + $8,442 (餐饮) = $102,792 总计
- 通勤: $8,776 (住宿) + $3,762 (餐饮) = $94,630 总计

**Source**: admission.usc.edu/financial-aid/ + affordability.usc.edu

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 | 来源 |
|------|-----|------|
| 学费免除收入门槛 | 家庭年收入 ≤$80,000 | admission.usc.edu/financial-aid/ |
| Need-blind/Need-aware (国内) | Need-blind (满足所有合格学生的全部需求) | 同上 |
| Need-blind/Need-aware (国际) | Need-aware (不提供need-based aid给国际学生) | admission.usc.edu/prospective-students/how-to-apply/international-students/ |
| 国际学生Merit奖学金 | 可申请 (基于综合评审，非need-based) | 同上 |
| 2024-25年财务援助总额 | $9.04亿 | admission.usc.edu/financial-aid/ |
| 获得Merit奖学金比例 | 约1/3新生 | 同上 |
| 近2/3本科生获得某种形式的财务援助 | 是 | 同上 |

### 4.3 Graduate Cost & Funding Framework

| 维度 | 值 | 来源 |
|------|-----|------|
| 申请费 | $120 ($105 for Fall 2026) | gradadm.usc.edu |
| 费用减免 | 可申请 (需提供证明文件) | 同上 |
| 资助类型 | RA/TA/Fellowship/Grant (因项目而异) | 各项目网站 |
| PhD资助 | 大多数PhD项目提供全额资助 | 各项目网站 |

---

## SECTION 5 — Evidence Chain Index

### Evidence Blocks

```yaml
E-U-001:
  field: undergraduate.deadlines.early_action
  value: "November 1"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/first-year-students/
  source_snippet: "Early Action (most majors) — November 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.early_decision
  value: "November 1"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/first-year-students/
  source_snippet: "Early Decision (most majors) — November 1"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.deadlines.regular_decision
  value: "January 10 (most majors); December 1 (performing arts)"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/first-year-students/
  source_snippet: "Regular Decision (performing arts majors) — December 1; Regular Decision (most majors) — January 10"
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.financial_aid.deadline
  value: "February 4, 2026"
  source_url: https://financialaid.usc.edu/
  source_snippet: "The 2026-27 FAFSA and CSS Profile will be available on October 1, 2025. The deadline for Regular Decision applicants is February 4, 2026."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.testing.policy
  value: "Test-Optional for 2026-27"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/international-students/
  source_snippet: "USC will continue our test-optional policy for the upcoming year, meaning that first-year applicants to the 2026-27 academic year are not required to send SAT or ACT scores to apply."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.cost.tuition_2026_2027
  value: "$75,384"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Tuition (12-18 units for two semesters) $75,384"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_on_campus
  value: "$103,162"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Total** $103,162"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.cost.fees
  value: "$1,952"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Fees $1,952"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.cost.housing
  value: "$13,510 (on-campus)"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Housing* $13,510"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.cost.food
  value: "$8,442"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Food* $8,442"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.financial_aid.tuition_free_threshold
  value: "Family income ≤$80,000"
  source_url: https://admission.usc.edu/financial-aid/
  source_snippet: "Incoming first-year students from U.S. families with an annual income of $80,000 or less with typical assets can attend USC tuition free."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.international.need_aware
  value: true
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/international-students/
  source_snippet: "USC does not offer need-based financial aid for international applicants."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-013:
  field: undergraduate.english_proficiency.toefl_min
  value: "100 (each section ≥20)"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/international-students/
  source_snippet: "TOEFL (or TOEFL iBT Special Home Edition): for an exam taken prior to 21 January 2026, a minimum score of 100 and no less than a score of 20 in each section."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.english_proficiency.ielts_min
  value: "7.0"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/international-students/
  source_snippet: "IELTS (or IELTS Indicator) score of 7."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.english_proficiency.duolingo_min
  value: "130"
  source_url: https://admission.usc.edu/prospective-students/how-to-apply/international-students/
  source_snippet: "If you are not able to sit for one of the USC-approved examinations, you can instead sit for the Duolingo English Test. You must achieve a minimum score of 130."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$120 ($105 for Fall 2026)"
  source_url: https://gradadm.usc.edu/prospective-students/how-to-apply/
  source_snippet: "The application fee for most USC graduate programs is $120 ($105 for programs beginning in Fall 2026)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-002:
  field: graduate.deadlines.phd_priority
  value: "December 1"
  source_url: https://gradadm.usc.edu/prospective-students/how-to-apply/
  source_snippet: "PhD Programs: The priority deadline for Ph.D. applicants is December 1."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-003:
  field: graduate.testing.gre_required
  value: "Required by most programs (scores valid 5 years)"
  source_url: https://gradadm.usc.edu/prospective-students/how-to-apply/
  source_snippet: "Most USC graduate programs require either GRE or GMAT scores."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_proficiency.toefl_phd
  value: "100+ (each section ≥20)"
  source_url: https://gradadm.usc.edu/prospective-international-students/english-proficiency/
  source_snippet: "PhD programs: 100 or above, with 20 or above in each section."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-005:
  field: graduate.english_proficiency.toefl_masters
  value: "90+ (each section ≥20)"
  source_url: https://gradadm.usc.edu/prospective-international-students/english-proficiency/
  source_snippet: "Master's degree programs: 90 or above, with 20 or above in each section."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-006:
  field: graduate.english_proficiency.ielts_masters
  value: "6.5+ (each band ≥6.0)"
  source_url: https://gradadm.usc.edu/prospective-international-students/english-proficiency/
  source_snippet: "Master's degree programs: 6.5 or above, with 6 or above on each band."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-007:
  field: graduate.max_programs_per_term
  value: 3
  source_url: https://gradadm.usc.edu/prospective-students/how-to-apply/
  source_snippet: "You may apply to up to three programs per term."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-G-008:
  field: graduate.ets_school_code
  value: 4852
  source_url: https://gradadm.usc.edu/prospective-students/how-to-apply/
  source_snippet: "If you are sending GRE scores: USC's ETS school code is 4852."
  capture_date: 2026-07-05
  evidence_type: official_webpage

E-P-001:
  field: program_counts.total
  value: 1149
  source_url: https://catalogue.usc.edu/content.php?catoid=22&navoid=9453
  source_snippet: "Programs by School - 1149 program links extracted from catalogue"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
usc-knowledge-base-v2/
├── 00-institution-overview.md          # Section 0: counts, hierarchy, degree inventory, matrix
├── 01-undergraduate-education.md       # Section 1: UG majors by school
├── 02-graduate-education.md            # Section 2: Grad programs by school
├── 03-deadlines-requirements.md        # Section 3: deadlines, test policy, English proficiency
├── 04-costs-financial-aid.md           # Section 4: COA, aid policy, grad funding
├── 05-evidence-chain.md                # Section 5: YAML evidence blocks
├── 06-weknora-manifest.md              # Section 6: this file
├── 07-comparison-framework.md          # Section 7: cross-school comparison
├── programs/
│   ├── dornsife-ug.md                  # One chunk per school (UG)
│   ├── dornsife-grad.md                # One chunk per school (Grad)
│   ├── marshall-ug.md
│   ├── marshall-grad.md
│   ├── viterbi-ug.md
│   ├── viterbi-grad.md
│   └── ... (all 23 schools)
└── minors/
    ├── dornsife-minors.md
    ├── marshall-minors.md
    └── ... (all schools with minors)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "usc-knowledge-base-v2"
  school: "<home college>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://catalogue.usc.edu/content.php?catoid=22&navoid=9453
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE/GMAT requirements | 各项目网站 |
| P0 | Per-program TOEFL/IELTS minimums (grad) | 各项目网站 |
| P1 | Financial aid notification dates | admission.usc.edu/financial-aid/ |
| P1 | Enrollment deposit deadline | admission.usc.edu |
| P1 | Transfer admission requirements | admission.usc.edu/prospective-students/how-to-apply/transfer-students/ |
| P2 | Per-program acceptance rates | 各项目网站 |
| P2 | Average GPA of admitted students | admission.usc.edu |
| P2 | Graduate cost of attendance | gradadm.usc.edu |
| P2 | Merit scholarship amounts | admission.usc.edu/cost-and-financial-aid/scholarships/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | USC | MIT | Stanford | Harvard | Caltech |
|------|-----|-----|----------|---------|---------|
| 类型 | 私立 | 私立 | 私立 | 私立 | 私立 |
| 位置 | Los Angeles, CA | Cambridge, MA | Stanford, CA | Cambridge, MA | Pasadena, CA |
| UG学费/年 | $75,384 | - | - | - | - |
| UG总费用/年 | $103,162 | - | - | - | - |
| Need-blind (国内) | Yes | - | - | - | - |
| Need-blind (国际) | No (Need-aware) | - | - | - | - |
| EA截止日期 | Nov 1 | - | - | - | - |
| RD截止日期 | Jan 10 | - | - | - | - |
| SAT/ACT要求 | Test-Optional | - | - | - | - |
| TOEFL最低 (UG) | 100 | - | - | - | - |
| IELTS最低 (UG) | 7.0 | - | - | - | - |
| 学费免除门槛 | ≤$80k income | - | - | - | - |
| 项目总数 (Rule 1) | 719 | - | - | - | - |
| 学院数 (Rule 2) | 23 | - | - | - | - |
| 研究生申请费 | $120 | - | - | - | - |
| PhD优先截止 | Dec 1 | - | - | - | - |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admission.usc.edu, gradadm.usc.edu, financialaid.usc.edu, catalogue.usc.edu, affordability.usc.edu, www.usc.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
