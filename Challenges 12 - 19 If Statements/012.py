# ask for two numbers.
fn=float(input("Enter first number: "))
sn=float(input("Enter second number: "))

# if the first one is larger than the second, display the second number first and then the first number
if fn>sn:
    print(sn,fn)

# otherwise show the first number first and then the second
else:
    print(fn,sn)