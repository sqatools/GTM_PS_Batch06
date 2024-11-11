# write a python program to create calculate where each operation has to do function
# and return a value, like add, multi, sub, divide
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
operator = input("Choose a operator: ")

def add(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mul(n1, n2):
    return n1*n2

def div(n1, n2):
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

print(f"Result: {result}")

