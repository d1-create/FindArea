#find the volume and surface area of a cube
# Input: side length
# Output: volume and surface area

import math

#details of the cube
cube = {"surface area": None, "volume": None, "side length": None}


#input side length
def inputfind():
    cube["side length"] = float(input("Enter the side length of the cube: "))
    
#find the volume and surface area
def find():
    cube["volume"] = math.pow(cube["side length"], 3)
    cube["surface area"] = 6 * math.pow(cube["side length"], 2)

#run the program
def run():
    inputfind()
    find()
    print("The volume of the cube is", cube["volume"], "and the surface area is", cube["surface area"])

run()

