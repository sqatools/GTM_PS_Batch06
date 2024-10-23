"""list2=[4,7,9,12,5]
for val in list2:
    sq=val**2
    if sq >25 :
        print(sq)"""

"""list2=[4,7,9,12,5,2,10,3,6]
for val in list2:
    #print(val)
    if val % 3 == 0  and val % 4 ==0 :
        print(val**2)
    elif val %5==0:
        print(val**3)"""

list3=[4,7,8,100,9,12,45]
max_val = 0
for val in list3:
    print(val)
    if val > max_val:
        max_val=val
    else:
        continue
print("max_val:",max_val)


