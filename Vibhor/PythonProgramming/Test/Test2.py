'''
num = int(input("Enter the Number: "))
if num%3 ==0:
    print("Square of number= ", num**2)
elif num%7 ==0:
    print("Cube of the Number =", num**3)

print("*"*50)

num = int(input("Enter the number= "))
fact = 1
if(num%3 ==0):
    for i in range(num,1,-1):
        fact = fact * i
        print("factorial of a no.=", fact)
else:
    print("Number is not Divisible by 3")

print("*"*50)
print("Print Prime Number")
for num in range(1,50):
    prime=True
    for i in range(2,num):
        if num%i== 0:
            prime=False
    if prime:
        print(num,end=' ')

print("*"*50)
num=int(input("Enter the Number= "))
if num%6==0 and num==36:
    print("Number is square of 6")
else:
    print("Number is not square  of 6")
'''

