# 1. Python program to check whether the input number is a square of 6 or not.
"""
input = 37

if input == 6**2:
   print("The given input 37 is square of 6 :", )
else:
   print("The give input number is not the square of 6.")
"""

# 2. Python program to print the square of the number if it is divided by 3 and cube if divisible by 7
"""
# num = 50
num = int(input("Enter number: "))
if num % 3 == 0:
   print("The square of num :", num ** 2)
if num % 7 == 0:
   print("The cube of num :", num ** 3)
if num % 3 != 0 and num % 7 != 0:
   print("The num value is not divisible by 3 or 7")
#else:
   #print("The num value is not divisible by 3 or 7")

# Enter number: 21
# The square of num : 441

# Enter number: 17
# The num value is not divisible by 3 or 7
"""

# 3. Write a python program to print factorial of number if it is divisible by 3.
"""
a = 0
b = 1
for _ in range(10):
   a,b = b, a+b
   # print(a, end=" ")
   if a%3 == 0:
       print(a, end=" ")
# 3 21
"""

# 4. write a python program to print prime numbers between 1 and 50.
"""
for num in range(2, 51):
   prime = True
   for i in range(2, num):
       if num % i == 0:
           prime = False
           break
   if prime:
       print(num, end=" ")
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
"""

# 5. Write a python program to print the average of 5 numbers from 10-15.
"""
Method 1:

list1 = [10, 11, 12, 13, 14, 15]
total = sum(list1)
print(total) # 75
avg = total/len(list1)
print("The average of numbers between 10-15 : ", avg) # The average of 6 numbers between 10-15 :  12.5

Method 2: for loop

list1 = [10, 11, 12, 13, 14, 15]
cnt = len(list1)
sum1 = 0
for i in range(0, cnt):
   sum1 = sum1+list1[i]
avg1 = sum1/cnt   
print("The average of numbers between 10-15 : ", avg1) # The average of numbers between 10-15 :  12.5

"""

# 6. Write a python program get score of even number and cube odd number from given list.
# list1 = [10, 13, 6, 7, 17, 3, 8, 19]
"""
list1 = [10, 13, 6, 7, 17, 3, 8, 19]
cnt = len(list1)
# result = []
for i in range(0, cnt):
   # print(i, end=" ")
   # print(list1[i])
   if list1[i]%2 == 0:
       print("Square of even numbers  :", list1[i] ** 2)
   else:
       print("Cube of odd numbers  :", list1[i] ** 3)

# Square of even numbers  : 100
# Cube of odd numbers  : 2197
# Square of even numbers  : 36
# Cube of odd numbers  : 343
# Cube of odd numbers  : 4913
# Cube of odd numbers  : 27
# Square of even numbers  : 64
# Cube of odd numbers  : 6859

"""

# 7. write a python repeated the string 5 time if length of string is even and repeat string 7 times if length is odd.
# input_str = take input from user.

"""
input_str = input(str("Enter a Word : "))
wrd = len(input_str)
print(wrd)
if wrd%2 == 0:
   for i in range(0, 5):
       print(input_str, end=" ")
else:
   for i in range(0, 7):
       print(input_str, end=" ")

# Enter a Word : python # even
# 6
# python python python python python

# Enter a Word : seven # odd
# 5
# seven seven seven seven seven seven seven
"""

# 8). Write a python program  to print below pattern of numbers
#
# 2
# 4 6
# 8 10 12
# 14 16 18 20
"""
num = 2
for i in range(1, 5):
   for j in range(i):
       print(num, end=" ")
       num = num + 2

   print()
"""

# 9).  Write a python program  to print below pattern of numbers
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2
# 0 1
# 0
#
"""
for i in range(1, 5):
   for j in range(i):
       print(j, end=" ")

   print()

for i in range(3, 0, -1):
   for j in range(i):
       print(j, end=" ")

   print()
"""

# 10). Write a python to check given number is palindrome or not, ( don't use data type conversation, use while loop reverse the number.

# n1 : 121 , palindrome : True
# n1 : 123 , palindrome : False

original_val = int(input("Enter the number: "))
num = original_val
reverse_val = 0

while num > 0:
    temp = num % 10
    reverse_val = reverse_val * 10 + temp
    num = num // 10

print("original_val = ", original_val)
print("reverse_val = ", reverse_val)
if original_val == reverse_val:
    print("palindrome : True")
else:
    print("palindrome : False")
# Enter the number: 121
# original_val =  121
# reverse_val =  121
# palindrome : True

# Enter the number: 123
# original_val =  123
# reverse_val =  321
# palindrome : False

