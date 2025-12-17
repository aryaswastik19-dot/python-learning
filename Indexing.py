# Indexing - accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# start field:
print(credit_number[10])

# end field:
print(credit_number[0 : 3])
print(credit_number[:5])
print(credit_number[5 : 8])
print(credit_number[5:])

# negative index:
print(credit_number[-1])
print(credit_number[-3])

# step field:
print(credit_number[::2])
print(credit_number[::3])