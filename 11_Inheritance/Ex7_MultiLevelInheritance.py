print("======Multilevel Inheritance==========")

class Demo1:  #super class
    def m1(self):
        print("m1 method from Demo 2 class")

class Demo2(Demo1):
    def m2(self):
        print("m2 method from Demo 2 class")

class Demo3(Demo2):
    def m3(self):
        print("m3 method from Demo 3 class")

d2=Demo2()
d2.m1()
d2.m2()

d3=Demo3()
d3.m3()

print("======Multilevel Inheritance(with Param)==========")

class Student1:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("Student Name=",self.name,self.age)

class Student2(Student1):
    def add(self,num1,num2):
        print("Addition from student 2 class =",num1+num2)

class Student3(Student2):
    def mul(self,num3,num4):
        print("Multiplication from student 3 class =",num3*num4)

s2=Student2("Akshay",31)
s2.add(30,30)
s2.info()
print("----------")
s3=Student3(20,20)
s3.add(20,20)
s3.mul(20,20)




































