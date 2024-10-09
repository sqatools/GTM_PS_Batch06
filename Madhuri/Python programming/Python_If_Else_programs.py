#The if-else statement is conditional statement in programming.
# It executes a set  of instructions
# if a particular condition is true, and another set of instructions
# if the condition  is false
#1 Python program to check given number is divided by 3 or not
# take  a number input through the user
"""
"""
"""
#__________________________________________
num = int(input("please enter number:"))
# check whether the number  is divisible by 3
if  num%3 == 0:
    print("Number is divisible by 3")
else:
    print("number is not divisible by 3")
"""

"""
"""
"""
#___________________________________________________________________
# 2   validate user_id in the list of user ids
id_list = [1,2, 3, 4, 5, 6, 7, 8]
# take user id as input through the user
user = int(input("enter id number:"))
if user in id_list:
    print("valid ID")
else:
    print("invalid id")
"""
#---------------------------------------------------------------------------
"""


"""
# 3 We will assign grades as per total marks
# we will assign  grades to each students as per total marks scored
# condition for  grades
# Marks less than 40; fail
# marks between 40-50: grade c
# marks between 51- 60 grade B
# marks between  61-70: grade A
# marks between 71-80: grade A+
# marks between 81-90: grade A++
# marks between 91-100: Excellent
# Take marks through the user
"""

"""
"""
"""
"""
marks = int(input("Enter Marks:"))
# assign grades based  on marks
if marks<40:
    print("fail")
elif marks>=40 and marks>=50:
    print("Grade c:")
elif marks>=50 and marks<=60:
    print("Grade B:")
elif marks>60 and marks<=70:
    print("grade A:")
elif marks>70 and marks<=80:
    print("grade A+")
elif marks>80 and marks<=90:
    print("Grade A++:")
elif marks>90 and marks<=100:
    print("Excellent")
else:
    print("Invalid marks")
"""
"""

"""
#__________________________________________________________
"""

"""
"""
"""
"""
# 4 Describe the  interview process
# use nested - if  else statements
round1 = input("enter the round1 result:")
round2 = input("enter the round2 result:")
if round1 == "passed":
    print("Congrats your 1st  round is clear")
    if round2 == "passed":
        print("Congrats your 2nd round is clear,you are placed")
    else :
        print("not selected in second round")
else:
   print("not selected")
"""
"""

"""
# write a python program to check given number is divisible by 2 and 3 and 7
# if divisible by 2 then square of the value
#if divisible by 3 then cube of the value
#if divisible by 7 then quatra of the value
"""
"""
"""
num = int(input("enter the number"))
if num%2 == 0:
    print(num**2)
elif num%3 ==0:
    print(num**3)
elif num%7 ==0:
    print(num**4)
else:
    print("The number can not divide by 2,3 or 7")
"""

"""
#_________________________________________________
x , y, z = 40, 50, 60
a = 60
b = 70
a , b = b, a
"""

"""
# write a python program to create a calculator where we have to three inputs from users
Var1 = 3
var2 = 3
var3 = 6
# operation = + output =12
var1 = int(input("Enter 1st number:"))
#var2 = int(input("Enter 2nd number:"))
Var3 = int(input("Enter 3 rd number"))
operation = input("Enter operation of your choice")
if operation == '+':
    print(var1+var2+var3)
elif operation == '-':
      print(var1-var2-var3)
elif operation == '*':
    print(Var1*var2*var3)
elif operation == '/':
     print(var1/var2)
else:
    print("Invalid operation")
"""

"""
#-----------------------------------------
# check the number is divided by 3 and 5
# take input through the user
num = int(input("Enter a number"))
if num%3 == 0 and num%5 ==0:
    print("Given number can divide by both 3 and 5")
else:
    print("Given number can not divide by both 3 and 5")
"""

"""

# we will check whether a person is eligible to vote or not
age = int(input("enter age:"))
if age>18 == 0:
    print("you are eligible")
else:
    print("you are not eligible")
"""

"""
# number is positive or not
num = int(int("enter the number:"))

if num>0:
    print("True")
else:
    print("false")
"""

"""
# Check whether  the given  number is  divisible by 11
# take input through the user
num = int(input("Enter a number"))
if num%11 == 0:
    print(num**2)
else:
    print("number is not divisible by 11")
"""

"""
# Check whether the given number is odd or even
num = int(input("Enter a number"))
if num%2 == 0:
    print("it is  an even number")
else:
    print ("it is an odd number")
# ____________________________________-
"""

"""
num = int(input("Enter a number"))
if num%2 == 0:
    print("square :", num**2)
elif num%3 == 0:
    print ("cube:", num**3)
elif num%5 == 0:
    print("addition", num++5)
"""
"""
a = 30
b = 35
print(a == b)
if a == b:
    print("a and b has equal  values")
else:
    print("a and b has  different  values")
"""
"""
# write a python program to check  given is available  in the list
list1 = [4, 7, 9, 3, 6, 7]
num1 = 8
if num1 in the list1:
    print ("data  is available  in the list")
else:
    print("dataa is not available in the list")
    
"""
"""
# write a python program get even and odd word as per value enter
# single line if condition
num2 = 16
result = "even " if num2%2 == 0  else "odd"
print(num2 , ":", result)
"""
"""
# is operator
var_a = none
if var_a is none:
    pass
else:
    print(var_a*5)

 var_b = none
if var_b is not None:
     print(var_b**7)
else:
    pass
"""
"""
# Iterate over numbers from1-30
for num in range(1,31):
    # check whether number is divisibleby 3
  if num%3==0:
    print(num, end=" ")

# iterate over numbers from 2-20
for i in range(2, 20):
    if i%2 == 0:
        print(i, end=" ")
    """"" \
"""
# iterate over numbers from 1-10
for k in range(1,10):
    if k%5==0:
        print(k, end=" - ")
"""
"""
# Check the number divided with 3 and 5
# take a input through the user
num1 = int(input("Enter a number"))
# check for division
if num1%3==0 and num1 %5==0:
 print(" Given number can divided by both 3 and 5")
else:
    print("give number can not divided by 3 and 5")
"""
"""
# print the square of the number
# take a number as input through the user
num2 = int(input("Enter a number:"))
if num2%11 == 0:
    print (num2**2)
else:
    print("number is not divisible by 11")
"""
"""
# whether the number is a prime number(for loop)
num4 = int(input("Enter a number:"))
count = 0
if i in range(2,num4):
    if num%i == 0:
        count += 1
 # check for prime number
    if count>0:
        print("It is not a prime number")
    else:
        print("it is a prime number")
"""
"""
# Check given number is odd and even(if- else)
num = int(input("Enter a number:"))
if num%2 == 0:
 print("It is an even number")
else:
    print("it is an odd number")
"""
"""
# fibonacci series
fib = [0, 1, 1, 2, 3, 5, 6, 8]
# take input through the user
num = int(input("Enter a number:"))
if num in fib:
    print("It is a part of the series")
else:
    print("It is not part of the series")
"""
"""
#  List of user id
id_list = [1, 2, 3, 4, 5, 6, 7]
id_ = int(input("Enter ID number"))
if id_ in id_list:
    print("valid id")
else:
    print("invalid id")
    """
"""
# a person eligible to vote
age = int(input("enter the age"))
if age>18:
    print("you are eligible")
else:
    print("You are not eligible")
"""
"""
# positive number or not
num = int(input("Enter a number:"))
if num>0:
    print("True")
else:
    print("false")
"""
"""
# negative number or not
num = int(input("Enter the number:"))
if num<0:
    print("true")
else:
    print("false")
"""
"""
# largest number
num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
if num1<num2 ==0:
    print("First number is greatest:")
else:
    print("Second number is greatest:")
"""
"""
# print all numbers from 10-15, expect 13
for i in range(10, 16):
    if i!= 13:
        print(i)
"""
"""
# write a program to calculate total number of odd  or even
tup_val =(5, 7,8,9,6, 12, 14)
odd_count = 0
even_count = 0
for val in tup_val:
    if val%2 == 0:
        even_count += 1  # or even_count = even_count+1
    else:
        odd_count +=1  # or odd_count = odd_count+1
print("odd count ", odd_count)
print("even count",even_count)

"""
"""

List = [2,4,6,8,3,9,11,13]
odd_count=0
even_count=0
for val in List:
    if val%2 == 0:
        even_count = even_count+1
        print("even count:",even_count)
    else:
        odd_count = odd_count+1
        print("odd count:", odd_count)

"""
"""
# tuple length of
tup_length = len(tup_val)
print("tuple length:", tup_length)
for i in range (tup_length):
  print(i,tup_val[i])
"""
"""
"""
# length of list
"""
list_length = len(list_val)
print("list_length:",list_length)
for i in range (list_length):
    print(i, list_val[i])
    """
"""
str1 = "Hello python"
for char in str1:
    print(char, end="-")
    """
# fibonacci series
a = 0
b = 1
for i in range (20):
 print(a,end="-")
 a,b = b,a+b

""""""
# while loop


























































































