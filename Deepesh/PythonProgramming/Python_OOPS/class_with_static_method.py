
"""
No need to create object of the class to access the static method, static methods are associated
with class name.
static method has to be defined with decorator as @staticmethod
"""
class Math:
    default_value = 100  # class variable

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        print("Addition of value :", self.num1 + self.num2)

    @staticmethod
    def factorials(n):
        fact = 1
        for i in range(n, 0, -1):
            fact = fact * i

        print("Factorial :", fact)

    # def multiplication(num_value):
    #     print(num_value**2)


    @classmethod
    def divide(abc):
        print("division of class variable :", abc.default_value//10)


obj = Math(50, 60)

# access static method with class name
# Math.factorials(5)

# access instance method class name, provide object as parameter.
# Math.addition(obj)

# Access static method with object
#obj.factorials(6)


# obj.multiplication()
# TypeError: unsupported operand type(s) for ** or pow(): 'Math' and 'int'


# Access the class method with class object
obj.divide()


Math.divide()
