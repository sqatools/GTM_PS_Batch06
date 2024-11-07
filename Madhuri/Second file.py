# Set data type Practice
set = {2,3,6,8,9}
print(set,type(set))
# apply loop on set data
print("apply loop on set data")
set1 = {4,7,9,12,34,56}
for val in set1:
    print(val)
    """
#Set Data type methods
# add method:- This method add one value at a time to the set
set_a = {3,6,8,2,5}
set_a.add(40)
set_a.add("hello")
set_a.add((4,7,8))
print("set_a",set_a)
# Update method:-
# this method update one set data to another set
set_b = {4,6,8,9}
set_c = {'a','b','c'}
set_c.update(set_b)
print("set_b:",set_b)
print("set_c:",set_c)
#3 union method:-
# This method combine the data from 2 sets and create a new values,without modifying the original list
set_p = {3,6,9,1}
set_q = {'X','y','z'}
result = set_p.union(set_q)
print("updated result:",result)
print("set_p:",set_p)
print("set_q:",set_q)
#4- Remove data method:-
#This method remove any specific value from  set and does not return anything
# if the provide element is not avaialble in the set then it will throw error
set_x= {4,7,9,2,12,14,17}
set_x.remove(14)
print("set_x:",set_x)
# 5-pop method:----------------
#This method remove random data from set and return it
set_z={44,60,88,22,11,45}
val = set_z.pop()
print("removed value:",val)
print("set_z:",set_z)
#6 discard method:--------------
# this method remove specific data fromset and does throw any error
set_k={44,66,223,34,45,65,77}
set_k.discard(223)
print("set_k:",set_k)
print("set_k:",set_k)
# remove value which is not avialable.it does not throw any error.
set_k.discord(200)
print("set_k:",set_k)
#7- Intersection method:-------------
# This method return the common values from 2 different sets
set_1 ={4,6,8,2,18,12}
set_2 = {14,15,17,18,12,8}
result = set_1.intersection(set_2)
print("result:",result)
print("set_1:",set_1)
print("set_2:",set_2)
print("result:", set_1.intersection(set_2))
#8-Different method--------
#This method provides the different of values between two sets
set_5 = {4,6,8,2,18,12}
set_6 = {14,15,17,18,12,8}
different_result = set_5.difference(set_6)
print("set_5:",set_5)
print("set_6:",set_6)
"""
"""
#9-Differene_method--------------
#This method update difference value in  target set
Set_5 ={4,6,9,7,81}
print("set_5:",Set_5)
#10 Symmetric-different method:-----------
# This method return the combine difference values from both two sets
set_7 = {4,6,8,12,18,2}
set_8 = {14,15,18,12,8}
all_diff_values=set_7.symmetric_differentsets
# 11-Symmetric_difference_update
#this method updte the target with combine difference value between both the sets
set_7.symmetric_differnce_update(set_7)
print("set_7:" ,set_7)
"""
"""
# clear method:----------
# this method clear all the data from set
set_9 = {4,6,8,2,18,12}
set_9.clear()
print("set_9:",set_9)
# del entire value from memory
del set_9
print("set_9:",set_9)
# subset and superset method
set_a = {4,6,8,12,34}
set_b = {4,8,3,4}
set_c ={2,6,15}
print("set_a is subset:",set_a.issubset(set_b))
"""
"""
#problem create a set in python
a = {1,2,3,5,6}
print("set:",a)
#  problem to add elements to setin python
a = {1,2,3,5,6}
print("orginal set:",a)
a.add(7)
print("new set:",a)
# problem to remove an element from set
a = {1,2,3,4,5,6}
print("orginal set:",a)
a.remove(5)
print("new set:",a)
#4 problem to find the length of set
a = {1,2,3,4,5,6}
print("orginal set:",a)
print("legnth of given set:",len(a))
# 5 problem to check if any element is in a set
a = {1,2,3,4,5,6}
print("orginal set:",a)
if 5 in a:
    print("true")
else:
    ("false")
    """
#6 problem to find the union of two sets:
a = {1,2,3,4,5,6}
b = {7,8,9,0}
print("orginal set:",a)
print("orginalset:",b)
print("union of a and b:",a.union(b))
# 7 problem to find the intersection of two sets
a = {1,2,4,5}
b = {7,8,9,1}
print("orginal set:",a)
print("orginal set:",b)
print("intersection of a and b:",a.intersection(b))
# 8problems to find the differnce of two sets
a = {1,2,3,4}
b = {7,8,9,1}
print("orginal seta:", a)
print("orginal setb:", b)
print("differnce of a and b:",a-b)
#Problem to find symmetric difference of two sets
a ={1,2,3,4,5}
b = {7,8,9,1}
print("symmetric difference of a and b:",a.symmetric_difference(b))
#10- problem to show one set is a subset of another
a = {1,2,3,4,5}
b = {2,4}
print("original set1:",a)
print("original set2:",b)
print("b is subset of a:",b.issubset(a))




