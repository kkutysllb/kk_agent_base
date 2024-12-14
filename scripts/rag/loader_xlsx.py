#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 12:49
# @Desc   : loader加载xlsx文件
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.document_loaders import DirectoryLoader

file_path = os.path.join(root_dir, "2022-2024年云平台维护室绩效.xlsx")

if __name__ == "__main__":
    loader = DirectoryLoader(path=root_dir, glob="*.xlsx")
    print(loader.load())
