set1 = {3, 6, 8, 2, 9, 3, 2}
"""
# properties:
->  It is mutable data type
->  Duplicate values are not allowed
->  It represent with curly braces.
->  It does not follow indexing
->  Set store data in un-structure order.
->  Only immutable data type can be member in set (int, float, string, tuple, boolean)
"""

print(set1, type(set1))  # {2, 3, 6, 8, 9} <class 'set'>
set2 = {'Hello', (3, 5, 7), True, 4.5, 12}
print(set2) # {(3, 5, 7), True, 4.5, 12, 'Hello'}


# set3 = {'Hello', (3, 5, 7), True, 4.5, 12, [4, 7, 9]}
# unhashable type: 'list'


#set3 = {'Hello', (3, 5, 7), True, 4.5, 12, {4, 7, 9}}
# unhashable type: 'set'

# set3 = {'Hello', (3, 5, 7), True, 4.5, 12, {'a': 123}}
# TypeError: unhashable type: 'dict'

print("_"*50)
print("Apply loop on set data")
# apply loop on set data type

set4 = {4, 7, 9, 12, 34, 56}
for val in set4:
    print(val)
"""
34
4
7
56
9
12
"""

########## Set Methods ###########
print(dir(set))
"""
 'add', 'clear', 'copy', 'difference', 
 'difference_update', 'discard', 'intersection',
  'intersection_update', 'isdisjoint', 'issubset', 
  'issuperset', 'pop', 'remove', 'symmetric_difference',
   'symmetric_difference_update', 'union', 'update']

"""

############### Add data to the set #############
print("_"*50)
# add method(): This method add one value at time to the set
set_a = {3, 6, 8, 2, 5}
set_a.add(40)
set_a.add('Hello')
set_a.add((4, 7, 8))

print("set_A :", set_a)
# {2, 3, 'Hello', 5, 6, (4, 7, 8), 8, 40}


#######################
print("_"*50)
# update method() : This method update one set data to another set
set_b = {4, 6, 8, 9}
set_c = {'a', 'b', 'c'}

set_c.update(set_b)
print("set_b :", set_b) # {8, 9, 4, 6}
print("set_c :", set_c) # {'c', 4, 6, 'a', 8, 'b', 9}


#######################
print("_"*50)
# union method() : This method combine the data from 2 sets and create a new values, without
# modifying the original set

set_p = {3, 6, 9, 1}
set_q = {'x', 'y', 'z'}
result = set_p.union(set_q)
print("updated result :", result) # {1, 3, 6, 'y', 9, 'z', 'x'}
print("set_p :", set_p)
print("set_q :", set_q)


##################### Remove data from set #######################
print("_"*50)
# remove method(): This method remove any specific value from set and does not return anything.

set_x = {4, 7, 9, 2, 14, 17}
set_x.remove(14)
print("set_x :", set_x) # {17, 2, 4, 7, 9}

# if the provide element is not available in the set, then it will throw error.
# set_x.remove(20)  # KeyError: 20


##################
print("_"*50)
# pop method(): This method remove random data from set and return it.
set_z = {44, 66, 88, 22, 11, 45}
val = set_z.pop()
print("removed value :", val) # 66
print("set_z :", set_z) # {22, 88, 11, 44, 45}



##################
print("_"*50)
# discard method() : This method remove specific data from set, and does throw any error
#                     if the target value is not available

set_k = {44, 66, 223, 34, 45, 65, 77}
set_k.discard(223)
print("set_k :", set_k) # {65, 66, 34, 77, 44, 45}

# remove value which is not available: It does not throw any error.
set_k.discard(200)
print("set_k :", set_k) # it does return any value or error.


##########################################
print("_"*50)
# intersection method() : This method return the common values from 2 different sets

set_1 = {4, 6, 8, 2, 18, 12}
set_2 = {14, 15, 17, 18, 12, 8}

common_values = set_1.intersection(set_2)
print("Common result :", common_values) # {8, 18, 12}
print("Common result :", set_1.intersection(set_2)) # {8, 18, 12}
print("set_1 :", set_1)
print("set_2 :", set_2)

###############
print("_"*50)
# intersection_update method(): This method update the target set or original set with common
#                              values

set_3 = {4, 6, 8, 2, 18, 12}
set_4 = {14, 15, 17, 18, 12, 8}

set_3.intersection_update(set_4)
print("set_3 updated with common values :", set_3) # {8, 18, 12}
print("set_4 :", set_4) # {17, 18, 8, 12, 14, 15}



###############
print("_"*50)
# different method() : This method provides the difference of values between two sets.

set_5 = {4, 6, 8, 2, 18, 12}
set_6 = {14, 15, 17, 18, 12, 8}

diff_result1 = set_5.difference(set_6)
diff_result2 = set_6.difference(set_5)
print("diff result1 :", diff_result1) # {2, 4, 6}
print("diff result2 :", diff_result2) # {17, 14, 15}
print("set_5:", set_5)
print("set_6:", set_6)

# difference_update(): This method update difference value in target set
set_5.difference_update(set_6)
print("set_5:", set_5) # {2, 4, 6}

###############
print("_"*50)
# symmetric_different method(): This method return the combine difference values from both sets.
set_7 = {4, 6, 8, 2, 18, 12}
set_8 = {14, 15, 17, 18, 12, 8}
all_diff_values = set_7.symmetric_difference(set_8)
print("diff values in both sets :", all_diff_values) # {2, 4, 6, 14, 15, 17}

# symmetric_difference_update : This method update the target with combine difference value
# between both the sets.
set_7.symmetric_difference_update(set_8)
print("set_7 updated :", set_7) #  {2, 4, 6, 14, 15, 17}
print("set_8 :", set_8) # {17, 18, 8, 12, 14, 15}


# clear all the data from set:
# clear method : This method clear all the data from set
set_9 = {4, 6, 8, 2, 18, 12}
set_9.clear()

print("set_9 :", set_9)

# del entire value from memory
del set_9
# print("set_9 :", set_9)
# NameError: name 'set_9' is not defined

print("_"*50)
####################################
# subset and superset method:
set_a = {4, 6, 8, 9, 12, 34}
set_b = {4, 8, 34}
set_c = {12, 6, 15}

print("set_a is superset :", set_a.issuperset(set_b)) # True
print("set_b is subset :", set_b.issubset(set_a)) # True
print("set_a is superset of set_c :", set_a.issuperset(set_c)) # False
print("set_c is subset of set_a :", set_c.issubset(set_a)) # False

print("_"*50)
###########################################
# isdisjoint method :
set_a = {4, 6, 8, 9, 12, 34}
set_b = {4, 8, 34}
set_c = {5, 7, 10}

print("set a and set b is isdisjoint :", set_a.isdisjoint(set_b)) # False
print("set a and set c is isdisjoint :", set_a.isdisjoint(set_c)) # True
