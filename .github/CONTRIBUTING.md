# 贡献指南

感谢你对 FDU Sharing 的关注！我们欢迎所有形式的贡献。

## 🚀 如何贡献

### 添加资料

1. **Fork** 本仓库到你的账号
2. **Clone** 到本地：`git clone https://github.com/你的用户名/FDU-Sharing.git`
3. 创建新分支：`git checkout -b add/课程名-资料描述`
4. 将资料文件放入 `public/resources/课程名/` 目录
5. 编辑 `pages/courses/课程名.mdx`，添加下载链接
6. 提交更改：`git commit -m "添加：课程名 - 资料描述"`
7. 推送分支：`git push origin add/课程名-资料描述`
8. 创建 Pull Request

### 文件命名规范

```
[年份]-[类型]-[描述].pdf

示例：
2023-期末-试卷.pdf
2023-期中-答案.pdf
2024-复习-知识点总结.pdf
```

### 添加下载链接

在对应课程的 `.mdx` 文件中添加：

```mdx
<FileDownload 
  name="2023年期末试卷" 
  path="/resources/课程名/2023-期末-试卷.pdf"
  date="2023-12"
/>
```

## 📋 资料要求

- ✅ 内容清晰可读
- ✅ 遵循命名规范
- ✅ 如有原作者请标注
- ❌ 不上传有版权争议的资料
- ❌ 不用于商业用途

## 🆕 添加新课程

1. 在 `public/resources/` 下创建新目录
2. 在 `pages/courses/` 下创建新的 `.mdx` 文件
3. 在 `pages/courses/_meta.ts` 中添加课程条目

## 🐛 报告问题

如发现问题，请提交 Issue 并包含以下信息：
- 问题描述
- 复现步骤（如适用）
- 截图（如适用）

## 💬 交流讨论

欢迎在 GitHub Discussions 中交流讨论！

---

再次感谢你的贡献！🙏


