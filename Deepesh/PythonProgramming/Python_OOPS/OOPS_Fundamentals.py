"""
class : class in the blueprint of an object where de defined all the properties and attribute
        and method of the object.
object : Object is an enitity through which we can access all the method/variable/attribute of
         the class.
method :  When we write a function inside the class, then it become method.
         1. Instance method : When we define any method with self as first parameter, then it
                              is known as instance method.
         2. Class Method : Class method, that only deals with class variable
         3. Static Method

variable :
         1. Instance variable : Any variable we defined with self, then it is instance variable
         2. class variable : Any variable we define at class, then it is known class variable

constructor : Constructor which initialize the memory for the object.
            1. Default constructor   def __init__()
               Whenever we create the object of the class, then default constructor will be initialized.
               class xyz:
                  def __init__():
                    print("Welcome")

               obj = xyz()


            2. Parametrize constructor  def __init__(num1, num2)

self :  Self is the object of the current class, when we call any instance through the object, then
        internally object is first parameter of each instance method.

Inheritance
Polymorphism
Abstraction
Data Hiding
"""


class ABC:
    CITY = 'Pune' # class variable
    Country = 'India'

    def __init__(self, num1, num2):
        print("Welcome to ABC class")
        self.x = num1  # instance/object variable
        self.y = num2  # instance/object variable

    # instance/object method
    def greeting(self):
        print("Good Morning")
        self.z = 500

    def table_of_number(self, num):
        for i in range(1, 11):
            print(i, "*", num, ":", i*num)

    def addition_values(self):
        print("Addition :", self.x + self.y)


    def country_name(self):
        print("country name :", self.Country)

    def city_name(self):
        print("City Name :", self.CITY)

    def largest_variable_value(self):
        print("Largest value :", self.z)

    @classmethod
    def address_details(cls):
        print("city name :", cls.CITY)
        print("Country name :", cls.Country)


if __name__ == '__main__':
    obj = ABC(30, 40)
    print(id(obj))
    obj.greeting()
    obj.table_of_number(5)
    obj.addition_values()
    #obj.country_name()
    #obj.city_name()
    obj.largest_variable_value()
    obj.address_details()
"""
    print("_"*50)
    obj1 = ABC(50, 60)
    obj1.greeting()
    print(id(obj1))

    print("_"*50)
    obj2 = ABC(70, 80)
    obj2.greeting()
    print(obj.__module__)
    print(__name__)
    print(id(obj2))
"""

#1  Write a class structure for Car and we have to provide following details
"""
-> car name
-> car price
-> car company
-> car model
-> car mileage
-> Car Country: class variable
"""
