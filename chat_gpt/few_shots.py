import json

messages = json.load(open('few_shots.json'))

content = ''
result = []
input_string = "Input:"
output_string = "Output :"

for message in messages:
    # print(json.loads(message['content']))
    input_str_id = message['content'].index(input_string)
    output_str_id = message['content'].index(output_string)

    input = ''
    # getting elements in between
    for idx in range(input_str_id + len(input_string) + 1, output_str_id):
        input = input + message['content'][idx]

    output = ''
    # getting elements in between
    for idx in range(output_str_id + len(output_string), len(message['content'])):
        output = output + message['content'][idx]
    result += [{"input": input, "output": output}]
    content += message['content'] + " \n\n"

print(result)

json.dump(result, open('few_shots.json', 'w'))
# print(content)
