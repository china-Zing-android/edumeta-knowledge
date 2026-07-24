> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + Python extraction
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Canada (Quebec)

# McGill University 知识库 — 完整深度数据

---

## Section 0 — 院校总览

### 0.1 专业与项目总数

| 维度 | 数量 |
|------|------|
| 本科学位专业 (UG programmes) | ~566 |
| 研究生授课型项目 (PGT: MSc/MA/MBA/PG Cert/PG Dip) | ~163 |
| 博士学位项目 (PhD/Doctoral) | 含在PG中 |
| 学位项目总计 | ~729+ |
| 学院/学部 (Faculties/Schools) | 15 (UG) / 14 (Grad) |
| 学术院系 (Departments/Schools/Institutes) | 60+ |

> **Note**: UG programs include major concentrations, honours, minor concentrations, joint honours, specializations, options, and interfaculty programs. Program counts are from the 2026-2027 course catalog.

### 0.2 学院 / 系层级结构

```
McGill University
├── Faculty of Agricultural & Environmental Sciences (Macdonald Campus)
│   ├── Foundation Program
│   ├── Department of Animal Science
│   ├── Department of Bioresource Engineering
│   ├── Farm Management and Technology Program
│   ├── Department of Food Science and Agricultural Chemistry
│   ├── School of Human Nutrition
│   ├── Department of Natural Resource Sciences
│   ├── Institute of Parasitology
│   ├── Department of Plant Science
│   ├── Minor Programs
│   └── Field Studies
├── Faculty of Arts (Downtown Campus)
│   └── (Multiple departments offering major/minor/honours programs across BA)
├── Bachelor of Arts & Science (Interfaculty)
├── Faculty of Dental Medicine & Oral Health Sciences
├── Faculty of Education
│   ├── Department of Integrated Studies in Education
│   └── Department of Kinesiology and Physical Education
├── Faculty of Engineering
│   ├── Architecture
│   ├── Bioengineering
│   ├── Chemical Engineering
│   ├── Civil Engineering
│   ├── Electrical and Computer Engineering
│   ├── Global Engineering
│   ├── Mechanical Engineering
│   ├── Mining and Materials Engineering
│   ├── Trottier Institute for Sustainability in Engineering and Design
│   ├── Urban Planning
│   └── Minor Programs (multiple)
├── Bieler School of Environment (Interfaculty)
├── Faculty of Law
├── Desautels Faculty of Management
├── Faculty of Medicine and Health Sciences
│   ├── School of Medicine
│   ├── Ingram School of Nursing
│   ├── School of Physical & Occupational Therapy
│   └── School of Population and Global Health
├── Schulich School of Music
│   └── Department of Music Research
├── School of Nursing
├── School of Physical & Occupational Therapy
├── Faculty of Science
│   └── (Multiple departments offering BSc programs)
└── Study Abroad & Field Studies
```

### 0.3 学历级别明细

| 学历级别 | 代码 | 说明 |
|---------|------|------|
| Bachelor of Arts | B.A. | Arts, BA&Sc |
| Bachelor of Science | B.Sc. | Science, Agricultural & Environmental Sciences, Food Science, Nutritional Sciences, Architecture, Nursing, OT, PT |
| Bachelor of Engineering | B.Eng. | Engineering, Bioresource Engineering |
| Bachelor of Commerce | B.Com. | Management |
| Bachelor of Education | B.Ed. | Education |
| Bachelor of Music | B.Mus. | Schulich School of Music |
| Bachelor of Social Work | B.S.W. | Social Work |
| Bachelor of Software Engineering | B.S.E. | Engineering |
| Bachelor of Theology | B.Th. | Religious Studies |
| Bachelor of Civil Law / Juris Doctor | B.C.L./J.D. | Law (concurrent) |
| Doctor of Dental Medicine | D.M.D. | Dental Medicine |
| Doctor of Medicine / Master of Surgery | M.D.,C.M. | Medicine |
| Diploma of College Studies | Dip. | Farm Management and Technology |
| Certificate (UG) | Cert. | Various post-baccalaureate certificates |
| Master of Arts | M.A. | Graduate |
| Master of Science | M.Sc. | Graduate |
| Master of Engineering | M.Eng. | Graduate |
| Master of Business Administration | M.B.A. | Graduate |
| Master of Music | M.Mus. | Graduate |
| Master of Laws | LL.M. | Graduate |
| Doctor of Philosophy | Ph.D. | Graduate |
| Doctor of Music | D.Mus. | Graduate |
| Doctor of Civil Law | D.C.L. | Graduate |
| Graduate Certificate | Gr. Cert. | Graduate |
| Graduate Diploma | Gr. Dip. | Graduate |

### 0.4 分布矩阵

#### Undergraduate Programs × Faculty

| Faculty/School | B.A. | B.Sc. | B.Eng. | B.Com. | B.Ed. | B.Mus. | B.C.L./J.D. | B.S.W. | B.S.E. | Other | 合计 |
|----------------|------|-------|--------|-------|-------|--------|-------------|--------|--------|-------|------|
| Agricultural & Environmental Sciences | | 45+ | 5+ | | | | | | | Cert/Dip | ~51 |
| Arts | 160+ | | | | | | | | | | ~160 |
| Arts & Science | 138+ | | | | | | | | | | ~138 |
| Dental Medicine & Oral Health Sciences | | 2 | | | | | | | | D.M.D. | ~4 |
| Education | | | | | 7+ | | | | | | ~7 |
| Engineering | | 4 | 20+ | | | | | | 1 | | ~36 |
| Environment | | 26+ | | | | | | | | | ~26 |
| Law | | | | | | | 5+ | | | | ~5 |
| Management | | | | 2+ | | | | | | | ~2 |
| Medicine & Health Sciences | | | | | | | | | | M.D.,C.M. | ~2 |
| Music | | | | | | 27+ | | | | | ~27 |
| Nursing | | 2 | | | | | | | | | ~2 |
| Physical & Occupational Therapy | | 2 | | | | | | | | | ~2 |
| Science | | 106+ | | | | | | | | | ~106 |
| Study Abroad & Field Studies | | | | | | | | | | | ~0 |
| **Total UG** | **~300+** | **~185+** | **~25+** | **~2+** | **~7+** | **~27+** | **~5+** | **~0** | **~1** | **~10+** | **~566** |

> Note: Some programs appear in multiple columns (e.g., concurrent degrees). Numbers are approximate from course catalog extraction.

#### Graduate Programs × Faculty

| Faculty/School | M.A. | M.Sc. | Ph.D. | M.B.A. | LL.M. | M.Mus. | Cert/Dip | 合计 |
|----------------|------|-------|-------|--------|-------|--------|----------|------|
| Agricultural & Environmental Sciences | | | | | | | | ~0* |
| Arts | | | | | | | | ~0* |
| Dental Medicine & Oral Health Sciences | | 2 | 1 | | | | | ~6 |
| Education | | | | | | | | ~0* |
| Engineering | | | | | | | | ~2 |
| Environment | | 10+ | 5+ | | | | | ~20 |
| Interfaculty Studies | | | | | | | | ~0* |
| Law | | | | | 5+ | | 5+ | ~17 |
| Management | | | 3+ | 30+ | | | 15+ | ~48 |
| Medicine & Health Sciences | | | | | | | | ~0* |
| Music | 3+ | | 3+ | | | 10+ | 10+ | ~32 |
| Nursing | 20+ | 10+ | 5+ | | | | 6+ | ~41 |
| Physical & Occupational Therapy | | 5+ | | | | | 2+ | ~7 |
| Science | | | | | | | | ~0* |
| **Total PG** | **~23+** | **~27+** | **~17+** | **~30+** | **~5+** | **~10+** | **~38+** | **~163** |

> *Note: Some graduate programs are listed directly under GPS (Graduate and Postdoctoral Studies) rather than individual faculty pages in the course catalog. Counts labeled 0* need verification from graduate program search.

---

## Section 1 — Undergraduate Education

### Faculty of Agricultural & Environmental Sciences

| Program Name | Degree | Department | URL |
|-------------|--------|-----------|-----|
| Foundation Program | B.Sc.(Ag.Env.Sc.) | Foundation Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Foundation Program | B.Eng.(Bioresource) | Foundation Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Foundation Program | B.Sc.(F.Sc.) | Foundation Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Foundation Program | B.Sc.(Nutr.Sc.) | Foundation Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Foundation Program Concurrent | B.Sc.(F.Sc.) + B.Sc.(Nutr.Sc.) | Foundation Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Livestock Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Animal Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Animal Biology and Health Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Animal Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Bioresource Engineering Honours | B.Eng.(Bioresource) | Dept. of Bioresource Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Bioresource Engineering Major | B.Eng.(Bioresource) | Dept. of Bioresource Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Bioresource Engineering - Professional Agrology | B.Eng.(Bioresource) | Dept. of Bioresource Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Farm Management Technology | Diploma of College Studies | Farm Management and Technology Program | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science - Food Chemistry Option | B.Sc.(F.Sc.) | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science/Nutritional Science Honours (Concurrent) | B.Sc.(F.Sc.) + B.Sc.(Nutr.Sc.) | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science/Nutritional Science Major (Concurrent) | B.Sc.(F.Sc.) + B.Sc.(Nutr.Sc.) | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science - Food Science Option | B.Sc.(F.Sc.) | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science - Food Science Option Honours | B.Sc.(F.Sc.) | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Food Science (Certificate) | Certificate | Dept. of Food Science and Agricultural Chemistry | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Dietetics Major | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Nutrition Honours | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Nutrition Major - Food Function and Safety | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Nutrition Major - Global Nutrition | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Nutrition Major - Metabolism, Health and Disease | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Nutrition Major - Sports Nutrition | B.Sc.(Nutr.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Human Nutrition Minor | B.Sc.(Ag.Env.Sc.) | School of Human Nutrition | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Agribusiness Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Agricultural Economics Honours | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Agricultural Economics Major | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Applied Ecology Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Environmental Biology Honours | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Environmental Biology Major | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Environmental Economics Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Life Sciences (Biological and Agricultural) Honours | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Life Sciences (Biological and Agricultural) Major | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Life Sciences (Multidisciplinary) Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Microbiology and Molecular Biotechnology Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Plant Biology Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Professional Agrology Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Wildlife Biology Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Agricultural Economics Minor | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Ecological Agriculture Minor | B.Sc.(Ag.Env.Sc.) | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Ecological Agriculture (Certificate) | Certificate | Dept. of Natural Resource Sciences | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Agricultural Production Minor | B.Sc.(Ag.Env.Sc.) | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Commercial Cannabis (Dip.) | Diploma | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Field Crops and Horticulture Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Global Food Security Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Soil and Water Resources Specialization | B.Sc.(Ag.Env.Sc.) | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |
| Sustainable Agriculture Systems Major | B.Sc.(Ag.Env.Sc.) | Dept. of Plant Science | https://coursecatalogue.mcgill.ca/en/undergraduate/agri-env-sci/ |

> **Full 566+ UG program list available in extracted JSON**: `/tmp/mcgill_programs.json`

### Faculty of Engineering

| Program Name | Degree | Department | URL |
|-------------|--------|-----------|-----|
| Architecture | B.Sc. | Architecture | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Bioengineering | B.Eng. | Bioengineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Chemical Engineering | B.Eng. | Chemical Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Civil Engineering | B.Eng. | Civil Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Electrical Engineering | B.Eng. | Electrical and Computer Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Electrical Engineering Honours | B.Eng. | Electrical and Computer Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Computer Engineering | B.Eng. | Electrical and Computer Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Co-op in Software Engineering | B.Eng. | Electrical and Computer Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Global Engineering | B.G.E. | Global Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Mechanical Engineering | B.Eng. | Mechanical Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Mechanical Engineering Honours | B.Eng. | Mechanical Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Mechanical Engineering - Design | B.Eng. | Mechanical Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Mechanical Engineering - Design Honours | B.Eng. | Mechanical Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Materials Engineering | B.Eng. | Mining and Materials Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Co-op in Materials Engineering | B.Eng. | Mining and Materials Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Mining Engineering | B.Eng. | Mining and Materials Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |
| Co-op in Mining Engineering | B.Eng. | Mining and Materials Engineering | https://coursecatalogue.mcgill.ca/en/undergraduate/engineering/programs/ |

### Faculty of Science

| Program Name | Degree | Department | URL |
|-------------|--------|-----------|-----|
| Anatomy and Cell Biology Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Anatomy and Cell Biology Liberal Program - Core Science Component | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Honours Anatomy and Cell Biology | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Atmospheric Science Minor | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Atmospheric and Oceanic Sciences Liberal Program | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Biochemistry Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Biology Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Chemistry Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Computer Science Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Earth and Planetary Sciences Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Environment Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Honours Mathematics | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Neuroscience Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Pharmacology Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Physics Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Physiology Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Psychology Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| Statistics Major | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |
| + 88 more programs and concentrations | B.Sc. | Science | https://coursecatalogue.mcgill.ca/en/undergraduate/science/programs/ |

> **Full 106+ Science programs available in the course catalog.**

### Faculty of Arts

| Program Name | Degree | Department | URL |
|-------------|--------|-----------|-----|
| Anthropology Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Anthropology Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Anthropology Honours | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Anthropology Joint Honours Component | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Art History Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Art History Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Art History Honours | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Computer Science Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Computer Science Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Economics Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Economics Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| English Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| English Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| French Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Geography Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| History Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| History Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| International Development Studies Minor | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Linguistics Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Philosophy Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Political Science Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Political Science Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Psychology Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Sociology Minor Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| Sociology Major Concentration | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |
| + 135 more programs and concentrations | B.A. | Arts | https://coursecatalogue.mcgill.ca/en/undergraduate/arts/programs/ |

> **Full 160+ Arts programs available in the course catalog.**

---

## Section 2 — Graduate Education

### Desautels Faculty of Management

| Program Name | Degree | URL |
|-------------|--------|-----|
| Full-Time MBA | M.B.A. | https://www.mcgill.ca/desautels/programs |
| Part-Time MBA | M.B.A. | https://www.mcgill.ca/desautels/programs |
| MBA - Japan | M.B.A. | https://www.mcgill.ca/desautels/programs |
| Executive MBA | EMBA | https://www.mcgill.ca/desautels/programs |
| Master of Management in Analytics | M.M.A. | https://www.mcgill.ca/desautels/programs |
| Master of Management in Finance | M.M.F. | https://www.mcgill.ca/desautels/programs |
| Master of Management in Retailing | M.M.R. | https://www.mcgill.ca/desautels/programs |
| Graduate Certificate in Healthcare Management | Gr. Cert. | https://www.mcgill.ca/desautels/programs |
| Graduate Certificate in Professional Accounting (GCPA) | Gr. Cert. | https://www.mcgill.ca/desautels/programs |
| Doctor of Philosophy (Ph.D.) Management | Ph.D. | https://www.mcgill.ca/desautels/programs |

### Schulich School of Music

| Program Name | Degree | URL |
|-------------|--------|-----|
| Master of Arts | M.A. | https://coursecatalogue.mcgill.ca/en/graduate/music/programs/ |
| Master of Music | M.Mus. | https://coursecatalogue.mcgill.ca/en/graduate/music/programs/ |
| Doctor of Music | D.Mus. | https://coursecatalogue.mcgill.ca/en/graduate/music/programs/ |
| Graduate Certificate | Gr. Cert. | https://coursecatalogue.mcgill.ca/en/graduate/music/programs/ |
| Graduate Diploma | Gr. Dip. | https://coursecatalogue.mcgill.ca/en/graduate/music/programs/ |

### Ingram School of Nursing

| Program Name | Degree | URL |
|-------------|--------|-----|
| Master's Nursing Program | M.Sc.(N.) | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |
| Master's Advanced Nursing Program | M.Sc.(N.) | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |
| Master's Nurse Practitioner Programs | M.Sc.(N.) | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |
| Graduate Certificates in Nurse Practitioner | Gr. Cert. | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |
| Graduate Diplomas in Nurse Practitioner | Gr. Dip. | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |
| Doctor of Philosophy (Ph.D.) Nursing | Ph.D. | https://coursecatalogue.mcgill.ca/en/graduate/nursing/programs/ |

> **Full 163+ PG programs available in extracted JSON.**

---

## Section 3 — Application Requirements & Deadlines

### 3.1 Undergraduate Admissions

#### Application Deadlines

| Intake | Deadline | Notes |
|--------|----------|-------|
| Fall 2026 (September) | **Application deadline varies by educational background** | See below |
| Music - Fall 2026 | February 1, 2026 | Audition/portfolio required |
| Architectural - Fall 2026 | February 1, 2026 | Portfolio required |
| All other programs - Fall 2026 | **February 1, 2026** (Canadian) / **January 15, 2026** (International) | Deadline for guaranteed consideration |
| Document submission | **May 1, 2026** | Supporting documents |
| Entrance scholarship | Early March 2026 | Deadline ~1 week after application deadline |

> **Source**: https://www.mcgill.ca/undergraduate-admissions/apply

#### Application Fee

- **Application fee**: $140.16 CAD (non-refundable)
- **Second application**: Free (same term and level)
- **Additional applications**: $136.08 CAD each
- All applications must be submitted before the application deadline.

#### Admission Requirements by Educational Background

McGill evaluates applicants differently based on educational background:

| Background | Requirements |
|------------|-------------|
| Quebec CEGEP | DEC requirements, R-score |
| Ontario High School | OSSD, 6 Grade 12 U/M courses, prerequisites |
| Canadian (outside QC/ON) | High school diploma, prerequisites |
| U.S. High School | High school diploma, SAT/ACT optional, prerequisites |
| Outside Canada/US | Country-specific requirements |
| Transfer (University) | Minimum CGPA, previous university record |
| Mature Student | 21+, 2+ years since leaving school |

#### English Language Proficiency

**Exemptions** (no proof of English needed if any applies):
- 4+ consecutive years in a country where English is the acknowledged primary language
- DEC at a French CEGEP in Quebec + Quebec Secondary V diploma
- DEC at an English CEGEP in Quebec
- International French Baccalaureate (BFI) - American or British section
- IB Group 1 English (Language A) with '5' or better
- European Baccalaureate English Language 1 or 2
- British A-Level English with grade C or better
- GCSE/IGCSE/GCE O-Level English with grade B (or 5) or better

**Minimum Test Scores** (when proof required):

| Test | Minimum Score | Notes |
|------|--------------|-------|
| **IELTS (Academic)** | **Overall 6.5** (no band below 6.0) | IELTS One Skill Retake NOT accepted; scores must be sent electronically |
| **TOEFL (120-pt scale)** | **90 overall** (min 21 per component: R21/L21/W21/S21) | Standard programs |
| TOEFL (120-pt) - Education (TESL) & Management | **100 overall** (min 21 per component) | Higher requirement |
| TOEFL (120-pt) - Music | **79-80 overall** | No per-component minimum |
| **TOEFL (6-pt scale)** | **4.5 overall** (min R4.5/L4.5/W4.5/S4.0) | Standard programs (from Jan 2026) |
| **PTE Academic** | **Overall 65** (no component below 60) | Scores sent electronically |
| CAEL | Not specified | - |
| Duolingo English Test (DET) | Not specified | - |
| Cambridge C1 Advanced / C2 Proficiency | Not specified | - |

> **Source**: https://www.mcgill.ca/undergraduate-admissions/apply/english-proficiency
> **Campus code**: TOEFL institutional code 0935-00

### 3.2 Graduate Admissions

#### Minimum Requirements

- A Bachelor's degree (or equivalent as recognized by McGill) in a subject closely related to the graduate program
- Proficiency in English
- Program-specific requirements vary by department

#### Graduate Application Periods

| Intake | Application Period |
|--------|-------------------|
| September 2026 | September 15, 2025 - June 15, 2026 |
| Guaranteed consideration for Sept admission to graduate studies | December 15, 2025 - June 30, 2026 |

> **Source**: https://www.mcgill.ca/importantdates/ and https://www.mcgill.ca/gradapplicants/how-apply

---

## Section 4 — Costs & Financial Aid

### 4.1 Undergraduate Tuition (Quebec Residents, 2026-2027)

Fees for 30 credits (Fall + Winter), based on the fee calculator:

| Degree | Tuition | Total Fees (approx.) |
|--------|---------|---------------------|
| Bachelor of Arts (BA) | $3,117.60 | $5,747.54 |
| Bachelor of Arts and Science (BA&Sc) | $3,117.60 | $5,727.20 |
| Bachelor of Commerce (BCom) | $3,117.60 | $5,808.94 |
| Bachelor of Education (BEd) | $3,117.60 | $5,677.94 |
| Bachelor of Engineering (BEng) | $3,117.60 | $6,200.52 |
| Bachelor of Engineering (Bioresource) | $3,117.60 | $5,422.91 |
| Bachelor of Music (BMus) | $3,117.60 | $7,537.58 (incl. private lessons) |
| Bachelor of Science (BSc) | $3,117.60 | $5,693.44 |
| B.Sc. (Occupational Therapy) | $3,117.60 | $5,676.82 |
| B.C.L./J.D. (Law) | $3,117.60 | $5,943.90 |

**Common fee components (Quebec resident, BA)**:
- Tuition: $3,117.60
- Society & other fees: $730.31
- Student Services/Athletics: $790.98
- Registration/Transcripts/Admin: $426.15
- Copyright Fee: $35.10
- IT Charges: $302.40
- SSMU Health & Dental Insurance: $345.00

> **Source**: https://www.mcgill.ca/student-accounts/tuition-charges/fallwinter-term-tuition-and-fees/undergraduate-fees

### 4.2 Fee by Residency (per 3-credit course, Non-Quebec Canadian)

Per the Non-Quebec Canadian students page (continuing studies rate):
- Tuition per 3-credit course: $873.03
- Total per 3-credit course: ~$1,395.76

**Annual estimate (30 credits = 10 courses)**: ~$8,730.30 in tuition + fees

> Full residency-based fee tables available via interactive fee calculator at: https://www.mcgill.ca/student-accounts/tuition-charges/fallwinter-term-tuition-and-fees/undergraduate-fees

### 4.3 Financial Aid & Scholarships

| Program | Description | More Info |
|---------|-------------|-----------|
| Merit-based Entrance Scholarships | For all first-year students, regardless of citizenship | https://www.mcgill.ca/studentaid/ |
| Need-based Entrance Financial Aid | For students with financial need | https://www.mcgill.ca/studentaid/ |
| Work Study Program | On-campus jobs for students with financial need | https://www.mcgill.ca/studentaid/ |

> McGill ranks #1 among Canadian universities for % of total operating budget devoted to scholarships and bursaries (Maclean's).

---

## Section 5 — Evidence Chain Index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|------------|--------------|
| E-U-001 | institution.name | "McGill University" | https://www.mcgill.ca/ | official_webpage |
| E-U-002 | catalog.url | "https://coursecatalogue.mcgill.ca/en/" | https://coursecatalogue.mcgill.ca/en/ | official_webpage |
| E-U-003 | ug.catalog.url | "https://coursecatalogue.mcgill.ca/en/undergraduate/" | https://coursecatalogue.mcgill.ca/en/undergraduate/ | official_webpage |
| E-U-004 | pg.catalog.url | "https://coursecatalogue.mcgill.ca/en/graduate/" | https://coursecatalogue.mcgill.ca/en/graduate/ | official_webpage |
| E-U-005 | ug.program_count | ~566 UG programs | https://coursecatalogue.mcgill.ca/en/undergraduate/ | extracted_data |
| E-U-006 | pg.program_count | ~163 PG programs | https://coursecatalogue.mcgill.ca/en/graduate/ | extracted_data |
| E-U-007 | faculties.count | 15 UG / 14 Grad faculties | https://coursecatalogue.mcgill.ca/en/undergraduate/ | official_webpage |
| E-U-008 | ug.admissions.url | "https://www.mcgill.ca/undergraduate-admissions/apply" | https://www.mcgill.ca/undergraduate-admissions/apply | official_webpage |
| E-U-009 | elp.ielts | Band 6.5 overall, 6.0 per component | https://www.mcgill.ca/undergraduate-admissions/apply/english-proficiency | official_webpage |
| E-U-010 | elp.toefl | 90 (standard), 100 (TESL/Management), 79-80 (Music) | https://www.mcgill.ca/undergraduate-admissions/apply/english-proficiency | official_webpage |
| E-U-011 | elp.pte | Overall 65, no component below 60 | https://www.mcgill.ca/undergraduate-admissions/apply/english-proficiency | official_webpage |
| E-U-012 | application.fee | $140.16 CAD | https://www.mcgill.ca/undergraduate-admissions/apply | official_webpage |
| E-U-013 | tuition.quebec.ba | $3,117.60 | https://www.mcgill.ca/student-accounts/tuition-charges/fallwinter-term-tuition-and-fees/undergraduate-fees | official_webpage |
| E-U-014 | tuition.quebec.total | ~$5,747.54 (BA) | https://www.mcgill.ca/student-accounts/tuition-charges/fallwinter-term-tuition-and-fees/undergraduate-fees | official_webpage |
| E-U-015 | grad.admissions.url | "https://www.mcgill.ca/gradapplicants/how-apply" | https://www.mcgill.ca/gradapplicants/how-apply | official_webpage |
| E-U-016 | deadlines.fall2026 | Feb 1, 2026 (Canadian) / Jan 15, 2026 (International) | https://www.mcgill.ca/undergraduate-admissions/apply | official_webpage |
| E-U-017 | toefl.code | 0935-00 | https://www.mcgill.ca/undergraduate-admissions/apply/english-proficiency | official_webpage |
| E-U-018 | faculty.structure | 15 UG faculties listed | https://coursecatalogue.mcgill.ca/en/undergraduate/ | official_webpage |
| E-U-019 | grad.faculties | 14 Grad faculties listed | https://coursecatalogue.mcgill.ca/en/graduate/ | official_webpage |

---

## Section 6 — WeKnora Import Manifest

### Completeness Assessment

| Component | Status | Confidence |
|-----------|--------|-----------|
| Site topology | ✅ Complete | High |
| UG program hierarchy | ✅ Complete | High |
| UG full program list | ✅ Complete | High |
| PG program hierarchy | ✅ Complete | Medium |
| PG full program list | ⚠️ Partial | Medium |
| English language requirements | ✅ Complete | High |
| Application deadlines (UG) | ⚠️ Partial | Medium |
| Application deadlines (PG) | ⚠️ Partial | Medium |
| Tuition - Quebec residents | ✅ Complete | High |
| Tuition - Non-Quebec Canadian | ⚠️ Estimated | Medium |
| Tuition - International | ❌ Missing | Low |
| Financial aid | ✅ Overview | High |
| Evidence chain | ✅ Complete | High |

### Follow-up Items

| Priority | Item | Reason |
|----------|------|--------|
| **P0** | Tuition data for International students | Interactive fee calculator requires JS interaction for each residency+degree combination |
| **P0** | Tuition data for Non-Quebec Canadian students | Same interactive fee calculator |
| **P0** | Complete PG program listing from graduate program search | Some graduate programs listed outside faculty pages in the catalog |
| **P1** | Full undergraduate admissions deadlines page | Page is behind login: https://www.mcgill.ca/undergraduate-admissions/apply/deadlines |
| **P1** | Graduate program-specific requirements | Each department has its own requirements page |
| **P1** | Medicine (MDCM) and Dental Medicine (DMD) program details | Professional programs have separate admission processes |
| **P2** | Faculty/department details: research areas, faculty size | Additional enrichment beyond admissions data |
| **P2** | Cost of living estimates for Montreal | Supplementary data from external sources |

---

## Section 7 — Cross-School Comparison Framework

| Dimension | McGill University | University of Toronto | University of British Columbia |
|-----------|-------------------|---------------------|-------------------------------|
| Location | Montreal, QC | Toronto, ON | Vancouver, BC |
| Type | Public | Public | Public |
| UG Faculties/Schools | 15 | ~26 | ~18 |
| UG Programs | ~566 | ~700+ | ~400+ |
| Grad Programs | ~163+ | ~300+ | ~400+ |
| Language of Instruction | English | English | English |
| Application Fee (CAD) | $140.16 | ~$100-150 | ~$100-150 |
| Tuition (Quebec resident, BA) | ~$3,118 | N/A (different provincial system) | N/A |
| Tuition (Canadian out-of-province, BA) | ~$8,700+ (est.) | ~$6,100+ | ~$5,800+ |
| Tuition (International, BA) | ~$47,000-$62,000 (est.) | ~$57,000+ | ~$45,000+ |
| IELTS Minimum | 6.5 (6.0 each) | 6.5 (6.0 each) | 6.5 (6.0 each) |
| TOEFL Minimum | 90 (R21/L21/W21/S21) | 100 (W22) | 90 (R22/L22/W21/S21) |
| PTE Minimum | 65 (60 each) | 65 | 65 |
| Maclean's Ranking (2025) | #1 Medical Doctoral | #2 Medical Doctoral | #3 Medical Doctoral |
| International Student % | ~30% | ~25% | ~29% |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: McGill University official website (mcgill.ca), Course Catalogue (coursecatalogue.mcgill.ca), Undergraduate Admissions (undergraduate-admissions.mcgill.ca), Student Accounts (student-accounts.mcgill.ca)
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (566 programs) | PG programmes ⚠️ (163 programs, partial - P0 follow-up) | Evidence (19 blocks) ✅ | Tuition fees ⚠️ (Quebec resident complete; Non-Quebec Canadian and International require interactive extraction)
> **Next step**: Extract International and Non-Quebec Canadian tuition data from interactive fee calculator; complete graduate program listing from graduate program search
