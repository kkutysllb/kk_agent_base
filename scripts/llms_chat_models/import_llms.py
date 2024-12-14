#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 09:48
# @Desc   : 调用langchain的llms
# 使用本地部署的模型，调用OpenAI的API
# --------------------------------------------------------
"""
from langchain_openai import OpenAI
from langchain.callbacks import get_openai_callback

api_key = "xxx"
base_url = "http://localhost:1234/v1"

llm = OpenAI(api_key=api_key, base_url=base_url, temperature=0.5)



if __name__ == "__main__":
    # print(llm.invoke("今天天气怎么样？"))
    # 追踪token消耗
    with get_openai_callback() as cb:
        # 流式输出 
        for chunk in llm.stream("请写一首关于秋天的诗"):
            print(chunk, end="", flush=False)
        print(cb)
