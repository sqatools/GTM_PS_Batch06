a = 10
print(a) # print function will the value of  variable

# id() function return the memory address  of any variable
print(id(a))

# if two variable holding same value, then the memory address will be same
b=10
print(id(b))

# assign one value to three different variable

P = q = r = 50
print("value of p:", P, id(P))
print("value of q:", q, id(q))
print("value of r:", r, id(r))
# assign three different variables three different values
x, y, z = 30,  40, 50

print("value of X:", x, id(x))
print("value of Y:", y, id(y))
print ("value of z:", z, id(z))

# Rules to define a variable
# 1. There should not be space in variable name
# a b = 50 invalid
# ab = 50 valid
x_y_z =500
User_name_value = "John123"
print(User_name_value)
print(x_y_z)
# 2.specials characters are not in  the variable  name
# email_&_id = 'testuser@gmail.com' #invalid
email_id = 'testuser@gmail.com'
print(email_id) # testuser@gamil.com
# 3. can not contain number as perfix in the variable name
var1_value3457 = 500 # valid
# 1var_value = 600 # invalid
# 4.variable  names are  case sensitive
Name = "Rahul"
nAme = "INDIA"
NAME = "mohit"
name = "Shree"

print(Name)
print(nAme)
print(NAME)
print(name)

# Addition of value
var1 = 500
var2 = 600
print("addition of value:", var1 + var2)
var3 = var1 + var2
print("addition with third variable:", var3)

# multiplication of values
var_p = 50
var_q = 3
print(" multiplication :", var_p*var_q)
multiply = var_p*var_q
print ("multiplication value:", multiply)

# subtraction of values##
var_s = 100
var_t = 40
print("subtraction output:", var_s - var_t)

# division with single slash
var_k = 600
var_l = 5
print("division output:", var_k/var_l)

# division with double slash
var_o = 45
var_l = 8
print("division output:", var_o//var_l)

# power operator
print("squre of 2:", 2**2)
print("cube of 4:", 4**3)
print("cube of 5:", 5**3)


# (a-b)^ 2 = a^2 + b^2 -2ab
a = 30
b = 10
LHS = (a-b)**2
print ("LHS output:", LHS)
RHS = a**2+b**2-2*(a*b)
print("RHS output:",RHS)

# (a+b+c)^2 = a^2 + b^2 + c^2 +2(ab + bc +ca)
a = 10
b = 5
c = 2
LHS = (a+b+c)**2
print("LHS output:", LHS)
RHS = a**2+b**2+2**2+2((a*b +b*c +c*a))
print("RHS output:", RHS)

# 4 area od circle
# are = PI*R^2
PI = 3.13
R = 5
LHS = PI*R**2
print("LHS output:", LHS)
<<<<<<< HEAD
# 5 simple interest calculation
#Si = (P * R * T)/100
P = 2000
R = 600
T = 3
RHS = (P*R*T)/100
print("RHS:", RHS)

# 6 compound interest calculation
# CI = (p*(1+i)^n-p)
# p = principal amount
# i = interest rate
# n = time period
P = 30
i = 5
n = 2
RHS = (P * (1+i) ^ n-P)
print("RHS:" , RHS)

# program to add two integers
a =5
b = 7
print(a+b)
# substract  with two integers
a =8
b =9
print(a-b)
#multiply number
a = 6
b = 8
print(a*b)
# program to repeat  a given  string 5 times
report = "Test"
print(report*5)
# Program get the average of given  numbers
# average (a+b+c)/3
a = 20
b = 30
c = 10
print("average:", (a+b+c)/3)

# print the square and cube of a given number
num = 9
print("square:",  num**2)
print("cube:", num**3)

# interchange values
a = 10
b = 30
a,b =b,a
print("a:", a)
print("b:", b)
# solve this  pythagorous theorem
#a2 + b2 = c2
a = 5
b = 4
LHS = a**2 + b**2
RHS = LHS
print(LHS**2)
# solve the  given match formula
# formula  a2- b2 = (a-b)(a+b)
a = 2
b = 6
LHS = a**2 - b**2
Result = ((a-b)*(a+b))
print(("LHS:", Result))
# slove the formula one
# formula (a+b)3 =  a3+3ab(a+b)+ b3
a = 3
b = 5
Result = a**3+3*a*b*(a+b)+b**3
print("(a+b)^ 3:", Result)

# (a-b)3 = a3 -3a2b+3ab2 -b3
a = 5
b = 7
result = a**3-3*a*b+3*a*b*2 -b**3
print("(a-b)^3):", Result)











=======
>>>>>>> 05afb3d817068be9dde9559491a44536c0700b71






