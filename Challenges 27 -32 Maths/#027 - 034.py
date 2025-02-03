#027
import math

# ask the user to enter a number with lots of decimal places.
ln=float(input("Enter a number with lots of decimal places: "))

# multiply this number by two and display the answer
ans=ln*2
print(ans)


#028
import math

# ask the user to enter a number with lots of decimal places.
ln=float(input("Enter a number with lots of decimal places: "))

# multiply this number by two and display the answer
ans=ln*2
# print(ans)

# update program 027 so that it will display the answer to two decimal places.
print(round(ans,2))


#029
import math

# ask the user to enter an integer that is over 500.
ln=float(input("Enter an integer that is over 500: "))

# work out the square root of that number
sr=math.sqrt(ln)

# and display it to two decimal place
print(round(sr,2))


#030
import math

# display pi to five decimal places
print(round(math.pi,5))


#031
import math

# ask the user to enter the radius of a circle(measurement from the centre point to the edge).
rc=float(input("Enter the radius of the circle: "))

# work out the area of the circl(pia*radius squared)
ac=math.pi*(rc**2)

print(ac)


#032
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


#033
import math

# ask the user to enter two numbers.
fn=float(input("Enter first number: "))
sn=float(input("Enter second number: "))

# use whole number division to divide the first number by the second
wnd=fn//sn

# and also work out the remainder
rnd=fn%sn

# and display the answer in a friendly way
# (e.g. if they enter 7 and 2 display "7 divided by 2 is 3 with 1 remaining")

print (fn,"divided by", sn ,"is", wnd ,"with", rnd, "remaining")


#034
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
