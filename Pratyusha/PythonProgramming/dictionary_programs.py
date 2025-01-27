# write a python program to create a dictionary from given string
str1 = "Hello Good Morning, How are you"
# output = {'Hello': 5, 'Good': 4, 'Morning,': 8, 'How': 3, 'are': 3, 'you': 3}

word_list = str1.split()
output = {}
for word in word_list:
    word_len = len(word)
    output[word] = word_len
print(output)

print('_'*50)
# write a python program to create a dictionary of square of each value from list
list1 = [2, 4, 6, 5]
# output = {2: 4, 4: 16, 6: 36, 5: 25}
output = {}
for val in list1:
    output[val] = val**2
print(output)

print('_'*50)
# write a python program to create a dictionary from the given list
# get square of even and cube of odd values from list to dictionary
list2 = [3, 4, 12, 5, 8]
output = {}
for val in list2:
    if val%2 == 0:
        output[val] = val**2
    else:
        output[val] = val**3
print(output)


print('_'*50)
# write a python program to create a dictionary by remove duplicates from the given list and get cube of uniques
list3 = [6, 8, 2, 6, 1, 5, 7, 8, 7]
# output = {6: 108, 8: 512, 2: 8, 1: 1, 5: 125, 7: 343}
output = {}
for val in list3:
    """if val not in output:
        output[val] = val**3"""
    output[val] = val**3    # if key is duplicate, it overrides with latest key:value pair in dictionary
print(output)

print('_'*50)
# write a python program to solve the below dictionary
dict1 = {'Python' : [2, 5, 7],
        'Programming' : (5, 1, 6),
        'Language' : [1, 7, 2]}

# output = {'nythoP' : 14,
#         'grogramminP' : 12,
#         'eanguagL' : 10}
output = {}
for k, v in dict1.items():
    print(k, v)
    updated_key = f"{k[-1]}{k[1:-1]}{k[0]}"
    val_sum = sum(v)
    output[updated_key] = val_sum
print(output)






# https://sqatools.in/python-dictionary-programs/
