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




print("*"*50)


set1 = {1,2,44,56,56}

del set1

print(set1)




