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
third = str3[-4:28]
print("third :", third)
fourth = str3[0:6]
print("fourth :", fourth)
fifth = str3[10:-11]
print("fifth :", fifth)

result = f"{first} {second} {third} {fourth} {fifth}"
print(result)
#{words[1]} {words[4]} {words[0]} {words[2]}"
#result = f"Hello My name is {name} and age is {age}, and I live in {city}"