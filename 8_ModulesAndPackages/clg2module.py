
def student1(name1,age1):          #function with parameter
    print("Student1 Name=",name1)
    print("Student1 Age=",age1)

def student2(name2,age2):          #function with Parameter
    print("Student2 Name=",name2)
    print("Student2 Age =",age2)

class Clg2:

    @staticmethod
    def student3(name3,age3):
        print("Static Method with Parameter Executed from clg2module")
        print("Student3 Name=", name3)
        print("Student3 Age =", age3)

    @staticmethod
    def student():
        print("Static Method without Executed from clg2module")