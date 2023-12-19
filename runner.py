import os

from chat_gpt.find_address import get_chat_gpt_response
from googleapi.image_to_txt import image_to_text

input_folder = "sample_pdf"
output_folder = "output_images"
credential_file_path = "credentials.json"
# openai_api_key = "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"
# prompts = "What is the name of company, address of company, account number, total bill from the following text ?"

for filename in os.listdir(input_folder):
    pdf_file_path = os.path.join(input_folder, filename)
    os.makedirs(output_folder, exist_ok=True)
    output_file_name = filename[:-4]

    # Cloud Vision API to convert pdf to text
    image_to_text(pdf_file_path, credential_file_path, output_folder, output_file_name)

    # input_file_path = os.path.join(output_folder, output_file_name + ".txt")

    # # Chat GPT API to extract features
    # get_chat_gpt_response(openai_api_key, input_file_path, prompts)
