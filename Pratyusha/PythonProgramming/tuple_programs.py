# write a program to find out all the values which are even in the tuple
"""tup_a = (3, 7, 12, 8, 10)
for val in tup_a:
    if val%2 == 0:
        print(val)
    else:
        continue"""

# write a python program to get a max. value from the given tuple
"""tup_b = (4, 7, 12, 55, 77, 23, 56)
max_val = 0
for i in tup_b:
    if i > max_val:
        max_val = i
    else:
        continue
print(max_val)"""

# write a python program to remove all duplicates from given tuple
tup_c = (3, 4, 4, 5, 3, 6, 7, 8, 7)
output = []
for val in tup_c:
    if val not in output:
        output.append(val)
    else:
        continue
print(output)
