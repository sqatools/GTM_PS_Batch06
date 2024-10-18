### Python String Slicing #######

# Rule1 : str[initial index : last index]
# In this rule, the output string will include initial index character and exclude
# last index character.

# -> the result string will always contain substring from left to right

str1 = "Good Morning"

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
print(str2[:-3])  # Python Programm



print("_"*50)
# Rule3 : str[initial index:]
# In this rule default last index will be end of the string
str3 = "Learning is Fun"
print(str3[5:])  # ing is Fun
print(str3[0:])  # Learning is Fun
print(str3[-8:]) # g is Fun


print("_"*50)
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
print(str_a[-1:-10:-1])  # t country
print(str_a[-1:-5:1])  # blank output
print(str_a[10:-20:-1]) #  a si a

print("_"*50)
# question:
# write a python program to arrange the sentence correctly
# output : Virat is best Indian Batsman
str3 = "Indian is Batsman Virat best"
first = str3[-10:-5:1]
print("first :", first)

second = str3[7:9:1]
print("second :", second)
third = str3[-4:]
print("third :", third)
fourth = str3[:6]
print("fourth :", fourth)
fifth = str3[10:17]
print("fifth :", fifth)

result = f"{first} {second} {third} {fourth} {fifth}"
print("Result :", result)
# Virat is best Indian Batsman


print("_"*50)
###################################################
# Rule5 : str[ : last index : different of index]
# -> if difference value is positive then default initial index will zero
# -> if difference value is negative then default initial index will -1

str4 = "Good Evening"
print(str4[:7:1])  # Good Ev # default initial index zero
# print(str4[0:7:1])

# In this example, it will print value from -1 to 7 in reverse order
print(str4[:7:-1]) # gnin  # deafult initial index will be -1
# print(str4[-1:7:-1])

# In this example, it will print value from -1 to 2 in reverse order
print(str4[:2:-1])  # gninevE d

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

print(str5[-2: 2:-2]) # otPgir

print("_"*40)
# Slicing Home Work
#Q1. Write a python slicing get below output
str_a = "My Name is John"
output = "ny Name is JohM"

first_char = str_a[0]
last_char = str_a[-1]
remain_char = str_a[1:-1]
print(f"{last_char}{remain_char}{first_char}")
# ny Name is JohM



#Q2. Write a python slicing get below output
str_b = "India is best country"
output2 = "IIndia iis bbest ccountry"
w1 = str_b[:5]
w2 = str_b[6:8]
w3 = str_b[9:13]
w4 = str_b[14:]
print(f"{w1[0]}{w1} {w2[0]}{w2} {w3[0]}{w3} {w4[0]}{w4}")
# IIndia iis bbest ccountry


#Q3. Write a python slicing get below output
str_c = "Sachin is god of cricket"
output3 = "nachiS si dog fo trickec"
w1 = str_c[:6]
w11 = f"{w1[-1]}{w1[1:-1]}{w1[0]}"

w2 = str_c[7:9]
w22 = f"{w2[-1]}{w2[1:-1]}{w2[0]}"

w3 = str_c[10:13]
w33 = f"{w3[-1]}{w3[1:-1]}{w3[0]}"

w4 = str_c[14:16]
w44 = f"{w4[-1]}{w4[1:-1]}{w4[0]}"

w5 = str_c[17:]
w55 = f"{w5[-1]}{w5[1:-1]}{w5[0]}"

print(f"{w11}  {w22} {w33} {w44} {w55}")
# nachiS  si dog fo trickec
