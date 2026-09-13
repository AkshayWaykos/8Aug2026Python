
#module 1

def fun1():
    print("Non static function from module 1")

def fun2(num1,num2):
    print("non static function-Addition=",num1+num2)


class Demo1():
    def method1(self):
        print("method 1 from Demo1 class")

    @staticmethod
    def method2(num3,num4):
        print("static method -mul =",num3*num4)


