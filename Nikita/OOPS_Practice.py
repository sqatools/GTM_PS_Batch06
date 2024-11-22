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