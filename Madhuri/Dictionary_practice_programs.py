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
pprint(school2['teachers']['Chemistry'][2]['mobile'])
pprint(school2['teachers']['maths'][1]['email'])
pprint(school2['students']['12th']['B'][1]['surname'])
pprint(school2['students']['12th']['A'][1]['surname'])






