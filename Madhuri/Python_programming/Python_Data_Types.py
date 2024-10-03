# Numeric  Type
# Integer (int): Represents whole numbers without  decimals  point
# Integers can be positive and negative they have no limts and size
num = 10
print(type (num))

num1 = 6, 3, 4, 5, 8,
print(type(num1))

# num1 = 100
# print(num1)  # replaced previous value

# Floating(float)
# it represents decimals numbers
# floats are used to represent  real numbers including positive and negative  values
Var_a = 50.5
print("data type of var_a:", type ("var_a :"), ("var_a :"), )

# complex number
#  is  combination of real and image values
# Complex number is represent in the format of x+yj, x-yj
# Complex number is immutable data type

var_b = 10+5j
print(var_b, type("var_b:"), var_b.imag, var_b.real)

# Sequence data types
# 1) String Data type:-
# String is immutable data type
# String follow the positive and negative index values
# String can define with singe and quotes double qutoes and triple qutoes
# Str_a
name = "rohan"
# 2)  List data type
#  List is mutable data type, we can add the values in the list
# list follow the positive and negative index ing as string(sequence)
# list can contain all types of data, int, float, string, list,tuple, dict ,set ,boolean
# list represent with square brackets
# all values are in list will be comma separated

list = [4, 4.5,  "hello", [1,4,6] ]
print("list1:", list,  type("list1:"))
print(list[3])

str1 = "python"
print("string length:", len(str1))
Str2 = "madhuri"
print("string length:", len(Str2))
List3 = [5,7,9]
List3.append(100)
print("list3:", ("list3:"))

# 3) Tuple Data type
# tuple is immutable data type , once it is defined we cant not modify
# tuple follow the positive and negative as like list and string
# tuple  can contains any of data, int,float,string,tuple,dec,set boolean
# tuple represent with round brackets
# tuple is faster than list data type
# we can store fixed data tuple that we dont want to change in future
# eg months in year days in week etc
Tup1 = (4, 5.6, "programming" , [3,6,7] , (1,5,7), {'a': 345 ,'b':  456})
print ( "tup1:" , type("tup1:"))
print("total values in the tuple:", len("tup1:"))
print("first value in the tuple:" , Tup1[0])

print(Tup1[2])
print(Tup1[-1])
print(Tup1[-5])
print (dir(tuple))

# Dictionary data type
# dictionary is mutable data type, we can update tha data at any point of time
# dictionary doesn't fallow the positive or negative index
# dictionary store values in key value format
# dictionary represent with {} braces
# dictionary only contains unique keys, duplicates keys are not allowed
# dictionary can contains duplicate values
# keys are allowed only immutable data type like int float string tuple boolean
# all types of data can store as value in the dictionary

dict1 = {'name: Rahul; name: madhu'}
print(dict1)

# set data type
# set is mutable data type
# set only stores unique values, duplicate values are not allowed
# set can contains only immutable data type
# mutable data type are not allowed as set member eg:- list dic set
# set store data in random order
# set does not fallow any indexing
# set represent with curly braces
set2 = {5, 7, 6, 8, 8, 7}
print("set2:", set2)
#set.add(100)
print("set2:", set2)
print(dir(set))

# boolean data type
# boolean values represent with true and false
# boolean is immutable data type
# boolean always consider as return value of any logical condition

var1 = 300
var2 = 400
var3 = 300
print(var1 == var2)
print(var1 == var3)






















