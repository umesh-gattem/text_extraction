import json

import openai
import pandas as pd


def get_chat_gpt_response(openai_api_key, messages):
    openai.api_key = openai_api_key

    messages = messages

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    output = chat.choices[0].message.content
    print("Due Date changed to : ", output)
    print("*" * 20)
    return output


gpt_prompt = [{"role": "system", "content": "Extract the date in the given content in the format of MM/DD/YYYY."}]

messages = json.load(open('dates_few_shots.json'))

for message in messages:
    gpt_prompt += [{"role": "user", "content": message['input']}]
    gpt_prompt += [{"role": "assistant", "content": message['output']}]

input_df = pd.read_csv('consolidated_records.csv')
key = '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'

df = input_df
for row in df.iterrows():
    if str(row[1]['Due Date']) != 'nan':
        print("Due date is : ", row[1]['Due Date'])
        try:
            prompt = gpt_prompt + [{"role": "user", "content": f"{row[1]['Due Date']}"}]
            output = get_chat_gpt_response(openai_api_key=key, messages=prompt)
            df.loc[[row[0]], ['Due Date']] = output
        except:
            print(f"This row has issues with Due date: Given Due date is {row[1]['Due Date']}")

df.to_csv('extract_address_dates.csv', index=False)
