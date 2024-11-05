"""
***** # i = 1
  *   # i = 2
  *
  *
  *
  *
  *  # i = 7
"""

for i in range(0, 7): # i=1
    for j in range(0, 5): # j = 1, 5
        if i == 6:
            print("*", end=" ")
        elif j == 0:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
