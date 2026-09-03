print("=====Ex8-User Define Constructor With Parameter=========")

class Sample:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def add(self):
        print("Addition=",self.num1 + self.num2)
    def mul(self):
        print("Multiplication=",self.num1 * self.num2)
    def sub(self):
        print("Substraction=",self.num1 - self.num2)
    def div(self):
        print("Subtraction=",self.num1 / self.num2)

s1=Sample(20,10)
s1.add()
s1.mul()
s1.div()
s1.sub()
print("---------------------")
s2=Sample(30,10)
s2.add()
s2.mul()
s2.div()
s2.sub()
print("---------------------")
















