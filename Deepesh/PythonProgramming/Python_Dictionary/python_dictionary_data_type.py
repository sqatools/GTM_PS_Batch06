dict1 = {'a': 345}
print(dict1, type(dict1))
"""
# properties:
-> dict is mutable data type.
-> dict is store data in key value pair.
-> dict keys are always unique.
-> Only immutable data type are allowed as dict key, int, float, string, tuple, boolean
-> All type of data can be value in the dictionary.
-> Duplicate values are allowed in the dictionary
"""

dict2 = {'Name': 'Rahul'}
# dict is mutable data type.
dict2['Surname'] = 'Sharma'
print("dict2 :", dict2)  # {'Name': 'Rahul', 'Surname': 'Sharma'}

# dict keys are always unique.
# if duplicate keys are there then only latest data will be considered
dict3 = {'a': 456, 'b': 678, 'a': 123}
print("dict3 :", dict3)  # {'a': 123, 'b': 678}

print("_" * 50)
# Only immutable data type are allowed as dict key, int, float, string, tuple, boolean
dict4 = {123: 'Hello'}  # int as key
dict4[4.5] = 'Python'  # float as key
dict4['abc'] = [3, 6, 7]  # string as key
dict4[(1, 4, 6)] = {'p': 111, 'q': 222}  # tuple as key
dict4[True] = {3, 6, 8, 1}

print("dict4 :", dict4)
# {123: 'Hello', 4.5: 'Python', 'abc': [3, 6, 7], (1, 4, 6): {'p': 111, 'q': 222}, True: {8, 1, 3, 6}}

# mutable data types are not allowed as key e.g list, dict, set
"""
# dict4[[1, 2, 3]] = 'Programming'  # unhashable type: 'list'
print("dict4 :", dict4)
"""

print("_" * 40)
# duplicate values are allowed in dictionary
dict5 = {'a': 123, 'b': 123, 'c': 1234}
print("dict5 :", dict5, id(dict5))
# dict5 : {'a': 123, 'b': 123, 'c': 1234} 1756189564160
print("dict5 :", dict5['a'], id(dict5['a']))  # dict5 : 123 140732315883768
print("dict5 :", dict5['b'], id(dict5['b']))  # 123 140732315883768
print("dict5 :", dict5['c'], id(dict5['c']))  # 1234 2742543139120

print("_" * 50)
school = {
    'students': {
        '11th': [3, 5, 7],
        '12th': [1, 3, 5],
    },
    'teachers': {
        'maths': [6, 8, 0],
        'chemistry': [2, 5, 1],
    }
}
print(school['teachers']['maths'][1])  # 8
print(school['students']['12th'][-1])  # 5
print(school['students']['12th'][2])  # 5
print(school['students']['12th'])  # [1, 3, 5]

school2 = {
    'students': {
        '11th': {
            'A': [
                {'Name': 'Rahul', 'Surname': 'Sharma'},
                {'Name': 'Nikhil', 'Surname': 'Gupta'}
            ],
            'B': [
                {'Name': 'Pooja', 'Surname': 'Agrawal'},
                {'Name': 'Mohit', 'Surname': 'Jaat'}
            ],
        },
        '12th': {
            'A': [{'Name': 'aarti', 'Surname': 'mehra'}, {'Name': 'Tappu', 'Surname': 'Gada'}],
            'B': [{'Name': 'Sonu', 'Surname': 'Rathor'}, {'Name': 'jayesh', 'Surname': 'Javed'}]
        },
    },
    'teachers': {
        'maths': [{'Name': 'MohanSir', 'email': 'mohansir@gmail.com', 'mobile' : 56789845},
                  {'Name': 'RathoreSir', 'email': 'rathoresir@gmail.com', 'mobile' : 56464364}],
        'chemistry': [{'Name': 'KTMam', 'email': 'ktmam@gmail.com', 'mobile' : 876867876},
                  {'Name': 'ruchiMam', 'email': 'rauchimam@gmail.com', 'mobile' : 346535464}]
    }
}

from pprint import pprint
print("_"*50)
pprint(school2['students']['11th']['A'][0]['Name']) # Rahul
#1. get mobile number of KT mam
#2 get email address of mohansir
#3. get surname of jayesh
#4. get surname of tappu

# create a IT company dictionary structure where we should have all there details
"""
# Each employee should have name, email, phone number data in dictionary
# IT Company
         HR  -> Recruiter HR (2 employee)
             -> Activity HR  (2 employee)
             -> Payroll HR  (2 employee)
         
         Management -> Managers (3 employee)
                    -> Teamlead (3 employee)
                    -> Module Lead (3 employee)
                    
         Development -> UI Dev  -> Sr Dev (2 employee)
                                -> Jr Dev (2 Employee)
                     -> API Dev -> Sr Dev (2 employee)
                                -> Jr Dev (2 Employee)
                     -> Database Dev -> Sr Dev (2 employee)
                                    -> Jr Dev (2 Employee)
         
         Support ->  Internal Support  (2 employee)
                 ->  Customer Support (2 employee)
         Testing -> Manual Tester (2 employee)
                 -> Automation Tester (2 employee)
                 -> Performance Tester (2 employee)
                 -> Security Tester (2 employee)
                 
         Administration ->  Payroll admin (2 employee)
                        ->  Employee admin (2 employee)
                        ->  Facility admin (2 employee)
"""
