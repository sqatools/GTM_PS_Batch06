# write a python program to check given is available in the list
list1 = [4, 6, 8, 1, 5, 18]
num1 = 9

if num1 in list1:
    print("Data is available in the list")
else:
    print("Data is not available in the list")

print("_"*50)
# write a python get even and odd word as per value enter.
# single line if condition
num2 = 7
result = "even" if num2%2 == 0 else "odd"
print(num2, ":", result)  # 7 : odd


# is operator
var_a = 'Python'

if var_a is None:
    pass
else:
    print(var_a*5)

var_b ='H '
if var_b is not None:
    print(var_b*7)
else:
    pass


dir()
list.append()
