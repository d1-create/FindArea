#find area and perimeter of a rectangle

#declare dictionary of rectangle details
rectangle = {"SideLength": None, "Area": None, "Perimeter": None}

#get side length from user
def getSideLength():
    rectangle["SideLength"] = float(input("Enter the side length of the rectangle: "))
    return rectangle["SideLength"]

#calculate area and perimeter from side length
def getArea():
    rectangle["Area"] = rectangle["SideLength"] * rectangle["SideLength"]
    return rectangle["Area"]

def getPerimeter():
    rectangle["Perimeter"] = rectangle["SideLength"] * 4
    return rectangle["Perimeter"]

#display area and perimeter
def displayData():
    print("The area of the rectangle is: ", rectangle["Area"])
    print("The perimeter of the rectangle is: ", rectangle["Perimeter"])
  
#run program  
def main():
    getSideLength()
    getArea()
    getPerimeter()
    displayData()

main()
