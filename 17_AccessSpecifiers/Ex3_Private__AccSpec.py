
class Student:
    __mark=90

    def info(self):
        print("Student Marks=",self.__mark)

s=Student()
s.info()

print("====================================")

class Student1:
    __name="AKshay"

    def __info(self):
        print("Student 1 Details =",self.__name)

    def info2(self):
        self.__info()

s1=Student1()
s1.info2()

print("====================================")