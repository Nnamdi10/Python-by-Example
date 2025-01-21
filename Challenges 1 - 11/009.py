#input number of days
nod=int(input("Input the number of days: "))

#hours
hours=nod * 24

#minutes
minutes=nod * hours

#seconds
seconds=nod * minutes

print("We've", hours,"Hours", minutes,"Minutes", seconds,"Seconds", "in", nod, "days")