#1). Python program to check given number is divided by 3 or not.
# Take input through the user
"""num = int(input("Please enter number :"))
# Check whether the number is divisible by 3
if num%3 == 0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")    """


#2. If else program to get all the numbers divided by 3 from 1 to
"""for i in range(1, 31):
    if i % 3 == 0:
        print(i, end=" ")"""

#4). Python program to check the given number divided by 3 and 5.
"""num_a = int(input("Please enter the values :"))

if num_a % 3 == 0 and num_a % 5 == 0:
    print("The number can divide by 3 and 5 :", num_a)
else:
    print("The number can not divide by both 3 and 5 :", num_a)"""

#Python program to check given number is a prime number or not## doubt
#5.Python program to print the square of the number if it is divided by 11.
"""num = int(input("Enter a number: "))
# Check for division
if num % 11 == 0:
    # Print output
    print(num**2)
else:
    # Print output
    print("Number is not divisible by 11")"""


# age = str(input("Please enter your package: "))
#
# if age == "1,000":
#     print('You are Manish')
# elif age == "500":
#     print('You are Sagar')
# else:
#     print('I do not know you')



# Concept of f string in python
# age = "30"
# name_1 = f"Nikita age is {age}"
#
# print(name_1)

name = input("Enter name: ")
password = input("Enter password: ")
# Authenticate username and password
if name == password:
# Print output
    print("It is valid")
else:
# Print output
    print("It is not valid")