#Session 3:25/09/2024

#DATA TYPES
#1.Number ---->Integer,float,complex numbers
#2.Sequentials--->String,List,Tuple
#3.Dictionary
#4.Set
#5.Boolean

#INTEGER DATA TYPE

a=10
print("integer type a:",type(a),a)

b=233243536446573473457324324
print("integer type b:",type(b),b)

c=123
print("integer type c:",type(c),c)
c=100
print("integer type c:",type(c),c)

d=0
e=-234
print("integer type d:",type(d),d)
print("integer type e:",type(e),e)

print("#"*50)

#FLOAT DATA TYPE

var_a=50.66
print("float type var_a:",type(var_a),var_a)

var_b=567721873682.1768716821
print("float type var_b:",type(var_b),var_b)

var_c=55.33454656655765756
print("float type var_c:",type(var_c),var_c)

var_d=0.0
print("float type var_d:",type(var_d),var_d)

print("#"*50)

#COMPLEX DATA TYPE
#complex data type contains real & Imaginary values

var_1= 5+7j
print("complex value:",var_1,type(var_1))
print("real value :",var_1.real)
print("imaginary value :",var_1.imag)

var_a = 10+45j
var_b = 34+50j
var_c = var_a + var_b
print("complex value:",var_c,type(var_c))

var_a = 10+45j
var_b = 34+50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))


#doubt

var_a = 10*45j
var_b = 34-50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))

var_a = 10+45j
var_b = 34+50j
var_c = var_a * var_b
print("complex value:",var_c,type(var_c))
#----------------------------------

var_a = -10+45j
var_b = 34+50j
var_c = var_a - var_b
print("complex value:",var_c,type(var_c))

var_1 = complex(10,98)
print("complex value:",var_1,type(var_1))

var_2 =complex()
print("complex value:",var_2,type(var_2))

var_3 =complex(5)
print("complex value:",var_3,type(var_3))

var_4 =complex(5j)
print("complex value:",var_4,type(var_4))

print("#"*50)

#SEQUENTIAL DATA TYPE

#STRING DATA TYPE

str_1="hello"
str_2='welcome'
str_3="""to grotech minds
         to learn python
         automation skills"""
print("string 1:",str_1,type(str_1))
print("string 2:",str_2,type(str_2))
print("string 3:",str_3,type(str_3))


str_1="hello "
str_2='welcome '
str_3="""to grotech minds
         to learn python
         automation skills"""
str_4 = str_1 + str_2 + str_3
print("string 4:",str_4,type(str_4))


string = "sushmaravi"
print("indexing value:",string[5]) #+ve indexing starts from s=0,u=1,s=2,h=3,m=3,a=5,r=6,a=7,v=8,i=9
print("indexing value:",string[9])
print("indexing value:",string[-4]) #-ve indexing starts from i=-1,v=-2,a=-3,r=-4,a=-5,m=-6,h=-7,s=-8,u=-9,s=-10
print("indexing value:",string[-10])

#Session 4:26/09/2024

#LIST DATA TYPE:it is mutable data type

#EX:1
list_1=[5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true"]
print("list values:",list_1,type(list_1)) # printing list values & type
print("list values:",len(list_1)) # finding length of the list
print("list values:",list_1[0])  # finding indexing values
print("list values:",list_1[7])
print("list values:",list_1[-6])
print("list values:",list_1[-1])

#EX:2
list_1=[5,8.9,"python"] # list is mutable after creating we can modify /update
                        #Append object to the end of the list.
list_1.append(1000000) # here append is method to add/update the new value at the last(default it will add the values at the last in list)
print("append the list values:",list_1,len(list_1),type(list_1)) # printing list values & type

#EX:3
list_1=[5,8.9,"python"]
list_1.clear() #Remove all items from list
print("clear the list values:",list_1,len(list_1),type(list_1))

#EX:4
list_1=[5,8.9,"python"]
list_1.copy() #copy Return a shallow copy of the list
print("copy the list values:",list_1,len(list_1),type(list_1))

#EX:5
list_1=[5,8.9,"python"]
list_1.count(1) # count Return number of occurrences of value
print("count the list values:",list_1,len(list_1),type(list_1))

#EX:6
"""list_1=[5,8.9,"python"]
list_1.extend() #Extend list by appending elements from the iterable
print("list values:",list_1,len(list_1),type(list_1))"""

#EX:7
list_1=[5,8.9,"python"]
list_1.index("python") #Index Return first index of value.
print("indexing the list values:",list_1,len(list_1),type(list_1))

#EX:8
"""list_1=[5,8.9,"python"]
list_1.insert() #Insert object before index
print("insert the list values:",list_1,len(list_1),type(list_1))"""

#EX:9
list_1=[5,8.9,"python"]
list_1.pop(1) # pop  Remove and return item at index (default last)
list_1.pop(-1)
print("pop the list values:",list_1,len(list_1),type(list_1))

#EX:10
list_1=[5,8.9,"python"]
list_1.remove(8.9) #Remove first occurrence of value
print("remove the list values:",list_1,len(list_1),type(list_1))

#EX:11
list_1=[5,8.9,"python"]
list_1.reverse() #Reverse *IN PLACE*.
print("reverse the list values:",list_1,len(list_1),type(list_1))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("#"*50)

#TUPLE DATA TYPE :it is immutable data type

#EX:1
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
print("tuple values:",tuple_1,type(tuple_1)) # printing list values & type
print("tuple values:",len(tuple_1)) # finding length of the list
print("tuple values:",tuple_1[0])  # finding indexing values
print("tuple values:",tuple_1[7])
print("tuple values:",tuple_1[-6])
print("tuple values:",tuple_1[-1])

#EX:2
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
tuple_1.count(1) #count Return number of occurrences of value
print("count the tuple values:",tuple_1,len(tuple_1),type(tuple_1))

#ex:3
tuple_1=(5,8.9,"python",[1,3,5],(2,4,6),{'name':"sushma",'skills':"python"},{2,3,4,5},"true")
tuple_1.index("python") #Index Return first index of value.
print("index the tuple values:",tuple_1,len(tuple_1),type(tuple_1))

print(dir(tuple)) # to check methods of tuple class
#'count', 'index'
print(dir(list)) # to check methods of list class
#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

print("#"*50)
#DICTIONARY DATA TYPE :it is mutable data type

#EX:1
dict_1={'a':12345,'b':6789}
print("dictionary values:",dict_1['a'],dict_1['b'])

#EX:2
dict_1={'a':12345,'b':6789}
print("dictionary values:",dict_1)

#EX:3 #only immutable data types can be key in the dictionary i,e int,float,string,tuple,boolean
dict_1={'name':"sushma",'education':"B.Tech"}
dict_1['department']=["ECE"] #string
dict_1[123]=["ravi"] # int
dict_1[2.3]=["parvathi"] #float
dict_1[(4,5,6)]=["sweet"] #tuple
dict_1[('true')]=["home"] #boolean
print("dictionary values:",dict_1,type(dict_1))

#EX:4 All types of data can store as values  in the dictionary
dict_1={'name':"sushma",'education':"B.Tech"}
dict_1[123]=["ravi"]
dict_1[(4,5,6)]=["sweet"]
print("dictionary values:",dict_1,type(dict_1))

#NOTE: List is not allowed in the dictionary
#dict_1[[1,2,3]]="python"

#EX:5
"""dict_1[4.5]=True
dict_1[False]=(1,2,3)
dict_1[5.5]='hello'
print("print values:",dict_1)"""
