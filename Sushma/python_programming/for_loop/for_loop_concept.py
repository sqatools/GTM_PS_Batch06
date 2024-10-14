#to check for prime number
"""num=int(input("enter the num:"))
prime = True
for i in range(2,num):
    if num % i == 0:
     prime = False
    else:
     pass
if prime == True:
    print("given num is prime")
else:
    print("given num is not prime")"""
#Factorial number
"""num=int(input("enter the number:"))
fact=1
for i in range(num,0,-1):
    fact =fact*i
    print("factorial num:",i,fact)"""

#Q) 1.print pattern
"""
*
* *
* * * 
* * * *
* * * * *
"""

"""for i in range(0,6,1):
    for j in range(i):
        print("*",end=" ")
    print()"""

#Q) 2.print pattern
"""
* * * * *
* * * *
* * *
* *
*
"""

"""for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()"""

#Q)swap numbers
"""a=10
b=20
print("before swapping a:",a)
print("before swapping b:",b)
a,b = b,a
print("after swapping a:",a)
print("after swapping b:",b)"""

#Q) fibonacci  number
num = int(input("Enter the number of terms for the Fibonacci sequence: "))

i, j = 0, 1  # Initialize the first two Fibonacci numbers

for _ in range(num):  # Loop num times
    print(i, end=" ")  # Print the current Fibonacci number
    k = i + j   # Calculate the next Fibonacci number
    i = j         # Update i to the current j
    j = k       # Update j to the next Fibonacci number
