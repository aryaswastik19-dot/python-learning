# Exercise 2: Shopping Cart Program

x = input("What item would you like to buy?:")
y = float(input(f"The price of one {x} is:"))
z = int(input(f"How many {x} would you like to buy?:"))
t = (y*z)

print(f"You have bought {z} {x}")
print(f"Your total is: ${t}")
