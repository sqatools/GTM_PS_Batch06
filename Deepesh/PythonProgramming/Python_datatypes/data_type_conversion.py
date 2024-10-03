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
######################### Integer #############

## int -> float ###

num1 = 404
f1 = float(num1)
print(f1, type(f1))  # 404.0 <class 'float'>

print("_" * 50)
### int -> string ###
num1 = 657
str1 = str(num1)
print(str1, type(str1), str1[0])
# 657 <class 'str'> 6

str2 = '"Hello"'
print(str2)

print("_" * 50)
### int -> list ###  coversion is not possible
"""
num2 = 7655765
l1 = list(num2)
print(l1)
#  'int' object is not iterable
"""
print("_" * 50)
### int -> tuple ### coversion is not possible
### int -> dict ### coversion is not possible
### int -> set ### coversion is not possible

### int -> boolean ###

num_a = 0
b1 = bool(num_a)
print(b1, type(b1))  # False <class 'bool'>

num_b = 123
b2 = bool(num_b)
print(b2, type(b2))  # True <class 'bool'>

print("_" * 50)
############## Float ##########

### float -> int #####
f2 = 55.56
n1 = int(f2)
print(n1, type(n1))  # 55 <class 'int'>

print("_" * 50)
### float -> string #####
f3 = 66.83
s2 = str(f3)
print(s2, type(s2))  # 66.83 <class 'str'>
print(s2[3])  # 8
print(s2[2])  # .

### float -> list ####  conversion is not possible
### float -> tuple ####  conversion is not possible
### float -> dict  ##### conversion is not possible
### float -> set  ##### conversion is not possible

print("_" * 50)
#########################
f1 = 0.0
b1 = bool(f1)
print(b1, type(b1))  # False <class 'bool'>

f2 = 0.25
b2 = bool(f2)
print(b2, type(b2))  # True <class 'bool'>

############################# string ##################################

print("_" * 50)
### string -> int #####

# i). If string contains characters: then string to int conversion is not possible
"""
str_a = "Hello345"
int1 = int(str_a)
print(int1, type(int1))
# invalid literal for int() with base 10: 'Hello345'
"""

# ii) if string contains only number: then conversion is possible

str_b = "56434277"
int_b = int(str_b)

print(int_b, type(int_b), int_b * 2)
# 56434277 <class 'int'> 112868554


##### string -> float #######
print("_" * 50)
str_c = "55.78"
f3 = float(str_c)
print(f3, type(f3))
# 55.78 <class 'float'>

# if string contain character along with float value then conversion is not possible


print("_" * 50)
#### string -> list ######

str_d = "Python"
list_d = list(str_d)
print(list_d, type(list_d))
# ['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>
list_d.append('M')
print(list_d)

print("_" * 50)
#### string -> tuple ######
str_e = "Programming"
tup_e = tuple(str_e)
print(tup_e, type(tup_e))
# ('P', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple'>


print("_" * 50)
#### string -> dictionary ######
"""
str_f = "Python Programming"
dict_f = dict(str_f)
print(dict_f)
# dictionary update sequence element #0 has length 1; 2 is required
"""

# json is inbuilt module in the python to deal with json data.
import json

# its raw string with dictionary format
details = '{"Name" : "John", "Mobile" : 455436534, "email" : "john@gmail.com"}'
print(details, type(details))
# {"Name" : "John", "Mobile" : 455436534, "email" : "john@gmail.com"} <class 'str'>

# convert string data into dict with the help of json module
data = json.loads(details)
print(data, type(data))
# {'Name': 'John', 'Mobile': 455436534, 'email': 'john@gmail.com'} <class 'dict'>
# get any specific value from dict
print(data['Name'])

print("_" * 50)
######## string -> set ###########

str_h = "Pyth& @ on Programming %"
set_h = set(str_h)
print(set_h, type(set_h))
# {'o', 't', ' ', 'n', 'y', 'm', 'r', '&', 'h', 'i', '%', 'a', 'P', 'g', '@'} <class 'set'>

print("_" * 50)
######## string -> boolean ###########

str_j = ""
bool_j = bool(str_j)
print(bool_j, type(bool_j))
# False <class 'bool'>


str_i = "Hello"
bool_i = bool(str_i)
print(bool_i, type(bool_i))
# True <class 'bool'>


###############################  List ############################

print("_"*50)
### list -> int #### conversion is not possible
### list -> float #### conversion is not possible
### list -> string ####

list1 = [4, 5, 6]
str1 = str(list1)
print(str1, type(str1))
print(str1[-2]) # 6
print(str1[0])  # [
print(str1[-1], str1[2], str1[3]) # ] ,

print("_"*50)
### list -> tuple ####
list_2 = [5, 8, 2, 7]
tup_2 = tuple(list_2)
print(tup_2, type(tup_2), tup_2[0])
# (5, 8, 2, 7) <class 'tuple'> 5


print("_"*50)
### list -> dict ####
"""
list_3 = [5, 8, 2, 7]
dict_3 = dict(list_3)
print(dict_3)
"""
# cannot convert dictionary update sequence element #0 to a sequence



# if we have 2 list, then we can create a dictionary with the help of zip function
list_a = ['a', 'b', 'c']
list_b = [4, 6, 8]

result = dict(zip(list_a, list_b))
print("result :", result, type(result))
# result : {'a': 4, 'b': 6, 'c': 8} <class 'dict'>




print("_"*50)
### list -> set ####
list_p = [5, 7, 2, 8, 5, 7, 2]
set_p = set(list_p)
print(set_p, type(set_p))
# {8, 2, 5, 7} <class 'set'>
print(list(set_p))  # [8, 2, 5, 7]

print("_"*50)
### list -> bool ####
list_x = []
bool_x = bool(list_x)
print(bool_x, type(bool_x)) # False <class 'bool'>


list_y = [5, 7, 8]
bool_y = bool(list_y)
print(bool_y, type(bool_y))  # True <class 'bool'>


########################### Tuple ####################

# tuple -> int # conversion is not possible
# tuple -> float # conversion is not possible

print("_"*50)
#### tuple -> string ####
tup1 = (5, 7, 2, 8)
str1 = str(tup1)
print(str1, type(str1), str1[0], str1[1])
# (5, 7, 2, 8) <class 'str'> ( 5



print("_"*50)
#### tuple -> list ####
tup2 = (5, 7, 2, 8, 1)
list2 = list(tup2)
print(list2, type(list2))  # [5, 7, 2, 8, 1] <class 'list'>
list2.append(100)
print(list2) # [5, 7, 2, 8, 1, 100]


print("_"*50)
#### tuple -> dict ####   conversion is not possible
#### tuple -> set ####
tup3 = (5, 7, 2, 8, 1, 6, 7, 2)
set3 = set(tup3)
print(set3, type(set3))
# {1, 2, 5, 6, 7, 8} <class 'set'>



# print("_"*50)
# #### tuple -> boolean ####

tup_a = tuple()
bool_a = bool(tup_a)
print(bool_a, type(bool_a))
# False <class 'bool'>

tup_b = (5, 7, 2, 8)
bool_b = bool(tup_b)
print(bool_b, type(bool_b))
# True <class 'bool'>


tup1 = ('Name', 'Age', 'Email')
tup2 = ('rahul', 20, 'rahul@gmail.com')
result_dict = dict(zip(tup1, tup2))
print(result_dict)
# {'Name': 'rahul', 'Age': 20, 'Email': 'rahul@gmail.com'}

##################### Dictionary #################

## Dict -> int #### conversion is not possible
## Dict -> float #### conversion is not possible

print("_"*40)
## Dict -> string ####
dict1 = {'a' : 123, 'b' : 456}
str_a = str(dict1)
print(str_a, type(str_a), str_a[0], str_a[-2])
# {'a': 123, 'b': 456} <class 'str'> { 6



print("_"*40)
## Dict -> list ####
dict2= {'a' : 123, 'b' : 456, 'c' : 789}
list_2 = list(dict2)
print(list_2, type(list_2))
# ['a', 'b', 'c'] <class 'list'>



print("_"*40)
#### Dict -> tuple ####
dict2= {'a' : 123, 'b' : 456, 'c' : 789}
tup2 = tuple(dict2)
print(tup2, type(tup2))
# ('a', 'b', 'c') <class 'tuple'>



print("_"*40)
#### Dict -> set ####
dict3= {'a' : 123, 'b' : 456, 'c' : 789}
set3 = set(dict3)
print(set3, type(set3))
# {'b', 'c', 'a'} <class 'set'>

print(dict3.values())
# dict_values([123, 456, 789])


print("_"*40)
#### Dict -> bool ####

dict_a = {}
bool_a = bool(dict_a)
print(bool_a, type(bool_a))
# False <class 'bool'>

dict_b = {'a' : 456, 'b' : 123}
bool_b = bool(dict_b)
print(bool_b, type(bool_b))
# True <class 'bool'>



####################### Set ########################

### Set -> Int ##### conversion is not possible
### Set -> Float ##### conversion is not possible


print("_"*50)
### Set -> string #####
set_a = {4, 7, 9, 1, 5, 4}
str_a = str(set_a)
print(str_a, type(str_a))
print(str_a[0], str_a[1], str_a[-1])  # { 1 }


print("_"*50)
### Set -> list #####
set_b = {4, 7, 9, 1, 5, 4}
list_b = list(set_b)
print(list_b, type(list_b))
# [1, 4, 5, 7, 9] <class 'list'>


print("_"*50)
### Set -> tuple #####
set_c = {4, 7, 9, 1, 5, 4}
tup_c = tuple(set_c)
print(tup_c, type(tup_c))
# (1, 4, 5, 7, 9) <class 'tuple'>

print("_"*50)
### Set -> dict #####   # CONVERSION IS NOT POSSIBLE
"""
set_d = {4, 7, 9, 1, 5, 4}
dict_d = dict(set_d)
print("dict_d :", dict_d)

# cannot convert dictionary update sequence element #0 to a sequence
"""

print("_"*50)
### Set -> Boolean #####
set_e = set()
bool_e = bool(set_e)
print(bool_e, type(bool_e))
# False <class 'bool'>


set_f = {4, 7, 9}
bool_f = bool(set_f)
print(bool_f, type(bool_f))
# True <class 'bool'>

