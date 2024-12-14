#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 09:36
# @Desc   : 语义相似度示例选择器，最大余弦相似度。根据输入相似度选择示例
# 通过计算两个向量的余弦值来衡量它们的相似度
# 余弦值越接近1，表示两个向量越相似
# --------------------------------------------------------
"""
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate, FewShotPromptTemplate

# 词嵌入模型
embeddings = HuggingFaceEmbeddings(model_name="/Users/libing/kk_LLMs/bge-large-zh-v1.5")

# 假设我们有一个prompt，里面有10个示例
examples = [
    {"input": "happy", "output": "sad"},
    {"input": "sunny", "output": "rainy"},
    {"input": "cold", "output": "hot"},
    {"input": "hot", "output": "cold"},
    {"input": "高兴", "output": "悲伤"},
    {"input": "兴高采烈", "output": "郁郁寡欢"},
]

# 创建提示词模板
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="原词: {input}\n反义词: {output}"
)

# 创建示例选择器
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    embeddings,
    Chroma,
    k=2
)

# 使用小样本模板
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="原词: {adjective}\n反义词:",
    input_variables=["adjective"]
)

if __name__ == "__main__":
    print(dynamic_prompt.format(adjective="难过"))
