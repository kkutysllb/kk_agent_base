#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 10:39
# @Desc   : 函数调用，希望每次根据指令，可以输出一个这样的笑话（小明是怎么死的？笨死的）
# --------------------------------------------------------
"""
from langchain_openai import OpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain.pydantic_v1 import BaseModel, Field, validator
from typing import List

# 构建本地模型采用OpenAI的API方式
api_key = "xxx"
base_url = "http://localhost:1234/v1"
model = OpenAI(api_key=api_key, base_url=base_url, temperature=0.5)

# 定义数据模型，描述最终的实例结构
class Joke(BaseModel):
    setup: str = Field(description="设置笑话的问题")
    punchline: str = Field(description="设置笑话的答案")

    # 验证笑话的问题是否包含小明，并且以问号结尾
    @validator("setup", allow_reuse=True)
    def validate_setup(cls, v):
        # if "小明" not in v:
        #     raise ValueError("笑话必须包含小明")
        if not v.endswith("?"):
            raise ValueError("笑话的问题必须以问号结尾")
        return v
    
# 构建输出解析器
parser = PydanticOutputParser(pydantic_object=Joke)
# format_instructions = parser.get_format_instructions()
format_instructions = """
{
'setup': '问题',
'punchline': '答案'
}
"""

# 构建提示词模板
prompt = PromptTemplate(
    template="回答问题.\n{format_instructions}\n{question}",
    input_variables=["question"],
    partial_variables={"format_instructions": format_instructions}
)

# 构建链
chain = prompt | model 


if __name__ == "__main__":
    result = chain.invoke({"question": "请给我讲一个美国的笑话"})
    print(result)