# University of Pennsylvania Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-05
> **Capture tool**: ego-browser (Chromium headless) + serverFetch
> **Target knowledge base**: WeKnora
> **Granularity**: school → degree-level → program (Penn catalog lists programs directly under their home school; department-level grouping is captured where the program name encodes it)
> **Document version**: v2.0 (deep)
> **University**: University of Pennsylvania (UPenn) — Ivy League, Philadelphia, PA

---

## The five structural rules (enforced)

1. **专业总数** — 641 catalog program rows = 202 UG majors + 101 UG minors + 16 UG certificates/post-bacc prep + 264 graduate degrees + 53 graduate certificates/certifications + 5 graduate minors. Degree-granting programs only (UG majors + grad degrees) = **466**.
2. **学院/系明细 + 父子层级** — 4 undergraduate-degree-granting schools (College of Arts & Sciences / Penn Engineering / Wharton / Penn Nursing) + 12 graduate/professional schools (SAS Graduate Division, SEAS, Wharton, Nursing, Perelman SOM, Penn GSE, Weitzman Design, Penn Carey Law, Dental, Vet, SP2, Annenberg).
3. **学历级别明细** — 76 distinct canonical degree designations (BA/BS/BSE/BAS/BAAS/BSN/BFA at UG; MA/MS/MFA/MBA/MSE/MSEd/MSN/MSD/MPA/MPhil/MArch/MLA/MCP/MEng-family/PhD/EdD/DNP/ScD/DMD/MD/VMD/JD/LLM/SJD/DSW + certificates).
4. **分布矩阵** — 学院 × canonical 学位级别 (below)
5. **全量专业明细按 学院 > 学位级别 分组** — every program listed under its school → degree level (641 rows)

> **Reconciliation gate (PASSED):** Rule-1 total (641) == sum of matrix cells (641) == count of Rule-5 rows (641) == sum of degree-inventory counts (641).

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BSE/BAS/BAAS/BSN/BFA) | 202 |
| 本科辅修 (Minor) | 101 |
| 本科证书 + Post-Bacc 预备项目 | 16 |
| 研究生学位项目 (MA/MS/MBA/MSE/MSEd/MSN/PhD/EdD/DNP/MD/DMD/VMD/JD/…) | 264 |
| 研究生高级证书 / 资格认证 (Certificate / Certification) | 53 |
| 研究生辅修 (Graduate Minor) | 5 |
| **学位项目总计 (UG majors + GRAD degrees)** | **466** |
| **目录条目总计 (含 minors/certs/prep)** | **641** |
| 本科可授学位学院 (undergraduate schools) | 4 |
| 研究生 / 专业学院 (graduate/professional schools) | 12 |

> Counts derived from `catalog.upenn.edu/programs/` (Penn's unified 2026-27 catalog, captured 2026-07-05). The catalog is a single static page listing all 641 program-degree rows; school attribution is encoded in each program's link text. Coordinated dual-degree programs (Huntsman / LSM / M&T / NHCM / VIPER / VIC) are listed separately on the admissions site (Section 1.3) and grant degrees from two schools — they are NOT double-counted in the 641.

### 0.2 学院 / 系层级结构 (Rule 2)

```
University of Pennsylvania  (Ivy League, founded 1740, Philadelphia)
├── [4 本科学院 — undergraduate-degree-granting]
│   ├── College of Arts and Sciences (within School of Arts & Sciences)  [学院]  152 BA majors + 1 BFA + 9 BAAS + 86 minors + 14 UG certs + 2 prep
│   │   └── (College of Liberal & Professional Studies / LPS hosts the BAAS adult-degree and UG certificates)
│   ├── School of Engineering and Applied Science (Penn Engineering / SEAS)  [学院]  10 BSE + 2 BAS + 9 minors
│   ├── The Wharton School                                                 [学院]  26 BS majors (concentrations)
│   ├── School of Nursing                                                  [学院]  2 BSN + 5 minors
│   └── Stuart Weitzman School of Design (UG: minor only)                  [学院]  1 Design minor
├── [12 研究生 / 专业学院]
│   ├── School of Arts & Sciences — Graduate Division                      [学院]  80 grad programs (43 PhD + 15 MA + 6 MPA + 3 MPhil + MS/MES/MCS/...)
│   ├── School of Engineering and Applied Science (Grad)                   [学院]  35 grad (17 MSE + 6 PhD + 8 certs + MCIT/MASCS/MIPD/MBIOT)
│   ├── The Wharton School (Grad)                                          [学院]  35 grad (23 MBA + 9 PhD + MSQF/MA + cert)
│   ├── School of Nursing (Grad)                                           [学院]  28 grad (12 MSN + 3 DNP + PhD + MPN + MSNS + certs/minors)
│   ├── Perelman School of Medicine (PSOM)                                 [学院]  41 grad (13 PhD + 12 certs + MD + MS + MCIT/MSGC/MPH/...)
│   │   └── Biomedical Graduate Studies (BGS) administers PSOM PhDs
│   ├── Graduate School of Education (Penn GSE)                            [学院]  44 grad (22 MSEd + 9 PhD + 8 EdD + 3 certifications + 2 MPhil)
│   ├── Stuart Weitzman School of Design (Grad)                            [学院]  25 grad (5 MSD + 2 PhD + 2 MLA + MArch/MCP/MUSA/MFA/MSHP/MS/MEBD + 10 certs)
│   ├── Penn Carey Law School                                              [学院]  5 grad (JD + 2 LLM + ML + SJD)
│   ├── School of Dental Medicine                                          [学院]  16 grad (DMD + DScD + MADS + MSOPH/MSOB/MOHS + 9 certs)
│   ├── School of Veterinary Medicine (Penn Vet)                           [学院]  4 grad (VMD + MSAWB + 2 certs)
│   ├── School of Social Policy & Practice (SP2)                           [学院]  7 grad (2 MSSP + DNP/MSNPL/PhD/DSW/MSW)
│   └── Annenberg School for Communication                                 [学院]  2 grad (PhD + MCMI)
└── (Coordinated dual-degree / specialized programs — see §1.3)
    ├── Huntsman (SAS BA + Wharton BS)
    ├── LSM (SAS BA + Wharton BS)
    ├── M&T (Wharton BS + SEAS BSE/BAS)
    ├── NHCM (Nursing BSN + Wharton BS)
    └── VIPER (SAS BA + SEAS BSE)
```

> Penn is unusual among Ivies in having **professional bachelor's variants** (BSE = Bachelor of Science in Engineering; BAS = Bachelor of Applied Science; BAAS = Bachelor of Applied Arts and Sciences via LPS) alongside the standard BA/BS. The College of Arts and Sciences sits **inside** the larger School of Arts & Sciences (which also houses the Graduate Division and LPS). Wharton's "majors" are formally **concentrations** within the single BS in Economics degree.

### 0.3 学历级别明细 (Rule 3)

> **学位规范化（强制）**：Rule 3 与 Rule 4 用 [degree-taxonomy.md](degree-taxonomy.md) 里的 **canonical（规范）** 缩写聚合，同时保留学校 official 缩写（Penn 用标准缩写，无拉丁文）。Penn 专有：BSE/BAS/BAAS/VMD/DMD/DScD 单列。

| canonical | official (本校) | 全称 | 类别 | 层级 | 数量 |
|-----------|----------------|------|------|------|------|
| BA | BA | Bachelor of Arts | bachelor | undergraduate | 152 |
| Minor | MINOR | Minor | minor | graduate/undergraduate | 106 |
| PhD | PHD | Doctor of Philosophy | doctor | graduate | 85 |
| Certificate | CERTIFICATE | Undergraduate Certificate | undergrad_cert | graduate/undergraduate | 64 |
| BS | BS | Bachelor of Science | bachelor | undergraduate | 26 |
| MBA | MBA | Master of Business Administration | master | graduate | 23 |
| MEd | MSED | Master of Science in Education | master | graduate | 22 |
| MSE | MSE | Master of Science in Engineering | master | graduate | 17 |
| MA | MA | Master of Arts | master | graduate | 16 |
| MSN | MSN | Master of Science in Nursing | master | graduate | 12 |
| BSE | BSE | Bachelor of Science in Engineering | bachelor | undergraduate | 10 |
| BAAS | BAAS | Bachelor of Applied Arts and Sciences | bachelor | undergraduate | 9 |
| EdD | EDD | Doctor of Education | doctor | graduate | 8 |
| MPA | MPA/MPAF | Master of Public Administration | master | graduate | 6 |
| MSD | MSD | Master of Science in Design | master | graduate | 5 |
| MPhil | MPHIL/MPHILED | Master of Philosophy | master | graduate | 5 |
| DNP | DNP/DNPA | Doctor of Nursing Practice | doctor | graduate | 4 |
| MS | MS | Master of Science | master | graduate | 3 |
| Certification | CERTIFICATION | Graduate Certification | grad_cert | graduate | 3 |
| BAS | BAS | Bachelor of Applied Science | bachelor | undergraduate | 2 |
| DMD | DMD | Doctor of Dental Medicine | doctor | graduate | 2 |
| MSHP | MSHP | Master of Science in Historic Preservation | master | graduate | 2 |
| MLA | MLA | Master of Landscape Architecture | master | graduate | 2 |
| LLM | LLCM/LLM | LL.M. in Corporation Law | doctor | graduate | 2 |
| BSN | BSN | Bachelor of Science in Nursing | bachelor | undergraduate | 2 |
| Prep | PREP | Post-Baccalaureate Preparatory Program | postbacc | undergraduate | 2 |
| MSSP | MSSP | Master of Science in Social Policy | master | graduate | 2 |
| MADS | MADS | Master of Advanced Dental Studies | master | graduate | 1 |
| MSAWB | MSAWB | Master of Science in Animal Welfare and Behavior | master | graduate | 1 |
| MCPL | MCPL | Master of Chemistry Prep Laboratory | master | graduate | 1 |
| MEDS | MEDS | Master of Education Statistics | master | graduate | 1 |
| MSAG | MSAG | Master of Science in Applied Geosciences | master | graduate | 1 |
| MAPP | MAPP | Master of Applied Positive Psychology | master | graduate | 1 |
| MArch | MARCH | Master of Architecture | master | graduate | 1 |
| MEBD | MEBD | Master of Environmental Building Design | master | graduate | 1 |
| MBDS | MBDS | Master of Biomedical Sciences | master | graduate | 1 |
| MBE | MBE | Master of Bioethics | master | graduate | 1 |
| MSBMI | MSBMI | Master of Science in Biomedical Informatics | master | graduate | 1 |
| MBIOT | MBIOT | Master of Biotechnology | master | graduate | 1 |
| MCS | MCS | Master of Computer and Information Science | master | graduate | 1 |
| MCP | MCP | Master of City Planning | master | graduate | 1 |
| MSCE | MSCE | Master of Science in Civil Engineering | master | graduate | 1 |
| MCI | MCI | Master of City Planning ( Innovation) | master | graduate | 1 |
| MCMI | MCMI | Master of Medical Informatics | master | graduate | 1 |
| MCIT | MCIT | Master of Computer and Information Technology | master | graduate | 1 |
| MASCS | MASCS | Master of Applied Science in Clinical Science | master | graduate | 1 |
| MD | MD | Doctor of Medicine | doctor | graduate | 1 |
| ScD | DSCD | Doctor of Science in Dentistry | doctor | graduate | 1 |
| MES | MES | Master of Environmental Studies | master | graduate | 1 |
| BFA | BFA | Bachelor of Fine Arts | bachelor | undergraduate | 1 |
| MFA | MFA | Master of Fine Arts | master | graduate | 1 |
| MSGC | MSGC | Master of Science in Genetic Counseling | master | graduate | 1 |
| MHCI | MHCI | Master of Science in Human-Centered Interaction | master | graduate | 1 |
| MHQS | MHQS | Master of Health Quality and Safety | master | graduate | 1 |
| MIPD | MIPD | Master of Integrated Product Design | master | graduate | 1 |
| JD | JD | Juris Doctor | doctor | graduate | 1 |
| ML | ML | Master in Law | master | graduate | 1 |
| SJD | SJD | Doctor of Juridical Science | doctor | graduate | 1 |
| MSME | MSME | Master of Science in Mechanical Engineering | master | graduate | 1 |
| MMP | MMP | Master of Medical Physics | master | graduate | 1 |
| MSNPL | MSNPL | Master of Science in Nursing Leadership | master | graduate | 1 |
| MPN | MPN | Master of Plant Neuroscience | master | graduate | 1 |
| MSNS | MSNS | Master of Science in Nutrition Science | master | graduate | 1 |
| MSOPH | MSOPH | Master of Science in Oral and Population Health | master | graduate | 1 |
| MSOB | MSOB | Master of Science in Oral Biology | master | graduate | 1 |
| MOHS | MOHS | Master of Oral Health Sciences | master | graduate | 1 |
| MSOD | MSOD | Master of Science in Organizational Dynamics | master | graduate | 1 |
| MPH | MPH | Master of Public Health | master | graduate | 1 |
| MSQF | MSQF | Master of Quantitative Finance | master | graduate | 1 |
| MRA | MRA | Master of Resource and Applied Economics | master | graduate | 1 |
| MSRS | MSRS | Master of Science in Radiological Science | master | graduate | 1 |
| DSW | DSW | Doctor of Social Work | doctor | graduate | 1 |
| MSW | MSW | MSW | other | graduate | 1 |
| MSTR | MSTR | Master of Science in Translational Research | master | graduate | 1 |
| MUSA | MUSA | Master of Urban Spatial Analytics | master | graduate | 1 |
| VMD | VMD | Doctor of Veterinary Medicine | doctor | graduate | 1 |

> Total inventory count = 641 = Rule-1 catalog rows. ✓

### 0.4 分布矩阵 (Rule 4 — 学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BSE | BAS | BAAS | BSN | BFA | Minor | Certificate | Prep | MA | MS | MFA | MBA | MSE | MEd | MSN | MSD | MPA | MPhil | MArch | MLA | MCP | PhD | EdD | DNP | ScD | DMD | MD | VMD | JD | LLM | SJD | DSW | Certification | Other | 合计 |
|---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---||---|
| The Wharton School | - | 26 | - | - | - | - | - | - | 1 | - | 1 | - | - | 23 | - | - | - | - | - | - | - | - | - | 9 | - | - | - | - | - | - | - | - | - | - | - | 1 | **61** |
| School of Nursing | - | - | - | - | - | 2 | - | 10 | 5 | - | - | - | - | - | - | - | 12 | - | - | - | - | - | - | 1 | - | 3 | - | - | - | - | - | - | - | - | - | 2 | **35** |
| School of Dental Medicine | - | - | - | - | - | - | - | - | 9 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | 2 | - | - | - | - | - | - | - | 4 | **16** |
| Perelman School of Medicine | - | - | - | - | - | - | - | - | 12 | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - | 13 | - | - | - | - | 1 | - | - | - | - | - | - | 14 | **41** |
| School of Engineering and Applied Science | - | - | 10 | 2 | - | - | - | 9 | 8 | - | - | - | - | - | 17 | - | - | - | - | - | - | - | - | 6 | - | - | - | - | - | - | - | - | - | - | - | 4 | **56** |
| School of Arts & Sciences | 152 | - | - | - | 9 | - | 1 | 86 | 17 | 2 | 15 | 1 | - | - | - | - | - | - | 6 | 3 | - | 1 | - | 43 | - | - | - | - | - | - | - | - | - | - | - | 8 | **344** |
| School of Veterinary Medicine | - | - | - | - | - | - | - | - | 2 | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | 1 | **4** |
| Stuart Weitzman School of Design | - | - | - | - | - | - | - | 1 | 10 | - | - | 1 | 1 | - | - | - | - | 5 | - | - | 1 | 1 | 1 | 2 | - | - | - | - | - | - | - | - | - | - | - | 3 | **26** |
| Annenberg School for Communication | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | - | - | - | - | - | - | - | - | - | - | 1 | **2** |
| Graduate School of Education | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 22 | - | - | - | 2 | - | - | - | 9 | 8 | - | - | - | - | - | - | - | - | - | 3 | - | **44** |
| Penn Carey Law School | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | 2 | 1 | - | - | 1 | **5** |
| School of Social Policy & Practice | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | 1 | - | 1 | - | - | - | - | - | - | - | 1 | - | 4 | **7** |
| **合计** | **152** | **26** | **10** | **2** | **9** | **2** | **1** | **106** | **64** | **2** | **16** | **3** | **1** | **23** | **17** | **22** | **12** | **5** | **6** | **5** | **1** | **2** | **1** | **85** | **8** | **4** | **1** | **2** | **1** | **1** | **1** | **2** | **1** | **1** | **3** | **43** | **641** |

> Matrix cell-sum = 641 = Rule-1 total. ✓ The "Other" column aggregates ~30 single-instance Penn-specific master's designations (MSE variants, MCIT, MCMI, MBE, etc.) that each appear in only one school — listed in full in Section 2 grouped tables.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College / school architecture

Penn undergraduates apply to **one of four undergraduate schools** (or a coordinated dual-degree program), not to "Penn" in the abstract. All four schools sit on one contiguous Philadelphia campus and students may take courses across all of them. See the full hierarchy at §0.2. Each school grants its own degree: SAS/College grants BA (+ BFA in Fine Arts, + BAAS via LPS); SEAS grants BSE and BAS; Wharton grants BS (in Economics, with named concentrations); Nursing grants BSN.

### 1.2 Undergraduate majors — grouped by 学院 > 学位级别

> Every undergraduate catalog row appears exactly once below (319 UG rows = 202 majors + 101 minors + 16 certificates/prep). URL points to each program's official catalog page.

#### School of Arts & Sciences

##### BA (152)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Africana Studies, BA: African American Studies | BA | https://catalog.upenn.edu/undergraduate/programs/africana-studies-african-american-ba/ |
| 2 | Africana Studies, BA: African Diaspora Studies | BA | https://catalog.upenn.edu/undergraduate/programs/africana-studies-african-diaspora-ba/ |
| 3 | Africana Studies, BA: African Studies | BA | https://catalog.upenn.edu/undergraduate/programs/africana-studies-african-studies-ba/ |
| 4 | Ancient History, BA | BA | https://catalog.upenn.edu/undergraduate/programs/ancient-history-ba/ |
| 5 | Anthropology, BA: Archaeology | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-archaeology-ba/ |
| 6 | Anthropology, BA: Biological Anthropology | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-human-biology-ba/ |
| 7 | Anthropology, BA: Cultural and Linguistic Anthropology | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-cultural-linguistic-anthropology-ba/ |
| 8 | Anthropology, BA: Environmental Anthropology | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-environmental-ba/ |
| 9 | Anthropology, BA: General Anthropology | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-general-anthropology-ba/ |
| 10 | Anthropology, BA: Medical Anthropology & Global Health | BA | https://catalog.upenn.edu/undergraduate/programs/anthropology-medical-anthropology-global-health-ba/ |
| 11 | Architecture, BA: Design | BA | https://catalog.upenn.edu/undergraduate/programs/architecture-design-ba/ |
| 12 | Architecture, BA: Intensive Design | BA | https://catalog.upenn.edu/undergraduate/programs/architecture-design-intensive-ba/ |
| 13 | Biochemistry, BA | BA | https://catalog.upenn.edu/undergraduate/programs/biochemistry-ba/ |
| 14 | Biology, BA | BA | https://catalog.upenn.edu/undergraduate/programs/biology-general-biology-ba/ |
| 15 | Biophysics, BA | BA | https://catalog.upenn.edu/undergraduate/programs/biophysics-ba/ |
| 16 | Chemistry, BA | BA | https://catalog.upenn.edu/undergraduate/programs/chemistry-ba/ |
| 17 | Cinema and Media Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/cinema-media-studies-ba/ |
| 18 | Classical Studies, BA: Classical Civilizations | BA | https://catalog.upenn.edu/undergraduate/programs/classical-studies-classical-civilizations-ba/ |
| 19 | Classical Studies, BA: Classical Languages and Literature | BA | https://catalog.upenn.edu/undergraduate/programs/classical-studies-classical-languages-literature-ba/ |
| 20 | Classical Studies, BA: Mediterranean Archaeology | BA | https://catalog.upenn.edu/undergraduate/programs/classical-studies-mediterranean-archaeology-ba/ |
| 21 | Cognitive Science, BA: Cognitive Neuroscience | BA | https://catalog.upenn.edu/undergraduate/programs/cognitive-science-cognitive-neuroscience-ba/ |
| 22 | Cognitive Science, BA: Computation and Cognition | BA | https://catalog.upenn.edu/undergraduate/programs/cognitive-science-computation-cognition-ba/ |
| 23 | Cognitive Science, BA: Individualized | BA | https://catalog.upenn.edu/undergraduate/programs/cognitive-science-individualized-ba/ |
| 24 | Cognitive Science, BA: Language & Mind | BA | https://catalog.upenn.edu/undergraduate/programs/cognitive-science-language-mind-ba/ |
| 25 | Communication, BA: Communication & Public Service | BA | https://catalog.upenn.edu/undergraduate/programs/communication-public-service-ba/ |
| 26 | Communication, BA: Communication, Culture & Journalism Studies | BA | https://catalog.upenn.edu/undergraduate/programs/communication-communication-culture-journalism-studies-ba/ |
| 27 | Communication, BA: Data & Network Science for Communication | BA | https://catalog.upenn.edu/undergraduate/programs/communication-data-network-science-communication-ba/ |
| 28 | Communication, BA: General Communication | BA | https://catalog.upenn.edu/undergraduate/programs/communication-ba/ |
| 29 | Communication, BA: Media, Audiences & Persuasion | BA | https://catalog.upenn.edu/undergraduate/programs/communication-media-audiences-persuasion-ba/ |
| 30 | Communication, BA: Politics, Policy & Advocacy | BA | https://catalog.upenn.edu/undergraduate/programs/communication-politics-policy-advocacy-ba/ |
| 31 | Comparative Literature, BA: (Trans)national Literatures | BA | https://catalog.upenn.edu/undergraduate/programs/comparative-literature-transnational-literature-ba/ |
| 32 | Comparative Literature, BA: Globalization | BA | https://catalog.upenn.edu/undergraduate/programs/comparative-literature-globalization-ba/ |
| 33 | Comparative Literature, BA: Theory | BA | https://catalog.upenn.edu/undergraduate/programs/comparative-literature-theory-ba/ |
| 34 | Criminology, BA | BA | https://catalog.upenn.edu/undergraduate/programs/criminology-ba/ |
| 35 | Design, BA | BA | https://catalog.upenn.edu/undergraduate/programs/design-ba/ |
| 36 | Earth and Environmental Science, BA | BA | https://catalog.upenn.edu/undergraduate/programs/earth-environmental-science-ba/ |
| 37 | East Asian Languages and Civilizations, BA: Dual Language | BA | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-dual-language-ba/ |
| 38 | East Asian Languages and Civilizations, BA: East Asian Area Studies | BA | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-east-asian-area-studies-ba/ |
| 39 | East Asian Languages and Civilizations, BA: General East Asian Languages and Civilizations | BA | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-ba/ |
| 40 | Economics, BA | BA | https://catalog.upenn.edu/undergraduate/programs/economics-ba/ |
| 41 | English, BA: 18th/19th Centuries | BA | https://catalog.upenn.edu/undergraduate/programs/english-18th-19th-centuries-ba/ |
| 42 | English, BA: 20th/21st Centuries | BA | https://catalog.upenn.edu/undergraduate/programs/english-20th-21st-centuries-ba/ |
| 43 | English, BA: Africana Literatures & Culture | BA | https://catalog.upenn.edu/undergraduate/programs/english-africana-literature-culture-ba/ |
| 44 | English, BA: Cinema & Media Studies | BA | https://catalog.upenn.edu/undergraduate/programs/english-cinema-media-studies-ba/ |
| 45 | English, BA: Creative Writing | BA | https://catalog.upenn.edu/undergraduate/programs/english-creative-writing-ba/ |
| 46 | English, BA: Drama | BA | https://catalog.upenn.edu/undergraduate/programs/english-drama-ba/ |
| 47 | English, BA: Gender/Sexuality | BA | https://catalog.upenn.edu/undergraduate/programs/english-gender-sexuality-ba/ |
| 48 | English, BA: General English | BA | https://catalog.upenn.edu/undergraduate/programs/english-ba/ |
| 49 | English, BA: Literary Theory & Cultural Studies | BA | https://catalog.upenn.edu/undergraduate/programs/english-literary-theory-cultural-studies-ba/ |
| 50 | English, BA: Literature, Journalism and Print Culture | BA | https://catalog.upenn.edu/undergraduate/programs/english-literature-journalism-print-culture-ba/ |
| 51 | English, BA: Medieval/Renaissance | BA | https://catalog.upenn.edu/undergraduate/programs/english-medieval-renaissance-ba/ |
| 52 | English, BA: Poetry and Poetics | BA | https://catalog.upenn.edu/undergraduate/programs/english-poetry-poetics-ba/ |
| 53 | English, BA: The Novel | BA | https://catalog.upenn.edu/undergraduate/programs/english-novel-ba/ |
| 54 | Environmental Studies, BA: Environmental History and Regional Studies | BA | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-history-regional-ba/ |
| 55 | Environmental Studies, BA: Environmental Policy and Application | BA | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-policy-application-ba/ |
| 56 | Environmental Studies, BA: General Environmental Studies | BA | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-ba/ |
| 57 | Environmental Studies, BA: Global Environmental Systems | BA | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-global-systems-ba/ |
| 58 | Environmental Studies, BA: Sustainability and Environmental Management | BA | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-sustainability-management-ba/ |
| 59 | Fine Arts, BA | BA | https://catalog.upenn.edu/undergraduate/programs/fine-arts-ba/ |
| 60 | Francophone, Italian and Germanic Studies, BA: Dual Language | BA | https://catalog.upenn.edu/undergraduate/programs/francophone-italian-germanic-dual-language-ba/ |
| 61 | Francophone, Italian and Germanic Studies, BA: French and Francophone Studies | BA | https://catalog.upenn.edu/undergraduate/programs/francophone-italian-germanic-french-francophone-ba/ |
| 62 | Francophone, Italian and Germanic Studies, BA: Germanic Studies | BA | https://catalog.upenn.edu/undergraduate/programs/francophone-italian-germanic-germanic-ba/ |
| 63 | Francophone, Italian and Germanic Studies, BA: Italian Studies | BA | https://catalog.upenn.edu/undergraduate/programs/francophone-italian-germanic-italian-ba/ |
| 64 | Gender, Sexuality, & Women's Studies, BA: Feminist Studies | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-feminist-studies-ba/ |
| 65 | Gender, Sexuality, & Women's Studies, BA: General | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-ba/ |
| 66 | Gender, Sexuality, & Women's Studies, BA: Global Gender and Sexuality Studies | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-global-gender-sexuality-studies-ba/ |
| 67 | Gender, Sexuality, & Women's Studies, BA: Health and Disability Studies | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-health-disability-studies-ba/ |
| 68 | Gender, Sexuality, & Women's Studies, BA: LGBTQ Studies | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-lgbtq-studies-ba/ |
| 69 | Gender, Sexuality, & Women's Studies, BA: Self Designed | BA | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-self-designed-ba/ |
| 70 | Health and Societies, BA: Bioethics and Society | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-bioethics-society-ba/ |
| 71 | Health and Societies, BA: Disease and Culture | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-disease-culture-ba/ |
| 72 | Health and Societies, BA: Global Health | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-global-health-ba/ |
| 73 | Health and Societies, BA: Health Care Markets & Finance | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-health-care-markets-finance-ba/ |
| 74 | Health and Societies, BA: Health Policy & Law | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-health-policy-law-ba/ |
| 75 | Health and Societies, BA: Public Health | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-public-health-ba/ |
| 76 | Health and Societies, BA: Race, Gender and Health | BA | https://catalog.upenn.edu/undergraduate/programs/health-societies-race-gender-health-ba/ |
| 77 | Hispanic Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/hispanic-studies-ba/ |
| 78 | History of Art, BA | BA | https://catalog.upenn.edu/undergraduate/programs/history-art-ba/ |
| 79 | History, BA: American History | BA | https://catalog.upenn.edu/undergraduate/programs/history-american-history-ba/ |
| 80 | History, BA: Diplomatic History | BA | https://catalog.upenn.edu/undergraduate/programs/history-diplomatic-history-ba/ |
| 81 | History, BA: Economic History | BA | https://catalog.upenn.edu/undergraduate/programs/history-economic-history-ba/ |
| 82 | History, BA: European History | BA | https://catalog.upenn.edu/undergraduate/programs/history-european-history-ba/ |
| 83 | History, BA: Gender History | BA | https://catalog.upenn.edu/undergraduate/programs/history-gender-history-ba/ |
| 84 | History, BA: General History | BA | https://catalog.upenn.edu/undergraduate/programs/history-general-history-ba/ |
| 85 | History, BA: Intellectual History | BA | https://catalog.upenn.edu/undergraduate/programs/history-intellectual-history-ba/ |
| 86 | History, BA: Jewish History | BA | https://catalog.upenn.edu/undergraduate/programs/history-jewish-history-ba/ |
| 87 | History, BA: Political History | BA | https://catalog.upenn.edu/undergraduate/programs/history-political-history-ba/ |
| 88 | History, BA: World History | BA | https://catalog.upenn.edu/undergraduate/programs/history-world-history-ba/ |
| 89 | Individualized Major, BA | BA | https://catalog.upenn.edu/undergraduate/programs/individualized-major-indm-ba/ |
| 90 | International Relations, BA | BA | https://catalog.upenn.edu/undergraduate/programs/international-relations-ba/ |
| 91 | International Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/international-studies-ba/ |
| 92 | Jewish Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/jewish-studies-ba/ |
| 93 | Latin American & Latinx Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/latin-american-latinx-studies-ba/ |
| 94 | Law and Society, BA | BA | https://catalog.upenn.edu/undergraduate/programs/law-society-ba/ |
| 95 | Linguistics, BA | BA | https://catalog.upenn.edu/undergraduate/programs/linguistics-ba/ |
| 96 | Logic, Information, & Computation, BA | BA | https://catalog.upenn.edu/undergraduate/programs/logic-information-computation-ba/ |
| 97 | Mathematical Economics, BA | BA | https://catalog.upenn.edu/undergraduate/programs/mathematical-economics-ba/ |
| 98 | Mathematics, BA: Biological Mathematics | BA | https://catalog.upenn.edu/undergraduate/programs/mathematics-biological-mathematics-ba/ |
| 99 | Mathematics, BA: General Mathematics | BA | https://catalog.upenn.edu/undergraduate/programs/mathematics-ba/ |
| 100 | Middle Eastern Languages & Cultures, BA: Ancient Middle East | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-ancient-middle-east-ba/ |
| 101 | Middle Eastern Languages & Cultures, BA: Arabic & Hebrew Studies | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-arabic-hebrew-studies-ba/ |
| 102 | Middle Eastern Languages & Cultures, BA: Arabic Language and Literature | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-arabic-language-literature-ba/ |
| 103 | Middle Eastern Languages & Cultures, BA: Cultures and Societies of the Middle East and North Africa | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-culture-societies-middle-east-north-africa-ba/ |
| 104 | Middle Eastern Languages & Cultures, BA: Hebrew and Judaic Studies | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-hebrew-judaic-studies-ba/ |
| 105 | Middle Eastern Languages & Cultures, BA: Persian Languages & Literature | BA | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-persian-languages-literature-ba/ |
| 106 | Modern Middle Eastern Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/modern-middle-eastern-studies-ba/ |
| 107 | Music, BA | BA | https://catalog.upenn.edu/undergraduate/programs/music-ba/ |
| 108 | Neuroscience, BA | BA | https://catalog.upenn.edu/undergraduate/programs/neuroscience-ba/ |
| 109 | Nutrition Science, BA | BA | https://catalog.upenn.edu/undergraduate/programs/nutrition-science-ba/ |
| 110 | Philosophy, BA: General Philosophy | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-general-philosophy-ba/ |
| 111 | Philosophy, BA: Humanistic Philosophy | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-humanistic-philosophy-ba/ |
| 112 | Philosophy, BA: Moral and Political Philosophy | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-political-moral-philosophy-ba/ |
| 113 | Philosophy, BA: Philosophy of Science | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-philosophy-science-ba/ |
| 114 | Philosophy, Politics and Economics, BA: Choice & Behavior | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-politics-economics-choice-behavior-ba/ |
| 115 | Philosophy, Politics and Economics, BA: Distributive Justice | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-politics-economics-distributive-justice-ba/ |
| 116 | Philosophy, Politics and Economics, BA: Globalization | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-politics-economics-globalization-ba/ |
| 117 | Philosophy, Politics and Economics, BA: Public Policy & Governance | BA | https://catalog.upenn.edu/undergraduate/programs/philosophy-politics-economics-public-policy-governance-ba/ |
| 118 | Physics, BA: Astrophysics | BA | https://catalog.upenn.edu/undergraduate/programs/physics-astrophysics-ba/ |
| 119 | Physics, BA: Biological Science | BA | https://catalog.upenn.edu/undergraduate/programs/physics-biological-science-ba/ |
| 120 | Physics, BA: Business & Technology | BA | https://catalog.upenn.edu/undergraduate/programs/physics-business-technology-ba/ |
| 121 | Physics, BA: Chemical Principles | BA | https://catalog.upenn.edu/undergraduate/programs/physics-chemical-principles-ba/ |
| 122 | Physics, BA: Computer Techniques | BA | https://catalog.upenn.edu/undergraduate/programs/physics-computer-techniques-ba/ |
| 123 | Physics, BA: Physical Theory and Experimental Technique | BA | https://catalog.upenn.edu/undergraduate/programs/physics-physical-theory-experimental-technique-ba/ |
| 124 | Political Science, BA: American Politics | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-american-politics-ba/ |
| 125 | Political Science, BA: Comparative Politics | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-comparative-politics-ba/ |
| 126 | Political Science, BA: General Political Science | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-general-ba/ |
| 127 | Political Science, BA: Individualized | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-individualized-ba/ |
| 128 | Political Science, BA: International Relations | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-international-relations-ba/ |
| 129 | Political Science, BA: Political Economy | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-economy-ba/ |
| 130 | Political Science, BA: Political Theory | BA | https://catalog.upenn.edu/undergraduate/programs/political-science-theory-ba/ |
| 131 | Psychology, BA | BA | https://catalog.upenn.edu/undergraduate/programs/psychology-ba/ |
| 132 | Religious Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/religious-studies-ba/ |
| 133 | Russian and East European Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/russian-east-european-studies-ba/ |
| 134 | Science, Technology and Society, BA: Biotechnology & Biomedicine | BA | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-biotechnology-biomedicine-ba/ |
| 135 | Science, Technology and Society, BA: Energy and Environment | BA | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-energy-environment-ba/ |
| 136 | Science, Technology and Society, BA: Global Science and Technology | BA | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-global-science-technology-ba/ |
| 137 | Science, Technology and Society, BA: Information and Organizations | BA | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-information-organizations-ba/ |
| 138 | Science, Technology and Society, BA: Science/Nature/Culture | BA | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-science-nature-culture-ba/ |
| 139 | Sociology, BA: Applied Research and Data Analysis | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-applied-research-data-analysis-ba/ |
| 140 | Sociology, BA: Cities, Markets, and the Global Economy | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-cities-markets-global-economy-ba/ |
| 141 | Sociology, BA: Culture and Diversity | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-culture-diversity-ba/ |
| 142 | Sociology, BA: Education and Society | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-education-society-ba/ |
| 143 | Sociology, BA: Family, Gender and Society | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-family-gender-society-ba/ |
| 144 | Sociology, BA: Medical Sociology | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-medical-sociology-ba/ |
| 145 | Sociology, BA: Structures of Opportunity and Inequality | BA | https://catalog.upenn.edu/undergraduate/programs/sociology-structures-opportunity-inequality-ba/ |
| 146 | South Asia Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/south-asia-studies-ba/ |
| 147 | Theatre Arts, BA | BA | https://catalog.upenn.edu/undergraduate/programs/theatre-arts-ba/ |
| 148 | Urban Studies, BA | BA | https://catalog.upenn.edu/undergraduate/programs/urban-studies-ba/ |
| 149 | Visual Studies, BA: Architecture Practice and Technology | BA | https://catalog.upenn.edu/undergraduate/programs/visual-studies-architecture-practice-technology-ba/ |
| 150 | Visual Studies, BA: Art and Culture of Seeing | BA | https://catalog.upenn.edu/undergraduate/programs/visual-studies-art-culture-seeing-ba/ |
| 151 | Visual Studies, BA: Art, Practice and Technology | BA | https://catalog.upenn.edu/undergraduate/programs/visual-studies-art-practice-technology-ba/ |
| 152 | Visual Studies, BA: Philosophy and Science of Seeing | BA | https://catalog.upenn.edu/undergraduate/programs/visual-studies-philosophy-science-seeing-ba/ |

##### Minor (86)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Africana Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/africana-studies-minor/ |
| 2 | American Public Policy, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/american-public-policy-minor/ |
| 3 | American Sign Language and Deaf Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/american-sign-language-deaf-studies-minor/ |
| 4 | Ancient History, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/ancient-history-minor/ |
| 5 | Anthropology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/anthropology-minor/ |
| 6 | Archaeological Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/archaeological-science-minor/ |
| 7 | Architectural History, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/architectural-history-minor/ |
| 8 | Architecture, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/architecture-minor/ |
| 9 | Asian American Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/asian-american-studies-minor/ |
| 10 | Bioethics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/bioethics-minor/ |
| 11 | Biology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/biology-minor/ |
| 12 | Biophysics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/biophysics-minor/ |
| 13 | Chemistry, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/chemistry-minor/ |
| 14 | Cinema and Media Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/cinema-media-studies-minor/ |
| 15 | Classical Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/classical-studies-minor/ |
| 16 | Cognitive Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/cognitive-science-minor/ |
| 17 | Comparative Literature, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/comparative-literature-minor/ |
| 18 | Computational Neuroscience, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/computational-neuroscience-minor/ |
| 19 | Consumer Psychology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/consumer-psychology-minor/ |
| 20 | Creative Writing, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/creative-writing-minor/ |
| 21 | Data Science and Analytics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/data-science-analytics-minor/ |
| 22 | Digital Humanities, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/digital-humanities-minor/ |
| 23 | East Asian Area Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/east-asian-area-studies-minor/ |
| 24 | East Asian Languages and Civilizations: Chinese, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-chinese-minor/ |
| 25 | East Asian Languages and Civilizations: Japanese, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-japanese-minor/ |
| 26 | East Asian Languages and Civilizations: Korean, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/east-asian-languages-civilizations-korean-minor/ |
| 27 | Economic Policy, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/economic-policy-minor/ |
| 28 | Economics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/economics-minor/ |
| 29 | English, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/english-minor/ |
| 30 | Environmental Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/environmental-science-minor/ |
| 31 | Environmental Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/environmental-studies-minor/ |
| 32 | European Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/european-studies-minor/ |
| 33 | Fine Arts, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/fine-arts-minor/ |
| 34 | French and Francophone Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/french-francophone-studies-minor/ |
| 35 | Gender, Sexuality, and Women's Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/gender-sexuality-womens-studies-minor/ |
| 36 | Geology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/geology-minor/ |
| 37 | German, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/german-minor/ |
| 38 | Global Medieval Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/global-medieval-studies-minor/ |
| 39 | Hispanic Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/hispanic-studies-minor/ |
| 40 | History of Art, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/history-art-minor/ |
| 41 | History, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/history-minor/ |
| 42 | International Development, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/international-development-minor/ |
| 43 | International Relations, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/international-relations-minor/ |
| 44 | Italian Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/italian-studies-minor/ |
| 45 | Jewish Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/jewish-studies-minor/ |
| 46 | Journalistic Writing, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/journalistic-writing-minor/ |
| 47 | Landscape Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/landscape-studies-minor/ |
| 48 | Latin American and Latinx Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/latin-american-latinx-studies-minor/ |
| 49 | Law and Society, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/law-society-minor/ |
| 50 | Legal Studies & History, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/legal-studies-history-minor/ |
| 51 | Linguistics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/linguistics-minor/ |
| 52 | Logic, Information, & Computation, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/logic-information-computation-minor/ |
| 53 | Mathematics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/mathematics-minor/ |
| 54 | Medical Sociology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/medical-sociology-minor/ |
| 55 | Middle Eastern Languages & Cultures: Ancient Middle East, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-ancient-middle-east-minor/ |
| 56 | Middle Eastern Languages & Cultures: Arabic & Hebrew Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-arabic-hebrew-studies-minor/ |
| 57 | Middle Eastern Languages & Cultures: Arabic Language and Literature, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-arabic-language-literature-minor/ |
| 58 | Middle Eastern Languages & Cultures: Cultures and Societies of the Middle East and North Africa, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-cultures-societies-middle-east-north-africa-minor/ |
| 59 | Middle Eastern Languages & Cultures: Hebrew & Judaic Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-hebrew-judaica-minor/ |
| 60 | Middle Eastern Languages & Cultures: Persian Language & Literature, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/middle-eastern-languages-cultures-persian-language-literature-minor/ |
| 61 | Modern Middle Eastern Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/modern-middle-eastern-studies-minor/ |
| 62 | Music, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/music-minor/ |
| 63 | Native American and Indigenous Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/native-american-indigenous-studies-minor/ |
| 64 | Neuroscience and Health Care Management, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/neuroscience-health-care-management-minor/ |
| 65 | Neuroscience, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/neuroscience-minor/ |
| 66 | Nutrition, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/nutrition-minor/ |
| 67 | Philosophy, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/philosophy-minor/ |
| 68 | Physics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/physics-minor/ |
| 69 | Political Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/political-science-minor/ |
| 70 | Psychoanalytic Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/psychoanalytic-studies-minor/ |
| 71 | Psychology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/psychology-minor/ |
| 72 | Religious Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/religious-studies-minor/ |
| 73 | Russian and East European Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/russian-east-european-studies-minor/ |
| 74 | Russian Language, Literature and Culture, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/russian-language-literature-culture-minor/ |
| 75 | Science, Technology and Society, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/science-technology-society-minor/ |
| 76 | Secondary Education, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/secondary-education-minor/ |
| 77 | Sociology, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/sociology-minor/ |
| 78 | South Asia Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/south-asia-studies-minor/ |
| 79 | Statistics and Data Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/statistics-data-science-minor/ |
| 80 | Survey Research and Data Analytics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/survey-research-data-analytics-minor/ |
| 81 | Sustainability and Environmental Management, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/sustainability-environmental-management-minor/ |
| 82 | Theatre Arts, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/theatre-arts-minor/ |
| 83 | Urban Education, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/urban-education-minor/ |
| 84 | Urban Real Estate and Development, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/urban-real-estate-development-minor/ |
| 85 | Urban Studies, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/urban-studies-minor/ |
| 86 | Yiddish, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/yiddish-minor/ |

##### Certificate (14)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Positive Psychology, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/applied-positive-psychology-certificate/ |
| 2 | Climate Science, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/climate-science-certificate/ |
| 3 | Creative Writing, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/creative-writing-certificate/ |
| 4 | Data Analytics, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/data-analytics-certificate/ |
| 5 | Dialogue, Ethics, and Social Good, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/dialogue-ethics-social-good-certificate/ |
| 6 | Digital Storytelling and Content Creation, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/digital-storytelling-content-creation-certificate/ |
| 7 | Digital Strategies and Applications, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/digital-strategies-applications-certificate/ |
| 8 | Global and Regional Studies, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/global-regional-studies-certificate/ |
| 9 | Leadership & Communication, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/leadership-communication-certificate/ |
| 10 | Neuroscience, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/neuroscience-certificate/ |
| 11 | Professional Writing, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/professional-writing-certificate/ |
| 12 | Science Foundations, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/science-foundations-certificate/ |
| 13 | Team Culture and Collaboration, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/team-culture-collaboration-certificate/ |
| 14 | UpSkill, Certificate | CERTIFICATE | https://catalog.upenn.edu/undergraduate/programs/upskill-certificate/ |

##### BAAS (9)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Creative Studies, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/creative-studies-baas/ |
| 2 | Data Analytics and Psychological Sciences, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/data-analytics-psychological-sciences-baas/ |
| 3 | Data Analytics and Social Sciences, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/data-analytics-social-sciences-baas/ |
| 4 | Individualized Studies, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/individualized-baas/ |
| 5 | Leadership and Communication, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/leadership-communication-baas/ |
| 6 | Literature, Culture and Tradition, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/literature-culture-tradition-baas/ |
| 7 | Organizational Studies, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/organizational-studies-baas/ |
| 8 | Physical and Life Sciences, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/physical-life-sciences-baas/ |
| 9 | Writing, BAAS | BAAS | https://catalog.upenn.edu/undergraduate/programs/writing-baas/ |

##### Prep (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Pre-Health Core Studies, Post-Baccalaureate Preparatory Program | PREP | https://catalog.upenn.edu/undergraduate/programs/pre-health-core-post-bacc-prep/ |
| 2 | Pre-Health Specialized Studies, Post-Baccalaureate Preparatory Program | PREP | https://catalog.upenn.edu/undergraduate/programs/pre-health-specialized-post-bacc-prep/ |

##### BFA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Fine Arts, BFA | BFA | https://catalog.upenn.edu/undergraduate/programs/fine-arts-bfa/ |

#### School of Engineering and Applied Science

##### BSE (10)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Artificial Intelligence, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/artificial-intelligence-bse/ |
| 2 | Bioengineering, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/bioengineering-bse/ |
| 3 | Chemical and Biomolecular Engineering, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/chemical-biomolecular-engineering-bse/ |
| 4 | Computer Engineering, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/computer-engineering-bse/ |
| 5 | Computer Science, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/computer-science-bse/ |
| 6 | Digital Media Design, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/digital-media-design-bse/ |
| 7 | Electrical Engineering, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/electrical-engineering-bse/ |
| 8 | Materials Science and Engineering, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/materials-science-engineering-bse/ |
| 9 | Mechanical Engineering and Applied Mechanics, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/mechanical-engineering-applied-mechanics-bse/ |
| 10 | Visual and Interactive Computing, BSE | BSE | https://catalog.upenn.edu/undergraduate/programs/visual-interactive-computing-bse/ |

##### Minor (9)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Chemical & Biomolecular Engineering, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/chemical-biomolecular-engineering-minor/ |
| 2 | Computer Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/computer-science-minor/ |
| 3 | Data Science, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/data-science-minor/ |
| 4 | Digital Media Design, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/digital-media-design-minor/ |
| 5 | Electrical Engineering, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/electrical-engineering-minor/ |
| 6 | Energy & Sustainability, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/energy-sustainability-minor/ |
| 7 | Engineering Entrepreneurship, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/engineering-entrepreneurship-minor/ |
| 8 | Materials Science and Engineering, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/materials-science-engineering-minor/ |
| 9 | Mechanical Engineering and Applied Mechanics, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/meam-minor/ |

##### BAS (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Biomedical Science, BAS | BAS | https://catalog.upenn.edu/undergraduate/programs/biomedical-science-bas/ |
| 2 | Computer Science, BAS | BAS | https://catalog.upenn.edu/undergraduate/programs/computer-science-bas/ |

#### The Wharton School

##### BS (26)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Accounting, BS | BS | https://catalog.upenn.edu/undergraduate/programs/accounting-bs/ |
| 2 | Artificial Intelligence for Business, BS | BS | https://catalog.upenn.edu/undergraduate/programs/artificial-intelligence-business-bs/ |
| 3 | Behavioral Economics, BS | BS | https://catalog.upenn.edu/undergraduate/programs/behavioral-economics-bs/ |
| 4 | Business Analytics, BS | BS | https://catalog.upenn.edu/undergraduate/programs/business-analytics-bs/ |
| 5 | Business Economics and Public Policy, BS | BS | https://catalog.upenn.edu/undergraduate/programs/business-economics-public-policy-bs/ |
| 6 | Entrepreneurship and Innovation, BS | BS | https://catalog.upenn.edu/undergraduate/programs/entrepreneurship-innovation-bs/ |
| 7 | Finance, BS | BS | https://catalog.upenn.edu/undergraduate/programs/finance-bs/ |
| 8 | Health Care Management and Policy, BS | BS | https://catalog.upenn.edu/undergraduate/programs/health-care-management-policy-bs/ |
| 9 | Impact, Value and Sustainable Business, BS | BS | https://catalog.upenn.edu/undergraduate/programs/impact-value-sustainable-business-bs/ |
| 10 | Individualized, BS | BS | https://catalog.upenn.edu/undergraduate/programs/individualized-bs/ |
| 11 | Leading Across Differences, BS | BS | https://catalog.upenn.edu/undergraduate/programs/leading-across-differences-bs/ |
| 12 | Legal Studies & Business Ethics, BS | BS | https://catalog.upenn.edu/undergraduate/programs/legal-studies-business-ethics-bs/ |
| 13 | Management, BS: General Track | BS | https://catalog.upenn.edu/undergraduate/programs/management-general-track-bs/ |
| 14 | Management, BS: Multinational Management Track | BS | https://catalog.upenn.edu/undergraduate/programs/management-multinational-management-track-bs/ |
| 15 | Management, BS: Organizational Effectiveness Track | BS | https://catalog.upenn.edu/undergraduate/programs/management-organizational-effectiveness-track-bs/ |
| 16 | Management, BS: Strategic Management Track | BS | https://catalog.upenn.edu/undergraduate/programs/management-strategic-management-track-bs/ |
| 17 | Marketing & Communication, BS | BS | https://catalog.upenn.edu/undergraduate/programs/marketing-communication-bs/ |
| 18 | Marketing & Operations Management, BS | BS | https://catalog.upenn.edu/undergraduate/programs/marketing-operations-management-bs/ |
| 19 | Marketing, BS | BS | https://catalog.upenn.edu/undergraduate/programs/marketing-bs/ |
| 20 | Operations, Information & Decisions, BS: Decision Processes Track | BS | https://catalog.upenn.edu/undergraduate/programs/operations-information-decisions-decision-processes-track-bs/ |
| 21 | Operations, Information & Decisions, BS: General Track | BS | https://catalog.upenn.edu/undergraduate/programs/operations-information-decisions-general-track-bs/ |
| 22 | Operations, Information & Decisions, BS: Information Systems Track | BS | https://catalog.upenn.edu/undergraduate/programs/operations-information-decisions-information-systems-track-bs/ |
| 23 | Operations, Information & Decisions, BS: Operations Management/Management Science Track | BS | https://catalog.upenn.edu/undergraduate/programs/operations-information-decisions-operations-management-science-track-bs/ |
| 24 | Real Estate, BS | BS | https://catalog.upenn.edu/undergraduate/programs/real-estate-bs/ |
| 25 | Retailing, BS | BS | https://catalog.upenn.edu/undergraduate/programs/retailing-bs/ |
| 26 | Statistics and Data Science, BS | BS | https://catalog.upenn.edu/undergraduate/programs/statistics-data-science-bs/ |

#### School of Nursing

##### Minor (5)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Global Health, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/global-health-minor/ |
| 2 | Health Communications, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/health-communications-minor/ |
| 3 | History, Health and the Humanities, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/history-health-humanities-minor/ |
| 4 | Nursing and Health Services Management, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/nursing-health-services-management-minor/ |
| 5 | Nutrition, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/nursing-nutrition-minor/ |

##### BSN (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nursing, BSN | BSN | https://catalog.upenn.edu/undergraduate/programs/nursing-bsn/ |
| 2 | Nutrition Science, BSN | BSN | https://catalog.upenn.edu/undergraduate/programs/nutrition-science-bsn/ |

#### Stuart Weitzman School of Design

##### Minor (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Design, Minor | MINOR | https://catalog.upenn.edu/undergraduate/programs/design-minor/ |


### 1.3 Coordinated dual-degree & specialized programs

Penn's distinctive coordinated dual-degree programs each grant **two bachelor's degrees** from two schools. Applicants indicate the program on the first-year application; most require additional essays. External transfers are NOT eligible for most. (Source: [admissions.upenn.edu/academics/exploring-academics/specialized-degree-programs](https://admissions.upenn.edu/academics/exploring-academics/specialized-degree-programs))

| Program | Degrees earned | Schools | Notes |
|---------|---------------|---------|-------|
| **Huntsman** (Program in International Studies & Business) | BA (International Studies) + BS (Economics) | SAS + Wharton | First-year app only; 1 extra essay; no transfer/internal |
| **LSM** (Roy & Diana Vagelos Program in Life Sciences & Management) | BA (life science major) + BS (Economics) | SAS + Wharton | First-year app or internal transfer; 2 extra essays; no external transfer |
| **M&T** (Jerome Fisher Program in Management & Technology) | BS (Economics) + BSE or BAS | Wharton + SEAS | First-year app or internal transfer; 2 extra essays; no external transfer |
| **NHCM** (Nursing and Health Care Management) | BSN + BS (Economics) | Nursing + Wharton | First-year app or internal transfer after first year; 1 extra essay |
| **VIPER** (Roy & Diana Vagelos Integrated Program in Energy Research) | BA (Physics/Chem/Bio/Math/Earth & Env Sci) + BSE (ChemBE/EE/MSE/MEAM) | SAS + SEAS | First-year app or internal transfer; 1 extra essay |
| **VIC** (Visual and Interactive Computing) | BSE (Visual and Interactive Computing) | SEAS (with Weitzman electives) | Interdisciplinary CS × fine arts; not a dual-degree but a specialized BSE |

### 1.4 Undergraduate minors — complete list

All 101 undergraduate minors appear under their home school in §1.2 (rows tagged `Minor`). The largest minor collections are in SAS (86) and SEAS (9); Nursing (5), Wharton (no cataloged UG minors — concentrations instead), and Weitzman (1 Design minor) round out the set.

### 1.5 General education / curriculum

Penn's general-education framework is set by each undergraduate school rather than by a single university core. The College of Arts & Sciences imposes distribution requirements across sectors; Wharton requires a liberal-arts foundation plus the business core; SEAS requires science/math/engineering fundamentals plus humanities/social-science electives; Nursing integrates arts/sciences with clinical coursework. Detail lives on each school's curriculum page (P2 follow-up).

### 1.6 Application snapshot (UG)

| Item | Value | Source |
|------|-------|--------|
| Application platforms | Common App, Coalition App, QuestBridge | E-U-002 |
| Application fee | **$75** (fee waiver available) | E-U-003 |
| Early Decision deadline | **November 1, 2025** (binding; decision in December) | E-U-001 |
| Regular Decision deadline | **January 5, 2026** (decision in April) | E-U-001 |
| Standardized testing | **SAT or ACT REQUIRED** for 2025-26 (hardship waiver available; NOT test-optional) | E-U-004 |
| SAT code | 2926 | E-U-004 |
| ACT code | 3732 | E-U-004 |
| TOEFL code | 2926 | E-U-004 |
| Letters of recommendation | 1 counselor + 1 core-subject teacher (1 optional extra) | E-U-005 |
| Essays | 3 Penn-specific short answers + school-specific prompt | E-U-005 |

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 学位级别

> Every graduate catalog row appears exactly once below (322 grad rows = 264 degrees + 53 certificates/certifications + 5 minors). URL points to each program's official catalog page. Penn's graduate admissions is **decentralized** (§2.3) — each school runs its own application, deadline, and GRE/ELP policy; the catalog pages carry curriculum only.

#### School of Arts & Sciences

##### PhD (43)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Africana Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/africana-studies-phd/ |
| 2 | Ancient History, PhD | PHD | https://catalog.upenn.edu/graduate/programs/ancient-history-phd/ |
| 3 | Anthropology, PhD: Archaeology | PHD | https://catalog.upenn.edu/graduate/programs/anthropology-archaeology-phd/ |
| 4 | Anthropology, PhD: Biological | PHD | https://catalog.upenn.edu/graduate/programs/anthropology-biological-phd/ |
| 5 | Anthropology, PhD: Cultural | PHD | https://catalog.upenn.edu/graduate/programs/anthropology-cultural-phd/ |
| 6 | Anthropology, PhD: Linguistic | PHD | https://catalog.upenn.edu/graduate/programs/anthropology-linguistic-phd/ |
| 7 | Anthropology, PhD: Medical | PHD | https://catalog.upenn.edu/graduate/programs/anthropology-medical-phd/ |
| 8 | Applied Mathematics and Computational Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/applied-mathematics-computational-science-phd/ |
| 9 | Art and Archaeology of the Mediterranean World, PhD | PHD | https://catalog.upenn.edu/graduate/programs/art-archaeology-mediterranean-world-phd/ |
| 10 | Biology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/biology-phd/ |
| 11 | Chemistry, PhD | PHD | https://catalog.upenn.edu/graduate/programs/chemistry-phd/ |
| 12 | Cinema and Media Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/cinema-media-studies-phd/ |
| 13 | Comparative Literature, PhD | PHD | https://catalog.upenn.edu/graduate/programs/comparative-literature-phd/ |
| 14 | Criminology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/criminology-phd/ |
| 15 | Demography, PhD | PHD | https://catalog.upenn.edu/graduate/programs/demography-phd/ |
| 16 | Earth and Environmental Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/earth-environmental-science-phd/ |
| 17 | East Asian Languages and Civilizations, PhD | PHD | https://catalog.upenn.edu/graduate/programs/east-asian-languages-civilizations-phd/ |
| 18 | Economics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/economics-phd/ |
| 19 | English, PhD | PHD | https://catalog.upenn.edu/graduate/programs/english-phd/ |
| 20 | Francophone, Italian and Germanic Studies, PhD: French and Francophone Studies | PHD | https://catalog.upenn.edu/graduate/programs/francophone-italian-germanic-french-francophone-studies-phd/ |
| 21 | Francophone, Italian and Germanic Studies, PhD: Germanic Studies | PHD | https://catalog.upenn.edu/graduate/programs/francophone-italian-germanic-germanic-studies-phd/ |
| 22 | Francophone, Italian and Germanic Studies, PhD: Italian Studies | PHD | https://catalog.upenn.edu/graduate/programs/francophone-italian-germanic-italian-studies-phd/ |
| 23 | Greek and Latin Languages and Literatures, PhD | PHD | https://catalog.upenn.edu/graduate/programs/greek-latin-languages-literatures-phd/ |
| 24 | History and Sociology of Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/history-sociology-science-phd/ |
| 25 | History of Art, PhD | PHD | https://catalog.upenn.edu/graduate/programs/history-art-phd/ |
| 26 | History, PhD | PHD | https://catalog.upenn.edu/graduate/programs/history-phd/ |
| 27 | Linguistics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/linguistics-phd/ |
| 28 | Mathematics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/mathematics-phd/ |
| 29 | Middle Eastern Languages & Cultures, PhD: Biblical Studies | PHD | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-biblical-studies-phd/ |
| 30 | Middle Eastern Languages & Cultures, PhD: Egyptology | PHD | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-egyptology-phd/ |
| 31 | Middle Eastern Languages & Cultures, PhD: Hebrew and Judaic Studies | PHD | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-hebrew-judaic-studies-phd/ |
| 32 | Middle Eastern Languages & Cultures, PhD: Mesopotamian Civilization | PHD | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-mesopotamian-civilization-phd/ |
| 33 | Middle Eastern Languages & Cultures, PhD: Middle Eastern Literatures & Societies | PHD | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-middle-eastern-literatures-societies-phd/ |
| 34 | Music, PhD: Composition | PHD | https://catalog.upenn.edu/graduate/programs/music-musical-composition-phd/ |
| 35 | Music, PhD: Music Studies | PHD | https://catalog.upenn.edu/graduate/programs/music-music-studies-phd/ |
| 36 | Philosophy, PhD | PHD | https://catalog.upenn.edu/graduate/programs/philosophy-phd/ |
| 37 | Physics and Astronomy, PhD | PHD | https://catalog.upenn.edu/graduate/programs/physics-astronomy-phd/ |
| 38 | Political Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/political-science-phd/ |
| 39 | Psychology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/psychology-phd/ |
| 40 | Religious Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/religious-studies-phd/ |
| 41 | Sociology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/sociology-phd/ |
| 42 | South Asia Regional Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/south-asia-regional-studies-phd/ |
| 43 | Spanish and Portuguese, PhD | PHD | https://catalog.upenn.edu/graduate/programs/spanish-portuguese-phd/ |

##### MA (15)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Mathematics and Computational Science, MA | MA | https://catalog.upenn.edu/graduate/programs/applied-mathematics-computational-science-ma/ |
| 2 | Art and Archaeology of the Mediterranean World, MA | MA | https://catalog.upenn.edu/graduate/programs/art-archaeology-mediterranean-world-ma/ |
| 3 | Cinema and Media Studies, MA | MA | https://catalog.upenn.edu/graduate/programs/cinema-media-studies-ma/ |
| 4 | East Asian Languages and Civilizations, MA | MA | https://catalog.upenn.edu/graduate/programs/east-asian-languages-civilizations-ma/ |
| 5 | English, MA | MA | https://catalog.upenn.edu/graduate/programs/english-ma/ |
| 6 | History of Art, MA | MA | https://catalog.upenn.edu/graduate/programs/history-art-ma/ |
| 7 | International Studies, MA | MA | https://catalog.upenn.edu/graduate/programs/international-studies-ma/ |
| 8 | Linguistics, MA | MA | https://catalog.upenn.edu/graduate/programs/linguistics-ma/ |
| 9 | Mathematics, MA | MA | https://catalog.upenn.edu/graduate/programs/mathematics-ma/ |
| 10 | Middle Eastern Languages & Cultures, MA: Biblical Studies | MA | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-biblical-studies-ma/ |
| 11 | Middle Eastern Languages & Cultures, MA: Egyptology | MA | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-egyptology-ma/ |
| 12 | Middle Eastern Languages & Cultures, MA: Hebrew and Judaic Studies | MA | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-hebrew-judaic-studies-ma/ |
| 13 | Middle Eastern Languages & Cultures, MA: Mesopotamian Civilization | MA | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-mesopotamian-civilization-ma/ |
| 14 | Middle Eastern Languages & Cultures, MA: Middle Eastern Literatures & Societies | MA | https://catalog.upenn.edu/graduate/programs/middle-eastern-languages-cultures-middle-eastern-literatures-societies-ma/ |
| 15 | South Asia Regional Studies, MA | MA | https://catalog.upenn.edu/graduate/programs/south-asia-regional-studies-ma/ |

##### MPA (6)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Global, MPA | MPA | https://catalog.upenn.edu/graduate/programs/global-mpa/ |
| 2 | Government Administration (Exec), MPA | MPA | https://catalog.upenn.edu/graduate/programs/government-administration-mpa/ |
| 3 | Government Administration (FT), MPA | MPAF | https://catalog.upenn.edu/graduate/programs/government-administration-mpaf/ |
| 4 | International Impact Evaluation, MPA | MPA | https://catalog.upenn.edu/graduate/programs/international-impact-evaluation-mpa/ |
| 5 | International, MPA | MPA | https://catalog.upenn.edu/graduate/programs/international-mpa/ |
| 6 | Quantitative Policy Analysis, MPA | MPA | https://catalog.upenn.edu/graduate/programs/quantitative-policy-analysis-mpa/ |

##### Certificate (3)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Engineering Geology, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/engineering-geology-certificate/ |
| 2 | Environmental Hydrogeology, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/environmental-hydrogeology-certificate/ |
| 3 | Global Public Administration, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/global-public-administration-certificate/ |

##### MPhil (3)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Individualized, MPhil | MPHIL | https://catalog.upenn.edu/graduate/programs/individualized-mphil/ |
| 2 | Mathematics, MPhil | MPHIL | https://catalog.upenn.edu/graduate/programs/mathematics-mphil/ |
| 3 | Organizational Dynamics, MPhil | MPHIL | https://catalog.upenn.edu/graduate/programs/organizational-dynamics-mphil/ |

##### MCPL (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Criminology and Police Leadership, MCPL | MCPL | https://catalog.upenn.edu/graduate/programs/applied-criminology-police-leadership-mcpl/ |

##### MEDS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Economics and Data Science, MEDS | MEDS | https://catalog.upenn.edu/graduate/programs/applied-economics-data-science-meds/ |

##### MSAG (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Geosciences, MSAG | MSAG | https://catalog.upenn.edu/graduate/programs/applied-geosciences-msag/ |

##### MAPP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Applied Positive Psychology, MAPP | MAPP | https://catalog.upenn.edu/graduate/programs/applied-positive-psychology-mapp/ |

##### MBDS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Behavioral and Decision Sciences, MBDS | MBDS | https://catalog.upenn.edu/graduate/programs/behavioral-decision-sciences-mbds/ |

##### MCS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Chemical Sciences, MCS | MCS | https://catalog.upenn.edu/graduate/programs/chemical-sciences-mcs/ |

##### MS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Criminology, MS | MS | https://catalog.upenn.edu/graduate/programs/criminology-ms/ |

##### MES (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Environmental Studies, MES | MES | https://catalog.upenn.edu/graduate/programs/environmental-studies-mes/ |

##### MLA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Liberal Arts Individualized, MLA | MLA | https://catalog.upenn.edu/graduate/programs/liberal-arts-individualized-mla/ |

##### MSOD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Organizational Dynamics, MSOD | MSOD | https://catalog.upenn.edu/graduate/programs/organizational-dynamics-msod/ |

#### School of Engineering and Applied Science

##### MSE (17)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Artificial Intelligence, MSE | MSE | https://catalog.upenn.edu/graduate/programs/artificial-intelligence-mse/ |
| 2 | Bioengineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/bioengineering-mse/ |
| 3 | Chemical & Biomolecular Engineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/chemical-biomolecular-engineering-mse/ |
| 4 | Computer & Information Science, MSE | MSE | https://catalog.upenn.edu/graduate/programs/computer-information-science-mse/ |
| 5 | Computer Graphics & Game Technology, MSE | MSE | https://catalog.upenn.edu/graduate/programs/computer-graphics-game-technology-mse/ |
| 6 | Data Science and Artificial Intelligence, MSE | MSE | https://catalog.upenn.edu/graduate/programs/data-science-artificial-intelligence-mse/ |
| 7 | Data Science, MSE | MSE | https://catalog.upenn.edu/graduate/programs/data-science-mse/ |
| 8 | Electrical Engineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/electrical-engineering-mse/ |
| 9 | Energy and Sustainability Engineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/energy-sustainability-engineering-mse/ |
| 10 | Integrated Product Design, MSE | MSE | https://catalog.upenn.edu/graduate/programs/integrated-product-design-mse/ |
| 11 | Materials Science and Engineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/materials-science-engineering-mse/ |
| 12 | Mechanical Engineering & Applied Mechanics, MSE | MSE | https://catalog.upenn.edu/graduate/programs/mechanical-engineering-applied-mechanics-mse/ |
| 13 | Robotics, MSE | MSE | https://catalog.upenn.edu/graduate/programs/robotics-mse/ |
| 14 | Scientific Computing, MSE | MSE | https://catalog.upenn.edu/graduate/programs/scientific-computing-mse/ |
| 15 | Software Systems and Cybersecurity, MSE | MSE | https://catalog.upenn.edu/graduate/programs/software-systems-cybersecurity-mse/ |
| 16 | Systems Engineering, MSE | MSE | https://catalog.upenn.edu/graduate/programs/systems-engineering-mse/ |
| 17 | Technology and Innovation, MSE | MSE | https://catalog.upenn.edu/graduate/programs/technology-innovation-mse/ |

##### Certificate (8)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Advanced Scientific Computing, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/advanced-scientific-computing-certificate/ |
| 2 | Artificial Intelligence, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/artificial-intelligence-certificate/ |
| 3 | Computer Science Fundamentals, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/computer-science-fundamentals-certificate/ |
| 4 | Data Science, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/data-science-certificate/ |
| 5 | Engineering Entrepreneurship, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/engineering-entrepreneurship-certificate/ |
| 6 | Integrated Product Design, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/integrated-product-design-certificate/ |
| 7 | Software Systems, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/software-systems-certificate/ |
| 8 | Sustainability Design & Engineering, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/sustainability-design-engineering-certificate/ |

##### PhD (6)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Bioengineering, PhD | PHD | https://catalog.upenn.edu/graduate/programs/bioengineering-phd/ |
| 2 | Chemical and Biomolecular Engineering, PhD | PHD | https://catalog.upenn.edu/graduate/programs/chemical-biomolecular-engineering-phd/ |
| 3 | Computer and Information Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/computer-information-science-phd/ |
| 4 | Electrical and Systems Engineering, PhD | PHD | https://catalog.upenn.edu/graduate/programs/electrical-systems-engineering-phd/ |
| 5 | Materials Science and Engineering, PhD | PHD | https://catalog.upenn.edu/graduate/programs/materials-science-engineering-phd/ |
| 6 | Mechanical Engineering and Applied Mechanics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/mechanical-engineering-applied-mechanics-phd/ |

##### MBIOT (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Biotechnology, MBIOT | MBIOT | https://catalog.upenn.edu/graduate/programs/biotechnology-mbiot/ |

##### MCIT (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Computer & Information Technology, MCIT | MCIT | https://catalog.upenn.edu/graduate/programs/computer-information-technology-mcit/ |

##### MASCS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Computer Science, MASCS | MASCS | https://catalog.upenn.edu/graduate/programs/computer-science-mascs/ |

##### MIPD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Integrated Product Design, MIPD | MIPD | https://catalog.upenn.edu/graduate/programs/integrated-product-design-mipd/ |

#### The Wharton School

##### MBA (23)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Accounting, MBA | MBA | https://catalog.upenn.edu/graduate/programs/accounting-mba/ |
| 2 | Artificial Intelligence for Business, MBA | MBA | https://catalog.upenn.edu/graduate/programs/artificial-intelligence-business-mba/ |
| 3 | Business Analytics, MBA | MBA | https://catalog.upenn.edu/graduate/programs/business-analytics-mba/ |
| 4 | Business Economics & Public Policy, MBA | MBA | https://catalog.upenn.edu/graduate/programs/business-economics-public-policy-mba/ |
| 5 | Business, Energy, Environment and Sustainability, MBA | MBA | https://catalog.upenn.edu/graduate/programs/business-energy-env-sustain-mba/ |
| 6 | Entrepreneurship and Innovation, MBA | MBA | https://catalog.upenn.edu/graduate/programs/entrepreneurship-innovation-mba/ |
| 7 | Executive MBA | MBA | https://catalog.upenn.edu/graduate/programs/executive-mba/ |
| 8 | Finance, MBA | MBA | https://catalog.upenn.edu/graduate/programs/finance-mba/ |
| 9 | Health Care Management, MBA | MBA | https://catalog.upenn.edu/graduate/programs/health-care-management-mba/ |
| 10 | Impact, Value and Sustainable Business, MBA | MBA | https://catalog.upenn.edu/graduate/programs/impact-value-sustainable-business-mba/ |
| 11 | Individualized Major, MBA | MBA | https://catalog.upenn.edu/graduate/programs/individualized-major-mba/ |
| 12 | Leading Across Differences, MBA | MBA | https://catalog.upenn.edu/graduate/programs/leading-across-differences-mba/ |
| 13 | Management, MBA | MBA | https://catalog.upenn.edu/graduate/programs/management-mba/ |
| 14 | Marketing & Operations Management, MBA | MBA | https://catalog.upenn.edu/graduate/programs/marketing-operations-management-mba/ |
| 15 | Marketing, MBA | MBA | https://catalog.upenn.edu/graduate/programs/marketing-mba/ |
| 16 | Multinational Management, MBA | MBA | https://catalog.upenn.edu/graduate/programs/multinational-management-mba/ |
| 17 | Operations, Information, & Decisions, MBA | MBA | https://catalog.upenn.edu/graduate/programs/operations-information-decisions-mba/ |
| 18 | Organizational Effectiveness, MBA | MBA | https://catalog.upenn.edu/graduate/programs/organizational-effectiveness-mba/ |
| 19 | Quantitative Finance, MBA | MBA | https://catalog.upenn.edu/graduate/programs/quantitative-finance-mba/ |
| 20 | Real Estate, MBA | MBA | https://catalog.upenn.edu/graduate/programs/real-estate-mba/ |
| 21 | Social and Governance Factors for Business, MBA | MBA | https://catalog.upenn.edu/graduate/programs/social-governance-factors-business-mba/ |
| 22 | Statistics and Data Science, MBA | MBA | https://catalog.upenn.edu/graduate/programs/statistics-data-science-mba/ |
| 23 | Strategic Management, MBA | MBA | https://catalog.upenn.edu/graduate/programs/strategic-management-mba/ |

##### PhD (9)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Accounting, PhD | PHD | https://catalog.upenn.edu/graduate/programs/accounting-phd/ |
| 2 | Applied Economics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/applied-economics-phd/ |
| 3 | Ethics and Legal Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/ethics-legal-studies-phd/ |
| 4 | Finance, PhD | PHD | https://catalog.upenn.edu/graduate/programs/finance-phd/ |
| 5 | Health Care Management & Economics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/health-care-management-economics-phd/ |
| 6 | Management, PhD | PHD | https://catalog.upenn.edu/graduate/programs/management-phd/ |
| 7 | Marketing, PhD | PHD | https://catalog.upenn.edu/graduate/programs/marketing-phd/ |
| 8 | Operations, Information and Decisions, PhD | PHD | https://catalog.upenn.edu/graduate/programs/operations-information-decisions-phd/ |
| 9 | Statistics and Data Science, PhD | PHD | https://catalog.upenn.edu/graduate/programs/statistics-data-science-phd/ |

##### MSQF (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Quantitative Finance, MSQF | MSQF | https://catalog.upenn.edu/graduate/programs/quantitative-finance-msqf/ |

##### Certificate (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Real Estate Design & Development, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/real-estate-design-development-certificate/ |

##### MA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Statistics and Data Science, MA | MA | https://catalog.upenn.edu/graduate/programs/statistics-data-science-ma/ |

#### School of Nursing

##### MSN (12)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Adult Gerontology Acute Care Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/adult-gerontology-acute-care-np-msn/ |
| 2 | Adult Gerontology Primary Care Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/adult-gerontology-primary-care-np-msn/ |
| 3 | Family Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/family-nurse-practitioner-msn/ |
| 4 | Neonatal Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/neonatal-np-msn/ |
| 5 | Nurse-Midwifery, MSN | MSN | https://catalog.upenn.edu/graduate/programs/nurse-midwifery-msn/ |
| 6 | Nursing & Healthcare Leadership, MSN | MSN | https://catalog.upenn.edu/graduate/programs/nursing-and-healthcare-leadership-msn/ |
| 7 | Pediatric Acute Care Nurse Practitioner: Acute/Chronic, MSN | MSN | https://catalog.upenn.edu/graduate/programs/pediatric-acute-care-np-acute-chronic-msn/ |
| 8 | Pediatric Acute Care Nurse Practitioner: Critical Care, MSN | MSN | https://catalog.upenn.edu/graduate/programs/pediatric-acute-care-np-critical-care-msn/ |
| 9 | Pediatric Acute Care Nurse Practitioner: Oncology, MSN | MSN | https://catalog.upenn.edu/graduate/programs/pediatric-acute-care-np-oncology-msn/ |
| 10 | Pediatric Primary Care Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/pediatric-primary-care-np-msn/ |
| 11 | Psychiatric Mental Health Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/psychiatric-mental-health-np-msn/ |
| 12 | Women's Health/Gender Related Nurse Practitioner, MSN | MSN | https://catalog.upenn.edu/graduate/programs/womens-health-gender-related-np-msn/ |

##### Certificate (5)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Adult Oncology Specialty, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/adult-oncology-specialist-certificate/ |
| 2 | Nutrition, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/nutrition-certificate/ |
| 3 | Palliative Care, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/palliative-care-certificate/ |
| 4 | Quality Improvement & Safety Processes Healthcare, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/quality-improvement-safety-processes-healthcare-certificate/ |
| 5 | Transformative Nursing Education Program, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/transformative-nursing-education-program-certificate/ |

##### Minor (5)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Adult Oncology Specialty, Minor | MINOR | https://catalog.upenn.edu/graduate/programs/adult-oncology-specialist-minor/ |
| 2 | Global Health, Minor | MINOR | https://catalog.upenn.edu/graduate/programs/global-health-minor/ |
| 3 | Nutrition, Minor | MINOR | https://catalog.upenn.edu/graduate/programs/nutrition-minor/ |
| 4 | Palliative Care, Minor | MINOR | https://catalog.upenn.edu/graduate/programs/palliative-care-minor/ |
| 5 | Quality Improvement & Safety Processes Healthcare, Minor | MINOR | https://catalog.upenn.edu/graduate/programs/quality-improvement-safety-processes-healthcare-minor/ |

##### DNP (3)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Executive Leadership, DNP | DNP | https://catalog.upenn.edu/graduate/programs/executive-leadership-dnp/ |
| 2 | Nurse Anesthesia Program, DNP | DNP | https://catalog.upenn.edu/graduate/programs/nurse-anesthesia-program-dnp/ |
| 3 | Systems Leadership, DNP | DNP | https://catalog.upenn.edu/graduate/programs/systems-leadership-dnp/ |

##### MPN (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nursing, MPN | MPN | https://catalog.upenn.edu/graduate/programs/nursing-mpn/ |

##### PhD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nursing, PhD | PHD | https://catalog.upenn.edu/graduate/programs/nursing-phd/ |

##### MSNS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nutrition Science, MSNS | MSNS | https://catalog.upenn.edu/graduate/programs/nutrition-science-msns/ |

#### Stuart Weitzman School of Design

##### Certificate (10)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Ecological Architecture, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/ecological-architecture-certificate/ |
| 2 | Ecological Planning, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/ecological-planning-certificate/ |
| 3 | Energy Management & Policy, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/energy-management-policy-certificate/ |
| 4 | Environmental Building Design, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/environmental-building-design-certificate/ |
| 5 | Geographical Information Systems & Spatial Analysis, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/geo-info-systems-spatial-analysis-certificate/ |
| 6 | Historic Preservation, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/historic-preservation-certificate/ |
| 7 | Landscape Studies, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/landscape-studies-certificate/ |
| 8 | Time-Based and Interactive Media, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/time-based-interactive-media-certificate/ |
| 9 | Urban Design, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/urban-design-certificate/ |
| 10 | Urban Resilience, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/urban-resilience-certificate/ |

##### MSD (5)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Architecture, MSD: Advanced Architectural Design | MSD | https://catalog.upenn.edu/graduate/programs/architecture-advanced-architectural-design-msd/ |
| 2 | Architecture, MSD: Environmental Building Design | MSD | https://catalog.upenn.edu/graduate/programs/architecture-environmental-building-design-msd/ |
| 3 | Architecture, MSD: Property Development and Design | MSD | https://catalog.upenn.edu/graduate/programs/architecture-property-development-design-msd/ |
| 4 | Architecture, MSD: Robotics and Autonomous Systems | MSD | https://catalog.upenn.edu/graduate/programs/architecture-robotics-autonomous-systems-msd/ |
| 5 | Historic Preservation, MSD | MSD | https://catalog.upenn.edu/graduate/programs/historic-preservation-msd/ |

##### PhD (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Architecture, PhD | PHD | https://catalog.upenn.edu/graduate/programs/architecture-phd/ |
| 2 | City & Regional Planning, PhD | PHD | https://catalog.upenn.edu/graduate/programs/city-planning-phd/ |

##### MArch (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Architecture, MArch | MARCH | https://catalog.upenn.edu/graduate/programs/architecture-march/ |

##### MEBD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Architecture, MEBD | MEBD | https://catalog.upenn.edu/graduate/programs/architecture-mebd/ |

##### MS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Architecture, MS | MS | https://catalog.upenn.edu/graduate/programs/architecture-ms/ |

##### MCP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | City & Regional Planning, MCP | MCP | https://catalog.upenn.edu/graduate/programs/city-and-regional-planning-mcp/ |

##### MFA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Fine Arts, MFA | MFA | https://catalog.upenn.edu/graduate/programs/fine-arts-mfa/ |

##### MSHP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Historic Preservation, MSHP | MSHP | https://catalog.upenn.edu/graduate/programs/historic-preservation-mshp/ |

##### MLA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Landscape Architecture & Regional Planning, MLA | MLA | https://catalog.upenn.edu/graduate/programs/landscape-architecture-regional-planning-mla/ |

##### MUSA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Urban Spatial Analytics, MUSA | MUSA | https://catalog.upenn.edu/graduate/programs/urban-spatial-analytics-musa/ |

#### Perelman School of Medicine

##### PhD (13)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Biochemistry, Biophysics and Chemical Biology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/biochemistry-biophysics-chemical-biology-phd/ |
| 2 | Cell and Molecular Biology, PhD: Cancer Biology | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-cancer-biology-phd/ |
| 3 | Cell and Molecular Biology, PhD: Cell Biology, Physiology, and Metabolism | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-cell-biology-physiology-metabolism-phd/ |
| 4 | Cell and Molecular Biology, PhD: Developmental, Stem Cell, and Regenerative Biology | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-developmental-stem-cell-regenerative-biology-phd/ |
| 5 | Cell and Molecular Biology, PhD: Gene Therapy and Vaccines | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-gene-therapy-vaccines-phd/ |
| 6 | Cell and Molecular Biology, PhD: Genetics and Epigenetics | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-genetics-epigenetics-phd/ |
| 7 | Cell and Molecular Biology, PhD: Microbiology, Virology, and Parasitology | PHD | https://catalog.upenn.edu/graduate/programs/cell-molecular-biology-microbiology-virology-parasitology-phd/ |
| 8 | Epidemiology and Biostatistics, PhD: Biostatistics | PHD | https://catalog.upenn.edu/graduate/programs/epidemiology-biostatistics-biostatistics-phd/ |
| 9 | Epidemiology and Biostatistics, PhD: Epidemiology | PHD | https://catalog.upenn.edu/graduate/programs/epidemiology-biostatistics-epidemiology-phd/ |
| 10 | Genomics and Computational Biology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/genomics-computational-biology-phd/ |
| 11 | Immunology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/immunology-phd/ |
| 12 | Neuroscience, PhD | PHD | https://catalog.upenn.edu/graduate/programs/neuroscience-phd/ |
| 13 | Pharmacology, PhD | PHD | https://catalog.upenn.edu/graduate/programs/pharmacology-phd/ |

##### Certificate (12)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Advanced Research Training for Genetic Counselors, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/advanced-research-training-genetic-counselors-certificate/ |
| 2 | Biomedical Informatics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/biomedical-informatics-certificate/ |
| 3 | Clinical Ethics Mediation, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/clinical-ethics-mediation-certificate/ |
| 4 | Health Care and Technology, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/health-care-technology-certificate/ |
| 5 | Health Care Innovation, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/health-care-innovation-certificate/ |
| 6 | Healthcare Quality and Safety, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/health-care-quality-safety-certificate/ |
| 7 | Implementation Science, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/implementation-science-certificate/ |
| 8 | Medical Physics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/medical-physics-certificate/ |
| 9 | Regulatory Affairs, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/regulatory-affairs-certificate/ |
| 10 | Translational Research, Certificate: Entrepreneurial Science | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/translational-research-entrepreneurial-science-certificate/ |
| 11 | Translational Research, Certificate: Regulatory Science | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/translational-research-regulatory-science-certificate/ |
| 12 | Translational Research, Certificate: Translational Science | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/translational-research-translational-science-certificate/ |

##### MBE (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Bioethics, MBE | MBE | https://catalog.upenn.edu/graduate/programs/bioethics-mbe/ |

##### MSBMI (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Biomedical Informatics, MSBMI | MSBMI | https://catalog.upenn.edu/graduate/programs/biomedical-informatics-msbmi/ |

##### MS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Biostatistics, MS | MS | https://catalog.upenn.edu/graduate/programs/epidemiology-biostatistics-biostatistics-ms/ |

##### MSCE (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Clinical Epidemiology, MSCE | MSCE | https://catalog.upenn.edu/graduate/programs/clinical-epidemiology-msce/ |

##### MCI (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Clinical Informatics, MCI | MCI | https://catalog.upenn.edu/graduate/programs/clinical-informatics-mci/ |

##### MD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Doctor of Medicine, MD | MD | https://catalog.upenn.edu/graduate/programs/doctor-medicine-md/ |

##### MSGC (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Genetic Counseling, MSGC | MSGC | https://catalog.upenn.edu/graduate/programs/genetic-counseling-msgc/ |

##### MHCI (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Health Care Innovation, MHCI | MHCI | https://catalog.upenn.edu/graduate/programs/health-care-innovation-mhci/ |

##### MSHP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Health Policy Research, MSHP | MSHP | https://catalog.upenn.edu/graduate/programs/health-policy-research-mshp/ |

##### MHQS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Healthcare Quality and Safety, MHQS | MHQS | https://catalog.upenn.edu/graduate/programs/healthcare-quality-safety-mhqs/ |

##### MSME (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Medical Ethics, MSME | MSME | https://catalog.upenn.edu/graduate/programs/medical-ethics-msme/ |

##### MMP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Medical Physics, MSMP | MMP | https://catalog.upenn.edu/graduate/programs/medical-physics-mmp/ |

##### MPH (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Public Health, MPH | MPH | https://catalog.upenn.edu/graduate/programs/public-health-mph/ |

##### MRA (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Regulatory Affairs, MRA | MRA | https://catalog.upenn.edu/graduate/programs/regulatory-affairs-mra/ |

##### MSRS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Regulatory Science, MSRS | MSRS | https://catalog.upenn.edu/graduate/programs/regulatory-science-msrs/ |

##### MSTR (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Translational Research, MSTR | MSTR | https://catalog.upenn.edu/graduate/programs/translational-research-mstr/ |

#### Graduate School of Education

##### MEd (22)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Education Entrepreneurship, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/educational-entrepreneurship-msed/ |
| 2 | Education Policy, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/education-policy-msed/ |
| 3 | Education Studies, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/education-studies-msed/ |
| 4 | Education, Culture, and Society, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/education-culture-society-msed/ |
| 5 | Global Higher Education Management, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/global-higher-education-management-msed/ |
| 6 | Higher Education, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/higher-education-msed/ |
| 7 | Independent School Teaching Residency, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/independent-school-teaching-residency-msed/ |
| 8 | Interdisciplinary Studies in Human Development, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/interdisciplinary-studies-human-development-msed/ |
| 9 | International Educational Development, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/international-educational-development-msed/ |
| 10 | Language, Globalization and Intercultural Studies, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/language-globalization-intercultural-studies-msed/ |
| 11 | Learning Analytics and Artificial Intelligence, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/learning-analytics-artificial-intelligence-msed/ |
| 12 | Learning Sciences and Technologies, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/learning-sciences-technologies-msed/ |
| 13 | Literacy Studies, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/literacy-studies-msed/ |
| 14 | Medical Education, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/medical-education-msed/ |
| 15 | School and Mental Health Counseling, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/school-mental-health-counseling-msed/ |
| 16 | School Leadership, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/school-leadership-msed/ |
| 17 | Statistics, Measurement, Assessment, and Research Technology, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/statistics-measurement-assessment-research-technology-msed/ |
| 18 | Teaching English to Speakers of Other Languages, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/tesol-msed/ |
| 19 | Teaching, Learning, and Leadership, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/teaching-learning-leadership-msed/ |
| 20 | Urban Education, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/urban-education-msed/ |
| 21 | Urban Teaching Apprenticeship, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/urban-teaching-apprenticeship-msed/ |
| 22 | Urban Teaching Residency, MSEd | MSED | https://catalog.upenn.edu/graduate/programs/urban-teaching-residency-msed/ |

##### PhD (9)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Education Policy, PhD | PHD | https://catalog.upenn.edu/graduate/programs/education-policy-phd/ |
| 2 | Education, Culture, and Society, PhD | PHD | https://catalog.upenn.edu/graduate/programs/education-culture-society-phd/ |
| 3 | Educational Linguistics, PhD | PHD | https://catalog.upenn.edu/graduate/programs/educational-linguistics-phd/ |
| 4 | Higher Education, PhD | PHD | https://catalog.upenn.edu/graduate/programs/higher-education-phd/ |
| 5 | Interdisciplinary Studies in Human Development, PhD | PHD | https://catalog.upenn.edu/graduate/programs/interdisciplinary-studies-human-development-phd/ |
| 6 | Learning Sciences & Technologies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/learning-sciences-technologies-phd/ |
| 7 | Literacy Studies, PhD | PHD | https://catalog.upenn.edu/graduate/programs/literacy-studies-phd/ |
| 8 | Quantitative Methods, PhD | PHD | https://catalog.upenn.edu/graduate/programs/quantitative-methods-phd/ |
| 9 | Teaching, Learning, and Teacher Education, PhD | PHD | https://catalog.upenn.edu/graduate/programs/teaching-learning-teacher-education-phd/ |

##### EdD (8)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Educational and Organizational Leadership, EdD | EDD | https://catalog.upenn.edu/graduate/programs/educational-organizational-leadership-edd/ |
| 2 | Educational Leadership, EdD | EDD | https://catalog.upenn.edu/graduate/programs/educational-leadership-edd/ |
| 3 | Educational Linguistics, EdD | EDD | https://catalog.upenn.edu/graduate/programs/educational-linguistics-edd/ |
| 4 | Higher Education Management, EdD | EDD | https://catalog.upenn.edu/graduate/programs/higher-education-management-edd/ |
| 5 | Higher Education, EdD | EDD | https://catalog.upenn.edu/graduate/programs/higher-education-edd/ |
| 6 | Literacy Studies, EdD | EDD | https://catalog.upenn.edu/graduate/programs/literacy-studies-edd/ |
| 7 | Penn Chief Learning Officer, EdD | EDD | https://catalog.upenn.edu/graduate/programs/penn-chief-learning-officer-edd/ |
| 8 | Teaching, Learning, and Teacher Education, EdD | EDD | https://catalog.upenn.edu/graduate/programs/teaching-learning-teacher-education-edd/ |

##### Certification (3)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | ESL Specialist, Certification | CERTIFICATION | https://catalog.upenn.edu/graduate/programs/esl-specialist-certification/ |
| 2 | Reading Specialist, Certification | CERTIFICATION | https://catalog.upenn.edu/graduate/programs/reading-specialist-certification/ |
| 3 | School Leadership, Certification | CERTIFICATION | https://catalog.upenn.edu/graduate/programs/school-leadership-certification/ |

##### MPhil (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Professional Counseling, MPhilEd | MPHILED | https://catalog.upenn.edu/graduate/programs/professional-counseling-mphiled/ |
| 2 | Quantitative Methods, MPhilEd | MPHILED | https://catalog.upenn.edu/graduate/programs/quantitative-methods-mphiled/ |

#### Penn Carey Law School

##### LLM (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Law, LLCM | LLCM | https://catalog.upenn.edu/graduate/programs/law-llcm/ |
| 2 | Law, LLM | LLM | https://catalog.upenn.edu/graduate/programs/law-llm/ |

##### JD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Law, JD | JD | https://catalog.upenn.edu/graduate/programs/law-jd/ |

##### ML (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Law, ML | ML | https://catalog.upenn.edu/graduate/programs/law-ml/ |

##### SJD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Law, SJD | SJD | https://catalog.upenn.edu/graduate/programs/law-sjd/ |

#### School of Dental Medicine

##### Certificate (9)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Endodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/endodontics-certificate/ |
| 2 | Oral and Maxillofacial Surgery, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/oral-maxillofacial-surgery-certificate/ |
| 3 | Oral Medicine, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/oral-medicine-certificate/ |
| 4 | Orthodontics and Periodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/orthodontics-periodontics-certificate/ |
| 5 | Orthodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/orthodontics-certificate/ |
| 6 | Pediatric Dentistry, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/pediatric-dentistry-certificate/ |
| 7 | Periodontics and Prosthodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/periodontal-prosthesis-certificate/ |
| 8 | Periodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/periodontics-certificate/ |
| 9 | Prosthodontics, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/prosthodontics-certificate/ |

##### DMD (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Doctor of Dental Medicine, DMD | DMD | https://catalog.upenn.edu/graduate/programs/doctor-dental-medicine-dmd/ |
| 2 | Program for Advanced Standing Students, DMD | DMD | https://catalog.upenn.edu/graduate/programs/pass-dmd/ |

##### MADS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Advanced Dental Studies, MADS | MADS | https://catalog.upenn.edu/graduate/programs/advanced-dental-studies-mads/ |

##### ScD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Doctor of Science in Dentistry, DScD | DSCD | https://catalog.upenn.edu/graduate/programs/doctor-science-dentistry-dscd/ |

##### MSOPH (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Oral and Population Health, MSOPH | MSOPH | https://catalog.upenn.edu/graduate/programs/oral-population-health-msoph/ |

##### MSOB (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Oral Biology, MSOB | MSOB | https://catalog.upenn.edu/graduate/programs/oral-biology-msob/ |

##### MOHS (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Oral Health Sciences, MOHS | MOHS | https://catalog.upenn.edu/graduate/programs/oral-health-sciences-mohs/ |

#### School of Veterinary Medicine

##### Certificate (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Animal Welfare and Behavior, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/animal-welfare-behavior-certificate/ |
| 2 | One Health, Certificate | CERTIFICATE | https://catalog.upenn.edu/graduate/programs/one-health-certificate/ |

##### MSAWB (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Animal Welfare and Behavior, MSAWB | MSAWB | https://catalog.upenn.edu/graduate/programs/animal-welfare-behavior-msawb/ |

##### VMD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Veterinary Medicine, VMD | VMD | https://catalog.upenn.edu/graduate/programs/veterinary-medicine-vmd/ |

#### School of Social Policy & Practice

##### MSSP (2)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Social Policy + Data Analytics, MSSP | MSSP | https://catalog.upenn.edu/graduate/programs/social-policy-data-analytics-mssp/ |
| 2 | Social Policy, MSSP | MSSP | https://catalog.upenn.edu/graduate/programs/social-policy-mssp/ |

##### DNP (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nonprofit Administration, DNPA | DNPA | https://catalog.upenn.edu/graduate/programs/nonprofit-administration-dnpa/ |

##### MSNPL (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Nonprofit/NGO Leadership, MSNPL | MSNPL | https://catalog.upenn.edu/graduate/programs/nonprofit-ngo-leadership-msnpl/ |

##### PhD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Social Welfare, PhD | PHD | https://catalog.upenn.edu/graduate/programs/social-welfare-phd/ |

##### DSW (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Social Work, DSW | DSW | https://catalog.upenn.edu/graduate/programs/social-work-dsw/ |

##### MSW (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Social Work, MSW | MSW | https://catalog.upenn.edu/graduate/programs/social-work-msw/ |

#### Annenberg School for Communication

##### MCMI (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Communication and Media Industries, MCMI | MCMI | https://catalog.upenn.edu/graduate/programs/communication-media-industries-mcmi/ |

##### PhD (1)

| # | 专业/项目 | official | URL |
|---|------|---------|-----|
| 1 | Communication, PhD | PHD | https://catalog.upenn.edu/graduate/programs/communication-phd/ |


### 2.2 Worked deep-dive — Wharton Doctoral Programs (PhD)

The Wharton School's doctoral programs (9 PhD fields + an Accounting/Finance/Marketing/etc. spread) are administered centrally through [doctoral.wharton.upenn.edu](https://doctoral.wharton.upenn.edu/admissions/):

| Field | Value |
|-------|-------|
| Office | Wharton Doctoral Programs, doctoral-admissions@wharton.upenn.edu |
| Application portal | [doctoral.wharton.upenn.edu/admissions/](https://doctoral.wharton.upenn.edu/admissions/) |
| Application deadline | **December 15, 11:59 p.m. ET** (Source: E-G-001) |
| Standardized test | GRE or GMAT required (Source: E-G-001) |
| Application fee | (See Wharton Doctoral site — P0 follow-up for exact current figure) |
| Funding | All admitted PhDs fully funded (tuition + stipend) — standard for top doctoral programs |
| ETS code | 2926 (institutional) |

Behind-the-accordion detail: each Wharton doctoral field's requirements, faculty contacts, and sample plans of study live on the field-specific page (e.g. [doctoral.wharton.upenn.edu/programs-of-study/accounting/](https://doctoral.wharton.upenn.edu/programs-of-study/accounting/)) and on the catalog detail page (`/graduate/programs/<field>-phd/`).

### 2.3 Graduate admissions model — DECENTRALIZED

Penn has **no central graduate application**. Each of the 12 graduate/professional schools runs its own admissions office, application, deadline, fee, and GRE/ELP policy. The catalog program detail pages carry curriculum and plan-of-study only — never admissions requirements. Key entry points:

| School | Admissions entry point | Representative deadline |
|--------|------------------------|-------------------------|
| SAS Graduate Division (administers all SAS-affiliated graduate groups, ~80 programs) | [sas.upenn.edu/graduate-division/prospective-students](https://www.sas.upenn.edu/graduate-division/prospective-students/admissions-faq) | PhD deadlines start **Dec 8** (program-specific) |
| Perelman School of Medicine — Biomedical Graduate Studies (BGS) | [med.upenn.edu/bgs](https://www.med.upenn.edu/bgs/) | Early Dec (program-specific) |
| Wharton Doctoral | [doctoral.wharton.upenn.edu/admissions](https://doctoral.wharton.upenn.edu/admissions/) | **Dec 15** |
| Wharton MBA | [mba.wharton.upenn.edu](https://mba.wharton.upenn.edu/) | Round-based (Sep/Oct/Jan) |
| Penn Engineering Graduate (SEAS) | [graduate.admissions.seas.upenn.edu](https://graduate.admissions.seas.upenn.edu/) | Rolling / program-specific |
| Penn Nursing Graduate | [nursing.upenn.edu/academics/graduate-programs](https://www.nursing.upenn.edu/) | Program-specific |
| Penn GSE | [gse.upenn.edu](https://www.gse.upenn.edu/) | Program-specific |
| Weitzman School of Design | [design.upenn.edu](https://www.design.upenn.edu/) | Mid-Dec to mid-Jan |
| Penn Carey Law (JD) | [law.upenn.edu/admissions](https://www.law.upenn.edu/admissions) | LSAC-driven |
| Penn Dental | [dental.upenn.edu](https://www.dental.upenn.edu/) | ADEA AADSAS-driven |
| Penn Vet | [vet.upenn.edu](https://www.vet.upenn.edu/) | VMCAS-driven |
| SP2 | [sp2.upenn.edu](https://www.sp2.upenn.edu/) | Program-specific |
| Annenberg (PhD) | [asc.upenn.edu](https://www.asc.upenn.edu/) | Dec |

> ETS institutional code **2926** (GRE + TOEFL). SAS Graduate Division accepts **IELTS in lieu of TOEFL**; many programs no longer require the GRE (check each program). GRE valid 5 yrs, TOEFL 2 yrs. (Source: E-G-002)

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Dimension | Value | Source |
|-----------|-------|--------|
| Admissions site | admissions.upenn.edu | E-U-002 |
| Application portal | Common App / Coalition / QuestBridge (one only per cycle) | E-U-002 |
| Early Decision deadline | **Nov 1, 2025** (binding; mid-Dec decision) | E-U-001 |
| Regular Decision deadline | **Jan 5, 2026** (early-April decision) | E-U-001 |
| Enrollment confirmation | May 1 (standard NACAC reply date) | — |
| Financial-aid deadline | Concurrent with admission (CSS Profile + tax returns; FAFSA for domestic) | E-U-006 |
| SAT/ACT policy | **REQUIRED for 2025-26** (hardship waiver available; not test-optional). No minimum score. | E-U-004 |
| Superscore policy | Yes — highest EBRW + Math combined across sittings (SAT); highest English/Math/Reading (ACT, Science optional) | E-U-004 |
| Score-report method | Self-report at application; official prior to enrollment (recruited athletes must submit official) | E-U-004 |
| Latest SAT test date | Nov 2025 (ED) / Dec 2025 (RD) / Mar 2026 | E-U-004 |
| Latest ACT test date | Oct 2025 (ED) / Dec 2025 (RD) / Feb 2026 | E-U-004 |
| Interview policy | Not offered as part of the standard review (no alumni interview required for decision) | — |
| Recommendations | 1 counselor + 1 core-subject teacher; 1 optional additional | E-U-005 |
| Portfolios / supplementary | Optional supplementary materials for specific talents (art/music/research); required for some specialized programs | E-U-005 |
| Transfer pathway | Separate transfer application; international transfers can apply but note: intl transfer students are typically NOT eligible for institutional financial aid (verify each cycle — P1) | — |
| QuestBridge | National College Match partner (College Match Finalists + non-finalists) | E-U-002 |

### 3.2 Undergraduate English proficiency table

> **Applicability:** Required if (a) English is NOT your native language AND (b) English has NOT been your primary language of instruction throughout high school. If either is true → proficient, no test needed. Penn does **NOT** accept IELTS Indicator or TOEFL MyBest. Scores valid 2 years. Penn does **NOT** accept self-reported proficiency scores — must be official from the testing agency.

| Exam | Competitive threshold | Penn notes |
|------|----------------------|------------|
| **TOEFL iBT** | **100+** composite (consistent across 4 sections) | Most recent exam, NOT MyBest; code 2926 |
| **IELTS Academic** | **7.0+** overall band (consistent across 4 sections) | — |
| **Duolingo English Test (DET)** | **130+** overall (consistent across subsections) | — |

(Source: E-U-007)

### 3.3 Graduate — global rules

| Dimension | Value |
|-----------|-------|
| Admissions model | **Decentralized** — no central grad application; each of 12 schools runs own process (§2.3) |
| Application platforms | School-specific (SAS uses Penn's online application; Law uses LSAC; Med uses AMCAS; Dental uses ADEA AADSAS; Vet uses VMCAS; Wharton MBA uses own) |
| Standard application fee | Varies by school (~$70–$120); SAS Graduate Division ~$90 |
| April-15-equivalent honor date | Penn is a CGS Resolution signatory (April 15) — standard for funded PhD offers |
| GRE/GMAT policy | Program-specific; many SAS/SEAS PhD programs no longer require GRE; Wharton Doctoral requires GRE or GMAT (E-G-001) |
| Language-test policy | TOEFL or IELTS required of non-native English speakers (some programs accept DET — check each). SAS accepts IELTS in lieu of TOEFL (E-G-002) |
| Exemption rules | Native English speaker; or English as primary language of instruction (UG rule); grad programs may set stricter per-program rules |
| Application timeline | PhD deadlines typically **Dec 1–15**; master's deadlines range Dec–Mar; professional schools (Law/Med/Dental/Vet) follow national application cycles |
| Institutional test codes | ETS institutional code **2926** (GRE, TOEFL, SAT); ACT 3732 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-27 academic year, line-itemized)

> Source: [srfs.upenn.edu/costs-budgeting/undergraduate-cost-attendance](https://srfs.upenn.edu/costs-budgeting/undergraduate-cost-attendance) (E-U-008) and [undergraduate-tuition-and-fees](https://srfs.upenn.edu/costs-budgeting/undergraduate-tuition-and-fees) (E-U-009).

| Expense item | Living on campus | Living off campus | Living with family | Description |
|--------------|------------------|-------------------|--------------------|-------------|
| Tuition | $65,670* | $65,670* | $65,670* | Billed |
| Fees (General $6,620 + Tech $918 + Clinical $770) | $8,308* | $8,308* | $8,308* | Billed |
| Housing | $13,644* | $12,978 | $0 | Billed only if on-campus |
| Food | $6,960* | $5,988 | $2,394 | Billed only if on-campus meal plan |
| Books and Supplies | $1,412 | $1,412 | $1,412 | Indirect (not billed) |
| Transportation | $1,080 | $1,080 | $1,756 | Indirect |
| Personal Expenses | $2,008 | $2,008 | $2,008 | Indirect |
| **Total Cost of Attendance** | **$99,082** | **$97,444** | **$81,548** | — |

> * = direct/billed. The fee breakdown: Tuition $65,670 + General Fee $6,620 + Technology Fee $918 + Clinical Fee $770 = **$73,978 total tuition + fees (2026-27)**. For comparison, 2025-26 totals were $95,612 on-campus (tuition $63,204, fees $8,032).

### 4.2 Undergraduate financial-aid policy

| Policy | Value | Source |
|--------|-------|--------|
| Aid philosophy | **Need-based only** (no merit scholarships); grants + work-study, **no loans** in aid packages | E-U-010 |
| Meets demonstrated need | **Yes — 100% of demonstrated need for all 8 semesters** | E-U-010 |
| Need-blind (US citizens & permanent residents) | **Yes** | E-U-011 |
| Need-blind (Canada & Mexico citizens) | **Yes** (treated same as domestic for aid consideration) | E-U-011 |
| Need-aware (other internationals) | **Yes** — family ability to pay factors into admission; but admitted intl get 100% need met | E-U-011 |
| Income ≤ $75,000 (typical assets) | **All billed expenses covered** (tuition + fees + housing + food) + laptop funding, summer course/research funding, etc. | E-U-012 |
| Income up to $200,000 (typical assets) | Aid package covers **at minimum full tuition** (often more) | E-U-012 |
| Avg aid package (2023-24) | $66,222 need-based ($69,990 incl. all undergrads) — exceeds tuition | E-U-010 |
| % receiving aid | ~46% of undergraduates | E-U-010 |
| Application forms | CSS Profile + federal tax returns (all); + FAFSA (domestic); + Penn Canadian Citizen App (Canadians) | E-U-006 |
| International aid timing | Must apply for aid **at the same time as admission**; late requests cannot be considered; aid decision binds all 4 years | E-U-011 |

### 4.3 Graduate cost & funding framework

Graduate cost-of-attendance is **per-school** — SRFS publishes per-program budgets at [srfs.upenn.edu/costs-budgeting/graduate-cost-attendance](https://srfs.upenn.edu/costs-budgeting/graduate-cost-attendance) (each of the 12 schools has its own sub-page). Funding models by degree type:

| Track | Typical funding | Notes |
|-------|----------------|-------|
| PhD (SAS, SEAS, Wharton, PSOM-BGS, GSE, Weitzman, Annenberg) | **Fully funded** — full tuition + stipend + health insurance via fellowships, RA/TA | Standard for funded PhD; ~5-year packages |
| Professional doctorates (MD, DMD, VMD, JD) | Mostly self-funded (loans/scholarships); some need-based grants | MD/DMD/VMD/JD do not guarantee full funding |
| Master's / professional master's | Mostly **self-funded** (tuition-paying); limited partial scholarships | MA/MS/MBA/MSE/MSEd/MSN/etc. |
| Certificates | Self-funded | — |

> Application fees and fee-waiver policies vary by school; check each school's admissions page (§2.3). Stipend rates and living-expense budgets are published per-program on the SRFS graduate COA sub-pages (P0 follow-up to capture the full per-school table).

---

## SECTION 5 — Evidence chain index

```yaml
- id: E-U-001
  field: undergraduate.deadlines.ED_and_RD
  value: { ED: "2025-11-01", RD: "2026-01-05", ED_notification: "December", RD_notification: "April" }
  source_url: https://admissions.upenn.edu/how-to-apply/first-year-applicants
  source_snippet: "Our Early Decision application deadline is November 1, 2025, and applicants are notified of our decision in December. … Our Regular Decision application deadline is January 5, 2026, and applicants are notified of our decision in April."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-002
  field: undergraduate.application.platforms
  value: ["Common App", "Coalition App", "QuestBridge"]
  source_url: https://admissions.upenn.edu/how-to-apply/first-year-applicants
  source_snippet: "You can apply to Penn through the Common App, Coalition App, or through QuestBridge."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-003
  field: undergraduate.application.fee
  value: 75  # USD; fee waiver available
  source_url: https://admissions.upenn.edu/how-to-apply/first-year-applicants/application-requirements
  source_snippet: "The application fee to apply to Penn is $75. If paying the application fee is a significant financial burden for you and your family, please request an application fee waiver through either your Common App or the Coalition Application in the 'fee waiver' section."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-004
  field: undergraduate.testing.policy_and_codes
  value: { policy: "SAT or ACT REQUIRED for 2025-26", waiver: "available for hardship", SAT_code: 2926, ACT_code: 3732, TOEFL_code: 2926, latest_sat_ED: "Nov 2025", latest_sat_RD: "Dec 2025", superscore: true }
  source_url: https://admissions.upenn.edu/how-to-apply/preparing-your-application/testing
  source_snippet: "Penn applicants are required to submit the SAT or ACT for the 2025-26 application cycle. Applicants who face hardship in meeting this requirement can submit a waiver instead. … SAT: 2926 / ACT: 3732 / TOEFL: 2926."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-005
  field: undergraduate.application.materials
  value: { essays: "3 Penn-specific short answers + school-specific prompt", recommendations: "1 counselor + 1 core-subject teacher + 1 optional", transcript: "official high school + School Report" }
  source_url: https://admissions.upenn.edu/how-to-apply/first-year-applicants/application-requirements
  source_snippet: "Students will be asked to respond to the three following prompts in their application to Penn … you will need to request recommendation letters from two people: your school counselor or college official; a teacher in a core subject area …"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-006
  field: undergraduate.financial_aid.forms
  value: ["CSS Profile (all)", "Federal tax returns (all)", "FAFSA (domestic only)"]
  source_url: https://admissions.upenn.edu/affording-penn/how-it-works
  source_snippet: "All financial aid applicants need to submit: CSS Profile; Federal Tax Returns or Tax Return/Income Statement from your country. If you are a domestic student … you will also need to submit: FAFSA."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-007
  field: undergraduate.elp.competitive_thresholds
  value: { TOEFL_iBT: 100, IELTS: 7.0, DET: 130, accepted_exams: ["TOEFL", "IELTS", "Duolingo"], rejected: ["IELTS Indicator", "TOEFL MyBest"], self_reported_accepted: false }
  source_url: https://admissions.upenn.edu/how-to-apply/international-applicants
  source_snippet: "Competitive applicants tend to have a composite score of 100 or above [TOEFL] … overall band score of 7 or above [IELTS] … overall score of 130 or above [Duolingo]. … Penn does not currently accept the IELTS Indicator exam or MyBest scores for the TOEFL."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-008
  field: undergraduate.cost.coa_2026_2027
  value: { tuition: 65670, fees: 8308, housing_on_campus: 13644, food_on_campus: 6960, books: 1412, transportation: 1080, personal: 2008, total_on_campus: 99082, total_off_campus: 97444, total_with_family: 81548 }
  source_url: https://srfs.upenn.edu/costs-budgeting/undergraduate-cost-attendance
  source_snippet: "2026-2027 Academic Year | Tuition $65,670* | Fees $8,308* | Housing $13,644* | Food $6,960* | Books and Supplies $1,412 | Transportation $1,080 | Personal Expenses $2,008 | Total Budget $99,082"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-009
  field: undergraduate.cost.tuition_fees_breakdown_2026_2027
  value: { tuition: 65670, general_fee: 6620, technology_fee: 918, clinical_fee: 770, total_tuition_and_fees: 73978 }
  source_url: https://srfs.upenn.edu/costs-budgeting/undergraduate-tuition-and-fees
  source_snippet: "2026-2027 Tuition and Fees | Tuition $65,670 | General Fee $6,620 | Technology Fee $918 | Clinical Fee $770 | Total Tuition and Fees $73,978"
  capture_date: 2026-07-05
  evidence_type: official_webpage_table

- id: E-U-010
  field: undergraduate.financial_aid.policy
  value: { need_based_only: true, no_loans: true, meets_full_need: true, four_year_commitment: true, avg_package_2023_24: 66222, pct_receiving_aid: 46 }
  source_url: https://admissions.upenn.edu/affording-penn/how-it-works
  source_snippet: "Penn meets 100% of demonstrated financial need with grants, scholarships, and work-study funding. … 46% of undergraduate students received need-based financial aid in 2023-2024, with an average package of $66,222."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-011
  field: undergraduate.financial_aid.international_policy
  value: { need_blind_us_citizens_permanent_residents: true, need_blind_canada_mexico: true, need_aware_other_international: true, meets_full_need_admitted_intl: true, intl_must_apply_at_admission_time: true }
  source_url: https://admissions.upenn.edu/affording-penn/international-aid
  source_snippet: "Penn is need-aware for international applicants, who are defined as non-citizens, and non-permanent residents of the United States, Canada, and Mexico. This means a family's ability to pay does factor into admissions decisions. … International students admitted as financial aid recipients will receive need-based aid that covers 100% of their demonstrated need, just like domestic students. … Requests for financial aid after being admitted as an international student cannot be considered."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-012
  field: undergraduate.financial_aid.income_thresholds
  value: { full_billed_expenses_covered_at_income: 75000, at_least_full_tuition_covered_at_income: 200000, typical_assets_required: true }
  source_url: https://admissions.upenn.edu/affording-penn/understanding-your-costs
  source_snippet: "Students with family incomes less than $75,000* receive financial aid packages guaranteed to cover all billed expenses (tuition and fees, housing, and dining) … Students with family incomes up to $200,000* who are eligible for aid receive a financial aid package that is guaranteed to cover at minimum full tuition (and often more)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-013
  field: undergraduate.programs.directory
  value: { catalog_url: "https://catalog.upenn.edu/programs/", total_program_rows: 641, ug_majors: 202, ug_minors: 101, ug_certs_prep: 16, grad_degrees: 264, grad_certs: 53, grad_minors: 5 }
  source_url: https://catalog.upenn.edu/programs/
  source_snippet: "Programs A-Z — 2026-27 University Catalog (641 program-degree rows: 319 UG + 322 grad). Each link text encodes program name + degree tag + level + mode + degree category + school."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-014
  field: undergraduate.structure.four_schools
  value: ["College of Arts and Sciences (within SAS)", "School of Engineering and Applied Science (Penn Engineering)", "The Wharton School", "School of Nursing"]
  source_url: https://admissions.upenn.edu/academics/four-schools
  source_snippet: "Exploring academics at Penn starts with picking a home base in one of four undergraduate schools. … you apply to one of our four undergraduate schools (or one of our coordinated dual-degree programs)."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-U-015
  field: undergraduate.specialized_programs.dual_degree
  value: ["Huntsman (BA + BS)", "LSM (BA + BS)", "M&T (BS + BSE/BAS)", "NHCM (BSN + BS)", "VIPER (BA + BSE)", "VIC (BSE specialized)"]
  source_url: https://admissions.upenn.edu/academics/exploring-academics/specialized-degree-programs
  source_snippet: "Huntsman … Students earn a BA from the College of Arts and Sciences in International Studies and a BS in Economics from the Wharton School. … M&T … a BS in Economics from the Wharton School and either a BSE or BAS from the School of Engineering and Applied Science."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-001
  field: graduate.wharton_doctoral.deadline_and_test
  value: { application_deadline: "December 15, 11:59 p.m.", test_required: "GRE or GMAT" }
  source_url: https://doctoral.wharton.upenn.edu/admissions/
  source_snippet: "Application Deadline: December 15 Note: Your completed application must be received by 11:59 p.m. … the admissions committee considers your previous academic work, your standardized graduate examination performance (GRE/GMAT) …"
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-002
  field: graduate.sas_grad.deadlines_tests
  value: { phd_deadlines_start: "December 8", ets_code: 2926, gre: "some programs no longer require (check per program)", ielts_accepted_in_lieu_of_toefl: true, gre_valid_years: 5, toefl_valid_years: 2 }
  source_url: https://www.sas.upenn.edu/graduate-division/prospective-students/admissions-faq
  source_snippet: "deadlines are program specific and start on December 8 for PhD consideration … The school code is 2926. GRE scores are valid for 5 years and TOEFL scores for 2 years. IELTS scores are accepted in lieu of the TOEFL. … There are several programs that no longer require GRE scores."
  capture_date: 2026-07-05
  evidence_type: official_webpage

- id: E-G-003
  field: graduate.cost_model
  value: { model: "per-school", hub_url: "https://srfs.upenn.edu/costs-budgeting/graduate-cost-attendance", phd_typically_fully_funded: true, masters_typically_self_funded: true }
  source_url: https://srfs.upenn.edu/costs-budgeting/graduate-cost-attendance
  source_snippet: "Graduate Cost of Attendance — per-school budgets published as sub-pages for each of the 12 schools (Annenberg, SAS, Dental, etc.)"
  capture_date: 2026-07-05
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
upenn-knowledge-base-v2/
├── overview/
│   ├── chunk: institution-overview (Section 0 — counts, hierarchy, inventory, matrix)
│   └── chunk: evidence-index (Section 5)
├── undergraduate/  (one chunk per school — preserves 学院 → 学位级别 grouping)
│   ├── chunk: sas-undergraduate        (College of Arts & Sciences — 264 rows)
│   ├── chunk: seas-undergraduate       (Penn Engineering — 21 rows)
│   ├── chunk: wharton-undergraduate    (26 BS concentrations)
│   ├── chunk: nursing-undergraduate    (7 rows)
│   └── chunk: weitzman-undergraduate   (1 minor)
├── graduate/  (one chunk per school)
│   ├── chunk: sas-graduate             (80 rows)
│   ├── chunk: seas-graduate            (35 rows)
│   ├── chunk: wharton-graduate         (35 rows)
│   ├── chunk: nursing-graduate         (28 rows)
│   ├── chunk: psom-graduate            (41 rows)
│   ├── chunk: gse-graduate             (44 rows)
│   ├── chunk: weitzman-graduate        (25 rows)
│   ├── chunk: law-graduate             (5 rows)
│   ├── chunk: dental-graduate          (16 rows)
│   ├── chunk: vet-graduate             (4 rows)
│   ├── chunk: sp2-graduate             (7 rows)
│   └── chunk: annenberg-graduate       (2 rows)
├── admissions/
│   ├── chunk: ug-requirements-deadlines (Section 3.1, 3.2)
│   ├── chunk: ug-costs-finaid           (Section 4.1, 4.2)
│   └── chunk: grad-admissions-model     (Section 2.3, 3.3, 4.3)
└── dual-degree/
    └── chunk: coordinated-dual-degree   (Section 1.3)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "upenn-knowledge-base-v2"
  school: "<home college / school>"
  degree_level: "<BA|BS|BSE|BAS|BAAS|BSN|BFA|MA|MS|MBA|MSE|MSEd|MSN|PhD|EdD|DNP|MD|DMD|VMD|JD|LLM|SJD|...|Minor|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding | evidence
  source_url: <URL>
  capture_date: 2026-07-05
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-05
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL | Rationale |
|----------|-----------|------------|-----------|
| P0 | Per-school graduate COA tables (12 sub-pages) | srfs.upenn.edu/costs-budgeting/graduate-cost-attendance/<school> | Section 4.3 currently summarized; full line-item tables per school needed |
| P0 | Per-program grad admissions: GRE/IELTS minimums, fees, deadlines for each of 264 grad degrees | Each school's admissions sub-page (§2.3) | Decentralized — catalog has curriculum only |
| P0 | Penn Engineering graduate (SEAS) admissions hub | graduate.admissions.seas.upenn.edu (returned connection error in this run — retry fresh) | Confirms SEAS MS/PhD deadlines, fee, GRE policy |
| P0 | Penn GSE, Penn Carey Law (JD/LLM), Penn Dental, Penn Vet, SP2 admissions detail pages | Each school site | Confirm current fees/deadlines/ELP per school |
| P1 | Wharton MBA round deadlines + fee | mba.wharton.upenn.edu | Only Wharton Doctoral captured in this run |
| P1 | Transfer applicant pathway + intl transfer aid rule | admissions.upenn.edu/how-to-apply/transfer-applicants | Verify "intl transfers not aid-eligible" claim |
| P1 | Pre-college credit policy + homeschool policy | admissions.upenn.edu/how-to-apply/first-year-applicants/pre-college-credits etc. | Linked from app-requirements page |
| P2 | Per-school UG curriculum / core requirements | Each UG school's academics page | Section 1.5 summarized at high level |
| P2 | Penn academic calendar 2026-27 | almanac.upenn.edu/penn-academic-calendar | For term-start/registration dates |

---

## SECTION 7 — Cross-school comparison framework (optional)

| Dimension | UPenn | (other schools) |
|-----------|-------|-----------------|
| Total program count (Rule 1, catalog rows) | **641** | — |
| Degree-granting programs (UG majors + grad degrees) | 466 | — |
| Schools (UG) | 4 | — |
| Schools (grad/prof) | 12 | — |
| Total cost/yr (UG on-campus, 2026-27) | **$99,082** | — |
| Tuition/yr (UG, 2026-27) | **$65,670** | — |
| Tuition + fees/yr (UG, 2026-27) | $73,978 | — |
| Need-blind (US/citizens) | Yes | — |
| Need-blind (Canada & Mexico) | **Yes** (distinctive) | — |
| Need-blind (other internationals) | **No — need-aware** | — |
| No-loan aid | Yes | — |
| Income ≤ $75k → full billed costs | Yes | — |
| Income up to $200k → at least full tuition | Yes | — |
| ED deadline | **Nov 1** | — |
| RD deadline | **Jan 5** | — |
| SAT/ACT required? | **Yes (2025-26; reinstated)** | — |
| TOEFL competitive | 100 | — |
| IELTS competitive | 7.0 | — |
| Duolingo competitive | 130 | — |
| UG app fee | $75 | — |
| Grad app fee | Varies (~$70–$120 by school) | — |
| April-15 honor date (funded PhD) | Yes (CGS signatory) | — |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-05
> **Sources**: admissions.upenn.edu, srfs.upenn.edu, catalog.upenn.edu, doctoral.wharton.upenn.edu, www.sas.upenn.edu/graduate-division
> **Verification**: ego-browser serverFetch + JS DOM extraction (Phase 1 discovery + Phase 2 catalog parse of all 641 program links)
> **Granularity**: school → degree-level → program
> **Reconciliation**: Rule-1 (641) == matrix-sum (641) == Rule-5 rows (641) == inventory-sum (641) — PASS
