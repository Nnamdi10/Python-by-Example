#012
# ask for two numbers.
fn=float(input("Enter first number: "))
sn=float(input("Enter second number: "))

# if the first one is larger than the second, display the second number first and then the first number
if fn>sn:
    print(sn,fn)

# otherwise show the first number first and then the second
else:
    print(fn,sn)


#013
# ask the user to enter a number that is under 20
num=float(input("Enter a number under 20: "))

# if they enter a number that is 20 or more, display the message "Too high"
if num>=20:
    print("Too high")

# otherwise display "Thank you"
else:
    print("Thank you")


#014
# ask the user to enter a number between 10 and 20(inclusive).
num=float(input("Enter a number between 10 and 20: "))

# if they enter a number within this range, display the message "Thank you"
if num<=20 and num>=10:
    print("Thank you")

# otherwise display the message "Incorrect answer"
else:
    print("Incorrect answer")


#015
# ask the user to enter their favourite colour.
lour=input("What's your favourite colour: ")

# if they enter "red", "RED" or "Red" display the message "I like red too"
if lour=="red" or lour=="RED" or lour=="Red":
    print("I like red too")

# otherwise display the message "I don't like [colour], I prefer red"
else:
    print("I don't like", lour, "I prefer red")


#016
# ask the user if it is raining and convert their answer to lower case
ans=input("Is it raining?: ").lower()
if ans=="yes":

# if they answer "yes", ask if it is windy.
    ans1=input("Is it windy?: ")

# if they answer "yes" to this second question, display the answer "it is too windy for an umbrella"
    if ans1=="yes":
        print("It is too windy for an umbrella")

# otherwise display the message "Take an umbrella".
    else:
        print("Take an umbrella")

# if they did not answer yes to the first question, display the answer "Enjoy your day".
else:
    print("Enjoy your day")


#017
# ask the user's age. If they are 18 or over, display the message "You can vote"
age=int(input("Input your age: "))
if age==18:
    print("You can vote")

# if they are aged 17, display the message "You can learn to drive"
elif age==17:
    print("You can learn to drive")

# if they are 16, display the message "You can buy a lottery ticket"
elif age==16:
    print("You can buy a lottery ticket")

# if they are under 16, display the message "You can go Trick-or-Treating"
elif age < 16:
    print("You can go Trick-or-Treating")
else:
    ()


#018
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


#019
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