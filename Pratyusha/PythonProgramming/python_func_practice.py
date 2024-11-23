"""n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
operator = input("Choose a operator: ")

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
    if n2 == 0:
        return "you can't divide by zero"
    return n1/n2


if operator == '+':
    result = add(n1, n2)
elif operator == '-':
    result = sub(n1, n2)
elif operator == '*':
    result = mul(n1, n2)
elif operator == '/':
    result = div(n1, n2)
else:
    result = "Sorry, that's not a valid operation"


print(f"Result: {result}")"""


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


def prime(num):
    pm = True
    for i in range(2, num):
        if num % i == 0:
            pm = False
    if pm:
        return "Prime number"
    else:
        return "Not a prime number"


def fibonacci(num):
    a = 0
    b = 1
    fib = []
    for i in range(num):
        a, b = b, a + b
        fib.append(b)
        return fib


def table(num):
    for i in range(1, 13):
        print(num, 'x', i, '=', num * i)


def calculate_operation(num):
    print("___________Factorial_____________")
    print(f"Factorial of {num}: ", factorial(num))
    print("___________Check prime_____________")
    print(f"Check prime of {num}: ", prime(num))
    print("___________Fibonacci series_____________")
    print(f"Fibonacci series of {num}: ", fibonacci(num))
    print("___________Table of num_____________")
    table(num)

calculate_operation(4)

