#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:13
# @Desc   : 记载pdf文件
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.document_loaders import PyPDFLoader

file_path = os.path.join(root_dir, "改进CLIP-ReID的跨模态行人重识别_贾军营.pdf")




if __name__ == "__main__":
    loader = PyPDFLoader(file_path)
    pages = loader.load_and_split()
    print(len(pages))
