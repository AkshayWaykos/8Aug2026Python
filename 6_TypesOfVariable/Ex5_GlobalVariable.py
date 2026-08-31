print("======Ex 3 Global Variable(non static) ==========")

num1=20
num2=10
def function1():
    print("Global variable print in function1 =",num1)
def function2():
    print("Global variable print in function1 =",num2)
function1()
function2()

print("--------------------")

class SampleX():
    def XX(self):
        print("Global Variable print in XX method =",num1,num2)

    @staticmethod
    def YY():
        print("Global Variable print in YY Method =",num1,num2)
S1=SampleX()
S1.XX()

SampleX.YY()
