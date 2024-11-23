
"""
class ABC:
    def __init__(self, num1, num2):
        print("Welcome to ABC class")
        self.x = num1
        self.y = num2

    def greeting(self):
        print("Good Morning")

    def table_of_number(self, num):
        for i in range(1, 11):
            print(i, "*", num, ":", i * num)

    def addition_values(self):
        print("Addition :", self.x + self.y)

obj = ABC(8, 9)
obj.greeting()            # Calls the greeting method
obj.table_of_number(4)    # Prints the multiplication table for 4
obj.addition_values()     # Prints the sum of num1 and num2 (8 + 9)
"""
"""
class Car:

    # Class variables
    COUNTRY = "India"  # Default country for all cars

    def __init__(self, name, price, company, model, mileage):
        print("Welcome to Car Class")
        # Instance variables
        self.name = name
        self.price = price
        self.company = company
        self.model = model
        self.mileage = mileage
"""
class Car:
    # Class variable
    country = "India"  # Default country for all cars

    def __init__(self, name, price, company, model, mileage):
        # Instance variables
        self.name = name
        self.price = price
        self.company = company
        self.model = model
        self.mileage = mileage

    # Method to display car details
    def display_details(self):
        print("Car Name:", self.name)
        print("Car Price:", self.price)
        print("Car Company:", self.company)
        print("Car Model:", self.model)
        print("Car Mileage:", self.mileage, "km/l")
        print("Car Country:", Car.country)


# Creating objects and displaying their details
car1 = Car("Corolla", 20000, "Toyota", "2023", 16)
car1.display_details()

print("-" * 30)

car2 = Car("Civic", 22000, "Honda", "2022", 18)
car2.display_details()



