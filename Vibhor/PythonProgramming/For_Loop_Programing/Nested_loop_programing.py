for i in range(5):
    print("value of i :", i)
    for j in range(3):
        print("Value of j :", j)
    print("*"*40)

for i in range(5):
    for j in range(i):
        print("*",end=' ')
    print()
for i in range(5,0,-1):
    for j in range(i):
        print("*",end=' ')
    print()

print("*"*50)

tup_val=(4,23,5,7,3,4,12,55,67,66)
odd_count=0
even_count=0
for val in tup_val:
    if val%2 ==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print("Odd count= ", odd_count)
print("Even count= ",even_count)

print("*"*50)

a=0
b=1
for _ in range(10):
    print(a, end=' ')
    a,b= b, a+b
