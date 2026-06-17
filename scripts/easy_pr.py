#!/usr/bin/env python3
"""
FDU-Sharing 简便PR工具
用于快速上传资料并创建Pull Request

使用方法:
    1. 将资料放入 upload/ 目录
    2. 运行: python scripts/easy_pr.py
    3. 按照提示完成交互
"""

import sys
import os
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Tuple

try:
    import questionary
    from questionary import Choice
    from colorama import init, Fore, Style
except ImportError:
    print("❌ 缺少依赖，请先安装:")
    print("   pip install -r scripts/requirements.txt")
    sys.exit(1)

# 初始化colorama
init(autoreset=True)

# 添加项目根目录到Python路径
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.utils import CourseManager, FileManager, MDXEditor, GitManager


class EasyPR:
    """简便PR工具主类"""
    
    def __init__(self):
        self.project_root = PROJECT_ROOT
        self.course_manager = CourseManager(self.project_root)
        self.file_manager = FileManager(self.project_root)
        self.git_manager = GitManager(self.project_root)
        
        # 资料类型选项
        self.resource_types = [
            '期末考试',
            '期中考试',
            '复习资料',
            '课堂笔记',
            '作业习题',
            'PPT课件',
            '其他'
        ]
        
        # 处理结果
        self.processed_files: List[Tuple[str, str, str, str, str]] = []  # (课程中文名, 课程拼音, 文件名, 文件路径, 资料类型)
    
    def print_banner(self):
        """打印欢迎横幅"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"{Fore.CYAN}  🎓 FDU-Sharing 简便PR工具")
        print(f"{Fore.CYAN}{'='*60}\n")
    
    def print_step(self, step: int, total: int, message: str):
        """打印步骤信息"""
        print(f"\n{Fore.YELLOW}[{step}/{total}] {message}{Style.RESET_ALL}")
    
    def run(self):
        """运行主流程"""
        self.print_banner()
        
        # 步骤1: 扫描文件
        self.print_step(1, 6, "扫描上传目录...")
        files = self.file_manager.scan_upload_dir()
        
        if not files:
            print(f"{Fore.RED}❌ upload/ 目录中没有找到文件")
            print(f"{Fore.YELLOW}💡 请将要上传的资料放入 upload/ 目录")
            return
        
        print(f"{Fore.GREEN}✅ 找到 {len(files)} 个文件\n")
        
        # 显示文件列表
        for i, file_info in enumerate(files, 1):
            # 验证文件
            is_valid, error = self.file_manager.validate_file(file_info)
            status = f"{Fore.GREEN}✓" if is_valid else f"{Fore.RED}✗"
            print(f"  {status} {i}. {self.file_manager.get_file_display_name(file_info)}")
            if not is_valid:
                print(f"     {Fore.RED}  {error}")
        
        print()
        
        # 过滤有效文件
        valid_files = [f for f in files if self.file_manager.validate_file(f)[0]]
        
        if not valid_files:
            print(f"{Fore.RED}❌ 没有有效的文件可以处理")
            return
        
        if len(valid_files) < len(files):
            if not questionary.confirm(
                f"发现 {len(files) - len(valid_files)} 个无效文件，是否继续处理其他文件？"
            ).ask():
                return
        
        # 步骤2: 选择要处理的文件
        self.print_step(2, 6, "选择要处理的文件")
        
        file_choices = [
            Choice(
                title=self.file_manager.get_file_display_name(f),
                value=f,
                checked=True
            )
            for f in valid_files
        ]
        
        selected_files = questionary.checkbox(
            "选择文件（空格选择，回车确认）:",
            choices=file_choices
        ).ask()
        
        if not selected_files:
            print(f"{Fore.YELLOW}⚠️  未选择任何文件，退出")
            return
        
        print(f"{Fore.GREEN}✅ 已选择 {len(selected_files)} 个文件")
        
        # 步骤3: 处理每个文件
        self.print_step(3, 6, "配置文件信息")
        
        for file_info in selected_files:
            if not self.process_file(file_info):
                if not questionary.confirm("处理失败，是否继续处理其他文件？").ask():
                    return
        
        if not self.processed_files:
            print(f"{Fore.RED}❌ 没有成功处理的文件")
            return
        
        # 步骤4: 预览操作
        self.print_step(4, 6, "预览操作")
        self.preview_changes()
        
        if not questionary.confirm("确认执行以上操作？").ask():
            print(f"{Fore.YELLOW}⚠️  操作已取消")
            return
        
        # 步骤5: 执行Git操作
        self.print_step(5, 6, "创建Git分支并提交")
        
        if not self.create_git_commit():
            print(f"{Fore.RED}❌ Git操作失败")
            return
        
        # 步骤6: 创建PR
        self.print_step(6, 6, "创建Pull Request")
        
        if self.create_pull_request():
            print(f"\n{Fore.GREEN}{'='*60}")
            print(f"{Fore.GREEN}  ✅ 成功！PR已创建")
            print(f"{Fore.GREEN}{'='*60}\n")
            
            # 询问是否清理upload目录
            if questionary.confirm("是否删除已处理的文件？").ask():
                for file_info in selected_files:
                    self.file_manager.delete_file(file_info)
                print(f"{Fore.GREEN}✅ 已清理上传目录")
        else:
            print(f"\n{Fore.YELLOW}⚠️  PR创建失败，但文件已提交到分支")
            print(f"{Fore.YELLOW}   你可以手动在GitHub上创建PR")
    
    def process_file(self, file_info) -> bool:
        """处理单个文件"""
        print(f"\n{Fore.CYAN}📄 处理文件: {file_info.name}")
        
        # 1. 选择课程
        course_hint = file_info.course_hint or ""
        course_choices = self.course_manager.get_course_choices()
        
        # 如果有课程提示，设为默认选项
        default = None
        if course_hint:
            for choice in course_choices:
                if course_hint in choice:
                    default = choice
                    break
        
        course_choice = questionary.select(
            "选择课程:",
            choices=course_choices,
            default=default
        ).ask()
        
        if not course_choice:
            return False
        
        # 解析课程信息
        course_info = self.course_manager.parse_choice(course_choice)
        
        if course_info is None:
            # 创建新课程
            chinese_name = questionary.text(
                "输入课程中文名:",
                default=course_hint or ""
            ).ask()
            
            if not chinese_name:
                return False
            
            pinyin = questionary.text(
                "输入课程拼音名（用于URL）:",
                validate=lambda x: len(x) > 0 and x.replace('_', '').replace('-', '').isalnum()
            ).ask()
            
            if not pinyin:
                return False
            
            emoji = questionary.text(
                "输入课程emoji（可选）:",
                default="📚"
            ).ask() or "📚"
            
            # 创建课程
            if not self.course_manager.create_course(chinese_name, pinyin, emoji):
                return False
            
            course_info = (pinyin, chinese_name)
        
        pinyin, chinese_name = course_info
        
        # 2. 选择资料类型
        type_hint = file_info.type_hint
        default_type = type_hint if type_hint in self.resource_types else self.resource_types[0]
        
        resource_type = questionary.select(
            "选择资料类型:",
            choices=self.resource_types,
            default=default_type
        ).ask()
        
        if not resource_type:
            return False
        
        # 3. 确认/编辑文件名
        suggested_name = self.file_manager.suggest_filename(
            file_info,
            year=file_info.year_hint,
            file_type=resource_type
        )
        
        final_name = questionary.text(
            "确认文件名:",
            default=suggested_name
        ).ask()
        
        if not final_name:
            return False
        
        # 4. 移动文件
        success, result = self.file_manager.move_file(file_info, chinese_name, final_name)
        
        if not success:
            print(f"{Fore.RED}❌ {result}")
            return False
        
        file_path = result
        print(f"{Fore.GREEN}✅ 文件已移动: {file_path}")
        
        # 5. 更新MDX文件
        mdx_path = self.course_manager.get_course_page_path(pinyin)
        
        try:
            editor = MDXEditor(mdx_path)
            
            # 提取显示名称（不含年份和类型前缀）
            display_name = final_name
            # 移除扩展名
            display_name = Path(display_name).stem
            
            if editor.add_file_download(display_name, file_path, resource_type):
                editor.format_content()
                editor.save()
                print(f"{Fore.GREEN}✅ 已更新课程页面")
            else:
                print(f"{Fore.YELLOW}⚠️  更新课程页面失败")
                
        except Exception as e:
            print(f"{Fore.RED}❌ 编辑MDX文件出错: {e}")
            return False
        
        # 记录处理结果
        self.processed_files.append((
            chinese_name,
            pinyin,
            final_name,
            file_path,
            resource_type
        ))
        
        return True
    
    def preview_changes(self):
        """预览将要执行的操作"""
        print(f"\n{Fore.CYAN}📋 操作预览:\n")
        
        # 按课程分组
        courses = {}
        for chinese_name, pinyin, filename, filepath, resource_type in self.processed_files:
            if chinese_name not in courses:
                courses[chinese_name] = []
            courses[chinese_name].append((filename, resource_type))
        
        for course_name, files in courses.items():
            print(f"{Fore.YELLOW}📘 {course_name}")
            for filename, resource_type in files:
                print(f"   ├─ {filename} ({resource_type})")
        
        print()
    
    def create_git_commit(self) -> bool:
        """创建Git提交"""
        try:
            # 获取当前分支（备份）
            original_branch = self.git_manager.get_current_branch()
            
            # 生成分支名
            courses = list(set([c[0] for c in self.processed_files]))
            branch_name = self.git_manager.generate_branch_name(courses[0])
            
            print(f"📌 创建分支: {branch_name}")
            
            # 创建分支
            success, error = self.git_manager.create_branch(branch_name)
            if not success:
                print(f"{Fore.RED}❌ {error}")
                return False
            
            # 添加文件
            files_to_add = []
            
            # 添加资料文件
            for _, _, _, filepath, _ in self.processed_files:
                # filepath是相对于public的，需要转换为相对于项目根目录的
                full_path = str(Path('public') / filepath.lstrip('/'))
                files_to_add.append(full_path)
            
            # 添加MDX文件
            mdx_files = set([f"pages/courses/{p}.mdx" for _, p, _, _, _ in self.processed_files])
            files_to_add.extend(mdx_files)
            
            # 可能修改了_meta.ts
            files_to_add.append("pages/courses/_meta.ts")
            
            print(f"📝 添加文件到暂存区...")
            success, error = self.git_manager.add_files(files_to_add)
            if not success:
                print(f"{Fore.RED}❌ {error}")
                self.git_manager.restore_branch(original_branch)
                self.git_manager.delete_branch(branch_name)
                return False
            
            # 提交
            commit_message = self.git_manager.generate_commit_message(
                courses,
                len(self.processed_files)
            )
            
            print(f"💾 提交更改: {commit_message}")
            success, error = self.git_manager.commit(commit_message)
            if not success:
                print(f"{Fore.RED}❌ {error}")
                self.git_manager.restore_branch(original_branch)
                self.git_manager.delete_branch(branch_name)
                return False
            
            # 推送
            print(f"🚀 推送到远程...")
            success, error = self.git_manager.push(branch_name)
            if not success:
                print(f"{Fore.RED}❌ {error}")
                print(f"{Fore.YELLOW}💡 请检查是否有权限推送到仓库")
                return False
            
            print(f"{Fore.GREEN}✅ Git操作完成")
            self.branch_name = branch_name
            return True
            
        except Exception as e:
            print(f"{Fore.RED}❌ Git操作失败: {e}")
            return False
    
    def create_pull_request(self) -> bool:
        """创建Pull Request"""
        try:
            # 生成PR标题
            courses = list(set([c[0] for c in self.processed_files]))
            if len(courses) == 1:
                title = f"添加: {courses[0]} - {len(self.processed_files)}个资料"
            else:
                title = f"添加: {', '.join(courses[:2])}{'等' if len(courses) > 2 else ''} - {len(self.processed_files)}个资料"
            
            # 生成PR描述
            file_info_list = [
                (chinese_name, filename, resource_type)
                for chinese_name, _, filename, _, resource_type in self.processed_files
            ]
            body = self.git_manager.generate_pr_body(file_info_list)
            
            # 创建PR
            print(f"📬 创建Pull Request...")
            success, result = self.git_manager.create_pr(title, body, self.branch_name)
            
            if success:
                print(f"{Fore.GREEN}✅ PR已创建: {result}")
                return True
            else:
                print(f"{Fore.YELLOW}{result}")
                
                # 即使PR创建失败，更改也已经推送
                print(f"\n{Fore.CYAN}ℹ️  你的更改已成功推送到分支: {self.branch_name}")
                print(f"{Fore.CYAN}   可以稍后手动创建PR，或按上述链接操作")
                
                return False
                
        except Exception as e:
            print(f"{Fore.RED}❌ 创建PR失败: {e}")
            return False
            return False


def main():
    """主函数"""
    try:
        app = EasyPR()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}⚠️  操作已取消")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
