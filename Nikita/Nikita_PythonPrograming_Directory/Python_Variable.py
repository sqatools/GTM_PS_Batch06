#2. (a-b)^2 = a^2 - b^2 - 2ab
a = 100
b = 50
LHS = (a - b)**2
print("LHS output : ", LHS)

RHS = a**2+b**2 - 2*a*b
print("RHS output : ", RHS)

# 3. (a + b + c)^2 =a^2 + b^2 + c^2 + 2(ab + bc + ca)
a = 200
b = 800
c = 1000
LHS = (a + b + c)**2
print("LHS output : ", LHS)

RHS = a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)
print("RHS output : ", RHS)

# 4. area of circle
# area = PI*R^2
PI = 3.13
R = 5
print(PI*R**2)

#5. simple interest calacuatipn
# SI (P*R*T)/100
P = 100000
R = 10
T = 3
SI = (P*R*T)/100
print(SI)

#6.Compound interest calculation
# CI = ((P*(1+i)^n) - P)
P = 100000
i = 5
n = 5
CI = ((P*(1+i)*n) - P)
print(CI)



