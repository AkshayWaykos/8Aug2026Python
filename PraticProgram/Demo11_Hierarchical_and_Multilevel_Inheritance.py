print("============Hierarchical===============")

class Father:
    def Home(self):
        print("Father Home")
    def Car(self):
        print("Father car")
class son1(Father):
    def bike(self):
        print("Son1 Bike")
    def mobile(self):
        print("Son1 Mobile")
class son2(Father):
    def laptop(self):
        print("son2 Laptop")
    def plant(self):
        print("son2 plant")

s1=son1()
s1.Home()
s1.Car()
s1.bike()
s1.mobile()
print("------------")
s2=son2()
s2.Home()
s2.Car()
s2.laptop()
s2.plant()

print("============MultiLevel===============")

class Father:
    def fa(self):
        print("Father class property")
class Mother:
    def mo(self):
        print("Mother class property")
class son(Father,Mother):
    def so(self):
        print("Son class Property")

s=son()
s.so()
s.fa()
s.mo()