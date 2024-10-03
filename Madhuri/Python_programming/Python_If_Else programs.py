#The if-else statement is conditional statement in programming.
# It executes a set  of instructions
# if a particular condition is true, and another set of instructions
# if the condition  is false
#1 Python program to check given number is divided by 3 or not
# take  a number input through the user

num = int(input("please enter number:"))
# check whether the number  is divisible by 3
if  num%3 == 0:
    print("Number is divisible by 3")
else:
    print("number is not divisible by 3")
#___________________________________________________________________
# 2   validate user_id in the list of user ids
id_list = [1,2, 3, 4, 5, 6, 7, 8]
# take user id as input through the user
user = int(input("enter id number:"))
if user in id_list:
    print("valid ID")
else:
    print("invalid id")
#---------------------------------------------------------------------------


# 3 We will assign grades as per total marks
# we will assign  grades to each students as per total marks scored
# condition for  grades
# Marks less than 40; fail
# marks between 40-50: grade c
# marks between 51- 60 grade B
# marks between  61-70: grade A
# marks between 71-80: grade A+
# marks between 81-90: grade A++
# marks between 91-100: Excellent
# Take marks through the user
marks = int(input("Enter Marks:"))
# assign grades based  on marks
if marks<40:
    print("fail")
elif marks>=40 and marks>=50:
    print("Grade c:")
elif marks>=50 and marks<=60:
    print("Grade B:")
elif marks>60 and marks<=70:
    print("grade A:")
elif marks>70 and marks<=80:
    print("grade A+")
elif marks>80 and marks<=90:
    print("Grade A++:")
elif marks>90 and marks<=100:
    print("Excellent")
else:
    print("Invalid marks")

#__________________________________________________________



# 4 Describe the  interview process
# use nested - if  else statements
round1 = input("enter the round1 result:")
round2 = input("enter the round2 result:")
if round1 == "passed":
    print("Congrats your 1st  round is clear")
if round2 == "passed":
    print("Congrats your 2nd round is clear,you are placed")
elif round1 == "failed":
    print("failed in 1st round ,please try next time")
elif round2 == "failed":
    print("failed in 2nd round, please try next time")
if round1 == round2:
    print(" Congrats ")
else:
   print("not selected")



























































