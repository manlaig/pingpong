from PIL import Image
import os, sys
import glob

location = str(sys.argv[1])
degree = int(sys.argv[2])

assert os.path.isdir(location), "Invalid path"

images = glob.glob(os.path.join(location, "*.jpg"))
for image in images:
    with open(image, 'rb') as f:
        img = Image.open(f)
        img = img.rotate(degree)
        img.save(image)