print("====single level inh Variable(without Param)====")

class Demo1:
    i=10
    def m1(self):
        print("m1 method from Demo 1 class")
class Demo2(Demo1):
    j=20
    def m2(self):
        print("m2 method from Demo 2 class")
        print("Addition =",self.i+self.j)

d2=Demo2()
d2.m1()
d2.m2()

print("====single level inh Variable(with Param)====")

class student1:
    a=10
    def m11(self):
        print("m11 method from student1 class")

class student2(student1):
    b=30
    def m22(self):
        print("m22 method from student2 class")
        print("Addition =",self.a+self.b)
s2=student2()
s2.m11()
s2.m22()

print("==============================")

