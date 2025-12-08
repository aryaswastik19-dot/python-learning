# if-elif-else: Do some code only when IF some condition is True
#               Else do something else

age = int(input("Enter your age:"))

# Using greater sign and lesser sign (<,>)
if age >= 100:
    print("Dang!, you are boomer ultra pro max")

elif age >= 18:
    print("You can confirm your order")

elif age <= 0:
    print("Bro, you are not even born yet!")

else:
    print("Sorry, your age must be above 18 years to confirm the order")

response = input("Would you like some burgers? (Yes/No):")

# Using double equal sign/ The comparison operator(==)
if response == "Yes":
    print("Have some burgers")

elif response == "No":
    print("Ok than, i'll eat all")

else:
    print("huh?...")

name = input("What is your name?:")

if name == "":
    print("Why arent you speaking?")

else:
    print(f"Nice to meet you {name}")

# Using Boolean
for_free = True

if for_free:
    print("Yes its for free sir")

else:
    print("No sir its not for free")

you_there = False

if you_there:
    print("Yes, I am here")

else:
    print("No, he is not here")




