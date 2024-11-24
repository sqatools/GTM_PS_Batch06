"""
Polymorphism : When any specific method or operator perform different operation then it is know
is polymorphism.

1. Method Overriding : When we define same name method in parent class and child class, then child
                      class method override the parent class method, then it is known as method
                      overriding.
2. Method Overloading : When we defined two methods with same name and different parameter
                        in one class, then it is known as method overloading.
                        But Python Does not support method overloading, if we define two methods
                        with same name, it will only consider latest defined method.
3. Operator Overloading
"""


class Animal:
    def __init__(self, animal_name, animal_age, voice):
        self.animal_name = animal_name
        self.animal_age = animal_age
        self.voice = voice

    def show_animal_name(self):
        print(f"Animal name is : {self.animal_name}")

    def show_animal_Age(self):
        print(f"The animal age is : {self.animal_age}")

    def animal_voice(self):
        print("Animal voice from animal class :", self.voice)

class Tiger(Animal):
    def __init__(self, animal_name, animal_age, voice, tiger_breed):
        super().__init__(animal_name, animal_age, voice)

        self.tiger_breed = tiger_breed

    def show_tiger_breed(self):
        print("Tiger breed is :", self.tiger_breed)

    def animal_voice(self):
        print("The voice of Tiger is Roar")

    def addition(self, n1, n2):
        print("addition of 2 values :", n1+n2)

    def addition(self, n1, n2, n3):
        print("Addition of 3 values :", n1+n2+n3)


obj = Tiger("Tiger", 10, "Roar", "Bangal Tiger")
#obj.animal_voice()

# obj.addition(10, 20)
# TypeError: Tiger.addition() missing 1 required positional argument: 'n3'

obj.addition(10, 20, 30)
# Addition of 3 values : 60



# Operator overloading

# + Operator overloading
n1 = 20
n2 = 30
print("addition :", n1+n2)
print("addition :", n1.__add__(n2))
print(dir(int))  # ['__abs__', '__add__', '__and__

s1 = 'Hello'
s2 = 'Good Morning'
print("greeting :", s1 + s2)
print("greeting :", s1.__add__(s2))
print(dir(str)) # ['__add__', '__class__', '__contains__',


print("_"*50)
l1 = [4, 6, 7]
l2 = [30, 20, 10]
print("list concatenation :", l1+l2)
print("list concatenation :", l1.__add__(l2))
print(dir(list))  # ['__add__', '__class__', '__class_getitem__'



print("_"*50)
# * operator overloading
a1 = 50
a2 = 5
print("multiply values :", a1*a2)
print("multiply values :", a1.__mul__(a2))
# multiply values : 250

s1 = "Hello"
b1 = 5
print("repeat string :", s1*b1)
print("repeat string :", s1.__mul__(b1))
# HelloHelloHelloHelloHello

list1 = [4, 6, 7]
num = 5
print("repeat list values :", list1*num)
print("repeat list values :", list1.__mul__(num))
# [4, 6, 7, 4, 6, 7, 4, 6, 7, 4, 6, 7, 4, 6, 7]
