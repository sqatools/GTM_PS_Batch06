"""file = open("readcontent.txt", "r")
data = file.read()
print(data)
file.close()"""

"""def read_file(filepath):
    file = open(filepath, 'r')
    data = file.read()
    print(data)
    file.close()

read_file("readcontent.txt")"""

"""content = "This is China."
file = open("readcontent.txt", "w")
file.write(content)
file.close()"""

"""file = open("readcontent.txt", 'r')
data = file.read()
print(data)
file.close()"""

"""def append_file(filepath):
    file = open(filepath, "a")
    file.write("\nNew line: This is China.")
    file.close()

append_file("readcontent.txt")"""

"""file = open("readcontent.txt", "r")
lines_list = file.readlines()
# To print first 3 lines of content
for i in (lines_list[:3]):
    print(i, end='')

# To print last 3 lines of content
for i in (lines_list[-3:]):
    print(i, end='')"""

email_list = []
file = open("readcontent.txt", "r")
data = file.read()
word_list = data.split()
for word in word_list:
    if '@' in word:
        email_list.append(word)
    else:
        continue

print(email_list)


