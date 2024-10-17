# 1. Python program to check whether the input number is a square of 6 or not.
# Input= 37

input_a = 37
if input_a == 6**2:
    print("This value is square of 6:",input_a)
else:
    print("This value is not square of 6:",input_a)

print("#"*50)
# 2.Python program to print the square of the number if it is divided by 3 and cube if divisible by 7

num_a = int(input("Enter the number: "))
print(num_a%2 == 0 or num_a%7 == 0)
if num_a%3 == 0:
    print("This number is divided by 3 :",num_a**2)
elif num_a%7 == 0:
    print("This number is divided by 7 :",num_a**3)
else:
    print("the given number is not divided by 3 and 7")
    

print("#"*50)

# 3.Write a python program to print factorial of number if it is divisible by 3.
a = 10
num = 1
for i in range(3,10,3):
    num = num * i
    print("num :",i,":",num)

print("#"*50)
# 4.write a python print prime numbers between 1 to 50.
#
#prime = true
"""
num= (2,3,4,5,6,7,8,9,10)
for i in num:
    for i in range(1,50):
      if i%num == 0 :
         #print("i:",i)
#if prime == True:
          print("this is not prime number:",i)
else:
    print("this is  prime number",i)
    """
print("#"*50)

# 5.Write a python program to print the average of 5 numbers from 10-15.


print("#"*50)
#6. Write a python program get score of even nunber and cube odd number from given list.
list1 = [ 10, 13, 6, 7, 17, 3, 8, 19]
odd=0
even=0
for i in list1:
    if i%2==0:
        print("value is even:",i,"square of value:",i**2)
    else:
        print("value is odd:",i,"cube of value:",i**3)
print("#"*50)
# 7. write a python repeated the string 5 time if length of string is even and repeat string 7 times if length is odd.
#input_str = take input from user.

string= len("string")
string = input("Please enter the string ")
for i in range (len(string)):
    if len(string)%2 ==0:
      print("This string  length is even",string*5)
    else:
       print("This string is odd",string*7)
print("#"*50)
# 8). Write a python program  to print below pattern of numbers

num =0
for i in range(1,5):
     for j in range(i):
         num +=2

     print()


print("#"*50)
#9).  Write a python program  to print below pattern of numbers
for i in range(4):
    for j in range(i):
        print(j,end=" ")

    print()
for i in range(4,0,-1):
    for j in range(i):
        print(j,end=" ")
    print()

print("#" * 50)
#10). Write a python to check given number is palindrome or not, ( don't use data type conversation, use while loop
#   reverse the number.
#n1 : 121 , palindrome : True
#n1 : 123 , palindrome : False