"""课程管理模块 - 负责读取、匹配和创建课程"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class CourseManager:
    """管理课程信息和操作"""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.courses_dir = project_root / "pages" / "courses"
        self.resources_dir = project_root / "public" / "resources"
        self.meta_file = self.courses_dir / "_meta.ts"
        self.courses: Dict[str, str] = {}  # {pinyin: 中文名}
        self.load_courses()
    
    def load_courses(self):
        """从 _meta.ts 读取已有课程"""
        if not self.meta_file.exists():
            print(f"⚠️  警告: {self.meta_file} 不存在")
            return
        
        content = self.meta_file.read_text(encoding='utf-8')
        # 匹配格式: 'pinyin': '🔢 课程名'
        pattern = r"'([^']+)':\s*'(?:[^']*\s)?([^']+)'"
        matches = re.findall(pattern, content)
        
        for pinyin, chinese_name in matches:
            # 移除可能的emoji前缀
            chinese_name = re.sub(r'^[^\u4e00-\u9fa5a-zA-Z]+\s*', '', chinese_name)
            self.courses[pinyin] = chinese_name
        
        print(f"✅ 已加载 {len(self.courses)} 门课程")
    
    def get_all_courses(self) -> List[Tuple[str, str]]:
        """获取所有课程列表 [(拼音, 中文名)]"""
        return sorted(self.courses.items(), key=lambda x: x[1])
    
    def get_course_choices(self) -> List[str]:
        """获取课程选择列表（用于交互式选择）"""
        choices = []
        for pinyin, chinese_name in self.get_all_courses():
            # 检查是否有资料文件夹
            has_resources = (self.resources_dir / chinese_name).exists()
            # 检查是否有页面文件
            has_page = (self.courses_dir / f"{pinyin}.mdx").exists()
            
            status = "✅" if (has_resources and has_page) else "📝"
            choices.append(f"{status} {chinese_name} ({pinyin})")
        
        choices.append("➕ 创建新课程")
        return choices
    
    def match_course(self, user_input: str) -> Optional[Tuple[str, str]]:
        """
        匹配课程名称（支持模糊搜索）
        返回: (拼音, 中文名) 或 None
        """
        user_input = user_input.strip()
        
        # 精确匹配中文名
        for pinyin, chinese_name in self.courses.items():
            if user_input == chinese_name:
                return (pinyin, chinese_name)
        
        # 精确匹配拼音
        if user_input in self.courses:
            return (user_input, self.courses[user_input])
        
        # 模糊匹配中文名（包含关系）
        for pinyin, chinese_name in self.courses.items():
            if user_input in chinese_name or chinese_name in user_input:
                return (pinyin, chinese_name)
        
        # 模糊匹配拼音
        for pinyin, chinese_name in self.courses.items():
            if user_input in pinyin:
                return (pinyin, chinese_name)
        
        return None
    
    def parse_choice(self, choice: str) -> Optional[Tuple[str, str]]:
        """从选择字符串中解析出课程信息"""
        if choice == "➕ 创建新课程":
            return None
        
        # 格式: "✅ 数据结构 (shujujiegou)"
        match = re.search(r'([^(]+)\(([^)]+)\)', choice)
        if match:
            chinese_name = match.group(1).strip()
            # 移除前缀emoji
            chinese_name = re.sub(r'^[^\u4e00-\u9fa5a-zA-Z]+\s*', '', chinese_name)
            pinyin = match.group(2).strip()
            return (pinyin, chinese_name)
        
        return None
    
    def create_course(self, chinese_name: str, pinyin: str, emoji: str = "📚") -> bool:
        """
        创建新课程
        1. 创建资料目录
        2. 创建MDX文件
        3. 更新_meta.ts
        """
        try:
            # 1. 创建资料目录
            resources_path = self.resources_dir / chinese_name
            resources_path.mkdir(parents=True, exist_ok=True)
            print(f"✅ 创建资料目录: {resources_path.relative_to(self.project_root)}")
            
            # 2. 创建MDX文件
            mdx_path = self.courses_dir / f"{pinyin}.mdx"
            if not mdx_path.exists():
                mdx_content = self._get_mdx_template(chinese_name)
                mdx_path.write_text(mdx_content, encoding='utf-8')
                print(f"✅ 创建课程页面: {mdx_path.relative_to(self.project_root)}")
            else:
                print(f"ℹ️  课程页面已存在: {mdx_path.relative_to(self.project_root)}")
            
            # 3. 更新_meta.ts
            self._add_to_meta(pinyin, chinese_name, emoji)
            
            # 更新缓存
            self.courses[pinyin] = chinese_name
            
            return True
            
        except Exception as e:
            print(f"❌ 创建课程失败: {e}")
            return False
    
    def _get_mdx_template(self, course_name: str) -> str:
        """获取MDX文件模板"""
        return f"""import {{ FileDownload }} from '@/components/FileDownload'
import {{ Comments }} from '@/components/Comments'

# 📚 {course_name}

> 本页面收集了{course_name}课程的相关资料

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
"""
    
    def _add_to_meta(self, pinyin: str, chinese_name: str, emoji: str):
        """将新课程添加到_meta.ts"""
        if not self.meta_file.exists():
            print(f"⚠️  {self.meta_file} 不存在，跳过更新")
            return
        
        content = self.meta_file.read_text(encoding='utf-8')
        
        # 检查是否已存在
        if f"'{pinyin}'" in content:
            print(f"ℹ️  课程 {pinyin} 已在导航中")
            return
        
        # 在最后一个条目后插入
        # 查找 export default { ... }
        new_line = f"  '{pinyin}': '{emoji} {chinese_name}'"
        
        # 找到最后一个课程条目（在闭合大括号之前）
        lines = content.split('\n')
        insert_index = -1
        
        for i in range(len(lines) - 1, -1, -1):
            if '}' in lines[i] and 'export default' not in lines[i]:
                insert_index = i
                break
        
        if insert_index > 0:
            # 检查前一行是否需要添加逗号
            prev_line = lines[insert_index - 1].rstrip()
            if prev_line and not prev_line.endswith(','):
                lines[insert_index - 1] = prev_line + ','
            
            lines.insert(insert_index, new_line + ',')
            new_content = '\n'.join(lines)
            self.meta_file.write_text(new_content, encoding='utf-8')
            print(f"✅ 已添加到导航: {emoji} {chinese_name}")
        else:
            print(f"⚠️  无法自动更新 _meta.ts，请手动添加")
    
    def course_exists(self, pinyin: str) -> bool:
        """检查课程是否存在"""
        return pinyin in self.courses
    
    def get_course_page_path(self, pinyin: str) -> Path:
        """获取课程MDX文件路径"""
        return self.courses_dir / f"{pinyin}.mdx"
    
    def get_course_resources_path(self, chinese_name: str) -> Path:
        """获取课程资料目录路径"""
        return self.resources_dir / chinese_name
