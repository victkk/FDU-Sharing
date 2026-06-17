"""Git管理模块 - 负责Git操作和PR创建"""

import subprocess
import sys
from pathlib import Path
from typing import Optional, List, Tuple


class GitManager:
    """Git操作管理器"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.check_git_repo()
    
    def check_git_repo(self):
        """检查是否在Git仓库中"""
        try:
            self._run_command(['git', 'rev-parse', '--git-dir'], check=True, capture=True)
        except subprocess.CalledProcessError:
            raise RuntimeError("当前目录不是Git仓库")
    
    def _run_command(self, cmd: List[str], check: bool = False, 
                    capture: bool = False) -> Tuple[int, str, str]:
        """
        运行命令
        
        返回: (返回码, stdout, stderr)
        """
        try:
            if capture:
                result = subprocess.run(
                    cmd,
                    cwd=self.project_root,
                    capture_output=True,
                    text=True,
                    check=check
                )
                return result.returncode, result.stdout.strip(), result.stderr.strip()
            else:
                result = subprocess.run(
                    cmd,
                    cwd=self.project_root,
                    check=check
                )
                return result.returncode, "", ""
        except subprocess.CalledProcessError as e:
            if capture:
                return e.returncode, e.stdout.strip() if e.stdout else "", e.stderr.strip() if e.stderr else ""
            else:
                return e.returncode, "", str(e)
    
    def get_current_branch(self) -> str:
        """获取当前分支名"""
        code, stdout, _ = self._run_command(['git', 'branch', '--show-current'], capture=True)
        if code == 0:
            return stdout
        return "unknown"
    
    def check_clean_working_tree(self) -> bool:
        """检查工作区是否干净"""
        code, stdout, _ = self._run_command(['git', 'status', '--porcelain'], capture=True)
        return code == 0 and not stdout
    
    def create_branch(self, branch_name: str) -> Tuple[bool, str]:
        """
        创建新分支
        
        返回: (是否成功, 错误信息)
        """
        # 检查分支是否已存在
        code, _, _ = self._run_command(['git', 'show-ref', '--verify', f'refs/heads/{branch_name}'], capture=True)
        if code == 0:
            return False, f"分支 {branch_name} 已存在"
        
        # 创建并切换到新分支
        code, _, stderr = self._run_command(['git', 'checkout', '-b', branch_name], capture=True)
        if code != 0:
            return False, f"创建分支失败: {stderr}"
        
        return True, ""
    
    def add_files(self, file_paths: List[str]) -> Tuple[bool, str]:
        """
        添加文件到暂存区
        
        返回: (是否成功, 错误信息)
        """
        try:
            for file_path in file_paths:
                code, _, stderr = self._run_command(['git', 'add', file_path], capture=True)
                if code != 0:
                    return False, f"添加文件失败: {stderr}"
            return True, ""
        except Exception as e:
            return False, str(e)
    
    def commit(self, message: str) -> Tuple[bool, str]:
        """
        提交更改
        
        返回: (是否成功, 错误信息)
        """
        code, _, stderr = self._run_command(['git', 'commit', '-m', message], capture=True)
        if code != 0:
            return False, f"提交失败: {stderr}"
        return True, ""
    
    def push(self, branch_name: str, remote: str = 'origin') -> Tuple[bool, str]:
        """
        推送分支到远程
        
        返回: (是否成功, 错误信息)
        """
        code, _, stderr = self._run_command(
            ['git', 'push', '-u', remote, branch_name], 
            capture=True
        )
        if code != 0:
            return False, f"推送失败: {stderr}"
        return True, ""
    
    def check_gh_cli(self) -> bool:
        """检查是否安装了GitHub CLI"""
        code, _, _ = self._run_command(['gh', '--version'], capture=True)
        return code == 0
    
    def check_gh_auth(self) -> bool:
        """检查GitHub CLI是否已认证"""
        code, _, _ = self._run_command(['gh', 'auth', 'status'], capture=True)
        return code == 0
    
    def is_fork(self) -> bool:
        """检查当前仓库是否是fork"""
        if not self.check_gh_cli():
            return False
        
        code, stdout, _ = self._run_command(['gh', 'repo', 'view', '--json', 'isFork', '-q', '.isFork'], capture=True)
        return code == 0 and stdout.strip().lower() == 'true'
    
    def get_upstream_repo(self) -> Optional[str]:
        """获取上游仓库（如果是fork）"""
        if not self.check_gh_cli():
            return None
        
        code, stdout, _ = self._run_command(
            ['gh', 'repo', 'view', '--json', 'parent', '-q', '.parent.nameWithOwner'], 
            capture=True
        )
        if code == 0 and stdout.strip():
            return stdout.strip()
        return None
    
    def create_pr(self, title: str, body: str, branch_name: str) -> Tuple[bool, str]:
        """
        使用GitHub CLI创建PR
        
        返回: (是否成功, PR URL或错误信息)
        """
        if not self.check_gh_cli():
            return False, "未安装 GitHub CLI (gh)，请先安装: https://cli.github.com/"
        
        if not self.check_gh_auth():
            return False, "GitHub CLI 未认证，请运行: gh auth login"
        
        # 检查是否是fork
        is_fork = self.is_fork()
        
        if not is_fork:
            # 不是fork，给出提示
            owner, repo = self.get_repo_info()
            if owner and repo:
                return False, (
                    f"⚠️  当前仓库不是fork，无法自动创建PR\n\n"
                    f"请按以下步骤操作：\n"
                    f"1. 访问 https://github.com/{owner}/{repo}\n"
                    f"2. 点击右上角 'Fork' 按钮创建你的fork\n"
                    f"3. 将你的更改推送到fork\n"
                    f"4. 在GitHub上手动创建Pull Request\n\n"
                    f"或者直接访问：\n"
                    f"https://github.com/{owner}/{repo}/compare/master...{branch_name}"
                )
            else:
                return False, "无法确定仓库信息，请手动在GitHub上创建PR"
        
        # 获取上游仓库
        upstream = self.get_upstream_repo()
        
        # 构建PR创建命令
        cmd = [
            'gh', 'pr', 'create',
            '--title', title,
            '--body', body,
        ]
        
        # 如果是fork，指定base仓库
        if upstream:
            cmd.extend(['--repo', upstream])
        
        code, stdout, stderr = self._run_command(cmd, capture=True)
        if code != 0:
            # 提供手动创建PR的链接
            owner, repo = self.get_repo_info()
            upstream_info = self.get_upstream_repo()
            
            error_msg = f"创建PR失败: {stderr}\n\n"
            
            if upstream_info:
                error_msg += f"你可以手动创建PR：\n"
                error_msg += f"https://github.com/{upstream_info}/compare/master...{owner}:{branch_name}"
            elif owner and repo:
                error_msg += f"你可以手动创建PR：\n"
                error_msg += f"https://github.com/{owner}/{repo}/pull/new/{branch_name}"
            
            return False, error_msg
        
        # 从输出中提取PR URL
        pr_url = stdout.split('\n')[-1] if stdout else ""
        return True, pr_url
    
    def get_repo_info(self) -> Tuple[Optional[str], Optional[str]]:
        """
        获取仓库信息
        
        返回: (owner, repo_name) 或 (None, None)
        """
        code, stdout, _ = self._run_command(
            ['git', 'config', '--get', 'remote.origin.url'], 
            capture=True
        )
        
        if code != 0 or not stdout:
            return None, None
        
        # 解析Git URL
        # 格式: https://github.com/owner/repo.git 或 git@github.com:owner/repo.git
        url = stdout
        
        if 'github.com' in url:
            if url.startswith('https://'):
                # https://github.com/owner/repo.git
                parts = url.replace('https://github.com/', '').replace('.git', '').split('/')
            elif url.startswith('git@'):
                # git@github.com:owner/repo.git
                parts = url.replace('git@github.com:', '').replace('.git', '').split('/')
            else:
                return None, None
            
            if len(parts) >= 2:
                return parts[0], parts[1]
        
        return None, None
    
    def restore_branch(self, original_branch: str):
        """恢复到原分支"""
        self._run_command(['git', 'checkout', original_branch], capture=True)
    
    def delete_branch(self, branch_name: str):
        """删除分支"""
        self._run_command(['git', 'branch', '-D', branch_name], capture=True)
    
    def generate_branch_name(self, course_name: str) -> str:
        """
        生成分支名
        格式: add/课程名-YYYYMMDD-HHMMSS
        """
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        # 移除特殊字符
        safe_name = course_name.replace(' ', '-').replace('/', '-')
        return f"add/{safe_name}-{timestamp}"
    
    def generate_commit_message(self, courses: List[str], file_count: int) -> str:
        """
        生成提交信息
        """
        if len(courses) == 1:
            return f"添加: {courses[0]} - {file_count}个文件"
        else:
            course_list = "、".join(courses[:3])
            if len(courses) > 3:
                course_list += f"等{len(courses)}门课程"
            return f"添加: {course_list} - 共{file_count}个文件"
    
    def generate_pr_body(self, file_info_list: List[Tuple[str, str, str]]) -> str:
        """
        生成PR描述
        
        参数:
            file_info_list: [(课程名, 文件名, 资料类型), ...]
        """
        # 按课程分组
        courses = {}
        for course, filename, file_type in file_info_list:
            if course not in courses:
                courses[course] = []
            courses[course].append((filename, file_type))
        
        # 生成Markdown表格
        body = "## 📝 PR 说明\n\n"
        body += "### 本次提交类型\n\n"
        body += "- [x] 📚 添加新资料\n"
        body += "- [ ] ✏️ 修正错误\n"
        body += "- [ ] 🆕 添加新课程\n"
        body += "- [ ] 🔧 其他改进\n\n"
        
        body += "### 资料清单\n\n"
        
        for course_name, files in courses.items():
            body += f"#### 📘 {course_name}\n\n"
            body += "| 文件名 | 类型 |\n"
            body += "|--------|------|\n"
            
            for filename, file_type in files:
                body += f"| {filename} | {file_type} |\n"
            
            body += "\n"
        
        body += "### Checklist\n\n"
        body += "- [x] 文件已放入正确的目录\n"
        body += "- [x] 已在对应的 `.mdx` 文件中添加下载链接\n"
        body += "- [x] 资料内容清晰可读\n"
        body += "- [x] 确认无版权问题\n\n"
        
        body += "---\n\n"
        body += "*此PR由 easy_pr.py 脚本自动生成*\n"
        
        return body
