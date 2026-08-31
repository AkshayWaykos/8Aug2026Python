print("========Same Variable name=========")

a,b=10,20                        #Global Variable

class Test3():
    a,b=20,30                    #Class Variable
    def fun2(self):
        a,b=40,50

        print("Local V =",a+b)
        print("Class V =",self.a + self.b)
        print("Global V=",globals()['a']+globals()['b'])

    @staticmethod
    def fun3():
        a,b=40,40

        print("Local V =",a+b)                #calling Local variable
        print("Class V =",Test3.a+Test3.b)    #calling class Variable
        print("Global V",globals()['a']+globals()['b']) #calling Global variable

t3=Test3()
t3.fun2()
print("--------")
Test3.fun3()


