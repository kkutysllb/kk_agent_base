#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# --------------------------------------------------------
# @Author : kkutysllb
# @E-mail : libing1@sn.chinamobile.com，31468130@qq.com
# @Date   : 2024-10-14 21:15
# @Desc   : 长文本上下文精度处理
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(root_dir)

from langchain.chains import LLMChain, StuffDocumentsChain
from langchain.document_transformers import LongContextReorder
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


# 导入本地词嵌入模型
embeddings = HuggingFaceEmbeddings(model_name="/home/libing/kk_LLMs/bge-large-zh-v1.5")


# 模拟一组已经切分的长文本
text = [
    "篮球是一项伟大的运动",
    "带我飞往月球是我最喜欢的歌曲之一。",
    "凯尔特人队是我最喜欢的球队。",
    "这是一篇关于波士顿凯尔特人的文件。",
    "我非常喜欢去看电影。",
    "波士顿凯尔特人队以20分的优势赢得比赛。",
    "这只是一段随机文字。",
    "《艾尔登指环》是过去15年最好的游戏之一。",
    "L.科内特是凯尔特人队最好的球员之一。",
    "拉里·伯德是一位标志性的NBA球员。",
    "迈克尔·乔丹是一位伟大的篮球运动员。"
]

# 创建向量数据库
retriever = Chroma.from_texts(text, embeddings).as_retriever(
    search_kwargs={"k": 10} # 搜索前k个最相关的文档
)

query ="关于凯尔特人队你知道什么？"

# 针对问题找出最相关的3条文本块
docs = retriever.get_relevant_documents(query)

# 对检索结果进行排序，根绝论文的方案
# 问题相关性越低的内容放在中间
# 问题相关性越高的内容放在头尾
reordering = LongContextReorder()
reoder_docs = reordering.transform_documents(docs)

# 构建本地大模型api
api_key = "xxx"
base_url = "http://127.0.0.1:3456/v1"
llm = OpenAI(api_key=api_key, base_url=base_url, temperature=0.0)


# 构建提示词模板
prompt = PromptTemplate(
    input_variables=["page_content"],
    template="{page_content}"
)

shuff_prompt_override = """Given this text extracts:
-----------------------------------------------------
{context}
-----------------------------------------------------
Please answer the following question:
{query}
"""

final_prompt = PromptTemplate(
    input_variables=["context", "query"],
    template=shuff_prompt_override
)

# 构建链
llm_chain = LLMChain(
    llm=llm,
    prompt=final_prompt
)

WorkChain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_prompt=prompt,
    document_variable_name="context"
)




if __name__ == '__main__':
    # print(docs)
    # print(reoder_docs)
    query = "关于凯尔特人队你知道什么？"
    # 调用chain
    WorkChain.run(
        input_documents=reoder_docs,
        query=query
    )