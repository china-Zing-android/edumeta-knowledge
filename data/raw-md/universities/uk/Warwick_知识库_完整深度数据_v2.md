# University of Warwick Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: WebFetch + curl (SiteBuilder2 API)
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department/subject → degree-level → programme
> **Document version**: v2.0 (deep)
> **Region**: UK (England)
> **Russell Group**: Yes
> **QS World Ranking 2026**: #69 (QS)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG, 含 Foundation/Placement 变体) | 192 |
| 本科学位专业 (UG, 核心项目) | 168 |
| 研究生授课型 (PG Taught: MSc/MA/LLM/MBA/PGCert/PGDip 等) | 151 |
| 研究生研究型 (PG Research: PhD/MPhil/MRes/MSc by Research 等) | 73 |
| 研究生项目总计 (PG Taught + Research) | 263 |
| **学位项目总计 (UG核心 + PG)** | **431** |
| 学院 (Faculty) | 3 |
| 学术系/学校 (Department/School) | ~30 |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Warwick
├── Faculty of Arts [学院]
│   ├── Classics and Ancient History [系]
│   ├── English and Comparative Literary Studies [系]
│   ├── History [系]
│   ├── School of Creative Arts, Performance and Visual Cultures [系]
│   │   ├── Film and Television Studies
│   │   ├── History of Art
│   │   ├── Theatre and Performance Studies
│   │   └── Warwick Writing Programme
│   ├── School of Modern Languages and Cultures [系]
│   └── School for Cross-faculty Studies [系]
│       ├── Global Sustainable Development
│       ├── Liberal Arts
│       └── Design Studies
├── Faculty of Science, Engineering and Medicine (SEM) [学院]
│   ├── Chemistry [系]
│   ├── Computer Science (DCS) [系]
│   ├── Engineering [系]
│   ├── Life Sciences [系]
│   ├── Mathematics [系]
│   ├── Physics [系]
│   ├── Psychology [系]
│   ├── Statistics [系]
│   ├── Warwick Manufacturing Group (WMG) [系]
│   └── Warwick Medical School [系]
├── Faculty of Social Sciences [学院]
│   ├── Economics [系]
│   ├── Philosophy [系]
│   ├── Politics and International Studies (PAIS) [系]
│   ├── School of Law [系]
│   ├── Sociology [系]
│   ├── Warwick Business School (WBS) [系]
│   └── School of Education, Learning and Communication Sciences (SELCS) [系]
│       ├── Applied Linguistics
│       ├── Centre for Teacher Education (CTE)
│       └── Education Studies
└── Cross-Faculty Units
    ├── Centre for Interdisciplinary Methodologies (CIM)
    ├── Institute for Advanced Teaching and Learning (IATL)
    └── Warwick Q-Step
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本校项目数量 |
|---------|------|------|------------|
| BA | Bachelor of Arts | 本科 | 81 |
| BSc | Bachelor of Science | 本科 | 43 |
| BASc | Bachelor of Applied Science | 本科 | 16 |
| BEng | Bachelor of Engineering | 本科 | 11 |
| MEng | Master of Engineering (Integrated) | 本科 | 11 |
| MBio | Master of Bioscience (Integrated) | 本科 | 10 |
| LLB | Bachelor of Laws | 本科 | 7 |
| MChem | Master of Chemistry (Integrated) | 本科 | 4 |
| MSci | Master in Science (Integrated) | 本科 | 2 |
| MPhys | Master of Physics (Integrated) | 本科 | 2 |
| MMath | Master of Mathematics (Integrated) | 本科 | 1 |
| MMathPhys | Master of Math & Physics (Integrated) | 本科 | 1 |
| MMathStat | Master of Math & Statistics (Integrated) | 本科 | 1 |
| MMORSE | Master of MORSE (Integrated) | 本科 | 1 |
| MSc | Master of Science | 研究生 | 66 |
| MA | Master of Arts | 研究生 | 43 |
| MPhil/PhD | Master of Philosophy / Doctor of Philosophy | 研究生 | 33 |
| PhD | Doctor of Philosophy | 研究生 | 15 |
| MA by Research | Master of Arts by Research | 研究生 | 11 |
| PGA | Postgraduate Award | 研究生 | 9 |
| MSc by Research | Master of Science by Research | 研究生 | 6 |
| LLM | Master of Laws | 研究生 | 5 |
| PGCert | Postgraduate Certificate | 研究生 | 4 |
| MRes/PhD | Master of Research / Doctor of Philosophy | 研究生 | 3 |
| PGDip | Postgraduate Diploma | 研究生 | 3 |
| MASc | Master of Applied Science | 研究生 | 2 |
| MPH | Master of Public Health | 研究生 | 2 |
| DBA | Doctor of Business Administration | 研究生 | 1 |
| EngD | Engineering Doctorate | 研究生 | 1 |
| MPhil | Master of Philosophy | 研究生 | 1 |
| MRes | Master of Research | 研究生 | 1 |
| MBChB | Bachelor of Medicine (Graduate Entry) | 研究生 | 1 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

#### 本科 (Undergraduate)

| 学院 \ 学位 | BA | BSc | BASc | BEng | MEng | MBio | LLB | MChem | MSci | MPhys | MMath | MMathPhys | MMathStat | MMORSE | 合计 |
|------------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|------|
| Arts | 55 | | 15 | | | | | | | | | | | | **70** |
| Science, Engineering and Medicine | | 24 | | 11 | 11 | 9 | | 4 | 2 | 2 | 1 | 1 | 1 | 1 | **67** |
| Social Sciences | 26 | 17 | | | | | 7 | | | | | | | | **50** |
| Unknown | | 2 | 1 | | | 1 | | | | | | | | | **4** |
| **合计** | 81 | 43 | 16 | 11 | 11 | 10 | 7 | 4 | 2 | 2 | 1 | 1 | 1 | 1 | **191** |

#### 研究生 (Postgraduate) — 按学位类型

| 学位类型 | 授课型 (Taught) | 研究型 (Research) | 合计 |
|---------|----------------|-----------------|------|
| MSc | 66 | 6 | 72 |
| MA | 43 | 12 | 55 |
| MPhil/PhD | 0 | 33 | 33 |
| PhD | 0 | 15 | 15 |
| LLM | 5 | 1 | 6 |
| MASc | 4 | 0 | 4 |
| MBA/DBA | 1 | 0 | 1 |
| PGCert/PGDip/PGA | 16 | 0 | 16 |
| MRes/EngD | 2 | 4 | 6 |
| 其他 | 6 | 0 | 6 |
| **合计** | **150** | **73** | **263** |

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

Warwick has 3 faculties: Arts, Science/Engineering/Medicine (SEM), and Social Sciences. See Section 0.2 for the full hierarchy tree. Undergraduate programmes are offered across ~30 departments/schools.

### 1.2 Undergraduate programmes — grouped by 学院 > 系 > 学位级别

#### Arts

##### Classics and Ancient History

###### BA

| # | Programme |
|---|-----------|
| 1 | Ancient History and Classical Archaeology (BA) Part-time |
| 2 | Ancient History and Classical Archaeology BA |
| 3 | Ancient History and Classical Archaeology with Study in Europe BA |
| 4 | Classical Civilisation (BA) Part-time |
| 5 | Classical Civilisation BA |
| 6 | Classical Civilisation with Study in Europe BA |
| 7 | Classics (Ancient Greek) with Study in Europe BA |
| 8 | Classics (BA) Part-time |
| 9 | Classics (Latin) with Study in Europe BA |
| 10 | Classics BA |

##### Design Studies

###### BASc

| # | Programme |
|---|-----------|
| 1 | Design for Sustainable Innovation BASc |

##### English Literature

###### BA

| # | Programme |
|---|-----------|
| 1 | Classics and English BA |
| 2 | English Literature BA |
| 3 | English Literature and Creative Writing BA |
| 4 | English and Classical Civilisation BA |
| 5 | English and Cultural Studies part-time BA |

##### Film and Television Studies

###### BA

| # | Programme |
|---|-----------|
| 1 | Film Studies BA |
| 2 | Film and Literature BA |

##### Global Sustainable Development

###### BASc

| # | Programme |
|---|-----------|
| 1 | Design and Global Sustainable Development BASc |
| 2 | Economic Studies and Global Sustainable Development BASc |
| 3 | Education Studies and Global Sustainable Development BASc |
| 4 | Global Sustainable Development BASc |
| 5 | Global Sustainable Development and Business Studies BASc |
| 6 | Life Sciences and Global Sustainable Development BASc |

##### History

###### BA

| # | Programme |
|---|-----------|
| 1 | English and History BA |
| 2 | History BA |
| 3 | History part time BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | History and Global Sustainable Development BASc |

##### History of Art

###### BA

| # | Programme |
|---|-----------|
| 1 | History of Art BA |

##### Liberal Arts

###### BA

| # | Programme |
|---|-----------|
| 1 | Liberal Arts BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Liberal Arts and Sciences BASc |

##### Media and Creative Industries

###### BA

| # | Programme |
|---|-----------|
| 1 | Media and Creative Industries BA |

##### Modern Languages and Cultures

###### BA

| # | Programme |
|---|-----------|
| 1 | English and French BA |
| 2 | English and German BA |
| 3 | English and Hispanic Studies BA |
| 4 | English and Italian BA |
| 5 | French Studies BA |
| 6 | French and Economics BA |
| 7 | French and History BA |
| 8 | German Studies BA |
| 9 | German and Economics BA |
| 10 | German and History BA |
| 11 | Hispanic Studies BA |
| 12 | Hispanic Studies and Economics BA |
| 13 | Hispanic Studies and History BA |
| 14 | History and Italian BA |
| 15 | History of Art with Italian BA |
| 16 | Italian Studies BA |
| 17 | Italian and Classics BA |
| 18 | Italian and Economics BA |
| 19 | Modern Languages BA |
| 20 | Modern Languages and Economics BA |
| 21 | Modern Languages and Linguistics BA |
| 22 | Modern Languages with Linguistics BA |
| 23 | Modern Languages with Translation and Transcultural Studies BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Hispanic Studies and Global Sustainable Development BASc |

##### Philosophy

###### BA

| # | Programme |
|---|-----------|
| 1 | History and Philosophy BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Philosophy and Global Sustainable Development BASc |

##### Politics and International Studies

###### BA

| # | Programme |
|---|-----------|
| 1 | History and Politics BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Politics, International Studies and Global Sustainable Development BASc |

##### Psychology

###### BASc

| # | Programme |
|---|-----------|
| 1 | Psychology and Global Sustainable Development BASc |

##### Sociology

###### BA

| # | Programme |
|---|-----------|
| 1 | History and Sociology BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Sociology and Global Sustainable Development BASc |

##### Theatre and Performance Studies

###### BA

| # | Programme |
|---|-----------|
| 1 | English and Theatre Studies BA |
| 2 | French and Theatre Studies BA |
| 3 | German and Theatre Studies BA |
| 4 | Hispanic Studies and Theatre Studies BA |
| 5 | Italian and Theatre Studies BA |
| 6 | Theatre and Performance Studies BA |

###### BASc

| # | Programme |
|---|-----------|
| 1 | Theatre and Performance Studies and Global Sustainable Development BASc |

#### Science, Engineering and Medicine

##### Biology

###### BSc

| # | Programme |
|---|-----------|
| 1 | Biochemistry BSc |
| 2 | Biochemistry with Placement Year BSc |
| 3 | Biological Sciences BSc |
| 4 | Biomedical Science with Placement Year BSc |

###### MBio

| # | Programme |
|---|-----------|
| 1 | Biochemistry MBio |
| 2 | Biochemistry with Industrial Placement MBio |
| 3 | Biological Sciences MBio |
| 4 | Biological Sciences with Industrial Placement MBio |
| 5 | Biological Sciences with Placement Year BSc |
| 6 | Biomedical Science MBio |
| 7 | Biomedical Science with Industrial Placement MBio |

##### Chemistry

###### BSc

| # | Programme |
|---|-----------|
| 1 | Chemistry BSc |
| 2 | Chemistry with Medicinal Chemistry BSc |

###### MChem

| # | Programme |
|---|-----------|
| 1 | Chemistry MChem |
| 2 | Chemistry with Industrial Placement MChem |
| 3 | Chemistry with International Placement MChem |
| 4 | Chemistry with Medicinal Chemistry MChem |

##### Computer Science

###### BSc

| # | Programme |
|---|-----------|
| 1 | Computer Science BSc |
| 2 | Computer Science with Business Studies BSc |

###### MEng

| # | Programme |
|---|-----------|
| 1 | Computer Science MEng |

##### Cyber Security

###### BSc

| # | Programme |
|---|-----------|
| 1 | Cyber Security BSc |

##### Engineering

###### BEng

| # | Programme |
|---|-----------|
| 1 | Automotive Engineering BEng |
| 2 | Biomedical Systems Engineering BEng |
| 3 | Civil Engineering BEng |
| 4 | Computer Systems Engineering BEng |
| 5 | Electrical and Electronic Engineering BEng |
| 6 | Engineering BEng |
| 7 | Engineering Business Management BEng |
| 8 | Manufacturing and Mechanical Engineering BEng |
| 9 | Mechanical Engineering BEng |
| 10 | Robotics Engineering with Artificial Intelligence BEng |
| 11 | Systems Engineering BEng |

###### MEng

| # | Programme |
|---|-----------|
| 1 | Automotive Engineering MEng |
| 2 | Biomedical Systems Engineering MEng |
| 3 | Civil Engineering MEng |
| 4 | Computer Systems Engineering MEng |
| 5 | Electrical and Electronic Engineering MEng |
| 6 | Engineering MEng |
| 7 | Manufacturing and Mechanical Engineering MEng |
| 8 | Mechanical Engineering MEng |
| 9 | Systems Engineering MEng |

##### Health Sciences

###### BSc

| # | Programme |
|---|-----------|
| 1 | Neuroscience BSc |
| 2 | Neuroscience with Placement Year BSc |

###### MBio

| # | Programme |
|---|-----------|
| 1 | Neuroscience MBio |
| 2 | Neuroscience with Industrial Placement MBio |

##### Mathematics

###### BSc

| # | Programme |
|---|-----------|
| 1 | Discrete Mathematics BSc |
| 2 | Mathematics BSc |

###### MEng

| # | Programme |
|---|-----------|
| 1 | Discrete Mathematics MEng |

###### MMath

| # | Programme |
|---|-----------|
| 1 | Mathematics MMath |

##### Medical Sciences

###### BSc

| # | Programme |
|---|-----------|
| 1 | Health and Medical Sciences BSc |

##### Physics

###### BSc

| # | Programme |
|---|-----------|
| 1 | Integrated Natural Sciences BSc |
| 2 | Mathematics and Physics BSc |
| 3 | Physics BSc |
| 4 | Physics with Astrophysics BSc |

###### MMathPhys

| # | Programme |
|---|-----------|
| 1 | Mathematics and Physics MMathPhys |

###### MPhys

| # | Programme |
|---|-----------|
| 1 | Physics MPhys |
| 2 | Physics with Astrophysics MPhys |

###### MSci

| # | Programme |
|---|-----------|
| 1 | Integrated Natural Sciences MSci |

##### Psychology

###### BSc

| # | Programme |
|---|-----------|
| 1 | Psychology BSc |
| 2 | Psychology with Education BSc |
| 3 | Psychology with Linguistics BSc |

##### Statistics

###### BSc

| # | Programme |
|---|-----------|
| 1 | Data Science BSc |
| 2 | MORSE BSc |
| 3 | Mathematics and Statistics BSc |

###### MMORSE

| # | Programme |
|---|-----------|
| 1 | MORSE MMORSE |

###### MMathStat

| # | Programme |
|---|-----------|
| 1 | Mathematics and Statistics MMathStat |

###### MSci

| # | Programme |
|---|-----------|
| 1 | Data Science MSci |

#### Social Sciences

##### Accounting and finance

###### BSc

| # | Programme |
|---|-----------|
| 1 | Accounting and Finance (with Foundation Year) BSc |
| 2 | Accounting and Finance BSc |
| 3 | Accounting and Finance with Placement Year BSc |

##### Business and Management

###### BSc

| # | Programme |
|---|-----------|
| 1 | Business and Management (with Foundation Year) BSc |
| 2 | Business and Management BSc |
| 3 | Business and Management with Marketing BSc |
| 4 | Business and Management with Marketing with Placement Year BSc |
| 5 | Business and Management with Placement Year BSc |
| 6 | International Business and Management (with Foundation Year) BSc |
| 7 | International Business and Management BSc |
| 8 | International Business and Management with Marketing BSc |

##### Counselling

###### BA

| # | Programme |
|---|-----------|
| 1 | Child and Family: Mental Health BA |

##### Economics

###### BSc

| # | Programme |
|---|-----------|
| 1 | Economics BSc |
| 2 | Economics and Management BSc |

##### Education

###### BA

| # | Programme |
|---|-----------|
| 1 | Education BA |

##### Law

###### LLB

| # | Programme |
|---|-----------|
| 1 | Law (4 Year) LLB |
| 2 | Law LLB |
| 3 | Law with Humanities BA |
| 4 | Law with Study Abroad in English LLB |

##### Lifelong Learning

###### BA

| # | Programme |
|---|-----------|
| 1 | Counselling and the Psychotherapeutic Relationship BA |
| 2 | Early Childhood BA |

##### Linguistics

###### BA

| # | Programme |
|---|-----------|
| 1 | English Language and Linguistics BA |
| 2 | Professional and Intercultural Communication BA |

##### Modern Languages and Cultures

###### BA

| # | Programme |
|---|-----------|
| 1 | Linguistics with Modern Language BA |

###### LLB

| # | Programme |
|---|-----------|
| 1 | Law with French LLB |
| 2 | Law with German LLB |

##### Philosophy

###### BA

| # | Programme |
|---|-----------|
| 1 | Philosophy BA |
| 2 | Philosophy and Literature BA |
| 3 | Philosophy, English Literature and Classics BA |

###### BSc

| # | Programme |
|---|-----------|
| 1 | Mathematics and Philosophy BA/BSc |

##### Politics and International Studies

###### BA

| # | Programme |
|---|-----------|
| 1 | Global Politics with Integrated Year Abroad in Brussels BA |
| 2 | Philosophy and Politics BA |
| 3 | Politics BA |
| 4 | Politics and International Studies BA |
| 5 | Politics and International Studies with Chinese BA |
| 6 | Politics, International Studies and French BA |
| 7 | Politics, International Studies and German BA |
| 8 | Politics, International Studies and Hispanic Studies BA |
| 9 | Politics, International Studies and Italian BA |
| 10 | Politics, Philosophy and Law (PPL) BA |

###### BSc

| # | Programme |
|---|-----------|
| 1 | Economics, Politics and International Studies BSc/BA |
| 2 | Philosophy, Politics and Economics (PPE) BA/BSc |

##### Psychology

###### BA

| # | Programme |
|---|-----------|
| 1 | Philosophy with Psychology BA |

###### BSc

| # | Programme |
|---|-----------|
| 1 | Economics, Psychology and Philosophy (EPP) BA/BSc |

##### Social Work

###### Unknown

| # | Programme |
|---|-----------|
| 1 | Social Work Degree Apprenticeship BA |

##### Sociology

###### BA

| # | Programme |
|---|-----------|
| 1 | Law and Sociology BA |
| 2 | Politics and Sociology BA |
| 3 | Social Sciences with Data Science BA |
| 4 | Sociology BA |
| 5 | Sociology and Criminology BA |

###### LLB

| # | Programme |
|---|-----------|
| 1 | Human, Social and Political Sciences BA |

#### Unknown

##### Health Sciences

###### BSc

| # | Programme |
|---|-----------|
| 1 | Biomedical Sciences BSc |
| 2 | Biomedical Sciences with Placement Year BSc |

###### MBio

| # | Programme |
|---|-----------|
| 1 | Biomedical Sciences with Industrial Placement MBio |

##### Society and Culture

###### BASc

| # | Programme |
|---|-----------|
| 1 | Digital Futures, Artificial Intelligence and Society BASc |

### 1.3 Interdisciplinary / cross-faculty undergraduate programmes

Warwick's School for Cross-faculty Studies offers interdisciplinary programmes including Liberal Arts, Global Sustainable Development, and Design Studies. These sit under the Faculty of Arts but draw on multiple faculties.

### 1.4 General requirements

- GCSE English Language and Mathematics: minimum Grade C / Grade 4
- Three full A-levels required (no advantage for fourth A-level)
- EPQ not considered in offers
- Welsh Baccalaureate: one grade lower offer + Grade C in Advanced Skills Baccalaureate Wales

---

## SECTION 2 — Graduate education

### 2.1 Graduate programmes — grouped by degree level

#### Taught Programmes

##### MSc

| # | Programme | URL |
|---|-----------|-----|
| 1 | Accounting & Financial Management | https://warwick.ac.uk/study/postgraduate/courses/msc-accounting-financial-management |
| 2 | Accounting & Sustainability | https://warwick.ac.uk/study/postgraduate/courses/msc-accounting-sustainability |
| 3 | Advanced Mechanical Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-advanced-mechanical-engineering |
| 4 | Analytical Sciences and Instrumentation | https://warwick.ac.uk/study/postgraduate/courses/msc-analytical-sciences-instrumentation |
| 5 | Analytical and Polymer Science | https://warwick.ac.uk/study/postgraduate/courses/msc-analytical-polymer-science |
| 6 | Applied Artificial Intelligence | https://warwick.ac.uk/study/postgraduate/courses/msc-applied-artificial-intelligence |
| 7 | Behavioural and Data Science | https://warwick.ac.uk/study/postgraduate/courses/msc-behavioural-data-science |
| 8 | Behavioural and Economic Science (Economics Track) | https://warwick.ac.uk/study/postgraduate/courses/msc-behavioural-economics |
| 9 | Behavioural and Economic Science (Science Track) | https://warwick.ac.uk/study/postgraduate/courses/msc-behavioural-economics-science |
| 10 | Biomedical Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-biomedical-engineering |
| 11 | Biotechnology, Bioprocessing and Business Management | https://warwick.ac.uk/study/postgraduate/courses/msc-biotechnology-bioprocessing-business-management |
| 12 | Business & Finance | https://warwick.ac.uk/study/postgraduate/courses/msc-business-finance |
| 13 | Business Analytics & Artificial Intelligence | https://warwick.ac.uk/study/postgraduate/courses/msc-business-analytics |
| 14 | Business with Consulting | https://warwick.ac.uk/study/postgraduate/courses/msc-business-consulting |
| 15 | Business with Marketing | https://warwick.ac.uk/study/postgraduate/courses/msc-business-marketing |
| 16 | Business with Operations Management | https://warwick.ac.uk/study/postgraduate/courses/msc-business-operations-management |
| 17 | Clinical Applications of Psychology | https://warwick.ac.uk/study/postgraduate/courses/msc-clinical-applications-psychology |
| 18 | Communications and Information Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-communications-information-engineering |
| 19 | Computer Science | https://warwick.ac.uk/study/postgraduate/courses/msc-computer-science |
| 20 | Cyber Security Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-cyber-security-engineering |
| 21 | Cyber Security Management | https://warwick.ac.uk/study/postgraduate/courses/msc-cyber-security-management |
| 22 | Economics | https://warwick.ac.uk/study/postgraduate/courses/msc-economics |
| 23 | Economics and Data Science | https://warwick.ac.uk/study/postgraduate/courses/msc-economics-data-science |
| 24 | Economics and Environmental Policy | https://warwick.ac.uk/study/postgraduate/courses/msc-economics-environmental-policy |
| 25 | Economics and International Financial Economics | https://warwick.ac.uk/study/postgraduate/courses/msc-international-economics |
| 26 | Electrical Power Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-electrical-power-engineering |
| 27 | Electrical and Electronic Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-electrical-electronic-engineering |
| 28 | Engineering Business Management | https://warwick.ac.uk/study/postgraduate/courses/msc-engineering-business-management |
| 29 | Engineering Design Management | https://warwick.ac.uk/study/postgraduate/courses/msc-engineering-design-management |
| 30 | Environmental Bioscience in a Changing Climate | https://warwick.ac.uk/study/postgraduate/courses/msc-environmental-bioscience |
| 31 | Finance | https://warwick.ac.uk/study/postgraduate/courses/msc-finance |
| 32 | Finance & Economics | https://warwick.ac.uk/study/postgraduate/courses/msc-finance-economics |
| 33 | Financial Technology | https://warwick.ac.uk/study/postgraduate/courses/msc-financial-technology |
| 34 | Food Security | https://warwick.ac.uk/study/postgraduate/courses/msc-food-security |
| 35 | Games Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-games-engineering |
| 36 | Humanitarian Engineering (with Sustainability) | https://warwick.ac.uk/study/postgraduate/courses/msc-humanitarian-engineering-sustainability |
| 37 | Innovation and Entrepreneurship | https://warwick.ac.uk/study/postgraduate/courses/msc-innovation-entrepreneurship |
| 38 | Intercultural Communication for Business & Professions | https://warwick.ac.uk/study/postgraduate/courses/msc-intercultural-communication-business/ |
| 39 | Interdisciplinary Biomedical Research | https://warwick.ac.uk/study/postgraduate/courses/msc-interdisciplinary-biomedical-research |
| 40 | International Business | https://warwick.ac.uk/study/postgraduate/courses/msc-international-business |
| 41 | International Trade, Strategy and Operations | https://warwick.ac.uk/study/postgraduate/courses/msc-international-trade |
| 42 | Management | https://warwick.ac.uk/study/postgraduate/courses/msc-management |
| 43 | Management for Business Excellence | https://warwick.ac.uk/study/postgraduate/courses/msc-management-business-excellence |
| 44 | Management of Information Systems & Digital Innovation | https://warwick.ac.uk/study/postgraduate/courses/msc-management-digital-innovation |
| 45 | Marketing & Strategy | https://warwick.ac.uk/study/postgraduate/courses/msc-marketing-strategy |
| 46 | Mathematical Finance | https://warwick.ac.uk/study/postgraduate/courses/msc-mathematical-finance |
| 47 | Mathematics | https://warwick.ac.uk/study/postgraduate/courses/msc-mathematics |
| 48 | Medical Biotechnology and Business Management | https://warwick.ac.uk/study/postgraduate/courses/msc-medical-biotechnology-business-management |
| 49 | Medical Education for Health Professionals - iheed | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-medical-education-ideed/ |
| 50 | Mental Health and Wellbeing | https://warwick.ac.uk/study/postgraduate/courses/msc-mental-health-wellbeing |
| 51 | Neuroscience and Psychology of Mental Health - iheed | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-neuroscience-psychology-mental-health-iheed |
| 52 | Polymer Chemistry | https://warwick.ac.uk/study/postgraduate/courses/msc-polymer-chemistry |
| 53 | Polymer Science | https://warwick.ac.uk/study/postgraduate/courses/msc-polymer-science |
| 54 | Programme and Project Management | https://warwick.ac.uk/study/postgraduate/courses/msc-project-management |
| 55 | Psychological Research | https://warwick.ac.uk/study/postgraduate/courses/msc-psychological-research |
| 56 | Renewable Energy | https://warwick.ac.uk/study/postgraduate/courses/msc-renewable-energy |
| 57 | Reproductive Science (Women’s Health or Embryology) | https://warwick.ac.uk/study/postgraduate/courses/msc-reproductive-science |
| 58 | Smart, Connected and Autonomous Vehicles | https://warwick.ac.uk/study/postgraduate/courses/msc-smart-connected-autonomous-vehicles |
| 59 | Social Inequalities and Research Methods | https://warwick.ac.uk/study/postgraduate/courses/msc-social-inequalities-and-research-methods |
| 60 | Statistics | https://warwick.ac.uk/study/postgraduate/courses/msc-statistics |
| 61 | Statistics with Data Science | https://warwick.ac.uk/study/postgraduate/courses/msc-statistics-data-science |
| 62 | Statistics with Finance | https://warwick.ac.uk/study/postgraduate/courses/msc-statistics-finance |
| 63 | Statistics with Probability | https://warwick.ac.uk/study/postgraduate/courses/msc-statistics-probability |
| 64 | Supply Chain and Logistics Management | https://warwick.ac.uk/study/postgraduate/courses/msc-supply-chain-logistics-management |
| 65 | Sustainable Automotive Electrification | https://warwick.ac.uk/study/postgraduate/courses/msc-sustainable-automotive-electrification |
| 66 | e-Business Management | https://warwick.ac.uk/study/postgraduate/courses/msc-e-business-management |

##### MA

| # | Programme | URL |
|---|-----------|-----|
| 1 | Ancient Literature and Thought | https://warwick.ac.uk/study/postgraduate/courses/ma-ancient-literature-thought |
| 2 | Ancient Visual and Material Culture | https://warwick.ac.uk/study/postgraduate/courses/ma-ancient-visual-material-culture |
| 3 | Arts, Enterprise and Development | https://warwick.ac.uk/study/postgraduate/courses/ma-arts-enterprise-development |
| 4 | Career Development and Coaching Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-career-development |
| 5 | Career Education, Information and Guidance in HE | https://warwick.ac.uk/study/postgraduate/courses/ma-career-education |
| 6 | Childhood in Society | https://warwick.ac.uk/study/postgraduate/courses/ma-childhood-in-society |
| 7 | Coaching | https://warwick.ac.uk/study/postgraduate/courses/ma-coaching |
| 8 | Continental Philosophy | https://warwick.ac.uk/study/postgraduate/courses/ma-continental-philosophy |
| 9 | Creative and Media Enterprises | https://warwick.ac.uk/study/postgraduate/courses/ma-creative-media-enterprises |
| 10 | Critical and Cultural Theory | https://warwick.ac.uk/study/postgraduate/courses/ma-critical-cultural-theory |
| 11 | Culture of the European Renaissance | https://warwick.ac.uk/study/postgraduate/courses/ma-european-renaissance |
| 12 | Digital Media and Culture | https://warwick.ac.uk/study/postgraduate/courses/ma-digital-media-culture |
| 13 | Drama Education and English Language Teaching | https://warwick.ac.uk/study/postgraduate/courses/ma-drama-education-english-language-teaching |
| 14 | Drama and Theatre Education | https://warwick.ac.uk/study/postgraduate/courses/ma-drama-theatre-education |
| 15 | Education | https://warwick.ac.uk/study/postgraduate/courses/ma-education |
| 16 | Educational Innovation | https://warwick.ac.uk/study/postgraduate/courses/ma-educational-innovation |
| 17 | Educational Leadership and Management | https://warwick.ac.uk/study/postgraduate/courses/ma-educational-leadership |
| 18 | English Literature | https://warwick.ac.uk/study/postgraduate/courses/ma-english-literature |
| 19 | English and Drama | https://warwick.ac.uk/study/postgraduate/courses/ma-english-drama |
| 20 | Environmental Humanities | https://warwick.ac.uk/study/postgraduate/courses/ma-environmental-humanities |
| 21 | Film and Television Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-film-tv |
| 22 | Gender and International Development | https://warwick.ac.uk/study/postgraduate/courses/ma-gender-development |
| 23 | Gender and Sexuality | https://warwick.ac.uk/study/postgraduate/courses/ma-gender-sexuality |
| 24 | Global Education and International Development | https://warwick.ac.uk/study/postgraduate/courses/ma-global-education |
| 25 | Global Media and Communication | https://warwick.ac.uk/study/postgraduate/courses/ma-global-media-communication |
| 26 | International Development | https://warwick.ac.uk/study/postgraduate/courses/ma-international-development |
| 27 | International Political Economy | https://warwick.ac.uk/study/postgraduate/courses/ma-international-political-economy |
| 28 | International Relations | https://warwick.ac.uk/study/postgraduate/courses/ma-international-relations |
| 29 | International Security | https://warwick.ac.uk/study/postgraduate/courses/ma-international-security |
| 30 | Islamic Education: Theory and Practice | https://warwick.ac.uk/study/postgraduate/courses/ma-islamic-education |
| 31 | Philosophy | https://warwick.ac.uk/study/postgraduate/courses/ma-philosophy |
| 32 | Philosophy and the Arts | https://warwick.ac.uk/study/postgraduate/courses/ma-philosophy-arts |
| 33 | Political and Legal Theory | https://warwick.ac.uk/study/postgraduate/courses/ma-political-legal-theory |
| 34 | Politics of Climate Change | https://warwick.ac.uk/study/postgraduate/courses/ma-politics-climate-change/ |
| 35 | Professional Education | https://warwick.ac.uk/study/postgraduate/courses/ma-professional-education |
| 36 | Psychology and Education | https://warwick.ac.uk/study/postgraduate/courses/ma-psychology-education |
| 37 | Public Policy | https://warwick.ac.uk/study/postgraduate/courses/ma-public-policy |
| 38 | Social and Political Thought | https://warwick.ac.uk/study/postgraduate/courses/ma-social-political-thought |
| 39 | Sociology | https://warwick.ac.uk/study/postgraduate/courses/ma-sociology |
| 40 | Teaching English to Speakers of Other Languages (TESOL) | https://warwick.ac.uk/study/postgraduate/courses/ma-tesol |
| 41 | Translation and Cultures | https://warwick.ac.uk/study/postgraduate/courses/ma-translation-cultures |
| 42 | World Literature | https://warwick.ac.uk/study/postgraduate/courses/ma-world-literature |
| 43 | Writing | https://warwick.ac.uk/study/postgraduate/courses/ma-writing |

##### LLM

| # | Programme | URL |
|---|-----------|-----|
| 1 | Advanced Legal Studies | https://warwick.ac.uk/study/postgraduate/courses/llm-advanced-legal-studies |
| 2 | International Commercial Law | https://warwick.ac.uk/study/postgraduate/courses/llm-international-commercial-law |
| 3 | International Corporate Governance and Financial Regulation | https://warwick.ac.uk/study/postgraduate/courses/llm-international-corporate-governance-financial-regulation |
| 4 | International Development Law and Human Rights | https://warwick.ac.uk/study/postgraduate/courses/llm-international-development-law-human-rights |
| 5 | International Economic Law | https://warwick.ac.uk/study/postgraduate/courses/llm-international-economic-law |

##### MASc

| # | Programme | URL |
|---|-----------|-----|
| 1 | Design for Sustainability | https://warwick.ac.uk/study/postgraduate/courses/masc-design-sustainability |
| 2 | Global Sustainable Development | https://warwick.ac.uk/study/postgraduate/courses/masc-global-sustainable-development |

##### MASc/PGDip

| # | Programme | URL |
|---|-----------|-----|
| 1 | AI and Society | https://warwick.ac.uk/study/postgraduate/courses/masc-pgdip-ai-and-society |
| 2 | Data Visualisation | https://warwick.ac.uk/study/postgraduate/courses/pgdip-masc-data-visualisation |

##### MPH

| # | Programme | URL |
|---|-----------|-----|
| 1 | Public Health | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-mph-public-health |
| 2 | iheed Master of Public Health | https://warwick.ac.uk/study/postgraduate/courses/mph-public-health-iheed |

##### DBA

| # | Programme | URL |
|---|-----------|-----|
| 1 | Doctor of Business Administration | https://warwick.ac.uk/study/postgraduate/courses/dba-business-administration |

##### PGA

| # | Programme | URL |
|---|-----------|-----|
| 1 | Career Development Theories | https://warwick.ac.uk/study/postgraduate/courses/pga-career-development-theories |
| 2 | Career Development Theories - CEIGHE | https://warwick.ac.uk/study/postgraduate/courses/pga-career-development-theories-ceighe |
| 3 | Career Vocation and Calling | https://warwick.ac.uk/study/postgraduate/courses/pga-career-vocation-calling |
| 4 | Challenges of Careers Work in Higher Education | https://warwick.ac.uk/study/postgraduate/courses/pga-challenges-in-he |
| 5 | Employability and Career Education: Strategy and Inclusive Design | https://warwick.ac.uk/study/postgraduate/courses/pga-employability-career-education |
| 6 | Foundation Research Methods in Education | https://warwick.ac.uk/study/postgraduate/courses/pga-research-methods-education |
| 7 | Islamic Education | https://warwick.ac.uk/study/postgraduate/courses/pga-islamic-education |
| 8 | Leadership and Team Coaching | https://warwick.ac.uk/study/postgraduate/courses/pga-leadership-coaching |
| 9 | Leading Educational Change and Improvement | https://warwick.ac.uk/study/postgraduate/courses/pga-educational-change |

##### PGCert

| # | Programme | URL |
|---|-----------|-----|
| 1 | Career Development and Coaching Studies | https://warwick.ac.uk/study/postgraduate/courses/pgcert-career-development |
| 2 | Career Education, Information and Guidance in HE | https://warwick.ac.uk/study/postgraduate/courses/pgcert-career-education |
| 3 | Coaching | https://warwick.ac.uk/study/postgraduate/courses/pgcert-coaching |
| 4 | Professional Education | https://warwick.ac.uk/study/postgraduate/courses/pgcert-in-professional-education |

##### PGDip

| # | Programme | URL |
|---|-----------|-----|
| 1 | Career Development and Coaching Studies | https://warwick.ac.uk/study/postgraduate/courses/pgdip-career-development |
| 2 | Career Education, Information and Guidance in HE | https://warwick.ac.uk/study/postgraduate/courses/pgdip-career-education |
| 3 | Coaching | https://warwick.ac.uk/study/postgraduate/courses/pgdip-coaching |

##### Diploma plus MSc

| # | Programme | URL |
|---|-----------|-----|
| 1 | Economics | https://warwick.ac.uk/study/postgraduate/courses/diploma-msc-economics |
| 2 | Mathematics | https://warwick.ac.uk/study/postgraduate/courses/diploma-msc-mathematics |

##### MSc/PGDip

| # | Programme | URL |
|---|-----------|-----|
| 1 | Big Data and Digital Futures | https://warwick.ac.uk/study/postgraduate/courses/pgdip-msc-big-data-digital-futures |

##### MSc/PGDip/PGCert

| # | Programme | URL |
|---|-----------|-----|
| 1 | Diagnostics, Data and Digital Health | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-diagnostics-data-digital-health |
| 2 | Diagnostics, Data and Digital Health (Medical Imaging) | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-diagnostics-data-digital-health-medical-imgaging |

##### MSc/PGDip/PGCert/PGA

| # | Programme | URL |
|---|-----------|-----|
| 1 | Humanitarian Engineering | https://warwick.ac.uk/study/postgraduate/courses/pga-pgcert-pgdip-msc-humanitarian-engineering |
| 2 | Predictive Modelling and Scientific Computing | https://warwick.ac.uk/study/postgraduate/courses/pga-pgcert-pgdip-msc-predictive-modelling-scientific-computing |

##### PGCert / PGDip / MSc

| # | Programme | URL |
|---|-----------|-----|
| 1 | iheed MSc in Clinical Research | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-clinical-research-iheed/ |
| 2 | iheed MSc in Healthcare Leadership | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-msc-healthcare-leadership-iheed |

##### MSc / PGDip / PGCert / PGA

| # | Programme | URL |
|---|-----------|-----|
| 1 | Global Central Banking and Financial Regulation | https://warwick.ac.uk/study/postgraduate/courses/pga-pgcert-pgdip-msc-global-central-banking-financial-regulation |

##### MA/PGDip/PGCert/PGAward

| # | Programme | URL |
|---|-----------|-----|
| 1 | History | https://warwick.ac.uk/study/postgraduate/courses/ma-history |

##### MMedEd/PGDip/PGCert

| # | Programme | URL |
|---|-----------|-----|
| 1 | Medical Education | https://warwick.ac.uk/study/postgraduate/courses/pgcert-pgdip-mmeded-medical-education |

##### PGCEi

| # | Programme | URL |
|---|-----------|-----|
| 1 | Postgraduate Certificate in Education International | https://warwick.ac.uk/study/postgraduate/courses/pgcei-international |

#### Research Programmes

##### MPhil/PhD

| # | Programme | URL |
|---|-----------|-----|
| 1 | Adult Education and Lifelong Learning | https://warwick.ac.uk/study/postgraduate/courses/phd-lifelong-learning |
| 2 | Applied Linguistics | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-applied-linguistics |
| 3 | Applied Screen Studies: Practice as Research | https://warwick.ac.uk/study/postgraduate/courses/phd-applied-screen-studies |
| 4 | Caribbean Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-caribbean-studies |
| 5 | Classics and Ancient History | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-classics-ancient-history |
| 6 | Cultural Policy Studies/Creative Industries/Media and Communication | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-cultural-policy |
| 7 | Discourse Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-discourse-studies |
| 8 | Education | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-education |
| 9 | Education and Psychology | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-education-psychology |
| 10 | Engineering (School of Engineering) | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-engineering |
| 11 | Engineering (WMG) | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-engineering-wmg |
| 12 | English Language Teaching | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-english-language-teaching |
| 13 | English Language Teaching and Applied Linguistics | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-english-language-teaching-applied-linguistics |
| 14 | English and Comparative Literary Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-english-comparative-literary-studies |
| 15 | Film and/or Television Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-film-tv |
| 16 | French Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-french-studies |
| 17 | German Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-german-studies |
| 18 | Global Sustainable Development | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-global-sustainable-development |
| 19 | Hispanic Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-hispanic-studies |
| 20 | History | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-history |
| 21 | History of Art | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-history-of-art |
| 22 | Intercultural Communication | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-intercultural-communication |
| 23 | Interdisciplinary Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-interdisciplinary-studies |
| 24 | Italian | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-italian |
| 25 | Law | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-law |
| 26 | Linguistics | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-linguistics |
| 27 | Mathematics | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-mathematics |
| 28 | Open Professional Studies | https://warwick.ac.uk/study/postgraduate/courses/phd-open-professional-studies |
| 29 | Psychology | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-psychology |
| 30 | Renaissance Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-renaissance-studies |
| 31 | Social Policy and Social Work | https://warwick.ac.uk/study/postgraduate/courses/phd-social-policy-social-work |
| 32 | Statistics | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-statistics |
| 33 | Theatre and Performance Studies | https://warwick.ac.uk/study/postgraduate/courses/mphil-phd-theatre-performance-studies |

##### PhD

| # | Programme | URL |
|---|-----------|-----|
| 1 | Biomedical AI | https://warwick.ac.uk/study/postgraduate/courses/phd-biomedical-ai |
| 2 | Chemistry | https://warwick.ac.uk/study/postgraduate/courses/phd-chemistry |
| 3 | Computer Science | https://warwick.ac.uk/study/postgraduate/courses/phd-computer-science |
| 4 | Data Visualisation | https://warwick.ac.uk/study/postgraduate/courses/phd-data-visualisation |
| 5 | Employment Research | https://warwick.ac.uk/study/postgraduate/courses/phd-employment-research |
| 6 | Life Sciences | https://warwick.ac.uk/study/postgraduate/courses/phd-life-sciences |
| 7 | Literary Practice | https://warwick.ac.uk/study/postgraduate/courses/phd-literary-practice |
| 8 | Modelling of Heterogeneous Systems | https://warwick.ac.uk/study/postgraduate/courses/phd-modelling-heterogeneous-systems |
| 9 | Philosophy | https://warwick.ac.uk/study/postgraduate/courses/phd-philosophy |
| 10 | Philosophy and Literature | https://warwick.ac.uk/study/postgraduate/courses/phd-philosophy-literature |
| 11 | Physics | https://warwick.ac.uk/study/postgraduate/courses/phd-physics |
| 12 | Politics and International Studies | https://warwick.ac.uk/study/postgraduate/courses/phd-politics-international-studies |
| 13 | Sociology | https://warwick.ac.uk/study/postgraduate/courses/phd-sociology |
| 14 | Translation and Transcultural Studies | https://warwick.ac.uk/study/postgraduate/courses/phd-translation-transcultural-studies |
| 15 | Women’s and Gender Studies | https://warwick.ac.uk/study/postgraduate/courses/phd-women-gender-studies |

##### MA by Research

| # | Programme | URL |
|---|-----------|-----|
| 1 | Caribbean Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-caribbean-studies |
| 2 | Classics and Ancient History | https://warwick.ac.uk/study/postgraduate/courses/ma-classics-ancient-history-by-research |
| 3 | English and Comparative Literary Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-english-comparative-literary-studies-by-research |
| 4 | French Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-french-studies-by-research |
| 5 | German Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-german-studies-by-research |
| 6 | Hispanic Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-hispanic-studies-by-research |
| 7 | History | https://warwick.ac.uk/study/postgraduate/courses/ma-history-by-research |
| 8 | History of Art | https://warwick.ac.uk/study/postgraduate/courses/ma-history-of-art-by-research |
| 9 | Italian | https://warwick.ac.uk/study/postgraduate/courses/ma-italian-by-research |
| 10 | Renaissance Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-renaissance-studies-by-research |
| 11 | Theatre and Performance Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-theatre-performance-studies-by-research |

##### MSc by Research

| # | Programme | URL |
|---|-----------|-----|
| 1 | Chemistry | https://warwick.ac.uk/study/postgraduate/courses/msc-chemistry-by-research |
| 2 | Computer Science | https://warwick.ac.uk/study/postgraduate/courses/msc-computer-science-by-research |
| 3 | Engineering | https://warwick.ac.uk/study/postgraduate/courses/msc-engineering-by-research |
| 4 | Life Sciences | https://warwick.ac.uk/study/postgraduate/courses/msc-life-sciences-by-research |
| 5 | Physics | https://warwick.ac.uk/study/postgraduate/courses/msc-physics-by-research |
| 6 | Psychology | https://warwick.ac.uk/study/postgraduate/courses/msc-psychology-by-research |

##### MRes/PhD

| # | Programme | URL |
|---|-----------|-----|
| 1 | Business and Management | https://warwick.ac.uk/study/postgraduate/courses/mres-phd-business-management |
| 2 | Economics | https://warwick.ac.uk/study/postgraduate/courses/mres-phd-economics |
| 3 | Finance and Economics | https://warwick.ac.uk/study/postgraduate/courses/mres-phd-finance-economics |

##### EngD

| # | Programme | URL |
|---|-----------|-----|
| 1 | Engineering Doctorate | https://warwick.ac.uk/study/postgraduate/courses/engd-engineering |

##### MA for Research

| # | Programme | URL |
|---|-----------|-----|
| 1 | Film and Television Studies | https://warwick.ac.uk/study/postgraduate/courses/ma-film-tv-by-research |

##### LLM by Research

| # | Programme | URL |
|---|-----------|-----|
| 1 | Law | https://warwick.ac.uk/study/postgraduate/courses/llm-law-by-research |

##### MPhil

| # | Programme | URL |
|---|-----------|-----|
| 1 | Philosophy | https://warwick.ac.uk/study/postgraduate/courses/mphil-philosophy |

##### MRes

| # | Programme | URL |
|---|-----------|-----|
| 1 | Translational Biomedical Research | https://warwick.ac.uk/study/postgraduate/courses/mres-translational-biomedical-research |

##### MRes/PGCert

| # | Programme | URL |
|---|-----------|-----|
| 1 | Health and Care | https://warwick.ac.uk/study/postgraduate/courses/pgcert-mres-healthresearch-care |

#### Graduate Entry Medicine

| # | Programme | URL |
|---|-----------|-----|
| 1 | Medicine (Graduate Entry) MBChB | https://warwick.ac.uk/study/postgraduate/courses/mbchb |

### 2.2 Graduate admissions model

Warwick operates a **centralised application system** for postgraduate programmes. Applications are made directly to the university via the online portal (not through UCAS for postgraduate). Each department makes its own admissions decisions.

- **Application portal**: https://warwick.ac.uk/study/postgraduate/apply/
- **Research programmes**: Require a research proposal and supervisor identification before application
- **Taught programmes**: Standard application with personal statement, references, and transcripts

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | UCAS |
| UCAS deadline | 14 January 2026 at 18:00 (equal consideration) |
| UCAS applications open | 2 September 2025 |
| Decision notification | By 13 May 2026 |
| A-level results day | 13 August 2026 |
| Clearing opens | 13 August 2026 |
| Deadline to meet conditions | 31 August 2026 |
| GCSE English/Maths minimum | Grade C / Grade 4 |
| A-levels required | Three full A-levels |
| EPQ considered? | No |
| Admissions tests | TMUA (Computer Science, Mathematics required; Economics optional; Statistics optional) |
| Interviews | Select courses only (English/Theatre Studies, Theatre and Performance Studies) |

### 3.2 Undergraduate English proficiency table

Warwick uses a 3-band system (A, B, C) for UG English language requirements:

| Exam | Band A | Band B | Band C |
|------|--------|--------|--------|
| **IELTS Academic** | 6.0 overall (min 5.5 per component) | 6.5 overall (min 6.0 per component) | 7.0 overall (min 6.5 per component) |
| **TOEFL iBT** (pre-Jan 2026) | 87 (L21/W21/R22/S23) | 92 (L21/W21/R22/S23) | 100 (L21/W21/R22/S23) |
| **TOEFL iBT** (post-Jan 2026) | 4.5 overall (min 4.5 per component) | 4.5 overall (min 4.5 per component) | 5.0 overall (min 4.5 per component) |
| **PTE Academic** | 60 (min 59 per skill) | 69 (min 59 per skill) | 75 (min 59 per skill) |
| **Duolingo** | 110 (min 100 per component) | 120 (min 110 per component) | 130 (min 120 per component) |
| **Cambridge C1 Advanced** | 170 overall (min 165 per component) | 180 overall (min 170 per component) | 190 overall (min 180 per component) |
| **Cambridge C2 Proficiency** | 170 overall (min 165 per component) | 180 overall (min 170 per component) | 190 overall (min 180 per component) |
| **GCSE English Language** | Grade 4/C | Grade 4/C | Grade 6/B |
| **IB English A (HL/SL)** | HL 4 or SL 4 | HL 4 or SL 4 | HL 5 or SL 5 |
| **IB English B HL** | HL 4 | HL 4 | HL 5 |

Each course specifies its band on the course page under 'Entry Requirements'. Tests must be taken within 2 years and 1 month of course start date.

### 3.3 Postgraduate English proficiency table

Warwick uses a 4-band system (A, B, C, D) for PG English language requirements:

| Band | IELTS Overall | Component Requirements |
|------|--------------|----------------------|
| A | 6.5 | Min 6.0 per component |
| B | 7.0 | Min two at 6.0/6.5, rest at 7.0+ |
| C | 7.5 | Min two at 6.5/7.0, rest at 7.5+ |
| D | 8.0 | Min two at 7.0/7.5, rest at 8.0+ |

Exemption: Nationals of UKVI-recognised English-speaking countries, or those educated entirely in English within the last 2 years and 4 months.

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year)

| Fee Band | Annual Overseas Tuition | Description |
|---------|------------------------|-------------|
| Band 1 | £27,870 | Classroom-based courses (Humanities, most Social Sciences) |
| Band 2 | £35,530 | Laboratory-based courses, Mathematics, Statistics, Theatre & Performance Studies, Economics, Warwick Business School |

| Expense Item | Annual Estimate | Notes |
|-------------|----------------|-------
| Tuition (Band 1) | £27,870 | Overseas, classroom-based |
| Tuition (Band 2) | £35,530 | Overseas, lab-based/STEM |
| UK Home tuition | £9,250 | Capped by government |
| Accommodation | £4,920–£10,000 | £123–£250/week, 40-week contract typical |
| Living costs (food, travel, personal) | ~£5,000–£8,000 | Estimate; varies by lifestyle |
| **Total estimated COA (Overseas, on-campus)** | **£38,000–£53,000** | Band-dependent |

### 4.2 Postgraduate taught fees (Overseas, 2026-27, selected)

| Fee Band | Annual Overseas Fee | Representative Courses |
|---------|--------------------|-----------------------|
| Premium Business | £37,450–£59,500 | MBA (£59,500), Finance (£44,950), Business Analytics (£38,150) |
| STEM/Engineering | £31,670–£37,460 | Computer Science (£37,460), Engineering (£31,670), Data Science (£37,460) |
| Economics | £32,960 | Economics MSc and variants |
| Social Sciences | £25,340–£31,670 | Law LLM (£25,340), International Relations (£31,670), PAIS (£31,670) |
| Humanities/Arts | £25,340–£29,340 | History (£26,630), English (£27,950), Philosophy (£25,340) |
| Medical | £32,510 (Yr1) / £56,660 (Yrs2+) | MBChB Graduate Entry |

### 4.3 Postgraduate research fees (Overseas, 2026-27)

| Band | Full-time | Part-time | Departments |
|------|-----------|-----------|-------------|
| Band 1 | £25,920 | £15,552 | Business, Economics, Law, Maths, Philosophy, PAIS, Sociology, Statistics, History, English, Languages, Film, Theatre |
| Band 2 | £33,110 | £19,866 | Life Sciences, Chemistry, Engineering, Computer Science, Psychology, Physics, WMG, Medical School |

Part-time fees are 60% of full-time rate. Standard fee covers up to 36 months full-time / 60 months part-time.

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: University of Warwick
  source_url: https://warwick.ac.uk
  source_snippet: University of Warwick
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.programmes.total
  value: 192 (including Foundation/Placement variants)
  source_url: https://sitebuilder.warwick.ac.uk/sitebuilder2/api/dataentry/entries.json?page=/study/undergraduate/courses/course-list
  source_snippet: API returns 196 items, 192 visible (4 hidden)
  capture_date: 2026-07-08
  evidence_type: official_api

E-U-003:
  field: undergraduate.fees.band1.overseas
  value: £27,870 per year (2026-27)
  source_url: https://warwick.ac.uk/study/undergraduate/fees-and-funding/course-costs/
  source_snippet: Band 1 – £27,870 per year: classroom-based courses, including Humanities and most Social Science courses
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.fees.band2.overseas
  value: £35,530 per year (2026-27)
  source_url: https://warwick.ac.uk/study/undergraduate/fees-and-funding/course-costs/
  source_snippet: Band 2 – £35,530 per year: laboratory-based courses, plus Mathematics, Statistics, Theatre and Performance Studies, Economics
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.fees.home
  value: £9,250 per year
  source_url: https://warwick.ac.uk/study/undergraduate/fees-and-funding/course-costs/
  source_snippet: Home (UK) tuition fee
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-006:
  field: english_language.ug.ielts.band_a
  value: 6.0 overall, min 5.5 per component
  source_url: https://warwick.ac.uk/study/undergraduate/applying/english-language-requirements/
  source_snippet: Band A: Overall 6.0, Minimum per component 5.5
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-007:
  field: english_language.ug.ielts.band_c
  value: 7.0 overall, min 6.5 per component
  source_url: https://warwick.ac.uk/study/undergraduate/applying/english-language-requirements/
  source_snippet: Band C: Overall 7.0, Minimum per component 6.5
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: application.deadline.ucas
  value: 14 January 2026 at 18:00
  source_url: https://warwick.ac.uk/study/undergraduate/applying/dates/
  source_snippet: you must apply by the UCAS deadline at 18:00 on 14 January 2026
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: admissions_tests.tmua
  value: Required for CS, Discrete Maths; Optional for Economics, Statistics
  source_url: https://warwick.ac.uk/study/undergraduate/applying/admissions-tests/
  source_snippet: Computer Science — Required. All applicants must take TMUA except those eligible for a Contextual Offer
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.academic_structure.faculties
  value: 3 faculties (Arts, SEM, Social Sciences)
  source_url: https://warwick.ac.uk/faculties/
  source_snippet: Faculty of Arts, Faculty of Science Engineering and Medicine, Faculty of Social Sciences
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-001:
  field: postgraduate.programmes.total
  value: 263
  source_url: https://warwick.ac.uk/study/postgraduate/courses/
  source_snippet: 263 unique course URLs extracted from course listing page
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-002:
  field: postgraduate.fees.mba.overseas
  value: £59,500 (2026-27)
  source_url: https://warwick.ac.uk/services/academicoffice/finance/fees/postgraduatefees/
  source_snippet: Business Administration (MBA) P-N1P2: 2026-27 £59,500
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-003:
  field: postgraduate.fees.cs.msc.overseas
  value: £37,460 (2026-27)
  source_url: https://warwick.ac.uk/services/academicoffice/finance/fees/postgraduatefees/
  source_snippet: Computer Science (MSc) P-G5PD: 2026-27 £37,460
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-004:
  field: postgraduate.research.fees.band1.overseas
  value: £25,920 full-time (2026-27)
  source_url: https://warwick.ac.uk/services/academicoffice/finance/fees/pgr/
  source_snippet: Band 1 Overseas 2026-27: £25,920 full-time, £15,552 part-time
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-005:
  field: postgraduate.research.fees.band2.overseas
  value: £33,110 full-time (2026-27)
  source_url: https://warwick.ac.uk/services/academicoffice/finance/fees/pgr/
  source_snippet: Band 2 Overseas 2026-27: £33,110 full-time, £19,866 part-time
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-G-006:
  field: english_language.pg.band_a
  value: IELTS 6.5, min 6.0 per component
  source_url: https://warwick.ac.uk/study/postgraduate/apply/english/
  source_snippet: Band A: Overall IELTS 6.5, Components minimum 6.0 each
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-G-007:
  field: accommodation.costs.range
  value: £123–£250 per week (2025-26)
  source_url: https://warwick.ac.uk/study/undergraduate/explore/accommodation/
  source_snippet: Our campus residences start from around £123 per week right up to around £250 per week
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
warwick-knowledge-base-v2
├── overview (Section 0: counts, hierarchy, degree inventory, matrix)
├── ug-programmes (Section 1: all 192 UG courses)
├── pg-programmes (Section 2: all 263 PG courses)
├── admissions (Section 3: deadlines, entry requirements, English language)
├── costs (Section 4: UG/PG fees, accommodation)
└── evidence (Section 5: 17 evidence blocks)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: warwick-knowledge-base-v2
  school: <home faculty>
  department: <home department>
  degree_level: <BA|BSc|MEng|MSc|MA|PhD|...>
  level: undergraduate | postgraduate
  field_type: overview | counts | hierarchy | programmes | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|-----------|
| P0 | Per-course A-level/IB typical offers | Individual course pages |
| P0 | PG course-to-faculty attribution | Requires per-course scraping |
| P0 | TMUA score thresholds (published) | Not publicly disclosed per Warwick |
| P1 | Accommodation room-type breakdown | warwick.ac.uk/services/accommodation/ |
| P1 | Living costs detailed breakdown | warwick.ac.uk/study/postgraduate/funding/livingcosts |
| P1 | Scholarship/bursary details | warwick.ac.uk/study/undergraduate/fees-and-funding/scholarships-and-bursaries/ |
| P1 | PG course-specific entry requirements | Individual course pages |
| P2 | Module/curriculum details | Individual course pages |
| P2 | Career outcomes data | HESA/LEO data |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Warwick |
|-----------|--------|
| Total UG programmes (with variants) | 192 |
| Total UG core programmes | 168 |
| Total PG programmes | 263 |
| Russell Group | Yes |
| Faculties | 3 (Arts, SEM, Social Sciences) |
| UG overseas tuition (Band 1) | £27,870/yr |
| UG overseas tuition (Band 2) | £35,530/yr |
| UK Home tuition | £9,250/yr |
| IELTS minimum (UG Band A) | 6.0 (min 5.5) |
| IELTS minimum (UG Band C) | 7.0 (min 6.5) |
| UCAS deadline | 14 January 2026 |
| Admissions tests | TMUA (CS/Maths required) |
| PG MBA fee (Overseas) | £59,500 |
| PG MSc CS fee (Overseas) | £37,460 |
| PGR Band 1 fee (Overseas) | £25,920 |
| PGR Band 2 fee (Overseas) | £33,110 |
| Accommodation range | £123–£250/week |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: warwick.ac.uk, sitebuilder.warwick.ac.uk, wbs.ac.uk
> **Verification**: WebFetch + curl API extraction
> **Granularity**: faculty → department/subject → degree-level → programme
> **Completeness**: UG programmes 192/192 | PG programmes 263/263 | Evidence (17 blocks) | Fees (UG+PG) | Language requirements (UG+PG)
> **Note**: Per-course A-level/IB typical offers require individual course page scraping (P0 follow-up)