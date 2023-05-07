#find area and perimeter of a triangle

#store triangle details in a dictionary
triangle = {"Area":None, "Perimeter":None, "SideLength":None}

import math

#function to start collecting data
def start():
    print("Finding the area and perimeter of a triangle\n")
    sidelength = float(input("Enter the length of one side of the triangle: "))
    triangle["SideLength"] = sidelength

#function to find area
def findarea():
    print("Finding the area of the triangle\n")
    area = (triangle["SideLength"]**2)/2
    triangle["Area"] = area

#function to find perimeter
def findperimeter():
    print("Finding the perimeter of the triangle\n")
    perimeter = triangle["SideLength"]*3
    triangle["Perimeter"] = perimeter

#function to print results
def printresults():
    print("The area of the triangle is: ", triangle["Area"])
    print("The perimeter of the triangle is: ", triangle["Perimeter"])

#function to run everything
def run():
    start()
    findarea()
    findperimeter()
    printresults()

#run the program
run()
