
print("====Method overriding single Level Inheritance ======")

class Demo1:
    def method1(self):
        print("Method 1")

class Demo2(Demo1):
    def Method1(self):
        print("Method1 from Demo2")

D2=Demo2()
D2.Method1()

print("====Method overriding single Level Inheritance(WithParam)======")

class Sample1:
    def m1(self,num1,num2):
        print("Addition=",num1+num2)

class Sample2(Sample1):
    def m1(self,num1,num2):
        print("Multiplication=",num1*num2)

S2=Sample2()
S2.m1(20,20)












