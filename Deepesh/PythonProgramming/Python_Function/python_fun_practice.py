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
############### function with default parameter value ###############

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
