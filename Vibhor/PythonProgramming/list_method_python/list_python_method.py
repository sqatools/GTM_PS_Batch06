# insert method is for adding value in any position of the list with indexing.
# append method is for adding the value in the end of the list.
# extend method is for adding the 1 list data to another list at the end (modifying original list).
# list concatenation we can add 2 list with + operator and it does not modify original list.
# list multiplication all the values are repeated n number of times.
# remove method this can remove the specific value in the given list. (1st value if find)
# pop method remove the value from index position and default index is -1
# clear method removes all the data in the list only empty list remain.
# del method removes the entire variable from memory itself. also can remove the given values via slicing.
# replace method replace the value given by index.
# sort method sort the list data in assending and decending order an modify the original list. bydefault accendng
# or (reverse=True) in sort method.
# sorted function does not modify the original list, it can sorted list
# reverse method is reverse the value of list and modify the original value
# reversed function is reverse the value of list but it didnot modify original value.
# count method is count the number of occurences of the gven value in the list
# index method is return the index position of any value in the given list
# shallow copy method we generally assign value from list 1 to another and pass the reference
# of data, if we modify any list that will reflect in other list
# deep copy method we actually copy the content from list 1 to another and if we fo modification
# in list 1 it does not effect another list

# List comprehensing
list_a= [3, 4, 5, 6]
#square of the list
result=[x**2 for x in list_a]
print("Square= :", result)
result2=[val for val in list_a if val%2==0]
print("Even Value :", result2)
result3=[(val,'even') if val%2==0 else (val, 'odd') for val in list_a]
print("result3 :", result3)