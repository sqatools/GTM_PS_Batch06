list1 = [4, 6, 8, 1]
print(list1, type(list1))
# [4, 6, 8, 1] <class 'list'>

list2 = ['Hello', [1, 2, 3], (6, 7, 8), {'a': 123, 'b' : 345}, True, {4, 6, 1}]

list3 = ['Hello', [1, 2, 3], (6, 7, 8), {'a': 123, 'b' : {'a' : 2345, 'p' : 678}}, True, {4, 6, 1}]

print(list2[2]) # (6, 7, 8)
print(list2[-1]) # {1, 4, 6}
print(list2[1][1]) # 2
print(list2[0][2]) # l
print(list2[-3]['b']) # 345
print(list2[2][2]) # 8
print(list2[1:3]) # [[1, 2, 3], (6, 7, 8)]
print(list2[1:4:2]) # [[1, 2, 3], {'a': 123, 'b': 345}]

print(list3[-3]['b']['a'])  # 2345
print(list2[1][1:]) # [2, 3]

print("_"*50)
################ apply loop on list data ################

list_a = ['a', 'b', 'c', 4, 7, 9]

for val in list_a:
    print(val,end= " ")

# a b c 4 7 9

print()
print("_"*50)
# apply loop with indexing
len_list = len(list_a)
for i in range(len_list):
    print(i,":", list_a[i])
"""
0 : a
1 : b
2 : c
3 : 4
4 : 7
5 : 9
"""
print("_"*50)
# write a python get square of all the values
list_b = [5, 8, 2, 9, 1]
for v1 in list_b:
    print(v1, ":", v1**2)


print("_"*50)

for i in range(len(list_b)):
    print(i, ":",list_b[i], ":",  list_b[i]**2)


print("_"*50)
for i in range(5):
    print(i)


print("_"*50)
######################################
# write a python program to get integer values from list
list_c = [5, 'Hello', 50, 'python', 4.5, 11, [3, 6 ,7]]

for val in list_c:
    #print(val)
    if isinstance(val, int):
        print(val, val**2)
    elif isinstance(val, str):
        print(val, val*2)


print("_"*50)
############## slicing in the list ########
list_d = [4, 7, 2, 8, 12, 90]

print(list_d[::-1])  # [90, 12, 8, 2, 7, 4]
print(list_d[-2:-5:-1])  # [12, 8, 2]
print(list_d[0:5:2]) # [4, 2, 12]
print(list_d[::2]) # [4, 2, 12]
print(list_d[-1:-6:-2]) # [90, 8, 7]
print(list_d[-3:-7:-1]) # [8, 2, 7, 4]
print(list_d[1:5:1])  # [7, 2, 8, 12]
print(list_d[2:6:1])  # [2, 8, 12, 90]
print(list_d[-1:-5:-1]) # [90, 12, 8, 2]
