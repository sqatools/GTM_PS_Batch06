# write a python program to remove all duplicate values from list
"""list1 = [3, 6, 8, 2, 3, 8, 7, 10, 7]    # [3, 6, 8, 2, 7, 10]
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

# 1. Python program to calculate the square of each number from the given list
l1 = [2, 4, 6, 8, 3, 5, 7, 9]
for val in l1:
    print("Square of ", val, ":", val**2)

print('_'*50)
# 2. Python program to combine two lists
l2 = [2, 4, 6]
l3 = [1, 3, 5]
# Method1
"""combine_list = l2 + l3
print(combine_list)"""
# Method2
"""l2.extend(l3)
print(l2)"""

print('_'*50)
# 3.  Python program to calculate the sum of all elements from a list
l4 = [2, 4, 5, 1, 7]
summation = 0
for val in l4:
    summation = summation + val
print("Sum of all elements in list: ", summation)

print('_'*50)
# 4. Python program to find a product of all elements from a given list
l5 = [2, 4, 5, 1, 7]
product = 1
for val in l5:
    product = product * val
print("Product of all elements in list: ", product)

print('_'*50)
# 5. Python program to find the minimum and maximum elements from the list
l6 = [23, 4, 5, 54, 10, 60]
print('_____Method1____')
max_val = 0
min_val = l6[0]
for val in l6:
    if val > max_val:
        max_val = val
    elif val < min_val:
        min_val = val
    else:
        continue
print("Maximum value: ", max_val)
print("Minimum value: ", min_val)
print('_____Method2_____')
l6.sort()
print("Minimum value: ", l6[0])
print("Maximum value: ", l6[-1])
print('_____Method3_____')
print("Maximum value: ", max(l6))
print("Minimum value: ", min(l6))

print('_'*50)
# 6. Python program to differentiate even and odd elements from the given list
l7 = [5, 8, 43, 56, 3, 20, 45]
even = []
odd = []
for val in l7:
    if val%2 == 0:
        even.append(val)
    elif val%2 != 0:
        odd.append(val)
print("Even list: ", even)
print("Odd list: ", odd)

print('_'*50)
# 7. Python program to remove all duplicate elements from the list
l8 = [3, 6, 8, 2, 3, 8, 7, 10, 7]
output = []
for val in l8:
    if val not in output:
        output.append(val)
print("List after removing duplicates: ", output)

print('_'*50)
# 8. Python program to print a combination of 2 elements from the list whose sum is 10

