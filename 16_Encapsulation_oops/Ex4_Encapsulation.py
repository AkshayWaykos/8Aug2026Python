
print("=======Encapsulation=without parameter=============")

class Demo1:
    def setdata(self):
        self.__name="Akshay"
        self.__age="Waykos"

    def Emp1Info1(self):
        print("Emp Name =",self.__name)
        print("Emp Age  =",self.__age)

    def Emp1Info2(self):
        print("Emp Name =",self.__name)
        print("Emp Age  =",self.__age)

d1=Demo1()
d1.setdata()
d1.Emp1Info1()
print("---------")
d1.Emp1Info2()

print("=======Encapsulation=with parameter=============")

class Demo2:

    def setvalue(self,num1,num2):
        self.__num1=num1
        self.__num2=num2

    def add(self):
        print("Addition=",self.__num1 + self.__num2)

    def mul(self):
        print("Multiplication=", self.__num1 * self.__num2)

d2=Demo2()
d2.setvalue(20,20)
d2.add()
d2.mul()



























