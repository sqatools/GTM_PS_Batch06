class Hotel:
    def __init__(self, hotel_name='Hayat', booking_date=None):
        self.hotel_name = hotel_name
        self.booking_date = booking_date

    def show_hotel_name(self):
        print("Hotel name :", self.hotel_name)

    def show_hotel_booking_date(self):
        print(f"The hotel booking date is: {self.booking_date}")
