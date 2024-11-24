print('_'*50)
# 1. Single Inheritance
class Father:
    def __init__(self, fname, faddress):
        print("Welcome to first section")
        self.fname = fname
        self.faddress = faddress

    def show_father_name(self):
        print(f"The father name : {self.fname}")

    def show_father_address(self):
        print(f"The father address : {self.faddress}")

class Son(Father):
    def __init__(self, sname, fname, faddress):
        super().__init__(fname, faddress)
        self.son_name = sname

    def show_son_name(self):
        print("Son name :", self.son_name)

obj = Son('Mohit', 'Sharma', 'Construction in Pune')
obj.show_father_address()
obj.show_son_name()

print('_'*50)
# 2. Multilevel Inheritance
class grandFather:
    def __init__(self, gf_name, gf_property):
        self.gf_name = gf_name
        self.gf_property = gf_property
class Father(grandFather):
    def __init__(self, fname, faddress, gf_name, gf_property):
        super().__init__(gf_name, gf_property)
        print("Welcome to first section")
        self.fname = fname
        self.faddress = faddress

    def show_father_name(self):
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
        print(f"grand father name: {self.gf_name}")
        self.show_son_name()
        self.show_father_name()
        self.show_father_address()

obj = Son('Sonu', 'Mohan', 'Construction', 'Dayaram', 'Kolkata')
obj.show_family_details()

print('_'*50)
# 3. Multiple Inheritance
class Father:
    def __init__(self, fname, fbusiness, fcar):
        self.f_name = fname
        self.f_business = fbusiness
        self.f_car = fcar

    def show_father_details(self):
        print("Father name :", self.f_name)
        print("Father Business :", self.f_business)
        print(f"Father car : {self.f_car}")

class Mother:
    def __init__(self, mname, mbusiness):
        self.m_name = mname
        self.m_business = mbusiness

    def show_mother_details(self):
        print("Mother name: ", self.m_name)
        print(f"Mother business : {self.m_business}")

# M R O = Method Resolution Order
class Son(Father, Mother):
    def __init__(self, sname, fname, fbusiness, fcar, mname, mbusiness):
        super().__init__(fname, fbusiness, fcar)
        self.son_name = sname
        self.mom = Mother(mname, mbusiness)

    def show_family_details(self):
        self.show_father_details()
        self.mom.show_mother_details()
        print("Son Name :", self.son_name)

obj = Son('Rahul', 'Mohan', 'Transport', 'BMW', 'Pooja', 'Fashion business')
obj.show_family_details()