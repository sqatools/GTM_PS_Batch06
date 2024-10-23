# 1). Write a  Python loops program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included)

"""
for i in range(1500, 2701, 1):
   if i%7 == 0 and i%5 == 0:
       print(i, end=' ')
"""

# 3). Python Loops program that will add the word from the user to the empty string using  python.
"""
inputword = input("Enter Input: ")
var = " "
for i in range(len(inputword)):
   var = inputword[i]
   print(var)
"""

# write a python program to find out the given number is prime or not
# nested loop with break
"""
num1 = int(input("Enter Input: "))

for num in range(1, num1+1):
   prime = True
   for i in range(2, num):
       #print("i :", i)
       if num % i == 0:
           prime = False
           break
       else:
           pass

   result = "This is prime number :" if prime else "This is not prime number :"
   print(result , ":", num)
"""
"""
# continue and break statement
for i in range(1, 11):
   if i == 6:
       continue
   #else:
       #pass
   print("value if i :", i)
"""
# write a python program to print the number not divisible by 2
"""
for i in range(10):
   if i%2 == 0:
       continue
   print(i)
"""
# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
# using continue statement
"""
for k in range(0, 6):
   if k == 3 or k == 6:
       continue # skip
   else:
       pass
       print(k)
"""

# 4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
# 52). Find the numbers which are divisible by 5 in 0-100 using Python Loops.
"""
for i in range(0, 100+1):
   if i%5 == 0:
       print(i)
   else:
       pass
"""

# using string

