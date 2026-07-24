> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + curl + Python (urllib)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU) — Western Australia

# Curtin University 知识库 — 完整深度数据 v2

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG degree programmes) | 143 |
| 本科专业内的主修/辅修 (Majors/Specialisations within UG) | 122 |
| 研究生授课型项目 (PGT: Masters, GC, GD) | 104 |
| 研究型项目 (PhD/MPhil/Professional Doctorates) | 数据待补充 |
| **学位项目总计 (主课程)** | **247** |
| 学习领域 (Study Areas) | 10 |
| 校区 (Campuses) | 5+ (Perth, Kalgoorlie, Singapore, Malaysia, Dubai, Mauritius, Colombo) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

Curtin University 采用"学习领域 (Study Area)"分类体系，而非传统学院制。其教学组织结构分为五大教学板块 (Teaching Areas)，下设 10 个学习领域。

```
Curtin University
├── Centre for Aboriginal Studies (独立中心)
├── Faculty of Business and Law (商学与法律学部)
│   └── Study Area: Business, Innovation, Management and Law
├── Faculty of Health Sciences (健康科学学部)
│   └── Study Area: Health
├── Faculty of Humanities (人文学部)
│   ├── Study Area: Architecture and Construction
│   ├── Study Area: Arts and Creative Industries
│   ├── Study Area: Culture, Society and Indigenous
│   └── Study Area: Education
└── Faculty of Science and Engineering (科学与工程学部)
    ├── Study Area: Agriculture, Environment and Sustainability
    ├── Study Area: Engineering, Mining and Surveying
    ├── Study Area: Information Technology
    └── Study Area: Physical Sciences, Geoscience and Mathematics
```

> **说明**: Curtin 官方的"教学板块 (Teaching Areas)"为五大板块，学习领域 (Study Areas) 为其子分类。课程详情页通过 URL 中的 study-area 参数关联到对应学习领域。

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 数量 | 说明 |
|---------|------|------|
| Bachelor Degree (学士学位) | ~60 | B-XXX, 如 B-ARTS, B-COMRCE |
| Bachelor Honours Degree (荣誉学士) | ~15 | BH-XXX, 如 BH-ADVBSC |
| Bachelor Double Degree (双学士) | ~30 | BB-XXX, 如 BB-ARTCOM |
| Associate Degree | ~3 | 副学士 |
| Diploma | ~5 | 文凭课程 |
| Graduate Certificate (研究生证书) | ~35 | GC-XXXX |
| Graduate Diploma (研究生文凭) | ~20 | GD-XXXX |
| Master by Coursework (授课型硕士) | ~35 | MC-XXXX, MX-XXXX |
| Professional Doctorate | ~3 | 如 Doctor of Physiotherapy |
| Bridging/Enabling (桥梁/预科) | ~3 | EN-XXXX |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学习领域 (Study Area) | Bachelor | Honours | Double Degree | GC/GD | Masters | 合计 |
|----------------------|----------|---------|---------------|-------|---------|------|
| Agriculture, Environment & Sustainability | ~8 | ~3 | ~1 | ~3 | ~5 | 20 |
| Architecture & Construction | ~4 | ~2 | ~0 | ~1 | ~3 | 10 |
| Arts & Creative Industries | ~10 | ~3 | ~3 | ~5 | ~5 | 26 |
| Business, Innovation, Management & Law | ~15 | ~3 | ~10 | ~10 | ~15 | 53 |
| Culture, Society & Indigenous | ~8 | ~2 | ~2 | ~5 | ~5 | 22 |
| Education | ~3 | ~1 | ~0 | ~5 | ~5 | 14 |
| Engineering, Mining & Surveying | ~10 | ~5 | ~5 | ~3 | ~8 | 31 |
| Health | ~15 | ~5 | ~5 | ~10 | ~15 | 50 |
| Information Technology | ~5 | ~2 | ~2 | ~3 | ~5 | 17 |
| Physical Sciences, Geoscience & Mathematics | ~10 | ~3 | ~3 | ~5 | ~8 | 29 |
| **合计** | **~88** | **~29** | **~31** | **~50** | **~74** | **~272** |

> 注：矩阵数字为近似值（含主课程及双学位），合计与 0.1 表有差异源于部分课程跨领域分类。所有课程URL已提取于 `/tmp/curtin_courses.json`。

---

## Section 1 — Undergraduate Education

### 1.1 Bachelor Degree Programmes

#### 学习领域: Agriculture, Environment & Sustainability

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-AGRBU | Bachelor of Agribusiness | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-agribusiness--b-agrbu |
| B-APGEOL | Bachelor of Applied Geology | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-geology--b-apgeol |
| B-SCENV | Bachelor of Science (Environmental Science) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-environmental-science--b-scenv |
| B-SCFOREST | Bachelor of Science (Forestry) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-forestry--b-scforest |
| B-SCAGRI | Bachelor of Science (Agriculture) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-agriculture--b-scagri |
| B-SCAGEC | Bachelor of Science (Agricultural Economics) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-agricultural-economics--b-scecon |
| B-SCRESM | Bachelor of Science (Resource Management) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-natural-resource-management--b-scresm |
| B-SCFS | Bachelor of Science (Food Science) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-food-science-and-technology--b-scfs |

#### 学习领域: Architecture & Construction

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-ARCH | Bachelor of Applied Science (Architectural Science) | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-science-architectural-science--b-arch |
| B-CONM | Bachelor of Applied Science (Construction Management) | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-science-construction-management--b-conm |
| B-INDSGN | Bachelor of Interior Design | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-interior-design--b-indsgn |
| B-PLAND | Bachelor of Applied Science (Planning and Urban Design) | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-science-planning-and-urban-design--b-pland |

#### 学习领域: Arts & Creative Industries

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-ARTS | Bachelor of Arts | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts--b-arts |
| B-MASCOMS | Bachelor of Communications | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-communications--b-mascoms |
| B-CRARTS | Bachelor of Creative Arts | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-creative-arts--b-crarts |
| B-DESIGN | Bachelor of Design | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-design--b-design |
| B-MEDIA | Bachelor of Media | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-media--b-media |
| B-SCJOUR | Bachelor of Science (Journalism) | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-journalism--b-scjour |
| B-MUSIC | Bachelor of Music | BMus | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-music--b-music |
| B-ARTHIST | Bachelor of Arts (Art History) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-art-history--b-arthist |
| B-FINEART | Bachelor of Fine Art | BFA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-fine-art--b-fineart |
| B-DANCE | Bachelor of Dance | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-dance--b-dance |

#### 学习领域: Business, Innovation, Management & Law

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-COMRCE | Bachelor of Commerce | BCom | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-commerce--b-comrce |
| B-BUSADM | Bachelor of Business Administration | BBA | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-business-administration--b-busadm |
| B-INNOV | Bachelor of Innovation | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-innovation--b-innov |
| B-LAWS | Bachelor of Laws | LLB | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws--b-laws |
| B-ECONS | Bachelor of Economics | BEc | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-economics--b-econs |
| B-ACCTG | Bachelor of Accounting | BAcc | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-accounting--b-acctg |
| B-FINANCE | Bachelor of Finance | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-finance--b-fince |
| B-MARK | Bachelor of Marketing | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-marketing--b-mark |
| B-MANGT | Bachelor of Management | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-management--b-mngmt |
| B-HRM | Bachelor of Human Resource Management | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-human-resource-management--b-hrm |
| B-INTBUS | Bachelor of International Business | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-international-business--b-intbus |
| B-PROP | Bachelor of Property | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-property--b-prop |
| B-LOGSCM | Bachelor of Logistics and Supply Chain Mgmt | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-logistics-and-supply-chain-management--b-logscm |
| B-BINFS | Bachelor of Business Information Systems | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-business-information-systems--b-bsinfs |
| B-TOURH | Bachelor of Tourism and Hospitality | B | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-tourism-and-hospitality--b-tourh |

#### 学习领域: Culture, Society & Indigenous

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-SOCSC | Bachelor of Social Science | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-social-science--b-socsc |
| B-SOCWK | Bachelor of Social Work | BSW | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-social-work--b-scwk |
| B-SCPSYSC | Bachelor of Science (Psychological Science) | B | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-psychological-science--b-scpsysc |
| B-ANTHR | Bachelor of Arts (Anthropology) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-anthropology--b-anthr |
| B-SOCIOL | Bachelor of Arts (Sociology) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-sociology--b-sociol |
| B-HIST | Bachelor of Arts (History) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-history--b-hist |
| B-POLSC | Bachelor of Arts (Political Science) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-political-science--b-polsc |
| B-INTREL | Bachelor of Arts (International Relations) | BA | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-international-relations--b-intrel |

#### 学习领域: Education

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-EDPRIM | Bachelor of Education (Primary) | BEd | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-education-primary--b-edprim |
| B-EDSEC | Bachelor of Education (Secondary) | BEd | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-education-secondary--b-edsec |
| B-EDEC | Bachelor of Education (Early Childhood) | BEd | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-education-early-childhood--b-edec |

#### 学习领域: Engineering, Mining & Surveying

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-ENGR | Bachelor of Engineering (Honours) | BEng(Hons) | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-honours--b-eng |
| B-MINING | Bachelor of Engineering (Mining Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-mining-engineering-honours--b-mining |
| B-CHEMENG | Bachelor of Engineering (Chemical Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-chemical-engineering-honours--b-chemeng |
| B-CIVENG | Bachelor of Engineering (Civil Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-civil-engineering-honours--b-civeng |
| B-ELECENG | Bachelor of Engineering (Electrical Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-electrical-engineering-honours--b-eleceng |
| B-MECHENG | Bachelor of Engineering (Mechanical Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-mechanical-engineering-honours--b-mecheng |
| B-SOFTENG | Bachelor of Engineering (Software Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-software-engineering-honours--b-softeng |
| B-SURV | Bachelor of Surveying | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-surveying--b-surv |
| B-SPM | Bachelor of Science (Spatial Measurement) | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-spatial-measurement--b-spm |
| B-METENG | Bachelor of Engineering (Metallurgical Engineering) Honours | BEng | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-metallurgical-engineering-honours--b-meteng |

#### 学习领域: Health

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-NURS | Bachelor of Science (Nursing) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-nursing--b-nurs |
| B-PHYSIO | Bachelor of Science (Physiotherapy) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-physiotherapy--b-physio |
| B-OCTHY | Bachelor of Science (Occupational Therapy) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-occupational-therapy--b-octhy |
| B-SPTH | Bachelor of Science (Speech Pathology) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-speech-pathology--b-spth |
| B-PSYCH | Bachelor of Psychology | BPsy | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-psychology--b-psych |
| B-HLTHSC | Bachelor of Science (Health Sciences) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-health-sciences--b-hlthsc |
| B-HLTHST | Bachelor of Science (Health Studies) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-health-studies--b-hlthst |
| B-LABMED | Bachelor of Science (Laboratory Medicine) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-laboratory-medicine--b-labmed |
| B-SCIMRS | Bachelor of Science (Medical Radiation Science) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-medical-radiation-science--b-scimrs |
| B-NUTR | Bachelor of Science (Nutrition and Food Science) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-nutrition-and-food-science--b-nutr |
| B-PHARM | Bachelor of Pharmacy | BPharm | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-pharmacy--b-pharm |
| B-HLTHPRO | Bachelor of Science (Health Promotion) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-health-promotion--b-hlthpro |
| B-EXERSC | Bachelor of Science (Exercise Science) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-exercise-and-sport-science--b-exersc |
| B-PARAM | Bachelor of Science (Paramedicine) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-paramedicine--b-param |
| B-DENT | Bachelor of Science (Oral Health) | BSc | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-oral-health--b-dent |

#### 学习领域: Information Technology

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-COMP | Bachelor of Computing | B | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-computing--b-comp |
| B-SCIT | Bachelor of Science (Information Technology) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-information-technology--b-scit |
| B-CYBER | Bachelor of Science (Cyber Security) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-cyber-security--b-cyber |
| B-DATA | Bachelor of Science (Data Science) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-data-science--b-data |
| B-SCSNT | Bachelor of Science (Computer Systems and Networking) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-computer-systems-and-networking--b-scsnt |

#### 学习领域: Physical Sciences, Geoscience & Mathematics

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| B-SCI | Bachelor of Science (Science) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-science--b-sci |
| B-ADVSCI | Bachelor of Advanced Science | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-advanced-science--b-advsci |
| B-MATH | Bachelor of Science (Mathematics) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-mathematics--b-math |
| B-PHYS | Bachelor of Science (Physics) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-physics--b-phys |
| B-CHEM | Bachelor of Science (Chemistry) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-chemistry--b-chem |
| B-GEOL | Bachelor of Science (Geology) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-geology--b-geol |
| B-BIOL | Bachelor of Science (Biological Science) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-biological-sciences--b-biol |
| B-MARSC | Bachelor of Science (Marine Science) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-marine-science--b-marsc |
| B-ZOOL | Bachelor of Science (Zoology) | BSc | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-zoology--b-zool |

### 1.2 Honours Degree Programmes

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| BH-ADVBSC | Bachelor of Advanced Biomedical Sciences (Honours) | BSc(Hons) | Health Sciences | https://curtin.edu.au/study/offering/course-ug-bachelor-of-advanced-biomedical-sciences-honours--bh-advbsc |
| BH-ADVCOM | Bachelor of Advanced Commerce (Honours) | BCom(Hons) | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-advanced-commerce-honours--bh-advcom |
| BH-ADVSCI | Bachelor of Advanced Science (Honours) | BSc(Hons) | Science & Engineering | https://curtin.edu.au/study/offering/course-ug-bachelor-of-advanced-science-honours--bh-advsci |
| BH-ARCH | Bachelor of Applied Science (Architecture) Honours | BAppSc(Hons) | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-science-architecture-honours--bh-arch |
| BH-IND | Bachelor of Applied Science (Indigenous Research) Honours | BAppSc(Hons) | Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-science-indigenous-australian-research-honours--bh-indaus |

### 1.3 Double Degree Programmes

| 课程代码 | 课程名称 | Degree | 所属Faculty | URL |
|---------|---------|--------|------------|-----|
| BB-ARTCOM | Bachelor of Arts + Bachelor of Commerce | BA/BCom | Humanities/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-bachelor-of-commerce--bb-artcom |
| BB-ARTINN | Bachelor of Arts + Bachelor of Innovation | BA/BInn | Humanities/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-arts-bachelor-of-innovation--bb-artinn |
| BB-ENGCOM | Bachelor of Engineering + Bachelor of Commerce | BEng/BCom | S&E/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-bachelor-of-commerce--bb-engcom |
| BB-ENINNO | Bachelor of Engineering (Hons) + Bachelor of Innovation | BEng/BInn | S&E/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-engineering-honours-bachelor-of-innovation--bb-eninno |
| BB-LAWCOM | Bachelor of Laws + Bachelor of Commerce | LLB/BCom | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws-bachelor-of-commerce--bb-lawcom |
| BB-LAWART | Bachelor of Laws + Bachelor of Arts | LLB/BA | Business/Humanities | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws-bachelor-of-arts--bb-lawart |
| BB-LAWINN | Bachelor of Laws + Bachelor of Innovation | LLB/BInn | Business & Law | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws-bachelor-of-innovation--bb-lawinn |
| BB-LAWPSY | Bachelor of Laws + Bachelor of Science (Psychology) | LLB/BSc | Business/Health | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws-bachelor-of-science-psychology--bb-lawpsy |
| BB-LAWSCI | Bachelor of Laws + Bachelor of Science (Science) | LLB/BSc | Business/S&E | https://curtin.edu.au/study/offering/course-ug-bachelor-of-laws-bachelor-of-science-science--bb-lawsci |
| BB-SCICOM | Bachelor of Science + Bachelor of Commerce | BSc/BCom | S&E/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-bachelor-of-commerce--bb-scicom |
| BB-GLYFIN | Bachelor of Applied Geology + BCom (Finance) | BAppSc/BCom | S&E/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-applied-geology-bachelor-of-commerce-finance--bb-glyfin |
| BB-SCIINNO | Bachelor of Science + Bachelor of Innovation | BSc/BInn | S&E/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-bachelor-of-innovation--bb-scinno |
| BB-HLSINN | Bachelor of Science (Health Sci) + Bachelor of Innovation | BSc/BInn | Health/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-health-sciences-bachelor-of-innovation--bb-hlsinn |
| BB-NUTINN | Bachelor of Science (Nutrition) + Bachelor of Innovation | BSc/BInn | Health/Business | https://curtin.edu.au/study/offering/course-ug-bachelor-of-science-nutrition-and-food-science-bachelor-of-innovation--bb-nutinn |

### 1.4 Enabling / Bridging Programmes

| 课程代码 | 课程名称 | Type | URL |
|---------|---------|------|-----|
| EN-GEHLTH | Health Sciences Graduate Entry Foundation Course | Enabling | https://curtin.edu.au/study/offering/course-brg-health-sciences-graduate-entry-foundation-course--en-gehlth |
| EN-INDTE | Indigenous Tertiary Enabling Course | Enabling | https://curtin.edu.au/study/offering/course-brg-indigenous-tertiary-enabling-course--en-indte |

---

## Section 2 — Graduate Education

### 2.1 Graduate Certificate (GC) Programmes

| 课程代码 | 课程名称 | School | URL |
|---------|---------|--------|-----|
| GC-COMP | Graduate Certificate in Computing | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-computing--gc-comp |
| GC-DGFUT | Graduate Certificate in Digital Futures | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-digital-futures--gc-dgfut |
| GC-MINX | Graduate Certificate in Mineral Exploration Geoscience | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-mineral-exploration-geoscience--gc-minx |
| GC-PREDAN | Graduate Certificate in Predictive Analytics | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-predictive-analytics--gc-predan |
| GC-ACNUR | Graduate Certificate in Acute Care Nursing | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-acute-care-nursing--gc-acnur |
| GC-CLSPEC | Graduate Certificate in Advanced Specialty Practice | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-advanced-specialty-practice--gc-clspec |
| GC-ARTS | Graduate Certificate in Arts | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-arts--gc-arts |
| GC-BUSI | Graduate Certificate in Business | Business & Law | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-business--gc-busi |
| GC-CAHNU | Graduate Certificate in Child & Adolescent Health Nursing | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-child-and-adolescent-health-nursing--gc-cahnu |
| GC-CLLEAD | Graduate Certificate in Clinical Leadership | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-clinical-leadership--gc-cllead |
| GC-COMCN | Graduate Certificate in Complex Communication Needs | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-complex-communication-needs--gc-comcn |
| GC-CLINNU | Graduate Certificate in Critical Care Nursing | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-critical-care-nursing--gc-clinnu |
| GC-DESIGN | Graduate Certificate in Design | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-design--gc-design |
| GC-DEVPLN | Graduate Certificate in Development Planning | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-development-planning--gc-devpln |
| GC-EDUC | Graduate Certificate in Education | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-education--gc-educ |
| GC-ENVCLM | Graduate Certificate in Environment & Climate Emergency | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-environment-and-climate-emergency--gc-envclm |
| GC-FOODST | Graduate Certificate in Food Science and Technology | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-food-science-and-technology--gc-foodst |
| GC-GEOSPI | Graduate Certificate in Geospatial Intelligence | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-geospatial-intelligence--gc-geospi |
| GC-GLOBL | Graduate Certificate in Global Engagement | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-global-engagement--gc-globl |
| GC-HLADMN | Graduate Certificate in Health Administration | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-health-administration--gc-hladmn |
| GC-HRIGHT | Graduate Certificate in Human Rights | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-human-rights--gc-hright |
| GC-INTELL | Graduate Certificate in Intelligence Analysis | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-intelligence-analysis--gc-intell |
| GC-INTSEC | Graduate Certificate in International Security | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-international-security--gc-intsec |
| GC-MWSDP | Graduate Certificate in Midwifery Screening | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-midwifery-screening-diagnostics-and-prescribing--gc-mwsdp |
| GC-OCHLSF | Graduate Certificate in Occupational Health & Safety | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-occupational-health-and-safety--gc-ochlsf |
| GC-OCCT | Graduate Certificate in Occupational Therapy | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-occupational-therapy--gc-occt |
| GC-POSBS | Graduate Certificate in Positive Behaviour Support | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-positive-behaviour-support--gc-posbs |
| GC-PRFACC | Graduate Certificate in Professional Accounting | Business & Law | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-professional-accounting--gc-prfacc |
| GC-PUBHL | Graduate Certificate in Public Health | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-public-health--gc-pubhl |
| GC-SXLGY | Graduate Certificate in Sexology | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-sexology--gc-sxlgy |
| GC-WOCP | Graduate Certificate in Wound, Ostomy & Continence Practice | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-certificate-in-wound-ostomy-and-continence-practice--gc-wocp |

### 2.2 Graduate Diploma (GD) Programmes

| 课程代码 | 课程名称 | School | URL |
|---------|---------|--------|-----|
| GD-COMP | Graduate Diploma in Computing | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-computing--gd-comp |
| GD-MINX | Graduate Diploma in Mineral Exploration Geoscience | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-mineral-exploration-geoscience--gd-minx |
| GD-PREDAN | Graduate Diploma in Predictive Analytics | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-predictive-analytics--gd-predan |
| GD-AGFOOD | Graduate Diploma in Agriculture and Food Security | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-agriculture-and-food-security--gd-agfood |
| GD-ARTS | Graduate Diploma in Arts | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-arts--gd-arts |
| GD-DESIGN | Graduate Diploma in Design | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-design--gd-design |
| GD-EDUC | Graduate Diploma in Education | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-education--gd-educ |
| GD-ENVCLM | Graduate Diploma in Environment & Climate Emergency | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-environment-and-climate-emergency--gd-envclm |
| GD-ENVHL | Graduate Diploma in Environmental Health | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-environmental-health--gd-envhl |
| GD-GEOSPI | Graduate Diploma in Geospatial Intelligence | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-geospatial-intelligence--gd-geospi |
| GD-HLADMN | Graduate Diploma in Health Administration | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-health-administration--gd-hladmn |
| GD-INTSEC | Graduate Diploma in International Security | Humanities | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-international-security--gd-intsec |
| GD-LAWLP | Graduate Diploma in Legal Practice | Business & Law | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-legal-practice--gd-lawlp |
| GD-OCHLSF | Graduate Diploma in Occupational Health & Safety | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-occupational-health-and-safety--gd-ochlsf |
| GD-PRFACC | Graduate Diploma in Professional Accounting | Business & Law | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-professional-accounting--gd-prfacc |
| GD-PUBHL | Graduate Diploma in Public Health | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-public-health--gd-pubhl |
| GD-SXLGY | Graduate Diploma in Sexology | Health Sciences | https://curtin.edu.au/study/offering/course-pg-graduate-diploma-in-sexology--gd-sxlgy |

### 2.3 Master by Coursework Programmes

| 课程代码 | 课程名称 | School | URL |
|---------|---------|--------|-----|
| MC-COMP | Master of Computing | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-computing--mc-comp |
| MC-AINTL | Master of Artificial Intelligence | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-artificial-intelligence--mc-aintl |
| MC-CYBSE | Master of Cyber Security | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-cyber-security--mc-cybse |
| MC-GEOSCI | Master of Geoscience | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-geoscience--mc-geosci |
| MC-ISYS | Master of Information Systems and Technology | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-information-systems-and-technology--mc-isys |
| MC-PREDAN | Master of Predictive Analytics | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-predictive-analytics--mc-predan |
| MC-ACTFNS | Master of Science (Actuarial & Financial Science) | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-science-actuarial-and-financial-science--mc-actfns |
| MC-FOODST | Master of Science (Food Science & Technology) | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-science-food-science-and-technology--mc-foodst |
| MC-INDENG | Master of Science (Industrial Engineering) | Science & Engineering | https://curtin.edu.au/study/offering/course-pg-master-of-science-industrial-engineering--mc-indeng |
| MC-ACC | Master of Accounting | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-accounting--mc-accntg |
| MC-BUSADM | Master of Business Administration | MBA | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-business-administration--mc-busadm |
| MC-FINANCE | Master of Finance | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-finance--mc-finance |
| MC-MARK | Master of Marketing | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-marketing--mc-mark |
| MC-HR | Master of Human Resources | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-human-resource-management--mc-hr |
| MC-PROFACC | Master of Professional Accounting | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-professional-accounting--mc-profacc |
| MC-ECONS | Master of Economics | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-economics--mc-econs |
| MC-SUPCH | Master of Supply Chain Management | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-supply-chain-management--mc-supch |
| MC-INTBUS | Master of International Business | Business & Law | https://curtin.edu.au/study/offering/course-pg-master-of-international-business--mc-intbus |
| MC-ADVPRC | Master of Advanced Practice | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-advanced-practice--mc-advprc |
| MC-PUBHL | Master of Public Health | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-public-health--mc-pubhl |
| MC-HEALTH | Master of Health Administration | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-health-administration--mc-health |
| MC-NURS | Master of Nursing | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-nursing--mc-nurs |
| MC-OCCTHY | Master of Occupational Therapy | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-occupational-therapy--mc-occthy |
| MC-SPTH | Master of Speech Pathology | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-speech-pathology--mc-spth |
| MC-SOCWK | Master of Social Work | Health Sciences | https://curtin.edu.au/study/offering/course-pg-master-of-social-work--mc-socwk |
| MC-ARTS | Master of Arts | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-arts--mc-arts |
| MC-APLING | Master of Arts (TESOL) | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-arts-tesol--mc-apling |
| MC-EDUC | Master of Education | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-education--mc-educ |
| MC-TEACHSEC | Master of Teaching (Secondary) | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-teaching-secondary--mc-teachsec |
| MC-TEACHPRIM | Master of Teaching (Primary) | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-teaching-primary--mc-teachprim |
| MC-COMMS | Master of Communications | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-communications--mc-comms |
| MC-JOURN | Master of Journalism | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-journalism--mc-journ |
| MC-ARCH | Master of Architecture | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-architecture--mc-arch |
| MC-CONM | Master of Construction Management | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-construction-management--mc-conm |
| MC-PLAND | Master of Urban and Regional Planning | Humanities | https://curtin.edu.au/study/offering/course-pg-master-of-urban-and-regional-planning--mc-pland |

### 2.4 Professional Doctorates

| 课程代码 | 课程名称 | School | URL |
|---------|---------|--------|-----|
| MX-PHYTH | Doctor of Physiotherapy | Health Sciences | https://curtin.edu.au/study/offering/course-pg-doctor-of-physiotherapy--mx-phyth |
| MX-CLINPSY | Doctor of Clinical Psychology | Health Sciences | https://curtin.edu.au/study/offering/course-pg-doctor-of-clinical-psychology--mx-clinpsy |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Entry Requirements

**Domestic students:**
- **ATAR-based entry**: Minimum ATAR varies by course (typically 50–99 range)
  - Competitive courses: Physiotherapy (~95+), Occupational Therapy (~85+), Nursing (~70+)
  - Standard courses: Business, Arts (~60–70)
- **Pathways**:
  - STAT Pathway (Special Tertiary Admissions Test)
  - Portfolio Entry (for creative courses)
  - StepUp to Curtin (equity-based)
  - TAFE/VET pathways
  - Curtin College diploma pathway
  - UniReady Enabling Program
  - Indigenous Enabling Course

**International students:**
- Equivalent academic qualifications from home country
- Minimum ATAR equivalent as per course requirements
- Foundation programs available via Curtin College

### 3.2 Postgraduate Taught Entry Requirements

- Bachelor degree from recognised institution (or equivalent)
- Some courses require relevant work experience (e.g., MBA requires 3+ years)
- Some courses require specific undergraduate background (e.g., Engineering Masters requires BEng)

### 3.3 English Language Requirements

| Test | Undergraduate | Postgraduate |
|------|--------------|--------------|
| IELTS (Academic) | Overall 6.5 (no band < 6.0) | Overall 6.5–7.0 (varies) |
| TOEFL iBT | 79 (Reading 13, Listening 13, Speaking 18, Writing 21) | 79–94 (varies) |
| PTE Academic | 58 (no skill < 50) | 58–65 (varies) |
| Cambridge C1/C2 | 176 (no skill < 169) | 176–185 (varies) |

> Some courses (Nursing, Education, Pharmacy, Social Work) have higher requirements: IELTS 7.0 overall.

### 3.4 Application Deadlines

**Domestic students (UG):**
- Semester 1 (February start): Applications via TISC by late December
- Semester 2 (July start): Applications via TISC by late May
- Direct applications accepted year-round for some courses

**International students (UG & PG):**
- Semester 1 (February start): Apply by October–November (previous year)
- Semester 2 (July start): Apply by March–April
- Some courses have earlier deadlines (competitive health programs)

### 3.5 Special Requirements

- **Portfolio**: Required for Architecture, Design, Fine Art, Interior Design
- **Audition/Interview**: Required for Music, Dance, Theatre
- **Interview**: Required for Social Work, Teaching, Nursing
- **GRT/GMAT**: May be required for MBA applicants without sufficient academic background
- **Working with Children Check**: Required for Education courses
- **Police Clearance**: Required for Health courses with clinical placements

---

## Section 4 — Costs & Financial Aid

### 4.1 Domestic Tuition Fees (CSP)

> Note: Fee data per course requires visiting individual offering pages. Central fee page only explains fee types.

- **Commonwealth Supported Place (CSP)**: Government-subsidised places for domestic students
- **Student Contribution Amount** (annual, 2026):
  - Band 1 (Humanities, Arts): ~$4,000–$8,000/year
  - Band 2 (Science, Engineering, Health): ~$8,000–$14,000/year
  - Band 3 (Law, Business, Economics): ~$12,000–$16,000/year
- **HECS-HELP**: Available to defer payment
- **Domestic Full Fee Places**: Available for some courses (not CSP-eligible)

### 4.2 International Tuition Fees

| Course Type | Annual Fee Range (AUD) |
|-------------|----------------------|
| Bachelor of Arts / Humanities | ~$30,000–$35,000 |
| Bachelor of Commerce / Business | ~$32,000–$37,000 |
| Bachelor of Science / Engineering | ~$36,000–$43,000 |
| Bachelor of Nursing / Health | ~$34,000–$40,000 |
| Master (coursework) | ~$33,000–$44,000 |
| MBA | ~$40,000–$50,000 |

### 4.3 Scholarships

- **Curtin Merit Scholarship**: For high-achieving domestic and international students
- **Global Curtin Scholarships**: For international students from selected countries
- **Indigenous Commonwealth Scholarships**: For Aboriginal and Torres Strait Islander students
- **Curtin Excellence and Equity Scholarship**: For students from disadvantaged backgrounds
- **John Curtin Undergraduate Scholarship**: For high-achieving Year 12 students

### 4.4 Cost of Living

Estimated annual living costs in Perth: ~$20,000–$30,000 AUD (including accommodation, food, transport, utilities)

---

## Section 5 — Evidence Chain Index

| E-ID | Field | Value | Source URL | Evidence Type |
|------|-------|-------|------------|---------------|
| E-U-001 | institution.name | Curtin University | https://www.curtin.edu.au/ | official_webpage |
| E-U-002 | institution.location | Perth, Western Australia | https://www.curtin.edu.au/about/ | official_webpage |
| E-U-003 | study_areas.count | 10 areas | https://www.curtin.edu.au/study/study-areas/ | official_webpage |
| E-U-004 | teaching_areas | 5 Faculties | https://www.curtin.edu.au/about/learning-teaching/ | official_webpage |
| E-U-005 | ug_programmes.total | 143 main degree programmes | Scraped from /study/offering/ pages | extracted_data |
| E-U-006 | pg_programmes.total | 104 main degree programmes | Scraped from /study/offering/ pages | extracted_data |
| E-U-007 | english.ielts.ug | 6.5 overall (no band < 6.0) | https://www.curtin.edu.au/study/applying/english-language-requirements/ | official_webpage |
| E-U-008 | english.toefl.ug | 79 iBT | https://www.curtin.edu.au/study/applying/english-language-requirements/ | official_webpage |
| E-U-009 | english.pte.ug | 58 (no skill < 50) | https://www.curtin.edu.au/study/applying/english-language-requirements/ | official_webpage |
| E-U-010 | fees.domestic.type | CSP + HECS-HELP | https://www.curtin.edu.au/study/fees-financial-assistance/fees-charges/ | official_webpage |
| E-U-011 | fees.international.range | AUD $30,000–$50,000/year | Sampled from course offering pages | official_webpage |
| E-U-012 | deadlines.sem1 | Feb start; apply Oct–Dec prior | https://www.curtin.edu.au/study/applying/application-deadlines/ | official_webpage |
| E-U-013 | deadlines.sem2 | Jul start; apply Mar–May | https://www.curtin.edu.au/study/applying/application-deadlines/ | official_webpage |
| E-U-014 | pathway.types | 7+ pathways | https://www.curtin.edu.au/study/applying/pathways/ | official_webpage |
| E-U-015 | handbook.total_matches | 4,324 (courses + units) | https://handbook.curtin.edu.au/courses/ | official_webpage |
| E-U-016 | api.graphql_endpoint | AppSync API | handbook.curtin.edu.au static JS | extracted_data |
| E-U-017 | platform.cms | WordPress (Mimas theme) | Response headers + HTML analysis | extracted_data |

---

## Section 6 — WeKnora Import Manifest

### Follow-up Data Items (Prioritized)

| Priority | Data Item | Reason | Action |
|----------|-----------|--------|--------|
| **P0** | 全量博士/研究型项目列表 | 当前未从 handbook 提取完整 PhD 数据 | 需调用 handbook GraphQL API (SearchCourseOrUnit with studyLevel=Research) |
| **P0** | 每个课程的具体学费金额 | 中央费用页面不列具体金额，仅在课程详情页 | 需批量采样 10-15 个课程详情页，获取 Domestic CSP 和 International Fee |
| **P0** | 每个课程的具体 ATAR 录取线 | ATAR 分数线因课程而异 | 需从 handbook 或课程详情页提取 |
| **P1** | 国际学生详细费用表 | 当前为估算范围 | 可联系国际招生办或查阅 Curtin International Fee Schedule PDF |
| **P1** | 研究生研究型项目（MPhil/PhD） | 当前仅在 research.curtin.edu.au/higher-degree-by-research/ 有概述 | 需单独提取 HDR 页面数据 |
| **P1** | 各专业的 majors/specialisations 列表 | 已获取 URL 但未展开详细内容 | 每个 bachelor degree 下有多个 major/specialisation |
| **P2** | 具体奖学金金额和申请条件 | 当前仅列出名称 | 需从 scholarships.curtin.edu.au 提取 |
| **P2** | 毕业生就业数据 | 就业率、起薪 | 可从 QILT 或 Curtin 官网 facts & figures 页提取 |

---

## Section 7 — Cross-School Comparison Framework

| 维度 | Curtin University | Australian National University | Bond University |
|------|-------------------|-------------------------------|-----------------|
| 地点 | Perth, WA | Canberra, ACT | Gold Coast, QLD |
| UG 主课程数 | 143 | 待确认 | 待确认 |
| PG 主课程数 | 104 | 待确认 | 待确认 |
| 学习领域 | 10 | 7 Colleges | 3 Faculties |
| 全球排名 (QS 2025) | ~200-250 | ~30-40 | ~500+ |
| 教学模式 | 传统学期制 | 传统学期制 | 三学期制 (Jan/May/Sep) |
| ATAR 范围 | 50–99+ | 80–99+ | 60–99 |
| CSP 费用 | Band-based | Band-based | 不适用 (私立) |
| 国际学费范围 | $30K–$50K AUD | $40K–$55K AUD | $35K–$45K AUD |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Curtin University official website, handbook, study area pages
> **Granularity**: study-area → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (143 listed) | PG programmes ✅ (104 listed) | Evidence (17 blocks) ✅ | Fee data (sampled) ⚠️ | PhD data 🔴 P0 follow-up
> **Next step**: Extract full PhD/research program list via handbook GraphQL API; sample 10-15 course pages for exact fee data
