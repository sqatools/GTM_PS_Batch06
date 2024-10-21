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
# sorted() function : This function does not modify the original, it takes input and return a sorted list as
#                      output.

list_t = [5, 7, 11, 55, 22, 34]
result1 = sorted(list_t)
print("ascending order :", result1) # [5, 7, 11, 22, 34, 55]

result2 = sorted(list_t, reverse=True)
print("descending order :", result2) # [55, 34, 22, 11, 7, 5]
