print("====Multilevel Inheritance Static Method(without Param)=====")

class student1:
    @staticmethod
    def m1():
        print("Static m1 method from student1 class")

class student2(student1):
    @staticmethod
    def m2():
        print("Static m2 method from student2 class")

class student3(student2):
    @staticmethod
    def m3():
        print("Static m3 method from student3 class")

student3.m1()
student3.m2()
student3.m3()

print("====Multilevel Inheritance Static Method(With Param)=====")

class Emp1:
    @staticmethod
    def info1(name,id):
        print("Emp Details= ",name,id)
class Emp2(Emp1):
    @staticmethod
    def info2(salary,exp):
        print("Emp2 Details=",salary,exp)
class Emp3(Emp2):
    @staticmethod
    def info3(company,years):
        print("Emp3 Details=",company,years)

Emp3.info1("Akshay",101)
Emp3.info2(50000,8)
Emp3.info3("TATA",2022)


