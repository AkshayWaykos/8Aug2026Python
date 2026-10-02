print("=====Non-Static/Static Method without Parameter====")

class Demo1:
    def m1(self):
        print("Non Static Method1 without Parameter")
    def m2(self):
        print("Non Static Method1 without Parameter")

    @staticmethod
    def m3():
        print("Static Method3 call from static method")
    @staticmethod
    def m4():
        print("Static Method4 call from static method")

d1=Demo1()
d1.m1()
d1.m2()
print("-----------")
Demo1.m3()
Demo1.m4()

print("=====Non-Static/Static Method with Parameter====")

class Demo2:
    def me1(self,num1,num2):
        print("Addition =",num1+num2)

    def me2(self,num1,num2):
        print("Multiplication=",num1*num2)

    #staticmethod
    @staticmethod
    def me3(num1,num2):
        print("Subtraction=",num1-num2)

    @staticmethod
    def me4(num1,num2):
        print("Division=",num1/num2)

d2=Demo2()
d2.me1(10,10)
d2.me2(20,20)
print("-----------------")
Demo2.me3(30,20)
Demo2.me4(50,5)

print("=======================================r====")


























