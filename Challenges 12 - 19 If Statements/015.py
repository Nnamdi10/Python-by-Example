# ask the user to enter their favourite colour.
lour=input("What's your favourite colour: ")

# if they enter "red", "RED" or "Red" display the message "I like red too"
if lour=="red" or lour=="RED" or lour=="Red":
    print("I like red too")

# otherwise display the message "I don't like [colour], I prefer red"
else:
    print("I don't like", lour, "I prefer red")