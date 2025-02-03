import math

# display the following messages:


# enter a number:
print("(1) Square\n(2) Triangle")
sf=float(input("Enter a number: "))
if sf!=1 and sf!=2:
    print("Enter either 1 0r 2!")

# s
# if the user enter 1, then it should ask them for the lenght of one of it's sides and display the area.
if sf==1:
    sqa=float(input("Enter the lenght of one side of the square: "))
    print(sqa**2)

# t
# if they select 2, it should ask for the base and height of the triangle and display the area.
if sf==2:
    trb=float(input("Enter the base of the triangle: "))
    trh=float(input("Enter the height of the triangle: "))
    tra=(trb*trh)/2
    print(tra)
