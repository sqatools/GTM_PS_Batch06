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
pprint(school2)
#pprint(school2['students']['11th']['A'][0]['Name']) # Rahul
#1. get mobile numb er of KT mam
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


it_company = {
    'HR': {
        'Recruiter HR': [
            {'name': 'Aarav Sharma', 'email': 'aarav.sharma@itcompany.com', 'phone': '987-654-3210'},
            {'name': 'Ishita Verma', 'email': 'ishita.verma@itcompany.com', 'phone': '987-654-3211'}
        ],
        'Activity HR': [
            {'name': 'Ananya Reddy', 'email': 'ananya.reddy@itcompany.com', 'phone': '987-654-3212'},
            {'name': 'Karan Singh', 'email': 'karan.singh@itcompany.com', 'phone': '987-654-3213'}
        ],
        'Payroll HR': [
            {'name': 'Priya Patel', 'email': 'priya.patel@itcompany.com', 'phone': '987-654-3214'},
            {'name': 'Vikram Joshi', 'email': 'vikram.joshi@itcompany.com', 'phone': '987-654-3215'}
        ]
    },
    'Management': {
        'Managers': [
            {'name': 'Sanya Gupta', 'email': 'sanya.gupta@itcompany.com', 'phone': '987-654-3216'},
            {'name': 'Rohit Mehta', 'email': 'rohit.mehta@itcompany.com', 'phone': '987-654-3217'},
            {'name': 'Meera Chawla', 'email': 'meera.chawla@itcompany.com', 'phone': '987-654-3218'}
        ],
        'Teamlead': [
            {'name': 'Kabir Kapoor', 'email': 'kabir.kapoor@itcompany.com', 'phone': '987-654-3219'},
            {'name': 'Simran Bhatia', 'email': 'simran.bhatia@itcompany.com', 'phone': '987-654-3220'},
            {'name': 'Aditya Sethi', 'email': 'aditya.sethi@itcompany.com', 'phone': '987-654-3221'}
        ],
        'Module Lead': [
            {'name': 'Riya Nair', 'email': 'riya.nair@itcompany.com', 'phone': '987-654-3222'},
            {'name': 'Neeraj Malhotra', 'email': 'neeraj.malhotra@itcompany.com', 'phone': '987-654-3223'},
            {'name': 'Divya Yadav', 'email': 'divya.yadav@itcompany.com', 'phone': '987-654-3224'}
        ]
    },
    'Development': {
        'UI Dev': {
            'Sr Dev': [
                {'name': 'Rahul Rao', 'email': 'rahul.rao@itcompany.com', 'phone': '987-654-3225'},
                {'name': 'Neha Mishra', 'email': 'neha.mishra@itcompany.com', 'phone': '987-654-3226'}
            ],
            'Jr Dev': [
                {'name': 'Tara Kulkarni', 'email': 'tara.kulkarni@itcompany.com', 'phone': '987-654-3227'},
                {'name': 'Amit Deshmukh', 'email': 'amit.deshmukh@itcompany.com', 'phone': '987-654-3228'}
            ]
        },
        'API Dev': {
            'Sr Dev': [
                {'name': 'Rajesh Menon', 'email': 'rajesh.menon@itcompany.com', 'phone': '987-654-3229'},
                {'name': 'Pooja Ghosh', 'email': 'pooja.ghosh@itcompany.com', 'phone': '987-654-3230'}
            ],
            'Jr Dev': [
                {'name': 'Manoj Choudhury', 'email': 'manoj.choudhury@itcompany.com', 'phone': '987-654-3231'},
                {'name': 'Lavanya Shetty', 'email': 'lavanya.shetty@itcompany.com', 'phone': '987-654-3232'}
            ]
        },
        'Database Dev': {
            'Sr Dev': [
                {'name': 'Anil Gupta', 'email': 'anil.gupta@itcompany.com', 'phone': '987-654-3233'},
                {'name': 'Shalini Iyer', 'email': 'shalini.iyer@itcompany.com', 'phone': '987-654-3234'}
            ],
            'Jr Dev': [
                {'name': 'Gautam Kulkarni', 'email': 'gautam.kulkarni@itcompany.com', 'phone': '987-654-3235'},
                {'name': 'Sanya Bajaj', 'email': 'sanya.bajaj@itcompany.com', 'phone': '987-654-3236'}
            ]
        }
    },
    'Support': {
        'Internal Support': [
            {'name': 'Devika Singh', 'email': 'devika.singh@itcompany.com', 'phone': '987-654-3237'},
            {'name': 'Ajay Pawar', 'email': 'ajay.pawar@itcompany.com', 'phone': '987-654-3238'}
        ],
        'Customer Support': [
            {'name': 'Ritu Jain', 'email': 'ritu.jain@itcompany.com', 'phone': '987-654-3239'},
            {'name': 'Naveen Khan', 'email': 'naveen.khan@itcompany.com', 'phone': '987-654-3240'}
        ]
    },
    'Testing': {
        'Manual Tester': [
            {'name': 'Radhika Basu', 'email': 'radhika.basu@itcompany.com', 'phone': '987-654-3241'},
            {'name': 'Suresh Patil', 'email': 'suresh.patil@itcompany.com', 'phone': '987-654-3242'}
        ],
        'Automation Tester': [
            {'name': 'Mitali Joshi', 'email': 'mitali.joshi@itcompany.com', 'phone': '987-654-3243'},
            {'name': 'Vishal Prasad', 'email': 'vishal.prasad@itcompany.com', 'phone': '987-654-3244'}
        ],
        'Performance Tester': [
            {'name': 'Shruti Kulkarni', 'email': 'shruti.kulkarni@itcompany.com', 'phone': '987-654-3245'},
            {'name': 'Akash Desai', 'email': 'akash.desai@itcompany.com', 'phone': '987-654-3246'}
        ],
        'Security Tester': [
            {'name': 'Tanvi Kapoor', 'email': 'tanvi.kapoor@itcompany.com', 'phone': '987-654-3247'},
            {'name': 'Rakesh Rao', 'email': 'rakesh.rao@itcompany.com', 'phone': '987-654-3248'}
        ]
    },
    'Administration': {
        'Payroll admin': [
            {'name': 'Parul Nair', 'email': 'parul.nair@itcompany.com', 'phone': '987-654-3249'},
            {'name': 'Sameer Ahuja', 'email': 'sameer.ahuja@itcompany.com', 'phone': '987-654-3250'}
        ],
        'Employee admin': [
            {'name': 'Sneha Reddy', 'email': 'sneha.reddy@itcompany.com', 'phone': '987-654-3251'},
            {'name': 'Ravi Sharma', 'email': 'ravi.sharma@itcompany.com', 'phone': '987-654-3252'}
        ],
        'Facility admin': [
            {'name': 'Meghna Dixit', 'email': 'meghna.dixit@itcompany.com', 'phone': '987-654-3253'},
            {'name': 'Vijay Goel', 'email': 'vijay.goel@itcompany.com', 'phone': '987-654-3254'}
        ]
    }
}
print("_"*40)


########################
dict4 = {'a':123, 'b': 567}
print(dict4.items())  # dict_items([('a', 123), ('b', 567)])

for val in dict4.items():
    print(val)
"""
('a', 123)
('b', 567)
"""

for k, v in dict4.items():
    print("key :", k, "value :", v)

"""
key : a value : 123
key : b value : 567
"""

###############################
print("_"*50)
school3 = {
    'students': {
        '11th': [3, 5, 7],
        '12th': [1, 3, 5],
    },
    'teachers': {
        'maths': [6, 8, 0],
        'chemistry': [2, 5, 1],
    }
}


for p, q in school3.items():
    print(p,"::", q)
"""
students :: {'11th': [3, 5, 7], '12th': [1, 3, 5]}
teachers :: {'maths': [6, 8, 0], 'chemistry': [2, 5, 1]}
"""

print("_"*40)
for k, v in school3.items():
    #print(k,"::", v)
    for k1, v1 in v.items():
        #print(k1, "||", v1)
        for val in v1:
            print(val)
        #print("_"*40)

#########################################
school4 = {
    'students': {
        '11th': {
            'A': [
                {'Name': 'Rahul', 'Surname': 'Sharma'},
                {'Name': 'Nikhil', 'Surname': 'Gupta'},
                {'Name': 'Nikhil1', 'Surname': 'Gupta'},
                {'Name': 'Nikhil2', 'Surname': 'Gupta'},
                {'Name': 'Nikhil3', 'Surname': 'Gupta'},
                {'Name': 'Nikhil4', 'Surname': 'Gupta'},
                {'Name': 'Nikhil5', 'Surname': 'Gupta'},
                {'Name': 'Nikhil6', 'Surname': 'Gupta'},

            ],
            'B': [
                {'Name': 'Pooja', 'Surname': 'Agrawal'},
                {'Name': 'Mohit', 'Surname': 'Jaat'}
            ],
        },
        '12th': {
            'A': [{'Name': 'aarti', 'Surname': 'mehra'}, {'Name': 'Tappu', 'Surname': 'Gada'}, {'Name': 'Pooja', 'Surname': 'Gupta'}],
            'B': [{'Name': 'Sonu', 'Surname': 'Rathor'}, {'Name': 'jayesh', 'Surname': 'Javed'},
                  {'Name': 'Pooja', 'Surname': 'Sharma', 'phone' : 456789232},  {'Name': 'Pooja', 'Surname': 'Rathor', 'phone': 545436565}]
        },
    },
    'teachers': {
        'maths': [{'Name': 'MohanSir', 'email': 'mohansir@gmail.com', 'mobile' : 56789845},
                  {'Name': 'RathoreSir', 'email': 'rathoresir@gmail.com', 'mobile' : 56464364}],
        'chemistry': [{'Name': 'KTMam', 'email': 'ktmam@gmail.com', 'mobile' : 876867876},
                   {'Name': 'ruchiMam', 'email': 'rauchimam@gmail.com', 'mobile' : 346535464}]
    }
}


print("_"*50)
"""
st_name = 'Pooja'
for k, v in school4.items():
    if k == 'students':
        #print(k, "::", v)
        for k1, v1, in v.items():
            #print(k1, "::", v1)
            for k2, v2 in v1.items():
                #print(k2, "::", v2)
                for val in v2:
                    if val['Name'] == st_name:
                        print(val)

"""

"""
# Apply multiple filter to avoid duplicate name
st_name = 'Pooja'
class_name = "12th"
section = 'B'

for k, v in school4.items():
    if k == 'students':
        #print(k, "::", v)
        for k1, v1, in v.items():
            #print(k1, "::", v1)
            if k1 == class_name:
                for k2, v2 in v1.items():
                    if k2 == section:
                        #print(k2, "::", v2)
                        for val in v2:
                            if val['Name'] == st_name:
                                print(val)

"""

# get student data from database using mobile filter
phone_number = 456789232
for k, v in school4.items():
    if k == 'students':
        #print(k, "::", v)
        for k1, v1, in v.items():
            #print(k1, "::", v1)
            for k2, v2 in v1.items():
                #print(k2, "::", v2)
                for val in v2:
                    if 'phone' in val:
                        if val['phone'] == phone_number:
                            print(val)

