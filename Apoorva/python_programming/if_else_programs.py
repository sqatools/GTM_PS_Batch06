#1. Python program to check given number is divided by 3 or not.

num1 = float(input("enter the number:"))

if num1%3 == 0:
    print("number is divisible by 3:", num1)
else:
    print("number is not divisible by 3:")

#3.  If else program to assign grades as per total marks.
#marks > 40: Fail
#marks 40 – 50: grade C
#marks 50 – 60: grade B
#marks 60 – 70: grade A
#marks 70 – 80: grade A+
#marks 80 – 90: grade A++
#marks 90 – 100: grade Excellent
#marks > 100: Invalid marks

total_marks = float(input("enter the total marks scored:"))

if   total_marks <40:
    print("Fail")
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
    print("Invalid marks: Please enter valid marks")
