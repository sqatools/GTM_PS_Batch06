"""
def <function_name>:
     code

-> function can be defined without parameter.
-> function can be with parameters as well
-> once function is created, then we can call same function n number of times.
-> Function is block of code that will execute every time, whenever we call
   it in same module or any other module
"""
#
var_a = "November 2024"


# function without parameters
def greeting():
    print("Good Morning")


# greeting()
# greeting()
# greeting()
# greeting()

# print(id(list), type('Hello'))


# function with parameters
def greeting_msg(msg):
    print(msg)


"""
greeting_msg("Good Evening")
greeting_msg("How are you?")
greeting_msg("Good Night, Have a nice sleep")
greeting_msg(12345)
"""


# greeting_msg("Hello", 1234)
# TypeError: greeting_msg() takes 1 positional argument but 2 were given


def addition(num1, num2):
    print("add values :", num1 + num2)


# pass the values by 2 ways
# 1. Pass by value
addition(50, 70)

# 2. Pass by reference
x = 400
y = 600
addition(x, y)

list1 = [3, 6, 8, 2]
list2 = [10, 20, 30, 40]
for i in range(len(list1)):
    addition(list1[i], list2[i])

print("_" * 50)
###############
################

def multiplication(num1, num2=50):
    print(f"multiply values num1={num1}, num2={num2}: {num1 * num2}")

"""
->  if we call function without passing value to default parameter,
    then it will consider default value only

-> if we call function and pass value to the default parameter, then
   default value will be overwritten by new value
   
-> We can interchange the parameter value position with the help 
    of parameter name only
    
-> Default parameter always follow non default parameter, it means default parameter
   always come at end or right most side
   right :
     def fun1(var1, var2=50)
     
   wrong :
     def fun2(var1=40, var2) 
     
-> All parameter can have default value
    def fun(v1=40, v2=50, v3=60)
"""

multiplication(5)  # num2 considered default value
# multiply values num1=5, num2=50: 250

multiplication(6, 7) # num2 will consider 7 as new value
# multiply values num1=6, num2=7: 42

multiplication(num2=30, num1=20) # positions are interchanged with parameter name only
# multiply values num1=20, num2=30: 600


print("_"*50)
def names(n1='Rahul', n2='mohit', n3='Aman'):
    print(f"Name 1: {n1}")
    print(f"Name 2: {n2}")
    print(f"Name 3: {n3}")

names()
print("_"*50)
names('Ankita') # pass by value
print("_"*50)
var1 = 'Raghav'
names(var1)  # pass by reference


################# parameter data type ############
"""
-> We can provide function parameter data type, but it optional.
-> In good code coding style user should provide what type of data is expected 
for the parameters.

"""
def convert_uppercase(var1: str, var2: int,  var3: int):
    print(var1.upper())
    print("addition :", var2+var3)


#convert_uppercase(23456)
convert_uppercase('good morning', 'Hello', 'Python')
convert_uppercase('good morning', 400, 500)
#convert_uppercase((4, 6, 8), 400, 500)


print("_"*50)
################
# *args  parameter : This parameter accept the values in the form of tuple,
# and there is no limit to provide values and their data type.
# args is default name provided by python, we can customize the name as per our requirement.

def get_sum_of_values(*args):
    print(args, type(args))
    print("sum of all values :", sum(args))

get_sum_of_values(5, 7, 8)
get_sum_of_values(33, 55, 77, 99, 11)

def print_all_values(*var):
    print(var)
    for val in var:
        print(val)

print("_"*50)
print_all_values(3, 3.5, 'Hello', [3, 5, 7], (1, 4, 67), True)
print("_"*50)
print_all_values([6, 7, 9, 12]) # ([6, 7, 9, 12],)


################### **kwargs parameter ##############
"""
***kwargs
-> kwargs accept the values in the form key value pair it means the data type will
   be dictionary
   
-> The default name of parameter is kwargs, and we can customize the name as per 
   our requirement.
   
-> ** mainly accept the values in the dictionary format, param name could be anything
"""


def get_user_info(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, ":", v)

print("_"*50)
get_user_info(name='Rohan', email='rohan@gmail.com', phone=454354325, address='Pune')
# {'name': 'Rohan', 'email': 'rohan@gmail.com', 'phone': 454354325, 'address': 'Pune'}


def login_fun(**kwargs):
    db_username = 'admin'
    db_password = 'Admin@123'
    if kwargs['username'] == db_username and kwargs['password'] == db_password:
        print("Login Successful")
    else:
        print("Access Denied")


print("_"*50)
login_fun(username='admin', password='Admin@123')
print("_"*50)
login_fun(username='user123', password='admin@123')


################# Return value from function ########
"""
-> Function can return value with return statement, that we can use further.
-> We can return multiple values from function, return in form of tuple
-> Once the return statement is executed then function will be terminated.
   no further code will be executed.

"""
def factorials(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact*i
    print("Factorial :", fact)
    return fact

result = factorials(5)
#print("Factorial value :", result)
# Factorial value : 120
#print("multiply by 5 :", result*5)


def math_operations(n1, n2, n3):
    add = n1+n2
    mul = n2*n3
    subtract = n3-n1
    return add, mul, subtract

values = math_operations(10, 20, 30)
print("math operation values :", values)

a, b, c = math_operations(10, 20, 30)
print("addition of n1, n2:", a)
print("multiplication of n2, n3:", b)
print("subtraction of n3, n1:", c)


def get_sum_of_values(*args):
    sum = 0
    for val in args:
        if sum > 50:
            return sum
        print(val, sum)
        sum = sum + val

    print("Execution completed")

print("_"*50)
sum_result = get_sum_of_values(10, 3, 24, 17, 19, 20, 5)
print("sum result :", sum_result)



# write a python program to create calculate where each operation has to do function
# and return a value, like add, multi, sub, divide
def add(n1, n2):
    return n1+n2


