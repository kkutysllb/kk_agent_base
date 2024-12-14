#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 12:40
# @Desc   : 使用loader加载csv文件
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)
from langchain.document_loaders import CSVLoader

file_path = os.path.join(root_dir, "网络云语料库V2.csv")

if __name__ == "__main__":
    loader = CSVLoader(file_path)
    data = loader.load()
    # print(data)
    
    # 调用指定列的内容
    loader = CSVLoader(file_path, encoding="utf-8", source_column="position")
    print(loader.load())
