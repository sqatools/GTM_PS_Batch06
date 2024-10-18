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
""""
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
"""
"""
# 1) Write  a python slicing to get below output
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
"""
"""
#  2) Write a python slicing get below output
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
"""
# 3 Write  python slicing get below output
# Out put = "nachis si dog fo trickec
Str_c = "Sachin is god of cricket"
First = Str_c[0:6]
print("first:",First)
R1 = First[:: -1]
# print("R1:", R1)
Second = Str_c[7:9]
print("Second:",Second)
R2 = Second[:: -1]
print("R2:",R2)
Third = Str_c[10:14]
print("Third:",Third)
R3 = Third[::-1]
fourth = Str_c[14:17]
print("fourth:",fourth)
R4 = fourth[::-1]
Fifth = Str_c[17:25]
print("Fifth:",Fifth)
R5 = Fifth[::-1]
result = f" {R1} {R2} {R3} {R4} {R5}"
print("result:", result)
"""
"""
# 4) Write program to replace any specific word without using replace method
Str_P = "Code is best Code"
world_list = Str_P.split("")
print(word_list)
result = ''
count = 0
for word in word_list:
    #print(word)
    if word == 'Code':
        count = count+1
        if count == 1:
            result = result + 'cold'+ ' '
        elif count == 2:
            result = result + 'sold'+ ''
    else:
        result = result+ word
print("result:",result)

"""
"""
# 5) Write a program to get any specific word/substring without using count method
Str_q = "This is code is best code"
world_list = Str_q.split("")
print(word_list)
result = ''
count = 0
for word in word_list:
    #print(word)
    if word == 'Code':
        count = count+1
    else:
        continue
print("Code count:",count)
"""
"""
# Sub string
string = "python"
sub = "py"
result = string.count("py")
print"(result:",result)
"""
""""
# 1) Get a string made of first and last 2 chars
string = "Sqatools"
if len(string)<2:
    print(ture)
else:
    print(string[:2]+string[-2:])
    """
"""

# 2 from list of strings,length of longest string
string = ["I", "am", "learning", "Java"]
count = 0
for word in string:
    a = len(word)
    if a>count:
        count = a
        print (count)
"""
String = ["i", "am", "going"]
tem = 0
for word in String:
    a = len(word)
    if a > tem:
        tem = a
        print(tem)







