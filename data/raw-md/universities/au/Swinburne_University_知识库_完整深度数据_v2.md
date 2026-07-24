# Swinburne University of Technology 知识库_完整深度数据_v2

> **Data capture date**: 2026-07-10
> **Capture tool**: browser_navigate + browser_snapshot + curl
> **Target knowledge base**: WeKnora
> **Granularity**: school → department → degree-level → program
> **Document version**: v2.0 (deep)
> **Region**: Australia (AU) — Melbourne, Victoria
> **CRICOS**: 00111D
> **RTO**: 3059
> **TEQSA**: PRV12148 Australian University

---

## Section 0 — 院校总览 (Institution overview)

### 0.1 专业与项目总数 (Rule 1 — counts)

| 维度 | 数量 |
|------|------|
| 本科 (UG) 学位项目 | 119 |
| 研究生授课型 (PGT) | 90 |
| 研究型 (Research / PhD / MRes) | 45 |
| TAFE / Vocational | 108 |
| Short courses | 64 |
| 桥梁/Pathway 项目 | 18 |
| Inbound/Exchange | 4 |
| **学位项目总计 (unique base)** | **448** |
| 含细分方向的完整课程URL | **726** |
| 高等教育学院 (Schools) | 6 |
| 职业教育系 (Departments) | 5 |
| 研究机构 (Research Institutes) | 4 |
| 校区 | 3 (Hawthorn, Croydon, Wantirna) |

### 0.2 学院 / 系层级结构 (Rule 2 — hierarchy)

```
Swinburne University of Technology
├── Higher Education Schools
│   ├── School of Business, Law and Entrepreneurship
│   │   ├── Business disciplines (Accounting, Finance, Marketing, HR, Management, etc.)
│   │   ├── Law (LLB, combined law degrees)
│   │   └── Entrepreneurship & Innovation
│   ├── School of Design and Architecture
│   │   ├── Design (Communication, UX/Interaction, Motion, Photomedia, Branded Environments)
│   │   ├── Architecture & Interior Architecture
│   │   ├── Industrial Design
│   │   ├── Film, Television & Animation
│   │   ├── Games & Interactivity
│   │   └── Fashion Design
│   ├── School of Engineering
│   │   ├── Civil Engineering
│   │   ├── Mechanical Engineering
│   │   ├── Electrical & Electronic Engineering
│   │   ├── Robotics & Mechatronics
│   │   ├── Software Engineering
│   │   ├── Biomedical Engineering
│   │   ├── Architectural Engineering
│   │   ├── Product Design Engineering
│   │   └── Digital Construction Management
│   ├── School of Health Sciences
│   │   ├── Nursing
│   │   ├── Biomedical Science
│   │   ├── Exercise & Sport Science
│   │   ├── Nutrition
│   │   ├── Health Science
│   │   ├── Occupational Therapy
│   │   ├── Physiotherapy
│   │   ├── Dietetics
│   │   ├── Counselling
│   │   ├── Psychology & Psychological Sciences
│   │   └── Forensic Behavioural Science
│   ├── School of Science, Computing and Emerging Technologies
│   │   ├── Computer Science (AI, Cybersecurity, Data Science, Games Dev, IoT, Software Dev)
│   │   ├── Information & Communication Technology
│   │   ├── Data Science
│   │   ├── Cyber Security
│   │   ├── Aviation
│   │   ├── Science (Biochemistry, Biotechnology, Chemistry, Physics, Environmental, Space Tech, Astronomy)
│   │   └── Applied Artificial Intelligence
│   └── School of Social Sciences, Media, Film and Education
│       ├── Arts, Humanities & Social Sciences
│       ├── Media & Communication
│       ├── Screen Production
│       ├── Criminal Justice & Criminology
│       ├── Education (Early Childhood, Primary)
│       └── Writing
├── Vocational Education & Training (VET)
│   ├── Department of Business, Design, Media and ICT
│   ├── Department of Health, Science and Community
│   ├── Department of Trades and Engineering Technologies
│   ├── Knox Innovation, Opportunity and Sustainability Centre (KIOSC)
│   └── Swinburne Edge
├── Research Institutes
│   ├── Innovative Planet Research Institute
│   ├── Iverson Health Innovation Research Institute
│   ├── Social Innovation Research Institute
│   └── Space Technology and Industry Institute
└── Other Entities
    ├── Swinburne Online
    └── Swinburne College (ELICOS, Foundation, UniLink)
```

### 0.3 学历级别明细 (Rule 3 — degree-level inventory)

| 学历级别 | 数量 | 说明 |
|---------|------|------|
| Associate Degree | 3 | 应用AI、应用技术、工程、航空 |
| Bachelor Degree (BA, BSc, BEng, BBus, etc.) | ~90 | 本科单一学位 |
| Bachelor Degree (Double Degree) | ~29 | 双学位组合 (Law+Business, Engineering+Science, etc.) |
| Bachelor (Honours) | ~6 | 荣誉学士 (Psychology, CS, Design, Health Science) |
| Graduate Certificate | ~33 | 研究生证书 |
| Graduate Diploma | ~10 | 研究生文凭 |
| Master Degree (Coursework) | ~47 | 授课型硕士 |
| Master Degree (Research) | ~6 | 研究型硕士 |
| Doctor of Philosophy (PhD) | ~39 | 博士 |
| VET Certificate I-IV | ~30+ | 职业证书 |
| VET Diploma / Advanced Diploma | ~30+ | 职业文凭/高级文凭 |
| Short Courses | 64 | 短期课程 |
| Pathway (Foundation Year, UniLink) | 18 | 桥梁课程 |

### 0.4 分布矩阵 (Rule 4 — distribution cross-tab)

| 学院 | UG | PGT | Research | TAFE/VET | Total |
|------|----|-----|----------|----------|-------|
| School of Business, Law and Entrepreneurship | ~19 | ~30 | ~6 | - | ~55 |
| School of Design and Architecture | ~15 | ~3 | ~4 | - | ~22 |
| School of Engineering | ~9 | ~10 | ~3 | - | ~22 |
| School of Health Sciences | ~10 | ~12 | ~4 | - | ~26 |
| School of Science, Computing and Emerging Technologies | ~18 | ~12 | ~8 | - | ~38 |
| School of Social Sciences, Media, Film and Education | ~12 | ~7 | ~4 | - | ~23 |
| VET (跨系) | - | - | - | ~108 | ~108 |
| Short Courses | - | - | - | - | 64 |
| Pathway / Inbound | - | - | - | - | 22 |
| **Total** | **~83** | **~74** | **~29** | **~108** | **~448** |

> 注: 部分课程跨学院（如Applied Innovation双学位），分布矩阵为估算。职业教育课程（108）和短期课程（64）未按具体系部分配。

---

## Section 1 — Undergraduate education

### School of Business, Law and Entrepreneurship

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Bachelor of Accounting | BBus(Acc) | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-accounting/ |
| Bachelor of Accounting (Online) | BBus(Acc) | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-accounting-online/ |
| Bachelor of Accounting + Bachelor of Applied Innovation | BBus(Acc)/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-accounting-bachelor-of-applied-innovation/ |
| Bachelor of Artificial Intelligence in Business | BAI(Bus) | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-artificial-intelligence-in-business/ |
| Bachelor of Business | BBus | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business/ |
| Bachelor of Business (Online) | BBus | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-online/ |
| Bachelor of Business + Bachelor of Applied Innovation | BBus/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-bachelor-of-applied-innovation/ |
| Bachelor of Business Analytics | BBusAnalytics | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-analytics/ |
| Bachelor of Business Analytics + Bachelor of Applied Innovation | BBusAnalytics/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-analytics-bachelor-of-applied-innovation/ |
| Bachelor of Business Analytics + Bachelor of Business | BBusAnalytics/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-analytics-bachelor-of-business/ |
| Bachelor of Business Analytics + Bachelor of Cyber Security | BBusAnalytics/BCyberSec | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-analytics-bachelor-of-cyber-security/ |
| Bachelor of Business (Professional) | BBus(Prof) | Majors: Accounting, Business Admin, Business Analytics, Finance, HRM, Logistics, Management, Marketing, Sports Mgmt | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-business-professional/ |
| Bachelor of Laws | LLB | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws/ |
| Bachelor of Laws (Online) | LLB | - | Online | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-online/ |
| Bachelor of Laws + Bachelor of Arts | LLB/BA | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-arts/ |
| Bachelor of Laws + Bachelor of Business | LLB/BBus | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-business/ |
| Bachelor of Laws + Bachelor of Business Analytics | LLB/BBusAnalytics | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-business-analytics/ |
| Bachelor of Laws + Bachelor of Computer Science | LLB/BCompSci | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-computer-science/ |
| Bachelor of Laws + Bachelor of Criminal Justice and Criminology | LLB/BCrimJust | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-criminal-justice-and-criminology/ |
| Bachelor of Laws + Bachelor of Cyber Security | LLB/BCyberSec | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-cyber-security/ |
| Bachelor of Laws + Bachelor of Engineering (Honours) | LLB/BEng(Hons) | Double Degree | Hawthorn | 6 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-engineering-honours/ |
| Bachelor of Laws + Bachelor of Media and Communication | LLB/BMediaComm | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-media-and-communication/ |
| Bachelor of Laws + Bachelor of Psychological Sciences | LLB/BPsychSc | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-psychological-sciences/ |
| Bachelor of Laws + Bachelor of Science | LLB/BSc | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-laws-bachelor-of-science/ |

### School of Design and Architecture

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Bachelor of Animation | BAnim | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-animation/ |
| Bachelor of Animation + Bachelor of Applied Innovation | BAnim/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-animation-bachelor-of-applied-innovation/ |
| Bachelor of Design | BDes | Majors: Comm Design, UX/Interaction, Motion, Photomedia, Branded Environments | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design/ |
| Bachelor of Design + Bachelor of Applied Innovation | BDes/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-bachelor-of-applied-innovation/ |
| Bachelor of Design + Bachelor of Business | BDes/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-bachelor-of-business/ |
| Bachelor of Design + Bachelor of Media and Communication | BDes/BMediaComm | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-bachelor-of-media-and-communication/ |
| Bachelor of Design Architecture | BDesArch | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-architecture/ |
| Bachelor of Design (Communication Design) (Honours) | BDes(CommDes)(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-communication-design-honours/ |
| Bachelor of Design Fashion | BDesFashion | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-fashion/ |
| Bachelor of Design (Industrial Design) (Honours) | BDes(IndDes)(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-industrial-design-honours/ |
| Bachelor of Design (Interior Architecture) (Honours) | BDes(IntArch)(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-design-interior-architecture-honours/ |
| Bachelor of Games and Interactivity | BGI | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-games-and-interactivity/ |
| Bachelor of Games and Interactivity + Bachelor of Animation | BGI/BAnim | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-games-and-interactivity-bachelor-of-animation/ |
| Bachelor of Games and Interactivity + Bachelor of Applied Innovation | BGI/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-games-and-interactivity-bachelor-of-applied-innovation/ |
| Bachelor of Games and Interactivity + Bachelor of Computer Science | BGI/BCompSci | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-games-and-interactivity-bachelor-of-computer-science/ |
| Bachelor of Screen Production | BScrProd | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-screen-production/ |
| Bachelor of Screen Production + Bachelor of Applied Innovation | BScrProd/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-screen-production-bachelor-of-applied-innovation/ |
| Bachelor of Film and Television (Honours) | BFTV(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-film-and-television-honours/ |
| Bachelor of Digital Construction Management | BDigCM | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-digital-construction-management/ |
| Bachelor of Construction Management (Honours) | BCM(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-construction-management-honours/ |
| Bachelor of Construction Management (Honours) (Professional) | BCM(Hons)(Prof) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-construction-management-honours-professional/ |

### School of Engineering

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Associate Degree of Engineering | ADEng | Electrical | Hawthorn | 2 yrs | - | https://www.swinburne.edu.au/course/undergraduate/associate-degree-of-engineering/ |
| Bachelor of Engineering (Honours) | BEng(Hons) | Civil, Mechanical, Electrical & Electronic, Robotics & Mechatronics, Software, Biomedical, Architectural, Product Design | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours/ |
| Bachelor of Engineering (Honours) (Professional) | BEng(Hons)(Prof) | - | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-professional/ |
| Bachelor of Engineering Technology | BEngTech | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-technology/ |
| Bachelor of Engineering (Honours) + Bachelor of Applied Innovation | BEng(Hons)/BAppInnov | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-bachelor-of-applied-innovation/ |
| Bachelor of Engineering (Honours) + Bachelor of Arts | BEng(Hons)/BA | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-bachelor-of-arts/ |
| Bachelor of Engineering (Honours) + Bachelor of Business | BEng(Hons)/BBus | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-bachelor-of-business/ |
| Bachelor of Engineering (Honours) + Bachelor of Computer Science | BEng(Hons)/BCompSci | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-bachelor-of-computer-science/ |
| Bachelor of Engineering (Honours) + Bachelor of Science | BEng(Hons)/BSc | Double Degree | Hawthorn | 5 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-engineering-honours-bachelor-of-science/ |

### School of Health Sciences

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Bachelor of Biomedical Science | BBiomedSc | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-biomedical-science/ |
| Bachelor of Exercise and Sport Science | BExSS | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-exercise-and-sport-science/ |
| Bachelor of Health Science | BHealthSc | Majors: Health Service Mgmt, Health Economics | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science/ |
| Bachelor of Health Science (Professional) | BHealthSc(Prof) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-professional/ |
| Bachelor of Health Science (Honours) | BHealthSc(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-honours/ |
| Bachelor of Health Science + Bachelor of Applied Innovation | BHealthSc/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-bachelor-of-applied-innovation/ |
| Bachelor of Health Science + Bachelor of Arts | BHealthSc/BA | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-bachelor-of-arts/ |
| Bachelor of Health Science + Bachelor of Business | BHealthSc/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-bachelor-of-business/ |
| Bachelor of Health Science + Bachelor of Media and Communication | BHealthSc/BMediaComm | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-bachelor-of-media-and-communication/ |
| Bachelor of Health Science + Bachelor of Science | BHealthSc/BSc | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-health-science-bachelor-of-science/ |
| Bachelor of Nursing | BNurs | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-nursing/ |
| Bachelor of Nutrition | BNutr | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-nutrition/ |
| Bachelor of Psychological Sciences | BPsychSc | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychological-sciences/ |
| Bachelor of Psychological Sciences (Online) | BPsychSc | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychological-sciences-online/ |
| Bachelor of Psychological Sciences (Honours) | BPsychSc(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychological-sciences-honours/ |
| Bachelor of Psychology and Cognitive Neuroscience | BPsychCogNeuro | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychology-and-cognitive-neuroscience/ |
| Bachelor of Psychology (Honours) | BPsych(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychology-honours/ |
| Bachelor of Forensic Psychological Sciences | BForensPsychSc | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-forensic-psychological-sciences/ |
| Bachelor of Psychological Sciences + Bachelor of Criminal Justice and Criminology | BPsychSc/BCrimJust | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-psychological-sciences-bachelor-of-criminal-justice-and-criminology/ |

### School of Science, Computing and Emerging Technologies

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Associate Degree of Applied Artificial Intelligence | ADAppAI | Gen AI in Gaming/VFX, Cyber Security & Cloud | Hawthorn | 2 yrs | - | https://www.swinburne.edu.au/course/undergraduate/associate-degree-of-applied-artificial-intelligence/ |
| Associate Degree of Applied Technologies | ADAppTech | - | Hawthorn | 2 yrs | - | https://www.swinburne.edu.au/course/undergraduate/associate-degree-of-applied-technologies/ |
| Associate Degree of Aviation | ADAvn | - | Hawthorn | 2 yrs | - | https://www.swinburne.edu.au/course/undergraduate/associate-degree-of-aviation/ |
| Bachelor of Computer Science | BCompSci | AI, Cyber Security, Data Science, Games Dev, Software Dev, IoT | Hawthorn | 3 yrs | 70.0 | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science/ |
| Bachelor of Computer Science (Professional) | BCompSci(Prof) | AI, Cyber Security, Data Science, Games Dev, Software Dev, IoT | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science-professional/ |
| Bachelor of Computer Science (Honours) | BCompSci(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science-honours/ |
| Bachelor of Computer Science + Bachelor of Applied Innovation | BCompSci/BAppInnov | Cyber Security specialization | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science-bachelor-of-applied-innovation/ |
| Bachelor of Cyber Security | BCyberSec | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-cyber-security/ |
| Bachelor of Data Science | BDataSc | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-data-science/ |
| Bachelor of Information and Communication Technology | BICT | IT, Network Tech, Software Tech | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-information-and-communication-technology/ |
| Bachelor of ICT (Online) | BICT | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-information-and-communication-technology-online/ |
| Bachelor of ICT (Professional) | BICT(Prof) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-information-and-communication-technology-professional/ |
| Bachelor of ICT + Bachelor of Applied Innovation | BICT/BAppInnov | IT specialization | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-information-and-communication-technology-bachelor-of-applied-innovation/ |
| Bachelor of Science | BSc | Space Technology specialization | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-science/ |
| Bachelor of Science (Honours) | BSc(Hons) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-science-honours/ |
| Bachelor of Science (Professional) | BSc(Prof) | Biochemistry, Biotechnology, Applied Maths, Chemistry, Physics, Environmental Sci, Space Tech | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-science-professional/ |
| Bachelor of Science + Bachelor of Applied Innovation | BSc/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-science-bachelor-of-applied-innovation/ |
| Bachelor of Aviation | BAvn | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation/ |
| Bachelor of Aviation and Piloting | BAvnPilot | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation-and-piloting/ |
| Bachelor of Aviation Management | BAvnMgmt | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation-management/ |
| Bachelor of Aviation Management + Bachelor of Applied Innovation | BAvnMgmt/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation-management-bachelor-of-applied-innovation/ |
| Bachelor of Aviation Management (Professional) | BAvnMgmt(Prof) | Uncrewed Aircraft Systems, Aviation Operations | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation-management-professional/ |
| Bachelor of Aviation + Bachelor of Business | BAvn/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-aviation-bachelor-of-business/ |

### School of Social Sciences, Media, Film and Education

| Program Name | Degree Type | Major/Specialization | Campus | Duration | ATAR | URL |
|-------------|-------------|---------------------|--------|----------|------|-----|
| Bachelor of Arts | BA | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-arts/ |
| Bachelor of Arts + Bachelor of Applied Innovation | BA/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-arts-bachelor-of-applied-innovation/ |
| Bachelor of Arts + Bachelor of Business | BA/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-arts-bachelor-of-business/ |
| Bachelor of Arts + Bachelor of Psychological Sciences | BA/BPsychSc | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-arts-bachelor-of-psychological-sciences/ |
| Bachelor of Arts + Bachelor of Science | BA/BSc | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-arts-bachelor-of-science/ |
| Bachelor of Criminal Justice and Criminology | BCrimJust | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-criminal-justice-and-criminology/ |
| Bachelor of Criminal Justice and Criminology (Online) | BCrimJust | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-criminal-justice-and-criminology-online/ |
| Bachelor of Criminal Justice and Criminology + Bachelor of Applied Innovation | BCrimJust/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-criminal-justice-and-criminology-bachelor-of-applied-innovation/ |
| Bachelor of Criminal Justice and Criminology + Bachelor of Cyber Security | BCrimJust/BCyberSec | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-criminal-justice-and-criminology-bachelor-of-cyber-security/ |
| Bachelor of Education (Early Childhood and Primary) | BEd(ECPrim) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-early-childhood-and-primary/ |
| Bachelor of Education (Early Childhood Teaching) | BEd(ECT) | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-early-childhood-teaching/ |
| Bachelor of Education (Early Childhood Teaching) (Online) | BEd(ECT) | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-early-childhood-teaching-online/ |
| Bachelor of Education (Early Childhood and Primary Teaching) (Online) | BEd(ECPrim) | - | Online | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-early-childhood-primary-teaching-online/ |
| Bachelor of Education (Primary) | BEd(Prim) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-primary/ |
| Bachelor of Education (Primary Teaching) (Online) | BEd(Prim) | - | Online | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-primary-teaching-online/ |
| Bachelor of Education Studies | BEdStud | Primary Education, Early Childhood | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-education-studies/ |
| Bachelor of Media and Communication | BMediaComm | - | Hawthorn | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-media-and-communication/ |
| Bachelor of Media and Communication (Online) | BMediaComm | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-media-and-communication-online/ |
| Bachelor of Media and Communication (Professional) | BMediaComm(Prof) | - | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-media-and-communication-professional/ |
| Bachelor of Media and Communication + Bachelor of Applied Innovation | BMediaComm/BAppInnov | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-media-and-communication-bachelor-of-applied-innovation/ |
| Bachelor of Media and Communication + Bachelor of Business | BMediaComm/BBus | Double Degree | Hawthorn | 4 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-media-and-communication-bachelor-of-business/ |
| Bachelor of Social Science (Online) | BSocSc | - | Online | 3 yrs | - | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-social-science-online/ |

### Applied Innovation (跨学院项目)

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Bachelor of Applied Innovation | BAppInnov | Hawthorn | 3 yrs | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-applied-innovation/ |

> Applied Innovation is offered as a double degree component paired with most other bachelor degrees.

---

## Section 2 — Graduate education

### 2.1 Postgraduate Taught (PGT) — Coursework

#### School of Business, Law and Entrepreneurship

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate of Business Administration | GradCertBusAdm | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-business-administration/ |
| Graduate Certificate of Business Administration (Swinburne Online) | GradCertBusAdm | Online | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-business-administration-swinburne-online/ |
| Graduate Certificate of Business Information Systems | GradCertBIS | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-business-information-systems/ |
| Graduate Certificate of Entrepreneurship | GradCertEntrep | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-entrepreneurship/ |
| Graduate Certificate of Human Resource Management | GradCertHRM | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-human-resource-management/ |
| Graduate Certificate of Marketing | GradCertMktg | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-marketing/ |
| Graduate Certificate of Professional Accounting | GradCertProfAcc | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-professional-accounting/ |
| Graduate Certificate of Project Management | GradCertProjMgmt | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-project-management/ |
| Graduate Certificate of Project Management (Swinburne Online) | GradCertProjMgmt | Online | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-project-management-swinburne-online/ |
| Graduate Certificate of Social Impact | GradCertSocImp | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-social-impact/ |
| Graduate Certificate of Supply Chain Innovation | GradCertSCM | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-supply-chain-innovation/ |
| Graduate Certificate in Applied Business | GradCertAppBus | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-applied-business/ |
| Graduate Certificate in Construction Management | GradCertConstrMgmt | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-construction-management/ |
| Graduate Certificate in Organisational Coaching | GradCertOrgCoach | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-organisational-coaching/ |
| Graduate Diploma of Project Management (Swinburne Online) | GradDipProjMgmt | Online | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-project-management-swinburne-online/ |
| Graduate Diploma of Writing | GradDipWrit | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-writing/ |
| Master of Business Administration | MBA | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-business-administration/ |
| Master of Business Administration (Swinburne Online) | MBA | Online | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-business-administration-swinburne-online/ |
| Master of Business Information Systems | MBIS | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-business-information-systems/ |
| Master of Finance | MFin | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-finance/ |
| Master of Human Resource Management | MHRM | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-human-resource-management/ |
| Master of Marketing | MMktg | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-marketing/ |
| Master of Professional Accounting | MProfAcc | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-professional-accounting/ |
| Master of Project Management | MProjMgmt | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-project-management/ |
| Master of Social Impact | MSocImp | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-social-impact/ |
| Master of Supply Chain Innovation | MSCM | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-supply-chain-innovation/ |
| Master of Construction and Infrastructure Management | MCIM | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-construction-and-infrastructure-management/ |
| Master of Construction Management Practice | MCMP | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-construction-management-practice/ |

#### School of Design and Architecture

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate of Design | GradCertDes | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-design/ |
| Graduate Certificate of Writing | GradCertWrit | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-writing/ |
| Graduate Diploma of Writing | GradDipWrit | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-writing/ |
| Master of Architecture | MArch | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-architecture/ |
| Master of Architecture and Urban Design | MArchUrbDes | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-architecture-and-urban-design/ |
| Master of Design | MDes | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-design/ |
| Master of Writing | MWrit | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-writing/ |

#### School of Engineering

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate of Engineering | GradCertEng | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-engineering/ |
| Master of Engineering Practice | MEngPrac | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-engineering-practice/ |
| Master of Engineering Science | MEngSci | Hawthorn | 1-1.5 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-engineering-science/ |
| Master of Engineering Practice + Master of Construction Management Practice | MEngPrac/MCMP | Hawthorn | 2.5 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-engineering-practice-master-of-construction-management-practice/ |
| Master of Professional Engineering | MProfEng | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-professional-engineering/ |

#### School of Health Sciences

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate in Client Assessment and Case Management | GradCert | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-client-assessment-and-case-management/ |
| Graduate Certificate in Forensic Behavioural Science | GradCertForensBS | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-forensic-behavioural-science/ |
| Graduate Certificate in Forensic Mental Health Nursing | GradCertForensMHN | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-forensic-mental-health-nursing/ |
| Graduate Certificate of Counselling | GradCertCouns | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-counselling/ |
| Graduate Certificate of Forensic Psychiatric Practice | GradCertForensPsych | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-forensic-psychiatric-practice/ |
| Graduate Certificate of Psychology (Online) | GradCertPsych | Online | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-psychology-online/ |
| Graduate Diploma in Clinical Supervision | GradDipClinSup | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-in-clinical-supervision/ |
| Graduate Diploma in Forensic Psychology | GradDipForensPsych | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-in-forensic-psychology/ |
| Graduate Diploma of Counselling | GradDipCouns | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-counselling/ |
| Graduate Diploma of Early Childhood Teaching | GradDipECT | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-early-childhood-teaching/ |
| Graduate Diploma of Early Childhood Teaching (Swinburne Online) | GradDipECT | Online | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-early-childhood-teaching-swinburne-online/ |
| Graduate Diploma of Forensic Behavioural Science | GradDipForensBS | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-forensic-behavioural-science/ |
| Graduate Diploma of Forensic Mental Health Nursing | GradDipForensMHN | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-forensic-mental-health-nursing/ |
| Graduate Diploma of Psychology (Advanced) (Swinburne Online) | GradDipPsychAdv | Online | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-psychology-advanced-swinburne-online/ |
| Graduate Diploma of Psychology (Swinburne Online) | GradDipPsych | Online | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-psychology-swinburne-online/ |
| Master of Counselling | MCouns | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-counselling/ |
| Master of Dietetics | MDiet | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-dietetics/ |
| Master of Educational Leadership | MEdLead | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-educational-leadership/ |
| Master of Forensic Behavioural Science | MForensBS | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-forensic-behavioural-science/ |
| Master of Occupational Therapy | MOccTher | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-occupational-therapy/ |
| Master of Physiotherapy | MPhysio | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-physiotherapy/ |
| Master of Psychology (Clinical Psychology) | MPsych(Clin) | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-psychology-clinical-psychology/ |
| Master of Psychology (Educational and Development Psychology) | MPsych(EdDev) | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-psychology-educational-and-development-psychology/ |
| Master of Sports and Exercise Physiotherapy | MSportsExPhysio | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-sports-and-exercise-physiotherapy/ |
| Master of Teaching (Primary) (Swinburne Online) | MTeach(Prim) | Online | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-teaching-primary-swinburne-online/ |
| Master of Teaching (Secondary) | MTeach(Sec) | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-teaching-secondary/ |
| Master of Teaching (Secondary) (Swinburne Online) | MTeach(Sec) | Online | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-teaching-secondary-swinburne-online/ |

#### School of Science, Computing and Emerging Technologies

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate of Aviation | GradCertAvn | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-aviation/ |
| Graduate Certificate of Aviation Piloting | GradCertAvnPilot | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-aviation-piloting/ |
| Graduate Certificate of Cyber Security | GradCertCyberSec | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-cyber-security/ |
| Graduate Certificate of Cybersecurity Management (Swinburne Online) | GradCertCyberSecMgmt | Online | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-cybersecurity-management-swinburne-online/ |
| Graduate Certificate of Data Science | GradCertDataSc | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-data-science/ |
| Graduate Certificate of Information Technology | GradCertIT | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-information-technology/ |
| Graduate Certificate of Science (Astronomy) | GradCertSc(Ast) | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-science-astronomy/ |
| Graduate Certificate of Urban Informatics | GradCertUrbInf | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-urban-informatics/ |
| Graduate Diploma of Aviation | GradDipAvn | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-aviation/ |
| Graduate Diploma of Cyber Security | GradDipCyberSec | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-cyber-security/ |
| Graduate Diploma of Information Technology | GradDipIT | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-information-technology/ |
| Graduate Diploma of Science (Astronomy) | GradDipSc(Ast) | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-science-astronomy/ |
| Graduate Diploma of Science (Biotechnology) | GradDipSc(Biotech) | Hawthorn | 1 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-diploma-of-science-biotechnology/ |
| Master of Aviation | MAvn | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-aviation/ |
| Master of Cyber Security | MCyberSec | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-cyber-security/ |
| Master of Data Science | MDataSc | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-data-science/ |
| Master of Information Technology | MIT | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-information-technology/ |
| Master of Information Technology (Professional Computing) | MIT(ProfComp) | Hawthorn | 2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-information-technology-professional-computing/ |
| Master of Science (Astronomy) | MSc(Ast) | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-science-astronomy/ |
| Master of Science (Biotechnology) | MSc(Biotech) | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-science-biotechnology/ |

#### School of Social Sciences, Media, Film and Education

| Program Name | Degree Type | Campus | Duration | URL |
|-------------|-------------|--------|----------|-----|
| Graduate Certificate of Educational Studies (Non-Teaching) (Swinburne Online) | GradCertEdStud | Online | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-of-educational-studies-non-teaching-swinburne-online/ |
| Graduate Certificate in Learning and Teaching (Higher Education) | GradCertLearnTeach | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-learning-and-teaching-higher-education/ |
| Graduate Certificate in Learning and Teaching (VET) | GradCertLearnTeachVET | Hawthorn | 0.5 yr | https://www.swinburne.edu.au/course/postgraduate/graduate-certificate-in-learning-and-teaching-vet/ |
| Master of Media and Communication | MMediaComm | Hawthorn | 1.5-2 yrs | https://www.swinburne.edu.au/course/postgraduate/master-of-media-and-communication/ |

### 2.2 Research Degrees (PhD / MRes)

| Program Name | Degree Type | URL |
|-------------|-------------|-----|
| Doctor of Philosophy (Business) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-business/ |
| Doctor of Philosophy (Business Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-business-integrated/ |
| Doctor of Philosophy (Business — Practice-based Research) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-business-practice-based-research/ |
| Doctor of Philosophy (Clinical Psychology) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-clinical-psychology/ |
| Doctor of Philosophy (Design) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-design/ |
| Doctor of Philosophy (Design Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-design-integrated/ |
| Doctor of Philosophy (Engineering) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-engineering/ |
| Doctor of Philosophy (Health Sciences) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-health-sciences/ |
| Doctor of Philosophy (Health Sciences Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-health-sciences-integrated/ |
| Doctor of Philosophy (Humanities, Arts and Social Sciences) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-humanities-arts-and-social-sciences/ |
| Doctor of Philosophy (HASS Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-humanities-arts-and-social-sciences-integrated/ |
| Doctor of Philosophy (Information and Communication Technology) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-information-and-communication-technology/ |
| Doctor of Philosophy (ICT Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-information-and-communication-technology-integrated/ |
| Doctor of Philosophy (Information Systems) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-information-systems/ |
| Doctor of Philosophy (Law) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-law/ |
| Doctor of Philosophy (Science) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-science/ |
| Doctor of Philosophy (Science Integrated) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-science-integrated/ |
| Doctor of Philosophy (Technology Innovation — Business and Law) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-technology-innovation-business-and-law/ |
| Doctor of Philosophy (Technology Innovation — Health, Arts and Design) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-technology-innovation-health-arts-and-design/ |
| Doctor of Philosophy (Technology Innovation — Science, Engineering and Technology) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-technology-innovation-science-engineering-and-technology/ |
| Doctor of Psychology (Clinical and Forensic Psychology) | DPsych | https://www.swinburne.edu.au/course/research/doctor-of-psychology-clinical-and-forensic-psychology/ |
| PhD + GradCert Research and Innovation Management (Business) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-business/ |
| PhD + GradCert Research and Innovation Management (Design) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-design/ |
| PhD + GradCert Research and Innovation Management (Engineering) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-engineering/ |
| PhD + GradCert Research and Innovation Management (Health Sciences) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-health-sciences/ |
| PhD + GradCert Research and Innovation Management (HASS) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-humanities-arts-and-social-sciences/ |
| PhD + GradCert Research and Innovation Management (ICT) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-information-and-communication-technology/ |
| PhD + GradCert Research and Innovation Management (Information Systems) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-information-systems/ |
| PhD + GradCert Research and Innovation Management (Law) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-law/ |
| PhD + GradCert Research and Innovation Management (Science) | PhD | https://www.swinburne.edu.au/course/research/doctor-of-philosophy-and-graduate-certificate-of-research-and-innovation-management-science/ |
| Graduate Certificate of Research and Innovation Management | GradCertResInnov | https://www.swinburne.edu.au/course/research/graduate-certificate-of-research-and-innovation-management/ |
| Master of Arts (Research) | MA(Res) | https://www.swinburne.edu.au/course/research/master-of-arts-research/ |
| Master of Business (Research) | MBus(Res) | https://www.swinburne.edu.au/course/research/master-of-business-research/ |
| Master of Design (Research) | MDes(Res) | https://www.swinburne.edu.au/course/research/master-of-design-research/ |
| Master of Engineering (Research) | MEng(Res) | https://www.swinburne.edu.au/course/research/master-of-engineering-research/ |
| Master of Health Sciences (Research) | MHealthSc(Res) | https://www.swinburne.edu.au/course/research/master-of-health-sciences-research/ |
| Master of Information and Communication Technologies (Research) | MICT(Res) | https://www.swinburne.edu.au/course/research/master-of-information-and-communication-technologies-research/ |
| Master of Law (Research) | LLM(Res) | https://www.swinburne.edu.au/course/research/master-of-law-research/ |
| Master of Science (Research) | MSc(Res) | https://www.swinburne.edu.au/course/research/master-of-science-research/ |
| Master of Research (Business) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-business/ |
| Master of Research (Design) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-design/ |
| Master of Research (Health Sciences) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-health-sciences/ |
| Master of Research (Humanities, Arts and Social Sciences) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-humanities-arts-and-social-sciences/ |
| Master of Research (Information and Communication Technology) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-information-and-communication-technology/ |
| Master of Research (Science) | MRes | https://www.swinburne.edu.au/course/research/master-of-research-science/ |
| Master of Engineering Research | MEng(Res) | https://www.swinburne.edu.au/course/research/master-of-engineering-research/ |

---

## Section 3 — Application requirements & deadlines

### 3.1 Academic Entry Requirements

**Domestic (Australian) students:**
- Completion of Victorian Certificate of Education (VCE) or equivalent interstate/international Year 12
- Australian Tertiary Admission Rank (ATAR) — Guaranteed Entry ATAR varies by course (e.g., Bachelor of Computer Science: 70.0)
- Meeting minimum entry requirements does not guarantee selection
- For applicants with VET study, higher education study, or work/life experience — alternative entry pathways available

**International students:**
- Equivalent overseas qualification assessed at time of application
- Country-specific academic requirements available via dropdown on international entry requirements page
- Minimum age: 17 years old at course commencement
- Early Entry Program available for current Year 12 students

### 3.2 English Language Requirements

**For TAFE and Pathway courses:**

| Test | Foundation Program | UniLink Diplomas | UniLink Bridging | Cert III-IV, Diplomas, Adv Dip, PQP |
|-----|-------------------|-----------------|------------------|-------------------------------------|
| IELTS (Academic) | 5.5 (no band <5.0) | 5.5 (no band <5.0) | 6.0 (no band <5.5) | 6.0 (no band <5.5) |
| PTE Academic | 42 (no skill <36) | 42 (no skill <36) | 50 (no skill <42) | 50 (no skill <42) |
| TOEFL iBT | 46 (R4/L4/S14/W14) | 46 (R4/L4/S14/W14) | 64 (R8/L7/S16/W18) | 64 (R8/L7/S16/W18) |
| C1 Advanced | 162 (no band <154) | 162 (no band <154) | 169 (no band <162) | 169 (no band <162) |

**For Undergraduate and Postgraduate courses:**

| Test | UG Degrees (standard) | UG: Ed/ExSS/Law/Psych/ProfDeg | Nursing / MPhysio | PG Coursework / PG Research | MPsych / MDiet / MOccTher | MTeach(Sec) |
|-----|----------------------|-------------------------------|-------------------|----------------------------|--------------------------|-------------|
| IELTS (Academic) | 6.0 (no band <6.0) | 6.5 (no band <6.0) | 7.0 (L/R/S 7.0, W 6.5) | 6.5 (no band <6.0) | 7.0 (no band <7.0) | 7.0 (S&L 7.5, others 7.0) |
| PTE Academic | 50 (no skill <50) | 58 (no skill <50) | 66 (L/R/S 66, W 56) | 58 (no skill <50) | 66 (no skill <66) | 66 (S&L 76, others 66) |
| TOEFL iBT | 64 (R13/L12/S18/W21) | 79 (R13/L12/S18/W21) | 94 (L/R/W 24, S 23) | 79 (R13/L12/S18/W21) | 94 (R24/L24/S23/W27) | 94 (R25/L27/S25/W27) |
| C1 Advanced | 169 (no band <169) | 176 (no band <169) | 185 (L/R/S 185, W 176) | 176 (no band <169) | 185 (no band <185) | 185 (R185/L191/S191/W185) |

### 3.3 Application Deadlines — 2026 Intakes

**Higher Education (HE):**

| Intake | Start Date | End Date | Last Date to Apply |
|--------|-----------|---------|-------------------|
| Summer Intake | 5 Jan 2026 | 15 Feb 2026 | 17 Dec 2025 |
| Semester 1 | 2 Mar 2026 | 31 May 2026 | 25 Feb 2026 |
| Semester 2 | 3 Aug 2026 | 1 Nov 2026 | 29 Jul 2026 |
| Term 4 Intake | 21 Sep 2026 | 1 Nov 2026 | 16 Sep 2026 |
| Winter Intake | 22 Jun 2026 | 2 Aug 2026 | 17 Jun 2026 |
| HE Block 1 | 2 Feb 2026 | 15 Mar 2026 | 28 Jan 2026 |
| HE Block 2 | 16 Mar 2026 | 26 Apr 2026 | 11 Mar 2026 |
| HE Block 4 | 25 May 2026 | 5 Jul 2026 | 20 May 2026 |
| HE Block 5 | 6 Jul 2026 | 16 Aug 2026 | 1 Jul 2026 |
| HE Block 8 | 26 Oct 2026 | 6 Dec 2026 | 21 Oct 2026 |
| Quarter 1 | 19 Jan 2026 | 22 Mar 2026 | 14 Jan 2026 |
| Quarter 2 | 13 Apr 2026 | 14 Jun 2026 | 8 Apr 2026 |
| Quarter 3 | 6 Jul 2026 | 6 Sep 2026 | 1 Jul 2026 |
| Quarter 4 | 28 Sep 2026 | 29 Nov 2026 | 23 Sep 2026 |
| Study Block 1 | 19 Jan 2026 | 22 Mar 2026 | 14 Jan 2026 |
| Study Block 2 | 13 Apr 2026 | 14 Jun 2026 | 8 Apr 2026 |
| Study Block 3 | 6 Jul 2026 | 6 Sep 2026 | 1 Jul 2026 |

### 3.4 How to Apply

- **Domestic UG**: Via VTAC (Victorian Tertiary Admissions Centre) or direct application
- **Domestic PG**: Direct application to Swinburne
- **International**: Direct via online application portal OR through approved education agent
- **Research**: Direct application for research degree
- **VET (TAFE)**: Direct application
- **Special Entry Access Scheme (SEAS)**: Available for eligible VTAC applicants

### 3.5 Special Requirements

- Minimum age: 17 years at course commencement
- Prerequisite subjects: VCE Maths (MathsLink bridging available)
- Portfolio/Interview: Required for some Design, Architecture, Film & TV courses
- Work Integrated Learning (WIL): Guaranteed in all bachelor degrees (placements, internships, or industry-linked projects)

---

## Section 4 — Costs & financial aid

### 4.1 International Tuition Fees (Indicative)

Fees are indicative only, based on standard full-time study load, and subject to annual review.

**Study levels:**
- **Foundation and UniLink programs**: Fee varies by program
- **Vocational Education (TAFE)**: Fee varies by program
- **Undergraduate degrees**: Per individual course page (e.g., Bachelor of Computer Science — see course page for fee)
- **Postgraduate degrees**: Per individual course page
- **Research degrees**: Per individual course page

> **Note**: Individual course fees are displayed on each course page when toggled to "international student" view. The site uses an interactive fee calculator per course, and bulk fee extraction requires per-page navigation.

### 4.2 Local Student Fees

- **Diplomas and certificates**: Commonwealth Supported Places (CSP) available; HECS-HELP loan available
- **Bachelor degrees and double degrees**: CSP available; HECS-HELP available; Alumni Discount available
- **Postgraduate study**: FEE-HELP available; CSP may be available for some courses
- **PhDs**: Research Training Program (RTP) places available
- **Master by research**: RTP places available

### 4.3 Student Services and Amenities Fee (SSAF)

- International tuition fees generally inclusive of SSAF
- Domestic students may pay SSAF separately

### 4.4 Scholarships

- **International Scholarships**: Automatically considered when applying for 2026 intake — no separate application needed; included in offer letter
- **Domestic Scholarships**: Various merit-based and equity-based scholarships available
- **Alumni Discount**: Discount available for Swinburne alumni pursuing further study

### 4.5 Cost of Living (Melbourne)

Estimated living costs in Melbourne (per year):
- Accommodation: ~AUD $12,000–$20,000
- Food and groceries: ~AUD $5,000–$8,000
- Transport: ~AUD $1,500–$2,500
- Other expenses: ~AUD $4,000–$8,000

---

## Section 5 — Evidence chain index

| ID | Field | Value | Source URL | Evidence Type |
|----|-------|-------|-----------|--------------|
| E-SW-001 | institution.name | Swinburne University of Technology | https://www.swinburne.edu.au/ | official_webpage |
| E-SW-002 | institution.cricos | 00111D | https://www.swinburne.edu.au/ | official_webpage |
| E-SW-003 | institution.teqsa | PRV12148 Australian University | https://www.swinburne.edu.au/ | official_webpage |
| E-SW-004 | total_course_urls | 726 | https://www.swinburne.edu.au/course/sitemap.xml | sitemap |
| E-SW-005 | ug_programs | 119 unique | https://www.swinburne.edu.au/course/sitemap.xml | sitemap |
| E-SW-006 | pg_programs | 90 unique | https://www.swinburne.edu.au/course/sitemap.xml | sitemap |
| E-SW-007 | research_programs | 45 unique | https://www.swinburne.edu.au/course/sitemap.xml | sitemap |
| E-SW-008 | tafe_programs | 108 unique | https://www.swinburne.edu.au/course/sitemap.xml | sitemap |
| E-SW-009 | schools_higher_ed | 6 named | https://www.swinburne.edu.au/about/our-structure/organisational-structure/schools-departments/ | official_webpage |
| E-SW-010 | vet_departments | 5 named | https://www.swinburne.edu.au/about/our-structure/organisational-structure/schools-departments/ | official_webpage |
| E-SW-011 | research_institutes | 4 named | https://www.swinburne.edu.au/research/institutes/ | official_webpage |
| E-SW-012 | atar_guaranteed | 70.0 (BCompSci) | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science/ | official_webpage |
| E-SW-013 | duration | 3 years full-time | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science/ | official_webpage |
| E-SW-014 | campus | Hawthorn | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science/ | official_webpage |
| E-SW-015 | intakes | Semester 1, Semester 2, Study Block 4 | https://www.swinburne.edu.au/course/undergraduate/bachelor-of-computer-science/ | official_webpage |
| E-SW-016 | english_ielts_ug | 6.0 (no band <6.0) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-017 | english_ielts_pg | 6.5 (no band <6.0) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-018 | english_ielts_nursing | 7.0 (L/R/S 7.0, W 6.5) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-019 | english_ielts_teaching | 7.0 (S&L 7.5, others 7.0) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-020 | english_pte_ug | 50 (no skill <50) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-021 | english_toefl_ug | 64 (R13/L12/S18/W21) | https://www.swinburne.edu.au/study/international/apply/entry-requirements/ | official_webpage |
| E-SW-022 | min_age | 17 years at course commencement | https://www.swinburne.edu.au/courses/planning-your-future/admission-requirements/ | official_webpage |
| E-SW-023 | semester1_2026 | 2 Mar 2026 – 31 May 2026 | https://www.swinburne.edu.au/courses/intakes/start-dates-intakes/ | official_webpage |
| E-SW-024 | semester2_2026 | 3 Aug 2026 – 1 Nov 2026 | https://www.swinburne.edu.au/courses/intakes/start-dates-intakes/ | official_webpage |
| E-SW-025 | platform_cms | Squiz Matrix + Funnelback | https://www.swinburne.edu.au/ | http_headers |
| E-SW-026 | study_areas | 18 study areas | https://www.swinburne.edu.au/courses/find-a-course/ | official_webpage |

---

## Section 6 — WeKnora import manifest

### Follow-up data items (prioritized)

| Priority | Data item | Status | Action needed |
|----------|-----------|--------|---------------|
| **P0** | Per-course international tuition fees | ⚠️ Partial | Fees shown as interactive widget per course page — bulk sampling needed |
| **P0** | Per-course domestic CSP fees | ⚠️ Partial | Similar to international — per-page extraction required |
| **P1** | TAFE/VET full course listing with fees | ⏳ Pending | 108 TAFE courses listed in sitemap — need fee extraction |
| **P1** | Individual course ATAR/entry scores for all UG | ⏳ Pending | Currently have sample (BCompSci=70.0) — need full extraction |
| **P1** | Short courses (64) — detailed data | ⏳ Pending | Listed in sitemap but details not extracted |
| **P2** | Research institute details | ✅ Complete | Institutes identified, full details available on research pages |
| **P2** | Scholarships detailed info | ⏳ Pending | Scholarships page has detailed listings |
| **P2** | Swinburne Online course data | ⏳ Pending | Online variants listed in sitemap but fees not extracted |
| **P2** | Pathway (Foundation/UniLink) fees | ⏳ Pending | Listed in fees page accordion — data not extracted |
| **P2** | School handbooks / course structure | ⏳ Pending | Each course has handbook link — extraction needed |

### Import metadata for WeKnora

```yaml
document:
  id: au-swinburne-v2
  title: Swinburne_University_知识库_完整深度数据_v2
  country: AU
  region: Melbourne, Victoria
  granularity: school → department → degree-level → program
  total_programs_ug: 83 (base) / 119 (with specializations)
  total_programs_pg: 74 (coursework + research)
  total_programs_vet: 108
  total_short_courses: 64
  total_pathway: 18
  schools: 6 higher education + 5 VET departments
  research_institutes: 4
  evidence_entries: 26
  extract_date: 2026-07-10
  extract_tool: browser_navigate + browser_snapshot + curl + sitemap
  completeness: UG listing ✅ | PG listing ✅ | Research ✅ | English req ✅ | Deadlines ✅ | Fees ⚠️ (per-course, sampled)
```

---

## Section 7 — Cross-school comparison framework

> To be filled when comparative peer data is available. Suggested comparison universities:
> - RMIT University (Melbourne, similar tech focus)
> - Deakin University (Melbourne, similar size)
> - La Trobe University (Melbourne, similar structure)

| Dimension | Swinburne | RMIT | Deakin |
|-----------|-----------|------|--------|
| Total UG programmes | ~119 | TBD | TBD |
| Total PG programmes | ~90 | TBD | TBD |
| Schools/Faculties | 6 HE + 5 VET | TBD | TBD |
| ATAR range (sample) | 70.0 (CS) | TBD | TBD |
| IELTS UG minimum | 6.0 | TBD | TBD |
| IELTS PG minimum | 6.5 | TBD | TBD |

---

> **Document version**: v2.0 (deep)
> **Generated**: 2026-07-10
> **Sources**: Swinburne University of Technology official website
> **Granularity**: school → department → degree-level → program
> **Completeness**: Structural framework ✅ | UG programmes ✅ | PG programmes ✅ | Research ✅ | Evidence (26 blocks) ✅ | English req ✅ | Deadlines ✅ | Fees ⚠️ (per-course, sample available)
> **Next step**: Extract per-course international fees from individual course pages
