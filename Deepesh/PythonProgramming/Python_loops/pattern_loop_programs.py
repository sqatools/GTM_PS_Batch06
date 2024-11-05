"""
*
* *
* * *
* * * *
* * * * *
"""

for i in range(1, 6): # i = 0
    for j in range(i): # j = 1
        print("*", end=" ")
    print()

"""
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

"""

for i in range(1, 6): # i = 0
    for j in range(i): # j = 1
        print(j, end=" ")
    print()


"""
1
2 3 
4 5 6
7 8 9 10
11 12 13 14 15 
"""
print()
temp =1
for i in range(1, 6): # i = 0
    for j in range(i): # j = 1
        print(temp, end=" ")
        temp += 1
    print()

"""
A
B C
D E F
G H I J
K L M N O
P Q R S T U
"""

# ASCII VALUES
# 65-90  Capital letters
# 97-122 Small letters
print(chr(65)) # A

for i in range(65, 91):
    print(chr(i), end=" ")
"""
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
"""
print()

for i in range(97, 123):
    print(chr(i), end=" ")
"""
a b c d e f g h i j k l m n o p q r s t u v w x y z
"""

# get ascii value from character
print(ord('P'))  # 80

"""
A 
B C 
D E F 
G H I J 
K L M N O 
"""
k = 65
for i in range(1, 6): # i = 0
    for j in range(i): # j = 1
        print(chr(k), end=" ")
        k = k + 1

    print()


"""
A 
B B 
C C C
D D D D 
E E E E E 
"""
k = 65
for i in range(5): # i = 0, k = 65,| i=1, k=66, | i=2, k=67|
    for j in range(i+1): # j = 1| 0, 1 | 0, 1, 2
        print(chr(k), end=" ") # k=65, 66, 67

    print()
    k = k + 1 # 66, 67


print()
print("_"*50)
# write a python program to print a O pattern

"""
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * *  
"""

# part 1:
for i in range(1, 6):
    if i == 1 or i == 5:
        print("-", end=" ")
    else:
        print("*", end=" ")


# part2
print()
for k in range(5):
  for i in range(1, 6):
    if i == 1 or i == 5:
        print("*", end=" ")
    else:
        print("-", end=" ")
  print()

# part 3:
for i in range(1, 6):
    if i == 1 or i == 5:
        print("-", end=" ")
    else:
        print("*", end=" ")


print()
print("_"*50)
####### solution2 ##########
print()


for i in range(1, 8):
    for j in range(1, 6):
        if i == 1 and (j==1 or j == 5):
            print(" ", end=" ")
        elif i == 7 and (j==1 or j == 5):
            print(" ", end=" ")
        elif (1 < i < 7) and (1 < j < 5):
            print(" ", end=" ")
        else:
            print("*", end=" ")
    print()

"""
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * *  
"""