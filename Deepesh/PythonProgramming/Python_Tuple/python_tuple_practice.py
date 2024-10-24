tup1 = (3, 6, 7, 'a', 'b', 'Hello' 'c', [2, 5, 7], (2, 1, 4))

print(tup1, type(tup1))
# (3, 6, 7, 'a', 'b', 'c', [2, 5, 7], (2, 1, 4)) <class 'tuple'>

print(tup1[6]) #  [2, 5, 7]
print(tup1[6][1]) # 5
print(tup1[-2][1]) # 5
print(tup1[-2][-2]) # 5
print(tup1[3:6])  # ('a', 'b', 'c')
print(tup1[-3:-6:1])  # ('c', 'b', 'a')


print(tup1[-5:-2:1])  # ('a', 'b', 'c')
print(tup1[5:2:-1])   # ('c', 'b', 'a')
print(tup1[7][-1:-4:-1]) # (4, 1, 2)
print(tup1[-1][-1:-4:-1]) # (4, 1, 2)
print(tup1[-1][::-1]) # (4, 1, 2)
tup2 = (3, 6, 7, 'a', 'b', 'c', 'Hello', [2, 5, 7], (2, 1, 4))
print(tup2[-3][::-1]) # olleH


print("_"*40)
###### Apply loop on tuple ######
tup_a = (3, 6, 8, 1, 4)
for val in tup_a:
    print(val)

"""
3
6
8
1
4
"""

str1 = 'Python'
# default initial index would be -1 as different is negative and last index would
# -len(str1)-1
print(str1[::-1]) # nohtyP
print(str1[-1:-len(str1)-1:-1]) # nohtyP


# default initial index is zero and end index would len(str)
print(str1[::1]) # Python
print(str1[0:len(str1):1])  # Python


print("_"*40)
###### Apply loop with index ######
tup_a = (3, 6, 8, 1, 4)
for i in range(len(tup_a)):
    print(i, tup_a[i])

print("_"*40)
############# Tuple Methods #################
print(dir(tuple))

tup_b = (3, 7, 1, 4, 6, 7, 7, 2)
# count method: This method return the number occurence of any value in given tuple
print("count of 7 :", tup_b.count(7))
# count of 7 : 3

# index method : This method return the index position of any value in the tuple
print("Index of 6 :", tup_b.index(6))
# Index of 6 : 4






print("_"*50)
# write a python program to print square of all the values in tuple
tup_c = (3, 7, 12, 8)
for val in tup_c:
    print(val, ":", val**2)

print("_"*50)
# write a python find out all the value which even in the tuple
tup_d = (3, 7, 12, 8, 10)
for val in tup_d:
    if val%2 == 0:
        print(val)
    else:
        continue


print("_"*50)
# write a python program to get maximum value tuple
tup_e = (4, 7, 12, 55, 77, 23, 56)

max_val = 0
for val in tup_e:
    if val > max_val:
        max_val = val
    else:
        continue

print("max val:", max_val)

print("_"*50)
# write a python program to remove all duplicate from given tuple
tup_g = (4, 7, 12, 8, 34, 12, 8, 4)
result = []
for val in tup_g:
    if val not in result:
        result.append(val)
    else:
        continue

print("result :", tuple(result)) # (4, 7, 12, 8, 34)

#############################

tup1 = (2, 5, 7, [4, 7, 8], 20, 6)
tup1[3].append(10)
print(tup1)







