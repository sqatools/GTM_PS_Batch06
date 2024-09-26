# Python Program to add two integer values
a = 4.5
b = 6
add = a + b
print("Addition output: ", add)

# Python Program to subtract two integer values
x = 5.5
y = 6
sub = a - b
print("Subtraction output: ", sub)

# Python program to multiply two numbers
a = 5
b = 8.4
mul = a * b
print("Multiplication output: ", mul)

# Python program to repeat a given string 5 times
Str = "SQATools"
print("Sting output: ", Str * 5)

# Python program to get the Average of given numbers
a = 40
b = 50
c = 30
avg = (a + b + c) / 3
print("Average output: ", avg)

# Python program to print the square and cube of a given number
num1 = 9
square = num1 ** 2
cube = num1 **3
print("Square of number: ", square)
print("Cube of number: ", cube)

# Python program to interchange values between variables
a = 10
b = 20
a, b = b, a
print("Value of a: ", a)
print("Value of b: ", b)

# Python program to solve the given math formula - (a + b)2 = a^2 + b^2 + 2ab
a = 3
b = 5
LHS = (a + b)**2
RHS = a**2 + b**2 + 2*a*b
print("LHS output: ", LHS)
print("RHS output: ", RHS)

# Python program to solve the given math formula - (a-b)^2 = a^2 + b^2 -2ab
a = 20
b = 3
LHS = (a-b)**2
print("LHS output: ", LHS)
RHS = a**2 + b**2 - 2*(a*b)
print("RHS output: ", RHS)

# Python program to solve the given math formula - a2 – b2 = (a-b)(a+b)
a = 4
b = 3
LHS = a**2 - b**2
RHS = (a - b)*(a + b)
print("LHS output: ", LHS)
print("RHS output: ", RHS)

#  Python program to solve the given math formula - (a + b)3 = a3 + 3ab(a+b) + b3
a = 3
b = 4
LHS = (a + b)**3
RHS = a**3 + 3*a*b*(a + b) + b**3
print("LHS output: ", LHS)
print("RHS output: ", RHS)

# Python program to solve the given math formula - (a – b)3 = a3 – 3a2b + 3ab2 – b3
a = 4
b = 2
LHS = (a - b)**3
RHS = a**3 - 3*a**2*b + 3*a*b**2 - b**3
print("LHS = ", LHS)
print("RHS = ", RHS)

# Python program to calculate the area of the square - area = a*a
a = 6
area_of_square = a*a
print("Area of square: ", area_of_square)

# Python program to calculate the area of a circle - area = pi*r2
pi = 3.14
r = 4
area_of_circle = pi*r**2
print("Area of circle: ", area_of_circle)

# Python program to calculate the area of a cube - 6*a2
a = 4
area_of_cube = 6*a**2
print("Area of cube: ", area_of_cube)

# Python program to calculate the area of the cylinder - 2pirh
pi = 3.14
r = 3
h = 4
area_of_cylinder = 2*pi*r*h
print("Area of cylinder: ", area_of_cylinder)

# Python program to calculate simple interest
p = 1000
r = 4
t = 2
si = (p*r*t)/100
print("Simple Interest is: ", si)

# Python program to reverse a given number
num = input("Enter the number to reverse: ")
reverse_str = str(num)
print("Reversed number: ", reverse_str[-1::-1])

# Python program to check given number is palindrome or not
num = input("Enter a number to check palindrome: ")
rev = str(num)
rev_num = rev[::-1]
if num == rev_num:
    print("Entered number is a palindrome")
else:
    print("Entered number is not a palindrome")

# Python program to calculate compound interest.
p = 1000
i = 4
n = 2
ci = (p*((1+i)**n) - p)
print("Compound Interest: ", ci)

# Python program to check sum of n natural no.s
n = int(input("Enter a number to get the result of sum of natural no.s: "))
s = (n*(n+1))/2
print("Sum of n natural numbers: ", s)

# Python program to calculate the volume of a sphere - (4/3*pi*r^3)
pi = 3.14
r = 4
vol_of_sphere = 4/3*pi*r**3
print("volume of Sphere: ", round(vol_of_sphere))

# Python program to perform mathematical operations on two numbers
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