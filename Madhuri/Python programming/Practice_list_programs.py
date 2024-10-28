#.Append method (if you want add value)
"""
"""
"""

List_a = [5,7,8,12,16]
List_a.append(100)
print (List_a)
#insert method:- This method helps specic index position and value
List_b = [4,7,12,56,78]
List_b.insert(7,600)
print("List_b:", List_b)
List_b.insert(2, 600)
print("List_b:", List_b)
# Extend Method:- This method add one list data to another list aat the end position
List_c = ['a','b,', 'c']
List_d = [10,30,40,50]
List_d.extend(List_c)
print("list_d:",List_d)
#List Concatenation:- We can add two list with plus operator an dit is doenot modify the original data
List_e =[4,7,9]
list_f = [11,44,77,99]
List_g = List_e+list_f
print("list_g:", List_g)
# List multiplication in this method all this list values wil be repated n number of time
list_h= [4,7,1]
list_i = list_h*5
print("list_i:",list_i)
#remove data in this method specific value from given list
list_j = [4,7,9,22,5,7]
list_j.remove(5)
print("list_j:", list_j)
#pop method:- In this method remove the value from index position and default index position is -1and return thh value as well
list_m = [4,7,12,5,9]
val2 = list_m.pop(3)
print("list_m:", list_m)
# if you not define value last value will be removed example
val3 = list_m.pop
print("removed value:", val2)
# Clear method:- All the data from list and only empty list will be remain
list_o = [6,8,5,4]
list_o.clear()
print("list_0:", list_o)
#Del function: remove entire variable it slf from memory
list_n = [5,7,8,3]
#del list_n
#print("list_n:", list_n)
# remove the some pratial values from list
list_p = [5,2,3,5,8,]
del list_p[1:4]
print("list_p:",list_p)
# replace method
list_q = [4,6,8,22,78]
#replace 4,6 with 14,16
list_q [:2] = [14,16]
print("list_q:", list_q)
# sort method:- it will change accending and descending order
list_s = [5,9,3,2]
list_s.sort()
print("list_s:", list_s)
# sorted function
# this is not modifiy it will give orginal
list_t = [5,7,9,4,]
result= sorted(list_t)
print("accending order:",result)
"""
"""
"""
"""
# write  a python program to remove all duplicate values form list
list1 = [3,6,8,2,3,8,7,10,7]
#output = [3,6,8,2,10,7]
output = list1.copy()
for val in list1:
    val_count = output.count(val)
    print(val,val_count)
    if val_count>1:
        output.remove(val)
        print(output)
        """
"""
list1 = [3,6,8,2,3,8,7,10,7]
result = []
if val2 not in result:
    result.append(val2)
   else:
   continue
  """
"""

list1 = [3,6,8,2,3,8,7,10,7]
for val in  list1:
    print(val)
    if val%3 == 0 and val%4 ==0:
        print(val**2)
    elif val%5 ==0:
        print(val**3)
"""
"""
# write  a python program get max value
list3 = [4,7,8,100,9,12,45]
#max_val = 0
min_val = list3[0]
"""
##for val in list3:
   # print(val)
   # if val>max_val:
       # max_val = val
   # else:
       # continue


"""
for val in list3:
    print(val)
    if val< min_val:
        min_val = val
    else:
        continue
print("min_value:", min_val)
print("min_value:",min_val)
"""
"""
"""
"""
# Squre of all the  number in list
list1 = [3,5,7,1,8]
for val in list1:
    print (val ,":",val**2)
# Using while loop
list2 =[3.5,7,1,8]
count = 0
while count< len(list2):
    print(list2[count],":", list2[count]**2)
    count+=1

# problem to add elements  from list1 to  list2
# using concatenation
list1 = [3,6,7,81,2]
list2 = [11,15,17,13]
Output = list1+list2
print("output:", Output)
# using Extend() method
list1 = [3,6,7,81,2]
list2 = [11,15,17,13]
list1.extend(list2)
print(list1)

# 3) problem  to print the sum of all elements in alist
# using loop
list1 = [2,5,8,0,1]
# creating a varible
var = 0
for value in list1:
    var += value
    print(var)
 # while loop
list1 = [2, 5, 8, 0, 1]
count = 0
total = 0
while count<len(list1):
    total += list1[count]
    count+=1
    print(total)
# sum
list1 = [2,5,8,0,1]
print(sum(list1))
"""
"""
"""
""""
# write a python program to combine a list of data with their index
l1 = [5,7,9,12]
l2 = [10,40,50,60]
l3 = [15,47,59,72]
# l1.append(l2)
# print(l1)
# l1.extend(l3)
# print("l1:",l1)
result =[]
for i in range (len(l1)):
    result.append(l1[i]+l2[i])
    print("result:", result)
# Write a program to get below  result
list1 = [3,6,8,9,1,4,7,2]
for val in list1:
    if val%2 == 0:
  """
"""
# Practice List Programs(27/10)
#5)Problem to find minimum and maximum elements from  a list
# input list
list1 = [23,56,12,89]
#sorting listand index method
list1.sort()
# printing output
print("small number:", list1[0])
print("largest number",list1[-1])
# inbuilt function
print("small number:",min(list1))
print("largest number:", max (list1))
#6)Problems to differentitate even and odd elements from a list
# Input list
list2 = [23,11,78,90,34,55]
# creating empty lists
even= []
odd = []
for val in list2:
    if val %2 == 0:
        even.append(val)
    else:
        odd.append(val)
print("Even number:",even)
print("odd number:",odd)
# 3.Problem to print the sum of all elements in a list
# input list
list = [2,5,8,0,1]
# using sum method
print(sum(list))
# Creating variable
count = 0
total = 0
while count< len(list):
    total += list1[count]
    count += 1
    print(total)
"""
"""
# for loop for sum the all elements
# input list
list3 = [2,5,8,0,1]
# creating a varible
var = 0
for value in list3:
    var += value
print (var)
"""
"""
# 4)Product get all elements in a list
# using for loop
List4 = [3,6,9,2]
# creating a variable
var = 0
for value in List4:
    var *=  value
print(var)
# 7)problem to remove all the duplicate elements from a list
list1 = [5,7,8,2,5,0,7,2]
# creating emepty list
list2 =[]
for value in list1:
    if value not in list2:
        list2.append(value)
print(list2)
list5 = [ 9,7,5,7,9,5,2,6]
list3 =[]
for value in list5:
    if value not in list3:
        list3.append(value)
print(list3)

# 9 problem to print squares of even numbers from a list
list6 = [2,4,7,8,5,1,6]
for val in list6:
    if val%2 == 0:
        print(val,":",val**2)
list3 = [2,4,7,8,5,1,6]
for val in list3:
    if val%3 == 0:
        print(val,":",val**2)
        """
# 10)Problem to spilt the list into two-part
list1 = [5,7,2,8,11,12,17,19,22]
# creating empty list
even =[]
odd = []
for val in list1:
    if val%2==0:
        even.append(val)
        print(val)
    else:
        odd.append(val)
odd.append(even)
print(odd)
# 11 common elements from two lists
list1 = [4,5,7,9,2,1]
list2 = [2,5,8,3,4,7]
# creating empty list
common_list3 =[]
for val in list1:
    if val in list2:
        common_list3.append(val)
print(common_list3)























