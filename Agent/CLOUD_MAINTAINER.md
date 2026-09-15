# GitHub 云端维护助手

本仓库的 `.github/workflows/maintainer.yml` 在 GitHub 托管 runner 上运行，无需个人电脑在线。

- PR 新建、更新、重新打开或转为 ready 时审核，每小时第 17 分补查未处理的 PR。
- 使用 OpenToken Responses API；模型由仓库变量 `AGENT_MODEL` 指定。
- 自动审核资料、页面、文档和网站修复，尝试解决普通文本冲突。
- 生成保留双方历史的临时合并提交；独立 runner 构建成功、源分支和主分支未变化、无 changes requested、外部检查通过后合并。
- 仅对明确跳转到 `https://vercel.com/git/authorize` 的 Vercel 授权失败采用独立构建结果；其他失败或未完成检查会阻止合并。
- 合并提交作者和提交者：`victkk <zhangzc.fdfz@gmail.com>`；原贡献者提交保持不变。评论显示为 `github-actions[bot]`。
- Issue 新建、修改、重新打开或有人新增评论时，根据贡献指南和仓库信息回复；同一问题内容不重复回复。不自动关闭 issue。

## 凭据与权限

仅保存模型令牌到 Actions secret `OPENTOKEN_API_KEY`；接口地址保存在变量 `OPENTOKEN_BASE_URL`。
不复制本机 GitHub OAuth token、SSH 私钥或整个 Codex 配置。

模型通过受控 API 调用接收文本数据，无 shell、网络工具或 GitHub 凭据。控制脚本始终从主分支读取，不执行 PR 中的脚本。
构建任务不带模型 secret、GitHub 写令牌或持久化 Git 凭据。

## 冲突与合并

fork 的 PR 也会生成本仓库临时分支 `agent/merge-pr-*`，无需 fork 写权限。
合并提交包含原 PR 的 head 作为父提交。主分支只接收经过验证的后继提交，并在推送时再次比较主分支版本；不会覆盖其他人的更新。
GitHub 按提交可达性识别原 PR 的合并。成功后删除临时分支；失败时保留分支方便维护者检查。
若以后启用主分支保护且禁止机器人推送，规则会阻止自动合并，需要维护者调整授权方式，助手不会绕过保护。

## 需要人工处理的情况

自动化自身的策略/工作流、符号链接/可执行文件/子模块、超过审核上下文限制的变更、无法确定意图的冲突，以及审核或构建失败时不会自动合并，PR 中会留下原因或 Actions 中会报告错误。
二进制资料只检查元数据，无法替代人工对内容、来源及版权的检查。

## 运维

在 Actions → FDU Sharing Maintainer → Run workflow 可立即补查；填写 PR number 可强制重新审核该 PR。
编辑仓库变量可更换兼容模型或 endpoint；更新 secret 可轮换令牌。禁用该 workflow 即停止自动维护。
GitHub 可能延迟定时任务，并可能停用长期无活动的公开仓库定时任务；PR/issue 事件仍可触发。

验证控制器：`python -m unittest discover -s .github/agent -p 'test_*.py' -v`。
