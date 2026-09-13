#Single Level Inheritance
#MultiLevel Inheritance
#Hierarchical Inheritance
#Multiple Inheritance

print("===Single Inheritance===")

class Father:
    def car(self):
        print("Father car =Nano")
    def money(self):
        print("Father money =5L")
class son(Father):
    def bike(self):
        print("Son Bike = KTM")
s=son()
s.bike()
s.car()
s.money()
print("===Multilevel Inheritance===")

class Sample1:
    def m1(self):
        print("m1 from parent class")
class Sample2(Sample1):
    def m2(self):
        print("m2 from child/super class")
class Sample3(Sample2):
    def m3(self):
        print("m3 from child class")

S3=Sample3()
S3.m1()
S3.m2()
S3.m3()
print("===Hierarchical Inheritance===")

class Father:
    def money(self):
        print("Father money")
class son1(Father):
    def bike(self):
        print("Son1 bike")
class son2(Father):
    def laptop(self):
        print("son2 laptop")
s1=son1()
s1.money()      #father property
s1.bike()       #Son1 property
print("----")
s2=son2()
s2.money()        #father property
s2.laptop()       #Son2 property

print("===Multiple Inheritance===")

class BigBrother:
    def car(self):
        print("BigBrother Car =BMW")

class secondBrother:
    def bike(self):
        print("SecondBrother Bike")
class ThirdBrother(BigBrother,secondBrother):
    def laptop(self):
        print("Third brother Laptop")

t=ThirdBrother()
t.car()
t.bike()
t.laptop()
print("==================Complete All Inheritance=====================")