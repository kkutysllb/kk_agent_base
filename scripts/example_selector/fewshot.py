#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-14 00:12
# @Desc   : 根据输入的提示词长度综合结算最终长度，智能截取或者添加提示词的示例
# --------------------------------------------------------
"""
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts import PromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector

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


# 调用长度示例选择器
example_selector = LengthBasedExampleSelector(
    examples=examples,  # 示例组
    example_prompt=example_prompt,  # 示例模板
    max_length=20  # 最大长度
    # 内置的get_text_length方法，可以获取文本长度,如果默认分词计算方式不满足，可以自己扩展
    # get_text_length(text: str) -> int: = lambda text: len(re.split("\n"| ", text"))
)

# 使用小样本提示词模板实现动态示例的调用
dynamic_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix="给出每个输入的反义词",
    suffix="原词: {adjective}\n反义词:",
    input_variables=["adjective"]
)

if __name__ == "__main__":
    # 小样本获得所有示例
    print(dynamic_prompt.format(adjective="不开心"))
    print(dynamic_prompt.format(adjective="不开心，不开心，不开心，就是不开心，非常非常非常非常非常非常不开心，非常非常非常非常非常非常不开心"))
