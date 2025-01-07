import sys
from PIL import Image, ImageOps
import os

supported_types = ['.png', '.jpeg', '.jpg']

imported = os.path.splitext(sys.argv[1])
exported = os.path.splitext(sys.argv[2])

if exported[1] == supported_types[0] or exported[1] == supported_types[1] or exported[1] == supported_types[2]:
    if imported[1] == supported_types[0] or imported[1] == supported_types[1] or imported[1] == supported_types[2]:
        with Image.open("shirt.png") as shirt:
            with Image.open((imported[0]+imported[1])) as im:
                if im.size == shirt.size:
                    im.paste(shirt, box=(0,0), mask=shirt)
                    im.save(exported[0]+exported[1], format=None)
                    print("1")
                else:
                    im = ImageOps.fit(im, shirt.size)
                    im.paste(shirt, box=(0,0), mask=shirt)
                    im.save(exported[0]+exported[1])
                    print("2")
else:
    print("Unsupported arguments.")
    sys.exit(1)
