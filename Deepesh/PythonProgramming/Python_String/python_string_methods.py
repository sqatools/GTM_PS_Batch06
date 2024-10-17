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
print("str_e :", str_e.swapcase()) # lEARnING pYtHON pROGrAMMINg

#######
# title() method: This method convert first character of each word into camel case.
str_f = "LearNing PyThon ProgRamminG"
print(str_f.title())  # Learning Python Programming

str_g = "Hello Good Morning"
str_h = "GooD Evening"
print("str_g :", str_g.istitle())  # True
print("str_h :", str_f.istitle())  # False


print("_"*50)
##########
# count() method : This method count the repeatation of any char/substring in given string

str_k = "We are Learning Python Programming"
print("count of e:", str_k.count('e'))  # 3
print("count of ing:", str_k.count('ing')) # 2
print("count of space:", str_k.count(' ')) # 4

print("_"*50)
##########
# index method() : This method return the index position of any char/substring in given string
str_l = "We are Learning Python Programming"
print("index position of L:", str_l.index('L'))  # 7
print("index position of Python:", str_l.index('Python')) # 16
print("index position of e:", str_l.index('e')) # 1

# if the target character or substring is not available, then it will through error
# print("index position of W:", str_l.index('A')) # 1
# ValueError: substring not found


print("_"*50)
##########
# find() method: This method look for any char/substring and return index position
# if target char/substring is not available then it will return -1

str_x = "We are Learning Python Programming"
print("find index of Py :", str_x.find("Py")) # 16


# Hello is not available in the string, it will return -1
print("find index of Hello :", str_x.find("Hello")) # -1


print("_"*50)
##########
# replace() method:  This method replace any char/substring from given string.

str_y = "Java is Best Programming Language Java"
result = str_y.replace("Java", "Python")
print("result :", result)
print("str_y :",str_y )

result2 = str_y.replace("Java", "JAVASCRIPT").replace("Best", "Famous")
print("Result2 :", result2)
# JAVASCRIPT is Famous Programming Language JAVASCRIPT

result3 = str_y.replace("Java", "JAVASCRIPT").replace("Best", "Famous").lower()
print("Result3 :", result3)
# javascript is famous programming language javascript


print("_"*50)
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
#['J', 'v', ',is,Best,Progr', 'mming,L', 'ngu', 'ge,J', 'v', '']

url = "https://www.google.co.in"
split_url = url.split(".")
print(split_url)#['https://www', 'google', 'co', 'in']
print("www output :", split_url[0].split("//")[1]) # www
print("https output :", split_url[0].split("//")[0]) # https:



print("_"*50)
# Write a python to replace first Java word with Python and second Java with C#
str_p = "Java is Best Programming Language Java"
word_list = str_p.split(" ")
print(word_list)
# ['Java', 'is', 'Best', 'Programming', 'Language', 'Java']
output = ''
count = 0
for word in word_list: # Java, is Best
    #print(word)
    if word == 'Java':
        count += 1 # 1, 2
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


print("_"*40)
#Q2 . write a python program to remove all the vowels
str2 = "Hello Good Morning, Hope You are Doing Good"
vowels = "aeiou"
result = ''

for char in str2:
    if char in vowels:
        continue
    else:
        result = result + char

print("Result :", result)


#q1 : Write a program to replace any specific word without using replace method.
#q2 : Write a program to get count any specific word/substring without using count method.

