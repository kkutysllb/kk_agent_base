#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:08
# @Desc   : 加载json文件
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.document_loaders import JSONLoader

file_path = os.path.join(root_dir, "scripts", "prompts", "prompt.json")


if __name__ == "__main__":
    loader = JSONLoader(file_path, jq_schema=".template", text_content=False)
    print(loader.load())
