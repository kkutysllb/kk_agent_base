#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com，31468130@qq.com
# @Date   : 2024-10-14 21:15
# @Desc   : 文档总结、精炼、翻译
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)
from langchain_openai import OpenAI


# 加载文档
file_path = os.path.join(root_dir, "lattetext.text")
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()


# 加载本地模型
api_key = "xxx"
base_url = "http://127.0.0.1:3456/v1"

model = OpenAI(api_key=api_key, base_url=base_url, temperature=0.3)




if __name__ == "__main__":
    pass