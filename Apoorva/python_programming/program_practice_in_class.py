#1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

num1 = 24

if num1%2 == 0:
    print("square value is:",num1**2)
elif num1%3 == 0:
    print("Cube value is:",num1**3)
elif num1%7 == 0:
    print("power to 4 value of number is",num1**4)
else:
    print("number is not divisible 2,3 or 7")

#2.write a python program to create a calculator where we have to three inputs from users
#var1 = take value for action
#var2 = take value for operation
#var3 = take value for operation

#if var1 ==1 : addition of var2 and var3
#if var1 ==2 : multiplication of var2 and var3
#if var1 ==3 : division of var2 and var3
#if var1 ==4 : subtraction of var2 and var3

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

    ############# Pratyusha's code for calculator#################

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Choose a operator: ")
    if operation == '+':
        print("Addition of two numbers is: ", num1 + num2)
    elif operation == '-':
        print("Subtraction of two numbers is: ", num1 - num2)
    elif operation == '*':
        print("Multiplication of two numbers is: ", num1 * num2)
    elif operation == '/':
        print("Division of two numbers is: ", num1 / num2)
    else:
        print("Invalid operator")

