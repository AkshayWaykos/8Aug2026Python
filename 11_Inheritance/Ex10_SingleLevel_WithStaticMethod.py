print("=====Single Level Inheritance with Static Method(withoutParam)======")

class Father:
    @staticmethod
    def money():
        print("Static Method from Super class")

class son(Father):
    @staticmethod
    def home():
        print("Static method from sub class")

son.money()
son.home()
print("=====Single Level Inheritance with Static Method(with Param)======")

class Teacher:
    @staticmethod
    def add(num1,num2):
        print("Addition =",num1+num2)

class student(Teacher):
    @staticmethod
    def mul(num1,num2):
        print("Multiplication=",num1*num2)

student.add(20,20)
student.mul(20,20)
print("===============================================================")