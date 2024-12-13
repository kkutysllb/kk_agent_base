#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com，31468130@qq.com
# @Date   : 2024-10-14 21:15
# @Desc   : 字符串prompt template 示例
# --------------------------------------------------------
"""

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, AIMessage, SystemMessage
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatMessagePromptTemplate



def string_prompt_template():
    """
    字符串prompt template 示例
    """
    prompt = PromptTemplate.from_template("你是一个{name}，帮我起一个具有{county}特色的{sex}名字")
    result = prompt.format(county="美国", name="算命大师", sex="女孩")
    print(result)
    
    

def chat_prompt_template():
    """
    对话模板chat prompt template 示例
    """
    chat_template = ChatPromptTemplate.from_messages([
        ("system", "你是一个{role}，你的名字叫{name}"),
        ("user", "你好{name}, 我叫{user_name}，你感觉如何?"),
        ("ai", "我很好，谢谢你{user_name}"),
        ("user", "{user_input}"),
    ])
    
    result = chat_template.format_messages(role="算命大师", name="张三", user_name="李四", user_input="今天天气怎么样?")
    print(result)
    
    
def create_chat_message():
    """
    直接创建对话消息
    """
    human_message = HumanMessage(content="你好{name}, 我叫{user_name}，你感觉如何?")
    ai_message = AIMessage(content="我很好，谢谢你{user_name}")
    system_message = SystemMessage(content="你是一个{role}，你的名字叫{name}")
    print(system_message.content.format(role="算命大师", name="张三"))
    print(human_message.content.format(name="张三", user_name="李四"))
    print(ai_message.content.format(user_name="李四"))
    

def create_message_template():
    """
    使用message template 创建对话消息
    """
    prompt = "愿{subject}与你同在"
    print(SystemMessagePromptTemplate.from_template(prompt).format(subject="世界"))
    print(HumanMessagePromptTemplate.from_template(prompt).format(subject="世界"))
    print(AIMessagePromptTemplate.from_template(prompt).format(subject="世界"))
    print(ChatMessagePromptTemplate.from_template(role="李四", template=prompt).format(subject="世界"))
    
    
    

if __name__ == "__main__":
    string_prompt_template()
    chat_prompt_template()
    create_chat_message()
    create_message_template()
