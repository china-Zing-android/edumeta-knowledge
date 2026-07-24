# University of Texas at San Antonio (UTSA) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — Institution Overview

### 0.1 Program Counts (Rule 1)

| Dimension | Count |
|-----------|-------|
| UG Degree Programs (BA/BS/BBA/BFA) | 95 |
| UG Minors | 88 |
| UG Certificates | 16 |
| Graduate Degree Programs (MA/MS/MEd/PhD) | 100 |
| Graduate Certificates | 41 |
| **Total Programs** | **340** |
| Colleges | 9 |

### 0.2 College-Department Hierarchy (Rule 2)

```
UT San Antonio
+-- Carlos Alvarez College of Business [College]
|   +-- Accounting [Dept]
|   +-- Economics [Dept]
|   +-- Finance [Dept]
|   +-- Management [Dept]
|   +-- Marketing [Dept]
|   +-- Operations and Analytics [Dept]
+-- College of AI, Cyber and Computing [College]
|   +-- Computer Engineering [Dept]
|   +-- Computer Science [Dept]
|   +-- Information Systems and Cybersecurity [Dept]
|   +-- Statistics and Data Science [Dept]
+-- College of Education and Human Development [College]
|   +-- Bicultural-Bilingual Studies [Dept]
|   +-- Counseling [Dept]
|   +-- Educational Leadership and Policy Studies [Dept]
|   +-- Educational Psychology [Dept]
|   +-- Interdisciplinary Learning and Teaching [Dept]
|   +-- Race, Ethnicity, Gender and Sexuality Studies [Dept]
+-- Klesse College of Engineering and Integrated Design [College]
|   +-- Architecture and Planning [Dept]
|   +-- Biomedical Engineering [Dept]
|   +-- Civil/Environmental Engineering and Construction Management [Dept]
|   +-- Electrical Engineering [Dept]
|   +-- Mechanical Engineering [Dept]
+-- College for Health, Community and Policy [College]
|   +-- Criminology [Dept]
|   +-- Kinesiology [Dept]
|   +-- Psychology [Dept]
|   +-- Public Administration [Dept]
|   +-- Public Health [Dept]
|   +-- Sociology [Dept]
+-- College of Liberal and Fine Arts [College]
|   +-- Anthropology [Dept]
|   +-- Art [Dept]
|   +-- Communication [Dept]
|   +-- English [Dept]
|   +-- History [Dept]
|   +-- Humanities and Social Sciences [Dept]
|   +-- Modern Languages and Literatures [Dept]
|   +-- Music [Dept]
|   +-- Philosophy and Classics [Dept]
|   +-- Political Science and Geography [Dept]
+-- College of Sciences [College]
|   +-- Biology [Dept]
|   +-- Chemistry [Dept]
|   +-- Earth and Planetary Sciences [Dept]
|   +-- Mathematics [Dept]
|   +-- Molecular Microbiology and Immunology [Dept]
|   +-- Neuroscience [Dept]
|   +-- Physics and Astronomy [Dept]
+-- University College [College]
|   +-- Multidisciplinary Studies [Dept]
+-- Honors College [College]
```

### 0.3 Degree Level Inventory (Rule 3)

| Canonical | Full Name | Level | Count |
|-----------|-----------|-------|-------|
| BA | Bachelor of Arts | UG | 39 |
| BS | Bachelor of Science | UG | 45 |
| BBA | Bachelor of Business Administration | UG | 10 |
| BFA | Bachelor of Fine Arts | UG | 1 |
| Minor | Minor | UG | 88 |
| Certificate | Undergraduate Certificate | UG | 16 |
| MA | Master of Arts | Grad | 14 |
| MS | Master of Science | Grad | 55 |
| MEd | Master of Education | Grad | 3 |
| GradCert | Graduate Certificate | Grad | 41 |
| PhD | Doctor of Philosophy | Grad | 28 |

### 0.4 Distribution Matrix (Rule 4)

| College | BA | BS | BBA | BFA | Minor | Cert | MA | MS | MEd | GradCert | PhD | Total |
|---------|----|----|-----|-----|-------|------|----|----|----|----------|-----|-------|
| Carlos Alvarez College of Business | 0 | 1 | 9 | 0 | 8 | 2 | 0 | 8 | 0 | 4 | 2 | 34 |
| College for Health, Community and Policy | 3 | 4 | 0 | 0 | 9 | 2 | 0 | 5 | 0 | 2 | 2 | 27 |
| College of AI, Cyber and Computing | 0 | 7 | 1 | 0 | 7 | 0 | 0 | 11 | 0 | 6 | 4 | 36 |
| College of Education and Human Development | 5 | 0 | 0 | 0 | 10 | 0 | 9 | 2 | 3 | 11 | 5 | 45 |
| College of Liberal and Fine Arts | 26 | 0 | 0 | 1 | 41 | 3 | 5 | 3 | 0 | 7 | 2 | 88 |
| College of Sciences | 4 | 22 | 0 | 0 | 9 | 1 | 0 | 7 | 0 | 2 | 7 | 52 |
| Klesse College of Engineering and Integrated Design | 0 | 10 | 0 | 0 | 0 | 8 | 0 | 19 | 0 | 9 | 6 | 52 |
| University College | 1 | 1 | 0 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 6 |
| **Total** |
 **39** |
 **45** |
 **10** |
 **1** |
 **88** |
 **16** |
 **14** |
 **55** |
 **3** |
 **41** |
 **28** |
 **340** |


---

## SECTION 1 — Undergraduate Education (Rule 5)

### 1.1 Architecture
UTSA undergraduate programs are organized by College (学院) → Department / Program (系) → Degree Level (学位级别) → Program Name (专业). The colleges below each contain multiple 系 and award primarily BA / BS / BBA / BFA at the undergraduate level. For the full hierarchy tree see Section 0.2.

### 1.2 Undergraduate Programs by College > Department > Degree Level


#### Carlos Alvarez College of Business


##### accounting


**BBA**

| # | Program |
|---|---------|
| 1 | Accounting |

##### economics


**BBA**

| # | Program |
|---|---------|
| 1 | Business Economics |

**BS**

| # | Program |
|---|---------|
| 1 | Economics |

**Minor**

| # | Program |
|---|---------|
| 1 | Economics |
| 2 | Focus Option 4, Complementary Minor |

##### finance


**BBA**

| # | Program |
|---|---------|
| 1 | Finance |
| 2 | Real Estate Finance and Development |

##### management


**BBA**

| # | Program |
|---|---------|
| 1 | Management |

**Minor**

| # | Program |
|---|---------|
| 1 | Entrepreneurship |
| 2 | Technology Management |

##### marketing


**BBA**

| # | Program |
|---|---------|
| 1 | Marketing |

**Minor**

| # | Program |
|---|---------|
| 1 | Marketing |
| 2 | Sport Management |

##### operationsanalytics


**BBA**

| # | Program |
|---|---------|
| 1 | Actuarial Science |
| 2 | Business Analytics |
| 3 | Operations and Supply Chain Management |

**Certificate**

| # | Program |
|---|---------|
| 1 | Business Analytics |
| 2 | Operations and Supply Chain Management |

**Minor**

| # | Program |
|---|---------|
| 1 | Actuarial Science |
| 2 | Operations and Supply Chain Management |

#### College for Health, Community and Policy


##### criminology


**BA**

| # | Program |
|---|---------|
| 1 | Criminology and Criminal Justice |

**Minor**

| # | Program |
|---|---------|
| 1 | Criminology and Criminal Justice |

##### kinesiology


**BS**

| # | Program |
|---|---------|
| 1 | Kinesiology |

**Certificate**

| # | Program |
|---|---------|
| 1 | Athletic Coaching |

##### psychology


**BA**

| # | Program |
|---|---------|
| 1 | Psychology |

**Minor**

| # | Program |
|---|---------|
| 1 | Psychology |

##### publicadministration


**Certificate**

| # | Program |
|---|---------|
| 1 | Public Policy and Data Analysis |

**Minor**

| # | Program |
|---|---------|
| 1 | Civic Engagement |
| 2 | Nonprofit Management |
| 3 | Public Administration and Policy |

##### publichealth


**BS**

| # | Program |
|---|---------|
| 1 | Health Administration |
| 2 | Public Health |

**Minor**

| # | Program |
|---|---------|
| 1 | Community Health |
| 2 | Wellness |

##### sociology


**BA**

| # | Program |
|---|---------|
| 1 | Sociology |

**BS**

| # | Program |
|---|---------|
| 1 | Health, Aging and Society |

**Minor**

| # | Program |
|---|---------|
| 1 | Health, Aging and Society |
| 2 | Sociology |

#### College of AI, Cyber and Computing


##### computerengineering


**BS**

| # | Program |
|---|---------|
| 1 | Computer Engineering |

##### computerscience


**BS**

| # | Program |
|---|---------|
| 1 | Computer Science |
| 2 | Software Engineering |

**Minor**

| # | Program |
|---|---------|
| 1 | Computer Science |

##### informationsystemscybersecurity


**BBA**

| # | Program |
|---|---------|
| 1 | Cybersecurity (Online) |

**BS**

| # | Program |
|---|---------|
| 1 | Applied Cyber Analytics |
| 2 | Cybersecurity |
| 3 | Information Systems and Technology |

**Minor**

| # | Program |
|---|---------|
| 1 | Cybersecurity |
| 2 | Digital Forensics |
| 3 | Enterprise Technology Administration |
| 4 | Information Systems and Technology |
| 5 | Minors |

##### statisticsdatascience


**BS**

| # | Program |
|---|---------|
| 1 | Statistics and Data Science |

**Minor**

| # | Program |
|---|---------|
| 1 | Statistics |

#### College of Education and Human Development


##### biculturalbilingualstudies


**Minor**

| # | Program |
|---|---------|
| 1 | Bicultural Studies |
| 2 | English as a Second Language |

##### educationalpsychology


**Minor**

| # | Program |
|---|---------|
| 1 | Educational Psychology Research in Society |

##### interdisciplinarylearningteaching


**BA**

| # | Program |
|---|---------|
| 1 | Education (EC–12 Special Education Certification Concentration) |
| 2 | Education (degree-only concentration) |

**Minor**

| # | Program |
|---|---------|
| 1 | AI and Education |
| 2 | Secondary Education |
| 3 | Special Education |

##### raceethnicitygendersexualitystudies


**BA**

| # | Program |
|---|---------|
| 1 | African American Studies |
| 2 | Mexican American Studies |
| 3 | Women's, Gender and Sexuality Studies |

**Minor**

| # | Program |
|---|---------|
| 1 | African American Studies |
| 2 | Mexican American Studies |
| 3 | Women's Studies |

##### teachercertificationprograms


**Minor**

| # | Program |
|---|---------|
| 1 | Secondary Education |

#### College of Liberal and Fine Arts


##### anthropology


**BA**

| # | Program |
|---|---------|
| 1 | Anthropology |

**Minor**

| # | Program |
|---|---------|
| 1 | American Indian Studies |
| 2 | Anthropology |
| 3 | Archaeological Practice |

##### art


**BA**

| # | Program |
|---|---------|
| 1 | Art |
| 2 | Art History and Criticism |

**BFA**

| # | Program |
|---|---------|
| 1 | Pre-Art Therapy |

**Minor**

| # | Program |
|---|---------|
| 1 | Art History and Criticism |

##### communication


**BA**

| # | Program |
|---|---------|
| 1 | Communication |
| 2 | Communication Online |
| 3 | Digital Media Influence |
| 4 | Digital Media Influence Online |
| 5 | Journalism |

**Minor**

| # | Program |
|---|---------|
| 1 | Communication |

##### english


**BA**

| # | Program |
|---|---------|
| 1 | English |
| 2 | English - No Concentration |

**Certificate**

| # | Program |
|---|---------|
| 1 | Creative Writing |
| 2 | Professional Writing, Rhetoric, and Digital Composition |

**Minor**

| # | Program |
|---|---------|
| 1 | English Literature |
| 2 | Professional Writing, Rhetoric, and Digital Composition |

##### history


**BA**

| # | Program |
|---|---------|
| 1 | History |

**Minor**

| # | Program |
|---|---------|
| 1 | American Studies |
| 2 | History |

##### humanitiesandsocialsciences


**BA**

| # | Program |
|---|---------|
| 1 | Community Arts |
| 2 | Dramatic Arts |
| 3 | Film and Media Studies |
| 4 | Medical Humanities |

**Minor**

| # | Program |
|---|---------|
| 1 | Community Arts |
| 2 | Dramatic Arts |
| 3 | Film Studies |
| 4 | Latin American Studies |
| 5 | Media and Medicine |
| 6 | Media, Literacy, and Education |
| 7 | Medical Humanities |
| 8 | Museum Studies |
| 9 | Spanish and Medical Humanities |

##### modernlanguagesliteratures


**BA**

| # | Program |
|---|---------|
| 1 | Linguistics in the Local and Global Community |
| 2 | Modern Language Studies |
| 3 | Spanish |

**Certificate**

| # | Program |
|---|---------|
| 1 | Healthcare Interpreting |

**Minor**

| # | Program |
|---|---------|
| 1 | Comparative Literature |
| 2 | Foreign Languages |
| 3 | French |
| 4 | German |
| 5 | Linguistics |
| 6 | Russian |
| 7 | Spanish |
| 8 | Spanish and Medical Humanities |
| 9 | Spanish and the Criminal Justice System |
| 10 | Translation and Interpreting Studies |

##### music


**BA**

| # | Program |
|---|---------|
| 1 | Commercial and Digital Music degree |
| 2 | Music degree |

**Minor**

| # | Program |
|---|---------|
| 1 | Dance |
| 2 | Jazz Studies |
| 3 | Music |
| 4 | Music Technology |

##### philosophyandclassics


**BA**

| # | Program |
|---|---------|
| 1 | Classical Studies and Humanities |
| 2 | Philosophy |

**Minor**

| # | Program |
|---|---------|
| 1 | Classical Studies |
| 2 | Humanities |
| 3 | Philosophy |
| 4 | Religious Studies |

##### politicalscienceandgeography


**BA**

| # | Program |
|---|---------|
| 1 | Geography and Environmental Sustainability |
| 2 | Global Affairs |
| 3 | Political Science |
| 4 | Politics and Law |

**Minor**

| # | Program |
|---|---------|
| 1 | Geography and Environmental Sustainability |
| 2 | Global Affairs |
| 3 | Intelligence and Security Studies |
| 4 | Political Science |
| 5 | Politics and Law |

#### College of Sciences


##### biology


**BA**

| # | Program |
|---|---------|
| 1 | Environmental Studies |

**BS**

| # | Program |
|---|---------|
| 1 | Biology |
| 2 | Course Sequence for B.S. Degree in Multidisciplinary Science for Teaching |
| 3 | Environmental Science |
| 4 | Health Sciences |
| 5 | Health Sciences - No Concentration |
| 6 | Health Sciences - Pre-Dental Concentration |
| 7 | Health Sciences - Pre-Medicine Concentration |
| 8 | Health Sciences - Pre-Pharmacy Concentration |
| 9 | Health Sciences - Pre-Physical Therapy Concentration |
| 10 | Health Sciences - Pre-Physician's Assistant Concentration |
| 11 | Health Sciences - Pre-Veterinary Concentration |
| 12 | Health Sciences – (No Concentration) |
| 13 | Multidisciplinary Science for Teaching​ |

**Minor**

| # | Program |
|---|---------|
| 1 | Biology |
| 2 | Environmental Science |

##### chemistry


**BA**

| # | Program |
|---|---------|
| 1 | Chemistry |

**BS**

| # | Program |
|---|---------|
| 1 | Biochemistry |
| 2 | Chemistry |

**Minor**

| # | Program |
|---|---------|
| 1 | Chemistry |

##### earthandplanetarysciences


**BA**

| # | Program |
|---|---------|
| 1 | Geosciences |

**BS**

| # | Program |
|---|---------|
| 1 | Geosciences |

**Certificate**

| # | Program |
|---|---------|
| 1 | Geographic Information System |

**Minor**

| # | Program |
|---|---------|
| 1 | Geosciences |

##### mathematics


**BS**

| # | Program |
|---|---------|
| 1 | Mathematics |
| 2 | Mathematics for Teaching |
| 3 | Mathematics of Data and Computing |

**Minor**

| # | Program |
|---|---------|
| 1 | Mathematics |

##### molecularmicrobiologyimmunology


**BS**

| # | Program |
|---|---------|
| 1 | Microbiology and Immunology |

##### neuroscience


**BS**

| # | Program |
|---|---------|
| 1 | Neuroscience |

**Minor**

| # | Program |
|---|---------|
| 1 | Developmental and Regenerative Sciences |
| 2 | Neuroscience |

##### physicsandastronomy


**BA**

| # | Program |
|---|---------|
| 1 | Physics |

**BS**

| # | Program |
|---|---------|
| 1 | Physics |

**Minor**

| # | Program |
|---|---------|
| 1 | Astronomy/Astrophysics |
| 2 | Physics |

#### Klesse College of Engineering and Integrated Design


##### architectureandplanning


**BS**

| # | Program |
|---|---------|
| 1 | Architecture |
| 2 | Interior Design |

**Certificate**

| # | Program |
|---|---------|
| 1 | Design Communication and Fabrication |

##### biomedicalengineering


**BS**

| # | Program |
|---|---------|
| 1 | Biomedical Engineering |
| 2 | Chemical Engineering |

##### civilenvironengr-constructionmgt


**BS**

| # | Program |
|---|---------|
| 1 | Civil Engineering |
| 2 | Construction Science and Management |

##### electricalengineering


**BS**

| # | Program |
|---|---------|
| 1 | Electrical Engineering |
| 2 | Integrated B.S./M.S. in Electrical Engineering |

**Certificate**

| # | Program |
|---|---------|
| 1 | Artificial Intelligence |
| 2 | Computer Programming for Engineers |
| 3 | Semiconductor Engineering |

##### mechanicalengineering


**BS**

| # | Program |
|---|---------|
| 1 | Industrial and Systems Engineering |
| 2 | Mechanical Engineering |

**Certificate**

| # | Program |
|---|---------|
| 1 | Aerospace Engineering |
| 2 | Heating, Ventilation and Air-Conditioning |
| 3 | Industrial and Manufacturing Engineering |
| 4 | Oil/Gas |

#### University College


##### multidisciplinary


**BA**

| # | Program |
|---|---------|
| 1 | Multidisciplinary Studies |

**BS**

| # | Program |
|---|---------|
| 1 | Multidisciplinary Studies |

##### rotc


**Minor**

| # | Program |
|---|---------|
| 1 | Aerospace Studies |
| 2 | Minor |

##### rotcarmy


**Minor**

| # | Program |
|---|---------|
| 1 | Military Management and Leadership |
| 2 | Minor |


---

### 1.7 Reconciliation block
> Per contract reconciliation: Rule-1 UG total = N1; Rule-4 matrix sum = N2; Rule-5 §1.2 row count = N3. **Status**: PENDING per-program walk.

## SECTION 2 — Graduate Education (Rule 5)

### 2.1 Graduate Programs by College > Department > Degree Level
(Rule 5 leaf enumeration — see `#### College / ##### Department / ###### Degree Level` tables immediately below for the exhaustive list.)

### 2.2 At least one program's full deep-dive (worked example)
Deferred to a representative MS or PhD (e.g. MS in Computer Science under Carlos Alvarez College of Business — full deep-dive URL + GRE/TOEFL materials live behind the program's accordion section on the catalog page). See Section 6 follow-up items P0/P1 for the work item.




#### Carlos Alvarez College of Business


##### accounting


**MS**

| # | Program |
|---|---------|
| 1 | Master of Accountancy (MACY) |

**PhD**

| # | Program |
|---|---------|
| 1 | Accounting |

##### economics


**MS**

| # | Program |
|---|---------|
| 1 | Accelerated Master of Science in Economics |
| 2 | Economics – Business Data Analysis and Forecasting Concentration |
| 3 | Economics – Financial Economics Concentration |
| 4 | Economics – General Economics Concentration |

##### finance


**MS**

| # | Program |
|---|---------|
| 1 | Accelerated M.S. in Finance Program |
| 2 | Finance – General Option |
| 3 | Finance – Real Estate Finance and Development Concentration |

**PhD**

| # | Program |
|---|---------|
| 1 | Finance |

##### management


**GradCert**

| # | Program |
|---|---------|
| 1 | Project Management |
| 2 | Technology Entrepreneurship and Management |

##### operationsanalytics


**GradCert**

| # | Program |
|---|---------|
| 1 | Business Analytics |
| 2 | Operations and Supply Chain Management |

#### College for Health, Community and Policy


##### psychology


**MS**

| # | Program |
|---|---------|
| 1 | Psychology |

**PhD**

| # | Program |
|---|---------|
| 1 | Psychology |

##### publicadministration


**MS**

| # | Program |
|---|---------|
| 1 | Accelerated Master of Public Administration |
| 2 | Master of Public Administration |

##### publichealth


**GradCert**

| # | Program |
|---|---------|
| 1 | Applied Health Research |
| 2 | Health |

##### sociology


**MS**

| # | Program |
|---|---------|
| 1 | Applied Demography |
| 2 | Sociology |

**PhD**

| # | Program |
|---|---------|
| 1 | Applied Demography |

#### College of AI, Cyber and Computing


##### computerengineering


**MS**

| # | Program |
|---|---------|
| 1 | Artificial Intelligence |
| 2 | Computer Engineering |
| 3 | Integrated Bachelor's/Master's Program |

**PhD**

| # | Program |
|---|---------|
| 1 | Computer Engineering |

##### computerscience


**MS**

| # | Program |
|---|---------|
| 1 | Artificial Intelligence |
| 2 | Computer Science |
| 3 | Cybersecurity Science |

**PhD**

| # | Program |
|---|---------|
| 1 | Computer Science |

##### informationsystemscybersecurity


**GradCert**

| # | Program |
|---|---------|
| 1 | Cloud Computing |
| 2 | Cybersecurity |
| 3 | Intelligence Studies |

**MS**

| # | Program |
|---|---------|
| 1 | Information Technology |

**PhD**

| # | Program |
|---|---------|
| 1 | Information Technology |

##### statisticsdatascience


**GradCert**

| # | Program |
|---|---------|
| 1 | Data Engineering |
| 2 | Data Science |
| 3 | Predictive Analytics and Modeling |

**MS**

| # | Program |
|---|---------|
| 1 | Accelerated Master of Science in Data Analytics |
| 2 | Accelerated Master of Science in Statistics and Data Science |
| 3 | Data Analytics |
| 4 | Statistics and Data Science |

**PhD**

| # | Program |
|---|---------|
| 1 | Applied Statistics |

#### College of Education and Human Development


##### biculturalbilingualstudies


**GradCert**

| # | Program |
|---|---------|
| 1 | Bilingual Education |
| 2 | Bilingual Reading Specialist |
| 3 | Teaching English as a Second Language |
| 4 | Technology for Language Education |

**MA**

| # | Program |
|---|---------|
| 1 | Bicultural-Bilingual Education |
| 2 | Teaching English as a Second Language |

**PhD**

| # | Program |
|---|---------|
| 1 | Culture, Literacy and Language |

##### counseling


**GradCert**

| # | Program |
|---|---------|
| 1 | Bilingual Counseling |
| 2 | Integrated Behavioral Healthcare |

**MEd**

| # | Program |
|---|---------|
| 1 | School Counseling |

**MS**

| # | Program |
|---|---------|
| 1 | Clinical Mental Health Counseling |

**PhD**

| # | Program |
|---|---------|
| 1 | Counselor Education and Supervision |

##### educationalleadershippolicystudies


**MEd**

| # | Program |
|---|---------|
| 1 | Educational Leadership |
| 2 | Higher Education Administration |

**PhD**

| # | Program |
|---|---------|
| 1 | Educational Leadership |

##### educationalpsychology


**GradCert**

| # | Program |
|---|---------|
| 1 | Applied Behavior Analysis |
| 2 | Language Acquisition and Bilingual Psychoeducational Assessment |
| 3 | Program Evaluation and Applied Research |

**MA**

| # | Program |
|---|---------|
| 1 | Applied Educational Psychology |
| 2 | School Psychology |

**MS**

| # | Program |
|---|---------|
| 1 | Behavior Analysis |

**PhD**

| # | Program |
|---|---------|
| 1 | School Psychology |

##### interdisciplinarylearningteaching


**GradCert**

| # | Program |
|---|---------|
| 1 | Foundations of Learning, Design, and Technology |
| 2 | I-STEM Education |

**MA**

| # | Program |
|---|---------|
| 1 | Curriculum and Instruction |
| 2 | Early Childhood and Elementary Education |
| 3 | Learning, Design, and Technology |
| 4 | Literacy Education |
| 5 | Special Education |

**PhD**

| # | Program |
|---|---------|
| 1 | Interdisciplinary Learning and Teaching |

#### College of Liberal and Fine Arts


##### anthropology


**MA**

| # | Program |
|---|---------|
| 1 | Anthropology |

**PhD**

| # | Program |
|---|---------|
| 1 | Anthropology |

##### english


**GradCert**

| # | Program |
|---|---------|
| 1 | Creative Writing |
| 2 | Rhetoric and Composition |

**MA**

| # | Program |
|---|---------|
| 1 | English |

**PhD**

| # | Program |
|---|---------|
| 1 | English |

##### modernlanguagesliteratures


**GradCert**

| # | Program |
|---|---------|
| 1 | Linguistics |
| 2 | Translation and Interpreting Studies |

##### music


**GradCert**

| # | Program |
|---|---------|
| 1 | Instrumental Performance |
| 2 | Music Pedagogy |
| 3 | Music Theory Pedagogy |

**MS**

| # | Program |
|---|---------|
| 1 | Master of Music – Conducting Emphasis (Instrumental or Choral) |
| 2 | Master of Music – Music Education Emphasis |
| 3 | Master of Music – Performance Emphasis (Instrumental or Vocal) |

##### politicalscienceandgeography


**MA**

| # | Program |
|---|---------|
| 1 | Geography and Environmental Sustainability |
| 2 | Global Affairs |
| 3 | Political Science |

#### College of Sciences


##### biology


**GradCert**

| # | Program |
|---|---------|
| 1 | Environmental Science |
| 2 | Environmental Sustainability |

**MS**

| # | Program |
|---|---------|
| 1 | Biology |
| 2 | Environmental Science |

**PhD**

| # | Program |
|---|---------|
| 1 | Environmental Science and Engineering |

##### chemistry


**MS**

| # | Program |
|---|---------|
| 1 | Chemistry |

**PhD**

| # | Program |
|---|---------|
| 1 | Chemistry |

##### earthandplanetarysciences


**MS**

| # | Program |
|---|---------|
| 1 | Geoinformatics |
| 2 | Geosciences |

**PhD**

| # | Program |
|---|---------|
| 1 | Environmental Science and Engineering |

##### molecularmicrobiologyimmunology


**MS**

| # | Program |
|---|---------|
| 1 | Biotechnology |

**PhD**

| # | Program |
|---|---------|
| 1 | Molecular Microbiology and Immunology |

##### neuroscience


**PhD**

| # | Program |
|---|---------|
| 1 | Developmental and Regenerative Sciences |
| 2 | Neuroscience |

##### physicsandastronomy


**MS**

| # | Program |
|---|---------|
| 1 | Physics |

**PhD**

| # | Program |
|---|---------|
| 1 | Physics |

#### Klesse College of Engineering and Integrated Design


##### architectureandplanning


**GradCert**

| # | Program |
|---|---------|
| 1 | High-Performance Design and Sustainability |
| 2 | Historic Preservation |
| 3 | Urban and Regional Planning |

**MS**

| # | Program |
|---|---------|
| 1 | Architecture (M.S.) application website |
| 2 | Architecture - The Research Program |
| 3 | Dual Master of Architecture and M.S. Urban and Regional Planning |
| 4 | Dual Master of Architecture and M.S. in Architecture |
| 5 | Master of Architecture - The Professional Program |
| 6 | Urban and Regional Planning |
| 7 | Urban and Regional Planning (M.S.) application website |

##### biomedicalengineering


**GradCert**

| # | Program |
|---|---------|
| 1 | Engineering Education |
| 2 | Medical Device Commercialization |

**MS**

| # | Program |
|---|---------|
| 1 | Biomedical Engineering |
| 2 | Biomedical Technology Commercialization |
| 3 | Chemical Engineering |
| 4 | Engineering Education |

**PhD**

| # | Program |
|---|---------|
| 1 | Biomedical Engineering |
| 2 | Chemical Engineering |

##### civilenvironengr-constructionmgt


**GradCert**

| # | Program |
|---|---------|
| 1 | Construction Engineering, Science and Management |
| 2 | Facility Management |

**MS**

| # | Program |
|---|---------|
| 1 | Civil Engineering |
| 2 | Facility Management |
| 3 | Master of Civil Engineering |

**PhD**

| # | Program |
|---|---------|
| 1 | Civil Engineering |
| 2 | Environmental Science and Engineering |

##### electricalengineering


**MS**

| # | Program |
|---|---------|
| 1 | Advanced Materials Engineering |
| 2 | Electrical Engineering |
| 3 | Integrated Bachelor's/Master's Program |

**PhD**

| # | Program |
|---|---------|
| 1 | Electrical Engineering |

##### mechanicalengineering


**GradCert**

| # | Program |
|---|---------|
| 1 | Aerospace Engineering |
| 2 | Engineering Education |

**MS**

| # | Program |
|---|---------|
| 1 | Advanced Manufacturing and Industrial Engineering |
| 2 | Mechanical Engineering |

**PhD**

| # | Program |
|---|---------|
| 1 | Mechanical Engineering |


### 2.3 Graduate Admissions Model

UTSA uses a centralized Graduate Admissions Application (Liaison CAS). Requirements and deadlines are program-specific. Each program has a Graduate Advisor of Record (GAR).

---

## SECTION 3 — Application Requirements and Deadlines

### 3.1 Undergraduate Core Data

| Field | Value | Source |
|-------|-------|--------|
| Application Platforms | ApplyTexas, Common App | future.utsa.edu/freshman/admissions/ |
| Application Fee | $75 | future.utsa.edu/freshman/admissions/ |
| Priority Deadline (Fall) | January 15 | future.utsa.edu/freshman/admissions/ |
| International Deadline (Fall) | June 1 (app) / June 15 (docs) | future.utsa.edu/freshman/admissions/ |
| Domestic Deadline (Fall) | June 1 (app) / June 15 (docs) | future.utsa.edu/freshman/admissions/ |
| Spring Priority Deadline | October 15 | future.utsa.edu/freshman/admissions/ |
| Test Policy | TEST-OPTIONAL | future.utsa.edu/freshman/admissions/ |
| SAT Code | 6919 | future.utsa.edu/freshman/admissions/ |
| ACT Code | 4239 | future.utsa.edu/freshman/admissions/ |
| Guaranteed Admission (Top 25%) | No minimum score | future.utsa.edu/freshman/admissions/ |
| Guaranteed Admission (2nd 25%) | 1170 SAT / 24 ACT | future.utsa.edu/freshman/admissions/ |

### 3.2 English Proficiency (Undergraduate)

| Exam | Minimum Score | Notes |
|------|---------------|-------|
| TOEFL iBT (pre-Jan 21 2026) | 79 | future.utsa.edu/international/ |
| TOEFL iBT (post-Jan 21 2026) | 4.0 | New scoring scale |
| TOEFL PBT | 550 | |
| IELTS | 6.5 | Academic exam required |
| PTE Academic | 58 | UG only |
| iTEP Academic | 3.8 | UG only |
| Cambridge C1 Advanced | 180 (grade C) | UG only |
| Duolingo English Test | 95 | |
| SAT Critical Reading | 500 | Alternative for UG |
| ACT English | 21 | Alternative for UG |

### 3.3 Graduate Admissions

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | Liaison CAS | future.utsa.edu/graduate/admissions/ |
| Fee (Domestic) | $50 | future.utsa.edu/graduate/admissions/ |
| Fee (International) | $90 | future.utsa.edu/graduate/admissions/ |
| GRE/GMAT | Per-program | future.utsa.edu/graduate/admissions/ |
| ETS Code | 6919 | future.utsa.edu/graduate/admissions/ |
| TOEFL Minimum | 79 / 4.0 | future.utsa.edu/international/ |
| IELTS Minimum | 6.5 | future.utsa.edu/international/ |
| DET Minimum (Grad) | 100 | future.utsa.edu/international/ |
| Deadlines | Vary by program | future.utsa.edu/graduate/admissions/ |

---

## SECTION 4 — Costs and Financial Aid

### 4.1 Undergraduate Cost of Attendance 2026-2027

| Expense | At Home | Off Campus | On Campus |
|---------|---------|------------|-----------|
| Tuition & Fees (in-state) | $11,448 | $11,448 | $11,448 |
| Tuition & Fees (out-of-state) | $27,598 | $27,598 | $27,598 |
| Books & Supplies | $1,000 | $1,000 | $1,000 |
| Housing | $2,880 | $8,110 | $10,484 |
| Meals | $2,764 | $4,168 | $5,878 |
| Transportation | $3,216 | $3,990 | $774 |
| Personal/Misc | $1,540 | $2,134 | $2,160 |
| Loan Fees | $68 | $68 | $68 |
| **Total (in-state)** | **$22,916** | **$30,918** | **$31,812** |
| **Total (out-of-state)** | **$39,066** | **$47,068** | **$47,962** |

Source: future.utsa.edu/freshman/aid/

### 4.2 Financial Aid Policy

- **Bold Promise**: Free tuition and fees for qualifying Texas residents (family income up to $70,000)
- **Distinguished Presidential Scholarship**: Up to $24,000 over 4 years (deadline Jan 15)
- **Need-aware** for all applicants (not need-blind)
- Financial Aid Priority Deadline: January 15 (Fall), November 1 (Spring)

### 4.3 Graduate Cost and Funding

- Domestic fee: $50 per application
- International fee: $90 per application
- Funding via assistantships, fellowships, scholarships
- KRWU program for high-achieving students/alumni

---

## SECTION 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Snippet | Date |
|----|-------|-------|-----------|---------|------|
| E-U-001 | ug.deadlines.priority | Jan 15 | future.utsa.edu/freshman/admissions/ | Priority Freshman Deadline: January 15 | 2026-07-06 |
| E-U-002 | ug.test_policy | Test-optional | future.utsa.edu/freshman/admissions/ | You do not need to submit SAT or ACT scores | 2026-07-06 |
| E-U-003 | ug.tuition_in_state | $11,448 | future.utsa.edu/freshman/aid/ | Tuition and Fees: $11,448 | 2026-07-06 |
| E-U-004 | ug.tuition_oos | $27,598 | future.utsa.edu/freshman/aid/ | non-resident tuition and fees = $27,598 | 2026-07-06 |
| E-U-005 | ug.app_fee | $75 | future.utsa.edu/freshman/admissions/ | application fee is $75 | 2026-07-06 |
| E-U-006 | ug.toefl | 79/4.0 | future.utsa.edu/international/ | TOEFL IBT: 79 or greater / 4.0 or greater | 2026-07-06 |
| E-U-007 | ug.ielts | 6.5 | future.utsa.edu/international/ | IELTS: 6.5 or greater | 2026-07-06 |
| E-U-008 | ug.det | 95 | future.utsa.edu/international/ | DET: 95 or greater | 2026-07-06 |
| E-G-001 | grad.fee_domestic | $50 | future.utsa.edu/graduate/admissions/ | $50 Domestic Applicants | 2026-07-06 |
| E-G-002 | grad.fee_intl | $90 | future.utsa.edu/graduate/admissions/ | $90 International Applicants | 2026-07-06 |
| E-G-003 | grad.ets_code | 6919 | future.utsa.edu/graduate/admissions/ | institutional code is 6919 | 2026-07-06 |

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
utsa-knowledge-base-v2/
+-- 00-institution-overview/
|   +-- program-counts.md
|   +-- college-hierarchy.md
|   +-- degree-inventory.md
|   +-- distribution-matrix.md
+-- 01-undergraduate-programs/ (one chunk per college)
+-- 02-graduate-programs/ (one chunk per college)
+-- 03-deadlines-requirements/
+-- 04-costs-financial-aid/
```

### Follow-up Items

| Priority | Item | URL |
|----------|------|-----|
| P0 | Verify MBA details | catalog.utsa.edu/graduate/business/ |
| P0 | Verify MFA Art details | catalog.utsa.edu/graduate/liberalfinearts/ |
| P0 | Check DNP/DPT (Health Science Center) | catalog.uthscsa.edu/ |
| P1 | Per-program grad deadlines | Individual program pages |
| P1 | Verify Bold Promise threshold | future.utsa.edu/promise/ |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UTSA |
|-----------|------|
| Type | Public (UT System) |
| Location | San Antonio, TX |
| UG Tuition (in-state) | $11,448 |
| UG Tuition (out-of-state) | $27,598 |
| Test Policy | Test-optional |
| Priority Deadline | January 15 |
| Final Deadline (Fall) | June 1 |
| TOEFL Minimum | 79 / 4.0 |
| IELTS Minimum | 6.5 |
| DET Minimum | 95 |
| App Fee (UG) | $75 |
| App Fee (Grad) | $50 / $90 |
| Need-blind | No (need-aware) |
| Total Programs | 340 |
| UG Programs | 199 |
| Grad Programs | 141 |
| Colleges | 9 |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: future.utsa.edu, catalog.utsa.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
