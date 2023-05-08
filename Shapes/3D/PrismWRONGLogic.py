#create a script to make the volume and surface area of a prism, with the length, width, and height as inputs

#input
prism = {"Length":None, "Width":None, "Height":None, "Volume":None, "Surface Area":None, "Type":None, "sides":None}

#find the length, width, and height
def inputs():
    prism["Length"] = float(input("Length: "))
    prism["Width"] = float(input("Width: "))
    prism["Height"] = float(input("Height: "))
    #input type of prism
    prism["Type"] = input("Type of Prism: ")
    prism["sides"] = int(input("Number of sides as 2D shape (Tirangular = 3): "))
    

#calculate the volume
def volume():
    if(prism["Type"] == "Triangular"):
        prism["Volume"] = (prism["Length"] * prism["Width"] * prism["Height"]) / 2
    elif prism["Type"] == "Cuboid":
        prism["Volume"] = prism["Length"] * prism["Width"] * prism["Height"]
    elif prism["Type"] == "Pentagonal":
        prism["Volume"] = (prism["Length"] * prism["Width"] * prism["Height"]) / 5
    else:
        prism[volume] = (prism["Length"] * prism["Width"] * prism["Height"]) / prism["sides"]
        
def surfacearea():
    if (prism["Type"] == "Triangular"):
        prism["Surface Area"] = (prism["Length"] * prism["Width"]) + (prism["Length"] * prism["Height"]) + (prism["Width"] * prism["Height"])
    elif prism["Type"] == "Cuboid":
        prism["Surface Area"] = 2 * ((prism["Length"] * prism["Width"]) + (prism["Length"] * prism["Height"]) + (prism["Width"] * prism["Height"]))
    elif prism["Type"] == "Pentagonal":
        prism["Surface Area"] = 5 * ((prism["Length"] * prism["Width"]) + (prism["Length"] * prism["Height"]) + (prism["Width"] * prism["Height"]))
    else:
        prism["Surface Area"] = prism["sides"] * ((prism["Length"] * prism["Width"]) + (prism["Length"] * prism["Height"]) + (prism["Width"] * prism["Height"]))
        
        
def main():
    inputs()
    volume()
    surfacearea()
    print("The volume of the prism is", prism["Volume"], "and the surface area is", prism["Surface Area"], ".")
    
main()

