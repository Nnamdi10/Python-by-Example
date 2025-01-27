#001 - 011

#001
first_name=input("What is your first name?:  ")
print("Hello", first_name)


#002
first_name=input("What's your first name?: ")
surname=input("What's your surname?: ")
print("Hello", first_name, surname)


#003
print("What do you call a bear wit no teeth? \n A gummy bear!")


#004
#Ask the user to input 2 numbers
first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))

#Sum of both numbers
total=first_number + second_number

print("The total is", total)


#005
#Ask user to input 3 numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

#Sum the first 2 numbers
add_n=num1 + num2

#Multiply sum and 3rd number
total=add_n * num3

print("The answer is", total)


#006
#Initial number of slices
inos=int(input("Input initial number of slices: "))

#Number of slices eaten
nose=int(input("How many slices have you eaten?: "))

#Determining what is left
wilf=inos - nose

print(wilf, "slices left, you love pizza")


#007
#input name
nnaammee=input("What is your name?: ")

#input age
aaggee=int(input("How old are you?: "))

#add 1 to inputted age
agee=aaggee + 1

print(nnaammee,"next birthday you will be", agee)


#008
#total price of bill
tpob=int(input("Input the total price of the bill?: "))

#number of diners
nod=int(input("Input the number of diners?: "))

#divide the total bill by the number of diners
toco=tpob / nod

print("Each person must pay", toco)


#009
#input number of days
nod=int(input("Input the number of days: "))

#hours
hours=nod * 24

#minutes
minutes=nod * hours

#seconds
seconds=nod * minutes

print("We've", hours,"Hours", minutes,"Minutes", seconds,"Seconds", "in", nod, "days")


#010
#pounds to kilogram
kilog=2204

#enter weight
iw=int(input("Enter weight in kilogram: "))

#convertion to pounds
ctp=kilog * iw

print(ctp)


#011
#input number over 100
bn=int(input("Enter a number over 100: "))

#input number below 10
sn=int(input("Enter a number below 10: "))

#how many times sn goes into bn
divs=bn/sn

print("The smaller number goes into the larger number", divs, "times.")