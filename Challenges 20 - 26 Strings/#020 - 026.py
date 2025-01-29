#020
# # ask the user to enter their first name and then display the lenght of their name.
fn=input("Enter your firstname: ")
print(len(fn))


#021
# ask the user to enter their first name and then ask them to enter their surname.
fn=input("Enter first name: ")
sn=input("Enter surname: ")

# join them together with a space between and display the name and the lenght of whole name
print(fn,sn)
print(len(fn))
print(len(sn))


#022
# ask the user to enter their first name and surname in lower case.
fn=input("Enter first name: ").lower()
sn=input("Enter surname: ").lower()

# change the case to title case and join them together.
tot=(fn+sn).title()

# display the finished result
print(tot)


#023
# ask the user to type in the first line of a nursery rhyme and display the length of the string.
nr=input("Type in the first line of a nursery rhyme: ")

# ask for a starting number and an ending number and then display just that section of the text
# (remember python starts counting from 0 and not 1)
print(len(nr))


#024
# ask the user to type in any word and display it in upper case
user=input("Type in any word: ").upper()
print(user)


#025
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



#026
w=input("Enter a word: ")
f=w[0]
lw=len(w)
rw=w[1:lw]

# pig latin takes the first consonant of a word, moves it to the end of the word and add on an "ay"
if f!="a" and f!="e" and f!="i" and f!="o" and f!="u":
    nw=rw+f+"ay"

# if a word begins with a vowel you just add "way" to the end.
else:
    nw=w+"way"
print(nw.lower())