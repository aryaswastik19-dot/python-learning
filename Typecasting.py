# Typecasting - The process of converting a variable from one data type to another
#               str(), int(), float(), bool()

name = "Swastik"
age = 15
GPA = 4.5
Pass = 12345678
is_student = True

# type function:
print(type(name))
print(type(age))
print(type(GPA))
print(type(is_student))

GPA = int(GPA)
age = str(age)
age += "1"

Pass = float(Pass)
name = bool(name)
is_student = str(is_student)

print(name)
print(GPA)
print(age)
print(Pass)
print(is_student)





