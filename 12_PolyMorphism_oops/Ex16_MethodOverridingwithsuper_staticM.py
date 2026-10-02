print("======Method Overriding with super()======")

class Demo1:
    def m1(self,num1,num2):
        print("Addition = ", num1 + num2)

class Demo2(Demo1):
    def m1(self,num1,num2):
        print("Multiplication =", num1 * num2)
        super().m1(10,10)

D1=Demo1()
D1.m1(30,10)

D2=Demo2()
D2.m1(20,20)

print("=======================================")

class Sample1:
    def method1(self):
        print("Method 1 from Sample 1 class ")
class Sample2(Sample1):
    def method1(self):
        print("method 1 from Sample 2 class")
        super().method1()
S2=Sample2()
S2.method1()

