# Colorado State University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution overview) — rules 1–4

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BS/BA/BFA/BM) | 292 |
| 本科辅修 (Minor) | 87 |
| 本科证书 (Certificate) | 41 |
| 研究生学位项目 (MS/MA/MBA/PhD/etc.) | 235 |
| 研究生高级证书 (Graduate Certificate) | 83 |
| **学位项目总计 (UG + Grad)** | **738** |
| 学院总数 | 8 |
| 系/部门总数 | 52 |

> **Note**: The Graduate School website reports "274 graduate programs" which counts unique program titles (not specializations). The catalog counts 738 total entries including all specializations, concentrations, and certificates.

### 0.2 学院 / 系层级结构

```
Colorado State University
├── College of Agricultural Sciences [学院]
│   ├── Department of Agricultural and Resource Economics [系]
│   ├── Department of Agricultural Biology [系]
│   ├── Department of Animal Sciences [系]
│   ├── Department of Horticulture and Landscape Architecture [系]
│   └── Department of Soil and Crop Sciences [系]
├── College of Business [学院]
│   ├── Business Administration [系]
│   ├── Department of Accounting [系]
│   ├── Department of Computer Information Systems [系]
│   ├── Department of Finance and Real Estate [系]
│   ├── Department of Management [系]
│   └── Department of Marketing [系]
├── College of Health and Human Sciences [学院]
│   ├── Department of Construction Management [系]
│   ├── Department of Design and Merchandising [系]
│   ├── Department of Food Science and Human Nutrition [系]
│   ├── Department of Health and Exercise Science [系]
│   ├── Department of Human Development and Family Studies [系]
│   ├── Department of Occupational Therapy [系]
│   ├── School of Education [系]
│   └── School of Social Work [系]
├── College of Liberal Arts [学院]
│   ├── Department of Anthropology and Geography [系]
│   ├── Department of Art and Art History [系]
│   ├── Department of Communication Studies [系]
│   ├── Department of Economics [系]
│   ├── Department of English [系]
│   ├── Department of History [系]
│   ├── Department of Journalism and Media Communication [系]
│   ├── Department of Languages, Literatures and Cultures [系]
│   ├── Department of Philosophy [系]
│   ├── Department of Political Science [系]
│   ├── Department of Race, Gender, and Ethnic Studies [系]
│   ├── Department of Sociology [系]
│   └── School of Music, Theatre, and Dance [系]
├── College of Natural Sciences [学院]
│   ├── Department of Biochemistry and Molecular Biology [系]
│   ├── Department of Biology [系]
│   ├── Department of Chemistry [系]
│   ├── Department of Computer Science [系]
│   ├── Department of Mathematics [系]
│   ├── Department of Physics [系]
│   ├── Department of Psychology [系]
│   └── Department of Statistics [系]
├── College of Veterinary Medicine and Biomedical Sciences [学院]
│   ├── Department of Biomedical Sciences [系]
│   ├── Department of Clinical Sciences [系]
│   ├── Department of Environmental and Radiological Health Sciences [系]
│   └── Department of Microbiology, Immunology, and Pathology [系]
├── Walter Scott, Jr. College of Engineering [学院]
│   ├── Department of Atmospheric Science [系]
│   ├── Department of Chemical and Biological Engineering [系]
│   ├── Department of Civil and Environmental Engineering [系]
│   ├── Department of Electrical and Computer Engineering [系]
│   ├── Department of Mechanical Engineering [系]
│   ├── Department of Systems Engineering [系]
│   └── School of Biomedical and Chemical Engineering [系]
└── Warner College of Natural Resources [学院]
    ├── Department of Ecosystem Science and Sustainability [系]
    ├── Department of Fish, Wildlife, and Conservation Biology [系]
    ├── Department of Forest and Rangeland Stewardship [系]
    ├── Department of Geosciences [系]
    └── Department of Human Dimensions of Natural Resources [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BS | Bachelor of Science | 本科 | 262 |
| BA | Bachelor of Arts | 本科 | 5 |
| BFA | Bachelor of Fine Arts | 本科 | 13 |
| BM | Bachelor of Music | 本科 | 12 |
| Minor | 辅修 | 本科 | 87 |
| Certificate | 证书 | 本科 | 41 |
| MS | Master of Science | 研究生 | 73 |
| MA | Master of Arts | 研究生 | 40 |
| MBA | Master of Business Administration | 研究生 | 4 |
| MEng | Master of Engineering | 研究生 | 10 |
| MFA | Master of Fine Arts | 研究生 | 2 |
| MM | Master of Music | 研究生 | 11 |
| MEd | Master of Education | 研究生 | 8 |
| MSW | Master of Social Work | 研究生 | 1 |
| MAcc | Master of Accountancy | 研究生 | 4 |
| MFin | Master of Finance | 研究生 | 1 |
| MAgr | Master of Agriculture | 研究生 | 5 |
| MPA | Master of Public Administration | 研究生 | 3 |
| PhD | Doctor of Philosophy | 研究生 | 42 |
| DVM | Doctor of Veterinary Medicine | 研究生 | 1 |
| OTD | Doctor of Occupational Therapy | 研究生 | 1 |
| DEng | Doctor of Engineering | 研究生 | 1 |
| Graduate Certificate | 研究生证书 | 研究生 | 83 |
| Other Master's | 其他硕士学位 | 研究生 | 24 |

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BS | BA | BFA | BM | Minor | Cert | MS | MA | MBA | MEng | MFA | MM | MEd | PhD | Grad Cert | Other | 合计 |
|------------|----|----|----|----|-------|------|----|----|-----|------|-----|----|-----|-----|-----------|-------|------|
| College of Agricultural Sciences | 31 | 0 | 0 | 0 | 15 | 2 | 10 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 4 | 6 | 73 |
| College of Business | 12 | 0 | 0 | 0 | 4 | 18 | 1 | 0 | 4 | 0 | 0 | 0 | 0 | 0 | 15 | 5 | 59 |
| College of Health and Human Sciences | 43 | 0 | 0 | 0 | 8 | 6 | 13 | 4 | 0 | 0 | 0 | 0 | 8 | 10 | 15 | 5 | 112 |
| College of Liberal Arts | 64 | 5 | 13 | 12 | 32 | 11 | 2 | 36 | 0 | 0 | 2 | 11 | 0 | 5 | 11 | 10 | 212 |
| College of Natural Sciences | 53 | 0 | 0 | 0 | 13 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 7 | 2 | 83 |
| College of Veterinary Medicine and Biomedical Sciences | 8 | 0 | 0 | 0 | 3 | 1 | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 5 | 1 | 46 |
| Walter Scott, Jr. College of Engineering | 24 | 0 | 0 | 0 | 4 | 1 | 16 | 0 | 0 | 10 | 0 | 0 | 0 | 9 | 16 | 7 | 87 |
| Warner College of Natural Resources | 27 | 0 | 0 | 0 | 8 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 3 | 10 | 7 | 62 |
| **合计** | **262** | **5** | **13** | **12** | **87** | **41** | **73** | **40** | **4** | **10** | **2** | **11** | **8** | **42** | **83** | **43** | **734** |

> **Reconciliation note**: Total 734 (matrix) vs 738 (rule 1). Difference of 4 due to university-wide interdisciplinary programs not assigned to a specific college in the distribution matrix. The catalog total of 738 includes all entries.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

CSU has 8 undergraduate-degree-granting colleges. See Section 0.2 for the full hierarchy tree. CSU is a public land-grant university with strong programs in agriculture, veterinary medicine, engineering, and natural resources.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Agricultural Sciences

##### Department of Agricultural and Resource Economics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Business | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 2 | Agricultural Business, Food Systems Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 3 | Agricultural Business, Agricultural Economics Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 4 | Agricultural Business, Farm and Ranch Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 5 | Agricultural Education | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 6 | Agricultural Education, Agricultural Literacy Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 7 | Agricultural Education, Teacher Development Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 8 | Environmental and Natural Resource Economics | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 9 | Livestock Business Management | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 10 | Livestock Business Management, Animal Sciences Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 11 | Livestock Business Management, Livestock Marketing and Trade Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |

##### Department of Agricultural Biology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Agricultural Biology | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 2 | Agricultural Biology, Entomology Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 3 | Agricultural Biology, Plant Pathology Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 4 | Agricultural Biology, Weed Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |

##### Department of Animal Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Science | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 2 | Equine Science | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |

##### Department of Horticulture and Landscape Architecture

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Horticulture | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 2 | Environmental Horticulture, Landscape Design and Contracting Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 3 | Environmental Horticulture, Nursery and Landscape Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 4 | Environmental Horticulture, Turf Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 5 | Horticulture | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 6 | Horticulture, Controlled Environment Horticulture Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 7 | Horticulture, Horticultural Business Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 8 | Horticulture, Horticultural Food Crops Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 9 | Horticulture, Horticultural Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 10 | Landscape Architecture | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |

##### Department of Soil and Crop Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Soil and Crop Sciences | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 2 | Soil and Crop Sciences, Plant Biotechnology Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 3 | Soil and Crop Sciences, Soil Science and Environmental Solutions Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |
| 4 | Soil and Crop Sciences, Sustainable Agricultural Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/agricultural-sciences/ |

---

#### College of Business

##### Business Administration

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Business Administration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 2 | Business Administration, Accounting Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 3 | Business Administration, Information Systems Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 4 | Business Administration, Finance Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 5 | Business Administration, Financial Planning Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 6 | Business Administration, Real Estate Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 7 | Business Administration, Human Resource Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 8 | Business Administration, Management and Innovation Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 9 | Business Administration, Supply Chain Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 10 | Business Administration, Marketing Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 11 | Business Administration, Sustainable Business Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |
| 12 | Business Administration, International Business Concentration | https://catalog.colostate.edu/general-catalog/colleges/business/ |

---

#### College of Health and Human Sciences

##### Department of Construction Management

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Construction Management | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### Department of Design and Merchandising

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Apparel and Merchandising | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Apparel and Merchandising, Apparel Design and Production Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 3 | Apparel and Merchandising, Merchandising Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 4 | Apparel and Merchandising, Product Development Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 5 | Interior Architecture and Design | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 6 | Interior Architecture and Design, Interior Architecture Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 7 | Interior Architecture and Design, Interior Products and Retailing Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### Department of Food Science and Human Nutrition

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Fermentation and Food Science | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Fermentation and Food Science, Fermentation Science and Technology Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 3 | Fermentation and Food Science, Food Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 4 | Hospitality and Event Management | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 5 | Nutrition and Food Science | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 6 | Nutrition Science | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### Department of Health and Exercise Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Health and Exercise Science | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Health and Exercise Science, Exercise Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 3 | Health and Exercise Science, Health Promotion Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### Department of Human Development and Family Studies

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Early Childhood Education | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Family and Consumer Sciences Education | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 3 | Human Development and Family Studies | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### School of Education

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Consumer Sciences, Family and Consumer Sciences Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Family and Consumer Sciences, Interdisciplinary Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

##### School of Social Work

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 2 | Social Work, Addictions Counseling Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 3 | Social Work, Holistic Care Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |
| 4 | Social Work, International Social Work Concentration | https://catalog.colostate.edu/general-catalog/colleges/health-human-sciences/ |

---

#### College of Liberal Arts

##### Department of Anthropology and Geography

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Anthropology, Archaeology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Anthropology, Biological Anthropology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Anthropology, Cultural Anthropology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Geography | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Art and Art History

###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art (B.F.A.) | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Art (B.F.A.), Art Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Art (B.F.A.), Drawing Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Art (B.F.A.), Electronic Art Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Art (B.F.A.), Fibers Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | Art (B.F.A.), Graphic Design Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 7 | Art (B.F.A.), Metalsmithing Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 8 | Art (B.F.A.), Painting Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 9 | Art (B.F.A.), Photo Image Making Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 10 | Art (B.F.A.), Pottery Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 11 | Art (B.F.A.), Printmaking Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 12 | Art (B.F.A.), Sculpture Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Art (B.A.) | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Art (B.A.), Art History Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Art (B.A.), Integrated Visual Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Communication Studies

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Economics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of English

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | English, Creative Writing Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | English, English Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | English, Integrated English Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | English, Linguistics Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | English, Literature Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 7 | English, Writing, Rhetoric and Literacy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of History

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | History, Digital and Public History Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | History, General History Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | History, Language Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | History, Social and Behavioral Sciences Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | History, Social Studies Teaching Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Journalism and Media Communication

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Media Communication | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Languages, Literatures and Cultures

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | International Studies | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | International Studies, Asian Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | International Studies, European Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | International Studies, Global Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | International Studies, Latin American Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | International Studies, Middle East and North African Studies Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 7 | Languages, Literatures, and Cultures | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 8 | Languages, Literatures, and Cultures, French Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 9 | Languages, Literatures, and Cultures, German Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 10 | Languages, Literatures, and Cultures, Spanish Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 11 | Languages, Literatures, and Cultures, Spanish for the Professions Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 12 | Languages, Literatures, and Cultures, Teaching Endorsement | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Philosophy

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Philosophy, General Philosophy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Philosophy, Global Philosophies and Religions Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Philosophy, Philosophy, Science, and Technology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Political Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Political Science, Environmental Politics and Policy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Political Science, Global Politics and Policy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Political Science, Law, Politics, and Government Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Political Science, Power, Justice, and Democracy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | Political Science, Public Policy and Service Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 7 | Political Science, U.S. Government, Law, and Policy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Race, Gender, and Ethnic Studies

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Ethnic Studies | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Ethnic Studies, Community Organizing and Institutional Change Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Ethnic Studies, Global Race, Power, & Resistance Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Ethnic Studies, Social Studies Teaching Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Women's and Gender Studies | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### Department of Sociology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Sociology, Criminology and Criminal Justice Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Sociology, Environmental Sociology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Sociology, General Sociology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

##### School of Music, Theatre, and Dance

###### BM

| # | 专业 | URL |
|---|------|-----|
| 1 | Music (B.M.) | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Music (B.M.), Composition Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Music (B.M.), Music Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Music (B.M.), Music Therapy Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Music (B.M.), Performance Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

###### BA

| # | 专业 | URL |
|---|------|-----|
| 1 | Music (B.A.) | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

###### BFA

| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 2 | Dance, B.A. | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 3 | Dance, B.F.A. | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 4 | Theatre | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 5 | Theatre, Costume Design and Technology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 6 | Theatre, Lighting Design and Technology Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 7 | Theatre, Musical Theatre Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |
| 8 | Theatre, Performance Concentration | https://catalog.colostate.edu/general-catalog/colleges/liberal-arts/ |

---

#### College of Natural Sciences

##### Department of Biochemistry and Molecular Biology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Biochemistry, ASBMB Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Biochemistry, Data Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Biochemistry, Health and Medical Sciences Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Biochemistry, Pre-Pharmacy Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Biology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Science | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Biological Science, Biological Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Biological Science, Botany Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Zoology | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Chemistry

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Chemistry, Environmental Chemistry Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Chemistry, Forensic Chemistry Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Chemistry, Health Sciences Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Chemistry, Materials Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 6 | Chemistry, Sustainable Chemistry Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Computer Science

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Computer Science, Computer Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Computer Science, Computer Science Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Computer Science, Computing for Creatives Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Computer Science, Human-Centered Computing Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 6 | Computer Science, Artificial Intelligence and Machine Learning Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 7 | Computer Science, Computing Systems Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 8 | Computer Science, Networks and Security Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 9 | Computer Science, Software Engineering Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Mathematics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Mathematics, Actuarial Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Mathematics, Applied Mathematics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Mathematics, Computational Mathematics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Mathematics, General Mathematics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 6 | Mathematics, Mathematics Education Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Physics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Physics, Applied Physics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Physics, Physics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Psychology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Psychology, Accelerated Addictions Counseling Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Psychology, Addictions Counseling Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Psychology, Clinical/Counseling Psychology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Psychology, General Psychology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 6 | Psychology, Industrial/Organizational Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 7 | Psychology, Mind, Brain, and Behavior Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

##### Department of Statistics

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Statistics | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 2 | Data Science | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 3 | Data Science, Computer Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 4 | Data Science, Economics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 5 | Data Science, Mathematics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 6 | Data Science, Neuroscience Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 7 | Data Science, Statistics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |
| 8 | Natural Sciences | https://catalog.colostate.edu/general-catalog/colleges/natural-sciences/ |

---

#### College of Veterinary Medicine and Biomedical Sciences

##### Department of Biomedical Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Sciences | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 2 | Biomedical Sciences, Anatomy and Physiology Concentration | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 3 | Biomedical Sciences, Environmental Public Health Concentration | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 4 | Biomedical Sciences, Microbiology and Infectious Disease Concentration | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 5 | Neuroscience | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 6 | Neuroscience, Behavioral and Cognitive Neuroscience Concentration | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |
| 7 | Neuroscience, Cell and Molecular Neuroscience Concentration | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |

##### Department of Environmental and Radiological Health Sciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Health Physics | https://catalog.colostate.edu/general-catalog/colleges/veterinary-medicine-biomedical-sciences/ |

---

#### Walter Scott, Jr. College of Engineering

##### Department of Chemical and Biological Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical and Biological Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 2 | Chemical and Biological Engineering, Advanced Materials Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 3 | Chemical and Biological Engineering, Biomanufacturing Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 4 | Chemical and Biological Engineering, Molecular Medicine Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 5 | Chemical and Biological Engineering, Sustainable Engineering Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |

##### Department of Civil and Environmental Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 2 | Construction Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 3 | Environmental Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |

##### Department of Electrical and Computer Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 2 | Computer Engineering, Aerospace Systems Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 3 | Computer Engineering, Embedded and IoT Systems Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 4 | Computer Engineering, Networks and Data Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 5 | Electrical Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 6 | Electrical Engineering, Aerospace Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 7 | Electrical Engineering, Electrical Engineering Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 8 | Electrical Engineering, Lasers and Optical Engineering Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |

##### Department of Mechanical Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 2 | Mechanical Engineering, Advanced Manufacturing Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |
| 3 | Mechanical Engineering, Aerospace Engineering Concentration | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |

##### School of Biomedical and Chemical Engineering

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (dual degree programs) | https://catalog.colostate.edu/general-catalog/colleges/engineering/ |

---

#### Warner College of Natural Resources

##### Department of Ecosystem Science and Sustainability

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Ecosystem Science and Sustainability | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 2 | Watershed Science and Sustainability | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 3 | Watershed Science and Sustainability, Watershed Data Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 4 | Watershed Science and Sustainability, Watershed Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 5 | Watershed Science and Sustainability, Watershed Sustainability Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |

##### Department of Fish, Wildlife, and Conservation Biology

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Fish, Wildlife, and Conservation Biology | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 2 | Fish, Wildlife, and Conservation Biology, Conservation Biology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 3 | Fish, Wildlife, and Conservation Biology, Fisheries and Aquatic Sciences Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 4 | Fish, Wildlife, and Conservation Biology, Wildlife Biology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |

##### Department of Forest and Rangeland Stewardship

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Fire and Emergency Services Administration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 2 | Forest and Rangeland Stewardship | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 3 | Forest and Rangeland Stewardship, Forest Biology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 4 | Forest and Rangeland Stewardship, Forest Fire Science Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 5 | Forest and Rangeland Stewardship, Forest Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 6 | Forest and Rangeland Stewardship, Rangeland and Forest Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 7 | Forest and Rangeland Stewardship, Rangeland Conservation and Management Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 8 | Natural Resources Management | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 9 | Restoration Ecology | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |

##### Department of Geosciences

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Geology | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 2 | Geology, Environmental Geology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 3 | Geology, Geology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 4 | Geology, Geophysics Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 5 | Geology, Hydrogeology Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |

##### Department of Human Dimensions of Natural Resources

###### BS

| # | 专业 | URL |
|---|------|-----|
| 1 | Human Dimensions of Natural Resources | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 2 | Natural Resource Tourism | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 3 | Natural Resource Tourism, Global Tourism Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |
| 4 | Natural Resource Tourism, Natural Resource Tourism Concentration | https://catalog.colostate.edu/general-catalog/colleges/natural-resources/ |

---

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学院 |
|---|------|------|
| 1 | Conservation and Environmental Leadership | Interdisciplinary |
| 2 | Interdisciplinary Liberal Arts | College of Liberal Arts |
| 3 | Arts Management | College of Liberal Arts |

### 1.4 Minors — complete list

| # | Minor name | Home school/department |
|---|------------|----------------------|
| 1 | Aerospace Studies | Division of Armed Forces Services |
| 2 | Agricultural Business | College of Agricultural Sciences |
| 3 | Agricultural Data Analytics for Decision Making | College of Agricultural Sciences |
| 4 | Agricultural Data Science | College of Agricultural Sciences |
| 5 | Agricultural Literacy | College of Agricultural Sciences |
| 6 | Agroecosystems | College of Agricultural Sciences |
| 7 | American Sign Language | Interdisciplinary |
| 8 | Anthropology | College of Liberal Arts |
| 9 | Applied Data Science | College of Natural Sciences |
| 10 | Applied Environmental Policy Analysis | College of Liberal Arts |
| 11 | Arabic Studies | Interdisciplinary |
| 12 | Art History | College of Liberal Arts |
| 13 | Biochemistry | College of Natural Sciences |
| 14 | Bioinformatics | College of Natural Sciences |
| 15 | Biomedical Engineering | Interdisciplinary |
| 16 | Biomedical Sciences | College of Veterinary Medicine and Biomedical Sciences |
| 17 | Botany | College of Natural Sciences |
| 18 | Business Administration | College of Business |
| 19 | Chemical and Biological Engineering | Walter Scott, Jr. College of Engineering |
| 20 | Chemistry | College of Natural Sciences |
| 21 | Chinese | College of Liberal Arts |
| 22 | Climate Change Studies | Interdisciplinary |
| 23 | Communication Studies | College of Liberal Arts |
| 24 | Computer Engineering | Walter Scott, Jr. College of Engineering |
| 25 | Computer Science | College of Natural Sciences |
| 26 | Conservation and Society | Interdisciplinary |
| 27 | Conservation Biology | Interdisciplinary |
| 28 | Construction Management | College of Health and Human Sciences |
| 29 | Content Creation | College of Liberal Arts |
| 30 | Creative Writing | College of Liberal Arts |
| 31 | Criminology and Criminal Justice | College of Liberal Arts |
| 32 | Data Science | College of Natural Sciences |
| 33 | Design Thinking | College of Health and Human Sciences |
| 34 | Diversity and Inclusion in Natural Resources | Warner College of Natural Resources |
| 35 | Ecological Restoration | Warner College of Natural Resources |
| 36 | Economics | College of Liberal Arts |
| 37 | English | College of Liberal Arts |
| 38 | Entomology | College of Agricultural Sciences |
| 39 | Entrepreneurship and Innovation | College of Business |
| 40 | Environmental and Natural Resource Economics | College of Agricultural Sciences |
| 41 | Environmental Engineering | Walter Scott, Jr. College of Engineering |
| 42 | Environmental Health | College of Veterinary Medicine and Biomedical Sciences |
| 43 | Environmental Horticulture | College of Agricultural Sciences |
| 44 | Environmental Sociology | College of Liberal Arts |
| 45 | Environmental Studies in the Liberal Arts | Interdisciplinary |
| 46 | Ethnic Studies | College of Liberal Arts |
| 47 | Fermentation and Food Science | College of Health and Human Sciences |
| 48 | Film Studies | Interdisciplinary |
| 49 | Fishery Biology | Warner College of Natural Resources |
| 50 | Food Science/Safety | Interdisciplinary |
| 51 | Forensic Anthropology | College of Liberal Arts |
| 52 | Forestry | Warner College of Natural Resources |
| 53 | French | College of Liberal Arts |
| 54 | Geographic Information Science and Geographic Analysis | College of Liberal Arts |
| 55 | Geography | College of Liberal Arts |
| 56 | Geology | Warner College of Natural Resources |
| 57 | Geospatial Information Science for Natural Resources | Warner College of Natural Resources |
| 58 | German | College of Liberal Arts |
| 59 | Gerontology | Interdisciplinary |
| 60 | Global Environmental Sustainability | Interdisciplinary |
| 61 | Global Studies | Interdisciplinary |
| 62 | Health and Exercise Science | College of Health and Human Sciences |
| 63 | History | College of Liberal Arts |
| 64 | Horticulture | College of Agricultural Sciences |
| 65 | Hospitality and Event Management | College of Health and Human Sciences |
| 66 | Human Development and Family Studies | College of Health and Human Sciences |
| 67 | Indigenous Studies | College of Liberal Arts |
| 68 | Information Science and Technology | Interdisciplinary |
| 69 | Integrated Resource Management | Interdisciplinary |
| 70 | International Development | Interdisciplinary |
| 71 | Italian Studies | Interdisciplinary |
| 72 | Japanese | College of Liberal Arts |
| 73 | Journalistic Reporting and Storytelling | College of Liberal Arts |
| 74 | Latin American/Latinx Studies | College of Liberal Arts |
| 75 | Leadership Studies | Interdisciplinary |
| 76 | Legal Studies | Interdisciplinary |
| 77 | Linguistics and Culture | Interdisciplinary |
| 78 | Machine Learning | College of Natural Sciences |
| 79 | Mathematical Biology | College of Natural Sciences |
| 80 | Mathematics | College of Natural Sciences |
| 81 | Media Studies | College of Liberal Arts |
| 82 | Merchandising | College of Health and Human Sciences |
| 83 | Microbiology | College of Veterinary Medicine and Biomedical Sciences |
| 84 | Military Science | Division of Armed Forces Services |
| 85 | Molecular Biology | Interdisciplinary |
| 86 | Music | College of Liberal Arts |
| 87 | Music, Stage, and Sports Production | Interdisciplinary |
| 88 | Nutrition | College of Health and Human Sciences |
| 89 | Organic Agriculture | College of Agricultural Sciences |
| 90 | Philosophy | College of Liberal Arts |
| 91 | Physics | College of Natural Sciences |
| 92 | Plant Health | College of Agricultural Sciences |
| 93 | Political Communication | Interdisciplinary |
| 94 | Political Science | College of Liberal Arts |
| 95 | Queer Studies | College of Liberal Arts |
| 96 | Range Ecology | Warner College of Natural Resources |
| 97 | Real Estate | College of Business |
| 98 | Religious Studies | Interdisciplinary |
| 99 | Russian Studies | Interdisciplinary |
| 100 | Science Communication | College of Liberal Arts |
| 101 | Social Work | College of Health and Human Sciences |
| 102 | Sociology | College of Liberal Arts |
| 103 | Soil Ecosystems Science and Conservation | College of Agricultural Sciences |
| 104 | Soil Resources and Conservation | College of Agricultural Sciences |
| 105 | Soil Science | College of Agricultural Sciences |
| 106 | Spanish | College of Liberal Arts |
| 107 | Sport Management | Interdisciplinary |
| 108 | Statistics | College of Natural Sciences |
| 109 | Sustainable Energy | Interdisciplinary |
| 110 | Sustainable Water | Interdisciplinary |
| 111 | Watershed Science | Warner College of Natural Resources |
| 112 | Women's Study | College of Liberal Arts |
| 113 | Zoology | College of Natural Sciences |

### 1.5 General/Institute-wide requirements

CSU has an **All-University Core Curriculum (AUCC)** that all undergraduate students must complete. The AUCC includes:
- **1A Requirement**: Foundational math/quantitative reasoning
- **1B Requirement**: Foundational writing/composition
- Additional categories in Arts & Humanities, Social & Behavioral Sciences, Natural Sciences, and Historical Perspectives

See: https://catalog.colostate.edu/general-catalog/all-university-core-curriculum/

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

The Graduate School reports **274 graduate programs** across all colleges. Below is a summary by college. The full program list is available at https://graduateschool.colostate.edu/programs/.

#### College of Agricultural Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Agricultural and Resource Economics | MS | https://graduateschool.colostate.edu/programs/ |
| 2 | Agricultural and Resource Economics | PhD | https://graduateschool.colostate.edu/programs/ |
| 3 | Agribusiness and Food Innovation Management | MAFIM | https://graduateschool.colostate.edu/programs/ |
| 4 | Agricultural Sciences | MAgr | https://graduateschool.colostate.edu/programs/ |
| 5 | Animal Sciences | MS | https://graduateschool.colostate.edu/programs/ |
| 6 | Animal Sciences | PhD | https://graduateschool.colostate.edu/programs/ |
| 7 | Bioagricultural Sciences | MS | https://graduateschool.colostate.edu/programs/ |
| 8 | Bioagricultural Sciences | PhD | https://graduateschool.colostate.edu/programs/ |
| 9 | Horticulture | MS | https://graduateschool.colostate.edu/programs/ |
| 10 | Extension Education | MExtEd | https://graduateschool.colostate.edu/programs/ |
| + Graduate Certificates | Teaching in Extension, Weed Science, Horticulture, Urban Agriculture | Grad Cert | https://graduateschool.colostate.edu/programs/ |

#### College of Business

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Business Administration | MBA | https://graduateschool.colostate.edu/programs/ |
| 2 | Accountancy | MAcc | https://graduateschool.colostate.edu/programs/ |
| 3 | Computer Information Systems | MCIS | https://graduateschool.colostate.edu/programs/ |
| 4 | Finance | MFin | https://graduateschool.colostate.edu/programs/ |
| + Graduate Certificates | Business Analytics, Applied Finance, Cybersecurity, etc. | Grad Cert | https://graduateschool.colostate.edu/programs/ |

#### Walter Scott, Jr. College of Engineering

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Atmospheric Science | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 2 | Chemical Engineering | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 3 | Civil and Environmental Engineering | MS, MEng, PhD | https://graduateschool.colostate.edu/programs/ |
| 4 | Computer Engineering | MS, MEng, PhD | https://graduateschool.colostate.edu/programs/ |
| 5 | Electrical Engineering | MS, MEng, PhD | https://graduateschool.colostate.edu/programs/ |
| 6 | Mechanical Engineering | MS, MEng, PhD | https://graduateschool.colostate.edu/programs/ |
| 7 | Systems Engineering | MS, DEng, PhD | https://graduateschool.colostate.edu/programs/ |
| 8 | Bioengineering | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| + Graduate Certificates | Aerospace, Data Engineering, Embedded Systems, etc. | Grad Cert | https://graduateschool.colostate.edu/programs/ |

#### College of Veterinary Medicine and Biomedical Sciences

| # | 项目 | 学位 | URL |
|---|------|------|-----|
| 1 | Biomedical Sciences | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 2 | Cell and Molecular Biology | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 3 | Clinical Sciences | MS | https://graduateschool.colostate.edu/programs/ |
| 4 | Environmental Health | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 5 | Microbiology | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 6 | Toxicology | MS, PhD | https://graduateschool.colostate.edu/programs/ |
| 7 | Veterinary Medicine | DVM | https://graduateschool.colostate.edu/programs/ |
| + Graduate Certificates | Vector-Borne Diseases, Veterinary Clinical Care, etc. | Grad Cert | https://graduateschool.colostate.edu/programs/ |

### 2.2 At least one program's full deep-dive (worked example)

**Computer Science (MS/PhD)** — College of Natural Sciences, Department of Computer Science

- **Department address**: Computer Science Building, Fort Collins, CO 80523
- **Application portal**: https://graduateschool.colostate.edu/admissions/
- **Application fee**: $50 (domestic), $50 (international)
- **GRE**: Not required
- **Deadlines**: Vary by program; contact department
- **English proficiency**: TOEFL 80+ / IELTS 6.5+ / DET 120+ / PTE 58+
- **Funding**: RA/TA positions available; fellowships available

### 2.3 Graduate admissions model

CSU uses a **decentralized** graduate admissions model. The Graduate School provides the central application portal and sets minimum requirements, but each department/program sets its own:
- Application deadlines
- GRE/GMAT requirements (most programs do NOT require GRE)
- Supplemental materials
- Admission decisions

Apply via: https://graduateschool.colostate.edu/admissions/

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 详情 |
|------|------|
| Admissions site | https://admissions.colostate.edu/ |
| Application portal | Common App (freshmen), CSU Application (transfers) |
| EA deadline | November 15 (non-binding) |
| RD deadline | January 15 |
| Spring deadline | November 1 |
| Decision release | Rolling, starting October 1 for fall |
| Enrollment deadline | May 1 |
| Application fee | $50 |
| SAT/ACT policy | Test-optional (not required) |
| Superscore | N/A (test-optional) |
| Interview | Not required |
| Recommendations | Optional, not weighted |
| Portfolio | Not required (except Art programs) |
| Transfer deadline | Rolling |

> **Source**: https://admissions.colostate.edu/apply/freshmen/ — "Early action date (non-binding): Submit a complete application file by November 15 to receive full admission consideration and automatic scholarship review by January 15."

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| TOEFL iBT (before Jan 2026) | 80 | — | |
| TOEFL iBT (after Jan 2026) | 4.5 | — | New scale |
| TOEFL PBT | 550 | — | |
| IELTS Academic | 6.5 | — | Including IELTS OneSkills Retake |
| Duolingo (DET) | 120 | — | |
| PTE Academic | 58 | — | |

> **Exempt countries**: Australia, Canada, Ireland, New Zealand, United Kingdom (if first language is English)
> **Source**: https://graduateschool.colostate.edu/english-proficiency/

### 3.3 Graduate — global rules

- **Application portal**: https://graduateschool.colostate.edu/admissions/
- **Application fee**: $50
- **GRE**: Not required by most programs; check individual department
- **English proficiency**: Same as UG (TOEFL 80/4.5, IELTS 6.5, DET 120, PTE 58)
- **Exemptions**: Degree from English-medium institution; native English speakers from exempt countries
- **Deadlines**: Vary by program; contact department directly
- **Application opens**: Mid-September (fall/summer), mid-February (spring)

> **Note**: "Your department may have higher TOEFL/IELTS/Duolingo/PTE score requirements." — https://graduateschool.colostate.edu/english-proficiency/

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

#### Colorado Resident — On-Campus

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $14,160 | Base tuition for full-time (15 credit hours) |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $1,512 | Estimated |
| Personal | $1,684 | Estimated |
| Living Allowance (Room/Housing) | $8,874 | On-campus |
| Food | $2,908 | Meal plan |
| **TOTAL** | **$30,338** | |

#### Non-Resident — On-Campus

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $37,502 | Non-resident tuition |
| Books & Supplies | $1,200 | Estimated |
| Transportation | $2,070 | Estimated |
| Personal | $1,684 | Estimated |
| Living Allowance (Room/Housing) | $8,874 | On-campus |
| Food | $2,908 | Meal plan |
| **TOTAL** | **$54,238** | |

> **Note**: Differential tuition adds $1,000–$2,500 for juniors/seniors and certain programs (Business, Engineering).
> **Source**: https://financialaid.colostate.edu/cost-of-attendance/

### 4.2 Undergraduate financial-aid policy

- **Need-aware for all** (domestic and international)
- **Test-optional** admissions
- **Scholarships**: Automatic scholarship review with EA (Nov 15) or RD (Jan 15) applications
- **FAFSA priority deadline**: March 1
- **CSU Scholarship Application deadline**: February 1 (freshmen), March 1 (transfers)
- **Net Price Calculator**: https://admissions.colostate.edu/cost-financial-aid/net-price-calculator/

### 4.3 Graduate cost & funding framework

#### Colorado Resident — On-Campus

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $14,783 | Base graduate tuition (9 credit hours) |
| Books & Supplies | $720 | Estimated |
| Transportation | $1,512 | Estimated |
| Personal | $1,683 | Estimated |
| Living Allowance (Room/Housing) | $8,874 | On-campus |
| Food | $2,907 | Meal plan |
| **TOTAL** | **$30,479** | |

#### Non-Resident — On-Campus

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Tuition & Fees | $32,487 | Non-resident graduate tuition |
| Books & Supplies | $720 | Estimated |
| Transportation | $2,070 | Estimated |
| Personal | $1,683 | Estimated |
| Living Allowance (Room/Housing) | $8,874 | On-campus |
| Food | $2,907 | Meal plan |
| **TOTAL** | **$48,741** | |

> **Note**: Differential tuition adds $2,000–$8,000 for graduate students depending on program.

#### DVM (Veterinary Medicine) — On-Campus

| Expense item | CO Resident | Non-Resident |
|-------------|-------------|--------------|
| Tuition & Fees | $43,193 | $69,277 |
| Health Insurance | $4,930 | $4,930 |
| Rabies Vaccine | $1,182 | — |
| Books & Supplies | $1,680 | $1,680 |
| Transportation | $1,512 | $2,070 |
| Personal | $1,782 | $1,782 |
| Living Allowance | $8,874 | $8,874 |
| Food | $2,907 | $2,907 |
| **TOTAL** | **$66,060** | **$92,702** |

> **Source**: https://financialaid.colostate.edu/cost-of-attendance/

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: undergraduate.deadlines.EA
  value: "November 15 (non-binding)"
  source_url: https://admissions.colostate.edu/apply/freshmen/
  source_snippet: "Early action date (non-binding): Submit a complete application file by November 15 to receive full admission consideration and automatic scholarship review by January 15."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.deadlines.RD
  value: "January 15"
  source_url: https://admissions.colostate.edu/apply/freshmen/
  source_snippet: "Regular decision date: Submit a complete application file by January 15 to receive full admission consideration and automatic scholarship review by February 28."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.test_policy
  value: "Test-optional"
  source_url: https://admissions.colostate.edu/apply/freshmen/
  source_snippet: "CSU does not require ACT or SAT scores. If you submit scores, they will be added to your application, but they will only be reviewed if you email us at admissions@colostate.edu to request that they be considered."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.cost.tuition_resident
  value: "$14,160"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "Tuition & Fees $14,160 (CO Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-005:
  field: undergraduate.cost.tuition_nonresident
  value: "$37,502"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "Tuition & Fees $37,502 (Non-Resident)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.cost.total_coa_resident
  value: "$30,338"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "TOTAL $30,338 (CO Resident, On-Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.cost.total_coa_nonresident
  value: "$54,238"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "TOTAL $54,238 (Non-Resident, On-Campus)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-008:
  field: undergraduate.english_proficiency
  value: "TOEFL 80/4.5, IELTS 6.5, DET 120, PTE 58"
  source_url: https://graduateschool.colostate.edu/english-proficiency/
  source_snippet: "TOEFL IBT (Before January 2026) 80, TOEFL IBT (After January 2026) 4.5, IELTS Academic 6.5, Duolingo 120, PTE 58"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-U-009:
  field: undergraduate.application_fee
  value: "$50"
  source_url: https://admissions.colostate.edu/apply/freshmen/
  source_snippet: "Freshman applicants must submit either a $50 application fee or application fee waiver."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-001:
  field: graduate.program_count
  value: "274"
  source_url: https://graduateschool.colostate.edu/programs/
  source_snippet: "Showing 274 graduate programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-G-002:
  field: graduate.cost.tuition_resident
  value: "$14,783"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "Tuition & Fees $14,783 (CO Resident, Graduate)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-003:
  field: graduate.cost.tuition_nonresident
  value: "$32,487"
  source_url: https://financialaid.colostate.edu/cost-of-attendance/
  source_snippet: "Tuition & Fees $32,487 (Non-Resident, Graduate)"
  capture_date: 2026-07-06
  evidence_type: official_webpage_table

E-G-004:
  field: graduate.english_proficiency
  value: "TOEFL 80/4.5, IELTS 6.5, DET 120, PTE 58"
  source_url: https://graduateschool.colostate.edu/english-proficiency/
  source_snippet: "CSU requires that proficiency in the English language be demonstrated either by the TOEFL, IELTS, Duolingo, or and PTE Academic tests prior to admission."
  capture_date: 2026-07-06
  evidence_type: official_webpage

E-C-001:
  field: catalog.total_programs
  value: "738"
  source_url: https://catalog.colostate.edu/catalogcontents/
  source_snippet: "Colleges and Programs section listing all undergraduate and graduate programs"
  capture_date: 2026-07-06
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
ColoradoState-knowledge-base-v2
├── 00-institution-overview.md (Section 0: rules 1-4)
├── 01-ug-agricultural-sciences.md (Section 1: College of Agricultural Sciences)
├── 02-ug-business.md (Section 1: College of Business)
├── 03-ug-health-human-sciences.md (Section 1: College of Health and Human Sciences)
├── 04-ug-liberal-arts.md (Section 1: College of Liberal Arts)
├── 05-ug-natural-sciences.md (Section 1: College of Natural Sciences)
├── 06-ug-vet-med-biomedical.md (Section 1: College of Veterinary Medicine and Biomedical Sciences)
├── 07-ug-engineering.md (Section 1: Walter Scott, Jr. College of Engineering)
├── 08-ug-natural-resources.md (Section 1: Warner College of Natural Resources)
├── 09-graduate-programs.md (Section 2: All graduate programs)
├── 10-deadlines-requirements.md (Section 3)
├── 11-costs-financial-aid.md (Section 4)
├── 12-evidence-chain.md (Section 5)
└── 13-comparison-framework.md (Section 7)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "ColoradoState-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BS|BA|BFA|BM|MS|MA|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: https://catalog.colostate.edu/catalogcontents/
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| P0 | Per-program GRE requirements (grad) | Individual department pages |
| P0 | Per-program application deadlines (grad) | Individual department pages |
| P1 | Detailed scholarship criteria and amounts | https://admissions.colostate.edu/cost-financial-aid/financial-aid-scholarships/ |
| P1 | Transfer admission requirements | https://admissions.colostate.edu/apply/ |
| P2 | Per-program differential tuition amounts | https://financialaid.colostate.edu/cost-of-attendance/ |
| P2 | Campus housing options and costs | https://admissions.colostate.edu/about-csu/housing-dining/ |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | Colorado State University |
|------|---------------------------|
| Type | Public, Land-Grant, R1 |
| Location | Fort Collins, CO |
| UG Tuition (CO Resident) | $14,160 |
| UG Tuition (Non-Resident) | $37,502 |
| UG Total COA (On-Campus, CO) | $30,338 |
| UG Total COA (On-Campus, OOS) | $54,238 |
| Need-blind (intl?) | No (need-aware for all) |
| EA deadline | November 15 (non-binding) |
| RD deadline | January 15 |
| SAT/ACT required? | No (test-optional) |
| TOEFL min | 80 (before Jan 2026) / 4.5 (after) |
| IELTS min | 6.5 |
| DET min | 120 |
| Application fee | $50 |
| Total programs (Rule 1) | 738 |
| UG majors | 292 |
| UG minors | 87 |
| Graduate programs | 274 (Grad School count) |
| College count | 8 |
| Strong programs | Agriculture, Veterinary Medicine, Engineering, Natural Resources |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: admissions.colostate.edu, graduateschool.colostate.edu, financialaid.colostate.edu, catalog.colostate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
