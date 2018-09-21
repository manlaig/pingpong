import sys
import os
from PIL import Image
import numpy as np

assert os.path.isdir("Dataset_Formatted/"), "Dataset_Formatted folder not found"


"""
    get a screenshot and resize it to 32 by 32 and change the color space to grayscale
    this is basically formatting the dataset for the training
"""
def format_all_samples(path="Dataset/"):
    assert os.path.isdir(path), "Path not defined"

    for filename in os.listdir(path):
        if filename[0] != ".":
            img = Image.open(os.path.join(path, filename))
            img = img.convert("L")
            img = img.resize((32, 32))
            
            img.save(os.path.join("Dataset_Formatted/", filename))


"""
    get array as input and prepare it to feed through the model
"""
def format_array(array):
    img = Image.fromarray(array, "RGB")
    img = img.convert("L")
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    img = img.rotate(90)
    img = img.resize((32, 32))
    img = img.point(lambda x: 0.0 if x<128 else 1.0, 'L')
    
    img_arr = np.array(img).astype("float32")
    img_arr = img_arr[..., np.newaxis]
    img_arr = img_arr[np.newaxis, :]

    return img_arr



"""
for labels: 0 = UP
            1 = DOWN
            2 = STILL
"""
def load_data(path="Dataset_Formatted/"):
    img = []
    ans = []

    for filename in os.listdir(os.path.join(path)):
        if filename[0] != ".":
            img_sample = Image.open(os.path.join(path, filename))
            img_sample = img_sample.point(lambda x: 0.0 if x<128 else 1.0, 'L')
            img.append(np.array(img_sample))

            if filename[0] == "u":
                ans.append(0)
            elif filename[0] == "d":
                ans.append(1)
            elif filename[0] == "s":
                ans.append(2)
    
    return (img, ans)
    # return (img, ans), (img_test, ans_test)


"""
    prints out how many files for moving UP, DOWN, STILL there is
    and prints out the total file count
"""
def getTotalFileCount():
    sFiles = 0
    uFiles = 0
    dFiles = 0

    for filename in os.listdir("Dataset/"):
        if filename[0] == "s":
            sFiles += 1

        elif filename[0] == "d":
            dFiles += 1

        elif filename[0] == "u":
            uFiles += 1

    print("sFiles: " + str(sFiles))
    print("dFiles: " + str(dFiles))
    print("uFiles: " + str(uFiles))
    print("Total: " + str(uFiles + sFiles + dFiles))
