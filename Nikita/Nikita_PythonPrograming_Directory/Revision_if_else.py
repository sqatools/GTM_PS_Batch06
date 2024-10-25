"""
a = 500
b = 800
print (a == b)# False if we write print(a==b) only then it will print true False else
#it will only print else's result
"""
"""
if a == b:
    print("a and b has equal values")

else:
    print("a and b has different values")
#a and b has different values

#input always take user input instring format, we have to convert it as per our requirement
var1 = input("please enter your value:")
print(var1, type(var1))#456 <class 'str'>
"""
"""
#write a python program to check given number is odd or even
num1 = int(input("enter value to check number is odd or even:"))
print(num1 % 2)
if num1 % 2 == 0:
    print("this number is even number:", num1)
else:
    print("this number is odd number:", num1)

#1
#this number is odd number: 81
"""


num1 = int(input("enter value to check number is odd or even:"))
print(num1 % 2 == 0)
if num1 % 2 == 0:
    print("this number is even number:", num1)
else:
    print("this number is odd number:", num1)

#False
#this number is odd number: 55
"""
#another way to write above program
num2 = int(input("enter value to check number is odd or even:"))
list_a = ["Even", "odd"]
print("Number is:", list_a[num2 % 2])

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

print(num_a%2 == 0 and num_a%3 == 0 )#This will say true or false

if num_a%2 == 0 and num_a%3 == 0:
    print("Given number can divide by 2 and 3 :", num_a)
else:
    print("Given number can not divide by 2 and 3 :", num_a)
"""
