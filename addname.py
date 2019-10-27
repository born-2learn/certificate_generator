import cv2
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont

img = cv2.imread('out-1.jpg')
names = ['VAMSHI K.V.','SYED AMEEM SAEED','MOHAMMED ARFATH AHMED',
         'MOHAMMED ARMAAN', 'SYED ZEESHAN', 'MUHAMMAD EASA',
         'UMER AHMED R','YUNUS']



font1 = cv2.FONT_HERSHEY_PLAIN

font = ImageFont.truetype("arial.ttf", 70)
im = Image.open("out-1.jpg")
draw = ImageDraw.Draw(im)
text = names[0]


print(ImageFont.getsize(text, font))
mask = ImageFont.getmask(text, font)

textsize = ImageFont.getsize(text,font)
# get coords based on boundary
textX = int((img.shape[1] - textsize[0]) / 2)
textY = (img.shape[0] + textsize[1]) / 2

# add text centered on image
#cv2.putText(img, text, (textX, 670), font, 4, (37,30,2), 2)
draw.text((textX,600), text, font=font, fill=(3,31,53))



cv2.imwrite('out-final.jpg',img)
im.save('hello.jpg')
#cv2.imshow("mask", mask)
#im.show()
