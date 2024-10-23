# write a python program to remove all duplicate values from list
"""list1 = [3, 6, 8, 2, 3, 8, 7, 10, 7]    # [3, 6, 8, 2, 7, 10]
count = 0
output = []
for i in list1:
    if i not in output:
        output.append(i)
    else:
        continue
print(output)"""

# square of each value in list and print value which has greater than 15
list2 = [4, 6, 3, 8, 5, 12]
"""for val in list2:
    if val**2 > 15:
        print(val**2)"""

"""for val in list2:
    sqr = val**2
    # print(val, ":", sqr)
    if sqr > 25:
        print(sqr)"""

"""output = []
for val in list2:
    output.append(val**2)
print(output)
for i in output:
    if i > 25:
        print(i)"""

# square of values which are divisible by 3 and 4
# and cube of value which is divisible by 5
"""for i in list2:
    if i%3 == 0 and i%4 == 0:
        print(i**2)
    elif i%5 == 0:
        print(i**3)"""

# write a python program to get max value from list without using max function
list3 = [3, 5, 2, 4, 6]
"""max_val = 0
for val in list3:
    if val > max_val:
        max_val = val
    else:
        continue
print("max_val: ", max_val)"""



