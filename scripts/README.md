# Easy PR 脚本使用文档

## 📖 概述

`easy_pr.py` 是一个自动化工具，用于简化向 FDU-Sharing 项目贡献资料的流程。它会自动处理文件移动、MDX文件更新、Git操作和PR创建。

## 🔧 安装

### 1. Fork并克隆仓库

**重要：必须先Fork仓库！**

```bash
# 1. 在GitHub上Fork仓库
#    访问 https://github.com/victkk/FDU-Sharing
#    点击右上角的 "Fork" 按钮

# 2. 克隆你的fork到本地
git clone https://github.com/你的用户名/FDU-Sharing.git
cd FDU-Sharing
```

### 2. 安装Python依赖

```bash
pip install -r scripts/requirements.txt
```

需要的依赖：
- `questionary` - 交互式命令行界面
- `colorama` - 彩色终端输出
- `gitpython` - Git操作（可选）
- `PyGithub` - GitHub API（可选）

### 3. 安装 GitHub CLI（推荐）

用于自动创建PR：

```bash
# macOS
brew install gh

# Linux
sudo apt install gh

# Windows
winget install GitHub.cli

# 认证
gh auth login
```

## 🚀 快速开始

### 基本流程

1. **准备资料文件**
   ```bash
   # 将文件放入 upload/ 目录
   upload/
   ├── 数据结构/
   │   ├── 2024-期末-试卷.pdf
   │   └── 2024-期末-答案.pdf
   └── 线性代数/
       └── 2024-复习-总结.pdf
   ```

2. **运行脚本**
   ```bash
   python scripts/easy_pr.py
   ```

3. **按提示操作**
   - 查看扫描到的文件
   - 选择要处理的文件
   - 为每个文件选择课程和类型
   - 确认文件名
   - 预览并确认操作
   - 等待PR创建完成

## 📋 详细步骤

### 步骤1: 扫描文件

脚本会自动扫描 `upload/` 目录并显示：
- 文件名和大小
- 智能识别的课程提示
- 识别的资料类型和年份
- 文件验证结果（大小、格式等）

**智能识别规则：**
- 如果文件在子目录中，目录名作为课程提示
- 文件名中的4位数字识别为年份（如2024）
- 关键词识别：
  - "期末"/"final" → 期末考试
  - "期中"/"midterm" → 期中考试
  - "复习"/"review" → 复习资料
  - "笔记"/"note" → 课堂笔记
  - "作业"/"homework"/"hw" → 作业习题

### 步骤2: 选择文件

使用空格键选择/取消选择文件，回车确认。

可以：
- 全选所有文件
- 只选择部分文件
- 跳过无效文件

### 步骤3: 配置文件信息

对每个选中的文件：

#### 3.1 选择课程

选项包括：
- 所有已有课程（显示状态✅/📝）
- "➕ 创建新课程"

如果创建新课程，需要提供：
- **课程中文名**：如"编译原理"
- **课程拼音名**：如"bianyiyuanli"（用于URL）
- **Emoji**：如"⚙️"（可选，默认📚）

#### 3.2 选择资料类型

选项：
- 期末考试
- 期中考试
- 复习资料
- 课堂笔记
- 作业习题
- PPT课件
- 其他

#### 3.3 确认文件名

脚本会根据规范建议文件名：
```
[年份]-[类型]-[描述].pdf
```

例如：
- `2024-期末-试卷.pdf`
- `2024-复习-知识点总结.pdf`

你可以接受建议或自定义。

### 步骤4: 预览操作

脚本会显示将要执行的所有操作：
```
📋 操作预览:

📘 数据结构
   ├─ 2024-期末-试卷.pdf (期末考试)
   └─ 2024-期末-答案.pdf (期末考试)

📘 线性代数
   └─ 2024-复习-总结.pdf (复习资料)
```

确认无误后继续。

### 步骤5: Git操作

脚本会自动：
1. 创建新分支（格式：`add/课程名-时间戳`）
2. 移动文件到 `public/resources/课程名/`
3. 更新对应的 `pages/courses/拼音名.mdx`
4. 添加文件到Git暂存区
5. 创建提交（格式：`添加: 课程名 - N个文件`）
6. 推送到你的远程仓库

### 步骤6: 创建PR

如果安装了 `gh` CLI，脚本会自动创建PR：
- 生成规范的PR标题
- 生成详细的PR描述（包含资料清单表格）
- 显示PR链接

如果没有 `gh` CLI，脚本会提示你手动创建PR。

### 步骤7: 清理

成功后，脚本会询问是否删除 `upload/` 中已处理的文件。

## 🎯 使用示例

### 示例1: 添加单个课程的资料

```bash
# 1. 准备文件
mkdir -p upload/数据结构
cp ~/Downloads/期末试卷.pdf upload/数据结构/

# 2. 运行脚本
python scripts/easy_pr.py

# 3. 交互过程：
# - 选择文件：[x] 期末试卷.pdf
# - 选择课程：数据结构
# - 选择类型：期末考试
# - 确认文件名：2024-期末-试卷.pdf
# - 确认操作：是
# - 等待PR创建...

# 4. 完成！
```

### 示例2: 批量添加多门课程

```bash
# 1. 准备文件
upload/
├── 数据结构/
│   ├── 2024-期末-试卷.pdf
│   └── 2024-期末-答案.pdf
├── 算法/
│   └── 2024-复习-总结.pdf
└── 线性代数/
    └── 2023-期中-试卷.pdf

# 2. 运行脚本
python scripts/easy_pr.py

# 3. 全选文件，逐个配置
# 4. 一次性创建包含所有课程的PR
```

### 示例3: 创建新课程

```bash
# 1. 准备新课程资料
mkdir -p upload/编译原理
cp ~/course_files/* upload/编译原理/

# 2. 运行脚本
python scripts/easy_pr.py

# 3. 选择 "➕ 创建新课程"
#    - 中文名：编译原理
#    - 拼音名：bianyiyuanli
#    - Emoji：⚙️

# 4. 脚本会自动：
#    - 创建 public/resources/编译原理/
#    - 创建 pages/courses/bianyiyuanli.mdx
#    - 更新 pages/courses/_meta.ts
```

## ⚙️ 高级功能

### 文件命名建议

脚本会智能分析原文件名并建议规范名称：

原文件名 → 建议名称：
- `final_exam.pdf` → `2024-期末-试卷.pdf`
- `数据结构期末2024.pdf` → `2024-期末-试卷.pdf`
- `review_notes.pdf` → `2024-复习-笔记.pdf`

### 自动章节分类

根据资料类型，自动添加到MDX的对应章节：
- 期末考试 → `## 📝 期末考试`
- 期中考试 → `## 📝 期中考试`
- 复习资料 → `## 📚 复习资料`
- 课堂笔记 → `## 📖 课堂笔记`
- 作业习题 → `## 💡 作业习题`
- PPT课件 → `## 📊 PPT课件`

如果章节不存在，会自动创建。

### 重复检测

脚本会检查：
- 文件是否已存在于MDX中
- 避免重复添加相同文件

### 错误处理

- 文件大小超限（>100MB）→ 警告并跳过
- 不支持的格式 → 警告并跳过
- Git操作失败 → 自动回滚
- 网络问题 → 保留本地更改，提示手动PR

## ❓ 常见问题

### Q: 提示"当前仓库不是fork"怎么办？

A: 你需要先Fork仓库：
1. 访问 https://github.com/victkk/FDU-Sharing
2. 点击右上角 "Fork" 按钮
3. 克隆你的fork：
   ```bash
   git clone https://github.com/你的用户名/FDU-Sharing.git
   ```

### Q: 没有安装 gh CLI 怎么办？

A: 脚本会自动完成除创建PR外的所有操作，你可以：
1. 访问 GitHub 仓库
2. 手动创建 Pull Request
3. 选择刚推送的分支

### Q: 文件太大超过100MB？

A: 
- 压缩文件
- 拆分为多个文件
- 在PR中提供网盘链接

### Q: 如何撤销操作？

A:
```bash
# 删除分支
git branch -D add/xxx

# 如果已推送
git push origin --delete add/xxx
```

### Q: 可以一次处理不同课程吗？

A: 可以！脚本支持在一个PR中添加多门课程的资料。

### Q: 脚本支持哪些文件格式？

A: PDF, Word, PPT, Excel, ZIP, 图片等常见格式。

### Q: 如何处理中文文件名？

A: 完全支持中文文件名，无需担心。

### Q: 遇到错误怎么办？

A: 
1. 查看错误信息
2. 检查网络连接
3. 确认Git配置正确
4. 提交Issue寻求帮助

## 🔍 技术细节

### 项目结构

```
scripts/
├── easy_pr.py              # 主脚本
├── requirements.txt        # Python依赖
└── utils/
    ├── __init__.py
    ├── course_manager.py   # 课程管理
    ├── file_manager.py     # 文件处理
    ├── mdx_editor.py       # MDX编辑
    └── git_manager.py      # Git操作
```

### 工作流程

```
1. 扫描文件 (FileManager)
   ↓
2. 用户选择和配置 (questionary)
   ↓
3. 课程匹配/创建 (CourseManager)
   ↓
4. 移动文件 (FileManager)
   ↓
5. 更新MDX (MDXEditor)
   ↓
6. Git提交 (GitManager)
   ↓
7. 创建PR (GitManager + gh CLI)
```

## 🤝 贡献

欢迎改进这个脚本！可以：
- 添加新功能
- 改进用户体验
- 修复Bug
- 完善文档

## 📝 许可

与 FDU-Sharing 项目相同的许可协议。
