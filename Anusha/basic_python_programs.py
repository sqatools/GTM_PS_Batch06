# 2 (a-b)^2 = a^2 + b^2 - 2ab
print("-"*50)
a=100
b=200
lhs=(a-b)**2
print("lhs value:",lhs)
rhs=a**2 + b**2 -2*a*b
print("rhs value:",rhs)

# 3. (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)
print("-"*50)
a=50
b=60
c=90
lhs=(a+b+c)**2
print("lhs value:",lhs)
rhs=a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)
print("rhs value :",rhs)


# 4 area of circle
print("-"*50)
#  PI*R^2
PI = 3.14
R = 5
print ("area of the circle", PI * (R**2))

#5.  Simple Interest calculation
# si = (P*R*T)/100
# P = principle amount
# R = Rate of interest
# T = Time

print("-"*50)
p=5
r=8
t=10
print("simple interest:",(p*r*t)/100)
print("-"*50)

# 6. compound interest calculation
# CI=  ((P*(1+i)^n) - P)
# P = principle amount
# i = interest rate
# n = time period
p=10
i=20
n=30
print("compound interest:",(p*(1+i)**n) -p)

