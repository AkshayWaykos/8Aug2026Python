print("========Ex1: Class Variable ============")

class Company():
    num=10
    def method1(self):
        print(self.num)

    @staticmethod
    def method2():
        print(Company.num)

C1=Company()
C1.method1()

Company.method2()

print("========Ex2: Class Variable ============")

class Company2():
    num1=20

    def method1(self):
        print(self.num1)

    @staticmethod
    def method2():
        print(Company2.num1)

C2=Company2()
C2.method1()

Company2.method2()
print("========Ex3: Class Variable ============")

class Company3():
    value=20
    def m1(self):
        print("Addition of class Variable =",self.value + self.value)

    @staticmethod
    def m2():
        print("Multiplication of class variable",Company3.value*Company3.value)
C3=Company3()
C3.m1()

Company3.m2()



























