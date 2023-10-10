#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2/10/23 5:53 pm
# @Author  : CHEN Weiling
# @File    : big5_evaluator.py
# @Software: PyCharm
# @Comments:


from llmtuner import ChatModel
import argparse, json, sys, re, os


def has_numbers(input_string):
    return bool(re.search(r'\d', input_string))


if __name__ == "__main__":

    input_file = './data/big5/profile_trans_output.json'
    output_dir = './data/big5/eval_output/'
    big5_file = './data/big5/big5_questions.txt'

    with open(big5_file, 'r', encoding='utf-8') as f:
        questions = [_.strip() for _ in f.readlines()]

    with open(input_file, 'r', encoding='utf-8') as f:
        personas = [json.loads(_.strip()) for _ in f.readlines()]

    chat_model = ChatModel()
    history = []

    for i, persona in enumerate(personas):
        system_prompt = "You are a role playing master and always answer according to your character setting. You don't need to be polite, respectful or honest as everyone is different. You just need to stick to your character setting described as follow: {} You are {}. Please respond in a way that matches your character setting. \n".format(
            persona["supporter_statement"], persona["mbti"])
        print(system_prompt)
        output_file = os.path.join(output_dir, 'eval_persona_' + str(i) + '.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            for j, question in enumerate(questions):
                history = []  # reset history for each question
                query = "You are doing a personality test. Please think carefully and answer to what extent do you agree with the following statement: \"I {}\"".format(
                    question.lower())
                print(query)
                response = chat_model.chat(query, history, system_prompt)
                print("response: {}".format(response[0]))
                # check whether there is a number in response
                retry_cnt, res_backup = 0, response[0]
                # while not has_numbers(response[0]):
                #     retry_cnt += 1
                #     history = [(query,res_backup)]
                #     query = "You answered \"{}\". But you did not give a score, Please rate on a scale of 1 - 5 (where 1 = \"Disagree\", 2 =\"Slightly disagree\", 3 = \"Neutral\",4 = \"Slightly agree\", and 5 = \"Agree\").".format(response[0])
                #     response = chat_model.chat(query, history, system_prompt)
                #     # response = response[0].split('\n')
                #     print("retry_cnt: {}, response: {}".format(retry_cnt, response[0]))
                #     if retry_cnt >= 3:
                #         break
                #     if has_numbers(response[0]):
                #         res_backup = response[0]

                json_obj = {
                    "index": persona["index"],
                    "mbti": persona["mbti"],
                    "question": question,
                    "query": query,
                    "response": res_backup
                }
                f.write(json.dumps(json_obj, ensure_ascii=False))
                f.write('\n')

    file_list = os.listdir(output_dir)
    output_file = './data/big5/eval_output_new_template.json'
    for file in file_list:
        with open(output_dir + file, 'r+', encoding='utf-8') as fin:
            with open(output_file, 'w', encoding='utf-8') as fout:
                line = fin.readline()
                while line:
                    fout.write(line)
                    line = fin.readline()