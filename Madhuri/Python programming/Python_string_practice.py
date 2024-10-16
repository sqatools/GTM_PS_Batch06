"""
Str1 = "Hello good morning"
print(str1,type(str1))
# get the value from string using index positiogitn
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
"""
# output = "Virat is best Indian batsman"
str3 = "Indian is batsman Virat best"
first= str3[-11:-5:1]
print("first:",first)
second = str3[7:9]
print("second:", second)
third = str3[24: 29: ]
print("third:", third)
fourth = str3[0:6:]
print ("fourth:",fourth)
five = str3[9:17]
print("five:",five)
result = f"{first} {second} {third} {fourth} {five}"
print("result :", result)

"""
"""
# Write  a python slicing to get below output
# Out put = " ny Name is JohM "
Str_a = "My Name is John"
first = Str_a [-1:]
print("first:", first)
second = Str_a[1:-1]
print("second:", second)
third = Str_a[0:-14:1]
print("third:", third)
output = f"{first}{second}{third} "
print ("output:", output)



# Write a python slicing get below output
# out put = "IIndia iis bbest ccountry"
Str_b = "India is best country"
first = Str_b [0:5]
print("first:", first)
R1 = Str_b[0]
print("R1:",R1)
Second = Str_b[6:9]
print("second:", Second)
R2 = Str_b[6]
print("R2:",R2)
Third = Str_b[9:13]
print("Third:",Third)
R3 = Str_b[9]
print("R3:",R3)
Fourth = Str_b[14:22]
print("Fourth:",Fourth)
R4 = Str_b[14]
print("R4:",R4)
Result = f"{R1}{first} {R2}{Second} {R3}{Third} {R4}{Fourth}"
print("Result:", Result)
"""
