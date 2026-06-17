"""MDX文件编辑模块 - 负责解析和编辑MDX文件"""

import re
from pathlib import Path
from typing import List, Tuple, Optional


class MDXEditor:
    """MDX文件编辑器"""
    
    # 资料类型到MDX章节的映射
    SECTION_MAP = {
        '期末考试': '## 📝 期末考试',
        '期中考试': '## 📝 期中考试',
        '复习资料': '## 📚 复习资料',
        '课堂笔记': '## 📖 课堂笔记',
        '作业习题': '## 💡 作业习题',
        'PPT课件': '## 📊 PPT课件',
        '其他': '## 📦 其他资料'
    }
    
    def __init__(self, mdx_path: Path):
        self.mdx_path = mdx_path
        self.content = ""
        self.lines: List[str] = []
        self.load()
    
    def load(self):
        """加载MDX文件"""
        if self.mdx_path.exists():
            self.content = self.mdx_path.read_text(encoding='utf-8')
            self.lines = self.content.split('\n')
        else:
            raise FileNotFoundError(f"MDX文件不存在: {self.mdx_path}")
    
    def save(self):
        """保存MDX文件"""
        self.content = '\n'.join(self.lines)
        self.mdx_path.write_text(self.content, encoding='utf-8')
    
    def find_section(self, section_title: str) -> Optional[int]:
        """
        查找章节标题所在的行号
        返回: 行号（0-based）或 None
        """
        for i, line in enumerate(self.lines):
            if line.strip().startswith(section_title):
                return i
        return None
    
    def ensure_section(self, section_title: str) -> int:
        """
        确保章节存在，如果不存在则创建
        返回: 章节标题的行号
        """
        line_num = self.find_section(section_title)
        
        if line_num is not None:
            return line_num
        
        # 章节不存在，需要创建
        # 在 <Comments /> 之前插入
        comments_line = self._find_comments_line()
        
        if comments_line is not None:
            # 在 Comments 前插入新章节
            insert_pos = comments_line
            self.lines.insert(insert_pos, "")
            self.lines.insert(insert_pos + 1, section_title)
            self.lines.insert(insert_pos + 2, "")
            self.lines.insert(insert_pos + 3, "---")
            self.lines.insert(insert_pos + 4, "")
            return insert_pos + 1
        else:
            # 在文件末尾添加
            self.lines.append("")
            self.lines.append(section_title)
            self.lines.append("")
            self.lines.append("---")
            self.lines.append("")
            return len(self.lines) - 4
    
    def _find_comments_line(self) -> Optional[int]:
        """查找 <Comments /> 组件所在的行号"""
        for i, line in enumerate(self.lines):
            if '<Comments' in line:
                return i
        return None
    
    def add_file_download(self, file_name: str, file_path: str, 
                         section_type: str = '其他') -> bool:
        """
        在指定章节添加 FileDownload 组件
        
        参数:
            file_name: 显示的文件名
            file_path: 文件路径（相对于public，以/开头）
            section_type: 资料类型（期末考试、期中考试等）
        
        返回: 是否成功
        """
        try:
            # 获取对应的章节标题
            section_title = self.SECTION_MAP.get(section_type, self.SECTION_MAP['其他'])
            
            # 确保章节存在
            section_line = self.ensure_section(section_title)
            
            # 找到章节内容的插入位置（章节标题后的第一个空行之后）
            insert_line = section_line + 1
            
            # 跳过空行
            while insert_line < len(self.lines) and not self.lines[insert_line].strip():
                insert_line += 1
            
            # 查找下一个章节或分隔符的位置
            next_section_line = self._find_next_section(insert_line)
            
            # 在下一个章节之前插入
            if next_section_line is not None:
                insert_line = next_section_line
            else:
                insert_line = len(self.lines)
            
            # 构建 FileDownload 组件
            file_download = f'''<FileDownload 
  name="{file_name}" 
  path="{file_path}" 
/>'''
            
            # 插入空行和组件
            self.lines.insert(insert_line, "")
            for line in reversed(file_download.split('\n')):
                self.lines.insert(insert_line, line)
            
            return True
            
        except Exception as e:
            print(f"❌ 添加下载链接失败: {e}")
            return False
    
    def _find_next_section(self, start_line: int) -> Optional[int]:
        """
        从指定行开始，查找下一个章节或分隔符
        返回: 行号或 None
        """
        for i in range(start_line, len(self.lines)):
            line = self.lines[i].strip()
            # 检查是否是章节标题或分隔符
            if line.startswith('##') or line == '---':
                # 往前找到最后一个非空行之后的位置
                j = i - 1
                while j > start_line and not self.lines[j].strip():
                    j -= 1
                return j + 1
            # 检查是否是 Comments 组件
            if '<Comments' in line:
                j = i - 1
                while j > start_line and not self.lines[j].strip():
                    j -= 1
                return j + 1
        
        return None
    
    def check_duplicate(self, file_path: str) -> bool:
        """检查文件是否已经存在于MDX中"""
        for line in self.lines:
            if f'path="{file_path}"' in line:
                return True
        return False
    
    def get_section_files(self, section_type: str) -> List[str]:
        """获取指定章节中的所有文件"""
        section_title = self.SECTION_MAP.get(section_type, self.SECTION_MAP['其他'])
        section_line = self.find_section(section_title)
        
        if section_line is None:
            return []
        
        files = []
        next_section = self._find_next_section(section_line + 1)
        end_line = next_section if next_section else len(self.lines)
        
        # 提取该章节中的所有文件路径
        for i in range(section_line, end_line):
            line = self.lines[i]
            match = re.search(r'path="([^"]+)"', line)
            if match:
                files.append(match.group(1))
        
        return files
    
    def format_content(self):
        """格式化MDX内容（移除多余空行等）"""
        # 移除连续的空行（最多保留2个）
        formatted_lines = []
        empty_count = 0
        
        for line in self.lines:
            if not line.strip():
                empty_count += 1
                if empty_count <= 2:
                    formatted_lines.append(line)
            else:
                empty_count = 0
                formatted_lines.append(line)
        
        self.lines = formatted_lines
    
    def add_bulk_downloads(self, downloads: List[Tuple[str, str, str]]) -> int:
        """
        批量添加下载链接
        
        参数:
            downloads: [(文件名, 文件路径, 资料类型), ...]
        
        返回: 成功添加的数量
        """
        success_count = 0
        
        for file_name, file_path, section_type in downloads:
            # 检查是否重复
            if self.check_duplicate(file_path):
                print(f"ℹ️  文件已存在: {file_name}")
                continue
            
            if self.add_file_download(file_name, file_path, section_type):
                success_count += 1
                print(f"✅ 已添加: {file_name} -> {section_type}")
        
        return success_count
