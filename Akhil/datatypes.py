List1 = [1, 5, "Akhil", True, 3.67]
print(List1)
List1.append(10)
print(List1)

print("#" * 50)

List2  = ["89", 12, 78, 56, "sample1"]
print (List2)
print(List2.append("4"))
print(List2)
print(type(List2))
print(dir(List2))
print(List2[1])
print(List2[-1])


print ("#" * 50)


List3 = []
print(type(List3))
print (List3)
# List3.append(2,3)   Type Error : append will take only one argument
List3.append([1, 2, 3])
print(List3)




# Tuple data type:

tuple1 = (1, 2, 3, "4", "akhil")
print(type(tuple1))
print(dir(tuple1))
# tuple1.add("2")    AttributeError: 'tuple' object has no attribute 'add'
# tuple1.add("2")
print(tuple1)
print(tuple1[3])


# Dictionary data type

dict1 = {"Akhil" : 1234, "Kumar":345}
print(type(dict1))
print(dir(dict1))
print(dict1["Akhil"])
dict1["Mvs"] = 987
print(dict1)


# Set data type :

set1 = {1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 6}
print(set1)
print(type(set1))
print(dir(set1))
set1.add(9)
print(set1)
# print(set1[0])   TypeError: 'set' object is not subscriptable









