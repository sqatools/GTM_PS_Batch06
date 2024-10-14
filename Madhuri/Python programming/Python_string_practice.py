"""
Str1 = "Hello good morning"
print(str1,type(str1))
# get the value from string using index position
print(str1[4]) # 0
print(string[-7]) #m
"""

print("-"*50)
"""
# Apply loop on staging(without indexing)
str2 = "programming"
for ch in str2:
    print(ch,end="-")
"""
"""
# apply loop on staging (with indexing)
str3 = "python"
str_len = len(str3)
for i in range(str_len):
    print(i, str3[i])
    """
"""
# string formatting
# print(" "* 50)
# hello my name is  Rahul and age 25, ilive in pune
name = "Akki"
age = 20
city = "Mumbai"
# 1 string concatenation
result = "Hello My name is "+name+" and age is "+str(age)+" and i live in "+city+""
print (result)

var = "hello "+ "Good morning"
#print(var) 0r
var1 = "hello"
var2 = "good morning"
var3 = (var1+ "-"+var2) # if you need space between you can give " "
print(var3)

# 2) format method
result2 = "Hello  my name is {} and age is {}, i live in{}".format(name, age, city)
print(result2)

# 3) f string formating
result3 = f"hello my name is {name} and age is {age},and i live in {Mumbai}"
print (result3)
"""
num1 = 3
num2 = 6
num3 = num1+num2
print(f"addition of number:{num3}")
print (f"mulitiplication of number:{num1*num2}")

### Raw String ###
# if we will add r  before qutote  then entire string will convert into raw string
# There will be no effect of \n\t or any other symbols
# \n : line break
# \t : tab space
print (r"hello good morning \n\n hope you are doing\t\t\t good" )

