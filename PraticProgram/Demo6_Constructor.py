print("====Constructor without parameter====")

class Demo1:
    def __init__(self):
        self.num1=20
        self.num2=30
        print("Executed the Uer define Constructor")

    def add(self):
        print("Addition =", self.num1 + self.num2)

d1=Demo1()
d1.add()
print("====Constructor with parameter====")

class Demo2:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def mul(self):
        print("Multiplication =",self.num1*self.num2)


D2=Demo2(20,20)
D2.mul()