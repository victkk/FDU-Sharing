"""文件管理模块 - 负责扫描、验证和移动文件"""

import os
import re
import shutil
from pathlib import Path
from typing import List, Dict, Optional, Tuple
from datetime import datetime


class FileInfo:
    """文件信息类"""
    
    def __init__(self, path: Path, upload_root: Path):
        self.path = path
        self.name = path.name
        self.size = path.stat().st_size
        self.relative_path = path.relative_to(upload_root)
        self.course_hint = self._guess_course()
        self.type_hint = self._guess_type()
        self.year_hint = self._guess_year()
        
    def _guess_course(self) -> Optional[str]:
        """从路径或文件名猜测课程名"""
        # 优先从子目录中获取课程名
        parts = self.relative_path.parts
        if len(parts) > 1:
            return parts[0]
        
        # 尝试从文件名中提取课程名
        name = self.name
        
        # 移除学年学期信息
        name = re.sub(r'\d{4}-\d{4}学年', '', name)
        name = re.sub(r'第[一二三四]学期[-_]?', '', name)
        name = re.sub(r'[春秋夏冬]季?学期[-_]?', '', name)
        
        # 移除年份
        name = re.sub(r'20\d{2}年?', '', name)
        
        # 移除考试类型关键词
        name = re.sub(r'(期末|期中|阶段性|小测|测验)(考试)?[-_]?', '', name)
        name = re.sub(r'(试卷|答案|解答|复习|笔记|作业|课件|讲义)[-_]?', '', name)
        name = re.sub(r'(A|B|C)卷?[-_]?', '', name)
        name = re.sub(r'[（(].*?[）)]', '', name)  # 移除括号内容
        
        # 清理开头和结尾的分隔符
        name = re.sub(r'^[-_\s]+', '', name)
        name = re.sub(r'[-_\s]+$', '', name)
        
        # 提取第一个有意义的中文/字母部分（可能包含数字和罗马数字）
        match = re.search(r'([\u4e00-\u9fa5A-Za-z][A-Za-z\u4e00-\u9fa50-9ⅠⅡⅢⅣⅤ]*)', name)
        if match:
            course_hint = match.group(1).strip()
            # 排除一些明显不是课程名的词
            exclude_words = ['试卷', '答案', '解答', '复习', '笔记', '作业', '第', '章', '节']
            if course_hint and not any(word in course_hint for word in exclude_words):
                return course_hint
        
        return None
    
    def _guess_type(self) -> Optional[str]:
        """从文件名猜测资料类型"""
        name_lower = self.name.lower()
        
        # 优先级：从高到低检查
        if '期末' in self.name or 'final' in name_lower:
            return '期末考试'
        elif '期中' in self.name or 'midterm' in name_lower or '阶段性考试' in self.name or '段考' in self.name:
            return '期中考试'
        elif '小测' in self.name or 'quiz' in name_lower or '测验' in self.name:
            return '期中考试'  # 归类到期中考试
        elif '复习' in self.name or 'review' in name_lower or '总结' in self.name:
            return '复习资料'
        elif '笔记' in self.name or 'note' in name_lower:
            return '课堂笔记'
        elif '作业' in self.name or 'homework' in name_lower or 'hw' in name_lower:
            return '作业习题'
        elif 'ppt' in name_lower or '课件' in self.name or '讲义' in self.name:
            return 'PPT课件'
        elif '答案' in self.name or '解答' in self.name or 'solution' in name_lower or 'answer' in name_lower:
            # 根据文件名判断是哪种考试的答案
            if '期末' in self.name:
                return '期末考试'
            elif '期中' in self.name or '阶段' in self.name:
                return '期中考试'
            else:
                return '其他'
        
        return None
    
    def _guess_year(self) -> Optional[str]:
        """从文件名猜测年份"""
        # 优先匹配学年格式：2025-2026学年 -> 取第一个年份
        match = re.search(r'(20\d{2})-20\d{2}学年', self.name)
        if match:
            return match.group(1)
        
        # 匹配单独的年份
        match = re.search(r'(20\d{2})', self.name)
        if match:
            return match.group(1)
        
        return None
    
    def get_size_str(self) -> str:
        """获取人类可读的文件大小"""
        size = self.size
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024.0:
                return f"{size:.1f}{unit}"
            size /= 1024.0
        return f"{size:.1f}TB"
    
    def is_valid_size(self) -> bool:
        """检查文件大小是否在限制内（100MB）"""
        return self.size < 100 * 1024 * 1024
    
    def is_supported_format(self) -> bool:
        """检查文件格式是否支持"""
        supported = ['.pdf', '.docx', '.doc', '.pptx', '.ppt', '.zip', '.rar', 
                    '.7z', '.md', '.txt', '.xlsx', '.xls', '.png', '.jpg', '.jpeg']
        return self.path.suffix.lower() in supported


class FileManager:
    """文件管理器"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.upload_dir = project_root / "upload"
        self.resources_dir = project_root / "public" / "resources"
        
    def scan_upload_dir(self) -> List[FileInfo]:
        """扫描upload目录中的所有文件"""
        if not self.upload_dir.exists():
            print(f"⚠️  上传目录不存在: {self.upload_dir}")
            return []
        
        files = []
        for root, dirs, filenames in os.walk(self.upload_dir):
            # 跳过隐藏文件和特殊文件
            filenames = [f for f in filenames if not f.startswith('.') and f not in ['README.md', '.gitkeep']]
            
            for filename in filenames:
                file_path = Path(root) / filename
                file_info = FileInfo(file_path, self.upload_dir)
                files.append(file_info)
        
        return files
    
    def group_files_by_course(self, files: List[FileInfo]) -> Dict[str, List[FileInfo]]:
        """按课程分组文件"""
        groups = {}
        ungrouped = []
        
        for file_info in files:
            if file_info.course_hint:
                if file_info.course_hint not in groups:
                    groups[file_info.course_hint] = []
                groups[file_info.course_hint].append(file_info)
            else:
                ungrouped.append(file_info)
        
        if ungrouped:
            groups['未分类'] = ungrouped
        
        return groups
    
    def validate_file(self, file_info: FileInfo) -> Tuple[bool, str]:
        """
        验证文件
        返回: (是否有效, 错误信息)
        """
        if not file_info.path.exists():
            return False, "文件不存在"
        
        if not file_info.is_valid_size():
            return False, f"文件过大 ({file_info.get_size_str()})，超过100MB限制"
        
        if not file_info.is_supported_format():
            return False, f"不支持的文件格式: {file_info.path.suffix}"
        
        return True, ""
    
    def move_file(self, file_info: FileInfo, course_chinese_name: str, 
                  new_filename: Optional[str] = None) -> Tuple[bool, str]:
        """
        移动文件到资料目录
        返回: (是否成功, 目标路径或错误信息)
        """
        try:
            # 目标目录
            target_dir = self.resources_dir / course_chinese_name
            target_dir.mkdir(parents=True, exist_ok=True)
            
            # 确定目标文件名
            if new_filename:
                target_filename = new_filename
            else:
                target_filename = file_info.name
            
            # 目标路径
            target_path = target_dir / target_filename
            
            # 如果目标文件已存在，添加时间戳
            if target_path.exists():
                timestamp = datetime.now().strftime("%H%M%S")
                stem = target_path.stem
                suffix = target_path.suffix
                target_path = target_dir / f"{stem}_{timestamp}{suffix}"
            
            # 移动文件
            shutil.copy2(file_info.path, target_path)
            
            # 返回相对于public的路径（用于MDX）
            relative_path = target_path.relative_to(self.project_root / "public")
            return True, f"/{relative_path.as_posix()}"
            
        except Exception as e:
            return False, f"移动失败: {e}"
    
    def delete_file(self, file_info: FileInfo) -> bool:
        """删除已处理的文件"""
        try:
            file_info.path.unlink()
            
            # 如果目录为空，也删除
            parent = file_info.path.parent
            if parent != self.upload_dir and not any(parent.iterdir()):
                parent.rmdir()
            
            return True
        except Exception as e:
            print(f"⚠️  删除文件失败: {e}")
            return False
    
    def suggest_filename(self, file_info: FileInfo, year: str = None, 
                        file_type: str = None) -> str:
        """
        根据规范建议文件名
        格式: [年份]-[类型]-[描述].扩展名
        """
        # 提取原文件名中的描述部分
        stem = file_info.path.stem
        suffix = file_info.path.suffix
        
        # 清理文件名
        stem = re.sub(r'^\d{4}[-_]?', '', stem)  # 移除开头的年份
        stem = re.sub(r'(期末|期中|复习|笔记|作业|试卷|答案)[-_]?', '', stem)  # 移除类型关键词
        stem = stem.strip('-_')
        
        # 如果没有描述，使用类型作为描述
        if not stem:
            type_map = {
                '期末考试': '试卷',
                '期中考试': '试卷',
                '复习资料': '总结',
                '课堂笔记': '笔记',
                '作业习题': '作业',
                'PPT课件': 'PPT'
            }
            stem = type_map.get(file_type, '资料')
        
        # 构建新文件名
        parts = []
        
        if year:
            parts.append(year)
        elif file_info.year_hint:
            parts.append(file_info.year_hint)
        else:
            parts.append(datetime.now().strftime("%Y"))
        
        if file_type:
            type_short = file_type.replace('考试', '').replace('资料', '').replace('习题', '')
            parts.append(type_short)
        
        parts.append(stem)
        
        return '-'.join(parts) + suffix
    
    def get_file_display_name(self, file_info: FileInfo) -> str:
        """获取文件的显示名称（用于列表）"""
        hint_parts = []
        
        if file_info.course_hint:
            hint_parts.append(f"课程:{file_info.course_hint}")
        
        if file_info.year_hint:
            hint_parts.append(f"{file_info.year_hint}年")
        
        if file_info.type_hint:
            hint_parts.append(file_info.type_hint)
        
        hint_str = " | ".join(hint_parts) if hint_parts else "待分类"
        
        return f"{file_info.name} ({file_info.get_size_str()}) [{hint_str}]"
