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
"""
# string to float
# if contains string contains numbers then only conversion is possible
# if sring contains character along with float value then conversion is not possible
s5 = "667.09"
f5 = float(s5)
print(f5, type(f5))
"""
# string to list
#is possible becuse of sequentail property

s6 = "python"
l1 = list(s6)
