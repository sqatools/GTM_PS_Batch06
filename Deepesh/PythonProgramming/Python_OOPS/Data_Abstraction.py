"""
Data Abstraction : Provide only overview details of the product or application and hide the internal
                   structure and code logics from end user, then it is known as abstraction.

When we defined method in one and class and implement the method on another class, then it is known
as abstract method and class is known as abstract class.

"""
from abc import abstractmethod

class Animal:

    @abstractmethod
    def animal_name(self):
        pass

    @abstractmethod
    def animal_voice(self):
        pass

    @abstractmethod
    def animal_breed(self):
        pass


class Dog(Animal):

    def animal_name(self):
        print("Animal name is Dog")

    def animal_voice(self):
        print("Barking")

    def animal_breed(self):
        print("German")



obj = Dog()
obj.animal_breed()


str1= "Hello"
str1.upper()
