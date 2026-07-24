> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_snapshot + curl
> **Target knowledge base**: WeKnora
> **Granularity**: faculty → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (British Columbia)
> **Platform detected**: Drupal (Google Custom Search for program discovery)

# Vancouver Island University (VIU) — 知识库完整深度数据

---

## Section 0 — 院校总览

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | ~70+ (含 Major/Minor/Honours, 分布于10个学科领域) |
| 本科辅修 (Minors) | ~30+ |
| 研究生授课型项目 (PGT: Master's/Graduate Diploma/Certificate) | ~10 |
| 研究生博士项目 (PhD/Doctoral) | 0 (VIU不授予博士学位) |
| 证书/文凭项目 (Certificate/Diploma, 含Trades) | ~40+ |
| 学位项目总计 | ~120+ |
| 学院/教学领域 (Faculties/Areas of Study) | 10 个学科领域 |
| 学术院系 (Academic Schools/Departments) | 20+ |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Vancouver Island University (VIU)
├── Faculty of Arts, Humanities and Social Sciences (艺术、人文与社会科学)
│   ├── Department of Anthropology
│   ├── Department of Creative Writing and Journalism
│   ├── Department of Criminology
│   ├── Department of Digital Media Studies
│   ├── Department of Economics
│   ├── Department of English
│   ├── Department of Geography
│   ├── Department of Global Studies
│   ├── Department of History
│   ├── Department of Indigenous/Xwulmuxw Studies
│   ├── Department of Languages and Culture (Romance Languages)
│   ├── Department of Liberal Studies
│   ├── Department of Mathematics
│   ├── Department of Media Studies
│   ├── Department of Philosophy
│   ├── Department of Political Studies
│   ├── Department of Psychology
│   ├── Department of Sociology
│   └── Department of Studies in Women and Gender
├── Faculty of Science and Technology (科学与技术)
│   ├── Department of Biology
│   ├── Department of Chemistry
│   ├── Department of Computer Science
│   ├── Department of Earth Science
│   ├── Department of Fisheries and Aquaculture
│   ├── Department of Geography (BSc)
│   ├── Department of Geoscience
│   ├── Department of Mathematics
│   ├── Department of Physics
│   └── Department of Psychology (BSc)
├── Faculty of Art, Design and Performing Arts (艺术、设计与表演艺术)
│   ├── Department of Visual Art
│   ├── Department of Graphic Design
│   ├── Department of Interior Design
│   └── Department of Theatre
├── Faculty of Business and Management (商业与管理)
│   ├── School of Accounting
│   ├── School of Economics (BBA)
│   ├── School of Financial Services
│   ├── School of Human Resources Management
│   ├── School of International Business
│   ├── School of Management
│   └── School of Marketing
├── Faculty of Education (教育学院)
│   ├── Department of Teacher Education
│   └── Department of Graduate Studies in Education
├── Faculty of Health (健康学院)
│   ├── Department of Kinesiology
│   ├── Department of Nursing
│   └── Department of Dental Hygiene
├── Faculty of Human Services (人类服务学院)
│   ├── School of Social Work
│   ├── Department of Child and Youth Care
│   └── Department of Community Mental Health
├── Faculty of Indigenous Programs (原住民项目学院)
│   ├── Indigenous/Xwulmuxw Studies
│   ├── Indigenous Protected and Conserved Areas Planning
│   └── Professional Indigenous Lands Management
├── Faculty of Tourism, Recreation and Hospitality (旅游、休闲与酒店管理学院)
│   ├── Department of Hospitality Management
│   ├── Department of Tourism Management
│   └── Department of Recreation and Adventure Tourism
├── Trades and Applied Technology (职业技术与应用技术)
│   ├── Automotive Service Technician
│   ├── Baking and Pastry Arts / Culinary Arts
│   ├── Carpentry
│   ├── Electrician
│   ├── Esthetics and Spa Therapy
│   ├── Hairdressing/Hairstylist
│   ├── Heavy Equipment Operator
│   ├── Heavy Mechanical Trades
│   ├── Horticulture Technician
│   ├── Information Technology and Applied Systems
│   ├── Office Administration
│   ├── Professional Baking and Pastry Arts
│   ├── Systems Administration and Cybersecurity
│   └── Welding
└── Graduate Programs (研究生项目)
    ├── Master of Business Administration (MBA)
    ├── Master of Community Planning
    ├── Master of Education in Educational Leadership
    ├── Master of Education in Special Education
    ├── Master of Geographic Information Systems (GIS) Applications
    ├── Master of Arts in Sustainable Leisure Management
    ├── Graduate Diploma in Inclusive Education (Special Education)
    ├── Graduate Diploma in Literacy, Language, and Learning
    ├── Graduate Diploma in Teacher Leadership
    ├── Graduate Certificate in Psychedelic-Assisted Therapy
    └── Post-Degree Diploma in Fisheries and Aquaculture
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 缩写 | 数量 |
|---------|------|------|
| 本科学士 (Bachelor) | BA, BSc, BBA, BFA, BDes, BEd, BScN, BSW, BKin, BHM, BTM, BNRP | ~30+ |
| 本科辅修 (Minor) | Minor | ~30+ |
| 本科文凭 (Diploma) | Dip | ~15+ |
| 本科证书 (Certificate) | Cert | ~15+ |
| 硕士 (Master's) | MBA, MEd, MA, MSc | 6 |
| 研究生文凭 (Graduate Diploma) | GDip | 3 |
| 研究生证书 (Graduate Certificate) | GCert | 1 |
| 博士后文凭 (Post-Degree Diploma) | PDD | 2 |
| 学徒/职业技术证书 | Foundation/Apprenticeship | ~20+ |
| 博士学位 | PhD | 0 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学科领域 | BA/BSc | BBA | BFA/BDes | BEd | BScN/BSW/BKin | Diploma/Cert | Master's | Grad Dip/Cert | Post-Deg Dip |
|---------|--------|-----|---------|-----|-------------|-------------|----------|--------------|-------------|
| Arts, Humanities & Social Sciences | 25+ | - | - | - | - | 2+ | 2 | - | 1 |
| Science & Technology | 15+ | - | - | - | - | 2+ | - | - | 1 |
| Art, Design & Performing Arts | 1 | - | 3 | - | - | 1 | - | - | - |
| Business & Management | - | 7 | - | - | - | 1+ | 1 | - | - |
| Education | - | - | - | 1 | - | 1+ | 2 | 3 | - |
| Health | 1 | - | - | - | 3 | 2+ | - | - | - |
| Human Services | - | - | - | - | 1 | 2+ | - | - | - |
| Indigenous Programs | 1 | - | - | - | - | 2+ | - | - | - |
| Tourism, Recreation & Hospitality | - | - | - | - | - | 2+ | 1 | - | - |
| Trades & Applied Technology | - | - | - | - | - | 15+ | - | - | - |
| **Total (approx)** | **~42** | **7** | **3** | **1** | **4** | **~30** | **6** | **3** | **2** |

---

## Section 1 — Undergraduate Education

### 1.1 艺术、人文与社会科学 (Arts, Humanities and Social Sciences)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Anthropology (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | Anthropology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Anthropology (Major) | BA | Arts, Humanities & Social Sciences | Anthropology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Anthropology (Minor) | Minor | Arts, Humanities & Social Sciences | Anthropology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Aquaculture (Minor) | Minor | Arts, Humanities & Social Sciences | Biology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Biology (BA Minor) | Minor | Arts, Humanities & Social Sciences | Biology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Chemistry (BA Minor) | Minor | Arts, Humanities & Social Sciences | Chemistry | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Computer Science (BA Minor) | Minor | Arts, Humanities & Social Sciences | Computer Science | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Creative Writing and Journalism (Major) | BA | Arts, Humanities & Social Sciences | Creative Writing and Journalism | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Creative Writing and Journalism (Minor) | Minor | Arts, Humanities & Social Sciences | Creative Writing and Journalism | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Criminology (Major) | BA | Arts, Humanities & Social Sciences | Criminology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Criminology (Minor) | Minor | Arts, Humanities & Social Sciences | Criminology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Digital Media Studies (Major) | BA | Arts, Humanities & Social Sciences | Digital Media Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Earth Science (BA Minor) | Minor | Arts, Humanities & Social Sciences | Earth Science | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Economics (Major) | BA | Arts, Humanities & Social Sciences | Economics | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Economics (Minor) | Minor | Arts, Humanities & Social Sciences | Economics | https://www.viu.ca/programs/arts-humanities-social-sciences |
| English (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | English | https://www.viu.ca/programs/arts-humanities-social-sciences |
| English (Major) | BA | Arts, Humanities & Social Sciences | English | https://www.viu.ca/programs/arts-humanities-social-sciences |
| English (Minor) | Minor | Arts, Humanities & Social Sciences | English | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Geography (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | Geography | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Geography (Major) | BA | Arts, Humanities & Social Sciences | Geography | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Geography (Minor) | BA | Arts, Humanities & Social Sciences | Geography | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Global Studies (Major) | BA | Arts, Humanities & Social Sciences | Global Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Global Studies (Minor) | Minor | Arts, Humanities & Social Sciences | Global Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| History (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | History | https://www.viu.ca/programs/arts-humanities-social-sciences |
| History (Major) | BA | Arts, Humanities & Social Sciences | History | https://www.viu.ca/programs/arts-humanities-social-sciences |
| History (Minor) | Minor | Arts, Humanities & Social Sciences | History | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Indigenous/Xwulmuxw Studies (Major) | BA | Arts, Humanities & Social Sciences | Indigenous/Xwulmuxw Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Indigenous/Xwulmuxw Studies (Minor) | Minor | Arts, Humanities & Social Sciences | Indigenous/Xwulmuxw Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Kinesiology (BA Minor) | Minor | Arts, Humanities & Social Sciences | Kinesiology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Languages and Culture (Romance Languages) (Minor) | Minor | Arts, Humanities & Social Sciences | Languages and Culture | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Liberal Studies (Major) | BA | Arts, Humanities & Social Sciences | Liberal Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Liberal Studies (Minor) | Minor | Arts, Humanities & Social Sciences | Liberal Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Mathematics (BA Major) | BA | Arts, Humanities & Social Sciences | Mathematics | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Mathematics (BA Minor) | Minor | Arts, Humanities & Social Sciences | Mathematics | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Media Studies (Minor) | Minor | Arts, Humanities & Social Sciences | Media Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Philosophy (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | Philosophy | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Philosophy (Major) | BA | Arts, Humanities & Social Sciences | Philosophy | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Philosophy (Minor) | Minor | Arts, Humanities & Social Sciences | Philosophy | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Political Studies (Major) | BA | Arts, Humanities & Social Sciences | Political Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Political Studies (Minor) | Minor | Arts, Humanities & Social Sciences | Political Studies | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Psychology (BA Honours) | BA (Honours) | Arts, Humanities & Social Sciences | Psychology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Psychology (BA Major) | BA | Arts, Humanities & Social Sciences | Psychology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Psychology (BA Minor) | Minor | Arts, Humanities & Social Sciences | Psychology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Sociology (Honours) | BA (Honours) | Arts, Humanities & Social Sciences | Sociology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Sociology (Major) | BA | Arts, Humanities & Social Sciences | Sociology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Sociology (Minor) | Minor | Arts, Humanities & Social Sciences | Sociology | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Studies in Women and Gender (Major) | BA | Arts, Humanities & Social Sciences | Studies in Women and Gender | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Studies in Women and Gender (Minor) | Minor | Arts, Humanities & Social Sciences | Studies in Women and Gender | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Visual Art (Major) | BA | Arts, Humanities & Social Sciences | Visual Art | https://www.viu.ca/programs/art-design-performing-arts |
| Visual Art (Minor) | Minor | Arts, Humanities & Social Sciences | Visual Art | https://www.viu.ca/programs/art-design-performing-arts |

### 1.2 科学与技术 (Science and Technology)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Aquaculture (Minor) | BSc (Minor) | Science & Technology | Fisheries and Aquaculture | https://www.viu.ca/programs/science-and-technology |
| Biology (Honours) | BSc (Honours) | Science & Technology | Biology | https://www.viu.ca/programs/science-and-technology |
| Biology (Major) | BSc | Science & Technology | Biology | https://www.viu.ca/programs/science-and-technology |
| Biology (Minor) | BSc (Minor) | Science & Technology | Biology | https://www.viu.ca/programs/science-and-technology |
| Chemistry (Major) | BSc | Science & Technology | Chemistry | https://www.viu.ca/programs/science-and-technology |
| Chemistry (Minor) | BSc (Minor) | Science & Technology | Chemistry | https://www.viu.ca/programs/science-and-technology |
| Computer Science (Co-op) | BSc | Science & Technology | Computer Science | https://www.viu.ca/programs/science-and-technology |
| Computer Science (Honours) | BSc (Honours) | Science & Technology | Computer Science | https://www.viu.ca/programs/science-and-technology |
| Computer Science (Major) | BSc | Science & Technology | Computer Science | https://www.viu.ca/programs/science-and-technology |
| Computer Science (Minor) | BSc (Minor) | Science & Technology | Computer Science | https://www.viu.ca/programs/science-and-technology |
| Earth Science (Minor) | BSc (Minor) | Science & Technology | Earth Science | https://www.viu.ca/programs/science-and-technology |
| Geography (Minor) | BSc (Minor) | Science & Technology | Geography | https://www.viu.ca/programs/science-and-technology |
| Geoscience (Major) | BSc | Science & Technology | Geoscience | https://www.viu.ca/programs/science-and-technology |
| Mathematics (Major) | BSc | Science & Technology | Mathematics | https://www.viu.ca/programs/science-and-technology |
| Mathematics (Minor) | BSc (Minor) | Science & Technology | Mathematics | https://www.viu.ca/programs/science-and-technology |
| Physics (Transfer Program) | BSc (Transfer) | Science & Technology | Physics | https://www.viu.ca/programs/science-and-technology |
| Psychology (Honours) | BSc (Honours) | Science & Technology | Psychology | https://www.viu.ca/programs/science-and-technology |
| Psychology (Major) | BSc | Science & Technology | Psychology | https://www.viu.ca/programs/science-and-technology |
| Psychology (Minor) | BSc (Minor) | Science & Technology | Psychology | https://www.viu.ca/programs/science-and-technology |
| Bachelor of Natural Resource Protection | BNRP | Science & Technology | Fisheries and Aquaculture | https://www.viu.ca/programs/science-and-technology |
| Bachelor of Science in Fisheries and Aquaculture | BSc | Science & Technology | Fisheries and Aquaculture | https://www.viu.ca/programs/science-and-technology |

### 1.3 艺术、设计与表演艺术 (Art, Design and Performing Arts)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Bachelor of Design in Graphic Design | BDes | Art, Design & Performing Arts | Graphic Design | https://www.viu.ca/programs/art-design-performing-arts |
| Bachelor of Fine Arts – Theatre Transfer | BFA | Art, Design & Performing Arts | Theatre | https://www.viu.ca/programs/art-design-performing-arts |
| Bachelor of Interior Design | BID | Art, Design & Performing Arts | Interior Design | https://www.viu.ca/programs/art-design-performing-arts |

### 1.4 商业与管理 (Business and Management)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Accounting (Major) | BBA | Business & Management | Accounting | https://www.viu.ca/programs/business-management |
| Economics (Major) | BBA | Business & Management | Economics | https://www.viu.ca/programs/business-management |
| Financial Services (Major) | BBA | Business & Management | Financial Services | https://www.viu.ca/programs/business-management |
| Human Resources Management (Major) | BBA | Business & Management | Human Resources Management | https://www.viu.ca/programs/business-management |
| Human Resources Management (Minor) | Minor | Business & Management | Human Resources Management | https://www.viu.ca/programs/business-management |
| International Business (Major) | BBA | Business & Management | International Business | https://www.viu.ca/programs/business-management |
| International Business (Minor) | Minor | Business & Management | International Business | https://www.viu.ca/programs/business-management |
| Management (Major) | BBA | Business & Management | Management | https://www.viu.ca/programs/business-management |
| Management (Minor) | Minor | Business & Management | Management | https://www.viu.ca/programs/business-management |
| Marketing (Major) | BBA | Business & Management | Marketing | https://www.viu.ca/programs/business-management |
| Marketing (Minor) | Minor | Business & Management | Marketing | https://www.viu.ca/programs/business-management |
| Certificate in Business Management | Cert | Business & Management | Business Management | https://www.viu.ca/programs/business-management |

### 1.5 教育 (Education)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Bachelor of Education | BEd | Education | Teacher Education | https://www.viu.ca/programs/education |
| Bachelor of Education - Post Baccalaureate | BEd (Post-Bacc) | Education | Teacher Education | https://www.viu.ca/programs/education |
| Early Childhood Education and Care Certificate | Cert | Education | Early Childhood Education | https://www.viu.ca/programs/education |
| Early Childhood Education and Care Diploma | Dip | Education | Early Childhood Education | https://www.viu.ca/programs/education |

### 1.6 健康 (Health)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Bachelor of Kinesiology | BKin | Health | Kinesiology | https://www.viu.ca/programs/health |
| Bachelor of Science in Nursing | BScN | Health | Nursing | https://www.viu.ca/programs/health |
| Kinesiology (BA Minor) | Minor (BA) | Health / Arts | Kinesiology | https://www.viu.ca/programs/health |

### 1.7 人类服务 (Human Services)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Bachelor of Social Work | BSW | Human Services | Social Work | https://www.viu.ca/programs/human-services |
| Child and Youth Care Diploma | Dip | Human Services | Child and Youth Care | https://www.viu.ca/programs/human-services |
| Child and Youth Care First Nations Diploma | Dip | Human Services | Child and Youth Care | https://www.viu.ca/programs/human-services |

### 1.8 原住民项目 (Indigenous Programs)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Indigenous/Xwulmuxw Studies (BA Major) | BA | Indigenous Programs | Indigenous Studies | https://www.viu.ca/programs/indigenous |
| Indigenous/Xwulmuxw Studies (BA Minor) | Minor | Indigenous Programs | Indigenous Studies | https://www.viu.ca/programs/indigenous |
| Indigenous Protected and Conserved Areas Planning Advanced Certificate | Adv Cert | Indigenous Programs | Indigenous Lands Management | https://www.viu.ca/programs/indigenous |
| Professional Indigenous Lands Management Certificate | Cert | Indigenous Programs | Indigenous Lands Management | https://www.viu.ca/programs/indigenous |

### 1.9 旅游、休闲与酒店管理 (Tourism, Recreation and Hospitality)

| Program Name | Degree | School/College | Department | URL |
|-------------|--------|---------------|-----------|-----|
| Bachelor of Hospitality Management | BHM | Tourism, Recreation & Hospitality | Hospitality Management | https://www.viu.ca/programs/tourism-recreation-hospitality |
| Bachelor of Tourism Management | BTM | Tourism, Recreation & Hospitality | Tourism Management | https://www.viu.ca/programs/tourism-recreation-hospitality |
| Hospitality Management Diploma | Dip | Tourism, Recreation & Hospitality | Hospitality Management | https://www.viu.ca/programs/tourism-recreation-hospitality |
| Certificate in Adventure Tourism and Recreation | Cert | Tourism, Recreation & Hospitality | Adventure Tourism | https://www.viu.ca/programs/tourism-recreation-hospitality |
| Event Management Certificate | Cert | Tourism, Recreation & Hospitality | Event Management | https://www.viu.ca/programs/tourism-recreation-hospitality |

### 1.10 职业技术与应用技术 (Trades and Applied Technology)

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Automotive Service Technician | Foundation/Apprenticeship | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Baking and Pastry Arts Management | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Business Information Technology Systems Diploma | Dip | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Carpentry | Foundation/Apprenticeship | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Culinary Arts / Culinary Management | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Electrician | Foundation/Apprenticeship | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Esthetics and Spa Therapy Certificate | Cert | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Hairstylist Foundation | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Heavy Equipment Operator | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Heavy Mechanical Trades Foundation | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Horticulture Technician Foundation | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Office Administration Certificate | Cert | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Professional Baking and Pastry Arts | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Systems Administration and Cybersecurity Diploma | Dip | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |
| Welder Fitter / Welder Foundation | Foundation | Trades & Applied Technology | https://www.viu.ca/programs/trades-applied-technology |

### 1.11 特殊项目 / 预科

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Academic and Career Preparation (ABE) | Non-credit | Academic and Career Preparation | https://www.viu.ca/programs/academic-career-preparation |
| English Language Learning (ELL) | Non-credit | English Language Learning | https://www.viu.ca/programs/english-language-learning |
| Exploratory University Studies (EXPO) | Non-degree | Exploratory University Studies | https://www.viu.ca/programs/exploratory-university-studies |
| Canadian University Foundation Year (CUFY) | Foundation (Intl) | International | https://www.viu.ca/admissions/international |
| Engineering Transfer Certificate/Diploma | Transfer | Science & Technology | https://www.viu.ca/programs/science-and-technology |

---

## Section 2 — Graduate Education

### Master's Degrees

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Master of Business Administration (MBA) | MBA | Business & Management | https://www.viu.ca/programs/graduate-programs |
| Master of Education in Educational Leadership | MEd | Education | https://www.viu.ca/programs/graduate-programs |
| Master of Education in Special Education | MEd | Education | https://www.viu.ca/programs/graduate-programs |
| Master of Community Planning | MCP | Arts, Humanities & Social Sciences | https://www.viu.ca/programs/graduate-programs |
| Master of Geographic Information Systems (GIS) Applications | MGISA | Arts, Humanities & Social Sciences | https://www.viu.ca/programs/graduate-programs |
| Master of Arts in Sustainable Leisure Management | MA | Tourism, Recreation & Hospitality | https://www.viu.ca/programs/graduate-programs |

### Graduate Diplomas

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Inclusive Education (Special Education) Graduate Diploma | GDip | Education | https://www.viu.ca/programs/education |
| Literacy, Language, and Learning Graduate Diploma | GDip | Education | https://www.viu.ca/programs/education |
| Teacher Leadership Graduate Diploma | GDip | Education | https://www.viu.ca/programs/education |

### Graduate Certificates

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Psychedelic-Assisted Therapy Graduate Certificate | GCert | Health | https://www.viu.ca/programs/graduate-programs |

### Post-Degree Diplomas

| Program Name | Degree | School/College | URL |
|-------------|--------|---------------|-----|
| Post-Degree Diploma in Fisheries and Aquaculture | PDD | Science & Technology | https://www.viu.ca/programs/graduate-programs |
| Post-Degree Diploma in Languages and Culture (Romance Languages) | PDD | Arts, Humanities & Social Sciences | https://www.viu.ca/programs/arts-humanities-social-sciences |
| Post-Degree Diploma in Natural Resource Law Enforcement | PDD | Science & Technology | https://www.viu.ca/programs/science-and-technology |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 本科入学基本要求

**加拿大公民/永久居民 (Domestic):**
- 满足以下任一条件：
  1. BC省高中毕业（或同等学历），英语12或English First Peoples 12成绩不低于C
  2. 持有认可大学的前学位
  3. 转学生（完成至少24个可转学分的大学课程）
  4. 成年学生类别（21岁或以上，英语12或English First Peoples 12成绩不低于C）

**BC省高中录取平均分参考：**
- 开放录取（Open Admission）项目：满足最低要求即可
- 限额录取（Limited Entry）项目：竞争性录取，名额有限

**国际学生 (International):**
- 高中毕业，成绩相当于BC省英语12的C级
- 母语非英语者需提供英语能力证明

### 3.2 英语语言能力要求 (English Language Proficiency)

**本科课程 (UG Academic/Vocational Programs):**

| 考试类型 | 最低分数要求 |
|---------|------------|
| TOEFL iBT | 88 (单项不低于20) 或 4.5 (新评分体系单项不低于4.0) |
| TOEFL iBT Paper Edition | 550 (单项不低于56) |
| IELTS (Academic) | 6.5 (单项不低于6.0) |
| CAEL | 60 |
| C2 Proficiency (CPE) | 176 overall |
| C1 Advanced (CAE) | 176 overall |
| Pearson (PTE) Academic | 60 (单项不低于60) |
| Duolingo English Test | 115 (单项不低于105) |
| English Studies 12 (BC) | 最低C级 |
| International Baccalaureate English A1/A2 HL/SL | 3级或以上 |
| AP English Language/Composition or Literature | 2级或以上 |
| VIU English Language Centre | 完成University Preparation Level 5 (UP5) |
| GCSE O-level English | C或4级 |
| ILAC Pathway Program | Successful Completion of Pathway 3.3 |

**研究生课程 (Graduate Programs):**

| 考试类型 | 最低分数要求 |
|---------|------------|
| TOEFL iBT | 88 (单项不低于20) 或 4.5 (单项不低于4.0) |
| IELTS (Academic) | 6.5 (单项不低于6.0) |
| CAEL | 60 |
| Pearson (PTE) Academic | 60 (单项不低于60) |
| Duolingo English Test | 115 (单项不低于105) |
| C2 Proficiency (CPE) | 176 overall |
| C1 Advanced (CAE) | 176 overall |
| VIU English Language Centre | 完成UP5 |

**豁免条件：**
- 在以下英语国家完成高中或学位：持有认证英语授课院校的文凭/学位（2年以上课程）
- 在英语为主要教学语言的认证院校完成6学分的大学英语写作与文学课程，成绩不低于C
- 不需要GMAT或GRE成绩

### 3.3 申请费

| 申请人类别 | 费用 (CAD) |
|-----------|-----------|
| 加拿大本地本科 | $46.98 |
| 加拿大本地研究生 | $121.86 |
| 国际学生（所有项目） | $156.06 |
| 成人基础教育 (ABE) | 免费 |

### 3.4 申请截止日期

| 项目 | 日期 |
|-----|------|
| 大多数学术项目申请开放 | 每年10月1日（开学前一年） |
| 具体截止日期 | 因项目而异，请查看具体项目页面 |
| 限额录取项目 | 建议尽早提交申请，竞争激烈 |
| 国际学生 | 建议比本地学生提前2-3个月申请 |

### 3.5 其他入学要求

- IB/AP学分：IB Higher Level或AP 4级以上可获得最多30个大学学分
- 转学分：最多60个学分可转入VIU学位
- 项目特定要求：部分项目（护理、社会工作、犯罪学等）有额外入学要求和竞争性录取流程
- 实习/合作教育：通过EducationPlannerBC申请

### 3.6 申请流程

1. 选择项目
2. 通过EducationPlannerBC申请
3. 提交所需文件（成绩单、英语能力证明等）
4. 等待录取决定
5. 接受录取并支付学费押金
6. 注册课程

---

## Section 4 — Costs & Financial Aid

### 4.1 学费标准（加拿大本地学生 Domestic）

| 项目类别 | 费用 (CAD) |
|---------|-----------|
| 学分制本科项目 | $173.12/学分 |
| 成人基础教育 (ABE) | 免费（政府政策） |
| 合作教育 (Co-op) | $751.87/学期 |
| 职业技术全日制 | $519.36/月 |
| 职业技术非全日制 | $311.64/月 |
| 学徒制项目 | $119.88/周 |

**差异化学费项目 (部分示例):**

| 项目 | 费用 (CAD) |
|------|-----------|
| 社会工作学士 (BSW) | $471.06/学分（60学分） |
| 牙科卫生 (Dental Hygiene) | $260.02/学分 |
| 实用护理 (Practical Nursing) | $230.90/学分 |
| 室内设计 (Interior Design) | 年度实验室费用 |
| 活动助理证书 | $427.52/学分 |
| 高级GIS文凭 | $376.24/学分 |
| 社区心理健康工作证书 | $335.14/学分 |
| 商业管理证书 | $419.94/学分 |

### 4.2 学费标准（国际学生 International）

| 项目类别 | 费用 (CAD) |
|---------|-----------|
| 本科、文凭和证书项目 | $832.09/学分 |
| 职业技术项目 | $2,496.25/月 |
| 英语语言学习 (ELL) 全学期(14周) | $5,853.25 |
| 英语语言学习 (ELL) 半学期(6.5周) | $2,926.62 |
| 合作教育 (Co-op) | $2,496.25/学期 |

**研究生国际学费:**

| 项目 | 费用 (CAD) |
|------|-----------|
| MBA | $771.12/学分 |
| MEd Educational Leadership | $704.62/学分 |
| MEd Special Education | $704.62/学分 |
| MA Sustainable Leisure Management | $854.08/学分 |
| Master of Community Planning | $587.17/学分 |
| MGISA | $655.45/学分 |
| 心理辅助治疗研究生证书 | $781.09/学分 |

### 4.3 研究生费用（本地）

| 项目 | 费用 (CAD) |
|------|-----------|
| MBA | $454.84/学分 |
| MEd Educational Leadership | $471.38/学分 |
| MEd Special Education | $471.38/学分 |
| MA Sustainable Leisure Management | $469.02/学分 |
| Master of Community Planning | $369.89/学分 |
| MGISA Year 1 | $376.24/学分 |
| MGISA Year 2 | $505.87/学分 |
| Inclusive Education Graduate Diploma | $462.14/学分 |
| Psychedelic-Assisted Therapy Graduate Certificate | $557.46/学分 |

### 4.4 其他费用

| 费用项目 | 金额 (CAD) |
|---------|-----------|
| 学生活动费 | $20.78/月 |
| 学生服务费 | $22.94/月 |
| 毕业与校友费 | $60.92/次 |
| 补办证书/文凭 | $68.30/份 |
| 退票费 | $38.75/次 |
| 滞纳金 | 逾期金额的5% |
| 65岁以上老年人免学费 | 适用于学术本科课程（空间允许） |

### 4.5 奖学金与经济援助

- 每年发放超过$670万加元的奖学金、助学金和奖励
- 每年2000+项奖学金、奖项和助学金
- 一般要求：最低GPA 3.50（A-），课程负荷80%（大多12学分）
- 国际学生也有部分奖学金可申请
- 外部资助机会：$2,120万加元的外部资金
- 校内就业机会：Work-Op, Non Work-Op (含研究), Canada Summer Jobs

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-U-001 | institution.name | Vancouver Island University (VIU) | https://www.viu.ca/ | official_webpage |
| E-U-002 | total_students | 12,644 | https://www.viu.ca/key-facts | official_webpage |
| E-U-003 | international_students | 1,381 | https://www.viu.ca/key-facts | official_webpage |
| E-U-004 | indigenous_students | 1,700 | https://www.viu.ca/key-facts | official_webpage |
| E-U-005 | alumni_count | 100,000+ | https://www.viu.ca/key-facts | official_webpage |
| E-U-006 | faculty_staff_count | 2,000+ | https://www.viu.ca/key-facts | official_webpage |
| E-U-007 | program_count | 100+ | https://www.viu.ca/key-facts | official_webpage |
| E-U-008 | campuses | Nanaimo (main), Cowichan, tiwšɛmawtxʷ (Powell River) | https://www.viu.ca/ | official_webpage |
| E-U-009 | domestic_ug_tuition_per_credit | $173.12/credit | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-010 | domestic_trades_tuition_monthly | $519.36/month | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-011 | international_ug_tuition_per_credit | $832.09/credit | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-012 | international_trades_tuition_monthly | $2,496.25/month | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-013 | application_fee_domestic_ug | $46.98 | https://www.viu.ca/admissions/fees | official_webpage |
| E-U-014 | application_fee_domestic_grad | $121.86 | https://www.viu.ca/admissions/fees | official_webpage |
| E-U-015 | application_fee_international | $156.06 | https://www.viu.ca/admissions/fees | official_webpage |
| E-U-016 | elp_ielts_minimum_ug | 6.5 (no band below 6.0) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-017 | elp_toefl_minimum_ug | 88 (no section below 20) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-018 | elp_duolingo_minimum_ug | 115 (no band less than 105) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-019 | elp_pte_minimum_ug | 60 (no section below 60) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-020 | elp_ielts_minimum_grad | 6.5 (no band below 6.0) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-021 | elp_toefl_minimum_grad | 88 (no section below 20) | https://www.viu.ca/admissions/international | official_webpage |
| E-U-022 | graduate_admission_gpa | Minimum B average in final 2 years | https://www.viu.ca/admissions/international | official_webpage |
| E-U-023 | no_gmat_gre_required | No GMAT or GRE scores required | https://www.viu.ca/admissions/international | official_webpage |
| E-U-024 | application_deadline_opening | October 1 prior to start year | https://www.viu.ca/admissions | official_webpage |
| E-U-025 | student_activity_fee | $20.78/month | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-026 | student_services_fee | $22.94/month | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-027 | scholarship_amount_annual | $6.7 million | https://www.viu.ca/tuition-and-aid | official_webpage |
| E-U-028 | co_op_fee | $751.87/semester (domestic) | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-029 | program_areas_count | 10 areas of study | https://www.viu.ca/programs/undergraduate-programs | official_webpage |
| E-U-030 | mba_tuition_international | $771.12/credit | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |
| E-U-031 | mba_tuition_domestic | $454.84/credit | https://www.viu.ca/admissions/tuition-fee-schedule | official_webpage |

---

## Section 6 — WeKnora Import Manifest

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Notes |
|----------|-----------|-------|
| **P0** | 全量项目详细描述 | 项目详情页内容需要逐项采集（每个program的具体页面） |
| **P0** | 各项目具体申请截止日期 | 因项目而异，需逐项查看 |
| **P0** | 各限额录取项目的竞争性录取标准 | 具体录取平均分/GPA要求 |
| **P1** | 住宿费用 | 校内住宿10栋楼，费用未在网站直接列出 |
| **P1** | 大一新生入学要求细节 | 是否需要SAT/ACT等 |
| **P1** | 转学生学分评估细则 | 转学学分上限60 |
| **P1** | 奖学金具体列表 | 2000+项奖学金的具体类别和金额 |
| **P2** | 校园设施详情 | 图书馆、实验室等 |
| **P2** | 国际学生支持服务 | 国际学生中心服务详情 |
| **P2** | BC省 Student Aid 具体政策 | 贷款额度等 |

### Cache Write

- Site memory: written to `uni-cache/schools/viu/site-memory.json`
- Content hashes: written to `uni-cache/schools/viu/content-hashes.json`
- Last extract: written to `uni-cache/schools/viu/last-extract.json`

---

## Section 7 — Cross-School Comparison Framework

| Dimension | Vancouver Island University (VIU) |
|-----------|----------------------------------|
| Total UG programmes | ~70+ (major/minor/honours) |
| Total Graduate programmes | 10 (6 Master's, 3 Grad Dip, 1 Grad Cert) |
| PhD programmes | 0 |
| Total students | 12,644 |
| International students | 1,381 (11%) |
| Indigenous students | 1,700 (13.4%) |
| Alumni | 100,000+ |
| Faculty/Staff | 2,000+ |
| Province | British Columbia (BC) |
| Campuses | 3 (Nanaimo, Cowichan, Powell River) |
| Application system | EducationPlannerBC |
| Domestic tuition (per credit) | $173.12 (base) |
| International tuition (per credit) | $832.09 (base) |
| Minimum IELTS UG | 6.5 (6.0) |
| Minimum IELTS Grad | 6.5 (6.0) |
| No GMAT/GRE required | Yes |
| PhD granted | No |
| PUU (Primarily Undergraduate) | No (has graduate programs but no PhD) |
| Maclean's category | Primarily Undergraduate (中型本科为主) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: University official website (www.viu.ca)
> **Granularity**: faculty → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (~70+ listed) | PG programmes ✅ (10 listed) | Trades/Vocational ✅ (~15+) | Evidence (31 blocks) ✅
> **Next step**: P0 items require individual program page extraction for detailed descriptions, specific deadlines, and competitive admission statistics
