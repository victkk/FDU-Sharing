# 贡献指南

感谢你对 FDU Sharing 的关注！我们欢迎课程资料、考试回忆、复习笔记、作业参考和页面修正等贡献。所有资料仅供学习交流使用，请勿用于商业用途。

## 🚀 如何贡献

### 添加资料

1. **Fork** 本仓库到你的账号；
2. **Clone** 到本地：`git clone https://github.com/你的用户名/FDU-Sharing.git`；
3. 创建新分支：`git checkout -b add/课程名-资料描述`；
4. 将资料文件放入 `public/resources/课程中文名/` 目录；
5. 编辑对应课程页面 `pages/courses/课程拼音名.mdx`，添加下载链接；
6. 如果是新课程，同时在 `pages/courses/_meta.ts` 中注册课程；
7. 提交并推送分支，然后创建 Pull Request。

### 自动化脚本

也可以将资料放入 `upload/` 后运行：

```bash
pip install -r scripts/requirements.txt
python scripts/easy_pr.py
```

脚本会引导完成课程识别、文件移动、页面更新和 PR 创建。

## 📁 文件放置规范

资料文件放入中文课程目录：

```text
public/resources/课程中文名/年份-类型-描述.扩展名
```

示例：

```text
public/resources/数据结构/2024-期末-试卷.pdf
public/resources/人工智能的软件基础/2026春-期末-试题.md
```

## 🏷️ 文件命名规范

```text
[年份]-[类型]-[描述].扩展名
```

常见类型包括：`期末`、`期中`、`复习`、`作业`、`笔记`、`实验`。

示例：

```text
2023-期末-试卷.pdf
2023-期中-答案.pdf
2024-复习-知识点总结.pdf
2026春-期末-试题.md
```

## 🔗 添加下载链接

在对应课程的 `.mdx` 文件中添加：

```mdx
<FileDownload 
  name="2024年期末试卷" 
  path="/resources/数据结构/2024-期末-试卷.pdf" 
/>
```

## 🆕 添加新课程

1. 在 `public/resources/` 下创建新课程资料目录，例如 `public/resources/编译原理/`；
2. 在 `pages/courses/` 下创建拼音命名的课程页面，例如 `bianyiyuanli.mdx`；
3. 在 `pages/courses/_meta.ts` 中添加课程条目，例如 `'bianyiyuanli': '⚙️ 编译原理'`。

课程页面可以参考：

```mdx
import { FileDownload } from '@/components/FileDownload'
import { Comments } from '@/components/Comments'

# 📚 课程中文名

> 本页面收集了课程中文名课程的相关资料

## 📝 期末考试

<FileDownload
  name="2024年期末试卷"
  path="/resources/课程中文名/2024-期末-试卷.pdf"
/>

---

## 📝 期中考试

---

## 📚 复习资料

---

<Comments />
```

## 📋 资料要求

- ✅ 内容清晰可读；
- ✅ 文件命名清楚，包含年份、类型和简短描述；
- ✅ 如有原作者或资料来源，请在 PR 中说明；
- ❌ 不上传包含个人隐私的信息；
- ❌ 不上传有明显版权争议的资料；
- ❌ 不将资料用于商业用途。

## ✅ Pull Request Checklist

- [ ] 文件已放入 `public/resources/课程中文名/`；
- [ ] 文件名符合命名规范；
- [ ] 已在对应课程 `.mdx` 页面添加 `FileDownload` 链接；
- [ ] 新课程已在 `pages/courses/_meta.ts` 注册；
- [ ] PR 说明中写明课程、资料类型、年份和来源。

## 🐛 报告问题

如发现问题，请提交 Issue 并包含以下信息：

- 问题描述；
- 复现步骤（如适用）；
- 截图（如适用）。

---

再次感谢你的贡献！🙏
