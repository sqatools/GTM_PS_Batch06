print(dir(dict))
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 
'keys', 'pop', 'popitem', 'setdefault', 'update',
 'values'
"""

#################
# update method: This method update data from one dictionary to another dictionary
d1 = {'a' :123, 'b' : 567, 'c': 890}
d2 = {'p' : 222, 'q' : 333, 'r': 444}

d2.update(d1)
print("dictionary 2 update data:", d2)
# {'p': 222, 'q': 333, 'r': 444, 'a': 123, 'b': 567, 'c': 890}

print("_"*50)
#################
# get method : This method return value of any key provided

dict3 ={'p': 222, 'q': 333, 'r': 444, 'a': 123, 'b': 567, 'c': 890}
value = dict3.get('a')
print("value of a :", value)
print("value of a :", dict3['a'])

print("_"*50)
###############
# keys and values method: Keys method return list of keys and values method list of values
dict4 ={'p': 222, 'q': 333, 'r': 444, 'a': 123, 'b': 567, 'c': 890}
print("list of keys :", dict4.keys())
# dict_keys(['p', 'q', 'r', 'a', 'b', 'c'])

print("list of values :", dict4.values())
#dict_values([222, 333, 444, 123, 567, 890])


print("_"*50)
###############
# items() method : This method provide list of key value pair in tuple
dict5 ={'p': 222, 'q': 333, 'r': 444, 'a': 123, 'b': 567, 'c': 890}
print(dict5.items())
# [('p', 222), ('q', 333), ('r', 444), ('a', 123), ('b', 567), ('c', 890)])


print("_"*50)
###############
# pop method : This method remove data set of key value pair from dictionary and return value.
dict6 ={'p': 222, 'q': 333, 'r': 444, 'a': 123, 'b': 567, 'c': 890}
#removed_val = dict6.pop('r')
print("R removed value :", dict6.pop('r'))
print("dict6 :", dict6)
# {'p': 222, 'q': 333, 'a': 123, 'b': 567, 'c': 890}


print("_"*50)
###############
# popitem() method : This method remove key value pair combination from dictionary and return it
# This method remove data on the basis of rule LIFO (Last In First Out)
dict7 = {'p': 222, 'q': 333, 'a': 123, 'b': 567, 'c': 890}
removed_data = dict7.popitem()

print("removed data :", removed_data) # ('c', 890)
print("dict7 :", dict7)
# {'p': 222, 'q': 333, 'a': 123, 'b': 567}

print("_"*50)
###############
# clear method : This method clear all the data from dictionary
dict_a = {'p': 222, 'q': 333, 'a': 123, 'b': 567}
dict_a.clear()
print("dict a:", dict_a) # dict a: {}


print("_"*50)
###############
# del function : This will remove entire dictionary from memory or we can removed specific
# value as well

dict_b = {'p': 222, 'q': 333, 'a': 123, 'b': 567}
del dict_b['a']

print("dict_b :", dict_b) #{'p': 222, 'q': 333, 'b': 567}

del dict_b
# print("dict_b :", dict_b) # variable has been delete from memory.
# NameError: name 'dict_b' is not defined. Did you mean: 'dict_a'?

print("_"*50)
############################################
# shallow copy : In shallow we do not copy actual data, we just pass reference of dictionary var
# to another dictionary variable, in that case if we will do changes in any dict then changes will
# reflect on other dictionary as well.

dict_p = {'p': 222, 'q': 333, 'b': 567}
dict_q = dict_p
dict_q['c'] = 500
print("dict_q :", dict_q)
print("dict_p :", dict_p)


# Deep Copy : In deep copy we actually copy data from one dict to another dict, and if we will
# do any change in any dictionary than changes will not reflect in another dictionary.
x = {'Name' : 'Rahul', 'age': 25, 'mobile' : 56456456}
y = x.copy()
y['address'] = 'Pune, Mahalunge'

print("dictx :", x) # {'Name': 'Rahul', 'age': 25, 'mobile': 56456456}
print("dicty :", y) # {'Name': 'Rahul', 'age': 25, 'mobile': 56456456, 'address': 'Pune, Mahalunge'}


print("_"*50)
#######################
# fromkeys method: This method create a dictionary with list of keys provided and one single
# value assign to all the keys.

list1 = ['a', 'b', 'c']
result = dict.fromkeys(list1, 60)
print("result :", result) # {'a': 60, 'b': 60, 'c': 60}



print("_"*50)
#######################
# setdefault method : Set default update the dictionary with default value for any key, and return its
# value if keys is already in dictionary, or it will return default value for new key

dict_z = {'Name' : 'Rahul', 'age': 25, 'mobile' : 56456456}

result = dict_z.setdefault('mobile', 'INDIA')
print(result)  # 56456456
print("dictz :", dict_z) # {'Name': 'Rahul', 'age': 25, 'mobile': 56456456}

result2 = dict_z.setdefault('Address', 'INDIA')
print("result2 :", result2) # result2 : INDIA
print("dictz :", dict_z) # {'Name': 'Rahul', 'age': 25, 'mobile': 56456456, 'Address': 'INDIA'}
