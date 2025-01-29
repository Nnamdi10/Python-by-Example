# ask the user to enter their first name and surname in lower case.
fn=input("Enter first name: ").lower()
sn=input("Enter surname: ").lower()

# change the case to title case and join them together.
tot=(fn+sn).title()

# display the finished result
print(tot)