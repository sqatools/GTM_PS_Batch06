# (a-b)^2 = a^2 + b^2 -2ab
a = 20
b = 3
LHS = (a-b)**2
print("LHS output: ", LHS)
RHS = a**2 + b**2 - 2*(a*b)
print("RHS output: ", RHS)

# (a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab+bc+ca)
a = 4
b = 5
c = 3
LHS = (a+b+c)**2
print("LHS output: ", LHS)
RHS = a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)
print("RHS output: ", RHS)

# Area
pi = 3.14
r = 4
Area = pi*(r**2)
print("Area output: ", Area)

# Simple Interest
p = 1000
r = 4
t = 2
si = (p*r*t)/100
print("Simple Interest is: ", si)

# Compound Interest
p = 1000
i = 4
n = 2
ci = (p*((1+i)**n) - p)
print("Compound Interest: ", ci)
