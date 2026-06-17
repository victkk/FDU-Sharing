# Agent 目录

本目录用于 AI Agent 辅助贡献资料到 FDU-Sharing 项目。

## 文件说明

- **AGENT_GUIDE.md** - Agent 操作指南，完整的操作流程和规范
- **README.md** - 本文件

## 使用方式

### 方式一：让 AI Agent 读取指南

将以下提示词提供给 AI Agent（如 Claude Code）：

```
请读取 Agent/AGENT_GUIDE.md 文件，然后帮我添加课程资料。
```

### 方式二：直接提供文件

你可以：
1. 将需要上传的资料文件放在本目录
2. 告诉 AI Agent 文件位置和课程信息
3. Agent 将按照 AGENT_GUIDE.md 的规范处理

## 注意事项

- AI Agent 会直接操作你的仓库，请确保已 Fork 并拥有相应权限
- 资料文件会被移动到 `public/resources/课程中文名/` 目录
- 本目录仅作为临时存放区，处理后文件会被移动

---

更多详情请参考 [AGENT_GUIDE.md](./AGENT_GUIDE.md)
