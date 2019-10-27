import os
from pdf2image import convert_from_path

pdf_dir = r"C:\Users\Admin\PycharmProjects\certificate_generator"
os.chdir(pdf_dir)

for pdf_file in os.listdir(pdf_dir):

        if pdf_file.endswith(".pdf"):

            pages = convert_from_path(pdf_file, 300)
            pdf_file = pdf_file[:-4]

            for page in pages:

               page.save("%s-page%d.jpg" % (pdf_file,pages.index(page)), "JPEG")