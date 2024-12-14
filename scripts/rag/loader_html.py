#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:03
# @Desc   : 加载html文件
# --------------------------------------------------------
""" 
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
sys.path.append(root_dir)

from langchain.document_loaders import UnstructuredHTMLLoader, BSHTMLLoader

file_path = os.path.join(root_dir, "中国金融期货交易所.html")
if __name__ == "__main__":
    # 网页标签和内容全部加载
    # loader = UnstructuredHTMLLoader(file_path)
    # print(loader.load())
    
    # 只加载网页内容
    loader = BSHTMLLoader(file_path)
    print(loader.load())
