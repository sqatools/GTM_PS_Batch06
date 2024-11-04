#d). L Pattern

for row in range(7):
    for col in range(7):
        if col == 0 or row == 6:
            print("*", end=" ")
    print()

print("*"*50)
#I Pattern
for row in range(7):
    for col in range(7):
        if row == 0 or row == 6 or col == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print("*"*50)
#T Pattern

for row in range(7):
    for col in range(7):
        if row == 0 or col == 3:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("*"*50)

# O Pattern
for row in range(0, 7):
        for column in range(0, 7):
            # here in first and last row we want to three *
            if (row == 0 or row == 6) and (1 < column < 5) :
                print("*", end=' ')
            # here from 2 to 6 row, * will print on 1 and 5 index only.
            elif (0 < row <= 5) and (column ==1 or column ==5):
                print("*", end=' ')
            else:
                print(" ", end=' ')
        print()


