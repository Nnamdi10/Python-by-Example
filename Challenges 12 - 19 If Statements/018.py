# ask the user to enter a number
num=float(input("Enter a number: "))

# if it is under 10, display the message "Too low"
if num<10:
    print("Too low")

# if their number is between 10 and 20, display "Correct"
elif num>=10 and num<=20:
    print("Correct")

# otherwise display "Too high"
else:
    print("Too high")