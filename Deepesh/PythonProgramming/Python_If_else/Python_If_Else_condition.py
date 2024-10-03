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

"""
# write a program to check the given is divisible by 2 or 3
print("_"*50)
num_a = int(input("Please enter the values :"))

if num_a%2 == 0 or num_a%3 == 0:
    print("The number can divide by 2 or 3 :", num_a)
else:
    print("The number can not divide by both 2 or 3 :", num_a)
"""

"""
# If - elif - else condition

if cond1:
    code
elif cond2:
     code
elif cond3:
     code
else:
    code 
"""

"""
# logical operators
> : greater than
< : less than
>= : greater equal to
<= : less equal to
!= : not equal
== : equal to
in : in operator
is : is operator
"""
# --------------------------------------------
"""
print("_"*50)
# write a python program to check which number have greater value among three
# variables

p = 90
q = 80
r = 90

if p > q and p > r:
    print("P has greater value :", p)
elif q > p and q > r:
    print("Q has greater value :", q)
elif r > p and r > q:
    print("R has greater value :", r)
elif p == q:
    print("P and Q has same value :")
elif p == r:
    print("P and R has same value :")
elif q == r:
    print("R and Q has same value :")
else:
    print("No one has greater value")

"""
# --------------------------------------------

"""
# write a python program to implement the exam result marking
marks = int(input("Please enter the marks:"))
if marks > 100:
    print("Please enter valid marks, can not more than 100")
elif 40 < marks <= 50:
    print("Passed with D grade")
elif 50 < marks <= 60:
    print("Passed with C grade")
elif 60 < marks <= 70:
    print("Passed with B grade")
elif 70 < marks <= 80:
    print("Passed with A grade")
elif 80 < marks <= 90:
    print("Passed with A+ grade")
elif 90 < marks <= 100:
    print("Passed with Excellent A++ grade")
else:
    print("Failed in examination")

"""

#################### Nested If condition #############

"""
if cond1:
     code
     if cond2:
         code
         if cond3:
             code
         else:
             code
     else:
         code
else:
     code
"""

# write a python program to check given number can divide by 2 and 3 with
# nested if

num_b = 14
if num_b % 2 == 0:
    print("The number can divide 2:", num_b)
    if num_b % 3 == 0:
        print("The number can divide 3:", num_b)
    else:
        print("The number can not divide 3:", num_b)
else:
    print("The number can not divide 2:", num_b)

# Q1. write a python program to show interview process with nested if condition
