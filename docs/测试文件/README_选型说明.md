# 知识库测试文件选型说明

> **选取日期**: 2026-07-09
> **来源**: `knowledge-base/` 目录 (共 442 份院校文档，含 US 241 / UK 198 / Other 3)
> **选取原则**: 质量最高 + 特征互异 — 确保每一份文档都能测出其他文档测不出的问题

---

## 一、选取标准

从 442 份 v2.0 深度文档中筛选 10 份，每一份需同时满足：

1. **质量门槛**: 结构完整（Section 0–5 齐全）、数据详实、含来源引用、通过 Rule 1–5 对账验证
2. **特征互异**: 每份文档至少有一个维度是其他 9 份不具备或明显不同的（见下表）

---

## 二、10 份文件及各自独特特征

| # | 文件名 | 大小 | 院校 | 独有测试特征 |
|---|--------|------|------|-------------|
| 1 | `ASU_知识库_完整深度数据_v2.md` | 193 KB | Arizona State University | **程序量最大**：1,184 个学位项目，17+ 学院，数据密度全库第一 |
| 2 | `UPenn_知识库_完整深度数据_v2.md` | 139 KB | University of Pennsylvania | **学位类型最多**：76 种 distinct degree designation，641 行 program-degree，含 Wharton concentration / BSE/BAS/BAAS 等 Ivy 独有的"专业本科"变体 |
| 3 | `Harvard_知识库_完整深度数据_v2.md` | 66 KB | Harvard University | **拉丁学位命名体系**：A.B./S.B./A.M./S.M. 等拉丁缩写（非标准 BA/BS/MA/MS），v2.0 格式的"范例文档"原型 |
| 4 | `Caltech_知识库_完整深度数据_v2.md` | 58 KB | California Institute of Technology | **完全非标准术语**：不用"major"用"option"，不用"school"用"Division"，仅授 BS（无 BA/BFA），仅 76 个程序，极致精简型 |
| 5 | `MIT_知识库_完整深度数据_v2.md` | 79 KB | Massachusetts Institute of Technology | **工程编号体系**："Course 6/16/18" 等数字编号，SB/SM 学位缩写，OGE 集中式研究生院，IDSS 跨院共享系所 |
| 6 | `UCBerkeley_知识库_完整深度数据_v2.md` | 91 KB | UC Berkeley | **旗舰公立 + test-blind**：UC 系统旗舰，SAT/ACT 完全不考虑（test-free），州内/外学费双轨制，最新 CDSS 学院（2023 年成立），L&S 四分部结构 |
| 7 | `Imperial_知识库_完整深度数据_v2.md` | 72 KB | Imperial College London | **UK STEM 精英**：Russell Group，4-faculty 紧凑结构，MSc/MRes/PG Cert/PG Dip 英国研究生体系，UCAS 本科申请语境，PhD 未纳入主课程搜索 |
| 8 | `Melbourne_知识库_完整深度数据_v2.md` | 65 KB | University of Melbourne | **澳洲 Melbourne Model**：宽口径本科（仅 20 个 bachelor）+ 专业化研究生，Funnelback Search API 抓取，微证书(78)和短期课程(97)独立分类，AU Honours 学位层级 |
| 9 | `UofT_知识库_完整深度数据_v2.md` | 90 KB | University of Toronto | **加拿大三校区 + subject POSt**：St. George/Mississauga/Scarborough 独立招生，HBA/HBSc 命名，"Major/Minor/Specialist" 组合模型（非美国式单轨主修），MusBac/BKin 等稀有学位 |
| 10 | `Duke_知识库_完整深度数据_v2.md` | 74 KB | Duke University | **复杂专业学院群**：10 学院含 Trinity/Pratt/Fuqua/Law/Medicine/Nursing/Divinity/Sanford/Nicholas，AB→BA 命名映射，Nicholas School JS 壳降级处理记录，DKU 跨国项目，MDiv/ThD/DMin 神学学位 |

---

## 三、覆盖的测试维度矩阵

```
                     Ivy   大公立  理工    UK    AU    CA   超大   超小   非标准
                     League Public 精英  体系  体系  体系  体量   体量   术语
ASU                   -      ✓      -     -     -     -     ✓     -      -
UPenn                 ✓      -      -     -     -     -     ✓     -      ✓(76种学位)
Harvard               ✓      -      -     -     -     -     -     -      ✓(拉丁缩写)
Caltech               -      -      ✓     -     -     -     -     ✓      ✓(option/Division)
MIT                   -      -      ✓     -     -     -     -     -      ✓(Course编号)
UC Berkeley           -      ✓      -     -     -     -     -     -      ✓(test-blind)
Imperial              -      -      ✓     ✓     -     -     -     -      ✓(4-faculty)
Melbourne             -      -      -     -     ✓     -     -     -      ✓(Melbourne Model)
UofT                  -      ✓      -     -     -     ✓     -     -      ✓(subject POSt)
Duke                  -      -      -     -     -     -     -     -      ✓(神学/JS降级)
```

---

## 四、各文档能暴露的典型 RAG 问题

| 文档 | 可能暴露的问题 |
|------|---------------|
| **ASU** | 超长文档切分策略是否合理；海量程序名检索能否精准命中 |
| **UPenn** | 76 种学位缩写是否被正确归一化；Wharton "concentration" 是否被识别为本科主修 |
| **Harvard** | "A.B." 能否映射到 "Bachelor of Arts"；"concentration" vs "major" 语义对齐 |
| **Caltech** | "option" 是否能被理解为主修；"Division" 与 "School/College" 等价性 |
| **MIT** | "Course 6" 能否关联到 EECS 系；ScD 与 PhD 是否被正确区分 |
| **UC Berkeley** | test-blind 政策是否被准确检索；州内/外学费是否被混淆 |
| **Imperial** | UK PG Cert/PG Dip 是否被正确分类；UCAS vs Common App 申请路径差异 |
| **Melbourne** | AU Honours 层级是否被理解；micro-credential 是否被排除在学位计数外 |
| **UofT** | HBA/HBSc 是否被映射到标准 BA/BS；三校区独立招生是否被识别 |
| **Duke** | AB→BA 映射是否生效；MDiv/ThD/DMin 是否被正确归类为专业学位而非 PhD |

---

## 五、文件大小梯度（测试分块策略）

| 梯度 | 文件 | 大小 | 适用测试 |
|------|------|------|---------|
| 超大 (>100KB) | ASU, UPenn | 193KB, 139KB | 长文档分块/窗口溢出 |
| 大 (80-100KB) | UCBerkeley, UofT, MIT | 91-94KB | 标准长文档检索 |
| 中 (60-80KB) | Duke, Imperial, Harvard, Melbourne | 58-74KB | 中等文档完整性 |
| 全量 | 10 份合计 | ~927 KB | 跨文档聚合/去重/对比查询 |

---

## 六、未选入的高质量文档说明

以下文档同样质量很高，但因特征与已选文档重叠而未被选入（可作为扩展测试集）：

- **Stanford** (79KB) — 优秀但特征与 Harvard/MIT 重叠
- **Princeton** (65KB) — 优秀但特征与 Harvard 重叠（Ivy + 拉丁学位）
- **Columbia** (114KB) — 优秀但特征与 UPenn 重叠（多学院 Ivy）
- **Cornell** (84KB) — 优秀但公私合营模式未在已选集合中体现，可作为后续扩展
- **UCLA** (82KB) — 优秀但特征与 UC Berkeley 重叠（UC 系统旗舰）
- **USC** (198KB) — 体量与 ASU 相当但特征重叠
- **NYU** (147KB) — 优秀但与 Duke/UPenn 多学院特征重叠
- **Cardiff** (58KB) — UK 代表但 Imperial 质量更高、特征更鲜明
- **NC State** (204KB) — 体量最大但为框架型文档，深度不如 ASU
