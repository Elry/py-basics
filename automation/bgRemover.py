from rembg import remove
from PIL import Image

img_path = input("Please enter image path with file type: ")

output_path = input("Please enter image path with file name for the output: ")
output_path = output_path + ".png"

input = Image.open(img_path)
output = remove(input)

output.save(output_path, 'PNG')
