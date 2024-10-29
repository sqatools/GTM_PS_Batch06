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
        'maths': [{'Name': 'MohanSir', 'email': 'mohansir@gmail.com', 'mobile' : '56789845'},
                  {'Name': 'RathoreSir', 'email': 'rathoresir@gmail.com', 'mobile' : '56464364'}],
        'chemistry': [{'Name': 'KTMam', 'email': 'ktmam@gmail.com', 'mobile' : '876867876'},
                  {'Name': 'ruchiMam', 'email': 'rauchimam@gmail.com', 'mobile' : '346535464'}]
    }
}

#1. get mobile number of KT mam
#2 get email address of mohansir
#3. get surname of jayesh
#4. get surname of tappu

#1-
from pprint import pprint
pprint(school2['teachers']['chemistry'][0]['mobile'])
#2-
pprint(school2['teachers']['maths'][0]['email'])
#3-
pprint(school2['students']['12th']['B'][-1]['Surname'])
#4-
pprint(school2['students']['12th']['A'][-1]['Surname'])