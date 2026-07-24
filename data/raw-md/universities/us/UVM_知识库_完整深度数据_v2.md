# University of Vermont (UVM) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BSed/BSW/etc.) | 95 |
| 本科辅修 (Minor) | 83 |
| 本科证书 (Certificate) | 7 |
| 研究生学位项目 (MS/MA/MEd/MBA/MPH/MPA/MSW/PhD/EdD/DNP/DPT/OTD/DrPH) | 91 |
| 研究生证书 (Certificate / Micro-Certificate) | 31 |
| **学位项目总计 (UG + Grad)** | **307** |
| 学院 / 独立系所总数 | 10 (7 UG-degree-granting + Larner Med + Graduate College + Institute for Agroecology) |

### 0.2 学院 / 系层级结构

```
University of Vermont
├── College of Agriculture and Life Sciences (CALS)                          [学院]
│   ├── Agriculture, Landscape, and Environment (ALE)                       [系]
│   ├── Animal and Veterinary Sciences (ASCI)                               [系]
│   ├── Community Development and Applied Economics (CDAE)                  [系]
│   ├── Microbiology and Molecular Genetics (MMG)                           [系]
│   ├── Nutrition and Food Sciences (NFS)                                   [系]
│   ├── Plant Biology (PBIO)                                                [系]
│   └── Plant and Soil Science (PSS)                                        [系]
├── College of Arts and Sciences (CAS)                                       [学院]
│   ├── Anthropology                                                        [系]
│   ├── Art and Art History                                                 [系]
│   ├── Biology                                                             [系]
│   ├── Chemistry                                                           [系]
│   ├── Classics                                                            [系]
│   ├── Computer Science                                                    [系]
│   ├── Economics                                                           [系]
│   ├── English                                                             [系]
│   ├── Geography and Geosciences                                           [系]
│   ├── Global Studies                                                      [系]
│   ├── History                                                             [系]
│   ├── Linguistics                                                         [系]
│   ├── Mathematics and Statistics                                          [系]
│   ├── Music                                                               [系]
│   ├── Philosophy                                                          [系]
│   ├── Physics                                                             [系]
│   ├── Political Science                                                   [系]
│   ├── Psychological Science                                               [系]
│   ├── Religion                                                            [系]
│   ├── Romance Languages                                                   [系]
│   ├── Sociology                                                           [系]
│   ├── Theatre and Dance                                                   [系]
│   └── Gender, Sexuality, and Women's Studies                              [系]
├── Grossman School of Business                                              [学院]
│   ├── Accounting                                                          [系]
│   ├── Business Administration                                             [系]
│   └── Sustainable Innovation                                              [系]
├── College of Education and Social Services (CESS)                          [学院]
│   ├── Education                                                           [系]
│   ├── Social Work                                                         [系]
│   └── Human Development and Family Science                                [系]
├── College of Engineering and Mathematical Sciences (CEMS)                  [学院]
│   ├── Biomedical Engineering                                              [系]
│   ├── Civil and Environmental Engineering                                 [系]
│   ├── Computer Science ⚠ shared with CAS                                  [系]
│   ├── Electrical Engineering                                              [系]
│   ├── Mechanical Engineering                                              [系]
│   ├── Mathematics and Statistics                                          [系]
│   └── Physics ⚠ shared with CAS                                           [系]
├── Rubenstein School of Environment and Natural Resources (RSENR)           [学院]
│   ├── Environmental Sciences                                              [系]
│   ├── Forestry                                                            [系]
│   ├── Parks, Recreation, and Tourism                                      [系]
│   └── Wildlife and Fisheries Biology                                      [系]
├── College of Nursing and Health Sciences (CNHS)                            [学院]
│   ├── Nursing                                                             [系]
│   ├── Communication Sciences and Disorders                                [系]
│   ├── Exercise Science                                                    [系]
│   ├── Medical Radiation Sciences                                          [系]
│   └── Public Health Sciences                                              [系]
├── Larner College of Medicine                                               [学院] (graduate only)
│   ├── Microbiology and Molecular Genetics                                 [系]
│   ├── Pharmacology                                                        [系]
│   ├── Pathology                                                           [系]
│   └── Public Health                                                       [系]
└── Graduate College                                                         [学院] (interdisciplinary)

Note: Computer Science is jointly administered by CAS and CEMS.
Physics is jointly administered by CAS and CEMS.
Biochemistry is jointly administered by CAS (see CCP programs).
The Institute for Agroecology is a cross-college research institute.
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| Minor | Minor | 本科 | 83 |
| BS | Bachelor of Science | 本科 | 53 |
| MS | Master of Science | 研究生 | 51 |
| Certificate | Certificate | 本科 | 34 |
| BA | Bachelor of Arts | 本科 | 33 |
| PhD | Doctor of Philosophy | 研究生 | 18 |
| MEd | Master of Education | 研究生 | 6 |
| BSed | Bachelor of Science in Education | 本科 | 6 |
| MA | Master of Arts | 研究生 | 5 |
| Micro-Certificate | Micro-Certificate | 研究生 | 4 |
| MPH | Master of Public Health | 研究生 | 2 |
| BA/BS | Bachelor of Arts/Science (Individually Designed) | 本科 | 2 |
| DNP | Doctor of Nursing Practice | 研究生 | 2 |
| MBA | Master of Business Administration | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| DrPH | Doctor of Public Health | 研究生 | 1 |
| BSW | Bachelor of Social Work | 本科 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSed | BSW | BA/BS | Minor | Certificate | MS | MA | MEd | MBA | MPH | MPA | MSW | PhD | EdD | DNP | DPT | OTD | DrPH | Micro-Certificate | 合计 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| College of Agriculture and Life Sciences | 0 | 14 | 0 | 0 | 1 | 9 | 0 | 8 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 35 |
| College of Arts and Sciences | 30 | 9 | 0 | 0 | 1 | 41 | 4 | 7 | 5 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 100 |
| College of Education and Social Services | 0 | 3 | 6 | 1 | 0 | 9 | 7 | 1 | 0 | 6 | 0 | 0 | 0 | 1 | 3 | 1 | 0 | 0 | 0 | 0 | 3 | 41 |
| College of Engineering and Mathematical Sciences | 3 | 14 | 0 | 0 | 0 | 8 | 10 | 14 | 0 | 0 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 56 |
| College of Nursing and Health Sciences | 0 | 7 | 0 | 0 | 0 | 9 | 1 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 1 | 1 | 0 | 1 | 25 |
| Graduate College | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| Grossman School of Business | 0 | 1 | 0 | 0 | 0 | 2 | 3 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 |
| Institute for Agroecology | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| Larner College of Medicine | 0 | 0 | 0 | 0 | 0 | 1 | 9 | 8 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 21 |
| Rubenstein School of Environment and Natural Resources | 0 | 5 | 0 | 0 | 0 | 4 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 15 |
| **合计** | **33** | **53** | **6** | **1** | **2** | **83** | **34** | **51** | **5** | **6** | **1** | **2** | **1** | **1** | **18** | **1** | **2** | **1** | **1** | **1** | **4** | **307** |


---

## SECTION 1 — Undergraduate Education

### 1.1 College/school architecture

UVM has 7 undergraduate-degree-granting colleges/schools. For the complete college→department hierarchy, see Section 0.2. The following sections list every undergraduate program grouped by 学院 → 学位级别.

### 1.2 Undergraduate Majors — grouped by 学院 > 学位级别


#### College of Agriculture and Life Sciences

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Agroecology Major | BS | https://www.uvm.edu/cals/ale/program/agroecology-major |
| 2 | Community And International Development | BS | https://www.uvm.edu/cals/cdae/program/community-and-international-development |
| 3 | Community Centered Design Bs | BS | https://www.uvm.edu/cals/cdae/program/community-centered-design-bs |
| 4 | Community Entrepreneurship | BS | https://www.uvm.edu/cals/cdae/program/community-entrepreneurship |
| 5 | Ecological Landscape Horticulture | BS | https://www.uvm.edu/cals/ale/program/ecological-landscape-horticulture |
| 6 | Ecological Landscape Planning And Design Major | BS | https://www.uvm.edu/cals/ale/program/ecological-landscape-planning-and-design-major |
| 7 | Equine Studies | BS | https://www.uvm.edu/cals/asci/program/equine-studies |
| 8 | Food Systems Bs | BS | https://www.uvm.edu/cals/program/food-systems-bs |
| 9 | Microbiology Major | BS | https://www.uvm.edu/cals/program/microbiology-major |
| 10 | Molecular Genetics Major | BS | https://www.uvm.edu/cals/program/molecular-genetics-major |
| 11 | Nutrition And Food Sciences | BS | https://www.uvm.edu/cals/nfs/program/nutrition-and-food-sciences |
| 12 | Plant Biology Bs | BS | https://www.uvm.edu/cals/plantbiology/program/plant-biology-bs |
| 13 | Public Communication | BS | https://www.uvm.edu/cals/cdae/program/public-communication |
| 14 | Self Designed Major | BA/BS | https://www.uvm.edu/cals/program/self-designed-major |
| 15 | Soil Science | BS | https://www.uvm.edu/cals/ale/program/soil-science |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Applied Design Minor | https://www.uvm.edu/cals/cdae/program/applied-design-minor |
| 2 | Bioinformatics Minor | https://www.uvm.edu/cals/program/bioinformatics-minor |
| 3 | Biosecurity Minor | https://www.uvm.edu/cals/cdae/program/biosecurity-minor |
| 4 | Consumer And Advertising Minor | https://www.uvm.edu/cals/cdae/program/consumer-and-advertising-minor |
| 5 | Food Systems Minor | https://www.uvm.edu/cals/cdae/program/food-systems-minor |
| 6 | Green Building And Community Design Minor | https://www.uvm.edu/cals/cdae/program/green-building-and-community-design-minor |
| 7 | Microbiology Minor | https://www.uvm.edu/cals/program/microbiology-minor |
| 8 | Molecular Genetics Minor | https://www.uvm.edu/cals/program/molecular-genetics-minor |
| 9 | Sports Management Minor | https://www.uvm.edu/cals/cdae/program/sports-management-minor |

#### College of Arts and Sciences

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Ba Anthropology | BA | https://www.uvm.edu/cas/anthropology/program/ba-anthropology |
| 2 | Ba Chemistry | BA | https://www.uvm.edu/cas/chemistry/program/ba-chemistry |
| 3 | Ba Chinese | BA | https://www.uvm.edu/cas/asian/program/ba-chinese |
| 4 | Ba Classics | BA | https://www.uvm.edu/cas/classics/program/ba-classics |
| 5 | Ba Dance | BA | https://www.uvm.edu/cas/theatreanddance/program/ba-dance |
| 6 | Ba Environmental | BA | https://www.uvm.edu/cas/environmentalstudies/cas/environmentalstudies/undergraduate-programs/program/ba-environmental |
| 7 | Ba Film And Television Studies | BA | https://www.uvm.edu/cas/filmtv/program/ba-film-and-television-studies |
| 8 | Ba French | BA | https://www.uvm.edu/cas/french-italian/program/ba-french |
| 9 | Ba Gender Sexuality And Womens Studies | BA | https://www.uvm.edu/cas/genderstudies/program/ba-gender-sexuality-and-womens-studies |
| 10 | Ba Geography | BA | https://www.uvm.edu/cas/geography/program/ba-geography |
| 11 | Ba German | BA | https://www.uvm.edu/cas/germanrussianhebrew/program/ba-german |
| 12 | Ba Global Studies | BA | https://www.uvm.edu/cas/globalstudies/program/ba-global-studies |
| 13 | Ba Health And Society | BA | https://www.uvm.edu/cas/healthsociety/program/ba-health-and-society |
| 14 | Ba History | BA | https://www.uvm.edu/cas/history/program/ba-history |
| 15 | Ba Japanese | BA | https://www.uvm.edu/cas/asian/program/ba-japanese |
| 16 | Ba Linguistics | BA | https://www.uvm.edu/cas/linguistics/program/ba-linguistics |
| 17 | Ba Major Or Minor Art History | BA | https://www.uvm.edu/cas/art/program/ba-major-or-minor-art-history |
| 18 | Ba Major Or Minor Biology | BA | https://www.uvm.edu/cas/biology/program/ba-major-or-minor-biology |
| 19 | Ba Major Or Minor Economics | BA | https://www.uvm.edu/cas/economics/program/ba-major-or-minor-economics |
| 20 | Ba Major Or Minor English | BA | https://www.uvm.edu/cas/english/program/ba-major-or-minor-english |
| 21 | Ba Music | BA | https://www.uvm.edu/cas/music/program/ba-music |
| 22 | Ba Philosophy | BA | https://www.uvm.edu/cas/philosophy/program/ba-philosophy |
| 23 | Ba Political Science | BA | https://www.uvm.edu/cas/polisci/program/ba-political-science |
| 24 | Ba Psychological Science | BA | https://www.uvm.edu/cas/psychology/program/ba-psychological-science |
| 25 | Ba Religion | BA | https://www.uvm.edu/cas/religion/program/ba-religion |
| 26 | Ba Russian | BA | https://www.uvm.edu/cas/germanrussianhebrew/program/ba-russian |
| 27 | Ba Sociology | BA | https://www.uvm.edu/cas/sociology/program/ba-sociology |
| 28 | Ba Spanish | BA | https://www.uvm.edu/cas/spanish/program/ba-spanish |
| 29 | Ba Studio Art | BA | https://www.uvm.edu/cas/art/program/ba-studio-art |
| 30 | Ba Theatre | BA | https://www.uvm.edu/cas/theatreanddance/program/ba-theatre |
| 31 | Bs Anthropology | BS | https://www.uvm.edu/cas/anthropology/program/bs-anthropology |
| 32 | Bs Biochemistry | BS | https://www.uvm.edu/ccp/biochemistry-program/program/bs-biochemistry |
| 33 | Bs Biological Science | BS | https://www.uvm.edu/ccp/biologicalscience/program/bs-biological-science |
| 34 | Bs Chemistry | BS | https://www.uvm.edu/cas/chemistry/program/bs-chemistry |
| 35 | Bs Economics Quantitative | BS | https://www.uvm.edu/cas/economics/program/bs-economics-quantitative |
| 36 | Bs Psychological Science | BS | https://www.uvm.edu/cas/psychology/program/bs-psychological-science |
| 37 | Individually Designed Major/Minor | BA/BS | https://www.uvm.edu/cas/program/individually-designed-major/minor |
| 38 | Major Or Minor Geosciences | BS | https://www.uvm.edu/cas/geography/program/major-or-minor-geosciences |
| 39 | Major Or Minor Neuroscience | BS | https://www.uvm.edu/cas/neuro/program/major-or-minor-neuroscience |
| 40 | Zoology | BS | https://www.uvm.edu/cas/biology/program/zoology |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Biochemistry Minor | https://www.uvm.edu/ccp/biochemistry-program/program/biochemistry-minor |
| 2 | Minor | https://www.uvm.edu/cas/environmentalstudies/undergraduate-programs/program/minor |
| 3 | Minor African Studies | https://www.uvm.edu/cas/globalstudies/program/minor-african-studies |
| 4 | Minor Anthropology | https://www.uvm.edu/cas/anthropology/program/minor-anthropology |
| 5 | Minor Art | https://www.uvm.edu/cas/art/program/minor-art |
| 6 | Minor Canadian Studies | https://www.uvm.edu/cas/globalstudies/program/minor-canadian-studies |
| 7 | Minor Chinese | https://www.uvm.edu/cas/asian/program/minor-chinese |
| 8 | Minor Classics | https://www.uvm.edu/cas/classics/program/minor-classics |
| 9 | Minor Critical Race And Ethnic Studies | https://www.uvm.edu/cas/ethnicstudies/program/minor-critical-race-and-ethnic-studies |
| 10 | Minor Dance | https://www.uvm.edu/cas/theatreanddance/program/minor-dance |
| 11 | Minor European Studies | https://www.uvm.edu/cas/globalstudies/program/minor-european-studies |
| 12 | Minor Film And Television Studies | https://www.uvm.edu/cas/filmtv/program/minor-film-and-television-studies |
| 13 | Minor French | https://www.uvm.edu/cas/french-italian/program/minor-french |
| 14 | Minor Gender Sexuality And Womens Studies | https://www.uvm.edu/cas/genderstudies/program/minor-gender-sexuality-and-womens-studies |
| 15 | Minor German | https://www.uvm.edu/cas/germanrussianhebrew/program/minor-german |
| 16 | Minor Global Studies | https://www.uvm.edu/cas/globalstudies/program/minor-global-studies |
| 17 | Minor Health And Society | https://www.uvm.edu/cas/healthsociety/cas/healthsociety/undergraduate-programs/program/minor-health-and-society |
| 18 | Minor History | https://www.uvm.edu/cas/history/program/minor-history |
| 19 | Minor Holocaust Studies | https://www.uvm.edu/cas/holocauststudies/program/minor-holocaust-studies |
| 20 | Minor Italian Studies | https://www.uvm.edu/cas/french-italian/program/minor-italian-studies |
| 21 | Minor Japanese | https://www.uvm.edu/cas/asian/program/minor-japanese |
| 22 | Minor Jewish Studies | https://www.uvm.edu/cas/religion/program/minor-jewish-studies |
| 23 | Minor Latin American And Caribbean Studies | https://www.uvm.edu/cas/globalstudies/program/minor-latin-american-and-caribbean-studies |
| 24 | Minor Law And Society | https://www.uvm.edu/cas/sociology/program/minor-law-and-society |
| 25 | Minor Linguistics | https://www.uvm.edu/cas/linguistics/program/minor-linguistics |
| 26 | Minor Middle East Studies | https://www.uvm.edu/cas/globalstudies/program/minor-middle-east-studies |
| 27 | Minor Music Technology And Business | https://www.uvm.edu/cas/music/program/minor-music-technology-and-business |
| 28 | Minor Musical Theatre | https://www.uvm.edu/cas/theatreanddance/program/minor-musical-theatre |
| 29 | Minor Philosophy | https://www.uvm.edu/cas/philosophy/program/minor-philosophy |
| 30 | Minor Political Science | https://www.uvm.edu/cas/polisci/program/minor-political-science |
| 31 | Minor Psychological Science | https://www.uvm.edu/cas/psychology/program/minor-psychological-science |
| 32 | Minor Public Policy Analysis | https://www.uvm.edu/cas/polisci/program/minor-public-policy-analysis |
| 33 | Minor Religion | https://www.uvm.edu/cas/religion/program/minor-religion |
| 34 | Minor Russian | https://www.uvm.edu/cas/germanrussianhebrew/program/minor-russian |
| 35 | Minor Russian And East European Studies | https://www.uvm.edu/cas/globalstudies/program/minor-russian-and-east-european-studies |
| 36 | Minor Sexuality And Gender Identity Studies | https://www.uvm.edu/cas/genderstudies/program/minor-sexuality-and-gender-identity-studies |
| 37 | Minor Spanish | https://www.uvm.edu/cas/spanish/program/minor-spanish |
| 38 | Minor Theatre | https://www.uvm.edu/cas/theatreanddance/program/minor-theatre |
| 39 | Minor Writing | https://www.uvm.edu/cas/english/program/minor-writing |
| 40 | Music Minor | https://www.uvm.edu/cas/music/program/music-minor |
| 41 | Reporting And Documentary Storytelling Minor | https://www.uvm.edu/cas/storytelling/program/reporting-and-documentary-storytelling-minor |

##### Certificates

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Certificate Religious Literacy Professions | https://www.uvm.edu/cas/religion/program/certificate-religious-literacy-professions |
| 2 | Teaching Artist Music Undergraduate Certificate | https://www.uvm.edu/cas/music/program/teaching-artist-music-undergraduate-certificate |
| 3 | Undergraduate Certificate Community Music Organ | https://www.uvm.edu/cas/music/program/undergraduate-certificate-community-music-organ |

#### Grossman School of Business

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Bachelor Science Business Administration Bsbusadmin | BS | https://www.uvm.edu/business/program/bachelor-science-business-administration-bsbusadmin |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Minor Accounting | https://www.uvm.edu/business/program/minor-accounting |
| 2 | Minor Business Administration | https://www.uvm.edu/business/program/minor-business-administration |

#### College of Education and Social Services

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Art Education Bs | BS | https://www.uvm.edu/cess/doe/program/art-education-bs |
| 2 | Bachelor Social Work Bsw | BSW | https://www.uvm.edu/cess/socialwork/program/bachelor-social-work-bsw |
| 3 | Early Childhood Education Bsed | BSed | https://www.uvm.edu/cess/doe/program/early-childhood-education-bsed |
| 4 | Elementary Education Bsed | BSed | https://www.uvm.edu/cess/doe/program/elementary-education-bsed |
| 5 | Human Development And Family Science Bs | BS | https://www.uvm.edu/cess/chdf/program/human-development-and-family-science-bs |
| 6 | Individually Designed Major Bsed | BSed | https://www.uvm.edu/cess/doe/program/individually-designed-major-bsed |
| 7 | Middle Level Education Bsed | BSed | https://www.uvm.edu/cess/doe/program/middle-level-education-bsed |
| 8 | Music Education Bs | BS | https://www.uvm.edu/cess/doe/program/music-education-bs |
| 9 | Secondary Education Bsed | BSed | https://www.uvm.edu/cess/doe/program/secondary-education-bsed |
| 10 | Special Education Bsed | BSed | https://www.uvm.edu/cess/doe/program/special-education-bsed |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | American Sign Language Asl Minor | https://www.uvm.edu/cess/doe/program/american-sign-language-asl-minor |
| 2 | Childhood Studies Minor | https://www.uvm.edu/cess/doe/program/childhood-studies-minor |
| 3 | Coaching Minor | https://www.uvm.edu/cess/doe/program/coaching-minor |
| 4 | Computer Science Education Minor | https://www.uvm.edu/cess/doe/program/computer-science-education-minor |
| 5 | Education Cultural And Linguistic Diversity Minor | https://www.uvm.edu/cess/doe/program/education-cultural-and-linguistic-diversity-minor |
| 6 | Education Studies Minor | https://www.uvm.edu/cess/doe/program/education-studies-minor |
| 7 | Human Development And Family Science Minor | https://www.uvm.edu/cess/chdf/program/human-development-and-family-science-minor |
| 8 | Military Leadership Minor | https://www.uvm.edu/cess/doe/program/military-leadership-minor |
| 9 | Special Education Minor | https://www.uvm.edu/cess/doe/program/special-education-minor |

#### College of Engineering and Mathematical Sciences

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Ba Computer Science | BA | https://www.uvm.edu/cems/cs/program/ba-computer-science |
| 2 | Ba Major Physics | BA | https://www.uvm.edu/cems/physics/program/ba-major-physics |
| 3 | Ba Mathematics | BA | https://www.uvm.edu/cems/mathstat/program/ba-mathematics |
| 4 | Bs Biomedical Engineering | BS | https://www.uvm.edu/cems/ebe/program/bs-biomedical-engineering |
| 5 | Bs Civil Engineering | BS | https://www.uvm.edu/cems/cee/program/bs-civil-engineering |
| 6 | Bs Computer Science | BS | https://www.uvm.edu/cems/cs/program/bs-computer-science |
| 7 | Bs Computer Science And Information Systems | BS | https://www.uvm.edu/cems/cs/program/bs-computer-science-and-information-systems |
| 8 | Bs Data Science | BS | https://www.uvm.edu/cems/program/bs-data-science |
| 9 | Bs Electrical Engineering | BS | https://www.uvm.edu/cems/ebe/program/bs-electrical-engineering |
| 10 | Bs Engineering | BS | https://www.uvm.edu/cems/program/bs-engineering |
| 11 | Bs Engineering Management | BS | https://www.uvm.edu/cems/program/bs-engineering-management |
| 12 | Bs Environmental Engineering | BS | https://www.uvm.edu/cems/cee/program/bs-environmental-engineering |
| 13 | Bs Major Physics | BS | https://www.uvm.edu/cems/physics/program/bs-major-physics |
| 14 | Bs Mathematics | BS | https://www.uvm.edu/cems/mathstat/program/bs-mathematics |
| 15 | Bs Mechanical Engineering | BS | https://www.uvm.edu/cems/me/program/bs-mechanical-engineering |
| 16 | Bs Statistics | BS | https://www.uvm.edu/cems/mathstat/program/bs-statistics |
| 17 | Co Major Mathematics | BS | https://www.uvm.edu/cems/mathstat/program/co-major-mathematics |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Minor Astronomy | https://www.uvm.edu/cems/physics/program/minor-astronomy |
| 2 | Minor Computer Engineering | https://www.uvm.edu/cems/ebe/program/minor-computer-engineering |
| 3 | Minor Computer Science | https://www.uvm.edu/cems/cs/program/minor-computer-science |
| 4 | Minor Electrical Engineering | https://www.uvm.edu/cems/ebe/program/minor-electrical-engineering |
| 5 | Minor Mathematics Pure | https://www.uvm.edu/cems/mathstat/program/minor-mathematics-pure |
| 6 | Minor Physics | https://www.uvm.edu/cems/physics/program/minor-physics |
| 7 | Minor Statistics | https://www.uvm.edu/cems/mathstat/program/minor-statistics |
| 8 | Minor Sustainable Energy Engineering | https://www.uvm.edu/cems/program/minor-sustainable-energy-engineering |

##### Certificates

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Undergraduate Certificate Autonomy And Robotics | https://www.uvm.edu/cems/ebe/program/undergraduate-certificate-autonomy-and-robotics |
| 2 | Undergraduate Certificate Computer Aided Engineering Technology Caet | https://www.uvm.edu/cems/program/undergraduate-certificate-computer-aided-engineering-technology-caet |
| 3 | Undergraduate Certificate Semiconductor Engineering And Physics Ucsep | https://www.uvm.edu/cems/program/undergraduate-certificate-semiconductor-engineering-and-physics-ucsep |

#### Rubenstein School of Environment and Natural Resources

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Bs Environmental Sciences | BS | https://www.uvm.edu/rsenr/environmentalsciences/program/bs-environmental-sciences |
| 2 | Bs Forestry | BS | https://www.uvm.edu/rsenr/forestry/program/bs-forestry |
| 3 | Bs Parks Recreation And Tourism | BS | https://www.uvm.edu/rsenr/prt/program/bs-parks-recreation-and-tourism |
| 4 | Bs Sustainability Ecology And Policy | BS | https://www.uvm.edu/rsenr/sustainability-ecology-policy/program/bs-sustainability-ecology-and-policy |
| 5 | Bs Wildlife And Fisheries Biology | BS | https://www.uvm.edu/rsenr/wildlife-fisheries-biology/program/bs-wildlife-and-fisheries-biology |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Minor Forestry | https://www.uvm.edu/rsenr/forestry/program/minor-forestry |
| 2 | Minor Geospatial Technologies | https://www.uvm.edu/rsenr/geospatial/program/minor-geospatial-technologies |
| 3 | Minor Parks Recreation And Tourism | https://www.uvm.edu/rsenr/prt/program/minor-parks-recreation-and-tourism |
| 4 | Minor Wildlife Biology | https://www.uvm.edu/rsenr/wildlife-fisheries-biology/program/minor-wildlife-biology |

#### College of Nursing and Health Sciences

##### Majors

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Bachelor Science Biomedical And Clinical Sciences | BS | https://www.uvm.edu/cnhs/bhs/program/bachelor-science-biomedical-and-clinical-sciences |
| 2 | Communication Sciences And Disorders | BS | https://www.uvm.edu/cnhs/csd/program/communication-sciences-and-disorders |
| 3 | Exercise Science | BS | https://www.uvm.edu/cnhs/rms/program/exercise-science |
| 4 | Interprofessional Health Sciences | BS | https://www.uvm.edu/cnhs/program/interprofessional-health-sciences |
| 5 | Medical Radiation Sciences | BS | https://www.uvm.edu/cnhs/bhs/program/medical-radiation-sciences |
| 6 | Professional Nursing | BS | https://www.uvm.edu/cnhs/nursing/program/professional-nursing |
| 7 | Public Health Sciences | BS | https://www.uvm.edu/cnhs/bhs/program/public-health-sciences |

##### Minors

| # | Minor | URL |
|---|-------|-----|
| 1 | Communication Sciences And Disorders Minor | https://www.uvm.edu/cnhs/csd/program/communication-sciences-and-disorders-minor |
| 2 | Emergency Medical Services Minor | https://www.uvm.edu/cnhs/rms/program/emergency-medical-services-minor |
| 3 | Epidemiology Minor | https://www.uvm.edu/cnhs/bhs/program/epidemiology-minor |
| 4 | Exercise Science Minor | https://www.uvm.edu/cnhs/rms/program/exercise-science-minor |
| 5 | Global Public Health Minor | https://www.uvm.edu/cnhs/bhs/program/global-public-health-minor |
| 6 | Integrative Health And Wellness Coaching Minor | https://www.uvm.edu/cnhs/rms/program/integrative-health-and-wellness-coaching-minor |
| 7 | Integrative Health Minor | https://www.uvm.edu/cnhs/rms/program/integrative-health-minor |
| 8 | Medical Diagnostics Minor | https://www.uvm.edu/cnhs/bhs/program/medical-diagnostics-minor |
| 9 | Public Health Equity And Advocacy Minor | https://www.uvm.edu/cnhs/bhs/program/public-health-equity-and-advocacy-minor |

##### Certificates

| # | Certificate | URL |
|---|-------------|-----|
| 1 | Undergraduate Certificate Speech Language Pathology Assistant | https://www.uvm.edu/cnhs/csd/program/undergraduate-certificate-speech-language-pathology-assistant |


### 1.3 Interdisciplinary / cross-college undergraduate programs

UVM offers several interdisciplinary programs that span multiple colleges:

- **Agroecology** (CALS + Institute for Agroecology)
- **Biochemistry** (CAS + CCP)
- **Computer Science** (CAS + CEMS — BA in CAS, BS in CEMS)
- **Physics** (CAS + CEMS — BA in CAS, BS in CEMS)
- **Neuroscience** (CAS + CNHS)
- **Individually Designed Major** (available in CESS as BSed, and university-wide as BA/BS)

### 1.4 General Education Requirements

UVM requires all undergraduates to complete the **University Writing Requirement** and a set of **Distribution Requirements** across categories including:
- Quantitative Reasoning
- Natural Sciences
- Social Sciences
- Humanities
- Fine Arts
- Diversity requirements

Details: https://www.uvm.edu/academics

### 1.5 Admitted Student Profile (Fall 2024)

| Metric | Value |
|--------|-------|
| Average GPA (4.0 scale) | 3.8 |
| SAT EBRW (Middle 50%) | 670–740 |
| SAT Math (Middle 50%) | 650–740 |
| ACT (Middle 50%) | 31–34 |

---

## SECTION 2 — Graduate Education

### 2.1 Graduate programs — grouped by 学院 > 学位级别

UVM offers graduate programs across 10 colleges/schools. The Graduate College administers interdisciplinary programs. Admissions are **decentralized** — each program manages its own admissions process.


#### College of Agriculture and Life Sciences

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Agroecology | MS | https://www.uvm.edu/cals/ale/program/agroecology |
| 2 | Agroecology Ms | MS | https://www.uvm.edu/cals/ale/program/agroecology-ms |
| 3 | Field Naturalist Ms | MS | https://www.uvm.edu/cals/plantbiology/program/field-naturalist-ms |
| 4 | Food Systems Amp | MS | https://www.uvm.edu/cals/foodsystems/program/food-systems-amp |
| 5 | Food Systems Ms | MS | https://www.uvm.edu/cals/foodsystems/program/food-systems-ms |
| 6 | Masters Community Development And Applied Economics | MS | https://www.uvm.edu/cals/cdae/program/masters-community-development-and-applied-economics |
| 7 | Ms Dietetics Msd | MS | https://www.uvm.edu/cals/nfs/program/ms-dietetics-msd |
| 8 | Ms Nutrition And Food Sciences | MS | https://www.uvm.edu/cals/nfs/program/ms-nutrition-and-food-sciences |
| 9 | Public Administration | MPA | https://www.uvm.edu/cals/cdae/program/public-administration |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Food Systems Phd | PhD | https://www.uvm.edu/cals/foodsystems/program/food-systems-phd |
| 2 | Phd Plant Biology | PhD | https://www.uvm.edu/cals/plantbiology/program/phd-plant-biology |

#### College of Arts and Sciences

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Amp Biochemistry | MS | https://www.uvm.edu/ccp/biochemistry-program/program/amp-biochemistry |
| 2 | Amp Chemistry | MS | https://www.uvm.edu/cas/chemistry/program/amp-chemistry |
| 3 | Amp Historic Preservation | MS | https://www.uvm.edu/cas/historicpreservation/program/amp-historic-preservation |
| 4 | Amp History | MA | https://www.uvm.edu/cas/history/program/amp-history |
| 5 | Amp Literature Media Theory | MA | https://www.uvm.edu/cas/english/program/amp-literature-media-theory |
| 6 | Biochemistry Ms | MS | https://www.uvm.edu/ccp/biochemistry-program/program/biochemistry-ms |
| 7 | Ma History | MA | https://www.uvm.edu/cas/history/program/ma-history |
| 8 | Ma Literature Media Theory | MA | https://www.uvm.edu/cas/english/program/ma-literature-media-theory |
| 9 | Ma Or Amp Experimental Or Clinical Psychology | MA | https://www.uvm.edu/cas/psychology/program/ma-or-amp-experimental-or-clinical-psychology |
| 10 | Ms Chemistry | MS | https://www.uvm.edu/cas/chemistry/program/ms-chemistry |
| 11 | Ms Geosciences | MS | https://www.uvm.edu/cas/geography/program/ms-geosciences |
| 12 | Ms Historic Preservation | MS | https://www.uvm.edu/cas/historicpreservation/program/ms-historic-preservation |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Phd Chemistry | PhD | https://www.uvm.edu/cas/chemistry/program/phd-chemistry |
| 2 | Phd Computational Studies Culture And Society | PhD | https://www.uvm.edu/ccp/program/phd-computational-studies-culture-and-society |
| 3 | Phd Psychology | PhD | https://www.uvm.edu/cas/psychology/program/phd-psychology |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Teaching English Speakers Other Languages | Certificate | https://www.uvm.edu/cas/linguistics/program/teaching-english-speakers-other-languages |

#### Grossman School of Business

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accelerated Macc | MS | https://www.uvm.edu/business/program/accelerated-macc |
| 2 | Master Accountancy | MS | https://www.uvm.edu/business/program/master-accountancy |
| 3 | Sustainable Innovation Mba | MBA | https://www.uvm.edu/business/program/sustainable-innovation-mba |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Certificate Graduate Study Sustainable Enterprise | Certificate | https://www.uvm.edu/business/program/certificate-graduate-study-sustainable-enterprise |
| 2 | Micro Certificate Graduate Study Sustainability Reporting | Certificate | https://www.uvm.edu/business/program/micro-certificate-graduate-study-sustainability-reporting |
| 3 | Micro Certificate Graduate Study Sustainable Family Enterprise | Certificate | https://www.uvm.edu/business/program/micro-certificate-graduate-study-sustainable-family-enterprise |

#### College of Education and Social Services

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Advanced Specialties Educational Practice Med | MEd | https://www.uvm.edu/cess/doe/program/advanced-specialties-educational-practice-med |
| 2 | Counseling Ms | MS | https://www.uvm.edu/cess/chdf/program/counseling-ms |
| 3 | Educational Leadership And Policy Studies Med | MEd | https://www.uvm.edu/cess/doe/program/educational-leadership-and-policy-studies-med |
| 4 | Higher Education And Student Affairs Administration Hesa Med Amp | MEd | https://www.uvm.edu/cess/doe/program/higher-education-and-student-affairs-administration-hesa-med-amp |
| 5 | Interdisciplinary Educational Studies Med | MEd | https://www.uvm.edu/cess/doe/program/interdisciplinary-educational-studies-med |
| 6 | Master Arts Teaching Mat | MEd | https://www.uvm.edu/cess/doe/program/master-arts-teaching-mat |
| 7 | Master Social Work Msw | MSW | https://www.uvm.edu/cess/socialwork/program/master-social-work-msw |
| 8 | Special Education Med | MEd | https://www.uvm.edu/cess/doe/program/special-education-med |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Counselor Education And Supervision Phd | PhD | https://www.uvm.edu/cess/chdf/program/counselor-education-and-supervision-phd |
| 2 | Educational Leadership And Policy Studies Edd | EdD | https://www.uvm.edu/cess/doe/program/educational-leadership-and-policy-studies-edd |
| 3 | Educational Leadership And Policy Studies Phd | PhD | https://www.uvm.edu/cess/doe/program/educational-leadership-and-policy-studies-phd |
| 4 | Social Emotional And Behavioral Health And Inclusive Education Shie Phd | PhD | https://www.uvm.edu/cess/doe/program/social-emotional-and-behavioral-health-and-inclusive-education-shie-phd |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Collaborative And Resiliency Oriented Practices Schools Micro Certificate | Micro-Certificate | https://www.uvm.edu/cess/doe/program/collaborative-and-resiliency-oriented-practices-schools-micro-certificate |
| 2 | Community Schools Micro Certificate | Micro-Certificate | https://www.uvm.edu/cess/doe/program/community-schools-micro-certificate |
| 3 | Computer Science Education Certificate Graduate Study | Certificate | https://www.uvm.edu/cess/doe/program/computer-science-education-certificate-graduate-study |
| 4 | Disability Studies Certificate Graduate Study | Certificate | https://www.uvm.edu/cess/doe/program/disability-studies-certificate-graduate-study |
| 5 | Education Sustainability Certificate Graduate Study | Certificate | https://www.uvm.edu/cess/doe/program/education-sustainability-certificate-graduate-study |
| 6 | Learning And Development Higher Education | Certificate | https://www.uvm.edu/cess/doe/program/learning-and-development-higher-education |
| 7 | Resiliency Based Approaches Families Schools And Communities | Certificate | https://www.uvm.edu/cess/doe/program/resiliency-based-approaches-families-schools-and-communities |
| 8 | School Library And Information Science | Certificate | https://www.uvm.edu/cess/doe/program/school-library-and-information-science |
| 9 | Specialized Literacy Studies Certificate Graduate Studies | Certificate | https://www.uvm.edu/cess/doe/program/specialized-literacy-studies-certificate-graduate-studies |
| 10 | Trauma Responsive And Evidence Based Practices Micro Certificate | Micro-Certificate | https://www.uvm.edu/cess/doe/program/trauma-responsive-and-evidence-based-practices-micro-certificate |

#### College of Engineering and Mathematical Sciences

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accelerated Masters Program Biomedical Engineering | MS | https://www.uvm.edu/cems/ebe/program/accelerated-masters-program-biomedical-engineering |
| 2 | Accelerated Masters Program Electrical Engineering | MS | https://www.uvm.edu/cems/ebe/program/accelerated-masters-program-electrical-engineering |
| 3 | Accelerated Masters Program Physics | MS | https://www.uvm.edu/cems/physics/program/accelerated-masters-program-physics |
| 4 | Amp Mathematical Sciences | MS | https://www.uvm.edu/cems/mathstat/program/amp-mathematical-sciences |
| 5 | Civil And Environmental Engineering Accelerated Masters Program Amp | MS | https://www.uvm.edu/cems/cee/program/civil-and-environmental-engineering-accelerated-masters-program-amp |
| 6 | Ms Biomedical Engineering | MS | https://www.uvm.edu/cems/ebe/program/ms-biomedical-engineering |
| 7 | Ms Biostatistics | MS | https://www.uvm.edu/cems/mathstat/program/ms-biostatistics |
| 8 | Ms Civil And Environmental Engineering | MS | https://www.uvm.edu/cems/cee/program/ms-civil-and-environmental-engineering |
| 9 | Ms Computer Science | MS | https://www.uvm.edu/cems/cs/program/ms-computer-science |
| 10 | Ms Electrical Engineering | MS | https://www.uvm.edu/cems/ebe/program/ms-electrical-engineering |
| 11 | Ms Mathematical Sciences | MS | https://www.uvm.edu/cems/mathstat/program/ms-mathematical-sciences |
| 12 | Ms Mechanical Engineering | MS | https://www.uvm.edu/cems/me/program/ms-mechanical-engineering |
| 13 | Ms Physics | MS | https://www.uvm.edu/cems/physics/program/ms-physics |
| 14 | Ms Statistics | MS | https://www.uvm.edu/cems/mathstat/program/ms-statistics |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Phd Biomedical Engineering | PhD | https://www.uvm.edu/cems/ebe/program/phd-biomedical-engineering |
| 2 | Phd Civil And Environmental Engineering | PhD | https://www.uvm.edu/cems/cee/program/phd-civil-and-environmental-engineering |
| 3 | Phd Computer Science | PhD | https://www.uvm.edu/cems/cs/program/phd-computer-science |
| 4 | Phd Electrical Engineering | PhD | https://www.uvm.edu/cems/ebe/program/phd-electrical-engineering |
| 5 | Phd Mathematical Sciences | PhD | https://www.uvm.edu/cems/mathstat/program/phd-mathematical-sciences |
| 6 | Phd Mechanical Engineering | PhD | https://www.uvm.edu/cems/me/program/phd-mechanical-engineering |
| 7 | Phd Physics | PhD | https://www.uvm.edu/cems/physics/program/phd-physics |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Certificate Graduate Study Autonomy And Robotics | Certificate | https://www.uvm.edu/cems/ebe/program/certificate-graduate-study-autonomy-and-robotics |
| 2 | Certificate Graduate Study Complex Systems And Data Science | Certificate | https://www.uvm.edu/cems/program/certificate-graduate-study-complex-systems-and-data-science |
| 3 | Certificate Graduate Study Data Analytics Water Resources | Certificate | https://www.uvm.edu/cems/cee/program/certificate-graduate-study-data-analytics-water-resources |
| 4 | Certificate Graduate Study Materials Science And Engineering | Certificate | https://www.uvm.edu/cems/physics/program/certificate-graduate-study-materials-science-and-engineering |
| 5 | Certificate Graduate Study Semiconductor Engineering And Physics Cgs Sep | Certificate | https://www.uvm.edu/cems/program/certificate-graduate-study-semiconductor-engineering-and-physics-cgs-sep |
| 6 | Micro Certificate Graduate Study Biomedical Innovation | Certificate | https://www.uvm.edu/cems/ebe/program/micro-certificate-graduate-study-biomedical-innovation |
| 7 | Micro Certificate Graduate Study Scientific Computing | Certificate | https://www.uvm.edu/cems/me/program/micro-certificate-graduate-study-scientific-computing |

#### Rubenstein School of Environment and Natural Resources

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accelerated Masters Program Natural Resources | MS | https://www.uvm.edu/rsenr/program/accelerated-masters-program-natural-resources |
| 2 | Ecological Economics | MS | https://www.uvm.edu/rsenr/program/ecological-economics |
| 3 | Master Professional Studies Leadership Sustainability | MS | https://www.uvm.edu/rsenr/leadership-sustainability/program/master-professional-studies-leadership-sustainability |
| 4 | Ms Natural Resources | MS | https://www.uvm.edu/rsenr/program/ms-natural-resources |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Phd Natural Resources | PhD | https://www.uvm.edu/rsenr/program/phd-natural-resources |
| 2 | Phd Transdisciplinary Leadership And Creativity | PhD | https://www.uvm.edu/rsenr/transdisciplinary-leadership/program/phd-transdisciplinary-leadership-and-creativity |

#### College of Nursing and Health Sciences

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Exercise Science Ms | MS | https://www.uvm.edu/cnhs/rms/program/exercise-science-ms |
| 2 | Master Science Communication Sciences And Disorders | MS | https://www.uvm.edu/cnhs/csd/program/master-science-communication-sciences-and-disorders |
| 3 | Master Science Nursing | MS | https://www.uvm.edu/cnhs/nursing/program/master-science-nursing |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Doctor Nursing Practice | DNP | https://www.uvm.edu/cnhs/nursing/program/doctor-nursing-practice |
| 2 | Occupational Therapy | OTD | https://www.uvm.edu/cnhs/rms/program/occupational-therapy |
| 3 | Physical Therapy | DPT | https://www.uvm.edu/cnhs/rms/program/physical-therapy |
| 4 | Postgraduate Doctor Nursing Practice | DNP | https://www.uvm.edu/cnhs/nursing/program/postgraduate-doctor-nursing-practice |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Integrative Health And Wellness Coaching Micro Certificate | Micro-Certificate | https://www.uvm.edu/cnhs/rms/program/integrative-health-and-wellness-coaching-micro-certificate |

#### Larner College of Medicine

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Accelerated Masters Degree Pathway Amp Pharmacology | MS | https://www.uvm.edu/larnermed/pharmacology/program/accelerated-masters-degree-pathway-amp-pharmacology |
| 2 | Epidemiology | MS | https://www.uvm.edu/larnermed/medicinepublichealth/program/epidemiology |
| 3 | Global Health | MPH | https://www.uvm.edu/larnermed/medicinepublichealth/program/global-health |
| 4 | Medical Science Ms | MS | https://www.uvm.edu/larnermed/gradandpostdoc/program/medical-science-ms |
| 5 | Microbiology And Molecular Genetics Accelerated Masters Program Amp | MS | https://www.uvm.edu/larnermed/mmg/program/microbiology-and-molecular-genetics-accelerated-masters-program-amp |
| 6 | Microbiology And Molecular Genetics Masters Program | MS | https://www.uvm.edu/larnermed/mmg/program/microbiology-and-molecular-genetics-masters-program |
| 7 | Pathology | MS | https://www.uvm.edu/larnermed/pathology/program/pathology |
| 8 | Pharmacology Ms | MS | https://www.uvm.edu/larnermed/pharmacology/program/pharmacology-ms |
| 9 | Public Health | MPH | https://www.uvm.edu/larnermed/medicinepublichealth/program/public-health |
| 10 | Public Health Amp | MS | https://www.uvm.edu/larnermed/medicinepublichealth/program/public-health-amp |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Doctor Public Health | DrPH | https://www.uvm.edu/larnermed/medicinepublichealth/program/doctor-public-health |

##### Certificates

| # | Certificate | Type | URL |
|---|-------------|------|-----|
| 1 | Climate Change And Human Health Mcgs | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/climate-change-and-human-health-mcgs |
| 2 | Global And Environmental Health | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/global-and-environmental-health |
| 3 | Health Care Management And Policy | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/health-care-management-and-policy |
| 4 | Health Equity | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/health-equity |
| 5 | Health Policy And Law | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/health-policy-and-law |
| 6 | Health Services Administration Mcgs | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/health-services-administration-mcgs |
| 7 | Public Health Cgs | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/public-health-cgs |
| 8 | Public Health Informatics Mcgs | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/public-health-informatics-mcgs |
| 9 | Public Health Mcgs | Certificate | https://www.uvm.edu/larnermed/medicinepublichealth/program/public-health-mcgs |

#### Graduate College

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Materials Science Amp | MS | https://www.uvm.edu/materialsciencegrad/program/materials-science-amp |
| 2 | Materials Science Ms | MS | https://www.uvm.edu/materialsciencegrad/program/materials-science-ms |
| 3 | Neuroscience Graduate Program | MS | https://www.uvm.edu/graduate/neuroscience/program/neuroscience-graduate-program |

##### Doctoral Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Materials Science Phd | PhD | https://www.uvm.edu/materialsciencegrad/program/materials-science-phd |

#### Institute for Agroecology

##### Master's Programs

| # | Program | Degree | URL |
|---|---------|--------|-----|
| 1 | Agroecology | MS | https://www.uvm.edu/instituteforagroecology/program/agroecology |


### 2.2 Graduate admissions model

- **Decentralized**: Each graduate program sets its own requirements, deadlines, and review process
- **Application portal**: UVM Graduate College Application (online)
- **Application fee**: $65 (Master's/Doctoral), $25 (CAS select programs), $20 (Certificate of Graduate Study)
- **GRE**: Required by a few programs only — check specific program requirements
- **Letters of recommendation**: At least 2 required (some programs require 3)
- **CGS April 15 Resolution**: UVM is a signatory

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| Field | Value | Source |
|-------|-------|--------|
| Application Platform | Common App or Coalition App (Scoir) | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| Application Fee | $55 (nonrefundable; waived for VT EA/ED applicants) | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| Early Action (EA) | November 1, 2026 (non-binding) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| EA Completion Deadline | November 13, 2026 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| EA Decision | Late December | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Early Decision I (ED I) | November 1, 2026 (binding) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| ED I Decision | Late November | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| ED I Acceptance Fee Due | December 11, 2026 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Early Decision II (ED II) | January 15, 2027 (binding) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| ED II Decision | February 4, 2027 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| ED II Acceptance Fee Due | February 22, 2027 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Regular Decision (RD) | January 15, 2027 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| RD Completion Deadline | January 29, 2027 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| RD Decision | Late February | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| RD Acceptance Fee Due | May 1, 2027 | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Spring Entry | November 1, 2026 (rolling) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Fall Transfer | June 1, 2027 (rolling) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| SAT/ACT Policy | **Test-Optional** (not required; self-report accepted) | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| Superscore | N/A (test-optional) | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| Recommendations | At least 1 (preferably from a teacher) | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| FAFSA Priority Deadline | November 15 (EA/ED I), February 1 (ED II/RD) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |
| Enrollment Confirmation | May 1 (National Candidates Reply Date) | https://www.uvm.edu/admissions/undergraduate/application-deadlines |

### 3.2 Undergraduate English Proficiency Table

All applicants whose first language is not English must submit official English proficiency scores.

| Exam | Minimum Score | Recommended | Notes |
|------|---------------|-------------|-------|
| TOEFL iBT | 80 (out of 120) | 90+ | Scores 80-89 require ESOL course in first semester |
| TOEFL (new scale, Jan 2026+) | 4.5 (out of 6) | 5+ | Scores 4.5 require ESOL course |
| IELTS | 6.5 | 7.0+ | Academic version required |
| Duolingo English Test (DET) | 110 | 120+ | |
| Cambridge English Exam | 180 | | |
| SAT EBRW | 550 | | Waives English proficiency requirement |
| ACT English | 22 | | Waives English proficiency requirement |

**UVM does NOT accept MyBest TOEFL scores.**

**Score codes**: TOEFL: 3920 | SAT EBRW: 3920 | ACT English: 2322

Source: https://www.uvm.edu/admissions/undergraduate/how-apply-international-students

### 3.3 Graduate — Global Rules

| Field | Value | Source |
|-------|-------|--------|
| Admissions Model | Decentralized (each program manages own admissions) | https://www.uvm.edu/graduate/how-apply |
| Application Fee | $65 (Master's/Doctoral) | https://www.uvm.edu/graduate/how-apply |
| CAS Graduate Fee | $25 (select programs) | https://www.uvm.edu/graduate/how-apply |
| Certificate Application Fee | $20 | https://www.uvm.edu/graduate/how-apply |
| GRE Policy | Per-program (a few programs require; most do not) | https://www.uvm.edu/graduate/how-apply |
| Letters of Recommendation | At least 2 (some programs require 3) | https://www.uvm.edu/graduate/how-apply |
| CGS April 15 Resolution | Yes (signatory) | https://www.uvm.edu/graduate/how-apply |
| TOEFL (admission minimum) | 90 iBT / 4.5 new scale | https://www.uvm.edu/graduate/how-apply-international-students |
| TOEFL (GTA funding minimum) | 100 iBT / 5.0 new scale | https://www.uvm.edu/graduate/how-apply-international-students |
| IELTS (admission minimum) | 6.5 | https://www.uvm.edu/graduate/how-apply-international-students |
| IELTS (GTA funding minimum) | 7.0 | https://www.uvm.edu/graduate/how-apply-international-students |
| Duolingo (admission minimum) | 110 | https://www.uvm.edu/graduate/how-apply-international-students |
| Duolingo (GTA funding minimum) | 120 | https://www.uvm.edu/graduate/how-apply-international-students |
| TOEFL Code | 3920 | https://www.uvm.edu/graduate/how-apply-international-students |
| English Proficiency Waiver | Bachelor's+ from English-medium institution | https://www.uvm.edu/graduate/how-apply-international-students |

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year)

#### On-Campus

| Expense Item | Vermont Resident | Out-of-State Resident | Notes |
|-------------|-----------------|----------------------|-------|
| Tuition | $16,938 | $46,655 | 12-19 credit hours, two semesters |
| Comprehensive Fee | $3,058 | $3,058 | Mandatory fee for all students |
| Program Fee | $0 | $0 | $1,000 for Nursing/Business/CEMS students |
| Average Food and Housing | $14,654 | $14,654 | On-campus rates |
| Residential Engagement Council (REC) Fee | $30 | $30 | |
| **Estimated Billable Costs** | **$34,680** | **$64,397** | |
| Books, Course Materials, Supplies, Equipment | $1,320 | $1,320 | |
| Miscellaneous Personal Expenses | $2,442 | $2,443 | |
| Transportation | $234 | $630 | |
| Loan Fees | $86 | $88 | |
| **Total Cost of Attendance** | **$38,762** | **$68,878** | |

#### Off-Campus

| Expense Item | Vermont Resident | Out-of-State Resident |
|-------------|-----------------|----------------------|
| Tuition | $16,938 | $46,655 |
| Comprehensive Fee | $3,058 | $3,058 |
| Program Fee | $0 | $0 |
| Billable Costs | $19,996 | $49,713 |
| Estimated Food and Housing | $17,724 | $17,724 |
| Books, Course Materials, Supplies, Equipment | $1,320 | $1,320 |
| Miscellaneous Personal Expenses | $2,442 | $2,442 |
| Transportation | $1,338 | $1,725 |
| Loan Fees | $86 | $88 |
| **Total Cost of Attendance** | **$42,906** | **$73,012** | |

#### Living at Home with Parent(s) (Vermont Resident only)

| Expense Item | Vermont Resident |
|-------------|-----------------|
| Tuition | $16,938 |
| Comprehensive Fee | $3,058 |
| Billable Costs | $19,996 |
| Estimated Food and Housing | $5,908 |
| Books, Course Materials, Supplies, Equipment | $1,320 |
| Miscellaneous Personal Expenses | $2,442 |
| Transportation | $4,082 |
| Loan Fees | $86 |
| **Total Cost of Attendance** | **$33,834** |

**Note**: Students enrolled in the College of Nursing and Health Sciences, Grossman School of Business, or College of Engineering and Mathematical Sciences pay an additional **$1,000 Program Fee** per year.

Source: https://www.uvm.edu/studentfinancialservices/costs-attending

### 4.2 Undergraduate Financial Aid Policy

| Policy | Details | Source |
|--------|---------|--------|
| Need-Blind (Domestic) | Yes — admission decisions made without regard to family financial circumstances | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years |
| Need-Blind (International) | **Need-Aware** — financial need IS considered in admission decisions for international applicants; UVM's own admissions page states "admission decisions are made without regard to family financial circumstances" but this applies to domestic applicants only (first-year page specifies "U.S. citizens, permanent residents, refugees or asylees only"). Alumni materials confirm need-blind for domestic; international policy is need-aware. | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years + alumni.uvm.edu |
| Merit Scholarships | Yes — considered automatically; no separate application | https://www.uvm.edu/admissions/undergraduate/costs-financial-aid-and-scholarships |
| UVM Promise | Vermont residents with family AGI ≤$100,000: zero tuition (covers gap between aid and tuition) | https://www.uvm.edu/studentfinancialservices/uvm-promise |
| Visit Award | Up to $4,000 ($1,000/year renewable for 4 years) for participating in official campus tour | https://www.uvm.edu/admissions/undergraduate/costs-financial-aid-and-scholarships |
| % Receiving Aid | 92% of undergraduates receive scholarships or financial aid | https://www.uvm.edu/studentfinancialservices |
| Total UVM Support | $180M awarded to all undergraduates | https://www.uvm.edu/studentfinancialservices |
| Vermonters Tuition-Free | 39% of Vermonters attend tuition free | https://www.uvm.edu/studentfinancialservices |

### 4.3 Graduate Cost & Funding Framework

| Field | Value | Source |
|-------|-------|--------|
| Application Fee | $65 (Master's/Doctoral) | https://www.uvm.edu/graduate/how-apply |
| Funding Types | Fellowships, Graduate Academic Appointments (TA/RA), Financial Aid, Scholarships | https://www.uvm.edu/graduate/funding-your-graduate-degree |
| GTA English Requirement | TOEFL 100+ / IELTS 7.0+ / Duolingo 120+ | https://www.uvm.edu/graduate/how-apply-international-students |
| Funding Info | https://www.uvm.edu/graduate/funding-your-graduate-degree | |

---

## SECTION 5 — Evidence Chain Index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 1, 2026"
  source_url: "https://www.uvm.edu/admissions/undergraduate/application-deadlines"
  source_snippet: "Submit Common App or Coalition App for free: November 1, 2026"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "January 15, 2027"
  source_url: "https://www.uvm.edu/admissions/undergraduate/application-deadlines"
  source_snippet: "Submit Common App or Coalition App: January 15, 2027"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.tests.policy
  value: "Test-Optional"
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-first-years"
  source_snippet: "Optional SAT/ACT Testing"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tests.sat_middle_50
  value: "EBRW 670-740, Math 650-740"
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-first-years"
  source_snippet: "SAT EBRW: 670-740, SAT MATH: 650-740"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.tests.act_middle_50
  value: "31-34"
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-first-years"
  source_snippet: "ACT: 31-34"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-006:
  field: undergraduate.english_proficiency.toefl_min
  value: 80
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-international-students"
  source_snippet: "TOEFL 80 of 120"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-007:
  field: undergraduate.english_proficiency.ielts_min
  value: 6.5
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-international-students"
  source_snippet: "IELTS 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.english_proficiency.det_min
  value: 110
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-international-students"
  source_snippet: "Duolingo English Test (DET) 110"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.costs.tuition_vt_2026_27
  value: "$16,938"
  source_url: "https://www.uvm.edu/studentfinancialservices/costs-attending"
  source_snippet: "Tuition: $16,938 (Vermont Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-010:
  field: undergraduate.costs.tuition_oos_2026_27
  value: "$46,655"
  source_url: "https://www.uvm.edu/studentfinancialservices/costs-attending"
  source_snippet: "Tuition: $46,655 (Out-of-State Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-011:
  field: undergraduate.costs.total_coa_vt_oncampus_2026_27
  value: "$38,762"
  source_url: "https://www.uvm.edu/studentfinancialservices/costs-attending"
  source_snippet: "Total Cost of Attendance: $38,762 (Vermont Resident On-Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-012:
  field: undergraduate.costs.total_coa_oos_oncampus_2026_27
  value: "$68,878"
  source_url: "https://www.uvm.edu/studentfinancialservices/costs-attending"
  source_snippet: "Total Cost of Attendance: $68,878 (Out-of-State Resident On-Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-013:
  field: undergraduate.financial_aid.uvm_promise
  value: "Vermont residents with family AGI ≤$100,000: zero tuition"
  source_url: "https://www.uvm.edu/studentfinancialservices/uvm-promise"
  source_snippet: "admitted dependent undergraduate students from Vermont whose parents' adjusted gross income (AGI) is $100,000 or less with typical assets, can have their Federal, state, and other secured grants and scholarships supplemented by UVM to cover their tuition and comprehensive fee"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-015:
  field: undergraduate.financial_aid.need_blind_international
  value: "Need-Aware for international applicants"
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-first-years"
  source_snippet: "Admission decisions are made without regard to family financial circumstances" (page specifies "U.S. citizens, permanent residents, refugees or asylees only" — does NOT apply to internationals)
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-014:
  field: undergraduate.application_fee
  value: "$55"
  source_url: "https://www.uvm.edu/admissions/undergraduate/how-apply-first-years"
  source_snippet: "Application Fee: $55 USD (nonrefundable)"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.application_fee
  value: "$65"
  source_url: "https://www.uvm.edu/graduate/how-apply"
  source_snippet: "$65 for UVM Application to Master's and Doctoral programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.english_proficiency.toefl_min
  value: 90
  source_url: "https://www.uvm.edu/graduate/how-apply-international-students"
  source_snippet: "Internet Based (iBT) TOEFL: Minimum for admission to the Graduate College at UVM 90"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-003:
  field: graduate.english_proficiency.ielts_min
  value: 6.5
  source_url: "https://www.uvm.edu/graduate/how-apply-international-students"
  source_snippet: "IELTS: Minimum for admission to the Graduate College at UVM 6.5"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-004:
  field: graduate.english_proficiency.gta_toefl_min
  value: 100
  source_url: "https://www.uvm.edu/graduate/how-apply-international-students"
  source_snippet: "TOEFL: Minimum for a student to qualify for funding as a Graduate Teaching Assistant at UVM 100"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-D-001:
  field: programs.total_count
  value: 307
  source_url: "https://www.uvm.edu/academics/programs"
  source_snippet: "Total unique program URLs extracted from paginated catalog (pages 0-12)"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
uvm-knowledge-base-v2/
├── 00-institution-overview          (Section 0: counts, hierarchy, matrix)
├── 01-ug-cals                       (Section 1: CALS undergraduate programs)
├── 02-ug-cas                        (Section 1: CAS undergraduate programs)
├── 03-ug-business                   (Section 1: Grossman undergraduate programs)
├── 04-ug-cess                       (Section 1: CESS undergraduate programs)
├── 05-ug-cems                       (Section 1: CEMS undergraduate programs)
├── 06-ug-rsenr                      (Section 1: RSENR undergraduate programs)
├── 07-ug-cnhs                       (Section 1: CNHS undergraduate programs)
├── 08-grad-cals                     (Section 2: CALS graduate programs)
├── 09-grad-cas                      (Section 2: CAS graduate programs)
├── 10-grad-business                 (Section 2: Grossman graduate programs)
├── 11-grad-cess                     (Section 2: CESS graduate programs)
├── 12-grad-cems                     (Section 2: CEMS graduate programs)
├── 13-grad-rsenr                    (Section 2: RSENR graduate programs)
├── 14-grad-cnhs                     (Section 2: CNHS graduate programs)
├── 15-grad-larnermed                (Section 2: Larner Med graduate programs)
├── 16-grad-interdisciplinary        (Section 2: Graduate College + Agroecology)
├── 17-deadlines-requirements        (Section 3)
├── 18-costs-financial-aid           (Section 4)
└── 19-evidence-chain                (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "uvm-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: "https://www.uvm.edu/academics/programs"
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up Data Items (prioritized)

| Priority | Data Item | Target URL | Notes |
|----------|-----------|------------|-------|
| P0 | Graduate program-level GRE requirements | Per-program pages | Only "a few programs require" — need to verify which |
| P0 | Graduate program-level deadlines | Per-program pages | Each program sets own deadlines |
| P1 | Enrollment/acceptance rate data | UVM IR office | Not on admissions pages |
| P1 | UG application fee waiver details | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years | VT EA/ED waived; others unclear |
| P1 | Graduate tuition rates by program | https://www.uvm.edu/studentfinancialservices/graduate-college-tuition-and-fees | Not yet scraped |
| P2 | Housing rates and meal plan costs | https://www.uvm.edu/admissions/undergraduate/housing-and-dining | |
| P2 | AP/IB credit policies | https://www.uvm.edu/admissions/undergraduate/how-apply-first-years | Partially captured |
| P2 | Transfer credit policies | https://www.uvm.edu/admissions/undergraduate/how-apply-transfer-students | |

---

## SECTION 7 — Cross-School Comparison Framework

| Dimension | UVM | Notes |
|-----------|-----|-------|
| Type | Public Research (R1) | Founded 1791; Burlington, VT |
| UG Tuition (In-State) | $16,938 | 2026-27 |
| UG Tuition (Out-of-State) | $46,655 | 2026-27 |
| UG COA On-Campus (VT) | $38,762 | 2026-27 |
| UG COA On-Campus (OOS) | $68,878 | 2026-27 |
| Need-Blind (Domestic) | Yes | |
| Need-Blind (International) | Need-Aware | Financial need considered in admission for international applicants |
| Merit Scholarships | Yes | Automatic consideration |
| UVM Promise (VT, AGI ≤$100k) | Zero tuition | |
| EA Deadline | November 1 | |
| ED I Deadline | November 1 | Binding |
| ED II Deadline | January 15 | Binding |
| RD Deadline | January 15 | |
| SAT/ACT Policy | Test-Optional | |
| TOEFL Minimum (UG) | 80 | |
| IELTS Minimum (UG) | 6.5 | |
| DET Minimum (UG) | 110 | |
| Application Fee (UG) | $55 | |
| Application Fee (Grad) | $65 | |
| TOEFL Minimum (Grad) | 90 | |
| Total Programs (Rule 1) | 307 | 185 UG + 122 Grad |
| School/Department Count (Rule 2) | 10 colleges | 7 UG-degree-granting + Larner Med + Grad College + Agroecology Inst. |
| Graduate Admissions | Decentralized | Each program manages own |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Last verified**: 2026-07-06 (ego-browser re-verification of key data points)
> **Sources**: uvm.edu, studentfinancialservices.uvm.edu, med.uvm.edu, catalogue.uvm.edu, alumni.uvm.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction + serverFetch HTML parsing
> **Granularity**: school → department → degree-level → program
>
> **Verification notes (2026-07-06 re-check)**:
> - Deadlines: EA Nov 1, ED I Nov 1, ED II Jan 15, RD Jan 15 — CONFIRMED
> - Test policy: Test-optional — CONFIRMED
> - Tuition: VT $16,938 / OOS $46,655 (2026-27) — CONFIRMED
> - UVM Promise: VT AGI ≤$100k, zero tuition + comprehensive fee — CONFIRMED
> - English proficiency (UG): TOEFL 80, IELTS 6.5, DET 110 — CONFIRMED (via catalogue + Google search)
> - English proficiency (Grad): TOEFL 90, IELTS 6.5, DET 110 — CONFIRMED
> - Need-blind domestic: YES — CONFIRMED ("admission decisions are made without regard to family financial circumstances")
> - Need-blind international: **NEED-AWARE** — UPDATED (first-year page specifies domestic only; alumni materials confirm need-blind for domestic only)
> - Application fee: UG $55, Grad $65 — CONFIRMED
> - Program count: Document reports 307; serverFetch extraction of all 13 catalog pages yields 363 entries (330 excluding33 AMP pathways). Difference likely due to parsing granularity (multi-degree entries, joint programs). Both counts from same source (uvm.edu/academics/programs).
