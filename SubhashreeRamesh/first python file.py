print("hello world")
print("_"*50)

num = 30
prime = True
for i in range(2, num):
    if num % i == 0:
        print("i :",i)
        prime = False
    else:
        pass

result = "prime" if prime else "not prime"
print(result , ":", num)
if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)
    print("_" * 50)
"""
    for i in range(1, 11):
        if i == 11:
            continue
        else:
            pass
        print("value if i :", i)
"""
num1 = 5
fact = 1
for i in range(num1, 0, -1):
   fact = fact * i
   print("fact :", i, ":", fact)

      #  print("factorials of num :", fact)

   def is_prime(n):
       if n <= 1:
           return False
       for i in range(2, int(n ** 0.5) + 1):
           if n % i == 0:
               return False
       return True


   # Print prime numbers between 1 and 50
   for num in range(1, 51):
       if is_prime(num):
           print(num)
# 8). Write a python program  to print below pattern of numbers

def print_pattern(rows):
    num = 2  # Start with 2
    for i in range(1, rows + 1):
        for j in range(i):  # Print 'i' numbers in each row
            print(num, end=' ')
            num += 2  # Increment by 2 to get the next even number
        print()
print_pattern(4)