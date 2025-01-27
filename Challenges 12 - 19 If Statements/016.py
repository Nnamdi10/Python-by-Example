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

    