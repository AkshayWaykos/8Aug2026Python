
def fun2():
    print("Function 2 executed form module 3")

A=20
class Vari:
    A=30
    def fun3(self):
        A=40
        print("Local Variable=",A)
        print("Global Variable=",globals()['A'])
        print("Class Variable =",self.A)

    def method3(self):
        print("Method 3 executed from module 3")


