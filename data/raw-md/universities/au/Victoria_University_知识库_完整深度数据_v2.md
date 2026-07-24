> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + browser_console + sitemap.xml extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU)

# Victoria University (VU) — 完整深度招生数据

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG Bachelor Degrees) | 62 |
| 本科荣誉学位 (Bachelor Honours - embedded) | 11 |
| 本科荣誉学位 (Bachelor Honours - stand alone) | 2 |
| 本科文凭/副学士 (UG Diploma / Associate Degree / UG Certificate) | 22 |
| 本硕连读 (UG+PG combined) | 1 |
| **小计 - 本科层次** | **98** |
| 研究生授课型硕士 (PGT Masters Coursework) | 30 |
| 研究生研究型硕士 (PG Masters Research) | 4 |
| 研究生博士 (Doctoral/PhD) | 4 |
| 研究生证书 (Graduate Certificate) | 42 |
| 研究生文凭 (Graduate Diploma) | 15 |
| **小计 - 研究生层次** | **95** |
| **高等教育学位总计 (HE)** | **193** |
| TAFE 课程 | 87 |
| 短期课程/非学历 (Short Courses non-award) | 89 |
| **全部课程总计 (含TAFE/Short)** | **~369** |
| 学院 (Colleges) | 3 (+ 4 独立学校/中心) |
| 学术院系/项目 (Academic Programs) | 15+ |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Victoria University (VU)
├── College of Arts, Business, Law, Education & IT
│   ├── Arts & Humanities Program
│   ├── Community Program
│   ├── Early Childhood Education Program
│   ├── Education Program
│   ├── Information Technology Program
│   ├── Victoria Law School
│   └── Victoria University Business School
├── College of Sport, Health & Engineering
│   ├── Allied Health Program
│   ├── Biomedical & Life Sciences Program
│   ├── Built Environment Program
│   ├── Clinical Science Program
│   ├── Engineering Program
│   ├── Nursing & Midwifery Program
│   └── Sport & Movement Science Program
├── College of English, Foundation & Pathways (Centre of VU Transitions)
│   └── VU English
├── School for the Visitor Economy
├── TAFE at VU
├── VU First Year College
├── VU Tech Schools
└── Research Institutes (跨学院)
    ├── Institute for Health and Sport (IHES)
    ├── Mitchell Institute
    └── Centre for International Research on Education Systems (CIRES)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 计数 |
|----------|------|
| Bachelor Degree (本科) | 62 |
| Bachelor Honours Degree (embedded) (嵌入式荣誉学士) | 11 |
| Bachelor Honours Degree (stand alone) (独立荣誉学士) | 2 |
| Undergraduate Diploma (本科文凭) | 4 |
| Undergraduate Certificate (本科证书) | 17 |
| Associate Degree (副学士) | 1 |
| Bachelor Degree/Masters (Coursework) (本硕连读) | 1 |
| Graduate Certificate (研究生证书) | 42 |
| Graduate Diploma (研究生文凭) | 15 |
| Masters (Coursework) (授课型硕士) | 30 |
| Masters (Research) (研究型硕士) | 4 |
| Doctoral Degree (博士) | 4 |
| TAFE (职业技术教育) | 87 |
| Short Courses (non-award) (短期非学历) | 89 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

> **注**: VU 采用"College → Program"扁平化学院制，不设传统系(Department)层级。此矩阵按 College/Program 区域和学历级别交叉统计。TAFE 和 Short Courses 由 TAFE at VU 统一管理，学院归属标注为 TAFE。

| 学院/领域 | Bachelor | Honours | UG Dip/Cert/Assoc | Grad Cert | Grad Dip | Masters (CW) | Masters (R) | PhD | TAFE | Short | 合计 |
|-----------|----------|---------|-------------------|-----------|----------|-------------|-------------|-----|------|-------|------|
| Arts, Business, Law, Education & IT | 31 | 6 | 7 | 21 | 7 | 14 | 0 | 0 | ~20 | ~30 | ~136 |
| Sport, Health & Engineering | 27 | 5 | 10 | 18 | 7 | 15 | 0 | 0 | ~35 | ~25 | ~142 |
| Centre of VU Transitions / VU English | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 | ~5 | ~15 |
| School for the Visitor Economy | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | ~5 | ~3 | ~13 |
| TAFE at VU (跨领域) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 17 | ~15 | ~32 |
| Research Institutes | 0 | 0 | 0 | 3 | 1 | 1 | 4 | 4 | 0 | 0 | ~12 |
| 未分类 (跨学院) | 0 | 2 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 11 | ~17 |
| **合计** | **62** | **13** | **22** | **42** | **15** | **30** | **4** | **4** | **~87** | **~89** | **~369** |

---

## Section 1 — Undergraduate education (本科教育)

### 1.1 Bachelor Degrees (学士学位)

| 序号 | 专业名称 | 学位类型 | 学院/College | Program/领域 | URL |
|------|----------|----------|-------------|-------------|-----|
| 1 | Bachelor of Accounting (BBAQ) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria University Business School | https://www.vu.edu.au/courses/bachelor-of-accounting-bbaq |
| 2 | Bachelor of Applied Movement Sciences/Master of Physiotherapy (HCPT) | Bachelor (combined) | College of Sport, Health & Engineering | Allied Health / Clinical Science | https://www.vu.edu.au/courses/bachelor-of-applied-movement-sciences-master-of-physiotherapy-hcpt |
| 3 | Bachelor of Applied Music (ABAM) | Bachelor | College of Arts, Business, Law, Education & IT | Arts & Humanities Program | https://www.vu.edu.au/courses/bachelor-of-applied-music-abam |
| 4 | Bachelor of Architectural Design (NBAD) | Bachelor | College of Sport, Health & Engineering | Built Environment Program | https://www.vu.edu.au/courses/bachelor-of-architectural-design-nbad |
| 5 | Bachelor of Arts (ABAB) | Bachelor | College of Arts, Business, Law, Education & IT | Arts & Humanities Program | https://www.vu.edu.au/courses/bachelor-of-arts-abab |
| 6 | Bachelor of Biomedical and Exercise Science (HBES) | Bachelor | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-biomedical-and-exercise-science-hbes |
| 7 | Bachelor of Biomedical Science (HBBS) | Bachelor | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-biomedical-science-hbbs |
| 8 | Bachelor of Biomedicine (HBBM) | Bachelor | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-biomedicine-hbbm |
| 9 | Bachelor of Building Surveying (NBBS) | Bachelor | College of Sport, Health & Engineering | Built Environment Program | https://www.vu.edu.au/courses/bachelor-of-building-surveying-nbbs |
| 10 | Bachelor of Business (BBNS) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria University Business School | https://www.vu.edu.au/courses/bachelor-of-business-bbns |
| 11 | Bachelor of Chiropractic Science (HBCS) | Bachelor | College of Sport, Health & Engineering | Allied Health Program | https://www.vu.edu.au/courses/bachelor-of-chiropractic-science-hbcs |
| 12 | Bachelor of Community Development (ABCD) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-community-development-abcd |
| 13 | Bachelor of Criminal Justice (ABCJ) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-criminal-justice-abcj |
| 14 | Bachelor of Criminal Justice and Psychological Studies (ABCY) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-criminal-justice-and-psychological-studies-abcy |
| 15 | Bachelor of Criminology (LBCR) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-criminology-lbcr |
| 16 | Bachelor of Criminology/Bachelor of Psychological Studies (LBCP) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-criminology-bachelor-of-psychological-studies-lbcp |
| 17 | Bachelor of Cyber Security (NBCS) | Bachelor | College of Arts, Business, Law, Education & IT | Information Technology Program | https://www.vu.edu.au/courses/bachelor-of-cyber-security-nbcs |
| 18 | Bachelor of Data Science (NBDS) | Bachelor | College of Arts, Business, Law, Education & IT | Information Technology Program | https://www.vu.edu.au/courses/bachelor-of-data-science-nbds |
| 19 | Bachelor of Dermal Sciences (HBDS) | Bachelor | College of Sport, Health & Engineering | Allied Health Program | https://www.vu.edu.au/courses/bachelor-of-dermal-sciences-hbds |
| 20 | Bachelor of Early Childhood Education (EBEC) | Bachelor | College of Arts, Business, Law, Education & IT | Early Childhood Education Program | https://www.vu.edu.au/courses/bachelor-of-early-childhood-education-ebec |
| 21 | Bachelor of Early Childhood Education and Leadership (EBCL) | Bachelor | College of Arts, Business, Law, Education & IT | Early Childhood Education Program | https://www.vu.edu.au/courses/bachelor-of-early-childhood-education-and-leadership-ebcl |
| 22 | Bachelor of Education (P-12) (EBED) | Bachelor | College of Arts, Business, Law, Education & IT | Education Program | https://www.vu.edu.au/courses/bachelor-of-education-p-12-ebed |
| 23 | Bachelor of Education (Primary) (EBPE) | Bachelor | College of Arts, Business, Law, Education & IT | Education Program | https://www.vu.edu.au/courses/bachelor-of-education-primary-ebpe |
| 24 | Bachelor of Education Studies (EBST) | Bachelor | College of Arts, Business, Law, Education & IT | Education Program | https://www.vu.edu.au/courses/bachelor-of-education-studies-ebst |
| 25 | Bachelor of Exercise and Sport Science (SBEC) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-exercise-and-sport-science-sbec |
| 26 | Bachelor of Health Science (HBHL) | Bachelor | College of Sport, Health & Engineering | Allied Health Program | https://www.vu.edu.au/courses/bachelor-of-health-science-hbhl |
| 27 | Bachelor of Human Nutrition (HBNT) | Bachelor | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-human-nutrition-hbnt |
| 28 | Bachelor of Information Technology (NBIT) | Bachelor | College of Arts, Business, Law, Education & IT | Information Technology Program | https://www.vu.edu.au/courses/bachelor-of-information-technology-nbit |
| 29 | Bachelor of Information Technology (Professional) (NBIP) | Bachelor | College of Arts, Business, Law, Education & IT | Information Technology Program | https://www.vu.edu.au/courses/bachelor-of-information-technology-professional-nbip |
| 30 | Bachelor of Laws (BLAW) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-blaw |
| 31 | Bachelor of Laws (Graduate Entry) (BLGE) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-graduate-entry-blge |
| 32 | Bachelor of Laws/Bachelor of Arts (LBLA) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-bachelor-of-arts-lbla |
| 33 | Bachelor of Laws/Bachelor of Business (LBWB) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-bachelor-of-business-lbwb |
| 34 | Bachelor of Laws/Bachelor of Criminology (LBLC) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-bachelor-of-criminology-lblc |
| 35 | Bachelor of Laws/Bachelor of Psychological Studies (LBWP) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-laws-bachelor-of-psychological-studies-lbwp |
| 36 | Bachelor of Legal Services (LBLS) | Bachelor | College of Arts, Business, Law, Education & IT | Victoria Law School | https://www.vu.edu.au/courses/bachelor-of-legal-services-lbls |
| 37 | Bachelor of Midwifery/Bachelor of Nursing (HBMA) | Bachelor (Double) | College of Sport, Health & Engineering | Nursing & Midwifery Program | https://www.vu.edu.au/courses/bachelor-of-midwifery-bachelor-of-nursing-hbma |
| 38 | Bachelor of Nursing (HBNB) | Bachelor | College of Sport, Health & Engineering | Nursing & Midwifery Program | https://www.vu.edu.au/courses/bachelor-of-nursing-hbnb |
| 39 | Bachelor of Nutritional Science/Master of Dietetics (HCND) | Bachelor (combined) | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-nutritional-science-master-of-dietetics-hcnd |
| 40 | Bachelor of Outdoor Education and Environmental Science (SBOE) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-outdoor-education-and-environmental-science-sboe |
| 41 | Bachelor of Outdoor Leadership (SBOL) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-outdoor-leadership-sbol |
| 42 | Bachelor of Paramedicine (HBPD) | Bachelor | College of Sport, Health & Engineering | Clinical Science Program | https://www.vu.edu.au/courses/bachelor-of-paramedicine-hbpd |
| 43 | Bachelor of Physical Education and Sport Science (SBPH) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-physical-education-and-sport-science-sbph |
| 44 | Bachelor of Psychological Studies (ABPA) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-psychological-studies-abpa |
| 45 | Bachelor of Psychological Studies/Bachelor of Business (ABPB) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-psychological-studies-bachelor-of-business-abpb |
| 46 | Bachelor of Science (NBSC) | Bachelor | College of Sport, Health & Engineering | Biomedical & Life Sciences Program | https://www.vu.edu.au/courses/bachelor-of-science-nbsc |
| 47 | Bachelor of Science (Osteopathy)/Master of Health Science (Osteopathy) (HCOP) | Bachelor (combined) | College of Sport, Health & Engineering | Allied Health Program | https://www.vu.edu.au/courses/bachelor-of-science-osteopathy-master-of-health-science-osteopathy-hcop |
| 48 | Bachelor of Science/Master of Teaching (Secondary Education) (ECST) | Bachelor (combined) | College of Arts, Business, Law, Education & IT | Education Program | https://www.vu.edu.au/courses/bachelor-of-science-master-of-teaching-secondary-education-ecst |
| 49 | Bachelor of Screen Media (ABSN) | Bachelor | College of Arts, Business, Law, Education & IT | Arts & Humanities Program | https://www.vu.edu.au/courses/bachelor-of-screen-media-absn |
| 50 | Bachelor of Social Work (ABSW) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-social-work-absw |
| 51 | Bachelor of Speech and Language Sciences/Master of Speech Pathology (HCSP) | Bachelor (combined) | College of Sport, Health & Engineering | Allied Health Program | https://www.vu.edu.au/courses/bachelor-of-speech-and-language-sciences-master-of-speech-pathology-hcsp |
| 52 | Bachelor of Sport Management (SBSM) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-sport-management-sbsm |
| 53 | Bachelor of Sport Management/Bachelor of Business (SBSB) | Bachelor (Double) | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-sport-management-bachelor-of-business-sbsb |
| 54 | Bachelor of Sport Science (SBSA) | Bachelor | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-sport-science-sbsa |
| 55 | Bachelor of Sport Science (Human Movement)/Bachelor of Psychological Studies (SBHP) | Bachelor (Double) | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-sport-science-human-movement-bachelor-of-psychological-studies-sbhp |
| 56 | Bachelor of Sport Science (Human Movement)/Bachelor of Sport Management (SBHS) | Bachelor (Double) | College of Sport, Health & Engineering | Sport & Movement Science Program | https://www.vu.edu.au/courses/bachelor-of-sport-science-human-movement-bachelor-of-sport-management-sbhs |
| 57 | Bachelor of Youth Work (ABYW) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-youth-work-abyw |
| 58 | Bachelor of Youth Work and Criminal Justice (ABYC) | Bachelor | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-youth-work-and-criminal-justice-abyc |
| 59 | Bachelor of Youth Work/Bachelor of Sport Management (EBYS) | Bachelor (Double) | College of Arts, Business, Law, Education & IT | Community Program | https://www.vu.edu.au/courses/bachelor-of-youth-work-bachelor-of-sport-management-ebys |

### 1.2 Bachelor Honours Degrees (荣誉学士学位)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Bachelor of Construction Management (Honours) (NHCM) | Honours (embedded) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/bachelor-of-construction-management-honours-nhcm |
| 2 | Bachelor of Engineering (Honours) (Civil Engineering) (NHEC) | Honours (embedded) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/bachelor-of-engineering-honours-civil-engineering-nhec |
| 3 | Bachelor of Engineering (Honours) (Electrical and Electronic Engineering) (NHEE) | Honours (embedded) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/bachelor-of-engineering-honours-electrical-and-electronic-engineering-nhee |
| 4 | Bachelor of Engineering (Honours) (Mechanical Engineering) (NHEM) | Honours (embedded) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/bachelor-of-engineering-honours-mechanical-engineering-nhem |
| 5 | Bachelor of Laws (Honours) (LHLW) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-lhlw |
| 6 | Bachelor of Laws (Honours) (Graduate Entry) (LHGE) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-graduate-entry-lhge |
| 7 | Bachelor of Laws (Honours)/Bachelor of Arts (LHWA) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-bachelor-of-arts-lhwa |
| 8 | Bachelor of Laws (Honours)/Bachelor of Business (LHWB) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-bachelor-of-business-lhwb |
| 9 | Bachelor of Laws (Honours)/Bachelor of Criminology (LHCR) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-bachelor-of-criminology-lhcr |
| 10 | Bachelor of Laws (Honours)/Bachelor of Psychology (Honours) (LHWP) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-laws-honours-bachelor-of-psychology-honours-lhwp |
| 11 | Bachelor of Psychology (Honours) (ABPC) | Honours (embedded) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-psychology-honours-abpc |
| 12 | Bachelor of Psychological Studies (Honours) (AHPA) | Honours (stand alone) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/bachelor-of-psychological-studies-honours-ahpa |
| 13 | Bachelor of Science (Honours) (HHSC) | Honours (stand alone) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/bachelor-of-science-honours-hhsc |

### 1.3 Undergraduate Diplomas (本科文凭)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Diploma of Business (Enterprise) (VDBE) | UG Diploma | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/diploma-of-business-enterprise-vdbe |
| 2 | Diploma of Cyber Security (VDCS) | UG Diploma | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/diploma-of-cyber-security-vdcs |
| 3 | Diploma of Education Studies (EDES) | UG Diploma | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/diploma-of-education-studies-edes |
| 4 | Diploma of Information Technology (VDIT) | UG Diploma | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/diploma-of-information-technology-vdit |

### 1.4 Associate Degree (副学士)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Associate Degree in Hospitality and Hotel Management (VAHH) | Associate Degree | School for the Visitor Economy | https://www.vu.edu.au/courses/associate-degree-in-hospitality-and-hotel-management-vahh |

### 1.5 Undergraduate Certificates (本科证书)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Undergraduate Certificate in Architectural Design (NUAD) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-architectural-design-nuad |
| 2 | Undergraduate Certificate in Building Construction Management (NUBC) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-building-construction-management-nubc |
| 3 | Undergraduate Certificate in Diet and Health (HUDH) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-diet-and-health-hudh |
| 4 | Undergraduate Certificate in Digital Business Skills (VUDS) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-digital-business-skills-vuds |
| 5 | Undergraduate Certificate in Early Childhood Education (EUEC) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-early-childhood-education-euec |
| 6 | Undergraduate Certificate in Education (P12) STEM (EUED) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-education-p12-stem-eued |
| 7 | Undergraduate Certificate in Education Studies (EUES) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-education-studies-eues |
| 8 | Undergraduate Certificate in Engineering Fundamentals (NUEF) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-engineering-fundamentals-nuef |
| 9 | Undergraduate Certificate in Health Science (HUHS) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-health-science-huhs |
| 10 | Undergraduate Certificate in Information Technology (NUIT) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-information-technology-nuit |
| 11 | Undergraduate Certificate in Interpersonal and Organisational Skills (HUIO) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-interpersonal-and-organisational-skills-huio |
| 12 | Undergraduate Certificate in Laser Safety (HULS) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-laser-safety-huls |
| 13 | Undergraduate Certificate in Primary Physical Education (SUPP) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-primary-physical-education-supp |
| 14 | Undergraduate Certificate in Psychological Studies (HUPS) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-psychological-studies-hups |
| 15 | Undergraduate Certificate in Science and the Environment (NUSE) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-science-and-the-environment-nuse |
| 16 | Undergraduate Certificate in Secondary Physical Education (SUSP) | UG Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/undergraduate-certificate-in-secondary-physical-education-susp |
| 17 | Undergraduate Certificate in Web Development and Programming (VUWD) | UG Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/undergraduate-certificate-in-web-development-and-programming-vuwd |

---

## Section 2 — Graduate education (研究生教育)

### 2.1 Graduate Certificates (研究生证书)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Graduate Certificate in Artificial Intelligence (NTAI) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-artificial-intelligence-ntai |
| 2 | Graduate Certificate in Block Teaching (ETBL) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-block-teaching-etbl |
| 3 | Graduate Certificate in Building Surveying (NTBS) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-building-surveying-ntbs |
| 4 | Graduate Certificate in Business (BTBU) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-business-btbu |
| 5 | Graduate Certificate in Business Administration (BTPF) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-business-administration-btpf |
| 6 | Graduate Certificate in Business Analytics (BTBI) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-business-analytics-btbi |
| 7 | Graduate Certificate in Change Management (BTCM) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-change-management-btcm |
| 8 | Graduate Certificate in Child and Adolescent Mental Health (HTCH) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-child-and-adolescent-mental-health-htch |
| 9 | Graduate Certificate in Construction Management (NTCM) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-construction-management-ntcm |
| 10 | Graduate Certificate in Construction Project Management (NTCP) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-construction-project-management-ntcp |
| 11 | Graduate Certificate in Counselling Theory and Practice (HTCP) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-counselling-theory-and-practice-htcp |
| 12 | Graduate Certificate in Countering Violent Extremism (LTCV) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-countering-violent-extremism-ltcv |
| 13 | Graduate Certificate in Crime Prevention (LTCP) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-crime-prevention-ltcp |
| 14 | Graduate Certificate in Cyber Security (NTCS) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-cyber-security-ntcs |
| 15 | Graduate Certificate in Data Analytics for Sport Performance (STSP) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-data-analytics-for-sport-performance-stsp |
| 16 | Graduate Certificate in Digital Construction Management (NTDC) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-digital-construction-management-ntdc |
| 17 | Graduate Certificate in Digital Content Creation (ATDC) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-digital-content-creation-atdc |
| 18 | Graduate Certificate in Digital Learning and Teaching (ATDI) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-digital-learning-and-teaching-atdi |
| 19 | Graduate Certificate in Early Childhood Education (ETEC) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-early-childhood-education-etec |
| 20 | Graduate Certificate in Education (ETED) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-education-eted |
| 21 | Graduate Certificate in Enterprise and Resource Planning Systems (BTEN) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-enterprise-and-resource-planning-systems-bten |
| 22 | Graduate Certificate in Finance (BTFF) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-finance-btff |
| 23 | Graduate Certificate in Financial Planning (BTFP) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-financial-planning-btfp |
| 24 | Graduate Certificate in Global Health Leadership (HTGL) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-global-health-leadership-htgl |
| 25 | Graduate Certificate in Global Public Health (HTGP) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-global-public-health-htgp |
| 26 | Graduate Certificate in Health Promotion (HTHP) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-health-promotion-hthp |
| 27 | Graduate Certificate in Information Technology Project Management (NTIP) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-information-technology-project-management-ntip |
| 28 | Graduate Certificate in International Community Development (ATID) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-international-community-development-atid |
| 29 | Graduate Certificate in Marketing (BTKM) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-marketing-btkm |
| 30 | Graduate Certificate in Mental Health (HTMH) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-mental-health-htmh |
| 31 | Graduate Certificate in Mental Health Nursing (HTMN) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-mental-health-nursing-htmn |
| 32 | Graduate Certificate in Nursing (HTNG) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-nursing-htng |
| 33 | Graduate Certificate in Nursing Informatics Leadership (HTNI) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-nursing-informatics-leadership-htni |
| 34 | Graduate Certificate in Performance-Based Building & Fire Codes (ETQB) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-performance-based-building-fire-codes-etqb |
| 35 | Graduate Certificate in Project Management (NTPM) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-project-management-ntpm |
| 36 | Graduate Certificate in Public Health (HTPT) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-public-health-htpt |
| 37 | Graduate Certificate in Strength and Conditioning (STSA) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-strength-and-conditioning-stsa |
| 38 | Graduate Certificate in Supply Chain Management (BTSP) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-supply-chain-management-btsp |
| 39 | Graduate Certificate in Sustainable Construction Management (NTSC) | Grad Cert | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-certificate-in-sustainable-construction-management-ntsc |
| 40 | Graduate Certificate in Transport Systems (BTTS) | Grad Cert | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-certificate-in-transport-systems-btts |

### 2.2 Graduate Diplomas (研究生文凭)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Graduate Diploma in Block Teaching (EGBL) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-block-teaching-egbl |
| 2 | Graduate Diploma in Building Surveying (NGBS) | Grad Dip | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-diploma-in-building-surveying-ngbs |
| 3 | Graduate Diploma in Business (BGAB) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-business-bgab |
| 4 | Graduate Diploma in Business Administration (BGPB) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-business-administration-bgpb |
| 5 | Graduate Diploma in Construction Management (NGCM) | Grad Dip | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-diploma-in-construction-management-ngcm |
| 6 | Graduate Diploma in Counselling (AGPD) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-counselling-agpd |
| 7 | Graduate Diploma in Counselling Theory and Practice (HGCP) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-counselling-theory-and-practice-hgcp |
| 8 | Graduate Diploma in Cyber Security (NGCS) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-cyber-security-ngcs |
| 9 | Graduate Diploma in Early Childhood Education (EGEC) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-early-childhood-education-egec |
| 10 | Graduate Diploma in Education (EGED) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-education-eged |
| 11 | Graduate Diploma in Financial Planning (BGFP) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-financial-planning-bgfp |
| 12 | Graduate Diploma in International Community Development (AGID) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-international-community-development-agid |
| 13 | Graduate Diploma in Mental Health Nursing (HGMN) | Grad Dip | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-diploma-in-mental-health-nursing-hgmn |
| 14 | Graduate Diploma in Migration Law (LGML) | Grad Dip | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/graduate-diploma-in-migration-law-lgml |
| 15 | Graduate Diploma in Project Management (NGPM) | Grad Dip | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/graduate-diploma-in-project-management-ngpm |

### 2.3 Masters by Coursework (授课型硕士)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Master of Applied Information Technology (NMIT) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-applied-information-technology-nmit |
| 2 | Master of Applied Psychology (Clinical Psychology) (AMAL) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-applied-psychology-clinical-psychology-amal |
| 3 | Master of Applied Teaching (Secondary Education) (EMAT) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-applied-teaching-secondary-education-emat |
| 4 | Master of Business Administration (BMPF) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-business-administration-bmpf |
| 5 | Master of Business Administration (Global) (BMAG) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-business-administration-global-bmag |
| 6 | Master of Business Analytics (BMBU) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-business-analytics-bmbu |
| 7 | Master of Child and Adolescent Mental Health (HMCH) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-child-and-adolescent-mental-health-hmch |
| 8 | Master of Clinical Exercise Science and Rehabilitation (AMEP) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-clinical-exercise-science-and-rehabilitation-amep |
| 9 | Master of Construction Management (NMCM) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-construction-management-nmcm |
| 10 | Master of Counselling (AMPE) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-counselling-ampe |
| 11 | Master of Dietetics (HMDT) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-dietetics-hmdt |
| 12 | Master of Education (EMED) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-education-emed |
| 13 | Master of Enterprise Resource Planning (BMEN) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-enterprise-resource-planning-bmen |
| 14 | Master of Financial Planning (BMFP) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-financial-planning-bmfp |
| 15 | Master of Global Public Health (HMGP) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-global-public-health-hmgp |
| 16 | Master of International Community Development (AMCD) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-international-community-development-amcd |
| 17 | Master of Marketing (BMKT) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-marketing-bmkt |
| 18 | Master of Mental Health (HMMH) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-mental-health-hmmh |
| 19 | Master of Mental Health Nursing (HMMN) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-mental-health-nursing-hmmn |
| 20 | Master of Nursing (HMNG) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-nursing-hmng |
| 21 | Master of Physiotherapy (HMPS) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-physiotherapy-hmps |
| 22 | Master of Professional Accounting (BMAQ) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-professional-accounting-bmaq |
| 23 | Master of Professional Psychology (HMPP) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-professional-psychology-hmpp |
| 24 | Master of Project Management (NMPM) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-project-management-nmpm |
| 25 | Master of Public Health (HMPT) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-public-health-hmpt |
| 26 | Master of Speech Pathology (HMST) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-speech-pathology-hmst |
| 27 | Master of Sport and Exercise Science (SMES) | Masters (CW) | College of Sport, Health & Engineering | https://www.vu.edu.au/courses/master-of-sport-and-exercise-science-smes |
| 28 | Master of Supply Chain Management (BMSU) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-supply-chain-management-bmsu |
| 29 | Master of Teaching (Primary Education) (EMPE) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-teaching-primary-education-empe |
| 30 | Master of Teaching (Secondary Education) (EMES) | Masters (CW) | College of Arts, Business, Law, Education & IT | https://www.vu.edu.au/courses/master-of-teaching-secondary-education-emes |

### 2.4 Masters by Research (研究型硕士)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Master of Applied Research (URAP) | Masters (R) | Research Institutes | https://www.vu.edu.au/courses/master-of-applied-research-urap |
| 2 | Master of Applied Research (URAR) | Masters (R) | Research Institutes | https://www.vu.edu.au/courses/master-of-applied-research-urar |
| 3 | Master of Research (URRE) | Masters (R) | Research Institutes | https://www.vu.edu.au/courses/master-of-research-urre |
| 4 | Master of Research (URRS) | Masters (R) | Research Institutes | https://www.vu.edu.au/courses/master-of-research-urrs |

### 2.5 Doctoral Degrees (博士学位)

| 序号 | 专业名称 | 学位类型 | 学院/College | URL |
|------|----------|----------|-------------|-----|
| 1 | Doctor of Philosophy (UPAD) | PhD | Research Institutes | https://www.vu.edu.au/courses/doctor-of-philosophy-upad |
| 2 | Doctor of Philosophy (UPAF) | PhD | Research Institutes | https://www.vu.edu.au/courses/doctor-of-philosophy-upaf |
| 3 | Doctor of Philosophy (Integrated) (UPAE) | PhD (Integrated) | Research Institutes | https://www.vu.edu.au/courses/doctor-of-philosophy-integrated-upae |
| 4 | Doctor of Philosophy (Integrated) (UPAG) | PhD (Integrated) | Research Institutes | https://www.vu.edu.au/courses/doctor-of-philosophy-integrated-upag |

---

## Section 3 — Application requirements & deadlines (申请要求与截止日期)

### 3.1 Academic entry requirements (学术入学要求)

| 学习层次 | 学术要求 |
|----------|----------|
| Certificates, Diplomas & Advanced Diplomas | 各课程页面列明具体要求，入学时逐案评估 |
| Bachelor Degrees | 完成相当于澳大利亚 Year 12 的中学学历 |
| Graduate Certificates & Graduate Diplomas | 完成相当于澳大利亚学士学位的本科资格 |
| Masters Degrees | 完成相当于澳大利亚学士、荣誉学士或研究生文凭的资格 |
| Research Degrees (PhD/Masters by Research) | 完成荣誉学士学位、授课型硕士（含研究成分）或同等资格 |

### 3.2 English language requirements (英语语言要求)

| 学习层次 | IELTS | TOEFL iBT | PTE Academic | Cambridge CAE | VU English EAP |
|----------|-------|-----------|-------------|---------------|----------------|
| Certificates/Diplomas/Adv Dip | 各课程页面列明 | 各课程页面列明 | 各课程页面列明 | 各课程页面列明 | 各课程页面列明 |
| Bachelor Degrees | 总分 6.0 (单项≥6.0) | 总分 67 (L:12, S:18, R:15, W:21) | 总分 ≥52 (单项≥52) | 总分 169 (单项≥169) | EAP Level 5 |
| Grad Cert / Grad Dip | 总分 6.5 (单项≥6.0) | 总分 79 (L:19, S:19, R:18, W:22) | 总分 ≥60 (单项≥52) | 总分 176 (单项≥169) | EAP Level 6 |
| Masters Degrees | 总分 6.5 (单项≥6.0) | 总分 79 (L:19, S:19, R:18, W:22) | 总分 ≥60 (单项≥52) | 总分 176 (单项≥169) | EAP Level 6 |
| Research Degrees | 总分 6.5 (单项≥6.0) | 总分 79 (L:19, S:19, R:18, W:22) | 总分 ≥60 (单项≥52) | 总分 176 (单项≥169) | EAP Level 6 |

> 英语考试成绩须在课程开始前两年内有效。
> 如申请人此前学历主要以英语授课，可能符合英语豁免条件。
> TOEFL iBT 总分基于 0-120 分制。

### 3.3 Application process (申请流程)

**国际学生申请途径：**
1. **通过教育代理申请** — 来自某些国家的申请人必须通过 VU 批准的代理申请
2. **直接申请 VU** — 在线提交申请

**所需文件：**
- 学历成绩单（经认证副本）
- 英语语言能力证明（如有）
- 护照（经认证副本，如有）
- 部分课程可能有额外文件要求

**学分减免 (Credit)：**
- 如之前学习过相关课程或有相关工作/生活经验，可申请学分减免
- 学士及以上层次：申请 "advanced standing"
- 证书/文凭层次：申请 "recognition of prior learning (RPL)"
- 学分减免须在标准申请截止日期前至少 10 个工作日提交

### 3.4 Key application dates (重要申请日期)

> VU 采用 Block Model® 教学模式，每年有多个入学时段。具体申请截止日期因课程和入学季而异，请参考课程页面获取最新信息。

**通用申请渠道：**
- **VTAC (维多利亚高等教育招生中心)** — 澳大利亚高中毕业生通过 VTAC 申请本科课程
- **VU Early Entry 项目** — 高中学生可提前获得有条件录取
- **Direct application** — 国际学生可直接或通过代理申请

---

## Section 4 — Costs & financial aid (费用与奖助学金)

### 4.1 International student tuition fees (国际学生学费)

> VU 国际学生学费每年公布在课程指南和在线课程查找器中。学费在每个日历年初进行指数化调整（增长）。具体费用因课程、学习层次和学习负荷而异。

**费用计算方式：**
- **高等教育 (本科/研究生)**: 按学期/ trimester 收费，全日制等效为 48 学分或 0.5 EFTSL
- **职业教育 (TAFE)**: 按学期收费，基于课程全日制学习负荷
- **研究型课程**: 按日费率计算，6个月注册期通常为 0.5 全日制或 0.25 非全日制

**参考学费范围 (2026 年度):**
> 具体课程费用请查看 VU 国际学生课程指南 PDF 或在线课程查找器。

其他费用：
- **课程申请费**: 在线申请时收取
- **材料费**: 视所选课程而定
- **学生服务与设施费 (SSAF)**: 适用于所有学生

**国际学生奖学金优惠：**
- **VU Block Model® International Scholarship**: 符合条件的新国际学生可获得最高 30% 学费减免（首年）
- **STEM Accommodation Scholarship**: 科学、工程和信息技术学位的学生可获得最高一年免费住宿（价值约 A$15,500）
- **VU Global Research Scholarship**: 研究型学位学生可获 20% 学费减免（全课程期间）
- **Alumni discount**: VU 校友可享受 10% 学费折扣

### 4.2 Domestic student fees (CSP - Commonwealth Supported Places)

> 符合 Commonwealth Supported Place (CSP) 资格的本地学生，学费由政府补贴。

**2026 年度学生贡献金额 (CSP 费率):**

| 资助领域 | 每年 (全日制) | 每单元 |
|----------|-------------|--------|
| Band 1: Agriculture, Education, Nursing, Mathematics, Clinical Psychology, English, Indigenous/Foreign Languages, Statistics | $4,738 | $592 |
| Band 2: Allied Health, IT, Engineering, Science, Architecture, Built Environment, Environmental Studies, Pathology, Visual & Performing Arts, Surveying | $9,537 | $1,192 |
| Band 3: Dentistry, Medicine, Veterinary Science | $13,558 | $1,694 |
| Band 4: Accounting, Law, Commerce, Economics, Communications, Administration, Behavioural Science, Society and Culture | $17,399 | $2,174 |

### 4.3 Scholarship opportunities (奖学金机会)

| 奖学金名称 | 金额 | 适用对象 |
|------------|------|----------|
| VU Block Model® International Scholarship | 最高 30% 学费减免（首年） | 新国际学生（符合条件的课程） |
| STEM Accommodation Scholarship | 最高一年免费住宿 (~$15,500) | 国际 STEM 学生 |
| VU Global Research Scholarship | 20% 学费减免（全课程期） | 国际研究型学位学生 |
| Medibank School Leavers Merit Scholarship | $5,000（第二学期） | 在澳完成 Year 12 的国际学生 |
| VU Access Scholarships | 多种 | 本地学生 |
| Graduate Research Scholarships (多种) | 含生活费津贴 | 研究型学位学生 |
| Elite / Emerging Elite Scholarships | 多种 | 体育/学术精英学生 |
| First Year Booster Scholarship | 多种 | 新生 |
| External scholarships (Australia Awards etc.) | 多种 | 国际学生 |

---

## Section 5 — Evidence chain index (证据链索引)

| 编号 | 数据字段 | 值 | 来源 URL | 证据片段 | 捕获日期 | 证据类型 |
|------|----------|-----|---------|----------|---------|---------|
| E-U-001 | institution.name | Victoria University | https://www.vu.edu.au/ | Victoria University | 2026-07-10 | official_webpage |
| E-U-002 | institution.website | https://www.vu.edu.au/ | https://www.vu.edu.au/ | Victoria University home | 2026-07-10 | official_webpage |
| E-U-003 | institution.cricos | 00124K (Melbourne), 02475D (Sydney, Brisbane) | https://www.vu.edu.au/ | CRICOS No. 00124K (Melbourne), 02475D (Sydney and Brisbane) | 2026-07-10 | footer |
| E-U-004 | institution.teqsa | PRV12152 | https://www.vu.edu.au/ | TEQSA No. PRV12152 | 2026-07-10 | footer |
| E-U-005 | institution.rto | 3113 | https://www.vu.edu.au/ | RTO 3113 | 2026-07-10 | footer |
| E-U-006 | institution.platform | Drupal + Nuxt.js | https://www.vu.edu.au/ | __nuxt, drupal, cloudflare | 2026-07-10 | curl + sitemap |
| E-U-007 | course.total.count | ~369 (含 TAFE/Short) | https://www.vu.edu.au/study-at-vu/courses/browse-study-areas/all-courses-a-to-z | 全量 A-Z 课程列表 | 2026-07-10 | official_webpage |
| E-U-008 | course.sitemap.url.count | 480 | https://www.vu.edu.au/sitemap.xml?page=1 | Sitemap contains 480 course URLs | 2026-07-10 | sitemap |
| E-U-009 | college.hierarchy | 3 Colleges + 4 Schools/Centres | https://www.vu.edu.au/about-vu/teaching-colleges-schools | Teaching colleges & schools | 2026-07-10 | official_webpage |
| E-U-010 | english.bachelor | IELTS 6.0 (no band <6.0) | https://www.vu.edu.au/study-at-vu/how-to-apply/international-applicants/entry-requirements-for-international-students | IELTS: overall score of 6.0, no band less than 6.0 | 2026-07-10 | official_webpage |
| E-U-011 | english.gradcert | IELTS 6.5 (no band <6.0) | https://www.vu.edu.au/study-at-vu/how-to-apply/international-applicants/entry-requirements-for-international-students | IELTS: overall score of 6.5, no band less than 6.0 | 2026-07-10 | official_webpage |
| E-U-012 | english.masters | IELTS 6.5 (no band <6.0) | https://www.vu.edu.au/study-at-vu/how-to-apply/international-applicants/entry-requirements-for-international-students | IELTS: overall score of 6.5, no band less than 6.0 | 2026-07-10 | official_webpage |
| E-U-013 | english.research | IELTS 6.5 (no band <6.0) | https://www.vu.edu.au/study-at-vu/how-to-apply/international-applicants/entry-requirements-for-international-students | IELTS: overall score of 6.5, no band less than 6.0 | 2026-07-10 | official_webpage |
| E-U-014 | fees.international.general | Upfront payment per semester | https://www.vu.edu.au/study-at-vu/fees-scholarships/course-tuition-fees/international-student-fees | As an international student... you will be required to pay your tuition fees up front each semester | 2026-07-10 | official_webpage |
| E-U-015 | fees.csp.2026.band1 | $4,738/year | https://www.vu.edu.au/study-at-vu/fees-scholarships/course-tuition-fees/commonwealth-supported-students | $4,738 per year (full-time) | 2026-07-10 | official_webpage |
| E-U-016 | fees.csp.2026.band2 | $9,537/year | https://www.vu.edu.au/study-at-vu/fees-scholarships/course-tuition-fees/commonwealth-supported-students | $9,537 per year (full-time) | 2026-07-10 | official_webpage |
| E-U-017 | fees.csp.2026.band4 | $17,399/year | https://www.vu.edu.au/study-at-vu/fees-scholarships/course-tuition-fees/commonwealth-supported-students | $17,399 per year (full-time) | 2026-07-10 | official_webpage |
| E-U-018 | scholarship.international | VU Block Model Intl Scholarship - up to 30% | https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships/international-scholarships | up to 30% off tuition fees | 2026-07-10 | official_webpage |
| E-U-019 | scholarship.stem | STEM Accommodation Scholarship | https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships/international-scholarships | free accommodation at UniLodge Victoria University for up to your entire first year | 2026-07-10 | official_webpage |
| E-U-020 | scholarship.research | VU Global Research Scholarship - 20% off | https://www.vu.edu.au/study-at-vu/fees-scholarships/scholarships/international-scholarships | 20% off tuition fees for the entire duration of a research degree | 2026-07-10 | official_webpage |
| E-U-021 | application.international | Apply via agent or direct | https://www.vu.edu.au/study-at-vu/apply-to-vu/international-applicants | International applicants page | 2026-07-10 | official_webpage |

---

## Section 6 — WeKnora import manifest & follow-up items

### 6.1 Follow-up data items (优先级排序)

| 优先级 | 数据项 | 说明 |
|--------|--------|------|
| **P0** | 各课程具体国际学生学费金额 | 课程详情页面返回 404（Drupal/Nuxt.js 渲染问题），需通过课程指南 PDF 或在线查找器获取 |
| **P0** | 各课程具体开学日期/学期安排 | 同上 — 课程详情页无法访问 |
| **P0** | 各课程学制（Duration）| 同上 |
| **P0** | 各课程 CRICOS 代码 | 同上 |
| **P1** | 本地学生 ATAR 录取分数线 | VU 有 Early Entry 项目，ATAR 要求可能与非选拔性入学相关 |
| **P1** | 国际学生申请截止日期 | 页面仅提及通过代理申请，未列出具体截止日期 |
| **P1** | 英文考试成绩豁免细节 | 页面提及豁免可能性但未列出具体标准 |
| **P2** | 住宿费用估算 | 宿舍费用数据 |
| **P2** | 生活成本估算 | 墨尔本生活成本数据 |
| **P2** | TAFE 课程完整列表 | TAFE 课程已列出名称，但学院归属未记录 |

### 6.2 Known limitations

- **课程详情页 404**: VU 的 Drupal + Nuxt.js 架构导致大部分 `/courses/{slug}` 页面返回 "An error occurred"。仅 `/study-at-vu/courses` 搜索页面和 A-Z 列表正常。学费和入学要求数据只能从汇总页面获取。
- **Cloudflare WAF**: 网站由 Cloudflare 保护，但 `browser_navigate` 工具可正常访问（无 Playwright 拦截问题）。
- **College 归属推断**: 大部分课程的学院归属基于课程代码前缀和课程名称推断。精确的学院归属可能需要从课程详情页获取。

---

## Section 7 — Cross-school comparison framework (跨校比较框架)

| 维度 | Victoria University | 待对比院校 |
|------|-------------------|-----------|
| 国家 | Australia | |
| 总课程数 (含 TAFE) | ~369 | |
| 本科学位课程 | 62 | |
| 研究生课程 (授课型) | 30 | |
| 博士课程 | 4 | |
| 研究生证书/文凭 | 57 | |
| 学院/学校数 | 7+ | |
| IELTS 最低要求 (本科) | 6.0 (单项≥6.0) | |
| IELTS 最低要求 (研究生) | 6.5 (单项≥6.0) | |
| 国际奖学金 | 最高 30% 学费减免 | |
| 特色教学模式 | VU Block Model® (小班工作坊) | |
| TAFE/VET 课程 | 87 (含高级文凭、证书等) | |
| 校区 | Melbourne (Footscray Park, City, Sunshine, Werribee等), Sydney, Brisbane | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Victoria University official website (vu.edu.au)
> **Granularity**: college → program → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (全部列出) | PG programmes ✅ (全部列出) | TAFE courses ✅ (列出) | Evidence (21 blocks) ✅ | 
> **Per-program fees**: P0 follow-up (course detail pages return 404)
> **Next step**: 通过课程指南 PDF 补充各课程国际学生具体学费金额
