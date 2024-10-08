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
