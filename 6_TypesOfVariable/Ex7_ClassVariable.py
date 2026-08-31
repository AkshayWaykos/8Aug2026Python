print("==========Class Variable(without parameter)============")

class Demo():
    num1=10
    def fun1(self):
        print(self.num1)
    @staticmethod
    def func2():
        print(Demo.num1)
D1=Demo()
D1.fun1()
Demo.func2()
print("==========Class Variable(without parameter)============")

class Demo2():
    name="Akshay"
    def m1(self):
        print(self.name)

    @staticmethod
    def m2():
        print(Demo2.name)

d2=Demo2()
d2.m1()

Demo2.m2()
