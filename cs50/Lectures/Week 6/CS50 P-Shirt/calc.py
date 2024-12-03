from PIL import Image
with Image.open("./shirt.png") as im:
    print(im.size)