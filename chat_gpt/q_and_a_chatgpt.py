import openai


def get_chat_gpt_response(openai_api_key, prompts):
    openai.api_key = openai_api_key

    messages = [{"role": "system", "content": "You are a intelligent assistant."
                                              "Answer the questions based on the text given"},
                {"role": "user", "content": prompts}]

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    print("*" * 20)


context = "My name is Umesh Kumar. I finished my graduation in 2023 in Masters in Data Science program at" \
          " Indiana University Bloomington. I finished my undergraduation sever years earlier than graduation year. "

questions = "1. What is my name? \n 2. From which university did I graduate? \n " \
            "3. In which year I finished my undergraduate?"

key = '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'
get_chat_gpt_response(key, prompts=context + questions)
