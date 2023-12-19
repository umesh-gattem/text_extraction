import os

import openai


def get_chat_gpt_response(openai_api_key, file_path, prompts):
    openai.api_key = openai_api_key

    # for filename in os.listdir(input_folder):
    # f = os.path.join(input_folder, filename)
    text = open(file_path).read()
    messages = [{"role": "system", "content": "You are a intelligent assistant."},
                {"role": "user", "content": prompts + f"'{text}'"}]

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    print("*"*20)

