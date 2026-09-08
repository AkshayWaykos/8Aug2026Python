print("========Single Level Inheritance==========")

class Student1:
    def m1(self):
        print("Method m1 executed from super class")

    def m2(self):
        print("Method m2 executed from super class")

class Student2(Student1):
    def m3(self):
        print("Method m3 executed from sub class")
    def m4(self):
        print("Method m1 executed from sub class")

s2=Student2()
s2.m1()
s2.m2()
s2.m3()
s2.m4()

