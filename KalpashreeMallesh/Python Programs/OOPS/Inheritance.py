# 1. Single Inheritance

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
    def __init__(self, sname, fname,faddress):
        super().__init__(fname, faddress)
        self.son_name = sname

    def show_son_name(self):
        print("Son name :", self.son_name)


obj = Son('Mohit','Rahul', 'Construction in Pune')
obj.show_father_address()
obj.show_son_name()