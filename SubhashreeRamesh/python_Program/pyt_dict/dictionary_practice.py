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
print("KTMam Mobile:", school2['teachers']['chemistry'][0]['mobile'])
#2 get email address of mohansir
print("Mohansir email:", school2['teachers']['maths'][0]['email'])
#3. get surname of jayesh
print("Surname of jayesh:", school2['students']['12th']['B'][1]['Surname'])
#4. get surname of tappu
print("Surname of tappu:", school2['students']['12th']['A'][1]['Surname'])

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
ITcompany = {
    'HR':{
    'Recruiter HR':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}
    ],

    'Activity HR':[
        {'Name': 'daniel','Email_id':'danielit@gmail.com','mobile':7236974},
        {'Name': 'zozhi','Email_id':'zozhiit@gmail.com','mobile':4856144}
    ],
    'Payroll HR':[
        {'Name': 'smrithi','Email_id':'smrithiit@gmail.com','mobile':757444745},
        {'Name': 'bogie','Email_id':'bogieit@gmail.com','mobile':15963414}
    ],
},
    'Management':{
    'Managers':[
        {'Name': 'Hetty','Email_id':'hettyit@gmail.com','mobile':74122565},
        {'Name': 'linapae','Email_id':'linapaeit@gmail.com','mobile':15965522275},
        {'Name': 'Alberta','Email_id':'albertait@gmail.com','mobile':74125222563}
    ],

    'Team Lead':[
        {'Name': 'isaac','Email_id':'isaacit@gmail.com','mobile':7232895274},
        {'Name': 'thorfinn','Email_id':'thorfinnit@gmail.com','mobile':485256355},
        {'Name': 'trevor','Email_id':'trevorit@gmail.com','mobile':5463232}
    ],
    'Module Lead':[
        {'Name': 'flower','Email_id':'flowerit@gmail.com','mobile':125238963},
        {'Name': 'pete','Email_id':'peteit@gmail.com','mobile':151112475},
        {'Name': 'elias','Email_id':'eliasit@gmail.com','mobile':25558963}
    ],
},
'Development':{
    'UI Developer':{
        'Senior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}],
        'Junior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}]
    },

    'API Developer':{
        'Senior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}],
        'Junior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}]
    },

    'Database Developer':{
        'Senior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}],
        'Junior Developer':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}]
    },

},
    'Support':{
    'Internal Support':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}
    ],

    'Customer Support':[
        {'Name': 'daniel','Email_id':'danielit@gmail.com','mobile':7236974},
        {'Name': 'zozhi','Email_id':'zozhiit@gmail.com','mobile':4856144}
    ]
},
    'Testing':{
    'Manual Tester':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}
    ],

    'Automation Tester':[
        {'Name': 'daniel','Email_id':'danielit@gmail.com','mobile':7236974},
        {'Name': 'zozhi','Email_id':'zozhiit@gmail.com','mobile':4856144}
    ],
    'Performance Tester':[
        {'Name': 'daniel','Email_id':'danielit@gmail.com','mobile':7236974},
        {'Name': 'zozhi','Email_id':'zozhiit@gmail.com','mobile':4856144}
    ],
    'Security Tester':[
        {'Name': 'smrithi','Email_id':'smrithiit@gmail.com','mobile':757444745},
        {'Name': 'bogie','Email_id':'bogieit@gmail.com','mobile':15963414}
    ],
},
    'Administration':{
    'payroll admin':[
        {'Name': 'silas','Email_id':'silasit@gmail.com','mobile':741258963},
        {'Name': 'mila','Email_id':'milait@gmail.com','mobile':15963475}
    ],

    'Employee admin':[
        {'Name': 'daniel','Email_id':'danielit@gmail.com','mobile':7236974},
        {'Name': 'zozhi','Email_id':'zozhiit@gmail.com','mobile':4856144}
    ],
    'Facility admin':[
        {'Name': 'smrithi','Email_id':'smrithiit@gmail.com','mobile':757444745},
        {'Name': 'bogie','Email_id':'bogieit@gmail.com','mobile':15963414}
    ],
}
}


pprint(ITcompany)