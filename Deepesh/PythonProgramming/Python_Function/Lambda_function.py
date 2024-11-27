"""
Lambda function does not have any body
"""
output = lambda x, y: x+y
print(output(40, 50))

# Map , Filter and Reduce

# Map : Map function does mapping of list of input for any specific function

list1 = [4, 6, 8, 12, 68]
result = list(map(lambda x: x**2, list1))
print("square values :", result)
# [16, 36, 64, 144, 4624]

result2 = list(map(lambda x: x%2==0, list1))
print("result2 :", result2)
# [True, True, True, True, True]

# Filter : Filter function return all the values which is in favourable condition
list2 = [4, 6, 87, 23, 45, 67, 12]
filter_result = list(filter(lambda x: x%2 == 0, list2))
print("Filter result :", filter_result) # [4, 6, 12]



# reduce : reduce function provide one single output of given values
from functools import reduce
list3 = [5, 6, 8, 23, 45]
reduce_result = reduce(lambda x, y: x+y, list3)
print("sum of values :", reduce_result) # sum of values : 87

reduce_result2 = reduce(lambda x, y: x*y, list3)
print("multiplication of values :", reduce_result2) # 248400
