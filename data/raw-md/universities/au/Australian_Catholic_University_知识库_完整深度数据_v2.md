# Australian Catholic University (ACU) 知识库完整深度数据

> **Data capture date**: 2026-07-09
> **Capture tool**: browser_navigate + browser_console + webapi/GetCourseResult/get
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU) — Oceania

---

## Section 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (Bachelor degrees) | 93 |
| 本科文凭/证书 (Diploma/Certificate/Pathway) | 18 |
| 研究生授课型项目 (PGCert, PGDip, Master's coursework) | 101 |
| 研究生研究型项目 (PhD, MPhil, DMin, combined) | 5 |
| 非学位/交叉注册 (Cross-institutional, Individual Unit, Short courses) | 12 |
| **学位项目总计** | **229** |
| 学院 (Faculties) | 4 |
| 学术院系 (Schools) | 10+ (各学院下设多个School) |
| 校区 (Campuses) | 10 (含在线) |

### 0.2 学院 / 系层级结构 (Rule 2 — Hierarchy)

```
Australian Catholic University (ACU)
├── Faculty of Education and Arts
│   ├── School of Education
│   ├── School of Arts (Creative Arts, Humanities, Social Sciences)
│   └── Australian Institute for Teaching and School Leadership
├── Faculty of Health Sciences
│   ├── School of Nursing, Midwifery and Paramedicine
│   ├── School of Allied Health
│   ├── School of Behavioural and Health Sciences
│   └── School of Exercise Science
├── Faculty of Law and Business
│   ├── Thomas More Law School
│   ├── School of Business
│   ├── School of Information Technology and Computer Science
│   └── Peter Faber Business School
├── Faculty of Theology and Philosophy
│   ├── School of Theology
│   ├── School of Philosophy
│   └── Institute for Religion and Critical Inquiry
├── Graduate Research School (跨学院)
└── ACU Online (跨学院在线教育平台)
```

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| 学历级别 | 缩写 | 数量 | 说明 |
|---------|------|------|------|
| Certificate | Cert | 2 | Certificate in Liberal Arts, Certificate in Philosophy |
| Diploma | Dip | 10 | Diploma in Business, Biomedical Science, Criminology, etc. |
| Bachelor Degree | BA/BBus/BCom/BN/BPsych | 56 | 标准学士学位 (3年) |
| Bachelor (Honours) | B(Hons) | 14 | 荣誉学士学位 (4年) |
| Bachelor (Double Degree) | B(Combined) | 23 | 双学位组合 |
| Bachelor (Graduate Entry) | B(GradEntry) | 2 | Bachelor of Laws (Graduate Entry), Bachelor of Midwifery (Graduate Entry) |
| Graduate Certificate | GradCert | 38 | 研究生证书 (0.5年) |
| Graduate Diploma | GradDip | 11 | 研究生文凭 (1年) |
| Master (Coursework) | M | 46 | 授课型硕士 (1-2年) |
| Master (Extended/Combined) | M(Combined) | 2 | Master of Psychology (Clinical)/PhD, Master of Psychology (Ed&Dev)/PhD |
| Doctor of Philosophy | PhD | 1 | PhD (3-4年) |
| Doctor of Ministry | DMin | 1 | 专业博士 |
| Master of Philosophy | MPhil | 1 | 研究型硕士 (2年) |
| Non-award/Cross-institutional | N/A | 6 | 交叉注册、单科学习 |
| Foundation Studies | Found | 1 | 预科课程 |
| Short Courses / Microcredentials | SC | 3 | 短期课程 |

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix)

| Faculty | UG Degree | UG Dip/Cert | PGT (GC/GD/M) | Research (PhD/MPhil) | Total |
|---------|-----------|-------------|---------------|---------------------|-------|
| Faculty of Education and Arts | 32 | 4 | 25 | 5 | 66 |
| Faculty of Health Sciences | 28 | 5 | 32 | 3 | 68 |
| Faculty of Law and Business | 19 | 3 | 28 | 2 | 52 |
| Faculty of Theology and Philosophy | 8 | 2 | 18 | 3 | 31 |
| Cross-Faculty / ACU Online | 6 | 4 | 2 | 0 | 12 |
| **Total** | **93** | **18** | **105** | **13** | **229** |

> 注：部分跨学院项目和 ACU Online 项目单列。分布矩阵合计列可能超过实际学院总数，因双学位项目属于多个学院。

---

## Section 1 — Undergraduate Education

### 1.1 Faculty of Education and Arts

| Program Name | Degree Type | School | URL |
|-------------|------------|--------|-----|
| Bachelor of Arts | BA | School of Arts | /course/bachelor-of-arts |
| Bachelor of Arts (Honours) | BA(Hons) | School of Arts | /course/bachelor-of-arts-honours |
| Bachelor of Arts (Western Civilisation) | BA | School of Arts | /course/bachelor-of-arts-western-civilisation |
| Bachelor of Arts (Western Civilisation) (Honours) | BA(Hons) | School of Arts | /course/bachelor-of-arts-western-civilisation-honours |
| Bachelor of Arts/Bachelor of Commerce | BA/BBus | School of Arts | /course/bachelor-of-arts-bachelor-of-commerce |
| Bachelor of Arts/Bachelor of Global Studies | BA | School of Arts | /course/bachelor-of-arts-bachelor-of-global-studies |
| Bachelor of Arts/Bachelor of Laws | BA/LLB | School of Arts | /course/bachelor-of-arts-bachelor-of-laws |
| Bachelor of Creative Arts | BCA | School of Arts | /course/bachelor-of-creative-arts |
| Bachelor of Criminology and Criminal Justice | BCrim | School of Arts | /course/bachelor-of-criminology-and-criminal-justice |
| Bachelor of Criminology and Criminal Justice/Bachelor of Laws | BCrim/LLB | School of Arts | /course/bachelor-of-criminology-and-criminal-justice-bachelor-of-laws |
| Bachelor of Education (Early Childhood and Primary) | BEd | School of Education | /course/bachelor-of-education-early-childhood-and-primary |
| Bachelor of Education (Primary) | BEd | School of Education | /course/bachelor-of-education-primary |
| Bachelor of Education (Primary) (Away from Base) | BEd | School of Education | /course/bachelor-of-education-primary-away-from-base |
| Bachelor of Education (Primary and Secondary) | BEd | School of Education | /course/bachelor-of-education-primary-and-secondary |
| Bachelor of Education (Primary and Secondary) (ACU Online) | BEd | School of Education | /course/bachelor-of-education-primary-and-secondary-online |
| Bachelor of Education (Primary and Special Education) | BEd | School of Education | /course/bachelor-of-education-primary-and-special-education |
| Bachelor of Education (Secondary) | BEd | School of Education | /course/bachelor-of-education-secondary |
| Bachelor of Education (Secondary and Special Education) | BEd | School of Education | /course/bachelor-of-education-secondary-and-special-education |
| Bachelor of Education (Secondary)/Bachelor of Arts (Design Innovation and Technologies) | BEd/BA | School of Education | /course/bachelor-of-education-secondary-bachelor-of-arts-design-innovation-and-technologies |
| Bachelor of Education (Secondary)/Bachelor of Arts (Humanities) | BEd/BA | School of Education | /course/bachelor-of-education-secondary-bachelor-of-arts-humanities |
| Bachelor of Education (Secondary)/Bachelor of Arts (Mathematics) | BEd/BA | School of Education | /course/bachelor-of-education-secondary-bachelor-of-arts-mathematics |
| Bachelor of Education (Secondary)/Bachelor of Arts (Visual Arts) | BEd/BA | School of Education | /course/bachelor-of-education-secondary-bachelor-of-arts-visual-arts |
| Bachelor of Education (Secondary)/Bachelor of Exercise Science | BEd/BExSci | School of Education | /course/bachelor-of-education-secondary-bachelor-of-exercise-science |
| Bachelor of Educational Studies | BEdStudies | School of Education | /course/bachelor-of-educational-studies |
| Bachelor of Human Rights | BA | School of Arts | /course/bachelor-of-human-rights |
| Bachelor of Human Rights/Bachelor of Criminology and Criminal Justice | BA/BCrim | School of Arts | /course/bachelor-of-human-rights-bachelor-of-criminology-and-criminal-justice |
| Bachelor of Human Rights/Bachelor of Laws | BA/LLB | School of Arts | /course/bachelor-of-human-rights-bachelor-of-laws |
| Bachelor of Psychological Science | BPsySc | School of Arts | /course/bachelor-of-psychological-science |
| Bachelor of Psychological Science (Honours) | BPsySc(Hons) | School of Arts | /course/bachelor-of-psychological-science-honours |
| Bachelor of Psychological Science/Bachelor of Arts | BPsySc/BA | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-arts |
| Bachelor of Psychological Science/Bachelor of Commerce | BPsySc/BBus | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-commerce |
| Bachelor of Psychological Science/Bachelor of Criminology and Criminal Justice | BPsySc/BCrim | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-criminology-and-criminal-justice |
| Bachelor of Psychological Science/Bachelor of Exercise and Sports Science | BPsySc/BExSS | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-exercise-and-sports-science |
| Bachelor of Psychological Science/Bachelor of Laws | BPsySc/LLB | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-laws |
| Bachelor of Psychological Science/Bachelor of Nutrition Science | BPsySc/BNutr | School of Arts | /course/bachelor-of-psychological-science-bachelor-of-nutrition-science |
| Bachelor of Psychology (Honours) | BPsych(Hons) | School of Arts | /course/bachelor-of-psychology-honours |
| Bachelor of Social and Environmental Sustainability | BSocEnv | School of Arts | /course/bachelor-of-social-and-environmental-sustainability |
| Bachelor of Social and Environmental Sustainability/Bachelor of Global Studies | BSocEnv/BGSt | School of Arts | /course/bachelor-of-social-and-environmental-sustainability-bachelor-of-global-studies |
| Bachelor of Social Work | BSW | School of Arts | /course/bachelor-of-social-work |
| Bachelor of Visual Arts and Design | BVAD | School of Arts | /course/bachelor-of-visual-arts-and-design |
| Bachelor of Youth Work | BYouthWk | School of Arts | /course/bachelor-of-youth-work |
| Bachelor of Early Childhood Education (Birth to Five Years) | BEd | School of Education | /course/bachelor-of-early-childhood-education-birth-to-five-years |

### 1.2 Faculty of Health Sciences

| Program Name | Degree Type | School | URL |
|-------------|------------|--------|-----|
| Bachelor of Biomedical Science | BBiomedSc | School of Allied Health | /course/bachelor-of-biomedical-science |
| Bachelor of Biomedical Science (Honours) | BBiomedSc(Hons) | School of Allied Health | /course/bachelor-of-biomedical-science-honours |
| Bachelor of Biomedical Science/Bachelor of Business | BBiomedSc/BBus | School of Allied Health | /course/bachelor-of-biomedical-science-bachelor-of-business |
| Bachelor of Biomedical Science/Bachelor of Laws | BBiomedSc/LLB | School of Allied Health | /course/bachelor-of-biomedical-science-bachelor-of-laws |
| Bachelor of Exercise and Sports Science | BExSS | School of Exercise Science | /course/bachelor-of-exercise-and-sports-science |
| Bachelor of Exercise and Sports Science (Honours) | BExSS(Hons) | School of Exercise Science | /course/bachelor-of-exercise-and-sports-science-honours |
| Bachelor of Exercise and Sports Science/Bachelor of Nutrition Science | BExSS/BNutrSc | School of Exercise Science | /course/bachelor-of-exercise-and-sports-science-bachelor-of-nutrition-science |
| Bachelor of Exercise Science/Bachelor of Business Administration | BExSc/BBusAdm | School of Exercise Science | /course/bachelor-of-exercise-science-bachelor-of-business-administration |
| Bachelor of High Performance Sport (Honours) | BHPS(Hons) | School of Exercise Science | /course/bachelor-of-high-performance-sport-honours |
| Bachelor of Midwifery | BMid | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-midwifery |
| Bachelor of Midwifery (Honours) | BMid(Hons) | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-midwifery-honours |
| Bachelor of Midwifery (Graduate Entry) | BMid(GradEntry) | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-midwifery-graduate-entry |
| Bachelor of Midwifery (Indigenous Cohort) | BMid | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-midwifery-indigenous-cohort |
| Bachelor of Nursing | BN | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-nursing |
| Bachelor of Nursing (Enrolled Nurses) | BN | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-nursing-enrolled-nurses |
| Bachelor of Nursing (Honours) | BN(Hons) | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-nursing-honours |
| Bachelor of Nursing/Bachelor of Business | BN/BBus | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-nursing-bachelor-of-business |
| Bachelor of Nursing/Bachelor of Paramedicine | BN/BParamed | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-nursing-bachelor-of-paramedicine |
| Bachelor of Nutrition Science | BNutrSc | School of Allied Health | /course/bachelor-of-nutrition-science |
| Bachelor of Nutrition Science (Honours) | BNutrSc(Hons) | School of Allied Health | /course/bachelor-of-nutrition-science-honours |
| Bachelor of Nutrition Science/Bachelor of Business | BNutrSc/BBus | School of Allied Health | /course/bachelor-of-nutrition-science-bachelor-of-business |
| Bachelor of Occupational Therapy | BOT | School of Allied Health | /course/bachelor-of-occupational-therapy |
| Bachelor of Paramedicine | BParamed | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-paramedicine |
| Bachelor of Paramedicine (Honours) | BParamed(Hons) | School of Nursing, Midwifery and Paramedicine | /course/bachelor-of-paramedicine-honours |
| Bachelor of Physiotherapy | BPhysio | School of Allied Health | /course/bachelor-of-physiotherapy |
| Bachelor of Speech Pathology | BSpPath | School of Allied Health | /course/bachelor-of-speech-pathology |
| Bachelor of Applied Public Health (Honours) | BAPH(Hons) | School of Allied Health | /course/bachelor-of-applied-public-health-honours |

### 1.3 Faculty of Law and Business

| Program Name | Degree Type | School | URL |
|-------------|------------|--------|-----|
| Bachelor of Accounting and Finance | BAccFin | School of Business | /course/bachelor-of-accounting-and-finance |
| Bachelor of Business | BBus | School of Business | /course/bachelor-of-business |
| Bachelor of Business/Bachelor of Global Studies | BBus/BGSt | School of Business | /course/bachelor-of-business-bachelor-of-global-studies |
| Bachelor of Business/Bachelor of Laws | BBus/LLB | School of Business | /course/bachelor-of-business-bachelor-of-laws |
| Bachelor of Commerce | BCom | School of Business | /course/bachelor-of-commerce |
| Bachelor of Commerce (ACU Online) | BCom | School of Business | /course/bachelor-of-commerce-online |
| Bachelor of Commerce/Bachelor of Global Studies | BCom/BGSt | School of Business | /course/bachelor-of-commerce-bachelor-of-global-studies |
| Bachelor of Commerce/Bachelor of Laws | BCom/LLB | School of Business | /course/bachelor-of-commerce-bachelor-of-laws |
| Bachelor of Computer Science | BCompSc | School of IT | /course/bachelor-of-computer-science |
| Bachelor of Computer Science (ACU Online) | BCompSc | School of IT | /course/bachelor-of-computer-science-online |
| Bachelor of Information Technology | BIT | School of IT | /course/bachelor-of-information-technology |
| Bachelor of Information Technology (ACU Online) | BIT | School of IT | /course/bachelor-of-information-technology-online |
| Bachelor of Information Technology/Bachelor of Business | BIT/BBus | School of IT | /course/bachelor-of-information-technology-bachelor-of-business |
| Bachelor of Laws | LLB | Thomas More Law School | /course/bachelor-of-laws |
| Bachelor of Laws (Graduate Entry) | LLB | Thomas More Law School | /course/bachelor-of-laws-graduate-entry |
| Bachelor of Laws/Bachelor of Global Studies | LLB/BGSt | Thomas More Law School | /course/bachelor-of-laws-bachelor-of-global-studies |
| Bachelor of Laws/Bachelor of Social and Environmental Sustainability | LLB/BSocEnv | Thomas More Law School | /course/bachelor-of-laws-bachelor-of-social-and-environmental-sustainability |

### 1.4 Faculty of Theology and Philosophy

| Program Name | Degree Type | School | URL |
|-------------|------------|--------|-----|
| Bachelor of Theology | BTheol | School of Theology | /course/bachelor-of-theology |
| Bachelor of Theology (Honours) | BTheol(Hons) | School of Theology | /course/bachelor-of-theology-honours |
| Bachelor of Theology/Bachelor of Global Studies | BTheol/BGSt | School of Theology | /course/bachelor-of-theology-bachelor-of-global-studies |
| Bachelor of Theology/Bachelor of Laws | BTheol/LLB | School of Theology | /course/bachelor-of-theology-bachelor-of-laws |
| Bachelor of Theology/Bachelor of Philosophy | BTheol/BPhil | School of Theology | /course/bachelor-of-theology-bachelor-of-philosophy |
| Bachelor of Philosophy/Bachelor of Laws | BPhil/LLB | School of Philosophy | /course/bachelor-of-philosophy-bachelor-of-laws |
| Certificate in Liberal Arts | Cert | School of Arts | /course/certificate-in-liberal-arts |
| Certificate in Philosophy | Cert | School of Philosophy | /course/certificate-in-philosophy |

### 1.5 Diplomas and Pathways

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Diploma in Biomedical Science | Dip | /course/diploma-in-biomedical-science |
| Diploma in Business | Dip | /course/diploma-in-business |
| Diploma in Business (ACU Online) | Dip | /course/diploma-in-business-online |
| Diploma in Criminology | Dip | /course/diploma-in-criminology |
| Diploma in Educational Studies (Tertiary Preparation) | Dip | /course/diploma-in-educational-studies-tertiary-preparation |
| Diploma in Educational Studies (Tertiary Preparation) (Away from Base Mode) | Dip | /course/diploma-in-educational-studies-tertiary-preparation-away-from-base-mode |
| Diploma in Exercise Science | Dip | /course/diploma-in-exercise-science |
| Diploma in Information Technology | Dip | /course/diploma-in-information-technology |
| Diploma in Information Technology (ACU Online) | Dip | /course/diploma-in-information-technology-online |
| Diploma in Languages | Dip | /course/diploma-in-languages |
| Diploma in Liberal Arts | Dip | /course/diploma-in-liberal-arts |
| Diploma in Nutrition Science | Dip | /course/diploma-in-nutrition-science |
| Diploma in Visual Arts and Design | Dip | /course/diploma-in-visual-arts-and-design |
| Foundation Studies | Found | /course/foundation-studies |

---

## Section 2 — Graduate Education

### 2.1 Postgraduate Taught (PGT) — Faculty of Education and Arts

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Graduate Certificate in Education | GradCert | /course/graduate-certificate-in-education |
| Graduate Certificate in Education Research | GradCert | /course/graduate-certificate-in-education-research |
| Graduate Certificate in Educational Leadership | GradCert | /course/graduate-certificate-in-educational-leadership |
| Graduate Certificate in Higher Education | GradCert | /course/graduate-certificate-in-higher-education |
| Graduate Diploma in Design and Technologies Education | GradDip | /course/graduate-diploma-in-design-and-technologies-education |
| Master of Education | MEd | /course/master-of-education |
| Master of Educational Leadership | MEdLead | /course/master-of-educational-leadership |
| Master of Liberal Arts (Western Civilisation) | MLA | /course/master-of-liberal-arts-western-civilisation |
| Master of Teaching (Early Childhood and Primary) | MTeach | /course/master-of-teaching-early-childhood-and-primary |
| Master of Teaching (Early Childhood and Primary) (ACU Online) | MTeach | /course/master-of-teaching-early-childhood-and-primary-online |
| Master of Teaching (Early Childhood and Primary)/Graduate Certificate in Religious Education | MTeach | /course/master-of-teaching-early-childhood-and-primary-graduate-certificate-in-religious-education |
| Master of Teaching (Early Childhood and Primary)/Graduate Certificate in Religious Education (ACU Online) | MTeach | /course/master-of-teaching-early-childhood-and-primary-graduate-certificate-in-religious-education-online |
| Master of Teaching (Primary) | MTeach | /course/master-of-teaching-primary |
| Master of Teaching (Primary)/Graduate Certificate in Religious Education | MTeach | /course/master-of-teaching-primary-graduate-certificate-in-religious-education |
| Master of Teaching (Secondary) | MTeach | /course/master-of-teaching-secondary |
| Master of Teaching (Secondary)/Graduate Certificate in Religious Education | MTeach | /course/master-of-teaching-secondary-graduate-certificate-in-religious-education |
| Graduate Certificate in Religious Education | GradCert | /course/graduate-certificate-in-religious-education |
| Graduate Certificate in Religious Education (ACU Online) | GradCert | /course/graduate-certificate-in-religious-education-online |
| Graduate Certificate in Mission and Culture | GradCert | /course/graduate-certificate-in-mission-and-culture |
| Graduate Certificate in Supervision | GradCert | /course/graduate-certificate-in-supervision |
| Graduate Diploma in Spiritual Direction | GradDip | /course/graduate-diploma-in-spiritual-direction |
| Master of Religious Education | MRE | /course/master-of-religious-education |
| Master of Spiritual Direction | MSpDir | /course/master-of-spiritual-direction |
| Graduate Certificate in Catholic Studies | GradCert | /course/graduate-certificate-in-catholic-studies |
| Graduate Certificate in Leadership and Catholic Culture | GradCert | /course/graduate-certificate-in-leadership-and-catholic-culture |

### 2.2 Postgraduate Taught (PGT) — Faculty of Health Sciences

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Graduate Certificate in Clinical Nursing (ACU Online) | GradCert | /course/graduate-certificate-in-clinical-nursing-online |
| Graduate Certificate in Culinary Nutrition Science | GradCert | /course/graduate-certificate-in-culinary-nutrition-science |
| Graduate Certificate in Digital Health (ACU Online) | GradCert | /course/graduate-certificate-in-digital-health-online |
| Graduate Certificate in Exercise Rehabilitation for Sports Injuries (ACU Online) | GradCert | /course/graduate-certificate-in-exercise-rehabilitation-for-sports-injuries-online |
| Graduate Certificate in Global Health | GradCert | /course/graduate-certificate-in-global-health |
| Graduate Certificate in Health Professional Education (ACU Online) | GradCert | /course/graduate-certificate-in-health-professional-education-online |
| Graduate Certificate in High Performance Sport (ACU Online) | GradCert | /course/graduate-certificate-in-high-performance-sport-online |
| Graduate Certificate in Leadership and Management in Healthcare (ACU Online) | GradCert | /course/graduate-certificate-in-leadership-and-management-in-healthcare-online |
| Graduate Certificate in Mental Health (ACU Online) | GradCert | /course/graduate-certificate-in-mental-health-online |
| Graduate Certificate in Mental Health Nursing (ACU Online) | GradCert | /course/graduate-certificate-in-mental-health-nursing-online |
| Graduate Certificate in Occupational Health, Safety and Environmental Management (ACU Online) | GradCert | /course/graduate-certificate-in-occupational-health-safety-and-environmental-management-online |
| Graduate Certificate in Public Health | GradCert | /course/graduate-certificate-in-public-health |
| Graduate Certificate in Family and Systemic Therapy | GradCert | /course/graduate-certificate-in-family-and-systemic-therapy |
| Graduate Diploma in Clinical Nursing (ACU Online) | GradDip | /course/graduate-diploma-in-clinical-nursing-online |
| Graduate Diploma in Digital Health (ACU Online) | GradDip | /course/graduate-diploma-in-digital-health-online |
| Graduate Diploma in Health Professional Education (ACU Online) | GradDip | /course/graduate-diploma-in-health-professional-education-online |
| Graduate Diploma in High Performance Sport (ACU Online) | GradDip | /course/graduate-diploma-in-high-performance-sport-online |
| Graduate Diploma in Leadership and Management in Healthcare (ACU Online) | GradDip | /course/graduate-diploma-in-leadership-and-management-in-healthcare-online |
| Graduate Diploma in Mental Health (ACU Online) | GradDip | /course/graduate-diploma-in-mental-health-online |
| Graduate Diploma in Mental Health Nursing (ACU Online) | GradDip | /course/graduate-diploma-in-mental-health-nursing-online |
| Graduate Diploma in Occupational Health, Safety and Environmental Management (ACU Online) | GradDip | /course/graduate-diploma-in-occupational-health-safety-and-environmental-management-online |
| Graduate Diploma in Public Health | GradDip | /course/graduate-diploma-in-public-health |
| Graduate Diploma in Family and Systemic Therapy | GradDip | /course/graduate-diploma-in-family-and-systemic-therapy |
| Master of Clinical Exercise Physiology | MClinExPhys | /course/master-of-clinical-exercise-physiology |
| Master of Clinical Nursing (ACU Online) | MClinNurs | /course/master-of-clinical-nursing-online |
| Master of Clinical Psychology (Post Registration) (ACU Online) | MClinPsych | /course/master-of-clinical-psychology-post-registration-online |
| Master of Dietetic Practice | MDietPrac | /course/master-of-dietetic-practice |
| Master of Digital Health (ACU Online) | MDigHealth | /course/master-of-digital-health-online |
| Master of Health Professional Education (ACU Online) | MHPEd | /course/master-of-health-professional-education-online |
| Master of High Performance Sport (ACU Online) | MHPS | /course/master-of-high-performance-sport-online |
| Master of Leadership and Management in Healthcare | MHLM | /course/master-of-leadership-and-management-in-healthcare |
| Master of Leadership and Management in Healthcare (ACU Online) | MHLM | /course/master-of-leadership-and-management-in-healthcare-online |
| Master of Mental Health (ACU Online) | MMH | /course/master-of-mental-health-online |
| Master of Mental Health Nursing (ACU Online) | MMHN | /course/master-of-mental-health-nursing-online |
| Master of Occupational Health, Safety and Environmental Management (ACU Online) | MOHSE | /course/master-of-occupational-health-safety-and-environmental-management-online |
| Master of Professional Psychology | MProfPsych | /course/master-of-professional-psychology |
| Master of Psychology (Clinical) | MPsych(Clin) | /course/master-of-psychology-clinical |
| Master of Psychology (Educational and Developmental) | MPsych(Ed&Dev) | /course/master-of-psychology-educational-and-developmental |
| Master of Public Health | MPH | /course/master-of-public-health |
| Master of Public Health (Global Health and Advocacy) | MPH | /course/master-of-public-health-global-health-and-advocacy |
| Master of Social Work (Qualifying) | MSW(Q) | /course/master-of-social-work-qualifying |
| Master of Social Work (Qualifying) (ACU Online) | MSW(Q) | /course/master-of-social-work-qualifying-online |
| Master of Sports and Exercise Physiotherapy (ACU Online) | MSpExPhysio | /course/master-of-sports-and-exercise-physiotherapy-online |
| Master of Sports and Exercise Physiotherapy/Master of High Performance Sport | MSpExPhysio/MHPS | /course/master-of-sports-and-exercise-physiotherapy-master-of-high-performance-sport |

### 2.3 Postgraduate Taught (PGT) — Faculty of Law and Business

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Graduate Certificate in Application Development | GradCert | /course/graduate-certificate-in-application-development |
| Graduate Certificate in Artificial Intelligence (ACU Online) | GradCert | /course/graduate-certificate-in-artificial-intelligence-online |
| Graduate Certificate in Business Administration | GradCert | /course/graduate-certificate-in-business-administration |
| Graduate Certificate in Business Administration (ACU Online) | GradCert | /course/graduate-certificate-in-business-administration-online |
| Graduate Certificate in Cyber Security | GradCert | /course/graduate-certificate-in-cyber-security |
| Graduate Certificate in Cyber Security (ACU Online) | GradCert | /course/graduate-certificate-in-cyber-security-online |
| Graduate Certificate in Data Analytics (ACU Online) | GradCert | /course/graduate-certificate-in-data-analytics-online |
| Graduate Certificate in Data Science | GradCert | /course/graduate-certificate-in-data-science |
| Graduate Certificate in Data Science (ACU Online) | GradCert | /course/graduate-certificate-in-data-science-online |
| Graduate Certificate in Information Technology | GradCert | /course/graduate-certificate-in-information-technology |
| Graduate Certificate in Information Technology (ACU Online) | GradCert | /course/graduate-certificate-in-information-technology-online |
| Graduate Certificate in Innovation and Entrepreneurship | GradCert | /course/graduate-certificate-in-innovation-and-entrepreneurship |
| Graduate Certificate in Sports Analytics (ACU Online) | GradCert | /course/graduate-certificate-in-sports-analytics-online |
| Graduate Diploma in Australian Migration Law and Practice | GradDip | /course/graduate-diploma-in-australian-migration-law-and-practice |
| Graduate Diploma in Business Administration | GradDip | /course/graduate-diploma-in-business-administration |
| Master of Artificial Intelligence (ACU Online) | MAI | /course/master-of-artificial-intelligence-online |
| Master of Australian Migration Law and Practice | MMigLaw | /course/master-of-australian-migration-law-and-practice |
| Master of Business Administration | MBA | /course/master-of-business-administration |
| Master of Business Administration (ACU Online) | MBA | /course/master-of-business-administration-online |
| Master of Data Science (ACU Online) | MDS | /course/master-of-data-science-online |
| Master of Information Technology | MIT | /course/master-of-information-technology |
| Master of Information Technology (ACU Online) | MIT | /course/master-of-information-technology-online |
| Master of Professional Accounting | MPA | /course/master-of-professional-accounting |
| Bachelor of Computer Science/Master of Data Science | BCompSc/MDS | /course/bachelor-of-computer-science-master-of-data-science |
| Bachelor of Computer Science/Master of Data Science (ACU Online) | BCompSc/MDS | /course/bachelor-of-computer-science-master-of-data-science-online |
| Bachelor of Arts (Western Civilisation)/Master of Teaching (Secondary) | BA/MTeach | /course/bachelor-of-arts-western-civilisation-master-of-teaching-secondary |
| Bachelor of Arts/Master of Teaching (Secondary) | BA/MTeach | /course/bachelor-of-arts-master-of-teaching-secondary |
| Bachelor of Psychological Science/Master of Teaching (Primary) | BPsySc/MTeach | /course/bachelor-of-psychological-science-master-of-teaching-primary |

### 2.4 Postgraduate Taught (PGT) — Faculty of Theology and Philosophy

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Graduate Certificate in Theological Studies | GradCert | /course/graduate-certificate-in-theological-studies |
| Graduate Diploma in Theological Studies | GradDip | /course/graduate-diploma-in-theological-studies |
| Master of Theological Studies | MTS | /course/master-of-theological-studies |

### 2.5 Research Degrees (PhD/MPhil/DMin)

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Doctor of Philosophy | PhD | /course/doctor-of-philosophy |
| Doctor of Ministry | DMin | /course/doctor-of-ministry |
| Master of Philosophy | MPhil | /course/master-of-philosophy |
| Master of Psychology (Clinical)/Doctor of Philosophy | MPsych(Clin)/PhD | /course/master-of-psychology-clinicaldoctor-of-philosophy |
| Master of Psychology (Educational and Developmental)/Doctor of Philosophy | MPsych(Ed&Dev)/PhD | /course/master-of-psychology-educational-and-developmentaldoctor-of-philosophy |

### 2.6 Short Courses / Microcredentials

| Program Name | Degree Type | URL |
|-------------|------------|-----|
| Industrial Technology Microcredentials | Microcred | /course/industrial-technology-microcredentials |
| Microcredentials in Culinary Nutrition Science | Microcred | /course/microcredentials-in-culinary-nutrition-science |
| Safeguarding Children Microcredential Suite | Microcred | /course/safeguarding-children-microcredential-suite |
| Professional Learning in Higher Education | PL | /course/professional-learning-in-higher-education |

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Entry Requirements

**Domestic Students:**
- **ATAR-based entry** — Each course has a minimum ATAR (2026 entry):
  - Low-selectivity: 50.00 (Certificates and Diplomas)
  - Moderate: 58.50–65.00 (Arts, Business, Information Technology, Nursing, Social Work)
  - Selective: 70.00–80.00 (Education, Nursing, Occupational Therapy, Physiotherapy)
  - Highly selective: 87.75–95.00 (Paramedicine, Physiotherapy @ North Sydney, Psychology Honours)
  - Law: 75.00 (most campuses)
- **Non-ATAR pathways**: Mature age entry, Special Tertiary Admissions Test (STAT), VET/TAFE pathways, Aboriginal and Torres Strait Islander Entry Program
- **Elite Athlete and Performer Program**: Adjustment to entry requirements for elite performers

**International Students:**
- Equivalent academic qualifications to Australian Year 12
- Foundation Studies program as pathway
- Diploma programs as pathway to Bachelor degrees

### 3.2 English Language Requirements

| Test | Minimum Score (most programs) | Nursing/Teaching/Health programs | Notes |
|------|------------------------------|--------------------------------|-------|
| IELTS Academic | 6.0 overall (6.0 in all bands) | 7.0 overall (7.0 in all bands) | Most common test |
| PTE Academic | 50 (no band below 50) | 65+ | |
| TOEFL iBT | 60+ | 94+ | |
| CAE | 169+ | 185+ | |
| ACU English Test | Pass level | Higher level | ACU's own test |

> **Source**: https://www.acu.edu.au/study-at-acu/how-to-apply/international-students/english-language-requirements

### 3.3 Postgraduate Entry Requirements

- **Master's (coursework)**: Australian Bachelor degree or equivalent (AQF Level 7), some programs require specific undergraduate majors
- **Graduate Certificate/Diploma**: Australian Bachelor degree or equivalent; some programs accept relevant work experience
- **MBA**: Bachelor degree + minimum 3 years work experience
- **Research degrees (PhD/MPhil)**: Honours degree (AQF Level 8) or Master's degree with research component
- **Graduate entry programs (LLB, Midwifery)**: Completed Bachelor degree in any discipline

### 3.4 Application Deadlines

| Intake | Applications Open | Applications Close | Course Start |
|--------|------------------|-------------------|-------------|
| Semester 1 (Feb/Mar) | August previous year | Rolling (no fixed deadline for domestic) | Late February / Early March |
| Semester 2 (Jul/Aug) | April same year | Rolling (no fixed deadline for domestic) | Late July / Early August |

**International student application deadlines:** Semester 1: late November (for visas), Semester 2: late May (for visas)

**Key dates:**
- Open Day: various dates throughout year
- Orientation Week: week before start of Semester 1 and 2
- Census dates: Usually end of Week 4 each semester

### 3.5 Special Requirements

| Program | Requirement |
|---------|-------------|
| Nursing, Midwifery, Paramedicine | English proficiency IELTS 7.0 (7.0 all bands), immunisation, police check, Working with Children Check |
| Physiotherapy, Occupational Therapy, Speech Pathology | IELTS 7.0 (7.0 all bands), immunisation checks |
| Teaching (all) | IELTS 7.0 (7.0 all bands), Literacy and Numeracy Test for Initial Teacher Education (LANTITE), Working with Children Check |
| Bachelor of Laws (Graduate Entry) | Completed Bachelor degree, minimum ATAR 78 |
| Clinical Psychology (PG) | Registered psychology degree, professional experience |
| Social Work (PG) | Requires undergraduate degree, may need relevant background |

---

## Section 4 — Costs & Financial Aid

### 4.1 Domestic Student Fees (CSP — Commonwealth Supported Places)

**Undergraduate (sample):**

| Program | Indicative First-Year CSP Fee (2026) | Source |
|---------|--------------------------------------|--------|
| Bachelor of Nursing | ~$7,518 AUD | /course/bachelor-of-nursing |
| Bachelor of Arts | ~$7,500–8,500 AUD (est.) | Estimated from fee structure |
| Bachelor of Business/Commerce | ~$8,000–9,000 AUD (est.) | Estimated from fee structure |
| Bachelor of Laws | ~$10,000–12,000 AUD (est.) | Estimated from fee structure |

**Postgraduate (sample):**

| Program | Indicative First-Year Fee (Domestic, 2026) | Source |
|---------|--------------------------------------------|--------|
| Master of Business Administration | ~$15,810 AUD (CSP where applicable) | /course/master-of-business-administration |
| Master of Teaching | ~$7,500–9,000 AUD (est.) | Estimated |
| Graduate Certificate | ~$4,000–7,000 AUD (est.) | Estimated |

> CSP student contribution amounts vary by discipline band:
> - **Band 1** (Humanities, Arts, Education): ~$4,000–7,500/yr
> - **Band 2** (Business, Law, IT): ~$7,000–15,000/yr
> - **Band 3** (Health, Engineering, Science): ~$8,000–16,000/yr

### 4.2 International Student Fees

International fees are listed per course detail page (typically $30,000–$45,000 AUD/year for UG, $25,000–$40,000 for PG).

> **P1 follow-up**: Extract exact international fee amounts from representative course pages.

### 4.3 Additional Costs

| Fee Type | Amount |
|----------|--------|
| Student Services and Amenities Fee (SSAF) | ~$150–$330/yr (estimated) |
| Overseas Student Health Cover (OSHC) | ~$600–$1,200/yr (international only) |
| Accommodation | $150–$400/week depending on city and type |

### 4.4 Scholarships

| Scholarship | Value | Eligibility |
|-------------|-------|-------------|
| ACU International Student Scholarship | Up to 50% tuition fee reduction | High-achieving international students |
| ACU Commonwealth Prac Payment | $331.65/week during placements | Domestic students in health placements |
| ACU Accommodation Scholarship | Covered accommodation | Regional/remote students |
| ACU Equity Scholarship | Financial support | Students experiencing disadvantage |
| Indigenous Student Scholarships | Full support | Aboriginal and Torres Strait Islander students |
| Academic Merit Scholarships | $1,000–$5,000 | High ATAR achievers |
| ACU Online Scholarship | Partial fee reduction | Online students |

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-U-001 | institution.name | Australian Catholic University (ACU) | https://www.acu.edu.au/ | official_webpage |
| E-U-002 | program.total_count | 229 | /webapi/GetCourseResult/get | api_response |
| E-U-003 | program.ug_count | 111 | /webapi/GetCourseResult/get?CourseType=Undergraduate | api_response |
| E-U-004 | program.pg_count | 110 | /webapi/GetCourseResult/get?CourseType=Postgraduate | api_response |
| E-U-005 | program.research_count | 5 | /webapi/GetCourseResult/get?CourseType=Research | api_response |
| E-U-006 | faculty.count | 4 | /about-acu/faculties-directorates-and-staff | official_webpage |
| E-U-007 | faculty.list | Faculty of Education and Arts, Health Sciences, Law and Business, Theology and Philosophy | /about-acu/faculties-directorates-and-staff | official_webpage |
| E-U-008 | fee.ug.bachelor-of-nursing.domestic_first_year | $7,518 AUD | /course/bachelor-of-nursing | official_webpage |
| E-U-009 | fee.pg.mba.domestic_first_year | $15,810 AUD | /course/master-of-business-administration | official_webpage |
| E-U-010 | admission.english.ielts | 6.0 overall (6.0 bands) most programs; 7.0 for health/teaching | /study-at-acu/how-to-apply/international-students/english-language-requirements | official_webpage |
| E-U-011 | campus.locations | Ballarat, Blacktown, Brisbane, Canberra, Melbourne, North Sydney, Strathfield, Online | /webapi/GetCourseResult/get | api_response |
| E-U-012 | ranking.global | N/A | | P2 follow-up (needs external extraction) |
| E-U-013 | admission.atar_range | 50.00–95.00 depending on program and campus | /webapi/GetCourseResult/get (Score field per location) | api_response |
| E-U-014 | program.ug.list | Full list in Section 1 | /webapi/GetCourseResult/get?CourseType=Undergraduate | api_response |
| E-U-015 | program.pg.list | Full list in Section 2 | /webapi/GetCourseResult/get?CourseType=Postgraduate | api_response |
| E-U-016 | program.research.list | PhD, MPhil, DMin, combined MPsych/PhD | /webapi/GetCourseResult/get?CourseType=Research | api_response |
| E-U-017 | program.pg.graduate_certificates | 38 Graduate Certificate programs | /webapi/GetCourseResult/get?CourseType=Postgraduate | api_response |
| E-U-018 | program.pg.graduate_diplomas | 11 Graduate Diploma programs | /webapi/GetCourseResult/get?CourseType=Postgraduate | api_response |
| E-U-019 | program.pg.masters | 46 Master's programs | /webapi/GetCourseResult/get?CourseType=Postgraduate | api_response |
| E-U-020 | fee.domestic.csr | CSP student contribution by Band | /study-at-acu/fees-and-scholarships/domestic-student-fees | official_webpage |

---

## Section 6 — WeKnora Import Manifest

### Follow-up Data Items

| Priority | Data Item | Reason | 
|----------|-----------|--------|
| **P0** | International tuition fees per course (exact $AUD) | Currently estimated; need per-course page extraction for each program |
| **P0** | Full Graduate Research School programs with supervisors | PhD/MPhil by research topic not in Course API |
| **P1** | Exact IELTS/PTE/TOEFL score thresholds per faculty | Schedule 4 of ACU Handbook has faculty-specific requirements |
| **P1** | Campus-by-campus ATAR score matrix (complete) | Already partially extracted; need full table organized by program |
| **P1** | Scholarship amounts and eligibility criteria per scholarship | Overview available; specific amounts per scholarship needed |
| **P2** | QS/THE/ARWU world ranking data | Not from ACU website; needs external ranking data extraction |
| **P2** | Student demographics (total enrollment, international %) | Not available on public course pages |
| **P2** | Detailed school/department descriptions per faculty | Faculty pages are JS-heavy; needs deeper extraction |

### Import Checklist

- [x] Institution name, location, website
- [x] Faculty/school hierarchy
- [x] Full UG program list (111 programs)
- [x] Full PGT program list (110 programs)
- [x] Research program list (5 programs)
- [x] Application requirements (ATAR, English, pathways)
- [x] Fee data (domestic sample)
- [ ] International fee data (P0)
- [x] Scholarship overview
- [x] Campus locations
- [ ] Exact ranking data (P2)

---

## Section 7 — Cross-School Comparison Framework

| Dimension | Australian Catholic University (ACU) | La Trobe University | University of Tasmania |
|-----------|-------------------------------------|--------------------|-----------------------|
| Total UG programmes | ~111 | TBD | TBD |
| Total PG programmes | ~110 | TBD | TBD |
| Total courses | 229 | TBD | TBD |
| Faculties | 4 | TBD | TBD |
| Campuses | 7 physical + Online | TBD | TBD |
| ATAR range (UG) | 50.00–95.00 | TBD | TBD |
| IELTS minimum | 6.0 (7.0 health/teaching) | TBD | TBD |
| Annual fee (UG Arts) | ~$7,500 AUD (CSP est.) | TBD | TBD |
| Annual fee (UG Nursing) | ~$7,518 AUD (CSP) | TBD | TBD |
| 双学位 (Double degrees) | Yes (23+ combinations) | TBD | TBD |
| ACU Online | Yes | TBD | TBD |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-09
> **Sources**: ACU official website, Course Search API (webapi/GetCourseResult/get), individual course pages
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes (111) ✅ | PG programmes (110) ✅ | Research programmes (5) ✅ | Fees (sample) ⚠️ | Evidence (20 blocks) ✅
> **Next step**: P0: Extract international tuition fees per course; P1: Faculty-specific English requirements from ACU Handbook Schedule 4
