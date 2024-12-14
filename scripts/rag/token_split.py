#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com，31468130@qq.com
# @Date   : 2024-10-14 21:15
# @Desc   : token分割器
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.text_splitter import CharacterTextSplitter



if __name__ == "__main__":
    # 加载文档
    file_path = os.path.join(root_dir, "test.txt")
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    # 分割文档
    text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=5)
    chunks = text_splitter.create_documents([text])
    print(chunks)
