#1). Python program to check given number is divided by 3 or not.
# Take input through the user
"""num = int(input("Please enter number :"))
# Check whether the number is divisible by 3
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")    """


#2. If else program to get all the numbers divided by 3 from 1 to
"""for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")"""

#4). Python program to check the given number divided by 3 and 5.
"""num_a = int(input("Please enter the values :"))

if num_a % 3 == 0 and num_a % 5 == 0:
    print("The number can divide by 3 and 5 :", num_a)
else:
    print("The number can not divide by both 3 and 5 :", num_a)"""

#Python program to check given number is a prime number or not## doubt
#5.Python program to print the square of the number if it is divided by 11.
"""num = int(input("Enter a number: "))
# Check for division
if num % 11 == 0:
    # Print output
    print(num**2)
else:
    # Print output
    print("Number is not divisible by 11")"""


# age = str(input("Please enter your package: "))
#
# if age == "1,000":
#     print('You are Manish')
# elif age == "500":
#     print('You are Sagar')
# else:
#     print('I do not know you')



# Concept of f string in python
# age = "30"
# name_1 = f"Nikita age is {age}"
#
# print(name_1)

""" name = input("Enter name: ")
password = input("Enter password: ")
# Authenticate username and password
if name == password:
# Print output
    print("It is valid")
else:
# Print output
    print("It is not valid") """

# write a python program to check given number can divide by 2 and 3 with
# nested if

"""num_b = 14
if num_b % 2 == 0:
    print("The number can divide 2:", num_b)
    if num_b % 3 == 0:
        print("The number can divide 3:", num_b)
    else:
        print("The number can not divide 3:", num_b)
else:
    print("The number can not divide 2:", num_b)"""

# Q1. write a python program to show interview process with nested if condition

#1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

"""num = int(input("Please enter number :"))
if  num%2==0:
    print("the number is divisble by 2:", num**2)
elif num % 3 == 0:
    print("the number is divisble by 3:", num**3)

elif num%7==0:
    print("the number is divisble by 7:", num**4)

else:
    print("Number is not divisble")"""
#write a python program to create a calculator where we have to three inputs from users
"""var1 = take value for action
var2 = take value for operation
var3 = take value for operation

if var1 ==1 : addition of var2 and var3
if var1 ==2 : multiplication of var2 and var3
if var1 ==3 : division of var2 and var3
if var1 ==4 : subtraction of var2 and var3"""

var1 = int(input("enter the var1 value :"))
var2 = int(input("enter the var2 value :"))
var3 = int(input("enter the var3 value :"))

if var1 == 1:
    print("var2+var3 is:" , var2+var3)
elif var1 == 2:
    print("var2*var3 is:", var2*var3)
elif var1 == 3:
    print("var2%var3 is:", var2 / var3)
elif var1 == 4:
    print("var2-var3 is:", var2 - var3)
else:
    print("No operations to be done")



