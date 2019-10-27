import os, subprocess
import cv2
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont

import img2pdf
from PIL import Image as img1

pdf_dir = r"C:\Users\Admin\PycharmProjects\certificate_generator"
os.chdir(pdf_dir)
pdftoppm_path = r"C:\Program Files (x86)\Poppler\poppler-0.68.0\bin\pdftoppm.exe"


names = ['VAMSHI K.V.','SYED AMEEM SAEED',
         'MOHAMMED ARMAAN', 'SYED ZEESHAN',
         'UMER AHMED R','A  MOHAMAD YUNUS']

for i in range(len(names)):
    for pdf_file in os.listdir(pdf_dir):

        if pdf_file.endswith("participation.pdf"):
            subprocess.Popen('"%s" -jpeg %s out' % (pdftoppm_path, pdf_file))

    #conversion to image complete

    #image processing begins
    img = cv2.imread('out-1.jpg')
    font = ImageFont.truetype("arial.ttf", 60)
    im = Image.open("out-1.jpg")
    draw = ImageDraw.Draw(im)
    text = names[i]

    #print(ImageFont.getsize(text, font))
    mask = ImageFont.getmask(text, font)

    textsize = ImageFont.getsize(text, font)
    # get coords based on boundary
    textX = int((img.shape[1] - textsize[0]) / 2)
    textY = (img.shape[0] + textsize[1]) / 2

    # add text centered on image
    # cv2.putText(img, text, (textX, 670), font, 4, (37,30,2), 2)
    draw.text((textX, 600), text, font=font, fill=(3,31,53))

    #cv2.imwrite('out-final.jpg', img)
    im.save('temp.jpg')





    #conversion of image to pdf

    img_path = "temp.jpg"

    # storing pdf path
    path_var = "C:/Users/Admin/Desktop/TechMaze 1.0/named_certificates/"+names[i] + ".pdf"
    pdf_path = path_var

    # opening image
    image = img1.open(img_path)

    # converting into chunks using img2pdf
    pdf_bytes = img2pdf.convert(image.filename)

    # opening or creating pdf file
    file = open(pdf_path, "wb")

    # writing pdf files with chunks
    file.write(pdf_bytes)

    # closing image file
    image.close()

    # closing pdf file
    file.close()

    # output
    print()
    print()

    print(names[i], "    :     Successfully generated Certificate of Participation")
print()
print()
print('Check all Certificates now.')