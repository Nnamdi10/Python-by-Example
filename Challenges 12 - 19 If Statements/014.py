# ask the user to enter a number between 10 and 20(inclusive).
num=float(input("Enter a number between 10 and 20: "))

# if they enter a number within this range, display the message "Thank you"
if num<=20 and num>=10:
    print("Thank you")

# otherwise display the message "Incorrect answer"
else:
    print("Incorrect answer")