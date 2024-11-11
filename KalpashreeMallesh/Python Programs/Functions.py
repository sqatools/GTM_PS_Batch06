def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
   return "Cannot divide by zero"
  return x / y

# Display operations to the user
print("Select operation:" )
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = int(input("Enter choice of operation 1/2/3/4: "))
x = int(input("Enter the First Number: "))
y = int(input("Enter the Second Number: "))