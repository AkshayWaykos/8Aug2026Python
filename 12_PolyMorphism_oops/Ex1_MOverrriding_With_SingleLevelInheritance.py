print("===Method Overriding with Single Level Inheritance=====")

class Father:
    def car(self):
        print("Car =Nano")
    def home(self):
        print("Home =1 BHK")
    def money(self):
        print("Money = 2L")
class son(Father):
    def car(self):             #Method Override
        print("Car =BMW")
    def home(self):            #Method Override
        print("Home =3 BHK")
    def money(self):           #Method Override
        print("Money = 5L")
s=son()
s.car()
s.home()
s.money()

print("===Method Overriding with Single Level Inheritance(static)=====")

class Father1:
    @staticmethod
    def car():
        print("Car=Nano")
    @staticmethod
    def money():
        pritn("Money=3L")
class son1(Father1):
    @staticmethod
    def car():
        print("Car = BMW")
    @staticmethod
    def money():
        print("money=2L")
s1=son1()
s1.car()
s1.money()
