print("=========Example Local variable(non static)==============")

def AB():
    num1=10
    print("Local Variable print in AB Function =",num1)
def CD():
    num2=20
    print("Local Variable print in CD Function =",num2)
AB()
CD()

print("=========Example Local variable(Static)==============")

class Demo():
    def add(self):
        num1=10
        print("Addition =",num1+num1)
    def mul(self):
        num2=20
        print("Multiplication = ",num2*num2)
    def square(self,num7):
        print("Square = ",num7)

    @staticmethod
    def sub():
        num3=30
        num4=10
        print("Substraction =",num3-num4)

    @staticmethod
    def div(num5,num6):
        division=num5/num6
        print("Division =",division)

D1=Demo()
D1.Add()
D1.Mul()
D1.square(5)

Demo.sub()
Demo.div(20,5)

print("=========other==============")

x="amazon"
def other():
    x="superb"
    print("Python is", x ,"language")
other()