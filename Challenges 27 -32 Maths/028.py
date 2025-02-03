import math

# ask the user to enter a number with lots of decimal places.
ln=float(input("Enter a number with lots of decimal places: "))

# multiply this number by two and display the answer
ans=ln*2
# print(ans)

# update program 027 so that it will display the answer to two decimal places.
print(round(ans,2))