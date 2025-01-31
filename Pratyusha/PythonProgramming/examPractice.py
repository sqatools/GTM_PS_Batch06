"""str1 = "Rahul Mohit John Rahul Vaibhav John"

word_list = str1.split()
count = {}

for word in word_list:
    if word in count:
        count = count+1
    else:
        count = 1"""

"""file = open("readcontent.txt", "r")
file_data = file.read()
max_word = ''
max_len = 0
word_list = file_data.split()
for word in word_list:
    if len(word) > max_len:
        max_len = len(word)
        max_word = word
    else:
        continue

print(max_word)"""

"""list = [2, -16, 6, 44, -71, 18, -11, -1]
output_list1 = []
output_list2 = []
for i in list:
    if i > 0:
        output_list1.append(i)
    elif i < 0:
        output_list2.append(i)

print(output_list1+output_list2)"""

Dict1 = {'x': 10, 'y': 20, 'c': 50, 'f': 44 }
Dict2 = {'x': 60, 'c': 25, 'y': 56}

list1 = [("mike",1),("sarah",20),("jim", 16)]
dict1 = {}
for val in list1:
    dict1[val[0]] = val[1]

print(dict1)


