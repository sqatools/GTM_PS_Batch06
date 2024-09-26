a = 10
print(a)

# id() function return the memory address of any variable
# if two variables holding same value, then the memory address will be same.
print(id(a)) # 140716298865368


# assign one value to three different  variable

p = q = r = 50

print("value of p :", p, id(p))
print("value of q :", q, id(q))
print("value of r :", r, id(r))


# assign three different variables to three different values
print("_"*50) # this is to draw lines
x, y, z = 30, 40, 50

print("value of x :", x, id(x))
print("value of y :", y, id(y))
print("value of z :", z, id(z))

# Rules to define a variable
# Rule 1. There should not be space a variable

# Rule 2. Special characters are not in the variable name

# Rule 3. Can not contain number as prefix in the variable name

# Rule 4. Variable names are case-sensitive


# September 24th
# 2. (a-b)^2 = (a^2) + b^2 -2ab
a=25
b=30

RHS = (a-b)**2
print("RHS value:", RHS)

LHS = (a**2) + (b**2) - 2*a*b
print("LHS value:", LHS)

print("_"*50)
# 3. (a+b+c)^2= a^2 + b^2 + C^2 + 2(ab + bc + ca)
a=5
b=9
c=8

RHS=(a+b+c)**2
print("RHS value:", RHS)

LHS = a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)
print("LHS value:", LHS)

print("If RHS equals LHS:", LHS == RHS)

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






