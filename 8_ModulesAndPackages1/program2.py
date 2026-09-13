#module 2

def function1():
    print("function with out param from module 2")

def function2(num5,num6):
    print("function with param from modul2(multi=) ",num5*num6)

class Demo2:
    def method3(self):
        print("method3 from module 2 without parameter")

    @staticmethod
    def method4(num7,num8):
        print("Method4 from module 2 with parameter(add) =",num7+num8)


