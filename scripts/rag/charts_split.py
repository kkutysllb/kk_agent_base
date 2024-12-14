#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:42
# @Desc   : 字符切割
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.text_splitter import CharacterTextSplitter

def charts_split_text(text):
    """定义字符切割器"""
    text_splitter = CharacterTextSplitter(
        separator="。", # 切割符，默认是\n\n
        chunk_size=50, # 切割的大小
        chunk_overlap=20, # 重叠的大小
        length_function=len, # 长度函数
        add_start_index=True, # 是否添加起始索引
        is_separator_regex=False, # 是否使用正则表达式
    )
    return text_splitter.create_documents([text])


if __name__ == "__main__":
    # 加载要切分的文档
    file_path = os.path.join(root_dir, "test.txt")
    with open(file_path, "r") as f:
        text = f.read()
    print(charts_split_text(text)[0])