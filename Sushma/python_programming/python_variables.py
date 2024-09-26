# VARIABLES

a=10
print(a)
print(id(a)) # memory address

b=10
print(b)
print(id(b))  # memory address  is same for both a & b because a & b values are same,
              # to save the memory it is storing in same memory.

c=20
print(c)
print(id(c)) # c value is different  so it is storing in diff memory

#----------------------------------------------------------------------------
print('*'*50) # to separate the line this print function is used to repeat the * value 50 times


#Assign one value to three different variables
a=b=c=10
print("value of a:",a,id(a))
print("value of b:",b,id(b))
print("value of c:",a,id(c))

print('*'*50)

#Assign 3 different variables 3 different values
x,y,z=10,20,30
print("value of x:",x,id(x))
print("value of y:",y,id(y))
print("value of z:",z,id(z))
#---------------------------------------------------------------------------------------
print('*'*50)

#RULE TO DEFINE A VARIABLE
#1.there should not be space in variable name
#a b =50 #invalid

a_b=50  # valid a_b is taken as one variable
print(a_b)

x_y_z=100  #valid x_y_z is taken as one variable
print(x_y_z)
print(id(x_y_z))

print('*'*50)
#2.special charcter are not allowed in variable name

#email_$_id="sushma123@gmail.com" # @#$%^&* - special chacters are not allowed

email_id="sushma123@gmail.com"
print(email_id)

print('*'*50)

#3.can not contain number as prefix in the variable name

#1var="sushma" # invalid
#print(1var)

var_1="sushma" # valid
print(var_1)

print('*'*50)

#4.variable names are case sensitive
Name = 'Sushma'
name = "ravi"
NAme = 'sanvi'
nAMe= 'ojaswi'
print(Name)
print(name)
print(NAme)
print(nAMe)
#-----------------------------------------------------------------

print('*'*50)

#OPERATORS
"""
+ --->Addition
- --->Subtraction
* --->Multiplication
/ --->Division with single slash (exact value it will give like 5/2 =2.5)
// --->Division with doble slash (round figer value it will give 5//2=2)
% --->Remainder operator 
** --->Power operator
== --->Equal to operator
"""

#ADDITION OPERATOR
#method 1:
a=20
b=50
print("after adding", a+b) # directly printing the added value, we are not storing any where

#method 2:
a=600
b=800
c=300
d=1000000
total=a+b+c+d # storing the added value to an total
print("after adding",total) # printing the total value

#-----------------------------------------------------
print('#'*50)

#SUBTRACTION OPERATOR

#method 1:

x=10000
y=600
print("after subtraction",x-y)

#method 2:
x=100000000
y=45
z=78
t=90000
total_sub=x-y-z-t
print("after subtraction",total_sub)

#---------------------------------------

print("#"*50)
#MULTIPLICATION OPERATOR
# method 1:
a=100
b=378
print("after multiplication",a*b)

#method 2:
x=34
y=78
z=23
t=100
total_mul=x*y*z*t
print("after mul",total_mul)
print((id(total_mul))) # memory address  where mul function is storing

#------------------------------------------------
print("*"*50)

#DIVISION OPERATOR
#method 1:
a=80
b=3
print("after division",a/b) # division with single slash gives accurate value
print("after division",a//b) # division with double slash gives exact value

# method 2:
a=80
b=3
c=2
d=4
total_div=a/b/c/d # division with single slash gives accurate value
total_div1=a//b//c//d  # division with double slash gives exact value
print("after division",total_div)
print("after division",total_div1)
#---------------------------------------------------
print("#",30)

#POWER OPERATOR

print("square of 2 :",2**2)  #2*2=4
print("square of 4 :",4**4) # 4*4*4*4=256
print("square of 2:",2**5) #2*2*2*2*2=32
print("square of 6 :",6**3) #6*6*6=216

#############################
print("#"*30)
a=40
b=20
lhs=(a-b)**2
print("lhs output:",lhs)

rhs=a**2+b**2-2*a*b
print("rhs output:",rhs)

print("#"*30)
a=10
b=5
c=2
LHS=(a+b+c)**2
print(LHS)

RHS = a**2+b**2+2*(a*b+b*c+c*a)
print(RHS)

print("#"*30)

pi=3.13
r=5
x=pi*r
print(x)

print("#"*30)

#si=(p*r*t)/100
p=10000
r=2
t=1
print(p*r*t)

print("#"*30)

CI=((p*(1+i)**n)-p)
p=10000
i=3
n=2
CI=((p*(1+i)**n)-p)
print(CI)

"""num1=10
num2=20
print(num1+num2)

num1=20
num2=15
print(num1-num2)

num1=5
num2=10
print(num1*num2)"""




