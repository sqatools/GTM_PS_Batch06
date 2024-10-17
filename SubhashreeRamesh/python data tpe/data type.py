"""
num=int(input(" Please enter the number"))
if num%2==0:
    print(num**2)
elif num%3 == 0:
    print(num**3)
elif num%7==0:
    print(num**4)
else:
    print("number does not match")
"""
var1=10
var2=2
var3=3
num=int(input(" Please enter the number for var1:"))
if var1 == 1:
    print("addition of values:",var1+var2)
elif var1==2:
    print("multiplication of value:",var2*var3)
elif var1==3:
    print("division of value:",var2%var3)
elif var1==4:
    print("subraction of value:",var2-var3)
else:
    print("none of the values are matched")

