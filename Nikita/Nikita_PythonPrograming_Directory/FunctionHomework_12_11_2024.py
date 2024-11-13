
def factorial(number):
    output = 1
    for i in range(1, number + 1):
        output = output * i
    return output


def prime_number(number):
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        return (f"{number} is a prime number")
    else:
        return (f"{number} is not a prime number")


def fabonacci(number):
    return 'In progress'


def create_table(number):
    table = []
    for i in range(1, 11):
        table.append(number * i)
    return table


def calulate_operation(number):
    print('Factorial value is: ', factorial(number))
    print('Table is: ', create_table(number))
    print('Prime function: ', prime_number(number))
    print('Fabonacci function: ', fabonacci(number))


calulate_operation(10)

