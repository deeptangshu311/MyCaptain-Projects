#for circle area with radius

import math

rad = float(input("Input the radius of circle:"))

a = rad**2

area = math.pi * a

print("Area of the circle with radius", rad ,"is", area)



#for file name follow the code below



filename = input("Enter file name")

K = filename.split(".")

print("Extension of file is:" +K[-1])

