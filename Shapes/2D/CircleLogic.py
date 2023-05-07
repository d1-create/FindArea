#find area and perimeter of a circle

#import libraries
import math

# define main function
def main():
    radius = eval(input("Enter the radius of the circle: "))
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    print("The area of the circle is", area,"and the perimeter is", perimeter)
  
#run code  
main()
