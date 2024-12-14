#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com，31468130@qq.com
# @Date   : 2024-10-14 21:15
# @Desc   : 自定义模板示例
# --------------------------------------------------------
"""
from langchain.prompts import StringPromptTemplate
import inspect
from langchain_openai import ChatOpenAI, OpenAI

### 代码大师：根据函数名称，查找函数代码，并给出中文解释
PROMPT = """ 你是一个非常有经验的程序员，现在给你如下函数名称，你会按照如下格式，输出这段代码的名称、源代码、中文解释 
    函数名称: {function_name}
    函数源代码: \n{source_code}
    函数中文解释: {function_explanation}
    """

def custom_prompt_template():
    # 定义一个简单函数示例
    def hello_world():
        print("Hello, World!")

    
    
    def get_source_code(function_name):
        """获得源代码"""
        return inspect.getsource(function_name)
    
    # 自定义模板
    class CustomPrompt(StringPromptTemplate):
        def format(self, **kwargs):
            # 获得源代码
            source_code = get_source_code(kwargs["function_name"])
           
            # 生成提示词模板
            prompt = PROMPT.format(
                function_name=kwargs["function_name"].__name__, 
                source_code=source_code, 
                function_explanation=kwargs["function_explanation"])
            
            return prompt
        
    custom_prompt = CustomPrompt(input_variables=["function_name", "function_explanation"])
    custom_prompt = custom_prompt.format(function_name=hello_world, function_explanation="这是一个简单的Hello, World!函数")
    # print(custom_prompt)
    
    # 直接和本地大模型连接起来
    # 本地大模型采用LMStudio启用lamma3-8b-instruct模型
    api_key = "xxx"
    base_url = "http://127.0.0.1:1234/v1"
    llm = OpenAI(api_key=api_key, base_url=base_url, temperature=0.7)
    
    print(llm.invoke(custom_prompt))

if __name__ == "__main__":
    custom_prompt_template()
