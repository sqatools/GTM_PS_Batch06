"""
# 1. inter to Float
num = 400
f1 = float(num1)
print(f1, type(f1))

# 2. integer to string
num2 = 400
s1 = str(num2)
print(s1, type(s1), s1[0])
"""
# 3. integer to list
# 4. integer to tuple
# 5. integer to list dictionary
# 6. integer to set
#Not iterable because list contains multiple values and because integer contains only single value

# 7. integer to bollean

"""
num_a = 0
b1 = bool(num_a)
print(b1 , type(b1)) #False <class 'bool'> because it has 0 value
# for any value other than 0 it will be true

num_b = 98
b1 = bool(num_b)
print(b1 , type(b1))#True <class 'bool'>
"""

################Float###########
#1. float to integert
"""
f2 = 77.89
n1 = int(f2)
print(n1, type(n1)) #77 <class 'int'>
"""
# 2. float to string in float . also have a position
"""
f3 = 99.77
s4 = str(f3)
print((s4), type(s4), s4[2]) #99.77 <class 'str'> .

# 3. float to list
# 4. float to tuple
# 5. float to list dictionary
# 6. float to set
#Not iterable because list contains multiple values and because integer contains only single value
"""

# 7. Float to bollean
"""
f1 = 78.98
b1 = bool(f1)
print(b1, type(b1)) #True <class 'bool'>

f1 = 0.00
b1 = bool(f1)
print(b1, type(b1)) #False <class 'bool'>
"""
########string###########
#string to integer
#if string contains character then conversion is not possible
"""
s2 = "HELLO789"
n3 = int(s2)
print(s2, type(s2)) #invalid literal for int() with base 10: 'HELLO789'
"""
"""
#if sting contains only value
s4 = "878988"
n4 = int(s4)
print((n4), type(n4), n4*2)#878988 <class 'int'> 1757976
"""

# string to float
# if contains string contains numbers then only conversion is possible
# if sring contains character along with float value then conversion is not possible
s5 = "667.09"
f5 = float(s5)
print(f5, type(f5))

# string to list
#is possible becuse of sequentail property
# it follows indexing

str_d = "Python"
list_d = list(str_d)
print(list_d, type(list_d))#['P', 'y', 't', 'h', 'o', 'n'] <class 'list'>

#string to tupple
strf = "programming"
tupe = tuple(strf)
print(tupe , type(tupe)) #('p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g') <class 'tuple

#string to dictionary
"""
str_y = "python programming"
dict_y = dict(str_y)
print(dict_y , type(dict_y))

#ValueError: dictionary update sequence element #0 has length 1; 2 is require
#why we will convert string into dictionary in real time if we want a dictnioary
# we will write a dictinoary why we will write in a string format becuae text file 
#only consider string format even if you write dictnoary in notepad it will consider it as a text data
#so we will use json module 
"""

import json

details = '{"Name" : "John", "Mobile" : "6376363", "email" : "john@yopmail.com"}'
data = json.loads(details)
print(data, type(data))
#{'Name': 'John', 'Mobile': '6376363', 'email': 'john@yopmail.com'} <class 'dict'>
print(data['Name'])#John

#string to set
str_h = "python programming $ %"
set_h = set(str_h)
print(set_h, type(set_h))
#{'a', '$', 'm', ' ', 'r', 'i', 'o', 't', '%', 'y', 'n', 'g', 'h', 'p'} <class 'set'>

#string to bollean

str_j = ""
bool_j = bool(str_j)
print(bool_j, type(bool_j))#False <class 'bool'>

str_k = "python"
bool_k = bool(str_k)
print(bool_k, type(bool_k))#True <class 'bool'>

##########################LIST############
#list to integet conversion is not possible
#list to float conversion is not possible

list1 = [4 , 5, 6]
#it will also convert the bracket the value of bracket here is 0 value of 4 is 1
str_1 = str(list1)
print(str_1, type(str_1))#[4, 5, 6] <class 'str'>
print(str_1[-2])#6
print(str_1[0])#[

########list to tuple###########
#list and tupple have same properties so its indexing will be same
list_6 = [7, 6, 7, 9]
tupp = tuple(list_6)
print(tupp, type(tupp), tupp[0])#(7, 6, 7, 9) <class 'tuple'> 7

#list to dictionary
"""
list_9 = [7, 6, 7, 9]
dict_9 = dict(list_9)
print(dict_9, type(dict_9))#TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""

#but by zip function one can do the conversion
#it combines two lists into a dictinoary
list_11 =["a", "b", "c", "d"]
list_12 =["4 ", "5" , "6"]
result = dict(zip(list_11, list_12))
print( result, type(result))#{'a': '4 ', 'b': '5', 'c': '6'} <class 'dict'>
# extra d is not printed because we have not assigned value to it

#list to set

list_n = [4, 5, 7, 7, 8]
set_n = set(list_n)
print(set_n, type(set_n))#{8, 4, 5, 7} <class 'set'>
#set removes the duplicate data
#again convert in list below
print(list(set_n))#[8, 4, 5, 7]

#list to boolean

list_x = []
bool_x = bool(list_x)
print(bool_x, type(bool_x))#False <class 'bool'>

list_y = [4, 6, 7]
bool_y = bool(list_y)
print(bool_y, type(bool_y))#True <class 'bool'>

##########Tuple#####

#tuple to integer
#conversion is not possible

#tuple to float
#conversion is not possible

#tuple to string
tup_1 = (3, 5, 7, 9)
str_1 = str(tup_1)
print(str_1, type(str_1), str_1[-1], str_1[-3], str_1[-4])
#(3, 5, 7, 9) <class 'str'> )   ,
#in index postions it will consider brackets and spaces

#tuple to list
tup_2 = (3, 5, 7, 9, 9, 10, 10, 5, 2, 1,)
list_2 = list(tup_2)
print(list_2, type(list_2))
#[3, 5, 7, 9, 9, 10, 10, 5, 2, 1] <class 'list'>

#tuple to dictionary is not possible
#tuple to dictionary with zip function is possible
tup_k = ('Name', 'age', 'email')
tup_r = ('reema', 55, 'rema@gmail.com')
result_1 = dict(zip(tup_k, tup_r))
print(result_1)
#{'Name': 'reema', 'age': 55, 'email': 'rema@gmail.com'}


#tuple to set
tup_4 = (3, 5, 7, 9, 9, 10, 10, 5, 2, 1,)
set_3 = set(tup_4)
print(set_3, type(set_3))#{1, 2, 3, 5, 7, 9, 10} <class 'set'>
#tuple to set is possible it is easy True, False

#########Dictionary########
#1. dict to integer is not possible
#2. dict to float is not possible

#. dict to string
dict_1 = {'a' : 3, 'b' : 0}
str_l = str(dict_1)
print(str_l, type(str_l), str_1[-1], str_l[0])
#{'a': 3, 'b': 0} <class 'str'> ) {

#dict to list
#it will give the list in form of keys that is it will only take the keys
dict_2 = {'a' : 3, 'b' : 0, 'd': 9}
list_m = list(dict_2)
print(list_m, type(list_m), list_m[-1], list_m[0])
#['a', 'b', 'd'] <class 'list'> d a

#dict to tuple#
#it will give the list in form of keys that is it will only take the keys
dict_3 = {'a' : 3, 'b' : 0, 'd': 9}
tup_m = tuple(dict_3)
print(tup_m, type(tup_m), tup_m[-1], tup_m[0])
#('a', 'b', 'd') <class 'tuple'> d a

#dict to set#
dict_4 = {'a' : 3, 'b' : 0, 'd': 9}
set_m = set(dict_4)
print(set_m, type(set_m))#{'a', 'd', 'b'} <class 'set'>

print(dict_4.values())#dict_values([3, 0, 9])
#this is the method to get values and at the time of conversion it will not print values

#dict to boolean possible (True and False)


###################set#################
#set to integer conversion is not possible
#set to float conversion is not possible

#set to string conversion is possible
set_b = {4, 6, 7, 8, 9, 45, 90}
str_b = str(set_b)
print(str_b, type(str_b))
print(str_b[0], str_b[1], str_b[-1])
#at the time of conversion it also prints the bracket and spaces in counting

#set to list conversion is possible
set_c = {4, 6, 7, 8, 9, 45, 90}
list_c = list(set_c)
print(list_c, type(list_c))
print(list_c[0], list_c[1], list_c[-2])
# it does not print count bracket and spaces

#set to tuple
set_d = {4, 6, 7, 8, 9, 45, 90}
tup_d = tuple(set_d)
print(tup_d, type(tup_d))
print(tup_d[0], tup_d[1], tup_d[-2])
# it does not print count bracket and spaces

#set to dict is not possible#

#set to boolean is possible
