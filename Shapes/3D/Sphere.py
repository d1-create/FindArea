#script to find the surface area and volume of a sphere

import math

def inputs():
    radius = float(input("Enter the radius of the sphere: "))
    return radius

def surface_area(radius):
    surface_area = 4 * math.pi * radius**2
    return surface_area

def volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def main():
    radius = inputs()
    print("The surface area of the sphere is", surface_area(radius))
    print("The volume of the sphere is", volume(radius))
    
main()
