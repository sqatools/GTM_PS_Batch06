from A import Hotel


class flight(Hotel):
    def __init__(self, flight_name='Indigo', f_booking_date=None):
        super().__init__()
        self.flight_name = flight_name
        self.flight_booking_date = f_booking_date

    def show_flight_name(self):
        print(f"Flight name is: {self.flight_name}")

    def show_flight_booking_date(self):
        print(f"FLight booking date: {self.flight_booking_date}")


