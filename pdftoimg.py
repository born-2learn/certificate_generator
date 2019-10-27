import os, subprocess

pdf_dir = r"C:\Users\Admin\PycharmProjects\certificate_generator"
os.chdir(pdf_dir)
pdftoppm_path = r"C:\Program Files (x86)\Poppler\poppler-0.68.0\bin\pdftoppm.exe"


names = ['VAMSHI K.V.','SYED AMEEM SAEED','MOHAMMED ARFATH AHMED',
         'MOHAMMED ARMAAN', 'SYED ZEESHAN', 'MUHAMMAD EASA',
         'UMER AHMED R','YUNUS']


for pdf_file in os.listdir(pdf_dir):

    if pdf_file.endswith(".pdf"):

        subprocess.Popen('"%s" -jpeg %s out' % (pdftoppm_path, pdf_file))