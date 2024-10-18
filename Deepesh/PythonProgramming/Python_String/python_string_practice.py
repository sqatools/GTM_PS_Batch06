str1 = "Hello good morning"
print(str1, type(str1))

# get value from string using index position
print(str1[4])  # o
print(str1[-7])  # m

print("_"*50)
# Apply loop on string (without indexing)
str2 = "Programming"
for ch in str2:
    print(ch, end=' ')
# P r o g r a m m i n g

print("_"*50)
# Apply loop on string (with indexing)
str3 = "Python"
str_len = len(str3)
for i in range(str_len):
    print(i, str3[i])

"""
0 P
1 y
2 t
3 h
4 o
5 n

"""

print("_"*50)

# String Formatting
# Hello My name is Rahul and age is 25, and I live in Pune
name = "Akhil"
age = 20
city = "Mumbai"

# 1. string concatenation
result1 = "Hello My name is "+name+" and age is "+str(age)+", and I live in "+city
print(result1)

var = "Hello" + " Good Morning"
print(var)
v1 = 'Hello'
v2 = 'Good Morning'
v3 = v1 +" "+v2
print(v3)


# 2. Format method
result2 = "Hello My name is {} and age is {}, and I live in {}".format(name, age, city)
print(result2)


# 3. f string formatting
result3 = f"Hello My name is {name} and age is {age}, and I live in {city}"
print(result3)


num1 = 50
num2 = 60
num3 = num1 + num2
print(f"addition of number: {num3}")
# addition of number: 110
print(f"multiplication of number: {num1*num2}")
# multiplication of number: 3000


print("_"*50)
##### raw string ####
# if we will add r before quote then entire string will convert into raw string.
# there will be no effect of \n\t or any other symbols

# \n : line break
# \t : tab space
print(r"Hello Good Morning \n\n Hope you are doing \t\t\t good")

print("_"*50)
a = "Hello"
b = "Python"
a, b = b, a
print("value of a :", a)
print("value of b :", b)
