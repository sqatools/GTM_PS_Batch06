"""str1 = "Rahul Mohit John Rahul Vaibhav John"

word_list = str1.split()
count = {}

for word in word_list:
    if word in count:
        count = count+1
    else:
        count = 1"""

file = open("readcontent.txt", "r")
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

print(max_word)



