
# Q1.  write a python program to combine a list of data with their index and create new list
l1 = (5, 7, 9, 12)
l2 = (10, 40, 50, 60)
l3 = [15, 47, 59, 72]

result = []

for i in range(len(l1)):
   result.append((l1[i],l2[i],l3[i]))
print(tuple(result))

print('#'*50)
# Q3: write a python program to get below result:
# if the value is divisible by 2 then square it else add 'odd' string.
list1 = [3, 6, 8, 9, 1, 4, 7, 2]
#output = ['odd', 36, 64, 'odd', 'odd', 16, 'odd', 4]

res = []
for val in list1:
   if val%2==0:
      res.append(val**2)
   else:
      res.append('odd')
print(res)

