"""Python tuple program to create a tuple with 2 lists of data.

Input lists:
list1 = [4, 6, 8]
list2 = [7, 1, 4]
Output= ((4, 7), (6, 1), (8, 4))
"""
list1 = [4, 6, 8, 1]
list2 = [7, 1, 4]
result = []
for i in range(len(list1)):
    if i < len(list2):
        result.append((list1[i], list2[i]))

    elif i >= len(list2):
        result.append((list1[i], 0))
        print("result data in list:", tuple(result))
        int_value = tuple(result)
        print("int values :", int_value)


tup1 = (50,)
print(tup1) #
print(tup1, ":", type(tup1))

print("_"*50)
###  Get max value and mini with inbuilt method
tupp = (5, 7, 9, 2, 5, 20, 32)
print("max value :", max(tupp))
print("min value :", min(tupp))
print("sum value :", sum(tupp))


print("_"*50)
tup_lp_A = (30, 20, 40, 13, 50, 11)
tuple_comprehension = tuple((val for val in  tup_lp_A if val%2 == 0))
print(tuple_comprehension) # (30, 20, 40, 50)


# Q1.  write a python program to combine a list of data with their index and create new list
l1 = (5, 7, 9, 12)
l2 = (10, 40, 50, 60)
l3 = [15, 47, 59, 72]

result = []
for i in range(len(l1)):
    result.append(l1[i]+l2[i])

print("result :", result)


#q2 :  write a python program to get below result
list1 = [3, 7, 9, -1, - 2, -5, 6, -8]
#output = [3, 7, 8, 6, -1, -2, -5, -8]
result = []
for val in list1:
    if val > 0:
        result.insert(0, val)
    else:
        result.append(val)

print("result :", result)


# Q3: write a python program to get below result:
# if the value is divisible by 2 then square it else add 'odd' string.
list1 = [3, 6, 8, 9, 1, 4, 7, 2]
#output = ['odd', 36, 64, 'odd', 'odd', 16, 'odd', 4]

output = []
for val in list1:
    if val%2 == 0:
        output.append(val**2)
    else:
        output.append('odd')

print("output :", output)
