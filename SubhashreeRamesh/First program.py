"""
a=10
b=20
# (a-b)2=a2+b2-2ab

RHS=(a-b)**2
print("RHS value",RHS)
LHS=a**2+b**2-2*a*b
print("LHS value",LHS)
print("#"*50)
#3.(a+b+c)2=a2+b2+c2+2(ab+bc+ca)
a=20
b=30
c=50
LHS=(a+b+c)**2
#RHS=a**2 + b**2 + c**2 + 2(a*b +b*c +c*a )
print("LHS value",LHS)
print("RHS value",RHS)
print("#"*50)
#4.area of circle
#are=PI*Rpower2
PI=3.13
R=5
are=PI*R**2
print("value of are",are)
print("#"*50)
#5.simple interest calculation

#p=principal amount
#R=Rate of interest
#T=TimeoutError
P = 5
R = 2
T = 4
si=(P*R*T)/100
print("value of si",si)
print("#"*50)

#6.compond interest calculation
#CI=((P*(1+i)power n)-P)
p = 100
i = 50
n = 25
CI=((P*(1+i)** n)-P)
print("value of CI",CI)

"""
