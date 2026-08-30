print("=======Ex3:Global Variable use in function & class============")

num1=20

def function1():
    print("Executed fun1 from non-static Method =",num1)

def function2():
    print("Executed fun2 from static Method =",num1)

function1()
function2()
print("-------------------------------")
class Sample22():
    def method1(self):
        print("Executed method1 from Sample class",num1)
    @staticmethod
    def method2():
        print("Executed Method2 from Sample class",num1)

S1=Sample22()
S1.method1()

Sample22.method2()

print("=======Ex4:Global Variable use in function & class============")

number=10

def fun1():
    print("Executed function1 and print global variable =",number)
    print("Square of global no=",number*number)

def fun2():
    print("Executed function2 and print global variable =",number)
    print("Addition of global no=", number + number)

fun1()
fun2()
print("==============")
class Math1():
    def addtion(self):
        print("Addition in class of global variable =",number+number)

    @staticmethod
    def multiplication():
        print("Multiplication in class of global variable =",number*number)

M1=Math1()
M1.addtion()

Math1.multiplication()

print("===================================================================")































