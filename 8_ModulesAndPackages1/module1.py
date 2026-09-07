from pydoc_data.module_docs import module_docs


def studentinfo(FName,LName):                  #function with Parameter
    print("Student Name =",FName,LName)

def addition(num1,num2):             #function with Parameter
    print("Addition =",num1+num2)

def loop():                                  #function without parameter
    mark=20
    if mark>=35:
        print("Result = PASS")
    else:
        print("Result = FAIL")

class Abcd1:                                 #class
    def mul(self):                          #Non-Static Method without parameter
        x=10
        y=20
        print("Multiplication =",x*y)

    @staticmethod                       #Static Method without Parameter
    def addition():
        p=30
        q=40
        print("addition=",p+q)
