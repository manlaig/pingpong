import sys
import os

assert os.path.isdir("Dataset/"), "Dataset folder not found"

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