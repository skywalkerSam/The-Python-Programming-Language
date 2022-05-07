"""
Developer: Sam Skywalker
Purpose: Learning   
Date: 12022.05.03.23:19
"""

from PIL import Image, ImageFilter
from matplotlib.pyplot import show


with Image.open("./src_images/Strawberry_Attack.jpg") as img:
    print(img)
    print(img.mode)
    print(img.size)
    # img.show()

    resized_img = img.resize((900, 900))
    # resized_img.show()
    # resized_img.save("./src_images/Strawberry_profile.png")

    resized_img.thumbnail((600, 600))
    resized_img.show()
    resized_img.save("./src_images/Strawberry_thumbnail.png")









