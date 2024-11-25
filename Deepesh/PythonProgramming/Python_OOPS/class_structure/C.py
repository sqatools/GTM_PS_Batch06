from B import flight


class Train(flight):
    def __init__(self, train_name='Vande Bharat', train_booking_date=None):
        super().__init__()
        self.train_name = train_name
        self.train_booking_date = train_booking_date

    def show_train_name(self):
        print(f"Train name is: {self.train_name}")

    def show_train_booking_date(self):
        print(f"Train booking date is: {self.train_booking_date}")
