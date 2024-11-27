"""
decorator  in python:
Decorator that decorator the existing code without changing its core functionality.

"""

def decorate_fun(func):
    def inner(param):
        print("*"*20)
        func(param)
        print("_"*20)
    return inner


@decorate_fun
def greeting(msg):
    print(msg)


greeting("Good Morning")



def prime_decorator(func):
    def inner(param):
        if param < 100:
            func(param)
        else:
            func(100)

    return inner

@prime_decorator
def get_prime_number_list(range_val):

    for num in range(1, range_val):
        prime = True
        for i in range(2, num):
            if num%i == 0:
                prime = False
            else:
                continue

        if prime:
            print(num, end= " ")

get_prime_number_list(300)
