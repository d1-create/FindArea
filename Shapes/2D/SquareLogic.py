square = {"Area":None, "SideLength":None, "Perimeter":None}

#store the side length of the square
square["SideLength"] = int(input("Enter the side length of the square: "))
print("\n")

#find permieter and store it
square["Perimeter"] = square["SideLength"] * 4

#find the area of the square and store it
square["Area"] = square["SideLength"] * square["SideLength"]

#print the area of the square and the perimeter of the square
print("The area of the square is: ", square["Area"], "cm^2", " And the perimeter of the square is: ", square["Perimeter"], "cm", "\n")
