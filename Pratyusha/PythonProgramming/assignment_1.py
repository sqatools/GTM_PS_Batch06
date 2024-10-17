# 1.Python program to check whether the input number is a square of 6 or not - input = 37
"""num = 36
if num%6 == 0:
    print("Number is a square of 6")
else:
    print("Number is not a square of 6")"""

# 2.Python program to print the square of the number if it is divided by 3 and cube if divisible by 7
"""num1 = int(input("Enter a number to get square or cube: "))
if num1%3 == 0:
    print("Square of number: ", num1**2)
elif num1%7 == 0:
    print("Cube of number: ", num1**3)
else:
    print("Given number is not divisible by both 3 and 7")"""

# 3.Write a python program to print factorial of number if it is divisible by 3.
"""num2 = int(input("Enter a number to get factorial if divisible by 3: "))
fact = 1
if num2%3 == 0:
    for i in range(num2, 0, -1):
        fact = fact*i
else:
    print("Given number is not divisible by 3")

print("factorial of num: ", fact)"""

# 4.Write a python program to print prime numbers between 1 to 50
"""for num3 in range(1, 50):
    if num3 > 1:
        for i in range(2, num3):
            if num3%i == 0:
                break
        else:
            print(num3, end=' ')"""

# 5.Write a python program to print the average of 5 numbers from 10-15 - sum/total
"""sum = 0
for i in range(10, 15):
    sum = sum + i

print("Average of 5 numbers: ", sum//5)"""

# 6.Write a python program to get square of even number and cube of odd number from given list
"""list1 = [10, 13, 6, 7, 17, 3, 8, 19]
for val in list1:
    if val%2 == 0:
        print(val**2)
    else:
        print(val**3)"""

# 7.Write a python program to repeat the string 5 times if length of the string is even and repeat the string
# 7 times if length of the string is odd - input_str = take input from user
"""str1 = input("Enter a string - ")
if len(str1)%2 == 0:
    for i in range(5):
        print(str1)
else:
    for i in range(7):
        print(str1)"""

# 8. Write a python program to print below pattern of numbers:
# 2
# 4 6
# 8 10 12
# 14 16 28 20
"""for i in range(5):
    for j in range(2, 20):
        if j%2 == 0:
            print(j, end=' ')

    print()"""

# 9. Write a python program to print below pattern of numbers:
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2
# 0 1
# 0
"""for i in range(4):
    for j in range(i):
        print(j, end=' ')
    print()

for i in range(4, 0, -1):
    for j in range(i):
        print(j, end=' ')
    print()"""

# 10. Write a python program to check given number i s palindrome or not
# n1: 121, palindrome = true
# n2: 123, palindrome = false

n1 = int(input("Enter number to check palindrome: "))
original_number = n1
rev_val = 0

while n1 > 0:
    temp = n1%10
    rev_val = rev_val*10 + temp
    n1 = n1//10

if original_number == rev_val:
    print("Palindrome = true")
else:
    print("Palindrome = false")