# https://sqatools.in/python-list-programs/
# write a python program to remove all duplicate values from list
list1 = [3, 6, 3, 8, 2, 3, 8, 7, 8, 10, 7]
# output = [3, 6, 8, 2, 10, 7]
# [6, 2, 3, 8, 10, 7]

output = list1.copy()
for val in list1:
    val_count = output.count(val)
    #print(val,":", val_count)
    if val_count > 1:
        output.remove(val)

print(output)

print("_"*40)
########## solve program without count method ######
list2 = [3, 6, 3, 8, 2, 3, 8, 7, 8, 10, 7]
result = []

for val in list2:
    if val not in result:
        result.append(val)
    else:
        continue


print("result :",result)

# solution with list comprehension
result2 = []
[result2.append(val) for val in list2 if val not in result2]
print("result2 :", result2) # [3, 6, 8, 2, 7, 10]

print("_"*50)
##############################################
# q1. get square of all values from given list
list2 = [4, 7, 9, 12, 5]
for val in list2:
    print(val**2)

print("_"*50)
# q1. get square of all values from given list and print value if it greater than 25
list2 = [4, 7, 9, 12, 5, 2, 10, 3, 6]
for val in list2:
    sqr = val**2
    if sqr > 25:
        print(sqr)

print("_"*50)
# q1. get square of all values which are divisible by 3 and 4 and cube of value which is
# divisible by 5
list2 = [4, 7, 9, 12, 5, 2, 10, 3, 6]

for val in list2:
    #print(val)
    if val%3 == 0 and val%4 ==0:
        print(val**2)
    elif val%5 == 0:
        print(val**3)


print("_"*50)
# write a python program get max value from list without max function.
list3 = [4, 7, 8, 100, 9, 2,  12, 45]
max_val = 0
min_val = list3[0]
for val in list3:
    print(val)
    if val > max_val: # 4 > 0 | 7> 4 | 8> 7 | 100 > 8 | 9 > 100
        max_val = val # 4, 7, 8, 100
    else:
        continue

for val in list3:
    print(val)
    if val < min_val:
        min_val = val
    else:
        continue

print("max value :", max_val)
print("min value :", min_val)
# https://sqatools.in/python-list-programs/













