###### integer########

# integer---> float
num1 = 404
f1 = float(num1)
print(f1, type(f1))

# print("_"* 50)
# int----> string
num1 = 657
str1 = str(num1)
print(str1, type(str1), str1[0])
print(str1, type(str1), str1[2])
str2 = '"Hello"'
print (str2)

# int---> list # conversion is not possible
# int is single value list and dict set tuple  are ha multiple values
# conversion not possible
# int--->list
# int----> dic
# int ----> set
# int----> tuple

# int---> boolean ##
num_a = 0
b1 = bool(num_a)
print(b1, type(b1))
num_b = 1
b2 = bool(num_b)
print(b2, type(b2))
num_c = 3
b3 = bool(num_c)
print(b3, type(b3))

### float conversion##
##float---> int
f1 = 55.8
n1 = int(f1)
print(n1, type(n1))
print("_"*50)
## float--->string##
f3 = 67.98
s2 = str(f3)
print(s2, type(s2))
print(s2[3])

# float --> list # conversion is not possible
# float ---> tuple # conversion is not possible
# float ---> dic # conversion is not possible
# float --> set # conversion is not possible

# float---> boolean
f1 = 0.0
b1 = bool(f1)
print(b1, type(b1)) # false,

f2 = 0.25
b2 = bool(f2)
print(b2, type(b2))
