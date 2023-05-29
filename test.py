import os
import openai
import openKey
openai.api_key = openKey.openAiKey


messages = []
while True:
    user_content = input("질문 : ")
    messages.append({"role": "user", "content":f"{user_content}"})
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages = messages)

    content_save = completion['choices'][0]['message']['content'].strip()

    messages.append({"role": "user", "content":f"{content_save}"})

    print("GPT : {0}\n".format(content_save))