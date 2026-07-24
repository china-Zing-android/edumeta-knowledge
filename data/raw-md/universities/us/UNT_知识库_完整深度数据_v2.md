# University of North Texas (UNT) Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-07
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)

**University**: University of North Texas (UNT)
**Location**: Denton, Texas (Denton County), with UNT at Frisco extension; ~40 miles north of the Dallas–Fort Worth metroplex. Address: 1155 Union Circle #311277, Denton, TX 76203-5017. Metro line: 817-267-3731; Main: 940-565-2000; TTY: 800-735-2989; Admissions: 940-565-2681.
**Classification**: Carnegie R1: Doctoral Universities – Very High Research Activity; 4-year public; Hispanic-Serving Institution; Established 1890.
**Source catalog edition**: 2026-2027 Undergraduate Catalog & 2026-2027 Graduate Catalog (official release July 1, 2026; effective fall 2026), plus the UNT program finder (https://search.unt.edu/) for the master's/doctoral program list.
**Primary websites**:
- Main: https://www.unt.edu/
- Undergraduate admissions: https://admissions.unt.edu/
- Toulouse Graduate School: https://tgs.unt.edu/ (redirects to https://www.unt.edu/graduate/index.html)
- Catalog (programs): https://catalog.unt.edu/
- Academics portal (program finder): https://www.unt.edu/academics/

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BS/BFA/BM/BSET/BAS/BAAS/BSMLS/BSMTH/BSCHM/BSBIO/BSPHY/BSBC/BSECO/BBA/BSW) | 194 |
| 本科辅修 (Minor) | 91 |
| 本科证书 (Professional Certificate + Undergraduate Academic Certificates) | 1 + 103 = 104 |
| 本科教师认证 (Secondary + All-Level tracks) | 12 + 4 = 16 |
| 研究生学位项目 (Master's incl. MBA/MFA/MLA-近义 — plus Doctoral) | 102 + 50 = 152 |
| 研究生 Grad Track 衔接 (UG→Grad combined track, not a separate award) | 131 (pathway listings) |
| **学位项目总计 (UG majors + UG certificates + Grad programs)** | **194 + 104 + 152 = 450** |
| **仅计独立学位/证书项目 (排除 Grad Track 衔接)** | **194 + 91 + 104 + 16 + 152 = 557** |
| 学院 / 独立系所总数 (UG home colleges + Graduate School) | 12 |

> 解读：本表把 Grad Track Options 单独归类为"衔接路径"而不是"独立学位"，因为它把规定的本科课程与对应硕士课程打包、允许提前选修硕士学分，但最终拿到的还是本科+硕士**两个独立学位**（合计已计入 194 + 152 行）。Teacher certifications 归为非学位认证轨道，与证书分别列示。Dual degrees（如 Accounting BS+MS）已作为两条独立主修计数。

Source for counts:
- `catalog.unt.edu/content.php?catoid=40&navoid=4657` (Majors, Minors, Certificates hub), captured 2026-07-07.
- `search.unt.edu/s/search.html?collection=unt%7Esp-program-finder` (program finder; classification filters Master's, Doctoral), captured 2026-07-07.

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy with parent-child)

UNT has 12 degree-granting academic units (11 colleges + Toulouse Graduate School). Below is the parent → child map for the **2026-2027 academic year** (from the catalog's "Degree Programs Listed by Academic Unit" page, navoid 4658, captured 2026-07-07):

```
University of North Texas
├── Honors College                                          [学院 / interdisciplinary]
├── International Affairs                                   [学院 / administrative]
├── G. Brint Ryan College of Business                       [学院]
│   ├── Accounting                                          [系]
│   ├── Business Information Assurance                      [系 / cross-listed with COIST below]
│   ├── Business Integrated Studies                         [系]
│   ├── Economics                                           [系]
│   ├── Finance, Insurance, Real Estate and Law (FIRE)      [系]
│   ├── Information Technology and Decision Sciences (ITDS) [系]
│   ├── Management                                          [系 / 含 Entrepreneurship, HR, Sport Entertainment]
│   └── Marketing                                            [系 / 含 Professional Selling]
├── College of Education                                    [学院]
│   ├── Counseling and Higher Education                     [系]
│   ├── Educational Psychology                              [系]
│   ├── Kinesiology, Health Promotion and Recreation         [系]
│   ├── Teacher Education and Administration                [系]
│   └── [Special Ed / Autism Intervention programs]         [embedded]
├── College of Engineering                                  [学院]
│   ├── Biomedical Engineering                              [系]
│   ├── Computer Science and Engineering                    [系]
│   ├── Electrical Engineering                              [系]
│   ├── Engineering Technology (Construction, Mechanical)   [系]
│   ├── Materials Science and Engineering                   [系]
│   └── Mechanical and Energy Engineering                   [系]
├── College of Information                                  [学院] (formerly College of Information Science; renamed)
│   ├── Information Science                                 [系]
│   ├── Information Technology                              [系]
│   └── Learning Technologies                               [系]
├── College of Liberal Arts and Social Sciences (CLASS)     [学院]
│   ├── Anthropology                                        [系]
│   ├── Communication Studies                               [系]
│   ├── Dance & Theatre Arts                                [系]
│   ├── Economics (shared w/ Business)                      [系 ⚠ cross-listed]
│   ├── English Studies                                     [系]
│   ├── Geography and the Environment                      [系]
│   ├── History                                             [系]
│   ├── International Studies                               [系]
│   ├── Journalism (Mayborn School of Journalism)           [系]
│   ├── Media Arts                                          [系]
│   ├── Philosophy and Religion                             [系]
│   ├── Political Science                                   [系]
│   ├── Psychology                                          [系]
│   ├── Sociology                                           [系]
│   ├── Technical Communication                             [系]
│   └── Urban Policy and Planning                           [系]
├── School of Merchandising and Hospitality Management      [学院]
│   ├── Hospitality Management                              [系]
│   └── Merchandising and Digital Retailing                 [系]
├── College of Music                                        [学院]
│   ├── Composition Studies                                 [系]
│   ├── Conducting and Ensembles                            [系]
│   ├── Dance                                               [系 (joint w/ CLASS)]
│   ├── Jazz Studies                                        [系]
│   ├── Music Business                                      [系]
│   ├── Music Education                                    [系]
│   ├── Music Theory                                        [系]
│   ├── Performance (keyboard, vocal, orchestral instruments)[系]
│   └── Ethnomusicology                                     [系]
├── College of Public Affairs and Health Sciences           [学院]
│   (note: UNT informally calls this "College of Health & Public Service" in some materials — the official catalog name as of 2026-27 is "College of Public Affairs and Health Sciences")
│   ├── Audiology and Speech-Language Pathology             [系]
│   ├── Behavior Analysis                                   [系]
│   ├── Criminal Justice                                    [系]
│   ├── Emergency Management and Disaster Science           [系]
│   ├── Public Administration                               [系]
│   ├── Rehabilitation and Health Services                  [系 / 含 Addiction Studies, Public Health, Rehab Studies]
│   └── Social Work                                         [系]
├── College of Science                                      [学院]
│   ├── Biological Sciences                                 [系]
│   ├── Chemistry and Biochemistry                          [系]
│   ├── Computer Science (joint w/ COE)                     [系 ⚠ cross-listed]
│   ├── Mathematics                                         [系]
│   ├── Physics                                             [系]
│   └── [Data Science program is interdisciplinary, not a separate dept]
├── College of Visual Arts and Design                       [学院]
│   ├── Art Education and Art History                       [系]
│   ├── Design (Communication Design)                       [系]
│   ├── Fashion Design and Merchandising                    [系 / cross-listed w/ School of Merchandising & Hospitality Mgmt]
│   ├── Studio Art (Ceramics, Drawing/Painting, Metals, New Media, Photography, Printmaking, Sculpture) [系]
│   └── Critical Studies in Music and Society               [embedded / cross-listed w/ Music]
└── Toulouse Graduate School                                [研究生院]
    └── (Graduate-only programs in any college above are administered jointly; students apply through the
        program/department, but enrollment is processed through TGS. TGS also houses stand-alone grad programs
        not hosted in a college: e.g., Educational Leadership Ed.D., Interdisciplinary Studies M.A., Higher
        Education programs, certain certificates, and unclassified grad students.)
```

**Source verbatim**: "**University of North Texas Bulletin | 2026-2027 Undergraduate Catalog** … Official release date is July 1, 2026 … Catalog goes into effect at the beginning of the 2026 fall semester." From https://catalog.unt.edu/ (captured 2026-07-07). The 11 colleges + Toulouse Graduate School list appears in the left-nav and in the "Degree Programs Listed by Academic Unit" page: https://catalog.unt.edu/content.php?catoid=40&navoid=4658 (captured 2026-07-07).

> Note on cross-listings: ⚠ Computer Science lives in BOTH the College of Engineering (as part of "Computer Science and Engineering" department) AND the College of Science (the dept website uses computer science without the "Engineering" word). The catalog number-sectioned discipline "Computer Science and Engineering" is one department with both BS (in CoE) and BA/BS tracks. UNT does not number programs by MIT-style course IDs; programs are identified by full name plus college.

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

UNT uses a wide variety of official degree abbreviations. The canonical column below maps each to the degree-taxonomy controlled vocabulary (see `degree-taxonomy.md`); counts are derived from catalog snapshots of 2026-27 program lists.

| canonical | official (本校) | 全称 | 层级 | 本项目数量 |
|-----------|----------------|------|------|-----------|
| BA | BA | Bachelor of Arts | 本科 | many |
| BS | BS | Bachelor of Science | 本科 | many |
| BAAS | BAAS | Bachelor of Applied Arts and Sciences | 本科 | (with 22 concentrations) |
| BAS | BAS | Bachelor of Applied Studies | 本科 | 1 (Learning Technologies) |
| BBA | BBA | Bachelor of Business Administration | 本科 | many |
| BFA | BFA | Bachelor of Fine Arts | 本科 | many |
| BM | BM | Bachelor of Music | 本科 | many |
| BSBIO | BSBIO | Bachelor of Science (Biology, formal transcript code) | 本科 | 1+1 |
| BSBC | BSBC | Bachelor of Science (Biochemistry) | 本科 | 2 |
| BSBIO/BSCHM/BSPHY/BSECO/BSMTH/BSMLS/BSET | (variants) | Bachelor of Science with discipline-specific transcript codes | 本科 | 7 unique transcript codes |
| BSW | BSW | Bachelor of Social Work | 本科 | 1 |
| Minor | minor | Undergraduate minor | 本科 | 91 |
| Certificate | certificate | Undergraduate academic / professional certificate | 本科 | 1 (professional) + 103 (academic) = 104 |
| Teaching Cert | teacher certification | Secondary / All-Level teacher certification (post-bacc credential) | 本科-轨外 | 12 + 4 = 16 |
| MA | MA / M.A. | Master of Arts | 研究生 | many |
| MS | MS / M.S. | Master of Science | 研究生 | many |
| MBA | MBA / M.B.A. | Master of Business Administration | 研究生 | 7 (variants incl. AI, Analytics, Finance, Health, Mgmt Consulting, Marketing, Strategic Mgmt) |
| MSW | MSW | Master of Social Work | 研究生 | 1 |
| MPH-equivalent (note: UNT offers MS in Health Informatics & related) | (variant) | Master-level health | 研究生 | several |
| MEd-equivalent | MED | Master of Education-equivalent in Counseling, Special Ed, etc. | 研究生 | several |
| MFA-equivalent | (n/a in catalog) | Master of Fine Arts: UNT does not label any program MFA explicitly; closest is MM (Master of Music) and select Master of Arts in design-related areas | 研究生 | (no separate MFA listing) |
| MM | MM | Master of Music (interpreted as `MA`-equivalent / conservatory practitioner) | 研究生 | ~9 (Performance, Conducting, Composition, Jazz Studies, Music Business, Music Education, Music Theory, Musicology, Ethnomusicology) |
| Adv Cert | GAC / CERT | Graduate Academic Certificate (e.g. AI in Business GAC, Data Analytics Certificate, School Counseling Certificate, Specialist in Aging Certificate, Technical Writing GAC, Graduate Artist Certificate in Music Performance) | 研究生 | ~7 |
| PhD | Ph.D. / PhD | Doctor of Philosophy | 研究生 | many |
| EdD | Ed.D. | Doctor of Education | 研究生 | 2 (Educational Leadership Ed.D., Higher Education Ed.D.) |
| DBA | DBA | Doctor of Business Administration | 研究生 | 1 |
| AuD | Au.D. | Doctor of Audiology | 研究生 | 1 |
| DMA-equivalent | (n/a) | UNT does not list a DMA; closest is Music PhD with concentrations in Music Education, Musicology, Composition, Music Theory, Ethnomusicology — and the Doctoral Degree in Music Performance / Jazz Performance (these are Doctor of Musical Arts equivalents by structure but labeled "Doctoral Degree" or "PhD"). | 研究生 | (none labeled DMA) |

> TOTAL unique program lines counted (2026-27): **194 UG majors + 91 UG minors + 16 teacher certifications + 104 UG certificates + 102 Grad master's + 50 Grad doctoral = 557 distinct programs** (rule 1 reconciles with this table).

Source: program lists captured from https://catalog.unt.edu/content.php?catoid=40&navoid=4657 and https://search.unt.edu/s/search.html?collection=unt%7Esp-program-finder (both 2026-07-07). Degree abbreviation taxonomy normalized per `/Users/erik/.claude/skills/uni-admissions-research/references/degree-taxonomy.md`.

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

Cross-tab of program counts by college row × canonical degree-level column. UNT is the kind of large state R1 where distributions matter most for cross-school comparison.

Counts populated from catalog snapshot; rows total to the program-grouping counts in rule 1. Cells with "—" mean no program of that level exists in that unit.

| 学院 \ 级别 | BA | BS | BFA/BM/BAS/BAAS/BBA/BSW (other UG bachelor types) | Minor | Cert (UG) | Teach Cert | MA | MS | MBA / other master's spec. | PhD / EdD / DBA / AuD (other doctoral) | Adv Cert / GAC | 学院 合计 |
|------------|----|----|-----|------|------|------|----|----|-----------|---------|-----------|-----------|
| Honors College | — | — | — | — | — | — | — | — | — | — | — | (interdisciplinary; no standalone programs listed in catalog) |
| International Affairs | — | — | — | — | — | — | — | — | — | — | — | (admin unit) |
| **G. Brint Ryan College of Business** | 2 (Economics; minor-list BA-level) | 6 (Gen Business; Risk Mgmt & Insurance; BCIS; Digital Business; Supply Chain Mgmt; Industrial Distribution) | 18 (BBA majors: Accounting, Business Analytics, Economics-BBA, Entrepreneurship, Finance, Financial Planning, Gen Business-BBA, HR Mgmt, Mgmt, Marketing, Marketing-Professional Selling, Real Estate, Real Estate-Residential, Sport Entertainment, BIS, BIS-International Track, Accounting-BBA) | 13 | 8 | — | — | 4 (Accounting Bachelor's & Master's dual / Advanced Data Analytics MS / Business Analytics MS / Business Studies MS / Corporate Accounting MS / Supply Chain Analytics MS / Supply Chain Mgmt MS) | 7 (Business Analytics MBA; AI MBA; Finance MBA; Mgmt Consulting MBA; Health Services Mgmt MBA; Marketing MBA; Marketing Analytics MBA; Strategic Mgmt MBA) | 7 (Accounting PhD; Business Info Assurance PhD; Finance PhD; Mgmt PhD; Mgmt Science PhD; Marketing PhD; DBA; Supply Chain Mgmt PhD) | 1 (AI in Business GAC) | ~72 |
| **College of Education** | — | 2 (Education BS; Kinesiology BS with sub-tracks) | — | — | 1 | 12 secondary + 4 all-level = 16 | 6 (Curriculum & Instruction; Educational Leadership; Higher Education; Counseling-School Counseling; Special Education; Secondary Education Teaching; Advanced Teaching) | — | — | ~3 (Educational Leadership EdD; Higher Education EdD; Learning Technologies PhD — joint w/ Info) | — | ~28 |
| **College of Engineering** | 1 (Geography is shared; Engineering has no BA) | 8 (Biomedical; Computer; Computer Science; Construction Mgmt; Electrical; Materials Science; Mechanical & Energy; Cybersecurity; AI; Data Science; plus Engineering Technology BSETs) | 2 (Construction Engineering Tech BSET; Mechanical Engineering Tech BSET) | 1 (Computer Science & Engineering minor) | 11 (Additive & Digital Mfg; AI & ML; Communication & Networks; Computer Systems; Cybersecurity; Data Analytics; Electromechanical; Manufacturing Engineering Technologies; Real-Time & Embedded; RF & Circuit; Secure Software; Signal Processing & Control; Software Engineering; VLSI & Electronics; Web Development) | — | — | 5 (Computer Engineering; Computer Science; Cybersecurity; Data Engineering; Electrical Eng; Engineering Mgmt; Materials Science & Eng; Mechanical & Energy Eng; Semiconductor Mfg Eng) | — | 3 (Biomedical PhD; Computer Science & Engineering PhD; Electrical Eng PhD; Materials Science & Eng PhD; Mechanical & Energy Eng PhD) | — | ~31 |
| **College of Information** | — | 4 (Information Science; Information Technology; Learning Technologies BAS; Health Informatics) | 1 (Learning Technologies BAS) | 2 (Information Management and Health Informatics; Information Science and Knowledge Organization) | 7 (various tech certs) | — | 4 (Information Science; Library Science; Learning Technologies; Health Informatics — some cross-listed with Health) | — | — | 3 (Information Science PhD; Learning Technologies PhD) | — | ~21 |
| **College of Liberal Arts and Social Sciences** | ~38 (Anthropology; BA Communication Studies; Converged Broadcast Media; Content Strategy; Critical Studies in Music & Society; English-4 conc.; French; German Studies; History; International Studies-4 conc.; Japanese; Journalism-5 conc.; Media Arts; Nonprofit Leadership; Philosophy; Political Science; Psychology; Social Science; Spanish; Theatre-5 conc.; Theatre BA; Urban Policy & Planning; Communication Design-BFA; etc.) | ~10 (Criminal Justice; Emergency Admin & Planning; Social Work BSW; Rehabilitation Studies; Public Health; Sociology; Social Science; Geography; Geographic Info Systems & CS; Tech Communication; Converged Broadcast Media shared) | 6 (Communication Design-2 conc. BFA; Fashion Design BFA; Interior Design BFA; Studio Art-7 conc. BFA; Art Education BFA; Art History BA shared; Audio/SLP BS) | 18+ | ~30 (incl Africana, American Studies, Latina/o, Peace Studies, Health, Communication Systems, Digital Insights, Media Mgmt, Science & Popular Culture, Storytelling, etc.) | — | ~12 (Anthropology; Communication Studies; English; History; International Studies; Journalism; Philosophy; Political Science; Sociology; Spanish; Tech Writing; Public Admin; Interaction Design; etc.) | 3 (Criminology; Geography; Public Admin; French; etc.) | — | ~15 (English PhD; Counseling Psych PhD; Clinical Psych PhD; Sociology PhD; Political Science PhD; History 4 conc.; Public Admin-related; etc.) | 1 (Technical Writing GAC) | ~140 |
| **School of Merchandising and Hospitality Management** | — | ~5 (Hospitality Mgmt; Hospitality Mgmt teacher cert; Event Design & Experience Mgmt; Merchandising-2 conc.; Digital Business & E-commerce; Consumer Insights Interdisciplinary; Supply Chain Mgmt BS) | — | 4 (Hospitality Mgmt; Merchandising; Furnishings & Décor Merchandising; Logistics & Supply Chain Mgmt) | 12+ (Banking; E-commerce Marketing; Entrepreneurship; Event Mgmt; Fashion Buying; F&B Mgmt; Financial Services; Global Fashion Brand Mgmt; Hospitality Finance; Hospitality Tech; Hotel Operations; Live Entertainment Design; New Product Development; etc.) | — | — | 3 (Hospitality Mgmt MS; Hospitality & Tourism Data Analytics MS; Merchandising & Digital Retailing MS) | — | — | — | ~30 |
| **College of Music** | 6 (Music BA; Commercial Music BA; Art History BA-shared; Critical Studies BA shared; Communication Studies BA shared; Media Arts BA shared) | — | 14 (Music Education-6 specializations BM; Composition BM; Jazz Studies-3 emphases BM; Performance-7 specs BM) | 2 (Music minor; Music Theory minor) | 1 (Commercial Music minor-equiv certificate; Dance Choreography; Dance Studio Teaching; Dance Wellness; Creative Economy) | 1 (Theatre teacher cert) | ~9 (Music Business; Music Composition; Music Education; Music Performance; Music Theory; Musicology; Conducting & Performance; Jazz Studies; Ethnomusicology; Musicology) | — | — | ~9 (Music PhD-Composition; Music PhD-Ethnomusicology; Music PhD-Music Theory; Music PhD-Musicology; Music PhD-Music Education; Music Performance Doctoral; Jazz Performance Doctoral) | 1 (Graduate Artist Certificate in Music Performance) | ~49 |
| **College of Public Affairs and Health Sciences** | 3 (Nonprofit Leadership; Communication Studies shared; Rehabilitation-related) | ~7 (Addiction Studies; Applied Behavior Analysis; Audiology & SLP; Criminal Justice; Emergency Admin; Public Health; Public Health-Health Prof conc.; Rehabilitation Studies; Social Work BSW; Behavior Analysis; Public Health) | — | 3 (Addiction Studies; Behavior Analysis; Counseling; Human Services; Nonprofit Leadership; Rehabilitation Studies; Public Health; Public Admin; Substance Use Disorders Treatment cert; Trauma-Informed Care cert) | ~10 (Conflict Resolution; Cybercrime & Social Behavior; Drug & Alcohol; Specialist in Aging; etc.) | — | ~5 (Applied Anthropology; Applied Behavior Analysis; Behavior Analysis; Counseling-School; Counseling-Addictions; Public Admin; Rehab Counseling; Special Ed; Speech-Language Pathology) | 1 (Behavior Analysis; Health Informatics; Speech-Language Pathology) | 1 (Business Admin MBA w/ Health Services Mgmt) | 1 (Health Sciences PhD; Clinical & Counseling Psych PhD) | 1 (Specialist in Aging Certificate; School Counseling Certificate) | ~33 |
| **College of Science** | ~6 (Biochem BA; Biology BA; Chemistry BA; Chemistry w/ Computational conc. BA; Math BA-2 tracks) | ~8 (Biochem BS; Biology BSBIO; Chem BSCHM; Cybersecurity BS; Data Science BS; Mathematics BSMTH-2 tracks; Physics BSPHY-4 conc.; Computer Science BS-shared) | 1 (Medical Lab Sciences BSMLS) | 3 (Biological Sciences; Chemistry; Mathematics; Physics; Statistics) | ~7 (Actuarial Science; Computational Science; Cybercrime & Social Behavior; Data Analytics; Environmental Studies; Geospatial Analytics; Statistics; Water Resources) | — | ~3 (Biology MA; Chemistry MA; Mathematics MA; Mathematics-Education conc.; Physics MA; Computer Science MS; Statistics MS; Environmental Science MS) | ~6 (Biochem & Molecular Biology MS; Biology MS; Chemistry MS; Mathematics MS; Computer Science MS; Physics MS; Data Science MS; Statistics MS) | — | ~5 (Biochemistry & Molecular Biology PhD; Biology PhD; Chemistry PhD; Mathematics PhD; Physics PhD; Computer Science & Engineering PhD-shared; Exercise Physiology Biology PhD) | — | ~38 |
| **College of Visual Arts and Design** | 2 (Art History BA; Interdisciplinary Art & Design Studies-3 conc. BA; Communication Design shared) | — | 13 (Art Education BFA; Communication Design 2-conc. BFA; Fashion Design BFA; Interior Design BFA; Studio Art 7-conc. BFA) | 1 (Studio Art minor; Photography) | 2 (Arts Management; Arts; Design Management; Creative Economy — also under CVAD specifically) | — | ~3 (Art History MA; Art Education MA; Fashion Design MFA-equiv MM/A; Interaction Design MA; Interior Design MA; Photography MA; Studio Art with Ceramics/Drawing/New Media/Photo/Printmaking/Sculpture) | — | — | 2 (Art Education PhD; possibly Art History PhD-shared) | — | ~20 |
| **Toulouse Graduate School** | — | — | — | — | — | — | (admin): hosts Interdisciplinary Studies MA; Educational Leadership programs | (admin): Advanced Data Analytics MS — could be cross-college | (admin): general MBA, DBA, plus non-departmental graduate certificates | (admin): all PhDs route through TGS | — | (admin overlay) |
| **TOTAL** | ~58 | ~52 | ~58 | ~91 | ~104 | ~16 | ~50 | ~30 | ~7 (MBA family) + several MA specialty variants | ~50 | ~7 | **~557** |

Source for the matrix: `catoid=40&navoid=4657` catalog page (2026-07-07), `catalog.unt.edu/content.php?catoid=40&navoid=4658` for college-by-college confirmation, and `search.unt.edu/s/search.html?…&f.Classification=Master%27s` (102 entries) and `…&f.Classification=Doctoral` (50 entries), captured 2026-07-07. The matrix counts are approximate; see per-college breakdowns in Sections 1 and 2 for the exact lists.

> The matrix uses canonical degree codes per `/Users/erik/.claude/skills/uni-admissions-research/references/degree-taxonomy.md`. UNT's BS-with-discipline-codes (BSBIO, BSBC, BSCHM, BSPHY, BSMTH, BSECO, BSMLS) all map to canonical `BS`. UNT's BBA maps to canonical `BBA` (Bachelor of Business Admin). UNT's BM (Bachelor of Music) maps to canonical `BFA` per music-school convention adopted in the taxonomy (treated as a bachelor of fine/performing arts). UNT's BAAS and BAS are their own canonical types — currently grouped under `other UG bachelor types` column but could be split; in the document per-row breakdown they'll be labeled explicitly.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture (1-paragraph orientation + pointer)

UNT's undergraduate majors span **11 colleges + the Toulouse Graduate School** (which, while graduate-only, lists a small number of "grad track" combined-degree pathways for undergrads). The college-list in §0.2 is the authoritative structure; in §1.2 each program is placed under its home college → department → degree level, mirroring the Acalog-managed catalog at `https://catalog.unt.edu/content.php?catoid=40&navoid=4657` and the "Degree Programs Listed by Academic Unit" page at `navoid=4658`. The 194 majors listed include many that appear in two or more colleges (e.g., Computer Science lives in both College of Engineering and College of Science; Economics in both Business and CLASS); they are placed under their **administrative home department** per the catalog's college-by-college listing. Section 1.3 captures cross-listings; §1.4 lists all 91 minors; §1.5 notes the core curriculum.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

Each college block in this section uses the catalog's official ordering. Program names are reproduced verbatim from `catalog.unt.edu/content.php?catoid=40&navoid=4657&poid=<id>` (each program has its own preview_program URL). When a college's department structure isn't broken out as sub-departments in the catalog (e.g., Music), the listing is grouped under the college heading with degree-level sub-headings.


#### G. Brint Ryan College of Business
##### Department of Accounting
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accounting, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21179&returnto=4657 |
| 2 | Accounting, BS (dual degree; may not be earned without completion of the MS) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21475&returnto=4657 |

##### Department of Business Information Assurance / ITDS (cross-listed)
###### BBA / BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Business Analytics, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21237&returnto=4657 |
| 4 | Business Computer Information Systems, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21208&returnto=4657 |

##### Department of Economics (cross-listed with CLASS)
###### BA / BBA / BSECO
| # | 专业 | URL |
|---|------|-----|
| 5 | Economics, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21246&returnto=4657 |
| 6 | Economics, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21247&returnto=4657 |
| 7 | Economics, BSECO | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21248&returnto=4657 |

##### Department of Finance, Insurance, Real Estate and Law (FIRE)
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 8 | Financial Planning, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21714&returnto=4657 |
| 9 | Finance, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21264&returnto=4657 |
| 10 | Real Estate, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21383&returnto=4657 |
| 11 | Real Estate with a concentration in Residential Property Management, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21382&returnto=4657 |
| 12 | Risk Management and Insurance, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21392&returnto=4657 |

##### Department of Information Technology and Decision Sciences (ITDS)
###### BBA / BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Digital Business and E-commerce, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21241&returnto=4657 |

##### Department of Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 14 | Entrepreneurship and Enterprise Management, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21260&returnto=4657 |
| 15 | Human Resource Management, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21353&returnto=4657 |
| 16 | Management, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21751&returnto=4657 |
| 17 | Sport Entertainment Management, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21683&returnto=4657 |
| 18 | Business Integrated Studies, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21272&returnto=4657 |
| 19 | Business Integrated Studies - International Track, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21848&returnto=4657 |

##### Department of Marketing
###### BBA / BS
| # | 专业 | URL |
|---|------|-----|
| 20 | Marketing, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21325&returnto=4657 |
| 21 | Marketing with a concentration in Professional Selling, BBA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21506&returnto=4657 |
| 22 | General Business, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21618&returnto=4657 |


#### College of Education
##### Department of Teacher Education and Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Education, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21252&returnto=4657 |

##### Department of Kinesiology, Health Promotion and Recreation
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Kinesiology, BS (General track) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21483&returnto=4657 |
| 3 | Kinesiology with a concentration in Pre-PT/Allied Health, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21582&returnto=4657 |
| 4 | Kinesiology with a concentration in Strength and Conditioning, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22245&returnto=4657 |
| 5 | Health Behavior and Fitness, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21467&returnto=4657 |

> Note: Special Education / Autism Intervention Special Education Master's program is grad-level; UG programs in Special Ed are tracks within Education BS.

---

#### College of Engineering
##### Department of Computer Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21225&returnto=4657 |
| 2 | Computer Science, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21227&returnto=4657 |
| 3 | Cybersecurity, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21644&returnto=4657 |
| 4 | Artificial Intelligence, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22347&returnto=4657 |
| 5 | Data Science, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21610&returnto=4657 |
| 6 | Game Studies and Design, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21834&returnto=4657 |

##### Department of Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 7 | Electrical Engineering, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21250&returnto=4657 |

##### Department of Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Biomedical Engineering, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21519&returnto=4657 |

##### Department of Materials Science and Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Materials Science and Engineering, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21327&returnto=4657 |

##### Department of Mechanical and Energy Engineering
###### BS / BSET
| # | 专业 | URL |
|---|------|-----|
| 10 | Mechanical and Energy Engineering, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21335&returnto=4657 |
| 11 | Mechanical Engineering Technology, BSET | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21337&returnto=4657 |

##### Department of Engineering Technology (Construction)
###### BS / BSET
| # | 专业 | URL |
|---|------|-----|
| 12 | Construction Engineering Technology, BSET | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21228&returnto=4657 |
| 13 | Construction Management, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21645&returnto=4657 |

---

#### College of Information
##### Department of Information Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Science, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21300&returnto=4657 |
| 2 | Health Informatics, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21846&returnto=4657 |

##### Department of Information Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Information Technology, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21301&returnto=4657 |

##### Department of Learning Technologies
###### BAS
| # | 专业 | URL |
|---|------|-----|
| 4 | Learning Technologies, BAS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21591&returnto=4657 |

---

#### College of Liberal Arts and Social Sciences (CLASS)
##### Department of Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21187&returnto=4657 |
| 2 | Applied Arts and Sciences, BAAS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21188&returnto=4657 |

##### BAAS concentrations (Applied Arts and Sciences, BAAS):
| # | BAAS Concentration | URL |
|---|------|-----|
| 2.1 | Applied Arts and Sciences, BAAS with a concentration in Applied Geography and GIS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22270&returnto=4657 |
| 2.2 | Applied Arts and Sciences, BAAS with a concentration in Applied Heritage Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21835&returnto=4657 |
| 2.3 | Applied Arts and Sciences, BAAS with a concentration in Applied Professional Practices | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22240&returnto=4657 |
| 2.4 | Applied Arts and Sciences, BAAS with a concentration in Applied Project Design | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21758&returnto=4657 |
| 2.5 | Applied Arts and Sciences, BAAS with a concentration in Aviation Operations | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22271&returnto=4657 |
| 2.6 | Applied Arts and Sciences, BAAS with a concentration in Computer Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22272&returnto=4657 |
| 2.7 | Applied Arts and Sciences, BAAS with a concentration in Consumer Insights | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22241&returnto=4657 |
| 2.8 | Applied Arts and Sciences, BAAS with a concentration in Data Analytics | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22273&returnto=4657 |
| 2.9 | Applied Arts and Sciences, BAAS with a concentration in Digital Business and E-commerce | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22242&returnto=4657 |
| 2.10 | Applied Arts and Sciences, BAAS with a concentration in Enology and Brewing | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21837&returnto=4657 |
| 2.11 | Applied Arts and Sciences, BAAS with a concentration in Global Societies and GIS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22274&returnto=4657 |
| 2.12 | Applied Arts and Sciences, BAAS with a concentration in Homeland Security | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22275&returnto=4657 |
| 2.13 | Applied Arts and Sciences, BAAS with a concentration in Hospitality Services | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22287&returnto=4657 |
| 2.14 | Applied Arts and Sciences, BAAS with a concentration in Industrial Distribution | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21759&returnto=4657 |
| 2.15 | Applied Arts and Sciences, BAAS with a concentration in Information Technology | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22276&returnto=4657 |
| 2.16 | Applied Arts and Sciences, BAAS with a concentration in Leadership Development | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22288&returnto=4657 |
| 2.17 | Applied Arts and Sciences, BAAS with a concentration in Logistical Operations | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22281&returnto=4657 |
| 2.18 | Applied Arts and Sciences, BAAS with a concentration in Natural Hazards and Geography GIS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22282&returnto=4657 |
| 2.19 | Applied Arts and Sciences, BAAS with a concentration in Organizations and Supervision | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22289&returnto=4657 |
| 2.20 | Applied Arts and Sciences, BAAS with a concentration in Public Health Education and Practice | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22283&returnto=4657 |
| 2.21 | Applied Arts and Sciences, BAAS with a concentration in Public Safety | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22284&returnto=4657 |
| 2.22 | Applied Arts and Sciences, BAAS with a concentration in Recreation and Sport Leadership | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22285&returnto=4657 |
| 2.23 | Applied Arts and Sciences, BAAS with a concentration in Residential Property Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22290&returnto=4657 |
| 2.24 | Applied Arts and Sciences, BAAS with a concentration in Workforce and Technical Administration | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21760&returnto=4657 |

##### Department of Communication Studies
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 3 | Communication Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21222&returnto=4657 |

##### Department of Dance & Theatre Arts (joint with College of Music)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 4 | Theatre, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21417&returnto=4657 |
| 5 | Theatre with a concentration in Acting, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21499&returnto=4657 |
| 6 | Theatre with a concentration in Dance, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22279&returnto=4657 |
| 7 | Theatre with a concentration in Design/Tech, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21498&returnto=4657 |
| 8 | Theatre with a concentration in Theatre Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21725&returnto=4657 |

##### Department of English Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 9 | English with a concentration in Creative Writing, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21427&returnto=4657 |
| 10 | English with a concentration in Language Arts, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21428&returnto=4657 |
| 11 | English with a concentration in Literature, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21425&returnto=4657 |
| 12 | English with a concentration in Writing and Rhetoric, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21426&returnto=4657 |

##### Department of Geography and the Environment
###### BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Geography, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21280&returnto=4657 |
| 14 | Geography with a concentration in Earth Systems, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21651&returnto=4657 |
| 15 | Geography with a concentration in Environmental Studies, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21653&returnto=4657 |
| 16 | Geographic Information Systems and Computer Science, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21647&returnto=4657 |
| 17 | Ecology for Environmental Science, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21493&returnto=4657 |

##### Department of History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 18 | History, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21289&returnto=4657 |

##### Department of International Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 19 | International Studies with a concentration in Business and Economics, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21441&returnto=4657 |
| 20 | International Studies with a concentration in Global Conflict, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21726&returnto=4657 |
| 21 | International Studies with a concentration in Global Perspectives, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21728&returnto=4657 |
| 22 | International Studies with a concentration in Human Security, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21724&returnto=4657 |

##### Mayborn School of Journalism
###### BA
| # | 专业 | URL |
|---|------|-----|
| 23 | Journalism with a concentration in Digital Journalism, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21439&returnto=4657 |
| 24 | Journalism with a concentration in Photojournalism, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21537&returnto=4657 |
| 25 | Journalism with a concentration in Public Relations, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21538&returnto=4657 |
| 26 | Journalism with a concentration in Sports Journalism and Communications, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21750&returnto=4657 |
| 27 | Journalism with a concentration in Video, Broadcast and Multimedia, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21536&returnto=4657 |
| 28 | Converged Broadcast Media, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21229&returnto=4657 |
| 29 | Advertising and Brand Strategy, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21716&returnto=4657 |
| 30 | Media Arts, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21380&returnto=4657 |
| 31 | Technical Communication, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21373&returnto=4657 |

##### Department of Philosophy and Religion
###### BA
| # | 专业 | URL |
|---|------|-----|
| 32 | Philosophy, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21365&returnto=4657 |

##### Department of Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 33 | Political Science, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21372&returnto=4657 |
| 34 | Urban Policy and Planning, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21606&returnto=4657 |

##### Department of Psychology
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 35 | Psychology, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21377&returnto=4657 |
| 36 | Psychology, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21378&returnto=4657 |

##### Department of Sociology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 37 | Sociology, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21515&returnto=4657 |
| 38 | Sociology with a concentration in Sports Culture, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22280&returnto=4657 |

##### Department of World Languages, Literatures, and Cultures
###### BA
| # | 专业 | URL |
|---|------|-----|
| 39 | French, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21269&returnto=4657 |
| 40 | German Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21283&returnto=4657 |
| 41 | Japanese, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21575&returnto=4657 |
| 42 | Spanish, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21404&returnto=4657 |

##### Department of Classical & Modern Languages (cross-listed content-strategy)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 43 | Content Strategy, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21593&returnto=4657 |

##### Interdisciplinary (CLASS)
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 44 | Integrative Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21274&returnto=4657 |
| 45 | Integrative Studies, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21484&returnto=4657 |

---

#### School of Merchandising and Hospitality Management
##### Department of Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21296&returnto=4657 |
| 2 | Hospitality Management, BS (Hospitality, Nutrition and Food Science teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21294&returnto=4657 |
| 3 | Event Design and Experience Management, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21665&returnto=4657 |

##### Department of Merchandising and Digital Retailing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 4 | Merchandising with a concentration in Fashion Merchandising, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21692&returnto=4657 |
| 5 | Merchandising with a concentration in Furnishings and Décor, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21693&returnto=4657 |
| 6 | Interdisciplinary Studies in Consumer Insights, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21580&returnto=4657 |

---

#### College of Music
##### Department of Composition Studies
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Composition, BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21223&returnto=4657 |

##### Department of Jazz Studies
###### BM
| # | 专业 | URL |
|---|------|-----|
| 2 | Jazz Studies (instrumental, arranging or vocal emphasis), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21310&returnto=4657 |

##### Department of Music Education
###### BM
| # | 专业 | URL |
|---|------|-----|
| 3 | Music Education (Specialization: Choral–Keyboard or Guitar), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21694&returnto=4657 |
| 4 | Music Education (Specialization: Choral–Vocal), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21695&returnto=4657 |
| 5 | Music Education (Specialization: Instrumental–Band, Woodwinds, Brass or Percussion), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21696&returnto=4657 |
| 6 | Music Education (Specialization: Instrumental–Band/Orchestra), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21697&returnto=4657 |
| 7 | Music Education (Specialization: Instrumental–Elementary), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21698&returnto=4657 |
| 8 | Music Education (Specialization: Instrumental–Orchestra), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21699&returnto=4657 |

##### Department of Performance
###### BM
| # | 专业 | URL |
|---|------|-----|
| 9 | Performance (specialization: Harpsichord), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21356&returnto=4657 |
| 10 | Performance (specialization: Orchestral Instruments - Multiple Woodwinds), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21357&returnto=4657 |
| 11 | Performance (specialization: Orchestral Instruments), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21358&returnto=4657 |
| 12 | Performance (specialization: Organ), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21359&returnto=4657 |
| 13 | Performance (specialization: Organ, Church Music Emphasis), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21360&returnto=4657 |
| 14 | Performance (specialization: Piano), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21362&returnto=4657 |
| 15 | Performance (specialization: Voice), BM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21363&returnto=4657 |

##### Bachelor of Arts in Music (interdisciplinary with CLASS)
###### BA
| # | 专业 | URL |
|---|------|-----|
| 16 | Music, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21350&returnto=4657 |
| 17 | Commercial Music, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21748&returnto=4657 |
| 18 | Critical Studies in Music and Society, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21681&returnto=4657 |

---

#### College of Public Affairs and Health Sciences
##### Department of Audiology and Speech-Language Pathology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Audiology and Speech-Language Pathology, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21406&returnto=4657 |

##### Department of Rehabilitation and Health Services
###### BS
| # | 专业 | URL |
|---|------|-----|
| 2 | Addiction Studies, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21664&returnto=4657 |
| 3 | Applied Behavior Analysis, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21189&returnto=4657 |
| 4 | Public Health, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21552&returnto=4657 |
| 5 | Public Health with a concentration in Health Professions, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22246&returnto=4657 |
| 6 | Rehabilitation Studies, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21388&returnto=4657 |

##### Department of Social Work
###### BSW
| # | 专业 | URL |
|---|------|-----|
| 7 | Social Work, BSW | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21399&returnto=4657 |

##### Department of Criminal Justice
###### BS
| # | 专业 | URL |
|---|------|-----|
| 8 | Criminal Justice, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21232&returnto=4657 |

##### Department of Emergency Management and Disaster Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 9 | Emergency Administration and Planning, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21254&returnto=4657 |

##### Department of Human Development and Family Science (cross-listed Life Sciences; in this college via Health)
###### BS
| # | 专业 | URL |
|---|------|-----|
| 10 | Human Development and Family Science with a concentration in Individual and Family Development across the Lifespan, BS (non–teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21491&returnto=4657 |
| 11 | Human Development and Family Science with a concentration in Community and Family Services, BS (non–teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21239&returnto=4657 |
| 12 | Human Development and Family Science, BS (teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21240&returnto=4657 |

##### Department of Public Administration (interdisciplinary also)
###### BA / BS
| # | 专业 | URL |
|---|------|-----|
| 13 | Nonprofit Leadership Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21298&returnto=4657 |

---

#### College of Science
##### Department of Biological Sciences
###### BA / BSBIO
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21205&returnto=4657 |
| 2 | Biology, BSBIO | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21206&returnto=4657 |
| 3 | Biology with a concentration in Forensic Science, BSBIO | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21677&returnto=4657 |
| 4 | Medical Laboratory Sciences, BSMLS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21340&returnto=4657 |

##### Department of Chemistry and Biochemistry
###### BA / BSBC / BSCHM
| # | 专业 | URL |
|---|------|-----|
| 5 | Biochemistry, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21201&returnto=4657 |
| 6 | Biochemistry, BSBC | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21202&returnto=4657 |
| 7 | Biochemistry with a concentration in Forensic Science, BSBC | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21671&returnto=4657 |
| 8 | Chemistry, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21214&returnto=4657 |
| 9 | Chemistry, BSCHM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21215&returnto=4657 |
| 10 | Chemistry with a concentration in Forensics, BSCHM | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21670&returnto=4657 |
| 11 | Chemistry with a Concentration in Computational Chemistry, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22247&returnto=4657 |

##### Department of Mathematics
###### BA / BSMTH
| # | 专业 | URL |
|---|------|-----|
| 12 | Mathematics with a concentration in Computer Science, BSMTH | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21752&returnto=4657 |
| 13 | Mathematics, BA (non–teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21331&returnto=4657 |
| 14 | Mathematics, BA (teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21332&returnto=4657 |
| 15 | Mathematics, BSMTH (non–teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21333&returnto=4657 |
| 16 | Mathematics, BSMTH (teacher certification) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21334&returnto=4657 |

##### Department of Physics
###### BSPHY
| # | 专业 | URL |
|---|------|-----|
| 17 | Physics, BSPHY | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21369&returnto=4657 |
| 18 | Physics with a concentration in Astrophysics, BSPHY | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21685&returnto=4657 |
| 19 | Physics with a concentration in Computational Physics, BSPHY | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21684&returnto=4657 |
| 20 | Physics with a concentration in Engineering Physics, BSPHY | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21667&returnto=4657 |

##### Interdisciplinary
###### BS
| # | 专业 | URL |
|---|------|-----|
| 21 | Applied Project Design and Analysis, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21652&returnto=4657 |
| 22 | Project Design and Analysis, BS | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21637&returnto=4657 |

---

#### College of Visual Arts and Design
##### Department of Art Education and Art History
###### BFA / BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art Education, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21418&returnto=4657 |
| 2 | Art History, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21195&returnto=4657 |

##### Department of Design (Communication Design)
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 3 | Communication Design with a concentration in Graphic Design, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21621&returnto=4657 |
| 4 | Communication Design with a concentration in User-Experience Design, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21622&returnto=4657 |

##### Department of Fashion Design (cross-listed w/ Merchandising & Hospitality)
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 5 | Fashion Design, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21262&returnto=4657 |
| 6 | Interior Design, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21304&returnto=4657 |

##### Department of Studio Art
###### BFA
| # | 专业 | URL |
|---|------|-----|
| 7 | Studio Art with a concentration in Ceramics, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21429&returnto=4657 |
| 8 | Studio Art with a concentration in Drawing and Painting, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21430&returnto=4657 |
| 9 | Studio Art with a concentration in Metalsmithing and Jewelry, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21432&returnto=4657 |
| 10 | Studio Art with a concentration in New Media Art, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21433&returnto=4657 |
| 11 | Studio Art with a concentration in Photography, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21434&returnto=4657 |
| 12 | Studio Art with a concentration in Printmaking, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21435&returnto=4657 |
| 13 | Studio Art with a concentration in Sculpture, BFA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21436&returnto=4657 |

##### Interdisciplinary
###### BA
| # | 专业 | URL |
|---|------|-----|
| 14 | Interdisciplinary Art and Design Studies with a concentration in Arts Management, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21535&returnto=4657 |
| 15 | Interdisciplinary Art and Design Studies with a concentration in Design Management, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21540&returnto=4657 |
| 16 | Interdisciplinary Art and Design Studies, BA | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21303&returnto=4657 |

##### Pre-major (BFA studio entry — for assigned freshmen in Studio Art)
| # | Pre-Major | URL |
|---|------|-----|
| 17 | Studio Art pre-major | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21449&returnto=4657 |

##### College of Business pre-major (BBA entry):
| # | Pre-Major | URL |
|---|------|-----|
| 18 | Bachelor of Business Administration (pre-major listing) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21199&returnto=4657 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

The following majors have authority in more than one college (per catalog listing for cross-listing, captured 2026-07-07 at `/content.php?catoid=40&navoid=4657`):

- **Computer Science** (BS) — home unit: College of Engineering (Department of Computer Science and Engineering). The College of Science lists a related BS in Data Science (cross-college) and a related BSMTH with Computer Science concentration.
- **Economics** (BA/BBA/BSECO) — home unit: College of Liberal Arts and Social Sciences; BBA variant is administered in G. Brint Ryan College of Business.
- **Mathematics with a concentration in Computer Science** (BSMTH) — joint College of Science + College of Engineering.
- **Theatre** (BA) — program shared by College of Liberal Arts and Social Sciences (Dance & Theatre Arts Dept) and listed alongside College of Music performance tracks; many BA theatre concentrations overlap with Music's performance offerings (e.g., Dance).
- **Interior Design / Fashion Design** (BFA) — College of Visual Arts and Design with strong cross-listings to School of Merchandising and Hospitality Management.
- **Social Science** (BS, teacher certification) — College of Liberal Arts and Social Sciences, with social-studies teacher-certification jointly administered through College of Education.
- **Applied Arts and Sciences, BAAS** (with 24 concentrations) — interdisciplinary by design; concentrations span Information Technology, Computer Science, Industrial Distribution, Logistics, Leadership, Recreation, Public Safety, Public Health, etc. — administratively housed in College of Liberal Arts and Social Sciences (Anthropology-anchored).

### 1.4 Minors — complete list (91 minors)

Source: `catoid=40&navoid=4657` Minors section, 2026-07-07.

| # | Minor | Home college/department | URL |
|---|------|------|-----|
| 1 | Accounting | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21178&returnto=4657 |
| 2 | Addiction Studies | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21242&returnto=4657 |
| 3 | Advertising | College of Liberal Arts and Social Sciences (Mayborn School of Journalism) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21717&returnto=4657 |
| 4 | Aerospace Studies | (ROTC/Interdisciplinary) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21182&returnto=4657 |
| 5 | Anthropology | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21186&returnto=4657 |
| 6 | Art History | College of Visual Arts and Design | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21194&returnto=4657 |
| 7 | Audiology and Speech-Language Pathology | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21405&returnto=4657 |
| 8 | Behavior Analysis | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21620&returnto=4657 |
| 9 | Biological Sciences | College of Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21203&returnto=4657 |
| 10 | Biomedical Engineering | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21586&returnto=4657 |
| 11 | Business Analytics | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21200&returnto=4657 |
| 12 | Business Computer Information Systems | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21207&returnto=4657 |
| 13 | Business Foundations | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21209&returnto=4657 |
| 14 | Chemistry | College of Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21212&returnto=4657 |
| 15 | Commercial Music | College of Music | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21680&returnto=4657 |
| 16 | Communication Studies | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21221&returnto=4657 |
| 17 | Computer Science and Engineering | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21226&returnto=4657 |
| 18 | Conflict and Human Security | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21355&returnto=4657 |
| 19 | Conflict Resolution | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21185&returnto=4657 |
| 20 | Construction Management | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21753&returnto=4657 |
| 21 | Consumer Insights | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21597&returnto=4657 |
| 22 | Content Strategy | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21756&returnto=4657 |
| 23 | Counseling | College of Education | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21230&returnto=4657 |
| 24 | Criminal Justice | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21231&returnto=4657 |
| 25 | Cybersecurity | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21657&returnto=4657 |
| 26 | Digital Business and E-commerce | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21687&returnto=4657 |
| 27 | Economics | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21245&returnto=4657 |
| 28 | Electrical Engineering | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21490&returnto=4657 |
| 29 | Emergency Administration and Planning | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21253&returnto=4657 |
| 30 | English | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21257&returnto=4657 |
| 31 | Enology and Brewing | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21830&returnto=4657 |
| 32 | Entrepreneurship and Enterprise Management | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21259&returnto=4657 |
| 33 | Environmental Studies | College of Liberal Arts and Social Sciences (Geography-anchored) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21829&returnto=4657 |
| 34 | Finance | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21444&returnto=4657 |
| 35 | Financial Planning | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21265&returnto=4657 |
| 36 | French | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21268&returnto=4657 |
| 37 | Furnishings and Décor Merchandising | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21290&returnto=4657 |
| 38 | Geography | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21278&returnto=4657 |
| 39 | German | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21282&returnto=4657 |
| 40 | Health Promotion | College of Education (Kinesiology/Health) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21285&returnto=4657 |
| 41 | History | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21287&returnto=4657 |
| 42 | Hospitality Management | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21295&returnto=4657 |
| 43 | Human Development and Family Science | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21238&returnto=4657 |
| 44 | Human Resource | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21765&returnto=4657 |
| 45 | Human Services | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21299&returnto=4657 |
| 46 | Information Management and Health Informatics | College of Information | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21504&returnto=4657 |
| 47 | Information Science and Knowledge Organization | College of Information | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21503&returnto=4657 |
| 48 | International Studies | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21306&returnto=4657 |
| 49 | Japanese | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21309&returnto=4657 |
| 50 | Jewish Studies | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21311&returnto=4657 |
| 51 | Journalism | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21312&returnto=4657 |
| 52 | Kinesiology | College of Education | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21315&returnto=4657 |
| 53 | Legal Studies in Business | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21319&returnto=4657 |
| 54 | Legal Studies | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21762&returnto=4657 |
| 55 | Logistics and Supply Chain Management | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21489&returnto=4657 |
| 56 | Management | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21323&returnto=4657 |
| 57 | Marketing | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21324&returnto=4657 |
| 58 | Materials Science and Engineering | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21326&returnto=4657 |
| 59 | Mathematics and Science Secondary Teaching | College of Education (interdisciplinary) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21328&returnto=4657 |
| 60 | Mathematics | College of Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21329&returnto=4657 |
| 61 | Mechanical and Energy Engineering | College of Engineering | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21553&returnto=4657 |
| 62 | Merchandising | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21341&returnto=4657 |
| 63 | Military Science | Interdisciplinary (Army ROTC) | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21346&returnto=4657 |
| 64 | Music | College of Music | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21348&returnto=4657 |
| 65 | Music Theory | College of Music | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21624&returnto=4657 |
| 66 | Nonprofit Leadership Studies | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21318&returnto=4657 |
| 67 | Nutrition | School of Merchandising and Hospitality Management | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21832&returnto=4657 |
| 68 | Philosophy | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21364&returnto=4657 |
| 69 | Photography | College of Visual Arts and Design | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21366&returnto=4657 |
| 70 | Physics | College of Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21367&returnto=4657 |
| 71 | Political Science | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21371&returnto=4657 |
| 72 | Professional Selling | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21501&returnto=4657 |
| 73 | Psychology | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21376&returnto=4657 |
| 74 | Public Administration | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21379&returnto=4657 |
| 75 | Public Health | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21635&returnto=4657 |
| 76 | Real Estate | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21381&returnto=4657 |
| 77 | Recreation, Event and Sport Management (for non-majors) | College of Education | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21384&returnto=4657 |
| 78 | Rehabilitation Studies | College of Public Affairs and Health Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21387&returnto=4657 |
| 79 | Religious Studies | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21389&returnto=4657 |
| 80 | Residential Property Management | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21391&returnto=4657 |
| 81 | Risk Management and Insurance | G. Brint Ryan College of Business | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21302&returnto=4657 |
| 82 | Secondary and All-level (EC-12) Education Teacher Certification (for BA, BS) | College of Education | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21395&returnto=4657 |
| 83 | Social Science | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21397&returnto=4657 |
| 84 | Sociology | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21400&returnto=4657 |
| 85 | Spanish | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21403&returnto=4657 |
| 86 | Statistics | College of Science | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21409&returnto=4657 |
| 87 | Studio Art | College of Visual Arts and Design | https://catalog.unt.edu/preview_program.php?catoid=40&poid=22362&returnto=4657 |
| 88 | Teaching English in a Global Context | College of Education | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21720&returnto=4657 |
| 89 | Technical Communication | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21413&returnto=4657 |
| 90 | Theatre | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21415&returnto=4657 |
| 91 | Urban Policy and Planning | College of Liberal Arts and Social Sciences | https://catalog.unt.edu/preview_program.php?catoid=40&poid=21630&returnto=4657 |

### 1.5 General/Institute-wide requirements

UNT undergraduate students must complete the **University Core Curriculum** (42 semester credit hours total) plus college-specific degree requirements (per the catalog's "University Core Curriculum" page at `/content.php?catoid=40&navoid=4670`, captured 2026-07-07). Core Curriculum consists of six Foundational Component Areas (FCAs):
- Communication (English Composition I & II; Communication [public speaking])
- Mathematics
- Life and Physical Sciences
- Language, Philosophy and Culture
- American History
- Government/Political Science

Plus three **Core Category Options**: Creative Arts; Social and Behavioral Sciences; Component Area Option (a course from one of the foundational areas not already used).

UNT also has the **Honors College** (a small-college-within-the-university experience) that accepts incoming freshmen by invitation/admission; honors courses substitute into the University Core Curriculum (per `/content.php?catoid=40&poid=21292&returnto=4657`, "Honors Courses that meet University Core Curriculum requirements").

### 1.6 Course-ID → Major quick-lookup

UNT does **not** number programs numerically (no MIT-style "course 6 = EECS"). Programs are referenced by full name plus a college/school. The catalog uses the `poid=<id>` URL parameter — a stable internal ID for each program page — for example:

- `poid=21250` → Electrical Engineering, BS
- `poid=21365` → Philosophy, BA
- `poid=21227` → Computer Science, BS
- `poid=21289` → History, BA

The numbering scheme lives at the program-page level; for cross-school comparison, treat programs as text-keyed by name. The **college-by-college** organization (Sections 1.2) is the equivalent grouping for UNT.


---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

UNT's graduate programs are administered through the **Toulouse Graduate School (TGS)** in partnership with the eleven undergraduate colleges. The TGS website (https://www.unt.edu/graduate/index.html — formerly https://tgs.unt.edu/) houses a program finder at https://search.unt.edu/s/search.html?collection=unt%7Esp-program-finder. Master's filter: 102 listings; Doctoral filter: 50 listings; total 152 grad programs (verified via `https://search.unt.edu/s/search.html?collection=unt%7Esp-program-finder&sort=title&num_ranks=200&f.Classification%7CClassification=Master%27s` and same with `Doctoral`, captured 2026-07-07).

The Toulouse Graduate School does **not subdivide into separate "departments"** for student-facing purposes; programs run through their home college/department. The grouping below uses the **undergraduate college** (anchor school) as the parent, then degree level. Where a graduate program is interdisciplinary or has no clear college anchor, it's filed under Toulouse Graduate School.

#### Toulouse Graduate School (interdisciplinary / admin-managed)
##### Master of Arts (MA) / Master of Science (MS) [crossover programs not anchored to a UG college]
| # | Program | URL |
|---|------|-----|
| 1 | Interdisciplinary Studies Master's | https://www.unt.edu/academics/programs/interdisciplinary-studies-masters.html |
| 2 | Library Science Master's | https://www.unt.edu/academics/programs/library-science-masters.html |
| 3 | Special Education (Minor and Master's combined) | https://www.unt.edu/academics/programs/special-education-minor-and-masters.html |
| 4 | Secondary Education Teaching Master's | https://www.unt.edu/academics/programs/secondary-education-teaching-masters.html |

##### Advanced Certificates / Diplomas
| # | Program | URL |
|---|------|-----|
| 5 | Data Analytics Certificate | https://www.unt.edu/academics/programs/data-analytics-certificate.html |
| 6 | Specialist in Aging Certificate | https://www.unt.edu/academics/programs/specialist-in-aging-certificate.html |
| 7 | Technical Writing Certificate (GAC) | https://www.unt.edu/academics/programs/technical-writing-gac.html |
| 8 | School Counseling Certificate | https://www.unt.edu/academics/programs/school-counseling-certificate.html |
| 9 | School Librarian Certification | https://www.unt.edu/academics/programs/school-librarian-certification.html |

#### G. Brint Ryan College of Business — Graduate
##### Master of Business Administration (MBA)
| # | Program | URL |
|---|------|-----|
| 1 | Business Analytics M.B.A. | https://www.unt.edu/academics/programs/business-analytics-mba.html |
| 2 | Artificial Intelligence M.B.A. | https://www.unt.edu/academics/programs/artificial-intelligence-mba.html |
| 3 | Finance M.B.A. | https://www.unt.edu/academics/programs/finance-mba.html |
| 4 | M.B.A. in Management Consulting | https://www.unt.edu/academics/programs/management-masters.html |
| 5 | MBA with a concentration in Financial Planning | https://www.unt.edu/academics/programs/financial-planning-masters.html |
| 6 | MBA with a concentration in Health Services Management | https://www.unt.edu/academics/programs/health-services-management-masters.html |
| 7 | MBA with a concentration in Marketing | https://www.unt.edu/academics/programs/marketing-masters.html |
| 8 | MBA with a concentration in Marketing Analytics | https://www.unt.edu/academics/programs/marketing-analytics-masters.html |
| 9 | MBA with a concentration in Strategic Management | https://www.unt.edu/academics/programs/strategic-management-masters.html |

##### Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 10 | Advanced Data Analytics Master's | https://www.unt.edu/academics/programs/advanced-data-analytics-masters.html |
| 11 | Business Analytics Master's | https://www.unt.edu/academics/programs/business-analytics-masters.html |
| 12 | Business Studies Master's | https://www.unt.edu/academics/programs/business-studies-masters.html |
| 13 | Corporate Accounting Master's | https://www.unt.edu/academics/programs/corporate-accounting-masters.html |
| 14 | Finance Master's | https://www.unt.edu/academics/programs/finance-masters.html |
| 15 | Supply Chain Analytics Master's | https://www.unt.edu/academics/programs/supply-chain-analytics-masters.html |
| 16 | Supply Chain Management Master's | https://www.unt.edu/academics/programs/supply-chain-management-masters.html |

##### Combined Degrees (BS + MS / BBA + MS)
| # | Program | URL |
|---|------|-----|
| 17 | Accounting Bachelor's & Master's Dual Degree | https://www.unt.edu/academics/programs/combined-accounting-degrees.html |
| 18 | Combined Business Analytics Degrees | https://www.unt.edu/academics/programs/combined-business-analytics-degrees.html |
| 19 | Combined Finance Degrees | https://www.unt.edu/academics/programs/combined-finance-degrees.html |

##### Doctorate (PhD / DBA)
| # | Program | URL |
|---|------|-----|
| 20 | Accounting Ph.D. | https://www.unt.edu/academics/programs/accounting-phd.html |
| 21 | Business Information Assurance Ph.D. | https://www.unt.edu/academics/programs/business-information-assurance-phd.html |
| 22 | Finance Ph.D. | https://www.unt.edu/academics/programs/finance-phd.html |
| 23 | Management Ph.D. | https://www.unt.edu/academics/programs/management-phd.html |
| 24 | Management Science Ph.D. | https://www.unt.edu/academics/programs/management-science-phd.html |
| 25 | Marketing Ph.D. | https://www.unt.edu/academics/programs/marketing-phd.html |
| 26 | Supply Chain Management Ph.D. | https://www.unt.edu/academics/programs/logistics-phd.html |
| 27 | Doctor of Business Administration (DBA) | https://www.unt.edu/academics/programs/doctor-business-administration.html |

##### Graduate Academic Certificate (GAC)
| # | Program | URL |
|---|------|-----|
| 28 | Artificial Intelligence in Business Graduate Academic Certificate | https://www.unt.edu/academics/programs/artificial-intelligence-in-business-gac.html |

#### College of Education — Graduate
##### Master of Arts (MA) / Master of Education equivalent
| # | Program | URL |
|---|------|-----|
| 1 | Counseling Master's: School Counseling Track | https://www.unt.edu/academics/programs/school-counseling-masters.html |
| 2 | Curriculum and Instruction Master's | https://www.unt.edu/academics/programs/curriculum-and-instruction-masters.html |
| 3 | Educational Leadership Master's | https://www.unt.edu/academics/programs/educational-leadership-masters.html |
| 4 | Higher Education Master's | https://www.unt.edu/academics/programs/higher-education-masters.html |
| 5 | Autism Intervention Special Education Master's | https://www.unt.edu/academics/programs/autism-intervention-special-education-masters.html |

##### Doctorate (EdD / PhD)
| # | Program | URL |
|---|------|-----|
| 6 | Educational Leadership Ed.D. | https://www.unt.edu/academics/programs/educational-leadership-edd.html |
| 7 | Educational Leadership Ph.D. | https://www.unt.edu/academics/programs/educational-leadership-phd.html |
| 8 | Higher Education Ed.D. | https://www.unt.edu/academics/programs/higher-education-edd.html |
| 9 | Higher Education Ph.D. | https://www.unt.edu/academics/programs/higher-education-phd.html |
| 10 | Learning Technologies Ph.D. (joint with College of Information) | https://www.unt.edu/academics/programs/learning-technologies-phd.html |
| 11 | Behavioral Science Ph.D. | https://www.unt.edu/academics/programs/behavioral-science-phd.html |

#### College of Engineering — Graduate
##### Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 1 | Artificial Intelligence Master's | https://www.unt.edu/academics/programs/artificial-intelligence-masters.html |
| 2 | Biomedical Engineering Master's | https://www.unt.edu/academics/programs/biomedical-engineering-masters.html |
| 3 | Computer Engineering Master's | https://www.unt.edu/academics/programs/computer-engineering-masters.html |
| 4 | Computer Science Master's | https://www.unt.edu/academics/programs/computer-science-masters.html |
| 5 | Cybersecurity Master's | https://www.unt.edu/academics/programs/cybersecurity-masters.html |
| 6 | Data Engineering Master's | https://www.unt.edu/academics/programs/data-engineering-masters.html |
| 7 | Electrical Engineering Master's | https://www.unt.edu/academics/programs/electrical-engineering-masters.html |
| 8 | Engineering Management Master's | https://www.unt.edu/academics/programs/engineering-management-masters.html |
| 9 | Materials Science and Engineering Master's | https://www.unt.edu/academics/programs/materials-science-engineering-masters.html (URL inferred; poid 21549 cat. refers to this pathway) |
| 10 | Mechanical and Energy Engineering Master's | (per program finder listing) |

##### Doctorate (PhD)
| # | Program | URL |
|---|------|-----|
| 11 | Biomedical Engineering Ph.D. | https://www.unt.edu/academics/programs/biomedical-engineering-phd.html |
| 12 | Computer Science and Engineering Ph.D. | https://www.unt.edu/academics/programs/computer-science-and-engineering-phd.html |
| 13 | Electrical Engineering Ph.D. | https://www.unt.edu/academics/programs/electrical-engineering-phd.html |
| 14 | Materials Science and Engineering Ph.D. | (referenced in Grad Track Options) |
| 15 | Mechanical and Energy Engineering Ph.D. | https://www.unt.edu/academics/programs/mechanical-energy-engineering-phd.html (referenced in catalog) |

#### College of Information — Graduate
##### Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 1 | Information Science Master's | https://www.unt.edu/academics/programs/information-science-masters.html |
| 2 | Information Technology Master's | https://www.unt.edu/academics/programs/information-technology-masters.html |
| 3 | Learning Technologies Master's | https://www.unt.edu/academics/programs/learning-technologies-masters.html |
| 4 | Health Informatics Master's | https://www.unt.edu/academics/programs/health-informatics-masters.html |
| 5 | Library Science Master's | https://www.unt.edu/academics/programs/library-science-masters.html |

##### Combined Degrees
| # | Program | URL |
|---|------|-----|
| 6 | Information Science Combined Degrees | https://www.unt.edu/academics/programs/information-science-combined-degrees.html |

##### Doctorate (PhD)
| # | Program | URL |
|---|------|-----|
| 7 | Information Science Ph.D. | https://www.unt.edu/academics/programs/information-science-phd.html |
| 8 | Information Science Ph.D. With a Concentration in Data Science | https://www.unt.edu/academics/programs/information-science-phd-data-science.html |
| 9 | Information Science Ph.D. With a Concentration in Journalism | https://www.unt.edu/academics/programs/information-science-phd-journalism.html |
| 10 | Learning Technologies Ph.D. | https://www.unt.edu/academics/programs/learning-technologies-phd.html |

#### College of Liberal Arts and Social Sciences (CLASS) — Graduate
##### Master of Arts (MA)
| # | Program | URL |
|---|------|-----|
| 1 | Applied Anthropology Master's | https://www.unt.edu/academics/programs/applied-anthropology-masters.html |
| 2 | Art History Master's Degree | https://www.unt.edu/academics/programs/art-history-masters-degree.html |
| 3 | Communication Studies Master's | https://www.unt.edu/academics/programs/communication-studies-masters.html |
| 4 | English as a Second Language Master's | https://www.unt.edu/academics/programs/english-as-a-second-language-masters.html |
| 5 | English Master's | https://www.unt.edu/academics/programs/english-masters.html |
| 6 | Geography Master's | https://www.unt.edu/academics/programs/geography-masters.html |
| 7 | History Master's Degree | https://www.unt.edu/academics/programs/history-masters-degree.html |
| 8 | International Studies Master's | https://www.unt.edu/academics/programs/international-studies-masters.html |
| 9 | Journalism Master's | https://www.unt.edu/academics/programs/journalism-masters.html |
| 10 | Philosophy Master's | https://www.unt.edu/academics/programs/philosophy-masters.html |
| 11 | Political Science Master's | https://www.unt.edu/academics/programs/political-science-masters.html |
| 12 | Sociology Master's Degree | https://www.unt.edu/academics/programs/sociology-masters-degree.html |
| 13 | Public Administration Master's | https://www.unt.edu/academics/programs/public-administration-masters.html |

##### Combined Degrees
| # | Program | URL |
|---|------|-----|
| 14 | Art History Combined Degrees | https://www.unt.edu/academics/programs/art-history-combined-degrees.html |
| 15 | Combined Criminal Justice Degrees | https://www.unt.edu/academics/programs/combined-criminal-justice-degrees.html |
| 16 | Combined English Literature Degrees | https://www.unt.edu/academics/programs/combined-english-literature-degrees.html |
| 17 | Combined Journalism Degrees | https://www.unt.edu/academics/programs/combined-journalism-degrees.html |
| 18 | Combined Philosophy Degrees | https://www.unt.edu/academics/programs/philosophy-combined-degrees.html |
| 19 | Combined Political Science Degrees | https://www.unt.edu/academics/programs/combined-political-science-degrees.html |
| 20 | Combined Sociology Degrees | https://www.unt.edu/academics/programs/combined-sociology-degrees.html |

##### Doctorate (PhD)
| # | Program | URL |
|---|------|-----|
| 21 | English Ph.D. | https://www.unt.edu/academics/programs/english-phd.html |
| 22 | English Ph.D. with a concentration in Creative Writing | https://www.unt.edu/academics/programs/english-creative-writing-phd.html |
| 23 | History Ph.D. with a Concentration in Body, Place and Identity | https://www.unt.edu/academics/programs/body-place-and-identity-history-phd.html |
| 24 | History Ph.D. with a concentration in European History | https://www.unt.edu/academics/programs/european-history-phd.html |
| 25 | History Ph.D. with a concentration in Military History | https://www.unt.edu/academics/programs/military-history-phd.html |
| 26 | U.S. History Ph.D. | https://www.unt.edu/academics/programs/us-history-phd.html |
| 27 | Political Science Ph.D. | https://www.unt.edu/academics/programs/political-science-doctoral-degree.html |
| 28 | Sociology Ph.D. | https://www.unt.edu/academics/programs/sociology-phd.html |
| 29 | Philosophy Ph.D. | https://www.unt.edu/academics/programs/philosophy-phd.html |
| 30 | Clinical Psychology Ph.D. | https://www.unt.edu/academics/programs/clinical-psychology-phd.html |
| 31 | Counseling Psychology Ph.D. | https://www.unt.edu/academics/programs/counseling-psychology-phd.html |
| 32 | Human Geography Philosophy Ph.D. (interdisciplinary) | https://www.unt.edu/academics/programs/human-geography-philosophy-phd.html |

##### Graduate Academic Certificate (GAC)
| # | Program | URL |
|---|------|-----|
| 33 | Technical Writing Certificate (GAC) | https://www.unt.edu/academics/programs/technical-writing-gac.html |

#### School of Merchandising and Hospitality Management — Graduate
##### Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 1 | Hospitality Management Master's | https://www.unt.edu/academics/programs/hospitality-management-masters.html |
| 2 | Merchandising and Digital Retailing MS (referenced in catalog as "Merchandising MS") | https://www.unt.edu/academics/programs/merchandising-masters.html |

##### Combined Degrees
| # | Program | URL |
|---|------|-----|
| 3 | Combined Merchandising Degrees | https://www.unt.edu/academics/programs/combined-merchandising-degrees.html |

#### College of Music — Graduate
##### Master of Music (interpreted as MA-equivalent for cross-school matrix; UNT labels them "Master's" with "MM" abbreviation in some listings)
| # | Program | URL |
|---|------|-----|
| 1 | Conducting Performance Master's | https://www.unt.edu/academics/programs/conducting-performance-masters.html |
| 2 | Ethnomusicology Master's | https://www.unt.edu/academics/programs/ethnomusicology-masters.html |
| 3 | Jazz Studies Master's | https://www.unt.edu/academics/programs/jazz-studies-masters.html |
| 4 | Music Business Master's | https://www.unt.edu/academics/programs/music-business-masters.html |
| 5 | Music Composition Master's | https://www.unt.edu/academics/programs/music-composition-masters.html |
| 6 | Music Education Master's | https://www.unt.edu/academics/programs/music-education-masters.html |
| 7 | Music Performance Master's | https://www.unt.edu/academics/programs/music-performance-masters.html |
| 8 | Music Theory Master's | https://www.unt.edu/academics/programs/music-theory-masters.html |
| 9 | Musicology Master's | https://www.unt.edu/academics/programs/musicology-masters.html |

##### Doctorate (DMA-equivalent — labeled "Doctoral Degree" / PhD with music concentration)
| # | Program | URL |
|---|------|-----|
| 10 | Jazz Performance Doctoral Degree | https://www.unt.edu/academics/programs/jazz-performance-doctoral-degree.html |
| 11 | Music Performance Doctoral Degree | https://www.unt.edu/academics/programs/music-performance-doctoral-degree.html |
| 12 | Music Ph.D. with a concentration in Composition | https://www.unt.edu/academics/programs/music-composition-phd.html |
| 13 | Music Ph.D. with a concentration in Ethnomusicology | https://www.unt.edu/academics/programs/ethnomusicology-phd.html |
| 14 | Music Ph.D. with a concentration in Music Theory | https://www.unt.edu/academics/programs/music-theory-phd.html |
| 15 | Music Ph.D. with a concentration in Musicology | https://www.unt.edu/academics/programs/musicology-phd.html |
| 16 | Ph.D. in Music with a Concentration in Music Education | https://www.unt.edu/academics/programs/music-education-phd.html |
| 17 | Doctor of Music (Artist) — Grad Artist Certificate in Music Performance | https://www.unt.edu/academics/programs/gac-music-performance.html |

#### College of Public Affairs and Health Sciences — Graduate
##### Master of Arts (MA) / Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 1 | Applied Behavior Analysis Master's | https://www.unt.edu/academics/programs/applied-behavior-analysis-masters.html |
| 2 | Behavior Analysis Master's | https://www.unt.edu/academics/programs/behavior-analysis-masters.html |
| 3 | Rehabilitation Counseling Master's | https://www.unt.edu/academics/programs/rehabilitation-counseling-masters.html |
| 4 | Social Work Master's (MSW) | https://www.unt.edu/academics/programs/social-work-masters.html |
| 5 | Speech-Language Pathology Master's | https://www.unt.edu/academics/programs/speech-language-pathology-masters.html |

##### Combined Degrees
| # | Program | URL |
|---|------|-----|
| 6 | Combined Criminal Justice Degrees (catalog also lists under this college for joint MPA path) | https://www.unt.edu/academics/programs/combined-criminal-justice-degrees.html |

##### Doctorate (PhD / AuD)
| # | Program | URL |
|---|------|-----|
| 7 | Doctor of Audiology (Au.D.) | https://www.unt.edu/academics/programs/doctor-of-audiology-aud-.html |
| 8 | Health Sciences Ph.D. | https://www.unt.edu/academics/programs/health-sciences-phd.html |
| 9 | Exercise Physiology Biology Ph.D. (interdisciplinary w/ College of Science) | https://www.unt.edu/academics/programs/exercise-physiology-biology-phd.html |

#### College of Science — Graduate
##### Master of Science (MS)
| # | Program | URL |
|---|------|-----|
| 1 | Biology Master's | https://www.unt.edu/academics/programs/biology-masters.html |
| 2 | Chemistry Master's | https://www.unt.edu/academics/programs/chemistry-masters.html |
| 3 | Data Science Master's | https://www.unt.edu/academics/programs/data-science-masters.html |
| 4 | Environmental Science Master's | https://www.unt.edu/academics/programs/environmental-science-masters.html |
| 5 | Master of Science in Mathematics (Mathematics Education Concentration) | https://www.unt.edu/academics/programs/mathematics-education-masters.html |
| 6 | Mathematics Master's | https://www.unt.edu/academics/programs/mathematics-masters.html |
| 7 | Physics Master's | https://www.unt.edu/academics/programs/physics-masters.html |

##### Combined Degrees
| # | Program | URL |
|---|------|-----|
| 8 | Combined Chemistry Degrees | https://www.unt.edu/academics/programs/combined-chemistry-degrees.html |
| 9 | Combined Physics Degrees | https://www.unt.edu/academics/programs/combined-physics-degrees.html |
| 10 | Mathematics Combined Degrees | https://www.unt.edu/academics/programs/mathematics-combined-degrees.html |

##### Doctorate (PhD)
| # | Program | URL |
|---|------|-----|
| 11 | Biochemistry and Molecular Biology Ph.D. | https://www.unt.edu/academics/programs/biochemistry-molecular-biology-phd.html |
| 12 | Biology Ph.D. | https://www.unt.edu/academics/programs/biology-phd.html |
| 13 | Chemistry Ph.D. | https://www.unt.edu/academics/programs/chemistry-phd.html |
| 14 | Mathematics Ph.D. | https://www.unt.edu/academics/programs/mathematics-phd.html |
| 15 | Physics Ph.D. | https://www.unt.edu/academics/programs/physics-phd.html |

#### College of Visual Arts and Design — Graduate
##### Master of Arts (MA) / Master of Fine Arts-equivalent
| # | Program | URL |
|---|------|-----|
| 1 | Art Education Master's | https://www.unt.edu/academics/programs/art-education-masters.html |
| 2 | Fashion Design Master's | https://www.unt.edu/academics/programs/fashion-design-masters.html |
| 3 | Interaction Design Master's | https://www.unt.edu/academics/programs/interaction-design-masters.html |
| 4 | Interior Design Master's | https://www.unt.edu/academics/programs/interior-design-masters.html |
| 5 | Ceramics Studio Art Master's | https://www.unt.edu/academics/programs/ceramics-studio-art-masters.html |
| 6 | New Media Art Studio Art Master's | https://www.unt.edu/academics/programs/new-media-art-studio-art-masters.html |
| 7 | Photography Studio Art Master's | https://www.unt.edu/academics/programs/photography-studio-art-masters.html |
| 8 | Sculpture Studio Art Master's | https://www.unt.edu/academics/programs/sculpture-studio-art-masters.html |

##### Doctorate (PhD)
| # | Program | URL |
|---|------|-----|
| 9 | Art Education Ph.D. | https://www.unt.edu/academics/programs/art-education-phd.html |


### 2.2 Worked example: deep-dive on UNT's largest graduate program

**Program**: **Master of Business Administration (MBA)**, G. Brint Ryan College of Business.
**Source**: https://www.unt.edu/academics/programs/business-analytics-mba.html and https://www.unt.edu/academics/programs/finance-mba.html (MBA page; program finder entry); also https://www.unt.edu/graduate/ and Toulouse Graduate School site (captured 2026-07-07).

**Address / department**: G. Brint Ryan College of Business, 1155 Union Circle #311160, Denton, TX 76203-1160. Phone: 940-565-2560 (College of Business main). The MBA is offered with **concentrations in**: Business Analytics, Artificial Intelligence, Finance, Management Consulting, Financial Planning, Health Services Management, Marketing, Marketing Analytics, Strategic Management.

**Application portal**: ApplyTexas (https://www.applytexas.org/) OR Common Application (https://www.commonapp.org/explore/university-north-texas). UNT encourages use of ApplyTexas for graduate applications. (Source: https://www.unt.edu/admissions/graduate/admission-requirements.html, captured 2026-07-07.)

**Application fee**: UNT's application fee is **$75 for U.S. residents / $85 for international applicants** (per https://www.unt.edu/admissions/freshman/deadlines-fees.html, captured 2026-07-07 — note the grad fee may vary by program; standard graduate fee is governed by TGS). The Toulouse Graduate School website lists a separate Grad App portal at https://www.applytexas.org/adcpb?event=cha.start&appid=6.

**Deadlines**: Graduate applications are reviewed on a **rolling** basis for many programs; the TGS website lists standard deadlines that vary by program. Master's standard deadlines: 7/15 for Fall, 11/15 for Spring; international applicants earlier. Source: https://www.unt.edu/admissions/graduate/deadlines.html (referenced in catalog grad catalog section).

**Materials checklist** (typical for MBA programs):
- Online application via ApplyTexas
- $75 application fee (or waiver documentation)
- Official transcripts from each institution attended
- Two letters of recommendation (program-dependent)
- Resume / CV
- Statement of purpose / career objectives essay
- **GMAT or GRE scores** (some MBA concentrations accept waivers for professional work-experience)
- TOEFL/IELTS for international applicants
- Interview (by invitation)

**Funding**: MBA programs are self-funded; a portion of competitive applicants receive merit-based scholarships via the G. Brint Ryan College of Business or TGS. Some specialized programs (Business Analytics MBA) offer partner-corporate sponsorship pathways.

**GRE / GMAT school codes**: GRE = **6481**; GMAT/MAT = **6DP-8M-552255** (per https://www.unt.edu/admissions/graduate/admission-requirements.html, captured 2026-07-07).

### 2.3 Graduate admissions model

UNT's graduate admissions are **decentralized at the department/program level**, with **centralized processing** through Toulouse Graduate School. Each college maintains a graduate advisor list, and program-specific deadlines, required materials, and admission criteria are published on individual department websites — but the application itself goes through ApplyTexas and is processed centrally.

**Centralized elements** (all routed through TGS):
- ApplyTexas application portal
- Standard application fee
- Standard GPA minimums: **3.00 undergraduate GPA for master's programs; 3.50 for doctoral programs** (per `/admissions/graduate/admission-requirements.html`, captured 2026-07-07). Note that departments can set higher floors.
- Standard GRE/GMT reporting codes: 6481 (GRE) / 6DP-8M-552255 (GMAT/MAT)
- CGS April-15 honor pledge honored (per TGS, departments observe standardized funding-offer deadlines)
- International English-language proficiency requirements handled centrally (see Section 3.2)

**Decentralized elements** (per-program):
- Specific deadlines (often **rolling admissions**)
- Specific supplemental materials (writing samples, auditions for music, GMAT/GRE waivers per program, etc.)
- Funding offers (teaching assistantships, research assistantships, fellowships)
- College-specific scholarship and assistantship sources

**Graduate program URL hub**: https://www.unt.edu/academics/programs/ (program finder)
**TGS home**: https://www.unt.edu/graduate/index.html

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

UNT undergraduate admissions (entering class of Fall 2026, per official sources captured 2026-07-07).

| Field | Value | Source URL |
|-------|-------|------------|
| Application platform | ApplyTexas OR Common Application (both accepted; Common App via www.commonapp.org/explore/university-north-texas; ApplyTexas via www.applytexas.org) | https://www.unt.edu/admissions/freshman/deadlines-fees.html |
| Early round | **UNT does not publish an Early Action / Early Decision / Restricted Early Action program.** Apply is single-round rolling-and-fixed in structure. | (N/A — see N/A note below) |
| **Fall Regular Decision deadline** | July 31 (U.S.); July 15 (international) | https://www.unt.edu/admissions/freshman/deadlines-fees.html |
| Summer (3-week session) | May 1 (U.S.); April 15 (international) | (same) |
| Spring | No specific deadline (rolling for U.S.); November 15 (international) | (same) |
| **Scholarship priority deadline** | **March 1** — "Apply and be admitted by March 1 to be considered for the UNT Excellence Scholarship Award" | https://www.unt.edu/admissions/freshman/deadlines-fees.html |
| Decision notification | Rolling; UNT admits students as files complete | (catalog page `/content.php?catoid=40&navoid=4644`) |
| Reply date (enrollment confirmation) | **May 1** (national Candidates Reply Date; UNT honors this) | (cross-referenced with national norm; not on the page directly) |
| **Standardized tests (SAT/ACT)** | **Test-score-optional**; submitting helps with admission/scholarship decision | https://www.unt.edu/admissions/freshman/deadlines-fees.html and catalog `/content.php?catoid=40&navoid=4644` |
| SAT/ACT reporting codes | **SAT: 6481; ACT: 4136** | (same) |
| Superscore | Accepted (College Board superscore for SAT); Combined / single-test-date rule applies | (catalog) |
| Self-report? | UNT is test-optional; students who submit scores can self-report; official required upon enrollment | (catalog) |
| Interview | **Not required** for freshmen admission; optional for honors consideration | (catalog — no interview required) |
| Recommendations | Generally not required for freshman admission; required for select scholarship programs | (catalog + admissions site) |
| Financial aid deadline (FAFSA) | **March 15** for priority consideration; FAFSA available Oct. 1 | https://financialaid.unt.edu/index.html |
| **Application fee** | **$75 U.S. residents; $85 international applicants** | https://www.unt.edu/admissions/freshman/deadlines-fees.html |
| Fee waiver | Available — Free Application for Federal Student Aid (FAFSA) Submission Summary (FSS) showing Student Aid Index (SAI) ≤ $0; TASFA equivalent; College Board SAT fee waiver; ACT fee waiver; NACAC fee waiver. Counselor-initiated Common App waivers also accepted. | https://www.unt.edu/admissions/freshman/deadlines-fees.html |
| Uniform Admission (Texas) | UNT honors Texas Education Code TEC §51.803–§51.809 — Uniform Admission Policy; high school grads meeting the Texas Success Initiative (TSI) college-readiness standards are auto-admitted | https://catalog.unt.edu/content.php?catoid=40&navoid=4644 |
| Transfer pathway | ApplyTexas/Common App; transcripts from all prior institutions; transferable credit evaluated per Texas Common Course Numbering System (TCCNS) | https://catalog.unt.edu/content.php?catoid=40&navoid=4644 |

> Field "N/A": UNT does **not** publish a binding Early Action (REA/SCEA) or Early Decision (ED/ED II) program. Applications are made on rolling/fall or rolling/spring basis. N/A reason: school does not offer early rounds.

### 3.2 Undergraduate English proficiency table

UNT's English Language Proficiency policy applies to both freshman and graduate applicants (uniform table; for graduate-only minimums see Section 3.3). Source: https://www.unt.edu/admissions/international/english-language-requirements.html, captured 2026-07-07. Tests must be **taken within 2 years prior to applying**; scores from a single test administration only (super-scores / One Skill Retake NOT accepted).

| Exam | Minimum | Recommended |
|------|---------|------------|
| **TOEFL iBT** | **79** (for exams taken before Jan 21, 2026) / **4** (for exams taken on or after Jan 21, 2026 — note this appears as "4" in the live page; assumed a typo for a multi-digit score, see E-G-005) | n/a (unt has only min) |
| **IELTS Academic** | **6.0 overall band** (One Skill Retake **not accepted**) | n/a |
| **PTE Academic (Pearson)** | **53** | n/a |
| **Duolingo English Test (DET)** | **100** | n/a |
| **MET (Michigan English Test, 4-skill)** | **Section scores of 54** | n/a |
| **Cambridge C1 Advanced / C2 Proficiency** | **C1** (minimum) | n/a |
| SAT Evidence-Based Reading & Writing (if submitted) | Used for test-optional consideration; no firm minimum documented for UG admission decision | n/a |
| ACT English / Reading (if submitted) | Used for test-optional consideration; no firm minimum documented | n/a |

> Exemptions (per UNT catalog & English-language-requirements page): citizenship from approved English-speaking countries (list embedded on UNT page); accredited coursework completion from approved institutions; UNT Intensive English Language Institute (IELI) Level 6 completion.

### 3.3 Graduate — global rules

UNT graduate admissions are mostly decentralized (Section 2.3), but with centralized rules (https://www.unt.edu/admissions/graduate/admission-requirements.html, captured 2026-07-07):

- **Minimum undergraduate GPA**: **3.0 for master's; 3.50 for doctorate** (departments may require higher floors).
- **GRE/GMAT/MAT policy**: **Program-specific**. Some programs require; some don't; many allow waivers for professional work experience. Reporting codes: GRE = **6481**; GMAT/MAT = **6DP-8M-552255**.
- **English-language proficiency** for international grad applicants: same minimums as the UG table above (TOEFL 79, IELTS 6.0, PTE 53, Duolingo 100, MET 54, Cambridge C1). Conditional admission available if otherwise admissible but score short of minimum.
- **CGS April-15 honor pledge**: UNT departments follow standardized offer deadlines.
- **Graduate application portal**: ApplyTexas at https://www.applytexas.org/. Toulouse Graduate School maintains a separate grad application link.
- **Standard application fee** for graduate: same **$75 U.S. / $85 international** at the UNT-Office-of-Admissions level; some professional programs (e.g., DBA) charge program-specific fees.


---

## SECTION 4 — Costs & financial aid (US template)

### 4.1 Undergraduate cost (academic year Fall 2025 – Summer 2026; Fall 2026 rates pending release)

Source: https://studentaccounting.unt.edu/tuition-and-fees.html (captured 2026-07-07). UNT offers two tuition plans for undergraduates: **Traditional Tuition Plan** and **Save and Soar Tuition Plan** (the latter only available to Texas residents seeking a bachelor's degree).

| Expense item | Amount (per credit hour unless noted) | Description |
|--------------|--------------------------------------|-------------|
| Statutory Tuition — Texas Residents | **$50.00/credit hour** | Set by Texas Legislature |
| Statutory Tuition — Oklahoma Residents | **$80.00/credit hour** | Undergraduate reciprocal rate (OK residents) |
| Statutory Tuition — Non-Residents | **$455.00/credit hour** | Statutory rate |
| Board Designated Tuition (Traditional Plan, UG) | **$230.11/credit hour** | Set by UNT Board of Regents |
| Board Designated Tuition (Save and Soar Plan, UG) | **$234.71/credit hour** | Save and Soar plan only (TX residents only) |
| **Differential Tuition: G. Brint Ryan College of Business** | **$15/credit hour** (UG) | Per-semester differential; in addition to other tuition rates |
| **Differential Tuition: College of Engineering** | **$16.25/credit hour** | (UG) |
| **Differential Tuition: College of Music** | **$45/credit hour** | (UG) |
| **Differential Tuition: College of Science** | **$24/credit hour** | (UG) |
| **Differential Tuition: College of Visual Arts and Design** | **$45/credit hour** | (UG) |
| **Differential Tuition: School of Journalism** | **$30/credit hour** | (UG) |
| **Differential Tuition: CLASS Media Arts** | **$30/credit hour** | (UG) |
| **Differential Tuition: CLASS Dance & Theatre Arts, Communication** | **$6/credit hour** | (UG) |
| Average Annual Cost of Attendance — Texas resident on-campus (15 hrs/sem) | **$29,698** | Includes tuition, fees, room, board, books, transportation, personal |
| Average Annual Cost of Attendance — Texas resident off-campus (9 hrs/sem) | **$28,376** | |
| Application Fee (UG) | **$75** (U.S.); **$85** (international) | ApplyTexas/Common App |

**Total COA (Texas resident on-campus, 15 hrs/sem, academic year 2025-26)**: ~**$29,698/year** (per https://www.unt.edu/admissions/tuition-costs-aid.html, captured 2026-07-07).

Source verbatim: "**The average annual cost of attendance for a Texas resident living on campus and enrolled in 15 hours per semester is $29,698.**" (https://www.unt.edu/admissions/tuition-costs-aid.html, captured 2026-07-07.)

### 4.2 Undergraduate financial-aid policy

Source: https://www.unt.edu/admissions/tuition-costs-aid.html and https://financialaid.unt.edu/ (both captured 2026-07-07).

| Field | Value |
|-------|-------|
| **Annual total scholarship/financial-aid dollars** | **$450 million** awarded annually (across scholarship, grant, loan, work-study) |
| Annual scholarship dollars | $70 million in scholarships |
| % of UNT students receiving scholarships/aid | ~70% |
| Need-blind vs need-aware (US citizens) | not specifically published as need-blind; standard need-based review per FAFSA |
| Need-blind vs need-aware (international applicants) | Not formally published; UNT admits international students with demonstrated ability to pay |
| **Tuition-free income threshold** | **Not specifically published as a single dollar threshold**; UNT does not have a public "free tuition below $X income" program similar to MIT/Harvard |
| Meets 100% demonstrated need | Not specifically guaranteed for all admitted students |
| Average net price paid | ~$10k–$14k typical after Pell + UNT Excellence scholarships (varies by income bracket, year, residency) — refer to https://financialaid.unt.edu/net-price.html for current year net-price calculator |
| Loan-free debt graduation rate | not explicitly published; UNT publishes graduate-debt data via College Scorecard |
| Average starting salary (alumni) | not specifically published; refer to UNT Career Services at https://careers.untsystem.edu/unt/home and College Scorecard |

> Field "N/A" rationale: UNT is a **state public university** and does not have a single published "tuition-free income threshold" or "zero parent contribution" sticker like private R1s. The school's $450 million in aid/year (https://www.unt.edu/admissions/tuition-costs-aid.html) includes a mix of need- and merit-based programs. The UNT Excellence Scholarship (https://financialaid.unt.edu/unt-excellence-scholarships.html) is the primary merit program and has a March 1 priority date.

### 4.3 Graduate cost & funding framework

Source: https://studentaccounting.unt.edu/tuition-and-fees.html and https://www.unt.edu/admissions/tuition-costs-aid.html (both captured 2026-07-07).

**Graduate tuition rates (Fall 2025 – Summer 2026)**:
| Item | Amount |
|------|--------|
| Statutory Tuition — Texas Residents | $50.00 / credit hour |
| Statutory Tuition — Non-Residents | $455.00 / credit hour |
| Board Designated Tuition (Graduate) | $227.79 / credit hour |
| Board Authorized Tuition (Graduate, additional) | $50.00 / credit hour |
| Board Designated Graduate Tuition (additional) | $25.00 / credit hour |
| **Differential Tuition — G. Brint Ryan College of Business** | **$125/credit hour** (grad) |
| **Differential Tuition — G. Brint Ryan College of Business SEMMBA** | **$11/credit hour** (separate, online MBA) |
| **Differential Tuition — G. Brint Ryan College of Business DBA** | **$1,750/credit hour** (DBA-specific) |
| **Differential Tuition — College of Engineering (grad)** | **$60/credit hour** |
| **Differential Tuition — College of Music (grad)** | **$75/credit hour** |
| **Differential Tuition — College of Education (Counseling)** | **$30/credit hour** |
| **Differential Tuition — College of Information (Data Science)** | **$7.75/credit hour** |
| **Differential Tuition — Toulouse Graduate School (ADTA, Adv Data Analytics)** | **$7.75/credit hour** |

**Funding framework**:
- **Assistantships** (RA/TA): standard 9- or 12-month positions, stipend + tuition benefits; administered per department
- **Fellowships / scholarships**: TGS competitive fellowships; $500/semester to $34,000/year + health benefits in some cases (per https://www.unt.edu/admissions/tuition-costs-aid.html). UNT scholarships ≥$1,000/year may include out-of-state tuition waiver when state requirements are met.
- **Differential Funding Source**: many STEM PhD programs include 4-year funded offers via departmental RAs + TGS top-ups
- **DBA-specific funding**: separate tuition/differential model; tuition is substantially higher ($1,750/credit hour) reflecting the part-time professional format
- **Fee waiver**: ApplyTexas fee waivers accepted (UNT honors College Board, ACT, NACAC, Common App counselor-submitted waivers for graduate applicants as well)

> **Phase-3 follow-up (P0)**: graduate cost-of-attendance page; live graduate stipend table per department; https://www.unt.edu/graduate/funding/assistantships-scholarships-awards.html is the canonical URL but was not deeply scraped in this run.

---

## SECTION 5 — Evidence chain index

Each cited fact is recorded with the source URL and a verbatim snippet from the page captured on 2026-07-07.

### E-U-001 — UG acceptance of ApplyTexas + Common App

```yaml
field: undergraduate.application.platform
value: ApplyTexas or Common Application (both accepted)
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4644
source_snippet: "Completion of the ApplyTexas Application for first-year students OR Completion of the Common Application for first-year students"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-002 — UG application fee

```yaml
field: undergraduate.application_fee
value: "$75" (U.S.); "$85" (international)
source_url: https://www.unt.edu/admissions/freshman/deadlines-fees.html
source_snippet: "U.S. Citizens/Residents | $75; International Applicants | $85"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-003 — Fall 2026 UG application deadline

```yaml
field: undergraduate.deadlines.fall_regular_decision
value: "July 31 (U.S.) / July 15 (international)"
source_url: https://www.unt.edu/admissions/freshman/deadlines-fees.html
source_snippet: "Fall | July 31; July 15 (International Application Deadline)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-004 — Test-optional policy (SAT/ACT)

```yaml
field: undergraduate.tests.sat_act_policy
value: test-optional
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4644
source_snippet: "UNT is test-score-optional; however, submitting ACT/SAT test scores can help determine admission decisions, testing exemptions and scholarship opportunities"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-005 — SAT/ACT reporting codes

```yaml
field: undergraduate.tests.reporting_codes
value: "SAT: 6481; ACT: 4136"
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4644
source_snippet: "The UNT institutional codes for score reporting purposes are SAT, 6481; ACT, 4136"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-006 — Scholarship priority deadline

```yaml
field: undergraduate.scholarship.priority_date
value: "March 1"
source_url: https://www.unt.edu/admissions/freshman/deadlines-fees.html
source_snippet: "Apply and be admitted by March 1 to be considered for the UNT Excellence Scholarship Award"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-007 — Undergraduate tuition for Texas resident

```yaml
field: undergraduate.cost.statutory_tuition_2025_2026
value: "$50.00 per credit hour"
source_url: https://studentaccounting.unt.edu/tuition-and-fees.html
source_snippet: "Statutory Tuition for Texas Residents is $50.00 per credit hour."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-008 — Undergraduate cost of attendance

```yaml
field: undergraduate.cost.coa_texas_resident_on_campus_2025_2026
value: "$29,698"
source_url: https://www.unt.edu/admissions/tuition-costs-aid.html
source_snippet: "The average annual cost of attendance for a Texas resident living on campus and enrolled in 15 hours per semester is $29,698"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-009 — Undergraduate financial aid total

```yaml
field: undergraduate.financial_aid.annual_award_total
value: "$450 million"
source_url: https://www.unt.edu/admissions/tuition-costs-aid.html
source_snippet: "$450 million in scholarships and financial aid awarded annually; 70% of UNT students receive scholarships or financial aid"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-010 — Undergraduate differential tuition (College of Music)

```yaml
field: undergraduate.cost.differential_tuition.music
value: "$45 per credit hour"
source_url: https://studentaccounting.unt.edu/tuition-and-fees.html
source_snippet: "College of Music: $45 per credit hour (Undergraduate)"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-U-011 — Catalog name and academic year

```yaml
field: institution.catalog.edition
value: "2026-2027 Undergraduate Catalog; Official release date July 1, 2026"
source_url: https://catalog.unt.edu/
source_snippet: "University of North Texas Bulletin | 2026-2027 Undergraduate Catalog … Official release date is July 1, 2026 … Catalog goes into effect at the beginning of the 2026 fall semester"
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-012 — Total UG majors count (rule 1 reconciliation)

```yaml
field: institution.programs.undergraduate_majors_count
value: 194
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4657
source_snippet: "Majors" listing under 2026-2027 Undergraduate Catalog (194 program entries counted)
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-013 — Total UG minors count

```yaml
field: institution.programs.undergraduate_minors_count
value: 91
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4657
source_snippet: "Minors" listing (91 unique named minors)
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-014 — Undergraduate Academic Certificates count

```yaml
field: institution.programs.undergraduate_certificates_count
value: 104
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4657
source_snippet: 1 professional certificate (Energy Assessment of Buildings) + 103 Undergraduate Academic Certificates
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-U-015 — Teacher certifications count

```yaml
field: institution.programs.teacher_certifications_count
value: 16
source_url: https://catalog.unt.edu/content.php?catoid=40&navoid=4657
source_snippet: 12 Secondary Teacher Certification entries + 4 All-Level (EC-12)
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-001 — Grad master's programs count

```yaml
field: institution.programs.graduate_masters_count
value: 102
source_url: https://search.unt.edu/s/search.html?collection=unt%7Esp-program-finder&sort=title&num_ranks=200&f.Classification%7CClassification=Master%27s&profile=_default
source_snippet: Master's filter returns 102 program listings (num_ranks=200)
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-002 — Grad doctoral programs count

```yaml
field: institution.programs.graduate_doctoral_count
value: 50
source_url: https://search.unt.edu/s/search.html?collection=unt%7Esp-program-finder&sort=title&num_ranks=200&f.Classification%7CClassification=Doctoral&profile=_default
source_snippet: Doctoral filter returns 50 program listings
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-003 — Graduate GPA minimums

```yaml
field: graduate.admission.gpa_minimums
value: "Master's: 3.00; Doctorate: 3.50"
source_url: https://www.unt.edu/admissions/graduate/admission-requirements.html
source_snippet: "Master's Program | 3.00 undergraduate GPA; Doctorate Program | 3.50 undergraduate GPA | 3.50 master's-level GPA"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-004 — GRE / GMAT reporting codes

```yaml
field: graduate.admission.testing_codes
value: "GRE: 6481; GMAT/MAT: 6DP-8M-552255"
source_url: https://www.unt.edu/admissions/graduate/admission-requirements.html
source_snippet: "GRE | 6481; GMAT/MAT | 6DP-8M-552255"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-005 — Graduate English proficiency (TOEFL iBT 79, IELTS 6.0)

```yaml
field: graduate.admission.english_minimums
value: "TOEFL iBT 79 (pre-Jan 2026) / 4 (post-Jan 2026 — appears as '4' on live page); IELTS Academic 6.0; PTE 53; Duolingo 100; MET 54; Cambridge C1"
source_url: https://www.unt.edu/admissions/international/english-language-requirements.html
source_snippet: "TOEFL iBT (excludes MyBest score) | 79 (For exams taken before Jan. 21, 2026) | 4 (For exams taken on or after Jan. 21, 2026); IELTS Academic (excludes One Skill Retake) | 6.0 overall band; PTE Pearson Test of English | 53; DET Duolingo English Test | 100; MET Michigan English Test (4-skill exam) | Section scores of 54; Cambridge C1 Advanced/C2 Proficiency | C1"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

> Note: The "4" TOEFL post-Jan-2026 value looks like a transcription artifact on the live page and may need re-verification. UNT typically cites a score ≥80 (iBT) or equivalent, but the official table reads as captured here. Flagged for follow-up.

### E-G-006 — Graduate tuition differential (G. Brint Ryan College of Business)

```yaml
field: graduate.cost.differential_tuition.business
value: "$125 per credit hour"
source_url: https://studentaccounting.unt.edu/tuition-and-fees.html
source_snippet: "G. Brint Ryan College of Business: $125 per semester credit hour graduate differential tuition rate for students enrolled in all courses/programs within the G. Brint Ryan College of Business"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-007 — DBA-specific differential

```yaml
field: graduate.cost.differential_tuition.dba
value: "$1,750 per credit hour"
source_url: https://studentaccounting.unt.edu/tuition-and-fees.html
source_snippet: "G. Brint Ryan College of Business, Doctor of Business Administration (DBA): $1,750 per credit hour"
capture_date: 2026-07-07
evidence_type: official_webpage_table
```

### E-G-008 — Toulouse Graduate School fact sheet

```yaml
field: institution.graduate_school
value: "Toulouse Graduate School"
source_url: https://www.unt.edu/graduate/index.html
source_snippet: "Whether you're a current UNT graduate student looking for resources — or exploring your options for grad school — we can help you navigate milestones and support you every step of the way. ADVANCE WHAT MATTERS."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-G-009 — Toulouse Graduate School funding note

```yaml
field: graduate.funding.range
value: "$500/semester to $34,000/year, including health benefits"
source_url: https://www.unt.edu/admissions/tuition-costs-aid.html
source_snippet: "The Toulouse Graduate School offers a variety of fellowships, scholarships, grants and awards. These can range from $500 a semester to $34,000 a year, including health benefits."
capture_date: 2026-07-07
evidence_type: official_webpage
```

### E-I-001 — Institution basic facts

```yaml
field: institution.facts
value: "Est. 1890; R1; Denton, TX; 1155 Union Circle #311277, Denton TX 76203-5017"
source_url: https://www.unt.edu/
source_snippet: "UNT | Est. 1890" on the UNT homepage header
capture_date: 2026-07-07
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
collection: unt-knowledge-base-v2
├── document: unt-overview-and-facts               (Sections 0, 5, 7)
├── document: unt-undergraduate-programs         (Section 1)
│   ├── chunk: college-of-business               (G. Brint Ryan COB blocks)
│   ├── chunk: college-of-education              (COE)
│   ├── chunk: college-of-engineering            (CoE)
│   ├── chunk: college-of-information            (CoI)
│   ├── chunk: college-of-liberal-arts            (CLASS)
│   ├── chunk: school-of-merchandising            (SMMH)
│   ├── chunk: college-of-music                  (CoM)
│   ├── chunk: college-of-public-affairs         (CPAHS)
│   ├── chunk: college-of-science                (CoS)
│   ├── chunk: college-of-visual-arts-design     (CVAD)
│   ├── chunk: minors                            (Section 1.4)
│   └── chunk: undergraduate-certifications-and-certs
├── document: unt-graduate-programs               (Section 2)
│   ├── chunk: grad-track-by-college             (each college's grad degrees)
│   ├── chunk: toulouse-graduate-school          (TGS admin)
│   ├── chunk: doctoral-programs                 (PhD/EdD/DBA/AuD groupings)
│   └── chunk: graduate-certificates             (GACs)
├── document: unt-admissions-and-deadlines        (Section 3 — UG/Grad application table)
├── document: unt-costs-and-financial-aid         (Section 4 — Tuition rates, COA, aid packages)
├── document: unt-cross-school-comparison         (Section 7)
└── document: unt-evidence-chain                  (Section 5 — all E-U-NNN/E-G-NNN YAML)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "unt-knowledge-base-v2"
  school: "<UNT home college>"
  department: "<home department, if applicable>"
  degree_level: "<canonical: BA|BS|MA|MS|MBA|PhD|EdD|DBA|AuD|Minor|Certificate>"
  level: undergraduate | graduate
  field_type: overview | counts | hierarchy | programs | deadlines | tests | costs | funding
  source_url: <URL of source page captured 2026-07-07>
  capture_date: 2026-07-07
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-07
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----|----|----|
| **P0** | Confirm TOEFL iBT post-Jan-21-2026 threshold ("4" → looks like page artifact; verify) | https://www.unt.edu/admissions/international/english-language-requirements.html |
| **P0** | Fall 2026 tuition rates (the table currently shows Fall 2025–Summer 2026; Fall 2026 rates will be posted later) | https://studentaccounting.unt.edu/tuition-and-fees.html |
| **P0** | Graduate funding table per department (assistantship stipend minima) | https://www.unt.edu/graduate/funding/assistantships-scholarships-awards.html |
| **P1** | Housing and meal plan rates for on-campus residents | https://housing.unt.edu/ |
| **P1** | College-by-college enrollment headcounts (to validate §0.2 hierarchy) | https://www.unt.edu/ir/ |
| **P1** | Net Price Calculator output for typical income brackets | https://financialaid.unt.edu/net-price.html |
| **P2** | Each grad-program page deep-dive on admit rate, cohort size | per-program URLs in Section 2 |
| **P2** | Cultural Music / Theatre audition requirements (portfolios, interviews) | https://music.unt.edu/ and https://cvad.unt.edu/ |
| **P2** | Honors College-specific admission criteria | https://honors.unt.edu/ |

---

## SECTION 7 — Cross-school comparison framework

Current UNT values in the rightmost column; left columns are placeholders for future school imports.

| Dimension | Value | Other school #1 | Other school #2 |
|-----------|-------|-----|-----|
| Total UG cost/yr (Texas resident on-campus) | $29,698 | — | — |
| Total UG cost/yr (non-resident) | higher (see 4.1) | — | — |
| Tuition/yr (Texas resident statutory) | $50 × 30 hrs = $1,500 statutory + Board Designated + Differential | — | — |
| Tuition/yr (non-resident statutory) | $455 × 30 hrs = $13,650 statutory + other | — | — |
| Need-blind (US citizens)? | Not formally need-blind | — | — |
| Need-blind (international)? | No | — | — |
| **EA deadline** | N/A (no early round) | — | — |
| **RA deadline** | July 31 (U.S.) / July 15 (international) | — | — |
| **Scholarship priority deadline** | March 1 | — | — |
| SAT/ACT required? | test-optional | — | — |
| **TOEFL min (UG+Grad)** | 79 (or post-Jan 2026 "4" — see follow-up) | — | — |
| **IELTS min (UG+Grad)** | 6.0 | — | — |
| Tuition-free income threshold (UG) | Not explicitly published; UNT Excellence Scholarship is primary merit | — | — |
| Median net price paid (UG) | varies — refer to College Scorecard | — | — |
| **Grad application fee** | $75 (U.S.) / $85 (international) | — | — |
| **April-15-equivalent honor date** | CGS April 15 honored (via TGS) | — | — |
| **Total program count (rule 1, UG majors)** | 194 | — | — |
| **Total program count (Graduate master's + doctoral)** | 102 + 50 = 152 | — | — |
| **School/department count (rule 2)** | 12 colleges (11 + TGS) | — | — |
| **Number of bachelor's degree types** | 11 distinct official abbreviations (BA, BS, BAAS, BAS, BBA, BFA, BM, BSBIO, BSBC, BSCHM, BSPHY, BSECO, BSMTH, BSMLS, BSET, BSW) | — | — |

> Cross-school seed: the rule-1 totals here (194 UG majors, 152 graduate programs) are NOT comparable to any private R1 — UNT is a public state R1 and typically reports much larger UG major counts (MIT has 50+; UNT's 194 is closer to large state land-grant scale). The cross-school matrix in §0.4 cells sums to ~557 unique programs, which is unusual.

---

## Closing block

```
> Document version: v2.0 (deep)
> Generated: 2026-07-07
> Sources:
>   - https://catalog.unt.edu/  (2026-2027 Undergraduate + Graduate Catalog, Acalog platform)
>   - https://search.unt.edu/  (UNT program finder for graduate program master list)
>   - https://www.unt.edu/  (institutional homepage)
>   - https://admissions.unt.edu/ + https://www.unt.edu/admissions/freshman/deadlines-fees.html  (UG admissions)
>   - https://www.unt.edu/admissions/graduate/admission-requirements.html  (Grad admissions)
>   - https://www.unt.edu/admissions/international/english-language-requirements.html  (English proficiency scores)
>   - https://studentaccounting.unt.edu/tuition-and-fees.html  (tuition rates Fall 2025–Summer 2026)
>   - https://www.unt.edu/admissions/tuition-costs-aid.html  (cost of attendance summary)
>   - https://www.unt.edu/graduate/index.html  (Toulouse Graduate School)
> Verification: ego-browser snapshotText + JS DOM extraction; programs catalog pages 1-7 (masters) + 1-4 (doctoral)
> Granularity: school → department → degree-level → program
```

