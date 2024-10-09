# Interview process demonstration using nested if conditions
"""
# with elif
rusume_round = int(input("Resume score: "))
tech_score = int(input("Enter technical interview score: "))
hr_score = int(input("Enter HR interview score: "))

# Step 1: Resume selection
if rusume_round >= 80:
    print("Resume selection: Passed")

# Step 2:
elif tech_score > 70:
        print("Technical Interview: Pass")
        print("Sorry, you did not pass the technical interview.")

# Step 3: HR Interview
elif hr_score >= 80:
        print("HR Interview: Failed")
        print("Congratulations! You have been selected for the job.")
# Final Success Case
else:
    print("Resume selection: Failed")
    print("Technical Interview: Failed")
    print("HR Interview: Failed")


# Interview process using nested if conditions
# with nested
rusume_round = int(input("Resume score: "))
tech_score = int(input("Enter technical interview score: "))
hr_score = int(input("Enter HR interview score: "))

if rusume_round >= 90:  # Passed technical interview
    print("Resume is eligible: Passed")

    # Nested if for Technical Round
    if tech_score >= 70:
        print("Technical interview: Passed")
    else:
        print("Technical Interview: Failed")
        print("Sorry, you did not pass the Technical interview.")


    # Nested if for HR interview
    if hr_score >= 90:
        print("HR Interview: Passed")
        print("Congratulations! You have been selected for the job.")
    else:
        print("HR Interview: Failed")
        print("Sorry, you did not pass the HR interview.")
else:
    print("Resume is not eligible: Failed")
    print("Sorry, you did not pass the technical interview.")



#1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

num = int(input("Enter Number : "))

if num%2 == 0:
    print(num**2)
elif num%3 == 0:
    print(num **3)
elif num%7 == 0:
    print(num **4)

# write a python program to create a calculator where we have to three inputs from users
#var1 = int(input("Enter number:"))
#var2 = float(input("Enter number:"))
#var3 = int(input("Enter number:"))
#operator = input("Enter operator(+, -, *, /)")
#if var1 ==1 : addition of var2 and var3
#if var1 ==2 : multiplication of var2 and var3
#if var1 ==3 : division of var2 and var3
#if var1 ==4 : subtraction of var2 and var3

# Input for the first number
var1 = int(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
# Input for the second number
var2 = float(input("Enter the second number: "))

var3 = 0

if operator == '+':
    var3 = var1 + var2
    print("var1 + var2 = var3")
else:
    if operator == '-':
        var3 = var1 - var2
        print("var1 - var2 = var3")
    else:
        if operator == '*':
            var3 = var1 * var2
            print("var1 * var2 = var3")
        else:
            if operator == '/':
                if var2 == 0:
                    print("Division by zero.")
                else:
                    var3 = var1 / var2
                    print(f"var1 / var2 = var3")
            else:
                print("Invalid operator")

"""

# Python program without nested if
# var1 = take value for action
# var2 = take value for operation
# var3 = take value for operation

# if var1 ==1 : addition of var2 and var3
# if var1 ==2 : multiplication of var2 and var3
# if var1 ==3 : division of var2 and var3
# if var1 ==4 : subtraction of var2 and var3

"""
# Input for the first number
operator = input("Enter operator(+, -, *, /, //): ")
var2 = int(input("Enter the first number: "))
var3 = int(input("Enter the second number: "))

if operator == "+":
    result = var2 + var3
    print("add :", result)

elif operator == "-":
    result = var2 - var3
    print("sub :", result)

elif operator == "*":
    result = var2 * var3
    print("mul :", result)

elif operator == "/":
    result = var2 / var3
    print("div :", result)

elif operator == "//":
    result = var2 // var3
    print("div :", result)

else:
    print("Invalid choice")

"""
"""
# with nested
var1 = int(input("Enter the action: "))
var2 = int(input("Enter the first number: "))
var3 = int(input("Enter the second number: "))

if var1 == 1:
    result = var2 + var3
    print("add :", result)
else:
    if var1 == 2:
        result = var2 - var3
        print("sub :", result)

    else:
        if var1 == 3:
        result = var2 * var3
        print("add :", result)

    else:
        if var1 == 4:
                result = var2/var3
                print("div :", result)

else:
    print("Invalid action")

"""

# 1. write a python program if given number is :
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

"""
num1 = int(input("Enter the number: "))

if num1%2 == 0:
    print("square of the number is :", num1**2)

elif num1%3 == 0:
    print("cube of the number is :", num1**3)

elif num1%7 == 0:
    print("squares of squares of the number is :", num1**4)

else:
    print("The number is not divisible by 2,3 and 7")

"""
"""
# 1). Python program to check given number is divided by 3 or not.
num1 = int(input("Enter the number: "))

if num1%3 == 0:
    print("Yes the number is divisible be 3")

else:
    print("No the number is not divisible be 3")
"""
"""
# 2). If else program to get all the numbers divided by 3 from 1 to 30.
for i in range(1, 31):
#    print(i)

    if i%3 == 0:
        print(i, end=" ")
"""
# 3). If else program to assign grades as per total marks.
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
"""
mark = int(input("Enter the marks :"))

if mark > 100:
    print("Enter valid marks")
elif 40 < mark <= 50:
    print("Passed with grade C")
elif 50< mark <= 60:
    print("Passed with grade B")
elif 60 < mark <= 70:
    print("Passed with grade A")
elif 70 < mark <= 80:
    print("Passed with grade A+")
elif 80 < mark <= 90:
    print("Passed with grade A++")
elif 90 < mark <= 100:
    print("Passed with grade Excellent")
elif mark > 100:
    print("Enter the valid marks")
else:
    print("Failed")
"""
"""
# 7). Python program to check given number is odd or even.
num1 = int(input("Enter number :"))

if num1%2 == 0:
    print("This is a prime number")

else:
    print("This is not a prime number")
"""

#  write a python program to check given is available in the list
# in operator
list1 = [8, 6, 7, 3, 4, 2, 1, 3, 0]
num1 = 7

if num1 in list1:
    print("num1 is available in the list1")

else:
    print("Not available")







