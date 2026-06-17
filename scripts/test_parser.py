#!/usr/bin/env python3
"""测试文件名解析功能"""

import sys
from pathlib import Path

# 添加项目根目录到路径
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.utils.file_manager import FileInfo

# 创建一个模拟的上传目录
upload_dir = PROJECT_ROOT / "upload"
upload_dir.mkdir(exist_ok=True)

# 测试文件名列表
test_files = [
    "2025-2026学年第一学期-数学分析BⅠ-阶段性考试-试卷 A-参考解答（草稿）.pdf",
    "2024-期末-数据结构-试卷.pdf",
    "线性代数-2024-期中考试.pdf",
    "2023秋季学期-概率论-复习总结.pdf",
    "算法设计-作业答案-第三章.pdf",
    "计算机组成-课件-第一讲.ppt",
    "数据库引论期末试卷2024.pdf",
    "final_exam_2024.pdf",
]

print("=" * 80)
print("文件名解析测试")
print("=" * 80)

for filename in test_files:
    # 创建临时文件用于测试
    test_file = upload_dir / filename
    test_file.touch()
    
    # 创建FileInfo对象
    file_info = FileInfo(test_file, upload_dir)
    
    print(f"\n📄 原文件名: {filename}")
    print(f"   📚 课程提示: {file_info.course_hint or '未识别'}")
    print(f"   📅 年份提示: {file_info.year_hint or '未识别'}")
    print(f"   📋 类型提示: {file_info.type_hint or '未识别'}")
    
    # 清理临时文件
    test_file.unlink()

print("\n" + "=" * 80)
print("测试完成！")
print("=" * 80)
