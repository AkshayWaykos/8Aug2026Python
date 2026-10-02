print("=====Method Overriding(single level)======")
#same method name ,same parameter but in different class.
class Student1:
    def method1(self,name,roll):
        print("Student1 Details=",name,roll)

class Student2(Student1):
    def method1(self,name,roll):
        print("Student2 Details=",name,roll)

S2=Student2()
S2.method1("Akshay",31)

print("======Method Overriding(multi level)======")

class Demo1:
    def m1(self,name):
        print("m1 method from Demo1 class")
class Demo2(Demo1):
    def m1(self,name):
        print("m1 method from Demo2 class")
class Demo3(Demo2):
    def m1(self,name):
        print("m1 method from Demo3 class=",name)
D3=Demo3()
D3.m1("Akshay")

print("======Method Overriding(Hierarchical Inh)======")

class Father:
    def car(self,carname):
        print("Father Name =",carname)
class son1(Father):
    def car(self,carname):
        print("son1 car =",carname)
class son2(Father):
    def car(self,carname):
        print("son2 car =",carname)

s1=son1()
s1.car("BMW")

s2=son2()
s2.car("Lamborghini")

print("======Method Overriding(Multiple Inh)======")

class CEO:
    def companyasset1(self):
        print("CEO method for companyasset1 ")

class COO:
    def companyasset1(self):
        print("COO method for companyasset1")
class Employee(CEO,COO):
    def companyasset1(self):
        print("Employee method for companyasset1")
E=Employee()
E.companyasset1()

print("===========================================")
