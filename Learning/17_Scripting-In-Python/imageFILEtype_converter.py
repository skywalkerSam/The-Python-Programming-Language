"""
Developer: Sam Skywalker
Purpose: Image Type Conversion
Date: 12022.05.04.03:13
"""


from PIL import Image, ImageFilter
import sys
import os
from matplotlib.pyplot import show


script_name = sys.argv[0]
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# print("\n\n\t", script_name, "\n\n", image_path, "\n\n", output_path, "\n")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    image = Image.open(f"./{image_folder}/{filename}")
    clean_name = os.path.splitext(filename)[0]
    image.filter(ImageFilter.SHARPEN)
    image.save(f"./{output_folder}/{clean_name}.png", "png")
    print("\n\t\t New Image Creation Successful :) \n")
    # image.show()




"""
>_ Command Used:   python .\imageFILEtype_converter.py ./pokemons ./pokemons_new


"""
