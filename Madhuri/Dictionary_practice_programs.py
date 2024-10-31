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













