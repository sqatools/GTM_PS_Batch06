"""
Data Hiding : To hide data of class from outside access. to achieve data hiding we have to declare
              variables and methods in specific pattern

1. When we define any variable/method name with single underscore '_' and
    double underscore '__' as prefix, then those data will not available in suggest list.

2.

"""

class Car:
    def __init__(self, car_name, car_price, car_comp):
        self.car_name = car_name
        self._car_price = car_price
        self.__car_comp = car_comp


    def show_car_name(self):
        print("Car name is :", self.car_name)

    def _show_car_price(self):
        print("Car price is :", self._car_price)

    def __show_car_company(self):
        print("Car company name is :", self.__car_comp)

    def show_car_details(self):
        self.show_car_name()
        self._show_car_price()
        self.__show_car_company()


obj = Car('XUV700', '30 Lac', 'Mahindra')
# method/variable with single underscore, we can access directly without any issue
obj._show_car_price()
print(obj._car_price)

# method/variable with double underscore, we can access through the class name
# obj._<class>__<method/variable>
obj._Car__show_car_company()
print(obj._Car__car_comp)

#obj.show_car_details()
