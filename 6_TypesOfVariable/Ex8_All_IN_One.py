print("============================")

num1=10                                         #Global Variable
def fun1():
    num2=20                                     #Local Variable
    print("Global variable value =",num1)
    print("Local variable value =",num2)

fun1()

class allInOne():
    num3=30                                   #class Variable
    def fun2(self):
        print("Class Variable =",self.num3)

    def all(self):
        num4=40
        print("Global",num1)        #global v
        print("Local",num4)        #local v
        print("Class",self.num3)   #class v

a1=allInOne()
a1.fun2()
a1.all()