"""
Inheritance
Polymorphism
Abstraction
Data Hiding
"""
# Inheritance
"""
1. Single Inheritance
2. Multiple Inheritance
3. Multi level inheritance()
"""
# 1. Single Inheritance
"""
class Father:
    def __init__(self, fname, faddress):
        print("Welcome to first section")
        self.fname = fname
        self.faddress  = faddress

    def show_father_nane(self):
        print(f"The father name : {self.fname}")

    def show_father_address(self):
        print(f"The father address : {self.faddress}")

class Son(Father):
    def __init__(self, sname, fname, faddress):
        super().__init__(fname, faddress)
        self.son_name = sname

    def show_son_name(self):
        print("Son name :", self.son_name)


obj = Son('Mohit', 'Rahul', 'Construction in Pune')
obj.show_father_address()
obj.show_son_name()
"""

"""
# 2. multi level inheritance
class grandFather:
    def __init__(self, gf_name, gf_property):
        self.gf_name = gf_name
        self.gfproperties = gf_property

class Father(grandFather):
    def __init__(self, fname, faddress, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        print("Welcome to first section")
        self.fname = fname
        self.faddress  = faddress

    def show_father_nane(self):
        print(f"The father name : {self.fname}")

    def show_father_address(self):
        print(f"The father address : {self.faddress}")


class Son(Father):
    def __init__(self, sname, fname, faddress, gf_name, gf_property):

        super().__init__(fname, faddress, gf_name, gf_property)
        self.son_name = sname

    def show_son_name(self):
        print("Son name :", self.son_name)

    def show_family_details(self):
        print("grand father name :", self.gf_name)
        self.show_son_name()
        self.show_father_nane()
        self.show_father_address()


obj = Son('Sonu', 'Mohan', 'construction', 'Dayaram', '200Acr')
obj.show_family_details()

"""

############################ multiple inheritance #######################

class Father:
    def __init__(self, fname, f_business, f_car):
        self.fname = fname
        self.business = f_business
        self.car = f_car

    def show_father_details(self):
        print("Father name :", self.fname)
        print("Father Business :", self.business)
        print(f"Father car : {self.car}")


class Mother:
    def __init__(self, m_name , m_business):
        self.mother_name = m_name
        self.business = m_business


    def show_mother_details(self):
        print(f"Mother name : {self.mother_name}")
        print(f"Mother Business : {self.business}")


#M R O (Method Resolution Order)
class Son(Father, Mother):
    def __init__(self, son_name, fname, f_business, f_car, m_name, m_business):
        super().__init__(fname, f_business, f_car)
        self.son_name = son_name
        self.mom = Mother(m_name, m_business)


    def show_family_details(self):
        self.show_father_details()
        self.mom.show_mother_details()
        print("Son Name :", self.son_name)



obj = Son('Rahul', 'MOhan', 'Transport', 'BMW', 'Pooja', 'Fashion')

obj.show_family_details()
