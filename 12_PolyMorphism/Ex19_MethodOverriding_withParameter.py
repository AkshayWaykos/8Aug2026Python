print("=======Method overriding with Parameter =========")
class Demo1:
    def method1(self,num1,num2):
        print("Addition = ",num1+num2)

class Demo2(Demo1):
    def method1(self,num1,num2):
        print("Multiplication =",num1+num2)

class Demo3(Demo2):
    def method1(self,num1,num2):
        print("Division = ",num1 / num2)

d3=Demo3()
d3.method1(50,10)
print("====================================================")

class Father:
    def car(self):
        print("Father car THAR",)
class son1(Father):
    def car(self):
        print("son1 car KIYA")
        super().car()
class son2(Father):
    def car(self):
        print("son2 car SUMO")
        super().car()

s1=son1()
s1.car()
s2=son2()
s2.car()

print("====================================================")
