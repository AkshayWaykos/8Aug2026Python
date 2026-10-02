print("======Single Level Inheritance======")

class father:
    def money(self):
        print("Money from Father class")

class son(father):
    def car(self):
        print("car from son class")
s1=son()
s1.money()
s1.car()
print("======Single Level Inheritance(with Parameter======")
class Demo1:
    def __init__(self,name):
        self.name=name

    def info1(self):
        print("Person Name=",self.name)

class Demo2(Demo1):
    def info2(self):
        print("Demo2 class method from info2 method")
        print(self.name)

d2=Demo2("Akshay")
d2.info1()
d2.info2()

print("=========Single Inheritance(With Parameter============")

class Father:
    def proeprty(self,car,home):
        print("Father  Car=",car)
        print("Father Home=",home)
class son(Father):
    def ownpropertry(self,bike):
        print("Son Bike=",bike)
s=son()
s.proeprty("BMW","2BHK")
s.ownpropertry("KTM")

print("=========Single Inheritance============")







