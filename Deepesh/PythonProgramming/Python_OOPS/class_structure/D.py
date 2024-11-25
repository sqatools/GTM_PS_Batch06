from C import Train

class BOOKING(Train):
    db_username = 'admin'
    db_password = 'admin@123'

    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

    def login(self):
        if self.username == self.db_username and self.password == self.db_password:
            print("Login Successful")
        else:
            print("Invalid Username and Password")


obj = BOOKING('admin', 'admin@123')
obj.login()

print(obj.__getattribute__("flight_name"))
obj.__setattr__("flight_name", "Vistara")

#obj.flight_name = 'AirIndia'
obj.flight_booking_date = "25 Dec 2024"

obj.show_flight_name()
obj.show_flight_booking_date()
