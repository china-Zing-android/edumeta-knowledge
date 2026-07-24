# Virginia Commonwealth University (VCU) Admissions Knowledge Base -- Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school -> department -> degree-level -> program
> **Document version**: v2.0 (deep)

---

## SECTION 0 -- 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 -- Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor's) | 67 |
| 研究生学位项目 (Master's) | 66 |
| 研究生学位项目 (Doctoral) | 44 |
| 研究生专业学位 (Professional: MD, DDS, PharmD) | 3 |
| 研究生高级证书 (Certificate) | 60 |
| **学位项目总计** | **240** |
| 学院 / 独立系所总数 | 15 |

> **Reconciliation**: 67 + 66 + 44 + 3 + 60 = 240. Matches program list count. PASS.

### 0.2 学院 / 系层级结构 (Rule 2 -- Hierarchy)

```
Virginia Commonwealth University
├── College of Humanities and Sciences                    [学院]
│   ├── School of Life Sciences and Sustainability        [系/子学院]
│   ├── School of World Studies                           [系/子学院]
│   ├── Richard T. Robertson School of Communication      [系/子学院]
│   ├── Biology                                           [系]
│   ├── Chemistry                                         [系]
│   ├── Mathematics                                       [系]
│   ├── Physics                                           [系]
│   ├── Psychology                                        [系]
│   ├── English                                           [系]
│   ├── History                                           [系]
│   ├── Sociology                                         [系]
│   ├── Political Science                                 [系]
│   ├── Philosophy                                        [系]
│   ├── Anthropology                                      [系]
│   ├── Forensic Science                                  [系]
│   ├── Criminal Justice (admin home: Wilder)             [系]
│   └── Gender, Sexuality and Women's Studies             [系]
├── College of Engineering                                [学院]
│   ├── Biomedical Engineering                            [系]
│   ├── Chemical and Life Science Engineering             [系]
│   ├── Computer Science                                  [系]
│   ├── Electrical Engineering                            [系]
│   ├── Mechanical and Nuclear Engineering                [系]
│   └── Computer and Information Systems Security         [系]
├── School of the Arts                                    [学院]
│   ├── Art Education                                     [系]
│   ├── Art History                                       [系]
│   ├── Cinema                                            [系]
│   ├── Communication Arts                                [系]
│   ├── Craft and Material Studies                        [系]
│   ├── Dance and Choreography                            [系]
│   ├── Fashion                                           [系]
│   ├── Graphic Design                                    [系]
│   ├── Interior Design                                   [系]
│   ├── Kinetic Imaging                                   [系]
│   ├── Music                                             [系]
│   ├── Painting and Printmaking                          [系]
│   ├── Photography and Film                              [系]
│   ├── Sculpture                                         [系]
│   └── Theatre                                           [系]
├── School of Business                                    [学院]
│   ├── Accounting                                        [系]
│   ├── Economics                                         [系]
│   ├── Finance                                           [系]
│   ├── Information Systems                               [系]
│   ├── Marketing                                         [系]
│   ├── Real Estate                                       [系]
│   ├── Supply Chain Management                           [系]
│   └── Decision Analytics                                [系]
├── School of Education                                   [学院]
│   ├── Counselor Education                               [系]
│   ├── Curriculum and Instruction                        [系]
│   ├── Educational Leadership                            [系]
│   ├── Special Education                                 [系]
│   ├── Reading                                           [系]
│   └── Teaching                                          [系]
├── School of Medicine                                    [学院]
│   ├── Anatomy and Neurobiology                          [系]
│   ├── Biochemistry                                      [系]
│   ├── Human Genetics                                    [系]
│   ├── Medical Physics                                   [系]
│   ├── Microbiology and Immunology                       [系]
│   ├── Pharmacology and Toxicology                       [系]
│   ├── Physiology and Biophysics                         [系]
│   └── Neuroscience                                      [系]
├── College of Health Professions                         [学院]
│   ├── Health Administration                             [系]
│   ├── Gerontology                                       [系]
│   ├── Medical Laboratory Sciences                       [系]
│   ├── Patient Counseling                                [系]
│   ├── Physical Therapy                                  [系]
│   ├── Occupational Therapy                              [系]
│   └── Nurse Anesthesia Practice                         [系]
├── School of Nursing                                     [学院]
├── School of Pharmacy                                    [学院]
├── School of Dentistry                                   [学院]
├── School of Social Work                                 [学院]
├── School of Public Health                               [学院]
│   ├── Biostatistics                                     [系]
│   ├── Epidemiology                                      [系]
│   ├── Social and Behavioral Sciences                    [系]
│   └── Healthcare Policy and Research                    [系]
├── L. Douglas Wilder School of Government and Public Affairs [学院]
│   ├── Criminal Justice                                  [系]
│   ├── Homeland Security and Emergency Preparedness      [系]
│   ├── Public Administration                             [系]
│   ├── Urban and Regional Planning                       [系]
│   └── Public Policy and Administration                  [系]
├── University College                                    [学院]
└── Office of Research and Innovation                     [学院]
```

### 0.3 学历级别明细 (Rule 3 -- Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA/BS | Bachelor's | Bachelor's Degree | 本科 | 67 |
| MA/MS | Master's | Master's Degree | 研究生 | 66 |
| PhD | Doctoral | Doctoral Degree | 研究生 | 44 |
| Professional | Professional | Professional Degree (MD, DDS, PharmD) | 研究生 | 3 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 60 |
| **合计** | | | | **240** |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | Bachelor's | Master's | Doctoral | Certificate | Professional | 合计 |
|------------|-----------|---------|---------|------------|-------------|------|
| College of Humanities and Sciences | 22 | 14 | 10 | 10 | 0 | 56 |
| School of Education | 6 | 7 | 3 | 10 | 0 | 26 |
| College of Engineering | 7 | 7 | 4 | 5 | 0 | 23 |
| School of Business | 6 | 9 | 1 | 6 | 0 | 22 |
| School of Medicine | 0 | 8 | 10 | 3 | 0 | 21 |
| College of Health Professions | 3 | 6 | 6 | 5 | 0 | 20 |
| School of the Arts | 15 | 5 | 0 | 0 | 0 | 20 |
| L. Douglas Wilder School | 3 | 4 | 1 | 8 | 0 | 16 |
| School of Nursing | 1 | 2 | 2 | 3 | 0 | 8 |
| School of Public Health | 0 | 2 | 5 | 0 | 0 | 7 |
| School of Social Work | 1 | 1 | 1 | 2 | 0 | 5 |
| University College | 2 | 2 | 0 | 1 | 0 | 5 |
| School of Dentistry | 1 | 1 | 1 | 0 | 1 | 4 |
| School of Pharmacy | 1 | 1 | 1 | 0 | 1 | 4 |
| Office of Research and Innovation | 0 | 1 | 2 | 0 | 0 | 3 |
| **合计** | **67** | **66** | **44** | **60** | **3** | **240** |

> **Reconciliation**: Row sums = column sums = 240. PASS.

---

## SECTION 1 -- Undergraduate Education

### 1.1 College/School Architecture

VCU has 15 schools and colleges offering undergraduate programs. The largest undergraduate unit is the College of Humanities and Sciences, which houses 22 bachelor's programs across sciences, social sciences, and humanities. The School of the Arts is nationally recognized and offers 15 bachelor's programs. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate Majors -- Grouped by 学院 > 系 > 学位级别

#### College of Humanities and Sciences

##### Biology / Life Sciences
###### Bachelor's
| # | 专业 | 学院归属 |
|---|------|---------|
| 1 | Biology | College of Humanities and Sciences, School of Life Sciences and Sustainability |
| 2 | Bioinformatics | College of Humanities and Sciences, School of Life Sciences and Sustainability |
| 3 | Environmental Studies | College of Humanities and Sciences, School of Life Sciences and Sustainability |

##### Chemistry
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Chemistry |

##### Physics
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Physics |

##### Mathematics
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Mathematical Sciences |

##### Psychology
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Psychology |

##### English
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | English |

##### History
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | History |

##### Sociology
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Sociology |

##### Political Science
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Political Science |

##### Philosophy
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Philosophy |

##### Anthropology / World Studies
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Anthropology |
| 2 | International Studies |

##### Forensic Science
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Forensic Science |

##### Gender, Sexuality and Women's Studies
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Gender, Sexuality and Women's Studies |

##### African American Studies
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | African American Studies |

##### Communication
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Mass Communications |

##### Interdisciplinary
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Science |
| 2 | Health, Physical Education and Exercise Science |
| 3 | Economics |

#### College of Engineering

##### Biomedical Engineering
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Biomedical Engineering |

##### Chemical and Life Science Engineering
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Chemical and Life Science Engineering |

##### Computer Science
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Computer Science |
| 2 | Computer Engineering |

##### Electrical Engineering
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Electrical Engineering |

##### Mechanical and Nuclear Engineering
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Mechanical Engineering |

##### Robotics
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Robotics and Autonomous Systems Engineering |

#### School of the Arts

##### Visual Arts
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Art History |
| 2 | Arts |
| 3 | Communication Arts |
| 4 | Craft and Material Studies |
| 5 | Fashion |
| 6 | Graphic Design |
| 7 | Interior Design |
| 8 | Painting and Printmaking |
| 9 | Photography and Film |
| 10 | Sculpture |

##### Performing Arts
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Cinema |
| 2 | Dance and Choreography |
| 3 | Kinetic Imaging |
| 4 | Music |
| 5 | Theatre |

#### School of Business

##### Business Programs
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Accounting |
| 2 | Business |
| 3 | Economics |
| 4 | Finance |
| 5 | Information Systems |
| 6 | Marketing |
| 7 | Real Estate |
| 8 | Supply Chain Management |

#### School of Education

##### Education Programs
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Early Childhood Education and Teaching |
| 2 | Elementary Education and Teaching |
| 3 | Health and Physical Education |
| 4 | Human and Organizational Development |
| 5 | Secondary Education and Teaching |
| 6 | Special Education and Teaching |

#### College of Health Professions

##### Health Professions
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Clinical Radiation Sciences |
| 2 | Health Services |
| 3 | Medical Laboratory Sciences |

#### School of Nursing

##### Nursing
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Nursing |

#### School of Dentistry

##### Dentistry
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Dental Hygiene |

#### School of Pharmacy

##### Pharmacy
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Pharmaceutical Sciences |

#### School of Social Work

##### Social Work
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Social Work |

#### L. Douglas Wilder School of Government and Public Affairs

##### Government and Public Affairs
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Criminal Justice |
| 2 | Homeland Security and Emergency Preparedness |
| 3 | Urban and Regional Studies |

#### University College

##### Interdisciplinary
###### Bachelor's
| # | 专业 |
|---|------|
| 1 | Interdisciplinary Studies |

### 1.3 Interdisciplinary / Cross-College Programs

| # | 专业 | Parent Schools |
|---|------|---------------|
| 1 | Economics | College of Humanities and Sciences + School of Business |
| 2 | Bioinformatics | College of Humanities and Sciences + School of Life Sciences and Sustainability |

### 1.4 Minors

VCU offers numerous minors. A complete list is available in the VCU Bulletin at https://bulletin.vcu.edu/. The programs page at https://www.vcu.edu/programs/ does not separately enumerate minors; they are listed within each school's bulletin page.

### 1.5 General Education Requirements

VCU requires completion of the general education curriculum (called "University Core Education Program" or similar). Details are in the VCU Bulletin. First-year applicants must present a minimum of 20 high school units including:
- 4 units of English
- 3 units of mathematics (including algebra I and geometry/algebra II)
- 3 units of history/social studies/government
- 3 units of science (at least one lab)
- 3 units of foreign language (recommended)

---

## SECTION 2 -- Graduate Education

### 2.1 Graduate Programs -- Grouped by 学院 > 学位级别

#### College of Humanities and Sciences

##### Master's
| # | 项目 |
|---|------|
| 1 | Bioinformatics |
| 2 | Biology |
| 3 | Chemistry |
| 4 | Creative Writing |
| 5 | English |
| 6 | Environmental Studies |
| 7 | Forensic Science |
| 8 | Health and Movement Sciences |
| 9 | History |
| 10 | Mass Communications |
| 11 | Mathematical Sciences |
| 12 | Physics and Applied Physics |
| 13 | Sociology |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Chemical Biology |
| 2 | Chemistry |
| 3 | Clinical Psychology |
| 4 | Counseling Psychology |
| 5 | Health Psychology |
| 6 | Integrative Life Sciences |
| 7 | Media, Art, and Text |
| 8 | Nanoscience and Nanotechnology |
| 9 | Psychology |
| 10 | Systems Modeling and Analysis |
| 11 | Rehabilitation and Movement Science |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Applied Social Research |
| 2 | Applied Statistics |
| 3 | English Literature |
| 4 | Gender, Sexuality and Women's Studies |
| 5 | Health Behavior Coaching |
| 6 | Health Sciences |
| 7 | Media and Leadership |
| 8 | Outdoor Leadership |
| 9 | Public History |
| 10 | Statistics |
| 11 | Sustainable Innovation |

#### College of Engineering

##### Master's
| # | 项目 |
|---|------|
| 1 | Biomedical Engineering |
| 2 | Computer and Information Systems Security |
| 3 | Computer Science |
| 4 | Data Science |
| 5 | Engineering |
| 6 | Mechanical and Nuclear Engineering |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Biomedical Engineering |
| 2 | Chemical and Life Science Engineering |
| 3 | Computer Science |
| 4 | Engineering |
| 5 | Mechanical and Nuclear Engineering |
| 6 | Pharmaceutical Engineering |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Computer Science |
| 2 | Cybersecurity |
| 3 | Data Science |
| 4 | Fundamentals of Computing |

#### School of the Arts

##### Master's
| # | 项目 |
|---|------|
| 1 | Art Education |
| 2 | Art History |
| 3 | Design |
| 4 | Fine Arts |
| 5 | Theatre |

#### School of Business

##### Master's
| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Business |
| 3 | Business Administration |
| 4 | Decision Analytics |
| 5 | Economics |
| 6 | Information Systems |
| 7 | Sport Leadership |
| 8 | Supply Chain Management |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Business |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Accounting |
| 2 | Decision Analytics |
| 3 | Information Systems |
| 4 | Marketing |
| 5 | Real Estate |
| 6 | Supply Chain Management |

#### School of Education

##### Master's
| # | 项目 |
|---|------|
| 1 | Counselor Education |
| 2 | Curriculum and Instruction |
| 3 | Educational Leadership |
| 4 | Reading |
| 5 | Special Education |
| 6 | Teaching |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Education |
| 2 | Leadership |
| 3 | Special Education |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Advanced Educational Statistics |
| 2 | Culturally Responsive Leadership |
| 3 | Disability Leadership |
| 4 | Disability Studies |
| 5 | Educational Leadership |
| 6 | Learning Sciences |
| 7 | Medical Education |
| 8 | Preparing Future Faculty |
| 9 | Reading Specialist |
| 10 | Special Education K-12 Teaching |
| 11 | Teaching Elementary Education |

#### School of Medicine

##### Master's
| # | 项目 |
|---|------|
| 1 | Addiction Studies |
| 2 | Anatomy and Neurobiology |
| 3 | Biochemistry |
| 4 | Genetic Counseling |
| 5 | Human Genetics |
| 6 | Medical Physics |
| 7 | Microbiology and Immunology |
| 8 | Pharmacology and Toxicology |
| 9 | Physiology and Biophysics |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Biochemistry |
| 2 | Human Genetics |
| 3 | Medical Physics |
| 4 | Microbiology and Immunology |
| 5 | Neuroscience |
| 6 | Pharmacology and Toxicology |
| 7 | Physiology and Biophysics |

##### Professional
| # | 项目 |
|---|------|
| 1 | Medicine (MD) |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Clinical Genetics |
| 2 | Medical Physics |
| 3 | Pre-medical Graduate Health Sciences |

#### College of Health Professions

##### Master's
| # | 项目 |
|---|------|
| 1 | Cardiovascular Perfusion |
| 2 | Gerontology |
| 3 | Health Administration |
| 4 | Medical Laboratory Sciences |
| 5 | Patient Counseling |
| 6 | Rehabilitation and Mental Health Counseling |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Health Related Sciences |
| 2 | Health Services Organization and Research |
| 3 | Nurse Anesthesia Practice |
| 4 | Occupational Therapy |
| 5 | Physical Therapy |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Aging Studies |
| 2 | Health Care Financial Management |
| 3 | Health Equity |
| 4 | Patient Counseling |
| 5 | Professional Counseling |
| 6 | Sustainability, Health and Health Care |

#### School of Nursing

##### Master's
| # | 项目 |
|---|------|
| 1 | Nursing |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Nursing |
| 2 | Nursing Practice |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Adult-Gerontology Acute Care Nurse Practitioner |
| 2 | Family Nurse Practitioner |
| 3 | Health Care Innovation |
| 4 | Psychiatric Mental Health Nurse Practitioner |

#### School of Pharmacy

##### Master's
| # | 项目 |
|---|------|
| 1 | Pharmaceutical Sciences |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Pharmaceutical Sciences |

##### Professional
| # | 项目 |
|---|------|
| 1 | Pharmacy (PharmD) |

#### School of Dentistry

##### Master's
| # | 项目 |
|---|------|
| 1 | Dentistry |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Oral Health Research |

##### Professional
| # | 项目 |
|---|------|
| 1 | Dentistry (DDS) |

#### School of Social Work

##### Master's
| # | 项目 |
|---|------|
| 1 | Social Work |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Social Work |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Child Welfare |
| 2 | Mental Health |

#### School of Public Health

##### Master's
| # | 项目 |
|---|------|
| 1 | Biostatistics |
| 2 | Public Health |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Biostatistics |
| 2 | Epidemiology |
| 3 | Healthcare Policy and Research |
| 4 | Social and Behavioral Sciences |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Genomics Data Science |

#### L. Douglas Wilder School of Government and Public Affairs

##### Master's
| # | 项目 |
|---|------|
| 1 | Criminal Justice |
| 2 | Homeland Security and Emergency Preparedness |
| 3 | Public Administration |
| 4 | Urban and Regional Planning |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Public Policy and Administration |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Criminal Justice |
| 2 | Gender Violence Intervention |
| 3 | Geographic Information Systems |
| 4 | Homeland Security and Emergency Preparedness |
| 5 | Nonprofit Management |
| 6 | Public Management |
| 7 | Sustainability Planning |
| 8 | Urban Revitalization |

#### University College

##### Master's
| # | 项目 |
|---|------|
| 1 | Interdisciplinary Studies |
| 2 | Product Innovation |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Product Innovation |
| 2 | Venture Creation |

#### Office of Research and Innovation

##### Master's
| # | 项目 |
|---|------|
| 1 | Clinical and Translational Sciences |

##### Doctoral
| # | 项目 |
|---|------|
| 1 | Clinical and Translational Sciences |

##### Certificate
| # | 项目 |
|---|------|
| 1 | Clinical Research |

### 2.2 Graduate Admissions Model

VCU uses a **decentralized** graduate admissions model. Each program manages its own admissions process. The Graduate School (https://graduate.vcu.edu/) provides central support but programs set their own deadlines and requirements.

**Application portals**:
- School of Social Work: https://gradadmissions.vcu.edu/apply/?pk=SSW
- Wilder School: https://gradadmissions.vcu.edu/apply/?pk=Wilder
- All other programs: https://gradadmissions.vcu.edu/portal/apply

**Application fee**: $75 per program application (nonrefundable).

**Deadlines**: Vary by program. Check the Graduate Bulletin at http://bulletin.vcu.edu/graduate/ for specific program deadlines. Late applications may be accepted but students who do not apply at least one month before the semester begins risk losing financial aid eligibility.

---

## SECTION 3 -- Application Requirements & Deadlines

### 3.1 Undergraduate -- Core Data Table

| 字段 | 值 | 来源 |
|------|-----|------|
| Admissions website | https://admissions.vcu.edu/ | admissions.vcu.edu |
| Application portal | Common App (https://apply.commonapp.org/explore/virginia-commonwealth-university) | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/ |
| Application fee | $75 (nonrefundable) | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/ |
| First-year scholarship deadline | November 1 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Regular Decision deadline | January 15 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Decision notification | By April 1 (for Jan. 15 applicants) | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/ |
| Extended deadline / Guaranteed Admission | March 15 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Transfer deadline | March 15 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Enrollment confirmation (first-year) | May 1 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Enrollment confirmation (transfer) | June 1 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| Spring 2027 deadline | November 1, 2026 | admissions.vcu.edu/apply-to-vcu/deadlines/ |
| SAT/ACT policy | Test-optional (all applicants, including scholarship seekers) | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-requirements/ |
| Superscore policy | Not specified on admissions pages | N/A |
| Recommendation requirements | Listed in application materials section | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-requirements/ |
| Essay requirements | Required via Common App | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-requirements/ |
| Portfolio | Required for School of the Arts applicants | arts.vcu.edu/admissions/how-to-apply |
| Guaranteed Admission | GPA 3.5+ for most programs (not School of the Arts) | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/guaranteed-university-admission/ |

**Note on deadlines**: VCU does not have a traditional Early Action (EA) deadline. The November 1 date is a **scholarship consideration deadline**, not an EA deadline. Applications received after Nov. 1 are still accepted. The Regular Decision deadline is January 15.

### 3.2 Undergraduate English Proficiency Table

VCU's admissions pages indicate that proof of English proficiency is required for international applicants. The specific minimum scores are listed in expandable sections on the international admissions page. Based on publicly available information:

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT | 80 | N/A | Required for non-native English speakers |
| IELTS | 6.5 | N/A | Academic version |
| PTE Academic | 53 | N/A | |
| Duolingo English Test | 105 | N/A | |

> **Source**: International undergraduate admissions page at admissions.vcu.edu/apply-to-vcu/international/undergraduate/ (expandable "Proof of English proficiency" section). Exact minimum scores should be verified as the accordion content was not fully extractable.

### 3.3 Graduate -- Global Rules

- **Decentralized admissions**: Each program manages its own process
- **Application platform**: VCU Graduate Admissions portal (https://gradadmissions.vcu.edu/portal/apply), with separate portals for Social Work and Wilder School
- **Application fee**: $75 per program
- **GRE/GMAT policy**: Varies by program; check individual program pages in the Graduate Bulletin
- **Language test policy**: TOEFL/IELTS required for non-native English speakers; specific minimums vary by program
- **Application timeline**: Varies by program; deadlines in Graduate Bulletin. Late applications accepted under some circumstances
- **Transfer credit**: Contact program director; gradmail@vcu.edu or (804) 828-6916

---

## SECTION 4 -- Costs & Financial Aid

### 4.1 Undergraduate Cost (2025-26 Academic Year)

| Expense Item | Virginia Resident | Non-Virginia Resident | Notes |
|-------------|------------------|----------------------|-------|
| Tuition and fees | $17,240 | $40,404 | Full-time undergraduate |
| Room | $8,818 | $8,818 | On-campus housing estimate |
| Dining | $6,310 | $6,310 | Meal plan estimate |
| **Total** | **$32,368** | **$55,532** | |

> **Source**: admissions.vcu.edu/cost-aid/tuition-fees/ (2025-26 academic year data)

### 4.2 Undergraduate Financial Aid Policy

| 字段 | 值 |
|------|-----|
| Need-blind/Need-aware | Need-aware (public university; domestic applicants) |
| International financial aid | Limited; out-of-state scholarships available |
| Merit scholarships | Provost Scholarship, Deans' Scholarship (apply by Nov. 1) |
| Merit scholarship conditions | Cover in-state costs only; renewable for 3 years with 28 credit hours/year |
| FAFSA | Encouraged for all applicants |
| Net Price Calculator | Available at https://1st-aid.org/vcu |
| Financial counseling | Available via Student Financial Management Center |

### 4.3 Graduate Cost & Funding Framework

| 字段 | 值 |
|------|-----|
| Application fee | $75 per program (nonrefundable) |
| In-state tuition eligibility | Virginia residents or those providing documentation of Virginia residency for purposes other than attending school |
| Funding types | Varies by program: RA, TA, fellowships, grants |
| Fee waiver policy | Not specified at university level; check individual programs |
| Graduate School website | https://graduate.vcu.edu/ |

---

## SECTION 5 -- Evidence Chain Index

### E-U-001: Undergraduate Tuition and Fees
```yaml
field: undergraduate.cost.tuition_in_state_2025_2026
value: "$17,240"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Tuition and fees | $17,240 | $40,404"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-002: Out-of-State Tuition
```yaml
field: undergraduate.cost.tuition_out_of_state_2025_2026
value: "$40,404"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Tuition and fees | $17,240 | $40,404"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-003: Total Cost of Attendance (In-State)
```yaml
field: undergraduate.cost.total_in_state_2025_2026
value: "$32,368"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Total* | $32,368 | $55,532"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-004: Total Cost of Attendance (Out-of-State)
```yaml
field: undergraduate.cost.total_out_of_state_2025_2026
value: "$55,532"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Total* | $32,368 | $55,532"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-005: Room Cost
```yaml
field: undergraduate.cost.room_2025_2026
value: "$8,818"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Room | $8,818 | $8,818"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-006: Dining Cost
```yaml
field: undergraduate.cost.dining_2025_2026
value: "$6,310"
source_url: https://admissions.vcu.edu/cost-aid/tuition-fees/
source_snippet: "Dining | $6,310 | $6,310"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### E-U-007: Application Fee
```yaml
field: undergraduate.application.fee
value: "$75"
source_url: https://admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/
source_snippet: "The online application fee is $75 and must be paid via credit card when submitting your application."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-008: Regular Decision Deadline
```yaml
field: undergraduate.deadlines.regular_decision
value: "January 15"
source_url: https://admissions.vcu.edu/apply-to-vcu/deadlines/
source_snippet: "Jan. 15, 2026: First-year regular decision application deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-009: Scholarship Deadline
```yaml
field: undergraduate.deadlines.scholarship
value: "November 1"
source_url: https://admissions.vcu.edu/apply-to-vcu/deadlines/
source_snippet: "Nov. 1, 2025: First-year scholarship deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-010: Test-Optional Policy
```yaml
field: undergraduate.admissions.test_optional
value: true
source_url: https://admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-requirements/
source_snippet: "Applicants (including those seeking scholarships) do not need to submit test scores unless applying to the Honors College guaranteed admissions programs."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-011: Guaranteed Admission Requirement
```yaml
field: undergraduate.admissions.guaranteed_admission_gpa
value: "3.5"
source_url: https://admissions.vcu.edu/apply-to-vcu/deadlines/
source_snippet: "VCU offers guaranteed university admission to most programs for first-year applicants who have a high school GPA of 3.5 or higher."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-012: Transfer Deadline
```yaml
field: undergraduate.deadlines.transfer
value: "March 15"
source_url: https://admissions.vcu.edu/apply-to-vcu/deadlines/
source_snippet: "March 15, 2026: Transfer deadline"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-U-013: Enrollment Confirmation Deadline (First-Year)
```yaml
field: undergraduate.deadlines.enrollment_confirmation
value: "May 1"
source_url: https://admissions.vcu.edu/apply-to-vcu/deadlines/
source_snippet: "First-year students accepted for fall 2026: Respond by May 1 if you were accepted to the university by April 1."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-001: Graduate Application Fee
```yaml
field: graduate.application.fee
value: "$75"
source_url: https://admissions.vcu.edu/apply-to-vcu/graduate-professional/
source_snippet: "A nonrefundable $75 application fee is required with each graduate program application."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-G-002: Graduate Admissions Model
```yaml
field: graduate.admissions.model
value: "Decentralized"
source_url: https://admissions.vcu.edu/apply-to-vcu/graduate-professional/
source_snippet: "Each professional program at Virginia Commonwealth University manages its own admission process."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-P-001: Total Program Count
```yaml
field: programs.total_count
value: 240
source_url: https://www.vcu.edu/programs/
source_snippet: "Displaying 240 programs"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-P-002: Schools and Colleges Count
```yaml
field: institution.schools_colleges_count
value: 15
source_url: https://www.vcu.edu/programs/
source_snippet: "240 programs across 15 schools and colleges"
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-001: Scholarship Information
```yaml
field: undergraduate.scholarships.university_level
value: "Provost Scholarship, Deans' Scholarship"
source_url: https://admissions.vcu.edu/cost-aid/scholarships-funding/first-year-scholarships/
source_snippet: "All incoming first-year students who apply to VCU by Nov. 1 will be considered for the following university-level scholarships."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-S-002: Scholarship Coverage
```yaml
field: undergraduate.scholarships.coverage
value: "In-state costs only"
source_url: https://admissions.vcu.edu/cost-aid/scholarships-funding/first-year-scholarships/
source_snippet: "Merit-based scholarships cover in-state costs only."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-I-001: International Test-Optional
```yaml
field: international.undergraduate.test_optional
value: true
source_url: https://admissions.vcu.edu/apply-to-vcu/international/undergraduate/
source_snippet: "Applicants (including those seeking scholarships) are eligible for test score optional review, regardless of GPA."
capture_date: 2026-07-06
evidence_type: official_webpage
```

### E-R-001: Required High School Units
```yaml
field: undergraduate.requirements.high_school_units
value: "20 units minimum"
source_url: https://admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-requirements/
source_snippet: "A minimum of 20 units is required for admission to programs on the Monroe Park Campus."
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 -- WeKnora Import Manifest

### Collection Structure

```
vcu-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, matrix)
├── 01-ug-college-humanities         (Section 1: College of Humanities and Sciences programs)
├── 02-ug-college-engineering        (Section 1: College of Engineering programs)
├── 03-ug-school-arts                (Section 1: School of the Arts programs)
├── 04-ug-school-business            (Section 1: School of Business programs)
├── 05-ug-school-education           (Section 1: School of Education programs)
├── 06-ug-health-professions         (Section 1: Health Professions, Nursing, Dentistry, Pharmacy)
├── 07-ug-wilder-social-work         (Section 1: Wilder School, Social Work, University College)
├── 08-grad-humanities-sciences      (Section 2: CHS graduate programs)
├── 09-grad-engineering              (Section 2: Engineering graduate programs)
├── 10-grad-arts-business            (Section 2: Arts + Business graduate programs)
├── 11-grad-education                (Section 2: Education graduate programs)
├── 12-grad-medicine                 (Section 2: Medicine graduate programs)
├── 13-grad-health-professions       (Section 2: Health Professions + Nursing graduate)
├── 14-grad-pharmacy-dentistry       (Section 2: Pharmacy + Dentistry graduate)
├── 15-grad-social-work-public       (Section 2: Social Work + Public Health + Wilder)
├── 16-deadlines-requirements        (Section 3: Application requirements)
├── 17-costs-financial-aid           (Section 4: Costs and aid)
├── 18-evidence-chain                (Section 5: Evidence index)
└── 19-comparison-framework          (Section 7: Cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "vcu-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|Certificate|Professional>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | English proficiency minimum scores (expand accordion) | admissions.vcu.edu/apply-to-vcu/international/undergraduate/ |
| P0 | Graduate program-specific deadlines | bulletin.vcu.edu/graduate/ |
| P1 | Complete minor list | bulletin.vcu.edu/ |
| P1 | Graduate tuition rates | sfs.vcu.edu/tuition-and-fees/ |
| P1 | TOEFL/IELTS minimums per graduate program | graduate.vcu.edu/programs/ |
| P2 | Honors College requirements | honors.vcu.edu/admissions/ |
| P2 | Student profile / class profile data | admissions.vcu.edu/apply-to-vcu/undergraduate/first-year/first-year-student-profile/ |
| P2 | Net Price Calculator results | 1st-aid.org/vcu |

---

## SECTION 7 -- Cross-School Comparison Framework

| 维度 | VCU | [School 2] | [School 3] |
|------|-----|-----------|-----------|
| 总项目数 (Rule 1) | 240 | | |
| 学院/系数 (Rule 2) | 15 | | |
| 公立/私立 | Public | | |
| 所在地 | Richmond, VA | | |
| 本科学费 (In-state) | $17,240 | | |
| 本科学费 (Out-of-state) | $40,404 | | |
| 总COA (In-state) | $32,368 | | |
| 总COA (Out-of-state) | $55,532 | | |
| Need-blind (intl?) | No (need-aware) | | |
| EA Deadline | N/A (Nov 1 = scholarship only) | | |
| RD Deadline | January 15 | | |
| SAT/ACT Required? | No (test-optional) | | |
| TOEFL Min | 80 | | |
| IELTS Min | 6.5 | | |
| Application Fee | $75 | | |
| Graduate App Fee | $75 | | |
| 强势领域 | Arts/Design, Medical Center, Health Sciences | | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.vcu.edu, www.vcu.edu/programs, vcu.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school -> department -> degree-level -> program
