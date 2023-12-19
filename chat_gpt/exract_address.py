import json

import openai
import pandas as pd


def get_chat_gpt_response(openai_api_key, messages):
    openai.api_key = openai_api_key

    messages = messages

    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    output = chat.choices[0].message.content
    print("Output address is : ", output)
    print("*" * 20)
    return json.loads(output)


gpt_prompt = [{"role": "system", "content": "For the given content extract only address, city, state, zip-code "
                                            "as python dictionary and trim other information.Find proper address "
                                            "even though the content is not properly aligned. Also given some "
                                            "few shots to learn."}]

messages = json.load(open('few_shots.json'))

for message in messages:
    gpt_prompt += [{"role": "user", "content": message['input']}]
    gpt_prompt += [{"role": "assistant", "content": json.dumps(message['output'])}]

input_df = pd.read_csv('consolidated_records.csv')
key = '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'
input_df[['customer-address', 'customer-city', 'customer-state', 'customer-zipcode']] = ''
input_df[['remittance-address', 'remittance-city', 'remittance-state', 'remittance-zipcode']] = ''

df = input_df
for row in df.iterrows():
    if str(row[1]['Customer Address']) != 'nan':
        print("Customer address is : ", row[1]['Customer Address'])
        try:
            prompt = gpt_prompt + [{"role": "user", "content": f"{row[1]['Customer Address']}"}]
            output = get_chat_gpt_response(openai_api_key=key, messages=prompt)
            df.loc[[row[0]], ['customer-address']] = str(output['address'])
            df.loc[[row[0]], ['customer-city']] = str(output['city'])
            df.loc[[row[0]], ['customer-state']] = str(output['state'])
            df.loc[[row[0]], ['customer-zipcode']] = str(output['zip-code'])
        except:
            print(f"This row has issues with Customer address: Given address is {row[1]['Customer Address']}")

    if str(row[1]['Remittance address']) != 'nan':
        print("Remittance address is : ", row[1]['Remittance address'])
        try:
            prompt = gpt_prompt + [{"role": "user", "content": f"{row[1]['Remittance address']}"}]
            output = get_chat_gpt_response(openai_api_key=key, messages=prompt)
            df.loc[[row[0]], ['remittance-address']] = str(output['address'])
            df.loc[[row[0]], ['remittance-city']] = str(output['city'])
            df.loc[[row[0]], ['remittance-state']] = str(output['state'])
            df.loc[[row[0]], ['remittance-zipcode']] = str(output['zip-code'])
        except:
            print(f"This row has issues with Remittance address: Given address is {row[1]['Remittance address']}")

df.to_csv('extract_address.csv', index=False)
