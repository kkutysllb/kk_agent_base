#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-13 22:10
# @Desc   : 序列化提示词模板示例
# --------------------------------------------------------
"""
import os
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from langchain.prompts import load_prompt
from langchain_core.output_parsers import StructuredOutputParser
from langchain_core.prompts import PromptTemplate


def yaml_prompt():
    """加载yaml格式prompt示例"""
    prompt = load_prompt(os.path.join(root_dir, "prompts", "prompt.yaml"))
    print(prompt.input_variables)
    print(prompt.format(name="张三", what="悲伤"))


def json_prompt():
    """加载json格式prompt示例"""
    prompt = load_prompt(os.path.join(root_dir, "prompts", "prompt.json"))
    print(prompt.input_variables)
    print(prompt.format(name="李四", what="开心"))


def json_with_output_parser():

    prompt_template = """
    Given the following question and student answer, provide a correct answer and score the student answer.
    Question: {question}
    Student Answer: {student_answer}
    Correct Answer: {answer}
    Score: {score}
    """

    output_parser = StructuredOutputParser.from_response_format(
        response_format=[
            {"name": "answer", "description": "The correct answer"},
            {"name": "score", "description": "The score for the student's answer"}
        ]
    )

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["question", "student_answer"],
        output_parser=output_parser
    )

    result = prompt.format(
        question="What is the capital of France?",
        student_answer="Paris"
    )
    print(result)



if __name__ == "__main__":
    yaml_prompt()
    json_prompt()
    json_with_output_parser()
