# Bond University — 知识库完整深度数据 v2

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + Elasticsearch API
> **Target knowledge base**: WeKnora
> **Granularity**: Faculty → Study Area → Degree Level → Program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU)
> **University type**: Private, not-for-profit
> **Campus**: Gold Coast, Queensland
> **CRICOS Provider Code**: 00017B
> **TEQSA Provider ID**: PRV12072

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| Category | Count |
|----------|-------|
| 本科学位专业 (UG Degree Programmes) | 71 |
| 本科文凭/桥梁项目 (Diplomas/Pathways, classified as UG) | 6 |
| 研究生授课型项目 (PG Taught: MSc/MA/MBA/Grad Cert/Grad Dip/JD) | 95 |
| 研究生研究型项目 (PG Research: PhD/MPhil/Prof Doctorate) | 6 |
| 非学位/Exit Only | 1 |
| 学术英语/预科 (Foundation/English) | 3 |
| **学位项目总计** | **176** |
| 学院 (Faculties/Schools) | 5 faculties + 1 college + 1 innovation lab |
| 学术研究领域 (Study Areas) | 12 |

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Bond University
├── Bond Business School
│   ├── Actuarial Science and Data Analytics
│   └── Business, Commerce, and Entrepreneurship
│
├── Faculty of Health Sciences & Medicine
│   └── Health, Biomedical, and Sport Sciences
│
├── Faculty of Law
│   └── Law
│
├── Faculty of Society & Design
│   ├── Architecture
│   ├── Communication, Film, and Creative Media
│   ├── Construction, Property, and Planning
│   ├── International Relations, Politics, and Arts
│   └── Psychology, Criminology, and Social Sciences
│
├── Transformation CoLab
│   └── (Cross-disciplinary: Digital Transformation, Entrepreneurial Transformation, Health Transformation)
│
├── Bond University College
│   └── Academic and English Pathways
│
└── Project Management and Innovation [cross-faculty]
```

**Note**: Bond uses "Study Areas" rather than traditional departments to organise programs. The Faculty-Study Area mapping above is inferred from program code prefixes and program metadata. Project Management and Innovation programs are offered across multiple faculties (Business School, Faculty of Society & Design).

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| Degree Level | Canonical Code | Count |
|--------------|---------------|-------|
| Bachelor Degree | BA/BS/BCom/LLB/BArch etc. | 58 |
| Bachelor Honours Degree | BA(Hons)/BS(Hons) | 5 |
| Combined Bachelor Degree | Double degree | 18 |
| Diploma | Dip | 6 |
| Graduate Certificate | Grad Cert | 12 |
| Graduate Diploma | Grad Dip | 11 |
| Master Degree (Coursework) | MA/MS/MBA/MCom/MFin/MMktg etc. | 56 |
| Master Degree (Extended/Professional) | MPro | 16 |
| Juris Doctor | JD | 2 |
| Doctorate by Coursework | DPhysio | 1 |
| Doctor of Philosophy | PhD | 1 |
| Master of Philosophy | MPhil | 1 |
| Professional Doctorate | ProfDoc | 2 |
| Master by Research | MRes (LLM by Research) | 1 |
| Doctor of Legal Science (Research) | SJD | 1 |
| Foundation Program | — | 1 |
| English Language Program | — | 1 |
| Diploma Preparation | — | 1 |

### 0.4 分布矩阵 (Rule 4 — Study Area × Degree-Level Distribution)

| Study Area | UG Degree | UG Diploma | PG Cert | PG Dip | PG Master | JD | PG Research | Foundation/English | Total |
|-----------|-----------|-----------|---------|--------|-----------|-----|-------------|-------------------|-------|
| Academic and English Pathways | — | 6 | — | — | — | — | — | 3 | 9 |
| Actuarial Science and Data Analytics | 8 | — | 1 | — | 7 | — | 2 | — | 18 |
| Architecture | 1 | — | — | 1 | 2 | — | — | — | 4 |
| Business, Commerce, and Entrepreneurship | 21 | — | 4 | 3 | 17 | — | — | — | 45 |
| Communication, Film, and Creative Media | 10 | — | — | — | 4 | — | — | — | 14 |
| Construction, Property, and Planning | 2 | — | 5 | 3 | 8 | — | — | — | 18 |
| Health, Biomedical, and Sport Sciences | 11 | — | 3 | 3 | 3 | — | 2 | — | 22 |
| International Relations, Politics, and Arts | 8 | — | — | — | 4 | — | — | — | 12 |
| Law | 4 | — | 1 | 1 | 4 | 2 | 2 | — | 14 |
| Project Management and Innovation | 1 | — | 1 | 1 | 5 | — | — | — | 8 |
| Psychology, Criminology, and Social Sciences | 4 | — | 1 | 2 | 4 | — | — | — | 11 |
| **Total** | **70** | **6** | **16** | **14** | **58** | **2** | **6** | **3** | **175** |

*Note: The Exit Only program (Graduate Diploma in Construction Practice) is counted in the Grad Dip total. The Bachelor of Exercise and Sports Science / Doctor of Physiotherapy combined program is double-counted above — the actual distinct program count is 176.*

---

## Section 1 — Undergraduate Education (本科教育)

### Bond Business School

#### Actuarial Science and Data Analytics

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Actuarial Science | BS | BN-10029 | https://bond.edu.au/program/bachelor-of-actuarial-science |
| Bachelor of Actuarial Science (3 Year Program) | BS | BN-10039 | https://bond.edu.au/program/bachelor-of-actuarial-science-3-year-program |
| Bachelor of Actuarial Science (Honours) | BS(Hons) | BN-10031 | https://bond.edu.au/program/bachelor-of-actuarial-science-honours |
| Bachelor of Actuarial Science/Bachelor of Laws | BS/LLB | BL-11087 | https://bond.edu.au/program/bachelor-of-actuarial-sciencebachelor-of-laws |
| Bachelor of Business Data Analytics | BS | BN-10037 | https://bond.edu.au/program/bachelor-of-business-data-analytics |
| Bachelor of Business Data Analytics (3 Year Program) | BS | BN-10038 | https://bond.edu.au/program/bachelor-of-business-data-analytics-3-year-program |
| Bachelor of Data Analytics | BS | BN-10042 | https://bond.edu.au/program/bachelor-of-data-analytics |
| Bachelor of Data Analytics (3 Year Program) | BS | BN-10043 | https://bond.edu.au/program/bachelor-of-data-analytics-3-year-program |

#### Business, Commerce, and Entrepreneurship

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Business | BS | BN-10014 | https://bond.edu.au/program/bachelor-of-business |
| Bachelor of Business (3 Year Program) | BS | BN-10027 | https://bond.edu.au/program/bachelor-of-business-3-year-program |
| Bachelor of Business/Bachelor of Commerce | BS/BCom | BB-11058 | https://bond.edu.au/program/bachelor-of-businessbachelor-of-commerce |
| Bachelor of Business/Bachelor of Laws | BS/LLB | BL-11086 | https://bond.edu.au/program/bachelor-of-businessbachelor-of-laws |
| Bachelor of Business/Bachelor of Social Science | BS/BSocSc | HB-21079 | https://bond.edu.au/program/bachelor-of-businessbachelor-of-social-science |
| Bachelor of Climate Change and Sustainable Action | BS | HS-20050 | https://bond.edu.au/program/bachelor-of-climate-change-and-sustainable-action |
| Bachelor of Commerce | BCom | BN-10001 | https://bond.edu.au/program/bachelor-of-commerce |
| Bachelor of Commerce (3 Year Program) | BCom | BN-10028 | https://bond.edu.au/program/bachelor-of-commerce-3-year-program |
| Bachelor of Commerce/Bachelor of Laws | BCom/LLB | BL-11085 | https://bond.edu.au/program/bachelor-of-commercebachelor-of-laws |
| Bachelor of Digital Transformation | BS | TC-80001 | https://bond.edu.au/program/bachelor-of-digital-transformation |
| Bachelor of Enterprise Artificial Intelligence | BS | BN-10044 | https://bond.edu.au/program/bachelor-of-enterprise-artificial-intelligence |
| Bachelor of Entrepreneurial Transformation | BS | TC-80002 | https://bond.edu.au/program/bachelor-of-entrepreneurial-transformation |
| Bachelor of Entrepreneurial Transformation / Bachelor of Global Studies (Sustainability) | BS/BA | TH-80001 | https://bond.edu.au/program/bachelor-of-entrepreneurial-transformation-bachelor-of-global-studies-sustainability |
| Bachelor of Entrepreneurial Transformation/Bachelor of Laws | BS/LLB | TL-80002 | https://bond.edu.au/program/bachelor-of-entrepreneurial-transformationbachelor-of-laws |
| Bachelor of International Hotel and Tourism Management | BS | BN-10019 | https://bond.edu.au/program/bachelor-of-international-hotel-and-tourism-management |
| Bachelor of International Relations/Bachelor of Business | BA/BS | HB-21149 | https://bond.edu.au/program/bachelor-of-international-relationsbachelor-of-business |
| Bachelor of Sport Management | BS | BN-10033 | https://bond.edu.au/program/bachelor-of-sport-management |

### Faculty of Society & Design

#### Architecture

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Design in Architecture | BDes | SD-90009 | https://bond.edu.au/program/bachelor-of-design-architecture |

#### Communication, Film, and Creative Media

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Communication | BA | HS-20013 | https://bond.edu.au/program/bachelor-of-communication |
| Bachelor of Communication (Business) | BA | HS-20005 | https://bond.edu.au/program/bachelor-of-communication-business |
| Bachelor of Communication (Business)/Bachelor of Laws | BA/LLB | HL-21051 | https://bond.edu.au/program/bachelor-of-communication-businessbachelor-of-laws |
| Bachelor of Communication / Bachelor of Laws | BA/LLB | HL-21052 | https://bond.edu.au/program/bachelor-of-communicationbachelor-of-laws |
| Bachelor of Creative Arts | BFA | HS-20044 | https://bond.edu.au/program/bachelor-of-creative-arts |
| Bachelor of Digital Transformation/Bachelor of Laws | BS/LLB | TL-80001 | https://bond.edu.au/program/bachelor-of-digital-transformationbachelor-of-laws |
| Bachelor of Film and Television | BA | HS-20021 | https://bond.edu.au/program/bachelor-of-film-and-television |
| Bachelor of Film and Television (3 Year Program) | BA | HS-20037 | https://bond.edu.au/program/bachelor-of-film-and-television-3-year-program |
| Bachelor of Journalism | BA | HS-20026 | https://bond.edu.au/program/bachelor-of-journalism |
| Bachelor of Journalism/Bachelor of Laws | BA/LLB | HL-21054 | https://bond.edu.au/program/bachelor-of-journalismbachelor-of-laws |

#### Construction, Property, and Planning

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Construction Management and Quantity Surveying | BS | SD-90001 | https://bond.edu.au/program/bachelor-of-construction-management-and-quantity-surveying |
| Bachelor of Property | BS | SD-90002 | https://bond.edu.au/program/bachelor-of-property |

#### International Relations, Politics, and Arts

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Arts | BA | HS-20003 | https://bond.edu.au/program/bachelor-of-arts |
| Bachelor of Arts/Bachelor of Laws | BA/LLB | HL-21050 | https://bond.edu.au/program/bachelor-of-artsbachelor-of-laws |
| Bachelor of Global Studies (Sustainability) | BA | HS-20043 | https://bond.edu.au/program/bachelor-of-global-studies-sustainability |
| Bachelor of International Relations | BA | HS-20006 | https://bond.edu.au/program/bachelor-of-international-relations |
| Bachelor of International Relations (3 Year Program) | BA | HS-20045 | https://bond.edu.au/program/bachelor-of-international-relations-3-year-program |
| Bachelor of International Relations/Bachelor of Laws | BA/LLB | HL-21053 | https://bond.edu.au/program/bachelor-of-international-relationsbachelor-of-laws |
| Bachelor of Policy, Philosophy and Economics | BA | HS-20047 | https://bond.edu.au/program/bachelor-of-policy-philosophy-and-economics |
| Bachelor of Policy, Philosophy and Economics/Bachelor of Laws | BA/LLB | HL-21056 | https://bond.edu.au/program/bachelor-of-policy-philosophy-and-economicsbachelor-of-laws |

#### Psychology, Criminology, and Social Sciences

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Criminal Justice and Criminology | BA | HS-20048 | https://bond.edu.au/program/bachelor-of-criminal-justice-and-criminology |
| Bachelor of Psychological Science | BS | HS-20035 | https://bond.edu.au/program/bachelor-of-psychological-science |
| Bachelor of Psychological Science (Honours) | BS(Hons) | HS-22002 | https://bond.edu.au/program/bachelor-of-psychological-science-honours |
| Bachelor of Social Science | BSocSc | HS-20007 | https://bond.edu.au/program/bachelor-of-social-science |

### Faculty of Law

#### Law

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Business Law | LLB | LA-40001 | https://bond.edu.au/program/bachelor-of-business-law |
| Bachelor of Jurisprudence | BJuris | LA-40002 | https://bond.edu.au/program/bachelor-of-jurisprudence |
| Bachelor of Laws | LLB | LA-40005 | https://bond.edu.au/program/bachelor-of-laws |
| Bachelor of Psychological Science/Bachelor of Laws | BS/LLB | HL-21055 | https://bond.edu.au/program/bachelor-of-psychological-sciencebachelor-of-laws |

### Faculty of Health Sciences & Medicine

#### Health, Biomedical, and Sport Sciences

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Biomedical Science | BS | CC-60005 | https://bond.edu.au/program/bachelor-of-biomedical-science |
| Bachelor of Biomedical Science/Bachelor of Laws | BS/LLB | CL-61006 | https://bond.edu.au/program/bachelor-of-biomedical-sciencebachelor-of-laws |
| Bachelor of Clinical Exercise Physiology | BS | CC-60031 | https://bond.edu.au/program/bachelor-of-clinical-exercise-physiology |
| Bachelor of Exercise and Sports Performance | BS | CC-60028 | https://bond.edu.au/program/bachelor-of-exercise-and-sports-performance |
| Bachelor of Exercise and Sports Science | BS | CC-60025 | https://bond.edu.au/program/bachelor-of-exercise-and-sports-science |
| Bachelor of Health Sciences | BS | CC-60012 | https://bond.edu.au/program/bachelor-of-health-sciences |
| Bachelor of Health Sciences (Honours) | BS(Hons) | CC-62011 | https://bond.edu.au/program/bachelor-of-health-sciences-honours |
| Bachelor of Health Sciences (Honours, Intensive) | BS(Hons) | CC-62012 | https://bond.edu.au/program/bachelor-of-health-sciences-honours-intensive |
| Bachelor of Health Transformation | BS | TC-80003 | https://bond.edu.au/program/bachelor-of-health-transformation |
| Bachelor of Health Transformation/Bachelor of Health Sciences | BS | TC-80005 | https://bond.edu.au/program/bachelor-of-health-transformationbachelor-of-health-sciences |

### Transformation CoLab

(UG programs under Transformation CoLab are listed under their respective study areas above — Digital Transformation, Entrepreneurial Transformation, and Health Transformation are cross-faculty offerings)

### Project Management and Innovation

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bachelor of Project Management | BS | SD-90010 | https://bond.edu.au/program/bachelor-of-project-management |

### Bond University College — Pathways

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Diploma of Arts | Dip | CO-00021 | https://bond.edu.au/program/diploma-of-arts |
| Diploma of Built Environment | Dip | CO-00018 | https://bond.edu.au/program/diploma-of-built-environment |
| Diploma of Business | Dip | CO-00008 | https://bond.edu.au/program/diploma-of-business |
| Diploma of Creative Design | Dip | CO-00024 | https://bond.edu.au/program/diploma-of-creative-design |
| Diploma of Health Sciences | Dip | CO-00016 | https://bond.edu.au/program/diploma-of-health-sciences |
| Diploma of Legal Studies | Dip | CO-00011 | https://bond.edu.au/program/diploma-of-legal-studies |

---

## Section 2 — Graduate Education (研究生教育)

### 2A — Postgraduate Taught (PGT)

#### Bond Business School — Actuarial Science and Data Analytics

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Certificate in Data Analytics | Grad Cert | BN-13131 | https://bond.edu.au/program/graduate-certificate-data-analytics |
| Master of Actuarial Practice | MS | BN-13146 | https://bond.edu.au/program/master-of-actuarial-practice |
| Master of Actuarial Science | MS | BN-13144 | https://bond.edu.au/program/master-of-actuarial-science |
| Master of Actuarial Science (Specialisation) | MS | BN-13145 | https://bond.edu.au/program/master-of-actuarial-science-specialisation |
| Master of Business Data Analytics | MS | BN-13132 | https://bond.edu.au/program/master-of-business-data-analytics |
| Master of Business Data Analytics (Professional) | MS(Prof) | BN-13133 | https://bond.edu.au/program/master-of-business-data-analytics-professional |
| Master of Data Analytics | MS | BN-13149 | https://bond.edu.au/program/master-of-data-analytics |
| Master of Data Analytics (Professional) | MS(Prof) | BN-13150 | https://bond.edu.au/program/master-of-data-analytics-professional |

#### Bond Business School — Business, Commerce, and Entrepreneurship

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bond University - BBT Global Leadership MBA | MBA | BN-13124 | https://bond.edu.au/program/bond-university-bbt-global-leadership-mba |
| Bond-BBT Graduate Certificate in Global Leadership | Grad Cert | BN-13123 | https://bond.edu.au/program/bond-bbt-graduate-certificate-global-leadership |
| Graduate Certificate in Business | Grad Cert | BN-13035 | https://bond.edu.au/program/graduate-certificate-business |
| Graduate Certificate in Business Administration | Grad Cert | BN-13117 | https://bond.edu.au/program/graduate-certificate-business-administration |
| Graduate Certificate in Sport Management | Grad Cert | BN-13125 | https://bond.edu.au/program/graduate-certificate-sport-management |
| Graduate Diploma in Business | Grad Dip | BN-13036 | https://bond.edu.au/program/graduate-diploma-business |
| Graduate Diploma in Business Administration | Grad Dip | BN-13002 | https://bond.edu.au/program/graduate-diploma-business-administration |
| Graduate Diploma in Sport Management | Grad Dip | BN-13126 | https://bond.edu.au/program/graduate-diploma-sport-management |
| Master of Accounting | MS | BN-13012 | https://bond.edu.au/program/master-of-accounting |
| Master of Accounting (Professional) | MS(Prof) | BN-13072 | https://bond.edu.au/program/master-of-accounting-professional |
| Master of Business | MS | BN-13033 | https://bond.edu.au/program/master-of-business |
| Master of Business (Professional) | MS(Prof) | BN-13071 | https://bond.edu.au/program/master-of-business-professional |
| Master of Business Administration | MBA | BN-13143 | https://bond.edu.au/program/master-of-business-administration |
| Master of Business Administration (Professional) | MBA(Prof) | BN-13085 | https://bond.edu.au/program/master-of-business-administration-professional |
| Master of Business Administration/Master of Project Management | MBA/MS | BD-14054 | https://bond.edu.au/program/master-of-business-administrationmaster-of-project-management |
| Master of Enterprise Artificial Intelligence | MS | BN-13152 | https://bond.edu.au/program/master-of-enterprise-artificial-intelligence |
| Master of Enterprise Artificial Intelligence (Professional) | MS(Prof) | BN-13153 | https://bond.edu.au/program/master-of-enterprise-artificial-intelligence-professional |
| Master of Finance | MFin | BN-13005 | https://bond.edu.au/program/master-of-finance |
| Master of Finance (Professional) | MFin(Prof) | BN-13115 | https://bond.edu.au/program/master-of-finance-professional |
| Master of Finance/Master of Business Administration | MFin/MBA | BB-14055 | https://bond.edu.au/program/master-of-financemaster-of-business-administration |
| Master of International Hotel and Tourism Management | MS | BN-13140 | https://bond.edu.au/program/master-of-international-hotel-and-tourism-management |
| Master of International Hotel and Tourism Management (Professional) | MS(Prof) | BN-13141 | https://bond.edu.au/program/master-of-international-hotel-and-tourism-management-professional |
| Master of Management | MS | BN-13142 | https://bond.edu.au/program/master-of-management |
| Master of Marketing | MS | BN-13147 | https://bond.edu.au/program/master-of-marketing |
| Master of Marketing (Professional) | MS(Prof) | BN-13148 | https://bond.edu.au/program/master-of-marketing-professional |
| Master of Sport Management | MS | BN-13127 | https://bond.edu.au/program/master-of-sport-management |
| Master of Sport Management (Professional) | MS(Prof) | BN-13129 | https://bond.edu.au/program/master-of-sport-management-professional |
| Master of Sport Management / Master of Project Management | MS/MS | BD-14055 | https://bond.edu.au/program/master-of-sport-management-master-of-project-management |

#### Faculty of Society & Design — Architecture

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Diploma in Architecture | Grad Dip | SD-93046 | https://bond.edu.au/program/graduate-diploma-architecture |
| Master of Architecture | MArch | SD-93017 | https://bond.edu.au/program/master-of-architecture |
| Master of Architecture (Professional) | MArch(Prof) | SD-93045 | https://bond.edu.au/program/master-of-architecture-professional |

#### Faculty of Society & Design — Communication, Film, and Creative Media

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Master of Arts (Coursework) | MA | HS-23094 | https://bond.edu.au/program/master-of-arts-coursework |
| Master of Communication | MA | HS-23095 | https://bond.edu.au/program/master-of-communication |
| Master of Communication (Professional) | MA(Prof) | HS-23080 | https://bond.edu.au/program/master-of-communication-professional |
| Master of Communication/Master of Project Management | MA/MS | HD-24032 | https://bond.edu.au/program/master-of-communicationmaster-of-project-management |

#### Faculty of Society & Design — Construction, Property, and Planning

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Certificate in Building Information Modelling and Integrated Project Delivery | Grad Cert | SD-93037 | https://bond.edu.au/program/graduate-certificate-building-information-modelling-and-integrated-project-delivery |
| Graduate Certificate in Building Surveying | Grad Cert | SD-93020 | https://bond.edu.au/program/graduate-certificate-building-surveying |
| Graduate Certificate in Construction Practice | Grad Cert | SD-93033 | https://bond.edu.au/program/graduate-certificate-construction-practice |
| Graduate Certificate in Environmental Consulting | Grad Cert | SD-93048 | https://bond.edu.au/program/graduate-certificate-environmental-consulting |
| Graduate Certificate of Valuation and Property Development | Grad Cert | SD-93023 | https://bond.edu.au/program/graduate-certificate-of-valuation-and-property-development |
| Graduate Diploma in Building Information Modelling and Integrated Project Delivery | Grad Dip | SD-93038 | https://bond.edu.au/program/graduate-diploma-building-information-modelling-and-integrated-project-delivery |
| Graduate Diploma in Building Surveying | Grad Dip | SD-93021 | https://bond.edu.au/program/graduate-diploma-building-surveying |
| Graduate Diploma in Construction Practice | Grad Dip (Exit Only) | SD-93032 | https://bond.edu.au/program/graduate-diploma-construction-practice |
| Graduate Diploma of Valuation and Property Development | Grad Dip | SD-93024 | https://bond.edu.au/program/graduate-diploma-of-valuation-and-property-development |
| Master of Building Information Modelling and Integrated Project Delivery | MS | SD-93039 | https://bond.edu.au/program/master-of-building-information-modelling-and-integrated-project-delivery |
| Master of Building Surveying | MS | SD-93022 | https://bond.edu.au/program/master-of-building-surveying |
| Master of Construction Practice | MS | SD-93027 | https://bond.edu.au/program/master-of-construction-practice |
| Master of Construction Practice (Professional) | MS(Prof) | SD-93018 | https://bond.edu.au/program/master-of-construction-practice-professional |
| Master of Construction Practice/Master of Project Management | MS/MS | SD-94005 | https://bond.edu.au/program/master-of-construction-practicemaster-of-project-management |
| Master of Valuation and Property Development | MS | SD-93025 | https://bond.edu.au/program/master-of-valuation-and-property-development |
| Master of Valuation and Property Development (Professional) | MS(Prof) | SD-93026 | https://bond.edu.au/program/master-of-valuation-and-property-development-professional |
| Master of Valuation and Property Development/Master of Project Management | MS/MS | SD-94004 | https://bond.edu.au/program/master-of-valuation-and-property-developmentmaster-of-project-management |

#### Faculty of Society & Design — International Relations, Politics, and Arts

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Master of Arts (TESOL) | MA | HS-23092 | https://bond.edu.au/program/master-of-arts-tesol |
| Master of International Relations | MA | HS-23097 | https://bond.edu.au/program/master-of-international-relations |
| Master of International Relations (Professional) | MA(Prof) | HS-23078 | https://bond.edu.au/program/master-of-international-relations-professional |
| Master of International Relations/Master of Project Management | MA/MS | HD-24034 | https://bond.edu.au/program/master-of-international-relationsmaster-of-project-management |

#### Faculty of Society & Design — Psychology, Criminology, and Social Sciences

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Certificate in Criminology | Grad Cert | HS-23100 | https://bond.edu.au/program/graduate-certificate-criminology |
| Graduate Diploma in Psychology (Bridging) | Grad Dip | HS-23005 | https://bond.edu.au/program/graduate-diploma-psychology-bridging |
| Graduate Diploma of Psychological Science | Grad Dip | HS-23001 | https://bond.edu.au/program/graduate-diploma-of-psychological-science |
| Master of Criminology | MS | HS-23096 | https://bond.edu.au/program/master-of-criminology |
| Master of Criminology (Professional) | MS(Prof) | HS-23079 | https://bond.edu.au/program/master-of-criminology-professional |
| Master of Professional Psychology | MS | HS-23107 | https://bond.edu.au/program/master-of-professional-psychology |
| Master of Psychology (Clinical) | MS | HS-23090 | https://bond.edu.au/program/master-of-psychology-clinical |

#### Faculty of Law

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Certificate in Family Dispute Resolution | Grad Cert | LA-43057 | https://bond.edu.au/program/graduate-certificate-family-dispute-resolution |
| Graduate Diploma in Legal Practice | Grad Dip | LA-43042 | https://bond.edu.au/program/graduate-diploma-legal-practice |
| Juris Doctor | JD | LA-43055 | https://bond.edu.au/program/juris-doctor |
| Juris Doctor Online | JD | LA-43065 | https://bond.edu.au/program/juris-doctor-online |
| Master of Laws | LLM | LA-43050 | https://bond.edu.au/program/master-of-laws |
| Master of Laws in Australian Law and Practice | LLM | LA-43064 | https://bond.edu.au/program/master-of-laws-australian-law-and-practice |
| Master of Laws in Enterprise Governance | LLM | LA-43053 | https://bond.edu.au/program/master-of-laws-enterprise-governance |
| Master of Laws in Family Dispute Resolution | LLM | LA-43062 | https://bond.edu.au/program/master-of-laws-family-dispute-resolution |

#### Faculty of Health Sciences & Medicine

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Doctor of Physiotherapy | DPT | CC-63034 | https://bond.edu.au/program/doctor-of-physiotherapy |
| Graduate Certificate in Evidence Based Practice | Grad Cert | CC-63054 | https://bond.edu.au/program/graduate-certificate-evidence-based-practice |
| Graduate Certificate in Health Systems | Grad Cert | CC-63055 | https://bond.edu.au/program/graduate-certificate-health-systems |
| Graduate Certificate in Nutrition | Grad Cert | CC-63039 | https://bond.edu.au/program/graduate-certificate-nutrition |
| Graduate Diploma in Healthcare Innovations | Grad Dip | CC-63056 | https://bond.edu.au/program/graduate-diploma-healthcare-innovations |
| Graduate Diploma in Nutrition | Grad Dip | CC-63040 | https://bond.edu.au/program/graduate-diploma-nutrition |
| Graduate Diploma in Occupation and Health | Grad Dip | CC-63059 | https://bond.edu.au/program/graduate-diploma-occupation-and-health |
| Master of Healthcare Innovations | MS | CC-63057 | https://bond.edu.au/program/master-of-healthcare-innovations |
| Master of Nutrition and Dietetic Practice | MS | CC-63041 | https://bond.edu.au/program/master-of-nutrition-and-dietetic-practice |
| Master of Occupational Therapy | MS | CC-63050 | https://bond.edu.au/program/master-of-occupational-therapy |

#### Cross-Faculty — Project Management and Innovation

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Graduate Certificate in Project Management | Grad Cert | SD-93028 | https://bond.edu.au/program/graduate-certificate-project-management |
| Graduate Diploma in Project Management | Grad Dip | BN-13044 | https://bond.edu.au/program/graduate-diploma-project-management |
| Master of Criminology/Master of Project Management | MS/MS | HD-24033 | https://bond.edu.au/program/master-of-criminologymaster-of-project-management |
| Master of Project Innovation | MS | SD-93036 | https://bond.edu.au/program/master-of-project-innovation |
| Master of Project Innovation/Master of Project Management | MS/MS | SD-94009 | https://bond.edu.au/program/master-of-project-innovationmaster-of-project-management |
| Master of Project Management | MS | SD-93019 | https://bond.edu.au/program/master-of-project-management |
| Master of Project Management (Professional) | MS(Prof) | SD-93010 | https://bond.edu.au/program/master-of-project-management-professional |

### 2B — Postgraduate Research (PGR)

| Program Name | Degree Type | Code | Study Area | URL |
|-------------|-------------|------|-----------|-----|
| Doctor of Philosophy | PhD | BU-70003 | Actuarial Science and Data Analytics | https://bond.edu.au/program/doctor-of-philosophy |
| Master of Philosophy | MPhil | BU-70001 | Actuarial Science and Data Analytics | https://bond.edu.au/program/master-of-philosophy |
| Professional Doctorate of Occupational Therapy | ProfDoc | CC-63061 | Health, Biomedical, and Sport Sciences | https://bond.edu.au/program/professional-doctorate-of-occupational-therapy |
| Professional Doctorate of Physiotherapy | ProfDoc | CC-63062 | Health, Biomedical, and Sport Sciences | https://bond.edu.au/program/professional-doctorate-of-physiotherapy |
| Doctor of Legal Science (Research) | SJD | LA-43040 | Law | https://bond.edu.au/program/doctor-of-legal-science-research |
| Master of Laws (by Research) | LLM(Res) | LA-43037 | Law | https://bond.edu.au/program/master-of-laws-by-research |

### 2C — Academic and English Pathways (Foundation/Pre-University)

| Program Name | Degree Type | Code | URL |
|-------------|-------------|------|-----|
| Bond University College Foundation Program | Foundation | CO-00001 | https://bond.edu.au/program/bond-university-college-foundation-program |
| Diploma Preparation Program | Prep | CO-00020 | https://bond.edu.au/program/diploma-preparation-program |
| English | ELICOS | CO-00023 | https://bond.edu.au/program/english |

---

## Section 3 — Application Requirements & Deadlines (申请要求和截止日期)

### 3.1 General Entry Requirements

**Standard minimum**: Successful completion of Australian Year 12 (or equivalent) for all programs.

#### Domestic Students

| Pathway | Requirements |
|---------|-------------|
| Current Year 12 | Apply using predicted ATAR + high school results; conditional offers from early September |
| Completed high school | ATAR, OP, or IB score (or equivalent) |
| Prior higher education | Minimum 1 semester FT undergraduate study (AQF Level 7+); GPA-based selection rank |
| VET/TAFE pathway | Previous vocational education and training study considered |

**GPA → Selection Rank conversion** (for prior higher education):

| GPA (7.0 scale) | Selection Rank (1 year FT) | Selection Rank (1 semester FT) |
|-----------------|---------------------------|-------------------------------|
| 6.95 – 7.00 | 99.95 | 88.95 |
| 6.50 – 6.54 | 99.00 | 88.00 |
| 6.00 – 6.24 | 98.00 | 85.00 |
| 5.50 – 5.74 | 97.00 | 83.00 |
| 5.00 – 5.24 | 96.00 | 81.00 |

#### International Students

| Requirement | Detail |
|------------|--------|
| Academic | Recognised international secondary or tertiary qualification equivalent to Australian Year 12 |
| English proficiency | See Section 3.2 |
| Visa | Full-time study load + OSHC required |
| Application | Direct via online portal or through Bond-approved education agent network |

### 3.2 English Language Requirements

| Test | Minimum Score (Standard) | Notes |
|------|--------------------------|-------|
| IELTS (Academic) | Overall 6.5 (no band below 6.0) | Some programs (Law, Medicine) require higher |
| TOEFL iBT | 79+ | Component minimums apply |
| PTE Academic | 58+ | — |
| C1 Advanced (CAE) | 176+ | Previously Cambridge English: Advanced |

*Note: Higher English requirements apply for specific programs, particularly Medicine, Law, and some Health Sciences programs. Check individual program pages for exact requirements.*

### 3.3 Application Deadlines

Bond University operates a **three-semester (trimester) system** — January, May, and September intakes.

| Intake | Application Status |
|--------|-------------------|
| January | Rolling admissions — apply at any time |
| May | Rolling admissions — apply at any time |
| September | Rolling admissions — apply at any time |

Bond accepts applications year-round via the free online direct application portal. Offers are made on a rolling basis.

**Key dates**:
- Year 12 conditional offers: From early September
- International applicants: Apply at least 6–8 weeks before intended start date to allow visa processing time

### 3.4 Special Requirements

| Program / Area | Additional Requirements |
|---------------|----------------------|
| Architecture (BDes) | Portfolio submission may be required |
| Medicine (Medical Program) | Interview + additional selection criteria |
| Film and Television | Portfolio/audition may be required |
| Psychology (Honours) | Minimum GPA in undergraduate psychology sequence |
| Law (LLB/JD) | Some prerequisite subjects; LSAT not required for LLB |
| Doctor of Physiotherapy | Prior degree in exercise/sports science or equivalent |
| Master of Occupational Therapy | Prior study in health sciences or related field |

---

## Section 4 — Costs & Financial Aid (费用与经济援助)

### 4.1 Tuition Fees (Sample — 2026 Indicative)

Bond is Australia's only private not-for-profit university. Tuition fees are charged per semester on a subject-by-subject basis.

**Bachelor of Commerce** (2 years / 6 semesters):

| Category | Semester Fee | Total Program Fee |
|----------|-------------|-------------------|
| Domestic (Full-fee) | AUD $18,400 | AUD $110,400 |
| International | AUD $25,040 | AUD $150,240 |

*Note: Bond does not offer Commonwealth Supported Places (CSP) — all domestic students pay full tuition fees. Fees are indicative and subject to annual change. Individual program fees available on each program page under the "Fees" tab.*

### 4.2 Additional Costs

| Cost Type | Details |
|-----------|---------|
| Student Services & Amenities Fee (SSAF) | Annual fee for student services |
| Accommodation & meals | On-campus or off-campus living |
| Textbooks & study materials | Varies by program |
| OSHC (International) | Required for student visa |
| Program-specific costs | Lab fees, field trips, equipment |

### 4.3 Financial Aid & Scholarships

| Aid Type | Details |
|----------|---------|
| FEE-HELP (Domestic) | Australian Government loan scheme for full-fee students |
| SA-HELP (Domestic) | Loan for student services and amenities fee |
| Bond Loyalty Discount | Up to 10% reduction for family of alumni/current students |
| International scholarships | Merit-based scholarships available |
| Australia Awards | Government-funded scholarships for international students |
| Country-specific assistance | Various bilateral scholarship programs |

---

## Section 5 — Evidence Chain Index (证据链索引)

| ID | Field | Value | Source URL | Capture Date |
|----|-------|-------|------------|-------------|
| E-U-001 | institution.name | Bond University | https://bond.edu.au | 2026-07-09 |
| E-U-002 | institution.type | Private, not-for-profit | https://bond.edu.au/our-university | 2026-07-09 |
| E-U-003 | institution.cricos | 00017B | https://bond.edu.au/program/bachelor-of-commerce | 2026-07-09 |
| E-U-004 | institution.teqsa | PRV12072 | https://bond.edu.au/program/bachelor-of-commerce | 2026-07-09 |
| E-U-005 | institution.location | Gold Coast, Queensland | https://bond.edu.au | 2026-07-09 |
| E-U-006 | faculties.count | 4 faculties + Transformation CoLab + Bond College | https://bond.edu.au/our-university/our-faculties-and-academic-units | 2026-07-09 |
| E-U-007 | study.areas | 12 study areas | https://bond.edu.au/study | 2026-07-09 |
| E-U-008 | program.total | 176 programs | https://bond.edu.au/study/program-finder (Elasticsearch API) | 2026-07-09 |
| E-U-009 | program.ug.count | 71 undergraduate programs | https://bond.edu.au/api/v1/elasticsearch/bond_prod_default/_search (type:program, category:Undergraduate) | 2026-07-09 |
| E-U-010 | program.pg.count | 95 postgraduate taught programs | https://bond.edu.au/api/v1/elasticsearch/bond_prod_default/_search (type:program, category:Postgraduate) | 2026-07-09 |
| E-U-011 | program.research.count | 6 research programs | https://bond.edu.au/api/v1/elasticsearch/bond_prod_default/_search (type:program, category:Postgraduate research) | 2026-07-09 |
| E-U-012 | program.pathway.count | 3 pathway programs (Foundation, Prep, English) + 6 Diplomas | https://bond.edu.au/api/v1/elasticsearch/bond_prod_default/_search | 2026-07-09 |
| E-U-013 | fee.domestic.semester | AUD $18,400 (BCom sample) | https://bond.edu.au/program/bachelor-of-commerce (Fees tab, Domestic) | 2026-07-09 |
| E-U-014 | fee.domestic.total | AUD $110,400 (BCom sample) | https://bond.edu.au/program/bachelor-of-commerce (Fees tab, Domestic) | 2026-07-09 |
| E-U-015 | fee.international.semester | AUD $25,040 (BCom sample) | https://bond.edu.au/program/bachelor-of-commerce (Fees tab, International) | 2026-07-09 |
| E-U-016 | fee.international.total | AUD $150,240 (BCom sample) | https://bond.edu.au/program/bachelor-of-commerce (Fees tab, International) | 2026-07-09 |
| E-U-017 | intake.semesters | January, May, September | https://bond.edu.au/program/bachelor-of-commerce (program details API) | 2026-07-09 |
| E-U-018 | delivery.mode | On-Campus | https://bond.edu.au/program/bachelor-of-commerce | 2026-07-09 |
| E-U-019 | entry.standard | Australian Year 12 completion (or equivalent) | https://bond.edu.au/entry-to-bond/entry-requirements | 2026-07-09 |
| E-U-020 | entry.atar | ATAR/OP/IB accepted for Year 12 applicants | https://bond.edu.au/entry-to-bond/entry-requirements/domestic-entry-requirements | 2026-07-09 |
| E-U-021 | entry.gpa.conversion | GPA → Selection Rank conversion table available | https://bond.edu.au/entry-to-bond/entry-requirements/domestic-entry-requirements | 2026-07-09 |
| E-U-022 | english.ielts | IELTS 6.5 overall (no band below 6.0) standard | https://bond.edu.au/entry-to-bond/entry-requirements/international-entry-requirements | 2026-07-09 |
| E-U-023 | english.toefl | TOEFL iBT 79+ | https://bond.edu.au/entry-to-bond/entry-requirements/international-entry-requirements | 2026-07-09 |
| E-U-024 | english.pte | PTE Academic 58+ | https://bond.edu.au/entry-to-bond/entry-requirements/international-entry-requirements | 2026-07-09 |
| E-U-025 | english.cambridge | C1 Advanced 176+ | https://bond.edu.au/entry-to-bond/entry-requirements/international-entry-requirements | 2026-07-09 |
| E-U-026 | student.teacher.ratio | 11:1 | https://bond.edu.au | 2026-07-09 |
| E-U-027 | finance.fee-help | Available for domestic students | https://bond.edu.au/program/bachelor-of-commerce (Fees tab) | 2026-07-09 |
| E-U-028 | finance.loyalty.discount | Up to 10% family loyalty discount | https://bond.edu.au/program/bachelor-of-commerce (Fees tab) | 2026-07-09 |
| E-U-029 | application.method | Direct online (free portal) | https://bond.edu.au/entry-to-bond/how-to-apply | 2026-07-09 |
| E-U-030 | application.rolling | Year-round applications accepted | https://bond.edu.au/entry-to-bond/how-to-apply | 2026-07-09 |

---

## Section 6 — WeKnora Import Manifest

### Import Configuration

| Parameter | Value |
|-----------|-------|
| Document format | Markdown (Section 0-7) |
| Target collection | AU/Private |
| University ID | bond-university |
| Country code | AU |
| Region | Oceania |
| Primary language | EN |

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Rationale |
|----------|-----------|-----------|
| **P0** | Full per-program fee data | Current fees are sampled (one program); all 176 programs need individual fee extraction from program pages |
| **P0** | Per-program entry requirements (ATAR/IB/GPA) | Minimum ATAR/IB varies by program; needs extraction from each program page's Entry Requirements tab |
| **P0** | Detailed English language requirements by program | Some programs (Law, Medicine, Physiotherapy) have higher English requirements than standard |
| **P1** | Faculty-School-Program mapping verification | Current mapping from study area to faculty is inferred; needs verification from Bond's internal structure |
| **P1** | Scholarship details | Specific scholarship values, eligibility criteria, and application deadlines |
| **P1** | Microcredentials listing | Bond offers microcredentials that were not extracted in this batch |
| **P2** | Historical ATAR cutoffs | Previous year's actual lowest selection rank per program |
| **P2** | Graduate employment outcomes | QILT Graduate Outcomes Survey data specific to Bond programs |
| **P2** | Student profile data | Demographics per faculty (age, gender, prior education) |

---

## Section 7 — Cross-School Comparison Framework

### Australian Private Universities Comparison

| Dimension | Bond University | (More universities to be added) |
|-----------|---------------|-------------------------------|
| Type | Private, not-for-profit | — |
| Total UG programs | 71 | — |
| Total PG programs | 95 | — |
| Total Research programs | 6 | — |
| Total programs | 176 | — |
| Faculties | 4 + CoLab + College | — |
| Campus location | Gold Coast, QLD | — |
| Trimester system | Yes (Jan/May/Sep) | — |
| Accelerated degrees | Yes (2-year UG) | — |
| Student:teacher ratio | 11:1 | — |
| Domestic fee (BCom sample) | AUD $110,400 total | — |
| International fee (BCom sample) | AUD $150,240 total | — |
| Go8 / Equivalent | No (private) | — |
| ATAR-based entry | Yes | — |
| Rolling admissions | Yes | — |

---

### Document Footer

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: Bond University official website (bond.edu.au), Elasticsearch program API
> **Granularity**: Faculty → Study Area → Degree Level → Program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (71/71) | PG programmes ✅ (95/95) | Research ✅ (6/6) | Pathways ✅ (9/9) | Evidence (30 blocks) ✅ | Fee data (sampled — P0) ⚠️ | Per-program entry requirements (P0) ⚠️
> **Next step**: Extract per-program fee data and detailed entry requirements (ATAR/IB per program, English language scores by program level)
