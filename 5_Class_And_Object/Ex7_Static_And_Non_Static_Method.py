print("================================")

class Employee():
    @staticmethod
    def method1():
        print(" Static Method 1 ")

    @staticmethod
    def method2():
        print(" Static Method 2")

    def method3(self):
        print("Non-Static Method 3 ")

    def method4(self):
        print("Non-Static Method 4")

#call static method
#classname.method
Employee.method1()
Employee.method2()
print("=======")
#call non-static method
#object.method
E1=Employee()
E1.method3()
E1.method4()
