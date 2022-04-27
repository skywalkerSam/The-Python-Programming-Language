"""
Programmer: Sam Skywalker
Purpose: Learning
Date: 12022.04.22.18:29
"""

from PIL import Image, ImageFilter

img_one = Image.open('./src_images/Gwen_Stacy.jpg')
print(img_one)

print(img_one.size)
print(img_one.mode)

print(dir(img_one))


bluredimage_one = img_one.filter(ImageFilter.BLUR)
# bluredimage_one.save("./src_images/bluredimage_one.png")



