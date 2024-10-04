print("'Grade'")
marks= int(input("Enter the Marks Obtain by Student: "))
if marks <40:
    print("Fail")
elif marks >=40 and marks <50:
    print("GradecC")
elif marks >=50 and marks <60:
    print("Grade B")
elif marks >=60 and marks <70:
    print("Grade A")
elif marks >=70 and marks <80:
    print("Grade A+")
elif marks >=80 and marks <90:
    print("Grade A++")
elif marks >=90 and marks ==100:
    print("Excellent")
elif marks >100:
    print("Invalid")

print("*" *50)
print("'Divisible by 3 or not'")

num = int(input("Enter the number: "))
if num%3 ==0:
    print("Number is divisible by 3")
else:
    print("Number is not divisible by 3")

print("*" *50)
print("'Divisible by 3 and 5 or not'")

num = int(input("Enter the number: "))
if num%3 ==0 and num%5 ==0:
    print("Number is divisible by 3 and 5")
else:
    print("Number is not divisible by 3 and 5")

print("*" *50)
print("'Divisible by 11 and square'")

num = int(input("Enter the number: "))
if num%11 ==0 :
    print(num**2)
else:
    print("Number is not divisible by 11")

print("*" *50)
print("'Even or ODD'")

num = int(input("Enter the Number: "))
if num%2 ==0:
    print("Number is Even")
else:
    print("Number is ODD")

print("*" *50)
print("'Exam Result'")

round1 = input("Enter round1 Result: ")
round2 = input("Enter round2 Result: ")
if round1 == "Passed":
    print("You Cleared the 1st Round of Interview")
else:
    print("1st Round is not Cleared 'Try Next Year'")
if round2 == "Passed":
    print("You Cleared all the Round and You are Placed")
else:
    print("2nd Round is not cleared 'Try Next Year'")

print("*" *50)

print("'Voter's Eligibility'")

Age = int(input("Enter the Candidate Age: "))
if Age >=18:
    print("Candidate is Eligible")
else:
    print("Candidate is not Eligible")

print("*" *50)
print("Number divisible by 2,3 and 7 and do Sqare, Cube and Quadra")

num = int(input("Enter the number: "))
if num%2 ==0 :
    print("Square if the Value= ", num**2)
elif num%3 ==0:
    print("Cube if the Value= ", num**3)
elif num%7 ==0:
    print("Quadra if the Value= ", num**4)
else:
    print("Invalid Number")

print("*" *50)

print("Create a Calculator")

num1=int(input("Enter the Value of 1st  Number="))
num2=int(input("Enter the Value of 2nd  Number="))
num3=int(input("Enter the Value of 3rd  Number="))
if num1 == 1:
    print("Addition=", num2+num3)
elif num1 ==2:
    print("Multiplication=", num2*num3)
elif num1 ==3:
    print("Division=", num2%num3)
elif num1 ==4:
    print("Substraction=",num2-num3)
else:
    print("Invalid Action")
