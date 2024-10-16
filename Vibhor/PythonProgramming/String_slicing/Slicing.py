'''
# Virat is best Indian Batsman
str3 = "Indian is Batsman Virat best"
first = str3[-10:-5:1]
print("first: ", first)
second = str3[7:9]
print("second: ", second)
third = str3[-4:]
print("third: ", third)
fourth = str3[0:7:1]
print("fourth: ", fourth)
fifth = str3[10:17:1]
print("fifth: ", fifth)
Result= f"{first} {second} {third} {fourth} {fifth}"
print("Result= ",Result)
'''

# 1- write a python slicing to get below output-
str_a ="My Name is John"
output= "ny Name is JohM"

# 2 write a python slicing to get below output-
str_b ="India is best Country"
Output= "IIndia iis bbest CCountry"

# 3 write a python slicing to get below output-
str_c ="Sachin is god of Cricket"
Output= "nachiS si dog fo trickeC"

#1 str_a ="My Name is John"
print(str_a[-1]+str_a[1:-1]+str_a[0])

print("*"*50)

#2 str_b ="India is best Country"
first=str_b[0]+str_b[0:5]
print(first)
second=str_b[6]+str_b[6:8]
print(second)
third=str_b[9]+str_b[9:13]
print(third)
fourth=str_b[-7]+str_b[-7:]
print(fourth)
Result= f"{first} {second} {third} {fourth}"
print("Result= ", Result)

print("*"*50)

#3 str_c ="Sachin is god of Cricket"
first=str_c[5]+str_c[1:5]+str_c[0]
print(first)
second=str_c[8]+str_c[7]
print(second)
third=str_c[12]+str_c[11]+str_c[10]
print(third)
fourth=str_c[-9]+str_c[-10]
print(fourth)
fifth=str_c[-1]+str_c[-6:-1]+str_c[-7]
print(fifth)
Result=f"{first} {second} {third} {fourth} {fifth}"
print("Result= ", Result)

print("*"*50)

str_1= "My Name Is Vibhor"
print(str_1.upper())
print(str_1.lower())
print(str_1.title())
print(str_1.islower())
print(str_1.isupper())
print(str_1.istitle())
print(str_1.swapcase())
