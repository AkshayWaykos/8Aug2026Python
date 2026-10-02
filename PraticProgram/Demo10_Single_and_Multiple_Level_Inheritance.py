class Father:
    def Home(self):
        print("Home from Father Property")
    def car(self):
        print("Car from Father property")

class son(Father):
    def bike(self):
        print("Bike from son Property")

s=son()
s.Home()
s.car()
s.bike()

print("=======Multilevel Inheritance=========")

class Grandfather:
    def car(self):
        print("Grandfather Lamborghini")
class Father1(Grandfather):
    def Homeee(self):
        print("Father Homeee")
class son1(Father1):
    def bike(self):
        print("Son Bike")

s1=son1()
s1.Homeee()
s1.car()
s1.bike()