"""1. Python program to check whether the input number is a square of 6 or not.
Input = 37

2. Python program to print the square of the number if it is divided by 3 and cube if divisible by 7

3. Write a python program to print factorial of number if it is divisible by 3.

4. write a python print prime numbers between 1 to 50.

5. Write a python program to print the average of 5 numbers from 10-15.

6. Write a python program get score of even nunber and cube odd number from given list.
list1 = [ 10, 13, 6, 7, 17, 3, 8, 19]

7. write a python repeated the string 5 time if length of string is even and repeat string 7 times if length is odd.

input_str = take input from user.


8). Write a python program  to print below pattern of numbers

2
4 6
8 10 12
14 16 18 20


9).  Write a python program  to print below pattern of numbers

0
0 1
0 1 2
0 1 2 3
0 1 2
0 1
0

10). Write a python to check given number is palindrome or not, ( don't use data type conversation, use while loop reverse the number.

n1 : 121 , palindrome : True
n1 : 123 , palindrome : False"""

# Q1.  write a python program to combine a list of data with their index and create new list
# l1 = (5, 7, 9, 12)
# l2 = (10, 40, 50, 600)
# l3 = [15, 47, 59, 72]
# combineresult = []
# for i in range(len(l1)):
#     combineresult.append((l1[i])+(l2[i])+ (l3[i]))
#     print(combineresult)#this is wrong code

list1 = [3, 6, 8, 9, 1, 4, 7, 2]
result = []

for num in list1:
    if num % 2 == 0:
        result.append(num ** 2)
    else:
        result.append('odd')
print(result)


