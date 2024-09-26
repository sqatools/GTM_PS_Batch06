q=100
w=50
print ("addition is:", q+w)

print ("substraction is:", q-w)

print("division single slash is:", q/w)

print("division double slash is:", q//w)

print("cube of 6 is:", 6**3)

print("Average is:", (q+w)/2)

print("_" *50)

a=10
b=5
c=8

LHS = (a-b)**2
print("LHS value:", LHS)

RHS = a**2 +b**2 -2*a*b
print("RHS Value is:", RHS)

print("_" *50)

LHS1 = (a + b + c)**2
print("LHS value is:", LHS1)

print("_" *50)

RHS1 = (a**2 + b**2 + c**2 + 2*a*b + 2*b*c + 2*c*a)
print("RHS value is:", RHS1)

print("_" *50)

PI=3.14
r=5
a= PI*r**2
print("area of circle:", a)

print("_" *50)

l=10
Area = l**2
print("Area of square:", Area)

print("_" *50)

P=1000
R=5
T=10
SI = P+(P/R)*T
print("Simple Intrest is:", SI)

print("_" *50)

p=1000
r=8
CI= (p*(1+r/100)**2)
print("Compound Intrest is:", CI)

print("_" *50)

print("Area")
num1 = int(input("Please insert Number:"))
num2 = int(input("Please insert Number:"))
num3 = int(input("Please insert Number:"))
Area = num1*num2*num3
print("Area of rectangle:", Area)

print("_" *50)

print("Average")
num1 = int(input("Please insert Number:"))
num2 = int(input("Please insert Number:"))
num3 = int(input("Please insert Number:"))
Average = (num1+num2+num3)/3
print("Average of Numbers:", Average)

print("_" *50)

print("Volume of Sphere")
PI=3.14
r=int(input("Please insert Radius:"))
Formula = 4/3*PI*r**2
print("Volume of sphere:", Formula)

print("_" *50)

print("Square Root")
import math
num1 = int(input("Enter the Number:"))
print(math.sqrt(num1))

print("_" *50)

print("Reverse")
num= int(input("Enter the Number:"))
reverse = str(num)
print("Reverse:", reverse[::-1])