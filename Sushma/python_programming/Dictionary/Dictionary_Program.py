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
IT_company={
    'HR': {
        'Recruiter HR':[
            {'NAME':'Dimpu','Email':'Dimpu@gmail.com','Phone_no':'2864816826'},
            {'NAME':'sony','Email':'sony@gmail.com','Phone_no':'7266192978'},
        ],
        'Activity HR':[
            {'NAME': 'joni', 'Email': 'joni@gmail.com', 'Phone_no': '98987876868'},
            {'NAME': 'sheker', 'Email': 'sheker@gmail.com', 'Phone_no': '7454657778'},
        ],
        'Payroll HR ':[
            {'NAME': 'maya', 'Email': 'maya@gmail.com', 'Phone_no': '27687687686'},
            {'NAME': 'neha', 'Email': 'neha@gmail.com', 'Phone_no': '8977686868788'},
        ],
    },

    'Management':{

            'Managers':[
                {'NAME': 'anil', 'Email': 'anil@gmail.com', 'Phone_no': '793759735983'},
                {'NAME': 'kumar', 'Email': 'kumar@gmail.com', 'Phone_no': '93642624728'},
                {'NAME': 'pavan', 'Email': 'pavan@gmail.com', 'Phone_no': '734593879475'},
            ],
            'Teamlead':[
                {'NAME': 'sundeep', 'Email': 'sundeep@gmail.com', 'Phone_no': '8276262868'},
                {'NAME': 'sunil', 'Email': 'sunil@gmail.com', 'Phone_no': '126763878728'},
                {'NAME': 'rajesh', 'Email': 'rajesh@gmail.com', 'Phone_no': '628767618718'},

            ],

            'Module Lead':[
                {'NAME': 'sushma', 'Email': 'sushma@gmail.com', 'Phone_no': '617681638713'},
                {'NAME': 'akhila', 'Email': 'akhila@gmail.com', 'Phone_no': '868766776876'},
                {'NAME': 'rakesh', 'Email': 'rakesh@gmail.com', 'Phone_no': '8976776576787'},
            ],
    },


            'Development':{
                'UI Dev':{
                    'Sr Dev':[
                        {'NAME': 'jyothi', 'Email': 'jyothi@gmail.com', 'Phone_no': '617667877813'},
                        {'NAME': 'ravi', 'Email': 'ravi@gmail.com', 'Phone_no': '8685654476'},

                    ],
                    'jr Dev':[
                        {'NAME': 'paru', 'Email': 'paru@gmail.com', 'Phone_no': '61786456713'},
                        {'NAME': 'balaram', 'Email': 'balaram@gmail.com', 'Phone_no': '8678854776'},

                    ],
                },

                    'API Dev':{
                        'Sr Dev': [
                            {'NAME': 'vishnu', 'Email': 'vishnu@gmail.com', 'Phone_no': '617877813'},
                            {'NAME': 'parvathi', 'Email': 'parvathi@gmail.com', 'Phone_no': '8685864476'},

                        ],
                        'jr Dev': [
                            {'NAME': 'reddy', 'Email': 'reddy@gmail.com', 'Phone_no': '61766713'},
                            {'NAME': 'padhma', 'Email': 'padhma@gmail.com', 'Phone_no': '8688597776'},

                        ],
                    },


                        'Database Dev':{
                            'Sr Dev': [
                                {'NAME': 'rollex', 'Email': 'rollex@gmail.com', 'Phone_no': '6171237813'},
                                {'NAME': 'bhavya', 'Email': 'bhavya@gmail.com', 'Phone_no': '8095864476'},

                            ],
                            'jr Dev': [
                                {'NAME': 'rahul', 'Email': 'rahul@gmail.com', 'Phone_no': '61766709813'},
                                {'NAME': 'chaithanya', 'Email': 'chaithanya@gmail.com', 'Phone_no': '88890597776'},

                            ],
                        },
            'Support': {
                'Internal Support':  [
                        {'NAME': 'nani', 'Email': 'nani@gmail.com', 'Phone_no': '617687813'},
                        {'NAME': 'chaithu', 'Email': 'chaithu@gmail.com', 'Phone_no': '88890876776'},

                                ],
                'Customer Support':[
                        {'NAME': 'bantu', 'Email': 'bantu@gmail.com', 'Phone_no': '61096709813'},
                        {'NAME': 'babblu', 'Email': 'babblu@gmail.com', 'Phone_no': '8090597776'},

                                ],
                        },
                     ' Testing ':{
                                    'Manual Tester':[
                                        {'NAME': 'chintu', 'Email': 'chintu@gmail.com', 'Phone_no': '71096709813'},
                                        {'NAME': 'chinni', 'Email': 'chinni@gmail.com', 'Phone_no': '87990597776'},

                                    ],
                                    'Automation Tester': [
                                        {'NAME': 'abhi', 'Email': 'abhi@gmail.com', 'Phone_no': '6108709813'},
                                        {'NAME': 'siddu', 'Email': 'siddu@gmail.com', 'Phone_no': '0990597776'},

                                    ],
                                    'Performance Tester':[
                                        {'NAME': 'nirmala', 'Email': 'nirmala@gmail.com', 'Phone_no': '6100709813'},
                                        {'NAME': 'monesh', 'Email': 'monesh@gmail.com', 'Phone_no': '09911197776'},


                                    ],
                                    'Security Tester':[

                                        {'NAME': 'geeresh', 'Email': 'geeresh@gmail.com', 'Phone_no': '11108709813'},
                                        {'NAME': 'raj', 'Email': 'raj@gmail.com', 'Phone_no': '0909897776'},
                                    ],
                     },
                    'Administration':{
                                'Payroll admin': [
                                        {'NAME': 'vasu', 'Email': 'vasu@gmail.com', 'Phone_no': '6098709813'},
                                        {'NAME': 'swetha', 'Email': 'swetha@gmail.com', 'Phone_no': '0990598766'},

                                        ],
                                'Employee admin': [
                                         {'NAME': 'manu', 'Email': 'manu@gmail.com', 'Phone_no': '6108333813'},
                                        {'NAME': 'suni', 'Email': 'suni@gmail.com', 'Phone_no': '098767776'},
                                        ],
                                 'Facility admin ':[

                                            {'NAME': 'hema', 'Email': 'hema@gmail.com', 'Phone_no': '610666813'},
                                            {'NAME': 'venky', 'Email': 'venky@gmail.com', 'Phone_no': '099777776'},
                                        ],

                                    },


                                }


}








#print(IT_company['HR']['Recruiter HR'])
#print(IT_company['HR']['Activity HR'])
#print(IT_company['HR']['Payroll HR '])
#print(IT_company['Management']['Managers'])
#print(IT_company['Management']['Module Lead'])
#print(IT_company['Development']['UI Dev']['Sr Dev'])
#print(IT_company['Development']['UI Dev']['jr Dev'])

from pprint import pprint
pprint(IT_company)