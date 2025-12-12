# Useful strings methods and functions:

name = input("Whats your name?:")
age = input("Whats your age?:")
father = input("Whats your father's name?:")
mother = input("Whats your mothers name?:")
hobby = input("Whats your hobby?:")
food = input("Whats your favourite food?:")
pin = input("Whats the pin your city?:")
email = input("Whats your email?:")
phone_no = input("Whats your phone number?:")
pet = input("Whats your pet's name?:")

# len() function - (shows the length of the string)
result = len(name)
print(result)

# .find() method - (shows the number of first occurrence of a letter,
#                     counts in whole numbers)
x = age.find("5")
print(x)

# .rfind() method - (shows the number of last occurrence of a letter,
#                      counts in whole numbers)
y = father.rfind("e")
print(y)

# .capitalize() method - (Makes the first letter capital)
z = mother.capitalize()
print(z)

# .upper() method - (Makes all the letters upper case{capital})
a = hobby.upper()
print(a)

# .lower() method - (Makes all the letter lower case{decapitalize})
b = food.lower()
print(b)

# .isdigit() method - (if only numericals, return True, else False)
c = pin.isdigit()
print(c)

# .isalpha() method - (if only alphabets, returns True, else False)
d = email.isalpha()
print(d)

# .count() method
e = phone_no.count("6")
print(e)

# .replace() method - (Replaces any occurrence with each other you want)
f = pet.replace("s", "e")
print(f)