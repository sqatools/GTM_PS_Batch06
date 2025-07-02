#1. write a python program if given number is
# if divisible by 2 then print square of the number
# if divisible by 3 then print cube of the number
# if divisible by 7 then print num**4 of the number

num_a = int(input("Enter the number :"))

if num_a% 2 == 0:
    print("value is divisible by 2 : square of the value = ", num_a** 2)
    if num_a % 3 == 0:
        print("value is divisible by 3 : square of the value = ",
        num_a ** 3)
        if num_a % 7 == 0:
            print("value is divisible by 7 : square of the value = ",
            num_a ** 4)
        else:
            print("The value is not divisible by 7")
    else:
        print("The value is not divisible by 3")
else:
    print("The value is not divisible by 2")