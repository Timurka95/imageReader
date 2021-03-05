import pytesseract
from PIL import Image, ImageEnhance

pytesseract.pytesseract.tesseract_cmd = 'D:\\Program Files (x86)\\Python3_8_2\\Scripts\\Tesseract\\tesseract.exe'

img = Image.open('test3.jpg')

# подрезать изображение, если на картинке не только циферблат

desaturate = ImageEnhance.Color(img)
img = desaturate.enhance(0)
brightness = ImageEnhance.Brightness(img)
img = brightness.enhance(2.7)
contrast = ImageEnhance.Contrast(img)
img = contrast.enhance(7)

img.save("testCont.jpg")

config = r'--oem 3 --psm 7'
text = pytesseract.image_to_string(img, config=config)
# outText = ''
#
# for s in text.split():
#     if s.isdigit():
#         outText += s
#
# print(outText[0:5] + ',' + outText[5:8])

print(text[0:5] + ',' + text[5:8])
