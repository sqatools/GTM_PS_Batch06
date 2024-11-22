# Write a python program to calculate following operation with the help of function
# 1.  Calculate factorials  :  def fact
# 2.  Check the prime number : def prime
# 3.  Create fabonacci series :  def fabonacci
# 4.  Create a table of given number : def create_table
# 5.  Calculate_operation : This function will accept only one number then it will provide output for all above operation.
def fact(n):
    fact = 1
    while n > 0:
        fact *= n
        n -= 1
    print(f"Factorial of {num}: {fact}")
num = int(input("Enter a number for Factorial: "))
fact(num)

print("*"*50)


def prime(num):
    count = 0

    for i in range(2,num):
        if num%i == 0:
            count += 1

    if count > 0:
        print("It is not a prime number")
    else:
        print("It is a prime number")

num1 =  int(input("Enter a number for Prime: "))
prime(num1)

print("*"*50)


def table(num):
    a = 0
    for i in range(1,11):
        a = i*num
        print(i,"*",num,"=",a)

n = int(input("Enter a number for Table: "))

table(n)

print("*"*50)


