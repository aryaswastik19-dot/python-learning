# Temperature converter

temperature = float(input("Enter the temperature:"))
unit = input("Celsius or Fahrenheit(C/F)")

if unit == "C":
    temperature = (temperature * 9/5) + 32
    print(f"{round(temperature, 2)}°F")

elif unit == "F":
    temperature = (temperature - 32) * 5/9
    print(f"{round(temperature, 2)}°C")

else:
    print(f"{unit} is invalid")

