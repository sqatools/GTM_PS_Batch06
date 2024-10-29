from pprint import pprint

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
        'maths': [{'Name': 'MohanSir', 'email': 'mohansir@gmail.com', 'mobile': 56789845},
                  {'Name': 'RathoreSir', 'email': 'rathoresir@gmail.com', 'mobile': 56464364}],
        'chemistry': [{'Name': 'KTMam', 'email': 'ktmam@gmail.com', 'mobile': 876867876},
                      {'Name': 'ruchiMam', 'email': 'rauchimam@gmail.com', 'mobile': 346535464}]
    }
}

"""# pprint(school2)

# 1.get mobile number of KT mam
pprint(school2['teachers']['chemistry'][0]['mobile'])

# 2.get email address of mohansir
pprint(school2['teachers']['maths'][0]['email'])

# 3.get surname of jayesh
pprint(school2['students']['12th']['B'][1]['Surname'])

# 4.get surname of tappu
pprint(school2['students']['12th']['A'][1]['Surname'])"""

IT_Company = {
    'HR': {
        'Recruiter HR': [
            {'Name': 'Priya', 'email': 'priya@gmail.com', 'phone': 94857637},
            {'Name': 'Sheetal', 'email': 'sheetal@gmail.com', 'phone': 5463762547}
        ],
        'Activity HR': [
            {'Name': 'Rahul', 'email': 'rahul@gmail.com', 'phone': 86759489},
            {'Name': 'John', 'email': 'john@gmail.com', 'phone': 857494739}
        ],
        'Payroll HR': [
            {'Name': 'Ravi', 'email': 'ravi@gmail.com', 'phone': 674847594},
            {'Name': 'Teja', 'email': 'teja@gmail.com', 'phone': 564739385}
        ]
    },
    'Management': {
        'Manager': [
            {'Name': 'Nikhil', 'email': 'nikhil@gmail.com', 'phone': 758474958},
            {'Name': 'Raju', 'email': 'raju@gmail.com', 'phone': 94857637},
            {'Name': 'Ramya', 'email': 'ramya@gmail.com', 'phone': 857494739}
        ],
        'TeamLead': [
            {'Name': 'Jyoti', 'email': 'jyoti@gmail.com', 'phone': 7685945867},
            {'Name': 'Jagadeesh', 'email': 'jagadeesh123@gmail.com', 'phone': 859475839},
            {'Name': 'likith', 'email': 'likith4@gmail.com', 'phone': 8674948594}
        ],
        'ModuleLead': [
            {'Name': 'Jack', 'email': 'jack90@gmail.com', 'phone': 8674948759},
            {'Name': 'Priya', 'email': 'priya@gmail.com', 'phone': 94857637},
            {'Name': 'Joeseph', 'email': 'joe34#@gmail.com', 'phone': 76859587}
        ]
    },
    'Development': {
        'UI dev': {
            'Sr dev': [
                {'Name': 'Roja', 'email': 'roja@gmail.com', 'phone': 8593740938},
                {'Name': 'Neha', 'email': '345neha@gmail.com', 'phone': 86049589}
            ],
            'Jr dev': [
                {'Name': 'Lohit', 'email': 'lohi567@gmail.com', 'phone': 7584903485},
                {'Name': 'Mohit', 'email': 'mohit87@gmail.com', 'phone': 94857637}
            ]
        },
        'API dev': {
            'Sr dev': [
                {'Name': 'Lavanya', 'email': 'lavany56@gmail.com', 'phone': 86795849},
                {'Name': 'Trilok', 'email': '111trilok@gmail.com', 'phone': 46573847}
            ],
            'Jr dev': [
                {'Name': 'Gupta', 'email': 'gupta@gmail.com', 'phone': 6759685058},
                {'Name': 'Niraj', 'email': 'niraj43@gmail.com', 'phone': 7685749574}
            ]
        },
        'Database dev': {
            'Sr dev': [
                {'Name': 'Virat', 'email': 'virat@gmail.com', 'phone': 86759578549},
                {'Name': 'Sachin', 'email': 'sachin65@gmail.com', 'phone': 868459789}
            ],
            'Jr dev': [
                {'Name': 'Shreya', 'email': 'shreya#123@gmail.com', 'phone': 759475948},
                {'Name': 'Kajol', 'email': 'kajol@gmail.com', 'phone': 75947958}
            ]
        }
    },
    'Support': {
        'Internal support': [
            {'Name': 'Riya', 'email': 'riya@gmail.com', 'phone': 879589670},
            {'Name': 'Suresh', 'email': 'suresh345@gmail.com', 'phone': 869578695}
        ],
        'Customer support': [
            {'Name': 'Ramesh', 'email': 'ramesh34@gmail.com', 'phone': 76986749},
            {'Name': 'Naresh', 'email': 'naresh@gmail.com', 'phone': 7696859}
        ]
    },
    'Testing': {
        'Manual tester': [
            {'Name': 'Lisa', 'email': 'lisa@gmail.com', 'phone': 785758457},
            {'Name': 'Mounika', 'email': '65mounika@gmail.com', 'phone': 468574899}
        ],
        'Automation tester': [
            {'Name': 'Ricky', 'email': 'ricky@gmail.com', 'phone': 75947958},
            {'Name': 'Vicky', 'email': 'vicky@gmail.com', 'phone': 758465857}
        ],
        'Performance tester': [
            {'Name': 'Manoj', 'email': 'manoj14@gmail.com', 'phone': 57648576},
            {'Name': 'Sharma', 'email': 'sharma@gmail.com', 'phone': 759475947}
        ],
        'Security tester': [
            {'Name': 'Deepthi', 'email': 'deepthi@gmail.com', 'phone': 75947958},
            {'Name': 'Shradha', 'email': 'shradha23@gmail.com', 'phone': 75648546}
        ]
    },
    'Administration': {
        'Payroll admin': [
            {'Name': 'Prateek', 'email': 'prateek@gmail.com', 'phone': 75648579},
            {'Name': 'Kaur', 'email': 'kaur@gmail.com', 'phone': 46585748}
        ],
        'Employee admin': [
            {'Name': 'Viplav', 'email': 'viplav@gmail.com', 'phone': 476584658},
            {'Name': 'Viraj', 'email': 'viraj@gmail.com', 'phone': 47564585675}
        ],
        'Facility admin': [
            {'Name': 'Mehak', 'email': 'mehak67@gmail.com', 'phone': 84759547},
            {'Name': 'Arora', 'email': 'arora@gmail.com', 'phone': 8467584374}
        ]
    }
}
pprint(IT_Company)
