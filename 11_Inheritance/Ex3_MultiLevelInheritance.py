print("=============Multi Level Inheritance======================")

# 1 class -->2 class(acquired class1)-->3 class (acquired class2) -->class 3 object


class Demo1:
    def m1(self):
        print("m1 method executed from super class")
    def m2(self):
        print("m2 method executed from super class")
class Demo2(Demo1):
    def m3(self):
        print("m3 method executed from sub/super class")
    def m4(self):
        print("m4 method executed from sub/super class")
class Demo3(Demo2):
    def m5(self):
        print("m5 method executed from sub class")
    def m6(self):
        print("m6 method executed from sub class")

d3=Demo3()
d3.m1()
d3.m2()
d3.m3()
d3.m4()
d3.m5()
d3.m6()


