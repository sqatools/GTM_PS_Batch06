# 1- Combine list
l1 = (5, 7, 9, 12)
l2 = (10, 40, 50, 600)
l3 = (15, 47, 59, 72)
result = []
for i in range(len(l1)):
    l4 = result.append(l1[i]+l2[i]+l3[i])
print("Result = ", list(result))

print("*"*50)
# 2-
list1 = [3, 7, 9, -1, 2, -5, 6, -8]
output = [3, 7 , 9, -1, -2, -5, -8]
result = []
for val in list1:
    if val > 0:
        result.insert(0, val)
    else:
        result.append(val)
print(result)

print("*"*50)
# 3-
list1 = [3, 6, 8, 9, 1, 4, 7, 2]
result = []
for val in list1:
    if val%2 == 0:
        result.append(val**2)
    else:
        result.append("odd")
print(result)