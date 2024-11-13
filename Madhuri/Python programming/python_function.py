"""
def<function_name>:
code
"""
"""
def greeting():
    print("Good morning")
greeting()
"""
"""
def greeting_msg(msg):
    print(msg)
greeting_msg("good morning")
greeting_msg("How are you?")

# import specificfunction in this module
#greeting_msg("have a nice day")
#greeting()
def addition(num1,num2):
    print("add vales:",num1+num2)
# pass the values by 2 ways
# 1.pass by value
addition(50,70)
#2. pass by reference
X = 400
y = 600
addition(X,y)
#3
list1 =[3,6,8,2]
list2 = [10,20,30,40]
for i in range (len(list1)):
 addition (list1[i],list2[i])

# function with default parameter  value--
def mulitiplication(num1,num2):
    print(f"multiple values {num1},{num2},{num1*num2}")
"""
"""
# if we cal function without passing value of default parameter
then it will consider default value only
# if we cal function and pass value to the default parameter,then defaultvalue will be overwritten by new value
# we can interchange the parmeter value position with the of parmetername only
# default parmeter always fallow the non default parameter,it means default parmeter always come at the endor roght most side
wrong:def fun(var1 =40,var2)
right:def fun1(var1,var2=50)
# all parameters can have defalut value
def fun(v1 =40,v2 = 50,v3 = 60)
"""
"""
#Parmeter  data type######
def convert_uppercase(var1:str, var2:int,var3:int):
    print(var1.upper())
    print("addition:",var2+var3)
# convert_uppercase (23456)
convert_uppercase('good morning','Hello','Python')
#convert_uppercase('good moring',400,500)
print(" "*50)
# *args parmeters: This parameters accept the values in the from of tuple
# and there is no limit to provide values and their data type
# args name is default name provide by ptyhon we can customize the name as per our requirement

def get_sum_of_values(*args):
    print(args,type(args))
    print("sum of all values:",sum(args))
get_sum_of_values(5,7,8)
get_sum_of_values(35,55,77,99,11)
def print_all_values(*args):
    for val in args:
        print(val)
print(" "*50)
print_all_values(3,3.5,'hello',[3,5,7],(1,4,67),True)
print(" "*50)
print_all_values([6,7,9,12])
"""
###**kwargs
# Kwarg accept the values in the form key value pair it means the data type will be dictionary
# the default name of parameters is kwargs,and we can customize the name as per our requirement
#  Here ** mainly accept the values in the dictionary format,parametr name could be anything
"""
def get_user_info(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,":",v)
print(""*50)
get_user_info(name='Rohn',email='rohan@gamil.com',phone=45667799,address='pune')
"""
"""

def login_fun(**kwargs):
    db_username = 'admin'
    db_password = 'Admin@123'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login successful")
    else:
        print("Access Deined")
print("_"* 50)
login_fun(username='admin',password ='Admin@123')
print("_"* 50)
login_fun(username='user1123',password ='Admin@123')


#######return value  from function#######
$$ function can return value with return statement,that we can use further
$$ we can return mulitiple values from function and retur in form of tuple
&& once the return stament is exectued then function will be terminated
$$ no further code will be exectued
def factorials(num):
    fact =1
    for i in range(num,0,-1):
        fact = fact*i
        print("factorial:",fact)
        return fact

result = factorials(5)
print("factorial value:",result)
print("multiply by 5:",result*5)
"""
"""
def math_operations(n1,n2,n3):
    add = n1+n2
    mul = n2*n3
    subtract = n3-n1
    return add,mul,subtract
values = math_operations(10,20,30)
print("math_operations values:",values)

a,b,c = math_operations(10,20,30)
print("addition of n1 ,n2:",a)
print("multiplication of n2,n3:",b)
print("subtraction of n3,n1:",c)

def get_sum_of_values(*args):
    sum = 0
    for val in args:
        if sum >50:
            return sum
        print(val)
        sum = sum + val
print("-"*50)
sum_result  = get_sum_of_values(10,3,24,17,19,20,5)
print("sum_result:",sum_result)

def add(a,b):
    total = a+b
    return total
add(5,6)
print(a+b)
def mul(a,b):
    total = a*b
    return total
mul( a*b)
print(a*b)
"""
"""

#  HOME WORK_________python program  to make a simple calculator using functions
# create an application  with function all inside function
def add(n1,n2):
    return(n1+n2)
def subtract(n1,n2):
    return(n1-n2)
def multiply(n1,n2):
    return(n1*n2)
def divide(n1,n2):
    return(n1/n2)


def substrction(v1, v2):
    pass


def calculator(operation_num,v1,v2):
    if operation_num ==1:
        add_val = add(v1,v2)
        print ("addition:",add_val)
    elif operation_num ==2:
        print("mulitiplication:",multiply(v1,v2))
    elif operation_num ==3:
        print("subtraction:",substrction(v1,v2))
    elif operation_num ==4:
        print("Divide:",divide ((v1,v2)))

op_val = int(input("Enter the operation number:\n"
                   "1.Addition\n"
                   "2.Mulitiply\n"
                   "3.substraction\n"
                   "4.Division|\n"))

num1 = int(input("enter value for num1:"))
num2 = int(input("enter value for num2:"))
calculator (op_val,num1,num2)
"""

"""
**local variables---------- when we defined any variable inside the function then it is non as local variable
and scope of local varaible is limited to the same function  
***global variables--------When we defined any variablle outside the function then it is non as global variable
and scope of the global varaible is across the module.
-----if we want t change the value of global variables inside the function then we should use global key word.
****non local variables---------When we defined any variable inside the outer function then it is non as non local variable
------Non lolacl variable scope is limited to all the inner funtion and all the outer function only.
------If we want to change the value of non local variable in side the inner function then we should use non local keyword
"""
"""
var_x = 500
def function1():
    print("-------function1------")
    global var_x
    var_y = 300 # local variable
    var_x = 700
    print ("var_x global :",var_x)
    print("var_y local:", var_y)

def function2():
     print("-----function2----")
     var_z = 400 # local varible
     print("var_x global:",var_x)
    # print("Var_y local:", var_y)
    # local varible of any OTHER FUNCTION CAN NOT ACCESS
     print("var_z local:",var_z)
function2()
function1()
function2()
##########non local variable######
var_p = 50 # global variable
def outer_function():
 var_q =100 # non local variable
 def inner_fun1():
      print("---fun1-----")
      nonlocal var_q
      global  var_p
      var_r = 200 # local variable
      var_q = 500 # non local variable
      var_p = 1000
      print("global variable var_p:",var_p)
      print("nonlocal variable var_q:",var_q)
      print("local variable var_r:",var_r)

 def inner_fun2():
      print("---fun2-----")
      var_s = 300 # local variable
      print("global variable var_p:",var_p)
      print("nonlocal variable var_q:",var_q)
      print("local variable var_s:",var_s)
 inner_fun2()
 inner_fun1()
 inner_fun2()
 """

# python function  program to print a table of a number\
def table(num):
    a = 0
    for i in range(1,11):
        a = i*num
        print(i,"*",num,"=",a)
n = int(input("enter the number"))
table(n)
# prime number
def prime(num):
    count = 0
    for i in range(2,num):
        if num%i ==0:
            count +=1
    if count >0:
      print("It is not prime number ")
    else:
        print("it is a prime number")
num1 = int(input("Enter a number"))
prime(num1)
# fibonacci series
def fibo():
    num1 = 0
    num2 = 1
    count = 0
    while count <10:
     print(num1,end=" ")
    n2 = num1+num2
    num1 = num2
    num2 = n2
    count+=1
fibo()

def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(f"Factorial of {num}: {fact}")
num = int(input("Enter a number: "))
fact(num)
# Home Work------------------->
# write a python program to calculate following operation with the help of function
def  factorial(num):
    fact = 1
    for i in range (num,0,-1):
        fact = fact*i
    return fact
"""
def check_prime_number(num):
    prime = True
    for i in range(2,num):
        if num % i == 0:
             prime = False
            break
        else:
            continue
    return prime
    """
def get_fabonacci_series(num):
    a = 0
    b = 1
    series = []
    for i in range(num):
        a,b =b,a+b
        series.append(a)
    return series
def create_table(num):
    for i in range(1,11):
        print(i,"*",num,"=",i*num)
def calculate_operation(num):
    print("--------factorial------------")
    print(f"factorial of {num}:",factorial(num))
    print("------ check prime number--------")
    print("-------fabonacci series--------")
    #print(f"checkprime number of {num}:",check_prime_number(num))
    print(f"fabonacci series of {num}:",get_fabonacci_series(num))
    print("-------table of given number----------")
    create_table(num)






