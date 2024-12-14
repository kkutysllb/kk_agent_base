#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 09:51
# @Desc   : 导入langchain的chat模型, 使用本地部署的模型调用ChatOpenAI的API
# --------------------------------------------------------
"""
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.callbacks import get_openai_callback

api_key = "xxx"
base_url = "http://localhost:1234/v1"

llm = ChatOpenAI(api_key=api_key, base_url=base_url, temperature=0.5)

# 构造一组聊天信息
messages = [
    SystemMessage(content="你是一个AI助手，回答问题时请使用中文。你的名字叫tom."),
    HumanMessage(content="你好，AI"),
    AIMessage(content="你好，我是AI助手tom，很高兴见到你！"),
    HumanMessage(content="tom你好，我叫李冰.？"),
    AIMessage(content="你好，李冰，请问有什么可以帮助你？"),
    HumanMessage(content="我该如何开始入门学习中国历史和并且学习大模型应用开发？"),
]


if __name__ == "__main__":
    # print(llm.invoke(messages))
    # 追踪token消耗
    with get_openai_callback() as cb:
        # 流式输出  
        for chunk in llm.stream(messages):
            print(chunk.content, end="", flush=False)
        print(cb)
