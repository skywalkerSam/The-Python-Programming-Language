"""
Programmer: Sam Skywalker
Purpose: Learning
Date: 12022.04.22.18:29
"""

from ctypes import resize
from PIL import Image, ImageFilter
from matplotlib.pyplot import show

img_one = Image.open('./src_images/crush_one.png')
print(img_one)

print(img_one.size)
print(img_one.mode)

# print(dir(img_one))


blured_image = img_one.filter(ImageFilter.BLUR)
# blured_image.save("./src_images/crush_blur_one.png")

                                
smooth_image = img_one.filter(ImageFilter.SMOOTH)
# smooth_image.save("./src_images/crushone_smooth.png")


img_two = Image.open("./src_images/crushone_blured.png")
# img_one.show()
print(img_two)

sharpen_img = img_one.filter(ImageFilter.SHARPEN)
# sharpen_img.save("./src_images/crushone_sharpen.png")


filteredimg_one = img_one.convert("L")
# filteredimg_one.save("./src_images/crushone_filterONE.png")

# filteredimg_one.show()


upsidedown_img = filteredimg_one.rotate(180)
# upsidedown_img.show()
# upsidedown_img.save("./src_images/crushone_upsidedown.png")


resize_img = img_one.resize((600, 600))
resize_img.save("./src_images/crushone_profile.png")


box = (250, 250, 900, 900)
croped_img = img_one.crop(box)
croped_img.show()
# croped_img.save("./src_images/crushone_small_img.png")


