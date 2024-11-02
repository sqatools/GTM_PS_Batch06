Company = {
    'HR': {
            'Recruiter HR':[
                          {'Name': 'Aice', 'email': 'alice.johnson@gmail.com', 'mobile' : 1234567},
                          {'Name': 'david', 'email': 'david.lee@gmail.com', 'mobile' : 7890123}
            ],
            'Activity HR':[
                          {'Name': 'lee', 'email': 'lee.san@gmail.com', 'mobile' : 2345678},
                          {'Name': 'emily', 'email': 'emily.brown@gmail.com', 'mobile' : 6789012}
            ],
            'Payroll HR ':[
                          {'Name': 'georage', 'email': 'george.smith@gmail.com', 'mobile' : 3456789},
                          {'Name': 'hannah', 'email': 'hannah.white@gmail.com', 'mobile' : 4567890}
            ],
        },
    'Management': {
            'Managers':[
                          {'Name': 'Brown', 'email': 'Brown.johnson@gmail.com', 'mobile' : 1204567},
                          {'Name': 'SMith', 'email': 'SMith.lee@gmail.com', 'mobile' : 7800123},
                          {'Name': 'White', 'email': 'White.lee@gmail.com', 'mobile' : 7800123}
            ],
            'Teamlead':[
                          {'Name': 'isaac', 'email': 'isaac.san@gmail.com', 'mobile' : 2945678},
                          {'Name': 'clark', 'email': 'clark.brown@gmail.com', 'mobile' : 9789012},
                          {'Name': 'peter', 'email': 'peter.lee@gmail.com', 'mobile' : 7090123}
            ],
            'Module Lead':[
                          {'Name': 'georage', 'email': 'george.smith@gmail.com', 'mobile' : 3456789},
                          {'Name': 'hannah', 'email': 'hannah.white@gmail.com', 'mobile' : 4567890},
                          {'Name': 'david', 'email': 'david.lee@gmail.com', 'mobile' : 7890123}
            ],
        },
    'Development': {
        'UI Dev' : {
            'Sr Dev':[
                          {'Name': 'florain', 'email': 'florain.johnson@gmail.com', 'mobile' : 1204567},
                          {'Name': 'vignet', 'email': 'vignet.lee@gmail.com', 'mobile' : 7800123}
            ],
            'Jr Dev':[
                          {'Name': 'michael', 'email': 'michael.san@gmail.com', 'mobile' : 2945678},
                          {'Name': 'jagadish', 'email': 'jagadish.brown@gmail.com', 'mobile' : 9789012}
            ],
            },
        'API Dev' : {
            'Sr Dev':[
                          {'Name': 'ask', 'email': 'ask.johnson@gmail.com', 'mobile' : 1304567},
                          {'Name': 'moller', 'email': 'moller.lee@gmail.com', 'mobile' : 7800123}
            ],
            'Jr Dev':[
                          {'Name': 'green', 'email': 'green.san@gmail.com', 'mobile' : 2935678},
                          {'Name': 'wood', 'email': 'wood.brown@gmail.com', 'mobile' : 97859012}
            ],
        },
        'Database Dev ' : {
            'Sr Dev':[
                          {'Name': 'acme', 'email': 'crop.johnson@gmail.com', 'mobile' : 1204567},
                          {'Name': 'SMith', 'email': 'SMith.lee@gmail.com', 'mobile' : 7800123}
            ],
            'Jr Dev':[
                          {'Name': 'frdeick', 'email': 'fedrick.san@gmail.com', 'mobile' : 2945378},
                          {'Name': 'angles', 'email': 'angles.brown@gmail.com', 'mobile' : 9782012}
            ],
            }
        },
    'Support' : {
       'Internal Support':[
                          {'Name': 'Aice', 'email': 'alice.johnson@gmail.com', 'mobile' : 71234567},
                          {'Name': 'david', 'email': 'david.lee@gmail.com', 'mobile' : 87890123}
            ],
        'Customer Support':[
                          {'Name': 'erica', 'email': 'erica.san@gmail.com', 'mobile' : 32345678},
                          {'Name': 'cheryl', 'email': 'cheryl.brown@gmail.com', 'mobile' : 46789012}
            ],
        },
    'Testing' : {
       'Manual Tester':[
                          {'Name': 'monami', 'email': 'alice.monami@gmail.com', 'mobile' : 7234567},
                          {'Name': 'sarah', 'email': 'smith.lee@gmail.com', 'mobile' : 78990123}
            ],
        'Automation Tester':[
                          {'Name': 'graham', 'email': 'moon.san@gmail.com', 'mobile' : 2349965678},
                          {'Name': 'johnn', 'email': 'erica.brown@gmail.com', 'mobile' : 556789012}
            ],
        'Performance Tester':[
                          {'Name': 'Aice', 'email': 'alice.johnson@gmail.com', 'mobile' : 1234567},
                          {'Name': 'david', 'email': 'david.lee@gmail.com', 'mobile' : 7890123}
            ],
        'Security Tester':[
                          {'Name': 'lee', 'email': 'lee.san@gmail.com', 'mobile' : 2345678},
                          {'Name': 'emily', 'email': 'emily.brown@gmail.com', 'mobile' : 6789012}
            ],
    },
        'Administration': {
        'Payroll admin':[
                          {'Name': 'janelle', 'email': 'lee.monami@gmail.com', 'mobile' : 27234567},
                          {'Name': 'alex', 'email': 'alex.lee@gmail.com', 'mobile' : 478990123}
            ],
        'Employee admin':[
                          {'Name': 'maple', 'email': 'maple.san@gmail.com', 'mobile' : 52349965678},
                          {'Name': 'olivia', 'email': 'olivia.brown@gmail.com', 'mobile' : 6556789012}
            ],
        'Facility admin':[
                          {'Name': 'whisperer', 'email': 'code.johnson@gmail.com', 'mobile' : 97951234567},
                          {'Name': 'birch', 'email': 'birch.lee@gmail.com', 'mobile' : 378901293}
            ]
       }
}
from pprint import pprint
print("_"*50)
pprint(Company)
#pprint(Company['Employee'])

#------------------------------------------------------------------------------
#print("_"*50)
for p, q in Company.items():
    #print(p, ":", q)
    for p1, q1 in q.items():
       #print(p1,":",q1)
       if isinstance(q1, list):
           for value in q1:
            print(value)
       elif isinstance(q1, dict):
           for p2, q2 in q1.items():
               #print(p2, ":", q2)
               for value in q2:
                   print(value)
