import os

import pypdfium2 as pdfium


def convert_pdf_to_image(pdf_file_path, temp_folder):
    print(pdf_file_path)
    pdf = pdfium.PdfDocument(pdf_file_path)
    n_pages = len(pdf)
    print(n_pages)
    for page_number in range(n_pages):
        page = pdf.get_page(page_number)
        pil_image = page.render(scale=300 / 72).to_pil()
        pil_image.save(temp_folder + f"image_{page_number + 1}.jpg")


convert_pdf_to_image(
    "/Users/umeshkumar/PycharmProjects/text_extraction/sample/SP Troy - Electric 08.09.22 to 09.09.22 - AES Ohio.pdf",
    "")

input_folder = "/Users/umeshkumar/PycharmProjects/text_extraction/sample"
output_folder = "../../output_images"
for filename in os.listdir(input_folder):
    file = os.path.join(input_folder, filename)
    convert_pdf_to_image(file, output_folder)
