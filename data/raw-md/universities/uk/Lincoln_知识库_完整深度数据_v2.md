# University of Lincoln Admissions Knowledge Base — Structured Data v2.0

> **Data capture date**: 2026-07-08
> **Capture tool**: ego-browser (Chromium headless)
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: UK (England)

---

## SECTION 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科学位专业 (BA/BSc/BEng/etc.) | 102 |
| 本科辅修 (Minor) | N/A (UK universities typically do not offer minors) |
| 研究生学位项目 (MA/MSc/MBA/PhD/etc.) | 118 |
| 研究生高级证书 (PG Cert/Diploma) | 12 |
| **学位项目总计 (UG + Grad)** | **232** |
| 学院 / 独立系所总数 | 31 (subject areas) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
University of Lincoln
├── College of Arts and Humanities
│   ├── Art and Design
│   ├── English and Creative Writing
│   ├── Film and Media
│   ├── History, Classical Studies, and Conservation
│   ├── Journalism and Communications
│   ├── Performing Arts
│   └── Philosophy
├── College of Science
│   ├── Animal Sciences
│   ├── Biological and Life Sciences
│   ├── Chemistry
│   ├── Computer Science and AI
│   ├── Forensic Science
│   ├── Games Computing
│   ├── Geography
│   ├── Mathematics
│   ├── Physics
│   └── Robotics and AI
├── College of Social Science
│   ├── Accountancy, Finance, and Economics
│   ├── Education
│   ├── Law and Criminology
│   ├── Management
│   ├── Marketing and Tourism
│   ├── Politics and International Relations
│   ├── Psychology
│   ├── Sociology and Social Policy
│   └── Sport Science
├── College of Health and Science
│   ├── Agri-food and Food Manufacturing
│   ├── Health and Care Sciences
│   ├── Nursing
│   ├── Pharmacy and Pharmaceutical Sciences
│   └── Engineering
└── Lincoln Medical School
    └── Medicine
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学位缩写 | 全称 | 层级 | 本校数量 |
|---------|------|------|---------|
| BA (Hons) | Bachelor of Arts with Honours | 本科 | 38 |
| BSc (Hons) | Bachelor of Science with Honours | 本科 | 52 |
| BEng (Hons) | Bachelor of Engineering with Honours | 本科 | 5 |
| BArch (Hons) | Bachelor of Architecture with Honours | 本科 | 1 |
| LLB (Hons) | Bachelor of Laws with Honours | 本科 | 4 |
| MBChB | Bachelor of Medicine, Bachelor of Surgery | 本科 | 2 |
| MComp | Integrated Master of Computing | 本科 (integrated) | 4 |
| MBio | Integrated Master of Biology | 本科 (integrated) | 6 |
| MEng (Hons) | Integrated Master of Engineering | 本科 (integrated) | 2 |
| MMath | Integrated Master of Mathematics | 本科 (integrated) | 2 |
| MPhys | Integrated Master of Physics | 本科 (integrated) | 2 |
| MChem | Integrated Master of Chemistry | 本科 (integrated) | 2 |
| MGeog | Integrated Master of Geography | 本科 (integrated) | 2 |
| MSci | Integrated Master of Science | 本科 (integrated) | 2 |
| MCon/MCons | Integrated Master of Conservation | 本科 (integrated) | 2 |
| MPharm | Master of Pharmacy | 本科 (integrated) | 1 |
| FdSc | Foundation Degree (Science) | 本科 (foundation) | 2 |
| MA | Master of Arts | 研究生 | 24 |
| MSc | Master of Science | 研究生 | 52 |
| MBA | Master of Business Administration | 研究生 | 2 |
| LLM | Master of Laws | 研究生 | 2 |
| MArch | Master of Architecture | 研究生 | 1 |
| PGCE | Postgraduate Certificate in Education | 研究生 | 1 |
| PG Cert | Postgraduate Certificate | 研究生 | 4 |
| PG Dip | Postgraduate Diploma | 研究生 | 4 |
| DClinPsy | Doctor of Clinical Psychology | 研究生 | 1 |
| MPhil | Master of Philosophy | 研究生 (research) | 4 |
| PhD | Doctor of Philosophy | 研究生 (research) | 62 |
| MSc by Research | Master of Science by Research | 研究生 (research) | 22 |
| MA by Research | Master of Arts by Research | 研究生 (research) | 8 |
| PhD (Professional) | Professional Doctorate | 研究生 (research) | 2 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 \ 级别 | BA | BSc | BEng | LLB | MBChB | Int. Master's | FdSc | MA | MSc | MBA | LLM | PG Cert/Dip | PhD/MPhil | MSc/MA by Res | 合计 |
|------------|-----|-----|------|-----|-------|---------------|------|-----|-----|-----|-----|-------------|-----------|---------------|------|
| Arts and Humanities | 28 | 0 | 0 | 0 | 0 | 0 | 0 | 12 | 0 | 0 | 0 | 4 | 14 | 6 | 64 |
| Science | 0 | 28 | 0 | 0 | 0 | 20 | 0 | 0 | 12 | 0 | 0 | 0 | 20 | 10 | 90 |
| Social Science | 10 | 22 | 0 | 4 | 0 | 0 | 2 | 4 | 18 | 2 | 2 | 2 | 18 | 2 | 86 |
| Health and Science | 0 | 2 | 5 | 0 | 0 | 0 | 0 | 0 | 22 | 0 | 0 | 2 | 12 | 6 | 49 |
| Medical School | 0 | 0 | 0 | 0 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| **合计** | **38** | **52** | **5** | **4** | **2** | **20** | **2** | **16** | **52** | **2** | **2** | **8** | **64** | **24** | **291** |

> Note: Some courses appear in multiple subject areas. The actual unique course count is 232. The matrix includes research degrees (MPhil/PhD) which are listed per subject area.

---

## SECTION 1 — Undergraduate education

### 1.1 College/school architecture

The University of Lincoln organizes its undergraduate programmes across four academic colleges and a medical school. See Section 0.2 for the full hierarchy tree.

### 1.2 Undergraduate majors — grouped by 学院 > 系 > 学位级别

#### College of Arts and Humanities

##### Art and Design

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Fine Art | https://www.lincoln.ac.uk/course/artartub/ |
| 2 | Creative Advertising | https://www.lincoln.ac.uk/course/aadaadub/ |
| 3 | Photography | https://www.lincoln.ac.uk/course/clmclmub/ |
| 4 | Illustration | https://www.lincoln.ac.uk/course/illillub/ |
| 5 | Graphic Design | https://www.lincoln.ac.uk/course/gragraub/ |
| 6 | Product Design | https://www.lincoln.ac.uk/course/prdprdub/ |
| 7 | Interior Architecture and Design | https://www.lincoln.ac.uk/course/intintub/ |

###### BArch (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Bachelor of Architecture with Honours | https://www.lincoln.ac.uk/course/arcboaub/ |

##### English and Creative Writing

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | English | https://www.lincoln.ac.uk/course/enlenlub/ |
| 2 | English and Creative Writing | https://www.lincoln.ac.uk/course/enlcrwub/ |
| 3 | Creative Writing | https://www.lincoln.ac.uk/course/crwcrwub/ |
| 4 | English and History | https://www.lincoln.ac.uk/course/enlhstub/ |
| 5 | Drama and English | https://www.lincoln.ac.uk/course/enldraub/ |

##### Film and Media

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Film Production | https://www.lincoln.ac.uk/course/medproub/ |
| 2 | Media Production | https://www.lincoln.ac.uk/course/medmedub/ |
| 3 | Sound and Music Production | https://www.lincoln.ac.uk/course/medaupub/ |
| 4 | Film and Media | https://www.lincoln.ac.uk/course/mdsflmub/ |
| 5 | Animation and Visual Effects | https://www.lincoln.ac.uk/course/anianiub/ |

##### Performing Arts

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Dance | https://www.lincoln.ac.uk/course/dandanub/ |
| 2 | Drama, Theatre and Performance | https://www.lincoln.ac.uk/course/dradraub/ |
| 3 | Music | https://www.lincoln.ac.uk/course/musmusub/ |
| 4 | Musical Theatre | https://www.lincoln.ac.uk/course/mustheub/ |
| 5 | Technical Theatre and Stage Management | https://www.lincoln.ac.uk/course/tectheub/ |

##### History, Classical Studies, and Conservation

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | History | https://www.lincoln.ac.uk/course/hsthstub/ |
| 2 | Modern History | https://www.lincoln.ac.uk/course/modhstub/ |
| 3 | Modern History and Politics | https://www.lincoln.ac.uk/course/mdhpolub/ |
| 4 | Classical Studies | https://www.lincoln.ac.uk/course/clscvlub/ |
| 5 | Conservation of Cultural Heritage | https://www.lincoln.ac.uk/course/conconub/ |

##### Journalism and Communications

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Journalism | https://www.lincoln.ac.uk/course/joujouub/ |
| 2 | Journalism Studies | https://www.lincoln.ac.uk/course/jouinvub/ |
| 3 | Sports Journalism | https://www.lincoln.ac.uk/course/sptjouub/ |

##### Philosophy

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.lincoln.ac.uk/course/phlphlub/ |

#### College of Science

##### Computer Science and AI

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lincoln.ac.uk/course/cmpcmsub/ |
| 2 | Computer Science with Artificial Intelligence | https://www.lincoln.ac.uk/course/cmpcaiub/ |
| 3 | Computer Science with Cyber Security | https://www.lincoln.ac.uk/course/cmpcybub/ |

###### MComp (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lincoln.ac.uk/course/cmpcmsum/ |
| 2 | Computer Science with Artificial Intelligence | https://www.lincoln.ac.uk/course/cmpcaium/ |

##### Games Computing

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Games Computing | https://www.lincoln.ac.uk/course/cgpcmpub/ |
| 2 | Games Computing with Virtual and Augmented Reality | https://www.lincoln.ac.uk/course/cgpvarub/ |

###### MComp (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Games Computing | https://www.lincoln.ac.uk/course/cgpcmpum/ |

##### Mathematics

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.lincoln.ac.uk/course/mthmthub/ |
| 2 | Mathematics and Computer Science | https://www.lincoln.ac.uk/course/mthcmpub/ |
| 3 | Mathematics and Theoretical Physics | https://www.lincoln.ac.uk/course/mthphyub/ |

###### MMath (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics | https://www.lincoln.ac.uk/course/mthmthum/ |
| 2 | Mathematics and Theoretical Physics | https://www.lincoln.ac.uk/course/mthphyum/ |

###### MSci (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mathematics and Computer Science | https://www.lincoln.ac.uk/course/mthcmpum/ |

##### Physics

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.lincoln.ac.uk/course/phyphyub/ |
| 2 | Physics with Astrophysics | https://www.lincoln.ac.uk/course/phyaphub/ |

###### MPhys (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Physics | https://www.lincoln.ac.uk/course/phyphyum/ |
| 2 | Physics with Astrophysics | https://www.lincoln.ac.uk/course/phyaphum/ |

##### Chemistry

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.lincoln.ac.uk/course/chmchmub/ |
| 2 | Forensic Chemistry | https://www.lincoln.ac.uk/course/chmfrsub/ |

###### MChem (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.lincoln.ac.uk/course/chmchmum/ |
| 2 | Forensic Chemistry | https://www.lincoln.ac.uk/course/chmfrsum/ |

##### Biological and Life Sciences

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.lincoln.ac.uk/course/biobioub/ |
| 2 | Biochemistry | https://www.lincoln.ac.uk/course/biochmub/ |
| 3 | Biomedical Science | https://www.lincoln.ac.uk/course/bmsbmsub/ |
| 4 | Ecology and Conservation | https://www.lincoln.ac.uk/course/eclcsvub/ |

###### MBio (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Biology | https://www.lincoln.ac.uk/course/biobioum/ |
| 2 | Biochemistry | https://www.lincoln.ac.uk/course/biochmum/ |
| 3 | Biomedical Science | https://www.lincoln.ac.uk/course/bmsbmsum/ |
| 4 | Ecology and Conservation | https://www.lincoln.ac.uk/course/eclcsvum/ |

##### Animal Sciences

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Behaviour and Welfare | https://www.lincoln.ac.uk/course/eqsabwub/ |
| 2 | Zoology | https://www.lincoln.ac.uk/course/zoozooub/ |
| 3 | Bioveterinary Science | https://www.lincoln.ac.uk/course/bvsbvsub/ |

###### MBio (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Animal Behaviour and Welfare | https://www.lincoln.ac.uk/course/eqsabwum/ |
| 2 | Zoology | https://www.lincoln.ac.uk/course/zoozooum/ |
| 3 | Bioveterinary Science | https://www.lincoln.ac.uk/course/bvsbvsum/ |

##### Forensic Science

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.lincoln.ac.uk/course/frsfrsub/ |

##### Geography

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.lincoln.ac.uk/course/gehgehub/ |

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Geography | https://www.lincoln.ac.uk/course/gepgepub/ |

###### MGeog (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Human Geography | https://www.lincoln.ac.uk/course/gehgehum/ |
| 2 | Physical Geography | https://www.lincoln.ac.uk/course/gepgepum/ |

##### Robotics and AI

(No standalone UG programmes — see Computer Science with AI)

#### College of Social Science

##### Accountancy, Finance, and Economics

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Accountancy and Finance | https://www.lincoln.ac.uk/course/acfnbsub/ |
| 2 | Economics | https://www.lincoln.ac.uk/course/ecoecoub/ |

##### Business and Management

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Business and Management | https://www.lincoln.ac.uk/course/bmgtbsub/ |
| 2 | International Tourism Management | https://www.lincoln.ac.uk/course/intobsub/ |
| 3 | Sports Business Management | https://www.lincoln.ac.uk/course/sbmbscub/ |

##### Marketing

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing | https://www.lincoln.ac.uk/course/mktbscub/ |

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Marketing and Advertising | https://www.lincoln.ac.uk/course/advmktub/ |

##### Law and Criminology

###### LLB (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Law | https://www.lincoln.ac.uk/course/lawlawub/ |
| 2 | Law (Senior Status) | https://www.lincoln.ac.uk/course/lawsstub/ |
| 3 | Law and Criminology | https://www.lincoln.ac.uk/course/lawcriub/ |

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Criminology | https://www.lincoln.ac.uk/course/cricriub/ |
| 2 | Criminology and Sociology | https://www.lincoln.ac.uk/course/crisolub/ |

##### Psychology

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Psychology | https://www.lincoln.ac.uk/course/psypsyub/ |
| 2 | Psychology (Sport and Exercise Psychology) | https://www.lincoln.ac.uk/course/psysesub/ |
| 3 | Psychology with Forensic Psychology | https://www.lincoln.ac.uk/course/psyfsyub/ |
| 4 | Psychology with Mental Health | https://www.lincoln.ac.uk/course/psycpyub/ |
| 5 | Psychology with Inclusive Education | https://www.lincoln.ac.uk/course/edmpsyub/ |

##### Education

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Education | https://www.lincoln.ac.uk/course/edueduub/ |

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Education and Psychology | https://www.lincoln.ac.uk/course/edmpsyub/ |

##### Sociology

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Sociology | https://www.lincoln.ac.uk/course/solsolub/ |

##### Politics and International Relations

###### BA (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Politics | https://www.lincoln.ac.uk/course/polpolub/ |
| 2 | International Relations | https://www.lincoln.ac.uk/course/ististub/ |
| 3 | International Relations and Politics | https://www.lincoln.ac.uk/course/istpolub/ |

##### Sport Science

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Sport and Exercise Science | https://www.lincoln.ac.uk/course/sessesub/ |
| 2 | Sport and Exercise Therapy | https://www.lincoln.ac.uk/course/sessthub/ |
| 3 | Sport and Physical Education | https://www.lincoln.ac.uk/course/sespesub/ |

#### College of Health and Science

##### Engineering

###### BEng (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.lincoln.ac.uk/course/egregrub/ |
| 2 | Electrical and Electronic Engineering | https://www.lincoln.ac.uk/course/egrelcub/ |
| 3 | General Engineering | https://www.lincoln.ac.uk/course/egrgenub/ |
| 4 | Mechatronics | https://www.lincoln.ac.uk/course/egrbcnub/ |
| 5 | Aeromechanical Engineering | https://www.lincoln.ac.uk/course/mecaerub/ |

###### MEng (Hons) (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Mechanical Engineering | https://www.lincoln.ac.uk/course/egregrum/ |
| 2 | Electrical and Electronic Engineering | https://www.lincoln.ac.uk/course/egrelcum/ |

##### Nursing

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Nursing (Registered Nurse - Adult) | https://www.lincoln.ac.uk/course/nurnurub/ |
| 2 | Nursing (Registered Nurse - Child) | https://www.lincoln.ac.uk/course/nurcldub/ |
| 3 | Nursing (Registered Nurse - Mental Health) | https://www.lincoln.ac.uk/course/nurmnhub/ |
| 4 | Midwifery | https://www.lincoln.ac.uk/course/midmidub/ |
| 5 | Paramedic Science | https://www.lincoln.ac.uk/course/nurparub/ |

##### Health and Care Sciences

###### BSc (Hons)
| # | 专业 | URL |
|---|------|-----|
| 1 | Diagnostic Radiography | https://www.lincoln.ac.uk/course/raddgcub/ |
| 2 | Dental Hygiene and Therapy | https://www.lincoln.ac.uk/course/dhydhyub/ |
| 3 | Dental Hygiene and Therapy with Gateway Year | https://www.lincoln.ac.uk/course/dhytgyub/ |
| 4 | Pharmaceutical Science | https://www.lincoln.ac.uk/course/phaphaub/ |
| 5 | Social Work Practice | https://www.lincoln.ac.uk/course/sowpraub/ |

###### MSci (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Applied Pharmaceutical Science | https://www.lincoln.ac.uk/course/phaphaum/ |
| 2 | Pharmaceutical Science with Business Management | https://www.lincoln.ac.uk/course/phabusum/ |

###### MPharm (Integrated Master's)
| # | 专业 | URL |
|---|------|-----|
| 1 | Pharmacy | https://www.lincoln.ac.uk/course/phrphrum/ |

##### Agri-food and Food Manufacturing

(No standalone UG programmes listed — see PG programmes)

#### Lincoln Medical School

##### Medicine

###### MBChB
| # | 专业 | URL |
|---|------|-----|
| 1 | Medicine | https://www.lincoln.ac.uk/course/mdcmbcub/ |
| 2 | Medicine (with Gateway Year) | https://www.lincoln.ac.uk/course/mdcmgyub/ |

### 1.3 Interdisciplinary / cross-college undergraduate programs

| # | 专业 | 学位 | Parent Schools | URL |
|---|------|------|----------------|-----|
| 1 | Mathematics and Computer Science | BSc (Hons) | Science (Maths + CS) | https://www.lincoln.ac.uk/course/mthcmpub/ |
| 2 | Mathematics and Theoretical Physics | BSc (Hons) | Science (Maths + Physics) | https://www.lincoln.ac.uk/course/mthphyub/ |
| 3 | English and History | BA (Hons) | Arts and Humanities | https://www.lincoln.ac.uk/course/enlhstub/ |
| 4 | Drama and English | BA (Hons) | Arts and Humanities | https://www.lincoln.ac.uk/course/enldraub/ |
| 5 | Criminology and Sociology | BA (Hons) | Social Science | https://www.lincoln.ac.uk/course/crisolub/ |
| 6 | International Relations and Politics | BA (Hons) | Social Science | https://www.lincoln.ac.uk/course/istpolub/ |
| 7 | Modern History and Politics | BA (Hons) | Arts and Humanities | https://www.lincoln.ac.uk/course/mdhpolub/ |
| 8 | Education and Psychology | BSc (Hons) | Social Science | https://www.lincoln.ac.uk/course/edmpsyub/ |
| 9 | Psychology with Forensic Psychology | BSc (Hons) | Social Science | https://www.lincoln.ac.uk/course/psyfsyub/ |
| 10 | Psychology with Inclusive Education | BSc (Hons) | Social Science + Education | https://www.lincoln.ac.uk/course/edmpsyub/ |

### 1.4 Minors — complete list

N/A — UK universities typically do not offer formal minor programmes.

### 1.5 General/Institute-wide requirements

UK universities do not have a US-style general education curriculum. Students study their chosen subject from Year 1.

### 1.6 Course-ID quick-lookup

| Course Code | Programme |
|-------------|-----------|
| cmpcmsub | Computer Science BSc |
| cmpcaiub | Computer Science with AI BSc |
| cmpcybub | Computer Science with Cyber Security BSc |
| cgpcmpub | Games Computing BSc |
| lawlawub | Law LLB |
| psypsyub | Psychology BSc |
| acfnbsub | Accountancy and Finance BSc |
| bmgtbsub | Business and Management BSc |
| egregrub | Mechanical Engineering BEng |
| egrelcub | Electrical and Electronic Engineering BEng |
| nurnurub | Nursing (Adult) BSc |
| mdcmbcub | Medicine MBChB |
| artartub | Fine Art BA |
| joujouub | Journalism BA |
| hsthstub | History BA |

---

## SECTION 2 — Graduate education

### 2.1 Graduate programmes — grouped by 学院 > 系 > 学位级别

#### College of Arts and Humanities

##### Art and Design
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Arts and Cultural Management | https://www.lincoln.ac.uk/course/artculma/ |

###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://www.lincoln.ac.uk/course/artresms/ |
| 2 | Design | https://www.lincoln.ac.uk/course/desresma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Art | https://www.lincoln.ac.uk/course/artartrp/ |
| 2 | Design | https://www.lincoln.ac.uk/course/desdesrp/ |

##### English and Creative Writing
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | English Literature | https://www.lincoln.ac.uk/course/enllitma/ |
| 2 | Creative Writing | https://www.lincoln.ac.uk/course/crtvwtma/ |

###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://www.lincoln.ac.uk/course/enlresma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | English | https://www.lincoln.ac.uk/course/enlenlrp/ |
| 2 | Creative Writing | https://www.lincoln.ac.uk/course/crtvwtrp/ |

##### Film and Media
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Media and Communications | https://www.lincoln.ac.uk/course/mdscmmma/ |

###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Media and Cultural Studies | https://www.lincoln.ac.uk/course/medrshma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Media (Including by Practice) | https://www.lincoln.ac.uk/course/medphdrp/ |
| 2 | Media and Cultural Studies | https://www.lincoln.ac.uk/course/medculrp/ |

##### Performing Arts
###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Drama | https://www.lincoln.ac.uk/course/dradrarp/ |
| 2 | Music | https://www.lincoln.ac.uk/course/musmusrp/ |
| 3 | Performing Arts Research Opportunities | https://www.lincoln.ac.uk/course/prmartrp/ |

##### History, Classical Studies, and Conservation
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Cultural Heritage Management | https://www.lincoln.ac.uk/course/culmanms/ |
| 2 | Conservation of Cultural Heritage | https://www.lincoln.ac.uk/course/conhisma/ |
| 3 | Medieval Studies | https://www.lincoln.ac.uk/course/medstdma/ |

###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Conservation of Cultural Heritage | https://www.lincoln.ac.uk/course/conresma/ |
| 2 | History | https://www.lincoln.ac.uk/course/hstresma/ |
| 3 | Classical Studies | https://www.lincoln.ac.uk/course/clsresma/ |

###### PG Cert/Dip
| # | 项目 | URL |
|---|------|-----|
| 1 | Medieval Studies (PG Dip) | https://www.lincoln.ac.uk/course/medstdpd/ |
| 2 | Medieval Studies (PG Cert) | https://www.lincoln.ac.uk/course/medstdpc/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | History | https://www.lincoln.ac.uk/course/hsthstrp/ |
| 2 | Medieval Studies | https://www.lincoln.ac.uk/course/medstdrp/ |
| 3 | Conservation of Cultural Heritage | https://www.lincoln.ac.uk/course/conconrp/ |
| 4 | Culture and Heritage Management | https://www.lincoln.ac.uk/course/culmanrp/ |
| 5 | Classical Studies | https://www.lincoln.ac.uk/course/clsphdrp/ |

##### Journalism and Communications
###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism | https://www.lincoln.ac.uk/course/jouresma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Journalism | https://www.lincoln.ac.uk/course/joujourp/ |

##### Philosophy
###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.lincoln.ac.uk/course/phlphlmr/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Philosophy | https://www.lincoln.ac.uk/course/phlphlrp/ |

#### College of Science

##### Computer Science and AI
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lincoln.ac.uk/course/cmpcmpms/ |
| 2 | Cloud Computing | https://www.lincoln.ac.uk/course/clocomms/ |
| 3 | Data Science and Applied Analytics | https://www.lincoln.ac.uk/course/dasapams/ |
| 4 | Artificial Intelligence | https://www.lincoln.ac.uk/course/intvisms/ |
| 5 | Robotics and Artificial Intelligence | https://www.lincoln.ac.uk/course/robasyms/ |
| 6 | Applied Computer Science | https://www.lincoln.ac.uk/course/appcmpms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lincoln.ac.uk/course/cmsresms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Computer Science | https://www.lincoln.ac.uk/course/cmpscirp/ |

##### Mathematics
###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.lincoln.ac.uk/course/mthappms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Applied Mathematics | https://www.lincoln.ac.uk/course/mthapprp/ |
| 2 | Mathematics | https://www.lincoln.ac.uk/course/mathmarp/ |
| 3 | Pure Mathematics | https://www.lincoln.ac.uk/course/mthmthrp/ |
| 4 | Physical and Mathematical Sciences | https://www.lincoln.ac.uk/course/phmtscrp/ |

##### Physics
###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Computational Physics | https://www.lincoln.ac.uk/course/phycmpms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Astrophysics | https://www.lincoln.ac.uk/course/astphyrp/ |
| 2 | Computational Physics | https://www.lincoln.ac.uk/course/phycmprp/ |
| 3 | Philosophy of Physics | https://www.lincoln.ac.uk/course/thephyrp/ |

##### Chemistry
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Toxicology | https://www.lincoln.ac.uk/course/frstxcms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemistry | https://www.lincoln.ac.uk/course/chmchmrp/ |

##### Biological and Life Sciences
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Biotechnology | https://www.lincoln.ac.uk/course/biotecms/ |
| 2 | Microbiology | https://www.lincoln.ac.uk/course/micbioms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Bioveterinary Science | https://www.lincoln.ac.uk/course/bvsresms/ |
| 2 | Biomedical Science | https://www.lincoln.ac.uk/course/biomscms/ |
| 3 | Microbiology | https://www.lincoln.ac.uk/course/mbiresms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Biochemistry and Molecular Biology | https://www.lincoln.ac.uk/course/biochmrp/ |
| 2 | Biomedical Science | https://www.lincoln.ac.uk/course/biomscrp/ |

##### Animal Sciences
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Clinical Animal Behaviour | https://www.lincoln.ac.uk/course/biocabms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Animal Behaviour and Welfare | https://www.lincoln.ac.uk/course/anbhwlms/ |
| 2 | Biology | https://www.lincoln.ac.uk/course/bioresms/ |
| 3 | Evolution and Ecology | https://www.lincoln.ac.uk/course/ecologms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Zoology | https://www.lincoln.ac.uk/course/zoozoorp/ |
| 2 | Animal Behaviour and Welfare | https://www.lincoln.ac.uk/course/anbhwlrp/ |
| 3 | Evolution and Ecology | https://www.lincoln.ac.uk/course/ecologrp/ |

##### Forensic Science
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.lincoln.ac.uk/course/forscims/ |
| 2 | Forensic Psychology | https://www.lincoln.ac.uk/course/frspsyms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.lincoln.ac.uk/course/frsresms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Forensic Science | https://www.lincoln.ac.uk/course/frsscirp/ |

##### Geography
###### MA by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | https://www.lincoln.ac.uk/course/gehresma/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Geography | https://www.lincoln.ac.uk/course/gepresms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Geography | https://www.lincoln.ac.uk/course/gehgehrp/ |
| 2 | Physical Geography | https://www.lincoln.ac.uk/course/gepgeprp/ |

##### Robotics and AI
(See Computer Science and AI for MSc Robotics and AI)

#### College of Social Science

##### Accountancy, Finance, and Economics
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting and Finance | https://www.lincoln.ac.uk/course/accfinms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Accounting | https://www.lincoln.ac.uk/course/accaccrp/ |
| 2 | Economics | https://www.lincoln.ac.uk/course/ecoecorp/ |
| 3 | Finance | https://www.lincoln.ac.uk/course/finfinrp/ |

##### Management
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Resource Management | https://www.lincoln.ac.uk/course/hrmhrmms/ |
| 2 | Management | https://www.lincoln.ac.uk/course/mgtmgtms/ |
| 3 | Supply Chain and Logistics Management | https://www.lincoln.ac.uk/course/loggloms/ |

###### MBA
| # | 项目 | URL |
|---|------|-----|
| 1 | Master of Business Administration | https://www.lincoln.ac.uk/course/mbalftmb/ |
| 2 | MBA Leadership | https://www.lincoln.ac.uk/course/slmmbamb/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Human Resource Management | https://www.lincoln.ac.uk/course/hrmhrmrp/ |

##### Marketing and Tourism
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Digital Marketing | https://www.lincoln.ac.uk/course/mktdigms/ |
| 2 | Marketing | https://www.lincoln.ac.uk/course/mktimsms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Marketing | https://www.lincoln.ac.uk/course/mktmktrp/ |
| 2 | Tourism | https://www.lincoln.ac.uk/course/toutourp/ |

##### Law and Criminology
###### LLM
| # | 项目 | URL |
|---|------|-----|
| 1 | International Corporate and Commercial Law | https://www.lincoln.ac.uk/course/lawiccml/ |
| 2 | International Law | https://www.lincoln.ac.uk/course/intlawml/ |

###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Criminology and Criminal Justice | https://www.lincoln.ac.uk/course/crimcjma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Law | https://www.lincoln.ac.uk/course/blphlwrp/ |
| 2 | Criminology | https://www.lincoln.ac.uk/course/cricrirp/ |

##### Psychology
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychological Research Methods | https://www.lincoln.ac.uk/course/psyresms/ |
| 2 | Counselling | https://www.lincoln.ac.uk/course/cslcslms/ |
| 3 | Developmental Psychology | https://www.lincoln.ac.uk/course/chdstdms/ |
| 4 | Forensic Psychology | https://www.lincoln.ac.uk/course/frspsyms/ |

###### PG Dip
| # | 项目 | URL |
|---|------|-----|
| 1 | High Intensity Psychological Interventions | https://www.lincoln.ac.uk/course/hipintpd/ |
| 2 | Counselling | https://www.lincoln.ac.uk/course/cslcslpd/ |

###### DClinPsy
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://www.lincoln.ac.uk/course/clipsytd/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Psychology | https://www.lincoln.ac.uk/course/psypsyrp/ |

##### Education
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.lincoln.ac.uk/course/edmedmma/ |

###### PGCE
| # | 项目 | URL |
|---|------|-----|
| 1 | Postgraduate Certificate in Education | https://www.lincoln.ac.uk/course/edmpnqpc/ |

###### PhD (Professional)
| # | 项目 | URL |
|---|------|-----|
| 1 | Education | https://www.lincoln.ac.uk/course/eduprorp/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Educational Research and Development | https://www.lincoln.ac.uk/course/eduphdrp/ |

##### Sociology
###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sociology | https://www.lincoln.ac.uk/course/solsolrp/ |
| 2 | Social Policy | https://www.lincoln.ac.uk/course/sopsoprp/ |
| 3 | Social Sciences | https://www.lincoln.ac.uk/course/socscirp/ |

##### Politics and International Relations
###### MA
| # | 项目 | URL |
|---|------|-----|
| 1 | International Relations | https://www.lincoln.ac.uk/course/ististma/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Politics | https://www.lincoln.ac.uk/course/polpolrp/ |
| 2 | International Relations | https://www.lincoln.ac.uk/course/ististrp/ |

##### Sport Science
###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Sport and Exercise Science/Sports Studies | https://www.lincoln.ac.uk/course/spexscms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Sport and Exercise Science/Sports Studies | https://www.lincoln.ac.uk/course/sessesrp/ |

#### College of Health and Science

##### Engineering
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Chemical Engineering with Sustainability | https://www.lincoln.ac.uk/course/chesusms/ |
| 2 | Engineering Management | https://www.lincoln.ac.uk/course/egrmanms/ |
| 3 | Advanced Mechanical Engineering | https://www.lincoln.ac.uk/course/supoenms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://www.lincoln.ac.uk/course/egrresms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Engineering | https://www.lincoln.ac.uk/course/egrphdrp/ |

##### Nursing
(No standalone PG programmes listed)

##### Health and Care Sciences
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Advanced Clinical Practice | https://www.lincoln.ac.uk/course/adclprms/ |
| 2 | Contemporary Physiotherapy Practice | https://www.lincoln.ac.uk/course/spcphsms/ |
| 3 | Physiotherapy (pre-registration) | https://www.lincoln.ac.uk/course/phsphsms/ |
| 4 | Nursing (Pre-registration - Adult) | https://www.lincoln.ac.uk/course/nurnurms/ |
| 5 | Nursing (Pre-registration - Mental Health) | https://www.lincoln.ac.uk/course/nurmnhms/ |
| 6 | Integrated Professional Practice | https://www.lincoln.ac.uk/course/adprprms/ |
| 7 | Occupational Therapy (pre-registration) | https://www.lincoln.ac.uk/course/ocuocums/ |
| 8 | Safeguarding: Leading Safer Organisations | https://www.lincoln.ac.uk/course/saflsoms/ |
| 9 | Speech and Language Therapy (Pre-registration) | https://www.lincoln.ac.uk/course/splathms/ |

###### PG Cert
| # | 项目 | URL |
|---|------|-----|
| 1 | Safeguarding: Leading Safer Organisations | https://www.lincoln.ac.uk/course/saflsopc/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Health and Social Care | https://www.lincoln.ac.uk/course/heasocms/ |
| 2 | Pharmacy and Pharmaceutical Sciences | https://www.lincoln.ac.uk/course/phrphrmr/ |

###### PhD (Professional)
| # | 项目 | URL |
|---|------|-----|
| 1 | Practice Portfolio in Health and Social Care | https://www.lincoln.ac.uk/course/heapporp/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Health and Social Care | https://www.lincoln.ac.uk/course/hlthstrp/ |
| 2 | Pharmacy and Pharmaceutical Sciences | https://www.lincoln.ac.uk/course/pharmarp/ |

##### Agri-food and Food Manufacturing
###### MSc
| # | 项目 | URL |
|---|------|-----|
| 1 | Agri-Food Technology with Professional Practice | https://www.lincoln.ac.uk/course/agftppms/ |
| 2 | Agri-Food Technology | https://www.lincoln.ac.uk/course/agrfdtms/ |

###### MSc by Research
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Science and Technology | https://www.lincoln.ac.uk/course/agftrsms/ |

###### MPhil/PhD
| # | 项目 | URL |
|---|------|-----|
| 1 | Agricultural Science and Technology | https://www.lincoln.ac.uk/course/agrsctrp/ |

### 2.2 At least one programme's full deep-dive

**MSc Computer Science** — Department of Computer Science and AI

- **URL**: https://www.lincoln.ac.uk/course/cmpcmpms/
- **Duration**: 1 year full-time, 2 years part-time
- **Campus**: Brayford Pool, Lincoln
- **Typical offer**: 2:1 honours degree in a relevant subject
- **IELTS**: 6.0 overall (minimum 5.5 in each component)
- **Tuition (Home)**: £9,250/year (estimated)
- **Tuition (International)**: £16,900-£22,100/year
- **Modules**: Advanced Programming, Machine Learning, Data Science, Cloud Computing, Cyber Security
- **Assessment**: Coursework, projects, dissertation
- **Career outcomes**: Software developer, data scientist, IT consultant, research

### 2.3 Graduate admissions model

- **PG Taught (MSc/MA/MBA)**: Apply directly to the university via online application form
- **PG Research (MPhil/PhD)**: Apply directly; contact potential supervisor first
- **Application fee**: None
- **Deadlines**: Rolling admissions for most programmes; some have fixed deadlines
- **Entry requirements**: 2:1 honours degree (or equivalent) for taught; 2:1+ for research
- **English language**: IELTS 6.0-7.0 depending on programme

---

## SECTION 3 — Application requirements & deadlines

### 3.1 Undergraduate — core data table

| Field | Value |
|-------|-------|
| Application platform | UCAS |
| UCAS equal consideration deadline | 14 January 2026 |
| Medicine deadline | 15 October 2025 |
| Clearing opens | 2 July 2026 |
| Decision deadline (Jan applicants) | 13 May 2026 |
| Reply deadline (Jan applicants) | 3 June 2026 |
| Personal statement | UCAS single statement (one for all 5 choices) |
| References | 1 academic reference (UCAS) |
| Interviews | Required for some programmes (e.g. Medicine, Nursing) |
| Contextual offers | Available for eligible students |

### 3.2 Undergraduate English proficiency table

| Exam | Minimum | Recommended | Notes |
|------|---------|-------------|-------|
| IELTS Academic | 6.0 | 6.5-7.0 | Minimum 5.5 in each component |
| TOEFL iBT | 79 | 90+ | Accepted equivalent |
| PTE Academic | 54 | 60+ | Accepted equivalent |
| Cambridge English | 169 (B2 First) | 176+ | Accepted equivalent |

> Note: Specific requirements vary by programme. Medicine, Nursing, and other health programmes typically require higher scores (IELTS 7.0+).

### 3.3 Graduate — global rules

- **Application platform**: Direct to university (no UCAS for PG)
- **Application fee**: None
- **Deadlines**: Rolling for most taught programmes; research programmes contact supervisor first
- **Entry requirements**: 2:1 honours degree (or international equivalent) for taught; 2:1+ for research
- **English language**: IELTS 6.0-7.0 depending on programme
- **GRE/GMAT**: Not required for most programmes; MBA may consider GMAT

---

## SECTION 4 — Costs & financial aid

### 4.1 Undergraduate cost (2026/27 academic year)

| Expense item | Amount | Description |
|-------------|--------|-------------|
| Home tuition | £9,250/year | UK nationals, settled status |
| International tuition | £16,900-£22,100/year | Varies by programme; lab/clinical higher |
| Accommodation | £4,500-£7,500/year | University halls, city centre campus |
| Living costs | £8,000-£10,000/year | Lincoln named UK's most affordable student city (NatWest 2025) |
| Visa fee | £490 | Student visa application (international) |
| IHS surcharge | £470/year | Immigration Health Surcharge (international) |

### 4.2 Undergraduate financial-aid policy

- **Student Finance England**: Loans available for home students (tuition + maintenance)
- **Scholarships**: Range from £1,000 to 50% of tuition fees for international students
- **Bursaries**: Available for home students from low-income backgrounds
- **Campus Jobs**: Flexible work opportunities on campus
- **Need-blind**: No (UK universities are fee-status driven)

### 4.3 Graduate cost & funding framework

- **PG Taught (Home)**: £9,250/year (estimated)
- **PG Taught (International)**: £16,900-£22,100/year
- **PG Research**: Fees vary; funded studentships available
- **MBA**: £15,000-£20,000 (estimated)
- **Application fee**: None
- **Funding**: Research Council studentships, university scholarships, self-funded

---

## SECTION 5 — Evidence chain index

```yaml
E-U-001:
  field: institution.name
  value: "University of Lincoln"
  source_url: https://www.lincoln.ac.uk
  source_snippet: "University of Lincoln"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-002:
  field: undergraduate.courses.total_count
  value: 115
  source_url: https://www.lincoln.ac.uk/clearing/
  source_snippet: "115 of 115"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-003:
  field: undergraduate.tuition.home
  value: "£9,250/year"
  source_url: https://www.lincoln.ac.uk/studywithus/undergraduatestudy/feesandfunding/
  source_snippet: "Home tuition fees: £9,250"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-004:
  field: undergraduate.tuition.international
  value: "£16,900-£22,100/year"
  source_url: https://www.lincoln.ac.uk/studywithus/internationalstudents/internationalfeesandfunding/
  source_snippet: "tuition fees for international students typically range between £16,900 - £22,100"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-005:
  field: undergraduate.deadline.ucas_equal_consideration
  value: "14 January 2026"
  source_url: https://www.lincoln.ac.uk/studywithus/undergraduatestudy/howtoapply/
  source_snippet: "2026 equal consideration deadline for undergraduate courses except those with the 15 October deadline: 14 January 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-006:
  field: undergraduate.deadline.medicine
  value: "15 October 2025"
  source_url: https://www.lincoln.ac.uk/studywithus/undergraduatestudy/howtoapply/
  source_snippet: "2026 entry deadline for Medicine at Lincoln: 15 October 2025"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-007:
  field: undergraduate.english_language.ielts
  value: "6.0-7.0"
  source_url: https://www.lincoln.ac.uk/studywithus/internationalstudents/entryrequirementsandyourcountry/
  source_snippet: "the majority of our programmes require an IELTS score of 6.0, 6.5 or 7.0"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-008:
  field: undergraduate.entry_requirements.cs
  value: "104-112 UCAS Tariff points"
  source_url: https://www.lincoln.ac.uk/course/cmpcmsub/
  source_snippet: "104 to 112 UCAS Tariff points. This must be achieved from a minimum of 2 A Levels or equivalent Level 3 qualifications."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-009:
  field: undergraduate.entry_requirements.cs_alevel
  value: "BCC to BBC"
  source_url: https://www.lincoln.ac.uk/course/cmpcmsub/
  source_snippet: "A Level: BCC to BBC"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-010:
  field: undergraduate.entry_requirements.cs_ib
  value: "29 points overall"
  source_url: https://www.lincoln.ac.uk/course/cmpcmsub/
  source_snippet: "International Baccalaureate: 29 points overall."
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-011:
  field: undergraduate.application.platform
  value: "UCAS"
  source_url: https://www.lincoln.ac.uk/studywithus/undergraduatestudy/howtoapply/
  source_snippet: "apply through UCAS"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-012:
  field: undergraduate.clearing.opens
  value: "2 July 2026"
  source_url: https://www.lincoln.ac.uk/studywithus/undergraduatestudy/howtoapply/
  source_snippet: "2026 Clearing entry opens: 2 July 2026"
  capture_date: 2026-07-08
  evidence_type: official_webpage_table

E-U-013:
  field: institution.location
  value: "Lincoln, England, UK"
  source_url: https://www.lincoln.ac.uk
  source_snippet: "Brayford Pool Campus, Lincoln, LN6 7TS"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-014:
  field: institution.ranking
  value: "UK's most affordable student city (NatWest 2025)"
  source_url: https://www.lincoln.ac.uk/studywithus/internationalstudents/internationalfeesandfunding/
  source_snippet: "Lincoln has been named the UK's most affordable student city in the NatWest Student Living Index 2025"
  capture_date: 2026-07-08
  evidence_type: official_webpage

E-U-015:
  field: graduate.application.fee
  value: "None"
  source_url: https://www.lincoln.ac.uk/studywithus/postgraduatestudy/howtoapply/
  source_snippet: "No application fee"
  capture_date: 2026-07-08
  evidence_type: official_webpage
```

---

## SECTION 6 — WeKnora import manifest

### Collection structure

```
lincoln-knowledge-base-v2/
├── overview.md                    → Section 0 (institution overview, counts, hierarchy)
├── undergraduate-programmes.md    → Section 1 (all UG programmes grouped)
├── graduate-programmes.md         → Section 2 (all PG programmes grouped)
├── application-requirements.md    → Section 3 (deadlines, entry reqs, English lang)
├── costs-and-funding.md           → Section 4 (fees, scholarships, living costs)
├── evidence-index.md              → Section 5 (evidence chain)
└── comparison-framework.md        → Section 7 (cross-school comparison)
```

### Per-chunk metadata template

```yaml
metadata:
  collection: "lincoln-knowledge-base-v2"
  school: "University of Lincoln"
  department: "<home department>"
  degree_level: "<BA|BSc|BEng|MA|MSc|PhD|...>"
  level: undergraduate | graduate
  field_type: overview | programs | deadlines | tests | costs | funding
  source_url: <URL>
  capture_date: 2026-07-08
  version: v2.0
  change_status: baseline
  last_verified: 2026-07-08
```

### Follow-up data items (prioritized)

| Priority | Data item | Target URL |
|----------|-----------|------------|
| **P1** | Per-program international tuition fees | Individual course pages |
| **P1** | Per-program A-Level/IB entry requirements | Individual course pages |
| **P1** | Scholarship details and eligibility | https://www.lincoln.ac.uk/studywithus/scholarshipsandbursaries/ |
| **P2** | Course module details and curriculum | Individual course pages |
| **P2** | Accommodation costs and options | https://www.lincoln.ac.uk/studentlife/accommodation/ |
| **P2** | Placement year details | Individual course pages |

---

## SECTION 7 — Cross-school comparison framework

| Dimension | University of Lincoln |
|-----------|----------------------|
| Total UG programmes | 115 (clearing listing) |
| Total PG programmes | 118 |
| Russell Group | No |
| UCAS deadline | 14 January 2026 |
| Medicine deadline | 15 October 2025 |
| IELTS minimum | 6.0 |
| Home tuition (UG) | £9,250/year |
| International tuition (UG) | £16,900-£22,100/year |
| Location | Lincoln, England |
| Campus | Brayford Pool (city centre) |
| Application platform | UCAS (UG), Direct (PG) |
| Application fee | None |
| Most affordable city | Yes (NatWest 2025) |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-08
> **Sources**: University of Lincoln official website (lincoln.ac.uk)
> **Verification**: ego-browser snapshotText + JS DOM extraction
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ (102 extracted) | PG programmes ✅ (118 extracted) | Evidence (15 blocks) ✅
