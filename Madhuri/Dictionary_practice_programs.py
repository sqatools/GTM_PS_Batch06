"""
dict1 = {'a':345}
print(dict1,type(dict1))
# dictionary is mutable data type
dict2 = {'name': 'Rahul'}
dict2 ['Surname']='sharma'
print("dict2:",dict2)

# dict keys are always unique
# if duplicate keys are there then only latest data will be considered
dict3 = {'a':456,'b':678,'a':123}
print ("dict3:",dict3)

# onli immutable data type are allowed as dict key,int,float,string,tuple,boolean
dict4 = {123:'Hello'}# int as key
dict4[4.5]='python' # float as key
dict4['abc']= [3,6,7]# string as key
dict4[(1,4,6)]= {'p':111,'q':222}# tuple as key
dict4[True] = {3,6,8,1}
print("dict4:",dict4)
# duplicate values are allowed in dictionary
dict5= {'a':123,'b':123,'c':1234}
print("dict5:",dict5['a'],id(dict5['a']))
print("dict5:",dict5['b'],id(dict5['b']))
print("dict5:",dict5['c'],id(dict5['c']))
print("_"* 50)
school = {
    'students':{
        '11th':[3,5,7],
        '12th':[1,3,5],
    },
    'teachers':{
        'maths':[6,8,0],
        'chemistry':[2,5,1],
    }
}
print(school['teachers']['maths'][1]) # 8
print(school['students']['12th'][-1]) #5
print (school['students']['12th'][2]) # 5
print(school['students']['12th'])# [1,3,5]
"""
print("-"*40)
school2 ={
 'students':{
        '11th':{
        'A':[
            {'Name':'Rahul','surname':'sharma'},
            {'Name':'Nikhil','surname':'Gupta'}
          ],
            'B':[
                {'Name':'pooja','surname':'Agrawal'},
                {'Name':'Mohit','Surname':'jaat'}
         ],
    },
     '12th':{
         'A':[{'Name':'aarati','surname':'mehara'},
              {'Name':'Tappu','surname':'Gada'}],

         'B':[{'Name':'Sonu','surname':'Rathor'},
              {'Name':'Jayesh','surname':'javed'}]
     },
 },
    'teachers':{
        'maths':[{'Name':'Mohansir','email':'mohansir@gmail.com','mobile':56789845},
                 {'Name':'Rathoresir','email':'Rathoresir@gmail.com','mobile':56464364}],
        'Chemistry':[{'Name':'KTmam','email':'KTmam@mail.com','mobile':876867896},
                     {'Name':'ruchiMam','email':'ruchimam@gmail.com','mobile':346535464}]
    },
}

from pprint import pprint
print("-"* 50)
pprint(school2['students']['11th']['A'][0]['Name'])
pprint(school2['teachers']['Chemistry'][0]['mobile'])
pprint(school2['teachers']['maths'][0]['email'])
pprint(school2['students']['12th']['B'][-1]['surname'])
pprint(school2['students']['12th']['A'][1]['surname'])


# Create a IT company dictionary  structive where we should have all there details
IT_Company = {
'HR':{
      'Recruiter HR':[{'Name':'Ram','email':'Ram@gmail.com','Mobile':'9876456667' },
                      {'Name': 'Rao','email':'Rao@gmail.com','Mobile':'987754356'}],

         'Activity HR':[{'Name':'Rak','email':'Rak@gmail.com','Mobile': '9776544567'},
                       {'Name':'Avani','email':'Avani@gmail.com', 'Mobile':'9887766698'}],

        'Payroll HR':[{'Name':'Aman','email':'Aman@gamil.com','Mobile':'9765543788'},
                      {'Name':'Akhil','email':'Akhil@gamil.com','Mobile':'8123789990'}],
},
  'Managers':{
        'Managers':[{'Name':'Gani','email':'Gani@gamil.com','Mobile':'8765432'},
                    {'Name':'Gowri','email':'Gowri@gmail.com','Mobile':'98765443'},
                    {'Name':'Gayatri','email':'Gayatri@gamil.com','Mobile':'879654332'}],

        'Team lead':[{'Name':'Rasi','email':'Rasi@gamil.com','Mobile':'9876543332'},
                    {'Name':'Akki','email':'Akki@gamil.com','Mobile':'977655443'},
                    {'Name':'Laxmi','email':'Laxmi@gmail.com','Mobile':'977654433'}],

        'Module lead':[{'Name':'Ram','email':'Ram@gamil.com','Mobile':'89976554'},
                     {'Name':'Arha','email':'Arha@gmail.com','Mobile':'6788909988'},
                     {'Name':'Rao','email':'Rao@gamil.com','Mobile':'7889995433'}],
  },

   'Development':{
               'UI dev':{
                        'Sr dev':[{ 'Name':'Hema','email':'heam@gmail.com','Mobile':'9866543333'},
                                 {'Name':'Bumi','email':'Bumi@gmail.com','Mobile':'567899900'}],
                        'Jr dev':[{'Name':'Hera','email':'hera@gamil.com','Mobile':'98765543678'},
                                 {'Name':'Nani','email':'Nani@gmail.com','Mobile':'9877766654'}],
               },
            'Api dev':{
                  'Sr dev': [{'Name': 'Manan', 'email': 'manan@gmail.com', 'Mobile': '9866543333'},
                             {'Name': 'Boomi', 'email': 'Boomi@gmail.com', 'Mobile': '567899900'}],
                  'Jr dev': [{'Name': 'Harsha', 'email': 'harsha@gamil.com', 'Mobile': '98765543678'},
                             {'Name': 'Nivi', 'email': 'Nivi@gmail.com', 'Mobile': '9877766654'}],
            },
      'Data base dev':{
                  'Sr dev': [{'Name': 'Madhu', 'email': 'madhu@gmail.com', 'Mobile': '9866543333'},
                             {'Name': 'Bujji', 'email': 'Bujji@gmail.com','Mobile': '567899900'}],
                  'Jr dev': [{'Name': 'Bindu', 'email': 'Bindu@gamil.com', 'Mobile': '98765543678'},
                             {'Name': 'Appu', 'email': 'Appu@gmail.com', 'Mobile': '9877766654'}],
      },
   },
 'Support':{
      'Internal Support':[{ 'Name':'Hema','email':'heam@gmail.com','Mobile':'9866543333'},
                        {'Name':'Bumi','email':'Bumi@gmail.com','Mobile':'567899900'}],
       'Customer Support':[{'Name':'Akki','email':'Akki@gmail.com','Mobile':'987666544'},
                         {'Name':'Roja','email':'Roja@gmail.com','Mobile':'98986544'}],
 },
  'Testing' :{
       'Manual Tester':[{'Name':'Rak','email':'Rak@gmail.com','Mobile': '9776544567'},
                        {'Name':'Avani','email':'Avani@gmail.com', 'Mobile':'9887766698'}],

      'Automation Tester':[{'Name':'Aman','email':'Aman@gamil.com','Mobile':'9765543788'},
                           {'Name':'Akhil','email':'Akhil@gamil.com','Mobile':'8123789990'}],
       'Performance Tester':[{'Name':'Ram','email':'Ram@gmail.com','Mobile':'9876456667' },
                             {'Name': 'Rao','email':'Rao@gmail.com','Mobile':'987754356'}],

        'Security Tester':[{'Name':'Rak','email':'Rak@gmail.com','Mobile': '9776544567'},
                            {'Name':'Avani','email':'Avani@gmail.com', 'Mobile':'9887766698'}],
  },
  'Administration':{
          'payroll admin':[{'Name':'Rak','email':'Rak@gmail.com','Mobile': '9776544567'},
                           {'Name':'Avani','email':'Avani@gmail.com', 'Mobile':'9887766698'}],

            'employee admin':[{'Name':'Aman','email':'Aman@gamil.com','Mobile':'9765543788'},
                              {'Name':'Akhil','email':'Akhil@gamil.com','Mobile':'8123789990'}],

         'facility admin':[{'Name': 'Bindu','email': 'Bindu@gamil.com', 'Mobile': '98765543678'},
                          {'Name': 'Appu','email':'Appu@gmail.com','Mobile': '9877766654'}],
   }
   }

#  practice
# 1)python program to add elements to the dictionary
dictionary={}
dictionary["Name"]="ketan"
dictionary["Age"]="21"
print(dictionary)
#2 print the squre of allvalues in a dictionary
dictionary ={'a':5,'b':3,'c':6,'d':8}
for val in dictionary:
    print(val,":",dictionary[val]**2)
#3 MOVE ITEMS FROM one dictionary to another dictionary
D1= {'name':'john','city':'london','country':'uk'}
D2 ={}
for val in D1:
    D2[val]=D1[val]
print(D2)
#4 program to contcatenate two dictionaries
dict1 ={'Name':'Harry','Rollno':345,'Address':'jorden'}
dict2 = {'Age':25,'salary':'$25k'}
dict1.update(dict2)
print(dict1)
#5 program to get a list of odd and even keys from the dictionary
dict1 ={1:25,5:'abc',8:'pqr',21:'XYZ',12:'def',2:'utv'}
list1= [[val,dict1[val]]for val in dict1 if val%2==0]
list2 = [[val,dict1[val]]for val in dict1 if val%2!=0]
print("Even key = ",list1)
print("odd key=",list2)
#6 python program to create a dictionrary from two lists
list1 = ['a,','b','c','d','e']
list2 = [12,23,24,25,15,16]
dict1={}
for a,b in zip(list1,list2):
    dict1[a] = b
    print(dict1)
#7 store squres of even and cubes of add numbers in a dictionary using dictionary comperension
list1 =[4,5,6,2,1,7,11]
dict={}
for val in list1:
    if val %2 ==0:
        dict[val] = val**2
    else:
        dict[val] =val**3
        print(dict)
        """
#8 python program to clear all items from the dictionary
dict1 = {'Name':'Harry','Rollno':345,'Address':'jorden'}
dict1.clear()
print(dict1)
#9 python program to remove duplicate values from dictionary
dict1 = {'a':12,'b':2,'c':12,'d':5,'e':35,'f':5}
dict2 ={}
for key,val in dict1.items():
    if val not in dict2.values():
        dict2[key]= val
    print(dict2)
# 10 python program to create a dictionary from the string
string ='SQATOOLSS'
dict1 ={}
for char in string:
    dict1[char]=string.count(char)
print(dict1)
#11 python program to sort a dictionary using keys
dict1 = {'d':21,'b':53,'a':13,'c':41}
for key in sorted (dict1):
print(dict1)
"""
#13 python progarm to add akey in a dictionary
dict1 = {1:'a',2:'b'}
dict1.update({3:'c'})
print(dict1)
#14 python program to concatenate two dictionaries to from a single dictionary
dict1 = {'name':'yash','City':'Pune'}
dict2 = {'course':'python','institute':'sqatools'}
dict1.update(dict2)
print(dict1)
#15 get the sum of all the items in a dictionary
D1 = {'x':23,'y':10,'z':7}
total =0
for val in D1.values():
    total+= val
    print (total)








