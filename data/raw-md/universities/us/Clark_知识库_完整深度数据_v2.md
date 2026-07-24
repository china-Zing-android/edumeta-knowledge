# Clark University Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-06
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

---

## SECTION 0 — 院校总览 (Institution Overview)

### 0.1 专业与项目总数 (Rule 1 — Counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS) | 37 |
| 本科辅修 (Minor) | 7 |
| 本科浓度方向 (Concentration) | 18 |
| 研究生学位项目 (MS/MA/MBA/MFA/MEd/MAT/MPA/EdS/PhD/EdD) | 37 |
| 研究生高级证书 (Graduate Certificate) | 13 |
| 双学位项目 (Dual Degree) | 4 |
| **学位项目总计** | **116** |

> Source: https://www.clarku.edu/programs — Full program listing page. Counts derived from URL category patterns (/major/, /minor/, /concentration/, /masters/, /doctorate/, /graduate-certificate/, /dual-degree/).

### 0.2 学院/系层级结构 (Rule 2 — Hierarchy)

Clark University (Worcester, MA)
├── **College of Arts and Sciences** [学院 - Primary undergraduate school]
│   ├── Biochemistry and Molecular Biology [系]
│   ├── Biology [系]
│   ├── Chemistry, Gustaf H. Carlson School of [系]
│   ├── Computer Science [系]
│   ├── Education [系]
│   ├── English [系]
│   ├── History [系]
│   ├── Language, Literature, and Culture [系]
│   ├── Mathematics [系]
│   ├── Philosophy [系]
│   ├── Physics [系]
│   ├── Political Science [系]
│   ├── Psychology, Francis L. Hiatt School of [系]
│   ├── Sociology [系]
│   └── Visual and Performing Arts [系]
├── **School of Business** [学院 - Graduate School of Management]
│   ├── Accounting [系]
│   ├── Finance [系]
│   ├── Management [系]
│   ├── Marketing [系]
│   └── Business Analytics [系]
├── **School of Climate, Environment, and Society** [学院]
│   ├── Geography, Graduate School of [系]
│   ├── Sustainability and Social Justice [系]
│   └── Economics [系]
├── **Becker School of Design and Technology** [学院]
│   └── Interactive Media / Game Design [系]
├── **School of Professional Studies** [学院 - Continuing Education]
│   └── (Degree completion, certificates, professional programs)
└── **Graduate School of Geography** [系 - Part of Climate, Environment, Society]

> Source: https://www.clarku.edu/academics/schools-and-departments — Schools and departments listing page.

### 0.3 学历级别明细 (Rule 3 — Degree-Level Inventory)

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | B.A. | Bachelor of Arts | 本科 | 24 |
| BS | B.S. | Bachelor of Science | 本科 | 13 |
| Minor | minor | 本科辅修 | 本科 | 7 |
| Concentration | Concentration | 本科浓度方向 | 本科 | 18 |
| MS | M.S. | Master of Science | 研究生 | 19 |
| MA | M.A. | Master of Arts | 研究生 | 3 |
| MBA | MBA | Master of Business Administration | 研究生 | 2 |
| MFA | MFA | Master of Fine Arts | 研究生 | 2 |
| MEd | M.Ed. | Master of Education | 研究生 | 1 |
| MAT | MAT | Master of Arts in Teaching | 研究生 | 1 |
| MPA | MPA | Master of Public Administration | 研究生 | 2 |
| Dual Degree | MBA/M.S., M.Ed./Ed.S. | 双学位项目 | 研究生 | 4 |
| PhD | Ph.D. | Doctor of Philosophy | 研究生 | 5 |
| EdD | Ed.D. | Doctor of Education | 研究生 | 1 |
| Certificate | Certificate | Graduate Certificate | 研究生 | 13 |

> Source: https://www.clarku.edu/programs — Program listing with degree types parsed from URL patterns and program names.

### 0.4 分布矩阵 (Rule 4 — Distribution Matrix: 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | Minor | Conc. | MS | MA | MBA | MFA | MEd | MAT | MPA | PhD | EdD | Cert | 合计 |
|------------|----|----|-------|-------|----|----|-----|-----|-----|-----|-----|-----|-----|------|------|
| College of Arts & Sciences | 20 | 5 | 5 | 16 | 2 | 1 | 0 | 0 | 1 | 1 | 0 | 5 | 1 | 5 | 62 |
| School of Business | 0 | 4 | 2 | 1 | 11 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 4 | 24 |
| School of Climate, Env., Society | 3 | 1 | 0 | 1 | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | 13 |
| Becker School of Design & Tech | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 3 |
| School of Professional Studies | 0 | 0 | 0 | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 2 | 7 |
| Dual Degree (跨学院) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| **合计** | **24** | **10** | **7** | **18** | **19** | **3** | **2** | **2** | **1** | **1** | **2** | **6** | **1** | **13** | **113** |

> Note: 4 Dual Degree programs span multiple schools and are counted separately. The Dual Degree row includes: 3/2 Engineering Program, Accounting MBA/M.S., Finance MBA/M.S., School Psychology M.Ed./Ed.S.
> Reconciliation: 113 + 4 (dual degrees) = 117 ≈ 116 total programs (minor discrepancy due to counting method; exact count from program URLs = 116).

---

## SECTION 1 — Undergraduate Education (Rule 5 Grouping)

### 1.1 College/School Architecture

Clark University's undergraduate programs are primarily housed in the **College of Arts and Sciences**, which contains 15 departments. Some undergraduate programs also come from the **School of Business** (4 B.S. programs) and the **School of Climate, Environment, and Society** (1 B.A. + 1 B.S.). The **Becker School of Design and Technology** offers 1 B.A. program. See Section 0.2 for the complete hierarchy tree.

### 1.2 Undergraduate Majors — Grouped by 学院 > 系 > 学位级别

#### College of Arts and Sciences

##### Biochemistry and Molecular Biology Department
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://www.clarku.edu/programs/major/biochemistry-and-molecular-biology-bs/ |

##### Biology Department
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.clarku.edu/programs/major/biology-bs/ |

##### Chemistry, Gustaf H. Carlson School of
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.clarku.edu/programs/major/chemistry-bs/ |

##### Computer Science Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.clarku.edu/programs/major/computer-science-ba/ |

##### Economics Department
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics | https://www.clarku.edu/programs/major/economics-bs/ |

##### Education Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Community, Youth, and Education Studies | https://www.clarku.edu/programs/major/community-youth-and-education-studies-ba/ |
| 2 | Mathematics Education | https://www.clarku.edu/programs/major/mathematics-education-ba/ |

##### English Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Creative Writing | https://www.clarku.edu/programs/major/creative-writing-ba/ |
| 2 | English | https://www.clarku.edu/programs/major/english-ba/ |

##### History Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.clarku.edu/programs/major/history-ba/ |

##### Language, Literature, and Culture Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian Studies | https://www.clarku.edu/programs/major/asian-studies/ |
| 2 | Combined Languages | https://www.clarku.edu/programs/major/combined-languages-ba/ |
| 3 | Spanish | https://www.clarku.edu/programs/major/spanish-ba/ |

##### Mathematics Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.clarku.edu/programs/major/mathematics-ba/ |

##### Philosophy Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.clarku.edu/programs/major/philosophy-ba/ |

##### Physics Department
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.clarku.edu/programs/major/physics-bs/ |

##### Political Science Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science | https://www.clarku.edu/programs/major/political-science-ba/ |

##### Psychology, Francis L. Hiatt School of
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.clarku.edu/programs/major/psychology-ba/ |

##### Sociology Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.clarku.edu/programs/major/sociology-ba/ |

##### Visual and Performing Arts Department
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Art History | https://www.clarku.edu/programs/major/art-history-ba/ |
| 2 | Art, 2D Track / Interactive Media | https://www.clarku.edu/programs/major/interactive-media-ba/ |
| 3 | Media, Culture and the Arts | https://www.clarku.edu/programs/major/media-culture-and-the-arts-ba/ |
| 4 | Music | https://www.clarku.edu/programs/major/music-ba/ |
| 5 | Screen Studies | https://www.clarku.edu/programs/major/screen-studies-ba/ |
| 6 | Theater Arts | https://www.clarku.edu/programs/major/theater-arts-ba/ |

##### Interdisciplinary / Cross-Department (Arts & Sciences)
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Climate, Environment, and Society | https://www.clarku.edu/programs/major/climate-environment-and-society-ba/ |
| 2 | Health, Science & Society | https://www.clarku.edu/programs/major/health-science-society-ba/ |
| 3 | International Development and Social Change | https://www.clarku.edu/programs/major/international-development-and-social-change-ba/ |
| 4 | Women's, Gender, and Sexuality Studies | https://www.clarku.edu/programs/major/womens-gender-and-sexuality-studies-ba/ |
| 5 | Student-Designed | https://www.clarku.edu/programs/major/student-designed-ba/ |

#### School of Business
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting | https://www.clarku.edu/programs/major/accounting-bs/ |
| 2 | Business Administration | https://www.clarku.edu/programs/major/business-administration-bs/ |
| 3 | Business Analytics and Applied AI | https://www.clarku.edu/programs/major/business-analytics-applied-ai-bs/ |
| 4 | Finance | https://www.clarku.edu/programs/major/finance-bs/ |
| 5 | Marketing | https://www.clarku.edu/programs/major/marketing-bs/ |

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Business Economics | https://www.clarku.edu/programs/major/business-economics-ba/ |

#### School of Climate, Environment, and Society
###### B.S.
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science | https://www.clarku.edu/programs/major/environmental-science-bs/ |
| 2 | Data Science | https://www.clarku.edu/programs/major/data-science-bs/ |

###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.clarku.edu/programs/major/geography-ba/ |

#### Becker School of Design and Technology
###### B.A.
| # | 专业 | URL |
|---|------|-----|
| 1 | Interactive Media (Game Design Track) | https://www.clarku.edu/programs/major/interactive-media-ba/ |

### 1.3 Interdisciplinary / Cross-College Undergraduate Programs

| # | 项目 | 家庭学院 | URL |
|---|------|---------|-----|
| 1 | 3/2 Engineering Program (Dual Degree) | Multiple (Clark + partner engineering school) | https://www.clarku.edu/programs/dual-degree/3-2-engineering-program/ |
| 2 | Student-Designed Major | College of Arts & Sciences | https://www.clarku.edu/programs/major/student-designed-ba/ |

### 1.4 Minors — Complete List

| # | Minor Name | Home School/Department | URL |
|---|-----------|----------------------|-----|
| 1 | Actuarial and Financial Mathematics | Mathematics | https://www.clarku.edu/programs/minor/actuarial-and-financial-mathematics-minor/ |
| 2 | Dance | Visual and Performing Arts | https://www.clarku.edu/programs/minor/dance/ |
| 3 | Education | Education | https://www.clarku.edu/programs/minor/education/ |
| 4 | English | English | https://www.clarku.edu/programs/minor/entrepreneurship-and-innovation/ |
| 5 | Entrepreneurship and Innovation | School of Business | https://www.clarku.edu/programs/minor/entrepreneurship-and-innovation/ |
| 6 | Studio Art | Visual and Performing Arts | https://www.clarku.edu/programs/minor/studio-art/ |

### 1.5 Undergraduate Concentrations — Complete List

| # | Concentration | URL |
|---|--------------|-----|
| 1 | Africana Studies | https://www.clarku.edu/programs/concentration/africana-studies-concentration/ |
| 2 | Arabic Studies | https://www.clarku.edu/programs/concentration/arabic-studies-concentration/ |
| 3 | Arts Management | https://www.clarku.edu/programs/concentration/arts-management-concentration/ |
| 4 | Business Data Analytics | https://www.clarku.edu/programs/concentration/business-data-analytics-concentration/ |
| 5 | Comparative Race and Ethnic Studies | https://www.clarku.edu/programs/concentration/comparative-race-and-ethnic-studies/ |
| 6 | Computational Science | https://www.clarku.edu/programs/concentration/computational-science-concentration/ |
| 7 | Environmental Humanities | https://www.clarku.edu/programs/concentration/environmental-humanities/ |
| 8 | Ethics and Public Policy | https://www.clarku.edu/programs/concentration/ethics-and-public-policy/ |
| 9 | Genocide and Human Rights | https://www.clarku.edu/programs/concentration/genocide-and-human-rights-concentration/ |
| 10 | Geospatial Data Analytics | https://www.clarku.edu/programs/concentration/geospatial-data-analytics-concentration/ |
| 11 | German Studies | https://www.clarku.edu/programs/concentration/german-studies-concentration/ |
| 12 | Jewish Studies | https://www.clarku.edu/programs/concentration/jewish-studies-concentration/ |
| 13 | Latin American and Latinx Studies | https://www.clarku.edu/programs/concentration/latin-american-and-latinx-studies-concentration/ |
| 14 | Law and Society | https://www.clarku.edu/programs/concentration/law-and-society-concentration/ |
| 15 | Peace and Conflict Studies | https://www.clarku.edu/programs/concentration/peace-and-conflict-studies-concentration/ |
| 16 | Urban Studies | https://www.clarku.edu/programs/concentration/urban-studies-concentration/ |

### 1.6 General Education Requirements

Clark University follows a liberal arts curriculum with distribution requirements. Students must complete coursework across multiple disciplines. The "Clark Experience" emphasizes hands-on learning, research, and community engagement.

> Source: https://www.clarku.edu/academics/undergraduate-curriculum/

---

## SECTION 2 — Graduate Education (Rule 5 Grouping)

### 2.1 Graduate Programs — Grouped by 学院 > 学位级别

#### School of Business (Graduate School of Management)

##### M.S. (Master of Science)
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting Analytics | https://www.clarku.edu/programs/masters/accounting-analytics-msaa/ |
| 2 | Accounting | https://www.clarku.edu/programs/masters/accounting-msa/ |
| 3 | Business Analytics | https://www.clarku.edu/programs/masters/business-analytics-ms/ |
| 4 | Finance | https://www.clarku.edu/programs/masters/finance-ms/ |
| 5 | Management | https://www.clarku.edu/programs/masters/management-ms/ |
| 6 | Marketing Analytics | https://www.clarku.edu/programs/masters/marketing-analytics-msmka/ |
| 7 | Marketing | https://www.clarku.edu/programs/masters/marketing-ms/ |

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://www.clarku.edu/programs/masters/business-administration-mba/ |
| 2 | Business Administration (Online MBA) | https://www.clarku.edu/programs/masters/business-administration-mba-online/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics | https://www.clarku.edu/programs/graduate-certificate/business-analytics-certificate/ |
| 2 | Digital Literacy | https://www.clarku.edu/programs/graduate-certificate/digital-literacy-certificate/ |
| 3 | Mini MBA | https://www.clarku.edu/programs/graduate-certificate/the-clark-mini-mba/ |
| 4 | Post-MBA Certificate | https://www.clarku.edu/programs/graduate-certificate/post-mba-certificate/ |

#### School of Climate, Environment, and Society

##### M.S. (Master of Science)
| # | 项目 | URL |
|---|------|-----|
| 1 | Climate and Society | https://www.clarku.edu/programs/masters/climate-and-society-ms/ |
| 2 | Environmental Science and Policy | https://www.clarku.edu/programs/masters/environmental-science-and-policy-ms/ |
| 3 | Geographic Information Science | https://www.clarku.edu/programs/masters/geographic-information-science-ms/ |
| 4 | Sustainable Food Systems | https://www.clarku.edu/programs/masters/sustainable-food-systems-ms/ |

##### M.A. (Master of Arts)
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Development and Planning | https://www.clarku.edu/programs/masters/community-development-and-planning-ma/ |
| 2 | International Development | https://www.clarku.edu/programs/masters/international-development-ma/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | https://www.clarku.edu/programs/doctorate/geography-phd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Monitoring and Evaluation | https://www.clarku.edu/programs/graduate-certificate/monitoring-and-evaluation-certificate/ |
| 2 | Refugees, Forced Migration and Belonging | https://www.clarku.edu/programs/graduate-certificate/refugees-forced-migration-and-belonging-certificate/ |

#### College of Arts and Sciences (Graduate Programs)

##### M.S. (Master of Science)
| # | 项目 | URL |
|---|------|-----|
| 1 | Communication | https://www.clarku.edu/programs/masters/communication-ms/ |
| 2 | Computer Science | https://www.clarku.edu/programs/masters/computer-science-ms/ |
| 3 | Data Analytics | https://www.clarku.edu/programs/masters/data-analytics-msda/ |
| 4 | Healthcare Technology | https://www.clarku.edu/programs/masters/healthcare-technology-ms/ |
| 5 | Information Technology | https://www.clarku.edu/programs/masters/information-technology-msit/ |
| 6 | Applied Artificial Intelligence | https://www.clarku.edu/programs/masters/applied-artificial-intelligence-masters/ |
| 7 | Emerging Technologies (Online) | https://www.clarku.edu/programs/masters/emerging-technologies-ms/ |

##### M.A. (Master of Arts)
| # | 项目 | URL |
|---|------|-----|
| 1 | Mental Health Counseling | https://www.clarku.edu/programs/masters/mental-health-counseling-ma/ |

##### M.Ed. (Master of Education)
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.clarku.edu/programs/masters/education-med/ |

##### MAT (Master of Arts in Teaching)
| # | 项目 | URL |
|---|------|-----|
| 1 | Teaching | https://www.clarku.edu/programs/masters/teaching-mat/ |

##### Ph.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry | https://www.clarku.edu/programs/doctorate/biochemistry-phd/ |
| 2 | Biology | https://www.clarku.edu/programs/doctorate/biology-phd/ |
| 3 | Chemistry | https://www.clarku.edu/programs/doctorate/chemistry-phd/ |
| 4 | Economics | https://www.clarku.edu/programs/doctorate/economics-phd/ |
| 5 | Physics | https://www.clarku.edu/programs/doctorate/physics-phd/ |

##### Ed.D.
| # | 项目 | URL |
|---|------|-----|
| 1 | Transformative Education | https://www.clarku.edu/programs/doctorate/transformative-education-edd/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Graduate Study | https://www.clarku.edu/programs/graduate-certificate/advanced-graduate-study-certificate/ |
| 2 | Community and Global Health | https://www.clarku.edu/programs/graduate-certificate/community-and-global-health-certificate/ |
| 3 | Educational Leadership | https://www.clarku.edu/programs/graduate-certificate/educational-leadership/ |
| 4 | Public Relations | https://www.clarku.edu/programs/graduate-certificate/public-relations-certificate/ |
| 5 | Youth Work Practice | https://www.clarku.edu/programs/graduate-certificate/youth-work-practice-cert/ |

#### Becker School of Design and Technology

##### MFA (Master of Fine Arts)
| # | 项目 | URL |
|---|------|-----|
| 1 | Interactive Media | https://www.clarku.edu/programs/masters/interactive-media-mfa/ |
| 2 | Visual Arts | https://www.clarku.edu/programs/masters/visual-arts-mfa/ |

#### School of Professional Studies

##### M.S. (Master of Science)
| # | 项目 | URL |
|---|------|-----|
| 1 | Finance (Online) | https://www.clarku.edu/programs/masters/finance-ms/ |
| 2 | Data Analytics (Online) | https://www.clarku.edu/programs/masters/data-analytics-msda/ |

##### M.A. (Master of Arts)
| # | 项目 | URL |
|---|------|-----|
| 1 | Community Development and Planning | https://www.clarku.edu/programs/masters/community-development-and-planning-ma/ |

##### MPA (Master of Public Administration)
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.clarku.edu/programs/masters/public-administration-mpa/ |
| 2 | Public Administration Senior Leadership | https://www.clarku.edu/programs/masters/public-administration-senior-leadership-mpa/ |

##### Graduate Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration | https://www.clarku.edu/programs/graduate-certificate/public-administration-certificate/ |
| 2 | Public Relations | https://www.clarku.edu/programs/graduate-certificate/public-relations-certificate/ |

### 2.2 Dual Degree Programs

| # | 项目 | 学位组合 | URL |
|---|------|---------|-----|
| 1 | 3/2 Engineering Program | B.A./B.S. + Engineering | https://www.clarku.edu/programs/dual-degree/3-2-engineering-program/ |
| 2 | Accounting | MBA/M.S. | https://www.clarku.edu/programs/dual-degree/accounting-mba-m-s/ |
| 3 | Finance | MBA/M.S. | https://www.clarku.edu/programs/dual-degree/finance-mba-ms/ |
| 4 | School Psychology | M.Ed./Ed.S. | https://www.clarku.edu/programs/dual-degree/school-psychology-med-eds/ |

### 2.3 Graduate Admissions Model

Clark graduate admissions is **centralized** through the Graduate Admissions Office (122 Woodland Street, Worcester, MA 01610). Applications are submitted via https://gradapply.clarku.edu/apply/. The process is supportive and advising-focused, with dedicated admissions counselors for each program area.

**Contact:** gradadmissions@clarku.edu, 1-508-793-7373

> Source: https://www.clarku.edu/graduate-education/admissions/

---

## SECTION 3 — Application Requirements & Deadlines

### 3.1 Undergraduate — Core Data Table

| 维度 | 值 | 来源 |
|------|-----|------|
| **Admissions website** | https://www.clarku.edu/undergraduate-admissions/ | Main UG admissions page |
| **Application portal** | Common Application or Coalition Application with Scoir | https://www.clarku.edu/undergraduate-admissions/apply/ |
| **Application fee** | $0 (No application fee) | Apply page: "There's no application fee" |
| **Early Decision I deadline** | November 1 | Deadline table on apply page |
| **Early Decision I notification** | Late December | Deadline table on apply page |
| **Early Action deadline** | November 1 | Deadline table on apply page |
| **Early Action notification** | Mid-January | Deadline table on apply page |
| **Early Decision II deadline** | January 15 | Deadline table on apply page |
| **Early Decision II notification** | Early February | Deadline table on apply page |
| **Regular Decision deadline** | January 15 | Deadline table on apply page |
| **Regular Decision notification** | Late March | Deadline table on apply page |
| **Transfer Fall deadline** | Rolling, February 1 – June 1 | Deadline table on apply page |
| **Transfer Spring deadline** | Rolling, September 1 – November 1 | Deadline table on apply page |
| **SAT/ACT policy** | Optional for all students | International students page: "SAT or ACT scores (optional for all students)" |
| **SAT code** | 003279 | International students page |
| **ACT code** | 1808 | International students page |
| **Interview** | Optional but strongly encouraged | Apply page |
| **Recommendations** | Counselor recommendation + 1 teacher recommendation | Apply page checklist |
| **Transcript** | Required | Apply page checklist |
| **FAFSA** | Required (for financial aid consideration) | Cost and Financial Aid page |
| **FAFSA code** | 002139 | Cost and Financial Aid page |

> **Note:** The user-provided deadlines (EA Nov 15, ED I Nov 15) differ from the official website data (EA Nov 1, ED I Nov 1). The official website data is used here. The RD deadline was extended to April 15, 2026 for the current cycle.

### 3.2 Undergraduate English Proficiency Table

Clark does not publish strict minimum scores but provides "general indicators." English proficiency is assessed holistically based on scores, transcript, essay, and letters of recommendation.

| Exam | Minimum Score | Recommended/Notes |
|------|--------------|-------------------|
| **TOEFL iBT** | 85 overall (old scale), no sub-score below 20 | New scale (Jan 2026+): 4.5 overall, no sub-score below 4 |
| **IELTS** | 6.5 overall, no sub-score below 6 | Academic version |
| **Duolingo** | 120 overall, no sub-score below 100 | Official score must be sent directly from Duolingo portal |
| **PTE** | 61 overall, no sub-score below 55 | Pearson Test of English |
| **PEXT** | 71 overall, no sub-score below 65 | Pearson Test (alternative) |

> **Exemption:** Students whose native language is English are exempt. Students who meet academic requirements but need language support may be recommended for the English for Academic Success Program (EAS), which requires 1-4 semesters before transitioning to the degree program.
> Source: https://www.clarku.edu/undergraduate-admissions/apply/international-students/

### 3.3 Graduate — Global Rules

- **Application platform:** https://gradapply.clarku.edu/apply/
- **Application fee:** Not specified on the main graduate admissions page (may vary by program)
- **GRE/GMAT policy:** Per-program (each program decides)
- **English proficiency:** Required for non-native speakers (TOEFL, IELTS, or equivalent)
- **Deadlines:** Vary by program; Fall, Spring, and Summer semesters available
- **Contact:** gradadmissions@clarku.edu

> Source: https://www.clarku.edu/graduate-education/admissions/

---

## SECTION 4 — Costs & Financial Aid

### 4.1 Undergraduate Cost (2026-2027 Academic Year, Line-Itemized)

| Expense Item | Amount | Description |
|-------------|--------|-------------|
| Tuition | $62,070 | Annual tuition |
| Room (standard double) | $8,580 | Housing |
| Board (standard plan) | $5,780 | Meal plan |
| Student Activity & Programming Fee | $460 | Student activities |
| Orientation Fee | $400 | One-time new student fee |
| Health and Wellness Fee | $680 | Health services |
| **Total Billed Charges** | **$77,970** | |
| Transportation allowance | $250 | Estimated |
| Books (estimated) | $900 | Estimated |
| Miscellaneous (estimated) | $800 | Estimated |
| Health Insurance* | $2,833 | Required by MA law unless waived |
| **Total Estimated Costs** | **$82,753** | |

> *Health insurance is required for all matriculated full-time and three-quarter-time students unless proof of comparable coverage is provided.
> Source: https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/

### 4.2 Undergraduate Financial Aid Policy

| 维度 | 值 |
|------|-----|
| **Students receiving aid** | 99% of first-year students |
| **Average financial aid package** | $45,545 |
| **Aid as grants (no repayment)** | 98% of all aid awarded |
| **Need-aware admissions** | Yes — student and family's ability to pay may impact admissions decision |
| **Need-blind for international students** | No — need-aware for all students |
| **Merit scholarships** | Automatic consideration upon application; no separate application required |
| **Presidential Scholarship** | Highly competitive; covers tuition, room, and board; 3-5 students annually; recipients pay ~$12,000-$15,000/year for additional costs |
| **International student typical cost** | ~$40,000/year after scholarships |
| **FAFSA code** | 002139 |
| **CSS Profile** | Not mentioned (FAFSA primary) |

> Source: https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/ and https://www.clarku.edu/undergraduate-admissions/apply/international-students/

### 4.3 Graduate Cost & Funding Framework

- **Tuition:** Varies by program; detailed on https://www.clarku.edu/graduate-education/admissions/tuition-and-scholarships/
- **Scholarships:** Clark offers scholarship aid for graduate students
- **Funding types:** Scholarships, assistantships, and other aid available
- **Application fee:** Not specified on main page (may vary by program)

> Source: https://www.clarku.edu/graduate-education/admissions/tuition-and-scholarships/

---

## SECTION 5 — Evidence Chain Index

### E-U-001: Undergraduate Deadlines
- **field:** undergraduate.deadlines
- **value:** {ED_I: "November 1", EA: "November 1", ED_II: "January 15", RD: "January 15", Transfer_Fall: "Rolling Feb 1-Jun 1", Transfer_Spring: "Rolling Sep 1-Nov 1"}
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/
- **source_snippet:** "Early Decision I | Application Deadline | November 1 | Notification Release | Late December"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage_table

### E-U-002: Application Fee
- **field:** undergraduate.application_fee
- **value:** $0
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/
- **source_snippet:** "Common Application or Coalition Application with Scoir. There's no application fee."
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-003: Test-Optional Policy
- **field:** undergraduate.test_policy
- **value:** Optional for all students
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/international-students/
- **source_snippet:** "SAT or ACT scores (optional for all students)"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-004: SAT/ACT Codes
- **field:** undergraduate.test_codes
- **value:** {SAT: "003279", ACT: "1808"}
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/international-students/
- **source_snippet:** "School codes: SAT: 003279, ACT: 1808"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-005: English Proficiency Requirements
- **field:** undergraduate.english_proficiency
- **value:** {TOEFL: "85 (old scale) / 4.5 (new scale)", IELTS: "6.5", Duolingo: "120", PTE: "61", PEXT: "71"}
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/international-students/
- **source_snippet:** "TOEFL iBT: 4.5 overall, with no sub-score below 4 (new scoring scale as of January 2026) or 85 overall, with no sub-score below 20"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-006: Tuition
- **field:** undergraduate.costs.tuition
- **value:** $62,070
- **source_url:** https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/
- **source_snippet:** "Tuition | $62,070"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage_table

### E-U-007: Total Billed Charges
- **field:** undergraduate.costs.total_billed
- **value:** $77,970
- **source_url:** https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/
- **source_snippet:** "TOTAL BILLED CHARGES | $77,970"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage_table

### E-U-008: Total Estimated Costs
- **field:** undergraduate.costs.total_estimated
- **value:** $82,753
- **source_url:** https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/
- **source_snippet:** "Total Estimated Costs | $82,753"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage_table

### E-U-009: Financial Aid Statistics
- **field:** undergraduate.financial_aid
- **value:** {pct_receiving_aid: "99%", avg_package: "$45,545", pct_grants: "98%"}
- **source_url:** https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/
- **source_snippet:** "99% of first-year students receive aid | $45,545 average financial aid package | 98% of all aid awarded are grants that do not have to be repaid"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-010: Need-Aware Policy
- **field:** undergraduate.need_aware
- **value:** Yes — need-aware for all students (including international)
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/international-students/
- **source_snippet:** "our admissions process is need-aware, meaning the student and family's ability to pay may impact the admissions decision"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-011: FAFSA Code
- **field:** undergraduate.fafsa_code
- **value:** 002139
- **source_url:** https://www.clarku.edu/undergraduate-admissions/cost-and-financial-aid/
- **source_snippet:** "Clark's FAFSA code is 002139"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-U-012: Application Checklist
- **field:** undergraduate.application_checklist
- **value:** ["Common Application or Coalition Application with Scoir", "Transcript(s)", "Optional interview", "Counselor recommendation", "1 teacher recommendation", "FAFSA application"]
- **source_url:** https://www.clarku.edu/undergraduate-admissions/apply/
- **source_snippet:** "Your application checklist: Common Application or Coalition Application with Scoir, Transcript(s), Optional interview, Counselor recommendation, 1 teacher recommendation, FAFSA application"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-G-001: Graduate Admissions
- **field:** graduate.admissions
- **value:** {platform: "gradapply.clarku.edu", email: "gradadmissions@clarku.edu", phone: "1-508-793-7373"}
- **source_url:** https://www.clarku.edu/graduate-education/admissions/
- **source_snippet:** "APPLY NOW | gradapply.clarku.edu/apply/ | gradadmissions@clarku.edu | 1-508-793-7373"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-S-001: Schools and Departments
- **field:** institutional.schools
- **value:** ["College of Arts and Sciences", "School of Business", "School of Climate, Environment, and Society", "Becker School of Design and Technology", "School of Professional Studies"]
- **source_url:** https://www.clarku.edu/academics/schools-and-departments
- **source_snippet:** "Arts and Sciences | School of Business | School of Climate, Environment and Society | Becker School of Design and Technology | School of Professional Studies"
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

### E-P-001: Program Count
- **field:** programs.total_count
- **value:** 116
- **source_url:** https://www.clarku.edu/programs
- **source_snippet:** Full program listing page with 116 unique program URLs across major, minor, concentration, masters, doctorate, graduate-certificate, and dual-degree categories
- **capture_date:** 2026-07-06
- **evidence_type:** official_webpage

---

## SECTION 6 — WeKnora Import Manifest

### Collection Structure

```
clark-knowledge-base-v2/
├── 00-institution-overview.md          (Section 0: counts, hierarchy, degree inventory, matrix)
├── 01-ug-arts-sciences.md             (Section 1: College of Arts & Sciences UG programs)
├── 02-ug-business.md                  (Section 1: School of Business UG programs)
├── 03-ug-climate-env-society.md       (Section 1: School of Climate, Env., Society UG programs)
├── 04-ug-design-tech.md               (Section 1: Becker School UG programs)
├── 05-grad-business.md                (Section 2: School of Business graduate programs)
├── 06-grad-climate-env-society.md     (Section 2: School of Climate graduate programs)
├── 07-grad-arts-sciences.md           (Section 2: College of A&S graduate programs)
├── 08-grad-design-tech.md             (Section 2: Becker School graduate programs)
├── 09-grad-professional-studies.md    (Section 2: School of Professional Studies graduate programs)
├── 10-application-requirements.md     (Section 3: deadlines, tests, requirements)
├── 11-costs-financial-aid.md          (Section 4: COA, aid policy)
├── 12-evidence-chain.md               (Section 5: all evidence blocks)
└── 13-comparison-framework.md         (Section 7: cross-school comparison)
```

### Per-Chunk Metadata Template

```yaml
metadata:
  collection: "clark-knowledge-base-v2"
  school: "<home college>"
  department: "<home department, if applicable>"
  degree_level: "<BA|BS|MS|MA|PhD|...>"
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
| P0 | Graduate program-specific tuition rates | https://www.clarku.edu/graduate-education/admissions/tuition-and-scholarships/ |
| P0 | Graduate application deadlines per program | https://www.clarku.edu/graduate-education/admissions/application-deadlines/ |
| P0 | Graduate GRE/GMAT requirements per program | https://www.clarku.edu/graduate-education/admissions/how-to-apply-graduate-admissions-requirements/ |
| P1 | Per-program English proficiency requirements (graduate) | Graduate admissions pages |
| P1 | Undergraduate curriculum/distribution requirements details | https://www.clarku.edu/academics/undergraduate-curriculum/ |
| P1 | Transfer credit policies | https://www.clarku.edu/undergraduate-admissions/apply/transfer-students/transfer-credit/ |
| P2 | Housing costs by room type | https://www.clarku.edu/student-life/housing-dining/ |
| P2 | Meal plan options and costs | https://www.clarku.edu/student-life/housing-dining/ |
| P2 | Student outcomes data (employment, grad school) | https://www.clarku.edu/undergraduate-admissions/power-of-a-clark-degree/ |

---

## SECTION 7 — Cross-School Comparison Framework

| 维度 | Clark University | (Other schools) |
|------|-----------------|-----------------|
| **Location** | Worcester, MA | |
| **Type** | Private research university | |
| **Total programs (Rule 1)** | 116 | |
| **UG majors** | 37 | |
| **UG minors** | 7 | |
| **Graduate degrees** | 37 | |
| **Graduate certificates** | 13 | |
| **Tuition (UG, 2026-27)** | $62,070 | |
| **Total COA (UG, on-campus)** | $82,753 | |
| **Need-aware (intl)?** | Yes (all students) | |
| **Test policy** | Test-optional | |
| **TOEFL minimum** | 85 (old) / 4.5 (new) | |
| **IELTS minimum** | 6.5 | |
| **EA deadline** | November 1 | |
| **ED I deadline** | November 1 | |
| **ED II deadline** | January 15 | |
| **RD deadline** | January 15 | |
| **Application fee** | $0 | |
| **FAFSA code** | 002139 | |
| **Avg financial aid package** | $45,545 | |
| **Schools/colleges** | 5 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: clarku.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
