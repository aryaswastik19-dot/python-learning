# Currency converter (dollar-rupees)

amount = float(input("Enter the amount:"))
currency = input("Enter its currency ($/₹):")

if currency == "$":
    amount = amount * 90
    print(f"{round(amount, 2)}₹")

elif currency == "₹":
    amount = amount / 90
    print(f"{round(amount, 2)}$")

else:
    print(f"{currency} is invalid currency")