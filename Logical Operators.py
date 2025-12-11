# Logical Operators - evaluate multiple conditions (or, and, not)
#                     or - at least one condition must be true
#                     and - both conditions must be true
#                     not - inverts the condition (not false, not true)

# 'or' operator
temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")

else:
    print("The outdoor event is still scheduled")

# 'and' operator
temperature = -12
is_sunny = False

if temperature >= 35 and is_sunny:
    print("Its very hot outside")

elif temperature <= 0 and is_sunny:
    print("its a moderate temperature")

elif 28 > temperature > 0 and is_sunny:
    print("Its warm outside")

else:
    print("its cold outside")

# 'not' operator
tem = 4
is_cold = False

if tem >= 10 and not is_cold:
    print("Its not cold outside")

elif tem < 5 and not is_cold:
    print("Its a not sunny at all")

else:
    print("Its winter")


