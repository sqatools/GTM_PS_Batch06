# Square of tuples


# Q1.  write a python program to combine a list of data with their index and create new list
l1 = (5, 7, 9, 12)
l2 = (10, 40, 50, 60)
l3 = [15, 47, 59, 72]
l1=list(l1)
l2=list(l2)
result=[]
for i in range(len(l1)):
      result.append(l1[i]+l2[i])
print ("results",result)


#Q3
list_w = [3,6,8,9,1,4,7,2]
result=[]
for i in list_w:
      if i%2 == 0:
            result.append(i**2)
      else:
            result.append('odd')
print("result:",result)

