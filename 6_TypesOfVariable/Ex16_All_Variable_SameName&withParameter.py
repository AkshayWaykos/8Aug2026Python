print("=====G-C-L Variable==========")

student="Akshay"                  #Global VAriable
class Demo1:
    student="Sagar"

    def info(self):
        student="Shiva"
        print("Local Variable =",student)
        print("class variable=",self.student)
        print("Global Variable",globals()['student'])

d1=Demo1()
d1.info()

print("=====Global Variable==========")
s=20
def fun():
    print("Global=",s)
def fun2():
    print("Global=",s)
fun()
fun2()
print("=====Local Variable==========")
def add():
    num1=30
    print("local=",num1)
add()
print("=====class Variable==========")

class Demo2:
    num2=40
    num3=40
    def add(self):
        print("Addition=",self.num2+self.num3)
d2=Demo2()
d2.add()

print("============================")



















