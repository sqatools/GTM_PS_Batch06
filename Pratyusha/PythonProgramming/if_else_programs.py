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

# 6. If else program to get all the numbers divided by 3 from 1 to 30
"""for i in range(1, 31):
    if i%3 == 0:
        print(i, end=' ')"""

# 7. Python program to check the given number divided by 3 and 5
"""num = int(input("Enter a number to check it is divided by 3 & 5: "))
if num % 3 == 0 and num % 5 == 0:
    print("Given number is divided by both 3 & 5")
else:
    print("Given number is not divided by both 3 & 5")"""

# 8. Python program to print the square of the number if it is divided by 11
"""num1 = int(input("Enter a number to get square: "))
if num1%11 == 0:
    print(num1**2)
else:
    print("Given number not divisible by 11")"""

# 9. Python program to check given number is a prime number or not
"""# input from user
num = int(input("Enter a number to check prime: "))
# make prime as true initially
prime = True
# if number is divisible by any of the numbers starting from 2 to given number, prime become false
for i in range(2, num):
    if num%i == 0:
        prime = False
if prime:
    print("Given number is Prime number")
else:
    print("Given number is not a Prime number")"""

# 10. Python program to check given number is odd or even
"""num = int(input("Enter a number to check it is odd or even: "))
if num%2 == 0:
    print("Even number")
else:
    print("Odd number")"""

# 11. Python program to check a given number is part of the Fibonacci series from 1 to 10
"""a = 0
b = 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a+b
print()"""
"""fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
num = int(input("Enter number to check in fibonacci series: "))
if num in fib:
    print("Number is a part of series")
else:
    print("Number is not a part of series")"""

# 12. Python program to check authentication with the given username and password
"""org_username = "Pratyusha"
org_password = "python@123"
username = input("Enter username: ")
password = input("Enter password: ")
if org_username == username and org_password == password:
    print("Successfully logged in")
else:
    print("Incorrect username or password")"""

# 13. Python program to validate user_id in the list of user_ids
"""user_ids = ['Rahul', 'Pratyusha', 'Kevin', 'Bob']
user_id = input("Enter user id to validate: ")
if user_id in user_ids:
    print("Valid user id")
else:
    print("Invalid user id")"""

# 14. Python program to print a square or cube if the given number is divided by 2 or 3 respectively
"""num = int(input("Enter a number: "))
if num%2 == 0:
    print("Square: ", num**2)
elif num%3 == 0:
    print("Cube: ", num**3)
else:
    print("Number is neither divisible by 2 nor divisible by 3")"""

# 15. Python program to determine whether a given number is available in the list of numbers or not
"""list1 = [2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 0]
num = int(input("Enter a number to verify it in list: "))
if num in list1:
    print("Available")
else:
    print("Not available")"""

# 16. Python program to find the largest number among three numbers
"""n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
if n1 > n2:
    if n1 > n3:
        print(str(n1) + " " + "is the greatest number")
    else:
        print(str(n3) + " " + "is the greatest number")
else:
    if n2 > n3:
        print(str(n2) + " " + "is the greatest number")
    else:
        print(str(n3) + " " + "is the greatest number")"""

# 17. Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

"""str3 = "Indian is Batsman Virat best"
first = str3[-10:-5:1]
second = str3[7:9]
third = str3[0:6]
fourth = str3[-4:]
fifth = str3[10:17]
print("{} {} {} {} {}".format(first, second, third, fourth, fifth))"""

#q1. str_a = "My name is John" -> "ny name is JohM"
#q2. str_b = "India is best country" -> "IIndia iis bbest ccountry"

