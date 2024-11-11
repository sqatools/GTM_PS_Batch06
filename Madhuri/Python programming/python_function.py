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
"""
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

#  HOME WORK_________python program  to make a simple calculator using functions
def add(a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)


num1 = int(input("Enter first number:"))
num2 = int(input("Enter Second number:"))
val = int(input("Enter opertion  of your choice"))
if val in (1,2,3,4,5):
    if val == 1:
        print("addition of two numbers",num1,num2, add(num1+num2))
    elif val  == 2:
        print("subtraction of two numbers",num1,num2,subtract(num1,num2))
    elif val == 3:
        print("multiplication of two numbers",num1,num2, multiply(num1*num2))
    elif val == 4:
        print("Division of two numbers",num1,num2,divide(num1,num2))
else:
    print("Invalid value ")




