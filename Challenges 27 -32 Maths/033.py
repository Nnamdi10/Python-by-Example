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