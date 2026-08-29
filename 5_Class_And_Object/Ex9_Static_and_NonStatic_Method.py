from Functionsprogram.Exp1_Function_WithoutParameter import multiplication

print("=======Non Static and static Method=======")

class Demo():
    def Method11(self):
        print( "Method 11" )
    @staticmethod
    def Method22():
        print( "Method 22" )
D1=Demo()
D1.Method11()
Demo.Method22()
print("=======Static & NonStatic Method========")

class Demo1():
    def Method3(self):
        print( "Method 3" )

    @staticmethod
    def Method4():
        print( "Method 4" )
D2=Demo1()
D2.Method3()

Demo1.Method4()
print("========Non Static Method=========")

class Arithmatic():
    @staticmethod
    def Addition(num1,num2):
        num3=num1+num2
        print("Addition =",num3)

    @staticmethod
    def Multiple(num1,num2):
        num3=num1*num2
        print("Method 6 =",num3)
Arithmatic.Addition(20,20)
Arithmatic.Multiple(20,20)
print("========Non-Static/static Method=========")

class Math():
    @staticmethod
    def addition(num1,num2):
        additon=num1+num2
        print("Addition =",additon)
    @staticmethod
    def multiplication(num1,num2):
        mul=num1*num2
        print("Multiplication =",mul)
Math.multiplication(10,20)
Math.multiplication(20,20)

print("=======Static Method=========")

class Operation():
    @staticmethod
    def ope1():
        print("operation 1")
    @staticmethod
    def open2():
        print("operation 2")

Operation.ope1()
Operation.open2()
print("=============================")




