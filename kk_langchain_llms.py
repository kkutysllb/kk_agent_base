#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-04 11:56
# @Desc   : 自定义库函数，封装langchain的llms
# --------------------------------------------------------
"""
from langchain.llms.base import LLM
from zhipuai import ZhipuAI
from langchain_core.messages.ai import AIMessage
from typing import List, Optional, Any, Generator



class kk_ChatGLM4(LLM):
    """智谱ai的ChatGLM4模型自定义封装"""
    history_messages: List = []
    client: object = None

    def __init__(self, api_key: str):
        super().__init__()
        self.client = ZhipuAI(api_key=api_key)

    @property
    def _llm_type(self) -> str:
        return "kk_ChatGLM4"
    
    def invoke(self, prompt: str, history_messages: List = []) -> str:
        if history_messages is None:
            self.history_messages = []  # 如果history_messages为空，则初始化为空列表
        else:
            self.history_messages = history_messages  # 如果history_messages不为空，则更新history_messages
        history_messages.append({"role": "user", "content": prompt}) # 追加新的消息记录
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=history_messages
        )
        result = response.choices[0].message.content
        return AIMessage(content=result)
    
    def _call(self, prompt: str, history_messages: List = []) -> str:
        return self.invoke(prompt, history_messages)
    
    def stream(self, prompt: str, history_messages: List = []) -> Generator[str, None, None]:
        if history_messages is None:
            self.history_messages = []
        else:
            self.history_messages = history_messages
        history_messages.append({"role": "user", "content": prompt})
        response = self.client.chat.completions.create(
            model="glm-4",
            messages=history_messages,
            stream=True
        )
        for chunk in response:
            yield chunk.choices[0].delta.content

if __name__ == "__main__":
    pass
