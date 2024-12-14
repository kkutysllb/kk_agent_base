#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 13:46
# @Desc   : 代码文档的切割
# --------------------------------------------------------
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

def get_supported_languages():
    """
    获取支持的语言列表
    """
    return [e.value for e in Language]

# 构建要切割的代码文档实例
PYTHON_CODE = """
def get_supported_languages():
    '''
    获取支持的语言列表
    '''
    return [e.value for e in Language]
# 调用函数
get_supported_languages()
"""


if __name__ == "__main__":
    print(get_supported_languages())
    py_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=50,
        chunk_overlap=10,
        length_function=len
    )
    python_docs = py_splitter.create_documents([PYTHON_CODE])
    print(python_docs)
