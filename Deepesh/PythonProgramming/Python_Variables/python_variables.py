"""
Notes and Practice

https://sqatools.in/python-variables-tutorials/

https://sqatools.in/python-basic-programs/
"""

a = 10
print(a)  # print function will the value of variable a

# id() function return the memory address of any variable
print(id(a))  # 140727433972440

# if two variables holding same value, then the memory address will be same.
b = 10
print(id(b))

# assign one value to three different variables

p = q = r = 50
print("value of p :", p, id(p))
print("value of q :", q, id(q))
print("value of r :", r, id(r))

# assign three different variables three different values
x, y, z = 30, 40, 50

print("value of x :", x, id(x))  # 30, 140727433973080
print("value of y :", y, id(y))  # 40, 140727433973400
print("value of z :", z, id(z))  # 50, 140727433973720

# Rule to define a variable
# 1. There should not be space in variable name
#  a b = 50 invald
# a_b = 50 valid
x_y_z = 500
user_name_value = 'john123'
print(user_name_value)
print(x_y_z)

# 2. special characters are not in the variable name

# email_&_id = 'testuser@gmail.com' # invalid
email_id = 'testuser@gmail.com'
print(email_id)  # testuser@gmail.com

# 3. Can not contain number as prefix in the variable name

var1_Value34567 = 500  # valid
# 1var_value = 600 # invalid

# 4. Variable names are case-sensitive

Name = 'Rahul'
NAME = 'INDIA'
name = 'Mohit'
nAme = 'Shresth'

print(Name)
print(NAME)
print(name)
print(nAme)

#######################################
"""
Math operators
+ : plus
- : minus
* : multiplication
/ : division with single slash
// : division with double slash
% : Remainder operator
** : power operator
== : Equal to operator
!= : not equal to operator
"""

# This will repeat the # value 50 times to draw a line
print("#" * 50)

# Addition of values
var1 = 500
var2 = 600
print("addition of value :", var1 + var2)
var3 = var1 + var2
print("addition with third variable :", var3)

print("#" * 50)
### multiplication of values ###

var_p = 50
var_q = 3
print("multiplication :", var_p * var_q)

multiply = var_p * var_q
print("multiplication value :", multiply)

print("#" * 50)
### subtraction of values ###
var_s = 100
var_t = 50

print("subtraction output :", var_s - var_t) # 50


## division of values ####

var_k = 600
var_l = 11
# division with single slash
print("division output :", var_k/var_l) # 54.54545454545455

# division with double slash
print("division output :", var_k//var_l) # 54

var_o = 45
var_6 = 11
print(var_o/var_6) # 4.090909090909091
print(var_o//var_6) # 4


print("_"*50)
# power operator: **

print("square of 2 :", 2**2) # 2*2
print("cube of 4 :", 4**3) # 4*4*4 : 64
print("cube of 5 :", 5**3) # 5*5*5 : 125

###################################
print("_"*50)
# remainder operator %

var11 = 10
var2 = 4

print("remainder value :", var11%var2) # 2

print(11%4) # 3

num1 = 30
print("check for even :", num1%2 == 0) # even True

print("check for odd :", 13%2 != 0) # odd True


print("_"*50)
### equal to operator ####

n1 = 40
n2 = 50
n3 = 40
print(n1 == n2) # False
print(n1 == n3) # True

print("_"*40)
#########################################################
# 1. (a+b)^2  = a^2 + b^2 + 2ab
a = 40
b = 23
LHS = (a+b)**2
print("LSH output :", LHS)

RHS = a**2 + b**2 + 2*a*b
print("RHS output :", RHS)

print("_"*40)
# 2 (a-b)^2 = a^2 + b^2 - 2ab

# 3. (a + b + c)^2 = a^2 + b^2 + c^2 + 2(ab + bc + ca)

# 4. area od circle
# are = (PI)*(R**2)
PI = 3.13
R = 5

# 5.  simple interest calculation

# si = (P*R*T)/100
# P = principle amount
# R = Rate of interest
# T = Time

# 6. compound interest calculation
#
# CI=  ((P*(1+i)^n) - P)
# P = principle amount
# i = interest rate
# n = time period
