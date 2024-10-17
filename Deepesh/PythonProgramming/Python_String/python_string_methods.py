print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode',
 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 
 'isdigit', 'isidentifier', 'islower', 'isnumeric',
  'isprintable', 'isspace', 'istitle', 'isupper', 'join', 
  'ljust', 'lower', 'lstrip', 'maketrans', 'partition',
   'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
    'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
    'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper',
     'zfill'
"""
######
# lower() and upper() Method:

str_a = "Hello Good Morning"
print(str_a.lower())  # hello good morning
print(str_a.upper())  # HELLO GOOD MORNING

# isupper() and islower() : These methods check the given string in upper case
#                    or lower case.

str_b = "PYTHON"
str_c = "programming"
str_d = "Language"
print("str_b :", str_b.isupper())  # True
print("str_c :", str_c.islower())  # True
print("str_d :", str_d.isupper())  # False
print("str_d :", str_d.islower())  # False

#######
# swapcase() method : This method convert all upper case character to lower, and
#  lower case character to upper case.

str_e = "LearNing PyThon ProgRamminG"
print("str_e :", str_e.swapcase())  # lEARnING pYtHON pROGrAMMINg

#######
# title() method: This method convert first character of each word into camel case.
str_f = "LearNing PyThon ProgRamminG"
print(str_f.title())  # Learning Python Programming

str_g = "Hello Good Morning"
str_h = "GooD Evening"
print("str_g :", str_g.istitle())  # True
print("str_h :", str_f.istitle())  # False

print("_" * 50)
##########
# count() method : This method count the repeatation of any char/substring in given string

str_k = "We are Learning Python Programming"
print("count of e:", str_k.count('e'))  # 3
print("count of ing:", str_k.count('ing'))  # 2
print("count of space:", str_k.count(' '))  # 4

print("_" * 50)
##########
# index method() : This method return the index position of any char/substring in given string
str_l = "We are Learning Python Programming"
print("index position of L:", str_l.index('L'))  # 7
print("index position of Python:", str_l.index('Python'))  # 16
print("index position of e:", str_l.index('e'))  # 1

# if the target character or substring is not available, then it will through error
# print("index position of W:", str_l.index('A')) # 1
# ValueError: substring not found


print("_" * 50)
##########
# find() method: This method look for any char/substring and return index position
# if target char/substring is not available then it will return -1

str_x = "We are Learning Python Programming"
print("find index of Py :", str_x.find("Py"))  # 16

# Hello is not available in the string, it will return -1
print("find index of Hello :", str_x.find("Hello"))  # -1

print("_" * 50)
##########
# replace() method:  This method replace any char/substring from given string.

str_y = "Java is Best Programming Language Java"
result = str_y.replace("Java", "Python")
print("result :", result)
print("str_y :", str_y)

result2 = str_y.replace("Java", "JAVASCRIPT").replace("Best", "Famous")
print("Result2 :", result2)
# JAVASCRIPT is Famous Programming Language JAVASCRIPT

result3 = str_y.replace("Java", "JAVASCRIPT").replace("Best", "Famous").lower()
print("Result3 :", result3)
# javascript is famous programming language javascript


print("_" * 50)
########################
# split() method: This method split given string from given delimeter (, . | # char)
# and return list of words

str_z = "Java is Best Programming Language Java"
str_s = "Java,is,Best,Programming,Language,Java"

str_z_list = str_z.split(" ")
print("str_z list of words :", str_z_list)
#  ['Java', 'is', 'Best', 'Programming', 'Language', 'Java']

str_s_list = str_s.split(",")
print("str_s list of words :", str_s_list)
# ['Java', 'is', 'Best', 'Programming', 'Language', 'Java']

str_s_list2 = str_s.split("a")
print("word list3 :", str_s_list2)

url = "https://www.google.co.in"
split_url = url.split(".")
print(split_url)
print("www output :", split_url[0].split("//")[1])  # www
print("https output :", split_url[0].split("//")[0])  # https:

print("_" * 50)
# Write a python to replace first Java word with Python and second Java with C#
str_p = "Java is Best Programming Language Java"
word_list = str_p.split(" ")
print(word_list)
# ['Java', 'is', 'Best', 'Programming', 'Language', 'Java']
output = ''
count = 0
for word in word_list:  # Java, is Best
    # print(word)
    if word == 'Java':
        count += 1  # 1, 2
        if count == 1:
            output = output + 'Python' + " "
            # ouptut = ''+Python+" " = 'Python '
        elif count == 2:
            output = output + 'C#' + " "
            # 'Python is Best Programming Language  C#'
    else:
        output = output + word + " "
        # output = 'Python is Best Programming Language'

print("java count :", count)
print("output :", output)

print("_" * 40)
# Q2 . write a python program to remove all the vowels
str2 = "Hello Good Morning, Hope You are Doing Good"
vowels = "aeiou"
result = ''

for char in str2:
    if char in vowels:
        continue
    else:
        result = result + char

print("Result :", result)

# q1 : Write a program to replace any specific word without using replace method.
# q2 : Write a program to get count any specific word/substring without using count method.

print("_" * 50)
# q1 : Write a program to replace any specific word without using replace method.
str1 = "Diwali Lets celebrate Diwali 2024"
src_w = 'Diwali'
new_word = 'Holi'
result = ""
word_list = str1.split(" ")
for word in word_list:
    if word == src_w:
        result = result + new_word + " "
    else:
        result = result + word + " "

print("Result :", result)

print("_" * 50)
# q2 : Write a program to get count any specific word/substring without using count method.
str2 = "Diwali Lets celebrate Diwali 2024 Diwali"
word_list = str2.split(" ")
count = 0
chk_word = 'Diwali'

for word in word_list:
    if word == chk_word:
        count += 1
    else:
        continue

print(f"count of {chk_word}: {count}")

print("_" * 40)
###########
# strip() method: This remove trailing space from given, it means, it removes all prefix and
# end spaces from given string

str_a = "  Good Morning  "
print(str_a)
result1 = str_a.strip()
print(result1)

# rstrip method : This remove right side space from given string
rstrip_result = str_a.rstrip()
print(rstrip_result)

# lstrip method : This remove left side space from given string
lstrip_result = str_a.lstrip()
print(lstrip_result)

print("_" * 40)
#################
# join() method : This method join the given string with delimiters/substring/char

str_A = "Python Programming"

result = "_".join(str_A)
print("result :", result)  # P_y_t_h_o_n_ _P_r_o_g_r_a_m_m_i_n_g

result2 = "^&^*&".join(str_A)
print("result2 :", result2)
actual = result2.replace("^&^*&", "")
print("actual string :", actual)  # Python Programming

############
#  rsplit method() :

str2 = "Good Evening How are you"
result = str2.rsplit(" ")
print("result :", result)

print("_" * 50)
#####################
# isnumeric method(): This method check given string in only contains number or not

s1 = "h12345"
print("s1 is numeric :", s1.isnumeric())  # False
s2 = "56456450"
print("s2 is numeric :", s2.isnumeric())  # True

s3 = "56456450 54654654"
print("s3 is numeric :", s3.isnumeric())  # False

print("_" * 50)
#####################
# isalpha() method(): Check given string only contains characters

s4 = "Hello"
print("s4 is isalpha :", s4.isalpha())  # True

s5 = "Hello Good"
print("s5 is isalpha :", s5.isalpha())  # False

print("_" * 50)
#####################
# isalnum() method() : This method check given string only contains charater and numbers

s6 = "Hello123"
print("s6 is isalpha :", s6.isalnum())  # True

s7 = "Hello 123"  # space is not considered
print("s7 is isalpha :", s7.isalnum())  # False

print("_" * 40)
#############################################
# write a python program to find out all the mobile number from given string

str_B = """
I have been 8845663455 using Python 123 Selenium 
for user3@facebook.com quite some 8845423455 time and test123@gmail.com I have been happy 
with it 8845523455 until I got this new 9945423455 requirement test789@hotmail.com which 
I am 234 supposed to set sliders on
"""

word_list = str_B.split(" ")
for word in word_list:
    if word.isnumeric() and len(word) == 10:
        print(word)
    else:
        continue

print("_" * 50)
# get all the email id from given string
for word in word_list:
    if "@" in word:
        print(word)
    else:
        continue

print("_" * 50)
# Q: write a python to find out longest word in the given string

str_C = "I have been Programming using Python with Selenium"
max_len = 0
longest_word = ''
word_list = str_C.split(" ")

for word in word_list:  # I, have, been, Programming, using
    word_len = len(word)  # 1, 4, 4, 11, 5
    if word_len > max_len:  # 1> 0 | 4 > 1 | 4 > 4 | 11> 4 | 5> 11 | 6> 11
        max_len = word_len  # 1, 4, 11
        longest_word = word  # I, have, Programming
        print(longest_word)
    else:
        continue

print("logest word :", longest_word)

print("_"*50)
# q2. write a python programming to remove duplicate words from given string.
# without using any conversion or method.

str_x = "Akhil Aman Pratyusa Akhil Aman Ritesh Sushma"
output = ''
name_list = str_x.split(" ")
for name in name_list:
    if name not in output:
        output = output + name + " "
    else:
        continue

print("output :", output) # Akhil Aman Pratyusa Ritesh Sushma


#Q. write a python program to get count each character without using count method.

str_y = "We are Learning Python"

for char in str_y:
    print(char, ":", str_y.count(char))


# without count method:
count_dict = {}
for char in str_y: # w
    if char in count_dict:
        count_dict[char] += 1
    else:
        count_dict[char] = 1

print("count_dict :", count_dict)
# {'W': 1, 'e': 3, ' ': 3, 'a': 2, 'r': 2, 'L': 1, 'n': 3, 'i': 1, 'g': 1, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1}
