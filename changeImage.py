#!/usr/bin/env python3

from PIL import Image
from pathlib import Path

size = (600, 400)
paths = Path("supplier-data/images").glob("*.tiff")
for im_path in paths:
    outfile = str(im_path.parent) + "/" + str(im_path.stem) + ".jpeg"
    print(outfile)
    with Image.open(im_path) as im:
        if im.mode != "RGD":
            im = im.convert("RGB")
            im.thumbnail(size=size)
            print(im.mode)
            im.save(outfile)
# for path in paths:
#     compress_image(path, path.stem + ".jpg")
