print("=======Hierarchical Inheritance=========")
#One Super class and Multiple Sub class
class Demo1:
    def m1(self):
        print("Method m1 from super class from Demo1")
    def m2(self):
        print("Method m2 from super class from Demo2")

class Demo2(Demo1):
    def m3(self):
        print("Method m3 executed from sub class")
    def m4(self):
        print("Method m4 executed from sub class")

class Demo3(Demo1):
    def m5(self):
        print("Method m5 executed from sub class ")
    def m6(self):
        print("Method m6 executed from sub class")

d2=Demo2()
d2.m1()
d2.m2()
d2.m3()
d2.m4()

d3=Demo3()
d2.m1()
d2.m2()
d2.m3()
d2.m4()
d3.m5()
d3.m6()

