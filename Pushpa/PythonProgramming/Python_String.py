# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string

# if else condition
#str1 = input("Enter a string: ")
str1 = "python"
if len(str1) < 2:
   result = ""
else:
   result = str1[:2] + str1[-2:]

print("Result:", result)

# for loop with range the above variable (with indexing)
str_l = len(str1)
for i in range(str_l):
   print(i, str1[i])

# for loop(without indexing)
for i in str1:
   print(i, end=' ')
# output
# Result: pyon
# 0 p
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n
# p y t h o n

# String Formatting
# Type 1
name = "Paul"
age = 16
location = "New Jersey"
# String Concatenation
result = "My name is "+name+" and age is "+str(age)+", I live in "+location
print(result) # output:  My name is Paul and age is 16, I live in New Jersey

# simple string format
var = "Hi!, " + "How are you?"
print(var)
v1 = "Yes"
v2 = "I'm good"
v3 = v1 + " " + v2
print(v3) # Hi!, How are you? Yes I'm good


# Type 2
# another way of concatenation format method .format() using the above variables
result = "My name is {} and age is {}, I live in {}".format(name, age, location)
print(result) # output: My name is Paul and age is 16, I live in New Jersey

# Type 3
# f string formatting, using f in the front
result = f"My name is {name} and age is {age}, I live in {location}"
print(result) # output: My name is Paul and age is 16, I live in New Jersey



# class work
# result = f"My name is {name} and age is {age}, I live in {location}"
# print(result) # output: My name is Paul and age is 16, I live in New Jersey

str_a = "Virat is the best Indian Batsman"
s1 = "Virat"
s2 = "is"
s3 = "the"
s4 = "best"
s5 = "Indian"
s6 = "Batsman"
result = f"{s1} {s2} {s3} {s4} {s5} {s6}"
print(result)

result1 = "{} {} {} {} {} {}".format(s1, s2, s3, s4, s5, s6)
print(result1)

# output : Virat is best Indian Batsman
str3 = "Virat is the best Indian Batsman"

first = str3[:5]         # "Virat"
second = str3[6:8]       # "is"
third = str3[9:12]       # "the"
fourth = str3[13:17]     # "best"
fifth = str3[18:24]      # "Indian"
sixth = str3[25:]        # "Batsman"

sentence = first + " " + second + " " + third + " " + fourth + " " + fifth + " " + sixth
sentence1 = f"{first} {second} {third} {fourth} {fifth} {sixth}"
print("Full Sentence :", sentence) # Full Sentence : Virat is the best Indian Batsman
print("Full Sentence1 :", sentence1) # Full Sentence1 : Virat is the best Indian Batsman


str5 = "Learning Python"
print(str5[-2:1:-2])

#Q1. Write a python slicing get below output
str_a = "My Name is John"
# output = "ny Name is JohM"

first_letter = str_a[-1]  #ny
print(first_letter)
middle_letters = str_a[1:-1]  # or str_a[1:14:1] #y Name is Joh
last_letter = str_a[0]  #M
output = first_letter + middle_letters + last_letter
print(output) # ny Name is JohM

#Q2. Write a python slicing get below output
str_b = "India is best country"
# output2 = "IIndia iis bbest ccountry"
a1 = str_b[0]
a2 = str_b[0:5:1]
a3 = str_b[6]
a4 = str_b[6:8]
a5 = str_b[9]
a6 = str_b[9:13]
a7 = str_b[14]
a8 = str_b[14:]

output2 = a1+a2 +" "+ a3+a4 +" "+ a5+a6 +" "+ a7+a8
print(output2) # IIndia iis bbest ccountry

# Method 2
str_c = "India is best country"
a = str_c.split(" ") # split using space
print(a[0])
print(len(a))
# output4 = a[0][0]+a[0] +" "+ a[1][0]+a[1] +" "+ a[2][0]+a[2] +" "+ a[3][0]+a[3]
# print(output4) # IIndia iis bbest ccountry

# using for loop by using split()
output5 = ""
for i in range(0, len(a)):
   output5 = output5 + a[i][0]+a[i] + " "
print(output5) # IIndia iis bbest ccountry


#Q3. Write a python slicing get below output
str_c = "Sachin is god of cricket"
# output3 = "nachiS si dog fo trickec"
b1 = str_c[5]
b2 = str_c[1:5]
b3 = str_c[0]
word1 = b1+b2+b3
print(word1) # nachiS

c1 = str_c[8]
c2 = str_c[7]
word2 = c1+c2
print(word2) #si

d1 = str_c[12]
d2 = str_c[11]
d3 = str_c[10]
word3 = d1+d2+d3
print(word3)

e1 = str_c[15]
e2 = str_c[14]
word4 = e1+e2
print(word4)

f1 = str_c[-1]
f2 = str_c[-6:-1]
f3 = str_c[-7]
word5 = f1+f2+f3
print(word5)

output3 = word1+" "+word2+" "+word3+" "+word4+" "+word5
print(output3) # nachiS si dog fo trickec

