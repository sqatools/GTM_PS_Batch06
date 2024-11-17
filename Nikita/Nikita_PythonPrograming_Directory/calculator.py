def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


number1 = float(input('Enter first number: '))
number2 = float(input('Enter second number: '))
operation = int(input("""What operation do you want? 
1. Addition
2. Subtraction
3, Multiplication
4. Divide
"""))

if operation == 1:
    result = add(number1, number2)
    print('Result is: ', result)
elif operation == 2:
    result = substract(number1, number2)
    print('Result is: ', result)
elif operation == 3:
    result = multiply(number1, number2)
    print('Result is: ', result)
elif operation == 4:
    if number2 == 0:
        print('You can not divide any number by 0')
    else:
        result = divide(number1, number2)
        print('Result is: ', result)
else:
    print('Please enter a valid number')



