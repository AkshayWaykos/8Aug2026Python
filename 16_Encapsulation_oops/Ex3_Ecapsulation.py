print("==========Encapsulation=====================")
class Demo3:
    def setdata(self):
        self.__name="Akshay"
        self.__age=31

        self.__a = 10
        self.__b = 20

    def student1(self):
        print("Student Name=",self.__name)
        print("Age od Stu1=",self.__age)

    def student2(self):
        print("Student Name=", self.__name)
        print("Age od Stu1=", self.__age)

    def add(self):
        print("Addition=",self.__a+self.__b)

    def mul(self):
        print("Multiplication=",self.__a*self.__b)

d3=Demo3()
d3.setdata()

d3.student1()
print("==============")
d3.student2()
print("==============")
d3.add()
print("==============")
d3.mul()
