#find surface area and volumme of a cuboid
#cuboid details
cuboid = {"length":None, "width":None, "height":None, "surface area":None, "volume":None}

#input from user
def userinput():
    cuboid["length"] = float(input("Enter the length of the cuboid: "))
    cuboid["width"] = float(input("Enter the width of the cuboid: "))
    cuboid["height"] = float(input("Enter the height of the cuboid: "))
    
#find surface area and volume
def find():
    cuboid["surface area"] = 2 * (cuboid["length"] * cuboid["width"] + cuboid["width"] * cuboid["height"] + cuboid["height"] * cuboid["length"])
    cuboid["volume"] = cuboid["length"] * cuboid["width"] * cuboid["height"]

#print output 
def output():
    print("Surface area of cuboid is: ", cuboid["surface area"], " and volume of cuboid is: ", cuboid["volume"]) 

def run():
    userinput()
    find()
    output()
    
run()
