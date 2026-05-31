# -*- coding: utf-8 -*-
import os

def main():
    print("=============================================")
    print("🚀 欢迎使用个人资产商业化转译器 (CLI v1.0)")
    print("=============================================")
    
    # 1. 输入阶段
    pain_point = input("1. 过去3年，你解决过最恶心、最麻烦的一件事是什么？\n输入: ")
    steps = input("2. 搞定这件事，你主要分成了哪几步？（用逗号隔开）\n输入: ")
    
    # 2. 处理与映射
    step_list = steps.split("，") if "，" in steps else steps.split(",")
    
    # 3. 输出报告
    report_content = f"""# 您的资产转译报告

### 🎯 核心痛点资产
- {pain_point}

### 📦 提炼出的 SOP 步骤
"""
    for i, step in enumerate(step_list, 1):
        report_content += f"{i}. [ ] {step.strip()}\n"
        
    report_content += "\n### 💰 变现建议\n- **产品化**: 将这些步骤封装为 Notion/Excel 模板发布。\n- **顾问式**: 针对该痛点提供 1对1 咨询。"

    # 保存为 Markdown 文件
    with open("我的资产转译报告.md", "w", encoding="utf-8") as f:
        f.write(report_content)
        
    print("\n🎉 报告生成成功！已保存在当前目录下的 '我的资产转译报告.md'。")

if __name__ == "__main__":
    main()
