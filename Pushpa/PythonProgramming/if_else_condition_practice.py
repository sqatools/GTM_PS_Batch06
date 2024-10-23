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

str3 = "Virat is the best Indian Batsman"

first = str3[:5]         # "Virat"
second = str3[6:8]       # "is"
third = str3[9:12]       # "the"
fourth = str3[13:17]     # "best"
fifth = str3[18:24]      # "Indian"
sixth = str3[25:]        # "Batsman"

sentence = first + " " + second + " " + third + " " + fourth + " " + fifth + " " + sixth
print("sentence :", sentence)




