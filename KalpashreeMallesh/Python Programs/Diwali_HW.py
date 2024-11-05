#T pattern
"""
for row in range (5):
    for col in range(5):
        if row==0 or col==3:
            print("*", end=" ")
        else:
            print("",end="")
    print()

#I pattern
for i in range(7):
    for j in range(5):
        if j==2 or ((i==0 or i==6) and j!=2):
            print("*", end="  ")
        else:
            print(end="")
            print()
"""
#L pattern
for i in range(7):
    for j in range(5):
        if j==0 or (i==6 and j>0):
            print("*", end=" ")
        else:
            print(" ", end=" ")
            print()
#0 Pattern

