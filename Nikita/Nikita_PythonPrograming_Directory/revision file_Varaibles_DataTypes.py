""""
a = 10
print(a) #print function will print the value of variable a
print(id(a))

b = 10
print(id(a))
# if two varaible holds same value then adrress will be the same
# = is an assignment operator we assign value with assignment operator

# assign one value to three different variable
p = q = r = 50
print("value of p:", p)
print("value of q:", q)
print("value of r:", r)


#assign three different variables to three different values
x, y, z = 30, 40, 50
print("value of x:", x , id(x))
print("value of y:", y , id(y))
print("value of z:", z , id(z))

# Rules to define a variable
#1. There should not be space in variale name
# a b = 50 invalid
# a_b = 50 valid
    #x_y_z = 500 invalid
# x_y_z = 500 valid

#2. Special charatcers are not allowed in the vriable name
#email_$_id = "testuser@gmail.com" invalid
email_id = "testuser@gmail.com"
print(email_id)

#3 can not keep number as prefix in the varialbe name
#1var_value = 600 #invalid

#4 varialbe name are case sensitive

Name = 'Rahul'
NAME = "iNDIA"
name = "priya"
nAme = "pAyal"

print(Name)
print(NAME)
print(name)
print(nAme)
"""
"""
+ : plus
- : minus
* : multiplication
/ : division with single slash
// : division with double slash
% : Remainder operator
** : power operator
== : For comparision operator
!= : not equal to operator
"""

"""
# This will repeat the # value 50 times to draw a line
print("#" * 50)

# Addition of values
var1 = 500
var2 = 600
print("addition of value :", var1 + var2)
var3 = var1 + var2
print("addition with third variable :", var3)
"""
"""
var_p = 50
var_q = 3
print("multiplication :", var_p * var_q)

multiply = var_p * var_q
print("multiplication value :", multiply)

"""
"""
print("#" * 50)
### subtraction of values ###
var_s = 100
var_t = 50
print("subtraction output:", var_s - var_t)
"""

"""
## division of values ####

var_k = 600
var_l = 11
# division with single slash
print("division output :", var_k/var_l) # 54.54545454545455

# division with double slash
print("division output :", var_k//var_l) # 54

var_o = 45
var_6 = 11
print(var_o/var_6) # 4.090909090909091
print(var_o//var_6) # 4


print("_"*50)
# power operator: **

print("square of 2 :", 2**2) # 2*2
print("cube of 4 :", 4**3) # 4*4*4 : 64
print("cube of 5 :", 5**3) # 5*5*5 : 125
"""
"""
num1 = 30
print("check for even :", num1%2 == 0) # even True

print("check for odd :", 9 % 2 != 0) # odd True
"""
"""
### comparison operator ==
n1 = 40
n2 = 40
n3 = 70
print(n1 == n2) # True
print(n1 == n3) # False
"""

# 6. compound interest calculation
#
# CI=  ((P*(1+i)^n) - P)
# P = principle amount
# i = interest rate
# n = time period
"""
P = 100000
i = 0.07
n = 3
CI = (P*((1+i)**n) - P)
print("compund interest:", "is:", CI)
"""

#Python data type

"""
1. Number:
    i). Integer
    ii). Float
    iii). Complex Number

2. Sequential: (they follow indexing (positive and negative)
    i). String
    ii). List
    iii). Tuple

3. Dictionary
4. Set
5. Boolean
"""
# in python everything is object
# integer data type does not have any limit to defined the value
#integer belongs to int class
# Every whole number is integer (integer data types only contains whole number no decimal
# integer is immutable datatype (means it re-place the previous value)(it can hold only one value)
# it also consider negative numbers
"""
num1 = 40
print(type(num1), num1)

num1 = 50
print(type(num1), num1)
"""
"""
properties of FLOAT
->  float data type represent with keyword as float (<class 'float'>)
->  float data type does not have any limit to defined the value
->  float is immutable data type
->  float data type only contains pointer value
"""
"""
var_a = 50.55
print("data type of var_a :", type(var_a), var_a)

var_b = 564356435636.4968925812
print("data type of var_b :", type(var_b), var_b) # <class 'float'> 564356435636.497

var_c = 45.49548934525434
print("data type of var_c :", type(var_c), var_c) # <class 'float'> 45.49548934525434

var_d = 0.0
print("data type of var_d :", type(var_d), var_d) # <class 'float'> 0.0
"""

# Complex number #####
"""
-> complex number is combination of real and image values
-> complex number is represent in the format of x+yj, x-yj, -x+yj
-> complex number is immutable data type.
-> it will always be j
"""

"""
var_e = 50 + 40j

print("imaginary value :", var_e.imag) # 40.0
print("real value :", var_e.real) # 50.0
"""
"""
var_f = 5 + 10j
var_g = 8 + 15j
var_h = var_f + var_g
print("Addition of complex number :", var_h, type(var_h), var_h.real, var_h.imag)
"""

"""
var_k = -10 * 5j
print(var_k, type(var_k), var_k.imag, var_k.real)

result = complex(70 , 60)
print(result)
"""

"""
var_t = 59 - 7j
print(var_t, var_t.imag, var_t.real)
"""

############################
#######String data type##########
#->  string is immutable data type
#->  string follows positive and negative indexing
#-> in string . also has a value
#->  string can defined with single quotes, double quotes and triple quotes.
#->  string only contains any value under quotes
#-> IT contains special characters

#0 1 2 3 4
#h e l l o
#-5 -4 -3 -2 -1
"""
str1 = "hello"
print(str1[-4])
print(str1[0])

str_a = "Hello '%*()'(*"
print(str_a)
str_b = 'Python "5435"34543'
print(str_b)
"""
# str_c = """
# python
# programming
# learning  *&)(*)(*()*)(*
# automation
# """
# print(str_c)


#########list##########
# # list is a mutable data type, it contains previos along with new
# -> List follow positive and negative indexing as like string.
# -> List can contains all type of data, int, float, string, list, tuple, dict, set, boolean
# -> List represent with square brackets.
# -> All values are in list will be comma separated

list = [4, 4.5, "hello", [1, 4, 5,]] #list inside list is called child list
print("list:", list, type(list))

#   0   1    2       3
#  [4, 4.5, 'Hello', [1, 4, 5]]
#   -4  -3   -2      -1
print(list[3])  # [1, 4, 5]
print(list[-2]) # Hello

list2 = [2, 4.5, "python", [1, 2, 3], (4, 5,7 ), {'a':123, 'b': 456}, {9, 56, 90}, True, False, None]
print(len(list2),type(list2))
print(list2[5])

string = 'Nikita'
print('length of Nikita letters:', len(string))

#Example why it is mutable

#appends adds one value at time
# it adds only at the last
list3=[4,6,8]
list3.append(10) #this is used to add a parameter append is a method
print(list3) #[4, 6, 8, 10]
#print(dir(list)) # ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


 ##############tuple###########
 # tuple is exact same as list
 # the difference is tuple is immutable data type, once it is defined it can not be modified
 # duplicate valuse are allowed in tuple
 # -> Tuple follow positive and negative as like list and string.
# -> Tuple can contains any of data, int, float, string, list, tuple, dict, set, boolean
# -> Tuple represent with round bracket.
# -> Tuple is faster than list data type
# -> We can store fixed data tuple, that we dont want to change in future.
#   e.g. months in year, days in week etc

"""
tup1 = (4, 5.6, 'Programming', [3, 6, 7],
        (1, 5, 7), {'a': 345,'b' : 456})

print(tup1, type(tup1))
print("total values in the tuple :", len(tup1))
print("first value in the tuple :", tup1[0]) # 4
print(tup1[2]) # Programming
print(tup1[-1]) # {'a': 345, 'b': 456}
print(tup1[-5]) # 5.6

print(len(tup1))
print(dir(tuple))
"""
# properties of dictionary
"""
-> dictionary is mutable data type, we can update the data at any point of time.
-> dictionary does not follow positive or negative indexing
-> dictionary store values in key value format
-> dictionary represent with {} braces.
-> dictionary only contains unique keys, duplicate keys are not allowed.
-> dictionary can contains duplicate values.
-> Only immutable data type can be key in the dictionary , int, float, string, tuple, boolean
(list and set and dictionary can not be the key because they are mutable)
-> All type of data can store as value in the dictionary
-> key is wriiten in [] big brakets
"""

"""
dict1 = {'name': 'Rahul', 'name' : 'Mohit'}
dict1[234] = [4, 7, 8]
dict1['Python'] = 'Good Morning'
dict1[(5, 7, 9)] = {4, 8, 1, 5, 4}
# dict1[[4, 7, 9]] = 'Python'  # TypeError: unhashable type: 'list'
dict1[{8, 9, 7}] = "python" #TypeError: unhashable type: 'set'

dict1[4.5] = True
dict1[False] = (4, 7, 1, 8)
dict1[4.5] = 'Hello'
print(dict1)
"""
"""
#################Set###############
# properties:
->  set is mutable data type
->  set only store unique values, duplicate values are not allowed.
->  set can contains only immutable data type
->  multable data type are not allowed as set member e.g list, dict, set.
->  set store data in random order.
->  set does not follow any indexing.
->  set represent with curly braces
-> in tuple we use append and in set we use add(tuple adds at the end set adds the new parameter at any place

"""

"""
set2 = {5, 7, 9, 2, 4, 5}
print("set2 :", set2)
set2.add(100)
print("set2 :", set2)
print(dir(set))
"""
#set3 = {5, 7, (4, 6, 9), [9, 8, 5]}
#print(set3) # unhashable type: 'dict'
#set3 = {5, 7, (4, 6, 9), {'a':678, 'p': 234} }
#print(set3) # unhashable type: 'dict'

#Example of a Dictionary with Duplicate Values:

student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 85,  # Duplicate value
    "David": 92    # Duplicate value
}
# Printing the dictionary
print(student_grades)

# Accessing values
print(student_grades["Alice"])  # Output: 85
print(student_grades["Charlie"])    # Output: 85

# Example of a Dictionary with no Duplicate Values becuase it can not have
fruits = {"apple", "banana", "cherry", "apple"}  # 'apple' will appear only once

# Printing the set
print(fruits)  # Output: {'banana', 'apple', 'cherry'} (order may vary)

# Adding an element to the set
fruits.add("orange")
print(fruits)  # Output: {'banana', 'apple', 'orange', 'cherry'}

#################bollean###########
# boolean data type

"""
-> Boolean values represent with True and False
-> Boolean is immutable data type
-> Boolean always consider as return value of any logical condition
"""
var1 = True
var2 = False
print(var1, type(var1))  # True <class 'bool'>
print(var2, type(var2))  # False <class 'bool'>

num1 = 300
num2 = 400
num3 = 300
print(num1 == num2) # False
print(num1 == num3) # True

