#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 12:32
# @Desc   : loader_mardown方法
# --------------------------------------------------------
"""
from langchain.document_loaders import TextLoader
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)


file_path = os.path.join(root_dir, "README.md")
loader = TextLoader(file_path)


if __name__ == "__main__":
    print(loader.load())
