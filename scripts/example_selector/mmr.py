#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 09:21
# @Desc   : 最大边际相关性示例选择器，根据输入相似度选择示例
# MMR首先找出与输入最相似的样本，然后在迭代过程中，对于与已选择的样本过于接近的样本进行惩罚
# --------------------------------------------------------
"""
from langchain.prompts.example_selector import MaxMarginalRelevanceExampleSelector
from langchain.vectorstores import FAISS
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
    {"input": "big", "output": "small"},
    {"input": "fast", "output": "slow"},
    {"input": "高兴", "output": "悲伤"},
    {"input": "兴高采烈", "output": "郁郁寡欢"},
]

# 构造提示词模板
example_prompt = PromptTemplate(
    input_variables=["input", "output"],
    template="原词: {input}\n反义词: {output}"
)

# 调用示例选择器
example_selector = MaxMarginalRelevanceExampleSelector.from_examples(
    examples,
    embeddings,
    FAISS,
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
# 调用最大边际相关性示例选择器
if __name__ == "__main__":
    print(dynamic_prompt.format(adjective="难过"))
