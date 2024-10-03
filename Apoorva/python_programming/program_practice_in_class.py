#1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

num1 = 24

if num1%2 == 0:
    print("square value is:",num1**2)
elif num1%3 == 0:
    print("Cube value is:",num1**3)
elif num1%7 == 0:
    print("power to 4 value of number is",num1**4)
else:
    print("number is not divisible 2,3 or 7")