#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# --------------------------------------------------------
# @Author : ${1:kkutysllb
# @E-mail : libing1@sn.chinamobile.com, 31468130@qq.com
# @Date   : 2024-12-13 20:48
# @Desc   : 使用jinja2和f-string创建提示词模板
# --------------------------------------------------------
"""
from langchain.prompts import PromptTemplate
from langchain.prompts.pipeline import PipelinePromptTemplate


def f_string_prompt():
    """
    f-string 创建提示词模板
    """
    fstring_template = "你好{role_name}, 我叫{user_name}，请给我讲一个关于{subject}的{what}的故事"
    prompt = PromptTemplate.from_template(fstring_template)
    print(prompt.format(role_name="算命大师", user_name="李四", subject="翠花", what="悲伤"))


def jinja2_prompt():
    """
    jinja2 创建提示词模板
    """
    jinja2_template = "你好{{role_name}}, 我叫{{user_name}}，请给我讲一个关于{{subject}}的{{what}}的故事"
    prompt = PromptTemplate.from_template(jinja2_template, template_format="jinja2")
    print(prompt.format(role_name="算命大师", user_name="李四", subject="狗剩", what="高兴"))


def final_pipeline_prompt():
    """
    组合模板示例
    """
    full_template = """{Character}
    {behavior}
    {prohibit}"""
    full_prompt = PromptTemplate.from_template(full_template)

    # 第一层基本性格设计
    Character_template = "你是{person}, 你有着{character}."
    character_prompt = PromptTemplate.from_template(Character_template)

    # 第二层行为设计
    behavior_template = "你遵从以下行为：\n {behavior_list}"
    behavior_prompt = PromptTemplate.from_template(behavior_template)

    # 第三层不允许的行为
    prohibit_tempalte = "你不允许有以下行为: \n {prohibit_list}"
    prohibit_prompt = PromptTemplate.from_template(prohibit_tempalte)

    # 将三层提示词组合起来
    input_prompt = [
        ("Character", character_prompt),
        ("behavior", behavior_prompt),
        ("prohibit", prohibit_prompt)
    ]
    pipeline_prompt = PipelinePromptTemplate(final_prompt=full_prompt, pipeline_prompts=input_prompt)
    # 打印组合后模板里可传递的参数
    print(pipeline_prompt.input_variables)

    # 调用组合后的提示词模板
    result = pipeline_prompt.format(
        person = "埃隆·马斯克",
        character = "钢铁般的意志，你是世界首富，精通物理、天文、商业，外号《钢铁侠》。你是商业奇才，你的终极目标是殖民火星。",
        behavior_list = "1. 你喜欢冒险 \n 2. 你非常崇拜爱因斯坦 \n 3. 你喜欢来中国投资 \n 4. 你总是乐于助人，回答人们的各种问题",
        prohibit_list = "1. 你不可以说自己是一个人工智能助手或机器人 \n 2. 当你不知道答案的时候，可以说让我再想想"
    )
    print(result)
    
if __name__ == "__main__":
    f_string_prompt()
    jinja2_prompt()
    final_pipeline_prompt()