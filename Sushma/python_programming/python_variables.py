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

print("#"*50)

#FLOAT DATA TYPE

var_a=50.66
print("float type var_a:",type(var_a),var_a)

var_b=567721873682.1768716821
print("float type var_b:",type(var_b),var_b)

var_c=55.33454656655765756
print("float type var_c:",type(var_c),var_c)

var_d=0.0
print("float type var_d:",type(var_d),var_d)

print("#"*50)

#COMPLEX DATA TYPE
#complex data type contains real & Imaginary values

var_1= 5+7j
print("complex value:",var_1,type(var_1))
print("real value :",var_1.real)
print("imaginary value :",var_1.imag)

var_a = 10+45j
var_b = 34+50j
var_c = var_a + var_b
print("complex value:",var_c,type(var_c))

var_a = 10+45j
var_b = 34+50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))


#doubt

var_a = 10*45j
var_b = 34-50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))

var_a = 10+45j
var_b = 34+50j
var_c = var_a * var_b
print("complex value:",var_c,type(var_c))
#----------------------------------

var_a = -10+45j
var_b = 34+50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))

var_1 = complex(10,98)
print("complex value:",var_1,type(var_1))

var_2 =complex()
print("complex value:",var_2,type(var_2))

var_3 =complex(5)
print("complex value:",var_3,type(var_3))

var_4 =complex(5j)
print("complex value:",var_4,type(var_4))

print("#"*50)

#SEQUENTIAL DATA TYPE

#STRING DATA TYPE

str_1="hello"
str_2='welcome'
str_3="""to grotech minds
         to learn python
         automation skills"""
print("string 1:",str_1,type(str_1))
print("string 2:",str_2,type(str_2))
print("string 3:",str_3,type(str_3))


str_1="hello "
str_2='welcome '
str_3="""to grotech minds
         to learn python
         automation skills"""
str_4 = str_1 + str_2 + str_3
print("string 4:",str_4,type(str_4))


string = "sushmaravi"
print("indexing value:",string[5]) #+ve indexing starts from s=0,u=1,s=2,h=3,m=3,a=5,r=6,a=7,v=8,i=9
print("indexing value:",string[9])
print("indexing value:",string[-4]) #-ve indexing starts from i=-1,v=-2,a=-3,r=-4,a=-5,m=-6,h=-7,s=-8,u=-9,s=-10
print("indexing value:",string[-10])

#Session 4:26/09/2024

#LIST DATA TYPE:it is mutable data type

#EX:1
list_1=[5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true"]
print("list values:",list_1,type(list_1)) # printing list values & type
print("list values:",len(list_1)) # finding length of the list
print("list values:",list_1[0])  # finding indexing values
print("list values:",list_1[7])
print("list values:",list_1[-6])
print("list values:",list_1[-1])

#EX:2
list_1=[5,8.9,"python"] # list is mutable after creating we can modify /update
                        #Append object to the end of the list.
list_1.append(1000000) # here append is method to add/update the new value at the last(default it will add the values at the last in list)
print("append the list values:",list_1,len(list_1),type(list_1)) # printing list values & type

#EX:3
list_1=[5,8.9,"python"]
list_1.clear() #Remove all items from list
print("clear the list values:",list_1,len(list_1),type(list_1))

#EX:4
list_1=[5,8.9,"python"]
list_1.copy() #copy Return a shallow copy of the list
print("copy the list values:",list_1,len(list_1),type(list_1))

#EX:5
list_1=[5,8.9,"python"]
list_1.count(1) # count Return number of occurrences of value
print("count the list values:",list_1,len(list_1),type(list_1))

#EX:6
"""list_1=[5,8.9,"python"]
list_1.extend() #Extend list by appending elements from the iterable
print("list values:",list_1,len(list_1),type(list_1))"""

#EX:7
list_1=[5,8.9,"python"]
list_1.index("python") #Index Return first index of value.
print("indexing the list values:",list_1,len(list_1),type(list_1))

#EX:8
"""list_1=[5,8.9,"python"]
list_1.insert() #Insert object before index
print("insert the list values:",list_1,len(list_1),type(list_1))"""

#EX:9
list_1=[5,8.9,"python"]
list_1.pop(1) # pop  Remove and return item at index (default last)
list_1.pop(-1)
print("pop the list values:",list_1,len(list_1),type(list_1))

#EX:10
list_1=[5,8.9,"python"]
list_1.remove(8.9) #Remove first occurrence of value
print("remove the list values:",list_1,len(list_1),type(list_1))

#EX:11
list_1=[5,8.9,"python"]
list_1.reverse() #Reverse *IN PLACE*.
print("reverse the list values:",list_1,len(list_1),type(list_1))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("#"*50)

#TUPLE DATA TYPE :it is immutable data type

#EX:1
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
print("tuple values:",tuple_1,type(tuple_1)) # printing list values & type
print("tuple values:",len(tuple_1)) # finding length of the list
print("tuple values:",tuple_1[0])  # finding indexing values
print("tuple values:",tuple_1[7])
print("tuple values:",tuple_1[-6])
print("tuple values:",tuple_1[-1])

#EX:2
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
tuple_1.count(1) #count Return number of occurrences of value
print("count the tuple values:",tuple_1,len(tuple_1),type(tuple_1))

#ex:3
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
tuple_1.index("python") #Index Return first index of value.
print("index the tuple values:",tuple_1,len(tuple_1),type(tuple_1))

print(dir(tuple)) # to check methods of tuple class
#'count', 'index'
print(dir(list)) # to check methods of list class
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("#"*50)
#DICTIONARY DATA TYPE :it is mutable data type

#EX:1
dict_1={'a':12345,'b':6789}
print("dictionary values:",dict_1['a'],dict_1['b'])

#EX:2
dict_1={'a':12345,'b':6789}
print("dictionary values:",dict_1)

#EX:3 #only immutable data types can be key in the dictionary i,e int,float,string,tuple,boolean
dict_1={'name':"sushma",'education':"B.Tech"}
dict_1['department']=["ECE"] #string
dict_1[123]=["ravi"] # int
dict_1[2.3]=["parvathi"] #float
dict_1[(4,5,6)]=["sweet"] #tuple
dict_1[('true')]=["home"] #boolean
print("dictionary values:",dict_1,type(dict_1))

#EX:4 All types of data can store as values  in the dictionary
dict_1={'name':"sushma",'education':"B.Tech"}
dict_1[123]=["ravi"]
dict_1[(4,5,6)]=["sweet"]
print("dictionary values:",dict_1,type(dict_1))

#NOTE: List is not allowed in the dictionary
#dict_1[[1,2,3]]="python"

#EX:5
dict_1[4.5]=True
dict_1[False]=(1,2,3)
dict_1[5.5]='hello'
print("print values:",dict_1)










