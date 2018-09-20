import sys
import os
from PIL import Image
import numpy as np

def format_all_samples(path="Dataset/"):
    assert os.path.isdir(path), "Path not defined"

    for filename in os.listdir(path):
        if filename[0] != ".":
            img = Image.open(os.path.join(path, filename))
            img = img.convert("L")
            img = img.resize((32, 32))
            img = img.point(lambda x: 0 if x<128 else 255, 'L')
            
            img.save(os.path.join("Dataset_Formatted/", filename))
            
            #arr = np.array(img)
            #np.set_printoptions(threshold=np.inf)
            #print(arr)



assert os.path.isdir("Dataset/"), "Dataset folder not found"




def load_data():
    print("loading data")
    # return as a matrix
    # returns (img, ans), (img_test, ans_test)

sFiles = 0
uFiles = 0
dFiles = 0

sCount = 0
uCount = 0
dCount = 0

for filename in os.listdir("Dataset/"):
    if filename[0] == "s":
        sFiles += 1

        #sCount += 1
        #os.rename(filename, "s-" + str(sCount) + ".jpg")

    elif filename[0] == "d":
        dFiles += 1

        #dCount += 1
        #os.rename(filename, "d-" + str(dCount) + ".jpg")

    elif filename[0] == "u":
        uFiles += 1

        #uCount += 1
        #os.rename(filename, "u-" + str(uCount) + ".jpg")

print("sFiles: " + str(sFiles))
print("dFiles: " + str(dFiles))
print("uFiles: " + str(uFiles))
print("Total: " + str(uFiles + sFiles + dFiles))

format_all_samples()