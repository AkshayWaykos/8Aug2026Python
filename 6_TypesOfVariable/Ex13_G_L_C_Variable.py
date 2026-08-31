print("==Ex All Variable with Diff Name and With parameter============")

num1=10
def fun1():
    num2=20
    print("Global Variable =", num1)
    print("Local Variable =",num2)

def fun2(num3):
    print("Local Variable =",num3)

fun1()
fun2(30)

class Sample2():
    num4=40
    def func3(self,num5):
        print("Local Variable =",num5)
        print("Class Variable =",self.num4)     #for non static = self.variable
        print("Global Variable=",num1)
    @staticmethod
    def fun4(num6):
        print("Local Variable=",num6)
        print("Class Variable=",Sample2.num4)   #for static = classname.variable
        print("Class Variable=",num1)

S1=Sample2()
S1.func3(50)
print("---------------")

Sample2.fun4(60)