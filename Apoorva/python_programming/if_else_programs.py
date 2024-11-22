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
'''

##########################################################

# 10). Python program to validate user_id in the list of user_ids.

'''user_id = [1,1.2,2,3,4,5,6,7,8]

id = float(input("enter the id ::"))

if id in user_id:
    print("id is in the list of user ids")
else:
    print("id is not in the list of user ids")
'''

#############################################################

# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.

'''num1 = int(input("enter the number::"))

if num1%2 == 0:
    print("square of the number:", num1**2)
elif num1%3== 0:
    print("cube of the number:", num1**3)
else:
    print("the number is not divisible by 2 or 3", num1)
'''

##########################################################

#12). Python program to describe the interview process.

'''
round1 = "clear1"
round2 = "clear2"
round3 = "not_clear3"

if round1 == "clear1":
    print("Candidate has cleared 1st round")
    if round2 == "clear2":
        print("Candidate has cleared 2nd round")
        if round3 == "clear3":
            print("Candidate has cleared 3rd round. Congratulations,you are hired.")
        else:
            print("Candidate has not cleared 3rd round")
    else:
        print("Candidate has not cleared 2nd round")
else:
    print("Candidate has not cleared 1st round")
'''

# 13. Python program to determine whether a given number is available in the list of numbers or not.

'''list1 = [2,4,6,8,10,12,14,16,18,20]

num1= int(input("enter the number::"))

if num1 in list1:
    print("the number is available in list of numbers:", num1)
else:
    print("the number is not available in the list", num1)
'''

###########################################################

#14). Python program to find the largest number among three numbers.

'''num1 = float(input("enter the num1:"))
num2 = float(input("enter the num3:"))
num3 = float(input("enter the num3:"))

if num1>num
'''

#15: 15). Python program to check any person eligible to vote or not
#age > 18+ : eligible
#age < 18: not eligible

'''age1 = float(input("enter the age of the voter::"))

if age1 >=18 and age1<=105:
    print("the person is eligible to vote with age:", age1)
elif age1 <18:
    print("the person is not eligible for voting with age:", age1)
else:
    print("Please enter valid age")
'''

#########################################################################

#18). Python program to check whether a student has passed the exam.
# If marks are greater than 35 students have passed the exam.

'''
marks1 = float(input("enter the marks scored:"))

if 35 <= marks1 <= 100:
    print("Student passed exam with marks:", marks1)
else:
    print("Student failed the exam with marks:", marks1)
'''

################################################################

 #19.Python program to check whether the given number is positive or not.
#Input = 20
#Output = True
'''
num1 = float(input("enter the number ::"))

if num1>=0:
    print("the number is positive:",num1)
else:
    print("the number is negative:", num1)
'''

#20). Python program to check whether the given number is negative or not.
'''
num1 = float(input("enter the number ::"))

if num1<0:
    print("the number is negative:",num1)
else:
    print("the number is positive:", num1)
'''

#21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even

num1 = float(input("Enter the number:"))

if num1>=0
    print("the number is divisible by2 and even:",num1)
    if


    else



