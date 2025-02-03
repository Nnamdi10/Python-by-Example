import math

# ask for the radius and depth of a cylinder and work out the total volume
ra=float(input("Enter the radius of the circle: "))
dc=float(input("Enter the depth of the circle: "))

# work out the area of the circl(pia*radius squared)
ca=math.pi*(ra**2)

# (circle area * depth)
tv=ca*dc

# rounded to three decimal places
print(round(tv,3))