
#module 5

def fun11():
    print("Function run from module 4")

def fun22(num1,num2):
    print("Addition = ",num1+num2)

class Demo11:
    def __init__(self,num3,num4):
        self.num3=num3
        self.num4=num4

    def mul(self):
        print("Multiplication=",self.num3*self.num4)

class Demo2(Demo11):
    @staticmethod
    def div(num5,num6):
        print("Division =",num5/num6)