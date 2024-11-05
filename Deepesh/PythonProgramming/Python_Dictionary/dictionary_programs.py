# write a python program to create a dictionary from givens string

str1 = "Hello Good Morning, How are you"
# output = {"Hello" : 5, "Good" : 4, "Morning,": 8, "How" : 3, "are" : 3, "you": 3}

word_list = str1.split()
output = {}
for word in word_list:
    word_len = len(word)
    output[word] = word_len

print("Output :", output)


print("_"*50)
# write a python program to create a dictionary from given list

list1 = [4, 7, 9, 12, 6]
#output = {4: 16, 7: 49, 9:81, 12: 144, 6: 36}
output = {}
for val in list1:
    output[val] = val**2

print("output :", output)
# output : {4: 16, 7: 49, 9: 81, 12: 144, 6: 36}


print("_"*50)
# Write a python program to create a dictionary from given list
list1 = [4, 7, 9, 12, 3, 5, 2]
# square of even
# cube of odd
#output =  {4 : 16, 7:343, 9: 729, 12:144,  3:27, 5:125, 2: 4}
output = {}
for val in list1:
    if val%2 == 0:
        output[val] = val**2
    else:
        output[val] = val**3


print("output :", output)

# {4: 16, 7: 343, 9: 729, 12: 144, 3: 27, 5: 125, 2: 4}

# write a python program to create a dictionary to avoid duplicate value from list
# add with cubes

list1 = [6, 8, 2, 6, 1, 5, 7, 8, 7]
#output = {6:216, 8:512, 2:8, 1:1, 5:125, 7:343}

output = {}
for val in list1:
    #if val not in output:
    output[val] = val**3

print("output :", output)

print("_"*50)
# write a python program to solve the below dictionary
dict1= {'Python' : [2, 5, 7],
        'Programming' : (5, 1, 6),
        'Language' : [1, 7, 2]}

# output = {'nythoP' : 14,
#         'grogramminP' : 12,
#         'eanguagL' : 10}

#output : {'nythoP': 14, 'grogramminP': 12, 'eanguagL': 10}

output = {}
for k, v in dict1.items():
    print(k, v)
    updated_key = f"{k[-1]}{k[1:-1]}{k[0]}"
    sum_value = sum(v)
    output[updated_key] = sum_value

print("output :", output)
