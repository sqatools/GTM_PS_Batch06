##############################
print("_"*50)
# Remainder operator: %

var1= 10
var2 = 3
remainder= var1 % var2
print("remainder is :", remainder)

# check for even and odd:
num1 = 10 #even
print("check for even:" , num1%2 == 0)

num2 = 30  # even
print("check for odd:", num2%2 != 0)

num3 = 29  # even
print("check for odd:", num3%2 != 0)

print("_"*50
    )


# equal to operator: ==

n1= 10
n2=20
n3= 10
print(n1==n2) # false
print(n1==n3) #true

#######################################
print("_"*50
    )
#1. (a+b)^2 = a^2 + b^2 + 2ab

a = 10
b = 20

LHS = (a+b)**2
RHS = a**2 + b**2 + 2*a*b
print ("LHS value:" , LHS)
print ("RHS value:" , RHS)

print("*"*50)

#2. (a-b)^2 = a^2 + b^2 - 2ab

LHS = (a-b)**2
RHS = a**2 + b**2 - 2*a*b
print("LHS value:", LHS)
print("RHS value :", RHS)

c= 25
#3. (a+b+c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)

LHS = (a+b+c)**2
RHS = a**2 + b**2 + c**2 + 2*(a*b + b*c + c*a)

print("LHS value is :", LHS)
print("RHS value is :", RHS)

#4. Area of circle:  area = PI*r^2

PI = 3.14
r = 6
area  = PI * r**2
print ("area of circle is:" , area)

#5. Simple interest calculation:
# si = (p*r*t)/100

p = 10000
r = 2
t = 6

print("interest is:", (p*r*t)/100)

#6. compount interest :
# ci = ((p*(1+i)^n) - p)

p = 10000
i = 2
n = 6
ci = ((p*((1+i)**n)) - p)
print("compond interest is:" , ci)








