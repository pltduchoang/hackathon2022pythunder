print("TESTING AIWPJUODFHSIJ:FHUOHDSI2342rds")
# Ratio of crime rate of population individually

import class_of_anything as c
import os

# cwd = os.getcwd(r"c:\Users\emagt\OneDrive\Desktop\Hackathon\hackathon2022pythunder")  # Get the current working directory (cwd)
# files = os.listdir(cwd)  # Get all the files in that directory
object_list = []
community = []
count = []


def readFile():
    with open("test.txt", "r") as file:
        l = 1
        for line in file:
            if l == 1:
                l += 1
                continue
            items = line.rstrip().split(",")
            print(items)
            object = (c.pythunder(items[0],items[1],items[2],int(items[3]),int(items[4]),items[5],int(items[6]),items[8]))
            print(object)
            object_list.append(str(object))
            print(object_list)
            print(items[1])
            print(items[3])
            community.append(items[1])
            count.append(items[3])
        file.close()

def mathThing():
    count = {i:ciunt}

if __name__ == "__main__":
    readFile()