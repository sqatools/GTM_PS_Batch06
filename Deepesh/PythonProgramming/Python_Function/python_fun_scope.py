"""
local variables : When we defined any variable inside the function, then it is known as local
                  variable, and scope of the local variable is limited to the same function.

global variables :  When we defined any variable outside the function, then it is known
                    global variable, and scope the of the global variable is across the module.

                    ->  If we want to change the value of global variable inside the function
                    then we should use "global var_x" keyword.

non local variables : When we defined any variable inside the outer function, then it is known nonlocal variable
                    -> non local variable scope is limited all the inner function and the outer function only.
                    -> if we want to change the value of nonlocal variable inside the inner function then we should use
                    'nonlocal keyword'
"""
# global variable
var_x = 500


def function1():
    print("______Function1_____")
    global var_x
    var_y = 300  # local variable
    var_x = 700
    print("var_x global  :", var_x)
    print("var_y local  :", var_y)


def function2():
    print("______Function2_____")
    var_z = 400  # local variable
    print("var_x global  :", var_x)
    # print("var_y local  :", var_y)
    # local variable of any other function can not access
    print("var_z local  :", var_z)


function2()
function1()
function2()

print("\n\n\n\n")

print("#" * 40)

################ Nonlocal variable ############
var_p = 50  # global variable


def outer_function():
    var_q = 100  # nonlocal variable

    def inner_fun1():
        print("----fun1-----")
        nonlocal var_q
        global var_p
        var_r = 200  # locaL variable
        var_q = 500
        var_p = 1000
        print("global variable var_p :", var_p)
        print("nonlocal variable var_q :", var_q)
        print("local variable var_r :", var_r)

    def inner_fun2():
        print("----fun2-----")
        var_s = 300  # locaL variable
        print("global variable var_p :", var_p)
        print("nonlocal variable var_q :", var_q)
        print("loval variable var_r :", var_s)

    inner_fun2()
    inner_fun1()
    inner_fun2()


outer_function()


###########
# Write a python program to calculate following operation with the help of function
# 1.  Calculate factorials  :  def fact
# 2.  Check the prime number : def prime
# 3.  Create fabonacci series :  def fabonacci
# 4.  Create a table of given number : def create_table
# 5.  Calculate_operation : This function will accept only one number then it will provide output for all above operation.

def factorial(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i

    return fact


def check_prime_number(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
        else:
            continue
    return prime


def get_fabonacci_series(num):
    a = 0
    b = 1
    series = []
    for i in range(num):
        a, b = b, a + b
        series.append(a)

    return series


def create_table(num):
    for i in range(1, 11):
        print(i, "*", num, "=", i * num)


def calculate_operation(num):
    print("________Factorial________")
    print(f"Factorials of {num} :", factorial(num))
    print("________Check Prime Number________")
    print(f"Check prime number of {num} :", check_prime_number(num))
    print("_______Fabonacci Series________")
    print(f"Fabonacci Series {num} :", get_fabonacci_series(num))
    print("__________Table of given number________")
    create_table(num)


calculate_operation(11)
