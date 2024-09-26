#Session:1 23/09/2024
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
#Session 2:24/09/2024

#REMAINDER OPERATOR

var1=10
var2=4
print("remainder value:",var1 % var2)
print("remainder value:", 11%4)

#EQUAL TO OPERATOR
print("#"*30)

n1=10
n2=40
n3=10
print("eual to:",n1 == n2)
print("eual to:",n1 == n3)

print("#"*30)

n1=10
print("check for even:",n1 % 2 == 0)
print("check for odd:", n1 %2 !=0)
#or
print("check for odd:", n1 % 2 ==1)

print("#"*30)

# BASIC ASSIGNMENT PROGRAMS

#1.Python Program to add two integer values.
num1=10
num2=20
print("add two integer values:",num1+num2)

print("#"*30)
#2.Python Program to subtract two integer values.
num1=20
num2=15
print("to subtract two integer values:",num1-num2)

print("#"*30)
#3.Python program to multiply two numbers
num1=5
num2=10
print("to multiply two numbers:",num1*num2)

print("#"*30)

#4. Python program to repeat a given string 5 times.
#Input :
#str1 = "SQATools"
#Output :
#“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”

str1="SQATools"
print("repeat a given string 5 times:",str1*5)

print("#"*30)

#5.Python program to get the Average of given numbers.
#Formula: sum of all the number/ total number
#Input:
#a = 40
#b = 50
#c = 30
#Output :
#Average = 40

a = 40
b = 50
c = 30
print("Average of given numbers:",(a+b+c)//3)

print("#"*30)

#6. Python program to get the median of given numbers.
#Note: all the numbers should be arranged in ascending order
#Formula : (n+1)/2
#n = Number of values
#Input : [45, 60, 61, 66, 70, 77, 80]
#Output:  66

input = [45, 60, 61, 66, 70, 77, 80]
input.sort()
n=(len(input))/2
print("median of given numbers:",input[int(n)])

print("#"*30)

#7. Python program to print the square and cube of a given number.
#Input :
#num1 = 9
#Output :
#Square = 81
#Cube =   729

num1=9
print("square of given num:",num1**2)
print("cube of given num:",num1**3)

print("#"*30)

#8. Python program to interchange values between variables.
#Input :
#a = 10
#b = 20
#Output :
#a = 20
#b = 10

a=10
b=20
a,b = b,a
print("after interchanging value of a: ",a)
print("after interchanging value of b: ",b)

print("#"*30)

#DOUBT

#9.Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)



#10.Python program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab

a=40
b=20
lhs=(a+b)**2
print("lhs output:",lhs)

rhs=a**2+b**2+2*a*b
print("rhs output:",rhs)

print("#"*30)

#11.Python program to solve the given math formula.
#Formula : (a – b)2 = a^2 + b^2 – 2ab
a=40
b=20
lhs=(a-b)**2
print("lhs output:",lhs)

rhs=a**2+b**2-2*a*b
print("rhs output:",rhs)

print("#"*30)

#12. Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)

a=40
b=20
lhs=a**2 - b**2
print("lhs output:",lhs)

rhs=(a-b)*(a+b)
print("rhs output:",rhs)

print("#"*30)

#13.Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a=40
b=20
lhs=(a+b)**3
print("lhs output:",lhs)

rhs=a**3+3*a*b*(a+b)+b**3
print("rhs output:",rhs)

print("#"*30)

#14.Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a=40
b=20
lhs=(a-b)**3
print("lhs output:",lhs)

rhs=a**3-3*a*2*b+3*a*b*2-b**3
print("rhs output:",rhs)

print("#"*30)

#15.Python program to calculate the area of the square.
#Formula : area = a*a

a=9
print("The area of the square:",a*a)
#or
print("The area of the square:",a**2)

print("#"*30)

#16.Python program to calculate the area of a circle.
#Formula = PI*r*r
#r = radius
#PI = 3.14

pi=3.14
r=5
x=pi*r*r
print("area of a circle:",x)

print("#"*30)

#17. Python program to calculate the area of a cube.
#Formula = 6*a*a

a=2
print("area of a cube:",6*a*a)

print("#"*30)

#18.Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

pi=3.14
r=2
h=3
print("area of the cylinder:",2*pi*r*h + 2*pi*r*r)

print("#"*30)

# DOUBT

#19.Python program to check whether the given number is an Armstrong number or not.
#Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

print("#"*30)

#20.Python program to calculate simple interest.
#Formula = P+(P/r)*t
#P = Principle Amount
#r = Anual interest rate
#t = time
p=10000
r=2
t=1
print("simple interest:",p+(p/r)*t)


print("#"*30)

#27.Python program to calculate compound interest.
#CI=p*((1+r/100)**n)
p=10000
r=10
n=2
CI=p*((1+r/100)**n)
print("compound  interest:",CI)

print("#"*30)

#39.Python program to calculate the volume of a sphere.
#Formula = (4/3*pi*r^2)
#r = radius
#pi = 3

pi=3.14
r=5
n=4/3*pi*r**2
print("volume of a sphere:",n)

print("#"*50)

#Session 3:25/09/2024

#DATA TYPES
#1.Number ---->Integer,float,complex numbers
#2.Sequentials--->String,List,Tuple
#3.Dictionary
#4.Set
#5.Boolean

#INTEGER DATA TYPE

a=10
print("integer type a:",type(a),a)

b=233243536446573473457324324
print("integer type b:",type(b),b)

c=123
print("integer type c:",type(c),c)
c=100
print("integer type c:",type(c),c)

d=0
e=-234
print("integer type d:",type(d),d)
print("integer type e:",type(e),e)

#FLOAT DATA TYPE

var_a=50.66
print("float type var_a:",type(var_a),var_a)

var_b=567721873682.1768716821
print("float type var_b:",type(var_b),var_b)

var_c=55.33454656655765756
print("float type var_c:",type(var_c),var_c)

var_d=0.0
print("float type var_d:",type(var_d),var_d)

#COMPLEX DATA TYPE










