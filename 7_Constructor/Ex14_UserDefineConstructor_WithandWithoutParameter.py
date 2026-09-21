print("========User Define Constructor Without Parameter========")

class Student:
    def __init__(self):
        self.name="Akshay"
        self.age=31
        self.roll=101

    def studentInfo(self):
        print("Student Name =",self.name)
        print("Student Age = ",self.age)
        print("Student Roll =",self.roll)

s1=Student()
s1.studentInfo()
print("========User Define Constructor With Parameter========")

class Student11:
    def __init__(self,name,age,roll):
        self.name=name
        self.age=age
        self.roll=roll

    def studentIndo11(self):
        print("Student Name =",self.name)
        print("Student Age = ",self.age)
        print("Student Roll=",self.roll)

s11=Student11("Akshay",31,101)
s11.studentIndo11()
