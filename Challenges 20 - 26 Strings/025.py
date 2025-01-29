# ask the user to enter their first name.
fn=(input("Enter firstname: ")).upper()
fnl=len(fn)

# if the length of their first name is under five characters, ask them to enter their surname and join them together (without a space)
if fnl<5:
    sn=(input("Surname: ")).upper()

# and display the name in upper case.
    print(fn+sn)

# if the length of the first name is five or more characters, display their first name in lower case.
elif fnl>5:
        fn=fn.lower()
        print(fn)
else:
    print("nah!")

