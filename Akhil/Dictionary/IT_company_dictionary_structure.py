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


Soft_tech = {
           "HR":{
               "Recruiter HR":[
                    {"Name":"Shiley", "Email":"Shiley@gmail.com", "Phone_number":9912345671},
                     {"Name":"Mohan", "Email":"Mohan@gmail.com", "Phone_number":9912345695}
               ],

               "Activity HR":[
                    {"Name":"Raju", "Email":"Raju@gmail.com", "Phone_number":9901234567},
                    {"Name":"Ram", "Email":"Ram@gmail.com", "Phone_number":8916234569}
               ],

               "Payroll HR":[
                    {"Name":"Raghu", "Email":"Raghu@gmail.com", "Phone_number":7191234567},
                    {"Name":"Keerthi", "Email":"kerthi@gmail.com", "Phone_number":9991234569}
               ]
            },

            "Management":{
                "Managers":[
                    {"Name":"Ajay", "Email":"Ajay@gmail.com","Phone_number":91912345671},
                    {"Name":"Avi", "Email":"Avi@gmail.com","Phone_number":7912345695},
                    {"Name":"jay", "Email":"jay@gmail.com","Phone_number":8191200671}
                ],
                "Teamlead":[
                    {"Name":"Sarab", "Email":"Arab@gmail.com", "Phone_number":9012345671},
                    {"Name":"Akhil", "Email":"Akhil@gmail.com", "Phone_number":79123456952},
                    {"Name":"Kumar", "Email":"Kumar@gmail.com", "Phone_number":8191255555}
                ],
                "Modulelead":[
                    {"Name":"Mounika", "Email":"mounika@gmail.com", "Phone_number":9033345671},
                    {"Name":"Adhipa", "Email":"Adhipa@gmail.com", "Phone_number":79155456952},
                    {"Name":"Ranjan", "Email":"Ranjan@gmail.com", "Phone_number":8111255555}
                ]

            },

             "Development":{
                 "UI Dev":{
                     "Sr Dev":[
                          {"Name":"Gayathri", "Email":"Gayathri@gmail.com", "Phone_number":991112345671},
                          {"Name":"Siva", "Email":"Siva@gmail.com", "Phone_number":99123777745695}
                       ],

                     "Jr Dev":[
                            {"Name":"Dinesh", "Email":"Dinesh@gmail.com", "Phone_number":991239990},
                            {"Name":"Kavya", "Email":"Kavya@gmail.com", "Phone_number":99123488895}
                      ]
                    }

            },

            "API Dev":{
                "Sr Dev":[
                    {"Name":"Akilesh", "Email":"Akilesh@gmail.com", "Phone_number":1222345671},
                    {"Name":"Ganesh", "Email":"Ganesh@gmail.com", "Phone_number":9123450695}
                ],
                "Jr Dev":[
                    {"Name":"Ramnath", "Email":"Ramnath@gmail.com", "Phone_number":22212345671},
                    {"Name":"Nandu", "Email":"nandu@gmail.com", "Phone_number":1234569500}
                ]
            },
            "Database Dev":{
                "Sr Dev":[
                    {"Name":"Sai", "Email":"Sai@gmail.com", "Phone_number":9988845671},
                    {"Name":"Sugeeth", "Email":"Sugeeth@gmail.com", "Phone_number":456999995}
                ],
                "Jr Dev":[
                    {"Name":"Durga", "Email":"Durga@gmail.com", "Phone_number":6000612345671},
                    {"Name":"Sachin", "Email":"Sachin@gmail.com", "Phone_number":90000345695}
                ]
             },


            "Support":{
                 "Internal Support": [
                    {"Name":"Prakash", "Email":"Prakash@gmail.com", "Phone_number":66612345671},
                    {"Name":"Prudhvi", "Email":"Prudhvi@gmail.com", "Phone_number":90002345695}

                 ],
                 "Customer Support":[
                    {"Name":"Pranavi", "Email":"Pranavi@gmail.com", "Phone_number":69612345671},
                    {"Name":"Eswar", "Email":"Eswar@gmail.com", "Phone_number":90102345695}
                 ],

             },
             "Testing" :{
                 "Manual Tester":[
                    {"Name":"Nasir", "Email":"Nasir@gmail.com", "Phone_number":696111112345671},
                    {"Name":"Nikhil", "Email":"Nikhil@gmail.com", "Phone_number":901023111145695}
                 ],
                 "Automation Tester":[
                     {"Name":"vinod", "Email":"vinod@gmail.com", "Phone_number":69612333345671},
                     {"Name":"srinu", "Email":"srinu@gmail.com", "Phone_number":908888102345695}
                 ],
                 "Performance Tester":[
                    {"Name":"Prasad", "Email":"Prasad@gmail.com", "Phone_number":60009612345671},
                    {"Name":"Murthy", "Email":"Murthy@gmail.com", "Phone_number":9010231145695}
                 ],
                 "Security Tester":[
                    {"Name":"Tester1", "Email":"tester1@gmail.com", "Phone_number":692222345671},
                    {"Name":"Tester2", "Email":"tester2@gmail.com", "Phone_number":90111102345695}
                 ]

        },
          "Administration":{
                 "Payroll admin":[
                    {"Name":"Pooja", "Email":"Pooja@gmail.com", "Phone_number":69999995671},
                    {"Name":"Tapas", "Email":"Tapas@gmail.com", "Phone_number":90999345695}
                 ],
                 "Employee admin":[
                    {"Name":"karan", "Email":"karan@gmail.com", "Phone_number":11112345671},
                    {"Name":"sneha", "Email":"sneha@gmail.com", "Phone_number":90100005695}
                  ],
                 "Facility admin":[
                    {"Name":"venky", "Email":"venky@gmail.com", "Phone_number":8888612345671},
                    {"Name":"Nagarjuna", "Email":"Nagarjuna@gmail.com", "Phone_number":90188845695}
                 ]

           }
   }
