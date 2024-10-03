#Q)1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number
"""num=int(input("enter the num:"))
if num % 2 ==0:
    print("it is divisible by 2:",num**2)
else:
    print("its not divisible by 2:")
if num % 3 == 0:
    print("it is divisible by 3:",num ** 3)
else:
    print("its not divisible by 3:")

if num % 7 == 0:
        print("it is divisible by 7:",num ** 4)
else:
    print("its not divisible by 7:")"""

#Q)2.write a python program to create a calculator where we have to three inputs from users
#var1 = take value for action
#var2 = take value for operation
#var3 = take value for operation

#if var1 ==1 : addition of var2 and var3
#if var1 ==2 : multiplication of var2 and var3
#if var1 ==3 : division of var2 and var3
#if var1 ==4 : subtraction of var2 and var3

"""var1=int(input("enter the value:"))
var2=10
var3=5
if var1 == 1:
    print("addition of var2 and var3:",var2 + var3)

elif var1 == 2:
    print("multiplication of var2 and var3:",var2 * var3)
elif var1 == 3:
    print("division of var2 and var3:",var2 / var3)
elif var1 == 4:
    print("subtraction of var2 and var3:",var2 - var3)
else:
    print("entered value is not matching ")"""

#Q)3.Python program to check given number is divided by 3 or not.
"""num=int(input("enter the number:"))
if num % 3 ==0:
    print("given number is divisble by 3")
else:
    print("given number is not divisble by 3")"""

#Q)4. If else program to get all the numbers divided by 3 from 1 to 30.

for num in range (1,31):
    if num % 3 == 0:
        print(num,end=' ')
