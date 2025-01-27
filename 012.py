# ask for two numbers.
fn=float(input("Enter first number: "))
sn=float(input("Enter second number: "))

# if the first one is lager than the second, 
# display the second number first and then the first number
if fn > sn:
    print(sn, fn)

# otherwise show first number first and then second.
else:
    print(fn, sn)
