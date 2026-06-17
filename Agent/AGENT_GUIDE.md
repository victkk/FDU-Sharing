# FDU-Sharing Agent 操作指南

> **目标**: 当用户提供课程资料文件时，帮助用户将这些资料添加到 FDU-Sharing 项目中。
> **原则**: Agent 直接操作，不依赖任何自动化脚本。
> **文件位置**: `Agent/AGENT_GUIDE.md`（本文件应放在 Agent 文件夹中）

---

## 🚀 启动步骤（Agent 必读）

**收到用户请求后，必须首先执行：**

```
第1步: Read pages/courses/_meta.ts
```

这是**不可跳过**的首步操作，读取后才能：
- 确认课程是否已存在
- 获取准确的拼音名
- 了解完整的课程列表

**等待用户确认/提供文件后，再继续后续流程。**

---

## 一、项目概述

**FDU-Sharing** 是复旦大学课程资料分享网站，使用 Next.js + Nextra 构建。

### 核心概念

| 概念 | 说明 | 路径示例 |
|------|------|----------|
| 资料存储 | 课程中文名目录 | `public/resources/数据结构/xxx.pdf` |
| 课程页面 | 拼音名 MDX 文件 | `pages/courses/shujujiegou.mdx` |
| 导航配置 | 课程注册表 | `pages/courses/_meta.ts` |

**为什么页面用拼音？** Next.js 对中文路由支持有问题，拼音可避免 404 错误。

### 目录结构

```
FDU-Sharing/
├── public/
│   └── resources/
│       └── 数据结构/              # 课程中文名目录
│           ├── 2024-期末-试卷.pdf
│           └── 2023-复习-总结.pdf
├── pages/
│   └── courses/
│       ├── _meta.ts              # 课程导航配置（⭐ 首步必读）
│       ├── shujujiegou.mdx       # 课程页面（拼音名）
│       └── ...
├── Agent/                        # AI Agent 辅助目录
│   ├── AGENT_GUIDE.md            # 本文件 - Agent 操作指南
│   └── README.md                 # Agent 目录说明
├── scripts/                      # 自动化脚本（本指南不依赖）
└── upload/                       # 临时上传目录
    └── README.md
```

---

## 二、Agent 直接操作流程（唯一流程）

```
1. [必做] Read pages/courses/_meta.ts → 获取课程列表
2. 确认用户提供的文件路径和课程信息
3. Bash mv（先检查不覆盖）将文件移动到 public/resources/课程中文名/
4. Read pages/courses/课程拼音.mdx → 获取当前页面内容
5. Edit 在 MDX 中添加 <FileDownload> 组件
6. 如为新课程：Edit 更新 _meta.ts 添加课程条目
7. Bash git 操作：add → commit → push
```

---

## 三、文件移动规则（⭐ 统一约束）

### 工具约束

**必须使用 `Bash` 工具执行 `mv` 命令，禁止使用其他方式移动文件。**

为避免误删/误覆盖，移动前必须：
- 先确认源文件存在、目标目录存在（不存在先 `mkdir -p`）
- 路径加引号，避免空格或特殊字符导致命令失败
- 若目标文件已存在，不覆盖；改名为 `_v2` 或时间戳后再移动

```bash
# 标准命令格式
mv "源文件路径" "public/resources/课程中文名/目标文件名.pdf"
```

### 文件命名规范

**标准格式**: `[年份]-[类型]-[描述].扩展名`

| 类型 | 示例 |
|------|------|
| 期末考试 | `2024-期末-试卷.pdf`, `2024-期末-答案.pdf` |
| 期中考试 | `2024-期中-试卷.pdf`, `2024-期中-答案.pdf` |
| 复习资料 | `2024-复习-知识点总结.pdf`, `2024-复习-重点笔记.pdf` |
| 课堂笔记 | `2024-笔记-第一章.pdf` |
| 作业习题 | `2024-作业-习题1.pdf` |
| PPT课件 | `2024-课件-第三章.pptx` |

**支持的文件格式**: `.pdf`, `.docx`, `.doc`, `.pptx`, `.ppt`, `.zip`, `.rar`, `.7z`, `.md`, `.txt`, `.xlsx`, `.xls`, `.png`, `.jpg`, `.jpeg`

**文件大小限制**: 单文件不超过 100MB

---

## 四、课程注册（_meta.ts）

### 文件格式

```typescript
export default {
  'shujujiegou': '🌲 数据结构',
  'xianxingdaishu': '📊 线性代数',
  // ... 更多课程
}
```

### 格式规则

| 规则 | 说明 |
|------|------|
| 键 | 拼音名，单引号包围 |
| 值 | emoji + 空格 + 课程中文名，单引号包围 |
| 逗号 | 每行结尾加逗号（最后一行除外） |

### 添加新课程

在最后一行之前插入新行：

```typescript
  'bianyiyuanli': '⚙️ 编译原理',  // 新增课程
}
```

---

## 五、MDX 页面编辑规则

### 页面结构

```mdx
import { FileDownload } from '@/components/FileDownload'
import { Comments } from '@/components/Comments'

# 📚 课程中文名

> 本页面收集了XXX课程的相关资料

## 📝 期末考试

---

## 📝 期中考试

---

## 📚 复习资料

---

## 📖 课堂笔记

---

## 💡 作业习题

---

<Comments />
```

### FileDownload 组件格式

```mdx
<FileDownload name="显示名称" path="/resources/课程中文名/文件名.扩展名" />
```

### name 显示名格式模板

| 情况 | name 格式 | 示例 |
|------|----------|------|
| 有年份和描述 | `{年份}年{描述}` | `name="2024年期末试卷"` |
| 有年份无明确描述 | `{年份}年{类型}` | `name="2024年期末答案"` |
| 无年份 | `{描述}` 或 `{类型}` | `name="复习总结"` |

**注意**: name 是**用户在网页上看到的名称**，可以与文件名不同。应简洁易读。

### 章节类型映射

| 资料类型关键词 | 对应章节标题 |
|---------------|-------------|
| 期末、final | `## 📝 期末考试` |
| 期中、midterm、段考、小测、quiz | `## 📝 期中考试` |
| 复习、review、总结 | `## 📚 复习资料` |
| 笔记、note | `## 📖 课堂笔记` |
| 作业、homework、hw | `## 💡 作业习题` |
| ppt、课件、讲义 | `## 📊 PPT课件` |
| 其他 | `## 📦 其他资料` |

### ⭐ 插入点定位规则（关键）

**步骤**:

1. **找到目标章节** - 定位如 `## 📝 期末考试` 的行号
2. **找到插入点** - 从章节行往下找，找到**第一个** `##` 或 `---` 的行
3. **在插入点之前插入** - 在那个分隔符行**之前**插入 `<FileDownload>`
4. **添加空行** - 在 `<FileDownload>` 之前添加一个空行

**图示**:
```mdx
## 📝 期末考试
                              ← 如果这里直接有内容，追加到现有内容后
<FileDownload name="..." path="..." />
                              ← 插入点1：新内容加在这里
---

## 📝 期中考试          ← 插入点2：或者在这个章节之前插入新章节
```

### ⭐ 章节不存在时的处理

**如果目标章节（如 `## 📚 复习资料`）在 MDX 中不存在：**

1. 找到 `<Comments />` 所在的行
2. 在 `<Comments />` **之前**插入新章节：

```mdx
（空行）
## 📚 复习资料

---
（空行）
<Comments />
```

3. 然后按"插入点定位规则"添加 `<FileDownload>`

---

## 六、课程名对照表

| 中文名 | 拼音名 | emoji |
|--------|--------|-------|
| 数学分析B | shuxuefenxiB | 📐 |
| 管院数学分析 | guanyuanshufenxi | 📐 |
| 线性代数 | xianxingdaishu | 📊 |
| 高等线性代数 | gaodengxianxingdaishu | 📈 |
| 高等代数 | gaodengdaishu | 📈 |
| 高等数学A | gaodengshuxueA | 📐 |
| 概率论与数理统计 | gailulun | 🎲 |
| 经院统计学 | jingyuantongjixue | 📊 |
| 集合与图论 | jiheyutulun | 🔗 |
| 最优化方法 | zuiyouhua | 📉 |
| 大学物理 | daxuewuli | ⚡ |
| 电路基础 | dianlujichu | 🔌 |
| 普通化学A（上） | puhuaAshang | 🧪 |
| 程序设计 | chengxusheji | 💻 |
| Python程序设计 | pythonchengxusheji | 🐍 |
| 面向对象程序设计 | oop | 🧩 |
| 数据结构 | shujujiegou | 🌲 |
| 算法设计与分析 | suanfa | ⚙️ |
| 计算机组成与体系结构 | jisuanjizucheng | 🖥️ |
| 数据库引论 | shujukuyinlun | 🗄️ |
| 模数电实验 | moshudianshiyan | 🔧 |
| 人工智能基础 | rengongzhinengjichu | 🤖 |
| 代数结构与数理逻辑 | daishujiegouyushuliluoji | 📚 |
| 自然语言处理 | ziranyuyanchuli | 🤖 |
| 科技人才英语沟通 | kejirencaiyingyugoutong | 🗣️ |
| 微观经济学 | weiguanjingjixue | 📈 |
| 政治经济学 | zhengzhijingjixue | 📕 |
| 腾飞先导课 | tengfeixiandao | 🚀 |
| 近代史纲要 | jindaishi | 📜 |
| 习概 | xigai | 📕 |
| 马克思主义基本原理 | makesi | 📗 |
| 毛概 | maogai | 📗 |
| 宋词导读 | songcidaodu | 📜 |
| 法哲学原理导读 | fazhexueyuanlidaodu | 📚 |
| 改革开放史 | gaigekaifangshi | 📚 |
| 概率统计与工程数学 | gailvtongjiyugongchengshuxue | 📚 |
| 高等数学B（下） | gaodengshuxueBxia | 📚 |
| 基础物理实验 | jichuwulishiyan | 📚 |
| 京剧 | jingju | 📚 |
| 军事理论 | junshililun | 📚 |
| 模拟电子线路 | monidianziluxian | 📚 |
| 嵌入式处理器与芯片系统设计 | qianrushichuliyuxinpixitongsheji | 📚 |
| 数字集成电路设计原理 | shuzijichengdianlushejiyuanli | 📚 |
| 数字逻辑基础-微电子 | shuziluojijichu_weidianzi | 📚 |
| 外国经济思潮 | waiguojingjisichao | 📚 |
| 现代生物科学导论 | xiandaishengwukexuedaolun | 📚 |
| 信号与通信系统 | xinhaoyutongxinxitong | 📚 |
| 植物改变生活 | zhiwugaibianshenghuo | 📚 |
| 中国音乐史 | zhongguoyinyueshi | 📚 |
| 中外音乐审美 | zhongwaiyinyueshenmei | 📚 |
| 先秦哲学 | xianqinzhexue | 📚 |
| 影视剧艺术 | yingshijuyishu | 🎬 |

> **动态获取**: 优先读取 `pages/courses/_meta.ts` 获取最新完整列表

---

## 七、Agent 识别与决策规则

### 课程名识别

1. **优先使用用户明确给出的课程名**
2. 若用户未明确，从文件夹名或文件名推断
3. 如有歧义，使用**交互提问工具**向用户确认（例如 AskUserQuestion）

### 资料类型识别

| 关键词 | 归类为 |
|--------|--------|
| 期末、final | 期末考试 |
| 期中、midterm、阶段性考试、段考、小测、quiz、测验 | 期中考试 |
| 复习、review、总结 | 复习资料 |
| 笔记、note | 课堂笔记 |
| 作业、homework、hw | 作业习题 |
| ppt、课件、讲义 | PPT课件 |
| 其他/无法归类 | 其他资料 |

### 年份识别

| 模式 | 提取结果 |
|------|----------|
| `2024-2025学年` | 2024 |
| `2024年`、`2024` | 2024 |
| 无法识别 | 省略年份或询问用户 |

### ⭐ 新课拼音来源策略

**优先级**：

1. **用户直接提供** - 用户明确说出拼音（最准确）
2. **交互提问工具询问** - 使用可用的提问工具让用户输入/确认拼音（例如 AskUserQuestion）
   ```
   选项：
   - "bianyiyuanli" (推荐)
   - "bianyi" (简化)
   - 其他 (用户自填)
   ```
3. **agent 推断** - 基于汉语拼音规则推断，但需用户确认

**拼音规范**:
- 优先与现有 `_meta.ts` 风格保持一致
- 不带声调
- 不使用空格（可使用连字符 `-` 或下划线 `_`，按现有风格保持一致）
- 避免特殊符号，保证可读且可用于路径

### Emoji 选择参考

| 学科分类 | 推荐emoji |
|----------|-----------|
| 数学/统计 | 📐 📊 📈 📉 🎲 |
| 物理/化学 | ⚡ 🔌 🧪 🔬 |
| 计算机 | 💻 🖥️ 🤖 ⚙️ 🌲 🗄️ 🧩 🔧 |
| 英语/语言 | 🗣️ 📝 📖 📚 |
| 经济 | 📈 📕 💰 |
| 政治/历史 | 📜 📕 📗 🏛️ |
| 文学/艺术 | 📜 🎬 🎭 🎨 |
| 通识/其他 | 📚 📖 💡 🚀 ⭐ |

---

## 八、Git 工作流程

### 分支命名规范

```
add/课程名-资料描述

例如: add/数据结构-期末试卷
```

### 提交信息格式

```
添加: 课程名 - 资料描述

例如: 添加: 数据结构 - 2024年期末试卷
```

### 完整命令

```bash
# 1. 创建分支（如果不在新分支上）
git checkout -b add/数据结构-期末试卷

# 2. 添加所有变更的文件
git add public/resources/数据结构/2024-期末-试卷.pdf
git add pages/courses/shujujiegou.mdx
git add pages/courses/_meta.ts  # 仅当更新了_meta.ts时

# 3. 提交
git commit -m "添加: 数据结构 - 2024年期末试卷"

# 4. 推送
git push origin add/数据结构-期末试卷
```

### 推送后操作

- 告知用户推送成功
- 提醒用户前往 GitHub 创建 PR
- 提供 PR 链接（如果可生成）

---

## 九、常见场景处理

### 场景1: 为已有课程添加资料

1. ✅ 已读 `_meta.ts`，确认课程存在
2. `mv` 文件到 `public/resources/课程中文名/`
3. `Read` 对应 MDX 页面
4. `Edit` 添加 `<FileDownload>` 组件
5. `Bash` git 操作

### 场景2: 添加全新课程

1. ✅ 已读 `_meta.ts`，确认课程不存在
2. **确定拼音** - 询问用户或让用户提供
3. **确定 emoji** - 根据学科分类选择
4. `Bash mkdir` 创建 `public/resources/课程中文名/`
5. `Write` 创建 `pages/courses/课程拼音.mdx`（使用模板）
6. `Edit` 更新 `_meta.ts` 添加课程条目
7. `Edit` 在新 MDX 中添加资料
8. `Bash` git 操作

### 场景3: 文件已存在（重复处理）

1. `Read` MDX 检查是否已添加该文件路径
2. 如果内容不同 → 在文件名加 `_v2` 或时间戳区分
3. 如果完全相同 → 跳过，告知用户

### 场景4: 文件名不规范

1. Agent 按命名规范重命名
2. 如重命名有歧义（年份/类型不明确）→ **先询问用户**

### 场景5: MDX 章节缺失

1. 按"章节不存在时的处理"规则创建新章节
2. 然后再插入 `<FileDownload>`

---

## 十、Agent 操作检查清单

| 步骤 | 操作 | 工具 |
|------|------|------|
| 1 | Read `_meta.ts` 获取课程列表 | ✅ Read |
| 2 | 确认用户提供的文件路径 | - |
| 3 | 识别课程名（中文+拼音） | - |
| 4 | 识别资料类型 | - |
| 5 | 识别年份 | - |
| 6 | 检查课程是否存在（基于步骤1） | - |
| 7 | 确定目标文件名 | - |
| 8 | 移动文件到正确位置 | ✅ Bash mv |
| 9 | Read 对应 MDX 页面 | ✅ Read |
| 10 | Edit 添加 `<FileDownload>` | ✅ Edit |
| 11 | 如果新课程：Edit 更新 `_meta.ts` | ✅ Edit |
| 12 | Git add → commit → push | ✅ Bash |

---

## 十一、完整示例对话

### 示例1: 添加已有课程的资料

**用户**: 我有数据结构的2024期末试卷，文件在 `/tmp/期末.pdf`

---

**Agent 执行流程**:

```
[Agent] 正在读取课程列表...
Read: pages/courses/_meta.ts

[Agent] 课程"数据结构"已存在，拼音名: shujujiegou
       目标路径: public/resources/数据结构/2024-期末-试卷.pdf

[Agent] 移动文件...
Bash: mv /tmp/期末.pdf public/resources/数据结构/2024-期末-试卷.pdf

[Agent] 读取课程页面...
Read: pages/courses/shujujiegou.mdx

[Agent] 在"期末考试"章节添加下载链接...
Edit: 在 ## 📝 期末考试 下方插入:
<FileDownload name="2024年期末试卷" path="/resources/数据结构/2024-期末-试卷.pdf" />

[Agent] 提交变更...
Bash: git add public/resources/数据结构/2024-期末-试卷.pdf pages/courses/shujujiegou.mdx
Bash: git commit -m "添加: 数据结构 - 2024年期末试卷"
Bash: git push origin add/数据结构-期末试卷

[Agent] ✅ 完成！请前往 GitHub 创建 PR
```

---

### 示例2: 添加全新课程

**用户**: 新增课程"编译原理"，资料在 `/tmp/编译原理资料.zip`

---

**Agent 执行流程**:

```
[Agent] 正在读取课程列表...
Read: pages/courses/_meta.ts

[Agent] 课程"编译原理"不存在，需要创建新课程

[Agent] 询问课程拼音和 emoji...
交互提问工具（例如 AskUserQuestion）:
  Q1: 课程拼音名？
     → bianyiyuanli (推荐) / 其他
  Q2: 选择 emoji？
     → ⚙️ (推荐) / 其他

[Agent] 创建资料目录...
Bash: mkdir -p public/resources/编译原理

[Agent] 创建课程页面...
Write: pages/courses/bianyiyuanli.mdx
      (使用附录模板)

[Agent] 更新导航配置...
Edit: pages/courses/_meta.ts
      在最后一行前插入: 'bianyiyuanli': '⚙️ 编译原理',

[Agent] 移动资料文件...
Bash: mv /tmp/编译原理资料.zip public/resources/编译原理/2024-课件-资料.zip

[Agent] 在新课程页面添加资料...
Read: pages/courses/bianyiyuanli.mdx
Edit: 在 ## 📚 复习资料 下方插入:
<FileDownload name="课件资料" path="/resources/编译原理/2024-课件-资料.zip" />

[Agent] 提交变更...
Bash: git add public/resources/编译原理/ pages/courses/bianyiyuanli.mdx pages/courses/_meta.ts
Bash: git commit -m "添加: 编译原理 - 新课程及课件资料"
Bash: git push origin add/编译原理-新课程

[Agent] ✅ 完成！新课程已创建，请前往 GitHub 创建 PR
```

---

## 十二、错误处理

| 错误情况 | 处理方式 |
|----------|----------|
| 文件超过 100MB | 提示用户压缩/拆分，或使用网盘链接方案 |
| 无法识别课程 | 使用交互提问工具让用户确认/输入课程名（例如 AskUserQuestion） |
| Git 推送失败 | 检查远程仓库配置，提示用户检查 Fork 状态 |
| MDX 文件不存在 | 先创建 MDX（使用模板），再添加内容 |
| 目标目录不存在 | Bash mkdir -p 创建目录 |
| 文件名冲突 | 在文件名后加 `_v2` 或时间戳 |

---

## 附录：MDX 页面模板

```mdx
import { FileDownload } from '@/components/FileDownload'
import { Comments } from '@/components/Comments'

# 📚 课程中文名

> 本页面收集了XXX课程的相关资料

## 📝 期末考试

---

## 📝 期中考试

---

## 📚 复习资料

---

## 📖 课堂笔记

---

## 💡 作业习题

---

<Comments />
```

---

**文档版本**: v2.0
**最后更新**: 2026-03-21
**适用**: Agent 直接操作，不依赖自动化脚本
