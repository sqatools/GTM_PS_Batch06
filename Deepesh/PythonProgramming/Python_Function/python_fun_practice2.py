# create an application with function call inside function
def add(n1, n2):
    return n1 + n2


def multiply(n1, n2):
    return n1 * n2


def subtraction(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 // n2


def calculator(operation_num, v1, v2):
    if operation_num == 1:
        add_val = add(v1, v2)
        print("addition:", add_val)

    elif operation_num == 2:
        print("multiplication :", multiply(v1, v2))

    elif operation_num == 3:
        print("Subtraction  :", subtraction(v1, v2))

    elif operation_num == 4:
        print("Divide :", divide(v1, v2))


op_val = int(input("Enter the operation number :\n"
                   "1. Addition\n"
                   "2. Multiply \n"
                   "3. Subtraction \n"
                   "4. Division \n"))

num1 = int(input("enter value for num1:"))
num2 = int(input("enter value for num2:"))
calculator(op_val, num1, num2)
