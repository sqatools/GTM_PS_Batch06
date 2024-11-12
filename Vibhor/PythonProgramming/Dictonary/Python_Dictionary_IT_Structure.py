"""
# Each employee should have name, email, phone number data in dictionary
# IT Company
         HR  -> Recruiter HR (2 employee)
             -> Activity HR  (2 employee)
             -> Payroll HR  (2 employee)

         Management -> Managers (3 employee)
                    -> Team lead (3 employee)
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

ITCompany = {
    'HR': {
        'Recruiter HR': [
            {'Name': 'Rahul', 'Email': 'rahul@gmail.com', 'Mobile': '9932324'},
            {'Name': 'Nikhil', 'Email': 'nikhil@gmail.com', 'Mobile': '42423646'}
        ],
        'Activity HR': [
            {'Name': 'Pooja', 'Email': 'pooja@gmail.com', 'Mobile': '45573466'},
            {'Name': 'Mohit', 'Email': 'mohit@gmail.com', 'Mobile': '34634636'}
        ],
        'Payroll HR': [
            {'Name': 'Amit', 'Email': 'amit@gmail.com', 'Mobile': '097032723'},
            {'Name': 'Shubham', 'Email': 'shubham@gmail.com', 'Mobile': '357497935'}
        ]
    },

    'Management': {
        'Managers': [
            {'Name': 'MohanSir', 'Email': 'mohansir@gmail.com', 'Mobile': '56789845'},
            {'Name': 'RathoreSir', 'Email': 'rathoresir@gmail.com', 'Mobile': '56464364'},
            {'Name': 'VikasSir', 'Email': 'vikassir@gmail.com', 'Mobile': '84245525'}
        ],
        'Team Lead': [
            {'Name': 'Michal', 'Email': 'michal@gmail.com', 'Mobile': '876867876'},
            {'Name': 'Rajshree', 'Email': 'rajshree@gmail.com', 'Mobile': '346535464'},
            {'Name': 'Alpana', 'Email': 'alpana@gmail.com', 'Mobile': '874039732'}
        ],
        'Module Lead': [
            {'Name': 'Sujal', 'Email': 'sujal@gmail.com', 'Mobile': '872367876'},
            {'Name': 'Kapil', 'Email': 'kapil@gmail.com', 'Mobile': '3923535464'},
            {'Name': 'Stuart', 'Email': 'stuart@gmail.com', 'Mobile': '8222039732'}
        ]
    },

    'Development': {
        'UI Dev': {
            'Sr Dev': [
                {'Name': 'Ashish', 'Email': 'ashish@gmail.com', 'Mobile': '2866492649'},
                {'Name': 'Akil', 'Email': 'akil@gmail.com', 'Mobile': '939239294'}
            ],
            'Jr Dev': [
                {'Name': 'Ujjwal', 'Email': 'ujjwal@gmail.com', 'Mobile': '42324324'},
                {'Name': 'Swanesh', 'Email': 'swanesh@gmail.com', 'Mobile': '3523523'}
            ],
        },
        'API Dev': {
            'Sr Dev': [
                {'Name': 'Krishna', 'Email': 'krishna@gmail.com', 'Mobile': '3223423'},
                {'Name': 'Arjun', 'Email': 'arjun@gmail.com', 'Mobile': '232352'}
            ],
            'Jr Dev': [
                {'Name': 'Aman', 'Email': 'aman@gmail.com', 'Mobile': '0324234'},
                {'Name': 'Abhay', 'Email': 'abhay@gmail.com', 'Mobile': '3523523'}
            ]
        },
        'Database Dev': [
            {'Name': 'Sonu', 'Email': 'sonu@gmail.com', 'Mobile': '352525'},
            {'Name': 'Anushree', 'Email': 'anushree@gmail.com', 'Mobile': '359242'}
        ]
    },

    'Support': {
        'Internal Support': [
            {'Name': 'Arvind', 'Email': 'arvind@gmail.com', 'Mobile': '299424'},
            {'Name': 'Piyush', 'Email': 'piyush@gmail.com', 'Mobile': '34235235'}
        ],
        'Customer Support': [
            {'Name': 'Matt', 'Email': 'matt@gmail.com', 'Mobile': '350295'},
            {'Name': 'Lijo', 'Email': 'lijo@gmail.com', 'Mobile': '95723'}
        ]
    },

    'Testing': {
        'Manual Tester': [
            {'Name': 'Vibhor', 'Email': 'vibhor@gmail.com', 'Mobile': '314134'},
            {'Name': 'Abhinav', 'Email': 'abhinav@gmail.com', 'Mobile': '3852035'}
        ],
        'Automation Tester': [
            {'Name': 'Vipul', 'Email': 'vipul@gmail.com', 'Mobile': '2947032'},
            {'Name': 'Vishwajeet', 'Email': 'vishwajeet@gmail.com', 'Mobile': '9385724'}
        ],
        'Performance Tester': [
            {'Name': 'Manu', 'Email': 'manu@gmail.com', 'Mobile': '93753'},
            {'Name': 'Deepak', 'Email': 'deepak@gmail.com', 'Mobile': '937092'}
        ],
        'Security Tester': [
            {'Name': 'Ritik', 'Email': 'ritik@gmail.com', 'Mobile': '3423523'},
            {'Name': 'Varun', 'Email': 'varun@gmil.com', 'Mobile': '323523'}
        ]
    },

    'Administration': {
        'Payroll Admin': [
            {'Name': 'Mayank', 'Email': 'mayank@gmail.com', 'Mobile': '387023'},
            {'Name': 'Rashmi', 'Email': 'rashmi@gmail.com', 'Mobile': '3288923'}
        ],
        'Employee Admin': [
            {'Name': 'Akshay', 'Email': 'akshay@gmail.com', 'Mobile': '9375037'},
            {'Name': 'Eshan', 'Email': 'eshan@gmail.com', 'Mobile': '32352'}
        ],
        'Facility Admin': [
            {'Name': 'Chhaya', 'Email': 'chhaya@gmail.com', 'Mobile': '83403'},
            {'Name': 'Garima', 'Email': 'garima@gmail.com', 'Mobile': '9375024'}
        ]
    }
}
