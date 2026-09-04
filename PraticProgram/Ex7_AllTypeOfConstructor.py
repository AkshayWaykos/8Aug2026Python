print("=========Default define Constructor=================")
# def __init__(self):
# print("running default Constructor")

class Sample1:
    def m1(self):
        print("Running non static methods")
s1=Sample1()
s1.m1()
print("====User define Constructor without Parameter======")

class Sample2:
    def __init__(self):
        print("running user define Constructor")

    def add(self):
        s=10
        t=20
        print("addition=",s+t)
s2=Sample2()
s2.add()

print("====User define Constructor with Parameter======")

class Sample3:
    def __init__(self,a,b):
        self.name=a
        self.age=b

    def details(self):
        print("Student Name =",self.name)
        print("Studemt Age =",self.age)
s3=Sample3(20,20)
s3.details()
print("====User define Constructor with Parameter======")

class Sample4:
    def __init__(self,x,y):
        self.num1=x
        self.num2=y
    def calculation(self):
        print("Addition = ",self.num1)
        print("Multiplication = ",self.num2)

s4=Sample4(40,40)
s4.calculation()

print("====END======")

