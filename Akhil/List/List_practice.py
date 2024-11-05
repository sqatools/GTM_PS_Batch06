# 25). Python program to remove data from the list from a specific index using the pop method.


List_1 = [1, 2, 3, 4, 5, 6]
removed_data = List_1.pop(1)
print(removed_data)
print(List_1)
print("-" * 50)

# 26). Python program to get the max, min, and sum of the list using in-built functions.


List_1 = [1, 2, 3, 4, 5, 6]
print("minimum of the list: ", min(List_1))
print("minimum of the list: ", max(List_1))
print("minimum of the list: ", sum(List_1))

# 27).  Python program to check whether a list contains a sublist.


List_1 = [64, 78, 90, 12, 34, 65]
List_2 = [78, 90, 65, ]
count = 0

for Value in List_1:
    for ele in List_2:
        if Value == ele:
            count = count + 1
print(count)

if len(List_1) == count:
    print("sublist exists")
else:
    print("sublist does not exists")

#  28). Python program to generate all sublists with 5 or more elements in it from the given list.


from itertools import combinations

List_1 = [1, 5, 7, 9, 10, 12]
List_2 = []

for i in range(1, len(List_1) + 1):
    for sub_data in combinations(List_1, i):
        sub_list = list(sub_data)
        if len(sub_list) > 4:
            List_2.append(sub_list)

print(List_2)

# 29). Python program to find the second largest number from the list.


List_1 = [23, 45, 67, 12, 43, 13, 17]
List_1.sort()
print(List_1)
print("Second Largest number is: ", List_1[-2])

# 30. Python program to find the second smallest number from the list.
print("Second smallest number is: ", List_1[1])

# 31). Python program to merge all elements of the list in a single entity using a special character.

List_2 = ["1", "2", "3", "4"]
result = "$".join(List_2)
print(result)
print(type(result))

# 32. Python program to get the difference between two lists.

List_1 = [1, 6, 4, 55, 2, 89, 77, 12]
List_2 = [1, 6, 4, 2]

for value in List_1:
    if value not in List_2:
        print(value, end=" ")

# 33.  Python program to reverse each element of the list.
# Input = [‘Sqa’, ‘Tools’, ‘Online’, ‘Learning’, ‘Platform’]
# output = [‘aqS’, ‘slooT’, ‘enilno’, ‘gninraeL’, ‘mroftalP’]
List_1 = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
result = []
for value in List_1:
    value_reverse = value[::-1]
    result.append(value_reverse)
print(result)

'''
34). Python program to combine two list elements as a sublist in a list.
list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
Output = [[3, 1], [5, 4], [7, 3], [8, 6], [9, 2]]
'''
list1 = [3, 5, 7, 8, 9]
list2 = [1, 4, 3, 6, 2]
result = []
x = zip(list1, list2)
print(list(x))

# 35.
'''
35). Python program to get keys and values from the list of dictionaries.
Input : [{‘a’:12}, {‘b’: 34}, {‘c’: 23}, {‘d’: 11}, {‘e’: 15}]
Output :  [‘a’, ‘b’, ‘c’, ‘d’, ‘c’]
                [12, 34, 23, 11, 15]

'''
List_1 = [{'a': 12}, {'b': 3.4}, {'c': 23}, {'d': 11}, {'e': 15}]

Key = []
Value = []

for dict_1 in List_1:
    print(dict_1)
    for key_1, value_1 in dict_1.items():
        Key.append(key_1)
        Value.append(value_1)
print("Key", Key)
print("Value", Value)

# 36. Python program to get all the unique numbers in the list.

List_1 = [1, 2, 3, 4, 5, 1, 2, 3, 4]
print(list(set(List_1)))

# 37. 37). Python program to convert a string into a list.

string_1 = "Akhil"
List_1 = list(string_1)
print(List_1)

string_2 = "i am learning python"
list1 = string_2.split(" ")
print(list1)

'''

38). Python program to replace the last and the first number of the list with the word.
Input: [12, 32, 33, 5, 4, 7]
output : [‘SQA’, 32, 33, 5, 4, ‘Tools’]

'''

list1 = [12, 32, 33, 5, 4, 7]
list1[0] = "Akhil"
list1[-1] = "Kumar"
print(list1)

'''
39.
39). Python program to check whether the given element is exist in the list or not.

'''

list1 = [22, 45, 67, 11, 90, 67]
print("is 17 data is present in the list?", 17 in list1)
print("is 45 data is present in the list?", 45 in list1)

'''


40). Python program to remove all odd index elements.
Input: [12, 32, 33, 5, 4, 7, 33]
Output: [12,33,4,33]

'''

list_1 = [12, 32, 33, 5, 4, 7, 88]
result = []

for i in range(0, len(list_1)):
    if i % 2 == 0:
        print(i)
        result.append(list_1[i])
print(result)

'''
41). Python program to take two lists and return true if then at least one common member.


'''
list1 = [25, 65, 77, 14, 23, 96]
list2 = [65, 35, 62, 77]
count = 0
for list1_value in list1:
    for list2_value in list2:
        if list1_value == list2_value:
            count = count + 1
if count > 0:
    print("have common member")
else:
    print("does not have common member")

'''


42). Python program to convert multiple numbers from a list into a single number.
Input: [12, 45, 56]
Output:124556

'''
list1 = [12, 45, 56]
for value in list1:
    print(value, end='')

print()
'''

43). Python program to convert words of a list into a single string.
Input: [‘Sqa’, ‘Tools’, ‘Best’, ‘Learning’, ‘Platform’]
Output: SqaToolsBestLearningPlatform

'''

string_1 = ['Sqa', 'Tools', 'Best', 'Learning', 'Platform']

for string1 in string_1:
    print(string1, end='')
print()
'''


44). Python program to print elements of the list separately.
Input: [(‘Black’, ‘Yellow’, ‘Blue’), (50, 55, 60), (30.0, 50.5, 55.66)]
Output:
(‘Black’, ‘Yellow’, ‘Blue’)
(50, 55, 60)
(30.0, 50.5, 55.66)


'''

List1 = [('Black', 'Yellow', 'Blue'), (50, 55, 60), (30.0, 50.5, 55.66)]
for value in List1:
    print(value)

'''

45). Python program to create a sublist of numbers and their squares from 1 to 10.
Output : [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]
'''
Result = []
for i in range(1, 11):
    val = [i, i ** 2]
    Result.append(val)
print(Result)

'''

46). Python program to create a list of five consecutive numbers in the list.
Output : [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]


'''
Result = []
sub_list = []

for i in range(0, 4):
    for j in range(1, 6):
        val = 5 * i + j
        sub_list.append(val)
    Result.append(sub_list)
    sub_list = []
print(Result)

'''

47). Python program to insert a given string at the beginning of all items in a list.
Input: [1, 2, 3, 4, 5], Sqa
Output: [‘Sqa1’, ‘Sqa2’, ‘Sqa3’, ‘Sqa4’, ‘Sqa5’]



'''
List_1 = [1, 2, 3, 4, 5]

Result = ["sqa{}".format(i) for i in List_1]
print(Result)

'''



49).  Python program to move all positive numbers on the left side and negative numbers on the right side.
Input: [2, -4, 6, 44, -7, 8, -1, -10]
Output: [2, 6, 44, 8, -4, -7, -1, -10]


'''
Postive_List = []
Negative_List = []
list_1 = [2, -4, 6, 44, -7, 8, -1, -10]
for val in list_1:
    if val > 0:
        Postive_List.append(val)
    else:
        Negative_List.append(val)
print(Postive_List)
print(Negative_List)
Postive_List.extend(Negative_List)
print(Postive_List)

'''



50). Python program to move all zero digits to the end of a given list of numbers.
Input: [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
Output: [3, 4, 6, 4, 22, 3, 21, 0, 0, 0, 0, 0, 0, 0, 0]


'''

'''


51). Python program to find the list in a list of lists whose sum of elements is the highest.
Input: [[11, 2, 3], [4, 15, 6], [10, 11, 12], [7 8, 19]]
Output: [7, 8, 19]

'''

List_1 = [[11, 2, 3], [4, 15, 6], [10, 11, 12], [7, 8, 19]]

print(max(List_1, key=sum))

'''



52). Python program to find the items that start with a specific character from a given list.
Input: [‘abbcd’, ‘ppq, ‘abdd’, ‘agr’, ‘bhr’, ‘sqqa’, tools, ‘bgr’]

# item starts with a from the given list.
[‘abbcd’, ‘abdd’, ‘agr’]

# item starts with b from the given list.
[‘bhr’, ‘bgr’]

# item starts with c from the given list.
[]

'''

List_1 = ['abbcd', 'ppq', 'abdd', 'agr', 'bhr', 'sqqa', 'tools', 'bgr']

List_a = []
List_b = []
List_c = []

for word in List_1:
    if word[0] == "a":
        List_a.append(word)
    elif word[0] == "b":
        List_b.append(word)
    elif word[0] == "c":
        List_c.append(word)
print(List_a)
print(List_b)
print(List_c)




































