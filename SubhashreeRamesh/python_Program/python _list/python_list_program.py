# Get square of all values from given list andprint value if it is greater than 15
list =[2,3,4,5,12]
for val in list:
    if val%3==0 and val%4 ==0:
        print(val**2)
    elif val%5==0:
        print(val**3)

#write a python program to get max value in the list

list3=[4,7,8,100,9,12,45]

max_val=0

for val in list3:
    if val > max_val:
       max_val = val
    else:
        continue
print("max_val:",max_val)






























