# 1. write a python program if given number is :
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number
"""num1 = float(input("Enter a number: "))
if num1%2 == 0:
    print("Square of the number: ", num1**2)
elif num1%3 == 0:
    print("Cube of the number: ", num1**3)
elif num1%7 == 0:
    print("Double square of the number", num1**4)
else:
    print("Number is not divisible by 2,3 and 7")"""

# 2. Create a calculator
"""num1 = float(input("Enter first number: "))
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
    print("Invalid operator")"""

# 3. Interview process with nested if condition
"""round_1 = input("Enter a result of 1st round like PASS/FAIL: ")
round_2 = input("Enter a result of 2nd round like PASS/FAIL: ")
round_3 = input("Enter a result of 3rd round like PASS/FAIL: ")
if round_1 == 'PASS':
    print("Congratulations, moved to 2nd round")
    if round_2 == 'PASS':
        print("Congratulations, selected for final round")
        if round_3 == 'PASS':
            print("Congratulations, you are selected in interview process")
        else:
            print("Welcome on board")
    else:
        print("Please brush up your technical skills")
else:
    print("Sorry try next time")"""

# 4. Python program to check given number is divided by 3 or not
"""num1 = int(input("Enter an integer: "))
if num1%3 == 0:
    print("Given number is divisible by 3")
else:
    print("Given number is not divisible by 3")"""

# 5. If else program to assign grades as per total marks
# marks > 40: Fail
# marks 40 – 50: grade C
# marks 50 – 60: grade B
# marks 60 – 70: grade A
# marks 70 – 80: grade A+
# marks 80 – 90: grade A++
# marks 90 – 100: grade Excellent
# marks > 100: Invalid marks
"""marks = int(input("Enter your marks: "))
if marks < 40:
    print("Failed")
elif marks >=40 and marks <= 50:
    print("Grade 'C'")
elif marks > 50 and marks <= 60:
    print("Grade 'B'")
elif marks > 60 and marks <= 70:
    print("Grade 'A'")
elif marks > 70 and marks <= 80:
    print("Grade 'A+'")
elif marks > 80 and marks <= 90:
    print("Grade 'A++'")
elif marks > 90 and marks <= 100:
    print("Grade 'Excellent'")
elif marks > 100:
    print("Invalid marks")"""
