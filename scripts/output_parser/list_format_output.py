#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 11:48
# @Desc   : 输出list格式的模板
# --------------------------------------------------------
"""
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# 构建llm模型
api_key = "xxx"
base_url = "http://localhost:1234/v1"
model = OpenAI(api_key=api_key, base_url=base_url, temperature=0.3)

# 构建parser
parser = CommaSeparatedListOutputParser()
format_instructions = """输出为一个列表格式，列表元素为中文，列表元素之间用逗号分隔。"""

# 构建prompt
prompt = PromptTemplate(
    template="列出5个{subject}.\n{format_instructions}",
    input_variables=["subject"],
    partial_variables={"format_instructions": format_instructions},
)

# 构建chain
chain = prompt | model



if __name__ == "__main__":
    # 执行chain
    output = chain.invoke({"subject": "常见的中国人名字"})
    print(output)
    print(parser.parse(output))
