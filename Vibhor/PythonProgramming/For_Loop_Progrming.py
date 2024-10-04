print("'Find numbers divisible by a certain number 5 and 7'")
for i in range(1500, 1601):
    if i%5 == 0 and i%7 == 0:
        print(i, end=' ')

print("*"*50)

print("'Even number'")
for i in range(21):
    if i%2 == 0:
        print(i, end=' ')

print("*"*50)

print("Prime number")

num= int(input("Enter the Number: "))
prime=True
for i in range(2,num):
    if num%i ==0:
        print(i, end=' ')
        prime = False
    else:
        pass

if prime:
    print("This is Prime Number:", num)
else:
    print("This is not Prime Number:", num)