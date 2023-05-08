#find the volume and surface area of a cube
# Input: side length
# Output: volume and surface area

import math

#details of the cube
cube = {"surface area": 0, "volume": 0, "side length": 0}


#input side length
def input():
    cube["side length"] = input("Enter the side length of the cube: ")
    
#find the volume and surface area
def find():
    cube["volume"] = math.pow(cube["side length"], 3)
    cube["surface area"] = 6 * math.pow(cube["side length"], 2)

#run the program
def run():
    input()
    find()
    print("The volume of the cube is", cube["volume"], "and the surface area is", cube["surface area"])

run()
