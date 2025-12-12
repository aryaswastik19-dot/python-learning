# Conditional Expression - A one-line shortcut for the if-else statement (ternary operator)
#                          print or assign one of two values based on a condition
#                          x if (condition) else y

num1 = 5
num2 = -40
num3 = 6
num4 = 50
age = 25
temperature = 25
user = "Member"

max_num = num1 if num1 > num3 else num3
min_num = num2 if num2 < num4 else num2
status = "Adult" if age >= 18 else "Kid"
climate = "Cold" if temperature <= 10 else "Hot"
access_level = "Full access" if user == "Admin" else "Access Denied"

print("Positive" if num1 > 0 else "Negative")
print("Yes" if num2 > -30 else "No")
print("Even" if num3 % 2 == 0 else "Odd")

print(max_num)
print(min_num)
print(status)
print(climate)
print(access_level)





