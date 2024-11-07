list1 = [6,8,2,6,1,5,7,8,7]
dict = {}
 for val in list1:
   if val not in dict:
       dict[val] = val**3
       print(dict)
