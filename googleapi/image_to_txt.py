import os
import tempfile
from base64 import b64encode

import googleapiclient.discovery
import pypdfium2 as pdfium
from oauth2client.client import GoogleCredentials


def convert_pdf_to_image(pdf_file_path, temp_folder):
    pdf = pdfium.PdfDocument(pdf_file_path)
    n_pages = len(pdf)
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render(scale=300 / 72).to_pil()
        pil_image.save(temp_folder + f"/image_{page_number + 1}.jpg")


def image_to_text(pdf_file_path, credentials_file_path, output_path, output_file_name):
    with tempfile.TemporaryDirectory() as temp_folder:
        convert_pdf_to_image(pdf_file_path, temp_folder)

        credentials = GoogleCredentials.from_stream(credentials_file_path)
        service = googleapiclient.discovery.build('vision', 'v1', credentials=credentials)
        for filename in os.listdir(temp_folder):
            image_file = os.path.join(temp_folder, filename)
            with open(image_file, "rb") as f:
                image_data = f.read()
                encoded_image_data = b64encode(image_data).decode('UTF-8')

            batch_request = [{'image': {'content': encoded_image_data},
                              'features': [{'type': 'TEXT_DETECTION'}]}]
            request = service.images().annotate(body={'requests': batch_request})

            response = request.execute()

            if 'error' in response:
                raise RuntimeError(response['error'])

            extracted_texts = response['responses'][0]['textAnnotations']

            extracted_text = extracted_texts[0]
            # print(extracted_text['description'])

            with open(output_path + "/"+output_file_name + ".txt", "a") as file:
                file.write(extracted_text['description'])

            # print(extracted_text['boundingPoly'])
