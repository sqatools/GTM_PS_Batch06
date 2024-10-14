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

print("*"*50)
print("Print the Pattern")
for i in range(4):
    for j in range(i):
        print(j,end=' ')
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(j,end=' ')
    print()

print("*"*50)
print("Print the Average")
num=[10,11,12,13,14]
avg=sum(num)/len(num)
print("Average of numbers= ", avg)

print("*"*50)
print("Check the number is Palindrome or not")
num=n=int(input("Enter a number: "))
rev = 0
while n>0:
    r = n%10
    rev = (rev*10) + r
    n = n//10
print("Reverse number: ",rev)
if num == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

print("*"*50)
print("'Square if Even and Cube if Odd inn given List'")
list1=[10,13,6,7,17,3,8,19]
for val in list1:
    if val%2 ==0:
        print("Square of the number= ", val**2)
    else:
        print("Cube of the number= ", val**3)


print("*"*50)
print("'Length of string'")
str=input("Enter the String= ")
if len(str)%2==0:
    print(str*5)
else:
    print(str*7)
'''