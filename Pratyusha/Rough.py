"""# Palindrome
# 343 - input
# 343 - reversed
num = input("Enter a number: ")
rev = str(num)
rev_num = rev[::-1]
if num == rev_num:
    print("Entered number is a palindrome")
else:
    print("Entered number is not a palindrome")

# Python program to check sum of n natural no.s
n = int(input("Enter a number to get the result of sum of natural no.s: "))
s = (n*(n+1))/2
print("Sum of n natural numbers: ", s)

Python program to calculate the volume of a sphere.
Formula = (4/3*pi*r^3)
pi = 3.14
r = 4
vol_of_sphere = 4/3*pi*r**3
print("volume of Sphere: ", round(vol_of_sphere)"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter your choice of operator: ")
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print("Invalid operation")
