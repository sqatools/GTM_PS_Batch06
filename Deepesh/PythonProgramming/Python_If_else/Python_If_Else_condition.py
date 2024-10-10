"""
if condition:
   code
else:
   code
"""


a = 30
b = 30

print(a == b)

if a == b:
    print("a and b has equal values")
else:
    print("a and b has different values")



"""
# input always take user input in string format, we have to convert it
# as per our requirement
var1 = input("Please enter your value :")
print(var1, type(var1))
"""

"""
print("_"*50)
# write a python to check given number is odd or even
num1 = int(input("Enter value to check odd or even :"))
print(num1%2)
if num1%2 == 0:
    print("This is even number :", num1)
else:
    print("This is odd number :", num1)
"""

"""
and condition

True and False : False
False and True : False
True and True : True
False and False : False
"""

"""
# write a program to check the given is divisible by 2 and 3
print("_"*50)
num_a = int(input("Please enter the values :"))

print(num_a%2 == 0  and num_a%3 == 0)

if num_a%2 == 0  and num_a%3 == 0:
    print("Given number can divide by 2 and 3 :", num_a)
else:
    print("Given number can not divide by 2 and 3 :", num_a)
"""


"""
or condition

True or False : True
False or True : True
True or True : True
False or False : False
"""

# write a program to check the given is divisible by 2 or 3
print("_"*50)
num_a = int(input("Please enter the values :"))

if num_a%2 == 0 or num_a%3 == 0:
    print("The number can divide by 2 or 3 :", num_a)
else:
    print("The number can not divide by both 2 or 3 :", num_a)
