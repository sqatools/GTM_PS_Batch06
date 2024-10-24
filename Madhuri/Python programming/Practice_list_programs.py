#.Append method (if you want add value)
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

