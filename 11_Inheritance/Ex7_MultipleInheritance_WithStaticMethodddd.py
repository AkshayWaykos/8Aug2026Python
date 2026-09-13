print("===Multiple Inheritance With Static Method=======")

class School1:
    @staticmethod
    def student1(num1,num2):
        print("Addition=",num1+num2)

    @staticmethod
    def student2(num1,num2):
        print("multiplelevel=",num1*num2)

class School2:
    @staticmethod
    def student3(num1,num2):
        print("multiplication=",num1*num2)

class Demo(School1,School2):
    @staticmethod
    def student4(name,age):
        print("Student Name & age =",name,age)
        print("Student method from Demo class")

Demo.student1(10,20)
Demo.student2(30,30)
Demo.student3(30,30)
Demo.student4("Akshay",30)