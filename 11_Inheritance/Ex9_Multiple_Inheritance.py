print("====Multiple Inheritance===============")

class son1:
    def bike(self):
        print("Son1 Bike=KTM")
class son2:
    def car(self):
        print("son2 Car=BMW")
class Father(son1,son2):
    def home(self):
        print("3 BKH House")
f1=Father()
f1.bike()
f1.car()
f1.home()

print("====Multiple Inheritance(with Param)===============")

class Student1:
    def add(self,num1,num2):
        print("Student 1 Perform Addition =",num1 + num2)
class Student2():
    def __init__(self,num3,num4):
        self.num3=num4
        self.num4=num4
    def mul(self):
        print("Student 1 Perform Multiplication =",self.num3*self.num4)
class Teacher(Student1,Student2):
    def result(self):
        print("Teacher Method from Teacher Class")

t1=Teacher(20,20)
t1.add(30,30)
t1.mul()
t1.result()


