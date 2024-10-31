


list1 = [4,7,9,12,5,2,10,3,6]
for val in list1:
    if val%3==0 and val%4==0:
        print("square of the value is:",val**2)
    elif val%5==0:
        print("cube of the value is:", val**3)


s2= "534654"
print(s2.isalnum())

for i in range(len(list1)):
    print(i,list1[i])


list2= [4,7,2,8,12,90]
print(list2[-1:0:-2])

print("-"*50)

print(list2.insert(-2,300))

a= [4,7,2,8,12,90]
print(a*2)
