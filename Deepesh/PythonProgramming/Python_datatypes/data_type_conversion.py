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


print("_"*50)
### int -> string ###
num1 = 657
str1 = str(num1)
print(str1, type(str1), str1[0])
# 657 <class 'str'> 6

str2 = '"Hello"'
print(str2)

print("_"*50)
### int -> list ###  coversion is not possible
"""
num2 = 7655765
l1 = list(num2)
print(l1)
#  'int' object is not iterable
"""
print("_"*50)
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


print("_"*50)
############## Float ##########

### float -> int #####
f2 = 55.56
n1 = int(f2)
print(n1, type(n1))  # 55 <class 'int'>


print("_"*50)
### float -> string #####
f3 = 66.83
s2 = str(f3)
print(s2, type(s2))  # 66.83 <class 'str'>
print(s2[3]) # 8
