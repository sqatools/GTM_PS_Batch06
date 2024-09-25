import datetime
import math

# 4. area of circle
# area = PI*R*^2
PI = 3.13
R = 5
area_of_circle = PI*R**2

print("Area of Circle:", area_of_circle)

print("_"*50)
# 5. simple interest calculation
# si = (P*R*T)/100
P = 5500
R = 3
T = 2

si = (P*R*T)/100
print("Simple Interest:", si)

print("_"*50)
# 6. compound interest calculation
# CI = ((P*(1+i)^n) - P)

P = 4500
i = 0.01
n = 3

CI = ((P*(1+i)**n) - P)
print("Compound Interest:", CI)

print("#"*100)
# Python basic program

# 1). Python Program to add two integer values.
a = 25.5
b = 30.10
c = a + b
print("1. Adding two integer :", c)
# 1. Adding two integer : 55.6
print("_"*40)

# 2). Python Program to subtract two integer values.

p = 57656734
q = 85672345
r = p - q
print("2. Subtracting two integer :", r)
# 2. Subtracting two integer : -28015611
print("_"*40)

# 3). Python program to multiply two numbers.
a = 57
b = 49
c = a * b
print("3. Multiply two integer :", c)
# 3. Multiply two integer : 2793
print("_"*40)

# 4). Python program to repeat a given string 5 times.
name = "Pushpa"
print("Repeat given string 5 times :", name*5)
print("4. Repeat given string 5 times :", "Pushpa"*5)  # can this be done???

# Repeat given string 5 times : PushpaPushpaPushpaPushpaPushpa
# 4. Repeat given string 5 times : PushpaPushpaPushpaPushpaPushpa
print("_"*40)

# 5). Python program to get the Average of given numbers.
# Formula: sum of all the number/ total number
# Input:
# a = 40
# b = 50
# c = 30

average = (a+b+c)/3
print("5. Average of given numbers :", average)
# 5. Average of given numbers : 966.3333333333334
print("_"*40)

# 6). Python program to get the median of given numbers.
# Formula : (n+1)/2
# n = Number of values
# Input : [45, 60, 61, 66, 70, 77, 80]

n = [45, 60, 61, 66, 70, 77, 80]
length = (len(n))/2

print("6. Median :", n[int(length)])
# 6. Median : 66

print("_"*40)
# 7). Python program to print the square and cube of a given number.
# Input :
# num1 = 9
# Output :
# Square = 81
# Cube =   729
n = 7
print("7. Square :", n**2)
print("7. Cube :", n**3)
# Square : 49
# Cube : 343
print("_"*40)
# 7. Square : 49
# 7. Cube : 343

# 8). Python program to interchange values between variables.
a = 200
b = 400

a, b = b, a
print("8. a :", a)
print("8. b :", b)
# 8. a : 400
# 8. b : 200
print("_"*40)

# 9). Python program to solve this Pythagorous theorem.
# Theorem : (a2 + b2 = c2)
a = 25
b = 40
print(a**2+b**2)
# c = a**2+b**2
print("9. Pythagorous theorem answer :", math.sqrt(c))
# 9. Pythagorous theorem answer : 52.848841046895245
print("_"*40)


# 10). Python program to solve the given math formula.
# Formula : (a + b)2 = a^2 + b^2 + 2ab
a = 9
b = 35
c = (a + b)**2
d = a**2 + b**2 + 2*a*b
print(c)
print(d)
print("10. Solution = c is equal to d:", c == d)
# ________________________________________
# 1936
# 1936
# 10. Solution = c is equal to d: True
print("_"*40)

# 11). Python program to solve the given math formula.
# Formula : (a – b)2 = a^2 + b^2 – 2ab
a = 78.46
b = 49.98
c = (a - b)**2
d = a**2 + b**2 - 2*a*b
print(c)
print(d)
print("11. Solution = c is equal to d:", c == d)
# 811.1103999999998
# 811.1103999999987
# 11. Solution = c is equal to d: False
print("_"*40)

# 12). Python program to solve the given math formula.
# Formula : a2 – b2 = (a-b)(a+b)
a = 9
b = 3
c = a**2 - b**2
d = (a-b)*(a+b)
print("12. Solution = c is equal to d:", c == d)
# 12. Solution = c is equal to d: True
print("_"*40)

# 13). Python program to solve the given math formula.
# Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a = 78
b = 97
c = (a+b)**3
d = a**3 + 3*a*b*(a+b) + b**3
print("c:", c)
print("d:", d)
print("13. Solution = c is equal to d:", c == d)
# c: 5359375
# d: 5359375
# 13. Solution = c is equal to d: True
print("_"*40)

# 14). Python program to solve the given math formula.
# Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
a = 9
b = 8
c = (a-b)**3
d = a**3 - 3*a**2*b + 3*a*b**2 - b**3
print("c:", c)
print("d:", d)
print("14. Solution = c is equal to d:", c == d)
# c: 1
# d: 1
# 14. Solution = c is equal to d: True
print("_"*40)

# 15). Python program to calculate the area of the square.
# Formula : area = a*a a2
a = 5
b = a**2
print("15. Area of square :", b)
# side = int(input("5:"))
# print("Area of sqaure: ", side**2)
# 15. Area : 25
print("_"*40)

# 16). Python program to calculate the area of a circle.
# Formula = PI*r*r
# area = PI*R*^2
PI = 3.13
R = 5
area_of_circle = PI*R**2
print("16. Area of Circle:", area_of_circle)
print("_"*40)

# 17). Python program to calculate the area of a cube.
# Formula = 6*a*a
a = 6
print("17. Area of cube: ", 6*a*a)
# 17. Area of cube:  216
print("_"*40)

# side = int(input("Enter side of a cube: "))
side = 6
area = 6*side*side
print("Area of cube: ", area)
print("_"*40)

# 18). Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
PI = 3.14
# r = int(input("Enter radius of cylinder: "))
# h = int(input("Enter height of cylinder: "))
# area = 2*3.14*r*h+2*3.14*r*r
# print("18. Area of cylinder: ", area)
# Enter radius of cylinder: 5
# Enter height of cylinder: 6
# 18. Area of cylinder:  345.4
print("_"*40)

print("# 19. not done "*5)
# 19. not done # 19. not done # 19. not done # 19. not done # 19. not done
# 19). Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

# 20). Python program to calculate simple interest.
# Formula = P+(P/r)*t
# P = Principle Amount
# r = Anual interest rate
# t = time
# si = (P*R*T)/100
P = 5500
R = 3
T = 2

si = (P*R*T)/100
print("20. Simple Interest:", si)
# 20. Simple Interest: 330.0
print("_"*50)

# 21). Python program to print the current date in the given format
# Output: 2023 Jan 05
# Note: Use the DateTime library
date = datetime.datetime.now()
print("21. current date and year: ", date.strftime(" %Y %b %d "))
# 21. current date and year:   2024 Sep 25
print("_"*50)

# 22). Python program to calculate days between 2 dates.
# Input date : (2023, 1, 5) (2023, 1, 22)
# Output: 17 days
from datetime import date

date_1 = date(2024, 9, 25)
date_2 = date(2024, 9, 30)

result = (date_2 - date_1).days
print("Number of Days between the given Dates are: ", result, "days")
# Number of Days between the given Dates are:  5 days
print("_"*50)

# 27).  Python program to calculate compound interest.
# CI = ((P*(1+i)^n) - P)

P = 4500
i = 0.01
n = 3

CI = ((P*(1+i)**n) - P)
print("27. Compound Interest:", CI)
# 27. Compound Interest: 136.35450000000037
print("_"*50)











