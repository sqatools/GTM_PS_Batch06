"""
# 25) Problem to remove element from the list using pop method
list1 = [33,56,89,12,45]
# removing an element whose index is 2 using pop method
list1.pop(2)
print(list1)
# 24 problemto sort a list using the sort and sorted method
list2 = [23,11,78,45,33]
#using sort method
list2.sort()
print("by sort function:",list2)
#using sorted method
print("by sorted method:",list2)

#23 problem to add two list using extend method
list3 = [2,4,6,8,1]
list4= [23,56,11,89]
# combining lists
list3.extend(list4)
print(list3)

# 22 problems to get a list of words which has vowels in
string = "www student ppp are qqqq learning python vvv"
#splitting a string
string2 = string.split()
list5 =[]
for words in string2:
    for char in words:
        if char == "a" or char =="e" or char =="i" or char =="o" or char =="u":
                 list5.append(words)
        break
    print(list5)

# 21 problem to check weather the list is plaindrome or not
 list1 = [2,4,6,6,4,2]
list2 = list1[::-1]
if list1 == list2:
    print("list is palindrome")
else:
    print("list is not palindrome")
"""
"""
#20 python program to get a list of allelements which are divided by 3 and 7
list1 = [3,7,0,2,6,14,88,21]
list2 =[]
for value in list1:
    if value% 3 == 0 or value% 7 ==0:
        list2.append(value)
        print(value)
 # 19 problem to remove negative elements from the list
list1 = [3,5,-8,0,-20,-55]
#for value in list1:
       # if value >=0:
          #print(value,end=" ")
for value in list1:
    if value<=0:
        print(value,end="-")
# 18
#17 python program to return true if two lists have any common member
list1 = [2,4,7,8,3]
list2 =[4,5,0]
for value in list1:
    if value in list2:
        print("true")
 #16 problem to copy the list to another list
list1 =[ 1,2,4,7,0,5]
list2 =[]
for value in list1:
    list2.append(value)
    print(list2)

# 15problem to reverse  a list with reversed and revrese methods
list1 = [2,3,7,9,3,1]
print("using reversed:", list(reversed(list1)))
list1.reverse()
print("using reverse:",list1)
# 14 problem to print list in reverse order using index slicing
list1 = [2,4,6,8]
list2 = list1[::-1]
print(list2)
# 13 python program to reverse a list with a while loop
# 12 problem to print the list in reverse order using for loop
list1 =[1,2,3,4,55]
for i in range(len(list1)-1,-1,-1):
    print(list1[i],end=" ")
#11 python program to get common elments from two lists
list1 = [4,5,7,9,2,1]
list2 = [2,5,8,3,4,7]
list3 =[]
for value in list1:
    if value in list2:
        list3.append(value)
        print(list3)
#10 problem to split the list into two-part
list1 = [5,7,2,8,11,12,17,19,22]
odd= []
even= []
for value in list1:
    if value%2 == 0:
        even.append(value)
    else:
        odd.append(value)
# 9 python program to print squre of all even number is a 
 list1 = [2,4,7,8,5,1,6]
for value in list1:
     if value%2 == 0:
       print (value,": " ,value**2)
# 8 python program to  print a combination of 2 elements from the list whose sum is 10
"""
"""
# 7 python program to remove all duplicate  elements from the list
list1 = [5,7,8,2,5,0,7,2]
list2=[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)
# 6 python program to differentitate  even odd elements from the given list
list1 = [23,11,78,90,34,55]
odd = []
even = []
for value in list1:
    if value%2 == 0:
        even.append(value)
    else:
        odd.append(value)
print("even number:",even)
print("odd number:",odd)
# 5 python program to find the minimum and maximum  elements from the list
list1 = [23,56,12,89]
list1.sort()
print(list1)
print("smallest number:",list[0])
print("largest number:",list[-1])
print("smallest number:",min(list1))
print("largest number:",max(list1))
# 4 problem to get product of all elements  in a list
# 3 problem to print the sum of all elements in a list
list1 =[ 2,5,8,0,1]
print(sum(list1))
#2 problem to add elements from list1 to list2
list1 = [3,6,7,81,2]
list2 = [11,15,17,13]
output = list1+list2
print(output)
#using extend method
list1.extend(list2)
print(list1)
# problem to get the squre of all numbers in the python list
list1 =[3,5,7,1,8]
for val in list1:
    print(val,":",val**2)
 # while loop method
 count = 0
while count<len(list1):
    print(list1[count],":",list1[count]**2)
    count+=1
"""
"""
# T patten
#This for loop section will print 2 horizontal lines.
for i in range(3):
    for j in range(9):
      print("*",end=" ")
    print()
# this for loopsection will print vertical line of t pattern
for i in range(5):
    for j in range(9):
        if j>2 and j<6:
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""
"""
# I pattern
for row in range(7):
    for col in range (5):
        if (row in{0,6}):
                print('*',end= ' ')
        elif (row in{1,2,3,4,5}) and (col == 2):
            print('*',end=' ')
        else:
            print('',end= '')
        print()
"""
"""
# o pattern
for i in range(0,7):
  for j in range(0,7):
      if (i ==0 or i==6)and (1< j <5):
          print("*",end=" ")
      elif (0<i<=5) and (j==1 or j==5):
          print("*",end="   ")
      else:
          print("",end="  ")

  print()
"""
# l pattern
for i in range(7):
    for j in range (5):
        if j==0 or (i==6 and j>0):
         print("*",end=" ")
        else:
          print("*",end=" ")
    print()




