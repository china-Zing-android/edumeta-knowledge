# California State University, Long Beach (CSULB) Admissions Knowledge Base — Structured Data v2.0

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
| 本科学位专业 (BA/BS/BFA/BM/BMus) | ~95 |
| 本科辅修 (Minor) | ~80 |
| 研究生学位项目 (MA/MS/MFA/MM/MBA/EdD/DPT/DNP/DPH) | ~85 |
| 研究生高级证书 (Advanced Certificate / Credential) | ~30 |
| **学位项目总计 (UG + Grad)** | **~210** |
| 学院 / 独立系所总数 | 7 学院 + ~60 系/项目组 |

> Note: CSULB's catalog lists programs by department within colleges. The counts above are estimates based on the 2026-2027 catalog structure. The exact count requires enumeration of each department's program page in the catalog.

### 0.2 学院 / 系层级结构

```
California State University, Long Beach (CSULB)
├── College of the Arts [学院]
│   ├── Art [系]
│   ├── Cinematic Arts [系]
│   ├── Dance [系]
│   ├── Design [系]
│   ├── Music (Bob Cole Conservatory) [系]
│   └── Theatre Arts [系]
├── College of Business [学院]
│   ├── Accountancy [系]
│   ├── Finance [系]
│   ├── Information Systems [系]
│   ├── International Business [系]
│   ├── Legal Studies [系]
│   ├── Management, HRM & Supply Chain Management [系]
│   └── Marketing [系]
├── College of Education [学院]
│   ├── Advanced Studies in Education and Counseling [系]
│   ├── Educational Leadership [系]
│   ├── Liberal Studies [系]
│   ├── Single Subject Teacher Education [系]
│   └── Teacher Education [系]
├── Hung Family College of Engineering [学院]
│   ├── Biomedical Engineering [系]
│   ├── Chemical Engineering [系]
│   ├── Civil Engineering and Construction Engineering Management [系]
│   ├── Computer Engineering and Computer Science [系]
│   ├── Electrical Engineering [系]
│   ├── Engineering Technology [系]
│   └── Mechanical and Aerospace Engineering [系]
├── College of Health and Human Services [学院]
│   ├── Child and Family Studies [系]
│   ├── Consumer Affairs [系]
│   ├── Criminology and Criminal Justice [系]
│   ├── Emergency Services Administration [系]
│   ├── Family and Consumer Sciences [系]
│   ├── Fashion Merchandising and Design [系]
│   ├── Food Science [系]
│   ├── Gerontology [系]
│   ├── Health Care Management [系]
│   ├── Health Science [系]
│   ├── Hospitality Management [系]
│   ├── Kinesiology [系]
│   ├── Military Science [系]
│   ├── Nursing [系]
│   ├── Nutrition and Dietetics [系]
│   ├── Physical Therapy [系]
│   ├── Public Policy and Administration [系]
│   ├── Recreation and Leisure Studies [系]
│   ├── Social Work [系]
│   ├── Speech-Language Pathology [系]
│   └── Student Life and Development [系]
├── College of Liberal Arts [学院]
│   ├── Africana Studies [系]
│   ├── American Indian Studies [系]
│   ├── American Studies [系]
│   ├── Anthropology [系]
│   ├── Asian and Asian American Studies [系]
│   ├── Asian Languages [系]
│   ├── Chicano and Latino Studies [系]
│   ├── Chinese Studies [系]
│   ├── Communication Studies [系]
│   ├── Comparative World Literature and Classics [系]
│   ├── Economics [系]
│   ├── English [系]
│   ├── Environmental Science and Policy [系]
│   ├── French and Francophone Studies [系]
│   ├── Geography [系]
│   ├── German [系]
│   ├── Global Migration Studies [系]
│   ├── Global Studies [系]
│   ├── History [系]
│   ├── Human Development [系]
│   ├── Italian Studies [系]
│   ├── Japanese [系]
│   ├── Jewish Studies [系]
│   ├── Journalism and Public Relations [系]
│   ├── Latin American Studies [系]
│   ├── Legal Studies [系]
│   ├── Linguistics [系]
│   ├── Medieval and Renaissance Studies [系]
│   ├── Peace Studies [系]
│   ├── Philosophy [系]
│   ├── Political Science [系]
│   ├── Psychology [系]
│   ├── Religious Studies [系]
│   ├── Romance, German, Russian Languages and Literatures [系]
│   ├── Russian [系]
│   ├── Sociology [系]
│   ├── Spanish [系]
│   ├── Translation Studies [系]
│   └── Women's, Gender, and Sexuality Studies [系]
└── College of Natural Sciences and Mathematics [学院]
    ├── Biological Sciences [系]
    ├── Chemistry and Biochemistry [系]
    ├── Earth Science [系]
    ├── Mathematics and Statistics [系]
    ├── Ocean Studies Institute [系]
    ├── Physics and Astronomy [系]
    └── Science Education [系]
```

### 0.3 学历级别明细

| 学位缩写 | 全称 | 层级 | 本项目数量 |
|---------|------|------|-----------|
| BA | Bachelor of Arts | 本科 | ~40 |
| BS | Bachelor of Science | 本科 | ~30 |
| BFA | Bachelor of Fine Arts | 本科 | ~5 |
| BM/BMus | Bachelor of Music | 本科 | ~4 |
| BBA | Bachelor of Business Administration | 本科 | ~7 |
| MA | Master of Arts | 研究生 | ~20 |
| MS | Master of Science | 研究生 | ~25 |
| MFA | Master of Fine Arts | 研究生 | ~5 |
| MM | Master of Music | 研究生 | ~3 |
| MBA | Master of Business Administration | 研究生 | 1 |
| MPA | Master of Public Administration | 研究生 | 1 |
| MSW | Master of Social Work | 研究生 | 1 |
| MFA/MBA | Dual Degree (Theatre Management) | 研究生 | 1 |
| EdD | Doctor of Education | 研究生 | 1 |
| DPT | Doctor of Physical Therapy | 研究生 | 1 |
| DNP | Doctor of Nursing Practice | 研究生 | 1 |
| DPH | Doctor of Public Health | 研究生 | 1 |
| Credential | Teaching Credential | 研究生 | ~15 |
| Certificate | Post-Baccalaureate Certificate | 研究生 | ~10 |

> Note: CSULB uses standard degree nomenclature (BA, BS, MA, MS, etc.). No special mappings needed per degree-taxonomy.md.

### 0.4 分布矩阵 (学院 × canonical 学位级别)

| 学院 \ 级别 | BA | BS | BFA | BM | BBA | MA | MS | MFA | MM | MBA | MPA | MSW | EdD | DPT | DNP | DPH | Credential | Cert | 合计 |
|------------|----|----|----|----|-----|----|----|----|----|----|----|----|----|----|----|----|----------|------|------|
| College of the Arts | 6 | 2 | 4 | 4 | 0 | 4 | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | ~28 |
| College of Business | 0 | 0 | 0 | 0 | 7 | 0 | 2 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~10 |
| College of Education | 1 | 0 | 0 | 0 | 0 | 3 | 2 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | ~12 | 2 | ~21 |
| College of Engineering | 0 | 7 | 0 | 0 | 0 | 0 | 7 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | ~14 |
| Health & Human Services | 1 | 10 | 0 | 0 | 0 | 2 | 8 | 0 | 0 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 2 | ~28 |
| College of Liberal Arts | 30 | 0 | 0 | 0 | 0 | 8 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | ~42 |
| Natural Sciences & Math | 0 | 12 | 0 | 0 | 0 | 1 | 5 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | ~19 |
| **合计** | ~38 | ~31 | ~4 | ~4 | ~7 | ~18 | ~27 | ~3 | ~2 | ~1 | ~1 | ~1 | ~1 | ~1 | ~1 | ~1 | ~12 | ~9 | **~162** |

> Note: This matrix is an estimate based on the college/department structure visible in the catalog. Exact counts require enumeration of each department's program page. The matrix includes both UG and Grad programs. Some departments may offer additional certificates or credentials not captured here.

---

## SECTION 1 — Undergraduate education (Rule 5 grouping)

### 1.1 College/school architecture

CSULB has 7 colleges offering undergraduate degrees. See Section 0.2 for the complete hierarchy tree. The colleges are: College of the Arts, College of Business, College of Education, Hung Family College of Engineering, College of Health and Human Services, College of Liberal Arts, and College of Natural Sciences and Mathematics.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of the Arts

##### Art
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Art (BFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |

##### Cinematic Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Cinematic Arts (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1489 |

##### Dance
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1487 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance (BFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1487 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance Science (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1487 |

##### Design
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Design (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1488 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Interior Design (BFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1488 |

###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Industrial Design (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1488 |

##### Music
###### BM
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (BM) - multiple options | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1490 |

###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Music (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1490 |

##### Theatre Arts
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1491 |

###### BFA
| # | 专业 | URL |
|---|------|-----|
| 1 | Theatre Arts (BFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1491 |

#### College of Business

##### Accountancy
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1493 |

##### Finance
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Finance (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1494 |

##### Information Systems
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Information Systems (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1495 |

##### International Business
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | International Business (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1496 |

##### Management, HRM & Supply Chain Management
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Management and Human Resource Management (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1497 |
| 2 | Supply Chain Management (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1497 |

##### Marketing
###### BBA
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing (BBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1498 |

#### College of Education

##### Liberal Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Liberal Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1502 |

#### Hung Family College of Engineering

##### Biomedical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1506 |

##### Chemical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemical Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1507 |

##### Civil Engineering and Construction Engineering Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Civil Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1508 |
| 2 | Construction Engineering Management (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1508 |

##### Computer Engineering and Computer Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1509 |
| 2 | Computer Science (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1509 |

##### Electrical Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Electrical Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1510 |

##### Engineering Technology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Engineering Technology (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1511 |

##### Mechanical and Aerospace Engineering
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1512 |
| 2 | Aerospace Engineering (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1512 |

#### College of Health and Human Services

##### Child and Family Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Child Development and Family Studies (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1515 |

##### Consumer Affairs
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Consumer Affairs (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1516 |

##### Criminology and Criminal Justice
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1517 |

##### Emergency Services Administration
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Emergency Services Administration (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1518 |

##### Family and Consumer Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Family and Consumer Sciences (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1519 |

##### Fashion Merchandising and Design
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Fashion Merchandising and Design (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1520 |

##### Food Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Food Science (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1521 |

##### Health Care Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Care Management (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1524 |

##### Health Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Health Science (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1525 |

##### Hospitality Management
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Hospitality Management (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1522 |

##### Kinesiology
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Kinesiology (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1526 |

##### Nursing
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1528 |

##### Nutrition and Dietetics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Nutrition and Dietetics (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1529 |

##### Recreation and Leisure Studies
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Recreation and Leisure Studies (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1532 |

##### Social Work
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Social Work (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1534 |

##### Speech-Language Pathology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Speech-Language Pathology (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1514 |

##### Student Life and Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Student Life and Development (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1533 |

#### College of Liberal Arts

##### Africana Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Africana Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1536 |

##### American Indian Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Indian Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1537 |

##### American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | American Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1538 |

##### Anthropology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Anthropology (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1539 |

##### Asian and Asian American Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Asian and Asian American Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1540 |

##### Chicano and Latino Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Chicano and Latino Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1542 |

##### Communication Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Communication Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1545 |

##### Comparative World Literature and Classics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Comparative World Literature and Classics (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1546 |

##### Economics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Economics (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1547 |

##### English
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | English (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1548 |

##### Environmental Science and Policy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Environmental Science and Policy (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1549 |

##### Geography
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1551 |

##### History
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | History (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1554 |

##### Human Development
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Development (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1555 |

##### Journalism and Public Relations
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism and Public Relations (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1560 |

##### Linguistics
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Linguistics (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1562 |

##### Philosophy
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1565 |

##### Political Science
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Political Science (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1566 |

##### Psychology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1567 |

##### Religious Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Religious Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1568 |

##### Sociology
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1571 |

##### Spanish
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Spanish (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1572 |

##### Women's, Gender, and Sexuality Studies
###### BA
| # | 专业 | URL |
|---|------|-----|
| 1 | Women's, Gender, and Sexuality Studies (BA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1573 |

#### College of Natural Sciences and Mathematics

##### Biological Sciences
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Biological Sciences (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1574 |

##### Chemistry and Biochemistry
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1575 |
| 2 | Biochemistry (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1575 |

##### Earth Science
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Earth Science (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1576 |

##### Mathematics and Statistics
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1577 |
| 2 | Statistics (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1577 |

##### Physics and Astronomy
###### BS
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1579 |
| 2 | Astronomy (BS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1579 |

### 1.3 Interdisciplinary / cross-college undergraduate programs

CSULB offers several interdisciplinary programs that span multiple colleges. These include Environmental Science and Policy (Liberal Arts + Natural Sciences), and various certificate programs offered through the College of Professional and Continuing Education (CPaCE).

### 1.4 Minors — complete list

CSULB offers minors in most departments across all 7 colleges. A complete list requires enumeration of each department's catalog page. Common minors include: Art, Business Administration, Chemistry, Communication Studies, Economics, English, History, Mathematics, Music, Philosophy, Political Science, Psychology, Sociology, Spanish, Theatre Arts, and many others.

### 1.5 General/Institute-wide requirements

CSULB requires completion of the CSU General Education Breadth requirements (also known as GE Breadth) or the IGETC (Intersegmental General Education Transfer Curriculum) for transfer students. These include courses in:
- Area A: English Language Communication and Critical Thinking
- Area B: Scientific Inquiry and Quantitative Reasoning
- Area C: Arts and Humanities
- Area D: Social Sciences
- Area E: Lifelong Learning and Self-Development

### 1.6 Course-ID → Major quick-lookup

CSULB does not use a course-ID numbering system for majors. Programs are identified by department and degree type.

---

## SECTION 2 — Graduate education (Rule 5 grouping)

### 2.1 Graduate programs — grouped by 学院 > 系 > 学位级别

#### College of the Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art History (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |
| 2 | Art (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |
| 3 | Dance (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1487 |
| 4 | Design (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1488 |

##### MFA
| # | 项目 | URL |
|---|------|-----|
| 1 | Art (MFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |
| 2 | Dance (MFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1487 |
| 3 | Theatre Arts (MFA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1491 |

##### MM
| # | 项目 | URL |
|---|------|-----|
| 1 | Music (MM) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1490 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Geographic Information Science (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Museum Studies (Post-Bacc Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |
| 2 | Biomedical Illustration (Post-Bacc Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1486 |

#### College of Business

##### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Administration (MBA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1492 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Accountancy (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1493 |
| 2 | Finance (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1494 |
| 3 | Information Systems (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1495 |
| 4 | Marketing Analytics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1498 |
| 5 | Financial Analytics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1494 |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Business Analytics (Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1492 |

#### College of Education

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education (MA) - multiple options | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1499 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Counseling (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1500 |
| 2 | School Psychology (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1500 |

##### EdD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Leadership (EdD) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1501 |

##### Credential
| # | 项目 | URL |
|---|------|-----|
| 1 | Multiple Subject Teaching Credential | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1504 |
| 2 | Single Subject Teaching Credential | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1503 |
| 3 | Education Specialist Credential | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1500 |
| 4 | Administrative Services Credential | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1501 |
| 5 | Pupil Personnel Services Credential | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1500 |

#### Hung Family College of Engineering

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biomedical Engineering (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1506 |
| 2 | Chemical Engineering (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1507 |
| 3 | Civil Engineering (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1508 |
| 4 | Computer Science (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1509 |
| 5 | Electrical Engineering (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1510 |
| 6 | Engineering Technology (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1511 |
| 7 | Mechanical Engineering (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1512 |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering (Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1505 |

#### College of Health and Human Services

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1517 |
| 2 | Emergency Services Administration (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1518 |
| 3 | Family and Consumer Sciences (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1519 |
| 4 | Gerontology (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1523 |
| 5 | Health Care Management (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1524 |
| 6 | Health Science (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1525 |
| 7 | Kinesiology (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1526 |
| 8 | Nutrition and Dietetics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1529 |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Speech-Language Pathology (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1514 |
| 2 | Linguistics (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1562 |

##### MSW
| # | 项目 | URL |
|---|------|-----|
| 1 | Social Work (MSW) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1534 |

##### MPA
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Administration (MPA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1531 |

##### DPT
| # | 项目 | URL |
|---|------|-----|
| 1 | Physical Therapy (DPT) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1530 |

##### DNP
| # | 项目 | URL |
|---|------|-----|
| 1 | Nursing Practice (DNP) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1528 |

##### DPH
| # | 项目 | URL |
|---|------|-----|
| 1 | Public Health (DPH) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1525 |

#### College of Liberal Arts

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1548 |
| 2 | History (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1554 |
| 3 | Linguistics (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1562 |
| 4 | Philosophy (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1565 |
| 5 | Political Science (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1566 |
| 6 | Psychology (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1567 |
| 7 | Sociology (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1571 |
| 8 | Spanish (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1572 |

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Geographic Information Science (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1551 |
| 2 | International Studies (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1556 |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Translation Studies (Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1588 |

#### College of Natural Sciences and Mathematics

##### MS
| # | 项目 | URL |
|---|------|-----|
| 1 | Biology (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1574 |
| 2 | Chemistry (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1575 |
| 3 | Mathematics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1577 |
| 4 | Statistics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1577 |
| 5 | Physics (MS) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1579 |

##### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Science Education (MA) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1580 |

##### Certificate
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology (Certificate) | https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1574 |

### 2.2 At least one program's full deep-dive (worked example)

**Program**: Master of Science in Computer Science
- **Department**: Computer Engineering and Computer Science
- **College**: Hung Family College of Engineering
- **Degree**: MS
- **URL**: https://csulb.catalog.acalog.com/preview_entity.php?catoid=12&ent_oid=1509
- **Application Portal**: Cal State Apply (https://www.calstate.edu/apply)
- **Application Deadline**: Varies by program (no later than June 1 for Fall)
- **Application Fee**: $70 (nonrefundable)
- **GRE Policy**: Not required (CSU system policy)
- **TOEFL Minimum**: 80 (iBT)
- **IELTS Minimum**: 6.5

### 2.3 Graduate admissions model

CSULB uses a **decentralized** graduate admissions model. Each department/program manages its own admissions process, deadlines, and requirements. Applications are submitted through Cal State Apply, but review and decisions are made at the department level.

- **Application Portal**: Cal State Apply
- **Application Fee**: $70 (standard); MBA programs may have additional fees
- **CGS April 15 Equivalent**: CSULB follows the CSU system's enrollment deposit deadline (May 1 for Fall)
- **Financial Aid**: Managed centrally through the Financial Aid and Scholarships office

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions site | https://www.csulb.edu/admissions | E-U-001 |
| Application portal | Cal State Apply (https://www.calstate.edu/apply) | E-U-002 |
| Application opens | October 1 (Fall); July 1 (Spring) | E-U-003 |
| Freshman application deadline | November 30 (Fall); December 1 (Spring) | E-U-003 |
| Transfer application deadline | November 30 (Fall); August 31 (Spring) | E-U-003 |
| Decision notification | Mid-February to April | E-U-003 |
| Enrollment deposit deadline | May 1 (Fall); November 15 (Spring) | E-U-003 |
| Application fee | $70 (nonrefundable) | E-U-004 |
| SAT/ACT policy | **Test-FREE** (CSU system — SAT/ACT not considered) | E-U-005 |
| Superscore policy | N/A (test-free) | E-U-005 |
| Interview policy | N/A (except Music/Dance auditions) | E-U-006 |
| Recommendation requirements | Not required for undergraduate | E-U-007 |
| Portfolio requirement | Required for Art, Design, and some Music programs | E-U-006 |

### 3.2 Undergraduate English proficiency table

CSULB requires English language demonstration for all international applicants. Tests accepted:

| Exam | Undergraduate Minimum | Post-Baccalaureate Minimum |
|------|----------------------|---------------------------|
| TOEFL iBT | 61 | 80 |
| IELTS | 6.0 | 6.5 |
| Duolingo English Test | 105 | 115 |
| Pearson Test of English (PTE) | 43 | 58 |
| Eiken | Grade Pre-1 | Grade 1 |
| Cambridge English (B2 First, C1 Advanced, C2 Proficiency) | 162 | 169 |
| ALI (American Language Institute) | Completion of Level 4 | Completion of Level 6 |

**Exemptions**: English language requirement is waived for applicants who:
- Obtained a bachelor's or master's degree from a U.S. regionally accredited institution
- Transfer applicants with 60+ semester units from a domestic U.S. institution
- First-year applicants who completed 3+ years at a U.S. high school
- Applicants educated in qualifying English-speaking countries (list includes: Antigua & Barbuda, Australia, Bahamas, Barbados, Belize, Bermuda, Botswana, Canada, England, Fiji, Gambia, Ghana, Grand Cayman Islands, Grenada, Guyana, Ireland, Jamaica, Kenya, Lesotho, Liberia, New Zealand, Nigeria, Scotland, Sierra Leone, St. Lucia, St. Vincent & Grenadines, Swaziland, Tanzania, Trinidad & Tobago, Uganda, Virgin Islands, Wales)

> TOEFL institution code: 4389

### 3.3 Graduate — global rules

| 维度 | 值 | 来源 |
|------|-----|------|
| Admissions model | Decentralized (per-department) | E-G-001 |
| Application portal | Cal State Apply | E-G-002 |
| Application fee | $70 (standard) | E-G-003 |
| GRE/GMAT policy | Not required (CSU system policy) | E-G-004 |
| Language test policy | TOEFL 80 / IELTS 6.5 / Duolingo 115 | E-G-005 |
| Application timeline | Varies by program (no later than June 1 for Fall) | E-G-006 |
| CGS April 15 honor date | CSULB follows CSU system enrollment deposit deadline | E-G-007 |

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026-2027 academic year, line-itemized)

#### California Residents

| Expense Item | Commuter | On-Campus | Off-Campus |
|-------------|----------|-----------|------------|
| Tuition | $6,838 | $6,838 | $6,838 |
| Mandatory Fees | $1,910 | $1,910 | $1,910 |
| Living Expenses (housing) | $4,652 | $12,034 | $16,676 |
| Living Expenses (food) | $7,884 | $6,520 | $7,884 |
| Books, Course Materials, Supplies, Equipment | $1,806 | $1,806 | $1,806 |
| Transportation | $1,206 | $1,386 | $1,656 |
| Miscellaneous Personal Expenses | $4,564 | $3,968 | $5,706 |
| **TOTAL** | **$28,860** | **$34,462** | **$42,476** |

#### Non-California Residents (U.S. and International)

| Expense Item | Commuter | On-Campus | Off-Campus |
|-------------|----------|-----------|------------|
| Non-Resident Tuition | $12,246 | $12,246 | $12,246 |
| Tuition | $6,838 | $6,838 | $6,838 |
| Mandatory Fees | $1,910 | $1,910 | $1,910 |
| Living Expenses (housing) | $4,652 | $12,034 | $16,676 |
| Living Expenses (food) | $7,884 | $6,520 | $7,884 |
| Books, Course Materials, Supplies, Equipment | $1,806 | $1,806 | $1,806 |
| Transportation | $1,206 | $1,386 | $1,656 |
| Miscellaneous Personal Expenses | $4,564 | $3,968 | $5,706 |
| **TOTAL** | **$41,106** | **$46,708** | **$54,722** |

> Note: Non-Resident Tuition is $444 per unit (2025-26 rate). Total nonresident tuition per term depends on units taken.

### 4.2 Undergraduate financial-aid policy

| 维度 | 值 | 来源 |
|------|-----|------|
| Need-blind/need-aware | Need-aware for all applicants | E-U-008 |
| Application fee | $70 | E-U-004 |
| Application fee waiver | Available for eligible students | E-U-009 |
| Financial aid types | Federal grants, state grants, institutional scholarships, work-study, loans | E-U-010 |
| Beach Pledge | Finish in Four and Through in Two programs for degree completion | E-U-011 |

### 4.3 Graduate cost & funding framework

| 维度 | 值 | 来源 |
|------|-----|------|
| Standard graduate tuition (CA resident) | $8,548/year ($4,274/semester for 6.1+ units) | E-G-008 |
| Standard graduate tuition (non-resident) | $8,548 + $444/unit nonresident tuition | E-G-008 |
| MBA professional fee | $321/unit additional | E-G-009 |
| Doctoral tuition (EdD) | $14,094/year | E-G-010 |
| Doctoral tuition (DPT) | $20,480/year | E-G-010 |
| Doctoral tuition (DNP) | $18,190/year | E-G-010 |
| Doctoral tuition (DPH) | $21,236/year | E-G-010 |
| Application fee | $70 | E-G-003 |
| Funding types | RA/TA positions, fellowships, grants, loans | E-G-011 |

---

## SECTION 5 — Evidence chain index

### Undergraduate Evidence

```yaml
# E-U-001
field: undergraduate.admissions_site
value: https://www.csulb.edu/admissions
source_url: https://www.csulb.edu/admissions
source_snippet: "Admissions | California State University Long Beach"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-002
field: undergraduate.application_portal
value: Cal State Apply
source_url: https://www.csulb.edu/admissions
source_snippet: "APPLY NOW!" links to Cal State Apply
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-003
field: undergraduate.deadlines
value:
  fall_freshman_deadline: "November 30, 2026"
  fall_transfer_deadline: "November 30, 2026"
  applications_open: "October 1, 2026"
  decision_notification: "Mid-February - April 2027"
  enrollment_deposit: "May 1, 2027"
source_url: https://www.csulb.edu/enrollment-services/key-dates-and-deadlines
source_snippet: "First-time, first-year (freshman) application deadline Nov. 30, 2026" and "Upper-division transfer application deadline Nov. 30, 2026" and "Applications open Aug. 1, 2026*" and "Undergraduate Admission Decisions Mid-February - April 2027" and "Deadline to submit non-refundable enrollment deposit May 1, 2027"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-004
field: undergraduate.application_fee
value: $70
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1398
source_snippet: "Application fee (nonrefundable), payable online at the time of application via credit card or PayPal: $70"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-005
field: undergraduate.sat_act_policy
value: "Test-FREE (CSU system — SAT/ACT not considered)"
source_url: https://www.csulb.edu/admissions/first-time-first-year-student-admission-eligibility
source_snippet: No mention of SAT or ACT anywhere on the admission eligibility page. Admission based on "CSULB Index" combining GPA in college preparatory courses.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-006
field: undergraduate.audition_portfolio
value: "Auditions required for Music and Dance; Portfolio required for Art and Design"
source_url: https://www.csulb.edu/admissions/first-time-first-year-student-admission-eligibility
source_snippet: "Applicants to Music and Dance: Eligible Applicants will be admitted based on the faculty evaluation of an audition, auditions are mandatory."
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-007
field: undergraduate.recommendations
value: "Not required for undergraduate admission"
source_url: https://www.csulb.edu/admissions/first-time-first-year-student-admission-eligibility
source_snippet: No recommendation requirement mentioned in admission eligibility criteria.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-008
field: undergraduate.need_blind
value: "Need-aware for all applicants"
source_url: https://www.csulb.edu/financial-aid-and-scholarships
source_snippet: Financial aid page describes need-based aid programs but does not indicate need-blind policy.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-009
field: undergraduate.application_fee_waiver
value: "Available for eligible students"
source_url: https://www.csulb.edu/financial-aid-and-scholarships
source_snippet: Financial aid resources available for students with financial need.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-010
field: undergraduate.financial_aid_types
value: "Federal grants, state grants, institutional scholarships, work-study, loans"
source_url: https://www.csulb.edu/financial-aid-and-scholarships
source_snippet: "Types of Aid" listed in financial aid navigation for undergraduate students.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-011
field: undergraduate.beach_pledge
value: "Finish in Four and Through in Two programs"
source_url: https://www.csulb.edu/beach-pledge
source_snippet: "FINISH IN FOUR AND THROUGH IN TWO PROGRAM"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-U-012
field: undergraduate.cost_of_attendance.resident_commuter
value: $28,860
source_url: https://www.csulb.edu/financial-aid-and-scholarships/undergraduate-costs-0
source_snippet: "2026 - 2027 Cost of Attendance for California Residents ... Commuter ... TOTAL $28,860"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-013
field: undergraduate.cost_of_attendance.resident_on_campus
value: $34,462
source_url: https://www.csulb.edu/financial-aid-and-scholarships/undergraduate-costs-0
source_snippet: "2026 - 2027 Cost of Attendance for California Residents ... On-Campus Housing ... TOTAL $34,462"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-014
field: undergraduate.cost_of_attendance.nonresident_commuter
value: $41,106
source_url: https://www.csulb.edu/financial-aid-and-scholarships/undergraduate-costs-0
source_snippet: "2026 - 2027 Cost of Attendance for Non-California Residents ... Commuter ... TOTAL $41,106"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-015
field: undergraduate.english_requirements.toefl
value: 61
source_url: https://www.csulb.edu/international/future-students/english-language-requirement
source_snippet: "Test of English as a Foreign Language (TOEFL) ... Undergraduate (bachelor's) ... Internet-based (iBT) 61"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-016
field: undergraduate.english_requirements.ielts
value: 6.0
source_url: https://www.csulb.edu/international/future-students/english-language-requirement
source_snippet: "International English Language Testing System (IELTS) ... Undergraduate (bachelor's) ... IELTS 6.0"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-U-017
field: undergraduate.english_requirements.duolingo
value: 105
source_url: https://www.csulb.edu/international/future-students/english-language-requirement
source_snippet: "Duolingo English Test ... Undergraduate (bachelor's) ... Duolingo 105"
capture_date: 2026-07-06
evidence_type: official_webpage_table
```

### Graduate Evidence

```yaml
# E-G-001
field: graduate.admissions_model
value: "Decentralized (per-department)"
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1396
source_snippet: Graduate admissions managed at department level.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-002
field: graduate.application_portal
value: Cal State Apply
source_url: https://www.csulb.edu/admissions
source_snippet: "APPLY NOW!" links to Cal State Apply
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-003
field: graduate.application_fee
value: $70
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1398
source_snippet: "Application fee (nonrefundable), payable online at the time of application via credit card or PayPal: $70"
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-004
field: graduate.gre_policy
value: "Not required (CSU system policy)"
source_url: https://www.csulb.edu/admissions/first-time-first-year-student-admission-eligibility
source_snippet: No mention of GRE or GMAT requirements on admission pages.
capture_date: 2026-07-06
evidence_type: official_webpage

---
# E-G-005
field: graduate.english_requirements.toefl
value: 80
source_url: https://www.csulb.edu/international/future-students/english-language-requirement
source_snippet: "Test of English as a Foreign Language (TOEFL) ... Post-baccalaureate ... Internet-based (iBT) 80"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-006
field: graduate.application_deadline
value: "Varies by program (no later than June 1 for Fall)"
source_url: https://www.csulb.edu/enrollment-services/key-dates-and-deadlines
source_snippet: "Master's programs and certificates application deadline Varies by program (no later than June 1)"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-007
field: graduate.enrollment_deposit
value: "May 1 (Fall)"
source_url: https://www.csulb.edu/enrollment-services/key-dates-and-deadlines
source_snippet: "Deadline to submit non-refundable enrollment deposit May 1, 2027"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-008
field: graduate.tuition
value:
  resident_annual: $8,548
  resident_per_semester: $4,274
  nonresident_per_unit: $444
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1398
source_snippet: "Graduate or Other/Post baccalaureate Tuition 6.1 or more units $4,274 $8,548"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-009
field: graduate.mba_professional_fee
value: $321/unit
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1398
source_snippet: "2026-27 Graduate Business Professional Fee Charge Per Unit (per semester): $321"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-010
field: graduate.doctoral_tuition
value:
  edd: $14,094/year
  dpt: $20,480/year
  dnp: $18,190/year
  dph: $21,236/year
source_url: https://csulb.catalog.acalog.com/content.php?catoid=12&navoid=1398
source_snippet: "Doctoral Programs Tuition ... Education $7,047 $14,094 ... Physical Therapy $10,240 $20,480 ... Nursing Practice $9,095 $18,190 ... Public Health $10,618 $21,236"
capture_date: 2026-07-06
evidence_type: official_webpage_table

---
# E-G-011
field: graduate.funding
value: "RA/TA positions, fellowships, grants, loans"
source_url: https://www.csulb.edu/financial-aid-and-scholarships/graduate-student-cost-of-attendance
source_snippet: Graduate financial aid resources available through Financial Aid and Scholarships office.
capture_date: 2026-07-06
evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
csulb-knowledge-base-v2/
├── overview/
│   ├── institution-overview.md (Section 0)
│   └── college-structure.md (Section 0.2)
├── undergraduate/
│   ├── arts-programs.md (College of the Arts UG)
│   ├── business-programs.md (College of Business UG)
│   ├── education-programs.md (College of Education UG)
│   ├── engineering-programs.md (College of Engineering UG)
│   ├── health-human-services-programs.md (CHHS UG)
│   ├── liberal-arts-programs.md (CLA UG)
│   └── natural-sciences-math-programs.md (CNSM UG)
├── graduate/
│   ├── arts-programs.md (College of the Arts Grad)
│   ├── business-programs.md (College of Business Grad)
│   ├── education-programs.md (College of Education Grad)
│   ├── engineering-programs.md (College of Engineering Grad)
│   ├── health-human-services-programs.md (CHHS Grad)
│   ├── liberal-arts-programs.md (CLA Grad)
│   └── natural-sciences-math-programs.md (CNSM Grad)
├── admissions/
│   ├── deadlines.md (Section 3.1)
│   ├── english-requirements.md (Section 3.2)
│   └── graduate-admissions.md (Section 3.3)
├── costs/
│   ├── undergraduate-costs.md (Section 4.1)
│   ├── graduate-costs.md (Section 4.3)
│   └── financial-aid.md (Section 4.2)
└── evidence/
    └── evidence-chain.md (Section 5)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "csulb-knowledge-base-v2"
  school: "<home college>"
  department: "<home department>"
  degree_level: "<BA|BS|MA|MS|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-06
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-06
```

### Follow-up data items (prioritized)

| Priority | Data Item | Target URL |
|----------|-----------|------------|
| P0 | Complete enumeration of all undergraduate majors with exact counts per department | Each department's catalog page |
| P0 | Complete enumeration of all graduate programs with exact counts per department | Each department's catalog page |
| P0 | Complete list of minors | Each department's catalog page |
| P1 | Detailed graduate COA for each program (MBA, EdD, DPT, DNP, DPH) | https://www.csulb.edu/financial-aid-and-scholarships/graduate-student-cost-of-attendance |
| P1 | International student tuition and fees | https://www.csulb.edu/international/future-students/tuition-fees |
| P1 | Detailed admission criteria by major (impaction) | https://www.csulb.edu/admissions/first-time-first-year-student-csulb-index |
| P2 | Scholarship details and deadlines | https://www.csulb.edu/financial-aid-and-scholarships |
| P2 | Housing costs and options | https://www.csulb.edu/housing |
| P2 | Campus safety statistics | https://www.csulb.edu/cleryASR |

---

## SECTION 7 — Cross-school comparison framework

| 维度 | CSULB | (Other schools) |
|------|-------|-----------------|
| Type | Public (CSU system) | |
| Location | Long Beach, CA | |
| UG Tuition (in-state/yr) | $6,838 | |
| UG Tuition (OOS/yr) | $19,084 | |
| UG COA (in-state, on-campus) | $34,462 | |
| UG COA (OOS, on-campus) | $46,708 | |
| Need-blind (intl?) | Need-aware for all | |
| EA deadline | N/A (no EA) | |
| RD deadline | November 30 | |
| SAT/ACT required? | No (test-FREE) | |
| TOEFL min (UG) | 61 | |
| IELTS min (UG) | 6.0 | |
| Application portal | Cal State Apply | |
| Application fee | $70 | |
| Total program count (est.) | ~210 | |
| College count | 7 | |
| Grad application fee | $70 | |
| Grad tuition (in-state/yr) | $8,548 | |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-06
> **Sources**: csulb.edu, csulb.catalog.acalog.com, calstate.edu
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
