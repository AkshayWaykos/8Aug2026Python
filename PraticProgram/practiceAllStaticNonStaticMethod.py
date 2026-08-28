#class & Object
#static method(with and without Parameter)
print("==Non static method(with and without Parameter==")
class Demo():
    def Method1(self):
        print("Method 1 has been Executed")

    def Mathod2(self,num1,num2):
        print("Addition of no = ",num1+num2)

D1=Demo()
D1.Method1()
D1.Mathod2(20,20)

#static method(with and without Parameter)
print("==Non static method(with Parameter==")

class Demo2():
    def method4(self,name,age):
        print("Name=",name ,"||", "Age =" ,age)

    def method5(self,num1):
        print("Square of no = ",num1*num1)

D2=Demo2()
D2.method4("Akshay",31)
D2.method5(2)

print("==Non static method(without Parameter==")

class Demo3():
    def Sample1(self):
        print("Sample1 Method run from Demo 3 class")

    def Sample2(self):
        print("Sample2 Method run from Demo 3 Class")
D3=Demo3()
D3.Sample1()
D3.Sample2()

print("==Static method(without Parameter==")

class Demo4():
    @staticmethod
    def MethodA():
        print("Static MethodA Executed")
    @staticmethod
    def MethodB():
        print("Static MethodB")

Demo4.MethodA()
Demo4.MethodB()

print("==Static method(with Parameter==")
class Demo5():
    @staticmethod
    def MethodX(num1):
        print("Square of no =",num1)

    @staticmethod
    def MethodY(num2,num3):
        total=num2+num3
        print(" Addition of no = ",total)
Demo5.MethodX(5)
Demo5.MethodY(10,20)

print("==Static method(with Parameter==")

class Demo6():
    @staticmethod
    def MethodP(name,age):
        print(name,age)
        print("MethodP in Static")

    @staticmethod
    def MethodQ(num1,num2):
        print(num1+num2)

Demo6.MethodP("Akshay",31)
Demo6.MethodQ(20,20)

print("===========================")































