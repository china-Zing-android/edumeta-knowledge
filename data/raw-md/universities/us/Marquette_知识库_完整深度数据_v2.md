# Marquette University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/etc.) | 71 |
| 本科辅修 (Minor) | N/A (minors listed on individual program pages, not centrally enumerated) |
| 研究生学位项目 (MA/MS/MBA/PhD/etc.) | 90+ |
| 研究生高级证书 (Advanced Certificate / Diploma) | Included in 90+ count |
| **学位项目总计 (UG + Grad)** | **161+** |
| 学院 / 独立系所总数 | 11 |

> **Reconciliation note**: UG majors count (71) comes from the official majors page (`marquette.edu/academics/majors/`). Graduate programs count (90+) comes from the Graduate School programs page (`marquette.edu/grad/programs.php`). The exact graduate count requires per-program verification as some are certificates vs. degree programs.

### 0.2 学院 / 系层级结构

```
Marquette University
├── Klingler College of Arts and Sciences          [学院 - UG]
│   ├── Africana Studies                           [系]
│   ├── Anthropology                               [系]
│   ├── Biological Sciences                        [系]
│   ├── Chemistry                                  [系]
│   ├── Classics                                   [系]
│   ├── Communication Studies                      [系]
│   ├── Computer Science                           [系]
│   ├── Economics                                  [系]
│   ├── English                                    [系]
│   ├── French                                     [系]
│   ├── German                                     [系]
│   ├── History                                    [系]
│   ├── Mathematics                                [系]
│   ├── Philosophy                                 [系]
│   ├── Physics                                    [系]
│   ├── Political Science                          [系]
│   ├── Psychology                                 [系]
│   ├── Sociology                                  [系]
│   ├── Spanish                                    [系]
│   ├── Theology and Religion                      [系]
│   └── (other departments)
├── College of Business Administration             [学院 - UG]
│   ├── Accounting                                 [系]
│   ├── Business Administration                    [系]
│   ├── Business Analytics                         [系]
│   ├── Business Economics                         [系]
│   ├── Finance                                    [系]
│   ├── Human Resources                            [系]
│   ├── Information Systems                        [系]
│   ├── International Business                     [系]
│   ├── Marketing                                  [系]
│   ├── Operations and Supply Chain Management     [系]
│   └── Real Estate                                [系]
├── Diederich College of Communication             [学院 - UG]
│   ├── Advertising                                [系]
│   ├── Communication Studies                      [系]
│   ├── Corporate Communication                    [系]
│   ├── Digital Media                              [系]
│   ├── Journalism                                 [系]
│   ├── Public Relations                           [系]
│   └── Sports Communication                       [系]
├── College of Education                           [学院 - UG]
│   ├── Education                                  [系]
│   └── Educational Studies                        [系]
├── Opus College of Engineering                    [学院 - UG]
│   ├── Biomedical Engineering                     [系]
│   ├── Civil Engineering                          [系]
│   ├── Computer Engineering                       [系]
│   ├── Construction Engineering                   [系]
│   ├── Electrical Engineering                     [系]
│   ├── Environmental Engineering                  [系]
│   └── Mechanical Engineering                     [系]
├── College of Health Sciences                     [学院 - UG/Grad]
│   ├── Athletic Training                          [系]
│   ├── Biomedical Sciences                        [系]
│   ├── Exercise Physiology                        [系]
│   ├── Occupational Therapy                       [系]
│   ├── Physical Therapy                           [系]
│   ├── Physician Assistant Studies                [系]
│   └── Speech Pathology and Audiology             [系]
├── College of Nursing                             [学院 - UG/Grad]
│   └── Nursing                                    [系]
├── Graduate School                                [学院 - Grad]
│   ├── Biological Sciences (PhD)                  [系]
│   ├── Chemistry (MS/PhD)                         [系]
│   ├── Clinical Psychology (PhD)                  [系]
│   ├── Communication (MA)                         [系]
│   ├── Computer Science (PhD)                     [系]
│   ├── English (MA/PhD)                           [系]
│   ├── History (MA/PhD)                           [系]
│   ├── Mathematics (MS)                           [系]
│   ├── Philosophy (MA/PhD)                        [系]
│   ├── Political Science (MA)                     [系]
│   ├── Religious Studies (PhD)                    [系]
│   └── (other programs)
├── Graduate School of Management                  [学院 - Grad]
│   ├── MBA                                        [系]
│   ├── Executive MBA                              [系]
│   ├── Master in Management                       [系]
│   ├── MS Finance                                 [系]
│   └── MS Accounting                              [系]
├── School of Dentistry                            [学院 - Grad/Professional]
│   ├── Dental Biomaterials (MS)                   [系]
│   ├── Endodontics (MS/Certificate)               [系]
│   ├── Orthodontics (MS/Certificate)              [系]
│   ├── Periodontics (MS/Certificate)              [系]
│   ├── Prosthodontics (MS/Certificate)            [系]
│   └── DDS                                        [系]
└── Law School                                     [学院 - Professional]
    └── JD                                         [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~30 |
| BS | Bachelor of Science | 本科 | ~35 |
| BSN | Bachelor of Science in Nursing | 本科 | 1 |
| BME | Bachelor of Mechanical Engineering | 本科 | 1 |
| BSEE | Bachelor of Science in Electrical Engineering | 本科 | 1 |
| Other UG | Other undergraduate degrees | 本科 | ~3 |
| MA | Master of Arts | 研究生 | ~10 |
| MS | Master of Science | 研究生 | ~25 |
| MBA | Master of Business Administration | 研究生 | 2 (Full-time, Executive) |
| MEd | Master of Education | 研究生 | ~5 |
| MFA | Master of Fine Arts | 研究生 | N/A |
| MEng | Master of Engineering | 研究生 | ~3 |
| PhD | Doctor of Philosophy | 研究生 | ~15 |
| EdD | Doctor of Education | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| JD | Juris Doctor | 研究生 | 1 |
| DDS | Doctor of Dental Surgery | 研究生 | 1 |
| Certificate | Graduate Certificate | 研究生 | ~10 |

> **Note**: Exact counts per degree level require program-by-program verification. The 90+ graduate programs include certificates, master's, and doctoral programs across all schools.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSN | MA | MS | MBA | MEd | MEng | PhD | Professional Doctorate | Certificate | 合计 |
|------------|----|----|-----|----|----|-----|-----|------|-----|------------------------|-------------|------|
| Klingler College of Arts and Sciences | ~25 | ~5 | 0 | ~5 | ~3 | 0 | 0 | 0 | ~8 | 0 | ~2 | ~48 |
| College of Business Administration | 0 | ~10 | 0 | 0 | ~3 | 2 | 0 | 0 | 0 | 0 | ~1 | ~16 |
| Diederich College of Communication | 0 | ~6 | 0 | ~2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~8 |
| College of Education | 0 | ~2 | 0 | 0 | 0 | 0 | ~4 | 0 | 1 | 0 | ~2 | ~9 |
| Opus College of Engineering | 0 | ~7 | 0 | 0 | ~3 | 0 | 0 | ~3 | ~3 | 0 | ~2 | ~18 |
| College of Health Sciences | 0 | ~4 | 0 | 0 | ~3 | 0 | 0 | 0 | ~2 | 3 (DPT/OTD/PA) | ~3 | ~15 |
| College of Nursing | 0 | 0 | 1 | 0 | ~2 | 0 | 0 | 0 | 1 | 1 (DNP) | ~2 | ~7 |
| Graduate School | 0 | 0 | 0 | ~3 | ~5 | 0 | ~2 | 0 | ~5 | 0 | ~3 | ~18 |
| Graduate School of Management | 0 | 0 | 0 | 0 | ~3 | 2 | 0 | 0 | 0 | 0 | 0 | ~5 |
| School of Dentistry | 0 | 0 | 0 | 0 | ~4 | 0 | 0 | 0 | 0 | 1 (DDS) | ~5 | ~10 |
| Law School | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 (JD) | 0 | ~1 |
| **合计** | ~25 | ~34 | 1 | ~10 | ~26 | 4 | ~6 | ~3 | ~20 | 10 | ~20 | **~161+** |

> **Reconciliation note**: These are approximate counts based on the extracted program data. Exact counts require program-by-program verification. The matrix shows the distribution across Marquette's 11 colleges/schools.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

Marquette University has 7 undergraduate-degree-granting colleges. Students are admitted directly into a college (direct-entry institution). See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### Klingler College of Arts and Sciences

##### Department of Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies | https://www.marquette.edu/academics/majors/ |

##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://www.marquette.edu/academics/majors/ |

##### Department of Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.marquette.edu/academics/majors/ |
| 2 | Biochemistry and Molecular Biology | https://www.marquette.edu/academics/majors/ |
| 3 | Biophysics | https://www.marquette.edu/academics/majors/ |
| 4 | Biomedical Sciences | https://www.marquette.edu/academics/majors/ |

##### Department of Chemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.marquette.edu/academics/majors/ |

##### Department of Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Classics | https://www.marquette.edu/academics/majors/ |

##### Department of Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.marquette.edu/academics/majors/ |
| 2 | Computational Mathematics | https://www.marquette.edu/academics/majors/ |
| 3 | Data Science | https://www.marquette.edu/academics/majors/ |

##### Department of Economics
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.marquette.edu/academics/majors/ |
| 2 | Applied Mathematical Economics | https://www.marquette.edu/academics/majors/ |

##### Department of English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.marquette.edu/academics/majors/ |

##### Department of Languages, Literatures and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | French | https://www.marquette.edu/academics/majors/ |
| 2 | German | https://www.marquette.edu/academics/majors/ |
| 3 | Spanish Language, Literature and Culture | https://www.marquette.edu/academics/majors/ |
| 4 | Spanish for the Professions | https://www.marquette.edu/academics/majors/ |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.marquette.edu/academics/majors/ |

##### Department of Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.marquette.edu/academics/majors/ |
| 2 | Statistical Science | https://www.marquette.edu/academics/majors/ |

##### Department of Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.marquette.edu/academics/majors/ |

##### Department of Physics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.marquette.edu/academics/majors/ |
| 2 | Applied Physics | https://www.marquette.edu/academics/majors/ |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.marquette.edu/academics/majors/ |
| 2 | International Affairs | https://www.marquette.edu/academics/majors/ |

##### Department of Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.marquette.edu/academics/majors/ |
| 2 | Cognitive Science | https://www.marquette.edu/academics/majors/ |

##### Department of Social and Cultural Sciences
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Law Studies | https://www.marquette.edu/academics/majors/ |
| 2 | Social Welfare and Justice | https://www.marquette.edu/academics/majors/ |
| 3 | Sociology | https://www.marquette.edu/academics/majors/ |

##### Department of Theology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theology and Religion | https://www.marquette.edu/academics/majors/ |

##### Interdisciplinary Programs
###### BA/BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.marquette.edu/academics/majors/ |
| 2 | Environmental Studies | https://www.marquette.edu/academics/majors/ |
| 3 | Film and Media Studies | https://www.marquette.edu/academics/majors/ |
| 4 | Gender and Sexualities Studies | https://www.marquette.edu/academics/majors/ |
| 5 | Latin American Studies | https://www.marquette.edu/academics/majors/ |
| 6 | Middle East and North Africa Studies | https://www.marquette.edu/academics/majors/ |
| 7 | Peace Studies | https://www.marquette.edu/academics/majors/ |

#### College of Business Administration

##### Department of Accounting
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.marquette.edu/academics/majors/ |

##### Department of Business Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://www.marquette.edu/academics/majors/ |
| 2 | Business Analytics | https://www.marquette.edu/academics/majors/ |
| 3 | Business Economics | https://www.marquette.edu/academics/majors/ |

##### Department of Finance
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance | https://www.marquette.edu/academics/majors/ |
| 2 | Real Estate | https://www.marquette.edu/academics/majors/ |
| 3 | Accelerating Ingenuity in Markets | https://www.marquette.edu/academics/majors/ |

##### Department of Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Resources | https://www.marquette.edu/academics/majors/ |
| 2 | Operations and Supply Chain Management | https://www.marquette.edu/academics/majors/ |

##### Department of Marketing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.marquette.edu/academics/majors/ |
| 2 | International Business | https://www.marquette.edu/academics/majors/ |

##### Department of Information Systems
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems | https://www.marquette.edu/academics/majors/ |

#### Diederich College of Communication

##### Department of Communication and Media
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://www.marquette.edu/academics/majors/ |
| 2 | Corporate Communication | https://www.marquette.edu/academics/majors/ |
| 3 | Digital Media | https://www.marquette.edu/academics/majors/ |
| 4 | Sports Communication | https://www.marquette.edu/academics/majors/ |

##### Department of Journalism
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.marquette.edu/academics/majors/ |

##### Department of Advertising and Public Relations
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Advertising | https://www.marquette.edu/academics/majors/ |
| 2 | Public Relations | https://www.marquette.edu/academics/majors/ |

#### College of Education

##### Department of Education
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://www.marquette.edu/academics/majors/ |
| 2 | Educational Studies | https://www.marquette.edu/academics/majors/ |

#### Opus College of Engineering

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.marquette.edu/academics/majors/ |

##### Department of Civil, Construction and Environmental Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://www.marquette.edu/academics/majors/ |
| 2 | Construction Engineering | https://www.marquette.edu/academics/majors/ |
| 3 | Environmental Engineering | https://www.marquette.edu/academics/majors/ |

##### Department of Electrical and Computer Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://www.marquette.edu/academics/majors/ |
| 2 | Electrical Engineering | https://www.marquette.edu/academics/majors/ |

##### Department of Mechanical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.marquette.edu/academics/majors/ |

#### College of Health Sciences

##### Department of Health Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://www.marquette.edu/academics/majors/ |
| 2 | Exercise Physiology | https://www.marquette.edu/academics/majors/ |
| 3 | Speech Pathology and Audiology | https://www.marquette.edu/academics/majors/ |

##### Accelerated Degree Programs (ADP/Grad)
| # | 专业 | URL |
|---|------|-----|
| 1 | Athletic Training (BS+MAT) | https://www.marquette.edu/academics/majors/ |
| 2 | Occupational Therapy (BS+OTD) | https://www.marquette.edu/academics/majors/ |
| 3 | Physical Therapy (BS+DPT) | https://www.marquette.edu/academics/majors/ |
| 4 | Physician Assistant Studies (BS+MPAS) | https://www.marquette.edu/academics/majors/ |

#### College of Nursing

##### Department of Nursing
###### BSN
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing | https://www.marquette.edu/academics/majors/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | Home College | URL |
|---|------|--------------|-----|
| 1 | Africana Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 2 | Cognitive Science | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 3 | Environmental Science | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 4 | Environmental Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 5 | Gender and Sexualities Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 6 | International Affairs | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 7 | Latin American Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 8 | Middle East and North Africa Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |
| 9 | Peace Studies | Klingler College of Arts and Sciences | https://www.marquette.edu/academics/majors/ |

### 1.4 Pre-professional programs

| # | Program | URL |
|---|---------|-----|
| 1 | Pre-Dentistry | https://www.marquette.edu/academics/majors/ |
| 2 | Pre-Law | https://www.marquette.edu/academics/majors/ |
| 3 | Pre-Medicine | https://www.marquette.edu/academics/majors/ |

### 1.5 General/Institute-wide requirements

Marquette Core Curriculum (MCC) - Details at: https://www.marquette.edu/academics/

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### Graduate School

##### Biological Sciences
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biological Sciences | https://www.marquette.edu/grad/programs.php |

##### Chemistry
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.marquette.edu/grad/programs.php |

##### Clinical Psychology
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Psychology | https://www.marquette.edu/grad/programs.php |

##### Communication
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://www.marquette.edu/grad/programs.php |

##### Computer Science
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer and Information Science | https://www.marquette.edu/grad/programs.php |
| 2 | Computer Science (PhD) | https://www.marquette.edu/grad/programs.php |

##### Counseling and Psychology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Mental Health Counseling | https://www.marquette.edu/grad/programs.php |
| 2 | School Counseling | https://www.marquette.edu/grad/programs.php |

##### Data Science
###### MS, Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Data Science | https://www.marquette.edu/grad/programs.php |
| 2 | Data Science Certificate | https://www.marquette.edu/grad/programs.php |

##### Education
###### MEd, Certificate, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership (MEd/Certificate) | https://www.marquette.edu/grad/programs.php |
| 2 | Educational Policy and Leadership (PhD) | https://www.marquette.edu/grad/programs.php |
| 3 | Student Affairs in Higher Education (MEd) | https://www.marquette.edu/grad/programs.php |
| 4 | Teacher Education, STEM Teacher (MEd) | https://www.marquette.edu/grad/programs.php |
| 5 | Special Education Certificate | https://www.marquette.edu/grad/programs.php |
| 6 | Superintendent/School District Administrator Licensure | https://www.marquette.edu/grad/programs.php |

##### Engineering
###### MS, ME, PhD, Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering | https://www.marquette.edu/grad/programs.php |
| 2 | Civil Engineering | https://www.marquette.edu/grad/programs.php |
| 3 | Computer Engineering | https://www.marquette.edu/grad/programs.php |
| 4 | Electrical Engineering | https://www.marquette.edu/grad/programs.php |
| 5 | Environmental Engineering | https://www.marquette.edu/grad/programs.php |
| 6 | Mechanical Engineering | https://www.marquette.edu/grad/programs.php |

##### English
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English (MA) | https://www.marquette.edu/grad/programs.php |
| 2 | English (PhD) | https://www.marquette.edu/grad/programs.php |

##### Health Sciences
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Athletic Training (MAT) | https://www.marquette.edu/grad/programs.php |
| 2 | Exercise and Rehabilitation Science | https://www.marquette.edu/grad/programs.php |
| 3 | Speech Pathology (MS) | https://www.marquette.edu/grad/programs.php |

##### History
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History (MA) | https://www.marquette.edu/grad/programs.php |
| 2 | History (PhD) | https://www.marquette.edu/grad/programs.php |

##### Mathematics and Statistics
###### MS, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Statistics (MS) | https://www.marquette.edu/grad/programs.php |
| 2 | Computational Mathematical and Statistical Sciences | https://www.marquette.edu/grad/programs.php |
| 3 | Math for Secondary School Teachers (MS) | https://www.marquette.edu/grad/programs.php |

##### Neuroscience
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Neuroscience | https://www.marquette.edu/grad/programs.php |

##### Philosophy
###### MA, PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy (MA) | https://www.marquette.edu/grad/programs.php |
| 2 | Philosophy (PhD) | https://www.marquette.edu/grad/programs.php |

##### Political Science
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Political Science | https://www.marquette.edu/grad/programs.php |
| 2 | International Affairs | https://www.marquette.edu/grad/programs.php |

##### Psychology
###### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Psychology Data Analytics | https://www.marquette.edu/grad/programs.php |
| 2 | Counseling Psychology (PhD) | https://www.marquette.edu/grad/programs.php |

##### Public Service
###### MAPS
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Service | https://www.marquette.edu/grad/programs.php |

##### Religious Studies
###### PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Religious Studies | https://www.marquette.edu/grad/programs.php |

##### Theology
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Theology | https://www.marquette.edu/grad/programs.php |
| 2 | Christian Doctrine | https://www.marquette.edu/grad/programs.php |

##### Other Graduate School Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Bioinformatics | MS | https://www.marquette.edu/grad/programs.php |
| 2 | Biomedical Sciences | MS | https://www.marquette.edu/grad/programs.php |
| 3 | Criminal Justice Data Analytics | MS | https://www.marquette.edu/grad/programs.php |
| 4 | Corporate Communication | MA | https://www.marquette.edu/grad/programs.php |
| 5 | Economics | MS | https://www.marquette.edu/grad/programs.php |
| 6 | Finance | MS | https://www.marquette.edu/grad/programs.php |
| 7 | Sports and Exercise Analytics | MS | https://www.marquette.edu/grad/programs.php |
| 8 | Transfusion Medicine | MS | https://www.marquette.edu/grad/programs.php |

#### Graduate School of Management

##### MBA Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | MBA | MBA | https://www.marquette.edu/business/graduate/index.php |
| 2 | Executive MBA | MBA | https://www.marquette.edu/business/graduate/index.php |

##### Other GSM Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master in Management | MS | https://www.marquette.edu/business/graduate/index.php |
| 2 | MS Finance | MS | https://www.marquette.edu/business/graduate/index.php |
| 3 | MS Accounting | MS | https://www.marquette.edu/business/graduate/index.php |
| 4 | Accounting Analytics | MS | https://www.marquette.edu/business/graduate/index.php |

#### School of Dentistry

##### Dental Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Doctor of Dental Surgery | DDS | https://www.marquette.edu/dentistry/admissions/ |
| 2 | Dental Biomaterials | MS | https://www.marquette.edu/dentistry/admissions/ |
| 3 | Endodontics | MS/Certificate | https://www.marquette.edu/dentistry/admissions/ |
| 4 | Orthodontics | MS/Certificate | https://www.marquette.edu/dentistry/admissions/ |
| 5 | Periodontics | MS/Certificate | https://www.marquette.edu/dentistry/admissions/ |
| 6 | Prosthodontics | MS/Certificate | https://www.marquette.edu/dentistry/admissions/ |

#### College of Health Sciences (Graduate)

##### Health Sciences Professional Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Biomedical Sciences Postbaccalaureate | Certificate | https://www.marquette.edu/health-sciences/ |
| 2 | Master of Athletic Training | MAT | https://www.marquette.edu/health-sciences/ |
| 3 | Speech Pathology and Audiology Postbaccalaureate | Certificate | https://www.marquette.edu/health-sciences/ |
| 4 | Doctor of Physical Therapy | DPT | https://www.marquette.edu/health-sciences/ |
| 5 | Physician Assistant | MPAS | https://www.marquette.edu/health-sciences/ |
| 6 | Clinical Doctor of Occupational Therapy | OTD | https://www.marquette.edu/health-sciences/ |
| 7 | Medical Laboratory Science Certificate | Certificate | https://www.marquette.edu/health-sciences/ |

#### College of Nursing (Graduate)

##### Nursing Graduate Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Master of Science in Nursing | MSN | https://www.marquette.edu/nursing/ |
| 2 | Doctor of Nursing Practice | DNP | https://www.marquette.edu/nursing/ |
| 3 | Nursing PhD | PhD | https://www.marquette.edu/nursing/ |
| 4 | Direct Entry MSN (for non-nurses) | MSN | https://www.marquette.edu/nursing/ |

#### Law School

##### Law Programs
| # | 项目 | Degree | URL |
|---|------|--------|-----|
| 1 | Juris Doctor | JD | https://law.marquette.edu/prospective-students/ |

### 2.2 Graduate admissions model

Marquette's graduate admissions is **decentralized**. Each school/college manages its own admissions process:

- **Graduate School**: Centralized application at `marquette.edu/grad/apply.php`. $50 application fee. Departments make admission recommendations.
- **Graduate School of Management**: Separate application process at `marquette.edu/business/graduate/`
- **School of Dentistry**: Separate application process at `marquette.edu/dentistry/admissions/`
- **Law School**: LSAC application at `law.marquette.edu`
- **College of Health Sciences**: CASPA for PA, PTCAS for PT, OTCAS for OT
- **College of Nursing**: NursingCAS

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | https://www.marquette.edu/admissions/undergraduate/ | Official |
| Application portal | Common App or Marquette Application | https://www.marquette.edu/apply/apply.php |
| **EA deadline** | **November 15** | https://www.marquette.edu/apply/apply.php |
| **RD deadline** | **February 1** | https://www.marquette.edu/apply/apply.php |
| EA notification | Late December | https://www.marquette.edu/apply/apply.php |
| RD notification | March 1 | https://www.marquette.edu/apply/apply.php |
| Rolling after RD | Yes, space-available after Feb 1 | https://www.marquette.edu/apply/apply.php |
| Application fee | **None** ($0) | https://bulletin.marquette.edu/admission-costs/undergrad-admission/ |
| SAT/ACT policy | **Test-optional** (since Fall 2020) | https://bulletin.marquette.edu/admission-costs/undergrad-admission/ |
| Superscore | N/A (test-optional) | - |
| Score-report method | Self-reported accepted | https://www.marquette.edu/apply/apply.php |
| Interview policy | Not offered | - |
| Recommendations | Optional (not required) | https://www.marquette.edu/admissions/undergraduate/first-year-application.php |
| Portfolio | Not required | - |
| Transfer pathway | Rolling basis | https://www.marquette.edu/admissions/undergraduate/transfer.php |
| Tuition deposit | $200 (non-refundable) | https://bulletin.marquette.edu/admission-costs/undergrad-admission/ |
| Housing deposit | $300 (if desired, non-refundable) | https://bulletin.marquette.edu/admission-costs/undergrad-admission/ |

### 3.2 Undergraduate English proficiency table

**Applicability**: Required for international students whose native language is not English.

| Exam | Minimum | Recommended | Source |
|------|---------|-------------|--------|
| TOEFL iBT | Reading 18, Listening 18, Speaking 20, Writing 20 | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |
| IELTS | Reading 6.5, Listening 6.5, Speaking 6.5, Writing 6.0 | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |
| Duolingo English Test | 115 overall (no subscore below 110) | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |
| ELS Language Center | Levels 110-112 with 87% cumulative average | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |
| SAT Evidence-Based Reading | 530 | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |
| ACT English + Reading | English 22, Reading 18 | N/A | https://www.marquette.edu/oie/prospective-students/application-materials.php |

**Exemptions**:
- U.S. or Canadian university transcript showing successful in-person academic studies over at least 2 semesters
- U.S. or Canadian high school transcript showing successful in-person academic study over at least 4 semesters

### 3.3 Graduate — global rules

| Dimension | Value | Source |
|-----------|-------|--------|
| Application platform | Graduate School online application | https://www.marquette.edu/grad/apply.php |
| Application fee | $50 (non-refundable) | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| Fee waivers | Current MU undergrads, MU alumni, McNair Scholars | https://www.marquette.edu/grad/faqs.php |
| GRE institutional code | 1448 | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| GRE policy | Per-program (some required, some optional) | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| CGS April-15 | Not specified | - |
| Language test policy | TOEFL/IELTS required for non-native English speakers | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| TOEFL minimum (Grad) | 80 overall, 20 in each section | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| IELTS minimum (Grad) | 6.5 overall, 6.5 in each section | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| Application timeline | Varies by program; general deadline Aug 1 (fall), Dec 15 (spring) | https://bulletin.marquette.edu/admission-costs/grad-admission/ |
| International deadline | May 1 (fall), Oct 1 (spring) | https://bulletin.marquette.edu/admission-costs/grad-admission/ |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $53,890 | Full-time (12 or more credits) |
| Fees | $1,200 | Student services, wellness, technology |
| Housing and Food | $14,380–$18,790 | Depends on residence hall selection |
| **TOTAL ANNUAL COSTS** | **$69,470–$73,880** | On-campus |

> **Source**: https://www.marquette.edu/tuition-financial-aid/ (2026-27 rates)
> **Note**: Additional costs exist (books, personal, transportation). Visit Marquette Central for complete breakdown.

### 4.2 Undergraduate financial-aid policy

| Dimension | Value | Source |
|-----------|-------|--------|
| Need-blind/need-aware | **Need-aware for all** (domestic and international) | https://www.marquette.edu/tuition-financial-aid/scholarships-overview.php |
| International aid | Limited - only Global Scholars and scholars programs | https://www.marquette.edu/tuition-financial-aid/scholarships-overview.php |
| Merit scholarships | Yes, automatic consideration based on application | https://www.marquette.edu/tuition-financial-aid/scholarships-overview.php |
| Full-tuition scholarship | Michael R. Lovell Presidential Scholarship (additional application) | https://www.marquette.edu/tuition-financial-aid/scholarships-overview.php |
| Financial aid stats | 99% of UG students receive some form of financial aid | https://www.marquette.edu/tuition-financial-aid/ |
| Scholarship total | $170 million+ distributed annually | https://www.marquette.edu/tuition-financial-aid/ |
| FAFSA school code | 003863 | https://www.marquette.edu/central/financial-aid/ |

### 4.3 Graduate cost & funding framework

| School/Program | Tuition (2026-27) | Source |
|---------------|-------------------|--------|
| Graduate School (most programs) | $1,450/credit hour | https://www.marquette.edu/tuition-financial-aid/ |
| Graduate School of Management | $1,450/credit hour | https://www.marquette.edu/tuition-financial-aid/ |
| Education Graduate | $1,080/credit hour | https://www.marquette.edu/tuition-financial-aid/ |
| Graduate Humanities (English, History, Theology, Philosophy) | $625/credit hour | https://www.marquette.edu/tuition-financial-aid/ |
| Law School | $2,095/credit hour | https://www.marquette.edu/tuition-financial-aid/ |
| Law School (full-time) | $53,010/year | https://www.marquette.edu/tuition-financial-aid/ |
| Dentistry (in-state) | $62,890/year | https://www.marquette.edu/tuition-financial-aid/ |
| Dentistry (out-of-state) | $71,550/year | https://www.marquette.edu/tuition-financial-aid/ |
| Physician Assistant | $60,594 (28-month program) | https://www.marquette.edu/tuition-financial-aid/ |
| Doctor of Physical Therapy | $55,196 | https://www.marquette.edu/tuition-financial-aid/ |
| Clinical Doctor of Occupational Therapy | $55,196 | https://www.marquette.edu/tuition-financial-aid/ |
| Master of Athletic Training | $46,703 | https://www.marquette.edu/tuition-financial-aid/ |
| Direct Entry MSN (Fall '26 start) | $69,000 | https://www.marquette.edu/tuition-financial-aid/ |
| Nursing, Direct Entry MSN | $65,000-$69,000 (varies by start date) | https://www.marquette.edu/tuition-financial-aid/ |

**Graduate funding**:
- Merit-based assistantships and scholarships available through Graduate School
- Application deadline for merit-based aid: February 15 (fall), November 15 (spring)
- Some departments offer RA/TA positions

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 15"
  source_url: https://www.marquette.edu/apply/apply.php
  source_snippet: "Early Action Deadline – November 15"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "February 1"
  source_url: https://www.marquette.edu/apply/apply.php
  source_snippet: "Regular Decision Deadline – February 1"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.application_fee
  value: "$0 (no fee)"
  source_url: https://bulletin.marquette.edu/admission-costs/undergrad-admission/
  source_snippet: "There is no application fee for undergraduate applicants."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: https://bulletin.marquette.edu/admission-costs/undergrad-admission/
  source_snippet: "Effective beginning with the Fall 2020 entry term, applicants are not required to submit results of the SAT or ACT entrance examination to receive consideration for admission to Marquette University."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.costs.tuition_2026_2027
  value: "$53,890"
  source_url: https://www.marquette.edu/tuition-financial-aid/
  source_snippet: "Full-time Tuition (12 or more credits) $53,890"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.costs.total_2026_2027
  value: "$69,470–$73,880"
  source_url: https://www.marquette.edu/tuition-financial-aid/
  source_snippet: "TOTAL ANNUAL COSTS $69,470–$73,880"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.english_proficiency.TOEFL
  value: "Reading 18, Listening 18, Speaking 20, Writing 20"
  source_url: https://www.marquette.edu/oie/prospective-students/application-materials.php
  source_snippet: "TOEFL scores of at least – Reading: 18, Listening: 18, Speaking: 20, Writing: 20"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english_proficiency.IELTS
  value: "Reading 6.5, Listening 6.5, Speaking 6.5, Writing 6.0"
  source_url: https://www.marquette.edu/oie/prospective-students/application-materials.php
  source_snippet: "IELTS scores of at least – Reading: 6.5, Listening: 6.5, Speaking: 6.5, Writing: 6.0"
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.english_proficiency.Duolingo
  value: "115 overall, no subscore below 110"
  source_url: https://www.marquette.edu/oie/prospective-students/application-materials.php
  source_snippet: "Duolingo English Test: Overall score of 115. Prefer no subscore lower than 110."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.financial_aid.need_policy
  value: "Need-aware for all (domestic and international)"
  source_url: https://www.marquette.edu/tuition-financial-aid/scholarships-overview.php
  source_snippet: "International students are not eligible for scholarships outside of Global Scholars and our scholars programs listed below."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$50"
  source_url: https://bulletin.marquette.edu/admission-costs/grad-admission/
  source_snippet: "A non-refundable application fee (U.S. currency only) of $50.00."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-002:
  field: graduate.english_proficiency.TOEFL
  value: "80 overall, 20 in each section"
  source_url: https://bulletin.marquette.edu/admission-costs/grad-admission/
  source_snippet: "TOEFL: The Internet-based, or iBT, version of TOEFL tests students in four areas: reading, writing, speaking and listening. In general, a minimum score of 20 is required for each of the four sections, with an overall minimum score of 80."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency.IELTS
  value: "6.5 overall, 6.5 in each section"
  source_url: https://bulletin.marquette.edu/admission-costs/grad-admission/
  source_snippet: "IELTS: Total overall score of 6.5 or higher is required, with no less than 6.5 in each of the four sections."
  capture_date: 2026-07-07
  evidence_type: official_webpage

E-G-004:
  field: graduate.tuition.general
  value: "$1,450/credit hour"
  source_url: https://www.marquette.edu/tuition-financial-aid/
  source_snippet: "Graduate School Tuition $1,450 (per credit hour)"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-005:
  field: graduate.tuition.law
  value: "$2,095/credit hour"
  source_url: https://www.marquette.edu/tuition-financial-aid/
  source_snippet: "Law School $2,095"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table

E-G-006:
  field: graduate.tuition.dentistry_in_state
  value: "$62,890/year"
  source_url: https://www.marquette.edu/tuition-financial-aid/
  source_snippet: "In state $31,445/Term $62,890/Year"
  capture_date: 2026-07-07
  evidence_type: official_webpage_table
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
marquette-knowledge-base-v2/
├── overview/
│   ├── institution-overview (Section 0)
│   └── colleges-schools-hierarchy
├── undergraduate/
│   ├── arts-sciences-programs
│   ├── business-administration-programs
│   ├── communication-programs
│   ├── education-programs
│   ├── engineering-programs
│   ├── health-sciences-programs
│   └── nursing-programs
├── graduate/
│   ├── graduate-school-programs
│   ├── graduate-school-management-programs
│   ├── dentistry-programs
│   ├── health-sciences-grad-programs
│   ├── nursing-grad-programs
│   └── law-school-programs
├── admissions/
│   ├── undergraduate-deadlines-requirements
│   ├── english-proficiency-requirements
│   └── graduate-admissions
├── costs/
│   ├── undergraduate-costs
│   ├── graduate-costs
│   └── financial-aid
└── evidence/
    └── evidence-chain-index
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "marquette-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
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
|----------|-----------|------------|
| P0 | Exact count of UG minors | https://www.marquette.edu/academics/majors/ (need minor enumeration) |
| P0 | Per-program GRE requirements | Individual program pages |
| P1 | Graduate program application deadlines (per program) | Individual program pages |
| P1 | UG program-specific requirements (portfolios, auditions) | Individual college pages |
| P1 | Net price calculator results | https://www.marquette.edu/central/financial-aid/ |
| P2 | Detailed COA breakdown (books, transportation, personal) | https://www.marquette.edu/central/bursar/ |
| P2 | Graduate stipend rates | Individual department pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | Marquette | [Other School] | [Other School] |
|-----------|-----------|----------------|----------------|
| Location | Milwaukee, WI | | |
| Type | Private Jesuit | | |
| UG Tuition (2026-27) | $53,890 | | |
| Total UG COA | $69,470–$73,880 | | |
| EA deadline | November 15 | | |
| RD deadline | February 1 | | |
| ED deadline | N/A | | |
| Test policy | Test-optional | | |
| Application fee (UG) | $0 | | |
| TOEFL minimum (UG) | R18/L18/S20/W20 | | |
| IELTS minimum (UG) | R6.5/L6.5/S6.5/W6.0 | | |
| Need-blind (intl)? | No (need-aware for all) | | |
| Total programs | 161+ | | |
| Schools/colleges | 11 | | |
| Grad application fee | $50 | | |
| TOEFL minimum (Grad) | 80 overall, 20 each | | |
| IELTS minimum (Grad) | 6.5 overall, 6.5 each | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-07
> **Sources**: marquette.edu, bulletin.marquette.edu, law.marquette.edu, admissions.marquette.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program

---

## Cache metadata

### site-memory.json

```json
{
  "schema_version": "1.0",
  "university": "Marquette University",
  "slug": "marquette",
  "region": "us",
  "platform": "static-html",
  "first_run": "2026-07-07",
  "last_run": "2026-07-07",
  "domains": {
    "ug_admissions": "www.marquette.edu/admissions/",
    "grad_admissions": "www.marquette.edu/grad/",
    "finances": "www.marquette.edu/tuition-financial-aid/",
    "catalog_ug": "www.marquette.edu/academics/majors/",
    "catalog_grad": "www.marquette.edu/grad/programs.php",
    "bulletin": "bulletin.marquette.edu"
  },
  "source_urls": {
    "ug_deadlines": "https://www.marquette.edu/apply/apply.php",
    "ug_test_policy": "https://bulletin.marquette.edu/admission-costs/undergrad-admission/",
    "ug_intl_requirements": "https://www.marquette.edu/oie/prospective-students/application-materials.php",
    "ug_coa": "https://www.marquette.edu/tuition-financial-aid/",
    "grad_hub": "https://www.marquette.edu/grad/programs.php",
    "grad_admission_details": "https://bulletin.marquette.edu/admission-costs/grad-admission/"
  },
  "selectors": {
    "program_list": "main .program-card, main [class*='major']",
    "tab_panel": "[role='tabpanel']",
    "accordion": ".CollapsiblePanel"
  },
  "pagination": {
    "type": "none",
    "notes": "All programs listed on single pages"
  },
  "decoders": {
    "degree_naming": "standard",
    "naming_quirks": []
  },
  "known_404s": [],
  "session_gotchas": [
    "Tab switching on tuition page doesn't work via click - must use JS to get all tab panel content",
    "International page accordions require JS expansion"
  ],
  "degree_naming": "standard",
  "notes": "Private Jesuit; need-aware for all; test-optional; no UG application fee; 11 colleges/schools"
}
```

### content-hashes.json

```json
{
  "schema_version": "1.0",
  "last_full_check": "2026-07-07",
  "watched_pages": [
    {
      "url": "https://www.marquette.edu/apply/apply.php",
      "field": "ug.deadlines",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-07",
      "normalized_selector": "[role='tabpanel']",
      "last_value": "EA: Nov 15, RD: Feb 1",
      "change_status": "baseline"
    },
    {
      "url": "https://www.marquette.edu/tuition-financial-aid/",
      "field": "ug.costs.tuition",
      "frequency": "high",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-07",
      "normalized_selector": "[role='tabpanel']",
      "last_value": "$53,890",
      "change_status": "baseline"
    },
    {
      "url": "https://www.marquette.edu/oie/prospective-students/application-materials.php",
      "field": "ug.english_proficiency",
      "frequency": "medium",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-07",
      "normalized_selector": "main",
      "last_value": "TOEFL R18/L18/S20/W20",
      "change_status": "baseline"
    },
    {
      "url": "https://www.marquette.edu/academics/majors/",
      "field": "ug.programs",
      "frequency": "medium",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-07",
      "normalized_selector": "main",
      "last_value": "71 majors",
      "change_status": "baseline"
    },
    {
      "url": "https://www.marquette.edu/grad/programs.php",
      "field": "grad.programs",
      "frequency": "medium",
      "hash_algo": "sha256",
      "hash": "baseline",
      "last_verified": "2026-07-07",
      "normalized_selector": "main",
      "last_value": "90+ programs",
      "change_status": "baseline"
    }
  ]
}
```

### last-extract.json

```json
{
  "schema_version": "1.0",
  "capture_date": "2026-07-07",
  "rule1": {
    "ug_majors": 71,
    "ug_minors": null,
    "grad_degrees": 90,
    "total": 161
  },
  "hierarchy": [
    {"school": "Klingler College of Arts and Sciences", "departments": ["Africana Studies", "Anthropology", "Biological Sciences", "Chemistry", "Classics", "Computer Science", "Economics", "English", "French", "German", "History", "Mathematics", "Philosophy", "Physics", "Political Science", "Psychology", "Social and Cultural Sciences", "Theology"]},
    {"school": "College of Business Administration", "departments": ["Accounting", "Business Administration", "Finance", "Management", "Marketing", "Information Systems"]},
    {"school": "Diederich College of Communication", "departments": ["Communication and Media", "Journalism", "Advertising and Public Relations"]},
    {"school": "College of Education", "departments": ["Education"]},
    {"school": "Opus College of Engineering", "departments": ["Biomedical Engineering", "Civil/Construction/Environmental Engineering", "Electrical and Computer Engineering", "Mechanical Engineering"]},
    {"school": "College of Health Sciences", "departments": ["Health Sciences", "Athletic Training", "Occupational Therapy", "Physical Therapy", "Physician Assistant"]},
    {"school": "College of Nursing", "departments": ["Nursing"]},
    {"school": "Graduate School", "departments": ["Biological Sciences", "Chemistry", "Clinical Psychology", "Communication", "Computer Science", "Counseling", "Data Science", "Education", "Engineering", "English", "History", "Mathematics", "Neuroscience", "Philosophy", "Political Science", "Psychology", "Religious Studies", "Theology"]},
    {"school": "Graduate School of Management", "departments": ["MBA", "Finance", "Accounting", "Management"]},
    {"school": "School of Dentistry", "departments": ["DDS", "Dental Biomaterials", "Endodontics", "Orthodontics", "Periodontics", "Prosthodontics"]},
    {"school": "Law School", "departments": ["JD"]}
  ],
  "degree_inventory": [
    {"abbr": "BA", "official_abbr": "BA", "canonical": "BA", "level": "undergraduate", "count": 30},
    {"abbr": "BS", "official_abbr": "BS", "canonical": "BS", "level": "undergraduate", "count": 35},
    {"abbr": "BSN", "official_abbr": "BSN", "canonical": "BSN", "level": "undergraduate", "count": 1},
    {"abbr": "MA", "official_abbr": "MA", "canonical": "MA", "level": "graduate", "count": 10},
    {"abbr": "MS", "official_abbr": "MS", "canonical": "MS", "level": "graduate", "count": 25},
    {"abbr": "MBA", "official_abbr": "MBA", "canonical": "MBA", "level": "graduate", "count": 2},
    {"abbr": "MEd", "official_abbr": "MEd", "canonical": "MEd", "level": "graduate", "count": 5},
    {"abbr": "MEng", "official_abbr": "ME", "canonical": "MEng", "level": "graduate", "count": 3},
    {"abbr": "PhD", "official_abbr": "PhD", "canonical": "PhD", "level": "graduate", "count": 15},
    {"abbr": "EdD", "official_abbr": "EdD", "canonical": "EdD", "level": "graduate", "count": 1},
    {"abbr": "DNP", "official_abbr": "DNP", "canonical": "DNP", "level": "graduate", "count": 1},
    {"abbr": "DPT", "official_abbr": "DPT", "canonical": "DPT", "level": "graduate", "count": 1},
    {"abbr": "OTD", "official_abbr": "OTD", "canonical": "OTD", "level": "graduate", "count": 1},
    {"abbr": "JD", "official_abbr": "JD", "canonical": "JD", "level": "graduate", "count": 1},
    {"abbr": "DDS", "official_abbr": "DDS", "canonical": "DDS", "level": "graduate", "count": 1},
    {"abbr": "Certificate", "official_abbr": "Certificate", "canonical": "Certificate", "level": "graduate", "count": 10}
  ],
  "distribution_matrix": {
    "rows": [
      {"school": "Klingler College of Arts and Sciences", "cells": {"BA": 25, "BS": 5, "MA": 5, "MS": 3, "PhD": 8, "Certificate": 2}},
      {"school": "College of Business Administration", "cells": {"BS": 10, "MS": 3, "MBA": 2, "Certificate": 1}},
      {"school": "Diederich College of Communication", "cells": {"BS": 6, "MA": 2}},
      {"school": "College of Education", "cells": {"BS": 2, "MEd": 4, "EdD": 1, "Certificate": 2}},
      {"school": "Opus College of Engineering", "cells": {"BS": 7, "MS": 3, "MEng": 3, "PhD": 3, "Certificate": 2}},
      {"school": "College of Health Sciences", "cells": {"BS": 4, "MS": 3, "PhD": 2, "DPT": 1, "OTD": 1, "Certificate": 3}},
      {"school": "College of Nursing", "cells": {"BSN": 1, "MS": 2, "PhD": 1, "DNP": 1, "Certificate": 2}},
      {"school": "Graduate School", "cells": {"MA": 3, "MS": 5, "MEd": 2, "PhD": 5, "Certificate": 3}},
      {"school": "Graduate School of Management", "cells": {"MS": 3, "MBA": 2}},
      {"school": "School of Dentistry", "cells": {"MS": 4, "DDS": 1, "Certificate": 5}},
      {"school": "Law School", "cells": {"JD": 1}}
    ]
  },
  "deadlines": {
    "ug": {"EA": "November 15", "RD": "February 1", "ED": null},
    "grad_fees": {"app_fee_usd": 50}
  },
  "costs": {
    "ug_coa_lineitems": [
      {"item": "Tuition", "amount_usd": 53890, "ay": "2026-27"},
      {"item": "Fees", "amount_usd": 1200, "ay": "2026-27"},
      {"item": "Housing and Food", "amount_usd_range": [14380, 18790], "ay": "2026-27"}
    ],
    "need_blind_intl": false,
    "need_blind_domestic": false,
    "tuition_free_threshold_usd": null
  },
  "evidence_refs": ["E-U-001", "E-U-002", "E-U-003", "E-U-004", "E-U-005", "E-U-006", "E-U-007", "E-U-008", "E-U-009", "E-U-010", "E-G-001", "E-G-002", "E-G-003", "E-G-004", "E-G-005", "E-G-006"]
}
```
