
"""
Exception handling provide facility to use, if they want to customize the error msg as per their
requirement.


try:
    num1 = 50
    num2 = "60"

    print("addition :", num1+num2)
except Exception as e:
    print(e)
    print("addition not integer number is not allowed")

print("Good Morning")
"""
"""
Exception with raise stop the execution on the spot and can not move ahead for further functionality.

"""
def try_except_with_raise():
    try:
        num1 = 50
        num2= "Hello"
        print("Addition :", num1+num2)
        print("Multiplication :", num1*num2)
        print("Subtraction :", num1-num2)
    except Exception as e:
        print("both the number should be integer")
        raise


    print("Good Morning")


#try_except_with_raise()


# try-except-else condition :
# else section of code only executes, if there is no exception in the code.

def try_except_else(num1, num2):
    try:
        num3 = num1//num2
        print("num3 :", num3)
    except Exception as e:
        print(e)
        print("Can not divide any number with zero")
        #raise
    else:
        # else condition only executes, when there is no error in the code
        print("Code Execution successful there is no error.")

#try_except_else(100, 30)
# Code Execution successful there is no error.
# try_except_else(50, 0)



# try-except-else-finally

def try_except_else_finally(n1, n2, n3):
    try:
        add = n1+n2
        divide = n2//n3
        multiple = n3*n1
        print("add :", add)
        print("Multiply :", multiple)
        print("Division :", divide)
    except Exception as e:
        print(e)
        print("Input values should be integer")
        raise
    else:
        print("Code execution successful")
    finally:
        # Finally block always execution in the code,
        # even there is exception or no exception.
        for i in range(1, 11):
            print(i, "*", n3, ":", n3*i)

    print("Good Morning")



# try_except_else_finally(10, 'Hello', 5)
# print("Good Morning")

"""
for i in range(1, 10):
    if i == 5:
        raise "I is equal to 5 is not allowed"
    print(i)
"""

##### Handle multiple exception ########

def handle_multiple_exception(n1, n2, n3):
    try:
        add_result = n1+n2
        mul_result = n1*n2
        sub_result = n1-n3
        division_result = n1//n3
        print("addition :", add_result)
        print("Multiply :", mul_result)
        print("Subtraction :", sub_result)
        print("division :", division_result)
    except TypeError as e:
        print("All the input values should be integer")
        print(e)
    except ZeroDivisionError as e:
        print("The number can not  divide by zero")
        print(e)
    except Exception as e:
        print(e)

# handle_multiple_exception(4, 5, 6)
"""
addition : 9
Multiply : 20
Subtraction : -2
division : 0
"""

# handle_multiple_exception(4, 'Test', 6)
"""
# Type Error
All the input values should be integer
unsupported operand type(s) for +: 'int' and 'str'
"""

# handle_multiple_exception(4, 10, 0)
"""
# Zero Division Error
The number can not  divide by zero
integer division or modulo by zero

"""

"""
#################### Custom Exception #############
class customException(Exception):
    pass


def try_except_with_custom(num1, num2):
    try:
        num3 = num1//num2
        print("num3 :", num3)
    except Exception as e:
        print(e)
        raise customException("Raising custom generic exception")

try_except_with_custom(5, 0)
"""

#################### Nested level exception #########################


def try_except_nested_exception(num1, num2):
    try:
        add = num1+num2
        print("addition :", add)
        try:
            num3 = num1//num2
            print("Division :", num3)
        except Exception as e :
            print(e)
            print("Can not divide any number with zero")
    except Exception as e:
        print(e)
        print("Both the number should be integer")


try_except_nested_exception(20, 5)
"""
addition : 25
Division : 4
"""

# try_except_nested_exception(20, 'Test')
"""
unsupported operand type(s) for +: 'int' and 'str'
Both the number should be integer
"""
try_except_nested_exception(20, 0)
"""
addition : 20
integer division or modulo by zero
Can not divide any number with zero
"""
