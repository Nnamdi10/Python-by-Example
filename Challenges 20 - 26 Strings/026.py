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