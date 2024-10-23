list_A = [4, 7, 2, 8, 12]
print("Index of 8 :", list_A.index(8))

for i, x in enumerate(list_A):
#   print(f"Value {x} is at index {i}")
    print("Value {} is at index {}".format(x, i))


for index, value in enumerate(list_A):
    print(index, value)

# List Comprehension
# get even value from list
list_a = [6, 7, 1, 2, 13, 14, 16]
print(list_a)
result = [x for x in list_a if x%2 == 0]
print("list_a even :", result) # list_a even : [6, 2, 14, 16]

# get square for the list elements
result1 = [x**2 for x in list_a]
print("Square of values in list_a: ", result1) # Square of values in list_a:  [36, 49, 1, 4, 169, 196, 256]

list_b = [1, 4, 8, 3, 5, 7]
# get max, min, sum values from list
print("max value :", max(list_b))
print("min value :", min(list_b))
print("sum of values :", sum(list_b))
print("average of values :", sum(list_b)//len(list_b))

# max value : 8
# min value : 1
# sum of values : 28
# average of values : 4

list_a = [5, 7, 8, 12, 6]
list_a.append(100)
print(list_a)

list_a.insert(2, 500)
print(list_a) # [5, 7, 500, 8, 12, 6, 100]

list_a = [5, 7, 8, 12, 6]
list_b = [3,4]
# list_b.extend(list_a)
# print(list_b) # [3, 4, 5, 7, 8, 12, 6]

# list_a.extend(list_b)
# print(list_a) # [5, 7, 8, 12, 6, 3, 4, 5, 7, 8, 12, 6]

# concatenation
"""
list_a + list_b
list_c = list_a + list_b
print(list_c) # [5, 7, 8, 12, 6, 3, 4]

"""
# multiply
list_d = list_a * 5
print(list_d) # [5, 7, 8, 12, 6, 5, 7, 8, 12, 6, 5, 7, 8, 12, 6, 5, 7, 8, 12, 6, 5, 7, 8, 12, 6]

"""
list_o = [4, 7, 9, 22, 5, 7]
# list_o.remove(7)
output = list_o.remove(22)
print("list_o :", output)

"""
list_e = [8, 5, 4, 6, 2]
# list_e.pop()
# print(list_e)

# val = list_e.pop()
# print(val) # will remove the last value

list_e.clear()
print(list_e)  # []

# replace using slicing

list_f = [2, 4, 6, 8, 10]
# list_f[:3] = [12, 14, 16]  # :3 index goes 0 1 2
# print("list_f :", list_f) # list_f : [12, 14, 16, 8, 10]
# list_f[3] = 9
# print(list_f)
















