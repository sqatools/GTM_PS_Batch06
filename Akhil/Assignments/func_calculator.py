
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

Operation_type = input("please provide the Operation addition /subtraction/multiplication/division :")
n1 = float(input("Enter n1 value "))
n2 = float(input("Enter n2 value "))

if Operation_type == 'addition':
    Result = addition(n1, n2)
    print(Result)

elif Operation_type == 'multiplication':
    Result = multiplication(n1, n2)
    print(Result)

elif Operation_type == 'subtraction':
    Result = subtraction(n1, n2)
    print(Result)

elif Operation_type == 'division':
    Result = division(n1, n2)
    print(Result)
else:
    print("wrong input, please choose valid input")