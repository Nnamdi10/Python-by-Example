# ask the user to enter 1,2 or 3
num=int(input("Enter 1, 2 or 3: "))

# if they enter a 1, display the message "Thank you"
if num==1:
    print("Thank you")

# if they enter a 2, display "Well done"
elif num==2:
    print("Well done")

# if they enter a 3, display "Correct"
elif num==3:
    print("Correct")

# if they enter anything else, display "Error message"
else:
    print("Error message")