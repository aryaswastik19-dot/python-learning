# Python weight converter

weight = float(input("Enter your weight:"))
unit = input("Kilograms or Grams (Kg/G):")

if unit == "Kg":
    weight = weight * 1000
    print(f"{weight}G")

elif unit == "G":
    weight = weight / 1000
    print(f"{weight}Kg")

else:
    print(f"{unit} was invalid")

