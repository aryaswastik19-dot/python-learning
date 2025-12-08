# Exercise 5: Hypotenuse of Right angled triangle
import math

a = float(input("Side A of the triangle:"))
b = float(input("Side B of the triangle:"))
hypotenuse = math.sqrt(pow(a, 2)+pow(b, 2))

print(f"The hypotenuse of the triangle is: {round(hypotenuse, 2)}cm")