list1= [3,6,8,9,1,4,7,2]

result = []

for val in list1:
    if val%2 == 0:
        result.append(val**2)
    else:
        result.append('odd')

print(result)


