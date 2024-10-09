# #2. (a-b)^2 = a^2 - b^2 - 2ab
# from math import sqrt
#
# a = 100
# b = 50
# LHS = (a - b)**2
# print("LHS output : ", LHS)
#
# RHS = a**2+b**2 - 2*a*b
# print("RHS output : ", RHS)
#
# # 3. (a + b + c)^2 =a^2 + b^2 + c^2 + 2(ab + bc + ca)
# a = 200
# b = 800
# c = 1000
# LHS = (a + b + c)**2
# print("LHS output : ", LHS)
#
# RHS = a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)
# print("RHS output : ", RHS)
#
# # 4. area of circle
# # area = PI*R^2
# PI = 3.13
# R = 5
# print(PI*R**2)
#
# #5. simple interest calacuatipn
# # SI (P*R*T)/100
# P = 100000
# R = 10
# T = 3
# SI = (P*R*T)/100
# print(SI)
#
# #6.Compound interest calculation
# # CI = ((P*(1+i)^n) - P)
# P = 100000
# i = 5
# n = 5
# CI = ((P*(1+i)*n) - P)
# print(CI)
#
# # 7. Python Program to add two integer values.
# a = 50
# b = 60
# print(a + b)
#
# # 8.Python program to repeat a given string 5 times.
# name = 'Nikita'
#
# print(name*5)
#
# #9. 5). Python program to get the Average of given numbers.
# a = 40
# b = 50
# c = 30
# sum = (a+b+c)/3
# print(sum)
#
# """10.Python program to get the median of given numbers.
# Note: all the numbers should be arranged in ascending order
# Formula : (n+1)/2"""
#
# list1 = [1, 5, 7, 9, 33, 55, 80]
# list1.sort()
# a = (len(list1))/2
# print("Median: ",list1[int(a)])
#
# #8). Python program to interchange values between variables.
# a = 10
# b = 20
# a,b = b,a
# print(a,b)
#
# #9). Python program to solve this Pythagorous theorem.
# #Theorem : (a2 + b2 = c2)
# a = 40
# b = 40
#
# # var1 = sqrt(a**2 + b**2)
# print(var1)
#
# #17). Python program to calculate the area of a cube.
# a = 6
# area = 6 * a ** 2
# print("Area of cube:", area)
#
# side = int(input("Enter side of a cube: "))
# area = 6*side*side
# print("Area of cube: ",area)

# import datetime
# current_date = datetime.datetime.now()
# print("current date:", current_date.strftime(" %Y %m %d"))

from datetime import datetime

# Get the current date
current_date = datetime.now()

# Print the current date
print("Current date:", current_date.strftime("%Y--%m--%d"))

