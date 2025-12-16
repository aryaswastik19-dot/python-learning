# Exercise 6: Validate the user input with ths following condition
# 1. username must be less than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

x = input("Enter your name:")

if len(x) > 12:
    print("Invalid input; username must be less than 12 characters")

elif not x.find(" ") == -1:
    print("Invalid input; username must not contain any spaces")
    
elif not x.isalpha():
    print("Invalid input; username must not contain digits")

else:
    print("Valid Input; Welcome")