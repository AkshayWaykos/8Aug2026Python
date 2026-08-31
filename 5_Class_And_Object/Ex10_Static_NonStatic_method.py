print("===Ex-10 Static and non static method(withoutParam) =======")

class Sample1():
    def method1(self):
        print("Non Static Method")

    @staticmethod
    def method2():
        print("Static method")

S1=Sample1()
S1.method1()

Sample1.method2()

print("===Ex-10 Static and non static method(withParam) =======")

class Sample2():
    def fun2(self,x,y):
        print("Addition =",x+y)

    @staticmethod
    def fun3(x,y):
        print("Multiplication=",x*y)

S2=Sample2()
S2.fun2(10,20)

Sample2.fun3(30,40)

