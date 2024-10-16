### Python String Slicing #######

# Rule1 : str[initial index : last index]
# In this rule, the output string will include initial index character and exclude
# last index character.

# -> the result string will always contain substring from left to right

str1 = "Good Morning" #12
#

print(str1[0:4])    # Good
print(str1[4:8])    #  Mor
print(str1[1:-1])   # ood Mornin
print(str1[2:-5])   # od Mo
print(str1[-1:5])   # can not move -1 to positive value
print(str1[-8:-2])  #  Morni

print("_"*50)
# Rule2 : str[:last index]
# In this default initial index will zero and other properties are same as above.

str2 = "Python Programming"
print(str2[:8])  # Python P
print(str2[:-3])  # Python Programm # it is same as above [:8] means [0:8]

# Rule3 : str[initial index:]
# In this rule default last index will be end of the string # till last if nothing is at the last
str3 = "Learning is Fun"
print(str3[5:])  # ing is Fun
print(str3[0:])  # Learning is Fun
print(str3[-8:]) # g is Fun

# Rule4 : str[initial index : last index : different of index]
# -> In this rule user has to define three parameters the initial index,
#    last index and difference between each index.

str_a = "India is a best country"

# get data with all positive
print(str_a[2:10:1])  # dia is a
print(str_a[1:15:2]) # ni sabs
print(str_a[3:20:3]) # iiae u

# get data with initial, last index and difference is negative
str_a = "India is a best country"
print(str_a[-1:-10:-1])  # yrtnuoc t
print(str_a[-1:-5:1])  # blank output
print(str_a[10:-20:-1]) #  a si a
print(str_a[10:-20:-2]) # ia

# question:
# write a python program to arrange the sentence correctly
# output : Virat is best Indian Batsman
str3 = "Indian is Batsman Virat best"
first = str3[-10:-5:1]
print("first :", first)
second = str3[7:9]
print("second :", second)
third = str3[-4:28] #[-4:]
print("third :", third)
fourth = str3[0:6]
print("fourth :", fourth)
fifth = str3[10:-11]
print("fifth :", fifth)

result = f"{first} {second} {third} {fourth} {fifth}"
print(result)
#{words[1]} {words[4]} {words[0]} {words[2]}"
#result = f"Hello My name is {name} and age is {age}, and I live in {city}"

print("_"*50)
###################################################
# Rule5 : str[ : last index : different of index]
# -> if difference value is positive then default initial index will zero
# -> if difference value is negative then default initial index will -1

str4 = "Good Evening"
print(str4[:7:1])  # Good Ev # default initial index zero
# print(str4[0:7:1])



# In this example, it will print value from -1 to 7 in reverse order(and 7 th value will not be printed
print(str4[:7:-1]) # gnin  # deafult initial index will be -1
# print(str4[-1:7:-1])

# In this example, it will print value from -1 to 2 in reverse order
print(str4[:2:-1])  # gninevE d #it will not print the letter at 2nd place i.e.goo
print(str4[:5:-1]) #gninev

#############################################
# Rule6 : str[:: different of index]
# -> If difference is positive then default initial will be zero and last index
#     will be the end of the string


# -> If difference is negative then default initial will be -1 and last index
#     will be the start of the string

str5 = "Learning Python"
# in this example initial index will 0 and read entire in positive order
print(str5[::1]) #  "Learning Python"

# in this example initial index will be -1 and read entire string in reverse order
print(str5[::-1]) # nohtyP gninraeL

print(str5[2:-2:-2]) # Blank
print(str5[2:-2:1])  # arning Pyth

print(str5[-2: 2:-2]) #otPgir
# Slicing Home Work
#Q1. Write a python slicing get below output
str_a = "My Name is John"
str_1 = str_a[:1]
str_2 = str_a[1:-1]
str_3 = str_a[-1:]
print(f'{str_3}{str_2}{str_1}')
#output = "ny Name is JohM"

#Q2. Write a python slicing get below output
str_b = "India is best country"
words = str_b.split(" ")
final_list = ""
for single in words:
    str_1 = single[:1]
    str_2 = str_a[1:-1]
    str_3 = str_1*2
    if final_list:
        final_list = f'{final_list} {str_3}{str_2}'
    else:
        final_list = f'{str_3}{str_2}'
print(final_list)

# output2 = "IIndia iis bbest ccountry"

#Q3. Write a python slicing get below output
str_c = "Sachin is god of cricket" #how we will use loop in it
"""
str_1 = str_c[:1]
str_2 = str_c[1:5]
str_3 = str_c[5:6]

str_4 = str_c[7:8]
str_5 = str_c[8:9]



print(f'{str_3}{str_2}{str_1} {str_5}{str_4}')"""

# str_c = "Sachin is god of cricket"
#
# words = str_c.split(" ")
# final_list = ""
# for single in words:
#     str_1 = single[:1]
#     str_2 = single[1:-1]
#     str_3 = single[-1:]
#     final_list = f'{final_list} {str_3}{str_2}{str_1}'
# print(final_list)





# output3 = "nachiS si dog fo trickec"
