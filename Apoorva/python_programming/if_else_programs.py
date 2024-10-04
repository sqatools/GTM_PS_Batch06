#1. Python program to check given number is divided by 3 or not.
'''
num1 = float(input("enter the number:"))

if num1%3 == 0:
    print("number is divisible by 3:", num1)
else:
    print("number is not divisible by 3:")
'''

#3.  If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks

'''
total_marks = float(input("enter the total marks scored:"))

if  total_marks >100:
    print("Invalid marks: Please enter valid marks")
elif  40<= total_marks < 50:
    print("the grade is grade C")
elif 50 <= total_marks < 60:
    print("the grade is grade B")
elif 60 <= total_marks < 70:
    print("the grade is grade A")
elif 70 <= total_marks < 80:
    print("the grade is grade A+")
elif 80 <= total_marks <90:
    print("the grade is grade A++")
elif 90 <= total_marks < 100:
    print("the grade is grade Excellent!")
else:
    print("Failed in examination")
    '''
#############################
print("444444444444444444444444444444444")
#4. Python program to check the given number divided by 3 and 5
'''
num2 = float(input("Enter the number to check if divisible by 3 and 5: "))

if num2%3 == 0 and num2 % 5 == 0:
    print("The number is divisible by 3 and 5", num2)

else:
    print("The number isn't divisible by 3 and 5")
    
'''
#####################################################################

# 5. Python program to print the square of the number if it is divided by 11.

'''num1 = float(input("Enter the number::"))

if num1%11 == 0:
    print("the number is didvisible by 11 and the square of the number is:", num1**2)
else:
    print("the number is not divisible by 11")
    
'''

##################################################################

#7). Python program to check given number is odd or even.
'''
num1 = float(input("Enter the number::"))

if num1%2 == 0:
    print("the given number is even")
else:
    print("the number is odd")
'''

##################################################################

#8. Python program to check a given number is part of the Fibonacci series from 1 to 10.

# 0,1,1,2,3,5,8 # only upto 10

'''fib = [0,1,1,2,3,5,8]
num1 = float(input("Enter the number::"))

if num1 in fib:
    print("the number is part of fibonacci series")
else:
    print("the number is not in fibonacci series")
'''

############################################################

# 9.  Python program to check authentication with the given username and password.
''''
username1 = "Apoorva"
password1 = "apoorva123"

username = input("enter valid Username:")
password = input("enter valid password:")

if username == username1 and password ==password1:
    print("Logged in successfully")
else:
    print("please enter valid username/password")
''''

##########################################################

# 10). Python program to validate user_id in the list of user_ids.

