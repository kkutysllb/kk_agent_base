#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:24
# @Desc   : 文档切割
# 原理    :  1. 将文档分成小的，有意义的块（句子）
#           2. 将这些块组合成一个大的文本，直到达到一定的大小
#           3. 一旦达到一定的大小，接着开始创建与下一个块重叠的部分
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.text_splitter import RecursiveCharacterTextSplitter

def document_split_test(text):
    """切分文档"""
    # 定义递归字符切割器
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=50,  # qief_size: 切割的大小
        chunk_overlap=20, # overlap_size: 重叠的大小
        length_function=len, # length_function: 长度函数
        add_start_index=True, # add_start_index: 是否添加起始索引
    )
    return text_splitter.create_documents([text])

if __name__ == "__main__":
    # 加载要切分的文档
    file_path = os.path.join(root_dir, "test.txt")
    with open(file_path, "r") as f:
        text = f.read()
    print(document_split_test(text))
