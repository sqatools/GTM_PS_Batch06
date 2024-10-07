# nested loop
"""
-> In nested loop condition for one value of outer loop, entire inner is
   going to execute.
"""
for i in range(5):# i = 0, 1, 2, 3
    print("value i :", i)

    for j in range(3): # j = 0, 1, 2
        print("value of j :", j)

    print("_"*40)


"""
*
* * 
* * *
* * * *
* * * * * 
"""


for i in range(6):
    for j in range(i):
        print("*", end=" ")

    print()

"""
* * * * * 
* * * *
* * *
* *
*
"""
for i in range(6, 0, -1):
    for j in range(i):
        print("*", end=" ")

    print()
