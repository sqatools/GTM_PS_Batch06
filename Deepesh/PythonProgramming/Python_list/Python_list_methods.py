# Python Methods
print(dir(list))
"""
'append', 'clear', 'copy', 'count', 
'extend', 'index', 'insert', 'pop',
 'remove', 'reverse', 'sort'
"""

############ Add data to the list #############
# Append() method : This method add one value at the end of the list
list_a = [5,7, 8, 12, 6]
list_a.append(100)
list_a.append('Hello')
list_a.append([4, 6, 8])
list_a.append((1, 89, 2))

print("list_a :", list_a)

print("_"*50)
################
# insert() method : This method help to insert data to the list at specific index
#                    position.
list_b = [4, 7, 12, 56, 78]
list_b.insert(2, 500)
# 2 : index, 500: value

print("list_b:", list_b)  # [4, 7, 500, 12, 56, 78]
list_b.insert(3, 'Python')
print("list_b:", list_b) # [4, 7, 500, 'Python', 12, 56, 78]


print("_"*50)
##############
# extend() method : This method add one list data to another list at the end of target list.
list_c = ['a', 'b', 'c', 5, [2, 7], (1, 8)]
list_d = [10, 30, 40, 50]
list_d.extend(list_c)

print("listd :", list_d)  # [10, 30, 40, 50, 'a', 'b', 'c', 5, [2, 7], (1, 8)]


print("_"*50)
##############
# list concatenation : In list concatenation we can add two list with plus operator
#             and it does not modify the original list

list_e = [4, 7, 9]
list_f = [11, 44, 77, 99]
list_g = list_e + list_f
print("list_g :", list_g) # list_g : [4, 7, 9, 11, 44, 77, 99]

print("_"*50)
##############
# list multiplication : In this concept all the list values will be repeated n number of time
list_h = [4, 7, 1]
list_j = list_h*5
print("list_j :", list_j)

list_1 = [3, 6]
list_2 = [6, 8]
# print(list_1*'a') # can't multiply sequence by non-int of type 'str'
# print(list_1*list_2)  # can't multiply sequence by non-int of type 'list'


######################### Remove data from list ##################
print("_"*50)
##############
# remove method: This method the specific value from given list.
list_k = [4, 7, 9, 22, 5, 7]
list_k.remove(7)
output = list_k.remove(22)
print("list_k :", list_k, output) # [4, 9, 5, 7] None


print("_"*50)
##############
# pop() method : This method remove the value from index position and default index position is -1,
                # and it returns the removed
#                  value as well.
list_m = [4, 7, 12, 4, 45, 78]
val = list_m.pop()
print("removed value :", val) # 78
print("list_m :", list_m) # [4, 7, 12, 4, 45]

val2 = list_m.pop(3)
print("removed value :", val2)  # removed value : 4
print("list_m :", list_m) # [4, 7, 12, 45]

print("_"*50)
##############
# clear() method : This method remove all the data from list and only empty list will be remain.
list_o = [3, 6, 8, 12]
list_o.clear()
print("list_o :", list_o)  # list_o : []


print("_"*50)
################
# del : del function remove entire variable it self from memory
list_n = [5, 7, 2, 8]
del list_n
# print("list_n :", list_n) # there no list_n variable anymore
# name 'list_n' is not defined. Did you mean: 'list_a'?


# remove some partial values from list
list_p = [5, 8, 1, 6, 2, 18, 11, 55]
del list_p[2:6]
print("list_p :", list_p) # [5, 8, 11, 55]


print("_"*50)
################## Replace data in the list #################

list_q = [4, 6, 8, 22, 78]
# replace 8 with 100
list_q[2] = 100
print("list_q :", list_q) # [4, 6, 100, 22, 78]


# replace 4, 6 with 14, 16
list_q[:2] = [14, 16]
print("list_q :", list_q) # [14, 16, 100, 22, 78]


##### Filteration of list data ##########
print("_"*50)
##################
# sort() method : This method sort the list data in ascending and descending order and modify the original list
list_r = [5, 7, 1, 8, 2, 4]
list_r.sort()  # ascending order
print("lisr_r :", list_r)  # [1, 2, 4, 5, 7, 8]

list_s = [15, 7, 11, 8, 32, 4]
list_s.sort(reverse=True) # descending order
print("lisr_s :", list_s) # [32, 15, 11, 8, 7, 4]


print("_"*50)
# ##################
# sorted() function : This function does not modify the original, it takes input and return a sorted list as
#                      output.

list_t = [5, 7, 11, 55, 22, 34]
result1 = sorted(list_t)
print("ascending order :", result1) # [5, 7, 11, 22, 34, 55]

result2 = sorted(list_t, reverse=True)
print("descending order :", result2) # [55, 34, 22, 11, 7, 5]


print("_"*50)
########### Reverse the list data ########
list_z =[6, 8, 2, 9, 12, 56]

# i).  reverse() method : This method reverse the values of the list and modify the origina'
#                    list
list_z.reverse()
print("list_z :", list_z) # [56, 12, 9, 2, 8, 6]


print("_"*50)
######
# ii). reversed() function : This function take list as input and return the reverse values of
#                        given list

list_j = [5, 8, 11, 55, 11, 22, 33]
result = list(reversed(list_j))
print("result :", result) # [33, 22, 11, 55, 11, 8, 5]
print("list_j :", list_j) # [5, 8, 11, 55, 11, 22, 33]

# iii). list slicing:
print("list slicing :", list_j[::-1]) # [33, 22, 11, 55, 11, 8, 5]
print(list_j[-1:-len(list_j)-1:-1]) # [33, 22, 11, 55, 11, 8, 5]

print("_"*50)
##############
# count method() : This method count of number of occurrences of given value in list
list_k = [5, 8, 1, 5, 7, 1, 7, 8, 3, 7]
print("count of 7 :", list_k.count(7)) # 3
print("count of 8 :", list_k.count(8)) # 2


print("_"*50)
##############
# index method() : This method return the index position of any value in given list
list_A = [4, 7, 2, 8, 12]
print("Index of 8 :", list_A.index(8))
# Index of 8 : 3


#################### Copy concept in the list ###############
# shallow copy : In shallow copy concept we generally assign value from one list to another
#   and pass the reference of data, and if we do modification in one list that will relect
#   in another list as well.

list_a = [4, 8, 12, 78]
list_b = list_a
list_b.append(100)

print("list_a :", list_a)
print("list_b :", list_b)
list_c = list_b
list_a.append(50)
list_c.append(300)

print("list_a :", list_a, id(list_a)) # [4, 8, 12, 78, 100, 50, 300]
print("list_b :", list_b, id(list_b)) # [4, 8, 12, 78, 100, 50, 300]
print("list_c :", list_c, id(list_c)) # # [4, 8, 12, 78, 100, 50, 300]

print("_"*50)
####################Deep Copy ############
# deep copy : In deep copy concept we actually copy the content from one list to another
#             and if we do modification in one list, it does not affect list

list_p = [4, 7, 2, 8, 12]
list_q = list_p.copy()
list_q.append(100)
list_p.append(500)

print("list P:", list_p, id(list_p)) # [4, 7, 2, 8, 12, 500] # 2125581067136
print("list Q:", list_q, id(list_q)) # [4, 7, 2, 8, 12, 100] # 2125581215936


############################
print("_"*50)
############## List Comprehension ####################
list_r = [2, 5, 6, 1, 7]

# get square all the values
result = [x**2 for x in list_r]
print("result :", result)  # [4, 25, 36, 1, 49]


# get all the even value from list
list_s = [3, 7, 1, 2, 13, 14, 15]
result2 = [val for val in list_s if val%2 == 0]
print("list_s even :", result2) # [2, 14]


list_s = [3, 7, 1, 12, 13, 14]
# [(3, 'odd'), (7, 'odd'), (1, 'odd'), (12, 'even') , (13, 'odd'), (14, 'even')]
result3 = [(val, 'even') if val%2 == 0 else (val, 'odd') for val in list_s]
print("result3 :", result3)
# [(3, 'odd'), (7, 'odd'), (1, 'odd'), (12, 'even'), (13, 'odd'), (14, 'even')]


# nested loop in the list
result4 = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print("result 4:", result4)
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]


print("_"*50)
####################################################
list_y = [44, 66, 88, 23, 56, 78]
# get max values from list
print("max value :", max(list_y)) # max value : 88
print("min value :", min(list_y)) # min value : 23
print("sum of values :", sum(list_y)) # sum of values : 355
print("average of values :", sum(list_y)//len(list_y)) # sum of values : 355
