print("=======Ex 1: Global Variable===========")

num=10

def fun1():
    print("Global Variable used in function1 = ",num)

@staticmethod
def fun2():
    print("Global Variable used in static func 2=" ,num)

fun1()
fun2()
print("-----------------------------------")
class Test1():
    def fun3(self):
        print("Global Variable used in class",num)

    @staticmethod
    def fun4():
        print("Global variable used in class =",num)

T1=Test1()
T1.fun3()
Test1.fun4()

