"""
Python data type:

1. Number:
    i). Integer
    ii). Float
    iii). Complex Number

2. Sequential:
    i). String
    ii). List
    iii). Tuple

3. Dictionary
4. Set
5. Boolean

"""
##################################################
####### Integer ################
"""
->  Integer data type represent with keyword as int (<class 'int'>)
->  Integer data type does not have any limit to defined the value
->  Integer is immutable data type
->  Integer data type only contains whole number
"""
num1 = 40
print(type(num1))
# int()

num2 = 65436346434358439085098495038490534890584390859034
print("num2 data type :", type(num2), num2)  # <class 'int'>

num2 = 100  # replaced previous value
print(num2)

num3 = 0
num4 = -309
print("data type of num3 :", type(num3))  # <class 'int'>
print("data type of num4 :", type(num4))  # <class 'int'>

print("_" * 50)
######################################
##### Float data type #######

"""
properties
->  float data type represent with keyword as float (<class 'float'>)
->  float data type does not have any limit to defined the value
->  float is immutable data type
->  float data type only contains pointer value
"""

var_a = 50.55
print("data type of var_a :", type(var_a), var_a)

var_b = 564356435636.4968925812
print("data type of var_b :", type(var_b), var_b) # <class 'float'> 564356435636.497

var_c = 45.49548934525434
print("data type of var_c :", type(var_c), var_c) # <class 'float'> 45.49548934525434

var_d = 0.0
print("data type of var_d :", type(var_d), var_d) # <class 'float'> 0.0

print("_" * 50)
#####################################
#### complex number #####
"""
-> complex number is combination of real and image values
-> complex number is represent in the format of x+yj, x-yj, -x+yj
-> complex number is immutable data type.
"""
var_e = 50 + 40j

print("imaginary value :", var_e.imag) # 40.0
print("real value :", var_e.real) # 50.0

var_f = 5 + 10j
var_g = 8 + 15j
var_h = var_f + var_g
print("Addition of complex number :", var_h, type(var_h)) # <class 'complex'>, (13+25j)

var_k = -10*5j
print(var_k, type(var_k), var_k.imag, var_k.real)

result = complex(70, -80)
print(result)  # (70+80j)

var_l = 10-5j
print(var_l, var_l.imag, var_l.real) # (10-5j) -5.0 10.0


print("_" * 50)
###################################################
###### String Data Type #######
"""
->  string is immutable data type
->  string follows positive and negative indexing
->  string can defined with single quotes, double quotes and triple quotes.
->  string only contains any value under quotes
"""

str_a = "Hello '%*()'(*"
str_b = 'Python "5435"34543'
str_c = """
python
programming
learning  *&)(*)(*()*)(*
automation
"""

print(str_a, type(str_a))
print(str_b, type(str_b))
print(str_c, type(str_c))

#  0 1 2 3 4
#  H e l l o
# -5-4-3-2-1

str_d = "Hello"
print(str_d[0])  # H
print(str_d[-1]) # o

print("_"*50)
#######################################
####### list data type ##########

"""
-> List is mutable data type, we can the values in the list
-> List follow positive and negative indexing as like string.
-> List can contains all type of data, int, float, string, list, tuple, dict, set, boolean
-> List represent with square brackets.
-> All values are in list will be comma separated
"""

list1 = [4, 4.5, 'Hello', [1, 4, 6]]
print("list1 :", list1, type(list1))

#   0   1    2       3
#  [4, 4.5, 'Hello', [1, 4, 6]]
#   -4  -3   -2      -1

print(list1[3])  # [1, 4, 6]
print(list1[-2]) # Hello

list2 = [ 2, 4.5, 'python',
         [1, 2, 4], (7, 9, 2),
         {'a': 123, 'b' : 456},
         {4, 7, 9, 12},
         True, False, None ]

print(list2, type(list2))
print("NUmber of values in the list :", len(list2)) # 10
str1 = "Python"
print("string length :", len(str1)) # 6
list3 = [5, 7, 9]
list3.append(10)
print("list 3:", list3)  # [5, 7, 9, 10]
print(dir(list))

# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'


print("_"*50)
#################################
##### tuple data type ##########

"""
-> Tuple is immutable data type, once it is defined we can not modify
-> Tuple follow positive and negative as like list and string.
-> Tuple can contains any of data, int, float, string, list, tuple, dict, set, boolean
-> Tuple represent with round bracket.
-> Tuple is faster than list data type
-> We can store fixed data tuple, that we dont want to change in future.
  e.g. months in year, days in week etc 
"""

tup1 = (4, 5.6, 'Programming', [3, 6, 7],
        (1, 5, 7), {'a': 345,'b' : 456})

print(tup1, type(tup1))
print("total values in the tuple :", len(tup1))
print("first value in the tuple :", tup1[0]) # 4
print(tup1[2]) # Programming
print(tup1[-1]) # {'a': 345, 'b': 456}
print(tup1[-5]) # 5.6

print(dir(tuple))
# 'count', 'index'


print("_"*50)
############################################
########## Dictionary data ################
# dict1 = {key : value}
dict1 = {'a' : 123, 'b' : 456}
print(dict1['a'])

"""
# properties of dictionary
-> dictionary is mutable data type, we can update the data at any point of time.
-> dictionary does not follow positive or negative indexing
-> dictionary store values in key value format
-> dictionary represent with {} braces.
-> dictionary only contains unique keys, duplicate keys are not allowed.
-> dictionary can contains duplicate values.
-> Only immutable data type can be key in the dictionary , int, float, string, tuple, boolean
-> All type of data can store as value in the dictionary
"""

dict1 = {'name': 'Rahul', 'name' : 'Mohit'}
dict1[234] = [4, 7, 8]
dict1['Python'] = 'Good Morning'
dict1[(5, 7, 9)] = {4, 8, 1, 5, 4}
# dict1[[4, 7, 9]] = 'Python'  # TypeError: unhashable type: 'list'

dict1[4.5] = True
dict1[False] = (4, 7, 1, 8)
dict1[4.5] = 'Hello'
print(dict1)
