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

P=10
R=5
T=15
SI = P+(P/R)*T
print("Simple Intrest is:", SI)

print("_" *50)

p=10
r=80
CI= (p*(1+r/100)**2)
print("Compound Intrest is:", CI)

print("_" *50)

print("Area")
l= int(input("Enter the Number:"))
b= int(input("Enter the Number:"))
h= int(input("Enter the Number:"))

Area=l*b*h
print("Area of Rectangle:", Area)

print("_" *50)

print("Cylinder Area")
PI=3.14
r= int(input("Enter the Radius:"))
h= int(input("Enter the Height"))
Area = 2*PI*r*h + 2*PI*r**2
print("Area of Cylinder: ", Area)

print("_" *50)

print("Reverse")
num= int(input("Enter the Number"))
reverse =str(num)
print("Reverse Number is: ", reverse[::-1])

print("_" *50)

print("Calculate days between 2 dates")
from datetime import date
date1= date(2024, 9, 27)
date2= date(2024, 12, 31)
result= (date2-date1).days
print("Number od days: ", result, "days")


print("******************************** End of the Exercise *****************************")