# print(dir(list))
"""
'append', 'clear', 'copy', 'count',
'extend', 'index', 'insert', 'pop',
'remove', 'reverse', 'sort'
"""

list1 = [3, 4, 'Good', 45, 7, 43]
list1.append(5)
list1.append('Hello')
list1.append(4.5)
print(list1)
list1.clear()
# print(list1)
del list1
# print(list1)

print('_'*50)
list1 = [4, 6, 'Good', 3.5, True, [5, 4, 3]]
# Shallow copy
list2 = list1
list2.append('Python')
print("list1: ", list1)
print("list2: ", list2)

# Deep copy
list3 = list1.copy()
list3.append('Programming')
print("list3: ", list3)

print('_'*50)
list4 = [3, 4, 5, 2, 3, 6, 4, 7, 8, 1, 2, 3]
count_of_2 = list4.count(2)
print(count_of_2)
print(list4.count(3))

print('_'*50)
list5 = [2, 'Python', 'Programming', 5, 2.5, True]
list6 = [[3, 4.3, 2], (2, 3, 4)]
print(list6)
list5.extend(list6)
print(list5)

print('_'*50)
list5 = [2, 'Python', 'Programming', 5, 2.5, True, [3, 4.3, 2], (2, 3, 4)]
print(list5.index(True))
print(list5.index(3, 4.3, 2))
