#2. (a-b)^2 = a^2+b^2-2ab

a = 10
b = 5
LHS = (a-b)**2
print("LHS value:",LHS)
RHS = a**2 + b**2 - 2*(a*b)
print("RHS value:",RHS)
print("checking both values", LHS == RHS)

#3. (a+b+c)^2=a^2+b^2+c^2+2(ab+bc+ca)

a = 2
b = 4
c = 6
LHS = (a+b+c)**2
print("LHS value:",LHS)
RHS = a**2 + b**2 + c**2 + 2*(a*b+b*c+c*a)
print("RHS value:",RHS)


# 4 area of circle
#  PI*R^2
PI = 3.14
R = 5
print ("area of the circle", PI * (R**2))


#5.  Simple Interest calculation

# si = (P*R*T)/100
# P = principle amount
# R = Rate of interest
# T = Time
P = 100
R = 5
T = 6
print ("Simple Interest calculation", (P*R*T)/100 )


# 6. compound interest calculation
# CI=  ((P*(1+i)^n) - P)
# P = principle amount
# i = interest rate
# n = time period

P = 200
i = 4
n = 6
print ("Compound Interest calculation", (P*(1+i)**n) - P )




